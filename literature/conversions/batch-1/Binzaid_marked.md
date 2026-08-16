---
conversion_metadata:
  converted_at: "2026-07-22T12:22:41Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Binzaid.pdf"
  source_pdf_sha256: "be8fa8e7b6dd2ab6bf605bcbda8911de9137eee0ff1771df64e8da737f452e24"
  page_count: 12
  markdown_char_count: 51540
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

Intelligent User Behavior Modeling for Customer Centric Fintech Product Decisions

Osama Binzaid

Dubai University of Information and Technology

Abstract:

The  exponential  growth  of  digital  financial  services  has  led  fintech  organizations  to  generate

massive volumes of user interaction data, offering unprecedented opportunities to improve product

decisions  using  intelligent  behavioral  modeling.  Traditional  product  development  approaches

often rely on intuition-driven or segmentation-based analyses that fail to capture dynamic, high-

frequency behavioral signals within fintech environments. This study proposes a comprehensive

user behavior modeling framework leveraging machine learning, natural language processing, and

behavioral  analytics  to  enable  customer-centric  fintech  product  decisions.  Using  multi-source

datasets  derived  from  14.2  million  user  interactions,  520,000  support  cases,  and  3.8  million

transactional events across six fintech verticals, the research evaluates the predictive performance

of  advanced  models  including  gradient  boosting,  deep  learning  autoencoders,  and  sequence

models.  Results  demonstrate  that  intelligent  behavior  modeling  improves  churn  prediction

accuracy  by  42%,  increases  feature  adoption  forecasting  precision  by  37%,  and  enhances

personalization outcomes by 34%. The findings reveal that user behavior signals—such as micro-

friction events, authentication patterns, risk behavior, and sentiment orientation—serve as strong

predictors of customer intent and product engagement.

Keywords:  User  behavior  modeling;  fintech  analytics;  customer-centric  decisions;  machine

learning

1. Introduction

37 | P a g e

---

<!-- PAGE 2 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

The  proliferation  of  digital  financial  services  has  fundamentally  transformed  user  expectations

relating to personalization, security, convenience, and reliability. As fintech platforms experience

exponential  adoption,  product  teams  face  increasing  pressure  to  understand  complex  user

behaviors  that  evolve  across  thousands  of  interactions  per  day.  Traditional  demographic  and

persona-driven  product  decision-making  frameworks  fail  to  accommodate  such  granular  and

dynamic  behavioral  shifts,  resulting  in  misaligned  features,  increased  friction,  and  reduced

customer  satisfaction.  The  rise  of  intelligent  user  behavior  modeling,  fueled  by  machine

learning, deep analytics, and cloud-native computation, now offers fintech organizations a data-

driven foundation for customer-centric product design.

User behavior in fintech is more intricate than in traditional digital platforms due to the interplay

between  financial  risk  perception,  trust  formation,  regulatory  constraints,  and  high-stakes

transactions. Users exhibit multi-layered behaviors driven not only by usability and convenience

but also by fear of fraud, privacy concerns, and financial literacy gaps. This necessitates behavior

modeling  frameworks  capable  of  capturing  both  overt  behavioral  patterns  (e.g.,  transaction

frequency, session duration) and latent psychological indicators (e.g., hesitation, trust formation,

sentiment  orientation).  Recent  industry  research  indicates  that  fintech  companies  adopting

behavioral  intelligence  models achieve up to  a 28% increase in  customer retention  (Accenture,

2024), highlighting the strategic importance of user-centric modeling.

Technological advancements further amplify this necessity. With the growing adoption of mobile

banking, digital wallets, robo-advisors, and AI-driven lending models, fintech platforms generate

high-frequency  logs  that  capture  user  interactions,  gestures,  keystrokes,  transaction  journeys,

customer support flows, risk scores, and authentication behavior. Integrating these heterogeneous

datasets requires sophisticated machine learning architectures capable of processing large-scale,

multi-modal information in real time. The emergence of deep sequence models, autoencoders, and

transformer-based architectures has made it feasible to analyze millions of behavioral signals and

38 | P a g e

---

<!-- PAGE 3 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

generate predictive insights that can directly inform product decisions, ranging from feature design

to risk mitigation strategies.

Despite  the  increasing  relevance  of  behavior  modeling,  academic  literature  addressing  its

application  in  fintech  product  decisions  remains  limited.  Many  existing  studies  focus  on

transactional  prediction,  fraud  analytics,  or  customer  segmentation  without  examining  how

behavior intelligence can drive strategic product choices across the entire product lifecycle. This

study  addresses  this  research  gap  by  proposing  an  end-to-end  intelligent  behavior  modeling

framework  and  empirically  evaluating  its  impact  on  customer-centric  decision-making  across

multiple fintech domains. This research contributes to both theoretical advancement and practical

strategies for integrating behavioral intelligence into fintech product ecosystems.

2. Literature Review

User  behavior  modeling  has  been  studied  extensively  in  digital  commerce,  social  media,  and

mobile  applications;  however,  its  application  in  fintech  poses  additional  complexity  due  to

characteristics  unique  to  financial  interactions.  Early  work  by  Furnell  &  Shah  (2018)  explored

behavioral authentication but emphasized its limited scope beyond security. Similarly, studies by

Lin et al. (2020) used behavioral clustering for mobile app optimization, but their models lacked

financial  contextualization.  In  contrast,  fintech-specific  behavior  has  been  studied  primarily

through  fraud  detection  frameworks,  such  as  those  described  by  Torres  et  al.  (2022),  who

highlighted anomalous financial activity patterns but did not extend their work to product decision

contexts.

Recent  research  has  expanded  the  scope  of  fintech  analytics.  Sharma  and  Goyal  (2021)

demonstrated that machine learning models could predict customer churn with up to 78% accuracy

in  mobile  banking  platforms  based  on  transactional  behavior.  Meanwhile,  research  by  Xu  and

Zhang (2022) found that sentiment extracted from customer support conversations plays a critical

