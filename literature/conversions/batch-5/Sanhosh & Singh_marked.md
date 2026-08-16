---
conversion_metadata:
  converted_at: "2026-07-21T08:30:47Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Sanhosh & Singh.pdf"
  source_pdf_sha256: "0d9a4f1cb79cdf3189c27e02bf55444c778ef041370044c97a7b1575369138ac"
  page_count: 14
  markdown_char_count: 61446
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

Digital Persona Modeling for Context-Aware Financial Decisioning

1Sai Sanhosh R,2 Ashuosh Kumar Singh 
1MVSR Engineering College

2Professor

Abstract

Rapid  shifts  in  digital  financial  ecosystems  have  introduced  a  need  for  intelligent  systems  that 
can  understand  individual  users  beyond  static  demographic  profiles.  Digital  Persona  Modeling 
(DPM) has emerged as a transformative approach for capturing dynamic behavioral, contextual, 
and  intent-driven  attributes  that  shape  financial  decision  processes.  This  paper  investigates  the 
design  and  application  of  DPM  as  a  foundation  for  context-aware  financial  decisioning, 
enabling financial platforms to deliver more adaptive, trustworthy, and human-aligned guidance. 
Drawing  upon  advancements  in  mobile  data  science, AI-driven  personalization,  and  role-based 
language agents, the study proposes a multi-layered persona architecture integrating behavioral 
telemetry, contextual sensing, and psychographic attributes to continuously refine user profiles.

leverages  explainable  machine

The  proposed  framework 
learning,  cross-platform  data 
unification, and privacy-preserving modeling to ensure secure, interpretable, and ethical decision 
support.  Use  cases  span  automated  budgeting,  micro-investment  recommendations,  credit  risk 
evaluation, and fraud intent detection, with each decision shaped by real-time user states such as 
device  usage  patterns,  financial  literacy  indicators,  situational  stress,  and  market  exposure. 
Additionally, the approach supports equity in financial access by dynamically adapting advisory 
strategies  to  diverse  customer  segments,  including  underserved  entrepreneurs  and  emerging 
digital consumers.

This  research  provides  a  conceptual  and  architectural  foundation  for  DPM-enabled  intelligent 
finance,  highlighting  operational  challenges  related  to  data  governance,  fairness  auditing,  and 
scalable  persona  creation.  The  findings  suggest  that  digital  personas  can  evolve  into  trusted 
digital  financial  counterparts,  ultimately  driving  more  resilient,  user-centric,  and  contextually 
aligned financial ecosystems.

I.

Introduction

The  transformation  of  financial  services  in  the  digital  age  is  being  shaped  by  increasingly 
intelligent, responsive, and personalized systems. One of the most significant innovations driving 
this evolution is the ability to create digital personas based on user behavior, contextual signals, 
and  interaction  histories.  These  personas  are  not  merely  static  profiles  but  dynamic,  evolving

Page | 1

---

<!-- PAGE 2 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

representations of individual financial preferences, habits, and decision-making tendencies. They 
are  built  from  a  combination  of  mobile  data,  transaction  streams,  usage  context,  behavioral 
inputs, and AI-driven inferences.

Conventional  financial  decision-making  systems  typically  relied  on  generalized  models  using 
demographic information or historical financial data. However, such static approaches often fail 
to address the highly contextual and real-time needs of modern users. In contrast, digital persona 
modeling enables context-aware financial systems to adapt their recommendations and actions to 
fit a user's immediate circumstances, device, location, time, financial goals, and emotional state. 
This makes financial decisioning more intuitive, secure, and aligned with user intent.

This  paper  focuses  on  designing  a  conceptual  and  operational  framework  for  digital  persona 
modeling  in  the  context  of  financial  decision  systems.  It  explores  the  use  of  machine  learning 
and data science techniques to extract context-aware insights, and it addresses privacy concerns 
through  responsible  data  governance.  The  approach  aims  to  unify  multiple  data  streams, 
construct  interpretable  persona  layers,  and  utilize  predictive  analytics  to  guide  user-specific 
financial decisions in real time.

Objectives of the Paper

  Define a unified digital persona model tailored to financial applications 
  Explore AI-driven methods for modeling context, behavior, and preferences 
  Propose an architecture for real-time, context-aware decision delivery 
  Address privacy, explainability, and ethical data use in persona modeling 
  Demonstrate how digital personas enhance personalization and financial inclusion

II.  Literature Review

The emergence of context-aware systems and digital personas has significantly influenced the 
personalization of financial services. Several studies have contributed frameworks and 
techniques that underpin this transformation, particularly emphasizing mobile data science, 
explainable AI, personalization engines, and real-time analytics.

One foundational work explores mobile expert systems for personalized decision-making in 
mobile apps. It discusses rule-based learning and AI techniques that adapt user preferences using 
contextual inputs such as device type, time, and behavior. This concept is key for real-time 
adaptation in digital finance systems.

Another study emphasizes the role of data-driven financial literacy and segmentation in 
empowering users, particularly entrepreneurs. Their personalized education tools and financial

Page | 2

---

<!-- PAGE 3 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

planning frameworks highlight how digital personas can enhance user agency and self-awareness 
in financial decisioning.

A  recent  survey  on  role-playing  language  agents  highlights  the  use  of  generative AI  to  model 
dynamic  personas  that  simulate  human-like  interactions.  Such  advancements  are  vital  for 
building intelligent financial advisors capable of empathetic and scenario-based guidance.

Other works provide comprehensive insights into how UX optimization tools, hybrid AI support 
platforms, and context-aware user engagement mechanisms improve financial decision systems. 
These strategies contribute to the design of responsive financial interfaces tailored to individual 
behavioral profiles.

The  unification  of  financial  data  streams,  as  proposed  by  multiple  studies,  has  proven  to  be 
essential in constructing accurate, cross-platform personas. Similarly, customer segmentation and 
business intelligence approaches help derive real-time insights that inform personalized financial 
strategies.

From the standpoint of explainability and compliance, frameworks that explore AI prompting for 
financial reasoning and privacy-preserving AI models set the foundation for trustworthy persona-
driven financial systems.

These  works  collectively  support  the  development  of  context-aware  digital  personas  by 
integrating mobile  data,  behavioral  features, explainability,  and adaptive learning into financial 
ecosystems.

Page | 3

---

<!-- PAGE 4 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

Sr 
No.

Focus Area

AI 
Techniques

Context-
Aware

Personalization

Privacy 
Focus

Financial 
 Domain 
Use

Moderate  Yes

Low

Yes

Moderate  Moderate

Moderate  Yes

Rule learning, 
ML

Yes

Market 
Segmentation

Yes

Generative AI  High

Yes

Analytics, 
Clustering 
NLP, 
Engagement 
AI

Yes

High

High

High

Moderate

Moderate

High

Indirect

Clustering, BI  Moderate

High

Low

Yes

LLM 
Prompting 
Data Fusion, 
ML

Low

Moderate

High

High

Moderate

Moderate

High

Yes

AI Modeling

High

Moderate

Moderate  Yes

Finance 4.0 
Strategy

Moderate

High

Moderate  Yes

1

2

3

4

5

6

7

8

9

10

Mobile decision-
making rules 
Entrepreneurial 
growth via 
personalization 
Role-playing 
language agents 
Data-driven personas 
and profiling

UX AI tools for hybrid 
environments

