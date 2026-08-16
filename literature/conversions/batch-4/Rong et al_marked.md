---
conversion_metadata:
  converted_at: "2026-07-21T08:20:35Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Rong et al.pdf"
  source_pdf_sha256: "8ae1786f30649f308604788db5e24801120b51531b7d5cb1d0cc82b6a796b955"
  page_count: 19
  markdown_char_count: 254404
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

2104

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

Towards Human-Centered Explainable AI: A Survey
of User Studies for Model Explanations

Yao Rong , Tobias Leemann , Thai-Trang Nguyen , Lisa Fiedler

, Peizhu Qian , Vaibhav Unhelkar

,

Tina Seidel

, Gjergji Kasneci

, and Enkelejda Kasneci

(Survey Paper)

Abstract—Explainable AI (XAI) is widely viewed as a sine qua
non for ever-expanding AI research. A better understanding of
the needs of XAI users, as well as human-centered evaluations of
explainable models are both a necessity and a challenge. In this
paper, we explore how human-computer interaction (HCI) and
AI researchers conduct user studies in XAI applications based on
a systematic literature review. After identifying and thoroughly
analyzing 97 core papers with human-based XAI evaluations over
the past ﬁve years, we categorize them along the measured char-
acteristics of explanatory methods, namely trust, understanding,
usability, and human-AI collaboration performance. Our research
shows that XAI is spreading more rapidly in certain application
domains, such as recommender systems than in others, but that
user evaluations are still rather sparse and incorporate hardly any
insights from cognitive or social sciences. Based on a comprehensive
discussion of best practices, i.e., common models, design choices,
and measures in user studies, we propose practical guidelines on
designing and conducting user studies for XAI researchers and
practitioners. Lastly, this survey also highlights several open re-
search directions, particularly linking psychological science and
human-centered XAI.

Index Terms—Explainable AI (XAI), human-centered XAI,

explainable ML, user study, human-AI interaction.

I. INTRODUCTION

A RTIFICIAL Intelligence (AI) is driving digital transfor-

mation and is already an integral part of various every-
day technologies. Recent developments in AI are essential to
progress in ﬁelds such as recommendation systems [97], [98],
[99], autonomous driving [100], [101], [102] or robotics [103],
[104], [105]. Moreover, AI’s success story has not excluded

Manuscript received 3 February 2023; revised 26 October 2023; accepted 4
November 2023. Date of publication 13 November 2023; date of current version
6 March 2024. Recommended for acceptance by M. Cheng. (Corresponding
author: Yao Rong.)

Yao Rong, Tina Seidel, Gjergji Kasneci, and Enkelejda Kasneci are
with the Technical University of Munich, 80335 Munich, Germany (e-mail:
yao.rong@tum.de;
tina.seidel@tum.de; gjergji.kasneci@tum.de; enkelejda.
kasneci@tum.de).

Tobias Leemann, Thai-Trang Nguyen, and Lisa Fiedler are with the Uni-
versity of Tübingen, 72076 Tübingen, Germany (e-mail: tobias.leemann@
uni-tuebingen.de;
lisa.ﬁedler@
student.uni-tuebingen.de).

thai-trang.nguyen@student.uni-tuebingen.de;

Peizhu Qian and Vaibhav Unhelkar are with the Rice University, Houston,

TX 77005 USA (e-mail: pq3@rice.edu; vaibhav.unhelkar@rice.edu).

This article has

supplementary downloadable material available at

https://doi.org/10.1109/TPAMI.2023.3331846, provided by the authors.

Digital Object Identiﬁer 10.1109/TPAMI.2023.3331846

high-stakes decision-making tasks like medical diagnosis [106],
[107], [108], credit scoring [109], [110], [111],
jurispru-
dence [112], [113] or recruiting and hiring decisions [114],
[115], However, the behavior and decision-making processes
of modern AI systems are often not understandable, so they are
frequently considered black boxes. Deploying such black-box
models presents a serious dilemma in certain safety-critical do-
mains, for instance, public health or ﬁnance [116]. This is due to
the necessity for a transparent and trustworthy AI system, which
is required by both practitioners (to gain better insights into
system functioning) and end users (to rely on model decisions).
Methods to increase the interpretability and transparency of
an AI system are developed in the research area of Explainable
AI (XAI). Speciﬁcally, human-centered XAI, which addresses
the importance of human stack-holders to the AI systems, has
been proposed and discussed since [117], [118]. While a huge
number of model explanations are available, the question of how
to transparently evaluate their quality is still an open research
question, and hence, extensively studied in recent years. A popu-
lar taxonomy of evaluation strategies for XAI methods proposes
three categories: functionally-grounded evaluation, application-
grounded evaluation, and human-grounded evaluation [119].
While functionally-grounded measures do not require human
labor, the other two involve human subjects and are more costly
to conduct.

Many functionally-grounded measures have been proposed
to evaluate XAI algorithms (see [120] for review), however, the
difﬁcult comparability between different automatic evaluation
measures is a common problem [121], [122]. Another drawback
of automated measures is that there is no guarantee that they
truly reﬂect humans’ preferences [40], [123]. Consequently,
user studies in XAI, especially when moving towards real-world
products, are inevitable if one wishes to test more general beliefs
of the quality of explanations [16]. However, only a small portion
(about 20%) of XAI evaluation projects consider human sub-
jects [120]. There exist efforts in developing taxonomies or intro-
ducing the deﬁnitions or implications of different human-centric
evaluations [124], [125], [126], but the recent generation of user
studies and their ﬁndings have not been systematically discussed
yet. Moreover, Yang et al. [127] point out that XAI is growing
separately and treated differently in different communities (e.g.,
machine learning and HCI). Hence, effective guidance in XAI
user study design is crucial to better let both XAI algorithm

© 2023 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see
https://creativecommons.org/licenses/by/4.0/

---

<!-- PAGE 2 -->

RONG et al.: TOWARDS HUMAN-CENTERED EXPLAINABLE AI: A SURVEY OF USER STUDIES FOR MODEL EXPLANATIONS

2105

TABLE I
OVERVIEW OF THE CORE PAPERS CONTAINING USER STUDIES IN XAI GROUPED BY CATEGORIES OF MEASUREMENTS AS SOME CORE PAPERS ASSESS
QUANTITIES BELONGING TO SEVERAL GROUPS, A SINGLE PAPER CAN ALSO BE LISTED AMONG MULTIPLE GROUPS

and application designers recognize the users’ real needs. This
work aims to bridge this research gap in modern XAI user study
design by distilling practical guidelines for user studies through
a comprehensive and structured literature review.

Therefore, we reviewed highly relevant papers that include
user studies from top-tier HCI and XAI venues. Speciﬁcally,
we included the recent ﬁve years of CHI, IUI, UIST, CSCW,
FA(cc)T, ICML, ICRL, NeurIPS, and AAAI. As we aim at ana-
lyzing human user evaluation of advanced model explanations,
we ran search queries involving keywords from the two groups
“explainable AI” and “user study”, as listed in the Table II.
We selected the papers containing at least one keyword from
each group, resulting in over one hundred papers. Then, we
thoroughly studied these papers and ﬁltered out papers that
did not fulﬁll the criteria: (1) deploying explainable models
or techniques and (2) conducting an assessment with human
subjects. We identiﬁed a total of 97 core papers for this survey
(see Table I for an overview of core papers with respect to their
measured quantities in user studies). Based on these core papers,
we performed a comprehensive analysis to ﬁll the research gap
by offering a systematic overview of user studies in XAI. We
highlight the main contributions:

1) To offer an overview of the foundational work of user stud-
ies in XAI, we investigated references of all 97 core papers
in a data-driven manner. Likewise, we analyzed follow-up
works building on these core papers (identiﬁed through
citations of core papers) to reveal the ﬁelds impacted by
XAI user evaluations (Section III).

2) We present a summary of the design details in XAI user
studies with particular focus on the deployed models
and explanation techniques, experimental design patterns,
participants as well as concrete measures, providing inspi-
ration of how to collect human assessment (Section IV).
3) We discuss the impact of using explanations on different
aspects of user experience (Section V), which can serve
as an overview of the effectiveness of the current XAI
technology and a summary of the state-of-the-art.

4) Based on the examined user study details and their best-
practice ﬁndings, we synthesize guidelines for designing
an effective user study for XAI (Section VI).

5) Beyond the user study design, we discuss potential
paradigms of AI systems understanding humans in the
context of e.g., theory of minds, as well as other future
research directions (Section VII).

Our study highlights under-investigated areas in the context
of current user-centered XAI research such as cognitive or psy-
chological sciences through data-driven bibliometric analysis.
Together with our proposed guidelines, we believe that this
work will beneﬁt XAI practitioners and researchers from various
disciplines and will help to approach the overarching goal of
human-centered XAI.

II. RELATED WORK

As a vast amount of explanation methods have been pro-
posed, many researchers seek a systematic overview of the ever-
growing ﬁeld of XAI. In [128], [129], [130], [131], [132], [133],
the authors aim to cover many facets of XAI technologies rang-
ing from problem deﬁnitions, goals, AI/ML model explanations
to evaluation measures, while in [134] the authors emphasize the
research trends and challenges in Human-Computer-Interaction
(HCI) applications. A large body of XAI surveys focuses
mainly on the interpretability of a particular family of models
and corresponding explanation techniques. For instance, [135],
[136], [137] investigate explanations for Deep Neural Networks
(DNNs), where models often take images as input [135], [136].
Joshi et al.
[137], however, provide an extensive review for
DNNs with multimodal input for instance that of joint vision-
language tasks. Causal interpretable models are gaining more
attention recently and Moraffah et al. [138] provide a literature
review for causal explanations. A systematic literature review on
explanations for advice-giving systems is conducted in [139].
Among these surveys focusing on general XAI technologies,
evaluation measures are only brieﬂy examined.

One challenge in XAI research is to evaluate and com-
pare different explanation methods, due to the multidisci-
plinary concepts in interpretability/explainability [119], [120],
[140]. Evaluation measures can be divided into two groups:
human-grounded measures that rely on human subjects and
functionally-grounded metrics that can be computed without
human subjects [119], [120]. Many researchers seek solutions to
evaluate explanations automatically. A comprehensive literature
review with a focus on these functionally-grounded evaluation
methods (without human subjects) can be found in [120]. Ex-
plainability is an inherently human-centric property, therefore,
the research community should and has started to recognize
the need for human-centered evaluations when working on
XAI [119], [141].

---

<!-- PAGE 3 -->

2106

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

Fig. 1. Roadmap of our literature analysis. We ﬁnd out the foundational works of core papers and their application domains using a data-driven method introduced
in Section III. Three main research questions in user studies are distilled from core papers. Methods related to measures of each category are discussed in Section
IV, and ﬁndings of the research questions are summarized in Section V. Based on the ﬁndings, we propose future directions to further promote human-centered
XAI in Section VII. We distill important messages in this ﬁgure, but refer to the discussion in the corresponding sections for more details.

For instance, Chromik and Schuessler [125] propose a taxon-
omy on XAI evaluations involving humans. Mohseni et al. [126]
summarize four groups of human-related evaluation metrics:
mental model (e.g., user’s understanding of the model), user
trust, human-AI task performance and explanation usefulness
and satisfaction (i.e., user experience). Hoffman [124] places
more focus on psychometric evaluations by proposing a con-
ceptual model of the XAI process and specifying four key
components that should be evaluated: explanation goodness
and satisfaction, (user’s) mental models, curiosity, trust and
performance. Beyond assessing evaluation methods, XAI ap-
plications are designed to eventually support decision-making
and beneﬁt end users. A recent review by Lai et al.
[142]
considers studies on collaborative Human-AI decision-making,
which may include AI agents providing explanations. Success
in human-AI decision-making tasks can be seen as one amongst
many other ways to evaluate the effect of explanations. Ferreira
and Monteiro [143] present a review of the user experience of
XAI applications to answer who uses XAI, why, and in which
context (what + when) the explanation is presented.

Closer to our focus on user studies concerning XAI, Liao
et al. [141] study user experiences with XAI to reveal pitfalls
of existing XAI methods, underscoring the important role of
humans in XAI development. As suggested by Doshi-Velez and
Kim [119], a human-subject experiment needs to be designed
sophisticatedly to reduce confounding factors. In contrast to
previous surveys on XAI, we aim to provide XAI researchers
and practitioners with a comprehensive overview of the re-
search questions explored in user studies, along with thorough

information on experimental design. To this end, we present
a practical guideline in user study design, which can be used
as a starting point for future exploration of human-centric XAI
applications.

III. METHODOLOGY

To analyze the collected papers related to user studies on
XAI, we ﬁrst categorize them into four groups based on their
objectives. From these studies, we distill three main research
questions concerning the effects of model explanations on each
objective. We then summarize the methods used in these studies
to quantify these objectives. Important ﬁndings from the pa-
pers are discussed, and we propose future directions based on
these ﬁndings. Additionally, we examine the foundational works
upon which these user studies are based (i.e., their references)
and the follow-up papers that cite them, shedding light on the
foundational works and emerging trends in human-centered XAI
studies. Fig. 1 presents a roadmap of our analysis.

In this section, we ﬁrst describe the criteria used for their
categorization. We then discuss the foundational and application
domains of these papers, providing a broader view before diving
into their detailed analysis.

A. Categorization of User-Study Objectives

Since the core papers cover various factors of model explana-
tions, we decided to categorize the core papers into different
clusters to better study their commonalities and differences.
In [119], interpretability in the context of ML systems is deﬁned

---

<!-- PAGE 4 -->

RONG et al.: TOWARDS HUMAN-CENTERED EXPLAINABLE AI: A SURVEY OF USER STUDIES FOR MODEL EXPLANATIONS

2107

as the ability to explain or present model predictions in under-
standable terms to a human. Beyond fostering comprehension,
the authors argue that interpretability can assist in qualitatively
ascertaining whether other desiderata, such as usability and trust
are met. During a profound study of the relevant literature that
was previously selected, we identiﬁed four sensible categories,
that are derived from the considered dependent variables in user
studies (desiderata of interpretability). These four categories
are trust, understanding, usability, and human-AI collaboration
performance. In Table I, the studied papers are categorized
according to the measured quantities. As each measure can
usually be assigned to only one of these categories, we found
this distinction to be intuitive.

These categories reﬂect different functionalities (goals) of
XAI. As interpretability is deﬁned as “the ability to explain
or to present in understandable terms to a human.”, humans’
“understanding” is the direct goal of XAI. To be concrete,
understanding in the context of interacting with an ML model
refers to a user’s grasp or “mental model” of how the model
operates, and this knowledge grows from using the system and
from clear explanations about it [141]. “Usability” is commonly
studied in human-computer interaction [144], which is one of
the desiderata of XAI [119]. According to [145], usability is
the extent to which users can utilize a product to successfully,
efﬁciently, and satisfactorily accomplish their intended objec-
tives. Thus, this category encompasses user studies that employ
model explanations to support users in achieving speciﬁc tasks.
In usability, different aspects are measured, for instance, whether
the system is easy to use or how much cognitive load it requires.
The aspect “undesired behavior detection” relates to use cases
where explanations uncover model discriminatory behaviors,
such as the utilization of undesired features. “Trust” in AI is
summarized as a combination of the user’s conﬁdence in a
model’s accuracy, a personal comfort level with understand-
ing and using it, and the willingness to let the model make
decisions [140]. It encompasses more requirements. Human-AI
collaboration performance is related to scenarios where the AI
system provides its predictions, but humans retain the ﬁnal deci-
sions [89]. In this case, model explanations are deployed to reach
a performance superior to that of the AI system or the human
decision-maker alone. These categories cover different depen-
dent variables of interest in the reviewed user studies, primarily
related to how XAI methods function. These functions mainly tie
to the models’ reasoning and knowledge representation. A wider
perspective on XAI, which assesses generalization or robustness,
remains an important ﬁeld for future exploration through user
studies.

These are a frequent subject of study in works measuring un-
derstanding and usability. Additionally, convolutional networks,
which are commonly employed in experiments, use tools like
GradCAM [148] and various saliency maps to generate model
explanations. Notably, many research papers appear within the
domain of recommender systems, because many XAI user stud-
ies are conducted in the context of recommendation solutions.
he EU’s General Data Protection Regulation (GDPR) [149] is
frequently mentioned in core papers due to the ongoing debate
on the right to explanation” [150]. This debate has signiﬁcantly
inﬂuenced the shift in modern AI systems towards explainability.
While the ultimate consumers of model explanations are hu-
mans, well-established research domains that focus on human
understanding are underrepresented. For instance, only a few
papers related to “Cognition” are cited compared to those on
other algorithmic topics. Millecamp et al. [18] suggest enhanc-
ing XAI theory with insights from social sciences, including
cognitive science and psychology. Given the scant references to
psychology, it appears that only a handful of XAI user studies
delve into evaluating XAI from a psychological standpoint.
We highlight a nascent research domain of XAI frameworks
based on human cognition and behavior theories [141]. This
theoretical guidance can also offer conceptual tools for better
evaluating XAI from user perspectives. More details about
common references can be found in Appendix A.1, available
online.

C. Impact of User Studies

Fig. 1 presents applications that make use (and thus are the
consumers) of the ﬁndings from core papers. We noticed that
studies on user understanding and trust span a wide range of
applications. For example, trust is frequently addressed in the
contexts of medical diagnosis and transportation, indicating its
signiﬁcance in high-risk scenarios. Recommendation systems
emerge as a primary focus in follow-up works. Papers on
usability have a signiﬁcant impact on ﬁelds like data visual-
ization, software development, and education. In these areas,
models frequently serve as tools to ease the burden on end
users. Human-AI collaboration measures particularly promote
the further development of robotics and or natural language
processing. The prominence of recommendation systems in
both foundational works and their impact implies that XAI is
an integral component of contemporary recommendation sys-
tems. A comprehensive overview of the fundamental works and
application domains can be found in Appendix A.1, available
online.

B. Foundations of User Studies

IV. COMPREHENSIVE USER STUDY ANALYSIS

Based on a data-driven bibliometric analysis of the refer-
ences in core papers, we highlight signiﬁcant research topics
within the “Foundational Domain” in Fig. 1. It is evident that
model explanations and interpretability are pivotal components.
This includes papers that introduce explanation methods such
as LIME [146], SHAP [147], and other attribution methods.

In this section, we present details of the covered XAI user
studies. We ﬁrst introduce some commonly used AI models and
explanation techniques (Section IV-A), followed by a discus-
sion of application domains and measures with respect to the
four measured quantities. The experimental designs, as well as
analysis tools are presented in Section IV-C.

---

<!-- PAGE 5 -->

2108

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

TABLE II
KEYWORDS FOR OUR PAPER SEARCH QUERY

TABLE III
MODELS AND EXPLANATIONS IN CORE PAPERS

A. Models and Explanations

As our selected core papers comprise a large spectrum of
AI models, data modalities, and explanation approaches, we
initially list the models and explanation techniques deployed
along with the corresponding core paper references in Table III.
It presents the utilization of explanation types in columns and
model types in rows. The explanation methods used is organized
according the the taxonomy by Molnar [151]. First, there are
intrinsically interpretable models, also known as white-box mod-
els. For instance, white-box models include decision trees and
linear models. Second, there are black-box models that provide
no parameter access or are too complex to be explained in a
human-understandable way [152]. These include ensembling
techniques such as Random Forests or neural models.

As for explanation techniques, we identiﬁed ﬁve key types
in the scope of the surveyed papers (rows of Table III).
Most frequently used are feature-based (attribution) explana-
tions, for instance, SHAP (Shapley additive explanations [147])

and LIME (Local
Interpretable Model-Agnostic Explana-
tions [146]). There is a clear differentiation between local,
instance-wise, explanations and global explanations that apply
to the model in its entirety. For instance, the weights of a linear
model have a global scope. This differentiation is common
among these feature-based explanations, where most of the
papers using local explanations. Other popular explanation types
are example-based explanations, counterfactual explanations,
which aim at providing actionable suggestions for attaining a
user-preferred prediction by changing certain input features, and
concept-based explanations, which use meaningful high-level
concepts such as objects or shapes to explain a prediction.

Besides these four main types of explanations, there are other
explanations such as rules [11], [88] or game strategies [7], [10]
when AI plays games. More details about concrete models and
explanations can be found in Appendix B, available online.

B. Measurements

The effectiveness of explanations can be characterized from
several angles. We speciﬁcally identiﬁed the categories of trust,
understanding, usability, and human-AI collaboration perfor-
mance. In this section, we give an overview of the contexts in
which each of these variables is studied and the measures used
to quantify them.

1) Trust: User trust is studied in decision-making applica-
tions such as image classiﬁcation [13], [17], (review) deception
detection [25] or loan approval [27]. Besides decision mak-
ing, [5], [8], [16], [18], [19], [23] study user trust in the domain
of recommendation systems. Whether explainable ML models
can increase user trust in the medical domain is studied in [1],
[6], [9]. Moreover, Colley et al.
[3] measure user trust in an
autonomous driving application with and without explanations.
Trust measures used in much of the existing research can be
divided into two groups: self-reported and observed trust [155].
Self-reported trust is commonly measured by asking users to
ﬁll out questionnaires whereas observed trust is quantiﬁed by
humans’ agreement with the model’s decisions. In Table III in
Appendix, available online, trust measures in these two groups
are listed. The agreement rate of users with the model decisions
is commonly used [9], [11], [12], [25] as a measure of observed
trust. Parallel to observed trust measurement, van der Waa
et al. [156] ascribe the user’s alignment behaviors to the persua-
sive power of model explanations, i.e., the capacity to convince
users to follow model decisions despite the correctness. As an
extension, trust calibration is deﬁned based on this measure.
For example, a high agreement rate to wrongly made decisions
represents overtrust, while a low agreement rate to correct
decisions means undertrust [12]. In self-reported measurements,
researchers either utilize well-developed questionnaires or self-
designed ones, with the exception of [4] which conducts a semi-
structured interview to explore user opinions. Several works [6],
[11], [13], [16], [17], [18], [19], [24], [27] propose their own
questionnaires. Among these, a subgroup [13], [16], [18], [19],
[24] simply asks users to rate a single statement such as “I
trust the system’s recommendation/decision”, which is named
as one-dimensional trust by [8]. When deploying previously

---

<!-- PAGE 6 -->

RONG et al.: TOWARDS HUMAN-CENTERED EXPLAINABLE AI: A SURVEY OF USER STUDIES FOR MODEL EXPLANATIONS

2109

proposed questionnaires [2], [3], [5], [7], [8], [10], [21], [22],
[23], [157], Trust in Automation [158] is the most commonly
used one, in which the underlying constructs of trust between
human and computerized systems are explored.

2) Understanding: An important goal of explanation tech-
niques is to foster users’ understanding of complex ML sys-
tems. An important separation has to be made between users’
perceived understanding and their actual comprehension of the
underlying model, as the two often do not agree [35], [40]. Cheng
et al. [22] explicitly differentiate between objective understand-
ing and self-reported understanding, which we term subjective
understanding in this work. While subjective understanding is
usually measured through questionnaires, measuring objective
understanding requires a proxy task where the users’ understand-
ing is put to a test. Additionally, user studies can be run to assess
how well users can understand the explanation itself (and not the
underlying model). This can be an important sanity check and is
particularly used in the domain of conceptual explanations [62],
[159], where the intelligibility of concepts needs to be veriﬁed.
We refer to the third category as understanding of explana-
tions but defer its detailed ﬁndings to Appendix C.3, available
online.

Objective Understanding: Works in the subdomain of objec-
tive understanding deploy proxy tasks to verify users’ under-
standing of a model’s inner workings. The most commonly con-
sidered domain in works on understanding is ﬁnance [35], [39],
[40], [47], [48], [49], [53] followed by image classiﬁcation [13],
[21], [52]. One of the most critical design choices when assessing
objective understanding is the selection of a suitable proxy task.
Doshi-Velez and Kim [119] argue that the task should “maintain
the essence of the target application” that is anticipated. One of
the most prominent tasks is forward simulation [119], [140].
This task demands subjects that are given an input to simulate,
i.e., predict, the model’s output. The extent to which participants
can successfully provide the model’s output is also referred to
as simulatability [140]. However, scholars have designed many
more tasks to quantify understanding and applied them across
a variety of data modalities (cf. Table 2 in Appendix, available
online for an exhaustive listing).

We brieﬂy describe other common tasks below. A special
variant of forward simulation is called relative simulation. In
this task, users predict which example out of a predeﬁned choice
will have the highest prediction score (or class probability). A
manipulation or counterfactual simulation task [119] asks users
to manipulate the input features in such a way that a certain
model outcome (counterfactual) is reached. Users’ performance
on this task can be used as a proxy for their understanding. Lip-
ton [140] pointed out that simulatability can only be a reasonable
measure, if the model is simple enough to be captured by humans
and that simpler tasks are required otherwise. An example could
be a feature importance query, where users have to tell which
features are actually used by the model. A directed and more
local version of this task is marginal effects queries, where the
subjects predict how changes in a given input feature will affect
the prediction (e.g., “Does increasing feature X lead to a higher
prediction of Y being class 1?”). Because explanations should
allow the identiﬁcation of weaknesses in models, the task of

failure prediction measures the accuracy of users’ prediction
when the model prediction is wrong.

Subjective Understanding: Besides the objective understand-
ing which is supported by performance indicators, understand-
ing of a model may be subjective, i.e., it may depend on a user’s
own perception. The most commonly used applications that
measure subjective understanding are various recommendation
system setups [16], [33], [34], [38].

Most of the works assess the subjective understanding of a
[7] adapted a
user with a post-task questionnaire. Guo et al.
popular questionnaire designed for recommendation systems by
Knijnenburg et al. [160], while Bell et al. [39] accommodated
the questionnaire which originally intended to measure the in-
telligibility of differenet explanations by Lim and Dey [161].
On the other hand, agreement to simple subjective statements
such as “I understand this decision algorithm” [22], “I un-
derstand how the AI...” [13], [17] or “The explanation(s) help
me to understand...” [33] can be collected to assess subjective
understanding.

3) Usability: Usability is a key concern of every HCI system
and thus applies to almost all domains. This is reﬂected in the
surveyed papers, where usability is studied in a wide range
of setups and contexts. We also include application-speciﬁc
performance measures in this category.

Based on the measurements in the user studies, we reﬁned us-
ability into measures of helpfulness, workload (cognitive load),
satisfaction, ease of use and detecting undesired behaviors of
the system, as shown in Table I. To assess workload (cognitive
load), NASA-TLX scale [162] is used in [3], [6], [16], [21], [66],
while Abdul et al. [48] measure cognitive load by capturing the
log-reading time of memorizing the explanation. Most of the
works use self-designed questionnaires or statements to measure
satisfaction [6], [16], [18], [19], [29], [30], [69], [70], however,
the Explanation Satisfaction Scale [163] can be deployed as an
established alternative [1], [47]. Helpfulness can be assessed
by simply asking for subjective ratings of the explanations for
accomplishing a speciﬁc task [13], [46], [56], [65], [67], [68].
Colley et al. [3] use an adapted version of the System Usability
Scale proposed in [164].

Using model explanations to audit models is one purpose
of explainability [129]. Some of the surveyed works study
how model explanations can assist users in detecting undesired
behaviors of models. These issues mainly include (perceived)
unfairness in the model decision-making [38], [74], [78], [79],
biases in models [72] or features [57], and wrong decisions
(failures) [24] in the studied papers. A detailed summary of types
of undesired behaviors is listed in Table VI. In the undesired
behavior detection, the effectiveness of explanations is evaluated
by objective performance measures, such as the number of bugs
identiﬁed [71], the share of participants that identify a certain
bias [57, First Experiment] or by the deviations between model
predictions and human predictions for unusual samples [53].
The perception of users regarding fair treatment by a system has
primarily been researched in high-stakes applications such as
granting loans [27] or granting bail for criminal offenders [73],
[74], [75]. For example, [73], [74], [75] investigate the fairness
of COMPAS, a commercial criminal risk estimation tool that was

---

<!-- PAGE 7 -->

2110

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

TABLE IV
EXPERIMENTAL DESIGNS IN CORE PAPERS

used in the US to help make judicial bail decisions. It is also con-
sidered in everyday use-cases such as news [38] and music [77]
recommendations, or possible career suggestions [76], where
a bias in the underlying system can be to the detriment of the
user. As the assessment of fairness is a very subjective matter,
questions regarding perceived fairness are prevalent, e.g., “how
the software made the prediction was fair” [74], which can be
answered on 5- or 7-point Likert scales [2], [27], [38], [73],
[74], [75]. Among these works, an effective explanation is the
one that can either increase or decrease the fairness perceptions,
since the aim of explanations is to show fairness or unfairness.
An exhaustive overview of measures for usability is given in
Table IV of the Appendix, available online.

4) Human-AI Collaboration Performance: The goal of
human-AI teaming is to improve the performance in AI-
supported decision-making above the bar set by humans or an
AI alone [89]. Improving human performance with the help of
AI has been considered in games [10], [88], question answering
tasks [89], [91], deception detection [25], [90] and topic model-
ing [29], [30].

The most common assessment is to rate AI-aided human
performance by the percentage of correctly predicted instances
in the decision-making process [25], [89], [90]. Paleja et al. [10],
however, deﬁne the performance as the time to complete the task.
In [88], performance is measured in a game-based application,
chess, using a winning percentage (which is commonly used in
sports) as well as a percentile rank of player moves.

C. Experimental Design and Analysis

There are three common experimental settings when conduct-
ing user evaluation: between-subjects (or between-groups) de-
signs, within-subjects designs, and mixed designs that combine
elements of both. An overview of the designs found in the core
papers and their participant numbers is presented in Table IV
and Fig. 2, respectively.

1) Between-Subjects: With slightly above 55 % of the user
studies conducted in a between-subjects manner, i.e., one subject
is only exposed to one condition, this design choice is most
common in the XAI literature. The number of participants in
the between-subjects manner usually starts at around 30 partic-
ipants, while it may go up to 1070 in total for 3 conditions as
in [17] and to 1250 for 5 conditions in [53]. However, the number
of participants can be limited when the studied application is
designed for speciﬁc groups of lay persons, which cannot be
easily recruited from the Internet platforms such as Amazon

Fig. 2. Distribution of participant numbers in the surveyed user studies by
design and participant type (each bar represents one study). Per-design means
are indicated in bold.

Mechanical Turk. For instance, Ooge et al. [8] use 12 school
students per condition. Some authors place particular emphasis
on participants being similar to the average demographic [73],
[75].

The conditions usually include the different explanation tech-
niques in combination with other parameters such as the model,
data set, data modality, or a number of features used as in-
dependent variables. Note that a full grid design with many
independent variables may quickly result in a very high number
of conditions, which in turn requires many participants. The out-
come variable of interest is commonly measured on a numerical
or ordinal scale right away, however, in the fairness domain,
qualitative analyses are sometimes obtained through conducted
interviews or written responses [2], [27], [73].

