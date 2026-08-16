---
conversion_metadata:
  converted_at: "2026-07-22T11:50:08Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Al Lawati et al.pdf"
  source_pdf_sha256: "80ce0e7752bc9ca8dc1d90ba6be0a269bcf30d54b9e9194ae798fc13c040d5aa"
  page_count: 21
  markdown_char_count: 244783
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 17 April 2025, accepted 5 May 2025, date of publication 13 May 2025, date of current version 2 June 2025.

Digital Object Identifier 10.1109/ACCESS.2025.3569609

An Integrated Preprocessing and Drift Detection
Approach With Adaptive Windowing for Fraud
Detection in Payment Systems

HADI M. R. AL LAWATI1, ANAZIDA ZAINAL 1,2,
BANDER ALI SALEH AL-RIMY3, (Senior Member, IEEE), MOHAMMAD AL-AZAWI4,
MOHAMAD NIZAM KASSIM5, SULTAN AHMED ALMALKI 6,
AND TAMI ABDULRAHMAN ALGHAMDI 7
1Faculty of Computing, Universiti Teknologi Malaysia (UTM), Johor Bahru 81310, Malaysia
2Anti-Financial Crime Laboratory, Faculty of Computing, Universiti Teknologi Malaysia (UTM), Johor Bahru 81310, Malaysia
3PAIDS Research Center, School of Computing, University of Portsmouth, PO1 3HE Portsmouth, U.K.
4Gulf College, Muscat 133, Oman
5National Anti-Financial Crime Centre (NFCC), Putrajaya 62100, Malaysia
6Computer Department, Applied College, Najran University, Najran 66462, Saudi Arabia
7Computer Science Department, Faculty of Computing and Information, Al-Baha University, Al-Baha 65779, Saudi Arabia

Corresponding author: Anazida Zinal (anazida@utm.my)

This work was supported in part by the Malaysia Ministry of Higher Education under Grant R.J130000.7851.5F477.

ABSTRACT As fraudulent transaction methods evolve rapidly; it becomes progressively more challenging
to detect them in payment systems. Static machine learning and rule-based traditional detection methods
cannot capture all the dynamic and evolving nature of fraudulent behaviors, resulting in lower detection
accuracy and a higher false positive rate. This study proposes a complete framework that brings together
advanced data preprocessing, effective drift detection, and a reliable detection model to address these issues.
The method uses Mutual Information and SelectKBest for selecting important features, applies ADASYN to
handle class imbalance, and adopts Convolutional Neural Networks (CNN) to capture complex transaction
patterns. By implementing Early Drift Detection Method (EDDM) and ADaptive WINdowing (ADWIN),
the drift can be detected in advance and the system can respond to changes, both gradual and sudden.The
framework was evaluated on three datasets, including real-world transactions and mixed-data environments,
achieving superior accuracy, precision, and drift detection rates, with values up to 99.99% accuracy and
1.0 respectively. The findings show that the framework can adjust to changing patterns of fraud, reduce
false positives, and enhance detection performance. These insights demonstrate the significance of dynamic
pre-processing and drift-aware approaches in the context of real-time fraud detection. This also serves as a
basis for future work in adaptive fraud detection model research areas such as of integrating online learning
for improved speed and efficiency in high-frequency transactional environments.

INDEX TERMS Banking fraud, payment systems, prepaid cards, debit cards, credit cards, fraud detection,
concept drift, class imbalance, data pre-processing, supervised feature selection, deep learning, drift detec-
tion, real-time fraud detection.

I. INTRODUCTION
Nowadays financial fraud has become one of the big issues
faced by the banking industries [1]. Fraud can be defined

The associate editor coordinating the review of this manuscript and

approving it for publication was S. K. Hafizul Islam .

as any activity carried out with the intent of gaining profit
through deception. Basically, fraud is an illegal method for
fraudsters to get funds and goods. Hence the goal of the
fraudsters is to get the product without paying the amount
or earning an unauthorized fund from an account. Techno-
logical advancement has led fraudsters to try new methods

92036

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/

VOLUME 13, 2025

---

<!-- PAGE 2 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

to accomplish their goals. As a result, fraud incidents are
increasing, therefore, the need to protect systems from fraud
has become evident.

A payment system processes transactions between a cus-
tomer (issuer) and a merchant (acquirer) without a complex
process or cash, generally by cards or electronic money.
Transactions fall into card-present (CP) requiring physical
presence and input of PIN (e.g. ATM, POS) and card-not-
present (CNP) occurring online (e.g., e-commerce). CNP
transactions are a bit more prone to fraud since they can
involve stolen card information. As payment volumes rise,
so do instances of fraud [3].

Nowadays companies and banks are spending millions
on Know Your Customer (KYC), Fraud Systems, and Anti
Money Laundering (AML) systems, yet the number of fraud-
ulent transactions is increasing [3]. Based on the Nilson
Report, in 2019 there were gross fraud losses on Card-based
payments which are around $28.65 billion, amounting to
6.8¢for every $100 of total volume [3].

According to the Merchant Savvy website, global losses
were 9,84$ billion in 2011 and keep growing till it is expected
to reach 40.63$ billion in 2027 which is 25% higher than
in 2020 [4]. Another statistic shared by the Merchant Savvy
website is related to the methods of compromise used by
fraudsters for different countries and the top value for each
country was related to CNP transactions. Although there are
many technologies designed and implemented to enhance
fraud in payment systems, these techniques have not proven
to be effective in protecting authorization and financial trans-
actions from fraudsters. The reason is that the different types
of fraud patterns are evolving which has a real impact on the
implemented technologies to detect fraud [5].

Most of the banking industries use a rule-based approach
to detect fraud in their payment system [6]. With rule-based
fraud detection, the user usually configures a set of rules, such
as account numbers, transaction types, amounts, etc. As part
of the rule configuration, the user can also define which action
the system should take if the transaction matches the rule.
This can include declining the transaction, displaying an alert,
blocking the card, or sending an SMS to the cardholder. Upon
identifying the rule by the user, the rule becomes active, and
fraud is detected when the transaction matches the rule.

Whenever there is a new suspicious transaction, the oper-
ator must verify whether it is fraudulent or otherwise and
update the rules if necessary. The operator’s verification
process is time-consuming and costly for the organiza-
tion. Occasionally, the operator might not check/miss some
transactions until the bank or organization receives a fraud
complaint from a customer. The fraudsters are, swiftly,
and continuously adjusting their patterns and strategies to
deceive.

The increase of e-commerce using various types of pay-
ment including prepaid cards, debit cards, credit cards, etc.,
is evolving fraud patterns so rapidly that the rules-based
approaches cannot be updated fast enough or change quickly,
leading to false positives (blocking good customers) and

inefficiencies in detecting fraudulent transactions [6]. Due
to an increase of sophisticated fraud strategies, traditional
systems no longer produce reliable results [6]. Thus, there is
a need to address this problem.

The disadvantages of rule-based systems has motivated the
researchers to turn to AI-based approaches as alternatives
such as Machine Learning and deep learning [7]. Fig. 1 shows
the difference between the rule-based and machine learning-
based in the context of fraud detection systems. Rule-based
systems depend on predefined rules. Therefore, these systems
fail to reveal the latest patterns and its variants because they
work on pre-defined rules. This limitation makes it difficult
to address emerging tactics in the fraud space and the system
performance may reduce when deals with rapidly evolving
fraud tactics. However, machine learning techniques exploit
data to learn autonomously and identify complex patterns,
which improves the accuracy of fraud detection [6], [48].
Machine learning has emerged as a powerful tool for fraud
detection, as these models can continuously adapt to new data
and learn from subtle patterns and deviations [48].

FIGURE 1. Behaviors in rule-based fraud detection system and ML fraud
detection system [3].

There are different ML techniques proposed in different
studies and each technique has its own advantages and disad-
vantages. ML techniques such as Support Vector Machines
(SVM) are used in fraud detection, but they are not suitable
for large data sets due to their high training complexity [8].
Hence with a large number of transactions such as in banking,
this technique might not be practical to be implemented.

[9], [10] utilizes KNN for some of the analysis. The KNN
requires clustering and would not work well with a large
dataset since calculating distances between data instances
would be very expensive. Furthermore, it is not effective
when there is a high degree of dimensionality because the
process of calculating distance for each dimension becomes
complex. KNN is also sensitive to data that is noisy and
missing [49]. Furthermore, it involves feature scaling, which

VOLUME 13, 2025

92037

---

<!-- PAGE 3 -->

means all the data should be scaled (normalized, standard-
ized) in the right way [9].

Data pre-processing is essential to prepare data in an
appropriate format for machine learning applications. This
step ensures data quality and accuracy before it is passed
to the machine learning model, enabling the model to per-
form effectively. By refining the data through techniques like
cleaning, normalization, and transformation, pre-processing
enhances the reliability of the input data and significantly
improves the model’s detection performance.

Detecting payment card fraud is critical in the evolving
landscape of payment systems. Several factors influence the
effectiveness of fraud detection measures. One key challenge
is the exponential growth in transaction volumes, which leads
to more complex financial activities. Fraud detection systems
must analyze these high volumes of transactions efficiently
to differentiate between legitimate activities and fraudulent
ones, a task that becomes increasingly difficult with the scale
and complexity of modern payment systems.

Fraudsters exploit vulnerabilities in cards and merchant
systems to carry out unauthorized transactions. While quick
to ensure a smooth
transaction processing is essential
customer experience, it often compromises thorough veri-
fication, leaving systems exposed to fraudulent activities.
Striking the right balance between fast processing and
effective fraud detection is crucial. Robust fraud detection
mechanisms must be designed to minimize fraud risks with-
out impeding legitimate transactions, addressing this delicate
trade-off in a scalable and efficient manner.

The problem characteristics of FDS can be described
into two perspectives which are; challenges in fraud and
limitations of the existing FDS solutions. One of the most sig-
nificant challenges in fraud detection is the constant evolution
of fraud strategies. Fraudsters continually adapt and modify
their methods to bypass fraud detection systems (FDS). For
example, a fraudster may steal a batch of credit card infor-
mation and strategically use it for multiple smaller purchases
across various online retail outlets. These transactions often
mimic the cardholder’s typical spending patterns, making it
difficult for the FDS to identify them as fraudulent. This
dynamic and ever-changing nature of fraudulent behavior
highlights the need for adaptable and sophisticated detection
mechanisms.

The main challenge with detecting fraudulent transactions
is the class imbalance that is present in payment data, in which
legitimate transactions far outnumber fraudulent transactions.
The majority class can lead to bias in models as it becomes
more dominant, and this limits the model’s ability to detect
less frequently occurred creative fraud activities. This works
to study fraud detection systems and improving them.

Another significant trend in fraud detection is known as
concept drift, which refers to the evolving nature of fraudulent
behavior over time. In the context of payment card fraud,
concept drift occurs when fraudsters develop new methods
and tactics to evade existing detection systems. This evolu-
tion can be driven by factors such as the emergence of new

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

technologies, shifts in consumer behaviour, or the develop-
ment of increasingly complex fraud strategies. Concept drift
is not limited to specific timeframes; it can occur gradually
over an extended period or as a sudden, abrupt change. This
dynamic nature of fraudulent activity underscores the need
for adaptive detection systems capable of keeping pace with
these changes.

For example, in those types of systems a fraud detection
model is being trained based on a dataset containing one
year’s worth of transactions. Models learn patterns such as
large purchases, suspicious transactions, or high-frequency
transactions. The system successfully flags transactions that
exhibit these patterns as potentially fraudulent. However, over
time fraudsters adapt and change their methods. To evade
detection, they also find that smaller, less-obvious purchases
or stolen credit card information to shop online may defeat
the detection system. Hence, the pattern of fraudulent trans-
actions are changing and a new set of features and rules may
not be able to detect the different types of frauds.

To summarize, issues in fraud detection in payment sys-

tems can be categorized as follows:

A. HIGH OVERHEAD AND CLASS IMBALANCE
Many researchers have applied machine learning and deep
learning to detect fraudulent payments, but their effective-
ness is often hindered by redundant and irrelevant features,
creating overhead. For example, features like exchange rates,
billing currency, or account numbers are unrelated to fraud-
ulent activity, as fraudsters typically exploit card numbers.
Reducing this overhead through targeted feature engineering
can significantly enhance detection accuracy and improve the
efficiency of fraud detection systems (FDS).

Furthermore, card payment fraud is difficult to detect due
to the highly imbalanced nature of the dataset [15]. As shown
in Fig. 2, the credit card dataset contains a large number
of positive instances (normal transactions) and only a small
number of negative instances (fraudulent transactions) [17].
Due to this imbalance, classical classification methods per-
form poorly [16], as machine learning models are biased
toward the majority class, which misclassifies the minor-
ity class (fraudulent transactions) [18]. This can be solved
by reducing the data complexity prior to processing, which
can be significant, allowing accurate and effective fraud
detection.

Despite the highly imbalanced nature of Credit Card in
which the positive instances make up only 0.17% of the
total instances, the prediction is never 100% accurate due
to the separability of features. Many features, in particular
anonymized attributes (V1 to V28) have overlapping classes
between fraudulent and non-fraudulent classes, resulting in
infeasible model-perfectly distinguish classes. In general
transactions, each fraudulent transaction shows similar fea-
ture distributions as that of legitimate transactions as they
try to blend in with the normal activities in order to avoid
being detected. Unfortunately, occasionally this overlap leads
to misclassification of points, even with balanced data and

92038

VOLUME 13, 2025

---

<!-- PAGE 4 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

