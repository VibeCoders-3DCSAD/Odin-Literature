---
conversion_metadata:
  converted_at: "2026-07-21T14:11:30Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Mareedu.pdf"
  source_pdf_sha256: "09a07927f9a90d59becba534e7c754ccb7fd030716c179c178ec610090b43535"
  page_count: 12
  markdown_char_count: 110197
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of Emerging Research in Engineering and Technology 
Pearl Blue Research Group| Volume 4, Issue 4, 53-64, 2023 
ISSN: 3050-922X | https://doi.org/10.63282/3050-922X.IJERET-V4I4P106

Original Article

Zero Trust before the Hype: Foundational Concepts and Early 
AI-Driven Implementations

Anitha Mareedu 
Electrical engineering Texas A&M University - Kingsville 700 University Blvd, Kingsville.

Abstract - The dynamic cloud environment, mobility workforces and the continuously growing cyber threats have triggered a 
transition of perimeter-based defences to Zero Trust Architectures (ZTAs). This review presents a comprehensive analysis of 
how Artificial Intelligence (AI) has been integrated into early uses of Zero Trust. Such formative AI-ZT systems implemented 
mechanisms  such  as  behavioural  authentication,  adaptive  trust  scores,  federated  learning  and  running  smart  contracts  to 
generate flexible and situational access controls. We look into the current technological foundations behind the early AI-ZT, 
including  edge  computing,  orchestration  and  training  on  decentralised  model  training  over  microservice  autonomy.  In 
particular, special attention is paid to the application of AI in the access pattern prediction, event tokenisation and risk-driven 
policy adaptation. The problem of data privacy, the security of models, and limitations in distributed systems are presented in 
terms  of  initial  implementations.  Basing  its  insights  on  them,  the  paper  speculates  on  how  the  experience  of  AI-ZT  systems 
contributed  to  the  current  security  paradigm,  estimating  the  integration  of  DevSecOps  with  AI,  SecAI  systems,  and  AI-
facilitated  context  processing.  Timelines  and  corresponding  comparative  tables  have  also  been  provided  to  visualise  the 
development of AI-ZT models and other pitfalls that a variety of solutions face. Finally, other new trends that we discuss are 
Zero  Trust  agents,  which  are  autonomous,  harmonisation  of  world  policies  and  AI  ethics.  This  review  aims  to  serve  as  a 
critical foundation for researchers and practitioners building the next generation of intelligent, resilient Zero Trust systems.

Keywords - Zero Trust Architecture (ZTA); Identity-Centric Security;  Network Segmentation;  Microservices Security; Secure 
Access Models; Cybersecurity Policy;  Federated Identity Management.

1. Introduction

The Zero Trust (ZT) security model is a paradigm shift in the architecture of cybersecurity due to which the traditionally 
accumulated  reference  to  the  protection  of  the  perimeter  is  being  disrupted  [1].  Already,  in  the  2010s,  researchers  and 
practitioners  started  to  be  sceptical  of  traditional  security  practices  and  techniques  that  presupposed  the  implicit  trust  of  the 
elements of the internal network. This assumption is undermined by the main principle of Zero Trust, which is the assumption 
that  says,  Never  Trust,  Always  Verify,  which  will  mandate  that  any  access  request  should  be  validated  through  multiple 
authentication, authorisation, and verification, irrespective of their origin as well as network location [2]. Firewalls, intrusion 
prevention  systems  (IPS) and  virtual  private networks  (VPNs)  are  some  of  the tools  which have  historically  been  applied to 
protect the enterprise perimeter [3]. This strategy was sufficient when assets used to be centrally controlled, users used to sit at 
the office and network boundaries used to be well defined. Nonetheless, the emergence of cloud computing, mobile endpoints, 
IoT devices, and hybrid workplaces has made the perimeter defence obsolete. Incidences of exploitation of lateral movement 
and credential compromise came in as attackers started exploiting this method, hence subverting faith inside the network since 
one trusts others, which is a further insecurity (4).

Figure  1  illustrates  this  paradigm  shift,  contrasting  perimeter-centric  models  with  identity-  and  behaviour-centric  Zero

Trust architectures.

Fig 1: Shift from Perimeter-Based Security to Zero Trust Architecture

---

<!-- PAGE 2 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

The initial development of Zero Trust centred around three major pillars: robust identity and access management (IAM), 
micro-segmentation  of  all  networks  and  services  and  offering  access  using  fine-grained  access  policies[5].  These 
implementations were largely static and were manually configured. Yet, with more and more data and more dynamic and ever-
evolving  threats,  static  rules  and  policies  started  falling  short.  This  led  to  the  integration  of  artificial  intelligence  (AI)  and 
machine  learning  (ML)  into  Zero  Trust  models.  Real-time  behavioural  analytics,  dynamic  risk  scoring  and  adaptive  access 
control are capabilities that may be critical in contemporary digital ecosystems made possible by AI. To give an example, ML 
algorithms  may  acquire  the  baselines  of  user  and  device  behaviours,  thus  being  able  to  detect  anomalies  like  access  at  an 
unusual time or a new location without informing the system with hardcoded rules (6). Essentially, AI augments the decision-
making capability of ZT systems, which can create a responsive and intelligent decision engine that automatically answers to 
changes in evolving and developing threats.

The said capabilities are not a luxury of a modern world but an evolutionary basis of the practical implementation of the 
Zero  Trust  [7].  Years  before  the  recent  and  current  hype  surrounding  Zero  Trust,  progressive  companies  and  university 
researchers were already using AI to contextualise identity, mechanise responses, and restrict access controls to achieve more 
precision in moving environments. These integrations formed the foundation for what is now advanced in Zero Trust platforms 
provided  by  cloud  providers  and  enterprise  vendors.  The remaining  sections  are  as  follows:  Section  2  with  an  outline of  the 
background of Zero Trust principles. Section 3 discusses the idea of how ZT was treated by early businesses until it became 
popular.  Section  4  talks  about  the  enabling  technologies,  especially  edge  computing  and  microservices.  Early  AI-based 
implementations  are  provided  in  section  5.  Section  6  presents  problems  related  to  the  use  of  AI  on  ZT.  Section  7  is  a 
distillation of lessons learnt, and Section 8 looks to the future directions.

2. Foundational Concepts of Zero Trust

Zero Trust is another approach and has a transition type of solving security problems by letting go of a perimeter-orientated 
security  model  and  replacing  it  with  an  identity-based  secure  method.  Zero  Trust  forces  authentication  and  continuous 
validation of access points instead of preconceiving that something within the network is trustworthy [8]. This part investigates 
the history of Zero Trust in addition to critical frameworks, which supremacized its ideas, and how the presuppositions of it 
changed and developed in the manner of access control using AI.

2.1. Core Philosophy: “Never Trust, Always Verify”

Zero Trust is governed by a central philosophy: assume breach, verify continuously. It abandons the outdated assumption

that anything inside the network perimeter is inherently safe.

2.1.1. Key Principles of Zero Trust 
The foundational tenets of ZT include:

  Continuous verification: All identities and devices must be authenticated and authorized in real time. 
  Least privilege access: Users are granted only the minimum level of access necessary for their role. 
  Microsegmentation: Network resources are divided into smaller zones, reducing lateral movement. 
  Assume breach: systems must be designed with the expectation that breaches are inevitable.

These  principles  align  with  the  Zero  Trust  Maturity  Model  proposed  by  the  U.S.  National  Institute  of  Standards  and

Technology (NIST) in its 800-207 publication, which established ZT as a formal architectural paradigm [9].

2.2. Evolution and Institutionalization of Zero Trust

The conceptual roots of ZT date back to the early 2000s, but its formal introduction reshaped modern cybersecurity policy

[10].

2.2.1. Forrester's Role

Analyst John Kindervag at Forrester Research coined the term Zero Trust in response to evolving security threats and the

failure of traditional perimeter models to adapt to cloud, BYOD, and mobile computing environments [11].

2.2.2. NIST SP 800-207 
Later,  NIST  Special  Publication  800-207  provided  a  standardised  framework  for  Zero  Trust  architecture.  This  document 
emphasised:

  Policy enforcement based on identity, context, and device posture 
  The need for dynamic trust evaluation 


Integration with existing enterprise systems (9)

This convergence of public and private efforts signalled a broader institutional shift toward Zero Trust adoption.

54

---

<!-- PAGE 3 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

2.3. Building Blocks of Zero Trust Architecture 
Zero Trust is not a single product but a combination of strategies, tools, and enforcement mechanisms.

2.3.1. Access Control Mechanisms 
Zero Trust depends on granular access control strategies. These include:

  Role-Based Access Control (RBAC) 
  Attribute-Based Access Control (ABAC) 
  Risk-Adaptive Access Control (RAAC)

Each model adds a new layer of contextual awareness, improving decision-making regarding access permissions [12].

2.3.2. Network Segmentation

ZT  encourages  the  use  of  microperimeters,  restricting  access  even  within  trusted  zones.  Microsegmentation  is  used  to 
isolate workloads and devices, reducing the risk of lateral threat propagation. This ensures that if an attacker gains entry to one 
zone, the damage remains contained [13].

2.4. Bridging the Perimeter and Identity Models

While  perimeter-based  security  relies  on  firewalls  and  trusted  zones,  Zero  Trust  is  identity-driven.  It  verifies  each  user,

device, and workload before granting access [14].

2.4.1. Traditional vs. Zero Trust 
The table below illustrates key differences:

Table 1: Comparison of Traditional Perimeter vs Zero Trust Models

Feature 
Trust Model 
Identity-Based Access 
Network Segmentation 
Authentication 
Threat Containment 
Policy Enforcement

Traditional Security  Zero Trust Architecture 
Trust inside perimeter 
Trust nothing, verify all 
Central to access decisions 
Limited 
Microsegmentation 
Minimal 
Continuous verification 
One-time login 
Built-in by design 
Limited 
Dynamic and adaptive 
Static

2.4.2. Transition Challenges 
Organisations shifting to ZT face challenges including:

  Legacy system integration 
  User experience trade-offs 
  Cultural resistance to identity-first security models

However,  as  more  people  work  remotely,  hybrid  clouds  are  used,  and  access  via  mobile,  an  identity-based  trust  is  an

unavoidable move [15].

Zero  Trust  has  a  solid  philosophy  and  architecture.  ZT  presents  a  flexible  solution  against  modern  security  threats  by 
removing  trust-based  behaviours  and  replacing  them  with  persistent  verification  and  changing  the  enforcement  of  static 
policies to flexible and identity-sensitive policy enforcement systems. The fact that it has expanded over the course of multiple 
years to be used as a federal standard indicates a sense of urgency in which enterprises and governments are taking on trustless 
frameworks,  especially  as  AI  allows  further  considerations  to  be  taken  when  making  access  control  decisions  that  move 
beyond the review of a simple user identity.

3. Pre-Hype Zero Trust Enterprise Systems

Some  enterprises  started  exploring  the  basic  tenets  of  the  Zero  Trust  Architecture  (ZTA)  several  years  before  the 
terminology acquired the status of a buzzword in the cybersecurity discourse after 2018. Much of this work tended to be split 
up and situation-dependent but provided an important foundation for the more standardised work that became NIST 800-207. 
Pre-hype  Zero  Trust  in  enterprise  settings  entailed  their  implementation  of  identity-based  controls,  federated  identity,  and 
adaptive  access  rule  enforcement  of  a  kind  without  always  appending  the  phrase  Zero  Trust to  the  effort.  We  examine  such 
early implementations, consider identity governance and behavioural modelling, and the ham-fisted application of AIs to assist 
in access control.

3.1. The Prevailing Early Use of Enterprises

Early perimeter-based protections have historically been used by the enterprises, yet as of the beginning of the 2010s, there

was a transition due to the movement to the cloud, remote work, and changing threat environments.

55

---

<!-- PAGE 4 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

3.1.1. Transition from Castle-and-Moat to Identity-Based Models

Legacy models such as the castle-and-moat technique started to crack as the organisations understood that internal threats 
and credential disclosures could outflank the  external security perimeter. The reduction of trust in internal networks by using 
user identity  as  the  first  principal  source  of  trust  began  to  emerge  within  enterprises.  Federated  identity  systems  came along 
with such protocols as SAML and OAuth to enable secure authentication of distributed systems [16].

3.1.2. Multifactor Authentication (MFA) Distribution

