---
conversion_metadata:
  converted_at: "2026-07-21T13:43:00Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Kaya et al.pdf"
  source_pdf_sha256: "38bc00a63a82a6b78ff2f9d834e7c701e1f3d5a6658824b5308a783654907476"
  page_count: 24
  markdown_char_count: 253475
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 23 January 2026, accepted 3 February 2026, date of publication 10 February 2026, date of current version 23 February 2026.

Digital Object Identifier 10.1109/ACCESS.2026.3663161

Explainable Artificial Intelligence (XAI): Concepts,
Applications, Challenges, and Future Perspectives

OSMAN KAYA 1,2, A. F. M. SHAHEN SHAH 1, (Senior Member, IEEE),
MUHAMMET ALI KARABULUT 2, (Senior Member, IEEE),
SUMEYE NUR KARAHAN 3, MUSTAFA SERDAR OSMANCA 3,
AND NURETTIN ACıR2
1Electronics and Communication Engineering Department, Yildiz Technical University, 34220 Istanbul, Türkiye
2Electronics Engineering Department, Turkish Air Force Academy, National Defense University, 34149 Istanbul, Türkiye
3Research and Development Department, Turk Telekom, 06000 Ankara, Türkiye

Corresponding author: A. F. M. Shahen Shah (shah@yildiz.edu.tr)

This work was supported by The Scientific and Technological Research Council of Türkiye (TÜBİTAK) through 1515 Frontier
Research and Development Laboratories Support Program for the Türk Telekom 6G Research and Development Laboratories
under Project 5249902.

ABSTRACT The aim of explainable artificial intelligence (XAI) is to address the black-box problem in
high-stakes applications. However, transparency alone does not guarantee trust. This review examines a
critical paradox in XAI research. While explanation methods can generate insights, three main challenges
limit their effectiveness. Firstly, adversarial manipulations can exploit explanations by creating new attack
surfaces with over ninety percent success while preserving model accuracy. Secondly, evaluation practices
remain primarily computational. Only twenty-six percent of user studies follow human-centered protocols
and fewer than twenty-three percent involve domain experts. Thirdly, regulatory requirements, such as the
GDPR right to explanation, lack clear technical implementations, complicating compliance. We analyzed
the literature across finance, healthcare, and cybersecurity and found that current research emphasizes
algorithmic innovation over practical deployment. Moving toward reliable AI requires shifting from simple
explanation methods (XAI 1.0) to systems that are aligned with human understanding, resistant to adversarial
attacks, and compliant with legal requirements (XAI 2.0). This review provides guidance on key technical
advances, evaluation strategies and regulatory clarifications necessary for deployment. trustworthy AI.

INDEX TERMS Ante-hoc, explainable artificial intelligence (XAI), human-centered XAI, interpretable
machine learning, trustworthy AI, post-hoc.

I. INTRODUCTION
Artificial intelligence (AI), especially deep learning, has
changed the technology of the twenty-first century in a big
way. These systems have changed many industries and sci-
entific fields, and they are better than human experts at
recognizing images and speech [1], running autonomous sys-
tems, and diagnosing complicated medical conditions [2].
Deep neural networks are able to do this by finding complex,
hierarchical patterns in huge datasets with millions or billions
of parameters. But this ability to predict comes at a cost: as

The associate editor coordinating the review of this manuscript and

approving it for publication was Ramoni Adeogun

.

models get more complicated, it’s harder to understand how
they make decisions. In artificial intelligence, the black box
problem describes systems that generate correct outputs with-
out revealing how those decisions are made [4], [5]. As AI is
increasingly being used in areas such as healthcare, finance,
criminal justice and transportation where safety is crucial,
this lack of transparency has become a significant concern,
since errors in algorithms may have serious consequences [6].
A lack of transparency leads to a loss of trust and accountabil-
ity, and makes it difficult to verify outcomes [7]. Furthermore,
regulations such as the GDPR entitle individuals affected by
automated decisions to an explanation [8]. The demand for
interpretability, driven by these legal and ethical demands,

27394

2026 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/

VOLUME 14, 2026

---

<!-- PAGE 2 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

has led to the rapid growth of explainable AI (XAI). The
aim of XAI is to make AI decisions more understandable,
reduce biases, and support the development of reliable and
fair systems [9], [10], [11], [12].

Current XAI surveys typically treat explainability as
primarily a technical challenge, with the focus being on gen-
erating interpretable outputs. However, failures observed in
real-world applications present a more complex picture. For
example, if a medical AI system provides accurate diagnoses
but clinicians distrust its explanations, the issue may lie not
only in the underlying algorithms, but also in the system’s
insufficiently human-centered design. These considerations
show that building trustworthy AI requires more than just
sophisticated explanation techniques. This review addresses
gaps in the existing literature by making three key con-
tributions. Firstly, we demonstrate that adversarial attacks
significantly reduce the reliability of explanation meth-
ods [13], [14], yet defense strategies are not widely adopted.
Secondly, we present evidence suggesting that current evalu-
ation practices prioritize computational metrics over human
interpretability. This helps to explain why systems that
perform well in controlled settings often fail in deploy-
ment. Lastly, we examine the challenges that organizations
face in meeting regulatory expectations when they cannot
determine whether their explanations satisfy legal standards,
demonstrating that regulatory and technical requirements
are not aligned, which makes practical
implementation
difficult.

A. FUNDAMENTAL CONCEPTS IN EXPLAINABLE
ARTIFICIAL INTELLIGENCE
XAI refers to the techniques and methods that make the
behavior and predictions of AI systems understandable to
humans. Unlike traditional black-box models, which provide
predictions without justification, XAI systems aim to provide
transparent reasoning, allowing users to understand, trust and
appropriately rely on AI decisions. The term explainable
AI formally emerged in the mid-2010s, although research
on interpretable models predates this terminology. Signifi-
cant momentum was gained in the field following DARPA’s
XAI program (2016–2021), which established foundational
frameworks for distinguishing between models that are inter-
pretable by design (ante-hoc methods) and techniques for
providing explanations after the fact (post-hoc) that can be
applied to black-box systems [128]. Early foundational work
in XAI includes decision tree visualization, rule extraction
from neural networks and sensitivity analysis [10], [41]. Piv-
otal developments in model-agnostic post-hoc explanations
were marked by Schlegel et al.’s LIME (2016) and Lundberg
and Lee’s SHAP (2017), enabling practitioners to generate
local or global explanations for any classifier [35], [36], [37].
At the same time, gradient-based attribution methods such
as Grad-CAM [54] emerged to improve the interpretabil-
ity of deep learning in computer vision. These seminal
contributions have laid the methodological groundwork for

contemporary XAI research. The need for XAI arises from
multiple converging factors. Firstly, regulatory requirements
such as EU’s General Data Protection Regulation (GDPR) [8]
and the proposed AI Act mandate transparency in automated
decision-making processes. Secondly, in high-stakes domains
such as healthcare diagnosis, credit assessment and criminal
justice, practitioners must understand AI reasoning in order
to identify potential biases, validate clinical or legal compli-
ance and maintain accountability [6]. Thirdly, psychological
research shows that users must understand when to rely on
and when to override AI recommendations in order to trust it
appropriately [7]. Without explainability, even highly accu-
rate models risk being misused, underutilized, or deployed
incorrectly when users cannot assess their reliability in new
situations. XAI is distinct from, yet related to, concepts such
as interpretability, transparency and trustworthiness. While
interpretability refers to the extent to which humans can
understand the cause of a decision, transparency describes
the degree to which a model’s internal mechanisms are vis-
ible. Trustworthiness encompasses broader considerations,
including robustness, fairness and privacy, with explainability
serving as a critical component. This review takes an inclusive
approach, examining XAI methods across the spectrum, from
intrinsically interpretable models to sophisticated post-hoc
explanation techniques. It recognizes that different stake-
holders and application contexts require different explanation
paradigms.

The important contributions of this paper to the literature

are summarized below.

• We provide a comprehensive and structured taxon-
omy of XAI by systematically organizing explanation
methods across multiple dimensions, including model
dependency, scope of explanation, and timing (ante-hoc
versus post-hoc), offering a unified conceptual frame-
work for both researchers and practitioners.

• We present a domain-oriented analysis of XAI applica-
tions in high-stakes sectors such as finance, healthcare,
and cybersecurity, highlighting domain-specific require-
ments, user roles, and deployment constraints that are
often overlooked in existing surveys.

• We conduct an in-depth examination of security and
robustness challenges in XAI,
including adversarial
attacks on explanations, fairwashing, and explanation
manipulation, and critically discuss emerging defense
and reliability assessment strategies.

• We systematically analyze current evaluation practices
the majority of stud-
for XAI, demonstrating that
ies rely on computational metrics while underutilizing
human-centered evaluation frameworks, and we identify
key limitations related to scalability, standardization,
and user trust.

• We bridge technical, human-centered, and regulatory
perspectives by explicitly discussing the gap between
existing XAI methods and legal requirements such as the
GDPR right to explanation, thereby clarifying practical
challenges in real-world deployment.

VOLUME 14, 2026

27395

---

<!-- PAGE 3 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

FIGURE 1. Conceptual classification of XAI methods based on key taxonomic axes such as model dependency, coverage,
and timing of explanation.

• We synthesize recent advances and open challenges to
outline a forward-looking research roadmap toward XAI
2.0, emphasizing the need for human-aligned, adversari-
ally robust, and regulation-aware explainability systems,
particularly in the context of foundation models and
multimodal AI.

The paper is organized as follows. Section II outlines
the scope of the review and the methodology employed.
Section III provides an overview of core XAI principles
and major techniques. Applications in the fields of finance,
healthcare and cybersecurity are presented in Section IV.
Section V discusses explanation robustness, including adver-
sarial risks and defense approaches. Section VI evaluates
assessment practices, emphasizing the need for human-
centered frameworks. Section VII highlights ongoing tech-
nical and ethical challenges, as well as potential research
directions. Section VIII acknowledges the limitations of the
review. Section IX concludes by presenting the main insights
and providing a roadmap for future XAI research.

II. REVIEW SCOPE AND APPROACH
Three main research questions (RQ1–RQ3) guide this review.
RQ1 focuses on identifying the main XAI methods and exam-
ining how they are systematically categorized across different
model types and explanation paradigms. RQ2 investigates
how XAI applications address domain-specific challenges,
particularly in high-stakes contexts such as finance, health-
care, and cybersecurity. RQ3 examines the potential limi-
tations and risks associated with deploying XAI systems,
including issues related to security, robustness, and regulatory
compliance.

The formulation of these research questions was informed
by an iterative analysis of existing XAI surveys and recent
application-driven studies. While prior works have exten-
sively addressed individual aspects such as the definition

and classification of XAI methods, our review identified
that these dimensions are often examined in isolation, with-
out being systematically linked to deployment challenges,
evaluation practices, and regulatory considerations. In this
context, RQ1 does not aim to introduce an entirely novel tax-
onomy; instead, it synthesizes widely accepted classification
dimensions into a unified and deployment-oriented frame-
work that serves as a foundation for the subsequent analysis
in RQ2 and RQ3. This integrative formulation enables a
coherent examination of how methodological choices in
XAI influence real-world applicability, security, and com-
pliance in high-stakes settings. To position our contributions
within the broader literature, Table 1 compares the scope of
this review with that of earlier surveys. This demonstrates
that, although previous studies have investigated individual
aspects of XAI, such as technical methods, applications in
specific sectors and ethical concerns, only a limited number
have considered these dimensions together in an integrated
manner.

To address these research questions, we have adopted
a structured thematic synthesis approach to comprehen-
sively cover the rapidly evolving field of XAI. Although
our approach is informed by systematic review principles,
we do not strictly adhere to formal protocols such as
PRISMA. This is because XAI research is dynamic, and it
is important to incorporate recent developments, including
preprints and technical reports that have not yet com-
pleted peer review. This methodological choice allows us to
identify emerging trends in foundation model interpretabil-
ity and address current deployment issues that would be
excluded by rigid temporal or publication-type constraints.
Our literature search targeted four major academic databases,
which we selected for their comprehensive coverage of
the field. IEEE Xplore and the ACM Digital Library for
computer science and engineering publications; Scopus for

27396

VOLUME 14, 2026

---

<!-- PAGE 4 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

broad, multidisciplinary coverage; and Arxiv for emerg-
ing research and preprints. The search covered publications
from 2018 to 2025, focusing on the period during which
XAI transitioned from a specialized research area to a critical
component of responsible AI deployment. Search queries
combined core terminology (‘explainable AI’, ‘XAI’, ‘inter-
pretable machine learning’, ‘interpretability’, ‘transparency’)
with domain-specific keywords related to methods (e.g.
‘LIME’, ‘SHAP’, ’attention mechanisms’), applications (e.g.
‘healthcare’, ‘finance’, ‘cybersecurity’), and cross-cutting
concerns (e.g. ‘fairness’, ‘robustness’, ‘evaluation’, ‘human-
centredness’). Boolean operators were used to systematically
combine these terms, and an English-language constraint
was applied to ensure consistency of analysis. The initial
search yielded a substantial body of literature that was poten-
tially relevant. The screening process proceeded in multiple
stages. First, the titles and abstracts of the literature were
reviewed to identify studies that addressed XAI methods,
applications, evaluation frameworks, security and robustness
considerations, or deployment challenges directly. Studies
focusing exclusively on general machine learning without
considering explainability, or providing only speculative
commentary without making any empirical or methodolog-
ical contributions, were excluded at this stage. Duplicate
articles appearing across multiple databases were identified
and removed. The remaining articles were then subjected to
a full-text review, which applied stricter eligibility criteria.
In order to be considered, studies had to provide substan-
tive empirical evidence, propose or evaluate specific XAI
techniques, or offer critical analysis relevant to our research
questions. Articles lacking sufficient methodological detail
or not directly contributing to the understanding of XAI
systems were excluded. We systematically extracted informa-
tion from the included articles and organized it around our
three research questions. The following key data points were
included: (1) characteristics of the XAI method (ante-hoc vs.
post-hoc; model-specific vs. model-agnostic; local vs. global
scope), (2) the application domain and specific use cases,
(3) the evaluation approaches employed (computational met-
rics; human-centred assessment; or hybrid methods), and
(4) considerations relating to security, robustness, and reg-
ulatory compliance. Articles were classified into thematic
categories through iterative discussion among the authors.
Any disagreements that arose during classification were
resolved through consensus and reference to established
XAI taxonomies in prior surveys. This approach was both
structured and flexible, enabling us to capture the technical
diversity of XAI methods and the contextual nuances of their
deployment across high-stakes domains. Figure 2 provides
a schematic overview of our literature search and selection
process.

FIGURE 2. Schematic overview of literature search and selection process.

III. CONCEPTS AND TAXONOMIES OF XAI
The understanding of XAI requires engagement with several
taxonomic dimensions that do not always align in straight-
forward ways. When selecting an explanation method,

practitioners must consider the interdependency of their
choices. Model-specific approaches offer high fidelity, but
cannot be applied across different models. In contrast,

VOLUME 14, 2026

27397

---

<!-- PAGE 5 -->

TABLE 1. Difference between our survey and other survey papers of a similar nature.

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

model-agnostic methods provide flexibility at the cost of
reduced accuracy. Local explanations address the needs of
individual users, but they do not consider broader structural
biases. Global explanations capture system level patterns.
However, they can overload decision makers. On the one
hand, ante hoc interpretability ensures fidelity but restricts
model capacity. On the other hand, post hoc explanations
allow the use of more complex models but may produce
approximations that are not fully reliable. These trade-offs
mean that no single XAI method is universally optimal. The
suitable option is dependent on the application context, the
proficiency of the users and whether the primary goal is trou-
bleshooting, regulatory alignment or establishing confidence.
This section provides a foundation for understanding these
design considerations and their implications.

In order to introduce a certain degree of order to this com-
plex landscape, we have introduced a taxonomy in Table 2
that organizes XAI methods according to a variety of crite-
ria. This framework enables practitioners to identify suitable
explanation techniques based on deployment requirements,
user expertise, and regulatory constraints. Table 2 forms the
basis of the taxonomy employed throughout this analysis.
These categories are not merely conceptual distinctions, but
reflect the practical choices that professionals must make
when implementing XAI systems. The following subsec-
tions examine each dimension in detail and discuss how
these design decisions affect the quality of explanations,
computational requirements, and user comprehension.

XAI is a broad research area focused on making the rea-
soning processes of AI systems more understandable. This
field has grown rapidly and now encompasses a variety of
methods developed for different purposes. Clear conceptual
models and structured taxonomies are essential to navigate
this variety [26]. This section summarizes core XAI princi-
ples and highlights influential taxonomies from recent work,
offering guidance on selecting the most suitable explanation
techniques. Figure 1 provides a visual overview of XAI meth-
ods. These are organized around three key factors. The first

factor is the underlying model. The second factor is the scope
of the explanation. The third factor is the timing of the inter-
pretability process. This framework illustrates how different
approaches occupy distinct positions in the design space, each
with its own strengths and limitations. The XAI landscape
is diverse, there is no single solution that outperforms all
others. Therefore, selecting the right method requires an
understanding of how these dimensions interact and shape
the resulting explanations. The following subsections pro-
vide more detailed exploration of each factor and emphasize
the principles that support effective and meaningful XAI
practice.

A. FUNDAMENTAL PRINCIPLES OF EXPLAINABILITY
Meaningful explanations strike a balance among various
attributes. Interpretability is the ability to understand how
a model works on the inside, while explainability is the
ability to explain how a model works in terms that people
can understand [28]. A radiologist analyzing a diagnostic AI
necessitates distinct explanations compared to a data scientist
troubleshooting the identical model. Fidelity assesses the
extent to which explanations accurately represent authentic
decision-making processes [29]. Low-fidelity explanations
trick users into thinking they know what’s going on, which is
worse than not knowing what’s going on. Comprehensibility
makes sure that people can understand explanations without
having to think too hard. An explanation that is completely
true to model mechanics but makes no sense to the per-
son who is supposed to use it is not useful. Finally, scope
sets apart local explanations that clarify individual choices
from global explanations that sum up how the whole model
works [30].

B. MODEL-SPECIFIC AND MODEL-AGNOSTIC
APPROACHES
A prevalent taxonomy categorizes methods according to their
reliance on particular machine learning models [31], [32].
Model-specific methods are designed to take advantage of

27398

VOLUME 14, 2026

---

<!-- PAGE 6 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

TABLE 2. XAI concepts and taxonomies.

the internal structure of certain model families [33]. They
usually have better accuracy and are faster at processing.
For instance, following decision tree paths shows reasoning
clearly and directly [34], and linear model coefficients show
the effect of each feature directly. In deep learning, Grad-
CAM (Gradient-weighted Class Activation Mapping) makes
visual explanations by using heatmaps to show important
parts of an image.

Model-agnostic methods look at the input-output rela-
tionships of models without looking at their internal struc-
ture [31], [32]. This adaptability permits utilization across any
machine learning model, which is advantageous in industrial
contexts where proprietary models are impervious to scrutiny.
Two main methods stand out and should be looked at closely.
LIME (Local Interpretable Model-Agnostic) trains simple

surrogate models that make predictions about black boxes in
a specific area [35]. SHAP (Shapley Additive exPlanations)
uses Shapley values from cooperative game theory to figure
out how much each feature contributes [36], [37]. SHAP
provides unique feature explanations, but calculating exact
values can be computationally demanding. For a model with
M features, all 2 to the power of M feature combinations
must be evaluated. This issue is usually resolved by using
approximate methods. Kernel SHAP reduces the number
of evaluations required by applying weighted linear regres-
sion, typically needing only 2,000 to 5,000 evaluations per
explanation. Tree SHAP uses the structure of decision tree
ensembles to perform calculations in polynomial time, mak-
ing the process about 2.5 times faster than Kernel SHAP [38].
These approximation methods involve significant trade-offs.

VOLUME 14, 2026

27399

---

<!-- PAGE 7 -->

TABLE 3. Practical guide: Matching XAI methods to user needs.

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

In real-world datasets where variables are often correlated,
the importance scores produced by Kernel SHAP can be inac-
curate because it assumes feature independence. For instance,
income and credit history are usually highly correlated in loan
applications, causing independence assumptions to produce
inaccurate results. Tree SHAP avoids this assumption, but it is
limited to tree-based models. Researchers have proposed con-
ditional SHAP variants to account for feature dependencies,
yet they increase computational complexity [39]. Despite
these advances, fundamental challenges remain. Approxi-
mate methods rely on simplifying assumptions, while exact
methods remain computationally infeasible for complex
models.

C. OTHER TAXONOMIC CLASSIFICATIONS
The timing of explanation generation differentiates ante-hoc
from post-hoc methods [40]. Ante-hoc approaches integrate
interpretability directly into the model architecture using
transparent structures, such as linear or logistic regression
and shallow decision trees. These models precisely reflect the
model logic, as the explanation mechanism is identical to the
model itself. However, models designed for interpretability
often underperform compared to black-box models when
it comes to tasks requiring complex pattern recognition.
This creates a dilemma in high-stakes applications. The
dilemma lies in whether to prioritize interpretability at the
cost of a potentially non-negligible reduction in predictive
performance, or to favor high-performing but less transpar-
ent black-box models. Notably, this accuracy–interpretability
trade-off is not universal, and recent studies argue that
interpretable models can achieve competitive performance,
particularly in high-stakes decision-making scenarios [41].
Post-hoc methods, by contrast, generate explanations after
training by analyzing pre-trained black-box models [42].
This approach allows us to understand complex sys-
tems, such as deep neural networks, as demonstrated by
methods like LIME, SHAP, and Grad-CAM [43]. Post-
hoc explanations can be classified according to their
approach: feature attribution evaluates the contribution of
each input to the model’s output; counterfactual explana-
tions identify minimal changes to inputs that would lead to

different outcomes; and example-based explanations inter-
pret decisions by referencing relevant instances from the
training data [2]. Understanding these classifications pro-
vides guidance for selecting appropriate techniques and
highlights that every choice involves trade-offs between
fidelity, interpretability, computational cost, and scope of
applicability.

D. CRITICAL PERSPECTIVES ON CURRENT XAI
TAXONOMIES
While these taxonomies provide a useful structure, impor-
tant conflicts remain. A key trade-off exists between fidelity
and interpretability. Model-specific methods offer high
fidelity, but lack generalizability; conversely, model-agnostic
approaches sacrifice some fidelity for broader applicability.
Empirical studies highlight these challenges. Schlegel et al.
[35] show that LIME explanations can be unstable in high-
dimensional data. Slack et al. [13] demonstrate that SHAP
explanations can be easily manipulated, with attacks chang-
ing 90 percent of explanations while keeping 75 percent of
the model’s original accuracy. Table 3 provides guidance
to help match XAI methods to specific use cases, translat-
ing taxonomic concepts into practical recommendations for
different users and contexts. This emphasizes the fact that
effective XAI use depends on selecting methods according to
the application, rather than following general best practices.
The next section evaluates the performance of these methods
in real-world settings and explores additional deployment
challenges.

IV. DOMAIN-SPECIFIC APPLICATIONS OF XAI
Table 4 shows that matching explanation methods to dif-
ferent types of users and decision contexts can help people
make better decisions. This shows that good XAI isn’t about
finding the best methods for everyone; it’s about choosing
methods that fit the user’s level of knowledge, the task at
hand, and the limitations of the deployment. The text gives an
overview of how XAI is used in important areas like finance,
healthcare, and cybersecurity. It then goes into detail about
each application, including its use cases, goals, and meth-
ods. This structured overview highlights the requirements
specific to each domain and the challenges that affect more

27400

VOLUME 14, 2026

---

<!-- PAGE 8 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

TABLE 4. Domain-specific applications of XAI.

than one application area. The applications in Table 4 show
that XAI has the power to change many different fields.

But being able to do it technically isn’t enough for a suc-
cessful deployment. It is very important to carefully look at

VOLUME 14, 2026

27401

---

<!-- PAGE 9 -->

domain constraints, user expertise, and regulatory require-
ments. The following subsections will look at each sector in
detail, covering both the successes and the problems that keep
coming up.

Theoretical XAI frameworks demonstrate their true sig-
nificance when utilized in practical scenarios. In high-stakes
areas where choices have a direct effect on people’s lives, the
economy, and national security, XAI has gone from being a
nice-to-have technology to an ethical and operational must-
have. This section looks at how XAI is used in three important
fields: finance, healthcare, and cybersecurity. It also talks
about the Human-Centered XAI paradigm that underlies all
of them.

A. XAI IN THE FINANCIAL SECTOR
The financial sector is one of the main users of algorithmic
decision-making, which has led to more calls for transparency
from both regulators and customers [45]. Black-box models
can make decisions that are not clear and may be biased,
which can lead to big financial losses and legal penalties [46].
XAI gives us important tools to lower these risks in a number
of different areas.

XAI methods, especially SHAP, show important factors
that affect loan outcomes by measuring how much each fea-
ture contributes [47], [48]. But the computational burden for
millions of customers slows down real-time decision-making,
and it’s still not clear if SHAP visualizations are legally suffi-
cient explanations under GDPR. This shows the gap between
academic feasibility and operational compliance.

XAI explains why transactions were flagged, which helps
analysts quickly look into alerts [49], [50], [51]. An explana-
tion that says ‘‘first international transaction from new device
at unusual hour’’ is more important than the amount of the
transaction being slightly above average. This cuts down on
the time spent on false positive investigations by 60% and
increases the number of detections.

It is very important to explain how complex models used
for high-frequency trading and portfolio optimization make
decisions in order to test strategies and understand how peo-
ple act when the market is unstable. XAI boosts portfolio
managers’ trust in algorithmic strategies and improves risk
management by explaining why a model chooses to buy or
sell certain assets [52]. In short, XAI in finance is important
for building trust, making sure rules are followed, and making
automated decision-making processes work better.

B. XAI IN THE HEALTHCARE SECTOR
Healthcare professionals need to trust AI for it to be used
in their field, especially when the decisions made by the
model have a direct effect on patients’ lives. Because doctors
are ultimately responsible, understanding how AI works is
not a nice-to-have, but a must-have for integrating it into
clinical workflows [53]. XAI is an important way to build
this trust. In diagnostic fields such as radiology, pathology,
and dermatology, Convolutional Neural Networks (CNNs)

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

can equal or surpass the performance of experts in the analysis
of medical images. Grad-CAM and other model-specific XAI
techniques create visual explanations by highlighting parts of
an image that had the biggest effect on decisions. This gives
clear visual proof [54], [55]. But the most important thing
is that the explanation is reliable. Recent studies show that
visual explanation methods have serious weaknesses. Stud-
ies indicate that heatmap-based explanations may emphasize
non-pathological image regions that inadvertently correlate
with disease in training datasets, rather than authentic dis-
ease indicators. In a recorded instance, a model accurately
detected the presence of disease, but this determination was
predicated on an extraneous watermark that appeared more
frequently in images of diseased patients. This is a big prob-
lem for doctors because they might trust AI recommendations
that make wrong predictions based on bad reasoning if they
use explanation visualizations. In medical contexts, this issue
of reliability is more than just a technical problem; it is a
patient safety issue that needs to be carefully checked before
being used in a clinical setting [56]. This risk emphasizes that
in healthcare, explainability is not only technical but essential
for clinical safety and accountability. Unreliable explanations
can create a false sense of security and cause mistakes in
diagnosis. XAI is important for more than just diagnostics; it
is also important for models that predict patient risk scores
or suggest personalized treatments. Clinicians must com-
prehend the rationale behind recommendations to trust and
implement them. XAI does this by explaining the things that
lead to high-risk classifications, which makes it possible to
make smart decisions about how to intervene [57], [58]. Addi-
tionally, counterfactual explanations can directly influence
treatment strategies by addressing hypothetical inquiries [59].
In summary, XAI in healthcare is changing from a tool
for making things clear to a necessary part of making sure
patients are safe, improving clinical decision-making, and
holding professionals accountable.

XAI applications in healthcare extend beyond medical
imaging to clinical decision support systems (CDSS) and
pharmaceutical research. In CDSS, for example, explainable
models can help clinicians to understand why a patient has
been classified as high-risk, enabling targeted preventive
interventions to be implemented. Counterfactual explanations
provide answers to clinically actionable questions, such as
’If the patient’s blood pressure had been 20 mmHg lower,
would their sepsis risk score have decreased by 15%?’,
thereby informing treatment decisions directly [57], [58].
These explanations bridge the gap between AI predictions
and clinical reasoning, enabling practitioners to validate AI
recommendations against their expertise and identify poten-
tial errors in the model before they affect patient care.
In drug discovery and molecular property prediction, XAI
has become essential for speeding up compound screen-
ing and identifying structure-activity relationships [111],
[112], [113]. Graph neural network explanations reveal which
molecular substructures contribute to desired pharmacologi-
cal properties, enabling medicinal chemists to design more

27402

VOLUME 14, 2026

---

<!-- PAGE 10 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

effective compounds while avoiding toxic structures. Recent
advances in chemistry-intuitive explanation methods, such
as substructure masking, provide interpretations that align
with established chemical principles. This enables scientists
to validate AI predictions against their own knowledge of
the field. As Jiménez-Luna et al. emphasize in their compre-
hensive review of drug discovery in, explainability bridges
the gap between AI’s predictive power and the mechanistic
insights required for experimental validation and regulatory
approval [111].

C. XAI IN CYBERSECURITY
Every day, cybersecurity analysts get thousands of alerts
about possible threats. Without explainability, these alerts just
mark IP addresses or files as suspicious without giving a
reason, which means that each incident has to be looked into
by hand. XAI changes this workflow by giving you infor-
mation that you can use. XAI shows specific evidence that
sets off alerts in intrusion detection, such as unusual packet
sizes that suggest data exfiltration attempts, communication
patterns that match known malicious hosts, or behavioral
sequences that are typical of certain types of attacks [60],
[61]. When an analyst sees the phrase ‘‘flagged due to a
10MB outbound data transfer to an unknown IP address
at 3pm,’’ they know right away how serious the threat is
and what to do about it. But when they see the phrase sus-
picious activity detected, they have to spend time looking
into it. This contextual understanding speeds up incident
response from hours to minutes and lowers the number of
false positives by letting analysts quickly ignore harmless
anomalies. Malware analysis also benefits from explanations
that show which file characteristics caused the classifica-
tion [62]. XAI identifying particular API call sequences,
code segments, or behavioral patterns facilitates analysts’
comprehension of new malware families and evolving attack
vectors. Instead of seeing AI as a mysterious oracle, security
teams use it to learn things that help them make decisions
about how to protect themselves and gather information about
threats.