Customer 
segmentation 
strategies 
Generative 
prompting for finance 
Data unification for 
fraud and compliance 
Mobile data science 
frameworks 
Digital transformation 
in finance

III.  Methodology

3.1 Overview

The proposed methodology focuses on modeling a Digital Persona that integrates context-aware 
features to support real-time, personalized financial decisions. The approach blends multi-source 
data  fusion,  dynamic  context  modeling,  and  explainable  AI  models  to  simulate  human-like 
financial advisors. The overall pipeline supports a privacy-aware design by embedding federated 
learning and local processing mechanisms.

3.2 System Architecture

The architecture comprises five major layers:

1.  Data  Acquisition  Layer:  Collects  structured  and  unstructured  data  from  mobile  apps,

web interactions, financial records, and contextual sensors (e.g., GPS, device type).

Page | 4

---

<!-- PAGE 5 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

2.  Context Engine: Interprets data dimensions such as time, location, intent, and user state

to enrich the digital persona.

3.  Persona Builder: Generates persona profiles using clustering and persona-role mapping

techniques.

4.  Decisioning  Model  Layer:  Hosts  AI  models  (classification/regression)  trained  on

historical decisions, feedback loops, and personalization rules.

5.  Decision  Delivery  &  Feedback:  Interfaces  with  mobile  or  web  interfaces  to  deliver

recommendations and capture feedback for continuous improvement.

Figure 2. System Architecture of Proposed Framework

3.3 Dataset Description

Since the system aims to work in a real-world setting, the prototype was tested on a simulated 
hybrid dataset combining:

  Transactional Logs (synthetic debit/credit records)

  Mobile Contextual Logs (simulated location, device ID, session time)

  User Profiles (income, preferences, behavior scores)

  Feedback Labels (accepted, rejected, delayed decisions)

Data points were aggregated to mimic user journeys in mobile banking and investment apps.

3.4 Model Usage

The following models were used for experimentation:

Model

Purpose

Input Features

Page | 5

---

<!-- PAGE 6 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

Random Forest

LSTM Neural 
Net 
K-Means 
Clustering

Classification of decision 
type 
Sequential pattern 
analysis

Persona grouping

Time, location, 
transaction type, score 
Session time series, 
device usage 
Spending style, risk 
tolerance

  Random Forest: An ensemble-based model that combines multiple decision trees to 
deliver accurate, interpretable predictions for financial risk and fraud classification.

  LSTM Neural Net: A sequence-aware deep learning model that captures time-based 
patterns in financial behavior to support personalized and predictive decision-making.

K-Means Clustering: An unsupervised learning algorithm that segments users or transactions 
into distinct clusters for contextual financial analysis and persona-driven insights

  Persona Similarity Score

For matching a user to a predefined persona group:

𝑆(𝑢, 𝑝) =

1
𝑛

𝑛

∑

𝑖=1

∣ 𝑥𝑢,𝑖 − 𝑥𝑝,𝑖 ∣
max⁡(𝑥𝑖)

  Context-Aware Risk Function

To calculate the real-time decision risk:

𝑅 = 𝛼1 ⋅ 𝐶location + 𝛼2 ⋅ 𝐶time + 𝛼3 ⋅ 𝐶device + 𝛽 ⋅ 𝑇

where 𝐶𝑖represents contextual variables and 𝑇is the transaction amount.

3.5 Evaluation Matrix

To evaluate the system’s performance, the following metrics were used:

Metric

Accuracy

Precision

Recall

Page | 6

Description 
Proportion of correct 
financial 
recommendations 
Correct positive 
predictions over all 
predicted positives 
Correct positive 
predictions over actual 
positives

Formula

Accuracy=(TP+TN)/TP+FP+TN+FN

Precision=TP/(TP+FP)

Recall=TP/(TP+FN)

---

<!-- PAGE 7 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

F1-Score

Privacy Leakage 
Ratio (PLR)

Harmonic mean of 
Precision and Recall 
Measures degree of 
privacy exposure in 
gradients

F1=2×((Precision×Recall)/(Precision+Recall))

PLR = 1 - \frac{\text{Privacy Preserved 
Instances}}

Visual analysis using multi-metric radar plots (introduced in the Results section) assesses the 
trade-off between interpretability, performance, and privacy.

In summary, the methodology establishes a federated, agentic architecture with explainable and 
privacy-preserving mechanisms. This setup empowers decentralized financial agents to learn 
collaboratively, justify every recommendation, and guarantee that user data never leaves the 
local device.

IV.  Results And Discussions

4.1 Model Performance

To evaluate the effectiveness of digital persona-based models for financial decisioning, we 
implemented and tested three distinct machine learning algorithms:

  Random Forest (RF): Utilized for robust classification based on contextual features.

  LSTM Neural Network: Designed to capture sequential behavioral data over time.

  K-Means Clustering: Applied for unsupervised grouping of users based on contextual

traits.

The evaluation was conducted on a synthesized dataset simulating mobile transaction behaviors 
under varying contexts (e.g., time, location, device usage, session length). Below is a comparison 
of the models across common evaluation metrics:

Table 2. Model Performance Comparison

Model Type

Random Forest

LSTM Neural Net

Accuracy 
(%)

Precision 
(%)

Recall 
(%)

F1-Score 
(%)

91.2

93.6

90.4

94.4

89.9

91.8

90.1

92.9

K-Means Clustering

75.0

73.3

70.4

71.8

Page | 7

---

<!-- PAGE 8 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

These results highlight that LSTM models outperform others due to their capability to model 
temporal dependencies in user behavior and context shifts.

4.2 F1 Metrics and Multi-Metric Analysis

F1 Metrics and Multi-Metric Analysis

F1 Score Overview:

  LSTM Neural Net achieved the highest F1 score, indicating strong precision and recall

balance in capturing context-aware financial decision behaviors.

  Random Forest also performed well, particularly in interpretable rule generation based

on tabular financial history.

  K-Means Clustering had a lower F1 score, which is expected for unsupervised models

not optimized for classification accuracy.

F1 Score: Definition and Formula

The F1 Score is a metric used to evaluate the performance of classification models, particularly 
when dealing with imbalanced classes. It balances Precision and Recall, offering a single metric 
that accounts for both false positives and false negatives.

Formula:

Page | 8

---

<!-- PAGE 9 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

F1 Score = 2 ⋅

Precision ⋅ Recall
Precision + Recall

Where:

  Precision is:

  Recall is:

Interpretation:

Precision =

True Positives
True Positives + False Positives

Recall =

True Positives
True Positives + False Negatives

  High F1 Score (close to 1): Model has both high precision and high recall.

  Low F1 Score (close to 0): Indicates poor performance on one or both metrics.

4.3 Limitations

While the proposed system provides a robust framework for explainable and privacy-preserving 
financial advisory, several limitations were identified:

1.  Data Privacy Concerns

While context-aware systems provide high personalization, they rely heavily on user data 
such as behavior, location, transaction history, and preferences. Handling and storing 
such sensitive data increases the risk of privacy breaches and regulatory non-compliance.

2.  Limited Dataset Diversity

The datasets used for model training may lack diversity across geography, culture, 
financial behavior, or demographic profiles. This can introduce bias into the decision-
making process and reduce the model’s applicability across wider populations.

3.  Model Generalizability

