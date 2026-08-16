---
conversion_metadata:
  converted_at: "2026-07-22T12:44:32Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Charizanis et al.pdf"
  source_pdf_sha256: "cc32ae917790db26ddde679156cd53fa5144a2a31a4c22a3bc50c26dbee2599a"
  page_count: 35
  markdown_char_count: 239753
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Review
Data-Driven Decision Support in SaaS Cloud-Based
Service Models

Gerasimos Charizanis, Efthimia Mavridou, Eleni Vrochidou , Theofanis Kalampokas and George A. Papakostas *

MLV Research Group, Department of Informatics, Democritus University of Thrace, 65404 Kavala, Greece;
gecsari@cs.duth.gr (G.C.); emavridou@cs.duth.gr (E.M.); evrochid@cs.duth.gr (E.V.); tkalampo@cs.duth.gr (T.K.)
* Correspondence: gpapak@cs.duth.gr; Tel.: +30-2510-462321

Abstract: Software as a service (SaaS) is a major service model for delivering software
to end users through the cloud. SaaS platforms provide their users with cost-efficient,
flexible and scalable services that can be available on demand, anytime, and anywhere.
Moreover, SaaS empowers software providers to establish recurring revenue and create
profitable businesses. However, SaaS can endure high customer turnover due to reasons
such as serving a wide range of customers, intense competition and rapid evolution of
technology. Maintaining a regular customer base and keeping users engaged is crucial for
the survival of a SaaS business. Thus, it is crucial for SaaS providers to identify both the
reasons behind users’ engagement and churn of their app towards taking proper actions to
retain them in the long term. SaaS data regarding user behavior, subscriptions and system
performance can be utilized for deriving insights and identifying patterns to support
decision-making for SaaS providers. To this end, the aim of this survey is to review research
in data-driven decision support systems in SaaS, identifying current gaps and challenges
and highlighting directions for future improvements towards the development of more
efficient and intelligent systems.

Keywords: software as a service; churn prediction; user engagement; machine learning;
usage mining

Academic Editor: Miguel

García-Pineda

Received: 2 May 2025

Revised: 29 May 2025

Accepted: 6 June 2025

Published: 10 June 2025

Citation: Charizanis, G.; Mavridou,

E.; Vrochidou, E.; Kalampokas, T.;

Papakostas, G.A. Data-Driven

Decision Support in SaaS Cloud-Based

Service Models. Appl. Sci. 2025, 15,

6508. https://doi.org/10.3390/

app15126508

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

1. Introduction

Cloud computing is the dominant model for providing software and technology
infrastructures nowadays. This approach enables access to computing resources and
applications without the need for hardware setup and maintenance. The main cloud
service models are infrastructure as a service (IaaS), platform as a service (PaaS) and
software as a service (SaaS) [1].

The IaaS model provides infrastructure resources through the cloud such as storage
and computational power. Users do not have to update and maintain the infrastructure, yet
they are in charge of setting up operating systems, software and data [2]. On the contrary,
the PaaS model also provides the software resources for creating software in the cloud.
Users do not maintain the software development environment, but they have to write their
own code. Finally, the SaaS model provides ready-to-use software solutions [3], meaning
that the users can start using the software without installation. Therefore, IaaS and PaaS
users are mainly developers and IT professionals, while SaaS users can vary depending on
the solution provided by the SaaS. For example, a SaaS that provides invoicing software
may have users ranging from various professions, e.g., engineers, lawyers, etc. The SaaS
model is the leading cloud computing model for delivering software nowadays since it

Appl. Sci. 2025, 15, 6508

https://doi.org/10.3390/app15126508

---

<!-- PAGE 2 -->

Appl. Sci. 2025, 15, 6508

2 of 35

enables software distribution without the need for installation and hardware setup [4].
Thus, users can use them easily and quickly, while generally paying by subscription instead
of a large amount upfront.

The SaaS model enables software providers to create profitable businesses allowing
software distribution through the cloud to many users, simultaneously [5]. Moreover, the
subscription-based business model provides opportunities for stable income streams. Thus,
the success of a SaaS model as a business heavily depends on whether it maintains a core
user base. When users experience meaningful benefits from a software solution, they use it
regularly and for a long time. Engaged users are the superpower of SaaS since they tend to
use it in the long term and with minimum support, while they could possibly suggest it to
other users. The cost of obtaining new users is generally much higher than retaining the
ones that already exist [6]. Thus, SaaS businesses strive to increase user engagement and
reduce user churn, i.e., the percentage of users that cancel their subscriptions.