39 | P a g e

---

<!-- PAGE 4 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

role in predicting dissatisfaction. These findings suggest that behavior modeling can provide strong

predictive signals for customer-centric product enhancements.

The  evolution  of  deep  learning  has  further  influenced  behavior  analysis.  Autoencoder-based

interaction pattern analysis by Esteban et al. (2020) showed promise in identifying friction signals

in user journeys. Sequence modeling approaches (e.g., LSTM networks) demonstrated predictive

capability in behavioral  forecasting, with Kim et al. (2023) showing that sequential transaction

data significantly improves financial intent prediction. More recently, transformer-based models

(BERT, RoBERTa, FinBERT) were adapted for behavior-rich textual data in fintech, allowing for

nuanced understanding of sentiment and intent.

Despite  this  progress,  the  literature  highlights  key  research  gaps.  Most  studies  remain  siloed,

focusing  on  fraud,  churn,  or  risk  independently,  rather  than  integrating  behavioral  insights  to

inform  product  design.  Additionally,  limited  research  explores  how  multi-modal  behavior—

combining session analytics, sentiment, risk behavior, and transaction patterns—can be integrated

into  a  unified  decision  model.  There  is  also  a  lack  of  empirical  evidence  on  how  behavioral

modeling influences roadmap development, feature prioritization, and long-term product adoption.

This study builds on this fragmented literature to propose a multidimensional behavior modeling

framework tailored for fintech product decisions.

3. Methodology

This  research  systemically  combines  quantitative  modeling,  machine  learning  experimentation,

and empirical validation using multi-source dataset streams.

3.1 Data Acquisition

Data were collected from six fintech platforms across digital banking, lending, personal finance

management, wealth-tech, and payments. The dataset includes:

40 | P a g e

---

<!-- PAGE 5 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

  14.2 million user interaction logs

  3.8 million transactions

  520,000 customer support cases

  82,000 mobile session recordings

  96,000 authentication sequences

  11,400 user offboarding interviews

3.2 Preprocessing Pipeline

Key preprocessing steps included:

  Session reconstruction from raw clickstreams

  Behavior encoding using Bi-LSTM autoencoders

  Sentiment extraction from text using FinBERT

  Normalization of time-series behavioral sequences

  Clustering of friction signals via DBSCAN

  Feature engineering (hesitation index, multi-step abandonment, behavioral volatility, trust

score)

3.3 Behavioral Modeling Framework

The modeling framework consists of:

1.  Interaction Behavior Modeling

o  Gradient boosting to predict feature adoption likelihood.

2.  Sequential Journey Analysis

o  LSTM sequence models for forecasting churn behavior.

3.  Sentiment and Intent Modeling

o  Transformer-based NLP for extracting frustration and positive engagement.

41 | P a g e

---

<!-- PAGE 6 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

4.  Risk Behavior Analysis

o  Anomaly detection for unusual transaction sequences or authentication failures.

5.  Unified

Behavioral

Score

(UBS)

A composite index generated from standardized outputs of all models.

3.4 Evaluation Metrics

  Precision/recall for churn classification

  RMSE for adoption prediction

  Sentiment classification accuracy

  Behavioral segmentation stability

  Business outcome uplift

4. Results

The results of this study demonstrate that intelligent behavior modeling significantly enhances the

accuracy  and  efficiency  of  customer-centric  product  decision-making  in  fintech  environments.

One  of  the  strongest  findings  emerged  from  the  churn  prediction  models.  Using  LSTM-based

sequential  behavior  analysis,  churn  prediction  accuracy  improved  from  61%  (baseline  gradient

boosting model) to  86% when incorporating behavioral  time-series data.  This  substantial  uplift

suggests that behavioral sequences—such as repeated authentication failures, transaction denials,

or multi-step form abandonment—contain powerful signals that precede user attrition. Analyzing

these fine-grained patterns enabled the model to identify micro-frictions that were not detectable

through aggregated engagement metrics. As a result, product teams were able to intervene earlier

through personalized nudges, friction-point redesigns, or tailored customer support, leading to a

measurable reduction in actual churn over a six-month validation period.

Feature  adoption  forecasting  also  showed  significant  performance  improvements.  Traditional

models that relied on demographic and static  engagement data  achieved  a precision of 48% in

42 | P a g e

---

<!-- PAGE 7 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

predicting  which new  features users would  adopt.  In contrast,  the proposed behavior modeling

framework increased precision to 85% by incorporating behavioral embeddings, intent sentiment,

and risk profiles. The analysis revealed that user intent is strongly influenced by trust signals—

users who demonstrated hesitation patterns during sensitive operations (e.g., card linking, high-

value transfers) were less likely to adopt advanced financial features such as automated investing

or  multi-country  remittances.  By  quantifying  these  hesitation  indicators,  the  model  provided

product  teams  with  granular  insights  that  guided  both  feature  design  and  onboarding  strategy

adjustments.

Another  major  outcome  relates  to  personalization  effectiveness.  Behavior-driven  segmentation

produced  significantly  more  stable  and  meaningful  customer  clusters  compared  to  traditional

segmentation  approaches.  Instead  of  grouping  users  solely  by  financial  demographics  or

transaction frequency, the intelligent model grouped users based on patterns such as risk-taking

behavior, trust-building phases, frustration signatures, session rhythms, and propensity to explore

new  features.  As  a  result,  personalized  product  recommendations  generated  through  these

behavioral segments improved feature engagement by 34%. For example, users identified as “risk-

cautious”  responded  positively  to  educational  prompts  and  lower-risk  offerings,  whereas

“exploratory users” reacted strongly to new feature notifications and beta programs.

Customer  support  insights  further  reinforced  the  value  of  intelligent  behavioral  modeling.

Sentiment analysis of 520,000 conversations revealed that user frustration often emerged two to

three  days  before  a  support  ticket  was  created.  By  correlating  sentiment  shifts  with  behavioral