Deployment  of  MFA  was  inevitable  as  it  became  a  management  process  in  need  of  deployment  across  industries. 
Enterprises  imposed  stricter  controls  over  access  by  using  the  combination  of  something  the  user  knows  (password),  has 
(token) or is (biometrics). Not labelled as Zero Trust, these implementations were quite close to the concept of never trusting 
anything unless it is verified[17].

3.2. Lifecycle Management of Identities

Identity  validation  was  a  very  important  aspect;  however,  identity-provisioned  governance  to  govern  access  and  ensure

continuous review was another area of concern, as was emphasised by early adopters.

3.2.1. First Generation IAM Governance Models

RBAC became one of the most fundamental propositions of identity governance, where all rights were strictly allocated by 
roles but not according to expediency. Higher organisations tried the attribute-based access control (ABAC) to add contextual 
warping of place, type of device, and time of access.

Key components in early IAM governance included:

  Automated provisioning/deprovisioning of user accounts. 
  Periodic access reviews to detect privilege creep. 
  Centralised access logs to support audits and compliance.

3.2.2. Integration with HR and Directory Systems

Enterprises  started  integrating  IAM  systems  thoroughly  with  HR  databases  and  directory  services,  such  as  Active

Directory, to permit access rights to vary dynamically based on changes in employee lifecycle.

3.3. Behavioral modeling and Threat Context 
Security teams identified that fixed policies could not be used in the dynamic threat environment and insider threats.

3.3.1. Baselines and Detection of Anomalous Behaviour

Enterprises have been using crude behavioural profiling solutions long before the mainstream version of  User and Entity 
Behaviour Analytics (UEBA). These systems monitored the login time, usage of devices, and the accessing patterns to come 
up with baseline behaviours. Any anomaly, including logging on to an unusual location, would instigate warnings or temporary 
blockage of access [18].

3.3.2. Threat Intelligence to make Access Decisions

There  was  also  experimentation  in  the  organisational  setting  to  incorporate  threat  intelligence  feeds  to  modify  access 
control. As an example, the admission may be rejected even with valid credentials in case one of the device IPs was blacklisted 
(or blacklisted anywhere).

3.4. Early AI in Access Management

However, the use of artificial intelligence (AI) tools to enhance decision-making in access governance and risk detection

has been piloted by a number of enterprises even though this is still early.

3.4.1. Learning-Based Access Control Rule-Based

The earlier systems applied fixed rules, such as denying access in the case there is a login outside business hours. With the 
flow of time, AI-enhanced platforms started to employ supervised learning to detect small patterns of either abuse of privilege 
or dangerous behaviour. These tools have changed to what they do today, which is predicting risks.

3.4.2. AI Use Cases in Zero Trust Components 
Some notable early applications of AI in Zero Trust included: 
  Dynamic policy adjustments based on risk scores. 
  Predictive alerts from behavioural modelling engines. 
  Context-aware MFA triggers to selectively enforce strong authentication based on user or device behaviour.

56

---

<!-- PAGE 5 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

Such attempts, despite their modest nature, confirmed the possibilities of AI technology in minimising false positives as

well as scaling control access [19].

The  pre-hype  implementations  of  the  Zero  Trust  have  impacted  the  security  architectures  in  modern  days  significantly. 
Through  the  adoption  of  identity  federation,  governance  structures,  behavioural  analytics,  and  early  AI,  enterprises  primed 
themselves to be able to implement Zero Trust deployments more formally than post-NIST 800-207 publication. These initial 
approaches  proved  that  the  security  cannot  be  ensured  once  as  a  perimeter  protection  but  is  a  very  continuously  evolving 
process depending on the situation, which still to date is the guiding principle in the security of enterprises.

4. Microservices and Edge AI as Enabling Technology

Zero  Trust  approaches  are  built  not  only  on  policies  and  concepts  but  also  on  a  base  of  enablers.  Architectures  need  to 
change  as  enterprise  systems  become  more  distributed  and,  in  many  cases,  real-time  so  that  verification, access  control  and 
threat  detection  can  take  place  at  the  edge.  Edge  AI and  secure microservice  architectures  are  two  of  the  most revolutionary 
pillars to help this evolution.

4.1. Edge-based federated AI Access Control

In  legacy  environments,  the  verification  of  identities  and  so-called  enforcement  of  the  access  are  usually  performed  on 
centrally  deployed  systems.  But,  as  edge  computing  increases, most  important  decisions have now  to  be  made at the nearest 
data source at edge nodes. Federated AI makes it possible to train intelligent models locally (it is not necessary to transmit raw 
data over the network), and it maintains the privacy of data to improve real-time decisions. This is especially important to the 
case  of  Zero  Trust,  which  requires  non-stop  authentication  and  authorisation  in  a  local  context.  The  significant  latency  and 
bandwidth overheads inherent in the process of deploying AI models at the edge may also be minimised by means of efficient 
training  data  caching  algorithms  used  on  deep  learning  constructs  that  are  tailored  to  edge  computing  settings  [20].  The 
provided  advancements  allow  edge  nodes  to  engage  in  interconnected  threat  detection  and  data access  evaluation  while  still 
maintaining the necessary speed parameters and data privacy.

4.2. Secure Microservices, Mesh, and Services

When  monolithic  applications  are  being  replaced  by  microservice-based  systems,  every  single  service  may  become  a 
potential source of attack. All internal API calls in a zero-trust environment should be authenticated, authorised and encrypted. 
Kubernetes  orchestration and  service  mesh  (Istio  or  Linkerd) to  enable  protection  of  service-to-service  communication  lie at 
the heart  of  the  capability  to  enable  secure  operation in  the  dynamic  world  of  cloud-native  infrastructures. The microservice 
communication patterns need to be secure, and, as such, internal traffic is also subject to scrutiny. In such distributed systems, 
particularly  those  that  are  hyper-distributed,  such  as  in  latency-constrained  settings  such  as  in  an  optical  network, 
microservices should be architected to use Zero Trust communication patterns such as mutual TLS, policy-based routing and 
behavioural monitoring during run time[21].

Key security advantages provided by microservices and service meshes include:

  Granular Policy Enforcement: Security rules can be applied at the pod or container level. 
  Built-in Identity and Certificate Management:  Service meshes can issue and rotate certificates automatically. 
  Observability and Telemetry

Enhanced visibility into service-to-service interactions enables rapid threat detection and remediation.

4.3. Decentralized Trust Anchors and Policy Enforcement

In  order  to  expand  the  Zero  Trust  framework  into hybrid and  multi-cloud, trust anchors  will need  to  be  decentralised as 
well. In Zero Trust systems, trust verification and related policies are distributed and enforced at dozens of nodes, each with 
the  capability  to  verify  and  enforce  local  policies  based  on identity,  device  posture  and  contextual  signals.  Such a transition 
allows rapid, location-sensitive decision-making that does not need the time of round trips to a central server. Together with 
edge-based AI inference, local trust anchors can have better scaling and survivability even in branch offices, remote clinics, or 
industrial IoT contexts.

Figure 2 (see below) represents a conceptual architecture in which Zero Trust principles have been incorporated into edge 
nodes supported by AI engines and service meshes. Our architecture proposes to train newer instances of federated models on 
an on-demand basis to derive local behavioural baselines, signed and encrypted payloads to share microservices, and real-time 
decisions by decentralised policy agents to express access.

Edge  AI  and  microservices  do  not  only  enable  Zero  Trust  deployment,  but  they  are  also  its  precondition  in  the  current 
digital ecosystem [22]. Through them, there is easy verification, independent neighbourhoods, and safe communication at any 
contact  point.  As  more  workloads roll  out  to  more  decentralised  architectures, these  technologies  will  be  needed  in  order to 
provide necessary security for enforcing Zero Trust policies in a dynamic, efficient, and secure way.

57

---

<!-- PAGE 6 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

Fig 2: Idealized design of zero trust and AI-Enabled Edge Notes

5. AI-Driven Implementations in Early Zero Trust Systems

Due  to  the  further  development  of  enterprise networks  to  facilitate  work  outside  the  office  environment,  cloud  solutions, 
and the decentralisation of networks, Zero Trust mechanisms started incorporating elements of AI to enhance decision-making 
and  limit  manual  policy  control.  The  initial  ways  in  which  AI  has  been  used  in  Zero  Trust  frameworks  involve  making 
authentication and access controls dynamic, contextual, and adaptable to the behaviour of the users [23].

5.1. Adaptive Trust-Scoring and Behaviour Authentication via AI

Adaptive  trust  scoring  became  the  core  concept  of  this  transformation,  where  the  AI  algorithms  would  consider  a 
combination  of  multiple  factors,  including  user  behaviour,  device  posture,  geolocation,  and  access  times,  to  analyse  and 
provide dynamic trust ratings. These scores were able to replace any static access rules since they kept updating according to 
risk conditions, thus enabling systems to make certain decisions regarding authorisation of access or decline. In other words, a 
trusted user whose beard has been stolen may try to log in to a new device/geographic location at an unusual hour; the trust 
score  may  go  into  decline, initiating  a  step-up  process  or  flat refusal  of  authentication.  Such an  adaptive  model  diverted  the 
attention towards the probabilistic models of behaviour rather than binary credentials.

5.2. Behavioral authentication

Behavioural  authentication  proved  to  be  an  excellent  tool  to  strengthen real-time  identity.  Instead  of  using  passwords  or 
tokens only, systems monitored the typing behaviour, mouse and dynamics, and screen operation behaviour. Machine learning 
models were fed this kind of data to identify an anomaly, impersonations, or bot usage. These techniques of behaviour-based 
controls  contributed  considerably  to  Zero Trust  with  its  constant  verification  during the  session,  and not  only  at  the  point  of 
connection.

5.3. Predictive Modeling of Access Patterns

Besides  examining  behaviour  in  real  time,  AI  was  also  used  to  develop  predictive  access  behaviour  models.  Having 
historical access logs, granting of specific roles, and accessing patterns of resources, an early Zero Trust could predict future 
occurrences of certain actions. Any accesses to rarely used servers, unusual file transfers and the like would generate red flags, 
as they  would not have been predicted. Such predictive models did not just impair the security position but also assisted the 
organisation  to  block  the  insider  threats  and  lateral  movement  in  the  networks.  This  type  of  modelling  would  have  been 
particularly useful in such fast-paced environments as DevOps teams or financial trading platforms.

5.4. Smart Contracts in Enforcement of Policies

A new  way  to  use  AI  in  Zero Trust  was related to  smart  contracts  that use  blockchain  to  enforce  security  policies  in the 
distributed environment. Such smart contracts had rules of  access to  organisations embedded in them as self-executing code. 
Combined  with  AI  systems  which  interpreted  the  risk  context,  these  contracts  functioned  as  policy  oracles  conducting  the 
predefined  actions  only  in  case  of  the  correct  current  risk  profile  in  comparison  to  predefined  conditions  related  to  security 
conditions.  As  an  illustration,  it  would  be  possible  to  have  the  behaviour  of  the  user  checked  by  an  AI  engine  that  would 
provide a trust verdict to the smart contract, and that would grant or deny access without leveraging centralised servers. This 
paradigm  could  not  only  guarantee  transparency,  but  it  could  also  guarantee  decentralisation  [24].  The  pairing  of  smart 
contracts  and  AI  decision  engines  enabled  organisations  to curb response time in  the  process  of  access  management  without 
breaching internal or regulatory compliance levels. Besides, the audit trails created with these contracts could not be altered in 
any way and cannot be tampered with and therefore, can perform forensics analysis in the event of a breach.

58

---

<!-- PAGE 7 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

5.5. Tokenizing of an Event and Adaptation of AI Rules

One of the enabling factors to zeroing in on trust across all aspects of AI was the tokenisation of security events. Historical 
security  logs  would  also  be  verbose,  fragmented,  and  challenging  to  interpret  with  the  AI  model.  To  achieve  this 
standardisation and tokenisation of these events and render them to be ingested by AI engines in real time, researchers added 
asynchronous  SCIM  (System  for  Cross-domain  Identity  Management)  profiles  [25].  These  event  logs  were  tokenised  to 
include metadata  with  contexts,  presenting the  session ID, permission  scope,  IP  address,  device  status, and  user  behavioural 
history.  The  trained  AI models  based  on  these tokens  could  adapt rules, automatically  changing the  conditions  of  the  access 
control rules in response to the situation. To use an example, in the event such a mass of abnormal log-in attempts had been 
flagged in an area, AI would temporarily raise the authentication requirements or geo-block it. The rule adaptation also enabled 
systems to keep up with the emerging threats, thereby limiting the manual updates that were always required by the security 
team.

