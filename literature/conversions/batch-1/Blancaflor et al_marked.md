---
conversion_metadata:
  converted_at: "2026-07-22T12:22:51Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Blancaflor et al.pdf"
  source_pdf_sha256: "70bac67faa15f478aac5ccc2f26079b3aaf0348a5d1bddc9e9aa09c265350e72"
  page_count: 6
  markdown_char_count: 68612
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Exploring Machine Learning for Credit Card Fraud Detection
from a Philippine Perspective

Eric Blancaflor
School of IT, Mapua University
Philippines
ebblancaflor@mapua.edu.ph

Hailie Jade Reyes
School of IT, Mapua University
Philippines
hjsreyes@mymail.mapua.edu.ph

Keziah Dawn Asuncion
School of IT, Mapua University
Philippines
kdrasuncion@mymail.mapua.edu.ph

Michaela Verzosa
School of IT, Mapua University
Philippines
mpverzosa@mymail.mapua.edu.ph

Abstract
This study examines how machine learning (ML) techniques are
applied in the Philippine setting to identify credit card fraud. This
research aims to provide insights into the effectiveness of ML tech-
niques in fraud detection, focusing on customizing ML algorithms
to the distinct patterns and dynamics of credit card fraud in the
Philippines, considering the nation’s unique economic, technologi-
cal, and social milieu. The research assesses the efficacy of different
machine learning (ML) models using available data on credit card
fraud occurrences and suggests improving fraud detection systems
in Philippine financial institutions through ML integration. It also
examines the opportunities and difficulties of using ML-driven
fraud detection techniques in the Philippine financial industry.

CCS Concepts
• Security and privacy; • Human and societal aspects of secu-
rity and privacy; • Privacy protections;

Keywords
Credit Card, Fraud Detection, Machine Learning, Philippines, Sup-
port Vector Machines, Artificial Neural Network, Prevention, De-
tection

ACM Reference Format:
Eric Blancaflor, Keziah Dawn Asuncion, Hailie Jade Reyes, and Michaela
Verzosa. 2024. Exploring Machine Learning for Credit Card Fraud Detection
from a Philippine Perspective. In 2024 The 6th World Symposium on Software
Engineering (WSSE) (WSSE 2024), September 13–15, 2024, Kyoto, Japan. ACM,
New York, NY, USA, 6 pages. https://doi.org/10.1145/3698062.3698088

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
WSSE 2024, September 13–15, 2024, Kyoto, Japan
© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-1708-6/24/09
https://doi.org/10.1145/3698062.3698088

1 Introduction
1.1 Background of the Study
Parallel to the phenomenal growth of digital transactions and on-
line commerce, credit card fraud in the Philippines has risen to
incredible heights. Together with increasingly sophisticated forms
of fraudulent activities come growing requirements for equally
innovative solutions that can cut these crimes down. In line with
this, this research will investigate whether machine learning could
be a powerful tool in enhancing credit card fraud detection within
the Philippine financial sector. It is an artificial intelligence domain
that imparted computers with the ability to learn from data with-
out explicit programming, hence a good solution for identifying
fraudulent patterns and anomalies in credit card transactions. Fo-
cusing on customizing the ML algorithms for the peculiarities of
the Philippine context—economic, technological, and social—this
paper, research will try to enhance the effectiveness of fraud de-
tection systems. The literature review will go into the background
of credit card fraud in this modern digital world, the scope and
purpose of the research, the methodology, key findings and dis-
cussions, and finally, implications and future research directions.
Credit card fraud instances are increasing at a rapid rate in the
Philippines, which goes in direct relation to the rapid growth of
its digital economy [1]. This threat increases with the limited ef-
fectiveness of traditional fraud detection. Herein lies the relevance
of this review. By providing way to the possibilities of ML for the
Philippine setting, this study hopes to add to the existing discussion
regarding the strengthening of financial institutions from fraud in
developing economies. Furthermore, lessons learned in tailing ML
models for the distinctly Philippine environment will also serve
other developing countries that face similar challenges.

1.2 Objective of the Study
This paper identifies the escalating threat of credit card fraud in
the Philippines and explores its parallelism with the proliferation
of computer-based transactions in the country and simultaneously
with the inadequacy of traditional fraud detection methods.
It
points out the main research question of whether it would be pos-
sible to fine-tune machine learning algorithms to the Philippine
context for more effective fraud detection. This section reviews the
background of the study on credit card fraud, its scope and purpose,
methodology used, findings, and discussions. The paper seeks to

---

<!-- PAGE 2 -->

WSSE 2024, September 13–15, 2024, Kyoto, Japan

Eric Blancaflor et al.

prepare a better ground for an all-rounded argument about ML’s
potential in fighting credit card fraud in the Philippine financial
sector.

2 LITERATURE REVIEW
With the sudden surge of digital payment platforms, fraudulent
credit card transactions in the Philippines have risen by 21% since
the outbreak of COVID-19. Many of the fraud prevention sys-
tems do not consider the security of e-commerce networks and the
fraud detection systems face issues like enormous quantities of data,
skewed distribution, concept drift, and real-time detection assis-
tance. Although at the cost of explainability, the accuracy achieved
by Machine learning models, empowered with superior pattern
detection and scalability, make them the future of Fraud detection.
Future research shall investigate the impacts of additional sample
techniques meta-classifiers and meta-learning methodologies to
deal with highly imbalanced credit card fraud data.

2.1 Fraud Issues on Credit Card Usage
According to Philstar [2], MANILA, Philippines — Fraudulent credit
card operations in the Philippines through remote and other digital
payment channels increased by 21% since the start of the pandemic,
according to the Credit Card Association of the Philippines. ”The
industry has suffered financially due to an increase in fraud cases
brought on by the increasing acceptance of different digital pay-
ment platforms,” Ilagan stated. According to ABS-CBN News [3],
The Bangko Sentral ng Pilipinas said on Monday that online fraud
cost consumers more than P540 million in 2021 alone. It also ap-
pealed to lawmakers to pass a bill that protects financial customers.
BSP said there were 42,456 complaints from fraud victims of online
monetary transactions between 2020 and 2021 involving phishing,
identity theft, and malware attacks, among other forms of deceit.
Most of these have already been considered closed. In addition,
Diokno enlightened the senators that a lot of complaints had reso-
lutions that did not benefit the consumer. To this extent, doubtless,
the increase in digital transactions has made consumers’ lives easier
and faster, but this trend has also opened up room for new types of
financial fraud. According to the CCAP, there has been a phenome-
nal surge in fraud-related activities, in particular through digital
and remote payment channels [4]. Apart from being a threat to the
consumers, the rise of these fraudulent cases is costing the sector
financially.

Responding to this escalating threat, the BSP has started to ad-
dress all of these concerns. With damages estimated at P540 million
last year, cybercrime highlights the necessity of better policies for
securing clients [3]. The law was legislated in response to the
BSP’s appeal to Congress to pass this type of law [5]. It provides
for the rights of financial consumers for fair treatment and timely
settlement of their complaints.

It is currently investigating claims of customers of Philippine
bank BDO that they lost money to internet scammers who used
accounts at Union Bank of the Philippines. It reported having mon-
itored the increased complaints in the past week and subsequently
frozen several accounts. The Philippines Anti-Money Launder-
ing Council announced that the country had stepped up its fight
against money laundering and terror financing in November 2021

[6]. Former RCBC branch manager Maia Deguito was in January
2019 convicted on eight counts of money laundering in the $81
million theft from the Central Bank of Bangladesh. The bank was
fined PHP 1 billion ($19.17 million) in August 2016 for its failure to
prevent the flow of stolen funds through it [6].

Maria Nite, president of Bank Capital Development Corp., was
behind a notorious Treasury bill scam in which she bilked banks
and investors by selling the Treasury bills repeatedly to trick people
into believing they were all of the same T-bill. She made off with
P2.5 billion ($200 million) and was arrested by FBI agents in 1997,
and extradited to the Philippines [6]. The FrancSwiss & Deutsch-
ers scam brought losses of PHP 1 billion, while that of the 12DP
scam was $500 million. Legacy insurance and pension scam caused
losses of PHP 30 billion, or $591 million. Aman Futures Group
conned more than 15,000 investors in Mindanao and Visayas into a
pyramid scheme where an investment return of 80% in just 20 days
was promised for commodities trading. Connected to Legal Funds
Transfer was the case of Annabella C. Ylagan, convicted in April
2018 of 55 counts of money laundering [6].

Between 2020 and 2021, card fraud losses globally increased by
more than 10 percent. This is the highest rise since 2018. It is
estimated that 30 billion dollars were lost by merchants and card
acquirers; of those, losses of about 12 billion were from merchants
and card acquirers in the United States alone, as reported. Please
note that the figures shown here include both credit card fraud
and debit card fraud. They are not distinguished on the website,
and neither is there any statistic on the US, which is yet another
country known for its addiction to credit cards [7].

