---
conversion_metadata:
  converted_at: "2026-07-21T13:41:24Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Karst et al.pdf"
  source_pdf_sha256: "cd4628bbfe870d0474cadaf5891bcaf9019000d5c6de414b2bcad13f360d5fc2"
  page_count: 28
  markdown_char_count: 290699
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Electronic Markets (2025) 35:7 
https://doi.org/10.1007/s12525-024-00746-8

RESEARCH PAPER

SynDEc: A Synthetic Data Ecosystem

Fabian Sven Karst1

· Mahei Manhai Li1,2 · Jan Marco Leimeister1,2

Received: 22 March 2024 / Accepted: 2 December 2024 / Published online: 25 January 2025 
© The Author(s) 2025

Abstract
Given the critical role of data availability for growth and innovation in financial services, especially small and mid-sized 
banks lack the data volumes required to fully leverage AI advancements for enhancing fraud detection, operational effi-
ciency, and risk management. With existing solutions facing challenges in scalability, inconsistent standards, and complex 
privacy regulations, we introduce a synthetic data sharing ecosystem (SynDEc) using generative AI. Employing design 
science research in collaboration with two banks, among them UnionBank of the Philippines, we developed and validated 
a synthetic data sharing ecosystem for financial institutions. The derived design principles highlight synthetic data setup, 
training configurations, and incentivization. Furthermore, our findings show that smaller banks benefit most from SynDEcs 
and our solution is viable even with limited participation. Thus, we advance data ecosystem design knowledge, show its 
viability for financial services, and offer practical guidance for privacy-resilient synthetic data sharing, laying groundwork 
for future applications of SynDEcs.

Keywords  Synthetic data · Data sharing platform · Data ecosystem · Financial services · Data scarcity

JEL classification  M15

Motivation

In the wake of recent global crises, the enhancement of 
financial services has become a crucial driver for accelerat-
ing economic recovery, particularly in developing economies 
where these services are essential for expanding financial 
inclusion and fostering socioeconomic growth (Demirgüç-
Kunt et al., 2022; Pazarbasioglu et al., 2020; White et al.,

Responsible Editor: Gero Strobel

*  Fabian Sven Karst

Fabian.Karst@unisg.ch

Mahei Manhai Li 
  Mahei.Li@unisg.ch; Mahei.Li@uni-kassel.de

Jan Marco Leimeister 
JanMarco.Leimeister@unisg.ch; Leimeister@uni-kassel.de

1  University of St.Gallen, Institute of Information Systems 
and Digital Business, Dufourstrasse 50, 9000 St.Gallen, 
Switzerland

2  University of Kassel, Information Systems, Pfannkuchstraße

1, 34121 Kassel, Germany

2021). However, given the financial services industry’s reli-
ance on information, increasing data availability is key to 
success. This is especially true for smaller financial institu-
tions, which lack the necessary volume of high-quality data 
to leverage current AI model advancements. This lack of 
data results in missed opportunities, with developing coun-
tries potentially losing out on up to 5% of GDP through 
improvements in fraud protection, operational efficiency, and 
workforce allocation (White et al., 2021; Zachariadis, 2020).
Although the sharing of financial transaction data could 
reduce risks and improve transparency (Brodsky & Oakes, 
2017), thereby driving economic growth (O’Leary et al., 
2021), it faces significant obstacles related to privacy regu-
lation and information security. Existing solutions such as 
open banking and federated learning have significant limita-
tions. Open banking, which enables customer-approved data 
exchange between financial institutions, often produces unre-
liable data due to selective participation (He et al., 2023) and 
lacks coverage of B2B transactions (Preziuso et al., 2023). 
Federated learning, an approach for training a model with-
out direct data exchange, faces scalability issues, restricts

---

<!-- PAGE 2 -->

7  Page 2 of 28

Electronic Markets (2025) 35:7

participants to a single shared model, and lacks adaptability 
(Baabdullah et al., 2024; Chatterjee et al., 2024). Therefore, 
research is required to explore data ecosystems that facilitate 
the exchange of data between financial institutions and regu-
latory bodies while safeguarding the privacy of individual 
users’ information (Assefa, 2020).

In the pursuit of establishing such an ecosystem enabling 
financial data sharing, the application of synthetic data gen-
eration emerges as a promising solution. Synthetic data, 
currently primarily used in financial services to tackle class 
imbalance in fraud detection models by synthesizing new 
fraudulent samples (Charitou et al., 2021), produces artificial 
data that if done correctly maintains privacy while capturing 
and generalizing the patterns and attributes essential for the 
training of machine learning models. Combining this with 
data sharing enables the creation of a secure and robust data 
ecosystem.

While plenty of research on synthetic data generation 
exists, significant gaps remain for its practical application 
within data ecosystems. Research has largely focused on 
algorithm development, leaving critical questions unan-
swered about how to design an ecosystem for privacy-pre-
serving data exchange with the capability to handle complex 
data and achieve interoperability across institutions (Oliveira 
et  al.,  2019).  Additionally,  there  is  limited  guidance  on 
which algorithms are most effective in a context where syn-
thetic data is leveraged to be shared between institutions 
and not merely used to increase the amount of training data 
(Langevin et al., 2022). Practical strategies for integrating 
shared synthetic data within machine learning models are 
also sparse, though such strategies are essential for realiz-
ing synthetic data’s potential in AI applications (Sattarov 
et al., 2023; Strelcenia & Prakoonwit, 2023). Finally, incen-
tives, for big as well as small players, necessary to encour-
age  participation  in  a  synthetic  data-sharing  ecosystem 
remain underexplored, despite being vital for fostering the 
cooperative engagement on which such ecosystems depend 
(Gelhaar & Otto, 2020). In response, our research seeks to 
answer the following questions: What architecture is best 
suited for secure data exchange? Which algorithms are most 
effective for data generation? What are the optimal strategies 
for utilizing shared synthetic data within individual insti-
tutions? And do the incentives within such an ecosystem 
effectively encourage participation? Furthermore, there is a 
need for specialized engineering and management method-
ologies tailored to the unique demands of financial services, 
where stringent privacy regulations and the complex nature 
of transaction data introduce distinct challenges (Oliveira 
et al., 2019).

Our research goal is to provide design knowledge for a 
synthetic data ecosystem that enables financial institutions 
to share financial transaction data and generate utility from 
doing so. Our study contributes to the existing literature in

two significant ways. First, it advances the field of data eco-
systems by addressing privacy challenges and exploring the 
use of data from multiple institutions for machine learning 
(Brée et al., 2024). Second, it offers practical guidance for 
financial institutions on generating and utilizing synthetic 
data, including benchmarking different algorithms, setups, 
and training schemes. Given the current lack of guidance on 
the conceptualization and implementation of such systems, 
this leads us to the following research question:

RQ: How to design a financial data ecosystem (SynDEc) 
based on synthetic data sharing?

To  address  the  RQ,  the  paper  adopts  a  multifaceted 
approach to investigate architectural design decisions. It 
encompasses an examination of synthetic data generation 
techniques within the ecosystem, explores its implications 
for training predictive models, and seeks to identify and mit-
igate potential challenges to the ecosystem’s stability and 
functionality. Additionally, it assesses the generalizability 
of the derived principles beyond the domain of financial 
fraud detection.

The paper is organized as follows: In the next section, 
we present an overview of data ecosystems in financial ser-
vices and synthetic data generation. Next, we outline, the 
Design Science Research Methodology by Peffers et al. 
(2007), combining context-driven innovation and iterative 
development, which we use as our methodological founda-
tion. In the first of our four design cycles, we diagnose the 
problem space through the meta (MR) and design require-
ments (DR) based on both literature and expert interviews. 
Based on this, our initial set of design principles (DP) is 
derived and instantiated as a system architecture. Building 
on this the second design cycle evaluates the feasibility of 
different synthetic data generation and integration methods. 
The following design cycle extends this by evaluating the 
proposed approach in new domains while also investigating 
improvements to the ecosystem based on data generation and 
exchange. Lastly, design cycle four takes a network view, 
investigating design elements to ensure early challenges fre-
quently seen in data ecosystems can be overcome. Finally, 
we discuss the findings, outline limitations, provide a per-
spective for future work, and conclude with a brief summary.

Related work

Data ecosystems in financial services

The growing recognition of data as a critical asset for inno-
vation, growth, and value creation has led firms to increas-
ingly seek external sources to enhance their data capabilities 
(Bagad et al., 2021; Gelhaar & Otto, 2020). One promising

---

<!-- PAGE 3 -->

Electronic Markets (2025) 35:7

Page 3 of 28  7

approach is the formation of inter-organizational networks, 
where  organizations  collaborate  to  share  resources  and 
knowledge (Gray & Sites, 2013). Within this context, data 
ecosystems have emerged as an effective framework for data 
exchange (Abbas et al., 2021; Heinz et al., 2022; Zuiderwijk 
et al., 2014). Defined as “a set of networks composed of 
autonomous actors that directly or indirectly consume, pro-
duce, or provide data and other related resources” (Oliveira 
& Lóscio, 2018, p. 4), data ecosystems are built around four 
key constructs: (1) actors, (2) their roles, (3) relationships 
among them, and (4) the resources they require. Actors in 
these ecosystems—whether organizations, individuals, or 
institutions—take on roles such as data consumers, provid-
ers, and intermediaries, each contributing uniquely to the 
ecosystem's function (Oliveira & Lóscio, 2018; van Schalk-
wyk et al., 2016). The roles they assume drive specific tasks, 
such as data intermediaries connecting various actors and 
data consumers analyzing and providing feedback to data 
providers. These interactions, and the dependencies that 
arise from them, form the relationships that underpin the 
ecosystem (Heimstädt et al., 2014; Oliveira & Lóscio, 2018). 
At the core of a data ecosystem, data platforms provide the 
technical infrastructure for processing and managing data 
from diverse sources, enabling various data applications. 
These platforms often incorporate data marketplaces, which 
serve as self-service platforms that connect data producers 
and consumers (Gröger, 2021). Another closely related con-
cept is data spaces, which are frequently used to describe 
data-sharing ecosystems across organizations and thus will 
be used as synonyms in this paper (Otto et al., 2019).

Building on this foundation, recent research has shifted 
its focus to the governance and operationalization of data 
ecosystems, particularly in the areas of data sovereignty 
(Jarke, 2017) and trust (Gelhaar & Otto, 2020; Schäfer et al., 
2023), which are critical for ensuring secure and reliable 
data exchange. However, in their comprehensive review of 
data ecosystems, Brée et al. (2024) identified several gaps 
within the literature that are currently under-researched, 
among them data security and the integration of artificial 
intelligence and machine learning within data ecosystems. 
On the one hand, data security deals with ways data can 
be stored and shared within data ecosystems while remain-
ing protected as well as the influence of such measures on 
the utility of data ecosystems (Brée et al., 2024). On the 
other hand, machine learning and artificial intelligence have 
become central to the formation of data ecosystems, yet there 
is a need for a deeper understanding of the requirements for 
sharing AI training data and how training on shared data 
should be conducted (Brée et al., 2024). Our research seeks 
to address these challenges by proposing a new type of data 
ecosystem centered on synthetic data, which offers a means 
to mitigate privacy risks while maintaining the benefits 
of data sharing. Additionally, we investigate strategies for

maximizing the utility of shared data to enhance individual 
organizational performance, thereby contributing to both the 
theoretical and practical development of data ecosystems.

With current research on data ecosystems, predominantly 
concentrating on applications within healthcare, Industry 
4.0, and smart cities (Cappiello et al., 2020), this study 
tries to extend this focus to the financial services industry. 
Given the sector’s significant dependence on highly sensitive 
data and its advanced application of machine learning tech-
nologies, this context provides a suitable setting to address 
previously identified research gaps in data security and the 
implementation of AI models within data ecosystems. Cur-
rent research on data ecosystems within the financial ser-
vices industry can be broadly categorized into two research 
streams. The first stream centers on open banking, a cus-
tomer-focused ecosystem where established standards facili-
tate the secure sharing of banking data with various actors 
within the financial services ecosystem, based on customer 
requests (Cosma et al., 2023). While this approach grants 
consumers  greater  control  over  their  data,  it  also  raises 
significant data security concerns due to the decentralized 
nature of data storage across multiple providers—a critical 
issue given the heightened sensitivity of financial transaction 
data (Y. Wang et al., 2018). Furthermore, open banking does 
not provide institutions with an efficient and secure mecha-
nism for large-scale data exchange, which is essential for 
applications such as fraud detection and anti-money launder-
ing (Asrow, 2021). The second stream of research revolves 
around federated learning, a methodology that completely 
eliminates data sharing by enabling distributed training of 
shared models, thereby ensuring compliance with privacy 
protection regulations (Awosika et al., 2024; Lei et al., 2023; 
Perez et al., 2023). However, federated learning presents 
significant challenges, including computational overhead, 
scalability issues, and still privacy risks, as malicious actors 
might be able to infer sensitive data from the model param-
eters shared during the training process (Baabdullah et al., 
2024; Chatterjee et al., 2024). Additionally, the necessity 
for participants in a federated learning ecosystem to agree 
on a single model architecture, which is difficult to modify 
once established, further complicates its implementation. 
The constraints of existing solutions, coupled with the fact 
that data ecosystems do not emerge organically but instead 
necessitate strategic planning around a shared value proposi-
tion, have resulted in the lack of a comprehensive financial 
data ecosystem to date (Adner, 2017; Immonen et al., 2014). 
This is aggravated by a research gap in the development 
of specialized engineering and management methodologies 
tailored to the needs of such an ecosystem (Oliveira et al., 
2019) which are especially critical in the financial services 
sector, where stringent privacy requirements and the com-
plex nature of financial transaction data introduce distinct 
challenges. Consequently, further research is essential to

---

<!-- PAGE 4 -->

7  Page 4 of 28

Electronic Markets (2025) 35:7

address these challenges and to delineate the architectural 
frameworks necessary for the creation of robust and secure 
data ecosystems within the financial industry.

Synthetic data generation and its application

Synthetic data can be defined as “data that has been gener-
ated using a purpose-built mathematical model or algorithm, 
with the aim of solving a (set of) data science task(s)” (Jor-
don et al., 2022, p. 5). This generation process can take many 
forms as comprehensively categorized by Bauer et al. (2024) 
into  20  distinct  method  types.  Among  these,  generative 
adversarial networks (GANs) are the most popular. GANs 
learn by pitting a generator (synthesizes data from random 
noise) and a discriminator (classifies samples as real or fake) 
against each other, resulting in two highly skilled networks 
(Goodfellow et al., 2014). This architecture is highly adapt-
able, as discriminator and generator can be easily adjusted to 
new tasks (e.g., time series or graph generation) while being 
frequently the best-performing synthetic data generation 
method (Bauer et al., 2024). Another commonly employed 
synthetic  data  generation  method  is  autoencoder-based 
architectures,  especially  variational  autoencoder  (VAE) 
(Kingma & Welling, 2013). VAEs are trained by mapping 
an input sample to a hidden representation, which is then 
mapped back to the original vector, thus creating a model 
that synthesizes valid data from a lower dimensional rep-
resentation. This decoder model is then used to generate 
data from random noise which makes it especially useful for 
learning from data with disentangled features (Bauer et al., 
2024). Third, recurrent neural networks, feedforward neural 
networks which include recurrent edges, are able to generate 
sequential data of arbitrary length. This makes them ideal for 
sequence generation tasks such as speech synthesis, music, 
and time series generation (Lipton et al., 2015). Finally, vir-
tual environments are computer simulations in which algo-
rithms interact with each other based on predefined rules, 
generating synthetic data in the process (Bonabeau, 2002).
In the context of machine learning, synthetic data is pri-
marily utilized in three key areas: (i) private data release, (ii) 
data de-biasing and fairness, and (iii) data augmentation for 
robustness (Jordon et al., 2022). As the focus of this paper 
is employing synthetic data for private data release, it will 
be investigated in more detail. Hereby, private data release 
describes the case where synthetic data is used to mitigate 
disclosure risk, allowing privacy concerns and regulatory 
issues to be circumvented by substituting real data with syn-
thetic data (Esteban et al., 2017; Jordon et al., 2018). How-
ever, this comes with certain risks of disclosure, which users 
need to be aware of. While multiple risks exist, the most 
relevant is membership inference which seeks to determine 
if an individual was part of the original dataset (Bun et al., 
2021; Jordon et al., 2022). This risk is particularly critical in

the context of financial transaction data, as revealing a user’s 
membership in a specific bank’s dataset could enable mali-
cious actors to carry out more targeted fraudulent activities, 
making fraud prevention more difficult. Research on dealing 
with membership inference risks in synthetic data, primarily 
drawn from the healthcare domain, can be divided into two 
major streams. The first stream focuses on achieving guaran-
teed privacy by modifying models to conform to differential 
privacy principles, ensuring both the data and the model are 
protected. Algorithms implementing this are the PATE-GAN 
(Jordon et al., 2018) or DP2-VAE (Jiang et al., 2022) archi-
tectures. The second research stream focuses on evaluating 
and managing privacy risks within acceptable limits for a 
given volume of published synthetic data, providing various 
metrics and thresholds for guidance (H. Chen et al., 2023; 
Yan et al., 2022). Popular measures are the nearest neighbor 
adversarial accuracy risk (Yale et al., 2020), the member-
ship inference risk (Choi et al., 2018), and the meaningful 
identity disclosure risk (Emam et al., 2020). Furthermore, 
these measures have also been adopted by regulators such as 
the European Medicines Agency and Health Canada which 
both provide thresholds for identifying disclosure risk (Yan 
et al., 2022).

As the complexity of models continues to grow, neces-
sitating larger datasets, synthetic data has been applied in a 
variety of fields, where it is used to facilitate more efficient 
and effective development of AI solutions (Lu et al., 2023). 
In financial services, these have been mainly use cases that 
inhibit a strong class imbalance such as anti-money laun-
dering and financial fraud detection. Here, synthetic data 
generation is used to increase the amount of data within the 
minority class, thereby increasing training efficiency (E. Alt-
man et al., 2024; Hilal et al., 2022). The current landscape 
is largely dominated by GAN-based architectures especially 
Wasserstein GANs due to their superior training stability 
(Hilal et al., 2022; Sethia et al., 2018; Strelcenia & Pra-
koonwit, 2023). However, recent advancements have seen 
transformer-based architectures (Nickerson et al., 2023) and 
diffusion-based models (Sattarov et al., 2023) emerging as 
competitive alternatives to GANs. Due to the internal usage 
of this synthetic data, data privacy has not been a main con-
sideration when building these models. Data privacy consid-
erations have mostly been explored in academic studies that 
aim to make their synthetic data publicly available. These 
studies typically employ virtual environment-based systems, 
such as multi-agent simulations, which simulate financial 
transaction data by modeling interactions between known 
actors and behaviors (E. Altman et al., 2024; Jensen et al., 
2023; Lopez-Rojas et al., 2016). While these approaches 
are very secure from a privacy perspective as real data is 
only used during model evaluation of the synthetic data, 
they require significant manual work to identify patterns and 
changing behaviors need to be detected first, before they can

---

<!-- PAGE 5 -->

Electronic Markets (2025) 35:7

Page 5 of 28  7

be integrated into the simulation (Bauer et al., 2024). How-
ever, the automatic generation and sharing of synthetic data 
derived from real data have not been extensively explored. 
As privacy concerns intensify due to regulatory pressure 
and customer expectations, as well as a growing necessity 
for extensive datasets to support cutting-edge machine learn-
ing models (Hittmeir et al., 2019), employing synthetic data 
has the potential to address privacy challenges in data eco-
systems. Recent studies by Sattarov et al. (2023) and Lan-
gevin et al. (2022) have begun to investigate this potential 
for financial services. However, these studies primarily focus 
on comparing different data generation methods and present 
synthetic data sharing as merely one potential application. 
This leaves significant research gaps regarding the mecha-
nisms for data exchange, the optimal strategies for learning 
from cross-institutional synthetic data, and the incentives 
for participating institutions, reaching beyond financial ser-
vices and tackling current challenges in data ecosystems in 
general. Moreover, these studies offer little guidance on the 
design of such an ecosystem, highlighting a clear need for 
establishing design principles and best practices.

Research approach

A design science research project was initiated to address 
a research gap in approaches to enhance privacy protec-
tion within data ecosystems while preserving data utility 
for machine learning applications. This need, combined 
with the financial services industry’s demand for solutions 
to address the limitations of inter-organizational collabo-
ration in tackling financial fraud and anti-money launder-
ing detection, prompted the research effort. This project is 
aimed at designing an innovative artifact that provides finan-
cial institutions with a tool to easily exchange high-quality 
data with each other enabling them to increase their fraud 
and anti-money laundering detection performance, creat-
ing guidance on how to implement such a system, as well 
as to evaluate its benefits and the associated privacy risks 
(Gregor & Hevner, 2013; Peffers et al., 2007). To achieve 
these objectives, we adopted design science research (DSR), 
a framework particularly suited for the iterative develop-
ment  of  novel  artifacts  addressing  solution  spaces  with 
broad implications for both theoretical and practical prob-
lem domains (Peffers et al., 2007) and providing theoreti-
cally justified prescriptive knowledge (Gregor et al., 2020). 
Following this paradigm, we focus on  creating  artifacts 
that serve organizational purpose, in our case enabling data 
sharing despite privacy restrictions, through a structured 
research process that rigorously builds and evaluates viable 
solutions (A. R. Hevner et al., 2004; March & Smith, 1995). 
Following Scheider et al. (2023), our artifact is a “model” 
(March & Smith, 1995), a type of DSR artifact that serves

as a simplified representation of reality and accumulates 
specific design knowledge (March & Smith, 1995); thus, 
DSR provides a suitable framework for our study (A. R. 
Hevner, 2007; Iivari, 2007). Our model presents a struc-
tured approach to designing a data ecosystem under privacy 
and data complexity constraints, exemplifying a solution 
to the problem discussed in the earlier sections. Our meth-
odological approach to DSR—the design science research 
methodology (DSRM) by Peffers et al. (2007) has six steps, 
arranged in sequential order, and incorporates an iterative 
research procedure by design. The process typically starts 
with the identification of a research problem with practical 
relevance, in our case, the challenge of data scarcity within 
financial fraud detection. Next, the solution objectives are 
designed to address the stated challenges and to create a 
meaningful artifact. In line with DSR, the insights gained 
from the build-and-evaluate process must be generalizable 
and therefore applicable in more generic settings (Jones & 
Gregor, 2007). Also, the design artifacts should result in 
profound disruptions to traditional ways of doing business 
(A. Hevner & Gregor, 2022). Based on these objectives and 
on theory, the artifact is designed and developed in the next 
research process step. Phase 5 comprises evaluation, which 
is necessary to test whether an artifact achieves the purpose 
of its creation and to prove this achievement using rigorous 
methods (Venable et al., 2016). The evaluation phase also 
helps one to better understand the problem at hand and thus 
to realize improved outcomes (A. R. Hevner et al., 2004). 
Due to the iterative nature of this process, it can be repeated 
until a suitable artifact is derived. The design knowledge in 
the form of DPs with their DRs and MRs generated during 
this process can be seen as a nascent design theory, cap-
turing a general solution in a class of artifacts (Baskerville 
et al., 2018). While MRs are high-level, generalized goals 
that an artifact must satisfy to address a class of problems, 
providing the foundational objectives for artifact design 
(Walls et al., 1992), DRs are specific, actionable specifica-
tions that detail the necessary features and characteristics an 
artifact must have to fulfill the meta-requirements (Gregor 
& Hevner, 2013). Lastly, DPs are prescriptive, actionable 
guidelines derived from design requirements and grounded 
in both theoretical foundations and empirical evidence, pro-
viding clear instructions for creating artifacts that meet the 
specified requirements and address the underlying problem 
space (Gregor et al., 2020). Thus, especially the DPs can be 
used to guide actions in a wider range of problems, in par-
ticular, data ecosystems where data with a complex structure 
needs to be shared under privacy restrictions (A. R. Hevner 
et al., 2004). They contribute to the theoretical advance-
ment of the information systems (IS) community and pro-
vide valuable guidance for practitioners in designing similar 
artifacts (Baskerville et al., 2018; Sein et al., 2011). Since 
the DSR approach requires integration into an organizational

---

<!-- PAGE 6 -->

7  Page 6 of 28

Electronic Markets (2025) 35:7

context, the project was conducted in collaboration with 
the UnionBank of the Philippines, a rapidly growing digi-
tal bank, as well as a European neo bank with a focus on 
wholesale transaction banking. Both banks rapidly scaled 
their digital transaction infrastructure in recent years and 
are now looking for new ways to tackle transaction fraud and 
money laundering. While the banks granted us deep insights 
into the problem of limited transaction data and provided 
invaluable feedback through all cycles, it was decided that 
prototyping and evaluation would be conducted on publicly 
available datasets instead of real bank data to reduce risks 
and allow fast iterations to create a solid understanding of 
potential pitfalls.

Within  this  DSRM  framework,  four  iterative  design 
cycles were conducted, thus allowing for continuous refine-
ment of the artifact’s design based on feedback and derive 
insights (Mullarkey & Hevner, 2019; Sein et al., 2011). In 
the next paragraph, the activities in each cycle are intro-
duced which are outlined in the following graphic (Fig. 1).
First, the DSRM project starts with problem identifica-
tion and motivation, focusing on stakeholder problems and 
challenges. This was done by conducting a systematic litera-
ture review on data ecosystems, synthetic data, and financial 
fraud detection as well as semi-structured interviews with 
employees at different levels at our partner banks, who are 
engaged in data sharing initiatives, fraud detection or data

analytics, and machine learning projects. Furthermore, these 
interviews were used to identify the objectives of our solu-
tion by deriving DRs and MRs. Next, we iterated the first 
“Design—Demonstrate—Evaluate”  cycle.  In  the  design 
phase, we formulated the initial set of DPs. These princi-
ples were then translated into a system architecture during 
the demonstration phase, specifying its material properties 
like algorithms and interaction layers. Subsequently, an 
evaluation was conducted, involving feedback from aca-
demics and industry experts through four semi-structured 
interviews. The outcomes helped evaluate the feasibility of 
the initial design and led to the refinement of selected DPs 
in the second iteration. In cycle 2, we conducted a literature 
review identifying suitable algorithms for synthetic financial 
transaction data generation and based on them, instantiated 
a prototype which was subsequently evaluated on a publicly 
available real-world credit card transaction dataset to iden-
tify the most suitable synthetic data generation algorithm, 
establish the feasibility of the solution, and demonstrate the 
privacy-preserving properties of synthetic data. Based on 
additional expert feedback as well as two large simulated 
financial transaction data sets, cycles 3 and 4 refine the exist-
ing DPs and introduce new ones where needed. While cycle 
3 explores the local level of the ecosystem in more detail, 
cycle 4 focuses on the global level and cooperative chal-
lenges within the ecosystem. Throughout the DSRM cycles,

Fig. 1   Steps and design cycles within our design science research study based on Peffers et al. (2007)

---

<!-- PAGE 7 -->

Electronic Markets (2025) 35:7

Page 7 of 28  7

we iteratively abstracted the requirements, DPs, and system 
features. Thus, our main theoretical contributions lie in the 
abstracted artifacts, particularly the DPs, which are first 
derived in “Design of initial DPs” and continuously refined 
throughout the paper.

Problem identification and motivation

The diagnosis phase consists of two tasks: understanding the 
problem and solution domain and defining the ecosystem’s 
requirements. First, we positioned our DSRM project within 
the domain of inter-institutional collaboration within finan-
cial services. With a major focus of such collaboration being 
financial fraud detection, a first literature review on data 
ecosystems, synthetic data, and financial fraud detection was 
conducted. Following the methodology by Webster and Wat-
son (2002), four search strings were established (Table 1) 
and the following databases: ScienceDirect, EBSCOhost, 
SpringerLink, IEEE Xplore, and AISeL, were queried for 
articles containing the previously defined search string in 
title, abstract, or the author keywords. Furthermore, only 
papers written in the English language and published within 
the past 5 years were included. This initial query resulted 
in a total of 3794 papers, which were then filtered based on 
a screening of titles and abstracts. While for papers iden-
tified by the “Fraud Detection” query strings only papers 
were included that deal with financial transaction fraud and 
either focus on privacy or a multi-organizational context, 
for papers selected by the “Data Ecosystem” string the only 
inclusion criteria were a focus on data ecosystems. After 
adding more relevant papers through a forward and back-
ward search a total of 61 papers were selected for inclusion 
in the literature review.

The  analysis  of  the  first  part  of  our  literature  review 
focusing on fraud detection revealed that the limited availa-
bility of data is a significant challenge, especially for smaller 
organizations (Kulatilleke, 2022; Pranto et al., 2022). Espe-
cially  with  increasingly  sophisticated  adversaries  (Qiao 
et al., 2024) and thus, more complex fraud detection models, 
frequently built based on deep learning architectures, more

data is needed for model training (Aurna et al., 2023; Hilal 
et al., 2022). This need for increasing amounts of training 
data is further aggregated by the extreme class imbalance 
of datasets (large datasets are needed for a sufficient num-
ber of samples in the minority class) as well as the fast-
changing nature of fraudulent patterns (Abdul Salam et al., 
2024; Ryman-Tubb et al., 2018). Tackling this, frequently, 
the proliferation of cross-institutional data is presented as a 
potential solution, to increase the amount of available data 
and train better and more robust models (Kong et al., 2024; 
Myalil et al., 2021; Qiao et al., 2024). However, due to the 
high sensitivity of financial transactions and the connected 
risk of privacy leakage, this exchange is usually prohibited 
by external regulation or internal guidelines (Bian & Zheng, 
2023; Pranto et al., 2022; Ryman-Tubb et al., 2018). To over-
come  this  problem,  frequently  federated-learning-based 
solutions are proposed, allowing the raw data to remain 
local, while a joined model is trained (Kong et al., 2024; 
Lei et al., 2023; Pranto et al., 2022). While these approaches 
show some promise, they retain significant drawbacks such 
as the computational overhead, scalability issues, and the 
necessity to agree on a single model architecture, which is 
difficult to modify once established (Baabdullah et al., 2024; 
Chatterjee et al., 2024). This leads us to the conclusion that 
there is a need for a data ecosystem that allows financial 
institutions to exchange data with one another while staying 
compliant with laws and internal regulations on data privacy 
and giving them the freedom to use this data to fulfill their 
specific needs.

Definition of solution objectives

Looking for potential solutions, we drew on the second 
part of our literature review focusing on data ecosystems 
providing relevant insights on how such challenges can be 
navigated and potentially overcome in the context of finan-
cial data. Particularly papers from the healthcare domain 
(H. Chen et al., 2023; Morley-Fletcher, 2022), investigations 
into the emergence (Gelhaar & Otto, 2020) and organization 
(Langer & Mukherjee, 2023) of data ecosystems as well as

Table 1   Results of systematic literature search

ID

Search string

Hits

Filter:  titlea

I

II

“Financial” AND “Fraud Detection”
“Transaction” AND “Fraud Detection”
“Financial” AND “Data Ecosystem”
“Synthetic Data” AND “Data Ecosystem”

2471
990
164
169

336
139
13
6

Remove dupli-
cates

Filter: 
 abstracta

Fwd and Bwd 
search

Total

449

19

30

18

5

8

35

26

a Detailed  filter  criteria  can  be  found  at  https:// anony mous. 4open. scien ce/r/ Synth eticD ataEc osyst ems- 801C/ Cycle1_ Initi alDes ignPr incip les/ 
README. MD

---

<!-- PAGE 8 -->

7  Page 8 of 28

Electronic Markets (2025) 35:7

Table 2   Overview interviewees for solution requirements

ID

Job title

Expertise

Years of experience

Length of interview

Interviewee 1
Interviewee 2
Interviewee 3
Interviewee 4
Interviewee 5
Interviewee 6
Interviewee  7*
Interviewee  8*

Chief data scientist
Senior data scientist
Data scientist
Chief financial officer
Senior compliance officer
Junior compliance officer
Head of the AI center of excellence
Head of data science ventures

Data science
Data science
Data science
Fraud detection
Fraud detection
Fraud detection
Data science
Data science

10 years
5 years
5 years
 > 20 years
 > 20 years
4 years
 > 20 years
10 years

*Interviewee from UnionBank of the Philippines

00:51:10
00:37:34
00:36:30
00:38:36
00:59:08
00:44:27
00:19:25
00:31:03

the preconditions for data sharing (Fassnacht et al., 2023), 
were detrimental in deriving the design requirements pre-
sented in the following section.

To extend our insights into the domain beyond academic 
literature next, nine semi-structured interviews with employ-
ees at various levels at our project partners, with a focus on 
fraud detection or data science, were conducted (for details, 
see Table 2). Querying them for challenges as well as poten-
tial solutions for tackling data scarcity within their domain.
Based on this, we formulated two meta-requirements 
(MR) that any solution must adhere to. MR1 emphasizes the 
ease of data sharing between financial institutions, encom-
passing both technical, legal, and collaboration aspects. 
The need for technical ease of use was informed by insights 
drawn from the medical field, where challenges related to 
tool availability and varying data standards were identified 
as hindrances to data sharing (van Panhuis et al., 2014). 
The legal dimension in ecosystem usability was motivated 
by diverse regulatory requirements across jurisdictions, as 
observed in existing approaches to sharing financial transac-
tion data (Blake et al., 2019). Lastly, ease of collaboration 
was drawn from the ecosystem literature, where cooperative 
challenges were outlined as a major hurdle to data ecosystem 
development (Gelhaar & Otto, 2020). MR2 highlights the 
necessity of increased utility as a result of sharing data. This 
requirement emanated from discussions with our partners 
regarding their goal of establishing a data-sharing ecosystem 
and from the literature describing incentives for participation 
in data ecosystems (Gelhaar et al., 2021).

Next, we refined the MRs into more specific DRs, draw-
ing from literature as well as the knowledge of our project 
partners.1 To incentivize users to participate in data-sharing, 
setup as well as reoccurring costs need to be as low as pos-
sible, which is reflected in MR1 and propagates into DR1

1  A detailed mapping from interview quotes to DRs can be found on: 
https:// github. com/ Farum an/ Synth eticD ataEc osyst ems/ blob/ master/  
Cycle1_ Initi alDes ignPr incip les/ README. MD