Recent industry reports point to several growing challenges that make strong, data-
driven decision support systems more important than ever for SaaS companies. One major
issue is the high rate of customer churn, shortly after customers sign up, which is commonly
observed with new artificial intelligence (AI)-powered tools (https://www.paddle.com/
blog/saas-market-report-q1-2025, assessed on 1 June 2025). This is particularly a problem
in the B2C market, where user behavior changes quickly and is hard to predict. At the
same time, many SaaS businesses do not pay enough attention to how they adjust their
prices, even though pricing can have a big impact on user retention (https://www.omnius.
so/blog/saas-industry-report-2024, assessed on 1 June 2025). Another challenge is the
rise of multi-cloud and hybrid systems, where companies run their software across several
cloud platforms. This makes it harder to gather and analyze all of their data in one
place (https://www.fortunebusinessinsights.com/software-as-a-service-saas-market-10
2222, assessed on 1 June 2025). The growing use of AI in SaaS platforms introduces
new benefits, like automation and personalization. However, this also leads to higher
infrastructure costs due to expensive computing resources like GPUs, high-volume data
usage, and the need for highly skilled professionals to build and maintain AI systems
(https://www.paddle.com/blog/saas-market-report-q1-2025, assessed on 1 June 2025).
These trends in the SaaS industry indicate that SaaS providers face increasingly complex
decisions. As a result, the role of data-driven decision support systems becomes critical in
helping SaaS vendors make informed, timely, and cost-effective choices.

At the core of modern SaaS ecosystems, vast amounts of data are generated, regarding
user behavior, subscriptions and system performance [7]. SaaS data can be leveraged for
deriving insights and identifying patterns to support decision-making for SaaS providers.
For example, machine learning (ML) algorithms can be employed to create churn prediction
models for user churn prediction [8]. Given that information, SaaS providers can act with a
specific incentive to reengage those users. To this end, the aim of this survey is to review
research in data-driven decision support in SaaS applications. In particular, the goal of this
work is to identify research that utilizes data to support SaaS vendors towards reducing
churn and increasing user engagement, satisfaction and loyalty.

Although related works are already present in the literature [9–11], this study stands
out by offering a comprehensive perspective on leveraging SaaS data to support decision-
making for SaaS vendors to sustain user loyalty and satisfaction. Unlike prior research that
often focuses narrowly on specific tasks such as churn prediction, this work provides a
holistic examination of strategies to maintain a stable user base. Specifically, the diverse
objectives of existing approaches are analyzed, as the variety of employed data sources,
and the comparative effectiveness of different machine learning methods on multiple
occasions. Moreover, the ways the outputs of these approaches, ranging from visualizations

---

<!-- PAGE 3 -->

Appl. Sci. 2025, 15, 6508

3 of 35

to actionable insights, are presented to SaaS vendors to facilitate spot-on decision-making,
are also discussed.

The rest of the paper is structured as follows: Section 2 presents related works and
highlights the contributions of this paper. Section 3 summarizes the research methodol-
ogy, while Section 4 presents the results. Discussions and conclusions are provided in
Sections 5 and 6, respectively.

2. Related Work

The current work constitutes a scoping review of research to assist SaaS vendors in
decision-making based on the data that SaaS businesses generate. Therefore, the aim is to
identify research efforts that perform literature reviews on the same subject. To the best
of our knowledge, there is no exact type of review found in the literature. However, there
are literature reviews that are related to the subject, yet with different focus. For example,
the authors in [9] performed a review on machine learning methods for churn prediction
covering the years between 2015 and 2023. Although their work provided insights on the
use of ML for churn prediction highlighting the trade-offs of different ML methods, the
focus was only on churn prediction, and it did not address other use cases such as user
segmentation or customer lifetime value prediction which are critical to support business
owners on decision-making. Moreover, the review focused on telecommunications, finance
and online gaming industries, regardless of the type of businesses and the adoption of
cloud-based models and SaaS specifically. To this end, our work constitutes a review
tailored to support businesses that operate based on the SaaS cloud model providing a
more holistic approach by covering a wide range of use cases, important to retain a strong
customer base.

Similarly, the authors in [10] conducted a general review of decision analytics ap-
proaches for cloud computing. It’s also worth noting that their work was published more
than 10 years ago, in 2014, and therefore it does not cover current research efforts. The
authors focused on decision support for cloud computing for problems like service selection
and pricing, rather than discussing decision support for user retention and engagement.
Moreover, there was no description of the systematic review research methodology and no
information or statistics regarding the number of papers included in their review. Moreover,
the authors considered papers with methods that were not data-driven, like heuristics
or ontology-based. The review presented in [11] addressed a broad range of different
topics AI, ML, Business Intelligence (BI) and SaaS at a high level without going into detail.
Regarding user behavior, authors discussed prediction strategies and personalization of
user experience, however, without going into specific insights and recommendations. A
systematic review methodology was also missing.

Another paper [5] published in the same year (2014) covered the technical challenges
and perspectives for SaaS such as multi-tenancy and scalability. That review also lacked a
research methodology and did not mention how the reviewed approaches were selected.
Performance comparisons were not included, and only a qualitative analysis was per-
formed. Lastly, there was no focus on user interaction subjects like user retention and churn.
Finally, the research presented in [11] addressed AI adoption for BI in SaaS. Although it
was mentioned that a literature review was conducted, only 8 papers were included in
their analysis.

To this end, compared to the existing bibliography, the current work:

•
•
•

Presents a systematic review process.
Includes only data-driven methods.
Presents of performance comparison to support model selection.

---

<!-- PAGE 4 -->

Appl. Sci. 2025, 15, 6508

4 of 35

•

Discusses of challenges the SaaS vendors face regarding maintaining a core user base
like churn, user engagement and user retention.

Moreover, the contributions of this work can be summarized in the following

distinct points:

• A comprehensive review of research initiatives aiming to support decision-making
for SaaS providers, expanding beyond single-task approaches to address broader
strategic goals.
An overview of various data inputs utilized across studies, identifying frequently used
data sources and highlighting cases where multiple kinds of data were integrated for
more robust insights.

•

•

• A comparative evaluation of employed machine learning techniques, analyzing their
relative strengths, weaknesses, and performance in different SaaS decision-making contexts.
An overview of user-faced output types proposed by researchers to help SaaS providers
take effective, data-driven actions.
A synthesis of best practices and key takeaways from the literature, offering actionable
recommendations for enhancing user retention and ensuring the long-term sustain-
ability of SaaS business models.

•

3. Research Methodology

The research questions that we aim to answer in this survey are the following:
RQ1: What is the main focus of the papers in the area of data-driven methods for

supporting decision-making in SaaS?

RQ2: What kind of data is utilized?
RQ3: Are machine learning methods employed and how effective are they?
RQ4: How are the results presented to SaaS providers to support decision-making?
The survey was conducted following the PRISMA-ScR methodology. The research was
conducted using the Scopus and Scholar bibliographic databases that contain papers from
libraries like Springer, Elsevier, IEEE, etc. The following query was posed on 5 March 2025
to Scopus:

(“web usage mining” OR “customer segmentation” OR “log analysis” OR “churn”
OR “user engagement” OR “customer lifetime value” OR “user lifetime value” OR “user
segmentation”) AND “SaaS” AND PUBYEAR > 2013 AND PUBYEAR < 2026.

This query returned 426 results. Screening was performed by reading the title and
abstract in order to identify the completely irrelevant ones. This process resulted in
147 papers. These papers were searched and retrieved in order to read them thoroughly.
During this second screening phase, there were excluded all papers that were not relevant
to our subject. Relevancy was based on three main rules: papers should be about SaaS,
decision-support and based on data. Thus, the excluded papers of the second phase fall
into one of the three categories:

• Not related to SaaS;
• Although related to SaaS they were not about supporting decisions;
• Not data-driven, theoretical.

This process resulted in 22 papers that were included in our survey. A supplementary
search was conducted in Google Scholar using keywords like “churn prediction SaaS”,
“user engagement SaaS” and “user lifetime value SaaS” resulting in 6 more papers. Thus, a
final list of 28 papers was formed that was analyzed further. Figure 1 illustrates the research
process followed.

---

<!-- PAGE 5 -->

Appl. Sci. 2025, 15, 6508

5 of 35

Figure 1. PRISMA flow diagram.

At this stage, it is important to acknowledge the limitations of this research. The
research was limited from 2014 to 2025, so as to cover a full range of 10 years, as well
as due to the fact that SaaS adoption began to rise mainly after 2014, where the main
volume of literature was located. However, the latter did not affect our research findings,
since the main volume of the research was located after 2014 and especially from 2020
onwards. Moreover, the database coverage was limited to Scopus and Google Scholar.
While other databases also exist, such as Web of Science or PubMed, the use of both Scopus
and Google Scholar could improve coverage and reliability, as they both cover a wide range
of peer-reviewed sources.

4. Data-Driven Decision Support in SaaS
4.1. Main Focus

The SaaS model is mainly offered by subscription which is the main source for revenue
generation for such businesses. Having a strong user base is crucial for the viability of
SaaS businesses. Therefore, it is very important for SaaS to maintain a small percentage of
users that cancel their subscriptions (churn). For SaaS businesses, even a small reduction in
churn can lead to significant profit growth and a healthier and long-term business. For this
reason, many researchers focus on predicting churn in SaaS businesses and on identifying
the best performing machine learning algorithms for each case.

Figure 2 summarizes the results regarding RQ1. As can be seen in Figure 1, most of
the reviewed papers (53.57%) focused on churn prediction. This comes as no surprise since
high churn rates cannot sustain a SaaS business model. The churn rate is the number of
users that leave the SaaS divided by the total number of users. Churn prediction refers to
predicting if a user is about to churn. The authors in [12,13] focused on applying and testing

---

<!-- PAGE 6 -->

Appl. Sci. 2025, 15, 6508

6 of 35

various algorithms fed with usage data to evaluate their performance in churn prediction,
in the context of SaaS, while research presented in [8,14–17] followed the same principle
but shifted their focus towards the Business to Business (B2B) SaaS business model. All
those studies aimed to point out key features that churning customers possess and offer
SaaS providers actionable insights for improving their customer retention strategies.

Figure 2. Main focus of the reviewed papers (RQ1).

Further research on this topic included in [18,19] focused on comparing multiple
machine learning algorithms to figure out which one was best performing for churn
prediction in the SaaS cloud service model. The authors in [18] developed a churn prediction
system to predict customer attrition for cloud-based service providers (CSPs), attempting
an early identification of customers at risk of canceling subscriptions. Churn prediction in
Customer Relationship Management systems (CRM) using hybrid machine learning models
was addressed in [19]. Apart from the comparison between machine learning methods, the
authors in [20] chose to use machine learning to analyze and monitor customer satisfaction
from support tickets and predict whether a client is going to renew their cloud service
subscription. Accordingly, the research presented in [21] experimented with the creation
and application of a hybrid machine learning framework designed for real-time prediction
of user events in SaaS products such as subscription cancellation, user interactions, and
task abandonment during user sessions.

Several research efforts dealt with predicting churn and improving retention specif-
ically for online games based on the SaaS model. The strategy employed in [22] aimed
to identify churners in earlier stages of a mobile freemium game, even after the tutorial
phase, using minimal early-stage user data, featuring a Transformer-based architecture (FT-
Transformer) tailored for tabular data. The research presented in [23] focused on predicting
player churn and disengagement within a 14-day window in a freemium online strategy
game using machine learning. Specifically, it aimed to identify the most effective machine
learning techniques and labeling approaches for early detection of players at risk of leav-
ing the game, enabling proactive retention strategies. In [23] the authors distinguished
between churn (permanent departure) and disengagement (reduced activity), providing a
comprehensive comparison of methods tailored to the gaming industry. The authors of [24]
extended their research to a larger time span, focusing on improving churn prediction in
casual freemium games by combining sequential (temporal) and aggregated (static) data
using different neural network architectures. Their study investigated how integrating
these two types of data can enhance prediction accuracy compared to models that rely
solely on sequential or aggregated data while also addressing the challenge of predicting

---

<!-- PAGE 7 -->

Appl. Sci. 2025, 15, 6508

7 of 35

churn in non-contractual contexts (for example in mobile games), where players could
leave without explicit signals.

Additionally, the research conducted in [25] focused on enhancing retention analysis
in freemium role-playing games (RPGs) by modeling players’ motivation, progression,
and churn. Particularly, it aimed to understand how in-game behaviors (engagement,
collaboration, and achievement) at different levels influence dropout rates, and how these
interdependencies could be leveraged to predict player retention more accurately. As
player retention in the video game industry is the key to its ongoing prosperity, work in [26]
explored how video game operators can retain players in subscription-based games by
dynamically adjusting the quality of the game over time. The study developed a dynamic
programming model that considered players’ memory of past service experiences and
network externalities (the phenomenon where the value or utility of a product or service
increases as more people use it) to determine the optimal data-driven decisions to maximize
long-term profits.

In order to better understand and adapt to clients’ needs in SaaS services it is impor-
tant to categorize them into groups to be able to provide them personalized attention. An
iterative mixed-method approach for creating user personas in the context of B2B SaaS
products was presented in [27]. That work also aimed to demonstrate how the generated
user personas could be practically applied as an indicator to improve the design, develop-
ment, and prioritization of features in a B2B SaaS product. Another research on customer
segmentation was presented in [28], particularly exploring how behavioral customer seg-
mentation and app usage analysis can be leveraged to predict customer interest in premium
subscriptions and identify key influencing factors to improve subscription conversion rates
for mobile apps. User conversion from free trials to paid subscriptions was the main focus
of [29], examining how marketing interactions (ads, messages, emails, etc.) and their type
of content along with free-trial usage behaviors could influence users’ decisions. Further
insights regarding free trials were showcased in [30]. The study highlighted the importance
of free trials as a customer acquisition strategy in the SaaS industry and analyzed how
customer acquisition, retention and profitability were affected by the duration of free trials
to discover their optimal design.

Establishing a long-term relationship with customers requires keeping them engaged
and satisfied with the services they are getting. The authors in [31] examined how visual
and functional aspects of user interface (UI) design could influence user experience (UX).
Advancing further on the subject of customer loyalty, the authors in [32] followed a data-
driven approach to discovering the determinants of customer loyalty in the B2B SaaS indus-
try. That study explored how transactional and behavioral data (like platform engagement,
and communication frequency) could be leveraged to predict customer loyalty without
relying on traditional surveys. The research presented in [33] proposed the design of an
adaptive negotiation mechanism to allow providers to interact with clients and dynamically
manage service quality, user satisfaction, and resource costs in cloud environments.

A very impactful factor in keeping customers from churning is whether these indi-
viduals discover the “aha moment” and acknowledge the return on their investment in
SaaS services. The “aha moment” refers to the point when users understand the value
of the software product, which is crucial for enabling customer activation and retention.
The authors of [34] focused on identifying the “aha moment” of B2B SaaS customers using
process mining techniques. Specifically, this study investigated how customers switch
from the activation phase to the retention phase in the AARRR (Acquisition, Activation,
Retention, Revenue, Referral) model by identifying and examining behavior patterns of
clients. In order to provide value to their customers, customer feedback must be taken into
consideration, so that providers can offer a more personalized experience and cater to their

---

<!-- PAGE 8 -->

Appl. Sci. 2025, 15, 6508

8 of 35

clients’ needs. The research presented in [35] explored structured approaches for collecting
and integrating customer feedback in SaaS companies operating in the B2B market and
ways of integrating customer knowledge into software development processes.

SaaS pricing also takes its toll on user satisfaction as it affects SaaS users directly.
The study presented in [36], however, showcased a data-driven framework integrating
real-time usage tracking, machine learning for demand prediction, and customer-centric
billing adjustments to optimize revenue for providers while enhancing user experience and
customer loyalty. Additional factors influencing usage continuance in SaaS applications,
particularly after the initial adoption phase were demonstrated in [37], in an attempt to
improve user retention and reduce churn by enhancing usage penetration (the number of
users actively engaging with the software).

Finally, another problem that the research addressed was the Customer Lifetime Value
(CLV) prediction. CLV prediction models predict the future revenue that customers may
generate. The authors in [38] proposed a novel machine learning framework for predicting
CLV in the context of B2B SaaS companies and described several business applications
where CLV predictions were used to enhance marketing expenditures, improve Return
on Investment (ROI), and provide essential insights for management decision-making in
this context.

4.2. Data Sources

In order to compare and evaluate algorithms for predicting churn in SaaS businesses,
researchers chose to utilize various types of data sources for their experiments. As per
the research question RQ2, the most common category among studies [8,12–19] is usage
behavior data. All those studies incorporate some form of user interaction or system
activity logs like logins, sessions, file uploads, application usage, number of users and
actions performed.

Another common type of data used in [8,12–14,16,17] is transactional and business
metrics including monetary values (monthly charges, total expenses, amount spent), sub-
scription status and billing information. Additionally, temporal data, contractual data
and customer lifecycle indicators appeared in [12,13,15,17–19] concerning customer tenure,
days to expiry, subscription age and monthly snapshots or observation windows while in
studies [8,16–19] customer demographics and attributes were also utilized (company size,
region, industry, onboarding status or business age).

The authors in [18] also used billing and loyalty program data like loyalty program
status and billing cycles. At last, customer support interaction data were used in [15]
(support tickets, resolution times) and [16] (support case logs) while customer satisfaction
metrics such as Net Promoter Score (NPS) and call quality were specifically included in [17].
Furthermore, regarding churn prediction, the approach followed in [20] used support and
subscription metadata while the study [21] focused on clickstream data combined with
dynamic user profiles (subscription status, tenure, demographics).

Studies that focused on predicting churn in games featuring a subscription model as
in [22–24], shared a strong emphasis on event logs, session data, and gameplay behavior
and chose to utilize behavioral data (gameplay actions, tutorial engagement, session metrics,
clicks, purchases, logins) to design their churn predicting models.

Focusing on improving retention of freemium online games, the study [25] conducted
its research by utilizing player behavioral data (engagement, achievements, collaboration,
progress, dropouts), demographic and contextual data (gender of game characters, geo-
graphic location, time of play), and some game-specific metrics. Moreover, the data used
in [26] was derived from a simulated dataset containing synthetic data (simulated quality
levels, utility functions, and cost structures).

---

<!-- PAGE 9 -->

Appl. Sci. 2025, 15, 6508

9 of 35

Data in [27] are derived from surveys, interviews and web behavioral data (time spent
per page, clicks per feature, aggregated over time) and are used in customer segmentation
algorithms. On the same page, work [28] used demographic features (age, gender, state),
behavioral features (engagement level, time spent, number of screens viewed, clicks,
sessions) and transactional features (maximum budget, maximum return on investment,
number of purchases) for customer segmentation.

For the purpose of discovering drivers of user loyalty and improving user satisfaction
and engagement, studies [29–32,34,37] leveraged mainly behavioral and usage data (login
frequency, feature usage, interaction patterns to understand user engagement, product
adoption over time). However, in [35,37] interview and survey data were used, providing
context on user perceptions, satisfaction, and demographic characteristics. In studies [34,35],
system logs and event data were used and specifically in [35] logs are used alongside direct
feedback like surveys and support tickets. Marketing, free trial, and transactional data (ad
impressions, message types, marketing variables and trial duration variations) are utilized
by researchers in [30,33] while in [36] simulated data were employed (transaction volumes,
volatility, user-centric metrics, user profiles, negotiation dynamics) to explore hypothetical
user behaviors and negotiation dynamics in scalable, controlled environments. Last, stud-
ies [32,35] utilized rich, multi-source data integrations, combining CRM, financial, usage,
and external firmographic data in order to better model loyalty and customer relationships.
Finally, research [38], which focused on predicting CLV, employed various types of
data to achieve its goal. Those data included revenue data (monthly recurring revenue,
historical billing data), product license data (product types, acquisition channels, license
terms), product usage data (feature adoption, user activity logs, engagement metrics),
firmographic data (company size, industry, geography, employee count) and customer
segments based on behavior. Table 1 summarizes the types of input data used in the
reviewed approaches.

Table 1. Types of data sources used by the reviewed approaches (RQ2).

Ref.

Usage
Behavior

Transactional/
Business
Metrics

Customer
Profile

Financial
Data

Customer
Support

Satisfaction
(e.g., NPS)

Survey/Interview Marketing

✓

✓

✓
✓

[18]
[24]
[12]
[14]
[22]
[19]
[25]
[13]
[20]
[15]
[8]
[23]
[21]
[38]
[29]
[30]
[31]
[26]
[33]
[32]
[27]
[37]

✓
✓
✓
✓
✓
✓
✓
✓

✓
✓
✓
✓
✓

✓
✓

✓
✓
✓
✓

✓
✓

✓

✓

✓

✓

✓

✓
✓
✓

✓
✓

✓
✓

✓
✓

✓

✓
✓

✓
✓

✓
✓

✓
✓

---

<!-- PAGE 10 -->

Appl. Sci. 2025, 15, 6508

10 of 35

Table 1. Cont.

Ref.

Usage
Behavior

[16]
[28]
[35]
[17]
[36]
[34]

✓
✓
✓
✓

✓

Transactional/
Business
Metrics
✓
✓

✓
✓
✓

Customer
Profile

Financial
Data

Customer
Support

Satisfaction
(e.g., NPS)

Survey/Interview Marketing

✓

✓

✓

✓

✓

✓
✓

✓

✓

4.3. Machine Learning Methods

Regarding RQ3, most of the studies relied solely on machine learning methods to
conduct their research and generate their expected results. Among the papers focused on
churn prediction, Random Forest (RF) [39–41] was one of the most widely used methods,
appearing in studies [8,13–19,23,24]. In the study [18], RF with 64 estimators achieved an
excellent performance of 98.8% accuracy, 0.997 Area Under the Curve (AUC), and strong
F-measures (0.989 non-churn, 0.981 churn). In studies [8,14], RF also stood out with 87%
testing accuracy, while being resistant to noise and overfitting. A study [13] reported
exceptionally strong RF results as well, with F1-score of 92.6% and recall of 91.6%, while a
study [15] found that RF had the highest precision (0.80) among the models tested, though
recall lagged behind XGBoost. On the contrary, RF underperformed in the study [12], with
an AUC of ~0.5, and adding PCA (Principal Component Analysis) did not have any impact
on the results. In work [23], RF achieved AUC > 0.99 and 97% accuracy, outperforming all
other models across various labeling schemes like sliding windows and activity quartiles
while in the study [24] RF was used as a baseline combining sequential and aggregated data,
where it achieved an AUC of 0.72, which was notably lower than the hybrid Long Short-
Term Memory (LSTM) models, indicating its limitations in modeling temporal dynamics
in sequential data. In the study [17], RF showed only moderate success with AUC-ROC
~0.65, though its performance improved slightly when paired with SMOTE-Tomek for class
imbalance handling. Figure 3 presents the number of papers that successfully employed
specific machine learning algorithms. Thus, it contains the number of papers to which the
specific machine learning algorithm noted the best results. RF was successfully used in
more works than any other machine learning algorithm.

Extreme Gradient Boosting (XGBoost) [42] was tested in studies [12,15,16], consistently
delivering top-tier results. In research [12], XGBoost achieved the highest AUC (0.7941)
and, after threshold tuning, improved sensitivity to 74%. Study [15] reported ROC AUC
of 0.86, recall of 0.85 and F1-score of 0.82, outperforming other models such as Random
Forests and Logistic Regression and identified ticket resolution time and license age as
key features. Study [16] found XGBoost and Logistic Regression achieved comparable
AUC (~60%), but XGBoost was less profitable than logistic regression when measured by
Expected Maximum Profit. XGBoost and Gradient Boosting Decision Trees (GBDT), were
also used in [22] with XGBoost emerging as the best-performing model with 98.8% AUC,
while GBDT followed with 93.4% AUC.

Decision Trees (DT) were used in studies [8,13,14,16,19]. In work [13], DT was the
best performer using Chi-squared-selected features, with 88.2% F1-score and 94.4% recall.
In contrast, studies [8,14] revealed DT’s tendency to overfit, achieving perfect training
accuracy but only 76% on test data. DT also served as a baseline in [16,19], with moderate
performance compared to ensemble and hybrid models.

---

<!-- PAGE 11 -->

Appl. Sci. 2025, 15, 6508

11 of 35

Figure 3. Machine learning methods proposed to use by the reviewed papers.

Logistic Regression (LR) [43] was applied in studies [8,12,13,15–17], mostly as a base-
line due to its interpretability. Its AUC ranged from 0.71 to 0.74 in studies [8,12], and
it consistently offered stable, if lower, performance. In work [16], LR delivered strong
profit-based performance, leading in Expected Maximum Profit and Top Decile Lift when
paired with usage-based features. In the research [17], LR initially had 97% accuracy but
0% recall until SMOTE-Tomek was applied, improving recall to 57% (but at the cost of
reduced precision).

Support Vector Machines (SVM) featured in studies [8,13,14,16,19]. SVMs often
struggled—studies [8,14] reported 100% training accuracy but just 63% test accuracy, indi-
cating severe overfitting. However, the study [19] successfully employed a hybrid model
combining SVM with Naive Bayes, achieving 95.67% accuracy, 94.3% precision, and 95.65%
recall, outperforming other classifiers. In work [16], SVM delivered strong profitability
metrics, rivaling LR in Expected Maximum Profit.

Neural Networks (NN) (including MLPs and deep learning) appeared in [8,14,15,18,20,23,24].
A study [18] reported 96.5% accuracy for a Multilayer Perceptron (MLP), which, while
lower than RF and AdaBoost, still offered valuable comparative insights. In works [8,14],
deep neural networks (including TensorFlow models) achieved around 82% test accuracy,
with one model identifying subtle churn signals like low session frequency and high pricing.
MLP was again tested in [15], performing adequately but trailing ensemble methods like
XGBoost and Gradient Boosting Machine (GBM). In [24], a non-sequential NN using only
aggregated features yielded lower performance (AUC not specified), underperforming
In research [20], sentiment modeling with LSTM
compared to LSTM-based hybrids.
networks produced learned sentiment features from support ticket data, which when
combined with metadata features, led to a noticeable +5% increase in accuracy and the
highest recall, critical for predicting subscription renewals. Single-layer neural networks
were employed in [23] achieving AUC = 0.987, though their performance degraded over
time due to staleness, making them less ideal for evolving user behavior.

AdaBoost [44] and other boosting techniques such as GBM [45] were included in
studies [15,18]. AdaBoost in [18] was the second-best performer with 98.4% accuracy and
0.995 AUC, while in [15], boosting methods (especially XGBoost) consistently outperformed
simpler classifiers across recall, AUC, and F1-score.

---

<!-- PAGE 12 -->

Appl. Sci. 2025, 15, 6508

12 of 35

Naive Bayes [46], though rarely a top performer, was evaluated in [8,14,19]. It per-
formed poorly when used alone in [8,14] (accuracy ~69–71%), but in [19], it formed part of
the high-performing hybrid model with SVM.

Transformer-based models [47] were explored in the study [22]. The FT-Transformer,
built for tabular data with embedded categorical and numerical features, achieved 86.79%
accuracy, 88.75% recall, and 94.9% AUC—a strong improvement over older works (AUC
~71–77%), though it was still outperformed by XGBoost (AUC 98.8%, F1 94.81%, accuracy
94.8%) in the same study.

Hybrid Models were explored in [19], where an SVM-Naive Bayes combination led to
superior performance across all key metrics, indicating the strength of ensemble learning
strategies, especially in reducing false positives/negatives for CRM applications. Addi-
tionally, ensemble and hybrid architectures were core in studies [20,21,24]. Hybrid LSTM
architectures combining sequential and static aggregated data outperformed single-source
models [24]. Study [21] introduced the BBE-LSWCM ensemble, integrating LightGBM,
BiLSTM, and LR to achieve 60% better decile lift (DL1 = 3.197) and 25% higher AUROC
than standalone BiLSTM, while maintaining reasonable latency. A modular fusion of LSTM-
learned sentiment features and handcrafted metadata yielded the highest accuracy and
recall, demonstrating the value of combining deep learning with traditional features [20].
The researchers in [26] employed a dynamic programming model to optimize player
retention over time alongside a Q-learning algorithm [48] to simulate offline decision-
making and identify convergence paths for both actual and perceived quality. The results
indicated that both game quality and perceived quality stabilized at high levels regardless
of initial quality. However, the speed of convergence depended on starting conditions,
with lower initial quality (x0 = 0.4) taking 20 periods to converge compared to 14 periods
for x0 = 0.6. Interestingly, when players initially overestimated quality, perceived quality
followed a “high-low-high” trajectory.

The authors of [27] employed an iterative clustering approach starting with PCA for
dimensionality reduction and K-means clustering, later switching to Uniform Manifold
Approximation and Projection (UMAP) and Hierarchical Density-Based Spatial Clustering
of Applications with Noise (HDBSCAN) for more effective handling of sparse and non-
normal data distributions. After four iterations, the final model identified six meaningful
personas (e.g., Uploaders, TV Builders), which were validated through interview-based
triangulation. Earlier clustering failed due to overlapping behaviors and sparse data, but the
refined method succeeded in differentiating user types by combining behavioral data with
qualitative insights. At last, in the study [28] a more traditional machine learning approach
was adopted for behavioral customer segmentation to predict subscription conversion
by evaluating several classifiers, including Decision Tree, K-Nearest Neighbors (KNN),
Naive Bayes, RF, LR, SVC, and XGBoost. Among these, XGBoost achieved the highest
performance, with an accuracy of 79%, precision of 80%, recall of 76%, and an F1-score of
78%. Cross-validation further confirmed the generalizability of the model with a mean
score of 78.5%. However, the model exhibited a slightly higher rate of false negatives than
false positives, a relevant trade-off when considering conversion sensitivity.

Studies [30,32,36] utilized machine learning and statistical modeling to personalize
user experience and predict outcomes. Study [30] employed Lasso regression [49] to
personalize free trial lengths, showing a 6.8% subscription increase compared to a 30-day
baseline. Simpler uniform policies like a 7-day trial still yielded a 5.59% gain. Among
alternatives, Lasso outperformed random forests and causal forests, which struggled
with overfitting and poor personalization. Similarly, a study [36] implemented logistic
regression, random forest, and gradient boosting for dynamic pricing in usage-based
models. While logistic regression achieved perfect accuracy on simulated data, real-world

---

<!-- PAGE 13 -->

Appl. Sci. 2025, 15, 6508

13 of 35

applicability favored gradient boosting and random forest, with accuracies around 0.77
and 0.75, respectively. Study [32] leveraged hierarchical logistic regression within the Cross
Industry Standard Process for Data Mining (CRISP-DM) framework to predict customer
retention and cross-buying. Retention prediction reached 93.7% accuracy (F1: 94.38%),
while cross-buying was less predictable (accuracy: 78.9%, F1: 20.60%).

Finally, in the work presented in [38], the authors used a hierarchical ensembled ma-
chine learning framework for predicting CLV in B2B SaaS companies. The CLV prediction
was framed as a lump sum regression task rather than a traditional time-series forecasting
problem, enabling the use of rich supervised learning models like LightGBM, XGBoost,
LASSO regression, KNN, and Auto ARIMA. To handle limited and drifting historical data,
a two-step hierarchical model was built: first predicting over a short time horizon, then
mapping it to a longer horizon. They also adopted an ensemble approach, segmenting
customers based on key features (like size) and fitting different models for different groups
(LightGBM for smaller customers, LASSO for enterprises). In performance tests, the lump
sum regression models outperformed traditional time-series models by 2 to 5 times across
metrics like Root Mean Square Error (RMSE), Mean Absolute Error (MAE), and symmetric
mean absolute percentage error (SMAPE), with LightGBM giving the best results.

Few researchers, however, opted to utilize several methods that rely on statistical,
econometric or heuristic models. In detail, study [34] deployed Process Mining [50], specifi-
cally Heuristic Miner and Fuzzy Miner, to track user behaviors leading to “Aha! moments”.
Through data cleaning and retention clustering, it identified key activation actions by
reducing model complexity by 62%. However, manual data processing was time-intensive.
Linear Mixed Models (LMMs) were utilized in [37] to evaluate usage continuance.
It accounted for repeated measures and individual client variability through fixed and
random effects. For existing clients, the model achieved an RMSE of 5.23, though it
struggled with new clients (RMSE: 13.93), indicating a gap in generalization. Activation
measures (banners) significantly increased usage (+5.2%).

PLS-SEM (Partial Least Squares Structural Equation Modeling) was employed in [31]
to validate the effect of UI design on satisfaction and loyalty. The results showed strong
model reliability (Cronbach’s alpha: 0.837–0.860) and high explanatory power (R2 ~ 0.50).
All hypotheses (UI design → Satisfaction → Loyalty) were statistically supported.

Focusing on the topic of customer segmentation, the study [25] introduced a joint
modeling framework that combined Generalized Linear Mixed Models (GLMMs) [51] to
track players’ in-game behavioral patterns with a Shared Parameter Model (SPM) [52] that
linked these behavioral groups to the probability of dropout. This integrated approach
significantly outperformed traditional models like Cox regression, improving retention
prediction by 63.2% at higher player levels and reducing RMSE for lifetime engagement
by 25.5%.

Authors in [29] took a more econometric route, applying a Dynamic Probit Model [53]
with copula-based corrections for endogeneity. It incorporated exponentially decaying
goodwill stocks to model user touchpoints and usage effects. In this study regularization
via Lasso/Ridge regression was also utilized, addressing multicollinearity and improv-
ing model stability. The study achieved a 9.3% error reduction in predictions and key
findings emphasized that consumer-initiated touchpoints and persuasive content boosted
conversions to premium users, while firm-initiated ads had negative effects.

Study [33] introduced the AQUAMan negotiation mechanism, combining quantile
estimation, opponent modeling, and surplus redistribution to manage service acceptability.
Under both normal and extreme loads (up to 2500 users/min), it maintained high accept-
ability rates (95%+ and 93.3%, respectively) while keeping costs and overhead manageable.

---

<!-- PAGE 14 -->

Appl. Sci. 2025, 15, 6508

14 of 35

At last, study [35] outlined a range of qualitative (interviews, questionnaires, incident
reports) and quantitative (A/B testing, in-product surveys and online ads, crowdfunding
and crowdsourcing platforms, click-based user data collection) methods deployed for
collecting and integrating customer feedback, as well as insights into their performance
across several companies. This study concluded that there’s no single perfect approach and
that the choice and success of methods depend heavily on the company’s size, the structure
of the product offering (custom vs. SaaS), the type of customers (B2B vs. B2C), the stage of
development and the internal communication and data integration structure.

Table 2 summarizes the results regarding the use of machine learning in the reviewed

approaches for SaaS.

Specifically, Table 2 includes the proposed ML algorithm for the reviewed papers
along with the compared methods. Results are split into two categories, indicating the
most commonly used metrics and miscellaneous across the reviewed papers. Additionally,
information about the used datasets and employed validation methods is included.

Table 2. Machine learning methods used for decision support in SaaS (RQ3).

Ref.

Proposed
Method

Compared
Methods

Evaluation Results

Common Metrics

Miscellaneous
Metrics

Validation
Method

Dataset

[18]

Random
Forest

Neural
Networks,
AdaBoost

[24]

Hybrid
Model (LSTM
Hidden State)

Random
Forest, LSTM

Random Forest: 0.997 AUC,
0.988 Accuracy,
0.989 F-measure for
Non-Churn Class and
0.981 for Churn
Neural Networks:
0.968 AUC, 0.965 Accuracy,
0.975 F-measure for
Non-Churn Class and
0.946 for Churn
AdaBoost: 0.995 AUC,
0.984 Accuracy,
0.989 F-measure for
Non-Churn Class and
0.974 for Churn

Hybrid Models: 0.8741 AUC,
0.6953 F1-score,
0.8023 Accuracy
LSTM: 0.8592 AUC,
0.6795 F1-score,
0.7900 Accuracy
Random Forest: 0.8405 AUC,
0.6414 F1-score,
0.7749 Accuracy

[12]

XGBoost

Logistic
Regression,
Random
Forests

XGBoost: 0.7526 AUC
Random Forest: ~0.5 AUC
Logistic Regression:
0.7257 AUC

Training (64%),
validation
(16%), and test
(20%) sets

10-fold cross-
validation

10-fold cross-
validation

Dataset from a
partner company
associated with the
University of
Évora, containing
196,977 instances
corresponding to
26,418 service
subscriptions

Dataset from player
logs of a freemium
mobile game
developed by
Tactile Games
including
2,284,238 records of
814,822 unique
players

Dataset from a
client SaaS
company including
76,668 observations
of 20 predictor
variables

-

-

-

---

<!-- PAGE 15 -->

Appl. Sci. 2025, 15, 6508

15 of 35

Table 2. Cont.

Ref.

Proposed
Method

Compared
Methods

Evaluation Results

Common Metrics

Miscellaneous
Metrics

Validation
Method

Dataset

[14]

Random
Forest

Decision
Trees,
Support
Vector
Machine,
Neural
Networks,
Naïve Bayes,
Logistic
Regression

[22]

XGBoost

Transformer-
based models
(FT-
transformer),
GBDT

[19]

Hybrid
Model (SVM +
Naïve Bayes)

KNN,
Random
Forest, ANN,
Decision tree

Random forest:
0.88 Training Accuracy,
0.87 Test Accuracy
Decision Trees: 1.00
(overfitting) Training
Accuracy, 0.76 Test Accuracy
Support Vector Machine:
1.00 (overfitting) Training
Accuracy, 0.63 Test Accuracy
Neural Networks:
0.85 Training Accuracy,
0.82 Test Accuracy
Naïve Bayes: 0.71 Training
Accuracy, 0.69 Test Accuracy
Logistic Regression:
0.73 Training Accuracy,
0.71 Test Accuracy

XGBoost: 0.948 Accuracy,
0.9545 Precision,
0.9418 Recall,
0.9481 F1-Score, 0.988 AUC
Transformer-based models:
0.8679 Accuracy,
0.8477 Precision,
0.8875 Recall,
0.8671 F1-Score, 0.949 AUC
GBDT: 0.8561 Accuracy,
0.8755 Precision,
0.8328 Recall,
0.8536 F1-Score, 0.934 AUC

Hybrid Model:
0.9567 Accuracy,
0.943 Precision,
0.9565 Recall, 0.943 F1-Score
ANN: 0.789 Accuracy,
0.8403 Precision,
0.8824 Recall,
0.8608 F1-Score
Random Forest:
0.8 Accuracy, 0.79 Precision,
0.80 Recall, 0.79 F1-Score
KNN: 0.839 Accuracy,
0.826 Precision, 0.829 Recall,
0.781 F1-Score
Decision Tree:
0.9097 Accuracy,
0.9242 Precision,
0.9242 Recall,
0.9242 F1-Score

train-test split
(percentage not
mentioned)

A B2B SaaS
subscriptions
dataset (source
not mentioned)
including
7044 examples of
B2B SaaS
subscriptions and
21 variables

train-test split
(percentage not
mentioned)

Dataset from a
mobile freemium
game includes data
from over
268,370 users

train-test split
(80%
train—20% test)

Dataset from
Kaggle containing
subscription details
on 7044 customers
of a fictional
SaaS company

-

-

-

---

<!-- PAGE 16 -->

Appl. Sci. 2025, 15, 6508

16 of 35

Table 2. Cont.

Ref.

Proposed
Method

Compared
Methods

Evaluation Results

Common Metrics

Miscellaneous
Metrics

Validation
Method

Dataset

[13]

Random
Forest

Decision Tree,
Logistic
Regression,
Support
Vector
Machine

Random Forest: 0.916 Recall,
0.926 F1-Score,
0.92 Accuracy,
0.939 Precision
Decision Tree: 0.945 Recall,
0.871 F1-Score,
0.845 Accuracy,
0.809 Precision
Logistic Regression:
0.868 Recall, 0.902 F1-Score,
0.896 Accuracy,
0.939 Precision
Support Vector Machine:
0.881 Recall, 0.839 F1-Score,
0.814 Accuracy,
0.803 Precision

-

train-test split
(80%
train—20%
test), 10-fold
cross validation

Dataset extracted
from the case-study
company’s
database system
containing
1788 observations
of churn and
non-churn samples

[11]

Neural
Networks

-

Neural Networks:
0.9694 Accuracy,
0.9651 Precision,
0.9540 Recall

-

Not provided

Dataset collected
from a cloud
service provider
including
approximately
700 unique
cloud service
offering-customer
pairs and around
90,000 associated
support tickets

[15]

XGBoost

Random
Forest,
Logistic
Regression,
Neural
Networks,
AdaBoost,
Gradient
Boosting
Machine

XGBoost: 0.7956 Accuracy,
0.7916 Precision,
0.8507 Recall,
0.8201 F1-Score,
0.86 ROC AUC
Random Forest:
0.7877 Accuracy,
0.8042 Precision,
0.8096 Recall,
0.8069 F1-Score,
0.85 ROC AUC
Logistic Regression:
0.7757 Accuracy,
0.7986 Precision,
0.7895 Recall,
0.7940 F1-Score,
0.84 ROC AUC
Neural Networks:
0.7835 Accuracy,
0.7910 Precision,
0.8220 Recall,
0.8062 F1-Score,
0.84 ROC AUC
AdaBoost: 0.7867 Accuracy,
0.7970 Precision,
0.8191 Recall,
0.8079 F1-Score,
0.86 ROC AUC

-

train-test split
(80%
train—20% test)

Two datasets
provided by a
Portuguese
software house
with the final
dataset included
9539 observations
from the two
datasets combined

---

<!-- PAGE 17 -->

Appl. Sci. 2025, 15, 6508

17 of 35

Table 2. Cont.

Ref.

Proposed
Method

Compared
Methods

Evaluation Results

Common Metrics

Miscellaneous
Metrics

Validation
Method

Dataset

Gradient Boosting Machine:
0.7935 Accuracy,
0.7946 Precision,
0.8402 Recall,
0.8167 F1-Score,
0.86 ROC AUC

Random Forest:
0.88 Training Accuracy,
0.87 Test Accuracy
Neural Networks:
0.85 Training Accuracy,
0.82 Test Accuracy
Decision Tree: 1.00
(overfitting) Training
Accuracy, 0.76 Test Accuracy
Logistic Regression:
0.73 Training Accuracy,
0.71 Test Accuracy
Support Vector Machine:
1.00 (overfitting) Training
Accuracy, 0.63 Test Accuracy
Naive Bayes: 0.71 Training
Accuracy, 0.69 Test Accuracy

Random Forest: 0.997 AUC
Decision tree: 0.987 AUC
Neural Networks:
0.994 AUC
Gradient Boosting:
0.984 AUC
Logistic Regression:
0.967 AUC
Support Vector Machine:
0.990 AUC
KNN: 0.840 AUC
Naïve Bayes 0.887 AUC

LightGBM: 0.690 AUROC,
~30 min Training Time
Hybrid Models:
0.591 AUROC,
~2 h Training Time

-

-

-

-

Performance
indexed to
LIghtGBM =
1.0×
LightGBM:
1 SMAPE,
1 RMSE,
1 MAE
XGBoost:
~1.10 SMAPE,
~1 RMSE,
~1.1 MAE

[8]

Random
Forest

[23]

Random
Forest

[21]

LightGBM

[38]

LightGBM

Neural
Networks,
Decision
Trees, Logistic
Regression,
Support
Vector
Machine,
Naïve Bayes

Neural
Networks,
Decision
Trees, Logistic
Regression,
Support
Vector
Machine,
Naïve Bayes,
Gradient
Boosting,
KNN

Hybrid
Models
(Neural
Network with
BiLSTM
layers)

XGBoost,
Gradient
boosting,
LASSO
Regression,
K-nearest-
neighbors,
AUTO-Arima

train-test split
(percentage not
mentioned)

User activity
datasets (source
and number of data
not mentioned)

train-test-
validation split
(percentage not
mentioned),
cross validation
(folds not
mentioned)

Dataset from “The
Settlers Online
(TSO)”, a freemium
online strategy
game, including
7439 users and
113,643 observed
events.

train-test split
(500,000
records–
200,000 records)

Dataset from
QuickBooks Online
(QBO) users,
including
700,000 combinations
of users and
reference
timestamps.

Not provided

Dataset collected
from a well-known
B2B SaaS company
(number of data
not mentioned)

---

<!-- PAGE 18 -->

Appl. Sci. 2025, 15, 6508

18 of 35

Table 2. Cont.

Ref.

Proposed
Method

Compared
Methods

Evaluation Results

Common Metrics

Validation
Method

Dataset

Not provided

Dataset from a
U.S.-based
multinational
computer software
company operating
on a Software-as-a-
Service business
model including a
sample of
14,989 unique
consumers

train-test split
(70%
train—30% test)

Dataset from a fully
randomized
experiment
involving
337,724 unconnected
users globally

Miscellaneous
Metrics

Gradient
Boosting:
~1.2 SMAPE,
~1.1 RMSE,
~1.2 MAE
KNN:
~1.25 SMAPE,
~1.2 RMSE,
~1.25 MAE
LASSO
Regression:
~1.25 SMAPE,
~1.1 RMSE,
~1.2 MAE
AUTO-
Arima:
~1.75 SMAPE,
~5 RMSE,
~2.5 MAE

LASSO
Regression
reduced MSE
to 0.122
Dynamic
probit model
with copula
corrections:
−3841
Log-Marginal
Density,
7808.5
Deviance
Information
Criterion

LASSO
Regression:
+6.8%
subscriptions
XGBoost:
+6.17%
subscriptions
Random
Forests: Poor
(overfitted
training data)
Causal
Forests: Poor
(minimal per-
sonalization)

[29]

LASSO
Regression,
Dynamic
probit model
with copula
corrections

-

[30]

LASSO
Regression

Random
Forest, causal
forest,
XGBoost

-

-

---

<!-- PAGE 19 -->

Appl. Sci. 2025, 15, 6508

19 of 35

Table 2. Cont.

Ref.

Proposed
Method

Compared
Methods

Evaluation Results

Common Metrics

[16]

Logistic
Regression

Random
Forest,
XGBoost,
Decision
Trees,
Support
Vector
Machine

Logistic Regression:
0.604 AUC
Support Vector Machine:
0.603 AUC
Random Forest: 0.594 AUC
XGBoost: 0.599 AUC
Decision Tree: 0.523 AUC

Validation
Method

Dataset

cross-
validation
(folds not
mentioned)

Dataset from a
European software
service provider
including
3959 subscriptions

Miscellaneous
Metrics

Logistic
Regression:
1.682 TDL,
21,209 EMPB
(EUR)
Support
Vector
Machine:
1.590 TDL,
22,566 EMPB
(EUR)
Random
Forest:
11.482 TDL,
15,106 EMPB
(EUR)
XGBoost:
1.360 TDL,
14,351 EMPB
(EUR)
Decision Tree:
0.856 TDL,
5809 EMPB
(EUR)

[28]

XGBoost

Random
Forest,
Decision
Trees, Logistic
Regression,
Support
Vector
Machine,
K-nearest-
neighbors,
Naïve Bayes

[17]

Random
Forest

Logistic
Regression

[36]

Random
Forest,
Gradient
Boosting
Machine

Logistic
Regression

XGBoost: 0.79 Accuracy,
0.8 Precision, 0.76 Recall,
0.78 F1-Score
All the other methods where
outperformed but their
specific results were not
provided

Random Forest:
0.09 Precision, 0.11 Recall,
0.10 F1-Score
Logistic Regression:
0.05 Precision, 0.57 Recall,
0.19 F1-Score
The proposed model was
better at explaining churn
drivers (feature importance)
than precise prediction.

Logistic Regression:
1.00 Accuracy,
1.00 Precision, 1.00 Recall
(due to dataset simplicity)
Random Forest:
0.75 Accuracy,
0.714 Precision, 0.789 Recall
Gradient Boosting Machine:
0.77 Accuracy,
0.753 Precision, 0.768 Recall

-

-

-

train-test split
(80%
train—20% test)

Dataset from
Kaggle
(fineTech_appData)
including
50,000 rows of user
information

cross validation
(folds not
mentioned)

Dataset from
Aircall, a Software
as a Service
company including
data from about
5000 customers

train-test split
(80%
train—20% test)

A simulation
dataset replicating
real-world
Software as a
Service (SaaS)
usage patterns
(number of data
not mentioned)

---

<!-- PAGE 20 -->

Appl. Sci. 2025, 15, 6508

20 of 35

Table 2. Cont.

Ref.

Proposed
Method

Compared
Methods

Evaluation Results

Common Metrics

Miscellaneous
Metrics

Validation
Method

Dataset

[32]

Logistic
Regression

-

Logistic Regression:
0.9372 Accuracy,
0.9549 Precision,
0.9330 Recall,
0.9438 F1-Score, 0.999 AUC

-

Not provided

Datasets collected
from four
databases at
Digidata, a SaaS
company where the
project was carried
out (number of
data not
mentioned)

4.4. Form of Outputs Presented to SaaS Providers

Concerning RQ4, researchers chose a wide variety of methods to present their results
to SaaS providers in order to support decision-making. As listed below, the categories of
those methods include:

1.

Visualizations

A significant number of papers utilized visual representations like confusion matrices,
Receiver Operating Characteristic (ROC) curves, feature importance plots, retention curves,
sentiment plots, time-series graphs and process maps. These visuals help non-technical
stakeholders quickly grasp patterns, model strengths, and key insights. They also support
internal presentations and stakeholder alignment around key metrics and strategies. Table 3
presents the visualization techniques deployed by the reviewed approaches.

Table 3. Visualizations for decision-making (RQ4).

Ref.

[14]
[22]
[25]
[13]
[20]
[23]
[21]
[31]
[33]
[34]
[37]
[16]
[35]
[36]

Visualizations

Accuracy curves to show the impact of tree counts in random forests
AUC-ROC curves and confusion matrices to validate robustness
Hazard rate curves and predictive intervals for retention statistics
Feature importance (e.g., prevPeriodTrans) via bar charts
Temporal sentiment plots track satisfaction trajectories
ROC curves and feature plots that highlight “missed days” as top predictors
(BBE-LSWCM) uses decile lift charts to show a 30% churn reduction in A/B tests
Path analysis diagrams to map UI design to loyalty
Time-series graphs to compare adaptive vs. non-adaptive negotiation modes
Process maps that reveal key activation moment
Trajectory plots that show activation impacts
Coefficient plots to illustrate usage data’s impact on churn
Dashboards to automate feedback summaries and issue prioritization
Comparative plots that guide model selection via accuracy/recall metrics

2.

Simulation/What-If Analysis

Simulation tools model hypothetical scenarios (e.g., pricing changes, trial lengths),
enabling SaaS providers to test retention strategies and forecast revenue impact before
implementation, supporting data-driven decision-making. Study [18] enabled “what-
if” scenarios to test the impact of retention strategies like loyalty extensions, helping
providers optimize interventions while the work presented in [25] simulated promotional
campaigns, showing a 20% engagement boost from aggressive incentives, and models
premium purchase values for revenue forecasting. Additionally, work [29] tested timing
strategies, revealing peak conversion windows (e.g., post-trial expiration) and warning

---

<!-- PAGE 21 -->

Appl. Sci. 2025, 15, 6508

21 of 35

against overusing persuasive messaging and study [30] compared trial lengths (7-day vs.
30-day trial) through simulations, finding shorter trials optimal for beginners but longer
trials better for experts. At last, in [26], the authors modeled player retention under quality
adjustments, showing that initial quality investments reduced attrition and study [36]
simulated dynamic pricing strategies, such as outcome-based billing, to align costs with
customer value.

3.

Segmentation and Persona Modeling

Studies [23,28,32,38] used clustering and behavioral analysis to segment users or create
personas. These help SaaS providers tailor features, marketing, and support strategies
to distinct user groups for better engagement. Table 4 includes the segmentation groups
used in those studies. Authors in [25] categorized users based on demographics and
engagement levels, in the study [23] the authors chose to categorize their users by their
activity patterns while [38] chose to group users by CLV. Additionally, the work in [27]
created B2B user personas while in [28] the authors created behavioral clusters. Finally, the
study [32] segmented users by relationship length and cross-selling dependency.

Table 4. Segmentation and persona modeling (RQ4).

Segmentation Groups

Description

Ref.

[25]

Demographics (gender, geography) and
engagement levels

[23]

Activity patterns (e.g., “economy overview usage”)

[38]

[27]

[28]

[32]

Customer Lifetime Value (CLV)

B2B user personas (e.g., “Data Sellers”)

Behavioral clusters (e.g., education-focused users)

Relationship length and cross-selling dependency

Groups people according to demographics and
engagement levels
Classifies players by activity patterns, using loyalty
markers to target interventions
Segments customers by CLV, focusing on prioritizing
enterprise clients for retention
Creates user personas with pain points and workflow
metrics to guide product development
Identifies behavioral clusters, such as
education-focused users, for targeted marketing
Segments by relationship length

4.

Business Impact Metrics

Metrics like CLV, MRR and ROI can be used to quantify churn effects. This en-
ables providers to understand the financial implications of retention efforts and prioritize
high-value customer segments. For instance, study [18] reported cost savings per re-
tained customer and revenue protection through churn reduction, while the work in [14]
demonstrated ROI improvements via dynamic pricing strategies. Early churn detection
and associated acquisition cost reductions were highlighted in study [19] and study [25]
showcased a revenue boost from collaboration-driven monetization models. Furthermore,
studies such as [8,21] focused on reducing negative MRR churn and increasing intervention
acceptance through A/B testing, respectively. The prediction of CLV and the application
of marginal ROI formulas were addressed in the work [38], whereas the study [30] illus-
trated how optimized free trial strategies could enhance both retention and revenue. In
addition, study [26] linked quality investment costs to gains in network-driven retention,
and study [16] evaluated predictive accuracy in relation to carbon emissions. Studies
like [36] connected usage-based billing models to a marked increase in customer satisfac-
tion, while [32] quantified retention differences across countries, providing further insights
into localization strategies. Table 5 summarizes the business metrics employed by the
reviewed approaches.

---

<!-- PAGE 22 -->

Appl. Sci. 2025, 15, 6508

22 of 35

Table 5. Business impact metrics (RQ4).

Ref.

[18]
[14]
[19]
[25]
[8]
[21]
[38]
[30]
[26]
[16]
[36]
[32]

Business Metrics

Cost savings per retained customer, revenue protection from churn reduction
Dynamic pricing ROI
Churn rates from early detection, acquisition cost reduction
Revenue boost from collaboration-based monetization
Negative MRR churn and CLV
Churn reduction and intervention acceptance in A/B tests.
Marginal ROI formulas
Improved retention and revenue
Quality investment costs against network-driven retention gains.
Predictive accuracy against carbon emissions
Customer satisfaction
Country-specific retention differences

5. Model Deployment and Integration

Model deployment integrates predictive models into SaaS platforms via APIs or
cloud pipelines, enabling automated churn prediction and alignment with CRM features.
Building on this, CRM and marketing tools use these insights to personalize campaigns
based on churn risk or user behavior. Additionally, toolkits and interactive systems sup-
port scenario testing and onboarding analysis, helping teams refine strategies and make
data-driven decisions.

For instance, the work in [30] integrated RESTful APIs and the CBAR platform to
deliver JSON-formatted real-time risk scores, enhancing both the speed and accuracy of
predictions. Centralized Bank Account Register (CBAR) not only ranked subscriptions
by risk and value but also enabled targeted actions based on live insights. Similarly,
study [12] proposed a standalone app that supported dynamic thresholding and feedback
loops, allowing continuous model refinement, and introduced a tool offering live churn
predictions for real-time decision-making. This study also highlighted declining login
activity as an early warning sign and recommends dynamic threshold adjustment based on
marketing capacity.

Several other studies proposed additional enhancements. As shown in [21] an AWS
SageMaker pipeline was utilized to support both batch and real-time featurization, enabling
flexible data processing, and triggered chat pop-ups for high-risk users to foster imme-
diate engagement. Study [16] recommended leveraging cloud storage and algorithmic
optimizations to reduce environmental impact, while work [36] provided pseudocode for
integrating real-time data streams with billing systems.

Moreover, the work in [24] aligned predictive models with targeted re-engagement
strategies for at-risk users, while [19] fine-tuned retention campaigns by balancing preci-
sion and recall, and designed hybrid models to ensure scalability for cloud deployment.
Study [29] optimized conversion rates through strategic ad placements and precise timing
of messaging. Study [17] ensured that key feature usage data is synced with CRM systems
and flags low-usage accounts for proactive customer success outreach.

Dashboards and interactive systems also play a critical supporting role. Study [15] pre-
sented a dashboard that visualizes churn risk metrics and integrates real-time alerts directly
into CRM dashboards, ensuring that teams can act swiftly on critical issues. Study [15]
offered a process mining toolkit that uncovers “Aha!” moments during onboarding, en-
hancing user activation efforts. Finally, authors in [35] proposed an automated feedback
system that prioritizes critical user issues and provides dashboards that visualize feedback
trends, helping teams monitor user sentiment and behavior patterns over time.

---

<!-- PAGE 23 -->

Appl. Sci. 2025, 15, 6508

23 of 35

5. Discussion

In response to RQ1, the analysis revealed that churn prediction is the most frequently
pursued objective in decision support systems in SaaS settings. Studies consistently empha-
sized the importance of identifying early at-risk users in order to interfere with data-driven
strategies, therefore improving subscription continuance and reducing revenue loss. Be-
yond churn, researchers also contributed significantly through user segmentation, which
enables the grouping of customers into meaningful behavioral or demographic clusters.
This supports personalized product development, targeted marketing, and more responsive
customer service. Other studies focused on improving user engagement and predicting
CLV, which are key indicators for long-term business sustainability. Additionally, strategic
decisions around pricing optimization, free trial policies, and onboarding practices were
offered so that SaaS providers are aided in aligning service design with actual user behavior
and expectations.

Regarding RQ2, this survey revealed that for the effectiveness of decision-making
in SaaS environments, diverse and rich datasets must be used. In most studies, behav-
ioral data, such as clickstream logs, feature usage, and session frequency, emerged as
foundational. These were often combined with transactional and subscription-related
information, including billing history and account tenure, to provide a fuller picture of
user engagement. Studies also made use of demographic and firmographic characteristics,
allowing for segmentation by industry, company size, or geographic location. In some cases,
sentiment data from support tickets or survey responses were incorporated to capture
users’ subjective experiences. A few studies employed synthetic or simulated data to test
hypothetical scenarios and optimize intervention strategies before deployment. Altogether,
the results underscore the importance of integrating both quantitative system usage metrics
and qualitative feedback for comprehensive decision support.

Addressing RQ3, it was found that machine learning techniques play a central role in
nearly all the examined implementations. RF and XGBoost were the most commonly used
algorithms, and they consistently delivered strong performance across various evaluation
metrics such as AUC, precision, recall, and F1-score. These models were particularly
effective in handling high-dimensional, tabular datasets and offered a balance of accuracy
and interpretability. In more complex scenarios requiring temporal modeling or behavioral
pattern recognition, hybrid and ensemble models outperformed traditional classifiers.
For example, combinations of LSTM networks with LightGBM or structured metadata
inputs captured sequential user behavior more effectively than static models alone. While
simpler models like LR and DT provided useful baselines, their performance was often
eclipsed by ensemble or deep learning approaches. Notably, some studies considered the
environmental impact and scalability of different algorithms, highlighting the relevance
of computational efficiency and carbon footprint in model selection. Overall, the choice
of method was shown to depend on specific task requirements, data characteristics, and
operational constraints such as latency or model transparency.

Finally, in response to RQ4, a wide variety of output types were presented to inform
and guide SaaS providers. The importance of visual analytics was highlighted, including
ROC curves, feature importance rankings, and user behavior maps, which helped non-
technical stakeholders interpret model outcomes. Business-oriented metrics such as CLV,
MRR, and ROI linked predictions to financial outcomes while simulation tools allowed
providers to experiment with trial durations or pricing adjustments before actual imple-
mentation, enhancing the strategic value of the DSSs. Furthermore, user segmentation
and persona modeling enabled more detailed targeting of user engagement and marketing
strategies, while process mining techniques uncovered critical activation patterns such as
the discovery of an “aha moment”.

---

<!-- PAGE 24 -->

Appl. Sci. 2025, 15, 6508

24 of 35

Some studies also focused on model deployment strategies, emphasizing cloud inte-
gration and scalability. By bridging predictive analytics with tangible business insights and
strategic tools, DSS outputs were shown to have a direct impact on operational efficiency,
customer satisfaction, and long-term profitability. Moreover, deploying such models as
churn prediction ones through the cloud offers the possibility of providing Machine Learn-
ing as Service (MLaaS) models specialized for supporting decision-making in SaaS. On
the same page, research [54] presented an MLaaS solution for marketing that contained a
churn prediction model tested in retail and e-commerce settings.

To synthesize the findings discussed in this review and provide a clearer understand-
ing of the research landscape, Table 6 presents the main insights and findings corresponding
to each research question (RQ1–RQ4) addressed in this study. Table 6 offers a compact
overview of the focus areas, types of data used, applied machine learning methods, and
the nature of decision support outputs in SaaS environments.

Table 6. Cumulative table, findings of RQ1–RQ4.

Ref.

Focus

Data

Proposed Method

Output

[18]

Churn prediction

Usage behavior, customer
profile, financial

Random Forest

Simulation/What-If
Analysis, Business Impact
Metrics, Model
Deployment and
Integration

[24]

Churn prediction

Usage behavior

Hybrid Model
(LSTM Hidden State)

Model Deployment
and Integration

[12]

Churn prediction

[14]

Churn prediction

Usage behavior,
customer profile,
transactional/business
metrics

Usage behavior,
transactional/business
metrics

XGBoost

Model Deployment
and Integration

Random Forest

Visualizations, Business
Impact Metrics

[22]

Churn prediction

Usage behavior

XGBoost

Visualizations

[19]

Churn prediction

Usage behavior,
customer profile

Hybrid Model (SVM
+ Naïve Bayes)

[25]

Churn prediction

Usage behavior,
customer profile

Cox Regression

Business Impact Metrics,
Model Deployment
and Integration

Visualizations,
Simulation/What-If
Analysis, Segmentation
and Persona Modeling,
Business Impact Metrics

[13]

Churn prediction

Usage behavior,
customer profile,
transactional/business
metrics

Decision Trees

Visualizations

Churn prediction

Customer support

Neural Networks

Visualizations

[20]

[15]

Churn prediction

[8]

Churn prediction

Usage behavior, customer
profile, customer support

Usage behavior,
transactional/business
metrics, customer profile

XGBoost

Model Deployment
and Integration

Neural Networks

Business Impact Metrics

---

<!-- PAGE 25 -->

Appl. Sci. 2025, 15, 6508

25 of 35

Table 6. Cont.

Ref.

Focus

Data

Proposed Method

Output

[23]

Churn prediction

Usage behavior

Random Forest

[21]

Churn prediction

Usage Behavior,
customer profile

LightGBM

[16]

Churn prediction

[17]

Churn prediction

[38]

Customer lifetime
value

Usage behavior,
transactional/business
metrics, customer profile,
customer support

Usage behavior,
transactional/business
metrics, customer
profile, satisfaction

Usage behavior,
transactional/business
metrics, customer
profile, financial

Logistic Regression

Random Forest

Model Deployment
and Integration

LightGBM

[36]

Customer lifetime
value

Transactional/business
metrics, financial

Random Forest

[29]

User engagement

marketing/trials

LASSO Regression

[34]

User engagement

Usage behavior

Heuristic and
Fuzzy Mining

[30]

User retention

Usage behavior,
survey/interview, marketing

LASSO Regression

[26]

User retention

Customer profile, satisfaction

Reinforcement
learning

[37]

User retention

[31]

[33]

User
satisfaction/user
loyalty

User
satisfaction/user
loyalty

Usage behavior, customer
profile, survey/interview

Usage behavior, customer
profile, survey/interview

Usage behavior, satisfaction

Linear Mixed Models

Visualizations

PLS-SEM (Partial
Least Squares
Structural Equation
Modeling)

AQUAman
negotiation
mechanism

Visualizations

Visualizations

Visualizations,
Segmentation and
Persona Modeling

Visualizations, Business
Impact Metrics, Model
Deployment and
Integration

Visualizations, Business
Impact Metrics, Model
Deployment and
Integration

Segmentation and
Persona Modeling,
Business Impact Metrics

Visualizations,
Simulation/What-If
Analysis, Business Impact
Metrics, Model
Deployment and
Integration

Simulation/What-If
Analysis, Model
Deployment and
Integration

Visualizations, Model
Deployment and
Integration

Simulation/What-If
Analysis, Business
Impact Metrics

Simulation/What-If
Analysis, Business
Impact Metrics

---

<!-- PAGE 26 -->

Appl. Sci. 2025, 15, 6508

26 of 35

Table 6. Cont.

Focus

Data

Proposed Method

Output

Ref.

[35]

[32]

User
satisfaction/user
loyalty

User
satisfaction/user
loyalty

[27]

User segmentation

[28]

User segmentation

Usage behavior, customer
support, satisfaction,
survey/interview

Comparative
analysis

Usage behavior,
transactional/business
metrics, marketing

Usage behavior,
survey/interview

Usage behavior,
transactional/business
metrics

Logistic Regression

UMAP and
HDBSCAN

XGBoost

Visualizations, Model
Deployment and
Integration

Segmentation and
Persona Modeling,
Business Impact Metrics

Segmentation and
Persona Modeling

Segmentation and
Persona Modeling

5.1. Insights and Strategic Recommendations

From many of the reviewed systems derived various actionable predictions and
recommendations, such as identifying customers at high risk of churning, estimating
potential revenue loss, or advising on optimal pricing strategies. One of the most consistent
themes across research was the use of machine learning to flag customers likely to churn.
Studies such as [14] concluded that newer B2B customers are particularly vulnerable to
churn, while those with low monthly payments often exhibit higher loyalty, suggesting
that random forests are well-suited for B2B SaaS due to their interpretability and scalability.
Pricing strategies also play a pivotal role in user retention. For instance, research [36]
concluded that a significant percentage of users prefer transparent billing and proposed a
dynamic pricing formula that factors in base rates, usage metrics, and risk adjustments. The
study recommended gradient boosting for complex pricing environments where traditional
models may fall short. Additionally, research [32] revealed that multi-product subscrip-
tions improved retention but cautioned against over-reliance on bundling, noting regional
variations in loyalty. Further supporting pricing adjustments, research [8] identified that
high fees combined with low session activity strongly correlate with churn, suggesting that
SaaS providers should consider flexible pricing for low-engagement users.

Additionally, other researchers proposed best-practice policies, like trial durations,
onboarding flows, and pricing tactics, to help SaaS providers align product decisions with
user behavior and retention trends. Study [30] recommended defaulting to 7-day trials
unless segmentation suggests longer ones, while authors of [31] highlighted that intuitive
UI design can boost satisfaction and increase loyalty by 41%. Additionally, work [26]
advised gradual quality adjustments to better match user perceptions, and work [33] set
performance benchmarks such as 90% acceptability rates in negotiation systems. Onboard-
ing strategies, according to [34], should center around key activation points, while the
work presented in [37] encouraged CRM-style engagement, including intranet banners, to
maintain user involvement.

In [22] the authors demonstrated that early onboarding metrics are strong predictors
of long-term retention. The study achieved an 88.75% recall rate in predicting post-tutorial
churn, underscoring the importance of monitoring early user behavior. Similarly, the work
presented in [20] linked negative sentiment in support tickets to churn, advocating for
sentiment analysis alongside usage logs to create a risk assessment framework. In another
study [19], the authors found that low API or integration usage and infrequent support
interactions are reliable churn signals, making these metrics essential for prioritizing
retention efforts.

---

<!-- PAGE 27 -->

Appl. Sci. 2025, 15, 6508

27 of 35

Other research [13,23] highlighted that selecting the right machine learning model
is crucial for effective churn prediction highlighting the trade-offs between different ap-
proaches. For example, the authors in [13] compared decision trees and random forests,
finding that decision trees excel in recall, making them ideal for minimizing missed churn
risks, while random forests offer better F1-scores, which may be preferable when balancing
precision and recall. Meanwhile, research [23] achieved near-perfect predictive perfor-
mance with an AUC of approximately 0.99 but warned against neural networks due to
their tendency to degrade over time without frequent retraining. On the operational side,
authors in [16] highlighted the computational cost of XGBoost, noting that it produces
335% higher emissions than logistic regression, and recommended cloud-based solutions
for scalability and efficiency.

Measuring the financial impact of churn ensures that retention efforts align with
business objectives. The work presented in [38] demonstrated how CLV predictions can
optimize budget allocation, ensuring marketing spending targets high-value users. Another
key insight comes from [29], which found that organic search ads outperformed email
campaigns in driving conversions, cautioning against overly aggressive retention tactics
that may alienate users.

Finally, the importance of addressing computational demands and sustainability in
SaaS systems was highlighted by studies [14,16,19,36]. Key recommendations included
optimizing models for cloud deployment, minimizing carbon footprints, and ensuring
scalable infrastructure for real-time, high-volume applications. For instance, study [14]
pointed out the significant computational requirements of deep learning models, particu-
larly for large firms. In addition, the authors in [19] focused on designing models suited for
cloud-based SaaS environments, while in study [16] the authors evaluated the environmen-
tal impact, specifically the carbon cost, of model training. To support scalability, authors
in [36] recommended hybrid computing approaches, especially for high-demand systems
like billing.

5.2. Selection of Optimal Machine Learning Model for Decision-Making

Selecting the optimal machine learning model depends on the specific use case. The
initial decision for a SaaS provider is to determine the primary business objective driving
the need for machine learning. If the goal is the churn prediction, which is the most
frequently cited use case, the provider should assess whether their dataset consists primarily
of structured behavioral and transactional data. If the data is rich in clickstream logs,
user sessions, or subscription data, ensemble models such as Random Forest or XGBoost
stand out due to their strong performance in predictive accuracy and feature importance
insights. These models are particularly effective when interpretability and scalability are
important, especially in Business-to-Business (B2B) contexts where clear justification for
churn predictions is essential.

However, in use cases where user behavior evolves over time, for instance, in freemium
games or SaaS products with high session variability [23], hybrid architectures that integrate
static and time-dependent features into LSTM networks (such as subscription age or
payment history) should be considered. These models better capture temporal dynamics
and early disengagement signals but at the cost of increased complexity and training
resources. For SaaS vendors requiring real-time deployment or low-latency predictions,
LightGBM offers a compelling balance between performance and computational efficiency
and is especially suitable for streaming contexts or integration into cloud-based platforms.
For use cases focusing on user segmentation, where the goal is to group users into
interpretable personas or strategic marketing groups, the nature of the input data plays
a pivotal role. If the data includes demographic, firmographic, and behavioral attributes,

---

<!-- PAGE 28 -->

Appl. Sci. 2025, 15, 6508

28 of 35

then traditional clustering methods like K-means are preferred for identifying meaningful
segments, especially when enhanced with dimensionality reduction techniques such as
UMAP or HDBSCAN to handle sparse datasets [26]. These approaches support exploratory
analysis and are valuable when strategic alignment with qualitative insights from surveys
or interviews is required.

For predicting CLV in B2B environments, where historical billing data, engagement
metrics, and firmographic features such as company size or industry play a critical role,
hierarchical ensemble models such as LightGBM were particularly effective. These models
deliver strong predictive accuracy and can be paired with time-series techniques like Auto
ARIMA to capture revenue trends across different customer segments [37]. Additionally,
LASSO regression was applied in this context to enhance model interpretability and stability
by selecting key predictive features in high-dimensional datasets. This approach allows
SaaS providers to identify and prioritize high-value accounts, allocate marketing resources
more efficiently, and optimize long-term revenue strategies.

If the focus is on user engagement, satisfaction, or loyalty, the decision is again based
on the type of available data. For use cases involving UI/UX feedback, support ticket
sentiment, or onboarding flows, vendors should consider deep learning models (like MLP
or sentiment-enhanced LSTM) only if they have large datasets and need to identify subtle
trends. For smaller datasets or when model explainability is prioritized, logistic regression
or PLS-SEM models provide interpretable insights and can be used to connect interface
design or feature adoption to engagement metrics.

When the business objective revolves around dynamic pricing or trial optimization,
where scenario testing and profitability forecasting are key, models must support what-if
simulations and business impact metrics. In these cases, gradient boosting techniques
(XGBoost, GBM), or LASSO regression are optimal due to their ability to model nonlinear
relationships and provide stable coefficients for strategic levers like trial duration or usage-
based pricing. SaaS platforms featuring dynamic pricing models may also benefit from
reinforcement learning to adjust prices in response to user behavior and network effects
over time.

Finally, for the choice of the appropriate machine learning model, deployment and
sustainability constraints should be considered. For SaaS vendors with limited engineering
capacity or requiring real-time predictions integrated into CRM systems, models like
Random Forest, XGBoost, or LightGBM can be deployed via REST APIs or embedded in
cloud ML pipelines (as in AWS SageMaker). Additionally, in energy-sensitive environments,
vendors should prefer computationally lightweight models and monitor carbon emissions,
as studies showed large environmental variances between architectures.

Although the primary focus of the reviewed papers was on the performance and
utility of data-driven decision support systems in SaaS, interpretability was also a key
consideration in several of the examined studies. For instance, paper [15] employed Logistic
Regression, a model valued for its transparency, and visualized its coefficients to help
stakeholders understand how different usage factors affect churn predictions. Likewise,
the paper [16] emphasized explainability by analyzing feature importance in Random
Forest and Logistic Regression models to reveal key churn drivers, even when predictive
performance was modest. Other studies such as [12,13,22] also used interpretable models
(such as Decision Trees) or feature importance plots to support decision-making with
understandable insights.

Figure 4 illustrates the recommended actions for selecting the optimal ML model based

on the specific use case and context as derived from the results of the reviewed papers.

---

<!-- PAGE 29 -->

Appl. Sci. 2025, 15, 6508

29 of 35

Figure 4. Taxonomy for ML algorithms selection for SaaS providers.

However, explainability techniques such as SHAP (SHapley Additive exPlana-
tions) [55] or LIME (Local Interpretable Model-agnostic Explanations) [56] were not em-
ployed by the reviewed papers. SHAP is a method used to explain the output of any
machine learning model by quantifying the contribution of each input feature to a specific
prediction. It utilizes the concept of Shapley values from game theory to determine the
importance of each feature. LIME is an interpretation technique used to explain the predic-
tions of any black box machine learning model. LIME approximates a complex model’s
prediction with a simpler, interpretable model, focusing on individual predictions rather
than the model as a whole. The choice between SHAP and LIME depends on the specific
needs of the task. SHAP is ideal when accuracy, consistency, and fairness are priorities,
especially in regulated settings or with tree-based models like XGBoost. LIME, on the
other hand, is useful for quick, model-agnostic explanations during development, and
works well with various data types. Its simplicity makes it great for explaining results
to non-technical users. Ultimately, the adoption of such techniques could significantly
improve stakeholder confidence in automated decisions and support error diagnosis, bias
detection, and regulatory compliance.

Moreover, explicit considerations of algorithmic fairness, privacy protection, or ethical
implications seem to be largely absent. Future research should address those gaps by
incorporating such explainability techniques into machine learning models and consider
the incorporation of privacy-preserving techniques such as differential privacy [57], feder-
ated learning [58] and secure multi-party computation, which can enable model training
on sensitive user data without compromising user confidentiality. Additionally, incor-
porating algorithmic fairness assessments into the development pipeline could prevent
discriminatory outcomes such as biased churn predictions. As SaaS solutions increasingly
influence strategic decisions like marketing, pricing, or retention investments, it is critical
to ensure that automated recommendations do not reinforce inequalities or introduce
unfair treatment.

Even though carbon footprint should be taken into consideration, only two stud-
ies [13,15] measured how machine learning model selection affects carbon emissions.
Study [15] examined the environmental impact of machine learning in B2B churn predic-

---

<!-- PAGE 30 -->

Appl. Sci. 2025, 15, 6508

30 of 35

tion, analyzing the trade-offs between model accuracy and carbon emissions. Using an
AMD EPYC 7763 processor (280 W) and European emissions data (296.96 g CO2/kWh),
the research quantified CO2eq emissions in relatable terms. The results revealed that even
basic preprocessing, such as feature creation, emits 86.379 g CO2eq, while model training
introduced far greater costs. The inclusion of multiple usage features resulting in a high
dimensional dataset, significantly affected the carbon footprint produced by the reviewed
machine learning methods. Specifically, Decision Trees and Random Forests showed a
~200% rise in emissions (DT: 2.349 g CO2eq to 4.044 g; RF: 1.350 g to 4.044 g). XGBoost’s
emissions rose by 335% (21.29 g CO2eq), and SVM increased by 50% (40.99 g CO2eq),
whereas Logistic Regression remained efficient (2.349 g CO2eq).

However, the most striking environmental costs seemed to derive from deep learn-
ing and complex ensemble methods. In study [13], a Deep Neural Network (DNN) with
two hidden layers (32/64 neurons) achieved a high accuracy percentage but at a high
computational expense, scaling considerably as model complexion increased. Similarly,
Random Forest proved resource-intensive, with costs growing alongside tree depth and
feature complexity. Both DNN and RF required parallel computation to train efficiently
and used up all of the available processors indicating their high resource consumption in
comparison with the rest of the reviewed models. Although advanced models seemed to
improve prediction, their energy demands make them unsustainable for firms without op-
timized infrastructure. The study concluded that businesses, especially smaller enterprises,
should prioritize energy-efficient algorithms (like Logistic Regression) or cloud-based
solutions to reduce environmental impact.

Although several of the reviewed studies experimented with deployment aspects,
such as standalone real-time applications [5], CRM-integrated dashboards for decision sup-
port [14], cloud-based prediction APIs [29], and real-time data streaming using platforms
like AWS SageMaker [20], these efforts primarily emphasize centralized, cloud-centric
architectures. An emerging direction for real-world deployment of decision support sys-
tems in SaaS would involve combining centralized model training with decentralized
inference through edge computing [59], particularly in settings involving IoT devices or
local clients. Following this, machine learning models are trained in the cloud, often via
MLaaS platforms that provide scalable computing resources, versioning and monitoring,
and then deployed to edge devices for local inference. This approach could potentially offer
key benefits such as reduced latency, improved bandwidth efficiency, offline functionality,
and enhanced privacy, as predictions can be made without transmitting sensitive data back
to the cloud.

6. Conclusions and Future Work

This work provided a scoping review of data-driven decision support systems (DSSs)
within SaaS environments, highlighting current advances, practices, and gaps. Through
an extensive analysis of recent literature, it has become clear that early churn prediction,
customer segmentation, and personalized engagement strategies are critical for sustaining
growth and profitability in SaaS businesses. Churn reduction emerges as the predominant
research objective, with studies focusing on the identification of at-risk users and proposing
targeted, data-driven interventions. From a methodological perspective, it was found
that Random Forest and XGBoost algorithms consistently outperformed other machine
learning models in churn prediction tasks, particularly when dealing with tabular behav-
ioral and transactional data. Additionally, hybrid models combining static and sequential
features have shown superior predictive performance, suggesting that integrating diverse
data sources can enhance model robustness. However, simpler models like Logistic Re-

---

<!-- PAGE 31 -->

Appl. Sci. 2025, 15, 6508

31 of 35

gression remain valuable for their interpretability, particularly in resource-constrained or
real-time applications.

Beyond predictive modeling, research emphasized the importance of user segmenta-
tion and persona modeling for creating personalized engagement strategies. Key drivers of
long-term retention identified across studies include UI/UX quality, effective onboarding
(such as “aha moments”), flexible pricing strategies, and proactive support interventions.
Moreover, linking predictive outputs to business impact metrics such as CLV, Monthly
Recurring Revenue (MRR), and retention-related ROI have proven essential for bridging
analytics with executive decision-making.

In terms of practical applications, many studies advocated for real-time deployment
of predictive models through CRM integrations, APIs, and dashboard visualizations. This
operationalization ensures that insights lead to immediate actions, supporting dynamic
marketing, retention, and customer success initiatives. Moreover, choosing the right
machine learning model for a SaaS provider depends on the business goal and data type.
For churn prediction, ensemble models like Random Forest and XGBoost are ideal for
structured behavioral data, offering accuracy and interpretability. When user behavior
changes over time, LSTM-based models are better suited, though more complex. For
real-time use, LightGBM balances speed and performance. In user segmentation use cases,
models like K-means work well when combined with dimensionality reduction techniques,
especially with diverse user data. For CLV predictions, LightGBM and LASSO regression
provide accurate and interpretable insights, particularly when paired with time-series
models. Regarding user engagement and satisfaction analysis, deep learning models are
useful for large datasets, while logistic regression or PLS-SEM offer clarity with smaller
ones. In dynamic pricing, XGBoost or reinforcement learning supports strategy testing
and adaptive pricing. Finally, deployment requirements and energy efficiency are critical
considerations. Models such as LightGBM, XGBoost, and Random Forest are not only
known for their strong performance but are also relatively straightforward to deploy via
REST APIs or integrate into cloud-based machine learning pipelines. However, in resource-
constrained or energy-sensitive settings, where computational load and sustainability are
priorities, lighter-weight models, such as logistic regression or decision trees should be
prioritized to reduce infrastructure costs and minimize environmental impact without
sacrificing essential performance.

However, despite the considerable progress in research, several challenges and open
research directions persist. Machine learning models may exhibit performance degradation
over time or struggle to adapt to evolving user behavior, highlighting the need for dynamic
model monitoring and continual learning mechanisms. In order to ensure that developed
DSSs remain effective, monitoring mechanisms should be established. Ensuring training
data is up to date and machine learning models maintain good accuracy levels is crucial.
Batch training of machine learning models may be a good starting point but will not be
sustainable in the long term as data volume increases. To this end, periodically batch
training of the models and/or real-time training incrementally updating the models could
be explored in order to ensure data integrity. Therefore, MLaaS solutions [60] specifically
designed for supporting decision-making in SaaS are of great importance since they can
provide monitoring and updating mechanisms ready to use assuring the efficiency of DSSs.
Meanwhile, the environmental impact of machine learning implementations emerged
as another critical consideration. Comparative analysis revealed that complex ensemble
methods and deep neural networks can incur higher computational costs and carbon emis-
sions than simpler model alternatives, underscoring the importance of balancing predictive
performance with sustainability, particularly for SaaS companies managing significant
computational workloads. Future research, except for seeking greener architectures, could

---

<!-- PAGE 32 -->

Appl. Sci. 2025, 15, 6508

32 of 35

also emphasize clearly explaining the trade-offs between accuracy metrics and environ-
mental footprint. Informing users of energy consumption and carbon emissions can create
awareness and lead to more environmentally friendly model selection decisions like smaller
architectures and the use of techniques like early stopping and transfer learning.

As decision-making increasingly relies on automated systems, ensuring the explain-
ability, fairness, and transparency of predictions, particularly in churn risk assessments,
will be critical. SaaS vendors need to have a clear view of what is happening in their
business at any time and act towards improving user experience and ultimately increas-
ing KPIs that are vital for their business. Therefore, it’s important that DSSs justify their
recommended decisions and provide clear guidance on what actions should be taken. To-
wards this direction, DSSs can utilize interpretable machine learning models to justify their
decision-making processes. Post hoc methods for non-interpretable models such as SHAP
values [55] and LIME [56] can be used to provide explanations on models’ predictions
allowing vendors to understand what influences the decisions. While both SHAP and
LIME offer valuable insights, they serve distinct purposes. For SaaS providers, SHAP may
be preferable for strategic decision-making and bias detection, while LIME could better
support customer-facing teams needing immediate, case-specific explanations.

Natural language UI could also be explored to provide an easier and friendlier way to
provide guidance to SaaS vendors. Large Language Models (LLMs) could be employed
to understand user’s intent and explain recommended actions, for example for reducing
churn or increasing user engagement. Complicated tools and UIs are not the best choice for
supporting SaaS professionals. They need to stay ahead of the competition and act fast and
efficiently. Providing clear explanations in natural language and suggesting a set of actions
to perform could adjust better to busy schedules and offer clarity.

Additionally, future systems may benefit from refined personalization strategies driven
by context-aware recommendations, dynamically adapting to each user’s lifecycle stage and
dynamic profile. In particular, the DSSs would recommend a personalized course of actions
tailored to each user’s holistic profile which will be dynamically updated. Ultimately, the
development of intelligent, adaptive, and sustainable decision support systems will be a
key differentiator for SaaS providers seeking to build resilient, customer-centric businesses
in an increasingly competitive and dynamic marketplace.

Author Contributions: Conceptualization, E.M.; methodology, E.M.; formal analysis, E.M. and G.C.;
investigation, G.C.; resources, G.C.; data curation, E.M. and G.C.; writing—original draft preparation,
E.M. and G.C.; writing—review and editing, E.V., T.K. and G.A.P.; visualization, E.M.; supervision,
G.A.P. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Conflicts of Interest: The authors declare no conflicts of interest.

References

1.

Bokhari, M.U.; Shallal, Q.M.; Tamandani, Y.K. Cloud Computing Service Models: A Comparative Study. In Proceedings of
the 2016 3rd International Conference on Computing for Sustainable Global Development (INDIACom), New Delhi, India,
16–18 March 2016; pp. 890–895.

2. Mohammed, C.M.; Zeebaree, S.R.M. Sufficient Comparison Among Cloud Computing Services: IaaS, PaaS, and SaaS: A Review.

Int. J. Sci. Bus. 2021, 5, 17–30.
Cusumano, M. Cloud Computing and SaaS as New Computing Platforms. Commun. ACM 2010, 53, 27–29. [CrossRef]
Kumar, K.V.K.M. Software as a service for efficient cloud computing. Int. J. Res. Eng. Technol. 2014, 3, 178–181. [CrossRef]
Tsai, W.; Bai, X.; Huang, Y. Software-as-a-Service (SaaS): Perspectives and Challenges. Sci. China Inf. Sci. 2014, 57, 1–15. [CrossRef]
Berger, P.D.; Nasr, N.I. Customer Lifetime Value: Marketing Models and Applications. J. Interact. Mark. 1998, 12, 17–30. [CrossRef]

3.
4.
5.
6.

---

<!-- PAGE 33 -->

Appl. Sci. 2025, 15, 6508

33 of 35

7. Wang, R.; Ying, S.; Jia, X. Log Data Modeling and Acquisition in Supporting SaaS Software Performance Issue Diagnosis. Int. J.

Softw. Eng. Knowl. Eng. 2019, 29, 1245–1277. [CrossRef]

8. Morozov, V.; Mezentseva, O.; Kolomiiets, A.; Proskurin, M. Predicting Customer Churn Using Machine Learning in IT Startups.
In Lecture Notes in Computational Intelligence and Decision Making, 2021 International Scientific Conference “Intellectual Systems of
Decision-making and Problems of Computational Intelligence”; Springer: Berlin/Heidelberg, Germany, 2022; pp. 645–664.

9. Manzoor, A.; Atif Qureshi, M.; Kidney, E.; Longo, L. A Review on Machine Learning Methods for Customer Churn Prediction

and Recommendations for Business Practitioners. IEEE Access 2024, 12, 70434–70463. [CrossRef]

10. Heilig, L.; Voß, S. Decision Analytics for Cloud Computing: A Classification and Literature Review. In Bridging Data and Decisions;

INFORMS: Catonsville, MD, USA, 2014; pp. 1–26. [CrossRef]

11. Arora, S.; Thota, S.R.; Gupta, S. Artificial Intelligence-Driven Big Data Analytics for Business Intelligence in SaaS Products. In
Proceedings of the 2024 First International Conference on Pioneering Developments in Computer Science & Digital Technologies
(IC2SDT), Delhi, India, 2–4 August 2024; IEEE: New York, NY, USA, 2024; pp. 164–169.

12. Ge, Y.; He, S.; Xiong, J.; Brown, D.E. Customer Churn Analysis for a Software-as-a-Service Company. In Proceedings of the 2017
Systems and Information Engineering Design Symposium (SIEDS), Charlottesville, VA, USA, 28 April 2017; IEEE: New York, NY,
USA, 2017; pp. 106–111.

13. Phumchusri, N.; Amornvetchayakul, P. Machine Learning Models for Predicting Customer Churn: A Case Study in a Software-

as-a-Service Inventory Management Company. Int. J. Bus. Intell. Data Min. 2024, 24, 74–106. [CrossRef]

14. Mezentseva, O.V.; Kolesnikova, K.; Kolomiiets, A. Customer Churn Prediction in the Software by Subscription Models IT Business
Using Machine Learning Methods. In Proceedings of the International Workshop on Information Technologies: Theoretical and
Applied Problems, Ternopil, Ukraine, 16–18 November 2021.

15. Dias, J.R.; Antonio, N. Predicting Customer Churn Using Machine Learning: A Case Study in the Software Industry. J. Mark. Anal.

16.

17.

18.

2025, 13, 111–127. [CrossRef]
Sanchez Ramirez, J.; Coussement, K.; De Caigny, A.; Benoit, D.F.; Guliyev, E. Incorporating Usage Data for B2B Churn Prediction
Modeling. Ind. Mark. Manag. 2024, 120, 191–205. [CrossRef]
Sergue, M. Customer Churn Analysis and Prediction Using Machine Learning for a B2B SaaS Company. Master’s Thesis, KTH
Royal Institute of Technology, Stockholm, Sweden, 2020.
Saias, J.; Rato, L.; Gonçalves, T. An Approach to Churn Prediction for Cloud Services Recommendation and User Retention.
Information 2022, 13, 227. [CrossRef]

19. Thota, S.R.; Arora, S.; Gupta, S. Hybrid Machine Learning Models for Predictive Maintenance in Cloud-Based Infrastructure for
SaaS Applications. In Proceedings of the 2024 International Conference on Data Science and Network Security (ICDSNS), Tiptur,
India, 26–27 July 2024; IEEE: New York, NY, USA, 2024; pp. 1–6.

20. Gajananan, K.; Loyola, P.; Katsuno, Y.; Munawar, A.; Trent, S.; Satoh, F. Modeling Sentiment Polarity in Support Ticket Data for
Predicting Cloud Service Subscription Renewal. In Proceedings of the 2018 IEEE International Conference on Services Computing
(SCC), San Francisco, CA, USA, 2–7 July 2018; IEEE: New York, NY, USA, 2018; pp. 49–56.

21. Chakraborty, A.; Raturi, V.; Harsola, S. BBE-LSWCM: A Bootstrapped Ensemble of Long and Short Window Clickstream Models.
In Proceedings of the 7th Joint International Conference on Data Science & Management of Data (11th ACM IKDD CODS and
29th COMAD), Bangalore, India, 4–7 January 2024; ACM: New York, NY, USA, 2024; pp. 350–358.

22. Hoang, H.D.; Cam, N.T. Early Churn Prediction in Freemium Game Mobile Using Transformer-Based Architecture for Tabular
Data. In Proceedings of the 2024 IEEE 3rd World Conference on Applied Intelligence and Computing (AIC), Gwalior, India,
27–28 July 2024; IEEE: New York, NY, USA, 2024; pp. 568–573.

23. Rothmeier, K.; Pflanzl, N.; Hullmann, J.A.; Preuss, M. Prediction of Player Churn and Disengagement Based on User Activity

Data of a Freemium Online Strategy Game. IEEE Trans. Games 2021, 13, 78–88. [CrossRef]

24. Kristensen, J.T.; Burelli, P. Combining Sequential and Aggregated Data for Churn Prediction in Casual Freemium Games. In
Proceedings of the 2019 IEEE Conference on Games (CoG), London, UK, 20–23 August 2019; IEEE: New York, NY, USA, 2019;
pp. 1–8.

25. Karmakar, B.; Liu, P.; Mukherjee, G.; Che, H.; Dutta, S. Improved Retention Analysis in Freemium Role-Playing Games by Jointly

Modelling Players’ Motivation, Progression and Churn. J. R. Stat. Soc. Ser. A Stat. Soc. 2022, 185, 102–133. [CrossRef]

26. Pang, L.; Hu, Z.; Liu, Y. How to Retain Players through Dynamic Quality Adjustment in Video Games. In Proceedings of the
2021 IEEE 5th Advanced Information Technology, Electronic and Automation Control Conference (IAEAC), Chongqing China,
12–14 March 2021; IEEE: New York, NY, USA, 2021; pp. 154–160.

27. Boyle, R.E.; Pledger, R.; Brown, H.-F. Iterative Mixed Method Approach to B2B SaaS User Personas. Proc. ACM Hum. Comput. Interact.

2022, 6, 1–44. [CrossRef]

28. Mali, M.; Mangaonkar, N. Behavioral Customer Segmentation For Subscription. In Proceedings of the 2023 3rd Asian Conference

on Innovation in Technology (ASIANCON), Pune, India, 25–27 August 2023; IEEE: New York, NY, USA, 2023; pp. 1–6.

---

<!-- PAGE 34 -->

Appl. Sci. 2025, 15, 6508

34 of 35

29. Li, H. (Alice) Converting Free Users to Paid Subscribers in the SaaS Context: The Impact of Marketing Touchpoints, Message

Content, and Usage. Prod. Oper. Manag. 2022, 31, 2185–2203. [CrossRef]

30. Yoganarasimhan, H.; Barzegary, E.; Pani, A. Design and Evaluation of Personalized Free Trials. arXiv 2020, arXiv:2006.13420.

[CrossRef]

31. Harahap, E.P.; Hermawan, P.; Kusumawardhani, D.A.R.; Rahayu, N.; Komara, M.A.; Agustian, H. User Interface Design’s Impact
on Customer Satisfaction and Loyalty in SaaS E-Commerce. In Proceedings of the 2024 3rd International Conference on Creative
Communication and Innovative Technology (ICCIT), Tangerang, Indonesia, 7–8 August 2024; IEEE: New York, NY, USA, 2024;
pp. 1–6.
van Belle, E.P.J. Data-Driven Drivers of Customer Loyalty in a Business-to-Business Environment for the Software as a Service
Industry. Master’s Thesis, Eindhoven University of Technology, Eindhoven, The Netherlands, 2022.

32.

33. Najjar, A.; Boissier, O.; Picard, G. Elastic & Load-Spike Proof One-to-Many Negotiation to Improve the Service Acceptability of an
Open SaaS Provider. In Autonomous Agents and Multiagent Systems, Proceedings of the AAMAS 2017 Workshops, Best Papers, São
Paulo, Brazil, 8–12 May 2017, Revised Selected Papers; Springer: Berlin/Heidelberg, Germany, 2017; pp. 1–20.

34. Chiang, W.-H.; Ahmad, U.; Wang, S.; Bukhsh, F. Investigating Aha Moment Through Process Mining. In Proceedings of the 25th
International Conference on Enterprise Information Systems, Prague, Czech Republic, 24–26 April 2023; SCITEPRESS—Science
and Technology Publications: Setúbal, Portugal, 2023; pp. 164–172.

35. Ahlgren, O.; Dalentoft, J. Collecting and Integrating Customer Feedback: A Case Study of SaaS Companies Working B2B. Master’s

Thesis, Lund University, Lund, Sweden, 2020.

36. Kumar, G.S.C.; Dhanalaxmi, B. Leveraging Usage-Based SaaS Models: Optimizing Revenue and User Experience. Knowl. Trans.

Appl. Mach. Learn. 2025, 3, 12–17. [CrossRef]

37. Baumann, E.; Kern, J.; Lessmann, S. Usage Continuance in Software-as-a-Service. Inf. Syst. Front. 2022, 24, 149–176. [CrossRef]
38. Curiskis, S.; Dong, X.; Jiang, F.; Scarr, M. A Novel Approach to Predicting Customer Lifetime Value in B2B SaaS Companies.

J. Mark. Anal. 2023, 11, 587–601. [CrossRef]

Ishwaran, H.; Kogalur, U.B.; Blackstone, E.H.; Lauer, M.S. Random Survival Forests. Ann. Appl. Stat. 2008, 2, 841–860. [CrossRef]

39. Breiman, L. Random Forests. Mach. Learn. 2001, 45, 5–32. [CrossRef]
40.
41. Liaw, A.; Wiener, M. Classification and Regression by RandomForest. R. News 2002, 2, 18–22.
42. Chen, T.; Guestrin, C. XGBoost. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery

and Data Mining, San Francisco, CA, USA, 13–17 August 2016; ACM: New York, NY, USA, 2016; pp. 785–794.

43. Dreiseitl, S.; Ohno-Machado, L. Logistic Regression and Artificial Neural Network Classification Models: A Methodology Review.

J. Biomed. Inf. 2002, 35, 352–359. [CrossRef]

44. Hastie, T.; Rosset, S.; Zhu, J.; Zou, H. Multi-Class AdaBoost. Stat. Interface 2009, 2, 349–360. [CrossRef]
45. AlShourbaji, I.; Helian, N.; Sun, Y.; Hussien, A.G.; Abualigah, L.; Elnaim, B. An Efficient Churn Prediction Model Using Gradient

Boosting Machine and Metaheuristic Optimization. Sci. Rep. 2023, 13, 14441. [CrossRef] [PubMed]

46. Rouder, J.N.; Morey, R.D. Teaching Bayes’ Theorem: Strength of Evidence as Predictive Accuracy. Am. Stat. 2019, 73, 186–190.

[CrossRef]

47. Huang, X.; Khetan, A.; Cvitkovic, M.; Karnin, Z. TabTransformer: Tabular Data Modeling Using Contextual Embeddings.

arXiv 2020, arXiv:2012.06678.

48. Ren, J.; Pang, L.; Cheng, Y. Dynamic Pricing Scheme for IaaS Cloud Platform Based on Load Balancing: A Q-Learning Approach.
In Proceedings of the 2017 8th IEEE International Conference on Software Engineering and Service Science (ICSESS), Beijing,
China, 24–26 November 2017; IEEE: New York, NY, USA, 2017; pp. 806–810.

49. Tibshirani, R. Regression Shrinkage and Selection via the Lasso. J. R. Stat. Soc. Ser. B Stat. Methodol. 1996, 58, 267–288. [CrossRef]
50.
51.

van der Aalst, W. Process Mining; Springer: Berlin/Heidelberg, Germany, 2016; ISBN 978-3-662-49850-7.
Jiang, J.; Nguyen, T. Linear and Generalized Linear Mixed Models and Their Applications; Springer: New York, NY, USA, 2021;
ISBN 978-1-0716-1281-1.

52. Rizopoulos, D.; Verbeke, G.; Molenberghs, G. Shared Parameter Models under Random Effects Misspecification. Biometrika 2008,

95, 63–74. [CrossRef]

53. Park, S.; Gupta, S. Handling Endogenous Regressors by Joint Estimation Using Copulas. Mark. Sci. 2012, 31, 567–586. [CrossRef]
54. Pereira, I.; Madureira, A.; Bettencourt, N.; Coelho, D.; Rebelo, M.Â.; Araújo, C.; de Oliveira, D.A. A Machine Learning as a Service

(MLaaS) Approach to Improve Marketing Success. Informatics 2024, 11, 19. [CrossRef]

55. Lundberg, S.M.; Lee, S.-I. A Unified Approach to Interpreting Model Predictions. In Proceedings of the 31st International
Conference on Neural Information Processing Systems, Long Beach, CA, USA, 4–9 December 2017; Curran Associates Inc.:
Red Hook, NY, USA, 2017; pp. 4768–4777.

56. Ribeiro, M.T.; Singh, S.; Guestrin, C. “Why Should I Trust You?”: Explaining the Predictions of Any Classifier. arXiv 2016,

arXiv:1602.04938.

---

<!-- PAGE 35 -->

Appl. Sci. 2025, 15, 6508

35 of 35

57. Dwork, C. Differential Privacy. In International Colloquium on Automata, Languages, and Programming; Bugliesi, M., Preneel, B.,

Sassone, V., Wegener, I., Eds.; Springer: Berlin/Heidelberg, Germany, 2006; pp. 1–12.

58. Koneˇcn\‘y, J.; McMahan, H.B.; Yu, F.X.; Richtárik, P.; Suresh, A.T.; Bacon, D. Federated Learning: Strategies for Improving

59.

Communication Efficiency. arXiv 2016, arXiv:1610.05492.
Shi, W.; Cao, J.; Zhang, Q.; Li, Y.; Xu, L. Edge Computing: Vision and Challenges. IEEE Internet Things J. 2016, 3, 637–646.
[CrossRef]

60. Grigoriadis Ioannis and Vrochidou, E. and T.I. and P.G.A. Machine Learning as a Service (MLaaS)—An Enterprise Perspective. In
Proceedings of the International Conference on Data Science and Applications, Jaipur, India, 14–15 July 2023; Nanda, S.J., Yadav,
R.P., Gandomi, A.H., Saraswat, M., Eds.; Springer: Singapore, 2023; pp. 261–273.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Review
Data-Driven Decision Support in SaaS Cloud-Based
Service Models
GerasimosCharizanis,EfthimiaMavridou,EleniVrochidou ,TheofanisKalampokasandGeorgeA.Papakostas*
MLVResearchGroup,DepartmentofInformatics,DemocritusUniversityofThrace,65404Kavala,Greece;
gecsari@cs.duth.gr(G.C.);emavridou@cs.duth.gr(E.M.);evrochid@cs.duth.gr(E.V.);tkalampo@cs.duth.gr(T.K.)
* Correspondence:gpapak@cs.duth.gr;Tel.:+30-2510-462321
Abstract: Software as a service (SaaS) is a major service model for delivering software
to end users through the cloud. SaaS platforms provide their users with cost-efficient,
flexibleandscalableservicesthatcanbeavailableondemand,anytime,andanywhere.
Moreover,SaaSempowerssoftwareproviderstoestablishrecurringrevenueandcreate
profitablebusinesses. However,SaaScanendurehighcustomerturnoverduetoreasons
suchasservingawiderangeofcustomers, intensecompetitionandrapidevolutionof
technology. Maintainingaregularcustomerbaseandkeepingusersengagediscrucialfor
thesurvivalofaSaaSbusiness. Thus,itiscrucialforSaaSproviderstoidentifyboththe
reasonsbehindusers’engagementandchurnoftheirapptowardstakingproperactionsto
retaintheminthelongterm. SaaSdataregardinguserbehavior,subscriptionsandsystem
performance can be utilized for deriving insights and identifying patterns to support
decision-makingforSaaSproviders. Tothisend,theaimofthissurveyistoreviewresearch
indata-drivendecisionsupportsystemsinSaaS,identifyingcurrentgapsandchallenges
andhighlightingdirectionsforfutureimprovementstowardsthedevelopmentofmore
efficientandintelligentsystems.
Keywords: softwareasaservice;churnprediction;userengagement;machinelearning;
usagemining
AcademicEditor:Miguel
García-Pineda
1. Introduction
Received:2May2025
Cloud computing is the dominant model for providing software and technology
Revised:29May2025
Accepted:6June2025 infrastructures nowadays. This approach enables access to computing resources and
Published:10June2025 applications without the need for hardware setup and maintenance. The main cloud
Citation: Charizanis,G.;Mavridou, service models are infrastructure as a service (IaaS), platform as a service (PaaS) and
E.;Vrochidou,E.;Kalampokas,T.; softwareasaservice(SaaS)[1].
Papakostas,G.A.Data-Driven TheIaaSmodelprovidesinfrastructureresourcesthroughthecloudsuchasstorage
DecisionSupportinSaaSCloud-Based
andcomputationalpower. Usersdonothavetoupdateandmaintaintheinfrastructure,yet
ServiceModels.Appl.Sci.2025,15,
theyareinchargeofsettingupoperatingsystems,softwareanddata[2]. Onthecontrary,
6508. https://doi.org/10.3390/
thePaaS modelalsoprovides thesoftware resources forcreating softwarein thecloud.
app15126508
Usersdonotmaintainthesoftwaredevelopmentenvironment,buttheyhavetowritetheir
Copyright:©2025bytheauthors.
owncode. Finally,theSaaSmodelprovidesready-to-usesoftwaresolutions[3],meaning
LicenseeMDPI,Basel,Switzerland.
thattheuserscanstartusingthesoftwarewithoutinstallation. Therefore,IaaSandPaaS
Thisarticleisanopenaccessarticle
distributedunderthetermsand usersaremainlydevelopersandITprofessionals,whileSaaSuserscanvarydependingon
conditionsoftheCreativeCommons thesolutionprovidedbytheSaaS.Forexample,aSaaSthatprovidesinvoicingsoftware
Attribution(CCBY)license mayhaveusersrangingfromvariousprofessions,e.g.,engineers,lawyers,etc. TheSaaS
(https://creativecommons.org/
modelistheleadingcloudcomputingmodelfordeliveringsoftwarenowadayssinceit
licenses/by/4.0/).
Appl.Sci.2025,15,6508 https://doi.org/10.3390/app15126508

Appl.Sci.2025,15,6508 2of35
enables software distribution without the need for installation and hardware setup [4].
Thus,userscanusethemeasilyandquickly,whilegenerallypayingbysubscriptioninstead
ofalargeamountupfront.
TheSaaSmodelenablessoftwareproviderstocreateprofitablebusinessesallowing
softwaredistributionthroughthecloudtomanyusers,simultaneously[5]. Moreover,the
subscription-basedbusinessmodelprovidesopportunitiesforstableincomestreams. Thus,
thesuccessofaSaaSmodelasabusinessheavilydependsonwhetheritmaintainsacore
userbase. Whenusersexperiencemeaningfulbenefitsfromasoftwaresolution,theyuseit
regularlyandforalongtime. EngagedusersarethesuperpowerofSaaSsincetheytendto
useitinthelongtermandwithminimumsupport,whiletheycouldpossiblysuggestitto
otherusers. Thecostofobtainingnewusersisgenerallymuchhigherthanretainingthe
onesthatalreadyexist[6]. Thus,SaaSbusinessesstrivetoincreaseuserengagementand
reduceuserchurn,i.e.,thepercentageofusersthatcanceltheirsubscriptions.
Recentindustryreportspointtoseveralgrowingchallengesthatmakestrong,data-
drivendecisionsupportsystemsmoreimportantthaneverforSaaScompanies. Onemajor
issueisthehighrateofcustomerchurn,shortlyaftercustomerssignup,whichiscommonly
observedwithnewartificialintelligence(AI)-poweredtools(https://www.paddle.com/
blog/saas-market-report-q1-2025,assessedon1June2025). Thisisparticularlyaproblem
intheB2Cmarket, whereuserbehaviorchangesquicklyandishardtopredict. Atthe
sametime,manySaaSbusinessesdonotpayenoughattentiontohowtheyadjusttheir
prices,eventhoughpricingcanhaveabigimpactonuserretention(https://www.omnius.
so/blog/saas-industry-report-2024, assessedon1June2025). Anotherchallengeisthe
riseofmulti-cloudandhybridsystems,wherecompaniesruntheirsoftwareacrossseveral
cloud platforms. This makes it harder to gather and analyze all of their data in one
place(https://www.fortunebusinessinsights.com/software-as-a-service-saas-market-10
2222, assessed on 1 June 2025). The growing use of AI in SaaS platforms introduces
new benefits, like automation and personalization. However, this also leads to higher
infrastructurecostsduetoexpensivecomputingresourceslikeGPUs,high-volumedata
usage, and the need for highly skilled professionals to build and maintain AI systems
(https://www.paddle.com/blog/saas-market-report-q1-2025,assessedon1June2025).
ThesetrendsintheSaaSindustryindicatethatSaaSprovidersfaceincreasinglycomplex
decisions. Asaresult,theroleofdata-drivendecisionsupportsystemsbecomescriticalin
helpingSaaSvendorsmakeinformed,timely,andcost-effectivechoices.
AtthecoreofmodernSaaSecosystems,vastamountsofdataaregenerated,regarding
userbehavior,subscriptionsandsystemperformance[7]. SaaSdatacanbeleveragedfor
derivinginsightsandidentifyingpatternstosupportdecision-makingforSaaSproviders.
Forexample,machinelearning(ML)algorithmscanbeemployedtocreatechurnprediction
modelsforuserchurnprediction[8]. Giventhatinformation,SaaSproviderscanactwitha
specificincentivetoreengagethoseusers. Tothisend,theaimofthissurveyistoreview
researchindata-drivendecisionsupportinSaaSapplications. Inparticular,thegoalofthis
workistoidentifyresearchthatutilizesdatatosupportSaaSvendorstowardsreducing
churnandincreasinguserengagement,satisfactionandloyalty.
Althoughrelatedworksarealreadypresentintheliterature[9–11],thisstudystands
outbyofferingacomprehensiveperspectiveonleveragingSaaSdatatosupportdecision-
makingforSaaSvendorstosustainuserloyaltyandsatisfaction. Unlikepriorresearchthat
oftenfocusesnarrowlyonspecifictaskssuchaschurnprediction,thisworkprovidesa
holisticexaminationofstrategiestomaintainastableuserbase. Specifically,thediverse
objectivesofexistingapproachesareanalyzed,asthevarietyofemployeddatasources,
and the comparative effectiveness of different machine learning methods on multiple
occasions.Moreover,thewaystheoutputsoftheseapproaches,rangingfromvisualizations

Appl.Sci.2025,15,6508 3of35
toactionableinsights,arepresentedtoSaaSvendorstofacilitatespot-ondecision-making,
arealsodiscussed.
Therestofthepaperisstructuredasfollows: Section2presentsrelatedworksand
highlightsthecontributionsofthispaper. Section3summarizestheresearchmethodol-
ogy, while Section 4 presents the results. Discussions and conclusions are provided in
Sections5and6,respectively.
2. RelatedWork
ThecurrentworkconstitutesascopingreviewofresearchtoassistSaaSvendorsin
decision-makingbasedonthedatathatSaaSbusinessesgenerate. Therefore,theaimisto
identifyresearcheffortsthatperformliteraturereviewsonthesamesubject. Tothebest
ofourknowledge,thereisnoexacttypeofreviewfoundintheliterature. However,there
areliteraturereviewsthatarerelatedtothesubject,yetwithdifferentfocus. Forexample,
theauthorsin[9]performedareviewonmachinelearningmethodsforchurnprediction
coveringtheyearsbetween2015and2023. Althoughtheirworkprovidedinsightsonthe
useofMLforchurnpredictionhighlightingthetrade-offsofdifferentMLmethods,the
focuswasonlyonchurnprediction,anditdidnotaddressotherusecasessuchasuser
segmentationorcustomerlifetimevaluepredictionwhicharecriticaltosupportbusiness
ownersondecision-making. Moreover,thereviewfocusedontelecommunications,finance
and online gaming industries, regardless of the type of businesses and the adoption of
cloud-based models and SaaS specifically. To this end, our work constitutes a review
tailoredtosupportbusinessesthatoperatebasedontheSaaScloudmodelprovidinga
moreholisticapproachbycoveringawiderangeofusecases,importanttoretainastrong
customerbase.
Similarly, the authors in [10] conducted a general review of decision analytics ap-
proachesforcloudcomputing. It’salsoworthnotingthattheirworkwaspublishedmore
than10yearsago, in2014, andthereforeitdoesnotcovercurrentresearchefforts. The
authorsfocusedondecisionsupportforcloudcomputingforproblemslikeserviceselection
andpricing,ratherthandiscussingdecisionsupportforuserretentionandengagement.
Moreover,therewasnodescriptionofthesystematicreviewresearchmethodologyandno
informationorstatisticsregardingthenumberofpapersincludedintheirreview.Moreover,
the authors considered papers with methods that were not data-driven, like heuristics
or ontology-based. The review presented in [11] addressed a broad range of different
topicsAI,ML,BusinessIntelligence(BI)andSaaSatahighlevelwithoutgoingintodetail.
Regardinguserbehavior,authorsdiscussedpredictionstrategiesandpersonalizationof
userexperience,however,withoutgoingintospecificinsightsandrecommendations. A
systematicreviewmethodologywasalsomissing.
Anotherpaper[5]publishedinthesameyear(2014)coveredthetechnicalchallenges
andperspectivesforSaaSsuchasmulti-tenancyandscalability. Thatreviewalsolackeda
researchmethodologyanddidnotmentionhowthereviewedapproacheswereselected.
Performance comparisons were not included, and only a qualitative analysis was per-
formed.Lastly,therewasnofocusonuserinteractionsubjectslikeuserretentionandchurn.
Finally,theresearchpresentedin[11]addressedAIadoptionforBIinSaaS.Althoughit
wasmentionedthataliteraturereviewwasconducted, only8paperswereincludedin
theiranalysis.
Tothisend,comparedtotheexistingbibliography,thecurrentwork:
• Presentsasystematicreviewprocess.
• Includesonlydata-drivenmethods.
• Presentsofperformancecomparisontosupportmodelselection.

Appl.Sci.2025,15,6508 4of35
• DiscussesofchallengestheSaaSvendorsfaceregardingmaintainingacoreuserbase
likechurn,userengagementanduserretention.
Moreover, the contributions of this work can be summarized in the following
distinctpoints:
• Acomprehensivereviewofresearchinitiativesaimingtosupportdecision-making
for SaaS providers, expanding beyond single-task approaches to address broader
strategicgoals.
• Anoverviewofvariousdatainputsutilizedacrossstudies,identifyingfrequentlyused
datasourcesandhighlightingcaseswheremultiplekindsofdatawereintegratedfor
morerobustinsights.
• Acomparativeevaluationofemployedmachinelearningtechniques,analyzingtheir
relativestrengths,weaknesses,andperformanceindifferentSaaSdecision-makingcontexts.
• Anoverviewofuser-facedoutputtypesproposedbyresearcherstohelpSaaSproviders
takeeffective,data-drivenactions.
• Asynthesisofbestpracticesandkeytakeawaysfromtheliterature,offeringactionable
recommendationsforenhancinguserretentionandensuringthelong-termsustain-
abilityofSaaSbusinessmodels.
3. ResearchMethodology
Theresearchquestionsthatweaimtoanswerinthissurveyarethefollowing:
RQ1: What is the main focus of the papers in the area of data-driven methods for
supportingdecision-makinginSaaS?
RQ2: Whatkindofdataisutilized?
RQ3: Aremachinelearningmethodsemployedandhoweffectivearethey?
RQ4: HowaretheresultspresentedtoSaaSproviderstosupportdecision-making?
ThesurveywasconductedfollowingthePRISMA-ScRmethodology.Theresearchwas
conductedusingtheScopusandScholarbibliographicdatabasesthatcontainpapersfrom
librarieslikeSpringer,Elsevier,IEEE,etc. Thefollowingquerywasposedon5March2025
toScopus:
(“webusagemining”OR“customersegmentation”OR“loganalysis”OR“churn”
OR“userengagement”OR“customerlifetimevalue”OR“userlifetimevalue”OR“user
segmentation”)AND“SaaS”ANDPUBYEAR>2013ANDPUBYEAR<2026.
Thisqueryreturned426results. Screeningwasperformedbyreadingthetitleand
abstract in order to identify the completely irrelevant ones. This process resulted in
147papers. Thesepapersweresearchedandretrievedinordertoreadthemthoroughly.
Duringthissecondscreeningphase,therewereexcludedallpapersthatwerenotrelevant
tooursubject. Relevancywasbasedonthreemainrules: papersshouldbeaboutSaaS,
decision-supportandbasedondata. Thus,theexcludedpapersofthesecondphasefall
intooneofthethreecategories:
• NotrelatedtoSaaS;
• AlthoughrelatedtoSaaStheywerenotaboutsupportingdecisions;
• Notdata-driven,theoretical.
Thisprocessresultedin22papersthatwereincludedinoursurvey. Asupplementary
search was conducted in Google Scholar using keywords like “churn prediction SaaS”,
“userengagementSaaS”and“userlifetimevalueSaaS”resultingin6morepapers. Thus,a
finallistof28paperswasformedthatwasanalyzedfurther.Figure1illustratestheresearch
processfollowed.

Appl.Sci.2025,15,6508 5of35
Figure1.PRISMAflowdiagram.
At this stage, it is important to acknowledge the limitations of this research. The
research was limited from 2014 to 2025, so as to cover a full range of 10 years, as well
as due to the fact that SaaS adoption began to rise mainly after 2014, where the main
volumeofliteraturewaslocated. However,thelatterdidnotaffectourresearchfindings,
since the main volume of the research was located after 2014 and especially from 2020
onwards. Moreover, the database coverage was limited to Scopus and Google Scholar.
Whileotherdatabasesalsoexist,suchasWebofScienceorPubMed,theuseofbothScopus
andGoogleScholarcouldimprovecoverageandreliability,astheybothcoverawiderange
ofpeer-reviewedsources.
4. Data-DrivenDecisionSupportinSaaS
4.1. MainFocus
TheSaaSmodelismainlyofferedbysubscriptionwhichisthemainsourceforrevenue
generationforsuch businesses. Havinga stronguser baseiscrucial fortheviabilityof
SaaSbusinesses. Therefore,itisveryimportantforSaaStomaintainasmallpercentageof
usersthatcanceltheirsubscriptions(churn). ForSaaSbusinesses,evenasmallreductionin
churncanleadtosignificantprofitgrowthandahealthierandlong-termbusiness. Forthis
reason,manyresearchersfocusonpredictingchurninSaaSbusinessesandonidentifying
thebestperformingmachinelearningalgorithmsforeachcase.
Figure2summarizestheresultsregardingRQ1. AscanbeseeninFigure1,mostof
thereviewedpapers(53.57%)focusedonchurnprediction. Thiscomesasnosurprisesince
highchurnratescannotsustainaSaaSbusinessmodel. Thechurnrateisthenumberof
usersthatleavetheSaaSdividedbythetotalnumberofusers. Churnpredictionrefersto
predictingifauserisabouttochurn.Theauthorsin[12,13]focusedonapplyingandtesting

Appl.Sci.2025,15,6508 6of35
variousalgorithmsfedwithusagedatatoevaluatetheirperformanceinchurnprediction,
inthecontextofSaaS,whileresearchpresentedin[8,14–17]followedthesameprinciple
butshiftedtheirfocustowardstheBusinesstoBusiness(B2B)SaaSbusinessmodel. All
thosestudiesaimedtopointoutkeyfeaturesthatchurningcustomerspossessandoffer
SaaSprovidersactionableinsightsforimprovingtheircustomerretentionstrategies.
Figure2.Mainfocusofthereviewedpapers(RQ1).
Further research on this topic included in [18,19] focused on comparing multiple
machine learning algorithms to figure out which one was best performing for churn
predictionintheSaaScloudservicemodel.Theauthorsin[18]developedachurnprediction
systemtopredictcustomerattritionforcloud-basedserviceproviders(CSPs),attempting
anearlyidentificationofcustomersatriskofcancelingsubscriptions. Churnpredictionin
CustomerRelationshipManagementsystems(CRM)usinghybridmachinelearningmodels
wasaddressedin[19]. Apartfromthecomparisonbetweenmachinelearningmethods,the
authorsin[20]chosetousemachinelearningtoanalyzeandmonitorcustomersatisfaction
from support tickets and predict whether a client is going to renew their cloud service
subscription. Accordingly,theresearchpresentedin[21]experimentedwiththecreation
andapplicationofahybridmachinelearningframeworkdesignedforreal-timeprediction
ofusereventsinSaaSproductssuchassubscriptioncancellation,userinteractions,and
taskabandonmentduringusersessions.
Severalresearcheffortsdealtwithpredictingchurnandimprovingretentionspecif-
icallyforonlinegamesbasedontheSaaSmodel. Thestrategyemployedin[22]aimed
toidentifychurnersinearlierstagesofamobilefreemiumgame,evenafterthetutorial
phase,usingminimalearly-stageuserdata,featuringaTransformer-basedarchitecture(FT-
Transformer)tailoredfortabulardata. Theresearchpresentedin[23]focusedonpredicting
playerchurnanddisengagementwithina14-daywindowinafreemiumonlinestrategy
gameusingmachinelearning. Specifically,itaimedtoidentifythemosteffectivemachine
learningtechniquesandlabelingapproachesforearlydetectionofplayersatriskofleav-
ingthegame, enablingproactiveretentionstrategies. In[23]theauthorsdistinguished
betweenchurn(permanentdeparture)anddisengagement(reducedactivity),providinga
comprehensivecomparisonofmethodstailoredtothegamingindustry. Theauthorsof[24]
extendedtheirresearchtoalargertimespan,focusingonimprovingchurnpredictionin
casualfreemiumgamesbycombiningsequential(temporal)andaggregated(static)data
usingdifferentneuralnetworkarchitectures. Theirstudyinvestigatedhowintegrating
these two types of data can enhance prediction accuracy compared to models that rely
solelyonsequentialoraggregateddatawhilealsoaddressingthechallengeofpredicting

Appl.Sci.2025,15,6508 7of35
churn in non-contractual contexts (for example in mobile games), where players could
leavewithoutexplicitsignals.
Additionally,theresearchconductedin[25]focusedonenhancingretentionanalysis
in freemium role-playing games (RPGs) by modeling players’ motivation, progression,
and churn. Particularly, it aimed to understand how in-game behaviors (engagement,
collaboration,andachievement)atdifferentlevelsinfluencedropoutrates,andhowthese
interdependencies could be leveraged to predict player retention more accurately. As
playerretentioninthevideogameindustryisthekeytoitsongoingprosperity,workin[26]
exploredhowvideogameoperatorscanretainplayersinsubscription-basedgamesby
dynamicallyadjustingthequalityofthegameovertime. Thestudydevelopedadynamic
programming model that considered players’ memory of past service experiences and
networkexternalities(thephenomenonwherethevalueorutilityofaproductorservice
increasesasmorepeopleuseit)todeterminetheoptimaldata-drivendecisionstomaximize
long-termprofits.
Inordertobetterunderstandandadapttoclients’needsinSaaSservicesitisimpor-
tanttocategorizethemintogroupstobeabletoprovidethempersonalizedattention. An
iterativemixed-methodapproachforcreatinguserpersonasinthecontextofB2BSaaS
productswaspresentedin[27]. Thatworkalsoaimedtodemonstratehowthegenerated
userpersonascouldbepracticallyappliedasanindicatortoimprovethedesign,develop-
ment,andprioritizationoffeaturesinaB2BSaaSproduct. Anotherresearchoncustomer
segmentationwaspresentedin[28],particularlyexploringhowbehavioralcustomerseg-
mentationandappusageanalysiscanbeleveragedtopredictcustomerinterestinpremium
subscriptionsandidentifykeyinfluencingfactorstoimprovesubscriptionconversionrates
formobileapps. Userconversionfromfreetrialstopaidsubscriptionswasthemainfocus
of[29],examininghowmarketinginteractions(ads,messages,emails,etc.) andtheirtype
ofcontentalongwithfree-trialusagebehaviorscouldinfluenceusers’decisions. Further
insightsregardingfreetrialswereshowcasedin[30]. Thestudyhighlightedtheimportance
of free trials as a customer acquisition strategy in the SaaS industry and analyzed how
customeracquisition,retentionandprofitabilitywereaffectedbythedurationoffreetrials
todiscovertheiroptimaldesign.
Establishingalong-termrelationshipwithcustomersrequireskeepingthemengaged
andsatisfiedwiththeservicestheyaregetting. Theauthorsin[31]examinedhowvisual
andfunctionalaspectsofuserinterface(UI)designcouldinfluenceuserexperience(UX).
Advancingfurtheronthesubjectofcustomerloyalty,theauthorsin[32]followedadata-
drivenapproachtodiscoveringthedeterminantsofcustomerloyaltyintheB2BSaaSindus-
try. Thatstudyexploredhowtransactionalandbehavioraldata(likeplatformengagement,
andcommunicationfrequency)couldbeleveragedtopredictcustomerloyaltywithout
relyingontraditionalsurveys. Theresearchpresentedin[33]proposedthedesignofan
adaptivenegotiationmechanismtoallowproviderstointeractwithclientsanddynamically
manageservicequality,usersatisfaction,andresourcecostsincloudenvironments.
Averyimpactfulfactorinkeepingcustomersfromchurningiswhethertheseindi-
vidualsdiscoverthe“ahamoment”andacknowledgethereturnontheirinvestmentin
SaaS services. The “aha moment” refers to the point when users understand the value
ofthesoftwareproduct,whichiscrucialforenablingcustomeractivationandretention.
Theauthorsof[34]focusedonidentifyingthe“ahamoment”ofB2BSaaScustomersusing
process mining techniques. Specifically, this study investigated how customers switch
fromtheactivationphasetotheretentionphaseintheAARRR(Acquisition,Activation,
Retention,Revenue,Referral)modelbyidentifyingandexaminingbehaviorpatternsof
clients. Inordertoprovidevaluetotheircustomers,customerfeedbackmustbetakeninto
consideration,sothatproviderscanofferamorepersonalizedexperienceandcatertotheir

Appl.Sci.2025,15,6508 8of35
clients’needs. Theresearchpresentedin[35]exploredstructuredapproachesforcollecting
andintegratingcustomerfeedbackinSaaScompaniesoperatingintheB2Bmarketand
waysofintegratingcustomerknowledgeintosoftwaredevelopmentprocesses.
SaaS pricing also takes its toll on user satisfaction as it affects SaaS users directly.
Thestudypresentedin[36], however, showcasedadata-drivenframeworkintegrating
real-timeusagetracking,machinelearningfordemandprediction,andcustomer-centric
billingadjustmentstooptimizerevenueforproviderswhileenhancinguserexperienceand
customerloyalty. AdditionalfactorsinfluencingusagecontinuanceinSaaSapplications,
particularlyaftertheinitialadoptionphaseweredemonstratedin[37],inanattemptto
improveuserretentionandreducechurnbyenhancingusagepenetration(thenumberof
usersactivelyengagingwiththesoftware).
Finally,anotherproblemthattheresearchaddressedwastheCustomerLifetimeValue
(CLV)prediction. CLVpredictionmodelspredictthefuturerevenuethatcustomersmay
generate. Theauthorsin[38]proposedanovelmachinelearningframeworkforpredicting
CLVinthecontextofB2BSaaScompaniesanddescribedseveralbusinessapplications
whereCLVpredictionswereusedtoenhancemarketingexpenditures,improveReturn
onInvestment(ROI),andprovideessentialinsightsformanagementdecision-makingin
thiscontext.
4.2. DataSources
InordertocompareandevaluatealgorithmsforpredictingchurninSaaSbusinesses,
researchers chose to utilize various types of data sources for their experiments. As per
theresearchquestionRQ2,themostcommoncategoryamongstudies[8,12–19]isusage
behavior data. All those studies incorporate some form of user interaction or system
activity logs like logins, sessions, file uploads, application usage, number of users and
actionsperformed.
Anothercommontypeofdatausedin[8,12–14,16,17]istransactionalandbusiness
metricsincludingmonetaryvalues(monthlycharges,totalexpenses,amountspent),sub-
scription status and billing information. Additionally, temporal data, contractual data
andcustomerlifecycleindicatorsappearedin[12,13,15,17–19]concerningcustomertenure,
daystoexpiry,subscriptionageandmonthlysnapshotsorobservationwindowswhilein
studies[8,16–19]customerdemographicsandattributeswerealsoutilized(companysize,
region,industry,onboardingstatusorbusinessage).
Theauthorsin[18]alsousedbillingandloyaltyprogramdatalikeloyaltyprogram
status and billing cycles. At last, customer support interaction data were used in [15]
(supporttickets,resolutiontimes)and[16](supportcaselogs)whilecustomersatisfaction
metricssuchasNetPromoterScore(NPS)andcallqualitywerespecificallyincludedin[17].
Furthermore,regardingchurnprediction,theapproachfollowedin[20]usedsupportand
subscriptionmetadatawhilethestudy[21]focusedonclickstreamdatacombinedwith
dynamicuserprofiles(subscriptionstatus,tenure,demographics).
Studiesthatfocusedonpredictingchurningamesfeaturingasubscriptionmodelas
in[22–24],sharedastrongemphasisoneventlogs,sessiondata,andgameplaybehavior
andchosetoutilizebehavioraldata(gameplayactions,tutorialengagement,sessionmetrics,
clicks,purchases,logins)todesigntheirchurnpredictingmodels.
Focusingonimprovingretentionoffreemiumonlinegames,thestudy[25]conducted
itsresearchbyutilizingplayerbehavioraldata(engagement,achievements,collaboration,
progress,dropouts),demographicandcontextualdata(genderofgamecharacters,geo-
graphiclocation,timeofplay),andsomegame-specificmetrics. Moreover,thedataused
in[26]wasderivedfromasimulateddatasetcontainingsyntheticdata(simulatedquality
levels,utilityfunctions,andcoststructures).

Appl.Sci.2025,15,6508
9of35
Datain[27]arederivedfromsurveys,interviewsandwebbehavioraldata(timespent
perpage,clicksperfeature,aggregatedovertime)andareusedincustomersegmentation
algorithms. Onthesamepage,work[28]useddemographicfeatures(age,gender,state),
behavioral features (engagement level, time spent, number of screens viewed, clicks,
sessions)andtransactionalfeatures(maximumbudget,maximumreturnoninvestment,
numberofpurchases)forcustomersegmentation.
Forthepurposeofdiscoveringdriversofuserloyaltyandimprovingusersatisfaction
andengagement,studies[29–32,34,37]leveragedmainlybehavioralandusagedata(login
frequency, feature usage, interaction patterns to understand user engagement, product
adoptionovertime). However,in[35,37]interviewandsurveydatawereused,providing
contextonuserperceptions,satisfaction,anddemographiccharacteristics.Instudies[34,35],
systemlogsandeventdatawereusedandspecificallyin[35]logsareusedalongsidedirect
feedbacklikesurveysandsupporttickets. Marketing,freetrial,andtransactionaldata(ad
impressions,messagetypes,marketingvariablesandtrialdurationvariations)areutilized
byresearchersin[30,33]whilein[36]simulateddatawereemployed(transactionvolumes,
volatility,user-centricmetrics,userprofiles,negotiationdynamics)toexplorehypothetical
userbehaviorsandnegotiationdynamicsinscalable,controlledenvironments. Last,stud-
ies[32,35]utilizedrich,multi-sourcedataintegrations,combiningCRM,financial,usage,
andexternalfirmographicdatainordertobettermodelloyaltyandcustomerrelationships.
Finally,research[38],whichfocusedonpredictingCLV,employedvarioustypesof
datatoachieveitsgoal. Thosedataincludedrevenuedata(monthlyrecurringrevenue,
historicalbillingdata),productlicensedata(producttypes,acquisitionchannels,license
terms), product usage data (feature adoption, user activity logs, engagement metrics),
firmographic data (company size, industry, geography, employee count) and customer
segments based on behavior. Table 1 summarizes the types of input data used in the
reviewedapproaches.
Table1.Typesofdatasourcesusedbythereviewedapproaches(RQ2).
Transactional/
| Usage    |          | Customer | Financial | Customer | Satisfaction |                  |           |
| -------- | -------- | -------- | --------- | -------- | ------------ | ---------------- | --------- |
| Ref.     | Business |          |           |          |              | Survey/Interview | Marketing |
| Behavior |          | Profile  | Data      | Support  | (e.g.,NPS)   |                  |           |
Metrics
| ✓   |     | ✓   | ✓   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[18]
✓
[24]
| [12] ✓ | ✓   | ✓   |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| [14] ✓ | ✓   |     |     |     |     |     |     |
✓
[22]
✓ ✓
[19]
✓ ✓
[25]
| [13] ✓ | ✓   | ✓   |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| [20]   |     |     |     | ✓   |     |     |     |
| ✓      |     | ✓   |     | ✓   |     |     |     |
[15]
| ✓   | ✓   | ✓   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[8]
✓
[23]
| [21] ✓ |     | ✓   |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| [38] ✓ | ✓   | ✓   | ✓   |     |     |     |     |
| [29]   |     |     |     |     |     |     | ✓   |
| ✓      |     |     |     |     |     | ✓   | ✓   |
[30]
| ✓   |     | ✓   |     |     |     | ✓   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[31]
|     |     | ✓   |     |     | ✓   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[26]
| [33] ✓ |     |     |     |     | ✓   |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
[32] ✓
✓ ✓
[27]
| ✓   |     | ✓   |     |     |     | ✓   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[37]

Appl.Sci.2025,15,6508 10of35
Table1.Cont.
Transactional/
Usage Customer Financial Customer Satisfaction
Ref. Business Survey/Interview Marketing
Behavior Profile Data Support (e.g.,NPS)
Metrics
[16] ✓ ✓ ✓ ✓
[28] ✓ ✓
[35] ✓ ✓ ✓ ✓
[17] ✓ ✓ ✓ ✓
[36] ✓ ✓
[34] ✓ ✓ ✓
4.3. MachineLearningMethods
Regarding RQ3, most of the studies relied solely on machine learning methods to
conducttheirresearchandgeneratetheirexpectedresults. Amongthepapersfocusedon
churnprediction,RandomForest(RF)[39–41]wasoneofthemostwidelyusedmethods,
appearinginstudies[8,13–19,23,24]. Inthestudy[18],RFwith64estimatorsachievedan
excellentperformanceof98.8%accuracy,0.997AreaUndertheCurve(AUC),andstrong
F-measures(0.989non-churn,0.981churn). Instudies[8,14],RFalsostoodoutwith87%
testing accuracy, while being resistant to noise and overfitting. A study [13] reported
exceptionallystrongRFresultsaswell,withF1-scoreof92.6%andrecallof91.6%,whilea
study[15]foundthatRFhadthehighestprecision(0.80)amongthemodelstested,though
recalllaggedbehindXGBoost. Onthecontrary,RFunderperformedinthestudy[12],with
anAUCof~0.5,andaddingPCA(PrincipalComponentAnalysis)didnothaveanyimpact
ontheresults. Inwork[23],RFachievedAUC>0.99and97%accuracy,outperformingall
othermodelsacrossvariouslabelingschemeslikeslidingwindowsandactivityquartiles
whileinthestudy[24]RFwasusedasabaselinecombiningsequentialandaggregateddata,
whereitachievedanAUCof0.72,whichwasnotablylowerthanthehybridLongShort-
TermMemory(LSTM)models,indicatingitslimitationsinmodelingtemporaldynamics
insequentialdata. Inthestudy[17],RFshowedonlymoderatesuccesswithAUC-ROC
~0.65,thoughitsperformanceimprovedslightlywhenpairedwithSMOTE-Tomekforclass
imbalancehandling. Figure3presentsthenumberofpapersthatsuccessfullyemployed
specificmachinelearningalgorithms. Thus,itcontainsthenumberofpaperstowhichthe
specificmachinelearningalgorithmnotedthebestresults. RFwassuccessfullyusedin
moreworksthananyothermachinelearningalgorithm.
ExtremeGradientBoosting(XGBoost)[42]wastestedinstudies[12,15,16],consistently
deliveringtop-tierresults. Inresearch[12],XGBoostachievedthehighestAUC(0.7941)
and,afterthresholdtuning,improvedsensitivityto74%. Study[15]reportedROCAUC
of0.86,recallof0.85andF1-scoreof0.82,outperformingothermodelssuchasRandom
Forests andLogistic Regressionand identifiedticket resolution timeandlicense ageas
key features. Study [16] found XGBoost and Logistic Regression achieved comparable
AUC(~60%),butXGBoostwaslessprofitablethanlogisticregressionwhenmeasuredby
ExpectedMaximumProfit. XGBoostandGradientBoostingDecisionTrees(GBDT),were
alsousedin[22]withXGBoostemergingasthebest-performingmodelwith98.8%AUC,
whileGBDTfollowedwith93.4%AUC.
Decision Trees (DT) were used in studies [8,13,14,16,19]. In work [13], DT was the
bestperformerusingChi-squared-selectedfeatures,with88.2%F1-scoreand94.4%recall.
In contrast, studies [8,14] revealed DT’s tendency to overfit, achieving perfect training
accuracybutonly76%ontestdata. DTalsoservedasabaselinein[16,19],withmoderate
performancecomparedtoensembleandhybridmodels.

Appl.Sci.2025,15,6508 11of35
Figure3.Machinelearningmethodsproposedtousebythereviewedpapers.
LogisticRegression(LR)[43]wasappliedinstudies[8,12,13,15–17],mostlyasabase-
line due to its interpretability. Its AUC ranged from 0.71 to 0.74 in studies [8,12], and
it consistently offered stable, if lower, performance. In work [16], LR delivered strong
profit-basedperformance,leadinginExpectedMaximumProfitandTopDecileLiftwhen
pairedwithusage-basedfeatures. Intheresearch[17],LRinitiallyhad97%accuracybut
0% recall until SMOTE-Tomek was applied, improving recall to 57% (but at the cost of
reducedprecision).
Support Vector Machines (SVM) featured in studies [8,13,14,16,19]. SVMs often
struggled—studies[8,14]reported100%trainingaccuracybutjust63%testaccuracy,indi-
catingsevereoverfitting. However,thestudy[19]successfullyemployedahybridmodel
combiningSVMwithNaiveBayes,achieving95.67%accuracy,94.3%precision,and95.65%
recall, outperformingotherclassifiers. Inwork[16], SVMdeliveredstrongprofitability
metrics,rivalingLRinExpectedMaximumProfit.
NeuralNetworks(NN)(includingMLPsanddeeplearning)appearedin[8,14,15,18,20,23,24].
A study [18] reported 96.5% accuracy for a Multilayer Perceptron (MLP), which, while
lowerthanRFandAdaBoost,stillofferedvaluablecomparativeinsights. Inworks[8,14],
deepneuralnetworks(includingTensorFlowmodels)achievedaround82%testaccuracy,
withonemodelidentifyingsubtlechurnsignalslikelowsessionfrequencyandhighpricing.
MLPwasagaintestedin[15],performingadequatelybuttrailingensemblemethodslike
XGBoostandGradientBoostingMachine(GBM).In[24],anon-sequentialNNusingonly
aggregated features yielded lower performance (AUC not specified), underperforming
compared to LSTM-based hybrids. In research [20], sentiment modeling with LSTM
networks produced learned sentiment features from support ticket data, which when
combinedwithmetadatafeatures, ledtoanoticeable+5%increaseinaccuracyandthe
highestrecall,criticalforpredictingsubscriptionrenewals. Single-layerneuralnetworks
wereemployedin[23]achievingAUC=0.987,thoughtheirperformancedegradedover
timeduetostaleness,makingthemlessidealforevolvinguserbehavior.
AdaBoost [44] and other boosting techniques such as GBM [45] were included in
studies[15,18]. AdaBoostin[18]wasthesecond-bestperformerwith98.4%accuracyand
0.995AUC,whilein[15],boostingmethods(especiallyXGBoost)consistentlyoutperformed
simplerclassifiersacrossrecall,AUC,andF1-score.

Appl.Sci.2025,15,6508 12of35
NaiveBayes[46],thoughrarelyatopperformer,wasevaluatedin[8,14,19]. Itper-
formedpoorlywhenusedalonein[8,14](accuracy~69–71%),butin[19],itformedpartof
thehigh-performinghybridmodelwithSVM.
Transformer-basedmodels[47]wereexploredinthestudy[22]. TheFT-Transformer,
builtfortabulardatawithembeddedcategoricalandnumericalfeatures,achieved86.79%
accuracy,88.75%recall,and94.9%AUC—astrongimprovementoverolderworks(AUC
~71–77%),thoughitwasstilloutperformedbyXGBoost(AUC98.8%,F194.81%,accuracy
94.8%)inthesamestudy.
HybridModelswereexploredin[19],whereanSVM-NaiveBayescombinationledto
superiorperformanceacrossallkeymetrics,indicatingthestrengthofensemblelearning
strategies,especiallyinreducingfalsepositives/negativesforCRMapplications. Addi-
tionally,ensembleandhybridarchitectureswerecoreinstudies[20,21,24]. HybridLSTM
architecturescombiningsequentialandstaticaggregateddataoutperformedsingle-source
models [24]. Study [21] introduced the BBE-LSWCM ensemble, integrating LightGBM,
BiLSTM,andLRtoachieve60%betterdecilelift(DL1=3.197)and25%higherAUROC
thanstandaloneBiLSTM,whilemaintainingreasonablelatency.AmodularfusionofLSTM-
learnedsentimentfeaturesandhandcraftedmetadatayieldedthehighestaccuracyand
recall,demonstratingthevalueofcombiningdeeplearningwithtraditionalfeatures[20].
Theresearchersin[26]employedadynamicprogrammingmodeltooptimizeplayer
retention over time alongside a Q-learning algorithm [48] to simulate offline decision-
makingandidentifyconvergencepathsforbothactualandperceivedquality. Theresults
indicatedthatbothgamequalityandperceivedqualitystabilizedathighlevelsregardless
of initial quality. However, the speed of convergence depended on starting conditions,
withlowerinitialquality(x =0.4)taking20periodstoconvergecomparedto14periods
0
forx =0.6. Interestingly,whenplayersinitiallyoverestimatedquality,perceivedquality
0
followeda“high-low-high”trajectory.
Theauthorsof[27]employedaniterativeclusteringapproachstartingwithPCAfor
dimensionalityreductionandK-meansclustering,laterswitchingtoUniformManifold
ApproximationandProjection(UMAP)andHierarchicalDensity-BasedSpatialClustering
ofApplicationswithNoise(HDBSCAN)formoreeffectivehandlingofsparseandnon-
normaldatadistributions. Afterfouriterations,thefinalmodelidentifiedsixmeaningful
personas(e.g.,Uploaders,TVBuilders),whichwerevalidatedthroughinterview-based
triangulation.Earlierclusteringfailedduetooverlappingbehaviorsandsparsedata,butthe
refinedmethodsucceededindifferentiatingusertypesbycombiningbehavioraldatawith
qualitativeinsights. Atlast,inthestudy[28]amoretraditionalmachinelearningapproach
was adopted for behavioral customer segmentation to predict subscription conversion
by evaluating several classifiers, including Decision Tree, K-Nearest Neighbors (KNN),
Naive Bayes, RF, LR, SVC, and XGBoost. Among these, XGBoost achieved the highest
performance,withanaccuracyof79%,precisionof80%,recallof76%,andanF1-scoreof
78%. Cross-validationfurtherconfirmedthegeneralizabilityofthemodelwithamean
scoreof78.5%. However,themodelexhibitedaslightlyhigherrateoffalsenegativesthan
falsepositives,arelevanttrade-offwhenconsideringconversionsensitivity.
Studies[30,32,36]utilizedmachinelearningandstatisticalmodelingtopersonalize
user experience and predict outcomes. Study [30] employed Lasso regression [49] to
personalizefreetriallengths,showinga6.8%subscriptionincreasecomparedtoa30-day
baseline. Simpler uniform policies like a 7-day trial still yielded a 5.59% gain. Among
alternatives, Lasso outperformed random forests and causal forests, which struggled
with overfitting and poor personalization. Similarly, a study [36] implemented logistic
regression, random forest, and gradient boosting for dynamic pricing in usage-based
models. Whilelogisticregressionachievedperfectaccuracyonsimulateddata,real-world

Appl.Sci.2025,15,6508 13of35
applicabilityfavoredgradientboostingandrandomforest,withaccuraciesaround0.77
and0.75,respectively. Study[32]leveragedhierarchicallogisticregressionwithintheCross
IndustryStandardProcessforDataMining(CRISP-DM)frameworktopredictcustomer
retention and cross-buying. Retention prediction reached 93.7% accuracy (F1: 94.38%),
whilecross-buyingwaslesspredictable(accuracy: 78.9%,F1: 20.60%).
Finally,intheworkpresentedin[38],theauthorsusedahierarchicalensembledma-
chinelearningframeworkforpredictingCLVinB2BSaaScompanies. TheCLVprediction
wasframedasalumpsumregressiontaskratherthanatraditionaltime-seriesforecasting
problem,enablingtheuseofrichsupervisedlearningmodelslikeLightGBM,XGBoost,
LASSOregression,KNN,andAutoARIMA.Tohandlelimitedanddriftinghistoricaldata,
atwo-stephierarchicalmodelwasbuilt: firstpredictingoverashorttimehorizon,then
mappingittoalongerhorizon. Theyalsoadoptedanensembleapproach, segmenting
customersbasedonkeyfeatures(likesize)andfittingdifferentmodelsfordifferentgroups
(LightGBMforsmallercustomers,LASSOforenterprises). Inperformancetests,thelump
sumregressionmodelsoutperformedtraditionaltime-seriesmodelsby2to5timesacross
metricslikeRootMeanSquareError(RMSE),MeanAbsoluteError(MAE),andsymmetric
meanabsolutepercentageerror(SMAPE),withLightGBMgivingthebestresults.
Few researchers, however, opted to utilize several methods that rely on statistical,
econometricorheuristicmodels. Indetail,study[34]deployedProcessMining[50],specifi-
callyHeuristicMinerandFuzzyMiner,totrackuserbehaviorsleadingto“Aha! moments”.
Through data cleaning and retention clustering, it identified key activation actions by
reducingmodelcomplexityby62%. However,manualdataprocessingwastime-intensive.
Linear Mixed Models (LMMs) were utilized in [37] to evaluate usage continuance.
It accounted for repeated measures and individual client variability through fixed and
random effects. For existing clients, the model achieved an RMSE of 5.23, though it
struggledwithnewclients(RMSE:13.93),indicatingagapingeneralization. Activation
measures(banners)significantlyincreasedusage(+5.2%).
PLS-SEM(PartialLeastSquaresStructuralEquationModeling)wasemployedin[31]
tovalidatetheeffectofUIdesignonsatisfactionandloyalty. Theresultsshowedstrong
modelreliability(Cronbach’salpha: 0.837–0.860)andhighexplanatorypower(R2~0.50).
Allhypotheses(UIdesign→Satisfaction→Loyalty)werestatisticallysupported.
Focusing on the topic of customer segmentation, the study [25] introduced a joint
modelingframeworkthatcombinedGeneralizedLinearMixedModels(GLMMs)[51]to
trackplayers’in-gamebehavioralpatternswithaSharedParameterModel(SPM)[52]that
linkedthesebehavioralgroupstotheprobabilityofdropout. Thisintegratedapproach
significantlyoutperformedtraditionalmodelslikeCoxregression,improvingretention
predictionby63.2%athigherplayerlevelsandreducingRMSEforlifetimeengagement
by25.5%.
Authorsin[29]tookamoreeconometricroute,applyingaDynamicProbitModel[53]
with copula-based corrections for endogeneity. It incorporated exponentially decaying
goodwillstockstomodelusertouchpointsandusageeffects. Inthisstudyregularization
viaLasso/Ridgeregressionwasalsoutilized,addressingmulticollinearityandimprov-
ing model stability. The study achieved a 9.3% error reduction in predictions and key
findingsemphasizedthatconsumer-initiatedtouchpointsandpersuasivecontentboosted
conversionstopremiumusers,whilefirm-initiatedadshadnegativeeffects.
Study[33]introducedtheAQUAMannegotiationmechanism,combiningquantile
estimation,opponentmodeling,andsurplusredistributiontomanageserviceacceptability.
Underbothnormalandextremeloads(upto2500users/min),itmaintainedhighaccept-
abilityrates(95%+and93.3%,respectively)whilekeepingcostsandoverheadmanageable.

Appl.Sci.2025,15,6508
14of35
Atlast,study[35]outlinedarangeofqualitative(interviews,questionnaires,incident
reports)andquantitative(A/Btesting,in-productsurveysandonlineads,crowdfunding
and crowdsourcing platforms, click-based user data collection) methods deployed for
collectingandintegratingcustomerfeedback,aswellasinsightsintotheirperformance
acrossseveralcompanies. Thisstudyconcludedthatthere’snosingleperfectapproachand
thatthechoiceandsuccessofmethodsdependheavilyonthecompany’ssize,thestructure
oftheproductoffering(customvs. SaaS),thetypeofcustomers(B2Bvs. B2C),thestageof
developmentandtheinternalcommunicationanddataintegrationstructure.
Table2summarizestheresultsregardingtheuseofmachinelearninginthereviewed
approachesforSaaS.
Specifically, Table 2 includes the proposed ML algorithm for the reviewed papers
alongwith the comparedmethods. Resultsaresplit intotwo categories, indicatingthe
mostcommonlyusedmetricsandmiscellaneousacrossthereviewedpapers. Additionally,
informationabouttheuseddatasetsandemployedvalidationmethodsisincluded.
Table2.MachinelearningmethodsusedfordecisionsupportinSaaS(RQ3).
EvaluationResults
| Proposed | Compared |               |               | Validation |         |
| -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref.     |          |               | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
RandomForest:0.997AUC,
0.988Accuracy,
0.989F-measurefor
|     |     | Non-ChurnClassand |     |     | Datasetfroma      |
| --- | --- | ----------------- | --- | --- | ----------------- |
|     |     | 0.981forChurn     |     |     | partnercompany    |
|     |     | NeuralNetworks:   |     |     | associatedwiththe |
Training(64%),
|     | Neural | 0.968AUC,0.965Accuracy, |     |     | Universityof |
| --- | ------ | ----------------------- | --- | --- | ------------ |
Random validation
| [18] | Networks, | 0.975F-measurefor | -   |     | Évora,containing |
| ---- | --------- | ----------------- | --- | --- | ---------------- |
Forest (16%),andtest
|     | AdaBoost | Non-ChurnClassand |     |     | 196,977instances |
| --- | -------- | ----------------- | --- | --- | ---------------- |
(20%)sets
|     |     | 0.946forChurn      |     |     | correspondingto |
| --- | --- | ------------------ | --- | --- | --------------- |
|     |     | AdaBoost:0.995AUC, |     |     | 26,418service   |
|     |     | 0.984Accuracy,     |     |     | subscriptions   |
0.989F-measurefor
Non-ChurnClassand
0.974forChurn
|                 |             | HybridModels:0.8741AUC, |     |               | Datasetfromplayer  |
| --------------- | ----------- | ----------------------- | --- | ------------- | ------------------ |
|                 |             | 0.6953F1-score,         |     |               | logsofafreemium    |
|                 |             | 0.8023Accuracy          |     |               | mobilegame         |
| Hybrid          |             | LSTM:0.8592AUC,         |     |               | developedby        |
|                 | Random      |                         |     | 10-foldcross- |                    |
| [24] Model(LSTM |             | 0.6795F1-score,         | -   |               | TactileGames       |
|                 | Forest,LSTM |                         |     | validation    |                    |
| HiddenState)    |             | 0.7900Accuracy          |     |               | including          |
|                 |             | RandomForest:0.8405AUC, |     |               | 2,284,238recordsof |
|                 |             | 0.6414F1-score,         |     |               | 814,822unique      |
|                 |             | 0.7749Accuracy          |     |               | players            |
Datasetfroma
|     | Logistic | XGBoost:0.7526AUC |     |     | clientSaaS |
| --- | -------- | ----------------- | --- | --- | ---------- |
Regression, RandomForest:~0.5AUC 10-foldcross- companyincluding
| [12] XGBoost |         |                     | -   |            |                    |
| ------------ | ------- | ------------------- | --- | ---------- | ------------------ |
|              | Random  | LogisticRegression: |     | validation | 76,668observations |
|              | Forests | 0.7257AUC           |     |            | of20predictor      |
variables

Appl.Sci.2025,15,6508
15of35
Table2.Cont.
EvaluationResults
| Proposed | Compared |               |               | Validation |         |
| -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref.     |          |               | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
Randomforest:
0.88TrainingAccuracy,
0.87TestAccuracy
DecisionTrees:1.00
Decision
|     |     | (overfitting)Training |     |     | AB2BSaaS |
| --- | --- | --------------------- | --- | --- | -------- |
Trees,
|     |     | Accuracy,0.76TestAccuracy |     |     | subscriptions |
| --- | --- | ------------------------- | --- | --- | ------------- |
Support
|     |     | SupportVectorMachine: |     |     | dataset(source |
| --- | --- | --------------------- | --- | --- | -------------- |
Vector
|     |     | 1.00(overfitting)Training |     | train-testsplit | notmentioned) |
| --- | --- | ------------------------- | --- | --------------- | ------------- |
Random Machine,
| [14] |     | Accuracy,0.63TestAccuracy | -   | (percentagenot | including |
| ---- | --- | ------------------------- | --- | -------------- | --------- |
Forest Neural
|     |     | NeuralNetworks: |     | mentioned) | 7044examplesof |
| --- | --- | --------------- | --- | ---------- | -------------- |
Networks,
|     |     | 0.85TrainingAccuracy, |     |     | B2BSaaS |
| --- | --- | --------------------- | --- | --- | ------- |
NaïveBayes,
|     |     | 0.82TestAccuracy |     |     | subscriptionsand |
| --- | --- | ---------------- | --- | --- | ---------------- |
Logistic
|     |     | NaïveBayes:0.71Training |     |     | 21variables |
| --- | --- | ----------------------- | --- | --- | ----------- |
Regression
Accuracy,0.69TestAccuracy
LogisticRegression:
0.73TrainingAccuracy,
0.71TestAccuracy
XGBoost:0.948Accuracy,
0.9545Precision,
0.9418Recall,
0.9481F1-Score,0.988AUC
|     | Transformer- | Transformer-basedmodels: |     |                 | Datasetfroma   |
| --- | ------------ | ------------------------ | --- | --------------- | -------------- |
|     | basedmodels  | 0.8679Accuracy,          |     | train-testsplit | mobilefreemium |
[22] XGBoost (FT- 0.8477Precision, - (percentagenot gameincludesdata
|     | transformer), | 0.8875Recall,           |     | mentioned) | fromover     |
| --- | ------------- | ----------------------- | --- | ---------- | ------------ |
|     | GBDT          | 0.8671F1-Score,0.949AUC |     |            | 268,370users |
GBDT:0.8561Accuracy,
0.8755Precision,
0.8328Recall,
0.8536F1-Score,0.934AUC
HybridModel:
0.9567Accuracy,
0.943Precision,
0.9565Recall,0.943F1-Score
ANN:0.789Accuracy,
0.8403Precision,
0.8824Recall,
Datasetfrom
0.8608F1-Score
|                 | KNN,         |                            |     |                 | Kagglecontaining    |
| --------------- | ------------ | -------------------------- | --- | --------------- | ------------------- |
| Hybrid          |              | RandomForest:              |     | train-testsplit |                     |
|                 | Random       |                            |     |                 | subscriptiondetails |
| [19] Model(SVM+ |              | 0.8Accuracy,0.79Precision, | -   | (80%            |                     |
|                 | Forest,ANN,  |                            |     |                 | on7044customers     |
| NaïveBayes)     |              | 0.80Recall,0.79F1-Score    |     | train—20%test)  |                     |
|                 | Decisiontree |                            |     |                 | ofafictional        |
KNN:0.839Accuracy,
SaaScompany
0.826Precision,0.829Recall,
0.781F1-Score
DecisionTree:
0.9097Accuracy,
0.9242Precision,
0.9242Recall,
0.9242F1-Score

Appl.Sci.2025,15,6508
16of35
Table2.Cont.
EvaluationResults
|      | Proposed | Compared |               |               | Validation |         |
| ---- | -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref. |          |          |               | Miscellaneous |            | Dataset |
|      | Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
RandomForest:0.916Recall,
0.926F1-Score,
0.92Accuracy,
0.939Precision
|     |     |               | DecisionTree:0.945Recall, |     |     | Datasetextracted  |
| --- | --- | ------------- | ------------------------- | --- | --- | ----------------- |
|     |     | DecisionTree, | 0.871F1-Score,            |     |     | fromthecase-study |
train-testsplit
|     |     | Logistic | 0.845Accuracy, |     |     | company’s |
| --- | --- | -------- | -------------- | --- | --- | --------- |
(80%
|      | Random | Regression, | 0.809Precision      |     |           | databasesystem |
| ---- | ------ | ----------- | ------------------- | --- | --------- | -------------- |
| [13] |        |             |                     | -   | train—20% |                |
|      | Forest | Support     | LogisticRegression: |     |           | containing     |
test),10-fold
|     |     | Vector | 0.868Recall,0.902F1-Score, |     |     | 1788observations |
| --- | --- | ------ | -------------------------- | --- | --- | ---------------- |
crossvalidation
|     |     | Machine | 0.896Accuracy, |     |     | ofchurnand       |
| --- | --- | ------- | -------------- | --- | --- | ---------------- |
|     |     |         | 0.939Precision |     |     | non-churnsamples |
SupportVectorMachine:
0.881Recall,0.839F1-Score,
0.814Accuracy,
0.803Precision
Datasetcollected
fromacloud
serviceprovider
including
NeuralNetworks:
approximately
|      | Neural   |     | 0.9694Accuracy,  |     |             |           |
| ---- | -------- | --- | ---------------- | --- | ----------- | --------- |
| [11] |          | -   |                  | -   | Notprovided | 700unique |
|      | Networks |     | 0.9651Precision, |     |             |           |
cloudservice
0.9540Recall
offering-customer
pairsandaround
90,000associated
supporttickets
XGBoost:0.7956Accuracy,
0.7916Precision,
0.8507Recall,
0.8201F1-Score,
0.86ROCAUC
RandomForest:
0.7877Accuracy,
0.8042Precision,
0.8096Recall,
|     |     | Random | 0.8069F1-Score, |     |     |     |
| --- | --- | ------ | --------------- | --- | --- | --- |
Twodatasets
|     |     | Forest, | 0.85ROCAUC |     |     |     |
| --- | --- | ------- | ---------- | --- | --- | --- |
providedbya
|     |     | Logistic | LogisticRegression: |     |     |     |
| --- | --- | -------- | ------------------- | --- | --- | --- |
Portuguese
|      |         | Regression, | 0.7757Accuracy,  |     |                 |                 |
| ---- | ------- | ----------- | ---------------- | --- | --------------- | --------------- |
|      |         |             |                  |     | train-testsplit | softwarehouse   |
|      |         | Neural      | 0.7986Precision, |     |                 |                 |
| [15] | XGBoost |             |                  | -   | (80%            | withthefinal    |
|      |         | Networks,   | 0.7895Recall,    |     |                 |                 |
|      |         |             |                  |     | train—20%test)  | datasetincluded |
|      |         | AdaBoost,   | 0.7940F1-Score,  |     |                 |                 |
9539observations
|     |     | Gradient | 0.84ROCAUC |     |     |     |
| --- | --- | -------- | ---------- | --- | --- | --- |
fromthetwo
|     |     | Boosting | NeuralNetworks: |     |     |     |
| --- | --- | -------- | --------------- | --- | --- | --- |
datasetscombined
|     |     | Machine | 0.7835Accuracy, |     |     |     |
| --- | --- | ------- | --------------- | --- | --- | --- |
0.7910Precision,
0.8220Recall,
0.8062F1-Score,
0.84ROCAUC
AdaBoost:0.7867Accuracy,
0.7970Precision,
0.8191Recall,
0.8079F1-Score,
0.86ROCAUC

Appl.Sci.2025,15,6508
17of35
Table2.Cont.
EvaluationResults
| Proposed | Compared |               |     |               | Validation |         |
| -------- | -------- | ------------- | --- | ------------- | ---------- | ------- |
| Ref.     |          |               |     | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |     |               | Method     |         |
Metrics
GradientBoostingMachine:
0.7935Accuracy,
0.7946Precision,
0.8402Recall,
0.8167F1-Score,
0.86ROCAUC
RandomForest:
0.88TrainingAccuracy,
0.87TestAccuracy
NeuralNetworks:
|     | Neural    | 0.85TrainingAccuracy, |     |     |     |     |
| --- | --------- | --------------------- | --- | --- | --- | --- |
|     | Networks, | 0.82TestAccuracy      |     |     |     |     |
|     | Decision  | DecisionTree:1.00     |     |     |     |     |
Useractivity
|     | Trees,Logistic | (overfitting)Training |     |     | train-testsplit |     |
| --- | -------------- | --------------------- | --- | --- | --------------- | --- |
Random datasets(source
| [8] | Regression, | Accuracy,0.76TestAccuracy |     | -   | (percentagenot |     |
| --- | ----------- | ------------------------- | --- | --- | -------------- | --- |
Forest andnumberofdata
|     | Support | LogisticRegression: |     |     | mentioned) |     |
| --- | ------- | ------------------- | --- | --- | ---------- | --- |
notmentioned)
|     | Vector     | 0.73TrainingAccuracy, |     |     |     |     |
| --- | ---------- | --------------------- | --- | --- | --- | --- |
|     | Machine,   | 0.71TestAccuracy      |     |     |     |     |
|     | NaïveBayes | SupportVectorMachine: |     |     |     |     |
1.00(overfitting)Training
Accuracy,0.63TestAccuracy
NaiveBayes:0.71Training
Accuracy,0.69TestAccuracy
|     | Neural    | RandomForest:0.997AUC |     |     |     |                 |
| --- | --------- | --------------------- | --- | --- | --- | --------------- |
|     | Networks, | Decisiontree:0.987AUC |     |     |     |                 |
|     | Decision  | NeuralNetworks:       |     |     |     | Datasetfrom“The |
train-test-
|     | Trees,Logistic |     | 0.994AUC |     |     | SettlersOnline |
| --- | -------------- | --- | -------- | --- | --- | -------------- |
validationsplit
|     | Regression, | GradientBoosting: |     |     |     | (TSO)”,afreemium |
| --- | ----------- | ----------------- | --- | --- | --- | ---------------- |
(percentagenot
| Random | Support |                     | 0.984AUC |     |             | onlinestrategy |
| ------ | ------- | ------------------- | -------- | --- | ----------- | -------------- |
| [23]   |         |                     |          | -   | mentioned), |                |
| Forest | Vector  | LogisticRegression: |          |     |             | game,including |
crossvalidation
|     | Machine, |     | 0.967AUC |     |     | 7439usersand |
| --- | -------- | --- | -------- | --- | --- | ------------ |
(foldsnot
|     | NaïveBayes, | SupportVectorMachine: |     |     |     | 113,643observed |
| --- | ----------- | --------------------- | --- | --- | --- | --------------- |
mentioned)
|     | Gradient  |                    | 0.990AUC |     |     | events. |
| --- | --------- | ------------------ | -------- | --- | --- | ------- |
|     | Boosting, | KNN:0.840AUC       |          |     |     |         |
|     | KNN       | NaïveBayes0.887AUC |          |     |     |         |
Datasetfrom
|     | Hybrid |     |     |     |     | QuickBooksOnline |
| --- | ------ | --- | --- | --- | --- | ---------------- |
LightGBM:0.690AUROC,
|     | Models |     |     |     | train-testsplit | (QBO)users, |
| --- | ------ | --- | --- | --- | --------------- | ----------- |
~30minTrainingTime
|               | (Neural     |               |     |     | (500,000 | including           |
| ------------- | ----------- | ------------- | --- | --- | -------- | ------------------- |
| [21] LightGBM |             | HybridModels: |     | -   |          |                     |
|               | Networkwith |               |     |     | records– | 700,000combinations |
0.591AUROC,
|     | BiLSTM |     |     |     | 200,000records) | ofusersand |
| --- | ------ | --- | --- | --- | --------------- | ---------- |
~2hTrainingTime
|     | layers) |     |     |     |     | reference |
| --- | ------- | --- | --- | --- | --- | --------- |
timestamps.
Performance
indexedto
|     | XGBoost, |     |     | LIghtGBM= |     |     |
| --- | -------- | --- | --- | --------- | --- | --- |
1.0×
Gradient
Datasetcollected
|     | boosting, |     |     | LightGBM: |     |     |
| --- | --------- | --- | --- | --------- | --- | --- |
fromawell-known
|               | LASSO       |     |     | 1SMAPE, |             |                |
| ------------- | ----------- | --- | --- | ------- | ----------- | -------------- |
| [38] LightGBM |             |     | -   |         | Notprovided | B2BSaaScompany |
|               | Regression, |     |     | 1RMSE,  |             |                |
(numberofdata
|     | K-nearest- |     |     | 1MAE |     |     |
| --- | ---------- | --- | --- | ---- | --- | --- |
notmentioned)
|     | neighbors, |     |     | XGBoost:    |     |     |
| --- | ---------- | --- | --- | ----------- | --- | --- |
|     | AUTO-Arima |     |     | ~1.10SMAPE, |     |     |
~1RMSE,
~1.1MAE

Appl.Sci.2025,15,6508
18of35
Table2.Cont.
EvaluationResults
| Proposed | Compared |               |               | Validation |         |
| -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref.     |          |               | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
Gradient
Boosting:
~1.2SMAPE,
~1.1RMSE,
~1.2MAE
KNN:
~1.25SMAPE,
~1.2RMSE,
~1.25MAE
LASSO
Regression:
~1.25SMAPE,
~1.1RMSE,
~1.2MAE
AUTO-
Arima:
~1.75SMAPE,
~5RMSE,
~2.5MAE
LASSO
Regression
|     |     |     | reducedMSE |     | Datasetfroma  |
| --- | --- | --- | ---------- | --- | ------------- |
|     |     |     | to0.122    |     | U.S.-based    |
|     |     |     | Dynamic    |     | multinational |
LASSO
|     |     |     | probitmodel |     | computersoftware |
| --- | --- | --- | ----------- | --- | ---------------- |
Regression,
|     |     |     | withcopula |     | companyoperating |
| --- | --- | --- | ---------- | --- | ---------------- |
Dynamic
| [29] | -   | -   | corrections: | Notprovided | onaSoftware-as-a- |
| ---- | --- | --- | ------------ | ----------- | ----------------- |
probitmodel
|     |     |     | −3841 |     | Servicebusiness |
| --- | --- | --- | ----- | --- | --------------- |
withcopula
|     |     |     | Log-Marginal |     | modelincludinga |
| --- | --- | --- | ------------ | --- | --------------- |
corrections
|     |     |     | Density, |     | sampleof     |
| --- | --- | --- | -------- | --- | ------------ |
|     |     |     | 7808.5   |     | 14,989unique |
|     |     |     | Deviance |     | consumers    |
Information
Criterion
LASSO
Regression:
+6.8%
subscriptions
XGBoost:
Datasetfromafully
+6.17%
|            | Random        |     |               |                 | randomized         |
| ---------- | ------------- | --- | ------------- | --------------- | ------------------ |
|            |               |     | subscriptions | train-testsplit |                    |
| LASSO      | Forest,causal |     |               |                 | experiment         |
| [30]       |               | -   | Random        | (70%            |                    |
| Regression | forest,       |     |               |                 | involving          |
|            |               |     | Forests:Poor  | train—30%test)  |                    |
|            | XGBoost       |     |               |                 | 337,724unconnected |
(overfitted
usersglobally
trainingdata)
Causal
Forests:Poor
(minimalper-
sonalization)

Appl.Sci.2025,15,6508
19of35
Table2.Cont.
EvaluationResults
|      | Proposed | Compared |               |               | Validation |         |
| ---- | -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref. |          |          |               | Miscellaneous |            | Dataset |
|      | Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
Logistic
Regression:
1.682TDL,
21,209EMPB
(EUR)
Support
Vector
Machine:
|     |     | Random |     | 1.590TDL, |     |     |
| --- | --- | ------ | --- | --------- | --- | --- |
LogisticRegression:
|      |            | Forest,  |                       | 22,566EMPB |            |                   |
| ---- | ---------- | -------- | --------------------- | ---------- | ---------- | ----------------- |
|      |            |          | 0.604AUC              |            |            | Datasetfroma      |
|      |            | XGBoost, |                       | (EUR)      | cross-     |                   |
|      |            |          | SupportVectorMachine: |            |            | Europeansoftware  |
|      | Logistic   | Decision |                       | Random     | validation |                   |
| [16] |            |          | 0.603AUC              |            |            | serviceprovider   |
|      | Regression | Trees,   |                       | Forest:    | (foldsnot  |                   |
|      |            |          | RandomForest:0.594AUC |            |            | including         |
|      |            | Support  |                       | 11.482TDL, | mentioned) |                   |
|      |            |          | XGBoost:0.599AUC      |            |            | 3959subscriptions |
|      |            | Vector   |                       | 15,106EMPB |            |                   |
DecisionTree:0.523AUC
|     |     | Machine |     | (EUR) |     |     |
| --- | --- | ------- | --- | ----- | --- | --- |
XGBoost:
1.360TDL,
14,351EMPB
(EUR)
DecisionTree:
0.856TDL,
5809EMPB
(EUR)
Random
Forest,
|     |     | Decision | XGBoost:0.79Accuracy, |     |     |     |
| --- | --- | -------- | --------------------- | --- | --- | --- |
Datasetfrom
|     |     | Trees,Logistic | 0.8Precision,0.76Recall, |     |     |     |
| --- | --- | -------------- | ------------------------ | --- | --- | --- |
Kaggle
|     |     | Regression, | 0.78F1-Score |     | train-testsplit |     |
| --- | --- | ----------- | ------------ | --- | --------------- | --- |
(fineTech_appData)
| [28] | XGBoost | Support | Alltheothermethodswhere | -   | (80% |     |
| ---- | ------- | ------- | ----------------------- | --- | ---- | --- |
including
|     |     | Vector | outperformedbuttheir |     | train—20%test) |     |
| --- | --- | ------ | -------------------- | --- | -------------- | --- |
50,000rowsofuser
|     |     | Machine, | specificresultswerenot |     |     |     |
| --- | --- | -------- | ---------------------- | --- | --- | --- |
information
|     |     | K-nearest- | provided |     |     |     |
| --- | --- | ---------- | -------- | --- | --- | --- |
neighbors,
NaïveBayes
RandomForest:
0.09Precision,0.11Recall,
|     |     |     | 0.10F1-Score        |     |     | Datasetfrom       |
| --- | --- | --- | ------------------- | --- | --- | ----------------- |
|     |     |     | LogisticRegression: |     |     | Aircall,aSoftware |
crossvalidation
|      | Random | Logistic   | 0.05Precision,0.57Recall, |     |           | asaService       |
| ---- | ------ | ---------- | ------------------------- | --- | --------- | ---------------- |
| [17] |        |            |                           | -   | (foldsnot |                  |
|      | Forest | Regression | 0.19F1-Score              |     |           | companyincluding |
mentioned)
|     |     |     | Theproposedmodelwas     |     |     | datafromabout |
| --- | --- | --- | ----------------------- | --- | --- | ------------- |
|     |     |     | betteratexplainingchurn |     |     | 5000customers |
drivers(featureimportance)
thanpreciseprediction.
LogisticRegression:
|     |     |     | 1.00Accuracy,            |     |     | Asimulation        |
| --- | --- | --- | ------------------------ | --- | --- | ------------------ |
|     |     |     | 1.00Precision,1.00Recall |     |     | datasetreplicating |
Random
|      |          |            | (duetodatasetsimplicity)   |     |                 | real-world    |
| ---- | -------- | ---------- | -------------------------- | --- | --------------- | ------------- |
|      | Forest,  |            |                            |     | train-testsplit |               |
|      |          | Logistic   | RandomForest:              |     |                 | Softwareasa   |
| [36] | Gradient |            |                            | -   | (80%            |               |
|      |          | Regression | 0.75Accuracy,              |     |                 | Service(SaaS) |
|      | Boosting |            |                            |     | train—20%test)  |               |
|      |          |            | 0.714Precision,0.789Recall |     |                 | usagepatterns |
Machine
|     |     |     | GradientBoostingMachine: |     |     | (numberofdata |
| --- | --- | --- | ------------------------ | --- | --- | ------------- |
|     |     |     | 0.77Accuracy,            |     |     | notmentioned) |
0.753Precision,0.768Recall

Appl.Sci.2025,15,6508
20of35
Table2.Cont.
EvaluationResults
| Proposed | Compared |               |               | Validation |         |
| -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref.     |          |               | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
Datasetscollected
fromfour
|     |     | LogisticRegression: |     |     | databasesat    |
| --- | --- | ------------------- | --- | --- | -------------- |
|     |     | 0.9372Accuracy,     |     |     | Digidata,aSaaS |
Logistic
| [32] | -   | 0.9549Precision, | -   | Notprovided | companywherethe |
| ---- | --- | ---------------- | --- | ----------- | --------------- |
Regression
|     |     | 0.9330Recall,           |     |     | projectwascarried |
| --- | --- | ----------------------- | --- | --- | ----------------- |
|     |     | 0.9438F1-Score,0.999AUC |     |     | out(numberof      |
datanot
mentioned)
4.4. FormofOutputsPresentedtoSaaSProviders
ConcerningRQ4,researcherschoseawidevarietyofmethodstopresenttheirresults
toSaaSprovidersinordertosupportdecision-making. Aslistedbelow,thecategoriesof
thosemethodsinclude:
1. Visualizations
Asignificantnumberofpapersutilizedvisualrepresentationslikeconfusionmatrices,
ReceiverOperatingCharacteristic(ROC)curves,featureimportanceplots,retentioncurves,
sentimentplots,time-seriesgraphsandprocessmaps. Thesevisualshelpnon-technical
stakeholdersquicklygrasppatterns,modelstrengths,andkeyinsights. Theyalsosupport
internalpresentationsandstakeholderalignmentaroundkeymetricsandstrategies.Table3
presentsthevisualizationtechniquesdeployedbythereviewedapproaches.
Table3.Visualizationsfordecision-making(RQ4).
|     | Ref. |     | Visualizations |     |     |
| --- | ---- | --- | -------------- | --- | --- |
[14] Accuracycurvestoshowtheimpactoftreecountsinrandomforests
|     | [22] | AUC-ROCcurvesandconfusionmatricestovalidaterobustness |     |     |     |
| --- | ---- | ----------------------------------------------------- | --- | --- | --- |
[25] Hazardratecurvesandpredictiveintervalsforretentionstatistics
|     | [13] | Featureimportance(e.g.,prevPeriodTrans)viabarcharts |     |     |     |
| --- | ---- | --------------------------------------------------- | --- | --- | --- |
|     | [20] | Temporalsentimentplotstracksatisfactiontrajectories |     |     |     |
[23] ROCcurvesandfeatureplotsthathighlight“misseddays”astoppredictors
[21] (BBE-LSWCM)usesdecileliftchartstoshowa30%churnreductioninA/Btests
|     | [31] | PathanalysisdiagramstomapUIdesigntoloyalty |     |     |     |
| --- | ---- | ------------------------------------------ | --- | --- | --- |
[33] Time-seriesgraphstocompareadaptivevs. non-adaptivenegotiationmodes
[34] Processmapsthatrevealkeyactivationmoment
[37] Trajectoryplotsthatshowactivationimpacts
|     | [16] | Coefficientplotstoillustrateusagedata’simpactonchurn |     |     |     |
| --- | ---- | ---------------------------------------------------- | --- | --- | --- |
[35] Dashboardstoautomatefeedbacksummariesandissueprioritization
[36] Comparativeplotsthatguidemodelselectionviaaccuracy/recallmetrics
2. Simulation/What-IfAnalysis
Simulationtoolsmodelhypotheticalscenarios(e.g.,pricingchanges,triallengths),
enabling SaaS providers to test retention strategies and forecast revenue impact before
implementation, supporting data-driven decision-making. Study [18] enabled “what-
if” scenarios to test the impact of retention strategies like loyalty extensions, helping
providersoptimizeinterventionswhiletheworkpresentedin[25]simulatedpromotional
campaigns, showing a 20% engagement boost from aggressive incentives, and models
premiumpurchasevaluesforrevenueforecasting. Additionally,work[29]testedtiming
strategies,revealingpeakconversionwindows(e.g.,post-trialexpiration)andwarning

Appl.Sci.2025,15,6508 21of35
againstoverusingpersuasivemessagingandstudy[30]comparedtriallengths(7-dayvs.
30-daytrial)throughsimulations,findingshortertrialsoptimalforbeginnersbutlonger
trialsbetterforexperts. Atlast,in[26],theauthorsmodeledplayerretentionunderquality
adjustments, showing that initial quality investments reduced attrition and study [36]
simulateddynamicpricingstrategies,suchasoutcome-basedbilling,toaligncostswith
customervalue.
3. SegmentationandPersonaModeling
Studies[23,28,32,38]usedclusteringandbehavioralanalysistosegmentusersorcreate
personas. These help SaaS providers tailor features, marketing, and support strategies
todistinctusergroupsforbetterengagement. Table4includesthesegmentationgroups
used in those studies. Authors in [25] categorized users based on demographics and
engagementlevels,inthestudy[23]theauthorschosetocategorizetheirusersbytheir
activitypatternswhile[38]chosetogroupusersbyCLV.Additionally, theworkin[27]
createdB2Buserpersonaswhilein[28]theauthorscreatedbehavioralclusters. Finally,the
study[32]segmentedusersbyrelationshiplengthandcross-sellingdependency.
Table4.Segmentationandpersonamodeling(RQ4).
Ref. SegmentationGroups Description
Demographics(gender,geography)and Groupspeopleaccordingtodemographicsand
[25]
engagementlevels engagementlevels
Classifiesplayersbyactivitypatterns,usingloyalty
[23] Activitypatterns(e.g.,“economyoverviewusage”)
markerstotargetinterventions
SegmentscustomersbyCLV,focusingonprioritizing
[38] CustomerLifetimeValue(CLV)
enterpriseclientsforretention
Createsuserpersonaswithpainpointsandworkflow
[27] B2Buserpersonas(e.g.,“DataSellers”)
metricstoguideproductdevelopment
Identifiesbehavioralclusters,suchas
[28] Behavioralclusters(e.g.,education-focusedusers)
education-focusedusers,fortargetedmarketing
[32] Relationshiplengthandcross-sellingdependency Segmentsbyrelationshiplength
4. BusinessImpactMetrics
Metrics like CLV, MRR and ROI can be used to quantify churn effects. This en-
ablesproviderstounderstandthefinancialimplicationsofretentioneffortsandprioritize
high-value customer segments. For instance, study [18] reported cost savings per re-
tainedcustomerandrevenueprotectionthroughchurnreduction,whiletheworkin[14]
demonstratedROIimprovementsviadynamicpricingstrategies. Earlychurndetection
andassociatedacquisitioncostreductionswerehighlightedinstudy[19]andstudy[25]
showcasedarevenueboostfromcollaboration-drivenmonetizationmodels. Furthermore,
studiessuchas[8,21]focusedonreducingnegativeMRRchurnandincreasingintervention
acceptancethroughA/Btesting,respectively. ThepredictionofCLVandtheapplication
ofmarginalROIformulaswereaddressedinthework[38],whereasthestudy[30]illus-
tratedhowoptimizedfreetrialstrategiescouldenhancebothretentionandrevenue. In
addition,study[26]linkedqualityinvestmentcoststogainsinnetwork-drivenretention,
and study [16] evaluated predictive accuracy in relation to carbon emissions. Studies
like[36]connectedusage-basedbillingmodelstoamarkedincreaseincustomersatisfac-
tion,while[32]quantifiedretentiondifferencesacrosscountries,providingfurtherinsights
into localization strategies. Table 5 summarizes the business metrics employed by the
reviewedapproaches.

Appl.Sci.2025,15,6508 22of35
Table5.Businessimpactmetrics(RQ4).
Ref. BusinessMetrics
[18] Costsavingsperretainedcustomer,revenueprotectionfromchurnreduction
[14] DynamicpricingROI
[19] Churnratesfromearlydetection,acquisitioncostreduction
[25] Revenueboostfromcollaboration-basedmonetization
[8] NegativeMRRchurnandCLV
[21] ChurnreductionandinterventionacceptanceinA/Btests.
[38] MarginalROIformulas
[30] Improvedretentionandrevenue
[26] Qualityinvestmentcostsagainstnetwork-drivenretentiongains.
[16] Predictiveaccuracyagainstcarbonemissions
[36] Customersatisfaction
[32] Country-specificretentiondifferences
5. ModelDeploymentandIntegration
Model deployment integrates predictive models into SaaS platforms via APIs or
cloudpipelines,enablingautomatedchurnpredictionandalignmentwithCRMfeatures.
Buildingonthis,CRMandmarketingtoolsusetheseinsightstopersonalizecampaigns
basedonchurnriskoruserbehavior. Additionally,toolkitsandinteractivesystemssup-
portscenariotestingandonboardinganalysis,helpingteamsrefinestrategiesandmake
data-drivendecisions.
For instance, the work in [30] integrated RESTful APIs and the CBAR platform to
deliverJSON-formattedreal-timeriskscores,enhancingboththespeedandaccuracyof
predictions. Centralized Bank Account Register (CBAR) not only ranked subscriptions
by risk and value but also enabled targeted actions based on live insights. Similarly,
study[12]proposedastandaloneappthatsupporteddynamicthresholdingandfeedback
loops,allowingcontinuousmodelrefinement,andintroducedatoolofferinglivechurn
predictions for real-time decision-making. This study also highlighted declining login
activityasanearlywarningsignandrecommendsdynamicthresholdadjustmentbasedon
marketingcapacity.
Severalotherstudiesproposedadditionalenhancements. Asshownin[21]anAWS
SageMakerpipelinewasutilizedtosupportbothbatchandreal-timefeaturization,enabling
flexibledataprocessing, andtriggeredchatpop-upsforhigh-riskuserstofosterimme-
diate engagement. Study [16] recommended leveraging cloud storage and algorithmic
optimizationstoreduceenvironmentalimpact,whilework[36]providedpseudocodefor
integratingreal-timedatastreamswithbillingsystems.
Moreover,theworkin[24]alignedpredictivemodelswithtargetedre-engagement
strategiesforat-riskusers,while[19]fine-tunedretentioncampaignsbybalancingpreci-
sionandrecall,anddesignedhybridmodelstoensurescalabilityforclouddeployment.
Study[29]optimizedconversionratesthroughstrategicadplacementsandprecisetiming
ofmessaging. Study[17]ensuredthatkeyfeatureusagedataissyncedwithCRMsystems
andflagslow-usageaccountsforproactivecustomersuccessoutreach.
Dashboardsandinteractivesystemsalsoplayacriticalsupportingrole. Study[15]pre-
sentedadashboardthatvisualizeschurnriskmetricsandintegratesreal-timealertsdirectly
intoCRMdashboards,ensuringthatteamscanactswiftlyoncriticalissues. Study[15]
offeredaprocessminingtoolkitthatuncovers“Aha!”momentsduringonboarding,en-
hancinguseractivationefforts. Finally,authorsin[35]proposedanautomatedfeedback
systemthatprioritizescriticaluserissuesandprovidesdashboardsthatvisualizefeedback
trends,helpingteamsmonitorusersentimentandbehaviorpatternsovertime.

Appl.Sci.2025,15,6508 23of35
5. Discussion
InresponsetoRQ1,theanalysisrevealedthatchurnpredictionisthemostfrequently
pursuedobjectiveindecisionsupportsystemsinSaaSsettings. Studiesconsistentlyempha-
sizedtheimportanceofidentifyingearlyat-riskusersinordertointerferewithdata-driven
strategies,thereforeimprovingsubscriptioncontinuanceandreducingrevenueloss. Be-
yondchurn,researchersalsocontributedsignificantlythroughusersegmentation,which
enablesthegroupingofcustomersintomeaningfulbehavioralordemographicclusters.
Thissupportspersonalizedproductdevelopment,targetedmarketing,andmoreresponsive
customerservice. Otherstudiesfocusedonimprovinguserengagementandpredicting
CLV,whicharekeyindicatorsforlong-termbusinesssustainability. Additionally,strategic
decisionsaroundpricingoptimization,freetrialpolicies,andonboardingpracticeswere
offeredsothatSaaSprovidersareaidedinaligningservicedesignwithactualuserbehavior
andexpectations.
Regarding RQ2, this survey revealed that for the effectiveness of decision-making
in SaaS environments, diverse and rich datasets must be used. In most studies, behav-
ioral data, such as clickstream logs, feature usage, and session frequency, emerged as
foundational. These were often combined with transactional and subscription-related
information,includingbillinghistoryandaccounttenure, toprovideafullerpictureof
userengagement. Studiesalsomadeuseofdemographicandfirmographiccharacteristics,
allowingforsegmentationbyindustry,companysize,orgeographiclocation.Insomecases,
sentiment data from support tickets or survey responses were incorporated to capture
users’subjectiveexperiences. Afewstudiesemployedsyntheticorsimulateddatatotest
hypotheticalscenariosandoptimizeinterventionstrategiesbeforedeployment. Altogether,
theresultsunderscoretheimportanceofintegratingbothquantitativesystemusagemetrics
andqualitativefeedbackforcomprehensivedecisionsupport.
AddressingRQ3,itwasfoundthatmachinelearningtechniquesplayacentralrolein
nearlyalltheexaminedimplementations. RFandXGBoostwerethemostcommonlyused
algorithms,andtheyconsistentlydeliveredstrongperformanceacrossvariousevaluation
metrics such as AUC, precision, recall, and F1-score. These models were particularly
effectiveinhandlinghigh-dimensional,tabulardatasetsandofferedabalanceofaccuracy
andinterpretability. Inmorecomplexscenariosrequiringtemporalmodelingorbehavioral
pattern recognition, hybrid and ensemble models outperformed traditional classifiers.
For example, combinations of LSTM networks with LightGBM or structured metadata
inputscapturedsequentialuserbehaviormoreeffectivelythanstaticmodelsalone. While
simplermodelslikeLRandDTprovidedusefulbaselines,theirperformancewasoften
eclipsedbyensembleordeeplearningapproaches. Notably,somestudiesconsideredthe
environmentalimpactandscalabilityofdifferentalgorithms,highlightingtherelevance
ofcomputationalefficiencyandcarbonfootprintinmodelselection. Overall,thechoice
ofmethodwasshowntodependonspecifictaskrequirements,datacharacteristics,and
operationalconstraintssuchaslatencyormodeltransparency.
Finally,inresponsetoRQ4,awidevarietyofoutputtypeswerepresentedtoinform
andguideSaaSproviders. Theimportanceofvisualanalyticswashighlighted,including
ROCcurves, featureimportancerankings, anduserbehaviormaps, whichhelpednon-
technicalstakeholdersinterpretmodeloutcomes. Business-orientedmetricssuchasCLV,
MRR,andROIlinkedpredictionstofinancialoutcomeswhilesimulationtoolsallowed
providerstoexperimentwithtrialdurationsorpricingadjustmentsbeforeactualimple-
mentation, enhancing the strategic value of the DSSs. Furthermore, user segmentation
andpersonamodelingenabledmoredetailedtargetingofuserengagementandmarketing
strategies,whileprocessminingtechniquesuncoveredcriticalactivationpatternssuchas
thediscoveryofan“ahamoment”.

Appl.Sci.2025,15,6508
24of35
Somestudiesalsofocusedonmodeldeploymentstrategies,emphasizingcloudinte-
grationandscalability. Bybridgingpredictiveanalyticswithtangiblebusinessinsightsand
strategictools,DSSoutputswereshowntohaveadirectimpactonoperationalefficiency,
customersatisfaction,andlong-termprofitability. Moreover,deployingsuchmodelsas
churnpredictiononesthroughthecloudoffersthepossibilityofprovidingMachineLearn-
ingasService(MLaaS)modelsspecializedforsupportingdecision-makinginSaaS.On
thesamepage,research[54]presentedanMLaaSsolutionformarketingthatcontaineda
churnpredictionmodeltestedinretailande-commercesettings.
Tosynthesizethefindingsdiscussedinthisreviewandprovideaclearerunderstand-
ingoftheresearchlandscape,Table6presentsthemaininsightsandfindingscorresponding
toeachresearchquestion(RQ1–RQ4)addressedinthisstudy. Table6offersacompact
overviewofthefocusareas,typesofdataused,appliedmachinelearningmethods,and
thenatureofdecisionsupportoutputsinSaaSenvironments.
Table6.Cumulativetable,findingsofRQ1–RQ4.
| Ref. | Focus | Data | ProposedMethod | Output |
| ---- | ----- | ---- | -------------- | ------ |
Simulation/What-If
Analysis,BusinessImpact
Usagebehavior,customer
| [18] Churnprediction |     |     | RandomForest | Metrics,Model |
| -------------------- | --- | --- | ------------ | ------------- |
profile,financial
Deploymentand
Integration
|                      |     |               | HybridModel       | ModelDeployment |
| -------------------- | --- | ------------- | ----------------- | --------------- |
| [24] Churnprediction |     | Usagebehavior |                   |                 |
|                      |     |               | (LSTMHiddenState) | andIntegration  |
Usagebehavior,
|                      |     | customerprofile,       |         | ModelDeployment |
| -------------------- | --- | ---------------------- | ------- | --------------- |
| [12] Churnprediction |     |                        | XGBoost |                 |
|                      |     | transactional/business |         | andIntegration  |
metrics
Usagebehavior,
Visualizations,Business
| [14] Churnprediction |     | transactional/business | RandomForest |     |
| -------------------- | --- | ---------------------- | ------------ | --- |
ImpactMetrics
metrics
| [22] Churnprediction |     | Usagebehavior | XGBoost | Visualizations |
| -------------------- | --- | ------------- | ------- | -------------- |
BusinessImpactMetrics,
|                      |     | Usagebehavior,  | HybridModel(SVM |                 |
| -------------------- | --- | --------------- | --------------- | --------------- |
| [19] Churnprediction |     |                 |                 | ModelDeployment |
|                      |     | customerprofile | +NaïveBayes)    |                 |
andIntegration
Visualizations,
Simulation/What-If
Usagebehavior,
| [25] Churnprediction |     |     | CoxRegression | Analysis,Segmentation |
| -------------------- | --- | --- | ------------- | --------------------- |
customerprofile
andPersonaModeling,
BusinessImpactMetrics
Usagebehavior,
customerprofile,
| [13] Churnprediction |     |     | DecisionTrees | Visualizations |
| -------------------- | --- | --- | ------------- | -------------- |
transactional/business
metrics
[20] Churnprediction Customersupport NeuralNetworks Visualizations
|                      |     | Usagebehavior,customer  |         | ModelDeployment |
| -------------------- | --- | ----------------------- | ------- | --------------- |
| [15] Churnprediction |     |                         | XGBoost |                 |
|                      |     | profile,customersupport |         | andIntegration  |
Usagebehavior,
[8] Churnprediction transactional/business NeuralNetworks BusinessImpactMetrics
metrics,customerprofile

Appl.Sci.2025,15,6508
25of35
Table6.Cont.
| Ref. | Focus | Data | ProposedMethod | Output |
| ---- | ----- | ---- | -------------- | ------ |
Visualizations,
[23] Churnprediction Usagebehavior RandomForest Segmentationand
PersonaModeling
Visualizations,Business
|      |                 | UsageBehavior,  |          | ImpactMetrics,Model |
| ---- | --------------- | --------------- | -------- | ------------------- |
| [21] | Churnprediction |                 | LightGBM |                     |
|      |                 | customerprofile |          | Deploymentand       |
Integration
|      |                 | Usagebehavior,           |                    | Visualizations,Business |
| ---- | --------------- | ------------------------ | ------------------ | ----------------------- |
|      |                 | transactional/business   |                    | ImpactMetrics,Model     |
| [16] | Churnprediction |                          | LogisticRegression |                         |
|      |                 | metrics,customerprofile, |                    | Deploymentand           |
|      |                 | customersupport          |                    | Integration             |
Usagebehavior,
|      |                 | transactional/business |              | ModelDeployment |
| ---- | --------------- | ---------------------- | ------------ | --------------- |
| [17] | Churnprediction |                        | RandomForest |                 |
|      |                 | metrics,customer       |              | andIntegration  |
profile,satisfaction
Usagebehavior,
Segmentationand
|      | Customerlifetime | transactional/business |          |                  |
| ---- | ---------------- | ---------------------- | -------- | ---------------- |
| [38] |                  |                        | LightGBM | PersonaModeling, |
|      | value            | metrics,customer       |          |                  |
BusinessImpactMetrics
profile,financial
Visualizations,
Simulation/What-If
Customerlifetime Transactional/business Analysis,BusinessImpact
| [36] |       |                   | RandomForest |               |
| ---- | ----- | ----------------- | ------------ | ------------- |
|      | value | metrics,financial |              | Metrics,Model |
Deploymentand
Integration
Simulation/What-If
Analysis,Model
| [29] | Userengagement | marketing/trials | LASSORegression |     |
| ---- | -------------- | ---------------- | --------------- | --- |
Deploymentand
Integration
Visualizations,Model
Heuristicand
| [34] | Userengagement | Usagebehavior |     | Deploymentand |
| ---- | -------------- | ------------- | --- | ------------- |
FuzzyMining
Integration
Simulation/What-If
Usagebehavior,
| [30] | Userretention |     | LASSORegression | Analysis,Business |
| ---- | ------------- | --- | --------------- | ----------------- |
survey/interview,marketing
ImpactMetrics
Simulation/What-If
Reinforcement
[26] Userretention Customerprofile,satisfaction Analysis,Business
learning
ImpactMetrics
Usagebehavior,customer
| [37] | Userretention |     | LinearMixedModels | Visualizations |
| ---- | ------------- | --- | ----------------- | -------------- |
profile,survey/interview
PLS-SEM(Partial
User
|      |                   | Usagebehavior,customer   | LeastSquares       |                |
| ---- | ----------------- | ------------------------ | ------------------ | -------------- |
| [31] | satisfaction/user |                          |                    | Visualizations |
|      |                   | profile,survey/interview | StructuralEquation |                |
loyalty
Modeling)
|     | User |     | AQUAman |     |
| --- | ---- | --- | ------- | --- |
[33] satisfaction/user Usagebehavior,satisfaction negotiation Visualizations
|     | loyalty |     | mechanism |     |
| --- | ------- | --- | --------- | --- |

Appl.Sci.2025,15,6508 26of35
Table6.Cont.
Ref. Focus Data ProposedMethod Output
User Usagebehavior,customer Visualizations,Model
Comparative
[35] satisfaction/user support,satisfaction, Deploymentand
analysis
loyalty survey/interview Integration
User Usagebehavior, Segmentationand
[32] satisfaction/user transactional/business LogisticRegression PersonaModeling,
loyalty metrics,marketing BusinessImpactMetrics
Usagebehavior, UMAPand Segmentationand
[27] Usersegmentation
survey/interview HDBSCAN PersonaModeling
Usagebehavior,
Segmentationand
[28] Usersegmentation transactional/business XGBoost
PersonaModeling
metrics
5.1. InsightsandStrategicRecommendations
From many of the reviewed systems derived various actionable predictions and
recommendations, such as identifying customers at high risk of churning, estimating
potentialrevenueloss,oradvisingonoptimalpricingstrategies. Oneofthemostconsistent
themesacrossresearchwastheuseofmachinelearningtoflagcustomerslikelytochurn.
Studiessuchas[14]concludedthatnewerB2Bcustomersareparticularlyvulnerableto
churn,whilethosewithlowmonthlypaymentsoftenexhibithigherloyalty,suggesting
thatrandomforestsarewell-suitedforB2BSaaSduetotheirinterpretabilityandscalability.
Pricingstrategiesalsoplayapivotalroleinuserretention. Forinstance,research[36]
concludedthatasignificantpercentageofusersprefertransparentbillingandproposeda
dynamicpricingformulathatfactorsinbaserates,usagemetrics,andriskadjustments.The
studyrecommendedgradientboostingforcomplexpricingenvironmentswheretraditional
modelsmayfallshort. Additionally,research[32]revealedthatmulti-productsubscrip-
tionsimprovedretentionbutcautionedagainstover-relianceonbundling,notingregional
variationsinloyalty. Furthersupportingpricingadjustments,research[8]identifiedthat
highfeescombinedwithlowsessionactivitystronglycorrelatewithchurn,suggestingthat
SaaSprovidersshouldconsiderflexiblepricingforlow-engagementusers.
Additionally,otherresearchersproposedbest-practicepolicies,liketrialdurations,
onboardingflows,andpricingtactics,tohelpSaaSprovidersalignproductdecisionswith
userbehaviorandretentiontrends. Study[30]recommendeddefaultingto7-daytrials
unlesssegmentationsuggestslongerones,whileauthorsof[31]highlightedthatintuitive
UI design can boost satisfaction and increase loyalty by 41%. Additionally, work [26]
advisedgradualqualityadjustmentstobettermatchuserperceptions,andwork[33]set
performancebenchmarkssuchas90%acceptabilityratesinnegotiationsystems. Onboard-
ing strategies, according to [34], should center around key activation points, while the
workpresentedin[37]encouragedCRM-styleengagement,includingintranetbanners,to
maintainuserinvolvement.
In[22]theauthorsdemonstratedthatearlyonboardingmetricsarestrongpredictors
oflong-termretention. Thestudyachievedan88.75%recallrateinpredictingpost-tutorial
churn,underscoringtheimportanceofmonitoringearlyuserbehavior. Similarly,thework
presented in [20] linked negative sentiment in support tickets to churn, advocating for
sentimentanalysisalongsideusagelogstocreateariskassessmentframework. Inanother
study[19],theauthorsfoundthatlowAPIorintegrationusageandinfrequentsupport
interactions are reliable churn signals, making these metrics essential for prioritizing
retentionefforts.

Appl.Sci.2025,15,6508 27of35
Otherresearch[13,23]highlightedthatselectingtherightmachinelearningmodel
iscrucialforeffectivechurnpredictionhighlightingthetrade-offsbetweendifferentap-
proaches. Forexample,theauthorsin[13]compareddecisiontreesandrandomforests,
findingthatdecisiontreesexcelinrecall,makingthemidealforminimizingmissedchurn
risks,whilerandomforestsofferbetterF1-scores,whichmaybepreferablewhenbalancing
precision and recall. Meanwhile, research [23] achieved near-perfect predictive perfor-
mancewithanAUCofapproximately0.99butwarnedagainstneuralnetworksdueto
theirtendencytodegradeovertimewithoutfrequentretraining. Ontheoperationalside,
authors in [16] highlighted the computational cost of XGBoost, noting that it produces
335%higheremissionsthanlogisticregression,andrecommendedcloud-basedsolutions
forscalabilityandefficiency.
Measuring the financial impact of churn ensures that retention efforts align with
businessobjectives. Theworkpresentedin[38]demonstratedhowCLVpredictionscan
optimizebudgetallocation,ensuringmarketingspendingtargetshigh-valueusers.Another
key insight comes from [29], which found that organic search ads outperformed email
campaignsindrivingconversions,cautioningagainstoverlyaggressiveretentiontactics
thatmayalienateusers.
Finally,theimportanceofaddressingcomputationaldemandsandsustainabilityin
SaaSsystemswashighlightedbystudies[14,16,19,36]. Keyrecommendationsincluded
optimizing models for cloud deployment, minimizing carbon footprints, and ensuring
scalableinfrastructureforreal-time,high-volumeapplications. Forinstance, study[14]
pointedoutthesignificantcomputationalrequirementsofdeeplearningmodels,particu-
larlyforlargefirms. Inaddition,theauthorsin[19]focusedondesigningmodelssuitedfor
cloud-basedSaaSenvironments,whileinstudy[16]theauthorsevaluatedtheenvironmen-
talimpact,specificallythecarboncost,ofmodeltraining. Tosupportscalability,authors
in[36]recommendedhybridcomputingapproaches,especiallyforhigh-demandsystems
likebilling.
5.2. SelectionofOptimalMachineLearningModelforDecision-Making
Selectingtheoptimalmachinelearningmodeldependsonthespecificusecase. The
initialdecisionforaSaaSprovideristodeterminetheprimarybusinessobjectivedriving
the need for machine learning. If the goal is the churn prediction, which is the most
frequentlycitedusecase,theprovidershouldassesswhethertheirdatasetconsistsprimarily
of structured behavioral and transactional data. If the data is rich in clickstream logs,
usersessions,orsubscriptiondata,ensemblemodelssuchasRandomForestorXGBoost
standoutduetotheirstrongperformanceinpredictiveaccuracyandfeatureimportance
insights. Thesemodelsareparticularlyeffectivewheninterpretabilityandscalabilityare
important,especiallyinBusiness-to-Business(B2B)contextswhereclearjustificationfor
churnpredictionsisessential.
However,inusecaseswhereuserbehaviorevolvesovertime,forinstance,infreemium
gamesorSaaSproductswithhighsessionvariability[23],hybridarchitecturesthatintegrate
static and time-dependent features into LSTM networks (such as subscription age or
paymenthistory)shouldbeconsidered. Thesemodelsbettercapturetemporaldynamics
and early disengagement signals but at the cost of increased complexity and training
resources. ForSaaSvendorsrequiringreal-timedeploymentorlow-latencypredictions,
LightGBMoffersacompellingbalancebetweenperformanceandcomputationalefficiency
andisespeciallysuitableforstreamingcontextsorintegrationintocloud-basedplatforms.
Forusecasesfocusingonusersegmentation,wherethegoalistogroupusersinto
interpretablepersonasorstrategicmarketinggroups,thenatureoftheinputdataplays
apivotalrole. Ifthedataincludesdemographic,firmographic,andbehavioralattributes,

Appl.Sci.2025,15,6508 28of35
thentraditionalclusteringmethodslikeK-meansarepreferredforidentifyingmeaningful
segments,especiallywhenenhancedwithdimensionalityreductiontechniquessuchas
UMAPorHDBSCANtohandlesparsedatasets[26]. Theseapproachessupportexploratory
analysisandarevaluablewhenstrategicalignmentwithqualitativeinsightsfromsurveys
orinterviewsisrequired.
ForpredictingCLVinB2Benvironments,wherehistoricalbillingdata,engagement
metrics,andfirmographicfeaturessuchascompanysizeorindustryplayacriticalrole,
hierarchicalensemblemodelssuchasLightGBMwereparticularlyeffective. Thesemodels
deliverstrongpredictiveaccuracyandcanbepairedwithtime-seriestechniqueslikeAuto
ARIMAtocapturerevenuetrendsacrossdifferentcustomersegments[37]. Additionally,
LASSOregressionwasappliedinthiscontexttoenhancemodelinterpretabilityandstability
byselectingkeypredictivefeaturesinhigh-dimensionaldatasets. Thisapproachallows
SaaSproviderstoidentifyandprioritizehigh-valueaccounts,allocatemarketingresources
moreefficiently,andoptimizelong-termrevenuestrategies.
Ifthefocusisonuserengagement,satisfaction,orloyalty,thedecisionisagainbased
on the type of available data. For use cases involving UI/UX feedback, support ticket
sentiment,oronboardingflows,vendorsshouldconsiderdeeplearningmodels(likeMLP
orsentiment-enhancedLSTM)onlyiftheyhavelargedatasetsandneedtoidentifysubtle
trends. Forsmallerdatasetsorwhenmodelexplainabilityisprioritized,logisticregression
orPLS-SEMmodelsprovideinterpretableinsightsandcanbeusedtoconnectinterface
designorfeatureadoptiontoengagementmetrics.
Whenthebusinessobjectiverevolvesarounddynamicpricingortrialoptimization,
wherescenariotestingandprofitabilityforecastingarekey,modelsmustsupportwhat-if
simulations and business impact metrics. In these cases, gradient boosting techniques
(XGBoost,GBM),orLASSOregressionareoptimalduetotheirabilitytomodelnonlinear
relationshipsandprovidestablecoefficientsforstrategicleversliketrialdurationorusage-
basedpricing. SaaSplatformsfeaturingdynamicpricingmodelsmayalsobenefitfrom
reinforcementlearningtoadjustpricesinresponsetouserbehaviorandnetworkeffects
overtime.
Finally,forthechoiceoftheappropriatemachinelearningmodel,deploymentand
sustainabilityconstraintsshouldbeconsidered. ForSaaSvendorswithlimitedengineering
capacity or requiring real-time predictions integrated into CRM systems, models like
RandomForest,XGBoost,orLightGBMcanbedeployedviaRESTAPIsorembeddedin
cloudMLpipelines(asinAWSSageMaker).Additionally,inenergy-sensitiveenvironments,
vendorsshouldprefercomputationallylightweightmodelsandmonitorcarbonemissions,
asstudiesshowedlargeenvironmentalvariancesbetweenarchitectures.
Although the primary focus of the reviewed papers was on the performance and
utility of data-driven decision support systems in SaaS, interpretability was also a key
considerationinseveraloftheexaminedstudies.Forinstance,paper[15]employedLogistic
Regression, a model valued for its transparency, and visualized its coefficients to help
stakeholdersunderstandhowdifferentusagefactorsaffectchurnpredictions. Likewise,
the paper [16] emphasized explainability by analyzing feature importance in Random
ForestandLogisticRegressionmodelstorevealkeychurndrivers,evenwhenpredictive
performancewasmodest. Otherstudiessuchas[12,13,22]alsousedinterpretablemodels
(such as Decision Trees) or feature importance plots to support decision-making with
understandableinsights.
Figure4illustratestherecommendedactionsforselectingtheoptimalMLmodelbased
onthespecificusecaseandcontextasderivedfromtheresultsofthereviewedpapers.

Appl.Sci.2025,15,6508 29of35
Figure4.TaxonomyforMLalgorithmsselectionforSaaSproviders.
However, explainability techniques such as SHAP (SHapley Additive exPlana-
tions)[55]orLIME(LocalInterpretableModel-agnosticExplanations)[56]werenotem-
ployed by the reviewed papers. SHAP is a method used to explain the output of any
machinelearningmodelbyquantifyingthecontributionofeachinputfeaturetoaspecific
prediction. ItutilizestheconceptofShapleyvaluesfromgametheorytodeterminethe
importanceofeachfeature. LIMEisaninterpretationtechniqueusedtoexplainthepredic-
tionsofanyblackboxmachinelearningmodel. LIMEapproximatesacomplexmodel’s
predictionwithasimpler,interpretablemodel,focusingonindividualpredictionsrather
thanthemodelasawhole. ThechoicebetweenSHAPandLIMEdependsonthespecific
needsofthetask. SHAPisidealwhenaccuracy,consistency,andfairnessarepriorities,
especially in regulated settings or with tree-based models like XGBoost. LIME, on the
other hand, is useful for quick, model-agnostic explanations during development, and
works well with various data types. Its simplicity makes it great for explaining results
to non-technical users. Ultimately, the adoption of such techniques could significantly
improvestakeholderconfidenceinautomateddecisionsandsupporterrordiagnosis,bias
detection,andregulatorycompliance.
Moreover,explicitconsiderationsofalgorithmicfairness,privacyprotection,orethical
implications seem to be largely absent. Future research should address those gaps by
incorporatingsuchexplainabilitytechniquesintomachinelearningmodelsandconsider
theincorporationofprivacy-preservingtechniquessuchasdifferentialprivacy[57],feder-
atedlearning[58]andsecuremulti-partycomputation,whichcanenablemodeltraining
on sensitive user data without compromising user confidentiality. Additionally, incor-
poratingalgorithmicfairnessassessmentsintothedevelopmentpipelinecouldprevent
discriminatoryoutcomessuchasbiasedchurnpredictions. AsSaaSsolutionsincreasingly
influencestrategicdecisionslikemarketing,pricing,orretentioninvestments,itiscritical
to ensure that automated recommendations do not reinforce inequalities or introduce
unfairtreatment.
Even though carbon footprint should be taken into consideration, only two stud-
ies [13,15] measured how machine learning model selection affects carbon emissions.
Study[15]examinedtheenvironmentalimpactofmachinelearninginB2Bchurnpredic-

Appl.Sci.2025,15,6508 30of35
tion,analyzingthetrade-offsbetweenmodelaccuracyandcarbonemissions. Usingan
AMDEPYC7763processor(280W)andEuropeanemissionsdata(296.96gCO /kWh),
2
theresearchquantifiedCO eqemissionsinrelatableterms. Theresultsrevealedthateven
2
basicpreprocessing,suchasfeaturecreation,emits86.379gCO eq,whilemodeltraining
2
introducedfargreatercosts. Theinclusionofmultipleusagefeaturesresultinginahigh
dimensionaldataset,significantlyaffectedthecarbonfootprintproducedbythereviewed
machine learning methods. Specifically, Decision Trees and Random Forests showed a
~200%riseinemissions(DT:2.349gCO eqto4.044g;RF:1.350gto4.044g). XGBoost’s
2
emissions rose by 335% (21.29 g CO eq), and SVM increased by 50% (40.99 g CO eq),
2 2
whereasLogisticRegressionremainedefficient(2.349gCO eq).
2
However,themoststrikingenvironmentalcostsseemedtoderivefromdeeplearn-
ingandcomplexensemblemethods. Instudy[13],aDeepNeuralNetwork(DNN)with
twohidden layers (32/64 neurons) achieved a high accuracy percentage but at a high
computationalexpense,scalingconsiderablyasmodelcomplexionincreased. Similarly,
RandomForestprovedresource-intensive,withcostsgrowingalongsidetreedepthand
featurecomplexity. BothDNNandRFrequiredparallelcomputationtotrainefficiently
andusedupalloftheavailableprocessorsindicatingtheirhighresourceconsumptionin
comparisonwiththerestofthereviewedmodels. Althoughadvancedmodelsseemedto
improveprediction,theirenergydemandsmakethemunsustainableforfirmswithoutop-
timizedinfrastructure. Thestudyconcludedthatbusinesses,especiallysmallerenterprises,
should prioritize energy-efficient algorithms (like Logistic Regression) or cloud-based
solutionstoreduceenvironmentalimpact.
Although several of the reviewed studies experimented with deployment aspects,
suchasstandalonereal-timeapplications[5],CRM-integrateddashboardsfordecisionsup-
port[14],cloud-basedpredictionAPIs[29],andreal-timedatastreamingusingplatforms
like AWS SageMaker [20], these efforts primarily emphasize centralized, cloud-centric
architectures. Anemergingdirectionforreal-worlddeploymentofdecisionsupportsys-
tems in SaaS would involve combining centralized model training with decentralized
inferencethroughedgecomputing[59],particularlyinsettingsinvolvingIoTdevicesor
localclients. Followingthis,machinelearningmodelsaretrainedinthecloud,oftenvia
MLaaSplatformsthatprovidescalablecomputingresources,versioningandmonitoring,
andthendeployedtoedgedevicesforlocalinference. Thisapproachcouldpotentiallyoffer
keybenefitssuchasreducedlatency,improvedbandwidthefficiency,offlinefunctionality,
andenhancedprivacy,aspredictionscanbemadewithouttransmittingsensitivedataback
tothecloud.
6. ConclusionsandFutureWork
Thisworkprovidedascopingreviewofdata-drivendecisionsupportsystems(DSSs)
withinSaaSenvironments,highlightingcurrentadvances,practices,andgaps. Through
anextensiveanalysisofrecentliterature,ithasbecomeclearthatearlychurnprediction,
customersegmentation,andpersonalizedengagementstrategiesarecriticalforsustaining
growthandprofitabilityinSaaSbusinesses. Churnreductionemergesasthepredominant
researchobjective,withstudiesfocusingontheidentificationofat-riskusersandproposing
targeted, data-driven interventions. From a methodological perspective, it was found
thatRandomForestandXGBoostalgorithmsconsistentlyoutperformedothermachine
learningmodelsinchurnpredictiontasks,particularlywhendealingwithtabularbehav-
ioralandtransactionaldata. Additionally,hybridmodelscombiningstaticandsequential
featureshaveshownsuperiorpredictiveperformance,suggestingthatintegratingdiverse
datasourcescanenhancemodelrobustness. However,simplermodelslikeLogisticRe-

Appl.Sci.2025,15,6508 31of35
gressionremainvaluablefortheirinterpretability,particularlyinresource-constrainedor
real-timeapplications.
Beyondpredictivemodeling,researchemphasizedtheimportanceofusersegmenta-
tionandpersonamodelingforcreatingpersonalizedengagementstrategies. Keydriversof
long-termretentionidentifiedacrossstudiesincludeUI/UXquality,effectiveonboarding
(suchas“ahamoments”),flexiblepricingstrategies,andproactivesupportinterventions.
Moreover, linking predictive outputs to business impact metrics such as CLV, Monthly
RecurringRevenue(MRR),andretention-relatedROIhaveprovenessentialforbridging
analyticswithexecutivedecision-making.
Intermsofpracticalapplications,manystudiesadvocatedforreal-timedeployment
ofpredictivemodelsthroughCRMintegrations,APIs,anddashboardvisualizations. This
operationalizationensuresthatinsightsleadtoimmediateactions,supportingdynamic
marketing, retention, and customer success initiatives. Moreover, choosing the right
machinelearningmodelforaSaaSproviderdependsonthebusinessgoalanddatatype.
For churn prediction, ensemble models like Random Forest and XGBoost are ideal for
structured behavioral data, offering accuracy and interpretability. When user behavior
changes over time, LSTM-based models are better suited, though more complex. For
real-timeuse,LightGBMbalancesspeedandperformance. Inusersegmentationusecases,
modelslikeK-meansworkwellwhencombinedwithdimensionalityreductiontechniques,
especiallywithdiverseuserdata. ForCLVpredictions,LightGBMandLASSOregression
provide accurate and interpretable insights, particularly when paired with time-series
models. Regardinguserengagementandsatisfactionanalysis,deeplearningmodelsare
usefulforlargedatasets,whilelogisticregressionorPLS-SEMofferclaritywithsmaller
ones. Indynamicpricing, XGBoostorreinforcementlearningsupportsstrategytesting
andadaptivepricing. Finally,deploymentrequirementsandenergyefficiencyarecritical
considerations. Models such as LightGBM, XGBoost, and Random Forest are not only
knownfortheirstrongperformancebutarealsorelativelystraightforwardtodeployvia
RESTAPIsorintegrateintocloud-basedmachinelearningpipelines. However,inresource-
constrainedorenergy-sensitivesettings,wherecomputationalloadandsustainabilityare
priorities,lighter-weightmodels,suchaslogisticregressionordecisiontreesshouldbe
prioritized to reduce infrastructure costs and minimize environmental impact without
sacrificingessentialperformance.
However,despitetheconsiderableprogressinresearch,severalchallengesandopen
researchdirectionspersist. Machinelearningmodelsmayexhibitperformancedegradation
overtimeorstruggletoadapttoevolvinguserbehavior,highlightingtheneedfordynamic
modelmonitoringandcontinuallearningmechanisms. Inordertoensurethatdeveloped
DSSsremaineffective,monitoringmechanismsshouldbeestablished. Ensuringtraining
dataisuptodateandmachinelearningmodelsmaintaingoodaccuracylevelsiscrucial.
Batchtrainingofmachinelearningmodelsmaybeagoodstartingpointbutwillnotbe
sustainable in the long term as data volume increases. To this end, periodically batch
trainingofthemodelsand/orreal-timetrainingincrementallyupdatingthemodelscould
beexploredinordertoensuredataintegrity. Therefore,MLaaSsolutions[60]specifically
designedforsupportingdecision-makinginSaaSareofgreatimportancesincetheycan
providemonitoringandupdatingmechanismsreadytouseassuringtheefficiencyofDSSs.
Meanwhile,theenvironmentalimpactofmachinelearningimplementationsemerged
asanothercriticalconsideration. Comparativeanalysisrevealedthatcomplexensemble
methodsanddeepneuralnetworkscanincurhighercomputationalcostsandcarbonemis-
sionsthansimplermodelalternatives,underscoringtheimportanceofbalancingpredictive
performance with sustainability, particularly for SaaS companies managing significant
computationalworkloads. Futureresearch,exceptforseekinggreenerarchitectures,could

Appl.Sci.2025,15,6508 32of35
alsoemphasizeclearlyexplainingthetrade-offsbetweenaccuracymetricsandenviron-
mentalfootprint. Informingusersofenergyconsumptionandcarbonemissionscancreate
awarenessandleadtomoreenvironmentallyfriendlymodelselectiondecisionslikesmaller
architecturesandtheuseoftechniqueslikeearlystoppingandtransferlearning.
Asdecision-makingincreasinglyreliesonautomatedsystems,ensuringtheexplain-
ability,fairness,andtransparencyofpredictions,particularlyinchurnriskassessments,
will be critical. SaaS vendors need to have a clear view of what is happening in their
businessatanytimeandacttowardsimprovinguserexperienceandultimatelyincreas-
ingKPIsthatarevitalfortheirbusiness. Therefore,it’simportantthatDSSsjustifytheir
recommendeddecisionsandprovideclearguidanceonwhatactionsshouldbetaken. To-
wardsthisdirection,DSSscanutilizeinterpretablemachinelearningmodelstojustifytheir
decision-makingprocesses. Posthocmethodsfornon-interpretablemodelssuchasSHAP
values [55] and LIME [56] can be used to provide explanations on models’ predictions
allowing vendors to understand what influences the decisions. While both SHAP and
LIMEoffervaluableinsights,theyservedistinctpurposes. ForSaaSproviders,SHAPmay
bepreferableforstrategicdecision-makingandbiasdetection,whileLIMEcouldbetter
supportcustomer-facingteamsneedingimmediate,case-specificexplanations.
NaturallanguageUIcouldalsobeexploredtoprovideaneasierandfriendlierwayto
provideguidancetoSaaSvendors. LargeLanguageModels(LLMs)couldbeemployed
tounderstanduser’sintentandexplainrecommendedactions,forexampleforreducing
churnorincreasinguserengagement. ComplicatedtoolsandUIsarenotthebestchoicefor
supportingSaaSprofessionals. Theyneedtostayaheadofthecompetitionandactfastand
efficiently. Providingclearexplanationsinnaturallanguageandsuggestingasetofactions
toperformcouldadjustbettertobusyschedulesandofferclarity.
Additionally,futuresystemsmaybenefitfromrefinedpersonalizationstrategiesdriven
bycontext-awarerecommendations,dynamicallyadaptingtoeachuser’slifecyclestageand
dynamicprofile. Inparticular,theDSSswouldrecommendapersonalizedcourseofactions
tailoredtoeachuser’sholisticprofilewhichwillbedynamicallyupdated. Ultimately,the
developmentofintelligent,adaptive,andsustainabledecisionsupportsystemswillbea
keydifferentiatorforSaaSprovidersseekingtobuildresilient,customer-centricbusinesses
inanincreasinglycompetitiveanddynamicmarketplace.
AuthorContributions:Conceptualization,E.M.;methodology,E.M.;formalanalysis,E.M.andG.C.;
investigation,G.C.;resources,G.C.;datacuration,E.M.andG.C.;writing—originaldraftpreparation,
E.M.andG.C.;writing—reviewandediting,E.V.,T.K.andG.A.P.;visualization,E.M.;supervision,
G.A.P.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Bokhari,M.U.;Shallal,Q.M.;Tamandani,Y.K.CloudComputingServiceModels: AComparativeStudy. InProceedingsof
the20163rdInternationalConferenceonComputingforSustainableGlobalDevelopment(INDIACom),NewDelhi,India,
16–18March2016;pp.890–895.
2. Mohammed,C.M.;Zeebaree,S.R.M.SufficientComparisonAmongCloudComputingServices:IaaS,PaaS,andSaaS:AReview.
Int.J.Sci.Bus.2021,5,17–30.
3. Cusumano,M.CloudComputingandSaaSasNewComputingPlatforms.Commun.ACM2010,53,27–29.[CrossRef]
4. Kumar,K.V.K.M.Softwareasaserviceforefficientcloudcomputing.Int.J.Res.Eng.Technol.2014,3,178–181.[CrossRef]
5. Tsai,W.;Bai,X.;Huang,Y.Software-as-a-Service(SaaS):PerspectivesandChallenges.Sci.ChinaInf.Sci.2014,57,1–15.[CrossRef]
6. Berger,P.D.;Nasr,N.I.CustomerLifetimeValue:MarketingModelsandApplications.J.Interact.Mark.1998,12,17–30.[CrossRef]

Appl.Sci.2025,15,6508 33of35
7. Wang,R.;Ying,S.;Jia,X.LogDataModelingandAcquisitioninSupportingSaaSSoftwarePerformanceIssueDiagnosis.Int.J.
Softw.Eng.Knowl.Eng.2019,29,1245–1277.[CrossRef]
8. Morozov,V.;Mezentseva,O.;Kolomiiets,A.;Proskurin,M.PredictingCustomerChurnUsingMachineLearninginITStartups.
InLectureNotesinComputationalIntelligenceandDecisionMaking,2021InternationalScientificConference“IntellectualSystemsof
Decision-makingandProblemsofComputationalIntelligence”;Springer:Berlin/Heidelberg,Germany,2022;pp.645–664.
9. Manzoor,A.;AtifQureshi,M.;Kidney,E.;Longo,L.AReviewonMachineLearningMethodsforCustomerChurnPrediction
andRecommendationsforBusinessPractitioners.IEEEAccess2024,12,70434–70463.[CrossRef]
10. Heilig,L.;Voß,S.DecisionAnalyticsforCloudComputing:AClassificationandLiteratureReview.InBridgingDataandDecisions;
INFORMS:Catonsville,MD,USA,2014;pp.1–26.[CrossRef]
11. Arora,S.;Thota,S.R.;Gupta,S.ArtificialIntelligence-DrivenBigDataAnalyticsforBusinessIntelligenceinSaaSProducts.In
Proceedingsofthe2024FirstInternationalConferenceonPioneeringDevelopmentsinComputerScience&DigitalTechnologies
(IC2SDT),Delhi,India,2–4August2024;IEEE:NewYork,NY,USA,2024;pp.164–169.
12. Ge,Y.;He,S.;Xiong,J.;Brown,D.E.CustomerChurnAnalysisforaSoftware-as-a-ServiceCompany.InProceedingsofthe2017
SystemsandInformationEngineeringDesignSymposium(SIEDS),Charlottesville,VA,USA,28April2017;IEEE:NewYork,NY,
USA,2017;pp.106–111.
13. Phumchusri,N.;Amornvetchayakul,P.MachineLearningModelsforPredictingCustomerChurn:ACaseStudyinaSoftware-
as-a-ServiceInventoryManagementCompany.Int.J.Bus.Intell.DataMin.2024,24,74–106.[CrossRef]
14. Mezentseva,O.V.;Kolesnikova,K.;Kolomiiets,A.CustomerChurnPredictionintheSoftwarebySubscriptionModelsITBusiness
UsingMachineLearningMethods.InProceedingsoftheInternationalWorkshoponInformationTechnologies:Theoreticaland
AppliedProblems,Ternopil,Ukraine,16–18November2021.
15. Dias,J.R.;Antonio,N.PredictingCustomerChurnUsingMachineLearning:ACaseStudyintheSoftwareIndustry.J.Mark.Anal.
2025,13,111–127.[CrossRef]
16. SanchezRamirez,J.;Coussement,K.;DeCaigny,A.;Benoit,D.F.;Guliyev,E.IncorporatingUsageDataforB2BChurnPrediction
Modeling.Ind.Mark.Manag.2024,120,191–205.[CrossRef]
17. Sergue,M.CustomerChurnAnalysisandPredictionUsingMachineLearningforaB2BSaaSCompany.Master’sThesis,KTH
RoyalInstituteofTechnology,Stockholm,Sweden,2020.
18. Saias,J.;Rato,L.;Gonçalves,T.AnApproachtoChurnPredictionforCloudServicesRecommendationandUserRetention.
Information2022,13,227.[CrossRef]
19. Thota,S.R.;Arora,S.;Gupta,S.HybridMachineLearningModelsforPredictiveMaintenanceinCloud-BasedInfrastructurefor
SaaSApplications.InProceedingsofthe2024InternationalConferenceonDataScienceandNetworkSecurity(ICDSNS),Tiptur,
India,26–27July2024;IEEE:NewYork,NY,USA,2024;pp.1–6.
20. Gajananan,K.;Loyola,P.;Katsuno,Y.;Munawar,A.;Trent,S.;Satoh,F.ModelingSentimentPolarityinSupportTicketDatafor
PredictingCloudServiceSubscriptionRenewal.InProceedingsofthe2018IEEEInternationalConferenceonServicesComputing
(SCC),SanFrancisco,CA,USA,2–7July2018;IEEE:NewYork,NY,USA,2018;pp.49–56.
21. Chakraborty,A.;Raturi,V.;Harsola,S.BBE-LSWCM:ABootstrappedEnsembleofLongandShortWindowClickstreamModels.
InProceedingsofthe7thJointInternationalConferenceonDataScience&ManagementofData(11thACMIKDDCODSand
29thCOMAD),Bangalore,India,4–7January2024;ACM:NewYork,NY,USA,2024;pp.350–358.
22. Hoang,H.D.;Cam,N.T.EarlyChurnPredictioninFreemiumGameMobileUsingTransformer-BasedArchitectureforTabular
Data. InProceedingsofthe2024IEEE3rdWorldConferenceonAppliedIntelligenceandComputing(AIC),Gwalior,India,
27–28July2024;IEEE:NewYork,NY,USA,2024;pp.568–573.
23. Rothmeier,K.;Pflanzl,N.;Hullmann,J.A.;Preuss,M.PredictionofPlayerChurnandDisengagementBasedonUserActivity
DataofaFreemiumOnlineStrategyGame.IEEETrans.Games2021,13,78–88.[CrossRef]
24. Kristensen,J.T.;Burelli,P.CombiningSequentialandAggregatedDataforChurnPredictioninCasualFreemiumGames. In
Proceedingsofthe2019IEEEConferenceonGames(CoG),London,UK,20–23August2019;IEEE:NewYork,NY,USA,2019;
pp.1–8.
25. Karmakar,B.;Liu,P.;Mukherjee,G.;Che,H.;Dutta,S.ImprovedRetentionAnalysisinFreemiumRole-PlayingGamesbyJointly
ModellingPlayers’Motivation,ProgressionandChurn.J.R.Stat.Soc.Ser.AStat.Soc.2022,185,102–133.[CrossRef]
26. Pang,L.;Hu,Z.;Liu,Y.HowtoRetainPlayersthroughDynamicQualityAdjustmentinVideoGames.InProceedingsofthe
2021IEEE5thAdvancedInformationTechnology,ElectronicandAutomationControlConference(IAEAC),ChongqingChina,
12–14March2021;IEEE:NewYork,NY,USA,2021;pp.154–160.
27. Boyle,R.E.;Pledger,R.;Brown,H.-F.IterativeMixedMethodApproachtoB2BSaaSUserPersonas.Proc.ACMHum.Comput.Interact.
2022,6,1–44.[CrossRef]
28. Mali,M.;Mangaonkar,N.BehavioralCustomerSegmentationForSubscription.InProceedingsofthe20233rdAsianConference
onInnovationinTechnology(ASIANCON),Pune,India,25–27August2023;IEEE:NewYork,NY,USA,2023;pp.1–6.

Appl.Sci.2025,15,6508 34of35
29. Li,H.(Alice)ConvertingFreeUserstoPaidSubscribersintheSaaSContext:TheImpactofMarketingTouchpoints,Message
Content,andUsage.Prod.Oper.Manag.2022,31,2185–2203.[CrossRef]
30. Yoganarasimhan,H.;Barzegary,E.;Pani,A.DesignandEvaluationofPersonalizedFreeTrials. arXiv2020,arXiv:2006.13420.
[CrossRef]
31. Harahap,E.P.;Hermawan,P.;Kusumawardhani,D.A.R.;Rahayu,N.;Komara,M.A.;Agustian,H.UserInterfaceDesign’sImpact
onCustomerSatisfactionandLoyaltyinSaaSE-Commerce.InProceedingsofthe20243rdInternationalConferenceonCreative
CommunicationandInnovativeTechnology(ICCIT),Tangerang,Indonesia,7–8August2024;IEEE:NewYork,NY,USA,2024;
pp.1–6.
32. vanBelle,E.P.J.Data-DrivenDriversofCustomerLoyaltyinaBusiness-to-BusinessEnvironmentfortheSoftwareasaService
Industry.Master’sThesis,EindhovenUniversityofTechnology,Eindhoven,TheNetherlands,2022.
33. Najjar,A.;Boissier,O.;Picard,G.Elastic&Load-SpikeProofOne-to-ManyNegotiationtoImprovetheServiceAcceptabilityofan
OpenSaaSProvider.InAutonomousAgentsandMultiagentSystems,ProceedingsoftheAAMAS2017Workshops,BestPapers,São
Paulo,Brazil,8–12May2017,RevisedSelectedPapers;Springer:Berlin/Heidelberg,Germany,2017;pp.1–20.
34. Chiang,W.-H.;Ahmad,U.;Wang,S.;Bukhsh,F.InvestigatingAhaMomentThroughProcessMining.InProceedingsofthe25th
InternationalConferenceonEnterpriseInformationSystems,Prague,CzechRepublic,24–26April2023;SCITEPRESS—Science
andTechnologyPublications:Setúbal,Portugal,2023;pp.164–172.
35. Ahlgren,O.;Dalentoft,J.CollectingandIntegratingCustomerFeedback:ACaseStudyofSaaSCompaniesWorkingB2B.Master’s
Thesis,LundUniversity,Lund,Sweden,2020.
36. Kumar,G.S.C.;Dhanalaxmi,B.LeveragingUsage-BasedSaaSModels:OptimizingRevenueandUserExperience.Knowl.Trans.
Appl.Mach.Learn.2025,3,12–17.[CrossRef]
37. Baumann,E.;Kern,J.;Lessmann,S.UsageContinuanceinSoftware-as-a-Service.Inf.Syst.Front.2022,24,149–176.[CrossRef]
38. Curiskis,S.;Dong,X.;Jiang,F.;Scarr,M.ANovelApproachtoPredictingCustomerLifetimeValueinB2BSaaSCompanies.
J.Mark.Anal.2023,11,587–601.[CrossRef]
39. Breiman,L.RandomForests.Mach.Learn.2001,45,5–32.[CrossRef]
40. Ishwaran,H.;Kogalur,U.B.;Blackstone,E.H.;Lauer,M.S.RandomSurvivalForests.Ann.Appl.Stat.2008,2,841–860.[CrossRef]
41. Liaw,A.;Wiener,M.ClassificationandRegressionbyRandomForest.R.News2002,2,18–22.
42. Chen,T.;Guestrin,C.XGBoost.InProceedingsofthe22ndACMSIGKDDInternationalConferenceonKnowledgeDiscovery
andDataMining,SanFrancisco,CA,USA,13–17August2016;ACM:NewYork,NY,USA,2016;pp.785–794.
43. Dreiseitl,S.;Ohno-Machado,L.LogisticRegressionandArtificialNeuralNetworkClassificationModels:AMethodologyReview.
J.Biomed.Inf.2002,35,352–359.[CrossRef]
44. Hastie,T.;Rosset,S.;Zhu,J.;Zou,H.Multi-ClassAdaBoost.Stat.Interface2009,2,349–360.[CrossRef]
45. AlShourbaji,I.;Helian,N.;Sun,Y.;Hussien,A.G.;Abualigah,L.;Elnaim,B.AnEfficientChurnPredictionModelUsingGradient
BoostingMachineandMetaheuristicOptimization.Sci.Rep.2023,13,14441.[CrossRef][PubMed]
46. Rouder,J.N.;Morey,R.D.TeachingBayes’Theorem:StrengthofEvidenceasPredictiveAccuracy.Am.Stat.2019,73,186–190.
[CrossRef]
47. Huang, X.; Khetan, A.; Cvitkovic, M.; Karnin, Z. TabTransformer: Tabular Data Modeling Using Contextual Embeddings.
arXiv2020,arXiv:2012.06678.
48. Ren,J.;Pang,L.;Cheng,Y.DynamicPricingSchemeforIaaSCloudPlatformBasedonLoadBalancing:AQ-LearningApproach.
InProceedingsofthe20178thIEEEInternationalConferenceonSoftwareEngineeringandServiceScience(ICSESS),Beijing,
China,24–26November2017;IEEE:NewYork,NY,USA,2017;pp.806–810.
49. Tibshirani,R.RegressionShrinkageandSelectionviatheLasso.J.R.Stat.Soc.Ser.BStat.Methodol.1996,58,267–288.[CrossRef]
50. vanderAalst,W.ProcessMining;Springer:Berlin/Heidelberg,Germany,2016;ISBN978-3-662-49850-7.
51. Jiang, J.; Nguyen, T.LinearandGeneralizedLinearMixedModelsandTheirApplications; Springer: NewYork, NY,USA,2021;
ISBN978-1-0716-1281-1.
52. Rizopoulos,D.;Verbeke,G.;Molenberghs,G.SharedParameterModelsunderRandomEffectsMisspecification.Biometrika2008,
95,63–74.[CrossRef]
53. Park,S.;Gupta,S.HandlingEndogenousRegressorsbyJointEstimationUsingCopulas.Mark.Sci.2012,31,567–586.[CrossRef]
54. Pereira,I.;Madureira,A.;Bettencourt,N.;Coelho,D.;Rebelo,M.Â.;Araújo,C.;deOliveira,D.A.AMachineLearningasaService
(MLaaS)ApproachtoImproveMarketingSuccess.Informatics2024,11,19.[CrossRef]
55. Lundberg, S.M.; Lee, S.-I. A Unified Approach to Interpreting Model Predictions. In Proceedings of the 31st International
ConferenceonNeuralInformationProcessingSystems,LongBeach,CA,USA,4–9December2017; CurranAssociatesInc.:
RedHook,NY,USA,2017;pp.4768–4777.
56. Ribeiro, M.T.; Singh, S.; Guestrin, C.“WhyShouldITrustYou?”: ExplainingthePredictionsofAnyClassifier. arXiv2016,
arXiv:1602.04938.

Appl.Sci.2025,15,6508 35of35
57. Dwork,C.DifferentialPrivacy. InInternationalColloquiumonAutomata,Languages,andProgramming;Bugliesi,M.,Preneel,B.,
Sassone,V.,Wegener,I.,Eds.;Springer:Berlin/Heidelberg,Germany,2006;pp.1–12.
58. Konecˇn\‘y, J.; McMahan, H.B.; Yu, F.X.; Richtárik, P.; Suresh, A.T.; Bacon, D.FederatedLearning: StrategiesforImproving
CommunicationEfficiency.arXiv2016,arXiv:1610.05492.
59. Shi, W.; Cao, J.; Zhang, Q.; Li, Y.; Xu, L.EdgeComputing: VisionandChallenges. IEEEInternetThingsJ.2016, 3, 637–646.
[CrossRef]
60. GrigoriadisIoannisandVrochidou,E.andT.I.andP.G.A.MachineLearningasaService(MLaaS)—AnEnterprisePerspective.In
ProceedingsoftheInternationalConferenceonDataScienceandApplications,Jaipur,India,14–15July2023;Nanda,S.J.,Yadav,
R.P.,Gandomi,A.H.,Saraswat,M.,Eds.;Springer:Singapore,2023;pp.261–273.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.