FIGURE 2. Among the credit card data datasets, 284806 transactions
show statistics of 0.17% fraud (i.e., a small percentage of the transactions
fall into the fraud class [40].

feature selection. In addition, adding noisy or non-informative
features also impedes the ability to separate classes. These
hurdles can be addressed with extensive preprocessing like
data cleansing to eliminate noise/inconsistencies in the first
step, balancing in the second and lastly feature selection to
maintain only the most significant features. These measures
greatly enhanced the model’s capability to recognize dis-
tinguishing patterns and mitigate the effects of overlapping
classes. This produced preprocessed datasets will be more
suitable and it can be utilized for the later stage.

There are different studies [13], [27], [42], [43], [44] to
tackle class imbalance. Some of them proposed to use over-
sampling and some of them proposed under-sampling. A key
difference between these two methods is that under-sampling
moves instances from the majority class into the minority
class to balance the data set while oversampling replicates
the minority class instances to balance the dataset [19]. The
drawback of each method is that under-sampling leads to the
loss of potentially relevant information, causing the model
to perform poorly while if the imbalance ratio is high, over-
sampling introduces the disadvantage of overfitting and an
additional computational cost [19].

Existing studies [2], [11], [13], [26], [27], [28] face
limitations in pre-processing, often lacking thorough data
cleansing, leading to incorrect AI model predictions and
degraded performance. Some approaches use feature selec-
tion without clearly demonstrating the value or stability of
the chosen features. Additionally, class imbalance handling
is frequently applied after data preparation and feature selec-
tion, reducing the overall efficiency of the process.

B. HIGH FALSE POSITIVE
Customers’ habits change over time, and so do fraudsters’
strategies — this is known as Concept Drift [22]. The perfor-
mance of FDS degrades when these patterns keep changing
and evolving. Concept drift, a widely studied phenomenon
in data streams, significantly impacts the performance of
machine learning models, including fraud detection systems.
It occurs when the statistical properties of data change over
time, creating a mismatch between the model’s training
data and new incoming data. In credit card fraud detec-
tion, concept drift often arises from evolving fraud tactics,

shifting user behaviors, or changes within the payment
ecosystem.

Concept drift and its effect on the effectiveness of exist-
ing fraud detection systems has been studied by several
researchers. For example, [20], [21] showed that concept drift
in credit cards can result in a higher rate of false alarms, and
therefore the model fails to adapt itself to changes in fraud
pattern in real-time. In another case [28], [47] reported lack
of timely detection as well as handling stating that static fraud
of concept drift compromised the fraud detection accuracy
resulting in higher false positive rates.

Research highlights that concept drift is a persistent issue
in credit card fraud detection, significantly contributing to
increased false alarm rates over time. Studies [28], [29] show
that static fraud detection models struggle to adapt to evolv-
ing patterns, leading to performance degradation. Lee [30]
emphasized the importance of detecting and managing con-
cept drift to preserve model performance and reduce false
alarms. Addressing concept drift is essential for maintain-
ing detection accuracy, minimizing operational costs, and
improving user experience, making it a critical factor for
effective fraud detection systems.

Fraudsters’ strategies continuously evolve, making fraud
detection systems (FDS) essential to detect new patterns
promptly. As a result of static rules and outdated models that
do not address the ever-changing nature of fraudulent behav-
ior, current solutions have poor detection accuracy and high
false alarm rates. In addition, the high operational overhead of
large datasets with noise and nonfunctional features and with
class imbalance degrades detection performance. Legitimate
and fraudulent payment behaviors can shift significantly over
time, requiring improvements in fraud detection systems. But
current rule based and machine learning based methods can-
not be readily adapted to cope with these challenges resulting
in limitations in both accuracy and reliability.

To solve these problems, this paper uses a combination
of improved processing, feature selection, adaptive resam-
pling and hierarchical concept drift detection. The phase in
pre-processing combines supervised feature selection tech-
niques including Mutual Information with SelectKBest that
will optimize pertinent features, as well as Adaptive Syn-
thetic Sampling (ADASYN) to deal with the imbalance of
classes. Furthermore, to keep it ahead of changes in fraud
behavior a scheme is adopted which detects at micro level the
process shift Adaptable Drift Detection (ADWIN) combined
with Early Drift Detection Method (EDDM) for both smooth
and sudden Changes in transaction pattern are implemented
through a convolutional neural network (CNN), thus improv-
ing the accuracy of fraud detection. The main goal of the
proposed way is to increase efficiency in identifying fraud,
while also reducing false positives and ensuring that detection
performance in constantly changing payment card transaction
situations stays good.

This paper is organized into six sections. The first
section introduces financial fraud, followed by the second
section which gives an overview of related work. The third

VOLUME 13, 2025

92039

---

<!-- PAGE 5 -->

section presents the proposed methodology including all
pre-processing steps and concept drift detection approach.
In this section also, the experimental setup, dataset used and
detailed framework’s technical implementation have been
explained. The fourth section presents results and analysis.
Meanwhile section five briefly describe future work and the
final section concludes the paper, summarizing key findings,
and highlighting the contributions.

II. LITERATURE REVIEW
This section explores the existing studies and works done by
others on fraud detection in card payment systems. A brief
overview of the card payment system and the most com-
mon fraud methods employed by fraudsters is provided at
the beginning of this review. Following this foundational
overview, existing research is analyzed in depth to identify
fraud detection techniques, models, and methodologies. Dur-
ing this process, the review identifies research gaps and areas
for further advancement.

A. PAYMENT CARD SYSTEM
A payment card is an electronic payment card that allows
the cardholder to pay through POSs or withdraw money
through ATMs, or e-commerce websites. Through a network
of connections, card payment systems allow customers to
make payments by card [35]. In the context of card payment,
the payment ecosystem consists of the different players and
their interactions that make the transaction work. The person
using a payment card to purchase something or transact is
known as the cardholder. Payment card issuer also known as
Issuer, it is typically a bank or other financial institution that
issues payment cards to cardholders. These cards are used
by merchants (for example, retailers, or service providers)
as a method of payment for goods or services. Acquirers
are essentially banks or other organizations that partner with
the merchants that accept and approve card payment. At the
heart of this ecosystem are the networks, like Mastercard,
Visa and American Express, which serve as intermediaries
between issuers and acquirers. These networks are responsi-
ble for governing the cards’ usage, laying the ground rules
for where and how cards can be used, instituting fees and
ensuring smooth, secure operations between parties. Fig. 3
shows how the payment card works over the network: A Cus-
tomer performs a transaction on e-commerce, ATM or POS
terminal at the merchant side. This transaction is then sent
to the merchant through the payment system. The merchant
terminal sends the transaction once again to the acquirer’s
payment system. The acquirer processes the transaction and
forwards to the card network. It forwards transaction data to
the issuing bank for approval or denial. The card network
sends the response back to the issuing bank. The card network
then routes the response back to acquirer, who would have
either approved or rejected the transaction based on whether
issuer approved or not.

There are three main types of payment cards: debit cards,
credit cards, and prepaid cards. A debit card is linked

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

FIGURE 3. Payment card over the network.

directly to the cardholder’s bank account, such as a savings
or checking account. When the customer uses the card for
transactions, the amount is immediately debited or credited to
their bank account. A credit card, on the other hand, is linked
to a shadow account, allowing the customer to borrow funds
up to a pre-approved credit limit. The customer can use the
card provided they pay their monthly dues. If payments are
delayed, interest or late fees are charged. A prepaid card,
also known as a pre-loaded card, is not tied to a bank account.
Customers load money onto the card, which can then be used
globally for various transactions such as cash withdrawals,
purchases, or e-commerce. Unlike debit and credit cards, pre-
paid cards can be used by both customers and non-customers.
At the system level, payment processors play a critical
role in facilitating transactions between issuers and acquirers.
They format and process transactions, forward clearing infor-
mation to merchants and card networks, validate transactions,
regulate payment authorizations, and ensure the security of
customer data against fraud and other threats.

B. EUROPAY, MASTERCARD, AND VISA (EMV)
EMV (Europay, MasterCard, and Visa) is a global standard
for secure payment processing using smart card technology.
It is named after the three companies that developed the
initial chip technology embedded in EMV cards. These chips
securely store and process cryptographic information during
transactions, reducing fraud risk and ensuring global consis-
tency in payment processing standards, terminal behavior,
and communication protocols.

EMV transactions are categorized into two types:
1. Contact Transactions: The chip card is physically
inserted into a terminal reader, such as an ATM, POS
system, or other compatible devices.

2. Contactless Transactions: The card is tapped on a
terminal’s contactless reader, and data is exchanged via
Near Field Communication (NFC).

An additional layer of security for contactless transactions
is tokenization, which replaces sensitive card information
with a unique token, further safeguarding the transaction from
fraud [37].

C. TRANSACTION TYPES
There are two types of transactions which are card-present
(CP) and card-not-present (CNP).

92040

VOLUME 13, 2025

---

<!-- PAGE 6 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

• CP transactions: transactions are those in which pay-
ment details are captured in person, at the time of
sale. This occurs when cards are physically tapped
via NFC, swiped over POS, or dipped into the ter-
minal CHIP’s reader to process transactions with the
EMV [38]. Hence the Customer needs to physically
insert or tap the Chip on the ATM for Cash Withdrawal,
POS for purchase transactions, etc. [3]. The following
are examples of CP transactions [39]: POS terminals
with EMV Reader, Contactless terminals, CHIP card
readers connected to smartphones

• CNP transactions: Cardholders who are not physically
present when a transaction is conducted are considered
Cards-Not-Present (CNP). In the present day, remote
order transactions are the most common. This can
be done over the phone, by fax, on the web, or by
mail [38]. The CNP means is unlike Card-present trans-
actions in which the transaction can be done online
such as e-commerce transactions and in this kind of
transactions, the fraudster always uses card details such
as card number, expiry date, and CVV2 to perform
transactions [3]. The following are examples of CNP
transactions [39]: E-commerce, shopping carts, sub-
scription or recurring billing, e-invoicing, ordering via
phone and manual entry and the apps that allow mobile
payments without requiring payment card readers.

D. FRAUD IN CARD PAYMENT SYSTEM
Payment card fraud is one of the challenges for businesses
as it involves the illegal use of cardholder data to per-
form unauthorized purchases and transactions. They disguise
unauthorized purchases and fake card as cardholder details,
adapt their behavior and use fraud patterns that can cir-
cumvent security measures. Exploiting vulnerabilities in the
payment system, such fraud results in financial losses and
potential harm to both businesses and individuals.

[46] presented a few types of Fraud in Card Payment:

i. Skimming: Using an electronic or manual imprinting
tool, the fraudster can access the information displayed
on the magnetic stripe. In other words, the fraudster can
skim the card using different tools to read the magnetic
stripe. Fraudsters may use this information in the future
for fraudulent transactions if they gain access to it.

ii. Card Not Present

(CNP) Fraud: As previously
explained, fraudsters can use a card without physically
possessing it by entering card information such as the
expiry date, card number, and CVV.

iii. Fake card: Fake card fraud is usually done using skim-
ming. Fraudsters make a clone mag stripe card with
the same data stored on the original card. The card is
a dummy but is still operational for future transactions.
iv. Lost or Stolen card fraud: For e-commerce or manual
entry transactions, fraudsters can use that card for trans-
actions as no PIN verification is needed when the card
is lost or stolen.

v. Application Fraud: Application fraud is when someone
steals payment card details, however, card ID theft is
not to be confused with this. But fraudsters use the
stolen card details to create a tenth account or make
transactions. This type of fraud is hard to identify.
vi. Fake Merchant Websites (Phishing): The victim of false
merchant websites is similar to phishing fraud, where
the customer is misled into a fake website created
by fraudsters, which closely resembles a genuine site.
To lure the customer into making a purchase, the fraud-
ulent webpage may offer several discounts. When the
transaction is completed, all the card and transaction
information is collected by the fraudsters and used for
fraudulent transactions.

vii. Merchant Collusion: Merchant collusion occurs when
the merchant forwards information related to the card-
holder without the cardholder’s knowledge.

The top three most common types of fraud:

i. Skimming: This involves gathering information from a
cardholder’s magnetic stripe through magstripe reader
or through other skimming tools. This data is also
captured during valid transactions and is then used
for subsequent illegal transactions. However, fraudsters
can use skimming devices on payment terminals like
ATMs to steal sensitive card information.

ii. Card-Not-Present Fraud (CNP): CNP fraud is common
in the online world. The thieves make illicit purchases
online using the card number, expiration date, and
CVV. The fact that e-commerce transactions do not
require the presentation of a physical card may lead
to them being also targeted by fraudsters, who can be
definitively deceiving both financial institutions and
merchants.

iii. Fake Card Fraud: Fraudsters use stolen card informa-
tion—often obtained through skimming—to create
fake payment cards, which are then used for fraudulent
transactions. The stolen data is encoded onto counter-
feit cards, allowing fraudsters to make unauthorized
purchases.

E. EXISTING WORKS IN FRAUD DETECTION
This section presents a review of the literature related to fraud
detection systems (FDS) published from 2015 to 2024. The
review discusses different approaches and methods to detect
fraud done by existing works, highlighting the techniques
used, limitations and their advantages. This section reviews
related works about fraud detection in card payment systems
and it focuses on five main challenges: class imbalance,
concept drift, feature selection, classification techniques, and
drift detection methods. The comparison of past approaches
demonstrates their shortcomings and gives some insights on
how to improve.

Shakya [24] examined the application of ML techniques
in credit card fraud detection, using classification algorithms
like Logistic Regression, Random Forest, and XGBoost.

VOLUME 13, 2025

92041

---

<!-- PAGE 7 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

model for improved performance. This approach integrates
manual oversight with model refinement, enhancing detec-
tion capabilities over time. Fig. 6 shows details of [27]
proposed system.

This study utilized resampling methods (such as Random
Under Sampling, Tomek Links Removal, SMOTE, and com-
binations of SMOTE and Tomek Links) to manage class
imbalance, and the model achieved a high accuracy of
approximately 98%. Shakya’s research provided full exper-
imental details for each machine learning that has been
utilized demonstrating effective handling of class imbalance
and robust classification performance. Fig. 4 demonstrates
the workflow of this model:

FIGURE 4. Fraud detection process flow in Shakya’s [24] proposed model.

Evan [26] proposed a hybrid method combining J48 Deci-
sion Tree, SVM, K-means Clustering, and Random Forest as
shown in Fig. 5. The approach involved clustering similar
data points to detect anomalies and classifying transac-
tions using Random Forest. Fraudulent transactions were
flagged if identified by either model, while unclassified trans-
actions were processed using confidence thresholds. The
two-stage model increased discriminability and provided a
robust detection, as evidenced by high classification accuracy
and robustness.

FIGURE 6. Workflow of the credit card fraud detection system by [27]
using random forest algorithm.

The Adaptive Multi-Layered Model proposed by Yusof [11]
as shown in Fig. 7, comprises four key systems: Authentica-
tion Layer, Behavioural Layer, Smart Layer, and Background
Processing Layer.

The Authentication Layer verifies incoming transactions
based on predefined rules and user profiles from past trans-
actions. Significant deviations trigger further review.

The Behavioural Layer employs fuzzy association rules
and feature selection to handle behavioural ambiguity, gen-
erating a fuzzy score for suspicious activities. High-risk
transactions are flagged based on substantial deviations from
normal behaviour.

In the Smart Layer, transactions are categorized as nor-
mal or priority. Normal
transactions are analysed using
Support Vector Machines (SVM), while high-priority ones
are processed by Gated Recurrent Units (GRU) for more
efficient anomaly detection. Lastly, the Background Pro-
cessing Layer ensures continuous improvement
through
under-sampling for class balancing, periodic model retrain-
ing, and rule updates.

FIGURE 5. Proposed credit card fraud detection system by Evan [26].

In Shmatko’s study [27], the Random Forest algorithm
served as the primary classification method for credit card
fraud detection. Transactions were assigned a risk score
(0–100) based on a machine learning model trained on his-
torical data. Transactions below a predefined threshold were
classified as non-risky, while those exceeding the threshold
(e.g., 90) were flagged for manual review. Bank staff could
approve, reject, or further investigate flagged transactions,
with outcomes used to update the dataset and retrain the

FIGURE 7. Adaptive Multi-Layered Model for Credit Card Fraud Detection
by Yusof [11].

Priya & Uthra [25] proposed a deep learning frame-
work, CIDD-ADODNN, to address concept drift and class

92042

VOLUME 13, 2025

---

<!-- PAGE 8 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

FIGURE 8. Workflow of CIDD-ADODNN model with ADASYN balancing
and ADWIN drift detection [25].

imbalance in streaming data. The proposed model is illus-
trated in Fig. 8.

The model combines techniques for preprocessing, imbal-
ance handling, drift detection, and classification. Preprocess-
ing formats raw data, followed by ADASYN to balance class
distribution, improving the detection of minority fraudulent
transactions. ADWIN drift detection is then applied to iden-
tify and adapt to real-time shifts in fraud patterns, triggering
self-updates to maintain high accuracy. The model employs
a Deep Neural Network (DNN) optimized with Adadelta for
precise transaction classification.

In 2017, S. Caxton Emerald and T. Vengattaraman [36]
introduced a model named ‘‘Concept Drift Detection with
Optimal Machine Learning Model for Data Classification.’’
Fig. 9 demonstrates the workflow of this model, starting with
the input training dataset from the KDDCup99 and Spam
datasets.

FIGURE 9. Workflow of the concept drift detection model with optimal
machine learning for data classification [36].

The extracted raw content is then processed further such as
chunk generation, data transformation and format conversion
as a part of data preprocessing to make it ready to be analyzed.
To detect such region shifts over time, the ADWIN (Adaptive
Windowing) model is utilized. During data evolution, this
step is essential to keep model performance.

As soon as drift detection is complete, the data is classified
using a Multilayer Perceptron (MLP) model. The Chimp
Optimization Algorithm further optimizes the model’s per-
formance by fine-tuning the classifier parameters to produce
more accurate predictions. Afterwards, the classification out-
put is evaluated, and the model’s performance is validated.

The model’s strength is its incorporation of a drift detec-
tion mechanism. ADWIN can efficiently identify sudden
drifts, allowing the model to adapt quickly to sudden changes
in transaction patterns. The enhanced Chimp Optimization
Algorithm ensures this model is also fine-tuned, paving
the way for optimal performance by improving the classi-
fier hyperparameter, thereby enhancing not only accuracy
but also the adaptability to evolving trends in credit card
fraud [36].

Reference [42] proposed an adaptive classifier framework
to address concept drift and class imbalance in streaming
data environments. The framework integrates drift detection,
class imbalance handling, and classification into a cohesive
workflow. It begins with preprocessing streaming data to
prepare it for further analysis.

Drift detection is achieved using ensemble-based resam-
pling and statistical methods like Kullback-Leibler (KL)
divergence and Cramer’s V statistic to identify changes in
data distribution. To address class imbalance, the framework
employs adaptive oversampling of minority class instances.
This ensures the model remains effective by retraining with
augmented instances that reflect the latest data distribution.
Classification is enhanced using robust ensemble methods
such as Random Forest, Bagging, LightGBM, and XGBoost,
which are particularly effective in handling noisy and com-
plex data with outliers.

This approach offers improved adaptability and pre-
diction accuracy, making it well-suited for dynamic and
complex environments. However, the computational com-
plexity of ensemble methods and adaptive resampling could
pose challenges in high-frequency or resource-constrained
applications.

The methodology proposed by Kajal and Kaur [43]
addresses class imbalance in datasets through resam-
pling techniques and feature selection. Preprocessing the
data before applying classification algorithms combines
Near-Miss undersampling with Information Gain. Feature
extraction and balancing of the dataset are the first steps in
the workflow.

In the proposed method, the Near-Miss undersampling
technique is used to equalize the number of instances in fraud
and non-fraud classes. As a result of Information Gain, the
most relevant attributes are identified, thus reducing compu-
tational complexity and improving model performance. The

VOLUME 13, 2025

92043

---

<!-- PAGE 9 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

classification method was divided into the Naive Bayes and
Decision tree algorithms with Decision Tree giving the better
results. Using Information Gain the Decision Tree classi-
fier with selected 18 features accuracy, precise, recall, F1
achieved at 97% This is much better than Naïve Bayes which
gets 90% for all these metrics. The adoption of proposed
methodology has been validated in context with European
Cardholder dataset, which thus gives the potential of pro-
posed methodology in prediction of better accuracies with
respect to handling highly imbalanced data.

The model designed by Saraf and Phakatkar [44] is an
ensemble model for fraudulent detection of credit cards. They
consider class imbalances as well as changing fraud trends.
Fig. 10 shows that the proposed bagging–boosting workflow
improves the accuracy of different models. Data preprocess-
ing involves the cleaning of data, outlier removal using the
interquartile range (IQR) approach, and oversampling of the
highly imbalanced datasets with the SMOTE technique.

to changing fraud generative patterns. Joshi et al. [51] use
architecture of ensemble learning-based credit card fraud
detection model shown in Fig 11. It starts with the Preprocess-
ing phase where transaction data in a raw form is cleaned up
and processed. Since the dataset is heavily imbalanced, under
sampling is used to reduce the number of data instances in the
majority class, therefore making the dataset more balanced.
The phase of Splitting Dataset slices the dataset into fea-
ture variables (independent) and target variables (dependent).
Data ports from the Data Preparation to Apply Classifiers
stage, where classifiers (e.g. Decision Tree, Logistic Regres-
sion, Naive Bayes) are applied. Apply Voting is a hard voting
mechanism used to obtain the predicted class label, which is
class with most predictions. Within the Evaluate Efficiency
phase, some metrics (Accuracy, F1 score, Precision, and
Recall) are used to evaluate how the model performs. This
is an ensemble method, to augment the model (which might
have had high class imbalances) on the top of classifiers
capabilities.

FIGURE 10. Workflow of the hybrid ensemble model for credit card fraud
detection with smote balancing [44].

In classification phase hybrid ensemble, which combines
Random Forest and AdaBoost. The Random Forest is an
ensemble of decision trees trained on bootstrapped sam-
ples (with replacement) with an aggregated result, making it
robust to overfitting, while AdaBoost performed on weighted
voting focusing on misclassified instances to improve clas-
sification performance. Model with the hybrid ensemble
outperformed Logistic regression Precision, Recall, and
F1-Score are 1.00, 0.94, and 0.97 respectively by using the
hybrid model, on the European credit card dataset, while on
the Credit Card Stimulation dataset similar improvements are
obtained. They described two datasets, the European dataset,
and the stimulation dataset,
that yielded precision-recall
curves areas of 98.26% and 99.37%, respectively, supporting
the model efficacy.

Similarly, Joshi et al. [51] proposed hard voting to identify
fraudulent transactions by integrating multiple classifiers for
credit card fraud detection using Decision Tree, Logistic
Regression, and Naive Bayes. However, their model outper-
formed individual classifiers, and was able to detect fraud
with higher accuracy. The study also highlighted that ensem-
ble learning models can use different classifiers to overcome
the difficulties of class imbalance. The caveat of this method
is that it is not sufficient where there is concept drift, as it does
not take into consideration the need for real-time adaptation

FIGURE 11. The process flow diagram for ensemble learning based credit
card FDS. [51].

Singh et al. [12] used Random Forest classifiers for detect-
ing fraudulent credit card transactions and addressed a class
imbalance problem with Synthetic Minority Over-sampling
Technique (SMOTE). Their approach provided a complete
preprocessing mechanism including outlier removal, nor-
malization, and feature scaling so that the model could be
applied efficiently. The SHAP values variably represented
the contribution of each feature to the model’s output, which
enabled the interpretable model and increased confidence in
the model predictions. Singh et al. [12] to verify the relevance
of individual features in fraudulent detection, making sure
that the model not only attained great performance but also
added insights for improving the system of fraud detection.
The proposed method achieved 98.5% accuracy with very
high precision and recall rates, also outperforming baseline
models.

This literature review of fraud detection systems (FDS)
between 2015 and 2024 discusses major contributions and
denotes the gaps in existing models. While the reviewed
papers addressed issues such as class imbalance, concept
drift, and feature selection, it did not sufficiently enhance
model adaptability and real-world applicability. Feature
selection was neglected in many works so that the huge
dimensions with irrelevant features (like Shakya [24] and
Evan [26]) were increasing the computational cost. Methods
like SMOTE and Tomek Links addressed class imbalance,

92044

VOLUME 13, 2025

---

<!-- PAGE 10 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

but introduced synthetic noise that led to overfitting and
loss of generalizability. Furthermore, many models like
Shmatko’s [27] required manual feedback for data entry,
hampering transaction processing speed and system adapt-
ability as the project progressed.

Finally, concept drift is a persistent challenge in fraud
detection given that transaction behavior is dynamic and
can change with seasonality, new fraud techniques, and
consumer behavior. The traditional models (e.g., Logistic
Regression, Decision Trees, Random Forest, and XGBoost)
assume that data distributions do not change over time. This
assumption does not hold true for real-life payment systems,
where a sudden or gradual drift can occur, significantly
reducing the effectiveness of static models. Concept drift
can be categorized into two types: abrupt drift, where data
patterns change suddenly, and gradual drift, where transac-
tion behavior evolves incrementally over time. or instance,
seasonal spending variations or subtle shifts in merchant
categories may gradually alter the decision boundaries of
a model, making previously effective classification rules
obsolete. Gradual drift is particularly problematic since it
causes the performance of the detection to gradually decrease
over time. As these changes happen unnoticed, the model
keeps applying old rules and hence, a lot of false positives
are left unnoticed leading to worse and worse accuracy.
Models based on ADWIN [36] can detect abrupt drift with-
out needing an initial reference set, and as such can be
prone to lose gradual and subtle changes, causing miss-
ing patterns of potential frauds and degradation in model
performance. Similarly, Mulimani’s [42] approach, which
integrated ensemble-based resampling with drift detection via
KL divergence and Cramer’s V, ensured robustness but was
more computationally expensive, preventing it from obtain-
ing real-time processing.

The study by S. Joshi et al. In [51] proposed an ensemble
learning approach where Decision tree, Logistic regressor
and Naive Bayes classifiers are applied independently and
are then combined through hard voting to detect fraud in
credit cards transactions. These results show that an ensemble
method was found to yield higher accuracy as compared to
any single classifier in prediction of fraudulent activity. The
only limitation of this approach is that hard voting is used
so no adaptive or incremental learning strategies for concepts
drift modeling are utilized once new instances are coming.
Furthermore, in dynamic fraud detection scenarios, ensemble
learning techniques might be ineffective because they rely on
a static model architecture and do not easily adapt well to
changes in transaction behavior.

The model proposed by Singh et al. [12] has some limita-
tions. Although SMOTE was able to solve the class imbalance
problem, it also added synthetic noise to the dataset, which
could increase the risk of overfitting to the synthesized
dataset and result in poor generalization to real-world data.
Furthermore, the model is unaware of concept drift, an impor-
tant challenge in credit card fraud detection, as transaction
patterns change over time. If no mechanisms for real-time

adaptation are embedded, the model’s accuracy may degrade
as new fraud patterns emerge. Furthermore, although SHAP
values provided valuable insights into feature importance,
the computational overhead associated with generating these
values and performing extensive hyperparameter tuning may
limit the scalability of the model, making it less practical for
high-frequency transaction environments.

Table 1 summarizes these studies and their respective
techniques as well as the strengths and limitations of the
methods. These results show that, despite various methods to
tackle class imbalance along with drift detection and feature
selection, most of the models were not genuinely adaptive
in real-time, nor did they accommodate the characteristics of
high dimensional datasets or the changing nature of fraud.

Fortunately, the proposed model effectively identifies and
reacts to gradual drift, which supports the mitigation of these
effects. By perpetually adjusting to the changes in the trans-
action behavior, the model minimizes false positive rates
while maximizing detection, mitigating the flaws of classical
convergence and therefore, accommodating drifting detection
models.

Drift is one of the most important factors that affect
detection performance. Fraudsters regularly modify trans-
action characteristics (like transaction values, retailer types
or geographical areas), moving the decision boundary of
the prototype overtime. If no drift detection is in place, the
models trained on historical data will become stale and inac-
curate, which inherent in minimization of detection accuracy
at higher levels specifically increase in false-positive and
degradation detection performance. Now think about push-
ing this process one step back in the chain and start using
drift-detection in a more proactive way so that you can make
your models with dynamic transaction permutations to learn
and adapt continuously. As an example, algorithms that can
detect gradual drift, such as EDDM, can be integrated with
popular algorithms to capture abrupt drift, such as ADWIN,
so that both types of drift can be detected comprehensively.
Deploying these strategies ensures that the model keeps pace
with evolving fraud patterns, maintaining a balance between
detection accuracy and adaptability. Previous models faced
difficult challenges with the complexity of the dataset as
many of them utilized numeric-only tabular datasets such as
KDDCup and Credit Card datasets, which limited its applica-
bility to real data, which is predominantly transactional and
mixed (k+ numeric).

An ensemble approach was employed by Priya and
Uthra [25] and Saraf and Phakatkar [44] to combine classifier
outputs and increase classification accuracy but came with
steep computational overheads and the potential for synthetic
noise. Moreover, Kajal and Kaur’s method [43] utilized the
under sampling and Information Gain, but failed to address
nonlinear feature interactions thus their solution is not flexi-
ble enough for real-world scenarios.

To overcome these limitations, a hierarchical feature selec-
tion process with Mutual Information and Feature Importance
is applied to extract and rank relevant features, minimizing

VOLUME 13, 2025

92045

---

<!-- PAGE 11 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

TABLE 1. Summary and comparison of fraud detection techniques in
literature.

the noise and improving classification performance. In addi-
tion, the proposed model is the first to combine EDDM
and ADWIN to work together for dual drift detection to
retain both sudden changes and gradual changes. This model
can therefore adapt dynamically to drift of transactions and
continues to perform detection at a high level. Additionally,
the use of Convolutional Neural Networks (CNN) allows the
model to recognize complex patterns in transactions, guar-
anteeing efficient, real-time fraud detection in ever-changing
environments. The enhancements commence addressing the
broader nature of fraud attempts and the limitations found on
previous approaches, defined the proposed method as a more
flexible and reliable way of acting against fraud.

III. METHODOLOGY AND THE PROPOSED MODEL
This section outlines an approach to developing an improved
methodology to address limitations discussed in the previous
section. Different challenges in fraud detection are handled
in the research, like class imbalance, computational overhead
and performance degradation owing to concept drift. It is
important to go beyond these challenges for a fraud detection
system to become more robust and effective.

This section describes the methodology used to develop
and evaluate the proposed model that is capable of han-
dling concept drift and imbalanced datasets. There were three
distinct datasets utilized, each with unique characteristics
relevant to fraud detection. To ensure effectiveness, accuracy,
and robustness, multiple metrics were used to evaluate the
model’s performance. These steps are explained in detail as
follows:

A. DATASET
The following datasets were selected to test the model’s
ability to detect fraud and adapt to drift in different contexts:
i. Kaggle’s first dataset contains European credit card
transactions from 2013 and is commonly used in fraud
detection research [50]. There are 31 features and
492 instances of fraud within 284,807 total transactions
in this dataset, providing a benchmark for detecting
fraudulent behavior under class imbalances.

ii. Data from a leading bank in the Gulf Cooperation
Council (GCC) region contains 200 features from debit
and prepaid card transactions in 2019. This dataset
provides insights into the model’s performance in an
operational banking environment with 120 fraudulent
transactions out of 66,523 total records.

iii. A third dataset, from the UCI Repository [45], con-
tains labeled email data for spam detection research.
57 features were extracted from email text to provide a
non-financial context for benchmarking concept drift
handling. Using the spam dataset, the proposed drift
detection techniques can be tested in scenarios of grad-
ual and abrupt drift.

A summary of the datasets is shown in Table 2:

92046

VOLUME 13, 2025

---

<!-- PAGE 12 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

TABLE 2. Datasets specifications.

The framework for the research is structured in two parts
in which each stage builds on the findings of the last. Fig. 11
illustrates the designed fraud detection research framework.
i. The first phase of data processing has three steps:
data cleansing, feature selection and resampling. Data
cleansing is the first phase of data quality in which
data gets enhanced and corrected. Data cleansing is fol-
lowed by features selection to select relevant features.
Finally, The Resampling techniques has been utilized
to solve the class imbalance problem and balance the
dataset. Thus, combining these steps enforces efficient
model training and detects fraud accurately.

ii. The second phase deals with concept drift detection.
The use of Convolutional Neural Networks (CNN),
Early Drift Detection Methods (EDDM), and sliding
windows allows the detection of both gradual and
abrupt drifts in data.

FIGURE 12. Proposed methodology for enhanced fraud detection with
pre-processing and drift detection techniques.

B. METHODOLOGY
The methodology proposed consists of two phases: Data
Preprocessing and Detection Model. The goal of each phase

is to tackle the major challenges of fraud detection, including
data quality, relevant features, imbalance between classes and
conceptual drift patterns.

1) PHASE 1 - DATA PREPROCESSING
The purpose of this phase is to prepare the dataset for effective
and accurate model training. There are three steps involved in
the data preprocessing: Data cleansing, feature selection and
handling class imbalance with ADASYN.

Data Cleansing: This step aims to reduce noise and
irrelevant information in a dataset to enhance data quality.
Cleaning the data (missing values and duplicates) and thus,
a dataset that can be analyzed. In payment systems which
contain mixed types of data (i.e., categorical and numerical
features), an integrated strategy is required during the balanc-
ing and feature selection process.

Handling Class Imbalance with ADASYN: ADASYN
(Adaptive Synthetic Sampling) is a method used to deal
with class imbalance, which is especially prevalent in fraud
detection datasets:

i generates synthetic instances of the minority class
(fraudulent), focusing more on regions where learning
is difficult. This helps in balancing the dataset by ensur-
ing that areas with fewer but significant fraud cases are
adequately represented.

ii Adapts sampling to the underlying data distribu-
tion to enhance the model’s sensitivity to fraudulent
transactions.

Thus, Phase 1 is focused on preparing a valid dataset to
improve model accuracy, noise reduction and class imbalance
correction using data cleansing, MI and K-Best feature selec-
tion and ADASYN balancing.

Feature Selection: To minimize the size of the dataset,
Information (MI) and SelectKBest are utilized
Mutual
for better feature selection. MI measures the dependence
between features and targets (fraud/non-fraud), producing
scores that rank the features. SelectKBest then selects only
those with the strongest association to the target variable,
removing irrelevant or redundant ones. This results in a more
accurate and interpretable model by eliminating low-impact
features. Both methods are powerful for fraud datasets. Labe-
lEncoder() is used for ordinal data, while OneHotEncoder()
is applied to non-ordinal categorical data.

2) PHASE 2 - DETECTION MODEL
This phase focuses on building a dynamic model of fraud
detection which would identify fraudulent transactions in real
time with a high degree of accuracy, and most importantly
a model that would look at data patterns that evolve due
to changing tactics of fraud. 3 mechanisms are the building
blocks for the detection scheme; they are Convolutional Neu-
ral Networks (CNN), Early Drift Detection Method (EDDM)
and ADaptive WINdowing (ADWIN).

CNN is further applied as a fundamental classifica-
tion model to identify fraudulent transactions. This model

VOLUME 13, 2025

92047

---

<!-- PAGE 13 -->

automatically identifies complex interrelations in transaction
data which traditional techniques could miss. Training CNN
on the Phase 1 dataset that is refined and balanced helps to
distinguish real transactions versus fraud attempts better.

This method of monitoring the drift or change in the
model’s error on different upcoming batches of data based on
the previous batches of data is termed as Early Drift Detection
Method (EDDM) which can detect changes in distribution
as well as fraudulent behavior. It constantly monitors the
average distance between errors to pick up sudden or gradual
changes in characteristics of transactions. It enables the sys-
tem to respond quickly to new patterns in fraud by sending
alerts when the error rate surpasses predefined warning and
control thresholds.

The adaptive windowing (ADWIN) technique works along
with EDDM to determine drift by adjusting the window
size according to the volatility of recent transaction patterns.
In ADWIN, the window size is dynamically adjusted to
keep the detection model focused on current data trends,
simplifying the process of detecting genuine shifts in fraudu-
lent behavior from temporary abnormalities. Maintaining the
model’s accuracy and minimizing false positives is dependent
on this component.

To address client-level drift and behavioral heterogeneity,
the ADWIN component dynamically adapts its window size
per client transaction stream, enabling localized detection of
shifting behaviors. This ensures that the model remains sen-
sitive to individual user-level changes in spending patterns,
supporting personalized fraud detection in heterogeneous
environments.

Fig. 12, shows a structured approach to fraud detection that
integrates Convolutional Neural Networks (CNNs), Early
Drift Detection Method (EDDM), and ADaptive WINdow
(ADWIN) to continuously observe and adapt to changing
transaction patterns. This framework accommodates both
abrupt and gradual drifts in transactional data in order to
maintain accuracy and be responsive to changing fraud tac-
tics. In the CNN model, data such as transaction amounts,
merchant details, and entry mode are extracted after initial
training. The extracted features are used to detect anomalies
and fraud.

The first step of the detection framework is Initial Model
Training using CNN, where the CNN model is trained with
historical transactional data, which learns complex rules that
differentiate between normal and fraudulent transactions.
This basic step guarantees that this CNN is implemented in
real-time, meaning any incoming transaction can be dynami-
cally classified as a baseline for fraud detection.

After the system is in production, the EDDM (Early Drift
Detection Method) runs and monitors errors of the pre-
dictions in production in near-real-time. EDDM assesses
for potential drift with two levels of thresholds: Warning
Level (0.1) and Out-of-Control Level (0.1). If one of the
significant deviations in the data patterns exceeds the out-of-
control threshold, the EDDM detects the drift and classifies
it as either Gradual Drift or Abrupt Drift. We identify a

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

FIGURE 13. Drift detection Workflow in fraud detection system using
CNN, EDDM, and ADWIN.

gradual drift if the error accumulation exceeds that gradual
threshold, typifying gradual, incremental changes in the data
distribution. In contrast, the drift in bringing to abrupt drift
is sudden — and considerable. At this point, if a drift is
detected, the system retries the CNN model or retrains its
weights to adjust to the changes in the pattern.

If the Out-of-Control Level condition is False, the next
to be evaluated is for the Warning Level. At this point,
EDDM tends to monitor slight changes from the data stream.
In case the warning condition holds True, EDDM trig-
gers ADWIN (Adaptive Windowing) for further validation.
ADWIN explicitly addresses this information gap by deter-
mining whether the observed shifts are true changes in data
distribution or just temporary fluctuations. ADWIN confirms
the drift type by adapting the size of its sliding windows
dynamically and conducting statistical tests. In the occur-
rence of drift detection for the warning phase, ADWIN
classifies the drift type within gradual or abrupt, the same
as for the out-of-control phase. In the case where no drift is
confirmed, the system reverts back to No Drift Detected and
continues monitoring.

In case the warning level and out-of-control levels are not
satisfied, the system will stay on tracking the data stream
where it continues to have EDDM and ADWIN on standby to
detect possible changes. This keeps it from generating false
alarms while being sensitive to both subtle and significant
drifts.

the
Upon confirmation of drift (EDDM or ADWIN),
system updates Drift Detection Metrics and implements nec-
essary actions. In the case of gradual drifts, it updates its
model weights to model the changing data according to the
changes in this data. You are required to perform a complete
retraining process with this CNN model every time it is a
sudden drift, which we want to avoid as stated above. This

92048

VOLUME 13, 2025

---

<!-- PAGE 14 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

iterative process is essential for keeping the system flexible
enough to respond to the evolving patterns of fraud.

Table 3 presents the main components and objectives of
EDDM and ADWIN used in our approach for detecting drift
and updating the model. When a change occurs, the system
returns to the monitoring step and continues analyzing the
data stream for further variations. This approach makes the
system more reliable, keeps accuracy high, and allows it to
adjust quickly to changes in fraud patterns.

TABLE 3. Summary of EDDM and ADWIN parameters for drift detection
and model updates.

C. EVALUATION METRIC
To gain an overall perspective about the model abilities,
different metrics were used to be able to analyze the perfor-
mance of the model. These metrics comprised:

i. Accuracy: Accuracy is the proportion of correctly clas-
sified instances over the total number of instances. Drift
detection in credit card or card payment fraud datasets
requires high classification performance as transaction
patterns evolve over time, making accuracy critical for
successful detection. Nonetheless, even if the model is
highly accurate, that means less in imbalanced datasets
such as this one where the legitimate transactions out-
number the fraudulent ones. High accuracy only tells
you that the model is broadly correct, but does not
mean drift has been detected, nor that minority (fraud)
examples are classified correctly. In addition, accuracy
alone might not reflect the shifts in the distribution of
data resulting from drift, and can cause the model to
degrade if not detected in time.