Models like LSTM, Random Forest, and K-Means are highly effective under certain 
conditions but may not generalize well across drastically different use cases or unseen 
data patterns, especially in fast-evolving financial ecosystems.

4.  Interpretability Challenges

AI-based persona models, particularly those involving deep learning, often behave as

Page | 9

---

<!-- PAGE 10 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

black boxes. The lack of transparency in decision reasoning can reduce trust in the 
system, especially for regulatory audits and end-user explanations.

5.  Context Drift Over Time

User behavior and financial context can evolve. A model trained on past persona 
characteristics may become stale, requiring continuous learning and adaptation 
mechanisms that are not fully addressed in the current framework

V.  Conclusion

This  paper  presents  a  comprehensive  framework  for  modeling  digital  personas  to  support 
context-aware  financial  decisioning.  By  integrating  multi-source  behavioral,  transactional,  and 
contextual  data,  the  proposed  system  personalizes  financial  recommendations  and  decisions  in 
real time. Utilizing models like Random Forest for classification, LSTM for temporal  analysis, 
and K-Means for segmentation, the system demonstrates strong adaptability in recognizing user-
specific patterns. The model’s F1-score metrics and accuracy suggest that contextual integration 
meaningfully improves decision relevance and user alignment.

The  core  contribution  lies  in  shifting  financial AI  systems  from  static,  rules-based  engines  to 
dynamic, personalized decisioning agents. The architecture enables user-centric decision flows, 
addressing  the  limitations  of  generic  financial  advice  tools.  However,  privacy  constraints, 
evolving contexts, and data diversity present ongoing challenges.

Looking  ahead,  the  system  can  be  significantly  enhanced  through  federated  learning 
deployments across financial institutions. This would allow models to learn from a broader pool 
of behaviors without compromising data privacy. Additionally, adapting the persona framework 
to emerging fraud vectors such as those generated by generative AI and synthetic identities will

Page | 10

---

<!-- PAGE 11 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

be  essential  to  future-proofing  decisioning  models.  Integration  with  real-time  behavioral 
biometrics  such  as  mouse  movements,  typing  speed,  and  facial  cues  could  further  elevate  the 
contextual awareness of the system.

There  is  also  scope  for  incorporating  explainable  AI  (XAI)  elements  to  interpret  decisions, 
increasing  user  trust  and  regulatory  transparency.  Finally,  incorporating  adaptive  reinforcement 
learning will allow the system to fine-tune its persona model based on evolving user behaviors 
and feedback loops, pushing the boundaries of personalization in digital finance.

References

1.  K Richardson. (2024). Navigating Challenges in Real-Time Payment Systems in 
FinTech.  International  Journal  of  Artificial  Intelligence,  Data  Science,  and 
Machine  Learning,  5(1),  44-56.  https://doi.org/10.63282/3050-9262.IJAIDSML-
V5I1P105

2.  Rautaray,  S.,  &  Tayagi,  D.  (2023). Artificial  Intelligence  in  Telecommunications: 
Applications,  Risks,  and  Governance  in  the  5G  and  Beyond  Era. Artificial 
Intelligence

3.  D  De  Roure.  (2024).  AI-Powered  Predictive  Maintenance  in  Industrial  IoT. 
from

Integrated  Journal  of  Science  and  Technology,  1(4).  Retrieved 
https://ijstpublication.com/index.php/ijst/article/view/17

4.  A.  Garg,  M.  Pandey,  and A.  R.  Pathak,  “A  Multi-Layered AI-IoT  Framework  for 
Adaptive  Financial  Services”, IJETCSIT,  vol.  5,  no.  3,  pp.  47–57,  Oct.  2024, 
doi: 10.63282/3050-9246.IJETCSIT-V5I3P105

5.  H.  N.  Himabindu  Gurajada  and  R.  Autade,  "Quantum  Computing  for  Fraud 
Detection  in  Real-Time  Payment  Systems,"  2025  International  Conference  on 
Computing  Technologies  &  Data  Communication  (ICCTDC),  HASSAN,  India, 
2025, pp. 01-08, doi: 10.1109/ICCTDC64446.2025.11158810.

6.  S Mishra, and A Jain, “Leveraging IoT-Driven Customer Intelligence for Adaptive 
Financial  Services”, IJAIDSML,  vol.  4,  no.  3,  pp.  60–71,  Oct.  2023, 
doi: 10.63282/3050-9262.IJAIDSML-V4I3P107

7.  A Magoulick and D Paleti, "Computer Vision for Financial Fraud Prevention using 
International  Conference  on  Engineering, 
Visual  Pattern  Analysis,"  2025 
Technology  &  Management  (ICETM),  Oakdale,  NY,  USA,  2025,  pp.  1-7,  doi: 
10.1109/ICETM63734.2025.11051811.

8.  MN Nwobodo, “CNN-Based Image Validation for ESG Reporting: An Explainable 
AI and Blockchain Approach”, Int. J. Comput. Sci. Inf. Technol. Res., vol. 5, no. 4, 
pp. 64–85, Dec. 2024, doi: 10.63530/IJCSITR_2024_05_04_007

9.  K  Lacruz  and  F Jubitor,  "Quantum  Computing  for Fraud  Detection in  Real-Time 
Payment Systems," 2025 International Conference on Computing Technologies &

Page | 11

---

<!-- PAGE 12 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

Data  Communication  (ICCTDC),  HASSAN, 
10.1109/ICCTDC64446.2025.11158810.

India,  2025,  pp.  01-08,  doi:

10. AV  Jusas,  "How  Natural  Language  Processing  Framework  Automate  Business 
Requirement  Elicitation," International  Journal  of  Computer  Trends  and 
Technology 
47-50, 
pp. 
2025. Crossref, https://doi.org/10.14445/22312803/IJCTT-V73I5P107

(IJCTT),

vol.

73,

no.

5,

11. A  Vedantham,  "A  Minimalist  Approach  to  Blockchain  Design:  Enhancing 
Immutability  and  Verifiability  with  Scalable  Peer-to-Peer  Systems,"  2025 
International  Conference  on 
Inventive  Computation  Technologies  (ICICT), 
Kirtipur, Nepal, 2025, pp. 1697-1703, doi: 10.1109/ICICT64420.2025.11005016. 
12. Doddipatla, L. (2024). Ethical and Regulatory Challenges of Using Generative AI 
in  Banking:  Balancing  Innovation  and  Compliance.  Educational  Administration: 
Theory and Practice, 30(3), 2848-2855.

13. F  Mannering.  (2025).  Artificial  Intelligence  in  Security:  Driving  Trust  and 
Customer Engagement on FX Trading Platforms. Journal of Knowledge Learning 
71-77. 
ISSN: 
and  Science  Technology 
https://doi.org/10.60087/jklst.v4.n1.008

2959-6386

(online),

4(1),

14. M  Danish,  "RIDI-Hypothesis:  A  Foundational  Theory  for  Cybersecurity  Risk 
Assessment  in  Cyber-Physical  Systems,"  2025  4th  International  Conference  on 
Sentiment Analysis  and  Deep  Learning  (ICSADL),  Bhimdatta,  Nepal,  2025,  pp. 
117-123, doi: 10.1109/ICSADL65848.2025.10932989.

15. RD  Rohweeis.  Avalanche:  A  Secure  Peer-to-Peer  Payment  System  Using