The statistical analysis directly follows from this design. If
one is interested in identifying signiﬁcant differences between
the groups, common statistical hypotheses tests are used. For
overall comparison, one or two-way ANOVA tests are the most
commonly used statistical tool. Interesting post-hoc compar-
isons between two groups can be made with a standard T-test,
if the data is normally distributed with equal variance, or by
using non-parametric tests such as the Wilcoxon rank-sum
test (also known as Mann-Whitney U-test) for comparison of
two populations (e.g, [57]) or the Tukey HSD test (e.g., [49])
for multiple populations. When running multiple post-hoc
tests, some works make use of the Bonferroni correction
(e.g, [57]).

2) Within-Subjects: Around 30 % of the papers use the
within-subjects design, where each participant sequentially
passes through all conditions and provides feedback. Fewer
participants are recruited in within-subjects experiments com-
pared to the between-subjects ones. Hence, they are particularly
popular when participants with restrictive characteristics, such
as domain-speciﬁc professional expertise, are required. For ex-
ample, Suresh et al. [9] and Rong et al. [26] recruit fourteen
medical professionals and ﬁve radiologists in their user studies,
respectively. The small number of medical experts contributing
to the user study is a limitation [26], however, it is often the case
in expert user research. Gegenfurtner et al. [165] evaluate 73
sources and point out that the majority of these studies include
only ﬁve, maybe ten experts. Besides the medical domain,
other works [3], [4], [19], [21] also invite subjects with par-
ticular professions such as engineers in a technology company.
When no speciﬁc knowledge is required, however, participant

---

<!-- PAGE 8 -->

RONG et al.: TOWARDS HUMAN-CENTERED EXPLAINABLE AI: A SURVEY OF USER STUDIES FOR MODEL EXPLANATIONS

2111

TABLE V
USER STUDY FINDINGS WHEN USING MODEL EXPLANATIONS AS EVALUATION DIMENSIONS

numbers reach up to 740 also for within-subjects designs [93].
For within-groups designs, the Wilcoxon signed-rank test (e.g.,
used by [35], [52]) is the most common method to compare
paired samples for signiﬁcant differences. Repeated-measures
ANOVA is a common analysis tool, when multiple comparisons
are required (see, e.g., [35]).

3) Mixed: The smallest group of studies, about 15%, use
a mixture of between- and within-subjects settings. In these
works, subjects are ﬁrst assigned randomly to one group, where
they are exposed to multiple conditions. Anik and Bunt [2]
use knowledge background in machine learning as a between-
subjects factor to divide the participants into three groups
(expert, intermediate and beginner), while inside each group
participants interact with explanations in the context of four
different scenarios (e.g., facial expression recognition or au-
tomated speech recognition). Dominguez et al.
[16] make
the presence of explanations a between-subjects condition and
different types of explanations a within-subjects factor in the
group with model explanations. A particular challenge for such
a study design is that statistical tools from both the independent-
samples and dependent-samples categories need to be
combined.

V. FINDINGS OF USER STUDIES

In this section, we summarize the primary ﬁndings from the
core papers. Table V lists ﬁndings with respect to four measured
quantities. To build an overview of the ﬁndings, we divide papers
according to their evaluation dimensions, i.e., the independent
variables in the user studies. When using the presence of expla-
nations as the evaluation aspect, the ﬁndings are summarized in
Table V. The listed impacts using explanations are to be seen in
comparison with a control group without explanations. Effects
are divided into two groups: (1) Positive effects, for example,
increasing user trust or understanding; (2) Non-positive effects:
the effect can be negative, or not signiﬁcantly positive (neural),
or a mixture of different effects (e.g., feature-based explanations
have positive effects but counterfactual explanations do not).
Beyond the explanations themselves, other possible evaluation
dimensions such as that might have an impact on the perception
of XAI, for instance, AI technology literacy, model performance,
or the dimensionality of the data. Instead of using the mere pres-
ence of explanations, many works compare different explanation
techniques with each other (see Appendix D, available online for
more details).

---

<!-- PAGE 9 -->

2112

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

TABLE VI
OVERVIEW OF RESULTS FOR UNDESIRED BEHAVIOR DETECTION USING MODEL
EXPLANATIONS

As various research questions and ﬁndings are addressed
in 97 core papers, many papers compare explanation types in
order to choose a preferable one, it is not possible to cover all
results in one table. Based on them, we outline some interesting
trends in the effectiveness of explanations on user experience: (1)
Explanations are effective in improving users’ subjective under-
standing; (2) The effectiveness of explanations in increasing user
trust and usability of models is not clear; (3) Explanations are not
good at convincing users that models are fair; (4) Interactivity
of the model has positive impact on user trust, understanding
and model usability. The ﬁrst three statements can validated
through the number of papers obtaining positive or non-positive
effects in each category, while the last ﬁnding is extracted from
Table V in the Appendix, available online, which details ﬁndings
with on other independent variables. We encourage the reader
to consider the short summary of primary ﬁndings in the tables
and check for further details according to their speciﬁc interests.
In the following section, we highlight some ﬁndings for each
category of measurement.

Trust: Among the papers comparing the effect of using expla-
nations to using no explanations, or placebo (randomly gener-
ated) explanations [8], [25], about half of the papers validate that
explanations have a positive impact on user trust [1], [8], [10],
[13], [16], [25], [27], [28], while the other half cannot verify this
hypothesis [3], [11], [12], [21], [22], [24]. For instance, Colley et
al. [3] investigated the explanations in an autonomous driving
task and discover that the trust is improved in simulation but
not with the real-world footage. Another example of the mixed
effect of using explanations is found in [12], where (minimal)
evidence is found that feature-based explanations help increase
appropriate trust, but counterfactual explanations do not.

Apart from using explanations as independent variables, the
user personalities or expertise may also affect their percep-
tions [2], [17], [18], [22], [23], [30]. Millecamp et al. [18] cap-
tured personal characteristics in the aspects such as the Locus of
Control deﬁned by Fourier (“the extent to which people believe
they have power over events in their lives”), Need for Cognition
(“a measure of the tendency for an individual to engage in effort-
ful cognitive activities”) or Tech-Savviness (“the conﬁdence in
trying out new technology”). However, no signiﬁcant interaction
effect could be found between the personal characteristics and
the trust. Liao and Sundar [5] studied a recommendation system
asking users’ personal data with different explanations. They
hypothesized that explanations in a “help-seeker” style and using

the pronoun “I” would gain more trust of users than the ex-
planations formalized in a “help-provider” style. Nevertheless,
However, the opposite result is found and using self-referential
expression resulted in lower affective trust. Model performance
together with model explanation was studied in [17] for an
image recognition task. The authors found out when images were
recognized (high model performance), users feel the system
more capable (“capability” is deﬁned as a belief of trust).

Understanding: The fundamental question in this subdomain
is to ﬁnd out which explanation technique is most beneﬁcial
for increasing the user’s understanding of a machine learning
model. As pointed out earlier, understanding can be measured
both in a subjective and objective manner.

We ﬁrst discuss results on objective understanding. The goal
of increasing objective understanding was explicitly posed by
Alqaraawi et al.
[54] who reported that saliency maps have
a positive effect on understanding. Wang and Yin [12] show
that counterfactual explanations and feature importance increase
users objective understanding. On the contrary, Sixt et al. [57]
ﬁnd none of their examined explanation techniques (counterfac-
tuals, conceptual explanations) superior to a baseline technique
consisting of example images for each class and the work by
Hase and Bansal [40] reveals that many explanations (includ-
ing anchors, prototypes) have no effect in increasing objective
understanding, which LIME on tabular data being the only
exception. Apart from the explanation, several other factors have
been identiﬁed to have an effect on objective understanding.
Hase and Bansal [40] suggest that the data modality may have a
non-negligible impact on how different explanation techniques
increase understanding. Some results highlight that the choice
of proxy task is inﬂuential. Arora et al.
[50] show that their
manipulatablity task revealed differences remained hidden when
forward simulation is used. In spite of these ﬁndings, Buçinca et
al. [13] underline that preferred explanations may be different
in a real-world application from a simulated one. Regarding
the type of model, there is disagreement on whether white or
black-box models can lead to increased objective understanding.
While black-box models without explanations resulted in higher
simulation performance than white-box models with SHAP
values in [39], Cheng et al. [22] observe that white-box models
increase simulatability and also conclude that interactivity is an
important factor when it comes to objective understanding.

In comparison with the objective understanding, the research
question in the subdomain subjective understanding is to ﬁnd
out how explanations impact user’s perceived understanding [7],
[12], [17], [22], [32], [33], [34], [37], [56]. There exist a trend
of using model explanations to improve subjective understand-
ing [13], [16], [17], [28], [34], [38], [167]. However, Chromik et
al. [35] challenge the improvement in perceived understanding
with the cognitive bias named illusion of explanatory depth
(IOED) [168], which means that laypeople often have overcon-
ﬁdence bias in their understanding of complex systems. Their
results conﬁrm the IOED issue in XAI, i.e., questioning users’
understanding by asking them to apply their understanding
in practice consistently reduces their subjective understand-
ing. Explanations can have different impacts on subjective and
objective understandings [22], where white-box explanations

---

<!-- PAGE 10 -->

RONG et al.: TOWARDS HUMAN-CENTERED EXPLAINABLE AI: A SURVEY OF USER STUDIES FOR MODEL EXPLANATIONS

2113

increase objective understanding but do not have signiﬁcant
impact on subjective understanding. Similar disagreements have
been observed in multiple other works [40], [167]. Radensky
et al. [33] examine the joint effects of local and global expla-
nations in a recommendation system and their results provide
evidence that both are better than either alone.

that the performance gain of novices and experts comes from
[10] reveal that
different explanation sources. Paleja et al.
explanations can improve novices’ performance but decrease
experts’ performance. Additionally,
less complex models
with explanations can better convince humans in correct
decisions [90].

Usability: Similar to trust, it is not clear whether explanations
are effective in improving users’ perceptions of helpfulness, sat-
isfaction or other dimensions of usability. For instance, in [16],
[30], [47], the explanations have a positive effect on satisfaction,
while no signiﬁcant effects on satisfaction are observed in [18],
[19], [29], [69]. Parallel to trust, Smith-Renner et al.
[29]
provide evidence for the hypothesis that it is harmful to user
trust and satisfaction to show explanations by highlighting the
important words in a text classiﬁcation task. A strong correlation
between self-reported trust and satisfaction can also be observed
in [3], where explanations have a positive impact in a simu-
lated driving environment, but no signiﬁcant effects when using
real-world data. Beyond explanations, Nourani et al. [56] study
the order of observing system weakness and strengths, which
reveals that encountering weakness ﬁrst results in a lower rate
of usage of system explanations than encountering strength ﬁrst.
Schoeffer et al. [27] ﬁnd out that showing feature importance
scores or counterfactual explanations (or a combination of both)
for explaining decisions helps increase the perceived fairness,
whereas highlighting important features without scores does not.
However, several studies don’t show a signiﬁcant difference
between scenarios with and without explanations [27], [38],
[78]. Effects of explanations may be dependent on input samples,
as shown in [67]. The authors show that both Debiased-CAM and
Biased-CAM improve the helpfulness for a weakly blurred im-
age, however, there is no signiﬁcant improvement for unblurred
or strongly blurred images. When used to assist users in detecting
undesired behaviors, model explanations are likely to identify
various types of problems that exist within models or data, as
demonstrated by [57], [71], [72]. However, successful detection
is not guaranteed. For example, Poursabzi-Sangdeh et al. [53]
show that users with model explanations are less able to identify
incorrect predictions. A limitation of current detection methods
is that users may have varying assessments, such as perceived
unfairness and irrelevance [53], [71], [73], regarding the features
used in models for decision-making. Due to this limitation, the
effectiveness of methods assessed through self-reported data
may face challenges in generalizability as discussed in [73].
Yet, these methods generally offer a one-size-ﬁts-all solution,
failing to account for variations in individual assessments.
Human-AI Collaboration Performance: A strain
[91],

of
[96] show that
works [25],
viewing explanations can improve human accuracy in making
decisions, especially with feature-based explanations taking
text data as input [25], [90], [91]. When using example-based
explanations in text classiﬁcation, there is no improvement
in human performance [25]. Likewise, utilizing explanations
has no signiﬁcant
impact on human performance in [89],
[92], but simply showing model predictions has a positive
in [92]. Experts and novices perceive explanations
effect
differently, for example, Feng and Boyd-Graber [91] conclude

[88],

[90],

[96],

[95],

VI. A GUIDELINE FOR XAI USER STUDY DESIGN

Learning from the best practices of the previous works, we
summarize a handy guideline for XAI user study, which serves
as a checklist for XAI practitioners. This guideline contains sug-
gestions to avoid pitfalls that researchers could easily overlook.
We introduce our guidelines in the order of before, during and
after user studies, which reﬂects user study design, execution
and data analysis, respectively.

Before the User Study: When designing a user study, the
ﬁrst step is to decide what to measure. To deﬁne the measured
quantities, one can consider two alternatives: using a general
deﬁnition or an application-based quantity that is speciﬁc to the
application at hand. The former one refers to a quantity that
is borrowed from previous well-established research, such as
using “trust in automation” [2], [3], [21] or “general trust in
technology” [7], [23]. To further construct “trust” as a quanti-
tative measurement, one needs to examine how existing work
has conceptualized “trust” in both social sciences context as
well as XAI and technical context [169]. The application-based
quantity depends on the application goal, for instance in a chess
game [88], the measurement is the human winning percentage
with the help of model explanations (Human-AI collaboration).
From Table V, we can see that previous works have frequently
struggled to prove the effectiveness of XAI even with respect to
a control group that is without explanation. When only different
explanation techniques are considered, there will always be
one winner explanation, but the overall beneﬁt will remain
undisclosed (see examples in Appendix D, available online).
Therefore, it is important to compare with a baseline without
explanations to rigorously show the strength of XAI. When
a comparative design is explicitly desired, baselines such as
random explanations [28], [41], [62]).

When deploying a proxy task, its difﬁculty should be gauged
and monitored carefully. In the past, the forward simulation task
has been criticized as being unrealistically complex for domains
such as computer vision [54]. Thus, other proxy tasks such as
feature importance queries [57] or manipulatability checks [32],
[50] were proposed. Another important point is to choose a proxy
task that is simpliﬁed, but features many characteristics of the
application in mind [119]. Notably, the proxy task should be
designed close to the ﬁnal anticipated application, as even slight
differences in the tasks may void the validity of the ﬁndings on
the proxy tasks in the real world [13].

The measurement is often dependent on the deﬁnition of
the measured quantity. For instance, in [58], the objective
understanding is measured as failure prediction (the accu-
racy of user prediction when the model prediction is wrong).
For subjective measurements such as subjective understand-
ing or trust, one-dimensional measures (i.e., simply rating one

---

<!-- PAGE 11 -->

2114

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

question such as “Do you trust the model explanation?”) have
the drawback that they cannot completely reﬂect different con-
structs of measured quantities [8]. Moreover, subjective ques-
tions and behavioral measurements often appear to be weakly
correlated. For example, the users state that they trust model but
they do not really follow the model suggestions [11]. Similar
ﬁndings have been made with respect to objective and subjective
understanding [12], [35], [40]. To overcome this limitation, both
self-reported and observed measures shall be used in parallel.

Besides the measures introduced in Section IV-B, there are
several psychological constructs that can be deployed to evaluate
multiple facets of the interaction between humans and XAI.
For instance, the subjective task value in the expectancy-value
framework is often used to analyze subjective motivation to take
any actions [170], which is not thoroughly studied in the XAI
experience yet. The subjective task value consists of intrinsic
value (enjoyment), attainment value (importance for one’s self),
utility value (usefulness), and cost (the amount of effort or time
needed) [170], [171]. A good explanation interface should be
positively correlated with the subjective task value, consequently
boosting one’s interest and motivation to use the model expla-
nation. With regard to the cost of using model explanations,
cognitive load is popularly measured in the current literature
with conventional Likert scales [162], [172]. Cognitive load
researchers study the validity of different visual appearances in
rating scales beyond numerical Likert scales, i.e., pictorial scales
such as emoticons (faces with different emotions), or embodied
pictures of different weights [173]. Their results demonstrate
that numerical scales are more proper in complex tasks while
pictorial scales are for simple ones.

Pre-registration using online platforms such as AsPredicted1
has become a common practice in recent years [174]. In this
process, researchers submit a document detailing their planned
study online before initiating the data collection. Among other
details, the pre-registration includes the measured variables and
hypotheses, data exclusion criteria, and the number of samples
that will be collected. An exhaustive pre-registration can provide
evidence against the ﬁndings being a result of selective reporting
or p-hacking [175] and thus strengthen the credibility of a study.
Expert interviews and pre-studies following a think-aloud proto-
col [176], e.g., in the references [32], [46], are often mentioned
as helpful tools to develop the explanation system and the study
design and gain ﬁrst qualitative insights or complement the
qualitative analysis [13], [65].

When preparing for a user study, it is important to plan for
explicit steps and to have a backup plan for different situations.
Before participants arrive, it is helpful to provide them with
information such as where the researchers will meet with them,
what they need to bring, and how they can prepare for the
study. If conducting the experiment in person, send participants
a reminder the day before and provide them with your contact in
case they cannot ﬁnd the experiment site or they need to cancel
the experiment session. Once participants arrive, make sure the
researchers have a plan that covers all stages of the experiment.
The protocol should cover small details (e.g., where participants

1[Online]. Available: https://aspredicted.org

should leave their backpacks, water bottles, and lunch boxes) and
plans for unexpected situations (e.g., uncooperative participants
and multifunctional systems). How to obtain participants’ con-
sent should be an important part of the procedure. Additional
procedure is required for obtaining consent when working with
vulnerable populations (e.g., children and pregnant women), in
which case alternative consent procedures might take place.
Another beneﬁt of pre-designing the experiment script is to
ﬁne-tune the language to avoid inadvertent cues. Researchers
can unintentionally pass on their expectations to participants
through verbal and nonverbal behavior, which might result
in participants’ skewed performance towards the researchers’
desire [169]. To ensure a sound experiment procedure and to
protect the integrity of the data, it is worthwhile to put in much
effort to design a detailed experiment script.

During the User Study: A sufﬁcient number of participants
is the prerequisite of a solid user study analysis. To get a rough
estimate of common sample sizes, we refer the reader to the
participant statistics in Fig. 2 where we analyze the subject
numbers in different experimental designs. For instance, around
350 users without any speciﬁc expertise are averagely recruited
in between-subject experiments. However, we would like to
underline that the required number of participants is highly spe-
ciﬁc to the study design and should be determined individually,
for instance by conducting a statistical power analysis [177].
Additionally, recruited participants should have the same knowl-
edge background as the end users that applications are designed
for. For instance, when evaluating an interface explaining loan
approval decisions to bank customers, it is not proper to include
only students whose major is computer science, since they may
have prior knowledge of how model explanations work. Note
that the design of an AI application requires different audiences
across the project cycle, thus model explanations need to evolve
as well [178].

To uphold high-quality standards of the collected data, atten-
tion or manipulation checks are essential to ﬁlter out careless
feedback. This particularly applies to long surveys or online
surveys with lay users. Kung et al. [179] justify the use of these
checks without compromising scale validity. In within-subject
experiments, a random order of conditions is necessary to avoid
order effect [1]. Participants can learn knowledge of data or
examples shown in the previous conditions, and Tsai et al. [6]
choose to use a Latin square design to avoid the learning effect.
After the User Study: After the data collection, statistical
tests are run to ﬁnd signiﬁcant effects. The applicable tests
used are determined by experimental designs and the form and
distribution of the data. Generally, ANOVA tests and T-test are
usually used when comparing distributions between different
conditions. Structural Equation Models (SEM) or multi-level
models are used for mediation analysis. More details of statistic
tools can be found in Section IV-C. Distributional assumption
checks should be applied. When Likert-type data is collected
as in most of the questionnaires, non-parametric tests such as
paired Wilcoxon signed-rank test, or Kruskal-Wallis H test for
multiple groups can be used to avoid normality assumptions.

If multiple measures are aggregated into a single instrument,
it is important to assess the validity of this aggregation with

---

<!-- PAGE 12 -->

RONG et al.: TOWARDS HUMAN-CENTERED EXPLAINABLE AI: A SURVEY OF USER STUDIES FOR MODEL EXPLANATIONS

2115

Fig. 3.

Summary cards of the guidelines extracted from past XAI user studies.

reliability measures such as the tau-equivalent reliability (also
known as Cronbach’s α). For example, if objective and subjec-
tive measures of a quantity, such as understanding are combined,
it is necessary to verify that there is sufﬁcient agreement. If
multiple items (e.g., data samples or visualizations) are rated
by several subjects, statistics such as Cohan’s κ as Fleiß’s κ
for more than two raters [180] can be used to assess agreement
beyond chance between these raters and serve as an indication
for the reliability of the ratings.

In the ﬁnal writing phase, it is essential to report sufﬁcient
details that allow readers to estimate the explanatory power of
the study. On the level of participants, this should include the
total number of participants and how many are assigned to each
treatment group, their recruitment, consent and incentivization,
and the exact treatment conditions they are subjected to. Further-
more, some descriptive statistics of the collected data can help
readers assess the characteristics of the adequacy of the statistical
tools used. Regarding the analysis, we found it important to
mention how the underlying assumptions of the statistical tests
used were checked and to mention the exact variant of the test
used (e.g., stating “a two-way ANOVA with the independent
variables X and Y” is used instead of just mentioning that
ANOVA-test is used).

VII. FUTURE RESEARCH DIRECTIONS

Our survey of recent and ongoing XAI research also helps
us identify research gaps and distill a few directions for future
investigations. In this section, we highlight these directions and
summarize our ﬁndings.

A. Towards Increasingly User-Centered XAI

We advocate that user-centered methods should be used not
only to assess XAI solutions (e.g., through user studies) but also
to design them (e.g., through user-centered design). By explicitly

modeling and involving users in the design phase and not just
in a post-hoc manner during the evaluation phase, we expect the
development of XAI solutions that better respond to user needs.
As discussed in [117], there are two aspects of human-centered
AI: (1) AI systems that understand humans with a sociocultural
background and (2) AI systems that help humans understand
them. The former point can guide the design of AI systems. In
this section, we discuss XAI research that leverages this insight.
The process of explaining a machine’s decisions to human
users can be viewed as a teaching-learning process where the
XAI system is the teacher and the human users are the students.
From a user-centered perspective, the problem of designing
effective teaching methods to enhance the student’s (i.e., user’s)
learning outcomes is essential to human-centered XAI algo-
rithms. To leverage the ability of humans and address unique
user’s needs, it is important to review studies and ﬁndings
from psychology and education. These studies provide insights
into how humans perceive other intelligent agents (humans or
artiﬁcial agents) and how they utilize limited information to
infer and generalize. Understanding how humans think and learn
will help XAI developers build and design systems that are not
only informative but also user-friendly to people with differ-
ent backgrounds. In this section, we discuss three pedagogical
frameworks, namely (1) the expectancy-value motivation theory,
(2) the theory of mind, and (3) hybrid teaching, to shed light
on incorporating such methods in computational approaches.
Inspired by existing work in pedagogy and XAI, we provide
implications for designing future transparent AI systems and
human-centered evaluations.

Expectancy-Value Motivation Theory: Human interaction
with XAI interfaces can be viewed as an activity where humans
learn about the model’s inner workings through explanations
and then achieve an understanding of the models. The question
of how to enhance the efﬁciency and the outcome of this human
learning process is of high importance [181]. This research

---

<!-- PAGE 13 -->

2116

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

problem is widely considered in educational psychology through
the lens of expectancy-value motivation theory. For instance,
Hulleman et al. [171] propose to utilize interventions to increase
the perception of usefulness (utility value) to subsequently in-
crease motivation and ﬁnal performance. Intervention here refers
to identifying the relevance of model explanations to the user’s
own situation, which can be a prompt question while working
with the interface. Moreover, when utilizing model explanations
in human-AI collaboration, explanations can be seen as a type of
“scaffolding” (prompt during a task) proposed in a conceptual
framework in education.

Theory of Mind: When interacting with XAI systems, humans
form mental models of the machine learning algorithms that
reﬂect their belief of how the algorithms work. The formation
of these mental models comes from observing explanations or
examples given to the human, who often subconsciously applies
the observations in a few examples to the broader understanding
of the whole machine learning system. This incredible ability
to infer, rationalize, and summarize other intelligent agent’s
decisions is known as the Theory of Mind (ToM) in psychology.
Based on this theory, the Bayesian Theory of Mind (BToM)
provides a probabilistic framework to predict inferences that
people make about mental states underlying other agents’ ac-
tions. Recent work, at the intersection of XAI and robotics,
indicates that humans also attribute ToM to artiﬁcial agents that
they observe or interact with. Guided by these user-centered
results, several works at the intersection of XAI and robotics
have utilized BToM to create a simulated user, and then use it to
generate helpful explanations.

Hybrid Teaching: Teaching strategies for the human-to-
human setting have been widely studied and many categoriza-
tions exist. One way of categorizing these strategies is through
the following three concepts: (1) direct teaching, (2) indirect
teaching, and (3) hybrid teaching. Direct teaching utilizes direct
instructions that are teacher-centered, involve clear teaching
objectives, and are consistent with classroom organizations. In
XAI applications, direct teaching methods generate explanations
by selecting representative examples of an agent’s decisions to
convey the patterns in its policy. In contrast, indirect teaching
is student-centered and encourages independent learning. In the
XAI perspective, methods utilizing indirect teaching provide
users with tools to actively and independently explore an AI sys-
tem. Technically, direct teaching focuses on providing guidance
(using a computational approach) to assist users in building an
understanding of a machine, whereas indirect teaching (often
through a user interface) enables users to address individual
learning preferences and mitigate individual confusion about the
AI. To leverage the advantages of the two teaching strategies, hy-
brid teaching has been widely used in human-to-human teaching
with an emphasis on interactivity. Recent work [182] indicates
that hybrid teaching reduces the amount of time for a user to
understand an agent’s policy compared to direct and indirect
teaching, and is more subjectively preferred by the participants.
Building on this, future XAI systems can consider using hybrid
teaching methods that (i) generate direct instructions to provide
guidance to user’s understanding of an AI system; and (ii)
provide methods to allow users to interact with the agent.

Explanations through Large Language Models (LLMs): The
recent rise of Large Language Models [183], [184] naturally
opens up new research directions. There is a growing interest
in leveraging their unprecedented capabilities [185] to offer
explanations for model decisions [186], [187]. Through their
natural language interface, LLMs offer the possibility to build
interactive explainers [188]. Intriguingly, textual explanations
can also be used as subsequent inputs to LLMs which may
help to solve subsequent problems and result in superior per-
formance [189]. This technique, referred to as chain-of-thought
reasoning [190], opens up an interesting research territory com-
bining interpretability and performance considerations.

B. Open Research Problems

1) Automatic versus Human-Subject Evaluations: With au-
tomatic evaluations, we refer to evaluation methods that do not
require human subjects, which corresponds to the functionally-
grounded metrics discussed in [119], [120]. These metrics aim
to test desiderata around the “faithfulness”/“ﬁdelity”/ “truthful-
ness” of model explanations [120], [121], [191]. Faithfulness of
explanations is deﬁned as that explanations are indicative of true
important features in the input [191]. The automatic evaluations
aim at capturing general objectivity which is independent from
downstream tasks, while human evaluations are contextualized
with speciﬁc use cases. Generally speaking, automatic evalu-
ations and human evaluations tackle different research chal-
lenges: the former objectively examines how truly explanations
reﬂect models and the latter one measures how humans perceive
models through explanations (although there existing algorithms
for automated evaluation designed to align with human evalu-
ations, which we will discuss later). All explanations used in
human-subject experiments should have satisfying performance
in automatic evaluations, i.e., the explanations should be able to
faithfully unbox the model. This veriﬁcation step is essential to
guarantee the validity of the empirical user study and to ensure
that users are not tricked by unfaithful explanations. However, in
most current human-subject experiments, the functional faith-
fulness of explanations is not thoroughly veriﬁed beforehand.
Using unfaithful explanations could lead to the problem that
only the placebo effect of explanations is measured. Ideally,
a good explanation should be faithful to the model as well as
understandable by users.

2) Identifying and Handling Confounders: Existing research
underscores the vulnerability of model explanation studies to
signiﬁcant confounding effects. For instance, Papenmeier et
al. [155] reveal that user trust can be more inﬂuenced by model
accuracy than the faithfulness of the explanation itself. Similarly,
Yin et al. [192] demonstrate that the accuracy score perceived
by users and the one shown to users contribute to trust formation.
A different problem is that good explanations also reveal
weaknesses of the model. However, when seeing unexpected
explanations, users may express their negative feelings about
the model through negative ratings of the explanations. There-
fore, good model explanations should help users calibrate their
trust [26], [193], i.e., trust the model’s decision when it is correct
but distrust it otherwise. There is a disagreement on how to

---

<!-- PAGE 14 -->

RONG et al.: TOWARDS HUMAN-CENTERED EXPLAINABLE AI: A SURVEY OF USER STUDIES FOR MODEL EXPLANATIONS

2117

handle such cases: When evaluating model fairness, several
works [2], [27], [38], [73], [75] reckon the increase in perceived
fairness as positive, while Dodge et al. [74] deﬁne the decrease
as positive. Other factors, such as the temporal occurrence of
model errors (Nourani et al. [56]), and the dimensions of models
(Ross et al. [32], Poursabzi et al. [53]), also come into play.

In summary, these confounding elements suggest that users
might be led to put more trust in oversimpliﬁed, deceptive,
or simply unfaithful explanations. To mitigate this, we rec-
ommend meticulous analysis, control and reporting of poten-
tial confounders, such as explanation faithfulness and model
accuracy, across various test conditions. More advanced mea-
sures have been suggested as well. For instance, Schoeffer and
Kuehl’s [79] propose appropriate fairness perceptions, which
measures whether people increase or decrease their fairness per-
ceptions depending on the algorithmic fairness of the underlying
model. Nevertheless, the thorough investigation of confounding
factors remains a challenge. Calibrated measures that are less
prone to confounding can be a valuable step forward.

3) Mitigating Personal Biases for XAI: Most XAI techniques
and corresponding designed user studies provide one-size-ﬁts-
all solutions. Individual bias, rooted in a user’s mental frame-
work, inﬂuences the user’s perception of a model. It should be
considered in XAI design, development, and evaluation proce-
dures. Several studies that aim to explain reinforcement learning
policies utilize cognitive science theories to create a model of
the human user [181], [182], [194], [195]. They then generate
explanations based on this human model and verify the beneﬁts
of tailoring explanations for individual user models. Within the
scope of XAI, [196], [197] utilize a Bayesian Teaching frame-
work to capture human perception of model explanations. In
user studies, depending on cultural and educational background,
participants may likely give different feedback [31]. This kind of
personal bias can be mitigated by deploying a large sample size
and recruiting participants who are representative of the target
audience. We advocate that personal biases should be taken into
account in the realm of XAI development.