6. Challenges in Early AI-ZT Models

When  AI-enabled  Zero  Trust  (ZT)  architectures  started  appearing,  they  also  entailed  a  new  challenge  in  execution. 
Although  they  enshrined  the  promises  of  granularity  and  context-sensitive  access  control,  early  deployments  demonstrated 
several challenges of paramount importance in model performance and transparency, as well as infrastructural limitations [26].

6.1. Risks in Model Performance and Decision-Making

The  first  set  of  limitations revolved  around  the  trustworthiness  and robustness  of  AI-driven  decisions  within  ZT  models.

Early systems often struggled to strike a balance between precision and flexibility.

6.1.1. Over fitting and Limited Generalization

Many early AI-ZT models were trained on narrowly scoped datasets collected in controlled enterprise environments. As a 
result,  these  models  frequently  overfit  to  familiar  behavioural  patterns,  failing  to  generalise  to  novel  access  attempts  or 
anomalous  but  legitimate  user  behaviour.  This  resulted  in  either  false  positives  denying  legitimate  users  or  false  negatives, 
where threat actors bypassed detection due to lack of representative training data.

6.1.2. Decision Latency and Inaccuracy

AI  models,  especially  those  based  on  complex  deep  learning  architectures,  sometimes  introduced  latency  into  access 
control  workflows.  The  need  for  real-time  verification  clashed  with  model  complexity,  leading  to  slower  decisions  and,  in 
some  cases,  misclassifications.  Early  implementations  lacked  optimised  inference  pipelines  suitable  for  low-latency  edge 
deployment.

6.2. Governance and Policy Maintenance Issues

Beyond accuracy, ensuring policy consistency and governance within AI-enhanced ZT frameworks proved difficult. These

systems required constant recalibration to remain aligned with organisational objectives and regulatory compliance.

6.2.1. Policy Drift and Versioning Problems

AI-based  access  decisions  often  evolved  based  on  user  and  entity  behaviour.  While  this  adaptive  capability  enhanced 
flexibility, it also resulted in policy drift. Without strict versioning or rollback mechanisms, administrators struggled to  trace 
why certain decisions were made or to revert to known-good states after a model update.

6.2.2. Lack of Explainability and Auditability

Another  major  concern  was  the  opacity  of  decision-making.  Traditional  rule-based  systems  allowed  security  teams  to 
justify  actions  based  on  documented  rules.  However,  early  AI  models  lacked  explainability,  making  it  difficult  to  audit  or 
justify access denial or approval, especially in regulated sectors such as finance or healthcare. The inability to generate human-
readable justifications hindered trust in these systems (27).

6.3. Data Security and Model Integrity

One  of  the  foundational  elements  of  AI  is  access  to  quality  data.  However,  in  Zero  Trust  settings  where  sensitive  or

privileged information is constantly evaluated, ensuring data security and integrity becomes paramount.

6.3.1. Training Data Leakage Risks

Training AI models for ZT involved collecting behavioural telemetry, logs, and system access records, some of which were 
highly sensitive. Improper anonymisation or poor storage practices led to incidents of data leakage, posing significant privacy 
and compliance risks.

59

---

<!-- PAGE 8 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

6.3.2. Poisoning and Tampering in Distributed Training

When  federated  or  edge-based  training  was  employed,  attackers  could  inject  malicious  data  (poisoning)  or  compromise 
training endpoints. This introduced corrupted models into production environments, leading to backdoors or manipulated trust 
evaluations that bypassed normal security boundaries.

6.4. Infrastructure and Resource Constraints

Finally,  resource  limitations,  particularly  at  the  edge  or  in  mobile/IoT  environments,  imposed  hard  boundaries  on  what

could realistically be deployed.

6.4.1. Inference at the Edge

Early deployments in smart factories, healthcare edge nodes, or mobile workforces struggled with running computationally 
intensive models locally. Constraints such as battery power, limited CPU/GPU, and thermal throttling prevented real-time AI 
inference,  requiring  frequent  offloading  to  central  cloud  systems,  undermining  ZT's  goal  of  local,  decentralised  trust 
enforcement [28].

6.4.2. Scalability of Lightweight AI Models

While  lightweight  models  (e.g.,  decision  trees  or  compressed  neural  nets)  were  developed,  they  often  underperformed 
compared  to  full-scale  AI  counterparts.  Balancing  scalability,  latency,  and  accuracy  remained  a  persistent  struggle  through 
early ZT implementations

Table 2: Common Limitations of AI-Powered Zero Trust Deployments

Challenge Category

Description

Overfitting 
Policy Drift 
Lack of Explainability 
Training Data Leakage 
Infrastructure Limits

Poor generalization due to limited or biased training data 
Models evolve away from organizational security intent 
Difficulty in auditing and interpreting AI decisions 
Exposure of sensitive telemetry during collection or model tuning 
Edge nodes unable to support real-time inference due to hardware limits

7. Modern Zero Trust Designs

The  continuing  Zero  Trust  (ZT)  development  demonstrates  that  the  development  of  a  secure  and  resilient  enterprise 
architecture  requires  more  than  penetration  of  the  perimeter  or  a  static  rule  base.  The  experience  with  initial  experiments 
allowed  modern  Zero  Trust  implementations to  be  much  more  contextual  and integrated. and  dynamic  over  the  last  decade. 
The lessons still apply to the readiness of ZT systems in the future, which will have to cope with challenges that come with the 
use of hybrid cloud, IoT, and even quantum computing.

7.1. Rigid Policy to Flexible Access

First, Zero Trust models applied hard-coded and invariable rules to authorise access to a system by verifying identity and 
privileges.  Although  these  sets  of  rules  gave  out  a  level  of  predictability,  they  were  unable  to  cope  along  with  the  evolving 
nature of the user habits and network attacks. It was understood that static policy could do nothing to prevent credential abuse 
and lateral performance, as well as those dynamic insider attacks. Thus, organisations started to move to adaptive trust scoring, 
whereby  risk  was  constantly  assessed  with  the  aim  of  developing  AI  models  based  on  which  it  is  possible  to  change  the 
permissions  dynamically  [29].  This  change  enabled  Zero  Trust  to  no  longer  be  a  compliance-based  checklist  but  instead  an 
active security platform that understands context.

7.2. The Rise of the Context-Aware ZT Agents

Among the most effective harbingers was that the Zero Trust decisions need to encompass environmental and contextual 
cues. To handle data on device posture, location, user history, and even feeds on local threat intelligence, context-aware Zero 
Trust agents came into evidence. In such a way, these agents allowed more localised and responsive enforcement of policies, 
eliminating false alarms and catching low-level signs of compromise. These agents have shown that practical ZT is no longer a 
yes/no validation of an event but an ongoing, contextually dependent evaluation that occurs in near real time.

7.3. DevSecOps and SecAI Zero Trust alignment

Recent security trends lay a heavier focus on DevSecOps and Security AI (SecAI) approaches to implement the concepts of 
trust throughout the entire software development lifecycle. In its earliest Zero Trust designs, the reality became apparent that 
the  number  of  disconnected  security  points  enforcing  security  could  become  a  bottleneck  to  agile  and  cloud-native 
deployments. Experience in this area led to the integration of ZT controls with DevSecOps toolchains, which supports policy-
as-code,  pipeline-based  security  scans,  and  anomalous  behaviours  which  are  auto-detected.  Moreover,  the  combined  use  of 
SecAI  tools  and  the  application  of  ZT  decision  engines  offered  intelligent  and autonomously  enhancing  controls  that would 
adjust in accordance  with  changing  workloads and  temporary  container  surroundings.  Zero Trust  in this respect  has  become 
distributed in nature, such that it belongs to infrastructure, code, or data.

60

---

<!-- PAGE 9 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

7.4. Future Readiness: Hybrid Cloud, IoT, and Quantum Resilience

Since  the  technology  stack  is  expanding  to  involve  edge  IoT  equipment,  multi-cloud  workloads,  and  teams  that  are 
dispersed  across  parts  of  the  globe,  Zero  Trust  designs  should  be  adaptable, interoperable, and  scalable[30].  The necessities 
educated the practitioners to learn that decentralisation of trust anchors and the federation of identities play an important role in 
circumventing  chokepoints  and  ensuring resilience.  Moving  forward, it  may  seem  to  be  one  of  the most  significant  lessons; 
quantum-resistant algorithms and identity models will be essential to design Zero Trust systems because quantum computing 
will  be  the  future  trend  of  post-quantum  cryptography.  Incorporating  Zero  Trust  approaches  and  quantum-safe  standards  is 
becoming one of the proactive best practices to secure control and remain compliant in the long-term shift.

Fig 3: Evolution of Zero Trust Architecture: From static perimeter models

Figure 3 illustrates this shift by showing a timeline of Zero Trust evolution from traditional perimeter models to dynamic, 
AI-enhanced, and quantum-aware frameworks   providing a powerful visual of how security expectations have matured over 
the past decade.

These lessons have made Zero Trust a fully-fledged security architecture, not just a marketing buzz term, and built to be 
versatile and adaptable to real-world environments of modern-day digital businesses. Context-aware controls, keeping in line 
with DevSecOps and cryptography-ready organisations can design the Zero Trust systems that would truly be ready to confront 
the dynamic security environment in the upcoming quantum era.

8. Future Outlook and Research Directions

Zero  Trust  (ZT)  architecture  has  now  become  inseparably  linked  to  artificial  intelligence  (AI),  especially  its  spheres  of 
automation,  policy  creation,  and  governance  across  the  world.  With  the  extended  capabilities  of  AI,  the  vision  of  ZT  is 
extending perimeter-less access control into areas of self-adaptive security ecosystems. Some of the most important trends in 
the  future  of  AI-enabled  Zero  Trust  are  mentioned  in  the  current  passage  and  include  the  prominent  idea  of  the  usage  of 
autonomous agents and legal and ethical concerns.

8.1. Rise of Autonomous Zero Trust Agents

Autonomous  Zero  Trust  agents  driven  with  large  language  models  (LLM),  AI  copilots,  and  reinforcement  learning 
frameworks  are among  the  most  critical  areas,  as  it  will  be  applied and  deployed  in  the nearest  future.  Such agents  can also 
engage in contextual reasoning, dynamic risk analysis and independent decision-making.

8.1.1. AI Copilots and LLM-Based Trust Brokers

Embedding LLMs into ZT systems gives AI copilots the opportunity to aid real-time authorisation choices based  on user 
behaviour, the condition of the hardware, and the context under which operation policies are made. Such copilots even have 
the  ability  to  execute  zero-touch  configuration,  auto-remediate  alerts  and  describe  decisions  in  natural  language;  hence,  the 
division between technical enforcement and human control. An example could be how AI copilots could dynamically change 
access levels in real time as part of a live security incident based on the behavioural deviation or a threat intelligence feed.

8.1.2. Reinforcement Learning for Policy Refinement

With reinforcement learning, autonomous agents can dynamically optimize security policies based on the consequences of 
the  earlier  decisions  about  enforcement.  This  forms  a  cyclical  relationship  in  which  the  policies  are  not  limited  to  written 
scripts but are continuously seen to cross  over to become dynamic  programs internalized into the action of the environment. 
This kind of agent minimizes the time it takes to have human intervention in the case of fast-paced threats and enhances the 
correctness of decisions.

8.2. AI-Governed Policy Lifecycles

Traditionally,  policy  lifecycle  in  Zero  Trust  is  characterised  by  manual  definition,  approval,  deployment  and  auditing. 
Nevertheless,  today,  AI  has  the  capability  to  control  all  of  these  cycles,  decreasing  the  cost  of  administration  as  well  as 
precision.

61

---

<!-- PAGE 10 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

8.2.1. Dynamic Policy Authoring and Simulation

It  is  now  possible  to  gain  access  to  machine  learning  algorithms  that  generate  new  access  policies,  using  the  contextual 
data, like log-in time, geolocation of the devices, and last accessed histories. By foreseeing the impact of new policies on the 
work  before  applying  them,  AI  can  overcome  eventual  gaps  or  contradictions.  This  human  error  mitigation  factor  in  policy 
formulations is proactive and validating.