From $28.4 billion in 2020 and $27.9 billion in 2018, a total of $33.5
billion was reported lost due to card theft globally in 2022. In the
EU, card transactions of € 1.53 billion were reported as fraudulent
in 2021, representing a 7% decline in fraudulent card transactions
overall. 93% of fraudulent charges in 2024 included credit cards
issued in the United States that were still in the owners’ possession.
Card-not-present is the fraud type affecting $174 million in lost
revenue in 2023. In 2023, customers did report 368,379 cases of
fraud related to online purchasing for a cost of $392 million. 94% of
all card-present transactions globally were made using cards with
EMV chips as of the second quarter of 2023, compared to 92% at
the same time in 2022 [8].

Despite such efforts, these are prima facie reasons to believe that
more needs to be done to educate and create awareness among
customers concerning the dangers associated with the use of e-
financial services. Several resolved cases without victims receiving
adequate compensation is a pointer to the need for more effective
enforcement and consumer education campaigns. It puts customers
on notice to be vigilant and at all times keep constant checks on
their accounts and report suspicious activities to their banks or
appropriate authorities. To have the capacity for a safe and reliable
digital ecosystem, the collaboration of all concerned stakeholders—
from financial institutions to regulators and consumers—should be
assurance-based once digital finance makes its way to the country.
Other than individual customer protection, a collaborative fight
against fraud would further cement the integrity of the Philippine
financial system.

---

<!-- PAGE 3 -->

Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective

WSSE 2024, September 13–15, 2024, Kyoto, Japan

2.2 Fraud Detection Studies on Machine

Learning

Fraudsters frequently target e-commerce systems and use a range
of underhanded tactics to get through. Using Fraud Prevention
Systems alone is not sufficient for securing the network. Two pos-
sible combinations of FPSs and FDSs are sharing their capacities in
securing e-commerce systems. However, the following factors usu-
ally make FDSs weak. Some of these are concept drift, the need for
real-time detection, and imbalanced distribution, coupled with han-
dling vast volumes of data. Furthermore, three specific limitations
prevent FDSs from becoming highly efficient: the problems asso-
ciated with the misclassification costs, noisy data, and overlapped
classes. These constraints drive the models constructed improperly
and to become too complicated detection models - affecting the pre-
dicted accuracy adversely. To address these problems, the following
fraud detection tools are more commonly relied on. These tools are
logistic regression, rule-induction techniques, decision trees, artifi-
cial neural networks, support vector machines, and meta-heuristic
such as evolutionary algorithms. According to Abdallah et al. in
2016, the instruments are applied to most of the fraud detection
industries [9]. Techniques provide a feasible means to improve the
effectiveness of the FDSs in securing e-commerce platforms.

• The matthews correlation coefficient (mcc) is a metric to
assess how well binary classifications are done. It is well
recognized as a balanced measure that can be applied even
in cases where the classes have drastically different sizes
because it accounts for both true and false positives and
negatives1. This formula is used to calculate the mcc: MCC
= (TP × TN) - (FP × FN) /
((TP + FP)(TP + FN)(TN + FP)(TN
+ FN)) : where tp is true positives, tn is true negatives, fp is
false positives, and fn is false negatives[10].

√

• Balanced classification rate (bcr): bcr is the average of the
recall scores for each class. It is sometimes referred to as
the average recall or the balanced accuracy. It helps handle
datasets that are unbalanced3. It comes out to be: BCR =
2Sensitivity + Specificity. The genuine positive rate is called
sensitivity, and the true negative rate is called specificity[11].
• A statistical model used in machine learning for binary clas-
sification issues is called logistic regression. Logistic re-
gression forecasts an event’s probability, which is a number
between 0 and 1, as opposed to linear regression, which
predicts a continuous outcome [12].

• K-nearest neighbor: k-nn is a supervised, non-parametric
learning classifier that classifies or predicts how to catego-
rize a single data point based on its proximity to other data
points67. When given a test observation and a positive inte-
ger k, k-nn finds the k nearest points and can conclude these
closest targets [13].

• Using the bayes theorem as its foundation, naïve bayes is a
probabilistic machine learning technique that may be used
for various classification tasks. It is referred to as ”naive”
because it assumes that each characteristic in the model is
independent of the others [14].

Although the tradeoff between explainability and accuracy exists,
with improved pattern detection and scalability, machine learning
models remain the way forward for fraud detection. This wave of

machine learning-driven focus shift from pre-transaction to post-
transaction detection portrays success in this war against fraud
and creates a much safer digital transaction environment [15]. In
this experiment, the three methods will be applied to both prepro-
cessed and raw data. The implementation of the work will be done
in Python. Their performance will then be evaluated using the
approaches based on their accuracy, sensitivity, specificity, preci-
sion, Matthews Correlation Coefficient, and balanced classification
rate. Descriptive statistics of models applied for logistic regression
and k-nearest neighbor classifiers have their best accuracy rates
at 54.86% and 97.69%, respectively, while that of naïve Bayes is
at 97.92%. Comparative results show that the K-nearest neighbor
outperforms the logistic regression and naïve Bayes methods. The
research gives the effect of hybrid sampling on the binary classi-
fication of imbalanced data. Expected future areas of studies on
meta-classifiers and meta-learning strategies for the handling of
highly imbalanced credit card fraud data and, the effects of other
re-sampling techniques could also be explored [16].

2.3 Focus on Fraud Prevention and Detection
Concerning the magnitude of the problem of credit card fraud in the
Philippines, the strategic approach has been about strengthening
fraud prevention and detection systems. It is through a combination
of multifactor authentication, encryption, and real-time monitor-
ing that FPSs become better equipped to detect, at an incredibly
fast pace, any suspicious action. Advanced analytics, along with
machine learning algorithms like Artificial Neural Networks (ANN)
and Support Vector Machines (SVM), strengthens fraud detection
capabilities within a Fraud Detection System (FDSs). These algo-
rithms learn to recognize fraudulent patterns and anomalies in
transaction data. Support Vector Machine is one of the popular
methods that is used to recognize patterns and classify problems,
especially when binary categorization like classifying fraudulent
and nonfraudulent patterns is involved.

Like all other AI techniques, an SVM needs to be trained to return
a model capable of predicting. Domains of application include but
are not limited to the following: text categorization, bioinformatics,
and face detection. SVM borrows from non-parametric applied
statistics, neural networks, and the basics of machine learning. Its
decision function, based on the theory of Structural Risk Minimiza-
tion, will define a boundary between classes in the case of binary
classification. This function also plays a very important role in
determining the separation margin between classes, wherein it is
learned by parameters w and b during the training phase by maxi-
mizing the margin [17]. Here is the sample of the SVM Equation:
𝑓 (𝑥) = 𝑠𝑞𝑛(𝑥 .𝑤) + 𝑏

To scale these systems up to the next level, there is an urgent
need to perform periodic upgrades of security protocols and algo-
rithms to stay ahead of the tactics of fraudsters in vogue each day
[18]. Big data technology can provide the competence of these sys-
tems to effectively deal with voluminous data on transactions, thus
identifying fraud activities with better accuracy in real-time. This
is because good collaboration within the bodies of banks, payment
processors, and regulatory authorities is especially crucial in shar-
ing vital information and trends on fraud. By doing so, it becomes
possible to foster universally accepted standards and solutions that

---

<!-- PAGE 4 -->

WSSE 2024, September 13–15, 2024, Kyoto, Japan

Eric Blancaflor et al.

this may be as important as explaining the rationale behind de-
cisions as accuracy. Therefore, in the case of credit card fraud, it
would be wiser to rely more on models like ANN-SMOTE to en-
hance the possibilities of detection. However, including LR models
is beneficial in meeting compliance and transparency requirements.
Therefore, a middle path can be adopted so that the discoverability
and prevention of fraud are more potent, and at the same time, the
developed processes remain compliant with the set regulations.

2.5 Using Machine Learning to Avoid Credit

Card Fraud

The case of credit card fraud detection in the Philippines stays
timely due to the steep rise in fraudulent transactions by 21% since
the pandemic [2]. Traditional FPSs do not suffice to protect digital
payment networks; thus, there is a need for modern technologies
like ML. The discussion points out the seriousness of the issue of
fraud and the need for proactive actions based on insights from
reliable sources—the Credit Card Association of the Philippines and
the Bangko Sentral ng Pilipinas. Very promising results in enhanc-
ing fraud detection skills, despite inherent model explainability–
accuracy trade-offs, have been seen lately with machine learning
models, especially support vector machines and artificial neural
networks. The discussion needs further research in more creative
methods such as meta-classifiers or meta-learning strategies to
solve the problems arising from fraudulent credit card use in the
Philippines. It also calls for stakeholder engagement in advanced
analytics to set the foundation for a collective defense against fraud-
sters on digital payment networks. The discussion is very much
in keeping with the research aims to investigate machine learning
in credit card fraud detection in the Philippines and provides very
valuable insights and ideas for future research in this field.

