---
conversion_metadata:
  converted_at: "2026-07-21T07:59:40Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Owusu-Mensah et al.pdf"
  source_pdf_sha256: "29cf85be0ae0c1104e55a4cb982025fb091084209a2a8c78f6b6a4db09dc3ad7"
  page_count: 71
  markdown_char_count: 437325
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Discover Internet of Things
Article in Press

https://doi.org/10.1007/s43926-026-00358-y

Systematic review of the internet of things 
ecosystem for real-time detection of card-not-
present (CNP) fraud

Received: 4 August 2025

Accepted: 11 May 2026

Kwabena Owusu-Mensah, Edward Danso Ansong, Kofi Sarpong Adu-Manu & Winfred 
Yaokumah

Cite this article as: Owusu-Mensah K., 
Ansong E.D., Adu-Manu K.S. et al. 
Systematic review of the internet of 
things ecosystem for real-time detection 
of card-not-present (CNP) fraud. Discov 
Internet Things (2026). https://doi.
org/10.1007/s43926-026-00358-y

We are providing an unedited version of this manuscript to give early access to its 
findings. Before final publication, the manuscript will undergo further editing. Please 
note there may be errors present which affect the content, and all legal disclaimers 
apply.

If this paper is publishing under a Transparent Peer Review model then Peer

Review reports will publish with the final article.

© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International 
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit 
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do 
not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the 
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain 
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

---

<!-- PAGE 2 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Review

Systematic Review of the Internet of Things Ecosystem for Real-Time Detection of 
Card-Not-Present (CNP) Fraud

Kwabena  Owusu-Mensah1,  Edward  Danso  Ansong2,  Kofi  Sarpong  Adu-Manu3,  
Winfred Yaokumah4

1234Department of Computer Science, University of Ghana, Legon-Accra, Ghana 
Corresponding 
Author: 
mensah001@st.ug.edu.gh

Owusu-Mensah.

Kwabena

Email:

kowusu-

Abstract: 
The  rapid  rise  in  card-not-present  (CNP)  transactions  has  increased  fraud  risks  in 
digital commerce, highlighting the limitations of traditional fraud detection methods. 
The integration of Internet of Things (IoT) technologies introduces contextual data that 
can  enhance  real-time,  context-aware  fraud  detection.  However,  it  also  presents 
challenges  related  to  scalability,  latency,  privacy,  and  governance.  This  study 
systematically  reviews  IoT-enabled  frameworks  for  real-time  CNP  fraud  detection, 
synthesizing  evidence  from  23  peer-reviewed  articles  identified  through  a  literature 
search  covering  the  period  2015  to  April  3,  2026,  following  the  PRISMA  2020 
guidelines.  The  analysis  categorizes  existing  frameworks  based  on  application 
layers,  performance  evaluation,  and  distributed 
scenarios,  IoT  architectural 
intelligence, revealing system-level trends and identifying research gaps. While many 
studies  emphasize  predictive  effectiveness,  performance  reports  mainly  rely  on 
accuracy metrics, often overlooking essential factors such as real-time responsiveness 
and  privacy.  Notably,  federated  and  split  learning  are  highlighted  as  significant 
enablers  of  scalable,  privacy-preserving  collaboration,  although  their  coordination 
and  communication  trade-offs  are  often  not  quantified.  Moreover,  blockchain 
mechanisms  can  enhance  auditability  but  require  careful  integration  to  address 
potential latency issues. This study provides several key contributions: (i) it introduces 
a scenario-aware synthesis that links IoT architectural placement with fraud detection 
requirements  and  evaluation  practices;  (ii)  it  provides  explicit  guidance  for 
benchmarking 
latency, 
scalability/coordination cost, and privacy/trust indicators; and (iii) it presents a unified 
multi-layer  IoT-CNP  reference  architecture  that  aligns  with  the  CNP  transaction 
lifecycle.  Rather  than  proposing  a  new  detection  algorithm,  this  review  enhances

encompass

accuracy

beyond

goes

that

to

---

<!-- PAGE 3 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

system-level  integration  and  deployment  readiness  by  consolidating  fragmented 
evidence into a practical architecture and metrics blueprint for detecting real-time IoT-
enabled payment fraud.

Keywords: Card-not-present fraud; Internet of Things (IoT); real-time fraud detection; 
federated  learning;  privacy-preserving  analytics;  blockchain-enabled  governance; 
payment security, fraud analytics

1. Introduction

1.1 Background and Motivation

The rapid expansion of digital commerce and remote payment platforms has led to 
a substantial increase in card-not-present (CNP) transactions, making CNP fraud one of 
the most persistent and costly threats to contemporary financial systems. Unlike card-
present transactions, CNP payments lack physical authentication mechanisms, thereby 
increasing exposure to identity theft, account takeover, and transaction manipulation in 
online and mobile payment environments [1,2]. Conventional fraud detection systems, 
largely  centralized  and  batch-oriented,  are  increasingly  challenged  by  the  scale, 
velocity, and real-time decision requirements of modern digital payment ecosystems.

In  parallel,  the  Internet  of  Things  (IoT)  has  become  an  integral  component  of 
emerging  payment  infrastructures,  enabling  smart  point-of-sale  terminals,  mobile 
payment devices, connected consumer platforms, and machine-to-machine transactions 
[3].  IoT-enabled  environments  facilitate  continuous  data  acquisition  and  distributed 
analytics, enabling the detection of anomalous transaction patterns closer to the data 
source  and  with  reduced  latency  [4,5].  However,  these  environments  also  introduce 
significant  architectural  and  operational  challenges,  including  heterogeneous  data 
streams, resource-constrained edge devices, communication overhead, and heightened 
privacy  and  regulatory  concerns  [6].  To  ensure  optimal  effectiveness,  CNP  fraud 
detection  systems  must  carefully  balance  predictive  accuracy  with  key  operational 
considerations,  including  latency,  scalability,  deployability,  and  compliance  across 
multiple  layers  of  the  Internet  of  Things  (IoT).  This  necessitates  a  comprehensive, 
integrative  approach  that  addresses  the  complexities  of  contemporary  digital 
transactions while maintaining regulatory compliance and operational efficiency.

Recent research has explored machine learning and deep  learning approaches for 
credit card fraud detection using data collected from IoT-enabled systems, as well as 
federated  and  privacy-preserving  learning  paradigms  that  mitigate  the  risks  of 
centralized  data  sharing  [1,7,8].  At  the  same  time,  blockchain  technology  has 
increasingly  been  investigated  as  a  complementary  trust  layer  for  IoT-based  digital 
services,  offering  immutability,  decentralization,  and  auditable  transaction  records. 
Emerging studies demonstrate that blockchain’s effectiveness is further enhanced when 
combined  with  artificial  intelligence  techniques,  such  as  federated  learning  and 
explainable  AI,  to  support  privacy-preserving,  transparent,  and  regulation-aware 
analytics  in  distributed  financial  systems  [9,10].  Advances  in  blockchain  security, 
including  post-quantum  cryptography  and  secure  cloud-enabled  auditing,  further 
highlight  its  relevance  for  safeguarding  sensitive  transactional  data  against  evolving 
threat models [11].

---

<!-- PAGE 4 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Despite these advances, the existing literature remains fragmented. Studies on fraud 
detection, IoT security, blockchain-based trust mechanisms, and AI-driven analytics are 
often conducted in isolation, and existing surveys typically focus either on centralized 
fraud detection models or on generic IoT anomaly detection. As a result, there is a lack 
of  a  consolidated  understanding  of  how  to  jointly  orchestrate  IoT  architectures, 
blockchain-enabled  trust,  and  AI-driven  intelligence  to  support  real-time  CNP  fraud 
detection under practical deployment constraints. Moreover, performance assessment 
metrics, datasets, and application scenarios are reported inconsistently, limiting cross-
study comparability and real-world adoption.

This study addresses existing limitations by presenting a systematic review of IoT-
enabled  ecosystem-level  frameworks  for  real-time  CNP  fraud  detection.  Unlike 
previous  surveys,  this  work  explicitly  integrates  various  IoT  architectural  layers, 
including devices, communication networks, edge and fog computing, cloud analytics, 
and  governance  mechanisms,  with  fraud  detection  models,  performance  assessment 
metrics,  and  relevant  application  scenarios  for  digital  payment  systems.  The  review 
introduces a layered IoT taxonomy specifically designed for CNP fraud detection and 
synthesizes  comparative  evidence 
latency, 
scalability, and privacy preservation. It also identifies critical gaps between conceptual 
proposals  and  deployable  solutions.  Recent  advancements  in  blockchain-integrated 
federated learning, explainable AI, and post-quantum security further underscore the 
need for this ecosystem-level synthesis that accounts for decentralization, regulatory 
compliance, and real-time performance in CNP transaction environments [8,9,11].

regarding  detection  effectiveness,

Existing  reviews  on  payment  fraud  and  IoT  security  predominantly  focus  on 
algorithmic  detection  performance  or  general  IoT  anomaly/IDS  settings,  often 
neglecting  the  integration  of  (a)  IoT  layer  placement,  (b)  real-time  operational 
constraints  such  as  end-to-end  latency  and  throughput,  (c)  privacy-preserving 
collaboration  methods  such  as  federated  or  split  learning  and  their  associated 
coordination  costs,  and  (d)  governance  and  auditability  mechanisms,  including 
blockchain, within a unified deployment framework. In contrast, this systematic review, 
guided  by  the  PRISMA  methodology,  synthesises  IoT-enabled  real-time  CNP  fraud 
detection at the ecosystem level by integrating scenario taxonomy, multi-dimensional 
benchmarking requirements, and a layered IoT-CNP reference architecture aligned with 
the CNP transaction lifecycle.

For the purposes of this review, a framework was considered real-time or near real-
time  -oriented  if  it  was  designed  to  support  fraud  detection  within  transaction 
authorization windows, but it was considered empirically real-time-validated only when 
the  study  reported  operational  metrics  such  as  end-to-end  latency,  inference  time, 
throughput,  update  delay,  or  comparable  timing-based  evidence.  Also,  "Distributed 
intelligence"  signifies  analytics  and  learning  capabilities  spread  across  IoT  sensing, 
edge,  and  coordination  layers,  rather  than  being  restricted  to  a  single  centralised 
processing entity.

1.2 Limitations of Existing CNP Fraud-Related Surveys and the Perspective of This 
Review

Despite the growing body of literature on card-not-present (CNP) fraud detection, 
existing surveys reveal several systematic limitations. Most previous reviews tend to 
view  CNP  fraud  primarily  as  a  standalone  machine  learning  classification  problem,

---

<!-- PAGE 5 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

emphasising  algorithmic  accuracy,  precision-recall  metrics,  or  class  imbalance 
management. This focus often comes at the expense of real-time operational constraints 
such as end-to-end latency, deployment scalability, and system coordination overhead.  
Consequently,  critical  questions  regarding  the  performance  of  detection  models 
under  realistic  transaction  throughput,  diverse  infrastructure  conditions,  and  time-
sensitive  payment  authorisation  workflows 
insufficiently  explored. 
Additionally, many surveys assume that data sources and computations are implicitly 
importance  of  distributed  IoT-enabled 
centralised,  overlooking 
infrastructures, such as edge devices, contextual sensors, and real-time telemetry, which 
now  play  a  role  in  fraud  signal  generation  and  decision-making  in  modern  payment 
ecosystems.

the  growing

remain

Moreover, existing CNP fraud surveys rarely adopt governance-aware perspectives. 
While privacy, compliance, and trust are often acknowledged as high-level concerns, 
they are seldom analysed in relation to specific system mechanisms, such as privacy-
preserving  collaborative  learning,  auditability,  or  cross-organizational  coordination 
costs. Surveys focusing on federated learning, IoT security, or blockchain-based trust 
frameworks  typically  address  these  topics  in  isolation  and  outside  the  specific 
constraints of CNP payment lifecycles. Consequently, the literature lacks an integrated 
synthesis that connects detection models, architectural placement, evaluation metrics, 
and governance mechanisms within a single coherent deployment context.

This  review  addresses  these  gaps  by  synthesizing  evidence  across  IoT  sensing, 
edge/fog/cloud placement, distributed and privacy-preserving learning, and governance 
mechanisms within a scenario-aware IoT-CNP reference architecture aligned with the 
CNP  transaction  lifecycle.  Rather  than  evaluating  detection  models  in  isolation,  the 
review integrates architectural placement, benchmarking dimensions, and deployment 
constraints within a single ecosystem-level framework.

1.3 Conceptual Foundations of IoT-Based Frameworks in Fraud Detection

IoT-based  fraud  detection  frameworks  combine  pervasive  sensing,  distributed 
computation,  and  intelligent  decision-making  for  real-time  analysis  of  transactional 
data. Unlike traditional centralized systems, IoT approaches leverage multi-source data 
across devices and networks to capture richer contextual information for fraud detection 
[12,13].

Contextual  intelligence  for  fraud  detection  combines  transaction  features,  device 
fingerprints,  temporal  patterns,  and  network  signals.  This  data  fusion  enables  IoT 
systems to detect behavioral deviations indicating fraud, especially in CNP payments 
without physical verification [14].

Another foundational concept is layered intelligence across the IoT stack. IoT-based 
fraud detection frameworks are typically structured across multiple layers as shown in 
Fig.  1,  including  the  perception  layer  (data  acquisition),  network  layer  (data 
transmission),  processing  layer  (edge  or  cloud  analytics),  and  application  layer 
(decision support and response). This layered organization enables flexible deployment 
strategies,  allowing  detection  logic  to  be  distributed  across  edge,  fog,  and  cloud 
resources depending on latency, scalability, and resource constraints [15].

Fig. 1 IoT Ecosystem for Fraud Detection

---

<!-- PAGE 6 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Real-time  responsiveness  constitutes  a  further  conceptual  pillar.  In  CNP  fraud 
detection, decisions must be made within  milliseconds to avoid transaction delays or 
customer  disruption.  IoT-based  frameworks,  therefore,  emphasize  stream-based 
processing and online learning, enabling models to adapt dynamically to evolving fraud 
patterns  and  concept  drift.  This  contrasts with  traditional  batch-oriented  approaches, 
which struggle to maintain effectiveness under rapidly changing threat landscapes [13]. 
Privacy-preserving intelligence is vital in IoT ecosystems due to concerns about data 
ownership  and  user  trust.  Federated  and  split  learning  enable  collaborative  model 
training  without  centralizing  sensitive  data  [6,15].  Blockchain  technologies  provide 
immutable  ledgers  and  decentralized  trust  mechanisms  that  enhance  auditability  in 
fraud-detection workflows [3].

Resilience  and  adaptability  are  fundamental  to  IoT-based  fraud  detection 
frameworks.  As  fraudulent  behavior  evolves  in  response  to  defenses,  systems  must 
adapt  while  maintaining  stability.  IoT  architectures  enable  resilience  through  layer 
redundancy,  reconfigurable  detection 
to  maintain 
effectiveness.[14].

logic,  and  model  updates

Conceptual foundations like contextual intelligence, layered deployment, real-time 
responsiveness, privacy preservation, and adaptive resilience underpin IoT-based CNP 
fraud detection frameworks. These principles guide the development of unified multi-
layer frameworks for real-time fraud detection and prevention.

1.4 Objectives and Scope of the Study

This study provides a systematic synthesis of IoT-based frameworks related to real-
time CNP fraud detection, examining their performance, architectural trade-offs, and 
deployment feasibility. The study consolidates fragmented research into an analytical 
framework supporting evidence-based system design and evaluation.

Specifically, the study pursues the following objectives: 
1.  To synthesize existing IoT-based CNP fraud detection frameworks by organizing 
them according to representative application scenarios, IoT deployment layers,

---

<!-- PAGE 7 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

and  architectural  paradigms,  thereby  enabling  structured  comparison  across 
heterogeneous studies.

2.  To  identify  and  consolidate  key  performance  benchmarks  and  evaluation 
dimensions reported in the literature, such as detection effectiveness, real-time 
responsiveness,  scalability,  privacy  preservation,  and  governance,  while 
systematically exposing methodological inconsistencies and research gaps. 
3.  To examine the role of distributed and privacy-preserving intelligence, including 
federated learning, split learning, and blockchain-enabled trust mechanisms, in 
enhancing the scalability, trustworthiness, and regulatory alignment of IoT-based 
CNP fraud detection systems.

4.  To derive empirically grounded design principles that can guide the development 
of efficient, adaptive, and resilient IoT-driven fraud detection frameworks, based 
on observed trade-offs across application scenarios and performance dimensions. 
5.  To  motivate  and  conceptualize  a  unified  multi-layer  IoT-CNP  fraud  detection 
framework,  integrating  edge-level  responsiveness,  cloud-based  intelligence, 
distributed learning, and blockchain-supported governance, to support real-time 
fraud detection and prevention in complex financial ecosystems.

The  review  evaluates  various  architectural  frameworks,  centralized,  edge-based, 
federated,  and  blockchain-supported,  emphasizing  those  that  facilitate  real-time 
detection and prevention. Research on anomaly or intrusion detection applicable to CNP 
fraud detection was considered.

1.5 Research Contributions

This study contributes to the understanding of IoT-enabled card-not-present (CNP) 
fraud  detection  by  integrating  existing  research  areas,  including  credit  card  fraud 
analytics and IoT anomaly detection, into a cohesive framework. It focuses on real-time 
CNP fraud detection as a cross-layer issue in the IoT payment ecosystem. The main 
contribution  lies  in  offering  a  comprehensive  synthesis  that  aligns  architectural 
considerations with operational constraints and fraud detection requirements.

First,  the  study  provides  an  ecosystem-level  review  of  IoT-enabled  CNP  fraud 
detection. Instead of viewing fraud detection solely as a prediction task or IoT security 
only  through  anomaly  or  intrusion  detection,  the  review  explores  how  sensing  and 
contextual  data,  communication  infrastructure,  edge  and  fog  deployment,  cloud 
analytics,  distributed  learning,  and  governance  controls  collectively  influence  fraud 
detection  in  digital  payments.  This  approach  broadens  the  focus  from  model 
performance to the overall system factors that affect the operational viability of fraud 
detection frameworks.

Second, the study develops a layered IoT-CNP analytical taxonomy tailored to fraud 
detection  architectures.  By  organizing  the  evidence  across  sensing  and  devices, 
communication,  edge/fog,  cloud  analytics,  applications,  governance,  and  security 
layers,  the  review  clarifies  where  detection  logic  is  placed,  how  intelligence  is 
distributed,  and  the  trade-offs  across  the  architecture.  This  layered  framing  makes 
visible several issues that are often treated only implicitly in the literature, particularly 
the  relationships  among  deployment  location,  response  time,  privacy  exposure, 
scalability, resilience, and compliance requirements.

Third, the review provides a scenario-aware comparative synthesis of the included 
studies. Rather than viewing the literature as isolated papers, it compares frameworks

---

<!-- PAGE 8 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

based on application scenario, architectural placement, learning paradigm, data context, 
and evaluation practices. This approach reveals which methods are used, where they are 
deployed,  the  assumptions  behind  their  evaluation,  and  the  performance  metrics 
measured.  It  also  highlights  ongoing  methodological  inconsistencies  in  the  field, 
including the use of diverse datasets, inconsistent reporting of latency and throughput, 
overemphasis on accuracy metrics, and a limited focus on privacy and governance.

Fourth,  the  study  makes  an  application-oriented  contribution  by  mapping  the 
reviewed frameworks to representative CNP payment contexts, including e-commerce 
transaction  screening,  edge-assisted  mobile  and  IoT  payments,  distributed  fraud 
monitoring,  and  blockchain-supported  auditing  and  settlement.  This  improves  the 
practical  relevance  of  the  review  by  distinguishing  frameworks  that  appear 
operationally plausible from those that remain largely conceptual. It also helps align the 
literature  with  the  real  constraints  of  payment  environments,  where  detection 
effectiveness  must  be  balanced  against  speed,  trust,  interoperability,  and  regulatory 
accountability.

Fifth,

the  review  consolidates  evidence  on  distributed,  privacy-preserving 
intelligence  for  IoT-enabled  fraud  detection.  It  examines  federated  learning,  split 
that  support  collaboration, 
learning,  and  blockchain-based 
auditability, and privacy in financial ecosystems. Rather than viewing these as separate, 
it positions them within broader fraud-detection workflows, highlighting trade-offs such 
as communication overhead, coordination complexity, interpretability limitations, and 
latency.

trust  mechanisms

inconsistent  reporting  of  operational  metrics,

Sixth,  the  study  identifies  empirical,  architectural,  and  deployment  gaps  that 
continue  to  constrain  the  field.  These  include  limited  validation  under  real-world 
conditions, 
limited  cross-study 
comparability,  insufficient  handling  of  heterogeneous  IoT  data,  and  fragmented 
treatment  of  privacy,  governance,  and  standardization  issues.  By  making  these  gaps 
explicit, the review provides a clearer agenda for advancing IoT-enabled fraud detection 
research  from  promising  conceptual  prototypes  to  more  rigorous,  deployable 
operational systems.

The  manuscript  concludes  with  a  unified  multi-layer  IoT-CNP  fraud  detection 
framework  aligned  with  the  CNP  transaction  lifecycle.  Instead  of  proposing  a  new 
detection algorithm, it integrates existing evidence into an architectural blueprint that 
connects contextual sensing, edge responsiveness, cloud intelligence, collaboration, and 
governance.  This  framework  aims  to  aid  future  benchmarking,  design,  and 
implementation  by  balancing  detection  performance  with  real-time  responsiveness, 
privacy, scalability, trust, and compliance.

Table 1 situates this review within the broader literature. While past reviews often 
focus  on  specific  areas  like  credit  card  fraud  detection  or  IoT  security,  they  rarely 
connect  these  elements  to  real-time  CNP  payment  systems.  Moreover,  they  often 
overlook  crucial  factors  such  as  cross-layer  architecture  and  governance  needs.  In 
contrast,  this  review  adopts  an  ecosystem-level  perspective,  incorporating  scenario-
aware  IoT  deployment  and  a  layered  IoT-CNP  reference  architecture,  thereby 
addressing a significant gap in the literature.

Table 1: Positioning of this Review relative to prior surveys

---

<!-- PAGE 9 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Review Type  Typical Focus

Credit card / 
CNP fraud 
surveys

Algorithm/model 
performance; 
accuracy/F1

IoT security / 
IDS surveys

Network 
intrusion/anomaly 
detection

Federated 
learning 
surveys 
(general) 
Blockchain-
in-IoT 
surveys

FL methods, 
aggregation, 
privacy

Auditability, 
integrity, and 
ledger designs

is  usually

What 
missing 
IoT-layer 
placement; end-to-
end latency; edge 
deployment; 
governance 
CNP payment 
lifecycle; payment 
governance; 
PCI/compliance 
framing 
CNP operational 
constraints; IoT 
heterogeneity tied 
to payment flow 
Latency impact on 
real-time 
decisioning; 
coupling with 
detection pipelines

What this paper adds

Scenario-aware, IoT-
layered synthesis and 
real-time benchmarking 
dimensions

CNP-centric lifecycle 
mapping and payment-
context requirements.

FL/SL role in CNP 
detection with explicit 
coordination/latency 
trade-offs 
Governance integration 
without compromising 
latency, supported by 
layered architecture 
guidance.

1.6 Paper Organization 
The remainder of this paper is organized as follows:

  Section 2 describes the research methodology, including the systematic review 
protocol,  search  strategy,  inclusion  and  exclusion  criteria,  quality  assessment, 
and analytical framework.

  Section 3 presents an overview of the selected studies and summarizes their core

characteristics.

  Section 4 provides the main analytical synthesis, covering reviewed frameworks 
and  analytical  structure,  application  scenarios  and  case-study  contexts, 
performance  evaluation  practices,  distributed  and  privacy-preserving  learning 
models,  design  principles  for  resilient  IoT-driven  fraud  detection,  and  the 
formulation of a unified multi-layer framework.

  Section 5 discusses the implications of the findings by mirroring the analytical 
structure of Section 4, relating results to the research questions and broader IoT 
and financial security contexts.

  Finally,  Section  6  concludes  the  paper  by  summarizing  key  contributions  and

outlining directions for future research.

2. Methodology

2.1 Overview and Research Design

This  study  employs  a  systematic  review  research  design  guided  by  the  PRISMA 
(Preferred  Reporting  Items  for  Systematic  Reviews  and  Meta-Analyses)  2020 
framework [16] to ensure methodological rigor, transparency, and reproducibility. The 
review is explicitly aligned with the study’s objectives and is structured to synthesize

---

<!-- PAGE 10 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

existing IoT-based frameworks for real-time CNP fraud detection, using a combination 
of qualitative thematic analysis and comparative performance assessment.

Rather than restricting the analysis to algorithmic performance alone, the research 
design  emphasizes  architectural,  operational,  and  governance  dimensions,  thereby 
reflecting the ecosystem-level nature of IoT-enabled fraud detection systems. To this 
end,  the  methodological  workflow  incorporates  both  descriptive  and  interpretive 
synthesis  techniques,  facilitating  the  identification  of  technical  trends,  performance 
benchmarks, and research gaps across diverse deployment contexts.

The review process consists of six interrelated stages: 
1.  Conceptual  framing  and  objective  alignment,  in  which  research  gaps  are 
identified from preliminary scoping and mapped explicitly to the study’s research 
questions and objectives.

2.  Systematic  literature  search  and  screening,  conducted  in  accordance  with 
PRISMA 2020 guidelines [16] and informed by the PICO model [17] to ensure 
comprehensive yet targeted retrieval of relevant studies.

3.  Eligibility  assessment  and  methodological  quality  evaluation,  using  a 
standardized checklist to assess the robustness, relevance, and reproducibility of 
included studies.

4.  Structured  data  extraction  and  thematic  coding,  aligned  with  the  research 
questions  to  capture  application  scenarios,  architectural  patterns,  learning 
paradigms, and evaluation practices.

5.  Comparative  synthesis  and  performance  benchmarking,  through  consolidation 
and cross-scenario analysis of reported metrics related to detection effectiveness, 
real-time performance, scalability, privacy, and governance.

6.  Cross-layer  and  cross-technology  synthesis,  integrating  findings  across  IoT 
layers and intelligent paradigms to inform the formulation of a unified multi-layer 
IoT-CNP fraud detection framework.

2.2 Research Questions

The  review  is  anchored  by  a  series  of  research  questions  (RQs)  that  serve  as 
methodological  pillars,  guiding  the  processes  of  literature  selection,  data  extraction, 
analysis, and synthesis. These research questions are intricately linked to the study’s 
objectives, analytical focus, and anticipated outcomes, ensuring coherence, traceability, 
and methodological rigor throughout the review process. Table 2 outlines each research 
objective, the corresponding research question, the analytical focus, and the expected 
outcomes. It provides a clear framework that explains the review's rationale, highlights 
the elements examined, and summarizes the methodologies used to present the findings.

Table 2: Research Objectives, Questions, Analytical Focus, and Expected Outputs

Objective

Objective 1: To 
conduct a quantitative 
and qualitative 
synthesis of existing 
IoT-based fraud-

Research 
Question (RQ) 
RQ1: How can 
existing IoT-based 
frameworks be 
synthesized to 
identify key

Analytical 
Focus 
Comparative 
synthesis of 
frameworks; 
analysis of 
accuracy,

Expected Output / 
Deliverable 
Performance matrix 
and synthesis table 
highlighting 
benchmark 
indicators and

---

<!-- PAGE 11 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Objective

detection frameworks 
to identify benchmarks, 
interoperability 
patterns, and gaps.

Objective 2: To 
evaluate distributed 
and privacy-preserving 
intelligence, such as 
federated learning, 
blockchain, and edge 
analytics, for 
scalability and trust.

Objective 3: To 
provide strategic 
design guidelines for 
IoT-driven fraud 
detection emphasizing 
efficiency, adaptability, 
and resilience.

Objective 4: To 
develop a unified IoT-
CNP fraud 
convergence 
framework integrating 
multiple IoT layers for 
real-time detection.

Research 
Question (RQ) 
performance 
benchmarks and 
research gaps in 
CNP fraud 
detection? 
RQ2: How can 
distributed and 
privacy-preserving 
intelligence 
enhance the 
scalability and 
trustworthiness of 
IoT-based CNP 
fraud detection 
systems? 
RQ3: What design 
principles can 
guide efficient, 
adaptive, and 
resilient IoT-
driven fraud-
detection 
frameworks?

RQ4: How can a 
unified multi-layer 
IoT-CNP 
framework be 
developed to 
enhance real-time 
fraud detection 
and prevention?

Analytical 
Focus 
latency, 
scalability, and 
privacy trade-
offs.

Expected Output / 
Deliverable 
interoperability 
gaps.

Evaluation of 
federated, 
blockchain, 
and edge-based 
models for 
explainability 
and resilience.

Thematic synthesis 
of distributed 
intelligence models 
and their 
contributions to 
scalable, privacy-
aware detection.

Comparative 
design 
analysis; 
identification 
of 
communication 
and learning 
optimization 
mechanisms. 
Integration of 
findings into a 
layered IoT 
taxonomy and 
convergence 
model.

Guideline 
framework 
summarizing best 
practices for 
efficiency, 
adaptability, and 
resilience.

A six-layer IoT-
CNP fraud 
convergence 
framework for 
scalable, 
explainable, 
privacy-compliant 
systems and real-
time detection.

2.3 Search and Study Selection Process

Identification of Studies

The identification stage involved a systematic search of major academic databases. 
Six  databases  were  selected  due  to  their  strong  coverage  of  computer  science, 
cybersecurity,  financial  technology,  and  digital  payment  research.  These  databases 
collectively  provide  broad  coverage  of  both  engineering-oriented  research  and 
interdisciplinary studies related to fraud detection and digital financial systems.

The databases included:

---

<!-- PAGE 12 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT



IEEE Xplore, which provides extensive coverage of engineering, cybersecurity, 
and Internet of Things research.

  ScienceDirect (Elsevier), a major repository of peer-reviewed journals covering

computer science, artificial intelligence, and financial technology.

  SpringerLink,  which  hosts  numerous  publications  on  cybersecurity,  machine

learning, and digital financial systems.

  Wiley Online Library, known for interdisciplinary research spanning information

systems, finance, and emerging technologies.

  MDPI, which publishes open-access journals such as Sensors, Electronics, and

Future Internet that frequently feature IoT-based fraud detection studies.

  Google Scholar, which was included to capture additional relevant studies not

indexed in the above databases and to ensure comprehensive coverage.

These  databases  were  selected  to  ensure  balanced  coverage  across  cybersecurity,

emerging technologies, IoT systems, and financial technology research domains.

The  literature  search  covered  publications  between  2015  and  April  3,  2026, 
reflecting the period during which IoT-based financial security systems and emerging 
technology approaches for fraud detection evolved substantially.

Search Strategy 
The  literature  search  was  conducted  using  the  PICO  model  [17]  to  ensure  a 
structured, systematic, and reproducible retrieval of studies relevant to IoT-based CNP 
fraud detection. The resulting PICO elements, associated keywords, and search terms 
are summarized in Table 3, enabling targeted identification of relevant studies.

Within  the  PICO  framework,  the  Population  corresponds  to  IoT-enabled  digital 
payment  and  transaction  environments;  the  Intervention  includes  IoT-based  fraud 
detection, prevention, and mitigation mechanisms; the Comparison spans centralized, 
edge-based, distributed, and privacy-preserving architecture; and the Outcome focuses 
on  real-time  or  near-real-time  fraud  detection  performance,  online  transaction 
monitoring, scalability, privacy preservation, and system trustworthiness.

Table 4 presents the database search strategy used to identify relevant studies for the 
review.  The  table  lists  the  scholarly  databases  searched,  the  exact  Boolean  search 
queries applied in each database, and the filters used to refine the results. The search 
queries  were  designed  to  capture  literature  related  to  Internet  of  Things  (IoT) 
technologies, fraud detection mechanisms, machine learning techniques, and financial 
transaction security. Because each database has different indexing structures and search 
capabilities, the queries were slightly adapted to suit the syntax and filtering options of 
each platform. The applied filters ensured that the retrieved records were relevant peer-
reviewed studies within fields such as computer science, cybersecurity, and financial 
technology,  thereby  supporting  a  systematic,  transparent,  and  reproducible  literature 
search process.

Table 3: PICO Model Mapping and Search Alignment

PICO 
Element 
Population  
(P)

Definition / Focus  Keywords and Synonyms 
Used 
“Internet of Things,” “IoT,” 
“edge device,” “smart sensor,”

IoT-based financial 
transaction and

Purpose / Link to 
RQs 
Defines the IoT 
ecosystem context 
for CNP fraud

---

<!-- PAGE 13 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

PICO 
Element

Intervention 
(I)

Comparison 
(C)

Outcome  
(O)

fraud-detection 
environments 
Real-time, 
distributed, and 
privacy-preserving 
fraud-detection 
frameworks

Definition / Focus  Keywords and Synonyms 
Used 
“connected device,” “smart 
payment infrastructure.” 
“real-time detection,” “fraud 
mitigation,” “federated 
learning,” “blockchain,” “edge 
AI,” “fog computing,” 
”Distributed Learning,’ “deep 
learning,” “anomaly detection” 
“rule-based detection,” 
“centralized framework,” 
“static models,” “batch 
processing” 
“accuracy,” “latency,” 
“precision,” “recall,” 
“scalability,” “communication 
efficiency,” “privacy 
overhead”

Traditional 
centralized or static 
fraud-detection 
systems 
Enhanced detection 
accuracy, 
scalability, privacy, 
and interoperability

Purpose / Link to 
RQs 
detection (RQ1-
RQ4). 
Identifies 
technological 
interventions and 
architectures 
studied (RQ1-
RQ3). 
Provides a baseline 
for comparing IoT-
enabled adaptive 
systems (RQ1). 
Defines 
measurable 
outcomes for 
synthesis and 
benchmarking 
(RQ1-RQ4).

Table 4: Database Search Strategy for Literature Retrieval

Database

Exact Search Query

Filters Applied

(("Fraud  Detection"  AND  IoT  AND  "Financial 
Transactions") OR ("IoT Device Security" AND 
"Smart  Card  Fraud"  AND  "Credit  Cards")  OR 
(Blockchain AND IoT AND "E-Commerce") OR 
("Privacy-Preserving  Anomaly  Detection"  AND 
IoT  AND  ("Federated  Learning"  OR  "Split 
Learning"))  OR  ("Federated  Learning"  AND 
"Intrusion  Detection"  AND  IoT)  OR  ("Deep 
Learning" AND "Real-Time Anomaly Detection" 
AND IoT)) 
(("IoT"  AND  "Financial  Fraud  Detection"  AND 
Intelligence"  OR  Survey  OR 
("Artificial 
Implementation))  OR 
IoT-Based 
("Secure 
Payments" AND "PCI DSS" AND "Payment Card 
Standard")  OR 
Security 
Industry  Data 
("Distributed  framework"  AND  "DDoS  attacks" 
AND  Blockchain  AND  IoT  AND  "Smart 
Contracts" AND "Fog Computing")) 
("Internet of Things" OR IoT OR "smart device" 
OR "connected device" OR "edge device") AND 
("fraud  detection"  OR  "fraud  prevention"  OR 
("card-not-present 
"fraud  mitigation")  AND

IEEE Xplore

Wiley Online 
Library

SpringerLink

Internet of Things 
Conferences 
Journals

Journals

Research Article 
Computational 
Intelligence 
Machine learning

---

<!-- PAGE 14 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Database

Exact Search Query

fraud"  OR  "card  not  present  fraud"  OR  "card 
fraud" OR "payment fraud" OR "online payment 
fraud") AND ("real-time" OR "near real-time" OR 
"real time")

ScienceDirect 
(Elsevier)

("fraud detection"  OR "credit card fraud") AND 
("Internet  of  Things"  OR  IoT)  AND  ("machine 
learning"  OR  "deep  learning")  AND  ("financial 
transaction" OR payment)

MDPI

Google 
Scholar

("Internet  of  Things"  OR  IoT)  AND  ("anomaly 
detection"  OR  "intrusion  detection"  OR  "fraud 
detection")  AND  ("machine  learning"  OR  "deep 
learning" OR "federated learning" OR "security" 
OR "privacy") 
("Internet  of  Things"  OR  IoT*)  AND  ("fraud 
detection"  OR  "card  fraud"  OR  card-not-present 
"intrusion 
fraud 
detection")  AND  ("machine  learning"  OR  "deep 
learning"  OR 
learning"  OR 
"federated 
Blockchain)

"anomaly  detection"  OR

Filters Applied 
Data and 
information 
security 
Federated 
Learning for 
privacy-
preserving and 
data analysis

Research Articles 
Computer 
Science  
Engineering  
Decision Science

Journals = 
sensors, 
information, IoT

Selection of Studies (Eligibility)

The  full  texts  of  the  remaining  articles  were  then  evaluated  against  predefined

inclusion and exclusion criteria.

Inclusion Criteria

Studies were included based on the following criteria: 
  They address card-not-present or online payment fraud detection within an

IoT ecosystem.

  They explicitly focus on IoT-based fraud detection, prevention, or mitigation

in online or CNP-based transaction environments.

  They  propose  frameworks  for  real-time  or  near-real-time  fraud  detection, 
substantiated  by  operational  evidence  (e.g.,  latency,  throughput)  or  design 
characteristics suitable for time-sensitive monitoring. Architectural suitability 
alone does not suffice.

  They  demonstrate  or  assert  real-time  fraud  detection  capabilities  in  online

monitoring, reflecting this through design or performance evaluation.

  They  employ  advanced  techniques  such  as  machine  learning,  federated

learning, distributed learning, or blockchain governance mechanisms. 
  They provide experimental validation or conduct a system evaluation.

---

<!-- PAGE 15 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Exclusion Criteria

Studies were excluded if they: 
  Focused exclusively on card-present fraud detection 
  Did not involve IoT or distributed computing technologies 
  Lacked sufficient methodological detail 
  Were non-peer-reviewed or non-English publications.

This review’s inclusion criteria were designed to identify studies that contribute to 
the technological ecosystem for CNP fraud detection in IoT environments. While the 
review is anchored in digital payment fraud detection, effective real-time detection in 
IoT  settings  depends  on  enabling  components,  including  data  collection,  network 
communication,  anomaly  detection,  distributed  learning,  edge  analytics,  blockchain, 
and IoT security controls. Accordingly, the review intentionally adopts an ecosystem 
perspective rather than a purely algorithmic one, retaining studies not only when they 
directly  address  card-not-present  fraud  but  also  when  they  contribute  cross-layer 
mechanisms essential to real-time CNP fraud detection.

Screening and Eligibility Assessment

The database search identified 1,129 records, which were narrowed to 303 articles 
through an initial relevance-filtering process. After duplicate removal using Zotero, 67 
unique  studies  remained.  Titles  and  abstracts  were  then  screened  against  predefined 
inclusion and exclusion criteria, resulting in the exclusion of 17 studies and leaving 50 
articles for full-text review.

At  the  second  stage,  full-text  articles  were  evaluated  for  methodological  rigor, 
evidence of IoT implementation, relevance to fraud detection, applicability to real-time 
or  near-real-time  contexts,  and  the  reporting  of  evaluation  metrics.  This  assessment 
resulted in the exclusion of 27 additional studies because they lacked methodological 
transparency, did not demonstrate explicit fraud-detection capability, focused on non-
IoT  settings,  or  failed  to  provide  evidence  relevant  to  distributed,  real-time,  or  IoT-
enabled payment security. As a result, 23 studies were included in the final synthesis.

Although the final corpus includes only 23 studies from 2015 to April 2026, this 
reflects  the  review’s  narrow  scope  and  the  strict  application  of  PRISMA-based 
eligibility criteria. The review was not designed to include all studies on credit card 
fraud, IoT anomaly detection, blockchain security, or federated learning independently. 
Instead, it retained only studies that contributed directly or mechanistically to real-time 
or  near-real-time  card-not-present  (CNP)  fraud  detection  in  IoT-enabled  payment 
environments. Thus, the final corpus serves as a focused, quality-controlled evidence 
base for ecosystem-level synthesis rather than a broad mapping of related literature.

The study selection process is presented in the PRISMA flow diagram (Fig. 2), and 
Fig. 3 shows the distribution of included studies across scholarly databases, highlighting 
each source’s contribution to the final corpus.

Fig. 2 The screening process

---

<!-- PAGE 16 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Fig. 3 Number of selected papers per database

10

6

3

2

1

1

Google
Scholar

IEEE

Wiley

MDPI

Springer ScienceDirect

2.4 Quality Assessment

To evaluate the methodological rigor of the selected studies, a quality assessment 
process  was  conducted  using  five  evaluation  criteria  shown  in  Table  5,  covering 
research  clarity,  methodological 
transparency,  dataset  adequacy,  performance 
evaluation, and relevance to IoT-enabled fraud detection.

Table 5: Quality Assessment Criteria

Code  Criterion 
QA1 
QA2 
QA3 
QA4

Clear research objective 
Adequate methodology description 
Use of an appropriate dataset or evaluation environment 
Performance evaluation using relevant metrics

---

<!-- PAGE 17 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Code  Criterion 
QA5

Relevance to IoT-enabled fraud detection

Each criterion was scored using a three-point scale: 1 (Yes), 0.5 (Partially), and 0

(No). The maximum possible score for each study was five.

The  results  summarized  in  Table  6  indicate  that  most  studies  demonstrate  strong 
methodological  rigor,  particularly  those  focusing  on  machine  learning-based  fraud 
detection  using  publicly  available  financial  transaction  datasets.  However,  several 
studies  focusing  on  conceptual  frameworks  or  surveys  scored  lower  in  dataset 
evaluation and empirical validation.

Overall, the quality assessment confirms that most of the included studies provide 
reliable empirical insights into fraud detection techniques relevant to CNP fraud in IoT-
enabled payment ecosystems.

Table 6: Quality Assessment Results

Study 
A1 
A2 
A3 
A4 
A5 
A6 
A7 
A8 
A9 
A10 
A11 
A12 
A13 
A14 
A15 
A16 
A17 
A18 
A19 
A20 
A21 
A22 
A23

QA1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1

QA2 
1 
0.5 
1 
0.5 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1 
1

QA3 
1 
0 
0.5 
0.5 
1 
1 
1 
1 
0.5 
0.5 
1 
1 
1 
0.5 
0.5 
0 
1 
1 
1 
1 
1 
1 
1

QA4 
1 
0 
0.5 
0.5 
1 
0.5 
0.5 
0.5 
0.5 
0.5 
1 
1 
1 
0.5 
1 
0 
1 
1 
1 
1 
1 
1 
1

QA5 
1 
1 
1 
0.5 
0.5 
0.5 
0.5 
0.5 
1 
0.5 
0.5 
0.5 
0.5 
0.5 
0.5 
0.5 
0.5 
0.5 
0.5 
0.5 
0.5 
0.5 
0.5

Score 
5 
2.5 
4 
3 
4.5 
4 
4 
4 
4 
3.5 
4.5 
4.5 
4.5 
3.5 
4 
2.5 
4.5 
4.5 
4.5 
4.5 
4.5 
4.5 
4.5

Table 7 presents all included studies, with articles coded from Article 1 (A1) to Article 
(A23) to support traceability and cross-referencing throughout the analysis.

---

<!-- PAGE 18 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Table 7: Summary of the 23 selected studies included in the review

Code

Author(s) & 
Year

Title / Framework

A1

Alatawi, 2025 
[1]

A2

Bhutta et al., 
2022 [2]

A3

Liu et al., 2019 
[3]

A4

Gupta & 
Kumar, 2024 
[4]

A5

Yasaei et al., 
2024 [5]

A6

Deshmukh et 
al., 2025 [6]

A7

Rguibi et al., 
2024 [7]

A8

Zhang et al., 
2024 [8]

A9

Devi et al., 
2023 [18]

Detection of Fraud in 
IoT-Based Credit Card 
Dataset Using Machine 
Learning

Towards Secure IoT-
Based Payments by 
Extending PCI DSS

NormaChain: A 
Blockchain-Based 
Normalized Autonomous 
Transaction Settlement 
System 
Integrating Deep 
Learning, Machine 
Learning, AI, IoT, and 
Data Science for Future 
Innovations 
IoT-GRAF: IoT Graph 
Learning-Based 
Anomaly and Intrusion 
Detection 
Enhancing Privacy in 
IoT-Enabled Digital 
Infrastructure: 
Evaluating Federated 
Learning 
Privacy-Preserving 
Anomaly Detection for 
IoT Using Federated and 
Split Learning 
Privacy-Aware Anomaly 
Detection in IoT 
Environments Using 
FedGroup 
IoT Device Security for 
Smart Card Fraud 
Detection for Credit 
Cards

Primary 
Approach / 
Technique

Key Focus Area

Ensemble 
Learning (RF, 
DNN, SVM)

ML-driven fraud 
detection in IoT 
ecosystems

Security 
Compliance, IoT 
Payment 
Architecture

Secure IoT 
payment 
compliance 
framework

Blockchain, 
Smart Contracts, 
Searchable 
Encryption

Blockchain 
auditability and 
autonomous IoT e-
commerce

Deep Learning, 
Predictive 
Analytics

AI-IoT integration 
for predictive 
decision systems

Graph Neural 
Networks 
(GNNs), Multi-
Modal Fusion

Graph-based fusion 
for anomaly and 
intrusion detection

Federated 
Learning, Privacy 
Preservation

Secure 
collaborative 
learning and 
anomaly detection

Split Learning, 
Federated 
Learning

Group-Based 
Federated 
Learning 
(FedGroup)

Collaborative 
model training 
under privacy 
constraints

Privacy-preserving 
collaborative 
anomaly detection

NFC, Random 
Forest, Bayesian 
Network

NFC-based IoT 
security and 
transaction 
verification

---

<!-- PAGE 19 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Code

Author(s) & 
Year

Title / Framework

Primary 
Approach / 
Technique

A10

Kumar et al., 
2021 [19]

A11

Garg et al., 
2024 [20]

A12

Benameur et al., 
2024 [21]

A13

Rehman et al., 
2025 [22]

A14

Vankayalapati 
et al., 2025 [23]

A15

Prakash et al., 
2024 [24]

A16

Goyal et al., 
2024 [25]

A Distributed 
Framework for Detecting 
DDoS Attacks in Smart 
Contract-Based 
Blockchain-IoT Systems 
A Multi-Layered AI-IoT 
Framework for Adaptive 
Financial Services 
A Novel Federated 
Learning-Based 
Intrusion Detection 
System for IoT Networks 
A Hybrid Fuzzy Logic 
and Federated Learning 
Framework for IoT-
Enabled Metaverse 
Transactions 
A Robust and Scalable 
Deep Learning 
Framework for Real-
Time IoT Intrusion 
Detection 
A Secure Framework for 
IoT Anomalies Using 
Machine Learning 
Advanced Deep 
Learning Approaches for 
Real-Time Anomaly 
Detection in IoT 
Environments

Blockchain, Fog 
Computing, 
Distributed 
Detection

Deep Learning, 
Multi-Agent IoT

Federated 
Learning 
(FedAvg)

Fuzzy Logic, 
Federated 
Learning

CNN-LSTM 
Hybrid, 
Adversarial 
Resilience

Random Forest, 
SVM, Ensemble 
Learning

Deep Neural 
Networks, 
Ensemble Models

A17

Choi & Lee, 
2018 [26]

An Artificial Intelligence 
Approach to Financial 
Fraud Detection under 
IoT Environment

AI Rule-Based 
Systems, Neural 
Networks

Key Focus Area

DDoS detection 
and fog-level fraud 
mitigation

Adaptive financial 
intelligence and 
anomaly detection 
Distributed 
intrusion detection 
and collaborative 
learning

Cybersecurity and 
anomaly detection 
in virtual IoT 
systems

Deep learning 
resilience and 
energy efficiency

IoT anomaly 
detection and 
network protection

Multi-class 
anomaly detection 
for IoT data 
streams

Financial 
transaction fraud 
detection and 
behavioral 
profiling

A18

Subhalaxmi et 
al., 2023 [27]

A19

Min et al., 2021 
[28]

Credit Card Fraud 
Detection Using Multi-
Layer Perceptron Based 
on Federated Learning 
Detecting Anomalous 
Transactions via an IoT-
Based Application

Federated Neural 
Networks

Collaborative fraud 
detection across 
distributed nodes

Decision Trees, 
Gradient 
Boosting

Transaction-level 
anomaly detection

---

<!-- PAGE 20 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Code

Author(s) & 
Year

Title / Framework

A20

Abubakar et al., 
2024 [29]

A21

Murthy et al., 
2024 [30]

A22

Kafila et al., 
2024 [31]

A23

Maddukuri, 
2022 [32]

Digital Twin and IoT-
Enabled Online Learning 
Model for Real-Time 
Fraud Monitoring 
Edge AI in IoT: 
Leveraging Cloud 
Computing and Big Data 
for Intelligent Decision-
Making 
Fraud Detection in IoT-
Based Financial 
Transactions Using 
Anomaly Detection 
Techniques 
Real-Time Fraud 
Detection Using IoT and 
AI: Securing the Digital 
Wallet

Primary 
Approach / 
Technique

Key Focus Area

Digital Twin, 
Edge Computing

Real-time 
monitoring and 
predictive learning

Edge AI, Cloud–
Fog Integration

Cloud-edge 
synergy for 
financial analytics

Isolation Forest, 
Autoencoder

Unsupervised 
anomaly detection 
in financial IoT 
systems

AI-Driven Fraud 
Detection, IoT 
Sensors

Real-time fraud 
protection for 
digital wallets

As illustrated in Fig. 4, the reviewed studies span the principal layers of the IoT-enabled 
fraud detection framework, enabling an ecosystem-level understanding of how sensing, 
communication, analytics, and governance interact in real-time payment surveillance.

Fig. 4 Mapping of studies to different layers of the IoT-enabled fraud detection 
ecosystem.

---

<!-- PAGE 21 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Potential Sources of Bias in the Included Studies

Several sources of bias were identified across the included studies. Many relied on 
simulated,  curated,  or  domain-specific  datasets  that  may  not  fully  capture  the 
complexity, imbalance, and temporal evolution of real-world CNP  fraud. Evaluation 
bias  was  also  evident,  as  performance  was  often  reported  primarily  using  accuracy-
oriented metrics, with limited consideration of false positives, latency, throughput, and 
deployment realism. Furthermore, some studies originated in adjacent IoT anomaly or 
intrusion-detection domains, which may limit the direct transferability of their findings 
to  CNP  fraud  detection.  Accordingly,  the  final  evidence  base  should  be  viewed  as 
scope-driven  and  quality-filtered,  with  emphasis  placed  on  recurring  architectural 
patterns and methodological trends rather than headline performance figures.

2.5 Data Extraction and Coding

A  structured  data  extraction  and  coding  protocol  was  implemented  to  ensure 
consistent  analysis  across  all  included  studies.  Table  8  summarizes  the  extraction 
schema,  outlining  the  categories,  variables,  and  their  analytical  roles.  Each  category 
serves  a  specific  purpose,  such  as  framework  characterization,  IoT  layer  mapping, 
learning  paradigm  identification,  performance  evaluation,  and  privacy  assessment, 
thereby  enhancing  comparability  across  diverse  studies.  By  aligning  each  extraction 
category with an analytical role, the protocol ensured comprehensive coverage of all 
research questions (RQ1-RQ4). These elements contributed to the thematic synthesis 
and to the development of a unified convergence framework that addresses all research 
questions.  This  extraction  protocol  also  underpins 
the  study’s  comparative 
benchmarking logic by ensuring that predictive effectiveness, real-time responsiveness, 
scalability/resource  efficiency,  privacy/trust indicators,  and  implementation  evidence 
were  captured  systematically  across  studies.  Accordingly,  the  coding  strategy  was

---

<!-- PAGE 22 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

designed not only to support thematic synthesis but also to reveal where the literature 
provides operationally useful evidence and where major reporting gaps remain.

Table 8: Data extraction and analytical mapping summary

Category

Data Extracted

General 
Identification

Study Identifier (code), 
Title, Authors, Year, 
Publication Type, Source 
Database

Framework 
Description

IoT Architectural 
Layer

Detection 
Approach / 
Algorithm

Data Source / 
Context

Performance 
Metrics

Privacy and 
Security 
Techniques

Interoperability 
and Scalability 
Indicators

Type of IoT-based 
framework (e.g., federated, 
blockchain, graph-based, 
deep learning, edge AI, 
fuzzy logic) 
Perception, Network, 
Processing, Application, or 
Security–Governance layer 
representation 
Machine Learning, Deep 
Learning, Federated 
Learning, Blockchain 
Integration, Graph Neural 
Networks, Anomaly 
Detection 
Dataset type (e.g., ISO 
8583, simulated IoT 
transactions, payment logs, 
edge-device data streams) 
Accuracy, Precision, Recall, 
F1-score, Latency, 
Communication Overhead, 
Energy Efficiency, Privacy 
Overhead 
Differential Privacy, SHA-
256, Homomorphic 
Encryption, K-Anonymity, 
Blockchain Auditability 
Cross-platform 
compatibility, network 
integration level, edge-fog-
cloud coordination

Linked 
Research 
Question(s) 
All RQs

RQ1, RQ4

RQ4

RQ1, RQ2

Purpose / Analytical 
Role

Enables traceability, 
transparency, and 
citation management 
across the 23 selected 
studies. 
Categorizes frameworks 
to facilitate comparative 
synthesis and taxonomy 
construction.

Maps frameworks to 
IoT ecosystem layers 
for layered framework 
synthesis. 
Identifies computational 
paradigms and 
architectural integration 
for pattern recognition.

Provides empirical 
grounding and 
application context of 
each framework. 
Enables quantitative 
benchmarking and 
comparative 
performance evaluation.

RQ1, RQ2

RQ1, RQ2, 
RQ3

Evaluates privacy-
preserving and trust 
mechanisms used in 
distributed models. 
Assesses the scalability 
and interoperability of 
IoT frameworks.

RQ2, RQ3

RQ2, RQ3

---

<!-- PAGE 23 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Category

Data Extracted

Limitations and 
Challenges

Proposed 
Solutions / 
Mitigation 
Strategies 
Emerging Trends 
/ Future 
Directions

Reported weaknesses (e.g., 
communication cost, 
latency, interoperability, 
energy consumption) 
Many studies on fraud 
detection frameworks 
describe them as real-time 
but fail to report key 
performance metrics like 
latency, inference time, or 
throughput, hindering 
objective evaluation. 
Optimization algorithms, 
encryption layers, edge 
computing, adaptive 
federated models 
Use of digital twins, self-
learning IoT nodes, ethical 
AI, and regulatory 
considerations

Tool Support / 
Implementation 
Evidence

Synthesis and 
Contribution 
Mapping

Simulation platforms, 
prototype deployment, or 
real-time testbeds (e.g., 
FogSim, TensorFlow, Edge 
devices) 
Key insight, contribution 
type (conceptual, technical, 
empirical), and impact 
statement

2.6 Analytical and Synthesis Strategy

Purpose / Analytical 
Role

Identifies systemic 
issues and informs 
design 
recommendations.

Linked 
Research 
Question(s) 
RQ1, RQ2, 
RQ3

Examines how prior 
studies addressed 
identified challenges.

RQ2, RQ3

RQ3, RQ4

RQ1, RQ4

All RQs

Captures evolving 
directions and 
anticipated 
technological 
transformations. 
Validates real-time 
capability and practical 
feasibility of reviewed 
frameworks.

Integrates qualitative 
and quantitative results 
into the unified IoT–
CNP Fraud 
Convergence 
Framework.

The analytical and synthesis strategy was designed to provide systematic progression 
from  evidence  gathering  to  framework  development.  Each  research  question  was 
addressed  using  specific  analytical  techniques,  enabling  structured  interpretation  of 
diverse findings aligned with the study's objectives. Table 9 summarizes the mapping 
of  research  questions,  analytical  techniques,  synthesis  approaches,  and  expected 
outcomes,  ensuring 
the 
reproducibility of the review.

in  evidence  processing  and  supporting

transparency

Table 9: Analytical and synthesis strategy for research questions

---

<!-- PAGE 24 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Research 
Question (RQ)

Analytical 
Technique

RQ1: How can 
existing IoT-based 
frameworks be 
synthesized to 
identify key 
performance 
benchmarks and 
research gaps in 
CNP fraud 
detection?

RQ2: How can 
distributed and 
privacy-preserving 
intelligence 
enhance the 
scalability and 
trustworthiness of 
IoT-based CNP 
fraud detection 
systems?

RQ3: What design 
principles can 
guide efficient, 
adaptive, and 
resilient IoT-driven 
fraud-detection 
frameworks?

• Chronological 
and typological 
mapping of 
frameworks  
• Quantitative 
benchmarking of 
accuracy, 
latency, 
scalability, and 
energy efficiency 
metrics

• Thematic coding 
of privacy and 
security features 
(e.g., federated 
learning, 
blockchain 
auditability, 
differential 
privacy)  
• Qualitative 
content analysis 
• Comparative 
design analysis  
• Problem–
solution matrix  
• Trend clustering 
via thematic 
synthesis

RQ4: How can a 
unified multi-layer 
IoT–CNP 
framework be 
developed to 
enhance real-time 
fraud detection and 
prevention?

• Integrative 
synthesis of 
results from 
RQ1-RQ3  
• Layer mapping 
and conceptual 
modeling  
• Taxonomy 
formulation

Expected Output / 
Deliverable

• Consolidated 
taxonomy of IoT-
based fraud-
detection 
frameworks  
• Benchmark matrix 
summarizing 
performance and 
interoperability 
indicators

• Evidence table of 
distributed learning 
models  
• Summary of 
scalability and trust-
enhancing 
mechanisms  
• Identified best 
practices for 
privacy-preserving 
architectures 
• Strategic design 
guideline set  
• Architecture-
performance 
correlation matrix  
• Recommendations 
for future IoT fraud-
detection design

• Final IoT-CNP 
Fraud Convergence 
Framework for 
scalable, 
explainable, and 
privacy-compliant.

Synthesis / 
Evaluation 
Approach 
• Comparative 
performance 
synthesis using a 
cross-study matrix  
• Descriptive 
statistics and trend 
identification  
• Framework 
evolution analysis 
(centralized - 
distributed - 
federated) 
• Cross-comparison 
of distributed-
intelligence 
approaches  
• Privacy-
performance trade-
off mapping  
• Evaluation of 
explainability and 
adversarial 
resilience 
• Synthesis of 
design strategies 
addressing 
communication 
overheads, adaptive 
learning, and 
resilience  
• Identification of 
recurring 
architectural motifs 
• Consolidation of 
analytical findings 
into six IoT layers 
(Perception, 
Network, 
Processing, Cloud 
Analytics, 
Application, 
Security-
Governance)

---

<!-- PAGE 25 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Research 
Question (RQ)

Analytical 
Technique

Expected Output / 
Deliverable

Synthesis / 
Evaluation 
Approach 
• Framework 
abstraction and 
validation roadmap

3 Literature Review

3.1 Evolution of IoT ecosystem for fraud detection and prevention

The layers of the IoT ecosystem have transitioned from abstract theoretical concepts 
to  fully  operational  systems  leveraging  edge  intelligence,  behavioral  analytics,  and 
adaptive  machine  learning  technologies.  This  progression  is  illustrated  in  Table  10, 
which provides a structured timeline detailing the evolution of various layers within the 
IoT ecosystem, particularly in the context of fraud detection. The analysis categorizes 
advancements across the fundamental layers. Each layer is essential to the architecture, 
enhancing fraud detection mechanisms and reinforcing the integrity of IoT systems.

From 2015 to April 3, 2026, the perception layer evolved from basic data sensing to 
the  integration  of  biometric  and  near  field  communication  (NFC)  technologies, 
providing  richer  contextual  insights.  The  network  layer  advanced  from  foundational 
encryption to sophisticated, large-scale, cloud-supported data flows. In the processing 
layer,  we  observed  a  transition  from  traditional  machine  learning  to  deep  learning, 
including  generative  adversarial  networks  (GANs),  and  real-time  analytics,  which 
enables scalable and adaptive detection. Meanwhile, the application layer progressed 
from simple user interfaces to advanced dashboards that incorporate explainable AI and 
adaptive  learning.  The  security  and  governance  layer  saw  notable  enhancements, 
integrating blockchain technologies and regulatory compliance mechanisms to enhance 
auditability and robustness.

These  layers  illustrate  a  developing  ecosystem  where  technological  innovation  is 
increasingly  aligned  with  real-time  responsiveness,  intelligent  capabilities,  privacy 
considerations,  and  regulatory  compliance  in  the  context  of  fraud  prevention.  This 
integration highlights the gradual, step-by-step improvement in the IoT fraud detection 
infrastructure observed over the past decade.

Table 10: Evolution timeline of IoT ecosystem layers in fraud detection

Layer

Perception Layer

Network Layer

Key Periods & Developments 
2015-2020:  Initial  adoption  of  IoT-enabled  payment  devices 
and sensors for real-time data collection.  
2021-April 3, 2026: Enhanced with NFC and biometric sensors 
for  double  verification  and  richer  behavioral/contextual  data 
capture. 
2015-2020:  Focus  on  secure,  reliable  data  transmission  and 
basic encryption protocols.  
2021-April 3, 2026: Integration of cloud networking, improved 
encryption,  and  support  for  high-speed,  large-scale  IoT  data 
flows.

---

<!-- PAGE 26 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Layer

Processing Layer

Application Layer

Security and 
Governance 
Layer

Key Periods & Developments 
2017-2022:  Introduction  of  machine  learning  (ML)  and  big 
data analytics for fraud detection.  
2023-April  3,  2026:  Adoption  of  deep  learning,  GANs,  and 
advanced  feature  engineering  for  real-time,  adaptive,  and 
scalable fraud analysis. 
2018-2022: Development of user interfaces for real-time alerts 
and risk visualization.  
2023-April  3,  2026:  Emphasis  on  explainable  AI,  adaptive 
learning,  and  user  feedback  integration  for  continuous 
improvement. 
2017-2022:  Implementation  of  basic  encryption  and  access 
control.  
2023-April  3,  2026:  Integration  of  blockchain,  advanced 
encryption, and regulatory compliance mechanisms for robust, 
tamper-resistant audit trails.

3.2 IoT Layered Taxonomy

Reviewing  IoT-driven  frameworks  through  a  layered  taxonomy  is  vital  for 
identifying their architectural strengths and weaknesses. Following the canonical IoT 
stack,  this  section  organizes  23  representative  frameworks  into  five  distinct  layers: 
perception, network, processing, application, and security and governance. Each layer 
encompasses various aspects of anomaly detection and fraud prevention.

Perception Layer: Device and Sensor Intelligence

The  perception  layer  comprises  sensors,  smart  cards,  near-field  communication 
(NFC) modules, and biometric capture units that collect transaction or behavioral data 
at its source.

A9 introduced an IoT-based smart card authentication model that integrates NFC re-
authentication  with  classifiers,  including  random  forests,  Bayesian  networks,  and  a 
multilayer perceptron. Their hybrid approach achieved 97% accuracy while reducing 
false positives by 5%, demonstrating the effectiveness of on-device anomaly detection. 
A20  developed  digital  twin  replicas  of  banking  environments  equipped  with  IoT 
sensors, achieving 92% accuracy and reducing the time to detect fraudulent transactions 
from  5  minutes  to  3  minutes.  Additionally,  edge-AI  approaches  improved  energy 
efficiency,  as  reported  by  A21,  with  edge-based  deep  learning  models  decreasing 
transmission load by 32% compared to cloud-only inference.

These studies illustrate that perception-layer frameworks significantly enhance real-
time  responsiveness  and  contextual  sensing.  However,  challenges  remain,  including 
sensor heterogeneity, spoofing threats, and limited cryptographic capabilities in low-
power devices.

Network Layer: Communication and Fog-Based Security

At the network layer, IoT data is transmitted through protocols such as Wi-Fi, 5G, 
or  low-power  wide-area  networks  (LPWAN)  to  fog  or  cloud  nodes  for  analysis. 
Network  anomalies  often  indicate  distributed  denial-of-service  (DDoS)  or  injection

---

<!-- PAGE 27 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

attacks, which can adversely affect payment gateways. A10 developed a fog computing 
framework specifically designed to mitigate DDoS attacks in blockchain-IoT systems, 
achieving  a  27%  reduction  in  latency  and  a  98.6%  throughput.  A5  introduced  IoT-
GRAF,  a  graph-learning-based  anomaly-detection  model  that  integrates  sensor  and 
communication data into a multimodal graph. This model, optimized for fog-computing 
environments, improved the F1-score by 22% compared to single-modal baselines. A12 
further  extended  this  concept  by  implementing  federated  intrusion  detection  across 
heterogeneous networks, thereby demonstrating high scalability and robustness against 
adversarial attacks. Collectively, these frameworks provide compelling evidence that 
fog  computing  and  graph-based  methodologies  significantly  reduce  network-layer 
delays and improve contextual anomaly detection. Nonetheless, challenges related to 
communication  overhead,  stemming 
frequent  gradient  exchanges  and 
from 
synchronization, remain a significant area for further exploration.

Processing Layer: Distributed and AI-Driven Fraud Analytics

The  processing  layer  encompasses  the  computational  intelligence  that  detects 
anomalies,  learns  behavioral  patterns,  and  makes  real-time  decisions.  A7  integrated 
federated learning (FL) and split learning (SL) to ensure data privacy while facilitating 
collaborative  anomaly  detection  across  IoT  nodes.  Their  system  achieved  98.8% 
accuracy and reduced communication costs by 35% compared to centralized models. 
A8 introduced FedGroup, a group-based FL algorithm that achieved 99.89% accuracy 
with a remarkably low false-positive rate of 0.02% in smart home anomaly detection. 
A6  evaluated  the  performance  of  FedAvg,  FedProx,  and  FedOpt  within  the  Flower 
framework,  attaining  99.94%  accuracy  on  both  the  UNSW-NB15  and  credit  card 
datasets.  A1  combined  ensemble  deep  neural  networks  and  clustering  in  an  IoT 
environment to effectively detect fraudulent transactions, achieving precision and recall 
rates above 96%.

These models demonstrate how federated and ensemble learning can surpass static 
rule-based systems, enabling adaptive and privacy-compliant analytics. Nevertheless, 
their  success  hinges  on  adequate  device  participation  and  stable  communication 
bandwidth, emphasizing the importance of lightweight model aggregation.

Application Layer: Contextual and Transactional Anomaly Detection

At the application layer, outputs from lower levels are contextualized for end-users, 
banks,  and  payment  processors.  A22  applied  anomaly-detection  techniques  to  IoT-
based financial transaction datasets to identify abnormal behavior, achieving a precision 
of  95%  and  an  F1  score  of  0.94.  A18  developed  a  multi-layer  perceptron  that 
incorporates federated learning for card fraud detection, achieving 98% accuracy while 
promoting fairness across clients. A19 developed an IoT-based transaction-monitoring 
application that provides real-time alerts and processes 10,000 transactions per second 
with minimal delay. A20 further showcased digital-twin-assisted monitoring interfaces 
that  dynamically  visualize  fraudulent  events.  Although  these  frameworks  enhance 
usability  and  decision-making,  they  must  still  address  challenges  related  to 
interpretability and cross-platform integration to facilitate widespread deployment.

Security and Governance Layer: Blockchain and Regulatory Compliance

---

<!-- PAGE 28 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

The  security  and  governance  layer  ensures  integrity,  transparency,  and  trust  by 
applying  cryptographic  and  regulatory  controls.  A3  introduced  NormaChain,  a 
blockchain-based, autonomous transaction settlement system that employs a three-layer 
sharded ledger and decentralized, public-key, searchable encryption. This framework 
achieved a throughput of 113 transactions per second and 100% supervision accuracy, 
effectively addressing concerns related to both privacy and legitimacy.

A2  advocated extending the Payment Card Industry Data Security Standard (PCI 
DSS) to cover IoT-based payments, highlighting the need for lightweight encryption 
and device compliance. Additionally, A15 presented a secure IoT anomaly framework 
that  leverages  homomorphic  encryption  and  distributed  ledgers,  achieving  99% 
accuracy while reducing energy consumption by 18%.

Complementary  studies,  such  as  those  by  A4,  emphasize  the  importance  of 
integrating  artificial  intelligence  (AI),  machine  learning  (ML),  and  data  science 
governance  to  improve  explainability  and  accountability.  Together,  these  research 
efforts  illustrate  that  blockchain  and  privacy-preserving  mechanisms  provide  robust, 
auditable  trust  anchors  for  IoT  financial  systems.  Nonetheless,  they  introduce 
computational overheads that must be effectively managed through sharding, Practical 
Byzantine Fault Tolerance (PBFT) consensus, and lightweight cryptography.

Cross-Layer Synthesis

Mapping  the  frameworks  across  the  layered  IoT  architecture  reveals  complex 
interdependencies  among  the  functions  of  sensing,  communication,  processing,  and 
governance.  The  sensing  capabilities  at  the  perception  layer  establish  the  contextual 
foundation  necessary  for  anomaly  detection  at  the  network  layer.  At  the  same  time, 
processing-layer  federated  learning  (FL)  models  rely  on  secure  governance  and 
blockchain-based trust mechanisms to uphold data integrity and privacy. Frameworks 
such  as  NormaChain  and  digital  twin-enabled  architecture  illustrate  how  integrating 
edge analytics with blockchain can enhance real-time visualization, transparency, and 
coordination  across  multiple  layers.  The  most  effective  systems  exhibit  vertical 
interoperability,  linking  the  perception  layer  to  governance  through  standardized 
protocols, privacy-aware computation, and auditable intelligence.

Despite

these  advances,

important  challenges

the 
communication  and  energy  overheads  of  synchronizing  distributed  learning  with 
blockchain-supported  governance,  the  persistence  of  heterogeneous  non-standard 
datasets,  and  the  limited  alignment  of  many  frameworks  with  compliance-oriented 
explainability and auditability requirements.

remain,  particularly

4. Results

4.1 Study Characteristics and Distribution

Table  11  reveals  a  globally  diversified  research  landscape  in  IoT-based  fraud 
detection  frameworks.  The  Asia-Pacific  region  accounts  for  43%  of  studies,  led  by 
India,  China,  Malaysia,  and  South  Korea,  where  IoT-enabled  financial  systems, 
federated learning, and edge computing have gained traction. These focus on real-time 
fraud analytics and mobile payment security, aligned with the region's digital economy 
growth.  Europe  (26%)  emphasizes  regulatory  and  privacy-oriented  frameworks, 
focusing  on  GDPR-compliant  mechanisms  and  blockchain-based  trust  architectures.

---

<!-- PAGE 29 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

North  American  research  (22%)  from  the  US  and  Canada  features  methodological 
sophistication, including adversarial resilient architectures and deep federated models. 
Emerging  regions  (9%)  demonstrate  strategic  importance  through  IoT-driven  digital 
banking  and  mobile fraud-prevention  mechanisms,  indicating  an  expanding  research 
frontier.

Institutional  distribution  indicates  a  strong  predominance  of  universities  and 
research  institutes  (78%),  underscoring  the  field's  academic  and  exploratory  nature, 
primarily  focused  on  developing  new  conceptual  frameworks  and  testing  proof-of-
concept prototypes. While industry and collaborative laboratories account for a smaller 
fraction (22%), they emphasize the application of IoT security, real-time analytics, and 
commercial FinTech deployment, thus bridging the gap between theoretical innovation 
and  operational  necessities  in  banking  and  e-commerce.  This  equilibrium  between 
academic inquiry and industrial experimentation reflects a maturing research ecosystem 
advancing from prototype development to scalable, real-world deployment.

The  analysis  of  publisher  distribution  reveals  key  dissemination  patterns. 
Institutional  and  regional  journals  (44%)  dominate,  showing  localized  IoT-FinTech 
research growth in Asia and Africa, with a focus on digital twin banking and IoT fraud 
frameworks. IEEE publications (26%) provide technical benchmarks in IoT architecture 
and blockchain security. Wiley (13%) contributes research on fog-blockchain models, 
while MDPI (9%) focuses on open-access and federated learning. Springer (4%) and 
Elsevier (4%) address theoretical foundations through governance frameworks and AI-
IoT convergence.

Table 11: Summary of Study Characteristics and Publication Distribution

Category

Sub-Category / 
Region / Journal 
Group

No. of 
Studies

Percentage 
(%)

Key  Research  Themes  / 
Focus

Asia-Pacific

10

43

Geographic 
Distribution

Europe

North America

Africa (Emerging 
Regions)

6

5

2

26

22

9

Institutional 
Context

Universities & 
Research Institutes

18

78

fraud 
federated  & 
learning,  mobile

IoT-enabled 
detection, 
edge 
payments. 
Privacy-preserving 
architectures, 
GDPR 
compliance,  blockchain 
trust. 
learning, 
Distributed 
adversarial 
resilience, 
scalable IoT frameworks. 
IoT-driven  FinTech  and 
banking fraud prevention. 
and 
theoretical 
Core 
IoT–
framework-driven 
CNP 
detection 
research.

fraud

---

<!-- PAGE 30 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Category

Sub-Category / 
Region / Journal 
Group

Industry / 
Collaborative Labs

5

22

No. of 
Studies

Percentage 
(%)

Key  Research  Themes  / 
Focus

Institutional / 
Regional Journals

10

44

IEEE (Journals & 
Conferences)

Publisher  / 
Journal 
Group

Wiley (ETT)

MDPI (Sensors, 
Electronics)

Springer (JNSM)

Elsevier (Computer 
Networks, FGCS)

6

3

2

1

1

26

13

9

4

4

Applied IoT security, data 
analytics,  and  FinTech 
deployment studies. 
IoT–FinTech 
frameworks,  digital  twin 
banking,  regional  fraud 
models. 
IoT  architecture,  edge 
computing,  blockchain-
enabled fraud detection. 
Fog–blockchain 
frameworks 
contract security. 
federated 
Open-access 
learning 
and  privacy-
preserving IoT analytics. 
Federated governance and 
privacy-aware 
anomaly 
detection. 
AI-IoT 
convergence, 
anomaly  detection,  and 
financial data analytics.

hybrid 
for  smart-

Total

23

100%

4.2 Overview of Reviewed Frameworks and Analytical Structure

This  review  organizes  the  examined  studies  by  architectural  paradigm,  IoT  layer 
involvement,  performance  focus,  and  coverage  of  research  questions,  enabling  a 
systematic  identification  of  strengths,  limitations,  and  research  gaps  in  IoT-enabled 
CNP fraud detection. The literature encompasses a wide range of approaches, including 
machine learning-driven fraud detection, edge- and fog-assisted analytics, distributed 
and  federated  intelligence,  blockchain-supported  governance,  and  hybrid  multi-layer 
IoT architectures. While these studies collectively highlight the increasing importance 
of  IoT  ecosystems  in  real-time  fraud  detection,  they  differ  significantly  in  their 
evaluation rigor, deployment assumptions, and system-level integration. Consequently, 
direct comparisons based solely on reported accuracy or latency metrics are inadequate 
for assessing their practical relevance in CNP transaction environments.

To address this challenge, the analysis in this section adopts a research-question-
driven categorization strategy. Each study is examined with respect to four analytical 
dimensions aligned with the study’s research questions:

(I).  performance benchmarking and evaluation metrics (RQ1), 
(II). distributed and privacy-preserving intelligence (RQ2), 
(III). design principles for efficiency, adaptability, and resilience (RQ3), and

---

<!-- PAGE 31 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

(IV).

integration into unified, multi-layer IoT-CNP frameworks (RQ4).

Table 12 operationalizes this categorization by mapping each reviewed study to its 
primary analytical paradigm, dominant IoT layer(s), real-time orientation, privacy/trust 
mechanism, application context, and explicit research-question coverage. This mapping 
enables cross-sectional traceability across Sections 4 and 5, ensuring that subsequent 
discussions on application scenarios, performance evaluation, distributed learning, and 
framework synthesis are grounded in clearly identified evidence.

Table 12: Analysis of study categorization and research question coverage.

Code

Primary 
Paradigm

Key IoT 
Layer(s)

Real-Time 
Orientation

Privacy / 
Trust 
Mechanism

Application 
Context

Performance 
Focus (RQ1)

Distributed 
/ Privacy 
Focus 
(RQ2)

Design

Framework

Principles

Integration

(RQ3)

(RQ4)

A1

ML-based 
fraud 
detection

Analytics, 
Application

Near real-
time

None

A2

IoT device 
security

Perception, 
Network

Real-time

Device-level 
security 
(NFC)

IoT credit 
card fraud 
detection 
Smart card 
IoT 
payments

A3

Compliance-
driven 
architecture

Governance, 
Security

Near real-
time

PCI DSS 
compliance

Secure IoT 
payments

A4

Fog + 
Blockchain

Edge, 
Governance

Near real-
time

Data locality 
(FL)

A5

A6

FL + SL 
anomaly 
detection

Federated 
IDS 
(FedAvg)

Analytics, 
Edge

Near real-
time

Federated + 
Split 
Learning

Analytics, 
Edge

Near real-
time

Blockchain 
immutability

A7

Multi-agent 
AI-IoT

Edge, 
Analytics

Real-time

Implicit

A8

A9

A10

Federated 
IDS

Analytics, 
Edge

Near real-
time

Model 
sharing only

Hybrid 
Fuzzy + FL 
DL intrusion 
detection

Analytics, 
Application

Near real-
time

Analytics  Real-time

Federated 
learning 
Adversarial 
resilience

Privacy-
aware IoT 
anomaly 
detection 
Privacy-
preserving 
IoT 
analytics 
DDoS & 
fraud 
mitigation 
Adaptive 
financial 
services 
IoT 
intrusion 
detection 
Metaverse 
IoT security 
Real-time 
IoT

✓

–

–

✓

✓

✓

✓

✓

✓

✓

–

–

–

✓

✓

✓

–

✓

✓

–

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

–

–

✓

✓

–

–

✓

–

–

–

---

<!-- PAGE 32 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Code

Primary 
Paradigm

Key IoT 
Layer(s)

Real-Time 
Orientation

Privacy / 
Trust 
Mechanism

A11

ML-based 
IoT security

Network, 
Analytics

Near real-
time

None

A12

A13

A14

A15

Deep 
learning 
ensembles 
AI-driven 
fraud 
detection 
Federated 
MLP 
IoT 
transaction 
analytics

Analytics  Real-time  None

Application

Near real-
time

None

Analytics, 
Edge

Near real-
time

Federated 
learning

Application

Near real-
time

None

A16

Digital twin 
+ IoT

Edge, 
Analytics

Real-time

Implicit

A17

A18

Edge AI + 
cloud 
Unsupervised 
anomaly 
detection

Edge, Fog  Real-time

Implicit

Analytics

Near real-
time

None

A19

AI–IoT 
integration

Analytics

Near real-
time

None

A20

Graph-based 
learning

Analytics, 
Network

Near real-
time

None

A21

Blockchain 
settlement

Governance

Near real-
time

Blockchain 
trust

A22

Group-based 
FL

Analytics, 
Edge

Near real-
time

Privacy-
aware FL

A23

IoT-AI fraud 
protection

Application  Real-time

Implicit

Application 
Context

Performance 
Focus (RQ1)

Distributed 
/ Privacy 
Focus 
(RQ2)

Design

Framework

Principles

Integration

(RQ3)

(RQ4)

intrusion 
detection 
IoT 
anomaly 
detection 
IoT 
anomaly 
streams 
Financial 
fraud 
profiling 
Credit card 
fraud 
Transaction 
anomaly 
detection 
Real-time 
fraud 
monitoring 
Financial 
analytics

Financial 
IoT fraud

AI-IoT 
decision 
systems 
Graph-
based 
anomaly 
detection 
IoT e-
commerce 
settlement 
IoT 
anomaly 
detection 
Digital 
wallet 
protection

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

–

✓

✓

✓

–

–

–

–

–

–

–

–

–

✓

✓

–

✓

✓

–

✓

–

✓

✓

✓

✓

✓

✓

✓

–

–

–

–

–

–

✓

✓

–

✓

–

✓

–

–

---

<!-- PAGE 33 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Legend: explicitly addressed (✓); not primary focus (–)

The distribution of studies within the field reveals significant patterns that deserve 
attention.  Primarily,  research  has  concentrated  on  local  or  centralized  performance 
evaluations, typically emphasizing metrics such as detection accuracy and latency in 
isolation.  In  contrast,  there  is  a  noticeable  lack  of  studies  focusing  on  distributed 
intelligence and privacy preservation. Moreover, although a handful of papers suggest 
design  principles  informed  by  architectural  elements,  these  proposals  often  lack 
formalization and systematic evaluation.

Another critical observation is the limited number of studies that investigate end-to-
end  framework  integration  across  different  IoT  layers  and  transaction  stages.  This 
reveals  a  gap  between  innovations  at  the  component  level  and  the  comprehensive 
system design necessary for practical deployment. To address these insights, a layered 
analysis is warranted.

A critical distinction emerging from the reviewed literature is that many frameworks 
are  described  as  real-time  in  a  conceptual  or  architectural  sense,  but  only  a  subset 
provides empirical evidence that they operate under genuine real-time constraints. In 
several studies, the use of edge computing, streaming analytics, online learning, or IoT 
telemetry  implies  time-sensitive  intent,  yet  this  is  not  accompanied  by  systematic 
measurement  of  end-to-end  decision  latency,  model  inference  time,  transaction 
throughput, or sustained performance under realistic operational load. Accordingly, this 
review  does  not  treat  all  real-time  claims  as  equivalent  and  distinguishes  between 
proposed  real-time  readiness  and  demonstrated  real-time  performance.  Real-time 
framing  appears  primarily  in  studies  A14,  A16,  A20,  and  A23,  but  the  level  of 
validation varies substantially across them.

Also, studies differ not only in evaluation rigor and deployment assumptions, but 
also in the nature of the datasets used, including credit card transaction datasets, IoT 
intrusion  datasets,  simulated  environments,  smart-home  anomaly  datasets,  and 
application-specific financial telemetry. Consequently,  metrics such as accuracy, F1-
score,  precision,  recall,  and  even  latency  cannot  be  directly  comparable  across  all 
studies, as they reflect different class distributions, feature spaces, attack surfaces, and 
operational settings.

Specifically, Section 4.2 delves into application scenarios within real CNP contexts, 
while  Section  4.3  assesses  performance  metrics  and  benchmarking.  Section  4.4 
emphasizes distributed learning and privacy-preserving models. Finally, Sections 4.5 
and 4.6 synthesize the findings, resulting in established design principles and a cohesive 
multi-layer IoT-CNP framework.

4.3 Application Scenarios and Case-Study Contexts

IoT-enabled CNP fraud detection frameworks are developed and evaluated across a 
wide  range  of  operational  environments,  each  characterized  by  distinct  transaction 
dynamics, latency constraints, privacy considerations, and deployment assumptions. A 
comprehensive  understanding  of  various  application  scenarios  is  essential  for 
accurately  interpreting  reported  performance  results  and  evaluating the  feasibility  of 
real-world deployment. For instance, models specifically optimized for centralized e-
commerce platforms may not be directly transferable to other contexts, such as edge-
assisted mobile payment systems or federated monitoring across multiple institutions.

---

<!-- PAGE 34 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Table  13  summarizes  the  primary  application  scenarios  and  case-study  contexts 
addressed by the reviewed studies, mapping each group of works to its dominant IoT 
context,  deployment  setting,  and  analytical  emphasis.  This  scenario-based 
categorization  provides  the  empirical  foundation  for  the  subsequent  analysis  by 
clarifying where and how different IoT-CNP fraud detection approaches operate. It also 
motivates  the  differentiated  performance  evaluation  criteria  discussed  later  in  this 
section,  ensuring  that  performance  metrics  are  interpreted  relative  to  their  intended 
operational environments rather than in isolation.

Building  on  this  classification,  the  remainder  of  this  section  examines  each 
application  scenario  in  turn,  highlighting  representative  case  studies,  common 
architectural  patterns,  and  context-specific  challenges  that  influence  fraud-detection 
effectiveness and system scalability.

Table 13: Application Scenarios and Case-Study Contexts for IoT-Enabled CNP 
Fraud Detection

IoT Context

Transaction 
streams, user 
behavior, 
device 
metadata

Mobile 
devices, NFC 
sensors, edge 
gateways

Multi-
institution IoT 
nodes, 
distributed data 
silos

IoT payment 
systems with 
ledger 
integration

Deployment 
Setting

Centralized / 
cloud-based

Edge / fog-
assisted

Federated / 
collaborative

Hybrid (IoT + 
blockchain)

Application 
Scenario

Representative 
Studies

E-commerce 
payment 
gateways

A1, A17, A19, 
A22, A23

Edge-assisted 
mobile and IoT 
payments

A9 A11, A20, 
A21

Distributed and 
federated fraud 
monitoring

A6, A7, A8, A10, 
A12, A13, A16, 
A18

A2, A10, A18, 
A3

Blockchain-
supported 
transaction and 
auditing

Multi-layer and 
cross-
ecosystem IoT 
frameworks

A5, A6, A7, A8, 
A12, A18

End-to-end IoT 
ecosystems

Cross-layer 
(edge-cloud-
governance)

Primary 
Analytical Focus 
Transaction-level 
fraud 
classification and 
anomaly 
detection 
Low-latency 
detection, energy 
efficiency, 
adaptive 
inference 
Privacy-
preserving 
learning, 
scalability, and 
non-IID 
robustness 
Auditability, 
trust, compliance, 
settlement 
integrity 
Framework 
integration, 
adaptability, 
system-level 
resilience

---

<!-- PAGE 35 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

4.3.1 E-Commerce Payment Gateway Scenarios

E-commerce  payment  gateways  represent  the  most  mature  and  widely  studied 
application context for IoT-enabled CNP fraud detection. As summarized in Table 13, 
studies in this category (A1, A17, A19, A22, A23) primarily operate in centralized or 
cloud-based environments, where high transaction volumes and diverse user behavior 
necessitate robust, scalable fraud-detection mechanisms.

In  these  scenarios,  IoT  contributions  are  typically  indirect,  manifesting  through 
device  metadata,  session  fingerprints,  and  behavioral  signals  captured  during  online 
transactions. Machine learning and deep learning models dominate this context, with 
performance evaluation focusing on detection effectiveness metrics such as accuracy, 
precision,  recall,  F1-score,  and  false-positive  rate.  While  many  studies  report  strong 
classification  performance,  they  often  assume  stable  connectivity  and  centralized 
processing,  limiting  direct  applicability  to  latency-sensitive  or  privacy-constrained 
environments.

A key limitation in this scenario is the underutilization of edge intelligence, as most 
frameworks defer inference to the cloud. This motivates the exploration of alternative 
deployment  models discussed  in  subsequent scenarios, particularly  for  real-time  and 
privacy-sensitive CNP environments.

4.3.2 Edge-Assisted Mobile and IoT Payment Scenarios

Edge-assisted mobile and IoT payment scenarios, highlighted in Table 13 by studies 
such as A9, A11, A20, and A21, address the limitations of purely centralized detection 
by  introducing  edge  and  fog-level  analytics.  These  environments  include  mobile 
wallets,  NFC-enabled  payments,  and  smart  point-of-sale  systems,  where  latency, 
energy efficiency, and intermittent connectivity are critical operational constraints.

In this context, fraud detection models are often deployed partially or entirely at the 
edge,  enabling  faster  response  times  and  reducing  reliance  on  continuous  cloud 
communication. Performance evaluation extends beyond detection accuracy to include 
end-to-end  latency,  inference  time,  and  energy  consumption,  reflecting  real-world 
deployment  considerations.  The  reviewed  studies  demonstrate  that  edge-assisted 
architectures  can  significantly  reduce  response  delays  while  maintaining  acceptable 
detection  performance,  particularly  when  lightweight  models  or  adaptive  inference 
strategies are employed.

However,  edge-assisted  scenarios  also  introduce  challenges  related  to  resource 
heterogeneity  and  model  maintenance,  underscoring  the  need  for  adaptive  and 
distributed learning mechanisms explored in Section 4.5.

4.3.3 Distributed and Federated Fraud Monitoring Scenarios

Distributed and federated fraud monitoring scenarios constitute a rapidly growing 
application domain, as reflected in Table 13 (A6, A7, A8, A10, A12, A13, A16, A18). 
These scenarios are characterized by multi-institution collaboration, where data silos 
across banks, merchants, and payment processors prevent centralized data aggregation 
due to privacy, regulatory, or competitive constraints.

Federated and distributed learning frameworks enable collaborative model training 
through parameter sharing rather than raw-data exchange. Performance evaluation in 
this  context  emphasizes  scalability,  communication  overhead,  convergence  stability, 
and  robustness  to  non-independent  and  identically  distributed    (non-IID)  data,  in

---

<!-- PAGE 36 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

addition  to  traditional  detection  metrics.  Empirical  results  indicate  that  federated 
approaches  can  achieve  near-centralized  performance  while  preserving  data  locality, 
particularly when heterogeneity-aware aggregation strategies are employed.

These scenarios highlight a fundamental shift in CNP fraud detection, from isolated, 
institution-specific models toward ecosystem-level intelligence, laying the groundwork 
for the privacy-preserving architectures discussed in Section 4.5.

4.3.4 Blockchain-Supported Transaction and Auditing Scenarios

Blockchain-supported scenarios, identified in Table 13 by studies such as A2, A3, 
A10, and A18, extend IoT-enabled CNP fraud detection beyond real-time decisioning 
to include auditability, trust, and compliance. In these settings, distributed ledgers are 
used  to  record  transaction  events,  model  updates,  and  fraud  alerts  in  an  immutable, 
verifiable manner.

The primary analytical focus in this scenario shifts from detection accuracy alone to 
governance-oriented  metrics,  including  audit  latency,  transaction  throughput,  and 
provenance  completeness.  Blockchain  integration  enhances  trustworthiness  and 
forensic accountability, particularly in regulated environments requiring post-incident 
investigation and dispute resolution. However, these benefits often come at the cost of 
increased  coordination  overhead  and  confirmation  delays,  necessitating  careful 
architectural trade-offs.

As such, blockchain-supported scenarios are best viewed as complementary to AI-
driven detection, providing governance and trust support rather than replacing real-time 
analytics.

4.3.5 Multi-layer and Cross-Ecosystem IoT Scenarios

Multi-layer and cross-ecosystem IoT scenarios, as outlined in Table 13 from studies 
A5, A6, A7, A8, A12, and A18, broaden the scope of IoT-enabled CNP fraud detection. 
These  scenarios  involve  collaborative  environments  with  multiple  stakeholders, 
including merchants, payment processors, and financial institutions, and distribute fraud 
detection logic across different layers: perception, edge/fog, analytics, and governance.  
The  focus  shifts  from  transaction-level  accuracy  to  system-level  coordination 
metrics, such as communication overhead, robustness to non-IID data, scalability, and 
cross-layer  latency.  Federated  and  group-based  learning  frameworks  (A6,  A8,  A12, 
A18) enable model training without centralizing sensitive data, while hybrid approaches 
(A7)  address  device heterogeneity.  Graph-based  models  (A5) enhance  awareness by 
capturing relationships among entities.

Performance  evaluation  emphasizes  collaboration  efficiency  and  resilience, 
considering  metrics  such  as  coordination  latency,  client  participation  stability,  and 
adaptability  to  evolving  fraud  patterns  as  crucial  indicators  alongside  detection 
performance.

Ultimately, these  multi-layer, cross-ecosystem IoT scenarios represent system-of-
systems  deployments  in  which  integrated,  privacy-preserving  intelligence  emerges. 
This  informs  the  unified  multi-layer  IoT-CNP  framework  presented  in  Section  4.6, 
which combines distributed analytics, adaptive learning, and governance mechanisms 
into a cohesive reference architecture.

---

<!-- PAGE 37 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

4.3.6 Synthesis of Application Scenarios

The application scenarios in Table 13 show that IoT-enabled CNP fraud frameworks 
operate  under  distinct  deployment  constraints.  Centralized  e-commerce  systems 
prioritize transaction-scale detection accuracy, edge-assisted environments emphasize 
latency and operational efficiency, distributed monitoring scenarios foreground privacy 
and  coordination,  and  blockchain-supported  architectures  strengthen  trust  and 
governance. These differences indicate that performance claims must be interpreted in 
relation  to  deployment  context  rather  than  through  a  one-size-fits-all  benchmarking 
lens.

4.4 Performance Evaluation of Frameworks

Performance  evaluation  in  the  reviewed  literature  clusters  around  four  recurring 
dimensions: detection effectiveness, real-time responsiveness, scalability and resource 
efficiency,  privacy,  trust,  and  governance  assurances.  Because  the  included  studies 
differ  substantially  in  datasets,  application  contexts,  deployment  assumptions,  and 
reporting completeness, the synthesis is presented as a comparative evidence map rather 
than as a strict meta-analytic ranking.

Table  14  summarizes,  where  reported,  the  principal  benchmarking  dimensions 
across  studies.  The  findings  indicate  that  predictive  effectiveness  metrics  are 
predominant across various scenarios, whereas reporting on real-time responsiveness 
and  system-level  scalability  remains  inconsistent.  Studies  explicitly  focused on  real-
time  applications  (A14,  A16,  A20,  A23)  tend  to  emphasize  latency  and  deployment 
metrics. Conversely, federated studies (A6, A7, A8, A12, A18) incorporate additional 
scalability considerations, notably communication overhead and client heterogeneity. 
Blockchain-oriented  studies  (A10,  A3)  primarily  focus  on  trust  and  auditability, 
requiring  throughput  and  confirmation  latency  metrics  to  support  claims  about  real-
world deployment.

Table 14: Performance Evaluation Metrics by Study and Application Scenario

Co
de

Scena
rio

Primary 
Technique

Eff. Metrics 
(examples)

A1  S1

RF/DNN/S
VM 
ensemble

Acc, Prec, 
Rec, F1, 
AUC

A2  S4

PCI DSS 
extension

Control 
coverage, 
compliance 
maturity

A3  S4

Blockchain 
+ SC + SE

System-level

RT 
Metrics 
(example
s) 
Inference 
time, 
decision 
delay

Process 
timing  
(if any)

Confirmat
ion 
latency

Scale 
Metrics 
(examples)

Priv./Trust 
Metrics 
(examples)

Bas
is

Model 
complexity

-

T

Operational 
overhead

Compliance 
assurance

Throughput/
TPS, storage

Auditability, 
encryption

E

E

---

<!-- PAGE 38 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Co
de

Scena
rio

Primary 
Technique

Eff. Metrics 
(examples)

RT 
Metrics 
(example
s)

Scale 
Metrics 
(examples)

Priv./Trust 
Metrics 
(examples)

Bas
is

Acc/F1

-

Compute/sca
le (if 
discussed)

Inference 
time

Graph size 
scalability

A4  S2

A5  S2/S3*

DL + 
predictive 
analytics 
GNN + 
multimodal 
fusion

A6  S3

Federated 
learning

Acc/F1/AUC; 
intrusion/ano
maly metrics

Acc/F1/AUC 
(task-
dependent)

Round 
time, 
update 
interval

#clients, 
comm 
rounds

Data 
locality/privacy 
discussion

E/T

-

-

T

T

A7  S3

FL + Split 
learning

Acc/F1/AUC; 
anomaly 
metrics

Train/infe
r time

A8  S3

FedGroup

Acc/F1/AUC; 
anomaly 
metrics

Round 
time

Comm cost + 
split 
overhead 
Comm 
rounds; 
group 
heterogeneit
y

Privacy-
preserving 
training

Privacy-aware 
FL

E

E

A9  S2

NFC + 
RF/BN

Acc, Prec, 
Rec, F1

Verificati
on latency

Device 
overhead

A10 S4

Blockchain 
+ fog

A11 S2

DL + 
multi-agent

Detection 
rate/FPR 
(security 
task) 
Acc/F1/AUC; 
anomaly 
metrics

Fog 
response 
time

Fog 
scalability, 
node load

Decision 
latency (if 
measured)

Resource 
footprint

A12 S3

FedAvg 
IDS

DR/TPR, 
FPR, F1

Round 
latency

Comm 
rounds, 
client 
heterogeneit
y

NFC 
assurance/devic
e trust

E/T

Integrity/audita
bility

E/T

-

T

Privacy by 
design (FL)

E/T

A13 S3

Fuzzy + FL

A14 S2

CNN–
LSTM + 
resilience

Acc/F1; 
anomaly 
metrics 
DR/TPR, 
FPR, F1, 
AUC

Update 
interval

Comm cost

Privacy by 
design (FL)

E/T

Latency / 
time-to-
detect

Energy 
efficiency, 
model size

Adversarial 
robustness

E

---

<!-- PAGE 39 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Bas
is

T

E/T

T

E/T

RT 
Metrics 
(example
s) 
Inference 
time

Decision 
time (if 
any)

Round 
time

Inference 
time 
Online 
update 
delay 
Edge 
response 
latency

Inference 
time

Co
de

Scena
rio

Primary 
Technique

Eff. Metrics 
(examples)

A15 S1/S2*

A16 S2

RF/SVM 
ensembles 
Deep 
models + 
ensembles

A17 S1

AI rules + 
NNs

A18 S3

FL MLP

Acc, Prec, 
Rec, F1 
Acc/F1 
(multi-class), 
macro-F1 
Acc/F1/AUC; 
profiling 
quality 
Acc, Prec, 
Rec, F1, 
AUC

A19 S1

DT/GB

Acc/F1/AUC

A20 S2

Digital 
twin + edge 
+ online

Acc/F1/AUC; 
detection 
stability

A21 S2

Edge AI + 
cloud/fog

System-level

A22 S1

IF + 
autoencode
r

AUC, PR-
AUC, 
anomaly 
score metrics

A23 S2

AI + IoT 
sensors

Acc/F1/AUC

Scale 
Metrics 
(examples)

Priv./Trust 
Metrics 
(examples)

Model 
complexity

Stream 
latency

Throughput, 
compute load

-

-

-

-

Comm 
rounds/#clie
nts

Privacy by 
design (FL)

-

-

T

Edge 
resource use

Monitoring/con
trol reliability

E/T

Partitioning 
overhead

-

Real-time 
decision 
delay 
RT=Real-time/Latency

Edge/device 
overhead

-

-

-

T

T

E/T

Eff.=Effectiveness;

Legend: 
Scale=Scalability/resource efficiency; Priv/Trust=Privacy/trust indicators 
Scenario clusters: (S1) E-commerce gateway, (S2) Edge-assisted mobile/IoT payments, 
(S3) Distributed/Federated monitoring, (S4) Blockchain-supported auditing/settlement. 
“Basis” indicates whether the metric family is Explicit (E) or Typical (T), given the 
study’s stated method/focus.

responsiveness;

The literature predominantly reports predictive performance metrics, while latency, 
throughput,  coordination  costs  in  federated  settings,  and  privacy  overhead  are 
comparatively  underreported, 
limiting  rigorous  cross-study  comparability  and 
motivating  multi-dimensional  benchmarking  beyond  accuracy  alone.  Furthermore, 
substantial heterogeneity in datasets and experimental conditions means that reported 
metrics (e.g., accuracy, F1, AUC, false-positive rate, throughput, latency) should not be 
treated as definitive evidence of any framework’s superiority, but rather as indicative

---

<!-- PAGE 40 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

of broad performance tendencies, evaluation practices, and recurring trade-offs across 
application scenarios.

Table  15  summarizes  the  most  common  evaluation  omissions  across  different 
framework families, emphasizing the real-time constraints that are measured rather than 
simply claimed. It highlights gaps in systematic evaluation across various frameworks. 
Reporting latency, throughput, energy consumption, and communication costs is often 
inconsistent, even when real-time deployment is claimed.

Framewor
k family

Table 15 Evaluation gaps in addressing real-time constraints across framework 
families  
Energy 
reported 
(device/ed
ge cost)

Typical 
evaluation gap 
observed

Latency 
reported 
(end-to-end 
or decision 
latency)

Through
put 
reported 
(TPS / 
event 
rate)

Communicat
ion cost 
reported 
(bytes/ 
rounds 
/bandwidth) 
N/A

Low

Rare

Rare

Centralized 
/ gateway 
ML (S1)

Medium 
(often 
partial)

Edge-
assisted / 
mobile IoT 
payments 
(S2)

Federated / 
distributed 
monitoring 
(S3)

Medium 
(often 
coordination 
latency)

Blockchain
-supported 
governance 
(S4)

Medium 
(confirmatio
n/ audit 
latency)

Rare

Low-
Medium

Low

Rare

Rare

Medium

Medium

Rare

Medium

Detection Effectiveness Metrics

Emphasizes 
predictive 
metrics; limited 
operational 
profiling under 
real-time loads 
Reports 
response-time 
proxies, but 
omits end-to-
end latency and 
device energy 
profiling 
Reports 
collaboration 
claims but 
inconsistently 
quantifies 
rounds/bytes 
and latency 
trade-offs 
Addresses trust 
but often 
underreports 
overhead under 
realistic 
transaction 
volumes

---

<!-- PAGE 41 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Predictive  effectiveness  is  the  most  consistently  reported  performance  dimension 
across  studies.  In  centralized  scenarios,  effectiveness  is  evaluated  using  accuracy, 
precision, recall, F1-score, and AUC/ROC to distinguish fraudulent transactions (A1, 
A17,  A19,  A22).  In  unsupervised  settings  for  IoT  streams  (A22),  performance  is 
assessed using anomaly-scoring metrics and detection consistency. IoT intrusion studies 
(A14,  A16)  evaluate  multi-class  detection  and  stream  accuracy,  while  graph 
frameworks (A5) assess multi-modal fusion quality.

Implications for benchmarking (RQ1): As demonstrated in Table  14, effectiveness 
metrics  vary  substantially  across  task  formulations  and  scenarios.  Consequently, 
benchmarking  must  distinguish  at  minimum  between  (i)  transaction-level  fraud 
classification, (ii) IoT anomaly or intrusion detection as a fraud-relevant proxy, and (iii) 
hybrid monitoring and control systems. This confirms that “effectiveness” is scenario-
dependent and cannot be meaningfully compared without task-consistent metrics.

Real-Time Responsiveness and Operational Readiness

In  CNP  fraud  detection  systems  that  operate  under  real-time  constraints,  simply 
having  effective  detection  is  not  enough.  The  importance  of  real-time  processing  is 
highlighted  in  studies  (A14,  A16,  A20,  A23)  that  focus  on  areas  such  as  intrusion 
detection,  streaming  anomaly  detection,  digital  twin  monitoring,  and  digital  wallet 
protection, as presented in Table 14. Studies’ reporting practices remain inconsistent, 
with some using qualitative assertions of streaming suitability, while others report only 
partial  indicators,  such  as  inference  time,  without  documenting  complete  decision 
latency or throughput. Digital twin approaches (A20), though aligned with continuous 
monitoring, need systematic reporting of update frequency and detection delay.

Missing real-time evaluation metrics: In the studies reviewed, real-time claims were 
rarely  supported  by  comprehensive  and  operational  metrics.  Frequently  overlooked 
indicators include end-to-end decision latency (from capture to decision), throughput or 
event processing rate (measured in transactions per second), energy consumption (per 
inference,  per  round,  or  per  device),  and  communication  cost  (in  terms  of  bytes 
exchanged, number of rounds, and bandwidth assumptions). When metrics are reported, 
they  are  often  incomplete,  such  as  omitting  the  model  inference  time,  which  limits 
reproducibility and impedes a fair comparison of real-time readiness across different 
architectures.

Implication  for  benchmarking  (RQ1)  and  design  principles  (RQ3):  Real-time 
responsiveness should be treated as a first-class evaluation dimension. At a minimum, 
studies should report one or more of the following: decision latency, event processing 
rate  or  throughput,  model  update  interval,  and  time  to  detection.  The  absence  of 
standardized  reporting  of  responsiveness  highlights  a  recurring  design  gap  in  the 
literature.

Scalability and Resource Efficiency

Scalability  evaluation  varies  across  paradigms  due  to  system  constraints.  Edge-
assisted scenarios (S2) consider computational footprint, energy use, and deployment 
feasibility. Studies on efficiency (A14, A21) address these concerns, though resource 
profiling  remains  limited.  In  distributed  and  federated  monitoring  (S3),  scalability 
encompasses  coordination  metrics  such  as  communication  overhead,  client 
participation, convergence, and robustness to non-IID data. Federated learning studies

---

<!-- PAGE 42 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

(A6,  A12,  A18,  A8)  and  hybrid  FL-SL  approaches  (A7)  address  scalability  under 
privacy constraints (see Table 14), though comparability requires consistent federation 
metrics.

Implication  for  RQ2:  Scalability  in  privacy-preserving  intelligence  encompasses 
not only computational aspects but also organizational and coordination-related factors. 
To  effectively  substantiate  RQ2,  studies  focusing  on  federated  and  split-learning 
methodologies must provide comprehensive reporting on both detection effectiveness 
and  the  associated  collaboration  costs.  These  costs  may  include  metrics  such  as  the 
number  of  communication  rounds,  bandwidth  assumptions,  and  variations  in  client 
heterogeneity.

Privacy, Trust, and Governance Indicators

A  fundamental  distinction  among  frameworks  lies  in  whether  their  performance 
evaluations extend beyond detection metrics to encompass privacy and trust assurances. 
Research  on  federated  and  split  learning  (A6,  A7,  A8,  A12,  A18)  underscores  the 
significance  of  privacy  through  the  principle  of  data  locality;  however,  the  rigor  of 
privacy evaluations varies considerably across studies. Those that incorporate explicit 
threat models or leakage analyses provide more robust evidence compared to those that 
rely solely on architectural assertions.

Blockchain-supported  scenarios  (S4)  introduce  trust  as  a  system-level  attribute. 
Studies integrating blockchain with IoT and fog computing (A10) or smart contract-
based settlement and searchable encryption (A3) emphasize integrity, auditability, and 
autonomous enforcement. In these cases, performance evaluation must include metrics 
such as throughput, confirmation latency, and operational overhead, as summarized in 
Table 14.

Implication for RQ2 and RQ4: Trustworthiness in IoT-based CNP fraud detection 
arises  from  integrating  privacy-preserving  intelligence,  auditable  infrastructure,  and 
governance  controls,  rather  than  relying  on  a  single  technique.  Consequently,  the 
performance  evaluation  must  incorporate  both  technical  metrics  and  assurance 
indicators to enable the synthesis of a unified framework (RQ4).

Cross-Scenario  Benchmarking:  Comparability  Rules,  Evidence  Gaps,  and 
Research Implications

Synthesizing  performance  across  heterogeneous  scenarios  requires  explicit 
comparability rules. Based on the  results so far  and  scenario taxonomy in Table 13, 
three benchmarking principles are identified:

1.  Benchmark within the scenario: Gateway studies should compare against similar 
transaction-level frameworks; federated studies against distributed counterparts; 
and blockchain-supported systems against governance-oriented baselines.

2.  Report multi-dimensional performance: Accuracy alone is insufficient; real-time 
systems require responsiveness metrics, federated systems require coordination 
costs, and blockchain systems require throughput and auditability indicators. 
3.  State  deployment  assumptions  explicitly:  Dataset  characteristics,  streaming 
assumptions, and operational budgets must be documented to support meaningful 
benchmarking.

---

<!-- PAGE 43 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

The  evidence  reviewed  indicates  robust  metrics  for  predictive  effectiveness,  yet 
reveals  inconsistencies  in  reporting  real-time  responsiveness,  federation-specific 
scalability costs, and blockchain throughput under realistic loads. These shortcomings 
inform the design principles presented in Section 4.6 and the unified multi-layer IoT-
CNP framework in Section 4.7, which conceptualizes performance as a composite of 
accuracy, responsiveness, scalability, and trust, rather than a singular score.

4.5 Distributed Learning & Privacy-preserving Models

This  section  synthesizes  evidence  on  how  distributed  intelligence  and  privacy-
preserving computation enhance scalability, trustworthiness, and regulatory viability in 
the  context  of  IoT-enabled  CNP  fraud  detection,  especially  when  centralized  data 
aggregation is impractical. In alignment with RQ2, the literature increasingly portrays 
CNP  fraud  detection  as  a  collaborative  learning  challenge  that  involves  diverse  IoT 
nodes and various financial stakeholders. Within this framework, the focus transitions 
from the exchange of raw customer or device data to the sharing of model parameters, 
thereby minimizing privacy risks and alleviating institutional friction. 
Across the studies, three dominant technical families emerge: 
(I). federated learning (FL) and its variants, 
(II). split learning (SL) and hybrid FL-SL architectures, and 
(III).

ledger-anchored trust mechanisms that reinforce auditability and post-

incident traceability.

The  empirical  evidence  underpinning  this  subsection  is  summarized  in  Table  16, 
which  presents  representative  indicators  of  scalability  and  trustworthiness  across 
distributed learning designs.

Table 16: Distributed learning & privacy-preserving models

Cod
e

Distribute
d model

Privacy / 
Trust 
mechanism(s)

A4

Hybrid 
Fuzzy and 
FL

Federated 
coordination; 
privacy-aware 
rules

Scalability 
signals

Trustworthine
ss signals

Notable 
outcomes

Latency 31 ms, 
≈ Moderate 
comms, ↑ High 
energy 
saving/throughp
ut

↑ High privacy 
overhead 
(privacy 
features 
enabled)

Efficient learning 
under 
heterogeneous, 
metaverse-style 
traffic.

A6

Fog-
distributed 
detection 
and 
blockchain

Tamper-
evident ledger; 
node 
attestation

Latency 38 ms, 
≈ Moderate 
comms, ↑ High 
energy saving

↑ High privacy 
overhead 
(crypto/ledger)

Edge/fog scale 
with verifiable 
event trails.

A10

Federated 
IDS 
(FedAvg)

Secure 
aggregation; 
local training

Latency 27 ms, 
↓ Low comms, ↑ 
High energy 
saving, ↑ High 
throughput

↑ High privacy 
overhead (kept 
local; protected 
sharing)

Near-centralized 
accuracy 
(98.4/97.2) with 
strong scale and 
privacy retention.

---

<!-- PAGE 44 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Cod
e

Distribute
d model

Privacy / 
Trust 
mechanism(s)

A4

Hybrid 
Fuzzy and 
FL

Federated 
coordination; 
privacy-aware 
rules

Scalability 
signals

Trustworthine
ss signals

Notable 
outcomes

Latency 31 ms, 
≈ Moderate 
comms, ↑ High 
energy 
saving/throughp
ut

↑ High privacy 
overhead 
(privacy 
features 
enabled)

Efficient learning 
under 
heterogeneous, 
metaverse-style 
traffic.

A6

Fog-
distributed 
detection 
and 
blockchain

Tamper-
evident ledger; 
node 
attestation

Latency 38 ms, 
≈ Moderate 
comms, ↑ High 
energy saving

↑ High privacy 
overhead 
(crypto/ledger)

Edge/fog scale 
with verifiable 
event trails.

A11

SplitFed 
(split 
learning 
and FL)

Split layers; 
secure 
aggregation

A12

FedGroup 
(group-
based FL 
for non-
IID)

Group-wise 
aggregation; 
secure sharing

A13

Privacy-
preserving 
FL

Communicatio
n-efficient FL; 
privacy 
controls

A16

Federated 
MLP

Secure 
aggregation

A18

Blockchai
n-based 
settlement 
& audit

Smart 
contracts; 
sharded ledger

Latency 24 ms, 
≈ Moderate 
comms, ↑ High 
energy 
saving/throughp
ut 
Latency 22 ms, 
↓ Low comms, ↑ 
Very high 
throughput/ener
gy saving 
Latency 33 ms, 
↓ Low comms, ↑ 
High energy 
saving/throughp
ut 
Latency 28 ms, 
↓ Low comms, ↑ 
High energy 
saving/throughp
ut 
Latency 36 ms, 
↑ High comms, 
≈ Moderate 
throughput, ↓ 
Low energy 
saving

↑ High privacy 
overhead

↑ High privacy 
overhead (by 
design)

↑ High privacy 
overhead

↑ High privacy 
overhead

↑ High privacy 
overhead

Handles 
weak/heterogeneo
us clients while 
preserving 
privacy.

Best-in-class F1 
99.3, minimal 
FPR (0.02%), 
resilient to data 
heterogeneity.

Balanced 
efficiency–trust 
profile for real 
deployments.

Higher accuracy 
than siloed 
models without 
centralizing data.

Strong 
auditability; trust 
anchored in 
immutable 
records.

Federated and Split Learning for Privacy-Preserving Intelligence

Table 17 summarizes key studies on latency, communication costs, scalability, and 
trustworthiness in distributed learning architectures. Federated learning (FL) is widely

---

<!-- PAGE 45 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

utilized  to  promote  collaboration  among  organizations  without  direct  data  sharing, 
particularly in environments featuring distributed IoT streams and payment telemetry 
(A4, A10, A12, A16). FL-based systems consistently achieve decision latencies under 
30  milliseconds  with  low  communication  overhead  while  maintaining  performance 
comparable to that of centralized detection systems. Specialized FL variants, such as 
heterogeneity-aware and group-based approaches (A12), effectively address challenges 
posed  by  non-IID  data  common  in  IoT  payment  ecosystems,  thereby  improving 
robustness and reducing false-positive rates.

Additionally,  split  learning  and  FL-split  learning  hybrids  (A11,  A13)  enhance 
privacy by partitioning model computations: sensitive feature representations remain 
on  client  devices,  while  deeper  layers  execute  on  server-side  infrastructure.  These 
architectures are particularly suited to resource-constrained edge devices and merchant 
gateways,  balancing  detection  quality,  computational  efficiency,  and  regulatory 
compliance.

Operational  Trade-offs  of  Federated  and  Split  Learning  in  Real-Time  CNP 
Detection

Although  federated  and  split  learning  are  often  suggested  as  privacy-preserving 
options  for  distributed  fraud  detection,  the  studies  reviewed  highlight  significant 
practical trade-offs that affect real-time CNP deployment. Federated learning minimises 
raw data exposure but introduces coordination delays, communication overhead, and 
sensitivity to client heterogeneity, which are seldom quantified under transaction-level 
time constraints.

However, split learning transfers part of the model computation to the client or edge, 
reducing  communication  payloads  but  increasing  on-device  computation  costs  and 
dependence on reliable, low-latency links between split layers. In the literature, both 
paradigms are generally assessed based on predictive accuracy, with limited empirical 
evaluation of round duration, synchronisation delays, energy consumption, or end-to-
end  decision  latency,  leaving  their  readiness  for  real-time  applications  insufficiently 
validated.

Table 17 provides a comparative analysis of federated and split learning, focusing

on their operational implications for real-time CNP fraud detection.

Table 17: Comparative analysis of federated and split learning for real-time CNP 
fraud detection

Category 
Primary privacy 
mechanism 
Communication 
pattern 
Latency 
implications 
Energy impact on 
the client

Federated Learning 
Model update aggregation 
without raw data sharing 
Periodic bidirectional 
updates (many rounds) 
Coordination and 
aggregation delays 
Medium (local training + 
communication)

Suitability for real-
time CNP

Moderate, but sensitive to 
round duration

Split Learning 
Feature/activation partitioning 
across client–server 
Frequent but smaller exchanges 
per inference/training step 
Inference pipeline dependency 
between split layers 
Medium–High 
(forward/backward computation 
on-device) 
Context-dependent; requires 
stable low-latency links

---

<!-- PAGE 46 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Common evaluation 
gap

Lack of round-time and 
throughput reporting

Lack of end-to-end latency and 
device energy profiling

Coordination overhead, synchronization, and convergence challenges

In addition to the privacy benefits, the studies reviewed underscore the substantial 
coordination  costs  associated  with  IoT-enabled  CNP  detection  using  distributed 
learning.  A  prominent  issue  is  the  communication  overhead  caused  by  frequent 
exchanges of models or activations. In reference to Table 17, federated learning entails 
multiple  rounds  of  aggregation  traffic,  whereas  split  learning  requires  continuous 
interaction  between  clients  and  servers  throughout  both  the  training  and  inference 
phases. The synchronization costs are further intensified by device heterogeneity and 
intermittent connectivity, which may lead to stragglers and delayed global updates in 
federated environments, or to stalled inference pipelines in split learning architectures. 
Convergence challenges are further complicated by non-IID transaction data, partial 
participation, and dynamic client availability, factors that are rarely rigorously tested 
under real-time payment conditions. These challenges cast doubt on the scalability of 
current designs without explicit coordination-aware optimisation.

Privacy-Performance Trade-offs and Operational Cost Drivers

Distributed  learning  effectively  minimizes  exposure  to  raw  data;  however, 
safeguarding  privacy  incurs  substantial  operational  costs.  The  deployment  of  secure 
aggregation,  encryption,  and  coordination  mechanisms  can  result  in  increased 
communication overhead, added complexity in synchronization processes, and potential 
latency increments in specific configurations. These trade-offs are elucidated in Table 
16, which demonstrates that enhanced privacy and trust guarantees are accompanied by 
varying degrees of communication and energy overhead.

Among the studies, three key cost drivers are essential for deployment: 
1.  Communication overhead, driven by update frequency, client participation, and

network constraints typical in IoT environments.

2.  Sensitivity to heterogeneity, reflecting robustness under non-IID data, variable

device capabilities, and uneven local sample sizes.

3.  Aggregation security, including resilience to poisoning, Sybil attacks, and

unreliable participants.

Ledger-Anchored Trust, Auditability, and Governance Support

In  regulated  payment  ecosystems,  privacy-preserving  detection  must  support 
auditability, governance, and dispute resolution. A blockchain-supported architecture 
meets these needs by providing immutability and verifiable event histories. As shown 
in Table 16 (A6, A18), ledger anchoring enhances trust and compliance by ensuring 
that transaction events, alerts, and model updates are tamper-evident.

However,  these  advantages  come  with  increased  coordination  overhead  and 
potential  delays  in  confirmation.  Therefore,  when  evaluating  blockchain-enabled 
contributions  within  the  performance  framework,  it  is  crucial  to  consider  not  only 
detection  metrics  but  also  factors  such  as  throughput  feasibility,  audit  latency,  and 
governance maturity, especially when evidentiary trails are necessary.

---

<!-- PAGE 47 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Permissioned versus permissionless blockchain designs

The  studies  under  review  implicitly  assume  various  blockchain  models  without 
consistently  distinguishing  their  operational  implications.  Permissioned  blockchains, 
typically  managed by recognised financial institutions or consortium  members, offer 
reduced  consensus  latency,  predictable  performance,  and  enhanced  access  control, 
making them more suitable for real-time card-not-present (CNP) fraud governance than 
public  blockchains.  In  contrast,  permissionless  blockchains  provide  greater 
decentralisation  but  come  with  increased  latency,  variable  throughput,  and  higher 
energy  and  communication  overheads,  which  may  conflict  with  the  requirements  of 
time-sensitive  transaction  authorisation.  This  distinction  is  crucial  for  evaluating  the 
feasibility of blockchain technology in IoT-enabled payment systems.

Latency mitigation strategies for real-time operations

Numerous  studies  have  proposed  or  adopted  strategies  to  mitigate  latency  and 
address the delays caused by blockchain technology. These strategies include off-chain 
or side-channel processing for time-sensitive fraud decisions, batching transaction logs 
rather than committing them for each event, and implementing lightweight consensus 
protocols  designed  explicitly  for  permissioned  environments.  Such  approaches 
effectively separate real-time detection from ledger finality, allowing fraud decisions to 
be executed at the edge or gateway while maintaining auditability through delayed or 
summarised on-chain commitments.

When blockchain adds value and when it does not

The synthesis indicates that integrating blockchain technology is most justified in 
multi-stakeholder CNP ecosystems, where auditability, cross-organisational trust, and 
non-repudiation are crucial. However, in environments with tightly controlled or single-
provider  deployments,  implementing  blockchain  may  introduce  unnecessary  latency 
and coordination overheads without commensurate benefits. In these cases, traditional 
secure logging  or  centralised trust  mechanisms  may  be  more  effective in addressing 
real-time constraints.

Explainability, Resilience, and Design Implications

A persistent challenge in distributed intelligence is maintaining stakeholder trust as 
models become more complex and decentralized. Two complementary strategies recur 
across the synthesis implied by Table 16:

  Robust aggregation and participant-aware defenses, aimed at mitigating

poisoning and Sybil behaviors in FL and FL-SL deployments.

  Provenance-aware auditing, where ledger-based records support traceability of

model versions, update sources, and decision contexts.

Explainability  is  most  effective  when  integrated  at  the  decision  point  using 
lightweight edge-side features and clearly linking decisions with model lineage. This 
balance is crucial for maintaining real-time responsiveness while ensuring compliance 
and facilitating post-hoc review.

Synthesis and Implications for IoT-Enabled CNP Fraud Detection

---

<!-- PAGE 48 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

The evidence indicates that distributed learning and privacy-preserving intelligence 
are valuable for scalable fraud detection in IoT-enabled CNP environments, but only 
when  their  coordination  costs  remain  within  the  bounds  of  time-sensitive  payment 
workflows.  Federated  and  split  learning  reduce  raw-data  exposure  and  support 
decentralized collaboration, yet their value depends on whether communication burden, 
synchronization  stability,  and  heterogeneous  participation  remain  operationally 
manageable. Likewise, blockchain-supported governance strengthens auditability and 
traceability, but only when its latency and overhead remain compatible with real-time 
authorization  requirements.  Overall,  these  findings  suggest  that  privacy-preserving 
collaboration  and  blockchain-supported  governance  should  be  assessed  in  terms  of 
responsiveness,  scalability,  and  coordination  costs  rather  than  as  isolated  design 
benefits.

4.6 Design principles for efficient, adaptive, and resilient IoT-driven fraud-detection 
frameworks

The  analysis  of  application  scenarios,  performance  evaluation  methods,  and 
distributed privacy-preserving models demonstrates that effective fraud detection for 
CNP transactions driven by the Internet of Things (IoT) cannot rely solely on isolated 
algorithm  improvements.  Instead,  practical  systems  must  adhere  to  clear  design 
principles  that  balance  real-time  operational  constraints,  diverse  IoT  environments, 
evolving fraud patterns, and regulatory trust requirements. This section outlines these 
principles based on the reviewed evidence and provides actionable guidance for system-
level implementation.

Principle 1: Scenario-Aware Performance Optimization

A  recurring  finding  across  Sections 4.3  and  4.4  is  that  performance  is  inherently 
context  dependent.  Detection  accuracy,  latency,  scalability,  and  trust  metrics  vary 
substantially  across  e-commerce  gateways,  edge-assisted  payments,  federated 
monitoring, and blockchain-supported environments. Consequently, IoT-driven fraud 
detection  frameworks should be designed with explicit scenario awareness, ensuring 
that optimization targets align with the intended deployment context.

For  example,  centralized  gateway  scenarios  prioritize  classification  effectiveness 
under high transaction throughput, whereas edge-assisted and mobile payments demand 
strict  latency  and  energy  constraints.  Distributed  and  federated  scenarios  introduce 
additional  coordination  costs  and  increased  sensitivity  to  heterogeneity,  while 
blockchain-supported systems emphasize auditability and governance. Treating these 
contexts uniformly leads to misleading optimization and brittle designs. Scenario-aware 
optimization,  therefore,  emerges  as  a  foundational  principle  for  efficient  IoT-CNP 
systems.

Principle 2: Real-Time Responsiveness as a First-Class Design Objective

The  performance  review  highlights  that  many  frameworks  emphasize  predictive 
effectiveness while under-specifying real-time behavior, even when claiming near-real-
time  operation.  In  CNP  fraud  detection,  delayed  responses  can  undermine  detection 
accuracy  by  allowing  fraudulent  transactions  to  proceed.  As  such,  real-time 
responsiveness  must  be  treated  as  a  first-class  design  objective,  not  a  secondary 
consideration.

---

<!-- PAGE 49 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Designs should explicitly account for end-to-end decision latency, event processing 
rate, and model update intervals, particularly in edge-assisted and streaming scenarios. 
Architectural strategies such as edge-level inference, lightweight models, and adaptive 
decision pipelines support this objective, but must be evaluated under realistic workload 
assumptions.  Embedding  responsiveness  into  system  design  directly  enhances 
operational readiness and resilience.

Principle 3: Distributed and Privacy-Preserving Intelligence by Design

The findings presented in Section 4.4 show that privacy preservation and scalability 
are interconnected with modern IoT-enabled payment systems. Regulatory constraints, 
institutional boundaries, and competitive factors hinder centralized data aggregation, 
necessitating the adoption of distributed learning approaches, such as federated and split 
learning.

The design of effective frameworks is intricately linked to the integration of privacy-
preserving  intelligence,  emphasizing  the  preservation  of  sensitive  transactional  and 
behavioral data at the local level. This approach not only safeguards individual privacy 
but also enables collaborative enhancements to the model, thereby fostering innovation. 
It is crucial to understand that privacy should not be regarded as a dichotomous trait; 
rather,  a  nuanced  design  is  necessary  to  achieve  a  harmonious  equilibrium  among 
several critical factors. These include the effectiveness of detection mechanisms, the 
impact of communication overhead, the capacity to withstand heterogeneity, and the 
ability to resist adversarial threats. Such a balanced framework enhances scalability and 
trustworthiness,  making  it  suitable  for  broad  deployment  across  diverse  stakeholder 
environments. This paradigm shift towards a multifaceted understanding of privacy is 
essential for the sustainable advancement of collaborative technological ecosystems.

Principle 4: Adaptive Learning under Non-Stationarity and Heterogeneity

CNP fraud patterns change rapidly due to evolving attacker strategies, varying user 
behaviors, and platform-specific dynamics. The challenge is further intensified in IoT 
environments,  which  involve  non-stationary  data  streams  and  diverse  device 
capabilities.  Studies  indicate  that  static  models  and  fixed  thresholds  become  less 
effective over time, compromising long-term performance.

To address this issue, adaptive learning mechanisms are crucial. Techniques such as 
online  updates,  incremental  training,  and  heterogeneity-aware  aggregation  must  be 
implemented.  Frameworks  should  be  designed  to  manage  concept  drift,  client 
variability, and partial participation without negatively impacting system performance. 
In this context, adaptivity goes beyond  model updates; it also encompasses dynamic 
resource allocation and decision-making policies, thereby enhancing resilience against 
evolving threats.

Principle 5: Resilience to Adversarial and System-Level Failures

In addition to accuracy and scalability, effective IoT-driven fraud detection systems 
must  withstand  adversarial  manipulation  and  operational  disruptions.  Distributed 
learning introduces various attack vectors, such as data poisoning, Sybil attacks, and 
unreliable  participants.  Deployments  on  edge  and  IoT  devices  also  face  challenges, 
including device failures, intermittent connectivity, and resource exhaustion.

---

<!-- PAGE 50 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

To achieve resilience, these systems require multi-layered defenses, including strong 
aggregation  strategies,  participant  validation,  redundancy  across  IoT  layers,  and  the 
ability  to  maintain  functionality  during  partial  system  failures.  By  designing  for 
resilience, we can ensure that detection capabilities remain effective even in adverse 
conditions, which is essential for financial transaction systems.

Principle 6: Integrated Trust, Governance, and Auditability

The  synthesis  highlights  that  fraud  detection  in  CNP  environments  is  not  just  a 
technical challenge; it is part of a socio-technical system that operates within regulatory 
and  governance  frameworks.  Trustworthiness  encompasses  more  than  just  detection 
outcomes; it also includes explainability, accountability, and compliance.

Frameworks  should  integrate  governance  mechanisms,  such  as  audit  trails, 
provenance tracking, and controls aligned with compliance standards, into the detection 
process.  Designs  supported  by  blockchain  technology  exemplify  one  method  for 
achieving immutable auditability. However, governance can also be enhanced through 
standardized  logging  and  transparent  decision  reporting.  By  incorporating  trust  and 
governance during the design phase, we can improve transparency and facilitate post-
incident analysis, dispute resolution, and regulatory acceptance.

Synthesis and Transition to Unified Framework Design

These design principles collectively highlight that an efficient, adaptive, and resilient 
IoT-driven CNP fraud detection system requires a holistic approach. Key elements such 
as  scenario  awareness,  real-time  responsiveness,  privacy-preserving  distribution, 
adaptability, resilience, and governance should be co-designed rather than optimized in 
isolation.

These principles are directly applied in the unified multi-layer IoT-CNP framework 
outlined in Section 4.7. In this framework, architectural layers, data flows, and decision-
making  mechanisms  are  integrated  to  implement  the  insights  gathered  from  the 
reviewed literature.

4.7 Unified Multi-Layer Framework Formulation and Convergence Synthesis

Building on the scenario analysis, performance evaluation framework, distributed 
and privacy-preserving intelligence models, and the design principles distilled from the 
reviewed  literature,  this  section  formulates  a  unified  multi-layer  IoT-CNP  fraud 
detection  framework.  The  proposed  framework  integrates  diverse  architectural 
paradigms  into  a  coherent  reference  architecture  for  real-time  detection,  scalability, 
adaptability, privacy preservation, and trustworthiness in card-not-present transaction 
environments.

Rather  than  proposing  a  new  detection  algorithm,  this  contribution  focuses  on 
architectural convergence. It integrates IoT sensing, secure communication, edge/fog 
intelligence,  cloud-based  coordination,  distributed 
learning,  decision-response 
mechanisms, and governance controls into a layered framework aligned with the CNP 
transaction  lifecycle.  This  approach  addresses  the  fragmentation  observed  in  the 
reviewed studies and provides a structured reference model for future IoT-enabled CNP 
fraud detection systems.

To  ground  the  framework  in  the  reviewed  evidence,  the  included  studies  were 
aligned with the layers they primarily addressed. Studies on IoT sensing and contextual

---

<!-- PAGE 51 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

data acquisition mainly contribute to the perception and device layers. Studies focused 
on gateway, edge, and fog-based detection align with the edge-fog processing layer. 
Centralized  analytics,  federated  learning,  split  learning,  and  large-scale  behavioral 
profiling contribute to the cloud analytics and coordination layer. Governance-oriented 
studies, including those addressing blockchain, compliance, auditability, and trust, span 
the Security, Privacy, and Governance Layer and interact with multiple technical layers. 
This  mapping  demonstrates  that  the  proposed  framework  consolidates  existing 
contributions  into  an  end-to-end  architecture  rather  than  presenting  an  abstract 
conceptual model detached from the reviewed literature.

Rationale for a Unified Multi-Layer Architecture

The synthesis of the reviewed literature shows that no single architectural paradigm, 
centralized cloud analytics, edge-centric processing, federated learning, split learning, 
or  blockchain-supported  governance,  can  independently  satisfy  the  full  range  of 
operational,  performance,  privacy,  and  regulatory  requirements  associated  with  real-
time  CNP  fraud  detection.  Centralized  cloud  architectures  provide  high  analytical 
capacity and support large-scale model training, but they are frequently constrained by 
latency, data sovereignty, privacy exposure, and reliance on continuous connectivity. 
Conversely, edge-centric architectures reduce response time by processing fraud signals 
closer to the transaction source, but they may face limitations in computational capacity, 
global coordination, model consistency, and long-term scalability.

Distributed learning approaches such as federated learning and split learning reduce 
the need to centralize sensitive payment and device data, but they introduce additional 
challenges related to communication overhead, client heterogeneity, synchronization, 
convergence stability, and trust management. Similarly, blockchain-based governance 
can  improve  auditability,  provenance,  and  transaction  accountability,  but  standalone 
blockchain  solutions  are  generally  unsuitable  as  primary  real-time  fraud  detection 
mechanisms when placed directly in the transaction authorization path because of their 
potential computational and communication overhead.

These limitations indicate that IoT-enabled CNP fraud detection is best understood 
as  a  system-of-systems  problem.  It  requires  coordinated  intelligence  across  multiple 
functional  layers  rather  than  dependence  on  a  single  computational  or  governance 
model.  The  reviewed  studies  collectively  suggest  that  real-time  responsiveness, 
analytical  depth,  privacy  preservation,  scalability,  auditability,  and  regulatory 
compliance  must  be  balanced  through  architectural  decomposition  and  functional 
specialization.

Accordingly,  the  proposed  framework  adopts  a  unified  six-layer  IoT-CNP 
architecture that assigns complementary and clearly delineated roles to the components 
of the payment ecosystem. This architecture extends earlier conceptual classifications 
by  explicitly  separating  data  capture,  secure  transmission,  real-time  edge  inference, 
cloud-based coordination, governance, and decision-response functions. In doing so, it 
reflects  deployment  practices  observed  across  edge-fog-cloud  systems,  where 
transaction-time inference, model coordination, and audit functions are not executed in 
the same layer or at the same speed.

The six layers of the proposed architecture, illustrated in Fig. 5, are described below. 
The Perception/Device Layer captures transaction context and telemetry from web, 
mobile,  and  IoT-enabled  payment  environments.  It  collects  device  and  browser

---

<!-- PAGE 52 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

fingerprints,  geolocation  signals,  behavioral  patterns,  transaction  metadata,  session 
characteristics,  and  other  contextual  indicators  generated  during  CNP  transaction 
initiation.  This  layer  provides  the  raw  contextual  foundation  for  downstream  fraud 
detection.

The Network/Communication Layer supports secure and efficient transmission of 
enriched transaction features across the payment ecosystem. It relies on secure transport 
protocols,  encrypted  communication  channels,  and  event-streaming  mechanisms  to 
route time-sensitive transaction signals while preserving confidentiality, integrity, and 
responsiveness.

The Edge-Fog Processing Layer performs low-latency fraud screening close to the 
transaction source. Its primary role is to execute lightweight anomaly scoring, device 
fingerprint  verification,  contextual  risk  assessment,  and  immediate  escalation  of 
suspicious transactions during the authorization window. Because CNP decisions often 
need  to  be  made  within  milliseconds,  this  layer  supports  real-time  or  near-real-time 
inference using locally cached models, recent risk indicators, predefined thresholds, and 
policy rules. By locating initial detection functions near the data source, the edge-fog 
layer  reduces  round-trip  communication  delays  and  avoids  overdependence  on 
centralized infrastructure during live authorization.

The Cloud Analytics and Coordination Layer provides high-compute analytical 
capacity and global fraud intelligence. Unlike the edge-fog layer, the cloud layer is not 
primarily  responsible  for  millisecond-level  transaction  decisions.  Instead, it supports 
historical  pattern  mining,  large-scale  model  retraining,  cross-channel  behavioral 
profiling,  federated  model  aggregation,  split-learning  coordination,  global  risk 
intelligence, and long-term risk analysis. Cloud-based analytics improve model quality, 
adaptability, and system-wide visibility, while edge/fog inference preserves transaction-
time responsiveness.

A central feature of the architecture is the deliberate separation between edge/fog 
detection  and cloud-based  analytics.  Edge/fog  detection prioritizes speed,  proximity, 
and  immediate  action.  It  is  most  suitable  for  transaction-time  screening,  where  the 
system must quickly determine whether a payment should proceed, be challenged, be 
temporarily  held,  or  be  escalated.  Cloud-based  detection  and  coordination  prioritize 
analytical  depth,  historical  learning,  cross-institutional  intelligence,  and  model 
refinement.  They  are  best  suited  for  identifying  emerging  fraud  patterns,  retraining 
models, aggregating federated updates, and improving detection capabilities over time. 
Synchronization  between  the  edge/fog  and  cloud  layers  is  handled  through 
asynchronous model-update and feedback loops rather than synchronous transaction-
time dependency. During live payment authorization, the edge/fog layer does not wait 
for  full  cloud-side  retraining,  federated  aggregation,  split-learning  coordination,  or 
blockchain confirmation. Instead, it relies on locally available models, cached policy 
rules, recent risk intelligence, and predefined thresholds to generate immediate fraud 
scores. After the transaction, relevant outcomes, confirmed fraud labels, false-positive 
feedback, drift indicators,  client-side  model updates,  and  model-performance  signals 
are transmitted to the cloud layer. The cloud layer then aggregates these signals, updates 
global models or policies, and redistributes refined model parameters, decision rules, or 
risk indicators back to edge and fog nodes. This asynchronous design preserves low-
latency  transaction-time  decision-making  while  enabling  the  system  to  continuously 
learn from broader fraud patterns.

---

<!-- PAGE 53 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

The  Security,  Privacy,  and  Governance  Layer  provides  mechanisms  for 
accountability, compliance, provenance, secure coordination, privacy protection, and 
post-event  review  across  stakeholders.  In  the  proposed  architecture,  blockchain  is 
positioned as a governance and audit-support mechanism rather than as the core real-
time fraud classifier. This layer may support permissioned or consortium-based audit 
trails,  smart-contract-based  policy  enforcement,  model-update  logging,  dispute 
evidence, and settlement-related traceability. By separating governance from immediate 
transaction scoring, the architecture avoids the latency burden that would arise if every 
live authorization decision depended on direct on-chain validation.

Consistent with the blockchain trade-offs identified in the reviewed literature, this 
layer  is  best  implemented  through  permissioned,  private,  or  consortium-based 
blockchain  mechanisms  rather  than  public-chain  validation.  In  this  configuration, 
trusted  payment  stakeholders  such  as  issuers,  acquirers,  processors,  regulators, 
merchants,  and  fraud-monitoring  entities  may  participate  in  controlled  ledger 
governance. Blockchain anchoring is therefore used to support auditability, provenance, 
model-update  logging,  dispute  evidence,  settlement-related  traceability,  and  policy 
accountability without requiring live CNP authorization decisions to wait for public-
chain confirmation.

The Application and Decision-Response Layer translates fraud scores, contextual 
risk  signals,  policy  rules,  and  governance  indicators  into  operational  actions.  These 
actions may include transaction approval, step-up authentication, temporary blocking, 
manual  review,  customer  notification,  fraud  analyst  escalation,  or  post-transaction 
monitoring.  This  layer  ensures  that  analytical  outputs  are  translated  into  timely, 
proportionate  fraud-control  decisions  while  supporting  explainable  reporting  for 
relevant stakeholders.

The proposed framework  reflects three major  synthesis  outcomes.  First,  effective 
IoT-enabled CNP fraud detection depends on cross-layer interaction rather than isolated 
model performance. Second, privacy-preserving intelligence, edge-cloud coordination, 
and governance mechanisms are integral to deployment viability rather than optional 
extensions.  Third,  future  systems  should  be  benchmarked  not  only  by  classification 
accuracy,  but  also  by 
throughput,  scalability,  synchronization  cost, 
communication overhead, privacy preservation, auditability, and operational resilience.

latency,

Fig. 5 Unified Multi-Layer IoT Fraud Detection Framework

---

<!-- PAGE 54 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

By  distributing  responsibilities  across  these  six  layers,  the  proposed  architecture 
mitigates the limitations of isolated approaches while enabling scalable, privacy-aware, 
low-latency, and auditable fraud detection. The layered design reflects the empirical 
evidence  synthesized  from  the  literature  and  provides  a  coherent  foundation  for 
implementing  adaptive,  trustworthy  CNP  fraud-detection  systems  in  IoT-enabled 
payment environments.

---

<!-- PAGE 55 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Cross-Layer Convergence and Data Flow 
The effectiveness of the proposed framework arises from cross-layer convergence 
rather than from isolated functions. As illustrated in Fig. 5, transactional and contextual 
data flow upward from the perception layer through the communication and edge-fog 
processing  layers,  enabling  real-time  risk  assessment.  At  the  same  time,  decisions, 
alerts, model updates, policy adjustments, and governance signals move downward and 
laterally across layers.

Short feedback loops between the Perception/Device, Network/Communication, and 
Edge-Fog  Processing  Layers  enable  immediate  fraud  detection  while  meeting  strict 
latency  requirements.  Longer  feedback  cycles  involving  the  Cloud  Analytics  and 
Coordination Layer and the Security, Privacy, and Governance Layer support strategic 
adaptation, global learning, model refinement, and regulatory compliance. Governance 
metadata, such as decision provenance, policy enforcement records, model update logs, 
and audit events, enhances explainability and traceability without impeding real-time 
execution.

This convergence ensures that detection effectiveness, latency, scalability, privacy, 
and trust are optimized collectively rather than independently. It also operationalizes 
the multi-dimensional performance framework established in Section 4.4 by showing 
how different performance dimensions are associated with different architectural layers.

Alignment with Research Questions and Design Principles

The unified architecture directly operationalizes the study’s research questions. 
For RQ1, the layered structure clarifies where performance metrics apply, enabling 
scenario-aware comparison across gateway, edge-assisted, federated, and blockchain-
supported contexts. For RQ2, federated learning and split learning within the edge-fog 
and  cloud  coordination  layers  enable  scalable  collaboration  without  centralizing 
sensitive  data.  For  RQ3,  real-time  responsiveness,  adaptivity,  resilience,  privacy 
preservation,  and  governance  are  embedded  as  structural  design  requirements  rather 
than  treated  as  post  hoc  additions.  For  RQ4,  integrating  all  six  layers  provides  a 
synthesis-derived  reference  model  for  trustworthy,  real-time  IoT-driven  CNP  fraud 
detection.

This explicit mapping distinguishes the proposed framework from prior works that 
address only isolated components of the fraud detection pipeline. It also demonstrates 
how  the  design  principles  identified  in  Section  4.6  are  translated  into  deployable 
architectural logic.

Implementation Considerations and Extensibility

The proposed framework is technology-agnostic and can be adopted incrementally. 
Organizations may implement specific layers depending on their operational maturity, 
regulatory requirements, technical infrastructure, and risk tolerance. For instance, real-
time  edge  scoring  can  be  deployed  independently  from  blockchain  anchoring,  while 
federated learning or split learning can be introduced gradually as cross-institutional 
collaboration develops.

The  architecture  is  intentionally  extensible.  It  allows  integration  of  emerging 
technologies such as explainable AI, secure enclaves, trusted execution environments, 
adaptive graph analytics, privacy-preserving computation, post-quantum cryptographic 
controls,  and  adaptive  policy  engines  without  requiring  structural  redesign.  This

---

<!-- PAGE 56 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

flexibility  ensures  that  the  framework  remains  relevant  within  the  rapidly  evolving 
payment and IoT ecosystems.

Operationalising governance and privacy across layers

In  the  proposed  framework,  governance  and  privacy  are  treated  as  operational 
functions embedded across the architecture rather than as isolated components. Privacy 
enforcement  begins  at  the  sensing  layer  through  data  minimisation  and  contextual 
feature abstraction. It continues at the edge through secure feature processing and at the 
coordination layer through privacy-preserving learning mechanisms such as federated 
learning and split learning. Governance mechanisms, including audit logging, access 
control, policy enforcement, provenance tracking, and compliance reporting, interact 
with all layers to ensure accountability while avoiding direct interference with time-
critical detection workflows.

This layered operationalisation clarifies how trust and privacy requirements can be 
enforced  without  compromising  real-time  performance.  It  also  reinforces  the  role  of 
governance as a cross-cutting capability rather than a separate, optional module.

Unified multi-layer IoT–CNP reference framework

Fig.  6  illustrates  the  integrated  data  flows  originating  from  IoT  sensing  and 
transaction sources, moving through edge-level detection and cloud-based coordinated 
analysis.  It  also  depicts  the  learning  loops  that  support  model  updates  through 
centralized, federated, or split-learning paradigms. Governance feedback mechanisms 
are  represented  as  orthogonal  controls,  ensuring  policy  enforcement,  auditability, 
traceability, and compliance without being confined to a single architectural layer.

Fig. 6 Unified multi-layer IoT–CNP reference framework illustrating data flows, 
learning loops, and governance interaction

---

<!-- PAGE 57 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Illustrative Deployment Scenario of the IoT-CNP Fraud Detection Architecture

To  demonstrate  how  the  proposed  architecture  can  operate  in  practice,  a

representative IoT-enabled card-not-present transaction scenario is described below.

1.  Transaction Generation: Perception/Device Layer

A  consumer  initiates  an  online  payment  using  a  connected  device  such  as  a 
smartphone,  wearable  device,  smart  appliance,  or  browser-enabled  platform. 
Transaction  and  contextual  signals,  including  device  fingerprint,  session 
metadata,  location  indicators,  behavioral  interaction  patterns,  and  transaction 
attributes, are generated at the point of initiation.

2.  Secure Data Transmission: Network/Communication Layer

The  transaction  request  and  associated  contextual  features  are  transmitted 
through  secure  communication  channels  to  the  relevant  gateway,  edge,  or 
payment-processing  infrastructure.  Encryption,  secure  transport  protocols,  and 
event-streaming mechanisms preserve confidentiality and responsiveness.

3.  Edge-Level Fraud Screening: Edge-Fog Processing Layer

At  the  edge  or  fog  node,  lightweight  anomaly  detection  models  perform 
preliminary inference. These models evaluate contextual features such as device 
identity,  abnormal  behavioral  patterns,  and  unusual  transaction  frequency,  as 
well  as  risk thresholds.  Suspicious  transactions  can be  flagged,  challenged,  or 
escalated immediately with minimal latency.

4.  Advanced Fraud Analytics: Cloud Analytics and Coordination Layer

Aggregated  insights  from  multiple  edge  and  fog  nodes  are  transmitted  to  the 
cloud  analytics  layer.  This  layer  performs  deeper  model  retraining,  historical 
analysis, behavioral profiling, federated aggregation, cross-channel intelligence 
generation,  and  long-term  model  governance.  Cloud-side  processing improves 
future detection performance without interrupting live transaction authorization.

5.  Decision and Response: Application and Decision-Response Layer

Based  on  the  computed  fraud  risk  score  and  applicable  policy  rules,  the 
application  layer  determines  whether  to  approve  the  transaction,  request 
additional authentication, temporarily hold the transaction, decline it, or escalate 
it  for  manual  review.  Where  appropriate,  explainable  outputs  are  provided  to 
support fraud analysts, customer communication, and dispute resolution.  
6.  Governance and Compliance: Security, Privacy, and Governance Layer

The Security, Privacy, and Governance Layer enforces security policies, privacy 
controls,  audit  logging,  model-update  traceability,  and  regulatory  compliance. 
Permissioned  or  consortium-based  ledger  anchoring  may  be  used  to  record 
selected  control  events  and  provenance  metadata,  supporting  accountability 
without  imposing  on-chain  confirmation  delays  on  the  real-time  authorization 
pathway.

Contribution of the Validation Scenario

The illustrative scenario demonstrates that the proposed framework can support real-
time fraud detection in distributed IoT payment environments by combining device-
level  contextual  intelligence,  secure  feature  transmission,  edge-based  anomaly 
detection,  cloud-scale  fraud  analytics,  privacy-preserving  learning,  and  governance-
aware compliance mechanisms.

---

<!-- PAGE 58 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

The proposed IoT-CNP framework should therefore be interpreted as a synthesis-
derived  reference  architecture  rather  than  as  an  experimentally  validated  fraud-
detection  system.  Its  purpose  is  to  integrate  fragmented  evidence  across  sensing, 
communication, analytics, distributed learning, decision support, and governance into a 
coherent  deployment-oriented  model.  In  this  review,  the  framework  functions  as  a 
reference  synthesis  and  benchmarking  guide  rather 
than  as  a  prescriptive 
implementation claim.

5. Discussion

5.1  Interpreting  the  Landscape  of  IoT-Based  CNP  Fraud  Detection  Frameworks 
(RQ1)

The synthesis of frameworks in Section 4.2 reveals a fragmented, siloed research 
landscape, in which IoT-enabled CNP fraud detection solutions are typically proposed 
as  isolated  models  or  architectures  that  address  narrow  technical  objectives.  While 
many studies demonstrate strong predictive performance in specific settings, relatively 
few examine how detection logic integrates across IoT layers or adapts to heterogeneous 
operational environments.

From an analytical standpoint, this fragmentation limits systematic benchmarking 
and obscures broader design trade-offs. Most reviewed studies implicitly address RQ1 
by  reporting  detection  performance,  yet  they  often  underrepresent  system-level 
considerations  such  as  scalability,  governance,  and  real-time  deployment.  This 
imbalance underscores the need to move beyond algorithm-centric comparisons toward 
ecosystem-level  synthesis,  in  which  frameworks  are  evaluated  based  on  their 
architectural placement, application context, and operational constraints.

5.2 Implications of Application Scenarios and Case-Study Contexts

The  scenario  taxonomy  introduced  in  Section  4.3  demonstrates  that  CNP  fraud 
detection is inherently context dependent. Gateway-centric e-commerce environments 
emphasize  low-latency  decisioning  and  high  precision.  In  contrast,  edge-assisted 
mobile  and  IoT  payment  scenarios  introduce  additional  challenges  related  to  device 
heterogeneity,  energy  efficiency,  and  intermittent  connectivity.  Distributed  and 
federated  monitoring  scenarios  further  shift  attention  toward  coordination  costs  and 
privacy preservation, while blockchain-supported scenarios foreground auditability and 
compliance.

A key implication is that performance claims divorced from application context have 
limited practical meaning. High accuracy reported under centralized assumptions may 
not translate to latency-sensitive edge deployments, just as privacy-preserving federated 
frameworks  may  incur  coordination  overheads  unsuitable  for  specific  real-time 
that  meaningful 
scenarios.  These  findings  reinforce  RQ1  by  demonstrating 
benchmarking must be scenario-aware, aligning evaluation metrics with the operational 
realities of each deployment context.

5.3 Performance Evaluation Practices and Benchmarking Implications

The performance evaluation synthesis in Section 4.4 highlights a persistent emphasis 
on predictive effectiveness metrics, often at the expense of real-time responsiveness, 
scalability,  and  trust-related  indicators.  While  accuracy-centric  reporting  remains

---

<!-- PAGE 59 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

three  critical

these  findings  reveals

valuable, it provides an incomplete picture of system readiness in IoT-enabled payment 
environments. 
Interpreting

insights.  First,  real-time 
responsiveness is inconsistently reported, even in studies claiming real-time capability, 
limiting the validation of deployment feasibility. Second, scalability must be treated as 
a  system-level  property,  encompassing  not  only  computational  efficiency  but  also 
communication  overhead,  coordination  complexity,  and  robustness  to  non-IID  data. 
Third, trust and privacy are increasingly central performance dimensions, particularly 
in regulated financial contexts, yet they are rarely quantified in a standardized manner. 
These observations address RQ1 by identifying benchmarking gaps and inform RQ3 
by  motivating  a  multi-dimensional  performance  evaluation  paradigm,  where 
effectiveness,  latency,  scalability,  and  trust  are  co-evaluated  rather  than  considered 
independently.

5.4 Distributed Learning and Privacy-Preserving Intelligence in Practice

The  analysis  in  Section  4.5  shows  that  distributed  intelligence  can  strengthen 
scalability, privacy preservation, and institutional interoperability in IoT-enabled CNP 
fraud detection.  However, its value  is  contingent on  whether  coordination overhead, 
client  heterogeneity,  aggregation  stability,  and  governance  costs  remain  compatible 
with real-time payment requirements. This indicates that distributed learning should be 
evaluated not only as a privacy  mechanism, but  as a deployment-dependent systems 
choice. These insights directly address RQ2, demonstrating that distributed intelligence 
enhances  scalability  and  trustworthiness  when  privacy,  coordination  cost,  and 
governance are treated as first-class design considerations.

5.5 Design Principles as System-Level Guidance

The  design  principles  articulated  in  Section  4.6  serve  to  translate  empirical 
observations into actionable guidance at the system level. These principles, scenario 
awareness, real-time responsiveness, adaptivity, resilience, and governance integration, 
should not be viewed as isolated optimization goals but rather as elements that shape an 
interdependent design space.

The  discourse  emphasizes  the  need  to  co-optimize  these  principles.  For  instance, 
relocating inference to the edge enhances responsiveness; it also requires implementing 
complementary resilience and governance mechanisms to address potential adversarial 
risks. Likewise, adopting privacy-preserving learning techniques enhances compliance; 
however,  this  advancement  requires  meticulous  management  of  communication 
efficiency and fault tolerance.

By  characterizing  these  principles  as  architectural  constraints  rather  than  mere 
optional features, the study advances RQ3. It lays a structured foundation for the design 
of IoT-driven CNP fraud detection systems capable of sustained operation in real-world 
environments.

5.6 Interpreting the Unified Multi-Layer IoT-CNP Framework

The  unified  multi-layer  framework  in  Section  4.7  should  be  understood  as  a 
reference synthesis rather than a prescriptive implementation blueprint. Its contribution 
lies  in  integrating  sensing,  communication,  analytics,  distributed  learning,  decision-
making,  and  governance  into  a  coherent  architectural  model  aligned  with  the  CNP

---

<!-- PAGE 60 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

transaction  lifecycle.  This  integrated  view  provides  a  practical  basis  for  future 
benchmarking and system design across diverse CNP payment environments.

5.7 Synthesis, Research Implications, and Limitations

Synthesis of Findings

The  synthesis  reveals  a  fragmented  research  landscape  in  which  most  studies 
prioritize predictive accuracy while underreporting deployment factors such as latency, 
communication  overhead,  and  governance  mechanisms.  Scenario-based  analysis 
further  shows  that  performance  claims  are  context-dependent  and  that  privacy-
preserving approaches often introduce  trade-offs in coordination and scalability. The 
unified IoT-CNP framework consolidates these findings into an architectural reference 
model aligned with the CNP transaction lifecycle.

Research Implications

From  a  research  perspective,  the  findings  indicate  a  shift  from  model-centric 
evaluation  toward  system-level  benchmarking  for  IoT-enabled  CNP  fraud  detection. 
Future studies should therefore report not only predictive effectiveness, but also real-
time  responsiveness,  scalability,  communication  cost,  and  trust-related  deployment 
constraints.  Scenario-aware  design  remains  essential, since  frameworks that perform 
well  in  centralized  e-commerce  settings  may  not  remain  suitable  in  edge-assisted, 
federated,  or  blockchain-supported  environments.  Security  evaluation  also  requires 
broader treatment than predictive performance alone, particularly in collaborative and 
distributed  settings  where  adversarial  resilience  and  governance-aware  trust  become 
central concerns.

Limitations

Several  limitations  should  be  acknowledged.  First,  the  study  is  constrained  by 
inconsistent reporting practices in the literature, particularly regarding latency budgets, 
dataset characteristics, and deployment assumptions. Second, industrial and proprietary 
fraud-detection  systems  remain  underrepresented  due  to  limited  public  disclosure, 
potentially biasing the evidence base toward academic prototypes. Third, although the 
proposed unified framework is analytically grounded in the reviewed literature, it has 
not been empirically validated within the scope of this systematic review. While proof-
of-concept  implementation  would  strengthen  external  validity,  the  present  study  is 
intended to provide a review-derived reference architecture and benchmarking agenda 
for subsequent simulation, prototyping, and operational validation.

5.8 Aligning IoT layers with the Card-Not-Present (CNP) transaction lifecycle

The CNP transaction lifecycle is a multi-stage socio-technical process in which fraud 
risk emerges dynamically across four phases: interaction, transmission, decision, and 
settlement. As illustrated in Fig. 7, effective fraud mitigation occurs when the Internet 
of Things (IoT) architectural layers are explicitly aligned with these transaction stages. 
This  alignment  enables  contextual  intelligence,  real-time  responsiveness,  and  post-
event accountability without disrupting the payment flow.

During the transaction initiation phase, the merchant's web or mobile interface acts 
as the primary sensing point. In addition to traditional elements outlined in ISO 8583

---

<!-- PAGE 61 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

and PCI, such as anonymized Primary Account Numbers (PAN), transaction amounts, 
merchant  IDs,  and  category  codes,  IoT-style  telemetry,  including  device  identifiers, 
operating system and browser fingerprints, IP addresses, and geolocation cues, enriches 
the behavioral context of the transaction.

Normalizing

these  heterogeneous  signals

feature 
representations  is  critical  for  preserving  privacy  and  enabling  efficient  downstream 
processing.  This  approach  represents  a  broader  shift  from  raw  data  transmission  to 
context-aware  feature  exchange,  consistent  with  the  privacy-preserving  design 
principles articulated in Section 4.5.

into  compact,  signed

During network transmission, edge and fog infrastructures serve as intermediaries 
between  merchant  environments  and  payment  processors.  Secure  protocols,  such  as 
TLS  or  QUIC,  ensure  data  confidentiality.  Additionally,  edge-level  queuing  and 
prioritization  enable the differentiated  handling  of high-risk  transactions.  This phase 
demonstrates  how  IoT  networking  capabilities  enable  event-driven  responsiveness, 
enabling model refresh triggers or contextual alerts to be issued without interrupting 
authorization flows. From a systems perspective, this reinforces the edge layer's role as 
both a performance accelerator and a coordination hub.

The processing and decision phase corresponds to the analytics layer of the unified 
framework.  In  this  phase,  real-time  fraud  scoring  is  performed,  often  within  strict 
latency budgets (typically within tens of milliseconds), using edge-resident or hybrid 
inference engines. It is important to note that federated and graph-aware risk models are 
particularly well-suited for  this stage, as they exploit relational dependencies among 
cards, devices, merchants, and network attributes while maintaining data locality. This 
alignment  operationalizes  the  convergence  of  AI  and  IoT,  demonstrating  how 
distributed intelligence can achieve both responsiveness and privacy.

After  conducting  a  risk  assessment,  the  application  and  response  stage  converts 
analytical  results  into  actionable  decisions.  Fraud  scores,  confidence  indicators,  and 
clear explanations are communicated to merchants or processors to help them decide 
whether to approve transactions, implement additional authentication steps, or decline 
them. From a governance perspective, readily available decision rationales are crucial 
for  effective  customer  communication,  dispute  management,  and  regulatory 
compliance.  This  highlights  the  importance  of  incorporating  explainability  into  the 
application layer from the outset rather than adding it later.

The  security  and  governance  layer  encompasses  the  entire  transaction  lifecycle, 
capturing  vital  events,  device  statuses,  and  decision-related  data  for  audit  and 
compliance purposes. By anchoring select control events in lightweight, ledger-based 
records,  we  enhance  integrity  and  traceability  without  introducing  delays  associated 
with  consensus.  This  strategic  application  of  blockchain  technology  exemplifies 
scenario-driven convergence: governance is strengthened where necessary, while real-
time  performance  is preserved.  Following  this,  authorization  and  settlement  proceed 
through  established  acquiring  and  issuing  workflows,  effectively  completing  the 
transaction process.

This  lifecycle-oriented  perspective  reframes  CNP  fraud  detection  as  an  ongoing, 
multi-layered control process rather than a single-point classification task. By aligning 
IoT  layers  with  transaction  stages,  the  unified  framework  ensures  reliable  context 
capture  from  devices,  efficient  transmission  of  features,  quick  and  understandable 
decision-making, and a clear audit trail of outcomes. This alignment directly supports

---

<!-- PAGE 62 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

RQ4 by demonstrating how a unified multi-layer IoT framework can improve real-time 
fraud detection and prevention across the entire CNP transaction process. Additionally, 
it  reinforces  RQ3  by  emphasizing  the  importance  of  lifecycle  alignment  as  a 
fundamental design principle for resilient deployment.

Fig. 7 CNP Transaction Process aligned with IoT ecosystem

Source: [33]

5.9 Regulatory and Compliance Implications for IoT-Enabled CNP Fraud Detection 
The  deployment  of  IoT-enabled  CNP  fraud  detection  systems  functions  within  a 
stringent financial and data-protection framework. Regulations such as the European 
Union’s  General  Data  Protection  Regulation  (GDPR)  and  the  Revised  Payment 
Services  Directive  (PSD2)  impose  strict  requirements  on  data  minimisation, 
transparency, user consent, and accountability. The reviewed frameworks indicate that 
centralised, data-heavy detection models may clash with GDPR principles, especially 
those concerning data locality and purpose limitation. In contrast, federated and split 
learning  approaches  align  more  naturally  with  regulatory  expectations  by  enabling 
collaborative  intelligence  without  direct  data-sharing.  Similarly,  PSD2’s  strong 
customer authentication (SCA) and transaction monitoring requirements underscore the 
need  for  low-latency,  explainable,  and  auditable  fraud  detection  mechanisms, 
particularly in IoT-enabled payment environments.

Blockchain-supported  governance  frameworks  further  strengthen  compliance  by 
providing immutable audit trails and verifiable decision provenance, both of which are 
crucial  for  post-incident  investigations  and  regulatory  reporting.  However,  their 
integration must be carefully designed to avoid introducing latency that could disrupt

---

<!-- PAGE 63 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

real-time  authorisation  flows.  Regulatory  compliance  emerges  not  as  an  external 
constraint but as a key architectural driver shaping the adoption of distributed learning, 
edge intelligence, and governance-aware IoT-CNP fraud detection systems.

6. Conclusion and Future Work

6.1 Conclusion

This study offers a systematic review of the IoT ecosystem for real-time CNP fraud 
detection,  synthesizing  findings  from  23  peer-reviewed  studies.  By  structuring  the 
analysis  around  application  scenarios,  performance  evaluation  methodologies, 
distributed intelligence, privacy preservation, and system-level design principles, this 
review  advances  beyond  algorithm-centric  comparisons,  providing  a  holistic 
understanding of deployable IoT-driven fraud detection frameworks.

In addressing RQ1, the review illustrates that current IoT-based CNP fraud detection 
frameworks cannot be  effectively benchmarked without explicit consideration of the 
contextual application and operational constraints. Although detection accuracy is the 
most frequently reported metric, it is inadequate when considered in isolation. Scenario-
aware  benchmarking  that  encompasses  latency,  scalability,  energy  efficiency,  and 
governance requirements are essential for establishing valid cross-study comparisons. 
Regarding  RQ2,  the  analysis  demonstrates  that  distributed,  privacy-preserving 
intelligence,  particularly  through  federated  and  split  learning,  is  fundamental  to 
achieving  scalable,  trustworthy  CNP  fraud  detection.  These  methodologies  facilitate 
collaborative learning across institutional boundaries while preserving data locality and 
ensuring  regulatory  compliance.  However,  their  practical  effectiveness  depends  on 
design choices that are sensitive to coordination, including communication efficiency, 
robustness 
to  non-IID  data  distributions,  and  resilience  against  adversarial 
manipulation.

In response to RQ3, the study distills a coherent set of system-level design principles 
that  underpin  efficient,  adaptive,  and  resilient  IoT-driven  fraud  detection  systems. 
These  principles,  scenario-aware  optimization,  real-time  responsiveness,  privacy-by-
design distribution, adaptive learning under non-stationarity, resilience to adversarial 
and  systemic  failures,  and  integrated  governance,  translate  empirical  findings  into 
actionable  guidance  for  the  transition  from  research  prototypes  to  operational 
deployments.

Finally, addressing RQ4, the paper proposes a unified multi-layer IoT-CNP fraud 
detection  framework  that  integrates  sensing,  edge  intelligence,  analytics,  distributed 
learning, and governance mechanisms throughout the CNP transaction lifecycle. Rather 
than  introducing  a  novel  detection  algorithm,  this  framework  offers  a  reference 
architecture that reconciles performance, privacy, scalability, and trust within a single 
coherent  system  model.  This  contribution,  oriented  toward  convergence,  seeks  to 
mitigate the fragmentation observed in prior studies and lays a structured foundation for 
future research and practical implementation.

6.2 Future Works

Despite growing interest in distributed, privacy-preserving learning, several research 
challenges remain unresolved in the scalable IoT-enabled CNP fraud detection domain. 
There  is an urgent need for coordination-efficient learning protocols that can reduce

---

<!-- PAGE 64 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

communication and synchronization costs while maintaining detection accuracy under 
strict  latency  constraints.  Current  evaluation  frameworks  do  not  adequately  address 
scalability issues, especially considering device heterogeneity in computational power, 
energy  capacity,  and  network  reliability.  Additionally,  understanding  convergence 
guarantees  in  non-IID  and  streaming  transaction  data  within  real-time  payment 
scenarios is limited. There is also a lack of standardized benchmarks and workloads to 
comprehensively  assess  accuracy, 
latency,  communication  costs,  and  energy 
consumption at scale. Addressing these challenges is essential to advance federated and 
split  learning  from  theoretical  potential  to  practical  deployment  in  large-scale  IoT 
payment  systems.  To  improve  IoT-enabled  CNP  fraud  detection,  researchers  should 
focus on several key areas.

First,  developing  standardized,  scenario-aware  performance  metrics  is  crucial—
particularly  for  real-time  responsiveness,  federated  scalability  costs,  and  governance 
indicators. Longitudinal studies simulating realistic transaction volumes and evolving 
fraud patterns would further strengthen empirical validation.

Second,  there  is  a  significant  need  for  thorough  empirical  validation  of  unified, 
multi-layer  architectures  in  real-world  settings  or  large-scale  pilots.  While  existing 
studies often evaluate individual components separately, future research should analyze 
end-to-end  system  performance  across  sensing,  analytics,  learning,  and  governance 
layers, including failure modes, recovery processes, and operational trade-offs.

Third,

integrating  explainable  artificial

intelligence  and  human-in-the-loop 
mechanisms  into  IoT-driven  CNP  fraud  detection  remains  underexplored.  Providing 
interpretable,  context-aware  explanations  at  critical  decision  points  is  vital  for 
regulatory compliance, customer trust, and operational oversight.

Fourth, recent advances in secure computation, trusted execution environments, and 
post-quantum  cryptography  offer  promising  pathways  to  enhance  privacy  and  trust. 
Exploring systematic incorporation of these technologies into federated and blockchain-
based architectures is an important future direction.

Fifth,  expanding  analysis  to  cross-border  payment  ecosystems,  emerging  digital 
currencies, and decentralized finance platforms will help evaluate the adaptability and 
scalability of IoT-enabled CNP fraud detection in evolving financial landscapes. Future 
research should go beyond accuracy testing and systematically examine coordination 
latency,  communication  costs,  and  energy  use  under  realistic  transaction  loads. 
Furthermore,  assessing  blockchain-enabled  CNP  systems  should  differentiate 
governance  benefits  from  performance  costs,  considering  both  permissioned  and 
permissionless designs.

Emerging technologies such as quantum computing and generative AI are also likely 
to influence  future  IoT-CNP  fraud detection  architectures.  Quantum  computing  may 
signatures,  blockchain 
weaken  conventional  public-key  encryption,  digital 
cryptography, and secure payment authentication, making post-quantum cryptographic 
readiness  an  important  research  priority.  Future  systems  should  therefore  examine 
quantum-resistant  digital  signatures,  post-quantum  key-exchange  mechanisms,  and 
migration  pathways  for  payment  and  blockchain  infrastructure.  Generative  AI  also 
introduces both defensive and adversarial implications. Defensively, generative models 
can  support  synthetic  fraud-pattern  generation,  rare  attack  simulation,  privacy-
preserving data augmentation, and adversarial stress testing, especially where labelled 
real-world  CNP  fraud  data  are  scarce.  However,  generative  AI  may  also  strengthen

---

<!-- PAGE 65 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

attacker  capabilities  by  enabling  synthetic  identities,  automated  phishing,  credential 
harvesting, adversarial transaction simulation, and adaptive social-engineering attacks. 
Future research should therefore evaluate generative AI both as a tool for improving 
model robustness and as a risk factor within IoT-enabled payment ecosystems.

including

assessment,

simulation-based

Future research should evaluate the proposed reference architecture through staged 
validation, 
testbed 
implementation, and pilot deployment under realistic payment authorization, privacy, 
jointly  assess  detection 
and  compliance  constraints.  Such  validation  should 
effectiveness,  end-to-end  latency,  throughput,  communication and  coordination  cost, 
privacy overhead, adversarial resilience, data-poisoning robustness, secure aggregation 
reliability, and cross-layer trust assurance. Without this broader validation, apparently 
strong  fraud-detection  performance  may  not  translate  into  dependable  real-world 
operation.

prototype

or

References

1.  Alatawi, M. N. (2025). Detection of fraud in IoT-based credit card collected 
datasets using machine learning. Machine Learning with Applications, 19, 
100603. https://doi.org/10.1016/j.mlwa.2024.100603

2.  Bhutta, M. N. M., Bhatia, S., Alojail, M. A., Khan, M. T. R., & Ahmad, A. 
(2022). Towards secure IoT-based payments by extending the Payment Card 
Industry Data Security Standard (PCI DSS). Wireless Communications and 
Mobile Computing, 2022, Article 9942270. 
https://doi.org/10.1155/2022/9942270

3.  Liu, C., Xiao, Y., Javangula, V., Hu, Q., Wang, S., & Cheng, X. (2019). 
NormaChain: A blockchain-based normalized autonomous transaction 
settlement system for IoT-based e-commerce. IEEE Internet of Things Journal, 
6(3), 4680–4693. https://ieeexplore.ieee.org/abstract/document/8502858

4.  Gupta, S., & Kumar, V. (2024). Integrating deep learning, machine learning, 
artificial intelligence, IoT, and data science for future innovations. Proceedings 
of the IEEE International Conference on Emerging Technologies. IEEE. 
https://ieeexplore.ieee.org/document/10917415

5.  Yasaei, R., Moghaddas, Y., Abdullah, M., & Faruque, A. (2024). IoT-

GRAF: IoT graph learning-based anomaly and intrusion detection through 
multimodal data fusion. IEEE Internet of Things Journal. Advance online 
publication. https://ieeexplore.ieee.org/document/10546572

6.  Deshmukh, A., de la Rosa, P. E., Rodriguez, R. V., & Dasari, S. (2025).

Enhancing privacy in IoT-enabled digital infrastructure: Evaluating federated 
learning for intrusion and fraud detection. Sensors, 25(10), 3043. 
https://doi.org/10.3390/s25103043

7.  Rguibi, A., Asimi, Y., Asimi, A., & Oumouss, L. (2024). Privacy-preserving 
anomaly detection for IoT: Leveraging federated and split learning. IEEE 
Access, 12, 75081–75095. https://doi.org/10.1109/ACCESS.2024.3456781 
8.  Zhang, Y., Suleiman, B., Alibasa, M. J., & Farid, F. (2024). Privacy-aware 
anomaly detection in IoT environments using FedGroup: A group-based

---

<!-- PAGE 66 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

federated learning approach. Journal of Network and Systems Management. 
Advance online publication. https://doi.org/10.1007/s10922-023-09782-9

9.  Khan, A. A., Alsufyani, A., Alsufyani, N., et al. (2025). BAML: A

decentralized approach to secure, privacy-preserving financial compliance 
using blockchain Hyperledger and federated learning. Peer-to-Peer Networking 
and Applications, 18, 270. https://doi.org/10.1007/s12083-025-02086-6

10. Khan, A. A., Ghodhbani, R., Alsufyani, A., Alsufyani, N., & Mohamed, M. 
A. (2025). Leveraging blockchain-integrated explainable artificial intelligence 
for ethical and personalized healthcare decision-making. The Journal of 
Supercomputing, 81(15), 1353-1372.   https://doi.org/10.1007/s11227-025-
07844-0

11. Khan, A. A., Laghari, A. A., Almansour, H., Jamel, L., Hajjej, F., Estrela,

V. V., & Ullah, S. (2025). Quantum computing empowering blockchain 
technology with post-quantum resistant cryptography for multimedia data 
privacy preservation. Journal of Cloud Computing, 14(1), 43. 
https://doi.org/10.1186/s13677-025-00771-8

12. Bhattacharyya, S., Jha, S., Tharakunnel, K., & Westland, J. C. (2011). Data 
mining for credit card fraud: A comparative study. Decision Support Systems, 
50(3), 602–613. https://doi.org/10.1016/j.dss.2010.08.008

13. Dal Pozzolo, A., Boracchi, G., Caelen, O., Alippi, C., & Bontempi, G.

(2018). Credit card fraud detection: A realistic modeling and a new publicly 
available dataset. IEEE Transactions on Neural Networks and Learning 
Systems, 29(8), 3784–3797. https://doi.org/10.1109/TNNLS.2017.2736643 
14. Carcillo, F., Dal Pozzolo, A., Le Borgne, Y. A., Caelen, O., Mazzer, Y., & 
Bontempi, G. (2018). Scarff: A scalable framework for streaming credit card 
fraud detection with Spark. Information Fusion, 41, 182–194. 
https://doi.org/10.1016/j.inffus.2017.09.005

15. Yang, Y., Wu, L., Yin, G., Li, L., & Zhao, H. (2017). A survey on security

and privacy issues in Internet of Things. IEEE Internet of Things Journal, 4(5), 
1250–1258. https://doi.org/10.1109/JIOT.2017.2694844

16. Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. (2021). The PRISMA

2020 statement: An updated guideline for reporting systematic reviews. BMJ, 
372, n71. https://doi.org/10.1136/bmj.n71

17. Schardt, C., Adams, M. B., Owens, T., Keitz, S., & Fontelo, P. (2007).

Utilization of the PICO framework to improve searching PubMed for clinical 
questions. BMC Medical Informatics and Decision Making, 7, 16. 
https://doi.org/10.1186/1472-6947-7-16

18. Devi, R. A., Sabitha, B., Raffik, R., & Akila, K. (2023). IoT device security 
for smart-card fraud detection for credit cards. In Proceedings of the 2nd 
International Conference on Advancements in Electrical, Electronics, 
Communication, Computing and Automation (ICAECA 2023) (pp. 1–6). IEEE. 
https://doi.org/10.1109/ICAECA56562.2023.10199738

19. Kumar, P., Kumar, R., Gupta, G. P., & Tripathi, R. (2021). A distributed

framework for detecting DDoS attacks in smart contract-based blockchain–IoT 
systems using fog computing. Transactions on Emerging Telecommunications 
Technologies, 32(12), e4112. https://doi.org/10.1002/ett.4112

---

<!-- PAGE 67 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

20. Garg, A., Pandey, M., & Pathak, A. R. (2024). A multi-layered AI–IoT

framework for adaptive financial services. International Journal of Emerging 
Technologies in Computer Science and Information Technology. 
https://doi.org/10.63282/3050-9246.IJETCSIT-V5I3P105

21. Benameur, R., Dahane, A., Souihi, S., & Mellouk, A. (2024). A novel

federated learning-based intrusion detection system for IoT networks. IEEE 
Internet of Things Journal. Advance online publication. 
https://ieeexplore.ieee.org/document/10622538

22. Rehman, A., Awan, K. A., Al-Rasheed, A., Ara, A., Alruwaili, F. F., Al-
Otaibi, S., & Saba, T. (2025). A hybrid fuzzy logic and federated learning 
framework for cybersecurity and fraud detection in IoT-enabled metaverse 
transactions. Engineering Intelligence Journal. 
https://doi.org/10.1016/j.eij.2025.100668

23. Vankayalapati, R. K., Syed, S., Jayalakshmi, S., Mandala, G., Yadav, O. P., 
& Yadav, A. K. (2025). A robust and scalable deep learning framework for 
real-time IoT intrusion detection with adaptive energy efficiency and 
adversarial resilience. SSRN Electronic Journal. 
https://doi.org/10.2139/ssrn.5077791

24. Prakash, V., Odedina, O., Kumar, A., Garg, L., & Bawa, S. (2024). A

secure framework for Internet of Things anomalies using machine learning. 
Discover Artificial Intelligence. https://doi.org/10.1007/s43926-024-00088-z 
25. Goyal, H. R., Husain, S. O., Dixit, K. K., Boob, N. S., Reddy, B. R., Kumar, 
J., & Sharma, S. (2024). Advanced deep learning approaches for real-time 
anomaly detection in IoT environments. IEEE Sensors Journal. 
https://ieeexplore.ieee.org/document/10829306

26. Choi, D., & Lee, K. (2018). An artificial intelligence approach to financial 
fraud detection under IoT environments. Journal of Sensors, 2018, Article 
5483472. https://doi.org/10.1155/2018/5483472

27. Subhalaxmi, A., Kishorekumar, V., Leela Prasad, V., Deekshitha, G. A. V.,

& Varma, S. L. S. (2023). Credit card fraud detection using multi-layer 
perceptron based on federated learning. International Journal for Research 
Trends and Innovation, 8(6), 552–556. 
https://www.ijrti.org/papers/IJRTI2306087.pdf

28. Min, M., Lee, J. J., Park, H., & Lee, K. (2021). Detecting anomalous

transactions via an IoT-based application: A machine learning approach. 
Sensors, 21(6), 2039. https://doi.org/10.3390/s21062039

29. Abubakar, A., Ali, M. H., & Darma, T. H. (2024). Digital twin and IoT-
enabled online learning model for real-time monitoring and control of 
fraudulent transactions in banking. Kabul Journal of Computer Science, 1(3), 1–
12. https://doi.org/10.47514/kjcs/2024.1.3.0018

30. Murthy, V. S. N., Kumari, R., Goyal, M., Dubey, P., & Ramesh, P. (2024).

Edge AI in IoT: Leveraging cloud computing and big data for intelligent 
decision-making. Journal of Information Systems Engineering and 
Management, 10(20S). https://doi.org/10.52783/jisem.v10i20s.3194

31. Kafila, H., Mohammad, H., Veena, C., Singla, A., Joshi, A., & Lourens, M. 
(2024). Fraud detection in IoT-based financial transactions using anomaly

---

<!-- PAGE 68 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

detection techniques. IEEE International Conference on Smart Computing. 
https://ieeexplore.ieee.org/document/10602423

32. Maddukuri, N. (2022). Real-time fraud detection using IoT and AI: Securing 
the digital wallet. Journal of Computing and Emerging Technologies, 5(1), 8. 
https://doi.org/10.34218/JCET_5_01_008

33. Owusu-Mensah, K., Yaokumah, W., & Ansong, E. D. (2025). A

comprehensive review of techniques for detecting and preventing card-not-
present (CNP) fraud. In Innovations in Cryptocrime and Financial Fraud (pp. 
283–314). IGI Global. https://doi.org/10.4018/979-8-3373-0675-9.ch008

Declarations

Acknowledgement: Fig. 1 and Fig. 6 were created using AI-generated content from 
ChatGPT  (OpenAI).  The  authors  confirm  that  no  human  likenesses,  copyrighted 
elements, or misleading representations are included in the image.

Fig. 5 was created by the authors using a combination of ChatGPT(OpenAI)-assisted 
conceptual design, Mermaid syntax for structured architectural modeling, and Draw.io 
for visual refinement and layout optimization. All architectural interpretations, design 
decisions, and final visual representations are the authors’ own.

Funding Statement: Not applicable

Author  Contributions:  Kwabena  Owusu-Mensah:  Conceptualization;  methodology; 
formal analysis;  thematic analysis and synthesis; writing  – original manuscript text; 
prepared  all  figures  and  tables.  Edward  Danso  Ansong,  Kofi  Sarpong  Adu-Manu, 
Winfred  Yaokumah:  Supervision;  validation;  review  and  editing;  methodological 
guidance; final approval of the manuscript. All authors reviewed the manuscript.

Ethics Approval: Not applicable

Conflicts of Interest: The authors declare no conflicts of interest related to the present 
study.

Consent to Participate: Not applicable

Consent to Publish: Not applicable

Clinical Trial Number: Not applicable

Availability of Data and Materials: not applicable

Code Availability: Not applicable

---

<!-- PAGE 69 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Acronyms

AI - Artificial Intelligence 
AS - Article Studies 
CNN - Convolutional Neural Network 
CNP - Card-Not-Present 
DDoS - Distributed Denial-of-Service 
DL - Deep Learning 
DP - Differential Privacy 
ETT - Emerging Telecommunications Technologies 
FedAvg - Federated Averaging 
FedGAT-DCNN - Federated Graph Attention Network-Dilated Convolution Neural 
Network 
FedGroup - Federated Learning Grouping Framework 
FedOpt - Federated Optimization 
FedProx - Federated Proximal 
FGCS - Future Generation Computer Systems 
FL - Federated Learning 
GANs – Generative Adversarial Networks 
GNN – Graph Neural Network 
IDS – Intrusion Detection System 
IIoT – Industrial Internet of Things 
IoT – Internet of Things 
IPFS – InterPlanetary File System 
JNSM - Journal of Network and Systems Management 
LSTM – Long Short-Term Memory 
ML – Machine Learning 
MLP – Multi-Layer Perceptron 
NFC – Near Field Communication 
Non-IID – Non-independent and non-identically distributed 
NSL-KDD – Network Security Laboratory–Knowledge Discovery in Databases 
PCI DSS – Payment Card Industry Data Security Standard 
QUIC  –  Quick UDP Internet Connections, a transport-layer protocol designed to 
support low-latency, secure communication 
RF – Random Forest 
RFID – Radio Frequency Identification 
RNN – Recurrent Neural Network 
SMOTE – Synthetic Minority Oversampling Technique 
UNSW-NB15  –  University  of  New  South  Wales-Network-Based  Intrusion 
Detection Dataset 
XAI – Explainable Artificial Intelligence 
XGBoost – Extreme Gradient Boosting

Key Words and Terms

Adaptive Learning - Techniques that enable models to dynamically adjust to new 
data and evolving conditions.

---

<!-- PAGE 70 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Anomaly Detection - Methods identifying data patterns significantly deviating from 
typical or expected behaviors. 
Auditability - Ability of a system to maintain traceable and verifiable records for 
regulatory and compliance purposes. 
Behavioral  Biometrics  -  User  authentication  based  on  unique  behavioral 
characteristics such as typing patterns, gestures, or mouse movements. 
Behavioral Profiling - Analysis and characterization of user activities to identify 
and predict potentially fraudulent behaviors. 
Blockchain - Decentralized, distributed ledger technology ensuring data integrity, 
transparency, immutability, and security. 
Cloud  Computing  -  Remote  delivery  and  management  of  computing  services 
(servers, storage, analytics) over the internet. 
Concept Drift - Changes over time in the underlying distribution or characteristics 
of data, impacting model performance. 
Context-Awareness  -  Ability  of  systems  to  interpret  and  react  appropriately  to 
environmental or situational contexts in real-time. 
Data Privacy - Protection of personal and sensitive data against unauthorized access 
or misuse. 
Decentralization  -  Distribution  of  control  and  decision-making  from  a  central 
authority to multiple dispersed nodes or entities. 
Deep Learning - Advanced subset of machine learning involving neural networks 
with multiple layers for complex data analysis. 
Digital  Twin  -  Virtual  representation  of  physical  systems  used  for  real-time 
simulation, monitoring, and analysis. 
Edge Computing - Distributed computing approach where data processing occurs 
at or near the source, reducing latency. 
Edge Intelligence - Deployment of intelligent computation models directly on edge 
devices for immediate processing and decision-making. 
Explainable AI (XAI) - Techniques that ensure artificial intelligence decisions are 
understandable and transparent to users. 
Federated Averaging (FedAvg) - A widely used algorithm in federated learning, 
designed  for  training  machine  learning  models  across  decentralized  data  sources 
without directly sharing the data. 
Federated  Learning  -  Machine  learning  paradigm  enabling  decentralized  model 
training across distributed devices while preserving data privacy. 
Federated  Proximal  (FedProx)  -  refers  to  the  combination  of  two  concepts  in 
machine learning: Federated Learning (FL) and proximal optimization. 
FedGAT-DCNN  -  employs  federated  learning,  allowing  financial  institutions  to 
collaboratively train models using local datasets, enhancing accuracy and robustness 
while maintaining data privacy. 
Flower Framework - an open-source software framework for building federated 
AI systems, including federated learning, analytics, and evaluation 
Fog Computing - Distributed computing architecture positioned closer to end-user 
devices, bridging cloud computing and edge computing. 
Fuzzy  Logic  -  Reasoning  methodology  handling  uncertainty  and  approximate 
reasoning rather than precise binary decisions.

---

<!-- PAGE 71 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Hybrid Models - Frameworks integrating multiple modeling methodologies (e.g., 
federated learning, fuzzy logic) to enhance predictive capabilities. 
Interoperability  -  Capability  of  disparate  systems  and  devices  to  effectively 
exchange and use information. 
Latency  -  Time  delay  between  initiating  an  action  and  observing  its  effect  or 
response. 
Lightweight Models - Computationally efficient models optimized for performance 
on devices with limited processing power and memory. 
Multi-Layered  Framework  -  Architectural  approach  involving  multiple  layers 
(e.g.,  perception,  processing,  application,  governance) 
to  enhance  system 
functionality and security. 
Multi-Modal  Data  -  Data  derived  from  multiple  distinct  sources  or  types  (e.g., 
biometric, transactional, behavioral). 
Non-IID - datasets where individual data points are not independent and identically 
distributed. This means the data points do not all  come from the same underlying 
probability  distribution,  and  there  may  be  dependencies  or  correlations  between 
them. 
Oversampling - Technique addressing dataset imbalance by increasing instances of 
underrepresented classes to improve model training. 
Privacy-Preserving  Techniques  -  Approaches  ensuring  sensitive  data  remains 
confidential and secure during data processing and analysis. 
Real-Time Detection - Immediate analysis and response to data as it is generated or 
observed. 
Real-time  detection  systems  –  systems  capable  of  performing  fraud  evaluation 
during  the  transaction  authorization  process.  These  systems  typically  rely  on 
streaming analytics, edge inference, or low-latency machine learning models. 
Near real-time detection systems – systems that analyze transactions shortly after 
they  occur,  usually  within  seconds  or  minutes,  and  are  used  to  trigger  alerts, 
additional authentication, or transaction reversal mechanisms. 
Regulatory  Compliance  -  Adherence  of  systems  and  processes  to  established 
standards, laws, and regulations, such as PCI DSS. 
Resource-Constrained Devices - Devices with limited computational capabilities, 
storage, and power supply. 
Scalability  -  Capacity  of  a  system  to  efficiently  manage  increased  workloads  or 
expanded operational scopes without performance degradation. 
Secure  Aggregation  -  Technique  for  securely  combining  model  updates  or  data 
inputs without compromising individual data privacy. 
Smart  Contract  -  Self-executing  contracts  with  encoded  business  logic  on 
blockchain, automating enforcement and verification processes.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Discover Internet of Things
https://doi.org/10.1007/s43926-026-00358-y
Article in Press
Systematic review of the internet of things
ecosystem for real-time detection of card-not-
present (CNP) fraud
Received: 4 August 2025 Kwabena Owusu-Mensah, Edward Danso Ansong, Kofi Sarpong Adu-Manu & Winfred
Accepted: 11 May 2026 Yaokumah
S
We are providing an unedited version of this manuscript to give early access to its
Cite this article as: Owusu-Mensah K., S
findings. Before final publication, the manuscript will undergo further editing. Please
Ansong E.D., Adu-Manu K.S. et al.
E
note there may be errors present which affect the content, and all legal disclaimers
Systematic review of the internet of
R
things ecosystem for real-time detection apply.
P
of card-not-present (CNP) fraud. Discov
If this paper is publishi ng under a Transparent Peer Review model then Peer
Internet Things (2026). https://doi. N
Review reports will publish with the final article.
org/10.1007/s43926-026-00358-y
I
E
L
C
I
T
R
A
© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do
not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Review
Systematic Review of the Internet of Things Ecosystem for Real-Time Detection of
Card-Not-Present (CNP) Fraud
Kwabena Owusu-Mensah1, Edward Danso Ansong2, Kofi Sarpong Adu-Manu3,
Winfred Yaokumah4
1234Department of Computer Science, University of Ghana, Legon-Accra, Ghana
Corresponding Author: Kwabena Owusu-MSensah. Email: kowusu-
S
mensah001@st.ug.edu.gh
E
R
P
N
Abstract:
I
The rapid rise in card-not-presen t (CNP) transactions has increased fraud risks in
E
digital commerce, highlightinLg the limitations of traditional fraud detection methods.
C
The integration of Internet of Things (IoT) technologies introduces contextual data that
I
can enhance real-timTe, context-aware fraud detection. However, it also presents
R
challenges related to scalability, latency, privacy, and governance. This study
A
systematically reviews IoT-enabled frameworks for real-time CNP fraud detection,
synthesizing evidence from 23 peer-reviewed articles identified through a literature
search covering the period 2015 to April 3, 2026, following the PRISMA 2020
guidelines. The analysis categorizes existing frameworks based on application
scenarios, IoT architectural layers, performance evaluation, and distributed
intelligence, revealing system-level trends and identifying research gaps. While many
studies emphasize predictive effectiveness, performance reports mainly rely on
accuracy metrics, often overlooking essential factors such as real-time responsiveness
and privacy. Notably, federated and split learning are highlighted as significant
enablers of scalable, privacy-preserving collaboration, although their coordination
and communication trade-offs are often not quantified. Moreover, blockchain
mechanisms can enhance auditability but require careful integration to address
potential latency issues. This study provides several key contributions: (i) it introduces
a scenario-aware synthesis that links IoT architectural placement with fraud detection
requirements and evaluation practices; (ii) it provides explicit guidance for
benchmarking that goes beyond accuracy to encompass latency,
scalability/coordination cost, and privacy/trust indicators; and (iii) it presents a unified
multi-layer IoT-CNP reference architecture that aligns with the CNP transaction
lifecycle. Rather than proposing a new detection algorithm, this review enhances

ACCAERPTTICEDLE M IANN PURSECSRSIPT
system-level integration and deployment readiness by consolidating fragmented
evidence into a practical architecture and metrics blueprint for detecting real-time IoT-
enabled payment fraud.
Keywords: Card-not-present fraud; Internet of Things (IoT); real-time fraud detection;
federated learning; privacy-preserving analytics; blockchain-enabled governance;
payment security, fraud analytics
1. Introduction
1.1 Background and Motivation
The rapid expansion of digital commerce and remote payment platforms has led to
a substantial increase in card-not-present (CNP) transactions, making CNP fraud one of
the most persistent and costly threats to contemporary financial systems. Unlike card-
present transactions, CNP payments lack physical authentication mechanisms, thereby
increasing exposure to identity theft, account takeover, and transaction manipulation in
online and mobile payment environments [1,2]. Conventional fraud detection systems,
largely centralized and batch-oriented, are increasiSngly challenged by the scale,
velocity, and real-time decision requirements of moSdern digital payment ecosystems.
E
In parallel, the Internet of Things (IoT) has become an integral component of
R
emerging payment infrastructures, enabliPng smart point-of-sale terminals, mobile
payment devices, connected consumer Nplatforms, and machine-to-machine transactions
[3]. IoT-enabled environments facilIitate continuous data acquisition and distributed
E
analytics, enabling the detection of anomalous transaction patterns closer to the data
L
source and with reduced lCatency [4,5]. However, these environments also introduce
I
significant architecturTal and operational challenges, including heterogeneous data
streams, resource-cRonstrained edge devices, communication overhead, and heightened
A
privacy and regulatory concerns [6]. To ensure optimal effectiveness, CNP fraud
detection systems must carefully balance predictive accuracy with key operational
considerations, including latency, scalability, deployability, and compliance across
multiple layers of the Internet of Things (IoT). This necessitates a comprehensive,
integrative approach that addresses the complexities of contemporary digital
transactions while maintaining regulatory compliance and operational efficiency.
Recent research has explored machine learning and deep learning approaches for
credit card fraud detection using data collected from IoT-enabled systems, as well as
federated and privacy-preserving learning paradigms that mitigate the risks of
centralized data sharing [1,7,8]. At the same time, blockchain technology has
increasingly been investigated as a complementary trust layer for IoT-based digital
services, offering immutability, decentralization, and auditable transaction records.
Emerging studies demonstrate that blockchain’s effectiveness is further enhanced when
combined with artificial intelligence techniques, such as federated learning and
explainable AI, to support privacy-preserving, transparent, and regulation-aware
analytics in distributed financial systems [9,10]. Advances in blockchain security,
including post-quantum cryptography and secure cloud-enabled auditing, further
highlight its relevance for safeguarding sensitive transactional data against evolving
threat models [11].

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Despite these advances, the existing literature remains fragmented. Studies on fraud
detection, IoT security, blockchain-based trust mechanisms, and AI-driven analytics are
often conducted in isolation, and existing surveys typically focus either on centralized
fraud detection models or on generic IoT anomaly detection. As a result, there is a lack
of a consolidated understanding of how to jointly orchestrate IoT architectures,
blockchain-enabled trust, and AI-driven intelligence to support real-time CNP fraud
detection under practical deployment constraints. Moreover, performance assessment
metrics, datasets, and application scenarios are reported inconsistently, limiting cross-
study comparability and real-world adoption.
This study addresses existing limitations by presenting a systematic review of IoT-
enabled ecosystem-level frameworks for real-time CNP fraud detection. Unlike
previous surveys, this work explicitly integrates various IoT architectural layers,
including devices, communication networks, edge and fog computing, cloud analytics,
and governance mechanisms, with fraud detection models, performance assessment
metrics, and relevant application scenarios for digital payment systems. The review
introduces a layered IoT taxonomy specifically designed for CNP fraud detection and
synthesizes comparative evidence regarding detection effectiveness, latency,
scalability, and privacy preservation. It also identifies critical gaps between conceptual
proposals and deployable solutions. Recent advanceSments in blockchain-integrated
S
federated learning, explainable AI, and post-quantum security further underscore the
E
need for this ecosystem-level synthesis that aRccounts for decentralization, regulatory
P
compliance, and real-time performance in CNP transaction environments [8,9,11].
N
Existing reviews on payment fraud and IoT security predominantly focus on
I
algorithmic detection performanc e or general IoT anomaly/IDS settings, often
E
neglecting the integration oLf (a) IoT layer placement, (b) real-time operational
C
constraints such as end-to-end latency and throughput, (c) privacy-preserving
I
collaboration methodTs such as federated or split learning and their associated
R
coordination costs, and (d) governance and auditability mechanisms, including
A
blockchain, within a unified deployment framework. In contrast, this systematic review,
guided by the PRISMA methodology, synthesises IoT-enabled real-time CNP fraud
detection at the ecosystem level by integrating scenario taxonomy, multi-dimensional
benchmarking requirements, and a layered IoT-CNP reference architecture aligned with
the CNP transaction lifecycle.
For the purposes of this review, a framework was considered real-time or near real-
time -oriented if it was designed to support fraud detection within transaction
authorization windows, but it was considered empirically real-time-validated only when
the study reported operational metrics such as end-to-end latency, inference time,
throughput, update delay, or comparable timing-based evidence. Also, "Distributed
intelligence" signifies analytics and learning capabilities spread across IoT sensing,
edge, and coordination layers, rather than being restricted to a single centralised
processing entity.
1.2 Limitations of Existing CNP Fraud-Related Surveys and the Perspective of This
Review
Despite the growing body of literature on card-not-present (CNP) fraud detection,
existing surveys reveal several systematic limitations. Most previous reviews tend to
view CNP fraud primarily as a standalone machine learning classification problem,

ACCAERPTTICEDLE M IANN PURSECSRSIPT
emphasising algorithmic accuracy, precision-recall metrics, or class imbalance
management. This focus often comes at the expense of real-time operational constraints
such as end-to-end latency, deployment scalability, and system coordination overhead.
Consequently, critical questions regarding the performance of detection models
under realistic transaction throughput, diverse infrastructure conditions, and time-
sensitive payment authorisation workflows remain insufficiently explored.
Additionally, many surveys assume that data sources and computations are implicitly
centralised, overlooking the growing importance of distributed IoT-enabled
infrastructures, such as edge devices, contextual sensors, and real-time telemetry, which
now play a role in fraud signal generation and decision-making in modern payment
ecosystems.
Moreover, existing CNP fraud surveys rarely adopt governance-aware perspectives.
While privacy, compliance, and trust are often acknowledged as high-level concerns,
they are seldom analysed in relation to specific system mechanisms, such as privacy-
preserving collaborative learning, auditability, or cross-organizational coordination
costs. Surveys focusing on federated learning, IoT security, or blockchain-based trust
frameworks typically address these topics in isolation and outside the specific
constraints of CNP payment lifecycles. Consequently, the literature lacks an integrated
synthesis that connects detection models, architecturalS placement, evaluation metrics,
S
and governance mechanisms within a single coherent deployment context.
E
This review addresses these gaps by synRthesizing evidence across IoT sensing,
P
edge/fog/cloud placement, distributed and privacy-preserving learning, and governance
N
mechanisms within a scenario-aware IoT-CNP reference architecture aligned with the
I
CNP transaction lifecycle. Rather than evaluating detection models in isolation, the
E
review integrates architecturaLl placement, benchmarking dimensions, and deployment
C
constraints within a single ecosystem-level framework.
I
T
R
1.3 Conceptual Foundations of IoT-Based Frameworks in Fraud Detection
A
IoT-based fraud detection frameworks combine pervasive sensing, distributed
computation, and intelligent decision-making for real-time analysis of transactional
data. Unlike traditional centralized systems, IoT approaches leverage multi-source data
across devices and networks to capture richer contextual information for fraud detection
[12,13].
Contextual intelligence for fraud detection combines transaction features, device
fingerprints, temporal patterns, and network signals. This data fusion enables IoT
systems to detect behavioral deviations indicating fraud, especially in CNP payments
without physical verification [14].
Another foundational concept is layered intelligence across the IoT stack. IoT-based
fraud detection frameworks are typically structured across multiple layers as shown in
Fig. 1, including the perception layer (data acquisition), network layer (data
transmission), processing layer (edge or cloud analytics), and application layer
(decision support and response). This layered organization enables flexible deployment
strategies, allowing detection logic to be distributed across edge, fog, and cloud
resources depending on latency, scalability, and resource constraints [15].
Fig. 1 IoT Ecosystem for Fraud Detection

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Real-time responsiveness constitutes a further conceptual pillar. In CNP fraud
detection, decisions must be made within millisecondSs to avoid transaction delays or
customer disruption. IoT-based frameworks, thSerefore, emphasize stream-based
E
processing and online learning, enabling models to adapt dynamically to evolving fraud
R
patterns and concept drift. This contrasts wPith traditional batch-oriented approaches,
which struggle to maintain effectivenesNs under rapidly changing threat landscapes [13].
Privacy-preserving intelligence isI vital in IoT ecosystems due to concerns about data
E
ownership and user trust. Federated and split learning enable collaborative model
L
training without centraliziCng sensitive data [6,15]. Blockchain technologies provide
I
immutable ledgers anTd decentralized trust mechanisms that enhance auditability in
fraud-detection worRkflows [3].
A
Resilience and adaptability are fundamental to IoT-based fraud detection
frameworks. As fraudulent behavior evolves in response to defenses, systems must
adapt while maintaining stability. IoT architectures enable resilience through layer
redundancy, reconfigurable detection logic, and model updates to maintain
effectiveness.[14].
Conceptual foundations like contextual intelligence, layered deployment, real-time
responsiveness, privacy preservation, and adaptive resilience underpin IoT-based CNP
fraud detection frameworks. These principles guide the development of unified multi-
layer frameworks for real-time fraud detection and prevention.
1.4 Objectives and Scope of the Study
This study provides a systematic synthesis of IoT-based frameworks related to real-
time CNP fraud detection, examining their performance, architectural trade-offs, and
deployment feasibility. The study consolidates fragmented research into an analytical
framework supporting evidence-based system design and evaluation.
Specifically, the study pursues the following objectives:
1. To synthesize existing IoT-based CNP fraud detection frameworks by organizing
them according to representative application scenarios, IoT deployment layers,

ACCAERPTTICEDLE M IANN PURSECSRSIPT
and architectural paradigms, thereby enabling structured comparison across
heterogeneous studies.
2. To identify and consolidate key performance benchmarks and evaluation
dimensions reported in the literature, such as detection effectiveness, real-time
responsiveness, scalability, privacy preservation, and governance, while
systematically exposing methodological inconsistencies and research gaps.
3. To examine the role of distributed and privacy-preserving intelligence, including
federated learning, split learning, and blockchain-enabled trust mechanisms, in
enhancing the scalability, trustworthiness, and regulatory alignment of IoT-based
CNP fraud detection systems.
4. To derive empirically grounded design principles that can guide the development
of efficient, adaptive, and resilient IoT-driven fraud detection frameworks, based
on observed trade-offs across application scenarios and performance dimensions.
5. To motivate and conceptualize a unified multi-layer IoT-CNP fraud detection
framework, integrating edge-level responsiveness, cloud-based intelligence,
distributed learning, and blockchain-supported governance, to support real-time
fraud detection and prevention in complex financial ecosystems.
The review evaluates various architectural frameworks, centralized, edge-based,
federated, and blockchain-supported, emphasizing Sthose that facilitate real-time
S
detection and prevention. Research on anomaly or intrusion detection applicable to CNP
E
fraud detection was considered. R
P
1.5 Research Contributions N
I
This study contributes to the un derstanding of IoT-enabled card-not-present (CNP)
E
fraud detection by integratinLg existing research areas, including credit card fraud
C
analytics and IoT anomaly detection, into a cohesive framework. It focuses on real-time
I
CNP fraud detection aTs a cross-layer issue in the IoT payment ecosystem. The main
R
contribution lies in offering a comprehensive synthesis that aligns architectural
A
considerations with operational constraints and fraud detection requirements.
First, the study provides an ecosystem-level review of IoT-enabled CNP fraud
detection. Instead of viewing fraud detection solely as a prediction task or IoT security
only through anomaly or intrusion detection, the review explores how sensing and
contextual data, communication infrastructure, edge and fog deployment, cloud
analytics, distributed learning, and governance controls collectively influence fraud
detection in digital payments. This approach broadens the focus from model
performance to the overall system factors that affect the operational viability of fraud
detection frameworks.
Second, the study develops a layered IoT-CNP analytical taxonomy tailored to fraud
detection architectures. By organizing the evidence across sensing and devices,
communication, edge/fog, cloud analytics, applications, governance, and security
layers, the review clarifies where detection logic is placed, how intelligence is
distributed, and the trade-offs across the architecture. This layered framing makes
visible several issues that are often treated only implicitly in the literature, particularly
the relationships among deployment location, response time, privacy exposure,
scalability, resilience, and compliance requirements.
Third, the review provides a scenario-aware comparative synthesis of the included
studies. Rather than viewing the literature as isolated papers, it compares frameworks

ACCAERPTTICEDLE M IANN PURSECSRSIPT
based on application scenario, architectural placement, learning paradigm, data context,
and evaluation practices. This approach reveals which methods are used, where they are
deployed, the assumptions behind their evaluation, and the performance metrics
measured. It also highlights ongoing methodological inconsistencies in the field,
including the use of diverse datasets, inconsistent reporting of latency and throughput,
overemphasis on accuracy metrics, and a limited focus on privacy and governance.
Fourth, the study makes an application-oriented contribution by mapping the
reviewed frameworks to representative CNP payment contexts, including e-commerce
transaction screening, edge-assisted mobile and IoT payments, distributed fraud
monitoring, and blockchain-supported auditing and settlement. This improves the
practical relevance of the review by distinguishing frameworks that appear
operationally plausible from those that remain largely conceptual. It also helps align the
literature with the real constraints of payment environments, where detection
effectiveness must be balanced against speed, trust, interoperability, and regulatory
accountability.
Fifth, the review consolidates evidence on distributed, privacy-preserving
intelligence for IoT-enabled fraud detection. It examines federated learning, split
learning, and blockchain-based trust mechanisms that support collaboration,
auditability, and privacy in financial ecosystems. RatheSr than viewing these as separate,
S
it positions them within broader fraud-detection workflows, highlighting trade-offs such
E
as communication overhead, coordination comRplexity, interpretability limitations, and
P
latency.
N
Sixth, the study identifies empirical, architectural, and deployment gaps that
I
continue to constrain the field. T hese include limited validation under real-world
E
conditions, inconsistent repLorting of operational metrics, limited cross-study
C
comparability, insufficient handling of heterogeneous IoT data, and fragmented
I
treatment of privacy, Tgovernance, and standardization issues. By making these gaps
R
explicit, the review provides a clearer agenda for advancing IoT-enabled fraud detection
A
research from promising conceptual prototypes to more rigorous, deployable
operational systems.
The manuscript concludes with a unified multi-layer IoT-CNP fraud detection
framework aligned with the CNP transaction lifecycle. Instead of proposing a new
detection algorithm, it integrates existing evidence into an architectural blueprint that
connects contextual sensing, edge responsiveness, cloud intelligence, collaboration, and
governance. This framework aims to aid future benchmarking, design, and
implementation by balancing detection performance with real-time responsiveness,
privacy, scalability, trust, and compliance.
Table 1 situates this review within the broader literature. While past reviews often
focus on specific areas like credit card fraud detection or IoT security, they rarely
connect these elements to real-time CNP payment systems. Moreover, they often
overlook crucial factors such as cross-layer architecture and governance needs. In
contrast, this review adopts an ecosystem-level perspective, incorporating scenario-
aware IoT deployment and a layered IoT-CNP reference architecture, thereby
addressing a significant gap in the literature.
Table 1: Positioning of this Review relative to prior surveys

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Review Type Typical Focus What is usually What this paper adds
missing
Credit card / Algorithm/model IoT-layer Scenario-aware, IoT-
CNP fraud performance; placement; end-to- layered synthesis and
surveys accuracy/F1 end latency; edge real-time benchmarking
deployment; dimensions
governance
IoT security / Network CNP payment CNP-centric lifecycle
IDS surveys intrusion/anomaly lifecycle; payment mapping and payment-
detection governance; context requirements.
PCI/compliance
framing
Federated FL methods, CNP operational FL/SL role in CNP
learning aggregation, constraints; IoT detection with explicit
surveys privacy heterogeneity tied coordination/latency
(general) to payment flow trade-offs
Blockchain- Auditability, Latency impact on Governance integration
in-IoT integrity, and real-time without compromising
S
surveys ledger designs decisioning; latency, supported by
S
coupling with layered architecture
E
detectioRn pipelines guidance.
P
1.6 Paper Organization N
I
The remainder of this paper is orga nized as follows:
E

Section 2 describes theL research methodology, including the systematic review
C
protocol, search strategy, inclusion and exclusion criteria, quality assessment,
I
and analytical frTamework.
R
Section 3 presents an overview of the selected studies and summarizes their core
 A
characteristics.
Section 4 provides the main analytical synthesis, covering reviewed frameworks

and analytical structure, application scenarios and case-study contexts,
performance evaluation practices, distributed and privacy-preserving learning
models, design principles for resilient IoT-driven fraud detection, and the
formulation of a unified multi-layer framework.
Section 5 discusses the implications of the findings by mirroring the analytical

structure of Section 4, relating results to the research questions and broader IoT
and financial security contexts.
Finally, Section 6 concludes the paper by summarizing key contributions and

outlining directions for future research.
2. Methodology
2.1 Overview and Research Design
This study employs a systematic review research design guided by the PRISMA
(Preferred Reporting Items for Systematic Reviews and Meta-Analyses) 2020
framework [16] to ensure methodological rigor, transparency, and reproducibility. The
review is explicitly aligned with the study’s objectives and is structured to synthesize

ACCAERPTTICEDLE M IANN PURSECSRSIPT
existing IoT-based frameworks for real-time CNP fraud detection, using a combination
of qualitative thematic analysis and comparative performance assessment.
Rather than restricting the analysis to algorithmic performance alone, the research
design emphasizes architectural, operational, and governance dimensions, thereby
reflecting the ecosystem-level nature of IoT-enabled fraud detection systems. To this
end, the methodological workflow incorporates both descriptive and interpretive
synthesis techniques, facilitating the identification of technical trends, performance
benchmarks, and research gaps across diverse deployment contexts.
The review process consists of six interrelated stages:
1. Conceptual framing and objective alignment, in which research gaps are
identified from preliminary scoping and mapped explicitly to the study’s research
questions and objectives.
2. Systematic literature search and screening, conducted in accordance with
PRISMA 2020 guidelines [16] and informed by the PICO model [17] to ensure
comprehensive yet targeted retrieval of relevant studies.
3. Eligibility assessment and methodological quality evaluation, using a
standardized checklist to assess the robustness, relevance, and reproducibility of
included studies.
4. Structured data extraction and thematic codiSng, aligned with the research
S
questions to capture application scenarios, architectural patterns, learning
E
paradigms, and evaluation practices. R
P
5. Comparative synthesis and performance benchmarking, through consolidation
N
and cross-scenario analysis of reported metrics related to detection effectiveness,
I
real-time performance, scala bility, privacy, and governance.
E
6. Cross-layer and cross-Ltechnology synthesis, integrating findings across IoT
C
layers and intelligent paradigms to inform the formulation of a unified multi-layer
I
IoT-CNP fraud Tdetection framework.
R
A
2.2 Research Questions
The review is anchored by a series of research questions (RQs) that serve as
methodological pillars, guiding the processes of literature selection, data extraction,
analysis, and synthesis. These research questions are intricately linked to the study’s
objectives, analytical focus, and anticipated outcomes, ensuring coherence, traceability,
and methodological rigor throughout the review process. Table 2 outlines each research
objective, the corresponding research question, the analytical focus, and the expected
outcomes. It provides a clear framework that explains the review's rationale, highlights
the elements examined, and summarizes the methodologies used to present the findings.
Table 2: Research Objectives, Questions, Analytical Focus, and Expected Outputs
Objective Research Analytical Expected Output /
Question (RQ) Focus Deliverable
Objective 1: To RQ1: How can Comparative Performance matrix
conduct a quantitative existing IoT-based synthesis of and synthesis table
and qualitative frameworks be frameworks; highlighting
synthesis of existing synthesized to analysis of benchmark
IoT-based fraud- identify key accuracy, indicators and

ACCAERPTTICEDLE M IANN PURSECSRSIPT
| Objective  | Research       | Analytical  | Expected Output /  |
| ---------- | -------------- | ----------- | ------------------ |
|            | Question (RQ)  | Focus       | Deliverable        |
detection frameworks  performance  latency,  interoperability
to identify benchmarks,  benchmarks and  scalability, and  gaps.
| interoperability     | research gaps in  | privacy trade- |     |
| -------------------- | ----------------- | -------------- | --- |
| patterns, and gaps.  | CNP fraud         | offs.          |     |
detection?
Objective 2: To  RQ2: How can  Evaluation of  Thematic synthesis
evaluate distributed  distributed and  federated,  of distributed
and privacy-preserving  privacy-preserving  blockchain,  intelligence models
intelligence, such as  intelligence  and edge-based  and their
federated learning,  enhance the  models for  contributions to
blockchain, and edge  scalability and  explainability  scalable, privacy-
analytics, for  trustworthiness of  and resilience.  aware detection.
| scalability and trust.  | IoT-based CNP  |     |     |
| ----------------------- | -------------- | --- | --- |
fraud detection
systems?
| Objective 3: To  | RQ3: What design  | CompaSrative  | Guideline  |
| ---------------- | ----------------- | ------------- | ---------- |
desiSgn
| provide strategic  | principles can  |     | framework  |
| ------------------ | --------------- | --- | ---------- |
E
design guidelines for  guide efficient,  analysis;  summarizing best
R
IoT-driven fraud  adaptive, and  Pidentification  practices for

| detection emphasizing  | resilient IoTN- | of  | efficiency,  |
| ---------------------- | --------------- | --- | ------------ |
I
efficiency, adaptability,  driven fraud-   communication  adaptability, and
E
| and resilience.  | detection  | and learning  | resilience.  |
| ---------------- | ---------- | ------------- | ------------ |
L
|     | Cframeworks?  | optimization  |     |
| --- | ------------- | ------------- | --- |
I
| T   |     | mechanisms.  |     |
| --- | --- | ------------ | --- |
R
Objective 4: To  RQ4: How can a  Integration of  A six-layer IoT-
A
develop a unified IoT- unified multi-layer  findings into a  CNP fraud
| CNP fraud              | IoT-CNP       | layered IoT   | convergence    |
| ---------------------- | ------------- | ------------- | -------------- |
| convergence            | framework be  | taxonomy and  | framework for  |
| framework integrating  | developed to  | convergence   | scalable,      |
multiple IoT layers for  enhance real-time  model.  explainable,
| real-time detection.  | fraud detection  |     | privacy-compliant  |
| --------------------- | ---------------- | --- | ------------------ |
|                       | and prevention?  |     | systems and real-  |
time detection.
2.3 Search and Study Selection Process

Identification of Studies
The identification stage involved a systematic search of major academic databases.
Six  databases  were  selected  due  to  their  strong  coverage  of  computer  science,
cybersecurity, financial technology, and digital payment research. These databases
collectively  provide  broad  coverage  of  both  engineering-oriented  research  and
interdisciplinary studies related to fraud detection and digital financial systems.
The databases included:

ACCAERPTTICEDLE M IANN PURSECSRSIPT
IEEE Xplore, which provides extensive coverage of engineering, cybersecurity,

and Internet of Things research.
ScienceDirect (Elsevier), a major repository of peer-reviewed journals covering

computer science, artificial intelligence, and financial technology.
SpringerLink, which hosts numerous publications on cybersecurity, machine

learning, and digital financial systems.
Wiley Online Library, known for interdisciplinary research spanning information

systems, finance, and emerging technologies.
MDPI, which publishes open-access journals such as Sensors, Electronics, and

Future Internet that frequently feature IoT-based fraud detection studies.
Google Scholar, which was included to capture additional relevant studies not

indexed in the above databases and to ensure comprehensive coverage.
These databases were selected to ensure balanced coverage across cybersecurity,
emerging technologies, IoT systems, and financial technology research domains.
The literature search covered publications between 2015 and April 3, 2026,
reflecting the period during which IoT-based financial security systems and emerging
technology approaches for fraud detection evolved substantially.
Search Strategy
The literature search was conducted using the PSICO model [17] to ensure a
S
structured, systematic, and reproducible retrieval of studies relevant to IoT-based CNP
E
fraud detection. The resulting PICO elementsR, associated keywords, and search terms
P
are summarized in Table 3, enabling targeted identification of relevant studies.
N
Within the PICO framework, the Population corresponds to IoT-enabled digital
I
payment and transaction environm ents; the Intervention includes IoT-based fraud
E
detection, prevention, and mitLigation mechanisms; the Comparison spans centralized,
C
edge-based, distributed, and privacy-preserving architecture; and the Outcome focuses
I
on real-time or neaTr-real-time fraud detection performance, online transaction
R
monitoring, scalability, privacy preservation, and system trustworthiness.
A
Table 4 presents the database search strategy used to identify relevant studies for the
review. The table lists the scholarly databases searched, the exact Boolean search
queries applied in each database, and the filters used to refine the results. The search
queries were designed to capture literature related to Internet of Things (IoT)
technologies, fraud detection mechanisms, machine learning techniques, and financial
transaction security. Because each database has different indexing structures and search
capabilities, the queries were slightly adapted to suit the syntax and filtering options of
each platform. The applied filters ensured that the retrieved records were relevant peer-
reviewed studies within fields such as computer science, cybersecurity, and financial
technology, thereby supporting a systematic, transparent, and reproducible literature
search process.
Table 3: PICO Model Mapping and Search Alignment
PICO Definition / Focus Keywords and Synonyms Purpose / Link to
Element Used RQs
Population IoT-based financial “Internet of Things,” “IoT,” Defines the IoT
(P) transaction and “edge device,” “smart sensor,” ecosystem context
for CNP fraud

ACCAERPTTICEDLE M IANN PURSECSRSIPT
PICO  Definition / Focus  Keywords and Synonyms  Purpose / Link to
| Element  |                  |     |     | Used                        |     |     |     |     | RQs             |
| -------- | ---------------- | --- | --- | --------------------------- | --- | --- | --- | --- | --------------- |
|          | fraud-detection  |     |     | “connected device,” “smart  |     |     |     |     | detection (RQ1- |
|          | environments     |     |     | payment infrastructure.”    |     |     |     |     | RQ4).           |
Intervention Real-time,  “real-time detection,” “fraud  Identifies
(I)  distributed, and  mitigation,” “federated  technological
privacy-preserving  learning,” “blockchain,” “edge  interventions and
|     | fraud-detection  |     |     | AI,” “fog computing,”           |     |     |     |     | architectures  |
| --- | ---------------- | --- | --- | ------------------------------- | --- | --- | --- | --- | -------------- |
|     | frameworks       |     |     | ”Distributed Learning,’ “deep   |     |     |     |     | studied (RQ1-  |
|     |                  |     |     | learning,” “anomaly detection”  |     |     |     |     | RQ3).          |
Comparison  Traditional  “rule-based detection,”  Provides a baseline
(C)  centralized or static  “centralized framework,”  for comparing IoT-
|     | fraud-detection  |     |     | “static models,” “batch  |     |     |     |     | enabled adaptive  |
| --- | ---------------- | --- | --- | ------------------------ | --- | --- | --- | --- | ----------------- |
|     | systems          |     |     | processing”              |     |     |     |     | systems (RQ1).    |
Outcome   Enhanced detection  “accuracy,” “latency,”  Defines
| (O)  | accuracy,  |     |     | “precision,” “recall,”  |     |     |     |     | measurable  |
| ---- | ---------- | --- | --- | ----------------------- | --- | --- | --- | --- | ----------- |
scalability, privacy,  “scalability,” “communication  outcomes for
|     | and interoperability  |     |     | efficiency,” “privacSy  |     |     |     |     | synthesis and  |
| --- | --------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | -------------- |
S
|     |     |     |     | overhead”  |     |     |     |     | benchmarking  |
| --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ------------- |
E
(RQ1-RQ4).
R
P

N
Table 4: Database Search Strategy for Literature Retrieval
I

| Database  |     | Exact SearchE Query  |     |     |     |     |     |     | Filters Applied  |
| --------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | ---------------- |
L
(("Fraud CDetection" AND IoT AND "Financial
I
|     |     | Transactions") OR ("IoT Device Security" AND  T |         |     |      |          |          |     |     |
| --- | --- | ----------------------------------------------- | ------- | --- | ---- | -------- | -------- | --- | --- |
|     |     | "SRmart  Card                                   | Fraud"  |     | AND  | "Credit  | Cards")  | OR  |     |
A
(Blockchain AND IoT AND "E-Commerce") OR  Internet of Things
|     |     | ("Privacy-Preserving Anomaly Detection" AND  |     |     |     |     |     |     | Conferences  |
| --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ |
IEEE Xplore
|     |     | IoT  AND     | ("Federated  |              |      | Learning"  | OR         | "Split  | Journals  |
| --- | --- | ------------ | ------------ | ------------ | ---- | ---------- | ---------- | ------- | --------- |
|     |     | Learning"))  | OR           | ("Federated  |      |            | Learning"  | AND     |           |
|     |     | "Intrusion   | Detection"   |              | AND  | IoT)       | OR         | ("Deep  |           |
Learning" AND "Real-Time Anomaly Detection"
AND IoT))
(("IoT" AND "Financial Fraud Detection" AND
|     |     | ("Artificial      | Intelligence"  |     |     | OR        | Survey     | OR  |     |
| --- | --- | ----------------- | -------------- | --- | --- | --------- | ---------- | --- | --- |
|     |     | Implementation))  |                |     | OR  | ("Secure  | IoT-Based  |     |     |
Wiley Online  Payments" AND "PCI DSS" AND "Payment Card  Journals
| Library  |     | Industry  | Data  | Security  |     |     | Standard")  | OR  |     |
| -------- | --- | --------- | ----- | --------- | --- | --- | ----------- | --- | --- |
("Distributed framework" AND "DDoS attacks"
|     |     | AND  Blockchain  |     |     | AND  | IoT  | AND  | "Smart  |     |
| --- | --- | ---------------- | --- | --- | ---- | ---- | ---- | ------- | --- |
Contracts" AND "Fog Computing"))
("Internet of Things" OR IoT OR "smart device"  Research Article
|     |     | OR "connected device" OR "edge device") AND  |     |     |     |     |     |     | Computational  |
| --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- |
SpringerLink
("fraud  detection"  OR  "fraud  prevention"  OR  Intelligence
"fraud  mitigation")  AND  ("card-not-present  Machine learning

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Database Exact Search Query Filters Applied
fraud" OR "card not present fraud" OR "card Data and
fraud" OR "payment fraud" OR "online payment information
fraud") AND ("real-time" OR "near real-time" OR security
"real time") Federated
Learning for
privacy-
preserving and
data analysis
Research Articles
("fraud detection" OR "credit card fraud") AND
Computer
ScienceDirect ("Internet of Things" OR IoT) AND ("machine
Science
(Elsevier) learning" OR "deep learning") AND ("financial
Engineering
transaction" OR payment)
Decision Science
("Internet of Things" OR IoT) AND ("anomaly
detection" OR "intrusion detection" OR "fraud Journals =
MDPI detection") AND ("machine learningS" OR "deep sensors,
learning" OR "federated learning"S OR "security" information, IoT
E
OR "privacy")
R
("Internet of Things" ORP IoT*) AND ("fraud
detection" OR "card Nfraud" OR card-not-present
I
Google fraud "anomaly detection" OR "intrusion
E
Scholar detection") ALND ("machine learning" OR "deep
C
learning" OR "federated learning" OR
I
BlockTchain)
R
A
Selection of Studies (Eligibility)
The full texts of the remaining articles were then evaluated against predefined
inclusion and exclusion criteria.
Inclusion Criteria
Studies were included based on the following criteria:
 They address card-not-present or online payment fraud detection within an
IoT ecosystem.
 They explicitly focus on IoT-based fraud detection, prevention, or mitigation
in online or CNP-based transaction environments.
 They propose frameworks for real-time or near-real-time fraud detection,
substantiated by operational evidence (e.g., latency, throughput) or design
characteristics suitable for time-sensitive monitoring. Architectural suitability
alone does not suffice.
 They demonstrate or assert real-time fraud detection capabilities in online
monitoring, reflecting this through design or performance evaluation.
 They employ advanced techniques such as machine learning, federated
learning, distributed learning, or blockchain governance mechanisms.
 They provide experimental validation or conduct a system evaluation.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Exclusion Criteria
Studies were excluded if they:
Focused exclusively on card-present fraud detection

Did not involve IoT or distributed computing technologies

Lacked sufficient methodological detail

Were non-peer-reviewed or non-English publications.

This review’s inclusion criteria were designed to identify studies that contribute to
the technological ecosystem for CNP fraud detection in IoT environments. While the
review is anchored in digital payment fraud detection, effective real-time detection in
IoT settings depends on enabling components, including data collection, network
communication, anomaly detection, distributed learning, edge analytics, blockchain,
and IoT security controls. Accordingly, the review intentionally adopts an ecosystem
perspective rather than a purely algorithmic one, retaining studies not only when they
directly address card-not-present fraud but also when they contribute cross-layer
mechanisms essential to real-time CNP fraud detection.
Screening and Eligibility Assessment S
S
The database search identified 1,129 records, which were narrowed to 303 articles
E
through an initial relevance-filtering process. ARfter duplicate removal using Zotero, 67
P
unique studies remained. Titles and abstracts were then screened against predefined
N
inclusion and exclusion criteria, resulting in the exclusion of 17 studies and leaving 50
I
articles for full-text review.
E
At the second stage, full-Ltext articles were evaluated for methodological rigor,
C
evidence of IoT implementation, relevance to fraud detection, applicability to real-time
I
or near-real-time contTexts, and the reporting of evaluation metrics. This assessment
R
resulted in the exclusion of 27 additional studies because they lacked methodological
A
transparency, did not demonstrate explicit fraud-detection capability, focused on non-
IoT settings, or failed to provide evidence relevant to distributed, real-time, or IoT-
enabled payment security. As a result, 23 studies were included in the final synthesis.
Although the final corpus includes only 23 studies from 2015 to April 2026, this
reflects the review’s narrow scope and the strict application of PRISMA-based
eligibility criteria. The review was not designed to include all studies on credit card
fraud, IoT anomaly detection, blockchain security, or federated learning independently.
Instead, it retained only studies that contributed directly or mechanistically to real-time
or near-real-time card-not-present (CNP) fraud detection in IoT-enabled payment
environments. Thus, the final corpus serves as a focused, quality-controlled evidence
base for ecosystem-level synthesis rather than a broad mapping of related literature.
The study selection process is presented in the PRISMA flow diagram (Fig. 2), and
Fig. 3 shows the distribution of included studies across scholarly databases, highlighting
each source’s contribution to the final corpus.
Fig. 2 The screening process

ACCAERPTTICEDLE M IANN PURSECSRSIPT
S
S
Fig. 3 Number of selected papers per database
E
R
P
10
N
I
E
6
L
C
I
T 3
R 2
1 1
A
Google IEEE Wiley MDPI Springer ScienceDirect
Scholar
2.4 Quality Assessment
To evaluate the methodological rigor of the selected studies, a quality assessment
process was conducted using five evaluation criteria shown in Table 5, covering
research clarity, methodological transparency, dataset adequacy, performance
evaluation, and relevance to IoT-enabled fraud detection.
Table 5: Quality Assessment Criteria
Code Criterion
QA1 Clear research objective
QA2 Adequate methodology description
QA3 Use of an appropriate dataset or evaluation environment
QA4 Performance evaluation using relevant metrics

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Code  Criterion
QA5  Relevance to IoT-enabled fraud detection

Each criterion was scored using a three-point scale: 1 (Yes), 0.5 (Partially), and 0
(No). The maximum possible score for each study was five.
The results summarized in Table 6 indicate that most studies demonstrate strong
methodological rigor,  particularly  those  focusing on  machine  learning-based  fraud
detection  using  publicly  available  financial  transaction  datasets.  However,  several
studies  focusing  on  conceptual  frameworks  or  surveys  scored  lower  in  dataset
evaluation and empirical validation.
Overall, the quality assessment confirms that most of the included studies provide
reliable empirical insights into fraud detection techniques relevant to CNP fraud in IoT-
enabled payment ecosystems.
Table 6: Quality Assessment Results
| Study  | QA1  | QA2  | QA3  | QA4  | QA5  | Score  |
| ------ | ---- | ---- | ---- | ---- | ---- | ------ |
| A1     | 1    | 1    | 1    | 1    | 1    | 5      |
| A2     | 1    | 0.5  | 0    | 0    | 1    | 2.5    |
S
| A3  | 1   | 1   | 0.5  | 0S.5  | 1   | 4   |
| --- | --- | --- | ---- | ----- | --- | --- |
E
| A4  | 1   | 0.5  | 0.5  | 0.5  | 0.5  | 3   |
| --- | --- | ---- | ---- | ---- | ---- | --- |
R
| A5  | 1   | 1   | 1 P | 1   | 0.5  | 4.5  |
| --- | --- | --- | --- | --- | ---- | ---- |

N
| A6  | 1   | 1   | 1   | 0.5  | 0.5  | 4   |
| --- | --- | --- | --- | ---- | ---- | --- |
I

| A7  | 1   | 1 E | 1   | 0.5  | 0.5  | 4   |
| --- | --- | --- | --- | ---- | ---- | --- |
L
| A8  | 1   | 1   | 1   | 0.5  | 0.5  | 4   |
| --- | --- | --- | --- | ---- | ---- | --- |
C
I
| A9  | 1  T | 1   | 0.5  | 0.5  | 1   | 4   |
| --- | ---- | --- | ---- | ---- | --- | --- |
R
| A10  | 1   | 1   | 0.5  | 0.5  | 0.5  | 3.5  |
| ---- | --- | --- | ---- | ---- | ---- | ---- |
A
| A11  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |
| ---- | --- | --- | ---- | ---- | ---- | ---- |
| A12  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |
| A13  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |
| A14  | 1   | 1   | 0.5  | 0.5  | 0.5  | 3.5  |
| A15  | 1   | 1   | 0.5  | 1    | 0.5  | 4    |
| A16  | 1   | 1   | 0    | 0    | 0.5  | 2.5  |
| A17  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |
| A18  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |
| A19  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |
| A20  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |
| A21  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |
| A22  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |
| A23  | 1   | 1   | 1    | 1    | 0.5  | 4.5  |

Table 7 presents all included studies, with articles coded from Article 1 (A1) to Article
(A23) to support traceability and cross-referencing throughout the analysis.

ACCAERPTTICEDLE M IANN PURSECSRSIPT

Table 7: Summary of the 23 selected studies included in the review
Primary
Author(s) &
| Code  | Title / Framework  | Approach /  | Key Focus Area  |
| ----- | ------------------ | ----------- | --------------- |
Year
Technique
Detection of Fraud in
|                |                        | Ensemble       | ML-driven fraud   |
| -------------- | ---------------------- | -------------- | ----------------- |
| Alatawi, 2025  | IoT-Based Credit Card  |                |                   |
| A1             |                        | Learning (RF,  | detection in IoT  |
| [1]            | Dataset Using Machine  |                |                   |
|                |                        | DNN, SVM)      | ecosystems        |
Learning
|     |     | Security  | Secure IoT  |
| --- | --- | --------- | ----------- |
Towards Secure IoT-
| Bhutta et al.,  |                    | Compliance, IoT  | payment     |
| --------------- | ------------------ | ---------------- | ----------- |
| A2              | Based Payments by  |                  |             |
| 2022 [2]        |                    | Payment          | compliance  |
Extending PCI DSS
|     |     | Architecture  | framework  |
| --- | --- | ------------- | ---------- |
NormaChain: A
|     |     | Blockchain,  | Blockchain  |
| --- | --- | ------------ | ----------- |
Blockchain-Based
| Liu et al., 2019  |                        | Smart Contracts,  | auditability and  |
| ----------------- | ---------------------- | ----------------- | ----------------- |
| A3                | Normalized Autonomous  |                   |                   |
| [3]               |                        | Searchable        | autonomous IoT e- |
Transaction Settlement
|     |         | Encryption  | commerce  |
| --- | ------- | ----------- | --------- |
|     | System  | S           |           |
S
|     | Integrating Deep  | E   |     |
| --- | ----------------- | --- | --- |
Gupta &  Learning, Machine  R Deep Learning,  AI-IoT integration
P
A4  Kumar, 2024  Learning, AI, IoT,  and  Predictive  for predictive
N
| [4]  | Data Science for Future  | Analytics  | decision systems  |
| ---- | ------------------------ | ---------- | ----------------- |
I

Innovations
E
L
|     | IoT-GRAF: IoT Graph  | Graph Neural  |     |
| --- | -------------------- | ------------- | --- |
C Graph-based fusion
| Yasaei et al.,  | LIearning-Based  | Networks  |     |
| --------------- | ---------------- | --------- | --- |
T
| A5        |                         |                | for anomaly and  |
| --------- | ----------------------- | -------------- | ---------------- |
| 2024 [5]  | RAnomaly and Intrusion  | (GNNs), Multi- |                  |
intrusion detection
|     | A Detection  | Modal Fusion  |     |
| --- | ------------ | ------------- | --- |
Enhancing Privacy in
Secure
|                | IoT-Enabled Digital   | Federated          |                |
| -------------- | --------------------- | ------------------ | -------------- |
| Deshmukh et    |                       |                    | collaborative  |
| A6             | Infrastructure:       | Learning, Privacy  |                |
| al., 2025 [6]  |                       |                    | learning and   |
|                | Evaluating Federated  | Preservation       |                |
anomaly detection
Learning
|     | Privacy-Preserving  |     | Collaborative  |
| --- | ------------------- | --- | -------------- |
Split Learning,
| Rguibi et al.,  | Anomaly Detection for    |            | model training  |
| --------------- | ------------------------ | ---------- | --------------- |
| A7              |                          | Federated  |                 |
| 2024 [7]        | IoT Using Federated and  |            | under privacy   |
Learning
|     | Split Learning  |     | constraints  |
| --- | --------------- | --- | ------------ |
Privacy-Aware Anomaly Group-Based
Privacy-preserving
| Zhang et al.,  | Detection in IoT    | Federated  |                |
| -------------- | ------------------- | ---------- | -------------- |
| A8             |                     |            | collaborative  |
| 2024 [8]       | Environments Using  | Learning   |                |
anomaly detection
|     | FedGroup                 | (FedGroup)  |                |
| --- | ------------------------ | ----------- | -------------- |
|     | IoT Device Security for  |             | NFC-based IoT  |
NFC, Random
| Devi et al.,  | Smart Card Fraud      |                   | security and  |
| ------------- | --------------------- | ----------------- | ------------- |
| A9            |                       | Forest, Bayesian  |               |
| 2023 [18]     | Detection for Credit  |                   | transaction   |
Network
|     | Cards  |     | verification  |
| --- | ------ | --- | ------------- |

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Primary
Author(s) &
| Code  | Title / Framework  |     | Approach /  | Key Focus Area  |
| ----- | ------------------ | --- | ----------- | --------------- |
Year
Technique
A Distributed
Blockchain, Fog
Framework for Detecting  DDoS detection
| Kumar et al.,  |                        |     | Computing,   |                      |
| -------------- | ---------------------- | --- | ------------ | -------------------- |
| A10            | DDoS Attacks in Smart  |     |              | and fog-level fraud  |
| 2021 [19]      |                        |     | Distributed  |                      |
Contract-Based  mitigation
Detection
Blockchain-IoT Systems
A Multi-Layered AI-IoT  Adaptive financial
| Garg et al.,  |                         |     | Deep Learning,   |                   |
| ------------- | ----------------------- | --- | ---------------- | ----------------- |
| A11           | Framework for Adaptive  |     |                  | intelligence and  |
| 2024 [20]     |                         |     | Multi-Agent IoT  |                   |
Financial Services  anomaly detection
A Novel Federated  Distributed
Federated
| Benameur et al., Learning-Based  |                      |     |           | intrusion detection  |
| -------------------------------- | -------------------- | --- | --------- | -------------------- |
| A12                              |                      |     | Learning  |                      |
| 2024 [21]                        | Intrusion Detection  |     |           | and collaborative    |
(FedAvg)
System for IoT Networks  learning
A Hybrid Fuzzy Logic
Cybersecurity and
and Federated Learning  Fuzzy Logic,
| Rehman et al.,  |                    |     |             | anomaly detection  |
| --------------- | ------------------ | --- | ----------- | ------------------ |
| A13             | Framework for IoT- |     | FederSated  |                    |
| 2025 [22]       |                    |     | S           | in virtual IoT     |
Enabled Metaverse  Learning
E
systems
Transactions
R
P
A Robust and Scalable

|     |     | N   | CNN-LSTM  |     |
| --- | --- | --- | --------- | --- |
Deep Learning  Deep learning
| Vankayalapati  |     | I   | Hybrid,  |     |
| -------------- | --- | --- | -------- | --- |
Framework  for Real-
| A14                |     |     |              | resilience and  |
| ------------------ | --- | --- | ------------ | --------------- |
| et al., 2025 [23]  |     | E   | Adversarial  |                 |
Time ILoT Intrusion  energy efficiency
|     | C   |     | Resilience  |     |
| --- | --- | --- | ----------- | --- |
Detection
I
T
A Secure Framework for Random Forest,  IoT anomaly
R
Prakash et al.,
| A15  | A IoT Anomalies Using  |     | SVM, Ensemble  | detection and  |
| ---- | ---------------------- | --- | -------------- | -------------- |
2024 [24]
|     | Machine Learning  |     | Learning  | network protection  |
| --- | ----------------- | --- | --------- | ------------------- |
Advanced Deep
Multi-class
Learning Approaches for Deep Neural
| Goyal et al.,  |                    |     |            | anomaly detection  |
| -------------- | ------------------ | --- | ---------- | ------------------ |
| A16            | Real-Time Anomaly  |     | Networks,  |                    |
| 2024 [25]      |                    |     |            | for IoT data       |
Detection in IoT  Ensemble Models
streams
Environments
Financial
An Artificial Intelligence
|     |     |     | AI Rule-Based  | transaction fraud  |
| --- | --- | --- | -------------- | ------------------ |
Choi & Lee,  Approach to Financial
| A17  |     |     | Systems, Neural  | detection and  |
| ---- | --- | --- | ---------------- | -------------- |
2018 [26]  Fraud Detection under
|     |     |     | Networks  | behavioral  |
| --- | --- | --- | --------- | ----------- |
IoT Environment
profiling
Credit Card Fraud
Collaborative fraud
| Subhalaxmi et   | Detection Using Multi-  |     | Federated Neural  |                   |
| --------------- | ----------------------- | --- | ----------------- | ----------------- |
| A18             |                         |     |                   | detection across  |
| al., 2023 [27]  | Layer Perceptron Based  |     | Networks          |                   |
distributed nodes
on Federated Learning
Detecting Anomalous  Decision Trees,
| Min et al., 2021  |                          |     |           | Transaction-level  |
| ----------------- | ------------------------ | --- | --------- | ------------------ |
| A19               | Transactions via an IoT- |     | Gradient  |                    |
| [28]              |                          |     |           | anomaly detection  |
Based Application  Boosting

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Primary
Author(s) &
| Code  | Title / Framework  | Approach /  | Key Focus Area  |
| ----- | ------------------ | ----------- | --------------- |
Year
Technique
Digital Twin and IoT-
Real-time
Abubakar et al., Enabled Online Learning Digital Twin,
| A20        |                      |                 | monitoring and  |
| ---------- | -------------------- | --------------- | --------------- |
| 2024 [29]  | Model for Real-Time  | Edge Computing  |                 |
predictive learning
Fraud Monitoring
Edge AI in IoT:
|                 | Leveraging Cloud          |                  | Cloud-edge           |
| --------------- | ------------------------- | ---------------- | -------------------- |
| Murthy et al.,  |                           | Edge AI, Cloud–  |                      |
| A21             | Computing and Big Data    |                  | synergy for          |
| 2024 [30]       |                           | Fog Integration  |                      |
|                 | for Intelligent Decision- |                  | financial analytics  |
Making
Fraud Detection in IoT-
Unsupervised
Based Financial
| Kafila et al.,  |                     | Isolation Forest,  | anomaly detection  |
| --------------- | ------------------- | ------------------ | ------------------ |
| A22             | Transactions Using  |                    |                    |
| 2024 [31]       |                     | Autoencoder        | in financial IoT   |
Anomaly Detection
systems
Techniques
|             | Real-Time Fraud          | S                 |                  |
| ----------- | ------------------------ | ----------------- | ---------------- |
|             |                          | AIS-Driven Fraud  | Real-time fraud  |
| Maddukuri,  | Detection Using IoT and  |                   |                  |
EDetection, IoT
| A23        |                            |          | protection for   |
| ---------- | -------------------------- | -------- | ---------------- |
| 2022 [32]  | AI: Securing the DigitRal  |          |                  |
|            |                            | Sensors  | digital wallets  |
P
Wallet

N

I
As illustrated in Fig. 4, the reviewed  studies span the principal layers of the IoT-enabled
E
fraud detection framework, enLabling an ecosystem-level understanding of how sensing,
C
communication, analytics, and governance interact in real-time payment surveillance.
I
T

R
Fig. 4 MappAing of studies to different layers of the IoT-enabled fraud detection
ecosystem.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
S
S
E
R
Potential Sources of Bias in the Included Studies
P
Several sources of bias were identified across the included studies. Many relied on
N
simulated, curated, or domain-specific datasets that may not fully capture the
I
complexity, imbalance, and temEporal evolution of real-world CNP fraud. Evaluation
L
bias was also evident, as performance was often reported primarily using accuracy-
C
oriented metrics, with limIited consideration of false positives, latency, throughput, and
T
deployment realismR. Furthermore, some studies originated in adjacent IoT anomaly or
intrusion-detectiAon domains, which may limit the direct transferability of their findings
to CNP fraud detection. Accordingly, the final evidence base should be viewed as
scope-driven and quality-filtered, with emphasis placed on recurring architectural
patterns and methodological trends rather than headline performance figures.
2.5 Data Extraction and Coding
A structured data extraction and coding protocol was implemented to ensure
consistent analysis across all included studies. Table 8 summarizes the extraction
schema, outlining the categories, variables, and their analytical roles. Each category
serves a specific purpose, such as framework characterization, IoT layer mapping,
learning paradigm identification, performance evaluation, and privacy assessment,
thereby enhancing comparability across diverse studies. By aligning each extraction
category with an analytical role, the protocol ensured comprehensive coverage of all
research questions (RQ1-RQ4). These elements contributed to the thematic synthesis
and to the development of a unified convergence framework that addresses all research
questions. This extraction protocol also underpins the study’s comparative
benchmarking logic by ensuring that predictive effectiveness, real-time responsiveness,
scalability/resource efficiency, privacy/trust indicators, and implementation evidence
were captured systematically across studies. Accordingly, the coding strategy was

ACCAERPTTICEDLE M IANN PURSECSRSIPT
designed not only to support thematic synthesis but also to reveal where the literature
provides operationally useful evidence and where major reporting gaps remain.

Table 8: Data extraction and analytical mapping summary
| Category  | Data Extracted  | Purpose / Analytical  | Linked    |
| --------- | --------------- | --------------------- | --------- |
|           |                 | Role                  | Research  |
Question(s)
General  Study Identifier (code),  Enables traceability,  All RQs
| Identification  | Title, Authors, Year,     | transparency, and       |     |
| --------------- | ------------------------- | ----------------------- | --- |
|                 | Publication Type, Source  | citation management     |     |
|                 | Database                  | across the 23 selected  |     |
studies.
Framework  Type of IoT-based  Categorizes frameworks RQ1, RQ4
Description  framework (e.g., federated,  to facilitate comparative
|     | blockchain, graph-based,  | synthesis and taxonomy  |     |
| --- | ------------------------- | ----------------------- | --- |
|     | deep learning, edge AI,   | construction.           |     |
fuzzy logic)
IoT Architectural  Perception, Network,  MapsS frameworks to  RQ4
S
| Layer  | Processing, Application, or  | IoT ecosystem layers  |     |
| ------ | ---------------------------- | --------------------- | --- |
E
|     | Security–Governance layeRr  | for layered framework  |     |
| --- | --------------------------- | ---------------------- | --- |
P
|     | representation  | synthesis.  |     |
| --- | --------------- | ----------- | --- |

N
Detection  Machine Learning, Deep  Identifies computational  RQ1, RQ2
I
Learning, Feder ated
| Approach /  |     | paradigms and  |     |
| ----------- | --- | -------------- | --- |
E
| Algorithm  | Learning, LBlockchain  | architectural integration  |     |
| ---------- | ---------------------- | -------------------------- | --- |
C
|     | Integration, Graph Neural  | for pattern recognition.  |     |
| --- | -------------------------- | ------------------------- | --- |
I
T
Networks, Anomaly
R
ADetection
Data Source /  Dataset type (e.g., ISO  Provides empirical  RQ1, RQ2
| Context  | 8583, simulated IoT          | grounding and           |     |
| -------- | ---------------------------- | ----------------------- | --- |
|          | transactions, payment logs,  | application context of  |     |
|          | edge-device data streams)    | each framework.         |     |
Performance  Accuracy, Precision, Recall,  Enables quantitative  RQ1, RQ2,
| Metrics  | F1-score, Latency,          | benchmarking and         | RQ3  |
| -------- | --------------------------- | ------------------------ | ---- |
|          | Communication Overhead,     | comparative              |      |
|          | Energy Efficiency, Privacy  | performance evaluation.  |      |
Overhead
Privacy and  Differential Privacy, SHA- Evaluates privacy- RQ2, RQ3
| Security    | 256, Homomorphic          | preserving and trust  |     |
| ----------- | ------------------------- | --------------------- | --- |
| Techniques  | Encryption, K-Anonymity,  | mechanisms used in    |     |
|             | Blockchain Auditability   | distributed models.   |     |
Interoperability  Cross-platform  Assesses the scalability  RQ2, RQ3
and Scalability  compatibility, network  and interoperability of
| Indicators  | integration level, edge-fog- | IoT frameworks.  |     |
| ----------- | ---------------------------- | ---------------- | --- |
cloud coordination

ACCAERPTTICEDLE M IANN PURSECSRSIPT
| Category  | Data Extracted  |     | Purpose / Analytical  | Linked    |
| --------- | --------------- | --- | --------------------- | --------- |
|           |                 |     | Role                  | Research  |
Question(s)
Limitations and  Reported weaknesses (e.g.,  Identifies systemic  RQ1, RQ2,
| Challenges  | communication cost,         |     | issues and informs  | RQ3  |
| ----------- | --------------------------- | --- | ------------------- | ---- |
|             | latency, interoperability,  |     | design              |      |
|             | energy consumption)         |     | recommendations.    |      |
Many studies on fraud
detection frameworks
describe them as real-time
but fail to report key
performance metrics like
latency, inference time, or
throughput, hindering
objective evaluation.
Proposed  Optimization algorithms,  Examines how prior  RQ2, RQ3
| Solutions /  | encryption layers, edge  |     | studies addressed       |     |
| ------------ | ------------------------ | --- | ----------------------- | --- |
| Mitigation   | computing, adaptive      |     | identified challenges.  |     |
S
| Strategies  | federated models  |     | S   |     |
| ----------- | ----------------- | --- | --- | --- |
E
Emerging Trends  Use of digital twins, self- Captures evolving  RQ3, RQ4
R
| / Future  | learning IoT nodes, ethiPcal  |     | directions and  |     |
| --------- | ----------------------------- | --- | --------------- | --- |

| Directions  | AI, and regulatory N |     | anticipated  |     |
| ----------- | -------------------- | --- | ------------ | --- |
I
|     | considerations  |     | technological  |     |
| --- | --------------- | --- | -------------- | --- |
E
transformations.
L
C
Tool Support /  Simulation platforms,  Validates real-time  RQ1, RQ4
I
proTtotype deployment, or
| Implementation  |     |     | capability and practical  |     |
| --------------- | --- | --- | ------------------------- | --- |
R
Evidence  real-time testbeds (e.g.,  feasibility of reviewed
A
|     | FogSim, TensorFlow, Edge  |     | frameworks.  |     |
| --- | ------------------------- | --- | ------------ | --- |
devices)
Synthesis and  Key insight, contribution  Integrates qualitative  All RQs
Contribution  type (conceptual, technical,  and quantitative results
| Mapping  | empirical), and impact  |     | into the unified IoT– |     |
| -------- | ----------------------- | --- | --------------------- | --- |
|          | statement               |     | CNP Fraud             |     |
Convergence
Framework.
2.6 Analytical and Synthesis Strategy
The analytical and synthesis strategy was designed to provide systematic progression
from  evidence  gathering  to  framework  development.  Each  research  question  was
addressed using specific analytical techniques, enabling structured interpretation of
diverse findings aligned with the study's objectives. Table 9 summarizes the mapping
of  research  questions,  analytical  techniques,  synthesis  approaches,  and  expected
outcomes,  ensuring  transparency  in  evidence  processing  and  supporting  the
reproducibility of the review.

Table 9: Analytical and synthesis strategy for research questions

ACCAERPTTICEDLE M IANN PURSECSRSIPT
| Research       | Analytical  | Synthesis /  | Expected Output /  |
| -------------- | ----------- | ------------ | ------------------ |
| Question (RQ)  | Technique   | Evaluation   | Deliverable        |
Approach
RQ1: How can  • Chronological  • Comparative  • Consolidated
existing IoT-based  and typological  performance  taxonomy of IoT-
| frameworks be   | mapping of      | synthesis using a    | based fraud- |
| --------------- | --------------- | -------------------- | ------------ |
| synthesized to  | frameworks      | cross-study matrix   | detection    |
| identify key    | • Quantitative  | • Descriptive        | frameworks   |
performance  benchmarking of  statistics and trend  • Benchmark matrix
| benchmarks and    | accuracy,  | identification   | summarizing      |
| ----------------- | ---------- | ---------------- | ---------------- |
| research gaps in  | latency,   | • Framework      | performance and  |
CNP fraud  scalability, and  evolution analysis  interoperability
| detection?  | energy efficiency  | (centralized -  | indicators  |
| ----------- | ------------------ | --------------- | ----------- |
|             | metrics            | distributed -   |             |
federated)
RQ2: How can  • Thematic coding  • Cross-comparison  • Evidence table of
distributed and  of privacy and  of distributed- distributed learning
privacy-preserving  security features  intelligence  models
S
| intelligence  | (e.g., federated  | approachSes   | • Summary of  |
| ------------- | ----------------- | ------------- | ------------- |
E
| enhance the  | learning,  | • Privacy- | scalability and trust- |
| ------------ | ---------- | ---------- | ---------------------- |
R
| scalability and  | blockchain  | pPerformance trade- | enhancing  |
| ---------------- | ----------- | ------------------- | ---------- |

trustworthiness of  auditability,  Noff mapping   mechanisms
IoT-based CNP  differential  I • Evaluation of  • Identified best

fraud detection  privacy)   E explainability and  practices for
L
| systems?  | • QuCalitative  | adversarial  | privacy-preserving  |
| --------- | --------------- | ------------ | ------------------- |
coIntent analysis
|     | T   | resilience  | architectures  |
| --- | --- | ----------- | -------------- |
RQ3: What design  R • Comparative  • Synthesis of  • Strategic design
A
principles can  design analysis   design strategies  guideline set
| guide efficient,  | • Problem–        | addressing     | • Architecture- |
| ----------------- | ----------------- | -------------- | --------------- |
| adaptive, and     | solution matrix   | communication  | performance     |
resilient IoT-driven  • Trend clustering  overheads, adaptive  correlation matrix
fraud-detection  via thematic  learning, and  • Recommendations
| frameworks?  | synthesis  | resilience           | for future IoT fraud- |
| ------------ | ---------- | -------------------- | --------------------- |
|              |            | • Identification of  | detection design      |
recurring
architectural motifs
RQ4: How can a  • Integrative  • Consolidation of  • Final IoT-CNP
unified multi-layer  synthesis of  analytical findings  Fraud Convergence
| IoT–CNP       | results from     | into six IoT layers  | Framework for     |
| ------------- | ---------------- | -------------------- | ----------------- |
| framework be  | RQ1-RQ3          | (Perception,         | scalable,         |
| developed to  | • Layer mapping  | Network,             | explainable, and  |
enhance real-time  and conceptual  Processing, Cloud  privacy-compliant.
| fraud detection and  | modeling     | Analytics,    |     |
| -------------------- | ------------ | ------------- | --- |
| prevention?          | • Taxonomy   | Application,  |     |
|                      | formulation  | Security-     |     |
Governance)

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Research Analytical Synthesis / Expected Output /
Question (RQ) Technique Evaluation Deliverable
Approach
• Framework
abstraction and
validation roadmap
3 Literature Review
3.1 Evolution of IoT ecosystem for fraud detection and prevention
The layers of the IoT ecosystem have transitioned from abstract theoretical concepts
to fully operational systems leveraging edge intelligence, behavioral analytics, and
adaptive machine learning technologies. This progression is illustrated in Table 10,
which provides a structured timeline detailing the evolution of various layers within the
IoT ecosystem, particularly in the context of fraud detection. The analysis categorizes
advancements across the fundamental layers. Each layer is essential to the architecture,
enhancing fraud detection mechanisms and reinforcing the integrity of IoT systems.
From 2015 to April 3, 2026, the perception layer evolved from basic data sensing to
S
the integration of biometric and near field communication (NFC) technologies,
S
providing richer contextual insights. The netwoErk layer advanced from foundational
R
encryption to sophisticated, large-scale, cloud-supported data flows. In the processing
P
layer, we observed a transition from tra ditional machine learning to deep learning,
N
including generative adversarial networks (GANs), and real-time analytics, which
I
enables scalable and adaptive dEetection. Meanwhile, the application layer progressed
from simple user interfaces to Ladvanced dashboards that incorporate explainable AI and
C
adaptive learning. The Isecurity and governance layer saw notable enhancements,
T
integrating blockchain technologies and regulatory compliance mechanisms to enhance
R
auditability and Arobustness.
These layers illustrate a developing ecosystem where technological innovation is
increasingly aligned with real-time responsiveness, intelligent capabilities, privacy
considerations, and regulatory compliance in the context of fraud prevention. This
integration highlights the gradual, step-by-step improvement in the IoT fraud detection
infrastructure observed over the past decade.
Table 10: Evolution timeline of IoT ecosystem layers in fraud detection
Layer Key Periods & Developments
2015-2020: Initial adoption of IoT-enabled payment devices
and sensors for real-time data collection.
Perception Layer 2021-April 3, 2026: Enhanced with NFC and biometric sensors
for double verification and richer behavioral/contextual data
capture.
2015-2020: Focus on secure, reliable data transmission and
basic encryption protocols.
Network Layer 2021-April 3, 2026: Integration of cloud networking, improved
encryption, and support for high-speed, large-scale IoT data
flows.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Layer Key Periods & Developments
2017-2022: Introduction of machine learning (ML) and big
data analytics for fraud detection.
Processing Layer 2023-April 3, 2026: Adoption of deep learning, GANs, and
advanced feature engineering for real-time, adaptive, and
scalable fraud analysis.
2018-2022: Development of user interfaces for real-time alerts
and risk visualization.
Application Layer 2023-April 3, 2026: Emphasis on explainable AI, adaptive
learning, and user feedback integration for continuous
improvement.
2017-2022: Implementation of basic encryption and access
Security and control.
Governance 2023-April 3, 2026: Integration of blockchain, advanced
Layer encryption, and regulatory compliance mechanisms for robust,
tamper-resistant audit trails.
3.2 IoT Layered Taxonomy
Reviewing IoT-driven frameworks through a laSyered taxonomy is vital for
S
identifying their architectural strengths and weaknesses. Following the canonical IoT
E
stack, this section organizes 23 representativRe frameworks into five distinct layers:
P
perception, network, processing, application, and security and governance. Each layer
N
encompasses various aspects of anomaly detection and fraud prevention.
I
E
Perception Layer: Device anLd Sensor Intelligence
C
The perception layer comprises sensors, smart cards, near-field communication
I
(NFC) modules, and bTiometric capture units that collect transaction or behavioral data
R
at its source.
A
A9 introduced an IoT-based smart card authentication model that integrates NFC re-
authentication with classifiers, including random forests, Bayesian networks, and a
multilayer perceptron. Their hybrid approach achieved 97% accuracy while reducing
false positives by 5%, demonstrating the effectiveness of on-device anomaly detection.
A20 developed digital twin replicas of banking environments equipped with IoT
sensors, achieving 92% accuracy and reducing the time to detect fraudulent transactions
from 5 minutes to 3 minutes. Additionally, edge-AI approaches improved energy
efficiency, as reported by A21, with edge-based deep learning models decreasing
transmission load by 32% compared to cloud-only inference.
These studies illustrate that perception-layer frameworks significantly enhance real-
time responsiveness and contextual sensing. However, challenges remain, including
sensor heterogeneity, spoofing threats, and limited cryptographic capabilities in low-
power devices.
Network Layer: Communication and Fog-Based Security
At the network layer, IoT data is transmitted through protocols such as Wi-Fi, 5G,
or low-power wide-area networks (LPWAN) to fog or cloud nodes for analysis.
Network anomalies often indicate distributed denial-of-service (DDoS) or injection

ACCAERPTTICEDLE M IANN PURSECSRSIPT
attacks, which can adversely affect payment gateways. A10 developed a fog computing
framework specifically designed to mitigate DDoS attacks in blockchain-IoT systems,
achieving a 27% reduction in latency and a 98.6% throughput. A5 introduced IoT-
GRAF, a graph-learning-based anomaly-detection model that integrates sensor and
communication data into a multimodal graph. This model, optimized for fog-computing
environments, improved the F1-score by 22% compared to single-modal baselines. A12
further extended this concept by implementing federated intrusion detection across
heterogeneous networks, thereby demonstrating high scalability and robustness against
adversarial attacks. Collectively, these frameworks provide compelling evidence that
fog computing and graph-based methodologies significantly reduce network-layer
delays and improve contextual anomaly detection. Nonetheless, challenges related to
communication overhead, stemming from frequent gradient exchanges and
synchronization, remain a significant area for further exploration.
Processing Layer: Distributed and AI-Driven Fraud Analytics
The processing layer encompasses the computational intelligence that detects
anomalies, learns behavioral patterns, and makes real-time decisions. A7 integrated
federated learning (FL) and split learning (SL) to ensure data privacy while facilitating
collaborative anomaly detection across IoT nodes. STheir system achieved 98.8%
S
accuracy and reduced communication costs by 35% compared to centralized models.
E
A8 introduced FedGroup, a group-based FL aRlgorithm that achieved 99.89% accuracy
P
with a remarkably low false-positive rate of 0.02% in smart home anomaly detection.
N
A6 evaluated the performance of FedAvg, FedProx, and FedOpt within the Flower
I
framework, attaining 99.94% acc uracy on both the UNSW-NB15 and credit card
E
datasets. A1 combined enseLmble deep neural networks and clustering in an IoT
C
environment to effectively detect fraudulent transactions, achieving precision and recall
I
rates above 96%. T
R
These models demonstrate how federated and ensemble learning can surpass static
A
rule-based systems, enabling adaptive and privacy-compliant analytics. Nevertheless,
their success hinges on adequate device participation and stable communication
bandwidth, emphasizing the importance of lightweight model aggregation.
Application Layer: Contextual and Transactional Anomaly Detection
At the application layer, outputs from lower levels are contextualized for end-users,
banks, and payment processors. A22 applied anomaly-detection techniques to IoT-
based financial transaction datasets to identify abnormal behavior, achieving a precision
of 95% and an F1 score of 0.94. A18 developed a multi-layer perceptron that
incorporates federated learning for card fraud detection, achieving 98% accuracy while
promoting fairness across clients. A19 developed an IoT-based transaction-monitoring
application that provides real-time alerts and processes 10,000 transactions per second
with minimal delay. A20 further showcased digital-twin-assisted monitoring interfaces
that dynamically visualize fraudulent events. Although these frameworks enhance
usability and decision-making, they must still address challenges related to
interpretability and cross-platform integration to facilitate widespread deployment.
Security and Governance Layer: Blockchain and Regulatory Compliance

ACCAERPTTICEDLE M IANN PURSECSRSIPT
The security and governance layer ensures integrity, transparency, and trust by
applying cryptographic and regulatory controls. A3 introduced NormaChain, a
blockchain-based, autonomous transaction settlement system that employs a three-layer
sharded ledger and decentralized, public-key, searchable encryption. This framework
achieved a throughput of 113 transactions per second and 100% supervision accuracy,
effectively addressing concerns related to both privacy and legitimacy.
A2 advocated extending the Payment Card Industry Data Security Standard (PCI
DSS) to cover IoT-based payments, highlighting the need for lightweight encryption
and device compliance. Additionally, A15 presented a secure IoT anomaly framework
that leverages homomorphic encryption and distributed ledgers, achieving 99%
accuracy while reducing energy consumption by 18%.
Complementary studies, such as those by A4, emphasize the importance of
integrating artificial intelligence (AI), machine learning (ML), and data science
governance to improve explainability and accountability. Together, these research
efforts illustrate that blockchain and privacy-preserving mechanisms provide robust,
auditable trust anchors for IoT financial systems. Nonetheless, they introduce
computational overheads that must be effectively managed through sharding, Practical
Byzantine Fault Tolerance (PBFT) consensus, and lightweight cryptography.
S
S
Cross-Layer Synthesis
E
Mapping the frameworks across the layRered IoT architecture reveals complex
P
interdependencies among the functions of sensing, communication, processing, and
N
governance. The sensing capabilities at the perception layer establish the contextual
I
foundation necessary for anomaly detection at the network layer. At the same time,
E
processing-layer federated leLarning (FL) models rely on secure governance and
C
blockchain-based trust mechanisms to uphold data integrity and privacy. Frameworks
I
such as NormaChain Tand digital twin-enabled architecture illustrate how integrating
R
edge analytics with blockchain can enhance real-time visualization, transparency, and
A
coordination across multiple layers. The most effective systems exhibit vertical
interoperability, linking the perception layer to governance through standardized
protocols, privacy-aware computation, and auditable intelligence.
Despite these advances, important challenges remain, particularly the
communication and energy overheads of synchronizing distributed learning with
blockchain-supported governance, the persistence of heterogeneous non-standard
datasets, and the limited alignment of many frameworks with compliance-oriented
explainability and auditability requirements.
4. Results
4.1 Study Characteristics and Distribution
Table 11 reveals a globally diversified research landscape in IoT-based fraud
detection frameworks. The Asia-Pacific region accounts for 43% of studies, led by
India, China, Malaysia, and South Korea, where IoT-enabled financial systems,
federated learning, and edge computing have gained traction. These focus on real-time
fraud analytics and mobile payment security, aligned with the region's digital economy
growth. Europe (26%) emphasizes regulatory and privacy-oriented frameworks,
focusing on GDPR-compliant mechanisms and blockchain-based trust architectures.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
North American research (22%) from the US and Canada features methodological
sophistication, including adversarial resilient architectures and deep federated models.
Emerging regions (9%) demonstrate strategic importance through IoT-driven digital
banking and mobile fraud-prevention mechanisms, indicating an expanding research
frontier.
Institutional  distribution  indicates  a  strong  predominance  of  universities  and
research institutes (78%), underscoring the field's academic and exploratory nature,
primarily focused on developing new conceptual frameworks and testing  proof-of-
concept prototypes. While industry and collaborative laboratories account for a smaller
fraction (22%), they emphasize the application of IoT security, real-time analytics, and
commercial FinTech deployment, thus bridging the gap between theoretical innovation
and operational necessities in banking and e-commerce. This equilibrium between
academic inquiry and industrial experimentation reflects a maturing research ecosystem
advancing from prototype development to scalable, real-world deployment.
The  analysis  of  publisher  distribution  reveals  key  dissemination  patterns.
Institutional and regional journals (44%) dominate, showing localized IoT-FinTech
research growth in Asia and Africa, with a focus on digital twin banking and IoT fraud
frameworks. IEEE publications (26%) provide technical benchmarks in IoT architecture
and blockchain security. Wiley (13%) contributes reseSarch on fog-blockchain models,
S
while MDPI (9%) focuses on open-access and federated learning. Springer (4%) and
E
Elsevier (4%) address theoretical foundations Rthrough governance frameworks and AI-
P
IoT convergence.

N

I
Table 11: Summary of Study  Characteristics and Publication Distribution
E
L
Sub-Category /
|           |                    | C   | No. of  Percentage  |     | Key Research Themes /  |     |     |
| --------- | ------------------ | --- | ------------------- | --- | ---------------------- | --- | --- |
| Category  | Region / JIournal  |     |                     |     |                        |     |     |
T
|     |     |     | Studies  | (%)  | Focus  |     |     |
| --- | --- | --- | -------- | ---- | ------ | --- | --- |
GrouRp
A
|     |               |     |     |     | IoT-enabled      |            | fraud   |
| --- | ------------- | --- | --- | --- | ---------------- | ---------- | ------- |
|     |               |     |     |     | detection,       | federated  | &       |
|     | Asia-Pacific  |     | 10  | 43  |                  |            |         |
|     |               |     |     |     | edge  learning,  |            | mobile  |
payments.
Privacy-preserving
|     |         |     |     |     | architectures,  |     | GDPR  |
| --- | ------- | --- | --- | --- | --------------- | --- | ----- |
|     | Europe  |     | 6   | 26  |                 |     |       |
Geographic
|     |     |     |     |     | compliance,  | blockchain  |     |
| --- | --- | --- | --- | --- | ------------ | ----------- | --- |
Distribution
trust.
|     |                |     |     |     | Distributed  | learning,    |     |
| --- | -------------- | --- | --- | --- | ------------ | ------------ | --- |
|     | North America  |     | 5   | 22  | adversarial  | resilience,  |     |
scalable IoT frameworks.
|                | Africa (Emerging     |     |     |     | IoT-driven                 | FinTech    | and  |
| -------------- | -------------------- | --- | --- | --- | -------------------------- | ---------- | ---- |
|                |                      |     | 2   | 9   |                            |            |      |
|                | Regions)             |     |     |     | banking fraud prevention.  |            |      |
|                |                      |     |     |     | Core  theoretical          |            | and  |
| Institutional  | Universities &       |     |     |     | framework-driven           |            | IoT– |
|                |                      |     | 18  | 78  |                            |            |      |
| Context        | Research Institutes  |     |     |     | CNP  fraud                 | detection  |      |
research.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Sub-Category /
|     | No. of  | Percentage  | Key Research Themes /  |     |     |
| --- | ------- | ----------- | ---------------------- | --- | --- |
Category  Region / Journal
|     | Studies  | (%)  | Focus  |     |     |
| --- | -------- | ---- | ------ | --- | --- |
Group
Applied IoT security, data
Industry /
|     | 5   | 22  | analytics,  | and  | FinTech  |
| --- | --- | --- | ----------- | ---- | -------- |
Collaborative Labs
deployment studies.
IoT–FinTech
| Institutional /  |     |     | frameworks,  | digital  | twin  |
| ---------------- | --- | --- | ------------ | -------- | ----- |
10  44
| Regional Journals  |     |     | banking,  | regional  | fraud  |
| ------------------ | --- | --- | --------- | --------- | ------ |
models.
|     |     |     | IoT  architecture,  |     | edge  |
| --- | --- | --- | ------------------- | --- | ----- |
IEEE (Journals &
|     | 6   | 26  | computing,  | blockchain- |     |
| --- | --- | --- | ----------- | ----------- | --- |
Conferences)
enabled fraud detection.
|              |     |     | Fog–blockchain  |      | hybrid  |
| ------------ | --- | --- | --------------- | ---- | ------- |
| Wiley (ETT)  | 3   | 13  | frameworks      | for  | smart-  |
Publisher  /
Journal  contract security.
Group
|     |     |     | Open-access  | federated  |     |
| --- | --- | --- | ------------ | ---------- | --- |
MDPI (Sensors,
S
|               | 2   | 9   | learning                   | and  | privacy- |
| ------------- | --- | --- | -------------------------- | ---- | -------- |
| Electronics)  |     | S   |                            |      |          |
|               |     | E   | preserving IoT analytics.  |      |          |
R
Federated governance and
P
| Springer (JNSM)  | 1   | 4   | privacy-aware  |     | anomaly  |
| ---------------- | --- | --- | -------------- | --- | -------- |
N
detection.
I

|     | E   |     | AI-IoT  | convergence,  |     |
| --- | --- | --- | ------- | ------------- | --- |
Elsevier (CompLuter
|     | 1   | 4   | anomaly  | detection,  | and  |
| --- | --- | --- | -------- | ----------- | ---- |
C
Networks, FGCS)
I financial data analytics.
T

| Total  R | 23  | 100%  |     |     |     |
| -------- | --- | ----- | --- | --- | --- |
A
4.2 Overview of Reviewed Frameworks and Analytical Structure
This review organizes the examined studies by architectural paradigm, IoT layer
involvement,  performance  focus,  and  coverage  of  research  questions,  enabling  a
systematic identification of strengths, limitations, and research gaps in IoT-enabled
CNP fraud detection. The literature encompasses a wide range of approaches, including
machine learning-driven fraud detection, edge- and fog-assisted analytics, distributed
and federated intelligence, blockchain-supported governance, and hybrid multi-layer
IoT architectures. While these studies collectively highlight the increasing importance
of  IoT  ecosystems  in  real-time  fraud  detection,  they  differ  significantly  in  their
evaluation rigor, deployment assumptions, and system-level integration. Consequently,
direct comparisons based solely on reported accuracy or latency metrics are inadequate
for assessing their practical relevance in CNP transaction environments.
To address this challenge, the analysis in this section adopts a research-question-
driven categorization strategy. Each study is examined with respect to four analytical
dimensions aligned with the study’s research questions:
(I).  performance benchmarking and evaluation metrics (RQ1),
(II). distributed and privacy-preserving intelligence (RQ2),
(III). design principles for efficiency, adaptability, and resilience (RQ3), and

ACCAERPTTICEDLE M IANN PURSECSRSIPT
(IV).  integration into unified, multi-layer IoT-CNP frameworks (RQ4).

Table 12 operationalizes this categorization by mapping each reviewed study to its
primary analytical paradigm, dominant IoT layer(s), real-time orientation, privacy/trust
mechanism, application context, and explicit research-question coverage. This mapping
enables cross-sectional traceability across Sections 4 and 5, ensuring that subsequent
discussions on application scenarios, performance evaluation, distributed learning, and
framework synthesis are grounded in clearly identified evidence.

Table 12: Analysis of study categorization and research question coverage.
Distributed
|     |     |     | Privacy /  |     |     |     | Design  | Framework  |
| --- | --- | --- | ---------- | --- | --- | --- | ------- | ---------- |
Primary  Key IoT  Real-Time  Application Performance  / Privacy
| Code  |     |     | Trust  |     |     |     | Principles Integration  |     |
| ----- | --- | --- | ------ | --- | --- | --- | ----------------------- | --- |
Paradigm  Layer(s)  Orientation  Context  Focus (RQ1)  Focus
|     |     |     | Mechanism  |     |     |     | (RQ3)  | (RQ4)  |
| --- | --- | --- | ---------- | --- | --- | --- | ------ | ------ |
(RQ2)
| ML-based   |              |            |       | IoT credit  |     |     |     |     |
| ---------- | ------------ | ---------- | ----- | ----------- | --- | --- | --- | --- |
|            | Analytics,   | Near real- |       |             |     |     |     |     |
| A1  fraud  |              |            | None  | card fraud  | ✓   | –   | ✓   | –   |
|            | Application  | time       |       |             |     |     |     |     |
| detection  |              |            |       | detection   |     |     |     |     |
Device-Slevel Smart card
| IoT device  | Perception,  |            |            |      |     |     |     |     |
| ----------- | ------------ | ---------- | ---------- | ---- | --- | --- | --- | --- |
| A2          |              | Real-time  | securSity  | IoT  | –   | –   |     | –   |
✓
| security  | Network  |     | E      |           |     |     |     |     |
| --------- | -------- | --- | ------ | --------- | --- | --- | --- | --- |
|           |          |     | (NFC)  | payments  |     |     |     |     |
R
| Compliance- |                         | P   |          |             |     |     |     |     |
| ----------- | ----------------------- | --- | -------- | ----------- | --- | --- | --- | --- |
|             | Governance, Near rea l- |     | PCI DSS  | Secure IoT  |     |     |     |     |
N
| A3  driven    |           |        |             |           | –   | –   | ✓   | ✓   |
| ------------- | --------- | ------ | ----------- | --------- | --- | --- | --- | --- |
|               | Security  | timIe  | compliance  | payments  |     |     |     |     |
| architecture  |           |        |             |           |     |     |     |     |
E
|     | L   |     |     | Privacy- |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- |
C
| Fog +  | Edge,  | Near real- | Data locality aware IoT  |     |     |     |     |     |
| ------ | ------ | ---------- | ------------------------ | --- | --- | --- | --- | --- |
I
| A4          | T                |     |       |          | ✓   | ✓   | ✓   | ✓   |
| ----------- | ---------------- | --- | ----- | -------- | --- | --- | --- | --- |
| Blockchain  | Governance time  |     | (FL)  | anomaly  |     |     |     |     |
R
detection
A
Privacy-
| FL + SL      |             |            | Federated +  |             |     |     |     |     |
| ------------ | ----------- | ---------- | ------------ | ----------- | --- | --- | --- | --- |
|              | Analytics,  | Near real- |              | preserving  |     |     |     |     |
| A5  anomaly  |             |            | Split        |             | ✓   | ✓   | ✓   | –   |
|              | Edge        | time       |              | IoT         |     |     |     |     |
| detection    |             |            | Learning     |             |     |     |     |     |
analytics
| Federated  |             |            |               | DDoS &      |     |     |     |     |
| ---------- | ----------- | ---------- | ------------- | ----------- | --- | --- | --- | --- |
|            | Analytics,  | Near real- | Blockchain    |             |     |     |     |     |
| A6  IDS    |             |            |               | fraud       | ✓   | ✓   | ✓   | –   |
|            | Edge        | time       | immutability  |             |     |     |     |     |
| (FedAvg)   |             |            |               | mitigation  |     |     |     |     |
Adaptive
| Multi-agent  | Edge,      |            |           |            |     |     |     |     |
| ------------ | ---------- | ---------- | --------- | ---------- | --- | --- | --- | --- |
| A7           |            | Real-time  | Implicit  | financial  | ✓   | –   | ✓   | ✓   |
| AI-IoT       | Analytics  |            |           |            |     |     |     |     |
services
IoT
| Federated  | Analytics,  | Near real- | Model         |            |     |     |     |     |
| ---------- | ----------- | ---------- | ------------- | ---------- | --- | --- | --- | --- |
| A8         |             |            |               | intrusion  |     |     |     | –   |
|            |             |            |               |            | ✓   | ✓   | ✓   |     |
| IDS        | Edge        | time       | sharing only  |            |     |     |     |     |
detection
| Hybrid        | Analytics,   | Near real- | Federated    | Metaverse     |     |     |     |     |
| ------------- | ------------ | ---------- | ------------ | ------------- | --- | --- | --- | --- |
| A9            |              |            |              |               | ✓   | ✓   | ✓   | –   |
| Fuzzy + FL    | Application  | time       | learning     | IoT security  |     |     |     |     |
| DL intrusion  |              |            | Adversarial  | Real-time     |     |     |     |     |
| A10           | Analytics    | Real-time  |              |               | ✓   | –   | ✓   | –   |
| detection     |              |            | resilience   | IoT           |     |     |     |     |

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Distributed
|     |     |     |     | Privacy /  |     |     |     | Design  | Framework  |
| --- | --- | --- | --- | ---------- | --- | --- | --- | ------- | ---------- |
Primary  Key IoT  Real-Time  Application Performance  / Privacy
| Code  |     |     |     | Trust  |     |     |     | Principles Integration  |     |
| ----- | --- | --- | --- | ------ | --- | --- | --- | ----------------------- | --- |
Paradigm  Layer(s)  Orientation  Context  Focus (RQ1)  Focus
|     |     |     |     | Mechanism  |     |     |     | (RQ3)  | (RQ4)  |
| --- | --- | --- | --- | ---------- | --- | --- | --- | ------ | ------ |
(RQ2)
intrusion
detection
IoT
| ML-based      | Network,   |     | Near real- |       |          |     |     |     |     |
| ------------- | ---------- | --- | ---------- | ----- | -------- | --- | --- | --- | --- |
| A11           |            |     |            | None  | anomaly  |     | –   |     | –   |
|               |            |     |            |       |          | ✓   |     | ✓   |     |
| IoT security  | Analytics  |     | time       |       |          |     |     |     |     |
detection
| Deep  |     |     |     |     | IoT  |     |     |     |     |
| ----- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
A12  learning  Analytics  Real-time  None  anomaly  ✓  –  ✓  –
| ensembles  |     |     |     |     | streams    |     |     |     |     |
| ---------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
| AI-driven  |     |     |     |     | Financial  |     |     |     |     |
Near real-
| A13  fraud  | Application  |     |     | None  | fraud  | ✓   | –   | –   | –   |
| ----------- | ------------ | --- | --- | ----- | ------ | --- | --- | --- | --- |
time
| detection  |             |     |            |            | profiling    |     |     |     |     |
| ---------- | ----------- | --- | ---------- | ---------- | ------------ | --- | --- | --- | --- |
| Federated  | Analytics,  |     | Near real- | Federated  | Credit card  |     |     |     |     |
| A14        |             |     |            |            |              | ✓   | ✓   | ✓   | –   |
| MLP        | Edge        |     | time       | learning   | fraud        |     |     |     |     |
S
| IoT  |     |     |     |     | Transaction  |     |     |     |     |
| ---- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
S
Near real-
| A15  transaction  | Application  |     |     | NEone  | anomaly  | ✓   | –   | –   | –   |
| ----------------- | ------------ | --- | --- | ------ | -------- | --- | --- | --- | --- |
time
| analytics  |     |     |     | R   | detection  |     |     |     |     |
| ---------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
P
|     |     |     |     |     | Real-time  |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
N
| Digital twin  | Edge,      |     |             |           |             |     |     |     |     |
| ------------- | ---------- | --- | ----------- | --------- | ----------- | --- | --- | --- | --- |
| A16           |            |     | ReIal-time  | Implicit  | fraud       | ✓   | –   | ✓   | ✓   |
| + IoT         | Analytics  |     |             |           |             |     |     |     |     |
|               |            |     | E           |           | monitoring  |     |     |     |     |
L
| Edge AI +  |            | C   |            |           | Financial  |     |     |     |     |
| ---------- | ---------- | --- | ---------- | --------- | ---------- | --- | --- | --- | --- |
| A17        | Edge, Fog  |     | Real-time  | Implicit  |            | ✓   | –   | ✓   | ✓   |
I
| cloud  | T   |     |     |     | analytics  |     |     |     |     |
| ------ | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
R
Unsupervised
|               | A          |     | Near real- |       | Financial  |     |     |     |     |
| ------------- | ---------- | --- | ---------- | ----- | ---------- | --- | --- | --- | --- |
| A18  anomaly  | Analytics  |     |            | None  |            | ✓   | –   | ✓   | –   |
|               |            |     | time       |       | IoT fraud  |     |     |     |     |
detection
AI-IoT
| AI–IoT       |            |     | Near real- |       |           |     |     |     |     |
| ------------ | ---------- | --- | ---------- | ----- | --------- | --- | --- | --- | --- |
| A19          | Analytics  |     |            | None  | decision  | ✓   | –   | ✓   | ✓   |
| integration  |            |     | time       |       |           |     |     |     |     |
systems
Graph-
| Graph-based  | Analytics,  |     | Near real- |       | based    |     |     |     |     |
| ------------ | ----------- | --- | ---------- | ----- | -------- | --- | --- | --- | --- |
| A20          |             |     |            | None  |          | ✓   | –   | ✓   | –   |
| learning     | Network     |     | time       |       | anomaly  |     |     |     |     |
detection
IoT e-
| Blockchain  |             |     | Near real- | Blockchain  |           |     |     |     |     |
| ----------- | ----------- | --- | ---------- | ----------- | --------- | --- | --- | --- | --- |
| A21         | Governance  |     |            |             | commerce  | –   | ✓   | ✓   | ✓   |
| settlement  |             |     | time       | trust       |           |     |     |     |     |
settlement
IoT
| Group-based  | Analytics,  |     | Near real- | Privacy-  |          |     |     |     |     |
| ------------ | ----------- | --- | ---------- | --------- | -------- | --- | --- | --- | --- |
| A22          |             |     |            |           | anomaly  | ✓   | ✓   | ✓   | –   |
| FL           | Edge        |     | time       | aware FL  |          |     |     |     |     |
detection
Digital
IoT-AI fraud
| A23  | Application  |     | Real-time  | Implicit  | wallet  |     | –   | –   | –   |
| ---- | ------------ | --- | ---------- | --------- | ------- | --- | --- | --- | --- |
✓
protection
protection

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Legend: explicitly addressed (✓); not primary focus (–)
The distribution of studies within the field reveals significant patterns that deserve
attention. Primarily, research has concentrated on local or centralized performance
evaluations, typically emphasizing metrics such as detection accuracy and latency in
isolation. In contrast, there is a noticeable lack of studies focusing on distributed
intelligence and privacy preservation. Moreover, although a handful of papers suggest
design principles informed by architectural elements, these proposals often lack
formalization and systematic evaluation.
Another critical observation is the limited number of studies that investigate end-to-
end framework integration across different IoT layers and transaction stages. This
reveals a gap between innovations at the component level and the comprehensive
system design necessary for practical deployment. To address these insights, a layered
analysis is warranted.
A critical distinction emerging from the reviewed literature is that many frameworks
are described as real-time in a conceptual or architectural sense, but only a subset
provides empirical evidence that they operate under genuine real-time constraints. In
several studies, the use of edge computing, streaming analytics, online learning, or IoT
S
telemetry implies time-sensitive intent, yet this is not accompanied by systematic
S
measurement of end-to-end decision latency, Emodel inference time, transaction
throughput, or sustained performance under reRalistic operational load. Accordingly, this
P
review does not treat all real-time claims as equivalent and distinguishes between
N
proposed real-time readiness and demonstrated real-time performance. Real-time
I
framing appears primarily in stud ies A14, A16, A20, and A23, but the level of
E
validation varies substantiallyL across them.
C
Also, studies differ not only in evaluation rigor and deployment assumptions, but
I
T
also in the nature of the datasets used, including credit card transaction datasets, IoT
R
intrusion dataseAts, simulated environments, smart-home anomaly datasets, and
application-specific financial telemetry. Consequently, metrics such as accuracy, F1-
score, precision, recall, and even latency cannot be directly comparable across all
studies, as they reflect different class distributions, feature spaces, attack surfaces, and
operational settings.
Specifically, Section 4.2 delves into application scenarios within real CNP contexts,
while Section 4.3 assesses performance metrics and benchmarking. Section 4.4
emphasizes distributed learning and privacy-preserving models. Finally, Sections 4.5
and 4.6 synthesize the findings, resulting in established design principles and a cohesive
multi-layer IoT-CNP framework.
4.3 Application Scenarios and Case-Study Contexts
IoT-enabled CNP fraud detection frameworks are developed and evaluated across a
wide range of operational environments, each characterized by distinct transaction
dynamics, latency constraints, privacy considerations, and deployment assumptions. A
comprehensive understanding of various application scenarios is essential for
accurately interpreting reported performance results and evaluating the feasibility of
real-world deployment. For instance, models specifically optimized for centralized e-
commerce platforms may not be directly transferable to other contexts, such as edge-
assisted mobile payment systems or federated monitoring across multiple institutions.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Table 13 summarizes the primary application scenarios and case-study contexts
addressed by the reviewed studies, mapping each group of works to its dominant IoT
context,  deployment  setting,  and  analytical  emphasis.  This  scenario-based
categorization  provides  the  empirical  foundation  for  the  subsequent  analysis  by
clarifying where and how different IoT-CNP fraud detection approaches operate. It also
motivates  the  differentiated  performance  evaluation  criteria  discussed  later  in  this
section, ensuring that performance metrics are interpreted relative to their intended
operational environments rather than in isolation.
Building  on  this  classification,  the  remainder  of  this  section  examines  each
application  scenario  in  turn,  highlighting  representative  case  studies,  common
architectural patterns, and context-specific challenges that influence fraud-detection
effectiveness and system scalability.

Table 13: Application Scenarios and Case-Study Contexts for IoT-Enabled CNP
Fraud Detection
S
| Application  | Representative  |     | Deployment  | Primary  |
| ------------ | --------------- | --- | ----------- | -------- |
S
IoT Context
ESetting
| Scenario  | Studies  |     |     | Analytical Focus  |
| --------- | -------- | --- | --- | ----------------- |
R
|     |     | TransacPtion  |     | Transaction-level  |
| --- | --- | ------------- | --- | ------------------ |

| E-commerce  |                | strNeams, user  |                | fraud               |
| ----------- | -------------- | --------------- | -------------- | ------------------- |
|             | A1, A17, A19,  |                 | Centralized /  |                     |
| payment     |                | bIehavior,      |                | classification and  |

|           | A22, A23  |           | cloud-based  |          |
| --------- | --------- | --------- | ------------ | -------- |
| gateways  |           | E device  |              | anomaly  |
L
|     |     | metadata  |     | detection  |
| --- | --- | --------- | --- | ---------- |
C
I
|     | T   |     |     | Low-latency  |
| --- | --- | --- | --- | ------------ |
Mobile
| Edge-assisted   | R              |                |             | detection, energy  |
| --------------- | -------------- | -------------- | ----------- | ------------------ |
|                 | AA9 A11, A20,  | devices, NFC   | Edge / fog- |                    |
| mobile and IoT  |                |                |             | efficiency,        |
|                 | A21            | sensors, edge  | assisted    |                    |
| payments        |                |                |             | adaptive           |
gateways
inference
Privacy-
Multi-
preserving
| Distributed and  | A6, A7, A8, A10, institution IoT  |                   |                |                   |
| ---------------- | --------------------------------- | ----------------- | -------------- | ----------------- |
|                  |                                   |                   | Federated /    | learning,         |
| federated fraud  | A12, A13, A16,                    | nodes,            |                |                   |
|                  |                                   |                   | collaborative  | scalability, and  |
| monitoring       | A18                               | distributed data  |                |                   |
non-IID
silos
robustness
| Blockchain- |     | IoT payment  |     | Auditability,  |
| ----------- | --- | ------------ | --- | -------------- |
supported  A2, A10, A18,  systems with  Hybrid (IoT +  trust, compliance,
| transaction and  | A3  | ledger       | blockchain)  | settlement  |
| ---------------- | --- | ------------ | ------------ | ----------- |
| auditing         |     | integration  |              | integrity   |
Framework
Multi-layer and
|                |                  |                 | Cross-layer  | integration,   |
| -------------- | ---------------- | --------------- | ------------ | -------------- |
| cross-         | A5, A6, A7, A8,  | End-to-end IoT  |              |                |
|                |                  |                 | (edge-cloud- | adaptability,  |
| ecosystem IoT  | A12, A18         | ecosystems      |              |                |
|                |                  |                 | governance)  | system-level   |
frameworks
resilience

ACCAERPTTICEDLE M IANN PURSECSRSIPT
4.3.1 E-Commerce Payment Gateway Scenarios
E-commerce payment gateways represent the most mature and widely studied
application context for IoT-enabled CNP fraud detection. As summarized in Table 13,
studies in this category (A1, A17, A19, A22, A23) primarily operate in centralized or
cloud-based environments, where high transaction volumes and diverse user behavior
necessitate robust, scalable fraud-detection mechanisms.
In these scenarios, IoT contributions are typically indirect, manifesting through
device metadata, session fingerprints, and behavioral signals captured during online
transactions. Machine learning and deep learning models dominate this context, with
performance evaluation focusing on detection effectiveness metrics such as accuracy,
precision, recall, F1-score, and false-positive rate. While many studies report strong
classification performance, they often assume stable connectivity and centralized
processing, limiting direct applicability to latency-sensitive or privacy-constrained
environments.
A key limitation in this scenario is the underutilization of edge intelligence, as most
frameworks defer inference to the cloud. This motivates the exploration of alternative
deployment models discussed in subsequent scenarios, particularly for real-time and
privacy-sensitive CNP environments.
S
4.3.2 Edge-Assisted Mobile and IoT Payment SceSnarios
E
Edge-assisted mobile and IoT payment scenRarios, highlighted in Table 13 by studies
P
such as A9, A11, A20, and A21, address the limitations of purely centralized detection
N
by introducing edge and fog-level analytics. These environments include mobile
I
wallets, NFC-enabled payments, and smart point-of-sale systems, where latency,
E
energy efficiency, and intermiLttent connectivity are critical operational constraints.
C
In this context, fraud detection models are often deployed partially or entirely at the
I
edge, enabling fasterT response times and reducing reliance on continuous cloud
R
communication. Performance evaluation extends beyond detection accuracy to include
A
end-to-end latency, inference time, and energy consumption, reflecting real-world
deployment considerations. The reviewed studies demonstrate that edge-assisted
architectures can significantly reduce response delays while maintaining acceptable
detection performance, particularly when lightweight models or adaptive inference
strategies are employed.
However, edge-assisted scenarios also introduce challenges related to resource
heterogeneity and model maintenance, underscoring the need for adaptive and
distributed learning mechanisms explored in Section 4.5.
4.3.3 Distributed and Federated Fraud Monitoring Scenarios
Distributed and federated fraud monitoring scenarios constitute a rapidly growing
application domain, as reflected in Table 13 (A6, A7, A8, A10, A12, A13, A16, A18).
These scenarios are characterized by multi-institution collaboration, where data silos
across banks, merchants, and payment processors prevent centralized data aggregation
due to privacy, regulatory, or competitive constraints.
Federated and distributed learning frameworks enable collaborative model training
through parameter sharing rather than raw-data exchange. Performance evaluation in
this context emphasizes scalability, communication overhead, convergence stability,
and robustness to non-independent and identically distributed (non-IID) data, in

ACCAERPTTICEDLE M IANN PURSECSRSIPT
addition to traditional detection metrics. Empirical results indicate that federated
approaches can achieve near-centralized performance while preserving data locality,
particularly when heterogeneity-aware aggregation strategies are employed.
These scenarios highlight a fundamental shift in CNP fraud detection, from isolated,
institution-specific models toward ecosystem-level intelligence, laying the groundwork
for the privacy-preserving architectures discussed in Section 4.5.
4.3.4 Blockchain-Supported Transaction and Auditing Scenarios
Blockchain-supported scenarios, identified in Table 13 by studies such as A2, A3,
A10, and A18, extend IoT-enabled CNP fraud detection beyond real-time decisioning
to include auditability, trust, and compliance. In these settings, distributed ledgers are
used to record transaction events, model updates, and fraud alerts in an immutable,
verifiable manner.
The primary analytical focus in this scenario shifts from detection accuracy alone to
governance-oriented metrics, including audit latency, transaction throughput, and
provenance completeness. Blockchain integration enhances trustworthiness and
forensic accountability, particularly in regulated environments requiring post-incident
investigation and dispute resolution. However, these benefits often come at the cost of
increased coordination overhead and confirmationS delays, necessitating careful
architectural trade-offs. S
E
As such, blockchain-supported scenarios are best viewed as complementary to AI-
R
driven detection, providing governance andP trust support rather than replacing real-time
analytics. N
I
4.3.5 Multi-layer and Cross-EcEosystem IoT Scenarios
L
Multi-layer and cross-ecCosystem IoT scenarios, as outlined in Table 13 from studies
A5, A6, A7, A8, A12, andI A18, broaden the scope of IoT-enabled CNP fraud detection.
T
These scenarios iRnvolve collaborative environments with multiple stakeholders,
A
including merchants, payment processors, and financial institutions, and distribute fraud
detection logic across different layers: perception, edge/fog, analytics, and governance.
The focus shifts from transaction-level accuracy to system-level coordination
metrics, such as communication overhead, robustness to non-IID data, scalability, and
cross-layer latency. Federated and group-based learning frameworks (A6, A8, A12,
A18) enable model training without centralizing sensitive data, while hybrid approaches
(A7) address device heterogeneity. Graph-based models (A5) enhance awareness by
capturing relationships among entities.
Performance evaluation emphasizes collaboration efficiency and resilience,
considering metrics such as coordination latency, client participation stability, and
adaptability to evolving fraud patterns as crucial indicators alongside detection
performance.
Ultimately, these multi-layer, cross-ecosystem IoT scenarios represent system-of-
systems deployments in which integrated, privacy-preserving intelligence emerges.
This informs the unified multi-layer IoT-CNP framework presented in Section 4.6,
which combines distributed analytics, adaptive learning, and governance mechanisms
into a cohesive reference architecture.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
4.3.6 Synthesis of Application Scenarios
The application scenarios in Table 13 show that IoT-enabled CNP fraud frameworks
operate  under  distinct  deployment  constraints.  Centralized  e-commerce  systems
prioritize transaction-scale detection accuracy, edge-assisted environments emphasize
latency and operational efficiency, distributed monitoring scenarios foreground privacy
and  coordination,  and  blockchain-supported  architectures  strengthen  trust  and
governance. These differences indicate that performance claims must be interpreted in
relation to deployment context rather than through a one-size-fits-all benchmarking
lens.
4.4 Performance Evaluation of Frameworks
Performance evaluation in the reviewed literature clusters around four recurring
dimensions: detection effectiveness, real-time responsiveness, scalability and resource
efficiency, privacy, trust, and governance assurances. Because the included studies
differ  substantially  in  datasets,  application  contexts,  deployment  assumptions,  and
reporting completeness, the synthesis is presented as a comparative evidence map rather
than as a strict meta-analytic ranking.
Table  14  summarizes,  where  reported,  the  principal  benchmarking  dimensions
S
across  studies.  The  findings  indicate  that  predictive  effectiveness  metrics  are
S
predominant across various scenarios, whereas rEeporting on real-time responsiveness
| and system-level scalability remains inconsistent. Studies explicitly focused on real- |     |     | R   |     |     |     |
| -------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
P
time applications (A14, A16, A20, A23) tend to emphasize latency and deployment

N
metrics. Conversely, federated studies (A6, A7, A8, A12, A18) incorporate additional
I
scalability considerations, notably  communication overhead and client heterogeneity.
E
Blockchain-oriented  studies L(A10,  A3)  primarily  focus  on  trust  and  auditability,
C
requiring throughput and confirmation latency metrics to support claims about real-
I
T
world deployment.
R
|     | A   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Table 14: Performance Evaluation Metrics by Study and Application Scenario
RT
|          |            |               |          | Scale       | Priv./Trust  |     |
| -------- | ---------- | ------------- | -------- | ----------- | ------------ | --- |
| Co Scena | Primary    | Eff. Metrics  | Metrics  |             |              | Bas |
|          |            |               |          | Metrics     | Metrics      |     |
| de  rio  | Technique  | (examples)    | (example |             |              | is  |
|          |            |               |          | (examples)  | (examples)   |     |
s)
Inference
|         | RF/DNN/S  | Acc, Prec,  |           |             |     |     |
| ------- | --------- | ----------- | --------- | ----------- | --- | --- |
|         |           |             | time,     | Model       |     |     |
| A1  S1  | VM        | Rec, F1,    |           |             | -   | T   |
|         |           |             | decision  | complexity  |     |     |
|         | ensemble  | AUC         |           |             |     |     |
delay
Control
Process
|         | PCI DSS    | coverage,   |          | Operational  | Compliance  |     |
| ------- | ---------- | ----------- | -------- | ------------ | ----------- | --- |
| A2  S4  |            |             | timing   |              |             | E   |
|         | extension  | compliance  |          | overhead     | assurance   |     |
(if any)
maturity
Confirmat
|         | Blockchain  |               |      | Throughput/   | Auditability,  |     |
| ------- | ----------- | ------------- | ---- | ------------- | -------------- | --- |
| A3  S4  |             | System-level  | ion  |               |                | E   |
|         | + SC + SE   |               |      | TPS, storage  | encryption     |     |
latency

ACCAERPTTICEDLE M IANN PURSECSRSIPT
RT
|          |            |               |          | Scale       | Priv./Trust  |     |
| -------- | ---------- | ------------- | -------- | ----------- | ------------ | --- |
| Co Scena | Primary    | Eff. Metrics  | Metrics  |             |              | Bas |
|          |            |               |          | Metrics     | Metrics      |     |
| de  rio  | Technique  | (examples)    | (example |             |              | is  |
|          |            |               |          | (examples)  | (examples)   |     |
s)
|                                     | DL +        |               |            | Compute/sca  |     |     |
| ----------------------------------- | ----------- | ------------- | ---------- | ------------ | --- | --- |
| A4  S2                              | predictive  | Acc/F1        | -          | le (if       | -   | T   |
|                                     | analytics   |               |            | discussed)   |     |     |
|                                     | GNN +       | Acc/F1/AUC;   |            |              |     |     |
|                                     |             |               | Inference  | Graph size   |     |     |
| A5  S2/S3* multimodal intrusion/ano |             |               |            |              | -   | T   |
|                                     |             |               | time       | scalability  |     |     |
|                                     | fusion      | maly metrics  |            |              |     |     |
Round
|         |            | Acc/F1/AUC  |         | #clients,  | Data                  |     |
| ------- | ---------- | ----------- | ------- | ---------- | --------------------- | --- |
|         | Federated  |             | time,   |            |                       |     |
| A6  S3  |            | (task-      |         | comm       | locality/privacy E/T  |     |
|         | learning   |             | update  |            |                       |     |
|         |            | dependent)  |         | rounds     | discussion            |     |
interval
|         |             | Acc/F1/AUC;  |            | Comm cost + Privacy- |             |     |
| ------- | ----------- | ------------ | ---------- | -------------------- | ----------- | --- |
|         | FL + Split  |              | Train/infe |                      |             |     |
| A7  S3  |             | anomaly      |            | split                | preserving  | E   |
|         | learning    |              | r time     |                      |             |     |
|         |             | metrics      |            | overhead             | training    |     |
Comm  S
S
|         |           | Acc/F1/AUC;  |         | E rounds;    |                |     |
| ------- | --------- | ------------ | ------- | ------------ | -------------- | --- |
|         |           |              | Round   |              | Privacy-aware  |     |
| A8  S3  | FedGroup  | anomaly      | Rgroup  |              |                | E   |
|         |           |              | timPe   |              | FL             |     |
|         |           | metrics      |         | heterogeneit |                |     |

N
y
I

NFC
E
|         | NFC +  | Acc, Prec,  | Verificati           | Device  |                 |      |
| ------- | ------ | ----------- | -------------------- | ------- | --------------- | ---- |
| A9  S2  |        | L           |                      |         | assurance/devic | E/T  |
|         | RF/BN  | RCec, F1    | on latency overhead  |         |                 |      |
|         |        | I           |                      |         | e trust         |      |
T
RDetection
|     |     |     | Fog  | Fog  |     |     |
| --- | --- | --- | ---- | ---- | --- | --- |
A
|         | Blockchain rate/FPR  |            |           |               | Integrity/audita |      |
| ------- | -------------------- | ---------- | --------- | ------------- | ---------------- | ---- |
| A10 S4  |                      |            | response  | scalability,  |                  | E/T  |
|         | + fog                | (security  |           |               | bility           |      |
|         |                      |            | time      | node load     |                  |      |
task)
Acc/F1/AUC; Decision
|         | DL +         |          |              | Resource   |     |     |
| ------- | ------------ | -------- | ------------ | ---------- | --- | --- |
| A11 S2  |              | anomaly  | latency (if  |            | -   | T   |
|         | multi-agent  |          |              | footprint  |     |     |
|         |              | metrics  | measured)    |            |     |     |
Comm
rounds,
|         | FedAvg  | DR/TPR,  | Round    |         | Privacy by   |      |
| ------- | ------- | -------- | -------- | ------- | ------------ | ---- |
| A12 S3  |         |          |          | client  |              | E/T  |
|         | IDS     | FPR, F1  | latency  |         | design (FL)  |      |
heterogeneit
y
Acc/F1;
|         |                     |     | Update    |            | Privacy by   |      |
| ------- | ------------------- | --- | --------- | ---------- | ------------ | ---- |
| A13 S3  | Fuzzy + FL anomaly  |     |           | Comm cost  |              | E/T  |
|         |                     |     | interval  |            | design (FL)  |      |
metrics
|     | CNN– | DR/TPR,  | Latency /  | Energy  |     |     |
| --- | ---- | -------- | ---------- | ------- | --- | --- |
Adversarial
| A14 S2  | LSTM +  | FPR, F1,  | time-to- | efficiency,  |     | E   |
| ------- | ------- | --------- | -------- | ------------ | --- | --- |
robustness
|     | resilience  | AUC  | detect  | model size  |     |     |
| --- | ----------- | ---- | ------- | ----------- | --- | --- |

ACCAERPTTICEDLE M IANN PURSECSRSIPT
RT
Scale  Priv./Trust
| Co Scena | Primary  | Eff. Metrics  | Metrics  |     |     | Bas |
| -------- | -------- | ------------- | -------- | --- | --- | --- |
Metrics  Metrics
| de  rio  | Technique  | (examples)  | (example |     |     | is  |
| -------- | ---------- | ----------- | -------- | --- | --- | --- |
(examples)  (examples)
s)
|             | RF/SVM     | Acc, Prec,      | Inference  | Model         |     |      |
| ----------- | ---------- | --------------- | ---------- | ------------- | --- | ---- |
| A15 S1/S2*  |            |                 |            |               | -   | T    |
|             | ensembles  | Rec, F1         | time       | complexity    |     |      |
|             | Deep       | Acc/F1          |            |               |     |      |
|             |            |                 | Stream     | Throughput,   |     |      |
| A16 S2      | models +   | (multi-class),  |            |               | -   | E/T  |
|             |            |                 | latency    | compute load  |     |      |
|             | ensembles  | macro-F1        |            |               |     |      |
Acc/F1/AUC; Decision
AI rules +
| A17 S1  |     | profiling  | time (if  | -   | -   | T   |
| ------- | --- | ---------- | --------- | --- | --- | --- |
NNs
|     |     | quality     | any)  |       |     |     |
| --- | --- | ----------- | ----- | ----- | --- | --- |
|     |     | Acc, Prec,  |       | Comm  |     |     |
Round  Privacy by
| A18 S3  | FL MLP  | Rec, F1,  |     | rounds/#clie |     | E/T  |
| ------- | ------- | --------- | --- | ------------ | --- | ---- |
time  design (FL)
|     |     | AUC  |     | nts  |     |     |
| --- | --- | ---- | --- | ---- | --- | --- |
Inference
| A19 S1  | DT/GB  | Acc/F1/AUC  |     | -   | -   | T   |
| ------- | ------ | ----------- | --- | --- | --- | --- |
time
S
|     | Digital  | Acc/F1/AUC; Online  |     |     |     |     |
| --- | -------- | ------------------- | --- | --- | --- | --- |
ESdge
Monitoring/con
| A20 S2  | twin + edge detection  |     | update  | E   |     | E/T  |
| ------- | ---------------------- | --- | ------- | --- | --- | ---- |
resource use  trol reliability
|     | + online  | stability  | delay  R |     |     |     |
| --- | --------- | ---------- | -------- | --- | --- | --- |
P
E dge
N
|         | Edge AI +  |                |            | Partitioning  |     |     |
| ------- | ---------- | -------------- | ---------- | ------------- | --- | --- |
| A21 S2  |            | System-levIel  | response   |               | -   | T   |
|         | cloud/fog  |                |            | overhead      |     |     |
|         |            |                | E latency  |               |     |     |
L
ACUC, PR-
IF +
I
|         |            | T AUC,  | Inference  |     |     |     |
| ------- | ---------- | ------- | ---------- | --- | --- | --- |
| A22 S1  | autoencode |         |            | -   | -   | T   |
|         | Ranomaly   |         | time       |     |     |     |
r  A
score metrics
Real-time
|         | AI + IoT  |             |           | Edge/device  |     |      |
| ------- | --------- | ----------- | --------- | ------------ | --- | ---- |
| A23 S2  |           | Acc/F1/AUC  | decision  |              | -   | E/T  |
|         | sensors   |             |           | overhead     |     |      |
delay
Legend:  Eff.=Effectiveness;  RT=Real-time/Latency  responsiveness;
Scale=Scalability/resource efficiency; Priv/Trust=Privacy/trust indicators
Scenario clusters: (S1) E-commerce gateway, (S2) Edge-assisted mobile/IoT payments,
(S3) Distributed/Federated monitoring, (S4) Blockchain-supported auditing/settlement.
“Basis” indicates whether the metric family is Explicit (E) or Typical (T), given the
study’s stated method/focus.

The literature predominantly reports predictive performance metrics, while latency,
throughput,  coordination  costs  in  federated  settings,  and  privacy  overhead  are
comparatively  underreported,  limiting  rigorous  cross-study  comparability  and
motivating  multi-dimensional  benchmarking  beyond  accuracy  alone.  Furthermore,
substantial heterogeneity in datasets and experimental conditions means that reported
metrics (e.g., accuracy, F1, AUC, false-positive rate, throughput, latency) should not be
treated as definitive evidence of any framework’s superiority, but rather as indicative

ACCAERPTTICEDLE M IANN PURSECSRSIPT
of broad performance tendencies, evaluation practices, and recurring trade-offs across
application scenarios.
Table 15 summarizes the most common evaluation omissions across different
framework families, emphasizing the real-time constraints that are measured rather than
simply claimed. It highlights gaps in systematic evaluation across various frameworks.
Reporting latency, throughput, energy consumption, and communication costs is often
inconsistent, even when real-time deployment is claimed.

Table 15 Evaluation gaps in addressing real-time constraints across framework
families
| Framewor | Latency  | Through | Energy  | Communicat | Typical  |
| -------- | -------- | ------- | ------- | ---------- | -------- |
k family   reported  put  reported  ion cost  evaluation gap
|              | (end-to-end  | reported  | (device/ed | reported     | observed    |
| ------------ | ------------ | --------- | ---------- | ------------ | ----------- |
|              | or decision  | (TPS /    | ge cost)   | (bytes/      |             |
|              | latency)     | event     |            | rounds       |             |
|              |              | rate)     |            | /bandwidth)  |             |
| Centralized  | Low          | Rare      | Rare       | N/A          | Emphasizes  |
| / gateway    |              |           |            |              | predictive  |
S
| ML (S1)  |     |     |     |     | metrics; limited  |
| -------- | --- | --- | --- | --- | ----------------- |
S
|     |     |     | E   |     | operational      |
| --- | --- | --- | --- | --- | ---------------- |
|     |     |     | R   |     | profiling under  |
P
|     |     |     |     |     | real-time loads  |
| --- | --- | --- | --- | --- | ---------------- |
N
| Edge- | Medium  | Rare  | Low- | Low  | Reports  |
| ----- | ------- | ----- | ---- | ---- | -------- |
I

| assisted /  | (often  |     | Medium  |     | response-time  |
| ----------- | ------- | --- | ------- | --- | -------------- |
E
| mobile IoT  | partial)  | L   |     |     | proxies, but  |
| ----------- | --------- | --- | --- | --- | ------------- |
C
| payments  |     | I   |     |     | omits end-to- |
| --------- | --- | --- | --- | --- | ------------- |
T
| (S2)  |     |     |     |     | end latency and  |
| ----- | --- | --- | --- | --- | ---------------- |
R
|     | A   |     |     |     | device energy  |
| --- | --- | --- | --- | --- | -------------- |
profiling
| Federated /  | Medium        | Rare  | Rare  | Medium  | Reports         |
| ------------ | ------------- | ----- | ----- | ------- | --------------- |
| distributed  | (often        |       |       |         | collaboration   |
| monitoring   | coordination  |       |       |         | claims but      |
| (S3)         | latency)      |       |       |         | inconsistently  |
quantifies
rounds/bytes
and latency
trade-offs
| Blockchain  | Medium       | Medium  | Rare  | Medium  | Addresses trust  |
| ----------- | ------------ | ------- | ----- | ------- | ---------------- |
| -supported  | (confirmatio |         |       |         | but often        |
| governance  | n/ audit     |         |       |         | underreports     |
| (S4)        | latency)     |         |       |         | overhead under   |
realistic
transaction
volumes

Detection Effectiveness Metrics

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Predictive effectiveness is the most consistently reported performance dimension
across studies. In centralized scenarios, effectiveness is evaluated using accuracy,
precision, recall, F1-score, and AUC/ROC to distinguish fraudulent transactions (A1,
A17, A19, A22). In unsupervised settings for IoT streams (A22), performance is
assessed using anomaly-scoring metrics and detection consistency. IoT intrusion studies
(A14, A16) evaluate multi-class detection and stream accuracy, while graph
frameworks (A5) assess multi-modal fusion quality.
Implications for benchmarking (RQ1): As demonstrated in Table 14, effectiveness
metrics vary substantially across task formulations and scenarios. Consequently,
benchmarking must distinguish at minimum between (i) transaction-level fraud
classification, (ii) IoT anomaly or intrusion detection as a fraud-relevant proxy, and (iii)
hybrid monitoring and control systems. This confirms that “effectiveness” is scenario-
dependent and cannot be meaningfully compared without task-consistent metrics.
Real-Time Responsiveness and Operational Readiness
In CNP fraud detection systems that operate under real-time constraints, simply
having effective detection is not enough. The importance of real-time processing is
highlighted in studies (A14, A16, A20, A23) that focus on areas such as intrusion
detection, streaming anomaly detection, digital twin Smonitoring, and digital wallet
S
protection, as presented in Table 14. Studies’ reporting practices remain inconsistent,
E
with some using qualitative assertions of streaRming suitability, while others report only
P
partial indicators, such as inference time, without documenting complete decision
N
latency or throughput. Digital twin approaches (A20), though aligned with continuous
I
monitoring, need systematic reporti ng of update frequency and detection delay.
E
Missing real-time evaluatioLn metrics: In the studies reviewed, real-time claims were
C
rarely supported by comprehensive and operational metrics. Frequently overlooked
I
indicators include end-Tto-end decision latency (from capture to decision), throughput or
R
event processing rate (measured in transactions per second), energy consumption (per
A
inference, per round, or per device), and communication cost (in terms of bytes
exchanged, number of rounds, and bandwidth assumptions). When metrics are reported,
they are often incomplete, such as omitting the model inference time, which limits
reproducibility and impedes a fair comparison of real-time readiness across different
architectures.
Implication for benchmarking (RQ1) and design principles (RQ3): Real-time
responsiveness should be treated as a first-class evaluation dimension. At a minimum,
studies should report one or more of the following: decision latency, event processing
rate or throughput, model update interval, and time to detection. The absence of
standardized reporting of responsiveness highlights a recurring design gap in the
literature.
Scalability and Resource Efficiency
Scalability evaluation varies across paradigms due to system constraints. Edge-
assisted scenarios (S2) consider computational footprint, energy use, and deployment
feasibility. Studies on efficiency (A14, A21) address these concerns, though resource
profiling remains limited. In distributed and federated monitoring (S3), scalability
encompasses coordination metrics such as communication overhead, client
participation, convergence, and robustness to non-IID data. Federated learning studies

ACCAERPTTICEDLE M IANN PURSECSRSIPT
(A6, A12, A18, A8) and hybrid FL-SL approaches (A7) address scalability under
privacy constraints (see Table 14), though comparability requires consistent federation
metrics.
Implication for RQ2: Scalability in privacy-preserving intelligence encompasses
not only computational aspects but also organizational and coordination-related factors.
To effectively substantiate RQ2, studies focusing on federated and split-learning
methodologies must provide comprehensive reporting on both detection effectiveness
and the associated collaboration costs. These costs may include metrics such as the
number of communication rounds, bandwidth assumptions, and variations in client
heterogeneity.
Privacy, Trust, and Governance Indicators
A fundamental distinction among frameworks lies in whether their performance
evaluations extend beyond detection metrics to encompass privacy and trust assurances.
Research on federated and split learning (A6, A7, A8, A12, A18) underscores the
significance of privacy through the principle of data locality; however, the rigor of
privacy evaluations varies considerably across studies. Those that incorporate explicit
threat models or leakage analyses provide more robust evidence compared to those that
rely solely on architectural assertions. S
S
Blockchain-supported scenarios (S4) introduce trust as a system-level attribute.
E
Studies integrating blockchain with IoT and Rfog computing (A10) or smart contract-
P
based settlement and searchable encryption (A3) emphasize integrity, auditability, and
N
autonomous enforcement. In these cases, performance evaluation must include metrics
I
such as throughput, confirmation la tency, and operational overhead, as summarized in
E
Table 14. L
C
Implication for RQ2 and RQ4: Trustworthiness in IoT-based CNP fraud detection
I
arises from integratinTg privacy-preserving intelligence, auditable infrastructure, and
R
governance controls, rather than relying on a single technique. Consequently, the
A
performance evaluation must incorporate both technical metrics and assurance
indicators to enable the synthesis of a unified framework (RQ4).
Cross-Scenario Benchmarking: Comparability Rules, Evidence Gaps, and
Research Implications
Synthesizing performance across heterogeneous scenarios requires explicit
comparability rules. Based on the results so far and scenario taxonomy in Table 13,
three benchmarking principles are identified:
1. Benchmark within the scenario: Gateway studies should compare against similar
transaction-level frameworks; federated studies against distributed counterparts;
and blockchain-supported systems against governance-oriented baselines.
2. Report multi-dimensional performance: Accuracy alone is insufficient; real-time
systems require responsiveness metrics, federated systems require coordination
costs, and blockchain systems require throughput and auditability indicators.
3. State deployment assumptions explicitly: Dataset characteristics, streaming
assumptions, and operational budgets must be documented to support meaningful
benchmarking.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
The evidence reviewed indicates robust metrics for predictive effectiveness, yet
reveals  inconsistencies  in  reporting  real-time  responsiveness,  federation-specific
scalability costs, and blockchain throughput under realistic loads. These shortcomings
inform the design principles presented in Section 4.6 and the unified multi-layer IoT-
CNP framework in Section 4.7, which conceptualizes performance as a composite of
accuracy, responsiveness, scalability, and trust, rather than a singular score.
4.5 Distributed Learning & Privacy-preserving Models
This  section  synthesizes  evidence  on  how  distributed intelligence  and  privacy-
preserving computation enhance scalability, trustworthiness, and regulatory viability in
the context of IoT-enabled CNP fraud detection, especially when centralized data
aggregation is impractical. In alignment with RQ2, the literature increasingly portrays
CNP fraud detection as a collaborative learning challenge that involves diverse IoT
nodes and various financial stakeholders. Within this framework, the focus transitions
from the exchange of raw customer or device data to the sharing of model parameters,
thereby minimizing privacy risks and alleviating institutional friction.
Across the studies, three dominant technical families emerge:
(I). federated learning (FL) and its variants,
(II). split learning (SL) and hybrid FL-SL architectuSres, and
S
(III).  ledger-anchored trust mechanisms that reinforce auditability and post-
E
incident traceability.
R
P
The empirical evidence underpinning this subsection is summarized in Table 16,

indicaNtors
which  presents  representative  of  scalability  and  trustworthiness  across
I
| distributed learning designs.  |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- |
E

L
C
Table 16: Distributed learning & privacy-preserving models
I
T
Privacy /
R
| Cod Distribute |     | Scalability  | Trustworthine | Notable  |
| -------------- | --- | ------------ | ------------- | -------- |
ATrust
| e  d model  |     | signals  | ss signals  | outcomes  |
| ----------- | --- | -------- | ----------- | --------- |
mechanism(s)
Latency 31 ms,
|                |                |                 | ↑ High privacy  | Efficient learning  |
| -------------- | -------------- | --------------- | --------------- | ------------------- |
|                | Federated      | ≈ Moderate      |                 |                     |
| Hybrid         |                |                 | overhead        | under               |
|                | coordination;  | comms, ↑ High   |                 |                     |
| A4  Fuzzy and  |                |                 | (privacy        | heterogeneous,      |
|                | privacy-aware  | energy          |                 |                     |
| FL             |                |                 | features        | metaverse-style     |
|                | rules          | saving/throughp |                 |                     |
|                |                |                 | enabled)        | traffic.            |
ut
Fog-
|              | Tamper- | Latency 38 ms,  |                 |                 |
| ------------ | ------- | --------------- | --------------- | --------------- |
| distributed  |         |                 | ↑ High privacy  | Edge/fog scale  |
evident ledger; ≈ Moderate
| A6  detection  |              |                | overhead         | with verifiable  |
| -------------- | ------------ | -------------- | ---------------- | ---------------- |
|                | node         | comms, ↑ High  |                  |                  |
| and            |              |                | (crypto/ledger)  | event trails.    |
|                | attestation  | energy saving  |                  |                  |
blockchain
|     |     | Latency 27 ms,  |     | Near-centralized  |
| --- | --- | --------------- | --- | ----------------- |
↑ High privacy
| Federated  | Secure  | ↓ Low comms, ↑  |     | accuracy  |
| ---------- | ------- | --------------- | --- | --------- |
overhead (kept
| A10  IDS  | aggregation;  | High energy  |     | (98.4/97.2) with  |
| --------- | ------------- | ------------ | --- | ----------------- |
local; protected
| (FedAvg)  | local training  | saving, ↑ High  |     | strong scale and  |
| --------- | --------------- | --------------- | --- | ----------------- |
sharing)
|     |     | throughput  |     | privacy retention.  |
| --- | --- | ----------- | --- | ------------------- |

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Privacy /
| Cod Distribute |     | Scalability  | Trustworthine | Notable  |
| -------------- | --- | ------------ | ------------- | -------- |
Trust
| e  d model  |     | signals  | ss signals  | outcomes  |
| ----------- | --- | -------- | ----------- | --------- |
mechanism(s)
Latency 31 ms,
|                |                |                 | ↑ High privacy  | Efficient learning  |
| -------------- | -------------- | --------------- | --------------- | ------------------- |
|                | Federated      | ≈ Moderate      |                 |                     |
| Hybrid         |                |                 | overhead        | under               |
|                | coordination;  | comms, ↑ High   |                 |                     |
| A4  Fuzzy and  |                |                 | (privacy        | heterogeneous,      |
|                | privacy-aware  | energy          |                 |                     |
| FL             |                |                 | features        | metaverse-style     |
|                | rules          | saving/throughp |                 |                     |
|                |                |                 | enabled)        | traffic.            |
ut
Fog-
|              | Tamper- | Latency 38 ms,  |                 |                 |
| ------------ | ------- | --------------- | --------------- | --------------- |
| distributed  |         |                 | ↑ High privacy  | Edge/fog scale  |
evident ledger; ≈ Moderate
| A6  detection  |              |                | overhead         | with verifiable  |
| -------------- | ------------ | -------------- | ---------------- | ---------------- |
|                | node         | comms, ↑ High  |                  |                  |
| and            |              |                | (crypto/ledger)  | event trails.    |
|                | attestation  | energy saving  |                  |                  |
blockchain
Latency 24 ms,
Handles
| SplitFed  |                | ≈ Moderate     |                 |                   |
| --------- | -------------- | -------------- | --------------- | ----------------- |
|           | Split layers;  |                |                 | weak/heterogeneo  |
| (split    |                | comms, ↑ High  | ↑ High privacy  |                   |
| A11       | secure         |                |                 | us clients while  |
| learning  |                | energy         | oveSrhead       |                   |
|           | aggregation    |                |                 | preserving        |
S
| and FL)  |     | saving/throughp |     |           |
| -------- | --- | --------------- | --- | --------- |
|          |     |                 | E   | privacy.  |
ut
R
Latency 2P2 ms,
| FedGroup  |     |     |     | Best-in-class F1  |
| --------- | --- | --- | --- | ----------------- |

↓ LoNw comms, ↑ ↑ High privacy
| (group- | Group-wise  |     |     | 99.3, minimal  |
| ------- | ----------- | --- | --- | -------------- |
I
A12  based FL  aggregation;  V ery high  overhead (by  FPR (0.02%),
E
for non- secure sharinLg  throughput/ener design)  resilient to data
| IID)  |     | C gy saving  |     | heterogeneity.  |
| ----- | --- | ------------ | --- | --------------- |
I
T
Latency 33 ms,
|                  | CRommunicatio    |                 |                 | Balanced          |
| ---------------- | ---------------- | --------------- | --------------- | ----------------- |
| Privacy-         | A                | ↓ Low comms, ↑  |                 |                   |
|                  | n-efficient FL;  |                 | ↑ High privacy  | efficiency–trust  |
| A13  preserving  |                  | High energy     |                 |                   |
|                  | privacy          |                 | overhead        | profile for real  |
| FL               |                  | saving/throughp |                 |                   |
|                  | controls         |                 |                 | deployments.      |
ut
Latency 28 ms,
Higher accuracy
↓ Low comms, ↑
| Federated  | Secure       |              | ↑ High privacy  | than siloed     |
| ---------- | ------------ | ------------ | --------------- | --------------- |
| A16        |              | High energy  |                 |                 |
| MLP        | aggregation  |              | overhead        | models without  |
saving/throughp
centralizing data.
ut
Latency 36 ms,
Strong
| Blockchai   |                 | ↑ High comms,  |                 |                      |
| ----------- | --------------- | -------------- | --------------- | -------------------- |
|             | Smart           |                |                 | auditability; trust  |
| n-based     |                 | ≈ Moderate     | ↑ High privacy  |                      |
| A18         | contracts;      |                |                 | anchored in          |
| settlement  |                 | throughput, ↓  | overhead        |                      |
|             | sharded ledger  |                |                 | immutable            |
| & audit     |                 | Low energy     |                 |                      |
records.
saving

Federated and Split Learning for Privacy-Preserving Intelligence
Table 17 summarizes key studies on latency, communication costs, scalability, and
trustworthiness in distributed learning architectures. Federated learning (FL) is widely

ACCAERPTTICEDLE M IANN PURSECSRSIPT
utilized to promote collaboration among organizations without direct data sharing,
particularly in environments featuring distributed IoT streams and payment telemetry
(A4, A10, A12, A16). FL-based systems consistently achieve decision latencies under
30 milliseconds with low communication overhead while maintaining performance
comparable to that of centralized detection systems. Specialized FL variants, such as
heterogeneity-aware and group-based approaches (A12), effectively address challenges
posed by non-IID data common in IoT payment ecosystems, thereby improving
robustness and reducing false-positive rates.
Additionally, split learning and FL-split learning hybrids (A11, A13) enhance
privacy by partitioning model computations: sensitive feature representations remain
on client devices, while deeper layers execute on server-side infrastructure. These
architectures are particularly suited to resource-constrained edge devices and merchant
gateways, balancing detection quality, computational efficiency, and regulatory
compliance.
Operational Trade-offs of Federated and Split Learning in Real-Time CNP
Detection
Although federated and split learning are often suggested as privacy-preserving
options for distributed fraud detection, the studies Sreviewed highlight significant
S
practical trade-offs that affect real-time CNP deployment. Federated learning minimises
E
raw data exposure but introduces coordinatioRn delays, communication overhead, and
P
sensitivity to client heterogeneity, which are seldom quantified under transaction-level
N
time constraints.
I
However, split learning transfer s part of the model computation to the client or edge,
E
reducing communication payLloads but increasing on-device computation costs and
C
dependence on reliable, low-latency links between split layers. In the literature, both
I
paradigms are generalTly assessed based on predictive accuracy, with limited empirical
R
evaluation of round duration, synchronisation delays, energy consumption, or end-to-
A
end decision latency, leaving their readiness for real-time applications insufficiently
validated.
Table 17 provides a comparative analysis of federated and split learning, focusing
on their operational implications for real-time CNP fraud detection.
Table 17: Comparative analysis of federated and split learning for real-time CNP
fraud detection
Category Federated Learning Split Learning
Primary privacy Model update aggregation Feature/activation partitioning
mechanism without raw data sharing across client–server
Communication Periodic bidirectional Frequent but smaller exchanges
pattern updates (many rounds) per inference/training step
Latency Coordination and Inference pipeline dependency
implications aggregation delays between split layers
Energy impact on Medium (local training + Medium–High
the client communication) (forward/backward computation
on-device)
Suitability for real- Moderate, but sensitive to Context-dependent; requires
time CNP round duration stable low-latency links

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Common evaluation Lack of round-time and Lack of end-to-end latency and
gap throughput reporting device energy profiling
Coordination overhead, synchronization, and convergence challenges
In addition to the privacy benefits, the studies reviewed underscore the substantial
coordination costs associated with IoT-enabled CNP detection using distributed
learning. A prominent issue is the communication overhead caused by frequent
exchanges of models or activations. In reference to Table 17, federated learning entails
multiple rounds of aggregation traffic, whereas split learning requires continuous
interaction between clients and servers throughout both the training and inference
phases. The synchronization costs are further intensified by device heterogeneity and
intermittent connectivity, which may lead to stragglers and delayed global updates in
federated environments, or to stalled inference pipelines in split learning architectures.
Convergence challenges are further complicated by non-IID transaction data, partial
participation, and dynamic client availability, factors that are rarely rigorously tested
under real-time payment conditions. These challenges cast doubt on the scalability of
current designs without explicit coordination-aware opStimisation.
S
E
Privacy-Performance Trade-offs and OperaRtional Cost Drivers
P
Distributed learning effectively minimizes exposure to raw data; however,
N
safeguarding privacy incurs substantial operational costs. The deployment of secure
I
aggregation, encryption, and co ordination mechanisms can result in increased
E
communication overhead, addLed complexity in synchronization processes, and potential
C
latency increments in specific configurations. These trade-offs are elucidated in Table
I
16, which demonstrateTs that enhanced privacy and trust guarantees are accompanied by
R
varying degrees of communication and energy overhead.
A
Among the studies, three key cost drivers are essential for deployment:
1. Communication overhead, driven by update frequency, client participation, and
network constraints typical in IoT environments.
2. Sensitivity to heterogeneity, reflecting robustness under non-IID data, variable
device capabilities, and uneven local sample sizes.
3. Aggregation security, including resilience to poisoning, Sybil attacks, and
unreliable participants.
Ledger-Anchored Trust, Auditability, and Governance Support
In regulated payment ecosystems, privacy-preserving detection must support
auditability, governance, and dispute resolution. A blockchain-supported architecture
meets these needs by providing immutability and verifiable event histories. As shown
in Table 16 (A6, A18), ledger anchoring enhances trust and compliance by ensuring
that transaction events, alerts, and model updates are tamper-evident.
However, these advantages come with increased coordination overhead and
potential delays in confirmation. Therefore, when evaluating blockchain-enabled
contributions within the performance framework, it is crucial to consider not only
detection metrics but also factors such as throughput feasibility, audit latency, and
governance maturity, especially when evidentiary trails are necessary.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Permissioned versus permissionless blockchain designs
The studies under review implicitly assume various blockchain models without
consistently distinguishing their operational implications. Permissioned blockchains,
typically managed by recognised financial institutions or consortium members, offer
reduced consensus latency, predictable performance, and enhanced access control,
making them more suitable for real-time card-not-present (CNP) fraud governance than
public blockchains. In contrast, permissionless blockchains provide greater
decentralisation but come with increased latency, variable throughput, and higher
energy and communication overheads, which may conflict with the requirements of
time-sensitive transaction authorisation. This distinction is crucial for evaluating the
feasibility of blockchain technology in IoT-enabled payment systems.
Latency mitigation strategies for real-time operations
Numerous studies have proposed or adopted strategies to mitigate latency and
address the delays caused by blockchain technology. These strategies include off-chain
or side-channel processing for time-sensitive fraud decisions, batching transaction logs
rather than committing them for each event, and implementing lightweight consensus
protocols designed explicitly for permissioned enSvironments. Such approaches
S
effectively separate real-time detection from ledger finality, allowing fraud decisions to
E
be executed at the edge or gateway while maRintaining auditability through delayed or
P
summarised on-chain commitments.
N
I
When blockchain adds value and w hen it does not
E
The synthesis indicates thaLt integrating blockchain technology is most justified in
C
multi-stakeholder CNP ecosystems, where auditability, cross-organisational trust, and
I
non-repudiation are cruTcial. However, in environments with tightly controlled or single-
R
provider deployments, implementing blockchain may introduce unnecessary latency
A
and coordination overheads without commensurate benefits. In these cases, traditional
secure logging or centralised trust mechanisms may be more effective in addressing
real-time constraints.
Explainability, Resilience, and Design Implications
A persistent challenge in distributed intelligence is maintaining stakeholder trust as
models become more complex and decentralized. Two complementary strategies recur
across the synthesis implied by Table 16:
Robust aggregation and participant-aware defenses, aimed at mitigating

poisoning and Sybil behaviors in FL and FL-SL deployments.
Provenance-aware auditing, where ledger-based records support traceability of

model versions, update sources, and decision contexts.
Explainability is most effective when integrated at the decision point using
lightweight edge-side features and clearly linking decisions with model lineage. This
balance is crucial for maintaining real-time responsiveness while ensuring compliance
and facilitating post-hoc review.
Synthesis and Implications for IoT-Enabled CNP Fraud Detection

ACCAERPTTICEDLE M IANN PURSECSRSIPT
The evidence indicates that distributed learning and privacy-preserving intelligence
are valuable for scalable fraud detection in IoT-enabled CNP environments, but only
when their coordination costs remain within the bounds of time-sensitive payment
workflows. Federated and split learning reduce raw-data exposure and support
decentralized collaboration, yet their value depends on whether communication burden,
synchronization stability, and heterogeneous participation remain operationally
manageable. Likewise, blockchain-supported governance strengthens auditability and
traceability, but only when its latency and overhead remain compatible with real-time
authorization requirements. Overall, these findings suggest that privacy-preserving
collaboration and blockchain-supported governance should be assessed in terms of
responsiveness, scalability, and coordination costs rather than as isolated design
benefits.
4.6 Design principles for efficient, adaptive, and resilient IoT-driven fraud-detection
frameworks
The analysis of application scenarios, performance evaluation methods, and
distributed privacy-preserving models demonstrates that effective fraud detection for
CNP transactions driven by the Internet of Things (IoT) cannot rely solely on isolated
algorithm improvements. Instead, practical systemsS must adhere to clear design
S
principles that balance real-time operational constraints, diverse IoT environments,
E
evolving fraud patterns, and regulatory trust rRequirements. This section outlines these
P
principles based on the reviewed evidence and provides actionable guidance for system-
level implementation. N
I
E
Principle 1: Scenario-AwareL Performance Optimization
C
A recurring finding across Sections 4.3 and 4.4 is that performance is inherently
I
context dependent. DTetection accuracy, latency, scalability, and trust metrics vary
R
substantially across e-commerce gateways, edge-assisted payments, federated
A
monitoring, and blockchain-supported environments. Consequently, IoT-driven fraud
detection frameworks should be designed with explicit scenario awareness, ensuring
that optimization targets align with the intended deployment context.
For example, centralized gateway scenarios prioritize classification effectiveness
under high transaction throughput, whereas edge-assisted and mobile payments demand
strict latency and energy constraints. Distributed and federated scenarios introduce
additional coordination costs and increased sensitivity to heterogeneity, while
blockchain-supported systems emphasize auditability and governance. Treating these
contexts uniformly leads to misleading optimization and brittle designs. Scenario-aware
optimization, therefore, emerges as a foundational principle for efficient IoT-CNP
systems.
Principle 2: Real-Time Responsiveness as a First-Class Design Objective
The performance review highlights that many frameworks emphasize predictive
effectiveness while under-specifying real-time behavior, even when claiming near-real-
time operation. In CNP fraud detection, delayed responses can undermine detection
accuracy by allowing fraudulent transactions to proceed. As such, real-time
responsiveness must be treated as a first-class design objective, not a secondary
consideration.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Designs should explicitly account for end-to-end decision latency, event processing
rate, and model update intervals, particularly in edge-assisted and streaming scenarios.
Architectural strategies such as edge-level inference, lightweight models, and adaptive
decision pipelines support this objective, but must be evaluated under realistic workload
assumptions. Embedding responsiveness into system design directly enhances
operational readiness and resilience.
Principle 3: Distributed and Privacy-Preserving Intelligence by Design
The findings presented in Section 4.4 show that privacy preservation and scalability
are interconnected with modern IoT-enabled payment systems. Regulatory constraints,
institutional boundaries, and competitive factors hinder centralized data aggregation,
necessitating the adoption of distributed learning approaches, such as federated and split
learning.
The design of effective frameworks is intricately linked to the integration of privacy-
preserving intelligence, emphasizing the preservation of sensitive transactional and
behavioral data at the local level. This approach not only safeguards individual privacy
but also enables collaborative enhancements to the model, thereby fostering innovation.
It is crucial to understand that privacy should not be regarded as a dichotomous trait;
rather, a nuanced design is necessary to achieve a hSarmonious equilibrium among
S
several critical factors. These include the effectiveness of detection mechanisms, the
E
impact of communication overhead, the capaRcity to withstand heterogeneity, and the
P
ability to resist adversarial threats. Such a balanced framework enhances scalability and
N
trustworthiness, making it suitable for broad deployment across diverse stakeholder
I
environments. This paradigm shift towards a multifaceted understanding of privacy is
E
essential for the sustainable adLvancement of collaborative technological ecosystems.
C
I
Principle 4: AdaptiveT Learning under Non-Stationarity and Heterogeneity
R
CNP fraud patterns change rapidly due to evolving attacker strategies, varying user
A
behaviors, and platform-specific dynamics. The challenge is further intensified in IoT
environments, which involve non-stationary data streams and diverse device
capabilities. Studies indicate that static models and fixed thresholds become less
effective over time, compromising long-term performance.
To address this issue, adaptive learning mechanisms are crucial. Techniques such as
online updates, incremental training, and heterogeneity-aware aggregation must be
implemented. Frameworks should be designed to manage concept drift, client
variability, and partial participation without negatively impacting system performance.
In this context, adaptivity goes beyond model updates; it also encompasses dynamic
resource allocation and decision-making policies, thereby enhancing resilience against
evolving threats.
Principle 5: Resilience to Adversarial and System-Level Failures
In addition to accuracy and scalability, effective IoT-driven fraud detection systems
must withstand adversarial manipulation and operational disruptions. Distributed
learning introduces various attack vectors, such as data poisoning, Sybil attacks, and
unreliable participants. Deployments on edge and IoT devices also face challenges,
including device failures, intermittent connectivity, and resource exhaustion.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
To achieve resilience, these systems require multi-layered defenses, including strong
aggregation strategies, participant validation, redundancy across IoT layers, and the
ability to maintain functionality during partial system failures. By designing for
resilience, we can ensure that detection capabilities remain effective even in adverse
conditions, which is essential for financial transaction systems.
Principle 6: Integrated Trust, Governance, and Auditability
The synthesis highlights that fraud detection in CNP environments is not just a
technical challenge; it is part of a socio-technical system that operates within regulatory
and governance frameworks. Trustworthiness encompasses more than just detection
outcomes; it also includes explainability, accountability, and compliance.
Frameworks should integrate governance mechanisms, such as audit trails,
provenance tracking, and controls aligned with compliance standards, into the detection
process. Designs supported by blockchain technology exemplify one method for
achieving immutable auditability. However, governance can also be enhanced through
standardized logging and transparent decision reporting. By incorporating trust and
governance during the design phase, we can improve transparency and facilitate post-
incident analysis, dispute resolution, and regulatory acceptance.
S
S
Synthesis and Transition to Unified Framework Design
E
These design principles collectively highligRht that an efficient, adaptive, and resilient
P
IoT-driven CNP fraud detection system requires a holistic approach. Key elements such
N
as scenario awareness, real-time responsiveness, privacy-preserving distribution,
I
adaptability, resilience, and govern ance should be co-designed rather than optimized in
E
isolation. L
C
These principles are directly applied in the unified multi-layer IoT-CNP framework
I
outlined in Section 4.7T. In this framework, architectural layers, data flows, and decision-
R
making mechanisms are integrated to implement the insights gathered from the
A
reviewed literature.
4.7 Unified Multi-Layer Framework Formulation and Convergence Synthesis
Building on the scenario analysis, performance evaluation framework, distributed
and privacy-preserving intelligence models, and the design principles distilled from the
reviewed literature, this section formulates a unified multi-layer IoT-CNP fraud
detection framework. The proposed framework integrates diverse architectural
paradigms into a coherent reference architecture for real-time detection, scalability,
adaptability, privacy preservation, and trustworthiness in card-not-present transaction
environments.
Rather than proposing a new detection algorithm, this contribution focuses on
architectural convergence. It integrates IoT sensing, secure communication, edge/fog
intelligence, cloud-based coordination, distributed learning, decision-response
mechanisms, and governance controls into a layered framework aligned with the CNP
transaction lifecycle. This approach addresses the fragmentation observed in the
reviewed studies and provides a structured reference model for future IoT-enabled CNP
fraud detection systems.
To ground the framework in the reviewed evidence, the included studies were
aligned with the layers they primarily addressed. Studies on IoT sensing and contextual

ACCAERPTTICEDLE M IANN PURSECSRSIPT
data acquisition mainly contribute to the perception and device layers. Studies focused
on gateway, edge, and fog-based detection align with the edge-fog processing layer.
Centralized analytics, federated learning, split learning, and large-scale behavioral
profiling contribute to the cloud analytics and coordination layer. Governance-oriented
studies, including those addressing blockchain, compliance, auditability, and trust, span
the Security, Privacy, and Governance Layer and interact with multiple technical layers.
This mapping demonstrates that the proposed framework consolidates existing
contributions into an end-to-end architecture rather than presenting an abstract
conceptual model detached from the reviewed literature.
Rationale for a Unified Multi-Layer Architecture
The synthesis of the reviewed literature shows that no single architectural paradigm,
centralized cloud analytics, edge-centric processing, federated learning, split learning,
or blockchain-supported governance, can independently satisfy the full range of
operational, performance, privacy, and regulatory requirements associated with real-
time CNP fraud detection. Centralized cloud architectures provide high analytical
capacity and support large-scale model training, but they are frequently constrained by
latency, data sovereignty, privacy exposure, and reliance on continuous connectivity.
Conversely, edge-centric architectures reduce response Stime by processing fraud signals
S
closer to the transaction source, but they may face limitations in computational capacity,
E
global coordination, model consistency, and loRng-term scalability.
P
Distributed learning approaches such as federated learning and split learning reduce
N
the need to centralize sensitive payment and device data, but they introduce additional
I
challenges related to communicatio n overhead, client heterogeneity, synchronization,
E
convergence stability, and truLst management. Similarly, blockchain-based governance
C
can improve auditability, provenance, and transaction accountability, but standalone
I
blockchain solutions Tare generally unsuitable as primary real-time fraud detection
R
mechanisms when placed directly in the transaction authorization path because of their
A
potential computational and communication overhead.
These limitations indicate that IoT-enabled CNP fraud detection is best understood
as a system-of-systems problem. It requires coordinated intelligence across multiple
functional layers rather than dependence on a single computational or governance
model. The reviewed studies collectively suggest that real-time responsiveness,
analytical depth, privacy preservation, scalability, auditability, and regulatory
compliance must be balanced through architectural decomposition and functional
specialization.
Accordingly, the proposed framework adopts a unified six-layer IoT-CNP
architecture that assigns complementary and clearly delineated roles to the components
of the payment ecosystem. This architecture extends earlier conceptual classifications
by explicitly separating data capture, secure transmission, real-time edge inference,
cloud-based coordination, governance, and decision-response functions. In doing so, it
reflects deployment practices observed across edge-fog-cloud systems, where
transaction-time inference, model coordination, and audit functions are not executed in
the same layer or at the same speed.
The six layers of the proposed architecture, illustrated in Fig. 5, are described below.
The Perception/Device Layer captures transaction context and telemetry from web,
mobile, and IoT-enabled payment environments. It collects device and browser

ACCAERPTTICEDLE M IANN PURSECSRSIPT
fingerprints, geolocation signals, behavioral patterns, transaction metadata, session
characteristics, and other contextual indicators generated during CNP transaction
initiation. This layer provides the raw contextual foundation for downstream fraud
detection.
The Network/Communication Layer supports secure and efficient transmission of
enriched transaction features across the payment ecosystem. It relies on secure transport
protocols, encrypted communication channels, and event-streaming mechanisms to
route time-sensitive transaction signals while preserving confidentiality, integrity, and
responsiveness.
The Edge-Fog Processing Layer performs low-latency fraud screening close to the
transaction source. Its primary role is to execute lightweight anomaly scoring, device
fingerprint verification, contextual risk assessment, and immediate escalation of
suspicious transactions during the authorization window. Because CNP decisions often
need to be made within milliseconds, this layer supports real-time or near-real-time
inference using locally cached models, recent risk indicators, predefined thresholds, and
policy rules. By locating initial detection functions near the data source, the edge-fog
layer reduces round-trip communication delays and avoids overdependence on
centralized infrastructure during live authorization.
The Cloud Analytics and Coordination Layer prSovides high-compute analytical
S
capacity and global fraud intelligence. Unlike the edge-fog layer, the cloud layer is not
E
primarily responsible for millisecond-level trRansaction decisions. Instead, it supports
P
historical pattern mining, large-scale model retraining, cross-channel behavioral
N
profiling, federated model aggregation, split-learning coordination, global risk
I
intelligence, and long-term risk ana lysis. Cloud-based analytics improve model quality,
E
adaptability, and system-wide Lvisibility, while edge/fog inference preserves transaction-
C
time responsiveness.
I
A central feature oTf the architecture is the deliberate separation between edge/fog
R
detection and cloud-based analytics. Edge/fog detection prioritizes speed, proximity,
A
and immediate action. It is most suitable for transaction-time screening, where the
system must quickly determine whether a payment should proceed, be challenged, be
temporarily held, or be escalated. Cloud-based detection and coordination prioritize
analytical depth, historical learning, cross-institutional intelligence, and model
refinement. They are best suited for identifying emerging fraud patterns, retraining
models, aggregating federated updates, and improving detection capabilities over time.
Synchronization between the edge/fog and cloud layers is handled through
asynchronous model-update and feedback loops rather than synchronous transaction-
time dependency. During live payment authorization, the edge/fog layer does not wait
for full cloud-side retraining, federated aggregation, split-learning coordination, or
blockchain confirmation. Instead, it relies on locally available models, cached policy
rules, recent risk intelligence, and predefined thresholds to generate immediate fraud
scores. After the transaction, relevant outcomes, confirmed fraud labels, false-positive
feedback, drift indicators, client-side model updates, and model-performance signals
are transmitted to the cloud layer. The cloud layer then aggregates these signals, updates
global models or policies, and redistributes refined model parameters, decision rules, or
risk indicators back to edge and fog nodes. This asynchronous design preserves low-
latency transaction-time decision-making while enabling the system to continuously
learn from broader fraud patterns.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
The Security, Privacy, and Governance Layer provides mechanisms for
accountability, compliance, provenance, secure coordination, privacy protection, and
post-event review across stakeholders. In the proposed architecture, blockchain is
positioned as a governance and audit-support mechanism rather than as the core real-
time fraud classifier. This layer may support permissioned or consortium-based audit
trails, smart-contract-based policy enforcement, model-update logging, dispute
evidence, and settlement-related traceability. By separating governance from immediate
transaction scoring, the architecture avoids the latency burden that would arise if every
live authorization decision depended on direct on-chain validation.
Consistent with the blockchain trade-offs identified in the reviewed literature, this
layer is best implemented through permissioned, private, or consortium-based
blockchain mechanisms rather than public-chain validation. In this configuration,
trusted payment stakeholders such as issuers, acquirers, processors, regulators,
merchants, and fraud-monitoring entities may participate in controlled ledger
governance. Blockchain anchoring is therefore used to support auditability, provenance,
model-update logging, dispute evidence, settlement-related traceability, and policy
accountability without requiring live CNP authorization decisions to wait for public-
chain confirmation.
The Application and Decision-Response Layer traSnslates fraud scores, contextual
S
risk signals, policy rules, and governance indicators into operational actions. These
E
actions may include transaction approval, stepR-up authentication, temporary blocking,
P
manual review, customer notification, fraud analyst escalation, or post-transaction
N
monitoring. This layer ensures that analytical outputs are translated into timely,
I
proportionate fraud-control decis ions while supporting explainable reporting for
E
relevant stakeholders. L
C
The proposed framework reflects three major synthesis outcomes. First, effective
I
IoT-enabled CNP frauTd detection depends on cross-layer interaction rather than isolated
R
model performance. Second, privacy-preserving intelligence, edge-cloud coordination,
A
and governance mechanisms are integral to deployment viability rather than optional
extensions. Third, future systems should be benchmarked not only by classification
accuracy, but also by latency, throughput, scalability, synchronization cost,
communication overhead, privacy preservation, auditability, and operational resilience.
Fig. 5 Unified Multi-Layer IoT Fraud Detection Framework

ACCAERPTTICEDLE M IANN PURSECSRSIPT
S
S
E
R
P
N
I
E
L
C
I
T
R
A
By distributing responsibilities across these six layers, the proposed architecture
mitigates the limitations of isolated approaches while enabling scalable, privacy-aware,
low-latency, and auditable fraud detection. The layered design reflects the empirical
evidence synthesized from the literature and provides a coherent foundation for
implementing adaptive, trustworthy CNP fraud-detection systems in IoT-enabled
payment environments.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Cross-Layer Convergence and Data Flow
The effectiveness of the proposed framework arises from cross-layer convergence
rather than from isolated functions. As illustrated in Fig. 5, transactional and contextual
data flow upward from the perception layer through the communication and edge-fog
processing layers, enabling real-time risk assessment. At the same time, decisions,
alerts, model updates, policy adjustments, and governance signals move downward and
laterally across layers.
Short feedback loops between the Perception/Device, Network/Communication, and
Edge-Fog Processing Layers enable immediate fraud detection while meeting strict
latency requirements. Longer feedback cycles involving the Cloud Analytics and
Coordination Layer and the Security, Privacy, and Governance Layer support strategic
adaptation, global learning, model refinement, and regulatory compliance. Governance
metadata, such as decision provenance, policy enforcement records, model update logs,
and audit events, enhances explainability and traceability without impeding real-time
execution.
This convergence ensures that detection effectiveness, latency, scalability, privacy,
and trust are optimized collectively rather than independently. It also operationalizes
the multi-dimensional performance framework established in Section 4.4 by showing
how different performance dimensions are associated wSith different architectural layers.
S
E
Alignment with Research Questions and DeRsign Principles
P
The unified architecture directly operationalizes the study’s research questions.
N
For RQ1, the layered structure clarifies where performance metrics apply, enabling
I
scenario-aware comparison across gateway, edge-assisted, federated, and blockchain-
E
supported contexts. For RQ2,L federated learning and split learning within the edge-fog
C
and cloud coordination layers enable scalable collaboration without centralizing
I
sensitive data. For RTQ3, real-time responsiveness, adaptivity, resilience, privacy
R
preservation, and governance are embedded as structural design requirements rather
A
than treated as post hoc additions. For RQ4, integrating all six layers provides a
synthesis-derived reference model for trustworthy, real-time IoT-driven CNP fraud
detection.
This explicit mapping distinguishes the proposed framework from prior works that
address only isolated components of the fraud detection pipeline. It also demonstrates
how the design principles identified in Section 4.6 are translated into deployable
architectural logic.
Implementation Considerations and Extensibility
The proposed framework is technology-agnostic and can be adopted incrementally.
Organizations may implement specific layers depending on their operational maturity,
regulatory requirements, technical infrastructure, and risk tolerance. For instance, real-
time edge scoring can be deployed independently from blockchain anchoring, while
federated learning or split learning can be introduced gradually as cross-institutional
collaboration develops.
The architecture is intentionally extensible. It allows integration of emerging
technologies such as explainable AI, secure enclaves, trusted execution environments,
adaptive graph analytics, privacy-preserving computation, post-quantum cryptographic
controls, and adaptive policy engines without requiring structural redesign. This

ACCAERPTTICEDLE M IANN PURSECSRSIPT
flexibility ensures that the framework remains relevant within the rapidly evolving
payment and IoT ecosystems.
Operationalising governance and privacy across layers
In the proposed framework, governance and privacy are treated as operational
functions embedded across the architecture rather than as isolated components. Privacy
enforcement begins at the sensing layer through data minimisation and contextual
feature abstraction. It continues at the edge through secure feature processing and at the
coordination layer through privacy-preserving learning mechanisms such as federated
learning and split learning. Governance mechanisms, including audit logging, access
control, policy enforcement, provenance tracking, and compliance reporting, interact
with all layers to ensure accountability while avoiding direct interference with time-
critical detection workflows.
This layered operationalisation clarifies how trust and privacy requirements can be
enforced without compromising real-time performance. It also reinforces the role of
governance as a cross-cutting capability rather than a separate, optional module.
Unified multi-layer IoT–CNP reference framework
Fig. 6 illustrates the integrated data flows origSinating from IoT sensing and
S
transaction sources, moving through edge-level detection and cloud-based coordinated
E
analysis. It also depicts the learning loopsR that support model updates through
P
centralized, federated, or split-learning paradigms. Governance feedback mechanisms
N
are represented as orthogonal controls, ensuring policy enforcement, auditability,
I
traceability, and compliance withou t being confined to a single architectural layer.
E
L
C
Fig. 6 Unified multi-layer IoT–CNP reference framework illustrating data flows,
I
lTearning loops, and governance interaction
R
A

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Illustrative Deployment Scenario of the IoT-CNP Fraud Detection Architecture
To demonstrate how the proposed architecture can operate in practice, a
representative IoT-enabled card-not-present transaction scenario is described below.
1. Transaction Generation: Perception/Device Layer
A consumer initiates an online payment using a connected device such as a
smartphone, wearable device, smart appliance, or browser-enabled platform.
Transaction and contextual signals, including device fingerprint, session
metadata, location indicators, behavioral interaction patterns, and transaction
attributes, are generated at the point of initiation.
2. Secure Data Transmission: Network/Communication Layer
The transaction request and associated contextual features are transmitted
through secure communication channels to the relevant gateway, edge, or
payment-processing infrastructure. Encryption, secure transport protocols, and
event-streaming mechanisms preserve confidentiality and responsiveness.
3. Edge-Level Fraud Screening: Edge-Fog Processing Layer
At the edge or fog node, lightweight anomaly detection models perform
preliminary inference. These models evaluate contextual features such as device
identity, abnormal behavioral patterns, and unSusual transaction frequency, as
S
well as risk thresholds. Suspicious transactions can be flagged, challenged, or
E
escalated immediately with minimal latRency.
P
4. Advanced Fraud Analytics: Cloud Analytics and Coordination Layer
N
Aggregated insights from multiple edge and fog nodes are transmitted to the
I
cloud analytics layer. This layer performs deeper model retraining, historical
E
analysis, behavioral proLfiling, federated aggregation, cross-channel intelligence
C
generation, and long-term model governance. Cloud-side processing improves
I
future detectionT performance without interrupting live transaction authorization.
R
5. Decision and Response: Application and Decision-Response Layer
A
Based on the computed fraud risk score and applicable policy rules, the
application layer determines whether to approve the transaction, request
additional authentication, temporarily hold the transaction, decline it, or escalate
it for manual review. Where appropriate, explainable outputs are provided to
support fraud analysts, customer communication, and dispute resolution.
6. Governance and Compliance: Security, Privacy, and Governance Layer
The Security, Privacy, and Governance Layer enforces security policies, privacy
controls, audit logging, model-update traceability, and regulatory compliance.
Permissioned or consortium-based ledger anchoring may be used to record
selected control events and provenance metadata, supporting accountability
without imposing on-chain confirmation delays on the real-time authorization
pathway.
Contribution of the Validation Scenario
The illustrative scenario demonstrates that the proposed framework can support real-
time fraud detection in distributed IoT payment environments by combining device-
level contextual intelligence, secure feature transmission, edge-based anomaly
detection, cloud-scale fraud analytics, privacy-preserving learning, and governance-
aware compliance mechanisms.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
The proposed IoT-CNP framework should therefore be interpreted as a synthesis-
derived reference architecture rather than as an experimentally validated fraud-
detection system. Its purpose is to integrate fragmented evidence across sensing,
communication, analytics, distributed learning, decision support, and governance into a
coherent deployment-oriented model. In this review, the framework functions as a
reference synthesis and benchmarking guide rather than as a prescriptive
implementation claim.
5. Discussion
5.1 Interpreting the Landscape of IoT-Based CNP Fraud Detection Frameworks
(RQ1)
The synthesis of frameworks in Section 4.2 reveals a fragmented, siloed research
landscape, in which IoT-enabled CNP fraud detection solutions are typically proposed
as isolated models or architectures that address narrow technical objectives. While
many studies demonstrate strong predictive performance in specific settings, relatively
few examine how detection logic integrates across IoT layers or adapts to heterogeneous
operational environments.
From an analytical standpoint, this fragmentation lSimits systematic benchmarking
and obscures broader design trade-offs. Most reviewSed studies implicitly address RQ1
E
by reporting detection performance, yet they often underrepresent system-level
R
considerations such as scalability, govePrnance, and real-time deployment. This
imbalance underscores the need to movNe beyond algorithm-centric comparisons toward
ecosystem-level synthesis, in whiIch frameworks are evaluated based on their
E
architectural placement, application context, and operational constraints.
L
C
5.2 Implications of ApplIication Scenarios and Case-Study Contexts
T
The scenario taRxonomy introduced in Section 4.3 demonstrates that CNP fraud
A
detection is inherently context dependent. Gateway-centric e-commerce environments
emphasize low-latency decisioning and high precision. In contrast, edge-assisted
mobile and IoT payment scenarios introduce additional challenges related to device
heterogeneity, energy efficiency, and intermittent connectivity. Distributed and
federated monitoring scenarios further shift attention toward coordination costs and
privacy preservation, while blockchain-supported scenarios foreground auditability and
compliance.
A key implication is that performance claims divorced from application context have
limited practical meaning. High accuracy reported under centralized assumptions may
not translate to latency-sensitive edge deployments, just as privacy-preserving federated
frameworks may incur coordination overheads unsuitable for specific real-time
scenarios. These findings reinforce RQ1 by demonstrating that meaningful
benchmarking must be scenario-aware, aligning evaluation metrics with the operational
realities of each deployment context.
5.3 Performance Evaluation Practices and Benchmarking Implications
The performance evaluation synthesis in Section 4.4 highlights a persistent emphasis
on predictive effectiveness metrics, often at the expense of real-time responsiveness,
scalability, and trust-related indicators. While accuracy-centric reporting remains

ACCAERPTTICEDLE M IANN PURSECSRSIPT
valuable, it provides an incomplete picture of system readiness in IoT-enabled payment
environments.
Interpreting these findings reveals three critical insights. First, real-time
responsiveness is inconsistently reported, even in studies claiming real-time capability,
limiting the validation of deployment feasibility. Second, scalability must be treated as
a system-level property, encompassing not only computational efficiency but also
communication overhead, coordination complexity, and robustness to non-IID data.
Third, trust and privacy are increasingly central performance dimensions, particularly
in regulated financial contexts, yet they are rarely quantified in a standardized manner.
These observations address RQ1 by identifying benchmarking gaps and inform RQ3
by motivating a multi-dimensional performance evaluation paradigm, where
effectiveness, latency, scalability, and trust are co-evaluated rather than considered
independently.
5.4 Distributed Learning and Privacy-Preserving Intelligence in Practice
The analysis in Section 4.5 shows that distributed intelligence can strengthen
scalability, privacy preservation, and institutional interoperability in IoT-enabled CNP
fraud detection. However, its value is contingent on whether coordination overhead,
client heterogeneity, aggregation stability, and goverSnance costs remain compatible
S
with real-time payment requirements. This indicates that distributed learning should be
E
evaluated not only as a privacy mechanism, Rbut as a deployment-dependent systems
P
choice. These insights directly address RQ2, demonstrating that distributed intelligence
enhances scalability and trustworthNiness when privacy, coordination cost, and
I
governance are treated as first-class design considerations.
E
L
5.5 Design Principles as SCystem-Level Guidance
I
The design princiTples articulated in Section 4.6 serve to translate empirical
R
observations into actionable guidance at the system level. These principles, scenario
A
awareness, real-time responsiveness, adaptivity, resilience, and governance integration,
should not be viewed as isolated optimization goals but rather as elements that shape an
interdependent design space.
The discourse emphasizes the need to co-optimize these principles. For instance,
relocating inference to the edge enhances responsiveness; it also requires implementing
complementary resilience and governance mechanisms to address potential adversarial
risks. Likewise, adopting privacy-preserving learning techniques enhances compliance;
however, this advancement requires meticulous management of communication
efficiency and fault tolerance.
By characterizing these principles as architectural constraints rather than mere
optional features, the study advances RQ3. It lays a structured foundation for the design
of IoT-driven CNP fraud detection systems capable of sustained operation in real-world
environments.
5.6 Interpreting the Unified Multi-Layer IoT-CNP Framework
The unified multi-layer framework in Section 4.7 should be understood as a
reference synthesis rather than a prescriptive implementation blueprint. Its contribution
lies in integrating sensing, communication, analytics, distributed learning, decision-
making, and governance into a coherent architectural model aligned with the CNP

ACCAERPTTICEDLE M IANN PURSECSRSIPT
transaction lifecycle. This integrated view provides a practical basis for future
benchmarking and system design across diverse CNP payment environments.
5.7 Synthesis, Research Implications, and Limitations
Synthesis of Findings
The synthesis reveals a fragmented research landscape in which most studies
prioritize predictive accuracy while underreporting deployment factors such as latency,
communication overhead, and governance mechanisms. Scenario-based analysis
further shows that performance claims are context-dependent and that privacy-
preserving approaches often introduce trade-offs in coordination and scalability. The
unified IoT-CNP framework consolidates these findings into an architectural reference
model aligned with the CNP transaction lifecycle.
Research Implications
From a research perspective, the findings indicate a shift from model-centric
evaluation toward system-level benchmarking for IoT-enabled CNP fraud detection.
Future studies should therefore report not only predictive effectiveness, but also real-
time responsiveness, scalability, communication costS, and trust-related deployment
S
constraints. Scenario-aware design remains essential, since frameworks that perform
E
well in centralized e-commerce settings maRy not remain suitable in edge-assisted,
P
federated, or blockchain-supported environments. Security evaluation also requires
broader treatment than predictive perfNormance alone, particularly in collaborative and
I
distributed settings where adversa rial resilience and governance-aware trust become
E
central concerns. L
C
I
Limitations T
R
Several limitations should be acknowledged. First, the study is constrained by
A
inconsistent reporting practices in the literature, particularly regarding latency budgets,
dataset characteristics, and deployment assumptions. Second, industrial and proprietary
fraud-detection systems remain underrepresented due to limited public disclosure,
potentially biasing the evidence base toward academic prototypes. Third, although the
proposed unified framework is analytically grounded in the reviewed literature, it has
not been empirically validated within the scope of this systematic review. While proof-
of-concept implementation would strengthen external validity, the present study is
intended to provide a review-derived reference architecture and benchmarking agenda
for subsequent simulation, prototyping, and operational validation.
5.8 Aligning IoT layers with the Card-Not-Present (CNP) transaction lifecycle
The CNP transaction lifecycle is a multi-stage socio-technical process in which fraud
risk emerges dynamically across four phases: interaction, transmission, decision, and
settlement. As illustrated in Fig. 7, effective fraud mitigation occurs when the Internet
of Things (IoT) architectural layers are explicitly aligned with these transaction stages.
This alignment enables contextual intelligence, real-time responsiveness, and post-
event accountability without disrupting the payment flow.
During the transaction initiation phase, the merchant's web or mobile interface acts
as the primary sensing point. In addition to traditional elements outlined in ISO 8583

ACCAERPTTICEDLE M IANN PURSECSRSIPT
and PCI, such as anonymized Primary Account Numbers (PAN), transaction amounts,
merchant IDs, and category codes, IoT-style telemetry, including device identifiers,
operating system and browser fingerprints, IP addresses, and geolocation cues, enriches
the behavioral context of the transaction.
Normalizing these heterogeneous signals into compact, signed feature
representations is critical for preserving privacy and enabling efficient downstream
processing. This approach represents a broader shift from raw data transmission to
context-aware feature exchange, consistent with the privacy-preserving design
principles articulated in Section 4.5.
During network transmission, edge and fog infrastructures serve as intermediaries
between merchant environments and payment processors. Secure protocols, such as
TLS or QUIC, ensure data confidentiality. Additionally, edge-level queuing and
prioritization enable the differentiated handling of high-risk transactions. This phase
demonstrates how IoT networking capabilities enable event-driven responsiveness,
enabling model refresh triggers or contextual alerts to be issued without interrupting
authorization flows. From a systems perspective, this reinforces the edge layer's role as
both a performance accelerator and a coordination hub.
The processing and decision phase corresponds to the analytics layer of the unified
framework. In this phase, real-time fraud scoring isS performed, often within strict
S
latency budgets (typically within tens of milliseconds), using edge-resident or hybrid
E
inference engines. It is important to note that feRderated and graph-aware risk models are
P
particularly well-suited for this stage, as they exploit relational dependencies among
N
cards, devices, merchants, and network attributes while maintaining data locality. This
I
alignment operationalizes the co nvergence of AI and IoT, demonstrating how
E
distributed intelligence can acLhieve both responsiveness and privacy.
C
After conducting a risk assessment, the application and response stage converts
I
analytical results into Tactionable decisions. Fraud scores, confidence indicators, and
R
clear explanations are communicated to merchants or processors to help them decide
A
whether to approve transactions, implement additional authentication steps, or decline
them. From a governance perspective, readily available decision rationales are crucial
for effective customer communication, dispute management, and regulatory
compliance. This highlights the importance of incorporating explainability into the
application layer from the outset rather than adding it later.
The security and governance layer encompasses the entire transaction lifecycle,
capturing vital events, device statuses, and decision-related data for audit and
compliance purposes. By anchoring select control events in lightweight, ledger-based
records, we enhance integrity and traceability without introducing delays associated
with consensus. This strategic application of blockchain technology exemplifies
scenario-driven convergence: governance is strengthened where necessary, while real-
time performance is preserved. Following this, authorization and settlement proceed
through established acquiring and issuing workflows, effectively completing the
transaction process.
This lifecycle-oriented perspective reframes CNP fraud detection as an ongoing,
multi-layered control process rather than a single-point classification task. By aligning
IoT layers with transaction stages, the unified framework ensures reliable context
capture from devices, efficient transmission of features, quick and understandable
decision-making, and a clear audit trail of outcomes. This alignment directly supports

ACCAERPTTICEDLE M IANN PURSECSRSIPT
RQ4 by demonstrating how a unified multi-layer IoT framework can improve real-time
fraud detection and prevention across the entire CNP transaction process. Additionally,
it reinforces RQ3 by emphasizing the importance of lifecycle alignment as a
fundamental design principle for resilient deployment.
Fig. 7 CNP Transaction Process aligned with IoT ecosystem
S
S
E
R
P
N
I
E
L
C
I
T
R
A
Source: [33]
5.9 Regulatory and Compliance Implications for IoT-Enabled CNP Fraud Detection
The deployment of IoT-enabled CNP fraud detection systems functions within a
stringent financial and data-protection framework. Regulations such as the European
Union’s General Data Protection Regulation (GDPR) and the Revised Payment
Services Directive (PSD2) impose strict requirements on data minimisation,
transparency, user consent, and accountability. The reviewed frameworks indicate that
centralised, data-heavy detection models may clash with GDPR principles, especially
those concerning data locality and purpose limitation. In contrast, federated and split
learning approaches align more naturally with regulatory expectations by enabling
collaborative intelligence without direct data-sharing. Similarly, PSD2’s strong
customer authentication (SCA) and transaction monitoring requirements underscore the
need for low-latency, explainable, and auditable fraud detection mechanisms,
particularly in IoT-enabled payment environments.
Blockchain-supported governance frameworks further strengthen compliance by
providing immutable audit trails and verifiable decision provenance, both of which are
crucial for post-incident investigations and regulatory reporting. However, their
integration must be carefully designed to avoid introducing latency that could disrupt

ACCAERPTTICEDLE M IANN PURSECSRSIPT
real-time authorisation flows. Regulatory compliance emerges not as an external
constraint but as a key architectural driver shaping the adoption of distributed learning,
edge intelligence, and governance-aware IoT-CNP fraud detection systems.
6. Conclusion and Future Work
6.1 Conclusion
This study offers a systematic review of the IoT ecosystem for real-time CNP fraud
detection, synthesizing findings from 23 peer-reviewed studies. By structuring the
analysis around application scenarios, performance evaluation methodologies,
distributed intelligence, privacy preservation, and system-level design principles, this
review advances beyond algorithm-centric comparisons, providing a holistic
understanding of deployable IoT-driven fraud detection frameworks.
In addressing RQ1, the review illustrates that current IoT-based CNP fraud detection
frameworks cannot be effectively benchmarked without explicit consideration of the
contextual application and operational constraints. Although detection accuracy is the
most frequently reported metric, it is inadequate when considered in isolation. Scenario-
aware benchmarking that encompasses latency, scalability, energy efficiency, and
governance requirements are essential for establishing Svalid cross-study comparisons.
Regarding RQ2, the analysis demonstrates thSat distributed, privacy-preserving
E
intelligence, particularly through federated and split learning, is fundamental to
R
achieving scalable, trustworthy CNP fraudP detection. These methodologies facilitate
collaborative learning across institutionNal boundaries while preserving data locality and
ensuring regulatory compliance. HoIwever, their practical effectiveness depends on
E
design choices that are sensitive to coordination, including communication efficiency,
L
robustness to non-IID Cdata distributions, and resilience against adversarial
I
manipulation. T
In response to RRQ3, the study distills a coherent set of system-level design principles
A
that underpin efficient, adaptive, and resilient IoT-driven fraud detection systems.
These principles, scenario-aware optimization, real-time responsiveness, privacy-by-
design distribution, adaptive learning under non-stationarity, resilience to adversarial
and systemic failures, and integrated governance, translate empirical findings into
actionable guidance for the transition from research prototypes to operational
deployments.
Finally, addressing RQ4, the paper proposes a unified multi-layer IoT-CNP fraud
detection framework that integrates sensing, edge intelligence, analytics, distributed
learning, and governance mechanisms throughout the CNP transaction lifecycle. Rather
than introducing a novel detection algorithm, this framework offers a reference
architecture that reconciles performance, privacy, scalability, and trust within a single
coherent system model. This contribution, oriented toward convergence, seeks to
mitigate the fragmentation observed in prior studies and lays a structured foundation for
future research and practical implementation.
6.2 Future Works
Despite growing interest in distributed, privacy-preserving learning, several research
challenges remain unresolved in the scalable IoT-enabled CNP fraud detection domain.
There is an urgent need for coordination-efficient learning protocols that can reduce

ACCAERPTTICEDLE M IANN PURSECSRSIPT
communication and synchronization costs while maintaining detection accuracy under
strict latency constraints. Current evaluation frameworks do not adequately address
scalability issues, especially considering device heterogeneity in computational power,
energy capacity, and network reliability. Additionally, understanding convergence
guarantees in non-IID and streaming transaction data within real-time payment
scenarios is limited. There is also a lack of standardized benchmarks and workloads to
comprehensively assess accuracy, latency, communication costs, and energy
consumption at scale. Addressing these challenges is essential to advance federated and
split learning from theoretical potential to practical deployment in large-scale IoT
payment systems. To improve IoT-enabled CNP fraud detection, researchers should
focus on several key areas.
First, developing standardized, scenario-aware performance metrics is crucial—
particularly for real-time responsiveness, federated scalability costs, and governance
indicators. Longitudinal studies simulating realistic transaction volumes and evolving
fraud patterns would further strengthen empirical validation.
Second, there is a significant need for thorough empirical validation of unified,
multi-layer architectures in real-world settings or large-scale pilots. While existing
studies often evaluate individual components separately, future research should analyze
end-to-end system performance across sensing, analyStics, learning, and governance
S
layers, including failure modes, recovery processes, and operational trade-offs.
E
Third, integrating explainable artificialR intelligence and human-in-the-loop
P
mechanisms into IoT-driven CNP fraud detection remains underexplored. Providing
N
interpretable, context-aware explanations at critical decision points is vital for
I
regulatory compliance, customer tr ust, and operational oversight.
E
Fourth, recent advances in Lsecure computation, trusted execution environments, and
C
post-quantum cryptography offer promising pathways to enhance privacy and trust.
I
Exploring systematic iTncorporation of these technologies into federated and blockchain-
R
based architectures is an important future direction.
A
Fifth, expanding analysis to cross-border payment ecosystems, emerging digital
currencies, and decentralized finance platforms will help evaluate the adaptability and
scalability of IoT-enabled CNP fraud detection in evolving financial landscapes. Future
research should go beyond accuracy testing and systematically examine coordination
latency, communication costs, and energy use under realistic transaction loads.
Furthermore, assessing blockchain-enabled CNP systems should differentiate
governance benefits from performance costs, considering both permissioned and
permissionless designs.
Emerging technologies such as quantum computing and generative AI are also likely
to influence future IoT-CNP fraud detection architectures. Quantum computing may
weaken conventional public-key encryption, digital signatures, blockchain
cryptography, and secure payment authentication, making post-quantum cryptographic
readiness an important research priority. Future systems should therefore examine
quantum-resistant digital signatures, post-quantum key-exchange mechanisms, and
migration pathways for payment and blockchain infrastructure. Generative AI also
introduces both defensive and adversarial implications. Defensively, generative models
can support synthetic fraud-pattern generation, rare attack simulation, privacy-
preserving data augmentation, and adversarial stress testing, especially where labelled
real-world CNP fraud data are scarce. However, generative AI may also strengthen

ACCAERPTTICEDLE M IANN PURSECSRSIPT
attacker capabilities by enabling synthetic identities, automated phishing, credential
harvesting, adversarial transaction simulation, and adaptive social-engineering attacks.
Future research should therefore evaluate generative AI both as a tool for improving
model robustness and as a risk factor within IoT-enabled payment ecosystems.
Future research should evaluate the proposed reference architecture through staged
validation, including simulation-based assessment, prototype or testbed
implementation, and pilot deployment under realistic payment authorization, privacy,
and compliance constraints. Such validation should jointly assess detection
effectiveness, end-to-end latency, throughput, communication and coordination cost,
privacy overhead, adversarial resilience, data-poisoning robustness, secure aggregation
reliability, and cross-layer trust assurance. Without this broader validation, apparently
strong fraud-detection performance may not translate into dependable real-world
operation.
References
1. Alatawi, M. N. (2025). Detection of fraud in IoT-based credit card collected
datasets using machine learning. Machine LearnSing with Applications, 19,
S
100603. https://doi.org/10.1016/j.mlwa.2024.100603
E
2. Bhutta, M. N. M., Bhatia, S., Alojail, RM. A., Khan, M. T. R., & Ahmad, A.
P
(2022). Towards secure IoT-based payments by extending the Payment Card
N
Industry Data Security Standard (PCI DSS). Wireless Communications and
I
Mobile Computing, 2022, Ar ticle 9942270.
E
https://doi.org/10.1155/L2022/9942270
C
3. Liu, C., Xiao, Y., Javangula, V., Hu, Q., Wang, S., & Cheng, X. (2019).
I
NormaChain: AT blockchain-based normalized autonomous transaction
R
settlement system for IoT-based e-commerce. IEEE Internet of Things Journal,
A
6(3), 4680–4693. https://ieeexplore.ieee.org/abstract/document/8502858
4. Gupta, S., & Kumar, V. (2024). Integrating deep learning, machine learning,
artificial intelligence, IoT, and data science for future innovations. Proceedings
of the IEEE International Conference on Emerging Technologies. IEEE.
https://ieeexplore.ieee.org/document/10917415
5. Yasaei, R., Moghaddas, Y., Abdullah, M., & Faruque, A. (2024). IoT-
GRAF: IoT graph learning-based anomaly and intrusion detection through
multimodal data fusion. IEEE Internet of Things Journal. Advance online
publication. https://ieeexplore.ieee.org/document/10546572
6. Deshmukh, A., de la Rosa, P. E., Rodriguez, R. V., & Dasari, S. (2025).
Enhancing privacy in IoT-enabled digital infrastructure: Evaluating federated
learning for intrusion and fraud detection. Sensors, 25(10), 3043.
https://doi.org/10.3390/s25103043
7. Rguibi, A., Asimi, Y., Asimi, A., & Oumouss, L. (2024). Privacy-preserving
anomaly detection for IoT: Leveraging federated and split learning. IEEE
Access, 12, 75081–75095. https://doi.org/10.1109/ACCESS.2024.3456781
8. Zhang, Y., Suleiman, B., Alibasa, M. J., & Farid, F. (2024). Privacy-aware
anomaly detection in IoT environments using FedGroup: A group-based

ACCAERPTTICEDLE M IANN PURSECSRSIPT
federated learning approach. Journal of Network and Systems Management.
Advance online publication. https://doi.org/10.1007/s10922-023-09782-9
9. Khan, A. A., Alsufyani, A., Alsufyani, N., et al. (2025). BAML: A
decentralized approach to secure, privacy-preserving financial compliance
using blockchain Hyperledger and federated learning. Peer-to-Peer Networking
and Applications, 18, 270. https://doi.org/10.1007/s12083-025-02086-6
10. Khan, A. A., Ghodhbani, R., Alsufyani, A., Alsufyani, N., & Mohamed, M.
A. (2025). Leveraging blockchain-integrated explainable artificial intelligence
for ethical and personalized healthcare decision-making. The Journal of
Supercomputing, 81(15), 1353-1372. https://doi.org/10.1007/s11227-025-
07844-0
11. Khan, A. A., Laghari, A. A., Almansour, H., Jamel, L., Hajjej, F., Estrela,
V. V., & Ullah, S. (2025). Quantum computing empowering blockchain
technology with post-quantum resistant cryptography for multimedia data
privacy preservation. Journal of Cloud Computing, 14(1), 43.
https://doi.org/10.1186/s13677-025-00771-8
12. Bhattacharyya, S., Jha, S., Tharakunnel, K., & Westland, J. C. (2011). Data
mining for credit card fraud: A comparative study. Decision Support Systems,
50(3), 602–613. https://doi.org/10.1016/j.dss.201S0.08.008
S
13. Dal Pozzolo, A., Boracchi, G., Caelen, O., Alippi, C., & Bontempi, G.
E
(2018). Credit card fraud detection: A rRealistic modeling and a new publicly
P
available dataset. IEEE Transactions on Neural Networks and Learning
N
Systems, 29(8), 3784–3797. https://doi.org/10.1109/TNNLS.2017.2736643
I
14. Carcillo, F., Dal Pozzolo, A ., Le Borgne, Y. A., Caelen, O., Mazzer, Y., &
E
Bontempi, G. (2018). SLcarff: A scalable framework for streaming credit card
C
fraud detection with Spark. Information Fusion, 41, 182–194.
I
https://doi.org/1T0.1016/j.inffus.2017.09.005
R
15. Yang, Y., Wu, L., Yin, G., Li, L., & Zhao, H. (2017). A survey on security
A
and privacy issues in Internet of Things. IEEE Internet of Things Journal, 4(5),
1250–1258. https://doi.org/10.1109/JIOT.2017.2694844
16. Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. (2021). The PRISMA
2020 statement: An updated guideline for reporting systematic reviews. BMJ,
372, n71. https://doi.org/10.1136/bmj.n71
17. Schardt, C., Adams, M. B., Owens, T., Keitz, S., & Fontelo, P. (2007).
Utilization of the PICO framework to improve searching PubMed for clinical
questions. BMC Medical Informatics and Decision Making, 7, 16.
https://doi.org/10.1186/1472-6947-7-16
18. Devi, R. A., Sabitha, B., Raffik, R., & Akila, K. (2023). IoT device security
for smart-card fraud detection for credit cards. In Proceedings of the 2nd
International Conference on Advancements in Electrical, Electronics,
Communication, Computing and Automation (ICAECA 2023) (pp. 1–6). IEEE.
https://doi.org/10.1109/ICAECA56562.2023.10199738
19. Kumar, P., Kumar, R., Gupta, G. P., & Tripathi, R. (2021). A distributed
framework for detecting DDoS attacks in smart contract-based blockchain–IoT
systems using fog computing. Transactions on Emerging Telecommunications
Technologies, 32(12), e4112. https://doi.org/10.1002/ett.4112

ACCAERPTTICEDLE M IANN PURSECSRSIPT
20. Garg, A., Pandey, M., & Pathak, A. R. (2024). A multi-layered AI–IoT
framework for adaptive financial services. International Journal of Emerging
Technologies in Computer Science and Information Technology.
https://doi.org/10.63282/3050-9246.IJETCSIT-V5I3P105
21. Benameur, R., Dahane, A., Souihi, S., & Mellouk, A. (2024). A novel
federated learning-based intrusion detection system for IoT networks. IEEE
Internet of Things Journal. Advance online publication.
https://ieeexplore.ieee.org/document/10622538
22. Rehman, A., Awan, K. A., Al-Rasheed, A., Ara, A., Alruwaili, F. F., Al-
Otaibi, S., & Saba, T. (2025). A hybrid fuzzy logic and federated learning
framework for cybersecurity and fraud detection in IoT-enabled metaverse
transactions. Engineering Intelligence Journal.
https://doi.org/10.1016/j.eij.2025.100668
23. Vankayalapati, R. K., Syed, S., Jayalakshmi, S., Mandala, G., Yadav, O. P.,
& Yadav, A. K. (2025). A robust and scalable deep learning framework for
real-time IoT intrusion detection with adaptive energy efficiency and
adversarial resilience. SSRN Electronic Journal.
https://doi.org/10.2139/ssrn.5077791
24. Prakash, V., Odedina, O., Kumar, A., Garg, LS., & Bawa, S. (2024). A
S
secure framework for Internet of Things anomalies using machine learning.
E
Discover Artificial Intelligence. https://Rdoi.org/10.1007/s43926-024-00088-z
P
25. Goyal, H. R., Husain, S. O., Dixit, K. K., Boob, N. S., Reddy, B. R., Kumar,
N
J., & Sharma, S. (2024). Advanced deep learning approaches for real-time
I
anomaly detection in IoT env ironments. IEEE Sensors Journal.
E
https://ieeexplore.ieee.oLrg/document/10829306
C
26. Choi, D., & Lee, K. (2018). An artificial intelligence approach to financial
I
fraud detection Tunder IoT environments. Journal of Sensors, 2018, Article
R
5483472. https://doi.org/10.1155/2018/5483472
A
27. Subhalaxmi, A., Kishorekumar, V., Leela Prasad, V., Deekshitha, G. A. V.,
& Varma, S. L. S. (2023). Credit card fraud detection using multi-layer
perceptron based on federated learning. International Journal for Research
Trends and Innovation, 8(6), 552–556.
https://www.ijrti.org/papers/IJRTI2306087.pdf
28. Min, M., Lee, J. J., Park, H., & Lee, K. (2021). Detecting anomalous
transactions via an IoT-based application: A machine learning approach.
Sensors, 21(6), 2039. https://doi.org/10.3390/s21062039
29. Abubakar, A., Ali, M. H., & Darma, T. H. (2024). Digital twin and IoT-
enabled online learning model for real-time monitoring and control of
fraudulent transactions in banking. Kabul Journal of Computer Science, 1(3), 1–
12. https://doi.org/10.47514/kjcs/2024.1.3.0018
30. Murthy, V. S. N., Kumari, R., Goyal, M., Dubey, P., & Ramesh, P. (2024).
Edge AI in IoT: Leveraging cloud computing and big data for intelligent
decision-making. Journal of Information Systems Engineering and
Management, 10(20S). https://doi.org/10.52783/jisem.v10i20s.3194
31. Kafila, H., Mohammad, H., Veena, C., Singla, A., Joshi, A., & Lourens, M.
(2024). Fraud detection in IoT-based financial transactions using anomaly

ACCAERPTTICEDLE M IANN PURSECSRSIPT
detection techniques. IEEE International Conference on Smart Computing.
https://ieeexplore.ieee.org/document/10602423
32. Maddukuri, N. (2022). Real-time fraud detection using IoT and AI: Securing
the digital wallet. Journal of Computing and Emerging Technologies, 5(1), 8.
https://doi.org/10.34218/JCET_5_01_008
33. Owusu-Mensah, K., Yaokumah, W., & Ansong, E. D. (2025). A
comprehensive review of techniques for detecting and preventing card-not-
present (CNP) fraud. In Innovations in Cryptocrime and Financial Fraud (pp.
283–314). IGI Global. https://doi.org/10.4018/979-8-3373-0675-9.ch008
Declarations
Acknowledgement: Fig. 1 and Fig. 6 were created using AI-generated content from
ChatGPT (OpenAI). The authors confirm that no human likenesses, copyrighted
elements, or misleading representations are included in the image.
Fig. 5 was created by the authors using a combination of ChatGPT(OpenAI)-assisted
conceptual design, Mermaid syntax for structured archSitectural modeling, and Draw.io
S
for visual refinement and layout optimization. All architectural interpretations, design
E
decisions, and final visual representations are Rthe authors’ own.
P
Funding Statement: Not applicable N
I
E
Author Contributions: KwaLbena Owusu-Mensah: Conceptualization; methodology;
C
formal analysis; thematic analysis and synthesis; writing – original manuscript text;
I
prepared all figures aTnd tables. Edward Danso Ansong, Kofi Sarpong Adu-Manu,
R
Winfred Yaokumah: Supervision; validation; review and editing; methodological
A
guidance; final approval of the manuscript. All authors reviewed the manuscript.
Ethics Approval: Not applicable
Conflicts of Interest: The authors declare no conflicts of interest related to the present
study.
Consent to Participate: Not applicable
Consent to Publish: Not applicable
Clinical Trial Number: Not applicable
Availability of Data and Materials: not applicable
Code Availability: Not applicable

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Acronyms
AI - Artificial Intelligence
AS - Article Studies
CNN - Convolutional Neural Network
CNP - Card-Not-Present
DDoS - Distributed Denial-of-Service
DL - Deep Learning
DP - Differential Privacy
ETT - Emerging Telecommunications Technologies
FedAvg - Federated Averaging
FedGAT-DCNN - Federated Graph Attention Network-Dilated Convolution Neural
Network
FedGroup - Federated Learning Grouping Framework
FedOpt - Federated Optimization
FedProx - Federated Proximal
FGCS - Future Generation Computer Systems
FL - Federated Learning
S
GANs – Generative Adversarial Networks
S
GNN – Graph Neural Network E
R
IDS – Intrusion Detection System
P
IIoT – Industrial Internet of Things
N
IoT – Internet of Things
I
IPFS – InterPlanetary File Syste m
E
JNSM - Journal of NetworLk and Systems Management
C
LSTM – Long Short-Term Memory
I
T
ML – Machine Learning
R
MLP – MultAi-Layer Perceptron
NFC – Near Field Communication
Non-IID – Non-independent and non-identically distributed
NSL-KDD – Network Security Laboratory–Knowledge Discovery in Databases
PCI DSS – Payment Card Industry Data Security Standard
QUIC – Quick UDP Internet Connections, a transport-layer protocol designed to
support low-latency, secure communication
RF – Random Forest
RFID – Radio Frequency Identification
RNN – Recurrent Neural Network
SMOTE – Synthetic Minority Oversampling Technique
UNSW-NB15 – University of New South Wales-Network-Based Intrusion
Detection Dataset
XAI – Explainable Artificial Intelligence
XGBoost – Extreme Gradient Boosting
Key Words and Terms
Adaptive Learning - Techniques that enable models to dynamically adjust to new
data and evolving conditions.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Anomaly Detection - Methods identifying data patterns significantly deviating from
typical or expected behaviors.
Auditability - Ability of a system to maintain traceable and verifiable records for
regulatory and compliance purposes.
Behavioral Biometrics - User authentication based on unique behavioral
characteristics such as typing patterns, gestures, or mouse movements.
Behavioral Profiling - Analysis and characterization of user activities to identify
and predict potentially fraudulent behaviors.
Blockchain - Decentralized, distributed ledger technology ensuring data integrity,
transparency, immutability, and security.
Cloud Computing - Remote delivery and management of computing services
(servers, storage, analytics) over the internet.
Concept Drift - Changes over time in the underlying distribution or characteristics
of data, impacting model performance.
Context-Awareness - Ability of systems to interpret and react appropriately to
environmental or situational contexts in real-time.
Data Privacy - Protection of personal and sensitive data against unauthorized access
or misuse.
Decentralization - Distribution of control and dSecision-making from a central
S
authority to multiple dispersed nodes or entities.
E
Deep Learning - Advanced subset of macRhine learning involving neural networks
P
with multiple layers for complex data analysis.
N
Digital Twin - Virtual representation of physical systems used for real-time
I
simulation, monitoring, and ana lysis.
E
Edge Computing - DistribLuted computing approach where data processing occurs
C
at or near the source, reducing latency.
I
Edge Intelligence T- Deployment of intelligent computation models directly on edge
R
devices for immediate processing and decision-making.
A
Explainable AI (XAI) - Techniques that ensure artificial intelligence decisions are
understandable and transparent to users.
Federated Averaging (FedAvg) - A widely used algorithm in federated learning,
designed for training machine learning models across decentralized data sources
without directly sharing the data.
Federated Learning - Machine learning paradigm enabling decentralized model
training across distributed devices while preserving data privacy.
Federated Proximal (FedProx) - refers to the combination of two concepts in
machine learning: Federated Learning (FL) and proximal optimization.
FedGAT-DCNN - employs federated learning, allowing financial institutions to
collaboratively train models using local datasets, enhancing accuracy and robustness
while maintaining data privacy.
Flower Framework - an open-source software framework for building federated
AI systems, including federated learning, analytics, and evaluation
Fog Computing - Distributed computing architecture positioned closer to end-user
devices, bridging cloud computing and edge computing.
Fuzzy Logic - Reasoning methodology handling uncertainty and approximate
reasoning rather than precise binary decisions.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Hybrid Models - Frameworks integrating multiple modeling methodologies (e.g.,
federated learning, fuzzy logic) to enhance predictive capabilities.
Interoperability - Capability of disparate systems and devices to effectively
exchange and use information.
Latency - Time delay between initiating an action and observing its effect or
response.
Lightweight Models - Computationally efficient models optimized for performance
on devices with limited processing power and memory.
Multi-Layered Framework - Architectural approach involving multiple layers
(e.g., perception, processing, application, governance) to enhance system
functionality and security.
Multi-Modal Data - Data derived from multiple distinct sources or types (e.g.,
biometric, transactional, behavioral).
Non-IID - datasets where individual data points are not independent and identically
distributed. This means the data points do not all come from the same underlying
probability distribution, and there may be dependencies or correlations between
them.
Oversampling - Technique addressing dataset imbalance by increasing instances of
underrepresented classes to improve model trainingS.
S
Privacy-Preserving Techniques - Approaches ensuring sensitive data remains
E
confidential and secure during data processRing and analysis.
P
Real-Time Detection - Immediate analysis and response to data as it is generated or
N
observed.
I
Real-time detection systems – systems capable of performing fraud evaluation
E
during the transaction auLthorization process. These systems typically rely on
C
streaming analytics, edge inference, or low-latency machine learning models.
I
Near real-time detTection systems – systems that analyze transactions shortly after
R
they occur, usually within seconds or minutes, and are used to trigger alerts,
A
additional authentication, or transaction reversal mechanisms.
Regulatory Compliance - Adherence of systems and processes to established
standards, laws, and regulations, such as PCI DSS.
Resource-Constrained Devices - Devices with limited computational capabilities,
storage, and power supply.
Scalability - Capacity of a system to efficiently manage increased workloads or
expanded operational scopes without performance degradation.
Secure Aggregation - Technique for securely combining model updates or data
inputs without compromising individual data privacy.
Smart Contract - Self-executing contracts with encoded business logic on
blockchain, automating enforcement and verification processes.