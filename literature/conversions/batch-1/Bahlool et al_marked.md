---
conversion_metadata:
  converted_at: "2026-07-22T12:06:56Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Bahlool et al.pdf"
  source_pdf_sha256: "0382d6d2e4dcc904e67d32760b3e1a2f393cb0418ac65be29a19db6bd12ce574"
  page_count: 36
  markdown_char_count: 293547
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Systematic Review
Performance, Fairness, and Explainability in AI-Based Credit
Scoring: A Systematic Literature Review

Rashed Bahlool *

, Nabil Hewahi

and Wael Elmedany

College of Information Technology, University of Bahrain, Sakhir Campus, Zallaq 1054, Bahrain;
nhewahi@uob.edu.bh (N.H.); welmedany@uob.edu.bh (W.E.)
* Correspondence: 20083051@stu.uob.edu.bh

Abstract

The integration of artificial intelligence (AI) in the financial sector has seen a rapid increase
over the past few years, offering new possibilities to streamline processes while ensuring
profitability for lending institutions. With its data-driven capability, predicting the cred-
itworthiness of applicants has demonstrated strong predictive performance, particularly
for thin-file clients. Despite these advances, growing concerns regarding AI’s fairness,
explainability, and regulatory accountability have increasingly limited its adoption in high-
stakes credit decision-making. This paper presents a synthesis derived from a systematic
literature review (SLR) of 43 peer-reviewed studies published between 2020 and 2025,
focusing on AI-based credit scoring and addressing at least one of the performance, fair-
ness, or explainability dimensions. Eligible studies were limited to peer-reviewed journal
and conference articles (2020–2025) retrieved from IEEE Xplore, Scopus, Web of Science,
and ScienceDirect (last searched: 30 September), examining AI-driven credit scoring in
consumer or lending decision contexts. Guided by the Relevance, Rigor, Reproducibility,
and Quality (3Rs&Q) appraisal framework, the review analyzes how existing approaches
navigate the interplay among performance, fairness, and explainability under regulatory
and human oversight considerations. The findings indicate that these dimensions are
predominantly addressed in isolation, with limited attention to their joint treatment in
regulated deployment settings. By consolidating empirical and conceptual evidence, this
review provides actionable guidance for designing and deploying credit scoring models
in practice.

Keywords: credit scoring; explainable AI; algorithmic fairness; AI governance; regulatory
compliance

Academic Editor: Thanasis Stengos

Received: 12 January 2026

Revised: 26 January 2026

Accepted: 29 January 2026

Published: 3 February 2026

Copyright: © 2026 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license.

1. Introduction

In the continued pursuit of nationwide economic growth, financial institutions provide
consumer facilities as one of their core business functions. Credit scoring plays a pivotal
role in deciding whether a loan should be granted to an applicant, whereby applicants
undergo a rigorous risk assessment process to evaluate their financial stability prior to
approving the facility (Adegoke et al., 2024). The problem of assessing the creditworthiness
of loan applicants is one risk exposure for lending institutions, among other risk sources
that organizations must address. If not properly evaluated, the likelihood of financial
loss increases due to higher loan default rates, ultimately putting financial institutions
at risk (Xie et al., 2025). In contrast, successfully distinguishing between defaulters and

J. Risk Financial Manag. 2026, 19, 104

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 2 -->

J. Risk Financial Manag. 2026, 19, 104

2 of 36

non-defaulters would ensure profitability for the institution. Common credit risk assess-
ments include application and behavioral credit scoring, with other assessments, such as
collection, fraud, and credit renewal, also coexisting (Muñoz-Cancino et al., 2023). These
risk assessments have been extensively relied upon by financial institutions to minimize
potential losses across their product lines. They enable institutions to quantify, monitor,
and mitigate associated risks, depending on the type of situational inputs and regulatory
mandates (Basel Committee on Banking Supervision, 2013; European Central Bank, 2024).
Application and behavioral scoring differ substantially in the timing of the credit-
worthiness assessment. On one hand, application scoring aims to assess the eligibility
of applicants prior to receiving the loan (Berg et al., 2020). To perform the assessment,
customers must undergo a rigorous process known as Know Your Customer (KYC), which
mandates that lending institutions capture personal and repayment records, often retrieved
from national credit bureaus (Mestiri & Hiboun, 2024). The data include demographic
information, loan repayment behavior, and credit bureau data showing outstanding debts
and other credit inquiries, all deemed necessary to ensure a data-driven assessment of cred-
itworthiness. On the other hand, behavioral scoring is an ongoing and periodic evaluation
procedure used to assess the credit behavior of existing customers, thereby monitoring
risk in the active portfolio of an institution (Y. Li et al., 2020). It relies on a subset of the
information used in application scoring, such as payment history and arrears patterns, and
offers early signs of default for proactive interventions. With these two scoring methods in
mind, financial institutions can take preventive measures with applicants who are likely to
default on their loans. Together, both methods enable a full credit life-cycle management
strategy that ensures the approval of eligible customers and the ongoing monitoring of
repayment behavior (Roa et al., 2021).

Beyond institutional risk, the implication of decisions made by credit scoring extends
to cover socioeconomic factors, including financial inclusion and exclusion, wealth distri-
bution, equity, and societal well-being (Bartlett et al., 2022). These consequences weigh
heavily on financial institutions and, if not addressed, result in exclusionary practices that
adversely affect underserved populations. Individuals or entities with access to credit can
contribute to social mobility, while unfair credit scoring can lead to inequalities and limited
opportunities for minority groups. The consequences of lending decisions have long been
the interest of researchers, mainly due to their adverse impact upon fundamental human
rights (Jiang et al., 2024). Regardless of whether the outcomes are intentional or driven by
algorithmic determination, often influenced by human bias in the form of biased historical
data, it is estimated that 1.3 million mortgage loans are rejected in the United States, mainly
due to discrimination (Bartlett et al., 2022). Consequently, minority groups, classified based
on gender, ethnicity, religion, or nationality, are more vulnerable to rejection, or in the
best-case scenario, pay higher interest rates. In the long term, this could lead to unfair
wealth accumulation and therefore perpetuate generational poverty.

The socioeconomic factors involved in credit scoring were key motivations for regula-
tors to step in, ensuring ethical practices and proper oversight of the lending process. As a
result, countries such as the US and the European Union have passed the Equal Credit Op-
portunity Act (ECOA) and the EU Charter of Fundamental Rights, respectively, to prohibit
discriminatory lending acts against personal characteristics (Griffith, 2023). These protec-
tions include race, gender, national origin, and marital status, and, more importantly, they
emphasize that lending institutions must rely solely on financial and application attributes.
These laws have emerged with the intent to foster transparency in the lending process
and reduce mistrust in the financial system that, when undermined, potentially leads to
social and political backlashes. From a risk management perspective, failures in fairness or
explainability translate directly into regulatory, legal, and reputational risks for lending

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 3 -->

J. Risk Financial Manag. 2026, 19, 104

3 of 36

institutions. Considering the long-standing ethical concerns in credit scoring and their com-
plex relation to societal and economic vectors, credit scoring efficiency does not merely seek
to improve lending decision performance, but also accounts for the broader consequences
of socially and ethically inadequate decision-making (Chen et al., 2024; Kumar et al., 2022;
Talaat et al., 2024). Having said that, despite many efforts to combat biased decisions in
algorithmic scoring, there is no consensus on a universal fairness model that is compatible
across all jurisdictional settings, considering also that the definition of fairness varies across
different notions of fairness (Alves et al., 2023; Caton & Haas, 2024; Goethals et al., 2024).
Given that fairness is crucial in credit scoring practices, explainability is central and
enables key stakeholders to interpret and comprehend model outputs, providing them with
a rationale behind particular outcomes (Wang et al., 2020). It allows compliance officers
to question and correct potentially discriminatory decision patterns, inviting intervention
when biased decisions arise, thereby supporting responsible and ethical adoption of AI
(Valdrighi et al., 2025). Explainability also helps ensure alignment with local regulations,
AI ethics and data privacy guidelines by allowing lenders to respond to audits and justify
rejected applications more transparently (Hlongwane et al., 2024). However, as AI mod-
els become more sophisticated and capable of achieving record-breaking precision and
accuracy, their performance often comes at the cost of explainability (Dessain et al., 2023),
resembling a notable tension between model performance and transparency.

Despite all the advancements made across the three dimensions—performance, fair-
ness, and explainability—the current research on the application of AI to solve the credit
scoring problem remains fragmented. Across the reviewed literature, these dimensions are
most often addressed in isolation rather than treated as jointly optimized objectives. The
existing literature often emphasizes one pillar at the expense of others, resulting in models
that are highly predictive but lack transparency, underperforming but inherently inter-
pretable, or fair but operationally inconsistent with regulatory mandates. More importantly,
the interactions among these three pillars, together with regulatory compliance, remain
underexplored, leaving uncertainty around how fairness can be practically implemented
without compromising performance or interpretability. In relation to existing SLRs, this
review extends prior work by explicitly examining the intersections between performance,
fairness, and explainability in AI-based credit scoring, rather than synthesizing these di-
mensions in isolation. This intersection-oriented synthesis yields new insights into how
these pillars interact in practice, where trade-offs are empirically quantified, and which
methodological and regulatory constraints remain under-addressed in deployable credit
decision pipelines.

In light of that, this study has three core objectives: (i) to systematically survey
AI-based credit scoring research published between 2020 and 2025; (ii) to examine how
existing approaches address predictive performance, interpretability, and fairness; and
(iii) to identify methodological and regulatory gaps that influence the practical deployment
of responsible credit scoring models. By consolidating evidence across these dimensions,
this review contributes a governance-oriented synthesis of AI-based credit scoring research
that clarifies existing trade-offs and highlights gaps relevant to regulated deployment.
The remainder of this work is structured as follows. Section 2 outlines the systematic
literature review (SLR) methodology, detailing the search strategy, selection criteria, and
data synthesis process used to ensure a rigorous and scientifically adequate investigation
of the current state of knowledge. Section 3 presents the results of the SLR search that align
with the research objectives and outlines the selection and assessment criteria. Section 4
provides a synthesis of the findings to answer the research questions comprehensively
across all dimensions discussed earlier. Finally, Section 5 concludes by identifying current
research gaps and outlining directions for future work.

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 4 -->

J. Risk Financial Manag. 2026, 19, 104

4 of 36

2. Methodology

To ensure a comprehensive and unbiased survey of key elements reported in the
literature, the SLR protocol was strictly followed to generate the synthesis while main-
taining transparency and reproducibility of the results. The Preferred Reporting Items for
Systematic Reviews and Meta-Analyses (PRISMA) framework (Moher et al., 2010) was
adopted to record the research elements, including the identification, screening, inclusion,
and exclusion of research papers. This systematic literature review was conducted and
reported in accordance with the PRISMA 2020 guidelines (Page et al., 2021). The review
protocol was not registered in PROSPERO or any other public registry.

To comply with the review protocol, the process consisted of several phases, begin-
ning with the formulation of research questions and concluding with the identification
of methodological patterns. Within this systematic process, an explicit search plan was
constructed to locate potentially relevant studies made available in public databases. This
step ensures that the evidence base is comprehensive and not selectively gathered. To
guide and refine the search prior to the in-depth reading, explicit inclusion and exclusion
criteria were defined to determine which studies to include and which to discard. Subse-
quently, for studies that passed the selection criteria, structured extraction was performed
to collect key variables such as methods used for explainability, fairness considerations,
or regulatory aspects. These data were later organized in a predefined schema, allowing
consistent comparison and tagging across different papers. The extracted information was
later synthesized to identify methodological patterns across the literature, from which
future directions are anticipated. Figure 1 illustrates the phases involved in formulating
the study’s key findings. The review process followed six sequential phases, beginning
with defining research questions and developing search strategies, followed by establishing
inclusion and exclusion criteria. Data were then systematically extracted, organized, and
synthesized to identify methodological patterns.

Figure 1. Phases of the systematic literature review process.

2.1. Research Questions (RQs) Formulation

To strengthen the goal of this study while ensuring a cohesive and structured approach
guiding the formulation of the search strategy across the three main pillars—performance,
explainability, and fairness—a Population, Intervention, Comparison, Outcome, and Con-
text (PICOC) framework (Keele, 2007) was adopted to translate the broader topic of em-
ploying AI in credit scoring into an operationally precise scope at the planning stage prior
to screening. By articulating the Population, Intervention, Comparison, Outcome, and
Context, the framework guides the search string construction, reduces bias by making
relevance criteria traceable to a predefined scope, and increases reproducibility by for-
mulating auditable selection choices. Using the PICOC framework, this work aims to

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 5 -->

J. Risk Financial Manag. 2026, 19, 104

5 of 36

explore the relationships and interactions among the three pillars, quantify their trade-offs,
and acknowledge that more than one pillar can operate jointly and influence another in a
quantifiable manner.

Table 1 explains the PICOC components and their relationship to the domain and
subject of this research, guiding RQ formulation and the search strategy developed to
align the findings with the overall objectives. The PICOC framework defines the domain
and subject of deployed AI models highlighted in past studies by referring to credit
scoring predictions based on evaluating default risks using historical financial information
exclusive to application risk assessments. This reflects the techniques or methods employed
to address single or joint challenges in credit scoring, including performance, fairness, and
explainability, corresponding to the deployment of AI to solve the credit scoring prediction
problem and incorporating multiple pillars. It specifies what the intervention is evaluated
against by requiring studies to make use of existing baselines to benchmark their methods
or highlight the trade-offs across the pillars, analyzing pillar interactions. It also captures
the measured and reported performance indicators, fairness metrics, explainability with
human comprehension, and quantitative assessment of trade-off analysis between pillars.
Finally, it defines the application environment and publication constraints by determining
whether the study is exclusive to the credit scoring domain, published in a peer-reviewed
venue, or demonstrates recency in reporting fairness and explainability integrated into
modeling, and it identifies where trade-offs or research gaps emerge among the three pillars.

Table 1. PICOC framework used for research question formulation.

Component Definition

Population

Defines the domain and subject of deployed AI models highlighted in past
studies. It refers to credit scoring predictions that are based on evaluating
default risks using historical financial information that is exclusive to
application risk assessments.

Intervention

Refers to the technique or method employed to tackle single or joint
problems given in credit scoring, including performance, fairness and
explainability. It corresponds to the deployment of AI to solve the credit
scoring prediction problem and can incorporate multiple pillars.

Comparison

Specifies what the intervention is evaluated against. In this context, studies
must make use of existing baselines to benchmark their methods or
highlight the trade-offs across the pillars. This element is crucial, as it
analyzes pillar interactions.

Outcome

Captures what was measured and reported, illustrating the outcomes of
interest, such as performance indicators, fairness metrics, explainability
with human comprehension, and quantitative assessment of the trade-off
analysis between pillars.

Context

Defines the application environment and publication constraints. It
determines whether the study is exclusive to the credit scoring domain,
published in a peer-reviewed journal or conference, or demonstrates
recency in terms of reporting fairness and explainability integrated into
modeling. In addition, it pinpoints where trade-offs arise or other gaps
exist, given the three pillars.

Drawing on the PICOC framework, the following research questions have been for-
mulated to define the context and objectives of this research. Collectively, three research
questions were aligned with the study’s overarching aim to explore how credit scoring
frameworks can balance predictive performance with fairness, explainability, and regula-
tory accountability through human-in-the-loop considerations. More specifically, RQ1 ex-

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 6 -->

J. Risk Financial Manag. 2026, 19, 104

6 of 36

amines the trade-offs between performance, interpretability, and fairness, RQ2 investigates
the current bias mitigation strategies focusing on their effectiveness, and RQ3 addresses
the role of regulation and human oversight in ensuring ethically aligned AI systems.

•

•

•

RQ1: To what extent can credit scoring frameworks achieve compelling performance
while balancing explainability and fairness trade-offs? The extent to which AI mod-
els operate opaquely in determining creditworthiness not only hinders their adoption
but also poses threats to their fairness and trustworthiness (Ribeiro-Flucht et al., 2024).
In response, numerous efforts within the credit scoring landscape have prioritized
transparency and explainability to develop complementary or embedded methods
that clarify the rationale and reasoning behind AI-generated outcomes. Model ex-
plainability and interpretability are foundational in the deployment of AI and are
considered no less important than the performance itself. Apart from describing the
motive, both can fundamentally serve the ability to explain causes leading to biased or
uncertain decisions (Alufaisan et al., 2021). High-stakes applications depend critically
on the ability to reason about and justify model decisions, whereby the lack of trans-
parent decision-making poses a significant drawback and may result in mistrust and
non-compliance with local regulations (Wang et al., 2020). Considering the criticality
of the three pillars, this research question examines the extent to which these pillars
can be elevated jointly or if there are potential trade-offs.
RQ2: How do historical repayment data, class imbalance, and protected attributes
contribute to biased predictions, and what mitigation strategies are most effective?
A common issue across datasets used to train AI models is class imbalance, which
hinders AI models from producing accurate results (Chen et al., 2024). This problem
is pervasive across credit scoring datasets where the number of defaulters is signifi-
cantly less than that of non-defaulters. Such an imbalance adversely affects accuracy,
suggesting the need for more adaptive techniques that treat all classes equitably. In
addition, the presence of protected attributes across different credit scoring datasets
potentially amplifies the historical discrimination against minority groups, leaving
structural traces in training data (Hurlin et al., 2024; Talaat et al., 2024). For instance,
certain ethnic groups have historically been granted credit less frequently, thereby
appearing more frequently in the “bad” class, not due to actual risk but because
they were denied favorable products or guidance. Addressing this research question
reveals the relationships among class imbalance, as well as their potential effect on
protected attributes, and provides means to understand the mitigation strategies that
eliminate biased decisions.
RQ3: How do regulatory frameworks and human-in-the-loop (HITL) approaches
influence the interpretation of fairness across different contexts, and how can
they be incorporated into ethically aligned AI models? Given that AI models are
prone to biased decisions and lack transparency in how their results are determined,
the intervention of regulatory bodies underscores the importance of consciously
adopting AI in domains involving monetary decisions and fundamental human rights.
While precision and accuracy were the ultimate goals sought in the past, the loss of
transparency has proven far more costly in critical and regulated domains, making
explainability a necessity rather than an option (Chen et al., 2024). Ensuring this
balance enables the responsible and accountable deployment of AI in credit scoring
domains, supported by adequate human oversight to maintain compliance with
local regulations, and ensures that results remain comprehensible to human decision-
makers (Peng et al., 2023).

Guided by these research questions, this work aims to explore the potential trade-offs
and possibilities to incorporate multiple dimensions to form an intersectional framework

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 7 -->

J. Risk Financial Manag. 2026, 19, 104

7 of 36

built around the triad of performance, explainability, and fairness, with Regulation and
HITL. Figure 2 illustrates the conceptual framework showing the intersections among
performance, explainability, and fairness in AI-driven credit scoring. The outer layers rep-
resent regulatory oversight and human intervention as contextual dimensions influencing
all three pillars. Each overlap corresponds to the research questions (RQ1–RQ3) guiding
this systematic literature review.

Figure 2. Conceptual framework of performance, fairness, and explainability in AI credit scoring.

2.2. Search Strategy

To ensure the retrieval of the relevant literature and refine the scope, the search string
was carefully crafted to emphasize the intersection between the three pillars highlighted
earlier. More importantly, it also highlights recent advancements related to balancing or
interaction across these distinct dimensions. Therefore, the study was conducted using
the IEEE, Scopus, Web of Science, and Science Direct databases to ensure comprehensive
and sufficient coverage of peer-reviewed journal articles and conference proceedings. In
addition, Scopus included records from major indexing services such as ScienceDirect,
SpringerLink, Wiley Online, Taylor & Francis Online, IEEEXplore, and ACM Digital Library.
This ensured broad interdisciplinary coverage of relevant sources and that the search was
conducted across multiple major databases to reduce the likelihood of database-specific
omission and bias in the retrieval process. Table 2 presents the search string used for
literature retrieval.

Table 2. Boolean search string used to retrieve publications between 2020 and 2025.

TITLE-ABS-KEY (“credit scoring” OR “credit risk”)
AND TITLE-ABS-KEY (“machine learning” OR “deep learning” OR “artificial intelligence” OR
“reinforcement learning” OR “deep reinforcement learning”)
AND TITLE-ABS-KEY (“explainable AI” OR “interpretability” OR “model transparency” OR “XAI”
OR “fairness” OR “bias” OR “discrimination” OR “protected attribute*”)
AND PUBYEAR ≥ 2020 AND PUBYEAR ≤ 2025

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 8 -->

J. Risk Financial Manag. 2026, 19, 104

8 of 36

The search string was designed to locate relevant papers by matching the specified
keywords across the titles, abstracts, and keywords sections; therefore, the field code (TITLE-
ABS-KEY) was used. In addition, key terms and synonyms were selected to represent the
core dimensions of this study, i.e., explainability, fairness and performance. Optionally,
papers were required to address at least one secondary dimension related to fairness or
explainability, rather than focusing solely on performance. This process initially retrieved a
total of 436 papers prior to the selection and screening stages.

2.3. Selection Criteria

To govern the selection of records, a set of selection criteria was established to cover
both inclusion and exclusion principles. This includes screening at the title or abstract level
and full-text exclusion. It ensures that the selection is structured and reproducible, that
the pool of studies aligns well with the research questions, and that biased selection is
prevented. Due to the large volume of records, only a representative subset of papers was
considered, guided by the PICOC components specified earlier.

2.3.1. Inclusion Criteria

Only studies that were published from 2020 onward in reputable, peer-reviewed
venues, such as ACM, IEEE, Springer, and Elsevier, were considered in this work. This tem-
poral scope was intentionally selected to capture the most recent phase of AI-based credit
scoring research shaped by the rapid adoption of explainable AI (XAI) and fairness-aware
learning, alongside increasing regulatory scrutiny of automated decision-making in high-
stakes domains. The period from 2020 onward reflects the growing maturity of explanation
techniques, counterfactual recourse, and fairness constraints integrated into modern learn-
ing objectives, as well as the increasing emphasis on transparency, non-discrimination, and
auditability in credit decision pipelines, aligned with emerging AI governance and account-
ability requirements. More importantly, restricting the scope to recent studies increases the
likelihood of capturing methods and evidence that jointly address multiple pillars within
the same experimental setting, which is essential for intersection-oriented assessment.

The eligibility of papers was later assessed based on their coverage of at least one
additional dimension beyond the performance of credit scoring models, namely explain-
ability and fairness, as highlighted earlier. In addition, the context and domain of the
research must be exclusive to credit scoring or credit risk assessment, and the studies must
demonstrate measurable or interpretable outcomes or, at a minimum, conceptually support
integrating fairness and explainability into credit scoring frameworks to establish clear
links for ethical framework assessment.

2.3.2. Exclusion Criteria

Studies not meeting the inclusion criteria were excluded or deemed insufficient to
explicitly integrate the different dimensions of this study. This included studies falling
outside the credit scoring domain or addressing irrelevant AI applications such as NLP,
fraud detection, or insurance risk. Further, non-peer-reviewed materials, pre-2020 pub-
lications, and overly generic works were also omitted. Additional exclusions applied to
papers focusing only on performance or feature selection without fairness or explainabil-
ity, or those addressing corporate lending, profit or loss prediction, or transfer learning
based on external datasets. Purely conceptual or regulatory discussions were excluded
unless directly relevant to fairness and explainability under RQ3. Lastly, studies addressing
credit scoring for corporate loans and Small and Medium Enterprises (SMEs) were also
omitted from this study, as they do not relate to data privacy and the inclusion of sensitive
(protected) attributes.

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 9 -->

J. Risk Financial Manag. 2026, 19, 104

9 of 36

2.4. Screening Process

Following the inclusion and exclusion criteria specified in the earlier subsection, the
PRISMA 2020 guidelines (Page et al., 2021) were followed, ensuring records identified
through database searches were screened by title, abstract, and full text to ensure their
alignment with the RQs. Figure 3 provides a summary of the systematic flow of study
identification, screening, eligibility assessment, and inclusion.

Figure 3. PRISMA 2020 flow diagram for the systematic identification and screening of studies.

The initial search result returned 436 records from electronic databases, with no addi-
tional records from registers being considered. During the identification phase, 132 records
were excluded due to duplication (i.e., identical papers retrieved from multiple databases),
irrelevance, methodological overlap, or discrepant metadata. The remaining 304 records
were subjected to title and abstract screening, during which 227 records were excluded for
failing to meet the inclusion criteria specified. This included, for instance, applications of
AI in corporate credit scoring, unrelated domains, or non–peer-reviewed materials.

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 10 -->

J. Risk Financial Manag. 2026, 19, 104

10 of 36

In the eligibility assessment stage, 77 reports were sought for full-text retrieval, of
which 19 could not be accessed due to unavailability or subscription-based restrictions.
The remaining 58 reports underwent full-text assessment against the quality assessment,
based on which 10 reports were excluded due to low-quality appraisal scores, and 5 were
excluded due to overlapping scope or outdated survey content, as detailed in Appendix A.
Finally, 43 studies were included in this review, forming the final corpus analyzed across
the dimensions of performance, explainability, and fairness.

All records retrieved from the selected databases were screened by one reviewer using
the predefined inclusion and exclusion criteria. The screening was performed in two stages,
i.e., title/abstract screening followed by full-text assessment. Any uncertainties during
screening were resolved through repeated manual verification against the eligibility criteria.

2.5. Data Extraction

To systematically record the bibliographic information, methodological details, and
thematic attributions of the 43 included studies, a structured data sheet was created, and the
data extraction was performed by one reviewer to ensure consistency and reproducibility.
Metadata extracted from the search databases were imported into Zotero as the primary
reference management tool, then exported to Excel for coding and synthesis. Bibliographic
details such as title, abstract, authors, DOIs, publication year, and venue formed the
evidence base for subsequent analysis.

For thematic classification, each study was tagged to reflect its dominant themes across
performance, explainability, and fairness, as well as connections to regulatory and HITL
concepts. These tags were instrumental in identifying intersections among the dimensions,
supporting the conceptual framework described in Figure 2. To minimize transcription
errors, the extracted entries were cross-checked against the original articles before synthesis.
No automation tools were used for extraction, and the study’s authors were not contacted
for additional information.

2.6. Quality Assessment

Since the included studies are methodologically diverse and target at least one pillar,
and since the synthesis of this work is narrative rather than effect-size based, this review
did not employ a domain-specific risk-of-bias tool. Instead, to ensure the inclusion of
methodologically and conceptually aligned studies, a structured multi-criteria appraisal
(Keele, 2007) was conducted by leveraging evidence weighting practices to assess the
relevance and rigor of each study. To support this, a customized 3Rs&Q framework
was designed to assess the contribution of each work toward the interaction among the
three main pillars while also accounting for contextual dimensions such as regulation
and human intervention. The scoring scale ranged from 0 to 3, whereby values of 0 and
3 indicate the lowest and highest scores, respectively. Considering each 3Rs&Q metric
consists of two sub-metrics (R1–R6 and Q1–Q2), the total attainable score was 24, as shown
in Table 3. The tier thresholds (high: 17–24; medium: 9–16; low: <9) were determined a
priori based on equal distribution across the 24-point scale and reflect increasing levels of
methodological alignment with the three pillars. This distribution-based approach also
ensures that papers scoring 8 or below fall naturally within the lower-quality tier of the
3Rs&Q scale. Papers demonstrating strong methodological and conceptual rigor were
scored between 17 and 24, forming the high-quality tier. In addition, papers that provided
partial coverage of isolated dimensions, such as focusing only on fairness, but still offered
useful insights, received scores ranging from 9 to 16 and belonged to the medium-quality
tier. Lastly, the remainder of the studies that scored below 9 points were not considered
due to limited connection to the review’s core dimensions.

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 11 -->

J. Risk Financial Manag. 2026, 19, 104

11 of 36

This customized 3Rs&Q appraisal framework was applied as a structured rubric to
support consistent quality appraisal across included studies. Since rubric-based scoring
may introduce assessor subjectivity, scores were assigned using evidence-driven rules
that relied only on explicitly reported information within each paper rather than inferred
intentions. Borderline cases were re-checked against the original text and scored conserva-
tively when evidence was insufficient, ensuring that the appraisal reflects documented and
relevant contributions to the review’s core dimensions.

Table 3. The 3Rs&Q quality assessment framework for evaluating study inclusion.

Dimension Submetric

Description

Scoring Criteria (0–3)

Does the study explicitly
address at least one of the
six conceptual pillars
(Explainable AI, Fairness,
Imbalance, Protected
Attributes, Regulation,
Human Intervention)?

Does the paper contribute
evidence toward one or
more of the three research
questions (RQs)?

Are the models or methods
clearly described,
validated, and
reproducible?

Does the study use
real-world datasets,
multiple metrics (e.g., AUC,
fairness measures), or
comparative baselines?

Does the study consider
regulatory compliance (e.g.,
ECOA, GDPR) or
cross-national fairness
transferability?

Does it combine multiple
pillars (e.g., fairness +
explainability or imbalance
+ regulation)?

Are code, data, or
supplementary
reproducibility resources
available?

Does the study provide
actionable insights for
deployment (e.g., industry
adoption, human oversight,
legal compliance)?

none, peripheral, central
and focus

none, weak, moderate and
strong

poor, basic, robust, and
state of the art

minimal, partial, strong
and comprehensive

none, partial, clear attempt,
and deep analysis

siloed, minor combination,
partial integration and
holistic framework

not available, vague, partial
and open and reproducible

theoretical, limited,
moderate and strong

Relevance

Pillar Alignment (R1)

Relevance RQ Fit (R2)

Rigor

Methodological Soundness
(R3)

Rigor

Evaluation Depth (R4)

Reach

Cross-Context Awareness
(R5)

Reach

Integration of Dimensions
(R6)

Quality

Transparency (Q1) and
Reproducibility

Quality

Practical Relevance (Q2)

3. Results
3.1. Study Selection

Following the quality assessment, a total of 58 papers were thoroughly assessed and
scored. Among these, 15 papers forming 25.8% of the selected studies were excluded due to
low scores (≤8), failure to meet the eligibility criteria and overlapping scopes. Consequently,

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 12 -->

J. Risk Financial Manag. 2026, 19, 104

12 of 36

they were deemed unsuitable to address the objectives of this work. A detailed summary
of the 43 studies considered in the analysis and results is provided in Appendix B.

3.2. Characteristics of Selected Studies

Considering the multidisciplinary nature of the credit scoring problem, studies in-
cluded in this review were published across various venues, with 95.4% and 4.6% published
as journal articles and conference papers, respectively. Among indexed sources, 13.95%
of studies were retrieved from IEEE Xplore, followed by SpringerLink, with over 11.63%.
Both venues represented a substantial portion of technical and computational research in
the selected sample. Additionally, smaller but notable portions of the selected studies were
obtained from Elsevier’s ScienceDirect and open-access publications, such as PLOS ONE,
both equally forming 6.98%. Other publications from ACM Digital Library and MDPI
accounted for 2.33% of the final set.

Table 4 shows the distribution of studies categorized by published family. Given that
credit scoring intersects finance, statistics, artificial intelligence, and regulatory studies,
more than half of the selected sample (55.81%) was elicited from domain-specific journals
or conference venues that do not belong to a particular digital library. Furthermore, most
of the studies included herein were published between 2023 and 2024, forming 30.2% and
48.8% for the same years, respectively. The remaining studies—published between 2020
and 2022—formed only 21%, thereby confirming the recency of the intersection across
dimensions considered in this study.

Table 4. Distribution of studies by publisher family.

Database/Publisher Family

Count

IEEE Xplore
SpringerLink
Elsevier (ScienceDirect)
Open Access (Public)
ACM Digital Library
MDPI
Other/Misc.

3.3. Topic Coverage

6
5
3
3
1
1
24

%

13.95%
11.63%
6.98%
6.98%
2.33%
2.33%
55.81%

The trends observed in the coverage across dimensions, as shown in Figure 4, reveal a
clear shift in the research agenda of credit scoring from 2023 onward, with a lower count
for 2025 since the year was still in progress at the time of data collection. Prior to this,
a small number of studies covered any of the investigated dimensions and were mostly
fragmented. While the concept of fairness was simply being applied in AI disciplines,
human intervention and regulatory aspects were almost absent. This suggests that studies
prior to 2023 were primarily focused on performance and, to a certain extent, on mitigating
bias associated with protected attributes.

However, in 2023, there is an evident surge across all investigated dimensions. It
is worth noting that studies increasingly incorporate protected attributes and examine
their effects on fairness and explainability, underscoring their growing importance in more
recent studies. This suggests a turning point where the field began to operationalize an
ethical and transparent model design rather than being merely performance-focused. This
shift aligns well with the policy pressure imposed by regulators, which likely stimulated
regulatory responses to address ethical and social accountability concerns in the literature.
Among all considered dimensions, explainability showed the strongest expansion
between 2023 and 2024, marking it as the dominant and most substantial pillar of recent

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 13 -->

J. Risk Financial Manag. 2026, 19, 104

13 of 36

credit scoring research. On the other hand, studies concerning protected attributes and
their regulation in algorithmic decision-making also increased significantly after 2022,
signaling a significant surge in compliance with governance and legal frameworks. Human
intervention, however, remains comparatively under-represented, despite its significance
in high-stakes settings, particularly when the trade-off between performance and fairness
is presumed. Overall, this trend represents a major transition from performance-focused
representation of the credit scoring problem toward bias and interpretability-aware credit
scoring, with regulation and human intervention being central to responsible deployment.

Figure 4. Topic coverage by year.

Furthermore, to quantify the intersections between different dimensions, Table 5
presents the pairwise intersections between all considered dimensions grouped by base
dimension. Notably, fairness and protected attributes represented the largest portion
of studies that accounted for measuring fairness across sensitive/private features, with
21 papers discussing this association. This confirms that fairness discourse is primarily
anchored in group fairness definitions. Moreover, the association between fairness and
other dimensions, including regulation and human intervention, was ranked second from
the point of view of fairness, having 11 papers relating it to human comprehension and
regulatory frameworks. This pattern suggests that when fairness and protected attributes
are foregrounded, regulatory requirements involving human oversight are simultane-
ously considered.

Despite that, mid-tier intersections between explainability and other pillars, including
fairness, the presence of protected attributes, regulation and human oversight were found in
seven or fewer papers, highlighting this association. This suggests that while explainability
is increasingly present in bias-aware frameworks, it remains an auxiliary function and not
yet central. In other words, explainability in credit scoring tends to serve as a bias-diagnostic
rather than a compliance- or fairness-enforcing mechanism.

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 14 -->

J. Risk Financial Manag. 2026, 19, 104

Table 5. Pairwise intersections grouped by base dimension.

Dimension

Intersect

Imbalance
Fairness
Protected Attributes
Regulation
Human Intervention

Protected Attributes
Regulation
Human Intervention
Imbalance

Regulation
Human Intervention
Imbalance

Human Intervention

Explainability

Fairness

Protected Attributes

Regulation

4. Discussion

14 of 36

Count

10
7
6
6
6

21
11
11
6

11
11
4

10

This section examines the trade-offs and assesses compatibility across performance,
fairness, and explainability as three crucial elements in the ethical and responsible deploy-
ment of AI within the credit scoring domain. To achieve that, the interactions among these
pillars are synthesized to determine their compatibility and describe observed patterns.
In addition, this section highlights common bias mitigation strategies and compares their
effectiveness in the deployment pipeline, and it conceptually relates model interpretation
to human comprehension to support ethically aligned deployment. Where applicable,
the discussion is supported by empirical and conceptual evidence reported in the re-
viewed literature.