8.2.2. Lifecycle Automation and Drift Correction

The AI-based systems are capable of independently detecting policy drift, in which specified access rules get out of sync 
with  real-life  patterns  of  action.  They  can  update  antiquated  or  inefficient  rules  using  historical  baselines,  which  keeps  the 
various policies up to date in terms of the security specifications and compliance requirements.

8.3. International Enforcement and Standardization

As multi-cloud environments and distributed workforces are needed to scale up, the pressing concern is the deployment of

Zero Trust policies across geopolitical and jurisdictional barriers.

8.3.1. Federated ZT Enforcement Models

The new architectures promote the use of federated models of enforcement so that Zero Trust policies could be enforced in 
multiple domains and followed by local governance policies. These models are based on decentralised identity, cross-domain 
policy translation and metadata tagging in order to allow national infrastructures to interoperate.

8.3.2. Trust Interoperability and Global Security Standards

International standards should be harmonised before the future of ZT is controlled by AI, particularly when ZT control is 
incorporated in the supply chains, smart grids, and healthcare systems. Organisations like NIST, ENISA, and ISO are working 
to establish agreeable methods, spanning vocabularies of trust anchors and reference architectures to allow the work of people 
across the public and the private sectors to operate congruently.

8.4. Legal Issues of Ethics and Interpretability

Transparency,  accountability  and  human  rights  are  some  of  the  issues  considered  when  AI  is  introduced  in  security 
decision-making. Ethical governance "has to" grow at the same pace as technical capability because AI will impose access and 
identity controls.

8.4.1. Legal Implications of AI-Enforced Access Denials

Are  you  to  blame  when  an  AI  agent  fails  to  offer  or  rejects  permission  to  key  infrastructure  inappropriately?  This  is  a 
developing  field  of  apprehension  to  the  regulators.  Laws  should  explain  how  model  developers,  data  custodians,  and 
infrastructure providers can behave when the decision about access impacts the safety of the people or civil liberties.

8.4.2. Explainability and Regulatory Compliance

Innovations  like  store  and  accountal  claim  the  right  to  explanation  and  auditability  of  automated  decisions  that  are 
regulations. As such, explainable AI (XAI) would be crucial in Zero Trust environments that support both legally readable and 
technologically  sound  decision  logs.  AI-ZT  systems  in  the future  will require  providing human-interpretable  reasons  behind 
every execution action to meet the global requirements of data protection.

8.4.3. Ethical Design Principles for AI-ZT Systems

It will be necessary to incorporate into the algorithms of AI-ZT fairness, bias mitigation, and inclusiveness. Without a lot 
of caution, AI agents can carry with them discriminative effects, particularly those machines that judge users according to their 
behavioural character or accessibility records. Security vendors can probably expect to incorporate such frameworks as IEEE 
P7003  (Algorithmic  Bias  Considerations)  and  the  NIST  AI  Risk  Management  Framework  into  the  design  of  AI-ZTs  in  the 
future.

9. Conclusion

The  Zero  Trust  development  of  security  models,  a  shift  in  the  concept  of  static  perimeter  protections  to  dynamic 
technological architectures, is the point of inflection in the cybersecurity strategy. With increased uptake and usage of clouds, 
mobile workforces and IoT, the zero trust concept of never trust, always verify is no longer a choice but a requirement of the 
original zero trust tenet, zero trust. This review has discussed how Early artificial intelligence integrations, in specific, started 
creating transformations to disrupt traditional Zero Trust by making the systems more intelligent and more capable of dynamic 
decision-making situations. Through the use of machine learning, federated learning and intelligent policy orchestration, early 
AI-ZT  systems  also  provided  capabilities  such  as  behaviour-based  authentication,  dynamic  access  control  and  anomaly 
detection  at  a  non-human  scale.  Such  developments  made  the  foundation  of  autonomous  trust  engines  and  real-time 
enforcement mechanisms, which outsmarted static rule sets.

62

---

<!-- PAGE 11 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

However, there were also fresh vulnerabilities and architectural challenges that were presented by such innovations. The 
danger of overfitting the models, policy drift and opaque decision-making showed that the absence of accountability in the face 
of  intelligence  might  corrode  trust  among  the  interested  parties  or  stakeholders.  Explainability,  auditability,  and  regulatory 
compliance were open issues in most of the deployments, especially when AI-generated decisions were to deny access or raise 
suspicion. In addition, there were also threats due to training data integrity, adversarial inputs, and model drift in distributed AI 
systems  to  trust  computation in  sensitive  contexts. The  concept  of  optimisation and model  pruning, in addition  to  retraining 
with  federated  learning,  became  significant  due  to  real-time  execution  in  cases  with  extremely  constrained  resources, 
especially on an edge device.

But these inadequacies led to the future design plans. Earlier efforts of AI-ZT installations led to the development of more 
durable and explainable models that have AI controls, human in-the-room management functions, and explanatory features of 
AI models. The congruency of AI-ZT and DevSecOps also helped the security teams to apply the concepts of adaptive trust to 
the CI/CD pipeline so that policy enforcement could adapt to changes in the development lifecycle. Moving forward, zero trust 
is converging with autonomous agents and large language models in addition to quantum-resilient cryptographic standards as 
the  next-gen  digital  trust.  The  questions  about  cross-border  enforcement,  ethical  AI  limits,  and  international  security  norms 
require  the  cooperation  of  many  stakeholders  so  that  the power  of  AI  could  also  be  useful  in  good  ways.  A  fully  intelligent 
Zero Trust model is an evolutionary journey, back and forth and mutually integrated. Finally, automation of decisions, which 
aims to be the ultimate goal of hybridisation between Zero Trust and AI, should not be seen as some sort of improvement or 
yet another way to make decisions, but rather as a way to make these decisions transparent, equitable, secure, and flexible. The 
comparative  equilibrium  between  autonomy  and  control  that  does  not  compromise  the  trustworthiness  of  trust  should  be 
further perfected in the future research that will be conducted despite the emerging threats/

References 
[1]  Gilman, E., & Barth, D. (2017). Zero Trust Networks: Building Secure Systems in Untrusted Networks. Foundational work 
on the architecture and core principles of Zero Trust, including continuous verification and dynamic policy enforcement, 
drawing from NIST SP 800-207

[2]  Forrester Research (2010). Introduction of Zero Trust concept and category by John Kindervag. This marked the formal

framing of Zero Trust Architecture (ZTA) as a strategic cybersecurity model

[3]  Google  (2014). BeyondCorp  initiative. Early,  real-world  enterprise  application  of  Zero  Trust  principles allowing remote

work without VPNs, demonstrating early implementation of Zero Trust architecture

[4]  NIST  (2018).  NIST  SP  800-207:  Zero  Trust  Architecture.  Provided  the  formal  architectural  framework  and  guidelines

widely adopted in both government and private sectors

[5]  M.  R.  Islam,  M.  H.  Rehmani,  &  F.  C.  Delicato  (2021).  Zero  Trust  Security  Model  for  Cloud  Computing.  IEEE

Transactions on Cloud Computing, 9(4), 1024–1036.

[6]  S. Dixit, “The impact of quantum supremacy on cryptography: Implications for secure financial transactions,” Int. J. Sci.

Res. Comput. Sci. Eng. Inf. Technol., vol. 6, no. 4, pp. 611–637, 2020. doi: 10.32628/CSEIT2064141

[7]  S.  Ghasemshirazi,  G.  Shirvani,  and  M.  A.  Alipour,  “Zero  trust:  Applications,  challenges,  and  opportunities,”  arXiv

preprint, arXiv:2309.03582, 2023.

[8]  R.  Kumar,  A.  K.  Gupta,  &  V.  Gupta  (2021).  Zero  Trust  Architecture  and  Security:  A  Survey.  IEEE  Access,  9,  13572–

13590.

[9]  J. Chen & L. Zeng (2021). Machine  Learning-Based Anomaly  Detection for  Cloud  Security in  Financial  Systems. IEEE 
Transactions  on  Neural  Networks  and  Learning  Systems,  32(9),  4001–4013.  J.  Chen  &  L.  Zeng  (2021).  Machine 
Learning-Based Anomaly Detection for Cloud Security in Financial Systems. IEEE Transactions on Neural Networks and 
Learning Systems, 32(9), 4001–4013.

[10] W.  Yeoh  et al.,  “Zero  trust  cybersecurity:  Critical  success  factors and  a maturity  assessment  framework,”  Computers &

Security, vol. 133, 103412, 2023.

[11] J. Kindervag, “Build security into your network’s DNA: The zero trust network architecture,” Forrester Research Inc., vol.

27, pp. 1–16, 2010.

[12] C. C. Ike et al., “Redefining zero trust architecture in cloud networks: A conceptual shift towards granular, dynamic access

control and policy enforcement,” Magna Scientia Adv. Res. Rev., vol. 2, no. 1, pp. 074–086, 2021.

[13] D. Singh, P. R. Kumar, & R. D. Shukla (2021). AI-Driven Identity and Access Management in Zero Trust. IEEE Security

& Privacy, 19(3), 63–70.

[14] T.  F.  Hennessy  &  S.  A.  Khan  (2021).  Machine  Learning  for  Threat  Detection  in  Zero  Trust  Cloud  Security.  IEEE

Transactions on Dependable and Secure Computing, 18(3), 1293–1305.

[15] M.  V.  Chandran,  P.  P.  Agarwal,  &  A.  S.  Patel  (2021).  Machine  Learning for  Predictive  Threat  Detection  in  Zero  Trust

Cloud Networks. IEEE Transactions on Artificial Intelligence, 10(3), 578–590.

[16] J. M. Smith, A. H. Williams, & L. T. Chen (2022). AI-Augmented Policy Decision Points in Zero Trust Networks. IEEE

Journal on Selected Areas in Communications, 40(1), 112–125.

[17] R.  Patel  &  S.  Kapoor  (2022).  Adaptive  Machine  Learning-Driven  Access  Control  for  Zero  Trust  Architectures.

International Journal of Information Security, 21(4), 457–472.

63

---

<!-- PAGE 12 -->

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

[18] K.  Y.  Lee,  M.  S.  Tan,  &  Q.  Li  (2022).  Leveraging  Behavioral  Analytics  for  Insider  Threat  Detection  in  Zero  Trust

Environments. Computers & Security, 114, 102573.

[19] H. García-García, E. García-Cruz, & M. T. Álvarez (2021). A Hybrid Zero Trust Model Based on AI-Driven Risk Scoring

and Rule Enforcement. Future Generation Computer Systems, 117, 332–345.

[20] J. Jangid, “Efficient training data caching for deep learning in edge computing networks,” Int. J. Sci. Res. Comput. Sci.

Eng. Inf. Technol., vol. 7, no. 5, pp. 337–362, 2020. doi: 10.32628/CSEIT20631113

[21] S. Kumar, A. B. Rao, & N. Patel (2021). Explainable AI for Zero Trust: Transparent Decision-Making in Access Control.

ACM Computing Surveys, 54(7), 147.

[22] F. Al-Doghman et al., “AI-enabled secure microservices in edge computing: Opportunities and challenges,” IEEE Trans.

Serv. Comput., vol. 16, no. 2, pp. 1485–1504, 2022.

[23] L.  Zhang  &  P.  Sharma  (2021).  Federated  Learning  for  Decentralized  Zero  Trust  Access  Control  Across  Cloud-Edge

Environments. IEEE Internet of Things Journal, 8(14), 11023–11034.

[24] A. Z. Bashir, M. A. Khan, & F. I. Al-Turjman (2020). Reinforcement Learning in Zero Trust Network Orchestration for

Adaptive Security Posture. Expert Systems with Applications, 150, 113223.

[25] Y. Cao, X. Liu, & Z. W. Xu (2020). Deep Learning-Enabled Lateral Movement Detection within Zero Trust Frameworks.

Journal of Network and Computer Applications, 150, 102511.

[26] J.  Kwon,  H.-J.  Kim,  &  S.-Y.  Ko  (2022).  Predictive  Analytics  in  Zero  Trust:  Forecasting  Access  Threats  Using  Time-

Series Machine Learning. Computers & Security, 113, 102532.

[27] E. Lopez, R. Wang, & P. Hernandez (2022). Context-Aware AI for Dynamic Access Control in Zero Trust Environments.