Applications of XAI in cybersecurity extend beyond intru-
sion detection and malware analysis to encompass botnet
detection, phishing and spam filtering, and digital foren-
sics [48], [59], [74], [114]. In the case of botnet detection,
for example, explainable models can identify coordinated
malicious traffic patterns by revealing which network flow
features indicate botnet activity, such as synchronized con-
nection timestamps, shared command-and-control server
communications or anomalous DNS query sequences [114].
These explanations enable security analysts to distinguish
between legitimate distributed systems and malicious bot-
nets, thereby reducing the number of false positives that
affect purely statistical approaches. Understanding which
features trigger alerts enables analysts to refine detection
rules and adapt to evolving attack tactics. Phishing and
spam detection also benefit from XAI methods that highlight

deceptive linguistic patterns and suspicious URL features.
Natural language processing–based explainability techniques
reveal which words, phrases, or structural elements trigger
malicious classifications, helping users to understand why an
email has been flagged [48]. In digital forensics, XAI sup-
ports incident investigations by providing causal explanations
of attack sequences and counterfactual analyses that trace the
provenance of security breaches. This helps to answer critical
questions such as ’Which initial access vector enabled the
attacker to escalate privileges?’ These applications demon-
strate that XAI is not merely a tool for model transparency, but
a practical necessity for the implementation of AI in security-
critical contexts, where analysts must be able to trust and
verify AI-generated insights quickly.

V. SECURITY AND ROBUSTNESS PERSPECTIVES
Table 5 lists the different kinds of security threats that XAI
systems face and the best ways to protect against them.
It separates attack vectors that target the disclosures them-
selves, like forgery and fairwashing, from defense strategies
that make disclosures stronger and more reliable. Table 5
shows that the threat landscape needs more than just tra-
ditional adversarial robustness to protect disclosures. The
subsequent subsections conduct a thorough analysis of these
vulnerabilities, evaluating the effectiveness of various attack
methodologies and the practicality of the proposed defense
strategies. The advent of XAI seeks to address the core chal-
lenge of trust in opaque models. However, it is important
to note that explanations create new vulnerabilities because
enemies can change them while keeping predictions the
same [13], [14]. This part talks about the threat landscape,
how well attacks work, and new ways to protect against them.

A. ADVERSARIAL ATTACKS ON XAI EXPLANATIONS
Beyond adversarial manipulation, XAI systems face three
additional critical threats that undermine the reliability of
deployment. Firstly, privacy leakage occurs when explana-
tions inadvertently reveal sensitive information about the
the model architecture or individual data
training data,
points [115], [116], [117]. Model
inversion attacks can
reconstruct approximate training samples from explana-
tion outputs, while membership inference attacks exploit
gradient-based explanations to determine whether specific
individuals were included in the training set. Recent research
shows that multiple explanation methods, including SHAP,
LIME and gradient-based attributions, create privacy vulner-
abilities that could violate regulations such as the GDPR.
The trade-off between privacy and transparency is partic-
ularly acute in healthcare and finance, where explanations
must balance regulatory requirements for transparency with
confidentiality obligations.

Secondly, over-reliance on explanations can lead to
automation bias, whereby users uncritically accept AI deci-
sions simply because an explanation is provided, regardless
of the quality of the explanation or the correctness of
the model [118], [119], [120]. Empirical human-computer

VOLUME 14, 2026

27403

---

<!-- PAGE 11 -->

TABLE 5. Security and robustness perspectives in XAI.

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

instead,

interaction research shows that explanations often fail
to improve human-AI team performance;
they
increase acceptance of AI recommendations, even incorrect
ones [119]. Bansal et al. found that explanations increased
users’ likelihood of accepting AI suggestions regardless of
their accuracy, thus failing to achieve the expected appro-
priate trust calibration [119]. Buçinca et al. demonstrated
that cognitive forcing interventions, which require users to
make initial judgements before seeing AI recommendations,
were necessary to reduce overreliance. However, users rated
these interventions least favourably [118]. This phenomenon
is particularly problematic in high-stakes domains, where
simplified explanations can create a false sense of confidence
in the reliability of the model. Thirdly, the misinterpreta-
tion of explanations can pose fundamental challenges to
the effective collaboration between humans and AI [121],
[122], [123]. For instance, users frequently conflate feature
importance with causality, or interpret saliency maps as literal
representations of what the model ‘sees’, rather than as gra-
dient approximations. Xuan et al. demonstrated that highly
comprehensible explanations are exceptionally susceptible to
misinterpretation. Users infer information that lies outside

the scope of the explanation. They remain overconfident
when they misinterpret it [121]. For example, a clinician
might incorrectly assume that a Grad-CAM heatmap high-
lighting a specific anatomical region proves that the model’s
diagnostic reasoning aligns with medical knowledge when,
in fact, the heatmap merely reflects gradient magnitudes.
Nguyen et al.’s study found that feature attribution was no
more effective than showing the nearest training examples
for human decision-making [123]. Without proper training
in explanation semantics, users risk making critical decisions
based on fundamentally flawed interpretations.

Conventional adversarial attacks modify model inputs to
change predictions, but new research shows that attacks can
also target XAI explanations directly [13]. The most dan-
gerous thing about them is that they can change prediction
explanations a lot without changing model outputs [14].
This lets attackers keep the model’s decisions correct while
making up all the evidence that supports them. This kind
of manipulation, which is often called a ‘‘spoofing attack,’’
takes advantage of users’ trust by giving them plausible but
fundamentally false reasons [66]. The real-world effects are
very bad. Think of a medical imaging model that can find

27404

VOLUME 14, 2026

---

<!-- PAGE 12 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

a tumor in an X-ray. An attacker could add noise to the
image that is too small to see, which would make explanation
methods like Grad-CAM highlight areas that aren’t impor-
tant, like healthy tissue or artifacts in the image, instead of
the tumor itself [14]. The model’s prediction of the tumor’s
presence is still accurate, but the misleading visualization
could make doctors question the diagnosis, which could delay
important treatment [67]. The threat has been measured in
the following way: Scaffolding attacks have demonstrated
a 90.8% accuracy in annotations while obscuring bias in
credit scoring [13]. Similar methods have been shown to
change descriptions of medical images with a 95% success
rate [14], which leads to the wrong attribution of diagnostic
evidence.

Adversarial attacks go beyond image-based systems and
into tabular domains. In financial situations, a biased credit
model could be used to make SHAP explanations that blame
rejections on valid reasons (like ‘‘high debt ratio’’) while
hiding discrimination based on protected traits. This trick,
known as fairwashing [66], makes ethical auditing less effec-
tive. Biased systems can avoid following the rules (see
Section VII-B). This occurrence engenders a significant para-
dox. It is clear that tools designed to promote openness and
build trust can actually be used to avoid scrutiny and hide
harmful biases. This discovery signifies that the establish-
ment of resilient defenses against malevolent entities must
be prioritized above all else in the field of XAI research.
Attackers usually figure out the changes they need to make
by solving optimization problems that change explanation
maps in certain ways while keeping model predictions the
same [68]. These attacks have been successful with different
types of data, such as images, text, and tables [69]. This shows
how important it is to make sure that explanations are as
strong as model predictions.

B. DEFENSE MECHANISMS AND RELIABILITY
ASSESSMENT
In response to these vulnerabilities, the research community
is actively developing defense mechanisms and reliability
assessment frameworks. The primary objective is generating
explanations that are robust, stable, and faithful to the model’s
genuine reasoning process [70], [71].
➢ Inherently Robust Explanation Methods: One defen-
sive strategy focuses on creating explanation methods
inherently less susceptible to adversarial perturbations.
For example, smoothing techniques averaging expla-
nations over multiple noisy input copies have been
proposed to mitigate instabilities common in gradient-
based methods, reducing sensitivity to minor malicious
perturbations [72]. Beyond these, certified robustness
approaches aim to provide mathematical guarantees
that explanations will remain consistent within prede-
fined perturbation bounds, offering a higher assurance
standard [73].

➢ Reliability Assessment and Sanity Checks: Another
systematic reliability

defensive approach involves

through sanity checks. The fundamen-
assessment
tal principle is measuring explanation stability when
subjected to semantically irrelevant or minor input
variations [74]. Dramatic explanation changes result-
ing from small, random perturbations strongly indicate
unreliability. To enable this, metrics for explanation
robustness or stability have been developed, allow-
ing quantitative comparison of different XAI methods’
reliability [75]. Adversarial Training for Explainers:
Mirroring adversarial training used to fortify models
themselves, it is possible to enhance explanation mech-
anism resilience. This technique involves incorporating
a loss function during training that minimizes both
model prediction error and explanation variability or
inconsistency. By exposing the system to intentionally
perturbed inputs [76], it learns to generate consistent
interpretations even under attack, thereby increasing
overall explainer robustness [77].

Current defenses show promise but face adoption barriers.
Certified robust explanation methods providing mathemat-
ical guarantees reduce attack success from 90% to 34%,
yet remain underutilized in deployment [73]. Computational
overhead increases explanation time by 3-5×, creating oper-
ational friction. Smoothing techniques averaging over noisy
inputs improve stability but assume attackers cannot adapt to
this defense [72]. Adversarial training for explainers shows
effectiveness in controlled settings but
lacks large-scale
deployment validation [76], [77]. Current defenses show
promise but face adoption barriers. Certified robust explana-
tion methods reduce attack success [73], yet computational
overhead increases explanation time by 3 − 5 × . Organiza-
tions must balance security against operational constraints.
In summary, as XAI becomes integral to safety-critical sys-
tems, its own security and robustness must be treated as
critical research objectives. Without reliable explanations, the
promise of transparency risks becoming a potent vector for
manipulation.

VI. EVALUATION OF EXPLANATIONS
To figure out how useful XAI is in the real world, we need to
do a lot of human-centered testing. Fidelity and other com-
putational metrics don’t do a good job of showing whether
users make better decisions [44]. This part talks about why
computational metrics aren’t enough and what makes an
evaluation meaningful.

Table 6 organizes the evaluation landscape into three areas:
human-centered frameworks that measure both subjective
and objective user outcomes, components that define useful
explanations, and ongoing problems with standardization and
scalability. This framework shows why using only computa-
tional metrics isn’t enough to measure how well XAI works.
The evaluation dimensions in Table 6 show that the quality
of an explanation can’t be based only on the properties of
the algorithm. True effectiveness only comes from thorough
human-centered testing that checks if explanations help peo-
ple make better decisions, build trust in the right way, and

VOLUME 14, 2026

27405

---

<!-- PAGE 13 -->

meet user needs. The next few sections go into more detail
about evaluation methods and problems that keep coming up
in this area.

A. HUMAN-CENTERED EVALUATION FRAMEWORKS
Human-centered evaluation sees explanations as ways to
communicate and measures their effectiveness by how they
affect people, not by how well
they work with algo-
rithms [78]. This necessitates regulated user studies that
gather both qualitative and quantitative data, establishing iter-
ative development cycles in which human feedback directly
influences system enhancement, as depicted in Figure 3.

Human-centered evaluation looks at two different things.
First, subjective perception looks at user satisfaction, trust,
understandability, and perceived adequacy through surveys
and interviews [79], [80]. These metrics show whether users
think the explanations are credible and helpful for the deci-
sions they need to make [81]. Second, objective performance
measures the concrete impact of tasks [82], [83]. Standard
evaluation frameworks encompass various practical configu-
rations. In one method, users look at the model’s explanation
and then try to guess how it will act on new, unseen data.
If they guess correctly, it means that the explanation did a
good job of conveying knowledge. In another method, users
are asked to find biases or mistakes that were put into the
model on purpose. The speed and accuracy with which they
find them shows how well the explanation shows weaknesses.
Lastly, users can make decisions with or without explana-
tions, and the fact that their decisions get better shows that
the explanations are useful in real life. Systematic analysis,
on the other hand, shows worrying trends. Akhtar et al. [44]
found 30 different evaluation components in the studies they
looked at. This shows that assessment needs to be done in
a way that takes into account trust, comprehensibility, task
performance, and user satisfaction. Nevertheless, merely 26%
of studies utilized established frameworks. Trust was the
most commonly assessed dimension in 46 out of 77 studies;
however, results regarding the efficacy of explanations varied
significantly according to user expertise and task complexity.
This variability stems not from XAI method limitations but
from failure to account for context-dependent factors. A clar-
ification that helps data scientists fix models might confuse
doctors who are trying to make a diagnosis. Kadi et al. [84]
discovered that although the utilization of quantitative eval-
uation methods rose from 40% in 2016 to 70% in 2020, the
rates of user studies remained constant at approximately 20%.
This difference between computer evaluation and human val-
idation is why systems that work well in the lab often fail
when they are put into use.

Figure 3 shows the iterative human-in-the-loop XAI devel-
opment
lifecycle. It shows how system design, human
evaluation, and refinement all work together in a continu-
ous feedback loop. This process model signifies a pivotal
transformation from perceiving explanations as static outputs
to recognizing them as dynamic communication instruments

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

FIGURE 3. The human-in-the-loop XAI development and evaluation
lifecycle, emphasizing iterative improvement and human-centric
assessment for trustworthy AI systems.

enhanced through systematic user interaction. The itera-
tive lifecycle shown in Figure 3 is the best way to build
human-centered XAI systems. However, as the following
analysis shows, this model doesn’t always match up with how
research is actually done. Most studies don’t use rigorous
human evaluation and instead rely only on computational
metrics.

B. COMPONENTS OF A MEANINGFUL EXPLANATION
In addition to human-centred evaluation frameworks, techni-
cal metrics provide a quantitative assessment of the quality
of explanations that is essential for a systematic compar-
ison. Localization metrics evaluate whether explanations
correctly identify relevant input regions, which is partic-
ularly critical for vision tasks [124], [125], [126]. The
pointing game, introduced by Zhou et al., measures whether
the maximum activation in a saliency map falls within
the ground-truth object bounding boxes. Intersection over
Union (IoU) between explanation heatmaps and ground-truth
annotations provides a detailed measurement of spatial over-
lap [124]. Petsiuk et al.’s deletion and insertion metrics assess
faithfulness by measuring how model confidence changes
as pixels are progressively removed or added in order of
attributed importance [126]. Together, these metrics address
the question of whether explanations actually point to the
features on which the model relies. Complexity metrics quan-
tify explanation simplicity, recognizing that overly detailed
explanations may overwhelm users despite being technically
accurate [35], [127], [128]. LIME’s foundational formulation
explicitly includes a complexity penalty (cid:127)(g), favoring sparse
explanations with fewer non-zero feature weights [35].

The complexity of rule-based explanations can be mea-
sured by decision tree depth or the number of conditions.

27406

VOLUME 14, 2026

---

<!-- PAGE 14 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

TABLE 6. Evaluating XAI disclosures.

Empirical evidence from cognitive science indicates that
explanations that highlight three to five key features are
more comprehensible to humans than exhaustive lists of

feature importance,
in line with limitations of working
memory [127], [128]. However, the optimal complexity-
accuracy trade-off remains context-dependent: for example,

VOLUME 14, 2026

27407

---

<!-- PAGE 15 -->

medical diagnosis may require more detailed explanations
than credit decisions. Consistency (or stability) is used to
evaluate whether explanation methods produce similar results
for semantically similar inputs [33], [69], [129]. Álvarez-
Melis and Jaakkola formalized this concept through local
Lipschitz continuity: an explanation method is considered
robust if small input perturbations result in proportionally
minor changes to the explanation [129].

Ghorbani et al. empirically demonstrated that popular
attribution methods are fragile, perceptually identical inputs
can receive vastly different explanations,
indicating low
reliability and potential susceptibility to adversarial manip-
ulation [33]. High consistency is essential for user trust.
If a model provides drastically different explanations for
similar cases, users cannot develop a reliable mental model
of the system’s behaviour. Finally, randomisation tests are
critical sanity checks that verify whether explanation methods
genuinely capture the model’s reasoning or merely gener-
ate visually plausible results. Adebayo et al.’s pioneering
work introduced model parameter and data randomisation
tests: valid explanation methods should produce substan-
tially different results when model weights are randomised.
Their analysis revealed that widely used methods such as
Guided Backpropagation fail these sanity checks, they act
as edge detectors rather than model-specific explainers.
Subsequent work by Kim et al. extended these tests to cre-
ate synthetic evaluation environments with known ground
truth [131]. These sanity checks are essential quality assur-
ance mechanisms. Without them, practitioners risk deploying
explanation methods that provide illusory rather than genuine
interpretability.

Human-centered evaluation reveals that effective expla-
nations must balance multiple interconnected dimensions.
Rather than excelling in a single aspect, meaningful explana-
tions integrate several key components. Fidelity and accuracy
form the technical foundation: explanations must faithfully
represent true model decision-making processes [85]. This
proves particularly challenging for post-hoc methods applied
to black-box models. Low-fidelity explanations mislead
users, potentially causing more harm than original opaque
systems by creating false understanding [86]. Comprehen-
sibility ensures accessibility to target audiences through
appropriate cognitive fit [87]. Drawing from cognitive sci-
ence principles, effective explanations minimize cognitive
load through concise presentation. Visualizations highlight-
ing top 3-5 determining factors typically prove more effective
than exhaustive feature importance lists. Explanation format
must match audience expertise and information processing
capabilities. Contemporary XAI systems increasingly incor-
porate interactivity and actionability. Interactive explanations
enable counterfactual exploration, allowing users to probe
what-if scenarios and develop nuanced model understand-
ing [88]. Actionable explanations extend further by providing
concrete guidance for achieving different outcomes, such as
specifying that ‘‘increasing annual income by $10,000 would

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

significantly improve loan approval likelihood’’ [89]. This
transforms explanations from passive information displays
into practical decision-support tools. However, balancing
these dimensions creates design tensions: highly interactive
systems may overwhelm novice users, while actionable rec-
ommendations risk oversimplifying complex model behavior.
Effective explanation systems must adapt to user expertise,
task context, and decision stakes.

C. CHALLENGES IN STANDARDIZATION AND METRICS
The lack of a standardized evaluation system leads to frag-
mentation that stops real progress. Different studies use
different metrics, which makes it impossible to compare
them directly and makes it hard to tell which methods really
work [90], [91]. This fragmentation is a sign of real complex-
ity: there is no one-size-fits-all explanation, and what works
for radiologists interpreting medical images is very different
from what loan officers need to make credit decisions. But the
lack of standards goes beyond context-dependence to include
methodological inconsistency. Akhtar et al. [44] discovered
studies that assessed trust using 15 distinct instruments, sat-
isfaction through 12 varied scales, and comprehensibility via
8 different evaluation methods. Without standardized metrics,
one study’s ‘‘high user satisfaction’’ cannot be compared to
another’s, hindering the accumulation of knowledge. Scala-
bility of human-centered evaluation poses further challenges.
It costs $15,000 to $50,000 to do a full human experiment,
and it takes months to finish [84]. This cost explains why so
few people use it: only 22% of papers include human subjects.
Researchers are forced to use automatable proxy metrics that
are close to human judgment because they don’t have enough
resources [92]. Still, it’s not clear how well computational
proxies reflect human understanding, trust, and the quality
of decision-making. A metric that works with human judg-
ments in one study might not work in other situations, with
different levels of expertise, or in different task areas. To deal
with these problems, infrastructure development needs to be
coordinated. The research community requires collaborative
evaluation platforms featuring standardized protocols, uni-
form datasets that facilitate reproducible comparisons, and
meticulously crafted benchmarking tasks that encompass var-
ious application domains and user proficiency levels. Big
funding groups should start programs to help this infrastruc-
ture. Without standardized frameworks, XAI development is
limited because it is impossible to say for sure which methods
work best for making decisions in certain situations.

D. HUMAN-CENTERED DESIGN CONSIDERATIONS
The ultimate effectiveness of any explanation relies on
the human user, a principle that
transcends all applica-
tion domains. Human-Centered XAI (HCXAI) is a model
that says explanations must be not only technically correct
but also easy to understand, use, and help end users [63].
An explanation that is completely true to the mechanics
of the model but too hard for a doctor or loan officer to

27408

VOLUME 14, 2026

---

<!-- PAGE 16 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

understand is not very useful in practice. So, HCXAI sup-
ports the idea of making and testing explanations that are
based on the needs, skills, and cognitive profiles of dif-
ferent users. This research framework utilizes user studies
and surveys to assess the impact of explanations on trust,
decision-making enhancement, and the facilitation of human-
system interaction [64], [65]. The transition from purely
technical XAI to Human-Centered XAI signifies a pivotal
paradigm shift towards the development of systems intended
for collaboration rather than mere understanding. In short,
XAI applications that are specific to a certain field have the
potential to change the way things work by making them
more open and accountable in areas where these traits are
necessary. To fully realize this potential, though, we need to
close important gaps between technical feasibility, regulatory
compliance, and human-centered design.

VII. CHALLENGES AND FUTURE RESEARCH DIRECTIONS
XAI has made a lot of progress in making it easier to under-
stand complicated models. Yet this algorithmic maturity has
not translated into widespread deployment success in high-
stakes domains. Three main problems stop XAI from keeping
its promise of reliable AI. First, technical scalability limits:
techniques made for models with millions of parameters can’t
work with foundation models that have hundreds of billions
of parameters. Second, there are gaps in ethics and rules: the
legal requirements for explainability don’t have clear defini-
tions, which makes it hard to know if you’re following the
rules. Third, the explainability crisis in large-scale models:
as models get more complicated, the amount of behavior that
can be explained goes down. Right now, only 65% of the
variance in state-of-the-art systems can be explained [93].
These problems are not separate from each other. The costs
of computation make it hard to scale up evaluations, which
makes it impossible to check if explanations meet regulatory
standards. Unclear laws make people less likely to spend
money on costly human-centered evaluation. The opacity of
foundation models makes both technical methods and human
understanding less effective. To deal with these problems,
we need to move from XAI 1.0’s focus on making explana-
tions to XAI 2.0’s focus on making explanation systems that
are human-aligned, adversarially robust, and follow the law
[94]. This section looks at each challenge, rates how bad it is,
and suggests specific research directions. Table 7 talks about
the problems and future research directions in XAI.

A. THE TRANSITION FROM XAI 1.0 TO XAI 2.0
XAI research evolved through two successive paradigms.
XAI 1.0, emerging between 2015-2023, focused on tech-
nical
transparency with a core objective of generating
explanations for any pre-trained model [94]. Success was
measured by computational metrics: fidelity to underly-
ing models, robustness against perturbations, and compu-
tational efficiency. Representative methods included LIME
for local approximations, SHAP for game-theoretic fea-
ture attribution, and Grad-CAM for visual explanations.

These methods applied post-hoc explanations to already-
trained models. The underlying assumption: more informa-
tion about model decisions would naturally translate to better
human understanding and appropriate trust. XAI 2.0 repre-
sents fundamental paradigm shift [94]. Rather than simply
explaining model decisions,
the goal becomes enabling
informed human decision-making through interactive expla-
nation systems. Evaluation shifted from computational met-
rics toward human-centered measures: do users actually
make better decisions, can they identify model weaknesses,
do they appropriately calibrate confidence in recommenda-
tions. Methods evolve to include interactive counterfactual
exploration, adaptive formats adjusting to user expertise, and
certified robustness ensuring explanations resist manipula-
tion [95], [96], [97], [98], [99], [100]. This paradigm requires
deep interdisciplinary integration with cognitive science,
human-computer interaction, and legal frameworks. This
transition was driven by practical failures in XAI 1.0. Labora-
tory studies increasingly demonstrated that technically accu-
rate explanations do not reliably improve human decision-
making. More alarmingly, research revealed explanations can
be adversarially manipulated while preserving predictions
(Section IV), meaning transparency can be weaponized rather
than enabling understanding. These findings show that the
basic assumption of XAI 1.0 is incomplete. Transparency
alone does not ensure trustworthiness, and disclosures that are
not human-verified create a false trust in flawed systems. XAI
2.0 emphasizes that explanations must be not only technically
sound but genuinely meaningful, persuasive, and useful to
end-users.

To provide a concise, high-level comparison of these
two paradigms, Table 8 summarizes the key differences
between XAI 1.0 and XAI 2.0 across technical objectives,
evaluation practices, user involvement, security and privacy
considerations, and regulatory alignment.

B. THE REGULATORY-TECHNICAL GAP: WHEN LEGAL
REQUIREMENTS LACK OPERATIONAL DEFINITIONS
Beyond technical hurdles, XAI faces significant challenges
aligning with societal and legal frameworks [101].
➢ XAI enables model bias auditing but simultaneously
complicates accountability. When a discriminatory deci-
sion occurs, determining responsibility among data
providers, model developers, and deploying organiza-
tions presents complex challenges [102]. Section IV
demonstrated that adversarial attacks can undermine
explanation integrity through fairwashing, where biased
models generate explanations concealing discrimina-
tion to evade regulatory oversight [66]. A credit model
internally discriminating based on protected charac-
teristics while explaining decisions through legitimate
factors passes audits relying on explanation-based over-
sight. This creates accountability paradox: organiza-
tions deploying XAI for compliance may inadvertently
enable more sophisticated bias concealment than opaque
systems would permit.

VOLUME 14, 2026

27409

---

<!-- PAGE 17 -->

TABLE 7. Challenges and future research directions in XAI.

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

➢ GDPR’s right to explanation highlights discrepancies
between legal requirements and technical capabili-
ties [15]. No consensus exists on what constitutes legally
sufficient explanation, and presenting users with SHAP
values or heatmaps may not fulfill regulatory man-
dates for meaningful disclosure [16]. This ambiguity
creates practical deployment barriers. A bank imple-
menting SHAP for loan explanations cannot determine
whether this satisfies GDPR until facing regulatory
scrutiny or legal challenge. The technical community
offers a variety of methods, such as feature attribu-
tions, counterfactuals, attention visualizations, natural
language summaries, but there is no guidance on which
approaches meet legal standards or under what condi-
tions. Bridging this gap requires urgent interdisciplinary
collaboration among computer scientists, legal scholars,

and policymakers to establish standards that are both
technically feasible and legally valid [17].

1) THE GDPR COMPLIANCE PARADOX
The European Union’s General Data Protection Regula-
tion introduces transparency requirements through Articles
13-15 and Recital 71, mandating provision of meaningful
information about the logic involved in automated decision-
making [8]. However, translating this legal language into
technical specifications remains unresolved. Legal
inter-
pretation of GDPR requirements remains ambiguous [8],
[15], while technical communities offer diverse explanation
methods (SHAP, counterfactuals, attention visualizations)
each with distinct limitations. SHAP assumes feature inde-
pendence, counterfactuals may suggest infeasible changes,
and attention mechanisms sometimes highlight non-semantic

27410

VOLUME 14, 2026

---

<!-- PAGE 18 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

TABLE 8. Comparison between XAI 1.0 and XAI 2.0 paradigms.

patterns [56]. No regulatory guidance establishes which
approaches satisfy requirements, forcing organizations to
choose methods without knowing whether they achieve
compliance. Resolving the regulatory-technical gap requires
coordinated interdisciplinary effort. Computer scientists must
develop explanation methods with quantifiable fidelity guar-
antees, computational feasibility for deployment constraints,
and robustness against manipulation. Legal scholars need
to clarify what constitutes meaningful information through
analysis of emerging case law and regulatory guidance.
Human-computer interaction researchers should systemati-
cally evaluate which explanation formats effectively com-
municate to different user populations. Policymakers must
balance transparency requirements against technical con-
straints, recognizing that some explanation demands may
prove infeasible for complex models. Organizations imple-
menting XAI systems should document method selection
rationale, validate explanation fidelity through testing, record
user comprehension results, and maintain audit trails [16],
[17]. This documentation demonstrates good-faith compli-
ance efforts even as technical standards evolve, providing

defensible evidence of transparency commitments should
regulators investigate deployment practices. Without such
coordination, the gap between legal requirements and techni-
cal capabilities will continue expanding as model complexity
increases.

2) SCALABILITY LIMITS: WHEN EXPLANATION METHODS
CANNOT KEEP PACE WITH MODEL COMPLEXITY
The emergence of Transformer-based foundation models,
particularly LLMs, poses a fundamental challenge for XAI.
Unlike conventional deep learning systems with millions
of parameters, contemporary foundation models operate at
scales involving hundreds of billions of parameters and
are trained through large-scale pretraining followed by task
adaptation. As a result, explanation techniques originally
designed for smaller models do not scale effectively to these
architectures. This limitation is not merely a computational
bottleneck but reflects a deeper conceptual challenge regard-
ing what interpretability means at extreme model scale.
Recent mechanistic interpretability efforts on Claude 3 Son-
net illustrate both the promise and the limitations of current
approaches. By extracting approximately 34 million internal
features, researchers were able to explain around 65% of
the model’s variance [93]. However, the remaining 35% of
unexplained variance corresponds to internal computational
pathways that remain opaque. This residual uncertainty raises
critical questions: whether these unexplained components
reflect learned representations not yet isolated, emergent
behaviors arising from complex parameter interactions that
resist feature-level interpretation, or methodological artifacts
of current extraction techniques. Until this ambiguity is
resolved, claims of comprehensive interpretability for foun-
dation models remain incomplete and potentially misleading,
particularly for organizations deploying such systems in
safety-critical or regulated environments. Beyond global
interpretability, local explanation and reasoning transparency
in LLMs present even more severe challenges. While models
often generate fluent chain-of-thought (CoT) explanations,
recent studies indicate that these verbalized rationales fre-
quently fail to reflect the model’s actual decision-making
process. Empirical evidence shows that LLMs may men-
tion true causal factors only inconsistently, while omit-
ting or obscuring internal reward-optimizing strategies that
guide predictions [103]. In many cases, models internally
rely on decision logic that diverges from the explanations
they present, creating a dangerous illusion of transparency.
This discrepancy is especially problematic in high-stakes
applications, where explanations are expected to support
accountability, fairness, and regulatory compliance. Fur-
thermore, conventional XAI techniques struggle with the
inherent architectural properties of Transformer-based mod-
els. Attention mechanisms, commonly used as proxies for
interpretability, correlate weakly with true feature impor-
tance and often highlight tokens that contribute minimally
to final predictions while ignoring genuinely influential