4.1. Compatibilities and Trade-Offs (RQ1)

Performance vs. Explainability
Considering the wide adoption of AI models, ranging from inherently interpretable
to black-box models, there is no consensus from the literature confirming the availability
of universally compliant models. Although the terms interpretability and explainability
are used interchangeably in this work, both denote the conscious adoption of AI aimed
at establishing the grounds for understanding model outcomes (Ratul et al., 2021). Over
the years, models have been primarily performance-focused, achieving high predictive
accuracy but often failing to explain their results due to their complexity. A clear example is
the transition from traditional models, such as logistic regression (LR) and shallow decision
trees (DTs), to more sophisticated boosting and deep learning (DL) architectures. Arguably,
despite both approaches being extensively explored and sharing similarities, deep learning
demonstrates greater suitability in addressing modern and complex credit scoring contexts.
However, this advancement comes at the cost of interpretability, which poses chal-
lenges in highly regulated, high-stakes domains (Bücker et al., 2022). Understanding the
model’s reasons for identifying defaulters is foundational in the financial sector, particu-
larly in credit risk domains (Valdrighi et al., 2025), considering that this opacity poses a
limitation for credit assessors in validating and trusting their results. By contrast, tradi-
tional and shallow tree-based models are generally more interpretable and can provide
insights into how eligibility is determined (Kanaparthi, 2023). For instance, the coefficients
optimized in LR reflect the magnitude of feature influence on the output, while DTs offer
a transparent tree-like structure showing the collective decision paths leading to the final
outcome. Conversely, DL methods rely heavily on post-hoc explainability techniques to

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 15 -->

J. Risk Financial Manag. 2026, 19, 104

15 of 36

compensate for their opacity, which often raises compliance concerns in regulated sectors
(Hjelkrem & Lange, 2023).

Consequently, there has been a noticeable expansion in the adoption of post-hoc meth-
ods, particularly SHAP and LIME (Aruleba & Sun, 2024; S. Han et al., 2024; Hjelkrem &
Lange, 2023; Hlongwane et al., 2024; Nwafor et al., 2024; Zhang et al., 2025), which can
operate independently of model design. For example, Nwafor et al. (2024) proposed a hy-
brid approach combining a single-dimensional CNN and XGBoost to formulate a stacking
architecture for credit scoring while ensuring explainability. Their results demonstrated
greater performance of the hybrid model when compared with native models, such as
CNN, XGBoost, and LR, attaining an accuracy of 96%, exceeding that of the interpretable
LR model by 4%. A similar example was observed in the work of Hlongwane et al. (2024).
They argued that while tree-based models such as XGBoost and RF provide promising
performance results, they lack sufficient interpretability to explain them. By integrating
SHAP into their deployment pipeline, they successfully visualized feature attributions
toward prediction outcomes. However, when the AUC measures were compared against
LR, both RF and XGBoost outperformed LR by only 1%.

These examples provide concrete evidence that the trade-off between explainability
and performance is largely assumed rather than empirically measured. This observation is
in line with the one highlighted by Dessain et al. (2023), where they explicitly stated that the
trade-off between performance and explainability stems from the move toward complex
black-box models lacking intrinsic interpretability. In their experiment, they quantified this
trade-off across 12 models, including inherently explainable and black-box models. From
a business standpoint, they concluded that the performance gap between interpretable
and black-box models corresponds to only 0.14–0.21% in annual return on investment.
Despite that, they applied isotonic smoothing to GAMs in order to increase interpretability
without further financial loss, achieving performance close to that of black-box models.
Therefore, the choice between inherently interpretable and black-box models is primarily
determined by an institution’s risk tolerance. It is also worth noting that studies measuring
this trade-off were relatively limited, underscoring the need for empirical measurement if
inherently interpretable models are to be considered.

Overall, the literature indicates that explainability is predominantly introduced as a
post-hoc addition to black-box models rather than being embedded or enhanced within
inherently interpretable ones. The presumed trade-off between performance and explain-
ability is thus often asserted rather than demonstrated, with a limited number of studies
quantifying this cost and observing it to be marginal. In general, it is observed that the
current practice in credit scoring favors preserving predictive strength while mitigating
opacity through auxiliary explainability methods rather than prioritizing interpretability
from the outset.

Despite recurring claims that model transparency degrades predictive strength, empir-
ical evidence shows that the performance gaps between transparent and black-box models
are consistently marginal, as illustrated in Table 6, with limited studies demonstrating a
substantial performance degradation when using interpretable baselines. It is also worth
noting that the comparison results should be perceived under a fair setting, where pre-
processing and feature preparation steps are applied consistently across both interpretable
and black-box models, ensuring that observed differences reflect model capacity rather
than unequal data treatment. In some cases, the gain from complex models was even
negligible, denoting that the perceived trade-off is largely assumed but rarely quantified.
As a result, model explainability tends to be incorporated after model selection rather than
shaping it, implying that the performance and explainability conflict is less structural than

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 16 -->

J. Risk Financial Manag. 2026, 19, 104

16 of 36

commonly portrayed, particularly in regulated credit scoring contexts where even marginal
gains rarely justify opacity.

Table 6. Comparison of interpretable vs. black-box model performance in included studies.

Paper

Dataset

Models Compared

Metric

Interp. Black-Box

Nwafor et al. (2024)

LendingClub

LR vs. XGB

AUC
H-score
Precision (w)
Recall (w)
F1-score (w)

0.95
0.95
0.93
0.92
0.92

0.99
0.95
0.95
0.94
0.94

∆

+0.04
0.00
+0.02
+0.02
+0.02

S. Han et al. (2024)

HE & GMSC (best-case)

LR vs. RF/GB

Chai et al. (2025)

Farmers (best-case)

DT vs. LCE

AUC

AUC

0.9750

0.9891

+0.0141

0.622

0.784

+0.162

Hlongwane et al. (2024)

Taiwan
Home Credit

LR vs. RF (best-case)
AUC
LR vs. XGB (best-case) AUC

0.74891
0.69644

0.75929
0.69766

+0.01038
+0.00122

Zhang et al. (2025)

PCL

DT vs. IAIBS

FICO

CCF

VL

Ali Shahee and Patel (2025) Proprietary

L. H. Li et al. (2025)

LendingClub (2007–2020)

LR vs. IAIBS

DT vs. IAIBS
LR vs. IAIBS

LR vs. IAIBS

DT vs. ANN
(ADASYN+FL)

LR vs. LightGBM
LR vs. CatBoost
LR vs. RF
LR vs. MLP
SVM vs. LightGBM
SVM vs. CatBoost
SVM vs. RF
SVM vs. MLP
NB vs. LightGBM
NB vs. CatBoost
NB vs. RF
NB vs. MLP
LR vs. LightGBM
LR vs. CatBoost
LR vs. RF
LR vs. MLP
SVM vs. LightGBM
SVM vs. CatBoost
SVM vs. RF
SVM vs. MLP
NB vs. LightGBM
NB vs. CatBoost
NB vs. RF
NB vs. MLP

AUC
Accuracy
F1

AUC
Accuracy
F1

AUC
Accuracy
F1

AUC
Accuracy
F1

Accuracy
F1-score
AUC
G-mean

AUC
AUC
AUC
AUC
AUC
AUC
AUC
AUC
AUC
AUC
AUC
AUC
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy

86.81
76.95
56.79

77.48
71.52
73.93

96.04
97.45
86.71

61.91
59.32
60.18

0.720
0.644
0.737
0.602

0.91
0.91
0.91
0.91
0.88
0.88
0.88
0.88
0.89
0.89
0.89
0.89
0.83
0.83
0.83
0.83
0.83
0.83
0.83
0.83
0.81
0.81
0.81
0.81

89.17
79.32
59.39

79.86
74.55
76.51

97.48
97.56
88.69

66.03
62.70
63.31

0.783
0.747
0.812
0.747

0.94
0.94
0.93
0.91
0.94
0.94
0.93
0.91
0.94
0.94
0.93
0.91
0.87
0.86
0.86
0.84
0.87
0.86
0.86
0.84
0.87
0.86
0.86
0.84

+2.36
+2.37
+2.60

+2.38
+3.03
+2.58

+1.44
+0.11
+1.98

+4.12
+3.38
+3.13

+0.063
+0.103
+0.075
+0.145

+0.03
+0.03
+0.02
+0.00
+0.06
+0.06
+0.05
+0.03
+0.05
+0.05
+0.04
+0.02
+0.04
+0.03
+0.03
+0.01
+0.04
+0.03
+0.03
+0.01
+0.06
+0.05
+0.05
+0.03

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 17 -->

J. Risk Financial Manag. 2026, 19, 104

17 of 36

To interpret the performance gap between inherently interpretable and black-box
models, the marginal differences reported in Table 6 should be viewed as dataset- and
method-dependent rather than consistent across all settings. While most comparisons
indicate only minor performance variations, some studies report larger gains when the
modelling approach introduces additional capacity to capture higher-order interactions
and non-linear decision patterns. Consequently, the observed differences are conditional
not only on the characteristics of the underlying datasets but also on the experimental
and pre-processing choices adopted in each study. A key driver of reduced performance
gaps is the extent of data refinement and feature reduction that simplifies the learning
problem. This is demonstrated by Nwafor et al. (2024), where the LendingClub dataset
was reduced from over 1 million observations and 145 features to 25,535 observations
with 25 features through exploratory analysis and feature filtering. This dimensionality
reduction likely decreased redundancy and noise, enabling interpretable baselines such
as logistic regression to remain competitive and limiting the incremental gain achieved
by XGBoost.

A similar trend is observed in the work of L. H. Li et al. (2025), where extensive
pre-processing, feature filtering, and normalization applied to the LendingClub dataset
resulted in performance improvements that remain broadly comparable across interpretable
and black-box models. Evidence of an even smaller trade-off is provided by Hlongwane
et al. (2024), where discretization, feature engineering, and variable selection were used
to constrain final scorecard complexity in the Taiwan and Home Credit datasets. Under
this controlled setup, performance differences between logistic regression and tree-based
models became near-negligible, particularly in Home Credit, where XGBoost yielded only
a minimal AUC improvement over logistic regression. Collectively, these findings suggest
that when input dimensionality is reduced, noise is controlled, and pre-processing steps
are applied uniformly across model families, the advantage of black-box models often
becomes marginal.

In contrast, pipelines that do not consider observation and complexity reduction
techniques can yield larger gains, particularly when explicitly targeting complex regions of
the feature space that interpretable models struggle to capture. Zhang et al. (2025) exemplify
this by proposing a boundary-focused hybrid framework that retains logistic regression as
a transparent baseline while introducing a deep learning component trained on boundary
samples. Rather than simplifying the feature space through reduction techniques, the
study applies pre-processing primarily for imbalance mitigation, enabling models to learn
more effectively from complex decision boundaries. This design increases model capacity
specifically in regions where linear decision functions underperform, helping to explain the
comparatively larger improvements reported in their experiments. In conclusion, Table 6
indicates that the trade-off between explainability and performance is not universal but
greatly shaped by the complexity of datasets, the extent of pre-processing and feature
reduction applied uniformly across different types of models, and whether the black-box
approach is a standard global learner or an advanced architecture designed to capture
high-order patterns.

Performance vs. Fairness
Fairness represents a long-standing challenge inherently present in credit scoring
datasets. It reflects a well-known tension with predictive performance, although this
tension is not absolute but conditional in most cases. Its adverse effects on underserved
and excluded populations stem primarily from historical data, which are often biased
and reflect past human decisions (Das et al., 2023; Valdrighi et al., 2025). When these
biased decisions remain unaddressed, the risk of amplifying their impact increases with the
integration of AI models, as such models tend to reproduce the embedded biases within

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 18 -->

J. Risk Financial Manag. 2026, 19, 104

18 of 36

accepted loan applications (Chai et al., 2025; Kozodoi et al., 2025). As a result, fairness is
integral to any credit scoring practice, whether it is traditional, statistical, or AI-based, and
ignoring it perpetuates discrimination.

Across the literature, given that bias is inevitable, fairness is often treated as a multi-
objective optimization problem that aims to optimize predictions under soft constraints
(S. Liu & Vicente, 2022; Martinez et al., 2020). This means that predictive capability and
equitable group treatment are jointly optimized rather than one being maximized at the
expense of the other. For instance, Balashankar and Lees (2022) argued that fairness in ML
can be achieved by transparently presenting non-dominant and best-performing trade-offs
between demographic group accuracy and overall prediction. Using a Pareto frontier,
human involvement becomes central to determine the best trade-off between performance
and fairness (Zehlike et al., 2025). Similar approaches have been reported in other studies
(Badar & Fisichella, 2024; S. Liu & Vicente, 2022; Martinez et al., 2020), confirming that the
trade-off between performance and fairness is unavoidable and is typically modeled as an
optimization problem seeking to balance both objectives.

Having said that, Kozodoi et al. (2022) and Badar and Fisichella (2024) further noted
that fairness can be improved while ensuring minimum loss in profit and performance,
provided that parity constraints are not enforced too strictly. In contrast, having strict parity
conditions could potentially lead to deterioration in prediction utility. This observation
was empirically reported by S. Liu and Vicente (2022), where they concluded that fair-
ness constraints reduce accuracy progressively as they tighten. By adjusting the objective
function to minimize prediction loss and fairness violation terms, they derived a curve
of optimal trade-offs, demonstrating a proportional relationship between accuracy and
fairness violations. In other words, minimizing fairness violation results in degraded
accuracy, and vice versa, confirming that fairness is tunable and not strictly achieved.
Therefore, data imbalance strategies contribute to fairness to the extent that they restore
representativeness and reconstruct missing groups that would otherwise be represented as
a structural discrimination.

Furthermore, although fairness and data imbalance are treated separately across the
literature, they implicitly influence one another and can potentially degrade fairness across
protected groups if not addressed (Brzezinski et al., 2024; J. Liu et al., 2024; Shi et al., 2025).
It forms not only a technical issue hindering performance, but also a material exclusion
system embedded into credit scoring models. Considering that protected groups are not
present at equal rates across different outcomes, data imbalance techniques can rectify the
adverse effects by over-representing these minority groups in the minority (default) class.
A similar trade-off pattern can be observed when considering data imbalance mitiga-
tion strategies. For instance, the work of Kozodoi et al. (2025) demonstrated a recoverable
36% of performance loss using their proposed BASL rejection inference framework while
simultaneously improving fairness compared with traditional sampling techniques. The
goal of their framework was to gradually infer labels to unlabeled samples iteratively, until
model performance improves. The process of relabeling continues until all samples in
a dataset are labeled and ready for final training. However, they simply noted that this
iterative process is prone to sampling bias, hence increasing the risk of overconfidence and
overfitting of a model, and thereby degrading the generalization of the model. The same
observation was also made by Sulastri et al. (2025) and Atif (2025), where strong inclusion
adjustments potentially harm generalization and stability.

Overall, the literature suggests that while there exists a notable trade-off, fairness is
neither impossible nor completely achievable, but tunable. This indicates that fairness is
an optimization decision that is bounded by risk tolerance and societal constraints rather
than being a technical impossibility. The literature showed some cases where moderate

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 19 -->

J. Risk Financial Manag. 2026, 19, 104

19 of 36

fairness adjustments achieved compelling results in terms of performance as well as fairness,
whereas aggressive corrections tend to distort data distributions and often lead to overfitting
and instability.

4.2. Fairness Strategies in Deployment Pipelines (RQ2)

Despite the notable growth in integrating fairness into AI deployments, as shown in
Figure 4, out of the selected 43 papers, only 10 explicitly measured the effectiveness
of existing mitigation strategies or proposed novel ones to counter bias in the credit
scoring domain. This represents no more than 23.25% of the total reviewed studies, despite
fairness being an integral and long-standing concern in credit scoring rather than a newly
introduced concept (Brzezinski et al., 2024; Kozodoi et al., 2022). As a result, relatively
few studies have addressed the adverse implications of protected attributes in lending
decisions, particularly in algorithmic decision-making settings that are prone to producing
discriminatory outcomes that disproportionately affect minority groups (Moldovan, 2023).
This pattern aligns with the observation of Kozodoi et al. (2022), who explicitly stated that
fairness remains underexplored relative to explainability and class imbalance.

Before delving into fairness mitigation strategies, it is worth noting that fairness
comes in two different notions: individual and group fairness (Valdrighi et al., 2025). The
latter is focused on generalizing credit decisions across groups characterized by protected
attributes such as gender, ethnicity, and religion. All studies included herein operationalize
group fairness, whereas individual fairness was mentioned only conceptually in a few
studies, such as the work of Kozodoi et al. (2022), as well as Valdrighi et al. (2025), without
empirical implementation. To determine fairness effectiveness, commonly known metrics
are used to evaluate their suitability across different notions, which include independence,
separation, and sufficiency (Kozodoi et al., 2025; Moldovan, 2023). These metrics were
found to be incompatible when combined, and there is no universal agreement on which
metric should be prioritized (Brzezinski et al., 2024; Zehlike et al., 2025). Due to this,
Zehlike et al. (2025) proposed a novel algorithm called Fair Interpolation Method (FAIM)
that interpolates between the three fairness criteria to develop a reward/penalty objective
function that relaxes the notion of competing metrics, resulting in a weighted combination
of fairness criteria.

Considering that bias may enter the deployment pipeline at multiple stages (Das
et al., 2023), fairness metrics are consistently applied as downstream evaluation measures,
regardless of the intervention point. Accordingly, the literature organizes fairness inter-
ventions into three broad categories based on their position in the deployment pipeline:
pre-processing, in-processing, and post-processing (Valdrighi et al., 2025). To date, no
consensus exists regarding a universally dominant mitigation strategy, rendering fairness
a practical challenge for lending institutions, as each category exhibits distinct strengths
and limitations (Kozodoi et al., 2022; Moldovan, 2023). The full set of fairness mitiga-
tion strategies identified from the reviewed literature, categorized by intervention stage
and methodological characteristics, is summarized in Appendix C. Across categories, no
mitigation strategy consistently dominates others, reinforcing the view of fairness as a
context-dependent optimization problem rather than a universal correction. Accordingly,
the comparison scope is inevitably large, with the existence of common aspects that touch
on each mitigation strategy. For example, pre-processing methods intervene before the
training phase of AI models and aim to modify the distribution of data prior to training
(S. Han et al., 2024). This often leads to lower deployment costs and the ability to improve
fairness without having to retrain models, considering model retraining is time-consuming
(Kozodoi et al., 2022). Nonetheless, since pre-processing strategies are model agnostic, they
often require repeated adjustments to the data pipeline and potentially lead to overfitting

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 20 -->

J. Risk Financial Manag. 2026, 19, 104

20 of 36

when fairness is strictly enforced, making them good strategies to tune and reduce bias,
rather than completely eliminate it (Chai et al., 2025).

Additionally, according to Kozodoi et al. (2022), in-processing techniques consistently
achieve larger fairness gains with minimal loss in predictive utility, assuming that fairness
is embedded into the optimization objective itself. Since they typically report the trade-off
between accuracy and equity in a Pareto frontier, in-processing techniques offer better
control and oversight to realize Pareto-efficient compromises. Several other studies also
reported this behavior, confirming that the trade-off is more tunable while having explicit
control over the outcomes (S. Liu & Vicente, 2022; Moldovan, 2023). Conversely, since
they account for multiple objectives simultaneously, they incur higher computational
cost and often require hyperparameter tuning to identify the optimal configuration due
to their model-specific mechanism, thereby resulting in higher implementation burden
(Valdrighi et al., 2025).

Similar to pre-processing methods, post-processing is another form of model-agnostic
techniques that aim to adjust model outputs post-training to meet fairness criteria
(Zehlike et al., 2025). This makes them a versatile option for black-box models and strictly
governed scorecards, since bias mitigation is performed in isolation from the model’s
training and prediction themselves (Valdrighi et al., 2025). Despite this, they incur the
highest utility cost per fairness gain and cannot repair upstream bias since they act solely
on the decision boundary. As a result, post-processing techniques exhibit a substantial
decrease in profitability relative to in-processing options, and they are less tunable than
in-processing techniques since they operate on outputs instead of learned representations
(Kozodoi et al., 2022).

Synthesizing the findings across studies reveals that fairness mitigation should be
viewed as an optimization problem rather than a one-time corrective step, with trade-
offs emerging between predictive performance, implementation complexity, and regu-
latory suitability. Pre-processing methods intervene before model training by modify-
ing data distributions (S. Han et al., 2024), often offering lower deployment costs and
model-agnostic applicability. However, strict enforcement of fairness constraints at the
data level may require repeated adjustments and can introduce overfitting risks, mak-
ing such approaches more suitable for bias reduction rather than complete mitigation
(Chai et al., 2025; Kozodoi et al., 2022).

Overall, while each fairness strategy has its own strengths and weaknesses, the litera-
ture makes it evident that there exists no universally dominant strategy across the scoring
pipeline. Rather, these strategies emerge as a case-dependent optimization problem that
is mainly influenced by the regulatory environment and the level of risk appetite within
the institution. Consequently, this positions fairness as a continuous process that must
be integrated holistically throughout the deployment pipeline, rather than corrected at a
single stage, as already highlighted by Das et al. (2023).

4.3. Regulatory, Ethical, and Governance Foundations for Fair AI Credit Scoring (RQ3)

In the United States, the Equal Credit Opportunity Act (ECOA) and the Fair Credit
Reporting Act (FCRA) have collectively imposed obligations to ensure equal treatment
across protected groups, and more importantly, to provide “adverse decision justifications”
within strict timelines (Kumar et al., 2022). These statutory requirements implicitly mandate
interpretable AI systems capable of supporting supervisory examinations and consumer
recourse. Similarly, in Europe, models that operate opaquely and fail to provide adequate
justification for algorithmically determined results were subjected to mistrust, viewed as
presenting heightened bias risks, and classified as high-risk applications (Langenbucher,
2020). Accordingly, the European Union enforced fairness-through-explainability require-

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 21 -->

J. Risk Financial Manag. 2026, 19, 104

21 of 36

ments under the forthcoming AI Act, emphasizing transparency and adequate fairness
measures (Perry et al., 2023). Additionally, privacy laws such as GDPR intersect with these
fairness obligations, as sensitive attributes may directly or indirectly influence outcomes,
posing discriminatory risks if left unmitigated (Ridzuan et al., 2024).

Beyond Western regulatory frameworks, the ASEAN region also experienced the
rise of governance approaches that prioritize fairness in the algorithmic lending process,
with additional emphasis on human oversight (Lainez & Gardner, 2023). Similar to the
EU AI Act proposal, ASEAN policy guidance encourages the HITL review, particularly
in high-stakes and credit scoring domains, while also stressing explainability as a key
enabler for a supervised evaluation (Ridzuan et al., 2024). This makes human intervention
central to validating outcomes and correcting undesired results. While these laws and
acts referenced in the literature might seem less prescriptive, they signal a growing global
convergence toward responsible AI credit scoring, with notable variation in maturity and
enforcement intensity. However, across multiple jurisdictional settings, these expectations
converge on the principle of fairness in algorithmic decision-making, which cannot be
achieved without consciously adopting AI systems that provide adequate explainability.
Explainability serves as the mechanism through which discriminatory risks can be revealed,
adverse effects can be justified, and, in the most severe cases, corrected through human
oversight. Thus, it functions not merely as a transparency tool but as a pivotal enabler for
equity, accountability, and the ethical deployment of AI (Langenbucher, 2020).

The included literature provides richer detail for Western and ASEAN regions, whereas
coverage beyond these settings becomes comparatively sparse and fragmented. In these
cases, explicit governance and privacy references appear less frequently and are often
discussed at a higher level of abstraction. For example, additional evidence from other
Asian settings includes institutional governance signals, such as the Bank of Indonesia
supporting credit-related decision-making through MSME profiling (Hartomo et al., 2025)
and Hong Kong SAR banking guidance on consumer protection and high-level AI usage
principles (Ridzuan et al., 2024). Within ASEAN, Vietnam provides comparatively richer
legal framing, where algorithmic credit scoring is described as expanding amid weak
oversight, motivating proposals for stronger safeguards, including limits on data collection,
consumer rights to explanation and appeal, and inspection powers by regulators such
as the State Bank of Vietnam, together with explicit obligations aligned to personal data
protection such as consent, correction, deletion after use, and notification of third-party
transfers (Lainez & Gardner, 2023). In Africa, one study notes that credit regulators in South
Africa require credit decision models to provide human-understandable interpretations
(Hlongwane et al., 2024), while evidence linked to Latin America highlights that regulatory
and privacy requirements constrain the availability of comprehensive public financial
datasets for research and benchmarking, particularly in Brazil (Valdrighi et al., 2025).

Nonetheless, the literature increasingly shifts from treating fairness, often framed
through anti-discrimination and consumer protection expectations, and explainability as
optional add-ons to recognizing them as foundational necessities in AI credit scoring, re-
flecting how global laws and regulatory contexts are shaping algorithmic decision-making.
Although explainability and fairness were addressed separately in most of the works
included herein, the reviewed studies consistently emphasize their conceptual interde-
pendence (Langenbucher, 2020). Model explainability constitutes the operational bridge
between fairness goals, compliance and human judgment and thereby supports audit-
ing, adverse-action reasoning, and regulatory disclosure (Das et al., 2023). Although most
reviewed studies address these pillars separately, the work of Hickey et al. (2020) opera-
tionalized the role of explainability to support fairness in the lending process. They argued
that while post-hoc explainability is widely adopted, it does not itself resolve fairness issues

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 22 -->

J. Risk Financial Manag. 2026, 19, 104

22 of 36

but rather guides their operationalization. To address this, they proposed a SHAP-based
regularization term that penalizes predictions correlated with protected attributes. This
penalty was incorporated into the model’s loss function to discourage it from providing pre-
dictions that highly depend on protected attributes. This adversarial technique constrains
the attributions to force fairness through explainability, thereby serving as the mechanism
that directly exposes and regulates a model’s dependence on protected attributes.

In support of fairness, however, the EU AI Act, as well as ECOA, explicitly empha-
size the right to contest adverse action notices, extending auditors’ ability to challenge
automated outcomes and obtain meaningful reconsideration to ensure essential procedu-
ral safeguards (Kumar et al., 2022; Langenbucher, 2020). This captures a key idea that
explainability is not merely for consumers but for supervisory examination and audit
trails, enabling individuals to appeal or seek reconsideration when outcomes are doubtful.
The concept of challenging outcomes through human oversight and providing means to
correct unintentional adverse outcomes aligns well with the qualitative study conducted
by Kuiper et al. (2021), where they managed to investigate the disparity between practice
and legal frameworks concerning explainability. They reported that when interpretability
is inherent, additional explainability becomes less critical. However, they also noted that
explainability becomes evidently crucial when advanced AI models produce results that
conflict with the outcomes made by traditional models, encouraging human intervention
to act as a potential ethical safeguard.

In addition, given the fairness–performance trade-off, human-in-the-loop (HITL)
oversight can be operationalized as a recurring governance mechanism across the fair-
ness pipeline, ensuring that human judgment remains embedded throughout model de-
velopment and deployment. First, HITL can be applied between pre-processing and
in-processing stages to certify augmented and rebalanced datasets and verify that augmen-
tation does not amplify historical bias through historical repayment records, particularly
given that leakage of protected attributes through proxies is a known risk in credit scor-
ing (Das et al., 2023). Second, HITL can support model selection during in-processing by
determining an appropriate trade-off among Pareto non-dominant solutions returned by
fairness-aware learning techniques, aligning with the fairness–performance tension dis-
cussed in RQ2 and enabling institutions to select models that satisfy regulatory expectations
without incurring unjustified performance degradation. Lastly, HITL remains essential in
post-processing as a corrective layer that mitigates residual or leaked bias by reviewing
flagged outcomes and overriding adverse decisions that conflict with fairness policies or
governance requirements. Together, these operational roles demonstrate that HITL is not
merely an optional intervention but a practical governance layer that supports certifiable
fairness and accountability under realistic deployment conditions.

In summary, while supervisory frameworks do not explicitly state how fairness and
explainability must be enforced to ensure ethical deployments, they played a pivotal role
in shaping modern credit scoring. Initially, it started by mandating justification of adverse
effects and enabling recourse mechanisms, but further extended beyond consumer-facing
transparency to enabling contesting and correcting unintended results that potentially lead
to discriminatory effects. Moreover, as the legal systems prioritize fairness and explain-
ability equally, they also unveil a well-established tie between the two. Fairness must be
operationalized through interpretable and contestable AI systems, with human judgment
serving as the ethical safeguard that ensures alignment with regulatory and societal expec-
tations. Therefore, regulatory frameworks and ethical governance do not merely influence
fairness interpretation; rather, they structurally integrate explainability as the mechanism
through which fairness is evaluated, enforced, and ethically operationalized in AI credit
scoring systems.

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 23 -->

J. Risk Financial Manag. 2026, 19, 104

23 of 36

5. Gaps and Future Directions

Despite various efforts to address performance, fairness, and explainability as three
core pillars in the ethical deployment of AI-based credit scoring, several gaps persist
that require further investigation. From a technical and methodological standpoint, fu-
ture research must move beyond post-hoc explainability to develop standardized frame-
works that incorporate explainability as a model constraint, enabling a “fairness-through-
explainability” paradigm that reduces model opacity. This paradigm aligns well with
anticipated regulatory requirements, such as the ability to detect bias in results, including
those caused by proxy, protected attributes, correct adverse outcomes through human
oversight, and justify adverse decisions to consumers, all of which cannot be achieved
without establishing strict ties between fairness and explainability. This transition redefines
explainability from a technical add-on to a meaningful capability that facilitates fairness
and invites human judgment when necessary.

From a regulatory and auditing perspective, although many studies acknowledge the
importance of human-in-the-loop (HITL) oversight, it remains under-specified in terms of
practical implementation. In particular, the literature rarely defines measurable escalation
triggers such as borderline cases, low-confidence predictions, or fairness-related flags,
standardized reviewer actions, or mechanisms for incorporating human feedback into
model monitoring and governance. Future work should therefore formalize HITL as an
operational protocol within credit scoring pipelines, ensuring traceable review, contesta-
bility of adverse outcomes, and consistent alignment with local compliance and auditing
requirements. This is especially important when fairness constraints introduce performance
trade-offs, where human governance is needed to justify model adoption decisions under
institutional risk tolerance.

Furthermore, while the conflict between explainability and performance is widely
debated, it is rarely quantified. Since there are no explicit legal mandates dictating the
choice between inherently interpretable and black-box models, it signals the need for more
standardized methodologies that quantify the performance loss incurred when compro-
mising performance for model transparency. Reporting potential loss in performance for
inherently interpretable models can serve as practical guidance for lending institutions,
enabling them to select between transparent and black-box models and justify the move
toward black-boxes if necessary, all of which depend heavily on the level of risk tolerance
and appetite.

In addition, given that no fairness metric or method is universal, and since regulatory
frameworks typically mandate fairness outcomes without explicitly specifying technical
metrics, it is anticipated that future work must focus on interpolating and reconciling
incompatible fairness metrics, ensuring context-aware metric and methodological selection
that aligns with the legal definition of non-discrimination across different jurisdictional
settings. This includes determining which metric, or combination thereof, aligns well with
legal definitions that concern non-discrimination.

Overall, the most significant gap would be the absence of standardized AI credit
scoring frameworks that jointly optimize all three pillars simultaneously while establishing
well-grounded, structural ties between them. Current methods often involve training for
performance, then incorporating explainability methods, and then adjusting for fairness,
when in reality, these dimensions intersect across all stages of the deployment pipeline.
Therefore, future research must focus on proposing unified, multi-objective frameworks that
treat performance, fairness, and explainability as interdependent constraints, addressing
HITL and regulatory requirements concurrently.

Finally, this systematic review is intended to serve as a foundation for a future applied
study aimed at developing and validating an AI credit scoring model that operationalizes

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 24 -->

J. Risk Financial Manag. 2026, 19, 104

24 of 36

the review conclusions within a deployable pipeline. While this work is an evidence
synthesis and does not propose a deployable system, these findings will guide model
selection under practical constraints, support integrating explainability as a structural
requirement rather than a post-hoc add-on, and evaluate fairness and performance stability
under realistic conditions that support human judgment when necessary. Such work would
enable empirical verification of unified, multi-objective credit scoring frameworks that
align performance, fairness, explainability, and HITL requirements with regulatory and
auditing expectations.

6. Conclusions

This systematic literature review (SLR) synthesizes 43 high-quality academic papers
published between 2020 and 2025, focusing on the intersection of performance, fairness,
and explainability in AI credit scoring. By adhering to PRISMA guidelines and employing
a detailed 3Rs&Q appraisal framework, the review established that while credit scoring
models continue to grapple with performance trade-offs, explainability has become the
dominant research pillar since 2023. This shift is largely driven by regulatory frameworks,
such as the EU AI Act, ECOA, and ASEAN principles, which mandate interpretable systems
capable of delivering adverse decision justifications, thereby reinforcing the need for human
oversight. Although the trade-off between explainability and performance persists, the
choice between interpretable and black-box models is shaped primarily by the risk tolerance
level of a lending institution, and this trade-off is scarcely measured across the literature.
In relation to the research questions, the review finds that (RQ1) the widely cited
trade-off between explainability and performance is largely assumed rather than empiri-
cally demonstrated; the limited studies that quantify this relationship show only marginal
differences between inherently interpretable and black-box models, indicating that the
choice between them is determined primarily by an institution’s risk tolerance rather than
measurable predictive loss. In contrast, the trade-off between performance and fairness
is consistently confirmed across the literature: fairness is treated as a multi-objective opti-
mization problem, and aggressive enforcement of fairness constraints results in significant
performance degradation, whereas moderate fairness adjustments tend to yield balanced
improvements. (RQ2) Bias originates primarily from historical data patterns, class imbal-
ance, and the inclusion of protected attributes, with mitigation strategies applied across
different stages differing in strengths, but no universally optimal solution. (RQ3) Reg-
ulatory and governance frameworks increasingly emphasize explainability and human
oversight, yet existing studies have not fully integrated these requirements into unified,
end-to-end credit scoring pipelines.

In addition, despite significant research into multi-objective optimization for balancing
performance and fairness, the current literature predominantly relies on fragmented and
sequential approaches. Models are often optimized for accuracy first, with fairness and
explainability applied as adjustments. This deficiency represents the most pressing finding
of the review, demonstrating the absence of a unified, holistic AI credit scoring framework
that co-optimizes all three pillars simultaneously across all stages. Such sequential method-
ologies are inadequate for meeting the strict compliance expectations of modern regulatory
environments and fail to embed transparency from the ground up.

To address this critical gap, the review recommends three key directions for future
research. First, scholars must focus on developing novel, unified co-optimization frame-
works that treat performance, fairness, and explainability as interdependent constraints
throughout the entire model design life-cycle. Second, research must advance beyond sta-
tistical definitions of fairness by developing and validating contextualized fairness metrics
tailored to specific lending markets and their socio-economic effects on protected groups.

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 25 -->

J. Risk Financial Manag. 2026, 19, 104

25 of 36

Finally, empirical investigations into human-in-the-loop (HITL) integration are required to
examine how auditors and compliance officers can effectively leverage explainability to
ensure regulatory compliance and produce credible, real-world outcomes.