and DR2. This is important because while a data standard for 
financial transaction data exists, different banks diverge from 
it (Major & Mangano, 2020), which was also confirmed dur-
ing our interviews (“Different data providers have different 
schemas and transaction languages.”—Interviewee 2); thus, 
a data ecosystem needs to be flexible enough to accommo-
date various input data structures (DR1). This is particularly 
important as data needs to be regularly updated and the cost 
for these updates should be as low as possible. Furthermore, 
data privacy standards imposed by regulators and internal 
policies must be upheld (“In terms of data sharing we do not 
engage in anything, because this is the pain with financial 
institutions, we are really protective of our data”—Inter-
viewee 8–1). Our interviews revealed that in the context of 
our partner institutions, this means that all real data must 
be processed locally within the financial institution (DR2). 
From a data-centric perspective, the performance of machine 
learning methods can be enhanced by increasing the vol-
ume of training data available (Sun et al., 2017). Thus, MR2 
can be achieved by enabling the combination of data from 
multiple sources through the data ecosystem and making it 
accessible as a unified data source (DR3). Given the goal of 
creating an ecosystem that is applicable to multiple tasks, the 
absence of a dominant algorithm in many fields (e.g., fraud 
detection), and the insight from our interviews that banks 
prefer to build and exclusively own their solutions (“One 
model will not be enough, it will be a collection of models 
which answer different questions …”—Interviewee 8–1), 
the data ecosystem must support diverse types of algorithms 
(DR4). Additionally, the imbalanced nature of fraud data 
necessitates tools on the ecosystem to address data imbal-
ances through filtering, oversampling, and undersampling 
(DR7), as most machine learning algorithms perform better 
on balanced datasets (Longadge & Dongre, 2013). As fraud 
patterns change quickly when discovered, the timely integra-
tion of recent fraud patterns into fraud detection algorithms 
is crucial (Benchaji et al., 2021; Zhu et al., 2021). As this is 
utterly important, two DRs were dedicated to achieving this. 
First, institutions should have the capability to automatically

---

<!-- PAGE 9 -->

Electronic Markets (2025) 35:7

Page 9 of 28  7

update the data (“fraud, money laundering patterns will 
change, behavior patterns will change and that's why you 
need to establish this relationship where there is a continu-
ous flow of information”—Interviewee 4), ensuring that the 
dataset incorporates the most recent fraud patterns (DR5). 
This not only aligns with MR1 by enhancing user conveni-
ence and reducing the need for frequent user inputs but also 
guards against model drift (Zhang, 2022). However, even 
with automatic updates, the dataset may still be dominated 
by outdated fraud patterns, posing a risk to the algorithms 
(Paleyes et al., 2023). Therefore, users should be able to 
incorporate pattern-based artificial data into the ecosystem 
(“…[the] machine has the benefit of learning the patterns 
you, as a human, identify as problematic. In the current 
world, such patterns are the key to everything because crimi-
nals will always evolve.”—Interviewee 6) (DR6). Allowing 
the data ecosystem to benefit from expert domain knowledge 
is not yet reflected in the data (Richhariya, 2012). After hav-
ing defined the problem as well as the solution space and 
outlined our requirements, we can now commence the first 
design, implementation, and evaluation cycle.

Cycle 1: DPs and system architecture 
for synthetic data sharing

During the initial phase of the DSRM project, founda-
tional DPs were established, integrating expert insights, 
relevant literature, and domain requirements, to develop a 
synthetic data ecosystem for financial institutions. Build-
ing on these insights an architecture for such an ecosystem 
was proposed.

Design of initial DPs

In our first design phase, our primary emphasis was on iden-
tifying the foundational DPs. Building on the DRs derived 
in the previous section and following the recommendations 
of Chandra et al. (2015), we created DPs that followed the 
structure “Provide the system with [material property—in 
terms of form and function] in order for users to [activity of 
user/group of users—in terms of action], given that [bound-
ary conditions—user group’s characteristics or implementa-
tion settings]” (Chandra et al., 2015, p. 4045). Furthermore, 
to ground these artifacts in practical relevance, expert inter-
views with our partners were conducted to justify the DPs 
derived from the literature. Figure 2 depicts the relationship 
between MRs, DRs, and DPs.

DP1—Provide the system with modular systems design 
in order to ensure independence of local data and cross-
institutional proliferation of synthetic data given that the 
raw data is sensitive: To address DR1 and DR3, the data 
ecosystem must possess the capability to process data from 
diverse sources while enabling the integration of this data 
for synthetic data generation. Drawing upon the principles 
of modular systems theory (Tiwana et al., 2010), institutions 
are granted flexibility in designing their module structures 
while adhering to a standardized representation, thereby 
ensuring that the data can be exchanged with the ecosystem. 
Additionally, once the initial setup is complete, automated 
data updating becomes straightforward, as all computations 
can be performed locally, without the need for sensitive data 
to be transmitted outside the local system. This capability 
fulfills the requirements outlined in DR5.

DP2—Provide the system with the ability to generate 
synthetic  transaction  data  using  generative  adversarial

Fig. 2   Relationship between MRs, DRs, and DPs using the final set of DPs

---

<!-- PAGE 10 -->

7  Page 10 of 28

Electronic Markets (2025) 35:7

networks (GANs) in order to remove private data, given 
guidelines, or regulations on data sharing: Most models 
created in financial institutions, such as fraud detection 
algorithms, need to be trained on transaction-level data as 
its granularity and connectedness over time allows for com-
plex patterns to emerge (Hilal et al., 2022) This combined 
with DR4, which requires users to train different types of 
algorithms and mandates a data ecosystem to provide the 
user with access to such low-level data. However, sharing 
transaction-level data poses challenges due to regulatory 
constraints (Blake et al., 2019) and internal policies man-
dating its local storage (DR2). As anonymization is not 
able to preserve both data utility and privacy for heavily 
interconnected data (Loukides et al., 2010), we propose to 
solve this challenge by using GANs, due to their unique 
ability to learn patterns in data and generate synthetic data 
nearly indistinguishable from the original (Walia et al., 
2020). This enables us to preserve real data locally while 
sharing only the privacy-preserving GAN-generated data 
within the data ecosystem. This data can then be merged 
with synthetic data from other institutions and allows the 
training of machine learning models on the combined data-
set. Therefore, ensuring the confidentiality of sensitive data 
while empowering the ecosystem to enhance fraud detec-
tion capabilities by training algorithms with substantial 
volumes of high-quality data.

DP3—Provide the system with a back-testing mecha-
nism in order to ensure newly generated synthetic data 
matches  in  composition  and  fraud  detection  training 
performance with real data given that data quality can-
not be independently verified: To facilitate the seamless 
integration of data from multiple institutions (DR3) and 
enable frequent system updates without human interven-
tion (DR5), it is essential to establish a robust quality 
control mechanism. This mechanism serves to uphold the 
integrity of the data introduced into the ecosystem, as 
only a few bad data points can have tremendous effects 
on machine learning models (Chakravarty et al., 2020). 
One approach to achieve this is by implementing a back-
testing procedure, which ensures that the synthetic data 
accurately captures the underlying patterns of the local 
real data (Dankar et al., 2022).

DP4—Provide the ability to alter synthetic data to give 
it the optimal composition for the training of machine 
learning  models  given  that  data  in  fraud  detection  is 
highly skewed: To further enhance model performance, 
a data-sharing ecosystem should be designed to provide 
users with the ability to alter and extend the existing data 
to  create  the  right  data  for  their  use  case.  In  financial 
services use cases, such as money laundering or fraud 
detection, the balance between the classes often is a chal-
lenge (Al-Hashedi & Magalingam, 2021), resulting in the

requirement, that a data ecosystem should be able to pro-
vide more balanced datasets (DR7). This can be accom-
plished by equipping users with advanced filtering options 
or enabling them to manipulate the existing data through 
techniques such as under- or oversampling (Lopez-Rojas 
& Axelsson, 2012).

Demonstration of DPs by instantiation in a system 
architecture

Based on the DRs and DPs, we present a multi-layered plat-
form architecture for a synthetic data ecosystem. While the 
local processing layer is implemented at every institution, 
the synthetic data generation as well as the fraud detec-
tion layer are centralized. An overview of this architecture 
mapped with corresponding DPs can be seen in Fig. 3.

Local processing layer  The local processing layer is modu-
lar and situated at every financial institution (DP1). Here, 
the GAN models are trained on sensitive transaction data 
to produce accurate synthetic representations of this data 
(DP3). Furthermore, the conversion to the data standard 
the synthetic data needs to conform to is enforced. Moreo-
ver, back-testing is done to ensure data quality while guar-
anteeing that the real data never leaves the local environ-
ment (DP2).

Global data layer  Contrary to the previous layer, the syn-
thetic  data  layer  is  not  situated  at  a  specific  institution. 
Instead, this layer is where synthetic data is merged and 
modifications to the data composition through the addition 
of pattern-based data generators or the artificial rebalancing 
of different classes can be achieved (DP4).

Fraud detection layer  This layer is accessible to any partici-
pating company allowing them to access the synthetically 
generated data and modify it to fit their models by providing 
capabilities to subsegment and alter data, making it optimal 
for their custom fraud detection models.

Evaluation of derived DPs and system architecture

After deriving the system architecture from our DPs, we 
presented both to two experts from our partner institution 
as well as 2 academics (for details, see Table 3).

The  feedback  gathered  from  the  experts  was  overall 
positive and especially the use of modular system design 
(DP1) to ensure reduced complexity of the eco-system and 
complete control of the local layer by the single institutions 
was highly appreciated. Furthermore, DP4 was approved 
by experts stating that “balancing data is a major concern 
when training ML models and a system providing smart

---

<!-- PAGE 11 -->

Electronic Markets (2025) 35:7

Fig. 3   System architecture (ver-
sion 1)

Page 11 of 28  7

Table 3   Interviewees for validation of DPs and platform architecture

ID

Job title

Expertise

Years of experience

Length of interview

Interviewee  7*
Interviewee  8*
Interviewee 9
Interviewee 10

Head of the AI center of excellence
Head of data science ventures
Research assistant
Research assistant

Data science
Data science
Statistical modeling
Design science research

> 20 years
10 years
5 years
5 years

00:23:16
00:20:27
00:31:26
00:22:01

*Interviewee from UnionBank of the Philippines

support for that could be particularly helpful” (Interviewee 
10). Lastly, the proposed architecture was seen as a good 
first outline to create a prototype; however, the computa-
tional resources required to train the synthetic data genera-
tion models for frequent updates were raised as a concern. 
When discussing the proposed DPs as well as architecture 
with  academic  experts  from  the  field  of  design  science 
research, data sharing, and fraud detection, DP2 was criti-
cized for multiple reasons. First, the limitation to a single 
technology for data generation (GANs) was seen as being 
too restrictive and limiting the system’s adaptability to dif-
ferent domains (“Why do you limit yourself to a single data 
generation algorithm?”—Interviewee 10). Furthermore, 
concerns emerged about the feasibility of generating finan-
cial transaction data from limited local data and the utility 
of synthetic data to benefit fraud detection performance (“I 
doubt that abstracted data from other institutions with dif-
ferent data distributions can improve fraud detection per-
formance.”—Interviewee 9).

Cycle 2: Synthetic financial transaction data 
generation and privacy

In the second cycle of the DSRM project, different methods 
for synthetic data generation were evaluated, thus tackling 
one of the limitations identified by expert feedback. This 
is done by testing the insights from a systematic literature 
review on synthetic data generation on a real-world financial 
fraud detection dataset, leading to the refinement of DP2.

Design of synthetic data generation

Addressing the expert feedback, the second design cycle 
focuses on the refinement and extension of DP2. Based on 
the comments, it was adjusted to DP2—Provide the sys-
tem with the ability to identify, validate, and apply context-
specific synthetic data generation techniques with mutually 
agreed on over-sampling in order to remove private data, 
given guidelines or regulations on data sharing so that it is

---

<!-- PAGE 12 -->

7  Page 12 of 28

Electronic Markets (2025) 35:7

Table 4   Results of systematic literature search

Search string

Hits Selected Fwd and Bwd search Total

(“synthetic data generation” OR “artificial data generation”) AND (“transaction data” OR “time

289 47

8

55

series data”)

no longer restricted to a single method for generating syn-
thetic data and includes the necessary validation of selected 
techniques to obtain optimal data generation performance.
To validate DP2 and identify suitable methods to gener-
ate synthetic financial transaction data, a literature review 
following vom Brocke et al. (2009) was conducted. In the 
first step, top publications regarding synthetic data genera-
tion were reviewed, resulting in our search string which was 
then used to identify journal articles and conference papers 
written in English and published after 2020 in the following 
databases: ScienceDirect, EBSCOhost, SpringerLink, IEEE 
Xplore, and AISeL. The results can be seen in Table 4.

From these papers, 46 distinct algorithms were extracted 
and grouped by their underlying algorithm type. Conse-
quently, GANs emerge as the primary underlying mecha-
nism (used by 55.3% of algorithms) for generating syn-
thetic transaction data. GAN models work by creating two 
neural networks that learn by competing in synthesizing 
and identifying synthetic data and thus, once trained, can 
generate synthetic data that is indistinguishable from real 
one (Goodfellow et al., 2014). However, different imple-
mentations exist. To allow for variations between the algo-
rithms tested and address the high degree of similarity 
between the different GAN architectures, we decided to 
only include two of them in our comparison: CTGAN (L. 
Xu et al., 2019), which was the most mentioned algorithm 
and is a representative of GANs taking only dependen-
cies between attributes, but not samples, into account and 
TimeGAN (Yoon et al., 2019) (ranked third by mentions) 
which incorporates the temporal dimension between sam-
ples. To tackle the criticism from cycle one, we extended 
our overview beyond GAN-based architectures. The most 
frequently mentioned implementations using other algo-
rithm types were Gaussian mixture models, which learn the 
distribution for each attribute and then generate new sam-
ples by drawing from these (S. Xu et al., 2021) and TVAE 
(Ishfaq  et  al., 2023),  a  variational  autoencoder  (VAE), 
which works by learning to compress and decompress data 
into a low-dimensional space and then use the decompress

module in combination with random noise to synthesize 
new data. The literature predominantly focuses on applying 
these algorithms to health records (Xing et al., 2022), with 
limited exploration in other domains such as traffic data (S. 
Xu et al., 2021) and IoT data (Liu et al., 2019); however, 
none of the papers identified has examined the application 
of these methods for the cross-institutional proliferation of 
financial transaction data. Furthermore, while Weldon et al. 
(2021) found that using only synthetic data can achieve 
performance gains, others, such as Frid-Adar et al. (2018), 
show that mixing synthetic and real-world data is more 
beneficial.  Thus,  the  optimal  algorithm  for  generating 
financial transactions in the context of synthetic data shar-
ing as well as the necessity of combining synthetic with 
real data remains unclear. Lastly, by employing algorithms 
that do not provide privacy guarantees by themselves, it 
remains unclear how safe it is to share the generated data. 
To tackle these two privacy measures frequently used in 
the literature, nearest neighbor adversarial accuracy and 
membership inference risk precision were used to ensure 
the  evaluated  algorithms  do  not  leak  information  (Yan 
et al., 2022). While nearest neighbor adversarial accuracy 
measures if a classifier is able to distinguish between real 
(holdout set) and synthetic data and thus is a good indi-
cator for privacy leakage through overfitting (Yale et al., 
2020), membership inference risk precision measures how 
easy it is for an attacker to predict if a record is part of 
the train dataset or not based on the synthetic data (Choi 
et al., 2018). As no thresholds for these measures for finan-
cial transaction data exist, the ones for medical data were 
employed, which can be seen below (Table 5).

Demonstration of synthetic financial data 
generation

In this section, we operationalized the derived DPs into 
a prototype system in Python using a modified version of 
the synthetic data vault library (Patki et al., 2016). Look-
ing at the system architecture from design cycle one, the

Table 5   Thresholds for privacy 
measures in medical synthetic 
data generation literature

Measure

Nearest neighbor adversarial accuracy
Membership inference risk precision

Threshold

0.030
close to 0.5

Literature

Yale et al. (2020)
Zhang et al., (2019, Appendix D)
Choi et al., (2018, Appendix F)

---

<!-- PAGE 13 -->

Electronic Markets (2025) 35:7

Page 13 of 28  7

local and global data layers were implemented, resulting 
in an ecosystem that allows data ingestion, synthetic data 
generation, and data sharing. Furthermore, the ecosystem 
was created in a way that allows to switch between differ-
ent synthetic data generation methods, thus enabling the 
evaluation of different algorithms for financial transaction 
data generation.2

Evaluation of synthetic financial data generation 
algorithms

This evaluation compares the different synthetic data gener-
ation approaches outlined before. As a real-world source for 
performance comparison, the credit card transaction data-
set from the IEEE-CIS Kaggle competition3 was chosen. 
This dataset was selected because credit card transactions, 
reflecting user spending patterns, are closely comparable to 
bank transactions. Furthermore, it was the only real dataset 
identified, which allowed matching transactions to users, 
allowing for models expecting time series data to be trained. 
However, limitations exist, such as the limited observation 
period (6 months), many obscured features as well as the 
inability to identify senders of payments but only receivers. 
As we aim to analyze the benefits of sharing synthetic data 
across financial institutions, we split the dataset by credit 
card provider, creating four distinct subsets. An analysis 
across subsets showed significant differences, aligning with 
anticipated variations in multi-institutional bank datasets. 
After obtaining a suitable dataset, we defined our evalu-
ation process. For this, first, a Bayesian parameter search 
was used to tune the hyperparameters of the different syn-
thetic data generation models using a subsample of 100,000 
data points for each institution.4 After selecting the best 
hyperparameter combination for each generation model, an 
XGBoost classifier (commonly used in fraud detection as 
per Interview with Interviewee 5 as well as Al-Hashedi and 
Magalingam (2021)) was trained on either real data, syn-
thetic data, or combination of both (hyperparameter where 
tuned using threefold cross-validation). The results of this 
process were assessed using the ROC AUC score on a hold-
out dataset (30% of the total data). The ROC AUC score 
was chosen as it provides a comprehensive evaluation of the 
classifier’s performance across different levels of sensitivity 
and specificity and is frequently used in the literature (Sun 
et al., 2023). Furthermore, the evaluation was conducted in

2  The full implementation of Cycle 2 can be found on https:// github. 
com/ Farum an/ Synth eticD ataEc osyst ems/ blob/ master/ Cycle2_ Algor  
ithmC ompar ison/ README. MD
3  https:// www. kaggle. com/c/ ieee- fraud- detec tion
4  A detailed description of the hyperparameter tuning procedure can be 
found  here:https:// github. com/ Farum an/ Synth eticD ataEc osyst ems/ blob/ 
master/ Cycle2_ Algor ithmC ompar ison/ 02_ param Search/ README. MD

two stages. The first one covered the performance of indi-
vidual synthetic data generation algorithms, thus helping us 
to validate DP2, while the second one looked at the overall 
benefit of the proposed synthetic data ecosystem. In the first 
stage, the focus was on evaluating the performance of dif-
ferent generation algorithms (Fig. 4), revealing that GMMs 
(ROC AUC score 0.52) and TimeGANs (ROC AUC score 
0.5) underperformed expectations. This can be explained by 
the composition of the data. While GMMs struggled with 
the high dimensionality of the data (148 features), TimeG-
ANs had problems with short transaction chains (below 2 
transactions per user) due to the short observation period. 
While CTGAN (ROC AUC score 0.59) performed a little 
better, TVAE (ROC AUC score 0.89) excelled, particularly 
thriving in scenarios with limited training data, notably in 
datasets for “Discover” and “American Express,” which 
had fewer than 10,000 transactions. Thus, confirming that 
the selection of the right algorithm is crucial and therefore 
validating DP2.

Next, we analyzed the privacy implications of the pro-
posed algorithms, ensuring that the tested algorithms meet 
the previously defined privacy objectives and thus can be 
used in our proposed synthetic data ecosystem. As can be 
seen in Table 6, apart from TIMEGAN, all of the proposed 
algorithms stay within our previously defined privacy thresh-
olds, leading us to the conclusion that, for the proposed 
dataset, GMM, CTGAN, and TVAE are able to sufficiently 
obscure the data and can thus be used in our ecosystem.

The second-stage evaluation assessed the advantage of 
training on shared synthetic data versus isolated real data. 
Figure 5 compares the performance of models trained on 
isolated real data, isolated synthetic data, shared synthetic 
data,  and  shared  synthetic  data  combined  with  isolated 
real data. Models trained solely on synthetic data from one

Fig. 4   Comparison  between  different  synthetic  data  generation  algo-
rithms

---

<!-- PAGE 14 -->

7  Page 14 of 28

Table 6   Privacy measures per 
algorithm

Electronic Markets (2025) 35:7

Measure

GMM

Nearest neighbor adver-

0.000554

sarial accuracy

CTGAN

0.00189

TVAE

TIMEGAN

0.001499

0.000241

Membership inference

0.485238

0.489603

0.469872

0.130435

risk precision

source underperformed compared to those trained on real 
data. Yet, combining synthetic data from multiple sources 
led to a further performance drop, likely due to varying 
fraud cases across providers, which dilutes relevant pat-
terns. However, merging synthetic with real data for each 
institution boosted performance, increasing the ROC AUC 
score by 1%.

To better understand the impact of this improvement, we 
can look at the recall or what percentage of fraudulent cases 
are identified. Using synthetic and real data combined, we 
find that 2.14% more true positives are detected. Combining 
this with an estimated number of 24.16 million fraudulent 
card transactions per year only in the EU (European Cen-
tral Bank, 2021), the improved model would have detected 
about half a million additional transactions. Thus, showing 
the benefit of our ecosystem. However, this fusion of shared 
synthetic data with local real data is not yet reflected in any 
DP; however, the evaluation showed it to be a critical princi-
ple of our proposed design. Thus, a new DP: DP5—Provide 
the capability to combine synthetic data to find an optimal 
composition for the training of machine learning models 
given scenarios with data from multiple institutions was cre-
ated, incorporating this important design criterion. Based on 
this the proposed system architecture was revised, which can 
be seen below (Fig. 6).

Moreover, the outcomes of this design cycle were pre-
sented to additional experts in the field and two primary

Fig. 5   Comparison between synthetic and real data combinations

critiques emerged: the constraint that the design was only 
validated in a singular context on a single dataset, which 
poses questions about its generalizability, and the inher-
ent challenges in establishing such an ecosystem, particu-
larly concerning the incentivization mechanisms required 
to  encourage  active  participation  among  the  financial 
institutions.

Cycle 3: Local synthetic data recombination 
and usage

In the third cycle, we expanded the scope of our data ecosys-
tem design to address a broader range of applications beyond 
fraud detection, aiming to validate the DPs’ versatility and 
robustness in two contexts. Furthermore, the design ele-
ments of the local data level were investigated in more detail, 
resulting in the refinement and validation of DP5 and DP2.

Design of mechanisms at the local data level

Building  on  the  expert  feedback,  in  this  iteration  of  our 
research, we broaden the scope of our data ecosystem design 
to encompass a wider range of applications, aiming to demon-
strate the versatility and robustness of our DPs in various con-
texts. Furthermore, this iteration focuses on investigating the 
design elements on the local data level, thus providing design 
knowledge for the individual institutions within the ecosystem. 
On the one hand, we focus on the validation and refinement of 
DP5—Provide the capability to combine synthetic data to find 
an optimal composition for the training of machine learning 
models given scenarios with data from multiple institutions 
by exploring the effect of the mixing percentage between syn-
thetic and real data. On the other hand, we investigate DP2—
Provide the system with the ability to identify, validate, and 
apply context-specific synthetic data generation techniques 
with mutually agreed on over-sampling in order to remove 
private data, given guidelines or regulations on data sharing 
in more detail by developing design recommendations on how 
to train the synthetic data generation models.

To extend our investigation to new domains, we consulted the 
literature and solicited input from our partner institutions, iden-
tifying money laundering detection as a significant use case that 
heavily relies on machine learning (Z. Chen et al., 2018) and often 
lacks sufficient training data (Jensen et al., 2023). Subsequently,

---

<!-- PAGE 15 -->

Electronic Markets (2025) 35:7

Fig. 6   Updated system architec-
ture (version 2)

Page 15 of 28  7

an examination of the literature regarding the enhancement of 
machine learning performance through the incorporation of syn-
thetic data was conducted, aiming to determine an optimal ratio of 
real to synthetic data (mix-in percentage). While some researchers 
only oversample the minority class using synthetic data (Charitou 
et al., 2021; Strelcenia & Prakoonwit, 2023), others train models 
exclusively on synthetic data (Sattarov et al., 2023) or combine 
real with synthetic data (Dahmen & Cook, 2019). Thus, it remains 
unclear if there is an optimal mix-in percentage that individual 
institutions should incorporate into their design.

To find the optimal way to generate synthetic data for our 
ecosystem, this section investigates data generation configu-
rations that utilize the entire dataset as well as those trained 
on distinct data subsets and further analyzes the benefit of 
different pre-processing steps during the synthesizing pro-
cess. Due to the challenge of dataset imbalance, models 
tend to be biased towards the majority class, decreasing the 
quality of data in the minority class; mitigating this issue, 
oversampling can be applied during the generation process 
to enhance generator robustness, albeit at the risk of distort-
ing dataset composition (too many positive samples) (Kiran 
& Kumar, 2024). Second, the construction of distinct syn-
thetic data generators for each class has been proposed as 
an alternative solution. Enabling the generator to better cap-
ture the characteristics of each individual class. However, 
this results in the problem that the minority class generator 
is only trained with a small dataset, which might harm its 
generalizability (Eilertsen et al., 2021). To remedy this, Fan 
et al. (2022) have suggested a novel methodology where the 
generator for the minority class is pre-trained using samples 
from the majority class, thus circumventing the problem.

Demonstration through implementation 
of different training and data‑fusing schemes

In this section, we operationalized the derived DPs into a 
prototype system in Python using a modified version of the

synthetic data vault library (Patki et al., 2016). Building upon 
the architecture from design cycle two, the local layer was 
modified to accommodate for different generation schemes 
with and without oversampling as well as pre-training on 
the local level. Furthermore, the training scheme of the pre-
diction model was modified so that the system was able to 
accommodate training with different mix-in percentages.5

Evaluation of different training and data‑fusing 
schemes

One challenge in evaluating the broader feasibility of our 
synthetic data sharing ecosystem is the lack of publicly 
available financial transaction data (Jensen et al., 2023). 
However, multiple researchers have shown that simulated 
financial transactions can be suitable for validating new 
models or even evaluating interventions (Langevin et al., 
2022; Sattarov et al., 2023). Therefore, in this as well as 
the next cycle, we will use two datasets, one for anti-money 
laundering (IBM-AML6) and one for fraudulent transac-
tions (IBM-CCF7), which were generated by using a multi-
agent-based approach, simulating actors that act according 
to predefined rules, thus creating a stream of transactions 
(E. Altman et al., 2024; E. R. Altman, 2019). The resulting 
datasets have the advantage of being magnitudes larger in 
size (IBM-AML: 31898238/ IBM-CCF: 24386900) than the 
data used in the previous cycle (IEEE-CIS: 1097231) and 
have a network structure more similar to the one in real data. 
However, due to its simulation-based nature, it might not

5  The  full  implementation  of  Cycle  3  can  be  found  here:  https:// 
github. com/ Farum an/ Synth eticD ataEc osyst ems/ blob/ master/ Cycle3-  
4_ Ecosy stemE valua tion/ README. MD
6  https:// www. kaggle. com/ datas ets/ ealtm an2019/ ibm- trans actio ns-  
for- anti- money- laund ering- aml
7  https:// www. kaggle. com/ datas ets/ ealtm an2019/ credit- card- trans  
actio ns

---

<!-- PAGE 16 -->

7  Page 16 of 28

Electronic Markets (2025) 35:7

inhibit all characteristics found in real data. As the selected 
datasets do not include a financial institution (IBM-CFF) 
or the number of financial institutions present in the data 
is too big (IBM-AML, 122333 different banks), the data 
was artificially grouped. This was done by segmenting the 
data based on the location of the individual (IBM-CCF)/
bank (IBM-AML) connected to a transaction, creating clus-
ters that simulate the transactional networks of hypotheti-
cal financial institutions. As a result, the IBM-CCF dataset 
included four financial institutions with a relatively even 
data distribution, while the IBM-AML dataset emerged with 
seven banks of which two banks held over 75% of the data. 
This contrast in dataset composition affords a unique chance 
to explore the synthetic data sharing ecosystem’s functional-
ity under a broad array of conditions. Moreover, an analysis 
of client distribution post-split for each provider highlighted 
significant disparities, aligning with the anticipated diversity 
suspected within multi-institutional datasets. Details on the 
specific distributions are outlined in Table 7.

To limit the variables of this investigation, the synthetic data 
generation model and the fraud prediction model were kept 
constant. For the synthetic data generation model, the previ-
ously superior TVAE-based generator8 with hyper parameters 
tuned to the individual institution was used. Similar to Cycle 
2, a XGBoost classifier with hyperparameter selection using 
threefold-cross validation was chosen as the prediction model 
and the performance comparisons were done using the ROC 
AUC score on a holdout dataset (30% of the data).

Before, investigating the approaches modifying the local 
layer, the transferability of synthetic transaction data sharing 
beyond transaction fraud detection was evaluated (Fig. 7). To 
do this, we compared the average ROC AUC score between 
the dataset constructed for financial fraud detection (IBM-
CFF) and the one constructed for anti-money laundering 
detection (IBM-AML).

Figure 7 demonstrates that across both datasets, models 
trained with synthetic shared data surpassed those trained 
without it, enhancing the ROC AUC score by 3.6% in the 
transaction fraud dataset (IBM-CCF) and 6.6% in the anti-
money laundering dataset (IBM-AML). This effect can be 
considered substantial within this context as even recently 
introduced fraud detection algorithms often only increase the 
ROC-AUC score by a few percentage points (Hashemi et al., 
2023; Lebichot et al., 2021). This performance gain suggests 
that the data ecosystem’s effectiveness extends beyond merely 
detecting financial fraud but is also suitable for other use cases 
utilizing financial transaction data such as money laundering 
detection. Thus, confirming the versatility and potential of

8  A detailed description of the hyperparameter tuning procedure can 
be  found  here:  https:// github. com/ Farum an/ Synth eticD ataEc osyst 
ems/ blob/ master/ Cycle3- 4_ Ecosy  stemE valua tion/ 02_ param Search/  
README. MD

Table 7   Distribution of data across the different banks

IBM-CCF

IBM-AML

Bank

Pct of data

Bank

Pct of data

Bank

Pct of data

0
1
2
3

21.54%
18.58%
39.16%
20.72%

0
1
2
3

5.93%
11.90%
2.87%
1.90%

4
5
6

29.94%
45.35%
2.12%

the synthetic data ecosystem in addressing a broad range of 
data challenges in financial services. Subsequently, we explore 
whether a specific mix-in percentage of real and synthetic data 
yields optimal results for machine learning performance. To 
accomplish this, we systematically assess the impact on model 
performance by varying the proportion of real and synthetic 
data used in training the models, exploring a spectrum from 
0% (no synthetic data) to 300% (3 times as much synthetic as 
real data). Figure 8 visualizes this experiment.

Observing the modest upward trajectory of the aggre-
gated performance line (black), we can conclude that there 
is a positive effect of adding synthetic data. However, in con-
trast to the more volatile performance trends of individual 
banks (grey), it appears there is not a universally optimal 
mix-in percentage. Instead, distinct peaks in performance 
suggest that the most effective mix-in ratios vary by bank. 
Consequently, we infer that allowing banks to adjust the 
mix-in percentage independently is most beneficial. This 
insight has been integrated into DP5, which mandates that 
banks have the autonomy to determine their mix-in ratios, 
leading to the updated principle: DP5—Provides the capa-
bility to combine synthetic data to find optimal composition 
for the training of machine learning models given scenarios 
with data from multiple institutions.

Finally, we explored various configurations and preproc-
essing methods for synthetic data generation to offer optimal 
guidance for setting up these processes at the local level. 
Essentially, there are two primary setups. The first, referred 
to as “full,” involves training the synthetic data generation 
model on the entire dataset. To mitigate the risk of the model 
predominantly generating samples from the majority class, 
versions that randomly oversample the minority class to a 
specified percentage of the data (“_OS{X}”) while training 
the synthetic data generator have been implemented. The 
second setup, “sep” entails training distinct generation mod-
els for each class. An extension of this approach, “sepPre” 
utilizes separate generators for each class but pre-trains the 
minority class generator with majority class data. The out-
comes of these varied approaches are detailed in Table 8.

The analysis of the data presented in Table 8 yields sev-
eral key findings. Initially, the “full” model demonstrates its 
ability to surpass the baseline performance, yet models built 
on the same training scheme but utilizing oversampled data

---

<!-- PAGE 17 -->

Electronic Markets (2025) 35:7

Fig. 7   Comparison between 
models trained with and without 
synthetic data for both datasets

Page 17 of 28  7

Fig. 8   Effect of synthetic data mix-in percentage on performance

Table 8   Comparison between 
different synthetic data 
generation models

Dataset

Method

ROC AUC score Dataset

Method

ROC AUC score

IBM-AML Without shared data 0.7168
0.7371
0.6435
0.6199
0.7209

Full
fullOS_10
fullOS_20
sep

IBM-CCF Without shared data 0.6817
0.7042
0.6618
0.6360
0.6817

Full
fullOS_10
fullOS_20
sep

sepPre

0.7473

sepPre

0.7323

exhibit a notable decline in performance. Thus, leading us to 
the conclusion, that for financial transaction data, oversam-
pling the data before training the synthetic data generation 
model is not suitable. Moreover, the “full” setup outperforms 
configurations where synthetic data generators are trained 
separately for each class (“sep”). This subpar performance 
stems from the “sep” model’s poor-quality synthetic data 
for the minority class, which fails to capture training data 
patterns due to limited training dataset size. However, when

the  minority  class  model  is  pre-trained  using  data  from 
the  majority  class  (“sepPre”),  a  significant  performance 
improvement  is  observed,  surpassing  all  other  methods. 
This enhancement is primarily due to the model’s capacity 
to generate higher-quality samples of the minority class with 
greater variability. Further discussions with partner institu-
tion  experts  emphasized  the  advantage  of  creating  class 
data separately as it enhances privacy by preventing leaks 
of sensitive information like fraud rates by independently

---

<!-- PAGE 18 -->

7  Page 18 of 28

Electronic Markets (2025) 35:7

producing the samples for each class. Consequently, we have 
refined DP4 to encapsulate these insights: DP2—Provide the 
system with the ability to identify, validate, and apply con-
text-specific synthetic data generation techniques with mutu-
ally agreed on over-sampling in order to remove private data, 
given guidelines or regulations on data sharing.

Cycle 4: Network effects of financial data 
sharing

In cycle four of our DSRM project, we delve into the global 
data layer, guided by the literature and expert insights to 
address cooperative challenges within the proposed syn-
thetic financial data ecosystems. Aiming to refine our DPs 
to enhance the ecosystem’s capability to effectively manage 
these challenges.