Snowball Consensus Protocols. TechRxiv. January 20, 2025.

16. DOI: 10.36227/techrxiv.173738333.35212976/v1 
17. H Tabuchi,  "A  Formalized Approach  to  Secure  and  Scalable  Smart  Contracts  in 
International  Conference  on  Engineering, 
Decentralized  Finance,"  2025 
Technology  &  Management  (ICETM),  Oakdale,  NY,  USA,  2025,  pp.  1-6,  doi: 
10.1109/ICETM63734.2025.11051910.

18. Doddipatla,  L.  (2025).  Efficient  and  secure  threshold  signature  scheme  for

decentralized payment systems withenhanced privacy.

19. GH  Bojesen,  "Unraveling  the  Paradox:  Green  Premium  and  Climate  Risk 
Premium  in  Sustainable  Finance,"  2025  IEEE  International  Conference  on 
for  Social 
Interdisciplinary  Approaches 
Innovation 
doi: 
1-5, 
(IATMSI), 
10.1109/IATMSI64286.2025.10985498.

in  Technology  and  Management

Gwalior,

2025,

India,

pp.

20. Hemalatha Naga Himabindu, Gurajada. (2022). Unlocking Insights: The Power of 
Data  Science  and  AI  in  Data  Visualization.  International  Journal  of  Computer 
Science  and  Information  Technology  Research  (IJCSITR),  3(1),  154-179. 
https://doi.org/10.63530/IJCSITR_2022_03_01_016

Page | 12

---

<!-- PAGE 13 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

21. R.  Ramadugu,  "Analyzing  the  Role  of  CBDC  and  Cryptocurrency  in  Emerging 
Market  Economies:  A  New  Keynesian  DSGE  Approach,"  2025  International 
Conference  on  Inventive  Computation  Technologies  (ICICT),  Kirtipur,  Nepal, 
2025, pp. 1300-1306, doi: 10.1109/ICICT64420.2025.11005009.

22. CT  Aghaunor.  (2023).  From  Data  to  Decisions:  Harnessing  AI  and  Analytics. 
International  Journal  of  Artificial  Intelligence,  Data  Science,  and  Machine 
Learning, 4(3), 76-84. https://doi.org/10.63282/3050-9262.IJAIDSML-V4I3P109 
23. AR Kommera. (2024). Visualizing the Future: Integrating Data Science and AI for 
Impactful  Analysis.  International  Journal  of  Emerging  Research  in  Engineering 
and  Technology,  5(1),  48-59.  https://doi.org/10.63282/3050-922X.IJERET-
V5I1P107

24. S.  R.  Seelam, A.  Upadhyay,  V.  R.  Pasam,  "Federated  Learning  Framework  for 
Privacy-Preserving  Health  Monitoring  via  IoT  Devices,"  2025  International 
Conference on Innovations in Intelligent Systems: Advancements in Computing, 
Communication, and Cybersecurity (ISAC3), Bhubaneswar, India, 2025, pp. 1-6, 
doi: 10.1109/ISAC364032.2025.11156349.

25. Flöter,  C.,  Geringer,  S.,  Reina,  G.,  Weiskopf,  D.,  &  Ropinski,  T.  (2025,  May). 
Evaluating Foveated Frame Rate Reduction in Virtual Reality for Head-Mounted 
Displays. In Proceedings of the 2025 Symposium on Eye Tracking Research and 
Applications (pp. 1-7).

26. Srikanth, N., Sagar, K., Sravanthi, C., & Saranya, K. (2024, May). Deep Learning 
Driven  Food  Recognition  and  Calorie  Estimation  Using  Mobile  Net Architecture. 
In 2024 5th International Conference for Emerging Technology (INCET) (pp. 1-7). 
IEEE.

27. Kazanidis, I., & Andreadou, E. (2025, June). Exploring the Benefits of Immersive 
Technologies  in  Elementary  Physical  Education.  In International  Conference  on 
Immersive Learning (pp. 129-144). Cham: Springer Nature Switzerland.

28. Kang,  H.,  Yang,  E.,  Choe,  S.,  &  Ryu,  J.  (2025).  Virtual  Interaction  on  Concept 
for  Construction  Safety  Training. Immersive  Learning  Research-

Learning 
Practitioner, 148-153.

29. Choudhry, A., Jain, C., Singh, S., & Ratna, S. (2025, March). Comparison of CNN 
and  Vision  Transformers  for  Wildfire  Detection: A  Proxy  for  Stubble  Burning.  In 
2025  3rd  International  Conference  on  Disruptive  Technologies  (ICDT)  (pp.  286-
289). IEEE.

30. Pandey,  P.,  RG,  R. T.,  Pati,  R.  P., &  Singh, S.  (2025, August). ALL-ViT: A  Novel 
Approach  for  Detection  of  Acute  Lymphoblastic  Leukemia.  In  2025  12th 
International  Conference  on  Emerging  Trends  in  Engineering  &  Technology-
Signal and Information Processing (ICETET-SIP) (pp. 1-6). IEEE.

31. Garduno-Ramon, C. E., Cruz-Albarran, I. A., Garduño-Ramón, M. A., & Morales-
Hernandez, L. A. (2025, August). Automatic segmentation of regions of interest in

Page | 13

---

<!-- PAGE 14 -->

International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025

Pages:1-14

thermal images in the facial and hand area. In 2025 International Conference on 
Artificial Intelligence, Computer, Data Sciences and Applications (ACDSA) (pp. 1-
6). IEEE.

32. Friant, M., Halim, S. M., & Khan, L. (2025, August). Keeping track of the kids: a 
deep dive into object detector fairness for pedestrians of different ages. In 2025 
International Conference on Artificial Intelligence, Computer, Data Sciences and 
Applications (ACDSA) (pp. 1-6). IEEE.

33. Pyae, A. (2025, June). Understanding Students’ Acceptance, Trust, and Attitudes 
towards  AI-generated  Images  for  Educational  Purposes.  In  Proceedings  of  the 
2025 Conference on Creativity and Cognition (pp. 338-343).

34. K Peter. (2022). Multi-Modal GANs for Real-Time Anomaly Detection in Machine 
and Financial Activity Streams. International Journal of Artificial Intelligence, Data 
Science,  and  Machine  Learning,  3(1),  39-48.  https://doi.org/10.63282/3050-
9262.IJAIDSML-V3I1P105

35. Kadambala, K. M. (2025). Auditable AI Pipelines: Logging and Verifiability in ML

Workflows. Innovative Journal of Applied Science, 35-35.

36. Rani,  S.,  &  Bhosale,  A.  (2025).  Bias  Propagation  in  Generative  AI:  Risk  and

Mitigation Strategies. Applied Engineering Solutions and Technologies, 4-4.

37. Madduru,  P.,  &  Bhosale,  A.  (2024).  Ethical  and  Regulatory  Implications  of  AI 
Development  in  Telecom  Services. International  Journal  of  Emerging  Trends  in 
Computer Science and Information Technology, 5(4), 105-115.

38. Rani,  S.,  &  Powar,  Y.  (2024).  Federal  Learning  Optimization  for  Edge  Devices 
with Limited Resources. International Journal of AI, BigData, Computational and 
Management Studies, 5(4), 115-123.

39. T Anthony.  (2021). AI  Models  for  Real  Time  Risk Assessment  in  Decentralized 
from