In addition, the implementation of machine learning algorithms
into fraud detection systems increases the accuracy of the identi-
fication of fraudulent actions, providing real-time detection with
the capability of adaptive learning [22]. Machine learning mod-
els adapt to newly developed fraud techniques by continuously
analysing transaction data and patterns. This adaptive ability is
quite important in fighting more complex fraud techniques, given
the fast-moving nature of digital transactions. Furthermore, fraud
prevention requires collaboration between different stakeholders,
including financial institutions, regulatory authorities, and technol-
ogy providers. Only through shared insights, best practices, and
collaboration can stakeholders be better placed to improve fraud
prevention measures within digital payment networks and reduce
vulnerabilities. Advanced analytics also showcases a greater inter-
est in the use of data-driven techniques to unearth quite hidden
trends and anomalies that serve as leading indicators of fraudu-
lent activities, and therefore secure and preserve the integrity of
financial transactions in the Philippines.

The researchers have taken a detailed drive through various ma-
chine learning models in service for credit card fraud detection.
This section will mainly focus on how well these models perform
in terms of accuracy—one of the major factors in determining how
efficient each model is at the detection of fraudulent transactions.
Further, some strategic ideas that are aimed at enhancing the fore-
cast accuracy and total efficiency of such models are sought. The

Figure 1: Comparative Performance of Machine Learning
Models in Credit Card Fraud Detection

effectively mitigate any vulnerabilities across all the platforms.
Training employees in financial institutions on the knowledge of
current fraud detection technologies and techniques helps maintain
an effective level of alertness and competence. Equally important
are consumer education programs that can boost knowledge of
security procedures and the importance of protecting personal in-
formation. Lastly, the development of machine learning adaptive
models into applications able easily to acquire information on new
fraudulent actions and, in the process, alter their algorithm will in
the long term ensure very effective fraud detection systems [19].

2.4 Approach to Address Credit Card Fraud
Identification of complex challenges in mitigating credit card fraud—
that this entails false alert cases and needs to be in real-time—is
important. To overcome such challenges, developing and putting in
place robust solutions will be relevant. These include real-time mon-
itoring options that facilitate immediate identification of suspicious
trends and reactions to the same. Furthermore, the improvement
of rules in fraud prevention itself increases accuracy and makes
the measures more responsive. These preventive steps can then
be implemented to safeguard the business from fraud, fortify the
protection of its financial assets, and uphold customer trust [20].
Figure 1 compares the performance of two Machine Learning
models: Artificial Neural Network (ANN) and Logistic Regression
(LR), with Genetic Algorithm (GA) and the Synthetic Minority Over-
sampling Technique (SMOTE)-based enhancements to each model
[21]. These enhancements are added to each model to make the
model more accurate and robust to skewness—a relevant factor
when dealing with fraud detection. It has the best performance
compared to other models on all aspects of accuracy, precision,
recall, and F1 score. This will mean it can detect fraud more impres-
sively and with few misclassifications. This means that probably,
ANN-SMOTE could probably be highly efficient, for example, in
credit card fraud detection, where illegal transactions are very few
as compared to legal ones. On the other hand, even if the LR
models—both LR-GA and LR-SMOTE—exhibit relatively poor per-
formance considering these metrics, they can turn out to be useful
in applications for which the interpretability of the decisions made
by a model is paramount. In particular, in regulatory compliance,

---

<!-- PAGE 5 -->

Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective

WSSE 2024, September 13–15, 2024, Kyoto, Japan

Table 1: Evaluating Machine Learning Models for Credit Card Fraud Detection: Accuracy and Improvement Strategies

Model

Dataset Description

Method

Accuracy

What to Improve

Reference

Logistic
Regression
K-Nearest
Neighbors
(k-NN)
Naïve Bayes

Support Vector
Machines (SVM)

Artificial Neural
Networks (ANN)

Credit card transaction data
from the Philippines
Data points clustered based
on proximity to detect fraud

Supervised binary
classification
Non-parametric,
nearest neighbor

Transaction patterns focusing
on anomaly detection
Features intended to
distinguish between authentic
and fraudulent transactions
High-dimensional datasets for
pattern recognition

Probabilistic
classification
Kernel-based
learning technique

Deep learning
algorithms

54.86%

97.69%

97.92%

Varies up to
80%

Varies up to
98.44%

Explore hybrid sampling to
handle imbalanced data
Increase the diversity and
size of the dataset for better
generalization
Adjust independence
assumptions in the model
Incorporate meta-learning
for skewed data handling

Optimize neural network
architecture for real-time
detection

[23]

[24]

[25]

[26]

[27]

authors have clearly shown that, for instance, some of their models
address imbalanced datasets or improving algorithm parameters
as the critical areas to enhance, and therefore this gives a clear
avenue for future research on its practical application in fraud de-
tection. This thorough assessment improves our understanding of
the current capabilities and limitations of existing machine learning
models and further drives innovation in methods to secure financial
security systems against the threats of fraudulent activities.

3 CONCLUSION
In conclusion, the digital payment systems that have been invented
have proved to be a potential source of unintended consequences
for increased fraudulent activities, especially in the Philippines,
which, since the epidemic, has seen an increase in credit card fraud
by 21%. Current FPSS are proving to be utterly inadequate in their
security for e-commerce networks, while various challenges, such
as managing huge amounts of data, skewed distribution, concept
drift, and the demand for real-time detection, plague FDSS. How-
ever, the introduction of machine learning models puts the future
of fraud detection on the bright side. The application of models
that can learn from data without explicit programming for improv-
ing security in e-commerce platforms is increasingly used. In this
way, an advanced war against fraud forms a safer environment for
digital transactions with a transition from pre-transaction to post-
transaction detection. This study, therefore, is much needed in the
Philippines, which is classified as one of the countries with a large
volume of fraudulent credit card transactions. In essence, what this
means is that there should be an enhanced FDSS with advanced
analytics, machine learning algorithms, and techniques for anomaly
detection while strengthening the FPSS by multifactor authentica-
tion, encryption protocols, and real-time monitoring. This would
involve collaboration concerning insight, best practices, and threat
information sharing among financial institutions, regulatory bod-
ies, and technology providers. The research goes further to outline
how machine learning will benefit fraud detection in the financial
sector. Tailoring machine learning algorithms to the intricacies of
the Philippine context—the unique economic, technological, and
social aspects—is what can greatly increase the efficacy of fraud

detection systems. Results from this study may help related issues
dealing with other developing countries.

References
[1] Kris Crismundo. 2021. Digital fraud attempts in PH rise amid pandemic | Philip-
pine News . Philippine News Agency. Retrieved from https://www.pna.gov.ph/
articles/1134735

[2] Lawrence Agcaoili. 2022. Credit card issuers report 21% jump in fraud cases |
Philstar.com. Philstar. Retrieved from https://www.philstar.com/business/2022/
08/17/2203090/credit-card-issuers-report-21-jump-fraud-cases

[3] Sherrie Ann Torres. 2022. BSP says online fraud cost P540 million in 2021 | ABS-
CBN News. Retrieved from https://news.abs-cbn.com/business/01/17/22/bsp-says-
online-fraud-cost-p540-million-in-2021

[4] Doris Dumlao-Abadilla, D. 2021. Credit card fraud cases surge 29%. IN-
QUIRER.net. Retrieved from https://business.inquirer.net/316906/credit-card-
fraud-cases-surge-29

[5] Republic Act No. 11765. 2022. Lawphil.net. Retrieved from https://lawphil.net/

statutes/repacts/ra2022/ra_11765_2022.html

[6] Jay Hilton. 2021. Philippines: Short list of top financial scams, central bank
cracks the whip on fraud, money laundering. gulfnews.com. Retrieved from https:
//gulfnews.com/business/philippines-short-list-of-top-financial-scams-central-
bank-cracks-the-whip-on-fraud-money-laundering-1.1639325591494?slide$=$1
[7] Raynor de Best. 2024. Card fraud value worldwide. Statista. Retrieved from

https://www.statista.com/statistics/1394119/global-card-fraud-losses/.

[8] Maria Webb. 2024. Credit card fraud statistics. Techopedia. Retrieved from https:

//www.techopedia.com/credit-card-fraud-statistics.