VOLUME 14, 2026

27411

---

<!-- PAGE 19 -->

components [104]. As highlighted in recent analyses, expla-
nation faithfulness deteriorates further in complex reasoning
scenarios, where models may employ internal strategies that
are systematically absent from generated explanations [103].
This divergence between internal reasoning and external
explanation constitutes a critical safety concern: a system
may comply superficially with explainability requirements
while internally operating in ways that violate ethical or legal
constraints. From a practical standpoint, computational feasi-
bility compounds these conceptual issues. Perturbation-based
explanation methods, such as SHAP, become economi-
cally infeasible at the foundation-model scale. Explaining
a single prediction from a large LLM can require thou-
sands of GPU-hours, rendering such approaches impractical
for real-time or large-scale deployment [93]. Approximate
methods reduce computational cost but introduce additional
uncertainty regarding explanation accuracy and legal suffi-
ciency. In the absence of clear regulatory guidance defining
acceptable trade-offs between explanation fidelity and effi-
ciency, organizations cannot confidently assess whether such
approximations meet disclosure obligations. Collectively,
these findings demonstrate that explainability challenges in
foundation models extend far beyond computational scala-
bility. The persistent gap between internal model behavior
and externally generated explanations—particularly in local
and causal reasoning contexts—suggests that existing XAI
paradigms may be fundamentally insufficient for LLMs.
Until explanation methods can reliably capture both the
global structure and local decision logic of foundation mod-
els, transparency claims for large-scale AI systems should
be regarded as aspirational rather than empirically estab-
lished. Addressing these challenges will require not only
improved algorithms but also a rethinking of explanation
paradigms tailored specifically to the unique properties of
Transformer-based foundation models.

3) MULTIMODAL EXPLAINABILITY CHALLENGES
Vision-language models (VLMs) introduce a distinct class
of explainability challenges arising from cross-modal inter-
actions between visual and linguistic representations. Unlike
unimodal systems, where explanations can be attributed to
a single input space, VLMs require disentangling how mul-
tiple components—namely the visual encoder, the language
encoder, and the projection or fusion layers—jointly con-
tribute to a model’s prediction. As a result, explaining not
only what the model predicts but which modality dominates
or interacts in the decision-making process becomes a central
challenge. Recent techniques such as CLIP Surgery demon-
strate partial progress by enabling class activation maps with-
out retraining and improving mean Intersection over Union
from 22.11% to 35.95% [105]. However, these approaches
primarily emphasize alignment at the representation level
and offer limited insight into causal modality contributions.
In practice, attention-based visualization methods frequently
highlight non-semantic tokens or background regions, while

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

the influence of projection layers and multilayer perceptron
components often overshadows interpretable attention pat-
terns. Consequently, it remains unclear whether a VLM’s
output is driven predominantly by visual evidence, linguistic
context, or spurious correlations introduced during multi-
modal fusion. This limitation becomes particularly critical in
high-stakes domains. For example, multimodal medical AI
systems that integrate imaging data, clinical notes, and struc-
tured patient records outperform unimodal approaches by up
to 6.2 percentage points in AUC [106]. Yet, without reliable
explanations, practitioners cannot determine whether perfor-
mance gains stem from clinically meaningful cross-modal
reasoning or from shortcuts, such as correlations between tex-
tual metadata and disease prevalence. As highlighted in recent
surveys on explainability for vision-language models, current
XAI techniques struggle to isolate modality-specific causal
contributions and to explain how intermediate fusion layers
influence final predictions [107]. Although emerging frame-
works attempt to combine feature attribution methods (e.g.,
SHAP), attention visualization for cross-modal alignment,
and concept-based explanations for semantic interpretation,
these approaches remain largely exploratory. Moreover, the
absence of standardized evaluation metrics for multimodal
explanations makes it difficult to assess whether generated
explanations faithfully reflect underlying model reasoning
or merely provide post-hoc rationalizations. Addressing
these challenges will require explanation methods explicitly
designed for multimodal architectures, along with evaluation
protocols capable of measuring modality dominance, cross-
modal causality, and explanation faithfulness in complex
vision-language systems.

4) RESEARCH PRIORITIES FOR XAI 2.0
Three research priorities emerge as critical for advancing
XAI toward deployment readiness. First, develop standard-
ized benchmarks and metrics. The absence of standard-
ized evaluation creates fragmentation preventing meaningful
progress [90], [91]. The research community must cre-
ate open-source benchmarking platforms incorporating both
technical and human-centered evaluation criteria. Major
funding organizations should establish coordinated initiatives
supporting creation of standardized datasets and evaluation
protocols across application domains. Success would be evi-
denced by adoption of these standards by more than 50%
of XAI research papers within three years. Second, advance
interactive and adaptive explanation systems. The transition
from static, one-way explanations to dynamic, interactive
systems is fundamental to XAI 2.0 [88], [94]. Future inter-
faces should enable users to customize explanations, adjust
feature importance, and explore counterfactual scenarios,
fostering collaborative dialogue building shared human-AI
understanding. Research should focus on developing systems
where explanations adapt to user expertise level and task con-
text rather than providing identical explanations to all users.
This requires integrating insights from cognitive science

27412

VOLUME 14, 2026

---

<!-- PAGE 20 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

about human explanation processing and human-computer
interaction about intuitive interface design. Third, estab-
lish legally sound technical standards. Bridging the gap
between regulatory mandates like GDPR’s right to expla-
nation and current technical capabilities represents urgent
interdisciplinary challenge [15], [16], [17]. Future research
must collaborate with legal experts and policymakers to
develop testable, enforceable technical standards defining
legally sufficient explanations. This collaboration should pro-
duce concrete guidance that organizations can follow when
designing explanation systems for regulated applications,
specifying which methods satisfy requirements under which
deployment conditions.

These priorities are interdependent. Standardized evalua-
tion enables determining which explanation methods satisfy
regulatory requirements. Interactive systems require eval-
uation protocols measuring whether adaptation improves
user understanding. Legal standards need empirical vali-
dation through human-centered studies. Progress requires
coordinated effort across computer science, cognitive sci-
ence, human-computer interaction, and legal scholarship.
XAI serves as crucial bridge toward making AI not only
more intelligent but also more transparent, accountable, and
aligned with human values. While the path forward presents
substantial challenges, the research directions articulated
here provide clear trajectory for AI to evolve from opaque
black boxes into transparent, understandable, and ultimately
trustworthy partners in human decision-making.

VIII. REVIEW LIMITATIONS AND SCOPE
This comprehensive review has important limitations readers
should consider. First, restricting to English-language publi-
cations may exclude significant research contributions from
academic communities in non-English-speaking regions, par-
ticularly China, Japan, and South Korea where AI research
prioritizes different application domains and methodological
approaches. Second, the databases used (IEEE Xplore, ACM
Digital Library, Scopus, arXiv) may systematically under-
represent technical reports, industry white papers, preprints
not yet peer reviewed, and negative results showing meth-
ods failed. The field’s rapid evolution means very recent
breakthroughs in 2024-2025 may not yet be adequately
indexed, though targeted arXiv searches partially address
this limitation. Third, the domain focus on finance, health-
care, and cybersecurity concentrates findings on sectors with
well-established AI adoption and clear high-stakes decision
contexts. Other important application areas such as legal
reasoning, educational recommendation, environmental fore-
casting, and criminal justice employ AI in fundamentally
different ways where XAI requirements differ substantially.
Fourth, our thematic analysis prioritizes conceptual synthesis
over exhaustive documentation, enabling incorporation of
cutting-edge research but reducing reproducibility. Finally,
XAI evolves rapidly; methods in this review may be super-
seded within months as regulatory landscapes shift and
foundation models create new challenges. Despite these

limitations, our integrated analysis linking technical method-
ologies with security vulnerabilities, evaluation frameworks,
and regulatory requirements offers perspective not yet syn-
thesized in prior XAI surveys.

IX. CONCLUSION
The widespread use of AI systems in important parts of
society’s infrastructure made it necessary for people to be
open and responsible. XAI came about to meet this need by
making the decisions of black-box models understandable
to people. This review looked into whether XAI has kept
its promise. The analysis has uncovered a paradox. Even
though there have been a lot of technical improvements in the
field of XAI, especially in the area of explanation generation,
these improvements have not yet led to real-world success.
There are three main gaps that keep AI from being reliable.
First, explanations create attack surfaces that allow adversar-
ial manipulation [13], [14], and fairwashing lets algorithms
that are biased get around audits. Second, evaluation practices
put more weight on computational metrics than on human
understanding [44], [84], which explains why deployments
fail even when they do well in the lab. Third, regulatory
requirements don’t have clear operational definitions [15],
[16], [17], which makes it hard for businesses to know if they
are following the rules. These problems are not separate; they
are all connected. The high cost of computation makes it hard
to scale evaluations, which means that it is hard to check if
explanations meet regulatory requirements. Legal uncertainty
deters investment in costly human-centered evaluation. The
foundation model’s lack of clarity, with 35% of the variance
unexplained [93], makes both technical methods and human
understanding less useful. The development of reasoning
models in which internal strategies deviate from generated
explanations in more than 97% of instances [105] indicates
inherent limitations within existing explanatory frameworks.
Our study finds three important areas of research that need
to be focused on. First, create standardized benchmarks that
include both technical fidelity and human-centered evalua-
tion criteria. This will make it possible to compare methods
in a way that can be repeated and find out which ones work
best for making decisions in different situations. Second,
make progress on interactive, adaptive explanation systems
that change based on the user’s skill level and the task
at hand, instead of giving the same output to everyone.
Third, work together across disciplines to create legally sound
technical standards that spell out what is a good enough
explanation for regulatory compliance. This review shows
that reliable AI needs more than just advanced explanation
algorithms. It requires a change in thinking from XAI 1.0’s
focus on making explanations to XAI 2.0’s focus on making
explanation systems that are human-aligned, adversarially
strong, and follow the law [94]. This change needs a lot
of work to be done in computer science, cognitive science,
human-computer interaction, and legal studies. If this inte-
gration doesn’t happen, the gap between what XAI promises
and what it delivers will keep getting bigger as models get

VOLUME 14, 2026

27413

---

<!-- PAGE 21 -->

more complicated and the stakes for deployment get higher.
The path forward is clear but challenging. XAI needs to
change from a technical capability to a socio-technical system
where explanations clearly help people make better decisions,
stop people from trying to trick it, and meet legal require-
ments. Only then can AI change from being black boxes
that people can’t see into partners in human decision-making
that are clear, accountable, and ultimately trustworthy. The
research directions outlined in this review offer a frame-
work for this transformation; however, success hinges on
collaborative efforts across disciplines and a continuous ded-
ication to prioritizing deployment readiness over algorithmic
innovation.

REFERENCES

[1] S. Al and S. Sağiroğlu, ‘‘A review of explainable artificial intelligence,’’

in Proc. 9th Int. Conf. Comput. Sci. Eng. (UBMK), 2023, pp. 310–315.

[2] M. Fontes, J. D. S. De Almeida, and A. Cunha, ‘‘Application of
example-based explainable artificial intelligence (XAI) for analysis and
interpretation of medical imaging: A systematic review,’’ IEEE Access,
vol. 12, pp. 26419–26427, 2024.

[3] V. Buhrmester, D. Münch, and M. Arens, ‘‘Analysis of explainers of black
box deep neural networks for computer vision: A survey,’’ Mach. Learn.
Knowl. Extraction, vol. 3, no. 4, pp. 966–989, Dec. 2021.

[4] A. Adadi and M. Berrada, ‘‘Peeking inside the black-box: A sur-
vey on explainable artificial intelligence (XAI),’’ IEEE Access, vol. 6,
pp. 52138–52160, 2018.

[5] E. S. Ortigossa, T. Gonçalves, and L. G. Nonato, ‘‘EXplainable artificial
intelligence (XAI)—From theory to methods and applications,’’ IEEE
Access, vol. 12, pp. 80799–80846, 2024.

[6] S. Sutthithatip, S. Perinpanayagam, and S. Aslam, ‘‘(Explainable) arti-
ficial intelligence in aerospace safety-critical systems,’’ in Proc. IEEE
Aerosp. Conf. (AERO), Big Sky, MT, USA, Mar. 2022, pp. 1–12.

[7] A. Kuznietsov, B. Gyevnar, C. Wang, S. Peters, and S. V. Albrecht,
‘‘Explainable AI for safe and trustworthy autonomous driving: A sys-
tematic review,’’ IEEE Trans. Intell. Transp. Syst., vol. 25, no. 12,
pp. 19342–19364, Dec. 2024.

[8] L. Edwards and M. Veale, ‘‘Enslaving the algorithm: From a right to an
explanation to a ‘right to better decisions?’’’ IEEE Secur. Privacy, vol. 16,
no. 3, pp. 46–54, May 2018.

[9] D. Gunning, M. Stefik, J. Choi, T. Miller, S. Stumpf, and G.-Z. Yang,
‘‘XAI-explainable artificial intelligence,’’ Sci. Robot., vol. 4, no. 26,
p. 7120, May 2019.

[10] A. B. Arrieta, N. Díaz-Rodríguez, J. D. Ser, A. Bennetot, S. Tabik,
A. Barbado, S. García, S. Gil-López, D. Molina, R. Benjamins, R. Chatila,
and F. Herrera, ‘‘Explainable artificial intelligence (XAI): Concepts,
taxonomies, opportunities and challenges toward responsible AI,’’ Inf.
Fusion, vol. 58, pp. 82–115, Jun. 2019.

[11] A. Rawal, J. McCoy, D. B. Rawat, B. M. Sadler, and R. S. Amant,
‘‘Recent advances in trustworthy explainable artificial intelligence: Sta-
tus, challenges, and perspectives,’’ IEEE Trans. Artif. Intell., vol. 3, no. 6,
pp. 852–866, Dec. 2022.

[12] W. Yang, Y. Wei, H. Wei, Y. Chen, G. Huang, X. Li, R. Li, N. Yao,
X. Wang, X. Gu, M. B. Amin, and B. Kang, ‘‘Survey on explainable AI:
From approaches, limitations and applications aspects,’’ Hum.-Centric
Intell. Syst., vol. 3, no. 3, pp. 161–188, Aug. 2023.

[13] D. Slack, S. Hilgard, E. Jia, S. Singh, and H. Lakkaraju, ‘‘Fooling LIME
and SHAP: Adversarial attacks on post hoc explanation methods,’’ in
Proc. AAAI/ACM Conf. AI, Ethics, Soc., Feb. 2020, pp. 180–186.
[14] X. Zhang, N. Wang, H. Shen, S. Ji, X. Luo, and T. Wang, ‘‘Interpretable

deep learning under fire,’’ in Proc. 29th Secur. Symp., 2018, pp. 1–18.

[15] S. Atakishiyev, M. Salameh, H. Yao, and R. Goebel, ‘‘Explainable arti-
ficial intelligence for autonomous driving: A comprehensive overview
and field guide for future research directions,’’ IEEE Access, vol. 12,
pp. 101603–101625, 2024.

[16] K. Wulff and H. Finnestrand, ‘‘Creating meaningful work in the age of
AI: Explainable AI, explainability, and why it matters to organizational
designers,’’ AI Soc., vol. 39, no. 4, pp. 1843–1856, Aug. 2024.

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

[17] B. Goodman and S. Flaxman, ‘‘European union regulations on algorith-
mic decision making and a ‘right to explanation,’’’ AI Mag., vol. 38, no. 3,
pp. 50–57, Sep. 2017.

[18] C. Rudin, C. Chen, Z. Chen, H. Huang, L. Semenova, and C. Zhong,
‘‘Interpretable machine learning: Fundamental principles and 10 grand
challenges,’’ Statistic Surveys, vol. 16, no. none, pp. 1–85, 2022.
[19] V. Chamola, V. Hassija, A. R. Sulthana, D. Ghosh, D. Dhingra, and B.
Sikdar, ‘‘A review of trustworthy and explainable artificial intelligence
(XAI),’’ IEEE Access, vol. 11, pp. 78994–79015, 2023.

[20] N. Pfeuffer, L. Baum, W. Stammer, B. M. Abdel-Karim, P. Schramowski,
A. M. Bucher, C. Hügel, G. Rohde, K. Kersting, and O. Hinz, ‘‘Explana-
tory interactive machine learning: Establishing an action design research
process for machine learning projects,’’ Bus. Inf. Syst. Eng., vol. 65, no. 6,
pp. 677–701, Dec. 2023.

[21] Y. Okay, M. Yildirim, and S. Ozdemir, ‘‘Interpretable machine learning:
A case study of healthcare,’’ in Proc. Int. Symp. Netw., Comput. Commun.
(ISNCC), Oct. 2021, pp. 1–6.

[22] Y. S. Heng and P. Subramanian, ‘‘A systematic review of machine learning
and explainable artificial intelligence (XAI) in credit risk modelling,’’ in
Proc. Future Technol. Conf., 2022, pp. 596–614.

[23] R.-K. Sheu and M. S. Pardeshi, ‘‘A survey on medical explainable
AI (XAI): Recent progress, explainability approach, human inter-
action and scoring system,’’ Sensors, vol. 22, no. 20, p. 8068,
Oct. 2022.

[24] F. Sovrano, ‘‘Legal XAI: A systematic review and interdisciplinary map-
ping of XAI and EU law, towards a research agenda for legally responsible
AI,’’ Towards Res. Agenda Legally Responsible AI, Jul. 2025. [Online].
Available: https://ssrn.com/abstract=5371124

[25] W. Pedrycz, ‘‘Design, interpretability, and explainability of models in the
framework of granular computing and federated learning,’’ in Proc. IEEE
Conf. Norbert Wiener 21st Century (21CW), Chennai, India, Jul. 2021,
pp. 1–6.

[26] G. Schwalbe and B. Finzel, ‘‘A comprehensive taxonomy for explainable
artificial intelligence: A systematic survey of surveys on methods and
concepts,’’ Data Min. Knowl. Disc., vol. 38, no. 5, pp. 3043–3101, 2023.
[27] M. R. Islam, ‘‘A comprehensive survey of explainable artificial intelli-
gence (XAI): A human-centered perspective,’’ IEEE Trans. Computat.
Social Syst., vol. 9, no. 4, pp. 1149–1166, Aug. 2022.

[28] D. Oreki and M. P. Lukinec, ‘‘Evaluation of explainable artificial intel-
ligence for predictive process mining in education,’’ WSEAS Trans. Adv.
Eng. Educ., vol. 22, pp. 1–8, Apr. 2025.

[29] K. Sokol and P. Flach, ‘‘Explainability fact sheets: A framework for sys-
tematic assessment of explainable approaches,’’ in Proc. Conf. Fairness,
Accountability, Transparency, Jan. 2020, pp. 56–67.

[30] N. Barr Kumarakulasinghe, T. Blomberg, J. Liu, A. Saraiva Leao, and
P. Papapetrou, ‘‘Evaluating local interpretable model-agnostic explana-
tions on clinical machine learning classification models,’’ in Proc. IEEE
33rd Int. Symp. Computer-Based Med. Syst. (CBMS), Rochester, MN,
USA, Jul. 2020, pp. 7–12.

[31] F. S. Khan, S. S. Mazhar, K. Mazhar, D. A. AlSaleh, and A.
Mazhar, ‘‘Model-agnostic explainable artificial intelligence methods in
finance: A systematic review, recent developments, limitations, chal-
lenges and future directions,’’ Artif. Intell. Rev., vol. 58, no. 8, p. 232,
May 2025.

[32] K. Devireddy, ‘‘A comparative study of explainable AI methods: Model-
agnostic vs. model-specific approaches,’’ 2025, arXiv:2504.04276.
[33] A. Ghorbani, A. Abid, and J. Zou, ‘‘Interpretation of neural networks is
fragile,’’ in Proc. AAAI Conf. Artif. Intell., 2017, pp. 3681–3688.
[34] Z. Zhang, L. Yilmaz, and B. Liu, ‘‘A critical review of inductive logic
programming techniques for explainable AI,’’ IEEE Trans. Neural Netw.
Learn. Syst., vol. 35, no. 8, pp. 10220–10236, Aug. 2024.

[35] U. Schlegel, D. V. Lam, D. A. Keim, and D. Seebacher, ‘‘TS-MULE:
Local interpretable model-agnostic explanations for time series forecast
models,’’ in Proc. Joint Eur. Conf. Mach. Learn. Knowl. Discovery
Databases, 2021, pp. 5–14.

[36] K. Kalasampath, K. N. Spoorthi, S. Sajeev, S. Kuppa, K. Ajay, and M.
Angulakshmi, ‘‘A literature review on applications of explainable artifi-
cial intelligence (XAI),’’ IEEE Access, vol. 13, pp. 41111–41140, 2025.
[37] P. Rasouli and I. C. Yu, ‘‘Analyzing and improving the robustness of
tabular classifiers using counterfactual explanations,’’ in Proc. 20th IEEE
Int. Conf. Mach. Learn. Appl. (ICMLA), Pasadena, CA, USA, Dec. 2021,
pp. 1286–1293.

27414

VOLUME 14, 2026

---

<!-- PAGE 22 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

[38] S. M. Lundberg, G. Erion, H. Chen, A. DeGrave, J. M. Prutkin, B. Nair,
R. Katz, J. Himmelfarb, N. Bansal, and S.-I. Lee, ‘‘From local expla-
nations to global understanding with explainable AI for trees,’’ Nature
Mach. Intell., vol. 2, no. 1, pp. 56–67, Jan. 2020.

[39] K. Aas, M. Jullum, and A. Løland, ‘‘Explaining individual predictions
when features are dependent: More accurate approximations to Shapley
values,’’ Artif. Intell., vol. 298, Sep. 2021, Art. no. 103502.

[40] A. Di Marino, V. Bevilacqua, A. Ciaramella, I. De Falco, and G. San-
nino, ‘‘Ante-hoc methods for interpretable deep models: A survey,’’ ACM
Comput. Surveys, vol. 57, no. 10, pp. 1–36, Oct. 2025.

[41] C. Rudin, ‘‘Stop explaining black box machine learning models for high
stakes decisions and use interpretable models instead,’’ Nature Mach.
Intell., vol. 1, no. 5, pp. 206–215, May 2019.

[42] R. Mochaourab, A. Venkitaraman, I. Samsten, P. Papapetrou, and C. R.
Rojas, ‘‘Post hoc explainability for time series classification: Toward a
signal processing perspective,’’ IEEE Signal Process. Mag., vol. 39, no. 4,
pp. 119–129, Jul. 2022.

[43] D. Bhati, M. Amiruzzaman, Y. Zhao, A. Guercio, and T.-L. Le, ‘‘A survey
of post-hoc XAI methods from a visualization perspective: Challenges
and opportunities,’’ IEEE Access, vol. 13, pp. 120785–120806, 2025.
[44] M. A. K. Akhtar, M. Kumar, and A. Nayyar, ‘‘The role of human-
centered design in developing explainable AI,’’ in Towards Ethical and
Socially Responsible Explainable AI: Challenges and Opportunities.
Cham, Switzerland: Springer, 2024.

[45] J. Cernevicien and K. Audrius, ‘‘Explainable artificial intelligence (XAI)
in finance: A systematic literature review,’’ Artif. Intell. Rev., vol. 57,
no. 8, p. 216, Jul. 2024.

[46] Q. Xu, Y. Liao, Q. Li, J. Zhang, Z. Song, L. Wang, and X. Yuan, ‘‘SHAP-
based interpretable models for credit default assessment using machine
learning,’’ in Proc. 14th Int. Conf. Softw. Technol. Eng. (ICSTE), Macau,
Aug. 2024, pp. 213–217.

[47] M. K. Nallakaruppan, B. Balusamy, M. L. Shri, V. Malathi, and S.
Bhattacharyya, ‘‘An explainable AI framework for credit evaluation and
analysis,’’ Appl. Soft Comput., vol. 153, Mar. 2024, Art. no. 111307.
[48] N. Capuano, G. Fenza, V. Loia, and C. Stanzione, ‘‘Explainable arti-
ficial intelligence in CyberSecurity: A survey,’’ IEEE Access, vol. 10,
pp. 93575–93600, 2022.

[49] R. Kapale, P. Deshpande, S. Shukla, S. Kediya, Y. Pethe, and S. Metre,
‘‘Explainable AI for fraud detection: Enhancing transparency and trust in
financial decision-making,’’ in Proc. 2nd DMIHER Int. Conf. Artif. Intell.
Healthcare, Educ. Ind. (IDICAIEI), Wardha, India, Nov. 2024, pp. 1–6.

[50] D. K. J. B. Saini, N. Shelke, S. N. Prajwalasimha, A. Pimpalkar, G. H.
Kumar, and L. Monish, ‘‘Advanced deep learning for real-time fraud
detection in banking: Scalable and high-accuracy solutions,’’ in Proc.
6th Int. Conf. Emerg. Technol. (INCET), BELGAUM, India, May 2025,
pp. 1–6.

[51] B. H. A. Khattak, I. Shafi, A. S. Khan, E. S. Flores, R. G. Lara,
M. A. Samad, and I. Ashraf, ‘‘A systematic survey of AI models in finan-
cial market forecasting for profitability analysis,’’ IEEE Access, vol. 11,
pp. 125359–125380, 2023.

[52] S. Bharati, M. R. H. Mondal, and P. Podder, ‘‘A review on explainable
artificial intelligence for healthcare: Why, how, and when?’’ IEEE Trans.
Artif. Intell., vol. 5, no. 4, pp. 1429–1442, Apr. 2024.

[53] H. C. Yoon and L. P. Lin, ‘‘Brain tumor classification in MRI: Insights
from LIME and grad-CAM explainable AI techniques,’’ IEEE Access,
vol. 13, pp. 154172–154202, 2025.

[54] D. Bhati, F. Neha, and M. Amiruzzaman, ‘‘A survey on explainable arti-
ficial intelligence (XAI) techniques for visualizing deep learning models
in medical imaging,’’ J. Imag., vol. 10, no. 10, p. 239, Sep. 2024.
[55] S. Durgaraju, D. V. T. Vel, and H. Madathala, ‘‘Transforming healthcare
diagnostics: A comprehensive review of convolutional neural networks in
medical imaging and disease prediction,’’ in Proc. 6th Int. Conf. Mobile
Comput. Sustain. Informat. (ICMCSI), Goathgaun, Nepal, Jan. 2025,
pp. 1167–1174.

[56] Q. Abbas, W. Jeong, and S. W. Lee, ‘‘Explainable AI in clinical decision
support systems: A meta-analysis of methods, applications, and usability
challenges,’’ Healthcare, vol. 13, no. 17, p. 2154, Aug. 2025.

[57] Q. Xu, W. Xie, B. Liao, C. Hu, L. Qin, Z. Yang, H. Xiong, Y. Lyu, Y. Zhou,
and A. Luo, ‘‘Interpretability of clinical decision support systems based
on artificial intelligence from technological and medical perspective:
A systematic review,’’ J. Healthcare Eng., vol. 2023, no. 1, Jan. 2023,
Art. no. 9919269.

[58] C. Düsing, P. Cimiano, S. Rehberg, C. Scherer, O. Kaup, C. Köster,
S. Hellmich, D. Herrmann, K. L. Meier, S. Claßen, and R. Borgstedt,
‘‘Integrating federated learning for improved counterfactual explanations
in clinical decision support systems for sepsis therapy,’’ Artif. Intell. Med.,
vol. 157, Nov. 2024, Art. no. 102982.

[59] G. Rjoub, J. Bentahar, O. A. Wahab, R. Mizouni, A. Song, R. Cohen,
H. Otrok, and A. Mourad, ‘‘A survey on explainable artificial intelligence
for cybersecurity,’’ IEEE Trans. Netw. Service Manage., vol. 20, no. 4,
pp. 5115–5140, Dec. 2023.

[60] K. Cherukuri, ‘‘Artificial intelligence-based approaches for anomaly
detection,’’ in Encrypted Network Traffic Analysis. Cham, Switzerland:
Springer, 2024, pp. 73–99.

[61] W. Liu, F. Zhao, L. Nkenyereye, S. Rani, K. Li, and J. Lv, ‘‘XAI
driven intelligent IoMT secure data management framework,’’ IEEE J.
Biomed. Health Informat., vol. 30, no. 2, pp. 935–946, Feb. 2025, doi:
10.1109/JBHI.2024.3408215.

[62] Y. Rong, T. Leemann, T.-T. Nguyen, L. Fiedler, P. Qian, V. Unhelkar, T.
Seidel, G. Kasneci, and E. Kasneci, ‘‘Towards human-centered explain-
able AI: A survey of user studies for model explanations,’’ IEEE Trans.
Pattern Anal. Mach. Intell., vol. 46, no. 4, pp. 2104–2122, Apr. 2024.

[63] R. Mandava, S. S. Vellela, S. Gorintla, L. Dalavai, N. Malathi, and
K. Haritha, ‘‘Evaluating the impact of explainable AI on user trust in
financial decision-support systems,’’ in Proc. Int. Conf. Comput. Robot.,
Test. Eng. Eval. (ICCRTEE), Virudhunagar, India, May 2025, pp. 1–6.

[64] T. Miller and Z. Jing, ‘‘Explanation in artificial intelligence: Insights from
the social sciences,’’ Digital Humanities Research, vol. 4, no. 2, p. 90,
2024.

[65] S. Tasneem and K. A. Islam, ‘‘Improve adversarial robustness of AI
models in remote sensing via data-augmentation and explainable-AI
methods,’’ Remote Sens., vol. 16, no. 17, p. 3210, Aug. 2024.

[66] U. Aïvodji, ‘‘Fairwashing: The risk of rationalization,’’ in Proc. Int. Conf.

Mach. Learn., 2019, pp. 161–170.