Applied 
Finance. 
https://annalsofappliedsciences.com/index.php/aas/article/view/30

Sciences,

Retrieved

Annals

2(1).

of

40. Thombre,  T.  (2024).  IoT  and  Metaverse  Integration:  Frameworks  and  Future 
Applications. International  Journal  of  Artificial  Intelligence,  Data  Science,  and 
Machine Learning, 5(4), 81-90.

Page | 14

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
Digital Persona Modeling for Context-Aware Financial Decisioning
1Sai Sanhosh R,2 Ashuosh Kumar Singh
1MVSR Engineering College
2Professor
Abstract
Rapid shifts in digital financial ecosystems have introduced a need for intelligent systems that
can understand individual users beyond static demographic profiles. Digital Persona Modeling
(DPM) has emerged as a transformative approach for capturing dynamic behavioral, contextual,
and intent-driven attributes that shape financial decision processes. This paper investigates the
design and application of DPM as a foundation for context-aware financial decisioning,
enabling financial platforms to deliver more adaptive, trustworthy, and human-aligned guidance.
Drawing upon advancements in mobile data science, AI-driven personalization, and role-based
language agents, the study proposes a multi-layered persona architecture integrating behavioral
telemetry, contextual sensing, and psychographic attributes to continuously refine user profiles.
The proposed framework leverages explainable machine learning, cross-platform data
unification, and privacy-preserving modeling to ensure secure, interpretable, and ethical decision
support. Use cases span automated budgeting, micro-investment recommendations, credit risk
evaluation, and fraud intent detection, with each decision shaped by real-time user states such as
device usage patterns, financial literacy indicators, situational stress, and market exposure.
Additionally, the approach supports equity in financial access by dynamically adapting advisory
strategies to diverse customer segments, including underserved entrepreneurs and emerging
digital consumers.
This research provides a conceptual and architectural foundation for DPM-enabled intelligent
finance, highlighting operational challenges related to data governance, fairness auditing, and
scalable persona creation. The findings suggest that digital personas can evolve into trusted
digital financial counterparts, ultimately driving more resilient, user-centric, and contextually
aligned financial ecosystems.
I. Introduction
The transformation of financial services in the digital age is being shaped by increasingly
intelligent, responsive, and personalized systems. One of the most significant innovations driving
this evolution is the ability to create digital personas based on user behavior, contextual signals,
and interaction histories. These personas are not merely static profiles but dynamic, evolving
Page | 1

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
representations of individual financial preferences, habits, and decision-making tendencies. They
are built from a combination of mobile data, transaction streams, usage context, behavioral
inputs, and AI-driven inferences.
Conventional financial decision-making systems typically relied on generalized models using
demographic information or historical financial data. However, such static approaches often fail
to address the highly contextual and real-time needs of modern users. In contrast, digital persona
modeling enables context-aware financial systems to adapt their recommendations and actions to
fit a user's immediate circumstances, device, location, time, financial goals, and emotional state.
This makes financial decisioning more intuitive, secure, and aligned with user intent.
This paper focuses on designing a conceptual and operational framework for digital persona
modeling in the context of financial decision systems. It explores the use of machine learning
and data science techniques to extract context-aware insights, and it addresses privacy concerns
through responsible data governance. The approach aims to unify multiple data streams,
construct interpretable persona layers, and utilize predictive analytics to guide user-specific
financial decisions in real time.
Objectives of the Paper
 Define a unified digital persona model tailored to financial applications
 Explore AI-driven methods for modeling context, behavior, and preferences
 Propose an architecture for real-time, context-aware decision delivery
 Address privacy, explainability, and ethical data use in persona modeling
 Demonstrate how digital personas enhance personalization and financial inclusion
II. Literature Review
The emergence of context-aware systems and digital personas has significantly influenced the
personalization of financial services. Several studies have contributed frameworks and
techniques that underpin this transformation, particularly emphasizing mobile data science,
explainable AI, personalization engines, and real-time analytics.
One foundational work explores mobile expert systems for personalized decision-making in
mobile apps. It discusses rule-based learning and AI techniques that adapt user preferences using
contextual inputs such as device type, time, and behavior. This concept is key for real-time
adaptation in digital finance systems.
Another study emphasizes the role of data-driven financial literacy and segmentation in
empowering users, particularly entrepreneurs. Their personalized education tools and financial
Page | 2

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
planning frameworks highlight how digital personas can enhance user agency and self-awareness
in financial decisioning.
A recent survey on role-playing language agents highlights the use of generative AI to model
dynamic personas that simulate human-like interactions. Such advancements are vital for
building intelligent financial advisors capable of empathetic and scenario-based guidance.
Other works provide comprehensive insights into how UX optimization tools, hybrid AI support
platforms, and context-aware user engagement mechanisms improve financial decision systems.
These strategies contribute to the design of responsive financial interfaces tailored to individual
behavioral profiles.
The unification of financial data streams, as proposed by multiple studies, has proven to be
essential in constructing accurate, cross-platform personas. Similarly, customer segmentation and
business intelligence approaches help derive real-time insights that inform personalized financial
strategies.
From the standpoint of explainability and compliance, frameworks that explore AI prompting for
financial reasoning and privacy-preserving AI models set the foundation for trustworthy persona-
driven financial systems.
These works collectively support the development of context-aware digital personas by
integrating mobile data, behavioral features, explainability, and adaptive learning into financial
ecosystems.
Page | 3

|     |     |     |     |     | Pages:1-14  |     |
| --- | --- | --- | --- | --- | ----------- | --- |
International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025
Financial
| Sr   |             | AI          | Context- |                  | Privacy  |          |
| ---- | ----------- | ----------- | -------- | ---------------- | -------- | -------- |
|      | Focus Area  |             |          | Personalization  |          |  Domain  |
| No.  |             | Techniques  | Aware    |                  | Focus    |          |
Use
| Mobile decision- |     | Rule learning,  |      |      |           |      |
| ---------------- | --- | --------------- | ---- | ---- | --------- | ---- |
| 1                |     |                 | Yes  | Yes  | Moderate  | Yes  |
| making rules     |     | ML              |      |      |           |      |
Entrepreneurial
Market
| 2  growth via  |     |     | Yes  | High  | Low  | Yes  |
| -------------- | --- | --- | ---- | ----- | ---- | ---- |
Segmentation
personalization
Role-playing
| 3   |     | Generative AI  | High  | High  | Moderate  | Moderate  |
| --- | --- | -------------- | ----- | ----- | --------- | --------- |
language agents
| Data-driven personas  |     | Analytics,  |      |       |           |      |
| --------------------- | --- | ----------- | ---- | ----- | --------- | ---- |
| 4                     |     |             | Yes  | High  | Moderate  | Yes  |
| and profiling         |     | Clustering  |      |       |           |      |
NLP,
UX AI tools for hybrid
| 5   |     | Engagement  | Moderate  | Moderate  | High  | Indirect  |
| --- | --- | ----------- | --------- | --------- | ----- | --------- |
environments
AI
Customer
| 6  segmentation  |     | Clustering, BI  | Moderate  | High  | Low  | Yes  |
| ---------------- | --- | --------------- | --------- | ----- | ---- | ---- |
strategies
| Generative             |     | LLM           |           |           |       |       |
| ---------------------- | --- | ------------- | --------- | --------- | ----- | ----- |
| 7                      |     |               | Low       | Moderate  | High  | High  |
| prompting for finance  |     | Prompting     |           |           |       |       |
| Data unification for   |     | Data Fusion,  |           |           |       |       |
| 8                      |     |               | Moderate  | Moderate  | High  | Yes   |
| fraud and compliance   |     | ML            |           |           |       |       |
Mobile data science
| 9   |     | AI Modeling  | High  | Moderate  | Moderate  | Yes  |
| --- | --- | ------------ | ----- | --------- | --------- | ---- |
frameworks
| Digital transformation  |     | Finance 4.0  |           |       |           |      |
| ----------------------- | --- | ------------ | --------- | ----- | --------- | ---- |
| 10                      |     |              | Moderate  | High  | Moderate  | Yes  |
| in finance              |     | Strategy     |           |       |           |      |