[9] Aisha Abdallah, Mohd Aizaini Maarof, and Anazida Zainal. 2016. Fraud detection
system: A survey | Journal of Network and Computer Applications, 68, 90–113.
Retrieved from https://doi.org/10.1016/j.jnca.2016.04.007

[10] Li Sisters. 2024. Matthew’s

it and when to avoid it. Medium. Retrieved May 8,
https://towardsdatascience.com/matthews-correlation-coefficient-when-
to-use-it-and-when-to-avoid-it-310b3c923f7e.

correlation coefficient: When to use
from

2024,

[11] Zach Bobbitt. 2021. What is balanced accuracy? (Definition & Example). Statology.
Retrieved May 8, 2024, from https://www.statology.org/balanced-accuracy.
[12] IBM. What is supply chain management? Retrieved from https://www.ibm.com/

topics/logistic-regression.

[13] IBM. What is the k-nearest neighbors algorithm? Retrieved from https://www.

ibm.com/topics/knn.

[14] Selva Prabhakaran. 2018. How naive bayes algorithm works?

(with ex-
ample and full code). Machine Learning Plus. Retrieved May 8, 2024,
from https://www.machinelearningplus.com/predictive-modeling/how-naive-
bayes-algorithm-works-with-example-and-full-code.

[15] Dor Bank. 2023. The game-changing role of machine learning in credit card
fraud detection | Justt. Retrieved from https://justt.ai/blog/tech/machine-learning-
credit-card-fraud-detection

[16] 6John O. Awoyemi, Adebayo O. Adetunmbi, and Samuel A. Oluwadare. 2017.
Credit card fraud detection using machine learning techniques: A comparative
analysis. In Proceedings of the 2017 International Conference on Computing
Networking and Informatics (ICCNI), 1–9. Retrieved from https://doi.org/10.1109/
iccni.2017.8123782.

---

<!-- PAGE 6 -->

WSSE 2024, September 13–15, 2024, Kyoto, Japan

Eric Blancaflor et al.

[17] V. Dheepa and R. Dhanapal 2012. Behavior based credit card fraud detection
using support vector machines. ICTACT Journal on Soft Computing, 2(4), 391–397.
Retrieved from https://doi.org/10.21917/ijsc.2012.0061.

[18] Philip Olaseni Shoetan, Adedoyin Tolulope Oyewole, Chinwe Chinazo Okoye,
and Onyeka Chrisanctus Ofodile. 2024. Reviewing the role of big data analytics in
financial fraud detection. Finance & Accounting Research Journal, 6(3), 384–394.
Retrieved from https://doi.org/10.51594/farj.v6i3.899

[19] Waleed Hilal, S. Andrew Gadsden, John Yawney. 2021. A review of anomaly
detection techniques and applications in financial fraud. Expert Systems with
Applications, 193(1), 116429. Retrieved from https://doi.org/10.1016/j.eswa.2021.
116429

[20] Kayode Ayorinde. 2021. A methodology for detecting credit card fraud. Cor-
nerstone: A Collection of Scholarly and Creative Works for Minnesota.
Retrieved from https://cornerstone.lib.mnsu.edu/cgi/viewcontent.cgi?article$=
$2167&context$=$etds.

[21] Shailendra Aswale, Nikita Shirodkar, Rohit Shet Mandrekar, Rahul Sakhalkar,
and K.M. Chaman Kumar. 2020. Credit card fraud detection techniques. Retrieved
May 04, 2024, from https://www.researchgate.net/publication/351686482_Credit_
Card_Fraud_Detection_Techniques/citations

[22] Ashish K Saxena and Aidar Vafin. 2019. Machine learning and big data analytics
for fraud detection systems in the United States fintech industry. Emerging
Trends in Machine Intelligence and Big Data, 11(12), 1–11. Retrieved from https:

//orientreview.com/index.php/etmibd-journal/article/view/46/50

[23] John O. Awoyemi, Adebayo O. Adetunmbi, and Samuel A. Oluwadare. 2017. Credit
card fraud detection using machine learning techniques: A comparative analy-
sis. 2017 International Conference on Computing Networking and Informatics
(ICCNI), pp. 1–9. Retrieved from https://doi.org/10.1109/iccni.2017.8123782.
[24] Kavita Arora, Sonal Pathak, and Nguyen T. D. Linh. 2023. Comparative analysis
of K-NN, Naïve Bayes, and logistic regression for credit card fraud detection.
Ingeniería Solidaria, 19(3), 1–22. Retrieved from https://doi.org/10.16925/2357-
6014.2023.03.05.

[25] T. Vairam, S. Sarathambekai, S. Bhavadharani, A. K. Dharshini, N. N. Sri, and
Tarika Sen. 2022. Evaluation of naïve bayes and voting classifier algorithm for
credit card fraud detection. 2022 8th International Conference on Advanced
Computing and Communication Systems (ICACCS). Retrieved from https://doi.
org/10.1109/icaccs54159.2022.9784968.

[26] Nana Kwame Gyamfi and Jamal-Deen Abdulai. 2018. Bank fraud detection using
support vector machine. Retrieved from https://doi.org/10.1109/iemcon.2018.
8614994.

[27] F. Yeşilyurt, H. Temurtaş, and Ç. Bakır. 2023. Detection of credit card fraud
with artificial neural networks. Proceedings of the International Conference on
Advanced Technologies. Retrieved from https://doi.org/10.58190/icat.2023.15.
.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| Exploring |                              | Machine        | Learning     | for Credit     | Card                            | Fraud Detection |     |
| --------- | ---------------------------- | -------------- | ------------ | -------------- | ------------------------------- | --------------- | --- |
|           |                              | from           | a Philippine | Perspective    |                                 |                 |     |
|           |                              | EricBlancaflor |              |                | KeziahDawnAsuncion              |                 |     |
|           | SchoolofIT,MapuaUniversity   |                |              |                | SchoolofIT,MapuaUniversity      |                 |     |
|           |                              | Philippines    |              |                | Philippines                     |                 |     |
|           | ebblancaflor@mapua.edu.ph    |                |              |                | kdrasuncion@mymail.mapua.edu.ph |                 |     |
|           | HailieJadeReyes              |                |              |                | MichaelaVerzosa                 |                 |     |
|           | SchoolofIT,MapuaUniversity   |                |              |                | SchoolofIT,MapuaUniversity      |                 |     |
|           |                              | Philippines    |              |                | Philippines                     |                 |     |
|           | hjsreyes@mymail.mapua.edu.ph |                |              |                | mpverzosa@mymail.mapua.edu.ph   |                 |     |
| Abstract  |                              |                |              | 1 Introduction |                                 |                 |     |
Thisstudyexamineshowmachinelearning(ML)techniquesare 1.1 BackgroundoftheStudy
appliedinthePhilippinesettingtoidentifycreditcardfraud.This
Paralleltothephenomenalgrowthofdigitaltransactionsandon-
researchaimstoprovideinsightsintotheeffectivenessofMLtech- linecommerce,creditcardfraudinthePhilippineshasrisento
niquesinfrauddetection,focusingoncustomizingMLalgorithms
|     |     |     |     | incredibleheights. | Togetherwithincreasinglysophisticatedforms |     |     |
| --- | --- | --- | --- | ------------------ | ------------------------------------------ | --- | --- |
tothedistinctpatternsanddynamicsofcreditcardfraudinthe
|     |     |     |     | of fraudulent | activities come | growing requirements | for equally |
| --- | --- | --- | --- | ------------- | --------------- | -------------------- | ----------- |
Philippines,consideringthenation’suniqueeconomic,technologi-
innovativesolutionsthatcancutthesecrimesdown.Inlinewith
cal,andsocialmilieu.Theresearchassessestheefficacyofdifferent
this,thisresearchwillinvestigatewhethermachinelearningcould
machinelearning(ML)modelsusingavailabledataoncreditcard beapowerfultoolinenhancingcreditcardfrauddetectionwithin
fraudoccurrencesandsuggestsimprovingfrauddetectionsystems
thePhilippinefinancialsector.Itisanartificialintelligencedomain
inPhilippinefinancialinstitutionsthroughMLintegration.Italso
thatimpartedcomputerswiththeabilitytolearnfromdatawith-
| examines | the opportunities | and difficulties | of using ML-driven |     |     |     |     |
| -------- | ----------------- | ---------------- | ------------------ | --- | --- | --- | --- |
outexplicitprogramming,henceagoodsolutionforidentifying
frauddetectiontechniquesinthePhilippinefinancialindustry.
fraudulentpatternsandanomaliesincreditcardtransactions.Fo-
cusingoncustomizingtheMLalgorithmsforthepeculiaritiesof
CCSConcepts
thePhilippinecontext—economic,technological,andsocial—this
•Securityandprivacy;•Humanandsocietalaspectsofsecu- paper,researchwilltrytoenhancetheeffectivenessoffraudde-
|     |     |     |     | tectionsystems. | Theliteraturereviewwillgointothebackground |     |     |
| --- | --- | --- | --- | --------------- | ------------------------------------------ | --- | --- |
rityandprivacy;•Privacyprotections;
ofcreditcardfraudinthismoderndigitalworld,thescopeand
purposeoftheresearch,themethodology,keyfindingsanddis-
Keywords
cussions,andfinally,implicationsandfutureresearchdirections.
CreditCard,FraudDetection,MachineLearning,Philippines,Sup- Creditcardfraudinstancesareincreasingatarapidrateinthe
portVectorMachines,ArtificialNeuralNetwork,Prevention,De- Philippines,whichgoesindirectrelationtotherapidgrowthof
tection itsdigitaleconomy[1]. Thisthreatincreaseswiththelimitedef-
fectivenessoftraditionalfrauddetection.Hereinliestherelevance
ACMReferenceFormat: ofthisreview. ByprovidingwaytothepossibilitiesofMLforthe
EricBlancaflor,KeziahDawnAsuncion,HailieJadeReyes,andMichaela Philippinesetting,thisstudyhopestoaddtotheexistingdiscussion
Verzosa.2024.ExploringMachineLearningforCreditCardFraudDetection regardingthestrengtheningoffinancialinstitutionsfromfraudin
fromaPhilippinePerspective.In2024The6thWorldSymposiumonSoftware developingeconomies. Furthermore,lessonslearnedintailingML
Engineering(WSSE)(WSSE2024),September13–15,2024,Kyoto,Japan.ACM, modelsforthedistinctlyPhilippineenvironmentwillalsoserve
NewYork,NY,USA,6pages.https://doi.org/10.1145/3698062.3698088 otherdevelopingcountriesthatfacesimilarchallenges.
|     |     |     |     | 1.2 ObjectiveoftheStudy |     |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --- | --- |
Thispaperidentifiestheescalatingthreatofcreditcardfraudin
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
thePhilippinesandexploresitsparallelismwiththeproliferation
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation ofcomputer-basedtransactionsinthecountryandsimultaneously
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe with the inadequacy of traditional fraud detection methods. It
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or pointsoutthemainresearchquestionofwhetheritwouldbepos-
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. sibletofine-tunemachinelearningalgorithmstothePhilippine
WSSE2024,September13–15,2024,Kyoto,Japan
contextformoreeffectivefrauddetection.Thissectionreviewsthe
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
backgroundofthestudyoncreditcardfraud,itsscopeandpurpose,
ACMISBN979-8-4007-1708-6/24/09
https://doi.org/10.1145/3698062.3698088 methodologyused,findings,anddiscussions. Thepaperseeksto
177