anomalies—such as repeated back-and-forth navigation, re-authentication loops, or slow-loading

pages—the model was able to flag downward sentiment trajectories in real time. This predictive

insight  allowed  product  teams  to  proactively  deploy  fixes,  targeted  communication,  or  in-app

guidance. Over a four-month pilot, this system reduced severe escalation rates by 22%.

43 | P a g e

---

<!-- PAGE 8 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

Finally,  the  unified  behavioral  score  (UBS)  proved  to  be  a  strong  predictor  of  long-term  user

loyalty and satisfaction. Users with consistently high UBS values displayed a 41% higher retention

rate and a 33% higher lifetime value. The UBS metric aggregated interaction quality, sentiment

orientation, behavioral stability, and risk indicators, offering product teams a holistic measure for

tracking  the  health  of  user-product  relationships.  The  compelling  improvements  across  churn

reduction,  forecasting  accuracy,  personalization  uplift,  and  predictive  sentiment  modeling

collectively  establish  intelligent  behavior  modeling  as  a  powerful  engine  for  customer-centric

fintech product decisions.

5. Discussion

The  findings  of  this  study  underscore  the  transformative  potential  of  intelligent  user  behavior

modeling  in  shaping  customer-centric  fintech  product  strategies.  The  substantial  uplift  in

predictive performance across churn detection, adoption forecasting, and personalization reflects

the strategic value of integrating multi-modal behavioral  data, sentiment  intelligence,  and deep

sequence  modeling.  Traditional  product  decision-making  frameworks—often  linear,  static,  and

intuition-driven—prove  inadequate  in  environments  where  user  behavior  is  dynamic,  context-

dependent,  and  sensitive  to  micro-frictions.  The  empirical  results  show  that  behavioral  signals

serve as leading indicators of customer satisfaction, trust levels, and intent formation, providing

product teams with actionable intelligence long before issues escalate.

The implications extend far beyond operational enhancements. Behavior modeling fundamentally

reshapes  how  fintech  organizations  conceptualize  their  product  roadmaps.  By  quantifying  user

intent and psychological friction, organizations can design features that align more closely with

actual  user  needs  rather  than  assumed  requirements.  Moreover,  the  ability  to  detect  emerging

patterns—such  as  increasing  frustration  in  a  specific  user  segment  or  early  disengagement

following  a  product  update—supports  continuous  product  evolution  grounded  in  measurable

44 | P a g e

---

<!-- PAGE 9 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

behavioral  insights.  This  aligns  with  broader  Industry  5.0  principles  emphasizing  hyper-

personalization, human-centered financial experiences, and AI-augmented decision-making.

The  results  also  highlight  the  importance  of  integrating  behavioral  intelligence  within  risk

management. Behavior anomalies are often early signals of financial distress, fraud risk, or trust

breakdown. Incorporating risk-aware behavioral models helps fintech firms refine authentication

workflows,  strengthen  fraud  detection,  and  enhance  user  education.  This  integrative  approach

bridges the gap between product teams, risk teams, and customer experience teams—driving more

cohesive, aligned operational strategies.

Challenges remain, particularly concerning data governance, privacy, and ethical use of behavioral

models.  Behavioral  data,  especially  related  to  financial  interactions,  is  sensitive  and  must  be

processed within strict legal and ethical frameworks. Future research should explore governance

models  that  support  transparent,  fair,  and  privacy-compliant  behavioral  modeling  in  fintech

ecosystems.

6. Conclusion

This study demonstrates that intelligent user behavior modeling provides a powerful foundation

for enhancing customer-centric decision-making in fintech product development. By integrating

deep behavioral analytics, sentiment modeling, and predictive machine learning architectures, the

proposed framework significantly improves predictive accuracy across churn forecasting, feature

adoption,  sentiment  shifts,  and  personalization  outcomes.  These  improvements  highlight  the

importance of leveraging multi-dimensional behavior signals—such as session patterns, hesitation

indices,  transaction  sequences,  and  sentiment  trajectories—to  understand  user  motivation  and

challenges at a granular level. The empirical findings show strong practical benefits, including a

42% improvement in churn prediction, 37% higher feature forecasting precision, and a 34% uplift

in personalized engagement.

45 | P a g e

---

<!-- PAGE 10 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

References

1.  Arooj  Hassan,  Malik  Arfat  Hassan,  &  Muhammad  Ahsan  Khan.  (2025).  Quantum-
Resistant  Cryptography  in  Cloud-Based  Fintech  Solutions.  Aminu  Kano  Academic 
Scholars Association Multidisciplinary Journal, 2(3), 267-286.

2.  Hassan,  Arooj,  Muhammad  Ahsan  Khan,  and  Malik  Arfat  Hassan.  "AI-Driven  Product 
Roadmaps in Fintech, Optimizing User Experience and Security Trade-offs." International 
Journal of Business & Digital Economy 1, no. 01 (2025): 1-13.

3.  Hassan, Arooj, Malik Arfat Hassan, and Muhammad Ahsan Khan. "Design Thinking for 
Secure Fintech Products: Balancing Innovation and Compliance." Econova 2, no. 1 (2025): 
1-16.

4.  Hassan,  Arooj,  Muhammad  Ahsan  Khan,  and  Malik  Arfat  Hassan.  "Sustainable  Cloud 
Product  Strategies  for  Green  Fintech  and  secure  Digital  Finance."  CogNexus  1,  no.  03 
(2025): 162-176.

5.  Hassan, Arooj, Muhammad Ahsan Khan, and Malik Arfat Hassan. "Product Management 
Challenges in AI-Enhanced Fintech Fraud." International Journal of Business & Digital 
Economy 1, no. 01 (2025): 14-28.

6.  Hassan,  Arooj,  Muhammad  Ahsan  Khan,  and  Malik  Arfat  Hassan.  "AI-Driven  Product 
Roadmaps in Fintech, Optimizing User Experience and Security Trade-offs." International 
Journal of Business & Digital Economy 1, no. 01 (2025): 1-13.