ACM Transactions on Cyber-Physical Systems, 6(4), 37.

[28] D. Roberts & M. Patel (2021). Integrating Expert Systems with ML Models for Zero Trust Decision Engines. Journal of

Systems Architecture, 115, 102162.

[29] S.  Dixit,  “AI-powered  risk modeling  in  quantum  finance: Redefining  enterprise  decision  systems,”  Int.  J.  Sci.  Res.  Sci.

Eng. Technol., vol. 9, no. 4, pp. 547–572, 2022. doi: 10.32628/IJSRSET221656

[30] K. Li, Y. Zhou, & X. Xu (2020). Graph Neural Networks for Trust Assessment in Zero Trust Architectures. IEEE Access,

8, 212345–212356.

64

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal of Emerging Research in Engineering and Technology
Pearl Blue Research Group| Volume 4, Issue 4, 53-64, 2023
ISSN: 3050-922X | https://doi.org/10.63282/3050-922X.IJERET-V4I4P106

Original Article

Zero Trust before the Hype: Foundational Concepts and Early
AI-Driven Implementations

Anitha Mareedu
Electrical engineering Texas A&M University - Kingsville 700 University Blvd, Kingsville.

Abstract - The dynamic cloud environment, mobility workforces and the continuously growing cyber threats have triggered a
transition of perimeter-based defences to Zero Trust Architectures (ZTAs). This review presents a comprehensive analysis of
how Artificial Intelligence (AI) has been integrated into early uses of Zero Trust. Such formative AI-ZT systems implemented
mechanisms  such  as  behavioural  authentication,  adaptive  trust  scores,  federated  learning  and  running  smart  contracts  to
generate flexible and situational access controls. We look into the current technological foundations behind the early AI-ZT,
including  edge  computing,  orchestration  and  training  on  decentralised  model  training  over  microservice  autonomy.  In
particular, special attention is paid to the application of AI in the access pattern prediction, event tokenisation and risk-driven
policy adaptation. The problem of data privacy, the security of models, and limitations in distributed systems are presented in
terms  of  initial  implementations.  Basing  its  insights  on  them,  the  paper  speculates  on  how  the  experience  of  AI-ZT  systems
contributed  to  the  current  security  paradigm,  estimating  the  integration  of  DevSecOps  with  AI,  SecAI  systems,  and  AI-
facilitated  context  processing.  Timelines  and  corresponding  comparative  tables  have  also  been  provided  to  visualise  the
development of AI-ZT models and other pitfalls that a variety of solutions face. Finally, other new trends that we discuss are
Zero  Trust  agents,  which  are  autonomous,  harmonisation  of  world  policies  and  AI  ethics.  This  review  aims  to  serve  as  a
critical foundation for researchers and practitioners building the next generation of intelligent, resilient Zero Trust systems.

Keywords - Zero Trust Architecture (ZTA); Identity-Centric Security;  Network Segmentation;  Microservices Security; Secure
Access Models; Cybersecurity Policy;  Federated Identity Management.

1. Introduction

The Zero Trust (ZT) security model is a paradigm shift in the architecture of cybersecurity due to which the traditionally
accumulated  reference  to  the  protection  of  the  perimeter  is  being  disrupted  [1].  Already,  in  the  2010s,  researchers  and
practitioners  started  to  be  sceptical  of  traditional  security  practices  and  techniques  that  presupposed  the  implicit  trust  of  the
elements of the internal network. This assumption is undermined by the main principle of Zero Trust, which is the assumption
that  says,  Never  Trust,  Always  Verify,  which  will  mandate  that  any  access  request  should  be  validated  through  multiple
authentication, authorisation, and verification, irrespective of their origin as well as network location [2]. Firewalls, intrusion
prevention  systems  (IPS) and  virtual  private networks  (VPNs)  are  some  of  the tools  which have  historically  been  applied to
protect the enterprise perimeter [3]. This strategy was sufficient when assets used to be centrally controlled, users used to sit at
the office and network boundaries used to be well defined. Nonetheless, the emergence of cloud computing, mobile endpoints,
IoT devices, and hybrid workplaces has made the perimeter defence obsolete. Incidences of exploitation of lateral movement
and credential compromise came in as attackers started exploiting this method, hence subverting faith inside the network since
one trusts others, which is a further insecurity (4).

Figure  1  illustrates  this  paradigm  shift,  contrasting  perimeter-centric  models  with  identity-  and  behaviour-centric  Zero

Trust architectures.

Fig 1: Shift from Perimeter-Based Security to Zero Trust Architecture

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

The initial development of Zero Trust centred around three major pillars: robust identity and access management (IAM),
micro-segmentation  of  all  networks  and  services  and  offering  access  using  fine-grained  access  policies[5].  These
implementations were largely static and were manually configured. Yet, with more and more data and more dynamic and ever-
evolving  threats,  static  rules  and  policies  started  falling  short.  This  led  to  the  integration  of  artificial  intelligence  (AI)  and
machine  learning  (ML)  into  Zero  Trust  models.  Real-time  behavioural  analytics,  dynamic  risk  scoring  and  adaptive  access
control are capabilities that may be critical in contemporary digital ecosystems made possible by AI. To give an example, ML
algorithms  may  acquire  the  baselines  of  user  and  device  behaviours,  thus  being  able  to  detect  anomalies  like  access  at  an
unusual time or a new location without informing the system with hardcoded rules (6). Essentially, AI augments the decision-
making capability of ZT systems, which can create a responsive and intelligent decision engine that automatically answers to
changes in evolving and developing threats.

The said capabilities are not a luxury of a modern world but an evolutionary basis of the practical implementation of the
Zero  Trust  [7].  Years  before  the  recent  and  current  hype  surrounding  Zero  Trust,  progressive  companies  and  university
researchers were already using AI to contextualise identity, mechanise responses, and restrict access controls to achieve more
precision in moving environments. These integrations formed the foundation for what is now advanced in Zero Trust platforms
provided  by  cloud  providers  and  enterprise  vendors.  The remaining  sections  are  as  follows:  Section  2  with  an  outline of  the
background of Zero Trust principles. Section 3 discusses the idea of how ZT was treated by early businesses until it became
popular.  Section  4  talks  about  the  enabling  technologies,  especially  edge  computing  and  microservices.  Early  AI-based
implementations  are  provided  in  section  5.  Section  6  presents  problems  related  to  the  use  of  AI  on  ZT.  Section  7  is  a
distillation of lessons learnt, and Section 8 looks to the future directions.

2. Foundational Concepts of Zero Trust

Zero Trust is another approach and has a transition type of solving security problems by letting go of a perimeter-orientated
security  model  and  replacing  it  with  an  identity-based  secure  method.  Zero  Trust  forces  authentication  and  continuous
validation of access points instead of preconceiving that something within the network is trustworthy [8]. This part investigates
the history of Zero Trust in addition to critical frameworks, which supremacized its ideas, and how the presuppositions of it
changed and developed in the manner of access control using AI.

2.1. Core Philosophy: “Never Trust, Always Verify”

Zero Trust is governed by a central philosophy: assume breach, verify continuously. It abandons the outdated assumption

that anything inside the network perimeter is inherently safe.

2.1.1. Key Principles of Zero Trust
The foundational tenets of ZT include:

  Continuous verification: All identities and devices must be authenticated and authorized in real time.
  Least privilege access: Users are granted only the minimum level of access necessary for their role.
  Microsegmentation: Network resources are divided into smaller zones, reducing lateral movement.
  Assume breach: systems must be designed with the expectation that breaches are inevitable.

These  principles  align  with  the  Zero  Trust  Maturity  Model  proposed  by  the  U.S.  National  Institute  of  Standards  and

Technology (NIST) in its 800-207 publication, which established ZT as a formal architectural paradigm [9].

2.2. Evolution and Institutionalization of Zero Trust

The conceptual roots of ZT date back to the early 2000s, but its formal introduction reshaped modern cybersecurity policy

[10].

2.2.1. Forrester's Role

Analyst John Kindervag at Forrester Research coined the term Zero Trust in response to evolving security threats and the

failure of traditional perimeter models to adapt to cloud, BYOD, and mobile computing environments [11].

2.2.2. NIST SP 800-207
Later,  NIST  Special  Publication  800-207  provided  a  standardised  framework  for  Zero  Trust  architecture.  This  document
emphasised:

  Policy enforcement based on identity, context, and device posture
  The need for dynamic trust evaluation


Integration with existing enterprise systems (9)

This convergence of public and private efforts signalled a broader institutional shift toward Zero Trust adoption.

54

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

2.3. Building Blocks of Zero Trust Architecture
Zero Trust is not a single product but a combination of strategies, tools, and enforcement mechanisms.

2.3.1. Access Control Mechanisms
Zero Trust depends on granular access control strategies. These include:

  Role-Based Access Control (RBAC)
  Attribute-Based Access Control (ABAC)
  Risk-Adaptive Access Control (RAAC)

Each model adds a new layer of contextual awareness, improving decision-making regarding access permissions [12].

2.3.2. Network Segmentation

ZT  encourages  the  use  of  microperimeters,  restricting  access  even  within  trusted  zones.  Microsegmentation  is  used  to
isolate workloads and devices, reducing the risk of lateral threat propagation. This ensures that if an attacker gains entry to one
zone, the damage remains contained [13].

2.4. Bridging the Perimeter and Identity Models

While  perimeter-based  security  relies  on  firewalls  and  trusted  zones,  Zero  Trust  is  identity-driven.  It  verifies  each  user,

device, and workload before granting access [14].

2.4.1. Traditional vs. Zero Trust
The table below illustrates key differences:

Table 1: Comparison of Traditional Perimeter vs Zero Trust Models

Feature
Trust Model
Identity-Based Access
Network Segmentation
Authentication
Threat Containment
Policy Enforcement

Traditional Security  Zero Trust Architecture
Trust inside perimeter
Trust nothing, verify all
Central to access decisions
Limited
Microsegmentation
Minimal
Continuous verification
One-time login
Built-in by design
Limited
Dynamic and adaptive
Static

2.4.2. Transition Challenges
Organisations shifting to ZT face challenges including:

  Legacy system integration
  User experience trade-offs
  Cultural resistance to identity-first security models

However,  as  more  people  work  remotely,  hybrid  clouds  are  used,  and  access  via  mobile,  an  identity-based  trust  is  an

unavoidable move [15].

Zero  Trust  has  a  solid  philosophy  and  architecture.  ZT  presents  a  flexible  solution  against  modern  security  threats  by
removing  trust-based  behaviours  and  replacing  them  with  persistent  verification  and  changing  the  enforcement  of  static
policies to flexible and identity-sensitive policy enforcement systems. The fact that it has expanded over the course of multiple
years to be used as a federal standard indicates a sense of urgency in which enterprises and governments are taking on trustless
frameworks,  especially  as  AI  allows  further  considerations  to  be  taken  when  making  access  control  decisions  that  move
beyond the review of a simple user identity.

3. Pre-Hype Zero Trust Enterprise Systems

Some  enterprises  started  exploring  the  basic  tenets  of  the  Zero  Trust  Architecture  (ZTA)  several  years  before  the
terminology acquired the status of a buzzword in the cybersecurity discourse after 2018. Much of this work tended to be split
up and situation-dependent but provided an important foundation for the more standardised work that became NIST 800-207.
Pre-hype  Zero  Trust  in  enterprise  settings  entailed  their  implementation  of  identity-based  controls,  federated  identity,  and
adaptive  access  rule  enforcement  of  a  kind  without  always  appending  the  phrase  Zero  Trust to  the  effort.  We  examine  such
early implementations, consider identity governance and behavioural modelling, and the ham-fisted application of AIs to assist
in access control.

3.1. The Prevailing Early Use of Enterprises

Early perimeter-based protections have historically been used by the enterprises, yet as of the beginning of the 2010s, there

was a transition due to the movement to the cloud, remote work, and changing threat environments.

55

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

3.1.1. Transition from Castle-and-Moat to Identity-Based Models

Legacy models such as the castle-and-moat technique started to crack as the organisations understood that internal threats
and credential disclosures could outflank the  external security perimeter. The reduction of trust in internal networks by using
user identity  as  the  first  principal  source  of  trust  began  to  emerge  within  enterprises.  Federated  identity  systems  came along
with such protocols as SAML and OAuth to enable secure authentication of distributed systems [16].

3.1.2. Multifactor Authentication (MFA) Distribution

Deployment  of  MFA  was  inevitable  as  it  became  a  management  process  in  need  of  deployment  across  industries.
Enterprises  imposed  stricter  controls  over  access  by  using  the  combination  of  something  the  user  knows  (password),  has
(token) or is (biometrics). Not labelled as Zero Trust, these implementations were quite close to the concept of never trusting
anything unless it is verified[17].

3.2. Lifecycle Management of Identities

Identity  validation  was  a  very  important  aspect;  however,  identity-provisioned  governance  to  govern  access  and  ensure

continuous review was another area of concern, as was emphasised by early adopters.

3.2.1. First Generation IAM Governance Models

RBAC became one of the most fundamental propositions of identity governance, where all rights were strictly allocated by
roles but not according to expediency. Higher organisations tried the attribute-based access control (ABAC) to add contextual
warping of place, type of device, and time of access.

Key components in early IAM governance included:

  Automated provisioning/deprovisioning of user accounts.
  Periodic access reviews to detect privilege creep.
  Centralised access logs to support audits and compliance.

3.2.2. Integration with HR and Directory Systems

Enterprises  started  integrating  IAM  systems  thoroughly  with  HR  databases  and  directory  services,  such  as  Active

Directory, to permit access rights to vary dynamically based on changes in employee lifecycle.

3.3. Behavioral modeling and Threat Context
Security teams identified that fixed policies could not be used in the dynamic threat environment and insider threats.

3.3.1. Baselines and Detection of Anomalous Behaviour

Enterprises have been using crude behavioural profiling solutions long before the mainstream version of  User and Entity
Behaviour Analytics (UEBA). These systems monitored the login time, usage of devices, and the accessing patterns to come
up with baseline behaviours. Any anomaly, including logging on to an unusual location, would instigate warnings or temporary
blockage of access [18].

3.3.2. Threat Intelligence to make Access Decisions

There  was  also  experimentation  in  the  organisational  setting  to  incorporate  threat  intelligence  feeds  to  modify  access
control. As an example, the admission may be rejected even with valid credentials in case one of the device IPs was blacklisted
(or blacklisted anywhere).

3.4. Early AI in Access Management

However, the use of artificial intelligence (AI) tools to enhance decision-making in access governance and risk detection

has been piloted by a number of enterprises even though this is still early.

3.4.1. Learning-Based Access Control Rule-Based

The earlier systems applied fixed rules, such as denying access in the case there is a login outside business hours. With the
flow of time, AI-enhanced platforms started to employ supervised learning to detect small patterns of either abuse of privilege
or dangerous behaviour. These tools have changed to what they do today, which is predicting risks.

3.4.2. AI Use Cases in Zero Trust Components
Some notable early applications of AI in Zero Trust included:
  Dynamic policy adjustments based on risk scores.
  Predictive alerts from behavioural modelling engines.
  Context-aware MFA triggers to selectively enforce strong authentication based on user or device behaviour.

56

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

Such attempts, despite their modest nature, confirmed the possibilities of AI technology in minimising false positives as

well as scaling control access [19].

The  pre-hype  implementations  of  the  Zero  Trust  have  impacted  the  security  architectures  in  modern  days  significantly.
Through  the  adoption  of  identity  federation,  governance  structures,  behavioural  analytics,  and  early  AI,  enterprises  primed
themselves to be able to implement Zero Trust deployments more formally than post-NIST 800-207 publication. These initial
approaches  proved  that  the  security  cannot  be  ensured  once  as  a  perimeter  protection  but  is  a  very  continuously  evolving
process depending on the situation, which still to date is the guiding principle in the security of enterprises.

4. Microservices and Edge AI as Enabling Technology

Zero  Trust  approaches  are  built  not  only  on  policies  and  concepts  but  also  on  a  base  of  enablers.  Architectures  need  to
change  as  enterprise  systems  become  more  distributed  and,  in  many  cases,  real-time  so  that  verification, access  control  and
threat  detection  can  take  place  at  the  edge.  Edge  AI and  secure microservice  architectures  are  two  of  the  most revolutionary
pillars to help this evolution.

4.1. Edge-based federated AI Access Control

In  legacy  environments,  the  verification  of  identities  and  so-called  enforcement  of  the  access  are  usually  performed  on
centrally  deployed  systems.  But,  as  edge  computing  increases, most  important  decisions have now  to  be  made at the nearest
data source at edge nodes. Federated AI makes it possible to train intelligent models locally (it is not necessary to transmit raw
data over the network), and it maintains the privacy of data to improve real-time decisions. This is especially important to the
case  of  Zero  Trust,  which  requires  non-stop  authentication  and  authorisation  in  a  local  context.  The  significant  latency  and
bandwidth overheads inherent in the process of deploying AI models at the edge may also be minimised by means of efficient
training  data  caching  algorithms  used  on  deep  learning  constructs  that  are  tailored  to  edge  computing  settings  [20].  The
provided  advancements  allow  edge  nodes  to  engage  in  interconnected  threat  detection  and  data access  evaluation  while  still
maintaining the necessary speed parameters and data privacy.

4.2. Secure Microservices, Mesh, and Services

When  monolithic  applications  are  being  replaced  by  microservice-based  systems,  every  single  service  may  become  a
potential source of attack. All internal API calls in a zero-trust environment should be authenticated, authorised and encrypted.
Kubernetes  orchestration and  service  mesh  (Istio  or  Linkerd) to  enable  protection  of  service-to-service  communication  lie at
the heart  of  the  capability  to  enable  secure  operation in  the  dynamic  world  of  cloud-native  infrastructures. The microservice
communication patterns need to be secure, and, as such, internal traffic is also subject to scrutiny. In such distributed systems,
particularly  those  that  are  hyper-distributed,  such  as  in  latency-constrained  settings  such  as  in  an  optical  network,
microservices should be architected to use Zero Trust communication patterns such as mutual TLS, policy-based routing and
behavioural monitoring during run time[21].

Key security advantages provided by microservices and service meshes include:

  Granular Policy Enforcement: Security rules can be applied at the pod or container level.
  Built-in Identity and Certificate Management:  Service meshes can issue and rotate certificates automatically.
  Observability and Telemetry

 Enhanced visibility into service-to-service interactions enables rapid threat detection and remediation.

4.3. Decentralized Trust Anchors and Policy Enforcement

In  order  to  expand  the  Zero  Trust  framework  into hybrid and  multi-cloud, trust anchors  will need  to  be  decentralised as
well. In Zero Trust systems, trust verification and related policies are distributed and enforced at dozens of nodes, each with
the  capability  to  verify  and  enforce  local  policies  based  on identity,  device  posture  and  contextual  signals.  Such a transition
allows rapid, location-sensitive decision-making that does not need the time of round trips to a central server. Together with
edge-based AI inference, local trust anchors can have better scaling and survivability even in branch offices, remote clinics, or
industrial IoT contexts.

Figure 2 (see below) represents a conceptual architecture in which Zero Trust principles have been incorporated into edge
nodes supported by AI engines and service meshes. Our architecture proposes to train newer instances of federated models on
an on-demand basis to derive local behavioural baselines, signed and encrypted payloads to share microservices, and real-time
decisions by decentralised policy agents to express access.

Edge  AI  and  microservices  do  not  only  enable  Zero  Trust  deployment,  but  they  are  also  its  precondition  in  the  current
digital ecosystem [22]. Through them, there is easy verification, independent neighbourhoods, and safe communication at any
contact  point.  As  more  workloads roll  out  to  more  decentralised  architectures, these  technologies  will  be  needed  in  order to
provide necessary security for enforcing Zero Trust policies in a dynamic, efficient, and secure way.

57

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

Fig 2: Idealized design of zero trust and AI-Enabled Edge Notes

5. AI-Driven Implementations in Early Zero Trust Systems

Due  to  the  further  development  of  enterprise networks  to  facilitate  work  outside  the  office  environment,  cloud  solutions,
and the decentralisation of networks, Zero Trust mechanisms started incorporating elements of AI to enhance decision-making
and  limit  manual  policy  control.  The  initial  ways  in  which  AI  has  been  used  in  Zero  Trust  frameworks  involve  making
authentication and access controls dynamic, contextual, and adaptable to the behaviour of the users [23].

5.1. Adaptive Trust-Scoring and Behaviour Authentication via AI

Adaptive  trust  scoring  became  the  core  concept  of  this  transformation,  where  the  AI  algorithms  would  consider  a
combination  of  multiple  factors,  including  user  behaviour,  device  posture,  geolocation,  and  access  times,  to  analyse  and
provide dynamic trust ratings. These scores were able to replace any static access rules since they kept updating according to
risk conditions, thus enabling systems to make certain decisions regarding authorisation of access or decline. In other words, a
trusted user whose beard has been stolen may try to log in to a new device/geographic location at an unusual hour; the trust
score  may  go  into  decline, initiating  a  step-up  process  or  flat refusal  of  authentication.  Such an  adaptive  model  diverted  the
attention towards the probabilistic models of behaviour rather than binary credentials.

5.2. Behavioral authentication

Behavioural  authentication  proved  to  be  an  excellent  tool  to  strengthen real-time  identity.  Instead  of  using  passwords  or
tokens only, systems monitored the typing behaviour, mouse and dynamics, and screen operation behaviour. Machine learning
models were fed this kind of data to identify an anomaly, impersonations, or bot usage. These techniques of behaviour-based
controls  contributed  considerably  to  Zero Trust  with  its  constant  verification  during the  session,  and not  only  at  the  point  of
connection.

5.3. Predictive Modeling of Access Patterns

Besides  examining  behaviour  in  real  time,  AI  was  also  used  to  develop  predictive  access  behaviour  models.  Having
historical access logs, granting of specific roles, and accessing patterns of resources, an early Zero Trust could predict future
occurrences of certain actions. Any accesses to rarely used servers, unusual file transfers and the like would generate red flags,
as they  would not have been predicted. Such predictive models did not just impair the security position but also assisted the
organisation  to  block  the  insider  threats  and  lateral  movement  in  the  networks.  This  type  of  modelling  would  have  been
particularly useful in such fast-paced environments as DevOps teams or financial trading platforms.

5.4. Smart Contracts in Enforcement of Policies

A new  way  to  use  AI  in  Zero Trust  was related to  smart  contracts  that use  blockchain  to  enforce  security  policies  in the
distributed environment. Such smart contracts had rules of  access to  organisations embedded in them as self-executing code.
Combined  with  AI  systems  which  interpreted  the  risk  context,  these  contracts  functioned  as  policy  oracles  conducting  the
predefined  actions  only  in  case  of  the  correct  current  risk  profile  in  comparison  to  predefined  conditions  related  to  security
conditions.  As  an  illustration,  it  would  be  possible  to  have  the  behaviour  of  the  user  checked  by  an  AI  engine  that  would
provide a trust verdict to the smart contract, and that would grant or deny access without leveraging centralised servers. This
paradigm  could  not  only  guarantee  transparency,  but  it  could  also  guarantee  decentralisation  [24].  The  pairing  of  smart
contracts  and  AI  decision  engines  enabled  organisations  to curb response time in  the  process  of  access  management  without
breaching internal or regulatory compliance levels. Besides, the audit trails created with these contracts could not be altered in
any way and cannot be tampered with and therefore, can perform forensics analysis in the event of a breach.

58

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

5.5. Tokenizing of an Event and Adaptation of AI Rules

One of the enabling factors to zeroing in on trust across all aspects of AI was the tokenisation of security events. Historical
security  logs  would  also  be  verbose,  fragmented,  and  challenging  to  interpret  with  the  AI  model.  To  achieve  this
standardisation and tokenisation of these events and render them to be ingested by AI engines in real time, researchers added
asynchronous  SCIM  (System  for  Cross-domain  Identity  Management)  profiles  [25].  These  event  logs  were  tokenised  to
include metadata  with  contexts,  presenting the  session ID, permission  scope,  IP  address,  device  status, and  user  behavioural
history.  The  trained  AI models  based  on  these tokens  could  adapt rules, automatically  changing the  conditions  of  the  access
control rules in response to the situation. To use an example, in the event such a mass of abnormal log-in attempts had been
flagged in an area, AI would temporarily raise the authentication requirements or geo-block it. The rule adaptation also enabled
systems to keep up with the emerging threats, thereby limiting the manual updates that were always required by the security
team.