WSSE2024,September13–15,2024,Kyoto,Japan EricBlancafloretal.
prepareabettergroundforanall-roundedargumentaboutML’s [6].FormerRCBCbranchmanagerMaiaDeguitowasinJanuary
potentialinfightingcreditcardfraudinthePhilippinefinancial 2019convictedoneightcountsofmoneylaunderinginthe$81
sector. milliontheftfromtheCentralBankofBangladesh. Thebankwas
finedPHP1billion($19.17million)inAugust2016foritsfailureto
2 LITERATUREREVIEW preventtheflowofstolenfundsthroughit[6].
MariaNite,presidentofBankCapitalDevelopmentCorp.,was
Withthesuddensurgeofdigitalpaymentplatforms,fraudulent
behindanotoriousTreasurybillscaminwhichshebilkedbanks
creditcardtransactionsinthePhilippineshaverisenby21%since
andinvestorsbysellingtheTreasurybillsrepeatedlytotrickpeople
the outbreak of COVID-19. Many of the fraud prevention sys-
intobelievingtheywereallofthesameT-bill.Shemadeoffwith
temsdonotconsiderthesecurityofe-commercenetworksandthe
P2.5billion($200million)andwasarrestedbyFBIagentsin1997,
frauddetectionsystemsfaceissueslikeenormousquantitiesofdata,
andextraditedtothePhilippines[6]. TheFrancSwiss&Deutsch-
skeweddistribution,conceptdrift,andreal-timedetectionassis-
ersscambroughtlossesofPHP1billion,whilethatofthe12DP
tance.Althoughatthecostofexplainability,theaccuracyachieved
scamwas$500million.Legacyinsuranceandpensionscamcaused
byMachinelearningmodels, empoweredwithsuperiorpattern
lossesofPHP30billion, or$591million. AmanFuturesGroup
detectionandscalability,makethemthefutureofFrauddetection.
connedmorethan15,000investorsinMindanaoandVisayasintoa
Futureresearchshallinvestigatetheimpactsofadditionalsample
pyramidschemewhereaninvestmentreturnof80%injust20days
techniquesmeta-classifiersandmeta-learningmethodologiesto
waspromisedforcommoditiestrading.ConnectedtoLegalFunds
dealwithhighlyimbalancedcreditcardfrauddata.
TransferwasthecaseofAnnabellaC.Ylagan,convictedinApril
2018of55countsofmoneylaundering[6].
2.1 FraudIssuesonCreditCardUsage
Between2020and2021,cardfraudlossesgloballyincreasedby
AccordingtoPhilstar[2],MANILA,Philippines—Fraudulentcredit more than 10 percent. This is the highest rise since 2018. It is
cardoperationsinthePhilippinesthroughremoteandotherdigital estimatedthat30billiondollarswerelostbymerchantsandcard
paymentchannelsincreasedby21%sincethestartofthepandemic, acquirers;ofthose,lossesofabout12billionwerefrommerchants
accordingtotheCreditCardAssociationofthePhilippines.”The andcardacquirersintheUnitedStatesalone,asreported.Please
industryhassufferedfinanciallyduetoanincreaseinfraudcases notethatthefiguresshownhereincludebothcreditcardfraud
broughtonbytheincreasingacceptanceofdifferentdigitalpay- anddebitcardfraud. Theyarenotdistinguishedonthewebsite,
mentplatforms,”Ilaganstated.AccordingtoABS-CBNNews[3], andneitheristhereanystatisticontheUS,whichisyetanother
TheBangkoSentralngPilipinassaidonMondaythatonlinefraud countryknownforitsaddictiontocreditcards[7].
costconsumersmorethanP540millionin2021alone. Italsoap- From$28.4billionin2020and$27.9billionin2018,atotalof$33.5
pealedtolawmakerstopassabillthatprotectsfinancialcustomers. billionwasreportedlostduetocardtheftgloballyin2022.Inthe
BSPsaidtherewere42,456complaintsfromfraudvictimsofonline EU,cardtransactionsof€1.53billionwerereportedasfraudulent
monetarytransactionsbetween2020and2021involvingphishing, in2021,representinga7%declineinfraudulentcardtransactions
identitytheft,andmalwareattacks,amongotherformsofdeceit. overall. 93%offraudulentchargesin2024includedcreditcards
Mostofthesehavealreadybeenconsideredclosed. Inaddition, issuedintheUnitedStatesthatwerestillintheowners’possession.
Dioknoenlightenedthesenatorsthatalotofcomplaintshadreso- Card-not-presentisthefraudtypeaffecting$174millioninlost
lutionsthatdidnotbenefittheconsumer. Tothisextent,doubtless, revenuein2023. In2023,customersdidreport368,379casesof
theincreaseindigitaltransactionshasmadeconsumers’liveseasier fraudrelatedtoonlinepurchasingforacostof$392million.94%of
andfaster,butthistrendhasalsoopeneduproomfornewtypesof allcard-presenttransactionsgloballyweremadeusingcardswith
financialfraud.AccordingtotheCCAP,therehasbeenaphenome- EMVchipsasofthesecondquarterof2023,comparedto92%at
nalsurgeinfraud-relatedactivities,inparticularthroughdigital thesametimein2022[8].
andremotepaymentchannels[4].Apartfrombeingathreattothe Despitesuchefforts,theseareprimafaciereasonstobelievethat
consumers,theriseofthesefraudulentcasesiscostingthesector moreneedstobedonetoeducateandcreateawarenessamong
financially. customersconcerningthedangersassociatedwiththeuseofe-
Respondingtothisescalatingthreat,theBSPhasstartedtoad- financialservices.Severalresolvedcaseswithoutvictimsreceiving
dressalloftheseconcerns.WithdamagesestimatedatP540million adequatecompensationisapointertotheneedformoreeffective
lastyear,cybercrimehighlightsthenecessityofbetterpoliciesfor enforcementandconsumereducationcampaigns.Itputscustomers
securing clients [3]. The law was legislated in response to the onnoticetobevigilantandatalltimeskeepconstantcheckson
BSP’sappealtoCongresstopassthistypeoflaw[5].Itprovides theiraccountsandreportsuspiciousactivitiestotheirbanksor
fortherightsoffinancialconsumersforfairtreatmentandtimely appropriateauthorities.Tohavethecapacityforasafeandreliable
settlementoftheircomplaints. digitalecosystem,thecollaborationofallconcernedstakeholders—
ItiscurrentlyinvestigatingclaimsofcustomersofPhilippine fromfinancialinstitutionstoregulatorsandconsumers—shouldbe
bankBDOthattheylostmoneytointernetscammerswhoused assurance-basedoncedigitalfinancemakesitswaytothecountry.
accountsatUnionBankofthePhilippines.Itreportedhavingmon- Otherthanindividualcustomerprotection,acollaborativefight
itoredtheincreasedcomplaintsinthepastweekandsubsequently againstfraudwouldfurthercementtheintegrityofthePhilippine
frozen several accounts. The Philippines Anti-Money Launder- financialsystem.
ingCouncilannouncedthatthecountryhadsteppedupitsfight
againstmoneylaunderingandterrorfinancinginNovember2021
178