4) Human-in-the-Loop and Sequential Explanations: In sev-
eral relevant cases, such as online recommendation systems,
users are not only confronted with an explanation once but
instead view decisions and potential explanations repeatedly.
Recent work in this domain [35] has shown that the order of
decisions and explanations may indeed have an effect on user
perception and understanding. The AI model may continue
to shape the user’s mental model over time. The differences
between the single-use and the sequential setting still remain to
be thoroughly investigated.

5) Proxy Tasks Should Be Close to Real-World Tasks: When
using proxy tasks to evaluate models, for instance, to measure
subjective understanding, there is a great choice of tasks present
in the literature. A good proxy task should have the following
features: (1) it has close real-world connections [119]; (2) users
or participants have some background knowledge of the task
but not too much to affect their judgment or performance during
the task; (3) the task is not too complicated to implement or
there exists an existing implementation but was used for different
purposes (i.e., not used for XAI); and (4) it has connections to

existing work. Yet, the link between evaluations through differ-
ent proxy tasks and real-world applications has not been made
very explicit to date. Buçinca et al. [13] show that the outcomes
of proxy evaluations can be different from a real-world task.
More speciﬁcally, the widely accepted proxy tasks, where users
are asked to build the mental models of the AI, may not predict
the performance in actual decision-making tasks, where users
make use of the explanations to assist in making decisions. The
results show that users trust different explanations in the proxy
task and the actual decision-making task. Therefore, we argue
that further research is required to uncover the links between
current proxy tasks and on-task performance or to devise new
proxy tasks with a veriﬁed connection to actual tasks.

6) Simulated Evaluation as a Cost-Efﬁcient Solution: As
human-subject experiments are costly to conduct, Chen
et al.
[198] propose a simulated evaluation framework
(SimEvals) to select potential explanations for user studies by
measuring the predictive information provided by explanations.
Concretely, the authors consider three use cases where model
explanations are deployed: forward simulation, counterfactual
reasoning, and data debugging. Human performance is measured
for these three tasks with different explanations. If there is a
signiﬁcant gap in settings of using two types of explanations,
the simulated evaluation can also observe such a gap under the
same task settings as well. Meanwhile, ﬁrst attempts to simulate
human textual responses in a given context using large language
models show that models can provide surprisingly anthropomor-
phic answers [199]. Undoubtedly and also afﬁrmed by Chen et
al. [198], it is not yet realistic to replace human evaluation with
the simulated framework as other factors e.g., cognitive biases
can affect human decisions. To better simulate human evalua-
tions, more effort should be directed towards modeling human
cognitive processes. Concurrently and with appropriate caveats,
XAI researchers should also leverage existing and approximate
models of human cognition to enable rapid prototyping and
assessment of explanations. Section VII-A discusses several
candidate human cognition models and highlights recent XAI
works [181], [182] that utilize this “Oz-of-Wizard” paradigm.

VIII. CONCLUSION

In recent years, there has been a proliferation of XAI research
in both academia and industry. Explainability is a human-centric
property [141] and therefore XAI should be preferably studied
by taking humans’ feedback into account. In this work, we
investigated recent user studies for XAI techniques through a
principled literature review. Based on our review, we found
out that the effectiveness of XAI in users’ interaction with
ML models was not consistent across different applications,
thus suggesting that there is a strong need for more transparent
and comparable human-based evaluations in XAI. Furthermore,
relevant disciplines, such as cognitive psychology and social
sciences in general, should become an integral part of XAI
research.

We comprehensively analyzed the design patterns and ﬁnd-
ings from previous works. Based on best-practice approaches
and measured quantities, we propose a general guideline for

---

<!-- PAGE 15 -->

2118

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

human-centered user studies and several future research direc-
tions for XAI researchers and practitioners. Thereby, this work
represents a starting point for more transparent and human-
centered XAI research.

REFERENCES

[1] C. Panigutti, A. Beretta, F. Giannotti, and D. Pedreschi, “Understanding
the impact of explanations on advice-taking: A user study for AI-based
clinical decision support systems,” in Proc. SIGCHI Conf. Hum. Factors
Comput. Syst., 2022, pp. 1–9.

[2] A. I. Anik and A. Bunt, “Data-centric explanations: Explaining training
data of machine learning systems to promote transparency,” in Proc.
SIGCHI Conf. Hum. Factors Comput. Syst., 2021, pp. 1–13.

[3] M. Colley, B. Eder, J. O. Rixen, and E. Rukzio, “Effects of semantic
segmentation visualization on trust, situation awareness, and cognitive
load in highly automated vehicles,” in Proc. SIGCHI Conf. Hum. Factors
Comput. Syst., 2021, pp. 1–1.

[4] U. Ehsan, Q. V. Liao, M. Muller, M. O. Riedl, and J. D. Weisz, “Expanding
explainability: Towards social transparency in ai systems,” in Proc.
SIGCHI Conf. Hum. Factors Comput. Syst., 2021, pp. 1–19.

[5] M. Liao and S. S. Sundar, “How should AI systems talk to users
when collecting their personal information? effects of role framing and
self-referencing on Human-AI interaction,” in Proc. SIGCHI Conf. Hum.
Factors Comput. Syst., 2021, pp. 1–14.

[6] C.-H. Tsai, Y. You, X. Gui, Y. Kou, and J. M. Carroll, “Exploring and
promoting diagnostic transparency and explainability in online symptom
checkers,” in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2021,
pp. 1–17.

[7] L. Guo, E. M. Daly, O. Alkan, M. Mattetti, O. Cornec, and B. Knijnen-
burg, “Building trust in interactive machine learning via user contributed
interpretable rules,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2022,
pp. 537–548.

[8] J. Ooge, S. Kato, and K. Verbert, “Explaining recommendations in E-
learning: Effects on adolescents’ trust,” in Proc. ACM Int. Conf. Intell.
User Interfaces, 2022, pp. 93–105.

[9] H. Suresh, K. M. Lewis, J. Guttag, and A. Satyanarayan, “Intuitively
assessing ML model reliability through example-based explanations and
editing model inputs,” in Proc. ACM Int. Conf. Intell. User Interfaces,
2022, pp. 767–781.

[10] R. Paleja, M. Ghuy, N. Ranawaka Arachchige, R. Jensen, and M. Gom-
bolay, “The utility of explainable AI in ad hoc human-machine teaming,”
in Proc. Int. Conf. Neural Inf. Process. Syst., vol. 34, 2021, pp. 610–623.
[11] J. Schaffer, J. O’Donovan, J. Michaelis, A. Raglin, and T. Höllerer, “I
can do better than your AI: Expertise and explanations,” in Proc. ACM
Int. Conf. Intell. User Interfaces, 2019, pp. 240–251.

[12] X. Wang and M. Yin, “Are explanations helpful? A comparative study
of the effects of explanations in AI-assisted decision-making,” in Proc.
ACM Int. Conf. Intell. User Interfaces, 2021, pp. 318–328.

[13] Z. Buçinca, P. Lin, K. Z. Gajos, and E. L. Glassman, “Proxy tasks
and subjective measures can be misleading in evaluating explainable
AI systems,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2020,
pp. 454–464.

[14] X. Peng, M. Riedl, and P. Ammanabrolu, “Inherently explainable rein-
forcement learning in natural language,” in Proc. Int. Conf. Neural Inf.
Process. Syst., 2022, pp. 16178–16190.

[15] Y. Zhang, Q. V. Liao, and R. K. Bellamy, “Effect of conﬁdence and
explanation on accuracy and trust calibration in AI-assisted decision
making,” in Proc. Conf. Fairness Accountability Transparency, 2020,
pp. 295–305.

[16] V. Dominguez, P. Messina, I. Donoso-Guzmán, and D. Parra, “The effect
of explanations and algorithmic accuracy on visual recommender systems
of artistic images,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2019,
pp. 408–446.

[17] C. J. Cai, J. Jongejan, and J. Holbrook, “The effects of example-based
explanations in a machine learning interface,” in Proc. ACM Int. Conf.
Intell. User Interfaces, 2019, pp. 258–262.

[18] M. Millecamp, N. N. Htun, C. Conati, and K. Verbert, “To explain or not
to explain: The effects of personal characteristics when explaining music
recommendations,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2019,
pp. 397–407.

[19] C.-H. Tsai and P. Brusilovsky, “Beyond the ranked list: User-driven
exploration and diversiﬁcation of social recommendation,” in Proc. ACM
Int. Conf. Intell. User Interfaces, 2018, pp. 239–250.

[20] T. Li, G. Convertino, R. K. Tayi, and S. Kazerooni, “What data should I
protect? recommender and planning support for data security analysts,”
in Proc. ACM Int. Conf. Intell. User Interfaces, 2019, pp. 286–297.
[21] H. Kaur, H. Nori, S. Jenkins, R. Caruana, H. Wallach, and J. Wortman
Vaughan, “Interpreting interpretability: Understanding data scientists’
use of interpretability tools for machine learning,” in Proc. SIGCHI Conf.
Hum. Factors Comput. Syst., 2020, pp. 1–14.

[22] H.-F. Cheng et al., “Explaining decision-making algorithms through UI:
Strategies to help non-expert stakeholders,” in Proc. SIGCHI Conf. Hum.
Factors Comput. Syst., 2019, pp. 1–12.

[23] J. Kunkel, T. Donkers, L. Michael, C.-M. Barbu, and J. Ziegler, “Let
me explain: Impact of personal and impersonal explanations on trust in
recommender systems,” in Proc. SIGCHI Conf. Hum. Factors Comput.
Syst., 2019, pp. 1–12.

[24] D. H. Kim, E. Hoque, and M. Agrawala, “Answering questions about
charts and generating visual explanations,” in Proc. SIGCHI Conf. Hum.
Factors Comput. Syst., 2020, pp. 1–13.

[25] V. Lai and C. Tan, “On human predictions with explanations and pre-
dictions of machine learning models: A case study on deception detec-
tion,” in Proc. ACM Conf. Fairness Accountability Transparency, 2019,
pp. 1–13.

[26] Y. Rong, N. Castner, E. Bozkir, and E. Kasneci, “User

on an explainable ai-based medical diagnosis
2022, arXiv:2204.12230.

support

trust
system,”

[27] J. Schoeffer, N. Kuehl, and Y. Machowski, ““there is not enough in-
formation”: On the effects of explanations on perceptions of infor-
mational fairness and trustworthiness in automated decision-making,”
2022, arXiv:2205.05758.

[28] U. Ehsan, P. Tambwekar, L. Chan, B. Harrison, and M. O. Riedl, “Auto-
mated rationale generation: A technique for explainable AI and its effects
on human perceptions,” in Proc. ACM Int. Conf. Intell. User Interfaces,
2019, pp. 263–274.

[29] A. Smith-Renner et al., “No explainability without accountability: An
empirical study of explanations and feedback in interactive ML,” in Proc.
SIGCHI Conf. Hum. Factors Comput. Syst., 2020, pp. 1–13.

[30] A. Smith-Renner, V. Kumar, J. Boyd-Graber, K. Seppi, and L. Findlater,
“Digging into user control: Perceptions of adherence and instability in
transparent models,” in Proc. ACM Int. Conf. Intell. User Interfaces,
2020, pp. 519–530.

[31] A. Springer and S. Whittaker, “Progressive disclosure: Empirically moti-
vated approaches to designing effective transparency,” in Proc. ACM Int.
Conf. Intell. User Interfaces, 2019, pp. 107–120.

[32] A. Ross, N. Chen, E. Z. Hang, E. L. Glassman, and F. Doshi-Velez,
“Evaluating the interpretability of generative models by interactive re-
construction,” in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2021,
pp. 1–15.

[33] M. Radensky, D. Downey, K. Lo, Z. Popovic, and D. S. Weld, “Exploring
the role of local and global explanations in recommender systems,” in
Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2022, pp. 1–7.
[34] S. Hadash, M. C. Willemsen, C. Snijders, and W. A. IJsselsteijn, “Im-
proving understandability of feature contributions in model-agnostic
explainable AI tools,” in Proc. SIGCHI Conf. Hum. Factors Comput.
Syst., 2022, pp. 1–9.

[35] M. Chromik, M. Eiband, F. Buchner, A. Krüger, and A. Butz, “I think I
get your point, AI! the illusion of explanatory depth in explainable AI,”
in Proc. ACM Int. Conf. Intell. User Interfaces, 2021, pp. 307–317.
[36] J. Rebanal, J. Combitsis, Y. Tang, and X. Chen, “XAlgo: A design probe
of explaining algorithms’ internal states via question-answering,” in Proc.
ACM Int. Conf. Intell. User Interfaces, 2021, pp. 329–339.

[37] U. Kuhl, A. Artelt, and B. Hammer, “Keep your friends close and
your counterfactuals closer: Improved learning from closest rather
than plausible counterfactual explanations in an abstract setting,”
2022, arXiv:2205.05515.

[38] E. Rader, K. Cotter, and J. Cho, “Explanations as mechanisms for sup-
porting algorithmic transparency,” in Proc. SIGCHI Conf. Hum. Factors
Comput. Syst., 2018, pp. 1–13.

[39] A. Bell, I. Solano-Kamaiko, O. Nov, and J. Stoyanovich, “It’s just not
that simple: An empirical study of the accuracy-explainability trade-off
in machine learning for public policy,” in Proc. ACM Conf. Fairness
Accountability Transparency, 2022, pp. 248–266.

[40] P. Hase and M. Bansal, “Evaluating explainable AI: Which algorithmic
explanations help users predict model behavior?,” in Proc. 58th Annu.
Meeting Assoc. Comput. Linguistics, 2020, pp. 5540–5552.

[41] H. Schuff, A. Jacovi, H. Adel, Y. Goldberg, and N. T. Vu,
text,”

saliency-based explanation over

“Human interpretation of
2022, arXiv:2201.11569, .

---

<!-- PAGE 16 -->

RONG et al.: TOWARDS HUMAN-CENTERED EXPLAINABLE AI: A SURVEY OF USER STUDIES FOR MODEL EXPLANATIONS

2119

[42] S. Bang, P. Xie, H. Lee, W. Wu, and E. Xing, “Explaining a black-box
by using a deep variational information bottleneck approach,” in Proc.
AAAI Conf. Artif. Intell., 2021, pp. 11396–11404.

[43] S. S. Kim, N. Meister, V. V. Ramaswamy, R. Fong, and O. Russakovsky,
“HIVE: Evaluating the human interpretability of visual explanations,” in
Proc. Eur. Conf. Comput. Vis., 2022, pp. 280–298.

[44] M. Szymanski, M. Millecamp, and K. Verbert, “Visual, textual or hybrid:
The effect of user expertise on different explanations,” in Proc. ACM Int.
Conf. Intell. User Interfaces, 2021, pp. 109–119.

[45] G. Plumb, M. Al-Shedivat, Á. A. Cabrera, A. Perer, E. Xing, and A. Tal-
walkar, “Regularizing black-box models for improved interpretability,”
in Proc. Int. Conf. Neural Inf. Process. Syst., 2020, pp. 10526–10536.

[46] W. Zhang and B. Y. Lim, “Towards relatable explainable ai with the
perceptual process,” in Proc. SIGCHI Conf. Hum. Factors Comput. Syst.,
2022, pp. 1–24.

[47] C. Bove, J. Aigrain, M.-J. Lesot, C. Tijus, and M. Detyniecki, “Con-
textualization and exploration of local feature importance explanations
to improve understanding and satisfaction of non-expert users,” in Proc.
ACM Int. Conf. Intell. User Interfaces, 2022, pp. 807–819.

[48] A. Abdul, C. von der Weth, M. Kankanhalli, and B. Y. Lim, “COGAM:
Measuring and moderating cognitive load in machine learning model
explanations,” in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2020,
pp. 1–14.

[49] K. Natesan Ramamurthy, B. Vinzamuri, Y. Zhang, and A. Dhurandhar,
“Model agnostic multilevel explanations,” in Proc. Int. Conf. Neural Inf.
Process. Syst., 2020, pp. 5968–5979.

[50] S. Arora, D. Pruthi, N. Sadeh, W. W. Cohen, Z. C. Lipton, and G.
Neubig, “Explain, edit, and understand: Rethinking user study design
for evaluating model explanations,” in Proc. AAAI Conf. Artif. Intell.,
2022, pp. 5277–5285.

[51] J. Antoran, U. Bhatt, T. Adel, A. Weller, and J. M. Hern ández-Lobato,
“Getting a {clue}: A method for explaining uncertainty estimates,” in
Proc. Int. Conf. Learn. Representations, 2021.

[52] J. Borowski et al., “Exemplary natural images explain {CNN} activations
better than state-of-the-art feature visualization,” in Proc. Int. Conf.
Learn. Representations, 2021.

[53] F. Poursabzi-Sangdeh, D. G. Goldstein, J. M. Hofman, J. W. Wortman
Vaughan, and H. Wallach, “Manipulating and measuring model inter-
pretability,” in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2021,
pp. 1–52.

[54] A. Alqaraawi, M. Schuessler, P. Weiß, E. Costanza, and N. Berthouze,
“Evaluating saliency map explanations for convolutional neural net-
works: A user study,” in Proc. ACM Int. Conf. Intell. User Interfaces,
2020, pp. 275–285.

[55] M. T. Ribeiro, S. Singh, and C. Guestrin, “Anchors: High-precision
model-agnostic explanations,” in Proc. AAAI Conf. Artif. Intell., 2018,
pp. 1527–1535.

[56] M. Nourani et al., “Anchoring bias affects mental model formation and
user reliance in explainable ai systems,” in Proc. ACM Int. Conf. Intell.
User Interfaces, 2021, pp. 340–350.

[57] L. Sixt, M. Schuessler, O.-I. Popescu, P. Weiß, and T. Landgraf, “Do users
beneﬁt from interpretable vision? a user study, baseline, and dataset,” in
Proc. Int. Conf. Learn. Representations, 2022.

[58] A. Chandrasekaran, V. Prabhu, D. Yadav, P. Chattopadhyay, and D.
Parikh, “Do explanations make VQA models more predictable to
a human?,” in Proc. Conf. Empir. Methods Natural Lang. Process.,
2018, pp. 1036–1042.

[59] J. Colin, T. Fel, R. Cadene, and T. Serre, “What I cannot predict, I do
not understand: A human-centered evaluation framework for explain-
ability methods,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2022,
pp. 2832–2845.

[60] H. Shen and T.-H. Huang, “How useful are the machine-generated
interpretations to general users? a human evaluation on guessing the
incorrectly predicted labels,” in Proc. AAAI Conf. Hum. Comput. Crowd-
sourcing, 2020, pp. 168–172.

[61] C.-K. Yeh, B. Kim, S. O. Arik, C.-L. Li, T. Pﬁster, and P. Raviku-
mar, “On completeness-aware concept-based explanations in deep neu-
ral networks,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2019,
pp. 20554–20565.

[62] A. Ghorbani, J. Wexler, J. Y. Zou, and B. Kim, “Towards automatic
concept-based explanations,” in Proc. Int. Conf. Neural Inf. Process. Syst.,
2019, pp. 9277–9286.

[63] T. Leemann, Y. Rong, S. Kraft, E. Kasneci, and G. Kasneci, “Coherence
evaluation of visual concepts with objects and language,” in Proc. Int.
Conf. Learn. Representations WS, 2022.

[64] I. Laina, R. Fong, and A. Vedaldi, “Quantifying learnability and de-
scribability of visual concepts emerging in representation learning,”
Adv. Neural Inf. Process. Syst., vol. 33, 2020, pp. 13112–13126.
[65] Y. Wang, P. Venkatesh, and B. Y. Lim, “Interpretable directed di-
versity: Leveraging model explanations for iterative crowd ideation,”
in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2022,
pp. 1–28.

[66] D. L. Arendt, N. Nur, Z. Huang, G. Fair, and W. Dou, “Parallel embed-
dings: A visualization technique for contrasting learned representations,”
in Proc. ACM Int. Conf. Intell. User Interfaces, 2020, pp. 259–274.
[67] W. Zhang, M. Dimiccoli, and B. Y. Lim, “Debiased-CAM to mitigate im-
age perturbations with faithful visual explanations of machine learning,”
in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2022, pp. 1–32.
[68] J. Gao, X. Wang, Y. Wang, and X. Xie, “Explainable recommendation
through attentive multi-view learning,” in Proc. AAAI Conf. Artif. Intell.,
2019, pp. 3622–3629.

[69] P. Kouki, J. Schaffer, J. Pujara, J. O’Donovan, and L. Getoor, “Personal-
ized explanations for hybrid recommender systems,” in Proc. ACM Int.
Conf. Intell. User Interfaces, 2019, pp. 379–390.

[70] C.-H. Tsai and P. Brusilovsky, “Explaining recommendations in an
interactive hybrid social recommender,” in Proc. ACM Int. Conf. Intell.
User Interfaces, 2019, pp. 391–396.

[71] A. Balayn, N. Rikalo, C. Loﬁ, J. Yang, and A. Bozzon, “How can
explainability methods be used to support bug identiﬁcation in computer
vision models?,” in Proc. SIGCHI Conf. Hum. Factors Comput. Syst.,
2022, pp. 1–16.

[72] K. Rawal and H. Lakkaraju, “Beyond individualized recourse: Inter-
pretable and interactive summaries of actionable recourses,” in Proc. Int.
Conf. Neural Inf. Process. Syst., 2020, pp. 12187–12198.

[73] N. Grgi´c-Hlaˇca, E. M. Redmiles, K. P. Gummadi, and A. Weller, “Human
perceptions of fairness in algorithmic decision making: A case study of
criminal risk prediction,” in Proc. Wide Web Conf., 2018, pp. 903–912.
[74] J. Dodge, Q. V. Liao, Y. Zhang, R. K. Bellamy, and C. Dugan, “Explaining
models: An empirical study of how explanations impact fairness judg-
ment,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2019, pp. 275–285.
[75] G. Harrison, J. Hanson, C. Jacinto, J. Ramirez, and B. Ur, “An empirical
study on the perceived fairness of realistic, imperfect machine learning
models,” in Proc. Conf. Fairness Accountability Transparency, 2020,
pp. 392–402.

[76] C. Wang et al., “Do humans prefer debiased AI algorithms? a case study in
career recommendation,” in Proc. ACM Int. Conf. Intell. User Interfaces,
2022, pp. 134–147.

[77] N. N. Htun, E. Lecluse, and K. Verbert, “Perception of fairness in group
music recommender systems,” in Proc. ACM Int. Conf. Intell. User
Interfaces, 2021, pp. 302–306.

[78] R. Binns, M. Van Kleek, M. Veale, U. Lyngs, J. Zhao, and N. Shadbolt,
“‘it’s reducing a human being to a percentage’ perceptions of justice in
algorithmic decisions,” in Proc. SIGCHI Conf. Hum. Factors Comput.
Syst., 2018, pp. 1–14.

[79] J. Schoeffer and N. Kuehl, “Appropriate fairness perceptions? on the
effectiveness of explanations in enabling people to assess the fairness
of automated decision systems,” in Proc. Companion: Companion Pub.
Conf. Comput. Supported Cooperative Work Social Comput., 2021,
pp. 153–157.

[80] T. Donkers, T. Kleemann, and J. Ziegler, “Explaining recommendations
by means of aspect-based transparent memories,” in Proc. ACM Int. Conf.
Intell. User Interfaces, 2020, pp. 166–176.

[81] F. Hohman, A. Head, R. Caruana, R. DeLine, and S. M. Drucker, “Gamut:
A design probe to understand how data scientists understand machine
learning models,” in Proc. SIGCHI Conf. Hum. Factors Comput. Syst.,
2019, pp. 1–13.

[82] U. Kuhl, A. Artelt, and B. Hammer, “Let’s go to the alien zoo: Intro-
ducing an experimental framework to study usability of counterfactual
explanations for machine learning,” 2022, arXiv:2205.03398.

[83] T. Schneider, J. Hois, A. Rosenstein, S. Ghellal, D. Theofanou-Fülbier,
and A. R. Gerlicher, “ExplAIn yourself! transparency for positive UX
in autonomous driving,” in Proc. SIGCHI Conf. Hum. Factors Comput.
Syst., 2021, pp. 1–12.

[84] S. Choi, K. Aizawa, and N. Sebe, “FontMatcher: Font image paring for
harmonious digital graphic design,” in Proc. ACM Int. Conf. Intell. User
Interfaces, 2018, pp. 37–41.

[85] P. Le Bras, D. A. Robb, T. S. Methven, S. Padilla, and M. J. Chantler,
“Improving user conﬁdence in concept maps: Exploring data driven
explanations,” in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2018,
pp. 1–13.

---

<!-- PAGE 17 -->

2120

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

[86] R. Shang, K. K. Feng, and C. Shah, “Why am I not seeing it? under-
standing users’ needs for counterfactual explanations in everyday recom-
mendations,” in Proc. ACM Conf. Fairness Accountability Transparency,
2022, pp. 1330–1340.

[87] J. Dodge, A. A. Anderson, M. Olson, R. Dikkala, and M. Burnett, “How
do people rank multiple mutant agents?,” in Proc. ACM Int. Conf. Intell.
User Interfaces, 2022, pp. 191–211.

[88] D. Das and S. Chernova, “Leveraging rationales to improve human task
performance,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2020,
pp. 510–518.

[89] G. Bansal et al., “Does the whole exceed its parts? the effect of ai
explanations on complementary team performance,” in Proc. SIGCHI
Conf. Hum. Factors Comput. Syst., 2021, pp. 1–16.

[90] V. Lai, H. Liu, and C. Tan, ““why is’ Chicago’deceptive?,” towards
building model-driven tutorials for humans,” in Proc. SIGCHI Conf. Hum.
Factors Comput. Syst., 2020, pp. 1–13.

[91] S. Feng and J. Boyd-Graber, “What can ai do for me? evaluating machine
learning interpretations in cooperative play,” in Proc. ACM Int. Conf.
Intell. User Interfaces, 2019, pp. 229–239.

[92] Y. Alufaisan, L. R. Marusich, J. Z. Bakdash, Y. Zhou, and M. Kantar-
cioglu, “Does explainable artiﬁcial intelligence improve human decision-
making?,” in Proc. AAAI Conf. Artif. Intell., 2021, pp. 6618–6626.
[93] K. Z. Gajos and L. Mamykina, “Do people engage cognitively with AI?
impact of AI assistance on incidental learning,” in Proc. ACM Int. Conf.
Intell. User Interfaces, 2022, pp. 794–806.

[94] M. Liao, S. S. Sundar, and J. B. Walther, “User trust in recommenda-
tion systems: A comparison of content-based, collaborative and demo-
graphic ﬁltering,” in Proc. CHI Conf. Hum. Factors Comput. Syst., 2022,
pp. 1–14.

[95] G. Nguyen, D. Kim, and A. Nguyen, “The effectiveness of feature
attribution methods and its correlation with automatic evaluation scores,”
in Proc. Int. Conf. Neural Inf. Process. Syst., 2021, pp. 26422–26436.

[96] M. R. Taesiri, G. Nguyen, and A. Nguyen, “Visual correspondence-based
explanations improve AI robustness and human-AI team accuracy,” in
Proc. Int. Conf. Neural Inf. Process. Syst., 2022, pp. 34287–34301.
[97] J. Wei, J. He, K. Chen, Y. Zhou, and Z. Tang, “Collaborative ﬁltering and
deep learning based recommendation system for cold start items,” Expert
Syst. Appl., vol. 69, pp. 29–39, 2017.

[98] S. Yang, M. Korayem, K. AlJadda, T. Grainger, and S. Natarajan, “Com-
bining content-based and collaborative ﬁltering for job recommendation
system: A cost-sensitive statistical relational learning approach,” Knowl.-
Based Syst., vol. 136, pp. 37–45, 2017.

[99] Y. Zhang, X. Chen, Q. Ai, L. Yang, and W. B. Croft, “Towards conversa-
tional search and recommendation: System ask, user respond,” in Proc.
ACM Int. Conf. Inf. Knowl. Manage., 2018, pp. 177–186.

[100] S. Grigorescu, B. Trasnea, T. Cocias, and G. Macesanu, “A survey of deep
learning techniques for autonomous driving,” J. Field Robot., vol. 37,
pp. 362–386, 2020.

[101] H. Cui et al., “Multimodal trajectory predictions for autonomous driving
using deep convolutional networks,” in Proc. Int. Conf. Robot. Automat.,
2019, pp. 2090–2096.

[102] Y. Rong, C. Han, C. Hellert, A. Loyal, and E. Kasneci, “Artiﬁcial
intelligence methods in in-cabin use cases: A survey,” IEEE Intell. Transp.
Syst. Mag., vol. 14, no. 3, pp. 132–145, May/Jun. 2021.

[103] R. R. Murphy, “Introduction to AI robotics,” Ind. Robot: An Int. J., vol. 28,

no. 3, pp. 266–267, 2001.

[104] K. Rajan and A. Safﬁotti, “Towards a science of integrated AI and

robotics,” Artif. Intell., vol. 247, pp. 1–9, 2017.

[105] S. Wachter, B. Mittelstadt, and L. Floridi, “Transparent, explainable, and
accountable AI for robotics,” Sci. Robot., vol. 2, 2017, Art. no. eaan6080.
[106] S. H. Park and K. Han, “Methodologic guide for evaluating clinical
performance and effect of artiﬁcial intelligence technology for medical
diagnosis and prediction,” Radiology, vol. 286, pp. 800–809, 2018.
[107] J. A. Sidey-Gibbons and C. J. Sidey-Gibbons, “Machine learning in
medicine: A practical introduction,” BMC Med. Res. Methodol., vol. 19,
2019, Art. no. 64.

[108] R. Vaishya, M. Javaid, I. H. Khan, and A. Haleem, “Artiﬁcial intelli-
gence (AI) applications for COVID-19 pandemic,” Diabetes Metabolic
Syndrome: Clin. Res. Rev., vol. 14, pp. 337–339, 2020.

[109] X. Dastile, T. Celik, and M. Potsane, “Statistical and machine learning
models in credit scoring: A systematic literature survey,” Appl. Soft
Comput., vol. 91, 2020, Art. no. 106263.

[110] M. Ala’raj, M. F. Abbod, M. Majdalawieh, and L. Jum’a, “A deep learning
model for behavioural credit scoring in banks,” Neural Comput. Appl.,
vol. 34, pp. 5839–5866, 2022.

[111] P. M. Addo, D. Guegan, and B. Hassani, “Credit risk analysis using

machine and deep learning models,” Risks, vol. 6, no. 2, p. 38, 2018.

[112] N. Van Berkel, J. Goncalves, D. Hettiachchi, S. Wijenayake, R. M.
Kelly, and V. Kostakos, “Crowdsourcing perceptions of fair predictors for
machine learning: A recidivism case study,” in Proc. ACM Hum.-Comput.
Interact., vol. 3, pp. 1–21, 2019.

[113] T. Sourdin, “Judge V robot?: Artiﬁcial intelligence and judicial decision-
making,” Univ. New South Wales Law J., vol. 41, no. 4, pp. 1114–1133,
2018.

[114] M. Raghavan, S. Barocas, J. Kleinberg, and K. Levy, “Mitigating bias
in algorithmic hiring: Evaluating claims and practices,” in Proc. Conf.
Fairness Accountability Transparency, 2020, pp. 469–481.

[115] P. Tambe, P. Cappelli, and V. Yakubovich, “Artiﬁcial intelligence in hu-
man resources management: Challenges and a path forward,” California
Manage. Rev., vol. 61, pp. 15–42, 2019.

[116] D. Castelvecchi, “Can we open the black box of AI?,” Nature News,

vol. 538, pp. 20–23, 2016.

[117] M. O. Riedl, “Human-centered artiﬁcial intelligence and machine learn-

ing,” Hum. Behav. Emerg. Technol., vol. 1, pp. 33–36, 2019.

[118] U. Ehsan and M. O. Riedl, “Human-centered explainable AI: Towards a
reﬂective sociotechnical approach,” in Proc. Int. Conf. Human-Comput.
Interact., 2020, pp. 449–466.

[119] F. Doshi-Velez and B. Kim, “Towards a rigorous science of interpretable

machine learning,” 2017, arXiv: 1702.08608.

[120] M. Nauta et al., “From anecdotal evidence to quantitative evaluation
methods: A systematic review on evaluating explainable AI,” ACM
Comput. Surv., vol. 55, pp. 1–42, 2023.

[121] R. Tomsett, D. Harborne, S. Chakraborty, P. Gurram, and A. Preece,
“Sanity checks for saliency metrics,” in Proc. AAAI Conf. Artif. Intell.,
2020, pp. 6021–6029.

[122] Y. Rong, T. Leemann, V. Borisov, G. Kasneci, and E. Kasneci, “A
consistent and efﬁcient evaluation strategy for attribution methods,” in
Proc. Int. Conf. Mach. Learn., 2022, pp. 18770–18795.

[123] D. Nguyen, “Comparing automatic and human evaluation of lo-
cal explanations for text classiﬁcation,” in Proc. Conf. North Amer.
Chapter Assoc. Comput. Linguistics: Hum. Lang. Technol., 2018,
pp. 1069–1078.

[124] G. Hoffman, “Evaluating ﬂuency in human–robot collaboration,” IEEE
Trans. Human-Mach. Syst., vol. 49, no. 3, pp. 209–218, Jun. 2019.
[125] Workshop, “ExSS-ATEC: Explainable smart systems for algorithmic
transparency in emerging technologies,” in Proc. 25th Int. Conf. Intell.
User Interfaces Companion, vol. 1, 2020.

[126] S. Mohseni, N. Zarei, and E. D. Ragan, “A multidisciplinary survey and
framework for design and evaluation of explainable AI systems,” ACM
Trans. Interact. Intell. Syst. (TiiS), vol. 11, no. 3/4, pp. 1–45, 2021.
[127] Q. Yang, N. Banovic, and J. Zimmerman, “Mapping machine learning ad-
vances from HCI research to reveal starting places for design innovation,”
in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2018, pp. 1–11.

[128] A. Adadi and M. Berrada, “Peeking inside the black-box: A survey on
explainable artiﬁcial intelligence (XAI),” IEEE Access, vol. 6, pp. 52138–
52160, 2018.

[129] A. B. Arrieta et al., “Explainable artiﬁcial intelligence (XAI): Concepts,
taxonomies, opportunities and challenges toward responsible AI,” Inf.
Fusion, 2020, vol. 58, pp. 82–115.

[130] W. Samek and K.-R. Müller, “Towards explainable artiﬁcial intelli-
gence,” in Proc. Explainable AI: Interpreting Explaining Visualizing
Deep Learn., 2019, pp. 5–22.

[131] N. Burkart and M. F. Huber, “A survey on the explainability of supervised
machine learning,” J. Artif. Intell. Res., vol. 70, pp. 245–317, 2021.
[132] D. V. Carvalho, E. M. Pereira, and J. S. Cardoso, “Machine learning
interpretability: A survey on methods and metrics,” Electronics, vol. 8,
2019, Art. no. 832.

[133] L. H. Gilpin, D. Bau, B. Z. Yuan, A. Bajwa, M. Specter, and L. Ka-
gal, “Explaining explanations: An overview of interpretability of ma-
chine learning,” in Proc. IEEE 5th Int. Conf. Data Sci. Adv. Analytics,
2018, pp. 80–89.

[134] A. Abdul, J. Vermeulen, D. Wang, B. Y. Lim, and M. Kankanhalli,
“Trends and trajectories for explainable, accountable and intelligible
systems: An HCI research agenda,” in Proc. SIGCHI Conf. Hum. Factors
Comput. Syst., 2018, pp. 1–28.

[135] G. Montavon, W. Samek, and K.-R. Müller, “Methods for interpreting
and understanding deep neural networks,” Digit. Signal Process., vol. 73,
pp. 1–15, 2018.

[136] A. Das and P. Rad, “Opportunities and challenges in explainable artiﬁcial

intelligence (XAI): A survey,” 2020, arXiv: 2006.11371.

---

<!-- PAGE 18 -->

RONG et al.: TOWARDS HUMAN-CENTERED EXPLAINABLE AI: A SURVEY OF USER STUDIES FOR MODEL EXPLANATIONS

2121

[137] G. Joshi, R. Walambe, and K. Kotecha, “A review on explainability in
multimodal deep neural nets,” IEEE Access, vol. 9, pp. 59800–59821,
2021.

[138] R. Moraffah, M. Karami, R. Guo, A. Raglin, and H. Liu, “Causal
interpretability for machine learning-problems, methods and evaluation,”
ACM SIGKDD Explorations Newslett., vol. 22, pp. 18–33, 2020.
[139] I. Nunes and D. Jannach, “A systematic review and taxonomy of ex-
planations in decision support and recommender systems,” User Model.
User-Adapted Interact., vol. 27, pp. 393–444, 2017.

[140] Z. C. Lipton, “The mythos of model interpretability: In machine learning,
the concept of interpretability is both important and slippery,” Queue,
vol. 16, pp. 31–57, 2018.

[141] Q. V. Liao and K. R. Varshney, “Human-centered explainable AI (XAI):
From algorithms to user experiences,” 2021, arXiv:2110.10790.
[142] V. Lai, C. Chen, Q. V. Liao, A. Smith-Renner, and C. Tan, “Towards a
science of Human-AI decision making: A survey of empirical studies,”
2021, arXiv:2112.11471.

[143] J. J. Ferreira and M. S. Monteiro, “What are people doing about XAI user
experience? a survey on ai explainability research and practice,” in Proc.
Int. Conf. Hum.-Comput. Interact., 2020, pp. 56–73.

[144] N. Bevan, “International standards for HCI and usability,” Int. J. Hum.-

Comput. Stud., vol. 55, pp. 533–552, 2001.

[145] W. Iso, “9241–11: 1998, Ergonomic requirements for work with visual
display terminals (VDTs)-Part 11: Guidance on usability,” Int. Org.
Standardization, vol. 45, no. 9, 1998.

[146] M. T. Ribeiro, S. Singh, and C. Guestrin, ““Why should I trust
you?,” explaining the predictions of any classiﬁer,” in Proc. 22nd
ACM SIGKDD Int. Conf. Knowl. Discov. Data Mining, 2016,
pp. 1135–1144.

[147] S. M. Lundberg and S.-I. Lee, “A uniﬁed approach to interpreting model
predictions,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2017, pp. 4768–
4777.

[148] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and
D. Batra, “Grad-CAM: Visual explanations from deep networks via
gradient-based localization,” in Proc. IEEE Int. Conf. Comput. Vis., 2017,
pp. 618–626.

[149] P. Voigt and A. Von dem Bussche, “The EU general data protection
regulation (GDPR),” in A Practical Guide, 1st ed., Berlin, Germany:
Springer, 2017.

[150] B. Goodman and S. Flaxman, “European union regulations on algorith-
mic decision-making and a “right to explanation”,” AI Mag., vol. 38,
no. 3, pp. 50–57, 2017.

[151] C. Molnar, “Interpretable machine learning,” pp. 26–27, 2020.
[152] C. Rudin, “Stop explaining black box machine learning models for high
stakes decisions and use interpretable models instead,” Nat. Mach. Intell.,
vol. 1, pp. 206–215, 2019.

[153] R. Caruana, Y. Lou, J. Gehrke, P. Koch, M. Sturm, and N. Elhadad, “In-
telligible models for healthcare: Predicting pneumonia risk and hospital
30-day readmission,” in Proc. 21th ACM SIGKDD Int. Conf. Knowl.
Discov. Data Mining, 2015, pp. 1721–1730.

[154] C. Panigutti, A. Perotti, and D. Pedreschi, “Doctor XAI: An ontology-
based approach to black-box sequential data classiﬁcation explana-
tions,” in Proc. Conf. Fairness Accountability Transparency, 2020,
pp. 629–639.

[155] A. Papenmeier, G. Englebienne, and C. Seifert, “How model accuracy
and explanation ﬁdelity inﬂuence user trust,” 2019, arXiv: 1907.12652.
[156] J. van der Waa, E. Nieuwburg, A. Cremers, and M. Neerincx, “Evaluating
XAI: A comparison of rule-based and example-based explanations,”
Artif. Intell., vol. 291, 2021, Art. no. 103404.

[157] B. J. Erickson, P. Korﬁatis, Z. Akkus, and T. L. Kline, “Machine learning
for medical imaging,” Radiographics, vol. 37, no. 2, pp. 505–515, 2017.
[158] J.-Y. Jian, A. M. Bisantz, and C. G. Drury, “Foundations for an em-
pirically determined scale of trust in automated systems,” Int. J. Cogn.
Ergonom., vol. 4, pp. 53–71, 2000.

[159] B. Kim et al., “Interpretability beyond feature attribution: Quantitative
testing with concept activation vectors (TCAV),” in Proc. Int. Conf. Mach.
Learn., 2018, pp. 2668–2677.

[160] B. P. Knijnenburg, M. C. Willemsen, Z. Gantner, H. Soncu, and C.
Newell, “Explaining the user experience of recommender systems,” in
User Modeling User-Adapted Interaction. Berlin, Germany: Springer,
2012.

[161] B. Y. Lim and A. K. Dey, “Assessing demand for intelligibility in context-
aware applications,” in Proc. 11th Int. Conf. Ubiquitous Comput., 2009,
pp. 195–204.

[162] S. G. Hart and L. E. Staveland, “Development of NASA-TLX (task load
index): Results of empirical and theoretical research,” Adv. Psychol.,
vol. 52, pp. 139–183, 1988.

[163] R. R. Hoffman, S. T. Mueller, G. Klein, and J. Litman, “Metrics for

explainable AI: Challenges and prospects,” 2018, arXiv: 1812.04608.

[164] A. Holzinger, A. Carrington, and H. Müller, “Measuring the quality
of explanations: The system causability scale (SCS),” KI-Künstliche
Intelligenz, 2020.

[165] A. Gegenfurtner, E. Lehtinen, and R. Säljö, “Expertise differences in
the comprehension of visualizations: A meta-analysis of eye-tracking
research in professional domains,” KI-Ku nstliche Intelligenz, vol. 34,
no. 2, pp. 193–198, 2020.

[166] K. Cotter, J. Cho, and E. Rader, “Explaining the news feed algorithm:
An analysis of the “news feed FYI,” blog,” in Proc. CHI Conf. Extended
Abstr. Hum. Factors Comput. Syst., 2017, pp. 1553–1560.

[167] D. Wang, Q. Yang, A. Abdul, and B. Y. Lim, “Designing theory-driven
user-centric explainable AI,” in Proc. SIGCHI Conf. Hum. Factors Com-
put. Syst., 2019, pp. 1–15.

[168] L. Rozenblit and F. Keil, “The misunderstood limits of folk science:
An illusion of explanatory depth,” Cogn. Sci., vol. 26, pp. 521–562,
2002.

[169] G. Hoffman and X. Zhao, “A primer for conducting experiments in
human–robot interaction,” ACM Trans. Human-Robot Interact., vol. 10,
pp. 1–31, 2020.

[170] J. Eccles, “Expectancies, values and academic behaviors,” Achievement

Achievement Motives, vol. 58, pp. 58–74, 1983.

[171] C. S. Hulleman, J. J. Kosovich, K. E. Barron, and D. B. Daniel, “Making
connections: Replicating and extending the utility value intervention in
the classroom,” J. Educ. Psychol., vol. 109, 2017, Art. no. 387.
[172] F. G. Paas, “Training strategies for attaining transfer of problem-solving
skill in statistics: A cognitive-load approach,” J. Educ. Psychol., vol. 84,
pp. 429–434, 1992.

[173] K. Ouwehand, A. V. D. Kroef, J. Wong, and F. Paas, “Measuring cognitive
load: Are there more valid alternatives to likert rating scales?,” Front.
Educ., Frontiers Educ., vol. 6, p. 702616, 2021.

[174] J. P. Simmons, L. D. Nelson, and U. Simonsohn, “Pre-registration: Why

and how,” J. Consum. Psychol., vol. 31, pp. 151–162, 2021.

[175] U. Simonsohn, L. D. Nelson, and J. P. Simmons, “P-curve: A key to the
ﬁle-drawer,” J. Exp. Psychol.: Gen., vol. 143, pp. 534–547, 2014.
[176] K. A. Ericsson and H. A. Simon, Protocol Analysis: Verbal Reports as

Data. Cambridge, MA, USA: MIT Press, 1984.

[177] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, San

Francisco, CA, USA: Academic, 2013.

[178] S. Dhanorkar, C. T. Wolf, K. Qian, A. Xu, L. Popa, and Y. Li, “Who
needs to know what, when?: Broadening the explainable AI (XAI) design
space by looking at explanations across the AI lifecycle,” in Proc. Des.
Interactive Syst. Conf., 2021, pp. 1591–1602.

[179] F. Y. Kung, N. Kwok, and D. J. Brown, “Are attention check ques-
tions a threat to scale validity?,” Appl. Psychol., vol. 67, pp. 264–283,
2018.

[180] J. L. Fleiss, “Measuring nominal scale agreement among many raters,”

Psychol. Bull., vol. 76, pp. 378–382, 1971.

[181] I. Lage, D. Lifschitz, F. Doshi-Velez, and O. Amir, “Exploring compu-
tational user models for agent policy summarization,” in IJCAI: Proc.
Conf., 2019, Art. no. 1401.

[182] P. Qian and V. Unhelkar, “Evaluating the role of interactivity on improv-
ing transparency in autonomous agents,” in Proc. 21st Int. Conf. Auton.
Agents Multiagent Syst., 2022, pp. 1083–1091.

[183] A. Radford et al., “Language models are unsupervised multitask learn-

ers,” OpenAI Blog, vol. 1, no. 8, 2019, Art. no. 9.

[184] ChatGPT, Introducing, “OpenAI,” 2023. Accessed: Feb. 17, 2023. [On-

line]. Available: https://openai.com/blog/chatgpt

[185] S. Bubeck et al., “Sparks of artiﬁcial general intelligence: Early experi-

ments with GPT-4,” 2023, arXiv:2303.12712.

[186] W. Zhou et al., “Towards interpretable natural language understanding
with explanations as latent variables,” in Proc. Int. Conf. Neural Inf.
Process. Syst., 2020, pp. 6803–6814.

[187] S. Wiegreffe, J. Hessel, S. Swayamdipta, M. Riedl, and Y. Choi, “Re-
framing Human-AI collaboration for generating free-text explanations,”
in Proc. Conf. North Amer. Chapter Assoc. Comput. Linguistics: Hum.
Lang. Technol., 2022, pp. 632–658.

[188] S. Wang, Z. Zhao, X. Ouyang, Q. Wang, and D. Shen, “Chatcad: Inter-
active computer-aided diagnosis on medical image using large language
models,” 2023, arXiv:2302.07257.

[189] N. F. Rajani, B. McCann, C. Xiong, and R. Socher, “Explain yourself!
leveraging language models for commonsense reasoning,” in Proc. 57th
Annu. Meeting Assoc. Comput. Linguistics, 2019, pp. 4932–4942.
[190] J. Wei et al., “Chain-of-thought prompting elicits reasoning in large
language models,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2022,
pp. 24824–24837.

---

<!-- PAGE 19 -->

2122

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 46, NO. 4, APRIL 2024

[191] D. Alvarez Melis and T. Jaakkola, “Towards robust interpretability with
self-explaining neural networks,” in Proc. Int. Conf. Neural Inf. Process.
Syst., 2018, pp. 7786–7795.

[192] M. Yin, J. Wortman Vaughan, and H. Wallach, “Understanding the effect
of accuracy on trust in machine learning models,” in Proc. SIGCHI Conf.
Hum. Factors Comput. Syst., 2019, pp. 1–12.

[193] A. Bussone, S. Stumpf, and D. O’Sullivan, “The role of explanations on
trust and reliance in clinical decision support systems,” in Proc. Int. Conf.
Healthcare Inform., 2015, pp. 160–169.

[194] C. Baker, R. Saxe, and J. Tenenbaum, “Bayesian theory of mind: Mod-
eling joint belief-desire attribution,” in Proc. Annu. Meeting Cogn. Sci.
Soc., vol. 33, no. 33, 2011.

[195] S. H. Huang, D. Held, P. Abbeel, and A. D. Dragan, “Enabling robots
to communicate their objectives,” Auton. Robots, vol. 43, pp. 309–326,
2019.

[196] S. C.-H. Yang, N. E. T. Folke, and P. Shafto, “A psychological theory of
explainability,” in Proc. Int. Conf. Mach. Learn., 2022, pp. 25007–25021.
[197] S. C.-H. Yang, W. K. Vong, R. B. Sojitra, T. Folke, and P. Shafto,
“Mitigating belief projection in explainable artiﬁcial intelligence via
Bayesian teaching,” Sci. Rep., vol. 11, 2021, Art. no. 9863.

[198] V. Chen, N. Johnson, N. Topin, G. Plumb, and A. Talwalkar,
“Use-case-grounded simulations for explanation evaluation,” 2022,
arXiv:2206.02256.

[199] G. Aher, R. I. Arriaga, and A. T. Kalai, “Using large language models to

simulate multiple humans,” 2022, arXiv:2208.10264.

Yao Rong received the MSc degree in electrical
and computer engineering from the Technical Uni-
versity of Munich, Germany, in 2019. She is cur-
rently working toward the doctoral degree with the
Human-Centered Technologies for Learning Group,
the Technical University of Munich. From 2022 to
2023, she served as a visiting scholar with the DATA
Lab, Rice University. Her research interests lie in
human-centered AI, explainable AI, and human-AI
interaction technologies.

Tobias Leemann received the MSc degree from
the University of Erlangen-Nuremberg, Germany, in
2020. He is currently working toward the PhD degree
with the University of Tübingen, Germany where his
research is focused on trustworthy machine learning.
Speciﬁcally, his research interests include the quality
assessment of interpretability techniques and the in-
tersections of interpretability, fairness and privacy.

Thai-Trang Nguyen is graduated with a BSc degree
in computer science from the University of Tübingen,
Germany. She is currently working toward the MSc
degree with the same university. Furthermore, she
served as a research assistant, the Human-Computer
Interaction group from 2019 to 2022.

Lisa Fiedler is currently working toward the BSc
degree in media informatics from the University of
Tübingen, Germany. Additionally, she works as a
student assistant for the Human-Computer Interaction
Group at the University of Tübingen.

Peizhu Qian is currently working toward the PhD de-
gree in computer science with Rice University, USA
working with Dr. Vaibhav Unhelkar on problems
in human-robot interaction, robot transparency, and
explainable AI. Her research interest lies in building
a mutual understanding between a robot and its hu-
man collaborators. Her work applies psychology the-
ories to computational frameworks, enabling robots
to communicate their objectives.

Vaibhav Unhelkar received the MS degree in aero-
nautics and astronautics and the PhD degree in au-
tonomous systems, in 2015 and 2020, respectively.
He is an assistant professor of computer science with
Rice University, USA where he leads a research group
in the emerging area of Human-Centered AI and
Robotics. Unhelkar earned his undergraduate degree
in aerospace engineering from the Indian Institute
of Technology in Bombay, in 2012. From the Mas-
sachusetts Institute of Technology, where he worked
in the Computer Science and Artiﬁcial Intelligence

Laboratory (CSAIL).

Tina Seidel received the diploma degree in psychol-
ogy from the University of Regensburg (Germany)
and Vanderbilt University Nashville (USA), in 1998,
and the PhD degree with excellence, in 2002 from the
Leibniz Institute for Science and Mathematics Edu-
cation Kiel (Germany). She holds the Friedl Schoeller
Chair for Educational Psychology with the School of
Social Sciences and Technology, Technical Univer-
sity of Munich, Germany. Her research focuses on
teaching and teacher education. She has established a
Teacher Research & Training Simulation Center that
conducts several research projects funded by the German Science Foundation
and the German Federal Ministry of Education and Research.

Gjergji Kasneci received the MSc degree in com-
puter science and mathematics from the University
of Marburg, in 2005, and the PhD degree from the
University of Saarland - while with the Max Planck
Institute - in 2009. He then worked with Microsoft
Research Cambridge, the Hasso Plattner Institute, and
SCHUFA Holding AG, where he served as CTO from
2017 to 2022. Between 2018 and 2023, he led the Data
Science and Analytics Group with the University of
Tübingen as an Honorary professor. In 2023, Gjergji
Kasneci was appointed professor of Responsible Data

Science with the Technical University of Munich.

Enkelejda Kasneci received the PhD degree in
computer science from the University of Tübingen,
in 2013. She was postdoctoral researcher and a
Margarete-von-Wrangell Fellow with the University
of Tübingen. She is a distinguished professor for
Human-Centered Technologies for Learning with the
Technical University of Munich and Core Member
of the Munich Data Science Institute. Her research
evolves around Human-Centered Technologies and
AI systems that sense and infer the user’s cognitive
state, the level of task-related expertise, actions, and
intentions based on multimodal data and provide information for media and
assistive technologies in many activities of everyday life, and especially in the
context of learning.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

2104 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
| Towards |     | Human-Centered |     |         |     |     | Explainable |              |     | AI: | A   | Survey |     |
| ------- | --- | -------------- | --- | ------- | --- | --- | ----------- | ------------ | --- | --- | --- | ------ | --- |
|         |     | of User        |     | Studies |     | for | Model       | Explanations |     |     |     |        |     |
YaoRong ,TobiasLeemann ,Thai-TrangNguyen ,LisaFiedler ,PeizhuQian ,VaibhavUnhelkar ,
|     |     |     | TinaSeidel |     | ,GjergjiKasneci |     | ,andEnkelejdaKasneci |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
(SurveyPaper)
Abstract—ExplainableAI(XAI)iswidelyviewedasasinequa high-stakesdecision-makingtaskslikemedicaldiagnosis[106],
| non for ever-expanding |     | AI  | research. | A better | understanding |     | of            |        |         |        |        |        |           |
| ---------------------- | --- | --- | --------- | -------- | ------------- | --- | ------------- | ------ | ------- | ------ | ------ | ------ | --------- |
|                        |     |     |           |          |               |     | [107], [108], | credit | scoring | [109], | [110], | [111], | jurispru- |
theneedsofXAIusers,aswellashuman-centeredevaluationsof
|             |         |                    |             |             |              |           | dence [112],    | [113] | or recruiting | and | hiring          | decisions | [114],    |
| ----------- | ------- | ------------------ | ----------- | ----------- | ------------ | --------- | --------------- | ----- | ------------- | --- | --------------- | --------- | --------- |
| explainable | models  | are both           | a necessity | and         | a challenge. | In this   |                 |       |               |     |                 |           |           |
|             |         |                    |             |             |              |           | [115], However, | the   | behavior      | and | decision-making |           | processes |
| paper, we   | explore | how human-computer |             | interaction |              | (HCI) and |                 |       |               |     |                 |           |           |
AIresearchersconductuserstudiesinXAIapplicationsbasedon ofmodernAIsystemsareoftennotunderstandable,sotheyare
a systematic literature review. After identifying and thoroughly frequently considered black boxes. Deploying such black-box
analyzing97corepaperswithhuman-basedXAIevaluationsover modelspresentsaseriousdilemmaincertainsafety-criticaldo-
thepastfiveyears,wecategorizethemalongthemeasuredchar-
mains,forinstance,publichealthorfinance[116].Thisisdueto
| acteristics | of explanatory | methods, |     | namely | trust, understanding, |     |     |     |     |     |     |     |     |
| ----------- | -------------- | -------- | --- | ------ | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
thenecessityforatransparentandtrustworthyAIsystem,which
usability,andhuman-AIcollaborationperformance.Ourresearch
shows that XAI is spreading more rapidly in certain application is required by both practitioners (to gain better insights into
domains, such as recommender systems than in others, but that systemfunctioning)andendusers(torelyonmodeldecisions).
userevaluationsarestillrathersparseandincorporatehardlyany Methods toincrease the interpretability and transparency of
insightsfromcognitiveorsocialsciences.Basedonacomprehensive
anAIsystemaredevelopedintheresearchareaofExplainable
discussionofbestpractices,i.e.,commonmodels,designchoices,
|     |     |     |     |     |     |     | AI(XAI).Specifically, |     | human-centered |     | XAI,whichaddresses |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | -------------- | --- | ------------------ | --- | --- |
andmeasuresinuserstudies,weproposepracticalguidelineson
designing and conducting user studies for XAI researchers and the importance of human stack-holders to the AI systems, has
practitioners. Lastly, this survey also highlights several open re- beenproposedanddiscussedsince[117],[118].Whileahuge
search directions, particularly linking psychological science and numberofmodelexplanationsareavailable,thequestionofhow
human-centeredXAI.
|     |     |     |     |     |     |     | to transparently | evaluate |     | their quality | is still | an  | open research |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | --- | ------------- | -------- | --- | ------------- |
Index Terms—Explainable AI (XAI), human-centered XAI, question,andhence,extensivelystudiedinrecentyears.Apopu-
explainableML,userstudy,human-AIinteraction.
lartaxonomyofevaluationstrategiesforXAImethodsproposes
threecategories:functionally-groundedevaluation,application-
|     |     |                 |     |     |     |     | grounded                    | evaluation, | and | human-grounded |     | evaluation  | [119]. |
| --- | --- | --------------- | --- | --- | --- | --- | --------------------------- | ----------- | --- | -------------- | --- | ----------- | ------ |
|     |     | I. INTRODUCTION |     |     |     |     |                             |             |     |                |     |             |        |
|     |     |                 |     |     |     |     | While functionally-grounded |             |     | measures       | do  | not require | human  |
ARTIFICIAL Intelligence (AI) is driving digital transfor- labor,theothertwoinvolvehumansubjectsandaremorecostly
| mation | and | is already | an integral | part | of various | every- |     |     |     |     |     |     |     |
| ------ | --- | ---------- | ----------- | ---- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
toconduct.
day technologies. Recent developments in AI are essential to Many functionally-grounded measures have been proposed
progress in fields such as recommendation systems [97], [98], toevaluateXAIalgorithms(see[120]forreview),however,the
[99],autonomousdriving[100],[101],[102]orrobotics[103],
|     |     |     |     |     |     |     | difficult | comparability | between | different |     | automatic | evaluation |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ------- | --------- | --- | --------- | ---------- |
[104], [105]. Moreover, AI’s success story has not excluded measuresisacommonproblem[121],[122].Anotherdrawback
|     |     |     |     |     |     |     | of automated  | measures | is          | that there | is no        | guarantee | that they     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ----------- | ---------- | ------------ | --------- | ------------- |
|     |     |     |     |     |     |     | truly reflect | humans’  | preferences |            | [40], [123]. |           | Consequently, |
Manuscriptreceived3February2023;revised26October2023;accepted4
userstudiesinXAI,especiallywhenmovingtowardsreal-world
November2023.Dateofpublication13November2023;dateofcurrentversion
6March2024.RecommendedforacceptancebyM.Cheng.(Corresponding
products,areinevitableifonewishestotestmoregeneralbeliefs
author:YaoRong.)
ofthequalityofexplanations[16].However,onlyasmallportion
| Yao Rong,          | Tina | Seidel, Gjergji | Kasneci, | and           | Enkelejda | Kasneci are |             |        |            |          |          |     |            |
| ------------------ | ---- | --------------- | -------- | ------------- | --------- | ----------- | ----------- | ------ | ---------- | -------- | -------- | --- | ---------- |
|                    |      |                 |          |               |           |             | (about 20%) | of XAI | evaluation | projects | consider |     | human sub- |
| with the Technical |      | University of   | Munich,  | 80335 Munich, | Germany   | (e-mail:    |             |        |            |          |          |     |            |
yao.rong@tum.de; tina.seidel@tum.de; gjergji.kasneci@tum.de; enkelejda. jects[120].Thereexisteffortsindevelopingtaxonomiesorintro-
kasneci@tum.de).
ducingthedefinitionsorimplicationsofdifferenthuman-centric
| Tobias Leemann, |     | Thai-Trang | Nguyen, and | Lisa | Fiedler are | with the Uni- |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | ----------- | ---- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
versity of Tübingen, 72076 Tübingen, Germany (e-mail: tobias.leemann@ evaluations[124],[125],[126],buttherecentgenerationofuser
uni-tuebingen.de; thai-trang.nguyen@student.uni-tuebingen.de; lisa.fiedler@ studiesandtheirfindingshavenotbeensystematicallydiscussed
student.uni-tuebingen.de).
|     |     |     |     |     |     |     | yet.Moreover,Yangetal. |     |     | [127]pointoutthatXAIisgrowing |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ----------------------------- | --- | --- | --- |
PeizhuQianandVaibhavUnhelkararewiththeRiceUniversity,Houston,
TX77005USA(e-mail:pq3@rice.edu;vaibhav.unhelkar@rice.edu). separatelyandtreateddifferentlyindifferentcommunities(e.g.,
This article has supplementary downloadable material available at machinelearningandHCI).Hence,effectiveguidanceinXAI
https://doi.org/10.1109/TPAMI.2023.3331846,providedbytheauthors.
DigitalObjectIdentifier10.1109/TPAMI.2023.3331846 user study design is crucial to better let both XAI algorithm
©2023TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,see
https://creativecommons.org/licenses/by/4.0/

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2105
TABLEI
OVERVIEWOFTHECOREPAPERSCONTAININGUSERSTUDIESINXAIGROUPEDBYCATEGORIESOFMEASUREMENTSASSOMECOREPAPERSASSESS
QUANTITIESBELONGINGTOSEVERALGROUPS,ASINGLEPAPERCANALSOBELISTEDAMONGMULTIPLEGROUPS
andapplicationdesignersrecognizetheusers’realneeds.This Our study highlights under-investigated areas in the context
workaimstobridgethisresearchgapinmodernXAIuserstudy ofcurrentuser-centeredXAIresearchsuchascognitiveorpsy-
designbydistillingpracticalguidelinesforuserstudiesthrough chological sciences through data-driven bibliometric analysis.
acomprehensiveandstructuredliteraturereview. Together with our proposed guidelines, we believe that this
Therefore, we reviewed highly relevant papers that include workwillbenefitXAIpractitionersandresearchersfromvarious
user studies from top-tier HCI and XAI venues. Specifically, disciplines and will help to approach the overarching goal of
we included the recent five years of CHI, IUI, UIST, CSCW, human-centeredXAI.
FA(cc)T,ICML,ICRL,NeurIPS,andAAAI.Asweaimatana-
lyzinghumanuserevaluationofadvancedmodelexplanations,
weransearchqueriesinvolvingkeywordsfromthetwogroups II. RELATEDWORK
| “explainable | AI” | and “user | study”, | as  | listed | in the | Table II. |      |             |                |     |         |                |
| ------------ | --- | --------- | ------- | --- | ------ | ------ | --------- | ---- | ----------- | -------------- | --- | ------- | -------------- |
|              |     |           |         |     |        |        |           | As a | vast amount | of explanation |     | methods | have been pro- |
We selected the papers containing at least one keyword from posed,manyresearchersseekasystematicoverviewoftheever-
| each group, | resulting | in  | over one | hundred | papers. | Then, | we  |     |     |     |     |     |     |
| ----------- | --------- | --- | -------- | ------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
growingfieldofXAI.In[128],[129],[130],[131],[132],[133],
thoroughly studied these papers and filtered out papers that theauthorsaimtocovermanyfacetsofXAItechnologiesrang-
| did not | fulfill the | criteria: | (1) | deploying | explainable |     | models |     |     |     |     |     |     |
| ------- | ----------- | --------- | --- | --------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
ingfromproblemdefinitions,goals,AI/MLmodelexplanations
| or techniques | and | (2) conducting |     | an  | assessment | with | human |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | --- | ---------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
toevaluationmeasures,whilein[134]theauthorsemphasizethe
subjects.Weidentifiedatotalof97corepapersforthissurvey researchtrendsandchallengesinHuman-Computer-Interaction
(seeTableIforanoverviewofcorepaperswithrespecttotheir
|     |     |     |     |     |     |     |     | (HCI) applications. |     | A large | body | of XAI | surveys focuses |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------- | ---- | ------ | --------------- |
measuredquantitiesinuserstudies).Basedonthesecorepapers, mainly on the interpretability of a particular family of models
weperformedacomprehensiveanalysistofilltheresearchgap
andcorrespondingexplanationtechniques.Forinstance,[135],
| by offering | a systematic |     | overview | of  | user studies | in  | XAI. We |     |     |     |     |     |     |
| ----------- | ------------ | --- | -------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- |
[136],[137]investigateexplanationsforDeepNeuralNetworks
highlightthemaincontributions: (DNNs),wheremodelsoftentakeimagesasinput[135],[136].
1) Toofferanoverviewofthefoundationalworkofuserstud-
|     |     |     |     |     |     |     |     | Joshi et | al. [137], | however, | provide | an extensive | review for |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | ------- | ------------ | ---------- |
iesinXAI,weinvestigatedreferencesofall97corepapers DNNs with multimodal input for instance that of joint vision-
inadata-drivenmanner.Likewise,weanalyzedfollow-up language tasks. Causal interpretable models are gaining more
| works | building | on  | these core | papers | (identified |     | through |                                   |     |     |     |                         |     |
| ----- | -------- | --- | ---------- | ------ | ----------- | --- | ------- | --------------------------------- | --- | --- | --- | ----------------------- | --- |
|       |          |     |            |        |             |     |         | attentionrecentlyandMoraffahetal. |     |     |     | [138]providealiterature |     |
citationsofcorepapers)torevealthefieldsimpactedby reviewforcausalexplanations.Asystematicliteraturereviewon
XAIuserevaluations(SectionIII).
|     |     |     |     |     |     |     |     | explanations | for | advice-giving |     | systems is conducted | in [139]. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | -------------------- | --------- |
2) WepresentasummaryofthedesigndetailsinXAIuser Among these surveys focusing on general XAI technologies,
studies with particular focus on the deployed models evaluationmeasuresareonlybrieflyexamined.
andexplanationtechniques,experimentaldesignpatterns,
|     |     |     |     |     |     |     |     | One challenge |     | in XAI | research | is to evaluate | and com- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | -------- | -------------- | -------- |
participantsaswellasconcretemeasures,providinginspi- pare different explanation methods, due to the multidisci-
rationofhowtocollecthumanassessment(SectionIV).
|     |     |     |     |     |     |     |     | plinary concepts |     | in interpretability/explainability |     |     | [119], [120], |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------------------------------- | --- | --- | ------------- |
3) Wediscusstheimpactofusingexplanationsondifferent
|     |     |     |     |     |     |     |     | [140]. Evaluation |     | measures | can | be divided | into two groups: |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | --- | ---------- | ---------------- |
aspects of user experience (Section V), which can serve human-grounded measures that rely on human subjects and
| as  | an overview | of  | the effectiveness |     | of  | the current | XAI |                       |     |         |     |                      |         |
| --- | ----------- | --- | ----------------- | --- | --- | ----------- | --- | --------------------- | --- | ------- | --- | -------------------- | ------- |
|     |             |     |                   |     |     |             |     | functionally-grounded |     | metrics |     | that can be computed | without |
technologyandasummaryofthestate-of-the-art. humansubjects[119],[120].Manyresearchersseeksolutionsto
4) Basedontheexamineduserstudydetailsandtheirbest-
evaluateexplanationsautomatically.Acomprehensiveliterature
practicefindings,wesynthesizeguidelinesfordesigning
reviewwithafocusonthesefunctionally-groundedevaluation
aneffectiveuserstudyforXAI(SectionVI). methods (without human subjects) can be found in [120]. Ex-
| 5) Beyond | the | user | study | design, | we discuss |     | potential |     |     |     |     |     |     |
| --------- | --- | ---- | ----- | ------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- |
plainabilityisaninherentlyhuman-centricproperty,therefore,
paradigms of AI systems understanding humans in the the research community should and has started to recognize
| context | of  | e.g., theory | of  | minds, | as well | as other | future |          |                    |     |     |                  |            |
| ------- | --- | ------------ | --- | ------ | ------- | -------- | ------ | -------- | ------------------ | --- | --- | ---------------- | ---------- |
|         |     |              |     |        |         |          |        | the need | for human-centered |     |     | evaluations when | working on |
researchdirections(SectionVII).
XAI[119],[141].

2106 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
Fig.1. Roadmapofourliteratureanalysis.Wefindoutthefoundationalworksofcorepapersandtheirapplicationdomainsusingadata-drivenmethodintroduced
inSectionIII.Threemainresearchquestionsinuserstudiesaredistilledfromcorepapers.MethodsrelatedtomeasuresofeachcategoryarediscussedinSection
IV,andfindingsoftheresearchquestionsaresummarizedinSectionV.Basedonthefindings,weproposefuturedirectionstofurtherpromotehuman-centered
XAIinSectionVII.Wedistillimportantmessagesinthisfigure,butrefertothediscussioninthecorrespondingsectionsformoredetails.
Forinstance,ChromikandSchuessler[125]proposeataxon- information on experimental design. To this end, we present
omyonXAIevaluationsinvolvinghumans.Mohsenietal. [126] a practical guideline in user study design, which can be used
summarize four groups of human-related evaluation metrics: asastartingpointforfutureexplorationofhuman-centricXAI
| mental          | model (e.g., | user’s           | understanding |     | of          | the | model), user | applications. |     |     |     |     |     |
| --------------- | ------------ | ---------------- | ------------- | --- | ----------- | --- | ------------ | ------------- | --- | --- | --- | --- | --- |
| trust, human-AI |              | task performance |               | and | explanation |     | usefulness   |               |     |     |     |     |     |
and satisfaction (i.e., user experience). Hoffman [124] places III. METHODOLOGY
| more focus        | on    | psychometric |             | evaluations | by             | proposing  | a con-    |             |                       |        |               |         |            |
| ----------------- | ----- | ------------ | ----------- | ----------- | -------------- | ---------- | --------- | ----------- | --------------------- | ------ | ------------- | ------- | ---------- |
|                   |       |              |             |             |                |            |           | To analyze  | the collected         | papers | related       | to user | studies on |
| ceptual           | model | of the       | XAI process |             | and specifying |            | four key  |             |                       |        |               |         |            |
|                   |       |              |             |             |                |            |           | XAI, we     | first categorize them | into   | four groups   | based   | on their   |
| components        | that  | should       | be          | evaluated:  | explanation    |            | goodness  |             |                       |        |               |         |            |
|                   |       |              |             |             |                |            |           | objectives. | From these studies,   | we     | distill three | main    | research   |
| and satisfaction, |       | (user’s)     | mental      | models,     |                | curiosity, | trust and |             |                       |        |               |         |            |
questionsconcerningtheeffectsofmodelexplanationsoneach
| performance. | Beyond |     | assessing | evaluation |     | methods, | XAI ap- |     |     |     |     |     |     |
| ------------ | ------ | --- | --------- | ---------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- |
objective.Wethensummarizethemethodsusedinthesestudies
| plications  | are designed |        | to eventually |        | support | decision-making |              |                     |                   |           |                   |      |          |
| ----------- | ------------ | ------ | ------------- | ------ | ------- | --------------- | ------------ | ------------------- | ----------------- | --------- | ----------------- | ---- | -------- |
|             |              |        |               |        |         |                 |              | to quantify         | these objectives. | Important | findings          | from | the pa-  |
| and benefit | end          | users. | A recent      | review | by      | Lai             | et al. [142] |                     |                   |           |                   |      |          |
|             |              |        |               |        |         |                 |              | pers are discussed, | and we            | propose   | future directions |      | based on |
considersstudiesoncollaborativeHuman-AIdecision-making,
thesefindings.Additionally,weexaminethefoundationalworks
| which may | include | AI  | agents | providing | explanations. |     | Success |     |     |     |     |     |     |
| --------- | ------- | --- | ------ | --------- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
uponwhichtheseuserstudiesarebased(i.e.,theirreferences)
inhuman-AIdecision-makingtaskscanbeseenasoneamongst
|     |     |     |     |     |     |     |     | and the follow-up | papers that | cite them, | shedding |     | light on the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------- | ---------- | -------- | --- | ------------ |
manyotherwaystoevaluatetheeffectofexplanations.Ferreira
foundationalworksandemergingtrendsinhuman-centeredXAI
| andMonteiro[143]presentareviewoftheuserexperience |     |     |     |     |     |     | of  |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
studies.Fig.1presentsaroadmapofouranalysis.
XAIapplicationstoanswerwhousesXAI,why,andinwhich
|     |     |     |     |     |     |     |     | In this | section, we first | describe | the criteria | used | for their |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | -------- | ------------ | ---- | --------- |
context(what+when)theexplanationispresented.
categorization.Wethendiscussthefoundationalandapplication
| Closer | to our | focus | on user | studies | concerning |     | XAI, Liao |     |     |     |     |     |     |
| ------ | ------ | ----- | ------- | ------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- |
domainsofthesepapers,providingabroaderviewbeforediving
| etal. [141]studyuserexperiences |     |     |     |     | withXAItoreveal |     | pitfalls |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
intotheirdetailedanalysis.
| of existing | XAI | methods, | underscoring |     | the | important | role of |     |     |     |     |     |     |
| ----------- | --- | -------- | ------------ | --- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
humansinXAIdevelopment.AssuggestedbyDoshi-Velezand
A. CategorizationofUser-StudyObjectives
| Kim [119], | a human-subject |     |     | experiment | needs | to  | be designed |     |     |     |     |     |     |
| ---------- | --------------- | --- | --- | ---------- | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- |
sophisticatedly to reduce confounding factors. In contrast to Sincethecorepaperscovervariousfactorsofmodelexplana-
previous surveys on XAI, we aim to provide XAI researchers tions, we decided to categorize the core papers into different
| and practitioners |     | with | a comprehensive |     | overview |     | of the re- |             |                    |               |     |     |              |
| ----------------- | --- | ---- | --------------- | --- | -------- | --- | ---------- | ----------- | ------------------ | ------------- | --- | --- | ------------ |
|                   |     |      |                 |     |          |     |            | clusters to | better study their | commonalities |     | and | differences. |
searchquestionsexploredinuserstudies,alongwiththorough In[119],interpretabilityinthecontextofMLsystemsisdefined

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2107
astheabilitytoexplainorpresentmodelpredictionsinunder- These are a frequent subject of study in works measuring un-
standabletermstoahuman.Beyondfosteringcomprehension, derstandingandusability.Additionally,convolutionalnetworks,
theauthorsarguethatinterpretabilitycanassistinqualitatively which are commonly employed in experiments, use tools like
ascertainingwhetherotherdesiderata,suchasusabilityandtrust GradCAM[148]andvarioussaliencymapstogeneratemodel
aremet.Duringaprofoundstudyoftherelevantliteraturethat explanations.Notably,manyresearchpapersappearwithinthe
waspreviouslyselected,weidentifiedfoursensiblecategories, domainofrecommendersystems,becausemanyXAIuserstud-
thatarederivedfromtheconsidereddependentvariablesinuser ies are conducted in the context of recommendation solutions.
studies (desiderata of interpretability). These four categories he EU’s General Data Protection Regulation (GDPR) [149] is
aretrust,understanding,usability,andhuman-AIcollaboration frequentlymentionedincorepapersduetotheongoingdebate
performance. In Table I, the studied papers are categorized ontherighttoexplanation”[150].Thisdebatehassignificantly
according to the measured quantities. As each measure can influencedtheshiftinmodernAIsystemstowardsexplainability.
usually be assigned to only one of these categories, we found While the ultimate consumers of model explanations are hu-
thisdistinctiontobeintuitive. mans, well-established research domains that focus on human
These categories reflect different functionalities (goals) of understanding are underrepresented. For instance, only a few
XAI. As interpretability is defined as “the ability to explain papers related to “Cognition” are cited compared to those on
or to present in understandable terms to a human.”, humans’ otheralgorithmictopics.Millecampetal. [18]suggestenhanc-
“understanding” is the direct goal of XAI. To be concrete, ing XAI theory with insights from social sciences, including
understanding in the context of interacting with an ML model cognitivescienceandpsychology.Giventhescantreferencesto
refers to a user’s grasp or “mental model” of how the model psychology,itappearsthatonlyahandfulofXAIuserstudies
operates,andthisknowledgegrowsfromusingthesystemand delve into evaluating XAI from a psychological standpoint.
fromclearexplanationsaboutit[141].“Usability”iscommonly We highlight a nascent research domain of XAI frameworks
studied in human-computer interaction [144], which is one of based on human cognition and behavior theories [141]. This
the desiderata of XAI [119]. According to [145], usability is theoretical guidance can also offer conceptual tools for better
the extent to which users can utilize a product to successfully, evaluating XAI from user perspectives. More details about
efficiently, and satisfactorily accomplish their intended objec- common references can be found in Appendix A.1, available
tives.Thus,thiscategoryencompassesuserstudiesthatemploy online.
modelexplanationstosupportusersinachievingspecifictasks.
Inusability,differentaspectsaremeasured,forinstance,whether
C. ImpactofUserStudies
thesystemiseasytouseorhowmuchcognitiveloaditrequires.
Theaspect“undesired behavior detection” relatestousecases Fig. 1 presents applications that make use (and thus are the
where explanations uncover model discriminatory behaviors, consumers) of the findings from core papers. We noticed that
such as the utilization of undesired features. “Trust” in AI is studies on user understanding and trust span a wide range of
summarized as a combination of the user’s confidence in a applications. For example, trust is frequently addressed in the
model’s accuracy, a personal comfort level with understand- contextsofmedicaldiagnosisandtransportation,indicatingits
ing and using it, and the willingness to let the model make significance in high-risk scenarios. Recommendation systems
decisions[140].Itencompassesmorerequirements.Human-AI emerge as a primary focus in follow-up works. Papers on
collaborationperformanceisrelatedtoscenarioswheretheAI usability have a significant impact on fields like data visual-
systemprovidesitspredictions,buthumansretainthefinaldeci- ization, software development, and education. In these areas,
sions[89].Inthiscase,modelexplanationsaredeployedtoreach models frequently serve as tools to ease the burden on end
a performance superior to that of the AI system or the human users. Human-AI collaboration measures particularly promote
decision-maker alone. These categories cover different depen- the further development of robotics and or natural language
dentvariablesofinterestintherevieweduserstudies,primarily processing. The prominence of recommendation systems in
relatedtohowXAImethodsfunction.Thesefunctionsmainlytie both foundational works and their impact implies that XAI is
tothemodels’reasoningandknowledgerepresentation.Awider an integral component of contemporary recommendation sys-
perspectiveonXAI,whichassessesgeneralizationorrobustness, tems.Acomprehensiveoverviewofthefundamentalworksand
remains an important field for future exploration through user application domains can be found in Appendix A.1, available
studies. online.
B. FoundationsofUserStudies IV. COMPREHENSIVEUSERSTUDYANALYSIS
Based on a data-driven bibliometric analysis of the refer- In this section, we present details of the covered XAI user
ences in core papers, we highlight significant research topics studies.WefirstintroducesomecommonlyusedAImodelsand
within the “Foundational Domain” in Fig. 1. It is evident that explanation techniques (Section IV-A), followed by a discus-
modelexplanationsandinterpretabilityarepivotalcomponents. sion of application domains and measures with respect to the
This includes papers that introduce explanation methods such fourmeasuredquantities.Theexperimentaldesigns,aswellas
as LIME [146], SHAP [147], and other attribution methods. analysistoolsarepresentedinSectionIV-C.

2108 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
TABLEII and LIME (Local Interpretable Model-Agnostic Explana-
KEYWORDSFOROURPAPERSEARCHQUERY
tions [146]). There is a clear differentiation between local,
instance-wise,explanationsandglobalexplanationsthatapply
tothemodelinitsentirety.Forinstance,theweightsofalinear
model have a global scope. This differentiation is common
among these feature-based explanations, where most of the
papersusinglocalexplanations.Otherpopularexplanationtypes
are example-based explanations, counterfactual explanations,
which aim at providing actionable suggestions for attaining a
user-preferredpredictionbychangingcertaininputfeatures,and
concept-based explanations, which use meaningful high-level
TABLEIII conceptssuchasobjectsorshapestoexplainaprediction.
MODELSANDEXPLANATIONSINCOREPAPERS Besidesthesefourmaintypesofexplanations,thereareother
explanationssuchasrules[11],[88]orgamestrategies[7],[10]
whenAIplaysgames.Moredetailsaboutconcretemodelsand
explanationscanbefoundinAppendixB,availableonline.
B. Measurements
Theeffectivenessofexplanationscanbecharacterizedfrom
severalangles.Wespecificallyidentifiedthecategoriesoftrust,
understanding, usability, and human-AI collaboration perfor-
mance. In this section, we give an overview of the contexts in
whicheachofthesevariablesisstudiedandthemeasuresused
toquantifythem.
1) Trust: User trust is studied in decision-making applica-
tionssuchasimageclassification[13],[17],(review)deception
detection [25] or loan approval [27]. Besides decision mak-
ing,[5],[8],[16],[18],[19],[23]studyusertrustinthedomain
ofrecommendation systems.Whether explainable MLmodels
canincreaseusertrustinthemedicaldomainisstudiedin[1],
[6], [9]. Moreover, Colley et al. [3] measure user trust in an
autonomousdrivingapplicationwithandwithoutexplanations.
Trustmeasuresusedinmuchoftheexistingresearchcanbe
dividedintotwogroups:self-reportedandobservedtrust[155].
Self-reported trust is commonly measured by asking users to
fill out questionnaires whereas observed trust is quantified by
humans’agreementwiththemodel’sdecisions.InTableIIIin
Appendix,availableonline,trustmeasuresinthesetwogroups
A. ModelsandExplanations
arelisted.Theagreementrateofuserswiththemodeldecisions
As our selected core papers comprise a large spectrum of iscommonlyused[9],[11],[12],[25]asameasureofobserved
AI models, data modalities, and explanation approaches, we trust. Parallel to observed trust measurement, van der Waa
initially list the models and explanation techniques deployed etal. [156]ascribetheuser’salignmentbehaviorstothepersua-
alongwiththecorrespondingcorepaperreferencesinTableIII. sivepowerofmodelexplanations,i.e.,thecapacitytoconvince
It presents the utilization of explanation types in columns and userstofollowmodeldecisions despitethecorrectness.Asan
modeltypesinrows.Theexplanationmethodsusedisorganized extension, trust calibration is defined based on this measure.
according the the taxonomy by Molnar [151]. First, there are Forexample,ahighagreementratetowronglymadedecisions
intrinsicallyinterpretablemodels,alsoknownaswhite-boxmod- represents overtrust, while a low agreement rate to correct
els.Forinstance,white-boxmodelsincludedecisiontreesand decisionsmeansundertrust[12].Inself-reportedmeasurements,
linearmodels.Second,thereareblack-boxmodelsthatprovide researcherseitherutilizewell-developedquestionnairesorself-
no parameter access or are too complex to be explained in a designedones,withtheexceptionof[4]whichconductsasemi-
human-understandable way [152]. These include ensembling structuredinterviewtoexploreuseropinions.Severalworks[6],
techniquessuchasRandomForestsorneuralmodels. [11], [13], [16], [17], [18], [19], [24], [27] propose their own
As for explanation techniques, we identified five key types questionnaires.Amongthese,asubgroup[13],[16],[18],[19],
in the scope of the surveyed papers (rows of Table III). [24] simply asks users to rate a single statement such as “I
Most frequently used are feature-based (attribution) explana- trust the system’s recommendation/decision”, which is named
tions,forinstance,SHAP(Shapleyadditiveexplanations[147]) as one-dimensional trust by [8]. When deploying previously

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2109
proposed questionnaires [2], [3], [5], [7], [8], [10], [21], [22], failure prediction measures the accuracy of users’ prediction
[23], [157], Trust in Automation [158] is the most commonly whenthemodelpredictioniswrong.
used one, in which the underlying constructs of trust between SubjectiveUnderstanding:Besidestheobjectiveunderstand-
humanandcomputerizedsystemsareexplored. ingwhichissupportedbyperformanceindicators,understand-
2) Understanding: An important goal of explanation tech- ingofamodelmaybesubjective,i.e.,itmaydependonauser’s
niques is to foster users’ understanding of complex ML sys- own perception. The most commonly used applications that
tems. An important separation has to be made between users’ measuresubjectiveunderstandingarevariousrecommendation
perceivedunderstandingandtheiractualcomprehensionofthe systemsetups[16],[33],[34],[38].
underlyingmodel,asthetwooftendonotagree[35],[40].Cheng Most of the works assess the subjective understanding of a
etal. [22]explicitlydifferentiatebetweenobjectiveunderstand- user with a post-task questionnaire. Guo et al. [7] adapted a
ingandself-reportedunderstanding,whichwetermsubjective popularquestionnairedesignedforrecommendationsystemsby
understanding in this work. While subjective understanding is Knijnenburgetal. [160],whileBelletal.[39]accommodated
usually measured through questionnaires, measuring objective thequestionnairewhichoriginallyintendedtomeasurethein-
understandingrequiresaproxytaskwheretheusers’understand- telligibility of differenet explanations by Lim and Dey [161].
ingisputtoatest.Additionally,userstudiescanberuntoassess On the other hand, agreement to simple subjective statements
howwelluserscanunderstandtheexplanationitself(andnotthe such as “I understand this decision algorithm” [22], “I un-
underlyingmodel).Thiscanbeanimportantsanitycheckandis derstandhowtheAI...”[13],[17]or“Theexplanation(s)help
particularlyusedinthedomainofconceptualexplanations[62], metounderstand...”[33]canbecollectedtoassesssubjective
[159],wheretheintelligibilityofconceptsneedstobeverified. understanding.
We refer to the third category as understanding of explana- 3) Usability: UsabilityisakeyconcernofeveryHCIsystem
tionsbutdeferitsdetailedfindingstoAppendixC.3,available andthusappliestoalmostalldomains.Thisisreflectedinthe
online. surveyed papers, where usability is studied in a wide range
ObjectiveUnderstanding:Worksinthesubdomainofobjec- of setups and contexts. We also include application-specific
tive understanding deploy proxy tasks to verify users’ under- performancemeasuresinthiscategory.
standingofamodel’sinnerworkings.Themostcommonlycon- Basedonthemeasurementsintheuserstudies,werefinedus-
sidereddomaininworksonunderstandingisfinance[35],[39], abilityintomeasuresofhelpfulness,workload(cognitiveload),
[40],[47],[48],[49],[53]followedbyimageclassification[13], satisfaction, ease of use and detecting undesired behaviors of
[21],[52].Oneofthemostcriticaldesignchoiceswhenassessing thesystem,asshowninTableI.Toassessworkload(cognitive
objectiveunderstandingistheselectionofasuitableproxytask. load),NASA-TLXscale[162]isusedin[3],[6],[16],[21],[66],
Doshi-VelezandKim[119]arguethatthetaskshould“maintain whileAbduletal. [48]measurecognitiveloadbycapturingthe
theessenceofthetargetapplication”thatisanticipated.Oneof log-reading time of memorizing the explanation. Most of the
the most prominent tasks is forward simulation [119], [140]. worksuseself-designedquestionnairesorstatementstomeasure
Thistaskdemandssubjectsthataregivenaninputtosimulate, satisfaction[6],[16],[18],[19],[29],[30],[69],[70],however,
i.e.,predict,themodel’soutput.Theextenttowhichparticipants theExplanationSatisfactionScale[163]canbedeployedasan
can successfully provide the model’s output is also referred to established alternative [1], [47]. Helpfulness can be assessed
assimulatability[140].However,scholarshavedesignedmany bysimplyaskingforsubjective ratings oftheexplanations for
more tasks to quantify understanding and applied them across accomplishing a specific task [13], [46], [56], [65], [67], [68].
avarietyofdatamodalities(cf.Table2inAppendix,available Colleyetal. [3]useanadaptedversionoftheSystemUsability
onlineforanexhaustivelisting). Scaleproposedin[164].
We briefly describe other common tasks below. A special Using model explanations to audit models is one purpose
variant of forward simulation is called relative simulation. In of explainability [129]. Some of the surveyed works study
thistask,userspredictwhichexampleoutofapredefinedchoice howmodelexplanationscanassistusersindetectingundesired
will have the highest prediction score (or class probability). A behaviors of models. These issues mainly include (perceived)
manipulationorcounterfactualsimulationtask[119]asksusers unfairnessinthemodeldecision-making[38],[74],[78],[79],
to manipulate the input features in such a way that a certain biases in models [72] or features [57], and wrong decisions
modeloutcome(counterfactual)isreached.Users’performance (failures)[24]inthestudiedpapers.Adetailedsummaryoftypes
onthistaskcanbeusedasaproxyfortheirunderstanding.Lip- of undesired behaviors is listed in Table VI. In the undesired
ton[140]pointedoutthatsimulatabilitycanonlybeareasonable behaviordetection,theeffectivenessofexplanationsisevaluated
measure,ifthemodelissimpleenoughtobecapturedbyhumans byobjectiveperformancemeasures,suchasthenumberofbugs
andthatsimplertasksarerequiredotherwise.Anexamplecould identified [71], the share of participants that identify a certain
be a feature importance query, where users have to tell which bias[57,FirstExperiment]orbythedeviationsbetweenmodel
features are actually used by the model. A directed and more predictions and human predictions for unusual samples [53].
localversionofthistaskismarginaleffectsqueries,wherethe Theperceptionofusersregardingfairtreatmentbyasystemhas
subjectspredicthowchangesinagiveninputfeaturewillaffect primarily been researched in high-stakes applications such as
theprediction(e.g.,“DoesincreasingfeatureXleadtoahigher grantingloans[27]orgrantingbailforcriminaloffenders[73],
predictionofY beingclass1?”).Becauseexplanationsshould [74],[75].Forexample,[73],[74],[75]investigatethefairness
allow the identification of weaknesses in models, the task of ofCOMPAS,acommercialcriminalriskestimationtoolthatwas