Design of mechanisms at the global data level

Addressing  the  second  aspect  of  expert  feedback  and 
informed by the literature on data ecosystems, this cycle 
focuses on the global data layer and its DPs to ensure that 
the created ecosystem is able to handle the challenges of 
data ecosystems described by Gelhaar and Otto (2020). 
Because cooperative challenges play a dominant role in 
the early stage of an ecosystem, the following cycle will 
focus on these (Autio & Thomas, 2014). In their paper, 
Gelhaar and Otto (2020) describe four major cooperative 
challenges that need to be addressed for a data ecosystem 
to emerge successfully. First, it is necessary to build trust 
between the participants. Second, it needs to be shown 
that all actors benefit from participating in the ecosys-
tem. Third, it is important to identify the right number of 
participants. Fourth, interoperability needs to be enabled 
through the agreement on standards. Thus, the focus of 
this section is to evaluate existing DPs through this lens 
and analyze whether refinements or additional principles 
are necessary for the development of an ecosystem capa-
ble of effectively addressing these challenges. First, trust 
between ecosystem partners can be built in multiple ways. 
On the one hand, trust can be increased by adequate con-
trol mechanisms (Geisler et al., 2021), which is already 
reflected in DP3—Provide the system with a back-testing 
mechanism in order to ensure newly generated synthetic 
data matches in composition and fraud detection training 
performance with real data given that data quality can-
not be independently verified which ensures sufficient data 
quality in the synthetic data ecosystem. On the other hand, 
Majava et al. (2016) show that intermediaries play a signifi-
cant role in increasing participants’ trust in an ecosystem. 
In the financial services ecosystem, this role is typically

held by public regulators. To incentivize them to partici-
pate in the ecosystem and allow them to ensure data quality 
and thus increase trust, we propose DP6—Provide access 
for external collaborators, such as regulators, to leverage 
the synthetic data within the ecosystem given a diverse set 
of synthetic data available. This gives regulators access 
to the ecosystem while adhering to the existing privacy 
measures. However, it remains unclear if access to purely 
synthetic data can provide enough value and thus incentiv-
ize their participation in the ecosystem. The next challenge 
data ecosystems face is that all actors need to benefit from 
participating in the ecosystem. While we already demon-
strated in previous iterations that our data ecosystem is able 
to increase the overall performance, it remains unclear how 
this performance gain is distributed between institutions. 
To address this, further investigation is needed to check if 
adjustments to our design need to be made to create suffi-
cient incentives for all institutions. Connected to this prob-
lem is identifying the right number of participants. While 
our previous cycles show that the ecosystem is beneficial 
if all institutions participate, it remains unclear if a similar 
effect exists, if only part of the institutions is included in 
the ecosystem. To incorporate this into our DPs, DP3 was 
extended to not only describe the monitoring of outgoing 
synthetic data but also cover the evaluation of performance 
gained by using the shared synthetic data from the data 
ecosystem. This results in DP3—Provide the system with a 
back-testing mechanism in order to ensure newly generated 
synthetic data matches in composition and fraud detection 
training performance with real data given that data quality 
cannot be independently verified. The last cooperative chal-
lenge that needs to be overcome is interoperability through 
the agreement on standards. At the moment, that is already 
incorporated in DP1—Provide the system with modular 
systems design in order to ensure independence of local 
data and cross-institutional proliferation of synthetic data 
given that the raw data is sensitive, from a data perspective 
where the local layer of the ecosystem is used to align the 
data so that it can be easily shared with the system later. 
Furthermore, we argue that creating DPs for the financial 
data ecosystem contributes to the standardization of the 
ecosystem from an infrastructure and ecosystem perspec-
tive and thus by creating these DPs we contribute to over-
coming this challenge.

Demonstration through the introduction 
of non‑sharing entities and individual performance 
benchmarking

In this part, we further improved the prototype developed 
in Python, by altering the global data layer to allow for the 
participation of entities that do not contribute data. Addi-
tionally,  we  updated  the  system  to  track  and  report  the

---

<!-- PAGE 19 -->

Electronic Markets (2025) 35:7

Page 19 of 28  7

Fig. 9   Regulator models using different resampled data and performance of the regulator model (only synthetic data) vs. the bank models

performance to each participating institution, thus allowing 
institutions on an individual level to see the performance 
gain from engaging in the data ecosystem.9

Evaluation of ecosystems with non‑sharing entities 
and individual performance benchmarking

Similar to the previous cycle, this evaluation again utilizes 
the two synthetic datasets (IBM-AML and IBM-CFF), due 
to their high data quality, size, and diversity. Moreover, the 
ecosystem setup and evaluation scheme are adopted from 
the previous cycle, utilizing the “sepPre” training scheme.

We start with evaluating DP6, which allows regulators 
to access purely synthetic data within the data ecosystem. 
To validate this DP, the synthetic data that is provided to 
the regulators need to be of sufficient quality for them to 
derive meaningful insights and effectively improve their 
models. However, as this cannot be easily evaluated, we 
use the performance of a prediction model trained on the 
data available to the regulator (only synthetic  data) as 
a proxy for the quality of the data. As the architecture 
chosen in Cycle 3 generates separate models for different 
classes, more data of a specific class can easily be gener-
ated. This is especially relevant for cases where only syn-
thetic data is used as no additional positive samples from 
the real data exist. Thus, the experiment conducted had 
two steps. In the first step, regulator models were trained 
on synthetic data with different amounts of minority class 
samples (indicated by OS_{percentage of minority class 
cases}). From this selection, the over-sampling ratio with 
the best performance was chosen and compared to the 
performance of the models trained at the different banks, 
once trained on a combination of real and synthetic data,

9  The  full  implementation  of  Cycle  4  can  be  found  here:  https:// 
github. com/ Farum an/ Synth eticD ataEc osyst ems/ blob/ master/ Cycle3-  
4_ Ecosy stemE valua tion/ README. MD

and once trained with only real data. The results of this 
experiment can be seen in the following diagram (Fig. 9).
The regulator model, trained exclusively on synthetic 
data, exhibits performance that, while not matching that 
of the bank’s internal models (trained on a mix of real and 
synthetic data), remains significant. The model approaches 
the performance of the bank’s baseline models (trained 
on real data only), as illustrated in Fig. 9. This capability 
offers considerable advantages to collaborators who would 
otherwise lack access to such data. Consequently, allowing 
regulators to access synthetic data emerges as an effective 
strategy to foster collaboration and enhance trust in the 
ecosystem. Therefore, DP6—Provide access for external 
collaborators, such as regulators, to leverage the synthetic 
data within the ecosystem given a diverse set of synthetic 
data available is validated and was added to our DPs for 
synthetic data ecosystems.

Subsequently,  the  adjustment  to  DP3  is  validated, 
checking if all banks profit from the synthetic data eco-
system and evaluating if the synthetic ecosystem includ-
ing fewer institutions is still able to profit from the net-
work effects of the ecosystem. To investigate this, we plot 
the performance of each institution against its baseline 
(score  without  any  artificial  data),  which  can  be  seen 
below (Fig. 10).

As evidenced in Fig. 10 for each single bank in both 
datasets, the performance increases by combining real and 
synthetic data. Furthermore, looking at the rightmost panel 
of Fig. 10, it can clearly be seen that there is a negative cor-
relation (− 0.09) between the performance gained by par-
ticipating in the ecosystem and the size of the bank. Thus, 
showing that small banks over proportionally profit from 
participation, providing a clear incentive for them to engage 
in the ecosystem. However, even if absolute performance 
gained by bigger banks is lower, we argue that they still 
have a sufficient incentive to participate due to their large 
volume of transactions, where even small changes in the

---

<!-- PAGE 20 -->

7  Page 20 of 28

Electronic Markets (2025) 35:7

Fig. 10   Performance gain per individual bank and performance gain by institution size

fraud detection percentage result in a high absolute sum 
of prevented losses. These results lead us to the conclu-
sion that all banks contributing to the ecosystem profit from 
their involvement and thus the designed ecosystem is able to 
overcome another one of the previously outlined challenges.
Next, we investigate our synthetic data ecosystem for 
cases where not all institutions engage in synthetic data 
sharing. To achieve this, we simulated environments, where 
none, 50%, 75%, or 100% of all banks were part of the eco-
system. The results can be seen in Fig. 11.

Despite the significant difference between the two data 
sets regarding their data distribution (with IBM-CCF having 
an equal distribution between banks, while IBM-AML has a 
highly skewed one), we can clearly see that in both cases, even 
with only half of the banks being part of the ecosystem (IBM-
CCF: 2 banks/IBM-AML: 3 banks), a significant performance 
gain is achieved. Thus, it seems the benefits of the synthetic 
data ecosystem can be realized from an early stage onwards, 
making it easy to overcome the hurdle of a minimum number

Fig. 11   Performance  (avg  per  bank)  by  percentage  of  participating 
institutions

of members needing to participate in the ecosystem, thus tack-
ling another of the challenges outlined previously.

Summarizing these results, we were able to demonstrate 
that the proposed data ecosystem is able to deliver excess 
performance for all participants in the network on an indi-
vidual level and it can be seen that even for data ecosys-
tems with only a fraction of the institutions participating in 
synthetic data sharing, still a significant performance gain 
can be achieved. Furthermore, there seem to be network 
effects to some extent where more partners in the ecosys-
tem increase its overall utility. As these results validate the 
incentives for partners to participate in an ecosystem, we 
confirm our DP3—Provide the system with a back-testing 
mechanism in order to ensure newly generated synthetic 
data matches in composition and fraud detection training 
performance with real data given that data quality cannot 
be independently verified.

Discussion

This research paper is aimed at extending the research on 
privacy in data ecosystems as well as machine learning of 
multi-organizational datasets by investigating these chal-
lenges in the field of financial fraud detection. This was done 
by deriving DPs for an innovative synthetic data-sharing 
ecosystem  that  allows  financial  institutions  to  exchange 
financial transaction data while protecting client privacy 
and learning effectively from this multi-institutional data. 
To create this artifact, we followed the process of DSRM 
(Peffers et al., 2007), with this paper covering four “design-
implement-evaluate” cycles. Starting with the problem iden-
tification our study contributes to descriptive knowledge 
concerning the problem space by identifying data scarcity 
in combination with the inability to share data due to pri-
vacy protection as a major hurdle for financial institutions, 
validating  the  existing  research  on  cross-organizational 
fraud  detection  collaboration  within  financial  services 
(Abdul Salam et al., 2024; Kong et al., 2024). During the 
exploration of the solution, space synthetic data sharing

---

<!-- PAGE 21 -->

Electronic Markets (2025) 35:7

Page 21 of 28  7

was identified as an underexplored solution to tackle data 
scarcity in financial fraud detection extending the literature 
on cross-organizational collaboration in the field (Chatter-
jee et al., 2024). Furthermore, the exploration of synthetic 
data to allow privacy-compliant data sharing as well as our 
experimentation on multi-organizational synthetic data dur-
ing multiple “design-implement-evaluate” cycles reaches 
beyond financial services and addresses significant chal-
lenges in the realm of data ecosystems (Brée et al., 2024). 
Moreover, our research extends beyond studies that simply 
outline the requirements of such a data ecosystem (Immonen 
et al., 2014). We validate these requirements and the derived 
DPs through rigorous experimentation on publicly available 
datasets and through close collaboration with industry part-
ners and experts, ensuring the practical applicability and 
robustness of our findings. Furthermore, by extending data 
ecosystem research into a less frequently explored domain 
(Cappiello et al., 2020), we are able to validate the applica-
bility of existing knowledge and uncover new insights with 
potential for generalization. We achieve this by developing 
prescriptive knowledge and nascent theory concerning the 
solution space, offering a set of DPs for designing a synthetic 
data sharing ecosystem and providing a first instantiation in 
the form of a platform architecture. To provide more detailed 
insights into this solution space, additional key findings are 
encapsulated in Table 9, clustered by key areas which we 
deductively derived a posteriori from our study.

As shown in Table 9 under the generation dimension, we 
contribute to the literature on synthetic data generation in 
multiple ways. First, we identified the necessity for a strictly 
separated local layer (where real data is transformed) and 
a global layer (where data is shared). Second, we transfer 
existing algorithms to a new setup including cross-organ-
izational data with a complex data structure and compare 
their performance on a prediction task (Pathare et al., 2023) 
identifying TVAE as the most performant algorithm for syn-
thetic financial data generation while still showing sufficient 
privacy. Third, we extend the research on the generation 
setup by consolidating different training schemes from mul-
tiple sources (Eilertsen et al., 2021; Fan et al., 2022; Kiran & 
Kumar, 2024) and comparing them to each other, identifying 
training on data sub-clusters as the most beneficial setup.

Moving forward to training models based on synthetic 
data, as shown in Table 9 under the prediction dimension, 
we extend the literature which often looks at synthetic data 
generation performance separately but provides little guid-
ance on how the generated data is best used in a data eco-
system (Dankar et al., 2022). Our research further shows 
that a mixture of synthetic and real data is most useful when 
combined; however, the exact mix-in percentage is highly 
organization and context-specific. Moreover, we demon-
strated that using purely synthetic data can still be beneficial 
for players with no access to real data; however, adjustments

need to be made to the composition of the data by artificially 
rebalancing it.

As can be seen in Table 9’s ecosystem dimension, our 
research investigates the complexities of data ecosystems, 
analyzing how the incentives for participation affect per-
formance  outcomes  across  various  sizes  of  institutions. 
This analysis also places our findings in the context of the 
research by Gelhaar and Otto (2020) about the initial chal-
lenges encountered within data ecosystems. By implement-
ing design interventions that clearly articulate performance 
benefits and facilitate the integration of external collabora-
tors, our research substantiates the ecosystem’s capacity to 
overcome these early hurdles. Further, our empirical evi-
dence suggests that even partial participation in the data eco-
system can lead to substantial performance improvements, 
thereby affirming the ecosystem’s operational feasibility and 
enhancing its attractiveness to potential participants.

In the last dimension in Table 9, we demonstrate the 
generalizability of our derived design knowledge beyond 
a single use case and application area. This was done in 
two ways. First, through validation with experts from the 
field in academia and the private sector. Second, through 
performance evaluation in two financial services domains 
and three datasets which required data sharing with privacy 
restrictions. While performance gains might seem insignifi-
cant, small changes in fraud detection rate can have major 
implications on financial institutions (Levi, 1998). Thus, our 
research not only confirms the relevance of our DPs and sys-
tem architecture but also sets the stage for their application 
beyond the immediate context of financial transactions, sug-
gesting a blueprint for extending beyond financial services 
to other domains where data needs to be shared with privacy 
restrictions (Susha et al., 2019).

For practitioners, our contribution is two-fold: For man-
agers and decision-makers, we demonstrate the value of 
synthetic  data-sharing  ecosystems  that  allow  both  large 
and small institutions to securely collaborate on data while 
ensuring privacy. This approach is particularly relevant in 
industries with complex, highly sensitive data, such as finan-
cial services, where data ecosystems do not emerge organi-
cally and require careful planning allowing for shared value 
propositions and services (Adner, 2017; Immonen et al., 
2014). Furthermore, our framework addresses regulatory 
requirements  on  data  privacy  and  our  results  suggest  a 
robust foundation for scaling and sustaining privacy-focused 
data ecosystems. For system architects, we outline a set of 
DPs that guide practitioners in structuring the architecture 
of these ecosystems. These principles assist in selecting 
suitable synthetic data generation methods, implementing 
mechanisms for data quality assurance, and integrating data 
to enhance AI model performance. By focusing on these 
core areas, our contribution provides architects with action-
able guidance toward building secure and resilient synthetic

---

<!-- PAGE 22 -->

7  Page 22 of 28

Electronic Markets (2025) 35:7

-
c
i
d
e
r
p

g
n
i
z
i
m
i
x
a
m
-
y
t
i
l
i
t
u

,
y
t
i
l
a
u
q
-
h
g
i
h
f
o

n
o
i
t
a
r
e
n
e
g

f
o

e
c
n
a
m
r
o
f
r
e
p
t
u
o
(

g
n
i
l
p
m
a
s
r
e
v
o

f
o

s
e
e
r
g
e
d

t
n
e
r
e
ff
i
d

s
l
e
d
o
m
n
o
i
t

t
o
n

o
t

d
e
r
a
p
m
o
c

%
5
.
7

*

y
b

g
n
i
l
p
m
a
s
r
e
v
o
%
0
1

h
t
i

w
a
t
a
d

)
e
n
i
l
e
s
a
b

d
e
l
p
m
a
s
r
e
v
o

*

%
8
.
9
4

s
’
m
e
t
s
y
s
o
c
e

e
h
t

g
n
i
n
e
d
a
o
r
b

d
e
fi

i
t
n
e
d
i

e
r
e
w
s
e
i
g
e
t
a
r
t
s

n
o
i
t
a
r
g
e
t
n
i

a
t
a
d
l
a
m

i
t
p
o

,
r
e
h
t
r
u
F

.
s
r
e
y
a
l

l
a
b
o
l
g

d
n
a

l
a
c
o
l

-

m
o
c

)
l
e
d
o
m

t
s
e
b

t
x
e
n

o
t

d
e
r
a
p

y
b
E
A
V
T
f
o

e
c
n
a
m
r
o
f
r
e
p
t
u
o
(

a
t
a
d

n
o
i
t

e
c
n
a
m
r
o
f
r
e
p

e
c
n
a
h
n
e

o
t

a
t
a
d

c
i
t
e
h
t
n
y
s

g
n
i
t
a
r
e
n
e
g

n
e
e
w
t
e
b

s
e
t
a
r
a
p
e
s

y
l
r
a
e
l
c

t
a
h
t

h
c
a
o
r
p
p
a

c
i
t
s
o
n
g
a
-
m
h
t
i
r

-
c
a
s
n
a
r
t

l
a
i
c
n
a
n
fi
d
l
r
o
w

-
l
a
e
r

n
o

s
m
h
t
i
r
o
g
l
a

n
o
i
t
a
r
e
n
e
g

r
o
f

p
u
t
e
s

l
a
m

i
t
p
o

e
h
t

d
n
a
m
h
t
i
r
o
g
l
a

n
o
i
t
a
r
e
n
e
g

a
t
a
d

l
a
i
t
n
e
t
o
p

e
c
n
a
m
r
o
f
r
e
p
s
t
i

g
n
i
c
n
a
h
n
e

d
n
a

y
t
i
l
i
b
a
c
i
l
p
p
a

-
t
a
r
e
n
e
g

n
e
h
w
p
u
t
e
s

g
n
i
n
i
a
r
t

l
a
m

i
t
p
o

e
h
t

f
o

n
o
i
t
a
u
l
a
v
E
-

t
x
e
n

o
t

d
e
r
a
p
m
o
c

*

%
0
.
2

y
b

s
l
e
d
o
m
d
e
t
a
r
a
p
e
s
-
s
s
a
l
c

)
e
m
e
h
c
s

g
n
i
n
i
a
r
t

t
s
e
b

d
e
n
i
a
r
t
-
e
r
p

f
o

e
c
n
a
m
r
o
f
r
e
p
t
u
o
(

a
t
a
d

c
i
t
e
h
t
n
y
s

g
n
i

c
fi
i
c
e
p
s

e
h
t

e
t
a
d
o
m
m
o
c
c
a

t
a
h
t

s
e
h
c
a
o
r
p
p
a

g
n
i
n
i
a
r
t

l
e
v
e
l

l
a
n
o
i
t
u
t
i
t
s
n
i

e
h
t

n
o

a
t
a
d

c
i
t
e
h
t
n
y
s

d
n
a

l
a
e
r

n
i

y
l
l
a
i
c
e
p
s
e

,
n
o
i
t
a
r
e
n
e
g

a
t
a
d

c
i
t
e
h
t
n
y
s

r
o
f

s
p
u
t
e
s

e
h
t

g
n
i
r
u
s
n
e

,
s
t
n
a
p
i
c
i
t
r
a
p

s
’
m
e
t
s
y
s
o
c
e

e
h
t

f
o

s
d
e
e
n

g
n
i
s
u

a
t
a
d

c
i
t
e
h
t
n
y
s

y
l
e
r
u
p

f
o

n
o
i
t
a
u
l
a
v
e

e
c
n
a
m
r
o
f
r
e
P
-

s
e
s
s
a
l
c

d
e
c
n
a
l
a
b
m

i

h
t
i

w
s
t
x
e
t
n
o
c

d
e
r
o
l
i
a
t

f
o

n
o
i
t
a
c
fi

i
t
n
e
d
i

e
h
t

e
t
a
t
i
l
i
c
a
f

s
n
o
i
t
a
g
i
t
s
e
v
n
i

e
s
e
h
T

n
e
e
w
t
e
b

e
g
a
t
n
e
c
r
e
p

n
i
-
x
i
m

l
a
m

i
t
p
o

e
h
t

f
o

n
o
i
t
a
u
l
a
v
E
-

g
n
i
n
i
a
r
t

f
o
s
c
fi
i
c
e
p
s

e
h
t

n
o

s
e
s
u
c
o
f

n
o
i
s
n
e
m
i
d

s
i
h
T

n
o
i
t
c
i
d
e
r
P

-
o
g
l
a

,
r
a
l
u
d
o
m
a

f
o

n
o
i
t
c
e
l
e
s

e
h
t
o
t

d
a
e
l

s
e
s
y
l
a
n
a

e
h
T

a
t
a
d

c
i
t
e
h
t
n
y
s

r
a
l
u
p
o
p

f
o

n
o
s
i
r
a
p
m
o
c

e
c
n
a
m
r
o
f
r
e
P
-

c
i
t
e
h
t
n
y
s

e
l
b
a
t
i
u
s

t
s
o
m
e
h
t

s
e
fi

i
t
n
e
d
i

n
o
i
s
n
e
m
i
d

s
i
h
T

n
o
i
t
a
r
e
n
e
G

g
n
i
n
o
s
a
e
R

s
e
i
t
i
v
i
t
c
A

s
u
c
o
F

t
h
g
i
s
n
i

f
o

a
e
r
A

s
e
l
c
y
c

e
t
a
u
l
a
v
e
-
t
n
e
m
e
l
p
m

i
-
n
g
i
s
e
d

r
u
o
f

e
h
t

n
i

d
e
t
a
r
e
n
e
g
s
t
h
g
i
s
n
i

f
o

y
r
a
m
m
u
S

9
e
l
b
a
T

d
n
a

y
t
i
l
i
b
a
i
v
s
m
e
t
s
y
s

'

e
h
t

g
n
i
r
u
s
n
e

,
s
u
h
T

.
s
t
n
e
m
e
v
o
r
p
m

i

t
n
a
c
fi
i
n
g
i
s
(

s
n
o
i
t
u
t
i
t
s
n
i

g
n
i
t
a
p
i
c
i
t
r
a
p

f
o
s
r
e
b
m
u
n

g
n
i

e
c
n
a
m
r
o
f
r
e
p
l
a
i
t
n
a
t
s
b
u
s

s
d
l
e
i
y

n
o
i
t
a
p
i
c
i
t
r
a
p
m
e
t
s
y
s

-
y
r
a
v

h
t
i

w
e
c
n
a
m
r
o
f
r
e
p

s
’
m
e
t
s
y
s
o
c
e

e
h
t

f
o

n
o
i
t
a
u
l
a
v
E
-

s
s
e
n
e
v
i
t
c
a
r
t
t
a

)
s
e
z
i
s
m
e
t
s
y
s
o
c
e

l
l
a

h
t
i

w
n
i
a
g

e
c
n
a
m
r
o
f
r
e
p

-
o
c
e

l
a
i
t
r
a
p

n
e
v
e

,
e
r
o
m
r
e
h
t
r
u
F

.
s
n
o
i
t
u
t
i
t
s
n
i

r
e
l
l
a
m
s

)
9
0
.
0
−

f
o

n
o
i
t
a
l
e
r
r
o
c

e
v
i
t
a
g
e
n
(

n
i
a
g

e
c
n
a
m
r
o
f
r
e
p

n
o
i
t
a
p
i
c
i
t
r
a
p

l
a
i
t
r
a
p

f
o

t
c
e
ff
e

e
h
t

d
n
a

s
e
z
i
s

g
n
i
y
r
a
v

r
o
f

s
e
g
a
t
n
a
v
d
a

r
a
l
u
c
i
t
r
a
p

g
n
i
t
h
g
i
l
h
g
i
h

,

m
e
t
s
y
s
o
c
e

d
n
a

e
z
i
s

n
o
i
t
u
t
i
t
s
n
i

n
e
e
w
t
e
b

p
i
h
s
n
o
i
t
a
l
e
r

e
h
t

d
n
a

n
o
i
t

f
o
s
n
o
i
t
u
t
i
t
s
n
i

s
s
o
r
c
a

s
e
v
i
t
n
e
c
n
i

n
o
i
t
a
p
i
c
i
t
r
a
p

f
o

s
m
r
e
t

e
h
t

s
s
o
r
c
a

t

fi
e
n
e
b

l
a
n
o
i
t
r
o
p
o
r
p

a

e
t
a
c
i
d
n
i

s
g
n
i
d
n
fi
e
h
T

-
u
t
i
t
s
n
i

l
a
i
c
n
a
n
fi
r
e
p

n
i
a
g

e
c
n
a
m
r
o
f
r
e
p

f
o
s
i
s
y
l
a
n
A

-

n
i

e
c
n
a
l
a
b
s
’
m
e
t
s
y
s
o
c
e

e
h
t

s
e
s
s
e
s
s
a

n
o
i
s
n
e
m
i
d

s
i
h
T

m
e
t
s
y
s
o
c
E

w
e
n

o
t

p
u
t
e
s

g
n
i
r
a
h
s

a
t
a
d

c
i
t
e
h
t
n
y
s

e
h
t

f
o

r
e
f
s
n
a
r
T
-

l
a
i
c
n
a
n
fi
e
l
p
i
t
l
u
m
s
s
o
r
c
a

e
g
d
e
l
w
o
n
k

n
g
i
s
e
d

e
h
t

f
o

y
t
i

-
e
r
c

e
h
t

e
t
a
d
i
l
a
v

o
t

s
t
r
e
p
x
e

c
i
m
e
d
a
c
a

d
n
a

s
n
o
i
t
u
t
i
t
s
n
i

e
r
u
t
c
e
t
i
h
c
r
a
m
e
t
s
y
s

d
n
a

e
g
d
e
l
w
o
n
k

n
g
i
s
e
d

d
e
t
a
e
r
c

-
l
i
b
a
c
i
l
p
p
a

d
n
a

e
c
n
a
v
e
l
e
r

e
h
t

d
e
m
r
fi
n
o
c

n
o
i
t
a
u
l
a
v
e

e
h
T

l
a
i
c
n
a
n
fi
m
o
r
f

s
t
r
e
p
x
e

h
t
i

w
s
w
e
i
v
r
e
t
n
i

d
e
r
u
t
c
u
r
t
s
-
i

m
e
S
-

e
h
t

e
t
a
d
i
l
a
v

o
t

s
m
i
a

y
t
i
l
i
b
a
z
i
l
a
r
e
n
e
g

f
o

n
o
i
s
n
e
m
i
d

e
h
T

y
t
i
l
i
b
a
z
i
l
a
r
e
n
e
G

s
n
i
a
m
o
d

s
e
c
i
v
r
e
s

e
r
u
t
c
e
t
i
h
c
r
a
m
e
t
s
y
s

d
n
a

s
P
D
d
e
t
a

s
e
v
i
t
c
e
p
s
r
e
p

’
s
t
r
e
p
x
e

d
n
a

s
t
x
e
t
n
o
c

e
s
r
e
v
i
d

s
s
o
r
c
a

-
a
t
a
d

d
e
s
a
b
-
n
o
i
t
a
l
u
m
i
s

g
n
i
s
u

)

%
6
.
6

*

e
c
n
a
m
r
o
f
r
e
p

d
e
v
o
r
p
m