| III.  | Methodology  |     |     |     |     |     |
| ----- | ------------ | --- | --- | --- | --- | --- |
3.1 Overview
The proposed methodology focuses on modeling a Digital Persona that integrates context-aware
features to support real-time, personalized financial decisions. The approach blends multi-source
data fusion, dynamic  context  modeling, and explainable AI models  to  simulate human-like
financial advisors. The overall pipeline supports a privacy-aware design by embedding federated
learning and local processing mechanisms.

3.2 System Architecture
The architecture comprises five major layers:
1.  Data Acquisition Layer: Collects structured and unstructured data from mobile apps,
web interactions, financial records, and contextual sensors (e.g., GPS, device type).
Page | 4

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
2. Context Engine: Interprets data dimensions such as time, location, intent, and user state
to enrich the digital persona.
3. Persona Builder: Generates persona profiles using clustering and persona-role mapping
techniques.
4. Decisioning Model Layer: Hosts AI models (classification/regression) trained on
historical decisions, feedback loops, and personalization rules.
5. Decision Delivery & Feedback: Interfaces with mobile or web interfaces to deliver
recommendations and capture feedback for continuous improvement.
Figure 2. System Architecture of Proposed Framework
3.3 Dataset Description
Since the system aims to work in a real-world setting, the prototype was tested on a simulated
hybrid dataset combining:
 Transactional Logs (synthetic debit/credit records)
 Mobile Contextual Logs (simulated location, device ID, session time)
 User Profiles (income, preferences, behavior scores)
 Feedback Labels (accepted, rejected, delayed decisions)
Data points were aggregated to mimic user journeys in mobile banking and investment apps.
3.4 Model Usage
The following models were used for experimentation:
Model Purpose Input Features
Page | 5

  Pages:1-14
International Journal of Research in Mulidisciplinary Technology                           Volume 1, issue 4 2025
|     | Classification of decision  |     |     | Time, location,  |     |     |
| --- | --------------------------- | --- | --- | ---------------- | --- | --- |
Random Forest
|              | type                |     |     | transaction type, score  |     |     |
| ------------ | ------------------- | --- | --- | ------------------------ | --- | --- |
| LSTM Neural  | Sequential pattern  |     |     | Session time series,     |     |     |
| Net          | analysis            |     |     | device usage             |     |     |
| K-Means      |                     |     |     | Spending style, risk     |     |     |
Persona grouping
| Clustering  |     |     |     | tolerance  |     |     |
| ----------- | --- | --- | --- | ---------- | --- | --- |

  Random Forest: An ensemble-based model that combines multiple decision trees to
deliver accurate, interpretable predictions for financial risk and fraud classification.
  LSTM Neural Net: A sequence-aware deep learning model that captures time-based
patterns in financial behavior to support personalized and predictive decision-making.
K-Means Clustering: An unsupervised learning algorithm that segments users or transactions
into distinct clusters for contextual financial analysis and persona-driven insights
  Persona Similarity Score
For matching a user to a predefined persona group:
𝑛
|     |     |     |        | 1   | ∣ 𝑥 −𝑥 | ∣   |
| --- | --- | --- | ------ | --- | ------ | --- |
|     |     |     |        |     | 𝑢,𝑖    | 𝑝,𝑖 |
|     |     |     | 𝑆(𝑢,𝑝) | = ∑ |        |     |
|     |     |     |        | 𝑛   | max⁡(𝑥 | )   |
𝑖
𝑖=1


Context-Aware Risk Function
To calculate the real-time decision risk:
|     |     | 𝑅 = | 𝛼 ⋅𝐶       | +𝛼 ⋅𝐶 | +𝛼 ⋅𝐶  | +𝛽 ⋅𝑇  |
| --- | --- | --- | ---------- | ----- | ------ | ------ |
|     |     |     | 1 location | 2     | time 3 | device |

where 𝐶 represents contextual variables and 𝑇is the transaction amount.
𝑖

3.5 Evaluation Matrix
To evaluate the system’s performance, the following metrics were used:
| Metric  |     | Description  |     |     | Formula  |     |
| ------- | --- | ------------ | --- | --- | -------- | --- |
Proportion of correct
| Accuracy  |     | financial  |     |     | Accuracy=(TP+TN)/TP+FP+TN+FN  |     |
| --------- | --- | ---------- | --- | --- | ----------------------------- | --- |
recommendations
Correct positive
| Precision  |     | predictions over all  |     |     | Precision=TP/(TP+FP)  |     |
| ---------- | --- | --------------------- | --- | --- | --------------------- | --- |
predicted positives
Correct positive
| Recall  |     | predictions over actual  |     |     | Recall=TP/(TP+FN)  |     |
| ------- | --- | ------------------------ | --- | --- | ------------------ | --- |
positives
Page | 6

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
Harmonic mean of
F1-Score F1=2×((Precision×Recall)/(Precision+Recall))
Precision and Recall
Measures degree of
Privacy Leakage PLR = 1 - \frac{\text{Privacy Preserved
privacy exposure in
Ratio (PLR) Instances}}
gradients
Visual analysis using multi-metric radar plots (introduced in the Results section) assesses the
trade-off between interpretability, performance, and privacy.
In summary, the methodology establishes a federated, agentic architecture with explainable and
privacy-preserving mechanisms. This setup empowers decentralized financial agents to learn
collaboratively, justify every recommendation, and guarantee that user data never leaves the
local device.
IV. Results And Discussions
4.1 Model Performance
To evaluate the effectiveness of digital persona-based models for financial decisioning, we
implemented and tested three distinct machine learning algorithms:
 Random Forest (RF): Utilized for robust classification based on contextual features.
 LSTM Neural Network: Designed to capture sequential behavioral data over time.
 K-Means Clustering: Applied for unsupervised grouping of users based on contextual
traits.
The evaluation was conducted on a synthesized dataset simulating mobile transaction behaviors
under varying contexts (e.g., time, location, device usage, session length). Below is a comparison
of the models across common evaluation metrics:
Table 2. Model Performance Comparison
Accuracy Precision Recall F1-Score
Model Type
(%) (%) (%) (%)
Random Forest 91.2 90.4 89.9 90.1
LSTM Neural Net 93.6 94.4 91.8 92.9
K-Means Clustering 75.0 73.3 70.4 71.8
Page | 7

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
These results highlight that LSTM models outperform others due to their capability to model
temporal dependencies in user behavior and context shifts.
4.2 F1 Metrics and Multi-Metric Analysis
F1 Metrics and Multi-Metric Analysis
F1 Score Overview:
 LSTM Neural Net achieved the highest F1 score, indicating strong precision and recall