Author Contributions: Conceptualization, R.B.; methodology, R.B., N.H. and W.E.; software, R.B.;
validation, N.H. and W.E.; formal analysis, R.B.; investigation, R.B.; resources, W.E.; data curation,
R.B.; writing—original draft preparation, R.B.; writing—review and editing, N.H. and W.E.; supervi-
sion, N.H. and W.E.; project administration, N.H. All authors have read and agreed to the published
version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: This study is based on the previously published literature. No new
datasets were generated or analyzed. All referenced datasets are publicly available from the sources
cited in the corresponding studies. The study selection protocol and appraisal criteria are available
from the corresponding author upon reasonable request.

Conflicts of Interest: The authors declare no conflict of interest.

Appendix A

Table A1. Full-text excluded studies and reasons for exclusion (Part 1: IDs 1–8).

ID Author(s)

Title

Exclusion Reason

PRISMA Bucket

1

Zacharias et al. (2022)

Designing a feature selection
method based on explainable
artificial intelligence

2

3

Corrales-Barquero et al.
(2021)

A Review of Gender Bias
Mitigation in Credit
Scoring Models

de Castro Vieira et al.
(2025)

Towards Fair AI: Mitigating Bias
in Credit Decisions—A
Systematic Literature Review

Excluded due to overlapping scope, as explainability is
applied mainly as post-hoc SHAP-based feature
attribution within a performance-driven pipeline that is
already well represented among the included studies.

Excluded due to overlapping scope, as a survey-style
review summarizing bias mitigation strategies, which is
already covered by more recent or synthesis-relevant
included sources, contributing limited additional evidence
to the review objectives.

Excluded due to overlapping scope, as the study is
primarily a survey summarizing fairness and bias
mitigation without providing distinct empirical evidence
or integrated analysis across performance, fairness, and
explainability beyond included works.

Overlapping scope

Overlapping scope

Overlapping scope

4

Vukovi´c et al. (2025)

AI integration in financial
services: a systematic review of
trends and regulatory challenges

Excluded as out of scope, as it addresses AI in financial
services broadly rather than AI-based credit scoring and
does not provide credit scoring-specific evidence aligned
with the review eligibility criteria.

Did not meet
eligibility

5

Cornacchia et al. (2023)

6

Mou et al. (2024)

7

Cao et al. (2021)

8 Wu et al. (2025)

A General Architecture for a
Trustworthy Creditworthiness-
Assessment Platform in the
Financial Domain

Excluded due to overlapping scope, as the study
emphasizes a performance-oriented architecture with
explainability treated primarily as a post-hoc component,
overlapping with included works addressing similar
post-hoc explainability configurations.

Cost-aware Credit-scoring
Framework Based on
Resampling and Feature
Selection

Excluded as performance-oriented only, focusing on class
imbalance handling, resampling, and feature selection for
cost-aware optimization without substantive treatment of
fairness or explainability as primary review pillars.

Ensemble methods for credit
scoring of Chinese peer-to-peer
loans

Excluded as performance-oriented only, as it evaluates
ensemble learning primarily for predictive performance
without explicit fairness, explainability, or regulatory/
HITL considerations aligned with the review scope.

A ‘divide and conquer’ reject
inference approach leveraging
graph-based semi-supervised
learning

Excluded as reject-inference/performance-oriented, where
reject inference is used to address sample selection bias
and improve predictive performance without
protected-attribute fairness analysis or explainability
objectives aligned with the review synthesis goals.

Overlapping scope

Did not meet
eligibility

Did not meet
eligibility

Did not meet
eligibility

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 26 -->

J. Risk Financial Manag. 2026, 19, 104

26 of 36

Table A2. Full-text excluded studies and reasons for exclusion (Part 2: IDs 9–15).

ID Author(s)

Title

Exclusion Reason

PRISMA Bucket

9

Liao et al. (2022)

Combating Sampling Bias: A
Self-Training Method in Credit
Risk Models

Excluded as performance/sample-bias oriented, focusing
on accepted-only sampling bias using self-training without
explicitly addressing fairness across protected attributes or
explainability as core objectives.

Did not meet
eligibility

10

C-Rella et al. (2025)

Cost-sensitive reinforcement
learning for credit risk

11 Koulu (2019)

Human control over automation:
EU policy and AI ethics

12

Z. Li et al. (2020)

Inferring the outcomes of
rejected loans: an application of
semisupervised clustering

Excluded as performance-oriented only, proposing
cost-sensitive reinforcement learning to optimize credit
risk decisioning without operationalizing fairness,
explainability, or regulatory/HITL requirements central to
the review eligibility criteria.

Excluded as not eligible, as it is primarily a legal/policy
discussion of automation and AI ethics without credit
scoring-specific empirical methods or operational evidence
supporting synthesis across performance, fairness, and
explainability.

Excluded as reject-inference/performance-oriented,
focusing on outcome inference for rejected applicants to
enhance prediction performance, with fairness and
explainability not treated as central,
operationalized objectives.

Did not meet
eligibility

Did not meet
eligibility

Did not meet
eligibility

13

Tiukhova et al. (2025)

Boosting Credit Risk Data
Quality Using Machine Learning
and eXplainable AI Techniques

Excluded due to overlapping scope, as XAI is applied
mainly for data/model diagnostics, and explainability is
treated as post-hoc analysis, closely overlapping with
included SHAP-post-hoc explainability studies.

Overlapping scope

14 W. Li et al. (2022)

A data-driven explainable
case-based reasoning approach
for financial risk detection

Excluded as out of scope, as it targets financial risk
detection rather than credit scoring/creditworthiness
assessment, and it does not align with the review’s
domain-specific eligibility criteria.

Did not meet
eligibility

15

Chacko and Aravindhar
(2025)

Enhancing Fairness and
Accuracy in Credit Score
Analysis: A Novel Framework
Utilizing Kernel PCA

Excluded due to insufficient operationalization of fairness,
as fairness is referenced but not clearly defined using
explicit metrics or evaluation protocols that support
structured synthesis under the review eligibility criteria.

Did not meet
eligibility

Appendix B

Table A3. Summary of included studies and their mapping to research questions (Part 1: IDs 1–6).

ID Author(s)

Title

Summary

Related RQs

1

Kozodoi et al. (2022)

Fairness in Credit Scoring:
Assessment, Implementation and
Profit Implications

2

Dessain et al. (2023)

Cost of Explainability in AI: An
Example with Credit Scoring
Models

3

Moldovan (2023)

Algorithmic Decision Making
Methods for Fair Credit Scoring

Examines trade-offs between fairness and profitability in
credit scoring. Integrates fairness metrics into ML pipelines
and evaluates pre-, in-, and post-processing methods
(reweighing, prejudice remover, adversarial debiasing, reject
option) across seven datasets. Concludes fairness can
improve without major performance loss, supporting
regulatory compliance and ethical lending.

Explores the explainability–performance trade-off in credit
scoring. Compares black-box and interpretable models
(XGBoost, NN, LR, GAMs) under ECB compliance.
Introduces isotonic smoothing to align expert judgement
with regulatory master-scale grading. Finds GAM-style
models achieve near-black-box accuracy while preserving
inherent interpretability and meeting regulatory standards.

Assesses algorithmic bias and compares 12 mitigation
strategies across five fairness metrics using German and
Romanian datasets. Highlights that no single fairness
measure satisfies fairness, performance, and profitability
simultaneously. Shows incompatibilities among metrics
(independence, separation, sufficiency) and stresses
regulatory ambiguity and the need for balanced,
multi-method approaches.

RQ1, RQ2

RQ1, RQ3

RQ1, RQ2, RQ3

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 27 -->

J. Risk Financial Manag. 2026, 19, 104

27 of 36

Table A3. Cont.

ID Author(s)

Title

Summary

Related RQs

4

Zehlike et al. (2025)

Beyond Incompatibility: Trade-offs
Between Mutually Exclusive
Fairness Criteria in Machine
Learning and Law

5

Das et al. (2023)

Algorithmic Fairness

Introduces the Fair Interpolation Method (FAIM), a
post-processing algorithm using optimal transport to
interpolate between calibration, balance for positives, and
balance for negatives. Motivated by the EU AI Act, it
addresses fairness incompatibility and legal ambiguity,
emphasizing regulator involvement and human oversight
for trade-off management across jurisdictions.

Situates fairness within ECOA, FCRA, and supervisory rules;
distinguishes individual vs. group fairness. Argues bias can
enter pre-, in-, or post-training and catalogues dataset biases
and metrics (e.g., DI, EO, equalized odds, predictive parity).
Advocates a systemic approach combining data quality,
interpretability, and regulatory alignment.

RQ1, RQ2, RQ3

RQ2, RQ3

6

Brzezinski et al. (2024)

Properties of Fairness Measures in
the Context of Varying Class
Imbalance and Protected
Group Ratios

Analyzes effects of class imbalance and protected-group ratios
on fairness metrics using the UCI Adult dataset. Finds
Statistical Parity Difference and Disparate Impact are highly
sensitive to imbalance, while Equal Opportunity and Average
Odds Difference are more stable. Recommends contextual
evaluation combining fairness and performance indicators.

RQ2

Table A4. Summary of included studies and their mapping to research questions (Part 2: IDs 7–12).

ID Author(s)

Title

Summary

Related RQs

7

Langenbucher and
Corcoran (2022)

Responsible AI Credit Scoring–A
Lesson from Upstart.com

8

Langenbucher (2020)

Responsible A.I.-based Credit
Scoring–A Legal Framework

9

Valdrighi et al. (2025)

Best Practices for Responsible
Machine Learning in Credit Scoring

10 Kuiper et al. (2021)

Exploring Explainable AI in the
Financial Sector: Perspectives of
Banks and Supervisory Authorities

11

Balashankar and Lees
(2022)

The Need for Transparent
Demographic Group Trade-Offs in
Credit Risk and Income
Classification

12 Amekoe et al. (2024)

Exploring Accuracy and
Interpretability Trade-off in Tabular
Learning with Novel
Attention-based Models

Examines regulatory and ethical challenges in AI-driven
credit scoring under GDPR, ECOA, FCRA, and GLBA.
Highlights privacy risks, proxy discrimination, and
fairness–accuracy trade-offs. Recommends transparency,
fairness audits, human-in-the-loop oversight, and regulator
collaboration to ensure compliant and explainable lending
decisions.

RQ1, RQ3

Outlines a legal framework for responsible AI credit scoring
based on transparency, fairness, and accountability. Warns
opaque models can conflict with GDPR’s “right to explain.”
Recommends embedding interpretability, validating fairness
throughout model phases, enforcing human oversight, and
assigning accountability roles for lawful deployment.

RQ3

Addresses bias, transparency, and reject inference in
AI-based credit scoring across German, Taiwanese, and
Home Credit datasets. Discusses bias origins, fairness
metrics (group and individual), and mitigation across pre-,
in-, and post-processing. Highlights transparency tools
(LIME, SHAP, PD, ICE) and emphasizes inclusive,
responsible deployment.

Reports qualitative findings from Dutch banks and
regulators on integrating XAI into credit scoring. Defines
explainability as transparency into model reasoning, data,
and design. Notes reliance on interpretable traditional
models, human safeguards, and phased deployment.
Positions explainability as essential for ethical, accountable,
regulatory-aligned AI.

Highlights fairness as jurisdiction-dependent. Uses Pareto
principles to balance group- and overall-level accuracies
with human-in-the-loop oversight. Shows intersecting
protected attributes reduce sample sizes and degrade
accuracy, motivating data improvements. Advocates
transparent trade-off visualization to align fairness,
performance, and social objectives.

Quantifies accuracy–interpretability trade-offs in tabular
learning using 45 datasets. Finds less than 4% accuracy loss
between black-box and inherently interpretable models.
Proposes a TabSRA attention-based ensemble inspired by
GAMs, offering feature-level interpretability and stable
performance; argues for inherent interpretability in
high-stakes domains.

RQ1, RQ2

RQ1, RQ3

RQ1, RQ2, RQ3

RQ1, RQ3

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 28 -->

J. Risk Financial Manag. 2026, 19, 104

28 of 36

Table A5. Summary of included studies and their mapping to research questions (Part 3: IDs 13–18).

ID Author(s)

Title

Summary

Related RQs

13

S. Liu and Vicente
(2022)

Accuracy and Fairness Trade-offs in
Machine Learning: A Stochastic
Multi-objective Approach

14 Martinez et al. (2020)

Minimax Pareto Fairness: A
Multi-objective Perspective

15

Badar and Fisichella
(2024)

Fair-CMNB: Advancing
Fairness-Aware Stream Learning
with Naïve Bayes and
Multi-Objective Optimization

16

J. Liu et al. (2024)

Credit Risk Prediction Based on
Causal Machine Learning: Bayesian
Network Learning, Default
Inference, and Interpretation

17 Hickey et al. (2020)

Fairness by Explicability and
Adversarial SHAP Learning

Formulates fairness–accuracy trade-offs as a stochastic
multi-objective optimization problem. Proposes the
Stochastic Multi-Gradient (SMG) algorithm using Disparate
Impact and Equal Opportunity as constraints. Demonstrates
Pareto frontiers on the UCI Adult dataset, showing tension
between fairness and accuracy driven by proxy and
protected attributes.

Models group fairness as multi-objective optimization where
each sensitive group defines a fairness objective. Proposes
Minimum-Maximum Pareto Fairness (MMPF) using neural
networks with post-hoc corrections to reduce risk disparity.
Evaluated on German Credit and Adult Income datasets
with accuracy, Brier score, and cross-entropy metrics.

Proposes Fair-CMNB, a fairness- and imbalance-aware
Mixed Naïve Bayes model for streaming credit data using
multi-objective optimization. Introduces dynamic instance
weighting to prioritize minority updates and control
discrimination. Reports improved accuracy and fairness
over baselines, emphasizing scalability and practicality for
high-stakes credit scoring.

Applies causal ML with Bayesian networks to model
cause–effect relations and enable transparent decision
analysis via DAGs. Uses SMOTE and L1 regularization for
imbalance handling and feature selection. Supports
interpretable, regulation-oriented what-if analysis across six
real datasets.

Proposes an adversarial SHAP framework linking fairness
and explainability by penalizing predictions correlated with
protected attributes via SHAP-based regularization. Uses
surrogate auditing to mirror oversight. Demonstrates
improved fairness and interpretability on Adult Income and
proprietary credit datasets while maintaining strong
predictive performance.

RQ1, RQ2

RQ1, RQ2

RQ1, RQ2

RQ1, RQ2, RQ3

RQ1, RQ2, RQ3

18

Lainez and Gardner
(2023)

Algorithmic Credit Scoring in
Vietnam: A Legal Proposal for
Maximizing Benefits and
Minimizing Risks

Analyzes regulatory gaps and ethical risks in Vietnam’s
adoption of algorithmic credit scoring. Highlights
discrimination, bias, opacity, and privacy concerns under
FCRA, ECOA, FCA, and the EU AI Act. Advocates stronger
legal oversight and interpretability standards to restore trust
and fairness.

RQ3

Table A6. Summary of included studies and their mapping to research questions (Part 4: IDs 19–24).

ID Author(s)

Title

Summary

19 Nwafor et al. (2024)

Enhancing Transparency and
Fairness in Automated Credit
Decisions: An Explainable Novel
Hybrid Machine Learning Approach

20

S. Han et al. (2024)

NOTE: Non-parametric
Oversampling Technique for
Explainable Credit Scoring

21 Kozodoi et al. (2025)

Fighting Sampling Bias: A
Framework for Training and
Evaluating Credit Scoring Models

Proposes a hybrid CNN–XGBoost stacking model to improve
accuracy and interpretability in credit scoring. Uses SHAP
global explanations to examine feature effects on the Lending
Club dataset. Reports high predictive performance while
enhancing transparency and trust in automated lending
decisions.

Introduces NOTE, a non-parametric oversampling approach
combining stacked autoencoders and conditional Wasserstein
GANs to address severe class imbalance. Evaluated on Home
Equity and Give Me Some Credit datasets; reports improved
accuracy over ADSGAN and DeepSMOTE. Uses SHAP for
global interpretability, linking imbalance correction with
explainable credit scoring.

Proposes BASL, a bias-aware self-learning framework
addressing sampling bias from missing rejected applicants.
Uses a semi-supervised Bayesian approach to iteratively label
unlabeled data while filtering outliers. Applied to Monedo’s
real-world dataset; recovers up to 36% performance loss due to
sampling bias and outperforms reweighting and
Heckman-style methods.

Related RQs

RQ1, RQ2

RQ1, RQ2

RQ1, RQ2

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 29 -->

J. Risk Financial Manag. 2026, 19, 104

29 of 36

Table A6. Cont.

ID Author(s)

Title

Summary

22

Shi et al. (2025)

Credit Scoring Prediction Using Deep
Learning Models in the Financial
Sector

23

Bueff et al. (2022)

Machine Learning Interpretability for
a Stress Scenario Generation in Credit
Scoring Based on Counterfactuals

24 Kumar et al. (2022)

Equalizing Credit Opportunity in
Algorithms: Aligning Algorithmic
Fairness Research with U.S. Fair
Lending Regulation

Proposes a hybrid LSTM-based framework capturing temporal
borrower behavior for credit scoring. Uses SMOTE,
normalization, and one-hot encoding for imbalance handling.
Introduces a hybrid loss with interpretability regularization
enforcing feature sparsity, aiming to retain transparency
without relying on post-hoc explainers.

Compares SHAP with counterfactual methods for
interpretability in credit scoring. Uses Genetic Algorithms to
generate counterfactuals identifying minimal feature changes
needed to alter outcomes. Links interpretability to robustness
under stress scenarios and highlights how counterfactuals
expose sensitive decision boundaries and bias-prone features.

Aligns algorithmic fairness research with US
anti-discrimination laws (ECOA, FCRA, HMDA). Discusses
disparate impact/treatment as legal fairness criteria and the
role of proxy attributes in bias. Advocates causal and
counterfactual analysis and regulatory oversight for equitable,
transparent AI-driven lending practices.

Related RQs

RQ1, RQ2

RQ1, RQ2

RQ2, RQ3

Table A7. Summary of included studies and their mapping to research questions (Part 5: IDs 25–30).

ID Author(s)

Title

Summary

25

Chai et al. (2025)

Farmers’ Credit Risk Evaluation with
an Explainable Hybrid Ensemble
Approach: A Closer Look in
Microfinance

26

Hlongwane et al.
(2024)

A Novel Framework for Enhancing
Transparency in Credit Scoring:
Leveraging Shapley Values for
Interpretable Credit Scorecards

27

Zhang et al. (2025)

An Interpretable Credit Risk
Assessment Model with Boundary
Sample Identification

28

Hjelkrem and Lange
(2023)

Explaining Deep Learning Models for
Credit Scoring with SHAP: A Case
Study Using Open Banking Data

29

Bulut and Arslan
(2025)

A Hybrid Approach to Credit Risk
Assessment Using Bill Payment
Habits Data and Explainable
Artificial Intelligence

30

Ali Shahee and Patel
(2025)

An Explainable ADASYN-Based
Focal Loss Approach for Credit
Assessment

Proposes a hybrid ADASYN–LCE model combining adaptive
resampling and local cascading ensembles for microfinance
credit scoring. Uses SHAP and LIME for interpretability and
fairness validation. Reports improved robustness and visibility
for underserved populations through balanced learning and
explainable ensemble modeling.

Integrates SHAP explanations into credit scoring pipelines
using XGBoost and Random Forest models. Improves
transparency, regulatory alignment, and consumer trust by
visualizing feature attributions. Evaluated on Taiwanese and
Home Credit datasets, demonstrating interpretable
performance aligned with explainability expectations
in lending.

Proposes IAIBS, combining logistic regression and deep
learning to handle ambiguous boundary samples. Uses ARPD
to classify noise/anomalies and applies SHAP for
interpretability. Reports improved AUC while enhancing
transparency via boundary-aware pre-processing.

Compares 1D-CNN and transfer-learning BERT models using
open banking transactions for credit scoring. Uses SHAP to
interpret deep models and support justification under
regulatory mandates. Finds that 1D-CNN outperforms BERT
in AUC and Brier score, emphasizing explainable deep
learning for compliant credit assessment.

Addresses multi-class credit risk prediction using hybrid
ensembles (LR, RF, SVM, NB, MLP) with SMOTE and
ADASYN. Uses Mutual Information to capture proxy
interactions and applies SHAP/LIME for interpretability.
Reports strong performance with tree-based models and
highlights explainable, balanced risk assessment in
alternative-data settings.

Proposes an ANN integrating ADASYN resampling and Focal
Loss to mitigate imbalance. Tested on the German dataset;
reports improved accuracy and AUC over baselines. Uses
SHAP and LIME for feature attribution, aiming to combine
predictive performance with interpretability in credit
assessment.

Related RQs

RQ1, RQ2

RQ1

RQ1

RQ1

RQ1, RQ2

RQ1, RQ2

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 30 -->

J. Risk Financial Manag. 2026, 19, 104

30 of 36

Table A8. Summary of included studies and their mapping to research questions (Part 6: IDs 31–36).

ID Author(s)

Title

Summary

Related RQs

31 Dastile et al. (2022)

Model-Agnostic Counterfactual
Explanations in Credit Scoring

32 Atif (2025)

VAE-INN: Variational Autoencoder
with Integrated Neural Network
Classifier for Imbalanced Credit
Scoring

33 Hartomo et al. (2025)

A Novel Weighted Loss
TabTransformer Integrating
Explainable AI for Imbalanced
Credit Risk Datasets

34 W. Han et al. (2023)

A Multi-layer Multi-view Stacking
Model for Credit Risk Assessment

35

Ridzuan et al. (2024)

AI in the Financial Sector: The Line
Between Innovation, Regulation and
Ethical Responsibility

36

Perry et al. (2023)

Algorithms for All: Can AI in the
Mortgage Market Expand Access to
Homeownership?

Introduces a GA-based counterfactual explanation
framework for black-box credit models. Searches
neighbouring instances that flip predictions with minimal
feature changes, exposing decision boundaries and potential
bias sources. Validated on German and HMEQ datasets,
supporting model-agnostic interpretability for transparency
and auditing.

RQ1

Proposes VAE-INN, a variational autoencoder guided by
weighted loss to counter class imbalance in latent space.
Assigns higher weights to minority classes to reduce Type II
errors. Tested on the Taiwanese credit dataset and reports
improved balanced accuracy and reliability over
SMOTE/ADASYN-based baselines.

Combines TabTransformer with weighted loss to address
class imbalance while preserving interpretability. Applies
SHAP for global feature attribution. Evaluated on German
and BISAID datasets, reporting accuracy/AUC
improvements and demonstrating explainable, balanced
performance for tabular credit scoring.

Introduces MLMVS, a stacking ensemble (LR, MLP, RF,
KNN) with multi-view partitioning (personal, behavioral,
history features). Uses LIME for instance-level
interpretability. Reports gains in accuracy, precision, and
specificity over baselines, supporting interpretable ensemble
learning for default prediction.

Discusses AI governance in finance, emphasizing regulation,
ethical responsibility, and human oversight. Identifies key
challenges (privacy, fairness, accountability) and positions
explainability as central for human decision-making.
Advocates governance approaches aligned with societal
values to foster trust in regulated financial AI.

Examines whether AI can expand mortgage access while
managing bias and equity concerns. Warns historical data
may perpetuate discrimination. Recommends aligning AI
outcomes with legal and ethical frameworks, ensuring
demographic fairness, transparency, and human oversight to
prevent disparate impact.

RQ1, RQ2

RQ1, RQ2

RQ1

RQ3

RQ2, RQ3

Table A9. Summary of included studies and their mapping to research questions (Part 7: IDs 37–43).

ID Author(s)

Title

Summary

Related RQs

37

Repetto (2025)

Multicriteria Interpretability Driven
Deep Learning

38

Sulastri et al. (2025)

Sensitivity Analysis: Improving
Inclusive Credit Scoring Algorithm
Through Feature Weight and
Penalty-Based Approach

39

L. H. Li et al. (2025)

Explainable AI-based LightGBM
Prediction Model to Predict Default
Borrower in Social Lending
Platform

Proposes a deep learning framework that injects
interpretability constraints into training via multi-objective
optimization. Uses soft constraints and weighted-sum
scalarization to balance criteria. Demonstrates on the Polish
bankruptcy dataset and visualizes effects using ALE plots,
indicating interpretability-aware training can support
generalization in high-stakes tasks.

RQ1

Proposes feature-weight adjustment, penalty-based
modeling, and a hybrid method to enhance inclusion in
credit scoring. Evaluates inclusivity and performance
across extensive hyperparameter combinations using
XGBoost, CatBoost, RF, and DT. Improves inclusion by
reweighting sensitive features but notes risks of
dataset-specific overfitting and limited generalizability.

RQ1, RQ2

Implements LightGBM with LIME and SHAP for
global/local interpretability in credit scoring. Uses
sampling and RFE to address imbalance and
dimensionality on the Lending Club dataset. Reports strong
predictive performance and provides a reference pipeline
for integrating explainability with ensemble models in
social lending.

RQ1

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 31 -->

J. Risk Financial Manag. 2026, 19, 104

31 of 36

Table A9. Cont.

ID Author(s)

Title

Summary

Related RQs

40 Dastile and Celik (2024)

Counterfactual Explanations with
Multiple Properties in Credit
Scoring

41 Aruleba and Sun (2024)

Effective Credit Risk Prediction
Using Ensemble Classifiers With
Model Explanation

42

Patron et al. (2020)

An Interpretable Automated
Machine Learning Credit Risk
Model

43

C. Li et al. (2024)

The Effect of AI-enabled Credit
Scoring on Financial Inclusion:
Evidence from an Underserved
Population of Over One Million

Appendix C

Proposes a counterfactual explanation method optimizing
validity and sparsity to improve interpretability. Uses GA
and PSO to find minimal feature changes that alter
predictions. Highlights challenges such as drift sensitivity
and missing data, and positions counterfactuals as a
transparent alternative to feature-importance explanations
for auditing.

Presents an ensemble framework (RF, AdaBoost, XGBoost,
LightGBM) with SMOTE-ENN for imbalance correction
and SHAP for interpretation. Evaluated on German and
Australian datasets; reports improved recall/specificity and
argues balanced, explainable ensemble learning improves
generalization and auditability.

RQ1, RQ3

RQ1, RQ2

Proposes an AutoML framework integrating LIME for local
interpretability of complex models. Reports near–deep
learning performance while maintaining transparency
through local perturbation-based explanations, supporting
expert validation and contestability in credit risk decisions.

RQ1

Analyzes AI’s impact on financial inclusion using data from
over one million underserved borrowers. Introduces weak
signals (features weakly tied to financial status) to study
inclusion and bias trade-offs. Warns protected attributes
may amplify discrimination and argues for balanced
adoption to improve access while managing equity risks.

RQ2, RQ3

Table A10. Summary of fairness mitigation strategies in credit scoring (Part 1: Rows 1–6).

Author

Category

Method

Mechanism

Strengths

Limitations

Kozodoi et al.
(2022)

Pre-processing

Reweighing

Kozodoi et al.
(2022)

Pre-processing

Disparate Impact
Remover (DIR)

Kozodoi et al.
(2022)

In-processing

Prejudice Remover
Regularizer (PRR)

Kozodoi et al.
(2022)

In-processing

Adversarial
Debiasing

Kozodoi et al.
(2022)

In-processing

Meta-fair
Classification

Kozodoi et al.
(2022)

Post-processing

Reject Option
Classification (ROC)

Adjusts training sample weights
so disadvantaged groups receive
higher influence during training,
targeting independence (parity).

Transforms feature values to
reduce distribution differences
across protected groups, reducing
dependence on protected
attributes.

Model-agnostic; simple
to apply before training;
can reduce
discrimination at low
implementation cost.

Smaller fairness gains than
the strongest post-
processing option in their
comparison; may require
repeated data-pipeline
adjustments.

Improves fairness
without changing model
architecture;
model-agnostic.

Worse profit–fairness
trade-off than the best
in-processing option (PRR)
in their reported results.

Adds a regularization term to the
training objective that penalizes
unfairness using a prejudice index,
with a tunable penalty weight.

Tunable trade-off;
achieves better profit–
fairness trade-off than
DIR in their evaluation.

Invasive; modifies the
training objective/
scorecards and increases
implementation burden.

Trains a predictor while an auxiliary
adversary tries to infer the protected
attribute; penalizes the predictor
when the adversary succeeds.

Optimizes a classifier under
fairness constraints (e.g.,
independence/separation) with
trade-off meta-parameters
controlling accuracy vs. fairness.

Tunable fairness–profit
balance via
meta-parameters.

Requires retraining and
pipeline changes; more
invasive than
post-processing.

Explicit control over
fairness–accuracy
trade-offs.

Model/training specific;
requires retraining and
integration effort.

Relabels decisions in an
uncertainty region in favor of the
disadvantaged group to improve
group parity.

Strong fairness gains;
largely preserves the
existing scoring
pipeline.

Can reduce profitability
compared to in-processing
approaches; acts only on
the decision boundary.

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 32 -->

J. Risk Financial Manag. 2026, 19, 104

32 of 36

Table A11. Summary of fairness mitigation strategies in credit scoring (Part 2: Rows 7–12).

Author

Category

Method

Mechanism

Strengths

Limitations

Kozodoi et al.
(2022)

Post-processing

Equalized Odds
Post-processing

Uses group-specific thresholds to
equalize error rates across groups
(separation/equalized odds).

Kozodoi et al.
(2022)

Post-processing

Group-wise Platt
Scaling

Calibrates predicted probabilities
per group to satisfy sufficiency (risk
meaning consistent across groups).

Post-hoc; model-agnostic;
can reduce discrimination
at low cost up to a point
on the Pareto frontier.

Strict fairness may
require large
profit/utility sacrifices
across datasets.

Post-hoc; preserves
pipeline; supports
calibration for sufficiency-
oriented compliance.

Inherits post-processing
trade-offs; does not
address upstream bias;
cannot satisfy all criteria
simultaneously.

Moldovan
(2023)

In-processing

GerryFair

Learner–auditor adversarial
approach minimizing unfairness
via iterative constraint enforcement
(targets individual fairness).

Explicitly targets
individual-level
unfairness, not only
group parity.

Hard to tune; may overfit
on small credit datasets.

Moldovan
(2023)

In-processing

Grid Search
Reduction

Zehlike et al.
(2025)

Post-processing

FAIM

Reformulates learning as a
cost-sensitive reduction and
searches constraint weights to
obtain fairness–accuracy trade-offs.

Optimal-transport interpolation
between incompatible fairness
criteria (calibration, balance for
positives, balance for negatives)
using weighted constraints.

Valdrighi et al.
(2025)

In-processing

Demographic
Parity/Equal
Opportunity
Classifier

Modifies LR training to minimize
loss subject to a correlation constraint
between predictions and sensitive
attributes (tunable constant).

Allows explicit
exploration and selection
of trade-off points.

Accuracy may degrade
sharply under strict
constraints.

Provides a tunable
mechanism to navigate
incompatibility between
fairness criteria.

Simple and interpretable;
tunable trade-off.

Weight selection embeds
normative/legal
judgment; may not
match a single regulatory
interpretation.

Requires sensitive
attributes during training;
remains a trade-off rather
than a guarantee.

Table A12. Summary of fairness mitigation strategies in credit scoring (Part 3: Rows 13–18).

Author

Category

Method

Mechanism

Strengths

Limitations

Valdrighi et al.
(2025)

In-processing

FairGBM
(constrained
gradient boosting)

Alters boosting to jointly minimize
prediction loss and a differentiable
proxy of a fairness metric (e.g.,
DP/EO) during training.

Strong tabular
performance with
embedded fairness
control using constrained
learning.

Model-class specific;
depends on proxy
design and
differentiability of
fairness objectives.

Valdrighi et al.
(2025)

Post-processing

Threshold
Optimizer

Builds separate ROC curves per
group and selects thresholds that
minimize loss within the feasible fair
region, yielding group-specific
thresholds.

Consistently reaches
fairness targets with
minimum accuracy loss
in their comparisons.

Valdrighi et al.
(2025)

Post-processing
(general)

Position on
post-processing
(general)

Alters outputs of black-box models
to satisfy fairness constraints (e.g.,
group thresholds) without changing
model training.

Versatile and suitable for
black-boxes and fixed
scorecards.

S. Liu and
Vicente (2022)

In-processing

Stochastic
Multi-Gradient
(SMG) bi-objective
optimization

Badar and
Fisichella (2024)

Hybrid

Fair-CMNB

S. Han et al.
(2024)

Pre-processing
(oversampling)

NOTE

Frames fairness as stochastic
multi-objective optimization and
aggregates gradients of prediction loss
and fairness penalty along the Pareto
frontier (e.g., DI/EO constraints).

Stream-learning Mixed Naïve Bayes
with multi-objective optimization;
dynamic instance weighting for
imbalance and discrimination
control (targets Statistical Parity;
uses causal fairness via ATE/FACE).

Non-parametric stacked
autoencoders to learn latent
structure, then conditional
Wasserstein GAN oversampling for
mixed categorical/
numerical features.

Requires sensitive
attributes at prediction
time, which may be
legally/practically
constrained.

Less tunable than
in-processing; may
yield weaker
improvements relative
to pre-/in-processing.

Not reported (explicit
method-level
limitations not stated
beyond general
trade-offs).

Produces smooth Pareto
frontiers and stable
convergence across
fairness constraints.

Low discrimination (SP
near 0) while improving
accuracy relative to
baselines; supports
streaming settings.

Does not guarantee
global fairness across
settings; gains are
dataset-dependent.

Stronger performance
than classic
oversampling (e.g.,
SMOTE) in their
comparisons.

Not reported.

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 33 -->

J. Risk Financial Manag. 2026, 19, 104

33 of 36

Table A13. Summary of fairness mitigation strategies in credit scoring (Part 4: Rows 19–21).

Author

Category

Method

Mechanism

Strengths

Limitations

Kozodoi et al.
(2025)

Pre-processing
(bias-aware
rejection
inference)

BASL: Bias-Aware
Self-Learning

Chai et al.
(2025)

Pre-processing

ADASYN-LCE

Hartomo
et al. (2025)

In-processing

Weighted
TabTransformer

Semi-supervised approach that
iteratively infers labels for
rejected/unlabeled instances to
reduce sampling bias and improve
training representativeness.

Combines ADASYN oversampling
with a Local Cascading Ensemble
(bagging/boosting/local
cascading) to improve robustness
for underserved populations under
imbalance.

Integrates a weighted
cross-entropy objective into
TabTransformer to give larger
gradients to minority classes.

Outperforms parceling,
reweighting, and
Heckman-style correction;
recovers a substantial
share of predictive loss
attributed to sampling bias
in their case study.

Not reported.

Improves generalization
under imbalance; LCE
balances bias–variance
across subsets of the data.

May struggle to address
bias and variance
simultaneously under
some conditions (as
noted by the authors).

Supports joint
improvements in
performance under
imbalance and
fairness-related objectives
in their framing.

Prone to overfitting if
weighting is
mis-specified.

References

Adegoke, T., Ofodile, O., Ochuba, N., & Akinrinol, O. (2024). Evaluating the fairness of credit scoring models: A literature review on

mortgage accessibility for under-reserved populations. GSC Advanced Research and Reviews, 18(3), 189–199. [CrossRef]

Ali Shahee, S., & Patel, R. (2025). An explainable ADASYN-based focal loss approach for credit assessment. Journal of Forecasting, 44,

1513–1530. [CrossRef]

Alufaisan, Y., Marusich, L. R., Bakdash, J. Z., Zhou, Y., & Kantarcioglu, M. (2021). Does explainable artificial intelligence improve
human decision-making? In Proceedings of the AAAI conference on artificial intelligence (Vol. 35, pp. 6618–6626). AAAI Press.
[CrossRef]

Alves, G., Bernier, F., Couceiro, M., Makhlouf, K., Palamidessi, C., & Zhioua, S. (2023). Survey on fairness notions and related tensions.

EURO Journal on Decision Processes, 11, 100033. [CrossRef]

Amekoe, K. M., Azzag, H., Dagdia, Z. C., Lebbah, M., & Jaffre, G. (2024). Exploring accuracy and interpretability trade-off in tabular

learning with novel attention-based models. Neural Computing and Applications, 36(30), 18583–18611. [CrossRef]

Aruleba, I., & Sun, Y. (2024). Effective credit risk prediction using ensemble classifiers with model explanation. IEEE Access, 12,

115015–115025. [CrossRef]

Atif, D. (2025). VAE-INN: Variational autoencoder with integrated neural network classifier for imbalanced credit scoring, utilizing

weighted loss for improved accuracy. Computational Economics. [CrossRef]

Badar, M., & Fisichella, M. (2024). Fair-CMNB: Advancing fairness-aware stream learning with naïve bayes and multi-objective

optimization. Big Data and Cognitive Computing, 8(2), 16. [CrossRef]

Balashankar, A., & Lees, A. (2022). The need for transparent demographic group trade-offs in credit risk and income classification. In

Proceedings of the international conference on information (pp. 344–354). Springer International Publishing.

Bartlett, R., Morse, A., Stanton, R., & Wallace, N. (2022). Consumer-lending discrimination in the FinTech era. Journal of Financial

Economics, 143(1), 30–56. [CrossRef]

Basel Committee on Banking Supervision. (2013). Principles for effective risk data aggregation and risk reporting (Technical report no. 8, Basel
committee publication no. 239). Bank for International Settlements. Available online: https://www.bis.org/publ/bcbs239.htm
(accessed on 30 September 2025).

Berg, T., Burg, V., Gombovi´c, A., & Puri, M. (2020). On the rise of Fintechs: Credit scoring using digital footprints. The Review of

Financial Studies, 33(7), 2845–2897. [CrossRef]

Brzezinski, D., Stachowiak, J., Stefanowski, J., Szczech, I., Susmaga, R., Aksenyuk, S., & Yasinskyi, O. (2024). Properties of fairness
measures in the context of varying class imbalance and protected group ratios. ACM Transactions on Knowledge Discovery from
Data, 18(7), 1–18. [CrossRef]

Bueff, A. C., Cytry ´nski, M., Calabrese, R., Jones, M., Roberts, J., Moore, J., & Brown, I. (2022). Machine learning interpretability for a

stress scenario generation in credit scoring based on counterfactuals. Expert Systems with Applications, 202, 117271. [CrossRef]

Bulut, C., & Arslan, E. (2025). A hybrid approach to credit risk assessment using bill payment habits data and explainable artificial

intelligence. Applied Sciences, 15(10), 5723. [CrossRef]

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 34 -->

J. Risk Financial Manag. 2026, 19, 104

34 of 36

Bücker, M., Szepannek, G., Gosiewska, A., & Biecek, P. (2022). Transparency, auditability, and explainability of machine learning

models in credit scoring. Journal of the Operational Research Society, 73(1), 70–90. [CrossRef]

Cao, W., He, Y., Wang, W., Zhu, W., & Demazeau, Y. (2021). Ensemble methods for credit scoring of chinese peer-to-peer loans. Journal

of Credit Risk, 17, 79–115. [CrossRef]

Caton, S., & Haas, C. (2024). Fairness in machine learning: A survey. ACM Computing Surveys, 56(7), 1–38. [CrossRef]
Chacko, A., & Aravindhar, D. J. (2025, February 21–22). Enhancing fairness and accuracy in credit score analysis: A novel framework
utilizing kernel PCA. 2025 International Conference on Information Technology, Innovation and Intelligent Systems (ICITIIT),
Kottayam, India. [CrossRef]

Chai, N., Abedin, M. Z., Yang, L., & Shi, B. (2025). Farmers’ credit risk evaluation with an explainable hybrid ensemble approach: A

closer look in microfinance. Pacific-Basin Finance Journal, 89, 102612. [CrossRef]

Chen, Y., Calabrese, R., & Martin-Barragán, B. (2024). Interpretable machine learning for imbalanced credit scoring datasets. European

Journal of Operational Research, 312(1), 357–372. [CrossRef]

Cornacchia, G., Anelli, V. W., Narducci, F., Ragone, A., & Di Sciascio, E. (2023). A general architecture for a trustworthy creditworthiness-

assessment platform in the financial domain. AETiC, 7, 56–64. [CrossRef]

Corrales-Barquero, R., Marín-Raventós, G., & Barrantes, E. G. (2021, October 27–28). A review of gender bias mitigation in credit scoring
models. 2021 International Conference on Electrical, Electronics and Related Data Science (EE-RDS), Johannesburg, South Africa.
[CrossRef]

C-Rella, J., Martínez-Rego, D., & Vilar Fernández, J. M. (2025). Cost-sensitive reinforcement learning for credit risk. Expert Systems with

Applications, 272, 126708. [CrossRef]

Das, S., Stanton, R., & Wallace, N. (2023). Algorithmic fairness. Annual Review of Financial Economics, 15(1), 565–593. [CrossRef]
Dastile, X., & Celik, T. (2024). Counterfactual explanations with multiple properties in credit scoring. IEEE Access, 12, 110713–110728.

[CrossRef]

Dastile, X., Celik, T., & Vandierendonck, H. (2022). Model-agnostic counterfactual explanations in credit scoring. IEEE Access, 10,

69543–69554. [CrossRef]

de Castro Vieira, J. R., Barboza, F. L. D. M., Cajueiro, D. O., & Kimura, H. (2025). Towards fair AI: Mitigating bias in credit decisions—A

systematic literature review. Journal of Risk and Financial Management, 18, 228. [CrossRef]

Dessain, J., Bentaleb, N., & Viñas, F. (2023). Cost of explainability in AI: An example with credit scoring models. In Proceedings of the

world conference on explainable artificial intelligence (pp. 498–516). Springer Nature. [CrossRef]

European Central Bank. (2024). Supervisory guide on risk data aggregation and risk reporting (Technical report, supervisory guide).
European Central Bank, Banking Supervision. Available online: https://www.bankingsupervision.europa.eu/ecb/pub/pdf/
ssm.supervisory_guides240503_riskreporting.en.pdf (accessed on 30 September 2025).

Goethals, S., Martens, D., & Calders, T. (2024). Precof: Counterfactual explanations for fairness. Machine Learning, 113(5), 3111–3142.

[CrossRef]

Griffith, M. A. (2023). AI lending and the ECOA: Avoiding accidental discrimination. North Carolina Banking Institute, 27, 349–381.

Available online: https://scholarship.law.unc.edu/ncbi/vol27/iss1/16 (accessed on 30 September 2025).

Han, S., Jung, H., Yoo, P. D., Provetti, A., & Calì, A. (2024). NOTE: Non-parametric oversampling technique for explainable credit

scoring. Scientific Reports, 14(1), 26070. [CrossRef]

Han, W., Gu, X., & Jian, L. (2023). A multi-layer multi-view stacking model for credit risk assessment. Intelligent Data Analysis, 27(5),

1457–1475. [CrossRef]

Hartomo, K. D., Arthur, C., & Nataliani, Y. (2025). A novel weighted loss tabtransformer integrating explainable AI for imbalanced

credit risk datasets. IEEE Access, 13, 31045–31056. [CrossRef]

Hickey, J. M., Di Stefano, P. G., & Vasileiou, V. (2020). Fairness by explicability and adversarial SHAP learning. In Joint European
conference on machine learning and knowledge discovery in databases (ECML PKDD) (pp. 174–190). Springer International Publishing.
Hjelkrem, L. O., & Lange, P. E. D. (2023). Explaining deep learning models for credit scoring with textual transaction data. Journal of

Risk and Financial Management, 16(4), 221. [CrossRef]

Hlongwane, R., Ramabao, K., & Mongwe, W. (2024). A novel framework for enhancing transparency in credit scoring: Leveraging

Shapley values for interpretable credit scorecards. PLoS ONE, 19(8), e0308718. [CrossRef] [PubMed]

Hurlin, C., Pérignon, C., & Saurin, S. (2024). The fairness of credit scoring models. Management Science, 70(11), 1234–1256. [CrossRef]
Jiang, Y., Fang, X., & Wang, Z. (2024). Disparity and discrimination in consumer credit markets: Evidence from online peer-to-peer

lending. Pacific-Basin Finance Journal, 83, 102237. [CrossRef]

Kanaparthi, V. (2023, April 26–28). Credit risk prediction using ensemble machine learning algorithms. 2023 International Conference on

Inventive Computation Technologies (ICICT) (pp. 41–47), Lalitpur, Nepal. [CrossRef]

Keele, S. (2007). Guidelines for performing systematic literature reviews in software engineering (EBSE technical report, version 2.3). Available

online: https://www.elsevier.com/__data/promis_misc/525444systematicreviewsguide.pdf (accessed on 17 October 2025).

Koulu, R. (2020). Human control over automation: EU policy and AI ethics. European Journal of Legal Studies, 12, 9–46. [CrossRef]

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 35 -->

J. Risk Financial Manag. 2026, 19, 104

35 of 36

Kozodoi, N., Jacob, J., & Lessmann, S. (2022). Fairness in credit scoring: Assessment, implementation and profit implications. European

Journal of Operational Research, 297(3), 1083–1094. [CrossRef]

Kozodoi, N., Lessmann, S., Alamgir, M., Moreira-Matias, L., & Papakonstantinou, K. (2025). Fighting sampling bias: A framework for

training and evaluating credit scoring models. European Journal of Operational Research, 324(2), 616–628. [CrossRef]

Kuiper, O., van den Berg, M., van der Burgt, J., & Leijnen, S. (2021). Exploring explainable AI in the financial sector: Perspectives
of banks and supervisory authorities. In Proceedings of the benelux conference on artificial intelligence (pp. 105–119). Springer
International Publishing.

Kumar, I. E., Hines, K. E., & Dickerson, J. P. (2022). Equalizing credit opportunity in algorithms: Aligning algorithmic fairness research
with US fair lending regulation. In Proceedings of the 2022 AAAI/ACM conference on AI, ethics, and society (pp. 357–368). Association
for Computing Machinery. [CrossRef]

Lainez, N., & Gardner, J. (2023). Algorithmic credit scoring in Vietnam: A legal proposal for maximizing benefits and minimizing risks.

Asian Journal of Law and Society, 10(3), 401–432. [CrossRef]

Langenbucher, K. (2020). Responsible AI-based credit scoring—A legal framework. European Business Law Review, 31(4), 527–572.

[CrossRef]

Langenbucher, K., & Corcoran, P. (2022). Responsible AI credit scoring—A lesson from upstart.com. In Digital finance in Europe: Law,

regulation, and governance. De Gruyter.

Li, C., Wang, H., Jiang, S., & Gu, B. (2024). The effect of AI-enabled credit scoring on financial inclusion: Evidence from an underserved

population of over one million. MIS Quarterly, 48(4), 1803–1834. [CrossRef]

Li, L. H., Sharma, A. K., & Cheng, S. T. (2025). Explainable AI based LightGBM prediction model to predict default borrower in social

lending platform. Intelligent Systems with Applications, 26, 200514. [CrossRef]

Li, W., Paraschiv, F., & Sermpinis, G. S. (2022). A data-driven explainable case-based reasoning approach for financial risk detection.

Quantitative Finance, 22, 2257–2274. [CrossRef]

Li, Y., Wang, X., Djehiche, B., & Hu, X. (2020). Credit scoring by incorporating dynamic networked information. European Journal of

Operational Research, 286(3), 1103–1112. [CrossRef]

Li, Z., Hu, X., Li, K., Zhou, F., & Shen, F. (2020). Inferring the outcomes of rejected loans: An application of semisupervised clustering.

Journal of the Royal Statistical Society: Series A, 183, 631–654. [CrossRef]

Liao, J., Wang, W., Xue, J., Lei, A., Han, X., & Lu, K. (2022). Combating sampling bias: A self-training method in credit risk models.

Proceedings of the AAAI Conference on Artificial Intelligence, 36, 12566–12572. [CrossRef]

Liu, J., Zhang, X., & Xiong, H. (2024). Credit risk prediction based on causal machine learning: Bayesian network learning, default

inference, and interpretation. Journal of Forecasting, 43(5), 1625–1660. [CrossRef]

Liu, S., & Vicente, L. N. (2022). Accuracy and fairness trade-offs in machine learning: A stochastic multi-objective approach.

Computational Management Science, 19(3), 513–537. [CrossRef]

Martinez, N., Bertran, M., & Sapiro, G. (2020, July 13–18). Minimax pareto fairness: A multi-objective perspective. International Conference

on Machine Learning (ICML) (pp. 6755–6764), Virtual.

Mestiri, S., & Hiboun, S. M. (2024). Credit scoring using machine learning and deep learning-based models. Data Science in Finance and

Economics, 4(2), 236–248. [CrossRef]

Moher, D., Liberati, A., Tetzlaff, J., Altman, D. G., & Group, P. (2010). Preferred reporting items for systematic reviews and meta-analyses:

The PRISMA statement. International Journal of Surgery, 8(5), 336–341. [CrossRef]

Moldovan, D. (2023). Algorithmic decision making methods for fair credit scoring. IEEE Access, 11, 59729–59743. [CrossRef]
Mou, Y., Pu, Z., Feng, D., Luo, Y., Lai, Y., Huang, J., Tian, Y., & Xiao, F. (2025). Cost-aware credit-scoring framework based on resampling

and feature selection. Computational Economics, 66, 3007–3032. [CrossRef]

Muñoz-Cancino, R., Bravo, C., Ríos, S. A., & Graña, M. (2023). On the dynamics of credit history and social interaction features, and

their impact on creditworthiness assessment performance. Expert Systems with Applications, 218, 119599. [CrossRef]

Nwafor, C. N., Nwafor, O., & Brahma, S. (2024). Enhancing transparency and fairness in automated credit decisions: An explainable

novel hybrid machine learning approach. Scientific Reports, 14(1), 25174. [CrossRef]

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan,
S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., &
Moher, D. (2021). Updating guidance for reporting systematic reviews: Development of the PRISMA 2020 statement. Journal of
Clinical Epidemiology, 134, 103–112. [CrossRef]

Patron, G., Leon, D., Lopez, E., & Hernandez, G. (2020). An interpretable automated machine learning credit risk model. In Workshop

on engineering applications (pp. 16–23). Springer International Publishing.

Peng, Z., Mo, W., Duan, C., Li, Q., & Zhou, B. (2023). Learning from active human involvement through proxy value propagation. In
Proceedings of the 37th conference on neural information processing systems (NeurIPS 2023). Curran Associates, Inc. Available online:
https://metadriverse.github.io/pvp (accessed on 17 October 2025).

https://doi.org/10.3390/jrfm19020104

---

<!-- PAGE 36 -->

J. Risk Financial Manag. 2026, 19, 104

36 of 36

Perry, V. G., Martin, K., & Schnare, A. (2023). Algorithms for all: Can AI in the mortgage market expand access to homeownership? AI,

4(4), 888–903. [CrossRef]

Ratul, Q. E. A., Serra, E., & Cuzzocrea, A. (2021, December 15–18). Evaluating attribution methods in machine learning interpretability. 2021

IEEE International Conference on Big Data (Big Data) (pp. 5239–5245), Orlando, FL, USA.

Repetto, M. (2025). Multicriteria interpretability driven deep learning. Annals of Operations Research, 346(2), 1621–1635. [CrossRef]
Ribeiro-Flucht, L., Chen, X., & Meurers, D. (2024). Explainable AI in language learning: Linking empirical evidence and theoretical
concepts in proficiency and readability modeling of portuguese. In Proceedings of the 19th workshop on innovative use of NLP
for building educational applications (BEA 2024) (pp. 199–209). Association for Computational Linguistics. Available online:
https://aclanthology.org/2024.bea-1.17 (accessed on 4 October 2025).

Ridzuan, N. N., Masri, M., Anshari, M., Fitriyani, N. L., & Syafrudin, M. (2024). AI in the financial sector: The line between innovation,

regulation and ethical responsibility. Information, 15(8), 432. [CrossRef]

Roa, L., Correa-Bahnsen, A., Suarez, G., Cortés-Tejada, F., Luque, M. A., & Bravo, C. (2021). Super-app behavioral patterns in credit risk

models: Financial, statistical and regulatory implications. Expert Systems with Applications, 169, 114486. [CrossRef]

Shi, X., Tang, D., & Yu, Y. (2025). Credit scoring prediction using deep learning models in the financial sector. IEEE Access, 13,

130731–130746. [CrossRef]

Sulastri, R., Ding, A. Y., & Janssen, M. (2025, June 18–20). Sensitivity analysis: Improving inclusive credit scoring algorithm through feature
weight and penalty-based approach. 2025 Eleventh International Conference on Edemocracy & Egovernment (ICEDEG) (pp. 54–61),
Bern, Switzerland. [CrossRef]

Talaat, F. M., Aljadani, A., Badawy, M., & Elhosseini, M. (2024). Toward interpretable credit scoring: Integrating explainable artificial
intelligence with deep learning for credit card default prediction. Neural Computing and Applications, 36(9), 4847–4865. [CrossRef]
Tiukhova, E., Salcuni, A., Oguz, C., Niglio, M., Storti, G., Forte, F., Baesens, B. M., & Snoeck, M. (2025). Boosting credit risk data quality
using machine learning and eXplainable AI techniques. In Machine learning and principles and practice of knowledge discovery in
databases. Springer. [CrossRef]

Valdrighi, G., Ribeiro, A. M., Pereira, J. S. B., Guardieiro, V., Hendricks, A., Miranda Filho, D., & Medeiros Raimundo, M. (2025). Best
practices for responsible machine learning in credit scoring. Neural Computing and Applications, 37, 20781–20821. [CrossRef]
Vukovi´c, D. B., Dekpo-Adza, S., & Matovi´c, S. (2025). AI integration in financial services: A systematic review of trends and regulatory

challenges. Humanities and Social Sciences Communications, 12, 562. [CrossRef]

Wang, W., Lesner, C., Ran, A., Rukonic, M., Xue, J., & Shiu, E. (2020). Using small business banking data for explainable credit risk

scoring. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 34, pp. 13396–13401). AAAI Press. [CrossRef]

Wu, Z., Dong, Y., Li, Y., & Liu, Y. (2025). A ‘Divide and Conquer’ reject inference approach leveraging graph-based semi-supervised

learning. Annals of Operations Research. [CrossRef]

Xie, W., He, J., Huang, F., & Ren, J. (2025). Operational risk assessment of commercial banks’ supply chain finance. Systems, 13(2), 76.

[CrossRef]

Zacharias, J., von Zahn, M., Chen, J., & Hinz, O. (2022). Designing a feature selection method based on explainable artificial intelligence.

Electronic Markets, 32, 2159–2184. [CrossRef]

Zehlike, M., Loosley, A., Jonsson, H., Wiedemann, E., & Hacker, P. (2025). Beyond incompatibility: Trade-offs between mutually

exclusive fairness criteria in machine learning and law. Artificial Intelligence, 340, 104280. [CrossRef]

Zhang, R., Li, I., & Ding, Z. (2025). An Interpretable credit risk assessment model with boundary sample identification. PeerJ Computer

Science, 11, e2988. [CrossRef] [PubMed]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

https://doi.org/10.3390/jrfm19020104

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