i
(

n
o
i
t
c
e
t
e
d

d
u
a
r
f

e
k
i
l

s
t
x
e
t
n
o
c

d
e
v
o
r
p
m

i
(

n
o
i
t
c
e
t
e
d

g
n
i
r
e
d
n
u
a
l

y
e
n
o
m
d
n
a

)

%
6
.
3

y
b

*

y
b

e
c
n
a
m
r
o
f
r
e
p

s
t
e
s

s
e
r
o
c
s
C
U
A
C
O
R
n
o

d
e
s
a
b

n
o
i
t
a
u
l
a
v
e

e
c
n
a
m
r
o
f
r
e
 P
*

---

<!-- PAGE 23 -->

Electronic Markets (2025) 35:7

Page 23 of 28  7

data-sharing ecosystems. This framework, therefore, serves 
as a blueprint for future system designers working within 
regulated environments where data privacy and AI perfor-
mance are essential.

Limitations and future research opportunities can be iden-
tified across our four key areas of insight. Regarding data 
generation, the current study was constrained by the avail-
able data, which prevented the consideration of advanced 
graph-based  synthetic  data  generation  methods  such  as 
TransGAN (X. Wang & Yang, 2024). Additionally, while 
privacy was tested, it was not fully guaranteed by the mod-
els used, highlighting the need for future research on the 
effectiveness of differentially private synthetic data genera-
tion methods such as PATEGAN (Jordon et al., 2018) in 
a synthetic data ecosystem. From a prediction standpoint, 
further investigation is required to determine how models 
can be aligned when data schemas—and thus the synthetic 
data—differ between institutions. Moreover, the design of 
an effective back-testing mechanism to ensure the ecosys-
tem’s predictive performance should be explored. On the 
ecosystem level, additional research is necessary to explore 
ecosystem usage incentives, building on the work by (Gel-
haar et al., 2021), which was beyond the scope of this paper. 
Finally, while this study was limited to financial services due 
to resource constraints, future research should explore the 
applicability of the defined DPs beyond this domain, testing 
their general applicability.

Conclusion

Based on the need for increased data availability to foster 
economic growth, this paper provides the design and evalu-
ation of a synthetic data-sharing ecosystem for financial 
institutions under privacy constraints. The main contribution 
lies in providing guidance on how to train models based on 
shared data. By formulating a set of DPs, practical insights, 
and prototype testing, iterative design cycles were used to 
provide a robust framework for constructing a data ecosys-
tem that leverages synthetic data. Each DP, from ensuring 
data quality and enhancing adaptability through transforma-
tion and resampling to fostering trust among ecosystem par-
ticipants and facilitating regulatory access to synthetic data, 
extends existing research on synthetic data sharing and gen-
eration, particularly in the context of financial transaction 
data. For practice, our example instantiation and codebase 
can be used as a reference architecture for future instantia-
tions. We not only address the identified need for an efficient, 
privacy-preserving financial data ecosystem but also set a 
foundation for future exploration in broader domains where 
data sharing under privacy restrictions is paramount. Thus, 
this contribution offers guidance for overcoming technical, 
trust-related, and regulatory challenges in data ecosystems,

unlocking the potential for data-driven innovation and future 
economic development.

Acknowledgements  The authors express their gratitude to the Union-
Bank of the Philippines for their valuable collaboration and the provi-
sion of key insights that contributed to this research. This research pro-
ject was funded by the St. Gallen Symposium and the German Federal 
Ministry of Education and Research (BMBF) within the “Innovations 
for Tomorrow’s Production, Services, and Work” Program (funding 
number 02K23A001) which is managed by the Project Management 
Agency Karlsruhe (PTKA). The authors are responsible for the content 
of this publication.

Funding  Open access funding provided by University of St. Gallen.

Data Availability  The datasets used during the current study are avail-
able in the Kaggle repositories: https:// www. kaggle. com/c/ ieee- fraud- 
detec tion, https:// www. kaggle. com/ datas ets/ ealtm an2019/ ibm- trans  
actio ns- for- anti- money- laund ering- aml, https:// www. kaggle. com/ datas 
ets/ ealtm an2019/ credit- card- trans actio ns.

Declarations

Competing Interests  The authors declare that they have no conflict 
of interest.

Open Access   This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, 
provide a link to the Creative Commons licence, and indicate if changes 
were made. The images or other third party material in this article are 
included in the article's Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in 
the article's Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a 
copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

References

Abbas, A. E., Agahari, W., van de Ven, M., Zuiderwijk, A., & de 
Reuver, M. (2021). Business data sharing through data market-
places: A systematic literature review. Journal of Theoretical and 
Applied Electronic Commerce Research, 16(7), 7. https:// doi. org/ 
10. 3390/ jtaer 16070 180

Abdul Salam, M., Fouad, K. M., Elbably, D. L., & Elsayed, S. M. 
(2024). Federated learning model for credit card fraud detec-
tion with data balancing techniques. Neural Computing and 
Applications,  36(11),  6231–6256.  https:// doi. org/ 10. 1007/  
s00521- 023- 09410-2

Adner, R. (2017). Ecosystem as structure: An actionable construct for 
strategy. Journal of Management, 43(1), 39–58. https:// doi. org/ 
10. 1177/ 01492 06316 678451

Al-Hashedi, K. G., & Magalingam, P. (2021). Financial fraud detection 
applying data mining techniques: A comprehensive review from 
2009 to 2019. Computer Science Review, 40, 100402. https:// doi. 
org/ 10. 1016/j. cosrev. 2021. 100402

Altman, E., Blanuša, J., von Niederhäusern, L., Egressy, B., Anghel, 
A., & Atasu, K. (2024). Realistic synthetic financial transac-
tions for anti-money laundering models (No. arXiv: 2306. 16424). 
arXiv. https:// doi. org/ 10. 48550/ arXiv. 2306. 16424

---

<!-- PAGE 24 -->

7  Page 24 of 28

Electronic Markets (2025) 35:7

Altman, E. R. (2019). Synthesizing credit card transactions (No.

arXiv: 1910. 03033).  arXiv. https:// doi. org/ 10. 48550/ arXiv.
1910. 03033

Asrow, K. (2021). The role of individuals in the data ecosystem: Cur-
rent debates and considerations for individual data protection 
and data rights in the U.S. Federal Reserve Bank of San Fran-
cisco. https:// priva cysec urity acade my. com/ wp- conte nt/ uploa ds/ 
2021/ 05/ The- Role- of- Indiv iduals- in- the- Data- Ecosy  stem. pdf. 
Accessed 9 Mar 2023.

Assefa, S. (2020). Generating synthetic data in finance: Opportunities, 
challenges and pitfalls. SSRN Electronic Journal. https:// doi. org/ 
10. 2139/ ssrn. 36342 35

Aurna, N. F., Hossain, M. D., Taenaka, Y., & Kadobayashi, Y. (2023). 
Federated learning-based credit card fraud detection: Perfor-
mance analysis with sampling methods and deep learning algo-
rithms. 2023 IEEE International Conference on Cyber Security 
and Resilience (CSR), 2023, 180–186. https:// doi. org/ 10. 1109/ 
CSR57 506. 2023. 10224 978

Autio, E., spsampsps Thomas, L. D. W. (2014). Innovation ecosystems: 
Implications for innovation management? In M. Dodgson, D. M. 
Gann, spsampsps N. Phillips (Eds.), The Oxford Handbook of 
Innovation Management (p. 0). Oxford University Press. https:// 
doi. org/ 10. 1093/ oxfor dhb/ 97801 99694 945. 013. 012

Awosika, T., Shukla, R. M., & Pranggono, B. (2024). Transparency 
and privacy: The role of explainable AI and federated learning in 
financial fraud detection. IEEE Access, 12, 64551–64560. https:// 
doi. org/ 10. 1109/ ACCESS. 2024. 33945 28. IEEE Access.
Baabdullah, T., Alzahrani, A., Rawat, D. B., & Liu, C. (2024). Effi-
ciency of federated learning and blockchain in preserving privacy 
and enhancing the performance of credit card fraud detection 
(CCFD) systems. Future Internet, 16(6), 6. https:// doi. org/ 10.  
3390/ fi160 60196

Bagad,  P.,  Mitra,  S.,  Dhamnani,  S.,  Sinha,  A.  R.,  Gautam,  R.,  & 
Khanna, H. (2021). Data-sharing economy: Value-addition from 
data meets privacy. Proceedings of the 14th ACM International 
Conference on Web Search and Data Mining, 1105–1108. https:// 
doi. org/ 10. 1145/ 34379 63. 34417 12

Baskerville, R., Baiyere, A., Gregor, S., Hevner, A., & Rossi, M. 
(2018). Design science research contributions: Finding a bal-
ance between artifact and theory. Journal of the Association for 
Information Systems, 19(5). https:// aisel. aisnet. org/ jais/ vol19/  
iss5/3. Accessed 13 June 2023.

Bauer, A., Trapp, S., Stenger, M., Leppich, R., Kounev, S., Leznik, 
M., Chard, K., & Foster, I. (2024). Comprehensive explora-
tion of synthetic data generation: A survey (No. arXiv: 2401. 
02524). arXiv. https:// arxiv. org/ abs/ 2401. 02524. Accessed 15 
Aug 2024.

Benchaji, I., Douzi, S., & Ouahidi, B. E. (2021). Credit card fraud 
detection model based on LSTM recurrent neural networks. 
Journal of Advances in Information Technology, 12(2), 113–118. 
https:// doi. org/ 10. 12720/ jait. 12.2. 113- 118

Bian, K., & Zheng, H. (2023). FedAvg-DWA: A novel algorithm for 
enhanced fraud detection in federated learning environment. 
2023 4th International Conference on Big Data, Artificial Intel-
ligence and Internet of Things Engineering (ICBAIE), 13–17. 
https:// doi. org/ 10. 1109/ ICBAI E59714. 2023. 10281 317

Blake, M., McWaters, J., & Galaski, R. (2019). The next generation of 
data-sharing in financial services (p. 33) [White Paper]. World 
Economic Forum. https:// www2. deloi tte. com/ conte nt/ dam/ Deloi 
tte/ lu/ Docum ents/ finan cial- servi ces/ lu- next- gener ation- data- 
shari nging- finan cial- servi ces. pdf. Accessed 29 Jan 2023.
Bonabeau, E. (2002). Agent-based modeling: Methods and techniques 
for  simulating  human  systems. Proceedings  of  the  National 
Academy of Sciences, 99(suppl_3), 7280–7287. https:// doi. org/ 
10. 1073/ pnas. 08208 0899

Brée, T., Karger, E., & Ahlemann, F. (2024). Shaping the future of data 
ecosystem research—What is still missing? IEEE Access, 12, 
103162–103175. IEEE Access. https:// doi. org/ 10. 1109/ ACCESS. 
2024. 34329 69

Brodsky, L., & Oakes, L. (2017). Data sharing and open banking. 
McKinsey. https:// www. mckin sey. com/ ~/ media/ McKin sey/ Indus 
tries/ Finan cial% 20Ser vices/ Our% 20Ins ights/ Data% 20sha ring% 
20and% 20open% 20ban king/ Data- shari ng- and- open- banki ng. pdf. 
Accessed 26 Feb 2024.

Bun, M., Desfontaines, D., Dwork, C., Naor, M., Nissim, K., Roth, A., 
Smith, A., Steinke, T., Ullman, J., & Vadhan, S. (2021). Statis-
tical inference is not a privacy violation. https:// diffe renti alpri 
vacy. org/ infer ence- is- not-a- priva cy- viola tion/. Accessed 14 Aug 
2024.

Cappiello, C., Gal, A., Jarke, M., & Rehof, J. (2020). Data ecosystems: 
Sovereign data exchange among organizations (Dagstuhl Semi-
nar 19391). DROPS-IDN/v2/Document/https:// doi. org/ 10. 4230/ 
DagRep. 9.9. 66. https:// doi. org/ 10. 4230/ DagRep. 9.9. 66
Chakravarty, S., Demirhan, H., & Baser, F. (2020). Fuzzy regres-
sion functions with a noise cluster and the impact of outliers on 
mainstream machine learning methods in the regression setting. 
Applied Soft Computing, 96, 106535. https:// doi. org/ 10. 1016/j. 
asoc. 2020. 106535

Chandra, L., Seidel, S., & Gregor, S. (2015). Prescriptive knowledge in 
IS research: Conceptualizing design principles in terms of mate-
riality, action, and boundary conditions. 2015 48th Hawaii Inter-
national Conference on System Sciences, 4039–4048. https:// doi. 
org/ 10. 1109/ HICSS. 2015. 485

Charitou, C., Dragicevic, S., & Garcez, A. d’Avila. (2021). Synthetic 
data generation for fraud detection using GANs (No. arXiv: 2109. 
12546). arXiv. http:// arxiv. org/ abs/ 2109. 12546. Accessed 11 Mar 
2024.

Chatterjee, P., Das, D., & Rawat, D. B. (2024). Digital twin for credit 
card fraud detection: Opportunities, challenges, and fraud detec-
tion advancements. Future Generation Computer Systems, 158, 
410–426. https:// doi. org/ 10. 1016/j. future. 2024. 04. 057

Chen, Z., Van Khoa, L. D., Teoh, E. N., Nazir, A., Karuppiah, E. K., & 
Lam, K. S. (2018). Machine learning techniques for anti-money 
laundering (AML) solutions in suspicious transaction detection: 
A review. Knowledge and Information Systems, 57(2), 245–285. 
https:// doi. org/ 10. 1007/ s10115- 017- 1144-z

Chen, H., Grossman, M., Sen, A., & Tsao, S.-F. (2023). Establish-
ing a FAIR, CARE, and efficient synthetic health data shar-
ing ecosystem for canada establishing a FAIR, CARE, and 
efficient synthetic health data sharing ecosystem for Canada. 
IARIW-CIGI Conference on the Valuation of Data. https:// 
www. resea rchga te. net/ publi cation/ 37544 6378_ Estab lishi 
ng_a_ FAIR_ CARE_ and_ Effic ient_ Synth etic_ Health_ Data_  
Shari ng_ Ecosy  stem_ for_ Canada_ Estab lishi ng_a_ FAIR_  
CARE_ and_ Effic ient_ Synth etic_ Health_ Data_ Shari ng_ Ecosy  
stem_ for_ Canada. Accessed 17 Dec 2024

Choi, E., Biswal, S., Malin, B., Duke, J., Stewart, W. F., & Sun, J. 
(2018). Generating multi-label discrete patient records using 
generative adversarial networks (No. arXiv: 1703. 06490). arXiv. 
https:// doi. org/ 10. 48550/ arXiv. 1703. 06490

Cosma, S., Cosma, S., & Pennetta, D. (2023). The rise of financial ser-
vices ecosystems: Towards open banking platforms. In T. Walker, 
E. Nikbakht, & M. Kooli (Eds.), The Fintech Disruption: How 
Financial Innovation Is Transforming the Banking Industry (pp. 
191–213). Springer International Publishing. https:// doi. org/ 10. 
1007/ 978-3- 031- 23069-1_8

Dahmen, J., & Cook, D. (2019). SynSys: A synthetic data generation 
system for healthcare applications. Sensors, 19(5), 5. https:// doi. 
org/ 10. 3390/ s1905 1181

Dankar, F. K., Ibrahim, M. K., & Ismail, L. (2022). A multi-dimen-
sional evaluation of synthetic data generators. IEEE Access, 10,

---

<!-- PAGE 25 -->

Electronic Markets (2025) 35:7

Page 25 of 28  7

11147–11158. https:// doi. org/ 10. 1109/ ACCESS. 2022. 31447 65. 
IEEE Access.

Demirgüç-Kunt, A., Klapper, L., Singer, D., & Ansar, S. (2022). The 
global findex database 2021—Financial inclusion, digital pay-
ments, and resilience in the age of COVID-19. International Bank 
for Reconstruction and Development / The World Bank. https:// 
openk nowle dge. world bank. org/ bitst ream/ handle/ 10986/ 37578/ 
97814 64818 974. pdf. Accessed 22 Jan 2023.

Eilertsen, G., Tsirikoglou, A., Lundström, C., & Unger, J. (2021). 
Ensembles of GANs for synthetic training data generation (No. 
arXiv: 2104. 11797). arXiv. https:// doi. org/ 10. 48550/ arXiv. 2104. 
11797

Emam, K. E., Mosquera, L., & Bass, J. (2020). Evaluating identity 
disclosure risk in fully synthetic health data: Model development 
and validation. Journal of Medical Internet Research, 22(11), 
e23139. https:// doi. org/ 10. 2196/ 23139

Esteban, C., Hyland, S. L., & Rätsch, G. (2017). Real-valued (medi-
cal) time series generation with recurrent conditional GANs 
(No. arXiv: 1706. 02633). arXiv. http:// arxiv. org/ abs/ 1706. 02633. 
Accessed 14 Aug 2024.

European Central Bank. (2021). Seventh report on card fraud. 2021. 
https:// www. ecb. europa. eu/ pub/ cardf raud/ html/ ecb. cardf raudr  
eport 20211 0~cac4c 418e8. en. html. Accessed 16 June 2023.
Fan, X., Guo, X., Chen, Q., Chen, Y., Wang, T., & Zhang, Y. (2022). 
Data augmentation of credit default swap transactions based on 
a sequence GAN. Information Processing & Management, 59(3), 
102889. https:// doi. org/ 10. 1016/j. ipm. 2022. 102889

Fassnacht, M. K., Benz, C., Leimstoll, J., & Satzger, G. (2023). Is 
your organization ready to share? A framework of beneficial 
conditions for data sharing. 44th International Conference 
on  Information  Systems  (ICIS  2023),  Hyderabad,  Indien, 
10.12.2023 - 13.12.2023.  https:// doi. org/ 10. 5445/ IR/ 10001  
62812

Frid-Adar, M., Klang, E., Amitai, M., Goldberger, J., & Greenspan, H. 
(2018). Synthetic data augmentation using GAN for improved 
liver lesion classification. 2018 IEEE 15th International Sympo-
sium on Biomedical Imaging (ISBI 2018), 289–293. 2018 IEEE 
15th International Symposium on Biomedical Imaging (ISBI 
2018). https:// doi. org/ 10. 1109/ ISBI. 2018. 83635 76

Geisler, S., Vidal, M.-E., Cappiello, C., Lóscio, B. F., Gal, A., Jarke, 
M., Lenzerini, M., Missier, P., Otto, B., Paja, E., Pernici, B., & 
Rehof, J. (2021). Knowledge-driven data ecosystems toward data 
transparency. Journal of Data and Information Quality, 14(1), 
3:1-3:12. https:// doi. org/ 10. 1145/ 34670 22

Gelhaar, J., & Otto, B. (2020). Challenges in the emergence of data 
ecosystems. PACIS 2020 Proceedings. 175. https:// aisel. aisnet. 
org/ pacis 2020/ 175/. Accessed 17 Dec 2024.

Gelhaar, J., Groß, T., & Otto, B. (2021). A taxonomy for data eco-
systems. Hawaii International Conference on System Sciences. 
https:// doi. org/ 10. 24251/ HICSS. 2021. 739

Gelhaar, J., Henke, M., Gürpinar, T., & Otto, B. (2021). Towards a 
taxonomy of incentive mechanisms for data sharing in data eco-
systems. PACIS 2021 Proceedings. 121. https:// aisel. aisnet. org/ 
pacis 2021/ 121/. Accessed 17 Dec 2024.

Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, 
D., Ozair, S., Courville, A., & Bengio, Y. (2014). Generative 
adversarial networks (No. arXiv: 1406. 2661). arXiv. https:// doi. 
org/ 10. 48550/ arXiv. 1406. 2661

Gray, B., & Sites, J. P. (2013). Sustainability through partnerships. 
Network for business sustainability. https:// nbs. net/ wp- conte  
nt/ uploa ds/ 2022/ 01/ NBS- Syste matic- Review- Partn ershi ps. pdf. 
Accessed 18 Dec 2024.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design 
science research for maximum impact. MIS Quarterly, 37(2), 
337–355.

Gregor, S., Chandra Kruse, L., & Seidel, S. (2020). The anatomy of 
a design principle. Journal of the Association for Information 
Systems, 21, 1622–1652. https:// doi. org/ 10. 17705/ 1jais. 00649

Gregor, S., Kruse, L. C., & Seidel, S. (2020). Research perspectives: 
The anatomy of a design principle. Journal of the Association 
for Information Systems, 21(6). https:// doi. org/ 10. 17705/ 1jais.  
00649

Gröger, C. (2021). There is no AI without data. Communications of the 
ACM, 64(11), 98–108. https:// doi. org/ 10. 1145/ 34482 47
Hashemi, S. K., Mirtaheri, S. L., & Greco, S. (2023). Fraud detection 
in banking data by machine learning techniques. IEEE Access, 
11, 3034–3043. https:// doi. org/ 10. 1109/ ACCESS. 2022. 32322 87.
He, Z., Huang, J., & Zhou, J. (2023). Open banking: Credit market 
competition when borrowers own the data. Journal of Financial 
Economics, 147(2), 449–474. https:// doi. org/ 10. 1016/j. jfine co.  
2022. 12. 003

Heimstädt, M., Saunderson, F., & Heath, T. (2014). Conceptualizing 
Open Data ecosystems: A timeline analysis of Open Data devel-
opment in the UK. [13] S. https:// doi. org/ 10. 17169/ FUDOCS_ 
DOCUM ENT_ 00000 00203 32

Heinz, D., Benz, C., Fassnacht, M., & Satzger, G. (2022). Past, present 
and future of data ecosystems research: A systematic literature 
review. PACIS 2022 Proceedings. 46. https:// aisel. aisnet. org/  
pacis 2022/ 46/. Accessed 18 Dec 2024.

Hevner, A. R., March, S., Park, J., & Ram, S. (2004). Design science 
in information systems research. Management Information Sys-
tems Quarterly, 28(1). https:// aisel. aisnet. org/ misq/ vol28/ iss1/6. 
Accessed 13 Nov 2024.

Hevner, A., & Gregor, S. (2022). Envisioning entrepreneurship and 
digital innovation through a design science research lens: A 
matrix approach. Information & Management, 59(3), 103350. 
https:// doi. org/ 10. 1016/j. im. 2020. 103350

Hevner, A. R. (2007). A three cycle view of design science research. 
Scandinavian Journal of Information Systems: Vol. 19: Iss. 2, 
Article 4. https:// aisel. aisnet. org/ sjis/ vol19/ iss2/4/. Accessed 18 
Dec 2024.

Hilal, W., Gadsden, S. A., & Yawney, J. (2022). Financial fraud: A 
review of anomaly detection techniques and recent advances. 
Expert Systems with Applications, 193, 116429. https:// doi. org/ 
10. 1016/j. eswa. 2021. 116429

Hittmeir, M., Ekelhart, A., & Mayer, R. (2019). On the utility of syn-
thetic data: An empirical evaluation on machine learning tasks. 
Proceedings of the 14th International Conference on Availability, 
Reliability and Security, 1–6. https:// doi. org/ 10. 1145/ 33392 52. 
33392 81

Iivari, J. (2007). A paradigmatic analysis of information systems as a 
design science. Scandinavian Journal of Information Systems, 
19, 39.

Immonen, A., Palviainen, M., & Ovaska, E. (2014). Requirements of 
an open data based business ecosystem. IEEE Access, 2, 88–103. 
https:// doi. org/ 10. 1109/ ACCESS. 2014. 23028 72

Ishfaq,  H.,  Hoogi,  A.,  &  Rubin,  D.  (2023).  TVAE:  Triplet-based 
variational autoencoder using metric learning (No. arXiv: 1802. 
04403). arXiv. https:// arxiv. org/ abs/ 1802. 04403 . Accessed 16 
June 2023.

Jarke, M. (2017). Data spaces: Combining goal-driven and data-driven 
approaches in community decision and negotiation support. In 
M. Schoop spsampsps D. M. Kilgour (Eds.), Group Decision 
and  Negotiation.  A  Socio-Technical  Perspective  (pp.  3–14). 
Springer  International  Publishing.  https:// doi. org/ 10. 1007/  
978-3- 319- 63546-0_1

Jensen, R. I. T., Ferwerda, J., Jørgensen, K. S., Jensen, E. R., Borg, M., 
Krogh, M. P., Jensen, J. B., & Iosifidis, A. (2023). A synthetic 
data set to benchmark anti-money laundering methods. Scientific 
Data, 10(1), 661. https:// doi. org/ 10. 1038/ s41597- 023- 02569-2

---

<!-- PAGE 26 -->

7  Page 26 of 28

Electronic Markets (2025) 35:7

Jiang, D., Zhang, G., Karami, M., Chen, X., Shao, Y., & Yu, Y. (2022). 
DP$^2$-VAE:  Differentially  private  pre-trained  variational 
autoencoders (No. arXiv: 2208. 03409). arXiv. https:// doi. org/  
10. 48550/ arXiv. 2208. 03409

Jones, D., & Gregor, S. (2007). The anatomy of a design theory. Jour-
nal of the Association for Information Systems, 8(5), 1.

Jordon, J., Yoon, J., & Schaar, M. van der. (2018, September 27). 
PATE-GAN: Generating synthetic data with differential privacy 
guarantees. International Conference on Learning Representa-
tions. https:// openr eview. net/ forum? id= S1zk9 iRqF7. Accessed 
14 Aug 2024.

Jordon, J., Szpruch, L., Houssiau, F., Bottarelli, M., Cherubin, G., 
Maple, C., Cohen, S. N., & Weller, A. (2022). Synthetic data—
What, why and how? (No. arXiv: 2205. 03257). arXiv. http:// arxiv. 
org/ abs/ 2205. 03257. Accessed 14 Aug 2024.

Kingma,  D.  P.,  &  Welling,  M.  (2013).  Auto-encoding  variational 
Bayes.  CoRR.  https:// www. seman ticsc holar. org/ paper/ Auto- 
Encod ing- Varia tional- Bayes- Kingma- Welli ng/ 5f5dc 5b9a2 ba710 
937e2 c413b 37b05 3cd67 3df02. Accessed 16 May 2024.

Kiran, A., & Kumar, S. S. (2024). A methodology and an empirical 
analysis to determine the most suitable synthetic data genera-
tor. IEEE Access, 12, 12209–12228. https:// doi. org/ 10. 1109/ 
ACCESS. 2024. 33542 77

Kong, Y., Li, Z., & Jiang, C. (2024). ASIA: A federated boosting tree 
model against sequence inference attacks in financial networks. 
IEEE Transactions on Information Forensics and Security, 19, 
6991–7004. IEEE Transactions on Information Forensics and 
Security. https:// doi. org/ 10. 1109/ TIFS. 2024. 34284 12

Kulatilleke, G. K. (2022). Challenges and complexities in machine 
learning based credit card fraud detection (No. arXiv: 2208. 
10943). arXiv. http:// arxiv. org/ abs/ 2208. 10943. Accessed 18 
Mar 2024.

Langer, A., spsampsps Mukherjee, A. (2023). Organizing the data eco-
system. In A. Langer spsampsps A. Mukherjee (Eds.), Develop-
ing a path to data dominance: Strategies for digital data-centric 
enterprises (pp. 113–141). Springer International Publishing. 
https:// doi. org/ 10. 1007/ 978-3- 031- 26401-6_5

Langevin, A., Cody, T., Adams, S., & Beling, P. (2022). Generative 
adversarial networks for data augmentation and transfer in credit 
card fraud detection. Journal of the Operational Research Soci-
ety, 73(1), 153–180. https:// doi. org/ 10. 1080/ 01605 682. 2021.  
18802 96

Lebichot, B., Verhelst, T., Le Borgne, Y.-A., He-Guelton, L., Oble, F., 
& Bontempi, G. (2021). Transfer learning strategies for credit 
card fraud detection. IEEE Access, 9, 114754–114766. https:// 
doi. org/ 10. 1109/ ACCESS. 2021. 31044 72.

Lei, Y.-T., Ma, C.-Q., Ren, Y.-S., Chen, X.-Q., Narayan, S., & Huynh, 
A.  N.  Q.  (2023).  A  distributed  deep  neural  network  model 
for credit card fraud detection. Finance Research Letters, 58, 
104547. https:// doi. org/ 10. 1016/j. frl. 2023. 104547

Levi, M. (1998). Organising plastic fraud: Enterprise criminals and 
the side-stepping of fraud prevention. The Howard Journal of 
Criminal Justice, 37(4), 423–438. https:// doi. org/ 10. 1111/ 1468- 
2311. 00110

Lipton, Z. C., Berkowitz, J., & Elkan, C. (2015). A critical review 
of recurrent neural networks for sequence learning (No. arXiv: 
1506. 00019). arXiv. https:// doi. org/ 10. 48550/ arXiv. 1506. 00019
Liu, X., Iftikhar, N., Huo, H., Li, R., & Nielsen, P. S. (2019). Two 
approaches for synthesizing scalable residential energy consump-
tion data. Future Generation Computer Systems, 95, 586–600. 
https:// doi. org/ 10. 1016/j. future. 2019. 01. 045

Longadge, R., & Dongre, S. (2013). Class imbalance problem in data 
mining review (No. arXiv: 1305. 1707). arXiv. https:// doi. org/ 10. 
48550/ arXiv. 1305. 1707

Lopez-Rojas, E. A., & Axelsson, S. (2012). Money laundering detec-
tion  using  synthetic  data.  Linköping  Electronic  Conference

Proceedings 71(5), 33–40. https:// ep. liu. se/ en/ confe rence- artic  
le. aspx? Artic le_ No= 5& issue= 71& series= ecp. Accessed 18 Dec 
2024.

Lopez-Rojas, E. A., Elmir, A., & Axelsson, S. (2016). PaySim: A 
financial mobile money simulator for fraud detection. European 
Modeling and Simulation Symposium 2016. https:// www. msc- 
les. org/ proce edings/ emss/ 2016/ EMSS2 016_ 249. pdf. Accessed 
18 Dec 2024.

Loukides,  G.,  Gkoulalas-Divanis,  A.,  spsampsps  Shao,  J.  (2010). 
Anonymizing transaction data to eliminate sensitive inferences. 
In P. G. Bringas, A. Hameurlain, spsampsps G. Quirchmayr 
(Eds.), Database and Expert Systems Applications (pp. 400–
415). Springer. https:// doi. org/ 10. 1007/ 978-3- 642- 15364-8_ 34

Lu, Y., Wang, H., & Wei, W. (2023). Machine learning for synthetic 
data  generation:  A  review  (No.  arXiv: 2302. 04062).  arXiv. 
https:// doi. org/ 10. 48550/ arXiv. 2302. 04062

Majava, J., Kinnunen, T., Foit, D., & Kess, P. (2016). An intermediary 
as a trust enabler in a spatial business ecosystem. International 
Journal of Innovation and Learning, 20(2), 199. https:// doi. org/ 
10. 1504/ IJIL. 2016. 077845

Major, T., & Mangano, J. (2020). Modernising payments messaging: 
The ISO 20022 standard. Reserve Bank of Australia. https:// 
www. rba. gov. au/ publi catio ns/ bulle  tin/ 2020/ sep/ pdf/ moder  nis-
ing- payme nts- messa ging- the- iso- 20022- stand ard. pdf. Accessed 
18 Dec 2024.

March,  S.  T.,  &  Smith,  G.  F.  (1995).  Design  and  natural  science 
research on information technology. Decision Support Systems, 
15(4), 251–266. https:// doi. org/ 10. 1016/ 0167- 9236(94) 00041-2
Morley-Fletcher, E. (2022). New solutions to biomedical data shar-
ing data sharing: Secure computation secure computationsand 
synthetic data synthetic data. In C. Beneduce spsampsps M. 
Bertolaso (Eds.), Personalized Medicine in the Making: Philo-
sophical Perspectives from Biology to Healthcare (pp. 173–189). 
Springer  International  Publishing.  https:// doi. org/ 10. 1007/  
978-3- 030- 74804-3_9

Mullarkey, M. T., & Hevner, A. R. (2019). An elaborated action design 
research process model. European Journal of Information Sys-
tems, 28(1), 6–20. https:// doi. org/ 10. 1080/ 09600 85X. 2018. 14518 
11

Myalil, D., Rajan, M. A., Apte, M., & Lodha, S. (2021). Robust collab-
orative fraudulent transaction detection using federated learning. 
2021 20th IEEE International Conference on Machine Learning 
and Applications (ICMLA), 373–378. https:// doi. org/ 10. 1109/  
ICMLA 52953. 2021. 00064

Nickerson, K., Tricco, T., Kolokolova, A., Shoeleh, F., Robertson, 
C., Hawkin, J., spsampsps Hu, T. (2023). Banksformer: A deep 
generative model for synthetic transaction sequences. In M.-R. 
Amini, S. Canu, A. Fischer, T. Guns, P. Kralj Novak, spsampsps 
G. Tsoumakas (Eds.), Machine Learning and Knowledge Discov-
ery in Databases (pp. 121–136). Springer Nature Switzerland. 
https:// doi. org/ 10. 1007/ 978-3- 031- 26422-1_8

O’Leary, K., O’Reilly, P., Nagle, T., Filelis-Papadopoulos, C., & 
Dehghani, M. (2021). The sustainable value of open banking: 
Insights from an open data lens. Hawaii International Con-
ference on System Sciences. https:// doi. org/ 10. 24251/ HICSS.  
2021. 713.

Oliveira, M. I. S., & Lóscio, B. F. (2018). What is a data ecosystem? 
Proceedings of the 19th Annual International Conference on 
Digital Government Research: Governance in the Data Age, 
1–9. https:// doi. org/ 10. 1145/ 32092 81. 32093 35.

Oliveira, M. I. S., & de Barros LimaFariasLóscio, G. F. B. (2019). 
Investigations into data ecosystems: A systematic mapping study. 
Knowledge and Information Systems, 61(2), 589–630. https:// doi. 
org/ 10. 1007/ s10115- 018- 1323-6

Otto, B., Steinbuß, S., Teuscher, A., & Lohmann, S. (2019). IDS refer-
ence architecture model 3.0 (p. 118). International Data Spaces

---

<!-- PAGE 27 -->

Electronic Markets (2025) 35:7

Page 27 of 28  7

Association.  https:// inter natio nalda taspa ces. org/ wp- conte nt/  
uploa ds/ IDS- Refer  ence- Archi tectu re- Model-3. 0- 2019. pdf. 
Accessed 17 Oct 2024.

Paleyes, A., Urma, R.-G., & Lawrence, N. D. (2023). Challenges in 
deploying machine learning: A survey of case studies. ACM 
Computing Surveys, 55(6), 1–29. https:// doi. org/ 10. 1145/ 35333 
78

Pathare, A., Mangrulkar, R., Suvarna, K., Parekh, A., Thakur, G., & 
Gawade, A. (2023). Comparison of tabular synthetic data genera-
tion techniques using propensity and cluster log metric. Interna-
tional Journal of Information Management Data Insights, 3(2), 
100177. https:// doi. org/ 10. 1016/j. jjimei. 2023. 100177

Patki, N., Wedge, R., & Veeramachaneni, K. (2016). The synthetic data 
vault. 2016 IEEE International Conference on Data Science and 
Advanced Analytics (DSAA), 2016, 399–410. https:// doi. org/ 10. 
1109/ DSAA. 2016. 49

Pazarbasioglu, C., Mora, A. G., Uttamchandani, M., Natarajan, H., 
Feyen, E., & Saal, M. (2020). Digital financial services (p. 54). 
World Bank Group. https:// pubdo cs. world bank. org/ en/ 23028  
15881 69110 691/ Digit  al- Finan cial- Servi ces. pdf. Accessed 22 
Jan 2023.

Peffers,  K.,  Tuunanen,  T.,  Rothenberger,  M.  A.,  &  Chatterjee,  S. 
(2007). A design science research methodology for information 
systems research. Journal of Management Information Systems, 
24(3), 45–77. https:// doi. org/ 10. 2753/ MIS07 42- 12222 40302
Perez, I., Wong, J., Skalski, P., Burrell, S., Mortier, R., McAuley, D., & 
Sutton, D. (2023). Locally differentially private embedding mod-
els in distributed fraud prevention systems. 2023 IEEE Interna-
tional Conference on Data Mining Workshops (ICDMW), 2023, 
475–484. https:// doi. org/ 10. 1109/ ICDMW 60847. 2023. 00068

Pranto, T. H., Hasib, K. T. A. Md., Rahman, T., Haque, A. B., Islam, 
A. K. M. N., & Rahman, R. M. (2022). Blockchain and machine 
learning for fraud detection: A privacy-preserving and adaptive 
incentive based approach. IEEE Access, 10, 87115–87134. IEEE 
Access. https:// doi. org/ 10. 1109/ ACCESS. 2022. 31989 56
Preziuso, M., Koefer, F., & Ehrenhard, M. (2023). Open banking and 
inclusive finance in the European Union: Perspectives from the 
Dutch stakeholder ecosystem. Financial Innovation, 9(1), 111. 
https:// doi. org/ 10. 1186/ s40854- 023- 00522-1

Qiao, F., Li, Z., & Kong, Y. (2024). A privacy-aware and incremen-
tal defense method against GAN-based poisoning attack. IEEE 
Transactions on Computational Social Systems, 11(2), 1708–
1721. IEEE Transactions on Computational Social Systems. 
https:// doi. org/ 10. 1109/ TCSS. 2023. 32632 41

Richhariya, P. (2012). A survey on financial fraud detection methodolo-
gies. International Journal of Computer Applications, 45. https:// 
www. ijcao nline. org/ archi ves/ volum e45/ numbe r22/ 7080- 9373/. 
Accessed 18 Dec 2024.

Ryman-Tubb, N. F., Krause, P., & Garn, W. (2018). How artificial intel-
ligence and machine learning research impacts payment card 
fraud detection: A survey and industry benchmark. Engineering 
Applications of Artificial Intelligence, 76, 130–157. https:// doi. 
org/ 10. 1016/j. engap pai. 2018. 07. 008

Sattarov, T., Schreyer, M., & Borth, D. (2023). FinDiff: Diffusion mod-
els for financial tabular data generation. 4th ACM International 
Conference on AI in Finance, 64–72. https:// doi. org/ 10. 1145/  
36042 37. 36268 76

Schäfer, F., Rosen, J., Zimmermann, C., & Wortmann, F. (2023). 
Unleashing  the  potential  of  data  ecosystems:  Establishing 
digital trust through trust-enhancing technologies. ECIS 2023 
Research  Papers.  https:// aisel. aisnet. org/ ecis2 023_ rp/ 325. 
Accessed 14 Aug 2024.

Scheider, S., Lauf, F., Möller, F., & Otto, B. (2023). A reference 
system architecture with data sovereignty for human-centric 
data ecosystems. Business & Information Systems Engineering, 
65(5), 577–595. https:// doi. org/ 10. 1007/ s12599- 023- 00816-9

Sein, M. K., Henfridsson, O., Purao, S., Rossi, M., & Lindgren, R. 
(2011). Action design research. MIS Quarterly, 35(1), 37–56. 
https:// doi. org/ 10. 2307/ 23043 488

Sethia, A., Patel, R., & Raut, P. (2018). Data augmentation using 
generative models for credit card fraud detection. 2018 4th 
International Conference on Computing Communication and 
Automation  (ICCCA),  1–6. https:// doi. org/ 10. 1109/ CCAA. 
2018. 87776 28

Strelcenia, E., & Prakoonwit, S. (2023). Improving classification 
performance in credit card fraud detection by using new data 
augmentation. AI, 4(1), 1. https:// doi. org/ 10. 3390/ ai401 0008
Sun, C., Shrivastava, A., Singh, S., & Gupta, A. (2017). Revisit-
ing unreasonable effectiveness of data in deep learning era. 
843–852. https:// opena ccess. thecvf. com/ conte nt_ iccv_ 2017/  
html/ Sun_ Revis iting_ Unrea sonab le_ Effec tiven ess_ ICCV_  
2017_ paper. html. Accessed 29 Jan 2023.

Sun, C., van Soest, J., & Dumontier, M. (2023). Generating synthetic 
personal health data using conditional generative adversarial 
networks combining with differential privacy. Journal of Bio-
medical Informatics, 143. Scopus. https:// doi. org/ 10. 1016/j.  
jbi. 2023. 104404

Susha, I., Grönlund, Å., & Van Tulder, R. (2019). Data driven social 
partnerships: Exploring an emergent trend in search of research 
challenges and questions. Government Information Quarterly, 
36(1), 112–128. https:// doi. org/ 10. 1016/j. giq. 2018. 11. 002
Tiwana, A., Konsynski, B., & Bush, A. A. (2010). Research com-
mentary—Platform evolution: Coevolution of platform archi-
tecture, governance, and environmental dynamics. Information 
Systems Research, 21(4), 675–687. https:// doi. org/ 10. 1287/ 
isre. 1100. 0323

van Panhuis, W. G., Paul, P., Emerson, C., Grefenstette, J., Wilder, 
R., Herbst, A. J., Heymann, D., & Burke, D. S. (2014). A sys-
tematic review of barriers to data sharing in public health. 
BMC  Public  Health,  14(1),  1144.  https:// doi. org/ 10. 1186/  
1471- 2458- 14- 1144

van  Schalkwyk,  F.,  Willmers,  M.,  &  McNaughton,  M.  (2016). 
Viscous open data: The roles of intermediaries in an open 
data  ecosystem. Information  Technology  for  Development, 
22(sup1),  68–83.  https:// doi. org/ 10. 1080/ 02681 102. 2015.
10818 68

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A frame-
work for evaluation in design science research. European Jour-
nal of Information Systems, 25(1), 77–89. https:// doi. org/ 10.  
1057/ ejis. 2014. 36

vom Brocke, J., Simons, A., Niehaves, B., Niehaves, B., & Reimer, 
K. (2009). Reconstructing the giant: On the importance of 
rigour in documenting the literature search process. https:// 
www. seman ticsc holar. org/ paper/ Europ ean- Confe rence- on- 
Infor mation- Syste ms- (- ECIS-)- Simons- Nieha  ves/ 2fc90 c0163 
905ee 89bbd 72a2b a27ac f3dd0 12526. Accessed 29 Feb 2024.

Walia, M., Tierney, B., & McKeever, S. (2020). Synthesising tabular 
data using wasserstein conditional GANs with gradient penalty. 
Irish Conference on Artificial Intelligence and Cognitive Sci-
ence. https:// ceur- ws. org/ Vol- 2771/ AICS2 020_ paper_ 57. pdf. 
Accessed 18 Dec 2024.

Walls, J. G., Widmeyer, G. R., & El Sawy, O. A. (1992). Building 
an information system design theory for vigilant EIS. Informa-
tion Systems Research, 3(1), 36–59. https:// doi. org/ 10. 1287/ 
isre.3. 1. 36

Wang, X., & Yang, Y. (2024). A data simulation method of financial 
fraud transactions based on TransGAN. Proceedings of the 3rd 
International Conference on Computer, Artificial Intelligence 
and Control Engineering, 242–246. https:// doi. org/ 10. 1145/  
36727 58. 36727 98

Wang, Y., Adams, S., Beling, P., Greenspan, S., Rajagopalan, S., 
Velez-Rojas,  M.,  Mankovski,  S.,  Boker,  S.,  &  Brown,  D.

---

<!-- PAGE 28 -->

7  Page 28 of 28

Electronic Markets (2025) 35:7

(2018). Privacy preserving distributed deep learning and its 
application in credit card fraud detection. 2018 17th IEEE 
International Conference On Trust, Security And Privacy In 
Computing And Communications/ 12th IEEE International 
Conference On Big Data Science And Engineering (TrustCom/
BigDataSE), 1070–1078. https:// doi. org/ 10. 1109/ Trust Com/  
BigDa taSE. 2018. 00150

Webster, J., & Watson, R. T. (2002). Analyzing the past to prepare 
for  the  future:  Writing  a  literature  review. MIS  Quarterly, 
26(2), xiii–xxiii.

Weldon, J. C., Ward, T., & Brophy, E. (2021). Generation of syn-
thetic electronic health records using a federated GAN. ArXiv. 
https:// www. seman ticsc  holar. org/ reader/ 16f0a caec6 e5d2c  
7421f 95d81 625f3 c3719 ff81a. Accessed 4 Sept 2023.

White,  O.,  Madgavkar,  A.,  Townsend,  Z.,  Manyika,  J.,  Olanre-
waju, T., Sibanda, T., & Kaufman, S. (2021). Financial data 
unbound: The value of open data for individuals and institu-
tions [Discussion paper]. McKinsey Global Institute. https:// 
www. mckin sey. com/ indus  tries/ finan cial- servi ces/ our- insig hts/  
finan cial- data- unbou nd- the- value- of- open- data- for- indiv idu-
als- and- insti tutio ns#/. Accessed 24 Feb 2024.

Xing,  X.,  Wu,  H.,  Wang,  L.,  Stenson,  I.,  Yong,  M.,  Del  Ser,  J., 
Walsh,  S.,  &  Yang,  G.  (2022). Non-imaging  medical  data 
synthesis for trustworthy AI: A comprehensive survey (No. 
arXiv: 2209. 09239). arXiv. https:// arxiv. org/ abs/ 2209. 09239. 
Accessed 13 June 2023.

Xu, L., Skoularidou, M., Cuesta-Infante, A., & Veeramachaneni, K. 
(2019). Modeling tabular data using conditional GAN (No. 
arXiv: 1907. 00503).  arXiv. https:// doi. org/ 10. 48550/ arXiv.
1907. 00503

Xu,  S.,  Marwah,  M.,  Arlitt,  M.,  spsampsps  Ramakrishnan,  N. 
(2021). STAN: Synthetic network traffic generation with gen-
erative neural models. In G. Wang, A. Ciptadi, spsampsps A. 
Ahmadzadeh (Eds.), Deployable Machine Learning for Secu-
rity Defense (pp. 3–29). Springer International Publishing. 
https:// doi. org/ 10. 1007/ 978-3- 030- 87839-9_1

Yale, A., Dash, S., Dutta, R., Guyon, I., Pavao, A., & Bennett, K. P. 
(2020). Generation and evaluation of privacy preserving syn-
thetic health data. Neurocomputing, 416, 244–255. https:// doi. 
org/ 10. 1016/j. neucom. 2019. 12. 136

Yan,  C.,  Yan,  Y.,  Wan,  Z.,  Zhang,  Z.,  Omberg,  L.,  Guinney,  J., 
Mooney, S. D., & Malin, B. A. (2022). A multifaceted bench-
marking of synthetic electronic health record generation mod-
els. Nature Communications, 13(1). Scopus. https:// doi. org/ 10. 
1038/ s41467- 022- 35295-1

Yoon, J., Jarrett, D., & van der Schaar, M. (2019). Time-series gen-
erative adversarial networks. Advances in Neural Information 
Processing Systems, 32. https:// proce edings. neuri ps. cc/ paper/  
2019/ hash/ c9efe 5f26c d17ba 6216b be2a7 d26d4 90-  Abstr act. 
html. Accessed 20 Dec 2023.

Zachariadis, M. (2020). Data-sharing frameworks in financial ser-
vices: Discussing open banking regulation for Canada (SSRN 
Scholarly Paper No. 2983066). https:// doi. org/ 10. 2139/ ssrn.  
29830 66

Zhang, Z., Yan, C., Mesa, D. A., Sun, J., & Malin, B. A. (2019). 
Ensuring electronic medical record simulation through better 
training, modeling, and evaluation. Journal of the American 
Medical  Informatics  Association :  JAMIA,  27(1),  99–108. 
https:// doi. org/ 10. 1093/ jamia/ ocz161

Zhang, Z. (2022). Synthetic data simulation for privacy-preserv-
ing medical data sharing [Dissertation, Vanderbilt Univer-
sity]. https:// www. proqu est. com/ openv iew/ a52c1 b5ba9 8353a  
d63fe ac8ae dc236 0f/1? casa_ token= EA2kv 24XHB cAAAA  
A:_ 5l8Nr IgKBX 4sLCr Wkkua  y9QsZ X0MsO 3tYa4 h5DMX  
mjQu4 8RmTi orNOG IiP6T LS9Zn 1MOwc ymfxo & cbl= 18750  
& diss= y& pq- origs ite= gscho lar& paren tSess ionId= gry0y
ux5GX HzUSL r77QP zN7q6% 2FkMy iMM8U  n8M7E pXKE% 
3D. Accessed 6 Mar 2024.

Zhu, X., Ao, X., Qin, Z., Chang, Y., Liu, Y., He, Q., & Li, J. (2021). 
Intelligent financial fraud detection practices in post-pandemic 
era. The Innovation, 2(4), 100176. https:// doi. org/ 10. 1016/j. xinn. 
2021. 100176

Zuiderwijk, A., Janssen, M., & Davis, C. (2014). Innovation with open 
data: Essential elements of open data ecosystems. Information 
Polity, 19(1,2), 17–33. https:// doi. org/ 10. 3233/ IP- 140329

Publisher's  Note  Springer  Nature  remains  neutral  with  regard  to 
jurisdictional claims in published maps and institutional affiliations.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Electronic Markets (2025) 35:7
https://doi.org/10.1007/s12525-024-00746-8
RESEARCH PAPER
SynDEc: A Synthetic Data Ecosystem
Fabian Sven Karst1 · Mahei Manhai Li1,2 · Jan Marco Leimeister1,2
Received: 22 March 2024 / Accepted: 2 December 2024 / Published online: 25 January 2025
© The Author(s) 2025
Abstract
Given the critical role of data availability for growth and innovation in financial services, especially small and mid-sized
banks lack the data volumes required to fully leverage AI advancements for enhancing fraud detection, operational effi-
ciency, and risk management. With existing solutions facing challenges in scalability, inconsistent standards, and complex
privacy regulations, we introduce a synthetic data sharing ecosystem (SynDEc) using generative AI. Employing design
science research in collaboration with two banks, among them UnionBank of the Philippines, we developed and validated
a synthetic data sharing ecosystem for financial institutions. The derived design principles highlight synthetic data setup,
training configurations, and incentivization. Furthermore, our findings show that smaller banks benefit most from SynDEcs
and our solution is viable even with limited participation. Thus, we advance data ecosystem design knowledge, show its
viability for financial services, and offer practical guidance for privacy-resilient synthetic data sharing, laying groundwork
for future applications of SynDEcs.
Keywords Synthetic data · Data sharing platform · Data ecosystem · Financial services · Data scarcity
JEL classification M15
Motivation
2021). However, given the financial services industry’s reli-
ance on information, increasing data availability is key to
In the wake of recent global crises, the enhancement of success. This is especially true for smaller financial institu-
financial services has become a crucial driver for accelerat- tions, which lack the necessary volume of high-quality data
ing economic recovery, particularly in developing economies to leverage current AI model advancements. This lack of
where these services are essential for expanding financial data results in missed opportunities, with developing coun-
inclusion and fostering socioeconomic growth (Demirgüç- tries potentially losing out on up to 5% of GDP through
Kunt et al., 2022; Pazarbasioglu et al., 2020; White et al., improvements in fraud protection, operational efficiency, and
workforce allocation (White et al., 2021; Zachariadis, 2020).
Although the sharing of financial transaction data could
Responsible Editor: Gero Strobel
reduce risks and improve transparency (Brodsky & Oakes,
*
Fabian Sven Karst 2017), thereby driving economic growth (O’Leary et al.,
Fabian.Karst@unisg.ch
2021), it faces significant obstacles related to privacy regu-
Mahei Manhai Li lation and information security. Existing solutions such as
Mahei.Li@unisg.ch; Mahei.Li@uni-kassel.de
open banking and federated learning have significant limita-
Jan Marco Leimeister tions. Open banking, which enables customer-approved data
JanMarco.Leimeister@unisg.ch; Leimeister@uni-kassel.de
exchange between financial institutions, often produces unre-
1 University of St.Gallen, Institute of Information Systems liable data due to selective participation (He et al., 2023) and
and Digital Business, Dufourstrasse 50, 9000 St.Gallen, lacks coverage of B2B transactions (Preziuso et al., 2023).
Switzerland Federated learning, an approach for training a model with-
2 University of Kassel, Information Systems, Pfannkuchstraße out direct data exchange, faces scalability issues, restricts
1, 34121 Kassel, Germany
Vol.:(0123456789)

7 Page 2 of 28 Electronic Markets (2025) 35:7
participants to a single shared model, and lacks adaptability two significant ways. First, it advances the field of data eco-
(Baabdullah et al., 2024; Chatterjee et al., 2024). Therefore, systems by addressing privacy challenges and exploring the
research is required to explore data ecosystems that facilitate use of data from multiple institutions for machine learning
the exchange of data between financial institutions and regu- (Brée et al., 2024). Second, it offers practical guidance for
latory bodies while safeguarding the privacy of individual financial institutions on generating and utilizing synthetic
users’ information (Assefa, 2020). data, including benchmarking different algorithms, setups,
In the pursuit of establishing such an ecosystem enabling and training schemes. Given the current lack of guidance on
financial data sharing, the application of synthetic data gen- the conceptualization and implementation of such systems,
eration emerges as a promising solution. Synthetic data, this leads us to the following research question:
currently primarily used in financial services to tackle class
imbalance in fraud detection models by synthesizing new RQ: How to design a financial data ecosystem (SynDEc)
fraudulent samples (Charitou et al., 2021), produces artificial based on synthetic data sharing?
data that if done correctly maintains privacy while capturing
and generalizing the patterns and attributes essential for the To address the RQ, the paper adopts a multifaceted
training of machine learning models. Combining this with approach to investigate architectural design decisions. It
data sharing enables the creation of a secure and robust data encompasses an examination of synthetic data generation
ecosystem. techniques within the ecosystem, explores its implications
While plenty of research on synthetic data generation for training predictive models, and seeks to identify and mit-
exists, significant gaps remain for its practical application igate potential challenges to the ecosystem’s stability and
within data ecosystems. Research has largely focused on functionality. Additionally, it assesses the generalizability
algorithm development, leaving critical questions unan- of the derived principles beyond the domain of financial
swered about how to design an ecosystem for privacy-pre- fraud detection.
serving data exchange with the capability to handle complex The paper is organized as follows: In the next section,
data and achieve interoperability across institutions (Oliveira we present an overview of data ecosystems in financial ser-
et al., 2019). Additionally, there is limited guidance on vices and synthetic data generation. Next, we outline, the
which algorithms are most effective in a context where syn- Design Science Research Methodology by Peffers et al.
thetic data is leveraged to be shared between institutions (2007), combining context-driven innovation and iterative
and not merely used to increase the amount of training data development, which we use as our methodological founda-
(Langevin et al., 2022). Practical strategies for integrating tion. In the first of our four design cycles, we diagnose the
shared synthetic data within machine learning models are problem space through the meta (MR) and design require-
also sparse, though such strategies are essential for realiz- ments (DR) based on both literature and expert interviews.
ing synthetic data’s potential in AI applications (Sattarov Based on this, our initial set of design principles (DP) is
et al., 2023; Strelcenia & Prakoonwit, 2023). Finally, incen- derived and instantiated as a system architecture. Building
tives, for big as well as small players, necessary to encour- on this the second design cycle evaluates the feasibility of
age participation in a synthetic data-sharing ecosystem different synthetic data generation and integration methods.
remain underexplored, despite being vital for fostering the The following design cycle extends this by evaluating the
cooperative engagement on which such ecosystems depend proposed approach in new domains while also investigating
(Gelhaar & Otto, 2020). In response, our research seeks to improvements to the ecosystem based on data generation and
answer the following questions: What architecture is best exchange. Lastly, design cycle four takes a network view,
suited for secure data exchange? Which algorithms are most investigating design elements to ensure early challenges fre-
effective for data generation? What are the optimal strategies quently seen in data ecosystems can be overcome. Finally,
for utilizing shared synthetic data within individual insti- we discuss the findings, outline limitations, provide a per-
tutions? And do the incentives within such an ecosystem spective for future work, and conclude with a brief summary.
effectively encourage participation? Furthermore, there is a
need for specialized engineering and management method-
Related work
ologies tailored to the unique demands of financial services,
where stringent privacy regulations and the complex nature
Data ecosystems in financial services
of transaction data introduce distinct challenges (Oliveira
et al., 2019).
Our research goal is to provide design knowledge for a The growing recognition of data as a critical asset for inno-
synthetic data ecosystem that enables financial institutions vation, growth, and value creation has led firms to increas-
to share financial transaction data and generate utility from ingly seek external sources to enhance their data capabilities
doing so. Our study contributes to the existing literature in (Bagad et al., 2021; Gelhaar & Otto, 2020). One promising

Electronic Markets (2025) 35:7 Page 3 of 28 7
approach is the formation of inter-organizational networks, maximizing the utility of shared data to enhance individual
where organizations collaborate to share resources and organizational performance, thereby contributing to both the
knowledge (Gray & Sites, 2013). Within this context, data theoretical and practical development of data ecosystems.
ecosystems have emerged as an effective framework for data With current research on data ecosystems, predominantly
exchange (Abbas et al., 2021; Heinz et al., 2022; Zuiderwijk concentrating on applications within healthcare, Industry
et al., 2014). Defined as “a set of networks composed of 4.0, and smart cities (Cappiello et al., 2020), this study
autonomous actors that directly or indirectly consume, pro- tries to extend this focus to the financial services industry.
duce, or provide data and other related resources” (Oliveira Given the sector’s significant dependence on highly sensitive
& Lóscio, 2018, p. 4), data ecosystems are built around four data and its advanced application of machine learning tech-
key constructs: (1) actors, (2) their roles, (3) relationships nologies, this context provides a suitable setting to address
among them, and (4) the resources they require. Actors in previously identified research gaps in data security and the
these ecosystems—whether organizations, individuals, or implementation of AI models within data ecosystems. Cur-
institutions—take on roles such as data consumers, provid- rent research on data ecosystems within the financial ser-
ers, and intermediaries, each contributing uniquely to the vices industry can be broadly categorized into two research
ecosystem's function (Oliveira & Lóscio, 2018; van Schalk- streams. The first stream centers on open banking, a cus-
wyk et al., 2016). The roles they assume drive specific tasks, tomer-focused ecosystem where established standards facili-
such as data intermediaries connecting various actors and tate the secure sharing of banking data with various actors
data consumers analyzing and providing feedback to data within the financial services ecosystem, based on customer
providers. These interactions, and the dependencies that requests (Cosma et al., 2023). While this approach grants
arise from them, form the relationships that underpin the consumers greater control over their data, it also raises
ecosystem (Heimstädt et al., 2014; Oliveira & Lóscio, 2018). significant data security concerns due to the decentralized
At the core of a data ecosystem, data platforms provide the nature of data storage across multiple providers—a critical
technical infrastructure for processing and managing data issue given the heightened sensitivity of financial transaction
from diverse sources, enabling various data applications. data (Y. Wang et al., 2018). Furthermore, open banking does
These platforms often incorporate data marketplaces, which not provide institutions with an efficient and secure mecha-
serve as self-service platforms that connect data producers nism for large-scale data exchange, which is essential for
and consumers (Gröger, 2021). Another closely related con- applications such as fraud detection and anti-money launder-
cept is data spaces, which are frequently used to describe ing (Asrow, 2021). The second stream of research revolves
data-sharing ecosystems across organizations and thus will around federated learning, a methodology that completely
be used as synonyms in this paper (Otto et al., 2019). eliminates data sharing by enabling distributed training of
Building on this foundation, recent research has shifted shared models, thereby ensuring compliance with privacy
its focus to the governance and operationalization of data protection regulations (Awosika et al., 2024; Lei et al., 2023;
ecosystems, particularly in the areas of data sovereignty Perez et al., 2023). However, federated learning presents
(Jarke, 2017) and trust (Gelhaar & Otto, 2020; Schäfer et al., significant challenges, including computational overhead,
2023), which are critical for ensuring secure and reliable scalability issues, and still privacy risks, as malicious actors
data exchange. However, in their comprehensive review of might be able to infer sensitive data from the model param-
data ecosystems, Brée et al. (2024) identified several gaps eters shared during the training process (Baabdullah et al.,
within the literature that are currently under-researched, 2024; Chatterjee et al., 2024). Additionally, the necessity
among them data security and the integration of artificial for participants in a federated learning ecosystem to agree
intelligence and machine learning within data ecosystems. on a single model architecture, which is difficult to modify
On the one hand, data security deals with ways data can once established, further complicates its implementation.
be stored and shared within data ecosystems while remain- The constraints of existing solutions, coupled with the fact
ing protected as well as the influence of such measures on that data ecosystems do not emerge organically but instead
the utility of data ecosystems (Brée et al., 2024). On the necessitate strategic planning around a shared value proposi-
other hand, machine learning and artificial intelligence have tion, have resulted in the lack of a comprehensive financial
become central to the formation of data ecosystems, yet there data ecosystem to date (Adner, 2017; Immonen et al., 2014).
is a need for a deeper understanding of the requirements for This is aggravated by a research gap in the development
sharing AI training data and how training on shared data of specialized engineering and management methodologies
should be conducted (Brée et al., 2024). Our research seeks tailored to the needs of such an ecosystem (Oliveira et al.,
to address these challenges by proposing a new type of data 2019) which are especially critical in the financial services
ecosystem centered on synthetic data, which offers a means sector, where stringent privacy requirements and the com-
to mitigate privacy risks while maintaining the benefits plex nature of financial transaction data introduce distinct
of data sharing. Additionally, we investigate strategies for challenges. Consequently, further research is essential to