7.  Hassan,  Arooj,  Malik  Arfat  Hassan,  and  Muhammad  Ahsan  Khan.  "Threat  Intelligence 
Automation in Fintech, A Product Management Perspective." Multiverse Journal 1, no. 2 
(2024): 50-62.

8.  Hassan, Arooj, Muhammad Ahsan Khan, and Malik Arfat Hassan. "Impact of Regulatory 
Compliance  PSD2,  GDPR  on  Fintech  Product  Design."  Frontiers  in  Multidisciplinary 
Studies 1, no. 01 (2024): 59-72.

9.  Hassan, Arooj, Muhammad Ahsan Khan, and Malik Arfat Hassan. "Integrating Cyber Risk 
Metrics into Fintech Product Lifecycle Management." Econova 1, no. 01 (2024): 42-53. 
10. Hassan, Arooj, Malik Arfat Hassan, and Muhammad Ahsan Khan. "Evaluating Zero Trust 
Security Models for Fintech Cloud  Infrastructures." Multiverse Journal 1, no. 1 (2024): 
52-60.

11. Hassan,  Arooj,  Malik  Arfat  Hassan,  and  Muhammad  Ahsan  Khan.  "The  Role  of  Cloud 
Compliance Automation  in  Scaling Fintech Products  Globally." Journal  of  Educational 
Research in Developing Areas 4, no. 2 (2023): 245-255.

46 | P a g e

---

<!-- PAGE 11 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

12. Hassan, Arooj, Malik Arfat Hassan, and Muhammad Ahsan Khan. "Multi-Cloud Strategies 
for  Scalable  and  Secure  Fintech  Applications."  Journal  of  Educational  Research  in 
Developing Areas 4, no. 1 (2023): 123-133.

13. Nabi, Hussain Abdul, Ali Abbas Hussain, Abdul Karim Sajid Ali, and Haroon Arif. "Data-
Driven  ERP  Solutions  Integrated  with  AI  for  Streamlined  Marketing  Operations  and 
Resilient Supply Chain Networks." The Asian Bulletin of Big Data Management 5, no. 2 
(2025): 115-128.

14. Arif,  Haroon,  Abdul  Karim  Sajid  Ali,  Aamir  Raza,  and  Aashesh  Kumar.  "Adversarial 
Attacks  on  AI  Diagnostic  Tools:  Assessing  Risks  and  Developing  Mitigation 
Strategies." Frontier in Medical and Health Research 3, no. 1 (2025): 317-332.

15. Arif, Haroon, Ali Abbas Hussain, Hussain Abdul Nabi, and Abdul Karim Sajid Ali. "AI 
POWERED DETECTION OF ADVERSARIAL AND SUPPLY CHAIN ATTACKS ON 
GENERATIVE MODELS."

16. Arif,  H.,  Ali,  A.  K.  S.,  &  Nabi,  H.  A.  (2025).  IoT  Security  through  ML/DL:  Software 
Engineering Challenges and Directions. ICCK Journal of Software Engineering, 1(2), 90–
108. https://doi.org/10.62762/JSE.2025.372865

17. Arif,  Haroon,  Aashesh  Kumar,  Muhammad  Fahad,  and  Hafiz  Khawar  Hussain.  "Future 
horizons: AI-enhanced threat detection in cloud environments: Unveiling opportunities for 
research." International journal of multidisciplinary sciences and arts 3, no. 1 (2024): 242-
251.

INTRUSION  DETECTION  AND  DATA  PROTECTION

18. Ali,  Abdul  Karim  Sajid,  Aamir  Raza,  Haroon  Arif,  and  Ali  Abbas  Hussain. 
"INTELLIGENT 
IN 
INFORMATION SECURITY USING ARTIFICIAL INTELLIGENCE AND MACHINE 
LEARNING TECHNIQUES." Spectrum of Engineering Sciences 3, no. 4 (2025): 818-828. 
19. Fahad, Muhammad, Aashesh Kumar, Haroon Arif, and Hafiz Khawar Hussain. "Mastering 
apt  defense:  strategies, technologies, and  collaboration." BIN: Bulletin Of Informatics 1 
(2023): 84-94.

20. Ghelani,  Harshitkumar.  "AI-Driven  Quality  Control  in  PCB  Manufacturing:  Enhancing 
Production Efficiency and Precision." Valley International Journal Digital Library (2024): 
1549-1564.

21. Ghelani,  Harshitkumar.  "Advanced  AI  Technologies  for  Defect  Prevention  and  Yield 
Optimization  in  PCB  Manufacturing."  International  Journal  Of  Engineering  And 
Computer Science 13, no. 10 (2024).

47 | P a g e

---

<!-- PAGE 12 -->

Unique Journal of Artificial Intelligence (UJAI)

Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

22. Ghelani,  Harshitkumar.  "Six  Sigma  and  Continuous  Improvement  Strategies:  A 
Comparative Analysis in Global Manufacturing Industries." Valley International Journal 
Digital Library (2023): 954-972.

23. Ghelani, Harshitkumar. "Automated Defect Detection in Printed Circuit Boards: Exploring 
the Impact of Convolutional Neural Networks on Quality Assurance and Environmental 
Sustainability  in  Manufacturing."  International  Journal  of  Advanced  Engineering 
Technologies and Innovations 1: 275-289.

24. Ghelani,  Harshitkumar.

"Harnessing  AI

Inspection:  Developing 
Environmentally Friendly Frameworks for PCB Quality Control Using Energy-Efficient 
Machine  Learning  Algorithms."  International  Journal  of  Advanced  Engineering 
Technologies and Innovations 1: 146-154.

for  Visual

25. Ghelani, Harshitkumar. "Enhancing PCB Quality Control through AI-Driven Inspection: 
Leveraging Convolutional Neural Networks for Automated Defect Detection in Electronic 
Manufacturing Environments." Available at SSRN 5160737 (2024).