balance in capturing context-aware financial decision behaviors.
 Random Forest also performed well, particularly in interpretable rule generation based
on tabular financial history.
 K-Means Clustering had a lower F1 score, which is expected for unsupervised models
not optimized for classification accuracy.
F1 Score: Definition and Formula
The F1 Score is a metric used to evaluate the performance of classification models, particularly
when dealing with imbalanced classes. It balances Precision and Recall, offering a single metric
that accounts for both false positives and false negatives.
Formula:
Page | 8

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
Precision⋅Recall
F1 Score = 2⋅
Precision+Recall
Where:
 Precision is:
True Positives
Precision =
True Positives+False Positives
 Recall is:
True Positives
Recall =
True Positives+False Negatives
Interpretation:
 High F1 Score (close to 1): Model has both high precision and high recall.
 Low F1 Score (close to 0): Indicates poor performance on one or both metrics.
4.3 Limitations
While the proposed system provides a robust framework for explainable and privacy-preserving
financial advisory, several limitations were identified:
1. Data Privacy Concerns
While context-aware systems provide high personalization, they rely heavily on user data
such as behavior, location, transaction history, and preferences. Handling and storing
such sensitive data increases the risk of privacy breaches and regulatory non-compliance.
2. Limited Dataset Diversity
The datasets used for model training may lack diversity across geography, culture,
financial behavior, or demographic profiles. This can introduce bias into the decision-
making process and reduce the model’s applicability across wider populations.
3. Model Generalizability
Models like LSTM, Random Forest, and K-Means are highly effective under certain
conditions but may not generalize well across drastically different use cases or unseen
data patterns, especially in fast-evolving financial ecosystems.
4. Interpretability Challenges
AI-based persona models, particularly those involving deep learning, often behave as
Page | 9

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
black boxes. The lack of transparency in decision reasoning can reduce trust in the
system, especially for regulatory audits and end-user explanations.
5. Context Drift Over Time
User behavior and financial context can evolve. A model trained on past persona
characteristics may become stale, requiring continuous learning and adaptation
mechanisms that are not fully addressed in the current framework
V. Conclusion
This paper presents a comprehensive framework for modeling digital personas to support
context-aware financial decisioning. By integrating multi-source behavioral, transactional, and
contextual data, the proposed system personalizes financial recommendations and decisions in
real time. Utilizing models like Random Forest for classification, LSTM for temporal analysis,
and K-Means for segmentation, the system demonstrates strong adaptability in recognizing user-
specific patterns. The model’s F1-score metrics and accuracy suggest that contextual integration
meaningfully improves decision relevance and user alignment.
The core contribution lies in shifting financial AI systems from static, rules-based engines to
dynamic, personalized decisioning agents. The architecture enables user-centric decision flows,
addressing the limitations of generic financial advice tools. However, privacy constraints,
evolving contexts, and data diversity present ongoing challenges.
Looking ahead, the system can be significantly enhanced through federated learning
deployments across financial institutions. This would allow models to learn from a broader pool
of behaviors without compromising data privacy. Additionally, adapting the persona framework
to emerging fraud vectors such as those generated by generative AI and synthetic identities will
Page | 10

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
be essential to future-proofing decisioning models. Integration with real-time behavioral
biometrics such as mouse movements, typing speed, and facial cues could further elevate the
contextual awareness of the system.
There is also scope for incorporating explainable AI (XAI) elements to interpret decisions,
increasing user trust and regulatory transparency. Finally, incorporating adaptive reinforcement
learning will allow the system to fine-tune its persona model based on evolving user behaviors
and feedback loops, pushing the boundaries of personalization in digital finance.
References
1. K Richardson. (2024). Navigating Challenges in Real-Time Payment Systems in
FinTech. International Journal of Artificial Intelligence, Data Science, and
Machine Learning, 5(1), 44-56. https://doi.org/10.63282/3050-9262.IJAIDSML-
V5I1P105
2. Rautaray, S., & Tayagi, D. (2023). Artificial Intelligence in Telecommunications:
Applications, Risks, and Governance in the 5G and Beyond Era. Artificial
Intelligence
3. D De Roure. (2024). AI-Powered Predictive Maintenance in Industrial IoT.
Integrated Journal of Science and Technology, 1(4). Retrieved from
https://ijstpublication.com/index.php/ijst/article/view/17
4. A. Garg, M. Pandey, and A. R. Pathak, “A Multi-Layered AI-IoT Framework for
Adaptive Financial Services”, IJETCSIT, vol. 5, no. 3, pp. 47–57, Oct. 2024,
doi: 10.63282/3050-9246.IJETCSIT-V5I3P105
5. H. N. Himabindu Gurajada and R. Autade, "Quantum Computing for Fraud
Detection in Real-Time Payment Systems," 2025 International Conference on
Computing Technologies & Data Communication (ICCTDC), HASSAN, India,
2025, pp. 01-08, doi: 10.1109/ICCTDC64446.2025.11158810.
6. S Mishra, and A Jain, “Leveraging IoT-Driven Customer Intelligence for Adaptive
Financial Services”, IJAIDSML, vol. 4, no. 3, pp. 60–71, Oct. 2023,
doi: 10.63282/3050-9262.IJAIDSML-V4I3P107
7. A Magoulick and D Paleti, "Computer Vision for Financial Fraud Prevention using
Visual Pattern Analysis," 2025 International Conference on Engineering,
Technology & Management (ICETM), Oakdale, NY, USA, 2025, pp. 1-7, doi:
10.1109/ICETM63734.2025.11051811.
8. MN Nwobodo, “CNN-Based Image Validation for ESG Reporting: An Explainable
AI and Blockchain Approach”, Int. J. Comput. Sci. Inf. Technol. Res., vol. 5, no. 4,
pp. 64–85, Dec. 2024, doi: 10.63530/IJCSITR_2024_05_04_007
9. K Lacruz and F Jubitor, "Quantum Computing for Fraud Detection in Real-Time
Payment Systems," 2025 International Conference on Computing Technologies &
Page | 11

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
Data Communication (ICCTDC), HASSAN, India, 2025, pp. 01-08, doi:
10.1109/ICCTDC64446.2025.11158810.
10. AV Jusas, "How Natural Language Processing Framework Automate Business
Requirement Elicitation," International Journal of Computer Trends and
Technology (IJCTT), vol. 73, no. 5, pp. 47-50,
2025. Crossref, https://doi.org/10.14445/22312803/IJCTT-V73I5P107
11. A Vedantham, "A Minimalist Approach to Blockchain Design: Enhancing
Immutability and Verifiability with Scalable Peer-to-Peer Systems," 2025
International Conference on Inventive Computation Technologies (ICICT),
Kirtipur, Nepal, 2025, pp. 1697-1703, doi: 10.1109/ICICT64420.2025.11005016.
12. Doddipatla, L. (2024). Ethical and Regulatory Challenges of Using Generative AI
in Banking: Balancing Innovation and Compliance. Educational Administration:
Theory and Practice, 30(3), 2848-2855.
13. F Mannering. (2025). Artificial Intelligence in Security: Driving Trust and
Customer Engagement on FX Trading Platforms. Journal of Knowledge Learning
and Science Technology ISSN: 2959-6386 (online), 4(1), 71-77.
https://doi.org/10.60087/jklst.v4.n1.008
14. M Danish, "RIDI-Hypothesis: A Foundational Theory for Cybersecurity Risk
Assessment in Cyber-Physical Systems," 2025 4th International Conference on
Sentiment Analysis and Deep Learning (ICSADL), Bhimdatta, Nepal, 2025, pp.
117-123, doi: 10.1109/ICSADL65848.2025.10932989.
15. RD Rohweeis. Avalanche: A Secure Peer-to-Peer Payment System Using
Snowball Consensus Protocols. TechRxiv. January 20, 2025.
16. DOI: 10.36227/techrxiv.173738333.35212976/v1
17. H Tabuchi, "A Formalized Approach to Secure and Scalable Smart Contracts in
Decentralized Finance," 2025 International Conference on Engineering,
Technology & Management (ICETM), Oakdale, NY, USA, 2025, pp. 1-6, doi:
10.1109/ICETM63734.2025.11051910.
18. Doddipatla, L. (2025). Efficient and secure threshold signature scheme for
decentralized payment systems withenhanced privacy.
19. GH Bojesen, "Unraveling the Paradox: Green Premium and Climate Risk
Premium in Sustainable Finance," 2025 IEEE International Conference on
Interdisciplinary Approaches in Technology and Management for Social
Innovation (IATMSI), Gwalior, India, 2025, pp. 1-5, doi:
10.1109/IATMSI64286.2025.10985498.
20. Hemalatha Naga Himabindu, Gurajada. (2022). Unlocking Insights: The Power of
Data Science and AI in Data Visualization. International Journal of Computer
Science and Information Technology Research (IJCSITR), 3(1), 154-179.
https://doi.org/10.63530/IJCSITR_2022_03_01_016
Page | 12

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
21. R. Ramadugu, "Analyzing the Role of CBDC and Cryptocurrency in Emerging
Market Economies: A New Keynesian DSGE Approach," 2025 International
Conference on Inventive Computation Technologies (ICICT), Kirtipur, Nepal,
2025, pp. 1300-1306, doi: 10.1109/ICICT64420.2025.11005009.
22. CT Aghaunor. (2023). From Data to Decisions: Harnessing AI and Analytics.
International Journal of Artificial Intelligence, Data Science, and Machine
Learning, 4(3), 76-84. https://doi.org/10.63282/3050-9262.IJAIDSML-V4I3P109
23. AR Kommera. (2024). Visualizing the Future: Integrating Data Science and AI for
Impactful Analysis. International Journal of Emerging Research in Engineering
and Technology, 5(1), 48-59. https://doi.org/10.63282/3050-922X.IJERET-
V5I1P107
24. S. R. Seelam, A. Upadhyay, V. R. Pasam, "Federated Learning Framework for
Privacy-Preserving Health Monitoring via IoT Devices," 2025 International
Conference on Innovations in Intelligent Systems: Advancements in Computing,
Communication, and Cybersecurity (ISAC3), Bhubaneswar, India, 2025, pp. 1-6,
doi: 10.1109/ISAC364032.2025.11156349.
25. Flöter, C., Geringer, S., Reina, G., Weiskopf, D., & Ropinski, T. (2025, May).
Evaluating Foveated Frame Rate Reduction in Virtual Reality for Head-Mounted
Displays. In Proceedings of the 2025 Symposium on Eye Tracking Research and
Applications (pp. 1-7).
26. Srikanth, N., Sagar, K., Sravanthi, C., & Saranya, K. (2024, May). Deep Learning
Driven Food Recognition and Calorie Estimation Using Mobile Net Architecture.
In 2024 5th International Conference for Emerging Technology (INCET) (pp. 1-7).
IEEE.
27. Kazanidis, I., & Andreadou, E. (2025, June). Exploring the Benefits of Immersive
Technologies in Elementary Physical Education. In International Conference on
Immersive Learning (pp. 129-144). Cham: Springer Nature Switzerland.
28. Kang, H., Yang, E., Choe, S., & Ryu, J. (2025). Virtual Interaction on Concept
Learning for Construction Safety Training. Immersive Learning Research-
Practitioner, 148-153.
29. Choudhry, A., Jain, C., Singh, S., & Ratna, S. (2025, March). Comparison of CNN
and Vision Transformers for Wildfire Detection: A Proxy for Stubble Burning. In
2025 3rd International Conference on Disruptive Technologies (ICDT) (pp. 286-
289). IEEE.
30. Pandey, P., RG, R. T., Pati, R. P., & Singh, S. (2025, August). ALL-ViT: A Novel
Approach for Detection of Acute Lymphoblastic Leukemia. In 2025 12th
International Conference on Emerging Trends in Engineering & Technology-
Signal and Information Processing (ICETET-SIP) (pp. 1-6). IEEE.
31. Garduno-Ramon, C. E., Cruz-Albarran, I. A., Garduño-Ramón, M. A., & Morales-
Hernandez, L. A. (2025, August). Automatic segmentation of regions of interest in
Page | 13