ii. Precision: Precision is the ratio of correctly identified
positive observations to the total predicted positive
observations. In drift detection uses cases; precision
conveys that change in patterns occurring in fraud
instances due to drift would not lead to nightmare-level
false positives. As drift takes place, fraudsters may
adapt to it by adjusting their behavior, causing trans-
action characteristics to differ. With high precision, the

chance of false positives is decreased, meaning that
fewer legitimate transactions will be flagged as fraud-
ulent, reducing unnecessary alerts and disruptions.
iii. Recall: Recall is the number of relevant instances
(actual fraudulent transactions) retrieved by the model
over the total number of instances that should have been
retrieved (actual fraudulent transactions). So, in the
case of drift detection, a high recall makes sure that the
model adapts as quickly as possible to changes intro-
duced by the concept drift, and do not let undetected
fraudulent patterns manifest. Though drift changes the
nature of fake transactions, having a high recall limits
false negatives (there will be frauds they miss), ulti-
mately holding the system safe from adapting threats.
In drift scenarios, low recall means non-adaptation to
changing patterns, hence the need for constant moni-
toring and retraining.

iv. F1 Score: The F1 Score is the harmonic mean of pre-
cision and recall, which balances the trade-off between
false positives and false negatives. In drift detection,
a high F1 Score indicates that the model has adapted
to the changes in transaction distributions without
sacrificing its flexibility to correctly identify fraud.
Since both precision and recall get affected by drifting
concepts, a high F1 Score guarantees that the model
captures fraudulent transactions without hurting sensi-
tivity or specificity along the evolution of the data.
v. ROC-AUC (Receiver Operating Characteristic - Area
Under Curve): Ther ROC-AUC evaluates a model’s
capacity to separate fraudulent transactions from legit-
imate ones at various threshold levels. ROC-AUC is
critical in drift detection as it serves to assess how well
the model identifies a supervisory signal so that the
classification boundaries shift dynamically with drift.
This means the significantly high ROC-AUC value
indicates the model’s ability to determine between
legalized transaction and fraudulent transaction as the
characteristic of the transaction changes over a cer-
tain time. If the ROC-AUC remains consistently high,
this indicates that even as drift affects the underlying
data distribution, the model maintains its discrimina-
tive capability over time and is thus robust to such
change.

vi. Drift Detection Rate: The Drift Detection Rate mea-
sures the model’s sensitivity to detecting changes in
the underlying data distribution over time. With the
prevalence of emerging patterns amongst fraudulent
transactions, detecting drift allows the model to retrain
and adapt to changes in that process quickly. With-
out a high enough drift detection rate, the model can
become outdated speculation, resulting in increased
false negatives (missed fraud) or false positives (false
alarms). Drift detection: The detection of shifts in the
distribution of incoming data.

vii. Confusion Matrix: The confusion matrix divides result
of classification into true positives, true negatives, false

VOLUME 13, 2025

92049

---

<!-- PAGE 15 -->

positives and false negatives (TP, TN, FP, FN). The
confusion matrix can be used for drift detection in fraud
detection models to see how well the model is able to
stay within class prediction accuracy as drift occurs.
Tracking this matrix through time can show whether
the model’s sensitivity to changing patterns of fraud is
getting better or worse, allowing for actionable insights
on retraining and refinement.

The selection of these evaluation metrics was performed in
order to keep high classification performance of the model
while adapting to the concept drift. These metrics together
provide an overview of the model’s performance over time,
focusing on how well the model is performing and how well
it is adapting to changes as they occur.

D. IMPLEMENTATION DETAILS
Fraud detection using various kinds of python libraries tai-
lored for machine learning, data preprocessing and drift
detection were performed in google colab:

i TensorFlow/Keras: used to create Convolutional Neu-
ral Networks (CNN) for investigating complex patterns
in transaction data. CNNs constructs multiple layers:
Conv1D, MaxPooling1D, Dense to learn complex pat-
terns from large amounts of data.

ii TensorFlow/Keras: used to create Convolutional Neu-
ral Networks (CNN) for investigating complex patterns
in transaction data. CNNs constructs multiple layers:
Conv1D, MaxPooling1D, Dense to learn complex pat-
terns from large amounts of data.

iii River: Used for drift detection Because River is
designed for streaming data, this library is utilized
for drift detection. River was used to implement the
EDDM and ADWIN techniques, which perform well
for sudden and gradual changes, respectively.

Table 4 outlines the main code components utilized in each
stage:

IV. RESULTS AND DISCUSSION
This section provides the evaluation outcomes, where Real
Dataset, the Credit Card Dataset, and the Spam Dataset were
utilized in the study to evaluate the model’s performance in
detecting drift and fraud. Before performing the actual exper-
iments, each dataset was optimized to improve the robustness
and reliability of drift detection using ADASYN for class
balancing. Then the features were extracted using Mutual
Information and SelectKBest. Then the integrated approach
of EDDM, ADWIN and CNN was used to evaluate the per-
formance of the model as it drifted.

The findings illustrate the contribution of each feature set
to the model’s performance metrics, which include Accuracy,
Precision, Recall, F1 Score, ROC AUC, Drift Detection Rate,
and False Positive Rate. The evaluation highlights the most
effective feature configuration for each dataset, resulting in
the highest detection accuracy and the ability to adapt to
changing fraud patterns.

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

TABLE 4. Main code components.

A. REAL DATASET
Table 5 illustrates the results obtained over the Credit Card
dataset applying to the ADASYN balancing technique and by
carry on the feature selection process, and also compares the
performance achieved by those predictive models that were
built using different sets of four or fewer distinct features,
accuracy, precision, recall and F1 here too are reported. The
configuration with 90 features yielded the best performance
metrics among those tested, featuring 100% accuracy, 100%
precision, and 100% recall. This indicates that the under-
lying model is detecting fraud with world class sensitivity
and little in the way of false positives or false negatives.
The 10-features (99.99%) and 20-features (99.99%) datasets
also performed very well, achieving high accuracy (99.98%)
and perfect recall, respectively, indicating high efficiency in
identifying a fraudulent transaction.

However, while fewer features performed well, they might
not retain all important fraud-related patterns and this could
affect generalizability. High scoring sets across every metric
occurred at features 30, 50, and 80, indicating the optimal
selections of features. 40, 60 and 70 features were also found
that could be highlighted but they were not balance metrics as
metrics were better for Precision and F1 scores. This indicates
that although the majority of feature combinations used, after
ADASYN and feature selection, provided highly positive
results, some combinations —especially at 90 and above—
buoyed an optimal, repeated, and good detection potential.

B. CREDIT CARD DATASET
The performance results of the Credit Card dataset post
feature selection and data balancing is detailed in table 5.
A 30-feature set with 99.88% accuracy, 99.76% precision,
and 100% recall was the most balanced across all metrics

92050

VOLUME 13, 2025

---

<!-- PAGE 16 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

of the tested configurations. In the credit card dataset, the
model accurately detected drift and fraudulent instances with
minimal false positives and false negatives.

All other lower feature configurations (10, 15, 20 and
25 features) all scored well, getting between 0.9901 and
0.9975 for accuracy, and everything including the 10 fea-
tures scored 0.9900 and above for F1. As such, the resulting
30-feature configuration is the optimal combination of accu-
racy and adaptability regarding drift and fraud detection,
through features selection and balancing.

C. ESPAM DATASET
Table 5 presents performance results of Spam dataset; results
after addressing data cleansing, feature selection and data bal-
ancing issues, to illustrate the impact on accuracy, precision,
recall and F1 score. With 55 features, the results showed the
most balanced performance with accuracy 0.9306, precision
0.9262, recall 0.9448, F1 score 0.9354 and ROC AUC 0.9706.
These findings imply that it aids the model to identify spam
instances with significant sensitivity as well as minimal false
positives as well as minimal false negatives in these functions.
Overall, other lower number of features also achieved good
accuracy like 5 and 10 features but significantly lower preci-
sion and F1 score, indicating more false positive cases. The
performance improvement is seen between 15 and 30 feature
counts but the balance achieved by 55-feature configuration
were not found in configuration with less features.

The 55-feature set is the best selection for the Spam dataset,
providing a balanced method for correctly identifying both
spam and non-spam instances with strong precision, recall,
and overall accuracy. The chosen features provide strong
detection efficacy while reducing errors, making it appropri-
ate for dynamic data contexts.

D. DRIFT DETECTION RESULT
The final performance of drift detection was evaluated on
the datasets using EDDM, ADWIN, and CNN methods after
resampling and feature selection. Based on the results of this
evaluation, the model has demonstrated its ability to adapt
to evolving data distributions across a variety of datasets.
The final performance of drift detection was evaluated on
the datasets using EDDM, ADWIN, and CNN methods after
resampling and feature selection. Based on the results of this
evaluation, the model has demonstrated its ability to adapt
to evolving data distributions across a variety of datasets.
Table 6 shows the final performance result

According to Table 6, the feature selection analysis for
the Real Dataset with 90 features, produced the best detec-
tion results with an accuracy, precision and recall rate equal
to 100%. This demonstrates that the model is able to pick
up on shifting transactional behaviors, whether gradual or
sudden. For the Credit Card Dataset, the set of 30 fea-
tures provided 100% accuracy and 100% F1 Score. This
balance maintains high sensitivity while reducing false pos-
itives which is critical to fraud detection. A well-balanced
precision and recall will provide a reliable model in a real

TABLE 5. Result of all datasets during pre-processing stage.

TABLE 6. Result of all dataset during detection stage.

scenario where there is a need to identify fraudulent cases
accurately but also limit false alarms. The Spam Dataset (55
features) achieved 99.34% accuracy, 100% precision, and
98.69% recall, specific to the variant. ’These findings validate
the robust performance of the model to detect differences in
datasets. In addition, the results demonstrate the applicability
of the methodology in more general sense beyond financial
fraud detection, as they highlight its capacity to cope with
changing data distributions.

Figure 14 illustrates the drift detection overlap using Venn
diagram on the Credit Card Dataset. As per the Venn diagram,
the total of 284314 drifts detected on the Credit Card Dataset
as seen from the Venn diagram in Fig. 10 EDDM detected
284,313 drifts, and 100% drifts was detected by EDDM.
ADWIN only uniquely detected 1 drift, which was a gradual

VOLUME 13, 2025

92051

---

<!-- PAGE 17 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

one. There were 476 abrupt drifts and 283,838 gradual drifts.
EDDM shows a high alignment with ADWIN indicating that
EDDM captures all important drifts with only 1 missed drift
(gradual). This demonstrates that EDDM is a sound method
for capturing both the sudden changes and those that happen
more gradually, in this data set.

FIGURE 14. Drift detection overlap for the credit card dataset.

Figure 15 illustrates the drift detection overlap using Venn
diagram on the ESPAM Dataset. As per the Venn diagram,
the total of 2,792 drifts with EDDM capturing 100% of them.
ADWIN did not identify any unique drifts, confirming that
EDDM alone was capable of detecting all critical changes.
The drifts included 75 abrupt drifts and 2,717 gradual drifts.
These results emphasize the effectiveness of EDDM in identi-
fying changes in this dataset, ensuring no drift instances were
overlooked.

FIGURE 15. Drift detection overlap for the ESPAM Dataset.

Figure 16 illustrates the drift detection overlap using Venn
diagram on the Real Dataset. As per the Venn diagram, the
total of 66,402 drifts detected by EDDM. For this dataset,
ADWIN did not identify any distinct drift as like for the
ESPAM dataset. In summary, EDDM achieves 109 abrupt
drifts and 66,293 gradual drifts. Such behavior substantiates
that when functioning with real time events, EDDM is able
toward detect drifts belligerently (observing no omission of
any genuine drifts) which recommends its realism for genuine
application where high compass for drifts is vital.

FIGURE 16. Drift detection overlap for the real dataset.

In most of the datasets, EDDM was able to successfully
capture most of the drifts, including abrupt as well as gradual
concept drifting. ADWIN, on the other hand, proved to find
few drifts missed by EDDM and guaranteed that no major
drift events went undetected. The complementing perfor-
mance of both techniques demonstrates their robustness in
achieving high detection sensitivity together. Utilizing both
EDDM and ADWIN at different stages improves efficiency
without sacrificing either speed or accuracy, making the
approach more suitable for real-time environments.

While the dual-drift detector can enhance its adaptability,
it does cause a small communication and computational over-
head especially in the drift validation steps. Nevertheless, this
is reduced by only updating the model where a drift has been
confirmed.

E. PERFORMANCE COMPARISON
The performance of various drift detection and feature
selection methods are displayed in Table 9 for the Credit
Card dataset. When compared to earlier studies, the pro-
posed model yields superior results in terms of accuracy,
precision, and recall. Table 7 compares results from the
Credit Card dataset with other studies demonstrating the
proposed model enhanced detection of drift and classification
performance.

In Table 8, the Spam dataset results are compared across
studies, emphasizing the current approach’s improved drift
detection and classification performance. The Spam dataset
was selected because it also exhibits concept drift, so it
can be also part of evaluation to confirm the effectiveness
of the technique using different dataset financial and non-
financial datasets. By applying the proposed methodology to
a non-financial dataset with drift, the ability of the proposed
methodology to detect changes and maintain classification
performance across different domains is validated. This high-
lights the adaptability of our approach to datasets where data
distribution evolves over time.

In Table 9, the Real dataset’s high results support the effec-
tiveness of the proposed methodology. As a result, the model
achieved near-perfect detection metrics, such as accuracy of
99.99%, precision of 99.99%, drift detection rate of 99.99%,

92052

VOLUME 13, 2025

---

<!-- PAGE 18 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

TABLE 7. Performance comparison on credit card dataset.

TABLE 9. Result of detection stage using real dataset.

TABLE 8. Performance comparison on SPAM dataset.

However, it is also important to evaluate its stability when
evaluated on various data subsets. K-fold cross-validation
with K=5 was employed to accomplish this. Table 10
presents the outcomes across many test folds, indicating that
accuracy, precision, recall, and F1-score remain consistent.
The model’s performance is not affected by how the data
are split, indicating that it is reliable across different data
distributions.

TABLE 10. Results using 5-fold cross-validation.

demonstrating exceptional robustness in handling complex,
mixed data types.

F. K-FOLD CROSS-VALIDATION
The comparison results earlier showed that the proposed
model achieves better performance than the existing methods.

Table 11 compares the proposed model’s performance,
evaluated using K-Fold Cross-Validation, with existing stud-
ies on the Credit Card and Spam datasets. The results indicate
that the proposed approach achieves higher accuracy, pre-
cision, recall, and F1-score compared to previous methods.
For the Credit Card dataset, the model recorded an accuracy
of 0.99999, surpassing the 0.97000 reported by Kajal et al.
[43]. As a result, the model effectively detected all drift

VOLUME 13, 2025

92053

---

<!-- PAGE 19 -->

occurrences with a recall of 0.99999. Saraf & Phakatkar [44]
reported a recall of 0.94, which indicates that certain dis-
tribution shifts may have been missed. Using the Spam
dataset, the proposed model was able to recognize evolving
patterns with an accuracy of 1.0. The precision and recall
scores further highlight the model’s capability to detect spam
while minimizing false positives. These results reinforce the
effectiveness of the proposed model across different datasets.
The consistent performance across various K-Fold validation
splits confirms its robustness and adaptability to different data
conditions.

TABLE 11. Comparison of K-fold cross-validation and existing works.

V. FUTURE WORK
Despite the good drift detection capabilities on various
datasets of the current framework, it still does not support
direct real-time learning based on changing fraud patterns.
To solve this challenge, the adaptive learning model was
developed in Phase 3, including the online learning mecha-
nism with the SGD and a dynamic ensemble with LightGBM.
This improvement allows the model to adapt to new trans-
actional data incrementally without having to retrain over
the whole dataset, which is crucial when deployed in high-
frequency, concept-drifting applications like fraud detection.
In the future, it is planned to investigate enhancements for this
architecture using privacy-preserving methods (i.e., federated
learning) to enable joint detection of fraud across institutions
and protect sensitive data. Further, lightweight model archi-
tectures will also be explored to minimize computational and
communication overhead to improve the responsiveness and
scalability of the system in real-time applications.

VI. CONCLUSION
The present study presented an organized framework for
drift detection and fraud identification, with performance
evaluated via several datasets: Credit Card, Spam, and Real
datasets. In summary, the incorporation of Mutual Infor-
mation with SelectKBest feature selection, ADASYN for
data balance, and advanced drift detection via EDDM and
ADWIN provides a robust and flexible method for dynamic
data environments. The proposed framework achieved 100%
accuracy and a 100% drift detection rate on the Real
dataset, demonstrating significant sensitivity and specificity
for real-world fraud detection in both numeric and mixed-
data contexts. This approach is obvious, comprehensible,

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

customized for real-time applications, in contrast to intri-
cate ensemble models. The ability to adapt conducts future
research, especially for integrating online learning to enhance
adaptability to changing fraud patterns in both financial and
non-financial sectors.

REFERENCES

[1] A. K. Mishra, A. Pandey, and S. Anand. (Oct. 2019). A Review on Credit
Card Fraud Detection Using Machine Learning. [Online]. Available:
https://www.researchgate.net/publication/336552027_A_Review_On
_Credit_Card_Fraud_Detection_Using_Machine_Learning

[2] BitEffect. Payment Systems: Principle of Operation and Opportuni-
ties. [Online]. Available: https://biteffect.net/payment-systems-principle-
of-operation-and-opportunities/

[3] SDK Finance. Detecting Payment Card Fraud with Machine Learning—
H2O Driverless AI Kaggle Dataset. Accessed: Dec. 14, 2024. [Online].
Available:
https://sdk.finance/detecting-payment-card-fraud-with-
machine-learning-h2o-driverless-ai-kaggle-dataset/

[4] Merchant Savvy. (2023). Payment Fraud Statistics 2023: Trends, Data, and
Insights. [Online]. Available: https://www.merchantsavvy.co.uk/payment-
fraud-statistics/

[5] H. Zou, ‘‘Analysis of best sampling strategy in credit card fraud detection
using machine learning,’’ in Proc. 6th Int. Conf. Intell. Inf. Tech-
nol., New York, NY, USA, Feb. 2021, pp. 40–44. [Online]. Available:
https://dl.acm.org/doi/fullHtml/10.1145/3460179.3460186

[6] Mitek Systems. How Does Machine Learning Help With Fraud
Detection in Banks. Accessed: Dec. 23, 2024. [Online]. Available:
https://www.miteksystems.com/blog/how-does-machine-learning-help-
with-fraud-detection-in-banks/

[7] A. Arya. (7, 2024). Fraud Detection Using Machine Learning Algorithms.
[Online]. Available: https://intellipaat.com/blog/fraud-detection-machine-
learning-algorithms/?U.S.#::text=Manual%20Review%20and%20
Transaction%20Rules,-Nowadays%2C%20Machine%20Learning&amp;
text=Previously%2C%20industries%20were%20using%20a,detection
%20to%20ML%2Dbased%20solutions

[8] D. Kumar. Top 4 Advantages and Disadvantages of Support Vector
Machine (SVM). Accessed: Dec. 23, 2024. [Online]. Available: https://
dhirajkumarblog.medium.com/top-4-advantages-and-disadvantages-of-
support-vector-machine-or-SVM-a3c06a2b107

[9] A. Soni. Advantages and Disadvantages of KNN. Medium. Accessed:
[Online]. Available: https://medium.com/anuuz.soni/

Dec. 28, 2024.
advantages-and-disadvantages-of-knn-ee06599b9336

[10] S. Wandre, S. Desai, A. Patel, and H. Lopes, ‘‘Credit card fraud
detection using KNN and naive Bayes algorithm,’’ J. Emerg. Tech-
nol. Innov. Res., vol. 9, no. 4, pp. 327–332, 2022. [Online]. Available:
https://www.jetir.org/papers/JETIR2204420.pdf

[11] T. A. Yusof. Adaptive Model

for Credit Card Fraud Detection.
Accessed: Dec. 23, 2024. [Online]. Available: https://www.researchgate.
net/publication/339585842_Adaptive_Model_for_Credit_Card_Fraud_
Detection

[12] Z. Bawany and A. D. Shanbhag, ‘‘Using machine learning to detect
credit card fraud,’’ in Proc. Int. Conf. Electr., Comput. Energy Tech-
nol. (ICECET), Cape Town, South Africa, Nov. 2023, pp. 1–7, doi:
10.1109/icecet58911.2023.10389421.

[13] A. Taha and S. J. Malebary,

‘‘An intelligent approach to credit
card fraud detection using an optimized light gradient boosting
machine,’’ IEEE Access, vol. 8, pp. 25579–25587, Feb. 2020, doi:
10.1109/ACCESS.2020.2971354.

[14] BINUS. (2022). The Importance of Data Preprocessing for Machine
Learning in E-Commerce. [Online]. Available: https://sis.binus.ac.id/
2022/07/11/the-importance-of-data-preprocessing-for-machine-learning-
in-the-e-commerce-industry/#:text=In%20this%20case%2C%20data%20
preprocessing,
incorrect%20output%20from%20the%20AI

[15] R. A. Mohammed, K.-W. Wong, M. F. Shiratuddin, and X. Wang,
‘‘Scalable machine learning techniques for highly imbalanced credit card
fraud detection: A comparative study,’’ in Proc. Trends Artif. Intell.,
Lect. Notes Comput. Sci. (PRICAI), vol. 11013, Jan. 2018, pp. 237–246.
[Online]. Available: https://link.springer.com/chapter/10.1007/978-3-319-
97310-4_27

92054

VOLUME 13, 2025

---

<!-- PAGE 20 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

[16] D. Singh, S. Vardhan, and N. Agrawal, ‘‘Credit card fraud detection
analysis,’’ Int. Res. J. Eng. Technol., vol. 5, no. 11, pp. 1600–1603,
Nov. 2018.

[17] T. Chioka. The Class Imbalance Problem in Machine Learning. Chioka’s
[Online]. Available: http://www.
:text=What%20is%20the%20

Blog. Accessed: Dec. 20, 2024.
chioka.in/class-imbalance-problem/#:
Class%20Imbalance,class%20of%20data%20(negative)

[18] R. Verma. Class Imbalance: A Classification Headache. Towards Data
Science. Accessed: Dec. 20, 2024. [Online]. Available: https://towards
datascience.com/class-imbalance-a-classification-headache-
1939297ff4a4

[19] M. S. Kraiem, F. Sánchez-Hernández, and M. N. Moreno-García, ‘‘Select-
ing the suitable resampling strategy for imbalanced data classification
regarding dataset properties. An approach based on association models,’’
Appl. Sci., vol. 11, no. 18, p. 8546, Sep. 2021, doi: 10.3390/app11188546.
[20] A. Smith, B. Johnson, and C. Williams, ‘‘Concept drift and false alarm
rates in credit card fraud detection,’’ J. Fraud Detect. Prevent., vol. 15,
no. 3, pp. 178–187, 2021.

strategy,’’

IEEE Trans. Neural Netw.

[21] Understanding Model Drift in Machine Learning. [Online]. Available:
https://www.projectpro.io/article/model-drift-in-machine-learning/871
[22] A. D. Pozzolo, G. Boracchi, O. Caelen, C. Alippi, and G. Bontempi,
‘‘Credit card fraud detection: A realistic modeling and a novel
Learn.
Syst.,
learning
[Online]. Available:
vol. 29, no. 8, pp. 3784–3797, Aug. 2017.
https://re.public.polimi.it/bitstream/11311/1044896/1/08038008.pdf
[23] A. Bifet and R. Gavalda, ‘‘Learning from time-changing data with adap-
tive windowing,’’ in Proc. SIAM Int. Conf. Data Mining, Jul. 2007,
pp. 443–448.
[24] R. Shakya,

‘‘Application of machine learning techniques in credit
thesis, Dept. Comput. Sci., Howard
card fraud detection,’’ M.S.
R. Hughes College Eng., Univ. Nevada, Las Vegas, NV, USA, 2018.
[Online]. Available: https://digitalscholarship.unlv.edu/cgi/viewcontent.
cgi?article=4457&context=thesesdissertations

[25] S. Priya and R. A. Uthra, ‘‘Deep learning framework for handling concept
drift and class imbalanced complex decision-making on streaming data,’’
Complex Intell. Syst., vol. 8, pp. 41–53, 2021, doi: 10.1007/s40747-021-
00456-0.

[26] E. M. H. A. Rubaie, ‘‘Improvement in credit card fraud detection using
ensemble classification technique,’’ Int. J. Nonlinear Anal. Appl., vol. 12,
no. 2, pp. 1255–1265, Jun. 2021, doi: 10.22075/IJNAA.2021.5228.
[Online]. Available: https://ijnaa.semnan.ac.ir/article_5228_bffa45b11
da19bafd8e8431ce1de1e05.pdf
[27] O. Shmatko, V. Fedorchenko,

‘‘Detecting
InterConf,
credit card fraud using machine learning algorithms,’’
vol. 71, pp. 393–403, Aug. 2021. [Online]. Available: https://www.
researchgate.net/publication/354112967_DETECTING_CREDIT_
CARD_FRAUD_USING_MACHINE_LEARNING_ALGORITHMS

and D. Prochukhan,

[28] S. Agrahari and A. K. Singh,

‘‘Concept drift detection in data
stream mining: A literature review,’’ J. King Saud Univ.-Comput. Inf.
Sci., vol. 34, no. 10, pp. 9523–9540, Nov. 2022. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S1319157821003062

[29] C. Brown and L. White, ‘‘The impact of concept drift on fraud detection
performance,’’ in Proc. ACM Int. Conf. Knowl. Discovery Data Mining,
Jun. 2017, pp. 256–268.

[30] S. Lee, J. Kim, and M. Park, ‘‘Adaptive fraud detection using con-
cept drift adaptationm,’’ IEEE Trans. Knowl. Data Eng., vol. 28, no. 9,
pp. 2453–2467, Sep. 2018.

[31] K. Kajal and K. Kaur, ‘‘Credit card fraud detection using imbalance
resampling method with feature selection,’’ Int. J. Adv. Trends Com-
put. Sci. Eng., vol. 10, no. 3, pp. 1693–1699, 2021. [Online]. Available:
https://www.warse.org/IJATCSE/static/pdf/file/ijatcse801032021.pdf
[32] S. Mungase, A. Tikande, S. Bora, P. Zanwar, and A. Pathan, ‘‘Credit card
fraud detection using machine learning framework,’’ Int. J. Innov. Res. Sci.,
Eng. Technol., vol. 7, no. 6, pp. 355–360, Jun. 2020. [Online]. Available:
https://www.ijirset.com/upload/2020/september/104_Tejas_NC.PDF
[33] E. Ileberi, Y. Sun, and Z. Wang, ‘‘A machine learning based credit
card fraud detection using the GA algorithm for feature selection,’’
J. Big Data, vol. 9, no. 1, pp. 1–18, Feb. 2022. [Online]. Available:
https://www.academia.edu/76673761/A_machine_learning_based_credit
_card_fraud_detection_using_the_GA_algorithm_for_feature_selection