[67] C. Thames and Y. Sun, ‘‘A survey of artificial intelligence approaches to
safety and mission-critical systems,’’ in Proc. Integr. Commun., Navigat.
Surveill. Conf. (ICNS), Herndon, VA, USA, Apr. 2024, pp. 1–12.
[68] J. Wei, H. Turbé, and G. Mengaldo, ‘‘Revisiting the robustness of post-

hoc interpretability methods,’’ 2024, arXiv:2407.19683.

[69] I. E. Nielsen, D. Dera, G. Rasool, R. P. Ramachandran, and N. C. Bouay-
naya, ‘‘Robust explainability: A tutorial on gradient-based attribution
methods for deep neural networks,’’ IEEE Signal Process. Mag., vol. 39,
no. 4, pp. 73–84, Jul. 2022.

[70] H. Jin, A. Xue, W. You, S. Goel, and E. Wong, ‘‘Probabilistic stability

guarantees for feature attributions,’’ 2025, arXiv:2504.13787.

[71] I. Vaccari, A. Carlevaro, S. Narteni, E. Cambiaso, and M. Mongelli,
‘‘Explainable and reliable against adversarial machine learning in data
analytics,’’ IEEE Access, vol. 10, pp. 83949–83970, 2022.

[72] A. Hedström, L. Weber, S. Lapuschkin, and M. Höhne, ‘‘A fresh look at
sanity checks for saliency maps,’’ in Proc. World Conf. Explainable Artif.
Intell., 2024, pp. 403–420.

[73] J.-H. Sim and H.-M. Song, ‘‘A generalized framework for adversarial
attack detection and prevention using grad-CAM and clustering tech-
niques,’’ Systems, vol. 13, no. 2, p. 88, Jan. 2025.

[74] Z. Zhang, H. A. Hamadi, E. Damiani, C. Y. Yeun, and F. Taher,
‘‘Explainable artificial intelligence applications in cyber security: State-
IEEE Access, vol. 10, pp. 93104–93139,
of-the-art
2022.

in research,’’

[75] A. Zahid, ‘‘Explainability, robustness, and fairness in user-centric
intelligent systems: A systematic review,’’ IEEE Trans. Emerg. Top-
ics Comput. Intell., vol. 9, no. 6, pp. 3728–3753, Jul. 2025, doi:
10.1109/TETCI.2025.3567604.

[76] A. Kuppa and N.-A. Le-Khac, ‘‘Black box attacks on explainable artificial
intelligence(XAI) methods in cyber security,’’ in Proc. Int. Joint Conf.
Neural Netw. (IJCNN), Jul. 2020, pp. 1–8.

[77] Leofante and M. Wicker, Robust Explainable AI. Cham, Switzerland:

Springer, 2025.

[78] S. Naveed, G. Stevens, and D. Robin-Kern, ‘‘An overview of the empir-
ical evaluation of explainable AI (XAI): A comprehensive guideline for
user-centered evaluation in XAI,’’ Appl. Sci., vol. 14, no. 23, p. 11288,
Dec. 2024.

[79] S. Alhasan and R. Alnanih, ‘‘Enhancing AI explainability through the
EXACT framework: A user-centric approach,’’ IEEE Access, vol. 13,
pp. 98208–98228, 2025.

VOLUME 14, 2026

27415

---

<!-- PAGE 23 -->

[80] F. Poursabzi-Sangdeh, D. G. Goldstein, J. M. Hofman, J. W. Wortman
Vaughan, and H. Wallach, ‘‘Manipulating and measuring model inter-
pretability,’’ in Proc. CHI Conf. Hum. Factors Comput. Syst., May 2021,
pp. 1–52.

[81] E. D. Okonta, F. O. Okeke, E. E. Mgbemena, R. C. Nnaemeka-Okeke, S.
Guo, F. C. Awe, and C. Eke, ‘‘An intelligent natural language process-
ing (NLP) workflow for automated smart building design,’’ Buildings,
vol. 15, no. 14, p. 2413, Jul. 2025.

[82] R. Confalonieri and J. M. Alonso-Moral, ‘‘An operational framework
for guiding human evaluation in explainable and trustworthy artificial
intelligence,’’ IEEE Intell. Syst., vol. 39, no. 1, pp. 18–28, Jan. 2024.
[83] E. Mariotti, A. Arias-Duart, M. Cafagna, A. Gatt, D. Garcia-Gasulla, and
J. M. Alonso-Moral, ‘‘TextFocus: Assessing the faithfulness of feature
attribution methods explanations in natural language processing,’’ IEEE
Access, vol. 12, pp. 138870–138880, 2024.

[84] M. A. Kadir, A. Mosavi, and D. Sonntag, ‘‘Evaluation metrics for XAI:
A review, taxonomy, and practical applications,’’ in Proc. IEEE 27th Int.
Conf. Intell. Eng. Syst. (INES), Nairobi, Kenya, Jul. 2023, pp. 000111–
000124.

[85] K. Ong, R. Mao, D. Varshney, P. Pu Liang, E. Cambria, and G. Mengaldo,
‘‘Deriving strategic market insights with large language models: A bench-
mark for forward counterfactual generation,’’ 2025, arXiv:2505.19430.

[86] S. Sithakoul, S. Meftah, and C. Feutry, ‘‘BEExAI: Benchmark to evaluate
explainable AI,’’ in Proc. World Conf. Explainable Artif. Intell., 2024,
pp. 445–468.

[87] S. Roy, G. Laberge, B. Roy, F. Khomh, A. Nikanjam, and S. Mondal,
‘‘Why Don’t XAI techniques agree? Characterizing the disagreements
between post-hoc explanations of defect predictions,’’ in Proc. IEEE Int.
Conf. Softw. Maintenance Evol. (ICSME), Limassol, Cyprus, Oct. 2022,
pp. 444–448.

[88] A. Gambetti, Q. Han, H. Shen, and C. Soares, ‘‘A survey on human-
centered evaluation of explainable AI methods in clinical decision support
systems,’’ 2025, arXiv:2502.09849.

[89] A. Jacovi, A. Marasovic, T. Miller, and Y. Goldberg, ‘‘Formalizing trust
in artificial intelligence: Prerequisites, causes and goals of human trust in
AI,’’ in Proc. ACM Conf. Fairness, Accountability, Transparency, 2021,
pp. 624–635.

[90] E. Tjoa and C. Guan, ‘‘A survey on explainable artificial intelligence
(XAI): Toward medical XAI,’’ IEEE Trans. Neural Netw. Learn. Syst.,
vol. 32, no. 11, pp. 4793–4813, Nov. 2021.

[91] W. Saeed and C. Omlin, ‘‘Explainable AI (XAI): A systematic meta-
survey of current challenges and future opportunities,’’ Knowledge-Based
Syst., vol. 263, Mar. 2023, Art. no. 110273.

[92] V. L. Kalmykov and L. V. Kalmykov, ‘‘Towards explicitly explainable
artificial intelligence,’’ Inf. Fusion, vol. 123, Nov. 2025, Art. no. 103352.
Scaling Monosemanticity: Extracting
Interpretable Features From Claude 3 Sonnet. [Online]. Available:
https://transformer-circuits.pub/2024/scaling-monosemanticity/

[93] Anthropic.

2024).