2110 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
TABLEIV
EXPERIMENTALDESIGNSINCOREPAPERS
|     |     |     |     |     |     |     | Fig.2. Distributionofparticipantnumbersinthesurveyeduserstudiesby |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
designandparticipanttype(eachbarrepresentsonestudy).Per-designmeans
areindicatedinbold.
usedintheUStohelpmakejudicialbaildecisions.Itisalsocon-
sideredineverydayuse-casessuchasnews[38]andmusic[77]
recommendations, or possible career suggestions [76], where Mechanical Turk. For instance, Ooge et al. [8] use 12 school
a bias in the underlying system can be to the detriment of the studentspercondition.Someauthorsplaceparticularemphasis
user.Astheassessmentoffairnessisaverysubjectivematter, onparticipantsbeingsimilartotheaveragedemographic[73],
[75].
questionsregardingperceivedfairnessareprevalent,e.g.,“how
the software made the prediction was fair” [74], which can be Theconditionsusuallyincludethedifferentexplanationtech-
answered on 5- or 7-point Likert scales [2], [27], [38], [73], niquesincombinationwithotherparameterssuchasthemodel,
|                  |       |        |              |     |             |        | data set, | data modality, |     | or a number | of  | features | used as in- |
| ---------------- | ----- | ------ | ------------ | --- | ----------- | ------ | --------- | -------------- | --- | ----------- | --- | -------- | ----------- |
| [74],[75]. Among | these | works, | an effective |     | explanation | is the |           |                |     |             |     |          |             |
onethatcaneitherincreaseordecreasethefairnessperceptions, dependent variables. Note that a full grid design with many
independentvariablesmayquicklyresultinaveryhighnumber
sincetheaimofexplanationsistoshowfairnessorunfairness.
An exhaustive overview of measures for usability is given in ofconditions,whichinturnrequiresmanyparticipants.Theout-
TableIVoftheAppendix,availableonline. comevariableofinterestiscommonlymeasuredonanumerical
|             |               |     |              |     |     |         | or ordinal | scale | right away, | however, | in  | the fairness | domain, |
| ----------- | ------------- | --- | ------------ | --- | --- | ------- | ---------- | ----- | ----------- | -------- | --- | ------------ | ------- |
| 4) Human-AI | Collaboration |     | Performance: |     | The | goal of |            |       |             |          |     |              |         |
human-AI teaming is to improve the performance in AI- qualitativeanalysesaresometimesobtainedthroughconducted
interviewsorwrittenresponses[2],[27],[73].
| supported decision-making |     | above | the | bar set | by humans | or an |     |     |     |     |     |     |     |
| ------------------------- | --- | ----- | --- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
AIalone[89].Improvinghumanperformancewiththehelpof The statistical analysis directly follows from this design. If
AIhasbeenconsideredingames[10],[88],questionanswering one is interested in identifying significant differences between
|     |     |     |     |     |     |     | the groups, | common | statistical | hypotheses |     | tests | are used. For |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ----------- | ---------- | --- | ----- | ------------- |
tasks[89],[91],deceptiondetection[25],[90]andtopicmodel-
ing[29],[30]. overallcomparison,oneortwo-wayANOVAtestsarethemost
|          |        |            |     |         |          |       | commonly | used | statistical | tool. | Interesting | post-hoc | compar- |
| -------- | ------ | ---------- | --- | ------- | -------- | ----- | -------- | ---- | ----------- | ----- | ----------- | -------- | ------- |
| The most | common | assessment | is  | to rate | AI-aided | human |          |      |             |       |             |          |         |
performancebythepercentageofcorrectlypredictedinstances isonsbetween twogroups can bemade withastandard T-test,
inthedecision-makingprocess[25],[89],[90].Palejaetal. [10], if the data is normally distributed with equal variance, or by
|     |     |     |     |     |     |     | using non-parametric |     | tests | such | as the | Wilcoxon | rank-sum |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | ---- | ------ | -------- | -------- |
however,definetheperformanceasthetimetocompletethetask.
In[88],performanceismeasuredinagame-basedapplication, test (also known as Mann-Whitney U-test) for comparison of
chess,usingawinningpercentage(whichiscommonlyusedin two populations (e.g, [57]) or the Tukey HSD test (e.g., [49])
|     |     |     |     |     |     |     | for multiple | populations. |     | When | running | multiple | post-hoc |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | ---- | ------- | -------- | -------- |
sports)aswellasapercentilerankofplayermoves.
|     |     |     |     |     |     |     | tests, some | works | make | use of | the | Bonferroni | correction |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ---- | ------ | --- | ---------- | ---------- |
(e.g,[57]).
| C. ExperimentalDesignandAnalysis |     |     |     |     |     |     |                     |     |     | 30%    |     |            |         |
| -------------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------ | --- | ---------- | ------- |
|                                  |     |     |     |     |     |     | 2) Within-Subjects: |     |     | Around | of  | the papers | use the |
Therearethreecommonexperimentalsettingswhenconduct- within-subjects design, where each participant sequentially
ing user evaluation: between-subjects (or between-groups) de- passes through all conditions and provides feedback. Fewer
signs,within-subjectsdesigns,andmixeddesignsthatcombine participants are recruited in within-subjects experiments com-
elementsofboth.Anoverviewofthedesignsfoundinthecore paredtothebetween-subjectsones.Hence,theyareparticularly
papers and their participant numbers is presented in Table IV popularwhenparticipantswithrestrictivecharacteristics,such
andFig.2,respectively. asdomain-specificprofessionalexpertise,arerequired.Forex-
1) Between-Subjects: With slightly above 55% of the user ample, Suresh et al. [9] and Rong et al. [26] recruit fourteen
studiesconductedinabetween-subjectsmanner,i.e.,onesubject medicalprofessionalsandfiveradiologistsintheiruserstudies,
is only exposed to one condition, this design choice is most respectively.Thesmallnumberofmedicalexpertscontributing
common in the XAI literature. The number of participants in totheuserstudyisalimitation[26],however,itisoftenthecase
thebetween-subjectsmannerusuallystartsataround30partic- in expert user research. Gegenfurtner et al. [165] evaluate 73
ipants, while it may go up to 1070 in total for 3 conditions as sourcesandpointoutthatthemajorityofthesestudiesinclude
in[17]andto1250for5conditionsin[53].However,thenumber only five, maybe ten experts. Besides the medical domain,
of participants can be limited when the studied application is other works [3], [4], [19], [21] also invite subjects with par-
designed for specific groups of lay persons, which cannot be ticularprofessionssuchasengineersinatechnologycompany.
easily recruited from the Internet platforms such as Amazon When no specific knowledge is required, however, participant

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2111
TABLEV
USERSTUDYFINDINGSWHENUSINGMODELEXPLANATIONSASEVALUATIONDIMENSIONS
numbersreachupto740alsoforwithin-subjectsdesigns[93]. V. FINDINGSOFUSERSTUDIES
Forwithin-groupsdesigns,theWilcoxonsigned-ranktest(e.g.,
Inthissection,wesummarizetheprimaryfindingsfromthe
| used by | [35], [52]) | is  | the most | common | method | to  | compare |     |     |     |     |     |
| ------- | ----------- | --- | -------- | ------ | ------ | --- | ------- | --- | --- | --- | --- | --- |
corepapers.TableVlistsfindingswithrespecttofourmeasured
| paired samples |     | for significant |     | differences. | Repeated-measures |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | ------------ | ----------------- | --- | --- | --- | --- | --- | --- | --- |
quantities.Tobuildanoverviewofthefindings,wedividepapers
ANOVAisacommonanalysistool,whenmultiplecomparisons
|     |     |     |     |     |     |     |     | according | to their evaluation | dimensions, | i.e., | the independent |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------- | ----------- | ----- | --------------- |
arerequired(see,e.g.,[35]).
variablesintheuserstudies.Whenusingthepresenceofexpla-
| 3) Mixed: | The | smallest | group | of  | studies, | about | 15%, use |     |     |     |     |     |
| --------- | --- | -------- | ----- | --- | -------- | ----- | -------- | --- | --- | --- | --- | --- |
nationsastheevaluationaspect,thefindingsaresummarizedin
| a mixture | of between- |     | and within-subjects |     |     | settings. | In these |     |     |     |     |     |
| --------- | ----------- | --- | ------------------- | --- | --- | --------- | -------- | --- | --- | --- | --- | --- |
TableV.Thelistedimpactsusingexplanationsaretobeseenin
works,subjectsarefirstassignedrandomlytoonegroup,where
comparisonwithacontrolgroupwithoutexplanations.Effects
| they are     | exposed | to         | multiple  | conditions. | Anik                | and | Bunt [2] |             |                  |              |          |              |
| ------------ | ------- | ---------- | --------- | ----------- | ------------------- | --- | -------- | ----------- | ---------------- | ------------ | -------- | ------------ |
|              |         |            |           |             |                     |     |          | are divided | into two groups: | (1) Positive | effects, | for example, |
| useknowledge |         | background | inmachine |             | learningasabetween- |     |          |             |                  |              |          |              |
increasingusertrustorunderstanding;(2)Non-positiveeffects:
| subjects | factor | to divide | the | participants | into | three | groups |     |     |     |     |     |
| -------- | ------ | --------- | --- | ------------ | ---- | ----- | ------ | --- | --- | --- | --- | --- |
theeffectcanbenegative,ornotsignificantlypositive(neural),
| (expert, | intermediate |     | and beginner), |     | while inside | each | group |     |     |     |     |     |
| -------- | ------------ | --- | -------------- | --- | ------------ | ---- | ----- | --- | --- | --- | --- | --- |
oramixtureofdifferenteffects(e.g.,feature-basedexplanations
| participants | interact  | with   | explanations |            | in the      | context | of four |               |             |                |              |          |
| ------------ | --------- | ------ | ------------ | ---------- | ----------- | ------- | ------- | ------------- | ----------- | -------------- | ------------ | -------- |
|              |           |        |              |            |             |         |         | have positive | effects but | counterfactual | explanations | do not). |
| different    | scenarios | (e.g., | facial       | expression | recognition |         | or au-  |               |             |                |              |          |
Beyondtheexplanationsthemselves,otherpossibleevaluation
| tomated | speech | recognition). |     | Dominguez | et  | al. | [16] make |     |     |     |     |     |
| ------- | ------ | ------------- | --- | --------- | --- | --- | --------- | --- | --- | --- | --- | --- |
dimensionssuchasthatmighthaveanimpactontheperception
thepresenceofexplanationsabetween-subjectsconditionand
ofXAI,forinstance,AItechnologyliteracy,modelperformance,
| different | types | of explanations |     | a within-subjects |     | factor | in the |     |     |     |     |     |
| --------- | ----- | --------------- | --- | ----------------- | --- | ------ | ------ | --- | --- | --- | --- | --- |
orthedimensionalityofthedata.Insteadofusingthemerepres-
groupwithmodelexplanations.Aparticularchallengeforsuch
enceofexplanations,manyworkscomparedifferentexplanation
astudydesignisthatstatisticaltoolsfromboththeindependent-
techniqueswitheachother(seeAppendixD,availableonlinefor
| samples | and | dependent-samples |     | categories |     | need | to be |     |     |     |     |     |
| ------- | --- | ----------------- | --- | ---------- | --- | ---- | ----- | --- | --- | --- | --- | --- |
moredetails).
combined.

2112 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
TABLEVI the pronoun “I” would gain more trust of users than the ex-
OVERVIEWOFRESULTSFORUNDESIREDBEHAVIORDETECTIONUSINGMODEL
planationsformalizedina“help-provider”style.Nevertheless,
EXPLANATIONS
However,theoppositeresultisfoundandusingself-referential
expressionresultedinloweraffectivetrust.Modelperformance
together with model explanation was studied in [17] for an
imagerecognitiontask.Theauthorsfoundoutwhenimageswere
recognized (high model performance), users feel the system
morecapable(“capability”isdefinedasabeliefoftrust).
Understanding:Thefundamentalquestioninthissubdomain
is to find out which explanation technique is most beneficial
for increasing the user’s understanding of a machine learning
model. As pointed out earlier, understanding can be measured
bothinasubjectiveandobjectivemanner.
As various research questions and findings are addressed Wefirstdiscussresultsonobjectiveunderstanding.Thegoal
in 97 core papers, many papers compare explanation types in of increasing objective understanding was explicitly posed by
ordertochoose apreferableone,itisnotpossibletocover all Alqaraawi et al. [54] who reported that saliency maps have
resultsinonetable.Basedonthem,weoutlinesomeinteresting a positive effect on understanding. Wang and Yin [12] show
trendsintheeffectivenessofexplanationsonuserexperience:(1) thatcounterfactualexplanationsandfeatureimportanceincrease
Explanationsareeffectiveinimprovingusers’subjectiveunder- usersobjectiveunderstanding.Onthecontrary,Sixtetal. [57]
standing;(2)Theeffectivenessofexplanationsinincreasinguser findnoneoftheirexaminedexplanationtechniques(counterfac-
trustandusabilityofmodelsisnotclear;(3)Explanationsarenot tuals,conceptualexplanations)superiortoabaselinetechnique
good at convincing users that models are fair; (4) Interactivity consisting of example images for each class and the work by
of the model has positive impact on user trust, understanding Hase and Bansal [40] reveals that many explanations (includ-
and model usability. The first three statements can validated inganchors,prototypes)havenoeffectinincreasingobjective
throughthenumberofpapersobtainingpositiveornon-positive understanding, which LIME on tabular data being the only
effectsineachcategory,whilethelastfindingisextractedfrom exception.Apartfromtheexplanation,severalotherfactorshave
TableVintheAppendix,availableonline,whichdetailsfindings been identified to have an effect on objective understanding.
with on other independent variables. We encourage the reader HaseandBansal[40]suggestthatthedatamodalitymayhavea
toconsidertheshortsummaryofprimaryfindingsinthetables non-negligibleimpactonhowdifferentexplanationtechniques
andcheckforfurtherdetailsaccordingtotheirspecificinterests. increase understanding. Some results highlight that the choice
In the following section, we highlight some findings for each of proxy task is influential. Arora et al. [50] show that their
categoryofmeasurement. manipulatablitytaskrevealeddifferencesremainedhiddenwhen
Trust:Amongthepaperscomparingtheeffectofusingexpla- forwardsimulationisused.Inspiteofthesefindings,Buçincaet
nations to using no explanations, or placebo (randomly gener- al. [13]underlinethatpreferredexplanationsmaybedifferent
ated)explanations[8],[25],abouthalfofthepapersvalidatethat in a real-world application from a simulated one. Regarding
explanationshaveapositiveimpactonusertrust[1],[8],[10], the type of model, there is disagreement on whether white or
[13],[16],[25],[27],[28],whiletheotherhalfcannotverifythis black-boxmodelscanleadtoincreasedobjectiveunderstanding.
hypothesis[3],[11],[12],[21],[22],[24].Forinstance,Colleyet Whileblack-boxmodelswithoutexplanationsresultedinhigher
al. [3]investigatedtheexplanationsinanautonomousdriving simulation performance than white-box models with SHAP
task and discover that the trust is improved in simulation but valuesin[39],Chengetal. [22]observethatwhite-boxmodels
notwiththereal-worldfootage.Anotherexampleofthemixed increasesimulatabilityandalsoconcludethatinteractivityisan
effect of using explanations is found in [12], where (minimal) importantfactorwhenitcomestoobjectiveunderstanding.
evidenceisfoundthatfeature-basedexplanationshelpincrease Incomparisonwiththeobjectiveunderstanding,theresearch
appropriatetrust,butcounterfactualexplanationsdonot. question in the subdomain subjective understanding is to find
Apartfromusingexplanationsasindependentvariables,the outhowexplanationsimpactuser’sperceivedunderstanding[7],
user personalities or expertise may also affect their percep- [12],[17],[22],[32],[33],[34],[37],[56].Thereexistatrend
tions[2],[17],[18],[22],[23],[30].Millecampetal. [18]cap- ofusingmodelexplanationstoimprovesubjectiveunderstand-
turedpersonalcharacteristicsintheaspectssuchastheLocusof ing[13],[16],[17],[28],[34],[38],[167].However,Chromiket
ControldefinedbyFourier(“theextenttowhichpeoplebelieve al. [35]challengetheimprovementinperceivedunderstanding
theyhavepowerovereventsintheirlives”),NeedforCognition with the cognitive bias named illusion of explanatory depth
(“ameasureofthetendencyforanindividualtoengageineffort- (IOED)[168],whichmeansthatlaypeopleoftenhaveovercon-
fulcognitiveactivities”)orTech-Savviness(“theconfidencein fidence bias in their understanding of complex systems. Their
tryingoutnewtechnology”).However,nosignificantinteraction resultsconfirmtheIOEDissueinXAI,i.e.,questioningusers’
effectcouldbefoundbetweenthepersonalcharacteristicsand understanding by asking them to apply their understanding
thetrust.LiaoandSundar[5]studiedarecommendationsystem in practice consistently reduces their subjective understand-
asking users’ personal data with different explanations. They ing.Explanationscanhavedifferentimpactsonsubjectiveand
hypothesizedthatexplanationsina“help-seeker”styleandusing objective understandings [22], where white-box explanations

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2113
increase objective understanding but do not have significant that the performance gain of novices and experts comes from
impactonsubjectiveunderstanding.Similardisagreementshave different explanation sources. Paleja et al. [10] reveal that
been observed in multiple other works [40], [167]. Radensky explanations can improve novices’ performance but decrease
etal. [33]examinethejointeffectsoflocalandglobalexpla- experts’ performance. Additionally, less complex models
nations in a recommendation system and their results provide with explanations can better convince humans in correct
evidencethatbotharebetterthaneitheralone. decisions[90].
Usability:Similartotrust,itisnotclearwhetherexplanations
areeffectiveinimprovingusers’perceptionsofhelpfulness,sat-
VI. AGUIDELINEFORXAIUSERSTUDYDESIGN
isfactionorotherdimensionsofusability.Forinstance,in[16],
[30],[47],theexplanationshaveapositiveeffectonsatisfaction, Learning from the best practices of the previous works, we
whilenosignificanteffectsonsatisfactionareobservedin[18], summarizeahandyguidelineforXAIuserstudy,whichserves
[19], [29], [69]. Parallel to trust, Smith-Renner et al. [29] asachecklistforXAIpractitioners.Thisguidelinecontainssug-
provide evidence for the hypothesis that it is harmful to user gestionstoavoidpitfallsthatresearcherscouldeasilyoverlook.
trust and satisfaction to show explanations by highlighting the Weintroduceourguidelinesintheorderofbefore,duringand
importantwordsinatextclassificationtask.Astrongcorrelation after user studies, which reflects user study design, execution
betweenself-reportedtrustandsatisfactioncanalsobeobserved anddataanalysis,respectively.
in [3], where explanations have a positive impact in a simu- Before the User Study: When designing a user study, the
lateddrivingenvironment,butnosignificanteffectswhenusing firststepistodecidewhattomeasure.Todefinethemeasured
real-worlddata.Beyondexplanations,Nouranietal. [56]study quantities, one can consider two alternatives: using a general
the order of observing system weakness and strengths, which definitionoranapplication-basedquantitythatisspecifictothe
reveals that encountering weakness firstresults in a lower rate application at hand. The former one refers to a quantity that
ofusageofsystemexplanationsthanencounteringstrengthfirst. is borrowed from previous well-established research, such as
Schoeffer etal. [27] find outthatshowing featureimportance using “trust in automation” [2], [3], [21] or “general trust in
scoresorcounterfactualexplanations(oracombinationofboth) technology” [7], [23]. To further construct “trust” as a quanti-
for explaining decisions helps increase the perceived fairness, tative measurement, one needs to examine how existing work
whereashighlightingimportantfeatureswithoutscoresdoesnot. has conceptualized “trust” in both social sciences context as
However, several studies don’t show a significant difference wellasXAIandtechnicalcontext[169].Theapplication-based
between scenarios with and without explanations [27], [38], quantitydependsontheapplicationgoal,forinstanceinachess
[78].Effectsofexplanationsmaybedependentoninputsamples, game[88],themeasurementisthehumanwinningpercentage
asshownin[67].TheauthorsshowthatbothDebiased-CAMand withthehelpofmodelexplanations(Human-AIcollaboration).
Biased-CAMimprovethehelpfulnessforaweaklyblurredim- FromTableV,wecanseethatpreviousworkshavefrequently
age,however,thereisnosignificantimprovementforunblurred struggledtoprovetheeffectivenessofXAIevenwithrespectto
orstronglyblurredimages.Whenusedtoassistusersindetecting acontrolgroupthatiswithoutexplanation.Whenonlydifferent
undesired behaviors, model explanations are likely to identify explanation techniques are considered, there will always be
various types of problems that exist within models or data, as one winner explanation, but the overall benefit will remain
demonstratedby[57],[71],[72].However,successfuldetection undisclosed (see examples in Appendix D, available online).
is not guaranteed. For example, Poursabzi-Sangdeh et al. [53] Therefore, it is important to compare with a baseline without
showthatuserswithmodelexplanationsarelessabletoidentify explanations to rigorously show the strength of XAI. When
incorrectpredictions.Alimitationofcurrentdetectionmethods a comparative design is explicitly desired, baselines such as
is that users may have varying assessments, such as perceived randomexplanations[28],[41],[62]).
unfairnessandirrelevance[53],[71],[73],regardingthefeatures Whendeployingaproxytask,itsdifficultyshouldbegauged
usedinmodelsfordecision-making.Duetothislimitation,the andmonitoredcarefully.Inthepast,theforwardsimulationtask
effectiveness of methods assessed through self-reported data hasbeencriticizedasbeingunrealisticallycomplexfordomains
may face challenges in generalizability as discussed in [73]. such as computer vision [54]. Thus, other proxy tasks such as
Yet, these methods generally offer a one-size-fits-all solution, featureimportancequeries[57]ormanipulatabilitychecks[32],
failingtoaccountforvariationsinindividualassessments. [50]wereproposed.Anotherimportantpointistochooseaproxy
Human-AI Collaboration Performance: A strain of task that is simplified, but features many characteristics of the
works [25], [88], [90], [91], [95], [96], [96] show that application in mind [119]. Notably, the proxy task should be
viewing explanations can improve human accuracy in making designedclosetothefinalanticipatedapplication,asevenslight
decisions, especially with feature-based explanations taking differencesinthetasksmayvoidthevalidityofthefindingson
text data as input [25], [90], [91]. When using example-based theproxytasksintherealworld[13].
explanations in text classification, there is no improvement The measurement is often dependent on the definition of
in human performance [25]. Likewise, utilizing explanations the measured quantity. For instance, in [58], the objective
has no significant impact on human performance in [89], understanding is measured as failure prediction (the accu-
[92], but simply showing model predictions has a positive racy of user prediction when the model prediction is wrong).
effect in [92]. Experts and novices perceive explanations For subjective measurements such as subjective understand-
differently,forexample,FengandBoyd-Graber[91]conclude ingortrust,one-dimensionalmeasures(i.e.,simplyratingone

2114 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
questionsuchas“Doyoutrustthemodelexplanation?”)have shouldleavetheirbackpacks,waterbottles,andlunchboxes)and
thedrawbackthattheycannotcompletelyreflectdifferentcon- plansforunexpectedsituations(e.g.,uncooperativeparticipants
structs of measured quantities [8]. Moreover, subjective ques- andmultifunctionalsystems).Howtoobtainparticipants’con-
tions and behavioral measurements often appear to be weakly sent should be an important part of the procedure. Additional
correlated.Forexample,theusersstatethattheytrustmodelbut procedureisrequiredforobtainingconsentwhenworkingwith
they do not really follow the model suggestions [11]. Similar vulnerablepopulations(e.g.,childrenandpregnantwomen),in
findingshavebeenmadewithrespecttoobjectiveandsubjective which case alternative consent procedures might take place.
understanding[12],[35],[40].Toovercomethislimitation,both Another benefit of pre-designing the experiment script is to
self-reportedandobservedmeasuresshallbeusedinparallel. fine-tune the language to avoid inadvertent cues. Researchers
Besides the measures introduced in Section IV-B, there are can unintentionally pass on their expectations to participants
severalpsychologicalconstructsthatcanbedeployedtoevaluate through verbal and nonverbal behavior, which might result
multiple facets of the interaction between humans and XAI. in participants’ skewed performance towards the researchers’
Forinstance,thesubjectivetaskvalueintheexpectancy-value desire [169]. To ensure a sound experiment procedure and to
frameworkisoftenusedtoanalyzesubjectivemotivationtotake protecttheintegrityofthedata,itisworthwhiletoputinmuch
any actions [170], which is not thoroughly studied in the XAI efforttodesignadetailedexperimentscript.
experience yet. The subjective task value consists of intrinsic During the User Study: A sufficient number of participants
value(enjoyment),attainmentvalue(importanceforone’sself), istheprerequisiteofasoliduserstudyanalysis.Togetarough
utilityvalue(usefulness),andcost(theamountofeffortortime estimate of common sample sizes, we refer the reader to the
needed) [170], [171]. A good explanation interface should be participant statistics in Fig. 2 where we analyze the subject
positivelycorrelatedwiththesubjectivetaskvalue,consequently numbersindifferentexperimentaldesigns.Forinstance,around
boostingone’sinterestandmotivationtousethemodelexpla- 350userswithoutanyspecificexpertiseareaveragelyrecruited
nation. With regard to the cost of using model explanations, in between-subject experiments. However, we would like to
cognitive load is popularly measured in the current literature underlinethattherequirednumberofparticipantsishighlyspe-
with conventional Likert scales [162], [172]. Cognitive load cifictothestudydesignandshouldbedeterminedindividually,
researchersstudythevalidityofdifferentvisualappearancesin for instance by conducting a statistical power analysis [177].
ratingscalesbeyondnumericalLikertscales,i.e.,pictorialscales Additionally,recruitedparticipantsshouldhavethesameknowl-
suchasemoticons(faceswithdifferentemotions),orembodied edgebackgroundastheendusersthatapplicationsaredesigned
pictures of different weights [173]. Their results demonstrate for.Forinstance,whenevaluatinganinterfaceexplainingloan
that numerical scales are more proper in complex tasks while approvaldecisionstobankcustomers,itisnotpropertoinclude
pictorialscalesareforsimpleones. onlystudentswhosemajoriscomputerscience,sincetheymay
Pre-registrationusingonlineplatformssuchasAsPredicted1 have prior knowledge of how model explanations work. Note
has become a common practice in recent years [174]. In this thatthedesignofanAIapplicationrequiresdifferentaudiences
process,researcherssubmitadocumentdetailingtheirplanned acrosstheprojectcycle,thusmodelexplanationsneedtoevolve
studyonlinebeforeinitiatingthedatacollection.Amongother aswell[178].
details,thepre-registrationincludesthemeasuredvariablesand Toupholdhigh-qualitystandardsofthecollecteddata,atten-
hypotheses,dataexclusioncriteria,andthenumberofsamples tion or manipulation checks are essential to filter out careless
thatwillbecollected.Anexhaustivepre-registrationcanprovide feedback. This particularly applies to long surveys or online
evidenceagainstthefindingsbeingaresultofselectivereporting surveyswithlayusers.Kungetal. [179]justifytheuseofthese
orp-hacking[175]andthusstrengthenthecredibilityofastudy. checks without compromising scale validity. In within-subject
Expertinterviewsandpre-studiesfollowingathink-aloudproto- experiments,arandomorderofconditionsisnecessarytoavoid
col[176],e.g.,inthereferences[32],[46],areoftenmentioned order effect [1]. Participants can learn knowledge of data or
ashelpfultoolstodeveloptheexplanationsystemandthestudy examplesshowninthepreviousconditions,andTsaietal. [6]
design and gain first qualitative insights or complement the choosetouseaLatinsquaredesigntoavoidthelearningeffect.
qualitativeanalysis[13],[65]. After the User Study: After the data collection, statistical
When preparing for a user study, it is important to plan for tests are run to find significant effects. The applicable tests
explicitstepsandtohaveabackupplanfordifferentsituations. usedaredeterminedbyexperimentaldesignsandtheformand
Before participants arrive, it is helpful to provide them with distributionofthedata.Generally,ANOVAtestsandT-testare
informationsuchaswheretheresearcherswillmeetwiththem, usually used when comparing distributions between different
what they need to bring, and how they can prepare for the conditions. Structural Equation Models (SEM) or multi-level
study.Ifconductingtheexperimentinperson,sendparticipants modelsareusedformediationanalysis.Moredetailsofstatistic
areminderthedaybeforeandprovidethemwithyourcontactin tools can be found in Section IV-C. Distributional assumption
casetheycannotfindtheexperimentsiteortheyneedtocancel checks should be applied. When Likert-type data is collected
theexperimentsession.Onceparticipantsarrive,makesurethe as in most of the questionnaires, non-parametric tests such as
researchershaveaplanthatcoversallstagesoftheexperiment. pairedWilcoxonsigned-ranktest,orKruskal-WallisHtestfor
Theprotocolshouldcoversmalldetails(e.g.,whereparticipants multiplegroupscanbeusedtoavoidnormalityassumptions.
Ifmultiplemeasuresareaggregatedintoasingleinstrument,
1[Online].Available:https://aspredicted.org it is important to assess the validity of this aggregation with

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2115
Fig.3. SummarycardsoftheguidelinesextractedfrompastXAIuserstudies.
reliability measures such as the tau-equivalent reliability (also modeling and involving users in the design phase and not just
knownasCronbach’sα).Forexample,ifobjectiveandsubjec- inapost-hocmannerduringtheevaluationphase,weexpectthe
tivemeasuresofaquantity,suchasunderstandingarecombined, developmentofXAIsolutionsthatbetterrespondtouserneeds.
it is necessary to verify that there is sufficient agreement. If Asdiscussedin[117],therearetwoaspectsofhuman-centered
multiple items (e.g., data samples or visualizations) are rated AI:(1)AIsystemsthatunderstandhumanswithasociocultural
by several subjects, statistics such as Cohan’s κ as Fleiß’s κ background and (2) AI systems that help humans understand
formorethantworaters[180]canbeusedtoassessagreement them.TheformerpointcanguidethedesignofAIsystems.In
beyondchancebetweentheseratersandserveasanindication thissection,wediscussXAIresearchthatleveragesthisinsight.
forthereliabilityoftheratings. The process of explaining a machine’s decisions to human
In the final writing phase, it is essential to report sufficient users can be viewed as a teaching-learning process where the
detailsthatallowreaderstoestimatetheexplanatorypowerof XAIsystemistheteacherandthehumanusersarethestudents.
the study. On the level of participants, this should include the From a user-centered perspective, the problem of designing
totalnumberofparticipantsandhowmanyareassignedtoeach effectiveteachingmethodstoenhancethestudent’s(i.e.,user’s)
treatmentgroup,theirrecruitment,consentandincentivization, learning outcomes is essential to human-centered XAI algo-
andtheexacttreatmentconditionstheyaresubjectedto.Further- rithms. To leverage the ability of humans and address unique
more,somedescriptivestatisticsofthecollecteddatacanhelp user’s needs, it is important to review studies and findings
readersassessthecharacteristicsoftheadequacyofthestatistical frompsychologyandeducation.Thesestudiesprovideinsights
tools used. Regarding the analysis, we found it important to into how humans perceive other intelligent agents (humans or
mentionhowtheunderlyingassumptionsofthestatisticaltests artificial agents) and how they utilize limited information to
usedwerecheckedandtomentiontheexactvariantofthetest inferandgeneralize.Understandinghowhumansthinkandlearn
used (e.g., stating “a two-way ANOVA with the independent willhelpXAIdevelopersbuildanddesignsystemsthatarenot
variables X and Y” is used instead of just mentioning that only informative but also user-friendly to people with differ-
ANOVA-testisused). entbackgrounds.Inthissection,wediscussthreepedagogical
frameworks,namely(1)theexpectancy-valuemotivationtheory,
VII. FUTURERESEARCHDIRECTIONS (2) the theory of mind, and (3) hybrid teaching, to shed light
on incorporating such methods in computational approaches.
Our survey of recent and ongoing XAI research also helps
Inspired by existing work in pedagogy and XAI, we provide
usidentifyresearchgapsanddistillafewdirectionsforfuture
implications for designing future transparent AI systems and
investigations.Inthissection,wehighlightthesedirectionsand
human-centeredevaluations.
summarizeourfindings.
Expectancy-Value Motivation Theory: Human interaction
withXAIinterfacescanbeviewedasanactivitywherehumans
A. TowardsIncreasinglyUser-CenteredXAI
learn about the model’s inner workings through explanations
Weadvocatethatuser-centeredmethodsshouldbeusednot andthenachieveanunderstandingofthemodels.Thequestion
onlytoassessXAIsolutions(e.g.,throughuserstudies)butalso ofhowtoenhancetheefficiencyandtheoutcomeofthishuman
todesignthem(e.g.,throughuser-centereddesign).Byexplicitly learning process is of high importance [181]. This research

2116 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
problemiswidelyconsideredineducationalpsychologythrough ExplanationsthroughLargeLanguageModels(LLMs):The
the lens of expectancy-value motivation theory. For instance, recent rise of Large Language Models [183], [184] naturally
Hullemanetal. [171]proposetoutilizeinterventionstoincrease opens up new research directions. There is a growing interest
the perception of usefulness (utility value) to subsequently in- in leveraging their unprecedented capabilities [185] to offer
creasemotivationandfinalperformance.Interventionhererefers explanations for model decisions [186], [187]. Through their
toidentifyingtherelevanceofmodelexplanationstotheuser’s natural language interface, LLMs offer the possibility to build
own situation, which can be a prompt question while working interactive explainers [188]. Intriguingly, textual explanations
withtheinterface.Moreover,whenutilizingmodelexplanations can also be used as subsequent inputs to LLMs which may
inhuman-AIcollaboration,explanationscanbeseenasatypeof help to solve subsequent problems and result in superior per-
“scaffolding” (promptduringatask)proposed inaconceptual formance[189].Thistechnique,referredtoaschain-of-thought
frameworkineducation. reasoning[190],opensupaninterestingresearchterritorycom-
TheoryofMind:WheninteractingwithXAIsystems,humans bininginterpretabilityandperformanceconsiderations.
form mental models of the machine learning algorithms that
reflect their belief of how the algorithms work. The formation
B. OpenResearchProblems
ofthesementalmodelscomesfromobservingexplanations or
examplesgiventothehuman,whooftensubconsciouslyapplies 1) Automatic versus Human-Subject Evaluations: With au-
theobservationsinafewexamplestothebroaderunderstanding tomaticevaluations,werefertoevaluationmethodsthatdonot
of the whole machine learning system. This incredible ability requirehumansubjects,whichcorrespondstothefunctionally-
to infer, rationalize, and summarize other intelligent agent’s groundedmetricsdiscussedin[119],[120].Thesemetricsaim
decisionsisknownastheTheoryofMind(ToM)inpsychology. totestdesiderataaroundthe“faithfulness”/“fidelity”/“truthful-
Based on this theory, the Bayesian Theory of Mind (BToM) ness”ofmodelexplanations[120],[121],[191].Faithfulnessof
provides a probabilistic framework to predict inferences that explanationsisdefinedasthatexplanationsareindicativeoftrue
people make about mental states underlying other agents’ ac- importantfeaturesintheinput[191].Theautomaticevaluations
tions. Recent work, at the intersection of XAI and robotics, aimatcapturinggeneralobjectivitywhichisindependentfrom
indicatesthathumansalsoattributeToMtoartificialagentsthat downstreamtasks,whilehumanevaluationsarecontextualized
they observe or interact with. Guided by these user-centered with specific use cases. Generally speaking, automatic evalu-
results, several works at the intersection of XAI and robotics ations and human evaluations tackle different research chal-
haveutilizedBToMtocreateasimulateduser,andthenuseitto lenges:theformerobjectivelyexamineshowtrulyexplanations
generatehelpfulexplanations. reflectmodelsandthelatteronemeasureshowhumansperceive
Hybrid Teaching: Teaching strategies for the human-to- modelsthroughexplanations(althoughthereexistingalgorithms
humansettinghavebeenwidelystudiedandmanycategoriza- for automated evaluation designed to align with human evalu-
tionsexist.Onewayofcategorizingthesestrategiesisthrough ations, which we will discuss later). All explanations used in
the following three concepts: (1) direct teaching, (2) indirect human-subjectexperimentsshouldhavesatisfyingperformance
teaching,and(3)hybridteaching.Directteachingutilizesdirect inautomaticevaluations,i.e.,theexplanationsshouldbeableto
instructions that are teacher-centered, involve clear teaching faithfullyunboxthemodel.Thisverificationstepisessentialto
objectives,andareconsistentwithclassroomorganizations.In guaranteethevalidityoftheempiricaluserstudyandtoensure
XAIapplications,directteachingmethodsgenerateexplanations thatusersarenottrickedbyunfaithfulexplanations.However,in
byselectingrepresentativeexamplesofanagent’sdecisionsto most current human-subject experiments, the functional faith-
convey the patterns in its policy. In contrast, indirect teaching fulness of explanations is not thoroughly verified beforehand.
isstudent-centeredandencouragesindependentlearning.Inthe Using unfaithful explanations could lead to the problem that
XAI perspective, methods utilizing indirect teaching provide only the placebo effect of explanations is measured. Ideally,
userswithtoolstoactivelyandindependentlyexploreanAIsys- a good explanation should be faithful to the model as well as
tem.Technically,directteachingfocusesonprovidingguidance understandablebyusers.
(usingacomputationalapproach)toassistusersinbuildingan 2) IdentifyingandHandlingConfounders: Existingresearch
understanding of a machine, whereas indirect teaching (often underscores the vulnerability of model explanation studies to
through a user interface) enables users to address individual significant confounding effects. For instance, Papenmeier et
learningpreferencesandmitigateindividualconfusionaboutthe al. [155]revealthatusertrustcanbemoreinfluencedbymodel
AI.Toleveragetheadvantagesofthetwoteachingstrategies,hy- accuracythanthefaithfulnessoftheexplanationitself.Similarly,
bridteachinghasbeenwidelyusedinhuman-to-humanteaching Yinetal. [192]demonstratethattheaccuracyscoreperceived
withanemphasisoninteractivity.Recentwork [182]indicates byusersandtheoneshowntouserscontributetotrustformation.
that hybrid teaching reduces the amount of time for a user to A different problem is that good explanations also reveal
understand an agent’s policy compared to direct and indirect weaknesses of the model. However, when seeing unexpected
teaching,andismoresubjectivelypreferredbytheparticipants. explanations, users may express their negative feelings about
Buildingonthis,futureXAIsystemscanconsiderusinghybrid themodelthroughnegativeratingsoftheexplanations.There-
teachingmethodsthat(i)generatedirectinstructionstoprovide fore,goodmodelexplanationsshouldhelpuserscalibratetheir
guidance to user’s understanding of an AI system; and (ii) trust[26],[193],i.e.,trustthemodel’sdecisionwhenitiscorrect
providemethodstoallowuserstointeractwiththeagent. but distrust it otherwise. There is a disagreement on how to

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2117
handle such cases: When evaluating model fairness, several existingwork.Yet,thelinkbetweenevaluationsthroughdiffer-
works[2],[27],[38],[73],[75]reckontheincreaseinperceived entproxytasksandreal-worldapplicationshasnotbeenmade
fairnessaspositive,whileDodgeetal. [74]definethedecrease veryexplicittodate.Buçincaetal. [13]showthattheoutcomes
as positive. Other factors, such as the temporal occurrence of of proxy evaluations can be different from a real-world task.
modelerrors(Nouranietal. [56]),andthedimensionsofmodels Morespecifically,thewidelyacceptedproxytasks,whereusers
(Rossetal. [32],Poursabzietal. [53]),alsocomeintoplay. areaskedtobuildthementalmodelsoftheAI,maynotpredict
In summary, these confounding elements suggest that users the performance in actual decision-making tasks, where users
might be led to put more trust in oversimplified, deceptive, makeuseoftheexplanationstoassistinmakingdecisions.The
or simply unfaithful explanations. To mitigate this, we rec- resultsshowthatuserstrustdifferentexplanationsintheproxy
ommend meticulous analysis, control and reporting of poten- task and the actual decision-making task. Therefore, we argue
tial confounders, such as explanation faithfulness and model that further research is required to uncover the links between
accuracy, across various test conditions. More advanced mea- current proxy tasks and on-task performance or to devise new
sureshavebeensuggestedaswell.Forinstance,Schoefferand proxytaskswithaverifiedconnectiontoactualtasks.
Kuehl’s [79] propose appropriate fairness perceptions, which 6) Simulated Evaluation as a Cost-Efficient Solution: As
measureswhetherpeopleincreaseordecreasetheirfairnessper- human-subject experiments are costly to conduct, Chen
ceptionsdependingonthealgorithmicfairnessoftheunderlying et al. [198] propose a simulated evaluation framework
model.Nevertheless,thethoroughinvestigationofconfounding (SimEvals)toselectpotentialexplanationsforuserstudiesby
factors remains a challenge. Calibrated measures that are less measuringthepredictiveinformationprovidedbyexplanations.
pronetoconfoundingcanbeavaluablestepforward. Concretely, the authors consider three use cases where model
3) MitigatingPersonalBiasesforXAI: MostXAItechniques explanations are deployed: forward simulation, counterfactual
and corresponding designed user studies provide one-size-fits- reasoning,anddatadebugging.Humanperformanceismeasured
all solutions. Individual bias, rooted in a user’s mental frame- for these three tasks with different explanations. If there is a
work,influencestheuser’sperceptionofamodel.Itshouldbe significant gap in settings of using two types of explanations,
consideredinXAIdesign,development,andevaluationproce- thesimulatedevaluationcanalsoobservesuchagapunderthe
dures.Severalstudiesthataimtoexplainreinforcementlearning sametasksettingsaswell.Meanwhile,firstattemptstosimulate
policies utilize cognitive science theories to create a model of humantextualresponsesinagivencontextusinglargelanguage
the human user [181], [182], [194], [195]. They then generate modelsshowthatmodelscanprovidesurprisinglyanthropomor-
explanationsbasedonthishumanmodelandverifythebenefits phicanswers[199].UndoubtedlyandalsoaffirmedbyChenet
oftailoringexplanationsforindividualusermodels.Withinthe al. [198],itisnotyetrealistictoreplacehumanevaluationwith
scopeofXAI,[196],[197]utilizeaBayesianTeachingframe- thesimulatedframeworkasotherfactorse.g.,cognitivebiases
work to capture human perception of model explanations. In can affect human decisions. To better simulate human evalua-
userstudies,dependingonculturalandeducationalbackground, tions,moreeffortshouldbedirectedtowardsmodelinghuman
participantsmaylikelygivedifferentfeedback[31].Thiskindof cognitiveprocesses.Concurrentlyandwithappropriatecaveats,
personalbiascanbemitigatedbydeployingalargesamplesize XAIresearchersshouldalsoleverageexistingandapproximate
andrecruitingparticipantswhoarerepresentativeofthetarget models of human cognition to enable rapid prototyping and
audience.Weadvocatethatpersonalbiasesshouldbetakeninto assessment of explanations. Section VII-A discusses several
accountintherealmofXAIdevelopment. candidate human cognition models and highlights recent XAI
4) Human-in-the-LoopandSequentialExplanations: Insev- works[181],[182]thatutilizethis“Oz-of-Wizard”paradigm.
eral relevant cases, such as online recommendation systems,
users are not only confronted with an explanation once but
VIII. CONCLUSION
instead view decisions and potential explanations repeatedly.
Recent work in this domain [35] has shown that the order of Inrecentyears,therehasbeenaproliferationofXAIresearch
decisions and explanations may indeed have an effect on user inbothacademiaandindustry.Explainabilityisahuman-centric
perception and understanding. The AI model may continue property[141]andthereforeXAIshouldbepreferablystudied
to shape the user’s mental model over time. The differences by taking humans’ feedback into account. In this work, we
betweenthesingle-useandthesequentialsettingstillremainto investigated recent user studies for XAI techniques through a
bethoroughlyinvestigated. principled literature review. Based on our review, we found
5) ProxyTasksShouldBeClosetoReal-WorldTasks: When out that the effectiveness of XAI in users’ interaction with
usingproxytaskstoevaluate models,forinstance,tomeasure ML models was not consistent across different applications,
subjectiveunderstanding,thereisagreatchoiceoftaskspresent thussuggestingthatthereisastrongneedformoretransparent
in the literature. A good proxy task should have the following andcomparablehuman-basedevaluationsinXAI.Furthermore,
features:(1)ithasclosereal-worldconnections[119];(2)users relevant disciplines, such as cognitive psychology and social
or participants have some background knowledge of the task sciences in general, should become an integral part of XAI
butnottoomuchtoaffecttheirjudgmentorperformanceduring research.
the task; (3) the task is not too complicated to implement or We comprehensively analyzed the design patterns and find-
thereexistsanexistingimplementationbutwasusedfordifferent ings from previous works. Based on best-practice approaches
purposes(i.e.,notusedforXAI);and(4)ithasconnectionsto and measured quantities, we propose a general guideline for