26. Ghelani,  Harshitkumar.  "Advances  in  lean  manufacturing:  improving  quality  and 
efficiency  in  modern  production  systems."  Valley  International  Journal  Digital 
Library (2021): 611-625.

27. Ghelani, Harshitkumar. "Revolutionizing Visual Inspection Frameworks: The Integration 
of Machine Learning and Energy-Efficient Techniques in PCB Quality Control Systems 
for Sustainable Production." International Journal of Advanced Engineering Technologies 
and Innovations 1: 521-538.

48 | P a g e

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

Intelligent User Behavior Modeling for Customer Centric Fintech Product Decisions

Osama Binzaid

Dubai University of Information and Technology

Abstract:

The  exponential  growth  of  digital  financial  services  has  led  fintech  organizations  to  generate

massive volumes of user interaction data, offering unprecedented opportunities to improve product

decisions  using  intelligent  behavioral  modeling.  Traditional  product  development  approaches

often rely on intuition-driven or segmentation-based analyses that fail to capture dynamic, high-

frequency behavioral signals within fintech environments. This study proposes a comprehensive

user behavior modeling framework leveraging machine learning, natural language processing, and

behavioral  analytics  to  enable  customer-centric  fintech  product  decisions.  Using  multi-source

datasets  derived  from  14.2  million  user  interactions,  520,000  support  cases,  and  3.8  million

transactional events across six fintech verticals, the research evaluates the predictive performance

of  advanced  models  including  gradient  boosting,  deep  learning  autoencoders,  and  sequence

models.  Results  demonstrate  that  intelligent  behavior  modeling  improves  churn  prediction

accuracy  by  42%,  increases  feature  adoption  forecasting  precision  by  37%,  and  enhances

personalization outcomes by 34%. The findings reveal that user behavior signals—such as micro-

friction events, authentication patterns, risk behavior, and sentiment orientation—serve as strong

predictors of customer intent and product engagement.

Keywords:  User  behavior  modeling;  fintech  analytics;  customer-centric  decisions;  machine

learning

1. Introduction

37 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

The  proliferation  of  digital  financial  services  has  fundamentally  transformed  user  expectations

relating to personalization, security, convenience, and reliability. As fintech platforms experience

exponential  adoption,  product  teams  face  increasing  pressure  to  understand  complex  user

behaviors  that  evolve  across  thousands  of  interactions  per  day.  Traditional  demographic  and

persona-driven  product  decision-making  frameworks  fail  to  accommodate  such  granular  and

dynamic  behavioral  shifts,  resulting  in  misaligned  features,  increased  friction,  and  reduced

customer  satisfaction.  The  rise  of  intelligent  user  behavior  modeling,  fueled  by  machine

learning, deep analytics, and cloud-native computation, now offers fintech organizations a data-

driven foundation for customer-centric product design.

User behavior in fintech is more intricate than in traditional digital platforms due to the interplay

between  financial  risk  perception,  trust  formation,  regulatory  constraints,  and  high-stakes

transactions. Users exhibit multi-layered behaviors driven not only by usability and convenience

but also by fear of fraud, privacy concerns, and financial literacy gaps. This necessitates behavior

modeling  frameworks  capable  of  capturing  both  overt  behavioral  patterns  (e.g.,  transaction

frequency, session duration) and latent psychological indicators (e.g., hesitation, trust formation,

sentiment  orientation).  Recent  industry  research  indicates  that  fintech  companies  adopting

behavioral  intelligence  models achieve up to  a 28% increase in  customer retention  (Accenture,

2024), highlighting the strategic importance of user-centric modeling.

Technological advancements further amplify this necessity. With the growing adoption of mobile

banking, digital wallets, robo-advisors, and AI-driven lending models, fintech platforms generate

high-frequency  logs  that  capture  user  interactions,  gestures,  keystrokes,  transaction  journeys,

customer support flows, risk scores, and authentication behavior. Integrating these heterogeneous

datasets requires sophisticated machine learning architectures capable of processing large-scale,

multi-modal information in real time. The emergence of deep sequence models, autoencoders, and

transformer-based architectures has made it feasible to analyze millions of behavioral signals and

38 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

generate predictive insights that can directly inform product decisions, ranging from feature design

to risk mitigation strategies.

Despite  the  increasing  relevance  of  behavior  modeling,  academic  literature  addressing  its

application  in  fintech  product  decisions  remains  limited.  Many  existing  studies  focus  on

transactional  prediction,  fraud  analytics,  or  customer  segmentation  without  examining  how

behavior intelligence can drive strategic product choices across the entire product lifecycle. This

study  addresses  this  research  gap  by  proposing  an  end-to-end  intelligent  behavior  modeling

framework  and  empirically  evaluating  its  impact  on  customer-centric  decision-making  across

multiple fintech domains. This research contributes to both theoretical advancement and practical

strategies for integrating behavioral intelligence into fintech product ecosystems.

2. Literature Review

User  behavior  modeling  has  been  studied  extensively  in  digital  commerce,  social  media,  and

mobile  applications;  however,  its  application  in  fintech  poses  additional  complexity  due  to

characteristics  unique  to  financial  interactions.  Early  work  by  Furnell  &  Shah  (2018)  explored

behavioral authentication but emphasized its limited scope beyond security. Similarly, studies by

Lin et al. (2020) used behavioral clustering for mobile app optimization, but their models lacked

financial  contextualization.  In  contrast,  fintech-specific  behavior  has  been  studied  primarily

through  fraud  detection  frameworks,  such  as  those  described  by  Torres  et  al.  (2022),  who

highlighted anomalous financial activity patterns but did not extend their work to product decision

contexts.

Recent  research  has  expanded  the  scope  of  fintech  analytics.  Sharma  and  Goyal  (2021)

demonstrated that machine learning models could predict customer churn with up to 78% accuracy

in  mobile  banking  platforms  based  on  transactional  behavior.  Meanwhile,  research  by  Xu  and

Zhang (2022) found that sentiment extracted from customer support conversations plays a critical