(May

[94] L. Longo, M. Brčić, F. Cabitza, J. Choi, R. Confalonieri, J. D. Ser, R.
Guidotti, Y. Hayashi, F. Herrera, A. Holzinger, R. Jiang, H. Khosravi, F.
Lécué, G. Malgieri, A. Páez, W. Samek, J. Schneider, T. Speith, and S.
Stumpf, ‘‘Explainable artificial intelligence (XAI) 2.0: A manifesto of
open challenges and interdisciplinary research directions,’’ Inf. Fusion,
vol. 106, Jun. 2024, Art. no. 102301.

[95] A. A. Noor, A. Manzoor, M. D. Mazhar Qureshi, M. A. Qureshi, and W.
Rashwan, ‘‘Unveiling explainable AI in healthcare: Current trends, chal-
lenges, and future directions,’’ WIREs Data Mining Knowl. Discovery,
vol. 15, no. 2, p. 70018, Jun. 2025.

[96] S. N. Saw, Y. Y. Yan, and K. H. Ng, ‘‘Current status and future directions
of explainable artificial intelligence in medical imaging,’’ Eur. J. Radiol.,
vol. 183, Feb. 2025, Art. no. 111884.

[97] M. Pawlicki, A. Pawlicka, R. Kozik, and M. Choraś, ‘‘The survey on the
dual nature of xAI challenges in intrusion detection and their potential for
AI innovation,’’ Artif. Intell. Rev., vol. 57, no. 12, p. 330, Oct. 2024.
[98] Y.-L. Chou, C. Moreira, P. Bruza, C. Ouyang, and J. Jorge, ‘‘Coun-
terfactuals and causability in explainable artificial intelligence: Theory,
algorithms, and applications,’’ Inf. Fusion, vol. 81, pp. 59–83, May 2021.
[99] R. O. Weber, A. J. Johs, P. Goel, and J. M. Silva, ‘‘XAI is in trouble,’’ AI

Mag., vol. 45, no. 3, pp. 300–316, Sep. 2024.

[100] Umm-E-Habiba and K. M. Habibullah, ‘‘Explainable AI: A diverse stake-
holder perspective,’’ in Proc. IEEE 32nd Int. Requirements Eng. Conf.
(RE), Reykjavik, Iceland, Jun. 2024, pp. 494–495.

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

[101] O. S. Owolabi, P. C. Uche, N. T. Adeniken, C. Ihejirika, R. B. Islam,
and B. J. T. Chhetri, ‘‘Ethical implication of artificial intelligence (AI)
adoption in financial decision making,’’ Comput. Inf. Sci., vol. 17, no. 1,
p. 49, Apr. 2024.

[102] Z. Atf and P. R. Lewis, ‘‘Is trust correlated with explainability in AI? A
meta-analysis,’’ IEEE Trans. Technol. Soc., early access, Apr. 14, 2025,
doi: 10.1109/TTS.2025.3558448.

[103] S. Atakishiyev, H. K. B. Babiker, J. Dai, N. Farruque, T. Hayashi, N.
Sadaf Hriti, M. Abed Rahman, I. Smith, M.-Y. Kim, O. R. Zaïane,
and R. Goebel, ‘‘Explainability of large language models: Opportuni-
ties and challenges toward generating trustworthy explanations,’’ 2025,
arXiv:2510.17256.

[104] S. Jain and B. C. Wallace, ‘‘Attention is not explanation,’’ in Proc. Conf.
North Amer. Chapter Assoc. Comput. Linguistics, Hum. Lang. Technol.
(NAACL-HLT), 2019, pp. 3543–3556.

[105] Anthropic. (Apr. 2025). Reasoning Models Don’t Always Say What
They Think. [Online]. Available: https://www.anthropic.com/research/
reasoning-models-dont-say-think

[106] A. Pahud de Mortanges, H. Luo, S. Z. Shu, A. Kamath, Y. Suter, M.
Shelan, A. Pöllinger, and M. Reyes, ‘‘Orchestrating explainable artificial
intelligence for multimodal and longitudinal data in medical imaging,’’
npj Digit. Med., vol. 7, no. 1, p. 195, Jul. 2024.

[107] D. Shu, H. Zhao, J. Hu, W. Liu, A. Payani, L. Cheng, and M. Du, ‘‘Large
vision-language model alignment and misalignment: A survey through
the lens of explainability,’’ in Proc. Findings Assoc. Comput. Linguistics:
EMNLP, Suzhou, China, 2025, pp. 1713–1735.

[108] F. M. Talaat, A. Aljadani, M. Badawy, and M. Elhosseini, ‘‘Toward
interpretable credit scoring: Integrating explainable artificial intelligence
with deep learning for credit card default prediction,’’ Neural Comput.
Appl., vol. 36, no. 9, pp. 4847–4865, Mar. 2024.

[109] S. Gite, H. Khatavkar, K. Kotecha, S. Srivastava, P. Maheshwari, and
N. Pandey, ‘‘Explainable stock prices prediction from financial news
articles using sentiment analysis,’’ PeerJ Comput. Sci., vol. 7, p. e340,
Jan. 2021.

[110] B. Lim, S. Ö. Arık, N. Loeff, and T. Pfister, ‘‘Temporal fusion trans-
formers for interpretable multi-horizon time series forecasting,’’ Int. J.
Forecasting, vol. 37, no. 4, pp. 1748–1764, Oct. 2021.

[111] J. Jiménez-Luna, F. Grisoni, and G. Schneider, ‘‘Drug discovery with
explainable artificial intelligence,’’ Nature Mach. Intell., vol. 2, no. 10,
pp. 573–584, Oct. 2020.

[112] Z. Wu, J. Wang, H. Du, D. Jiang, Y. Kang, D. Li, P. Pan, Y. Deng,
D. Cao, C.-Y. Hsieh, and T. Hou, ‘‘Chemistry-intuitive explanation of
graph neural networks for molecular property prediction with substruc-
ture masking,’’ Nature Commun., vol. 14, no. 1, pp. 1–15, May 2023.

[113] M. Proietti, A. Ragno, B. L. Rosa, R. Ragno, and R. Capobianco,
‘‘Explainable AI
graph
neural network for molecular property prediction using concept
whitening,’’ Mach. Learn., vol. 113, no. 4, pp. 2013–2044,
Apr. 2024.

discovery: Self-interpretable

drug

in

[114] M. Saied and S. Guirguis, ‘‘Explainable artificial intelligence for botnet
detection in Internet of Things,’’ Sci. Rep., vol. 15, no. 1, pp. 1–17,
Mar. 2025.

[115] S. Milli, L. Schmidt, A. D. Dragan, and M. Hardt, ‘‘Model reconstruc-
tion from model explanations,’’ in Proc. Conf. Fairness, Accountability,
Transparency, Jan. 2019, pp. 1–9.

[116] R. Shokri, M. Strobel, and Y. Zick, ‘‘On the privacy risks of model
explanations,’’ in Proc. AAAI/ACM Conf. AI, Ethics, Soc., Jul. 2021,
pp. 231–241.

[117] H. Liu, Y. Wu, Z. Yu, and N. Zhang, ‘‘Please tell me more: Privacy impact
of explainability through the lens of membership inference attack,’’ in
Proc. IEEE Symp. Secur. Privacy (SP), May 2024, pp. 4791–4809.
[118] Z. Buçinca, M. B. Malaya, and K. Z. Gajos, ‘‘To trust or to think:
Cognitive forcing functions can reduce overreliance on AI in AI-assisted
decision-making,’’ ACM Hum.-Comput. Interact., vol. 5, pp. 1–21,
Apr. 2021.

[119] G. Bansal, T. Wu, J. Zhou, R. Fok, B. Nushi, E. Kamar, M. T. Ribeiro,
and D. Weld, ‘‘Does the whole exceed its parts? The effect of AI explana-
tions on complementary team performance,’’ in Proc. CHI Conf. Human
Factors Comput. Syst., May 2021, pp. 1–16.

[120] H. Vasconcelos, M. Jörke, M. Grunde-Mclaughlin, T. Gerstenberg, M. S.
Bernstein, and R. Krishna, ‘‘Explanations can reduce overreliance on AI
systems during decision-making,’’ Proc. ACM Hum.-Comput. Interact.,
vol. 7, no. CSCW1, pp. 1–38, Apr. 2023.

27416

VOLUME 14, 2026

---

<!-- PAGE 24 -->

O. Kaya et al.: XAI: Concepts, Applications, Challenges, and Future Perspectives

[121] Y. Xuan, E. Small, K. Sokol, D. Hettiachchi, and M. Sanderson,
‘‘Comprehension is a double-edged sword: Over-interpreting unspecified
information in intelligible machine learning explanations,’’ Int. J. Hum.-
Comput. Stud., vol. 193, Jan. 2025, Art. no. 103376.

[122] R. Müller, ‘‘How explainable AI affects human performance: A system-
atic review of the behavioural consequences of saliency maps,’’ Int. J.
Human–Computer Interact., vol. 41, no. 4, pp. 2020–2051, Feb. 2025.

[123] G. Nguyen, D. Kim, and A. Nguyen, ‘‘The effectiveness of feature
attribution methods and its correlation with automatic evaluation scores,’’
in Proc. Adv. Neural Inf. Process. Syst., vol. 34, 2021, pp. 26422–26436.
[124] B. Zhou, A. Khosla, A. Lapedriza, A. Oliva, and A. Torralba, ‘‘Learning
deep features for discriminative localization,’’ in Proc. IEEE Conf. Com-
put. Vis. Pattern Recognit. (CVPR), Jun. 2016, pp. 2921–2929.

[125] J. Zhang, S. A. Bargal, Z. Lin, J. Brandt, X. Shen, and S. Sclaroff,
‘‘Top-down neural attention by excitation backprop,’’ Int. J. Comput. Vis.,
vol. 126, no. 10, pp. 1084–1102, Oct. 2018.

[126] V. Petsiuk, A. Das, and K. Saenko, ‘‘RISE: Randomized input sampling
for explanation of black-box models,’’ 2018, arXiv:1806.07421.
[127] L.-V. Herm, ‘‘Impact of explainable AI on cognitive load: Insights from

an empirical study,’’ 2023, arXiv:2304.08861.

[128] D. Gunning, et al., ‘‘DARPA’s explainable AI, XAI program: A retrospec-

tive,’’ Applied AI Letters, vol. 2, no. 4, pp. 1–11, 2021.

[129] D. Alvarez-Melis and T. S. Jaakkola, ‘‘On the robustness of interpretabil-

ity methods,’’ 2018, arXiv:1806.08049.

[130] J. Adebayo, ‘‘Sanity checks for saliency maps,’’ in Proc. Adv. Neural Inf.

Process. Syst., vol. 31, 2018, pp. 1–11.

[131] J. Sik Kim, G. Plumb, and A. Talwalkar, ‘‘Sanity simulations for saliency

methods,’’ 2021, arXiv:2105.06506.

OSMAN KAYA received the M.Sc. degree in
electronics and communications engineering from
Yıldız Technical University, Istanbul, Türkiye,
where he is currently pursuing the Ph.D. degree
in communications. His research interests include
modulation classification, channel identification,
and the application of artificial intelligence in
5G and 6G wireless communication systems. His
work focuses on enhancing network performance
and reliability through advanced signal processing

and machine learning techniques.

A. F. M. SHAHEN SHAH (Senior Member,
IEEE) received the B.Sc. degree in electronics
and telecommunication engineering from Daffodil
International University, Bangladesh, in 2009, the
M.Sc. degree in information technology from the
University of Dhaka, Bangladesh, in 2011, and
the Ph.D. degree in electronics and communica-
tion engineering from Yildiz Technical University,
Türkiye, in 2020. He is currently an Associate
Professor with the Department of Electronics and
Communication Engineering and the Director of the AI and Next-Generation
Wireless Communication Laboratory (ANWCL), Yildiz Technical Univer-
sity. He has authored a book. He has published a good number of research
papers in international conferences and journals. His current research inter-
ests include wireless communication, artificial intelligence, 6G, blockchain,
and the IoT. He has been a TPC member for several IEEE conferences and
a regular reviewer for various IEEE journals. For his Ph.D. work, he won a
Gold Medal at the 32nd International Invention, Innovation, and Technology
Exhibition (ITEX) in 2021. He is serving as the Editor-in-Chief of ICCK
Transactions on Mobile and Wireless Intelligence and ICRRD Quality Index
Research Journal, an Editor for The Open Transportation Journal (Bentham)
and Discover Vehicles (Springer), and an Associate Editor for Journal of
Cyber Security Technology (Taylor and Francis).

MUHAMMET ALI KARABULUT (Senior Mem-
ber, IEEE) received the B.Sc. degree in electrical
and electronics engineering from Mustafa Kemal
University, Hatay, Türkiye, in 2010, and the M.Sc.
and Ph.D. degrees in electronics and communica-
tion engineering from Yildiz Technical University,
Istanbul, Türkiye, in 2015 and 2021, respectively.
He was a Research and Teaching Assistant with the
Department of Electronics and Communication
Engineering, Yildiz Technical University, from
2013 and 2021. He was an Assistant Professor with Kafkas University
from 2022 and 2024. Since 2024, he has been an Associate Profes-
sor with the Department of Electronics Engineering, Turkish Air Force
Academy, National Defense University, Türkiye, and a Researcher with the
AI and Next-Generation Wireless Communication Laboratory (ANWCL).
His research interests include digital communication, cooperative communi-
cation, MAC protocols for vehicular ad hoc networks, UAV communication,
and artificial intelligence.

SUMEYE NUR KARAHAN received the B.Sc.
degree in electronics and communication engi-
neering from Izmir University, Izmir, Türkiye,
in 2014, and the M.Sc. and Ph.D. degrees in elec-
trical and electronics engineering from Ankara
University, Ankara, Türkiye, in 2018 and 2025,
respectively. She was a Research Assistant with
the Department of Electrical and Electronics Engi-
neering, Ankara University, from 2015 and 2024.
Since 2024, she has been a Senior Research and
Development Researcher with the Research and Development Department,
Turk Telekom, Ankara. Her research interests include MIMO communica-
tion systems, integrated sensing and communication (ISAC), deep learning,
and explainable artificial intelligence.

MUSTAFA SERDAR OSMANCA is currently a
Faculty Member with Gazi University, Türkiye,
specializing in the field of communication within
the Department of Electrical and Electronics Engi-
neering. He teaches courses, such as commu-
nication techniques, Communication Laboratory,
and the Türk Telekom Industrial Communication
Laboratory. He has held various roles within the
Network departments with Türk Telekom. He is
currently the Research and Development Manager.
His research interests include communication, DWDM, and QUIC-based
traffic analysis.

NURETTIN ACıR received the Ph.D. degree in
electrical and electronics engineering from Dokuz
Eylul University, Izmir, Türkiye, in 2004. In 2003,
he was a Visiting Researcher with the Neu-
rosensory Engineering Laboratory, University of
Miami, FL, USA. From 2012 to 2013, he was
a Visiting Researcher with the Department of
Electrical and Electronic Engineering, Imperial
College London, London, U.K. He is currently
a Professor with the Department of Electronics
Engineering, Turkish Air Force Academy, National Defense University,
Istanbul, Türkiye. His research interests include linear/nonlinear systems
theory, adaptive filter theory, intelligent medical technology, advanced signal
and data processing, and artificial intelligence-based industrial applications.

VOLUME 14, 2026

27417

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received23January2026,accepted3February2026,dateofpublication10February2026,dateofcurrentversion23February2026.
DigitalObjectIdentifier10.1109/ACCESS.2026.3663161
Explainable Artificial Intelligence (XAI): Concepts,
Applications, Challenges, and Future Perspectives
OSMANKAYA 1,2,A.F.M.SHAHENSHAH 1,(SeniorMember,IEEE),
MUHAMMETALIKARABULUT 2,(SeniorMember,IEEE),
SUMEYENURKARAHAN 3,MUSTAFASERDAROSMANCA 3,
ANDNURETTINACıR2
1ElectronicsandCommunicationEngineeringDepartment,YildizTechnicalUniversity,34220Istanbul,Türkiye
2ElectronicsEngineeringDepartment,TurkishAirForceAcademy,NationalDefenseUniversity,34149Istanbul,Türkiye
3ResearchandDevelopmentDepartment,TurkTelekom,06000Ankara,Türkiye
Correspondingauthor:A.F.M.ShahenShah(shah@yildiz.edu.tr)
ThisworkwassupportedbyTheScientificandTechnologicalResearchCouncilofTürkiye(TÜBİTAK)through1515Frontier
ResearchandDevelopmentLaboratoriesSupportProgramfortheTürkTelekom6GResearchandDevelopmentLaboratories
underProject5249902.
ABSTRACT The aim of explainable artificial intelligence (XAI) is to address the black-box problem in
high-stakes applications. However, transparency alone does not guarantee trust. This review examines a
criticalparadoxinXAIresearch.Whileexplanationmethodscangenerateinsights,threemainchallenges
limittheireffectiveness.Firstly,adversarialmanipulationscanexploitexplanationsbycreatingnewattack
surfaceswithoverninetypercentsuccesswhilepreservingmodelaccuracy.Secondly,evaluationpractices
remainprimarilycomputational.Onlytwenty-sixpercentofuserstudiesfollowhuman-centeredprotocols
andfewerthantwenty-threepercentinvolvedomainexperts.Thirdly,regulatoryrequirements,suchasthe
GDPR right to explanation, lack clear technical implementations, complicating compliance. We analyzed
the literature across finance, healthcare, and cybersecurity and found that current research emphasizes
algorithmicinnovationoverpracticaldeployment.MovingtowardreliableAIrequiresshiftingfromsimple
explanationmethods(XAI1.0)tosystemsthatarealignedwithhumanunderstanding,resistanttoadversarial
attacks,andcompliantwithlegalrequirements(XAI2.0).Thisreviewprovidesguidanceonkeytechnical
advances,evaluationstrategiesandregulatoryclarificationsnecessaryfordeployment.trustworthyAI.
INDEX TERMS Ante-hoc, explainable artificial intelligence (XAI), human-centered XAI, interpretable
machinelearning,trustworthyAI,post-hoc.
I. INTRODUCTION modelsgetmorecomplicated,it’shardertounderstandhow
Artificial intelligence (AI), especially deep learning, has theymakedecisions.Inartificialintelligence,theblackbox
changed the technology of the twenty-first century in a big problemdescribessystemsthatgeneratecorrectoutputswith-
way. These systems have changed many industries and sci- outrevealinghowthosedecisionsaremade[4],[5].AsAIis
entific fields, and they are better than human experts at increasinglybeingusedinareassuchashealthcare,finance,
recognizingimagesandspeech[1],runningautonomoussys- criminal justice and transportation where safety is crucial,
tems, and diagnosing complicated medical conditions [2]. this lack of transparency has become a significant concern,
Deepneuralnetworksareabletodothisbyfindingcomplex, sinceerrorsinalgorithmsmayhaveseriousconsequences[6].
hierarchicalpatternsinhugedatasetswithmillionsorbillions Alackoftransparencyleadstoalossoftrustandaccountabil-
ofparameters.Butthisabilitytopredictcomesatacost:as ity,andmakesitdifficulttoverifyoutcomes[7].Furthermore,
regulationssuchastheGDPRentitleindividualsaffectedby
The associate editor coordinating the review of this manuscript and automated decisions to an explanation [8]. The demand for
interpretability, driven by these legal and ethical demands,
approvingitforpublicationwasRamoniAdeogun .
2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
27394 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME14,2026

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
has led to the rapid growth of explainable AI (XAI). The contemporary XAI research. The need for XAI arises from
aim of XAI is to make AI decisions more understandable, multipleconvergingfactors.Firstly,regulatoryrequirements
reduce biases, and support the development of reliable and suchasEU’sGeneralDataProtectionRegulation(GDPR)[8]
fairsystems[9],[10],[11],[12]. andtheproposedAIActmandatetransparencyinautomated
Current XAI surveys typically treat explainability as decision-makingprocesses.Secondly,inhigh-stakesdomains
primarilyatechnicalchallenge,withthefocusbeingongen- suchashealthcarediagnosis,creditassessmentandcriminal
erating interpretable outputs. However, failures observed in justice, practitioners must understand AI reasoning in order
real-worldapplicationspresentamorecomplexpicture.For toidentifypotentialbiases,validateclinicalorlegalcompli-
example,ifamedicalAIsystemprovidesaccuratediagnoses anceandmaintainaccountability[6].Thirdly,psychological
but clinicians distrust its explanations, the issue may lie not research shows that users must understand when to rely on
only in the underlying algorithms, but also in the system’s andwhentooverrideAIrecommendationsinordertotrustit
insufficiently human-centered design. These considerations appropriately [7]. Without explainability, even highly accu-
show that building trustworthy AI requires more than just rate models risk being misused, underutilized, or deployed
sophisticated explanation techniques. This review addresses incorrectlywhenuserscannotassesstheirreliabilityinnew
gaps in the existing literature by making three key con- situations.XAIisdistinctfrom,yetrelatedto,conceptssuch
tributions. Firstly, we demonstrate that adversarial attacks as interpretability, transparency and trustworthiness. While
significantly reduce the reliability of explanation meth- interpretability refers to the extent to which humans can
ods[13],[14],yetdefensestrategiesarenotwidelyadopted. understand the cause of a decision, transparency describes
Secondly,wepresentevidencesuggestingthatcurrentevalu- the degree to which a model’s internal mechanisms are vis-
ation practices prioritize computational metrics over human ible. Trustworthiness encompasses broader considerations,
interpretability. This helps to explain why systems that includingrobustness,fairnessandprivacy,withexplainability
perform well in controlled settings often fail in deploy- servingasacriticalcomponent.Thisreviewtakesaninclusive
ment. Lastly, we examine the challenges that organizations approach,examiningXAImethodsacrossthespectrum,from
face in meeting regulatory expectations when they cannot intrinsically interpretable models to sophisticated post-hoc
determinewhethertheirexplanationssatisfylegalstandards, explanation techniques. It recognizes that different stake-
demonstrating that regulatory and technical requirements holdersandapplicationcontextsrequiredifferentexplanation
are not aligned, which makes practical implementation paradigms.
difficult. Theimportantcontributionsofthispapertotheliterature
aresummarizedbelow.
• We provide a comprehensive and structured taxon-
A. FUNDAMENTALCONCEPTSINEXPLAINABLE omy of XAI by systematically organizing explanation
ARTIFICIALINTELLIGENCE methods across multiple dimensions, including model
XAI refers to the techniques and methods that make the dependency,scopeofexplanation,andtiming(ante-hoc
behavior and predictions of AI systems understandable to versus post-hoc), offering a unified conceptual frame-
humans.Unliketraditionalblack-boxmodels,whichprovide workforbothresearchersandpractitioners.
predictionswithoutjustification,XAIsystemsaimtoprovide • Wepresentadomain-orientedanalysisofXAIapplica-
transparentreasoning,allowinguserstounderstand,trustand tionsinhigh-stakessectorssuchasfinance,healthcare,
appropriately rely on AI decisions. The term explainable andcybersecurity,highlightingdomain-specificrequire-
AI formally emerged in the mid-2010s, although research ments, user roles, and deployment constraints that are
on interpretable models predates this terminology. Signifi- oftenoverlookedinexistingsurveys.
cantmomentumwasgainedinthefieldfollowingDARPA’s • We conduct an in-depth examination of security and
XAI program (2016–2021), which established foundational robustness challenges in XAI, including adversarial
frameworksfordistinguishingbetweenmodelsthatareinter- attacks on explanations, fairwashing, and explanation
pretable by design (ante-hoc methods) and techniques for manipulation, and critically discuss emerging defense
providing explanations after the fact (post-hoc) that can be andreliabilityassessmentstrategies.
appliedtoblack-boxsystems[128].Earlyfoundationalwork • We systematically analyze current evaluation practices
in XAI includes decision tree visualization, rule extraction for XAI, demonstrating that the majority of stud-
fromneuralnetworksandsensitivityanalysis[10],[41].Piv- ies rely on computational metrics while underutilizing
otal developments in model-agnostic post-hoc explanations human-centeredevaluationframeworks,andweidentify
weremarkedbySchlegeletal.’sLIME(2016)andLundberg key limitations related to scalability, standardization,
and Lee’s SHAP (2017), enabling practitioners to generate andusertrust.
localorglobalexplanationsforanyclassifier[35],[36],[37]. • We bridge technical, human-centered, and regulatory
At the same time, gradient-based attribution methods such perspectives by explicitly discussing the gap between
as Grad-CAM [54] emerged to improve the interpretabil- existingXAImethodsandlegalrequirementssuchasthe
ity of deep learning in computer vision. These seminal GDPRrighttoexplanation,therebyclarifyingpractical
contributions have laid the methodological groundwork for challengesinreal-worlddeployment.
VOLUME14,2026 27395

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
FIGURE1. ConceptualclassificationofXAImethodsbasedonkeytaxonomicaxessuchasmodeldependency,coverage,
andtimingofexplanation.
• We synthesize recent advances and open challenges to and classification of XAI methods, our review identified
outlineaforward-lookingresearchroadmaptowardXAI thatthesedimensionsareoftenexaminedinisolation,with-
2.0,emphasizingtheneedforhuman-aligned,adversari- out being systematically linked to deployment challenges,
allyrobust,andregulation-awareexplainabilitysystems, evaluation practices, and regulatory considerations. In this
particularly in the context of foundation models and context,RQ1doesnotaimtointroduceanentirelynoveltax-
multimodalAI. onomy;instead,itsynthesizeswidelyacceptedclassification
The paper is organized as follows. Section II outlines dimensions into a unified and deployment-oriented frame-
the scope of the review and the methodology employed. workthatservesasafoundationforthesubsequentanalysis
Section III provides an overview of core XAI principles in RQ2 and RQ3. This integrative formulation enables a
and major techniques. Applications in the fields of finance, coherent examination of how methodological choices in
healthcare and cybersecurity are presented in Section IV. XAI influence real-world applicability, security, and com-
SectionVdiscussesexplanationrobustness,includingadver- plianceinhigh-stakessettings.Topositionourcontributions
sarial risks and defense approaches. Section VI evaluates withinthebroaderliterature,Table1comparesthescopeof
assessment practices, emphasizing the need for human- this review with that of earlier surveys. This demonstrates
centered frameworks. Section VII highlights ongoing tech- that, although previous studies have investigated individual
nical and ethical challenges, as well as potential research aspects of XAI, such as technical methods, applications in
directions.SectionVIIIacknowledgesthelimitationsofthe specificsectorsandethicalconcerns,onlyalimitednumber
review.SectionIXconcludesbypresentingthemaininsights have considered these dimensions together in an integrated
andprovidingaroadmapforfutureXAIresearch. manner.
To address these research questions, we have adopted
II. REVIEWSCOPEANDAPPROACH a structured thematic synthesis approach to comprehen-
Threemainresearchquestions(RQ1–RQ3)guidethisreview. sively cover the rapidly evolving field of XAI. Although
RQ1focusesonidentifyingthemainXAImethodsandexam- our approach is informed by systematic review principles,
ininghowtheyaresystematicallycategorizedacrossdifferent we do not strictly adhere to formal protocols such as
model types and explanation paradigms. RQ2 investigates PRISMA. This is because XAI research is dynamic, and it
how XAI applications address domain-specific challenges, is important to incorporate recent developments, including
particularly in high-stakes contexts such as finance, health- preprints and technical reports that have not yet com-
care, and cybersecurity. RQ3 examines the potential limi- pletedpeerreview.Thismethodologicalchoiceallowsusto
tations and risks associated with deploying XAI systems, identify emerging trends in foundation model interpretabil-
includingissuesrelatedtosecurity,robustness,andregulatory ity and address current deployment issues that would be
compliance. excluded by rigid temporal or publication-type constraints.
Theformulationoftheseresearchquestionswasinformed Ourliteraturesearchtargetedfourmajoracademicdatabases,
by an iterative analysis of existing XAI surveys and recent which we selected for their comprehensive coverage of
application-driven studies. While prior works have exten- the field. IEEE Xplore and the ACM Digital Library for
sively addressed individual aspects such as the definition computer science and engineering publications; Scopus for
27396 VOLUME14,2026

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
broad, multidisciplinary coverage; and Arxiv for emerg-
ing research and preprints. The search covered publications
from 2018 to 2025, focusing on the period during which
XAItransitionedfromaspecializedresearchareatoacritical
component of responsible AI deployment. Search queries
combinedcoreterminology(‘explainableAI’,‘XAI’,‘inter-
pretablemachinelearning’,‘interpretability’,‘transparency’)
with domain-specific keywords related to methods (e.g.
‘LIME’,‘SHAP’,’attentionmechanisms’),applications(e.g.
‘healthcare’, ‘finance’, ‘cybersecurity’), and cross-cutting
concerns(e.g.‘fairness’,‘robustness’,‘evaluation’,‘human-
centredness’).Booleanoperatorswereusedtosystematically
combine these terms, and an English-language constraint
was applied to ensure consistency of analysis. The initial
searchyieldedasubstantialbodyofliteraturethatwaspoten-
tially relevant. The screening process proceeded in multiple
stages. First, the titles and abstracts of the literature were
reviewed to identify studies that addressed XAI methods,
applications,evaluationframeworks,securityandrobustness
considerations, or deployment challenges directly. Studies
focusing exclusively on general machine learning without
considering explainability, or providing only speculative
commentary without making any empirical or methodolog-
ical contributions, were excluded at this stage. Duplicate
articles appearing across multiple databases were identified
andremoved.Theremainingarticleswerethensubjectedto
a full-text review, which applied stricter eligibility criteria.
In order to be considered, studies had to provide substan-
tive empirical evidence, propose or evaluate specific XAI
techniques,oroffercriticalanalysisrelevanttoourresearch
questions. Articles lacking sufficient methodological detail
or not directly contributing to the understanding of XAI
systemswereexcluded.Wesystematicallyextractedinforma-
tion from the included articles and organized it around our
threeresearchquestions.Thefollowingkeydatapointswere
included:(1)characteristicsoftheXAImethod(ante-hocvs.
post-hoc;model-specificvs.model-agnostic;localvs.global
scope), (2) the application domain and specific use cases,
(3)theevaluationapproachesemployed(computationalmet-
rics; human-centred assessment; or hybrid methods), and
(4) considerations relating to security, robustness, and reg-
ulatory compliance. Articles were classified into thematic
categories through iterative discussion among the authors.
Any disagreements that arose during classification were
resolved through consensus and reference to established
XAI taxonomies in prior surveys. This approach was both
structured and flexible, enabling us to capture the technical
diversityofXAImethodsandthecontextualnuancesoftheir
deployment across high-stakes domains. Figure 2 provides
a schematic overview of our literature search and selection
process.
FIGURE2. Schematicoverviewofliteraturesearchandselectionprocess.
III. CONCEPTSANDTAXONOMIESOFXAI
TheunderstandingofXAIrequiresengagementwithseveral practitioners must consider the interdependency of their
taxonomic dimensions that do not always align in straight- choices. Model-specific approaches offer high fidelity, but
forward ways. When selecting an explanation method, cannot be applied across different models. In contrast,
VOLUME14,2026 27397

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
TABLE1. Differencebetweenoursurveyandothersurveypapersofasimilarnature.
model-agnostic methods provide flexibility at the cost of factoristheunderlyingmodel.Thesecondfactoristhescope
reduced accuracy. Local explanations address the needs of oftheexplanation.Thethirdfactoristhetimingoftheinter-
individual users,but they donot consider broaderstructural pretabilityprocess.Thisframeworkillustrateshowdifferent
biases. Global explanations capture system level patterns. approachesoccupydistinctpositionsinthedesignspace,each
However, they can overload decision makers. On the one with its own strengths and limitations. The XAI landscape
hand, ante hoc interpretability ensures fidelity but restricts is diverse, there is no single solution that outperforms all
model capacity. On the other hand, post hoc explanations others. Therefore, selecting the right method requires an
allow the use of more complex models but may produce understanding of how these dimensions interact and shape
approximations that are not fully reliable. These trade-offs the resulting explanations. The following subsections pro-
meanthatnosingleXAImethodisuniversallyoptimal.The videmoredetailedexplorationofeachfactorandemphasize
suitable option is dependent on the application context, the the principles that support effective and meaningful XAI
| proficiencyoftheusersandwhethertheprimarygoalistrou- |     |     |     |     |     | practice. |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
bleshooting,regulatoryalignmentorestablishingconfidence.
This section provides a foundation for understanding these A. FUNDAMENTALPRINCIPLESOFEXPLAINABILITY
designconsiderationsandtheirimplications. Meaningful explanations strike a balance among various
|     |     |     |     |     |     | attributes. Interpretability |     | is  | the ability | to understand | how |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | ----------- | ------------- | --- |
Inordertointroduceacertaindegreeofordertothiscom-
plex landscape, we have introduced a taxonomy in Table 2 a model works on the inside, while explainability is the
|                |     |         |           |              |           | ability to explain | how | a model | works | in terms that | people |
| -------------- | --- | ------- | --------- | ------------ | --------- | ------------------ | --- | ------- | ----- | ------------- | ------ |
| that organizes | XAI | methods | according | to a variety | of crite- |                    |     |         |       |               |        |
ria.Thisframeworkenablespractitionerstoidentifysuitable canunderstand[28].AradiologistanalyzingadiagnosticAI
explanation techniques based on deployment requirements, necessitatesdistinctexplanationscomparedtoadatascientist
|     |     |     |     |     |     | troubleshooting | the identical |     | model. | Fidelity assesses | the |
| --- | --- | --- | --- | --- | --- | --------------- | ------------- | --- | ------ | ----------------- | --- |
userexpertise,andregulatoryconstraints.Table2formsthe
basis of the taxonomy employed throughout this analysis. extent to which explanations accurately represent authentic
|     |     |     |     |     |     | decision-making | processes | [29]. | Low-fidelity | explanations |     |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | ----- | ------------ | ------------ | --- |
Thesecategoriesarenotmerelyconceptualdistinctions,but
reflect the practical choices that professionals must make trickusersintothinkingtheyknowwhat’sgoingon,whichis
when implementing XAI systems. The following subsec- worsethannotknowingwhat’sgoingon.Comprehensibility
makessurethatpeoplecanunderstandexplanationswithout
| tions examine |     | each dimension | in detail | and | discuss how |     |     |     |     |     |     |
| ------------- | --- | -------------- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
these design decisions affect the quality of explanations, having to think too hard. An explanation that is completely
computationalrequirements,andusercomprehension. true to model mechanics but makes no sense to the per-
XAI is a broad research area focused on making the rea- son who is supposed to use it is not useful. Finally, scope
soning processes of AI systems more understandable. This sets apart local explanations that clarify individual choices
fromglobalexplanationsthatsumuphowthewholemodel
| field has | grown          | rapidly       | and now encompasses |           | a variety of |            |     |     |     |     |     |
| --------- | -------------- | ------------- | ------------------- | --------- | ------------ | ---------- | --- | --- | --- | --- | --- |
| methods   | developed      | for different | purposes.           | Clear     | conceptual   | works[30]. |     |     |     |     |     |
| models    | and structured | taxonomies    | are                 | essential | to navigate  |            |     |     |     |     |     |
this variety [26]. This section summarizes core XAI princi- B. MODEL-SPECIFICANDMODEL-AGNOSTIC
plesandhighlightsinfluentialtaxonomiesfromrecentwork, APPROACHES
offeringguidanceonselectingthemostsuitableexplanation Aprevalenttaxonomycategorizesmethodsaccordingtotheir
techniques.Figure1providesavisualoverviewofXAImeth- reliance on particular machine learning models [31], [32].
| ods. These | are | organized | around three | key factors. | The first |                |         |     |          |                   |     |
| ---------- | --- | --------- | ------------ | ------------ | --------- | -------------- | ------- | --- | -------- | ----------------- | --- |
|            |     |           |              |              |           | Model-specific | methods | are | designed | to take advantage | of  |
| 27398      |     |           |              |              |           |                |         |     |          | VOLUME14,2026     |     |

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
TABLE2. XAIconceptsandtaxonomies.
the internal structure of certain model families [33]. They surrogatemodelsthatmakepredictionsaboutblackboxesin
usually have better accuracy and are faster at processing. aspecificarea[35].SHAP(ShapleyAdditiveexPlanations)
For instance, following decision tree paths shows reasoning usesShapleyvaluesfromcooperativegametheorytofigure
clearlyanddirectly[34],andlinearmodelcoefficientsshow out how much each feature contributes [36], [37]. SHAP
the effect of each feature directly. In deep learning, Grad- provides unique feature explanations, but calculating exact
CAM(Gradient-weightedClassActivationMapping)makes valuescanbecomputationallydemanding.Foramodelwith
visual explanations by using heatmaps to show important M features, all 2 to the power of M feature combinations
partsofanimage. must be evaluated. This issue is usually resolved by using
Model-agnostic methods look at the input-output rela- approximate methods. Kernel SHAP reduces the number
tionships of models without looking at their internal struc- of evaluations required by applying weighted linear regres-
ture[31],[32].Thisadaptabilitypermitsutilizationacrossany sion, typically needing only 2,000 to 5,000 evaluations per
machinelearningmodel,whichisadvantageousinindustrial explanation. Tree SHAP uses the structure of decision tree
contextswhereproprietarymodelsareimpervioustoscrutiny. ensemblestoperformcalculationsinpolynomialtime,mak-
Twomainmethodsstandoutandshouldbelookedatclosely. ingtheprocessabout2.5timesfasterthanKernelSHAP[38].
LIME (Local Interpretable Model-Agnostic) trains simple Theseapproximationmethodsinvolvesignificanttrade-offs.
VOLUME14,2026 27399

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
TABLE3. Practicalguide:MatchingXAImethodstouserneeds.
In real-world datasets where variables are often correlated, different outcomes; and example-based explanations inter-
theimportancescoresproducedbyKernelSHAPcanbeinac- pret decisions by referencing relevant instances from the
curatebecauseitassumesfeatureindependence.Forinstance, training data [2]. Understanding these classifications pro-
incomeandcredithistoryareusuallyhighlycorrelatedinloan vides guidance for selecting appropriate techniques and
applications, causing independence assumptions to produce highlights that every choice involves trade-offs between
inaccurateresults.TreeSHAPavoidsthisassumption,butitis fidelity, interpretability, computational cost, and scope of
limitedtotree-basedmodels.Researchershaveproposedcon- applicability.
ditionalSHAPvariantstoaccountforfeaturedependencies,
yet they increase computational complexity [39]. Despite D. CRITICALPERSPECTIVESONCURRENTXAI
these advances, fundamental challenges remain. Approxi- TAXONOMIES
mate methods rely on simplifying assumptions, while exact While these taxonomies provide a useful structure, impor-
methods remain computationally infeasible for complex tantconflictsremain.Akeytrade-offexistsbetweenfidelity
models. and interpretability. Model-specific methods offer high
fidelity,butlackgeneralizability;conversely,model-agnostic
approaches sacrifice some fidelity for broader applicability.
C. OTHERTAXONOMICCLASSIFICATIONS Empirical studies highlight these challenges. Schlegel et al.
Thetimingofexplanationgenerationdifferentiatesante-hoc [35] show that LIME explanations can be unstable in high-
from post-hoc methods [40]. Ante-hoc approaches integrate dimensional data. Slack et al. [13] demonstrate that SHAP
interpretability directly into the model architecture using explanationscanbeeasilymanipulated,withattackschang-
transparent structures, such as linear or logistic regression ing 90 percent of explanations while keeping 75 percent of
andshallowdecisiontrees.Thesemodelspreciselyreflectthe the model’s original accuracy. Table 3 provides guidance
modellogic,astheexplanationmechanismisidenticaltothe to help match XAI methods to specific use cases, translat-
model itself. However, models designed for interpretability ing taxonomic concepts into practical recommendations for
often underperform compared to black-box models when different users and contexts. This emphasizes the fact that
it comes to tasks requiring complex pattern recognition. effectiveXAIusedependsonselectingmethodsaccordingto
This creates a dilemma in high-stakes applications. The theapplication,ratherthanfollowinggeneralbestpractices.
dilemma lies in whether to prioritize interpretability at the Thenextsectionevaluatestheperformanceofthesemethods
cost of a potentially non-negligible reduction in predictive in real-world settings and explores additional deployment
performance, or to favor high-performing but less transpar- challenges.
entblack-boxmodels.Notably,thisaccuracy–interpretability
trade-off is not universal, and recent studies argue that IV. DOMAIN-SPECIFICAPPLICATIONSOFXAI
interpretable models can achieve competitive performance, Table 4 shows that matching explanation methods to dif-
particularly in high-stakes decision-making scenarios [41]. ferent types of users and decision contexts can help people
Post-hoc methods, by contrast, generate explanations after makebetterdecisions.ThisshowsthatgoodXAIisn’tabout
training by analyzing pre-trained black-box models [42]. finding the best methods for everyone; it’s about choosing
This approach allows us to understand complex sys- methods that fit the user’s level of knowledge, the task at
tems, such as deep neural networks, as demonstrated by hand,andthelimitationsofthedeployment.Thetextgivesan
methods like LIME, SHAP, and Grad-CAM [43]. Post- overviewofhowXAIisusedinimportantareaslikefinance,
hoc explanations can be classified according to their healthcare, and cybersecurity. It then goes into detail about
approach: feature attribution evaluates the contribution of each application, including its use cases, goals, and meth-
each input to the model’s output; counterfactual explana- ods. This structured overview highlights the requirements
tions identify minimal changes to inputs that would lead to specific to each domain and the challenges that affect more
27400 VOLUME14,2026

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
TABLE4. Domain-specificapplicationsofXAI.
than one application area. The applications in Table 4 show But being able to do it technically isn’t enough for a suc-
that XAI has the power to change many different fields. cessfuldeployment. Itisveryimportant tocarefullylookat
VOLUME14,2026 27401

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
domain constraints, user expertise, and regulatory require- canequalorsurpasstheperformanceofexpertsintheanalysis
ments.Thefollowingsubsectionswilllookateachsectorin ofmedicalimages.Grad-CAMandothermodel-specificXAI
detail,coveringboththesuccessesandtheproblemsthatkeep techniquescreatevisualexplanationsbyhighlightingpartsof
comingup. animagethathadthebiggesteffectondecisions.Thisgives
Theoretical XAI frameworks demonstrate their true sig- clear visual proof [54], [55]. But the most important thing
nificancewhenutilizedinpracticalscenarios.Inhigh-stakes is that the explanation is reliable. Recent studies show that
areaswherechoiceshaveadirecteffectonpeople’slives,the visual explanation methods have serious weaknesses. Stud-
economy,andnationalsecurity,XAIhasgonefrombeinga iesindicatethatheatmap-basedexplanationsmayemphasize
nice-to-have technology to an ethical and operational must- non-pathological image regions that inadvertently correlate
have.ThissectionlooksathowXAIisusedinthreeimportant with disease in training datasets, rather than authentic dis-
fields: finance, healthcare, and cybersecurity. It also talks ease indicators. In a recorded instance, a model accurately
about the Human-Centered XAI paradigm that underlies all detectedthepresenceofdisease,butthisdeterminationwas
ofthem. predicated on an extraneous watermark that appeared more
frequentlyinimagesofdiseasedpatients.Thisisabigprob-
lemfordoctorsbecausetheymighttrustAIrecommendations
A. XAIINTHEFINANCIALSECTOR
thatmakewrongpredictionsbasedonbadreasoningifthey
The financial sector is one of the main users of algorithmic
useexplanationvisualizations.Inmedicalcontexts,thisissue
decision-making,whichhasledtomorecallsfortransparency
of reliability is more than just a technical problem; it is a
frombothregulatorsandcustomers[45].Black-boxmodels
patientsafetyissuethatneedstobecarefullycheckedbefore
can make decisions that are not clear and may be biased,
beingusedinaclinicalsetting[56].Thisriskemphasizesthat
whichcanleadtobigfinanciallossesandlegalpenalties[46].
inhealthcare,explainabilityisnotonlytechnicalbutessential
XAIgivesusimportanttoolstolowertheserisksinanumber
forclinicalsafetyandaccountability.Unreliableexplanations
ofdifferentareas.
can create a false sense of security and cause mistakes in
XAI methods, especially SHAP, show important factors
diagnosis.XAIisimportantformorethanjustdiagnostics;it
thataffectloanoutcomesbymeasuringhowmucheachfea-
is also important for models that predict patient risk scores
turecontributes[47],[48].Butthecomputationalburdenfor
or suggest personalized treatments. Clinicians must com-
millionsofcustomersslowsdownreal-timedecision-making,
prehend the rationale behind recommendations to trust and
andit’sstillnotclearifSHAPvisualizationsarelegallysuffi-
implementthem.XAIdoesthisbyexplainingthethingsthat
cientexplanationsunderGDPR.Thisshowsthegapbetween
lead to high-risk classifications, which makes it possible to
academicfeasibilityandoperationalcompliance.
makesmartdecisionsabouthowtointervene[57],[58].Addi-
XAIexplainswhytransactionswereflagged,whichhelps
tionally, counterfactual explanations can directly influence
analystsquicklylookintoalerts[49],[50],[51].Anexplana-
treatmentstrategiesbyaddressinghypotheticalinquiries[59].
tionthatsays‘‘firstinternationaltransactionfromnewdevice
In summary, XAI in healthcare is changing from a tool
at unusual hour’’ is more important than the amount of the
for making things clear to a necessary part of making sure
transactionbeingslightlyaboveaverage.Thiscutsdownon
patients are safe, improving clinical decision-making, and
the time spent on false positive investigations by 60% and
holdingprofessionalsaccountable.
increasesthenumberofdetections.
XAI applications in healthcare extend beyond medical
It is very important to explain how complex models used
imaging to clinical decision support systems (CDSS) and
for high-frequency trading and portfolio optimization make
pharmaceuticalresearch.InCDSS,forexample,explainable
decisionsinordertoteststrategiesandunderstandhowpeo-
models can help clinicians to understand why a patient has
ple act when the market is unstable. XAI boosts portfolio
been classified as high-risk, enabling targeted preventive
managers’ trust in algorithmic strategies and improves risk
interventionstobeimplemented.Counterfactualexplanations
management by explaining why a model chooses to buy or
provide answers to clinically actionable questions, such as
sellcertainassets[52].Inshort,XAIinfinanceisimportant
’If the patient’s blood pressure had been 20 mmHg lower,
forbuildingtrust,makingsurerulesarefollowed,andmaking
would their sepsis risk score have decreased by 15%?’,
automateddecision-makingprocessesworkbetter.
thereby informing treatment decisions directly [57], [58].
These explanations bridge the gap between AI predictions
B. XAIINTHEHEALTHCARESECTOR and clinical reasoning, enabling practitioners to validate AI
Healthcare professionals need to trust AI for it to be used recommendationsagainsttheirexpertiseandidentifypoten-
in their field, especially when the decisions made by the tial errors in the model before they affect patient care.
modelhaveadirecteffectonpatients’lives.Becausedoctors In drug discovery and molecular property prediction, XAI
are ultimately responsible, understanding how AI works is has become essential for speeding up compound screen-
not a nice-to-have, but a must-have for integrating it into ing and identifying structure-activity relationships [111],
clinical workflows [53]. XAI is an important way to build [112],[113].Graphneuralnetworkexplanationsrevealwhich
this trust. In diagnostic fields such as radiology, pathology, molecularsubstructurescontributetodesiredpharmacologi-
and dermatology, Convolutional Neural Networks (CNNs) cal properties, enabling medicinal chemists to design more
27402 VOLUME14,2026

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
effectivecompoundswhileavoidingtoxicstructures.Recent deceptive linguistic patterns and suspicious URL features.
advances in chemistry-intuitive explanation methods, such Naturallanguageprocessing–basedexplainabilitytechniques
as substructure masking, provide interpretations that align reveal which words, phrases, or structural elements trigger
withestablishedchemicalprinciples.Thisenablesscientists maliciousclassifications,helpinguserstounderstandwhyan
to validate AI predictions against their own knowledge of email has been flagged [48]. In digital forensics, XAI sup-
thefield.AsJiménez-Lunaetal.emphasizeintheircompre- portsincidentinvestigationsbyprovidingcausalexplanations
hensive review of drug discovery in, explainability bridges ofattacksequencesandcounterfactualanalysesthattracethe
the gap between AI’s predictive power and the mechanistic provenanceofsecuritybreaches.Thishelpstoanswercritical
insights required for experimental validation and regulatory questions such as ’Which initial access vector enabled the
approval[111]. attacker to escalate privileges?’ These applications demon-
stratethatXAIisnotmerelyatoolformodeltransparency,but
apracticalnecessityfortheimplementationofAIinsecurity-
C. XAIINCYBERSECURITY critical contexts, where analysts must be able to trust and
Every day, cybersecurity analysts get thousands of alerts verifyAI-generatedinsightsquickly.
aboutpossiblethreats.Withoutexplainability,thesealertsjust
mark IP addresses or files as suspicious without giving a V. SECURITYANDROBUSTNESSPERSPECTIVES
reason,whichmeansthateachincidenthastobelookedinto Table 5 lists the different kinds of security threats that XAI
by hand. XAI changes this workflow by giving you infor- systems face and the best ways to protect against them.
mation that you can use. XAI shows specific evidence that It separates attack vectors that target the disclosures them-
sets off alerts in intrusion detection, such as unusual packet selves,likeforgeryandfairwashing,fromdefensestrategies
sizes that suggest data exfiltrationattempts, communication that make disclosures stronger and more reliable. Table 5
patterns that match known malicious hosts, or behavioral shows that the threat landscape needs more than just tra-
sequences that are typical of certain types of attacks [60], ditional adversarial robustness to protect disclosures. The
[61]. When an analyst sees the phrase ‘‘flagged due to a subsequentsubsectionsconductathoroughanalysisofthese
10MB outbound data transfer to an unknown IP address vulnerabilities,evaluatingtheeffectivenessofvariousattack
at 3pm,’’ they know right away how serious the threat is methodologies and the practicality of the proposed defense
and what to do about it. But when they see the phrase sus- strategies.TheadventofXAIseekstoaddressthecorechal-
picious activity detected, they have to spend time looking lenge of trust in opaque models. However, it is important
into it. This contextual understanding speeds up incident to note that explanations create new vulnerabilities because
response from hours to minutes and lowers the number of enemies can change them while keeping predictions the
false positives by letting analysts quickly ignore harmless same [13], [14]. This part talks about the threat landscape,
anomalies.Malwareanalysisalsobenefitsfromexplanations howwellattackswork,andnewwaystoprotectagainstthem.
that show which file characteristics caused the classifica-
tion [62]. XAI identifying particular API call sequences, A. ADVERSARIALATTACKSONXAIEXPLANATIONS
code segments, or behavioral patterns facilitates analysts’ Beyond adversarial manipulation, XAI systems face three
comprehensionofnewmalwarefamiliesandevolvingattack additional critical threats that undermine the reliability of
vectors.InsteadofseeingAIasamysteriousoracle,security deployment. Firstly, privacy leakage occurs when explana-
teams use it to learn things that help them make decisions tions inadvertently reveal sensitive information about the
abouthowtoprotectthemselvesandgatherinformationabout training data, the model architecture or individual data
threats. points [115], [116], [117]. Model inversion attacks can
ApplicationsofXAIincybersecurityextendbeyondintru- reconstruct approximate training samples from explana-
sion detection and malware analysis to encompass botnet tion outputs, while membership inference attacks exploit
detection, phishing and spam filtering, and digital foren- gradient-based explanations to determine whether specific
sics [48], [59], [74], [114]. In the case of botnet detection, individualswereincludedinthetrainingset.Recentresearch
for example, explainable models can identify coordinated shows that multiple explanation methods, including SHAP,
malicious traffic patterns by revealing which network flow LIMEandgradient-basedattributions,createprivacyvulner-
features indicate botnet activity, such as synchronized con- abilities that could violate regulations such as the GDPR.
nection timestamps, shared command-and-control server The trade-off between privacy and transparency is partic-
communicationsoranomalousDNSquerysequences[114]. ularly acute in healthcare and finance, where explanations
These explanations enable security analysts to distinguish must balance regulatory requirements for transparency with
between legitimate distributed systems and malicious bot- confidentialityobligations.
nets, thereby reducing the number of false positives that Secondly, over-reliance on explanations can lead to
affect purely statistical approaches. Understanding which automation bias, whereby users uncritically accept AI deci-
features trigger alerts enables analysts to refine detection sions simply because an explanation is provided, regardless
rules and adapt to evolving attack tactics. Phishing and of the quality of the explanation or the correctness of
spamdetectionalsobenefitfromXAImethodsthathighlight the model [118], [119], [120]. Empirical human-computer
VOLUME14,2026 27403

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
TABLE5. SecurityandrobustnessperspectivesinXAI.
interaction research shows that explanations often fail the scope of the explanation. They remain overconfident
to improve human-AI team performance; instead, they when they misinterpret it [121]. For example, a clinician
increase acceptance of AI recommendations, even incorrect might incorrectly assume that a Grad-CAM heatmap high-
ones [119]. Bansal et al. found that explanations increased lightingaspecificanatomicalregionprovesthatthemodel’s
users’ likelihood of accepting AI suggestions regardless of diagnostic reasoning aligns with medical knowledge when,
their accuracy, thus failing to achieve the expected appro- in fact, the heatmap merely reflects gradient magnitudes.
priate trust calibration [119]. Buçinca et al. demonstrated Nguyen et al.’s study found that feature attribution was no
that cognitive forcing interventions, which require users to more effective than showing the nearest training examples
makeinitialjudgementsbeforeseeingAIrecommendations, for human decision-making [123]. Without proper training
werenecessarytoreduceoverreliance.However,usersrated inexplanationsemantics,usersriskmakingcriticaldecisions
theseinterventionsleastfavourably[118].Thisphenomenon basedonfundamentallyflawedinterpretations.
is particularly problematic in high-stakes domains, where Conventional adversarial attacks modify model inputs to
simplifiedexplanationscancreateafalsesenseofconfidence changepredictions,butnewresearchshowsthatattackscan
in the reliability of the model. Thirdly, the misinterpreta- also target XAI explanations directly [13]. The most dan-
tion of explanations can pose fundamental challenges to gerous thing about them is that they can change prediction
the effective collaboration between humans and AI [121], explanations a lot without changing model outputs [14].
[122], [123]. For instance, users frequently conflate feature This lets attackers keep the model’s decisions correct while
importancewithcausality,orinterpretsaliencymapsasliteral making up all the evidence that supports them. This kind
representationsofwhatthemodel‘sees’,ratherthanasgra- of manipulation, which is often called a ‘‘spoofing attack,’’
dient approximations. Xuan et al. demonstrated that highly takes advantage of users’ trust by giving them plausible but
comprehensibleexplanationsareexceptionallysusceptibleto fundamentallyfalsereasons[66].Thereal-worldeffectsare
misinterpretation. Users infer information that lies outside very bad. Think of a medical imaging model that can find
27404 VOLUME14,2026

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
a tumor in an X-ray. An attacker could add noise to the assessment through sanity checks. The fundamen-
imagethatistoosmalltosee,whichwouldmakeexplanation tal principle is measuring explanation stability when
methods like Grad-CAM highlight areas that aren’t impor- subjected to semantically irrelevant or minor input
tant, like healthy tissue or artifacts in the image, instead of variations [74]. Dramatic explanation changes result-
the tumor itself [14]. The model’s prediction of the tumor’s ing from small, random perturbations strongly indicate
presence is still accurate, but the misleading visualization unreliability. To enable this, metrics for explanation
couldmakedoctorsquestionthediagnosis,whichcoulddelay robustness or stability have been developed, allow-
important treatment [67]. The threat has been measured in ing quantitative comparison of different XAI methods’
the following way: Scaffolding attacks have demonstrated reliability [75]. Adversarial Training for Explainers:
a 90.8% accuracy in annotations while obscuring bias in Mirroring adversarial training used to fortify models
credit scoring [13]. Similar methods have been shown to themselves,itispossibletoenhanceexplanationmech-
change descriptions of medical images with a 95% success anismresilience.Thistechniqueinvolvesincorporating
rate[14],whichleadstothewrongattributionofdiagnostic a loss function during training that minimizes both
evidence. model prediction error and explanation variability or
Adversarial attacks go beyond image-based systems and inconsistency. By exposing the system to intentionally
into tabular domains. In financial situations, a biased credit perturbed inputs [76], it learns to generate consistent
modelcouldbeusedtomakeSHAPexplanationsthatblame interpretations even under attack, thereby increasing
rejections on valid reasons (like ‘‘high debt ratio’’) while overallexplainerrobustness[77].
hiding discrimination based on protected traits. This trick, Current defenses show promise but face adoption barriers.
knownasfairwashing[66],makesethicalauditinglesseffec- Certified robust explanation methods providing mathemat-
tive. Biased systems can avoid following the rules (see ical guarantees reduce attack success from 90% to 34%,
SectionVII-B).Thisoccurrenceengendersasignificantpara- yetremainunderutilizedindeployment[73].Computational
dox. It is clear that tools designed topromote openness and overheadincreasesexplanationtimeby3-5×,creatingoper-
build trust can actually be used to avoid scrutiny and hide ationalfriction.Smoothingtechniquesaveragingovernoisy
harmful biases. This discovery signifies that the establish- inputsimprovestabilitybutassumeattackerscannotadaptto
ment of resilient defenses against malevolent entities must this defense [72]. Adversarial training for explainers shows
be prioritized above all else in the field of XAI research. effectiveness in controlled settings but lacks large-scale
Attackers usually figure out the changes they need to make deployment validation [76], [77]. Current defenses show
by solving optimization problems that change explanation promisebutfaceadoptionbarriers.Certifiedrobustexplana-
maps in certain ways while keeping model predictions the tion methods reduce attack success [73], yet computational
same[68].Theseattackshavebeensuccessfulwithdifferent overheadincreasesexplanationtimeby3−5×.Organiza-
typesofdata,suchasimages,text,andtables[69].Thisshows tions must balance security against operational constraints.
how important it is to make sure that explanations are as In summary, as XAI becomes integral to safety-critical sys-
strongasmodelpredictions. tems, its own security and robustness must be treated as
criticalresearchobjectives.Withoutreliableexplanations,the
B. DEFENSEMECHANISMSANDRELIABILITY promise of transparency risks becoming a potent vector for
ASSESSMENT manipulation.
Inresponsetothesevulnerabilities,theresearchcommunity
is actively developing defense mechanisms and reliability VI. EVALUATIONOFEXPLANATIONS
assessmentframeworks.Theprimaryobjectiveisgenerating TofigureouthowusefulXAIisintherealworld,weneedto
explanationsthatarerobust,stable,andfaithfultothemodel’s do a lot of human-centered testing. Fidelity and other com-
genuinereasoningprocess[70],[71]. putational metrics don’t do a good job of showing whether
➢ Inherently Robust Explanation Methods: One defen- users make better decisions [44]. This part talks about why
sive strategy focuses on creating explanation methods computational metrics aren’t enough and what makes an
inherently less susceptible to adversarial perturbations. evaluationmeaningful.
For example, smoothing techniques averaging expla- Table6organizestheevaluationlandscapeintothreeareas:
nations over multiple noisy input copies have been human-centered frameworks that measure both subjective
proposed to mitigate instabilities common in gradient- and objective user outcomes, components that define useful
basedmethods,reducingsensitivitytominormalicious explanations,andongoingproblemswithstandardizationand
perturbations [72]. Beyond these, certified robustness scalability.Thisframeworkshowswhyusingonlycomputa-
approaches aim to provide mathematical guarantees tionalmetricsisn’tenoughtomeasurehowwellXAIworks.
that explanations will remain consistent within prede- TheevaluationdimensionsinTable6showthatthequality
fined perturbation bounds, offering a higher assurance of an explanation can’t be based only on the properties of
standard[73]. thealgorithm.Trueeffectivenessonlycomesfromthorough
➢ Reliability Assessment and Sanity Checks: Another human-centeredtestingthatchecksifexplanationshelppeo-
defensive approach involves systematic reliability ple make better decisions, build trust in the right way, and
VOLUME14,2026 27405

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
| meet user | needs. | The | next few | sections | go  | into more | detail |     |     |     |     |
| --------- | ------ | --- | -------- | -------- | --- | --------- | ------ | --- | --- | --- | --- |
aboutevaluationmethodsandproblemsthatkeepcomingup
inthisarea.
A. HUMAN-CENTEREDEVALUATIONFRAMEWORKS
| Human-centered |      | evaluation   |       | sees explanations |      | as      | ways to  |     |     |     |     |
| -------------- | ---- | ------------ | ----- | ----------------- | ---- | ------- | -------- | --- | --- | --- | --- |
| communicate    | and  | measures     | their | effectiveness     |      | by      | how they |     |     |     |     |
| affect people, |      | not by       | how   | well they         | work | with    | algo-    |     |     |     |     |
| rithms [78].   | This | necessitates |       | regulated         | user | studies | that     |     |     |     |     |
gatherbothqualitativeandquantitativedata,establishingiter-
ativedevelopmentcyclesinwhichhumanfeedbackdirectly
influencessystemenhancement,asdepictedinFigure3.
| Human-centered     |     | evaluation |           | looks at | two                | different | things. |     |     |     |     |
| ------------------ | --- | ---------- | --------- | -------- | ------------------ | --------- | ------- | --- | --- | --- | --- |
| First, subjective  |     | perception | looks     | at       | user satisfaction, |           | trust,  |     |     |     |     |
| understandability, |     | and        | perceived | adequacy |                    | through   | surveys |     |     |     |     |
andinterviews[79],[80].Thesemetricsshowwhetherusers
| think the | explanations |     | are credible | and | helpful | for | the deci- |     |     |     |     |
| --------- | ------------ | --- | ------------ | --- | ------- | --- | --------- | --- | --- | --- | --- |
sionstheyneedtomake[81].Second,objectiveperformance
measures the concrete impact of tasks [82], [83]. Standard FIGURE3. Thehuman-in-the-loopXAIdevelopmentandevaluation
lifecycle,emphasizingiterativeimprovementandhuman-centric
evaluationframeworksencompassvariouspracticalconfigu- assessmentfortrustworthyAIsystems.
rations.Inonemethod,userslookatthemodel’sexplanation
| and then      | try to     | guess | how it   | will act | on new,         | unseen | data. |          |                    |                   |            |
| ------------- | ---------- | ----- | -------- | -------- | --------------- | ------ | ----- | -------- | ------------------ | ----------------- | ---------- |
|               |            |       |          |          |                 |        |       | enhanced | through systematic | user interaction. | The itera- |
| If they guess | correctly, |       | it means | that     | the explanation |        | did a |          |                    |                   |            |
goodjobofconveyingknowledge.Inanothermethod,users tive lifecycle shown in Figure 3 is the best way to build
|           |         |        |             |     |           |     |          | human-centered | XAI systems. | However, | as the following |
| --------- | ------- | ------ | ----------- | --- | --------- | --- | -------- | -------------- | ------------ | -------- | ---------------- |
| are asked | to find | biases | or mistakes |     | that were | put | into the |                |              |          |                  |
modelonpurpose.Thespeedandaccuracywithwhichthey analysisshows,thismodeldoesn’talwaysmatchupwithhow
|     |     |     |     |     |     |     |     | research is | actually done. | Most studies | don’t use rigorous |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------------ | ------------------ |
findthemshowshowwelltheexplanationshowsweaknesses.
|                  |          |            |           |            |            |       |           | human evaluation | and instead | rely only | on computational |
| ---------------- | -------- | ---------- | --------- | ---------- | ---------- | ----- | --------- | ---------------- | ----------- | --------- | ---------------- |
| Lastly, users    | can      | make       | decisions | with       | or without |       | explana-  |                  |             |           |                  |
| tions, and       | the fact | that       | their     | decisions  | get better | shows | that      | metrics.         |             |           |                  |
| the explanations |          | are useful | in        | real life. | Systematic |       | analysis, |                  |             |           |                  |
ontheotherhand,showsworryingtrends.Akhtaretal.[44] B. COMPONENTSOFAMEANINGFULEXPLANATION
found30differentevaluationcomponentsinthestudiesthey Inadditiontohuman-centredevaluationframeworks,techni-
looked at. This shows that assessment needs to be done in cal metrics provide a quantitative assessment of the quality
a way that takes into account trust, comprehensibility, task of explanations that is essential for a systematic compar-
performance,andusersatisfaction.Nevertheless,merely26% ison. Localization metrics evaluate whether explanations
of studies utilized established frameworks. Trust was the correctly identify relevant input regions, which is partic-
mostcommonlyassesseddimensionin46outof77studies;
|     |     |     |     |     |     |     |     | ularly critical | for vision | tasks [124], | [125], [126]. The |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ------------ | ----------------- |
however,resultsregardingtheefficacyofexplanationsvaried pointinggame,introducedbyZhouetal.,measureswhether
significantlyaccordingtouserexpertiseandtaskcomplexity. the maximum activation in a saliency map falls within
This variability stems not from XAI method limitations but the ground-truth object bounding boxes. Intersection over
fromfailuretoaccountforcontext-dependentfactors.Aclar- Union(IoU)betweenexplanationheatmapsandground-truth
ification that helps data scientists fix models might confuse annotationsprovidesadetailedmeasurementofspatialover-
doctorswhoaretryingtomakeadiagnosis.Kadietal.[84] lap[124].Petsiuketal.’sdeletionandinsertionmetricsassess
discovered that although the utilization of quantitative eval- faithfulness by measuring how model confidence changes
uationmethodsrosefrom40%in2016to70%in2020,the as pixels are progressively removed or added in order of
ratesofuserstudiesremainedconstantatapproximately20%. attributedimportance[126].Together,thesemetricsaddress
Thisdifferencebetweencomputerevaluationandhumanval- the question of whether explanations actually point to the
idation is why systems that work well in the lab often fail featuresonwhichthemodelrelies.Complexitymetricsquan-
whentheyareputintouse. tify explanation simplicity, recognizing that overly detailed
Figure3showstheiterativehuman-in-the-loopXAIdevel- explanationsmayoverwhelmusersdespitebeingtechnically
opment lifecycle. It shows how system design, human accurate[35],[127],[128].LIME’sfoundationalformulation
evaluation, and refinement all work together in a continu- explicitlyincludesacomplexitypenalty(cid:127)(g),favoringsparse
ous feedback loop. This process model signifies a pivotal explanationswithfewernon-zerofeatureweights[35].
transformationfromperceivingexplanationsasstaticoutputs The complexity of rule-based explanations can be mea-
torecognizingthemasdynamiccommunicationinstruments sured by decision tree depth or the number of conditions.
| 27406 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
TABLE6. EvaluatingXAIdisclosures.
Empirical evidence from cognitive science indicates that feature importance, in line with limitations of working
explanations that highlight three to five key features are memory [127], [128]. However, the optimal complexity-
more comprehensible to humans than exhaustive lists of accuracy trade-off remains context-dependent: for example,
VOLUME14,2026 27407

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
medical diagnosis may require more detailed explanations significantly improve loan approval likelihood’’ [89]. This
than credit decisions. Consistency (or stability) is used to transforms explanations from passive information displays
evaluatewhetherexplanationmethodsproducesimilarresults into practical decision-support tools. However, balancing
for semantically similar inputs [33], [69], [129]. Álvarez- these dimensions creates design tensions: highly interactive
Melis and Jaakkola formalized this concept through local systemsmayoverwhelmnoviceusers,whileactionablerec-
Lipschitz continuity: an explanation method is considered ommendationsriskoversimplifyingcomplexmodelbehavior.
robust if small input perturbations result in proportionally Effective explanation systems must adapt to user expertise,
minorchangestotheexplanation[129]. taskcontext,anddecisionstakes.
| Ghorbani | et  | al. empirically |     | demonstrated | that | popular |     |     |     |     |     |     |     |
| -------- | --- | --------------- | --- | ------------ | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
attributionmethodsarefragile,perceptuallyidenticalinputs C. CHALLENGESINSTANDARDIZATIONANDMETRICS
can receive vastly different explanations, indicating low The lack of a standardized evaluation system leads to frag-
| reliability | and potential |     | susceptibility | to  | adversarial | manip- |           |      |            |           |           |         |     |
| ----------- | ------------- | --- | -------------- | --- | ----------- | ------ | --------- | ---- | ---------- | --------- | --------- | ------- | --- |
|             |               |     |                |     |             |        | mentation | that | stops real | progress. | Different | studies | use |
ulation [33]. High consistency is essential for user trust. different metrics, which makes it impossible to compare
If a model provides drastically different explanations for themdirectlyandmakesithardtotellwhichmethodsreally
similar cases, users cannot develop a reliable mental model work[90],[91].Thisfragmentationisasignofrealcomplex-
of the system’s behaviour. Finally, randomisation tests are ity:thereisnoone-size-fits-allexplanation,andwhatworks
criticalsanitychecksthatverifywhetherexplanationmethods
forradiologistsinterpretingmedicalimagesisverydifferent
genuinely capture the model’s reasoning or merely gener- fromwhatloanofficersneedtomakecreditdecisions.Butthe
ate visually plausible results. Adebayo et al.’s pioneering lackofstandardsgoesbeyondcontext-dependencetoinclude
| work introduced |     | model | parameter | and | data randomisation |     |                |     |                |        |     |          |            |
| --------------- | --- | ----- | --------- | --- | ------------------ | --- | -------------- | --- | -------------- | ------ | --- | -------- | ---------- |
|                 |     |       |           |     |                    |     | methodological |     | inconsistency. | Akhtar | et  | al. [44] | discovered |
tests: valid explanation methods should produce substan- studiesthatassessedtrustusing15distinctinstruments,sat-
| tially different |     | results when | model | weights | are randomised. |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------ | ----- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
isfactionthrough12variedscales,andcomprehensibilityvia
Their analysis revealed that widely used methods such as 8differentevaluationmethods.Withoutstandardizedmetrics,
Guided Backpropagation fail these sanity checks, they act one study’s ‘‘high user satisfaction’’ cannot be compared to
| as edge | detectors | rather | than | model-specific |     | explainers. |            |           |     |              |     |            |        |
| ------- | --------- | ------ | ---- | -------------- | --- | ----------- | ---------- | --------- | --- | ------------ | --- | ---------- | ------ |
|         |           |        |      |                |     |             | another’s, | hindering | the | accumulation | of  | knowledge. | Scala- |
Subsequent work by Kim et al. extended these tests to cre- bilityofhuman-centeredevaluationposesfurtherchallenges.
| ate synthetic | evaluation |     | environments |     | with known | ground |                  |     |            |       |        |                   |     |
| ------------- | ---------- | --- | ------------ | --- | ---------- | ------ | ---------------- | --- | ---------- | ----- | ------ | ----------------- | --- |
|               |            |     |              |     |            |        | It costs $15,000 |     | to $50,000 | to do | a full | human experiment, |     |
truth [131]. These sanity checks are essential quality assur- andittakesmonthstofinish[84].Thiscostexplainswhyso
ancemechanisms.Withoutthem,practitionersriskdeploying fewpeopleuseit:only22%ofpapersincludehumansubjects.
explanationmethodsthatprovideillusoryratherthangenuine
Researchersareforcedtouseautomatableproxymetricsthat
interpretability. areclosetohumanjudgmentbecausetheydon’thaveenough
| Human-centered |     | evaluation |     | reveals | that effective | expla- |           |       |             |           |     |                    |     |
| -------------- | --- | ---------- | --- | ------- | -------------- | ------ | --------- | ----- | ----------- | --------- | --- | ------------------ | --- |
|                |     |            |     |         |                |        | resources | [92]. | Still, it’s | not clear | how | well computational |     |
nations must balance multiple interconnected dimensions. proxies reflect human understanding, trust, and the quality
Ratherthanexcellinginasingleaspect,meaningfulexplana- of decision-making. A metric that works with human judg-
tionsintegrateseveralkeycomponents.Fidelityandaccuracy
|     |     |     |     |     |     |     | ments in | one study | might | not work | in other | situations, | with |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | -------- | -------- | ----------- | ---- |
form the technical foundation: explanations must faithfully differentlevelsofexpertise,orindifferenttaskareas.Todeal
| represent | true model | decision-making |     |     | processes | [85]. This |     |     |     |     |     |     |     |
| --------- | ---------- | --------------- | --- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
withtheseproblems,infrastructuredevelopmentneedstobe
provesparticularlychallengingforpost-hocmethodsapplied coordinated.Theresearchcommunityrequirescollaborative
to black-box models. Low-fidelity explanations mislead evaluation platforms featuring standardized protocols, uni-
| users, potentially |     | causing | more | harm than | original | opaque |               |      |            |              |     |              |     |
| ------------------ | --- | ------- | ---- | --------- | -------- | ------ | ------------- | ---- | ---------- | ------------ | --- | ------------ | --- |
|                    |     |         |      |           |          |        | form datasets | that | facilitate | reproducible |     | comparisons, | and |
systems by creating false understanding [86]. Comprehen- meticulouslycraftedbenchmarkingtasksthatencompassvar-
sibility ensures accessibility to target audiences through ious application domains and user proficiency levels. Big
appropriate cognitive fit [87]. Drawing from cognitive sci- fundinggroupsshouldstartprogramstohelpthisinfrastruc-
ence principles, effective explanations minimize cognitive ture.Withoutstandardizedframeworks,XAIdevelopmentis
| load through | concise | presentation. |     | Visualizations |     | highlight- |     |     |     |     |     |     |     |
| ------------ | ------- | ------------- | --- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
limitedbecauseitisimpossibletosayforsurewhichmethods
ingtop3-5determiningfactorstypicallyprovemoreeffective workbestformakingdecisionsincertainsituations.
thanexhaustivefeatureimportancelists.Explanationformat
| must match | audience | expertise |     | and information |     | processing |     |     |     |     |     |     |     |
| ---------- | -------- | --------- | --- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
D. HUMAN-CENTEREDDESIGNCONSIDERATIONS
capabilities.ContemporaryXAIsystemsincreasinglyincor- The ultimate effectiveness of any explanation relies on
porateinteractivityandactionability.Interactiveexplanations the human user, a principle that transcends all applica-
enable counterfactual exploration, allowing users to probe tion domains. Human-Centered XAI (HCXAI) is a model
what-if scenarios and develop nuanced model understand- that says explanations must be not only technically correct
ing[88].Actionableexplanationsextendfurtherbyproviding
|     |     |     |     |     |     |     | but also | easy to | understand, | use, | and help | end | users [63]. |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ----------- | ---- | -------- | --- | ----------- |
concreteguidanceforachievingdifferentoutcomes,suchas An explanation that is completely true to the mechanics
specifyingthat‘‘increasingannualincomeby$10,000would of the model but too hard for a doctor or loan officer to
| 27408 |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
understand is not very useful in practice. So, HCXAI sup- These methods applied post-hoc explanations to already-
ports the idea of making and testing explanations that are trained models. The underlying assumption: more informa-
based on the needs, skills, and cognitive profiles of dif- tionaboutmodeldecisionswouldnaturallytranslatetobetter
ferent users. This research framework utilizes user studies human understanding and appropriate trust. XAI 2.0 repre-
and surveys to assess the impact of explanations on trust, sents fundamental paradigm shift [94]. Rather than simply
decision-makingenhancement,andthefacilitationofhuman- explaining model decisions, the goal becomes enabling
system interaction [64], [65]. The transition from purely informedhumandecision-makingthroughinteractiveexpla-
technical XAI to Human-Centered XAI signifies a pivotal nationsystems.Evaluationshiftedfromcomputationalmet-
paradigmshifttowardsthedevelopmentofsystemsintended rics toward human-centered measures: do users actually
for collaboration rather than mere understanding. In short, make better decisions, can they identify model weaknesses,
XAIapplicationsthatarespecifictoacertainfieldhavethe do they appropriately calibrate confidence in recommenda-
potential to change the way things work by making them tions. Methods evolve to include interactive counterfactual
more open and accountable in areas where these traits are exploration,adaptiveformatsadjustingtouserexpertise,and
necessary.Tofullyrealizethispotential,though,weneedto certified robustness ensuring explanations resist manipula-
closeimportantgapsbetweentechnicalfeasibility,regulatory tion[95],[96],[97],[98],[99],[100].Thisparadigmrequires
compliance,andhuman-centereddesign. deep interdisciplinary integration with cognitive science,
human-computer interaction, and legal frameworks. This
VII. CHALLENGESANDFUTURERESEARCHDIRECTIONS transitionwasdrivenbypracticalfailuresinXAI1.0.Labora-
XAIhasmadealotofprogressinmakingiteasiertounder- torystudiesincreasinglydemonstratedthattechnicallyaccu-
standcomplicatedmodels.Yetthisalgorithmicmaturityhas rate explanations do not reliably improve human decision-
not translated into widespread deployment success in high- making.Morealarmingly,researchrevealedexplanationscan
stakesdomains.ThreemainproblemsstopXAIfromkeeping be adversarially manipulated while preserving predictions
its promise of reliable AI. First, technical scalability limits: (SectionIV),meaningtransparencycanbeweaponizedrather
techniquesmadeformodelswithmillionsofparameterscan’t than enabling understanding. These findings show that the
workwithfoundationmodelsthathavehundredsofbillions basic assumption of XAI 1.0 is incomplete. Transparency
ofparameters.Second,therearegapsinethicsandrules:the alonedoesnotensuretrustworthiness,anddisclosuresthatare
legalrequirementsforexplainabilitydon’thavecleardefini- nothuman-verifiedcreateafalsetrustinflawedsystems.XAI
tions, which makes it hard to know if you’re following the 2.0emphasizesthatexplanationsmustbenotonlytechnically
rules. Third, the explainability crisis in large-scale models: sound but genuinely meaningful, persuasive, and useful to
asmodelsgetmorecomplicated,theamountofbehaviorthat end-users.
can be explained goes down. Right now, only 65% of the To provide a concise, high-level comparison of these
variance in state-of-the-art systems can be explained [93]. two paradigms, Table 8 summarizes the key differences
These problems are not separate from each other. The costs between XAI 1.0 and XAI 2.0 across technical objectives,
of computation make it hard to scale up evaluations, which evaluation practices, user involvement, security and privacy
makesitimpossibletocheckifexplanationsmeetregulatory considerations,andregulatoryalignment.
standards. Unclear laws make people less likely to spend
moneyoncostlyhuman-centeredevaluation.Theopacityof B. THEREGULATORY-TECHNICALGAP:WHENLEGAL
foundationmodelsmakesbothtechnicalmethodsandhuman REQUIREMENTSLACKOPERATIONALDEFINITIONS
understanding less effective. To deal with these problems, Beyond technical hurdles, XAI faces significant challenges
weneedtomovefromXAI1.0’sfocusonmakingexplana- aligningwithsocietalandlegalframeworks[101].
tionstoXAI2.0’sfocusonmakingexplanationsystemsthat ➢ XAI enables model bias auditing but simultaneously
are human-aligned, adversarially robust, and follow the law complicatesaccountability.Whenadiscriminatorydeci-
[94].Thissectionlooksateachchallenge,rateshowbaditis, sion occurs, determining responsibility among data
andsuggestsspecificresearchdirections.Table7talksabout providers, model developers, and deploying organiza-
theproblemsandfutureresearchdirectionsinXAI. tions presents complex challenges [102]. Section IV
demonstrated that adversarial attacks can undermine
A. THETRANSITIONFROMXAI1.0TOXAI2.0 explanationintegritythroughfairwashing,wherebiased
XAI research evolved through two successive paradigms. models generate explanations concealing discrimina-
XAI 1.0, emerging between 2015-2023, focused on tech- tion toevade regulatory oversight[66]. A creditmodel
nical transparency with a core objective of generating internally discriminating based on protected charac-
explanations for any pre-trained model [94]. Success was teristics while explaining decisions through legitimate
measured by computational metrics: fidelity to underly- factorspassesauditsrelyingonexplanation-basedover-
ing models, robustness against perturbations, and compu- sight. This creates accountability paradox: organiza-
tational efficiency. Representative methods included LIME tionsdeployingXAIforcompliancemayinadvertently
for local approximations, SHAP for game-theoretic fea- enablemoresophisticatedbiasconcealmentthanopaque
ture attribution, and Grad-CAM for visual explanations. systemswouldpermit.
VOLUME14,2026 27409

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
TABLE7. ChallengesandfutureresearchdirectionsinXAI.
➢ GDPR’s right to explanation highlights discrepancies and policymakers to establish standards that are both
between legal requirements and technical capabili- technicallyfeasibleandlegallyvalid[17].
ties[15].Noconsensusexistsonwhatconstituteslegally
sufficientexplanation,andpresentinguserswithSHAP 1) THEGDPRCOMPLIANCEPARADOX
values or heatmaps may not fulfill regulatory man- The European Union’s General Data Protection Regula-
dates for meaningful disclosure [16]. This ambiguity tion introduces transparency requirements through Articles
creates practical deployment barriers. A bank imple- 13-15 and Recital 71, mandating provision of meaningful
mentingSHAPforloanexplanationscannotdetermine informationaboutthelogicinvolvedinautomateddecision-
whether this satisfies GDPR until facing regulatory making [8]. However, translating this legal language into
scrutiny or legal challenge. The technical community technical specifications remains unresolved. Legal inter-
offers a variety of methods, such as feature attribu- pretation of GDPR requirements remains ambiguous [8],
tions, counterfactuals, attention visualizations, natural [15], while technical communities offer diverse explanation
languagesummaries,butthereisnoguidanceonwhich methods (SHAP, counterfactuals, attention visualizations)
approaches meet legal standards or under what condi- each with distinct limitations. SHAP assumes feature inde-
tions.Bridgingthisgaprequiresurgentinterdisciplinary pendence, counterfactuals may suggest infeasible changes,
collaborationamongcomputerscientists,legalscholars, andattentionmechanismssometimeshighlightnon-semantic
27410 VOLUME14,2026

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
TABLE8. ComparisonbetweenXAI1.0andXAI2.0paradigms. defensible evidence of transparency commitments should
|     |     |     |     | regulators | investigate |     | deployment |     | practices. | Without | such |
| --- | --- | --- | --- | ---------- | ----------- | --- | ---------- | --- | ---------- | ------- | ---- |
coordination,thegapbetweenlegalrequirementsandtechni-
calcapabilitieswillcontinueexpandingasmodelcomplexity
increases.
2) SCALABILITYLIMITS:WHENEXPLANATIONMETHODS
CANNOTKEEPPACEWITHMODELCOMPLEXITY
|     |     |     |     | The emergence    |              | of Transformer-based |               |             | foundation |            | models,    |
| --- | --- | --- | --- | ---------------- | ------------ | -------------------- | ------------- | ----------- | ---------- | ---------- | ---------- |
|     |     |     |     | particularly     | LLMs,        | poses                | a fundamental |             | challenge  |            | for XAI.   |
|     |     |     |     | Unlike           | conventional |                      | deep learning |             | systems    | with       | millions   |
|     |     |     |     | of parameters,   |              | contemporary         |               | foundation  | models     | operate    | at         |
|     |     |     |     | scales involving |              | hundreds             |               | of billions | of         | parameters | and        |
|     |     |     |     | are trained      | through      | large-scale          |               | pretraining |            | followed   | by task    |
|     |     |     |     | adaptation.      | As           | a result,            | explanation   |             | techniques |            | originally |
designedforsmallermodelsdonotscaleeffectivelytothese
|     |     |     |     | architectures. | This | limitation |     | is not | merely | a computational |     |
| --- | --- | --- | --- | -------------- | ---- | ---------- | --- | ------ | ------ | --------------- | --- |
bottleneckbutreflectsadeeperconceptualchallengeregard-
|     |     |     |     | ing what | interpretability |     | means | at  | extreme | model | scale. |
| --- | --- | --- | --- | -------- | ---------------- | --- | ----- | --- | ------- | ----- | ------ |
RecentmechanisticinterpretabilityeffortsonClaude3Son-
netillustrateboththepromiseandthelimitationsofcurrent
approaches.Byextractingapproximately34millioninternal
|     |     |     |     | features,   | researchers |     | were able      | to  | explain       | around        | 65% of |
| --- | --- | --- | --- | ----------- | ----------- | --- | -------------- | --- | ------------- | ------------- | ------ |
|     |     |     |     | the model’s | variance    |     | [93]. However, |     | the remaining |               | 35% of |
|     |     |     |     | unexplained | variance    |     | corresponds    | to  | internal      | computational |        |
pathwaysthatremainopaque.Thisresidualuncertaintyraises
|     |     |     |     | critical        | questions: | whether         |         | these unexplained |               | components   |          |
| --- | --- | --- | --- | --------------- | ---------- | --------------- | ------- | ----------------- | ------------- | ------------ | -------- |
|     |     |     |     | reflect learned |            | representations |         | not               | yet isolated, |              | emergent |
|     |     |     |     | behaviors       | arising    | from            | complex | parameter         |               | interactions | that     |
resistfeature-levelinterpretation,ormethodologicalartifacts
|     |     |     |     | of current | extraction |                  | techniques. |     | Until            | this ambiguity | is        |
| --- | --- | --- | --- | ---------- | ---------- | ---------------- | ----------- | --- | ---------------- | -------------- | --------- |
|     |     |     |     | resolved,  | claims     | of comprehensive |             |     | interpretability |                | for foun- |
dationmodelsremainincompleteandpotentiallymisleading,
|     |     |     |     | particularly | for | organizations |     | deploying |     | such systems | in  |
| --- | --- | --- | --- | ------------ | --- | ------------- | --- | --------- | --- | ------------ | --- |
patterns [56]. No regulatory guidance establishes which safety-critical or regulated environments. Beyond global
approaches satisfy requirements, forcing organizations to interpretability,localexplanationandreasoningtransparency
inLLMspresentevenmoreseverechallenges.Whilemodels
| choose methods | without knowing | whether they | achieve |     |     |     |     |     |     |     |     |
| -------------- | --------------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
compliance.Resolvingtheregulatory-technicalgaprequires often generate fluent chain-of-thought (CoT) explanations,
coordinatedinterdisciplinaryeffort.Computerscientistsmust recent studies indicate that these verbalized rationales fre-
developexplanationmethodswithquantifiablefidelityguar- quently fail to reflect the model’s actual decision-making
antees,computationalfeasibilityfordeploymentconstraints, process. Empirical evidence shows that LLMs may men-
and robustness against manipulation. Legal scholars need tion true causal factors only inconsistently, while omit-
to clarify what constitutes meaningful information through ting or obscuring internal reward-optimizing strategies that
analysis of emerging case law and regulatory guidance. guide predictions [103]. In many cases, models internally
Human-computer interaction researchers should systemati- rely on decision logic that diverges from the explanations
cally evaluate which explanation formats effectively com- they present, creating a dangerous illusion of transparency.
municate to different user populations. Policymakers must This discrepancy is especially problematic in high-stakes
balance transparency requirements against technical con- applications, where explanations are expected to support
straints, recognizing that some explanation demands may accountability, fairness, and regulatory compliance. Fur-
prove infeasible for complex models. Organizations imple- thermore, conventional XAI techniques struggle with the
menting XAI systems should document method selection inherentarchitecturalpropertiesofTransformer-basedmod-
rationale,validateexplanationfidelitythroughtesting,record els. Attention mechanisms, commonly used as proxies for
user comprehension results, and maintain audit trails [16], interpretability, correlate weakly with true feature impor-
[17]. This documentation demonstrates good-faith compli- tance and often highlight tokens that contribute minimally
ance efforts even as technical standards evolve, providing to final predictions while ignoring genuinely influential
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     | 27411 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
components[104].Ashighlightedinrecentanalyses,expla- the influence of projection layers and multilayer perceptron
nationfaithfulnessdeterioratesfurtherincomplexreasoning components often overshadows interpretable attention pat-
scenarios,wheremodelsmayemployinternalstrategiesthat terns. Consequently, it remains unclear whether a VLM’s
aresystematicallyabsentfromgeneratedexplanations[103]. outputisdrivenpredominantlybyvisualevidence,linguistic
This divergence between internal reasoning and external context, or spurious correlations introduced during multi-
explanation constitutes a critical safety concern: a system modalfusion.Thislimitationbecomesparticularlycriticalin
may comply superficially with explainability requirements high-stakes domains. For example, multimodal medical AI
whileinternallyoperatinginwaysthatviolateethicalorlegal systemsthatintegrateimagingdata,clinicalnotes,andstruc-
constraints.Fromapracticalstandpoint,computationalfeasi- turedpatientrecordsoutperformunimodalapproachesbyup
bilitycompoundstheseconceptualissues.Perturbation-based to6.2percentagepointsinAUC[106].Yet,withoutreliable
explanation methods, such as SHAP, become economi- explanations,practitionerscannotdeterminewhetherperfor-
cally infeasible at the foundation-model scale. Explaining mance gains stem from clinically meaningful cross-modal
a single prediction from a large LLM can require thou- reasoningorfromshortcuts,suchascorrelationsbetweentex-
sandsofGPU-hours,renderingsuchapproachesimpractical tualmetadataanddiseaseprevalence.Ashighlightedinrecent
for real-time or large-scale deployment [93]. Approximate surveysonexplainabilityforvision-languagemodels,current
methodsreducecomputationalcostbutintroduceadditional XAI techniques struggle to isolate modality-specific causal
uncertainty regarding explanation accuracy and legal suffi- contributions and to explain how intermediate fusion layers
ciency.Intheabsenceofclearregulatoryguidancedefining influencefinalpredictions[107].Althoughemergingframe-
acceptable trade-offs between explanation fidelity and effi- works attempt to combine feature attribution methods (e.g.,
ciency,organizationscannotconfidentlyassesswhethersuch SHAP), attention visualization for cross-modal alignment,
approximations meet disclosure obligations. Collectively, and concept-based explanations for semantic interpretation,
these findings demonstrate that explainability challenges in these approaches remain largely exploratory. Moreover, the
foundation models extend far beyond computational scala- absence of standardized evaluation metrics for multimodal
bility. The persistent gap between internal model behavior explanations makes it difficult to assess whether generated
and externally generated explanations—particularly in local explanations faithfully reflect underlying model reasoning
and causal reasoning contexts—suggests that existing XAI or merely provide post-hoc rationalizations. Addressing
paradigms may be fundamentally insufficient for LLMs. thesechallengeswillrequireexplanationmethodsexplicitly
Until explanation methods can reliably capture both the designedformultimodalarchitectures,alongwithevaluation
globalstructureandlocaldecisionlogicoffoundationmod- protocols capable of measuring modality dominance, cross-
els, transparency claims for large-scale AI systems should modal causality, and explanation faithfulness in complex
be regarded as aspirational rather than empirically estab- vision-languagesystems.
lished. Addressing these challenges will require not only
improved algorithms but also a rethinking of explanation
paradigms tailored specifically to the unique properties of 4) RESEARCHPRIORITIESFORXAI2.0
Transformer-basedfoundationmodels. Three research priorities emerge as critical for advancing
XAI toward deployment readiness. First, develop standard-
ized benchmarks and metrics. The absence of standard-
3) MULTIMODALEXPLAINABILITYCHALLENGES izedevaluationcreatesfragmentationpreventingmeaningful
Vision-language models (VLMs) introduce a distinct class progress [90], [91]. The research community must cre-
of explainability challenges arising from cross-modal inter- ateopen-sourcebenchmarkingplatformsincorporatingboth
actionsbetweenvisualandlinguisticrepresentations.Unlike technical and human-centered evaluation criteria. Major
unimodal systems, where explanations can be attributed to fundingorganizationsshouldestablishcoordinatedinitiatives
a single input space, VLMs require disentangling how mul- supporting creation of standardized datasets and evaluation
tiple components—namely the visual encoder, the language protocolsacrossapplicationdomains.Successwouldbeevi-
encoder, and the projection or fusion layers—jointly con- denced by adoption of these standards by more than 50%
tribute to a model’s prediction. As a result, explaining not ofXAIresearchpaperswithinthreeyears.Second,advance
onlywhatthemodelpredictsbutwhichmodalitydominates interactive and adaptive explanation systems. The transition
orinteractsinthedecision-makingprocessbecomesacentral from static, one-way explanations to dynamic, interactive
challenge.RecenttechniquessuchasCLIPSurgerydemon- systems is fundamental to XAI 2.0 [88], [94]. Future inter-
stratepartialprogressbyenablingclassactivationmapswith- faces should enable users to customize explanations, adjust
out retraining and improving mean Intersection over Union feature importance, and explore counterfactual scenarios,
from 22.11% to 35.95% [105]. However, these approaches fostering collaborative dialogue building shared human-AI
primarily emphasize alignment at the representation level understanding.Researchshouldfocusondevelopingsystems
and offer limited insight into causal modality contributions. whereexplanationsadapttouserexpertiselevelandtaskcon-
Inpractice,attention-basedvisualizationmethodsfrequently textratherthanprovidingidenticalexplanationstoallusers.
highlightnon-semantictokensorbackgroundregions,while This requires integrating insights from cognitive science
27412 VOLUME14,2026

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
about human explanation processing and human-computer limitations,ourintegratedanalysislinkingtechnicalmethod-
interaction about intuitive interface design. Third, estab- ologieswithsecurityvulnerabilities,evaluationframeworks,
lish legally sound technical standards. Bridging the gap and regulatory requirements offers perspective not yet syn-
between regulatory mandates like GDPR’s right to expla- thesizedinpriorXAIsurveys.
nation and current technical capabilities represents urgent
interdisciplinary challenge [15], [16], [17]. Future research IX. CONCLUSION
must collaborate with legal experts and policymakers to The widespread use of AI systems in important parts of
develop testable, enforceable technical standards defining society’s infrastructure made it necessary for people to be
legallysufficientexplanations.Thiscollaborationshouldpro- openandresponsible.XAIcameabouttomeetthisneedby
duce concrete guidance that organizations can follow when making the decisions of black-box models understandable
designing explanation systems for regulated applications, to people. This review looked into whether XAI has kept
specifyingwhichmethodssatisfyrequirementsunderwhich its promise. The analysis has uncovered a paradox. Even
deploymentconditions. thoughtherehavebeenalotoftechnicalimprovementsinthe
These priorities are interdependent. Standardized evalua- fieldofXAI,especiallyintheareaofexplanationgeneration,
tionenablesdeterminingwhichexplanationmethodssatisfy these improvements have not yet led to real-world success.
regulatory requirements. Interactive systems require eval- TherearethreemaingapsthatkeepAIfrombeingreliable.
uation protocols measuring whether adaptation improves First,explanationscreateattacksurfacesthatallowadversar-
user understanding. Legal standards need empirical vali- ial manipulation [13], [14], and fairwashing lets algorithms
dation through human-centered studies. Progress requires thatarebiasedgetaroundaudits.Second,evaluationpractices
coordinated effort across computer science, cognitive sci- put more weight on computational metrics than on human
ence, human-computer interaction, and legal scholarship. understanding [44], [84], which explains why deployments
XAI serves as crucial bridge toward making AI not only fail even when they do well in the lab. Third, regulatory
moreintelligentbutalsomoretransparent,accountable,and requirements don’t have clear operational definitions [15],
alignedwithhumanvalues.Whilethepathforwardpresents [16],[17],whichmakesithardforbusinessestoknowifthey
substantial challenges, the research directions articulated arefollowingtherules.Theseproblemsarenotseparate;they
here provide clear trajectory for AI to evolve from opaque areallconnected.Thehighcostofcomputationmakesithard
blackboxesintotransparent,understandable,andultimately to scale evaluations, which means that it is hard to check if
trustworthypartnersinhumandecision-making. explanationsmeetregulatoryrequirements.Legaluncertainty
deters investment in costly human-centered evaluation. The
VIII. REVIEWLIMITATIONSANDSCOPE foundationmodel’slackofclarity,with35%ofthevariance
Thiscomprehensivereviewhasimportantlimitationsreaders unexplained[93],makesbothtechnicalmethodsandhuman
shouldconsider.First,restrictingtoEnglish-languagepubli- understanding less useful. The development of reasoning
cationsmayexcludesignificantresearchcontributionsfrom models in which internal strategies deviate from generated
academiccommunitiesinnon-English-speakingregions,par- explanations in more than 97% of instances [105] indicates
ticularly China, Japan, and South Korea where AI research inherentlimitationswithinexistingexplanatoryframeworks.
prioritizesdifferentapplicationdomainsandmethodological Our study finds three important areas of research that need
approaches.Second,thedatabasesused(IEEEXplore,ACM tobefocusedon.First,createstandardizedbenchmarksthat
Digital Library, Scopus, arXiv) may systematically under- include both technical fidelity and human-centered evalua-
represent technical reports, industry white papers, preprints tioncriteria.Thiswillmakeitpossibletocomparemethods
not yet peer reviewed, and negative results showing meth- inawaythatcanberepeatedandfindoutwhichoneswork
ods failed. The field’s rapid evolution means very recent best for making decisions in different situations. Second,
breakthroughs in 2024-2025 may not yet be adequately make progress on interactive, adaptive explanation systems
indexed, though targeted arXiv searches partially address that change based on the user’s skill level and the task
this limitation. Third, the domain focus on finance, health- at hand, instead of giving the same output to everyone.
care,andcybersecurityconcentratesfindingsonsectorswith Third,worktogetheracrossdisciplinestocreatelegallysound
well-established AI adoption and clear high-stakes decision technical standards that spell out what is a good enough
contexts. Other important application areas such as legal explanation for regulatory compliance. This review shows
reasoning,educationalrecommendation,environmentalfore- that reliable AI needs more than just advanced explanation
casting, and criminal justice employ AI in fundamentally algorithms. It requires a change in thinking from XAI 1.0’s
different ways where XAI requirements differ substantially. focusonmakingexplanationstoXAI2.0’sfocusonmaking
Fourth,ourthematicanalysisprioritizesconceptualsynthesis explanation systems that are human-aligned, adversarially
over exhaustive documentation, enabling incorporation of strong, and follow the law [94]. This change needs a lot
cutting-edge research but reducing reproducibility. Finally, of work to be done in computer science, cognitive science,
XAI evolves rapidly; methods in this review may be super- human-computer interaction, and legal studies. If this inte-
seded within months as regulatory landscapes shift and grationdoesn’thappen,thegapbetweenwhatXAIpromises
foundation models create new challenges. Despite these and what it delivers will keep getting bigger as models get
VOLUME14,2026 27413

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
morecomplicatedandthestakesfordeploymentgethigher. [17] B.GoodmanandS.Flaxman,‘‘Europeanunionregulationsonalgorith-
The path forward is clear but challenging. XAI needs to micdecisionmakinganda‘righttoexplanation,’’’AIMag.,vol.38,no.3,
pp.50–57,Sep.2017.
changefromatechnicalcapabilitytoasocio-technicalsystem
[18] C.Rudin,C.Chen,Z.Chen,H.Huang,L.Semenova,andC.Zhong,
whereexplanationsclearlyhelppeoplemakebetterdecisions, ‘‘Interpretablemachinelearning:Fundamentalprinciplesand10grand
stop people from trying to trick it, and meet legal require- challenges,’’StatisticSurveys,vol.16,no.none,pp.1–85,2022.
ments. Only then can AI change from being black boxes [19] V.Chamola,V.Hassija,A.R.Sulthana,D.Ghosh,D.Dhingra,andB.
Sikdar,‘‘Areviewoftrustworthyandexplainableartificialintelligence
thatpeoplecan’tseeintopartnersinhumandecision-making
(XAI),’’IEEEAccess,vol.11,pp.78994–79015,2023.
that are clear, accountable, and ultimately trustworthy. The [20] N.Pfeuffer,L.Baum,W.Stammer,B.M.Abdel-Karim,P.Schramowski,
research directions outlined in this review offer a frame- A.M.Bucher,C.Hügel,G.Rohde,K.Kersting,andO.Hinz,‘‘Explana-
toryinteractivemachinelearning:Establishinganactiondesignresearch
work for this transformation; however, success hinges on
processformachinelearningprojects,’’Bus.Inf.Syst.Eng.,vol.65,no.6,
collaborativeeffortsacrossdisciplinesandacontinuousded- pp.677–701,Dec.2023.
icationtoprioritizingdeploymentreadinessoveralgorithmic [21] Y.Okay,M.Yildirim,andS.Ozdemir,‘‘Interpretablemachinelearning:
innovation. Acasestudyofhealthcare,’’inProc.Int.Symp.Netw.,Comput.Commun.
(ISNCC),Oct.2021,pp.1–6.
[22] Y.S.HengandP.Subramanian,‘‘Asystematicreviewofmachinelearning
REFERENCES andexplainableartificialintelligence(XAI)increditriskmodelling,’’in
Proc.FutureTechnol.Conf.,2022,pp.596–614.
[1] S.AlandS.Sağiroğlu,‘‘Areviewofexplainableartificialintelligence,’’
[23] R.-K. Sheu and M. S. Pardeshi, ‘‘A survey on medical explainable
inProc.9thInt.Conf.Comput.Sci.Eng.(UBMK),2023,pp.310–315.
AI (XAI): Recent progress, explainability approach, human inter-
[2] M. Fontes, J. D. S. De Almeida, and A. Cunha, ‘‘Application of
action and scoring system,’’ Sensors, vol. 22, no. 20, p. 8068,
example-basedexplainableartificialintelligence(XAI)foranalysisand
Oct.2022.
interpretationofmedicalimaging:Asystematicreview,’’IEEEAccess,
[24] F.Sovrano,‘‘LegalXAI:Asystematicreviewandinterdisciplinarymap-
vol.12,pp.26419–26427,2024.
pingofXAIandEUlaw,towardsaresearchagendaforlegallyresponsible
[3] V.Buhrmester,D.Münch,andM.Arens,‘‘Analysisofexplainersofblack
AI,’’TowardsRes.AgendaLegallyResponsibleAI,Jul.2025.[Online].
boxdeepneuralnetworksforcomputervision:Asurvey,’’Mach.Learn.
Available:https://ssrn.com/abstract=5371124
Knowl.Extraction,vol.3,no.4,pp.966–989,Dec.2021.
[25] W.Pedrycz,‘‘Design,interpretability,andexplainabilityofmodelsinthe
[4] A. Adadi and M. Berrada, ‘‘Peeking inside the black-box: A sur-
frameworkofgranularcomputingandfederatedlearning,’’inProc.IEEE
veyonexplainableartificialintelligence(XAI),’’IEEEAccess,vol.6,
Conf.NorbertWiener21stCentury(21CW),Chennai,India,Jul.2021,
pp.52138–52160,2018.
pp.1–6.
[5] E.S.Ortigossa,T.Gonçalves,andL.G.Nonato,‘‘EXplainableartificial
[26] G.SchwalbeandB.Finzel,‘‘Acomprehensivetaxonomyforexplainable
intelligence (XAI)—From theory to methods and applications,’’IEEE
artificialintelligence:Asystematicsurveyofsurveysonmethodsand
Access,vol.12,pp.80799–80846,2024.
concepts,’’DataMin.Knowl.Disc.,vol.38,no.5,pp.3043–3101,2023.
[6] S.Sutthithatip,S.Perinpanayagam,andS.Aslam,‘‘(Explainable)arti-
[27] M.R.Islam,‘‘Acomprehensivesurveyofexplainableartificialintelli-
ficialintelligenceinaerospacesafety-criticalsystems,’’inProc.IEEE
gence(XAI):Ahuman-centeredperspective,’’IEEETrans.Computat.
Aerosp.Conf.(AERO),BigSky,MT,USA,Mar.2022,pp.1–12.
SocialSyst.,vol.9,no.4,pp.1149–1166,Aug.2022.
[7] A. Kuznietsov, B. Gyevnar, C. Wang, S. Peters, and S. V. Albrecht,
[28] D.OrekiandM.P.Lukinec,‘‘Evaluationofexplainableartificialintel-
‘‘ExplainableAIforsafeandtrustworthyautonomousdriving:Asys-
ligenceforpredictiveprocessminingineducation,’’WSEASTrans.Adv.
tematic review,’’ IEEE Trans. Intell. Transp. Syst., vol. 25, no. 12,
Eng.Educ.,vol.22,pp.1–8,Apr.2025.
pp.19342–19364,Dec.2024.
[8] L.EdwardsandM.Veale,‘‘Enslavingthealgorithm:Fromarighttoan [29] K.SokolandP.Flach,‘‘Explainabilityfactsheets:Aframeworkforsys-
explanationtoa‘righttobetterdecisions?’’’IEEESecur.Privacy,vol.16, tematicassessmentofexplainableapproaches,’’inProc.Conf.Fairness,
no.3,pp.46–54,May2018. Accountability,Transparency,Jan.2020,pp.56–67.
[9] D.Gunning,M.Stefik,J.Choi,T.Miller,S.Stumpf,andG.-Z.Yang, [30] N.BarrKumarakulasinghe,T.Blomberg,J.Liu,A.SaraivaLeao,and
‘‘XAI-explainable artificial intelligence,’’ Sci. Robot., vol. 4, no. 26, P.Papapetrou,‘‘Evaluatinglocalinterpretablemodel-agnosticexplana-
p.7120,May2019. tionsonclinicalmachinelearningclassificationmodels,’’inProc.IEEE
33rdInt.Symp.Computer-BasedMed.Syst.(CBMS),Rochester,MN,
[10] A. B. Arrieta, N. Díaz-Rodríguez, J. D. Ser, A. Bennetot, S. Tabik,
USA,Jul.2020,pp.7–12.
A.Barbado,S.García,S.Gil-López,D.Molina,R.Benjamins,R.Chatila,
and F. Herrera, ‘‘Explainable artificial intelligence (XAI): Concepts, [31] F. S. Khan, S. S. Mazhar, K. Mazhar, D. A. AlSaleh, and A.
taxonomies,opportunitiesandchallengestowardresponsibleAI,’’Inf. Mazhar,‘‘Model-agnosticexplainableartificialintelligencemethodsin
Fusion,vol.58,pp.82–115,Jun.2019. finance: A systematic review, recent developments, limitations, chal-
[11] A. Rawal, J. McCoy, D. B. Rawat, B. M. Sadler, and R. S. Amant, lengesandfuturedirections,’’Artif.Intell.Rev.,vol.58,no.8,p.232,
‘‘Recentadvancesintrustworthyexplainableartificialintelligence:Sta- May2025.
tus,challenges,andperspectives,’’IEEETrans.Artif.Intell.,vol.3,no.6, [32] K.Devireddy,‘‘AcomparativestudyofexplainableAImethods:Model-
pp.852–866,Dec.2022. agnosticvs.model-specificapproaches,’’2025,arXiv:2504.04276.
[12] W. Yang, Y. Wei, H. Wei, Y. Chen, G. Huang, X. Li, R. Li, N. Yao, [33] A.Ghorbani,A.Abid,andJ.Zou,‘‘Interpretationofneuralnetworksis
X.Wang,X.Gu,M.B.Amin,andB.Kang,‘‘SurveyonexplainableAI: fragile,’’inProc.AAAIConf.Artif.Intell.,2017,pp.3681–3688.
Fromapproaches,limitationsandapplicationsaspects,’’Hum.-Centric [34] Z.Zhang,L.Yilmaz,andB.Liu,‘‘Acriticalreviewofinductivelogic
Intell.Syst.,vol.3,no.3,pp.161–188,Aug.2023. programmingtechniquesforexplainableAI,’’IEEETrans.NeuralNetw.
[13] D.Slack,S.Hilgard,E.Jia,S.Singh,andH.Lakkaraju,‘‘FoolingLIME Learn.Syst.,vol.35,no.8,pp.10220–10236,Aug.2024.
and SHAP: Adversarial attacks on post hoc explanation methods,’’ in [35] U.Schlegel,D.V.Lam,D.A.Keim,andD.Seebacher,‘‘TS-MULE:
Proc.AAAI/ACMConf.AI,Ethics,Soc.,Feb.2020,pp.180–186. Localinterpretablemodel-agnosticexplanationsfortimeseriesforecast
[14] X.Zhang,N.Wang,H.Shen,S.Ji,X.Luo,andT.Wang,‘‘Interpretable models,’’ in Proc. Joint Eur. Conf. Mach. Learn. Knowl. Discovery
deeplearningunderfire,’’inProc.29thSecur.Symp.,2018,pp.1–18. Databases,2021,pp.5–14.
[15] S.Atakishiyev,M.Salameh,H.Yao,andR.Goebel,‘‘Explainablearti- [36] K.Kalasampath,K.N.Spoorthi,S.Sajeev,S.Kuppa,K.Ajay,andM.
ficialintelligenceforautonomousdriving:Acomprehensiveoverview Angulakshmi,‘‘Aliteraturereviewonapplicationsofexplainableartifi-
and field guide for future research directions,’’ IEEE Access, vol. 12, cialintelligence(XAI),’’IEEEAccess,vol.13,pp.41111–41140,2025.
pp.101603–101625,2024. [37] P. Rasouli and I. C. Yu, ‘‘Analyzing and improving the robustness of
[16] K.WulffandH.Finnestrand,‘‘Creatingmeaningfulworkintheageof tabularclassifiersusingcounterfactualexplanations,’’inProc.20thIEEE
AI:ExplainableAI,explainability,andwhyitmatterstoorganizational Int.Conf.Mach.Learn.Appl.(ICMLA),Pasadena,CA,USA,Dec.2021,
designers,’’AISoc.,vol.39,no.4,pp.1843–1856,Aug.2024. pp.1286–1293.
27414 VOLUME14,2026

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
[38] S.M.Lundberg,G.Erion,H.Chen,A.DeGrave,J.M.Prutkin,B.Nair, [58] C. Düsing, P. Cimiano, S. Rehberg, C. Scherer, O. Kaup, C. Köster,
R.Katz,J.Himmelfarb,N.Bansal,andS.-I.Lee,‘‘Fromlocalexpla- S.Hellmich,D.Herrmann,K.L.Meier,S.Claßen,andR.Borgstedt,
nationstoglobalunderstandingwithexplainableAIfortrees,’’Nature ‘‘Integratingfederatedlearningforimprovedcounterfactualexplanations
Mach.Intell.,vol.2,no.1,pp.56–67,Jan.2020. inclinicaldecisionsupportsystemsforsepsistherapy,’’Artif.Intell.Med.,
[39] K.Aas,M.Jullum,andA.Løland,‘‘Explainingindividualpredictions vol.157,Nov.2024,Art.no.102982.
whenfeaturesaredependent:MoreaccurateapproximationstoShapley [59] G.Rjoub,J.Bentahar,O.A.Wahab,R.Mizouni,A.Song,R.Cohen,
values,’’Artif.Intell.,vol.298,Sep.2021,Art.no.103502. H.Otrok,andA.Mourad,‘‘Asurveyonexplainableartificialintelligence
[40] A.DiMarino,V.Bevilacqua,A.Ciaramella,I.DeFalco,andG.San- forcybersecurity,’’IEEETrans.Netw.ServiceManage.,vol.20,no.4,
nino,‘‘Ante-hocmethodsforinterpretabledeepmodels:Asurvey,’’ACM pp.5115–5140,Dec.2023.
Comput.Surveys,vol.57,no.10,pp.1–36,Oct.2025. [60] K. Cherukuri, ‘‘Artificial intelligence-based approaches for anomaly
[41] C.Rudin,‘‘Stopexplainingblackboxmachinelearningmodelsforhigh detection,’’inEncryptedNetworkTrafficAnalysis.Cham,Switzerland:
stakes decisions and use interpretable models instead,’’ Nature Mach. Springer,2024,pp.73–99.
Intell.,vol.1,no.5,pp.206–215,May2019. [61] W. Liu, F. Zhao, L. Nkenyereye, S. Rani, K. Li, and J. Lv, ‘‘XAI
[42] R.Mochaourab,A.Venkitaraman,I.Samsten,P.Papapetrou,andC.R. drivenintelligentIoMTsecuredatamanagementframework,’’IEEEJ.
Rojas,‘‘Posthocexplainabilityfortimeseriesclassification:Towarda Biomed.HealthInformat.,vol.30,no.2,pp.935–946,Feb.2025,doi:
signalprocessingperspective,’’IEEESignalProcess.Mag.,vol.39,no.4, 10.1109/JBHI.2024.3408215.
pp.119–129,Jul.2022. [62] Y.Rong,T.Leemann,T.-T.Nguyen,L.Fiedler,P.Qian,V.Unhelkar,T.
[43] D.Bhati,M.Amiruzzaman,Y.Zhao,A.Guercio,andT.-L.Le,‘‘Asurvey Seidel,G.Kasneci,andE.Kasneci,‘‘Towardshuman-centeredexplain-
ofpost-hocXAImethodsfromavisualizationperspective:Challenges ableAI:Asurveyofuserstudiesformodelexplanations,’’IEEETrans.
andopportunities,’’IEEEAccess,vol.13,pp.120785–120806,2025. PatternAnal.Mach.Intell.,vol.46,no.4,pp.2104–2122,Apr.2024.
[44] M. A. K. Akhtar, M. Kumar, and A. Nayyar, ‘‘The role of human- [63] R. Mandava, S. S. Vellela, S. Gorintla, L. Dalavai, N. Malathi, and
centereddesignindevelopingexplainableAI,’’inTowardsEthicaland K.Haritha,‘‘EvaluatingtheimpactofexplainableAIonusertrustin
Socially Responsible Explainable AI: Challenges and Opportunities. financialdecision-supportsystems,’’inProc.Int.Conf.Comput.Robot.,
Cham,Switzerland:Springer,2024. Test.Eng.Eval.(ICCRTEE),Virudhunagar,India,May2025,pp.1–6.
[45] J.CernevicienandK.Audrius,‘‘Explainableartificialintelligence(XAI) [64] T.MillerandZ.Jing,‘‘Explanationinartificialintelligence:Insightsfrom
in finance: A systematic literature review,’’ Artif. Intell. Rev., vol. 57, thesocialsciences,’’DigitalHumanitiesResearch,vol.4,no.2,p.90,
no.8,p.216,Jul.2024. 2024.
[46] Q.Xu,Y.Liao,Q.Li,J.Zhang,Z.Song,L.Wang,andX.Yuan,‘‘SHAP- [65] S. Tasneem and K. A. Islam, ‘‘Improve adversarial robustness of AI
basedinterpretablemodelsforcreditdefaultassessmentusingmachine models in remote sensing via data-augmentation and explainable-AI
learning,’’inProc.14thInt.Conf.Softw.Technol.Eng.(ICSTE),Macau, methods,’’RemoteSens.,vol.16,no.17,p.3210,Aug.2024.
Aug.2024,pp.213–217. [66] U.Aïvodji,‘‘Fairwashing:Theriskofrationalization,’’inProc.Int.Conf.
[47] M. K. Nallakaruppan, B. Balusamy, M. L. Shri, V. Malathi, and S. Mach.Learn.,2019,pp.161–170.
Bhattacharyya,‘‘AnexplainableAIframeworkforcreditevaluationand [67] C.ThamesandY.Sun,‘‘Asurveyofartificialintelligenceapproachesto
analysis,’’Appl.SoftComput.,vol.153,Mar.2024,Art.no.111307. safetyandmission-criticalsystems,’’inProc.Integr.Commun.,Navigat.
[48] N. Capuano, G. Fenza, V. Loia, and C. Stanzione, ‘‘Explainable arti- Surveill.Conf.(ICNS),Herndon,VA,USA,Apr.2024,pp.1–12.
ficialintelligenceinCyberSecurity:Asurvey,’’IEEEAccess,vol.10, [68] J.Wei,H.Turbé,andG.Mengaldo,‘‘Revisitingtherobustnessofpost-
pp.93575–93600,2022. hocinterpretabilitymethods,’’2024,arXiv:2407.19683.
[49] R.Kapale,P.Deshpande,S.Shukla,S.Kediya,Y.Pethe,andS.Metre, [69] I.E.Nielsen,D.Dera,G.Rasool,R.P.Ramachandran,andN.C.Bouay-
‘‘ExplainableAIforfrauddetection:Enhancingtransparencyandtrustin naya, ‘‘Robust explainability: A tutorial on gradient-based attribution
financialdecision-making,’’inProc.2ndDMIHERInt.Conf.Artif.Intell. methodsfordeepneuralnetworks,’’IEEESignalProcess.Mag.,vol.39,
Healthcare,Educ.Ind.(IDICAIEI),Wardha,India,Nov.2024,pp.1–6. no.4,pp.73–84,Jul.2022.
[50] D.K.J.B.Saini,N.Shelke,S.N.Prajwalasimha,A.Pimpalkar,G.H. [70] H.Jin,A.Xue,W.You,S.Goel,andE.Wong,‘‘Probabilisticstability
Kumar, and L. Monish, ‘‘Advanced deep learning for real-time fraud guaranteesforfeatureattributions,’’2025,arXiv:2504.13787.
detection in banking: Scalable and high-accuracy solutions,’’ in Proc. [71] I. Vaccari, A. Carlevaro, S. Narteni, E. Cambiaso, and M. Mongelli,
6thInt.Conf.Emerg.Technol.(INCET),BELGAUM,India,May2025, ‘‘Explainableandreliableagainstadversarialmachinelearningindata
pp.1–6. analytics,’’IEEEAccess,vol.10,pp.83949–83970,2022.
[51] B. H. A. Khattak, I. Shafi, A. S. Khan, E. S. Flores, R. G. Lara, [72] A.Hedström,L.Weber,S.Lapuschkin,andM.Höhne,‘‘Afreshlookat
M.A.Samad,andI.Ashraf,‘‘AsystematicsurveyofAImodelsinfinan- sanitychecksforsaliencymaps,’’inProc.WorldConf.ExplainableArtif.
cialmarketforecastingforprofitabilityanalysis,’’IEEEAccess,vol.11, Intell.,2024,pp.403–420.
pp.125359–125380,2023. [73] J.-H.SimandH.-M.Song,‘‘Ageneralizedframeworkforadversarial
[52] S.Bharati,M.R.H.Mondal,andP.Podder,‘‘Areviewonexplainable attack detection and prevention using grad-CAM and clustering tech-
artificialintelligenceforhealthcare:Why,how,andwhen?’’IEEETrans. niques,’’Systems,vol.13,no.2,p.88,Jan.2025.
Artif.Intell.,vol.5,no.4,pp.1429–1442,Apr.2024. [74] Z. Zhang, H. A. Hamadi, E. Damiani, C. Y. Yeun, and F. Taher,
[53] H.C.YoonandL.P.Lin,‘‘BraintumorclassificationinMRI:Insights ‘‘Explainableartificialintelligenceapplicationsincybersecurity:State-
fromLIMEandgrad-CAMexplainableAItechniques,’’IEEEAccess, of-the-art in research,’’ IEEE Access, vol. 10, pp. 93104–93139,
vol.13,pp.154172–154202,2025. 2022.
[54] D.Bhati,F.Neha,andM.Amiruzzaman,‘‘Asurveyonexplainablearti- [75] A. Zahid, ‘‘Explainability, robustness, and fairness in user-centric
ficialintelligence(XAI)techniquesforvisualizingdeeplearningmodels intelligent systems: A systematic review,’’ IEEE Trans. Emerg. Top-
inmedicalimaging,’’J.Imag.,vol.10,no.10,p.239,Sep.2024. ics Comput. Intell., vol. 9, no. 6, pp. 3728–3753, Jul. 2025, doi:
[55] S.Durgaraju,D.V.T.Vel,andH.Madathala,‘‘Transforminghealthcare 10.1109/TETCI.2025.3567604.
diagnostics:Acomprehensivereviewofconvolutionalneuralnetworksin [76] A.KuppaandN.-A.Le-Khac,‘‘Blackboxattacksonexplainableartificial
medicalimaginganddiseaseprediction,’’inProc.6thInt.Conf.Mobile intelligence(XAI)methodsincybersecurity,’’inProc.Int.JointConf.
Comput. Sustain. Informat. (ICMCSI), Goathgaun, Nepal, Jan. 2025, NeuralNetw.(IJCNN),Jul.2020,pp.1–8.
pp.1167–1174. [77] Leofante and M. Wicker, Robust Explainable AI. Cham, Switzerland:
[56] Q.Abbas,W.Jeong,andS.W.Lee,‘‘ExplainableAIinclinicaldecision Springer,2025.
supportsystems:Ameta-analysisofmethods,applications,andusability [78] S.Naveed,G.Stevens,andD.Robin-Kern,‘‘Anoverviewoftheempir-
challenges,’’Healthcare,vol.13,no.17,p.2154,Aug.2025. icalevaluationofexplainableAI(XAI):Acomprehensiveguidelinefor
[57] Q.Xu,W.Xie,B.Liao,C.Hu,L.Qin,Z.Yang,H.Xiong,Y.Lyu,Y.Zhou, user-centeredevaluationinXAI,’’Appl.Sci.,vol.14,no.23,p.11288,
andA.Luo,‘‘Interpretabilityofclinicaldecisionsupportsystemsbased Dec.2024.
on artificial intelligence from technological and medical perspective: [79] S.AlhasanandR.Alnanih,‘‘EnhancingAIexplainabilitythroughthe
Asystematicreview,’’J.HealthcareEng.,vol.2023,no.1,Jan.2023, EXACT framework: A user-centric approach,’’ IEEE Access, vol. 13,
Art.no.9919269. pp.98208–98228,2025.
VOLUME14,2026 27415

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
[80] F.Poursabzi-Sangdeh,D.G.Goldstein,J.M.Hofman,J.W.Wortman [101] O.S.Owolabi,P.C.Uche,N.T.Adeniken,C.Ihejirika,R.B.Islam,
Vaughan,andH.Wallach,‘‘Manipulatingandmeasuringmodelinter- andB.J.T.Chhetri,‘‘Ethicalimplicationofartificialintelligence(AI)
pretability,’’inProc.CHIConf.Hum.FactorsComput.Syst.,May2021, adoptioninfinancialdecisionmaking,’’Comput.Inf.Sci.,vol.17,no.1,
pp.1–52. p.49,Apr.2024.
[81] E.D.Okonta,F.O.Okeke,E.E.Mgbemena,R.C.Nnaemeka-Okeke,S. [102] Z.AtfandP.R.Lewis,‘‘IstrustcorrelatedwithexplainabilityinAI?A
Guo,F.C.Awe,andC.Eke,‘‘Anintelligentnaturallanguageprocess- meta-analysis,’’IEEETrans.Technol.Soc.,earlyaccess,Apr.14,2025,
ing(NLP)workflowforautomatedsmartbuildingdesign,’’Buildings, doi:10.1109/TTS.2025.3558448.
vol.15,no.14,p.2413,Jul.2025. [103] S.Atakishiyev,H.K.B.Babiker,J.Dai,N.Farruque,T.Hayashi,N.
[82] R. Confalonieri and J. M. Alonso-Moral, ‘‘An operational framework Sadaf Hriti, M. Abed Rahman, I. Smith, M.-Y. Kim, O. R. Zaïane,
forguidinghumanevaluationinexplainableandtrustworthyartificial and R. Goebel, ‘‘Explainability of large language models: Opportuni-
intelligence,’’IEEEIntell.Syst.,vol.39,no.1,pp.18–28,Jan.2024. tiesandchallengestowardgeneratingtrustworthyexplanations,’’2025,
[83] E.Mariotti,A.Arias-Duart,M.Cafagna,A.Gatt,D.Garcia-Gasulla,and arXiv:2510.17256.
J.M.Alonso-Moral,‘‘TextFocus:Assessingthefaithfulnessoffeature [104] S.JainandB.C.Wallace,‘‘Attentionisnotexplanation,’’inProc.Conf.
attributionmethodsexplanationsinnaturallanguageprocessing,’’IEEE NorthAmer.ChapterAssoc.Comput.Linguistics,Hum.Lang.Technol.
Access,vol.12,pp.138870–138880,2024. (NAACL-HLT),2019,pp.3543–3556.
[84] M.A.Kadir,A.Mosavi,andD.Sonntag,‘‘EvaluationmetricsforXAI: [105] Anthropic. (Apr. 2025). Reasoning Models Don’t Always Say What
Areview,taxonomy,andpracticalapplications,’’inProc.IEEE27thInt. They Think. [Online]. Available: https://www.anthropic.com/research/
Conf.Intell.Eng.Syst.(INES),Nairobi,Kenya,Jul.2023,pp.000111– reasoning-models-dont-say-think
000124. [106] A.PahuddeMortanges,H.Luo,S.Z.Shu,A.Kamath,Y.Suter,M.
[85] K.Ong,R.Mao,D.Varshney,P.PuLiang,E.Cambria,andG.Mengaldo, Shelan,A.Pöllinger,andM.Reyes,‘‘Orchestratingexplainableartificial
‘‘Derivingstrategicmarketinsightswithlargelanguagemodels:Abench- intelligenceformultimodalandlongitudinaldatainmedicalimaging,’’
markforforwardcounterfactualgeneration,’’2025,arXiv:2505.19430. npjDigit.Med.,vol.7,no.1,p.195,Jul.2024.
[86] S.Sithakoul,S.Meftah,andC.Feutry,‘‘BEExAI:Benchmarktoevaluate [107] D.Shu,H.Zhao,J.Hu,W.Liu,A.Payani,L.Cheng,andM.Du,‘‘Large
explainableAI,’’inProc.WorldConf.ExplainableArtif.Intell.,2024, vision-languagemodelalignmentandmisalignment:Asurveythrough
pp.445–468. thelensofexplainability,’’inProc.FindingsAssoc.Comput.Linguistics:
EMNLP,Suzhou,China,2025,pp.1713–1735.
[87] S.Roy,G.Laberge,B.Roy,F.Khomh,A.Nikanjam,andS.Mondal,
[108] F. M. Talaat, A. Aljadani, M. Badawy, and M. Elhosseini, ‘‘Toward
‘‘WhyDon’tXAItechniquesagree?Characterizingthedisagreements
interpretablecreditscoring:Integratingexplainableartificialintelligence
betweenpost-hocexplanationsofdefectpredictions,’’inProc.IEEEInt.
withdeeplearningforcreditcarddefaultprediction,’’NeuralComput.
Conf.Softw.MaintenanceEvol.(ICSME),Limassol,Cyprus,Oct.2022,
Appl.,vol.36,no.9,pp.4847–4865,Mar.2024.
pp.444–448.
[109] S.Gite,H.Khatavkar,K.Kotecha,S.Srivastava,P.Maheshwari,and
[88] A.Gambetti,Q.Han,H.Shen,andC.Soares,‘‘Asurveyonhuman-
N. Pandey, ‘‘Explainable stock prices prediction from financial news
centeredevaluationofexplainableAImethodsinclinicaldecisionsupport
articlesusingsentimentanalysis,’’PeerJComput.Sci.,vol.7,p.e340,
systems,’’2025,arXiv:2502.09849.
Jan.2021.
[89] A.Jacovi,A.Marasovic,T.Miller,andY.Goldberg,‘‘Formalizingtrust
[110] B.Lim,S.Ö.Arık,N.Loeff,andT.Pfister,‘‘Temporalfusiontrans-
inartificialintelligence:Prerequisites,causesandgoalsofhumantrustin
formersforinterpretablemulti-horizontimeseriesforecasting,’’Int.J.
AI,’’inProc.ACMConf.Fairness,Accountability,Transparency,2021,
Forecasting,vol.37,no.4,pp.1748–1764,Oct.2021.
pp.624–635.
[111] J.Jiménez-Luna,F.Grisoni,andG.Schneider,‘‘Drugdiscoverywith
[90] E. Tjoa and C. Guan, ‘‘A survey on explainable artificial intelligence
explainableartificialintelligence,’’NatureMach.Intell.,vol.2,no.10,
(XAI):TowardmedicalXAI,’’IEEETrans.NeuralNetw.Learn.Syst.,
pp.573–584,Oct.2020.
vol.32,no.11,pp.4793–4813,Nov.2021.
[112] Z. Wu, J. Wang, H. Du, D. Jiang, Y. Kang, D. Li, P. Pan, Y. Deng,
[91] W. Saeed and C. Omlin, ‘‘Explainable AI (XAI): A systematic meta-
D.Cao,C.-Y.Hsieh,andT.Hou,‘‘Chemistry-intuitiveexplanationof
surveyofcurrentchallengesandfutureopportunities,’’Knowledge-Based
graphneuralnetworksformolecularpropertypredictionwithsubstruc-
Syst.,vol.263,Mar.2023,Art.no.110273.
turemasking,’’NatureCommun.,vol.14,no.1,pp.1–15,May2023.
[92] V.L.KalmykovandL.V.Kalmykov,‘‘Towardsexplicitlyexplainable
[113] M. Proietti, A. Ragno, B. L. Rosa, R. Ragno, and R. Capobianco,
artificialintelligence,’’Inf.Fusion,vol.123,Nov.2025,Art.no.103352.
‘‘Explainable AI in drug discovery: Self-interpretable graph
[93] Anthropic. (May 2024). Scaling Monosemanticity: Extracting neural network for molecular property prediction using concept
Interpretable Features From Claude 3 Sonnet. [Online]. Available: whitening,’’ Mach. Learn., vol. 113, no. 4, pp. 2013–2044,
https://transformer-circuits.pub/2024/scaling-monosemanticity/ Apr.2024.
[94] L.Longo,M.Brčić,F.Cabitza,J.Choi,R.Confalonieri,J.D.Ser,R. [114] M.SaiedandS.Guirguis,‘‘Explainableartificialintelligenceforbotnet
Guidotti,Y.Hayashi,F.Herrera,A.Holzinger,R.Jiang,H.Khosravi,F. detection in Internet of Things,’’ Sci. Rep., vol. 15, no. 1, pp. 1–17,
Lécué,G.Malgieri,A.Páez,W.Samek,J.Schneider,T.Speith,andS. Mar.2025.
Stumpf,‘‘Explainableartificialintelligence(XAI)2.0:Amanifestoof [115] S.Milli,L.Schmidt,A.D.Dragan,andM.Hardt,‘‘Modelreconstruc-
openchallengesandinterdisciplinaryresearchdirections,’’Inf.Fusion, tionfrommodelexplanations,’’inProc.Conf.Fairness,Accountability,
vol.106,Jun.2024,Art.no.102301. Transparency,Jan.2019,pp.1–9.
[95] A.A.Noor,A.Manzoor,M.D.MazharQureshi,M.A.Qureshi,andW. [116] R. Shokri, M. Strobel, and Y. Zick, ‘‘On the privacy risks of model
Rashwan,‘‘UnveilingexplainableAIinhealthcare:Currenttrends,chal- explanations,’’ in Proc. AAAI/ACM Conf. AI, Ethics, Soc., Jul. 2021,
lenges,andfuturedirections,’’WIREsDataMiningKnowl.Discovery, pp.231–241.
vol.15,no.2,p.70018,Jun.2025.
[117] H.Liu,Y.Wu,Z.Yu,andN.Zhang,‘‘Pleasetellmemore:Privacyimpact
[96] S.N.Saw,Y.Y.Yan,andK.H.Ng,‘‘Currentstatusandfuturedirections ofexplainabilitythroughthelensofmembershipinferenceattack,’’in
ofexplainableartificialintelligenceinmedicalimaging,’’Eur.J.Radiol., Proc.IEEESymp.Secur.Privacy(SP),May2024,pp.4791–4809.
vol.183,Feb.2025,Art.no.111884. [118] Z. Buçinca, M. B. Malaya, and K. Z. Gajos, ‘‘To trust or to think:
[97] M.Pawlicki,A.Pawlicka,R.Kozik,andM.Choraś,‘‘Thesurveyonthe CognitiveforcingfunctionscanreduceoverrelianceonAIinAI-assisted
dualnatureofxAIchallengesinintrusiondetectionandtheirpotentialfor decision-making,’’ ACM Hum.-Comput. Interact., vol. 5, pp. 1–21,
AIinnovation,’’Artif.Intell.Rev.,vol.57,no.12,p.330,Oct.2024. Apr.2021.
[98] Y.-L. Chou, C. Moreira, P. Bruza, C. Ouyang, and J. Jorge, ‘‘Coun- [119] G.Bansal,T.Wu,J.Zhou,R.Fok,B.Nushi,E.Kamar,M.T.Ribeiro,
terfactualsandcausabilityinexplainableartificialintelligence:Theory, andD.Weld,‘‘Doesthewholeexceeditsparts?TheeffectofAIexplana-
algorithms,andapplications,’’Inf.Fusion,vol.81,pp.59–83,May2021. tionsoncomplementaryteamperformance,’’inProc.CHIConf.Human
[99] R.O.Weber,A.J.Johs,P.Goel,andJ.M.Silva,‘‘XAIisintrouble,’’AI FactorsComput.Syst.,May2021,pp.1–16.
Mag.,vol.45,no.3,pp.300–316,Sep.2024. [120] H.Vasconcelos,M.Jörke,M.Grunde-Mclaughlin,T.Gerstenberg,M.S.
[100] Umm-E-HabibaandK.M.Habibullah,‘‘ExplainableAI:Adiversestake- Bernstein,andR.Krishna,‘‘ExplanationscanreduceoverrelianceonAI
holderperspective,’’inProc.IEEE32ndInt.RequirementsEng.Conf. systemsduringdecision-making,’’Proc.ACMHum.-Comput.Interact.,
(RE),Reykjavik,Iceland,Jun.2024,pp.494–495. vol.7,no.CSCW1,pp.1–38,Apr.2023.
27416 VOLUME14,2026