7 Page 4 of 28 Electronic Markets (2025) 35:7
address these challenges and to delineate the architectural the context of financial transaction data, as revealing a user’s
frameworks necessary for the creation of robust and secure membership in a specific bank’s dataset could enable mali-
data ecosystems within the financial industry. cious actors to carry out more targeted fraudulent activities,
making fraud prevention more difficult. Research on dealing
Synthetic data generation and its application
with membership inference risks in synthetic data, primarily
drawn from the healthcare domain, can be divided into two
Synthetic data can be defined as “data that has been gener- major streams. The first stream focuses on achieving guaran-
ated using a purpose-built mathematical model or algorithm, teed privacy by modifying models to conform to differential
with the aim of solving a (set of) data science task(s)” (Jor- privacy principles, ensuring both the data and the model are
don et al., 2022, p. 5). This generation process can take many protected. Algorithms implementing this are the PATE-GAN
forms as comprehensively categorized by Bauer et al. (2024) (Jordon et al., 2018) or DP2-VAE (Jiang et al., 2022) archi-
into 20 distinct method types. Among these, generative tectures. The second research stream focuses on evaluating
adversarial networks (GANs) are the most popular. GANs and managing privacy risks within acceptable limits for a
learn by pitting a generator (synthesizes data from random given volume of published synthetic data, providing various
noise) and a discriminator (classifies samples as real or fake) metrics and thresholds for guidance (H. Chen et al., 2023;
against each other, resulting in two highly skilled networks Yan et al., 2022). Popular measures are the nearest neighbor
(Goodfellow et al., 2014). This architecture is highly adapt- adversarial accuracy risk (Yale et al., 2020), the member-
able, as discriminator and generator can be easily adjusted to ship inference risk (Choi et al., 2018), and the meaningful
new tasks (e.g., time series or graph generation) while being identity disclosure risk (Emam et al., 2020). Furthermore,
frequently the best-performing synthetic data generation these measures have also been adopted by regulators such as
method (Bauer et al., 2024). Another commonly employed the European Medicines Agency and Health Canada which
synthetic data generation method is autoencoder-based both provide thresholds for identifying disclosure risk (Yan
architectures, especially variational autoencoder (VAE) et al., 2022).
(Kingma & Welling, 2013). VAEs are trained by mapping As the complexity of models continues to grow, neces-
an input sample to a hidden representation, which is then sitating larger datasets, synthetic data has been applied in a
mapped back to the original vector, thus creating a model variety of fields, where it is used to facilitate more efficient
that synthesizes valid data from a lower dimensional rep- and effective development of AI solutions (Lu et al., 2023).
resentation. This decoder model is then used to generate In financial services, these have been mainly use cases that
data from random noise which makes it especially useful for inhibit a strong class imbalance such as anti-money laun-
learning from data with disentangled features (Bauer et al., dering and financial fraud detection. Here, synthetic data
2024). Third, recurrent neural networks, feedforward neural generation is used to increase the amount of data within the
networks which include recurrent edges, are able to generate minority class, thereby increasing training efficiency (E. Alt-
sequential data of arbitrary length. This makes them ideal for man et al., 2024; Hilal et al., 2022). The current landscape
sequence generation tasks such as speech synthesis, music, is largely dominated by GAN-based architectures especially
and time series generation (Lipton et al., 2015). Finally, vir- Wasserstein GANs due to their superior training stability
tual environments are computer simulations in which algo- (Hilal et al., 2022; Sethia et al., 2018; Strelcenia & Pra-
rithms interact with each other based on predefined rules, koonwit, 2023). However, recent advancements have seen
generating synthetic data in the process (Bonabeau, 2002). transformer-based architectures (Nickerson et al., 2023) and
In the context of machine learning, synthetic data is pri- diffusion-based models (Sattarov et al., 2023) emerging as
marily utilized in three key areas: (i) private data release, (ii) competitive alternatives to GANs. Due to the internal usage
data de-biasing and fairness, and (iii) data augmentation for of this synthetic data, data privacy has not been a main con-
robustness (Jordon et al., 2022). As the focus of this paper sideration when building these models. Data privacy consid-
is employing synthetic data for private data release, it will erations have mostly been explored in academic studies that
be investigated in more detail. Hereby, private data release aim to make their synthetic data publicly available. These
describes the case where synthetic data is used to mitigate studies typically employ virtual environment-based systems,
disclosure risk, allowing privacy concerns and regulatory such as multi-agent simulations, which simulate financial
issues to be circumvented by substituting real data with syn- transaction data by modeling interactions between known
thetic data (Esteban et al., 2017; Jordon et al., 2018). How- actors and behaviors (E. Altman et al., 2024; Jensen et al.,
ever, this comes with certain risks of disclosure, which users 2023; Lopez-Rojas et al., 2016). While these approaches
need to be aware of. While multiple risks exist, the most are very secure from a privacy perspective as real data is
relevant is membership inference which seeks to determine only used during model evaluation of the synthetic data,
if an individual was part of the original dataset (Bun et al., they require significant manual work to identify patterns and
2021; Jordon et al., 2022). This risk is particularly critical in changing behaviors need to be detected first, before they can

Electronic Markets (2025) 35:7 Page 5 of 28 7
be integrated into the simulation (Bauer et al., 2024). How- as a simplified representation of reality and accumulates
ever, the automatic generation and sharing of synthetic data specific design knowledge (March & Smith, 1995); thus,
derived from real data have not been extensively explored. DSR provides a suitable framework for our study (A. R.
As privacy concerns intensify due to regulatory pressure Hevner, 2007; Iivari, 2007). Our model presents a struc-
and customer expectations, as well as a growing necessity tured approach to designing a data ecosystem under privacy
for extensive datasets to support cutting-edge machine learn- and data complexity constraints, exemplifying a solution
ing models (Hittmeir et al., 2019), employing synthetic data to the problem discussed in the earlier sections. Our meth-
has the potential to address privacy challenges in data eco- odological approach to DSR—the design science research
systems. Recent studies by Sattarov et al. (2023) and Lan- methodology (DSRM) by Peffers et al. (2007) has six steps,
gevin et al. (2022) have begun to investigate this potential arranged in sequential order, and incorporates an iterative
for financial services. However, these studies primarily focus research procedure by design. The process typically starts
on comparing different data generation methods and present with the identification of a research problem with practical
synthetic data sharing as merely one potential application. relevance, in our case, the challenge of data scarcity within
This leaves significant research gaps regarding the mecha- financial fraud detection. Next, the solution objectives are
nisms for data exchange, the optimal strategies for learning designed to address the stated challenges and to create a
from cross-institutional synthetic data, and the incentives meaningful artifact. In line with DSR, the insights gained
for participating institutions, reaching beyond financial ser- from the build-and-evaluate process must be generalizable
vices and tackling current challenges in data ecosystems in and therefore applicable in more generic settings (Jones &
general. Moreover, these studies offer little guidance on the Gregor, 2007). Also, the design artifacts should result in
design of such an ecosystem, highlighting a clear need for profound disruptions to traditional ways of doing business
establishing design principles and best practices. (A. Hevner & Gregor, 2022). Based on these objectives and
on theory, the artifact is designed and developed in the next
research process step. Phase 5 comprises evaluation, which
Research approach
is necessary to test whether an artifact achieves the purpose
of its creation and to prove this achievement using rigorous
A design science research project was initiated to address methods (Venable et al., 2016). The evaluation phase also
a research gap in approaches to enhance privacy protec- helps one to better understand the problem at hand and thus
tion within data ecosystems while preserving data utility to realize improved outcomes (A. R. Hevner et al., 2004).
for machine learning applications. This need, combined Due to the iterative nature of this process, it can be repeated
with the financial services industry’s demand for solutions until a suitable artifact is derived. The design knowledge in
to address the limitations of inter-organizational collabo- the form of DPs with their DRs and MRs generated during
ration in tackling financial fraud and anti-money launder- this process can be seen as a nascent design theory, cap-
ing detection, prompted the research effort. This project is turing a general solution in a class of artifacts (Baskerville
aimed at designing an innovative artifact that provides finan- et al., 2018). While MRs are high-level, generalized goals
cial institutions with a tool to easily exchange high-quality that an artifact must satisfy to address a class of problems,
data with each other enabling them to increase their fraud providing the foundational objectives for artifact design
and anti-money laundering detection performance, creat- (Walls et al., 1992), DRs are specific, actionable specifica-
ing guidance on how to implement such a system, as well tions that detail the necessary features and characteristics an
as to evaluate its benefits and the associated privacy risks artifact must have to fulfill the meta-requirements (Gregor
(Gregor & Hevner, 2013; Peffers et al., 2007). To achieve & Hevner, 2013). Lastly, DPs are prescriptive, actionable
these objectives, we adopted design science research (DSR), guidelines derived from design requirements and grounded
a framework particularly suited for the iterative develop- in both theoretical foundations and empirical evidence, pro-
ment of novel artifacts addressing solution spaces with viding clear instructions for creating artifacts that meet the
broad implications for both theoretical and practical prob- specified requirements and address the underlying problem
lem domains (Peffers et al., 2007) and providing theoreti- space (Gregor et al., 2020). Thus, especially the DPs can be
cally justified prescriptive knowledge (Gregor et al., 2020). used to guide actions in a wider range of problems, in par-
Following this paradigm, we focus on creating artifacts ticular, data ecosystems where data with a complex structure
that serve organizational purpose, in our case enabling data needs to be shared under privacy restrictions (A. R. Hevner
sharing despite privacy restrictions, through a structured et al., 2004). They contribute to the theoretical advance-
research process that rigorously builds and evaluates viable ment of the information systems (IS) community and pro-
solutions (A. R. Hevner et al., 2004; March & Smith, 1995). vide valuable guidance for practitioners in designing similar
Following Scheider et al. (2023), our artifact is a “model” artifacts (Baskerville et al., 2018; Sein et al., 2011). Since
(March & Smith, 1995), a type of DSR artifact that serves the DSR approach requires integration into an organizational

7 Page 6 of 28 Electronic Markets (2025) 35:7
context, the project was conducted in collaboration with analytics, and machine learning projects. Furthermore, these
the UnionBank of the Philippines, a rapidly growing digi- interviews were used to identify the objectives of our solu-
tal bank, as well as a European neo bank with a focus on tion by deriving DRs and MRs. Next, we iterated the first
wholesale transaction banking. Both banks rapidly scaled “Design—Demonstrate—Evaluate” cycle. In the design
their digital transaction infrastructure in recent years and phase, we formulated the initial set of DPs. These princi-
are now looking for new ways to tackle transaction fraud and ples were then translated into a system architecture during
money laundering. While the banks granted us deep insights the demonstration phase, specifying its material properties
into the problem of limited transaction data and provided like algorithms and interaction layers. Subsequently, an
invaluable feedback through all cycles, it was decided that evaluation was conducted, involving feedback from aca-
prototyping and evaluation would be conducted on publicly demics and industry experts through four semi-structured
available datasets instead of real bank data to reduce risks interviews. The outcomes helped evaluate the feasibility of
and allow fast iterations to create a solid understanding of the initial design and led to the refinement of selected DPs
potential pitfalls. in the second iteration. In cycle 2, we conducted a literature
Within this DSRM framework, four iterative design review identifying suitable algorithms for synthetic financial
cycles were conducted, thus allowing for continuous refine- transaction data generation and based on them, instantiated
ment of the artifact’s design based on feedback and derive a prototype which was subsequently evaluated on a publicly
insights (Mullarkey & Hevner, 2019; Sein et al., 2011). In available real-world credit card transaction dataset to iden-
the next paragraph, the activities in each cycle are intro- tify the most suitable synthetic data generation algorithm,
duced which are outlined in the following graphic (Fig. 1). establish the feasibility of the solution, and demonstrate the
First, the DSRM project starts with problem identifica- privacy-preserving properties of synthetic data. Based on
tion and motivation, focusing on stakeholder problems and additional expert feedback as well as two large simulated
challenges. This was done by conducting a systematic litera- financial transaction data sets, cycles 3 and 4 refine the exist-
ture review on data ecosystems, synthetic data, and financial ing DPs and introduce new ones where needed. While cycle
fraud detection as well as semi-structured interviews with 3 explores the local level of the ecosystem in more detail,
employees at different levels at our partner banks, who are cycle 4 focuses on the global level and cooperative chal-
engaged in data sharing initiatives, fraud detection or data lenges within the ecosystem. Throughout the DSRM cycles,
Fig. 1 Steps and design cycles within our design science research study based on Peffers et al. (2007)

Electronic Markets (2025) 35:7 Page 7 of 28 7
we iteratively abstracted the requirements, DPs, and system data is needed for model training (Aurna et al., 2023; Hilal
features. Thus, our main theoretical contributions lie in the et al., 2022). This need for increasing amounts of training
abstracted artifacts, particularly the DPs, which are first data is further aggregated by the extreme class imbalance
derived in “Design of initial DPs” and continuously refined of datasets (large datasets are needed for a sufficient num-
throughout the paper. ber of samples in the minority class) as well as the fast-
changing nature of fraudulent patterns (Abdul Salam et al.,
2024; Ryman-Tubb et al., 2018). Tackling this, frequently,
Problem identification and motivation
the proliferation of cross-institutional data is presented as a
potential solution, to increase the amount of available data
The diagnosis phase consists of two tasks: understanding the and train better and more robust models (Kong et al., 2024;
problem and solution domain and defining the ecosystem’s Myalil et al., 2021; Qiao et al., 2024). However, due to the
requirements. First, we positioned our DSRM project within high sensitivity of financial transactions and the connected
the domain of inter-institutional collaboration within finan- risk of privacy leakage, this exchange is usually prohibited
cial services. With a major focus of such collaboration being by external regulation or internal guidelines (Bian & Zheng,
financial fraud detection, a first literature review on data 2023; Pranto et al., 2022; Ryman-Tubb et al., 2018). To over-
ecosystems, synthetic data, and financial fraud detection was come this problem, frequently federated-learning-based
conducted. Following the methodology by Webster and Wat- solutions are proposed, allowing the raw data to remain
son (2002), four search strings were established (Table 1) local, while a joined model is trained (Kong et al., 2024;
and the following databases: ScienceDirect, EBSCOhost, Lei et al., 2023; Pranto et al., 2022). While these approaches
SpringerLink, IEEE Xplore, and AISeL, were queried for show some promise, they retain significant drawbacks such
articles containing the previously defined search string in as the computational overhead, scalability issues, and the
title, abstract, or the author keywords. Furthermore, only necessity to agree on a single model architecture, which is
papers written in the English language and published within difficult to modify once established (Baabdullah et al., 2024;
the past 5 years were included. This initial query resulted Chatterjee et al., 2024). This leads us to the conclusion that
in a total of 3794 papers, which were then filtered based on there is a need for a data ecosystem that allows financial
a screening of titles and abstracts. While for papers iden- institutions to exchange data with one another while staying
tified by the “Fraud Detection” query strings only papers compliant with laws and internal regulations on data privacy
were included that deal with financial transaction fraud and and giving them the freedom to use this data to fulfill their
either focus on privacy or a multi-organizational context, specific needs.
for papers selected by the “Data Ecosystem” string the only
inclusion criteria were a focus on data ecosystems. After
Definition of solution objectives
adding more relevant papers through a forward and back-
ward search a total of 61 papers were selected for inclusion
in the literature review. Looking for potential solutions, we drew on the second
The analysis of the first part of our literature review part of our literature review focusing on data ecosystems
focusing on fraud detection revealed that the limited availa- providing relevant insights on how such challenges can be
bility of data is a significant challenge, especially for smaller navigated and potentially overcome in the context of finan-
organizations (Kulatilleke, 2022; Pranto et al., 2022). Espe- cial data. Particularly papers from the healthcare domain
cially with increasingly sophisticated adversaries (Qiao (H. Chen et al., 2023; Morley-Fletcher, 2022), investigations
et al., 2024) and thus, more complex fraud detection models, into the emergence (Gelhaar & Otto, 2020) and organization
frequently built based on deep learning architectures, more (Langer & Mukherjee, 2023) of data ecosystems as well as
Table 1 Results of systematic literature search
ID Search string Hits Filter: titlea Remove dupli- Filter: Fwd and Bwd Total
cates abstracta search
I “Financial” AND “Fraud Detection” 2471 336 449 30 5 35
“Transaction” AND “Fraud Detection” 990 139
II “Financial” AND “Data Ecosystem” 164 13 19 18 8 26
“Synthetic Data” AND “Data Ecosystem” 169 6
a Detailed filter criteria can be found at https:// anony mous. 4open. scien ce/r/ Synth eticD ataEc osyst ems- 801C/ Cycle1_ Initi alDes ignPr incip les/
README. MD