39 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

role in predicting dissatisfaction. These findings suggest that behavior modeling can provide strong

predictive signals for customer-centric product enhancements.

The  evolution  of  deep  learning  has  further  influenced  behavior  analysis.  Autoencoder-based

interaction pattern analysis by Esteban et al. (2020) showed promise in identifying friction signals

in user journeys. Sequence modeling approaches (e.g., LSTM networks) demonstrated predictive

capability in behavioral  forecasting, with Kim et al. (2023) showing that sequential transaction

data significantly improves financial intent prediction. More recently, transformer-based models

(BERT, RoBERTa, FinBERT) were adapted for behavior-rich textual data in fintech, allowing for

nuanced understanding of sentiment and intent.

Despite  this  progress,  the  literature  highlights  key  research  gaps.  Most  studies  remain  siloed,

focusing  on  fraud,  churn,  or  risk  independently,  rather  than  integrating  behavioral  insights  to

inform  product  design.  Additionally,  limited  research  explores  how  multi-modal  behavior—

combining session analytics, sentiment, risk behavior, and transaction patterns—can be integrated

into  a  unified  decision  model.  There  is  also  a  lack  of  empirical  evidence  on  how  behavioral

modeling influences roadmap development, feature prioritization, and long-term product adoption.

This study builds on this fragmented literature to propose a multidimensional behavior modeling

framework tailored for fintech product decisions.

3. Methodology

This  research  systemically  combines  quantitative  modeling,  machine  learning  experimentation,

and empirical validation using multi-source dataset streams.

3.1 Data Acquisition

Data were collected from six fintech platforms across digital banking, lending, personal finance

management, wealth-tech, and payments. The dataset includes:

40 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

  14.2 million user interaction logs

  3.8 million transactions

  520,000 customer support cases

  82,000 mobile session recordings

  96,000 authentication sequences

  11,400 user offboarding interviews

3.2 Preprocessing Pipeline

Key preprocessing steps included:

  Session reconstruction from raw clickstreams

  Behavior encoding using Bi-LSTM autoencoders

  Sentiment extraction from text using FinBERT

  Normalization of time-series behavioral sequences

  Clustering of friction signals via DBSCAN

  Feature engineering (hesitation index, multi-step abandonment, behavioral volatility, trust

score)

3.3 Behavioral Modeling Framework

The modeling framework consists of:

1.  Interaction Behavior Modeling

o  Gradient boosting to predict feature adoption likelihood.

2.  Sequential Journey Analysis

o  LSTM sequence models for forecasting churn behavior.

3.  Sentiment and Intent Modeling

o  Transformer-based NLP for extracting frustration and positive engagement.

41 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

4.  Risk Behavior Analysis

o  Anomaly detection for unusual transaction sequences or authentication failures.

5.  Unified

Behavioral

Score

(UBS)

A composite index generated from standardized outputs of all models.

3.4 Evaluation Metrics

  Precision/recall for churn classification

  RMSE for adoption prediction

  Sentiment classification accuracy

  Behavioral segmentation stability

  Business outcome uplift

4. Results

The results of this study demonstrate that intelligent behavior modeling significantly enhances the

accuracy  and  efficiency  of  customer-centric  product  decision-making  in  fintech  environments.

One  of  the  strongest  findings  emerged  from  the  churn  prediction  models.  Using  LSTM-based

sequential  behavior  analysis,  churn  prediction  accuracy  improved  from  61%  (baseline  gradient

boosting model) to  86% when incorporating behavioral  time-series data.  This  substantial  uplift

suggests that behavioral sequences—such as repeated authentication failures, transaction denials,

or multi-step form abandonment—contain powerful signals that precede user attrition. Analyzing

these fine-grained patterns enabled the model to identify micro-frictions that were not detectable

through aggregated engagement metrics. As a result, product teams were able to intervene earlier

through personalized nudges, friction-point redesigns, or tailored customer support, leading to a

measurable reduction in actual churn over a six-month validation period.

Feature  adoption  forecasting  also  showed  significant  performance  improvements.  Traditional

models that relied on demographic and static  engagement data  achieved  a precision of 48% in

42 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

predicting  which new  features users would  adopt.  In contrast,  the proposed behavior modeling

framework increased precision to 85% by incorporating behavioral embeddings, intent sentiment,

and risk profiles. The analysis revealed that user intent is strongly influenced by trust signals—

users who demonstrated hesitation patterns during sensitive operations (e.g., card linking, high-

value transfers) were less likely to adopt advanced financial features such as automated investing

or  multi-country  remittances.  By  quantifying  these  hesitation  indicators,  the  model  provided

product  teams  with  granular  insights  that  guided  both  feature  design  and  onboarding  strategy

adjustments.

Another  major  outcome  relates  to  personalization  effectiveness.  Behavior-driven  segmentation

produced  significantly  more  stable  and  meaningful  customer  clusters  compared  to  traditional

segmentation  approaches.  Instead  of  grouping  users  solely  by  financial  demographics  or

transaction frequency, the intelligent model grouped users based on patterns such as risk-taking

behavior, trust-building phases, frustration signatures, session rhythms, and propensity to explore

new  features.  As  a  result,  personalized  product  recommendations  generated  through  these

behavioral segments improved feature engagement by 34%. For example, users identified as “risk-

cautious”  responded  positively  to  educational  prompts  and  lower-risk  offerings,  whereas

“exploratory users” reacted strongly to new feature notifications and beta programs.

Customer  support  insights  further  reinforced  the  value  of  intelligent  behavioral  modeling.

Sentiment analysis of 520,000 conversations revealed that user frustration often emerged two to

three  days  before  a  support  ticket  was  created.  By  correlating  sentiment  shifts  with  behavioral

anomalies—such as repeated back-and-forth navigation, re-authentication loops, or slow-loading

pages—the model was able to flag downward sentiment trajectories in real time. This predictive

insight  allowed  product  teams  to  proactively  deploy  fixes,  targeted  communication,  or  in-app

guidance. Over a four-month pilot, this system reduced severe escalation rates by 22%.

43 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

Finally,  the  unified  behavioral  score  (UBS)  proved  to  be  a  strong  predictor  of  long-term  user

loyalty and satisfaction. Users with consistently high UBS values displayed a 41% higher retention

rate and a 33% higher lifetime value. The UBS metric aggregated interaction quality, sentiment

orientation, behavioral stability, and risk indicators, offering product teams a holistic measure for

tracking  the  health  of  user-product  relationships.  The  compelling  improvements  across  churn

reduction,  forecasting  accuracy,  personalization  uplift,  and  predictive  sentiment  modeling

collectively  establish  intelligent  behavior  modeling  as  a  powerful  engine  for  customer-centric

fintech product decisions.

5. Discussion

The  findings  of  this  study  underscore  the  transformative  potential  of  intelligent  user  behavior

modeling  in  shaping  customer-centric  fintech  product  strategies.  The  substantial  uplift  in

predictive performance across churn detection, adoption forecasting, and personalization reflects

the strategic value of integrating multi-modal behavioral  data, sentiment  intelligence,  and deep

sequence  modeling.  Traditional  product  decision-making  frameworks—often  linear,  static,  and

intuition-driven—prove  inadequate  in  environments  where  user  behavior  is  dynamic,  context-

dependent,  and  sensitive  to  micro-frictions.  The  empirical  results  show  that  behavioral  signals

serve as leading indicators of customer satisfaction, trust levels, and intent formation, providing

product teams with actionable intelligence long before issues escalate.

The implications extend far beyond operational enhancements. Behavior modeling fundamentally

reshapes  how  fintech  organizations  conceptualize  their  product  roadmaps.  By  quantifying  user

intent and psychological friction, organizations can design features that align more closely with

actual  user  needs  rather  than  assumed  requirements.  Moreover,  the  ability  to  detect  emerging

patterns—such  as  increasing  frustration  in  a  specific  user  segment  or  early  disengagement

following  a  product  update—supports  continuous  product  evolution  grounded  in  measurable

44 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

behavioral  insights.  This  aligns  with  broader  Industry  5.0  principles  emphasizing  hyper-

personalization, human-centered financial experiences, and AI-augmented decision-making.

The  results  also  highlight  the  importance  of  integrating  behavioral  intelligence  within  risk

management. Behavior anomalies are often early signals of financial distress, fraud risk, or trust

breakdown. Incorporating risk-aware behavioral models helps fintech firms refine authentication

workflows,  strengthen  fraud  detection,  and  enhance  user  education.  This  integrative  approach

bridges the gap between product teams, risk teams, and customer experience teams—driving more

cohesive, aligned operational strategies.

Challenges remain, particularly concerning data governance, privacy, and ethical use of behavioral

models.  Behavioral  data,  especially  related  to  financial  interactions,  is  sensitive  and  must  be

processed within strict legal and ethical frameworks. Future research should explore governance

models  that  support  transparent,  fair,  and  privacy-compliant  behavioral  modeling  in  fintech

ecosystems.

6. Conclusion

This study demonstrates that intelligent user behavior modeling provides a powerful foundation

for enhancing customer-centric decision-making in fintech product development. By integrating

deep behavioral analytics, sentiment modeling, and predictive machine learning architectures, the

proposed framework significantly improves predictive accuracy across churn forecasting, feature

adoption,  sentiment  shifts,  and  personalization  outcomes.  These  improvements  highlight  the

importance of leveraging multi-dimensional behavior signals—such as session patterns, hesitation

indices,  transaction  sequences,  and  sentiment  trajectories—to  understand  user  motivation  and

challenges at a granular level. The empirical findings show strong practical benefits, including a

42% improvement in churn prediction, 37% higher feature forecasting precision, and a 34% uplift

in personalized engagement.

45 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

References

1.  Arooj  Hassan,  Malik  Arfat  Hassan,  &  Muhammad  Ahsan  Khan.  (2025).  Quantum-
Resistant  Cryptography  in  Cloud-Based  Fintech  Solutions.  Aminu  Kano  Academic
Scholars Association Multidisciplinary Journal, 2(3), 267-286.

2.  Hassan,  Arooj,  Muhammad  Ahsan  Khan,  and  Malik  Arfat  Hassan.  "AI-Driven  Product
Roadmaps in Fintech, Optimizing User Experience and Security Trade-offs." International
Journal of Business & Digital Economy 1, no. 01 (2025): 1-13.

3.  Hassan, Arooj, Malik Arfat Hassan, and Muhammad Ahsan Khan. "Design Thinking for
Secure Fintech Products: Balancing Innovation and Compliance." Econova 2, no. 1 (2025):
1-16.

4.  Hassan,  Arooj,  Muhammad  Ahsan  Khan,  and  Malik  Arfat  Hassan.  "Sustainable  Cloud
Product  Strategies  for  Green  Fintech  and  secure  Digital  Finance."  CogNexus  1,  no.  03
(2025): 162-176.

5.  Hassan, Arooj, Muhammad Ahsan Khan, and Malik Arfat Hassan. "Product Management
Challenges in AI-Enhanced Fintech Fraud." International Journal of Business & Digital
Economy 1, no. 01 (2025): 14-28.

6.  Hassan,  Arooj,  Muhammad  Ahsan  Khan,  and  Malik  Arfat  Hassan.  "AI-Driven  Product
Roadmaps in Fintech, Optimizing User Experience and Security Trade-offs." International
Journal of Business & Digital Economy 1, no. 01 (2025): 1-13.

7.  Hassan,  Arooj,  Malik  Arfat  Hassan,  and  Muhammad  Ahsan  Khan.  "Threat  Intelligence
Automation in Fintech, A Product Management Perspective." Multiverse Journal 1, no. 2
(2024): 50-62.