O.Kayaetal.:XAI:Concepts,Applications,Challenges,andFuturePerspectives
[121] Y. Xuan, E. Small, K. Sokol, D. Hettiachchi, and M. Sanderson, MUHAMMETALIKARABULUT(SeniorMem-
‘‘Comprehensionisadouble-edgedsword:Over-interpretingunspecified ber,IEEE)receivedtheB.Sc.degreeinelectrical
informationinintelligiblemachinelearningexplanations,’’Int.J.Hum.- andelectronicsengineeringfromMustafaKemal
Comput.Stud.,vol.193,Jan.2025,Art.no.103376. University,Hatay,Türkiye,in2010,andtheM.Sc.
[122] R.Müller,‘‘HowexplainableAIaffectshumanperformance:Asystem- andPh.D.degreesinelectronicsandcommunica-
aticreviewofthebehaviouralconsequencesofsaliencymaps,’’Int.J.
tionengineeringfromYildizTechnicalUniversity,
Human–ComputerInteract.,vol.41,no.4,pp.2020–2051,Feb.2025.
Istanbul,Türkiye,in2015and2021,respectively.
| [123] G. Nguyen, | D.  | Kim, | and A. Nguyen, | ‘‘The effectiveness | of  | feature |     |     |     |     |     |     |     |
| ---------------- | --- | ---- | -------------- | ------------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
HewasaResearchandTeachingAssistantwiththe
attributionmethodsanditscorrelationwithautomaticevaluationscores,’’
|     |     |     |     |     |     |     |     |     | Department | of  | Electronics | and | Communication |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | --- | ------------- |
inProc.Adv.NeuralInf.Process.Syst.,vol.34,2021,pp.26422–26436.
[124] B.Zhou,A.Khosla,A.Lapedriza,A.Oliva,andA.Torralba,‘‘Learning Engineering, Yildiz Technical University, from
|     |     |     |     |     |     |     | 2013 and 2021. | He  | was an Assistant | Professor |     | with Kafkas | University |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | --------- | --- | ----------- | ---------- |
deepfeaturesfordiscriminativelocalization,’’inProc.IEEEConf.Com-
|     |     |     |     |     |     |     | from 2022 | and 2024. | Since 2024, | he  | has been | an Associate | Profes- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ----------- | --- | -------- | ------------ | ------- |
put.Vis.PatternRecognit.(CVPR),Jun.2016,pp.2921–2929.
|                 |     |            |         |                     |        |           | sor with the | Department | of Electronics |     | Engineering, | Turkish | Air Force |
| --------------- | --- | ---------- | ------- | ------------------- | ------ | --------- | ------------ | ---------- | -------------- | --- | ------------ | ------- | --------- |
| [125] J. Zhang, | S.  | A. Bargal, | Z. Lin, | J. Brandt, X. Shen, | and S. | Sclaroff, |              |            |                |     |              |         |           |
Academy,NationalDefenseUniversity,Türkiye,andaResearcherwiththe
‘‘Top-downneuralattentionbyexcitationbackprop,’’Int.J.Comput.Vis.,
AIandNext-GenerationWirelessCommunicationLaboratory(ANWCL).
vol.126,no.10,pp.1084–1102,Oct.2018.
[126] V.Petsiuk,A.Das,andK.Saenko,‘‘RISE:Randomizedinputsampling Hisresearchinterestsincludedigitalcommunication,cooperativecommuni-
forexplanationofblack-boxmodels,’’2018,arXiv:1806.07421. cation,MACprotocolsforvehicularadhocnetworks,UAVcommunication,
[127] L.-V.Herm,‘‘ImpactofexplainableAIoncognitiveload:Insightsfrom andartificialintelligence.
anempiricalstudy,’’2023,arXiv:2304.08861.
[128] D.Gunning,etal.,‘‘DARPA’sexplainableAI,XAIprogram:Aretrospec-
tive,’’AppliedAILetters,vol.2,no.4,pp.1–11,2021.
[129] D.Alvarez-MelisandT.S.Jaakkola,‘‘Ontherobustnessofinterpretabil-
itymethods,’’2018,arXiv:1806.08049. SUMEYE NUR KARAHAN received the B.Sc.
[130] J.Adebayo,‘‘Sanitychecksforsaliencymaps,’’inProc.Adv.NeuralInf. degree in electronics and communication engi-
|     |     |     |     |     |     |     |     |     | neering | from | Izmir University, |     | Izmir, Türkiye, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ----------------- | --- | --------------- |
Process.Syst.,vol.31,2018,pp.1–11.
in2014,andtheM.Sc.andPh.D.degreesinelec-
[131] J.SikKim,G.Plumb,andA.Talwalkar,‘‘Sanitysimulationsforsaliency
methods,’’2021,arXiv:2105.06506. trical and electronics engineering from Ankara
|     |     |     |     |     |     |     |     |     | University,   | Ankara, | Türkiye, | in       | 2018 and 2025, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | -------- | -------- | -------------- |
|     |     |     |     |     |     |     |     |     | respectively. | She     | was a    | Research | Assistant with |
theDepartmentofElectricalandElectronicsEngi-
neering,AnkaraUniversity,from2015and2024.
Since2024,shehasbeenaSeniorResearchand
|     |     | OSMAN | KAYA | received the | M.Sc. degree | in  |     |     |     |     |     |     |     |
| --- | --- | ----- | ---- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
DevelopmentResearcherwiththeResearchandDevelopmentDepartment,
electronicsandcommunicationsengineeringfrom
TurkTelekom,Ankara.HerresearchinterestsincludeMIMOcommunica-
|     |     | Yıldız | Technical | University, | Istanbul, Türkiye, |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --------- | ----------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
tionsystems,integratedsensingandcommunication(ISAC),deeplearning,
|     |     | where | he is | currently pursuing | the Ph.D. | degree |     |     |     |     |     |     |     |
| --- | --- | ----- | ----- | ------------------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
andexplainableartificialintelligence.
incommunications.Hisresearchinterestsinclude
|     |     | modulation |                 | classification, channel | identification, |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | --------------- | ----------------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | and        | the application | of artificial           | intelligence    | in  |     |     |     |     |     |     |     |
5Gand6Gwirelesscommunicationsystems.His
workfocusesonenhancingnetworkperformance MUSTAFA SERDAR OSMANCA is currently a
andreliabilitythroughadvancedsignalprocessing Faculty Member with Gazi University, Türkiye,
andmachinelearningtechniques. specializinginthefieldofcommunicationwithin
theDepartmentofElectricalandElectronicsEngi-
|     |     |     |     |     |     |     |     |     | neering. | He teaches  | courses,      | such | as commu-   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------------- | ---- | ----------- |
|     |     |     |     |     |     |     |     |     | nication | techniques, | Communication |      | Laboratory, |
andtheTürkTelekomIndustrialCommunication
Laboratory.Hehasheldvariousroleswithinthe
|     |     | A.  | F. M. | SHAHEN SHAH | (Senior Member, |     |     |     |         |             |      |      |                |
| --- | --- | --- | ----- | ----------- | --------------- | --- | --- | --- | ------- | ----------- | ---- | ---- | -------------- |
|     |     |     |       |             |                 |     |     |     | Network | departments | with | Türk | Telekom. He is |
IEEE) received the B.Sc. degree in electronics currentlytheResearchandDevelopmentManager.
andtelecommunicationengineeringfromDaffodil His research interests include communication, DWDM, and QUIC-based
|     |     | InternationalUniversity,Bangladesh,in2009,the |     |     |     |     | trafficanalysis. |     |     |     |     |     |     |
| --- | --- | --------------------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
M.Sc.degreeininformationtechnologyfromthe
|     |     | University | of           | Dhaka, Bangladesh, | in 2011,       | and |     |     |     |     |     |     |     |
| --- | --- | ---------- | ------------ | ------------------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | the        | Ph.D. degree | in electronics     | and communica- |     |     |     |     |     |     |     |     |
tionengineeringfromYildizTechnicalUniversity,
Türkiye, in 2020. He is currently an Associate NURETTIN ACıR received the Ph.D. degree in
ProfessorwiththeDepartmentofElectronicsand electricalandelectronicsengineeringfromDokuz
CommunicationEngineeringandtheDirectoroftheAIandNext-Generation EylulUniversity,Izmir,Türkiye,in2004.In2003,
WirelessCommunicationLaboratory(ANWCL),YildizTechnicalUniver- he was a Visiting Researcher with the Neu-
sity.Hehasauthoredabook.Hehaspublishedagoodnumberofresearch rosensory Engineering Laboratory, University of
papersininternationalconferencesandjournals.Hiscurrentresearchinter- Miami, FL, USA. From 2012 to 2013, he was
estsincludewirelesscommunication,artificialintelligence,6G,blockchain, a Visiting Researcher with the Department of
andtheIoT.HehasbeenaTPCmemberforseveralIEEEconferencesand Electrical and Electronic Engineering, Imperial
aregularreviewerforvariousIEEEjournals.ForhisPh.D.work,hewona College London, London, U.K. He is currently
GoldMedalatthe32ndInternationalInvention,Innovation,andTechnology a Professor with the Department of Electronics
Exhibition(ITEX)in2021.HeisservingastheEditor-in-ChiefofICCK Engineering, Turkish Air Force Academy, National Defense University,
TransactionsonMobileandWirelessIntelligenceandICRRDQualityIndex Istanbul, Türkiye. His research interests include linear/nonlinear systems
ResearchJournal,anEditorforTheOpenTransportationJournal(Bentham) theory,adaptivefiltertheory,intelligentmedicaltechnology,advancedsignal
and Discover Vehicles (Springer), and an Associate Editor for Journal of anddataprocessing,andartificialintelligence-basedindustrialapplications.
CyberSecurityTechnology(TaylorandFrancis).
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     | 27417 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |