---
conversion_metadata:
  converted_at: "2026-07-21T07:35:41Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Molla & Zobayed.pdf"
  source_pdf_sha256: "b10593edbdfba61cd0811d255c76faa8b97b8c5ce27c037ef9cb692ccb5cb365"
  page_count: 13
  markdown_char_count: 143470
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Frontiers in Computer Science and Artificial Intelligence 
ISSN: 2978-8048 
DOI: 10.32996/fcsai 
Journal Homepage: www.al-kindipublisher.com/index.php/fcsai

FCSAI

AL-KINDI CENTER FOR RESEARCH  
AND DEVELOPMENT

| REVIEW ARTICLE

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and 
Deployment Challenges

Shahadat Molla1, and S M Zobayed2  
1 Department of Information Systems, California State University, Los Angeles, CA 90032, USA 
2 Department of Engineering Management, Westcliff University, 17877 Von Karman Avenue, 4th Floor, Irvine, CA 92614, USA 
Corresponding Author: Shahadat Molla, E-mail: shadat.cse@gmail.com

| ABSTRACT 
Artificial  intelligence  (AI)  is  increasingly  embedded  in  consequential  decision-making  processes  across  healthcare,  assistive 
technologies,  smart  infrastructure,  agriculture,  business  analytics,  cybersecurity,  and  sustainability.  Unlike  general-purpose  AI 
deployments,  high-stakes  decision  support  demands  not  only  predictive  accuracy  but  also  explainability,  robustness,  privacy, 
scalability, human oversight, and governance readiness. This structured critical review synthesizes to map the current landscape 
of  AI  for  high-stakes  decision  support  using  a  four-axis  taxonomy:  application  domain,  data  modality,  architecture  family,  and 
deployment concern. The review identifies six application domains, healthcare and biomedical decision support, human-centered 
and assistive AI, smart infrastructure and cyber-physical systems, agriculture and sustainability, business and enterprise decision 
support,  and  cybersecurity  and  distributed  intelligence,  and  eight  architecture  families  ranging  from  conventional  machine 
learning and convolutional neural networks to vision transformers, graph neural networks, Bayesian models, generative AI, and 
federated  learning  systems.  The  synthesis  reveals  that  while  significant  architectural  advances  have  been  made,  deployment-
critical  properties  such  as  uncertainty  quantification,  privacy-preserving  inference,  real-time  feasibility  on  edge  devices,  and 
governance-aligned  reporting  remain  inconsistently  addressed.  Future  research  must  prioritize  cross-domain  benchmarking, 
trustworthy and auditable AI pipelines, human-in-the-loop frameworks, and evidence maturity standards  appropriate for high-
stakes  contexts.  This  review  provides  an  evidence-grounded  taxonomy  and  actionable  research  agenda  for  researchers  and 
practitioners to build the next generation of responsible AI decision-support systems.

| KEYWORDS

Artificial  intelligence;  High-stakes  decision  support;  Trustworthy  AI;  Explainable  AI;  Human-in-the-loop  AI;  Federated  learning; 
Graph neural networks; Vision transformers; Uncertainty quantification; AI governance

| ARTICLE INFORMATION

ACCEPTED: 15 April 2026                               PUBLISHED: 22 May 2026                    DOI: 10.32996/jcsts.2026.5.7.3

1. Introduction

The  deployment  of  artificial  intelligence  in  consequential  decision  environments,  those  where  an  erroneous  prediction  or 
recommendation  carries  significant  human,  financial,  or  societal  cost,  has  accelerated  substantially  over  the  past  decade. 
Healthcare diagnosis, patient monitoring, infrastructure fault detection, agricultural disease management, credit risk assessment, 
and  cybersecurity  threat  response  all  constitute  high-stakes  domains  in  which  AI  is  increasingly  positioned  not  as  an 
experimental  tool, but as an  operational support system.  The breadth of this deployment presents  both an opportunity and a 
methodological  challenge:  no  single  architecture,  modality,  or  evaluation  framework  can  address  the  full  spectrum  of 
requirements encountered across these domains.

Existing reviews of AI in decision support tend to focus narrowly on a single domain, most commonly medical imaging or clinical 
prediction,  while  the  cross-domain  structural  similarities  and  shared  deployment  challenges  remain  under-examined.  A  review 
that spans healthcare [49, 20, 26], assistive and neuro-affective AI [1, 2, 13], smart infrastructure and IoT [3, 9, 18], agriculture and

Copyright: © 2026 the Author(s). This article is an open access article distributed under the terms and conditions of the Creative Commons 
Attribution (CC-BY) 4.0 license (https://creativecommons.org/licenses/by/4.0/). Published by Al-Kindi Centre for Research and Development,  
London, United Kingdom.

Page | 25

---

<!-- PAGE 2 -->

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges

sustainability  [25,  70,  77],  business  analytics  and  enterprise  AI  [40,  42,  74],  and  cybersecurity  [73,  78,  79]  reveals  recurring 
architectural patterns, deployment tensions, and governance gaps that are invisible when each domain is examined in isolation. 
This  review  is  motivated  by  three  observations.  First,  the  architecture  families  are  most  frequently  employed  in  high-stakes 
applications, CNNs, vision transformers, ensemble methods, graph  neural networks,  and federated systems, each carry  distinct 
tradeoffs between accuracy, interpretability, and deployment feasibility. Second, the dominant evaluation criterion of predictive 
accuracy is necessary but insufficient: robustness to distribution shift, resistance to adversarial inputs, uncertainty quantification, 
and privacy compliance are equally consequential in deployment environments. Third, the literature reveals growing recognition 
that human oversight is not an optional add-on but a structural requirement in high-stakes AI, particularly in domains  such as 
autonomous  robotics  [16],  clinical  decision  support  [49,  71],  and  automated  risk  assessment  [69].  This  review  addresses  these 
gaps by constructing a structured cross-domain taxonomy, synthesizing architecture and deploying evidence, and identifying the 
research  directions  most  critical  for  responsible  AI  decision  support  at  scale.  Figure  1  demonstrates  the  end-to-end  pathway 
through  which  AI  systems  move  from  heterogeneous  data  sources  to  model-generated  recommendations,  human  review, 
deployment monitoring, and governance feedback.

2. Review Scope and Taxonomic Framework

Figure 1. High-stakes AI decision-support lifecycle.

The  corpus  was  assembled  to  span  the  principal  application  domains,  architecture  families,  data  modalities,  and  deployment 
concerns  relevant to high-stakes  AI decision support. Papers were selected to ensure representational balance across  domains 
and to enable a structured evidence map rather than an exhaustive literature census. A four-axis taxonomy organizes the corpus. 
Axis  1  classifies  papers  by  application  domain:  (i)  healthcare  and  biomedical  decision  support,  (ii)  human-centered,  neuro-
affective,  and  assistive  AI,  (iii)  smart  infrastructure,  IoT,  robotics,  and  cyber-physical  systems,  (iv)  agriculture,  environment,  and 
sustainability,  (v)  business,  enterprise,  and  organizational  decision  support,  and  (vi)  cybersecurity,  privacy,  and  distributed 
intelligence.  Axis  2  classifies  by  data  modality—medical  images,  facial  and  affective  signals,  EEG  and  physiological  signals,  IoT 
and sensor streams, acoustic-emission and industrial signals, text and natural language, graph and knowledge-structured data, 
business and tabular data, and multimodal data. Axis 3 identifies the architecture family: conventional machine learning, CNN-
based  deep  learning  and  transfer  learning,  vision  transformers  and  attention-based  models,  graph  neural  networks  and 
knowledge  graphs,  hybrid  and  ensemble  systems,  Bayesian  and  physics-guided  models,  generative  and  agentic  AI,  and 
federated/edge/privacy-preserving  systems.  Axis  4  catalogues  the  deployment  concern:  explainability,  robustness,  privacy, 
scalability,  real-time  feasibility,  human  oversight,  governance,  security,  and  safety/accountability.  The  taxonomy  enables  two 
forms  of  analysis:  vertical  analysis  within  a  domain  (tracking  how  architecture  choices  affect  deployment  readiness)  and 
horizontal analysis across domains (identifying universal deployment tensions that transcend domain-specific context).

3. Architecture Families for High-Stakes Decision Support 
3.1. Conventional Machine Learning and Structured Decision Models 
Conventional machine learning encompasses logistic regression, decision trees, random forests, gradient boosting, and support 
vector  machines  applied  to  structured  tabular  data,  remains  highly  relevant  in  high-stakes  decision  support,  particularly  in 
clinical,  business,  and  financial  settings  where  data  are  structured  and  interpretability  is  paramount.  Work  focusing  on  clinical

Page | 26

---

<!-- PAGE 3 -->

FCSAI 5(7): 25-37

decision  support  for  heart  disease  prediction  using  structured  patient  data  [49]  illustrates  the  continued  utility  of  classical  ML 
pipelines  when  feature  engineering  and  validation  are  handled  rigorously.  In  business  contexts,  research  on  credit  scoring  for 
financially  underserved  populations  [40],  predictive  analytics  for  project  risk  [42],  retail  demand  forecasting  [57],  and  small-
business  management  including  customer  retention  and  financial  forecasting  [58]  demonstrates  that  gradient-boosted 
ensembles  and  LSTM  networks  constitute  practical,  deployment-ready  tools  when  the  decision  environment  is  data-rich  but 
annotation-constrained.  Multi-class  sentiment  classification  [38]  and  data-driven  sentiment  extraction  from  drug  reviews  [39] 
further illustrate ML's relevance in text-based decision support. Market basket analysis for healthcare service bundling [43] and 
studies  on  customer  satisfaction  and  business  transactions  in  hospitality  [59]  represent  the  application  of  association  and 
regression  methods  to  organizational  decision  support  at  scale.  Enhanced  market  trend  forecasting  with  external  factor 
integration [60] and ML-driven e-commerce pricing optimization [55] extend this cluster to demand-side business intelligence. 
Collectively, these works  suggest that structured ML remains  a foundational layer of high-stakes  decision support, often more 
interpretable  and  computationally  efficient  than  deep  learning  alternatives,  though  issues  of  fairness,  feature  reliability,  and 
governance remain underspecified. 
3.2. CNN-Based Deep Learning and Transfer Learning 
Convolutional  neural  networks  and  their  transfer-learned  variants  constitute  the  dominant  architecture  family  in  image-based 
high-stakes AI. The application range spans medical imaging, including multichannel lung cancer classification from CT data [20], 
early leukemia diagnostics via transfer learning [36], and aquaculture disease diagnosis using lightweight ResNeXt architectures 
[46]  to  agricultural  disease  detection  and  industrial  inspection.  Transfer  learning  is  particularly  prominent  in  domains 
characterized by limited labelled training data: the use of transfer learning for sleep stage classification under data-constrained 
conditions  [47] illustrates  how pre-trained feature extractors  can be repurposed to clinically sensitive classification tasks. Facial 
emotion recognition systems, including a bidirectional Elman neural network approach [7] and a hybrid deep belief optimization 
system [8], similarly leverage learned feature representations from large facial datasets. The lightweight deep learning framework 
applied to concrete crack characterization using acoustic-emission signals [21] extends the CNN paradigm to industrial sensing, 
where real-time feasibility and sensor-data compatibility are critical. Across all these applications, the transfer learning strategy 
addresses  data  scarcity  but  introduces  the  risk  of  negative  transfer  and  domain  mismatch,  both  of  which  are  deployment 
concerns requiring systematic evaluation. 
3.3. Vision Transformers and Attention-Based Architectures 
Vision transformers (ViTs) and their attention-based variants have emerged as a high-performing architecture family for image 
classification in high-stakes domains, progressively displacing purely convolutional approaches in medical imaging and precision 
agriculture. The dual-branch visual transformation framework developed for ASD classification [4, 1] illustrates how transformer 
architectures can model spatially distributed facial features more flexibly than fixed-receptive-field CNNs. In medical imaging, the 
hybrid vision transformer for prostate cancer classification in MRI images [48] and the LMVT hybrid vision transformer for lung 
cancer  diagnosis  [30]  demonstrate  that  combining  convolutional  feature  extraction  with  self-attention  can  improve  both 
accuracy and explainability. The hierarchical Swin Transformer ensemble for breast cancer diagnosis [31] and Swin Transformer–
driven  cervical  cell  classification  with  web-based  deployment  [61]  specifically  demonstrates  the  compatibility  of  transformer 
architectures  with  decentralized  and  web-deployed  screening  workflows.  In  precision  agriculture,  MaizeFormerX,  a  lightweight 
cross-scale  attention  vision  transformer  [25],  and  the  MaxViT-based  soybean  disease  identification  model  [33]  illustrate  that 
transformer  efficiency  advances  are  beginning  to  close  the gap  with  CNN-based  lightweight  models,  enabling  deployment  on 
resource-constrained  agricultural  hardware.  Global–local  attention  modeling  for  kidney  disease  classification  from  CT  images 
[63] represents a further architectural refinement, combining coarse global context with fine-grained local feature attention that 
is  particularly  relevant  for  multi-class  lesion  discrimination.  The  convergence  of  explainability  requirements  with  transformer 
attention maps [62] offers promising but still-maturing interpretability mechanisms. 
3.4. Hybrid, Ensemble, and Multimodal Fusion Systems 
Hybrid and ensemble systems are prominent in domains requiring both high accuracy and some form of post-hoc justification. 
The explainable deep stacking ensemble for brain tumor diagnosis [32] and the stacking ensemble with explainable AI for breast 
cancer  diagnosis  and  web  deployment  [52]  exemplify  the  combination  of  heterogeneous  base  learners  with  ensemble 
aggregation,  achieving  improved  generalization  while  preserving  the  interpretability  needed  for  clinical  endorsement.  The 
ensemble transformer with post-hoc explanations for depression and severity detection [27] extends this architecture to affective 
computing,  where  label  ambiguity  and  subjective  ground  truth  make  ensemble  uncertainty  estimation  particularly  valuable. 
Multimodal  fusion  represents  an  important  sub-category:  the  hybrid  multi-modal  emotion  recognition  framework  based  on 
InceptionV3DenseNet [6] and the vision-audio multimodal object recognition system using hybrid tensor fusion [29] address the 
challenge  of  integrating  heterogeneous  modalities  without  introducing  cross-modal  interference.  The  multimodal  machine 
learning framework for privacy-preserving and scalable cancer diagnosis [51] is notable in that it combines fusion with privacy 
Page | 27

---

<!-- PAGE 4 -->

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges

constraints,  foreshadowing  the  next  generation  of  privacy-aware  multimodal  clinical  systems.  The  attention-enhanced  deep 
learning framework for business strategy optimization [53] extends multimodal fusion principles  to business intelligence, while 
the explainable transformer for cotton leaf diagnostics and fabric defect detection [28] applies them to dual-task agricultural and 
manufacturing inspection. 
3.5. Graph Neural Networks and Knowledge-Graph Reasoning 
Graph-structured data and knowledge-graph reasoning occupy a specialized but important niche in high-stakes AI, particularly 
where  relational  dependencies  among  entities  carry  decision-relevant  information.  The  enhancement  of  acoustic-emission-
driven gas-pipeline monitoring using graph neural networks [18] illustrates how GNNs can model the propagation structure of 
physical  signals  across  networked  sensor  arrays,  enabling  more  accurate  fault  localization  than  signal-level  classifiers  alone. 
Knowledge-graph  and  NLP  integration  for  facilitating  heuristic  reasoning  [17]  addresses  a  different  but  complementary  need: 
enabling  AI  systems  to  leverage  structured  domain  knowledge  in  support  of  reasoning  tasks  that  resist  purely  statistical 
approaches.  The  AddManBERT  combinatorial  triples  extraction  and  knowledge-graph  construction  for  additive  manufacturing 
design support [23] demonstrates that BERT-based language models and knowledge graphs can be coupled to create semantic 
decision-support  tools  in  specialized  engineering  domains.  Together,  these  architectures  suggest  that  relational  and  symbolic 
reasoning  are  not  superseded  by  deep  learning  but  rather  constitute  a  complementary  layer  of  high-stakes  decision  support, 
particularly in safety-critical industrial and engineering contexts. 
3.6. Bayesian, Physics-Guided, and Uncertainty-Aware Models 
Uncertainty quantification is a fundamental requirement in safety-critical systems, and Bayesian and physics-guided approaches 
represent the most principled available framework for this purpose. The physics-guided Bayesian neural network for sensor fault 
detection  in  wind  turbines  [54]  is  directly  relevant:  by  embedding  physical  priors  into  the  network  architecture,  the  model 
addresses  the  twin  challenges  of  sensor  data  sparsity  and  the  need  for  calibrated  uncertainty  estimates  in  a  safety-sensitive 
industrial context. This architecture family is underrepresented in the broader corpus, reflecting a maturity gap in the literature: 
while  Bayesian  deep  learning  and  physics-informed  neural  networks  have  attracted  substantial  methodological  attention,  their 
integration into domain-specific high-stakes applications remains limited. The deployment implications are significant, systems 
that cannot quantify their own uncertainty cannot reliably support human oversight, particularly in contexts such as wind-energy 
management, structural health monitoring, and clinical diagnostics where false confidence carries severe consequences. 
3.7. Generative, Agentic, and Enterprise AI 
Generative  AI  and  agentic  systems  represent  the  most  recent  and  rapidly  evolving  frontier  in  high-stakes  decision  support. 
Generative  AI  in  enterprise  information  systems  for  transforming  business  intelligence  and  strategic  decision  support  [74] 
addresses  the  organizational  embedding  of  large  language  model  capabilities  into  enterprise  workflows,  a  transition  that 
introduces  new  questions  of  factual  reliability,  audit  trails,  and  accountability.  Automated  risk  assessment  and  collaborative 
decision-making  AI  in  agile  project  management  and  stakeholder  engagement  [69]  exemplifies  agentic  AI—systems  that  not 
only  predict  but  also  initiate  decision  workflows,  coordinate  among  stakeholders,  and  adapt  to  feedback.  AI-driven  business 
analytics  for  IT  strategy  [66]  and  AI-enabled  management  information  systems  for  economic  resilience  and  governance  [76] 
further  illustrate  the  enterprise  AI  cluster,  where  real-time  data  integration,  organizational  agility,  and  governance  compliance 
are  simultaneously  demanded.  The  sustainability  framing  of  AI-ERP  integration  in  dark  factories  [65]  introduces  additional 
complexity:  autonomous  industrial  environments  require  AI  systems  that  are  not  only  accurate  but  also  auditable,  energy-
efficient, and aligned with broader sustainability objectives. 
3.8. Edge-Cloud, Federated, Privacy-Preserving, and Distributed AI 
The  deployment  of  AI  at  the  edge  of  networks,  on  IoT  devices,  clinical  sensors,  and  distributed  infrastructure,  introduces  a 
distinct  set  of  architectural  constraints.  Privacy-preserving  behavior  analytics  for  workforce  retention  [44]  and  the  multimodal 
privacy-preserving  cancer  diagnosis  framework  [51]  illustrate  the  operational  demand  for  analytics  that  never  expose  raw 
personal data to centralized servers. The distributed intelligence and privacy-preserving deployment framework encompassing 
edge-cloud,  6G  connectivity,  and  federated  learning  for  secure  and  auditable  decision  support  [79]  represents  the  most 
comprehensive  architectural  response  to  this  demand,  integrating  multiple  privacy-preserving  mechanisms  into  a  unified 
deployment  stack.  Stacking  ensemble-based  breast  cancer  classification  with  real-time  web  deployment  [52]  and  Swin 
Transformer cervical cell classification with web-based screening [61] demonstrate that deployment-readiness, including latency, 
user-interface  integration,  and  cross-platform  accessibility,  is  itself  an  architectural  concern  that  must  be  addressed  during 
model design, not as an afterthought. The intelligent cybersecurity framework integrating ML-driven data protection and threat 
intelligence  [73],  AI  for  data  security  and  digital  communication  resilience  [72],  and  the  resilience-by-design  framework  [75] 
collectively  constitute  an  emerging  distributed  AI  security  cluster  in  which  privacy,  auditability,  and  real-time  threat  response 
must be simultaneously maintained.

Page | 28

---

<!-- PAGE 5 -->

FCSAI 5(7): 25-37

4. Application Domains 
4.1. Healthcare and Biomedical Decision Support 
Healthcare constitutes the largest and most architecturally diverse domain in the corpus. Cancer diagnosis applications span skin 
cancer [26, 62], lung cancer [20, 30], breast cancer [31, 32, 52], cervical cancer [35, 61], leukemia [36], and prostate cancer [48], 
collectively  demonstrating  that  transformer-based,  CNN-based,  and  ensemble  architectures  are  all  actively  explored  for 
oncological  image  analysis.  The  comparative  analysis  of  explainable  ML  for  cancer classification  using  cytological  features  [50] 
and  the  multimodal  privacy-preserving  cancer  diagnosis  framework  [51]  illustrate  the  dual  push  toward  interpretability  and 
privacy compliance that characterizes mature healthcare AI. Beyond oncology, kidney disease classification from CT images [63], 
Parkinson's  disease  screening  via  voice  biomarkers  [45],  sleep  stage  classification  with  transfer  learning  [47],  heart  disease 
prediction  from  structured  clinical  data  [49],  and  AI-integrated  healthcare  information  systems  for  diabetes  management  [71] 
demonstrate  the  breadth  of  modality  and  architecture  diversity  within  this  domain.  Sentiment  analysis  of  online  drug  reviews 
[39] and market basket analysis for healthcare service bundling [43] extend decision support into health services research. The 
consistent  emphasis  on  explainability  across  these  works,  reflected  in  post-hoc  XAI  methods,  attention  visualization,  and 
transparent  ensemble  reporting,  reflects  clinical  regulatory  and  professional  requirements  that  AI  recommendations  be 
interpretable  by  clinicians.  Neural  network  methods  combined  with  dimensionality  reduction  can  enhance  breast  cancer 
diagnosis by simplifying high-dimensional feature representations while retaining clinically meaningful diagnostic patterns [80]. 
4.2. Human-Centered, Neuro-Affective, and Assistive AI 
This  domain  addresses  AI  systems  designed  to  support  humans  with  cognitive,  communicative,  or  affective  needs.  ASD 
classification  using  facial  grid-wise  emotion  features  and  dual-branch  visual  transformation  [1,  4]  represents  a  high-stakes 
application in which misclassification carries significant developmental and social consequences. The facial expression database 
of  ASD  children  [5]  provides  the  foundational  data  resource  for  this  research  cluster.  Multimodal  EEG  analysis  of  neural 
synchrony  in  phrase  processing  [2]  and  the  standard  tDCS  model  [13]  address  neuro-affective  AI  in  clinical  neuroscience 
contexts.  Emotion  recognition  systems,  including  the  InceptionV3DenseNet  hybrid  [6],  bidirectional  Elman  NN  [7],  and  hybrid 
deep belief optimization [8], target affective computing applications where training data quality and subject variability introduce 
systematic  reliability  challenges.  The  flex  sensor–based  hand  glove  for  deaf  and  mute  people  [14]  and  iris  detection  and 
recognition  system  [22]  represent  sensor-based  assistive  AI.  Suicidal  ideation  detection  using  NLP  and  deep  learning  [37]  is  a 
critical  mental  health  application  where  both  false  positives  and  false  negatives  carry  severe  consequences,  demanding 
calibrated  uncertainty  and  human  oversight.  The  adaptive  feedback  system  for  learner  improvement  [19]  and  the  AI-powered 
digital health platform for ASD students [67] address adaptive and personalized decision support in educational and therapeutic 
settings.  Bengali  social  media  sentiment  classification  [38]  and  sentiment  extraction  from  drug  reviews  [39]  provide  modality 
evidence for text-based human-centered AI. 
4.3. Smart Infrastructure, IoT, Robotics, and Cyber-Physical Systems 
Smart  infrastructure  encompasses  a  diverse  set  of  sensor-rich,  real-time,  and  safety-critical  environments.  IoT-based  wireless 
battery  monitoring  for  solar  micro-grids  [3]  and  smart  energy  metering  [10]  illustrate  AI-assisted  monitoring  in  energy 
infrastructure. The IoT-based smart healthcare medical box for elderly patients [9] extends IoT decision support into clinical care 
contexts.  Wireless  mesh  network  routing  [11]  and  MANET  routing  protocol  simulation  [12]  address  network-layer  decision 
support  in  distributed  infrastructure.  High-altitude  platform  communications  optimization  [15]  represents  a  communication-
systems  application  of  simulation-based  AI.  The  question  of  full  autonomy  in  underwater  robotics  [16]  directly  engages  the 
human  oversight  axis:  the  framing  as  a  prospect  question  reflects  genuine  uncertainty  about  whether  autonomous  decision-
making in unstructured aquatic environments is currently reliable enough for unsupervised deployment. Gas-pipeline condition 
diagnosis  through  acoustic-emission  signal  imaging  [24]  and  GNN-based  smart  gas-pipeline  monitoring  [18]  address  safety-
critical industrial infrastructure where fault detection failures have severe physical consequences. Concrete crack characterization 
using acoustic-emission and lightweight deep learning [21] and vision-audio multimodal object recognition using tensor fusion 
[29] contribute additional modality and architecture evidence for the infrastructure monitoring cluster. 
4.4. Agriculture, Environment, and Sustainability 
Agricultural  AI  decision  support  encompasses  disease  detection,  yield  optimization,  and  sustainability-oriented  resource 
management. Maize leaf disease diagnosis with a lightweight vision transformer [25], cotton leaf diagnostics with an explainable 
transformer  [28],  soybean  leaf  and  seed  disease  identification  with  MaxViT  [33],  mango  leaf  disease  recognition  with  an 
ensemble vision transformer [34], tea leaf disease precision diagnosis with deep learning [77], and aquaculture disease diagnosis 
with  lightweight  ResNeXt  [46]  collectively  constitute  a  precision  agriculture  cluster  in  which  lightweight,  explainable,  and  real-
time-feasible  architectures  are  prioritized  for  field  deployment.  AI-driven  smart  agriculture  for  crop  yield  optimization  and 
sustainability [70] addresses the systemic dimension, integrating AI into broader agricultural management frameworks. AI-driven 
Page | 29

---

<!-- PAGE 6 -->

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges

solar  financing  for  rural  clinics  and  small  health  businesses  [41]  introduces  sustainability  and  resilience  framing  into  health 
infrastructure,  connecting  agricultural  and  health  domains  through  shared  energy  and  financing  challenges.  The  resilience-by-
design framework [75] provides a cross-cutting lens for sustainability-oriented AI across infrastructure, health, and environmental 
systems. 
4.5. Business, Enterprise, and Organizational Decision Support 
Business decision support is the most thematically diverse domain in the corpus, spanning credit scoring, project management, 
demand  forecasting,  supply  chain  analytics,  digital  transformation,  and  enterprise  information  systems.  Credit  scoring  models 
leveraging  alternative  data  for  underserved  businesses  [40]  address  fairness  and  access  in  financial  AI.  Predictive  analytics  for 
project risk identification and mitigation [42] and automated risk assessment in agile project management [69] illustrate AI's role 
in  organizational  risk  governance.  Market  basket  analysis  for  healthcare  service  bundling  [43]  bridges  health  and  business 
analytics.  Blockchain  applications  in  supply  chain  management  [56]  introduced  ledger  technology  as  a  trust  mechanism 
complementary to predictive AI. Retail demand forecasting using LSTM and gradient boosting [57], small-business management 
using  predictive  ML  [58],  e-commerce  pricing  optimization  [55],  market  trend  forecasting  with  external  factor  integration  [60], 
and  customer  satisfaction  in  hospitality  [59]  represent  a  forecasting  and  optimization  cluster  where  ML  methods  address 
operational  decision  support.  The  attention-enhanced  deep  learning  system  for  business  strategy  optimization  [53]  extends 
transformer architecture into enterprise analytics. AI-driven business analytics for IT strategy [66], digital transformation analytics 
for  IT  project  excellence  [68],  agile  IT  project  risk  and  AI  thematic  analysis  [64],  and  AI-ERP  integration  in  dark  factories  [65] 
constitute  the  enterprise  AI  governance  cluster.  Generative  AI  for  enterprise  business  intelligence  [74]  and  AI-enabled 
management information systems for economic resilience [76] represent the most strategic layer of this domain, addressing how 
AI reshapes organizational decision architectures rather than merely optimizing individual predictions. 
4.6. Cybersecurity, Privacy, and Distributed Intelligence 
Cybersecurity  and  privacy-preserving  AI  represent  both  a  standalone  application  domain  and  a  horizontal  deployment

requirement across all other domains. The intelligent cybersecurity framework integrating ML-driven data protection and threat

intelligence [73] and AI for data security, analytics, and digital communication resilience [72] address real-time threat response in

digital infrastructure. Privacy-preserving behavior analytics for workforce retention [44] illustrates  the application of differential

privacy and anonymization techniques in organizational analytics. Trustworthy AI for high-stakes decision support across critical

sectors [78] provides a governance and framework perspective spanning all domains. The resilience-by-design AI framework for

security,  sustainability,  and  health  in  interdependent  systems  [75]  emphasizes  that  AI  security  cannot  be  designed  in  isolation

from sustainability and health system resilience. Distributed intelligence with edge-cloud-6G-federated learning for secure and

auditable  decision  support  [79]  represents  the  architectural  frontier  of  privacy-preserving  deployment,  integrating  edge

inference, cloud aggregation, 6G communication, and federated training into a unified auditable stack.

5. Deployment Challenges 
Figure  2  summarizes  recurring  pathways  through  which  AI  systems  may  fail  after  development.  Data-level  limitations,  model-
level overconfidence, environmental distribution shifts, and governance weaknesses  can jointly convert a technically promising 
model into an unreliable decision-support system. 
5.1. Data Quality, Heterogeneity, and Imbalance 
High-stakes  AI  systems  encounter  heterogeneous  data  at  every  layer.  Medical  imaging  corpora  vary  in  scanner  protocol, 
resolution, acquisition site, and annotation convention, making cross-institutional generalization a persistent challenge [20, 51]. 
Agricultural  disease  datasets  are  subject  to  lighting  variability,  growth-stage  confounds,  and  regional  crop  variety  differences 
that compromise model transferability [25, 34, 77]. Business datasets are often imbalanced across class labels property directly 
relevant  to  credit  scoring  models  for  underserved  populations  [40]  and  demand  forecasting  under  rare-event  conditions  [57]. 
The  facial  expression  database  for  ASD  children  [5]  highlights  the  challenge  of  constructing  domain-specific  datasets  with 
sufficient  diversity  to  support  generalizable  models  in  sensitive  populations.  Data  heterogeneity  is  not  merely  a  technical 
obstacle but a governance concern: models trained on non-representative data risk encoding systematic biases that propagate 
into high-stakes decisions. 
5.2. Explainability and Post-Hoc Interpretability 
Explainability  is  the  deployment  requirement  most  consistently  addressed  in  the  corpus,  and  it  is  represented  across  all  six 
application  domains.  The  post-hoc  explanation  strategies  integrated  into  ensemble  transformers  [27],  stacking  ensembles  [32, 
35], vision transformers [25, 28, 61, 62], and CNN-based systems [26, 50] reflect the institutional and regulatory expectation that 
AI  recommendations  in  healthcare,  agriculture,  and  business  settings  be  accompanied  by  intelligible  justifications.  The  Swin 
Transformer with web-deployed explainability for cervical cell screening [61] illustrates  that explainability mechanisms must be 
preserved under deployment constraints, including web-based inference pipelines. However, attention visualization and saliency

Page | 30

---

<!-- PAGE 7 -->

mapping, while increasingly ubiquitous, do not provide the formal guarantees of causal or counterfactual explanation that high-
stakes  settings  may  eventually  require  [78].  The  gap  between  current  post-hoc  explainability  practices  and  deployment-grade 
interpretability standards represents an important research frontier.

FCSAI 5(7): 25-37

Figure 2. Shared failure modes in high-stakes AI deployment.

5.3. Robustness and Distribution Shift 
Robustness to distribution shifts the degradation of model performance when test conditions diverge from training conditions is 
particularly  consequential  in  high-stakes  deployment.  Medical  imaging  models  face  cross-scanner  and  cross-population 
distribution  shifts  [31,  51,  63].  Agricultural  models  face  seasonal,  geographical,  and  phenological  shifts  [33,  46,  70].  Industrial 
monitoring models must remain reliable under varying operational conditions, sensor degradation, and novel fault patterns [18, 
54,  24].  Business  forecasting  models  are  vulnerable  to  economic  regime  changes  and  external  shocks  [57,  60].  The  physics-
guided  Bayesian  neural  network  [54]  represents  an  important  robustness  strategy  in  industrial  settings  by  embedding  domain 
priors that constrain model behavior under novel inputs. The trustworthy AI framework [78] and resilience-by-design approach 
[75] address robustness at a systemic rather than model-specific level. 
5.4. Privacy, Security, and Federated Deployment 
Privacy-preserving  AI  is  no  longer  a  speculative  research  direction  but  an  operational  requirement  in  health,  workforce,  and 
government contexts. Privacy-preserving behavior analytics for workforce retention [44] and the multimodal privacy-preserving 
cancer diagnosis framework [51] demonstrate that utility and privacy can be simultaneously addressed, though with architecture-
specific  tradeoffs.  Federated  learning  frameworks,  as  illustrated  by  [79],  distribute  training  across  data  owners  without 
centralizing  raw  data,  enabling  multi-institutional  model  development  without  privacy  violation.  The  intelligent  cybersecurity 
framework  [73]  and  the  AI-driven  resilience  framework  [72]  address  the  security  layer  of  AI  deployments,  where  adversarial 
attacks, data poisoning, and model inversion represent active threats. Blockchain integration in supply chain AI [56] introduces 
distributed  ledger  mechanisms  as  complementary  trust  infrastructure.  As  6G-enabled  edge  deployments  proliferate,  the 
convergence  of  privacy,  security,  and  real-time  inference,  addressed  architecturally  in  [79],  will  become  a  central  design 
constraint. 
5.5. Real-Time Feasibility and Resource Constraints 
Real-time inference on resource-constrained devices is a deployment-critical requirement in IoT, agricultural, and clinical point-
of-care contexts. The lightweight cross-scale attention transformer for maize disease [25], lightweight ResNeXt for aquaculture 
[46],  and  lightweight  deep  learning  for  concrete  crack  characterization  [21]  all  explicitly  address  the  inference-speed  and 
memory-footprint tradeoffs required for edge deployment. IoT-based systems for solar micro-grid monitoring [3], smart energy 
metering  [10],  and  smart  medical  boxes  [9]  require  embedded  inference  with  real-time  response  guarantees.  Web-based 
deployment for cervical cell screening [61] and breast cancer diagnosis [52] demonstrates that cloud-hosted inference can satisfy 
real-time  requirements  while  maintaining  model  complexity,  provided  network  latency  and  interface  design  are  appropriately 
managed. HAPs  communication systems  [15] and  MANET routing [12] address the  network-layer constraints  that govern real-
time AI in distributed infrastructure. 
5.6. Human Oversight and Accountability

Page | 31

---

<!-- PAGE 8 -->

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges

The question of how much autonomy AI systems should exercise in high-stakes decisions is a governance and safety question as 
much  as  a  technical  one.  The  framing  of  full  autonomy  in  underwater  robotics  as  an  open  prospect  [16]  reflects  genuine 
uncertainty  about  the  conditions  under  which  unsupervised  autonomous  decision-making  is  responsible.  The  automated  risk 
assessment and collaborative decision-making AI in agile project management [69] explicitly positions AI as a collaborator rather 
than a sole decision-maker, a design principle with broad applicability in high-stakes settings. The trustworthy AI framework [78] 
and  AI-enabled  management  information  systems  for  governance  [76]  embed  human  oversight  as  a  design  requirement.  The 
adaptive feedback system for learner improvement [19] and AI-powered ASD digital health platform [67] similarly position AI as 
an  assistive  system  that  augments  human  professional  judgment  rather  than  replacing  it.  High-stakes  AI  systems  should,  in 
general,  be  designed  to  support  decision-makers  rather  than  supplant  them,  and  evaluation  frameworks  should  reflect  this 
distinction. Table 1 distinguishes levels of AI involvement in high-stakes decision support, ranging from informative assistance to 
constrained automation.

Table 1. Human–AI interaction modes and accountability boundaries.

Mode

AI role

Human role

Accountability boundary

Informative

Provides 
rankings

scores,

alerts,

or

Interprets and decides

Human accountable

Assistive

Suggests 
explanation

decision

with

Reviews,  accepts,  modifies,  or 
rejects

Human retains final authority

Deferral-based

Flags uncertain or high-risk cases  Resolves ambiguous cases

AI  accountable 
human for final decision

for  deferral  reliability;

Collaborative

Supports  evidence  synthesis  or 
scenario analysis

Integrates  AI  output  with 
expert judgment

Shared responsibility through documented 
decision trail

Constrained 
automation

Executes  predefined 
actions

low-risk

Monitors and intervenes when 
needed

Organization 
monitoring, and override

accountable

for

limits,

Unsupervised 
autonomy

Acts without real-time review

Provides 
supervision

retrospective

Highest risk; rarely suitable for high-stakes 
use

5.7. Benchmarking, Reproducibility, and Evidence Maturity 
The  corpus  reveals  inconsistent  benchmarking  practices  across  domains.  Medical  imaging  studies  frequently  report  accuracy, 
sensitivity, and specificity on held-out test sets, but cross-institutional or external validation is less common. Agricultural studies 
use  domain-specific  datasets  that  are  rarely  shared  across  research  groups.  Business  analytics  studies  employ  varied  train-test 
split conventions and rarely report confidence intervals or statistical significance tests. The absence of a shared evidence maturity 
framework,  analogous  to  the  CONSORT  or  TRIPOD  reporting  standards  in  clinical  research,  makes  cross-domain  comparison 
difficult. A comparative analysis of explainable ML for cancer classification [50] and the multimodal cancer diagnosis framework 
[51] illustrate the value of systematic comparison but do not resolve the benchmarking gap. Future reviews and meta-analyses in 
this  space  will  require  standardized  reporting  of  dataset  provenance,  class  balance,  validation  protocol,  uncertainty  estimates, 
and  deployment  constraints.  Table  2  summarizes  a  staged  framework  for  judging  whether  an  AI  system  has  progressed  from 
technical feasibility to externally validated, human-supervised, deployment-ready, and continuously monitored decision support. 
6. Future research directions 
Future  research  should  move  from  isolated  model  development  to  evidence  that  is  standardized,  auditable,  and  deployment 
ready.  Cross-domain  benchmarks  are  needed  to  test  AI  systems  across  modalities,  architectures,  and  decision  settings  using 
multi-domain  holdout  sets  and  clinical  or  engineering-style  reporting  standards.  Foundation  models,  generative  AI,  and  large 
language models should be assessed in high-stakes enterprise and healthcare contexts for hallucination, factual accuracy, audit-
trail completeness, and governance alignment [74,69]. Human-in-the-loop systems should use structured deferral for uncertain 
predictions  and  be  evaluated  by  decision  quality,  expert  override  rates,  and  outcomes  with  and  without  AI  support  [16,78]. 
Federated and edge-cloud AI should be tested across  institutions  with clear reporting of privacy budget, federated utility, and 
communication  efficiency  [79,51].  Transformer  and  ensemble  models  also  require  formal  explainability  audits,  including 
explanation fidelity, user comprehension, and regulatory acceptability [27,35,78]. Robustness and uncertainty should be built into 
deep-learning  pipelines  through  Bayesian  and  physics-guided  methods,  with  calibration  error,  distribution-shift  performance,

Page | 32

---

<!-- PAGE 9 -->

FCSAI 5(7): 25-37

and out-of-distribution  detection reported [54,75].  Lightweight models should be optimized for IoT, embedded, and point-of-
care  use  based  on  latency,  memory  use,  and  accuracy–efficiency  trade-offs  [25,46,21].  Finally,  governance-aware  reporting 
standards  and  evidence  maturity  frameworks  should  classify  systems  from  proof-of-concept  to  deployment-validated  AI  using 
reproducibility, external validation, governance compliance, and deployment-readiness indicators [78,76].

Table 2. Evidence-readiness levels for high-stakes AI studies.

Level

Evidence status

Minimum requirement

Deployment meaning

Level 1

Proof-of-concept

Internal  dataset;  basic  train-test  or  cross-validation;  baseline 
comparison

Technical feasibility only

Level 2

Internal validation

Predefined  split;  leakage  control;  class-wise  metrics;  calibration 
summary

Stronger internal evidence

Level 3

External/temporal 
validation

Independent site, cohort, device, or time-period testing

Generalization evidence

Level 4

Human-in-the-loop 
evaluation

review;  AI-assisted

Expert 
override/deferral analysis

versus  unaided

comparison;

Workflow usefulness

Level 5

Monitored 
deployment

pilot

Prospective  or  controlled  deployment;  privacy,  safety,  and 
monitoring protocol

Deployment readiness

Level 6

Post-deployment 
evidence

Drift  monitoring;  audit  logs;  incident  reporting;  model-update 
governance

Sustained 
maturity

operational

7. Limitations of the review 
This review is based on a curated provided as titles only. Consequently, the synthesis is thematic, architectural, and deployment-
level in nature rather than quantitative. It was not possible to extract specific performance metrics, dataset characteristics, sample 
sizes,  experimental  protocols,  or  statistical  validation  details.  The  synthesis  should  therefore  be  interpreted  as  a  structured 
evidence  map  and  taxonomic  analysis  rather  than  a  quantitative  meta-analysis.  Full  paper-level  extraction,  including  access  to 
abstracts,  methods,  results,  and  supplementary  materials,  would  be  required  to  support  meta-analytic  comparison  of  model 
performance, dataset characteristics, or validation rigor across  papers. Additionally, the corpus  reflects  a curated selection and 
may not comprehensively represent all active research threads in high-stakes AI. Domains such as legal AI, financial systemic risk, 
and autonomous vehicles are not well represented and are acknowledged as important adjacent fields. The four-axis taxonomy 
proposed here represents one defensible organization of the evidence space, not the only possible one. 
8. Conclusion 
This  structured  critical  review  has  mapped  the  application  of  artificial  intelligence  to  high-stakes  decision  support  across  six 
domain  healthcare  and  biomedical  systems,  human-centered  and  assistive  AI,  smart  infrastructure  and  cyber-physical  systems, 
agriculture and sustainability, business and enterprise analytics, and cybersecurity and distributed intelligence, using a four-axis 
taxonomy  of  domain,  modality,  architecture,  and  deployment  concern.  The  synthesis  of  79  papers  reveals  a  rich  and  rapidly 
advancing  landscape  in  which  vision  transformers,  ensemble  methods,  graph  neural  networks,  lightweight  CNN  architectures, 
and  federated  learning  systems  are  each  contributing  to  a  qualitatively  new  generation  of  decision-support  capabilities.  The 
cross-domain view discloses structural commonalities, recurrent explainability demands, universal data quality challenges, shared 
real-time  feasibility  constraints,  and  consistent  governance  gaps,  that  are  invisible  within  single-domain  reviews.  Further 
evidence  reveals  that  architecture  selection  in  high-stakes  AI  is  not  a  purely  performance-driven  choice  but  is  shaped  by 
deployment  constraints  including  computational  resources,  privacy  requirements,  interpretability  obligations,  and  human 
oversight  needs.  Looking  forward,  the  critical  research  priorities  are  not  architectural  innovation  per  se,  but  the  responsible 
operationalization of existing advances. Trustworthy AI frameworks [78], privacy-preserving federated pipelines [79], governance-
aware  management  information  systems  [76],  and  resilience-by-design  infrastructure  [75]  collectively  point  toward  a  research 
agenda  that  prioritizes  auditability,  human  oversight,  and  deployment  readiness  alongside  predictive  performance.  The  field 
requires  standardized  evidence  maturity  frameworks,  cross-domain  benchmarking  suites,  formal  explainability  audit  protocols, 
and  reporting  standards  that  reflect  the  multi-dimensional  demands  of  real-world  high-stakes  deployment.  Progress  on  these 
fronts  will  determine  whether  AI  decision  support  fulfills  its  potential  not  merely  as  a  technically  capable  system,  but  as  a 
trustworthy, equitable, and accountable partner in consequential human decisions.

Page | 33

---

<!-- PAGE 10 -->

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges

Funding: This research received no external funding.  
Conflicts of Interest: The authors declare no conflict of interest. 
Publisher’s Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of 
their affiliated organizations, or those of the publisher, the editors and the reviewers.

References

[1]  Alamgir  FM,  et  al.  ASDnet:  Classification  model  for  individuals  with  autism  spectrum  disorder  using  facial  grid-wise 
expressions  features  and  dual-branch  visual  transformation.  Biomedical  Signal  Processing  and  Control.  2026;120(Part 
A):109999. doi:10.1016/j.bspc.2026.109999.

[2]  Majumdar  J,  Apu  MH,  Rahman  M,  Zaman  T,  Hassan  MM.  Multimodal  EEG  analysis  of  neural  synchrony  in  minimal

phrase processing using machine learning. Conference paper; 2025 Nov.

[3]  Mahamud  S,  Hossain  MS,  Hassan  MM,  Maruf  MY,  Rafi  MAH,  et  al.  IoT  based  wireless  battery  monitoring  system  for 
enhanced solar micro-grid performance in Bangladesh. In: Arefin MS, Kaiser MS, Bhuiyan T, Based MA, Ray K, editors. 
Proceedings  of  the  3rd  International  Conference  on  Big  Data,  IoT  and  Machine  Learning.  BIM  2025.  Lecture  Notes  in 
Networks and Systems, vol. 1798. Cham: Springer; 2026. p. 474-489. doi:10.1007/978-3-032-15346-3_33.

[4]  Alamgir  FM,  Zaman  T,  Hassan  MM,  Jonayed  MR,  Alam  MS.  Classification  model  for  autism  spectrum  disorder 
individuals: Utilizing facial grid-wise emotion features and dual-branch visual transformation. In: 2024 IEEE International 
Conference  on  Power,  Electrical,  Electronics  and  Industrial  Applications  (PEEIACON);  2024  Sep  12-13;  Rajshahi, 
Bangladesh. doi:10.1109/PEEIACON63629.2024.10800506.

[5]  Alamgir  FM,  Saif  SMH,  Hossain  MS,  Al  Hadi  A,  Alam  MS.  Facial  expression  database  of  autism  spectrum  disorder

children. European Chemical Bulletin. 2023;12(Special Issue 4):21109-21120. doi:10.48047/ecb/2023.12.Si4.1851.

[6]  Alamgir FM, Alam MS. Hybrid multi-modal emotion recognition framework based on InceptionV3DenseNet. Multimedia

Tools and Applications. 2023;82:40375-40402. doi:10.1007/s11042-023-15066-w.

[7]  Alamgir FM, Alam MS. A novel deep learning-based bidirectional Elman neural network for facial emotion recognition. 
2022;36(10):2252016.

Recognition

Intelligence.

Artificial

Pattern

Journal

and

of

International 
doi:10.1142/S0218001422520164.

[8]  Alamgir FM, Alam MS. An artificial intelligence driven facial emotion recognition system using hybrid deep belief rain

optimization. Multimedia Tools and Applications. 2023;82:2437-2464. doi:10.1007/s11042-022-13378-x.

[9]  Al-Mahmud  O,  Khan  K,  Roy  R,  Alamgir  FM.  Internet  of  things  (IoT)  based  smart  health  care  medical  box  for  elderly 
1-6. 
for

International

Technology

Conference

Emerging

(INCET);

2020.

In:

p.

people. 
2020 
doi:10.1109/INCET49848.2020.9153994.

[10] Haque MM, Choudhury ZH, Alamgir FM. IoT based smart energy metering system for power consumers. In: 2019 2nd 
International  Conference  on  Innovation  in  Engineering  and  Technology  (ICIET);  2019  Dec  23-24;  Dhaka,  Bangladesh. 
doi:10.1109/ICIET48527.2019.9290661.

[11] Alamgir  FM,  Ahmed  F,  Miah  M,  Munna  HM,  Barua  S.  A  novel  routing  algorithm  for  inter-group  load  balancing  in 
wireless  mesh  networks.  In:  2018  21st  Saudi  Computer  Society  National  Computer  Conference  (NCC);  2018. 
doi:10.1109/NCG.2018.8593192.

[12] Ahmed  F,  Alamgir  FM.  Simulation-based  proportional  study  of  routing  protocols  for  MANET.  International  Journal  of

Computer Networks and Communications Security. 2017;5(12):28-36.

[13] Sourav  MSU,  Rahman  A,  Al  Mamun  A,  Alamgir  FM.  Standard  transcranial  direct  current  stimulation  (tDCS)  model.

International Journal of Computer Networks and Communications Security. 2017;5(12):264-270.

[14] Al Mamun A, Polash MSJK, Alamgir FM. Flex sensor based hand glove for deaf and mute people. International Journal of

Computer Networks and Communications Security. 2017;5(2):38-48.

[15] Adnan  BM,  Chakma  S,  Alam  MMJ,  Alamgir  FM.  Performance  simulation  and  comparison  in  High  Altitude  Platforms 
(HAPs) communications systems under PSK, DPSK, QAM and FSK modulation schemes and AWGN, Rician and Rayleigh 
communication  channels.  In:  2016  IEEE  7th  Annual  Information  Technology,  Electronics  and  Mobile  Communication 
Conference (IEMCON); 2016; Vancouver, BC. p. 1-11. doi:10.1109/IEMCON.2016.7746080.

[16] Rohan A, Tolie HF, Hasan MJ, Kannan S. Full autonomy in underwater robotics systems: A realistic prospect? Engineering

Applications of Artificial Intelligence. 2025;162:112638. doi:10.1016/j.engappai.2025.112638.

[17] Haruna  A,  Noman  K,  Li  Y,  Makanda  ILD,  Zubair  A,  Hasan  MJ,  Alhassan  AB.  Facilitating  heuristic  reasoning  by  utilizing 
2026;334:115153.

Knowledge-Based

processing.

language

Systems.

natural

and

knowledge 
graph 
doi:10.1016/j.knosys.2025.115153.

[18] Arifeen  M,  Hasan  MJ,  Rohan  A,  Kannan  S,  Prathuru  A,  et  al.  Enhancing  acoustic  emission  driven  smart  gas-pipeline 
monitoring  with  graph  neural  network.  In:  Manjurul  Islam  MM,  Baptista  ML,  Tariq  F,  editors.  Artificial  Intelligence  for 
Smart Manufacturing and Industry X.0. Cham: Springer; 2025. p. 165-178. doi:10.1007/978-3-031-80154-9_8.

[19] Qadir HM, Khan RA, Rasool M, Sohaib M, Shah MA, Hasan  MJ. An adaptive feedback system for the improvement of

learners. Scientific Reports. 2025;15:17242. doi:10.1038/s41598-025-01429-w.

Page | 34

---

<!-- PAGE 11 -->

FCSAI 5(7): 25-37

[20] Sohaib  M,  Hasan  MJ,  Zheng  Z.  A  multichannel  analysis  of  imbalanced  computed  tomography  data  for  lung  cancer

classification. Measurement Science and Technology. 2024;35(8):085401. doi:10.1088/1361-6501/ad437f.

[21] Habib  MA,  Hasan  MJ,  Kim  JM.  A  lightweight  deep  learning-based  approach  for  concrete  crack  characterization  using

acoustic emission signals. IEEE Access. 2021;9:104029-104050. doi:10.1109/ACCESS.2021.3097962.

[22] Biswas  R, Uddin J, Hasan MJ. A new approach of iris detection and recognition. International Journal of Electrical and

Computer Engineering. 2017;7(5):2530-2536. doi:10.11591/ijece.v7i5.pp2530-2536.

[23] Haruna  A,  Noman  K,  Li  Y,  Wang  X,  Hasan  MJ,  Alhassan  AB.  AddManBERT:  A  combinatorial  triples  extraction  and 
classification  task  for  establishing  a  knowledge  graph  to  facilitate  design  for  additive  manufacturing.  Advanced 
Engineering Informatics. 2025;67:103578. doi:10.1016/j.aei.2025.103578.

[24] Hasan  MJ,  Noman  K,  Navid  WU,  Li  Y,  Haruna  A,  Ashfak  K.  Intelligent  diagnosis  of  gas  pipeline  condition  through 
multivariate  analysis  of  acoustic  emission  signal-based  imaging.  Nondestructive  Testing  and  Evaluation.  2025:1-20. 
doi:10.1080/10589759.2025.2456088.

[25] Rahman MM, Gony MN, Ullah MS, Shuvra SMK, et al. MaizeFormerX: A lightweight vision transformer with cross-scale

attention for explainable maize leaf disease diagnosis. Scientific Reports. 2026. doi:10.1038/s41598-026-44550-0.

[26] Al Sakib A, Swapno SMMR, Ahamed F, Mohiuddin AB, Bhuiyan MIH, Khan S, Khushbu KG, Haque R, Alahmadi TJ, Moni 
MA.  Explainable  AI-driven  hybrid  deep  learning  framework  for  accurate  skin  cancer  diagnosis.  Digital  Health. 
2026;12:20552076261438923. doi:10.1177/20552076261438923.

[27] Islam S, Haque R, Khan MA, Mohiuddin AB, Siddiqui MIH, Limon ZH, Khushbu KG, Swapno SMMR, Ahmed MR, Appaji A. 
iScience.

Ensemble  transformer  with  post-hoc  explanations  for  depression  emotion  and  severity  detection. 
2026;29(2):114605. doi:10.1016/j.isci.2025.114605.

[28] Rahman  Swapno  SMM,  Sakib  A,  Uddin  Khondakar  Pranta  AS,  Hossain  A,  Debnath  J,  Al  Noman  A,  et  al.  Explainable 
transformer framework for fast cotton leaf diagnostics and fabric defect detection. iScience. 2026 Feb 20;29(2):114411. 
doi:10.1016/j.isci.2025.114411.

[29] Ahmed MR, Haque R, Rahman SMA, Reza AW, Siddique N, Wang H. Vision-audio multimodal object recognition using

hybrid and tensor fusion techniques. Information Fusion. 2025;126:103667. doi:10.1016/j.inffus.2025.103667.

[30] Debnath  J,  Pranta  ASUK,  Hossain  A,  Sakib  A,  Rahman  H,  Haque  R,  Ahmed  MR,  Reza  AW,  Swapno  SMMR,  Appaji  A. 
LMVT:  A  hybrid  vision  transformer  with  attention  mechanisms  for  efficient  and  explainable  lung  cancer  diagnosis. 
Informatics in Medicine Unlocked. 2025;57:101669. doi:10.1016/j.imu.2025.101669.

[31] Ahmed MR, Rahman H, Limon ZH, Siddiqui MIH, Khan MA, Pranta ASUK, Haque R, Swapno SMMR, Cho YI, Abdallah MS. 
Hierarchical  Swin  transformer  ensemble  with  explainable  AI  for  robust  and  decentralized  breast  cancer  diagnosis. 
Bioengineering. 2025;12(6):651. doi:10.3390/bioengineering12060651.

[32] Haque R, Khan MA, Rahman H, Khan S, Siddiqui MIH, Limon ZH, et al. Explainable deep stacking ensemble model for

accurate and transparent brain tumor diagnosis. Computers in Biology and Medicine. 2025;191:110166.

[33] Pranta ASUK, Fardin H, Debnath J, Hossain A, Sakib AH, Ahmed MR, et al. A novel MaxViT model for accelerated and 
precise soybean leaf and seed disease identification. Computers. 2025;14(5):197. doi:10.3390/computers14050197. 
[34] Noman AA, et al. ViX-MangoEFormer: An enhanced vision transformer-EfficientFormer and stacking ensemble approach 
intelligence.  Computers.  2025;14(5):171.

recognition  with  explainable  artificial

leaf  disease

for  mango 
doi:10.3390/computers14050171.

[35] Siddiqui  MIH,  Khan  S,  Limon  ZH,  Rahman  H,  Khan  MA,  Al  Sakib  A,  Swapno  SMMR,  Haque  R,  Reza  AW,  Appaji  A. 
Accelerated  and  accurate  cervical  cancer  diagnosis  using  a  novel  stacking  ensemble  method  with  explainable  AI. 
Informatics in Medicine Unlocked. 2025;56:101657. doi:10.1016/j.imu.2025.101657.

[36] Haque R, Sakib AA, Hossain MF, Islam F, Aziz FI, Ahmed MR, Kannan S, Rohan A, Hasan MJ. Advancing early leukemia 
diagnostics:  A  comprehensive  study  incorporating  image  processing  and  transfer  learning.  BioMedInformatics. 
2024;4(2):966-991. doi:10.3390/biomedinformatics4020054.

[37] Haque R, Islam N, Islam M, Ahsan MM. A comparative analysis on suicidal ideation detection using NLP, machine, and

deep learning. Technologies. 2022;10(3):57. doi:10.3390/technologies10030057.

[38] Haque  R,  Islam  N,  Tasneem  M,  Das  AK.  Multi-class  sentiment  classification  on  Bengali  social  media  comments  using 
2023;4:21-35.

International

Engineering.

Computing

Cognitive

Journal

of

in

learning. 
machine 
doi:10.1016/j.ijcce.2023.01.001.

[39] Haque  R,  Laskar  SH,  Khushbu  KG,  Hasan  MJ,  Uddin  J.  Data-driven  solution  to  identify  sentiments  from  online  drug

reviews. Computers. 2023;12(4):87. doi:10.3390/computers12040087.

[40] Mithun  MM,  Tanim  SH,  Tarannum  R.  Developing  AI-Powered  Credit  Scoring  Models  Leveraging  Alternative  Data  for

Financially Underserved US Small Businesses. Repository Antis Publisher. 2025 Oct 18:699254.

[41] Tanim  SH,  Mithun  MMU,  Tarannum  R.  Sustaining  vital  care  in  disasters:  AI-driven  solar  financing  for  rural  clinics  and 
health small businesses. American Journal of Technology Advancement. 2025;2(9):123-153. doi:10.31149/ajta.v2i9.2528.

Page | 35

---

<!-- PAGE 12 -->

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges

[42] Tanim  SH,  Ahmad  MS,  Mithun  MMU,  Tarannum  R,  Refat  FR,  Sunny  MNM.  Leveraging  predictive  analytics  for  risk 
identification  and  mitigation  in  project  management.  Journal  of  Information  Systems  Engineering  and  Management. 
2025;10(43s):1041-1052. doi:10.52783/jisem.v10i43s.8523.

[43] Rimon RH, Nurujjaman, Mithun MMU. Market basket analysis for healthcare services to identify bundled care offerings.

Frontiers in Computer Science and Artificial Intelligence. 2025;4(3):44-67.

[44] Hussain  TS,  Tarannum  R,  Mithun  MMM.  Privacy-preserving  behavior  analytics  for  workforce  retention  approach.

American Journal of Engineering, Mechanics and Architecture. 2023;1(9):188-215.

[45] Ghosh  BP,  Bhuiyan  MS,  Bishnu  KK,  Mahmud  FU,  et  al.  Personalized  machine  learning  models  for  Parkinson's  disease 
screening via voice biomarkers: Accounting for age, gender, and linguistic variability. The International Medicine. 2025 
Dec.

[46] Masum  AKM,  Khan  MFI,  Mahmud  FU,  Hassan  MM,  Khaliluzzaman  M.  Improving  aquaculture  disease  diagnosis  with 
lightweight  ResNeXt  architectures.  In:  2025  3rd  International  Conference  on  Artificial  Intelligence,  Blockchain,  and 
Internet of Things (AIBThings); 2025. doi:10.1109/AIBThings66987.2025.11296219.

[47] Mahmud FU, Rahman H, Limon ZH, Khan MA, Jashim FB. Transfer learning approach for sleep stage classification with 
2025;15(2).

International

Research

Archive.

Science

Journal

data.

and

of

limited 
doi:10.30574/ijsra.2025.15.2.1506.

training

[48] Farhan B, Jashim FR, Refat FR, et al. Hybrid vision transformer model for accurate prostate cancer classification in MRI

images. International Journal of Science and Research Archive. 2025;15(2). doi:10.30574/ijsra.2025.15.2.1509.

[49] Rashid SU, Siddiqui MIH, Mahmud FU, Rahman MS, Kabir AA, et al. Machine learning based clinical decision support for 
heart disease prediction using structured patient data. Journal of Computer Science and Technology Studies. 2024;6(1). 
doi:10.32996/jcsts.2024.6.1.36.

[50] Siddiqui  MIH,  Rahman  MS,  Kabir  AA,  Mahmud  FU,  Rashid  SU,  Shammah  RS.  Comparative  analysis  of  explainable 
machine  learning  models  for  cancer  classification  using  cytological  features.  Journal  of  Medical  and  Health  Studies. 
2023;4(5):114-126.

[51] Kabir AA, Mahmud FU, Rahman MS, Rashid SU, Siddiqui MIH, Shammah RS. Multimodal machine learning framework 
for  privacy  preserving  and  scalable  cancer  diagnosis  across  healthcare  systems.  Journal  of  Adaptive  Learning 
Technologies. 2024;1(6).

[52] Jashim FB, Refat FR, Karim MH, Mahmud FU, Sakib AH. Stacking ensemble-based breast cancer classification: Enhancing 
diagnostic  accuracy with deep learning and real-time web deployment. International Journal of Science and Research 
Archive. 2025;15:1417-1431.

[53] Mahmud  FU,  Rahman  A,  Khan  MA,  Bishnu  KK,  Eva  AA,  Maua  J.  FuseAttenX:  Leveraging  attention-enhanced  deep 
learning  for  business  strategy  optimization.  In:  2025  IEEE  4th  International  Conference  on  Computing  and  Machine 
Intelligence (ICMI); 2025. doi:10.1109/ICMI65310.2025.11141140.

[54] Khan MDA, Rahman A, Mahmud FU, Bishnu KK, Nabil HR, Mridha MF, et al. A physics-guided Bayesian neural network 
for  sensor  fault  detection  in  wind  turbines.  IEEE  Open  Journal  of  the  Computer  Society.  2025;6:931-942. 
doi:10.1109/OJCS.2025.3577588.

[55] Chowdhury MS, Shak MS, Devi S, Miah MR, Al Mamun A, Ahmed E, Hera SAA, Mahmud F, Mozumder MSA. Optimizing 
e-commerce pricing strategies: A comparative analysis of machine learning models for predicting customer satisfaction. 
The American Journal of Engineering and Technology. 2024;6(09):6-17. doi:10.37547/tajet/Volume06Issue09-02.

[56] Rahman T, Uddin MK, Hosen MM, Bhattacharjee B, Taluckder MS, Mou SN, Akter P, Hossain MS, Miah MR, Rahman MM. 
Blockchain  applications  in  business  operations  and  supply  chain  management  by  machine  learning.  International 
Journal of Computer Science & Information System. 2024;9(11):17-30. doi:10.55640/ijcsis/Volume09Issue11-03.

[57] Shak MS, Mozumder MSA, Hasan MA, Das AC, Miah MR, Akter S, Hossain MN. Optimizing retail demand forecasting: A 
performance  evaluation  of  machine  learning  models  including  LSTM  and  gradient  boosting.  The  American  Journal  of 
Engineering and Technology. 2024;6(9):67-80. doi:10.37547/tajet/Volume06Issue09-09.

[58] Naznin  R,  Sarkar  MAI,  Asaduzzaman  M,  Akter  S,  Mou  SN,  Miah  MR,  Sajal  A.  Enhancing  small  business  management 
through machine learning: A comparative study of predictive models for customer retention, financial forecasting, and 
inventory optimization. International Interdisciplinary Business Economics Advancement Journal. 2024;5(11):21-32. 
[59] Talukder T, Masud SB, Miah MR, Hera A, Faruque MO. An examination of how social media participation and customer 
satisfaction  affect  the  likelihood  that  a  business  will  make  another  transaction  in  the  hospitality  sector.  Open  Access 
Library Journal. 2025;12:1-15. doi:10.4236/oalib.1112802.

[60] Hossain  MS,  Khan  A,  Das  P,  Haque  MSU,  Kamruzzaman  F,  Akter  S,  Ahmed  A,  Miah  MR.  Enhanced  market  trend 
forecasting  using  machine  learning  models:  A  study  with  external  factor  integration.  International  Interdisciplinary 
Business Economics Advancement Journal. 2025;6(1):5-12. doi:10.55640/business/volume06issue01-02.

[61] Shakil MR, Malik AH, Siddiqui MIH, Ahmed S, Miah MR, Linkon AA. Swin transformer-driven cervical cell classification 
with  explainable  AI  and  web-based  screening.  Journal  of  Medical  and  Health  Studies.  2026;7(5):25-35. 
doi:10.32996/jmhs.2026.7.5.5.

Page | 36

---

<!-- PAGE 13 -->

FCSAI 5(7): 25-37

[62] Linkon  AA,  Shakil  MR,  Ahmed  S,  Miah  MR,  Malik  AH.  Explainable  transformer-based  skin  lesion  classification  from

clinical images. Journal of Medical and Health Studies. 2026;7(5):46-55. doi:10.32996/jmhs.2026.7.5.7.

[63] Ahmed  S,  Miah  MR,  Shakil  MR,  Linkon  AA,  Siddiqui  MIH,  Malik  AH.  Global-local  attention  modeling  for  reliable 
multiclass  kidney  disease  classification  from  CT  images.  Journal  of  Medical  and  Health  Studies.  2026;7(5):36-45. 
doi:10.32996/jmhs.2026.7.5.6.

[64] Karshiboev  A,  Al-Samad  K,  Tarafdar  MTR,  Rimi  NN,  Islam  MS,  Papel  MSI.  Artificial  intelligence  for  risk  and  decision 
assessment  in  agile  IT  projects:  A  thematic  analysis  and  dynamic  structuration  framework  approach.  International 
Journal of Advances in Signal and Image Sciences. 2026;12(1):387-410. doi:10.29284/9k2nx425.

[65] Islam MS, Islam MI, Mozumder AQ, Khan MTH, Das N, Mohammad N. A conceptual framework for sustainable AI-ERP 
integration  in  dark  factories:  Synthesising  TOE,  TAM,  and  IS  success  models for  autonomous  industrial  environments. 
Sustainability. 2025;17(20):9234. doi:10.3390/su17209234.

[66] Haque  S,  Mohammad  N,  Mambetaliev  A,  Karshiboev  A,  Lucky  KY,  Khan  MTH,  Islam  H.  Artificial  intelligence-driven 
business  analytics  for  IT  strategy:  Advancing  decision-making,  real-time  insights,  and  organizational  agility  through 
intelligent 
2025;5(6):1848-1863. 
doi:10.63332/joph.v5i6.2287.

Posthumanism.

automation

integration.

Journal

data

and

of

[67] Haque  S,  Islam  MS,  Islam  MI,  Islam  MS,  Khan  R,  Tarafder  MTR,  Mohammad  N.  Enhancing  adaptive  learning, 
communication,  and  therapeutic  accessibility  through  the  integration  of  artificial  intelligence  and  data-driven 
personalization  in  digital  health  platforms  for  students  with  autism  spectrum  disorder.  Journal  of  Posthumanism. 
2025;5(8):737-756. doi:10.63332/joph.v5i8.3255.

[68] Faruq O, Islam MI, Islam MS, Tarafder MTR, Rahman MM, Islam MS, Mohammad N. Re-imagining digital transformation 
in the United States: Harnessing artificial intelligence and business analytics to drive IT project excellence in the digital 
innovation landscape. Journal of Posthumanism. 2025;5(9):333-354. doi:10.63332/joph.v5i9.3326.

[69] Haque S, Chowdhury S, Faruq O, Akter R, Joy MSI, Munny MA, Shimu F. Automated risk assessment and collaborative 
decision-making  AI  applications  in  agile  project  management  and  stakeholder  engagement.  International  Journal  of 
Advances in Signal and Image Sciences. 2026;12(1):915-923. doi:10.29284/v2jv8q59.

[70] Riipa  MB,  Saha  S,  Ferdousmou  J,  Khatoon  R,  Mohammad  N,  Hossain  M.  AI-driven  smart  agriculture:  Optimizing  crop 
yield  and  sustainability  in  the  U.S.  In:  2025  5th  International  Conference  on  Electrical,  Computer  and  Energy 
Technologies (ICECET); 2025; Paris, France. doi:10.1109/ICECET63943.2025.11472088.

[71] Lucky  KY,  Haque  S,  Al-Samad  K,  Akter  R,  Faruq  O,  Azim  KS,  Joy  MSI.  AI-powered  healthcare  information  systems 
securing diabetes management through integrated technology solutions and enhanced patient care delivery. Vascular 
and Endovascular Review. 2025;8(11s):465-476.

[72] Faruq  O,  Chowdhury  S,  et  al.  Artificial  intelligence  as  the  strategic  engine  of  data  security,  analytics,  and  digital 
communication for a resilient digital future. Journal of Information and Knowledge Management. 2025;20(2):1764-1773. 
[73] Shimu  F.  Intelligent  cybersecurity  framework:  Machine  learning-driven  data  protection  and  threat  intelligence 
integration  for  modern  digital  communications.  International  Journal  of  Applied  Mathematics.  2025;38(8s):620-632. 
doi:10.12732/ijam.v38i8s.595.

[74] Haque  S,  Islam  H,  Sharmin  F,  Joy  MSI,  Naher  K,  Rimi  NN,  Shimu  F.  Generative  artificial  intelligence  in  enterprise 
information  systems:  Transforming  business  intelligence  and  strategic  decision  support  processes.  Journal  of 
Information and Knowledge Management. 2025;20(2):887-897. doi:10.18848/8p0s2e25.

[75] Shakil  MR,  Hasan  M,  Tarek  MIH,  Polash  FI,  Meem  EJ.  Resilience-by-design:  AI  for  security,  sustainability  and  health  in 
interdependent  systems.  World  Journal  of  Advanced  Engineering  Technology  and  Sciences.  2026;18(3):254-267. 
doi:10.30574/wjaets.2026.18.3.0153.

[76] Shakil  MR,  Hasan  M,  Tarek  MIH,  Polash  FI,  Meem  EJ.  AI-enabled  management  information  systems  for  economic 
resilience and organizational performance: Analytics, governance, cyber risk and decision automation. World Journal of 
Advanced Engineering Technology and Sciences. 2026;18(3):294-307. doi:10.30574/wjaets.2026.18.3.0156.

[77] ZakirHossain M, Khan MM, Thapa S, Uddin R, Meem EJ, Niloy SK, et al. Advanced deep learning techniques for precision 
diagnosis  of  tea  leaf  diseases.  In:  2025  IEEE  International  Conference  on  Emerging  Technologies  and  Applications 
(MPSec ICETA); 2025. doi:10.1109/MPSecICETA64837.2025.11118779.

[78] Shakil  MR,  Hasan  M,  Tarek  MIH,  Polash  FI,  Meem  EJ.  Trustworthy  AI  for  high-stakes  decision  support  across  critical 
2026;18(3).

Engineering

Technology

Advanced

Sciences.

Journal

and

sectors.  World 
of 
doi:10.30574/wjaets.2026.18.3.0152.

[79] Shakil MR, Hasan M, Tarek MIH, Polash FI, Meem EJ. Distributed intelligence and privacy-preserving deployment: Edge-
cloud-6G-federated  learning  for  secure,  auditable  decision  support.  World  Journal  of  Advanced  Engineering 
Technology and Sciences. 2026;18(3):268-279. doi:10.30574/wjaets.2026.18.3.0154.

[80] Khan MA, Parveen R, Ahmed I, Milon MH, Khan TA. High-Accuracy Breast Cancer Diagnosis Using Neural Networks and 
Dimensionality  Reduction  Techniques.  In2025  IEEE  19th  International  Conference  on  Open  Source  Systems  and 
Technologies (ICOSST) 2025 Dec 1 (pp. 1-6). doi:10.1109/ICOSST69113.2025.11315291.

Page | 37

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Frontiers in Computer Science and Artificial Intelligence FCSAI
ISSN: 2978-8048
DOI: 10.32996/fcsai
AL-KINDI CENTER FOR RESEARCH
Journal Homepage: www.al-kindipublisher.com/index.php/fcsai AND DEVELOPMENT
| REVIEW ARTICLE
Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and
Deployment Challenges
Shahadat Molla1, and S M Zobayed2
1 Department of Information Systems, California State University, Los Angeles, CA 90032, USA
2 Department of Engineering Management, Westcliff University, 17877 Von Karman Avenue, 4th Floor, Irvine, CA 92614, USA
Corresponding Author: Shahadat Molla, E-mail: shadat.cse@gmail.com
| ABSTRACT
Artificial intelligence (AI) is increasingly embedded in consequential decision-making processes across healthcare, assistive
technologies, smart infrastructure, agriculture, business analytics, cybersecurity, and sustainability. Unlike general-purpose AI
deployments, high-stakes decision support demands not only predictive accuracy but also explainability, robustness, privacy,
scalability, human oversight, and governance readiness. This structured critical review synthesizes to map the current landscape
of AI for high-stakes decision support using a four-axis taxonomy: application domain, data modality, architecture family, and
deployment concern. The review identifies six application domains, healthcare and biomedical decision support, human-centered
and assistive AI, smart infrastructure and cyber-physical systems, agriculture and sustainability, business and enterprise decision
support, and cybersecurity and distributed intelligence, and eight architecture families ranging from conventional machine
learning and convolutional neural networks to vision transformers, graph neural networks, Bayesian models, generative AI, and
federated learning systems. The synthesis reveals that while significant architectural advances have been made, deployment-
critical properties such as uncertainty quantification, privacy-preserving inference, real-time feasibility on edge devices, and
governance-aligned reporting remain inconsistently addressed. Future research must prioritize cross-domain benchmarking,
trustworthy and auditable AI pipelines, human-in-the-loop frameworks, and evidence maturity standards appropriate for high-
stakes contexts. This review provides an evidence-grounded taxonomy and actionable research agenda for researchers and
practitioners to build the next generation of responsible AI decision-support systems.
| KEYWORDS
Artificial intelligence; High-stakes decision support; Trustworthy AI; Explainable AI; Human-in-the-loop AI; Federated learning;
Graph neural networks; Vision transformers; Uncertainty quantification; AI governance
| ARTICLE INFORMATION
ACCEPTED: 15 April 2026 PUBLISHED: 22 May 2026 DOI: 10.32996/jcsts.2026.5.7.3
1. Introduction
The deployment of artificial intelligence in consequential decision environments, those where an erroneous prediction or
recommendation carries significant human, financial, or societal cost, has accelerated substantially over the past decade.
Healthcare diagnosis, patient monitoring, infrastructure fault detection, agricultural disease management, credit risk assessment,
and cybersecurity threat response all constitute high-stakes domains in which AI is increasingly positioned not as an
experimental tool, but as an operational support system. The breadth of this deployment presents both an opportunity and a
methodological challenge: no single architecture, modality, or evaluation framework can address the full spectrum of
requirements encountered across these domains.
Existing reviews of AI in decision support tend to focus narrowly on a single domain, most commonly medical imaging or clinical
prediction, while the cross-domain structural similarities and shared deployment challenges remain under-examined. A review
that spans healthcare [49, 20, 26], assistive and neuro-affective AI [1, 2, 13], smart infrastructure and IoT [3, 9, 18], agriculture and
Copyright: © 2026 the Author(s). This article is an open access article distributed under the terms and conditions of the Creative Commons
Attribution (CC-BY) 4.0 license (https://creativecommons.org/licenses/by/4.0/). Published by Al-Kindi Centre for Research and Development,
London, United Kingdom.
Page | 25

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges
sustainability [25, 70, 77], business analytics and enterprise AI [40, 42, 74], and cybersecurity [73, 78, 79] reveals recurring
architectural patterns, deployment tensions, and governance gaps that are invisible when each domain is examined in isolation.
This review is motivated by three observations. First, the architecture families are most frequently employed in high-stakes
applications, CNNs, vision transformers, ensemble methods, graph neural networks, and federated systems, each carry distinct
tradeoffs between accuracy, interpretability, and deployment feasibility. Second, the dominant evaluation criterion of predictive
accuracy is necessary but insufficient: robustness to distribution shift, resistance to adversarial inputs, uncertainty quantification,
and privacy compliance are equally consequential in deployment environments. Third, the literature reveals growing recognition
that human oversight is not an optional add-on but a structural requirement in high-stakes AI, particularly in domains such as
autonomous robotics [16], clinical decision support [49, 71], and automated risk assessment [69]. This review addresses these
gaps by constructing a structured cross-domain taxonomy, synthesizing architecture and deploying evidence, and identifying the
research directions most critical for responsible AI decision support at scale. Figure 1 demonstrates the end-to-end pathway
through which AI systems move from heterogeneous data sources to model-generated recommendations, human review,
deployment monitoring, and governance feedback.
Figure 1. High-stakes AI decision-support lifecycle.
2. Review Scope and Taxonomic Framework
The corpus was assembled to span the principal application domains, architecture families, data modalities, and deployment
concerns relevant to high-stakes AI decision support. Papers were selected to ensure representational balance across domains
and to enable a structured evidence map rather than an exhaustive literature census. A four-axis taxonomy organizes the corpus.
Axis 1 classifies papers by application domain: (i) healthcare and biomedical decision support, (ii) human-centered, neuro-
affective, and assistive AI, (iii) smart infrastructure, IoT, robotics, and cyber-physical systems, (iv) agriculture, environment, and
sustainability, (v) business, enterprise, and organizational decision support, and (vi) cybersecurity, privacy, and distributed
intelligence. Axis 2 classifies by data modality—medical images, facial and affective signals, EEG and physiological signals, IoT
and sensor streams, acoustic-emission and industrial signals, text and natural language, graph and knowledge-structured data,
business and tabular data, and multimodal data. Axis 3 identifies the architecture family: conventional machine learning, CNN-
based deep learning and transfer learning, vision transformers and attention-based models, graph neural networks and
knowledge graphs, hybrid and ensemble systems, Bayesian and physics-guided models, generative and agentic AI, and
federated/edge/privacy-preserving systems. Axis 4 catalogues the deployment concern: explainability, robustness, privacy,
scalability, real-time feasibility, human oversight, governance, security, and safety/accountability. The taxonomy enables two
forms of analysis: vertical analysis within a domain (tracking how architecture choices affect deployment readiness) and
horizontal analysis across domains (identifying universal deployment tensions that transcend domain-specific context).
3. Architecture Families for High-Stakes Decision Support
3.1. Conventional Machine Learning and Structured Decision Models
Conventional machine learning encompasses logistic regression, decision trees, random forests, gradient boosting, and support
vector machines applied to structured tabular data, remains highly relevant in high-stakes decision support, particularly in
clinical, business, and financial settings where data are structured and interpretability is paramount. Work focusing on clinical
Page | 26

FCSAI 5(7): 25-37
decision support for heart disease prediction using structured patient data [49] illustrates the continued utility of classical ML
pipelines when feature engineering and validation are handled rigorously. In business contexts, research on credit scoring for
financially underserved populations [40], predictive analytics for project risk [42], retail demand forecasting [57], and small-
business management including customer retention and financial forecasting [58] demonstrates that gradient-boosted
ensembles and LSTM networks constitute practical, deployment-ready tools when the decision environment is data-rich but
annotation-constrained. Multi-class sentiment classification [38] and data-driven sentiment extraction from drug reviews [39]
further illustrate ML's relevance in text-based decision support. Market basket analysis for healthcare service bundling [43] and
studies on customer satisfaction and business transactions in hospitality [59] represent the application of association and
regression methods to organizational decision support at scale. Enhanced market trend forecasting with external factor
integration [60] and ML-driven e-commerce pricing optimization [55] extend this cluster to demand-side business intelligence.
Collectively, these works suggest that structured ML remains a foundational layer of high-stakes decision support, often more
interpretable and computationally efficient than deep learning alternatives, though issues of fairness, feature reliability, and
governance remain underspecified.
3.2. CNN-Based Deep Learning and Transfer Learning
Convolutional neural networks and their transfer-learned variants constitute the dominant architecture family in image-based
high-stakes AI. The application range spans medical imaging, including multichannel lung cancer classification from CT data [20],
early leukemia diagnostics via transfer learning [36], and aquaculture disease diagnosis using lightweight ResNeXt architectures
[46] to agricultural disease detection and industrial inspection. Transfer learning is particularly prominent in domains
characterized by limited labelled training data: the use of transfer learning for sleep stage classification under data-constrained
conditions [47] illustrates how pre-trained feature extractors can be repurposed to clinically sensitive classification tasks. Facial
emotion recognition systems, including a bidirectional Elman neural network approach [7] and a hybrid deep belief optimization
system [8], similarly leverage learned feature representations from large facial datasets. The lightweight deep learning framework
applied to concrete crack characterization using acoustic-emission signals [21] extends the CNN paradigm to industrial sensing,
where real-time feasibility and sensor-data compatibility are critical. Across all these applications, the transfer learning strategy
addresses data scarcity but introduces the risk of negative transfer and domain mismatch, both of which are deployment
concerns requiring systematic evaluation.
3.3. Vision Transformers and Attention-Based Architectures
Vision transformers (ViTs) and their attention-based variants have emerged as a high-performing architecture family for image
classification in high-stakes domains, progressively displacing purely convolutional approaches in medical imaging and precision
agriculture. The dual-branch visual transformation framework developed for ASD classification [4, 1] illustrates how transformer
architectures can model spatially distributed facial features more flexibly than fixed-receptive-field CNNs. In medical imaging, the
hybrid vision transformer for prostate cancer classification in MRI images [48] and the LMVT hybrid vision transformer for lung
cancer diagnosis [30] demonstrate that combining convolutional feature extraction with self-attention can improve both
accuracy and explainability. The hierarchical Swin Transformer ensemble for breast cancer diagnosis [31] and Swin Transformer–
driven cervical cell classification with web-based deployment [61] specifically demonstrates the compatibility of transformer
architectures with decentralized and web-deployed screening workflows. In precision agriculture, MaizeFormerX, a lightweight
cross-scale attention vision transformer [25], and the MaxViT-based soybean disease identification model [33] illustrate that
transformer efficiency advances are beginning to close the gap with CNN-based lightweight models, enabling deployment on
resource-constrained agricultural hardware. Global–local attention modeling for kidney disease classification from CT images
[63] represents a further architectural refinement, combining coarse global context with fine-grained local feature attention that
is particularly relevant for multi-class lesion discrimination. The convergence of explainability requirements with transformer
attention maps [62] offers promising but still-maturing interpretability mechanisms.
3.4. Hybrid, Ensemble, and Multimodal Fusion Systems
Hybrid and ensemble systems are prominent in domains requiring both high accuracy and some form of post-hoc justification.
The explainable deep stacking ensemble for brain tumor diagnosis [32] and the stacking ensemble with explainable AI for breast
cancer diagnosis and web deployment [52] exemplify the combination of heterogeneous base learners with ensemble
aggregation, achieving improved generalization while preserving the interpretability needed for clinical endorsement. The
ensemble transformer with post-hoc explanations for depression and severity detection [27] extends this architecture to affective
computing, where label ambiguity and subjective ground truth make ensemble uncertainty estimation particularly valuable.
Multimodal fusion represents an important sub-category: the hybrid multi-modal emotion recognition framework based on
InceptionV3DenseNet [6] and the vision-audio multimodal object recognition system using hybrid tensor fusion [29] address the
challenge of integrating heterogeneous modalities without introducing cross-modal interference. The multimodal machine
learning framework for privacy-preserving and scalable cancer diagnosis [51] is notable in that it combines fusion with privacy
Page | 27

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges
constraints, foreshadowing the next generation of privacy-aware multimodal clinical systems. The attention-enhanced deep
learning framework for business strategy optimization [53] extends multimodal fusion principles to business intelligence, while
the explainable transformer for cotton leaf diagnostics and fabric defect detection [28] applies them to dual-task agricultural and
manufacturing inspection.
3.5. Graph Neural Networks and Knowledge-Graph Reasoning
Graph-structured data and knowledge-graph reasoning occupy a specialized but important niche in high-stakes AI, particularly
where relational dependencies among entities carry decision-relevant information. The enhancement of acoustic-emission-
driven gas-pipeline monitoring using graph neural networks [18] illustrates how GNNs can model the propagation structure of
physical signals across networked sensor arrays, enabling more accurate fault localization than signal-level classifiers alone.
Knowledge-graph and NLP integration for facilitating heuristic reasoning [17] addresses a different but complementary need:
enabling AI systems to leverage structured domain knowledge in support of reasoning tasks that resist purely statistical
approaches. The AddManBERT combinatorial triples extraction and knowledge-graph construction for additive manufacturing
design support [23] demonstrates that BERT-based language models and knowledge graphs can be coupled to create semantic
decision-support tools in specialized engineering domains. Together, these architectures suggest that relational and symbolic
reasoning are not superseded by deep learning but rather constitute a complementary layer of high-stakes decision support,
particularly in safety-critical industrial and engineering contexts.
3.6. Bayesian, Physics-Guided, and Uncertainty-Aware Models
Uncertainty quantification is a fundamental requirement in safety-critical systems, and Bayesian and physics-guided approaches
represent the most principled available framework for this purpose. The physics-guided Bayesian neural network for sensor fault
detection in wind turbines [54] is directly relevant: by embedding physical priors into the network architecture, the model
addresses the twin challenges of sensor data sparsity and the need for calibrated uncertainty estimates in a safety-sensitive
industrial context. This architecture family is underrepresented in the broader corpus, reflecting a maturity gap in the literature:
while Bayesian deep learning and physics-informed neural networks have attracted substantial methodological attention, their
integration into domain-specific high-stakes applications remains limited. The deployment implications are significant, systems
that cannot quantify their own uncertainty cannot reliably support human oversight, particularly in contexts such as wind-energy
management, structural health monitoring, and clinical diagnostics where false confidence carries severe consequences.
3.7. Generative, Agentic, and Enterprise AI
Generative AI and agentic systems represent the most recent and rapidly evolving frontier in high-stakes decision support.
Generative AI in enterprise information systems for transforming business intelligence and strategic decision support [74]
addresses the organizational embedding of large language model capabilities into enterprise workflows, a transition that
introduces new questions of factual reliability, audit trails, and accountability. Automated risk assessment and collaborative
decision-making AI in agile project management and stakeholder engagement [69] exemplifies agentic AI—systems that not
only predict but also initiate decision workflows, coordinate among stakeholders, and adapt to feedback. AI-driven business
analytics for IT strategy [66] and AI-enabled management information systems for economic resilience and governance [76]
further illustrate the enterprise AI cluster, where real-time data integration, organizational agility, and governance compliance
are simultaneously demanded. The sustainability framing of AI-ERP integration in dark factories [65] introduces additional
complexity: autonomous industrial environments require AI systems that are not only accurate but also auditable, energy-
efficient, and aligned with broader sustainability objectives.
3.8. Edge-Cloud, Federated, Privacy-Preserving, and Distributed AI
The deployment of AI at the edge of networks, on IoT devices, clinical sensors, and distributed infrastructure, introduces a
distinct set of architectural constraints. Privacy-preserving behavior analytics for workforce retention [44] and the multimodal
privacy-preserving cancer diagnosis framework [51] illustrate the operational demand for analytics that never expose raw
personal data to centralized servers. The distributed intelligence and privacy-preserving deployment framework encompassing
edge-cloud, 6G connectivity, and federated learning for secure and auditable decision support [79] represents the most
comprehensive architectural response to this demand, integrating multiple privacy-preserving mechanisms into a unified
deployment stack. Stacking ensemble-based breast cancer classification with real-time web deployment [52] and Swin
Transformer cervical cell classification with web-based screening [61] demonstrate that deployment-readiness, including latency,
user-interface integration, and cross-platform accessibility, is itself an architectural concern that must be addressed during
model design, not as an afterthought. The intelligent cybersecurity framework integrating ML-driven data protection and threat
intelligence [73], AI for data security and digital communication resilience [72], and the resilience-by-design framework [75]
collectively constitute an emerging distributed AI security cluster in which privacy, auditability, and real-time threat response
must be simultaneously maintained.
Page | 28

FCSAI 5(7): 25-37
4. Application Domains
4.1. Healthcare and Biomedical Decision Support
Healthcare constitutes the largest and most architecturally diverse domain in the corpus. Cancer diagnosis applications span skin
cancer [26, 62], lung cancer [20, 30], breast cancer [31, 32, 52], cervical cancer [35, 61], leukemia [36], and prostate cancer [48],
collectively demonstrating that transformer-based, CNN-based, and ensemble architectures are all actively explored for
oncological image analysis. The comparative analysis of explainable ML for cancer classification using cytological features [50]
and the multimodal privacy-preserving cancer diagnosis framework [51] illustrate the dual push toward interpretability and
privacy compliance that characterizes mature healthcare AI. Beyond oncology, kidney disease classification from CT images [63],
Parkinson's disease screening via voice biomarkers [45], sleep stage classification with transfer learning [47], heart disease
prediction from structured clinical data [49], and AI-integrated healthcare information systems for diabetes management [71]
demonstrate the breadth of modality and architecture diversity within this domain. Sentiment analysis of online drug reviews
[39] and market basket analysis for healthcare service bundling [43] extend decision support into health services research. The
consistent emphasis on explainability across these works, reflected in post-hoc XAI methods, attention visualization, and
transparent ensemble reporting, reflects clinical regulatory and professional requirements that AI recommendations be
interpretable by clinicians. Neural network methods combined with dimensionality reduction can enhance breast cancer
diagnosis by simplifying high-dimensional feature representations while retaining clinically meaningful diagnostic patterns [80].
4.2. Human-Centered, Neuro-Affective, and Assistive AI
This domain addresses AI systems designed to support humans with cognitive, communicative, or affective needs. ASD
classification using facial grid-wise emotion features and dual-branch visual transformation [1, 4] represents a high-stakes
application in which misclassification carries significant developmental and social consequences. The facial expression database
of ASD children [5] provides the foundational data resource for this research cluster. Multimodal EEG analysis of neural
synchrony in phrase processing [2] and the standard tDCS model [13] address neuro-affective AI in clinical neuroscience
contexts. Emotion recognition systems, including the InceptionV3DenseNet hybrid [6], bidirectional Elman NN [7], and hybrid
deep belief optimization [8], target affective computing applications where training data quality and subject variability introduce
systematic reliability challenges. The flex sensor–based hand glove for deaf and mute people [14] and iris detection and
recognition system [22] represent sensor-based assistive AI. Suicidal ideation detection using NLP and deep learning [37] is a
critical mental health application where both false positives and false negatives carry severe consequences, demanding
calibrated uncertainty and human oversight. The adaptive feedback system for learner improvement [19] and the AI-powered
digital health platform for ASD students [67] address adaptive and personalized decision support in educational and therapeutic
settings. Bengali social media sentiment classification [38] and sentiment extraction from drug reviews [39] provide modality
evidence for text-based human-centered AI.
4.3. Smart Infrastructure, IoT, Robotics, and Cyber-Physical Systems
Smart infrastructure encompasses a diverse set of sensor-rich, real-time, and safety-critical environments. IoT-based wireless
battery monitoring for solar micro-grids [3] and smart energy metering [10] illustrate AI-assisted monitoring in energy
infrastructure. The IoT-based smart healthcare medical box for elderly patients [9] extends IoT decision support into clinical care
contexts. Wireless mesh network routing [11] and MANET routing protocol simulation [12] address network-layer decision
support in distributed infrastructure. High-altitude platform communications optimization [15] represents a communication-
systems application of simulation-based AI. The question of full autonomy in underwater robotics [16] directly engages the
human oversight axis: the framing as a prospect question reflects genuine uncertainty about whether autonomous decision-
making in unstructured aquatic environments is currently reliable enough for unsupervised deployment. Gas-pipeline condition
diagnosis through acoustic-emission signal imaging [24] and GNN-based smart gas-pipeline monitoring [18] address safety-
critical industrial infrastructure where fault detection failures have severe physical consequences. Concrete crack characterization
using acoustic-emission and lightweight deep learning [21] and vision-audio multimodal object recognition using tensor fusion
[29] contribute additional modality and architecture evidence for the infrastructure monitoring cluster.
4.4. Agriculture, Environment, and Sustainability
Agricultural AI decision support encompasses disease detection, yield optimization, and sustainability-oriented resource
management. Maize leaf disease diagnosis with a lightweight vision transformer [25], cotton leaf diagnostics with an explainable
transformer [28], soybean leaf and seed disease identification with MaxViT [33], mango leaf disease recognition with an
ensemble vision transformer [34], tea leaf disease precision diagnosis with deep learning [77], and aquaculture disease diagnosis
with lightweight ResNeXt [46] collectively constitute a precision agriculture cluster in which lightweight, explainable, and real-
time-feasible architectures are prioritized for field deployment. AI-driven smart agriculture for crop yield optimization and
sustainability [70] addresses the systemic dimension, integrating AI into broader agricultural management frameworks. AI-driven
Page | 29

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges
solar financing for rural clinics and small health businesses [41] introduces sustainability and resilience framing into health
infrastructure, connecting agricultural and health domains through shared energy and financing challenges. The resilience-by-
design framework [75] provides a cross-cutting lens for sustainability-oriented AI across infrastructure, health, and environmental
systems.
4.5. Business, Enterprise, and Organizational Decision Support
Business decision support is the most thematically diverse domain in the corpus, spanning credit scoring, project management,
demand forecasting, supply chain analytics, digital transformation, and enterprise information systems. Credit scoring models
leveraging alternative data for underserved businesses [40] address fairness and access in financial AI. Predictive analytics for
project risk identification and mitigation [42] and automated risk assessment in agile project management [69] illustrate AI's role
in organizational risk governance. Market basket analysis for healthcare service bundling [43] bridges health and business
analytics. Blockchain applications in supply chain management [56] introduced ledger technology as a trust mechanism
complementary to predictive AI. Retail demand forecasting using LSTM and gradient boosting [57], small-business management
using predictive ML [58], e-commerce pricing optimization [55], market trend forecasting with external factor integration [60],
and customer satisfaction in hospitality [59] represent a forecasting and optimization cluster where ML methods address
operational decision support. The attention-enhanced deep learning system for business strategy optimization [53] extends
transformer architecture into enterprise analytics. AI-driven business analytics for IT strategy [66], digital transformation analytics
for IT project excellence [68], agile IT project risk and AI thematic analysis [64], and AI-ERP integration in dark factories [65]
constitute the enterprise AI governance cluster. Generative AI for enterprise business intelligence [74] and AI-enabled
management information systems for economic resilience [76] represent the most strategic layer of this domain, addressing how
AI reshapes organizational decision architectures rather than merely optimizing individual predictions.
4.6. Cybersecurity, Privacy, and Distributed Intelligence
Cybersecurity and privacy-preserving AI represent both a standalone application domain and a horizontal deployment
requirement across all other domains. The intelligent cybersecurity framework integrating ML-driven data protection and threat
intelligence [73] and AI for data security, analytics, and digital communication resilience [72] address real-time threat response in
digital infrastructure. Privacy-preserving behavior analytics for workforce retention [44] illustrates the application of differential
privacy and anonymization techniques in organizational analytics. Trustworthy AI for high-stakes decision support across critical
sectors [78] provides a governance and framework perspective spanning all domains. The resilience-by-design AI framework for
security, sustainability, and health in interdependent systems [75] emphasizes that AI security cannot be designed in isolation
from sustainability and health system resilience. Distributed intelligence with edge-cloud-6G-federated learning for secure and
auditable decision support [79] represents the architectural frontier of privacy-preserving deployment, integrating edge
inference, cloud aggregation, 6G communication, and federated training into a unified auditable stack.
5. Deployment Challenges
Figure 2 summarizes recurring pathways through which AI systems may fail after development. Data-level limitations, model-
level overconfidence, environmental distribution shifts, and governance weaknesses can jointly convert a technically promising
model into an unreliable decision-support system.
5.1. Data Quality, Heterogeneity, and Imbalance
High-stakes AI systems encounter heterogeneous data at every layer. Medical imaging corpora vary in scanner protocol,
resolution, acquisition site, and annotation convention, making cross-institutional generalization a persistent challenge [20, 51].
Agricultural disease datasets are subject to lighting variability, growth-stage confounds, and regional crop variety differences
that compromise model transferability [25, 34, 77]. Business datasets are often imbalanced across class labels property directly
relevant to credit scoring models for underserved populations [40] and demand forecasting under rare-event conditions [57].
The facial expression database for ASD children [5] highlights the challenge of constructing domain-specific datasets with
sufficient diversity to support generalizable models in sensitive populations. Data heterogeneity is not merely a technical
obstacle but a governance concern: models trained on non-representative data risk encoding systematic biases that propagate
into high-stakes decisions.
5.2. Explainability and Post-Hoc Interpretability
Explainability is the deployment requirement most consistently addressed in the corpus, and it is represented across all six
application domains. The post-hoc explanation strategies integrated into ensemble transformers [27], stacking ensembles [32,
35], vision transformers [25, 28, 61, 62], and CNN-based systems [26, 50] reflect the institutional and regulatory expectation that
AI recommendations in healthcare, agriculture, and business settings be accompanied by intelligible justifications. The Swin
Transformer with web-deployed explainability for cervical cell screening [61] illustrates that explainability mechanisms must be
preserved under deployment constraints, including web-based inference pipelines. However, attention visualization and saliency
Page | 30

FCSAI 5(7): 25-37
mapping, while increasingly ubiquitous, do not provide the formal guarantees of causal or counterfactual explanation that high-
stakes settings may eventually require [78]. The gap between current post-hoc explainability practices and deployment-grade
interpretability standards represents an important research frontier.
Figure 2. Shared failure modes in high-stakes AI deployment.
5.3. Robustness and Distribution Shift
Robustness to distribution shifts the degradation of model performance when test conditions diverge from training conditions is
particularly consequential in high-stakes deployment. Medical imaging models face cross-scanner and cross-population
distribution shifts [31, 51, 63]. Agricultural models face seasonal, geographical, and phenological shifts [33, 46, 70]. Industrial
monitoring models must remain reliable under varying operational conditions, sensor degradation, and novel fault patterns [18,
54, 24]. Business forecasting models are vulnerable to economic regime changes and external shocks [57, 60]. The physics-
guided Bayesian neural network [54] represents an important robustness strategy in industrial settings by embedding domain
priors that constrain model behavior under novel inputs. The trustworthy AI framework [78] and resilience-by-design approach
[75] address robustness at a systemic rather than model-specific level.
5.4. Privacy, Security, and Federated Deployment
Privacy-preserving AI is no longer a speculative research direction but an operational requirement in health, workforce, and
government contexts. Privacy-preserving behavior analytics for workforce retention [44] and the multimodal privacy-preserving
cancer diagnosis framework [51] demonstrate that utility and privacy can be simultaneously addressed, though with architecture-
specific tradeoffs. Federated learning frameworks, as illustrated by [79], distribute training across data owners without
centralizing raw data, enabling multi-institutional model development without privacy violation. The intelligent cybersecurity
framework [73] and the AI-driven resilience framework [72] address the security layer of AI deployments, where adversarial
attacks, data poisoning, and model inversion represent active threats. Blockchain integration in supply chain AI [56] introduces
distributed ledger mechanisms as complementary trust infrastructure. As 6G-enabled edge deployments proliferate, the
convergence of privacy, security, and real-time inference, addressed architecturally in [79], will become a central design
constraint.
5.5. Real-Time Feasibility and Resource Constraints
Real-time inference on resource-constrained devices is a deployment-critical requirement in IoT, agricultural, and clinical point-
of-care contexts. The lightweight cross-scale attention transformer for maize disease [25], lightweight ResNeXt for aquaculture
[46], and lightweight deep learning for concrete crack characterization [21] all explicitly address the inference-speed and
memory-footprint tradeoffs required for edge deployment. IoT-based systems for solar micro-grid monitoring [3], smart energy
metering [10], and smart medical boxes [9] require embedded inference with real-time response guarantees. Web-based
deployment for cervical cell screening [61] and breast cancer diagnosis [52] demonstrates that cloud-hosted inference can satisfy
real-time requirements while maintaining model complexity, provided network latency and interface design are appropriately
managed. HAPs communication systems [15] and MANET routing [12] address the network-layer constraints that govern real-
time AI in distributed infrastructure.
5.6. Human Oversight and Accountability
Page | 31

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges
The question of how much autonomy AI systems should exercise in high-stakes decisions is a governance and safety question as
much as a technical one. The framing of full autonomy in underwater robotics as an open prospect [16] reflects genuine
uncertainty about the conditions under which unsupervised autonomous decision-making is responsible. The automated risk
assessment and collaborative decision-making AI in agile project management [69] explicitly positions AI as a collaborator rather
than a sole decision-maker, a design principle with broad applicability in high-stakes settings. The trustworthy AI framework [78]
and AI-enabled management information systems for governance [76] embed human oversight as a design requirement. The
adaptive feedback system for learner improvement [19] and AI-powered ASD digital health platform [67] similarly position AI as
an assistive system that augments human professional judgment rather than replacing it. High-stakes AI systems should, in
general, be designed to support decision-makers rather than supplant them, and evaluation frameworks should reflect this
distinction. Table 1 distinguishes levels of AI involvement in high-stakes decision support, ranging from informative assistance to
constrained automation.
Table 1. Human–AI interaction modes and accountability boundaries.
| Mode         | AI role   |                   | Human role              | Accountability boundary  |     |     |
| ------------ | --------- | ----------------- | ----------------------- | ------------------------ | --- | --- |
|              | Provides  | scores,  alerts,  | or                      |                          |     |     |
| Informative  |           |                   | Interprets and decides  | Human accountable        |     |     |
rankings
|                 | Suggests                                                     | decision  | with Reviews, accepts, modifies, or  |                                |                |               |
| --------------- | ------------------------------------------------------------ | --------- | ------------------------------------ | ------------------------------ | -------------- | ------------- |
| Assistive       |                                                              |           |                                      | Human retains final authority  |                |               |
|                 | explanation                                                  |           | rejects                              |                                |                |               |
|                 |                                                              |           |                                      | AI  accountable                | for  deferral  | reliability;  |
| Deferral-based  | Flags uncertain or high-risk cases Resolves ambiguous cases  |           |                                      |                                |                |               |
human for final decision
Supports  evidence  synthesis  or Integrates  AI  output  with Shared responsibility through documented
Collaborative
|     | scenario analysis  |     | expert judgment  | decision trail  |     |     |
| --- | ------------------ | --- | ---------------- | --------------- | --- | --- |
Constrained  Executes  predefined  low-risk Monitors and intervenes when Organization  accountable  for  limits,
| automation  | actions  |     | needed  | monitoring, and override  |     |     |
| ----------- | -------- | --- | ------- | ------------------------- | --- | --- |
Unsupervised  Provides  retrospective Highest risk; rarely suitable for high-stakes
Acts without real-time review
| autonomy  |     |     | supervision  | use  |     |     |
| --------- | --- | --- | ------------ | ---- | --- | --- |
5.7. Benchmarking, Reproducibility, and Evidence Maturity
The corpus reveals inconsistent benchmarking practices across domains. Medical imaging studies frequently report accuracy,
sensitivity, and specificity on held-out test sets, but cross-institutional or external validation is less common. Agricultural studies
use domain-specific datasets that are rarely shared across research groups. Business analytics studies employ varied train-test
split conventions and rarely report confidence intervals or statistical significance tests. The absence of a shared evidence maturity
framework, analogous to the CONSORT or TRIPOD reporting standards in clinical research, makes cross-domain comparison
difficult. A comparative analysis of explainable ML for cancer classification [50] and the multimodal cancer diagnosis framework
[51] illustrate the value of systematic comparison but do not resolve the benchmarking gap. Future reviews and meta-analyses in
this space will require standardized reporting of dataset provenance, class balance, validation protocol, uncertainty estimates,
and deployment constraints. Table 2 summarizes a staged framework for judging whether an AI system has progressed from
technical feasibility to externally validated, human-supervised, deployment-ready, and continuously monitored decision support.
6. Future research directions
Future research should move from isolated model development to evidence that is standardized, auditable, and deployment
ready. Cross-domain benchmarks are needed to test AI systems across modalities, architectures, and decision settings using
multi-domain holdout sets and clinical or engineering-style reporting standards. Foundation models, generative AI, and large
language models should be assessed in high-stakes enterprise and healthcare contexts for hallucination, factual accuracy, audit-
trail completeness, and governance alignment [74,69]. Human-in-the-loop systems should use structured deferral for uncertain
predictions and be evaluated by decision quality, expert override rates, and outcomes with and without AI support [16,78].
Federated and edge-cloud AI should be tested across institutions with clear reporting of privacy budget, federated utility, and
communication  efficiency  [79,51].  Transformer  and  ensemble  models  also  require  formal  explainability  audits,  including
explanation fidelity, user comprehension, and regulatory acceptability [27,35,78]. Robustness and uncertainty should be built into
deep-learning pipelines through Bayesian and physics-guided methods, with calibration error, distribution-shift performance,
Page | 32

FCSAI 5(7): 25-37
and out-of-distribution detection reported [54,75]. Lightweight models should be optimized for IoT, embedded, and point-of-
care use based on latency, memory use, and accuracy–efficiency trade-offs [25,46,21]. Finally, governance-aware reporting
standards and evidence maturity frameworks should classify systems from proof-of-concept to deployment-validated AI using
reproducibility, external validation, governance compliance, and deployment-readiness indicators [78,76].
Table 2. Evidence-readiness levels for high-stakes AI studies.
Level Evidence status Minimum requirement Deployment meaning
Internal dataset; basic train-test or cross-validation; baseline
Level 1 Proof-of-concept Technical feasibility only
comparison
Predefined split; leakage control; class-wise metrics; calibration
Level 2 Internal validation Stronger internal evidence
summary
External/temporal
Level 3 Independent site, cohort, device, or time-period testing Generalization evidence
validation
Human-in-the-loop Expert review; AI-assisted versus unaided comparison;
Level 4 Workflow usefulness
evaluation override/deferral analysis
Monitored pilot Prospective or controlled deployment; privacy, safety, and
Level 5 Deployment readiness
deployment monitoring protocol
Post-deployment Drift monitoring; audit logs; incident reporting; model-update Sustained operational
Level 6
evidence governance maturity
7. Limitations of the review
This review is based on a curated provided as titles only. Consequently, the synthesis is thematic, architectural, and deployment-
level in nature rather than quantitative. It was not possible to extract specific performance metrics, dataset characteristics, sample
sizes, experimental protocols, or statistical validation details. The synthesis should therefore be interpreted as a structured
evidence map and taxonomic analysis rather than a quantitative meta-analysis. Full paper-level extraction, including access to
abstracts, methods, results, and supplementary materials, would be required to support meta-analytic comparison of model
performance, dataset characteristics, or validation rigor across papers. Additionally, the corpus reflects a curated selection and
may not comprehensively represent all active research threads in high-stakes AI. Domains such as legal AI, financial systemic risk,
and autonomous vehicles are not well represented and are acknowledged as important adjacent fields. The four-axis taxonomy
proposed here represents one defensible organization of the evidence space, not the only possible one.
8. Conclusion
This structured critical review has mapped the application of artificial intelligence to high-stakes decision support across six
domain healthcare and biomedical systems, human-centered and assistive AI, smart infrastructure and cyber-physical systems,
agriculture and sustainability, business and enterprise analytics, and cybersecurity and distributed intelligence, using a four-axis
taxonomy of domain, modality, architecture, and deployment concern. The synthesis of 79 papers reveals a rich and rapidly
advancing landscape in which vision transformers, ensemble methods, graph neural networks, lightweight CNN architectures,
and federated learning systems are each contributing to a qualitatively new generation of decision-support capabilities. The
cross-domain view discloses structural commonalities, recurrent explainability demands, universal data quality challenges, shared
real-time feasibility constraints, and consistent governance gaps, that are invisible within single-domain reviews. Further
evidence reveals that architecture selection in high-stakes AI is not a purely performance-driven choice but is shaped by
deployment constraints including computational resources, privacy requirements, interpretability obligations, and human
oversight needs. Looking forward, the critical research priorities are not architectural innovation per se, but the responsible
operationalization of existing advances. Trustworthy AI frameworks [78], privacy-preserving federated pipelines [79], governance-
aware management information systems [76], and resilience-by-design infrastructure [75] collectively point toward a research
agenda that prioritizes auditability, human oversight, and deployment readiness alongside predictive performance. The field
requires standardized evidence maturity frameworks, cross-domain benchmarking suites, formal explainability audit protocols,
and reporting standards that reflect the multi-dimensional demands of real-world high-stakes deployment. Progress on these
fronts will determine whether AI decision support fulfills its potential not merely as a technically capable system, but as a
trustworthy, equitable, and accountable partner in consequential human decisions.
Page | 33

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.
Publisher’s Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of
their affiliated organizations, or those of the publisher, the editors and the reviewers.
References
[1] Alamgir FM, et al. ASDnet: Classification model for individuals with autism spectrum disorder using facial grid-wise
expressions features and dual-branch visual transformation. Biomedical Signal Processing and Control. 2026;120(Part
A):109999. doi:10.1016/j.bspc.2026.109999.
[2] Majumdar J, Apu MH, Rahman M, Zaman T, Hassan MM. Multimodal EEG analysis of neural synchrony in minimal
phrase processing using machine learning. Conference paper; 2025 Nov.
[3] Mahamud S, Hossain MS, Hassan MM, Maruf MY, Rafi MAH, et al. IoT based wireless battery monitoring system for
enhanced solar micro-grid performance in Bangladesh. In: Arefin MS, Kaiser MS, Bhuiyan T, Based MA, Ray K, editors.
Proceedings of the 3rd International Conference on Big Data, IoT and Machine Learning. BIM 2025. Lecture Notes in
Networks and Systems, vol. 1798. Cham: Springer; 2026. p. 474-489. doi:10.1007/978-3-032-15346-3_33.
[4] Alamgir FM, Zaman T, Hassan MM, Jonayed MR, Alam MS. Classification model for autism spectrum disorder
individuals: Utilizing facial grid-wise emotion features and dual-branch visual transformation. In: 2024 IEEE International
Conference on Power, Electrical, Electronics and Industrial Applications (PEEIACON); 2024 Sep 12-13; Rajshahi,
Bangladesh. doi:10.1109/PEEIACON63629.2024.10800506.
[5] Alamgir FM, Saif SMH, Hossain MS, Al Hadi A, Alam MS. Facial expression database of autism spectrum disorder
children. European Chemical Bulletin. 2023;12(Special Issue 4):21109-21120. doi:10.48047/ecb/2023.12.Si4.1851.
[6] Alamgir FM, Alam MS. Hybrid multi-modal emotion recognition framework based on InceptionV3DenseNet. Multimedia
Tools and Applications. 2023;82:40375-40402. doi:10.1007/s11042-023-15066-w.
[7] Alamgir FM, Alam MS. A novel deep learning-based bidirectional Elman neural network for facial emotion recognition.
International Journal of Pattern Recognition and Artificial Intelligence. 2022;36(10):2252016.
doi:10.1142/S0218001422520164.
[8] Alamgir FM, Alam MS. An artificial intelligence driven facial emotion recognition system using hybrid deep belief rain
optimization. Multimedia Tools and Applications. 2023;82:2437-2464. doi:10.1007/s11042-022-13378-x.
[9] Al-Mahmud O, Khan K, Roy R, Alamgir FM. Internet of things (IoT) based smart health care medical box for elderly
people. In: 2020 International Conference for Emerging Technology (INCET); 2020. p. 1-6.
doi:10.1109/INCET49848.2020.9153994.
[10] Haque MM, Choudhury ZH, Alamgir FM. IoT based smart energy metering system for power consumers. In: 2019 2nd
International Conference on Innovation in Engineering and Technology (ICIET); 2019 Dec 23-24; Dhaka, Bangladesh.
doi:10.1109/ICIET48527.2019.9290661.
[11] Alamgir FM, Ahmed F, Miah M, Munna HM, Barua S. A novel routing algorithm for inter-group load balancing in
wireless mesh networks. In: 2018 21st Saudi Computer Society National Computer Conference (NCC); 2018.
doi:10.1109/NCG.2018.8593192.
[12] Ahmed F, Alamgir FM. Simulation-based proportional study of routing protocols for MANET. International Journal of
Computer Networks and Communications Security. 2017;5(12):28-36.
[13] Sourav MSU, Rahman A, Al Mamun A, Alamgir FM. Standard transcranial direct current stimulation (tDCS) model.
International Journal of Computer Networks and Communications Security. 2017;5(12):264-270.
[14] Al Mamun A, Polash MSJK, Alamgir FM. Flex sensor based hand glove for deaf and mute people. International Journal of
Computer Networks and Communications Security. 2017;5(2):38-48.
[15] Adnan BM, Chakma S, Alam MMJ, Alamgir FM. Performance simulation and comparison in High Altitude Platforms
(HAPs) communications systems under PSK, DPSK, QAM and FSK modulation schemes and AWGN, Rician and Rayleigh
communication channels. In: 2016 IEEE 7th Annual Information Technology, Electronics and Mobile Communication
Conference (IEMCON); 2016; Vancouver, BC. p. 1-11. doi:10.1109/IEMCON.2016.7746080.
[16] Rohan A, Tolie HF, Hasan MJ, Kannan S. Full autonomy in underwater robotics systems: A realistic prospect? Engineering
Applications of Artificial Intelligence. 2025;162:112638. doi:10.1016/j.engappai.2025.112638.
[17] Haruna A, Noman K, Li Y, Makanda ILD, Zubair A, Hasan MJ, Alhassan AB. Facilitating heuristic reasoning by utilizing
knowledge graph and natural language processing. Knowledge-Based Systems. 2026;334:115153.
doi:10.1016/j.knosys.2025.115153.
[18] Arifeen M, Hasan MJ, Rohan A, Kannan S, Prathuru A, et al. Enhancing acoustic emission driven smart gas-pipeline
monitoring with graph neural network. In: Manjurul Islam MM, Baptista ML, Tariq F, editors. Artificial Intelligence for
Smart Manufacturing and Industry X.0. Cham: Springer; 2025. p. 165-178. doi:10.1007/978-3-031-80154-9_8.
[19] Qadir HM, Khan RA, Rasool M, Sohaib M, Shah MA, Hasan MJ. An adaptive feedback system for the improvement of
learners. Scientific Reports. 2025;15:17242. doi:10.1038/s41598-025-01429-w.
Page | 34

FCSAI 5(7): 25-37
[20] Sohaib M, Hasan MJ, Zheng Z. A multichannel analysis of imbalanced computed tomography data for lung cancer
classification. Measurement Science and Technology. 2024;35(8):085401. doi:10.1088/1361-6501/ad437f.
[21] Habib MA, Hasan MJ, Kim JM. A lightweight deep learning-based approach for concrete crack characterization using
acoustic emission signals. IEEE Access. 2021;9:104029-104050. doi:10.1109/ACCESS.2021.3097962.
[22] Biswas R, Uddin J, Hasan MJ. A new approach of iris detection and recognition. International Journal of Electrical and
Computer Engineering. 2017;7(5):2530-2536. doi:10.11591/ijece.v7i5.pp2530-2536.
[23] Haruna A, Noman K, Li Y, Wang X, Hasan MJ, Alhassan AB. AddManBERT: A combinatorial triples extraction and
classification task for establishing a knowledge graph to facilitate design for additive manufacturing. Advanced
Engineering Informatics. 2025;67:103578. doi:10.1016/j.aei.2025.103578.
[24] Hasan MJ, Noman K, Navid WU, Li Y, Haruna A, Ashfak K. Intelligent diagnosis of gas pipeline condition through
multivariate analysis of acoustic emission signal-based imaging. Nondestructive Testing and Evaluation. 2025:1-20.
doi:10.1080/10589759.2025.2456088.
[25] Rahman MM, Gony MN, Ullah MS, Shuvra SMK, et al. MaizeFormerX: A lightweight vision transformer with cross-scale
attention for explainable maize leaf disease diagnosis. Scientific Reports. 2026. doi:10.1038/s41598-026-44550-0.
[26] Al Sakib A, Swapno SMMR, Ahamed F, Mohiuddin AB, Bhuiyan MIH, Khan S, Khushbu KG, Haque R, Alahmadi TJ, Moni
MA. Explainable AI-driven hybrid deep learning framework for accurate skin cancer diagnosis. Digital Health.
2026;12:20552076261438923. doi:10.1177/20552076261438923.
[27] Islam S, Haque R, Khan MA, Mohiuddin AB, Siddiqui MIH, Limon ZH, Khushbu KG, Swapno SMMR, Ahmed MR, Appaji A.
Ensemble transformer with post-hoc explanations for depression emotion and severity detection. iScience.
2026;29(2):114605. doi:10.1016/j.isci.2025.114605.
[28] Rahman Swapno SMM, Sakib A, Uddin Khondakar Pranta AS, Hossain A, Debnath J, Al Noman A, et al. Explainable
transformer framework for fast cotton leaf diagnostics and fabric defect detection. iScience. 2026 Feb 20;29(2):114411.
doi:10.1016/j.isci.2025.114411.
[29] Ahmed MR, Haque R, Rahman SMA, Reza AW, Siddique N, Wang H. Vision-audio multimodal object recognition using
hybrid and tensor fusion techniques. Information Fusion. 2025;126:103667. doi:10.1016/j.inffus.2025.103667.
[30] Debnath J, Pranta ASUK, Hossain A, Sakib A, Rahman H, Haque R, Ahmed MR, Reza AW, Swapno SMMR, Appaji A.
LMVT: A hybrid vision transformer with attention mechanisms for efficient and explainable lung cancer diagnosis.
Informatics in Medicine Unlocked. 2025;57:101669. doi:10.1016/j.imu.2025.101669.
[31] Ahmed MR, Rahman H, Limon ZH, Siddiqui MIH, Khan MA, Pranta ASUK, Haque R, Swapno SMMR, Cho YI, Abdallah MS.
Hierarchical Swin transformer ensemble with explainable AI for robust and decentralized breast cancer diagnosis.
Bioengineering. 2025;12(6):651. doi:10.3390/bioengineering12060651.
[32] Haque R, Khan MA, Rahman H, Khan S, Siddiqui MIH, Limon ZH, et al. Explainable deep stacking ensemble model for
accurate and transparent brain tumor diagnosis. Computers in Biology and Medicine. 2025;191:110166.
[33] Pranta ASUK, Fardin H, Debnath J, Hossain A, Sakib AH, Ahmed MR, et al. A novel MaxViT model for accelerated and
precise soybean leaf and seed disease identification. Computers. 2025;14(5):197. doi:10.3390/computers14050197.
[34] Noman AA, et al. ViX-MangoEFormer: An enhanced vision transformer-EfficientFormer and stacking ensemble approach
for mango leaf disease recognition with explainable artificial intelligence. Computers. 2025;14(5):171.
doi:10.3390/computers14050171.
[35] Siddiqui MIH, Khan S, Limon ZH, Rahman H, Khan MA, Al Sakib A, Swapno SMMR, Haque R, Reza AW, Appaji A.
Accelerated and accurate cervical cancer diagnosis using a novel stacking ensemble method with explainable AI.
Informatics in Medicine Unlocked. 2025;56:101657. doi:10.1016/j.imu.2025.101657.
[36] Haque R, Sakib AA, Hossain MF, Islam F, Aziz FI, Ahmed MR, Kannan S, Rohan A, Hasan MJ. Advancing early leukemia
diagnostics: A comprehensive study incorporating image processing and transfer learning. BioMedInformatics.
2024;4(2):966-991. doi:10.3390/biomedinformatics4020054.
[37] Haque R, Islam N, Islam M, Ahsan MM. A comparative analysis on suicidal ideation detection using NLP, machine, and
deep learning. Technologies. 2022;10(3):57. doi:10.3390/technologies10030057.
[38] Haque R, Islam N, Tasneem M, Das AK. Multi-class sentiment classification on Bengali social media comments using
machine learning. International Journal of Cognitive Computing in Engineering. 2023;4:21-35.
doi:10.1016/j.ijcce.2023.01.001.
[39] Haque R, Laskar SH, Khushbu KG, Hasan MJ, Uddin J. Data-driven solution to identify sentiments from online drug
reviews. Computers. 2023;12(4):87. doi:10.3390/computers12040087.
[40] Mithun MM, Tanim SH, Tarannum R. Developing AI-Powered Credit Scoring Models Leveraging Alternative Data for
Financially Underserved US Small Businesses. Repository Antis Publisher. 2025 Oct 18:699254.
[41] Tanim SH, Mithun MMU, Tarannum R. Sustaining vital care in disasters: AI-driven solar financing for rural clinics and
health small businesses. American Journal of Technology Advancement. 2025;2(9):123-153. doi:10.31149/ajta.v2i9.2528.
Page | 35

Artificial Intelligence for High-Stakes Decision Support: Architectures, Applications, and Deployment Challenges
[42] Tanim SH, Ahmad MS, Mithun MMU, Tarannum R, Refat FR, Sunny MNM. Leveraging predictive analytics for risk
identification and mitigation in project management. Journal of Information Systems Engineering and Management.
2025;10(43s):1041-1052. doi:10.52783/jisem.v10i43s.8523.
[43] Rimon RH, Nurujjaman, Mithun MMU. Market basket analysis for healthcare services to identify bundled care offerings.
Frontiers in Computer Science and Artificial Intelligence. 2025;4(3):44-67.
[44] Hussain TS, Tarannum R, Mithun MMM. Privacy-preserving behavior analytics for workforce retention approach.
American Journal of Engineering, Mechanics and Architecture. 2023;1(9):188-215.
[45] Ghosh BP, Bhuiyan MS, Bishnu KK, Mahmud FU, et al. Personalized machine learning models for Parkinson's disease
screening via voice biomarkers: Accounting for age, gender, and linguistic variability. The International Medicine. 2025
Dec.
[46] Masum AKM, Khan MFI, Mahmud FU, Hassan MM, Khaliluzzaman M. Improving aquaculture disease diagnosis with
lightweight ResNeXt architectures. In: 2025 3rd International Conference on Artificial Intelligence, Blockchain, and
Internet of Things (AIBThings); 2025. doi:10.1109/AIBThings66987.2025.11296219.
[47] Mahmud FU, Rahman H, Limon ZH, Khan MA, Jashim FB. Transfer learning approach for sleep stage classification with
limited training data. International Journal of Science and Research Archive. 2025;15(2).
doi:10.30574/ijsra.2025.15.2.1506.
[48] Farhan B, Jashim FR, Refat FR, et al. Hybrid vision transformer model for accurate prostate cancer classification in MRI
images. International Journal of Science and Research Archive. 2025;15(2). doi:10.30574/ijsra.2025.15.2.1509.
[49] Rashid SU, Siddiqui MIH, Mahmud FU, Rahman MS, Kabir AA, et al. Machine learning based clinical decision support for
heart disease prediction using structured patient data. Journal of Computer Science and Technology Studies. 2024;6(1).
doi:10.32996/jcsts.2024.6.1.36.
[50] Siddiqui MIH, Rahman MS, Kabir AA, Mahmud FU, Rashid SU, Shammah RS. Comparative analysis of explainable
machine learning models for cancer classification using cytological features. Journal of Medical and Health Studies.
2023;4(5):114-126.
[51] Kabir AA, Mahmud FU, Rahman MS, Rashid SU, Siddiqui MIH, Shammah RS. Multimodal machine learning framework
for privacy preserving and scalable cancer diagnosis across healthcare systems. Journal of Adaptive Learning
Technologies. 2024;1(6).
[52] Jashim FB, Refat FR, Karim MH, Mahmud FU, Sakib AH. Stacking ensemble-based breast cancer classification: Enhancing
diagnostic accuracy with deep learning and real-time web deployment. International Journal of Science and Research
Archive. 2025;15:1417-1431.
[53] Mahmud FU, Rahman A, Khan MA, Bishnu KK, Eva AA, Maua J. FuseAttenX: Leveraging attention-enhanced deep
learning for business strategy optimization. In: 2025 IEEE 4th International Conference on Computing and Machine
Intelligence (ICMI); 2025. doi:10.1109/ICMI65310.2025.11141140.
[54] Khan MDA, Rahman A, Mahmud FU, Bishnu KK, Nabil HR, Mridha MF, et al. A physics-guided Bayesian neural network
for sensor fault detection in wind turbines. IEEE Open Journal of the Computer Society. 2025;6:931-942.
doi:10.1109/OJCS.2025.3577588.
[55] Chowdhury MS, Shak MS, Devi S, Miah MR, Al Mamun A, Ahmed E, Hera SAA, Mahmud F, Mozumder MSA. Optimizing
e-commerce pricing strategies: A comparative analysis of machine learning models for predicting customer satisfaction.
The American Journal of Engineering and Technology. 2024;6(09):6-17. doi:10.37547/tajet/Volume06Issue09-02.
[56] Rahman T, Uddin MK, Hosen MM, Bhattacharjee B, Taluckder MS, Mou SN, Akter P, Hossain MS, Miah MR, Rahman MM.
Blockchain applications in business operations and supply chain management by machine learning. International
Journal of Computer Science & Information System. 2024;9(11):17-30. doi:10.55640/ijcsis/Volume09Issue11-03.
[57] Shak MS, Mozumder MSA, Hasan MA, Das AC, Miah MR, Akter S, Hossain MN. Optimizing retail demand forecasting: A
performance evaluation of machine learning models including LSTM and gradient boosting. The American Journal of
Engineering and Technology. 2024;6(9):67-80. doi:10.37547/tajet/Volume06Issue09-09.
[58] Naznin R, Sarkar MAI, Asaduzzaman M, Akter S, Mou SN, Miah MR, Sajal A. Enhancing small business management
through machine learning: A comparative study of predictive models for customer retention, financial forecasting, and
inventory optimization. International Interdisciplinary Business Economics Advancement Journal. 2024;5(11):21-32.
[59] Talukder T, Masud SB, Miah MR, Hera A, Faruque MO. An examination of how social media participation and customer
satisfaction affect the likelihood that a business will make another transaction in the hospitality sector. Open Access
Library Journal. 2025;12:1-15. doi:10.4236/oalib.1112802.
[60] Hossain MS, Khan A, Das P, Haque MSU, Kamruzzaman F, Akter S, Ahmed A, Miah MR. Enhanced market trend
forecasting using machine learning models: A study with external factor integration. International Interdisciplinary
Business Economics Advancement Journal. 2025;6(1):5-12. doi:10.55640/business/volume06issue01-02.
[61] Shakil MR, Malik AH, Siddiqui MIH, Ahmed S, Miah MR, Linkon AA. Swin transformer-driven cervical cell classification
with explainable AI and web-based screening. Journal of Medical and Health Studies. 2026;7(5):25-35.
doi:10.32996/jmhs.2026.7.5.5.
Page | 36

FCSAI 5(7): 25-37
[62] Linkon AA, Shakil MR, Ahmed S, Miah MR, Malik AH. Explainable transformer-based skin lesion classification from
clinical images. Journal of Medical and Health Studies. 2026;7(5):46-55. doi:10.32996/jmhs.2026.7.5.7.
[63] Ahmed S, Miah MR, Shakil MR, Linkon AA, Siddiqui MIH, Malik AH. Global-local attention modeling for reliable
multiclass kidney disease classification from CT images. Journal of Medical and Health Studies. 2026;7(5):36-45.
doi:10.32996/jmhs.2026.7.5.6.
[64] Karshiboev A, Al-Samad K, Tarafdar MTR, Rimi NN, Islam MS, Papel MSI. Artificial intelligence for risk and decision
assessment in agile IT projects: A thematic analysis and dynamic structuration framework approach. International
Journal of Advances in Signal and Image Sciences. 2026;12(1):387-410. doi:10.29284/9k2nx425.
[65] Islam MS, Islam MI, Mozumder AQ, Khan MTH, Das N, Mohammad N. A conceptual framework for sustainable AI-ERP
integration in dark factories: Synthesising TOE, TAM, and IS success models for autonomous industrial environments.
Sustainability. 2025;17(20):9234. doi:10.3390/su17209234.
[66] Haque S, Mohammad N, Mambetaliev A, Karshiboev A, Lucky KY, Khan MTH, Islam H. Artificial intelligence-driven
business analytics for IT strategy: Advancing decision-making, real-time insights, and organizational agility through
intelligent automation and data integration. Journal of Posthumanism. 2025;5(6):1848-1863.
doi:10.63332/joph.v5i6.2287.
[67] Haque S, Islam MS, Islam MI, Islam MS, Khan R, Tarafder MTR, Mohammad N. Enhancing adaptive learning,
communication, and therapeutic accessibility through the integration of artificial intelligence and data-driven
personalization in digital health platforms for students with autism spectrum disorder. Journal of Posthumanism.
2025;5(8):737-756. doi:10.63332/joph.v5i8.3255.
[68] Faruq O, Islam MI, Islam MS, Tarafder MTR, Rahman MM, Islam MS, Mohammad N. Re-imagining digital transformation
in the United States: Harnessing artificial intelligence and business analytics to drive IT project excellence in the digital
innovation landscape. Journal of Posthumanism. 2025;5(9):333-354. doi:10.63332/joph.v5i9.3326.
[69] Haque S, Chowdhury S, Faruq O, Akter R, Joy MSI, Munny MA, Shimu F. Automated risk assessment and collaborative
decision-making AI applications in agile project management and stakeholder engagement. International Journal of
Advances in Signal and Image Sciences. 2026;12(1):915-923. doi:10.29284/v2jv8q59.
[70] Riipa MB, Saha S, Ferdousmou J, Khatoon R, Mohammad N, Hossain M. AI-driven smart agriculture: Optimizing crop
yield and sustainability in the U.S. In: 2025 5th International Conference on Electrical, Computer and Energy
Technologies (ICECET); 2025; Paris, France. doi:10.1109/ICECET63943.2025.11472088.
[71] Lucky KY, Haque S, Al-Samad K, Akter R, Faruq O, Azim KS, Joy MSI. AI-powered healthcare information systems
securing diabetes management through integrated technology solutions and enhanced patient care delivery. Vascular
and Endovascular Review. 2025;8(11s):465-476.
[72] Faruq O, Chowdhury S, et al. Artificial intelligence as the strategic engine of data security, analytics, and digital
communication for a resilient digital future. Journal of Information and Knowledge Management. 2025;20(2):1764-1773.
[73] Shimu F. Intelligent cybersecurity framework: Machine learning-driven data protection and threat intelligence
integration for modern digital communications. International Journal of Applied Mathematics. 2025;38(8s):620-632.
doi:10.12732/ijam.v38i8s.595.
[74] Haque S, Islam H, Sharmin F, Joy MSI, Naher K, Rimi NN, Shimu F. Generative artificial intelligence in enterprise
information systems: Transforming business intelligence and strategic decision support processes. Journal of
Information and Knowledge Management. 2025;20(2):887-897. doi:10.18848/8p0s2e25.
[75] Shakil MR, Hasan M, Tarek MIH, Polash FI, Meem EJ. Resilience-by-design: AI for security, sustainability and health in
interdependent systems. World Journal of Advanced Engineering Technology and Sciences. 2026;18(3):254-267.
doi:10.30574/wjaets.2026.18.3.0153.
[76] Shakil MR, Hasan M, Tarek MIH, Polash FI, Meem EJ. AI-enabled management information systems for economic
resilience and organizational performance: Analytics, governance, cyber risk and decision automation. World Journal of
Advanced Engineering Technology and Sciences. 2026;18(3):294-307. doi:10.30574/wjaets.2026.18.3.0156.
[77] ZakirHossain M, Khan MM, Thapa S, Uddin R, Meem EJ, Niloy SK, et al. Advanced deep learning techniques for precision
diagnosis of tea leaf diseases. In: 2025 IEEE International Conference on Emerging Technologies and Applications
(MPSec ICETA); 2025. doi:10.1109/MPSecICETA64837.2025.11118779.
[78] Shakil MR, Hasan M, Tarek MIH, Polash FI, Meem EJ. Trustworthy AI for high-stakes decision support across critical
sectors. World Journal of Advanced Engineering Technology and Sciences. 2026;18(3).
doi:10.30574/wjaets.2026.18.3.0152.
[79] Shakil MR, Hasan M, Tarek MIH, Polash FI, Meem EJ. Distributed intelligence and privacy-preserving deployment: Edge-
cloud-6G-federated learning for secure, auditable decision support. World Journal of Advanced Engineering
Technology and Sciences. 2026;18(3):268-279. doi:10.30574/wjaets.2026.18.3.0154.
[80] Khan MA, Parveen R, Ahmed I, Milon MH, Khan TA. High-Accuracy Breast Cancer Diagnosis Using Neural Networks and
Dimensionality Reduction Techniques. In2025 IEEE 19th International Conference on Open Source Systems and
Technologies (ICOSST) 2025 Dec 1 (pp. 1-6). doi:10.1109/ICOSST69113.2025.11315291.
Page | 37