2118 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
human-centereduserstudiesandseveralfutureresearchdirec- [20] T.Li,G.Convertino,R.K.Tayi,andS.Kazerooni,“WhatdatashouldI
tionsforXAIresearchersandpractitioners.Thereby,thiswork protect?recommenderandplanningsupportfordatasecurityanalysts,”
inProc.ACMInt.Conf.Intell.UserInterfaces,2019,pp.286–297.
represents a starting point for more transparent and human-
[21] H.Kaur,H.Nori,S.Jenkins,R.Caruana,H.Wallach,andJ.Wortman
centeredXAIresearch. Vaughan, “Interpreting interpretability: Understanding data scientists’
useofinterpretabilitytoolsformachinelearning,”inProc.SIGCHIConf.
Hum.FactorsComput.Syst.,2020,pp.1–14.
[22] H.-F.Chengetal.,“Explainingdecision-makingalgorithmsthroughUI:
REFERENCES
Strategiestohelpnon-expertstakeholders,”inProc.SIGCHIConf.Hum.
FactorsComput.Syst.,2019,pp.1–12.
[1] C.Panigutti,A.Beretta,F.Giannotti,andD.Pedreschi,“Understanding
[23] J.Kunkel,T.Donkers,L.Michael,C.-M.Barbu,andJ.Ziegler,“Let
theimpactofexplanationsonadvice-taking:AuserstudyforAI-based
meexplain:Impactofpersonalandimpersonalexplanationsontrustin
clinicaldecisionsupportsystems,”inProc.SIGCHIConf.Hum.Factors
recommendersystems,”inProc.SIGCHIConf.Hum.FactorsComput.
Comput.Syst.,2022,pp.1–9.
Syst.,2019,pp.1–12.
[2] A.I.AnikandA.Bunt,“Data-centricexplanations:Explainingtraining
[24] D.H.Kim,E.Hoque,andM.Agrawala,“Answeringquestionsabout
data of machine learning systems to promote transparency,” in Proc.
chartsandgeneratingvisualexplanations,”inProc.SIGCHIConf.Hum.
SIGCHIConf.Hum.FactorsComput.Syst.,2021,pp.1–13.
FactorsComput.Syst.,2020,pp.1–13.
[3] M.Colley,B.Eder,J.O.Rixen,andE.Rukzio,“Effectsofsemantic
[25] V.LaiandC.Tan,“Onhumanpredictionswithexplanationsandpre-
segmentationvisualizationontrust,situationawareness,andcognitive
dictionsofmachinelearningmodels:Acasestudyondeceptiondetec-
loadinhighlyautomatedvehicles,”inProc.SIGCHIConf.Hum.Factors
tion,”inProc.ACMConf.FairnessAccountabilityTransparency,2019,
Comput.Syst.,2021,pp.1–1.
pp.1–13.
[4] U.Ehsan,Q.V.Liao,M.Muller,M.O.Riedl,andJ.D.Weisz,“Expanding
[26] Y. Rong, N. Castner, E. Bozkir, and E. Kasneci, “User trust
explainability: Towards social transparency in ai systems,” in Proc.
on an explainable ai-based medical diagnosis support system,”
SIGCHIConf.Hum.FactorsComput.Syst.,2021,pp.1–19.
2022,arXiv:2204.12230.
[5] M. Liao and S. S. Sundar, “How should AI systems talk to users
[27] J. Schoeffer, N. Kuehl, and Y. Machowski, ““there is not enough in-
whencollectingtheirpersonalinformation?effectsofroleframingand
formation”: On the effects of explanations on perceptions of infor-
self-referencingonHuman-AIinteraction,”inProc.SIGCHIConf.Hum.
mational fairness and trustworthiness in automated decision-making,”
FactorsComput.Syst.,2021,pp.1–14.
2022,arXiv:2205.05758.
[6] C.-H.Tsai,Y.You,X.Gui,Y.Kou,andJ.M.Carroll,“Exploringand
[28] U.Ehsan,P.Tambwekar,L.Chan,B.Harrison,andM.O.Riedl,“Auto-
promotingdiagnostictransparencyandexplainabilityinonlinesymptom
matedrationalegeneration:AtechniqueforexplainableAIanditseffects
checkers,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2021,
onhumanperceptions,”inProc.ACMInt.Conf.Intell.UserInterfaces,
pp.1–17.
2019,pp.263–274.
[7] L.Guo,E.M.Daly,O.Alkan,M.Mattetti,O.Cornec,andB.Knijnen-
[29] A.Smith-Renneretal.,“Noexplainabilitywithoutaccountability:An
burg,“Buildingtrustininteractivemachinelearningviausercontributed
empiricalstudyofexplanationsandfeedbackininteractiveML,”inProc.
interpretablerules,”inProc.ACMInt.Conf.Intell.UserInterfaces,2022,
SIGCHIConf.Hum.FactorsComput.Syst.,2020,pp.1–13.
pp.537–548.
[30] A.Smith-Renner,V.Kumar,J.Boyd-Graber,K.Seppi,andL.Findlater,
[8] J.Ooge,S.Kato,andK.Verbert,“ExplainingrecommendationsinE-
“Diggingintousercontrol:Perceptionsofadherenceandinstabilityin
learning:Effectsonadolescents’trust,”inProc.ACMInt.Conf.Intell.
transparent models,” in Proc. ACM Int. Conf. Intell. User Interfaces,
UserInterfaces,2022,pp.93–105.
2020,pp.519–530.
[9] H.Suresh,K.M.Lewis, J.Guttag,andA.Satyanarayan,“Intuitively
[31] A.SpringerandS.Whittaker,“Progressivedisclosure:Empiricallymoti-
assessingMLmodelreliabilitythroughexample-basedexplanationsand
vatedapproachestodesigningeffectivetransparency,”inProc.ACMInt.
editingmodelinputs,”inProc.ACMInt.Conf.Intell.UserInterfaces,
Conf.Intell.UserInterfaces,2019,pp.107–120.
2022,pp.767–781.
[32] A. Ross, N. Chen, E. Z. Hang, E. L. Glassman, and F. Doshi-Velez,
[10] R.Paleja,M.Ghuy,N.RanawakaArachchige,R.Jensen,andM.Gom-
“Evaluatingtheinterpretabilityofgenerativemodelsbyinteractivere-
bolay,“TheutilityofexplainableAIinadhochuman-machineteaming,”
construction,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2021,
inProc.Int.Conf.NeuralInf.Process.Syst.,vol.34,2021,pp.610–623.
pp.1–15.
[11] J.Schaffer,J.O’Donovan,J.Michaelis,A.Raglin,andT.Höllerer,“I
[33] M.Radensky,D.Downey,K.Lo,Z.Popovic,andD.S.Weld,“Exploring
candobetterthanyourAI:Expertiseandexplanations,”inProc.ACM
theroleoflocalandglobalexplanationsinrecommendersystems,”in
Int.Conf.Intell.UserInterfaces,2019,pp.240–251.
Proc.SIGCHIConf.Hum.FactorsComput.Syst.,2022,pp.1–7.
[12] X.WangandM.Yin,“Areexplanationshelpful?Acomparativestudy
[34] S.Hadash,M.C.Willemsen,C.Snijders,andW.A.IJsselsteijn,“Im-
oftheeffectsofexplanationsinAI-assisteddecision-making,”inProc.
proving understandability of feature contributions in model-agnostic
ACMInt.Conf.Intell.UserInterfaces,2021,pp.318–328.
explainable AI tools,” in Proc. SIGCHI Conf. Hum. Factors Comput.
[13] Z. Buçinca, P. Lin, K. Z. Gajos, and E. L. Glassman, “Proxy tasks
Syst.,2022,pp.1–9.
and subjective measures can be misleading in evaluating explainable
[35] M.Chromik,M.Eiband,F.Buchner,A.Krüger,andA.Butz,“IthinkI
AI systems,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2020,
getyourpoint,AI!theillusionofexplanatorydepthinexplainableAI,”
pp.454–464.
inProc.ACMInt.Conf.Intell.UserInterfaces,2021,pp.307–317.
[14] X.Peng,M.Riedl,andP.Ammanabrolu,“Inherentlyexplainablerein-
[36] J.Rebanal,J.Combitsis,Y.Tang,andX.Chen,“XAlgo:Adesignprobe
forcementlearninginnaturallanguage,”inProc.Int.Conf.NeuralInf.
ofexplainingalgorithms’internalstatesviaquestion-answering,”inProc.
Process.Syst.,2022,pp.16178–16190.
ACMInt.Conf.Intell.UserInterfaces,2021,pp.329–339.
[15] Y. Zhang, Q. V. Liao, and R. K. Bellamy, “Effect of confidence and
[37] U. Kuhl, A. Artelt, and B. Hammer, “Keep your friends close and
explanation on accuracy and trust calibration in AI-assisted decision
your counterfactuals closer: Improved learning from closest rather
making,” in Proc. Conf. Fairness Accountability Transparency, 2020,
than plausible counterfactual explanations in an abstract setting,”
pp.295–305.
2022,arXiv:2205.05515.
[16] V.Dominguez,P.Messina,I.Donoso-Guzmán,andD.Parra,“Theeffect
[38] E.Rader,K.Cotter,andJ.Cho,“Explanationsasmechanismsforsup-
ofexplanationsandalgorithmicaccuracyonvisualrecommendersystems
portingalgorithmictransparency,”inProc.SIGCHIConf.Hum.Factors
ofartisticimages,”inProc.ACMInt.Conf.Intell.UserInterfaces,2019,
Comput.Syst.,2018,pp.1–13.
pp.408–446.
[39] A.Bell,I.Solano-Kamaiko,O.Nov,andJ.Stoyanovich,“It’sjustnot
[17] C.J.Cai,J.Jongejan,andJ.Holbrook,“Theeffectsofexample-based
thatsimple:Anempiricalstudyoftheaccuracy-explainabilitytrade-off
explanationsinamachinelearninginterface,”inProc.ACMInt.Conf.
in machine learning for public policy,” in Proc. ACM Conf. Fairness
Intell.UserInterfaces,2019,pp.258–262.
AccountabilityTransparency,2022,pp.248–266.
[18] M.Millecamp,N.N.Htun,C.Conati,andK.Verbert,“Toexplainornot
[40] P.HaseandM.Bansal,“EvaluatingexplainableAI:Whichalgorithmic
toexplain:Theeffectsofpersonalcharacteristicswhenexplainingmusic
explanationshelpuserspredictmodelbehavior?,”inProc.58thAnnu.
recommendations,”inProc.ACMInt.Conf.Intell.UserInterfaces,2019,
MeetingAssoc.Comput.Linguistics,2020,pp.5540–5552.
pp.397–407.
[41] H. Schuff, A. Jacovi, H. Adel, Y. Goldberg, and N. T. Vu,
[19] C.-H. Tsai and P. Brusilovsky, “Beyond the ranked list: User-driven
“Human interpretation of saliency-based explanation over text,”
explorationanddiversificationofsocialrecommendation,”inProc.ACM
2022,arXiv:2201.11569,.
Int.Conf.Intell.UserInterfaces,2018,pp.239–250.

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2119
[42] S.Bang,P.Xie,H.Lee,W.Wu,andE.Xing,“Explainingablack-box [64] I. Laina, R. Fong, and A. Vedaldi, “Quantifying learnability and de-
byusingadeepvariationalinformationbottleneckapproach,”inProc. scribability of visual concepts emerging in representation learning,”
AAAIConf.Artif.Intell.,2021,pp.11396–11404. Adv.NeuralInf.Process.Syst.,vol.33,2020,pp.13112–13126.
[43] S.S.Kim,N.Meister,V.V.Ramaswamy,R.Fong,andO.Russakovsky, [65] Y. Wang, P. Venkatesh, and B. Y. Lim, “Interpretable directed di-
“HIVE:Evaluatingthehumaninterpretabilityofvisualexplanations,”in versity: Leveraging model explanations for iterative crowd ideation,”
Proc.Eur.Conf.Comput.Vis.,2022,pp.280–298. in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2022,
[44] M.Szymanski,M.Millecamp,andK.Verbert,“Visual,textualorhybrid: pp.1–28.
Theeffectofuserexpertiseondifferentexplanations,”inProc.ACMInt. [66] D.L.Arendt,N.Nur,Z.Huang,G.Fair,andW.Dou,“Parallelembed-
Conf.Intell.UserInterfaces,2021,pp.109–119. dings:Avisualizationtechniqueforcontrastinglearnedrepresentations,”
[45] G.Plumb,M.Al-Shedivat,Á.A.Cabrera,A.Perer,E.Xing,andA.Tal- inProc.ACMInt.Conf.Intell.UserInterfaces,2020,pp.259–274.
walkar,“Regularizingblack-boxmodelsforimprovedinterpretability,” [67] W.Zhang,M.Dimiccoli,andB.Y.Lim,“Debiased-CAMtomitigateim-
inProc.Int.Conf.NeuralInf.Process.Syst.,2020,pp.10526–10536. ageperturbationswithfaithfulvisualexplanationsofmachinelearning,”
[46] W. Zhang and B. Y. Lim, “Towards relatable explainable ai with the inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2022,pp.1–32.
perceptualprocess,”inProc.SIGCHIConf.Hum.FactorsComput.Syst., [68] J.Gao,X.Wang,Y.Wang,andX.Xie,“Explainablerecommendation
2022,pp.1–24. throughattentivemulti-viewlearning,”inProc.AAAIConf.Artif.Intell.,
[47] C.Bove,J.Aigrain,M.-J.Lesot,C.Tijus,andM.Detyniecki,“Con- 2019,pp.3622–3629.
textualizationandexplorationoflocalfeatureimportanceexplanations [69] P.Kouki,J.Schaffer,J.Pujara,J.O’Donovan,andL.Getoor,“Personal-
toimproveunderstandingandsatisfactionofnon-expertusers,”inProc. izedexplanationsforhybridrecommendersystems,”inProc.ACMInt.
ACMInt.Conf.Intell.UserInterfaces,2022,pp.807–819. Conf.Intell.UserInterfaces,2019,pp.379–390.
[48] A.Abdul,C.vonderWeth,M.Kankanhalli,andB.Y.Lim,“COGAM: [70] C.-H. Tsai and P. Brusilovsky, “Explaining recommendations in an
Measuring and moderating cognitive load in machine learning model interactivehybridsocialrecommender,”inProc.ACMInt.Conf.Intell.
explanations,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2020, UserInterfaces,2019,pp.391–396.
pp.1–14. [71] A. Balayn, N. Rikalo, C. Lofi, J. Yang, and A. Bozzon, “How can
[49] K.NatesanRamamurthy,B.Vinzamuri,Y.Zhang,andA.Dhurandhar, explainabilitymethodsbeusedtosupportbugidentificationincomputer
“Modelagnosticmultilevelexplanations,”inProc.Int.Conf.NeuralInf. visionmodels?,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,
Process.Syst.,2020,pp.5968–5979. 2022,pp.1–16.
[50] S. Arora, D. Pruthi, N. Sadeh, W. W. Cohen, Z. C. Lipton, and G. [72] K. Rawal and H. Lakkaraju, “Beyond individualized recourse: Inter-
Neubig,“Explain,edit,andunderstand:Rethinkinguserstudydesign pretableandinteractivesummariesofactionablerecourses,”inProc.Int.
forevaluatingmodelexplanations,”inProc.AAAIConf.Artif.Intell., Conf.NeuralInf.Process.Syst.,2020,pp.12187–12198.
2022,pp.5277–5285. [73] N.Grgic´-Hlacˇa,E.M.Redmiles,K.P.Gummadi,andA.Weller,“Human
[51] J.Antoran,U.Bhatt,T.Adel,A.Weller,andJ.M.Hernández-Lobato, perceptionsoffairnessinalgorithmicdecisionmaking:Acasestudyof
“Gettinga{clue}:Amethodforexplaininguncertaintyestimates,”in criminalriskprediction,”inProc.WideWebConf.,2018,pp.903–912.
Proc.Int.Conf.Learn.Representations,2021. [74] J.Dodge,Q.V.Liao,Y.Zhang,R.K.Bellamy,andC.Dugan,“Explaining
[52] J.Borowskietal.,“Exemplarynaturalimagesexplain{CNN}activations models:Anempiricalstudyofhowexplanationsimpactfairnessjudg-
better than state-of-the-art feature visualization,” in Proc. Int. Conf. ment,”inProc.ACMInt.Conf.Intell.UserInterfaces,2019,pp.275–285.
Learn.Representations,2021. [75] G.Harrison,J.Hanson,C.Jacinto,J.Ramirez,andB.Ur,“Anempirical
[53] F.Poursabzi-Sangdeh,D.G.Goldstein,J.M.Hofman,J.W.Wortman studyontheperceivedfairnessofrealistic,imperfectmachinelearning
Vaughan,andH.Wallach,“Manipulatingandmeasuringmodelinter- models,” in Proc. Conf. Fairness Accountability Transparency, 2020,
pretability,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2021, pp.392–402.
pp.1–52. [76] C.Wangetal.,“DohumanspreferdebiasedAIalgorithms?acasestudyin
[54] A.Alqaraawi,M.Schuessler,P.Weiß,E.Costanza,andN.Berthouze, careerrecommendation,”inProc.ACMInt.Conf.Intell.UserInterfaces,
“Evaluating saliency map explanations for convolutional neural net- 2022,pp.134–147.
works:Auserstudy,”inProc.ACMInt.Conf.Intell.UserInterfaces, [77] N.N.Htun,E.Lecluse,andK.Verbert,“Perceptionoffairnessingroup
2020,pp.275–285. music recommender systems,” in Proc. ACM Int. Conf. Intell. User
[55] M. T. Ribeiro, S. Singh, and C. Guestrin, “Anchors: High-precision Interfaces,2021,pp.302–306.
model-agnosticexplanations,”inProc.AAAIConf.Artif.Intell.,2018, [78] R.Binns,M.VanKleek,M.Veale,U.Lyngs,J.Zhao,andN.Shadbolt,
pp.1527–1535. “‘it’sreducingahumanbeingtoapercentage’perceptionsofjusticein
[56] M.Nouranietal.,“Anchoringbiasaffectsmentalmodelformationand algorithmicdecisions,”inProc.SIGCHIConf.Hum.FactorsComput.
userrelianceinexplainableaisystems,”inProc.ACMInt.Conf.Intell. Syst.,2018,pp.1–14.
UserInterfaces,2021,pp.340–350. [79] J. Schoeffer and N. Kuehl, “Appropriate fairness perceptions? on the
[57] L.Sixt,M.Schuessler,O.-I.Popescu,P.Weiß,andT.Landgraf,“Dousers effectivenessofexplanationsinenablingpeopletoassessthefairness
benefitfrominterpretablevision?auserstudy,baseline,anddataset,”in ofautomateddecisionsystems,”inProc.Companion:CompanionPub.
Proc.Int.Conf.Learn.Representations,2022. Conf. Comput. Supported Cooperative Work Social Comput., 2021,
[58] A. Chandrasekaran, V. Prabhu, D. Yadav, P. Chattopadhyay, and D. pp.153–157.
Parikh, “Do explanations make VQA models more predictable to [80] T.Donkers,T.Kleemann,andJ.Ziegler,“Explainingrecommendations
a human?,” in Proc. Conf. Empir. Methods Natural Lang. Process., bymeansofaspect-basedtransparentmemories,”inProc.ACMInt.Conf.
2018,pp.1036–1042. Intell.UserInterfaces,2020,pp.166–176.
[59] J.Colin,T.Fel,R.Cadene,andT.Serre,“WhatIcannotpredict,Ido [81] F.Hohman,A.Head,R.Caruana,R.DeLine,andS.M.Drucker,“Gamut:
not understand: A human-centered evaluation framework for explain- Adesignprobetounderstandhowdatascientistsunderstandmachine
ability methods,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2022, learningmodels,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,
pp.2832–2845. 2019,pp.1–13.
[60] H. Shen and T.-H. Huang, “How useful are the machine-generated [82] U.Kuhl,A.Artelt,andB.Hammer,“Let’sgotothealienzoo:Intro-
interpretations to general users? a human evaluation on guessing the ducinganexperimentalframeworktostudyusabilityofcounterfactual
incorrectlypredictedlabels,”inProc.AAAIConf.Hum.Comput.Crowd- explanationsformachinelearning,”2022,arXiv:2205.03398.
sourcing,2020,pp.168–172. [83] T.Schneider,J.Hois,A.Rosenstein,S.Ghellal,D.Theofanou-Fülbier,
[61] C.-K. Yeh, B. Kim, S. O. Arik, C.-L. Li, T. Pfister, and P. Raviku- andA.R.Gerlicher,“ExplAInyourself!transparencyforpositiveUX
mar,“Oncompleteness-awareconcept-basedexplanationsindeepneu- inautonomousdriving,”inProc.SIGCHIConf.Hum.FactorsComput.
ral networks,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2019, Syst.,2021,pp.1–12.
pp.20554–20565. [84] S.Choi,K.Aizawa,andN.Sebe,“FontMatcher:Fontimageparingfor
[62] A. Ghorbani, J. Wexler, J. Y. Zou, and B. Kim, “Towards automatic harmoniousdigitalgraphicdesign,”inProc.ACMInt.Conf.Intell.User
concept-basedexplanations,”inProc.Int.Conf.NeuralInf.Process.Syst., Interfaces,2018,pp.37–41.
2019,pp.9277–9286. [85] P.LeBras,D.A.Robb,T.S.Methven,S.Padilla,andM.J.Chantler,
[63] T.Leemann,Y.Rong,S.Kraft,E.Kasneci,andG.Kasneci,“Coherence “Improving user confidence in concept maps: Exploring data driven
evaluationofvisualconceptswithobjectsandlanguage,”inProc.Int. explanations,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2018,
Conf.Learn.RepresentationsWS,2022. pp.1–13.