8.  Hassan, Arooj, Muhammad Ahsan Khan, and Malik Arfat Hassan. "Impact of Regulatory
Compliance  PSD2,  GDPR  on  Fintech  Product  Design."  Frontiers  in  Multidisciplinary
Studies 1, no. 01 (2024): 59-72.

9.  Hassan, Arooj, Muhammad Ahsan Khan, and Malik Arfat Hassan. "Integrating Cyber Risk
Metrics into Fintech Product Lifecycle Management." Econova 1, no. 01 (2024): 42-53.
10. Hassan, Arooj, Malik Arfat Hassan, and Muhammad Ahsan Khan. "Evaluating Zero Trust
Security Models for Fintech Cloud  Infrastructures." Multiverse Journal 1, no. 1 (2024):
52-60.

11. Hassan,  Arooj,  Malik  Arfat  Hassan,  and  Muhammad  Ahsan  Khan.  "The  Role  of  Cloud
Compliance Automation  in  Scaling Fintech Products  Globally." Journal  of  Educational
Research in Developing Areas 4, no. 2 (2023): 245-255.

46 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

12. Hassan, Arooj, Malik Arfat Hassan, and Muhammad Ahsan Khan. "Multi-Cloud Strategies
for  Scalable  and  Secure  Fintech  Applications."  Journal  of  Educational  Research  in
Developing Areas 4, no. 1 (2023): 123-133.

13. Nabi, Hussain Abdul, Ali Abbas Hussain, Abdul Karim Sajid Ali, and Haroon Arif. "Data-
Driven  ERP  Solutions  Integrated  with  AI  for  Streamlined  Marketing  Operations  and
Resilient Supply Chain Networks." The Asian Bulletin of Big Data Management 5, no. 2
(2025): 115-128.

14. Arif,  Haroon,  Abdul  Karim  Sajid  Ali,  Aamir  Raza,  and  Aashesh  Kumar.  "Adversarial
Attacks  on  AI  Diagnostic  Tools:  Assessing  Risks  and  Developing  Mitigation
Strategies." Frontier in Medical and Health Research 3, no. 1 (2025): 317-332.

15. Arif, Haroon, Ali Abbas Hussain, Hussain Abdul Nabi, and Abdul Karim Sajid Ali. "AI
POWERED DETECTION OF ADVERSARIAL AND SUPPLY CHAIN ATTACKS ON
GENERATIVE MODELS."

16. Arif,  H.,  Ali,  A.  K.  S.,  &  Nabi,  H.  A.  (2025).  IoT  Security  through  ML/DL:  Software
Engineering Challenges and Directions. ICCK Journal of Software Engineering, 1(2), 90–
108. https://doi.org/10.62762/JSE.2025.372865

17. Arif,  Haroon,  Aashesh  Kumar,  Muhammad  Fahad,  and  Hafiz  Khawar  Hussain.  "Future
horizons: AI-enhanced threat detection in cloud environments: Unveiling opportunities for
research." International journal of multidisciplinary sciences and arts 3, no. 1 (2024): 242-
251.

INTRUSION  DETECTION  AND  DATA  PROTECTION

18. Ali,  Abdul  Karim  Sajid,  Aamir  Raza,  Haroon  Arif,  and  Ali  Abbas  Hussain.
"INTELLIGENT
IN
INFORMATION SECURITY USING ARTIFICIAL INTELLIGENCE AND MACHINE
LEARNING TECHNIQUES." Spectrum of Engineering Sciences 3, no. 4 (2025): 818-828.
19. Fahad, Muhammad, Aashesh Kumar, Haroon Arif, and Hafiz Khawar Hussain. "Mastering
apt  defense:  strategies, technologies, and  collaboration." BIN: Bulletin Of Informatics 1
(2023): 84-94.

20. Ghelani,  Harshitkumar.  "AI-Driven  Quality  Control  in  PCB  Manufacturing:  Enhancing
Production Efficiency and Precision." Valley International Journal Digital Library (2024):
1549-1564.

21. Ghelani,  Harshitkumar.  "Advanced  AI  Technologies  for  Defect  Prevention  and  Yield
Optimization  in  PCB  Manufacturing."  International  Journal  Of  Engineering  And
Computer Science 13, no. 10 (2024).

47 | P a g e

Unique Journal of Artificial Intelligence (UJAI)

          Vol 03 issue 06 (2025)

https://uniquespublisher.com/index.php/UJAI

22. Ghelani,  Harshitkumar.  "Six  Sigma  and  Continuous  Improvement  Strategies:  A
Comparative Analysis in Global Manufacturing Industries." Valley International Journal
Digital Library (2023): 954-972.

23. Ghelani, Harshitkumar. "Automated Defect Detection in Printed Circuit Boards: Exploring
the Impact of Convolutional Neural Networks on Quality Assurance and Environmental
Sustainability  in  Manufacturing."  International  Journal  of  Advanced  Engineering
Technologies and Innovations 1: 275-289.

24. Ghelani,  Harshitkumar.

"Harnessing  AI

Inspection:  Developing
Environmentally Friendly Frameworks for PCB Quality Control Using Energy-Efficient
Machine  Learning  Algorithms."  International  Journal  of  Advanced  Engineering
Technologies and Innovations 1: 146-154.

for  Visual

25. Ghelani, Harshitkumar. "Enhancing PCB Quality Control through AI-Driven Inspection:
Leveraging Convolutional Neural Networks for Automated Defect Detection in Electronic
Manufacturing Environments." Available at SSRN 5160737 (2024).

26. Ghelani,  Harshitkumar.  "Advances  in  lean  manufacturing:  improving  quality  and
efficiency  in  modern  production  systems."  Valley  International  Journal  Digital
Library (2021): 611-625.

27. Ghelani, Harshitkumar. "Revolutionizing Visual Inspection Frameworks: The Integration
of Machine Learning and Energy-Efficient Techniques in PCB Quality Control Systems
for Sustainable Production." International Journal of Advanced Engineering Technologies
and Innovations 1: 521-538.

48 | P a g e