ExploringMachineLearningforCreditCardFraudDetectionfromaPhilippinePerspective WSSE2024,September13–15,2024,Kyoto,Japan
2.2 FraudDetectionStudiesonMachine machinelearning-drivenfocusshiftfrompre-transactiontopost-
Learning transactiondetectionportrayssuccessinthiswaragainstfraud
andcreatesamuchsaferdigitaltransactionenvironment[15]. In
Fraudstersfrequentlytargete-commercesystemsandusearange
thisexperiment,thethreemethodswillbeappliedtobothprepro-
ofunderhandedtacticstogetthrough. UsingFraudPrevention
cessedandrawdata.Theimplementationoftheworkwillbedone
Systemsaloneisnotsufficientforsecuringthenetwork.Twopos-
inPython. Theirperformancewillthenbeevaluatedusingthe
siblecombinationsofFPSsandFDSsaresharingtheircapacitiesin
approachesbasedontheiraccuracy,sensitivity,specificity,preci-
securinge-commercesystems.However,thefollowingfactorsusu-
sion,MatthewsCorrelationCoefficient,andbalancedclassification
allymakeFDSsweak.Someoftheseareconceptdrift,theneedfor
rate.Descriptivestatisticsofmodelsappliedforlogisticregression
real-timedetection,andimbalanceddistribution,coupledwithhan-
andk-nearestneighborclassifiershavetheirbestaccuracyrates
dlingvastvolumesofdata.Furthermore,threespecificlimitations
at54.86%and97.69%, respectively, whilethatofnaïveBayesis
preventFDSsfrombecominghighlyefficient: theproblemsasso-
at97.92%.ComparativeresultsshowthattheK-nearestneighbor
ciatedwiththemisclassificationcosts,noisydata,andoverlapped
outperformsthelogisticregressionandnaïveBayesmethods.The
classes.Theseconstraintsdrivethemodelsconstructedimproperly
researchgivestheeffectofhybridsamplingonthebinaryclassi-
andtobecometoocomplicateddetectionmodels-affectingthepre-
ficationofimbalanceddata. Expectedfutureareasofstudieson
dictedaccuracyadversely.Toaddresstheseproblems,thefollowing
meta-classifiersandmeta-learningstrategiesforthehandlingof
frauddetectiontoolsaremorecommonlyreliedon.Thesetoolsare
highlyimbalancedcreditcardfrauddataand,theeffectsofother
logisticregression,rule-inductiontechniques,decisiontrees,artifi-
re-samplingtechniquescouldalsobeexplored[16].
cialneuralnetworks,supportvectormachines,andmeta-heuristic
suchasevolutionaryalgorithms. AccordingtoAbdallahetal. in
2016,theinstrumentsareappliedtomostofthefrauddetection 2.3 FocusonFraudPreventionandDetection
industries[9].Techniquesprovideafeasiblemeanstoimprovethe
Concerningthemagnitudeoftheproblemofcreditcardfraudinthe
effectivenessoftheFDSsinsecuringe-commerceplatforms.
Philippines,thestrategicapproachhasbeenaboutstrengthening
• The matthews correlationcoefficient (mcc) is a metric to
fraudpreventionanddetectionsystems.Itisthroughacombination
assesshowwellbinaryclassificationsaredone. Itiswell
ofmultifactorauthentication,encryption,andreal-timemonitor-
recognizedasabalancedmeasurethatcanbeappliedeven
ingthatFPSsbecomebetterequippedtodetect,atanincredibly
incaseswheretheclasseshavedrasticallydifferentsizes
fastpace,anysuspiciousaction. Advancedanalytics,alongwith
because it accounts for both true and false positives and
machinelearningalgorithmslikeArtificialNeuralNetworks(ANN)
negatives1.Thisformulaisusedtocalculatethemcc:MCC
√ andSupportVectorMachines(SVM),strengthensfrauddetection
=(TP×TN)-(FP×FN)/ ((TP+FP)(TP+FN)(TN+FP)(TN
capabilitieswithinaFraudDetectionSystem(FDSs). Thesealgo-
+FN)):wheretpistruepositives,tnistruenegatives,fpis
rithms learn to recognize fraudulent patterns and anomalies in
falsepositives,andfnisfalsenegatives[10].
transactiondata. SupportVectorMachineisoneofthepopular
• Balancedclassificationrate(bcr): bcristheaverageofthe
methodsthatisusedtorecognizepatternsandclassifyproblems,
recallscoresforeachclass. Itissometimesreferredtoas
especiallywhenbinarycategorizationlikeclassifyingfraudulent
theaveragerecallorthebalancedaccuracy.Ithelpshandle
andnonfraudulentpatternsisinvolved.
datasetsthatareunbalanced3. Itcomesouttobe: BCR=
LikeallotherAItechniques,anSVMneedstobetrainedtoreturn
2Sensitivity+Specificity.Thegenuinepositiverateiscalled
amodelcapableofpredicting.Domainsofapplicationincludebut
sensitivity,andthetruenegativerateiscalledspecificity[11].
arenotlimitedtothefollowing:textcategorization,bioinformatics,
• Astatisticalmodelusedinmachinelearningforbinaryclas-
andfacedetection. SVMborrowsfromnon-parametricapplied
sification issues is called logistic regression. Logistic re-
statistics,neuralnetworks,andthebasicsofmachinelearning.Its
gressionforecastsanevent’sprobability,whichisanumber
decisionfunction,basedonthetheoryofStructuralRiskMinimiza-
between 0 and 1, as opposed to linear regression, which
tion,willdefineaboundarybetweenclassesinthecaseofbinary
predictsacontinuousoutcome[12].
classification. Thisfunctionalsoplaysaveryimportantrolein
• K-nearestneighbor: k-nnisasupervised,non-parametric
determiningtheseparationmarginbetweenclasses,whereinitis
learningclassifierthatclassifiesorpredictshowtocatego-
learnedbyparameterswandbduringthetrainingphasebymaxi-
rizeasingledatapointbasedonitsproximitytootherdata
mizingthemargin[17].HereisthesampleoftheSVMEquation:
points67.Whengivenatestobservationandapositiveinte- 𝑓(𝑥)=𝑠𝑞𝑛(𝑥.𝑤)+𝑏
gerk,k-nnfindstheknearestpointsandcanconcludethese
Toscalethesesystemsuptothenextlevel,thereisanurgent
closesttargets[13].
needtoperformperiodicupgradesofsecurityprotocolsandalgo-
• Usingthebayestheoremasitsfoundation,naïvebayesisa
rithmstostayaheadofthetacticsoffraudstersinvogueeachday
probabilisticmachinelearningtechniquethatmaybeused
[18].Bigdatatechnologycanprovidethecompetenceofthesesys-
forvariousclassificationtasks. Itisreferredtoas”naive”
temstoeffectivelydealwithvoluminousdataontransactions,thus
becauseitassumesthateachcharacteristicinthemodelis
identifyingfraudactivitieswithbetteraccuracyinreal-time. This
independentoftheothers[14].
isbecausegoodcollaborationwithinthebodiesofbanks,payment
Althoughthetradeoffbetweenexplainabilityandaccuracyexists, processors,andregulatoryauthoritiesisespeciallycrucialinshar-
withimprovedpatterndetectionandscalability,machinelearning ingvitalinformationandtrendsonfraud. Bydoingso,itbecomes
modelsremainthewayforwardforfrauddetection. Thiswaveof possibletofosteruniversallyacceptedstandardsandsolutionsthat
179