[34] R. Powar, R. Dawkhar,

and P. Pratichi,

card fraud
Int. J. Adv. Sci. Res. Eng.
detection using machine learning,’’
Trends, vol. 5, no. 9, pp. 62–67, Sep. 2020.
[Online]. Available:
http://ijasret.com/VolumeArticles/FullTextPDF/546_9.CREDIT_CARD_
FRAUD_DETECTION_USING_MACHINE__LEARNING.pdf

‘‘Credit

[35] Card Payments. Accessed: Nov. 4, 2024.
https://www.psr.org.uk/our-work/card-payments/

[Online]. Available:

[36] S. C. Emerald and T. Vengattaraman, ‘‘Concept drift detection with opti-
mal machine learning model for data classification,’’ in Proc. 6th Int.
Conf. Trends Electron. Informat. (ICOEI), Apr. 2022, pp. 1160–1165, doi:
10.1109/ICOEI53556.2022.9776949.

[37] S. Jain. Guide To EMV—Contact & Contactless Payment. Accessed:
https://sruti-jain.github.io/
[Online]. Available:

Dec.
img/GuidetoEMV-Contact-ContactlessPayments.pdf

2024.

20,

[38] What

is a Card-not-present (CNP) Transaction and Why It Costs
More. Accessed: Dec. 31, 2024. [Online]. Available: https://squareup.
com/us/en/townsquare/what-is-a-card-not-present-transaction

[39] B. Dwyer. What’s the Difference Between Card Present and Card Not
Present?. CardFellow Credit Card Processing Blog. Accessed: Dec. 31,
2024. [Online]. Available: https://www.cardfellow.com/blog/card-present-
card-not-present-definition/

[40] A. Patel. (13, 2021). Beginner’s Guide To Classification Models: Catch
Credit Card Fraud. Codex. [Online]. Available: https://medium.com/
codex/beginners-guide-to-classification-models-catch-credit-card-fraud-
fe5a73a3401f

[41] Cardinity. Payment Flow. Accessed: Dec. 31, 2024.
Available: https://cardinity.com/support/payment-flow

[Online].

[42] D. Mulimani, P. R. Patil, and S. G. Totad, ‘‘Adaptive classifier to address
concept drift in imbalanced data streams,’’ in Proc. IEEE 2nd Int. Conf.
Data, Decis. Syst. (ICDDS), Mangaluru, India, Dec. 2023, pp. 1–5, doi:
10.1109/icdds59137.2023.10434793.

[43] Kajal and K. Kaur, ‘‘Credit card fraud detection using imbalance
resampling method with feature selection,’’ Int. J. Adv. Trends Com-
put. Sci. Eng., vol. 10, no. 3, pp. 2061–2071, May 2021, doi:
10.30534/ijatcse/2021/811032021.

[44] S. Saraf and A. Phakatkar, ‘‘Detection of credit card fraud using a
hybrid ensemble model,’’ Int. J. Adv. Comput. Sci. Appl., vol. 13, no. 9,
pp. 464–474, 2022. [Online]. Available: https://thesai.org/Downloads/
Volume13No9/Paper_53-Detection_of_Credit_Card_Fraud.pdf

[45] UCI Mach. Learn. Repository. (1999). Spambase Dataset. [Online]. Avail-

able: https://archive.ics.uci.edu/dataset/94/spambase

[46] S. Saraf and A. Phakatkar, ‘‘Detection of credit card fraud using a
hybrid ensemble model,’’ Int. J. Adv. Comput. Sci. Appl., vol. 13, no. 9,
pp. 464–474, 2022.

[47] B. Lebichot, G. Marco Paldino, G. Bontempi, W. Siblini, L. He-Guelton,
and F. Oblé, ‘‘Incremental learning strategies for credit cards fraud detec-
tion: Extended abstract,’’ in Proc. IEEE 7th Int. Conf. Data Sci. Adv.
Analytics (DSAA), Sydney, NSW, Australia, Oct. 2020, pp. 785–786, doi:
10.1109/DSAA49011.2020.00116.

[48] M. K. H. Chy, ‘‘Proactive fraud defense: Machine learning’s evolving role
in protecting against online fraud,’’ World J. Adv. Res. Rev., vol. 23, no. 3,
pp. 1580–1589, Sep. 2024, doi: 10.30574/wjarr.2024.23.3.2811.

[49] A. Hachcham. (Jan. 27, 2025). The KNN Algorithm—Explanation, Oppor-
[Online]. Available: https://neptune.ai/blog/knn-

tunities, Limitations.
algorithm

[50] Kaggle. (2016). Credit Card Fraud Detection Dataset. [Online]. Available:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

[51] P. Tomar, S. Shrivastava, and U. Thakar, ‘‘Ensemble learning based
credit card fraud detection system,’’ in Proc. 5th Conf. Inf. Com-
mun. Technol.
(CICT), Kurnool,
India, Dec. 2021, pp. 1–5, doi:
10.1109/CICT53865.2020.9672426.

HADI M. R. AL LAWATI received the B.Sc.
degree in computer science from Gulf College,
Muscat, Oman, in 2009, and the M.Sc. degree
in computer science from Staffordshire Univer-
sity, Staffordshire, U.K., in 2011. He is currently
pursuing the Ph.D. degree in computing with Uni-
versiti Teknologi Malaysia (UTM), Johor Bahru,
Malaysia, with a focus on adaptive learning for
fraud detection in payment systems. He is also a
Senior Specialist in IT card technology with the

Sohar International Bank, Muscat.

VOLUME 13, 2025

92055

---

<!-- PAGE 21 -->

H. M. R. Al Lawati et al.: Integrated Preprocessing and Drift Detection Approach

ANAZIDA ZAINAL received the Ph.D. degree in
computer science from the Faculty of Computing,
Universiti Teknologi Malaysia (UTM), Malaysia.
She is currently an Associate Professor with the
Faculty of Computing, UTM. She is also affili-
ated with the Anti-Financial Crime Laboratory and
the Information Assurance and Security Research
Group (IASRG), UTM.

MOHAMAD NIZAM KASSIM received the
Ph.D. degree in computer science from Uni-
versiti Teknologi Malaysia (UTM). He is cur-
rently the Deputy Director with the Strategic
Research Division, National Anti-Financial Crime
Center (NFCC), Malaysia. He is also with the
Anti-Financial Crime Laboratory, UTM.

SALEH AL-RIMY (Senior
BANDER ALI
Member,
received the Ph.D. degree
IEEE)
from Universiti Teknologi Malaysia (UTM),
in 2019. He was a Senior Lecturer with UTM,
from 2021 to 2024, and UNITAR International
University, in 2020, and a Lecturer at Coventry
University, from 2021 to 2022, where he led the
ethical hacking and cybersecurity. He is currently
a Senior Lecturer in cybersecurity with the Univer-
sity of Portsmouth, in July 2024. He has 12 years
of industrial experience in ICT (roles in network infrastructure, security
engineering, and IT consulting).

SULTAN AHMED ALMALKI received the B.Sc.
degree in information systems from King Abdu-
laziz University, Saudi Arabia, the M.Sc. degree
in computer science from Saint Xavier University,
USA, and the Ph.D. degree in computer science
from the University of Idaho, USA. He is currently
an Assistant Professor with the Computer Depart-
ment, Applied College, Najran University, Saudi
Arabia. His research interests include, but are not
limited to, malware analysis, data analysis, intru-

sion detection systems (IDS), artificial intelligence, and machine learning.

MOHAMMAD AL-AZAWI received the Ph.D.
degree in artificial intelligence from De Montfort
University, United Kingdom. He is currently the
Deputy Dean for Academic Affairs, Research, and
Innovation at Gulf College, Oman, and serves as an
Associate Professor in Artificial Intelligence and
Computer Vision. With over 20 years of academic
experience, he has led initiatives in curriculum
development, academic governance, and quality
assurance. His research interests include ethical
AI, machine learning, AI applications in medical diagnostics, and human
attention modelling. He is also active in promoting AI-driven educational
transformation and participates in regional and international collaborations
focused on AI development, research, and innovation.

TAMI ABDULRAHMAN ALGHAMDI received
the bachelor’s and master’s in computer science
from Western Illinois University, and the Ph.D.
degree in computer science from the University
of Idaho,
in 2022. Currently, he is an Assis-
tant Professor at the College of Computing and
Information, Al-Baha University, Al Baha, Saudi
Arabia. His research interests are machine learn-
ing, transfer learning, genetic algorithms, and data
science.

92056

VOLUME 13, 2025

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received17April2025,accepted5May2025,dateofpublication13May2025,dateofcurrentversion2June2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3569609
| An Integrated                   |      | Preprocessing |           | and Drift | Detection |     |     |
| ------------------------------- | ---- | ------------- | --------- | --------- | --------- | --- | --- |
| Approach                        | With | Adaptive      | Windowing |           | for Fraud |     |     |
| Detection                       | in   | Payment       | Systems   |           |           |     |     |
| HADIM.R.ALLAWATI1,ANAZIDAZAINAL |      |               | 1,2,      |           |           |     |     |
BANDERALISALEHAL-RIMY3,(SeniorMember,IEEE),MOHAMMADAL-AZAWI4,
| MOHAMADNIZAMKASSIM5,SULTANAHMEDALMALKI |     |     |     | 6,  |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| ANDTAMIABDULRAHMANALGHAMDI             |     |     | 7   |     |     |     |     |
1FacultyofComputing,UniversitiTeknologiMalaysia(UTM),JohorBahru81310,Malaysia
2Anti-FinancialCrimeLaboratory,FacultyofComputing,UniversitiTeknologiMalaysia(UTM),JohorBahru81310,Malaysia
3PAIDSResearchCenter,SchoolofComputing,UniversityofPortsmouth,PO13HEPortsmouth,U.K.
4GulfCollege,Muscat133,Oman
5NationalAnti-FinancialCrimeCentre(NFCC),Putrajaya62100,Malaysia
6ComputerDepartment,AppliedCollege,NajranUniversity,Najran66462,SaudiArabia
7ComputerScienceDepartment,FacultyofComputingandInformation,Al-BahaUniversity,Al-Baha65779,SaudiArabia
Correspondingauthor:AnazidaZinal(anazida@utm.my)
ThisworkwassupportedinpartbytheMalaysiaMinistryofHigherEducationunderGrantR.J130000.7851.5F477.
Asfraudulenttransactionmethodsevolverapidly;itbecomesprogressivelymorechallenging
ABSTRACT
to detect them in payment systems. Static machine learning and rule-based traditional detection methods
cannot capture all the dynamic and evolving nature of fraudulent behaviors, resulting in lower detection
accuracy and a higher false positive rate. This study proposes a complete framework that brings together
advanceddatapreprocessing,effectivedriftdetection,andareliabledetectionmodeltoaddresstheseissues.
ThemethodusesMutualInformationandSelectKBestforselectingimportantfeatures,appliesADASYNto
handleclassimbalance,andadoptsConvolutionalNeuralNetworks(CNN)tocapturecomplextransaction
patterns. By implementing Early Drift Detection Method (EDDM) and ADaptive WINdowing (ADWIN),
thedriftcanbedetectedinadvanceandthesystemcanrespondtochanges,bothgradualandsudden.The
frameworkwasevaluatedonthreedatasets,includingreal-worldtransactionsandmixed-dataenvironments,
achieving superior accuracy, precision, and drift detection rates, with values up to 99.99% accuracy and
1.0 respectively. The findings show that the framework can adjust to changing patterns of fraud, reduce
falsepositives,andenhancedetectionperformance.Theseinsightsdemonstratethesignificanceofdynamic
pre-processinganddrift-awareapproachesinthecontextofreal-timefrauddetection.Thisalsoservesasa
basisforfutureworkinadaptivefrauddetectionmodelresearchareassuchasofintegratingonlinelearning
forimprovedspeedandefficiencyinhigh-frequencytransactionalenvironments.
INDEXTERMS Bankingfraud,paymentsystems,prepaidcards,debitcards,creditcards,frauddetection,
conceptdrift,classimbalance,datapre-processing,supervisedfeatureselection,deeplearning,driftdetec-
tion,real-timefrauddetection.
|     |     |     |     | as any activity | carried out with | the intent | of gaining profit |
| --- | --- | --- | --- | --------------- | ---------------- | ---------- | ----------------- |
I. INTRODUCTION
Nowadays financial fraud has become one of the big issues through deception. Basically, fraud is an illegal method for
faced by the banking industries [1]. Fraud can be defined fraudsters to get funds and goods. Hence the goal of the
|     |     |     |     | fraudsters | is to get the product | without paying | the amount |
| --- | --- | --- | --- | ---------- | --------------------- | -------------- | ---------- |
The associate editor coordinating the review of this manuscript and or earning an unauthorized fund from an account. Techno-
|                                              |     |     |     | logical advancement | has led | fraudsters to | try new methods |
| -------------------------------------------- | --- | --- | --- | ------------------- | ------- | ------------- | --------------- |
| approvingitforpublicationwasS.K.HafizulIslam |     |     | .   |                     |         |               |                 |