7 Page 8 of 28 Electronic Markets (2025) 35:7
Table 2 Overview interviewees for solution requirements
ID Job title Expertise Years of experience Length of interview
Interviewee 1 Chief data scientist Data science 10 years 00:51:10
Interviewee 2 Senior data scientist Data science 5 years 00:37:34
Interviewee 3 Data scientist Data science 5 years 00:36:30
Interviewee 4 Chief financial officer Fraud detection > 20 years 00:38:36
Interviewee 5 Senior compliance officer Fraud detection > 20 years 00:59:08
Interviewee 6 Junior compliance officer Fraud detection 4 years 00:44:27
Interviewee 7* Head of the AI center of excellence Data science > 20 years 00:19:25
Interviewee 8* Head of data science ventures Data science 10 years 00:31:03
*Interviewee from UnionBank of the Philippines
the preconditions for data sharing (Fassnacht et al., 2023), and DR2. This is important because while a data standard for
were detrimental in deriving the design requirements pre- financial transaction data exists, different banks diverge from
sented in the following section. it (Major & Mangano, 2020), which was also confirmed dur-
To extend our insights into the domain beyond academic ing our interviews (“Different data providers have different
literature next, nine semi-structured interviews with employ- schemas and transaction languages.”—Interviewee 2); thus,
ees at various levels at our project partners, with a focus on a data ecosystem needs to be flexible enough to accommo-
fraud detection or data science, were conducted (for details, date various input data structures (DR1). This is particularly
see Table 2). Querying them for challenges as well as poten- important as data needs to be regularly updated and the cost
tial solutions for tackling data scarcity within their domain. for these updates should be as low as possible. Furthermore,
Based on this, we formulated two meta-requirements data privacy standards imposed by regulators and internal
(MR) that any solution must adhere to. MR1 emphasizes the policies must be upheld (“In terms of data sharing we do not
ease of data sharing between financial institutions, encom- engage in anything, because this is the pain with financial
passing both technical, legal, and collaboration aspects. institutions, we are really protective of our data”—Inter-
The need for technical ease of use was informed by insights viewee 8–1). Our interviews revealed that in the context of
drawn from the medical field, where challenges related to our partner institutions, this means that all real data must
tool availability and varying data standards were identified be processed locally within the financial institution (DR2).
as hindrances to data sharing (van Panhuis et al., 2014). From a data-centric perspective, the performance of machine
The legal dimension in ecosystem usability was motivated learning methods can be enhanced by increasing the vol-
by diverse regulatory requirements across jurisdictions, as ume of training data available (Sun et al., 2017). Thus, MR2
observed in existing approaches to sharing financial transac- can be achieved by enabling the combination of data from
tion data (Blake et al., 2019). Lastly, ease of collaboration multiple sources through the data ecosystem and making it
was drawn from the ecosystem literature, where cooperative accessible as a unified data source (DR3). Given the goal of
challenges were outlined as a major hurdle to data ecosystem creating an ecosystem that is applicable to multiple tasks, the
development (Gelhaar & Otto, 2020). MR2 highlights the absence of a dominant algorithm in many fields (e.g., fraud
necessity of increased utility as a result of sharing data. This detection), and the insight from our interviews that banks
requirement emanated from discussions with our partners prefer to build and exclusively own their solutions (“One
regarding their goal of establishing a data-sharing ecosystem model will not be enough, it will be a collection of models
and from the literature describing incentives for participation which answer different questions …”—Interviewee 8–1),
in data ecosystems (Gelhaar et al., 2021). the data ecosystem must support diverse types of algorithms
Next, we refined the MRs into more specific DRs, draw- (DR4). Additionally, the imbalanced nature of fraud data
ing from literature as well as the knowledge of our project necessitates tools on the ecosystem to address data imbal-
partners.1 To incentivize users to participate in data-sharing, ances through filtering, oversampling, and undersampling
setup as well as reoccurring costs need to be as low as pos- (DR7), as most machine learning algorithms perform better
sible, which is reflected in MR1 and propagates into DR1 on balanced datasets (Longadge & Dongre, 2013). As fraud
patterns change quickly when discovered, the timely integra-
tion of recent fraud patterns into fraud detection algorithms
is crucial (Benchaji et al., 2021; Zhu et al., 2021). As this is
1 A detailed mapping from interview quotes to DRs can be found on:
utterly important, two DRs were dedicated to achieving this.
https:// github. com/ Farum an/ Synth eticD ataEc osyst ems/ blob/ master/
Cycle1_ Initi alDes ignPr incip les/ README. MD First, institutions should have the capability to automatically

Electronic Markets (2025) 35:7 Page 9 of 28 7
update the data (“fraud, money laundering patterns will Design of initial DPs
change, behavior patterns will change and that's why you
need to establish this relationship where there is a continu- In our first design phase, our primary emphasis was on iden-
ous flow of information”—Interviewee 4), ensuring that the tifying the foundational DPs. Building on the DRs derived
dataset incorporates the most recent fraud patterns (DR5). in the previous section and following the recommendations
This not only aligns with MR1 by enhancing user conveni- of Chandra et al. (2015), we created DPs that followed the
ence and reducing the need for frequent user inputs but also structure “Provide the system with [material property—in
guards against model drift (Zhang, 2022). However, even terms of form and function] in order for users to [activity of
with automatic updates, the dataset may still be dominated user/group of users—in terms of action], given that [bound-
by outdated fraud patterns, posing a risk to the algorithms ary conditions—user group’s characteristics or implementa-
(Paleyes et al., 2023). Therefore, users should be able to tion settings]” (Chandra et al., 2015, p. 4045). Furthermore,
incorporate pattern-based artificial data into the ecosystem to ground these artifacts in practical relevance, expert inter-
(“…[the] machine has the benefit of learning the patterns views with our partners were conducted to justify the DPs
you, as a human, identify as problematic. In the current derived from the literature. Figure 2 depicts the relationship
world, such patterns are the key to everything because crimi- between MRs, DRs, and DPs.
nals will always evolve.”—Interviewee 6) (DR6). Allowing DP1—Provide the system with modular systems design
the data ecosystem to benefit from expert domain knowledge in order to ensure independence of local data and cross-
is not yet reflected in the data (Richhariya, 2012). After hav- institutional proliferation of synthetic data given that the
ing defined the problem as well as the solution space and raw data is sensitive: To address DR1 and DR3, the data
outlined our requirements, we can now commence the first ecosystem must possess the capability to process data from
design, implementation, and evaluation cycle. diverse sources while enabling the integration of this data
for synthetic data generation. Drawing upon the principles
of modular systems theory (Tiwana et al., 2010), institutions
are granted flexibility in designing their module structures
Cycle 1: DPs and system architecture
while adhering to a standardized representation, thereby
for synthetic data sharing
ensuring that the data can be exchanged with the ecosystem.
Additionally, once the initial setup is complete, automated
During the initial phase of the DSRM project, founda- data updating becomes straightforward, as all computations
tional DPs were established, integrating expert insights, can be performed locally, without the need for sensitive data
relevant literature, and domain requirements, to develop a to be transmitted outside the local system. This capability
synthetic data ecosystem for financial institutions. Build- fulfills the requirements outlined in DR5.
ing on these insights an architecture for such an ecosystem DP2—Provide the system with the ability to generate
was proposed. synthetic transaction data using generative adversarial
Fig. 2 Relationship between MRs, DRs, and DPs using the final set of DPs

7 Page 10 of 28 Electronic Markets (2025) 35:7
networks (GANs) in order to remove private data, given requirement, that a data ecosystem should be able to pro-
guidelines, or regulations on data sharing: Most models vide more balanced datasets (DR7). This can be accom-
created in financial institutions, such as fraud detection plished by equipping users with advanced filtering options
algorithms, need to be trained on transaction-level data as or enabling them to manipulate the existing data through
its granularity and connectedness over time allows for com- techniques such as under- or oversampling (Lopez-Rojas
plex patterns to emerge (Hilal et al., 2022) This combined & Axelsson, 2012).
with DR4, which requires users to train different types of
Demonstration of DPs by instantiation in a system
algorithms and mandates a data ecosystem to provide the
architecture
user with access to such low-level data. However, sharing
transaction-level data poses challenges due to regulatory
constraints (Blake et al., 2019) and internal policies man- Based on the DRs and DPs, we present a multi-layered plat-
dating its local storage (DR2). As anonymization is not form architecture for a synthetic data ecosystem. While the
able to preserve both data utility and privacy for heavily local processing layer is implemented at every institution,
interconnected data (Loukides et al., 2010), we propose to the synthetic data generation as well as the fraud detec-
solve this challenge by using GANs, due to their unique tion layer are centralized. An overview of this architecture
ability to learn patterns in data and generate synthetic data mapped with corresponding DPs can be seen in Fig. 3.
nearly indistinguishable from the original (Walia et al.,
2020). This enables us to preserve real data locally while Local processing layer The local processing layer is modu-
sharing only the privacy-preserving GAN-generated data lar and situated at every financial institution (DP1). Here,
within the data ecosystem. This data can then be merged the GAN models are trained on sensitive transaction data
with synthetic data from other institutions and allows the to produce accurate synthetic representations of this data
training of machine learning models on the combined data- (DP3). Furthermore, the conversion to the data standard
set. Therefore, ensuring the confidentiality of sensitive data the synthetic data needs to conform to is enforced. Moreo-
while empowering the ecosystem to enhance fraud detec- ver, back-testing is done to ensure data quality while guar-
tion capabilities by training algorithms with substantial anteeing that the real data never leaves the local environ-
volumes of high-quality data. ment (DP2).
DP3—Provide the system with a back-testing mecha-
nism in order to ensure newly generated synthetic data Global data layer Contrary to the previous layer, the syn-
matches in composition and fraud detection training thetic data layer is not situated at a specific institution.
performance with real data given that data quality can- Instead, this layer is where synthetic data is merged and
not be independently verified: To facilitate the seamless modifications to the data composition through the addition
integration of data from multiple institutions (DR3) and of pattern-based data generators or the artificial rebalancing
enable frequent system updates without human interven- of different classes can be achieved (DP4).
tion (DR5), it is essential to establish a robust quality
control mechanism. This mechanism serves to uphold the Fraud detection layer This layer is accessible to any partici-
integrity of the data introduced into the ecosystem, as pating company allowing them to access the synthetically
only a few bad data points can have tremendous effects generated data and modify it to fit their models by providing
on machine learning models (Chakravarty et al., 2020). capabilities to subsegment and alter data, making it optimal
One approach to achieve this is by implementing a back- for their custom fraud detection models.
testing procedure, which ensures that the synthetic data
Evaluation of derived DPs and system architecture
accurately captures the underlying patterns of the local
real data (Dankar et al., 2022).
DP4—Provide the ability to alter synthetic data to give After deriving the system architecture from our DPs, we
it the optimal composition for the training of machine presented both to two experts from our partner institution
learning models given that data in fraud detection is as well as 2 academics (for details, see Table 3).
highly skewed: To further enhance model performance, The feedback gathered from the experts was overall
a data-sharing ecosystem should be designed to provide positive and especially the use of modular system design
users with the ability to alter and extend the existing data (DP1) to ensure reduced complexity of the eco-system and
to create the right data for their use case. In financial complete control of the local layer by the single institutions
services use cases, such as money laundering or fraud was highly appreciated. Furthermore, DP4 was approved
detection, the balance between the classes often is a chal- by experts stating that “balancing data is a major concern
lenge (Al-Hashedi & Magalingam, 2021), resulting in the when training ML models and a system providing smart

Electronic Markets (2025) 35:7 Page 11 of 28 7
Fig. 3 System architecture (ver-
sion 1)
Table 3 Interviewees for validation of DPs and platform architecture
ID Job title Expertise Years of experience Length of interview
Interviewee 7* Head of the AI center of excellence Data science > 20 years 00:23:16
Interviewee 8* Head of data science ventures Data science 10 years 00:20:27
Interviewee 9 Research assistant Statistical modeling 5 years 00:31:26
Interviewee 10 Research assistant Design science research 5 years 00:22:01
*Interviewee from UnionBank of the Philippines
support for that could be particularly helpful” (Interviewee Cycle 2: Synthetic financial transaction data
10). Lastly, the proposed architecture was seen as a good generation and privacy
first outline to create a prototype; however, the computa-
tional resources required to train the synthetic data genera- In the second cycle of the DSRM project, different methods
tion models for frequent updates were raised as a concern. for synthetic data generation were evaluated, thus tackling
When discussing the proposed DPs as well as architecture one of the limitations identified by expert feedback. This
with academic experts from the field of design science is done by testing the insights from a systematic literature
research, data sharing, and fraud detection, DP2 was criti- review on synthetic data generation on a real-world financial
cized for multiple reasons. First, the limitation to a single fraud detection dataset, leading to the refinement of DP2.
technology for data generation (GANs) was seen as being
too restrictive and limiting the system’s adaptability to dif- Design of synthetic data generation
ferent domains (“Why do you limit yourself to a single data
generation algorithm?”—Interviewee 10). Furthermore, Addressing the expert feedback, the second design cycle
concerns emerged about the feasibility of generating finan- focuses on the refinement and extension of DP2. Based on
cial transaction data from limited local data and the utility the comments, it was adjusted to DP2—Provide the sys-
of synthetic data to benefit fraud detection performance (“I tem with the ability to identify, validate, and apply context-
doubt that abstracted data from other institutions with dif- specific synthetic data generation techniques with mutually
ferent data distributions can improve fraud detection per- agreed on over-sampling in order to remove private data,
formance.”—Interviewee 9). given guidelines or regulations on data sharing so that it is

7 Page 12 of 28 Electronic Markets (2025) 35:7
Table 4 Results of systematic literature search
Search string Hits Selected Fwd and Bwd search Total
(“synthetic data generation” OR “artificial data generation”) AND (“transaction data” OR “time 289 47 8 55
series data”)
no longer restricted to a single method for generating syn- module in combination with random noise to synthesize
thetic data and includes the necessary validation of selected new data. The literature predominantly focuses on applying
techniques to obtain optimal data generation performance. these algorithms to health records (Xing et al., 2022), with
To validate DP2 and identify suitable methods to gener- limited exploration in other domains such as traffic data (S.
ate synthetic financial transaction data, a literature review Xu et al., 2021) and IoT data (Liu et al., 2019); however,
following vom Brocke et al. (2009) was conducted. In the none of the papers identified has examined the application
first step, top publications regarding synthetic data genera- of these methods for the cross-institutional proliferation of
tion were reviewed, resulting in our search string which was financial transaction data. Furthermore, while Weldon et al.
then used to identify journal articles and conference papers (2021) found that using only synthetic data can achieve
written in English and published after 2020 in the following performance gains, others, such as Frid-Adar et al. (2018),
databases: ScienceDirect, EBSCOhost, SpringerLink, IEEE show that mixing synthetic and real-world data is more
Xplore, and AISeL. The results can be seen in Table 4. beneficial. Thus, the optimal algorithm for generating
From these papers, 46 distinct algorithms were extracted financial transactions in the context of synthetic data shar-
and grouped by their underlying algorithm type. Conse- ing as well as the necessity of combining synthetic with
quently, GANs emerge as the primary underlying mecha- real data remains unclear. Lastly, by employing algorithms
nism (used by 55.3% of algorithms) for generating syn- that do not provide privacy guarantees by themselves, it
thetic transaction data. GAN models work by creating two remains unclear how safe it is to share the generated data.
neural networks that learn by competing in synthesizing To tackle these two privacy measures frequently used in
and identifying synthetic data and thus, once trained, can the literature, nearest neighbor adversarial accuracy and
generate synthetic data that is indistinguishable from real membership inference risk precision were used to ensure
one (Goodfellow et al., 2014). However, different imple- the evaluated algorithms do not leak information (Yan
mentations exist. To allow for variations between the algo- et al., 2022). While nearest neighbor adversarial accuracy
rithms tested and address the high degree of similarity measures if a classifier is able to distinguish between real
between the different GAN architectures, we decided to (holdout set) and synthetic data and thus is a good indi-
only include two of them in our comparison: CTGAN (L. cator for privacy leakage through overfitting (Yale et al.,
Xu et al., 2019), which was the most mentioned algorithm 2020), membership inference risk precision measures how
and is a representative of GANs taking only dependen- easy it is for an attacker to predict if a record is part of
cies between attributes, but not samples, into account and the train dataset or not based on the synthetic data (Choi
TimeGAN (Yoon et al., 2019) (ranked third by mentions) et al., 2018). As no thresholds for these measures for finan-
which incorporates the temporal dimension between sam- cial transaction data exist, the ones for medical data were
ples. To tackle the criticism from cycle one, we extended employed, which can be seen below (Table 5).
our overview beyond GAN-based architectures. The most
Demonstration of synthetic financial data
frequently mentioned implementations using other algo-
generation
rithm types were Gaussian mixture models, which learn the
distribution for each attribute and then generate new sam-
ples by drawing from these (S. Xu et al., 2021) and TVAE In this section, we operationalized the derived DPs into
(Ishfaq et al., 2023), a variational autoencoder (VAE), a prototype system in Python using a modified version of
which works by learning to compress and decompress data the synthetic data vault library (Patki et al., 2016). Look-
into a low-dimensional space and then use the decompress ing at the system architecture from design cycle one, the
Table 5 Thresholds for privacy
Measure Threshold Literature
measures in medical synthetic
data generation literature Nearest neighbor adversarial accuracy 0.030 Yale et al. (2020)
Membership inference risk precision close to 0.5 Zhang et al., (2019, Appendix D)
Choi et al., (2018, Appendix F)

Electronic Markets (2025) 35:7 Page 13 of 28 7
local and global data layers were implemented, resulting two stages. The first one covered the performance of indi-
in an ecosystem that allows data ingestion, synthetic data vidual synthetic data generation algorithms, thus helping us
generation, and data sharing. Furthermore, the ecosystem to validate DP2, while the second one looked at the overall
was created in a way that allows to switch between differ- benefit of the proposed synthetic data ecosystem. In the first
ent synthetic data generation methods, thus enabling the stage, the focus was on evaluating the performance of dif-
evaluation of different algorithms for financial transaction ferent generation algorithms (Fig. 4), revealing that GMMs
data generation.2 (ROC AUC score 0.52) and TimeGANs (ROC AUC score
0.5) underperformed expectations. This can be explained by
Evaluation of synthetic financial data generation
the composition of the data. While GMMs struggled with
algorithms
the high dimensionality of the data (148 features), TimeG-
ANs had problems with short transaction chains (below 2
This evaluation compares the different synthetic data gener- transactions per user) due to the short observation period.
ation approaches outlined before. As a real-world source for While CTGAN (ROC AUC score 0.59) performed a little
performance comparison, the credit card transaction data- better, TVAE (ROC AUC score 0.89) excelled, particularly
set from the IEEE-CIS Kaggle competition3 was chosen. thriving in scenarios with limited training data, notably in
This dataset was selected because credit card transactions, datasets for “Discover” and “American Express,” which
reflecting user spending patterns, are closely comparable to had fewer than 10,000 transactions. Thus, confirming that
bank transactions. Furthermore, it was the only real dataset the selection of the right algorithm is crucial and therefore
identified, which allowed matching transactions to users, validating DP2.
allowing for models expecting time series data to be trained. Next, we analyzed the privacy implications of the pro-
However, limitations exist, such as the limited observation posed algorithms, ensuring that the tested algorithms meet
period (6 months), many obscured features as well as the the previously defined privacy objectives and thus can be
inability to identify senders of payments but only receivers. used in our proposed synthetic data ecosystem. As can be
As we aim to analyze the benefits of sharing synthetic data seen in Table 6, apart from TIMEGAN, all of the proposed
across financial institutions, we split the dataset by credit algorithms stay within our previously defined privacy thresh-
card provider, creating four distinct subsets. An analysis olds, leading us to the conclusion that, for the proposed
across subsets showed significant differences, aligning with dataset, GMM, CTGAN, and TVAE are able to sufficiently
anticipated variations in multi-institutional bank datasets. obscure the data and can thus be used in our ecosystem.
After obtaining a suitable dataset, we defined our evalu- The second-stage evaluation assessed the advantage of
ation process. For this, first, a Bayesian parameter search training on shared synthetic data versus isolated real data.
was used to tune the hyperparameters of the different syn- Figure 5 compares the performance of models trained on
thetic data generation models using a subsample of 100,000 isolated real data, isolated synthetic data, shared synthetic
data points for each institution.4 After selecting the best data, and shared synthetic data combined with isolated
hyperparameter combination for each generation model, an real data. Models trained solely on synthetic data from one
XGBoost classifier (commonly used in fraud detection as
per Interview with Interviewee 5 as well as Al-Hashedi and
Magalingam (2021)) was trained on either real data, syn-
thetic data, or combination of both (hyperparameter where
tuned using threefold cross-validation). The results of this
process were assessed using the ROC AUC score on a hold-
out dataset (30% of the total data). The ROC AUC score
was chosen as it provides a comprehensive evaluation of the
classifier’s performance across different levels of sensitivity
and specificity and is frequently used in the literature (Sun
et al., 2023). Furthermore, the evaluation was conducted in
2 The full implementation of Cycle 2 can be found on https:// github.
com/ Farum an/ Synth eticD ataEc osyst ems/ blob/ master/ Cycle2_ Algor
ithmC ompar ison/ README. MD
3 https:// www. kaggle. com/c/ ieee- fraud- detec tion
4 A detailed description of the hyperparameter tuning procedure can be
found here:https:// github. com/ Farum an/ Synth eticD ataEc osyst ems/ blob / Fig. 4 Comparison between different synthetic data generation algo-
master/ Cycle2_ Algor ithmC ompar ison/ 02_ param Search/ README. MD rithms

7 Page 14 of 28 Electronic Markets (2025) 35:7
Table 6 Privacy measures per
Measure GMM CTGAN TVAE TIMEGAN
algorithm
Nearest neighbor adver- 0.000554 0.00189 0.001499 0.000241
sarial accuracy
Membership inference 0.485238 0.489603 0.469872 0.130435
risk precision
source underperformed compared to those trained on real critiques emerged: the constraint that the design was only
data. Yet, combining synthetic data from multiple sources validated in a singular context on a single dataset, which
led to a further performance drop, likely due to varying poses questions about its generalizability, and the inher-
fraud cases across providers, which dilutes relevant pat- ent challenges in establishing such an ecosystem, particu-
terns. However, merging synthetic with real data for each larly concerning the incentivization mechanisms required
institution boosted performance, increasing the ROC AUC to encourage active participation among the financial
score by 1%. institutions.
To better understand the impact of this improvement, we
can look at the recall or what percentage of fraudulent cases
Cycle 3: Local synthetic data recombination
are identified. Using synthetic and real data combined, we
and usage
find that 2.14% more true positives are detected. Combining
this with an estimated number of 24.16 million fraudulent
card transactions per year only in the EU (European Cen- In the third cycle, we expanded the scope of our data ecosys-
tral Bank, 2021), the improved model would have detected tem design to address a broader range of applications beyond
about half a million additional transactions. Thus, showing fraud detection, aiming to validate the DPs’ versatility and
the benefit of our ecosystem. However, this fusion of shared robustness in two contexts. Furthermore, the design ele-
synthetic data with local real data is not yet reflected in any ments of the local data level were investigated in more detail,
DP; however, the evaluation showed it to be a critical princi- resulting in the refinement and validation of DP5 and DP2.
ple of our proposed design. Thus, a new DP: DP5—Provide
Design of mechanisms at the local data level
the capability to combine synthetic data to find an optimal
composition for the training of machine learning models
given scenarios with data from multiple institutions was cre- Building on the expert feedback, in this iteration of our
ated, incorporating this important design criterion. Based on research, we broaden the scope of our data ecosystem design
this the proposed system architecture was revised, which can to encompass a wider range of applications, aiming to demon-
be seen below (Fig. 6). strate the versatility and robustness of our DPs in various con-
Moreover, the outcomes of this design cycle were pre- texts. Furthermore, this iteration focuses on investigating the
sented to additional experts in the field and two primary design elements on the local data level, thus providing design
knowledge for the individual institutions within the ecosystem.
On the one hand, we focus on the validation and refinement of
DP5—Provide the capability to combine synthetic data to find
an optimal composition for the training of machine learning
models given scenarios with data from multiple institutions
by exploring the effect of the mixing percentage between syn-
thetic and real data. On the other hand, we investigate DP2—
Provide the system with the ability to identify, validate, and
apply context-specific synthetic data generation techniques
with mutually agreed on over-sampling in order to remove
private data, given guidelines or regulations on data sharing
in more detail by developing design recommendations on how
to train the synthetic data generation models.
To extend our investigation to new domains, we consulted the
literature and solicited input from our partner institutions, iden-
tifying money laundering detection as a significant use case that
heavily relies on machine learning (Z. Chen et al., 2018) and often
Fig. 5 Comparison between synthetic and real data combinations lacks sufficient training data (Jensen et al., 2023). Subsequently,

Electronic Markets (2025) 35:7 Page 15 of 28 7
Fig. 6 Updated system architec-
ture (version 2)
an examination of the literature regarding the enhancement of synthetic data vault library (Patki et al., 2016). Building upon
machine learning performance through the incorporation of syn- the architecture from design cycle two, the local layer was
thetic data was conducted, aiming to determine an optimal ratio of modified to accommodate for different generation schemes
real to synthetic data (mix-in percentage). While some researchers with and without oversampling as well as pre-training on
only oversample the minority class using synthetic data (Charitou the local level. Furthermore, the training scheme of the pre-
et al., 2021; Strelcenia & Prakoonwit, 2023), others train models diction model was modified so that the system was able to
exclusively on synthetic data (Sattarov et al., 2023) or combine accommodate training with different mix-in percentages.5
real with synthetic data (Dahmen & Cook, 2019). Thus, it remains
Evaluation of different training and data‑fusing
unclear if there is an optimal mix-in percentage that individual
schemes
institutions should incorporate into their design.
To find the optimal way to generate synthetic data for our
ecosystem, this section investigates data generation configu- One challenge in evaluating the broader feasibility of our
rations that utilize the entire dataset as well as those trained synthetic data sharing ecosystem is the lack of publicly
on distinct data subsets and further analyzes the benefit of available financial transaction data (Jensen et al., 2023).
different pre-processing steps during the synthesizing pro- However, multiple researchers have shown that simulated
cess. Due to the challenge of dataset imbalance, models financial transactions can be suitable for validating new
tend to be biased towards the majority class, decreasing the models or even evaluating interventions (Langevin et al.,
quality of data in the minority class; mitigating this issue, 2022; Sattarov et al., 2023). Therefore, in this as well as
oversampling can be applied during the generation process the next cycle, we will use two datasets, one for anti-money
to enhance generator robustness, albeit at the risk of distort- laundering (IBM-AML6) and one for fraudulent transac-
ing dataset composition (too many positive samples) (Kiran tions (IBM-CCF7), which were generated by using a multi-
& Kumar, 2024). Second, the construction of distinct syn- agent-based approach, simulating actors that act according
thetic data generators for each class has been proposed as to predefined rules, thus creating a stream of transactions
an alternative solution. Enabling the generator to better cap- (E. Altman et al., 2024; E. R. Altman, 2019). The resulting
ture the characteristics of each individual class. However, datasets have the advantage of being magnitudes larger in
this results in the problem that the minority class generator size (IBM-AML: 31898238/ IBM-CCF: 24386900) than the
is only trained with a small dataset, which might harm its data used in the previous cycle (IEEE-CIS: 1097231) and
generalizability (Eilertsen et al., 2021). To remedy this, Fan have a network structure more similar to the one in real data.
et al. (2022) have suggested a novel methodology where the However, due to its simulation-based nature, it might not
generator for the minority class is pre-trained using samples
from the majority class, thus circumventing the problem.
5 The full implementation of Cycle 3 can be found here: https://
Demonstration through implementation github. com/ Farum an/ Synth eticD ataEc osyst ems/ blob/ master/ Cycle3-
4_ Ecosy stemE valua tion/ README. MD
of different training and data‑fusing schemes
6 https:// www. kaggle. com/ datas ets/ ealtm an2019/ ibm- trans actio ns-
for- anti- money- laund ering- aml
In this section, we operationalized the derived DPs into a 7 https:// www. kaggle. com/ datas ets/ ealtm an2019/ credit- card- trans
prototype system in Python using a modified version of the actio ns

7 Page 16 of 28 Electronic Markets (2025) 35:7
Table 7 Distribution of data across the different banks
inhibit all characteristics found in real data. As the selected
datasets do not include a financial institution (IBM-CFF) IBM-CCF IBM-AML
or the number of financial institutions present in the data
Bank Pct of data Bank Pct of data Bank Pct of data
is too big (IBM-AML, 122333 different banks), the data
was artificially grouped. This was done by segmenting the 0 21.54% 0 5.93% 4 29.94%
data based on the location of the individual (IBM-CCF)/ 1 18.58% 1 11.90% 5 45.35%
bank (IBM-AML) connected to a transaction, creating clus- 2 39.16% 2 2.87% 6 2.12%
ters that simulate the transactional networks of hypotheti- 3 20.72% 3 1.90%
cal financial institutions. As a result, the IBM-CCF dataset
included four financial institutions with a relatively even
the synthetic data ecosystem in addressing a broad range of
data distribution, while the IBM-AML dataset emerged with
data challenges in financial services. Subsequently, we explore
seven banks of which two banks held over 75% of the data.
whether a specific mix-in percentage of real and synthetic data
This contrast in dataset composition affords a unique chance
yields optimal results for machine learning performance. To
to explore the synthetic data sharing ecosystem’s functional-
accomplish this, we systematically assess the impact on model
ity under a broad array of conditions. Moreover, an analysis
performance by varying the proportion of real and synthetic
of client distribution post-split for each provider highlighted
data used in training the models, exploring a spectrum from
significant disparities, aligning with the anticipated diversity
0% (no synthetic data) to 300% (3 times as much synthetic as
suspected within multi-institutional datasets. Details on the
real data). Figure 8 visualizes this experiment.
specific distributions are outlined in Table 7.
Observing the modest upward trajectory of the aggre-
To limit the variables of this investigation, the synthetic data
gated performance line (black), we can conclude that there
generation model and the fraud prediction model were kept
is a positive effect of adding synthetic data. However, in con-
constant. For the synthetic data generation model, the previ-
ously superior TVAE-based generator8 with hyper parameters trast to the more volatile performance trends of individual
banks (grey), it appears there is not a universally optimal
tuned to the individual institution was used. Similar to Cycle
mix-in percentage. Instead, distinct peaks in performance
2, a XGBoost classifier with hyperparameter selection using
suggest that the most effective mix-in ratios vary by bank.
threefold-cross validation was chosen as the prediction model
Consequently, we infer that allowing banks to adjust the
and the performance comparisons were done using the ROC
mix-in percentage independently is most beneficial. This
AUC score on a holdout dataset (30% of the data).
insight has been integrated into DP5, which mandates that
Before, investigating the approaches modifying the local
banks have the autonomy to determine their mix-in ratios,
layer, the transferability of synthetic transaction data sharing
leading to the updated principle: DP5—Provides the capa-
beyond transaction fraud detection was evaluated (Fig. 7). To
bility to combine synthetic data to find optimal composition
do this, we compared the average ROC AUC score between
for the training of machine learning models given scenarios
the dataset constructed for financial fraud detection (IBM-
with data from multiple institutions.
CFF) and the one constructed for anti-money laundering
Finally, we explored various configurations and preproc-
detection (IBM-AML).
essing methods for synthetic data generation to offer optimal
Figure 7 demonstrates that across both datasets, models
guidance for setting up these processes at the local level.
trained with synthetic shared data surpassed those trained
Essentially, there are two primary setups. The first, referred
without it, enhancing the ROC AUC score by 3.6% in the
to as “full,” involves training the synthetic data generation
transaction fraud dataset (IBM-CCF) and 6.6% in the anti-
model on the entire dataset. To mitigate the risk of the model
money laundering dataset (IBM-AML). This effect can be
predominantly generating samples from the majority class,
considered substantial within this context as even recently
versions that randomly oversample the minority class to a
introduced fraud detection algorithms often only increase the
specified percentage of the data (“_OS{X}”) while training
ROC-AUC score by a few percentage points (Hashemi et al.,
the synthetic data generator have been implemented. The
2023; Lebichot et al., 2021). This performance gain suggests
second setup, “sep” entails training distinct generation mod-
that the data ecosystem’s effectiveness extends beyond merely
els for each class. An extension of this approach, “sepPre”
detecting financial fraud but is also suitable for other use cases
utilizes separate generators for each class but pre-trains the
utilizing financial transaction data such as money laundering
minority class generator with majority class data. The out-
detection. Thus, confirming the versatility and potential of
comes of these varied approaches are detailed in Table 8.
The analysis of the data presented in Table 8 yields sev-
8 A detailed description of the hyperparameter tuning procedure can eral key findings. Initially, the “full” model demonstrates its
be found here: https:// github. com/ Farum an/ Synth eticD ataEc osyst
ability to surpass the baseline performance, yet models built
ems/ blob/ master/ Cycle3- 4_ Ecosy stemE valua tion/ 02_ param Search/
README. MD on the same training scheme but utilizing oversampled data

| Electronic Markets (2025) 35:7  |     |     |     | Page 17 of 28  | 7   |
| ------------------------------- | --- | --- | --- | -------------- | --- |
Fig. 7  Comparison between
models trained with and without
synthetic data for both datasets
Fig. 8  Effect of synthetic data mix-in percentage on performance
Table 8  Comparison between
|     | Dataset Method | ROC AUC score | Dataset Method | ROC AUC score |     |
| --- | -------------- | ------------- | -------------- | ------------- | --- |
different synthetic data
generation models IBM-AML Without shared data 0.7168 IBM-CCF Without shared data 0.6817
|     | Full      | 0.7371 | Full      | 0.7042 |     |
| --- | --------- | ------ | --------- | ------ | --- |
|     | fullOS_10 | 0.6435 | fullOS_10 | 0.6618 |     |
|     | fullOS_20 | 0.6199 | fullOS_20 | 0.6360 |     |
|     | sep       | 0.7209 | sep       | 0.6817 |     |
|     | sepPre    | 0.7473 | sepPre    | 0.7323 |     |
exhibit a notable decline in performance. Thus, leading us to  the minority class model is pre-trained using data from
the conclusion, that for financial transaction data, oversam- the majority class (“sepPre”), a significant performance
pling the data before training the synthetic data generation  improvement is observed, surpassing all other methods.
model is not suitable. Moreover, the “full” setup outperforms  This enhancement is primarily due to the model’s capacity
configurations where synthetic data generators are trained  to generate higher-quality samples of the minority class with
separately for each class (“sep”). This subpar performance  greater variability. Further discussions with partner institu-
stems from the “sep” model’s poor-quality synthetic data  tion experts emphasized the advantage of creating class
for the minority class, which fails to capture training data  data separately as it enhances privacy by preventing leaks
patterns due to limited training dataset size. However, when  of sensitive information like fraud rates by independently

7 Page 18 of 28 Electronic Markets (2025) 35:7
producing the samples for each class. Consequently, we have held by public regulators. To incentivize them to partici-
refined DP4 to encapsulate these insights: DP2—Provide the pate in the ecosystem and allow them to ensure data quality
system with the ability to identify, validate, and apply con- and thus increase trust, we propose DP6—Provide access
text-specific synthetic data generation techniques with mutu- for external collaborators, such as regulators, to leverage
ally agreed on over-sampling in order to remove private data, the synthetic data within the ecosystem given a diverse set
given guidelines or regulations on data sharing. of synthetic data available. This gives regulators access
to the ecosystem while adhering to the existing privacy
measures. However, it remains unclear if access to purely
Cycle 4: Network effects of financial data
synthetic data can provide enough value and thus incentiv-
sharing
ize their participation in the ecosystem. The next challenge
data ecosystems face is that all actors need to benefit from
In cycle four of our DSRM project, we delve into the global participating in the ecosystem. While we already demon-
data layer, guided by the literature and expert insights to strated in previous iterations that our data ecosystem is able
address cooperative challenges within the proposed syn- to increase the overall performance, it remains unclear how
thetic financial data ecosystems. Aiming to refine our DPs this performance gain is distributed between institutions.
to enhance the ecosystem’s capability to effectively manage To address this, further investigation is needed to check if
these challenges. adjustments to our design need to be made to create suffi-
cient incentives for all institutions. Connected to this prob-
lem is identifying the right number of participants. While
Design of mechanisms at the global data level
our previous cycles show that the ecosystem is beneficial
if all institutions participate, it remains unclear if a similar
Addressing the second aspect of expert feedback and effect exists, if only part of the institutions is included in
informed by the literature on data ecosystems, this cycle the ecosystem. To incorporate this into our DPs, DP3 was
focuses on the global data layer and its DPs to ensure that extended to not only describe the monitoring of outgoing
the created ecosystem is able to handle the challenges of synthetic data but also cover the evaluation of performance
data ecosystems described by Gelhaar and Otto (2020). gained by using the shared synthetic data from the data
Because cooperative challenges play a dominant role in ecosystem. This results in DP3—Provide the system with a
the early stage of an ecosystem, the following cycle will back-testing mechanism in order to ensure newly generated
focus on these (Autio & Thomas, 2014). In their paper, synthetic data matches in composition and fraud detection
Gelhaar and Otto (2020) describe four major cooperative training performance with real data given that data quality
challenges that need to be addressed for a data ecosystem cannot be independently verified. The last cooperative chal-
to emerge successfully. First, it is necessary to build trust lenge that needs to be overcome is interoperability through
between the participants. Second, it needs to be shown the agreement on standards. At the moment, that is already
that all actors benefit from participating in the ecosys- incorporated in DP1—Provide the system with modular
tem. Third, it is important to identify the right number of systems design in order to ensure independence of local
participants. Fourth, interoperability needs to be enabled data and cross-institutional proliferation of synthetic data
through the agreement on standards. Thus, the focus of given that the raw data is sensitive, from a data perspective
this section is to evaluate existing DPs through this lens where the local layer of the ecosystem is used to align the
and analyze whether refinements or additional principles data so that it can be easily shared with the system later.
are necessary for the development of an ecosystem capa- Furthermore, we argue that creating DPs for the financial
ble of effectively addressing these challenges. First, trust data ecosystem contributes to the standardization of the
between ecosystem partners can be built in multiple ways. ecosystem from an infrastructure and ecosystem perspec-
On the one hand, trust can be increased by adequate con- tive and thus by creating these DPs we contribute to over-
trol mechanisms (Geisler et al., 2021), which is already coming this challenge.
reflected in DP3—Provide the system with a back-testing
Demonstration through the introduction
mechanism in order to ensure newly generated synthetic
of non‑sharing entities and individual performance
data matches in composition and fraud detection training
benchmarking
performance with real data given that data quality can-
not be independently verified which ensures sufficient data
quality in the synthetic data ecosystem. On the other hand, In this part, we further improved the prototype developed
Majava et al. (2016) show that intermediaries play a signifi- in Python, by altering the global data layer to allow for the
cant role in increasing participants’ trust in an ecosystem. participation of entities that do not contribute data. Addi-
In the financial services ecosystem, this role is typically tionally, we updated the system to track and report the

Electronic Markets (2025) 35:7 Page 19 of 28 7
Fig. 9 Regulator models using different resampled data and performance of the regulator model (only synthetic data) vs. the bank models
performance to each participating institution, thus allowing and once trained with only real data. The results of this
institutions on an individual level to see the performance experiment can be seen in the following diagram (Fig. 9).
gain from engaging in the data ecosystem.9 The regulator model, trained exclusively on synthetic
data, exhibits performance that, while not matching that
Evaluation of ecosystems with non‑sharing entities
of the bank’s internal models (trained on a mix of real and
and individual performance benchmarking
synthetic data), remains significant. The model approaches
the performance of the bank’s baseline models (trained
Similar to the previous cycle, this evaluation again utilizes on real data only), as illustrated in Fig. 9. This capability
the two synthetic datasets (IBM-AML and IBM-CFF), due offers considerable advantages to collaborators who would
to their high data quality, size, and diversity. Moreover, the otherwise lack access to such data. Consequently, allowing
ecosystem setup and evaluation scheme are adopted from regulators to access synthetic data emerges as an effective
the previous cycle, utilizing the “sepPre” training scheme. strategy to foster collaboration and enhance trust in the
We start with evaluating DP6, which allows regulators ecosystem. Therefore, DP6—Provide access for external
to access purely synthetic data within the data ecosystem. collaborators, such as regulators, to leverage the synthetic
To validate this DP, the synthetic data that is provided to data within the ecosystem given a diverse set of synthetic
the regulators need to be of sufficient quality for them to data available is validated and was added to our DPs for
derive meaningful insights and effectively improve their synthetic data ecosystems.
models. However, as this cannot be easily evaluated, we Subsequently, the adjustment to DP3 is validated,
use the performance of a prediction model trained on the checking if all banks profit from the synthetic data eco-
data available to the regulator (only synthetic data) as system and evaluating if the synthetic ecosystem includ-
a proxy for the quality of the data. As the architecture ing fewer institutions is still able to profit from the net-
chosen in Cycle 3 generates separate models for different work effects of the ecosystem. To investigate this, we plot
classes, more data of a specific class can easily be gener- the performance of each institution against its baseline
ated. This is especially relevant for cases where only syn- (score without any artificial data), which can be seen
thetic data is used as no additional positive samples from below (Fig. 10).
the real data exist. Thus, the experiment conducted had As evidenced in Fig. 10 for each single bank in both
two steps. In the first step, regulator models were trained datasets, the performance increases by combining real and
on synthetic data with different amounts of minority class synthetic data. Furthermore, looking at the rightmost panel
samples (indicated by OS_{percentage of minority class of Fig. 10, it can clearly be seen that there is a negative cor-
cases}). From this selection, the over-sampling ratio with relation (− 0.09) between the performance gained by par-
the best performance was chosen and compared to the ticipating in the ecosystem and the size of the bank. Thus,
performance of the models trained at the different banks, showing that small banks over proportionally profit from
once trained on a combination of real and synthetic data, participation, providing a clear incentive for them to engage
in the ecosystem. However, even if absolute performance
gained by bigger banks is lower, we argue that they still
9 The full implementation of Cycle 4 can be found here: https:// have a sufficient incentive to participate due to their large
github. com/ Farum an/ Synth eticD ataEc osyst ems/ blob/ master/ Cycle3-
volume of transactions, where even small changes in the
4_ Ecosy stemE valua tion/ README. MD

7 Page 20 of 28 Electronic Markets (2025) 35:7
Fig. 10 Performance gain per individual bank and performance gain by institution size
fraud detection percentage result in a high absolute sum of members needing to participate in the ecosystem, thus tack-
of prevented losses. These results lead us to the conclu- ling another of the challenges outlined previously.
sion that all banks contributing to the ecosystem profit from Summarizing these results, we were able to demonstrate
their involvement and thus the designed ecosystem is able to that the proposed data ecosystem is able to deliver excess
overcome another one of the previously outlined challenges. performance for all participants in the network on an indi-
Next, we investigate our synthetic data ecosystem for vidual level and it can be seen that even for data ecosys-
cases where not all institutions engage in synthetic data tems with only a fraction of the institutions participating in
sharing. To achieve this, we simulated environments, where synthetic data sharing, still a significant performance gain
none, 50%, 75%, or 100% of all banks were part of the eco- can be achieved. Furthermore, there seem to be network
system. The results can be seen in Fig. 11. effects to some extent where more partners in the ecosys-
Despite the significant difference between the two data tem increase its overall utility. As these results validate the
sets regarding their data distribution (with IBM-CCF having incentives for partners to participate in an ecosystem, we
an equal distribution between banks, while IBM-AML has a confirm our DP3—Provide the system with a back-testing
highly skewed one), we can clearly see that in both cases, even mechanism in order to ensure newly generated synthetic
with only half of the banks being part of the ecosystem (IBM- data matches in composition and fraud detection training
CCF: 2 banks/IBM-AML: 3 banks), a significant performance performance with real data given that data quality cannot
gain is achieved. Thus, it seems the benefits of the synthetic be independently verified.
data ecosystem can be realized from an early stage onwards,
making it easy to overcome the hurdle of a minimum number
Discussion
This research paper is aimed at extending the research on
privacy in data ecosystems as well as machine learning of
multi-organizational datasets by investigating these chal-
lenges in the field of financial fraud detection. This was done
by deriving DPs for an innovative synthetic data-sharing
ecosystem that allows financial institutions to exchange
financial transaction data while protecting client privacy
and learning effectively from this multi-institutional data.
To create this artifact, we followed the process of DSRM
(Peffers et al., 2007), with this paper covering four “design-
implement-evaluate” cycles. Starting with the problem iden-
tification our study contributes to descriptive knowledge
concerning the problem space by identifying data scarcity
in combination with the inability to share data due to pri-
vacy protection as a major hurdle for financial institutions,
validating the existing research on cross-organizational
fraud detection collaboration within financial services
Fig. 11 Performance (avg per bank) by percentage of participating (Abdul Salam et al., 2024; Kong et al., 2024). During the
institutions exploration of the solution, space synthetic data sharing

Electronic Markets (2025) 35:7 Page 21 of 28 7
was identified as an underexplored solution to tackle data need to be made to the composition of the data by artificially
scarcity in financial fraud detection extending the literature rebalancing it.
on cross-organizational collaboration in the field (Chatter- As can be seen in Table 9’s ecosystem dimension, our
jee et al., 2024). Furthermore, the exploration of synthetic research investigates the complexities of data ecosystems,
data to allow privacy-compliant data sharing as well as our analyzing how the incentives for participation affect per-
experimentation on multi-organizational synthetic data dur- formance outcomes across various sizes of institutions.
ing multiple “design-implement-evaluate” cycles reaches This analysis also places our findings in the context of the
beyond financial services and addresses significant chal- research by Gelhaar and Otto (2020) about the initial chal-
lenges in the realm of data ecosystems (Brée et al., 2024). lenges encountered within data ecosystems. By implement-
Moreover, our research extends beyond studies that simply ing design interventions that clearly articulate performance
outline the requirements of such a data ecosystem (Immonen benefits and facilitate the integration of external collabora-
et al., 2014). We validate these requirements and the derived tors, our research substantiates the ecosystem’s capacity to
DPs through rigorous experimentation on publicly available overcome these early hurdles. Further, our empirical evi-
datasets and through close collaboration with industry part- dence suggests that even partial participation in the data eco-
ners and experts, ensuring the practical applicability and system can lead to substantial performance improvements,
robustness of our findings. Furthermore, by extending data thereby affirming the ecosystem’s operational feasibility and
ecosystem research into a less frequently explored domain enhancing its attractiveness to potential participants.
(Cappiello et al., 2020), we are able to validate the applica- In the last dimension in Table 9, we demonstrate the
bility of existing knowledge and uncover new insights with generalizability of our derived design knowledge beyond
potential for generalization. We achieve this by developing a single use case and application area. This was done in
prescriptive knowledge and nascent theory concerning the two ways. First, through validation with experts from the
solution space, offering a set of DPs for designing a synthetic field in academia and the private sector. Second, through
data sharing ecosystem and providing a first instantiation in performance evaluation in two financial services domains
the form of a platform architecture. To provide more detailed and three datasets which required data sharing with privacy
insights into this solution space, additional key findings are restrictions. While performance gains might seem insignifi-
encapsulated in Table 9, clustered by key areas which we cant, small changes in fraud detection rate can have major
deductively derived a posteriori from our study. implications on financial institutions (Levi, 1998). Thus, our
As shown in Table 9 under the generation dimension, we research not only confirms the relevance of our DPs and sys-
contribute to the literature on synthetic data generation in tem architecture but also sets the stage for their application
multiple ways. First, we identified the necessity for a strictly beyond the immediate context of financial transactions, sug-
separated local layer (where real data is transformed) and gesting a blueprint for extending beyond financial services
a global layer (where data is shared). Second, we transfer to other domains where data needs to be shared with privacy
existing algorithms to a new setup including cross-organ- restrictions (Susha et al., 2019).
izational data with a complex data structure and compare For practitioners, our contribution is two-fold: For man-
their performance on a prediction task (Pathare et al., 2023) agers and decision-makers, we demonstrate the value of
identifying TVAE as the most performant algorithm for syn- synthetic data-sharing ecosystems that allow both large
thetic financial data generation while still showing sufficient and small institutions to securely collaborate on data while
privacy. Third, we extend the research on the generation ensuring privacy. This approach is particularly relevant in
setup by consolidating different training schemes from mul- industries with complex, highly sensitive data, such as finan-
tiple sources (Eilertsen et al., 2021; Fan et al., 2022; Kiran & cial services, where data ecosystems do not emerge organi-
Kumar, 2024) and comparing them to each other, identifying cally and require careful planning allowing for shared value
training on data sub-clusters as the most beneficial setup. propositions and services (Adner, 2017; Immonen et al.,
Moving forward to training models based on synthetic 2014). Furthermore, our framework addresses regulatory
data, as shown in Table 9 under the prediction dimension, requirements on data privacy and our results suggest a
we extend the literature which often looks at synthetic data robust foundation for scaling and sustaining privacy-focused
generation performance separately but provides little guid- data ecosystems. For system architects, we outline a set of
ance on how the generated data is best used in a data eco- DPs that guide practitioners in structuring the architecture
system (Dankar et al., 2022). Our research further shows of these ecosystems. These principles assist in selecting
that a mixture of synthetic and real data is most useful when suitable synthetic data generation methods, implementing
combined; however, the exact mix-in percentage is highly mechanisms for data quality assurance, and integrating data
organization and context-specific. Moreover, we demon- to enhance AI model performance. By focusing on these
strated that using purely synthetic data can still be beneficial core areas, our contribution provides architects with action-
for players with no access to real data; however, adjustments able guidance toward building secure and resilient synthetic