2120 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
[86] R.Shang,K.K.Feng,andC.Shah,“WhyamInotseeingit?under- [111] P. M. Addo, D. Guegan, and B. Hassani, “Credit risk analysis using
standingusers’needsforcounterfactualexplanationsineverydayrecom- machineanddeeplearningmodels,”Risks,vol.6,no.2,p.38,2018.
mendations,”inProc.ACMConf.FairnessAccountabilityTransparency, [112] N. Van Berkel, J. Goncalves, D. Hettiachchi, S. Wijenayake, R. M.
2022,pp.1330–1340. Kelly,andV.Kostakos,“Crowdsourcingperceptionsoffairpredictorsfor
[87] J.Dodge,A.A.Anderson,M.Olson,R.Dikkala,andM.Burnett,“How machinelearning:Arecidivismcasestudy,”inProc.ACMHum.-Comput.
dopeoplerankmultiplemutantagents?,”inProc.ACMInt.Conf.Intell. Interact.,vol.3,pp.1–21,2019.
UserInterfaces,2022,pp.191–211. [113] T.Sourdin,“JudgeVrobot?:Artificialintelligenceandjudicialdecision-
[88] D.DasandS.Chernova,“Leveragingrationalestoimprovehumantask making,”Univ.NewSouthWalesLawJ.,vol.41,no.4,pp.1114–1133,
performance,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2020, 2018.
pp.510–518. [114] M.Raghavan,S.Barocas,J.Kleinberg,andK.Levy,“Mitigatingbias
[89] G. Bansal et al., “Does the whole exceed its parts? the effect of ai inalgorithmichiring:Evaluatingclaimsandpractices,”inProc.Conf.
explanationsoncomplementaryteamperformance,”inProc.SIGCHI FairnessAccountabilityTransparency,2020,pp.469–481.
Conf.Hum.FactorsComput.Syst.,2021,pp.1–16. [115] P.Tambe,P.Cappelli,andV.Yakubovich,“Artificialintelligenceinhu-
[90] V. Lai, H. Liu, and C. Tan, ““why is’ Chicago’deceptive?,” towards manresourcesmanagement:Challengesandapathforward,”California
buildingmodel-driventutorialsforhumans,”inProc.SIGCHIConf.Hum. Manage.Rev.,vol.61,pp.15–42,2019.
FactorsComput.Syst.,2020,pp.1–13. [116] D. Castelvecchi, “Can we open the black box of AI?,” Nature News,
[91] S.FengandJ.Boyd-Graber,“Whatcanaidoforme?evaluatingmachine vol.538,pp.20–23,2016.
learninginterpretationsincooperativeplay,”inProc.ACMInt.Conf. [117] M.O.Riedl,“Human-centeredartificialintelligenceandmachinelearn-
Intell.UserInterfaces,2019,pp.229–239. ing,”Hum.Behav.Emerg.Technol.,vol.1,pp.33–36,2019.
[92] Y.Alufaisan,L.R.Marusich,J.Z.Bakdash,Y.Zhou,andM.Kantar- [118] U.EhsanandM.O.Riedl,“Human-centeredexplainableAI:Towardsa
cioglu,“Doesexplainableartificialintelligenceimprovehumandecision- reflectivesociotechnicalapproach,”inProc.Int.Conf.Human-Comput.
making?,”inProc.AAAIConf.Artif.Intell.,2021,pp.6618–6626. Interact.,2020,pp.449–466.
[93] K.Z.GajosandL.Mamykina,“DopeopleengagecognitivelywithAI? [119] F.Doshi-VelezandB.Kim,“Towardsarigorousscienceofinterpretable
impactofAIassistanceonincidentallearning,”inProc.ACMInt.Conf. machinelearning,”2017,arXiv:1702.08608.
Intell.UserInterfaces,2022,pp.794–806. [120] M. Nauta et al., “From anecdotal evidence to quantitative evaluation
[94] M.Liao,S.S.Sundar,andJ.B.Walther,“Usertrustinrecommenda- methods: A systematic review on evaluating explainable AI,” ACM
tionsystems:Acomparisonofcontent-based,collaborativeanddemo- Comput.Surv.,vol.55,pp.1–42,2023.
graphicfiltering,”inProc.CHIConf.Hum.FactorsComput.Syst.,2022, [121] R. Tomsett, D. Harborne, S. Chakraborty, P. Gurram, and A. Preece,
pp.1–14. “Sanitychecksforsaliencymetrics,”inProc.AAAIConf.Artif.Intell.,
[95] G. Nguyen, D. Kim, and A. Nguyen, “The effectiveness of feature 2020,pp.6021–6029.
attributionmethodsanditscorrelationwithautomaticevaluationscores,” [122] Y. Rong, T. Leemann, V. Borisov, G. Kasneci, and E. Kasneci, “A
inProc.Int.Conf.NeuralInf.Process.Syst.,2021,pp.26422–26436. consistentandefficientevaluationstrategyforattributionmethods,”in
[96] M.R.Taesiri,G.Nguyen,andA.Nguyen,“Visualcorrespondence-based Proc.Int.Conf.Mach.Learn.,2022,pp.18770–18795.
explanationsimproveAIrobustnessandhuman-AIteamaccuracy,”in [123] D. Nguyen, “Comparing automatic and human evaluation of lo-
Proc.Int.Conf.NeuralInf.Process.Syst.,2022,pp.34287–34301. cal explanations for text classification,” in Proc. Conf. North Amer.
[97] J.Wei,J.He,K.Chen,Y.Zhou,andZ.Tang,“Collaborativefilteringand Chapter Assoc. Comput. Linguistics: Hum. Lang. Technol., 2018,
deeplearningbasedrecommendationsystemforcoldstartitems,”Expert pp.1069–1078.
Syst.Appl.,vol.69,pp.29–39,2017. [124] G.Hoffman,“Evaluatingfluencyinhuman–robotcollaboration,”IEEE
[98] S.Yang,M.Korayem,K.AlJadda,T.Grainger,andS.Natarajan,“Com- Trans.Human-Mach.Syst.,vol.49,no.3,pp.209–218,Jun.2019.
biningcontent-basedandcollaborativefilteringforjobrecommendation [125] Workshop, “ExSS-ATEC: Explainable smart systems for algorithmic
system:Acost-sensitivestatisticalrelationallearningapproach,”Knowl.- transparencyinemergingtechnologies,”inProc.25thInt.Conf.Intell.
BasedSyst.,vol.136,pp.37–45,2017. UserInterfacesCompanion,vol.1,2020.
[99] Y.Zhang,X.Chen,Q.Ai,L.Yang,andW.B.Croft,“Towardsconversa- [126] S.Mohseni,N.Zarei,andE.D.Ragan,“Amultidisciplinarysurveyand
tionalsearchandrecommendation:Systemask,userrespond,”inProc. frameworkfordesignandevaluationofexplainableAIsystems,”ACM
ACMInt.Conf.Inf.Knowl.Manage.,2018,pp.177–186. Trans.Interact.Intell.Syst.(TiiS),vol.11,no.3/4,pp.1–45,2021.
[100] S.Grigorescu,B.Trasnea,T.Cocias,andG.Macesanu,“Asurveyofdeep [127] Q.Yang,N.Banovic,andJ.Zimmerman,“Mappingmachinelearningad-
learningtechniquesforautonomousdriving,”J.FieldRobot.,vol.37, vancesfromHCIresearchtorevealstartingplacesfordesigninnovation,”
pp.362–386,2020. inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2018,pp.1–11.
[101] H.Cuietal.,“Multimodaltrajectorypredictionsforautonomousdriving [128] A.AdadiandM.Berrada,“Peekinginsidetheblack-box:Asurveyon
usingdeepconvolutionalnetworks,”inProc.Int.Conf.Robot.Automat., explainableartificialintelligence(XAI),”IEEEAccess,vol.6,pp.52138–
2019,pp.2090–2096. 52160,2018.
[102] Y. Rong, C. Han, C. Hellert, A. Loyal, and E. Kasneci, “Artificial [129] A.B.Arrietaetal.,“Explainableartificialintelligence(XAI):Concepts,
intelligencemethodsinin-cabinusecases:Asurvey,”IEEEIntell.Transp. taxonomies,opportunitiesandchallengestowardresponsibleAI,”Inf.
Syst.Mag.,vol.14,no.3,pp.132–145,May/Jun.2021. Fusion,2020,vol.58,pp.82–115.
[103] R.R.Murphy,“IntroductiontoAIrobotics,”Ind.Robot:AnInt.J.,vol.28, [130] W. Samek and K.-R. Müller, “Towards explainable artificial intelli-
no.3,pp.266–267,2001. gence,” in Proc. Explainable AI: Interpreting Explaining Visualizing
[104] K. Rajan and A. Saffiotti, “Towards a science of integrated AI and DeepLearn.,2019,pp.5–22.
robotics,”Artif.Intell.,vol.247,pp.1–9,2017. [131] N.BurkartandM.F.Huber,“Asurveyontheexplainabilityofsupervised
[105] S.Wachter,B.Mittelstadt,andL.Floridi,“Transparent,explainable,and machinelearning,”J.Artif.Intell.Res.,vol.70,pp.245–317,2021.
accountableAIforrobotics,”Sci.Robot.,vol.2,2017,Art.no.eaan6080. [132] D. V. Carvalho, E. M. Pereira, and J. S. Cardoso, “Machine learning
[106] S. H. Park and K. Han, “Methodologic guide for evaluating clinical interpretability:Asurveyonmethodsandmetrics,”Electronics,vol.8,
performanceandeffectofartificialintelligencetechnologyformedical 2019,Art.no.832.
diagnosisandprediction,”Radiology,vol.286,pp.800–809,2018. [133] L.H.Gilpin,D.Bau,B.Z.Yuan,A.Bajwa,M.Specter,andL.Ka-
[107] J. A. Sidey-Gibbons and C. J. Sidey-Gibbons, “Machine learning in gal, “Explaining explanations: An overview of interpretability of ma-
medicine:Apracticalintroduction,”BMCMed.Res.Methodol.,vol.19, chinelearning,”inProc.IEEE5thInt.Conf.DataSci.Adv.Analytics,
2019,Art.no.64. 2018,pp.80–89.
[108] R.Vaishya,M.Javaid,I.H.Khan,andA.Haleem,“Artificialintelli- [134] A. Abdul, J. Vermeulen, D. Wang, B. Y. Lim, and M. Kankanhalli,
gence(AI)applicationsforCOVID-19pandemic,”DiabetesMetabolic “Trends and trajectories for explainable, accountable and intelligible
Syndrome:Clin.Res.Rev.,vol.14,pp.337–339,2020. systems:AnHCIresearchagenda,”inProc.SIGCHIConf.Hum.Factors
[109] X.Dastile,T.Celik,andM.Potsane,“Statisticalandmachinelearning Comput.Syst.,2018,pp.1–28.
models in credit scoring: A systematic literature survey,” Appl. Soft [135] G.Montavon,W.Samek,andK.-R.Müller,“Methodsforinterpreting
Comput.,vol.91,2020,Art.no.106263. andunderstandingdeepneuralnetworks,”Digit.SignalProcess.,vol.73,
[110] M.Ala’raj,M.F.Abbod,M.Majdalawieh,andL.Jum’a,“Adeeplearning pp.1–15,2018.
modelforbehaviouralcreditscoringinbanks,”NeuralComput.Appl., [136] A.DasandP.Rad,“Opportunitiesandchallengesinexplainableartificial
vol.34,pp.5839–5866,2022. intelligence(XAI):Asurvey,”2020,arXiv:2006.11371.

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2121
[137] G.Joshi,R.Walambe,andK.Kotecha,“Areviewonexplainabilityin [163] R. R. Hoffman, S. T. Mueller, G. Klein, and J. Litman, “Metrics for
multimodaldeepneuralnets,”IEEEAccess,vol.9,pp.59800–59821, explainableAI:Challengesandprospects,”2018,arXiv:1812.04608.
2021. [164] A. Holzinger, A. Carrington, and H. Müller, “Measuring the quality
[138] R. Moraffah, M. Karami, R. Guo, A. Raglin, and H. Liu, “Causal of explanations: The system causability scale (SCS),” KI-Künstliche
interpretabilityformachinelearning-problems,methodsandevaluation,” Intelligenz,2020.
ACMSIGKDDExplorationsNewslett.,vol.22,pp.18–33,2020. [165] A. Gegenfurtner, E. Lehtinen, and R. Säljö, “Expertise differences in
[139] I.NunesandD.Jannach,“Asystematicreviewandtaxonomyofex- the comprehension of visualizations: A meta-analysis of eye-tracking
planationsindecisionsupportandrecommendersystems,”UserModel. researchinprofessionaldomains,”KI-KunstlicheIntelligenz,vol.34,
User-AdaptedInteract.,vol.27,pp.393–444,2017. no.2,pp.193–198,2020.
[140] Z.C.Lipton,“Themythosofmodelinterpretability:Inmachinelearning, [166] K.Cotter,J.Cho,andE.Rader,“Explainingthenewsfeedalgorithm:
theconceptofinterpretabilityisbothimportantandslippery,”Queue, Ananalysisofthe“newsfeedFYI,”blog,”inProc.CHIConf.Extended
vol.16,pp.31–57,2018. Abstr.Hum.FactorsComput.Syst.,2017,pp.1553–1560.
[141] Q.V.LiaoandK.R.Varshney,“Human-centeredexplainableAI(XAI): [167] D.Wang,Q.Yang,A.Abdul,andB.Y.Lim,“Designingtheory-driven
Fromalgorithmstouserexperiences,”2021,arXiv:2110.10790. user-centricexplainableAI,”inProc.SIGCHIConf.Hum.FactorsCom-
[142] V.Lai,C.Chen,Q.V.Liao,A.Smith-Renner,andC.Tan,“Towardsa put.Syst.,2019,pp.1–15.
scienceofHuman-AIdecisionmaking:Asurveyofempiricalstudies,” [168] L. Rozenblit and F. Keil, “The misunderstood limits of folk science:
2021,arXiv:2112.11471. An illusion of explanatory depth,” Cogn. Sci., vol. 26, pp. 521–562,
[143] J.J.FerreiraandM.S.Monteiro,“WhatarepeopledoingaboutXAIuser 2002.
experience?asurveyonaiexplainabilityresearchandpractice,”inProc. [169] G. Hoffman and X. Zhao, “A primer for conducting experiments in
Int.Conf.Hum.-Comput.Interact.,2020,pp.56–73. human–robotinteraction,”ACMTrans.Human-RobotInteract.,vol.10,
[144] N.Bevan,“InternationalstandardsforHCIandusability,”Int.J.Hum.- pp.1–31,2020.
Comput.Stud.,vol.55,pp.533–552,2001. [170] J.Eccles,“Expectancies,valuesandacademicbehaviors,”Achievement
[145] W.Iso,“9241–11:1998,Ergonomicrequirementsforworkwithvisual AchievementMotives,vol.58,pp.58–74,1983.
display terminals (VDTs)-Part 11: Guidance on usability,” Int. Org. [171] C.S.Hulleman,J.J.Kosovich,K.E.Barron,andD.B.Daniel,“Making
Standardization,vol.45,no.9,1998. connections:Replicatingandextendingtheutilityvalueinterventionin
[146] M. T. Ribeiro, S. Singh, and C. Guestrin, ““Why should I trust theclassroom,”J.Educ.Psychol.,vol.109,2017,Art.no.387.
you?,” explaining the predictions of any classifier,” in Proc. 22nd [172] F.G.Paas,“Trainingstrategiesforattainingtransferofproblem-solving
ACM SIGKDD Int. Conf. Knowl. Discov. Data Mining, 2016, skillinstatistics:Acognitive-loadapproach,”J.Educ.Psychol.,vol.84,
pp.1135–1144. pp.429–434,1992.
[147] S.M.LundbergandS.-I.Lee,“Aunifiedapproachtointerpretingmodel [173] K.Ouwehand,A.V.D.Kroef,J.Wong,andF.Paas,“Measuringcognitive
predictions,”inProc.Int.Conf.NeuralInf.Process.Syst.,2017,pp.4768– load:Aretheremorevalidalternativestolikertratingscales?,”Front.
4777. Educ.,FrontiersEduc.,vol.6,p.702616,2021.
[148] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and [174] J.P.Simmons,L.D.Nelson,andU.Simonsohn,“Pre-registration:Why
D. Batra, “Grad-CAM: Visual explanations from deep networks via andhow,”J.Consum.Psychol.,vol.31,pp.151–162,2021.
gradient-basedlocalization,”inProc.IEEEInt.Conf.Comput.Vis.,2017, [175] U.Simonsohn,L.D.Nelson,andJ.P.Simmons,“P-curve:Akeytothe
pp.618–626. file-drawer,”J.Exp.Psychol.:Gen.,vol.143,pp.534–547,2014.
[149] P. Voigt and A. Von dem Bussche, “The EU general data protection [176] K.A.EricssonandH.A.Simon,ProtocolAnalysis:VerbalReportsas
regulation (GDPR),” in A Practical Guide, 1st ed., Berlin, Germany: Data.Cambridge,MA,USA:MITPress,1984.
Springer,2017. [177] J.Cohen,StatisticalPowerAnalysisfortheBehavioralSciences,San
[150] B.GoodmanandS.Flaxman,“Europeanunionregulationsonalgorith- Francisco,CA,USA:Academic,2013.
mic decision-making and a “right to explanation”,” AI Mag., vol. 38, [178] S.Dhanorkar,C.T.Wolf,K.Qian,A.Xu,L.Popa,andY.Li,“Who
no.3,pp.50–57,2017. needstoknowwhat,when?:BroadeningtheexplainableAI(XAI)design
[151] C.Molnar,“Interpretablemachinelearning,”pp.26–27,2020. spacebylookingatexplanationsacrosstheAIlifecycle,”inProc.Des.
[152] C.Rudin,“Stopexplainingblackboxmachinelearningmodelsforhigh InteractiveSyst.Conf.,2021,pp.1591–1602.
stakesdecisionsanduseinterpretablemodelsinstead,”Nat.Mach.Intell., [179] F. Y. Kung, N. Kwok, and D. J. Brown, “Are attention check ques-
vol.1,pp.206–215,2019. tionsathreattoscalevalidity?,”Appl.Psychol.,vol.67,pp.264–283,
[153] R.Caruana,Y.Lou,J.Gehrke,P.Koch,M.Sturm,andN.Elhadad,“In- 2018.
telligiblemodelsforhealthcare:Predictingpneumoniariskandhospital [180] J.L.Fleiss,“Measuringnominalscaleagreementamongmanyraters,”
30-day readmission,” in Proc. 21th ACM SIGKDD Int. Conf. Knowl. Psychol.Bull.,vol.76,pp.378–382,1971.
Discov.DataMining,2015,pp.1721–1730. [181] I.Lage,D.Lifschitz,F.Doshi-Velez,andO.Amir,“Exploringcompu-
[154] C.Panigutti,A.Perotti,andD.Pedreschi,“DoctorXAI:Anontology- tationalusermodelsforagentpolicysummarization,”inIJCAI:Proc.
based approach to black-box sequential data classification explana- Conf.,2019,Art.no.1401.
tions,” in Proc. Conf. Fairness Accountability Transparency, 2020, [182] P.QianandV.Unhelkar,“Evaluatingtheroleofinteractivityonimprov-
pp.629–639. ingtransparencyinautonomousagents,”inProc.21stInt.Conf.Auton.
[155] A.Papenmeier,G.Englebienne,andC.Seifert,“Howmodelaccuracy AgentsMultiagentSyst.,2022,pp.1083–1091.
andexplanationfidelityinfluenceusertrust,”2019,arXiv:1907.12652. [183] A.Radfordetal.,“Languagemodelsareunsupervisedmultitasklearn-
[156] J.vanderWaa,E.Nieuwburg,A.Cremers,andM.Neerincx,“Evaluating ers,”OpenAIBlog,vol.1,no.8,2019,Art.no.9.
XAI: A comparison of rule-based and example-based explanations,” [184] ChatGPT,Introducing,“OpenAI,”2023.Accessed:Feb.17,2023.[On-
Artif.Intell.,vol.291,2021,Art.no.103404. line].Available:https://openai.com/blog/chatgpt
[157] B.J.Erickson,P.Korfiatis,Z.Akkus,andT.L.Kline,“Machinelearning [185] S.Bubecketal.,“Sparksofartificialgeneralintelligence:Earlyexperi-
formedicalimaging,”Radiographics,vol.37,no.2,pp.505–515,2017. mentswithGPT-4,”2023,arXiv:2303.12712.
[158] J.-Y. Jian, A. M. Bisantz, and C. G. Drury, “Foundations for an em- [186] W.Zhouetal.,“Towardsinterpretablenaturallanguageunderstanding
piricallydeterminedscaleoftrustinautomatedsystems,”Int.J.Cogn. with explanations as latent variables,” in Proc. Int. Conf. Neural Inf.
Ergonom.,vol.4,pp.53–71,2000. Process.Syst.,2020,pp.6803–6814.
[159] B.Kimetal.,“Interpretabilitybeyondfeatureattribution:Quantitative [187] S.Wiegreffe,J.Hessel,S.Swayamdipta,M.Riedl,andY.Choi,“Re-
testingwithconceptactivationvectors(TCAV),”inProc.Int.Conf.Mach. framingHuman-AIcollaborationforgeneratingfree-textexplanations,”
Learn.,2018,pp.2668–2677. inProc.Conf.NorthAmer.ChapterAssoc.Comput.Linguistics:Hum.
[160] B. P. Knijnenburg, M. C. Willemsen, Z. Gantner, H. Soncu, and C. Lang.Technol.,2022,pp.632–658.
Newell,“Explainingtheuserexperienceofrecommendersystems,”in [188] S.Wang,Z.Zhao,X.Ouyang,Q.Wang,andD.Shen,“Chatcad:Inter-
UserModelingUser-AdaptedInteraction.Berlin,Germany:Springer, activecomputer-aideddiagnosisonmedicalimageusinglargelanguage
2012. models,”2023,arXiv:2302.07257.
[161] B.Y.LimandA.K.Dey,“Assessingdemandforintelligibilityincontext- [189] N.F.Rajani,B.McCann,C.Xiong,andR.Socher,“Explainyourself!
awareapplications,”inProc.11thInt.Conf.UbiquitousComput.,2009, leveraginglanguagemodelsforcommonsensereasoning,”inProc.57th
pp.195–204. Annu.MeetingAssoc.Comput.Linguistics,2019,pp.4932–4942.
[162] S.G.HartandL.E.Staveland,“DevelopmentofNASA-TLX(taskload [190] J. Wei et al., “Chain-of-thought prompting elicits reasoning in large
index): Results of empirical and theoretical research,” Adv. Psychol., languagemodels,”inProc.Int.Conf.NeuralInf.Process.Syst.,2022,
vol.52,pp.139–183,1988. pp.24824–24837.

2122 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
[191] D.AlvarezMelisandT.Jaakkola,“Towardsrobustinterpretabilitywith PeizhuQianiscurrentlyworkingtowardthePhDde-
self-explainingneuralnetworks,”inProc.Int.Conf.NeuralInf.Process. greeincomputersciencewithRiceUniversity,USA
Syst.,2018,pp.7786–7795. working with Dr. Vaibhav Unhelkar on problems
[192] M.Yin,J.WortmanVaughan,andH.Wallach,“Understandingtheeffect inhuman-robotinteraction,robottransparency,and
ofaccuracyontrustinmachinelearningmodels,”inProc.SIGCHIConf. explainableAI.Herresearchinterestliesinbuilding
Hum.FactorsComput.Syst.,2019,pp.1–12. amutualunderstandingbetweenarobotanditshu-
[193] A.Bussone,S.Stumpf,andD.O’Sullivan,“Theroleofexplanationson mancollaborators.Herworkappliespsychologythe-
trustandrelianceinclinicaldecisionsupportsystems,”inProc.Int.Conf. oriestocomputationalframeworks,enablingrobots
HealthcareInform.,2015,pp.160–169. tocommunicatetheirobjectives.
[194] C.Baker,R.Saxe,andJ.Tenenbaum,“Bayesiantheoryofmind:Mod-
elingjointbelief-desireattribution,”inProc.Annu.MeetingCogn.Sci.
Soc.,vol.33,no.33,2011.
[195] S.H.Huang,D.Held,P.Abbeel,andA.D.Dragan,“Enablingrobots VaibhavUnhelkarreceivedtheMSdegreeinaero-
tocommunicatetheirobjectives,”Auton.Robots,vol.43,pp.309–326, nauticsandastronauticsandthePhDdegreeinau-
2019. tonomoussystems,in2015and2020,respectively.
[196] S.C.-H.Yang,N.E.T.Folke,andP.Shafto,“Apsychologicaltheoryof Heisanassistantprofessorofcomputersciencewith
explainability,”inProc.Int.Conf.Mach.Learn.,2022,pp.25007–25021. RiceUniversity,USAwhereheleadsaresearchgroup
[197] S. C.-H. Yang, W. K. Vong, R. B. Sojitra, T. Folke, and P. Shafto, in the emerging area of Human-Centered AI and
“Mitigating belief projection in explainable artificial intelligence via Robotics.Unhelkarearnedhisundergraduatedegree
Bayesianteaching,”Sci.Rep.,vol.11,2021,Art.no.9863. in aerospace engineering from the Indian Institute
[198] V. Chen, N. Johnson, N. Topin, G. Plumb, and A. Talwalkar, ofTechnologyinBombay,in2012.FromtheMas-
“Use-case-grounded simulations for explanation evaluation,” 2022, sachusettsInstituteofTechnology,whereheworked
arXiv:2206.02256. intheComputerScienceandArtificialIntelligence
[199] G.Aher,R.I.Arriaga,andA.T.Kalai,“Usinglargelanguagemodelsto Laboratory(CSAIL).
simulatemultiplehumans,”2022,arXiv:2208.10264.
Yao Rong received the MSc degree in electrical
TinaSeidelreceivedthediplomadegreeinpsychol-
andcomputerengineeringfromtheTechnicalUni-
ogyfromtheUniversityofRegensburg(Germany)
versity of Munich, Germany, in 2019. She is cur-
andVanderbiltUniversityNashville(USA),in1998,
rentlyworkingtowardthedoctoraldegreewiththe
andthePhDdegreewithexcellence,in2002fromthe
Human-CenteredTechnologiesforLearningGroup,
LeibnizInstituteforScienceandMathematicsEdu-
theTechnicalUniversityofMunich.From2022to
cationKiel(Germany).SheholdstheFriedlSchoeller
2023,sheservedasavisitingscholarwiththeDATA
ChairforEducationalPsychologywiththeSchoolof
Lab, Rice University. Her research interests lie in
SocialSciencesandTechnology,TechnicalUniver-
human-centeredAI,explainableAI,andhuman-AI
sity ofMunich, Germany. Her research focuses on
interactiontechnologies.
teachingandteachereducation.Shehasestablisheda
TeacherResearch&TrainingSimulationCenterthat
conductsseveralresearchprojectsfundedbytheGermanScienceFoundation
Tobias Leemann received the MSc degree from andtheGermanFederalMinistryofEducationandResearch.
theUniversityofErlangen-Nuremberg,Germany,in
2020.HeiscurrentlyworkingtowardthePhDdegree
withtheUniversityofTübingen,Germanywherehis
researchisfocusedontrustworthymachinelearning. GjergjiKasnecireceivedtheMScdegreeincom-
Specifically,hisresearchinterestsincludethequality puterscienceandmathematicsfromtheUniversity
assessmentofinterpretabilitytechniquesandthein- ofMarburg,in2005,andthePhDdegreefromthe
tersectionsofinterpretability,fairnessandprivacy. UniversityofSaarland-whilewiththeMaxPlanck
Institute-in2009.HethenworkedwithMicrosoft
ResearchCambridge,theHassoPlattnerInstitute,and
SCHUFAHoldingAG,whereheservedasCTOfrom
2017to2022.Between2018and2023,heledtheData
Thai-TrangNguyenisgraduatedwithaBScdegree
ScienceandAnalyticsGroupwiththeUniversityof
incomputersciencefromtheUniversityofTübingen,
TübingenasanHonoraryprofessor.In2023,Gjergji
Germany.SheiscurrentlyworkingtowardtheMSc
KasneciwasappointedprofessorofResponsibleData
degree with the same university. Furthermore, she
SciencewiththeTechnicalUniversityofMunich.
servedasaresearchassistant,theHuman-Computer
Interactiongroupfrom2019to2022.
Enkelejda Kasneci received the PhD degree in
computersciencefromtheUniversityofTübingen,
in 2013. She was postdoctoral researcher and a
Margarete-von-WrangellFellowwiththeUniversity
Lisa Fiedler is currently working toward the BSc of Tübingen. She is a distinguished professor for
degreeinmediainformaticsfromtheUniversityof Human-CenteredTechnologiesforLearningwiththe
Tübingen, Germany. Additionally, she works as a TechnicalUniversityofMunichandCoreMember
studentassistantfortheHuman-ComputerInteraction oftheMunichDataScienceInstitute.Herresearch
GroupattheUniversityofTübingen. evolves around Human-Centered Technologies and
AIsystemsthatsenseandinfertheuser’scognitive
state,theleveloftask-relatedexpertise,actions,and
intentionsbasedonmultimodaldataandprovideinformationformediaand
assistivetechnologiesinmanyactivitiesofeverydaylife,andespeciallyinthe
contextoflearning.