2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
92036 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
to accomplish their goals. As a result, fraud incidents are inefficiencies in detecting fraudulent transactions [6]. Due
increasing,therefore,theneedtoprotectsystemsfromfraud to an increase of sophisticated fraud strategies, traditional
hasbecomeevident. systemsnolongerproducereliableresults[6].Thus,thereis
A payment system processes transactions between a cus- aneedtoaddressthisproblem.
tomer(issuer)andamerchant(acquirer)withoutacomplex Thedisadvantagesofrule-basedsystemshasmotivatedthe
process or cash, generally by cards or electronic money. researchers to turn to AI-based approaches as alternatives
Transactions fall into card-present (CP) requiring physical suchasMachineLearninganddeeplearning[7].Fig.1shows
presence and input of PIN (e.g. ATM, POS) and card-not- thedifferencebetweentherule-basedandmachinelearning-
present (CNP) occurring online (e.g., e-commerce). CNP based in the context of fraud detection systems. Rule-based
transactions are a bit more prone to fraud since they can systemsdependonpredefinedrules.Therefore,thesesystems
involve stolen card information. As payment volumes rise, failtorevealthelatestpatternsanditsvariantsbecausethey
sodoinstancesoffraud[3]. workonpre-definedrules.Thislimitationmakesitdifficult
Nowadays companies and banks are spending millions toaddressemergingtacticsinthefraudspaceandthesystem
on Know Your Customer (KYC), Fraud Systems, and Anti performance may reduce when deals with rapidly evolving
MoneyLaundering(AML)systems,yetthenumberoffraud- fraudtactics.However,machinelearningtechniquesexploit
ulent transactions is increasing [3]. Based on the Nilson data to learn autonomously and identify complex patterns,
Report,in2019thereweregrossfraudlossesonCard-based which improves the accuracy of fraud detection [6], [48].
payments which are around $28.65 billion, amounting to Machine learning has emerged as a powerful tool for fraud
6.8¢forevery$100oftotalvolume[3]. detection,asthesemodelscancontinuouslyadapttonewdata
According to the Merchant Savvy website, global losses andlearnfromsubtlepatternsanddeviations[48].
were9,84$billionin2011andkeepgrowingtillitisexpected
to reach 40.63$ billion in 2027 which is 25% higher than
in2020[4].AnotherstatisticsharedbytheMerchantSavvy
website is related to the methods of compromise used by
fraudsters for different countries and the top value for each
countrywasrelatedtoCNPtransactions.Althoughthereare
many technologies designed and implemented to enhance
fraudinpaymentsystems,thesetechniqueshavenotproven
tobeeffectiveinprotectingauthorizationandfinancialtrans-
actionsfromfraudsters.Thereasonisthatthedifferenttypes
offraudpatternsareevolvingwhichhasarealimpactonthe
implementedtechnologiestodetectfraud[5].
Mostofthebankingindustriesusearule-basedapproach
todetectfraudintheirpaymentsystem[6].Withrule-based
frauddetection,theuserusuallyconfiguresasetofrules,such
asaccountnumbers,transactiontypes,amounts,etc.Aspart
oftheruleconfiguration,theusercanalsodefinewhichaction
the system should take if the transaction matches the rule.
Thiscanincludedecliningthetransaction,displayinganalert, FIGURE1. Behaviorsinrule-basedfrauddetectionsystemandMLfraud
blockingthecard,orsendinganSMStothecardholder.Upon detectionsystem[3].
identifyingtherulebytheuser,therulebecomesactive,and
fraudisdetectedwhenthetransactionmatchestherule. There are different ML techniques proposed in different
Wheneverthereisanewsuspicioustransaction,theoper- studiesandeachtechniquehasitsownadvantagesanddisad-
ator must verify whether it is fraudulent or otherwise and vantages. ML techniques such as Support Vector Machines
update the rules if necessary. The operator’s verification (SVM)areusedinfrauddetection,buttheyarenotsuitable
process is time-consuming and costly for the organiza- for large data sets due to their high training complexity [8].
tion. Occasionally, the operator might not check/miss some Hencewithalargenumberoftransactionssuchasinbanking,
transactions until the bank or organization receives a fraud thistechniquemightnotbepracticaltobeimplemented.
complaint from a customer. The fraudsters are, swiftly, [9],[10]utilizesKNNforsomeoftheanalysis.TheKNN
and continuously adjusting their patterns and strategies to requires clustering and would not work well with a large
deceive. dataset since calculating distances between data instances
The increase of e-commerce using various types of pay- would be very expensive. Furthermore, it is not effective
mentincluding prepaidcards, debitcards,creditcards,etc., when there is a high degree of dimensionality because the
is evolving fraud patterns so rapidly that the rules-based processofcalculatingdistanceforeachdimensionbecomes
approachescannotbeupdatedfastenoughorchangequickly, complex. KNN is also sensitive to data that is noisy and
leading to false positives (blocking good customers) and missing[49].Furthermore,itinvolvesfeaturescaling,which
VOLUME13,2025 92037

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
means all the data should be scaled (normalized, standard- technologies, shifts in consumer behaviour, or the develop-
ized)intherightway[9]. mentofincreasinglycomplexfraudstrategies.Conceptdrift
Data pre-processing is essential to prepare data in an is not limited to specific timeframes; it can occur gradually
appropriate format for machine learning applications. This overanextendedperiodorasasudden,abruptchange.This
step ensures data quality and accuracy before it is passed dynamic nature of fraudulent activity underscores the need
to the machine learning model, enabling the model to per- foradaptivedetectionsystemscapableofkeepingpacewith
formeffectively.Byrefiningthedatathroughtechniqueslike thesechanges.
cleaning, normalization, and transformation, pre-processing For example, in those types of systems a fraud detection
enhances the reliability of the input data and significantly model is being trained based on a dataset containing one
improvesthemodel’sdetectionperformance. year’s worth of transactions. Models learn patterns such as
Detecting payment card fraud is critical in the evolving large purchases, suspicious transactions, or high-frequency
landscapeofpaymentsystems.Severalfactorsinfluencethe transactions.Thesystemsuccessfullyflagstransactionsthat
effectivenessoffrauddetectionmeasures.Onekeychallenge exhibitthesepatternsaspotentiallyfraudulent.However,over
istheexponentialgrowthintransactionvolumes,whichleads time fraudsters adapt and change their methods. To evade
tomorecomplexfinancialactivities.Frauddetectionsystems detection,theyalsofindthatsmaller,less-obviouspurchases
must analyze these high volumes of transactions efficiently or stolen credit card information to shop online may defeat
to differentiate between legitimate activities and fraudulent thedetectionsystem.Hence,thepatternoffraudulenttrans-
ones,ataskthatbecomesincreasinglydifficultwiththescale actionsarechangingandanewsetoffeaturesandrulesmay
andcomplexityofmodernpaymentsystems. notbeabletodetectthedifferenttypesoffrauds.
Fraudsters exploit vulnerabilities in cards and merchant To summarize, issues in fraud detection in payment sys-
systemstocarryoutunauthorizedtransactions.Whilequick temscanbecategorizedasfollows:
transaction processing is essential to ensure a smooth
customer experience, it often compromises thorough veri- A. HIGHOVERHEADANDCLASSIMBALANCE
fication, leaving systems exposed to fraudulent activities. Many researchers have applied machine learning and deep
Striking the right balance between fast processing and learning to detect fraudulent payments, but their effective-
effective fraud detection is crucial. Robust fraud detection ness is often hindered by redundant and irrelevant features,
mechanismsmustbedesignedtominimizefraudriskswith- creatingoverhead.Forexample,featureslikeexchangerates,
outimpedinglegitimatetransactions,addressingthisdelicate billingcurrency,oraccountnumbersareunrelatedtofraud-
trade-offinascalableandefficientmanner. ulent activity, as fraudsters typically exploit card numbers.
The problem characteristics of FDS can be described Reducingthisoverheadthroughtargetedfeatureengineering
into two perspectives which are; challenges in fraud and cansignificantlyenhancedetectionaccuracyandimprovethe
limitationsoftheexistingFDSsolutions.Oneofthemostsig- efficiencyoffrauddetectionsystems(FDS).
nificantchallengesinfrauddetectionistheconstantevolution Furthermore,cardpaymentfraudisdifficulttodetectdue
offraudstrategies.Fraudsterscontinuallyadaptandmodify tothehighlyimbalancednatureofthedataset[15].Asshown
their methods to bypass fraud detection systems (FDS). For in Fig. 2, the credit card dataset contains a large number
example, a fraudster may steal a batch of credit card infor- of positive instances (normal transactions) and only a small
mationandstrategicallyuseitformultiplesmallerpurchases number of negative instances (fraudulent transactions) [17].
acrossvariousonlineretailoutlets.Thesetransactionsoften Due to this imbalance, classical classification methods per-
mimic the cardholder’s typical spending patterns, making it form poorly [16], as machine learning models are biased
difficult for the FDS to identify them as fraudulent. This toward the majority class, which misclassifies the minor-
dynamic and ever-changing nature of fraudulent behavior ity class (fraudulent transactions) [18]. This can be solved
highlightstheneedforadaptableandsophisticateddetection by reducing the data complexity prior to processing, which
mechanisms. can be significant, allowing accurate and effective fraud
Themainchallengewithdetectingfraudulenttransactions detection.
istheclassimbalancethatispresentinpaymentdata,inwhich Despite the highly imbalanced nature of Credit Card in
legitimatetransactionsfaroutnumberfraudulenttransactions. which the positive instances make up only 0.17% of the
The majority class can lead to bias in models as it becomes total instances, the prediction is never 100% accurate due
more dominant, and this limits the model’s ability to detect to the separability of features. Many features, in particular
lessfrequentlyoccurredcreativefraudactivities.Thisworks anonymizedattributes(V1toV28)haveoverlappingclasses
tostudyfrauddetectionsystemsandimprovingthem. between fraudulent and non-fraudulent classes, resulting in
Another significant trend in fraud detection is known as infeasible model-perfectly distinguish classes. In general
conceptdrift,whichreferstotheevolvingnatureoffraudulent transactions, each fraudulent transaction shows similar fea-
behavior over time. In the context of payment card fraud, ture distributions as that of legitimate transactions as they
concept drift occurs when fraudsters develop new methods try to blend in with the normal activities in order to avoid
and tactics to evade existing detection systems. This evolu- beingdetected.Unfortunately,occasionallythisoverlapleads
tion can be driven by factors such as the emergence of new to misclassification of points, even with balanced data and
92038 VOLUME13,2025

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
|     |     |     |     |     |     |     |     | shifting | user behaviors, |     | or changes |     | within | the payment |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ---------- | --- | ------ | ----------- | --- |
ecosystem.
|     |     |     |     |     |     |     |     | Concept   | drift     | and its | effect | on the effectiveness |         | of         | exist- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------- | ------ | -------------------- | ------- | ---------- | ------ |
|     |     |     |     |     |     |     |     | ing fraud | detection | systems |        | has been             | studied | by several |        |
researchers.Forexample,[20],[21]showedthatconceptdrift
increditcardscanresultinahigherrateoffalsealarms,and
|     |     |     |     |     |     |     |     | therefore | the model | fails | to adapt | itself | to changes | in  | fraud |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ----- | -------- | ------ | ---------- | --- | ----- |
patterninreal-time.Inanothercase[28],[47]reportedlack
oftimelydetectionaswellashandlingstatingthatstaticfraud
|     |     |     |     |     |     |     |     | of concept | drift | compromised |     | the fraud | detection | accuracy |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------- | --- | --------- | --------- | -------- | --- |
FIGURE2. Amongthecreditcarddatadatasets,284806transactions resultinginhigherfalsepositiverates.
showstatisticsof0.17%fraud(i.e.,asmallpercentageofthetransactions Researchhighlightsthatconceptdriftisapersistentissue
fallintothefraudclass[40].
|     |     |     |     |     |     |     |     | in credit | card fraud | detection, |     | significantly | contributing |     | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ---------- | --- | ------------- | ------------ | --- | --- |
increasedfalsealarmratesovertime.Studies[28],[29]show
featureselection.Inaddition,addingnoisyornon-informative
thatstaticfrauddetectionmodelsstruggletoadapttoevolv-
| features | also impedes |     | the ability | to  | separate | classes. | These |               |         |     |             |              |     |     |      |
| -------- | ------------ | --- | ----------- | --- | -------- | -------- | ----- | ------------- | ------- | --- | ----------- | ------------ | --- | --- | ---- |
|          |              |     |             |     |          |          |       | ing patterns, | leading | to  | performance | degradation. |     | Lee | [30] |
hurdles can be addressed with extensive preprocessing like emphasizedtheimportanceofdetectingandmanagingcon-
| data cleansing  |     | to eliminate | noise/inconsistencies |            |         | in        | the first |                    |             |         |             |              |     |               |       |
| --------------- | --- | ------------ | --------------------- | ---------- | ------- | --------- | --------- | ------------------ | ----------- | ------- | ----------- | ------------ | --- | ------------- | ----- |
|                 |     |              |                       |            |         |           |           | cept drift         | to preserve | model   | performance |              | and | reduce        | false |
| step, balancing |     | in the       | second                | and lastly | feature | selection | to        |                    |             |         |             |              |     |               |       |
|                 |     |              |                       |            |         |           |           | alarms. Addressing |             | concept | drift       | is essential |     | for maintain- |       |
maintainonlythemostsignificantfeatures.Thesemeasures
|                  |     |     |         |            |     |           |      | ing detection | accuracy, |             | minimizing | operational |            | costs, | and |
| ---------------- | --- | --- | ------- | ---------- | --- | --------- | ---- | ------------- | --------- | ----------- | ---------- | ----------- | ---------- | ------ | --- |
| greatly enhanced |     | the | model’s | capability | to  | recognize | dis- |               |           |             |            |             |            |        |     |
|                  |     |     |         |            |     |           |      | improving     | user      | experience, | making     | it          | a critical | factor | for |
tinguishing patterns and mitigate the effects of overlapping effectivefrauddetectionsystems.
| classes. | This produced |     | preprocessed |     | datasets | will | be more |             |            |     |              |     |         |        |       |
| -------- | ------------- | --- | ------------ | --- | -------- | ---- | ------- | ----------- | ---------- | --- | ------------ | --- | ------- | ------ | ----- |
|          |               |     |              |     |          |      |         | Fraudsters’ | strategies |     | continuously |     | evolve, | making | fraud |
suitableanditcanbeutilizedforthelaterstage.
|       |               |     |         |             |       |       |         | detection | systems | (FDS) | essential | to  | detect | new patterns |     |
| ----- | ------------- | --- | ------- | ----------- | ----- | ----- | ------- | --------- | ------- | ----- | --------- | --- | ------ | ------------ | --- |
| There | are different |     | studies | [13], [27], | [42], | [43], | [44] to |           |         |       |           |     |        |              |     |
promptly.Asaresultofstaticrulesandoutdatedmodelsthat
tackleclassimbalance.Someofthemproposedtouseover-
donotaddresstheever-changingnatureoffraudulentbehav-
samplingandsomeofthemproposedunder-sampling.Akey ior,currentsolutionshavepoordetectionaccuracyandhigh
differencebetweenthesetwomethodsisthatunder-sampling
falsealarmrates.Inaddition,thehighoperationaloverheadof
| moves instances |     | from | the majority |     | class into | the | minority |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ------------ | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
largedatasetswithnoiseandnonfunctionalfeaturesandwith
| class to | balance | the data | set | while oversampling |     | replicates |     |     |     |     |     |     |     |     |     |
| -------- | ------- | -------- | --- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classimbalancedegradesdetectionperformance.Legitimate
theminorityclassinstancestobalancethedataset[19].The
andfraudulentpaymentbehaviorscanshiftsignificantlyover
drawbackofeachmethodisthatunder-samplingleadstothe time,requiringimprovementsinfrauddetectionsystems.But
| loss of potentially |     | relevant |     | information, | causing | the | model |     |     |     |     |     |     |     |     |
| ------------------- | --- | -------- | --- | ------------ | ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
currentrulebasedandmachinelearningbasedmethodscan-
toperformpoorlywhileiftheimbalanceratioishigh,over-
notbereadilyadaptedtocopewiththesechallengesresulting
sampling introduces the disadvantage of overfitting and an inlimitationsinbothaccuracyandreliability.
additionalcomputationalcost[19].
|     |     |     |     |     |     |     |     | To solve | these | problems, | this | paper | uses | a combination |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | ---- | ----- | ---- | ------------- | --- |
Existing studies [2], [11], [13], [26], [27], [28] face of improved processing, feature selection, adaptive resam-
| limitations | in      | pre-processing, |           | often | lacking | thorough    | data |                |              |          |            |                  |     |           |       |
| ----------- | ------- | --------------- | --------- | ----- | ------- | ----------- | ---- | -------------- | ------------ | -------- | ---------- | ---------------- | --- | --------- | ----- |
|             |         |                 |           |       |         |             |      | pling and      | hierarchical | concept  |            | drift detection. |     | The phase | in    |
| cleansing,  | leading | to              | incorrect | AI    | model   | predictions | and  |                |              |          |            |                  |     |           |       |
|             |         |                 |           |       |         |             |      | pre-processing |              | combines | supervised | feature          |     | selection | tech- |
degraded performance. Some approaches use feature selec- niques including Mutual Information with SelectKBest that
| tion without | clearly | demonstrating |     | the | value | or stability | of  |               |           |     |           |         |     |          |      |
| ------------ | ------- | ------------- | --- | --- | ----- | ------------ | --- | ------------- | --------- | --- | --------- | ------- | --- | -------- | ---- |
|              |         |               |     |     |       |              |     | will optimize | pertinent |     | features, | as well | as  | Adaptive | Syn- |
the chosen features. Additionally, class imbalance handling thetic Sampling (ADASYN) to deal with the imbalance of
isfrequentlyappliedafterdatapreparationandfeatureselec-
|     |     |     |     |     |     |     |     | classes. | Furthermore, | to  | keep | it ahead | of changes | in  | fraud |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ---- | -------- | ---------- | --- | ----- |
tion,reducingtheoverallefficiencyoftheprocess.
behavioraschemeisadoptedwhichdetectsatmicrolevelthe
processshiftAdaptableDriftDetection(ADWIN)combined
B. HIGHFALSEPOSITIVE withEarlyDriftDetectionMethod(EDDM)forbothsmooth
Customers’ habits change over time, and so do fraudsters’ andsuddenChangesintransactionpatternareimplemented
strategies—thisisknownasConceptDrift[22].Theperfor- throughaconvolutionalneuralnetwork(CNN),thusimprov-
mance of FDS degrades when these patterns keep changing ing the accuracy of fraud detection. The main goal of the
and evolving. Concept drift, a widely studied phenomenon proposed way is to increase efficiency in identifying fraud,
in data streams, significantly impacts the performance of whilealsoreducingfalsepositivesandensuringthatdetection
machinelearningmodels,includingfrauddetectionsystems. performanceinconstantlychangingpaymentcardtransaction
It occurs when the statistical properties of data change over situationsstaysgood.
time, creating a mismatch between the model’s training This paper is organized into six sections. The first
data and new incoming data. In credit card fraud detec- section introduces financial fraud, followed by the second
tion, concept drift often arises from evolving fraud tactics, section which gives an overview of related work. The third
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 92039 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
| section        | presents | the proposed |         | methodology |           | including | all       |     |     |     |     |     |     |     |     |
| -------------- | -------- | ------------ | ------- | ----------- | --------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| pre-processing |          | steps and    | concept | drift       | detection |           | approach. |     |     |     |     |     |     |     |     |
Inthissectionalso,theexperimentalsetup,datasetusedand
| detailed   | framework’s | technical      |     | implementation |         | have | been      |     |     |     |     |     |     |     |     |
| ---------- | ----------- | -------------- | --- | -------------- | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| explained. | The         | fourth section |     | presents       | results | and  | analysis. |     |     |     |     |     |     |     |     |
Meanwhilesectionfivebrieflydescribefutureworkandthe
finalsectionconcludesthepaper,summarizingkeyfindings,
andhighlightingthecontributions.
|     |     |     |     |     |     |     |     | FIGURE3. | Paymentcardoverthenetwork. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------------------- | --- | --- | --- | --- | --- | --- |
II. LITERATUREREVIEW
Thissectionexplorestheexistingstudiesandworksdoneby
| others on | fraud   | detection    | in card | payment       |     | systems.    | A brief |             |          |              |      |          |      |     |           |
| --------- | ------- | ------------ | ------- | ------------- | --- | ----------- | ------- | ----------- | -------- | ------------ | ---- | -------- | ---- | --- | --------- |
|           |         |              |         |               |     |             |         | directly    | to the   | cardholder’s | bank | account, | such | as  | a savings |
| overview  | of the  | card payment |         | system        | and | the most    | com-    |             |          |              |      |          |      |     |           |
|           |         |              |         |               |     |             |         | or checking | account. | When         | the  | customer | uses | the | card for  |
| mon fraud | methods | employed     |         | by fraudsters |     | is provided | at      |             |          |              |      |          |      |     |           |
transactions,theamountisimmediatelydebitedorcreditedto
| the beginning | of  | this review. |     | Following | this | foundational |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------ | --- | --------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theirbankaccount.Acreditcard,ontheotherhand,islinked
| overview, | existing | research | is  | analyzed | in depth | to  | identify |     |     |     |     |     |     |     |     |
| --------- | -------- | -------- | --- | -------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
toashadowaccount,allowingthecustomertoborrowfunds
frauddetectiontechniques,models,andmethodologies.Dur-
|     |     |     |     |     |     |     |     | up to a | pre-approved | credit | limit. | The | customer | can | use the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ------ | ------ | --- | -------- | --- | ------- |
ingthisprocess,thereviewidentifiesresearchgapsandareas
|     |     |     |     |     |     |     |     | card provided |     | they pay | their | monthly | dues. | If payments | are |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ----- | ------- | ----- | ----------- | --- |
forfurtheradvancement.
|     |     |     |     |     |     |     |     | delayed, | interest | or late | fees | are charged. | A   | prepaid | card, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------- | ---- | ------------ | --- | ------- | ----- |
alsoknownasapre-loadedcard,isnottiedtoabankaccount.
A. PAYMENTCARDSYSTEM
Customersloadmoneyontothecard,whichcanthenbeused
| A payment      | card | is an electronic |     | payment |             | card that | allows |          |             |              |     |      |         |              |     |
| -------------- | ---- | ---------------- | --- | ------- | ----------- | --------- | ------ | -------- | ----------- | ------------ | --- | ---- | ------- | ------------ | --- |
|                |      |                  |     |         |             |           |        | globally | for various | transactions |     | such | as cash | withdrawals, |     |
| the cardholder |      | to pay through   |     | POSs    | or withdraw |           | money  |          |             |              |     |      |         |              |     |
purchases,ore-commerce.Unlikedebitandcreditcards,pre-
throughATMs,ore-commercewebsites.Throughanetwork
paidcardscanbeusedbybothcustomersandnon-customers.
| of connections, |     | card payment |     | systems | allow | customers | to  |        |        |        |         |            |     |      |            |
| --------------- | --- | ------------ | --- | ------- | ----- | --------- | --- | ------ | ------ | ------ | ------- | ---------- | --- | ---- | ---------- |
|                 |     |              |     |         |       |           |     | At the | system | level, | payment | processors |     | play | a critical |
makepaymentsbycard[35].Inthecontextofcardpayment,
roleinfacilitatingtransactionsbetweenissuersandacquirers.
thepaymentecosystemconsistsofthedifferentplayersand
Theyformatandprocesstransactions,forwardclearinginfor-
theirinteractionsthatmakethetransactionwork.Theperson
mationtomerchantsandcardnetworks,validatetransactions,
| using a payment |     | card to | purchase | something |     | or transact | is  |          |         |                 |     |     |        |              |     |
| --------------- | --- | ------- | -------- | --------- | --- | ----------- | --- | -------- | ------- | --------------- | --- | --- | ------ | ------------ | --- |
|                 |     |         |          |           |     |             |     | regulate | payment | authorizations, |     | and | ensure | the security | of  |
knownasthecardholder.Paymentcardissueralsoknownas
customerdataagainstfraudandotherthreats.
Issuer,itistypicallyabankorotherfinancialinstitutionthat
| issues payment |     | cards to | cardholders. |     | These | cards | are used |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ------------ | --- | ----- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
B. EUROPAY,MASTERCARD,ANDVISA(EMV)
| by merchants | (for | example, | retailers, |       | or service   | providers) |           |               |     |             |     |           |      |        |          |
| ------------ | ---- | -------- | ---------- | ----- | ------------ | ---------- | --------- | ------------- | --- | ----------- | --- | --------- | ---- | ------ | -------- |
|              |      |          |            |       |              |            |           | EMV (Europay, |     | MasterCard, |     | and Visa) | is a | global | standard |
| as a method  | of   | payment  | for        | goods | or services. |            | Acquirers |               |     |             |     |           |      |        |          |
forsecurepaymentprocessingusingsmartcardtechnology.
areessentiallybanksorotherorganizationsthatpartnerwith
|     |     |     |     |     |     |     |     | It is named | after | the | three | companies | that | developed | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | ----- | --------- | ---- | --------- | --- |
themerchantsthatacceptandapprovecardpayment.Atthe
initialchiptechnologyembeddedinEMVcards.Thesechips
| heart of | this ecosystem |     | are the | networks, |     | like Mastercard, |     |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------- | --------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
securelystoreandprocesscryptographicinformationduring
| Visa and | American | Express, | which | serve | as  | intermediaries |     |     |     |     |     |     |     |     |     |
| -------- | -------- | -------- | ----- | ----- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transactions,reducingfraudriskandensuringglobalconsis-
betweenissuersandacquirers.Thesenetworksareresponsi-
|                   |     |            |        |        |     |            |       | tency in | payment | processing |     | standards, | terminal |     | behavior, |
| ----------------- | --- | ---------- | ------ | ------ | --- | ---------- | ----- | -------- | ------- | ---------- | --- | ---------- | -------- | --- | --------- |
| ble for governing |     | the cards’ | usage, | laying |     | the ground | rules |          |         |            |     |            |          |     |           |
andcommunicationprotocols.
| for where | and how | cards | can | be used, | instituting |     | fees and |     |     |     |     |     |     |     |     |
| --------- | ------- | ----- | --- | -------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
EMVtransactionsarecategorizedintotwotypes:
| ensuring | smooth, | secure | operations | between |     | parties. | Fig. 3 |     |     |     |     |     |     |     |     |
| -------- | ------- | ------ | ---------- | ------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
showshowthepaymentcardworksoverthenetwork:ACus- 1. Contact Transactions: The chip card is physically
|                |     |               |     |             |     |     |        | inserted |     | into a terminal |     | reader, | such as | an ATM, | POS |
| -------------- | --- | ------------- | --- | ----------- | --- | --- | ------ | -------- | --- | --------------- | --- | ------- | ------- | ------- | --- |
| tomer performs |     | a transaction | on  | e-commerce, |     | ATM | or POS |          |     |                 |     |         |         |         |     |
terminal at the merchant side. This transaction is then sent system,orothercompatibledevices.
|     |     |     |     |     |     |     |     | 2. Contactless |     | Transactions: |     | The | card | is tapped | on a |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- | --- | ---- | --------- | ---- |
tothemerchantthroughthepaymentsystem.Themerchant
terminal’scontactlessreader,anddataisexchangedvia
| terminal | sends | the transaction |     | once | again | to the | acquirer’s |     |     |     |     |     |     |     |     |
| -------- | ----- | --------------- | --- | ---- | ----- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
paymentsystem.Theacquirerprocessesthetransactionand NearFieldCommunication(NFC).
forwardstothecardnetwork.Itforwardstransactiondatato An additional layer of security for contactless transactions
the issuing bank for approval or denial. The card network is tokenization, which replaces sensitive card information
withauniquetoken,furthersafeguardingthetransactionfrom
sendstheresponsebacktotheissuingbank.Thecardnetwork
| then routes | the | response | back | to acquirer, | who | would | have | fraud[37]. |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ---- | ------------ | --- | ----- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
eitherapprovedorrejectedthetransactionbasedonwhether
| issuerapprovedornot. |     |     |     |     |     |     |     | C. TRANSACTIONTYPES |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
Therearethreemaintypesofpaymentcards:debitcards, There are two types of transactions which are card-present
credit cards, and prepaid cards. A debit card is linked (CP)andcard-not-present(CNP).
| 92040 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
• CP transactions: transactions are those in which pay- v. ApplicationFraud:Applicationfraudiswhensomeone
ment details are captured in person, at the time of steals payment card details, however, card ID theft is
sale. This occurs when cards are physically tapped not to be confused with this. But fraudsters use the
via NFC, swiped over POS, or dipped into the ter- stolen card details to create a tenth account or make
minal CHIP’s reader to process transactions with the transactions.Thistypeoffraudishardtoidentify.
EMV [38]. Hence the Customer needs to physically vi. FakeMerchantWebsites(Phishing):Thevictimoffalse
insertortaptheChipontheATMforCashWithdrawal, merchant websites is similar to phishing fraud, where
POSforpurchasetransactions,etc.[3].Thefollowing the customer is misled into a fake website created
are examples of CP transactions [39]: POS terminals byfraudsters,whichcloselyresemblesagenuinesite.
with EMV Reader, Contactless terminals, CHIP card Tolurethecustomerintomakingapurchase,thefraud-
readersconnectedtosmartphones ulent webpage may offer several discounts. When the
• CNPtransactions:Cardholderswhoarenotphysically transaction is completed, all the card and transaction
presentwhenatransactionisconductedareconsidered informationiscollectedbythefraudstersandusedfor
Cards-Not-Present (CNP). In the present day, remote fraudulenttransactions.
order transactions are the most common. This can vii. MerchantCollusion:Merchantcollusionoccurswhen
be done over the phone, by fax, on the web, or by themerchantforwardsinformationrelatedtothecard-
mail[38].TheCNPmeansisunlikeCard-presenttrans- holderwithoutthecardholder’sknowledge.
| actions | in which | the | transaction | can | be done | online |     |     |     |     |     |     |
| ------- | -------- | --- | ----------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- |
Thetopthreemostcommontypesoffraud:
| such | as e-commerce |     | transactions | and | in this | kind of |     |     |     |     |     |     |
| ---- | ------------- | --- | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
i. Skimming:Thisinvolvesgatheringinformationfroma
transactions,thefraudsteralwaysusescarddetailssuch
cardholder’smagneticstripethroughmagstripereader
| as  | card number, | expiry | date, | and | CVV2 | to perform |     |     |     |     |     |     |
| --- | ------------ | ------ | ----- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
transactions [3]. The following are examples of CNP or through other skimming tools. This data is also
|              |     |                   |     |          |     |             | captured | during | valid transactions |     | and | is then used |
| ------------ | --- | ----------------- | --- | -------- | --- | ----------- | -------- | ------ | ------------------ | --- | --- | ------------ |
| transactions |     | [39]: E-commerce, |     | shopping |     | carts, sub- |          |        |                    |     |     |              |
forsubsequentillegaltransactions.However,fraudsters
scriptionorrecurringbilling,e-invoicing,orderingvia
phoneandmanualentryandtheappsthatallowmobile can use skimming devices on payment terminals like
ATMstostealsensitivecardinformation.
paymentswithoutrequiringpaymentcardreaders.
ii. Card-Not-PresentFraud(CNP):CNPfraudiscommon
intheonlineworld.Thethievesmakeillicitpurchases
D. FRAUDINCARDPAYMENTSYSTEM online using the card number, expiration date, and
| Payment        | card fraud | is one  | of the | challenges | for  | businesses |         |                  |                 |               |              |          |
| -------------- | ---------- | ------- | ------ | ---------- | ---- | ---------- | ------- | ---------------- | --------------- | ------------- | ------------ | -------- |
|                |            |         |        |            |      |            | CVV.    | The fact         | that e-commerce |               | transactions | do not   |
| as it involves | the        | illegal | use of | cardholder | data | to per-    |         |                  |                 |               |              |          |
|                |            |         |        |            |      |            | require | the presentation |                 | of a physical | card         | may lead |
formunauthorizedpurchasesandtransactions.Theydisguise to them being also targeted by fraudsters,who can be
| unauthorized | purchases | and | fake | card as | cardholder | details, |              |           |      |           |              |     |
| ------------ | --------- | --- | ---- | ------- | ---------- | -------- | ------------ | --------- | ---- | --------- | ------------ | --- |
|              |           |     |      |         |            |          | definitively | deceiving | both | financial | institutions | and |
adapt their behavior and use fraud patterns that can cir- merchants.
cumventsecuritymeasures.Exploitingvulnerabilitiesinthe
|         |              |       |         |              |     |            | iii. Fake Card | Fraud:   | Fraudsters | use | stolen card | informa- |
| ------- | ------------ | ----- | ------- | ------------ | --- | ---------- | -------------- | -------- | ---------- | --- | ----------- | -------- |
| payment | system, such | fraud | results | in financial |     | losses and |                |          |            |     |             |          |
|         |              |       |         |              |     |            | tion—often     | obtained | through    |     | skimming—to | create   |
potentialharmtobothbusinessesandindividuals. fakepaymentcards,whicharethenusedforfraudulent
[46]presentedafewtypesofFraudinCardPayment:
transactions.Thestolendataisencodedontocounter-
|                                                   |       |     |            |     |        |            | feit cards, | allowing | fraudsters |     | to make | unauthorized |
| ------------------------------------------------- | ----- | --- | ---------- | --- | ------ | ---------- | ----------- | -------- | ---------- | --- | ------- | ------------ |
| i. Skimming:                                      | Using | an  | electronic | or  | manual | imprinting |             |          |            |     |         |              |
| tool,thefraudstercanaccesstheinformationdisplayed |       |     |            |     |        |            | purchases.  |          |            |     |         |              |
onthemagneticstripe.Inotherwords,thefraudstercan
skimthecardusingdifferenttoolstoreadthemagnetic E. EXISTINGWORKSINFRAUDDETECTION
stripe.Fraudstersmayusethisinformationinthefuture Thissectionpresentsareviewoftheliteraturerelatedtofraud
forfraudulenttransactionsiftheygainaccesstoit. detection systems (FDS) published from 2015 to 2024. The
ii. Card Not Present (CNP) Fraud: As previously reviewdiscussesdifferentapproachesandmethodstodetect
explained,fraudsterscanuseacardwithoutphysically fraud done by existing works, highlighting the techniques
possessingitbyenteringcardinformationsuchasthe used, limitations and their advantages. This section reviews
expirydate,cardnumber,andCVV. relatedworksaboutfrauddetectionincardpaymentsystems
iii. Fakecard:Fakecardfraudisusuallydoneusingskim- and it focuses on five main challenges: class imbalance,
ming. Fraudsters make a clone mag stripe card with conceptdrift,featureselection,classificationtechniques,and
the same data stored on the original card. The card is driftdetectionmethods.Thecomparisonofpastapproaches
adummybutisstilloperationalforfuturetransactions. demonstratestheirshortcomingsandgivessomeinsightson
iv. LostorStolencard fraud:Fore-commerceormanual howtoimprove.
entrytransactions,fraudsterscanusethatcardfortrans- Shakya [24] examined the application of ML techniques
actionsasnoPINverificationisneededwhenthecard increditcardfrauddetection,usingclassificationalgorithms
islostorstolen. like Logistic Regression, Random Forest, and XGBoost.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 92041 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
This study utilized resampling methods (such as Random model for improved performance. This approach integrates
UnderSampling,TomekLinksRemoval,SMOTE,andcom- manual oversight with model refinement, enhancing detec-
binations of SMOTE and Tomek Links) to manage class tion capabilities over time. Fig. 6 shows details of [27]
imbalance, and the model achieved a high accuracy of proposedsystem.
| approximately | 98%.             | Shakya’s | research | provided | full     | exper- |     |     |     |     |     |
| ------------- | ---------------- | -------- | -------- | -------- | -------- | ------ | --- | --- | --- | --- | --- |
| imental       | details for each | machine  |          | learning | that has | been   |     |     |     |     |     |
utilizeddemonstratingeffectivehandlingofclassimbalance
| and robust | classification | performance. |     | Fig. | 4 demonstrates |     |     |     |     |     |     |
| ---------- | -------------- | ------------ | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
theworkflowofthismodel:
|     |     |     |     |     |     |     | FIGURE6. Workflowofthecreditcardfrauddetectionsystemby[27] |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- |
usingrandomforestalgorithm.
TheAdaptiveMulti-LayeredModelproposedbyYusof[11]
asshowninFig.7,comprisesfourkeysystems:Authentica-
tionLayer,BehaviouralLayer,SmartLayer,andBackground
ProcessingLayer.
TheAuthenticationLayerverifiesincomingtransactions
|     |     |     |     |     |     |     | based on predefined | rules and | user profilesfrom |     | past trans- |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --------- | ----------------- | --- | ----------- |
FIGURE4. FrauddetectionprocessflowinShakya’s[24]proposedmodel.
actions.Significantdeviationstriggerfurtherreview.
|     |     |     |     |     |     |     | The Behavioural | Layer employs | fuzzy | association | rules |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | ----- | ----------- | ----- |
Evan[26]proposedahybridmethodcombiningJ48Deci-
|     |     |     |     |     |     |     | and feature | selection to handle | behavioural | ambiguity, | gen- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------- | ----------- | ---------- | ---- |
sionTree,SVM,K-meansClustering,andRandomForestas erating a fuzzy score for suspicious activities. High-risk
shown in Fig. 5. The approach involved clustering similar transactionsareflaggedbasedonsubstantialdeviationsfrom
| data points | to detect | anomalies |     | and classifying |     | transac- |     |     |     |     |     |
| ----------- | --------- | --------- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- |
normalbehaviour.
tions using Random Forest. Fraudulent transactions were In the Smart Layer, transactions are categorized as nor-
flaggedifidentifiedbyeithermodel,whileunclassifiedtrans-
|         |                |       |            |     |             |     | mal or priority. | Normal transactions |       | are analysed  | using |
| ------- | -------------- | ----- | ---------- | --- | ----------- | --- | ---------------- | ------------------- | ----- | ------------- | ----- |
| actions | were processed | using | confidence |     | thresholds. | The |                  |                     |       |               |       |
|         |                |       |            |     |             |     | Support Vector   | Machines (SVM),     | while | high-priority | ones  |
two-stage model increased discriminability and provided a are processed by Gated Recurrent Units (GRU) for more
robustdetection,asevidencedbyhighclassificationaccuracy
|     |     |     |     |     |     |     | efficient anomaly | detection. Lastly, | the | Background | Pro- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------------ | --- | ---------- | ---- |
androbustness. cessing Layer ensures continuous improvement through
|     |     |     |     |     |     |     | under-sampling | for class balancing, | periodic | model | retrain- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------------------- | -------- | ----- | -------- |
ing,andruleupdates.
FIGURE5. ProposedcreditcardfrauddetectionsystembyEvan[26].
| In Shmatko’s     | study              | [27],          | the Random |          | Forest algorithm |         |     |     |     |     |     |
| ---------------- | ------------------ | -------------- | ---------- | -------- | ---------------- | ------- | --- | --- | --- | --- | --- |
| served as        | the primary        | classification |            | method   | for credit       | card    |     |     |     |     |     |
| fraud detection. | Transactions       |                | were       | assigned | a risk           | score   |     |     |     |     |     |
| (0–100)          | based on a machine |                | learning   | model    | trained          | on his- |     |     |     |     |     |
toricaldata.Transactionsbelowapredefinedthresholdwere
classified as non-risky, while those exceeding the threshold FIGURE7. AdaptiveMulti-LayeredModelforCreditCardFraudDetection
byYusof[11].
| (e.g., 90) | were flagged | for | manual | review. | Bank staff | could |     |     |     |     |     |
| ---------- | ------------ | --- | ------ | ------- | ---------- | ----- | --- | --- | --- | --- | --- |
approve, reject, or further investigate flagged transactions, Priya & Uthra [25] proposed a deep learning frame-
with outcomes used to update the dataset and retrain the work, CIDD-ADODNN, to address concept drift and class
| 92042 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
Theextractedrawcontentisthenprocessedfurthersuchas
chunkgeneration,datatransformationandformatconversion
asapartofdatapreprocessingtomakeitreadytobeanalyzed.
Todetectsuchregionshiftsovertime,theADWIN(Adaptive
|     |     |     |     |     | Windowing) | model | is  | utilized. | During | data | evolution, | this |
| --- | --- | --- | --- | --- | ---------- | ----- | --- | --------- | ------ | ---- | ---------- | ---- |
stepisessentialtokeepmodelperformance.
Assoonasdriftdetectioniscomplete,thedataisclassified
|     |     |     |     |     | using a      | Multilayer | Perceptron |         | (MLP)     | model. |             | The Chimp |
| --- | --- | --- | --- | --- | ------------ | ---------- | ---------- | ------- | --------- | ------ | ----------- | --------- |
|     |     |     |     |     | Optimization | Algorithm  |            | further | optimizes |        | the model’s | per-      |
formancebyfine-tuningtheclassifierparameterstoproduce
moreaccuratepredictions.Afterwards,theclassificationout-
putisevaluated,andthemodel’sperformanceisvalidated.
|     |     |     |     |     | The model’s     |     | strength | is its | incorporation   |     | of a     | drift detec- |
| --- | --- | --- | --- | --- | --------------- | --- | -------- | ------ | --------------- | --- | -------- | ------------ |
|     |     |     |     |     | tion mechanism. |     | ADWIN    |        | can efficiently |     | identify | sudden       |
drifts,allowingthemodeltoadaptquicklytosuddenchanges
|     |     |     |     |     | in transaction |             | patterns. | The         | enhanced | Chimp        | Optimization |             |
| --- | --- | --- | --- | --- | -------------- | ----------- | --------- | ----------- | -------- | ------------ | ------------ | ----------- |
|     |     |     |     |     | Algorithm      | ensures     | this      | model       | is       | also         | fine-tuned,  | paving      |
|     |     |     |     |     | the way        | for optimal |           | performance |          | by improving |              | the classi- |
FIGURE8. WorkflowofCIDD-ADODNNmodelwithADASYNbalancing
|     |     |     |     |     | fier hyperparameter, |     |     | thereby | enhancing |     | not only | accuracy |
| --- | --- | --- | --- | --- | -------------------- | --- | --- | ------- | --------- | --- | -------- | -------- |
andADWINdriftdetection[25].
|     |     |     |     |     | but also | the adaptability |     | to  | evolving | trends | in  | credit card |
| --- | --- | --- | --- | --- | -------- | ---------------- | --- | --- | -------- | ------ | --- | ----------- |
fraud[36].
Reference[42]proposedanadaptiveclassifierframework
| imbalance | in streaming | data. | The proposed | model is illus- |     |     |     |     |     |     |     |     |
| --------- | ------------ | ----- | ------------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tratedinFig.8. to address concept drift and class imbalance in streaming
dataenvironments.Theframeworkintegratesdriftdetection,
Themodelcombinestechniquesforpreprocessing,imbal-
|     |     |     |     |     | class imbalance |     | handling, | and | classification |     | into | a cohesive |
| --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | -------------- | --- | ---- | ---------- |
ancehandling,driftdetection,andclassification.Preprocess-
|     |     |     |     |     | workflow. | It begins |     | with preprocessing |     |     | streaming | data to |
| --- | --- | --- | --- | --- | --------- | --------- | --- | ------------------ | --- | --- | --------- | ------- |
ingformatsrawdata,followedbyADASYNtobalanceclass
prepareitforfurtheranalysis.
| distribution, | improving | the detection | of  | minority fraudulent |     |     |     |     |     |     |     |     |
| ------------- | --------- | ------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
transactions.ADWINdriftdetectionisthenappliedtoiden- Drift detection is achieved using ensemble-based resam-
|     |     |     |     |     | pling and | statistical |     | methods | like | Kullback-Leibler |     | (KL) |
| --- | --- | --- | --- | --- | --------- | ----------- | --- | ------- | ---- | ---------------- | --- | ---- |
tifyandadapttoreal-timeshiftsinfraudpatterns,triggering
|              |             |                |     |                   | divergence | and | Cramer’s | V   | statistic | to identify |     | changes in |
| ------------ | ----------- | -------------- | --- | ----------------- | ---------- | --- | -------- | --- | --------- | ----------- | --- | ---------- |
| self-updates | to maintain | high accuracy. |     | The model employs |            |     |          |     |           |             |     |            |
datadistribution.Toaddressclassimbalance,theframework
aDeepNeuralNetwork(DNN)optimizedwithAdadeltafor
|     |     |     |     |     | employs | adaptive | oversampling |     | of  | minority | class | instances. |
| --- | --- | --- | --- | --- | ------- | -------- | ------------ | --- | --- | -------- | ----- | ---------- |
precisetransactionclassification.
In 2017, S. Caxton Emerald and T. Vengattaraman [36] This ensures the model remains effective by retraining with
|            |                  |           |          |                   | augmented      | instances |             | that reflect | the   | latest | data distribution. |         |
| ---------- | ---------------- | --------- | -------- | ----------------- | -------------- | --------- | ----------- | ------------ | ----- | ------ | ------------------ | ------- |
| introduced | a model named    | ‘‘Concept | Drift    | Detection with    |                |           |             |              |       |        |                    |         |
|            |                  |           |          |                   | Classification |           | is enhanced |              | using | robust | ensemble           | methods |
| Optimal    | Machine Learning | Model     | for Data | Classification.’’ |                |           |             |              |       |        |                    |         |
suchasRandomForest,Bagging,LightGBM,andXGBoost,
Fig.9demonstratestheworkflowofthismodel,startingwith
|           |                  |      |              |          | which are             | particularly  |        | effective | in          | handling          | noisy       | and com- |
| --------- | ---------------- | ---- | ------------ | -------- | --------------------- | ------------- | ------ | --------- | ----------- | ----------------- | ----------- | -------- |
| the input | training dataset | from | the KDDCup99 | and Spam |                       |               |        |           |             |                   |             |          |
| datasets. |                  |      |              |          | plexdatawithoutliers. |               |        |           |             |                   |             |          |
|           |                  |      |              |          | This                  | approach      | offers | improved  |             | adaptability      |             | and pre- |
|           |                  |      |              |          | diction               | accuracy,     | making | it        | well-suited |                   | for dynamic | and      |
|           |                  |      |              |          | complex               | environments. |        | However,  |             | the computational |             | com-     |
plexityofensemblemethodsandadaptiveresamplingcould
|     |     |     |     |     | pose challenges |     | in high-frequency |     |     | or resource-constrained |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | ----------------- | --- | --- | ----------------------- | --- | --- |
applications.
|     |     |     |     |     | The methodology  |               |           | proposed       | by          | Kajal      | and           | Kaur [43] |
| --- | --- | --- | --- | --- | ---------------- | ------------- | --------- | -------------- | ----------- | ---------- | ------------- | --------- |
|     |     |     |     |     | addresses        | class         | imbalance |                | in          | datasets   | through       | resam-    |
|     |     |     |     |     | pling techniques |               | and       | feature        | selection.  |            | Preprocessing | the       |
|     |     |     |     |     | data before      | applying      |           | classification |             | algorithms |               | combines  |
|     |     |     |     |     | Near-Miss        | undersampling |           | with           | Information |            | Gain.         | Feature   |
|     |     |     |     |     | extraction       | and           | balancing | of             | the dataset | are        | the first     | steps in  |
theworkflow.
|     |     |     |     |     | In the | proposed | method, |     | the Near-Miss |     | undersampling |     |
| --- | --- | --- | --- | --- | ------ | -------- | ------- | --- | ------------- | --- | ------------- | --- |
techniqueisusedtoequalizethenumberofinstancesinfraud
|     |     |     |     |     | and non-fraud |     | classes. | As a | result | of Information |     | Gain, the |
| --- | --- | --- | --- | --- | ------------- | --- | -------- | ---- | ------ | -------------- | --- | --------- |
mostrelevantattributesareidentified,thusreducingcompu-
FIGURE9. Workflowoftheconceptdriftdetectionmodelwithoptimal
machinelearningfordataclassification[36]. tationalcomplexityandimprovingmodelperformance.The
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 92043 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
classificationmethodwasdividedintotheNaiveBayesand to changing fraud generative patterns. Joshi et al. [51] use
DecisiontreealgorithmswithDecisionTreegivingthebetter architecture of ensemble learning-based credit card fraud
results. Using Information Gain the Decision Tree classi- detectionmodelshowninFig11.ItstartswiththePreprocess-
fier with selected 18 features accuracy, precise, recall, F1 ingphasewheretransactiondatainarawformiscleanedup
achievedat97%ThisismuchbetterthanNaïveBayeswhich andprocessed.Sincethedatasetisheavilyimbalanced,under
gets 90% for all these metrics. The adoption of proposed samplingisusedtoreducethenumberofdatainstancesinthe
methodology has been validated in context with European majority class, therefore making the dataset more balanced.
Cardholder dataset, which thus gives the potential of pro- The phase of Splitting Dataset slices the dataset into fea-
posed methodology in prediction of better accuracies with turevariables(independent)andtargetvariables(dependent).
respecttohandlinghighlyimbalanceddata. Data ports from the Data Preparation to Apply Classifiers
The model designed by Saraf and Phakatkar [44] is an stage,whereclassifiers(e.g.DecisionTree,LogisticRegres-
ensemblemodelforfraudulentdetectionofcreditcards.They sion,NaiveBayes)areapplied.ApplyVotingisahardvoting
consider class imbalances as well as changing fraud trends. mechanismusedtoobtainthepredictedclasslabel,whichis
Fig.10showsthattheproposedbagging–boostingworkflow class with most predictions. Within the Evaluate Efficiency
improvestheaccuracyofdifferentmodels.Datapreprocess- phase, some metrics (Accuracy, F1 score, Precision, and
ing involves the cleaning of data, outlier removal using the Recall) are used to evaluate how the model performs. This
interquartilerange(IQR)approach,andoversamplingofthe isanensemblemethod,toaugmentthemodel(whichmight
highlyimbalanceddatasetswiththeSMOTEtechnique. have had high class imbalances) on the top of classifiers
capabilities.
FIGURE11. Theprocessflowdiagramforensemblelearningbasedcredit
cardFDS.[51].
FIGURE10. Workflowofthehybridensemblemodelforcreditcardfraud
detectionwithsmotebalancing[44].
Singhetal.[12]usedRandomForestclassifiersfordetect-
In classification phase hybrid ensemble, which combines ingfraudulentcreditcardtransactionsandaddressedaclass
Random Forest and AdaBoost. The Random Forest is an imbalance problem with Synthetic Minority Over-sampling
ensemble of decision trees trained on bootstrapped sam- Technique (SMOTE). Their approach provided a complete
ples(withreplacement)withanaggregatedresult,makingit preprocessing mechanism including outlier removal, nor-
robusttooverfitting,whileAdaBoostperformedonweighted malization, and feature scaling so that the model could be
voting focusing on misclassified instances to improve clas- applied efficiently. The SHAP values variably represented
sification performance. Model with the hybrid ensemble thecontributionofeachfeaturetothemodel’soutput,which
outperformed Logistic regression Precision, Recall, and enabledtheinterpretablemodelandincreasedconfidencein
F1-Score are 1.00, 0.94, and 0.97 respectively by using the themodelpredictions.Singhetal.[12]toverifytherelevance
hybridmodel,ontheEuropeancreditcarddataset,whileon of individual features in fraudulent detection, making sure
theCreditCardStimulationdatasetsimilarimprovementsare that the model not only attained great performance but also
obtained.Theydescribedtwodatasets,theEuropeandataset, added insights for improving the system of fraud detection.
and the stimulation dataset, that yielded precision-recall The proposed method achieved 98.5% accuracy with very
curvesareasof98.26%and99.37%,respectively,supporting high precision and recall rates, also outperforming baseline
themodelefficacy. models.
Similarly,Joshietal.[51]proposedhardvotingtoidentify This literature review of fraud detection systems (FDS)
fraudulenttransactionsbyintegratingmultipleclassifiersfor between 2015 and 2024 discusses major contributions and
credit card fraud detection using Decision Tree, Logistic denotes the gaps in existing models. While the reviewed
Regression,andNaiveBayes.However,theirmodeloutper- papers addressed issues such as class imbalance, concept
formed individual classifiers, and was able to detect fraud drift, and feature selection, it did not sufficiently enhance
withhigheraccuracy.Thestudyalsohighlightedthatensem- model adaptability and real-world applicability. Feature
blelearningmodelscanusedifferentclassifierstoovercome selection was neglected in many works so that the huge
thedifficultiesofclassimbalance.Thecaveatofthismethod dimensions with irrelevant features (like Shakya [24] and
isthatitisnotsufficientwherethereisconceptdrift,asitdoes Evan[26])wereincreasingthecomputationalcost.Methods
nottakeintoconsiderationtheneedforreal-timeadaptation like SMOTE and Tomek Links addressed class imbalance,
92044 VOLUME13,2025

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
but introduced synthetic noise that led to overfitting and adaptationareembedded,themodel’saccuracymaydegrade
loss of generalizability. Furthermore, many models like asnewfraudpatternsemerge.Furthermore,althoughSHAP
Shmatko’s [27] required manual feedback for data entry, values provided valuable insights into feature importance,
hampering transaction processing speed and system adapt- thecomputationaloverheadassociatedwithgeneratingthese
abilityastheprojectprogressed. valuesandperformingextensivehyperparametertuningmay
Finally, concept drift is a persistent challenge in fraud limitthescalabilityofthemodel,makingitlesspracticalfor
detection given that transaction behavior is dynamic and high-frequencytransactionenvironments.
can change with seasonality, new fraud techniques, and Table 1 summarizes these studies and their respective
consumer behavior. The traditional models (e.g., Logistic techniques as well as the strengths and limitations of the
Regression, Decision Trees, Random Forest, and XGBoost) methods.Theseresultsshowthat,despitevariousmethodsto
assumethatdatadistributionsdonotchangeovertime.This tackleclassimbalancealongwithdriftdetectionandfeature
assumptiondoesnotholdtrueforreal-lifepaymentsystems, selection, most of the models were not genuinely adaptive
where a sudden or gradual drift can occur, significantly inreal-time,nordidtheyaccommodatethecharacteristicsof
reducing the effectiveness of static models. Concept drift highdimensionaldatasetsorthechangingnatureoffraud.
can be categorized into two types: abrupt drift, where data Fortunately,theproposedmodeleffectivelyidentifiesand
patterns change suddenly, and gradual drift, where transac- reactstogradualdrift,whichsupportsthemitigationofthese
tion behavior evolves incrementally over time. or instance, effects.Byperpetuallyadjustingtothechangesinthetrans-
seasonal spending variations or subtle shifts in merchant action behavior, the model minimizes false positive rates
categories may gradually alter the decision boundaries of whilemaximizingdetection,mitigatingtheflawsofclassical
a model, making previously effective classification rules convergenceandtherefore,accommodatingdriftingdetection
obsolete. Gradual drift is particularly problematic since it models.
causestheperformanceofthedetectiontograduallydecrease Drift is one of the most important factors that affect
over time. As these changes happen unnoticed, the model detection performance. Fraudsters regularly modify trans-
keeps applying old rules and hence, a lot of false positives action characteristics (like transaction values, retailer types
are left unnoticed leading to worse and worse accuracy. or geographical areas), moving the decision boundary of
ModelsbasedonADWIN[36]candetectabruptdriftwith- the prototype overtime. If no drift detection is in place, the
out needing an initial reference set, and as such can be modelstrainedonhistoricaldatawillbecomestaleandinac-
prone to lose gradual and subtle changes, causing miss- curate,whichinherentinminimizationofdetectionaccuracy
ing patterns of potential frauds and degradation in model at higher levels specifically increase in false-positive and
performance. Similarly, Mulimani’s [42] approach, which degradation detection performance. Now think about push-
integratedensemble-basedresamplingwithdriftdetectionvia ing this process one step back in the chain and start using
KL divergence and Cramer’s V, ensured robustness but was drift-detectioninamoreproactivewaysothatyoucanmake
more computationally expensive, preventing it from obtain- yourmodelswithdynamictransactionpermutationstolearn
ingreal-timeprocessing. andadaptcontinuously.Asanexample,algorithmsthatcan
ThestudybyS.Joshietal.In[51]proposedanensemble detect gradual drift, such as EDDM, can be integrated with
learning approach where Decision tree, Logistic regressor popularalgorithmstocaptureabruptdrift,suchasADWIN,
and Naive Bayes classifiers are applied independently and so that both types of drift can be detected comprehensively.
are then combined through hard voting to detect fraud in Deployingthesestrategiesensuresthatthemodelkeepspace
creditcardstransactions.Theseresultsshowthatanensemble withevolvingfraudpatterns,maintainingabalancebetween
method was found to yield higher accuracy as compared to detection accuracy and adaptability. Previous models faced
anysingleclassifierinpredictionoffraudulentactivity.The difficult challenges with the complexity of the dataset as
only limitation of this approach is that hard voting is used manyofthemutilizednumeric-onlytabulardatasetssuchas
sonoadaptiveorincrementallearningstrategiesforconcepts KDDCupandCreditCarddatasets,whichlimiteditsapplica-
drift modeling are utilized once new instances are coming. bilitytorealdata,whichispredominantlytransactionaland
Furthermore,indynamicfrauddetectionscenarios,ensemble mixed(k+numeric).
learningtechniquesmightbeineffectivebecausetheyrelyon An ensemble approach was employed by Priya and
a static model architecture and do not easily adapt well to Uthra[25]andSarafandPhakatkar[44]tocombineclassifier
changesintransactionbehavior. outputs and increase classification accuracy but came with
ThemodelproposedbySinghetal.[12]hassomelimita- steepcomputationaloverheadsandthepotentialforsynthetic
tions.AlthoughSMOTEwasabletosolvetheclassimbalance noise. Moreover, Kajal and Kaur’s method [43] utilized the
problem, it also added synthetic noise to the dataset, which under sampling and Information Gain, but failed to address
could increase the risk of overfitting to the synthesized nonlinearfeatureinteractionsthustheirsolutionisnotflexi-
dataset and result in poor generalization to real-world data. bleenoughforreal-worldscenarios.
Furthermore,themodelisunawareofconceptdrift,animpor- Toovercometheselimitations,ahierarchicalfeatureselec-
tant challenge in credit card fraud detection, as transaction tionprocesswithMutualInformationandFeatureImportance
patterns change over time. If no mechanisms for real-time is applied to extract and rank relevant features, minimizing
VOLUME13,2025 92045

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
thenoiseandimprovingclassificationperformance.Inaddi- TABLE1. Summaryandcomparisonoffrauddetectiontechniquesin
tion, the proposed model is the first to combine EDDM literature.
and ADWIN to work together for dual drift detection to
retainbothsuddenchangesandgradualchanges.Thismodel
can therefore adapt dynamically to drift of transactions and
continuestoperformdetectionatahighlevel.Additionally,
theuseofConvolutionalNeuralNetworks(CNN)allowsthe
model to recognize complex patterns in transactions, guar-
anteeingefficient,real-timefrauddetectioninever-changing
environments.The enhancementscommenceaddressingthe
broadernatureoffraudattemptsandthelimitationsfoundon
previousapproaches,definedtheproposedmethodasamore
flexibleandreliablewayofactingagainstfraud.
III. METHODOLOGYANDTHEPROPOSEDMODEL
Thissectionoutlinesanapproachtodevelopinganimproved
methodologytoaddresslimitationsdiscussedintheprevious
section. Different challenges in fraud detection are handled
intheresearch,likeclassimbalance,computationaloverhead
and performance degradation owing to concept drift. It is
importanttogobeyondthesechallengesforafrauddetection
systemtobecomemorerobustandeffective.
This section describes the methodology used to develop
and evaluate the proposed model that is capable of han-
dlingconceptdriftandimbalanceddatasets.Therewerethree
distinct datasets utilized, each with unique characteristics
relevanttofrauddetection.Toensureeffectiveness,accuracy,
and robustness, multiple metrics were used to evaluate the
model’s performance. These steps are explained in detail as
follows:
A. DATASET
The following datasets were selected to test the model’s
abilitytodetectfraudandadapttodriftindifferentcontexts:
i. Kaggle’s first dataset contains European credit card
transactionsfrom2013andiscommonlyusedinfraud
detection research [50]. There are 31 features and
492instancesoffraudwithin284,807totaltransactions
in this dataset, providing a benchmark for detecting
fraudulentbehaviorunderclassimbalances.
ii. Data from a leading bank in the Gulf Cooperation
Council(GCC)regioncontains200featuresfromdebit
and prepaid card transactions in 2019. This dataset
provides insights into the model’s performance in an
operational banking environment with 120 fraudulent
transactionsoutof66,523totalrecords.
iii. A third dataset, from the UCI Repository [45], con-
tains labeled email data for spam detection research.
57featureswereextractedfromemailtexttoprovidea
non-financial context for benchmarking concept drift
handling. Using the spam dataset, the proposed drift
detectiontechniquescanbetestedinscenariosofgrad-
ualandabruptdrift.
AsummaryofthedatasetsisshowninTable2:
92046 VOLUME13,2025

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
TABLE2. Datasetsspecifications. istotacklethemajorchallengesoffrauddetection,including
dataquality,relevantfeatures,imbalancebetweenclassesand
conceptualdriftpatterns.
1) PHASE1-DATAPREPROCESSING
Thepurposeofthisphaseistopreparethedatasetforeffective
andaccuratemodeltraining.Therearethreestepsinvolvedin
thedatapreprocessing:Datacleansing,featureselectionand
handlingclassimbalancewithADASYN.
|     |     |     |     | Data       | Cleansing:  |          | This step | aims               | to reduce   | noise         | and      |
| --- | --- | --- | --- | ---------- | ----------- | -------- | --------- | ------------------ | ----------- | ------------- | -------- |
|     |     |     |     | irrelevant | information |          | in a      | dataset to         | enhance     | data          | quality. |
|     |     |     |     | Cleaning   | the data    | (missing |           | values and         | duplicates) | and           | thus,    |
|     |     |     |     | a dataset  | that        | can be   | analyzed. | In payment         |             | systems       | which    |
|     |     |     |     | contain    | mixed       | types    | of data   | (i.e., categorical |             | and numerical |          |
features),anintegratedstrategyisrequiredduringthebalanc-
ingandfeatureselectionprocess.
Theframeworkfortheresearchisstructuredintwoparts
|     |     |     |     | Handling | Class |     | Imbalance | with | ADASYN: | ADASYN |     |
| --- | --- | --- | --- | -------- | ----- | --- | --------- | ---- | ------- | ------ | --- |
inwhicheachstagebuildsonthefindingsofthelast.Fig.11
|     |     |     |     | (Adaptive | Synthetic |     | Sampling) | is a | method | used | to deal |
| --- | --- | --- | --- | --------- | --------- | --- | --------- | ---- | ------ | ---- | ------- |
illustratesthedesignedfrauddetectionresearchframework.
|              |          |                 |                  | with class | imbalance, |     | which | is especially | prevalent |     | in fraud |
| ------------ | -------- | --------------- | ---------------- | ---------- | ---------- | --- | ----- | ------------- | --------- | --- | -------- |
| i. The first | phase of | data processing | has three steps: |            |            |     |       |               |           |     |          |
detectiondatasets:
datacleansing,featureselectionandresampling.Data
|           |              |               |                  | i generates |     | synthetic | instances |     | of the | minority | class |
| --------- | ------------ | ------------- | ---------------- | ----------- | --- | --------- | --------- | --- | ------ | -------- | ----- |
| cleansing | is the first | phase of data | quality in which |             |     |           |           |     |        |          |       |
(fraudulent),focusingmoreonregionswherelearning
datagetsenhancedandcorrected.Datacleansingisfol-
isdifficult.Thishelpsinbalancingthedatasetbyensur-
lowedbyfeaturesselectiontoselectrelevantfeatures.
ingthatareaswithfewerbutsignificantfraudcasesare
| Finally, | The Resampling | techniques | has been utilized |     |     |     |     |     |     |     |     |
| -------- | -------------- | ---------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
to solve the class imbalance problem and balance the adequatelyrepresented.
|     |     |     |     | ii Adapts |     | sampling | to  | the underlying |     | data | distribu- |
| --- | --- | --- | --- | --------- | --- | -------- | --- | -------------- | --- | ---- | --------- |
dataset.Thus,combiningthesestepsenforcesefficient
|     |     |     |     | tion | to enhance |     | the model’s | sensitivity |     | to fraudulent |     |
| --- | --- | --- | --- | ---- | ---------- | --- | ----------- | ----------- | --- | ------------- | --- |
modeltraininganddetectsfraudaccurately.
transactions.
| ii. The second | phase deals | with concept | drift detection. |     |     |     |     |     |     |     |     |
| -------------- | ----------- | ------------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
The use of Convolutional Neural Networks (CNN), Thus, Phase 1 is focused on preparing a valid dataset to
Early Drift Detection Methods (EDDM), and sliding improvemodelaccuracy,noisereductionandclassimbalance
windows allows the detection of both gradual and correctionusingdatacleansing,MIandK-Bestfeatureselec-
| abruptdriftsindata. |     |     |     | tionandADASYNbalancing. |             |            |             |                    |               |            |           |
| ------------------- | --- | --- | --- | ----------------------- | ----------- | ---------- | ----------- | ------------------ | ------------- | ---------- | --------- |
|                     |     |     |     | Feature                 | Selection:  |            | To minimize | the                | size          | of the     | dataset,  |
|                     |     |     |     | Mutual                  | Information |            | (MI)        | and SelectKBest    |               | are        | utilized  |
|                     |     |     |     | for better              | feature     | selection. |             | MI measures        | the           | dependence |           |
|                     |     |     |     | between                 | features    | and        | targets     | (fraud/non-fraud), |               | producing  |           |
|                     |     |     |     | scores that             | rank        | the        | features.   | SelectKBest        | then          | selects    | only      |
|                     |     |     |     | those with              | the         | strongest  | association |                    | to the target |            | variable, |
removingirrelevantorredundantones.Thisresultsinamore
accurateandinterpretablemodelbyeliminatinglow-impact
features.Bothmethodsarepowerfulforfrauddatasets.Labe-
|     |     |     |     | lEncoder() | is used | for | ordinal | data, while | OneHotEncoder() |     |     |
| --- | --- | --- | --- | ---------- | ------- | --- | ------- | ----------- | --------------- | --- | --- |
isappliedtonon-ordinalcategoricaldata.
2) PHASE2-DETECTIONMODEL
|     |     |     |     | This phase | focuses |     | on building | a dynamic | model |     | of fraud |
| --- | --- | --- | --- | ---------- | ------- | --- | ----------- | --------- | ----- | --- | -------- |
detectionwhichwouldidentifyfraudulenttransactionsinreal
|     |     |     |     | time with | a high | degree | of      | accuracy,     | and most | importantly |     |
| --- | --- | --- | --- | --------- | ------ | ------ | ------- | ------------- | -------- | ----------- | --- |
|     |     |     |     | a model   | that   | would  | look at | data patterns | that     | evolve      | due |
FIGURE12. Proposedmethodologyforenhancedfrauddetectionwith
pre-processinganddriftdetectiontechniques. to changing tactics of fraud. 3 mechanisms are the building
blocksforthedetectionscheme;theyareConvolutionalNeu-
ralNetworks(CNN),EarlyDriftDetectionMethod(EDDM)
| B. METHODOLOGY |     |     |     | andADaptiveWINdowing(ADWIN). |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
The methodology proposed consists of two phases: Data CNN is further applied as a fundamental classifica-
PreprocessingandDetectionModel.Thegoalofeachphase tion model to identify fraudulent transactions. This model
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     | 92047 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
automaticallyidentifiescomplexinterrelationsintransaction
datawhichtraditionaltechniquescouldmiss.TrainingCNN
on the Phase 1 dataset that is refined and balanced helps to
distinguishrealtransactionsversusfraudattemptsbetter.
This method of monitoring the drift or change in the
model’serrorondifferentupcomingbatchesofdatabasedon
thepreviousbatchesofdataistermedasEarlyDriftDetection
Method (EDDM) which can detect changes in distribution
as well as fraudulent behavior. It constantly monitors the
averagedistancebetweenerrorstopickupsuddenorgradual
changesincharacteristicsoftransactions.Itenablesthesys-
tem to respond quickly to new patterns in fraud by sending
alerts when the error rate surpasses predefined warning and
controlthresholds.
Theadaptivewindowing(ADWIN)techniqueworksalong
with EDDM to determine drift by adjusting the window
sizeaccordingtothevolatilityofrecenttransactionpatterns.
In ADWIN, the window size is dynamically adjusted to
keep the detection model focused on current data trends,
simplifyingtheprocessofdetectinggenuineshiftsinfraudu- FIGURE13. DriftdetectionWorkflowinfrauddetectionsystemusing
CNN,EDDM,andADWIN.
lentbehaviorfromtemporaryabnormalities.Maintainingthe
model’saccuracyandminimizingfalsepositivesisdependent
onthiscomponent. gradual drift if the error accumulation exceeds that gradual
Toaddressclient-leveldriftandbehavioralheterogeneity, threshold,typifyinggradual,incrementalchangesinthedata
theADWINcomponentdynamicallyadaptsitswindowsize distribution. In contrast, the drift in bringing to abrupt drift
perclienttransactionstream,enablinglocalizeddetectionof is sudden—and considerable. At this point, if a drift is
shiftingbehaviors.Thisensuresthatthemodelremainssen- detected, the system retries the CNN model or retrains its
sitive to individual user-level changes in spending patterns, weightstoadjusttothechangesinthepattern.
supporting personalized fraud detection in heterogeneous If the Out-of-Control Level condition is False, the next
environments. to be evaluated is for the Warning Level. At this point,
Fig.12,showsastructuredapproachtofrauddetectionthat EDDMtendstomonitorslightchangesfromthedatastream.
integrates Convolutional Neural Networks (CNNs), Early In case the warning condition holds True, EDDM trig-
Drift Detection Method (EDDM), and ADaptive WINdow gers ADWIN (Adaptive Windowing) for further validation.
(ADWIN) to continuously observe and adapt to changing ADWIN explicitly addresses this information gap by deter-
transaction patterns. This framework accommodates both mining whether the observed shifts are true changes in data
abrupt and gradual drifts in transactional data in order to distributionorjusttemporaryfluctuations.ADWINconfirms
maintain accuracy and be responsive to changing fraud tac- the drift type by adapting the size of its sliding windows
tics. In the CNN model, data such as transaction amounts, dynamically and conducting statistical tests. In the occur-
merchant details, and entry mode are extracted after initial rence of drift detection for the warning phase, ADWIN
training.Theextractedfeaturesareusedtodetectanomalies classifies the drift type within gradual or abrupt, the same
andfraud. asfortheout-of-controlphase.Inthecasewherenodriftis
ThefirststepofthedetectionframeworkisInitialModel confirmed,thesystemrevertsbacktoNoDriftDetectedand
Training using CNN, where the CNN model is trained with continuesmonitoring.
historicaltransactionaldata,whichlearnscomplexrulesthat Incasethewarninglevelandout-of-controllevelsarenot
differentiate between normal and fraudulent transactions. satisfied, the system will stay on tracking the data stream
This basic step guarantees that this CNN is implemented in whereitcontinuestohaveEDDMandADWINonstandbyto
real-time,meaninganyincomingtransactioncanbedynami- detect possible changes. This keeps it from generating false
callyclassifiedasabaselineforfrauddetection. alarms while being sensitive to both subtle and significant
Afterthesystemisinproduction,theEDDM(EarlyDrift drifts.
Detection Method) runs and monitors errors of the pre- Upon confirmation of drift (EDDM or ADWIN), the
dictions in production in near-real-time. EDDM assesses systemupdatesDriftDetectionMetricsandimplementsnec-
for potential drift with two levels of thresholds: Warning essary actions. In the case of gradual drifts, it updates its
Level (0.1) and Out-of-Control Level (0.1). If one of the model weights to model the changing data according to the
significantdeviationsinthedatapatternsexceedstheout-of- changesinthisdata.Youarerequiredtoperformacomplete
controlthreshold,the EDDMdetectsthedriftandclassifies retraining process with this CNN model every time it is a
it as either Gradual Drift or Abrupt Drift. We identify a sudden drift, which we want to avoid as stated above. This
92048 VOLUME13,2025

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
iterative process is essential for keeping the system flexible chance of false positives is decreased, meaning that
enoughtorespondtotheevolvingpatternsoffraud. fewerlegitimatetransactionswillbeflaggedasfraud-
Table 3 presents the main components and objectives of ulent,reducingunnecessaryalertsanddisruptions.
EDDMandADWINusedinourapproachfordetectingdrift iii. Recall: Recall is the number of relevant instances
and updating the model. When a change occurs, the system (actualfraudulenttransactions)retrievedbythemodel
returns to the monitoring step and continues analyzing the overthetotalnumberofinstancesthatshouldhavebeen
data stream for further variations. This approach makes the retrieved (actual fraudulent transactions). So, in the
system more reliable, keeps accuracy high, and allows it to caseofdriftdetection,ahighrecallmakessurethatthe
adjustquicklytochangesinfraudpatterns. model adapts as quickly as possible to changes intro-
|     |     |     |     |     | duced by | the | concept drift, | and | do not | let undetected |     |
| --- | --- | --- | --- | --- | -------- | --- | -------------- | --- | ------ | -------------- | --- |
fraudulentpatternsmanifest.Thoughdriftchangesthe
TABLE3. SummaryofEDDMandADWINparametersfordriftdetection
andmodelupdates. natureoffaketransactions,havingahighrecalllimits
|     |     |     |     |     | false negatives |     | (there will | be  | frauds they | miss), | ulti- |
| --- | --- | --- | --- | --- | --------------- | --- | ----------- | --- | ----------- | ------ | ----- |
matelyholdingthesystemsafefromadaptingthreats.
|     |     |     |     |     | In drift | scenarios, | low recall | means    | non-adaptation |          | to    |
| --- | --- | --- | --- | --- | -------- | ---------- | ---------- | -------- | -------------- | -------- | ----- |
|     |     |     |     |     | changing | patterns,  | hence      | the need | for            | constant | moni- |
toringandretraining.
iv. F1Score:TheF1Scoreistheharmonicmeanofpre-
cisionandrecall,whichbalancesthetrade-offbetween
|     |     |     |     |     | false positives |          | and false      | negatives.   | In            | drift detection, |         |
| --- | --- | --- | --- | --- | --------------- | -------- | -------------- | ------------ | ------------- | ---------------- | ------- |
|     |     |     |     |     | a high          | F1 Score | indicates      | that         | the model     | has              | adapted |
|     |     |     |     |     | to the          | changes  | in transaction |              | distributions |                  | without |
|     |     |     |     |     | sacrificing     | its      | flexibility    | to correctly |               | identify         | fraud.  |
Sincebothprecisionandrecallgetaffectedbydrifting
|     |     |     |     |     | concepts, | a high | F1 Score | guarantees |     | that the | model |
| --- | --- | --- | --- | --- | --------- | ------ | -------- | ---------- | --- | -------- | ----- |
capturesfraudulenttransactionswithouthurtingsensi-
tivityorspecificityalongtheevolutionofthedata.
|     |     |     |     |     | v. ROC-AUC | (Receiver | Operating    |     | Characteristic |     | - Area  |
| --- | --- | --- | --- | --- | ---------- | --------- | ------------ | --- | -------------- | --- | ------- |
|     |     |     |     |     | Under      | Curve):   | Ther ROC-AUC |     | evaluates      | a   | model’s |
C. EVALUATIONMETRIC capacitytoseparatefraudulenttransactionsfromlegit-
| To gain | an overall | perspective | about the model | abilities, |            |     |                   |     |         |         |     |
| ------- | ---------- | ----------- | --------------- | ---------- | ---------- | --- | ----------------- | --- | ------- | ------- | --- |
|         |            |             |                 |            | imate ones | at  | various threshold |     | levels. | ROC-AUC | is  |
differentmetricswereusedtobeabletoanalyzetheperfor- criticalindriftdetectionasitservestoassesshowwell
manceofthemodel.Thesemetricscomprised:
|     |     |     |     |     | the model | identifies | a   | supervisory | signal | so  | that the |
| --- | --- | --- | --- | --- | --------- | ---------- | --- | ----------- | ------ | --- | -------- |
i. Accuracy:Accuracyistheproportionofcorrectlyclas- classification boundaries shift dynamically with drift.
sifiedinstancesoverthetotalnumberofinstances.Drift This means the significantly high ROC-AUC value
detectionincreditcardorcardpaymentfrauddatasets indicates the model’s ability to determine between
requireshighclassificationperformanceastransaction legalizedtransactionandfraudulenttransactionasthe
patternsevolveovertime,makingaccuracycriticalfor characteristic of the transaction changes over a cer-
successfuldetection.Nonetheless,evenifthemodelis taintime.IftheROC-AUCremainsconsistentlyhigh,
highlyaccurate,thatmeanslessinimbalanceddatasets this indicates that even as drift affects the underlying
suchasthisonewherethelegitimatetransactionsout- data distribution, the model maintains its discrimina-
number the fraudulent ones. High accuracy only tells tive capability over time and is thus robust to such
| you | that | the model is | broadly correct, | but does not | change. |     |     |     |     |     |     |
| --- | ---- | ------------ | ---------------- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
meandrifthasbeendetected,northatminority(fraud) vi. Drift Detection Rate: The Drift Detection Rate mea-
examplesareclassifiedcorrectly.Inaddition,accuracy sures the model’s sensitivity to detecting changes in
alonemightnotreflecttheshiftsinthedistributionof the underlying data distribution over time. With the
data resulting from drift, and can cause the model to prevalence of emerging patterns amongst fraudulent
degradeifnotdetectedintime. transactions,detectingdriftallowsthemodeltoretrain
ii. Precision: Precision is the ratio of correctly identified and adapt to changes in that process quickly. With-
positive observations to the total predicted positive out a high enough drift detection rate, the model can
observations. In drift detection uses cases; precision become outdated speculation, resulting in increased
conveys that change in patterns occurring in fraud false negatives (missed fraud) or false positives (false
instancesduetodriftwouldnotleadtonightmare-level alarms). Drift detection: The detection of shifts in the
false positives. As drift takes place, fraudsters may distributionofincomingdata.
adapt to it by adjusting their behavior, causing trans- vii. ConfusionMatrix:Theconfusionmatrixdividesresult
actioncharacteristicstodiffer.Withhighprecision,the ofclassificationintotruepositives,truenegatives,false
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     | 92049 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
positives and false negatives (TP, TN, FP, FN). The TABLE4. Maincodecomponents.
confusionmatrixcanbeusedfordriftdetectioninfraud
detectionmodelstoseehowwellthemodelisableto
| stay     | within class | prediction | accuracy |          | as drift | occurs. |     |     |     |     |     |
| -------- | ------------ | ---------- | -------- | -------- | -------- | ------- | --- | --- | --- | --- | --- |
| Tracking | this         | matrix     | through  | time can | show     | whether |     |     |     |     |     |
themodel’ssensitivitytochangingpatternsoffraudis
gettingbetterorworse,allowingforactionableinsights
onretrainingandrefinement.
| The selection  | of these | evaluation     | metrics     | was         | performed | in       |     |     |     |     |     |
| -------------- | -------- | -------------- | ----------- | ----------- | --------- | -------- | --- | --- | --- | --- | --- |
| order to keep  | high     | classification | performance |             | of the    | model    |     |     |     |     |     |
| while adapting | to the   | concept        | drift.      | These       | metrics   | together |     |     |     |     |     |
| provide an     | overview | of the         | model’s     | performance | over      | time,    |     |     |     |     |     |
focusingonhowwellthemodelisperformingandhowwell
itisadaptingtochangesastheyoccur.
D. IMPLEMENTATIONDETAILS
| Fraud detection | using   | various   | kinds | of python     | libraries | tai-      |     |     |     |     |     |
| --------------- | ------- | --------- | ----- | ------------- | --------- | --------- | --- | --- | --- | --- | --- |
| lored for       | machine | learning, | data  | preprocessing |           | and drift |     |     |     |     |     |
detectionwereperformedingooglecolab:
| i TensorFlow/Keras: |     | used | to create | Convolutional |     | Neu- |     |     |     |     |     |
| ------------------- | --- | ---- | --------- | ------------- | --- | ---- | --- | --- | --- | --- | --- |
ralNetworks(CNN)forinvestigatingcomplexpatterns
| in transaction |     | data. CNNs | constructs |     | multiple | layers: |     |     |     |     |     |
| -------------- | --- | ---------- | ---------- | --- | -------- | ------- | --- | --- | --- | --- | --- |
Conv1D,MaxPooling1D,Densetolearncomplexpat-
|     |     |     |     |     |     |     | A. REALDATASET |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
ternsfromlargeamountsofdata. Table 5 illustrates the results obtained over the Credit Card
| ii TensorFlow/Keras: |     | used | to create | Convolutional |     | Neu- |     |     |     |     |     |
| -------------------- | --- | ---- | --------- | ------------- | --- | ---- | --- | --- | --- | --- | --- |
datasetapplyingtotheADASYNbalancingtechniqueandby
ralNetworks(CNN)forinvestigatingcomplexpatterns
carryonthefeatureselectionprocess,andalsocomparesthe
in transaction data. CNNs constructs multiple layers: performance achieved by those predictive models that were
Conv1D,MaxPooling1D,Densetolearncomplexpat-
|     |     |     |     |     |     |     | built using | different | sets of four | or fewer | distinct features, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ------------ | -------- | ------------------ |
ternsfromlargeamountsofdata. accuracy,precision,recallandF1heretooarereported.The
iii River: Used for drift detection Because River is configurationwith90featuresyieldedthebestperformance
| designed | for | streaming | data, | this library | is  | utilized |     |     |     |     |     |
| -------- | --- | --------- | ----- | ------------ | --- | -------- | --- | --- | --- | --- | --- |
metricsamongthosetested,featuring100%accuracy,100%
for drift detection. River was used to implement the precision, and 100% recall. This indicates that the under-
| EDDM | and ADWIN |     | techniques, | which | perform | well |             |              |       |            |                   |
| ---- | --------- | --- | ----------- | ----- | ------- | ---- | ----------- | ------------ | ----- | ---------- | ----------------- |
|      |           |     |             |       |         |      | lying model | is detecting | fraud | with world | class sensitivity |
forsuddenandgradualchanges,respectively. and little in the way of false positives or false negatives.
The10-features(99.99%)and20-features(99.99%)datasets
| Table 4 outlines | the | main code | components |     | utilized | in each |                                                     |     |     |     |     |
| ---------------- | --- | --------- | ---------- | --- | -------- | ------- | --------------------------------------------------- | --- | --- | --- | --- |
| stage:           |     |           |            |     |          |         | alsoperformedverywell,achievinghighaccuracy(99.98%) |     |     |     |     |
andperfectrecall,respectively,indicatinghighefficiencyin
| IV. RESULTSANDDISCUSSION |     |     |     |     |     |     | identifyingafraudulenttransaction. |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
This section provides the evaluation outcomes, where Real However,whilefewerfeaturesperformedwell,theymight
notretainallimportantfraud-relatedpatternsandthiscould
Dataset,theCreditCardDataset,andtheSpamDatasetwere
utilized in the study to evaluate the model’s performance in affectgeneralizability.Highscoringsetsacrosseverymetric
detectingdriftandfraud.Beforeperformingtheactualexper- occurred at features 30, 50, and 80, indicating the optimal
iments,eachdatasetwasoptimizedtoimprovetherobustness selectionsoffeatures.40,60and70featureswerealsofound
and reliability of drift detection using ADASYN for class thatcouldbehighlightedbuttheywerenotbalancemetricsas
metricswerebetterforPrecisionandF1scores.Thisindicates
| balancing. | Then the | features | were | extracted | using | Mutual |     |     |     |     |     |
| ---------- | -------- | -------- | ---- | --------- | ----- | ------ | --- | --- | --- | --- | --- |
Information and SelectKBest. Then the integrated approach thatalthoughthemajorityoffeaturecombinationsused,after
ofEDDM,ADWINandCNNwasusedtoevaluatetheper- ADASYN and feature selection, provided highly positive
formanceofthemodelasitdrifted. results, some combinations —especially at 90 and above—
Thefindingsillustratethecontributionofeachfeatureset buoyedanoptimal,repeated,andgooddetectionpotential.
tothemodel’sperformancemetrics,whichincludeAccuracy,
Precision,Recall,F1Score,ROCAUC,DriftDetectionRate, B. CREDITCARDDATASET
and False Positive Rate. The evaluation highlights the most The performance results of the Credit Card dataset post
effective feature configuration for each dataset, resulting in feature selection and data balancing is detailed in table 5.
the highest detection accuracy and the ability to adapt to A 30-feature set with 99.88% accuracy, 99.76% precision,
changingfraudpatterns. and 100% recall was the most balanced across all metrics
| 92050 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
of the tested configurations. In the credit card dataset, the TABLE5. Resultofalldatasetsduringpre-processingstage.
modelaccuratelydetecteddriftandfraudulentinstanceswith
minimalfalsepositivesandfalsenegatives.
| All other    | lower         | feature | configurations |           | (10,    | 15, 20 and  |
| ------------ | ------------- | ------- | -------------- | --------- | ------- | ----------- |
| 25 features) | all           | scored  | well, getting  |           | between | 0.9901 and  |
| 0.9975       | for accuracy, | and     | everything     | including |         | the 10 fea- |
turesscored0.9900andaboveforF1.Assuch,theresulting
30-featureconfigurationistheoptimalcombinationofaccu-
| racy and | adaptability | regarding |     | drift | and fraud | detection, |
| -------- | ------------ | --------- | --- | ----- | --------- | ---------- |
throughfeaturesselectionandbalancing.
C. ESPAMDATASET
Table5presentsperformanceresultsofSpamdataset;results
afteraddressingdatacleansing,featureselectionanddatabal-
ancingissues,toillustratetheimpactonaccuracy,precision,
recallandF1score.With55features,theresultsshowedthe
mostbalancedperformancewithaccuracy0.9306,precision
0.9262,recall0.9448,F1score0.9354andROCAUC0.9706.
Thesefindingsimplythatitaidsthemodeltoidentifyspam
instanceswithsignificantsensitivityaswellasminimalfalse
positivesaswellasminimalfalsenegativesinthesefunctions.
| Overall, | other lower | number | of  | features | also achieved | good |
| -------- | ----------- | ------ | --- | -------- | ------------- | ---- |
accuracylike5and10featuresbutsignificantlylowerpreci-
sionandF1score,indicatingmorefalsepositivecases.The
performanceimprovementisseenbetween15and30feature
TABLE6. Resultofalldatasetduringdetectionstage.
countsbutthebalanceachievedby55-featureconfiguration
werenotfoundinconfigurationwithlessfeatures.
The55-featuresetisthebestselectionfortheSpamdataset,
| providing   | a balanced | method    | for    | correctly | identifying | both    |
| ----------- | ---------- | --------- | ------ | --------- | ----------- | ------- |
| spam and    | non-spam   | instances | with   | strong    | precision,  | recall, |
| and overall | accuracy.  | The       | chosen | features  | provide     | strong  |
detectionefficacywhilereducingerrors,makingitappropri-
atefordynamicdatacontexts.
D. DRIFTDETECTIONRESULT
| The final | performance |     | of drift | detection | was evaluated | on  |
| --------- | ----------- | --- | -------- | --------- | ------------- | --- |
thedatasetsusingEDDM,ADWIN,andCNNmethodsafter
resamplingandfeatureselection.Basedontheresultsofthis
| evaluation, | the         | model has     | demonstrated |           | its ability   | to adapt     |
| ----------- | ----------- | ------------- | ------------ | --------- | ------------- | ------------ |
| to evolving | data        | distributions | across       | a         | variety       | of datasets. |
| The final   | performance |               | of drift     | detection | was evaluated | on           |
thedatasetsusingEDDM,ADWIN,andCNNmethodsafter scenario where there is a need to identify fraudulent cases
resamplingandfeatureselection.Basedontheresultsofthis accuratelybutalsolimitfalsealarms.TheSpamDataset(55
evaluation, the model has demonstrated its ability to adapt features) achieved 99.34% accuracy, 100% precision, and
to evolving data distributions across a variety of datasets. 98.69%recall,specifictothevariant.’Thesefindingsvalidate
Table6showsthefinalperformanceresult therobustperformanceofthemodeltodetectdifferencesin
According to Table 6, the feature selection analysis for datasets.Inaddition,theresultsdemonstratetheapplicability
the Real Dataset with 90 features, produced the best detec- of the methodology in more general sense beyond financial
tionresultswithanaccuracy,precisionandrecallrateequal fraud detection, as they highlight its capacity to cope with
to 100%. This demonstrates that the model is able to pick changingdatadistributions.
up on shifting transactional behaviors, whether gradual or Figure14illustratesthedriftdetectionoverlapusingVenn
sudden. For the Credit Card Dataset, the set of 30 fea- diagramontheCreditCardDataset.AspertheVenndiagram,
tures provided 100% accuracy and 100% F1 Score. This thetotalof284314driftsdetectedontheCreditCardDataset
balancemaintainshighsensitivitywhilereducingfalsepos- as seen from the Venn diagram in Fig. 10 EDDM detected
itives which is critical to fraud detection. A well-balanced 284,313 drifts, and 100% drifts was detected by EDDM.
precision and recall will provide a reliable model in a real ADWINonlyuniquelydetected1drift,whichwasagradual
VOLUME13,2025 92051

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
one.Therewere476abruptdriftsand283,838gradualdrifts.
EDDMshowsahighalignmentwithADWINindicatingthat
EDDMcapturesallimportantdriftswithonly1misseddrift
(gradual).ThisdemonstratesthatEDDMisasoundmethod
forcapturingboththesuddenchangesandthosethathappen
moregradually,inthisdataset.
|     |     |     |     |     |     | FIGURE16. | Driftdetectionoverlapfortherealdataset. |           |      |     |      |                 |     |
| --- | --- | --- | --- | --- | --- | --------- | --------------------------------------- | --------- | ---- | --- | ---- | --------------- | --- |
|     |     |     |     |     |     | In most   | of the                                  | datasets, | EDDM | was | able | to successfully |     |
capturemostofthedrifts,includingabruptaswellasgradual
conceptdrifting.ADWIN,ontheotherhand,provedtofind
|     |     |     |     |     |     | few drifts   | missed | by EDDM     |     | and guaranteed    |     | that | no major |
| --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------- | --- | ----------------- | --- | ---- | -------- |
|     |     |     |     |     |     | drift events | went   | undetected. |     | The complementing |     |      | perfor-  |
FIGURE14. Driftdetectionoverlapforthecreditcarddataset. mance of both techniques demonstrates their robustness in
|     |     |     |     |     |     | achieving | high | detection | sensitivity | together. |     | Utilizing | both |
| --- | --- | --- | --- | --- | --- | --------- | ---- | --------- | ----------- | --------- | --- | --------- | ---- |
Figure15illustratesthedriftdetectionoverlapusingVenn
|         |              |          |     |              |          | EDDM    | and ADWIN   | at     | different | stages | improves  | efficiency |     |
| ------- | ------------ | -------- | --- | ------------ | -------- | ------- | ----------- | ------ | --------- | ------ | --------- | ---------- | --- |
| diagram | on the ESPAM | Dataset. | As  | per the Venn | diagram, |         |             |        |           |        |           |            |     |
|         |              |          |     |              |          | without | sacrificing | either | speed     | or     | accuracy, | making     | the |
thetotalof2,792driftswithEDDMcapturing100%ofthem.
approachmoresuitableforreal-timeenvironments.
| ADWIN | did not identify | any | unique | drifts, confirming | that |     |     |     |     |     |     |     |     |
| ----- | ---------------- | --- | ------ | ------------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Whilethedual-driftdetectorcanenhanceitsadaptability,
| EDDM alone | was capable | of  | detecting | all critical | changes. |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
itdoescauseasmallcommunicationandcomputationalover-
Thedriftsincluded75abruptdriftsand2,717gradualdrifts.
headespeciallyinthedriftvalidationsteps.Nevertheless,this
TheseresultsemphasizetheeffectivenessofEDDMinidenti-
isreducedbyonlyupdatingthemodelwhereadrifthasbeen
fyingchangesinthisdataset,ensuringnodriftinstanceswere
confirmed.
overlooked.
E. PERFORMANCECOMPARISON
|     |     |     |     |     |     | The performance |         | of            | various   | drift      | detection     | and       | feature   |
| --- | --- | --- | --- | --- | --- | --------------- | ------- | ------------- | --------- | ---------- | ------------- | --------- | --------- |
|     |     |     |     |     |     | selection       | methods | are           | displayed | in         | Table         | 9 for the | Credit    |
|     |     |     |     |     |     | Card dataset.   |         | When compared |           | to earlier | studies,      |           | the pro-  |
|     |     |     |     |     |     | posed model     | yields  | superior      |           | results    | in terms      | of        | accuracy, |
|     |     |     |     |     |     | precision,      | and     | recall.       | Table     | 7 compares | results       |           | from the  |
|     |     |     |     |     |     | Credit Card     | dataset | with          | other     | studies    | demonstrating |           | the       |
proposedmodelenhanceddetectionofdriftandclassification
performance.
|           |                                          |     |     |     |     | In Table         | 8, the             | Spam          | dataset      | results    | are compared |               | across   |
| --------- | ---------------------------------------- | --- | --- | --- | --- | ---------------- | ------------------ | ------------- | ------------ | ---------- | ------------ | ------------- | -------- |
|           |                                          |     |     |     |     | studies,         | emphasizing        | the           | current      | approach’s |              | improved      | drift    |
|           |                                          |     |     |     |     | detection        | and classification |               | performance. |            | The          | Spam          | dataset  |
|           |                                          |     |     |     |     | was selected     | because            |               | it also      | exhibits   | concept      | drift,        | so it    |
|           |                                          |     |     |     |     | can be           | also part          | of evaluation |              | to confirm | the          | effectiveness |          |
| FIGURE15. | DriftdetectionoverlapfortheESPAMDataset. |     |     |     |     |                  |                    |               |              |            |              |               |          |
|           |                                          |     |     |     |     | of the technique |                    | using         | different    | dataset    | financial    |               | and non- |
Figure16illustratesthedriftdetectionoverlapusingVenn financialdatasets.Byapplyingtheproposedmethodologyto
diagram on the Real Dataset. As per the Venn diagram, the anon-financialdatasetwithdrift,theabilityoftheproposed
total of 66,402 drifts detected by EDDM. For this dataset, methodology to detect changes and maintain classification
ADWIN did not identify any distinct drift as like for the performanceacrossdifferentdomainsisvalidated.Thishigh-
ESPAM dataset. In summary, EDDM achieves 109 abrupt lightstheadaptabilityofourapproachtodatasetswheredata
driftsand66,293gradualdrifts.Suchbehaviorsubstantiates distributionevolvesovertime.
that when functioning with real time events, EDDM is able InTable9,theRealdataset’shighresultssupporttheeffec-
toward detect drifts belligerently (observing no omission of tivenessoftheproposedmethodology.Asaresult,themodel
anygenuinedrifts)whichrecommendsitsrealismforgenuine achievednear-perfectdetectionmetrics,suchasaccuracyof
applicationwherehighcompassfordriftsisvital. 99.99%,precisionof99.99%,driftdetectionrateof99.99%,
| 92052 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
TABLE7. Performancecomparisononcreditcarddataset. TABLE9. Resultofdetectionstageusingrealdataset.
|     |     |     | However,  | it is also | important | to            | evaluate | its stability    | when |
| --- | --- | --- | --------- | ---------- | --------- | ------------- | -------- | ---------------- | ---- |
|     |     |     | evaluated | on various |           | data subsets. | K-fold   | cross-validation |      |
|     |     |     | with K=5  | was        | employed  | to accomplish |          | this. Table      | 10   |
presentstheoutcomesacrossmanytestfolds,indicatingthat
TABLE8. PerformancecomparisononSPAMdataset. accuracy, precision, recall, and F1-score remain consistent.
|     |     |     | The model’s | performance |      | is not         | affected | by how    | the data |
| --- | --- | --- | ----------- | ----------- | ---- | -------------- | -------- | --------- | -------- |
|     |     |     | are split,  | indicating  | that | it is reliable | across   | different | data     |
distributions.
TABLE10. Resultsusing5-foldcross-validation.
|     |     |     | Table | 11 compares |     | the proposed | model’s | performance, |     |
| --- | --- | --- | ----- | ----------- | --- | ------------ | ------- | ------------ | --- |
evaluatedusingK-FoldCross-Validation,withexistingstud-
| demonstrating | exceptional robustness | in handling complex, |     |     |     |     |     |     |     |
| ------------- | ---------------------- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
iesontheCreditCardandSpamdatasets.Theresultsindicate
mixeddatatypes. that the proposed approach achieves higher accuracy, pre-
|     |     |     | cision, recall, | and | F1-score | compared | to  | previous | methods. |
| --- | --- | --- | --------------- | --- | -------- | -------- | --- | -------- | -------- |
F. K-FOLDCROSS-VALIDATION FortheCreditCarddataset,themodelrecordedanaccuracy
The comparison results earlier showed that the proposed of 0.99999, surpassing the 0.97000 reported by Kajal et al.
modelachievesbetterperformancethantheexistingmethods. [43]. As a result, the model effectively detected all drift
| VOLUME13,2025 |     |     |     |     |     |     |     |     | 92053 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
occurrenceswitharecallof0.99999.Saraf&Phakatkar[44] customized for real-time applications, in contrast to intri-
reported a recall of 0.94, which indicates that certain dis- cate ensemble models. The ability to adapt conducts future
tribution shifts may have been missed. Using the Spam research,especiallyforintegratingonlinelearningtoenhance
dataset, the proposed model was able to recognize evolving adaptabilitytochangingfraudpatternsinbothfinancialand
patterns with an accuracy of 1.0. The precision and recall non-financialsectors.
scoresfurtherhighlightthemodel’scapabilitytodetectspam
whileminimizingfalsepositives.Theseresultsreinforcethe
REFERENCES
effectivenessoftheproposedmodelacrossdifferentdatasets.
TheconsistentperformanceacrossvariousK-Foldvalidation [1] A.K.Mishra,A.Pandey,andS.Anand.(Oct.2019).AReviewonCredit
|     |     |     |     |     |     | Card | Fraud Detection |     | Using Machine |     | Learning. | [Online]. Available: |
| --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | ------------- | --- | --------- | -------------------- |
splitsconfirmsitsrobustnessandadaptabilitytodifferentdata https://www.researchgate.net/publication/336552027_A_Review_On
conditions. _Credit_Card_Fraud_Detection_Using_Machine_Learning
|     |     |     |     |     |     | [2] BitEffect. | Payment | Systems: | Principle |     | of Operation | and Opportuni- |
| --- | --- | --- | --- | --- | --- | -------------- | ------- | -------- | --------- | --- | ------------ | -------------- |
TABLE11. ComparisonofK-foldcross-validationandexistingworks. ties.[Online].Available:https://biteffect.net/payment-systems-principle-
of-operation-and-opportunities/
[3] SDKFinance.DetectingPaymentCardFraudwithMachineLearning—
H2ODriverlessAIKaggleDataset.Accessed:Dec.14,2024.[Online].
|     |     |     |     |     |     | Available: |     | https://sdk.finance/detecting-payment-card-fraud-with- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------------------------------------------ | --- | --- | --- | --- |
machine-learning-h2o-driverless-ai-kaggle-dataset/
[4] MerchantSavvy.(2023).PaymentFraudStatistics2023:Trends,Data,and
Insights.[Online].Available:https://www.merchantsavvy.co.uk/payment-
fraud-statistics/
[5] H.Zou,‘‘Analysisofbestsamplingstrategyincreditcardfrauddetection
|     |     |     |     |     |     | using     | machine | learning,’’ | in   | Proc. 6th       | Int. Conf. | Intell. Inf. Tech-   |
| --- | --- | --- | --- | --- | --- | --------- | ------- | ----------- | ---- | --------------- | ---------- | -------------------- |
|     |     |     |     |     |     | nol., New | York,   | NY, USA,    | Feb. | 2021, pp.40–44. |            | [Online]. Available: |
https://dl.acm.org/doi/fullHtml/10.1145/3460179.3460186
|     |     |     |     |     |     | [6] Mitek | Systems. | How    | Does      | Machine  | Learning | Help With Fraud      |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | --------- | -------- | -------- | -------------------- |
|     |     |     |     |     |     | Detection | in       | Banks. | Accessed: | Dec. 23, | 2024.    | [Online]. Available: |
https://www.miteksystems.com/blog/how-does-machine-learning-help-
with-fraud-detection-in-banks/
V. FUTUREWORK
[7] A.Arya.(7,2024).FraudDetectionUsingMachineLearningAlgorithms.
| Despite | the good drift | detection | capabilities | on  | various |     |     |     |     |     |     |     |
| ------- | -------------- | --------- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
[Online].Available:https://intellipaat.com/blog/fraud-detection-machine-
| datasets | of the current | framework, | it still | does not | support |     |     |     |     |     |     |     |
| -------- | -------------- | ---------- | -------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
learning-algorithms/?U.S.#::text=Manual%20Review%20and%20
Transaction%20Rules,-Nowadays%2C%20Machine%20Learning&amp;
| direct real-time | learning | based | on changing | fraud | patterns. |     |     |     |     |     |     |     |
| ---------------- | -------- | ----- | ----------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
text=Previously%2C%20industries%20were%20using%20a,detection
| To solve | this challenge, | the adaptive |     | learning model | was |     |     |     |     |     |     |     |
| -------- | --------------- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
%20to%20ML%2Dbased%20solutions
developed in Phase 3, including the online learning mecha- [8] D. Kumar. Top 4 Advantages and Disadvantages of Support Vector
nismwiththeSGDandadynamicensemblewithLightGBM. Machine (SVM). Accessed: Dec. 23, 2024. [Online]. Available: https://
dhirajkumarblog.medium.com/top-4-advantages-and-disadvantages-of-
| This improvement | allows | the model | to  | adapt to | new trans- |     |     |     |     |     |     |     |
| ---------------- | ------ | --------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
support-vector-machine-or-SVM-a3c06a2b107
actional data incrementally without having to retrain over [9] A. Soni. Advantages and Disadvantages of KNN. Medium. Accessed:
the whole dataset, which is crucial when deployed in high- Dec. 28, 2024. [Online]. Available: https://medium.com/anuuz.soni/
advantages-and-disadvantages-of-knn-ee06599b9336
frequency,concept-driftingapplicationslikefrauddetection.
|     |     |     |     |     |     | [10] S. Wandre, | S.  | Desai, | A. Patel, | and H. | Lopes, | ‘‘Credit card fraud |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | --------- | ------ | ------ | ------------------- |
Inthefuture,itisplannedtoinvestigateenhancementsforthis
|     |     |     |     |     |     | detection | using | KNN | and naive | Bayes | algorithm,’’ | J. Emerg. Tech- |
| --- | --- | --- | --- | --- | --- | --------- | ----- | --- | --------- | ----- | ------------ | --------------- |
architectureusingprivacy-preservingmethods(i.e.,federated nol. Innov. Res., vol. 9, no. 4, pp.327–332, 2022. [Online]. Available:
https://www.jetir.org/papers/JETIR2204420.pdf
learning)toenablejointdetectionoffraudacrossinstitutions
|     |     |     |     |     |     | [11] T. A. | Yusof. | Adaptive | Model | for Credit | Card | Fraud Detection. |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | -------- | ----- | ---------- | ---- | ---------------- |
andprotectsensitivedata.Further,lightweightmodelarchi-
Accessed:Dec.23,2024.[Online].Available:https://www.researchgate.
tectureswillalsobeexploredtominimizecomputationaland
net/publication/339585842_Adaptive_Model_for_Credit_Card_Fraud_
| communicationoverheadtoimprovetheresponsivenessand |     |     |     |     |     | Detection      |     |       |           |         |         |                    |
| -------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --------- | ------- | ------- | ------------------ |
|                                                    |     |     |     |     |     | [12] Z. Bawany | and | A. D. | Shanbhag, | ‘‘Using | machine | learning to detect |
scalabilityofthesysteminreal-timeapplications.
|                |     |     |     |     |     | credit                             | card fraud,’’ | in   | Proc. Int.  | Conf.   | Electr., Comput. | Energy Tech-       |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- | ------------- | ---- | ----------- | ------- | ---------------- | ------------------ |
|                |     |     |     |     |     | nol. (ICECET),                     |               | Cape | Town, South | Africa, | Nov.             | 2023, pp.1–7, doi: |
| VI. CONCLUSION |     |     |     |     |     | 10.1109/icecet58911.2023.10389421. |               |      |             |         |                  |                    |
The present study presented an organized framework for [13] A. Taha and S. J. Malebary, ‘‘An intelligent approach to credit
|     |     |     |     |     |     | card | fraud detection |     | using an | optimized | light | gradient boosting |
| --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | -------- | --------- | ----- | ----------------- |
drift detection and fraud identification, with performance machine,’’ IEEE Access, vol. 8, pp. 25579–25587, Feb. 2020, doi:
evaluated via several datasets: Credit Card, Spam, and Real 10.1109/ACCESS.2020.2971354.
datasets. In summary, the incorporation of Mutual Infor- [14] BINUS. (2022). The Importance of Data Preprocessing for Machine
|             |             |         |            |        |     | Learning | in E-Commerce. |     | [Online]. | Available: |     | https://sis.binus.ac.id/ |
| ----------- | ----------- | ------- | ---------- | ------ | --- | -------- | -------------- | --- | --------- | ---------- | --- | ------------------------ |
| mation with | SelectKBest | feature | selection, | ADASYN | for |          |                |     |           |            |     |                          |
2022/07/11/the-importance-of-data-preprocessing-for-machine-learning-
data balance, and advanced drift detection via EDDM and in-the-e-commerce-industry/#:text=In%20this%20case%2C%20data%20
preprocessing,
ADWINprovidesarobustandflexiblemethodfordynamic
incorrect%20output%20from%20the%20AI
dataenvironments.Theproposedframeworkachieved100%
|          |            |       |           |         |          | [15] R. A. | Mohammed, | K.-W. | Wong, | M. F. | Shiratuddin, | and X. Wang, |
| -------- | ---------- | ----- | --------- | ------- | -------- | ---------- | --------- | ----- | ----- | ----- | ------------ | ------------ |
| accuracy | and a 100% | drift | detection | rate on | the Real |            |           |       |       |       |              |              |
‘‘Scalablemachinelearningtechniquesforhighlyimbalancedcreditcard
dataset, demonstrating significant sensitivity and specificity fraud detection: A comparative study,’’ in Proc. Trends Artif. Intell.,
Lect.NotesComput.Sci.(PRICAI),vol.11013,Jan.2018,pp.237–246.
| for real-world | fraud detection |     | in both | numeric and | mixed- |     |     |     |     |     |     |     |
| -------------- | --------------- | --- | ------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
[Online].Available:https://link.springer.com/chapter/10.1007/978-3-319-
| data contexts. | This approach |     | is obvious, | comprehensible, |     | 97310-4_27 |     |     |     |     |     |               |
| -------------- | ------------- | --- | ----------- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | ------------- |
| 92054          |               |     |             |                 |     |            |     |     |     |     |     | VOLUME13,2025 |

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
[16] D. Singh, S. Vardhan, and N. Agrawal, ‘‘Credit card fraud detection [35] Card Payments. Accessed: Nov. 4, 2024. [Online]. Available:
analysis,’’ Int. Res. J. Eng. Technol., vol. 5, no. 11, pp. 1600–1603, https://www.psr.org.uk/our-work/card-payments/
Nov.2018. [36] S.C.EmeraldandT.Vengattaraman,‘‘Conceptdriftdetectionwithopti-
[17] T.Chioka.TheClassImbalanceProbleminMachineLearning.Chioka’s mal machine learning model for data classification,’’ in Proc. 6th Int.
Blog. Accessed: Dec. 20, 2024. [Online]. Available: http://www. Conf.TrendsElectron.Informat.(ICOEI),Apr.2022,pp.1160–1165,doi:
chioka.in/class-imbalance-problem/#: :text=What%20is%20the%20 10.1109/ICOEI53556.2022.9776949.
Class%20Imbalance,class%20of%20data%20(negative) [37] S. Jain. Guide To EMV—Contact & Contactless Payment. Accessed:
[18] R. Verma. Class Imbalance: A Classification Headache. Towards Data Dec. 20, 2024. [Online]. Available: https://sruti-jain.github.io/
Science. Accessed: Dec. 20, 2024. [Online]. Available: https://towards img/GuidetoEMV-Contact-ContactlessPayments.pdf
datascience.com/class-imbalance-a-classification-headache- [38] What is a Card-not-present (CNP) Transaction and Why It Costs
1939297ff4a4 More. Accessed: Dec. 31, 2024. [Online]. Available: https://squareup.
[19] M.S.Kraiem,F.Sánchez-Hernández,andM.N.Moreno-García,‘‘Select- com/us/en/townsquare/what-is-a-card-not-present-transaction
ing the suitable resampling strategy for imbalanced data classification [39] B. Dwyer. What’s the Difference Between Card Present and Card Not
regardingdatasetproperties.Anapproachbasedonassociationmodels,’’ Present?.CardFellowCreditCardProcessingBlog.Accessed:Dec.31,
Appl.Sci.,vol.11,no.18,p.8546,Sep.2021,doi:10.3390/app11188546. 2024.[Online].Available:https://www.cardfellow.com/blog/card-present-
[20] A.Smith,B.Johnson,andC.Williams,‘‘Conceptdriftandfalsealarm card-not-present-definition/
ratesincreditcardfrauddetection,’’J.FraudDetect.Prevent.,vol.15, [40] A.Patel.(13,2021).Beginner’sGuideToClassificationModels:Catch
no.3,pp.178–187,2021. Credit Card Fraud. Codex. [Online]. Available: https://medium.com/
[21] Understanding Model Drift in Machine Learning. [Online]. Available: codex/beginners-guide-to-classification-models-catch-credit-card-fraud-
https://www.projectpro.io/article/model-drift-in-machine-learning/871 fe5a73a3401f
[22] A. D. Pozzolo, G. Boracchi, O. Caelen, C. Alippi, and G. Bontempi, [41] Cardinity. Payment Flow. Accessed: Dec. 31, 2024. [Online].
‘‘Credit card fraud detection: A realistic modeling and a novel Available:https://cardinity.com/support/payment-flow
learning strategy,’’ IEEE Trans. Neural Netw. Learn. Syst., [42] D.Mulimani,P.R.Patil,andS.G.Totad,‘‘Adaptiveclassifiertoaddress
vol. 29, no. 8, pp.3784–3797, Aug. 2017. [Online]. Available: conceptdriftinimbalanceddatastreams,’’inProc.IEEE2ndInt.Conf.
https://re.public.polimi.it/bitstream/11311/1044896/1/08038008.pdf Data,Decis.Syst.(ICDDS),Mangaluru,India,Dec.2023,pp.1–5,doi:
[23] A.BifetandR.Gavalda,‘‘Learningfromtime-changingdatawithadap- 10.1109/icdds59137.2023.10434793.
tive windowing,’’ in Proc. SIAM Int. Conf. Data Mining, Jul. 2007, [43] Kajal and K. Kaur, ‘‘Credit card fraud detection using imbalance
pp.443–448. resampling method with feature selection,’’ Int. J. Adv. Trends Com-
[24] R. Shakya, ‘‘Application of machine learning techniques in credit put. Sci. Eng., vol. 10, no. 3, pp.2061–2071, May 2021, doi:
card fraud detection,’’ M.S. thesis, Dept. Comput. Sci., Howard 10.30534/ijatcse/2021/811032021.
R. Hughes College Eng., Univ. Nevada, Las Vegas, NV, USA, 2018. [44] S. Saraf and A. Phakatkar, ‘‘Detection of credit card fraud using a
[Online]. Available: https://digitalscholarship.unlv.edu/cgi/viewcontent. hybridensemblemodel,’’Int.J.Adv.Comput.Sci.Appl.,vol.13,no.9,
cgi?article=4457&context=thesesdissertations pp. 464–474, 2022. [Online]. Available: https://thesai.org/Downloads/
[25] S.PriyaandR.A.Uthra,‘‘Deeplearningframeworkforhandlingconcept Volume13No9/Paper_53-Detection_of_Credit_Card_Fraud.pdf
driftandclassimbalancedcomplexdecision-makingonstreamingdata,’’ [45] UCIMach.Learn.Repository.(1999).SpambaseDataset.[Online].Avail-
ComplexIntell.Syst.,vol.8,pp.41–53,2021,doi:10.1007/s40747-021- able:https://archive.ics.uci.edu/dataset/94/spambase
00456-0. [46] S. Saraf and A. Phakatkar, ‘‘Detection of credit card fraud using a
[26] E.M.H.A.Rubaie,‘‘Improvementincreditcardfrauddetectionusing hybridensemblemodel,’’Int.J.Adv.Comput.Sci.Appl.,vol.13,no.9,
ensembleclassificationtechnique,’’Int.J.NonlinearAnal.Appl.,vol.12, pp.464–474,2022.
no. 2, pp. 1255–1265, Jun. 2021, doi: 10.22075/IJNAA.2021.5228. [47] B.Lebichot,G.MarcoPaldino,G.Bontempi,W.Siblini,L.He-Guelton,
[Online]. Available: https://ijnaa.semnan.ac.ir/article_5228_bffa45b11 andF.Oblé,‘‘Incrementallearningstrategiesforcreditcardsfrauddetec-
da19bafd8e8431ce1de1e05.pdf tion: Extended abstract,’’ in Proc. IEEE 7th Int. Conf. Data Sci. Adv.
[27] O. Shmatko, V. Fedorchenko, and D. Prochukhan, ‘‘Detecting Analytics(DSAA),Sydney,NSW,Australia,Oct.2020,pp.785–786,doi:
credit card fraud using machine learning algorithms,’’ InterConf, 10.1109/DSAA49011.2020.00116.
vol. 71, pp.393–403, Aug. 2021. [Online]. Available: https://www. [48] M.K.H.Chy,‘‘Proactivefrauddefense:Machinelearning’sevolvingrole
researchgate.net/publication/354112967_DETECTING_CREDIT_ inprotectingagainstonlinefraud,’’WorldJ.Adv.Res.Rev.,vol.23,no.3,
CARD_FRAUD_USING_MACHINE_LEARNING_ALGORITHMS pp.1580–1589,Sep.2024,doi:10.30574/wjarr.2024.23.3.2811.
[28] S. Agrahari and A. K. Singh, ‘‘Concept drift detection in data [49] A.Hachcham.(Jan.27,2025).TheKNNAlgorithm—Explanation,Oppor-
stream mining: A literature review,’’ J. King Saud Univ.-Comput. Inf. tunities, Limitations. [Online]. Available: https://neptune.ai/blog/knn-
Sci., vol. 34, no. 10, pp.9523–9540, Nov. 2022. [Online]. Available: algorithm
https://www.sciencedirect.com/science/article/pii/S1319157821003062 [50] Kaggle.(2016).CreditCardFraudDetectionDataset.[Online].Available:
[29] C.BrownandL.White,‘‘Theimpactofconceptdriftonfrauddetection https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
performance,’’inProc.ACMInt.Conf.Knowl.DiscoveryDataMining, [51] P. Tomar, S. Shrivastava, and U. Thakar, ‘‘Ensemble learning based
Jun.2017,pp.256–268. credit card fraud detection system,’’ in Proc. 5th Conf. Inf. Com-
[30] S. Lee, J. Kim, and M. Park, ‘‘Adaptive fraud detection using con- mun. Technol. (CICT), Kurnool, India, Dec. 2021, pp.1–5, doi:
ceptdriftadaptationm,’’IEEETrans.Knowl.DataEng.,vol.28,no.9, 10.1109/CICT53865.2020.9672426.
pp.2453–2467,Sep.2018.
[31] K. Kajal and K. Kaur, ‘‘Credit card fraud detection using imbalance
resampling method with feature selection,’’ Int. J. Adv. Trends Com-
put.Sci.Eng.,vol.10,no.3,pp.1693–1699,2021.[Online].Available:
https://www.warse.org/IJATCSE/static/pdf/file/ijatcse801032021.pdf
[32] S.Mungase,A.Tikande,S.Bora,P.Zanwar,andA.Pathan,‘‘Creditcard
frauddetectionusingmachinelearningframework,’’Int.J.Innov.Res.Sci.,
Eng.Technol.,vol.7,no.6,pp.355–360,Jun.2020.[Online].Available:
HADI M. R. AL LAWATI received the B.Sc.
https://www.ijirset.com/upload/2020/september/104_Tejas_NC.PDF
degree in computer science from Gulf College,
[33] E. Ileberi, Y. Sun, and Z. Wang, ‘‘A machine learning based credit
Muscat, Oman, in 2009, and the M.Sc. degree
card fraud detection using the GA algorithm for feature selection,’’
in computer science from Staffordshire Univer-
J. Big Data, vol. 9, no. 1, pp.1–18, Feb. 2022. [Online]. Available:
sity,Staffordshire,U.K.,in2011.Heiscurrently
https://www.academia.edu/76673761/A_machine_learning_based_credit
_card_fraud_detection_using_the_GA_algorithm_for_feature_selection pursuingthePh.D.degreeincomputingwithUni-
[34] R. Powar, R. Dawkhar, and P. Pratichi, ‘‘Credit card fraud versitiTeknologiMalaysia(UTM),JohorBahru,
detection using machine learning,’’ Int. J. Adv. Sci. Res. Eng. Malaysia, with a focus on adaptive learning for
Trends, vol. 5, no. 9, pp.62–67, Sep. 2020. [Online]. Available: frauddetectioninpaymentsystems.Heisalsoa
http://ijasret.com/VolumeArticles/FullTextPDF/546_9.CREDIT_CARD_ SeniorSpecialistinITcardtechnologywiththe
FRAUD_DETECTION_USING_MACHINE__LEARNING.pdf SoharInternationalBank,Muscat.
VOLUME13,2025 92055