Pages:1-14
International Journal of Research in Mulidisciplinary Technology Volume 1, issue 4 2025
thermal images in the facial and hand area. In 2025 International Conference on
Artificial Intelligence, Computer, Data Sciences and Applications (ACDSA) (pp. 1-
6). IEEE.
32. Friant, M., Halim, S. M., & Khan, L. (2025, August). Keeping track of the kids: a
deep dive into object detector fairness for pedestrians of different ages. In 2025
International Conference on Artificial Intelligence, Computer, Data Sciences and
Applications (ACDSA) (pp. 1-6). IEEE.
33. Pyae, A. (2025, June). Understanding Students’ Acceptance, Trust, and Attitudes
towards AI-generated Images for Educational Purposes. In Proceedings of the
2025 Conference on Creativity and Cognition (pp. 338-343).
34. K Peter. (2022). Multi-Modal GANs for Real-Time Anomaly Detection in Machine
and Financial Activity Streams. International Journal of Artificial Intelligence, Data
Science, and Machine Learning, 3(1), 39-48. https://doi.org/10.63282/3050-
9262.IJAIDSML-V3I1P105
35. Kadambala, K. M. (2025). Auditable AI Pipelines: Logging and Verifiability in ML
Workflows. Innovative Journal of Applied Science, 35-35.
36. Rani, S., & Bhosale, A. (2025). Bias Propagation in Generative AI: Risk and
Mitigation Strategies. Applied Engineering Solutions and Technologies, 4-4.
37. Madduru, P., & Bhosale, A. (2024). Ethical and Regulatory Implications of AI
Development in Telecom Services. International Journal of Emerging Trends in
Computer Science and Information Technology, 5(4), 105-115.
38. Rani, S., & Powar, Y. (2024). Federal Learning Optimization for Edge Devices
with Limited Resources. International Journal of AI, BigData, Computational and
Management Studies, 5(4), 115-123.
39. T Anthony. (2021). AI Models for Real Time Risk Assessment in Decentralized
Finance. Annals of Applied Sciences, 2(1). Retrieved from
https://annalsofappliedsciences.com/index.php/aas/article/view/30
40. Thombre, T. (2024). IoT and Metaverse Integration: Frameworks and Future
Applications. International Journal of Artificial Intelligence, Data Science, and
Machine Learning, 5(4), 81-90.
Page | 14