7 Page 22 of 28 Electronic Markets (2025) 35:7
selcyc
etaulave-tnemelpmi-ngised
ruof
eht ni
detareneg
sthgisni
fo
yrammuS
9
elbaT
gninosaeR
seitivitcA
sucoF
thgisni
fo
aerA
-ogla
,raludom
a
fo
noitceles
eht
ot
dael
sesylana
ehT
atad
citehtnys
ralupop
fo nosirapmoc
ecnamrofreP
-
citehtnys
elbatius
tsom
eht sefiitnedi
noisnemid
sihT
noitareneG
neewteb
setarapes
ylraelc
taht
hcaorppa
citsonga-mhtir
-casnart
laicnanfi
dlrow-laer
no smhtirogla
noitareneg
rof putes
lamitpo
eht
dna
mhtirogla
noitareneg
atad
noitargetni
atad
lamitpo
,rehtruF
.sreyal
labolg
dna
lacol
-moc
*%8.94
yb
EAVT
fo ecnamrofreptuo(
atad
noit
ecnamrofrep
ecnahne
ot atad
citehtnys
gnitareneg
s’metsysoce
eht
gninedaorb
defiitnedi
erew
seigetarts
)ledom
tseb
txen ot
derap
laitnetop
ecnamrofrep
sti
gnicnahne
dna
ytilibacilppa
-tareneg
nehw
putes
gniniart
lamitpo
eht
fo noitaulavE
-
deniart-erp
fo ecnamrofreptuo(
atad
citehtnys
gni
txen
ot derapmoc
*%0.2
yb sledom
detarapes-ssalc
)emehcs
gniniart
tseb
deroliat
fo
noitacfiitnedi
eht
etatilicaf
snoitagitsevni
esehT
neewteb
egatnecrep
ni-xim
lamitpo
eht
fo noitaulavE
-
gniniart
fo
scfiiceps
eht
no sesucof
noisnemid
sihT
noitciderP
cfiiceps
eht
etadommocca
taht
sehcaorppa
gniniart
level
lanoitutitsni
eht no atad
citehtnys
dna
laer
ni yllaicepse
,noitareneg
atad
citehtnys
rof
sputes
eht
gnirusne
,stnapicitrap
s’metsysoce
eht
fo
sdeen
gnisu
atad
citehtnys
ylerup
fo noitaulave
ecnamrofreP
-
sessalc
decnalabmi
htiw
stxetnoc
-ciderp
gnizimixam-ytilitu
,ytilauq-hgih
fo noitareneg
fo
ecnamrofreptuo(
gnilpmasrevo
fo
seerged
tnereffid
sledom
noit
ton
ot derapmoc
*%5.7
yb
gnilpmasrevo
%01 htiw
atad
)enilesab
delpmasrevo
eht
ssorca
tfieneb
lanoitroporp
a etacidni
sgnidnfi
ehT
-utitsni
laicnanfi
rep
niag ecnamrofrep
fo sisylanA
-
ni ecnalab
s’metsysoce
eht sessessa
noisnemid
sihT
metsysocE
rof
segatnavda
ralucitrap
gnithgilhgih
,metsysoce
dna
ezis
noitutitsni
neewteb
pihsnoitaler
eht dna
noit
fo
snoitutitsni
ssorca
sevitnecni
noitapicitrap
fo
smret
-oce
laitrap
neve
,eromrehtruF
.snoitutitsni
rellams
)90.0
− fo
noitalerroc
evitagen(
niag
ecnamrofrep
noitapicitrap
laitrap
fo
tceffe eht
dna
sezis
gniyrav
ecnamrofrep
laitnatsbus
sdleiy
noitapicitrap
metsys
-yrav
htiw
ecnamrofrep
s’metsysoce
eht
fo noitaulavE
-
dna
ytilibaiv
s'metsys
eht
gnirusne
,suhT
.stnemevorpmi
tnacfiingis(
snoitutitsni
gnitapicitrap
fo srebmun
gni
ssenevitcartta
)sezis
metsysoce
lla htiw
niag
ecnamrofrep
-libacilppa
dna
ecnaveler
eht
demrfinoc
noitaulave
ehT
laicnanfi
morf
strepxe
htiw
sweivretni
derutcurts-imeS
-
eht etadilav
ot
smia
ytilibazilareneg
fo
noisnemid
ehT
ytilibazilareneG
laicnanfi
elpitlum
ssorca
egdelwonk
ngised
eht
fo
yti
-erc
eht
etadilav
ot
strepxe
cimedaca
dna snoitutitsni
erutcetihcra
metsys
dna
egdelwonk
ngised
detaerc
sniamod
secivres
erutcetihcra
metsys
dna sPD
deta
sevitcepsrep
’strepxe
dna stxetnoc
esrevid
ssorca
wen
ot putes
gnirahs
atad citehtnys
eht fo refsnarT
-
ecnamrofrep
devorpmi(
noitceted
duarf
ekil stxetnoc
devorpmi(
noitceted
gnirednual
yenom
dna )*%6.3
yb
-atad
desab-noitalumis
gnisu )*%6.6
yb ecnamrofrep
stes
serocs
CUA
COR
no
desab
noitaulave
ecnamrofreP
*

Electronic Markets (2025) 35:7 Page 23 of 28 7
data-sharing ecosystems. This framework, therefore, serves unlocking the potential for data-driven innovation and future
as a blueprint for future system designers working within economic development.
regulated environments where data privacy and AI perfor-
Acknowledgements The authors express their gratitude to the Union-
mance are essential.
Bank of the Philippines for their valuable collaboration and the provi-
Limitations and future research opportunities can be iden-
sion of key insights that contributed to this research. This research pro-
tified across our four key areas of insight. Regarding data ject was funded by the St. Gallen Symposium and the German Federal
generation, the current study was constrained by the avail- Ministry of Education and Research (BMBF) within the “Innovations
for Tomorrow’s Production, Services, and Work” Program (funding
able data, which prevented the consideration of advanced
number 02K23A001) which is managed by the Project Management
graph-based synthetic data generation methods such as
Agency Karlsruhe (PTKA). The authors are responsible for the content
TransGAN (X. Wang & Yang, 2024). Additionally, while of this publication.
privacy was tested, it was not fully guaranteed by the mod-
Funding Open access funding provided by University of St. Gallen.
els used, highlighting the need for future research on the
effectiveness of differentially private synthetic data genera- Data Availability The datasets used during the current study are avail-
tion methods such as PATEGAN (Jordon et al., 2018) in able in the Kaggle repositories: https://w ww.k aggle.c om/c/i eee-f raud-
a synthetic data ecosystem. From a prediction standpoint, detect ion, https://w ww.k aggle.c om/d atase ts/e altma n2019/i bm-t rans
action s-f or-a nti-m oney-l aunde ring-a ml, https://w ww.k aggle.c om/d atas
further investigation is required to determine how models
ets/e altma n2019/c redit-c ard-t ransa ction s.
can be aligned when data schemas—and thus the synthetic
data—differ between institutions. Moreover, the design of Declarations
an effective back-testing mechanism to ensure the ecosys-
tem’s predictive performance should be explored. On the Competing Interests The authors declare that they have no conflict
of interest.
ecosystem level, additional research is necessary to explore
ecosystem usage incentives, building on the work by (Gel-
Open Access This article is licensed under a Creative Commons Attri-
haar et al., 2021), which was beyond the scope of this paper.
bution 4.0 International License, which permits use, sharing, adapta-
Finally, while this study was limited to financial services due
tion, distribution and reproduction in any medium or format, as long
to resource constraints, future research should explore the as you give appropriate credit to the original author(s) and the source,
applicability of the defined DPs beyond this domain, testing provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article are
their general applicability.
included in the article's Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in
the article's Creative Commons licence and your intended use is not
Conclusion permitted by statutory regulation or exceeds the permitted use, you will
need to obtain permission directly from the copyright holder. To view a
copy of this licence, visit http://c reati vecom mons.o rg/l icens es/b y/4.0 /.
Based on the need for increased data availability to foster
economic growth, this paper provides the design and evalu-
ation of a synthetic data-sharing ecosystem for financial
institutions under privacy constraints. The main contribution References
lies in providing guidance on how to train models based on
shared data. By formulating a set of DPs, practical insights, Abbas, A. E., Agahari, W., van de Ven, M., Zuiderwijk, A., & de
and prototype testing, iterative design cycles were used to Reuver, M. (2021). Business data sharing through data market-
places: A systematic literature review. Journal of Theoretical and
provide a robust framework for constructing a data ecosys-
Applied Electronic Commerce Research, 16(7), 7. https://d oi.o rg/
tem that leverages synthetic data. Each DP, from ensuring
10.3 390/j taer1 60701 80
data quality and enhancing adaptability through transforma- Abdul Salam, M., Fouad, K. M., Elbably, D. L., & Elsayed, S. M.
tion and resampling to fostering trust among ecosystem par- (2024). Federated learning model for credit card fraud detec-
tion with data balancing techniques. Neural Computing and
ticipants and facilitating regulatory access to synthetic data,
Applications, 36(11), 6231–6256. https://d oi. org/1 0.1 007/
extends existing research on synthetic data sharing and gen-
s00521-0 23-0 9410-2
eration, particularly in the context of financial transaction Adner, R. (2017). Ecosystem as structure: An actionable construct for
data. For practice, our example instantiation and codebase strategy. Journal of Management, 43(1), 39–58. https://d oi.o rg/
10.1 177/0 14920 63166 78451
can be used as a reference architecture for future instantia-
Al-Hashedi, K. G., & Magalingam, P. (2021). Financial fraud detection
tions. We not only address the identified need for an efficient,
applying data mining techniques: A comprehensive review from
privacy-preserving financial data ecosystem but also set a 2009 to 2019. Computer Science Review, 40, 100402. https://d oi.
foundation for future exploration in broader domains where org/1 0.1 016/j.c osrev.2 021.1 00402
Altman, E., Blanuša, J., von Niederhäusern, L., Egressy, B., Anghel,
data sharing under privacy restrictions is paramount. Thus,
A., & Atasu, K. (2024). Realistic synthetic financial transac-
this contribution offers guidance for overcoming technical, tions for anti-money laundering models (No. arXiv:2 306.1 6424).
trust-related, and regulatory challenges in data ecosystems, arXiv. https://d oi.o rg/1 0.4 8550/a rXiv.2 306.1 6424

7 Page 24 of 28 Electronic Markets (2025) 35:7
Altman, E. R. (2019). Synthesizing credit card transactions (No. Brée, T., Karger, E., & Ahlemann, F. (2024). Shaping the future of data
arXiv:1 910.0 3033). arXiv. https://d oi.o rg/1 0.4 8550/a rXiv. ecosystem research—What is still missing? IEEE Access, 12,
1910.0 3033 103162–103175. IEEE Access. https://d oi.o rg/1 0.1 109/A CCESS.
Asrow, K. (2021). The role of individuals in the data ecosystem: Cur- 2024.3 43296 9
rent debates and considerations for individual data protection Brodsky, L., & Oakes, L. (2017). Data sharing and open banking.
and data rights in the U.S. Federal Reserve Bank of San Fran- McKinsey. https://w ww.m ckins ey.c om/~ /m edia/M cKins ey/I ndus
cisco. https://p rivac ysecu ritya cadem y.c om/w p-c onten t/u pload s/ tries/F inanc ial%2 0Serv ices/O ur%2 0Insi ghts/D ata%2 0shar ing%
2021/0 5/T he-R ole-o f-I ndivi duals-i n-t he-D ata-E cosys tem.p df. 20and%2 0open%2 0bank ing/D ata-s harin g-a nd-o pen-b ankin g.p df.
Accessed 9 Mar 2023. Accessed 26 Feb 2024.
Assefa, S. (2020). Generating synthetic data in finance: Opportunities, Bun, M., Desfontaines, D., Dwork, C., Naor, M., Nissim, K., Roth, A.,
challenges and pitfalls. SSRN Electronic Journal. https://d oi.o rg/ Smith, A., Steinke, T., Ullman, J., & Vadhan, S. (2021). Statis-
10.2 139/s srn.3 63423 5 tical inference is not a privacy violation. https://d iffer entia lpri
Aurna, N. F., Hossain, M. D., Taenaka, Y., & Kadobayashi, Y. (2023). vacy.o rg/i nfere nce-i s-n ot-a-p rivac y-v iolat ion/. Accessed 14 Aug
Federated learning-based credit card fraud detection: Perfor- 2024.
mance analysis with sampling methods and deep learning algo- Cappiello, C., Gal, A., Jarke, M., & Rehof, J. (2020). Data ecosystems:
rithms. 2023 IEEE International Conference on Cyber Security Sovereign data exchange among organizations (Dagstuhl Semi-
and Resilience (CSR), 2023, 180–186. https://d oi.o rg/1 0.1 109/ nar 19391). DROPS-IDN/v2/Document/https://d oi.o rg/1 0.4 230/
CSR575 06.2 023.1 02249 78 DagRep.9 .9.6 6. https://d oi.o rg/1 0.4 230/D agRep.9 .9.6 6
Autio, E., spsampsps Thomas, L. D. W. (2014). Innovation ecosystems: Chakravarty, S., Demirhan, H., & Baser, F. (2020). Fuzzy regres-
Implications for innovation management? In M. Dodgson, D. M. sion functions with a noise cluster and the impact of outliers on
Gann, spsampsps N. Phillips (Eds.), The Oxford Handbook of mainstream machine learning methods in the regression setting.
Innovation Management (p. 0). Oxford University Press. https:// Applied Soft Computing, 96, 106535. https://d oi.o rg/1 0.1 016/j.
doi.o rg/1 0.1 093/o xford hb/9 78019 96949 45.0 13.0 12 asoc.2 020.1 06535
Awosika, T., Shukla, R. M., & Pranggono, B. (2024). Transparency Chandra, L., Seidel, S., & Gregor, S. (2015). Prescriptive knowledge in
and privacy: The role of explainable AI and federated learning in IS research: Conceptualizing design principles in terms of mate-
financial fraud detection. IEEE Access, 12, 64551–64560. https:// riality, action, and boundary conditions. 2015 48th Hawaii Inter-
doi.o rg/1 0.1 109/A CCESS.2 024.3 39452 8. IEEE Access. national Conference on System Sciences, 4039–4048. https://d oi.
Baabdullah, T., Alzahrani, A., Rawat, D. B., & Liu, C. (2024). Effi- org/1 0.1 109/H ICSS.2 015.4 85
ciency of federated learning and blockchain in preserving privacy Charitou, C., Dragicevic, S., & Garcez, A. d’Avila. (2021). Synthetic
and enhancing the performance of credit card fraud detection data generation for fraud detection using GANs (No. arXiv:2 109.
(CCFD) systems. Future Internet, 16(6), 6. https://d oi.o rg/1 0. 12546). arXiv. http://a rxiv.o rg/a bs/2 109.1 2546. Accessed 11 Mar
3390/fi 1606 0196 2024.
Bagad, P., Mitra, S., Dhamnani, S., Sinha, A. R., Gautam, R., & Chatterjee, P., Das, D., & Rawat, D. B. (2024). Digital twin for credit
Khanna, H. (2021). Data-sharing economy: Value-addition from card fraud detection: Opportunities, challenges, and fraud detec-
data meets privacy. Proceedings of the 14th ACM International tion advancements. Future Generation Computer Systems, 158,
Conference on Web Search and Data Mining, 1105–1108. https:// 410–426. https://d oi.o rg/1 0.1 016/j.f uture.2 024.0 4.0 57
doi.o rg/1 0.1 145/3 43796 3.3 44171 2 Chen, Z., Van Khoa, L. D., Teoh, E. N., Nazir, A., Karuppiah, E. K., &
Baskerville, R., Baiyere, A., Gregor, S., Hevner, A., & Rossi, M. Lam, K. S. (2018). Machine learning techniques for anti-money
(2018). Design science research contributions: Finding a bal- laundering (AML) solutions in suspicious transaction detection:
ance between artifact and theory. Journal of the Association for A review. Knowledge and Information Systems, 57(2), 245–285.
Information Systems, 19(5). https://a isel.a isnet.o rg/j ais/v ol19/ https://d oi.o rg/1 0.1 007/s 10115-0 17-1 144-z
iss5/3. Accessed 13 June 2023. Chen, H., Grossman, M., Sen, A., & Tsao, S.-F. (2023). Establish-
Bauer, A., Trapp, S., Stenger, M., Leppich, R., Kounev, S., Leznik, ing a FAIR, CARE, and efficient synthetic health data shar-
M., Chard, K., & Foster, I. (2024). Comprehensive explora- ing ecosystem for canada establishing a FAIR, CARE, and
tion of synthetic data generation: A survey (No. arXiv:2 401. efficient synthetic health data sharing ecosystem for Canada.
02524). arXiv. https://a rxiv.o rg/a bs/2 401.0 2524. Accessed 15 IARIW-CIGI Conference on the Valuation of Data. https://
Aug 2024. www. resea rchga te. net/ publi cation/ 37544 6378_ Estab lishi
Benchaji, I., Douzi, S., & Ouahidi, B. E. (2021). Credit card fraud ng_a_F AIR_C ARE_a nd_E ffici ent_S ynthe tic_H ealth_D ata_
detection model based on LSTM recurrent neural networks. Sharin g_E cosys tem_f or_C anada_E stabl ishin g_a_F AIR_
Journal of Advances in Information Technology, 12(2), 113–118. CARE_a nd_E ffici ent_S ynthe tic_H ealth_D ata_S harin g_E cosy
https://d oi.o rg/1 0.1 2720/j ait.1 2.2.1 13-1 18 stem_f or_C anada. Accessed 17 Dec 2024
Bian, K., & Zheng, H. (2023). FedAvg-DWA: A novel algorithm for Choi, E., Biswal, S., Malin, B., Duke, J., Stewart, W. F., & Sun, J.
enhanced fraud detection in federated learning environment. (2018). Generating multi-label discrete patient records using
2023 4th International Conference on Big Data, Artificial Intel- generative adversarial networks (No. arXiv:1 703.0 6490). arXiv.
ligence and Internet of Things Engineering (ICBAIE), 13–17. https://d oi.o rg/1 0.4 8550/a rXiv.1 703.0 6490
https://d oi.o rg/1 0.1 109/I CBAIE 59714.2 023.1 02813 17 Cosma, S., Cosma, S., & Pennetta, D. (2023). The rise of financial ser-
Blake, M., McWaters, J., & Galaski, R. (2019). The next generation of vices ecosystems: Towards open banking platforms. In T. Walker,
data-sharing in financial services (p. 33) [White Paper]. World E. Nikbakht, & M. Kooli (Eds.), The Fintech Disruption: How
Economic Forum. https://w ww2.d eloit te.c om/c onten t/d am/D eloi Financial Innovation Is Transforming the Banking Industry (pp.
tte/ lu/ Docum ents/ finan cial- servi ces/ lu- next- gener ation- data- 191–213). Springer International Publishing. https://d oi.o rg/1 0.
sharin ging-fi nanc ial-s ervic es.p df. Accessed 29 Jan 2023. 1007/9 78-3-0 31-2 3069-1_8
Bonabeau, E. (2002). Agent-based modeling: Methods and techniques Dahmen, J., & Cook, D. (2019). SynSys: A synthetic data generation
for simulating human systems. Proceedings of the National system for healthcare applications. Sensors, 19(5), 5. https://d oi.
Academy of Sciences, 99(suppl_3), 7280–7287. https://d oi.o rg/ org/1 0.3 390/s 19051 181
10.1 073/p nas.0 82080 899 Dankar, F. K., Ibrahim, M. K., & Ismail, L. (2022). A multi-dimen-
sional evaluation of synthetic data generators. IEEE Access, 10,

Electronic Markets (2025) 35:7 Page 25 of 28 7
11147–11158. https://d oi.o rg/1 0.1 109/A CCESS.2 022.3 14476 5. Gregor, S., Chandra Kruse, L., & Seidel, S. (2020). The anatomy of
IEEE Access. a design principle. Journal of the Association for Information
Demirgüç-Kunt, A., Klapper, L., Singer, D., & Ansar, S. (2022). The Systems, 21, 1622–1652. https://d oi.o rg/1 0.1 7705/1 jais.0 0649
global findex database 2021—Financial inclusion, digital pay- Gregor, S., Kruse, L. C., & Seidel, S. (2020). Research perspectives:
ments, and resilience in the age of COVID-19. International Bank The anatomy of a design principle. Journal of the Association
for Reconstruction and Development / The World Bank. https:// for Information Systems, 21(6). https://d oi.o rg/1 0.1 7705/1 jais.
openk nowle dge. world bank. org/ bitst ream/ handle/ 10986/ 37578/ 00649
978146 48189 74.p df. Accessed 22 Jan 2023. Gröger, C. (2021). There is no AI without data. Communications of the
Eilertsen, G., Tsirikoglou, A., Lundström, C., & Unger, J. (2021). ACM, 64(11), 98–108. https://d oi.o rg/1 0.1 145/3 44824 7
Ensembles of GANs for synthetic training data generation (No. Hashemi, S. K., Mirtaheri, S. L., & Greco, S. (2023). Fraud detection
arXiv:2 104.1 1797). arXiv. https://d oi.o rg/1 0.4 8550/a rXiv.2 104. in banking data by machine learning techniques. IEEE Access,
11797 11, 3034–3043. https://d oi.o rg/1 0.1 109/A CCESS.2 022.3 23228 7.
Emam, K. E., Mosquera, L., & Bass, J. (2020). Evaluating identity He, Z., Huang, J., & Zhou, J. (2023). Open banking: Credit market
disclosure risk in fully synthetic health data: Model development competition when borrowers own the data. Journal of Financial
and validation. Journal of Medical Internet Research, 22(11), Economics, 147(2), 449–474. https://d oi.o rg/1 0.1 016/j.j finec o.
e23139. https://d oi.o rg/1 0.2 196/2 3139 2022.1 2.0 03
Esteban, C., Hyland, S. L., & Rätsch, G. (2017). Real-valued (medi- Heimstädt, M., Saunderson, F., & Heath, T. (2014). Conceptualizing
cal) time series generation with recurrent conditional GANs Open Data ecosystems: A timeline analysis of Open Data devel-
(No. arXiv:1 706.0 2633). arXiv. http://a rxiv.o rg/a bs/1 706.0 2633. opment in the UK. [13] S. https://d oi.o rg/1 0.1 7169/F UDOCS_
Accessed 14 Aug 2024. DOCUME NT_0 00000 02033 2
European Central Bank. (2021). Seventh report on card fraud. 2021. Heinz, D., Benz, C., Fassnacht, M., & Satzger, G. (2022). Past, present
https://w ww.e cb.e uropa.e u/p ub/c ardfr aud/h tml/e cb.c ardfr audr and future of data ecosystems research: A systematic literature
eport2 02110 ~cac4c4 18e8.e n.h tml. Accessed 16 June 2023. review. PACIS 2022 Proceedings. 46. https://a isel.a isnet.o rg/
Fan, X., Guo, X., Chen, Q., Chen, Y., Wang, T., & Zhang, Y. (2022). pacis2 022/4 6/. Accessed 18 Dec 2024.
Data augmentation of credit default swap transactions based on Hevner, A. R., March, S., Park, J., & Ram, S. (2004). Design science
a sequence GAN. Information Processing & Management, 59(3), in information systems research. Management Information Sys-
102889. https://d oi.o rg/1 0.1 016/j.i pm.2 022.1 02889 tems Quarterly, 28(1). https://a isel.a isnet.o rg/m isq/v ol28/i ss1/6.
Fassnacht, M. K., Benz, C., Leimstoll, J., & Satzger, G. (2023). Is Accessed 13 Nov 2024.
your organization ready to share? A framework of beneficial Hevner, A., & Gregor, S. (2022). Envisioning entrepreneurship and
conditions for data sharing. 44th International Conference digital innovation through a design science research lens: A
on Information Systems (ICIS 2023), Hyderabad, Indien, matrix approach. Information & Management, 59(3), 103350.
10.12.2023 - 13.12.2023. https://d oi.o rg/1 0.5 445/I R/1 0001 https://d oi.o rg/1 0.1 016/j.i m.2 020.1 03350
62812 Hevner, A. R. (2007). A three cycle view of design science research.
Frid-Adar, M., Klang, E., Amitai, M., Goldberger, J., & Greenspan, H. Scandinavian Journal of Information Systems: Vol. 19: Iss. 2,
(2018). Synthetic data augmentation using GAN for improved Article 4. https://a isel.a isnet.o rg/s jis/v ol19/i ss2/4/. Accessed 18
liver lesion classification. 2018 IEEE 15th International Sympo- Dec 2024.
sium on Biomedical Imaging (ISBI 2018), 289–293. 2018 IEEE Hilal, W., Gadsden, S. A., & Yawney, J. (2022). Financial fraud: A
15th International Symposium on Biomedical Imaging (ISBI review of anomaly detection techniques and recent advances.
2018). https://d oi.o rg/1 0.1 109/I SBI.2 018.8 36357 6 Expert Systems with Applications, 193, 116429. https://d oi.o rg/
Geisler, S., Vidal, M.-E., Cappiello, C., Lóscio, B. F., Gal, A., Jarke, 10.1 016/j.e swa.2 021.1 16429
M., Lenzerini, M., Missier, P., Otto, B., Paja, E., Pernici, B., & Hittmeir, M., Ekelhart, A., & Mayer, R. (2019). On the utility of syn-
Rehof, J. (2021). Knowledge-driven data ecosystems toward data thetic data: An empirical evaluation on machine learning tasks.
transparency. Journal of Data and Information Quality, 14(1), Proceedings of the 14th International Conference on Availability,
3:1-3:12. https://d oi.o rg/1 0.1 145/3 46702 2 Reliability and Security, 1–6. https://d oi.o rg/1 0.1 145/3 33925 2.
Gelhaar, J., & Otto, B. (2020). Challenges in the emergence of data 333928 1
ecosystems. PACIS 2020 Proceedings. 175. https://a isel.a isnet. Iivari, J. (2007). A paradigmatic analysis of information systems as a
org/p acis2 020/1 75/. Accessed 17 Dec 2024. design science. Scandinavian Journal of Information Systems,
Gelhaar, J., Groß, T., & Otto, B. (2021). A taxonomy for data eco- 19, 39.
systems. Hawaii International Conference on System Sciences. Immonen, A., Palviainen, M., & Ovaska, E. (2014). Requirements of
https://d oi.o rg/1 0.2 4251/H ICSS.2 021.7 39 an open data based business ecosystem. IEEE Access, 2, 88–103.
Gelhaar, J., Henke, M., Gürpinar, T., & Otto, B. (2021). Towards a https://d oi.o rg/1 0.1 109/A CCESS.2 014.2 30287 2
taxonomy of incentive mechanisms for data sharing in data eco- Ishfaq, H., Hoogi, A., & Rubin, D. (2023). TVAE: Triplet-based
systems. PACIS 2021 Proceedings. 121. https://a isel.a isnet.o rg/ variational autoencoder using metric learning (No. arXiv:1 802.
pacis2 021/1 21/. Accessed 17 Dec 2024. 04403). arXiv. https://a rxiv.o rg/a bs/1 802.0 4403 . Accessed 16
Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, June 2023.
D., Ozair, S., Courville, A., & Bengio, Y. (2014). Generative Jarke, M. (2017). Data spaces: Combining goal-driven and data-driven
adversarial networks (No. arXiv:1 406.2 661). arXiv. https://d oi. approaches in community decision and negotiation support. In
org/1 0.4 8550/a rXiv.1 406.2 661 M. Schoop spsampsps D. M. Kilgour (Eds.), Group Decision
Gray, B., & Sites, J. P. (2013). Sustainability through partnerships. and Negotiation. A Socio-Technical Perspective (pp. 3–14).
Network for business sustainability. https://n bs.n et/w p-c onte Springer International Publishing. https://d oi.o rg/1 0.1 007/
nt/u pload s/2 022/0 1/N BS-S ystem atic-R eview-P artne rship s.p df. 978-3-3 19-6 3546-0_1
Accessed 18 Dec 2024. Jensen, R. I. T., Ferwerda, J., Jørgensen, K. S., Jensen, E. R., Borg, M.,
Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design Krogh, M. P., Jensen, J. B., & Iosifidis, A. (2023). A synthetic
science research for maximum impact. MIS Quarterly, 37(2), data set to benchmark anti-money laundering methods. Scientific
337–355. Data, 10(1), 661. https://d oi.o rg/1 0.1 038/s 41597-0 23-0 2569-2

7 Page 26 of 28 Electronic Markets (2025) 35:7
Jiang, D., Zhang, G., Karami, M., Chen, X., Shao, Y., & Yu, Y. (2022). Proceedings 71(5), 33–40. https://e p.l iu.s e/e n/c onfer ence-a rtic
DP$^2$-VAE: Differentially private pre-trained variational le.a spx?A rticl e_N o=5 &i ssue=7 1&s eries=e cp. Accessed 18 Dec
autoencoders (No. arXiv:2 208.0 3409). arXiv. https://d oi.o rg/ 2024.
10.4 8550/a rXiv.2 208.0 3409 Lopez-Rojas, E. A., Elmir, A., & Axelsson, S. (2016). PaySim: A
Jones, D., & Gregor, S. (2007). The anatomy of a design theory. Jour- financial mobile money simulator for fraud detection. European
nal of the Association for Information Systems, 8(5), 1. Modeling and Simulation Symposium 2016. https://w ww.m sc-
Jordon, J., Yoon, J., & Schaar, M. van der. (2018, September 27). les. org/ proce edings/ emss/ 2016/ EMSS2 016_ 249. pdf. Accessed
PATE-GAN: Generating synthetic data with differential privacy 18 Dec 2024.
guarantees. International Conference on Learning Representa- Loukides, G., Gkoulalas-Divanis, A., spsampsps Shao, J. (2010).
tions. https://o penre view.n et/f orum?i d=S 1zk9i RqF7. Accessed Anonymizing transaction data to eliminate sensitive inferences.
14 Aug 2024. In P. G. Bringas, A. Hameurlain, spsampsps G. Quirchmayr
Jordon, J., Szpruch, L., Houssiau, F., Bottarelli, M., Cherubin, G., (Eds.), Database and Expert Systems Applications (pp. 400–
Maple, C., Cohen, S. N., & Weller, A. (2022). Synthetic data— 415). Springer. https://d oi.o rg/1 0.1 007/9 78-3-6 42-1 5364-8_3 4
What, why and how? (No. arXiv:2 205.0 3257). arXiv. http://a rxiv. Lu, Y., Wang, H., & Wei, W. (2023). Machine learning for synthetic
org/a bs/2 205.0 3257. Accessed 14 Aug 2024. data generation: A review (No. arXiv:2 302.0 4062). arXiv.
Kingma, D. P., & Welling, M. (2013). Auto-encoding variational https://d oi.o rg/1 0.4 8550/a rXiv.2 302.0 4062
Bayes. CoRR. https:// www. seman ticsc holar. org/ paper/ Auto- Majava, J., Kinnunen, T., Foit, D., & Kess, P. (2016). An intermediary
Encodi ng-V ariat ional-B ayes-K ingma-W ellin g/5 f5dc5 b9a2b a710 as a trust enabler in a spatial business ecosystem. International
937e2c 413b3 7b053 cd673 df02. Accessed 16 May 2024. Journal of Innovation and Learning, 20(2), 199. https://d oi.o rg/
Kiran, A., & Kumar, S. S. (2024). A methodology and an empirical 10.1 504/I JIL.2 016.0 77845
analysis to determine the most suitable synthetic data genera- Major, T., & Mangano, J. (2020). Modernising payments messaging:
tor. IEEE Access, 12, 12209–12228. https:// doi. org/ 10. 1109/ The ISO 20022 standard. Reserve Bank of Australia. https://
ACCESS.2 024.3 35427 7 www.r ba.g ov.a u/p ublic ation s/b ullet in/2 020/s ep/p df/m odern is-
Kong, Y., Li, Z., & Jiang, C. (2024). ASIA: A federated boosting tree ing-p aymen ts-m essag ing-t he-i so-2 0022-s tanda rd.p df. Accessed
model against sequence inference attacks in financial networks. 18 Dec 2024.
IEEE Transactions on Information Forensics and Security, 19, March, S. T., & Smith, G. F. (1995). Design and natural science
6991–7004. IEEE Transactions on Information Forensics and research on information technology. Decision Support Systems,
Security. https://d oi.o rg/1 0.1 109/T IFS.2 024.3 42841 2 15(4), 251–266. https://d oi.o rg/1 0.1 016/0 167-9 236(94)0 0041-2
Kulatilleke, G. K. (2022). Challenges and complexities in machine Morley-Fletcher, E. (2022). New solutions to biomedical data shar-
learning based credit card fraud detection (No. arXiv:2 208. ing data sharing: Secure computation secure computationsand
10943). arXiv. http://a rxiv.o rg/a bs/2 208.1 0943. Accessed 18 synthetic data synthetic data. In C. Beneduce spsampsps M.
Mar 2024. Bertolaso (Eds.), Personalized Medicine in the Making: Philo-
Langer, A., spsampsps Mukherjee, A. (2023). Organizing the data eco- sophical Perspectives from Biology to Healthcare (pp. 173–189).
system. In A. Langer spsampsps A. Mukherjee (Eds.), Develop- Springer International Publishing. https://d oi.o rg/1 0.1 007/
ing a path to data dominance: Strategies for digital data-centric 978-3-0 30-7 4804-3_9
enterprises (pp. 113–141). Springer International Publishing. Mullarkey, M. T., & Hevner, A. R. (2019). An elaborated action design
https://d oi.o rg/1 0.1 007/9 78-3-0 31-2 6401-6_5 research process model. European Journal of Information Sys-
Langevin, A., Cody, T., Adams, S., & Beling, P. (2022). Generative tems, 28(1), 6–20. https://d oi.o rg/1 0.1 080/0 96008 5X.2 018.1 4518
adversarial networks for data augmentation and transfer in credit 11
card fraud detection. Journal of the Operational Research Soci- Myalil, D., Rajan, M. A., Apte, M., & Lodha, S. (2021). Robust collab-
ety, 73(1), 153–180. https://d oi.o rg/1 0.1 080/0 16056 82.2 021. orative fraudulent transaction detection using federated learning.
188029 6 2021 20th IEEE International Conference on Machine Learning
Lebichot, B., Verhelst, T., Le Borgne, Y.-A., He-Guelton, L., Oble, F., and Applications (ICMLA), 373–378. https://d oi.o rg/1 0.1 109/
& Bontempi, G. (2021). Transfer learning strategies for credit ICMLA5 2953.2 021.0 0064
card fraud detection. IEEE Access, 9, 114754–114766. https:// Nickerson, K., Tricco, T., Kolokolova, A., Shoeleh, F., Robertson,
doi.o rg/1 0.1 109/A CCESS.2 021.3 10447 2. C., Hawkin, J., spsampsps Hu, T. (2023). Banksformer: A deep
Lei, Y.-T., Ma, C.-Q., Ren, Y.-S., Chen, X.-Q., Narayan, S., & Huynh, generative model for synthetic transaction sequences. In M.-R.
A. N. Q. (2023). A distributed deep neural network model Amini, S. Canu, A. Fischer, T. Guns, P. Kralj Novak, spsampsps
for credit card fraud detection. Finance Research Letters, 58, G. Tsoumakas (Eds.), Machine Learning and Knowledge Discov-
104547. https://d oi.o rg/1 0.1 016/j.f rl.2 023.1 04547 ery in Databases (pp. 121–136). Springer Nature Switzerland.
Levi, M. (1998). Organising plastic fraud: Enterprise criminals and https://d oi.o rg/1 0.1 007/9 78-3-0 31-2 6422-1_8
the side-stepping of fraud prevention. The Howard Journal of O’Leary, K., O’Reilly, P., Nagle, T., Filelis-Papadopoulos, C., &
Criminal Justice, 37(4), 423–438. https://d oi.o rg/1 0.1 111/1 468- Dehghani, M. (2021). The sustainable value of open banking:
2311.0 0110 Insights from an open data lens. Hawaii International Con-
Lipton, Z. C., Berkowitz, J., & Elkan, C. (2015). A critical review ference on System Sciences. https://d oi.o rg/1 0.2 4251/H ICSS.
of recurrent neural networks for sequence learning (No. arXiv: 2021.7 13.
1506.0 0019). arXiv. https://d oi.o rg/1 0.4 8550/a rXiv.1 506.0 0019 Oliveira, M. I. S., & Lóscio, B. F. (2018). What is a data ecosystem?
Liu, X., Iftikhar, N., Huo, H., Li, R., & Nielsen, P. S. (2019). Two Proceedings of the 19th Annual International Conference on
approaches for synthesizing scalable residential energy consump- Digital Government Research: Governance in the Data Age,
tion data. Future Generation Computer Systems, 95, 586–600. 1–9. https://d oi.o rg/1 0.1 145/3 20928 1.3 20933 5.
https://d oi.o rg/1 0.1 016/j.f uture.2 019.0 1.0 45 Oliveira, M. I. S., & de Barros LimaFariasLóscio, G. F. B. (2019).
Longadge, R., & Dongre, S. (2013). Class imbalance problem in data Investigations into data ecosystems: A systematic mapping study.
mining review (No. arXiv:1 305.1 707). arXiv. https://d oi.o rg/1 0. Knowledge and Information Systems, 61(2), 589–630. https://d oi.
48550/a rXiv.1 305.1 707 org/1 0.1 007/s 10115-0 18-1 323-6
Lopez-Rojas, E. A., & Axelsson, S. (2012). Money laundering detec- Otto, B., Steinbuß, S., Teuscher, A., & Lohmann, S. (2019). IDS refer-
tion using synthetic data. Linköping Electronic Conference ence architecture model 3.0 (p. 118). International Data Spaces

Electronic Markets (2025) 35:7 Page 27 of 28 7
Association. https://i ntern ation aldat aspac es.o rg/w p-c onten t/ Sein, M. K., Henfridsson, O., Purao, S., Rossi, M., & Lindgren, R.
upload s/I DS-R efere nce-A rchit ectur e-M odel-3.0 -2 019.p df. (2011). Action design research. MIS Quarterly, 35(1), 37–56.
Accessed 17 Oct 2024. https://d oi.o rg/1 0.2 307/2 30434 88
Paleyes, A., Urma, R.-G., & Lawrence, N. D. (2023). Challenges in Sethia, A., Patel, R., & Raut, P. (2018). Data augmentation using
deploying machine learning: A survey of case studies. ACM generative models for credit card fraud detection. 2018 4th
Computing Surveys, 55(6), 1–29. https://d oi.o rg/1 0.1 145/3 5333 International Conference on Computing Communication and
78 Automation (ICCCA), 1–6. https:// doi. org/ 10. 1109/ CCAA.
Pathare, A., Mangrulkar, R., Suvarna, K., Parekh, A., Thakur, G., & 2018.8 77762 8
Gawade, A. (2023). Comparison of tabular synthetic data genera- Strelcenia, E., & Prakoonwit, S. (2023). Improving classification
tion techniques using propensity and cluster log metric. Interna- performance in credit card fraud detection by using new data
tional Journal of Information Management Data Insights, 3(2), augmentation. AI, 4(1), 1. https://d oi.o rg/1 0.3 390/a i4010 008
100177. https://d oi.o rg/1 0.1 016/j.j jimei.2 023.1 00177 Sun, C., Shrivastava, A., Singh, S., & Gupta, A. (2017). Revisit-
Patki, N., Wedge, R., & Veeramachaneni, K. (2016). The synthetic data ing unreasonable effectiveness of data in deep learning era.
vault. 2016 IEEE International Conference on Data Science and 843–852. https://o penac cess.t hecvf.c om/c onten t_i ccv_2 017/
Advanced Analytics (DSAA), 2016, 399–410. https://d oi.o rg/1 0. html/S un_R evisi ting_U nreas onabl e_E ffect ivene ss_I CCV_
1109/D SAA.2 016.4 9 2017_p aper.h tml. Accessed 29 Jan 2023.
Pazarbasioglu, C., Mora, A. G., Uttamchandani, M., Natarajan, H., Sun, C., van Soest, J., & Dumontier, M. (2023). Generating synthetic
Feyen, E., & Saal, M. (2020). Digital financial services (p. 54). personal health data using conditional generative adversarial
World Bank Group. https://p ubdoc s.w orldb ank.o rg/e n/2 3028 networks combining with differential privacy. Journal of Bio-
158816 91106 91/D igita l-F inanc ial-S ervic es.p df. Accessed 22 medical Informatics, 143. Scopus. https://d oi.o rg/1 0.1 016/j.
Jan 2023. jbi.2 023.1 04404
Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. Susha, I., Grönlund, Å., & Van Tulder, R. (2019). Data driven social
(2007). A design science research methodology for information partnerships: Exploring an emergent trend in search of research
systems research. Journal of Management Information Systems, challenges and questions. Government Information Quarterly,
24(3), 45–77. https://d oi.o rg/1 0.2 753/M IS074 2-1 22224 0302 36(1), 112–128. https://d oi.o rg/1 0.1 016/j.g iq.2 018.1 1.0 02
Perez, I., Wong, J., Skalski, P., Burrell, S., Mortier, R., McAuley, D., & Tiwana, A., Konsynski, B., & Bush, A. A. (2010). Research com-
Sutton, D. (2023). Locally differentially private embedding mod- mentary—Platform evolution: Coevolution of platform archi-
els in distributed fraud prevention systems. 2023 IEEE Interna- tecture, governance, and environmental dynamics. Information
tional Conference on Data Mining Workshops (ICDMW), 2023, Systems Research, 21(4), 675–687. https:// doi. org/ 10. 1287/
475–484. https://d oi.o rg/1 0.1 109/I CDMW6 0847.2 023.0 0068 isre.1 100.0 323
Pranto, T. H., Hasib, K. T. A. Md., Rahman, T., Haque, A. B., Islam, van Panhuis, W. G., Paul, P., Emerson, C., Grefenstette, J., Wilder,
A. K. M. N., & Rahman, R. M. (2022). Blockchain and machine R., Herbst, A. J., Heymann, D., & Burke, D. S. (2014). A sys-
learning for fraud detection: A privacy-preserving and adaptive tematic review of barriers to data sharing in public health.
incentive based approach. IEEE Access, 10, 87115–87134. IEEE BMC Public Health, 14(1), 1144. https://d oi.o rg/1 0.1 186/
Access. https://d oi.o rg/1 0.1 109/A CCESS.2 022.3 19895 6 1471-2 458-1 4-1 144
Preziuso, M., Koefer, F., & Ehrenhard, M. (2023). Open banking and van Schalkwyk, F., Willmers, M., & McNaughton, M. (2016).
inclusive finance in the European Union: Perspectives from the Viscous open data: The roles of intermediaries in an open
Dutch stakeholder ecosystem. Financial Innovation, 9(1), 111. data ecosystem. Information Technology for Development,
https://d oi.o rg/1 0.1 186/s 40854-0 23-0 0522-1 22(sup1), 68–83. https://d oi.o rg/1 0.1 080/0 26811 02.2 015.
Qiao, F., Li, Z., & Kong, Y. (2024). A privacy-aware and incremen- 108186 8
tal defense method against GAN-based poisoning attack. IEEE Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A frame-
Transactions on Computational Social Systems, 11(2), 1708– work for evaluation in design science research. European Jour-
1721. IEEE Transactions on Computational Social Systems. nal of Information Systems, 25(1), 77–89. https://d oi.o rg/1 0.
https://d oi.o rg/1 0.1 109/T CSS.2 023.3 26324 1 1057/e jis.2 014.3 6
Richhariya, P. (2012). A survey on financial fraud detection methodolo- vom Brocke, J., Simons, A., Niehaves, B., Niehaves, B., & Reimer,
gies. International Journal of Computer Applications, 45. https:// K. (2009). Reconstructing the giant: On the importance of
www.i jcaon line.o rg/a rchiv es/v olume 45/n umber 22/7 080-9 373/. rigour in documenting the literature search process. https://
Accessed 18 Dec 2024. www. seman ticsc holar. org/ paper/ Europ ean- Confe rence- on-
Ryman-Tubb, N. F., Krause, P., & Garn, W. (2018). How artificial intel- Inform ation-S ystem s-( -E CIS-)-S imons-N iehav es/2 fc90c 0163
ligence and machine learning research impacts payment card 905ee8 9bbd7 2a2ba 27acf 3dd01 2526. Accessed 29 Feb 2024.
fraud detection: A survey and industry benchmark. Engineering Walia, M., Tierney, B., & McKeever, S. (2020). Synthesising tabular
Applications of Artificial Intelligence, 76, 130–157. https://d oi. data using wasserstein conditional GANs with gradient penalty.
org/1 0.1 016/j.e ngapp ai.2 018.0 7.0 08 Irish Conference on Artificial Intelligence and Cognitive Sci-
Sattarov, T., Schreyer, M., & Borth, D. (2023). FinDiff: Diffusion mod- ence. https://c eur-w s.o rg/V ol-2 771/A ICS20 20_p aper_5 7.p df.
els for financial tabular data generation. 4th ACM International Accessed 18 Dec 2024.
Conference on AI in Finance, 64–72. https://d oi.o rg/1 0.1 145/ Walls, J. G., Widmeyer, G. R., & El Sawy, O. A. (1992). Building
360423 7.3 62687 6 an information system design theory for vigilant EIS. Informa-
Schäfer, F., Rosen, J., Zimmermann, C., & Wortmann, F. (2023). tion Systems Research, 3(1), 36–59. https:// doi. org/ 10. 1287/
Unleashing the potential of data ecosystems: Establishing isre.3.1 .3 6
digital trust through trust-enhancing technologies. ECIS 2023 Wang, X., & Yang, Y. (2024). A data simulation method of financial
Research Papers. https://a isel.a isnet.o rg/e cis20 23_r p/3 25. fraud transactions based on TransGAN. Proceedings of the 3rd
Accessed 14 Aug 2024. International Conference on Computer, Artificial Intelligence
Scheider, S., Lauf, F., Möller, F., & Otto, B. (2023). A reference and Control Engineering, 242–246. https://d oi.o rg/1 0.1 145/
system architecture with data sovereignty for human-centric 367275 8.3 67279 8
data ecosystems. Business & Information Systems Engineering, Wang, Y., Adams, S., Beling, P., Greenspan, S., Rajagopalan, S.,
65(5), 577–595. https://d oi.o rg/1 0.1 007/s 12599-0 23-0 0816-9 Velez-Rojas, M., Mankovski, S., Boker, S., & Brown, D.

7 Page 28 of 28 Electronic Markets (2025) 35:7
(2018). Privacy preserving distributed deep learning and its Yan, C., Yan, Y., Wan, Z., Zhang, Z., Omberg, L., Guinney, J.,
application in credit card fraud detection. 2018 17th IEEE Mooney, S. D., & Malin, B. A. (2022). A multifaceted bench-
International Conference On Trust, Security And Privacy In marking of synthetic electronic health record generation mod-
Computing And Communications/ 12th IEEE International els. Nature Communications, 13(1). Scopus. https://d oi.o rg/1 0.
Conference On Big Data Science And Engineering (TrustCom/ 1038/s 41467-0 22-3 5295-1
BigDataSE), 1070–1078. https://d oi.o rg/1 0.1 109/T rustC om/ Yoon, J., Jarrett, D., & van der Schaar, M. (2019). Time-series gen-
BigDat aSE.2 018.0 0150 erative adversarial networks. Advances in Neural Information
Webster, J., & Watson, R. T. (2002). Analyzing the past to prepare Processing Systems, 32. https://p rocee dings.n eurip s.c c/p aper/
for the future: Writing a literature review. MIS Quarterly, 2019/h ash/c 9efe5 f26cd 17ba6 216bb e2a7d 26d49 0- A bstra ct.
26(2), xiii–xxiii. html. Accessed 20 Dec 2023.
Weldon, J. C., Ward, T., & Brophy, E. (2021). Generation of syn- Zachariadis, M. (2020). Data-sharing frameworks in financial ser-
thetic electronic health records using a federated GAN. ArXiv. vices: Discussing open banking regulation for Canada (SSRN
https://w ww.s emant icsch olar.o rg/r eader/1 6f0ac aec6e 5d2c Scholarly Paper No. 2983066). https://d oi.o rg/1 0.2 139/s srn.
7421f9 5d816 25f3c 3719ff 81a. Accessed 4 Sept 2023. 298306 6
White, O., Madgavkar, A., Townsend, Z., Manyika, J., Olanre- Zhang, Z., Yan, C., Mesa, D. A., Sun, J., & Malin, B. A. (2019).
waju, T., Sibanda, T., & Kaufman, S. (2021). Financial data Ensuring electronic medical record simulation through better
unbound: The value of open data for individuals and institu- training, modeling, and evaluation. Journal of the American
tions [Discussion paper]. McKinsey Global Institute. https:// Medical Informatics Association : JAMIA, 27(1), 99–108.
www.m ckins ey.c om/i ndust ries/fi nanc ial-s ervic es/o ur-i nsigh ts/ https://d oi.o rg/1 0.1 093/j amia/o cz161
financ ial-d ata-u nboun d-t he-v alue-o f-o pen-d ata-f or-i ndivi du- Zhang, Z. (2022). Synthetic data simulation for privacy-preserv-
als-a nd-i nstit ution s#/. Accessed 24 Feb 2024. ing medical data sharing [Dissertation, Vanderbilt Univer-
Xing, X., Wu, H., Wang, L., Stenson, I., Yong, M., Del Ser, J., sity]. https://w ww.p roque st.c om/o penvi ew/a 52c1b 5ba98 353a
Walsh, S., & Yang, G. (2022). Non-imaging medical data d63fea c8aed c2360 f/1?c asa_t oken=E A2kv2 4XHBc AAAA
synthesis for trustworthy AI: A comprehensive survey (No. A:_5 l8NrI gKBX4 sLCrW kkuay 9QsZX 0MsO3 tYa4h 5DMX
arXiv:2 209.0 9239). arXiv. https://a rxiv.o rg/a bs/2 209.0 9239. mjQu48 RmTio rNOGI iP6TL S9Zn1 MOwcy mfxo& c bl=1 8750
Accessed 13 June 2023. &d iss=y &p q-o rigsi te=g schol ar&p arent Sessi onId=g ry0y
Xu, L., Skoularidou, M., Cuesta-Infante, A., & Veeramachaneni, K. ux5GXH zUSLr 77QPz N7q6%2 FkMyi MM8Un 8M7Ep XKE%
(2019). Modeling tabular data using conditional GAN (No. 3D. Accessed 6 Mar 2024.
arXiv:1 907.0 0503). arXiv. https://d oi.o rg/1 0.4 8550/a rXiv. Zhu, X., Ao, X., Qin, Z., Chang, Y., Liu, Y., He, Q., & Li, J. (2021).
1907.0 0503 Intelligent financial fraud detection practices in post-pandemic
Xu, S., Marwah, M., Arlitt, M., spsampsps Ramakrishnan, N. era. The Innovation, 2(4), 100176. https://d oi.o rg/1 0.1 016/j.x inn.
(2021). STAN: Synthetic network traffic generation with gen- 2021.1 00176
erative neural models. In G. Wang, A. Ciptadi, spsampsps A. Zuiderwijk, A., Janssen, M., & Davis, C. (2014). Innovation with open
Ahmadzadeh (Eds.), Deployable Machine Learning for Secu- data: Essential elements of open data ecosystems. Information
rity Defense (pp. 3–29). Springer International Publishing. Polity, 19(1,2), 17–33. https://d oi.o rg/1 0.3 233/I P-1 40329
https://d oi.o rg/1 0.1 007/9 78-3-0 30-8 7839-9_1
Yale, A., Dash, S., Dutta, R., Guyon, I., Pavao, A., & Bennett, K. P. Publisher's Note Springer Nature remains neutral with regard to
(2020). Generation and evaluation of privacy preserving syn- jurisdictional claims in published maps and institutional affiliations.
thetic health data. Neurocomputing, 416, 244–255. https://d oi.
org/1 0.1 016/j.n eucom.2 019.1 2.1 36