SystematicReview
Performance, Fairness, and Explainability in AI-Based Credit
Scoring: A Systematic Literature Review
RashedBahlool* ,NabilHewahi andWaelElmedany
CollegeofInformationTechnology,UniversityofBahrain,SakhirCampus,Zallaq1054,Bahrain;
nhewahi@uob.edu.bh(N.H.);welmedany@uob.edu.bh(W.E.)
* Correspondence:20083051@stu.uob.edu.bh
Abstract
Theintegrationofartificialintelligence(AI)inthefinancialsectorhasseenarapidincrease
overthepastfewyears,offeringnewpossibilitiestostreamlineprocesseswhileensuring
profitabilityforlendinginstitutions. Withitsdata-drivencapability,predictingthecred-
itworthinessofapplicantshasdemonstratedstrongpredictiveperformance,particularly
for thin-file clients. Despite these advances, growing concerns regarding AI’s fairness,
explainability,andregulatoryaccountabilityhaveincreasinglylimiteditsadoptioninhigh-
stakescreditdecision-making. Thispaperpresentsasynthesisderivedfromasystematic
literature review (SLR) of 43 peer-reviewed studies published between 2020 and 2025,
focusingonAI-basedcreditscoringandaddressingatleastoneoftheperformance,fair-
ness,orexplainabilitydimensions. Eligiblestudieswerelimitedtopeer-reviewedjournal
andconferencearticles(2020–2025)retrievedfromIEEEXplore,Scopus,WebofScience,
andScienceDirect(lastsearched: 30September), examiningAI-drivencreditscoringin
consumerorlendingdecisioncontexts. GuidedbytheRelevance,Rigor,Reproducibility,
andQuality(3Rs&Q)appraisalframework,thereviewanalyzeshowexistingapproaches
navigatetheinterplayamongperformance,fairness,andexplainabilityunderregulatory
and human oversight considerations. The findings indicate that these dimensions are
predominantly addressed in isolation, with limited attention to their joint treatment in
regulateddeploymentsettings. Byconsolidatingempiricalandconceptualevidence,this
reviewprovidesactionableguidancefordesigninganddeployingcreditscoringmodels
inpractice.
Keywords: creditscoring;explainableAI;algorithmicfairness;AIgovernance;regulatory
compliance
1. Introduction
AcademicEditor:ThanasisStengos Inthecontinuedpursuitofnationwideeconomicgrowth,financialinstitutionsprovide
consumerfacilitiesasoneoftheircorebusinessfunctions. Creditscoringplaysapivotal
Received:12January2026
Revised:26January2026 roleindecidingwhetheraloanshouldbegrantedtoanapplicant, wherebyapplicants
Accepted:29January2026 undergo a rigorous risk assessment process to evaluate their financial stability prior to
Published:3February2026 approvingthefacility(Adegokeetal.,2024). Theproblemofassessingthecreditworthiness
Copyright:©2026bytheauthors. ofloanapplicantsisoneriskexposureforlendinginstitutions,amongotherrisksources
LicenseeMDPI,Basel,Switzerland.
that organizations must address. If not properly evaluated, the likelihood of financial
Thisarticleisanopenaccessarticle
loss increases due to higher loan default rates, ultimately putting financial institutions
distributedunderthetermsand
atrisk(Xieetal.,2025). Incontrast,successfullydistinguishingbetweendefaultersand
conditionsoftheCreativeCommons
Attribution(CCBY)license.
J.RiskFinancialManag.2026,19,104 https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 2of36
non-defaulterswouldensureprofitabilityfortheinstitution. Commoncreditriskassess-
mentsincludeapplicationandbehavioralcreditscoring,withotherassessments,suchas
collection,fraud,andcreditrenewal,alsocoexisting(Muñoz-Cancinoetal.,2023). These
riskassessmentshavebeenextensivelyrelieduponbyfinancialinstitutionstominimize
potentiallossesacrosstheirproductlines. Theyenableinstitutionstoquantify,monitor,
andmitigateassociatedrisks,dependingonthetypeofsituationalinputsandregulatory
mandates(BaselCommitteeonBankingSupervision,2013;EuropeanCentralBank,2024).
Application and behavioral scoring differ substantially in the timing of the credit-
worthiness assessment. On one hand, application scoring aims to assess the eligibility
of applicants prior to receiving the loan (Berg et al., 2020). To perform the assessment,
customersmustundergoarigorousprocessknownasKnowYourCustomer(KYC),which
mandatesthatlendinginstitutionscapturepersonalandrepaymentrecords,oftenretrieved
from national credit bureaus (Mestiri & Hiboun, 2024). The data include demographic
information,loanrepaymentbehavior,andcreditbureaudatashowingoutstandingdebts
andothercreditinquiries,alldeemednecessarytoensureadata-drivenassessmentofcred-
itworthiness. Ontheotherhand,behavioralscoringisanongoingandperiodicevaluation
procedureusedtoassessthecreditbehaviorofexistingcustomers, therebymonitoring
riskintheactiveportfolioofaninstitution(Y.Lietal.,2020). Itreliesonasubsetofthe
informationusedinapplicationscoring,suchaspaymenthistoryandarrearspatterns,and
offersearlysignsofdefaultforproactiveinterventions. Withthesetwoscoringmethodsin
mind,financialinstitutionscantakepreventivemeasureswithapplicantswhoarelikelyto
defaultontheirloans. Together,bothmethodsenableafullcreditlife-cyclemanagement
strategythatensurestheapprovalofeligiblecustomersandtheongoingmonitoringof
repaymentbehavior(Roaetal.,2021).
Beyondinstitutionalrisk,theimplicationofdecisionsmadebycreditscoringextends
tocoversocioeconomicfactors,includingfinancialinclusionandexclusion,wealthdistri-
bution,equity,andsocietalwell-being(Bartlettetal.,2022). Theseconsequencesweigh
heavilyonfinancialinstitutionsand,ifnotaddressed,resultinexclusionarypracticesthat
adverselyaffectunderservedpopulations. Individualsorentitieswithaccesstocreditcan
contributetosocialmobility,whileunfaircreditscoringcanleadtoinequalitiesandlimited
opportunitiesforminoritygroups. Theconsequencesoflendingdecisionshavelongbeen
theinterestofresearchers,mainlyduetotheiradverseimpactuponfundamentalhuman
rights(Jiangetal.,2024). Regardlessofwhethertheoutcomesareintentionalordrivenby
algorithmicdetermination,ofteninfluencedbyhumanbiasintheformofbiasedhistorical
data,itisestimatedthat1.3millionmortgageloansarerejectedintheUnitedStates,mainly
duetodiscrimination(Bartlettetal.,2022). Consequently,minoritygroups,classifiedbased
on gender, ethnicity, religion, or nationality, are more vulnerable to rejection, or in the
best-case scenario, pay higher interest rates. In the long term, this could lead to unfair
wealthaccumulationandthereforeperpetuategenerationalpoverty.
Thesocioeconomicfactorsinvolvedincreditscoringwerekeymotivationsforregula-
torstostepin,ensuringethicalpracticesandproperoversightofthelendingprocess. Asa
result,countriessuchastheUSandtheEuropeanUnionhavepassedtheEqualCreditOp-
portunityAct(ECOA)andtheEUCharterofFundamentalRights,respectively,toprohibit
discriminatorylendingactsagainstpersonalcharacteristics(Griffith,2023). Theseprotec-
tionsincluderace,gender,nationalorigin,andmaritalstatus,and,moreimportantly,they
emphasizethatlendinginstitutionsmustrelysolelyonfinancialandapplicationattributes.
These laws have emerged with the intent to foster transparency in the lending process
andreducemistrustinthefinancialsystemthat,whenundermined,potentiallyleadsto
socialandpoliticalbacklashes. Fromariskmanagementperspective,failuresinfairnessor
explainabilitytranslatedirectlyintoregulatory,legal,andreputationalrisksforlending
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 3of36
institutions. Consideringthelong-standingethicalconcernsincreditscoringandtheircom-
plexrelationtosocietalandeconomicvectors,creditscoringefficiencydoesnotmerelyseek
toimprovelendingdecisionperformance,butalsoaccountsforthebroaderconsequences
ofsociallyandethicallyinadequatedecision-making(Chenetal.,2024;Kumaretal.,2022;
Talaatetal.,2024). Havingsaidthat,despitemanyeffortstocombatbiaseddecisionsin
algorithmicscoring,thereisnoconsensusonauniversalfairnessmodelthatiscompatible
acrossalljurisdictionalsettings,consideringalsothatthedefinitionoffairnessvariesacross
differentnotionsoffairness(Alvesetal.,2023;Caton&Haas,2024;Goethalsetal.,2024).
Giventhatfairnessiscrucialincreditscoringpractices,explainabilityiscentraland
enableskeystakeholderstointerpretandcomprehendmodeloutputs,providingthemwith
arationalebehindparticularoutcomes(Wangetal.,2020). Itallowscomplianceofficers
toquestionandcorrectpotentiallydiscriminatorydecisionpatterns,invitingintervention
whenbiaseddecisionsarise,therebysupportingresponsibleandethicaladoptionofAI
(Valdrighietal.,2025). Explainabilityalsohelpsensurealignmentwithlocalregulations,
AIethicsanddataprivacyguidelinesbyallowinglenderstorespondtoauditsandjustify
rejectedapplicationsmoretransparently(Hlongwaneetal.,2024). However,asAImod-
elsbecomemoresophisticatedandcapableofachievingrecord-breakingprecisionand
accuracy,theirperformanceoftencomesatthecostofexplainability(Dessainetal.,2023),
resemblinganotabletensionbetweenmodelperformanceandtransparency.
Despitealltheadvancementsmadeacrossthethreedimensions—performance,fair-
ness,andexplainability—thecurrentresearchontheapplicationofAItosolvethecredit
scoringproblemremainsfragmented. Acrossthereviewedliterature,thesedimensionsare
mostoftenaddressedinisolationratherthantreatedasjointlyoptimizedobjectives. The
existingliteratureoftenemphasizesonepillarattheexpenseofothers,resultinginmodels
that are highly predictive but lack transparency, underperforming but inherently inter-
pretable,orfairbutoperationallyinconsistentwithregulatorymandates. Moreimportantly,
theinteractionsamongthesethreepillars,togetherwithregulatorycompliance,remain
underexplored,leavinguncertaintyaroundhowfairnesscanbepracticallyimplemented
withoutcompromisingperformanceorinterpretability. InrelationtoexistingSLRs,this
reviewextendspriorworkbyexplicitlyexaminingtheintersectionsbetweenperformance,
fairness,andexplainabilityinAI-basedcreditscoring,ratherthansynthesizingthesedi-
mensionsinisolation. Thisintersection-orientedsynthesisyieldsnewinsightsintohow
thesepillarsinteractinpractice,wheretrade-offsareempiricallyquantified,andwhich
methodologicalandregulatoryconstraintsremainunder-addressedindeployablecredit
decisionpipelines.
In light of that, this study has three core objectives: (i) to systematically survey
AI-basedcreditscoringresearchpublishedbetween2020and2025; (ii)toexaminehow
existing approaches address predictive performance, interpretability, and fairness; and
(iii)toidentifymethodologicalandregulatorygapsthatinfluencethepracticaldeployment
ofresponsiblecreditscoringmodels. Byconsolidatingevidenceacrossthesedimensions,
thisreviewcontributesagovernance-orientedsynthesisofAI-basedcreditscoringresearch
that clarifies existing trade-offs and highlights gaps relevant to regulated deployment.
The remainder of this work is structured as follows. Section 2 outlines the systematic
literaturereview(SLR)methodology,detailingthesearchstrategy,selectioncriteria,and
datasynthesisprocessusedtoensurearigorousandscientificallyadequateinvestigation
ofthecurrentstateofknowledge. Section3presentstheresultsoftheSLRsearchthatalign
withtheresearchobjectivesandoutlinestheselectionandassessmentcriteria. Section4
provides a synthesis of the findings to answer the research questions comprehensively
acrossalldimensionsdiscussedearlier. Finally,Section5concludesbyidentifyingcurrent
researchgapsandoutliningdirectionsforfuturework.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 4of36
2. Methodology
To ensure a comprehensive and unbiased survey of key elements reported in the
literature, the SLR protocol was strictly followed to generate the synthesis while main-
tainingtransparencyandreproducibilityoftheresults. ThePreferredReportingItemsfor
SystematicReviewsandMeta-Analyses(PRISMA)framework(Moheretal.,2010)was
adoptedtorecordtheresearchelements,includingtheidentification,screening,inclusion,
andexclusionofresearchpapers. Thissystematicliteraturereviewwasconductedand
reportedinaccordancewiththePRISMA2020guidelines(Pageetal.,2021). Thereview
protocolwasnotregisteredinPROSPEROoranyotherpublicregistry.
Tocomplywiththereviewprotocol,theprocessconsistedofseveralphases,begin-
ningwiththeformulationofresearchquestionsandconcludingwiththeidentification
ofmethodologicalpatterns. Withinthissystematicprocess, anexplicitsearchplanwas
constructedtolocatepotentiallyrelevantstudiesmadeavailableinpublicdatabases. This
step ensures that the evidence base is comprehensive and not selectively gathered. To
guideandrefinethesearchpriortothein-depthreading,explicitinclusionandexclusion
criteriaweredefinedtodeterminewhichstudiestoincludeandwhichtodiscard. Subse-
quently,forstudiesthatpassedtheselectioncriteria,structuredextractionwasperformed
tocollectkeyvariablessuchasmethodsusedforexplainability,fairnessconsiderations,
orregulatoryaspects. Thesedatawerelaterorganizedinapredefinedschema,allowing
consistentcomparisonandtaggingacrossdifferentpapers. Theextractedinformationwas
later synthesized to identify methodological patterns across the literature, from which
futuredirectionsareanticipated. Figure1illustratesthephasesinvolvedinformulating
thestudy’skeyfindings. Thereviewprocessfollowedsixsequentialphases,beginning
withdefiningresearchquestionsanddevelopingsearchstrategies,followedbyestablishing
inclusionandexclusioncriteria. Datawerethensystematicallyextracted,organized,and
synthesizedtoidentifymethodologicalpatterns.
Figure1.Phasesofthesystematicliteraturereviewprocess.
2.1. ResearchQuestions(RQs)Formulation
Tostrengthenthegoalofthisstudywhileensuringacohesiveandstructuredapproach
guidingtheformulationofthesearchstrategyacrossthethreemainpillars—performance,
explainability,andfairness—aPopulation,Intervention,Comparison,Outcome,andCon-
text(PICOC)framework(Keele,2007)wasadoptedtotranslatethebroadertopicofem-
ployingAIincreditscoringintoanoperationallyprecisescopeattheplanningstageprior
to screening. By articulating the Population, Intervention, Comparison, Outcome, and
Context, the framework guides the search string construction, reduces bias by making
relevance criteria traceable to a predefined scope, and increases reproducibility by for-
mulating auditable selection choices. Using the PICOC framework, this work aims to
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 5of36
exploretherelationshipsandinteractionsamongthethreepillars,quantifytheirtrade-offs,
andacknowledgethatmorethanonepillarcanoperatejointlyandinfluenceanotherina
quantifiablemanner.
Table 1 explains the PICOC components and their relationship to the domain and
subject of this research, guiding RQ formulation and the search strategy developed to
alignthefindingswiththeoverallobjectives. ThePICOCframeworkdefinesthedomain
and subject of deployed AI models highlighted in past studies by referring to credit
scoringpredictionsbasedonevaluatingdefaultrisksusinghistoricalfinancialinformation
exclusivetoapplicationriskassessments.Thisreflectsthetechniquesormethodsemployed
toaddresssingleorjointchallengesincreditscoring,includingperformance,fairness,and
explainability,correspondingtothedeploymentofAItosolvethecreditscoringprediction
problemandincorporatingmultiplepillars. Itspecifieswhattheinterventionisevaluated
againstbyrequiringstudiestomakeuseofexistingbaselinestobenchmarktheirmethods
orhighlightthetrade-offsacrossthepillars,analyzingpillarinteractions. Italsocaptures
themeasuredandreportedperformanceindicators,fairnessmetrics,explainabilitywith
humancomprehension,andquantitativeassessmentoftrade-offanalysisbetweenpillars.
Finally,itdefinestheapplicationenvironmentandpublicationconstraintsbydetermining
whetherthestudyisexclusivetothecreditscoringdomain,publishedinapeer-reviewed
venue, ordemonstratesrecencyinreportingfairnessandexplainabilityintegratedinto
modeling,anditidentifieswheretrade-offsorresearchgapsemergeamongthethreepillars.
Table1.PICOCframeworkusedforresearchquestionformulation.
Component Definition
DefinesthedomainandsubjectofdeployedAImodelshighlightedinpast
studies. Itreferstocreditscoringpredictionsthatarebasedonevaluating
Population
defaultrisksusinghistoricalfinancialinformationthatisexclusiveto
applicationriskassessments.
Referstothetechniqueormethodemployedtotacklesingleorjoint
problemsgivenincreditscoring,includingperformance,fairnessand
Intervention
explainability. ItcorrespondstothedeploymentofAItosolvethecredit
scoringpredictionproblemandcanincorporatemultiplepillars.
Specifieswhattheinterventionisevaluatedagainst. Inthiscontext,studies
mustmakeuseofexistingbaselinestobenchmarktheirmethodsor
Comparison
highlightthetrade-offsacrossthepillars. Thiselementiscrucial,asit
analyzespillarinteractions.
Captureswhatwasmeasuredandreported,illustratingtheoutcomesof
interest,suchasperformanceindicators,fairnessmetrics,explainability
Outcome
withhumancomprehension,andquantitativeassessmentofthetrade-off
analysisbetweenpillars.
Definestheapplicationenvironmentandpublicationconstraints. It
determineswhetherthestudyisexclusivetothecreditscoringdomain,
publishedinapeer-reviewedjournalorconference,ordemonstrates
Context
recencyintermsofreportingfairnessandexplainabilityintegratedinto
modeling. Inaddition,itpinpointswheretrade-offsariseorothergaps
exist,giventhethreepillars.
DrawingonthePICOCframework,thefollowingresearchquestionshavebeenfor-
mulatedtodefinethecontextandobjectivesofthisresearch. Collectively,threeresearch
questionswerealignedwiththestudy’soverarchingaimtoexplorehowcreditscoring
frameworkscanbalancepredictiveperformancewithfairness,explainability,andregula-
toryaccountabilitythroughhuman-in-the-loopconsiderations. Morespecifically,RQ1ex-
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 6of36
aminesthetrade-offsbetweenperformance,interpretability,andfairness,RQ2investigates
thecurrentbiasmitigationstrategiesfocusingontheireffectiveness,andRQ3addresses
theroleofregulationandhumanoversightinensuringethicallyalignedAIsystems.
• RQ1:Towhatextentcancreditscoringframeworksachievecompellingperformance
whilebalancingexplainabilityandfairnesstrade-offs? TheextenttowhichAImod-
elsoperateopaquelyindeterminingcreditworthinessnotonlyhinderstheiradoption
butalsoposesthreatstotheirfairnessandtrustworthiness(Ribeiro-Fluchtetal.,2024).
Inresponse,numerouseffortswithinthecreditscoringlandscapehaveprioritized
transparencyandexplainabilitytodevelopcomplementaryorembeddedmethods
that clarify the rationale and reasoning behind AI-generated outcomes. Model ex-
plainability and interpretability are foundational in the deployment of AI and are
considerednolessimportantthantheperformanceitself. Apartfromdescribingthe
motive,bothcanfundamentallyservetheabilitytoexplaincausesleadingtobiasedor
uncertaindecisions(Alufaisanetal.,2021). High-stakesapplicationsdependcritically
ontheabilitytoreasonaboutandjustifymodeldecisions,wherebythelackoftrans-
parentdecision-makingposesasignificantdrawbackandmayresultinmistrustand
non-compliancewithlocalregulations(Wangetal.,2020). Consideringthecriticality
ofthethreepillars,thisresearchquestionexaminestheextenttowhichthesepillars
canbeelevatedjointlyoriftherearepotentialtrade-offs.
• RQ2: Howdohistoricalrepaymentdata,classimbalance,andprotectedattributes
contributetobiasedpredictions,andwhatmitigationstrategiesaremosteffective?
AcommonissueacrossdatasetsusedtotrainAImodelsisclassimbalance,which
hindersAImodelsfromproducingaccurateresults(Chenetal.,2024). Thisproblem
ispervasiveacrosscreditscoringdatasetswherethenumberofdefaultersissignifi-
cantlylessthanthatofnon-defaulters. Suchanimbalanceadverselyaffectsaccuracy,
suggestingtheneedformoreadaptivetechniquesthattreatallclassesequitably. In
addition,thepresenceofprotectedattributesacrossdifferentcreditscoringdatasets
potentiallyamplifiesthehistoricaldiscriminationagainstminoritygroups,leaving
structuraltracesintrainingdata(Hurlinetal.,2024;Talaatetal.,2024). Forinstance,
certainethnicgroupshavehistoricallybeengrantedcreditlessfrequently, thereby
appearing more frequently in the “bad” class, not due to actual risk but because
theyweredeniedfavorableproductsorguidance. Addressingthisresearchquestion
revealstherelationshipsamongclassimbalance,aswellastheirpotentialeffecton
protectedattributes,andprovidesmeanstounderstandthemitigationstrategiesthat
eliminatebiaseddecisions.
• RQ3: Howdoregulatoryframeworksandhuman-in-the-loop(HITL)approaches
influence the interpretation of fairness across different contexts, and how can
theybeincorporatedintoethicallyalignedAImodels? GiventhatAImodelsare
pronetobiaseddecisionsandlacktransparencyinhowtheirresultsaredetermined,
the intervention of regulatory bodies underscores the importance of consciously
adoptingAIindomainsinvolvingmonetarydecisionsandfundamentalhumanrights.
Whileprecisionandaccuracyweretheultimategoalssoughtinthepast,thelossof
transparencyhasprovenfarmorecostlyincriticalandregulateddomains,making
explainability a necessity rather than an option (Chen et al., 2024). Ensuring this
balanceenablestheresponsibleandaccountabledeploymentofAIincreditscoring
domains, supported by adequate human oversight to maintain compliance with
localregulations,andensuresthatresultsremaincomprehensibletohumandecision-
makers(Pengetal.,2023).
Guidedbytheseresearchquestions,thisworkaimstoexplorethepotentialtrade-offs
andpossibilitiestoincorporatemultipledimensionstoformanintersectionalframework
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 7of36
builtaroundthetriadofperformance,explainability,andfairness,withRegulationand
HITL. Figure 2 illustrates the conceptual framework showing the intersections among
performance,explainability,andfairnessinAI-drivencreditscoring. Theouterlayersrep-
resentregulatoryoversightandhumaninterventionascontextualdimensionsinfluencing
allthreepillars. Eachoverlapcorrespondstotheresearchquestions(RQ1–RQ3)guiding
thissystematicliteraturereview.
Figure2.Conceptualframeworkofperformance,fairness,andexplainabilityinAIcreditscoring.
2.2. SearchStrategy
Toensuretheretrievaloftherelevantliteratureandrefinethescope,thesearchstring
wascarefullycraftedtoemphasizetheintersectionbetweenthethreepillarshighlighted
earlier. Moreimportantly,italsohighlightsrecentadvancementsrelatedtobalancingor
interactionacrossthesedistinctdimensions. Therefore,thestudywasconductedusing
theIEEE,Scopus,WebofScience,andScienceDirectdatabasestoensurecomprehensive
andsufficientcoverageofpeer-reviewedjournalarticlesandconferenceproceedings. In
addition, Scopus included records from major indexing services such as ScienceDirect,
SpringerLink,WileyOnline,Taylor&FrancisOnline,IEEEXplore,andACMDigitalLibrary.
Thisensuredbroadinterdisciplinarycoverageofrelevantsourcesandthatthesearchwas
conductedacrossmultiplemajordatabasestoreducethelikelihoodofdatabase-specific
omission and bias in the retrieval process. Table 2 presents the search string used for
literatureretrieval.
Table2.Booleansearchstringusedtoretrievepublicationsbetween2020and2025.
TITLE-ABS-KEY(“creditscoring”OR“creditrisk”)
AND TITLE-ABS-KEY (“machine learning” OR “deep learning” OR “artificial intelligence” OR
“reinforcementlearning”OR“deepreinforcementlearning”)
ANDTITLE-ABS-KEY(“explainableAI”OR“interpretability”OR“modeltransparency”OR“XAI”
OR“fairness”OR“bias”OR“discrimination”OR“protectedattribute*”)
ANDPUBYEAR≥2020ANDPUBYEAR≤2025
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 8of36
Thesearchstringwasdesignedtolocaterelevantpapersbymatchingthespecified
keywordsacrossthetitles,abstracts,andkeywordssections;therefore,thefieldcode(TITLE-
ABS-KEY)wasused. Inaddition,keytermsandsynonymswereselectedtorepresentthe
coredimensionsofthisstudy,i.e.,explainability,fairnessandperformance. Optionally,
paperswererequiredtoaddressatleastonesecondarydimensionrelatedtofairnessor
explainability,ratherthanfocusingsolelyonperformance. Thisprocessinitiallyretrieveda
totalof436paperspriortotheselectionandscreeningstages.
2.3. SelectionCriteria
Togoverntheselectionofrecords,asetofselectioncriteriawasestablishedtocover
bothinclusionandexclusionprinciples. Thisincludesscreeningatthetitleorabstractlevel
andfull-textexclusion. Itensuresthattheselectionisstructuredandreproducible,that
the pool of studies aligns well with the research questions, and that biased selection is
prevented. Duetothelargevolumeofrecords,onlyarepresentativesubsetofpaperswas
considered,guidedbythePICOCcomponentsspecifiedearlier.
2.3.1. InclusionCriteria
Only studies that were published from 2020 onward in reputable, peer-reviewed
venues,suchasACM,IEEE,Springer,andElsevier,wereconsideredinthiswork. Thistem-
poralscopewasintentionallyselectedtocapturethemostrecentphaseofAI-basedcredit
scoringresearchshapedbytherapidadoptionofexplainableAI(XAI)andfairness-aware
learning,alongsideincreasingregulatoryscrutinyofautomateddecision-makinginhigh-
stakesdomains. Theperiodfrom2020onwardreflectsthegrowingmaturityofexplanation
techniques,counterfactualrecourse,andfairnessconstraintsintegratedintomodernlearn-
ingobjectives,aswellastheincreasingemphasisontransparency,non-discrimination,and
auditabilityincreditdecisionpipelines,alignedwithemergingAIgovernanceandaccount-
abilityrequirements. Moreimportantly,restrictingthescopetorecentstudiesincreasesthe
likelihoodofcapturingmethodsandevidencethatjointlyaddressmultiplepillarswithin
thesameexperimentalsetting,whichisessentialforintersection-orientedassessment.
The eligibility of papers was later assessed based on their coverage of at least one
additionaldimensionbeyondtheperformanceofcreditscoringmodels,namelyexplain-
ability and fairness, as highlighted earlier. In addition, the context and domain of the
researchmustbeexclusivetocreditscoringorcreditriskassessment,andthestudiesmust
demonstratemeasurableorinterpretableoutcomesor,ataminimum,conceptuallysupport
integratingfairnessandexplainabilityintocreditscoringframeworkstoestablishclear
linksforethicalframeworkassessment.
2.3.2. ExclusionCriteria
Studiesnotmeetingtheinclusioncriteriawereexcludedordeemedinsufficientto
explicitlyintegratethedifferentdimensionsofthisstudy. Thisincludedstudiesfalling
outsidethecreditscoringdomainoraddressingirrelevantAIapplicationssuchasNLP,
frauddetection,orinsurancerisk. Further,non-peer-reviewedmaterials,pre-2020pub-
lications,andoverlygenericworkswerealsoomitted. Additionalexclusionsappliedto
papersfocusingonlyonperformanceorfeatureselectionwithoutfairnessorexplainabil-
ity,orthoseaddressingcorporatelending,profitorlossprediction,ortransferlearning
basedonexternaldatasets. Purelyconceptualorregulatorydiscussionswereexcluded
unlessdirectlyrelevanttofairnessandexplainabilityunderRQ3. Lastly,studiesaddressing
creditscoringforcorporateloansandSmallandMediumEnterprises(SMEs)werealso
omittedfromthisstudy,astheydonotrelatetodataprivacyandtheinclusionofsensitive
(protected)attributes.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 9of36
2.4. ScreeningProcess
Followingtheinclusionandexclusioncriteriaspecifiedintheearliersubsection,the
PRISMA 2020 guidelines (Page et al., 2021) were followed, ensuring records identified
through database searches were screened by title, abstract, and full text to ensure their
alignment with the RQs. Figure 3 provides a summary of the systematic flow of study
identification,screening,eligibilityassessment,andinclusion.
Figure3.PRISMA2020flowdiagramforthesystematicidentificationandscreeningofstudies.
Theinitialsearchresultreturned436recordsfromelectronicdatabases,withnoaddi-
tionalrecordsfromregistersbeingconsidered. Duringtheidentificationphase,132records
wereexcludedduetoduplication(i.e.,identicalpapersretrievedfrommultipledatabases),
irrelevance,methodologicaloverlap,ordiscrepantmetadata. Theremaining304records
weresubjectedtotitleandabstractscreening,duringwhich227recordswereexcludedfor
failingtomeettheinclusioncriteriaspecified. Thisincluded,forinstance,applicationsof
AIincorporatecreditscoring,unrelateddomains,ornon–peer-reviewedmaterials.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 10of36
In the eligibility assessment stage, 77 reports were sought for full-text retrieval, of
which19couldnotbeaccessedduetounavailabilityorsubscription-basedrestrictions.
Theremaining58reportsunderwentfull-textassessmentagainstthequalityassessment,
basedonwhich10reportswereexcludedduetolow-qualityappraisalscores,and5were
excludedduetooverlappingscopeoroutdatedsurveycontent,asdetailedinAppendixA.
Finally,43studieswereincludedinthisreview,formingthefinalcorpusanalyzedacross
thedimensionsofperformance,explainability,andfairness.
Allrecordsretrievedfromtheselecteddatabaseswerescreenedbyonereviewerusing
thepredefinedinclusionandexclusioncriteria. Thescreeningwasperformedintwostages,
i.e., title/abstractscreeningfollowedbyfull-textassessment. Anyuncertaintiesduring
screeningwereresolvedthroughrepeatedmanualverificationagainsttheeligibilitycriteria.
2.5. DataExtraction
Tosystematicallyrecordthebibliographicinformation,methodologicaldetails,and
thematicattributionsofthe43includedstudies,astructureddatasheetwascreated,andthe
dataextractionwasperformedbyonereviewertoensureconsistencyandreproducibility.
MetadataextractedfromthesearchdatabaseswereimportedintoZoteroastheprimary
referencemanagementtool,thenexportedtoExcelforcodingandsynthesis. Bibliographic
details such as title, abstract, authors, DOIs, publication year, and venue formed the
evidencebaseforsubsequentanalysis.
Forthematicclassification,eachstudywastaggedtoreflectitsdominantthemesacross
performance,explainability,andfairness,aswellasconnectionstoregulatoryandHITL
concepts. Thesetagswereinstrumentalinidentifyingintersectionsamongthedimensions,
supportingtheconceptualframeworkdescribedinFigure2. Tominimizetranscription
errors,theextractedentrieswerecross-checkedagainsttheoriginalarticlesbeforesynthesis.
Noautomationtoolswereusedforextraction,andthestudy’sauthorswerenotcontacted
foradditionalinformation.
2.6. QualityAssessment
Sincetheincludedstudiesaremethodologicallydiverseandtargetatleastonepillar,
andsincethesynthesisofthisworkisnarrativeratherthaneffect-sizebased,thisreview
did not employ a domain-specific risk-of-bias tool. Instead, to ensure the inclusion of
methodologicallyandconceptuallyalignedstudies,astructuredmulti-criteriaappraisal
(Keele, 2007) was conducted by leveraging evidence weighting practices to assess the
relevance and rigor of each study. To support this, a customized 3Rs&Q framework
wasdesignedtoassessthecontributionofeachworktowardtheinteractionamongthe
three main pillars while also accounting for contextual dimensions such as regulation
andhumanintervention. Thescoringscalerangedfrom0to3,wherebyvaluesof0and
3 indicate the lowest and highest scores, respectively. Considering each 3Rs&Q metric
consistsoftwosub-metrics(R1–R6andQ1–Q2),thetotalattainablescorewas24,asshown
inTable3. Thetierthresholds(high: 17–24;medium: 9–16;low: <9)weredetermineda
prioribasedonequaldistributionacrossthe24-pointscaleandreflectincreasinglevelsof
methodologicalalignmentwiththethreepillars. Thisdistribution-basedapproachalso
ensuresthatpapersscoring8orbelowfallnaturallywithinthelower-qualitytierofthe
3Rs&Q scale. Papers demonstrating strong methodological and conceptual rigor were
scoredbetween17and24,formingthehigh-qualitytier. Inaddition,papersthatprovided
partialcoverageofisolateddimensions,suchasfocusingonlyonfairness,butstilloffered
usefulinsights,receivedscoresrangingfrom9to16andbelongedtothemedium-quality
tier. Lastly,theremainderofthestudiesthatscoredbelow9pointswerenotconsidered
duetolimitedconnectiontothereview’scoredimensions.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
11of36
Thiscustomized3Rs&Qappraisalframeworkwasappliedasastructuredrubricto
supportconsistentqualityappraisalacrossincludedstudies. Sincerubric-basedscoring
may introduce assessor subjectivity, scores were assigned using evidence-driven rules
thatreliedonlyonexplicitlyreportedinformationwithineachpaperratherthaninferred
intentions. Borderlinecaseswerere-checkedagainsttheoriginaltextandscoredconserva-
tivelywhenevidencewasinsufficient,ensuringthattheappraisalreflectsdocumentedand
relevantcontributionstothereview’scoredimensions.
Table3.The3Rs&Qqualityassessmentframeworkforevaluatingstudyinclusion.
| Dimension | Submetric | Description | ScoringCriteria(0–3) |
| --------- | --------- | ----------- | -------------------- |
Doesthestudyexplicitly
addressatleastoneofthe
sixconceptualpillars
none,peripheral,central
| Relevance | PillarAlignment(R1) | (ExplainableAI,Fairness, |     |
| --------- | ------------------- | ------------------------ | --- |
andfocus
Imbalance,Protected
Attributes,Regulation,
HumanIntervention)?
Doesthepapercontribute
|           |           | evidencetowardoneor    | none,weak,moderateand |
| --------- | --------- | ---------------------- | --------------------- |
| Relevance | RQFit(R2) |                        |                       |
|           |           | moreofthethreeresearch | strong                |
questions(RQs)?
Arethemodelsormethods
|     | MethodologicalSoundness | clearlydescribed, | poor,basic,robust,and |
| --- | ----------------------- | ----------------- | --------------------- |
Rigor
|     | (R3) | validated,and | stateoftheart |
| --- | ---- | ------------- | ------------- |
reproducible?
Doesthestudyuse
real-worlddatasets,
minimal,partial,strong
| Rigor | EvaluationDepth(R4) | multiplemetrics(e.g.,AUC, |     |
| ----- | ------------------- | ------------------------- | --- |
andcomprehensive
fairnessmeasures),or
comparativebaselines?
Doesthestudyconsider
regulatorycompliance(e.g.,
|       | Cross-ContextAwareness |              | none,partial,clearattempt, |
| ----- | ---------------------- | ------------ | -------------------------- |
| Reach |                        | ECOA,GDPR)or |                            |
|       | (R5)                   |              | anddeepanalysis            |
cross-nationalfairness
transferability?
Doesitcombinemultiple
siloed,minorcombination,
|       | IntegrationofDimensions | pillars(e.g.,fairness+    |                       |
| ----- | ----------------------- | ------------------------- | --------------------- |
| Reach |                         |                           | partialintegrationand |
|       | (R6)                    | explainabilityorimbalance |                       |
holisticframework
+regulation)?
Arecode,data,or
|     | Transparency(Q1)and | supplementary | notavailable,vague,partial |
| --- | ------------------- | ------------- | -------------------------- |
Quality
Reproducibility reproducibilityresources andopenandreproducible
available?
Doesthestudyprovide
actionableinsightsfor
theoretical,limited,
| Quality | PracticalRelevance(Q2) | deployment(e.g.,industry |     |
| ------- | ---------------------- | ------------------------ | --- |
moderateandstrong
adoption,humanoversight,
legalcompliance)?
3. Results
3.1. StudySelection
Followingthequalityassessment,atotalof58paperswerethoroughlyassessedand
scored. Amongthese,15papersforming25.8%oftheselectedstudieswereexcludeddueto
lowscores(≤8),failuretomeettheeligibilitycriteriaandoverlappingscopes.Consequently,
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 12of36
theyweredeemedunsuitabletoaddresstheobjectivesofthiswork. Adetailedsummary
ofthe43studiesconsideredintheanalysisandresultsisprovidedinAppendixB.
3.2. CharacteristicsofSelectedStudies
Consideringthe multidisciplinary natureof thecreditscoring problem, studiesin-
cludedinthisreviewwerepublishedacrossvariousvenues,with95.4%and4.6%published
asjournalarticlesandconferencepapers,respectively. Amongindexedsources,13.95%
ofstudieswereretrievedfromIEEEXplore,followedbySpringerLink,withover11.63%.
Bothvenuesrepresentedasubstantialportionoftechnicalandcomputationalresearchin
theselectedsample. Additionally,smallerbutnotableportionsoftheselectedstudieswere
obtainedfromElsevier’sScienceDirectandopen-accesspublications,suchasPLOSONE,
both equally forming 6.98%. Other publications from ACM Digital Library and MDPI
accountedfor2.33%ofthefinalset.
Table4showsthedistributionofstudiescategorizedbypublishedfamily. Giventhat
creditscoringintersectsfinance, statistics, artificialintelligence, andregulatorystudies,
morethanhalfoftheselectedsample(55.81%)waselicitedfromdomain-specificjournals
orconferencevenuesthatdonotbelongtoaparticulardigitallibrary. Furthermore,most
ofthestudiesincludedhereinwerepublishedbetween2023and2024,forming30.2%and
48.8%forthesameyears,respectively. Theremainingstudies—publishedbetween2020
and 2022—formed only 21%, thereby confirming the recency of the intersection across
dimensionsconsideredinthisstudy.
Table4.Distributionofstudiesbypublisherfamily.
Database/PublisherFamily Count %
IEEEXplore 6 13.95%
SpringerLink 5 11.63%
Elsevier(ScienceDirect) 3 6.98%
OpenAccess(Public) 3 6.98%
ACMDigitalLibrary 1 2.33%
MDPI 1 2.33%
Other/Misc. 24 55.81%
3.3. TopicCoverage
Thetrendsobservedinthecoverageacrossdimensions,asshowninFigure4,reveala
clearshiftintheresearchagendaofcreditscoringfrom2023onward,withalowercount
for 2025 since the year was still in progress at the time of data collection. Prior to this,
asmallnumberofstudiescoveredanyoftheinvestigateddimensionsandweremostly
fragmented. While the concept of fairness was simply being applied in AI disciplines,
humaninterventionandregulatoryaspectswerealmostabsent. Thissuggeststhatstudies
priorto2023wereprimarilyfocusedonperformanceand,toacertainextent,onmitigating
biasassociatedwithprotectedattributes.
However, in 2023, there is an evident surge across all investigated dimensions. It
is worth noting that studies increasingly incorporate protected attributes and examine
theireffectsonfairnessandexplainability,underscoringtheirgrowingimportanceinmore
recentstudies. Thissuggestsaturningpointwherethefieldbegantooperationalizean
ethicalandtransparentmodeldesignratherthanbeingmerelyperformance-focused. This
shiftalignswellwiththepolicypressureimposedbyregulators,whichlikelystimulated
regulatoryresponsestoaddressethicalandsocialaccountabilityconcernsintheliterature.
Among all considered dimensions, explainability showed the strongest expansion
between2023and2024,markingitasthedominantandmostsubstantialpillarofrecent
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 13of36
creditscoringresearch. Ontheotherhand,studiesconcerningprotectedattributesand
their regulation in algorithmic decision-making also increased significantly after 2022,
signalingasignificantsurgeincompliancewithgovernanceandlegalframeworks. Human
intervention,however,remainscomparativelyunder-represented,despiteitssignificance
inhigh-stakessettings,particularlywhenthetrade-offbetweenperformanceandfairness
ispresumed. Overall,thistrendrepresentsamajortransitionfromperformance-focused
representationofthecreditscoringproblemtowardbiasandinterpretability-awarecredit
scoring,withregulationandhumaninterventionbeingcentraltoresponsibledeployment.
Figure4.Topiccoveragebyyear.
Furthermore, to quantify the intersections between different dimensions, Table 5
presentsthepairwiseintersectionsbetweenallconsidereddimensionsgroupedbybase
dimension. Notably, fairness and protected attributes represented the largest portion
ofstudiesthataccountedformeasuringfairnessacrosssensitive/privatefeatures,with
21papersdiscussingthisassociation. Thisconfirmsthatfairnessdiscourseisprimarily
anchoredingroupfairnessdefinitions. Moreover,theassociationbetweenfairnessand
otherdimensions,includingregulationandhumanintervention,wasrankedsecondfrom
thepointofviewoffairness,having11papersrelatingittohumancomprehensionand
regulatoryframeworks. Thispatternsuggeststhatwhenfairnessandprotectedattributes
are foregrounded, regulatory requirements involving human oversight are simultane-
ouslyconsidered.
Despitethat,mid-tierintersectionsbetweenexplainabilityandotherpillars,including
fairness,thepresenceofprotectedattributes,regulationandhumanoversightwerefoundin
sevenorfewerpapers,highlightingthisassociation. Thissuggeststhatwhileexplainability
isincreasinglypresentinbias-awareframeworks,itremainsanauxiliaryfunctionandnot
yetcentral.Inotherwords,explainabilityincreditscoringtendstoserveasabias-diagnostic
ratherthanacompliance-orfairness-enforcingmechanism.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
14of36
Table5.Pairwiseintersectionsgroupedbybasedimension.
| Dimension      | Intersect           | Count |
| -------------- | ------------------- | ----- |
|                | Imbalance           | 10    |
|                | Fairness            | 7     |
| Explainability | ProtectedAttributes | 6     |
|                | Regulation          | 6     |
|                | HumanIntervention   | 6     |
|                | ProtectedAttributes | 21    |
|                | Regulation          | 11    |
Fairness
|                     | HumanIntervention | 11  |
| ------------------- | ----------------- | --- |
|                     | Imbalance         | 6   |
|                     | Regulation        | 11  |
| ProtectedAttributes | HumanIntervention | 11  |
|                     | Imbalance         | 4   |
| Regulation          | HumanIntervention | 10  |
4. Discussion
Thissectionexaminesthetrade-offsandassessescompatibilityacrossperformance,
fairness,andexplainabilityasthreecrucialelementsintheethicalandresponsibledeploy-
mentofAIwithinthecreditscoringdomain. Toachievethat,theinteractionsamongthese
pillarsaresynthesizedtodeterminetheircompatibilityanddescribeobservedpatterns.
Inaddition,thissectionhighlightscommonbiasmitigationstrategiesandcomparestheir
effectivenessinthedeploymentpipeline,anditconceptuallyrelatesmodelinterpretation
to human comprehension to support ethically aligned deployment. Where applicable,
the discussion is supported by empirical and conceptual evidence reported in the re-
viewedliterature.
4.1. CompatibilitiesandTrade-Offs(RQ1)
| Performancevs. Explainability |     |     |
| ----------------------------- | --- | --- |
ConsideringthewideadoptionofAImodels,rangingfrominherentlyinterpretable
toblack-boxmodels,thereisnoconsensusfromtheliteratureconfirmingtheavailability
ofuniversallycompliantmodels. Althoughthetermsinterpretabilityandexplainability
areusedinterchangeablyinthiswork,bothdenotetheconsciousadoptionofAIaimed
atestablishingthegroundsforunderstandingmodeloutcomes(Ratuletal.,2021). Over
theyears, modelshavebeenprimarilyperformance-focused, achievinghighpredictive
accuracybutoftenfailingtoexplaintheirresultsduetotheircomplexity. Aclearexampleis
thetransitionfromtraditionalmodels,suchaslogisticregression(LR)andshallowdecision
trees(DTs),tomoresophisticatedboostinganddeeplearning(DL)architectures. Arguably,
despitebothapproachesbeingextensivelyexploredandsharingsimilarities,deeplearning
demonstratesgreatersuitabilityinaddressingmodernandcomplexcreditscoringcontexts.
However,thisadvancementcomesatthecostofinterpretability,whichposeschal-
lengesinhighlyregulated,high-stakesdomains(Bückeretal.,2022). Understandingthe
model’sreasonsforidentifyingdefaultersisfoundationalinthefinancialsector,particu-
larlyincreditriskdomains(Valdrighietal.,2025),consideringthatthisopacityposesa
limitationforcreditassessorsinvalidatingandtrustingtheirresults. Bycontrast,tradi-
tionalandshallowtree-basedmodelsaregenerallymoreinterpretableandcanprovide
insightsintohoweligibilityisdetermined(Kanaparthi,2023). Forinstance,thecoefficients
optimizedinLRreflectthemagnitudeoffeatureinfluenceontheoutput,whileDTsoffer
atransparenttree-likestructureshowingthecollectivedecisionpathsleadingtothefinal
outcome. Conversely,DLmethodsrelyheavilyonpost-hocexplainabilitytechniquesto
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 15of36
compensatefortheiropacity,whichoftenraisescomplianceconcernsinregulatedsectors
(Hjelkrem&Lange,2023).
Consequently,therehasbeenanoticeableexpansionintheadoptionofpost-hocmeth-
ods,particularlySHAPandLIME(Aruleba&Sun,2024;S.Hanetal.,2024;Hjelkrem&
Lange,2023;Hlongwaneetal.,2024;Nwaforetal.,2024;Zhangetal.,2025),whichcan
operateindependentlyofmodeldesign. Forexample,Nwaforetal.(2024)proposedahy-
bridapproachcombiningasingle-dimensionalCNNandXGBoosttoformulateastacking
architectureforcreditscoringwhileensuringexplainability. Theirresultsdemonstrated
greater performance of the hybrid model when compared with native models, such as
CNN,XGBoost,andLR,attaininganaccuracyof96%,exceedingthatoftheinterpretable
LRmodelby4%. AsimilarexamplewasobservedintheworkofHlongwaneetal.(2024).
Theyarguedthatwhiletree-basedmodelssuchasXGBoostandRFprovidepromising
performanceresults,theylacksufficientinterpretabilitytoexplainthem. Byintegrating
SHAP into their deployment pipeline, they successfully visualized feature attributions
towardpredictionoutcomes. However,whentheAUCmeasureswerecomparedagainst
LR,bothRFandXGBoostoutperformedLRbyonly1%.
Theseexamplesprovideconcreteevidencethatthetrade-offbetweenexplainability
andperformanceislargelyassumedratherthanempiricallymeasured. Thisobservationis
inlinewiththeonehighlightedbyDessainetal.(2023),wheretheyexplicitlystatedthatthe
trade-offbetweenperformanceandexplainabilitystemsfromthemovetowardcomplex
black-boxmodelslackingintrinsicinterpretability. Intheirexperiment,theyquantifiedthis
trade-offacross12models,includinginherentlyexplainableandblack-boxmodels. From
abusinessstandpoint, theyconcludedthattheperformancegapbetweeninterpretable
and black-box models corresponds to only 0.14–0.21% in annual return on investment.
Despitethat,theyappliedisotonicsmoothingtoGAMsinordertoincreaseinterpretability
withoutfurtherfinancialloss, achievingperformanceclosetothatofblack-boxmodels.
Therefore,thechoicebetweeninherentlyinterpretableandblack-boxmodelsisprimarily
determinedbyaninstitution’srisktolerance. Itisalsoworthnotingthatstudiesmeasuring
thistrade-offwererelativelylimited,underscoringtheneedforempiricalmeasurementif
inherentlyinterpretablemodelsaretobeconsidered.
Overall,theliteratureindicatesthatexplainabilityispredominantlyintroducedasa
post-hocadditiontoblack-boxmodelsratherthanbeingembeddedorenhancedwithin
inherentlyinterpretableones. Thepresumedtrade-offbetweenperformanceandexplain-
abilityisthusoftenassertedratherthandemonstrated,withalimitednumberofstudies
quantifyingthiscostandobservingittobemarginal. Ingeneral,itisobservedthatthe
currentpracticeincreditscoringfavorspreservingpredictivestrengthwhilemitigating
opacitythroughauxiliaryexplainabilitymethodsratherthanprioritizinginterpretability
fromtheoutset.
Despiterecurringclaimsthatmodeltransparencydegradespredictivestrength,empir-
icalevidenceshowsthattheperformancegapsbetweentransparentandblack-boxmodels
areconsistentlymarginal,asillustratedinTable6,withlimitedstudiesdemonstratinga
substantialperformancedegradationwhenusinginterpretablebaselines. Itisalsoworth
notingthatthecomparisonresultsshouldbeperceivedunderafairsetting, wherepre-
processingandfeaturepreparationstepsareappliedconsistentlyacrossbothinterpretable
andblack-boxmodels,ensuringthatobserveddifferencesreflectmodelcapacityrather
than unequal data treatment. In some cases, the gain from complex models was even
negligible,denotingthattheperceivedtrade-offislargelyassumedbutrarelyquantified.
Asaresult,modelexplainabilitytendstobeincorporatedaftermodelselectionratherthan
shapingit,implyingthattheperformanceandexplainabilityconflictislessstructuralthan
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
16of36
commonlyportrayed,particularlyinregulatedcreditscoringcontextswhereevenmarginal
gainsrarelyjustifyopacity.
Table6.Comparisonofinterpretablevs.black-boxmodelperformanceinincludedstudies.
| Paper | Dataset | ModelsCompared | Metric  | Interp. Black-Box | ∆     |
| ----- | ------- | -------------- | ------- | ----------------- | ----- |
|       |         |                | AUC     | 0.95 0.99         | +0.04 |
|       |         |                | H-score | 0.95 0.95         | 0.00  |
Nwaforetal.(2024) LendingClub LRvs.XGB Precision(w) 0.93 0.95 +0.02
|     |     |     | Recall(w)   | 0.92 0.94 | +0.02 |
| --- | --- | --- | ----------- | --------- | ----- |
|     |     |     | F1-score(w) | 0.92 0.94 | +0.02 |
S.Hanetal.(2024) HE&GMSC(best-case) LRvs.RF/GB AUC 0.9750 0.9891 +0.0141
Chaietal.(2025) Farmers(best-case) DTvs.LCE AUC 0.622 0.784 +0.162
|     | Taiwan | LRvs.RF(best-case) | AUC | 0.74891 0.75929 | +0.01038 |
| --- | ------ | ------------------ | --- | --------------- | -------- |
Hlongwaneetal.(2024)
|                         | HomeCredit             | LRvs.XGB(best-case) | AUC      | 0.69644 0.69766 | +0.00122 |
| ----------------------- | ---------------------- | ------------------- | -------- | --------------- | -------- |
|                         |                        |                     | AUC      | 86.81 89.17     | +2.36    |
| Zhangetal.(2025)        | PCL                    | DTvs.IAIBS          | Accuracy | 76.95 79.32     | +2.37    |
|                         |                        |                     | F1       | 56.79 59.39     | +2.60    |
|                         |                        | LRvs.IAIBS          | AUC      | 77.48 79.86     | +2.38    |
|                         | FICO                   |                     | Accuracy | 71.52 74.55     | +3.03    |
|                         |                        |                     | F1       | 73.93 76.51     | +2.58    |
|                         |                        | DTvs.IAIBS          | AUC      | 96.04 97.48     | +1.44    |
|                         | CCF                    | LRvs.IAIBS          | Accuracy | 97.45 97.56     | +0.11    |
|                         |                        |                     | F1       | 86.71 88.69     | +1.98    |
|                         |                        | LRvs.IAIBS          | AUC      | 61.91 66.03     | +4.12    |
|                         | VL                     |                     | Accuracy | 59.32 62.70     | +3.38    |
|                         |                        |                     | F1       | 60.18 63.31     | +3.13    |
|                         |                        |                     | Accuracy | 0.720 0.783     | +0.063   |
|                         |                        | DTvs.ANN            | F1-score | 0.644 0.747     | +0.103   |
| AliShaheeandPatel(2025) | Proprietary            |                     |          |                 |          |
|                         |                        | (ADASYN+FL)         | AUC      | 0.737 0.812     | +0.075   |
|                         |                        |                     | G-mean   | 0.602 0.747     | +0.145   |
|                         |                        | LRvs.LightGBM       | AUC      | 0.91 0.94       | +0.03    |
|                         |                        | LRvs.CatBoost       | AUC      | 0.91 0.94       | +0.03    |
|                         |                        | LRvs.RF             | AUC      | 0.91 0.93       | +0.02    |
|                         |                        | LRvs.MLP            | AUC      | 0.91 0.91       | +0.00    |
|                         |                        | SVMvs.LightGBM      | AUC      | 0.88 0.94       | +0.06    |
|                         |                        | SVMvs.CatBoost      | AUC      | 0.88 0.94       | +0.06    |
|                         |                        | SVMvs.RF            | AUC      | 0.88 0.93       | +0.05    |
|                         |                        | SVMvs.MLP           | AUC      | 0.88 0.91       | +0.03    |
|                         |                        | NBvs.LightGBM       | AUC      | 0.89 0.94       | +0.05    |
|                         |                        | NBvs.CatBoost       | AUC      | 0.89 0.94       | +0.05    |
|                         |                        | NBvs.RF             | AUC      | 0.89 0.93       | +0.04    |
|                         |                        | NBvs.MLP            | AUC      | 0.89 0.91       | +0.02    |
| L.H.Lietal.(2025)       | LendingClub(2007–2020) |                     |          |                 |          |
|                         |                        | LRvs.LightGBM       | Accuracy | 0.83 0.87       | +0.04    |
|                         |                        | LRvs.CatBoost       | Accuracy | 0.83 0.86       | +0.03    |
|                         |                        | LRvs.RF             | Accuracy | 0.83 0.86       | +0.03    |
|                         |                        | LRvs.MLP            | Accuracy | 0.83 0.84       | +0.01    |
|                         |                        | SVMvs.LightGBM      | Accuracy | 0.83 0.87       | +0.04    |
|                         |                        | SVMvs.CatBoost      | Accuracy | 0.83 0.86       | +0.03    |
|                         |                        | SVMvs.RF            | Accuracy | 0.83 0.86       | +0.03    |
|                         |                        | SVMvs.MLP           | Accuracy | 0.83 0.84       | +0.01    |
|                         |                        | NBvs.LightGBM       | Accuracy | 0.81 0.87       | +0.06    |
|                         |                        | NBvs.CatBoost       | Accuracy | 0.81 0.86       | +0.05    |
|                         |                        | NBvs.RF             | Accuracy | 0.81 0.86       | +0.05    |
|                         |                        | NBvs.MLP            | Accuracy | 0.81 0.84       | +0.03    |
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 17of36
To interpret the performance gap between inherently interpretable and black-box
models, the marginal differences reported in Table 6 should be viewed as dataset- and
method-dependent rather than consistent across all settings. While most comparisons
indicateonlyminorperformancevariations,somestudiesreportlargergainswhenthe
modellingapproachintroducesadditionalcapacitytocapturehigher-orderinteractions
andnon-lineardecisionpatterns. Consequently,theobserveddifferencesareconditional
not only on the characteristics of the underlying datasets but also on the experimental
andpre-processingchoicesadoptedineachstudy. Akeydriverofreducedperformance
gaps is the extent of data refinement and feature reduction that simplifies the learning
problem. ThisisdemonstratedbyNwaforetal.(2024),wheretheLendingClubdataset
was reduced from over 1 million observations and 145 features to 25,535 observations
with25featuresthroughexploratoryanalysisandfeaturefiltering. Thisdimensionality
reductionlikelydecreasedredundancyandnoise,enablinginterpretablebaselinessuch
aslogisticregressiontoremaincompetitiveandlimitingtheincrementalgainachieved
byXGBoost.
A similar trend is observed in the work of L. H. Li et al. (2025), where extensive
pre-processing,featurefiltering,andnormalizationappliedtotheLendingClubdataset
resultedinperformanceimprovementsthatremainbroadlycomparableacrossinterpretable
andblack-boxmodels. Evidenceofanevensmallertrade-offisprovidedbyHlongwane
etal.(2024),wherediscretization,featureengineering,andvariableselectionwereused
toconstrainfinalscorecardcomplexityintheTaiwanandHomeCreditdatasets. Under
thiscontrolledsetup,performancedifferencesbetweenlogisticregressionandtree-based
modelsbecamenear-negligible,particularlyinHomeCredit,whereXGBoostyieldedonly
aminimalAUCimprovementoverlogisticregression. Collectively,thesefindingssuggest
thatwheninputdimensionalityisreduced,noiseiscontrolled,andpre-processingsteps
are applied uniformly across model families, the advantage of black-box models often
becomesmarginal.
In contrast, pipelines that do not consider observation and complexity reduction
techniquescanyieldlargergains,particularlywhenexplicitlytargetingcomplexregionsof
thefeaturespacethatinterpretablemodelsstruggletocapture.Zhangetal.(2025)exemplify
thisbyproposingaboundary-focusedhybridframeworkthatretainslogisticregressionas
atransparentbaselinewhileintroducingadeeplearningcomponenttrainedonboundary
samples. Rather than simplifying the feature space through reduction techniques, the
studyappliespre-processingprimarilyforimbalancemitigation,enablingmodelstolearn
moreeffectivelyfromcomplexdecisionboundaries. Thisdesignincreasesmodelcapacity
specificallyinregionswherelineardecisionfunctionsunderperform,helpingtoexplainthe
comparativelylargerimprovementsreportedintheirexperiments. Inconclusion,Table6
indicatesthatthetrade-offbetweenexplainabilityandperformanceisnotuniversalbut
greatly shaped by the complexity of datasets, the extent of pre-processing and feature
reductionapplieduniformlyacrossdifferenttypesofmodels,andwhethertheblack-box
approach is a standard global learner or an advanced architecture designed to capture
high-orderpatterns.
Performancevs. Fairness
Fairness represents a long-standing challenge inherently present in credit scoring
datasets. It reflects a well-known tension with predictive performance, although this
tensionisnotabsolutebutconditionalinmostcases. Itsadverseeffectsonunderserved
and excluded populations stem primarily from historical data, which are often biased
and reflect past human decisions (Das et al., 2023; Valdrighi et al., 2025). When these
biaseddecisionsremainunaddressed,theriskofamplifyingtheirimpactincreaseswiththe
integrationofAImodels,assuchmodelstendtoreproducetheembeddedbiaseswithin
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 18of36
acceptedloanapplications(Chaietal.,2025;Kozodoietal.,2025). Asaresult,fairnessis
integraltoanycreditscoringpractice,whetheritistraditional,statistical,orAI-based,and
ignoringitperpetuatesdiscrimination.
Acrosstheliterature,giventhatbiasisinevitable,fairnessisoftentreatedasamulti-
objectiveoptimizationproblemthataimstooptimizepredictionsundersoftconstraints
(S.Liu&Vicente,2022;Martinezetal.,2020). Thismeansthatpredictivecapabilityand
equitablegrouptreatmentarejointlyoptimizedratherthanonebeingmaximizedatthe
expenseoftheother. Forinstance,BalashankarandLees(2022)arguedthatfairnessinML
canbeachievedbytransparentlypresentingnon-dominantandbest-performingtrade-offs
between demographic group accuracy and overall prediction. Using a Pareto frontier,
humaninvolvementbecomescentraltodeterminethebesttrade-offbetweenperformance
andfairness(Zehlikeetal.,2025). Similarapproacheshavebeenreportedinotherstudies
(Badar&Fisichella,2024;S.Liu&Vicente,2022;Martinezetal.,2020),confirmingthatthe
trade-offbetweenperformanceandfairnessisunavoidableandistypicallymodeledasan
optimizationproblemseekingtobalancebothobjectives.
Havingsaidthat,Kozodoietal.(2022)andBadarandFisichella(2024)furthernoted
thatfairnesscanbeimprovedwhileensuringminimumlossinprofitandperformance,
providedthatparityconstraintsarenotenforcedtoostrictly.Incontrast,havingstrictparity
conditionscouldpotentiallyleadtodeteriorationinpredictionutility.Thisobservation
was empirically reported by S. Liu and Vicente (2022), where they concluded that fair-
nessconstraintsreduceaccuracyprogressivelyastheytighten.Byadjustingtheobjective
functiontominimizepredictionlossandfairnessviolationterms, theyderivedacurve
ofoptimaltrade-offs, demonstratingaproportionalrelationshipbetweenaccuracyand
fairness violations. In other words, minimizing fairness violation results in degraded
accuracy, and vice versa, confirming that fairness is tunable and not strictly achieved.
Therefore,dataimbalancestrategiescontributetofairnesstotheextentthattheyrestore
representativenessandreconstructmissinggroupsthatwouldotherwiseberepresentedas
astructuraldiscrimination.
Furthermore,althoughfairnessanddataimbalancearetreatedseparatelyacrossthe
literature,theyimplicitlyinfluenceoneanotherandcanpotentiallydegradefairnessacross
protectedgroupsifnotaddressed(Brzezinskietal.,2024;J.Liuetal.,2024;Shietal.,2025).
Itformsnotonlyatechnicalissuehinderingperformance,butalsoamaterialexclusion
systemembeddedintocreditscoringmodels. Consideringthatprotectedgroupsarenot
presentatequalratesacrossdifferentoutcomes,dataimbalancetechniquescanrectifythe
adverseeffectsbyover-representingtheseminoritygroupsintheminority(default)class.
Asimilartrade-offpatterncanbeobservedwhenconsideringdataimbalancemitiga-
tionstrategies. Forinstance,theworkofKozodoietal.(2025)demonstratedarecoverable
36%ofperformancelossusingtheirproposedBASLrejectioninferenceframeworkwhile
simultaneouslyimprovingfairnesscomparedwithtraditionalsamplingtechniques. The
goaloftheirframeworkwastograduallyinferlabelstounlabeledsamplesiteratively,until
model performance improves. The process of relabeling continues until all samples in
adatasetarelabeledandreadyforfinaltraining. However,theysimplynotedthatthis
iterativeprocessispronetosamplingbias,henceincreasingtheriskofoverconfidenceand
overfittingofamodel,andtherebydegradingthegeneralizationofthemodel. Thesame
observationwasalsomadebySulastrietal.(2025)andAtif(2025),wherestronginclusion
adjustmentspotentiallyharmgeneralizationandstability.
Overall,theliteraturesuggeststhatwhilethereexistsanotabletrade-off,fairnessis
neitherimpossiblenorcompletelyachievable,buttunable. Thisindicatesthatfairnessis
anoptimizationdecisionthatisboundedbyrisktoleranceandsocietalconstraintsrather
thanbeingatechnicalimpossibility.Theliteratureshowedsomecaseswheremoderate
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 19of36
fairnessadjustmentsachievedcompellingresultsintermsofperformanceaswellasfairness,
whereasaggressivecorrectionstendtodistortdatadistributionsandoftenleadtooverfitting
andinstability.
4.2. FairnessStrategiesinDeploymentPipelines(RQ2)
DespitethenotablegrowthinintegratingfairnessintoAIdeployments,asshownin
Figure 4, out of the selected 43 papers, only 10 explicitly measured the effectiveness
of existing mitigation strategies or proposed novel ones to counter bias in the credit
scoringdomain.Thisrepresentsnomorethan23.25%ofthetotalreviewedstudies,despite
fairnessbeinganintegralandlong-standingconcernincreditscoringratherthananewly
introduced concept (Brzezinski et al., 2024; Kozodoi et al., 2022). As a result, relatively
few studies have addressed the adverse implications of protected attributes in lending
decisions,particularlyinalgorithmicdecision-makingsettingsthatarepronetoproducing
discriminatoryoutcomesthatdisproportionatelyaffectminoritygroups(Moldovan,2023).
ThispatternalignswiththeobservationofKozodoietal.(2022),whoexplicitlystatedthat
fairnessremainsunderexploredrelativetoexplainabilityandclassimbalance.
Before delving into fairness mitigation strategies, it is worth noting that fairness
comesintwodifferentnotions: individualandgroupfairness(Valdrighietal.,2025). The
latterisfocusedongeneralizingcreditdecisionsacrossgroupscharacterizedbyprotected
attributessuchasgender,ethnicity,andreligion. Allstudiesincludedhereinoperationalize
group fairness, whereas individual fairness was mentioned only conceptually in a few
studies,suchastheworkofKozodoietal.(2022),aswellasValdrighietal.(2025),without
empiricalimplementation. Todeterminefairnesseffectiveness,commonlyknownmetrics
areusedtoevaluatetheirsuitabilityacrossdifferentnotions,whichincludeindependence,
separation, and sufficiency (Kozodoi et al., 2025; Moldovan, 2023). These metrics were
foundtobeincompatiblewhencombined,andthereisnouniversalagreementonwhich
metric should be prioritized (Brzezinski et al., 2024; Zehlike et al., 2025). Due to this,
Zehlikeetal.(2025)proposedanovelalgorithmcalledFairInterpolationMethod(FAIM)
thatinterpolatesbetweenthethreefairnesscriteriatodevelopareward/penaltyobjective
functionthatrelaxesthenotionofcompetingmetrics,resultinginaweightedcombination
offairnesscriteria.
Considering that bias may enter the deployment pipeline at multiple stages (Das
etal.,2023),fairnessmetricsareconsistentlyappliedasdownstreamevaluationmeasures,
regardlessoftheinterventionpoint. Accordingly,theliteratureorganizesfairnessinter-
ventionsintothreebroadcategoriesbasedontheirpositioninthedeploymentpipeline:
pre-processing, in-processing, and post-processing (Valdrighi et al., 2025). To date, no
consensusexistsregardingauniversallydominantmitigationstrategy,renderingfairness
apracticalchallengeforlendinginstitutions,aseachcategoryexhibitsdistinctstrengths
and limitations (Kozodoi et al., 2022; Moldovan, 2023). The full set of fairness mitiga-
tionstrategiesidentifiedfromthereviewedliterature,categorizedbyinterventionstage
andmethodologicalcharacteristics,issummarizedinAppendixC.Acrosscategories,no
mitigation strategy consistently dominates others, reinforcing the view of fairness as a
context-dependentoptimizationproblemratherthanauniversalcorrection. Accordingly,
thecomparisonscopeisinevitablylarge,withtheexistenceofcommonaspectsthattouch
oneachmitigationstrategy. Forexample, pre-processingmethodsintervenebeforethe
trainingphaseofAImodelsandaimtomodifythedistributionofdatapriortotraining
(S.Hanetal.,2024). Thisoftenleadstolowerdeploymentcostsandtheabilitytoimprove
fairnesswithouthavingtoretrainmodels,consideringmodelretrainingistime-consuming
(Kozodoietal.,2022). Nonetheless,sincepre-processingstrategiesaremodelagnostic,they
oftenrequirerepeatedadjustmentstothedatapipelineandpotentiallyleadtooverfitting
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 20of36
whenfairnessisstrictlyenforced,makingthemgoodstrategiestotuneandreducebias,
ratherthancompletelyeliminateit(Chaietal.,2025).
Additionally,accordingtoKozodoietal.(2022),in-processingtechniquesconsistently
achievelargerfairnessgainswithminimallossinpredictiveutility,assumingthatfairness
isembeddedintotheoptimizationobjectiveitself. Sincetheytypicallyreportthetrade-off
between accuracy and equity in a Pareto frontier, in-processing techniques offer better
controlandoversighttorealizePareto-efficientcompromises. Severalotherstudiesalso
reportedthisbehavior,confirmingthatthetrade-offismoretunablewhilehavingexplicit
control over the outcomes (S. Liu & Vicente, 2022; Moldovan, 2023). Conversely, since
they account for multiple objectives simultaneously, they incur higher computational
costandoftenrequirehyperparametertuningtoidentifytheoptimalconfigurationdue
totheirmodel-specificmechanism, therebyresultinginhigherimplementationburden
(Valdrighietal.,2025).
Similartopre-processingmethods,post-processingisanotherformofmodel-agnostic
techniques that aim to adjust model outputs post-training to meet fairness criteria
(Zehlikeetal.,2025). Thismakesthemaversatileoptionforblack-boxmodelsandstrictly
governed scorecards, since bias mitigation is performed in isolation from the model’s
training and prediction themselves (Valdrighi et al., 2025). Despite this, they incur the
highestutilitycostperfairnessgainandcannotrepairupstreambiassincetheyactsolely
on the decision boundary. As a result, post-processing techniques exhibit a substantial
decreaseinprofitabilityrelativetoin-processingoptions,andtheyarelesstunablethan
in-processingtechniquessincetheyoperateonoutputsinsteadoflearnedrepresentations
(Kozodoietal.,2022).
Synthesizing the findings across studies reveals that fairness mitigation should be
viewed as an optimization problem rather than a one-time corrective step, with trade-
offs emerging between predictive performance, implementation complexity, and regu-
latory suitability. Pre-processing methods intervene before model training by modify-
ing data distributions (S. Han et al., 2024), often offering lower deployment costs and
model-agnosticapplicability. However, strictenforcementoffairnessconstraintsatthe
data level may require repeated adjustments and can introduce overfitting risks, mak-
ing such approaches more suitable for bias reduction rather than complete mitigation
(Chaietal.,2025;Kozodoietal.,2022).
Overall,whileeachfairnessstrategyhasitsownstrengthsandweaknesses,thelitera-
turemakesitevidentthatthereexistsnouniversallydominantstrategyacrossthescoring
pipeline. Rather,thesestrategiesemergeasacase-dependentoptimizationproblemthat
ismainlyinfluencedbytheregulatoryenvironmentandthelevelofriskappetitewithin
the institution. Consequently, this positions fairness as a continuous process that must
beintegratedholisticallythroughoutthedeploymentpipeline,ratherthancorrectedata
singlestage,asalreadyhighlightedbyDasetal.(2023).
4.3. Regulatory,Ethical,andGovernanceFoundationsforFairAICreditScoring(RQ3)
IntheUnitedStates,theEqualCreditOpportunityAct(ECOA)andtheFairCredit
ReportingAct(FCRA)havecollectivelyimposedobligationstoensureequaltreatment
acrossprotectedgroups,andmoreimportantly,toprovide“adversedecisionjustifications”
withinstricttimelines(Kumaretal.,2022).Thesestatutoryrequirementsimplicitlymandate
interpretableAIsystemscapableofsupportingsupervisoryexaminationsandconsumer
recourse. Similarly,inEurope,modelsthatoperateopaquelyandfailtoprovideadequate
justificationforalgorithmicallydeterminedresultsweresubjectedtomistrust,viewedas
presentingheightenedbiasrisks,andclassifiedashigh-riskapplications(Langenbucher,
2020). Accordingly,theEuropeanUnionenforcedfairness-through-explainabilityrequire-
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 21of36
mentsundertheforthcomingAIAct, emphasizingtransparencyandadequatefairness
measures(Perryetal.,2023). Additionally,privacylawssuchasGDPRintersectwiththese
fairnessobligations,assensitiveattributesmaydirectlyorindirectlyinfluenceoutcomes,
posingdiscriminatoryrisksifleftunmitigated(Ridzuanetal.,2024).
Beyond Western regulatory frameworks, the ASEAN region also experienced the
riseofgovernanceapproachesthatprioritizefairnessinthealgorithmiclendingprocess,
withadditionalemphasisonhumanoversight(Lainez&Gardner,2023). Similartothe
EUAIActproposal,ASEANpolicyguidanceencouragestheHITLreview,particularly
in high-stakes and credit scoring domains, while also stressing explainability as a key
enablerforasupervisedevaluation(Ridzuanetal.,2024). Thismakeshumanintervention
central to validating outcomes and correcting undesired results. While these laws and
actsreferencedintheliteraturemightseemlessprescriptive,theysignalagrowingglobal
convergencetowardresponsibleAIcreditscoring,withnotablevariationinmaturityand
enforcementintensity. However,acrossmultiplejurisdictionalsettings,theseexpectations
converge on the principle of fairness in algorithmic decision-making, which cannot be
achievedwithoutconsciouslyadoptingAIsystemsthatprovideadequateexplainability.
Explainabilityservesasthemechanismthroughwhichdiscriminatoryriskscanberevealed,
adverseeffectscanbejustified,and,inthemostseverecases,correctedthroughhuman
oversight. Thus,itfunctionsnotmerelyasatransparencytoolbutasapivotalenablerfor
equity,accountability,andtheethicaldeploymentofAI(Langenbucher,2020).
TheincludedliteratureprovidesricherdetailforWesternandASEANregions,whereas
coveragebeyondthesesettingsbecomescomparativelysparseandfragmented. Inthese
cases, explicit governance and privacy references appear less frequently and are often
discussedatahigherlevelofabstraction. Forexample, additionalevidencefromother
Asian settings includes institutional governance signals, such as the Bank of Indonesia
supportingcredit-relateddecision-makingthroughMSMEprofiling(Hartomoetal.,2025)
andHongKongSARbankingguidanceonconsumerprotectionandhigh-levelAIusage
principles(Ridzuanetal.,2024). WithinASEAN,Vietnamprovidescomparativelyricher
legal framing, where algorithmic credit scoring is described as expanding amid weak
oversight,motivatingproposalsforstrongersafeguards,includinglimitsondatacollection,
consumer rights to explanation and appeal, and inspection powers by regulators such
astheStateBankofVietnam,togetherwithexplicitobligationsalignedtopersonaldata
protectionsuchasconsent,correction,deletionafteruse,andnotificationofthird-party
transfers(Lainez&Gardner,2023).InAfrica,onestudynotesthatcreditregulatorsinSouth
Africarequirecreditdecisionmodelstoprovidehuman-understandableinterpretations
(Hlongwaneetal.,2024),whileevidencelinkedtoLatinAmericahighlightsthatregulatory
and privacy requirements constrain the availability of comprehensive public financial
datasetsforresearchandbenchmarking,particularlyinBrazil(Valdrighietal.,2025).
Nonetheless, the literature increasingly shifts from treating fairness, often framed
throughanti-discriminationandconsumerprotectionexpectations,andexplainabilityas
optionaladd-onstorecognizingthemasfoundationalnecessitiesinAIcreditscoring,re-
flectinghowgloballawsandregulatorycontextsareshapingalgorithmicdecision-making.
Although explainability and fairness were addressed separately in most of the works
included herein, the reviewed studies consistently emphasize their conceptual interde-
pendence(Langenbucher,2020). Modelexplainabilityconstitutestheoperationalbridge
between fairness goals, compliance and human judgment and thereby supports audit-
ing,adverse-actionreasoning,andregulatorydisclosure(Dasetal.,2023).Althoughmost
reviewedstudiesaddressthesepillarsseparately,theworkofHickeyetal.(2020)opera-
tionalizedtheroleofexplainabilitytosupportfairnessinthelendingprocess. Theyargued
thatwhilepost-hocexplainabilityiswidelyadopted,itdoesnotitselfresolvefairnessissues
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 22of36
butratherguidestheiroperationalization. Toaddressthis,theyproposedaSHAP-based
regularizationtermthatpenalizespredictionscorrelatedwithprotectedattributes. This
penaltywasincorporatedintothemodel’slossfunctiontodiscourageitfromprovidingpre-
dictionsthathighlydependonprotectedattributes. Thisadversarialtechniqueconstrains
theattributionstoforcefairnessthroughexplainability,therebyservingasthemechanism
thatdirectlyexposesandregulatesamodel’sdependenceonprotectedattributes.
Insupportoffairness,however,theEUAIAct,aswellasECOA,explicitlyempha-
size the right to contest adverse action notices, extending auditors’ ability to challenge
automatedoutcomesandobtainmeaningfulreconsiderationtoensureessentialprocedu-
ral safeguards (Kumar et al., 2022; Langenbucher, 2020). This captures a key idea that
explainability is not merely for consumers but for supervisory examination and audit
trails,enablingindividualstoappealorseekreconsiderationwhenoutcomesaredoubtful.
Theconceptofchallengingoutcomesthroughhumanoversightandprovidingmeansto
correctunintentionaladverseoutcomesalignswellwiththequalitativestudyconducted
byKuiperetal.(2021),wheretheymanagedtoinvestigatethedisparitybetweenpractice
andlegalframeworksconcerningexplainability. Theyreportedthatwheninterpretability
isinherent,additionalexplainabilitybecomeslesscritical. However,theyalsonotedthat
explainabilitybecomesevidentlycrucialwhenadvancedAImodelsproduceresultsthat
conflictwiththeoutcomesmadebytraditionalmodels,encouraginghumanintervention
toactasapotentialethicalsafeguard.
In addition, given the fairness–performance trade-off, human-in-the-loop (HITL)
oversight can be operationalized as a recurring governance mechanism across the fair-
nesspipeline,ensuringthathumanjudgmentremainsembeddedthroughoutmodelde-
velopment and deployment. First, HITL can be applied between pre-processing and
in-processingstagestocertifyaugmentedandrebalanceddatasetsandverifythataugmen-
tationdoesnotamplifyhistoricalbiasthroughhistoricalrepaymentrecords,particularly
giventhatleakageofprotectedattributesthroughproxiesisaknownriskincreditscor-
ing(Dasetal.,2023).Second,HITLcansupportmodelselectionduringin-processingby
determininganappropriatetrade-offamongParetonon-dominantsolutionsreturnedby
fairness-awarelearningtechniques,aligningwiththefairness–performancetensiondis-
cussedinRQ2andenablinginstitutionstoselectmodelsthatsatisfyregulatoryexpectations
withoutincurringunjustifiedperformancedegradation. Lastly,HITLremainsessentialin
post-processingasacorrectivelayerthatmitigatesresidualorleakedbiasbyreviewing
flaggedoutcomesandoverridingadversedecisionsthatconflictwithfairnesspoliciesor
governancerequirements. Together,theseoperationalrolesdemonstratethatHITLisnot
merelyanoptionalinterventionbutapracticalgovernancelayerthatsupportscertifiable
fairnessandaccountabilityunderrealisticdeploymentconditions.
Insummary,whilesupervisoryframeworksdonotexplicitlystatehowfairnessand
explainabilitymustbeenforcedtoensureethicaldeployments,theyplayedapivotalrole
inshapingmoderncreditscoring. Initially,itstartedbymandatingjustificationofadverse
effectsandenablingrecoursemechanisms,butfurtherextendedbeyondconsumer-facing
transparencytoenablingcontestingandcorrectingunintendedresultsthatpotentiallylead
todiscriminatoryeffects.Moreover,asthelegalsystemsprioritizefairnessandexplain-
abilityequally,theyalsounveilawell-establishedtiebetweenthetwo. Fairnessmustbe
operationalizedthroughinterpretableandcontestableAIsystems,withhumanjudgment
servingastheethicalsafeguardthatensuresalignmentwithregulatoryandsocietalexpec-
tations. Therefore,regulatoryframeworksandethicalgovernancedonotmerelyinfluence
fairnessinterpretation;rather,theystructurallyintegrateexplainabilityasthemechanism
throughwhichfairnessisevaluated,enforced,andethicallyoperationalizedinAIcredit
scoringsystems.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 23of36
5. GapsandFutureDirections
Despitevariouseffortstoaddressperformance,fairness,andexplainabilityasthree
core pillars in the ethical deployment of AI-based credit scoring, several gaps persist
thatrequirefurtherinvestigation. Fromatechnicalandmethodologicalstandpoint, fu-
tureresearchmustmovebeyondpost-hocexplainabilitytodevelopstandardizedframe-
worksthatincorporateexplainabilityasamodelconstraint,enablinga“fairness-through-
explainability” paradigm that reduces model opacity. This paradigm aligns well with
anticipatedregulatoryrequirements,suchastheabilitytodetectbiasinresults,including
those caused by proxy, protected attributes, correct adverse outcomes through human
oversight, and justify adverse decisions to consumers, all of which cannot be achieved
withoutestablishingstricttiesbetweenfairnessandexplainability. Thistransitionredefines
explainabilityfromatechnicaladd-ontoameaningfulcapabilitythatfacilitatesfairness
andinviteshumanjudgmentwhennecessary.
Fromaregulatoryandauditingperspective,althoughmanystudiesacknowledgethe
importanceofhuman-in-the-loop(HITL)oversight,itremainsunder-specifiedintermsof
practicalimplementation. Inparticular,theliteraturerarelydefinesmeasurableescalation
triggers such as borderline cases, low-confidence predictions, or fairness-related flags,
standardized reviewer actions, or mechanisms for incorporating human feedback into
modelmonitoringandgovernance. FutureworkshouldthereforeformalizeHITLasan
operationalprotocolwithincreditscoringpipelines,ensuringtraceablereview,contesta-
bilityofadverseoutcomes,andconsistentalignmentwithlocalcomplianceandauditing
requirements.Thisisespeciallyimportantwhenfairnessconstraintsintroduceperformance
trade-offs,wherehumangovernanceisneededtojustifymodeladoptiondecisionsunder
institutionalrisktolerance.
Furthermore, while the conflict between explainability and performance is widely
debated, it is rarely quantified. Since there are no explicit legal mandates dictating the
choicebetweeninherentlyinterpretableandblack-boxmodels,itsignalstheneedformore
standardizedmethodologiesthatquantifytheperformancelossincurredwhencompro-
misingperformanceformodeltransparency. Reportingpotentiallossinperformancefor
inherentlyinterpretablemodelscanserveaspracticalguidanceforlendinginstitutions,
enablingthemtoselectbetweentransparentandblack-boxmodelsandjustifythemove
towardblack-boxesifnecessary,allofwhichdependheavilyonthelevelofrisktolerance
andappetite.
Inaddition,giventhatnofairnessmetricormethodisuniversal,andsinceregulatory
frameworkstypicallymandatefairnessoutcomeswithoutexplicitlyspecifyingtechnical
metrics, it is anticipated that future work must focus on interpolating and reconciling
incompatiblefairnessmetrics,ensuringcontext-awaremetricandmethodologicalselection
thatalignswiththelegaldefinitionofnon-discriminationacrossdifferentjurisdictional
settings. Thisincludesdeterminingwhichmetric,orcombinationthereof,alignswellwith
legaldefinitionsthatconcernnon-discrimination.
Overall, the most significant gap would be the absence of standardized AI credit
scoringframeworksthatjointlyoptimizeallthreepillarssimultaneouslywhileestablishing
well-grounded,structuraltiesbetweenthem. Currentmethodsofteninvolvetrainingfor
performance,thenincorporatingexplainabilitymethods,andthenadjustingforfairness,
wheninreality,thesedimensionsintersectacrossallstagesofthedeploymentpipeline.
Therefore,futureresearchmustfocusonproposingunified,multi-objectiveframeworksthat
treatperformance,fairness,andexplainabilityasinterdependentconstraints,addressing
HITLandregulatoryrequirementsconcurrently.
Finally,thissystematicreviewisintendedtoserveasafoundationforafutureapplied
studyaimedatdevelopingandvalidatinganAIcreditscoringmodelthatoperationalizes
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 24of36
the review conclusions within a deployable pipeline. While this work is an evidence
synthesis and does not propose a deployable system, these findings will guide model
selection under practical constraints, support integrating explainability as a structural
requirementratherthanapost-hocadd-on,andevaluatefairnessandperformancestability
underrealisticconditionsthatsupporthumanjudgmentwhennecessary.Suchworkwould
enable empirical verification of unified, multi-objective credit scoring frameworks that
alignperformance,fairness,explainability,andHITLrequirementswithregulatoryand
auditingexpectations.
6. Conclusions
Thissystematicliteraturereview(SLR)synthesizes43high-qualityacademicpapers
publishedbetween2020and2025,focusingontheintersectionofperformance,fairness,
andexplainabilityinAIcreditscoring. ByadheringtoPRISMAguidelinesandemploying
adetailed3Rs&Qappraisalframework,thereviewestablishedthatwhilecreditscoring
modelscontinuetograpplewithperformancetrade-offs,explainabilityhasbecomethe
dominantresearchpillarsince2023. Thisshiftislargelydrivenbyregulatoryframeworks,
suchastheEUAIAct,ECOA,andASEANprinciples,whichmandateinterpretablesystems
capableofdeliveringadversedecisionjustifications,therebyreinforcingtheneedforhuman
oversight. Althoughthetrade-offbetweenexplainabilityandperformancepersists,the
choicebetweeninterpretableandblack-boxmodelsisshapedprimarilybytherisktolerance
levelofalendinginstitution,andthistrade-offisscarcelymeasuredacrosstheliterature.
In relation to the research questions, the review finds that (RQ1) the widely cited
trade-offbetweenexplainabilityandperformanceislargelyassumedratherthanempiri-
callydemonstrated;thelimitedstudiesthatquantifythisrelationshipshowonlymarginal
differences between inherently interpretable and black-box models, indicating that the
choicebetweenthemisdeterminedprimarilybyaninstitution’srisktoleranceratherthan
measurablepredictiveloss. Incontrast,thetrade-offbetweenperformanceandfairness
isconsistentlyconfirmedacrosstheliterature: fairnessistreatedasamulti-objectiveopti-
mizationproblem,andaggressiveenforcementoffairnessconstraintsresultsinsignificant
performancedegradation,whereasmoderatefairnessadjustmentstendtoyieldbalanced
improvements. (RQ2)Biasoriginatesprimarilyfromhistoricaldatapatterns,classimbal-
ance,andtheinclusionofprotectedattributes,withmitigationstrategiesappliedacross
different stages differing in strengths, but no universally optimal solution. (RQ3) Reg-
ulatoryandgovernanceframeworksincreasinglyemphasizeexplainabilityandhuman
oversight,yetexistingstudieshavenotfullyintegratedtheserequirementsintounified,
end-to-endcreditscoringpipelines.
Inaddition,despitesignificantresearchintomulti-objectiveoptimizationforbalancing
performanceandfairness,thecurrentliteraturepredominantlyreliesonfragmentedand
sequentialapproaches. Modelsareoftenoptimizedforaccuracyfirst,withfairnessand
explainabilityappliedasadjustments. Thisdeficiencyrepresentsthemostpressingfinding
ofthereview,demonstratingtheabsenceofaunified,holisticAIcreditscoringframework
thatco-optimizesallthreepillarssimultaneouslyacrossallstages. Suchsequentialmethod-
ologiesareinadequateformeetingthestrictcomplianceexpectationsofmodernregulatory
environmentsandfailtoembedtransparencyfromthegroundup.
Toaddressthiscriticalgap,thereviewrecommendsthreekeydirectionsforfuture
research. First,scholarsmustfocusondevelopingnovel,unifiedco-optimizationframe-
worksthattreatperformance,fairness,andexplainabilityasinterdependentconstraints
throughouttheentiremodeldesignlife-cycle. Second,researchmustadvancebeyondsta-
tisticaldefinitionsoffairnessbydevelopingandvalidatingcontextualizedfairnessmetrics
tailoredtospecificlendingmarketsandtheirsocio-economiceffectsonprotectedgroups.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
25of36
Finally,empiricalinvestigationsintohuman-in-the-loop(HITL)integrationarerequiredto
examinehowauditorsandcomplianceofficerscaneffectivelyleverageexplainabilityto
ensureregulatorycomplianceandproducecredible,real-worldoutcomes.
AuthorContributions:Conceptualization,R.B.;methodology,R.B.,N.H.andW.E.;software,R.B.;
validation,N.H.andW.E.;formalanalysis,R.B.;investigation,R.B.;resources,W.E.;datacuration,
R.B.;writing—originaldraftpreparation,R.B.;writing—reviewandediting,N.H.andW.E.;supervi-
sion,N.H.andW.E.;projectadministration,N.H.Allauthorshavereadandagreedtothepublished
versionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement: Thisstudyisbasedonthepreviouslypublishedliterature. Nonew
datasetsweregeneratedoranalyzed.Allreferenceddatasetsarepubliclyavailablefromthesources
citedinthecorrespondingstudies.Thestudyselectionprotocolandappraisalcriteriaareavailable
fromthecorrespondingauthoruponreasonablerequest.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
AppendixA
TableA1.Full-textexcludedstudiesandreasonsforexclusion(Part1:IDs1–8).
| ID Author(s) | Title | ExclusionReason | PRISMABucket |
| ------------ | ----- | --------------- | ------------ |
Excludedduetooverlappingscope,asexplainabilityis
Designingafeatureselection
appliedmainlyaspost-hocSHAP-basedfeature
1 Zachariasetal.(2022) methodbasedonexplainable Overlappingscope
attributionwithinaperformance-drivenpipelinethatis
artificialintelligence
alreadywellrepresentedamongtheincludedstudies.
Excludedduetooverlappingscope,asasurvey-style
|     | AReviewofGenderBias | reviewsummarizingbiasmitigationstrategies,whichis |     |
| --- | ------------------- | ------------------------------------------------- | --- |
Corrales-Barqueroetal.
2 MitigationinCredit alreadycoveredbymorerecentorsynthesis-relevant Overlappingscope
(2021)
|     | ScoringModels | includedsources,contributinglimitedadditionalevidence |     |
| --- | ------------- | ----------------------------------------------------- | --- |
tothereviewobjectives.
Excludedduetooverlappingscope,asthestudyis
|     | TowardsFairAI:MitigatingBias | primarilyasurveysummarizingfairnessandbias |     |
| --- | ---------------------------- | ------------------------------------------ | --- |
deCastroVieiraetal.
3 inCreditDecisions—A mitigationwithoutprovidingdistinctempiricalevidence Overlappingscope
(2025)
|     | SystematicLiteratureReview | orintegratedanalysisacrossperformance,fairness,and |     |
| --- | -------------------------- | -------------------------------------------------- | --- |
explainabilitybeyondincludedworks.
Excludedasoutofscope,asitaddressesAIinfinancial
AIintegrationinfinancial
|                       |                              | servicesbroadlyratherthanAI-basedcreditscoringand   | Didnotmeet  |
| --------------------- | ---------------------------- | --------------------------------------------------- | ----------- |
| 4 Vukovic´etal.(2025) | services:asystematicreviewof |                                                     |             |
|                       |                              | doesnotprovidecreditscoring-specificevidencealigned | eligibility |
trendsandregulatorychallenges
withtherevieweligibilitycriteria.
Excludedduetooverlappingscope,asthestudy
AGeneralArchitecturefora
emphasizesaperformance-orientedarchitecturewith
TrustworthyCreditworthiness-
5 Cornacchiaetal.(2023) explainabilitytreatedprimarilyasapost-hoccomponent, Overlappingscope
AssessmentPlatforminthe
overlappingwithincludedworksaddressingsimilar
FinancialDomain
post-hocexplainabilityconfigurations.
|     | Cost-awareCredit-scoring | Excludedasperformance-orientedonly,focusingonclass |     |
| --- | ------------------------ | -------------------------------------------------- | --- |
FrameworkBasedon imbalancehandling,resampling,andfeatureselectionfor Didnotmeet
6 Mouetal.(2024)
ResamplingandFeature cost-awareoptimizationwithoutsubstantivetreatmentof eligibility
|     | Selection | fairnessorexplainabilityasprimaryreviewpillars. |     |
| --- | --------- | ----------------------------------------------- | --- |
Excludedasperformance-orientedonly,asitevaluates
Ensemblemethodsforcredit
|                  |                              | ensemblelearningprimarilyforpredictiveperformance    | Didnotmeet  |
| ---------------- | ---------------------------- | ---------------------------------------------------- | ----------- |
| 7 Caoetal.(2021) | scoringofChinesepeer-to-peer |                                                      |             |
|                  |                              | withoutexplicitfairness,explainability,orregulatory/ | eligibility |
loans
HITLconsiderationsalignedwiththereviewscope.
|     | A‘divideandconquer’reject | Excludedasreject-inference/performance-oriented,where |     |
| --- | ------------------------- | ----------------------------------------------------- | --- |
rejectinferenceisusedtoaddresssampleselectionbias
|                 | inferenceapproachleveraging |                                        | Didnotmeet  |
| --------------- | --------------------------- | -------------------------------------- | ----------- |
| 8 Wuetal.(2025) |                             | andimprovepredictiveperformancewithout |             |
|                 | graph-basedsemi-supervised  |                                        | eligibility |
protected-attributefairnessanalysisorexplainability
learning
objectivesalignedwiththereviewsynthesisgoals.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
26of36
TableA2.Full-textexcludedstudiesandreasonsforexclusion(Part2:IDs9–15).
| ID Author(s) | Title | ExclusionReason | PRISMABucket |
| ------------ | ----- | --------------- | ------------ |
Excludedasperformance/sample-biasoriented,focusing
CombatingSamplingBias:A
|                   |                             | onaccepted-onlysamplingbiasusingself-trainingwithout    | Didnotmeet  |
| ----------------- | --------------------------- | ------------------------------------------------------- | ----------- |
| 9 Liaoetal.(2022) | Self-TrainingMethodinCredit |                                                         |             |
|                   |                             | explicitlyaddressingfairnessacrossprotectedattributesor | eligibility |
RiskModels
explainabilityascoreobjectives.
Excludedasperformance-orientedonly,proposing
cost-sensitivereinforcementlearningtooptimizecredit
|     | Cost-sensitivereinforcement |     | Didnotmeet |
| --- | --------------------------- | --- | ---------- |
10 C-Rellaetal.(2025) riskdecisioningwithoutoperationalizingfairness,
|     | learningforcreditrisk |     | eligibility |
| --- | --------------------- | --- | ----------- |
explainability,orregulatory/HITLrequirementscentralto
therevieweligibilitycriteria.
Excludedasnoteligible,asitisprimarilyalegal/policy
discussionofautomationandAIethicswithoutcredit
|     | Humancontroloverautomation: |     | Didnotmeet |
| --- | --------------------------- | --- | ---------- |
11 Koulu(2019) scoring-specificempiricalmethodsoroperationalevidence
|     | EUpolicyandAIethics |     | eligibility |
| --- | ------------------- | --- | ----------- |
supportingsynthesisacrossperformance,fairness,and
explainability.
Excludedasreject-inference/performance-oriented,
|     | Inferringtheoutcomesof | focusingonoutcomeinferenceforrejectedapplicantsto |     |
| --- | ---------------------- | ------------------------------------------------- | --- |
Didnotmeet
12 Z.Lietal.(2020) rejectedloans:anapplicationof enhancepredictionperformance,withfairnessand
eligibility
|     | semisupervisedclustering | explainabilitynottreatedascentral, |     |
| --- | ------------------------ | ---------------------------------- | --- |
operationalizedobjectives.
Excludedduetooverlappingscope,asXAIisapplied
BoostingCreditRiskData
mainlyfordata/modeldiagnostics,andexplainabilityis
13 Tiukhovaetal.(2025) QualityUsingMachineLearning Overlappingscope
treatedaspost-hocanalysis,closelyoverlappingwith
andeXplainableAITechniques
includedSHAP-post-hocexplainabilitystudies.
Excludedasoutofscope,asittargetsfinancialrisk
Adata-drivenexplainable
|                    |                             | detectionratherthancreditscoring/creditworthiness | Didnotmeet  |
| ------------------ | --------------------------- | ------------------------------------------------- | ----------- |
| 14 W.Lietal.(2022) | case-basedreasoningapproach |                                                   |             |
|                    |                             | assessment,anditdoesnotalignwiththereview’s       | eligibility |
forfinancialriskdetection
domain-specificeligibilitycriteria.
|     | EnhancingFairnessand | Excludedduetoinsufficientoperationalizationoffairness, |     |
| --- | -------------------- | ------------------------------------------------------ | --- |
ChackoandAravindhar AccuracyinCreditScore asfairnessisreferencedbutnotclearlydefinedusing Didnotmeet
15
(2025) Analysis:ANovelFramework explicitmetricsorevaluationprotocolsthatsupport eligibility
|     | UtilizingKernelPCA | structuredsynthesisundertherevieweligibilitycriteria. |     |
| --- | ------------------ | ----------------------------------------------------- | --- |
AppendixB
TableA3.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part1:IDs1–6).
| ID Author(s) | Title | Summary | RelatedRQs |
| ------------ | ----- | ------- | ---------- |
Examinestrade-offsbetweenfairnessandprofitabilityin
creditscoring.IntegratesfairnessmetricsintoMLpipelines
|     | FairnessinCreditScoring: | andevaluatespre-,in-,andpost-processingmethods |     |
| --- | ------------------------ | ---------------------------------------------- | --- |
1 Kozodoietal.(2022) Assessment,Implementationand (reweighing,prejudiceremover,adversarialdebiasing,reject RQ1,RQ2
|     | ProfitImplications | option)acrosssevendatasets.Concludesfairnesscan |     |
| --- | ------------------ | ----------------------------------------------- | --- |
improvewithoutmajorperformanceloss,supporting
regulatorycomplianceandethicallending.
Explorestheexplainability–performancetrade-offincredit
scoring.Comparesblack-boxandinterpretablemodels
|     | CostofExplainabilityinAI:An | (XGBoost,NN,LR,GAMs)underECBcompliance. |     |
| --- | --------------------------- | --------------------------------------- | --- |
2 Dessainetal.(2023) ExamplewithCreditScoring Introducesisotonicsmoothingtoalignexpertjudgement RQ1,RQ3
|     | Models | withregulatorymaster-scalegrading.FindsGAM-style |     |
| --- | ------ | ------------------------------------------------ | --- |
modelsachievenear-black-boxaccuracywhilepreserving
inherentinterpretabilityandmeetingregulatorystandards.
Assessesalgorithmicbiasandcompares12mitigation
strategiesacrossfivefairnessmetricsusingGermanand
Romaniandatasets.Highlightsthatnosinglefairness
AlgorithmicDecisionMaking measuresatisfiesfairness,performance,andprofitability
| 3 Moldovan(2023) |     |     | RQ1,RQ2,RQ3 |
| ---------------- | --- | --- | ----------- |
MethodsforFairCreditScoring simultaneously.Showsincompatibilitiesamongmetrics
(independence,separation,sufficiency)andstresses
regulatoryambiguityandtheneedforbalanced,
multi-methodapproaches.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 27of36
TableA3.Cont.
ID Author(s) Title Summary RelatedRQs
IntroducestheFairInterpolationMethod(FAIM),a
post-processingalgorithmusingoptimaltransportto
BeyondIncompatibility:Trade-offs
interpolatebetweencalibration,balanceforpositives,and
BetweenMutuallyExclusive
4 Zehlikeetal.(2025) balancefornegatives.MotivatedbytheEUAIAct,it RQ1,RQ2,RQ3
FairnessCriteriainMachine
addressesfairnessincompatibilityandlegalambiguity,
LearningandLaw
emphasizingregulatorinvolvementandhumanoversight
fortrade-offmanagementacrossjurisdictions.
SituatesfairnesswithinECOA,FCRA,andsupervisoryrules;
distinguishesindividualvs.groupfairness.Arguesbiascan
enterpre-,in-,orpost-trainingandcataloguesdatasetbiases
5 Dasetal.(2023) AlgorithmicFairness RQ2,RQ3
andmetrics(e.g.,DI,EO,equalizedodds,predictiveparity).
Advocatesasystemicapproachcombiningdataquality,
interpretability,andregulatoryalignment.
Analyzeseffectsofclassimbalanceandprotected-groupratios
PropertiesofFairnessMeasuresin onfairnessmetricsusingtheUCIAdultdataset.Finds
theContextofVaryingClass StatisticalParityDifferenceandDisparateImpactarehighly
6 Brzezinskietal.(2024) RQ2
ImbalanceandProtected sensitivetoimbalance,whileEqualOpportunityandAverage
GroupRatios OddsDifferencearemorestable.Recommendscontextual
evaluationcombiningfairnessandperformanceindicators.
TableA4.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part2:IDs7–12).
ID Author(s) Title Summary RelatedRQs
ExaminesregulatoryandethicalchallengesinAI-driven
creditscoringunderGDPR,ECOA,FCRA,andGLBA.
Highlightsprivacyrisks,proxydiscrimination,and
Langenbucherand ResponsibleAICreditScoring–A
7 fairness–accuracytrade-offs.Recommendstransparency, RQ1,RQ3
Corcoran(2022) LessonfromUpstart.com
fairnessaudits,human-in-the-loopoversight,andregulator
collaborationtoensurecompliantandexplainablelending
decisions.
OutlinesalegalframeworkforresponsibleAIcreditscoring
basedontransparency,fairness,andaccountability.Warns
ResponsibleA.I.-basedCredit opaquemodelscanconflictwithGDPR’s“righttoexplain.”
8 Langenbucher(2020) RQ3
Scoring–ALegalFramework Recommendsembeddinginterpretability,validatingfairness
throughoutmodelphases,enforcinghumanoversight,and
assigningaccountabilityrolesforlawfuldeployment.
Addressesbias,transparency,andrejectinferencein
AI-basedcreditscoringacrossGerman,Taiwanese,and
HomeCreditdatasets.Discussesbiasorigins,fairness
BestPracticesforResponsible
9 Valdrighietal.(2025) metrics(groupandindividual),andmitigationacrosspre-, RQ1,RQ2
MachineLearninginCreditScoring
in-,andpost-processing.Highlightstransparencytools
(LIME,SHAP,PD,ICE)andemphasizesinclusive,
responsibledeployment.
ReportsqualitativefindingsfromDutchbanksand
regulatorsonintegratingXAIintocreditscoring.Defines
ExploringExplainableAIinthe explainabilityastransparencyintomodelreasoning,data,
10 Kuiperetal.(2021) FinancialSector:Perspectivesof anddesign.Notesrelianceoninterpretabletraditional RQ1,RQ3
BanksandSupervisoryAuthorities models,humansafeguards,andphaseddeployment.
Positionsexplainabilityasessentialforethical,accountable,
regulatory-alignedAI.
Highlightsfairnessasjurisdiction-dependent.UsesPareto
principlestobalancegroup-andoverall-levelaccuracies
TheNeedforTransparent
withhuman-in-the-loopoversight.Showsintersecting
BalashankarandLees DemographicGroupTrade-Offsin
11 protectedattributesreducesamplesizesanddegrade RQ1,RQ2,RQ3
(2022) CreditRiskandIncome
accuracy,motivatingdataimprovements.Advocates
Classification
transparenttrade-offvisualizationtoalignfairness,
performance,andsocialobjectives.
Quantifiesaccuracy–interpretabilitytrade-offsintabular
learningusing45datasets.Findslessthan4%accuracyloss
ExploringAccuracyand
betweenblack-boxandinherentlyinterpretablemodels.
InterpretabilityTrade-offinTabular
12 Amekoeetal.(2024) ProposesaTabSRAattention-basedensembleinspiredby RQ1,RQ3
LearningwithNovel
GAMs,offeringfeature-levelinterpretabilityandstable
Attention-basedModels
performance;arguesforinherentinterpretabilityin
high-stakesdomains.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 28of36
TableA5.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part3:IDs13–18).
ID Author(s) Title Summary RelatedRQs
Formulatesfairness–accuracytrade-offsasastochastic
multi-objectiveoptimizationproblem.Proposesthe
AccuracyandFairnessTrade-offsin StochasticMulti-Gradient(SMG)algorithmusingDisparate
S.LiuandVicente
13 MachineLearning:AStochastic ImpactandEqualOpportunityasconstraints.Demonstrates RQ1,RQ2
(2022)
Multi-objectiveApproach ParetofrontiersontheUCIAdultdataset,showingtension
betweenfairnessandaccuracydrivenbyproxyand
protectedattributes.
Modelsgroupfairnessasmulti-objectiveoptimizationwhere
eachsensitivegroupdefinesafairnessobjective.Proposes
MinimaxParetoFairness:A Minimum-MaximumParetoFairness(MMPF)usingneural
14 Martinezetal.(2020) RQ1,RQ2
Multi-objectivePerspective networkswithpost-hoccorrectionstoreduceriskdisparity.
EvaluatedonGermanCreditandAdultIncomedatasets
withaccuracy,Brierscore,andcross-entropymetrics.
ProposesFair-CMNB,afairness-andimbalance-aware
MixedNaïveBayesmodelforstreamingcreditdatausing
Fair-CMNB:Advancing
multi-objectiveoptimization.Introducesdynamicinstance
BadarandFisichella Fairness-AwareStreamLearning
15 weightingtoprioritizeminorityupdatesandcontrol RQ1,RQ2
(2024) withNaïveBayesand
discrimination.Reportsimprovedaccuracyandfairness
Multi-ObjectiveOptimization
overbaselines,emphasizingscalabilityandpracticalityfor
high-stakescreditscoring.
AppliescausalMLwithBayesiannetworkstomodel
CreditRiskPredictionBasedon cause–effectrelationsandenabletransparentdecision
CausalMachineLearning:Bayesian analysisviaDAGs.UsesSMOTEandL1regularizationfor
16 J.Liuetal.(2024) RQ1,RQ2,RQ3
NetworkLearning,Default imbalancehandlingandfeatureselection.Supports
Inference,andInterpretation interpretable,regulation-orientedwhat-ifanalysisacrosssix
realdatasets.
ProposesanadversarialSHAPframeworklinkingfairness
andexplainabilitybypenalizingpredictionscorrelatedwith
protectedattributesviaSHAP-basedregularization.Uses
FairnessbyExplicabilityand
17 Hickeyetal.(2020) surrogateauditingtomirroroversight.Demonstrates RQ1,RQ2,RQ3
AdversarialSHAPLearning
improvedfairnessandinterpretabilityonAdultIncomeand
proprietarycreditdatasetswhilemaintainingstrong
predictiveperformance.
AnalyzesregulatorygapsandethicalrisksinVietnam’s
AlgorithmicCreditScoringin adoptionofalgorithmiccreditscoring.Highlights
LainezandGardner Vietnam:ALegalProposalfor discrimination,bias,opacity,andprivacyconcernsunder
18 RQ3
(2023) MaximizingBenefitsand FCRA,ECOA,FCA,andtheEUAIAct.Advocatesstronger
MinimizingRisks legaloversightandinterpretabilitystandardstorestoretrust
andfairness.
TableA6.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part4:IDs19–24).
ID Author(s) Title Summary RelatedRQs
ProposesahybridCNN–XGBooststackingmodeltoimprove
EnhancingTransparencyand accuracyandinterpretabilityincreditscoring.UsesSHAP
FairnessinAutomatedCredit globalexplanationstoexaminefeatureeffectsontheLending
19 Nwaforetal.(2024) RQ1,RQ2
Decisions:AnExplainableNovel Clubdataset.Reportshighpredictiveperformancewhile
HybridMachineLearningApproach enhancingtransparencyandtrustinautomatedlending
decisions.
IntroducesNOTE,anon-parametricoversamplingapproach
combiningstackedautoencodersandconditionalWasserstein
NOTE:Non-parametric GANstoaddresssevereclassimbalance.EvaluatedonHome
20 S.Hanetal.(2024) OversamplingTechniquefor EquityandGiveMeSomeCreditdatasets;reportsimproved RQ1,RQ2
ExplainableCreditScoring accuracyoverADSGANandDeepSMOTE.UsesSHAPfor
globalinterpretability,linkingimbalancecorrectionwith
explainablecreditscoring.
ProposesBASL,abias-awareself-learningframework
addressingsamplingbiasfrommissingrejectedapplicants.
FightingSamplingBias:A Usesasemi-supervisedBayesianapproachtoiterativelylabel
21 Kozodoietal.(2025) FrameworkforTrainingand unlabeleddatawhilefilteringoutliers.AppliedtoMonedo’s RQ1,RQ2
EvaluatingCreditScoringModels real-worlddataset;recoversupto36%performancelossdueto
samplingbiasandoutperformsreweightingand
Heckman-stylemethods.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 29of36
TableA6.Cont.
ID Author(s) Title Summary RelatedRQs
ProposesahybridLSTM-basedframeworkcapturingtemporal
borrowerbehaviorforcreditscoring.UsesSMOTE,
CreditScoringPredictionUsingDeep
normalization,andone-hotencodingforimbalancehandling.
22 Shietal.(2025) LearningModelsintheFinancial RQ1,RQ2
Introducesahybridlosswithinterpretabilityregularization
Sector
enforcingfeaturesparsity,aimingtoretaintransparency
withoutrelyingonpost-hocexplainers.
ComparesSHAPwithcounterfactualmethodsfor
interpretabilityincreditscoring.UsesGeneticAlgorithmsto
MachineLearningInterpretabilityfor
generatecounterfactualsidentifyingminimalfeaturechanges
23 Bueffetal.(2022) aStressScenarioGenerationinCredit RQ1,RQ2
neededtoalteroutcomes.Linksinterpretabilitytorobustness
ScoringBasedonCounterfactuals
understressscenariosandhighlightshowcounterfactuals
exposesensitivedecisionboundariesandbias-pronefeatures.
AlignsalgorithmicfairnessresearchwithUS
EqualizingCreditOpportunityin anti-discriminationlaws(ECOA,FCRA,HMDA).Discusses
Algorithms:AligningAlgorithmic disparateimpact/treatmentaslegalfairnesscriteriaandthe
24 Kumaretal.(2022) RQ2,RQ3
FairnessResearchwithU.S.Fair roleofproxyattributesinbias.Advocatescausaland
LendingRegulation counterfactualanalysisandregulatoryoversightforequitable,
transparentAI-drivenlendingpractices.
TableA7.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part5:IDs25–30).
ID Author(s) Title Summary RelatedRQs
ProposesahybridADASYN–LCEmodelcombiningadaptive
Farmers’CreditRiskEvaluationwith resamplingandlocalcascadingensemblesformicrofinance
anExplainableHybridEnsemble creditscoring.UsesSHAPandLIMEforinterpretabilityand
25 Chaietal.(2025) RQ1,RQ2
Approach:ACloserLookin fairnessvalidation.Reportsimprovedrobustnessandvisibility
Microfinance forunderservedpopulationsthroughbalancedlearningand
explainableensemblemodeling.
IntegratesSHAPexplanationsintocreditscoringpipelines
usingXGBoostandRandomForestmodels.Improves
ANovelFrameworkforEnhancing
transparency,regulatoryalignment,andconsumertrustby
Hlongwaneetal. TransparencyinCreditScoring:
26 visualizingfeatureattributions.EvaluatedonTaiwaneseand RQ1
(2024) LeveragingShapleyValuesfor
HomeCreditdatasets,demonstratinginterpretable
InterpretableCreditScorecards
performancealignedwithexplainabilityexpectations
inlending.
ProposesIAIBS,combininglogisticregressionanddeep
AnInterpretableCreditRisk learningtohandleambiguousboundarysamples.UsesARPD
27 Zhangetal.(2025) AssessmentModelwithBoundary toclassifynoise/anomaliesandappliesSHAPfor RQ1
SampleIdentification interpretability.ReportsimprovedAUCwhileenhancing
transparencyviaboundary-awarepre-processing.
Compares1D-CNNandtransfer-learningBERTmodelsusing
openbankingtransactionsforcreditscoring.UsesSHAPto
ExplainingDeepLearningModelsfor
HjelkremandLange interpretdeepmodelsandsupportjustificationunder
28 CreditScoringwithSHAP:ACase RQ1
(2023) regulatorymandates.Findsthat1D-CNNoutperformsBERT
StudyUsingOpenBankingData
inAUCandBrierscore,emphasizingexplainabledeep
learningforcompliantcreditassessment.
Addressesmulti-classcreditriskpredictionusinghybrid
ensembles(LR,RF,SVM,NB,MLP)withSMOTEand
AHybridApproachtoCreditRisk
ADASYN.UsesMutualInformationtocaptureproxy
BulutandArslan AssessmentUsingBillPayment
29 interactionsandappliesSHAP/LIMEforinterpretability. RQ1,RQ2
(2025) HabitsDataandExplainable
Reportsstrongperformancewithtree-basedmodelsand
ArtificialIntelligence
highlightsexplainable,balancedriskassessmentin
alternative-datasettings.
ProposesanANNintegratingADASYNresamplingandFocal
Losstomitigateimbalance.TestedontheGermandataset;
AnExplainableADASYN-Based
AliShaheeandPatel reportsimprovedaccuracyandAUCoverbaselines.Uses
30 FocalLossApproachforCredit RQ1,RQ2
(2025) SHAPandLIMEforfeatureattribution,aimingtocombine
Assessment
predictiveperformancewithinterpretabilityincredit
assessment.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 30of36
TableA8.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part6:IDs31–36).
ID Author(s) Title Summary RelatedRQs
IntroducesaGA-basedcounterfactualexplanation
frameworkforblack-boxcreditmodels.Searches
neighbouringinstancesthatflippredictionswithminimal
Model-AgnosticCounterfactual
31 Dastileetal.(2022) featurechanges,exposingdecisionboundariesandpotential RQ1
ExplanationsinCreditScoring
biassources.ValidatedonGermanandHMEQdatasets,
supportingmodel-agnosticinterpretabilityfortransparency
andauditing.
ProposesVAE-INN,avariationalautoencoderguidedby
VAE-INN:VariationalAutoencoder weightedlosstocounterclassimbalanceinlatentspace.
withIntegratedNeuralNetwork AssignshigherweightstominorityclassestoreduceTypeII
32 Atif(2025) RQ1,RQ2
ClassifierforImbalancedCredit errors.TestedontheTaiwanesecreditdatasetandreports
Scoring improvedbalancedaccuracyandreliabilityover
SMOTE/ADASYN-basedbaselines.
CombinesTabTransformerwithweightedlosstoaddress
ANovelWeightedLoss classimbalancewhilepreservinginterpretability.Applies
TabTransformerIntegrating SHAPforglobalfeatureattribution.EvaluatedonGerman
33 Hartomoetal.(2025) RQ1,RQ2
ExplainableAIforImbalanced andBISAIDdatasets,reportingaccuracy/AUC
CreditRiskDatasets improvementsanddemonstratingexplainable,balanced
performancefortabularcreditscoring.
IntroducesMLMVS,astackingensemble(LR,MLP,RF,
KNN)withmulti-viewpartitioning(personal,behavioral,
AMulti-layerMulti-viewStacking historyfeatures).UsesLIMEforinstance-level
34 W.Hanetal.(2023) RQ1
ModelforCreditRiskAssessment interpretability.Reportsgainsinaccuracy,precision,and
specificityoverbaselines,supportinginterpretableensemble
learningfordefaultprediction.
DiscussesAIgovernanceinfinance,emphasizingregulation,
ethicalresponsibility,andhumanoversight.Identifieskey
AIintheFinancialSector:TheLine
challenges(privacy,fairness,accountability)andpositions
35 Ridzuanetal.(2024) BetweenInnovation,Regulationand RQ3
explainabilityascentralforhumandecision-making.
EthicalResponsibility
Advocatesgovernanceapproachesalignedwithsocietal
valuestofostertrustinregulatedfinancialAI.
ExamineswhetherAIcanexpandmortgageaccesswhile
managingbiasandequityconcerns.Warnshistoricaldata
AlgorithmsforAll:CanAIinthe
mayperpetuatediscrimination.RecommendsaligningAI
36 Perryetal.(2023) MortgageMarketExpandAccessto RQ2,RQ3
outcomeswithlegalandethicalframeworks,ensuring
Homeownership?
demographicfairness,transparency,andhumanoversightto
preventdisparateimpact.
TableA9.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part7:IDs37–43).
ID Author(s) Title Summary RelatedRQs
Proposesadeeplearningframeworkthatinjects
interpretabilityconstraintsintotrainingviamulti-objective
optimization.Usessoftconstraintsandweighted-sum
MulticriteriaInterpretabilityDriven
37 Repetto(2025) scalarizationtobalancecriteria.DemonstratesonthePolish RQ1
DeepLearning
bankruptcydatasetandvisualizeseffectsusingALEplots,
indicatinginterpretability-awaretrainingcansupport
generalizationinhigh-stakestasks.
Proposesfeature-weightadjustment,penalty-based
modeling,andahybridmethodtoenhanceinclusionin
SensitivityAnalysis:Improving
creditscoring.Evaluatesinclusivityandperformance
InclusiveCreditScoringAlgorithm
38 Sulastrietal.(2025) acrossextensivehyperparametercombinationsusing RQ1,RQ2
ThroughFeatureWeightand
XGBoost,CatBoost,RF,andDT.Improvesinclusionby
Penalty-BasedApproach
reweightingsensitivefeaturesbutnotesrisksof
dataset-specificoverfittingandlimitedgeneralizability.
ImplementsLightGBMwithLIMEandSHAPfor
global/localinterpretabilityincreditscoring.Uses
ExplainableAI-basedLightGBM
samplingandRFEtoaddressimbalanceand
PredictionModeltoPredictDefault
39 L.H.Lietal.(2025) dimensionalityontheLendingClubdataset.Reportsstrong RQ1
BorrowerinSocialLending
predictiveperformanceandprovidesareferencepipeline
Platform
forintegratingexplainabilitywithensemblemodelsin
sociallending.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
31of36
TableA9.Cont.
| ID Author(s) |     | Title | Summary |     | RelatedRQs |
| ------------ | --- | ----- | ------- | --- | ---------- |
Proposesacounterfactualexplanationmethodoptimizing
validityandsparsitytoimproveinterpretability.UsesGA
CounterfactualExplanationswith andPSOtofindminimalfeaturechangesthatalter
40 DastileandCelik(2024) MultiplePropertiesinCredit predictions.Highlightschallengessuchasdriftsensitivity RQ1,RQ3
Scoring andmissingdata,andpositionscounterfactualsasa
transparentalternativetofeature-importanceexplanations
forauditing.
Presentsanensembleframework(RF,AdaBoost,XGBoost,
LightGBM)withSMOTE-ENNforimbalancecorrection
EffectiveCreditRiskPrediction
andSHAPforinterpretation.EvaluatedonGermanand
| 41 ArulebaandSun(2024) |     | UsingEnsembleClassifiersWith |     |     | RQ1,RQ2 |
| ---------------------- | --- | ---------------------------- | --- | --- | ------- |
Australiandatasets;reportsimprovedrecall/specificityand
ModelExplanation
arguesbalanced,explainableensemblelearningimproves
generalizationandauditability.
ProposesanAutoMLframeworkintegratingLIMEforlocal
AnInterpretableAutomated interpretabilityofcomplexmodels.Reportsnear–deep
42 Patronetal.(2020) MachineLearningCreditRisk learningperformancewhilemaintainingtransparency RQ1
Model throughlocalperturbation-basedexplanations,supporting
expertvalidationandcontestabilityincreditriskdecisions.
AnalyzesAI’simpactonfinancialinclusionusingdatafrom
TheEffectofAI-enabledCredit overonemillionunderservedborrowers.Introducesweak
ScoringonFinancialInclusion: signals(featuresweaklytiedtofinancialstatus)tostudy
43 C.Lietal.(2024) RQ2,RQ3
EvidencefromanUnderserved inclusionandbiastrade-offs.Warnsprotectedattributes
PopulationofOverOneMillion mayamplifydiscriminationandarguesforbalanced
adoptiontoimproveaccesswhilemanagingequityrisks.
AppendixC
TableA10.Summaryoffairnessmitigationstrategiesincreditscoring(Part1:Rows1–6).
| Author | Category | Method | Mechanism | Strengths | Limitations |
| ------ | -------- | ------ | --------- | --------- | ----------- |
Smallerfairnessgainsthan
Model-agnostic;simple
|     |     |     | Adjuststrainingsampleweights |     | thestrongestpost- |
| --- | --- | --- | ---------------------------- | --- | ----------------- |
toapplybeforetraining;
Kozodoietal. sodisadvantagedgroupsreceive processingoptionintheir
|        | Pre-processing | Reweighing |                                | canreduce |                       |
| ------ | -------------- | ---------- | ------------------------------ | --------- | --------------------- |
| (2022) |                |            | higherinfluenceduringtraining, |           | comparison;mayrequire |
discriminationatlow
|     |     |     | targetingindependence(parity). |     | repeateddata-pipeline |
| --- | --- | --- | ------------------------------ | --- | --------------------- |
implementationcost.
adjustments.
Transformsfeaturevaluesto
|     |     |     |     | Improvesfairness | Worseprofit–fairness |
| --- | --- | --- | --- | ---------------- | -------------------- |
reducedistributiondifferences
Kozodoietal. DisparateImpact withoutchangingmodel trade-offthanthebest
|     | Pre-processing |     | acrossprotectedgroups,reducing |     |     |
| --- | -------------- | --- | ------------------------------ | --- | --- |
(2022) Remover(DIR) dependenceonprotected architecture; in-processingoption(PRR)
|     |     |     |     | model-agnostic. | intheirreportedresults. |
| --- | --- | --- | --- | --------------- | ----------------------- |
attributes.
|     |     |     | Addsaregularizationtermtothe | Tunabletrade-off; | Invasive;modifiesthe |
| --- | --- | --- | ---------------------------- | ----------------- | -------------------- |
Kozodoietal. PrejudiceRemover trainingobjectivethatpenalizes achievesbetterprofit– trainingobjective/
In-processing
(2022) Regularizer(PRR) unfairnessusingaprejudiceindex, fairnesstrade-offthan scorecardsandincreases
|     |     |     | withatunablepenaltyweight.       | DIRintheirevaluation. | implementationburden. |
| --- | --- | --- | -------------------------------- | --------------------- | --------------------- |
|     |     |     | Trainsapredictorwhileanauxiliary |                       | Requiresretrainingand |
Tunablefairness–profit
Kozodoietal. Adversarial adversarytriestoinfertheprotected pipelinechanges;more
|     | In-processing |     |     | balancevia |     |
| --- | ------------- | --- | --- | ---------- | --- |
(2022) Debiasing attribute;penalizesthepredictor invasivethan
|     |     |     | whentheadversarysucceeds. | meta-parameters. | post-processing. |
| --- | --- | --- | ------------------------- | ---------------- | ---------------- |
Optimizesaclassifierunder
|              |     |           | fairnessconstraints(e.g., | Explicitcontrolover | Model/trainingspecific; |
| ------------ | --- | --------- | ------------------------- | ------------------- | ----------------------- |
| Kozodoietal. |     | Meta-fair |                           |                     |                         |
In-processing independence/separation)with fairness–accuracy requiresretrainingand
| (2022) |     | Classification |                          |             |                    |
| ------ | --- | -------------- | ------------------------ | ----------- | ------------------ |
|        |     |                | trade-offmeta-parameters | trade-offs. | integrationeffort. |
controllingaccuracyvs.fairness.
|     |     |     | Relabelsdecisionsinan | Strongfairnessgains; | Canreduceprofitability |
| --- | --- | --- | --------------------- | -------------------- | ---------------------- |
Kozodoietal. RejectOption uncertaintyregioninfavorofthe largelypreservesthe comparedtoin-processing
Post-processing
(2022) Classification(ROC) disadvantagedgrouptoimprove existingscoring approaches;actsonlyon
|     |     |     | groupparity. | pipeline. | thedecisionboundary. |
| --- | --- | --- | ------------ | --------- | -------------------- |
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
32of36
TableA11.Summaryoffairnessmitigationstrategiesincreditscoring(Part2:Rows7–12).
| Author | Category | Method | Mechanism | Strengths                | Limitations       |
| ------ | -------- | ------ | --------- | ------------------------ | ----------------- |
|        |          |        |           | Post-hoc;model-agnostic; | Strictfairnessmay |
Usesgroup-specificthresholdsto
Kozodoietal. EqualizedOdds canreducediscrimination requirelarge
|     | Post-processing |     | equalizeerrorratesacrossgroups |     |     |
| --- | --------------- | --- | ------------------------------ | --- | --- |
(2022) Post-processing atlowcostuptoapoint profit/utilitysacrifices
(separation/equalizedodds).
|     |     |     |     | ontheParetofrontier. | acrossdatasets. |
| --- | --- | --- | --- | -------------------- | --------------- |
Inheritspost-processing
Post-hoc;preserves
|              |     |                 | Calibratespredictedprobabilities |                   | trade-offs;doesnot |
| ------------ | --- | --------------- | -------------------------------- | ----------------- | ------------------ |
| Kozodoietal. |     | Group-wisePlatt |                                  | pipeline;supports |                    |
Post-processing pergrouptosatisfysufficiency(risk addressupstreambias;
| (2022) |     | Scaling |                                 | calibrationforsufficiency- |                          |
| ------ | --- | ------- | ------------------------------- | -------------------------- | ------------------------ |
|        |     |         | meaningconsistentacrossgroups). |                            | cannotsatisfyallcriteria |
|        |     |         |                                 | orientedcompliance.        | simultaneously.          |
|        |     |         | Learner–auditoradversarial      | Explicitlytargets          |                          |
Moldovan approachminimizingunfairness individual-level Hardtotune;mayoverfit
|     | In-processing | GerryFair |     |     |     |
| --- | ------------- | --------- | --- | --- | --- |
(2023) viaiterativeconstraintenforcement unfairness,notonly onsmallcreditdatasets.
|     |     |     | (targetsindividualfairness). | groupparity. |     |
| --- | --- | --- | ---------------------------- | ------------ | --- |
Reformulateslearningasa
|          |               |            |                             | Allowsexplicit          | Accuracymaydegrade |
| -------- | ------------- | ---------- | --------------------------- | ----------------------- | ------------------ |
| Moldovan |               | GridSearch | cost-sensitivereductionand  |                         |                    |
|          | In-processing |            |                             | explorationandselection | sharplyunderstrict |
| (2023)   |               | Reduction  | searchesconstraintweightsto |                         |                    |
|          |               |            |                             | oftrade-offpoints.      | constraints.       |
obtainfairness–accuracytrade-offs.
|              |     |     | Optimal-transportinterpolation | Providesatunable    | Weightselectionembeds |
| ------------ | --- | --- | ------------------------------ | ------------------- | --------------------- |
|              |     |     | betweenincompatiblefairness    |                     | normative/legal       |
| Zehlikeetal. |     |     |                                | mechanismtonavigate |                       |
Post-processing FAIM criteria(calibration,balancefor judgment;maynot
| (2025) |     |     |                                | incompatibilitybetween |                        |
| ------ | --- | --- | ------------------------------ | ---------------------- | ---------------------- |
|        |     |     | positives,balancefornegatives) |                        | matchasingleregulatory |
fairnesscriteria.
|     |     |             | usingweightedconstraints.    |     | interpretation.   |
| --- | --- | ----------- | ---------------------------- | --- | ----------------- |
|     |     | Demographic | ModifiesLRtrainingtominimize |     | Requiressensitive |
Valdrighietal. Parity/Equal losssubjecttoacorrelationconstraint Simpleandinterpretable; attributesduringtraining;
In-processing
(2025) Opportunity betweenpredictionsandsensitive tunabletrade-off. remainsatrade-offrather
|     |     | Classifier | attributes(tunableconstant). |     | thanaguarantee. |
| --- | --- | ---------- | ---------------------------- | --- | --------------- |
TableA12.Summaryoffairnessmitigationstrategiesincreditscoring(Part3:Rows13–18).
| Author | Category | Method | Mechanism | Strengths     | Limitations          |
| ------ | -------- | ------ | --------- | ------------- | -------------------- |
|        |          |        |           | Strongtabular | Model-classspecific; |
Altersboostingtojointlyminimize
|                |               | FairGBM      |                                  | performancewith  | dependsonproxy |
| -------------- | ------------- | ------------ | -------------------------------- | ---------------- | -------------- |
| Valdrighietal. |               |              | predictionlossandadifferentiable |                  |                |
|                | In-processing | (constrained |                                  | embeddedfairness | designand      |
(2025) gradientboosting) proxyofafairnessmetric(e.g., controlusingconstrained differentiabilityof
DP/EO)duringtraining.
|     |     |     |                            | learning. | fairnessobjectives. |
| --- | --- | --- | -------------------------- | --------- | ------------------- |
|     |     |     | BuildsseparateROCcurvesper |           | Requiressensitive   |
Consistentlyreaches
|                |     |           | groupandselectsthresholdsthat |                     | attributesatprediction |
| -------------- | --- | --------- | ----------------------------- | ------------------- | ---------------------- |
| Valdrighietal. |     | Threshold |                               | fairnesstargetswith |                        |
Post-processing minimizelosswithinthefeasiblefair time,whichmaybe
| (2025) |     | Optimizer |                               | minimumaccuracyloss |                     |
| ------ | --- | --------- | ----------------------------- | ------------------- | ------------------- |
|        |     |           | region,yieldinggroup-specific |                     | legally/practically |
intheircomparisons.
|     |     |     | thresholds. |     | constrained. |
| --- | --- | --- | ----------- | --- | ------------ |
Lesstunablethan
Altersoutputsofblack-boxmodels
|                |                 | Positionon |                                    | Versatileandsuitablefor | in-processing;may |
| -------------- | --------------- | ---------- | ---------------------------------- | ----------------------- | ----------------- |
| Valdrighietal. | Post-processing |            | tosatisfyfairnessconstraints(e.g., |                         |                   |
(2025) (general) post-processing groupthresholds)withoutchanging black-boxesandfixed yieldweaker
|     |     | (general) |     | scorecards. | improvementsrelative |
| --- | --- | --------- | --- | ----------- | -------------------- |
modeltraining.
topre-/in-processing.
|          |     |                | Framesfairnessasstochastic     |                      | Notreported(explicit |
| -------- | --- | -------------- | ------------------------------ | -------------------- | -------------------- |
|          |     | Stochastic     |                                | ProducessmoothPareto |                      |
|          |     |                | multi-objectiveoptimizationand |                      | method-level         |
| S.Liuand |     | Multi-Gradient |                                | frontiersandstable   |                      |
In-processing aggregatesgradientsofpredictionloss limitationsnotstated
| Vicente(2022) |     | (SMG)bi-objective |                                  | convergenceacross    |               |
| ------------- | --- | ----------------- | -------------------------------- | -------------------- | ------------- |
|               |     |                   | andfairnesspenaltyalongthePareto |                      | beyondgeneral |
|               |     | optimization      |                                  | fairnessconstraints. |               |
|               |     |                   | frontier(e.g.,DI/EOconstraints). |                      | trade-offs).  |
Stream-learningMixedNaïveBayes
Lowdiscrimination(SP
|          |        |           | withmulti-objectiveoptimization; | near0)whileimproving | Doesnotguarantee     |
| -------- | ------ | --------- | -------------------------------- | -------------------- | -------------------- |
| Badarand |        |           | dynamicinstanceweightingfor      |                      | globalfairnessacross |
|          | Hybrid | Fair-CMNB |                                  | accuracyrelativeto   |                      |
Fisichella(2024) imbalanceanddiscrimination settings;gainsare
baselines;supports
|     |     |     | control(targetsStatisticalParity; |     | dataset-dependent. |
| --- | --- | --- | --------------------------------- | --- | ------------------ |
streamingsettings.
usescausalfairnessviaATE/FACE).
Non-parametricstacked
Strongerperformance
autoencoderstolearnlatent
thanclassic
| S.Hanetal. | Pre-processing |      | structure,thenconditional     |                    |              |
| ---------- | -------------- | ---- | ----------------------------- | ------------------ | ------------ |
|            |                | NOTE |                               | oversampling(e.g., | Notreported. |
| (2024)     | (oversampling) |      | WassersteinGANoversamplingfor |                    |              |
SMOTE)intheir
mixedcategorical/
|     |     |     | numericalfeatures. | comparisons. |     |
| --- | --- | --- | ------------------ | ------------ | --- |
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
33of36
TableA13.Summaryoffairnessmitigationstrategiesincreditscoring(Part4:Rows19–21).
| Author | Category | Method | Mechanism | Strengths | Limitations |
| ------ | -------- | ------ | --------- | --------- | ----------- |
Outperformsparceling,
|     |     |     | Semi-supervisedapproachthat | reweighting,and |     |
| --- | --- | --- | --------------------------- | --------------- | --- |
Pre-processing
|              |             |                 | iterativelyinferslabelsfor    | Heckman-stylecorrection; |              |
| ------------ | ----------- | --------------- | ----------------------------- | ------------------------ | ------------ |
| Kozodoietal. | (bias-aware | BASL:Bias-Aware |                               |                          |              |
|              |             |                 | rejected/unlabeledinstancesto | recoversasubstantial     | Notreported. |
| (2025)       | rejection   | Self-Learning   |                               |                          |              |
|              |             |                 | reducesamplingbiasandimprove  | shareofpredictiveloss    |              |
inference)
|     |     |     | trainingrepresentativeness. | attributedtosamplingbias |     |
| --- | --- | --- | --------------------------- | ------------------------ | --- |
intheircasestudy.
CombinesADASYNoversampling
|     |     |     | withaLocalCascadingEnsemble | Improvesgeneralization | Maystruggletoaddress |
| --- | --- | --- | --------------------------- | ---------------------- | -------------------- |
biasandvariance
| Chaietal. |                |            | (bagging/boosting/local       | underimbalance;LCE    |                     |
| --------- | -------------- | ---------- | ----------------------------- | --------------------- | ------------------- |
|           | Pre-processing | ADASYN-LCE |                               |                       | simultaneouslyunder |
| (2025)    |                |            | cascading)toimproverobustness | balancesbias–variance |                     |
someconditions(as
|     |     |     | forunderservedpopulationsunder | acrosssubsetsofthedata. |     |
| --- | --- | --- | ------------------------------ | ----------------------- | --- |
notedbytheauthors).
imbalance.
Supportsjoint
|     |     |     | Integratesaweighted | improvementsin |     |
| --- | --- | --- | ------------------- | -------------- | --- |
Pronetooverfittingif
| Hartomo |               | Weighted | cross-entropyobjectiveinto | performanceunder |             |
| ------- | ------------- | -------- | -------------------------- | ---------------- | ----------- |
|         | In-processing |          |                            |                  | weightingis |
etal.(2025) TabTransformer TabTransformertogivelarger imbalanceand
mis-specified.
|     |     |     | gradientstominorityclasses. | fairness-relatedobjectives |     |
| --- | --- | --- | --------------------------- | -------------------------- | --- |
intheirframing.
References
Adegoke,T.,Ofodile,O.,Ochuba,N.,&Akinrinol,O.(2024).Evaluatingthefairnessofcreditscoringmodels:Aliteraturereviewon
mortgageaccessibilityforunder-reservedpopulations.GSCAdvancedResearchandReviews,18(3),189–199.[CrossRef]
AliShahee,S.,&Patel,R.(2025).AnexplainableADASYN-basedfocallossapproachforcreditassessment.JournalofForecasting,44,
1513–1530.[CrossRef]
Alufaisan,Y.,Marusich,L.R.,Bakdash,J.Z.,Zhou,Y.,&Kantarcioglu,M.(2021). Doesexplainableartificialintelligenceimprove
humandecision-making? InProceedingsoftheAAAIconferenceonartificialintelligence(Vol.35, pp.6618–6626). AAAIPress.
[CrossRef]
Alves,G.,Bernier,F.,Couceiro,M.,Makhlouf,K.,Palamidessi,C.,&Zhioua,S.(2023).Surveyonfairnessnotionsandrelatedtensions.
EUROJournalonDecisionProcesses,11,100033.[CrossRef]
Amekoe,K.M.,Azzag,H.,Dagdia,Z.C.,Lebbah,M.,&Jaffre,G.(2024).Exploringaccuracyandinterpretabilitytrade-offintabular
learningwithnovelattention-basedmodels.NeuralComputingandApplications,36(30),18583–18611.[CrossRef]
Aruleba, I., &Sun, Y.(2024). Effectivecreditriskpredictionusingensembleclassifierswithmodelexplanation. IEEEAccess, 12,
115015–115025.[CrossRef]
Atif,D.(2025).VAE-INN:Variationalautoencoderwithintegratedneuralnetworkclassifierforimbalancedcreditscoring,utilizing
weightedlossforimprovedaccuracy.ComputationalEconomics.[CrossRef]
Badar, M., &Fisichella, M.(2024). Fair-CMNB:Advancingfairness-awarestreamlearningwithnaïvebayesandmulti-objective
optimization.BigDataandCognitiveComputing,8(2),16.[CrossRef]
Balashankar,A.,&Lees,A.(2022).Theneedfortransparentdemographicgrouptrade-offsincreditriskandincomeclassification.In
Proceedingsoftheinternationalconferenceoninformation(pp.344–354).SpringerInternationalPublishing.
Bartlett,R.,Morse,A.,Stanton,R.,&Wallace,N.(2022). Consumer-lendingdiscriminationintheFinTechera. JournalofFinancial
Economics,143(1),30–56.[CrossRef]
BaselCommitteeonBankingSupervision.(2013).Principlesforeffectiveriskdataaggregationandriskreporting(Technicalreportno.8,Basel
committeepublicationno.239).BankforInternationalSettlements.Availableonline:https://www.bis.org/publ/bcbs239.htm
(accessedon30September2025).
Berg,T.,Burg,V.,Gombovic´,A.,&Puri,M.(2020). OntheriseofFintechs: Creditscoringusingdigitalfootprints. TheReviewof
FinancialStudies,33(7),2845–2897.[CrossRef]
Brzezinski,D.,Stachowiak,J.,Stefanowski,J.,Szczech,I.,Susmaga,R.,Aksenyuk,S.,&Yasinskyi,O.(2024). Propertiesoffairness
measuresinthecontextofvaryingclassimbalanceandprotectedgroupratios.ACMTransactionsonKnowledgeDiscoveryfrom
Data,18(7),1–18.[CrossRef]
Bueff,A.C.,Cytryn´ski,M.,Calabrese,R.,Jones,M.,Roberts,J.,Moore,J.,&Brown,I.(2022).Machinelearninginterpretabilityfora
stressscenariogenerationincreditscoringbasedoncounterfactuals.ExpertSystemswithApplications,202,117271.[CrossRef]
Bulut,C.,&Arslan,E.(2025).Ahybridapproachtocreditriskassessmentusingbillpaymenthabitsdataandexplainableartificial
intelligence.AppliedSciences,15(10),5723.[CrossRef]
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 34of36
Bücker,M.,Szepannek,G.,Gosiewska,A.,&Biecek,P.(2022). Transparency,auditability,andexplainabilityofmachinelearning
modelsincreditscoring.JournaloftheOperationalResearchSociety,73(1),70–90.[CrossRef]
Cao,W.,He,Y.,Wang,W.,Zhu,W.,&Demazeau,Y.(2021).Ensemblemethodsforcreditscoringofchinesepeer-to-peerloans.Journal
ofCreditRisk,17,79–115.[CrossRef]
Caton,S.,&Haas,C.(2024).Fairnessinmachinelearning:Asurvey.ACMComputingSurveys,56(7),1–38.[CrossRef]
Chacko, A., &Aravindhar, D.J.(2025, February21–22). Enhancingfairnessandaccuracyincreditscoreanalysis: Anovelframework
utilizingkernelPCA.2025InternationalConferenceonInformationTechnology,InnovationandIntelligentSystems(ICITIIT),
Kottayam,India.[CrossRef]
Chai,N.,Abedin,M.Z.,Yang,L.,&Shi,B.(2025).Farmers’creditriskevaluationwithanexplainablehybridensembleapproach:A
closerlookinmicrofinance.Pacific-BasinFinanceJournal,89,102612.[CrossRef]
Chen,Y.,Calabrese,R.,&Martin-Barragán,B.(2024).Interpretablemachinelearningforimbalancedcreditscoringdatasets.European
JournalofOperationalResearch,312(1),357–372.[CrossRef]
Cornacchia,G.,Anelli,V.W.,Narducci,F.,Ragone,A.,&DiSciascio,E.(2023).Ageneralarchitectureforatrustworthycreditworthiness-
assessmentplatforminthefinancialdomain.AETiC,7,56–64.[CrossRef]
Corrales-Barquero,R.,Marín-Raventós,G.,&Barrantes,E.G.(2021,October27–28).Areviewofgenderbiasmitigationincreditscoring
models.2021InternationalConferenceonElectrical,ElectronicsandRelatedDataScience(EE-RDS),Johannesburg,SouthAfrica.
[CrossRef]
C-Rella,J.,Martínez-Rego,D.,&VilarFernández,J.M.(2025).Cost-sensitivereinforcementlearningforcreditrisk.ExpertSystemswith
Applications,272,126708.[CrossRef]
Das,S.,Stanton,R.,&Wallace,N.(2023).Algorithmicfairness.AnnualReviewofFinancialEconomics,15(1),565–593.[CrossRef]
Dastile,X.,&Celik,T.(2024).Counterfactualexplanationswithmultiplepropertiesincreditscoring.IEEEAccess,12,110713–110728.
[CrossRef]
Dastile,X.,Celik,T.,&Vandierendonck,H.(2022). Model-agnosticcounterfactualexplanationsincreditscoring. IEEEAccess,10,
69543–69554.[CrossRef]
deCastroVieira,J.R.,Barboza,F.L.D.M.,Cajueiro,D.O.,&Kimura,H.(2025).TowardsfairAI:Mitigatingbiasincreditdecisions—A
systematicliteraturereview.JournalofRiskandFinancialManagement,18,228.[CrossRef]
Dessain,J.,Bentaleb,N.,&Viñas,F.(2023).CostofexplainabilityinAI:Anexamplewithcreditscoringmodels.InProceedingsofthe
worldconferenceonexplainableartificialintelligence(pp.498–516).SpringerNature.[CrossRef]
European Central Bank. (2024). Supervisory guide on risk data aggregation and risk reporting (Technical report, supervisory guide).
EuropeanCentralBank,BankingSupervision.Availableonline:https://www.bankingsupervision.europa.eu/ecb/pub/pdf/
ssm.supervisory_guides240503_riskreporting.en.pdf(accessedon30September2025).
Goethals,S.,Martens,D.,&Calders,T.(2024).Precof:Counterfactualexplanationsforfairness.MachineLearning,113(5),3111–3142.
[CrossRef]
Griffith,M.A.(2023). AIlendingandtheECOA:Avoidingaccidentaldiscrimination. NorthCarolinaBankingInstitute,27,349–381.
Availableonline:https://scholarship.law.unc.edu/ncbi/vol27/iss1/16(accessedon30September2025).
Han,S.,Jung,H.,Yoo,P.D.,Provetti,A.,&Calì,A.(2024). NOTE:Non-parametricoversamplingtechniqueforexplainablecredit
scoring.ScientificReports,14(1),26070.[CrossRef]
Han,W.,Gu,X.,&Jian,L.(2023).Amulti-layermulti-viewstackingmodelforcreditriskassessment.IntelligentDataAnalysis,27(5),
1457–1475.[CrossRef]
Hartomo,K.D.,Arthur,C.,&Nataliani,Y.(2025).AnovelweightedlosstabtransformerintegratingexplainableAIforimbalanced
creditriskdatasets.IEEEAccess,13,31045–31056.[CrossRef]
Hickey,J.M.,DiStefano,P.G.,&Vasileiou,V.(2020). FairnessbyexplicabilityandadversarialSHAPlearning. InJointEuropean
conferenceonmachinelearningandknowledgediscoveryindatabases(ECMLPKDD)(pp.174–190).SpringerInternationalPublishing.
Hjelkrem,L.O.,&Lange,P.E.D.(2023).Explainingdeeplearningmodelsforcreditscoringwithtextualtransactiondata.Journalof
RiskandFinancialManagement,16(4),221.[CrossRef]
Hlongwane,R.,Ramabao,K.,&Mongwe,W.(2024).Anovelframeworkforenhancingtransparencyincreditscoring:Leveraging
Shapleyvaluesforinterpretablecreditscorecards.PLoSONE,19(8),e0308718.[CrossRef][PubMed]
Hurlin,C.,Pérignon,C.,&Saurin,S.(2024).Thefairnessofcreditscoringmodels.ManagementScience,70(11),1234–1256.[CrossRef]
Jiang,Y.,Fang,X.,&Wang,Z.(2024).Disparityanddiscriminationinconsumercreditmarkets:Evidencefromonlinepeer-to-peer
lending.Pacific-BasinFinanceJournal,83,102237.[CrossRef]
Kanaparthi,V.(2023,April26–28).Creditriskpredictionusingensemblemachinelearningalgorithms.2023InternationalConferenceon
InventiveComputationTechnologies(ICICT)(pp.41–47),Lalitpur,Nepal.[CrossRef]
Keele,S.(2007).Guidelinesforperformingsystematicliteraturereviewsinsoftwareengineering(EBSEtechnicalreport,version2.3).Available
online:https://www.elsevier.com/__data/promis_misc/525444systematicreviewsguide.pdf(accessedon17October2025).
Koulu,R.(2020).Humancontroloverautomation:EUpolicyandAIethics.EuropeanJournalofLegalStudies,12,9–46.[CrossRef]
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 35of36
Kozodoi,N.,Jacob,J.,&Lessmann,S.(2022).Fairnessincreditscoring:Assessment,implementationandprofitimplications.European
JournalofOperationalResearch,297(3),1083–1094.[CrossRef]
Kozodoi,N.,Lessmann,S.,Alamgir,M.,Moreira-Matias,L.,&Papakonstantinou,K.(2025).Fightingsamplingbias:Aframeworkfor
trainingandevaluatingcreditscoringmodels.EuropeanJournalofOperationalResearch,324(2),616–628.[CrossRef]
Kuiper,O.,vandenBerg,M.,vanderBurgt,J.,&Leijnen,S.(2021). ExploringexplainableAIinthefinancialsector: Perspectives
of banks and supervisory authorities. In Proceedings of the benelux conference on artificial intelligence (pp. 105–119). Springer
InternationalPublishing.
Kumar,I.E.,Hines,K.E.,&Dickerson,J.P.(2022).Equalizingcreditopportunityinalgorithms:Aligningalgorithmicfairnessresearch
withUSfairlendingregulation.InProceedingsofthe2022AAAI/ACMconferenceonAI,ethics,andsociety(pp.357–368).Association
forComputingMachinery.[CrossRef]
Lainez,N.,&Gardner,J.(2023).AlgorithmiccreditscoringinVietnam:Alegalproposalformaximizingbenefitsandminimizingrisks.
AsianJournalofLawandSociety,10(3),401–432.[CrossRef]
Langenbucher,K.(2020). ResponsibleAI-basedcreditscoring—Alegalframework. EuropeanBusinessLawReview,31(4),527–572.
[CrossRef]
Langenbucher,K.,&Corcoran,P.(2022).ResponsibleAIcreditscoring—Alessonfromupstart.com.InDigitalfinanceinEurope:Law,
regulation,andgovernance.DeGruyter.
Li,C.,Wang,H.,Jiang,S.,&Gu,B.(2024).TheeffectofAI-enabledcreditscoringonfinancialinclusion:Evidencefromanunderserved
populationofoveronemillion.MISQuarterly,48(4),1803–1834.[CrossRef]
Li,L.H.,Sharma,A.K.,&Cheng,S.T.(2025).ExplainableAIbasedLightGBMpredictionmodeltopredictdefaultborrowerinsocial
lendingplatform.IntelligentSystemswithApplications,26,200514.[CrossRef]
Li,W.,Paraschiv,F.,&Sermpinis,G.S.(2022).Adata-drivenexplainablecase-basedreasoningapproachforfinancialriskdetection.
QuantitativeFinance,22,2257–2274.[CrossRef]
Li,Y.,Wang,X.,Djehiche,B.,&Hu,X.(2020).Creditscoringbyincorporatingdynamicnetworkedinformation.EuropeanJournalof
OperationalResearch,286(3),1103–1112.[CrossRef]
Li,Z.,Hu,X.,Li,K.,Zhou,F.,&Shen,F.(2020).Inferringtheoutcomesofrejectedloans:Anapplicationofsemisupervisedclustering.
JournaloftheRoyalStatisticalSociety:SeriesA,183,631–654.[CrossRef]
Liao,J.,Wang,W.,Xue,J.,Lei,A.,Han,X.,&Lu,K.(2022).Combatingsamplingbias:Aself-trainingmethodincreditriskmodels.
ProceedingsoftheAAAIConferenceonArtificialIntelligence,36,12566–12572.[CrossRef]
Liu,J.,Zhang,X.,&Xiong,H.(2024).Creditriskpredictionbasedoncausalmachinelearning:Bayesiannetworklearning,default
inference,andinterpretation.JournalofForecasting,43(5),1625–1660.[CrossRef]
Liu, S., & Vicente, L. N. (2022). Accuracy and fairness trade-offs in machine learning: A stochastic multi-objective approach.
ComputationalManagementScience,19(3),513–537.[CrossRef]
Martinez,N.,Bertran,M.,&Sapiro,G.(2020,July13–18).Minimaxparetofairness:Amulti-objectiveperspective.InternationalConference
onMachineLearning(ICML)(pp.6755–6764),Virtual.
Mestiri,S.,&Hiboun,S.M.(2024).Creditscoringusingmachinelearninganddeeplearning-basedmodels.DataScienceinFinanceand
Economics,4(2),236–248.[CrossRef]
Moher,D.,Liberati,A.,Tetzlaff,J.,Altman,D.G.,&Group,P.(2010).Preferredreportingitemsforsystematicreviewsandmeta-analyses:
ThePRISMAstatement.InternationalJournalofSurgery,8(5),336–341.[CrossRef]
Moldovan,D.(2023).Algorithmicdecisionmakingmethodsforfaircreditscoring.IEEEAccess,11,59729–59743.[CrossRef]
Mou,Y.,Pu,Z.,Feng,D.,Luo,Y.,Lai,Y.,Huang,J.,Tian,Y.,&Xiao,F.(2025).Cost-awarecredit-scoringframeworkbasedonresampling
andfeatureselection.ComputationalEconomics,66,3007–3032.[CrossRef]
Muñoz-Cancino,R.,Bravo,C.,Ríos,S.A.,&Graña,M.(2023).Onthedynamicsofcredithistoryandsocialinteractionfeatures,and
theirimpactoncreditworthinessassessmentperformance.ExpertSystemswithApplications,218,119599.[CrossRef]
Nwafor,C.N.,Nwafor,O.,&Brahma,S.(2024).Enhancingtransparencyandfairnessinautomatedcreditdecisions:Anexplainable
novelhybridmachinelearningapproach.ScientificReports,14(1),25174.[CrossRef]
Page,M.J.,McKenzie,J.E.,Bossuyt,P.M.,Boutron,I.,Hoffmann,T.C.,Mulrow,C.D.,Shamseer,L.,Tetzlaff,J.M.,Akl,E.A.,Brennan,
S.E.,Chou,R.,Glanville,J.,Grimshaw,J.M.,Hróbjartsson,A.,Lalu,M.M.,Li,T.,Loder,E.W.,Mayo-Wilson,E.,McDonald,S.,&
Moher,D.(2021).Updatingguidanceforreportingsystematicreviews:DevelopmentofthePRISMA2020statement.Journalof
ClinicalEpidemiology,134,103–112.[CrossRef]
Patron,G.,Leon,D.,Lopez,E.,&Hernandez,G.(2020).Aninterpretableautomatedmachinelearningcreditriskmodel.InWorkshop
onengineeringapplications(pp.16–23).SpringerInternationalPublishing.
Peng,Z.,Mo,W.,Duan,C.,Li,Q.,&Zhou,B.(2023).Learningfromactivehumaninvolvementthroughproxyvaluepropagation.In
Proceedingsofthe37thconferenceonneuralinformationprocessingsystems(NeurIPS2023).CurranAssociates,Inc.Availableonline:
https://metadriverse.github.io/pvp(accessedon17October2025).
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 36of36
Perry,V.G.,Martin,K.,&Schnare,A.(2023).Algorithmsforall:CanAIinthemortgagemarketexpandaccesstohomeownership?AI,
4(4),888–903.[CrossRef]
Ratul,Q.E.A.,Serra,E.,&Cuzzocrea,A.(2021,December15–18).Evaluatingattributionmethodsinmachinelearninginterpretability.2021
IEEEInternationalConferenceonBigData(BigData)(pp.5239–5245),Orlando,FL,USA.
Repetto,M.(2025).Multicriteriainterpretabilitydrivendeeplearning.AnnalsofOperationsResearch,346(2),1621–1635.[CrossRef]
Ribeiro-Flucht,L.,Chen,X.,&Meurers,D.(2024).ExplainableAIinlanguagelearning:Linkingempiricalevidenceandtheoretical
conceptsinproficiencyandreadabilitymodelingofportuguese. InProceedingsofthe19thworkshoponinnovativeuseofNLP
for building educational applications (BEA 2024) (pp. 199–209). Association for Computational Linguistics. Available online:
https://aclanthology.org/2024.bea-1.17(accessedon4October2025).
Ridzuan,N.N.,Masri,M.,Anshari,M.,Fitriyani,N.L.,&Syafrudin,M.(2024).AIinthefinancialsector:Thelinebetweeninnovation,
regulationandethicalresponsibility.Information,15(8),432.[CrossRef]
Roa,L.,Correa-Bahnsen,A.,Suarez,G.,Cortés-Tejada,F.,Luque,M.A.,&Bravo,C.(2021).Super-appbehavioralpatternsincreditrisk
models:Financial,statisticalandregulatoryimplications.ExpertSystemswithApplications,169,114486.[CrossRef]
Shi, X., Tang, D., & Yu, Y. (2025). Credit scoring prediction using deep learning models in the financial sector. IEEE Access, 13,
130731–130746.[CrossRef]
Sulastri,R.,Ding,A.Y.,&Janssen,M.(2025,June18–20).Sensitivityanalysis:Improvinginclusivecreditscoringalgorithmthroughfeature
weightandpenalty-basedapproach.2025EleventhInternationalConferenceonEdemocracy&Egovernment(ICEDEG)(pp.54–61),
Bern,Switzerland.[CrossRef]
Talaat,F.M.,Aljadani,A.,Badawy,M.,&Elhosseini,M.(2024).Towardinterpretablecreditscoring:Integratingexplainableartificial
intelligencewithdeeplearningforcreditcarddefaultprediction.NeuralComputingandApplications,36(9),4847–4865.[CrossRef]
Tiukhova,E.,Salcuni,A.,Oguz,C.,Niglio,M.,Storti,G.,Forte,F.,Baesens,B.M.,&Snoeck,M.(2025).Boostingcreditriskdataquality
usingmachinelearningandeXplainableAItechniques. InMachinelearningandprinciplesandpracticeofknowledgediscoveryin
databases.Springer.[CrossRef]
Valdrighi,G.,Ribeiro,A.M.,Pereira,J.S.B.,Guardieiro,V.,Hendricks,A.,MirandaFilho,D.,&MedeirosRaimundo,M.(2025).Best
practicesforresponsiblemachinelearningincreditscoring.NeuralComputingandApplications,37,20781–20821.[CrossRef]
Vukovic´,D.B.,Dekpo-Adza,S.,&Matovic´,S.(2025).AIintegrationinfinancialservices:Asystematicreviewoftrendsandregulatory
challenges.HumanitiesandSocialSciencesCommunications,12,562.[CrossRef]
Wang,W.,Lesner,C.,Ran,A.,Rukonic,M.,Xue,J.,&Shiu,E.(2020).Usingsmallbusinessbankingdataforexplainablecreditrisk
scoring.InProceedingsoftheAAAIConferenceonArtificialIntelligence(Vol.34,pp.13396–13401).AAAIPress.[CrossRef]
Wu,Z.,Dong,Y.,Li,Y.,&Liu,Y.(2025).A‘DivideandConquer’rejectinferenceapproachleveraginggraph-basedsemi-supervised
learning.AnnalsofOperationsResearch.[CrossRef]
Xie,W.,He,J.,Huang,F.,&Ren,J.(2025).Operationalriskassessmentofcommercialbanks’supplychainfinance.Systems,13(2),76.
[CrossRef]
Zacharias,J.,vonZahn,M.,Chen,J.,&Hinz,O.(2022).Designingafeatureselectionmethodbasedonexplainableartificialintelligence.
ElectronicMarkets,32,2159–2184.[CrossRef]
Zehlike,M.,Loosley,A.,Jonsson,H.,Wiedemann,E.,&Hacker,P.(2025). Beyondincompatibility: Trade-offsbetweenmutually
exclusivefairnesscriteriainmachinelearningandlaw.ArtificialIntelligence,340,104280.[CrossRef]
Zhang,R.,Li,I.,&Ding,Z.(2025).AnInterpretablecreditriskassessmentmodelwithboundarysampleidentification.PeerJComputer
Science,11,e2988.[CrossRef][PubMed]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/jrfm19020104