H.M.R.AlLawatietal.:IntegratedPreprocessingandDriftDetectionApproach
ANAZIDAZAINALreceivedthePh.D.degreein MOHAMAD NIZAM KASSIM received the
computersciencefromtheFacultyofComputing, Ph.D. degree in computer science from Uni-
UniversitiTeknologiMalaysia(UTM),Malaysia. versiti Teknologi Malaysia (UTM). He is cur-
SheiscurrentlyanAssociateProfessorwiththe rently the Deputy Director with the Strategic
Faculty of Computing, UTM. She is also affili- ResearchDivision,NationalAnti-FinancialCrime
atedwiththeAnti-FinancialCrimeLaboratoryand Center (NFCC), Malaysia. He is also with the
theInformationAssuranceandSecurityResearch Anti-FinancialCrimeLaboratory,UTM.
Group(IASRG),UTM.
BANDER ALI SALEH AL-RIMY (Senior
Member, IEEE) received the Ph.D. degree
from Universiti Teknologi Malaysia (UTM), SULTAN AHMED ALMALKI receivedtheB.Sc.
in 2019. He was a Senior Lecturer with UTM, degreeininformationsystemsfromKingAbdu-
from 2021 to 2024, and UNITAR International lazizUniversity,SaudiArabia,theM.Sc.degree
University, in 2020, and a Lecturer at Coventry incomputersciencefromSaintXavierUniversity,
University,from2021to2022,whereheledthe USA,andthePh.D.degreeincomputerscience
ethicalhackingandcybersecurity.Heiscurrently fromtheUniversityofIdaho,USA.Heiscurrently
aSeniorLecturerincybersecuritywiththeUniver- anAssistantProfessorwiththeComputerDepart-
sityofPortsmouth,inJuly2024.Hehas12years ment,AppliedCollege,NajranUniversity,Saudi
of industrial experience in ICT (roles in network infrastructure, security Arabia.Hisresearchinterestsinclude,butarenot
engineering,andITconsulting). limitedto,malwareanalysis,dataanalysis,intru-
siondetectionsystems(IDS),artificialintelligence,andmachinelearning.
MOHAMMAD AL-AZAWI received the Ph.D.
degreeinartificialintelligencefromDeMontfort
University,UnitedKingdom.Heiscurrentlythe
DeputyDeanforAcademicAffairs,Research,and TAMI ABDULRAHMAN ALGHAMDI received
InnovationatGulfCollege,Oman,andservesasan the bachelor’s and master’s in computer science
AssociateProfessorinArtificialIntelligenceand from Western Illinois University, and the Ph.D.
ComputerVision.Withover20yearsofacademic degree in computer science from the University
experience, he has led initiatives in curriculum of Idaho, in 2022. Currently, he is an Assis-
development, academic governance, and quality tant Professor at the College of Computing and
assurance. His research interests include ethical Information,Al-BahaUniversity,AlBaha,Saudi
AI,machinelearning,AIapplicationsinmedicaldiagnostics,andhuman Arabia.Hisresearchinterestsaremachinelearn-
attentionmodelling.HeisalsoactiveinpromotingAI-driveneducational ing,transferlearning,geneticalgorithms,anddata
transformationandparticipatesinregionalandinternationalcollaborations science.
focusedonAIdevelopment,research,andinnovation.
92056 VOLUME13,2025