WSSE2024,September13–15,2024,Kyoto,Japan EricBlancafloretal.
thismaybeasimportantasexplainingtherationalebehindde-
cisionsasaccuracy. Therefore,inthecaseofcreditcardfraud,it
wouldbewisertorelymoreonmodelslikeANN-SMOTEtoen-
hancethepossibilitiesofdetection.However,includingLRmodels
isbeneficialinmeetingcomplianceandtransparencyrequirements.
Therefore,amiddlepathcanbeadoptedsothatthediscoverability
andpreventionoffraudaremorepotent,andatthesametime,the
developedprocessesremaincompliantwiththesetregulations.
2.5 UsingMachineLearningtoAvoidCredit
CardFraud
The case of credit card fraud detection in the Philippines stays
Figure1: ComparativePerformanceofMachineLearning timelyduetothesteepriseinfraudulenttransactionsby21%since
ModelsinCreditCardFraudDetection thepandemic[2].TraditionalFPSsdonotsufficetoprotectdigital
paymentnetworks;thus,thereisaneedformoderntechnologies
likeML.Thediscussionpointsouttheseriousnessoftheissueof
fraudandtheneedforproactiveactionsbasedoninsightsfrom
effectively mitigate any vulnerabilities across all the platforms.
reliablesources—theCreditCardAssociationofthePhilippinesand
Trainingemployeesinfinancialinstitutionsontheknowledgeof
theBangkoSentralngPilipinas.Verypromisingresultsinenhanc-
currentfrauddetectiontechnologiesandtechniqueshelpsmaintain
ingfrauddetectionskills,despiteinherentmodelexplainability–
aneffectivelevelofalertnessandcompetence.Equallyimportant
accuracytrade-offs,havebeenseenlatelywithmachinelearning
areconsumereducationprogramsthatcanboostknowledgeof
models,especiallysupportvectormachinesandartificialneural
securityproceduresandtheimportanceofprotectingpersonalin-
networks.Thediscussionneedsfurtherresearchinmorecreative
formation.Lastly,thedevelopmentofmachinelearningadaptive
methods such as meta-classifiers or meta-learning strategies to
modelsintoapplicationsableeasilytoacquireinformationonnew
solvetheproblemsarisingfromfraudulentcreditcarduseinthe
fraudulentactionsand,intheprocess,altertheiralgorithmwillin
Philippines.Italsocallsforstakeholderengagementinadvanced
thelongtermensureveryeffectivefrauddetectionsystems[19].
analyticstosetthefoundationforacollectivedefenseagainstfraud-
stersondigitalpaymentnetworks. Thediscussionisverymuch
2.4 ApproachtoAddressCreditCardFraud
inkeepingwiththeresearchaimstoinvestigatemachinelearning
Identificationofcomplexchallengesinmitigatingcreditcardfraud— increditcardfrauddetectioninthePhilippinesandprovidesvery
thatthisentailsfalsealertcasesandneedstobeinreal-time—is valuableinsightsandideasforfutureresearchinthisfield.
important.Toovercomesuchchallenges,developingandputtingin Inaddition,theimplementationofmachinelearningalgorithms
placerobustsolutionswillberelevant.Theseincludereal-timemon- intofrauddetectionsystemsincreasestheaccuracyoftheidenti-
itoringoptionsthatfacilitateimmediateidentificationofsuspicious ficationoffraudulentactions,providingreal-timedetectionwith
trendsandreactionstothesame.Furthermore,theimprovement thecapabilityofadaptivelearning[22]. Machinelearningmod-
ofrulesinfraudpreventionitselfincreasesaccuracyandmakes elsadapttonewlydevelopedfraudtechniquesbycontinuously
themeasuresmoreresponsive. Thesepreventivestepscanthen analysingtransactiondataandpatterns. Thisadaptiveabilityis
beimplementedtosafeguardthebusinessfromfraud,fortifythe quiteimportantinfightingmorecomplexfraudtechniques,given
protectionofitsfinancialassets,andupholdcustomertrust[20]. thefast-movingnatureofdigitaltransactions.Furthermore,fraud
Figure1comparestheperformanceoftwoMachineLearning preventionrequirescollaborationbetweendifferentstakeholders,
models:ArtificialNeuralNetwork(ANN)andLogisticRegression includingfinancialinstitutions,regulatoryauthorities,andtechnol-
(LR),withGeneticAlgorithm(GA)andtheSyntheticMinorityOver- ogyproviders. Onlythroughsharedinsights,bestpractices,and
samplingTechnique(SMOTE)-basedenhancementstoeachmodel collaborationcanstakeholdersbebetterplacedtoimprovefraud
[21]. Theseenhancementsareaddedtoeachmodeltomakethe preventionmeasureswithindigitalpaymentnetworksandreduce
modelmoreaccurateandrobusttoskewness—arelevantfactor vulnerabilities.Advancedanalyticsalsoshowcasesagreaterinter-
whendealingwithfrauddetection. Ithasthebestperformance estintheuseofdata-driventechniquestounearthquitehidden
comparedtoothermodelsonallaspectsofaccuracy, precision, trendsandanomaliesthatserveasleadingindicatorsoffraudu-
recall,andF1score.Thiswillmeanitcandetectfraudmoreimpres- lentactivities,andthereforesecureandpreservetheintegrityof
sivelyandwithfewmisclassifications. Thismeansthatprobably, financialtransactionsinthePhilippines.
ANN-SMOTEcouldprobablybehighlyefficient,forexample,in Theresearchershavetakenadetaileddrivethroughvariousma-
creditcardfrauddetection,whereillegaltransactionsareveryfew chinelearningmodelsinserviceforcreditcardfrauddetection.
as compared to legal ones. On the other hand, even if the LR Thissectionwillmainlyfocusonhowwellthesemodelsperform
models—bothLR-GAandLR-SMOTE—exhibitrelativelypoorper- intermsofaccuracy—oneofthemajorfactorsindetermininghow
formanceconsideringthesemetrics,theycanturnouttobeuseful efficienteachmodelisatthedetectionoffraudulenttransactions.
inapplicationsforwhichtheinterpretabilityofthedecisionsmade Further,somestrategicideasthatareaimedatenhancingthefore-
byamodelisparamount. Inparticular,inregulatorycompliance, castaccuracyandtotalefficiencyofsuchmodelsaresought. The
180