6. Challenges in Early AI-ZT Models

When  AI-enabled  Zero  Trust  (ZT)  architectures  started  appearing,  they  also  entailed  a  new  challenge  in  execution.
Although  they  enshrined  the  promises  of  granularity  and  context-sensitive  access  control,  early  deployments  demonstrated
several challenges of paramount importance in model performance and transparency, as well as infrastructural limitations [26].

6.1. Risks in Model Performance and Decision-Making

The  first  set  of  limitations revolved  around  the  trustworthiness  and robustness  of  AI-driven  decisions  within  ZT  models.

Early systems often struggled to strike a balance between precision and flexibility.

6.1.1. Over fitting and Limited Generalization

Many early AI-ZT models were trained on narrowly scoped datasets collected in controlled enterprise environments. As a
result,  these  models  frequently  overfit  to  familiar  behavioural  patterns,  failing  to  generalise  to  novel  access  attempts  or
anomalous  but  legitimate  user  behaviour.  This  resulted  in  either  false  positives  denying  legitimate  users  or  false  negatives,
where threat actors bypassed detection due to lack of representative training data.

6.1.2. Decision Latency and Inaccuracy

AI  models,  especially  those  based  on  complex  deep  learning  architectures,  sometimes  introduced  latency  into  access
control  workflows.  The  need  for  real-time  verification  clashed  with  model  complexity,  leading  to  slower  decisions  and,  in
some  cases,  misclassifications.  Early  implementations  lacked  optimised  inference  pipelines  suitable  for  low-latency  edge
deployment.

6.2. Governance and Policy Maintenance Issues

Beyond accuracy, ensuring policy consistency and governance within AI-enhanced ZT frameworks proved difficult. These

systems required constant recalibration to remain aligned with organisational objectives and regulatory compliance.

6.2.1. Policy Drift and Versioning Problems

AI-based  access  decisions  often  evolved  based  on  user  and  entity  behaviour.  While  this  adaptive  capability  enhanced
flexibility, it also resulted in policy drift. Without strict versioning or rollback mechanisms, administrators struggled to  trace
why certain decisions were made or to revert to known-good states after a model update.

6.2.2. Lack of Explainability and Auditability

Another  major  concern  was  the  opacity  of  decision-making.  Traditional  rule-based  systems  allowed  security  teams  to
justify  actions  based  on  documented  rules.  However,  early  AI  models  lacked  explainability,  making  it  difficult  to  audit  or
justify access denial or approval, especially in regulated sectors such as finance or healthcare. The inability to generate human-
readable justifications hindered trust in these systems (27).

6.3. Data Security and Model Integrity

One  of  the  foundational  elements  of  AI  is  access  to  quality  data.  However,  in  Zero  Trust  settings  where  sensitive  or

privileged information is constantly evaluated, ensuring data security and integrity becomes paramount.

6.3.1. Training Data Leakage Risks

Training AI models for ZT involved collecting behavioural telemetry, logs, and system access records, some of which were
highly sensitive. Improper anonymisation or poor storage practices led to incidents of data leakage, posing significant privacy
and compliance risks.

59

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

6.3.2. Poisoning and Tampering in Distributed Training

When  federated  or  edge-based  training  was  employed,  attackers  could  inject  malicious  data  (poisoning)  or  compromise
training endpoints. This introduced corrupted models into production environments, leading to backdoors or manipulated trust
evaluations that bypassed normal security boundaries.

6.4. Infrastructure and Resource Constraints

Finally,  resource  limitations,  particularly  at  the  edge  or  in  mobile/IoT  environments,  imposed  hard  boundaries  on  what

could realistically be deployed.

6.4.1. Inference at the Edge

Early deployments in smart factories, healthcare edge nodes, or mobile workforces struggled with running computationally
intensive models locally. Constraints such as battery power, limited CPU/GPU, and thermal throttling prevented real-time AI
inference,  requiring  frequent  offloading  to  central  cloud  systems,  undermining  ZT's  goal  of  local,  decentralised  trust
enforcement [28].

6.4.2. Scalability of Lightweight AI Models

While  lightweight  models  (e.g.,  decision  trees  or  compressed  neural  nets)  were  developed,  they  often  underperformed
compared  to  full-scale  AI  counterparts.  Balancing  scalability,  latency,  and  accuracy  remained  a  persistent  struggle  through
early ZT implementations

Table 2: Common Limitations of AI-Powered Zero Trust Deployments

Challenge Category

Description

Overfitting
Policy Drift
Lack of Explainability
Training Data Leakage
Infrastructure Limits

Poor generalization due to limited or biased training data
Models evolve away from organizational security intent
Difficulty in auditing and interpreting AI decisions
Exposure of sensitive telemetry during collection or model tuning
Edge nodes unable to support real-time inference due to hardware limits

7. Modern Zero Trust Designs

The  continuing  Zero  Trust  (ZT)  development  demonstrates  that  the  development  of  a  secure  and  resilient  enterprise
architecture  requires  more  than  penetration  of  the  perimeter  or  a  static  rule  base.  The  experience  with  initial  experiments
allowed  modern  Zero  Trust  implementations to  be  much  more  contextual  and integrated. and  dynamic  over  the  last  decade.
The lessons still apply to the readiness of ZT systems in the future, which will have to cope with challenges that come with the
use of hybrid cloud, IoT, and even quantum computing.

7.1. Rigid Policy to Flexible Access

First, Zero Trust models applied hard-coded and invariable rules to authorise access to a system by verifying identity and
privileges.  Although  these  sets  of  rules  gave  out  a  level  of  predictability,  they  were  unable  to  cope  along  with  the  evolving
nature of the user habits and network attacks. It was understood that static policy could do nothing to prevent credential abuse
and lateral performance, as well as those dynamic insider attacks. Thus, organisations started to move to adaptive trust scoring,
whereby  risk  was  constantly  assessed  with  the  aim  of  developing  AI  models  based  on  which  it  is  possible  to  change  the
permissions  dynamically  [29].  This  change  enabled  Zero  Trust  to  no  longer  be  a  compliance-based  checklist  but  instead  an
active security platform that understands context.

7.2. The Rise of the Context-Aware ZT Agents

Among the most effective harbingers was that the Zero Trust decisions need to encompass environmental and contextual
cues. To handle data on device posture, location, user history, and even feeds on local threat intelligence, context-aware Zero
Trust agents came into evidence. In such a way, these agents allowed more localised and responsive enforcement of policies,
eliminating false alarms and catching low-level signs of compromise. These agents have shown that practical ZT is no longer a
yes/no validation of an event but an ongoing, contextually dependent evaluation that occurs in near real time.

7.3. DevSecOps and SecAI Zero Trust alignment

Recent security trends lay a heavier focus on DevSecOps and Security AI (SecAI) approaches to implement the concepts of
trust throughout the entire software development lifecycle. In its earliest Zero Trust designs, the reality became apparent that
the  number  of  disconnected  security  points  enforcing  security  could  become  a  bottleneck  to  agile  and  cloud-native
deployments. Experience in this area led to the integration of ZT controls with DevSecOps toolchains, which supports policy-
as-code,  pipeline-based  security  scans,  and  anomalous  behaviours  which  are  auto-detected.  Moreover,  the  combined  use  of
SecAI  tools  and  the  application  of  ZT  decision  engines  offered  intelligent  and autonomously  enhancing  controls  that would
adjust in accordance  with  changing  workloads and  temporary  container  surroundings.  Zero Trust  in this respect  has  become
distributed in nature, such that it belongs to infrastructure, code, or data.

60

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

7.4. Future Readiness: Hybrid Cloud, IoT, and Quantum Resilience

Since  the  technology  stack  is  expanding  to  involve  edge  IoT  equipment,  multi-cloud  workloads,  and  teams  that  are
dispersed  across  parts  of  the  globe,  Zero  Trust  designs  should  be  adaptable, interoperable, and  scalable[30].  The necessities
educated the practitioners to learn that decentralisation of trust anchors and the federation of identities play an important role in
circumventing  chokepoints  and  ensuring resilience.  Moving  forward, it  may  seem  to  be  one  of  the most  significant  lessons;
quantum-resistant algorithms and identity models will be essential to design Zero Trust systems because quantum computing
will  be  the  future  trend  of  post-quantum  cryptography.  Incorporating  Zero  Trust  approaches  and  quantum-safe  standards  is
becoming one of the proactive best practices to secure control and remain compliant in the long-term shift.

Fig 3: Evolution of Zero Trust Architecture: From static perimeter models

Figure 3 illustrates this shift by showing a timeline of Zero Trust evolution from traditional perimeter models to dynamic,
AI-enhanced, and quantum-aware frameworks   providing a powerful visual of how security expectations have matured over
the past decade.

These lessons have made Zero Trust a fully-fledged security architecture, not just a marketing buzz term, and built to be
versatile and adaptable to real-world environments of modern-day digital businesses. Context-aware controls, keeping in line
with DevSecOps and cryptography-ready organisations can design the Zero Trust systems that would truly be ready to confront
the dynamic security environment in the upcoming quantum era.

8. Future Outlook and Research Directions

Zero  Trust  (ZT)  architecture  has  now  become  inseparably  linked  to  artificial  intelligence  (AI),  especially  its  spheres  of
automation,  policy  creation,  and  governance  across  the  world.  With  the  extended  capabilities  of  AI,  the  vision  of  ZT  is
extending perimeter-less access control into areas of self-adaptive security ecosystems. Some of the most important trends in
the  future  of  AI-enabled  Zero  Trust  are  mentioned  in  the  current  passage  and  include  the  prominent  idea  of  the  usage  of
autonomous agents and legal and ethical concerns.

8.1. Rise of Autonomous Zero Trust Agents

Autonomous  Zero  Trust  agents  driven  with  large  language  models  (LLM),  AI  copilots,  and  reinforcement  learning
frameworks  are among  the  most  critical  areas,  as  it  will  be  applied and  deployed  in  the nearest  future.  Such agents  can also
engage in contextual reasoning, dynamic risk analysis and independent decision-making.

8.1.1. AI Copilots and LLM-Based Trust Brokers

Embedding LLMs into ZT systems gives AI copilots the opportunity to aid real-time authorisation choices based  on user
behaviour, the condition of the hardware, and the context under which operation policies are made. Such copilots even have
the  ability  to  execute  zero-touch  configuration,  auto-remediate  alerts  and  describe  decisions  in  natural  language;  hence,  the
division between technical enforcement and human control. An example could be how AI copilots could dynamically change
access levels in real time as part of a live security incident based on the behavioural deviation or a threat intelligence feed.

8.1.2. Reinforcement Learning for Policy Refinement

With reinforcement learning, autonomous agents can dynamically optimize security policies based on the consequences of
the  earlier  decisions  about  enforcement.  This  forms  a  cyclical  relationship  in  which  the  policies  are  not  limited  to  written
scripts but are continuously seen to cross  over to become dynamic  programs internalized into the action of the environment.
This kind of agent minimizes the time it takes to have human intervention in the case of fast-paced threats and enhances the
correctness of decisions.

8.2. AI-Governed Policy Lifecycles

Traditionally,  policy  lifecycle  in  Zero  Trust  is  characterised  by  manual  definition,  approval,  deployment  and  auditing.
Nevertheless,  today,  AI  has  the  capability  to  control  all  of  these  cycles,  decreasing  the  cost  of  administration  as  well  as
precision.

61

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

8.2.1. Dynamic Policy Authoring and Simulation

It  is  now  possible  to  gain  access  to  machine  learning  algorithms  that  generate  new  access  policies,  using  the  contextual
data, like log-in time, geolocation of the devices, and last accessed histories. By foreseeing the impact of new policies on the
work  before  applying  them,  AI  can  overcome  eventual  gaps  or  contradictions.  This  human  error  mitigation  factor  in  policy
formulations is proactive and validating.

8.2.2. Lifecycle Automation and Drift Correction

The AI-based systems are capable of independently detecting policy drift, in which specified access rules get out of sync
with  real-life  patterns  of  action.  They  can  update  antiquated  or  inefficient  rules  using  historical  baselines,  which  keeps  the
various policies up to date in terms of the security specifications and compliance requirements.

8.3. International Enforcement and Standardization

As multi-cloud environments and distributed workforces are needed to scale up, the pressing concern is the deployment of

Zero Trust policies across geopolitical and jurisdictional barriers.

8.3.1. Federated ZT Enforcement Models

The new architectures promote the use of federated models of enforcement so that Zero Trust policies could be enforced in
multiple domains and followed by local governance policies. These models are based on decentralised identity, cross-domain
policy translation and metadata tagging in order to allow national infrastructures to interoperate.

8.3.2. Trust Interoperability and Global Security Standards

International standards should be harmonised before the future of ZT is controlled by AI, particularly when ZT control is
incorporated in the supply chains, smart grids, and healthcare systems. Organisations like NIST, ENISA, and ISO are working
to establish agreeable methods, spanning vocabularies of trust anchors and reference architectures to allow the work of people
across the public and the private sectors to operate congruently.

8.4. Legal Issues of Ethics and Interpretability

Transparency,  accountability  and  human  rights  are  some  of  the  issues  considered  when  AI  is  introduced  in  security
decision-making. Ethical governance "has to" grow at the same pace as technical capability because AI will impose access and
identity controls.

8.4.1. Legal Implications of AI-Enforced Access Denials

Are  you  to  blame  when  an  AI  agent  fails  to  offer  or  rejects  permission  to  key  infrastructure  inappropriately?  This  is  a
developing  field  of  apprehension  to  the  regulators.  Laws  should  explain  how  model  developers,  data  custodians,  and
infrastructure providers can behave when the decision about access impacts the safety of the people or civil liberties.

8.4.2. Explainability and Regulatory Compliance

Innovations  like  store  and  accountal  claim  the  right  to  explanation  and  auditability  of  automated  decisions  that  are
regulations. As such, explainable AI (XAI) would be crucial in Zero Trust environments that support both legally readable and
technologically  sound  decision  logs.  AI-ZT  systems  in  the future  will require  providing human-interpretable  reasons  behind
every execution action to meet the global requirements of data protection.

8.4.3. Ethical Design Principles for AI-ZT Systems

It will be necessary to incorporate into the algorithms of AI-ZT fairness, bias mitigation, and inclusiveness. Without a lot
of caution, AI agents can carry with them discriminative effects, particularly those machines that judge users according to their
behavioural character or accessibility records. Security vendors can probably expect to incorporate such frameworks as IEEE
P7003  (Algorithmic  Bias  Considerations)  and  the  NIST  AI  Risk  Management  Framework  into  the  design  of  AI-ZTs  in  the
future.

9. Conclusion

The  Zero  Trust  development  of  security  models,  a  shift  in  the  concept  of  static  perimeter  protections  to  dynamic
technological architectures, is the point of inflection in the cybersecurity strategy. With increased uptake and usage of clouds,
mobile workforces and IoT, the zero trust concept of never trust, always verify is no longer a choice but a requirement of the
original zero trust tenet, zero trust. This review has discussed how Early artificial intelligence integrations, in specific, started
creating transformations to disrupt traditional Zero Trust by making the systems more intelligent and more capable of dynamic
decision-making situations. Through the use of machine learning, federated learning and intelligent policy orchestration, early
AI-ZT  systems  also  provided  capabilities  such  as  behaviour-based  authentication,  dynamic  access  control  and  anomaly
detection  at  a  non-human  scale.  Such  developments  made  the  foundation  of  autonomous  trust  engines  and  real-time
enforcement mechanisms, which outsmarted static rule sets.

62

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

However, there were also fresh vulnerabilities and architectural challenges that were presented by such innovations. The
danger of overfitting the models, policy drift and opaque decision-making showed that the absence of accountability in the face
of  intelligence  might  corrode  trust  among  the  interested  parties  or  stakeholders.  Explainability,  auditability,  and  regulatory
compliance were open issues in most of the deployments, especially when AI-generated decisions were to deny access or raise
suspicion. In addition, there were also threats due to training data integrity, adversarial inputs, and model drift in distributed AI
systems  to  trust  computation in  sensitive  contexts. The  concept  of  optimisation and model  pruning, in addition  to  retraining
with  federated  learning,  became  significant  due  to  real-time  execution  in  cases  with  extremely  constrained  resources,
especially on an edge device.

But these inadequacies led to the future design plans. Earlier efforts of AI-ZT installations led to the development of more
durable and explainable models that have AI controls, human in-the-room management functions, and explanatory features of
AI models. The congruency of AI-ZT and DevSecOps also helped the security teams to apply the concepts of adaptive trust to
the CI/CD pipeline so that policy enforcement could adapt to changes in the development lifecycle. Moving forward, zero trust
is converging with autonomous agents and large language models in addition to quantum-resilient cryptographic standards as
the  next-gen  digital  trust.  The  questions  about  cross-border  enforcement,  ethical  AI  limits,  and  international  security  norms
require  the  cooperation  of  many  stakeholders  so  that  the power  of  AI  could  also  be  useful  in  good  ways.  A  fully  intelligent
Zero Trust model is an evolutionary journey, back and forth and mutually integrated. Finally, automation of decisions, which
aims to be the ultimate goal of hybridisation between Zero Trust and AI, should not be seen as some sort of improvement or
yet another way to make decisions, but rather as a way to make these decisions transparent, equitable, secure, and flexible. The
comparative  equilibrium  between  autonomy  and  control  that  does  not  compromise  the  trustworthiness  of  trust  should  be
further perfected in the future research that will be conducted despite the emerging threats/

References
[1]  Gilman, E., & Barth, D. (2017). Zero Trust Networks: Building Secure Systems in Untrusted Networks. Foundational work
on the architecture and core principles of Zero Trust, including continuous verification and dynamic policy enforcement,
drawing from NIST SP 800-207

[2]  Forrester Research (2010). Introduction of Zero Trust concept and category by John Kindervag. This marked the formal

framing of Zero Trust Architecture (ZTA) as a strategic cybersecurity model

[3]  Google  (2014). BeyondCorp  initiative. Early,  real-world  enterprise  application  of  Zero  Trust  principles allowing remote

work without VPNs, demonstrating early implementation of Zero Trust architecture

[4]  NIST  (2018).  NIST  SP  800-207:  Zero  Trust  Architecture.  Provided  the  formal  architectural  framework  and  guidelines

widely adopted in both government and private sectors

[5]  M.  R.  Islam,  M.  H.  Rehmani,  &  F.  C.  Delicato  (2021).  Zero  Trust  Security  Model  for  Cloud  Computing.  IEEE

Transactions on Cloud Computing, 9(4), 1024–1036.

[6]  S. Dixit, “The impact of quantum supremacy on cryptography: Implications for secure financial transactions,” Int. J. Sci.

Res. Comput. Sci. Eng. Inf. Technol., vol. 6, no. 4, pp. 611–637, 2020. doi: 10.32628/CSEIT2064141

[7]  S.  Ghasemshirazi,  G.  Shirvani,  and  M.  A.  Alipour,  “Zero  trust:  Applications,  challenges,  and  opportunities,”  arXiv

preprint, arXiv:2309.03582, 2023.

[8]  R.  Kumar,  A.  K.  Gupta,  &  V.  Gupta  (2021).  Zero  Trust  Architecture  and  Security:  A  Survey.  IEEE  Access,  9,  13572–

13590.

[9]  J. Chen & L. Zeng (2021). Machine  Learning-Based Anomaly  Detection for  Cloud  Security in  Financial  Systems. IEEE
Transactions  on  Neural  Networks  and  Learning  Systems,  32(9),  4001–4013.  J.  Chen  &  L.  Zeng  (2021).  Machine
Learning-Based Anomaly Detection for Cloud Security in Financial Systems. IEEE Transactions on Neural Networks and
Learning Systems, 32(9), 4001–4013.

[10] W.  Yeoh  et al.,  “Zero  trust  cybersecurity:  Critical  success  factors and  a maturity  assessment  framework,”  Computers &

Security, vol. 133, 103412, 2023.

[11] J. Kindervag, “Build security into your network’s DNA: The zero trust network architecture,” Forrester Research Inc., vol.

27, pp. 1–16, 2010.

[12] C. C. Ike et al., “Redefining zero trust architecture in cloud networks: A conceptual shift towards granular, dynamic access

control and policy enforcement,” Magna Scientia Adv. Res. Rev., vol. 2, no. 1, pp. 074–086, 2021.

[13] D. Singh, P. R. Kumar, & R. D. Shukla (2021). AI-Driven Identity and Access Management in Zero Trust. IEEE Security

& Privacy, 19(3), 63–70.

[14] T.  F.  Hennessy  &  S.  A.  Khan  (2021).  Machine  Learning  for  Threat  Detection  in  Zero  Trust  Cloud  Security.  IEEE

Transactions on Dependable and Secure Computing, 18(3), 1293–1305.

[15] M.  V.  Chandran,  P.  P.  Agarwal,  &  A.  S.  Patel  (2021).  Machine  Learning for  Predictive  Threat  Detection  in  Zero  Trust

Cloud Networks. IEEE Transactions on Artificial Intelligence, 10(3), 578–590.

[16] J. M. Smith, A. H. Williams, & L. T. Chen (2022). AI-Augmented Policy Decision Points in Zero Trust Networks. IEEE

Journal on Selected Areas in Communications, 40(1), 112–125.

[17] R.  Patel  &  S.  Kapoor  (2022).  Adaptive  Machine  Learning-Driven  Access  Control  for  Zero  Trust  Architectures.

International Journal of Information Security, 21(4), 457–472.

63

Anitha Mareedu / IJERET, 4(4), 53-64, 2023

[18] K.  Y.  Lee,  M.  S.  Tan,  &  Q.  Li  (2022).  Leveraging  Behavioral  Analytics  for  Insider  Threat  Detection  in  Zero  Trust

Environments. Computers & Security, 114, 102573.

[19] H. García-García, E. García-Cruz, & M. T. Álvarez (2021). A Hybrid Zero Trust Model Based on AI-Driven Risk Scoring

and Rule Enforcement. Future Generation Computer Systems, 117, 332–345.

[20] J. Jangid, “Efficient training data caching for deep learning in edge computing networks,” Int. J. Sci. Res. Comput. Sci.

Eng. Inf. Technol., vol. 7, no. 5, pp. 337–362, 2020. doi: 10.32628/CSEIT20631113

[21] S. Kumar, A. B. Rao, & N. Patel (2021). Explainable AI for Zero Trust: Transparent Decision-Making in Access Control.

ACM Computing Surveys, 54(7), 147.

[22] F. Al-Doghman et al., “AI-enabled secure microservices in edge computing: Opportunities and challenges,” IEEE Trans.

Serv. Comput., vol. 16, no. 2, pp. 1485–1504, 2022.

[23] L.  Zhang  &  P.  Sharma  (2021).  Federated  Learning  for  Decentralized  Zero  Trust  Access  Control  Across  Cloud-Edge

Environments. IEEE Internet of Things Journal, 8(14), 11023–11034.

[24] A. Z. Bashir, M. A. Khan, & F. I. Al-Turjman (2020). Reinforcement Learning in Zero Trust Network Orchestration for

Adaptive Security Posture. Expert Systems with Applications, 150, 113223.

[25] Y. Cao, X. Liu, & Z. W. Xu (2020). Deep Learning-Enabled Lateral Movement Detection within Zero Trust Frameworks.

Journal of Network and Computer Applications, 150, 102511.

[26] J.  Kwon,  H.-J.  Kim,  &  S.-Y.  Ko  (2022).  Predictive  Analytics  in  Zero  Trust:  Forecasting  Access  Threats  Using  Time-

Series Machine Learning. Computers & Security, 113, 102532.

[27] E. Lopez, R. Wang, & P. Hernandez (2022). Context-Aware AI for Dynamic Access Control in Zero Trust Environments.

ACM Transactions on Cyber-Physical Systems, 6(4), 37.

[28] D. Roberts & M. Patel (2021). Integrating Expert Systems with ML Models for Zero Trust Decision Engines. Journal of

Systems Architecture, 115, 102162.

[29] S.  Dixit,  “AI-powered  risk modeling  in  quantum  finance: Redefining  enterprise  decision  systems,”  Int.  J.  Sci.  Res.  Sci.

Eng. Technol., vol. 9, no. 4, pp. 547–572, 2022. doi: 10.32628/IJSRSET221656

[30] K. Li, Y. Zhou, & X. Xu (2020). Graph Neural Networks for Trust Assessment in Zero Trust Architectures. IEEE Access,

8, 212345–212356.

64