ExploringMachineLearningforCreditCardFraudDetectionfromaPhilippinePerspective WSSE2024,September13–15,2024,Kyoto,Japan
Table1:EvaluatingMachineLearningModelsforCreditCardFraudDetection:AccuracyandImprovementStrategies
Model DatasetDescription Method Accuracy WhattoImprove Reference
Logistic Creditcardtransactiondata Supervisedbinary 54.86% Explorehybridsamplingto [23]
Regression fromthePhilippines classification handleimbalanceddata
K-Nearest Datapointsclusteredbased Non-parametric, 97.69% Increasethediversityand [24]
Neighbors onproximitytodetectfraud nearestneighbor sizeofthedatasetforbetter
(k-NN) generalization
NaïveBayes Transactionpatternsfocusing Probabilistic 97.92% Adjustindependence [25]
onanomalydetection classification assumptionsinthemodel
SupportVector Featuresintendedto Kernel-based Variesupto Incorporatemeta-learning [26]
Machines(SVM) distinguishbetweenauthentic learningtechnique 80% forskeweddatahandling
andfraudulenttransactions
ArtificialNeural High-dimensionaldatasetsfor Deeplearning Variesupto Optimizeneuralnetwork [27]
Networks(ANN) patternrecognition algorithms 98.44% architectureforreal-time
detection
authorshaveclearlyshownthat,forinstance,someoftheirmodels detectionsystems.Resultsfromthisstudymayhelprelatedissues
addressimbalanceddatasetsorimprovingalgorithmparameters dealingwithotherdevelopingcountries.
asthecriticalareastoenhance, andthereforethisgivesaclear
avenueforfutureresearchonitspracticalapplicationinfraudde- References
tection. Thisthoroughassessmentimprovesourunderstandingof [1] KrisCrismundo.2021.DigitalfraudattemptsinPHriseamidpandemic|Philip-
thecurrentcapabilitiesandlimitationsofexistingmachinelearning pineNews.PhilippineNewsAgency.Retrievedfromhttps://www.pna.gov.ph/
articles/1134735
modelsandfurtherdrivesinnovationinmethodstosecurefinancial [2] LawrenceAgcaoili.2022.Creditcardissuersreport21%jumpinfraudcases|
securitysystemsagainstthethreatsoffraudulentactivities. Philstar.com.Philstar.Retrievedfromhttps://www.philstar.com/business/2022/
08/17/2203090/credit-card-issuers-report-21-jump-fraud-cases
[3] SherrieAnnTorres.2022.BSPsaysonlinefraudcostP540millionin2021|ABS-
3 CONCLUSION
CBNNews.Retrievedfromhttps://news.abs-cbn.com/business/01/17/22/bsp-says-
online-fraud-cost-p540-million-in-2021
Inconclusion,thedigitalpaymentsystemsthathavebeeninvented
[4] Doris Dumlao-Abadilla, D. 2021. Credit card fraud cases surge 29%. IN-
haveprovedtobeapotentialsourceofunintendedconsequences QUIRER.net.Retrievedfromhttps://business.inquirer.net/316906/credit-card-
forincreasedfraudulentactivities, especiallyinthePhilippines, fraud-cases-surge-29
[5] RepublicActNo.11765.2022.Lawphil.net.Retrievedfromhttps://lawphil.net/
which,sincetheepidemic,hasseenanincreaseincreditcardfraud
statutes/repacts/ra2022/ra_11765_2022.html
by21%.CurrentFPSSareprovingtobeutterlyinadequateintheir [6] JayHilton.2021.Philippines: Shortlistoftopfinancialscams,centralbank
securityfore-commercenetworks,whilevariouschallenges,such cracksthewhiponfraud,moneylaundering.gulfnews.com.Retrievedfromhttps:
//gulfnews.com/business/philippines-short-list-of-top-financial-scams-central-
asmanaginghugeamountsofdata,skeweddistribution,concept bank-cracks-the-whip-on-fraud-money-laundering-1.1639325591494?slide$=$1
drift,andthedemandforreal-timedetection,plagueFDSS.How- [7] RaynordeBest.2024.Cardfraudvalueworldwide.Statista.Retrievedfrom
https://www.statista.com/statistics/1394119/global-card-fraud-losses/.
ever,theintroductionofmachinelearningmodelsputsthefuture
[8] MariaWebb.2024.Creditcardfraudstatistics.Techopedia.Retrievedfromhttps:
offrauddetectiononthebrightside. Theapplicationofmodels //www.techopedia.com/credit-card-fraud-statistics.
thatcanlearnfromdatawithoutexplicitprogrammingforimprov- [9] AishaAbdallah,MohdAizainiMaarof,andAnazidaZainal.2016.Frauddetection
system:Asurvey|JournalofNetworkandComputerApplications,68,90–113.
ingsecurityine-commerceplatformsisincreasinglyused.Inthis
Retrievedfromhttps://doi.org/10.1016/j.jnca.2016.04.007
way,anadvancedwaragainstfraudformsasaferenvironmentfor [10] Li Sisters. 2024. Matthew’s correlation coefficient: When to use
digitaltransactionswithatransitionfrompre-transactiontopost- it and when to avoid it. Medium. Retrieved May 8, 2024, from
https://towardsdatascience.com/matthews-correlation-coefficient-when-
transactiondetection. Thisstudy,therefore,ismuchneededinthe to-use-it-and-when-to-avoid-it-310b3c923f7e.
Philippines,whichisclassifiedasoneofthecountrieswithalarge [11] ZachBobbitt.2021.Whatisbalancedaccuracy?(Definition&Example).Statology.
RetrievedMay8,2024,fromhttps://www.statology.org/balanced-accuracy.
volumeoffraudulentcreditcardtransactions.Inessence,whatthis
[12] IBM.Whatissupplychainmanagement?Retrievedfromhttps://www.ibm.com/
meansisthatthereshouldbeanenhancedFDSSwithadvanced topics/logistic-regression.
analytics,machinelearningalgorithms,andtechniquesforanomaly [13] IBM.Whatisthek-nearestneighborsalgorithm?Retrievedfromhttps://www.
ibm.com/topics/knn.
detectionwhilestrengtheningtheFPSSbymultifactorauthentica-
[14] Selva Prabhakaran. 2018. How naive bayes algorithm works? (with ex-
tion,encryptionprotocols,andreal-timemonitoring.Thiswould ample and full code). Machine Learning Plus. Retrieved May 8, 2024,
involvecollaborationconcerninginsight,bestpractices,andthreat fromhttps://www.machinelearningplus.com/predictive-modeling/how-naive-
bayes-algorithm-works-with-example-and-full-code.
informationsharingamongfinancialinstitutions,regulatorybod- [15] DorBank.2023.Thegame-changingroleofmachinelearningincreditcard
ies,andtechnologyproviders.Theresearchgoesfurthertooutline frauddetection|Justt.Retrievedfromhttps://justt.ai/blog/tech/machine-learning-
credit-card-fraud-detection
howmachinelearningwillbenefitfrauddetectioninthefinancial
[16] 6JohnO.Awoyemi,AdebayoO.Adetunmbi,andSamuelA.Oluwadare.2017.
sector. Tailoringmachinelearningalgorithmstotheintricaciesof Creditcardfrauddetectionusingmachinelearningtechniques:Acomparative
thePhilippinecontext—theuniqueeconomic,technological,and analysis.InProceedingsofthe2017InternationalConferenceonComputing
NetworkingandInformatics(ICCNI),1–9.Retrievedfromhttps://doi.org/10.1109/
socialaspects—iswhatcangreatlyincreasetheefficacyoffraud
iccni.2017.8123782.
181

WSSE2024,September13–15,2024,Kyoto,Japan EricBlancafloretal.
[17] V.DheepaandR.Dhanapal2012.Behaviorbasedcreditcardfrauddetection //orientreview.com/index.php/etmibd-journal/article/view/46/50
usingsupportvectormachines.ICTACTJournalonSoftComputing,2(4),391–397. [23] JohnO.Awoyemi,AdebayoO.Adetunmbi,andSamuelA.Oluwadare.2017.Credit
Retrievedfromhttps://doi.org/10.21917/ijsc.2012.0061. cardfrauddetectionusingmachinelearningtechniques:Acomparativeanaly-
[18] PhilipOlaseniShoetan,AdedoyinTolulopeOyewole,ChinweChinazoOkoye, sis.2017InternationalConferenceonComputingNetworkingandInformatics
andOnyekaChrisanctusOfodile.2024.Reviewingtheroleofbigdataanalyticsin (ICCNI),pp.1–9.Retrievedfromhttps://doi.org/10.1109/iccni.2017.8123782.
financialfrauddetection.Finance&AccountingResearchJournal,6(3),384–394. [24] KavitaArora,SonalPathak,andNguyenT.D.Linh.2023.Comparativeanalysis
Retrievedfromhttps://doi.org/10.51594/farj.v6i3.899 ofK-NN,NaïveBayes,andlogisticregressionforcreditcardfrauddetection.
[19] WaleedHilal,S.AndrewGadsden,JohnYawney.2021.Areviewofanomaly IngenieríaSolidaria,19(3),1–22.Retrievedfromhttps://doi.org/10.16925/2357-
detectiontechniquesandapplicationsinfinancialfraud.ExpertSystemswith 6014.2023.03.05.
Applications,193(1),116429.Retrievedfromhttps://doi.org/10.1016/j.eswa.2021. [25] T.Vairam,S.Sarathambekai,S.Bhavadharani,A.K.Dharshini,N.N.Sri,and
116429 TarikaSen.2022.Evaluationofnaïvebayesandvotingclassifieralgorithmfor
[20] KayodeAyorinde.2021.Amethodologyfordetectingcreditcardfraud.Cor- creditcardfrauddetection.20228thInternationalConferenceonAdvanced
nerstone: A Collection of Scholarly and Creative Works for Minnesota. ComputingandCommunicationSystems(ICACCS).Retrievedfromhttps://doi.
Retrievedfromhttps://cornerstone.lib.mnsu.edu/cgi/viewcontent.cgi?article$= org/10.1109/icaccs54159.2022.9784968.
$2167&context$=$etds. [26] NanaKwameGyamfiandJamal-DeenAbdulai.2018.Bankfrauddetectionusing
[21] ShailendraAswale,NikitaShirodkar,RohitShetMandrekar,RahulSakhalkar, supportvectormachine.Retrievedfromhttps://doi.org/10.1109/iemcon.2018.
andK.M.ChamanKumar.2020.Creditcardfrauddetectiontechniques.Retrieved 8614994.
May04,2024,fromhttps://www.researchgate.net/publication/351686482_Credit_ [27] F.Yeşilyurt,H.Temurtaş,andÇ.Bakır.2023.Detectionofcreditcardfraud
Card_Fraud_Detection_Techniques/citations withartificialneuralnetworks.ProceedingsoftheInternationalConferenceon
[22] AshishKSaxenaandAidarVafin.2019.Machinelearningandbigdataanalytics AdvancedTechnologies.Retrievedfromhttps://doi.org/10.58190/icat.2023.15.
forfrauddetectionsystemsintheUnitedStatesfintechindustry.Emerging .
TrendsinMachineIntelligenceandBigData,11(12),1–11.Retrievedfromhttps:
182