---
conversion_metadata:
  converted_at: "2026-07-21T09:11:14Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Verma et al.pdf"
  source_pdf_sha256: "1012502b37650af253c72e409c4bc4c1b9f9497e72f23a3a8096b026e1b4b956"
  page_count: 42
  markdown_char_count: 357749
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Counterfactual Explanations and Algorithmic Recourses for
Machine Learning: A Review

SAHIL VERMA, Computer Science and Engineering, University of Washington, Seattle, United States
VARICH BOONSANONG, Computer Science and Engineering, University of Washington, Seattle,
United States
MINH HOANG, Computer Science and Engineering, University of Washington, Seattle, United States
KEEGAN HINES, Arthur AI, Washington DC, United States
JOHN DICKERSON, Arthur AI, Washington DC, United States
CHIRAG SHAH, University of Washington, Seattle, United States

Machine learning plays a role in many deployed decision systems, often in ways that are difficult or impos-
sible to understand by human stakeholders. Explaining, in a human-understandable way, the relationship
between the input and output of machine learning models is essential to the development of trustworthy
machine learning based systems. A burgeoning body of research seeks to define the goals and methods of
explainability in machine learning. In this article, we seek to review and categorize research on counterfactual
explanations, a specific class of explanation that provides a link between what could have happened had input
to a model been changed in a particular way. Modern approaches to counterfactual explainability in machine
learning draw connections to the established legal doctrine in many countries, making them appealing to
fielded systems in high-impact areas such as finance and healthcare. Thus, we design a rubric with desirable
properties of counterfactual explanation algorithms and comprehensively evaluate all currently proposed al-
gorithms against that rubric. Our rubric provides easy comparison and comprehension of the advantages and
disadvantages of different approaches and serves as an introduction to major research themes in this field.
We also identify gaps and discuss promising research directions in the space of counterfactual explainability.
CCS Concepts: • General and reference → Surveys and overviews;

Additional Key Words and Phrases: Explainability in ML, counterfactual explanations, algorithmic recourse,
interpretability in ML

ACM Reference Format:
Sahil Verma, Varich Boonsanong, Minh Hoang, Keegan Hines, John Dickerson, and Chirag Shah. 2024. Coun-
terfactual Explanations and Algorithmic Recourses for Machine Learning: A Review. ACM Comput. Surv. 56,
12, Article 312 (October 2024), 42 pages. https://doi.org/10.1145/3677119

Authors’ Contact Information: Sahil Verma, Computer Science and Engineering, University of Washington, Seattle, Wash-
ington, United States; e-mail: vsahil@cs.washington.edu; Varich Boonsanong, Computer Science and Engineering, Univer-
sity of Washington, Seattle, Washington, United States; e-mail: varicb@cs.washington.edu; Minh Hoang, Computer Sci-
ence and Engineering, University of Washington, Seattle, Washington, United States; e-mail: minh257@cs.washington.edu;
Keegan Hines, Arthur AI, Washington DC, District of Columbia, United States; e-mail: keegan.hines@gmail.com; John
Dickerson, Arthur AI, Washington DC, District of Columbia, United States; e-mail: john@arthur.ai; Chirag Shah, Univer-
sity of Washington, Seattle, Washington, United States; e-mail: chirags@uw.edu.

This work is licensed under a Creative Commons Attribution International 4.0 License.

© 2024 Copyright held by the owner/author(s).
ACM 0360-0300/2024/10-ART312
https://doi.org/10.1145/3677119

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 2 -->

312:2

1 Introduction

S. Verma et al.

Machine learning is increasingly accepted as an effective tool to enable large-scale automation
in many domains. In lieu of hand-designed rules, algorithms are able to learn from data to dis-
cover patterns and support decisions. Those decisions can, and do, directly or indirectly impact
humans; high-profile cases include applications in credit lending [301], talent sourcing [295], pa-
role [315], and medical treatment [106]. The nascent Fairness, Accountability, Transparency, and
Ethics (FATE) in machine learning community has emerged as a multi-disciplinary group of re-
searchers and industry practitioners interested in developing techniques to detect bias in machine
learning models, develop algorithms to counteract that bias, generate human-comprehensible ex-
planations for the machine decisions, hold organizations responsible for unfair decisions, etc.

Human-understandable explanations for machine-produced decisions are advantageous in sev-
eral ways. For example, focusing on a use case of applicants applying for loans, the benefits would
include:

— An explanation can be beneficial to the applicant whose life is impacted by the decision. For
example, it helps an applicant understand which of their attributes were strong drivers in
determining a decision;

— Various forms of explanations can serve as a proxy for transparency in the system, which

could increase its trustworthiness;

— Further, it can help an applicant challenge a decision if they feel an unfair treatment has
been meted out, e.g., if one’s race was crucial in determining the outcome. This can also be
useful for organizations to check for bias in their algorithms;

— In some instances, an explanation provides the applicant with feedback that they can act

upon to receive the desired outcome at a future time;

— Explanations can help the machine learning model developers identify, detect, and fix bugs

and other performance issues;

— Explanations help adhere to laws surrounding machine-produced decisions, e.g., GDPR [68].

Explainability in machine learning is broadly about using inherently interpretable and trans-
parent models or generating post-hoc explanations for opaque models. Examples of the former
include linear/logistic regression, decision trees, rule sets, and the like. Examples of the latter in-
clude random forests, support vector machines (SVMs), and neural networks. Post-hoc explanation
approaches can either be model-specific or model-agnostic. Explanations by feature importance
and model simplification are two broad kinds of model-specific approaches. Model-agnostic ap-
proaches can be categorized into visual explanations, local explanations, feature importance, and
model simplification.

Feature importance finds the most influential features contributing to the model’s overall ac-
curacy or for a particular decision, e.g., SHAP [224] and QII [78]. Model simplification finds an
interpretable model that imitates the opaque model closely. Dependency plots are a popular kind
of visual explanation, e.g., Partial Dependence Plots [119], Accumulated Local Effects Plot [16],
and Individual Conditional Expectation [131]. They plot the change in the model’s prediction as
one or multiple features are changed. Local explanations differ from other methods because they
only explain a single prediction. Local explanations can be further categorized into approximation
and example-based approaches. Approximation approaches sample new datapoints in the vicinity
of the datapoint whose prediction from the model needs to be explained (hereafter called the ex-
plainee datapoint), and then fit a linear model (e.g., LIME [281]) or extracts a rule set from them (e.g.,
Anchors [282]). Example-based approaches seek to find datapoints in the vicinity of the explainee
datapoint. They either offer explanations in the form of datapoints that have the same prediction
as the explainee datapoint or the datapoints whose prediction differs from the explainee datapoint.

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 3 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:3

Fig. 1. Two possible paths for a datapoint (shown in blue), originally classified in the negative class, to cross
the decision boundary. The endpoints of both the paths (shown in red and green) are valid counterfactuals
for the original point. Note that the red path is the shortest, whereas the green path adheres closely to the
manifold of the training data, but is longer.

Note that the latter kind of datapoints are still close to the explainee datapoint and are termed as
“counterfactual explanations” (CFE).

Recall the use case of applicants applying for a loan. For an individual whose loan request has
been denied, counterfactual explanations provide them with actionable feedback that could help
them make changes to their features in order to transition to the desirable side of the decision
boundary, i.e., get the loan. This feedback is termed as an algorithmic recourse.

An Example. Suppose Alice walks into a bank and seeks a home mortgage loan. The decision is
made by a machine learning classifier that considers Alice’s feature vector of {Income, CreditScore,
Education, Age}. Unfortunately, Alice is denied the loan she seeks and is left wondering (1) why
the loan was denied? and (2) what can she do differently so that the loan will be approved in
the future? The former question might be answered with explanations like: “CreditScore was too
low”, and is similar to the majority of traditional explainability methods. The latter question forms
the basis of a counterfactual explanation: what small changes could be made to Alice’s feature
vector in order to end up on the other side of the classifier’s decision boundary? Let us suppose
the bank provides Alice with exactly this advice (through a CFE) of what she might change in
order to be approved next time. A possible counterfactual recommended by the system might
be to increase her Income by $10K or get a new master’s degree or a combination of both. The
answer to the former question does not tell Alice what action to take, while the CFE explicitly
helps her. Figure 1 illustrates how the datapoint representing an individual, which originally got
classified in the negative class, can take two paths to cross the decision boundary into the positive
class region.

Unlike several other explainability techniques, CFEs (or recourses) do not explicitly answer
“why” the model made a prediction; instead, they provide suggestions to achieve the desired
outcome. CFEs are also applicable to black-box models (when only the predict function of the
model is accessible), and therefore place no restrictions on model complexity and do not require
model disclosure. They also do not necessarily approximate the underlying model, producing

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 4 -->

312:4

S. Verma et al.

accurate feedback. Owing to their intuitive nature, CFEs are also amenable to legal frameworks
(see Appendix B).

In this work, we collect, review and categorize more than 350 recent papers that propose al-
gorithms to generate counterfactual explanations for machine learning models. Many of these
methods have focused on datasets that are either tabular or image-based. We describe our method-
ology for collecting papers for this survey in Section 2. We describe recent research themes in this
field and categorize the collected papers among a fixed set of desiderata for effective counterfactual
explanations (see Table 1).

The contributions of this article are:

(1) We examine a set of more than 350 recent papers on the same set of parameters to allow for
an easy comparison of the techniques these papers propose and the assumptions they work
under;

(2) The categorization of the papers achieved by this evaluation helps a researcher or a developer
choose the most appropriate algorithm given the set of assumptions they have and the speed
and quality of the generation they want to achieve.

(3) Comprehensive and lucid introduction for beginners in the area of counterfactual explana-

tions for machine learning.

2 Methodology
In this section, we describe our methodology for collecting and reviewing the papers used for
constructing the survey presented here.

2.1 How Did We Collect the Papers to Review?

We collected a set of more than 350 papers. This section provides the exact procedure used to arrive
at this set of papers. For the first version of this article, we had started from a seed set of papers
recommended by other people [229, 244, 270, 331, 346], followed by snowballing their references.
For this updated (second) version of the paper, we collected papers that cited the first paper that
proposed CFEs for ML, i.e., Wachter et al. [346] and the first version of this CFE survey paper [335].
For an even complete search, we searched for “counterfactual explanations”, “recourse”, and
“inverse classification” on two popular search engines for scholarly articles, Semantic Scholar and
Google scholar. We looked for papers published in the last five years on both search engines. This is
a reasonable time frame since the article that started the discussion of counterfactual explanations
in the context of machine learning (specifically for tabular data) was published in 2017 [346]. We
collected papers that were published before 31st May 2022. The papers we collected were published
at conferences like KDD, IJCAI, FAccT, AAAI, WWW, NeurIPS, WHI, or uploaded to Arxiv.

2.2 Scope of the Review
In this work, we focus on counterfactual explanations for classifiers and targeted towards tabu-
lar datasets. Even though the first paper we review was published online in 2017, and most other
papers we review cite it [346] as the seminal paper that started the discussion around counterfac-
tual explanations, we do not claim that this is an entirely new idea. Communities from data min-
ing [111, 231], causal inference [264], and even software engineering [61] have explored similar
ideas to identify the principal cause of a prediction, an effect, and a bug, respectively. Even before
the emergence of counterfactual explanations in applied fields, they have been the topic of discus-
sion in fields like social sciences [238], philosophy [194, 215, 286], and psychology [49, 50, 178]. In
this article, we restrict our discussion to recent articles that discuss counterfactual explanations
in machine learning, specifically classification settings. These articles have been inspired by the

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 5 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:5

emerging trend of FATE and the legal requirements pertaining to explainability in tasks automated
by machine learning algorithms.

3 Background
This section gives the background about the social implications of machine learning, explainability
research in machine learning, and some prior studies about counterfactual explanations.

3.1 Social Implications of Machine Learning
Establishing fairness and making an automated tool’s decision explainable are two broad ways
in which we can ensure equitable social implications of machine learning. Fairness research aims
at developing algorithms that can ensure that the decisions produced by the system are not bi-
ased against a particular demographic group of individuals, which are defined with respect to
sensitive or protected features, such as race, sex, and religion. Anti-discrimination laws make it
illegal to use sensitive features as the basis of any decision (see Appendix B). Biased decisions can
also attract widespread criticism and are therefore crucial to avoid [136, 195]. Fairness has been
captured in several notions based on a demographic grouping or individual capacity. Verma and
Rubin [338] have enumerated and intuitively explained many fairness definitions using a unifying
dataset. Dunkelau and Leuschel [101] provide an extensive overview of the major categorization
of research efforts in ensuring fair machine learning and enlists important works in all categories.
Explainable machine learning has also seen interest from other communities, specifically health-
care [321], having huge social implications. Several works have summarized and reviewed other
research in explainable machine learning [3, 56, 140].

3.2 Explainability in Machine Learning

This section gives some concrete examples that emphasize the importance of explainability and
give further details of the research in this area. In a real-world example, the US military trained
a classifier to distinguish enemy tanks from friendly tanks. Although the classifier performed
well on the training and test dataset, its performance was abysmal on the battlefield. Later, it was
found that the photos of friendly tanks were taken on sunny days, while for enemy tanks, photos
clicked only on overcast days were available [140]. The classifier found it much easier to use the
difference between the background as the distinguishing feature. In a similar case, a husky was
classified as a wolf because of the presence of snow in the background, which the classifier had
learned as a feature associated with wolves [281]. The use of an explainability technique helped
discover these issues.

The explainability problem can be divided into model explanation and outcome explanation

problems [140].

Model explanation searches for an interpretable and transparent global explanation of the orig-
inal model. Various articles have developed techniques to explain neural networks and tree en-
sembles using single decision tree [72, 92, 202] and rule sets [14, 85]. Some approaches are model-
agnostic, such as Golden Eye and PALM [152, 203, 381].

Outcome explanation needs to provide an explanation for a specific prediction from the model.
This explanation need not be a global explanation or explain the internal logic of the model. Model-
specific approaches for deep neural networks (CAM, Grad-CAM [294, 379]), and model agnostic
approaches (LIME, MES [281, 328]) have been proposed. These are either feature attribution or
model simplification methods. Example-based approaches are another kind of explainability tech-
nique used to explain a particular outcome [339, 346]. This work focuses on counterfactual ex-
planations (CFEs), which is an example-based approach.

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 6 -->

312:6

S. Verma et al.

By definition, CFEs are applicable to supervised machine learning setups where the desired
prediction has not been obtained for a datapoint. The majority of research in this area has applied
CFEs to classification settings, which consists of several labeled datapoints that are given as input
to the model, and the goal is to learn a function mapping from the input datapoints (with, say, m
features) to labels. In classification, the labels are discrete values. Xm is used to denote the input
space of the features, and Y is used to denote the output space of the labels. The learned function
is the mapping f : Xm → Y, which is used to predict labels for unseen datapoints in the future.

3.3 History of Counterfactual Explanations

Counterfactual explanations have a long history in other fields like philosophy, psychology, and
the social sciences. Philosophers like David Lewis published articles on the ideas of counterfactu-
als back in 1973 [215]. Woodward [362] said that a satisfactory explanation must follow patterns
of counterfactual dependence. Psychologists have demonstrated that counterfactuals elicit causal
reasoning in humans [49, 50, 178]. Philosophers have also validated the concept of causal thinking
due to counterfactuals [32, 362].

Studies have compared the likeability of CFEs with other explanation approaches. Binns et al.
[36] and Dodge et al. [90] performed user studies that showed that users prefer CFEs over case-
based reasoning [193], which is another example-based approach. The work by Fernández-Loría
et al. [111] provides three interesting examples where the feature importance explanation methods
fail to capture the underlying model, whereas CFEs do. Asher et al. [25] argue that the partiality
and locality of CFEs make them epistemically accessible and an adequate form of explanations.

4 Counterfactual Explanations
This section outlines the major aspects of counterfactual explanations.

4.1 Desiderata and Major Themes of Research
The previous example alludes to many desirable properties of an effective counterfactual explana-
tion. For Alice, the counterfactual should quantify a relatively small change, which will lead to the
desired alternative outcome. Alice might need to increase her income by $10K to get approved for
a loan, and even though an increase of $50K would do the job, it is most pragmatic for her if she can
make the smallest possible change. Additionally, Alice might care about a simpler explanation—it
is easier for her to focus on changing a few things (such as only Income) instead of trying to change
many features. Alice certainly also cares that the counterfactual she receives is giving her advice,
which is realistic and actionable. It would be of little use if the recommendation were to decrease
her age by 10 years.

These desiderata, among others, have set the stage for recent developments in the field of coun-
terfactual explainability. As we describe in this section, major themes of research have sought to
incorporate increasingly complex constraints on counterfactuals, all in the spirit of ensuring the
resulting explanation is truly actionable and helpful. Development in this field has focused on ad-
dressing these desiderata in a way that is generalizable across algorithms and is computationally
efficient.

(1) Validity. Wachter et al. [346] first proposed counterfactual explanations in 2017. They posed
CFE as an optimization problem. Equation (1) states the optimization objective, which is to
minimize the distance between the counterfactual (x (cid:3)) and the original datapoint (x) subject
to the constraint that the output of the classifier on the counterfactual is the desired label
(y (cid:3) ∈ Y). Converting the objective into a differentiable, unconstrained form yields two terms
(see Equation (2)). The first term encourages the output of the classifier on the counterfactual

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 7 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:7

to be close to the desired class, and the second term forces the counterfactual to be close to
the original datapoint. A metric d is used to measure the distance between two datapoints
x, x (cid:3) ∈ X, which can be the L1/L2 distance, or quadratic distance, or distance functions
which take as input the CDF of the features [331], or pairwise feature costs as perceived by
users [278]. Thus, this original definition already emphasized that an effective counterfactual
only proposes small changes in the features relative to the starting point.

arg min

arg min

x (cid:3) d(x, x
x (cid:3) max

λ

(cid:3)) subject to f (x
(cid:3)) − y

(cid:3)) = y
(cid:3)).
(cid:3))2 + d(x, x

λ(f (x

(cid:3)

(1)

(2)

A counterfactual that indeed is classified in the desired class is a valid counterfactual. As
illustrated in Figure 1, the points shown in red and green are valid counterfactuals, as they
are in the positive class region. The distance to the red counterfactual is smaller than the
distance to the green counterfactual.

(2) Actionability. An important consideration while making a recommendation is about which
features are mutable (e.g., income, age) and which are not (e.g., race, country of origin) [331].
A recommended counterfactual should never change the immutable features. In fact, if a
change to a legally sensitive feature produces a change in prediction, it shows inherent bias
in the model. Several articles have also mentioned that an applicant might have a preference
order amongst the mutable features (which can also be hidden.) The optimization problem
is modified to take this into account. We might call the set of actionable features A, and
update our loss function to be,

arg min
x (cid:3) ∈A

max
λ

λ(f (x

(cid:3)) − y

(cid:3))2 + d(x, x

(cid:3)).

(3)

(3) Sparsity. There can be a tradeoff between the number of features changed and the total
amount of change made to obtain the counterfactual. A counterfactual ideally should change
a smaller number of features in order to be the most effective. Thagard’s theory of explana-
tory coherence proposed that people prefer simpler and shorter explanations [319] and it
has also been tested in the context of explanations in ML [238, 247]. This makes sparsity an
important consideration. We update our loss function to include a penalty function that en-
courages sparsity in the difference between the modified and the original datapoint, д(x (cid:3)−x),
e.g., L0/L1 norm:

arg min
x (cid:3) ∈A

max
λ1, λ2

λ1(f (x

(cid:3)) − y

(cid:3))2 + λ2 ∗ д(x

(cid:3) − x) + d(x, x

(cid:3)).

(4)

(4) Data Manifold Closeness/Plausibility. Thagard’s theory of explanatory coherence states that
people would find it hard to trust an explanation if it is inconsistent with their prior beliefs
[319], for example if it resulted in a combination of features that were utterly unlike any
observations the occurs in the real world. In this sense, the counterfactual would be “unreal-
istic", not easy to realize, and anomalous to the real datapoints [44]. Therefore, a generated
counterfactual should be realistic in the sense that it is near the training data and adheres
to observed correlations among the features. Many articles have proposed various ways of
quantifying this. We might update our loss function to include a penalty for adhering to the
data manifold defined by the training set X, denoted by l(x (cid:3); X) :

arg min
x (cid:3) ∈A

max
λ1, λ2, λ3

λ1(f (x (cid:3)) − y (cid:3))2 + λ2 ∗ д(x (cid:3) − x) + λ3 ∗ l(x (cid:3); X) + d(x, x (cid:3)).

(5)

In Figure 1, the region between the dashed lines shows the data manifold. There are two
possible paths to cross the decision boundary for the blue datapoint. The shorter, red path
takes it to a counterfactual that is outside the data manifold, whereas a bit longer, the green

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 8 -->

312:8

S. Verma et al.

Education

Age

Salary

Fig. 2. Structural Causal Model (SCM) showing the influence of Education on other features like Age and
Salary.

path takes it to a counterfactual that follows the data manifold. Adding the data manifold
loss term encourages the algorithm to choose the green path over the red path, even if it is
slightly longer.

(5) Causality. Features in a dataset are rarely independent, therefore, changing one feature in
the real world affects other features. For example, getting a new educational degree neces-
sitates increasing the individual’s age by at least some amount and it would likely result in
an increase in one’s salary. These relations are usually represented using a structural causal
model (SCM) as shown in Figure 2. In order to be realistic and actionable, a counterfactual
should adhere to causal relations between features. Adhering to causal relation can be incor-
porated as a loss function or as a hard constraint [182, 337], depending on a method.
Generally, our loss function now accounts for (1) counterfactual validity; (2) sparsity in fea-
ture vector (and actionability of features); (3) similarity to the training data; and (4) causal
relations.

4.2 Relationship to Other Related Terms
Out of the papers collected, different terminology often captures the basic idea of counterfactual
explanations, although subtle differences exist between the terms. Several terms worth noting
include:

— Algorithmic Recourse: Ustun et al. [331] point out that counterfactuals do not take into ac-
count the actionability of the prescribed changes, which recourse does. Works taking a causal
view of the problem further fortify this claim [183, 184]. Recent papers in counterfactual
generation take actionability and feasibility of the prescribed changes, and therefore the
difference with recourse has blurred.

— Inverse Classification: Inverse classification aims to perturb an input in a meaningful way in
order to classify it into its desired class [4, 208]. Such an approach prescribes the actions to
be taken in order to get the desired classification. Therefore, inverse classification has the
same goals as CFEs.

— Contrastive Explanation: Contrastive explanations generate explanations of the form “an in-
put x is classified as y because features f1, f2, . . . , fk are present and fn, . . . , fr are absent”.
The features that are minimally sufficient for a classification are called pertinent positives,
and the features whose absence is necessary for the final classification are termed pertinent
negatives [87]. To generate both pertinent positives and pertinent negatives, one needs to
solve the optimization problem to find the minimum perturbations needed to maintain the
same class label or change it, respectively. Therefore, contrastive explanations (specifically
pertinent negatives) are related to CFEs.

— Adversarial Learning: Adversarial learning is closely related, but the terms are not inter-
changeable. Adversarial learning aims to generate the least amount of change in a given

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 9 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:9

input to classify it differently, often with the goal of far-exceeding the decision boundary and
resulting in a highly confident misclassification. While the optimization problem is similar to
the one posed in a counterfactual generation, the desiderata are different. For example, in ad-
versarial learning (often applied to images), the goal is an imperceptible change in the input
image. This is often at odds with the CFE’s goal of sparsity and parsimony (though single-
pixel attacks are an exception). Further, notions of data manifold and actionability/causality
are rarely considerations in adversarial learning. A few works point to the similarity and
synergy between the two domains: Pawelczyk et al. [259] explore the connection between
the optimization objectives and results of the adversarial and CFE generating techniques.
Freiesleben [118] states that the differences in the desired class label and distance from the
original datapoint distinguish CFEs from adversarial examples. Elliott et al. [104] propose
generating semantically meaningful adversarial perturbations to generate CFEs for images.
Browne and Swift [45] point out that the constraint of producing plausible datapoints dis-
tinguishes CFEs from adversarial examples.

5 Assessment of the Approaches on Counterfactual Properties

For easy comprehension and comparison, we identify several properties that are important for a
counterfactual generation algorithm. For all the collected papers which propose an algorithm to
generate counterfactual explanations, we assess the algorithm they propose against these proper-
ties. The results are presented in Table 1. Papers that do not propose new algorithms and discuss
related aspects of counterfactual explanations or modifications to previous methods are mentioned
in Section 6.3. The methodology we used to collect the papers is given in Section 2.

5.1 Properties of Counterfactual Algorithms
This section expounds on the key properties of a counterfactual explanation generation algorithm.
The properties form the columns of Table 1.

(1) Model Access. The counterfactual generation algorithms require different levels of access to
the underlying model for which they generate counterfactuals. We identify three distinct
access levels—access to complete model internals, access to gradients, and access to only
the prediction function (black-box). The access level required for the model depends on the
optimization tool used by a CFE generating approach.
Access to the complete model internals is required when the algorithm uses a solver-based
method like, mixed integer programming [179, 182, 183, 287, 331] or if they operate on de-
cision trees [52, 110, 222, 241, 323] which requires access to all internal nodes of the tree.
Gradient-based algorithms to solve the optimization objective are used by a majority of the
methods, usually by modifying the loss function proposed by Wachter et al. [346], but this
is restricted to differentiable models only.
Black-box approaches use gradient-free optimization algorithms such as Nelder-Mead [137],
growing spheres [210], FISTA [88, 332], ASP [35], or genetic algorithms [75, 208, 298] to
solve the optimization problem. Finally, some approaches do not cast the goal into an op-
timization problem and solve it using heuristics [139, 188, 274, 357]. Poyiadzi et al. [267]
propose FACE, which uses Dijkstra’s algorithm [89] to find the shortest path between exist-
ing training datapoints to find counterfactual for a given input. Hence, this method does not
generate new datapoints. Fraunhofer IOSB et al. [117] and Blanchart [39] divide the feature
space into ‘pure’ regions where all datapoints (by sampling) belong to one class and then
use graph traversing techniques to find the closest CFEs.
There are several approaches can incorporate the generation of CFEs within the classifier
itself. Guo et al. [143] propose CounterNet, a novel architecture that predicts the class and

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 10 -->

312:10

S. Verma et al.

Table 1. Assessment of the Collected Articles on the Key Properties, which are Important for Readily
Comparing and Comprehending the Differences and Limitations of Different Counterfactual Algorithms

Assumptions

Optimization amortization

CF attributes

Feature handling attributes

Year

Paper

2017

2018

2019

2020

(cid:2)

⎧⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪

⎩

⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪

⎩

⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪

⎩

[208]
[346]
[323]

[210]

[139]

[87]
[137]
[287]

[331]

[298]

[88]

[274]
[174]
[270]
[357,
358]

[244]

[267]

[332]

[229]

[182]

[263]
[188]

[183]

[184]
[212]
[75]

[179]

[110]

[221,
222]

Model
access
Black-box
Gradients
Complete

Model
domain

Agnostic
Differentiable
Tree ensemble

Amortized
Inference
No
No
No

Multiple
CFEs
No
No
No

Black-box

Agnostic

Black-box

Agnostic

Gradients
Black-box
Complete

Differentiable
Agnostic
Linear

Complete

Linear

Black-box
Black-box
or gradient
Black-box
Gradients
Gradients

Agnostic

Differentiable

Agnostic
Differentiable
Differentiable

Black-box

Agnostic

Gradients

Differentiable

Black-box
Black-box
or gradient
Gradients

Agnostic

Differentiable

Differentiable

Complete

Linear

Gradients
Black-box

Complete

Gradients
Gradients
Black-box

Complete

Complete

and

Differentiable
Agnostic
Linear
causal graph
Differentiable
Differentiable
Agnostic
Linear
and
tree ensemble
Random
Forest

Complete

Tree ensemble

No

No

No
No
No

No

No

No

No
No
No

No

No

No

No

Yes

No

No
No

No

No
No
No

No

No

No

No

Yes

No
No
Yes

No

Yes

No

No
No
No

No

Yes

No

No

Yes

Yes

No
No

No

No
No
Yes

No

Yes

No

Sparsity

Iteratively
L1
No
L0 and post-
hoc
Flips min.
split nodes
L1
No
L1
Hard
constraint
No

L1

No
No
No
Changes
one feature
L1 and post-
hoc
No

L1

No
Hard
constraint
No
Yes

L1

No
Iteratively
L0

No

L1

L1

Data
manifold
No
No
No

Causal
relation
No
No
No

Feature
actionability
Yes
No
No

No

No

Yes
No
No

No

No

Yes

No
Yes
No

No

No

Yes3

Yes

Yes

No

Yes
Yes

No

No
Yes
Yes

Yes

No

No

No

No

No
No
No

No

No

No

No
No
No

No

No

No

No

Yes

No

No
No

Yes

Yes
No
No

No

No

No

No

No

No
No1
No

Yes

Yes

No

No
No
No

No

No

No

No

Yes

Yes

Yes
No

Yes

Yes
No5
Yes

Yes

No

No

Categorical
dist. func
−
−
−

−

Indicator
−
−
N.A.2
−

Indicator
−

−
−
−

−

Indicator
−

Embedding
−

Indicator

N.A.4
−

−

−
−
Indicator
−

−

−

Papers are sorted chronologically. Details about the full table is given in Appendix A.

generates the CFE of a datapoint when trained from scratch. Shao and Kersting [297] train
a sum-product network that acts as both a classifier and density estimator and uses that to
generate CFEs. Ross et al. [285] propose adding an adversarial loss during training of the ML
model to have a higher probability of having a recourse for the training datapoints. (After
training, any CFE generating method can be used.)

(2) Model Agnostic. This column describes the domain of models a given algorithm can operate
on. For example, gradient-based algorithms can only handle differentiable models, and the al-
gorithms based on solvers require linear or piece-wise linear models [179, 182, 183, 287, 331],
some algorithms are model-specific and only work for those models like tree ensem-
bles [110, 179, 222, 323]. Black-box methods have no restriction on the underlying model
and are, therefore, model-agnostic.

1It considers global and local feature importance, not preference.
2All features are converted to polytope type.
3Does not generate new datapoints.
4The distance is calculated in latent space.
5It considers feature importance not user preference.

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 11 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:11

(3) Optimization Amortization. Among the collected papers, the proposed algorithm mostly
returned a single counterfactual for a given input datapoint. Therefore, these algorithms
require solving an optimization problem to generate each counterfactual for every input
datapoint. A smaller number of the methods are able to generate multiple counterfactuals
(generally diverse by some metric of diversity) for a single input datapoint; therefore, they
require to be run once per input to get several counterfactuals [52, 75, 110, 139, 182, 229,
244, 287, 298]. Dandl et al. [75] propose a genetic algorithm to generate multiple CFEs of
a datapoint at once. Mahajan et al. [229]’s approach learns the mapping of datapoints to
counterfactuals using a variational auto-encoder (VAE) [91]. Therefore, once the VAE is
trained, it can generate multiple counterfactuals for all input datapoints, without solving
the optimization problem separately and is thus very fast. Verma et al. [337] and Samoilescu
et al. [290] train a reinforcement learning model to learn the actions that need to be taken to
generate CFEs for a data distribution. Hence, these approaches are also amortized. Yang et al.
[367] train a CGAN to synthesize CFEs with umbrella sampling; hence, their approach is also
amortized. Van Looveren et al. [333] also train a GAN-based model that is amortized. Schleich
et al. [292] partially evaluate (amortize) the classifier for the static features, hence speeding
up the CFE generation. We report two aspects of optimization amortization in the table:
• Amortized Inference: This column is marked Yes if the algorithm can generate counterfac-
tuals for multiple input datapoints without optimizing separately for them; otherwise, it
is marked No.

• Multiple Counterfactuals (CF): This column is marked Yes if the algorithm can generate

multiple counterfactuals for a single input datapoint; otherwise, it is marked No.

(4) Counterfactual (CF) Attributes. These columns evaluate algorithms on sparsity, data

manifold adherence, and causality.

(a) Sparsity: Among the collected articles, methods using solvers explicitly constrain spar-
sity [182, 331], black-box methods constrain L0 norm of counterfactual and the input dat-
apoint [75, 210]. Gradient-based methods typically use the L1 norm of counterfactual and
the input datapoint. Some of the methods change only a fixed number of features [188, 357],
change features iteratively [175, 212, 293, 337], or flip the minimum possible split nodes in
the decision tree [139] to induce sparsity. Some methods also induce sparsity post-hoc [210,
244]. This is done by sorting the features in ascending order of relative change and greed-
ily restoring their values to match the values in the input datapoint until the prediction for
the CFE is still different from the input datapoint. Sparsity column in the table is marked
No if the algorithm does not consider sparsity, else it specifies the sparsity constraint.
(b) Data Manifold Adherence: Adherence to the data manifold has been addressed using
several different approaches, like training VAEs on the data distribution [87, 174, 229, 332],
constraining the distance of a counterfactual from the k nearest training datapoints [75,
102, 179], directly sampling points from the latent space of a VAE trained on the data, and
then passing the points through the decoder [263], using an ensemble of models to capture
the predictive entropy [293], using a kernel density estimator (KDE) to estimate the
PDF of the underlying data manifold [122], using the cycle consistency loss in GAN [333],
mapping back to the data domain [212], using a combination of existing datapoints [188],
using Gaussian mixture models to approximate the probability of in-distributionness [19],
or by using feature correlations [20], or by simply not generating any new datapoint [267].
Data manifold column in the table is marked Yes if the algorithm forces the generated
CFEs to be close to the data manifold by some mechanism; otherwise, it is marked No.
(c) Causality: The relation between different features is represented by a directed graph
between them, which is termed as a causal graph [264]. Out of the papers that have

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 12 -->

312:12

S. Verma et al.

addressed this concern, most require access to the complete causal graph [183, 184]
(which is rarely available in the real world), while Duong et al. [102], Mahajan et al.
[229], Verma et al. [337], and Yang et al. [367] can work with partial causal graphs. Causal
relation column in the table is marked Yes if the algorithm considers the causal relations
between features when generating CFEs; otherwise, it is marked No.

(5) Feature Handling Attributes. Out of the articles that consider feature actionability, most
classify the features into immutable and mutable types. Karimi et al. [183] and Lash et al.
[208] categorize the features into immutable, mutable, and actionable types. Actionable
features are a subset of mutable features. They point out that certain features are mutable
but not directly actionable by the individual, e.g., CreditScore cannot be directly changed; it
changes as an effect of changes in other features like income and credit amount. Mahajan
et al. [229] uses an oracle to learn the user preferences for changing features (among
mutable features) and can also learn hidden preferences.
Most tabular datasets have both continuous and categorical features. Performing arithmetic
over continuous features is natural, but handling categorical variables in gradient-based
algorithms can be complicated. Some algorithms cannot handle categorical variables and
filter them out [210, 222]. Wachter et al. [346] proposed clamping all categorical features to
each of their values, thus spawning many processes (one for each value of each categorical
feature), leading to scalability issues. Some approaches convert categorical features to
one-hot encoding and then treat them as numerical features. In this case, maintaining
one-hotness can be challenging. Some use a different distance function for categorical
features, which is generally an indicator function (1 if a different value, else 0). [122] use
Markov chain transitions to encode categorical distances. Yang et al. [367] use Gaussian
mixture models to normalize the continuous features and Gumbel-Softmax to relax categor-
ical features into continuous ones. Genetic algorithms, evolutionary algorithms, and SMT
solvers can naturally handle categorical features. We report these properties in the table.
• Feature Actionability: This column is marked Yes if the algorithm considers feature

actionability, otherwise marked No.

• Categorical Distance Function: This column is marked—if the algorithm does not use a
separate distance function for categorical variables, else it specifies the distance function.

6 Evaluation of Counterfactual Generation Algorithms
This section lists the common datasets used to evaluate counterfactual generation algorithms and
the metrics on which they are typically evaluated and compared.

6.1 Commonly Used Datasets for Evaluation
The datasets used in the evaluation in the articles we review can be categorized into tabular and
image datasets. Not all methods support image datasets. Some of the articles also used synthetic
datasets for evaluating their algorithms, but we skip those in this review since they were generated
for a specific article and also might not be available. Common datasets in the literature include:

— Tabular: Adult income [33], German credit [154], Student Performance [71], Breast cancer
[97], Default of credit [372], Shopping [99], Iris [98], Wine [100], Spambase [157], Covertype
[38], ICU [96], LendingClub [314], Give Me Some Credit [177], COMPAS [170], LSAT [40],
Pima diabetes [303], HELOC/FICO [113], Fannie Mae [227], Portuguese Bank [243], San-
giovese [228], Bail dataset [173], Simple-BN [229], AllState [165], WiDS Datathon [164],
Home Credit Default Risk [138], German Housing [115], HospitalTriage [156], MIMIC-
IV [172], Freddie Mac [225], UK unsecured personal loans [47], insurance dataset [197],
BPIC2017 [160].

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 13 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:13

Table 2. Continued from Table 1

Assumptions

Optimization amortization

CF attributes

Feature handling attributes

Year

Paper

Model
access
Gradient

Model
domain
Differentiable

Amortized
Inference
Yes

Multiple
CFEs
No

[333]
[52,
147]
[181]
[293]
[247]
[46]
[102]

[248]

[20]

[292]

[250]

[39]
[290]
[337]
[258]

[241]

[117]
[367]
[175]

[122]

⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪

⎩

⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪

⎩

2021

2022

Complete

Decision Tree

Complete
Gradients
Black-box
Black-box
Black-box

Complete

Complete
Black-box
or
complete
Black-box
or gradient
Complete
Black-box
Black-box
Complete

Linear
Differentiable
Agnostic
Agnostic
Agnostic

Linear

Linear

Agnostic
black-box

if

if

Agnostic
black-box
Tree ensemble
Agnostic
Agnostic
Tree ensemble

Complete

Linear

Black-box
Black-box
Gradient

Agnostic
Agnostic
Differentiable

Black-box

Agnostic

No

No
No
No
No
No

No

No

No

Yes

Yes
Yes
Yes
No

No

Yes
Yes
No

No

[279]

Black-box

Agnostic

Partially

[143]

[363]
[366]
[278]

[297]

Training
from
scratch
Gradient
Black-box
Black-box
Training
from
scratch

Differentiable

Differentiable
Agnostic
Agnostic

Differentiable

Yes

No
No
Yes

No

Sparsity

L1

L1

Iteratively
Iteratively
Gower
Yes
No
Hard
constraint
No

L0/L1

L1

Yes
L0/L1
Iteratively
L0/L1
Hard
constraint
No
No
No

L1

Hard con-
straint

No

No
Yes
Yes

No

Data
manifold
No6

Causal
relation
No

Feature
actionability
No

Categorical
dist. func
−

No

No
Yes
No
Yes
No

Yes

Yes

No

Yes

No
Yes
Yes
Yes

No

No
Yes
No

Yes

No

No

Yes
No
No

Yes

No

Yes
No
Yes
No
Yes

No

No

Yes

No

No
No
Yes
No

No

No
Yes
No

No

No

No

Yes
No
No

No

Yes

No
Yes
Yes
No
No

Yes

No

Yes

Yes

Yes
Yes
Yes
Yes

Yes

No
No
No

No

Yes

No

No
Yes
Yes

Yes

−

−
−
Gower
Indicator
Latent space
−

−

Indicator

−

−
Indicator
−
Gower

Indicator
−
Not sure
−
Markov
Chains

Gower

−

−
−
Indicator

−

Yes

Yes
No
Yes
No
No

Yes

No

Yes

No

No
Yes
Yes
No

Yes

Yes
Yes
No

No

Yes

No

No
Might
Might

No

— Image: MNIST [213], EMNIST [66], CelebA [219], CheXpert [167], ImageNet [86], ISIC Skin

Lesion [65], ADNI [245], ChestX-ray8 [348].

6.2 Metrics for Evaluation of Counterfactual Generation Algorithms
Counterfactuals are considered as actionable feedback to individuals who have received undesir-
able outcomes from automated decision-makers, and therefore an ideal evaluation would consist
of a user-study. However, user studies are expensive and therefore the literature proposes to use
proxy metrics to evaluate the ease of acting on a recommended counterfactual:

(1) Validity: Validity measures the ratio of the counterfactuals that actually have the desired
class label to the total number of counterfactuals generated. Higher validity is preferable.
Most papers report it.

(2) Proximity: Proximity measures the distance of a counterfactual from the input datapoint. For
counterfactuals to be easy to act upon, they should be close to the input datapoint. Distance
metrics like the L1 norm, L2 norm, and Mahalanobis distance are common. To handle the vari-
ability of range among different features, some articles standardize them in pre-processing
or divide L1 norm by median absolute deviation of respective features [244, 287, 346], or di-
vide L1 norm by the range of the respective features [75, 182, 183]. Proximity for categorical

6Maybe partially as it uses cycle consistency loss.

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 14 -->

312:14

S. Verma et al.

features is treated as binary (one or zero depending of whether the value changed or not).
Some articles term proximity as the average distance of the generated counterfactuals from
the input. Lower values of average distance are preferable.

(3) Number of Features Changed: Shorter explanations are more comprehensible to humans
[238], therefore, counterfactuals ideally should prescribe a change in a small number of fea-
tures. Although a consensus on a hard cap on the number of modified features has not been
reached, Keane and Smyth [188] cap a sparse counterfactual to at most two feature changes.
(4) Counterfactual generation time: Intuitively, this measures the time required to generate
counterfactuals. This metric can be averaged over the generation of a counterfactual for a
batch of input datapoints or for the generation of multiple counterfactuals for a single input
datapoint.

(5) Diversity: Some algorithms support the generation of multiple counterfactuals for a single
input datapoint. The purpose of providing multiple counterfactuals is to increase the ease
for applicants to reach at least one counterfactual state. Therefore, the recommended coun-
terfactuals should be diverse, allowing applicants to choose the easiest one. If an algorithm
is strongly enforcing sparsity, there could be many different sparse subsets of the features
that could be changed. Therefore, having a diverse set of counterfactuals is useful. Diversity
is encouraged by maximizing the distance between the multiple counterfactuals by adding
it as a term in the optimization objective [75, 244] or as a hard constraint [182, 241, 331],
or by minimizing the mutual information between all pairs of modified features [212].
Mothilal et al. [244] reported diversity as the feature-wise distance between each pair of
counterfactuals. A higher value of diversity is preferable.

(6) Closeness to the Training Data/Plausibility: Recent articles have considered the action-
ability and realisticness of the modified features by grounding them in the training data
distribution. This has been captured by measuring the average distance to the k-nearest
datapoints [75], or measuring the local outlier factor [179], or measuring the reconstruction
error from a VAE trained on the training data [229, 332], or measuring the PDF of such
datapoints using KDE [122], or measuring the maximum mean discrepancy (MMD)
between the original and counterfactual points [333]. A lower value of the distance and
reconstruction error is preferable.

(7) Causal Constraint Satisfaction (Feasibility): This metric captures how realistic the modifi-
cations in the counterfactual are by measuring if they satisfy the causal relation between
features. Mahajan et al. [229] evaluated their algorithm on this metric.

Other Metrics. Here we describe the less commonly used metrics:
(1) IM1 and IM2: Van Looveren and Klaise [332] proposed two interpretability metrics specifi-
cally for algorithms that use auto-encoders. Let the counterfactual class be t, and the original
class be o. AEt is the auto-encoder trained on training instances of class t, and AEo is the
auto-encoder trained on training instances of class o. Let AE be the auto-encoder trained on
the full training dataset (all classes):

I M1 =

(cid:6)xcf − AEt (xcf )(cid:6)2
2
+ ϵ

(cid:6)xcf − AEo(xcf )(cid:6)2
2

I M2 =

(cid:6)AEt (xcf ) − AE(xcf )(cid:6)2
(cid:7)
2
(cid:7)

(cid:7)
(cid:7)xcf

+ ϵ

(6)

(7)

1
A lower value of IM1 implies that the counterfactual (xcf ) can be better reconstructed by
the auto-encoder trained on the counterfactual class (AEt ) compared to the auto-encoder

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 15 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:15

trained on the original class (AEo), thus implying that the counterfactual is closer to the data
manifold of the counterfactual class. A lower value of IM2 implies that the reconstruction
from the auto-encoder trained on the counterfactual class and the auto-encoder trained on
all classes is similar. Therefore, a lower value of IM1 and IM2 means a more interpretable
counterfactual, where interpretability refers to a plausible datapoint which is supposedly
more interpretable.

(2) Label Variation Score and Oracle Score: Hvilshøj et al. [162] point out that the previous met-
rics are unable to detect out-of-distribution CFEs (especially for high-dimensional datasets)
and propose two new metrics. Label Variation Score applies when each datapoint has multi-
ple labels, and the intuition is that CFE for a particular label should not affect the predictions
for other labels (unless they are highly correlated). This assumes the case of multi label clas-
sification, where a datapoint with original prediction A is being counterfactually predicted
as B. LVS states that the prediction probabilities for classes apart from A and B should not
change

(cid:8)

LV S =

ddiv [pl (x), pl (CF E(x))],

l ∈L

(8)

where L is the total number of labels for a datapoint and pl is the predicted probability for
the specific label l, and ddiv measures the divergence between the predicted probability of
label l for the original datapoint x and its CFE.
Oracle Score is similar to validity, however, with an additional classifier trained on the same
dataset as the original classifier. The intuition is that if a CFE is more like an adversarial
example for a classifier, the CFE would not be classified in the desired class by the other
classifier, and hence we use the prediction from the additional classifier as the ground truth
validity.

Note that several of the evaluation metrics might be at odds with each other, for example, achiev-
ing high diversity might come at cost of being close to the training data, or achieving high validity
might come at cost of low proximity.

Some of the reviewed papers did not evaluate their algorithm on any of the above metrics. They

only showed a couple of example inputs and respective CFEs (see Appendix A).

6.3 Other Works
This section enlists works that talk about the desirable properties of counterfactuals or point to
their issues. We also talk about works that propose minor modifications to previous similar ap-
proaches.

Works Exploring Desirable CFE Properties. Sokol and Flach [306] list several desirable properties
of counterfactuals inspired from Miller [238] and state how the method of flipping logical condi-
tions in a decision tree satisfies most of them. Laugel et al. [209] enlist proximity, connectedness,
and stability as three desirable properties of a CFE and propose the metrics to measure them.

Works Pointing to Issues with CFEs. Laugel et al. [211] say that if the explanation is not based
on training data, but the artifacts of non-robustness of the classifier, it is unjustified. They define
justified explanations to be connected to training data by a continuous set of datapoints, termed
E-chainability. Barocas et al. [30] state five reasons that have led to the success of counterfactual
explanations and also point out the overlooked assumptions. They mention the unavoidable con-
flicts which arise due to the need for privacy invasion in order to generate helpful explanations.
Mehedi Hasan and Talbert [236] state that generating multiple CFEs for a user might overwhelm
them in which case they might choose a suboptimal recourse. They propose a game-theoretic

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 16 -->

312:16

S. Verma et al.

framework to overcome this problem. Kasirzadeh and Smart [186] provide philosophical insight
into the implicit assumptions and choices made when generating CFEs.

Causal CFEs. Downs et al. [95] propose using conditional subspace VAEs (CSVAE), a vari-
ant of VAEs, to generate CFEs that obey correlations between features, causal relations between
features, and personal preferences. This method builds a probabilistic data model of the training
data using a CSVAE and uses it to generate CFEs. However, these CFEs are not with respect to a
specific ML model. Crupi et al. [73] propose a technique that can be used with any counterfactual
generation approach to generate causality abiding CFEs. von Kügelgen et al. [343] extend Karimi
et al. [184]’s work to the setting where unobserved confounders may be present in the causal
setting. de Lara et al. [79] show that optimal transport-based methods are an approximation of
Pearl’s CFEs and hence can be used to generate causal CFEs. Beckers [34] delves further into the
integration of causality, actual causation, and CFEs.

CFE for Specific Models. Albini et al. [11] propose a CFE generation approach targeted for
Bayesian network classifiers. Artelt and Hammer [18, 19] enlists the counterfactual optimization
problem formulation for several model-specific cases, like generalized linear model, gaussian naive
Bayes, and mention the general algorithm to solve them. Koopman and Renooij [198] propose a
BFS-based technique for generating CFEs for Bayesian networks.

Works Considering Multi-Agent Scenarios of CFEs. Tsirtsis and Gomez-Rodriguez [327] cast the
counterfactual generation problem as a Stackelberg game between the decision maker and the
person receiving the prediction. Given a ground set of CFEs, the proposed algorithm returns the
top-k CFEs, which maximizes the utility of both the involved parties. Bordt et al. [41] point out
that the interests of the provider and receiver of model explanations might be in conflict, and the
ambiguous post-hoc explanations might be unsuitable for achieving the purpose of transparency
as desired in GDPR. This also relates to fairwashing (see research challenge RC9).

Global CFEs. Rawal and Lakkaraju [278] propose AReS to generate rule lists that act as global
CFEs. Ley et al. [216] and Kanamori et al. [180] propose computationally more efficient implemen-
tation of Rawal and Lakkaraju [278]’s work. Carrizosa et al. [53] propose a mixed integer quadratic
model to generate CFEs for a group of datapoints. Warren et al. [354] and Carrizosa et al. [55] also
propose algorithms to generate group CFEs. Koo et al. [197] propose generating CFEs for a set of
datapoints using Lagrangian and subgradient methods. Pedapati et al. [265] propose a technique
to train a globally interpretable model (for a black-box model) such that this model is consistent
with the pertinent positives and pertinent negatives [87] of the training datapoints used to train
the original model.

Works Proposing Modifications to Previous Approaches. Chen et al. [63] and De Toni et al. [80]
use RL to generate CFE as was also proposed by Verma et al. [337]. Rasouli and Chieh Yu [272]
propose a genetic algorithm to generate CFEs as was also proposed by Dandl et al. [75]. Hashemi
and Fathi [150] propose to use genetic algorithm for CFE generation similar to Dandl et al. [75]’s
work. Monteiro and Reynoso-Meza [242] propose extending Dandl et al. [75]’s approach using
U-NSGA-III evolutionary algorithm. Barr et al. [31] extend Mahajan et al. [229]’s work by interpo-
lating between the input and CFE datapoint to generate CFEs closer to the input datapoint. Sajja
et al. [289] propose using a semi-supervised autoencoder instead of the traditional unsupervised
autoencoder to generate CFEs close to the training data manifold. Huang et al. [160] propose LORE-
LEY that extends LORE [139] to generate CFEs for multi-class classification problems and account
for flow constraints. Wijekoon et al. [360] use feature importances provided by LIME to assist the
case-based reasoning approach to generate CFEs. Delaney et al. [83] propose using trust scores

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 17 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:17

to measure the out-of-distributionness of the CFEs. Guidotti and Ruggieri [141] propose using an
ensemble of base CFE explainers to generate diverse CFEs.

Benchmark and Dataset Curation. Mazzine and Martens [233] quantitatively compare 10 CFE
generating approaches using 22 datasets and 9 metrics. Pawelczyk et al. [260] and Artelt [17] have
developed extensible toolboxes where several CFE approaches can be plugged in and compared
on specific datasets.

Semi-Factuals. Semi-factuals are recently proposed kind of explanations where the goal is to not
change the model prediction (unlike CFEs), but to improve the current outcome by changing the
input. For example, if Alice’s loan request is approved but her rate of interest is high, how can
Alice change her features such as to get a lower rate of interest. Several works have proposed
novel algorithms to generate semi-factual explanations [21, 24, 189, 190].

Various Uncategorized Works. State [308] talks about generating CFEs with real-world con-
straints on features and adaptability with updating ML models using constraint logic program-
ming. Tahoun and Kassis [311] propose to disentangle actions from feature modifications to ad-
dress the lack of intervention data and appropriate action costs. The users should already describe
the actions they are willing to take, and a model should just choose the minimum cost action
that generates the CFE. Lucic et al. [220] propose a CFE approach to provide a lower and upper
bound for the feature values that get a low prediction error from the ML model for a datapoint
that originally had a high prediction error. Korikov and Beck [199] and Korikov et al. [200] show
how CFEs can be generated by using the generalization of inverse combinatorial optimization and
solve it under two objectives. Pawelczyk et al. [261] provide a general upper bound on the cost
of counterfactual explanations under the phenomenon of predictive multiplicity, wherein more
than one trained model have the same test accuracy and there is no clear winner among them.
Fdez-Sánchez et al. [108] propose a hierarchical decompositions-based method to obtain CFEs for
multi-class classification problems. Bertossi [35] and Medeiros Raimundo et al. [234] propose brute
force approaches to generate CFEs.

7 Counterfactual Explanations for Other Data Modalities
Since we restrict this survey to the papers that generate CFEs for tabular data, in this section we
point the readers to the papers that propose algorithms targeted towards other data modalities:

(1) Image Data: [1, 8, 9, 12, 13, 29, 77, 104, 109, 114, 128, 135, 142, 146, 151, 161, 163, 168, 169, 191,
192, 207, 217, 218, 237, 255, 256, 266, 284, 291, 304, 320, 333, 334, 340, 347, 359, 368, 370, 377].

(2) Text Data: [42, 60, 175, 226, 271, 275, 283, 322, 368–370].
(3) Speech Data: [375].
(4) Time-Series Data: [26, 82, 159, 185, 310, 326, 333, 351, 352].
(5) Graph Data for Graph Neural Networks: [2, 27, 28, 105, 223, 252, 355]. A survey for CFE on

graph neural networks: [268].

(6) Agent Action (e.g., reinforcement learning or planning): [43, 257, 309].
(7) Recommender Systems: [81, 129, 130, 176, 296, 313, 324, 364, 378, 380].
(8) Functional Data: [54, 201] and Behavioral Data: [271].

8 Other Applications of Counterfactual Explanations
Here we refer the readers to other applications where counterfactual explanations are being used
apart from explaining ML models:

(1) Anomaly and Data-Drift Detection: Hinder and Hammer [153] propose to use CFEs to explain
data drift. Sulem et al. [310] propose to use CFEs to explain anomalies in time-series datasets.

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 18 -->

312:18

S. Verma et al.

Ravi et al. [276] wrote a survey on the explainability techniques for convolutional auto-
encoders for anomaly detection of images. Haldar et al. [148] propose to use CFEs to explain
anomaly detection when using autoencoders. Antoran et al. [15] use CFEs to find changes
in a datapoint that would help a classifier have a higher confidence in its prediction.

(2) Training Dataset Debugging: Yousefzadeh and O’Leary [373] propose to use CFEs to debug
ML models by diagnosing the behavior and using synthetic data to alter the decision bound-
aries. Qi and Chelmis [269] propose to use CFEs to debug potentially mislabeled datasets.
Gan et al. [124] propose to use CFEs to detect bugs in financial models. Han and Ghosh [149]
propose finding a minimal subset of training datapoints that are responsible for a particular
prediction and hence can be used to debug training datasets.

(3) Data Augmentation: Yuan et al. [374] propose to use CFEs to augment training data that is
used to predict market volatility based on earning calls. Temraz and Keane [316] propose
using CFEs to augment training data to tackle the class imbalance problem. Mehedi Hasan
and Talbert [235] and Rasouli and Yu [273] propose using CFEs for data augmentation of
tabular datasets for increased robustness. Temraz et al. [317] propose using CFEs to generate
data points that can be used to train ML models that predict crop growth (afflicted by climate
change).

(4) Drug Designing: Nguyen et al. [251] use CFEs to find changes in a drug and protein molecule

that will increase their affinity for each other. They use multi-agent RL to this end.

(5) ML Model Bias Detection: Myers et al. [246] build a visualization tool based on computing
CFEs to expose biases in ML models. Fawkes et al. [107] point out to the challenges with
using CFEs for fairness. Other works also use CFEs to measure and mitigate model biases
[205, 331].

(6) Various Applications: Mazzine et al. [232] propose to use CFEs in employment services to
help job seekers get personalized advice for increasing their propensity for getting recom-
mended for a job and to help the ML developers to detect potential bias and other issues in
their ML model. Sadler et al. [288] propose to use CFEs for community detection in social
networks. Fujiwara et al. [121] propose to use CFEs to understand interactive dimensionality
reduction. Tsiakmaki and Ragos [325] propose to use CFEs for providing actionable sugges-
tions to improve student performance in a university course. Cong et al. [69] propose a CFE
approach to explain why a test set fails the Kolmogorov-Smirnov test. Marchezini et al. [230]
propose to use CFE for altering both observational and latent variables to reason about men-
tal health. Yao et al. [371] propose to use counterfactuals for evaluating the explanations for
recommender systems. Gupta et al. [144] use CFEs to propose changes to constraint satis-
faction problems that have no solutions. Teofili et al. [318] propose using CFEs to explain
entity resolution models. Artelt et al. [22] use CFEs to explain the differences between the
learning of a pair of models. Frohberg and Binder [120] propose CRASS, a dataset to test
counterfactual reasoning of LLMs.

There has been one case of real-world deployment of CFEs in a hiring platform, Hired. Ne-
mirovsky et al. [249] use a GAN-based approach [250] to generate counterfactuals in order to get
candidates approved by the Hired Marketplace ML model. Their approach satisfies several of the
desiderata we discussed in Section 4.1, for example:

(1) they consider feature actionability and only change the mutable features like expected salary,

years of experience, and skills;

(2) their loss function encourages proximity and they use L1 distance between the generated

counterfactual and the input datapoint to measure it;

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 19 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:19

(3) they use a GAN-based approach to generate counterfactuals that are close to the data mani-

fold and use an auto-encoder reconstruction error to measure it;

(4) their approach was designed to amortize the optimization process and they measure the

counterfactual generation time to measure latency.

9 Open Questions and Research Progress

In the first version of this survey paper, we delineated the open questions and challenges yet to
be tackled by the existing works pertaining to CFEs [336]. A lot of progress has been made by the
research community and several of the open challenges have been solved (mentioned in the later
section). In this version of the paper, we highlight a set of main research problems that are yet to
be addressed and invite researchers to tackle them.

9.1 Current Open Questions

Research Challenge 1. Counterfactual explanations should capture the applicant’s preferences.

Along with the distinction between mutable and immutable features (finely classified into ac-
tionable, mutable, and immutable), counterfactual explanations should also capture preferences
specific to an applicant. This is important because the ease of changing different features can dif-
fer across applicants.

Progress: Mahajan et al. [229] captures the applicant’s preferences using an oracle, but that
is expensive and is still a challenge. Rawal and Lakkaraju [278] use the Bradley-Terry model to
learn the pairwise cost for each feature pair and hence the preference among them. Yadav et al.
[366] argue that assuming each user’s cost of changing different features is the same is unrealistic.
They propose asking for the user’s cost function or computing the expectation by sampling cost
functions from a distribution. Despite the progress, incorporating user preferences has not been
standardized and remains an expensive and elusive process. Ideally, a technique should be able to
collect preferences as a ranked list of features and provide CFEs that adhere to it.

Research Challenge 2. Counterfactual explanations should handle dynamics (data drift, classi-

fier update, applicant’s utility function changing, etc.)

All counterfactual explanation papers we review assume that the underlying black box is mono-
tonic and does not change over time. However, this might not be true; credit card companies and
banks update their models as frequently as 12-18 months [126]. Therefore, counterfactual expla-
nation algorithms should take data drift and the dynamism and non-monotonicity of the classifier
into account. There has not been much work for addressing this research question.

Research Challenge 3. The ability of counterfactual explanations to work with missing feature

values.

Counterfactual explanation algorithms should also be able to handle missing feature values,
which often happens in the real world [125]. There has not been much work for addressing this
research question.

Research Challenge 4. Preserving model privacy.

Privacy attacks on ML models can come in two major forms: member inference and model
extraction. Both of these privacy attacks can be enhanced due to the provision of CFEs. Aïvodji
et al. [7] empirically demonstrate that adversaries can train a surrogate model with very high
fidelity to the original model (i.e., model extraction attack) with as few as 1,000 queries to the model
(which is required during CFE generation). The problem is further aggravated when diverse CFEs

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 20 -->

312:20

S. Verma et al.

are provided. Shokri et al. [299] have demonstrated that gradient-based explanations methods leak
a lot of information and make the models vulnerable to membership inference attacks. Miura et al.
[240] propose MEGEX, a data-free model extraction attack that learns a surrogate model without
access to its training data by training a generative model. Wang et al. [350] propose using the CFE
of a CFE to train a surrogate model and show that it is more efficient in model extraction when
compared to [7]. Most of the works point out to the challenges CFE presents for the privacy of the
models, while the solutions remain elusive.

Research Challenge 5. Counterfactual explanations as an interactive service to the applicants.

Counterfactual explanations should be provided as an interactive interface, where an individual
can come at regular intervals, inform the system of the modified state, and get updated instructions
to achieve the counterfactual state. This can help when the individual could not precisely follow
the earlier advice for various reasons.

Progress: Hohman et al. [155] developed an interactive user-interface for providing expla-
nations to data scientists. They found out that data scientists used interactivity as the primary
mechanism for exploring, comparing, and explaining predictions. Sokol and Flach [305] propose
to enhance ML explanations with a voice-assisted interactive service. Akula et al. [9] propose an ap-
proach that explains an ML model using an interactive sequence of CFEs. Wang et al. [349] propose
refining the CFEs for different feature change costs based on user interactions. An ideal approach
to solve this problem would develop an interactive platform that will tailor a counterfactual for
the updated features at each step of the interaction.

Research Challenge 6. Counterfactual explanations should account for bias in the classifier.

Counterfactuals potentially capture and reflect the bias in the models. To underscore this as a
possibility, Ustun et al. [331] experimented on the difference in the difficulty of attaining a coun-
terfactual state across genders, which clearly showed a significant difference. More work must be
done to find how equally easy counterfactual explanations can be provided across different demo-
graphic groups, or how adjustments should be made to the prescribed changes to account for the
bias.

Progress: Rawal and Lakkaraju [278] generate recourse rules for a subgroup that they use to
detect model biases. Gupta et al. [145] propose adding a regularizer while training a classifier that
encourages the classifier to maintain a similar distance of the decision boundary from different
demographic groups, thereby facilitating the opportunity of equal recourse across demographic
groups (which is their definition of fairness). von Kügelgen et al. [344] extend this fairness notion
when the distance between the recourse is measured in a causal manner. Galhotra et al. [123] pro-
pose LEWIS that uses CFEs to identify racial bias in COMPAS and gender in Adult datasets. Dash
et al. [77] propose using CFEs to detect bias in image classifiers and counterfactual regularizer to
counteract that bias. However, an approach that consider the bias of the classifier while generating
CFEs stills needs to be researched.

Research Challenge 7. Generating optimal recourses when considering a multi-agent scenario.

O’Brien and Kim [253] demonstrate the non-optimality of recourses generated when a single
agent’s interest is considered in a multi-agent scenario like the prisoner’s dilemma. In the real
world, an agent’s actions affect other agents, hence generating recourses that consider the interests
of multiple agents would be useful. There has not been much work for addressing this research
question.

Research Challenge 8. Strengthen the ties between machine learning and regulatory commu-

nities.

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 21 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:21

A joint statement between the machine learning community and regulatory community (OCC,
Federal Reserve, FTC, CFPB) acknowledging successes and limitations of where counterfactual ex-
planations will be adequate for legal and consumer-facing needs and would improve the adoption
and use of counterfactual explanations in critical software.

Progress: Reed et al. [280] talk about how regulation and policies need to adapt to how ML
models can explain their decisions. However much more needs to be done in order to enhance the
adoption of CFEs.

Research Challenge 9. Guarding against fairwashing.

Aivodji et al. [5, 6] have pointed out the risk of an adversary using model explanations to ratio-
nalize a model’s decisions and obscure its bias. It remains to be seen if the fair recourse approaches
can guard against fairwashing.

Research Challenge 10. Enhance real-world deployment of counterfactuals.

Progress: There has been one known case of real-world deployment of counterfactuals at Hired
platforms for providing advice to candidates seeking jobs [250]. Deploying CFEs in more real world
applications will improve our understanding of user preferences and highlight new research chal-
lenges.

Research Challenge 11. Counterfactual explanations should also inform the applicants about

what must not change

Suppose a CFE advises someone to increase their income but does not tell that their length of
last employment should not decrease. To increase their income, the applicant who switches to a
higher-paying job may find themselves in a worse position than earlier. Thus, by failing to disclose
what must not change, an explanation may lead the applicant to an unsuccessful state [30]. This
corroborates RC5, whereby an applicant might be able to interact with a platform to see the effect
of a potential real-world action they are considering taking to achieve the counterfactual state.

9.2 Questions with Significant Research Progress

In this section, we highlight the research progress made for towards previously open questions.

Research Problem 1. Unify counterfactual explanations with traditional “explainable AI.”

Although counterfactual explanations have been credited to eliciting causal thinking and provid-
ing actionable feedback to users, they do not tell which feature(s) was the principal reason for the
original decision and why. It would be nice if, along with giving actionable feedback, counterfac-
tual explanations also gave the reason for the original decision, which can help applicants under-
stand the model’s logic. This is addressed by traditional “explainable AI” methods like LIME [281],
Anchors [282], Grad-CAM [294].

Progress: Guidotti et al. [139] have attempted this unification, as they first learn a local deci-
sion tree and then interpret the inversion of decision nodes of the tree as counterfactual explana-
tions. However, they do not show the CFEs they generate, and their technique also misses other
desiderata of counterfactuals (see Section 4.1). Kommiya Mothilal et al. [196] propose necessity and
sufficiency as the two important properties of an explanation. Feature attribution explanations find
the feature values that are sufficient for a prediction, while CFEs find the feature values that are
necessary for a prediction. They propose methods to find the necessity and sufficiency of any fea-
ture subset and discuss how that aligns with finding CFEs. Galhotra et al. [123] propose Lewis

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 22 -->

312:22

S. Verma et al.

that also emphasizes the necessity and sufficiency scores of a feature subset in finding its global im-
portance and in generating a CFE for local explainability. Jia et al. [171] propose to use DeepLIFT
to assign contribution scores to the features that changed in a counterfactual datapoint. Ramon
et al. [271] rank the feature importances using LIME and SHAP, and then remove the features in
decreasing order of importance until a CFE is found. Wiratunga et al. [361] propose to use methods
like LIME and SHAP to find feature importances and then replace the features in decreasing order
of importance with the values borrowed from the nearest unlike neighbor (case-based reasoning
approach). Albini et al. [10] propose to change the background distribution used to compute the
Shapley values to make the feature attribution amount to the counterfactual-ability of the features,
i.e., changing a feature with higher attribution would have a higher probability of changing the
prediction. Wang and Vasconcelos [347] propose to use the discriminant attribution explanations
as a way to produce CFEs for images. Wijekoon et al. [360] use LIME to assist case-based reasoning
techniques to generate CFEs. Ge et al. [127] propose using counterfactual-ability of features as a
metric for their feature importance.

Research Problem 2. Provide counterfactual explanations as discrete and sequential steps of

actions.

Most counterfactual generation approaches return the modified datapoint, which would receive
the desired classification. The modified datapoint (state) reflects the idea of instantaneous and
continuous actions, but in the real world, actions are discrete and often sequential. Therefore, the
counterfactual generation process must take the discreteness of actions into account and provide a
series of actions that would take the individual from the current state to the modified state, which
has the desired class label.

Progress: Naumann and Ntoutsi [247] argue that to help an individual achieve the desired
goal, CFEs should be provided as a sequential step of actions instead of just providing the final
goal. Singh et al. [300] conduct a user study to show the high preference for a sequential step
of actions steps over a single-step goal. Ramakrishnan et al. [270] propose a program synthesis
based technique to generate such sequences. Kanamori et al. [181] propose a mixed-integer based
programming method and Verma et al. [337] propose an RL-based method that generates ordered
sequences of actions as a CFE.

Research Problem 3. The ability of counterfactual explanations to work with incomplete—or

missing—causal graphs.

Incorporating causality in the counterfactual generation is essential for the CFEs to be grounded
in reality. Complete causal graphs and structural equations are rarely available in the real world,
and therefore the algorithm should be able to work with incomplete causal graphs.

Progress: Mahajan et al. [229]’s approach was the first to be compatible with incomplete causal
graphs. Now other works like Galhotra et al. [123], Verma et al. [337], Schleich et al. [292], Yang
et al. [367] can also work with partial causal graphs.

Research Problem 4. Scalability and throughput of counterfactual explanations generation.

As we see in Table 1, most approaches need to solve an optimization problem to generate one
counterfactual explanation. Some papers generate multiple counterfactuals while optimizing once,
but they still need to optimize separately for different input datapoints. However, for industrial
deployment, the generation should be more scalable.

Progress: Mahajan et al. [229] learn a VAE which can generate multiple CFEs for any given
input datapoint after training. Therefore, their approach is highly scalable and is termed as “amor-
tized inference”. Verma et al. [337] proposed an RL-based technique, FastAR, that also generates

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 23 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:23

amortized CFEs. Van Looveren et al. [333], Samoilescu et al. [290], Yang et al. [367], Rawal and
Lakkaraju [278], and Nemirovsky et al. [250] also propose approaches to this end.

Research Problem 5. Generate robust counterfactual explanations [112, 239].

Counterfactual explanation optimization problems force the modified datapoint to obtain the
desired class label. However, the modified datapoint could be labeled either in a robust manner or
due to the classifier’s non-robustness, e.g., an overfitted classifier. Laugel et al. [209] term this as
the stability property of a counterfactual. There are three kinds of robustness needs: (1) robustness
to model changes when models are retrained, for example, (2) robustness to the input datapoint
(two individuals with a slight change in features should be given similar CFEs), and (3) robustness
to small changes in the attained CFE (a CFE with minor changes to the originally suggested CFE
should also be accepted).

Progress: Slack et al. [302] underscore this challenge by showing that small perturbations in
the input datapoints can result in drastically different CFEs. Rawal et al. [277] further emphasize
this challenge by empirically demonstrating the invalidation of already prescribed recourses when
the ML model gets retrained on datasets with temporal or geospatial distribution shifts. Artelt et al.
[23] evaluate the robustness of closest CFEs when contrasted with CFEs generated with the data
manifold constraint. Bueff et al. [47] propose the framework to measure the robustness of models
by purposing generated CFEs as adversarial attack datasets. Virgolin and Fracaros [342] empiri-
cally show that non-robust CFEs encounter a higher cost of change when adverse perturbations
are applied to the datapoint, thus concluding that robustness in CFEs should be considered.

Upadhyay et al. [330] propose a technique named ROAR that uses adversarial training to gen-
erate recourses robust to changes in an ML model that is retrained on a distributionally shifted
training dataset. Dominguez-Olmedo et al. [93] show that the CFEs that just cross the decision
boundary are usually non-robust and formulate an optimization problem that generates robust re-
course for linear models and neural networks. Pawelczyk et al. [262] propose a technique named
PROBE that generates robust CFEs while letting the users decide the tradeoff between the CFE
invalidation risk and its cost. Black et al. [37] argue that robust CFEs should have high=confidence
neighborhoods with small Lipschitz constants, and propose a Stable Neighbor Search algorithm to
that end. Bui et al. [48] propose an algorithm to generate robust CFEs by considering a distribution
over the parameters of the model if retrained. Dutta et al. [103] propose counterfactual stability
(the lower bound of the predicted class probability for the sampled datapoints in the neighbor-
hood of a given CFE) as a metric for filtering robust CFEs. Bajaj et al. [28] propose a technique to
generate robust CFEs for graph neural networks.

Research Problem 6. Extend counterfactual explanations beyond classification.

Progress: Recent work has been extending counterfactual explanations to different tasks and
model architectures. Spooner et al. [307] propose a Bayesian optimization-based technique for
generating CFEs for regression problems. Numeroso and Bacciu [252] propose an RL-based ap-
proach for generating CFEs for graph neural networks, which are used to predict chemical mole-
cule properties. Delaney et al. [82] propose a case-based reasoning approach to generate CFEs for
a time-series classifier.

Research Problem 7. Handling of categorical features in counterfactual explanations

Different articles have come up with various methods to handle categorical features, like con-
verting them to one-hot encoding and then enforcing the sum of those columns to be 1 using
regularization or a hard constraint, or clamping an optimization problem to a specific categori-
cal value, or leaving them to be automatically handled by genetic approaches and SMT solvers.

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 24 -->

312:24

S. Verma et al.

Measuring distance in categorical features is also not obvious. Some articles use an indicator func-
tion, which equates to 1 for unequal values and 0 if the same; other papers convert to one-hot
encoding and use standard distance metrics like L1/L2 norm, or use the distance in Markov chains
[115]. Therefore, handling categorical variables have not been standardized, future research must
consider this and develop appropriate methods.

Research Problem 8. Evaluate counterfactual explanations using a user study.

The evaluation for counterfactual explanations must be done using a user study because eval-
uation proxies (see Section 6) might not be able to precisely capture the psychological and other
intricacies of human cognition on the ease of actionability of a counterfactual. Keane et al. [187]
emphasize the importance of user studies in the context of CFEs.

Progress: Förster et al. [116] conduct a user study with 144 participants to understand the
format of explanation they prefer. They conclude that users prefer concrete, consistent, relevant
explanations, and lengthy explanations if they are concrete. Förster et al. [115] conduct a user study
with 46 participants who were asked to rate the realisticness of the CFEs generated by theirs and
a baseline approach. Using statistical tests, they concluded that the CFEs generated by their ap-
proach were perceived to be more real and typical. Rawal and Lakkaraju [278] conduct a user
study with 21 participants who were asked to detect a bias in the recourse summaries for demo-
graphic groups. Kanamori et al. [180] conduct a user study with 35 participants to compare their
global CFE generating technique with that of Rawal and Lakkaraju [278]. Singh et al. [300] conduct
a user study with 54 participants and found that most users prefer specific directives over generic
and non-directive explanations. Warren et al. [353] conduct a user study with 127 participants and
found that counterfactual explanations elicited higher trust and satisfaction than causal explana-
tions. Yacoby et al. [365] conduct a user study with eight U.S. state court judges to understand
their response to CFEs from pretrial risk assessment instruments (PRAI). They conclude that
judges ignored the CFEs and focused on the factual features of the defendant. Kuhl et al. [204]
conduct a user study with 74 users in an interactive game setting and found that users benefit
less from receiving computationally plausible CFEs than the closest CFEs (measured using feature
distance). Zhang. et al. [376] conduct a user study with 200 users to check their understanding
of global, local, and CF explanations. Cai et al. [51] conduct a user study on 1070 participants to
understand how users perceive explanations when provided examples from the desired class vs.
when provided examples from all other classes. Celar and Byrne [57] conduct a user study with
731 participants and concluded that counterfactual explanations were perceived to be better expla-
nations than factual explanations (explanations justifying the original model prediction). Dai et al.
[74] conduct a user study with 243 participants and found that counterfactual and prefactual expla-
nations were equally helpful. Delaney et al. [84] conduct a user study and found that participants
prefer large, meaningful edits for counterfactual explanations for images.

Research Problem 9. Counterfactual explanations should be integrated with data visualization

interfaces.

Counterfactual explanations will directly interact with consumers with varying technical knowl-
edge levels; therefore, counterfactual generation algorithms should be integrated with visualiza-
tion interfaces. We already know that visualization can influence human behavior [70], and a
collaboration between machine learning and HCI communities could help address this challenge.

Progress: Cheng et al. [64], Gomez et al. [132, 133], Leung et al. [214], and Wexler et al. [356]
have developed interactive graphical user interfaces for displaying CFEs. DECE [64] also summa-
rizes CFEs for subgroups that can help detect model biases, if any. Tamagnini et al. [312] develop

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 25 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:25

a visualization tool for CFEs for text classification models. Hohman et al. [155] also build a visual
interactive user interface for providing model explanations.

Research Problem 10. Incentivize users to improve features in non-manipulative ways.

An approach that provides a recourse to users might want to prevent the “gamification” of the
model (when users manipulate simple features like the purpose of a loan to get approved). This
also protects the ML models from adversarial robustness attacks.

Progress: Chen et al. [62] propose the optimization objective for linear classification models
when the goal is to develop an accurate model that encourages actual feature improvement for
users. They categorize features into three categories: improvement, manipulative, and immutable.
Users should be encouraged to change the improvement features, not the manipulative ones when
optimizing for recourse. König et al. [206] suggest using causality to generate meaningful recourses
and prevent gamification of the model.

10 Conclusions

In this article, we collected and reviewed more than 350 papers which proposed various algo-
rithmic solutions to finding counterfactual explanations for the decisions produced by automated
systems, specifically automated by machine learning. Evaluating all the papers on the same rubric
helps in quickly understanding the peculiarities of different approaches and the advantages, and
disadvantages of each of them, which can also help organizations choose the algorithm best suited
to their application constraints. This has also helped us readily identify the gaps, which will be
beneficial to researchers scouring for open problems in this space and quickly sifting the large
body of literature. We hope this article can also be the starting point for people wanting to get an
introduction to the broad area of counterfactual explanations and guide them to proper resources
for things they might be interested in.

Appendices

A Full Table
Initially, we categorized the set of papers with more columns and in a much larger table. We
selected the most critical columns and put them in Table 1. The full table is available here.

B Burgeoning Legal Frameworks around Explanations in AI
To increase the accountability of automated decision systems—specifically, AI systems—laws
and regulations regarding the decisions produced by such systems have been proposed and
implemented across the globe [94]. The most recent version of the European Union’s General
Data Protection Regulation (GDPR), enforced starting on May 25, 2018, offered a right to
information about the existence, logic, and envisaged consequences of such a system [134]. This
also includes the right to not be a subject of an automated decision-making system. Although
the closeness of this law to “right to explanation” is debatable and ambiguous [345], the official
interpretation by Working Party for Article 29 has concluded that the GDPR requires explanations
of specific decisions, and therefore counterfactual explanations are apt. In the US, the Equal
Credit Opportunity Act (ECOA) and the Fair Credit Reporting Act (FCRA) require the
creditor to inform the reasons for an adverse action, such as rejection of a loan request [58, 59].
They generally compare the applicant’s feature to the average value in the population to arrive at
the principal reasons. Government reports from the United Kingdom [254] and France [166, 341]
also touched on the issue of explainability in AI systems. In the US, Defense Advanced
Research Projects Agency (DARPA) launched the Explainable AI (XAI) program in 2016

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 26 -->

312:26

S. Verma et al.

to encourage research into designing explainable models, understanding the psychological
requirements of explanations, and the design of explanation interfaces [76]. The European
Union has taken similar initiatives as well [67, 329]. The US White House recently put forward
the Blueprint for an AI Bill of Rights [158] to modulate decisions from automated systems.
The Bill outlines five principles for operating such systems: (1) safe and effective systems, (2)
algorithmic discrimination protections, (3) data privacy, (4) explanations for decisions made using
such systems, and (5) discussion about human alternatives. While many techniques have been
proposed for explainable machine learning, it is yet unclear if and how these specific techniques
can help address the letter of the law. Future collaboration between AI researchers, regulators,
the legal community, and consumer watchdog groups will help ensure the development of
trustworthy AI.

Acknowledgments
We thank Jason Wittenbach, Aditya Kusupati, Divyat Mahajan, Jessica Dai, Soumye Singhal, Harsh
Vardhan, and Jesse Michel for helpful comments.

References

[1] Abubakar Abid, Mert Yuksekgonul, and James Zou. 2022. Meaningfully debugging model mistakes using conceptual
counterfactual explanations. In Proceedings of the 39th International Conference on Machine Learning. PMLR, 66–88.
https://proceedings.mlr.press/v162/abid22a.html

[2] Carlo Abrate and Francesco Bonchi. 2021. Counterfactual graphs for explainable classification of brain networks

(KDD ’21). ACM, New York, 10. https://doi.org/10.1145/3447548.3467154

[3] Amina Adadi and Mohammed Berrada. 2018. Peeking inside the black-box: A survey on explainable artificial intelli-

gence (XAI). IEEE Access PP (09 2018), 1–1. https://doi.org/10.1109/ACCESS.2018.2870052

[4] Charu C. Aggarwal, Chen Chen, and Jiawei Han. 2010. The inverse classification problem. J. Comput. Sci. Technol.

(2010), 458–468. https://doi.org/10.1007/s11390-010-9337-x

[5] Ulrich Aïvodji, Hiromi Arai, Olivier Fortineau, Sébastien Gambs, Satoshi Hara, and Alain Tapp. 2019. Fairwashing:
The risk of rationalization. In Proceedings of the 36th International Conference on Machine Learning. PMLR. https://
proceedings.mlr.press/v97/aivodji19a.html

[6] Ulrich Aïvodji, Hiromi Arai, Sébastien Gambs, and Satoshi Hara. 2021. Characterizing the risk of fairwashing. In
Advances in Neural Information Processing Systems, Vol. 34. Curran Associates, Inc. https://proceedings.neurips.cc/
paper/2021/file/7caf5e22ea3eb8175ab518429c8589a4-Paper.pdf

[7] Ulrich Aïvodji, Alexandre Bolot, and Sébastien Gambs. 2020. Model extraction from counterfactual explanations.

arXiv:2009.01884 (2020).

[8] Arjun Akula, Shuai Wang, and Song-Chun Zhu. 2020. CoCoX: Generating conceptual and counterfactual explana-
tions via fault-lines. In Proceedings of the AAAI Conference on Artificial Intelligence 34, 03 (Apr. 2020), 2594–2601.
https://doi.org/10.1609/aaai.v34i03.5643

[9] Arjun R. Akula, Keze Wang, Changsong Liu, Sari Saba-Sadiya, Hongjing Lu, Sinisa Todorovic, Joyce Chai, and Song-
Chun Zhu. 2022. CX-ToM: Counterfactual explanations with theory-of-mind for enhancing human trust in image
recognition models. iScience 25, 1 (2022), 103581. https://doi.org/10.1016/j.isci.2021.103581

[10] Emanuele Albini, Jason Long, Danial Dervovic, and Daniele Magazzeni. 2022. Counterfactual shapley additive expla-

nations (FAccT ’22). ACM, New York, 17. https://doi.org/10.1145/3531146.3533168

[11] Emanuele Albini, Antonio Rago, Pietro Baroni, and Francesca Toni. 2021. Influence-driven explanations for Bayesian
network classifiers. In PRICAI 2021. Springer-Verlag, Berlin, , 13. https://doi.org/10.1007/978-3-030-89188-67
[12] Gohar Ali, Feras Al-Obeidat, Abdallah Tubaishat, Tehseen Zia, Muhammad Ilyas, and Alvaro Rocha. 2021. Counter-
factual explanation of Bayesian model uncertainty. Neural Computing and Applications (Sept. 2021). https://doi.org/
10.1007/s00521-021-06528-z

[13] Kamran Alipour, Arijit Ray, Xiao Lin, Michael Cogswell, Jurgen P. Schulze, Yi Yao, and Giedrius T. Burachas. 2021.
Improving users’ mental model with attention-directed counterfactual edits. Applied AI Letters 2, 4 (2021). https:
//doi.org/10.1002/ail2.47

[14] Robert Andrews, Joachim Diederich, and Alan B. Tickle. 1995. Survey and critique of techniques for extracting rules
from trained artificial neural networks. Know.-Based Syst. 8, 6 (1995), 17. https://doi.org/10.1016/0950-7051(96)81920-
4

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 27 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:27

[15] Javier Antoran, Umang Bhatt, Tameem Adel, Adrian Weller, and José Miguel Hernández-Lobato. 2021. Getting a
CLUE: A method for explaining uncertainty estimates. In Proceedings of the International Conference on Learning
Representations. https://openreview.net/forum?id=XSLF1XFq5h

[16] Daniel Apley and Jingyu Zhu. 2020. Visualizing the effects of predictor variables in black box supervised learning
models. Journal of the Royal Statistical Society: Series B (Statistical Methodology) 82(4) (06 2020), 1059–1086. https://
doi.org/10.1111/rssb.12377

[17] André Artelt. 2019 - 2021. CEML: Counterfactuals for Explaining Machine Learning Models. https://www.

github.com/andreArtelt/ceml

[18] André Artelt and Barbara Hammer. 2019. On the Computation of Counterfactual Explanations – A Survey. http://

arxiv.org/abs/1911.07749

[19] André Artelt and Barbara Hammer. 2020. Efficient Computation of Contrastive Explanations. https://doi.org/

10.48550/ARXIV.2010.02647

[20] André Artelt and Barbara Hammer. 2021. Convex Optimization for Actionable & Plausible Counterfactual Explana-

tions. https://doi.org/10.48550/ARXIV.2105.07630

[21] André Artelt and Barbara Hammer. 2022. “Even if ...” – Diverse Semifactual Explanations of Reject. arXiv:2207.01898
[22] André Artelt, Fabian Hinder, Valerie Vaquet, Robert Feldhans, and Barbara Hammer. 2021. Contrastive explana-
tions for explaining model adaptations. In Advances in Computational Intelligence. Springer International Publishing,
Cham, 101–112. https://doi.org/10.1007/978-3-030-85030-29

[23] André Artelt, Valerie Vaquet, Riza Velioglu, Fabian Hinder, Johannes Brinkrolf, Malte Schilling, and Barbara Hammer.
2021. Evaluating robustness of counterfactual explanations. In Proceedings of the 2021 IEEE Symposium Series on
Computational Intelligence (SSCI) (2021), 01–09. https://doi.org/10.1109/SSCI50451.2021.9660058

[24] Saugat Aryal. 2024. Semi-factual explanations in AI. In Proceedings of the AAAI Conference on Artificial Intelligence

38 (2024), 23379–23380. https://doi.org/10.1609/aaai.v38i21.30390

[25] Nicholas Asher, Lucas De Lara, Soumya Paul, and Chris Russell. 2022. Counterfactual models for fair and adequate
explanations. Machine Learning and Knowledge Extraction 4, 2 (2022), 316–349. https://doi.org/10.3390/make4020014
[26] Emre Ates, Burak Aksar, Vitus J. Leung, and Ayse K. Coskun. 2021. Counterfactual explanations for multivariate
time series. In Proceedings of the 2021 International Conference on Applied Artificial Intelligence (ICAPAI’21). 1–8. https:
//doi.org/10.1109/ICAPAI49758.2021.9462056

[27] Davide Bacciu and Danilo Numeroso. 2022. Explaining deep graph networks via input perturbation. IEEE Transactions

on Neural Networks and Learning Systems (2022). https://doi.org/10.1109/TNNLS.2022.3165618

[28] Mohit Bajaj, Lingyang Chu, Zi Yu Xue, Jian Pei, Lanjun Wang, Peter Cho-Ho Lam, and Yong Zhang. 2021. Robust

Counterfactual Explanations on Graph Neural Networks. https://doi.org/10.48550/ARXIV.2107.04086

[29] Rachana Balasubramanian, Samuel Sharpe, Brian Barr, Jason Wittenbach, and C. Bayan Bruss. 2020. Latent-CF: A

Simple Baseline for Reverse Counterfactual Explanations. https://doi.org/10.48550/ARXIV.2012.09301

[30] Solon Barocas, Andrew D. Selbst, and Manish Raghavan. 2020. The hidden assumptions behind counterfactual ex-
planations and principal reasons. In Proceedings of the Conference on Fairness, Accountability, and Transparency
(FAccT’20) (FAT* ’20). ACM, New York, 10. https://doi.org/10.1145/3351095.3372830

[31] Brian Barr, Matthew R. Harrington, Samuel Sharpe, and C. Bayan Bruss. 2021. Counterfactual Explanations via Latent

Space Projection and Interpolation. https://doi.org/10.48550/ARXIV.2112.00890

[32] C. Van Fraassen Bas. 1980. The Scientific Image. Oxford University Press.
[33] Barry Becker and Ronny Kohavi. 1996. Adult. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20
[34] Sander Beckers. 2022. Causal Explanations and XAI. https://doi.org/10.48550/ARXIV.2201.13169
[35] Leopoldo Bertossi. 2021. Declarative approaches to counterfactual explanations for classification. Theory and Practice

of Logic Programming 23 (12 2021), 1–35. https://doi.org/10.1017/S1471068421000582

[36] Reuben Binns, Max Van Kleek, Michael Veale, Ulrik Lyngs, Jun Zhao, and Nigel Shadbolt. 2018. ’It’s reducing a human
being to a percentage’: Perceptions of justice in algorithmic decisions. In Proceedings of CHI 2018. ACM, New York,
14. https://doi.org/10.1145/3173574.3173951

[37] Emily Black, Zifan Wang, and Matt Fredrikson. 2022. Consistent counterfactuals for deep models. In Proceedings of

the International Conference on Learning Representations. https://arxiv.org/abs/2110.03109

[38] Jock Blackard. 1998. Covertype. UCI Machine Learning Repository. https://doi.org/10.24432/C50K5N
[39] Pierre Blanchart. 2021. An Exact Counterfactual-example-based Approach to Tree-ensemble Models Interpretability.

https://doi.org/10.48550/ARXIV.2105.14820

[40] R. D. Boch and M. Lieberman. 1970. Fitting a response model for n dichotomously scored items. Psychometrika 35

(1970), 179–97.

[41] Sebastian Bordt, Michèle Finck, Eric Raidl, and Ulrike von Luxburg. 2022. Post-Hoc Explanations Fail to Achieve

their Purpose in Adversarial Contexts. https://arxiv.org/abs/2201.10295

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 28 -->

312:28

S. Verma et al.

[42] Zeyd Boukhers, Timo Hartmann, and Jan Jürjens. 2022. COIN: Counterfactual Image Generation for VQA Interpre-

tation. https://doi.org/10.48550/ARXIV.2201.03342

[43] Martim Brandão, Gerard Canal, Senka Krivić, Paul Luff, and Amanda Coles. 2021. How experts explain motion
planner output: A preliminary user-study to inform the design of explainable planners. In Proceedings of the 2021
30th IEEE International Conference on Robot & Human Interactive Communication (RO-MAN’21). 299–306. https://
doi.org/10.1109/RO-MAN50785.2021.9515407

[44] Katherine Elizabeth Brown, Doug Talbert, and Steve Talbert. 2021. The uncertainty of counterfactuals in deep learn-
ing. In The International FLAIRS Conference Proceedings 34 (2021). https://doi.org/10.32473/flairs.v34i1.128795
[45] Kieran Browne and Ben Swift. 2020. Semantics and Explanation: Why Counterfactual Explanations Produce Adver-

sarial Examples in Deep Neural Networks. https://doi.org/10.48550/ARXIV.2012.10076

[46] Dieter Brughmans and David Martens. 2021. NICE: An Algorithm for Nearest Instance Counterfactual Explanations.

https://doi.org/10.48550/ARXIV.2104.07411

[47] Andreas C. Bueff, Mateusz Cytryński, Raffaella Calabrese, Matthew Jones, John Roberts, Jonathon Moore, and Iain
Brown. 2022. Machine learning interpretability for a stress scenario generation in credit scoring based on counter-
factuals. Expert Systems with Applications 202 (2022). https://doi.org/10.1016/j.eswa.2022.117271

[48] Ngoc Bui, Duy Nguyen, and Viet Anh Nguyen. 2022. Counterfactual Plans under Distributional Ambiguity. https://

doi.org/10.48550/ARXIV.2201.12487

[49] Ruth Byrne. 2008. The rational imagination: How people create alternatives to reality. The Behavioral and Brain

Sciences 30 (2008), 439–53; discussion 453. https://doi.org/10.1017/S0140525X07002579

[50] Ruth M. J. Byrne. 2019. Counterfactuals in explainable artificial intelligence (XAI): Evidence from human reasoning.
In Proceedings of the 28th International Joint Conference on Artificial Intelligence (IJCAI-19). International Joint Con-
ferences on Artificial Intelligence Organization, California, USA, 6276–6282. https://doi.org/10.24963/ijcai.2019/876
[51] Carrie J. Cai, Jonas Jongejan, and Jess Holbrook. 2019. The effects of example-based explanations in a machine

learning interface (IUI ’19). ACM, New York, 258–262. https://doi.org/10.1145/3301275.3302289

[52] Miguel Á. Carreira-Perpiñán and Suryabhan Singh Hada. 2021. Counterfactual explanations for oblique decision
trees: Exact, efficient algorithms. In Proceedings of the AAAI Conference on Artificial Intelligence 35 (May 2021), 6903–
6911. https://doi.org/10.1609/aaai.v35i8.16851

[53] Emilio Carrizosa, Jasone Ramirez-Ayerbe, and Dolores Romero Morales. 2021. Generating Collective Coun-
terfactual Explanations in Score-Based Classification via Mathematical Optimization. https://doi.org/10.13140/
RG.2.2.22996.12168/1

[54] Emilio Carrizosa, Jasone Ramírez-Ayerbe, and Dolores Romero Morales. 2022. Counterfactual Explanations for Func-

tional Data: A Mathematical Optimization Approach. https://doi.org/10.13140/RG.2.2.25682.68801

[55] Emilio Carrizosa, Jasone Ramírez-Ayerbe, and Dolores Romero Morales. 2024. Mathematical optimization modelling
for group counterfactual explanations. European Journal of Operational Research (2024). https://doi.org/10.1016/
j.ejor.2024.01.002

[56] Diogo V. Carvalho, Eduardo M. Pereira, and Jaime S. Cardoso. 2019. Machine learning interpretability: A survey on

methods and metrics. Electronics 8 (2019), 832. https://doi.org/10.3390/electronics8080832

[57] Lenart Celar and Ruth M. J. Byrne. 2023. How people reason with counterfactual and causal explanations for
artificial intelligence decisions in familiar and unfamiliar domains. Memory & Cognition 51, 7 (2023), 1481–1496.
https://doi.org/10.3758/s13421-023-01407-5

[58] CFPB.

[n. d.]. Adverse Action Notice Requirements Under

the ECOA and the

FCRA. https://

consumercomplianceoutlook.org/2013/second-quarter/adverse-action-notice-requirements-under-ecoa-fcra/.
Accessed: 2020-10-15.

[59] CFPB. [n. d.]. Notification of Action Taken, ECOA Notice, and Statement of Specific Reasons. https://www.

consumerfinance.gov/policy-compliance/rulemaking/regulations/1002/9/. Accessed: 2020-10-15.

[60] Qianglong Chen, Feng Ji, Xiangji Zeng, Feng-Lin Li, Ji Zhang, Haiqing Chen, and Yin Zhang. 2021. KACE: Gen-
erating knowledge aware contrastive explanations for natural language inference. In Proceedings of the 59th An-
nual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natu-
ral Language Processing. Association for Computational Linguistics, Online, 2516–2527. https://doi.org/10.18653/v1/
2021.acl-long.196

[61] Tsong Yueh Chen, Fei-Ching Kuo, Huai Liu, Pak-Lok Poon, Dave Towey, T. H. Tse, and Zhi Quan Zhou. 2018. Meta-
morphic testing: A review of challenges and opportunities. ACM Comput. Surv. 51, 1 (2018), 27. https://doi.org/
10.1145/3143561

[62] Yatong Chen,

Jialu Wang, and Yang Liu. 2020. Strategic Recourse in Linear Classification. https:

//dynamicdecisions.github.io

[63] Ziheng Chen, Fabrizio Silvestri, Jia Wang, He Zhu, Hongshik Ahn, and Gabriele Tolomei. 2021. ReLAX: Reinforce-
ment Learning Agent eXplainer for Arbitrary Predictive Models. https://doi.org/10.48550/ARXIV.2110.11960

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 29 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:29

[64] Furui Cheng, Yao Ming, and Huamin Qu. 2020. DECE: Decision Explorer with Counterfactual Explanations for Ma-

chine Learning Models. arXiv:cs.LG/2008.08353

[65] Noel Codella, Veronica Rotemberg, Philipp Tschandl, M. Emre Celebi, Stephen Dusza, David Gutman, Brian Helba,
Aadi Kalloo, Konstantinos Liopyris, Michael Marchetti, Harald Kittler, and Allan Halpern. 2019. Skin Lesion Analysis
Toward Melanoma Detection 2018: A Challenge Hosted by the International Skin Imaging Collaboration (ISIC). https:
//doi.org/10.48550/ARXIV.1902.03368

[66] Gregory Cohen, Saeed Afshar, Jonathan C. Tapson, and André van Schaik. 2017. EMNIST: Extending MNIST to
handwritten letters. In Proceedings of the 2017 International Joint Conference on Neural Networks (IJCNN) (2017),
2921–2926. https://doi.org/10.1109/IJCNN.2017.7966217

[67] European Commission. [n. d.]. Artificial Intelligence. https://ec.europa.eu/info/funding-tenders/opportunities/

portal/screen/opportunities/topic-details/ict-26-2018-2020. Accessed: 2020-10-15.

[68] European Commission. [n. d.]. REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE
COUNCIL of 27 April 2016 on the Protection of Natural Persons with Regard to the Processing of Personal Data
and on the Free Movement of Such Data, and Repealing Directive 95/46/EC (General Data Protection Regulation).
https://eur-lex.europa.eu/eli/reg/2016/679/oj. Accessed: 2020-10-15.

[69] Zicun Cong, Lingyang Chu, Yu Yang, and Jian Pei. 2021. Comprehensible counterfactual explanation on Kolmogorov-

Smirnov test. Proc. VLDB Endow. 14, 9 (2021), 1583–1596. https://doi.org/10.14778/3461535.3461546

[70] Michael Correll. 2019. Ethical dimensions of visualization research. In Proceedings of CHI ’19. ACM, New York„ 13.

https://doi.org/10.1145/3290605.3300418

[71] Paulo Cortez. 2014. Student Performance. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T
[72] Mark W. Craven and Jude W. Shavlik. 1995. Extracting tree-structured representations of trained networks. In Pro-
ceedings of the 8th International Conference on Neural Information Processing Systems (NIPS’95). MIT Press, Cambridge,
MA, USA, 24–30.

[73] Riccardo Crupi, Beatriz San Miguel González, Alessandro Castelnovo, and Daniele Regoli. 2022. Leveraging causal
relations to provide counterfactual explanations and feasible recommendations to end users. In Proceedings of the
14th International Conference on Agents and Artificial Intelligence - Volume 2: ICAART,. SciTePress, 24–32. https://
doi.org/10.5220/0010761500003116

[74] Xinyue Dai, Mark T. Keane, Laurence Shalloo, Elodie Ruelle, and Ruth M. J. Byrne. 2022. Counterfactual explanations
for prediction and diagnosis in XAI. In Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society (AIES
’22). ACM, New York„ 12. https://doi.org/10.1145/3514094.3534144

[75] Susanne Dandl, Christoph Molnar, Martin Binder, and Bernd Bischl. 2020. Multi-objective counterfactual explana-
tions. In Proceedings of PPSN XVI. Springer International Publishing, Cham, 448–469. https://doi.org/10.1007/978-3-
030-58112-131

[76] DARPA. [n. d.]. Broad Agency Announcement: Explainable Artificial Intelligence (XAI). https://www.darpa.mil/

attachments/DARPA-BAA-16-53.pdf. Accessed: 2020-10-15.

[77] Saloni Dash, Vineeth N Balasubramanian, and Amit Sharma. 2022. Evaluating and mitigating bias in image classi-
fiers: A causal perspective using counterfactuals. In Proceedings of the IEEE/CVF Winter Conference on Applications
of Computer Vision (WACV’22). 915–924. https://doi.org/10.1109/WACV51458.2022.00393

[78] A. Datta, S. Sen, and Y. Zick. 2016. Algorithmic transparency via quantitative input influence: Theory and experi-
ments with learning systems. In Proceedings of 2016 IEEE Symposium on Security and Privacy (SP’16). IEEE, New York,
, 598–617. https://doi.org/10.1109/SP.2016.42

[79] Lucas de Lara, Alberto González-Sanz, Nicholas Asher, and Jean-Michel Loubes. 2021. Transport-based Counterfac-

tual Models. https://doi.org/10.48550/ARXIV.2108.13025

[80] Giovanni De Toni, Bruno Lepri, and Andrea Passerini. 2022. Synthesizing Explainable Counterfactual Policies for

Algorithmic Recourse with Program Synthesis. https://doi.org/10.48550/ARXIV.2201.07135

[81] Sarah Dean, Sarah Rich, and Benjamin Recht. 2020. Recommendations and user agency: The reachability of
collaboratively-filtered information. In Proceedings of FAT* ’20. ACM, New York, 10. https://doi.org/10.1145/3351095.
3372866

[82] Eoin Delaney, Derek Greene, and Mark T. Keane. 2021. Instance-based counterfactual explanations for time series
classification. In Proceedings of the 29th International Conference on Case-Based Reasoning Research and Development
(ICCBR 2021), (Salamanca, Spain, September 13–16, 2021). , . Springer-Verlag, Berlin, , 32–47. https://doi.org/10.1007/
978-3-030-86957-13

[83] Eoin Delaney, Derek Greene, and Mark T. Keane. 2021. Uncertainty Estimation and Out-of-Distribution Detection

for Counterfactual Explanations: Pitfalls and Solutions. https://arxiv.org/abs/2107.09734

[84] Eoin Delaney, Arjun Pakrashi, Derek Greene, and Mark T. Keane. 2023. Counterfactual explanations for misclassi-
fied images: How human and machine explanations differ. Artificial Intelligence 324 (2023), 103995. https://doi.org/
10.1016/j.artint.2023.103995

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 30 -->

312:30

S. Verma et al.

[85] Houtao Deng. 2014. Interpreting tree ensembles with inTrees. arXiv:1408.5456 (08 2014). https://doi.org/10.1007/

s41060-018-0144-8

[86] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. 2009. ImageNet: A large-scale hierarchical
image database. In Proceedings of the 2009 IEEE Conference on Computer Vision and Pattern Recognition. 248–255.
https://doi.org/10.1109/CVPR.2009.5206848

[87] Amit Dhurandhar, Pin-Yu Chen, Ronny Luss, Chun-Chen Tu, Paishun Ting, Karthikeyan Shanmugam, and Payel Das.
2018. Explanations based on the missing: Towards contrastive explanations with pertinent negatives. In Proceedings
of the NeurIPS 2018. Curran Associates Inc., 590–601.

[88] Amit Dhurandhar, Tejaswini Pedapati, Avinash Balakrishnan, Pin-Yu Chen, Karthikeyan Shanmugam, and Ruchir

Puri. 2019. Model Agnostic Contrastive Explanations for Structured Data. http://arxiv.org/abs/1906.00117

[89] Edsger W Dijkstra. 1959. A note on two problems in connexion with graphs. Numerische Mathematik 1, 1 (1959),

269–271.

[90] Jonathan Dodge, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Casey Dugan. 2019. Explaining models:
An empirical study of how explanations impact fairness judgment. In Proceedings of IUI 2019. ACM, New York, 11.
https://doi.org/10.1145/3301275.3302310

[91] Carl Doersch. 2016. Tutorial on Variational Autoencoders. arXiv:stat.ML/1606.05908
[92] Pedro Domingos. 1998. Knowledge discovery via multiple models. Intell. Data Anal. 2, 3 (May 1998), 187–202.
[93] Ricardo Dominguez-Olmedo, Amir H. Karimi, and Bernhard Schölkopf. 2022. On the adversarial robustness of causal
algorithmic recourse. In Proceedings of the 39th International Conference on Machine Learning. PMLR, 5324–5342.
https://proceedings.mlr.press/v162/dominguez-olmedo22a.html

[94] Finale Doshi-Velez, Mason Kortz, Ryan Budish, Chris Bavitz, Sam Gershman, D. O’Brien, Stuart Schieber, J. Waldo,
D. Weinberger, and Alexandra Wood. 2017. Accountability of AI Under the Law: The Role of Explanation. https://
doi.org/10.2139/ssrn.3064761

[95] Michael Downs, Jonathan Chu, Yaniv Yacoby, Finale Doshi-Velez, and Weiwei. Pan. 2020. CRUDS: Counterfactual
recourse using disentangled subspaces. In Proceedings of the Workshop on Human Interpretability in Machine Learn-
ing (WHI’20). https://finale.seas.harvard.edu/files/finale/files/cruds-_counterfactual_recourse_using_disentangled_
subspaces.pdf

[96] Dheeru Dua and Casey Graff. 2017. UCI Machine Learning Repository - Adult Income. http://archive.ics.uci.edu/

ml/datasets/Adult

[97] Dheeru Dua and Casey Graff. 2017. UCI Machine Learning Repository - Breast Cancer. https://archive.ics.uci.edu/

ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)

[98] Dheeru Dua and Casey Graff. 2017. UCI Machine Learning Repository - Iris. https://archive.ics.uci.edu/ml/datasets/

iris

[99] Dheeru Dua and Casey Graff. 2017. UCI Machine Learning Repository - Shopping. https://archive.ics.uci.edu/ml/

datasets/Online+Shoppers+Purchasing+Intention+Dataset

[100] Dheeru Dua and Casey Graff. 2017. UCI Machine Learning Repository - Wine. https://archive.ics.uci.edu/ml/

datasets/wine

[101] Jannik Dunkelau and Michael Leuschel. 2019. Fairness-Aware Machine Learning. 60 pages. https://www.phil-fak.uni-

duesseldorf.de/fileadmin/Redaktion/Institute/Sozialwissenschaften/Kommunikations-_und_Medienwissenschaft/
KMW_I/Working_Paper/Dunkelau___Leuschel__2019__Fairness-Aware_Machine_Learning.pdf

[102] Tri Dung Duong, Qian Li, and Guandong Xu. 2021. Prototype-based Counterfactual Explanation for Causal Classifi-

cation. https://doi.org/10.48550/ARXIV.2105.00703

[103] Sanghamitra Dutta, Jason Long, Saumitra Mishra, Cecilia Tilli, and Daniele Magazzeni. 2022. Robust counterfactual
explanations for tree-based ensembles. In Proceedings of the 39th International Conference on Machine Learning. PMLR,
5742–5756. https://proceedings.mlr.press/v162/dutta22a.html

[104] Andrew Elliott, Stephen Law, and Chris Russell. 2021. Explaining classifiers using adversarial perturbations on
the perceptual ball. In Proceedings of the Conference on Computer Vision and Pattern Recognition (CVPR’21). https://
doi.org/10.48550/ARXIV.1912.09405

[105] Lukas Faber, Amin K. Moghaddam, and Roger Wattenhofer. 2020. Contrastive Graph Neural Network Explanation.

https://doi.org/10.48550/ARXIV.2010.13663

[106] Daniel Faggella. 2020. Machine Learning for Medical Diagnostics – 4 Current Applications. https://emerj.com/ai-

sector-overviews/machine-learning-medical-diagnostics-4-current-applications/. Accessed: 2020-10-15.

[107] Jake Fawkes, Robin Evans, and Dino Sejdinovic. 2022. Selection, Ignorability and Challenges with Causal Fairness.

https://doi.org/10.48550/ARXIV.2202.13774

[108] J. A. Fdez-Sánchez, J. D. Pascual-Triana, A. Fernández, and F. Herrera. 2021. Learning interpretable multi-class mod-
els by means of hierarchical decomposition: Threshold control for nested dichotomies. Neurocomputing 463 (2021),
514–524. https://doi.org/10.1016/j.neucom.2021.07.097

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 31 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:31

[109] Amir H. Feghahati, Christian R. Shelton, Michael J. Pazzani, and Kevin Tang. 2020. CDeepEx: Contrastive deep

explanations. In Proceedings of ECAI.

[110] Rubén R. Fernández, Isaac Martín de Diego, Víctor Aceña, Alberto Fernández-Isabel, and Javier M. Moguerza.
2020. Random forest explainability using counterfactual sets. Information Fusion 63 (2020), 196–207. https://doi.org/
10.1016/j.inffus.2020.07.001

[111] Carlos Fernández-Loría, Foster Provost, and Xintian Han. 2020. Explaining Data-Driven Decisions made by AI Sys-

tems: The Counterfactual Approach. http://arxiv.org/abs/2001.07417

[112] Andrea Ferrario and Michele Loi. 2020. A Series of Unfortunate Counterfactual Events: the Role of Time in Counter-

factual Explanations. https://doi.org/10.48550/ARXIV.2010.04687

[113] FICO. 2018. FICO (HELOC) Dataset. https://community.fico.com/s/explainable-machine-learning-challenge?tabset-

3158a=2

[114] Giorgos Filandrianos, Konstantinos Thomas, Edmund Dervakos, and Giorgos Stamou. 2022. Conceptual edits as
counterfactual explanations (CEUR Workshop Proceedings). CEUR-WS.org. http://ceur-ws.org/Vol-3121/paper6.pdf
[115] Maximilian Förster, Philipp Hühn, Mathias Klier, and Kilian Kluge. 2021. Capturing users’ reality: A novel approach

to generate coherent counterfactual explanations. https://doi.org/10.24251/HICSS.2021.155

[116] Maximilian Förster, Mathias Klier, Kilian Kluge, and Irina Sigler. 2020. Evaluating explainable Artifical intelligence–

What users really appreciate. (2020). https://aisel.aisnet.org/ecis2020rp/195

[117] Maximilian Becker, Nadia Burkart, Pascal Birnstill, and Jürgen Beyerer. 2021. A step towards global counterfactual
explanations: Approximating the feature space through hierarchical division and graph search. Adv. Artif. Intell.
Mach. Learn. 1, 2 (2021), 90–110.

[118] Timo Freiesleben. 2022. The intriguing relation between counterfactual explanations and adversarial examples.

Minds Mach. (Dordr.) (2022), 77–109.

[119] Jerome H. Friedman. 2001. Greedy function approximation: A gradient boosting machine. The Annals of Statistics 29,

5 (2001), 1189–1232. http://www.jstor.org/stable/2699986

[120] Jörg Frohberg and Frank Binder. 2022. CRASS: A novel data set and benchmark to test counterfactual reasoning
of large language models. In Proceedings of the Language Resources and Evaluation Conference. European Language
Resources Association, Marseille, France, 2126–2140. https://aclanthology.org/2022.lrec-1.229

[121] Takanori Fujiwara, Xinhai Wei, Jian Zhao, and Kwan-Liu Ma. 2022. Interactive dimensionality reduction for compar-
ative analysis. IEEE Transactions on Visualization and Computer Graphics (2022), 758–768. https://doi.org/10.1109/
tvcg.2021.3114807

[122] Maximilian Förster, Philipp Hühn, Mathias Klier, and Kilian Kluge. 2021. Capturing users’ reality: A novel approach

to generate coherent counterfactual explanations. https://doi.org/10.24251/HICSS.2021.155

[123] Sainyam Galhotra, Romila Pradhan, and Babak Salimi. 2021. Explaining black-box algorithms using probabilistic
contrastive counterfactuals. In : Proceedings of the International Conference on Management of Data (SIGMOD ’21),
(Virtual Event, China, June 20–25, 2021.) ACM. https://doi.org/10.1145/3448016.3458455

[124] Jingwei Gan, Shinan Zhang, Chi Zhang, and Andy Li. 2021. Automated counterfactual generation in financial model
risk management. In Proceedings of the 2021 IEEE International Conference on Big Data (Big Data). 4064–4068. https://
doi.org/10.1109/BigData52589.2021.9671561

[125] P. J. García-Laencina, J. Sancho-Gómez, and A. R. Figueiras-Vidal. 2009. Pattern classification with missing data: A

review. Neural Computing and Applications 19 (2009), 263–282.

[126] Gordon Garisch. [n. d.]. Model Lifecycle Transformation: How Banks Are Unlocking Efficiencies. https:
//financialservicesblog.accenture.com/model-lifecycle-transformation-how-banks-are-unlocking-efficiencies. Ac-
cessed: 2022-10-15.

[127] Yingqiang Ge, Shuchang Liu, Zelong Li, Shuyuan Xu, Shijie Geng, Yunqi Li, Juntao Tan, Fei Sun, and Yongfeng Zhang.

2021. Counterfactual Evaluation for Explainable AI. https://doi.org/10.48550/ARXIV.2109.01962

[128] Asma Ghandeharioun, Been Kim, Chun-Liang Li, Brendan Jou, Brian Eoff, and Rosalind Picard. 2022. DISSECT:
Disentangled simultaneous explanations via concept traversals. In Proceedings of the International Conference on
Learning Representations. https://openreview.net/forum?id=qY79G8jGsep

[129] Azin Ghazimatin, Oana Balalau, Rishiraj Saha Roy, and Gerhard Weikum. 2020. PRINCE: Provider-side interpretabil-
ity with counterfactual explanations in recommender systems (WSDM ’20). ACM, NewYork, 9. https://doi.org/
10.1145/3336191.3371824

[130] Giorgos Giannopoulos, George Papastefanatos, Dimitris Sacharidis, and Kostas Stefanidis. 2021. Interactivity, Fairness

and Explanations in Recommendations. ACM. New York. https://doi.org/10.1145/3450614.3462238

[131] Alex Goldstein, Adam Kapelner, Justin Bleich, and Emil Pitkin. 2013. Peeking inside the black box: Visualizing sta-
tistical learning with plots of individual conditional expectation. Journal of Computational and Graphical Statistics
24 (09 2013). https://doi.org/10.1080/10618600.2014.907095

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 32 -->

312:32

S. Verma et al.

[132] Oscar Gomez, Steffen Holter, Jun Yuan, and Enrico Bertini. 2020. ViCE: Visual counterfactual explanations for ma-

chine learning models. In Proceedings of IUI ’20. 5. https://doi.org/10.1145/3377325.3377536

[133] Oscar Gomez, Steffen Holter, Jun Yuan, and Enrico Bertini. 2021. AdViCE: Aggregated Visual Counterfactual Expla-

nations for Machine Learning Model Validation. https://doi.org/10.48550/ARXIV.2109.05629

[134] Bryce Goodman and S. Flaxman. 2016. EU regulations on algorithmic decision-making and a “Right to Explanation”.

ArXiv abs/1606.08813 (2016).

[135] Yash Goyal, Ziyan Wu, Jan Ernst, Dhruv Batra, Devi Parikh, and Stefan Lee. 2019. Counterfactual visual explanations.

In Proceedings of ICML 2019. PMLR, 2376–2384. https://proceedings.mlr.press/v97/goyal19a.html

[136] Preston Gralla. 2016. Amazon Prime and the Racist Algorithms. https://www.computerworld.com/article/3068622/

amazon-prime-and-the-racist-algorithms.html

[137] Rory McGrath, Luca Costabello, Chan Le Van, Paul Sweeney, Farbod Kamiab, Zhao Shen, and Freddy Lecue. 2018.
Interpretable Credit Application Predictions with Counterfactual Explanations. http://arxiv.org/abs/1811.05245
[138] Home Credit Group. 2018. Home Credit Default Risk. https://www.kaggle.com/c/home-credit-default-risk/data
[139] Riccardo Guidotti, Anna Monreale, Salvatore Ruggieri, Dino Pedreschi, Franco Turini, and Fosca Giannotti. 2018.

Local Rule-Based Explanations of Black Box Decision Systems. http://arxiv.org/abs/1805.10820

[140] Riccardo Guidotti, Anna Monreale, Salvatore Ruggieri, Franco Turini, Fosca Giannotti, and Dino Pedreschi. 2018.
A survey of methods for explaining black box models. ACM Comput. Surv. 51, 5, Article 93 (Aug. 2018), 42 pages.
https://doi.org/10.1145/3236009

[141] Riccardo Guidotti and Salvatore Ruggieri. 2021. Ensemble of counterfactual explainers. Springer-Verlag, Berlin, 11.

https://doi.org/10.1007/978-3-030-88942-528

[142] Sadaf Gulshad and Arnold Smeulders. 2021. Counterfactual attribute-based visual explanations for classification.
International Journal of Multimedia Information Retrieval (2021), 127–140. https://doi.org/10.1007/s13735-021-00208-
3

[143] Hangzhi Guo, Thanh Hong Nguyen, and Amulya Yadav. 2021. CounterNet: End-to-End Training of Counterfactual

Aware Predictions. https://doi.org/10.48550/ARXIV.2109.07557

[144] Sharmi Dev Gupta, Begum Genc, and Barry O’Sullivan. 2022. Finding Counterfactual Explanations through Con-

straint Relaxations. https://doi.org/10.48550/ARXIV.2204.03429

[145] Vivek Gupta, Pegah Nokhiz, Chitradeep Dutta Roy, and Suresh Venkatasubramanian. 2019. Equalizing Recourse

Across Groups. https://arxiv.org/abs/1909.03166

[146] Victor Guyomard, Françoise Fessant, Tassadit Bouadi, and Thomas Guyet. 2021. Post-hoc counterfactual generation

with supervised autoencoder. https://doi.org/10.1007/978-3-030-93736-210

[147] Suryabhan Singh Hada and Miguel Á. Carreira-Perpiñán. 2021. Exploring counterfactual explanations for classifi-
cation and regression trees. In Machine Learning and Principles and Practice of Knowledge Discovery in Databases.
Springer International Publishing, Cham, 489–504. https://doi.org/10.1007/978-3-030-93736-237

[148] Swastik Haldar, Philips George John, and Diptikalyan Saha. 2021. Reliable counterfactual explanations for autoen-
coder based anomalies. In Proceedings of the 8th ACM IKDD CODS and 26th COMAD. ACM. New York, 83–91.
https://doi.org/10.1145/3430984.3431015

[149] Xing Han and Joydeep Ghosh. 2021. Model-agnostic explanations using minimal forcing subsets. In Proceed-
ings of the 2021 International Joint Conference on Neural Networks (IJCNN’21). 1–8. https://doi.org/10.1109/
IJCNN52387.2021.9533992

[150] Masoud Hashemi and Ali Fathi. 2020. PermuteAttack: Counterfactual Explanation of Machine Learning Credit Score-

cards. https://doi.org/10.48550/ARXIV.2008.10138

[151] Lisa Anne Hendricks, Ronghang Hu, Trevor Darrell, and Zeynep Akata. 2018. Generating Counterfactual Explana-

tions with Natural Language. https://doi.org/10.48550/ARXIV.1806.09809

[152] Andreas Henelius, Kai Puolamäki, Henrik Boström, Lars Asker, and Panagiotis Papapetrou. 2014. A peek into the
black box: Exploring classifiers by randomization. Data Min. Knowl. Discov. 28, 5-6 (2014), 27. https://doi.org/10.1007/
s10618-014-0368-8

[153] Fabian Hinder and Barbara Hammer. 2020. Counterfactual Explanations of Concept Drift. https://doi.org/10.48550/

ARXIV.2006.12822

[154] Hans Hofmann. 1994. Statlog (German Credit Data). UCI Machine Learning Repository. https://doi.org/10.24432/

C5NC77

[155] Fred Hohman, Andrew Head, Rich Caruana, Robert DeLine, and Steven Mark Drucker. 2019. Gamut: A design probe
to understand how data scientists understand machine learning models. In Proceedings of the 2019 CHI Conference
on Human Factors in Computing Systems (2019).

[156] Woo Suk Hong, Adrian Daniel Haimovich, and R. Andrew Taylor. 2018. Predicting hospital admission at emergency
department triage using machine learning. Plos One 13, 7 (2018). https://doi.org/10.1371/journal.pone.0201016

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 33 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:33

[157] Reeber Erik Forman George Hopkins, Mark and Jaap Suermondt. 1999. Spambase. UCI Machine Learning Repository.

https://doi.org/10.24432/C53G6X

[158] The US White House. 2022. Blueprint for an AI Bill of Rights. https://www.whitehouse.gov/ostp/ai-bill-of-rights/

#discrimination

[159] Chihcheng Hsieh, Catarina Moreira, and Chun Ouyang. 2021. DiCE4EL: Interpreting process predictions using a
milestone-aware counterfactual approach. In Proceedings of the 2021 3rd International Conference on Process Mining
(ICPM’21). 88–95. https://doi.org/10.1109/ICPM53251.2021.9576881

[160] Tsung-Hao Huang, Andreas Metzger, and Klaus Pohl. 2022. Counterfactual explanations for predictive business pro-

cess monitoring. Springer International Publishing, Cham, 399–413. https://doi.org/10.1007/978-3-030-95947-028

[161] Frederik Hvilshøj, Alexandros Iosifidis, and Ira Assent. 2021. ECINN: Efficient Counterfactuals from Invertible Neural

Networks. https://doi.org/10.48550/ARXIV.2103.13701

[162] Frederik Hvilshøj, Alexandros Iosifidis, and Ira Assent. 2021. On Quantitative Evaluations of Counterfactuals. https:

//doi.org/10.48550/ARXIV.2111.00177

[163] Benedikt Höltgen, Lisa Schut, Jan M. Brauner, and Yarin Gal. 2021. DeDUCE: Generating Counterfactual Explanations

Efficiently. https://doi.org/10.48550/ARXIV.2111.15639

[164] Global Women in Data Science Conference The Global Open Source Severity of Illness Score Consortium. 2020. WiDS

Datathon 2020. https://www.kaggle.com/c/widsdatathon2020

[165] Allstate Insurance. 2011. Allstate Claim Prediction Challenge. https://www.kaggle.com/c/ClaimPredictionChallenge
[166] France Intelligence Artificielle. [n. d.]. Rapport de Synthese France Intelligence Artificielle. https://www.economie.

gouv.fr/files/files/PDF/2017/Rapport_synthese_France_IA_.pdf. Accessed: 2020-10-15.

[167] Jeremy Irvin, Pranav Rajpurkar, Michael Ko, Yifan Yu, Silviana Ciurea-Ilcus, Chris Chute, Henrik Marklund, Behzad
Haghgoo, Robyn Ball, Katie Shpanskaya, Jayne Seekins, David A. Mong, Safwan S. Halabi, Jesse K. Sandberg, Ricky
Jones, David B. Larson, Curtis P. Langlotz, Bhavik N. Patel, Matthew P. Lungren, and Andrew Y. Ng. 2019. CheX-
pert: A Large Chest Radiograph Dataset with Uncertainty Labels and Expert Comparison. https://doi.org/10.48550/
ARXIV.1901.07031

[168] Paul Jacob, Éloi Zablocki, Hédi Ben-Younes, Mickaël Chen, Patrick Pérez, and Matthieu Cord. [n. d.]. STEEX: Steering

Counterfactual Explanations with Semantics. https://doi.org/10.48550/ARXIV.2111.09094

[169] Guillaume Jeanneret, Loïc Simon, and Frédéric Jurie. 2022. Diffusion Models for Counterfactual Explanations. https://

doi.org/10.48550/ARXIV.2203.15636

[170] Lauren Kirchner Jeff Larson, Surya Mattu and Julia Angwin. 2016. UCI Machine Learning Repository. https://

github.com/propublica/compas-analysis/

[171] Yan Jia, John McDermid, and Ibrahim Habli. 2021. Enhancing the value of counterfactual explanations for deep
learning. In Artificial Intelligence in Medicine. Springer International Publishing, Cham, 389–394. https://doi.org/
10.1007/978-3-030-77211-646

[172] Alistair Johnson, Lucas Bulgarelli, Tom Pollard, Steven Horng, Leo Anthony Celi, and Roger Mark. 2021. MIMIC-IV.

https://doi.org/10.13026/S6N6-XD98

[173] Kareem L. Jordan and Tina L. Freiburger. 2015. The effect of race/ethnicity on sentencing: Examining sentence
type, jail length, and prison length. Journal of Ethnicity in Criminal Justice 13, 3 (2015). https://doi.org/10.1080/
15377938.2014.984045

[174] Shalmali Joshi, Oluwasanmi Koyejo, Warut Vijitbenjaronk, Been Kim, and Joydeep Ghosh. 2019. Towards Realis-
tic Individual Recourse and Actionable Explanations in Black-Box Decision Making Systems. http://arxiv.org/abs/
1907.09615

[175] Hong-Gyu Jung, Sin-Han Kang, Hee-Dong Kim, Dong-Ok Won, and Seong-Whan Lee. 2020. Counterfactual Expla-

nation Based on Gradual Construction for Deep Networks. https://doi.org/10.48550/ARXIV.2008.01897

[176] Vassilis Kaffes, Dimitris Sacharidis, and Giorgos Giannopoulos. 2021. Model-agnostic counterfactual explanations of

recommendations (UMAP ’21). ACM. New York, 6. https://doi.org/10.1145/3450613.3456846

[177] Kaggle. 2012. Give Me Some Credit. https://www.kaggle.com/c/GiveMeSomeCredit
[178] D. Kahneman and D. Miller. 1986. Norm theory: Comparing reality to its alternatives. Psychological Review 93 (1986),

136–153.

[179] Kentaro Kanamori, Takuya Takagi, Ken Kobayashi, and Hiroki Arimura. 2020. DACE: Distribution-aware counterfac-
tual explanation by mixed-integer linear optimization. In Proceedings of the International Joint Conference on Artificial
Intelligence (IJCAI’20). https://doi.org/10.24963/ijcai.2020/395

[180] Kentaro Kanamori, Takuya Takagi, Ken Kobayashi, and Yuichi Ike. 2022. Counterfactual explanation trees: Trans-
parent and consistent actionable recourse with decision tree . In Proceedings of Machine Learning Research (PMLR),
1846–1870.

[181] Kentaro Kanamori, Takuya Takagi, Ken Kobayashi, Yuichi Ike, Kento Uemura, and Hiroki Arimura. 2021. Ordered
counterfactual explanation by mixed-integer linear optimization. In Proceedings of the AAAI Conference on Artificial
Intelligence (2021), 11. https://doi.org/10.1609/aaai.v35i13.17376

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 34 -->

312:34

S. Verma et al.

[182] A.-H. Karimi, G. Barthe, B. Balle, and I. Valera. 2020. Model-Agnostic Counterfactual Explanations for Consequential

Decisions. http://arxiv.org/abs/1905.11190

[183] Amir-Hossein Karimi, Bernhard Schölkopf, and Isabel Valera. 2021. Algorithmic recourse: From counterfactual expla-
nations to interventions. In Proceedings of FAccT ’21. ACM, New York, 10. https://doi.org/10.1145/3442188.3445899
[184] Amir-Hossein Karimi, Julius von Kügelgen, Bernhard Schölkopf, and Isabel Valera. 2020. Algorithmic Recourse under

Imperfect Causal Knowledge: A Probabilistic Approach. http://arxiv.org/abs/2006.06831

[185] Isak Karlsson, Jonathan Rebane, Panagiotis Papapetrou, and Aristides Gionis. 2020. Locally and globally explainable

time series tweaking. Knowl. Inf. Syst. (2020), 30. https://doi.org/10.1007/s10115-019-01389-4

[186] Atoosa Kasirzadeh and Andrew Smart. 2021. The use and misuse of counterfactuals in ethical machine learning. In
Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency. ACM, New York, 9. https://
doi.org/10.1145/3442188.3445886

[187] Mark T. Keane, Eoin M. Kenny, Eoin Delaney, and Barry Smyth. 2021. If only we had better counterfactual expla-
nations: Five key deficits to rectify in the evaluation of counterfactual XAI techniques. CoRR (2021). https://arxiv.
org/abs/2103.01035

[188] Mark T. Keane and Barry Smyth. 2020. Good Counterfactuals and Where to Find Them: A Case-Based Technique for

Generating Counterfactuals for Explainable AI (XAI). arXiv:cs.AI/2005.13997

[189] Eoin Kenny and Weipeng Huang. 2023. The utility of “Even if” semifactual explanation to optimise positive outcomes.
In Advances in Neural Information Processing Systems, A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and
S. Levine (Eds.), Vol. 36. Curran Associates, Inc., 52907–52935. https://proceedings.neurips.cc/paperf iles/paper/2023/
file/a5e146ca55a2b18be41942cfa677123d-Paper-Conference.pdf

[190] Eoin M. Kenny and Mark T. Keane. 2020. On Generating Plausible Counterfactual and Semi-Factual Explanations for

Deep Learning. arXiv:2009.06399

[191] Eoin M. Kenny and Mark T Keane. 2021. On generating plausible counterfactual and semi-factual explanations for
deep learning. In Proceedings of the AAAI Conference on Artificial Intelligence 35 (May 2021), 11. https://ojs.aaai.org/
index.php/AAAI/article/view/17377

[192] Saeed Khorram and Li Fuxin. 2022. Cycle-consistent counterfactuals by latent transformations. In Proceedings of the

IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR’22). 10.

[193] Been Kim, Rajiv Khanna, and Oluwasanmi O. Koyejo. 2016. Examples are not enough, learn to criticize! criticism for
interpretability. In Advances in Neural Information Processing Systems, D. Lee, M. Sugiyama, U. Luxburg, I. Guyon,
and R. Garnett (Eds.), Vol. 29. Curran Associates, Inc. https://proceedings.neurips.cc/paperf iles/paper/2016/file/
5680522b8e2bb01943234bce7bf84534-Paper.pdf

[194] Boris Kment. 2006. Counterfactuals and explanation. Mind 115 (2006). https://doi.org/10.1093/mind/fzl261
[195] Will Knight. 2019. The Apple Card Didn’t ’See’ Gender-and That’s the Problem. https://www.wired.com/story/the-

apple-card-didnt-see-genderand-thats-the-problem/

[196] Ramaravind Kommiya Mothilal, Divyat Mahajan, Chenhao Tan, and Amit Sharma. 2021. Towards Unifying Feature

Attribution and Counterfactual Explanations: Different Means to the Same End. ACM, New York.

[197] Jaehoon Koo, Diego Klabjan, and Jean Utke. 2020. Inverse Classification with Limited Budget and Maximum Number

of Perturbed Samples. https://doi.org/10.48550/ARXIV.2009.14111

[198] Tara Koopman and Silja Renooij. 2021. Persuasive contrastive explanations for Bayesian networks. In Symbolic and
Quantitative Approaches to Reasoning with Uncertainty. Springer International Publishing, Cham, 229–242. https://
doi.org/10.1007/978-3-030-86772-0_17

[199] Anton Korikov and J. Christopher Beck. 2021. Counterfactual explanations via inverse constraint programming. In
Proceedings of the 27th International Conference on Principles and Practice of Constraint Programming (CP’21), Vol. 210.
Schloss Dagstuhl – Leibniz-Zentrum für Informatik. https://doi.org/10.4230/LIPIcs.CP.2021.35

[200] Anton Korikov, Alexander Shleyfman, and J. Christopher Beck. 2021. Counterfactual explanations for optimization-
based decisions in the context of the GDPR. In Proceedings of IJCAI-21. 4097–4103. https://doi.org/10.24963/
ijcai.2021/564

[201] Maxim Kovalev, Lev Utkin, Frank Coolen, and Andrei Konstantinov. 2021. Counterfactual explanation of machine

learning survival models. Informatica (2021), 817–847. https://doi.org/10.15388/21-INFOR468

[202] R. Krishnan, G. Sivakumar, and P. Bhattacharya. 1999. Extracting decision trees from trained neural networks. Pattern

Recognition 32, 12 (1999), 1999 – 2009. https://doi.org/10.1016/S0031-3203(98)00181-2

[203] Sanjay Krishnan and Eugene Wu. 2017. PALM: Machine learning explanations for iterative debugging. In Proceedings

of HILDA’17. ACM. New York, 6. https://doi.org/10.1145/3077257.3077271

[204] Ulrike Kuhl, André Artelt, and Barbara Hammer. 2022. Keep your friends close and your counterfactuals closer:
Improved learning from closest rather than plausible counterfactual explanations in an abstract setting. ArXiv
abs/2205.05515 (2022).

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 35 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:35

[205] Matt J. Kusner, Joshua Loftus, Chris Russell, and Ricardo Silva. 2017. Counterfactual fairness. Advances in Neural

Information Processing Systems 30 (2017).

[206] Gunnar König, Timo Freiesleben, and Moritz Grosse-Wentrup. 2021. A Causal Perspective on Meaningful and Robust

Algorithmic Recourse. https://doi.org/10.48550/ARXIV.2107.07853

[207] Jokin Labaien, Ekhi Zugasti, and Xabier De Carlos. 2021. DA-DGCEx: Ensuring Validity of Deep Guided Counterfac-
tual Explanations with Distribution-Aware Autoencoder Loss. https://doi.org/10.48550/ARXIV.2104.09062
[208] Michael T. Lash, Qihang Lin, William Nick Street, Jennifer G. Robinson, and Jeffrey W. Ohlmann. 2017. General-
ized inverse classification. In Proceedings of SDM. Society for Industrial and Applied Mathematics, Philadelphia, PA,
162–170. https://doi.org/10.1137/1.9781611974973.19

[209] Thibault Laugel, Marie-Jeanne Lesot, Christophe Marsala, and Marcin Detyniecki. 2019. Issues with Post-hoc Coun-

terfactual Explanations: A Discussion. arXiv:1906.04774

[210] Thibault Laugel, Marie-Jeanne Lesot, Christophe Marsala, Xavier Renard, and Marcin Detyniecki. 2018. Comparison-
based inverse classification for interpretability in machine learning. In Proceedings of Information Processing and
Management of Uncertainty in Knowledge-Based Systems, Theory and Foundations (IPMU’18). Springer International
Publishing. https://doi.org/10.1007/978-3-319-91473-29

[211] Thibault Laugel, Marie-Jeanne Lesot, Christophe Marsala, Xavier Renard, and Marcin Detyniecki. 2019. The Dangers

of Post-hoc Interpretability: Unjustified Counterfactual Explanations. http://arxiv.org/abs/1907.09294

[212] Thai Le, Suhang Wang, and Dongwon Lee. 2019. GRACE: Generating Concise and Informative Contrastive Sample

to Explain Neural Network Model’s Prediction. arXiv:cs.LG/1911.02042

[213] Yann LeCun and Corinna Cortes. 2010. MNIST handwritten digit database. (2010). http://yann.lecun.com/exdb/

mnist/

[214] Carson K. Leung, Adam G. M. Pazdor, and Joglas Souza. 2021. Explainable artificial intelligence for data science on
customer churn. In Proceedings of the 2021 IEEE 8th International Conference on Data Science and Advanced Analytics
(DSAA’21). 1–10. https://doi.org/10.1109/DSAA53316.2021.9564166

[215] David Lewis. 1973. Counterfactuals. Blackwell Publishers, Oxford.
[216] Dan Ley, Saumitra Mishra, and Daniele Magazzeni. 2022. Global counterfactual explanations: Investigations, im-
plementations and improvements. In Proceedings of the ICLR Workshop on Privacy, Accountability, Interpretability,
Robustness, Reasoning on Structured Data.

[217] Yan Li, Shasha Liu, Chunwei Wu, Xidong Xi, Guitao Cao, and Wenming Cao. 2021. DCFG: Discovering direc-
tional CounterFactual generation for chest X-rays. In Proceedings of BIBM 2021. 972–979. https://doi.org/10.1109/
BIBM52615.2021.9669770

[218] Shusen Liu, Bhavya Kailkhura, Donald Loveland, and Yong Han. 2019. Generative counterfactual introspection for
explainable deep learning. In Proceedings of the 2019 IEEE Global Conference on Signal and Information Processing
(GlobalSIP’19). 1–5. https://doi.org/10.1109/GlobalSIP45357.2019.8969491

[219] Ziwei Liu, Ping Luo, Xiaogang Wang, and Xiaoou Tang. 2014. Deep learning face attributes in the wild. (11 2014).

https://doi.org/10.1109/ICCV.2015.425

[220] Ana Lucic, Hinda Haned, and Maarten de Rijke. 2020. Why does my model fail? Contrastive local explanations for
retail forecasting. In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency. ACM, New
York, 9. https://doi.org/10.1145/3351095.3372824

[221] Ana Lucic, Harrie Oosterhuis, Hinda Haned, and Maarten de Rijke. 2019. FOCUS: Flexible Optimizable Counterfac-

tual Explanations for Tree Ensembles. https://doi.org/10.48550/ARXIV.1911.12199

[222] Ana Lucic, Harrie Oosterhuis, Hinda Haned, and Maarten de Rijke. 2020. Actionable Interpretability through Opti-

mizable Counterfactual Explanations for Tree Ensembles. http://arxiv.org/abs/1911.12199

[223] Ana Lucic, Maartje ter Hoeve, Gabriele Tolomei, Maarten de Rijke, and Fabrizio Silvestri. 2021. CF-GNNExplainer:

Counterfactual Explanations for Graph Neural Networks. arXiv:cs.LG/2102.03322

[224] Scott M. Lundberg and Su-In Lee. 2017. A unified approach to interpreting model predictions. In Advances in Neural

Information Processing Systems 30. Curran Associates, Inc., 4765–4774.

[225] Freddie Mac. 2019. Single Family Loan-level Dataset. https://www.freddiemac.com/research/datasets/sf-loanlevel-

dataset

[226] Nishtha Madaan, Inkit Padhi, Naveen Panwar, and Diptikalyan Saha. 2021. Generate your counterfactuals: Towards
controlled counterfactual generation for text. In Proceedings of the AAAI Conference on Artificial Intelligence 35 (May
2021), 13516–13524. https://ojs.aaai.org/index.php/AAAI/article/view/17594

[227] Fannie Mae. 2020. Fannie Mae Dataset. https://www.fanniemae.com/portal/funding-the-market/data/loan-

performance-data.html

[228] Alessandro Magrini, Stefano di Blasi, and Federico Stefanini. 2017. A conditional linear Gaussian network to assess
the impact of several agronomic settings on the quality of Tuscan Sangiovese grapes. Biometrical Letters 54 (06 2017),
25–42. https://doi.org/10.1515/bile-2017-0002

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 36 -->

312:36

S. Verma et al.

[229] Divyat Mahajan, Chenhao Tan, and Amit Sharma. 2020. Preserving Causal Constraints in Counterfactual Explana-

tions for Machine Learning Classifiers. http://arxiv.org/abs/1912.03277

[230] Guilherme F. Marchezini, Anisio M. Lacerda, Gisele L. Pappa, Wagner Meira, Jr., Debora Miranda, Marco A. Romano-
Silva, Danielle S. Costa, and Leandro Malloy Diniz. 2022. Counterfactual inference with latent variable and its applica-
tion in mental health care. Data Min. Knowl. Discov. 36 (2022), 811–840. https://doi.org/10.1007/s10618-021-00818-9
[231] David Martens and Foster J. Provost. 2014. Explaining data-driven document classifications. MIS Q. 38 (2014), 73–99.

https://doi.org/10.25300/MISQ/2014/38.1.04

[232] Raphael Mazzine, Sofie Goethals, Dieter Brughmans, and David Martens. 2021. Counterfactual explanations for em-
ployment services. In Proceedings of the International Workshop on Fair, Effective and Sustainable Talent Management
using Data Science. 1–7.

[233] Raphael Mazzine and David Martens. 2021. A Framework and Benchmarking Study for Counterfactual Generating

Methods on Tabular Data. https://doi.org/10.48550/ARXIV.2107.04680

[234] Marcos Medeiros Raimundo, Luis Nonato, and Jorge Poco. 2021. Mining Pareto-Optimal Counterfactual Antecedents

with a Branch-And-Bound Model-Agnostic Algorithm. https://doi.org/10.21203/rs.3.rs-551661/v1

[235] Md. Golam Moula Mehedi Hasan and Douglas Talbert. 2022. Data augmentation using counterfactuals: Prox-
imity vs. diversity. In The International FLAIRS Conference Proceedings 35 (May 2022). https://doi.org/10.32473/
flairs.v35i.130705

[236] Md. Golam Moula Mehedi Hasan and Douglas Talbert. 2022. Mitigating the Rashomon effect in counterfactual ex-
planation: A game-theoretic approach. In The International FLAIRS Conference Proceedings 35 (2022). https://doi.org/
10.32473/flairs.v35i.130711

[237] Silvan Mertes, Tobias Huber, Katharina Weitz, Alexander Heimerl, and Elisabeth André. 2022. GANterfactual–
counterfactual explanations for medical non-experts using generative adversarial learning. Frontiers in Artificial
Intelligence 5 (2022). https://doi.org/10.3389/frai.2022.825565

[238] Tim Miller. 2019. Explanation in artificial intelligence: Insights from the social sciences. Artificial Intelligence (2019),

1–38. https://doi.org/10.1016/j.artint.2018.07.007

[239] Saumitra Mishra, Sanghamitra Dutta, Jason Long, and Daniele Magazzeni. 2021. A Survey on the Robustness of

Feature Importance and Counterfactual Explanations. https://doi.org/10.48550/ARXIV.2111.00358

[240] Takayuki Miura, Satoshi Hasegawa, and Toshiki Shibahara. 2021. MEGEX: Data-free model extraction attack against

gradient-based explainable AI. ArXiv abs/2107.08909 (2021).

[241] Kiarash Mohammadi, Amir-Hossein Karimi, Gilles Barthe, and Isabel Valera. 2021. Scaling guarantees for near-
est counterfactual explanations. In Proceedings of the ACM Conference on AI, Ethics, and Society. ACM, New York,
177–187. https://doi.org/10.1145/3461702.3462514

[242] Wellington Rodrigo Monteiro and Gilberto Reynoso-Meza. 2022. Counterfactual generation through multi-objective

constrained optimisation. (2022), 23. https://www.researchsquare.com/article/rs-1325730/v1

[243] Sérgio Moro, Paulo Cortez, and Paulo Rita. 2014. A data-driven approach to predict the success of bank telemarketing.

Decision Support Systems 62 (2014), 22–31. https://doi.org/10.1016/j.dss.2014.03.001

[244] Ramaravind K. Mothilal, Amit Sharma, and Chenhao Tan. 2020. Explaining machine learning classifiers through
diverse counterfactual explanations. In Proceedings of the Conference on Fairness, Accountability, and Transparency
(FAccT’20) (FAT* ’20). ACM, New York, https://doi.org/10.1145/3351095.3372850

[245] Susanne G. Mueller, Michael W. Weiner, Leon J. Thal, Ronald C. Petersen, Clifford Jack, William Jagust, John Q.
Trojanowski, Arthur W. Toga, and Laurel Beckett. 2008. Alzheimer’s disease neuroimaging initiative. In Advances in
Alzheimer’s and Parkinson’s Disease. Springer US, 183–189. https://doi.org/10.1007/978-0-387-72076-018

[246] Chelsea M. Myers, Evan Freed, Luis Fernando Laris Pardo, Anushay Furqan, Sebastian Risi, and Jichen Zhu. 2020.
Revealing Neural Network Bias to Non-Experts Through Interactive Counterfactual Examples. https://doi.org/
10.48550/ARXIV.2001.02271

[247] Philip Naumann and Eirini Ntoutsi. 2021. Consequence-aware Sequential Counterfactual Generation.

arXiv:cs.LG/2104.05592

[248] Guillermo Navas-Palencia. 2021. Optimal Counterfactual Explanations for Scorecard Modelling. https://arxiv.org/

abs/2104.08619

[249] Daniel Nemirovsky, Nicolas Thiebaut, Ye Xu, and Abhishek Gupta. 2021. Providing actionable feedback in hiring
marketplaces using generative adversarial networks. In Proceedings of WSDM 2021. ACM, New York, 4. https://
doi.org/10.1145/3437963.3441705

[250] Daniel Nemirovsky, Nicolas Thiebaut, Ye Xu, and Abhishek Gupta. 2022. CounteRGAN: Generating counterfactuals
for real-time recourse and interpretability using residual GANs. In Proceedings of UAI 2022. PMLR, 1488–1497. https://
proceedings.mlr.press/v180/nemirovsky22a.html

[251] Tri Minh Nguyen, Thomas P. Quinn, Thin Nguyen, and Truyen Tran. 2021. Counterfactual Explanation with Multi-

Agent Reinforcement Learning for Drug Target Prediction. arXiv:cs.AI/2103.12983

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 37 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:37

[252] Danilo Numeroso and Davide Bacciu. 2021. MEG: Generating molecular counterfactual explanations for deep graph
networks. In 2021 International Joint Conference on Neural Networks (IJCNN). 1–8. DOI:https://doi.org/10.1109/
IJCNN52387.2021.9534266

[253] Andrew O’Brien and Edward Kim. 2021. Multi-Agent Algorithmic Recourse. https://doi.org/10.48550/

ARXIV.2110.00673

[254] House of Commons. [n. d.]. Algorithms in Decision Making. https://publications.parliament.uk/pa/cm201719/

cmselect/cmsctech/351/351.pdf. Accessed: 2020-10-15.

[255] Kwanseok Oh, Jee Seok Yoon, and Heung-Il Suk. 2020. Born Identity Network: Multi-way Counterfactual Map Gen-

eration to Explain a Classifier’s Decision. https://doi.org/10.48550/ARXIV.2011.10381

[256] Kwanseok Oh, Jee Seok Yoon, and Heung-Il Suk. 2021. Learn-Explain-Reinforce: Counterfactual Reasoning and Its
Guidance to Reinforce an Alzheimer’s Disease Diagnosis Model. https://doi.org/10.48550/ARXIV.2108.09451
[257] Matthew L. Olson, Roli Khanna, Lawrence Neal, Fuxin Li, and Weng-Keen Wong. 2021. Counterfactual state ex-
planations for reinforcement learning agents via generative deep learning. Artificial Intelligence 295 (2021), 103455.
https://doi.org/10.1016/j.artint.2021.103455

[258] Axel Parmentier and Thibaut Vidal. 2021. Optimal Counterfactual Explanations in Tree Ensembles. https://arxiv.org/

abs/2106.06631

[259] Martin Pawelczyk, Chirag Agarwal, Shalmali Joshi, Sohini Upadhyay, and Himabindu Lakkaraju. 2022. Explor-
ing counterfactual explanations through the lens of adversarial examples: A theoretical and empirical analysis. In
Proceedings of the 25th International Conference on Artificial Intelligence and Statistics. PMLR, 4574–4594. https://
proceedings.mlr.press/v151/pawelczyk22a.html

[260] Martin Pawelczyk, Sascha Bielawski, Johannes van den Heuvel, Tobias Richter, and Gjergji Kasneci. 2021.
CARLA: A Python Library to Benchmark Algorithmic Recourse and Counterfactual Explanation Algorithms.
arXiv:cs.LG/2108.00783

[261] Martin Pawelczyk, Klaus Broelemann, and Gjergji. Kasneci. 2020. On counterfactual explanations under predic-
tive multiplicity. In Proceedings of Machine Learning Research. PMLR, Virtual, 9. http://proceedings.mlr.press/v124/
pawelczyk20a.html

[262] Martin Pawelczyk, Teresa Datta, Johannes van-den Heuvel, Gjergji Kasneci, and Himabindu Lakkaraju. 2022. Prob-
abilistically Robust Recourse: Navigating the Trade-offs between Costs and Robustness in Algorithmic Recourse.
https://doi.org/10.48550/ARXIV.2203.06768

[263] Martin Pawelczyk, Klaus Broelemann, and Gjergji Kasneci. 2020. Learning model-agnostic counterfactual explana-
tions for tabular data. In Proceedings of The Web Conference. Association for Computing Machinery, New York, NY,
USA. DOI:https://doi.org/10.1145/3366423.3380087

[264] Judea Pearl. 2000. Causality: Models, Reasoning, and Inference. Cambridge University Press, Cambridge, MA, USA.
[265] Tejaswini Pedapati, Avinash Balakrishnan, Karthikeyan Shanmugan, and Amit Dhurandhar. 2020. Learning global
transparent models consistent with local contrastive explanations. In Proceedings of NeurIPS 2020. Curran Associates
Inc., 11.

[266] Oana-Iuliana Popescu, Maha Shadaydeh, and Joachim Denzler. 2021. Counterfactual Generation with Knockoffs.

https://doi.org/10.48550/ARXIV.2102.00951

[267] Rafael Poyiadzi, Kacper Sokol, Raul Santos-Rodriguez, Tijl De Bie, and Peter Flach. 2020. FACE: Feasible and Action-

able Counterfactual Explanations. https://doi.org/10.1145/3375627.3375850 arXiv: 1909.09369.

[268] Mario Alfonso Prado-Romero, Bardh Prenkaj, Giovanni Stilo, and Fosca Giannotti. 2022. A Survey on Graph Coun-

terfactual Explanations: Definitions, Methods, Evaluation. https://doi.org/10.48550/ARXIV.2210.12089

[269] Wenting Qi and Charalampos Chelmis. 2021. Improving algorithmic decision–making in the presence of untrust-
worthy training data. In Proceedings of the 2021 IEEE International Conference on Big Data (Big Data’21). 1102–1108.
https://doi.org/10.1109/BigData52589.2021.9671677

[270] Goutham Ramakrishnan, Y. C. Lee, and Aws Albarghouthi. 2020. Synthesizing action sequences for modifying model
decisions. In Proceedings of the Conference on Artificial Intelligence (AAAI’20). AAAI press, California, USA, 16. http://
arxiv.org/abs/1910.00057

[271] Yanou Ramon, David Martens, Foster Provost, and Theodoros Evgeniou. 2020. A comparison of instance-level coun-
terfactual explanation algorithms for behavioral and textual data: SEDC, LIME-C and SHAP-C. Advances in Data
Analysis and Classification 14, 4 (2020), 801–819. DOI:https://doi.org/10.1007/s11634-020-00418-3

[272] Peyman Rasouli and Ingrid Chieh Yu. 2022. CARE: Coherent actionable recourse based on sound counterfactual
explanations. International Journal of Data Science and Analytics (2022), 1–26. https://doi.org/10.1007/s41060-022-
00365-6

[273] Peyman Rasouli and Ingrid Chieh Yu. 2021. Analyzing and improving the robustness of tabular classifiers using
counterfactual explanations. In Proceedings of the 2021 20th IEEE International Conference on Machine Learning and
Applications (ICMLA’21). 1286–1293. https://doi.org/10.1109/ICMLA52953.2021.00209

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 38 -->

312:38

S. Verma et al.

[274] Shubham Rathi. 2019. Generating Counterfactual and Contrastive Explanations using SHAP. http://arxiv.org/abs/

1906.09293 arXiv: 1906.09293.

[275] Shauli Ravfogel, Grusha Prasad, Tal Linzen, and Yoav Goldberg. 2021. Counterfactual interventions reveal the causal
effect of relative clause representations on agreement prediction. In Proceedings of the 25th Conference on Computa-
tional Natural Language Learning. Association for Computational Linguistics, 194–209. https://doi.org/10.18653/v1/
2021.conll-1.15

[276] Ambareesh Ravi, Xiaozhuo Yu, Iara Santelices, Fakhri Karray, and Baris Fidan. 2021. General frameworks for anomaly
detection explainability: Comparative study. In Proceedings of the 2021 IEEE International Conference on Autonomous
Systems (ICAS’21). 1–5. https://doi.org/10.1109/ICAS49788.2021.9551129

[277] Kaivalya Rawal, Ece Kamar, and Himabindu Lakkaraju. 2021. Algorithmic Recourse in the Wild: Understanding the

Impact of Data and Model Shifts. arXiv:cs.LG/2012.11788

[278] Kaivalya Rawal and Himabindu Lakkaraju. 2020. Beyond individualized recourse: Interpretable and interactive sum-
maries of actionable recourses. In Advances in Neural Information Processing Systems, Vol. 33. Curran Associates, Inc.,
12187–12198. https://proceedings.neurips.cc/paper/2020/file/8ee7730e97c67473a424ccfeff49ab20-Paper.pdf
[279] Annabelle Redelmeier, Martin Jullum, Kjersti Aas, and Anders Løland. 2021. MCCE: Monte Carlo Sampling of Real-

istic Counterfactual Explanations. https://doi.org/10.48550/ARXIV.2111.09790

[280] Chris Reed, Keri Grieman, and Joseph Early. 2021. Non-Asimov explanations regulating AI through transparency. In

Queen Mary Law Research Paper No. 370/2021. https://ssrn.com/abstract=3970518

[281] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. 2016. “Why Should I Trust You?”: Explaining the predictions

of any classifier. In Proceedings of KDD ’16. ACM, New York, 10. https://doi.org/10.1145/2939672.2939778

[282] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. 2018. Anchors: High-precision model-agnostic explana-
tions. In Proceedings of the Conference on Artificial Intelligence (AAAI’18). AAAI Press, California, USA, 9. https://
www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16982

[283] Marcel Robeer, Floris Bex, and Ad Feelders. 2021. Generating realistic natural language counterfactuals. In Findings of
the Association for Computational Linguistics (EMNLP 2021). Association for Computational Linguistics, Punta Cana,
Dominican Republic, 3611–3625. https://doi.org/10.18653/v1/2021.findings-emnlp.306

[284] Pau Rodriguez, Massimo Caccia, Alexandre Lacoste, Lee Zamparo, Issam Laradji, Laurent Charlin, and David Vazquez.
2021. Beyond Trivial Counterfactual Explanations with Diverse Valuable Explanations. https://doi.org/10.48550/
ARXIV.2103.10226

[285] Alexis Ross, Himabindu Lakkaraju, and Osbert Bastani. 2021. Learning models for actionable recourse. In Advances in
Neural Information Processing Systems, Vol. 34. Curran Associates, Inc., 18734–18746. https://proceedings.neurips.cc/
paper/2021/file/9b82909c30456ac902e14526e63081d4-Paper.pdf

[286] David-Hillel Ruben. 1992. Counterfactuals. Routledge Publishers. https://philarchive.org/archive/RUBEE-3
[287] Chris Russell. 2019. Efficient search for diverse coherent explanations. In Proceedings of the Conference on Fairness,
Accountability, and Transparency (FAccT’19) (FAT* ’19). ACM, New York, 9. https://doi.org/10.1145/3287560.3287569
[288] Sophie Sadler, Derek Greene, and Daniel W. Archambault. 2021. A study of explainable community-level features. In

GEM: Graph Embedding and Mining (ECML-PKDD 2021 Workshop+Tutorial).

[289] Surya Shravan Kumar Sajja, Sumanta Mukherjee, Satyam Dwivedi, and Vikas C. Raykar. 2021. Semi-supervised

Counterfactual Explanations. https://openreview.net/forum?id=o6ndFLB1DST

[290] Robert-Florian Samoilescu, Arnaud Van Looveren, and Janis Klaise. 2021. Model-agnostic and Scalable Counterfac-

tual Explanations via Reinforcement Learning. https://doi.org/10.48550/ARXIV.2106.02597

[291] Pedro Sanchez and Sotirios A. Tsaftaris. 2022. Diffusion Causal Models for Counterfactual Estimation. https://doi.org/

10.48550/ARXIV.2202.10166

[292] Maximilian Schleich, Zixuan Geng, Yihong Zhang, and Dan Suciu. 2021. GeCo: Quality Counterfactual Explanations

in Real Time. arXiv:cs.LG/2101.01292

[293] Lisa Schut, Oscar Key, Rory McGrath, Luca Costabello, Bogdan Sacaleanu, Medb Corcoran, and Yarin Gal. 2021. Gen-
erating Interpretable Counterfactual Explanations By Implicit Minimisation of Epistemic and Aleatoric Uncertainties.
https://doi.org/10.48550/ARXIV.2103.08951

[294] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra. 2017. Grad-CAM: Visual explanations
from deep networks via gradient-based localization. In Proceedings of the IEEE International Conference on Computer
Vision. 618–626. https://doi.org/10.1109/ICCV.2017.74

[295] Kumba Sennaar. 2019. Machine Learning for Recruiting and Hiring – 6 Current Applications. https://emerj.com/ai-

sector-overviews/machine-learning-for-recruiting-and-hiring/. Accessed: 2020-10-15.

[296] Ruoxi Shang, K. J. Kevin Feng, and Chirag Shah. 2022. Why am I not seeing it? Understanding users’ needs for
counterfactual explanations in everyday recommendations. In Proceedings of FAccT ’22. ACM, New York, 11. https://
doi.org/10.1145/3531146.3533189

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 39 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:39

[297] Xiaoting Shao and Kristian Kersting. 2022. Gradient-based Counterfactual Explanations using Tractable Probabilistic

Models. https://doi.org/10.48550/ARXIV.2205.07774

[298] Shubham Sharma, Jette Henderson, and Joydeep Ghosh. 2019. CERTIFAI: Counterfactual Explanations for Robust-

ness, Transparency, Interpretability, and Fairness of Artificial Intelligence models. http://arxiv.org/abs/1905.07857
[299] Reza Shokri, Martin Strobel, and Yair Zick. 2021. On the privacy risks of model explanations. In Proceedings of the
2021 AAAI/ACM Conference on AI, Ethics, and Society. ACM, New York, 11. https://doi.org/10.1145/3461702.3462533
[300] Ronal Rajneshwar Singh, Paul Dourish, Piers Howe, Tim Miller, Liz Sonenberg, Eduardo Velloso, and Frank Vet-
ere. 2021. Directive Explanations for Actionable Explainability in Machine Learning Applications. https://doi.org/
10.1145/3579363

[301] Saurav Singla. 2020. Machine Learning to Predict Credit Risk in Lending Industry. https://www.aitimejournal.com/

@saurav.singla/machine-learning-to-predict-credit-risk-in-lending-industry. Accessed: 2020-10-15.

[302] Dylan Slack, Sophie Hilgard, Himabindu Lakkaraju, and Sameer Singh. 2021. Counterfactual Explanations Can Be

Manipulated. arXiv:cs.LG/2106.02666

[303] J. W. Smith, J. Everhart, W. C. Dickson, W. Knowler, and R. Johannes. 1988. Using the ADAP learning algorithm to
forecast the onset of diabetes mellitus. In Proceedings of the Annual Symposium on Computer Application in Medical
Care. American Medical Informatics Association, Washington, D.C., 261–265.

[304] Simón C. Smith and Subramanian Ramamoorthy. 2020. Counterfactual explanation and causal inference in service
of robustness in robot control. In Proceedings of the 2020 Joint IEEE 10th International Conference on Development and
Learning and Epigenetic Robotics (ICDL-EpiRob’20). 1–8. https://doi.org/10.1109/ICDL-EpiRob48136.2020.9278061

[305] Kacper Sokol and Peter Flach. 2018. Glass-Box: Explaining AI decisions with counterfactual statements through
conversation with a voice-enabled virtual assistant. In Proceedings of IJCAI’18. AAAI Press, 5868–5870. https://
doi.org/10.24963/ijcai.2018/865

[306] Kacper Sokol and Peter Flach. 2019. Desiderata for interpretability: Explaining decision tree predictions with coun-
terfactuals. In Proceedings of the Conference on Artificial Intelligence (AAAI) 33 (July 2019). https://doi.org/10.1609/
aaai.v33i01.330110035

[307] Thomas Spooner, Danial Dervovic, Jason Long, Jon Shepard, Jiahao Chen, and Daniele Magazzeni. 2021. Counterfac-

tual Explanations for Arbitrary Regression Models. https://arxiv.org/abs/2106.15212

[308] Laura State. 2021. Logic programming for XAI: A technical perspective. In Proceedings of the International Conference

on Logic Programming 2021 Workshops (ICLP’21), Vol. 2970. http://ceur-ws.org/Vol-2970/meepaper1.pdf

[309] Gregory Stein. 2021. Generating high-quality explanations for navigation in partially-revealed environments.
In Advances in Neural Information Processing Systems, Vol. 34. Curran Associates, Inc., 17493–17506. https://
proceedings.neurips.cc/paper/2021/file/926ec030f29f83ce5318754fdb631a33-Paper.pdf

[310] Deborah Sulem, Michele Donini, Muhammad Bilal Zafar, Francois-Xavier Aubet, Jan Gasthaus, Tim Januschowski,
Sanjiv Das, Krishnaram Kenthapadi, and Cedric Archambeau. 2022. Diverse Counterfactual Explanations for Anom-
aly Detection in Time Series. https://doi.org/10.48550/ARXIV.2203.11103

[311] Ezzeldin Tahoun and Andre Kassis. 2020. Beyond Explanations: Recourse via Actionable Interpretability - Extended.

https://doi.org/10.13140/RG.2.2.19076.14729

[312] Paolo Tamagnini, Josua Krause, Aritra Dasgupta, and Enrico Bertini. 2017. Interpreting black-box classifiers using
instance-level visual explanations. In Proceedings of the 2nd Workshop on Human-In-the-Loop Data Analytics. ACM,
New York, 6. https://doi.org/10.1145/3077257.3077260

[313] Juntao Tan, Shuyuan Xu, Yingqiang Ge, Yunqi Li, Xu Chen, and Yongfeng Zhang. 2021. Counterfactual explainable
recommendation. In Proceedings of the 30th ACM International Conference on Information & Knowledge Management.
ACM, New York, 10. https://doi.org/10.1145/3459637.3482420

[314] Sarah Tan, Rich Caruana, Giles Hooker, and Yin Lou. 2018. Distill-and-compare: Auditing black-box models us-
ing transparent model distillation. In Proceedings of AIES ’18. ACM, New York, 8. https://doi.org/10.1145/3278721.
3278725

[315] Jason Tashea. 2017. Courts Are Using AI to Sentence Criminals. That Must Stop Now. https://www.wired.com/2017/

04/courts-using-ai-sentence-criminals-must-stop-now/. Accessed: 2020-10-15.

[316] Mohammed Temraz and Mark T. Keane. 2021. Solving the Class Imbalance Problem Using a Counterfactual Method

for Data Augmentation. https://doi.org/10.48550/ARXIV.2111.03516

[317] Mohammed Temraz, Eoin M. Kenny, Elodie Ruelle, Laurence Shalloo, Barry Smyth, and Mark T. Keane. 2021. Han-
dling climate change using counterfactuals: Using counterfactuals in data augmentation to predict crop growth in
an uncertain climate future. In Case-Based Reasoning Research and Development. Springer International Publishing,
Cham, 216–231.

[318] T. Teofili, D. Firmani, N. Koudas, V. Martello, P. Merialdo, and D. Srivastava. 2022. Effective explanations for entity
resolution models. In Proceedings of the 2022 IEEE 38th International Conference on Data Engineering (ICDE’22). IEEE
Computer Society, Los Alamitos, CA, USA, 2709–2721. https://doi.org/10.1109/ICDE53745.2022.00248

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 40 -->

312:40

S. Verma et al.

[319] Paul Thagard. 1989. Explanatory coherence. Behavioral and Brain Sciences (1989), 435–467. https://doi.org/10.1017/

S0140525X00057046

[320] Jayaraman Thiagarajan, Vivek Sivaraman Narayanaswamy, Deepta Rajan, Jia Liang, Akshay Chaudhari, and Andreas
Spanias. 2021. Designing counterfactual generators using deep model inversion. In Advances in Neural Information
Processing Systems, Vol. 34. Curran Associates, Inc., 16873–16884. https://proceedings.neurips.cc/paper/2021/file/
8ca01ea920679a0fe3728441494041b9-Paper.pdf

[321] Erico Tjoa and Cuntai Guan. 2019. A Survey on Explainable Artificial Intelligence (XAI): Towards Medical XAI.

arXiv:cs.LG/1907.07374

[322] George Tolkachev, Stephen Mell, Stephan Zdancewic, and Osbert Bastani. 2022. Counterfactual explanations for natu-
ral language interfaces. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Vol-
ume 2: Short Papers). Association for Computational Linguistics, Dublin, Ireland, 113–118. https://aclanthology.org/
2022.acl-short.14

[323] Gabriele Tolomei, Fabrizio Silvestri, Andrew Haines, and Mounia Lalmas. 2017. Interpretable predictions of tree-
based ensembles via actionable feature tweaking. In Proceedings of the International Conference on Knowledge Discov-
ery and Data Mining (KDD’17). ACM, New York, 10. https://doi.org/10.1145/3097983.3098039

[324] Khanh Hiep Tran, Azin Ghazimatin, and Rishiraj Saha Roy. 2021. Counterfactual Explanations for Neural Recom-

menders. ACM, New York, 1627–1631. https://doi.org/10.1145/3404835.3463005

[325] Maria Tsiakmaki and Omiros Ragos. 2021. A case study of interpretable counterfactual explanations for the task of
predicting student academic performance. In Proceedings of the 2021 25th International Conference on Circuits, Systems,
Communications and Computers (CSCC’21). https://doi.org/10.1109/CSCC53858.2021.00029

[326] Stratis Tsirtsis, Abir De, and Manuel Rodriguez. 2021. Counterfactual explanations in sequential decision making
under uncertainty. In Advances in Neural Information Processing Systems, Vol. 34. Curran Associates, Inc., 30127–
30139. https://proceedings.neurips.cc/paper/2021/file/fd0a5a5e367a0955d81278062ef37429-Paper.pdf

[327] Stratis Tsirtsis and Manuel Gomez-Rodriguez. 2020. Decisions, Counterfactual Explanations and Strategic Behavior.

arXiv:cs.LG/2002.04333

[328] Ryan Turner. 2016. A model explanation system: Latest updates and extensions. ArXiv abs/1606.09517 (2016).
[329] Aalto University. [n. d.]. The European Commission Offers Significant Support to Europe’s AI Excellence. https://

www.eurekalert.org/pub_releases/2020-03/au-tec031820.php. Accessed: 2020-10-15.

[330] Sohini Upadhyay, Shalmali Joshi, and Himabindu Lakkaraju. 2021. Towards Robust and Reliable Algorithmic

Recourse. arXiv:cs.LG/2102.13620

[331] Berk Ustun, Alexander Spangher, and Yang Liu. 2019. Actionable recourse in linear classification. In Proceedings
of the Conference on Fairness, Accountability, and Transparency (FAccT’19) (FAT* ’19). ACM, New York, 10. https://
doi.org/10.1145/3287560.3287566

[332] Arnaud Van Looveren and Janis Klaise. 2020. Interpretable Counterfactual Explanations Guided by Prototypes. http:

//arxiv.org/abs/1907.02584

[333] Arnaud Van Looveren, Janis Klaise, Giovanni Vacanti, and Oliver Cobb. 2021. Conditional Generative Models for

Counterfactual Explanations. https://doi.org/10.48550/ARXIV.2101.10123

[334] Simon Vandenhende, Dhruv Mahajan, Filip Radenovic, and Deepti Ghadiyaram. 2022. Making heads or tails: To-
wards semantically consistent visual counterfactuals. In Proceedings of ECCV 2022. https://doi.org/10.1007/978-3-
031-19775-816

[335] Sahil Verma, John Dickerson, and Keegan Hines. 2020. Counterfactual Explanations for Machine Learning: A Review.

https://doi.org/10.48550/ARXIV.2010.10596

[336] Sahil Verma, John Dickerson, and Keegan Hines. 2021. Counterfactual Explanations for Machine Learning: Chal-

lenges Revisited. https://doi.org/10.48550/ARXIV.2106.07756

[337] Sahil Verma, Keegan Hines, and John P. Dickerson. 2021. Amortized Generation of Sequential Counterfactual Expla-

nations for Black-box Models. arXiv:cs.LG/2106.03962

[338] Sahil Verma and Julia Rubin. 2018. Fairness definitions explained. In Proceedings of the International Workshop on

Software Fairness (FairWare ’18). ACM, New York, 1–7. https://doi.org/10.1145/3194770.3194776

[339] Sahil Verma, Chirag Shah,

John P. Dickerson, Anurag Beniwal, Narayanan Sadagopan, and Arjun Se-
shadri. 2023. RecXplainer: Amortized Attribute-based Personalized Explanations for Recommender Systems.
arXiv:cs.IR/2211.14935

[340] Tom Vermeire, Dieter Brughmans, Sofie Goethals, Raphael Mazzine Barbossa de Oliveira, and David Martens. [n.
d.]. Explainable image classification with evidence counterfactual. Pattern Anal. Appl. ([n. d.]), 21. https://doi.org/
10.1007/s10044-021-01055-y

[341] Cédric Villani.

[n. d.].

For

a Meaningful Artificial

Intelligence. https://www.aiforhumanity.fr/pdfs/

MissionVillaniReportENG-VF.pdf. Accessed: 2020-10-15.

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 41 -->

Counterfactual Explanations and Algorithmic Recourses for Machine Learning

312:41

[342] Marco Virgolin and Saverio Fracaros. 2022. On the Robustness of Sparse Counterfactual Explanations to Adverse

Perturbations. https://doi.org/10.48550/ARXIV.2201.09051

[343] J. von Kügelgen, N. Agarwal, J. Zeitler, A. Mastouri, and B. Schölkopf. 2021. Algorithmic recourse in partially and
fully confounded settings through bounding counterfactual effects. In Proceedings of the ICML 2021 Workshop on
Algorithmic Recourse. https://sites.google.com/view/recourse21/home

[344] J. von Kügelgen, A.-H. Karimi, U. Bhatt, I. Valera, A. Weller, and B. Schölkopf. 2022. On the fairness of causal algo-
rithmic recourse. In Proceedings of the 36th AAAI Conference on Artificial Intelligence, Vol. 9. AAAI Press, Palo Alto,
CA, 9584–9594. https://doi.org/10.1609/aaai.v36i9.21192

[345] Sandra Wachter, Brent Mittelstadt, and Luciano Floridi. 2017. Why a right to explanation of automated decision-
making does not exist in the general data protection regulation. International Data Privacy Law 7, 2 (06 2017). https:
//doi.org/10.1093/idpl/ipx005

[346] Sandra Wachter, Brent Mittelstadt, and Chris Russell. 2017. Counterfactual explanations without opening the black
box: Automated decisions and the GDPR. SSRN Electronic Journal 31, 2 (2017). https://doi.org/10.2139/ssrn.3063289
[347] Pei Wang and Nuno Vasconcelos. 2020. SCOUT: Self-aware discriminant counterfactual explanations. In Proceed-
ings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR’20). https://doi.org/10.1109/
CVPR42600.2020.00900

[348] Xiaosong Wang, Yifan Peng, Le Lu, Zhiyong Lu, Mohammadhadi Bagheri, and Ronald M. Summers. 2017. ChestX-
ray8: Hospital-scale chest X-Ray database and benchmarks on weakly-supervised classification and localization of
common thorax diseases. In Proceedings of CVPR. https://doi.org/10.1007/978-3-030-13969-818

[349] Yongjie Wang, Qinxu Ding, Ke Wang, Yue Liu, Xingyu Wu, Jinglong Wang, Yong Liu, and Chunyan Miao. 2021. The
skyline of counterfactual explanations for machine learning decision models. In Proceedings of CIKM. ACM, New
York, 10. https://doi.org/10.1145/3459637.3482397

[350] Yongjie Wang, Hangwei Qian, and Chunyan Miao. 2022. DualCF: Efficient model extraction attack from counterfac-
tual explanations . In Proceedings of FAccT ’22. ACM, New York., 12. https://doi.org/10.1145/3531146.3533188
[351] Zhendong Wang, Isak Samsten, Rami Mochaourab, and Panagiotis Papapetrou. 2021. Learning time series counter-
factuals via latent space representations. In Discovery Science. Springer International Publishing, Cham, 369–384.
https://doi.org/10.1007/978-3-030-88942-529

[352] Zhendong Wang, Isak Samsten, and Panagiotis Papapetrou. 2021. Counterfactual explanations for survival prediction
of cardiovascular ICU patients. In Artificial Intelligence in Medicine. Springer International Publishing, Cham, 338–
348. https://doi.org/10.1007/978-3-030-77211-638

[353] Greta Warren, Mark T. Keane, and Ruth M. J. Byrne. 2022. Features of Explainability: How Users Understand
Counterfactual and Causal Explanations for Categorical and Continuous Features in XAI. https://doi.org/10.48550/
ARXIV.2204.10152

[354] Greta Warren, Mark T. Keane, Christophe Gueret, and Eoin Delaney. 2023. Explaining Groups of Instances Counter-
factually for XAI: A Use Case, Algorithm and User Study for Group-Counterfactuals. arXiv:cs.AI/2303.09297
[355] Geemi P. Wellawatte, Aditi Seshadri, and Andrew D. White. 2022. Model agnostic generation of counterfactual ex-

planations for molecules. Chem. Sci. 13 (2022), 3697–3705. https://doi.org/10.1039/D1SC05259D

[356] J. Wexler, M. Pushkarna, T. Bolukbasi, M. Wattenberg, F. Viégas, and J. Wilson. 2020. The What-If tool: Interactive
probing of machine learning models. IEEE Transactions on Visualization and Computer Graphics 26, 1 (2020), 56–65.
https://doi.org/10.1109/TVCG.2019.2934619

[357] Adam White and Artur d’Avila Garcez. 2019. Measurable Counterfactual Local Explanations for Any Classifier. http:

//arxiv.org/abs/1908.03020

[358] Adam White and Artur d’Avila Garcez. 2021. Counterfactual Instances Explain Little. https://doi.org/10.48550/

ARXIV.2109.09809

[359] Adam White, Kwun Ho Ngan, James Phelan, Saman Sadeghi Afgeh, Kevin Ryan, Constantino Carlos Reyes-Aldasoro,
and Artur d’Avila Garcez. 2021. Contrastive Counterfactual Visual Explanations with Overdetermination. https://
doi.org/10.48550/ARXIV.2106.14556

[360] Anjana Wijekoon, Nirmalie Wiratunga, Ikechukwu Nkisi-Orji, Kyle Martin, Chamath Palihawadana, and David Cor-
sar. 2021. Counterfactual explanations for student outcome prediction with moodle footprints. In Proceedings of the
CEUR Workshop , 1–8. https://rgu-repository.worktribe.com/output/1395861

[361] Nirmalie Wiratunga, Anjana Wijekoon, Ikechukwu Nkisi-Orji, Kyle Martin, Chamath Palihawadana, and David Cor-
sar. 2021. DisCERN: Discovering counterfactual explanations using relevance features from neighbourhoods. In Pro-
ceedings of the 2021 IEEE 33rd International Conference on Tools with Artificial Intelligence (ICTAI’21). 1466–1473.
https://doi.org/10.1109/ICTAI52525.2021.00233

[362] James Woodward. 2003. Making Things Happen: A Theory of Causal Explanation. Oxford University Press.
[363] Xintao Xiang and Artem Lenskiy. 2022. Realistic Counterfactual Explanations by Learned Relations. https://

arxiv.org/abs/2202.07356

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

---

<!-- PAGE 42 -->

312:42

S. Verma et al.

[364] Shuyuan Xu, Yunqi Li, Shuchang Liu, Zuohui Fu, Yingqiang Ge, Xu Chen, and Yongfeng Zhang. 2021. Learning causal

explanations for recommendation. CEUR Workshop Proceedings 2911 (2021), 13–25.

[365] Yaniv Yacoby, Ben Green, Christopher L. Griffin, and Finale Doshi Velez. 2022. “If it didn’t happen, why would
I Change my Decision?”: How Judges Respond to Counterfactual Explanations for the Public Safety Assessment.
https://doi.org/10.48550/ARXIV.2205.05424

[366] Prateek Yadav, Peter Hase, and Mohit Bansal. 2021. Low-Cost Algorithmic Recourse for Users with Uncertain Cost

Functions. https://doi.org/10.48550/ARXIV.2111.01235

[367] Fan Yang, Sahan Suresh Alva, Jiahao Chen, and Xia Hu. 2021. Model-based counterfactual synthesizer for interpre-

tation. In Proceedings of KDD ’21. ACM, New York, 1964–1974. https://doi.org/10.1145/3447548.3467333

[368] Fan Yang, Ninghao Liu, Mengnan Du, and Xia Hu. 2021. Generative counterfactuals for neural networks via attribute-

informed perturbation. SIGKDD Explor. Newsl. 23 (May 2021), 10. https://doi.org/10.1145/3468507.3468517
[369] Linyi Yang, Eoin Kenny, Tin Lok James Ng, Yi Yang, Barry Smyth, and Ruihai Dong. 2020. Generating plausible
counterfactual explanations for deep transformers in financial text classification. In Proceedings of ICCL. 6150–6160.
https://doi.org/10.18653/v1/2020.coling-main.541

[370] Nakyeong Yang, Taegwan Kang, and Kyomin Jung. 2022. Deriving explainable discriminative attributes using con-
fusion about counterfactual class. In Proceedings of ICASSP 2022. 1730–1734. https://doi.org/10.1109/ICASSP43922.
2022.9747693

[371] Yuanshun Yao, Chong Wang, and Hang Li. 2022. Counterfactually Evaluating Explanations in Recommender Systems.

https://doi.org/10.48550/ARXIV.2203.01310

[372] I-Cheng Yeh. 2016. Default of Credit Card Clients. UCI Machine Learning Repository. https://doi.org/10.24432/

C55S3H

[373] Roozbeh Yousefzadeh and Dianne P. O’Leary. 2019. Debugging Trained Machine Learning Models using Flip Points.

https://debug-ml-iclr2019.github.io/cameraready/DebugML-19paper11.pdf

[374] Zixuan Yuan, Yada Zhu, Wei Zhang, Ziming Huang, Guangnan Ye, and Hui Xiong. 2021. Multi-Domain Transformer-
Based Counterfactual Augmentation for Earnings Call Analysis. https://doi.org/10.48550/ARXIV.2112.00963
[375] Wencan Zhang and Brian Y Lim. 2022. Towards relatable explainable AI with the perceptual process. ACM, New

York, https://doi.org/10.1145/3491102.3501826

[376] Yuhao Zhang., Kevin McAreavey., and Weiru Liu. 2022. Developing and experimenting on approaches to explainabil-
ity in AI systems. In Proceedings of ICAART. SciTePress, 518–527. https://doi.org/10.5220/0010900300003116
[377] Yunxia Zhao. 2020. Fast Real-time Counterfactual Explanations. https://doi.org/10.48550/ARXIV.2007.05684
[378] Jinfeng Zhong and Elsa Negre. 2022. Shap-enhanced counterfactual explanations for recommendations. In Proceed-
ings of the 37th ACM/SIGAPP Symposium on Applied Computing. ACM, New York,1365–1372. https://doi.org/10.1145/
3477314.3507029

[379] B. Zhou, A. Khosla, A. Lapedriza, A. Oliva, and A. Torralba. 2016. Learning deep features for discriminative localiza-

tion. In Proceedings of CVPR. IEEE, New York, USA, 2921–2929. https://doi.org/10.1109/CVPR.2016.319

[380] Yao Zhou, Haonan Wang, Jingrui He, and Haixun Wang. 2021. From Intrinsic to Counterfactual: On the Explainability

of Contextualized Recommender Systems. https://doi.org/10.48550/ARXIV.2110.14844

[381] Alexander Zien, Nicole Krämer, Sören Sonnenburg, and Gunnar Rätsch. 2009. The feature importance ranking
measure. In Machine Learning and Knowledge Discovery in Databases, Vol. 5782. Springer Berlin, Berlin. https://
doi.org/10.1007/978-3-642-04174-7_45

Received 25 July 2023; revised 21 June 2024; accepted 5 July 2024

ACM Comput. Surv., Vol. 56, No. 12, Article 312. Publication date: October 2024.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Counterfactual Explanations and Algorithmic Recourses for
Machine Learning: A Review
SAHILVERMA,ComputerScienceandEngineering,UniversityofWashington,Seattle,UnitedStates
VARICH BOONSANONG, Computer Science and Engineering, University of Washington, Seattle,
UnitedStates
MINHHOANG,ComputerScienceandEngineering,UniversityofWashington,Seattle,UnitedStates
KEEGANHINES,ArthurAI,WashingtonDC,UnitedStates
JOHNDICKERSON,ArthurAI,WashingtonDC,UnitedStates
CHIRAGSHAH,UniversityofWashington,Seattle,UnitedStates
Machinelearningplaysaroleinmanydeployeddecisionsystems,ofteninwaysthataredifficultorimpos-
sible to understand by human stakeholders. Explaining, in a human-understandable way, the relationship
betweentheinputandoutputofmachinelearningmodelsisessentialtothedevelopmentoftrustworthy
machinelearningbasedsystems.Aburgeoningbodyofresearchseekstodefinethegoalsandmethodsof
explainabilityinmachinelearning.Inthisarticle,weseektoreviewandcategorizeresearchoncounterfactual
explanations,aspecificclassofexplanationthatprovidesalinkbetweenwhatcouldhavehappenedhadinput
toamodelbeenchangedinaparticularway.Modernapproachestocounterfactualexplainabilityinmachine
learningdrawconnectionstotheestablishedlegaldoctrineinmanycountries,makingthemappealingto
fieldedsystemsinhigh-impactareassuchasfinanceandhealthcare.Thus,wedesignarubricwithdesirable
propertiesofcounterfactualexplanationalgorithmsandcomprehensivelyevaluateallcurrentlyproposedal-
gorithmsagainstthatrubric.Ourrubricprovideseasycomparisonandcomprehensionoftheadvantagesand
disadvantagesofdifferentapproachesandservesasanintroductiontomajorresearchthemesinthisfield.
Wealsoidentifygapsanddiscusspromisingresearchdirectionsinthespaceofcounterfactualexplainability.
CCSConcepts:•Generalandreference→Surveysandoverviews;
AdditionalKeyWordsandPhrases:ExplainabilityinML,counterfactualexplanations,algorithmicrecourse,
interpretabilityinML
ACMReferenceFormat:
SahilVerma,VarichBoonsanong,MinhHoang,KeeganHines,JohnDickerson,andChiragShah.2024.Coun-
terfactualExplanationsandAlgorithmicRecoursesforMachineLearning:AReview.ACMComput.Surv.56,
12,Article312(October2024),42pages.https://doi.org/10.1145/3677119
Authors’ContactInformation:SahilVerma,ComputerScienceandEngineering,UniversityofWashington,Seattle,Wash-
ington,UnitedStates;e-mail:vsahil@cs.washington.edu;VarichBoonsanong,ComputerScienceandEngineering,Univer-
sityofWashington,Seattle,Washington,UnitedStates;e-mail:varicb@cs.washington.edu;MinhHoang,ComputerSci-
enceandEngineering,UniversityofWashington,Seattle,Washington,UnitedStates;e-mail:minh257@cs.washington.edu;
KeeganHines,ArthurAI,WashingtonDC,DistrictofColumbia,UnitedStates;e-mail:keegan.hines@gmail.com;John
Dickerson,ArthurAI,WashingtonDC,DistrictofColumbia,UnitedStates;e-mail:john@arthur.ai;ChiragShah,Univer-
sityofWashington,Seattle,Washington,UnitedStates;e-mail:chirags@uw.edu.
This work is licensed under a Creative Commons Attribution International 4.0 License.
©2024Copyrightheldbytheowner/author(s).
ACM0360-0300/2024/10-ART312
https://doi.org/10.1145/3677119
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:2 S.Vermaetal.
1 Introduction
Machine learning is increasingly accepted as an effective tool to enable large-scale automation
in many domains. In lieu of hand-designed rules, algorithms are able to learn from data to dis-
cover patterns and support decisions. Those decisions can, and do, directly or indirectly impact
humans;high-profilecasesincludeapplicationsincreditlending[301],talentsourcing[295],pa-
role[315],andmedicaltreatment[106].ThenascentFairness,Accountability,Transparency,and
Ethics (FATE) in machine learning community has emerged as a multi-disciplinary group of re-
searchersandindustrypractitionersinterestedindevelopingtechniquestodetectbiasinmachine
learningmodels,developalgorithmstocounteractthatbias,generatehuman-comprehensibleex-
planationsforthemachinedecisions,holdorganizationsresponsibleforunfairdecisions,etc.
Human-understandableexplanationsformachine-produceddecisionsareadvantageousinsev-
eralways.Forexample,focusingonausecaseofapplicantsapplyingforloans,thebenefitswould
include:
—Anexplanationcanbebeneficialtotheapplicantwhoselifeisimpactedbythedecision.For
example, it helps an applicant understand which of their attributes were strong drivers in
determiningadecision;
—Variousformsofexplanationscanserveasaproxyfortransparencyinthesystem,which
couldincreaseitstrustworthiness;
—Further, it can help an applicant challenge a decision if they feel an unfair treatment has
beenmetedout,e.g.,ifone’sracewascrucialindeterminingtheoutcome.Thiscanalsobe
usefulfororganizationstocheckforbiasintheiralgorithms;
—In some instances, an explanation provides the applicant with feedback that they can act
upontoreceivethedesiredoutcomeatafuturetime;
—Explanationscanhelpthemachinelearningmodeldevelopersidentify,detect,andfixbugs
andotherperformanceissues;
—Explanationshelpadheretolawssurroundingmachine-produceddecisions,e.g.,GDPR[68].
Explainability in machine learning is broadly about using inherently interpretable and trans-
parent models or generating post-hoc explanations for opaque models. Examples of the former
includelinear/logisticregression,decisiontrees,rulesets,andthelike.Examplesofthelatterin-
cluderandomforests,supportvectormachines(SVMs),andneuralnetworks.Post-hocexplanation
approaches can either be model-specific or model-agnostic. Explanations by feature importance
and model simplification are two broad kinds of model-specific approaches. Model-agnostic ap-
proachescanbecategorizedintovisualexplanations,localexplanations,featureimportance,and
modelsimplification.
Feature importance finds the most influential features contributing to the model’s overall ac-
curacy or for a particular decision, e.g., SHAP [224] and QII [78]. Model simplification finds an
interpretablemodelthatimitatestheopaquemodelclosely.Dependencyplotsareapopularkind
of visual explanation, e.g., Partial Dependence Plots [119], Accumulated Local Effects Plot [16],
andIndividualConditionalExpectation[131].Theyplotthechangeinthemodel’spredictionas
oneormultiplefeaturesarechanged.Localexplanationsdifferfromothermethodsbecausethey
onlyexplainasingleprediction.Localexplanationscanbefurthercategorizedintoapproximation
andexample-basedapproaches.Approximationapproachessamplenewdatapointsinthevicinity
ofthedatapointwhosepredictionfromthemodelneedstobeexplained(hereaftercalledtheex-
plaineedatapoint),andthenfitalinearmodel(e.g.,LIME[281])orextractsarulesetfromthem(e.g.,
Anchors[282]).Example-basedapproachesseektofinddatapointsinthevicinityoftheexplainee
datapoint.Theyeitherofferexplanationsintheformofdatapointsthathavethesameprediction
astheexplaineedatapointorthedatapointswhosepredictiondiffersfromtheexplaineedatapoint.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:3
Fig.1. Twopossiblepathsforadatapoint(showninblue),originallyclassifiedinthenegativeclass,tocross
thedecisionboundary.Theendpointsofboththepaths(showninredandgreen)arevalidcounterfactuals
fortheoriginalpoint.Notethattheredpathistheshortest,whereasthegreenpathadherescloselytothe
manifoldofthetrainingdata,butislonger.
Notethatthelatterkindofdatapointsarestillclosetotheexplaineedatapointandaretermedas
“counterfactualexplanations”(CFE).
Recalltheusecaseofapplicantsapplyingforaloan.Foranindividualwhoseloanrequesthas
beendenied,counterfactualexplanationsprovidethemwithactionable feedbackthatcouldhelp
them make changes to their features in order to transition to the desirable side of the decision
boundary,i.e.,gettheloan.Thisfeedbackistermedasanalgorithmicrecourse.
AnExample. SupposeAlicewalksintoabankandseeksahomemortgageloan.Thedecisionis
madebyamachinelearningclassifierthatconsidersAlice’sfeaturevectorof{Income,CreditScore,
Education, Age}. Unfortunately, Alice is denied the loan she seeks and is left wondering (1) why
the loan was denied? and (2) what can she do differently so that the loan will be approved in
thefuture?Theformerquestionmightbeansweredwithexplanationslike:“CreditScorewastoo
low”,andissimilartothemajorityoftraditionalexplainabilitymethods.Thelatterquestionforms
the basis of a counterfactual explanation: what small changes could be made to Alice’s feature
vectorinordertoendupontheothersideoftheclassifier’sdecisionboundary?Letussuppose
the bank provides Alice with exactly this advice (through a CFE) of what she might change in
order to be approved next time. A possible counterfactual recommended by the system might
be to increase her Income by $10K or get a new master’s degree or a combination of both. The
answer to the former question does not tell Alice what action to take, while the CFE explicitly
helpsher.Figure1illustrateshowthedatapointrepresentinganindividual,whichoriginallygot
classifiedinthenegativeclass,cantaketwopathstocrossthedecisionboundaryintothepositive
classregion.
Unlike several other explainability techniques, CFEs (or recourses) do not explicitly answer
“why” the model made a prediction; instead, they provide suggestions to achieve the desired
outcome. CFEs are also applicable to black-box models (when only the predict function of the
modelisaccessible),andthereforeplacenorestrictionsonmodelcomplexityanddonotrequire
model disclosure. They also do not necessarily approximate the underlying model, producing
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:4 S.Vermaetal.
accurate feedback. Owing to their intuitive nature, CFEs are also amenable to legal frameworks
(seeAppendixB).
In this work, we collect, review and categorize more than 350 recent papers that propose al-
gorithms to generate counterfactual explanations for machine learning models. Many of these
methodshavefocusedondatasetsthatareeithertabularorimage-based.Wedescribeourmethod-
ologyforcollectingpapersforthissurveyinSection2.Wedescriberecentresearchthemesinthis
fieldandcategorizethecollectedpapersamongafixedsetofdesiderataforeffectivecounterfactual
explanations(seeTable1).
Thecontributionsofthisarticleare:
(1) Weexamineasetofmorethan350recentpapersonthesamesetofparameterstoallowfor
aneasycomparisonofthetechniquesthesepapersproposeandtheassumptionstheywork
under;
(2) Thecategorizationofthepapersachievedbythisevaluationhelpsaresearcheroradeveloper
choosethemostappropriatealgorithmgiventhesetofassumptionstheyhaveandthespeed
andqualityofthegenerationtheywanttoachieve.
(3) Comprehensiveandlucidintroductionforbeginnersintheareaofcounterfactualexplana-
tionsformachinelearning.
2 Methodology
In this section, we describe our methodology for collecting and reviewing the papers used for
constructingthesurveypresentedhere.
2.1 HowDidWeCollectthePaperstoReview?
Wecollectedasetofmorethan350papers.Thissectionprovidestheexactprocedureusedtoarrive
atthissetofpapers.Forthefirstversionofthisarticle,wehadstartedfromaseedsetofpapers
recommendedbyotherpeople[229,244,270,331,346],followedbysnowballingtheirreferences.
Forthisupdated(second)versionofthepaper,wecollectedpapersthatcitedthefirstpaperthat
proposedCFEsforML,i.e.,Wachteretal.[346]andthefirstversionofthisCFEsurveypaper[335].
For an even complete search, we searched for “counterfactual explanations”, “recourse”, and
“inverseclassification”ontwopopularsearchenginesforscholarlyarticles,SemanticScholarand
Googlescholar.Welookedforpaperspublishedinthelastfiveyearsonbothsearchengines.Thisis
areasonabletimeframesincethearticlethatstartedthediscussionofcounterfactualexplanations
inthecontextofmachinelearning(specificallyfortabulardata)waspublishedin2017[346].We
collectedpapersthatwerepublishedbefore31stMay2022.Thepaperswecollectedwerepublished
atconferenceslikeKDD,IJCAI,FAccT,AAAI,WWW,NeurIPS,WHI,oruploadedtoArxiv.
2.2 ScopeoftheReview
In this work, we focus on counterfactual explanations for classifiers and targeted towards tabu-
lardatasets.Eventhoughthefirstpaperwereviewwaspublishedonlinein2017,andmostother
paperswereviewciteit[346]astheseminalpaperthatstartedthediscussionaroundcounterfac-
tualexplanations,wedonotclaimthatthisisanentirelynewidea.Communitiesfromdatamin-
ing [111, 231], causal inference [264], and even software engineering [61] have explored similar
ideastoidentifytheprincipalcauseofaprediction,aneffect,andabug,respectively.Evenbefore
theemergenceofcounterfactualexplanationsinappliedfields,theyhavebeenthetopicofdiscus-
sioninfieldslikesocialsciences[238],philosophy[194,215,286],andpsychology[49,50,178].In
this article, we restrict our discussion to recent articles that discuss counterfactual explanations
inmachinelearning,specificallyclassificationsettings.Thesearticleshavebeeninspiredbythe
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:5
emergingtrendofFATEandthelegalrequirementspertainingtoexplainabilityintasksautomated
bymachinelearningalgorithms.
3 Background
Thissectiongivesthebackgroundaboutthesocialimplicationsofmachinelearning,explainability
researchinmachinelearning,andsomepriorstudiesaboutcounterfactualexplanations.
3.1 SocialImplicationsofMachineLearning
Establishing fairness and making an automated tool’s decision explainable are two broad ways
inwhichwecanensureequitablesocialimplicationsofmachinelearning.Fairnessresearchaims
at developing algorithms that can ensure that the decisions produced by the system are not bi-
ased against a particular demographic group of individuals, which are defined with respect to
sensitive or protected features, such as race, sex, and religion. Anti-discrimination laws make it
illegaltousesensitivefeaturesasthebasisofanydecision(seeAppendixB).Biaseddecisionscan
alsoattractwidespreadcriticismandarethereforecrucialtoavoid[136,195].Fairnesshasbeen
capturedinseveralnotionsbasedonademographicgroupingorindividualcapacity.Vermaand
Rubin[338]haveenumeratedandintuitivelyexplainedmanyfairnessdefinitionsusingaunifying
dataset.DunkelauandLeuschel[101]provideanextensiveoverviewofthemajorcategorization
ofresearcheffortsinensuringfairmachinelearningandenlistsimportantworksinallcategories.
Explainablemachinelearninghasalsoseeninterestfromothercommunities,specificallyhealth-
care[321],havinghugesocialimplications.Severalworkshavesummarizedandreviewedother
researchinexplainablemachinelearning[3,56,140].
3.2 ExplainabilityinMachineLearning
This section gives some concrete examples that emphasize the importance of explainability and
givefurtherdetailsoftheresearchinthisarea.Inareal-worldexample,theUSmilitarytrained
a classifier to distinguish enemy tanks from friendly tanks. Although the classifier performed
wellonthetrainingandtestdataset,itsperformancewasabysmalonthebattlefield.Later,itwas
foundthatthephotosoffriendlytanksweretakenonsunnydays,whileforenemytanks,photos
clickedonlyonovercastdayswereavailable[140].Theclassifierfounditmucheasiertousethe
difference between the background as the distinguishing feature. In a similar case, a husky was
classifiedasawolfbecauseofthepresenceofsnowinthebackground,whichtheclassifierhad
learnedasafeatureassociatedwithwolves[281].Theuseofanexplainabilitytechniquehelped
discovertheseissues.
The explainability problem can be divided into model explanation and outcome explanation
problems[140].
Modelexplanationsearchesforaninterpretableandtransparentglobalexplanationoftheorig-
inal model. Various articles have developed techniques to explain neural networks and tree en-
semblesusingsingledecisiontree[72,92,202]andrulesets[14,85].Someapproachesaremodel-
agnostic,suchasGoldenEyeandPALM[152,203,381].
Outcomeexplanationneedstoprovideanexplanationforaspecificpredictionfromthemodel.
Thisexplanationneednotbeaglobalexplanationorexplaintheinternallogicofthemodel.Model-
specificapproachesfordeepneuralnetworks(CAM,Grad-CAM[294,379]),andmodelagnostic
approaches (LIME, MES [281, 328]) have been proposed. These are either feature attribution or
modelsimplificationmethods.Example-basedapproachesareanotherkindofexplainabilitytech-
niqueusedtoexplainaparticularoutcome[339,346].Thisworkfocusesoncounterfactualex-
planations(CFEs),whichisanexample-basedapproach.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:6 S.Vermaetal.
By definition, CFEs are applicable to supervised machine learning setups where the desired
predictionhasnotbeenobtainedforadatapoint.Themajorityofresearchinthisareahasapplied
CFEstoclassificationsettings,whichconsistsofseverallabeleddatapointsthataregivenasinput
tothemodel,andthegoalistolearnafunctionmappingfromtheinputdatapoints(with,say,m
features)tolabels.Inclassification,thelabelsarediscretevalues.Xm isusedtodenotetheinput
spaceofthefeatures,andYisusedtodenotetheoutputspaceofthelabels.Thelearnedfunction
isthemapping f :Xm →Y,whichisusedtopredictlabelsforunseendatapointsinthefuture.
3.3 HistoryofCounterfactualExplanations
Counterfactualexplanationshavealonghistoryinotherfieldslikephilosophy,psychology,and
thesocialsciences.PhilosopherslikeDavidLewispublishedarticlesontheideasofcounterfactu-
alsbackin1973[215].Woodward[362]saidthatasatisfactoryexplanationmustfollowpatterns
ofcounterfactualdependence.Psychologistshavedemonstratedthatcounterfactualselicitcausal
reasoninginhumans[49,50,178].Philosophershavealsovalidatedtheconceptofcausalthinking
duetocounterfactuals[32,362].
StudieshavecomparedthelikeabilityofCFEswithotherexplanationapproaches.Binnsetal.
[36] and Dodge etal. [90] performeduserstudiesthatshowedthatuserspreferCFEs over case-
basedreasoning[193],whichisanotherexample-basedapproach.TheworkbyFernández-Loría
etal.[111]providesthreeinterestingexampleswherethefeatureimportanceexplanationmethods
failtocapturetheunderlyingmodel,whereasCFEsdo.Asheretal.[25]arguethatthepartiality
andlocalityofCFEsmakethemepistemicallyaccessibleandanadequateformofexplanations.
4 CounterfactualExplanations
Thissectionoutlinesthemajoraspectsofcounterfactualexplanations.
4.1 DesiderataandMajorThemesofResearch
Thepreviousexamplealludestomanydesirablepropertiesofaneffectivecounterfactualexplana-
tion.ForAlice,thecounterfactualshouldquantifyarelativelysmallchange,whichwillleadtothe
desiredalternativeoutcome.Alicemightneedtoincreaseherincomeby$10Ktogetapprovedfor
aloan,andeventhoughanincreaseof$50Kwoulddothejob,itismostpragmaticforherifshecan
makethesmallestpossiblechange.Additionally,Alicemightcareaboutasimplerexplanation—it
iseasierforhertofocusonchangingafewthings(suchasonlyIncome)insteadoftryingtochange
manyfeatures.Alicecertainlyalsocaresthatthecounterfactualshereceivesisgivingheradvice,
whichisrealisticandactionable.Itwouldbeoflittleuseiftherecommendationweretodecrease
herageby10years.
Thesedesiderata,amongothers,havesetthestageforrecentdevelopmentsinthefieldofcoun-
terfactualexplainability.Aswedescribeinthissection,majorthemesofresearchhavesoughtto
incorporateincreasinglycomplexconstraintsoncounterfactuals,allinthespiritofensuringthe
resultingexplanationistrulyactionableandhelpful.Developmentinthisfieldhasfocusedonad-
dressingthesedesideratainawaythatisgeneralizableacrossalgorithmsandiscomputationally
efficient.
(1) Validity.Wachteretal.[346]firstproposedcounterfactualexplanationsin2017.Theyposed
CFEasanoptimizationproblem.Equation(1)statestheoptimizationobjective,whichisto
(cid:3)
minimizethedistancebetweenthecounterfactual(x )andtheoriginaldatapoint(x)subject
totheconstraintthattheoutputoftheclassifieronthecounterfactualisthedesiredlabel
(y (cid:3) ∈Y).Convertingtheobjectiveintoadifferentiable,unconstrainedformyieldstwoterms
(seeEquation(2)).Thefirsttermencouragestheoutputoftheclassifieronthecounterfactual
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:7
tobeclosetothedesiredclass,andthesecondtermforcesthecounterfactualtobecloseto
theoriginaldatapoint.Ametricd isusedtomeasurethedistancebetweentwodatapoints
x,x (cid:3) ∈ X, which can be the L1/L2 distance, or quadratic distance, or distance functions
whichtakeasinputtheCDFofthefeatures[331],orpairwisefeaturecostsasperceivedby
users[278].Thus,thisoriginaldefinitionalreadyemphasizedthataneffectivecounterfactual
onlyproposessmallchangesinthefeaturesrelativetothestartingpoint.
argmind(x,x (cid:3))subjectto f(x (cid:3))=y (cid:3) (1)
x(cid:3)
argminmaxλ(f(x (cid:3))−y (cid:3))2+d(x,x (cid:3)). (2)
x(cid:3) λ
A counterfactual that indeed is classified in the desired class is a valid counterfactual. As
illustratedinFigure1,thepointsshowninredandgreenarevalidcounterfactuals,asthey
are in the positive class region. The distance to the red counterfactual is smaller than the
distancetothegreencounterfactual.
(2) Actionability.Animportantconsiderationwhilemakingarecommendationisaboutwhich
featuresaremutable(e.g.,income,age)andwhicharenot(e.g.,race,countryoforigin)[331].
A recommended counterfactual should never change the immutable features. In fact, if a
changetoalegallysensitivefeatureproducesachangeinprediction,itshowsinherentbias
inthemodel.Severalarticleshavealsomentionedthatanapplicantmighthaveapreference
orderamongstthemutablefeatures(whichcanalsobehidden.)Theoptimizationproblem
is modified to take this into account. We might call the set of actionable features A, and
updateourlossfunctiontobe,
argminmaxλ(f(x (cid:3))−y (cid:3))2+d(x,x (cid:3)). (3)
x(cid:3)∈A λ
(3) Sparsity. There can be a tradeoff between the number of features changed and the total
amountofchangemadetoobtainthecounterfactual.Acounterfactualideallyshouldchange
asmallernumberoffeaturesinordertobethemosteffective.Thagard’stheoryofexplana-
tory coherence proposed that people prefer simpler and shorter explanations [319] and it
hasalsobeentestedinthecontextofexplanationsinML[238,247].Thismakessparsityan
importantconsideration.Weupdateourlossfunctiontoincludeapenaltyfunctionthaten-
couragessparsityinthedifferencebetweenthemodifiedandtheoriginaldatapoint,д(x (cid:3)−x),
e.g.,L0/L1norm:
argmin maxλ (f(x (cid:3))−y (cid:3))2+λ ∗д(x (cid:3)−x)+d(x,x (cid:3)). (4)
x(cid:3)∈A λ1,λ2 1 2
(4) DataManifoldCloseness/Plausibility.Thagard’stheoryofexplanatorycoherencestatesthat
peoplewouldfindithardtotrustanexplanationifitisinconsistentwiththeirpriorbeliefs
[319], for example if it resulted in a combination of features that were utterly unlike any
observationstheoccursintherealworld.Inthissense,thecounterfactualwouldbe“unreal-
istic",noteasytorealize,andanomaloustotherealdatapoints[44].Therefore,agenerated
counterfactualshouldberealisticinthesensethatitisnearthetrainingdataandadheres
toobservedcorrelationsamongthefeatures.Manyarticleshaveproposedvariouswaysof
quantifyingthis.Wemightupdateourlossfunctiontoincludeapenaltyforadheringtothe
datamanifolddefinedbythetrainingsetX,denotedbyl(x (cid:3) ;X):
argmin max λ (f(x (cid:3))−y (cid:3))2+λ ∗д(x (cid:3)−x)+λ ∗l(x (cid:3) ;X)+d(x,x (cid:3)). (5)
x(cid:3)∈A λ1,λ2,λ3 1 2 3
In Figure 1, the region between the dashed lines shows the data manifold. There are two
possiblepathstocrossthedecisionboundaryforthebluedatapoint.Theshorter,redpath
takesittoacounterfactualthatisoutsidethedatamanifold,whereasabitlonger,thegreen
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:8 S.Vermaetal.
Education
Age Salary
Fig.2. StructuralCausalModel(SCM)showingtheinfluenceofEducationonotherfeatureslikeAgeand
Salary.
path takes it to a counterfactual that follows the data manifold. Adding the data manifold
losstermencouragesthealgorithmtochoosethegreenpathovertheredpath,evenifitis
slightlylonger.
(5) Causality.Featuresina datasetarerarelyindependent,therefore,changing onefeaturein
therealworldaffectsotherfeatures.Forexample,gettinganeweducationaldegreeneces-
sitatesincreasingtheindividual’sagebyatleastsomeamountanditwouldlikelyresultin
anincreaseinone’ssalary.Theserelationsareusuallyrepresentedusingastructuralcausal
model(SCM)asshowninFigure2.Inordertoberealisticandactionable,acounterfactual
shouldadheretocausalrelationsbetweenfeatures.Adheringtocausalrelationcanbeincor-
poratedasalossfunctionorasahardconstraint[182,337],dependingonamethod.
Generally,ourlossfunctionnowaccountsfor(1)counterfactualvalidity;(2)sparsityinfea-
turevector(andactionabilityoffeatures);(3)similaritytothetrainingdata;and(4)causal
relations.
4.2 RelationshiptoOtherRelatedTerms
Outofthepaperscollected,differentterminologyoftencapturesthebasicideaofcounterfactual
explanations, although subtle differences exist between the terms. Several terms worth noting
include:
—AlgorithmicRecourse: Ustunet al. [331] pointoutthatcounterfactualsdo not takeinto ac-
counttheactionabilityoftheprescribedchanges,whichrecoursedoes.Workstakingacausal
view of the problem further fortify this claim [183, 184]. Recent papers in counterfactual
generation take actionability and feasibility of the prescribed changes, and therefore the
differencewithrecoursehasblurred.
—InverseClassification:Inverseclassificationaimstoperturbaninputinameaningfulwayin
ordertoclassifyitintoitsdesiredclass[4,208].Suchanapproachprescribestheactionsto
be taken in order to get the desired classification. Therefore, inverse classification has the
samegoalsasCFEs.
—ContrastiveExplanation:Contrastiveexplanationsgenerateexplanationsoftheform“anin-
putx isclassifiedasy becausefeatures f ,f ,...,f arepresentand f ,...,f areabsent”.
1 2 k n r
The features that are minimally sufficient for a classification are called pertinent positives,
andthefeatureswhoseabsenceisnecessaryforthefinalclassificationaretermedpertinent
negatives [87]. To generate both pertinent positives and pertinent negatives, one needs to
solvetheoptimizationproblemtofindtheminimumperturbationsneededtomaintainthe
sameclasslabelorchangeit,respectively.Therefore,contrastiveexplanations(specifically
pertinentnegatives)arerelatedtoCFEs.
—Adversarial Learning: Adversarial learning is closely related, but the terms are not inter-
changeable. Adversarial learning aims to generate the least amount of change in a given
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:9
inputtoclassifyitdifferently,oftenwiththegoaloffar-exceedingthedecisionboundaryand
resultinginahighlyconfidentmisclassification.Whiletheoptimizationproblemissimilarto
theoneposedinacounterfactualgeneration,thedesiderataaredifferent.Forexample,inad-
versariallearning(oftenappliedtoimages),thegoalisanimperceptiblechangeintheinput
image.ThisisoftenatoddswiththeCFE’sgoalofsparsityandparsimony(thoughsingle-
pixelattacksareanexception).Further,notionsofdatamanifoldandactionability/causality
are rarely considerations in adversarial learning. A few works point to the similarity and
synergybetweenthetwodomains:Pawelczyketal.[259]exploretheconnectionbetween
the optimization objectives and results of the adversarial and CFE generating techniques.
Freiesleben[118]statesthatthedifferencesinthedesiredclasslabelanddistancefromthe
original datapoint distinguish CFEs from adversarial examples. Elliott et al. [104] propose
generatingsemanticallymeaningfuladversarialperturbationstogenerateCFEsforimages.
BrowneandSwift[45]pointoutthattheconstraintofproducingplausibledatapointsdis-
tinguishesCFEsfromadversarialexamples.
5 AssessmentoftheApproachesonCounterfactualProperties
Foreasycomprehensionandcomparison,weidentifyseveralpropertiesthatareimportantfora
counterfactualgenerationalgorithm.Forallthecollectedpaperswhichproposeanalgorithmto
generatecounterfactualexplanations,weassessthealgorithmtheyproposeagainsttheseproper-
ties.TheresultsarepresentedinTable1.Papersthatdonotproposenewalgorithmsanddiscuss
relatedaspectsofcounterfactualexplanationsormodificationstopreviousmethodsarementioned
inSection6.3.ThemethodologyweusedtocollectthepapersisgiveninSection2.
5.1 PropertiesofCounterfactualAlgorithms
Thissectionexpoundsonthekeypropertiesofacounterfactualexplanationgenerationalgorithm.
ThepropertiesformthecolumnsofTable1.
(1) ModelAccess.Thecounterfactualgenerationalgorithmsrequiredifferentlevelsofaccessto
the underlying model for which they generate counterfactuals. We identify three distinct
access levels—access to complete model internals, access to gradients, and access to only
thepredictionfunction(black-box).Theaccesslevelrequiredforthemodeldependsonthe
optimizationtoolusedbyaCFEgeneratingapproach.
Accesstothecompletemodelinternalsisrequiredwhenthealgorithmusesasolver-based
methodlike,mixedintegerprogramming[179,182,183,287,331]oriftheyoperateonde-
cision trees [52, 110, 222, 241, 323] which requires access to all internal nodes of the tree.
Gradient-basedalgorithmstosolvetheoptimizationobjectiveareusedbyamajorityofthe
methods,usuallybymodifyingthelossfunctionproposedbyWachteretal.[346],butthis
isrestrictedtodifferentiablemodelsonly.
Black-boxapproachesusegradient-freeoptimizationalgorithmssuchasNelder-Mead[137],
growing spheres [210], FISTA [88, 332], ASP [35], or genetic algorithms [75, 208, 298] to
solve the optimization problem. Finally, some approaches do not cast the goal into an op-
timization problem and solve it using heuristics [139, 188, 274, 357]. Poyiadzi et al. [267]
proposeFACE,whichusesDijkstra’salgorithm[89]tofindtheshortestpathbetweenexist-
ingtrainingdatapointstofindcounterfactualforagiveninput.Hence,thismethoddoesnot
generatenewdatapoints.FraunhoferIOSBetal.[117]andBlanchart[39]dividethefeature
space into ‘pure’ regions where all datapoints (by sampling) belong to one class and then
usegraphtraversingtechniquestofindtheclosestCFEs.
There are several approaches can incorporate the generation of CFEs within the classifier
itself.Guoetal.[143]proposeCounterNet,anovelarchitecturethatpredictstheclassand
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

| 312:10 |     |     |     |     |     | S.Vermaetal. |     |
| ------ | --- | --- | --- | --- | --- | ------------ | --- |
Table1. AssessmentoftheCollectedArticlesontheKeyProperties,whichareImportantforReadily
ComparingandComprehendingtheDifferencesandLimitationsofDifferentCounterfactualAlgorithms
Assumptions Optimizationamortization CFattributes Featurehandlingattributes
Year Paper Model Model Amortized Multiple Sparsity Data Causal Feature Categorical
access domain Inference CFEs manifold relation actionability dist.func
| (cid:2)    |           |                |       |             |       |     | −   |
| ---------- | --------- | -------------- | ----- | ----------- | ----- | --- | --- |
| [208]      | Black-box | Agnostic       | No No | Iteratively | No No | Yes |     |
| 2017 [346] | Gradients | Differentiable | No No | L1          | No No | No  | −   |
−
| [323]   | Complete  | Treeensemble | No No | No           | No No | No  |     |
| ------- | --------- | ------------ | ----- | ------------ | ----- | --- | --- |
| ⎧⎪⎪⎪⎪⎪⎨ |           |              |       | L 0 andpost- |       |     | −   |
| [210]   | Black-box | Agnostic     | No No |              | No No | No  |     |
h oc
Flips min.
2018⎪⎪⎪⎪⎪[ [ 1 3 9] B l a c k - b o x Ag n o s t ic N o Y e s s p litnodes N o N o N o Indi cator
8 7 ] G r a d i e n t s D iff e r e n tiable N o N o L 1 Y e s N o N o −
| ⎩ [137] | Black-box | Agnostic | No No | No  | No No | No1 | −   |
| ------- | --------- | -------- | ----- | --- | ----- | --- | --- |
⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
[ 2 8 7 ] C o m p l e t e L i n e a r N o Y e s L 1 N o N o N o N . A . 2
H a r d
[ 3 3 1 ] C o m p l e t e L i n e a r N o N o N o N o Y e s −
c o n s tr a i nt
[ 2 9 8 ] B l a c k - b o x A g n o s t i c N o Y e s N o N o N o Y e s In di c a t or
[ 8 8 ] B l a c k - b o x D i ff e r e n t i a b l e N o N o L 1 Y e s N o N o −
| 2019 ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪ | o r g r a d | i e nt |     |     |     |     |     |
| -------------------- | ----------- | ------ | --- | --- | --- | --- | --- |
−
[ 2 7 4 ] B l a c k - b o x A g n o s t i c N o N o N o N o N o N o
[ 1 7 4 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o N o Y e s N o N o −
−
[ 2 7 0 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o N o N o N o N o
| ⎩ [ 3 5                            | 7 ,           |                     |         | C h a n g e s     |         |     | −   |
| ---------------------------------- | ------------- | ------------------- | ------- | ----------------- | ------- | --- | --- |
|                                    | B l a c k - b | o x A g n o s t i c | N o N o |                   | N o N o | N o |     |
| 358]                               |               |                     |         | onefeature        |         |     |     |
| ⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ |               |                     |         | L 1 a n d p o st- |         |     |     |
[ 2 4 4 ] G r a d i e n t s D i ff e r e n t i a b l e N o Y e s N o N o N o I n d i c a t o r
h o c
[ 2 6 7 ] B l a c k - b o x A g n o s t i c N o N o N o Y e s 3 N o N o −
B l a c k - b o x
[ 3 3 2 ] D i ff e r e n t i a b l e N o N o L 1 Y e s N o N o E m b e d d in g
or g r a d i e nt
[ 2 2 9 ] G r a d i e n t s D i ff e r e n t i a b l e Y e s Y e s N o Y e s Y e s Y e s −
H a r d
[ 1 8 2 ] C o m p l e t e L i n e a r N o Y e s c o n s t ra in t N o N o Y e s I n d i c a t o r
[ 2 6 3 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o N o Y e s N o Y e s N . A . 4
[ 1 8 8 ] B l a c k - b o x A g n o s t i c N o N o Y e s Y e s N o N o −
2020⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪
[ 1 8 3 ] C o m p l e t e L i n e a r a n d N o N o L 1 N o Y e s Y e s −
|     |     | c a u s a l g r a p h |     |     |     |     |     |
| --- | --- | --------------------- | --- | --- | --- | --- | --- |
−
[ 1 8 4 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o N o N o Y e s Y e s
[ 2 1 2 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o It e ratively Y e s N o N o 5 −
[ 7 5 ] Bl a c k - b o x A g n o s t ic N o Y e s L 0 Y e s N o Y e s Indi cator
|        |               | L i n e a r a n d       |           |     |           |       |     |
| ------ | ------------- | ----------------------- | --------- | --- | --------- | ----- | --- |
| [ 1 7  | 9 ] C o m p l | e t e                   | N o N o   | N o | Y e s N o | Y e s | −   |
|        |               | t r e e e n s e m b l e |           |     |           |       |     |
|        |               | R a n d o m             |           |     |           |       | −   |
| [ 1 1  | 0 ] C o m p l | e t e                   | N o Y e s | L 1 | N o N o   | N o   |     |
|        |               | F o r e s t             |           |     |           |       |     |
| ⎩[221, |               |                         |           |     |           |       | −   |
|        | Complete      | Treeensemble            | No No     | L1  | No No     | No    |     |
222]
Papersaresortedchronologically.DetailsaboutthefulltableisgiveninAppendixA.
generatestheCFEofadatapointwhentrainedfromscratch.ShaoandKersting[297]train
asum-productnetworkthatactsasbothaclassifieranddensityestimatorandusesthatto
generateCFEs.Rossetal.[285]proposeaddinganadversariallossduringtrainingoftheML
modeltohaveahigherprobabilityofhavingarecourseforthetrainingdatapoints.(After
training,anyCFEgeneratingmethodcanbeused.)
(2) ModelAgnostic.Thiscolumndescribesthedomainofmodelsagivenalgorithmcanoperate
on.Forexample,gradient-basedalgorithmscanonlyhandledifferentiablemodels,andtheal-
gorithmsbasedonsolversrequirelinearorpiece-wiselinearmodels[179,182,183,287,331],
some algorithms are model-specific and only work for those models like tree ensem-
bles [110, 179, 222, 323]. Black-box methods have no restriction on the underlying model
andare,therefore,model-agnostic.
1Itconsidersglobalandlocalfeatureimportance,notpreference.
2Allfeaturesareconvertedtopolytopetype.
3Doesnotgeneratenewdatapoints.
4Thedistanceiscalculatedinlatentspace.
5Itconsidersfeatureimportancenotuserpreference.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:11
(3) Optimization Amortization. Among the collected papers, the proposed algorithm mostly
returned a single counterfactual for a given input datapoint. Therefore, these algorithms
require solving an optimization problem to generate each counterfactual for every input
datapoint.Asmallernumberofthemethodsareabletogeneratemultiplecounterfactuals
(generallydiversebysomemetricofdiversity)forasingleinputdatapoint;therefore,they
require to be run once per input to get several counterfactuals [52, 75, 110, 139, 182, 229,
244, 287, 298]. Dandl et al. [75] propose a genetic algorithm to generate multiple CFEs of
a datapoint at once. Mahajan et al. [229]’s approach learns the mapping of datapoints to
counterfactualsusingavariationalauto-encoder(VAE)[91].Therefore,oncetheVAEis
trained, it can generate multiple counterfactuals for all input datapoints, without solving
theoptimizationproblemseparatelyandisthusveryfast.Vermaetal.[337]andSamoilescu
etal.[290]trainareinforcementlearningmodeltolearntheactionsthatneedtobetakento
generateCFEsforadatadistribution.Hence,theseapproachesarealsoamortized.Yangetal.
[367]trainaCGANtosynthesizeCFEswithumbrellasampling;hence,theirapproachisalso
amortized.VanLooverenetal.[333]alsotrainaGAN-basedmodelthatisamortized.Schleich
etal.[292]partiallyevaluate(amortize)theclassifierforthestaticfeatures,hencespeeding
uptheCFEgeneration.Wereporttwoaspectsofoptimizationamortizationinthetable:
• AmortizedInference:ThiscolumnismarkedYesifthealgorithmcangeneratecounterfac-
tualsformultipleinputdatapointswithoutoptimizingseparatelyforthem;otherwise,it
ismarkedNo.
• Multiple Counterfactuals (CF): This column is marked Yes if the algorithm can generate
multiplecounterfactualsforasingleinputdatapoint;otherwise,itismarkedNo.
(4) Counterfactual (CF) Attributes. These columns evaluate algorithms on sparsity, data
manifoldadherence,andcausality.
(a) Sparsity: Among the collected articles, methods using solvers explicitly constrain spar-
sity[182,331],black-boxmethodsconstrainL0normofcounterfactualandtheinputdat-
apoint[75,210].Gradient-basedmethodstypicallyusetheL1normofcounterfactualand
theinputdatapoint.Someofthemethodschangeonlyafixednumberoffeatures[188,357],
changefeaturesiteratively[175,212,293,337],orfliptheminimumpossiblesplitnodesin
thedecisiontree[139]toinducesparsity.Somemethodsalsoinducesparsitypost-hoc[210,
244].Thisisdonebysortingthefeaturesinascendingorderofrelativechangeandgreed-
ilyrestoringtheirvaluestomatchthevaluesintheinputdatapointuntilthepredictionfor
theCFEisstilldifferentfromtheinputdatapoint.Sparsity columninthetableismarked
Noifthealgorithmdoesnotconsidersparsity,elseitspecifiesthesparsityconstraint.
(b) Data Manifold Adherence: Adherence to the data manifold has been addressed using
severaldifferentapproaches,liketrainingVAEsonthedatadistribution[87,174,229,332],
constraining the distance of a counterfactualfrom thek nearest training datapoints[75,
102,179],directlysamplingpointsfromthelatentspaceofaVAEtrainedonthedata,and
thenpassingthepointsthroughthedecoder[263],usinganensembleofmodelstocapture
the predictive entropy [293], using a kernel density estimator (KDE) to estimate the
PDFoftheunderlyingdatamanifold[122],usingthecycleconsistencylossinGAN[333],
mappingbacktothedatadomain[212],usingacombinationofexistingdatapoints[188],
usingGaussianmixturemodelstoapproximatetheprobabilityofin-distributionness[19],
orbyusingfeaturecorrelations[20],orbysimplynotgeneratinganynewdatapoint[267].
Data manifold column in the table is marked Yes if the algorithm forces the generated
CFEstobeclosetothedatamanifoldbysomemechanism;otherwise,itismarkedNo.
(c) Causality: The relation between different features is represented by a directed graph
between them, which is termed as a causal graph [264]. Out of the papers that have
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:12 S.Vermaetal.
addressed this concern, most require access to the complete causal graph [183, 184]
(which is rarely available in the real world), while Duong et al. [102], Mahajan et al.
[229],Vermaetal.[337],andYangetal.[367]canworkwithpartialcausalgraphs.Causal
relationcolumninthetableismarkedYesifthealgorithmconsidersthecausalrelations
betweenfeatureswhengeneratingCFEs;otherwise,itismarkedNo.
(5) Feature Handling Attributes. Out of the articles that consider feature actionability, most
classify the features into immutable and mutable types. Karimi et al. [183] and Lash et al.
[208] categorize the features into immutable, mutable, and actionable types. Actionable
featuresareasubsetofmutablefeatures.Theypointoutthatcertainfeaturesaremutable
butnotdirectlyactionablebytheindividual,e.g.,CreditScorecannotbedirectlychanged;it
changesasaneffectofchangesinotherfeatureslikeincomeandcreditamount.Mahajan
et al. [229] uses an oracle to learn the user preferences for changing features (among
mutablefeatures)andcanalsolearnhiddenpreferences.
Mosttabulardatasetshavebothcontinuousandcategoricalfeatures.Performingarithmetic
over continuous features is natural, but handling categorical variables in gradient-based
algorithms can be complicated. Some algorithms cannot handle categorical variables and
filterthemout[210,222].Wachteretal.[346]proposedclampingallcategoricalfeaturesto
eachoftheirvalues,thusspawningmanyprocesses(oneforeachvalueofeachcategorical
feature), leading to scalability issues. Some approaches convert categorical features to
one-hot encoding and then treat them as numerical features. In this case, maintaining
one-hotness can be challenging. Some use a different distance function for categorical
features, which is generally an indicator function (1 if a different value, else 0). [122] use
Markov chain transitions to encode categorical distances. Yang et al. [367] use Gaussian
mixturemodelstonormalizethecontinuousfeaturesandGumbel-Softmaxtorelaxcategor-
ical features into continuous ones. Genetic algorithms, evolutionary algorithms, and SMT
solverscannaturallyhandlecategoricalfeatures.Wereportthesepropertiesinthetable.
• Feature Actionability: This column is marked Yes if the algorithm considers feature
actionability,otherwisemarkedNo.
• Categorical Distance Function: This column is marked—if the algorithm does not use a
separatedistancefunctionforcategoricalvariables,elseitspecifiesthedistancefunction.
6 EvaluationofCounterfactualGenerationAlgorithms
Thissectionliststhecommondatasetsusedtoevaluatecounterfactualgenerationalgorithmsand
themetricsonwhichtheyaretypicallyevaluatedandcompared.
6.1 CommonlyUsedDatasetsforEvaluation
Thedatasetsusedintheevaluationinthearticleswereviewcanbecategorizedintotabularand
imagedatasets.Notallmethodssupportimagedatasets.Someofthearticlesalsousedsynthetic
datasetsforevaluatingtheiralgorithms,butweskipthoseinthisreviewsincetheyweregenerated
foraspecificarticleandalsomightnotbeavailable.Commondatasetsintheliteratureinclude:
—Tabular:Adultincome[33],Germancredit[154],StudentPerformance[71],Breastcancer
[97],Defaultofcredit[372],Shopping[99],Iris[98],Wine[100],Spambase[157],Covertype
[38],ICU[96],LendingClub[314],GiveMeSomeCredit[177],COMPAS[170],LSAT[40],
Pima diabetes [303], HELOC/FICO [113], Fannie Mae [227], Portuguese Bank [243], San-
giovese [228], Bail dataset [173], Simple-BN [229], AllState [165], WiDS Datathon [164],
Home Credit Default Risk [138], German Housing [115], HospitalTriage [156], MIMIC-
IV [172], Freddie Mac [225], UK unsecured personal loans [47], insurance dataset [197],
BPIC2017[160].
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:13
Table2. ContinuedfromTable1
Assumptions Optimizationamortization CFattributes Featurehandlingattributes
Model Model Amortized Multiple Data Causal Feature Categorical
Year Paper Sparsity
access domain Inference CFEs manifold relation actionability dist.func
⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
1
[
[
[
[
[
[
[
[
[
[
1
2
2
4
1
2
2
2
5
3
4
8
9
4
6
0
4
0
9
2
3
7
1
3
7
2
8
2
]
]
,
3
]
]
]
]
]
]
]
]
C
G
B
B
C
B
o
c
B
C
C
G
o
r
l
l
l
l
o
o
o
o
r
r
a
a
a
a
m
a
a
m
m
m
m
c
c
c
c
d
d
p
k
k
k
k
p
p
p
p
i
i
l
-
-
-
-
e
e
l
l
l
l
e
b
b
b
b
e
e
e
e
n
n
t
o
o
o
o
t
t
t
t
e
t
t
e
e
e
e
x
x
x
x
s
A
b
D
L
A
A
L
A
L
D
D
l
i
i
i
g
g
g
g
i
i
e
a
n
n
n
ff
ff
c
n
n
n
n
c
e
e
e
e
e
i
k
o
o
o
o
a
a
a
s
r
r
-
s
s
s
s
i
r
r
r
e
e
b
o
t
t
t
t
n
n
i
i
i
i
o
n
c
c
c
c
t
t
x
i
i
T
a
a
r
b
b
e
l
l
e
e
e
if
Y
N
N
N
N
N
N
N
N
N
e
o
o
o
o
o
o
o
o
o
s
Y
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
e
o
o
o
o
o
s
s
s
s
s H
c
L
I
L
G
N
N
I
Y
L
t
t
o
e
0
1
1
e
e
o
o
o
a
n
s
/
r
r
w
r
L
a
a
s
d
1
t
t
t
e
r
i
i
r
v
v
a
e
e
in
l
l
y
y
t
N
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
o
o
o
o
o
o
s
s
s
s
6
Y
Y
Y
Y
N
N
N
N
N
N
e
e
e
e
o
o
o
o
o
o
s
s
s
s
Y
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
e
o
o
o
o
o
s
s
s
s
s
La
I
I
t
n
n
G
e
d
d
n
o
i
i
−
−
−
−
−
−
t
c
c
w
a
a
s
e
t
t
p
o
o
r
a
r
r
ce
2021⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪
⎩
[
[
[
[
[
[
[
[
[
[
[
2
2
1
3
1
1
2
3
2
3
2
5
4
1
6
7
2
7
9
9
3
5
8
1
7
7
5
2
9
0
7
]
0
]
]
]
]
]
]
]
]
]
]
C
C
B
B
G
B
B
B
B
C
B
or
l
l
l
l
l
l
l
o
o
o
r
a
a
a
a
a
a
a
a
g
m
m
m
c
c
c
c
c
c
c
d
r
k
k
k
k
k
k
k
p
p
p
a
i
-
-
-
-
-
-
-
e
d
l
l
l
b
b
b
b
b
b
b
e
e
e
n
i
o
o
o
o
o
o
o
t
t
t
e
t
e
e
e
x
x
x
x
x
x
x
nt
A
D
A
b
T
L
A
A
A
A
A
T
l
i
r
r
g
g
g
g
g
g
g
i
a
n
e
e
ff
n
n
n
n
n
n
n
c
e
e
e
e
k
o
o
o
o
o
o
o
a
r
e
e
-
s
s
s
s
s
s
s
r
e
b
n
n
t
t
t
t
t
t
t
n
i
i
i
i
i
i
i
o
s
s
c
c
c
c
c
c
c
t
e
e
x
i
m
m
ab
b
b
le
l
l
i
e
e
f
Par
Y
Y
Y
Y
Y
Y
N
N
N
N
t
e
e
e
e
e
e
i
o
o
o
o
a
s
s
s
s
s
s
lly Y
Y
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
e
e
o
o
o
o
o
s
s
s
s
s
s
H
c
H
s
L
N
L
N
N
L
L
I
Y
t
t
o
e
1
1
0
0
e
o
o
o
r
a
a
n
s
/
/
r
a
r
r
L
L
a
s
i
d
d
n
1
1
t
t
r
i
t
v
a
c
e
i
o
n
l
n
y
t
-
Y
Y
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
e
e
o
o
o
o
o
s
s
s
s
s
s
Y
Y
N
N
N
N
N
N
N
N
N
e
e
o
o
o
o
o
o
o
o
o
s
s
Y
Y
Y
Y
Y
Y
Y
N
N
N
N
e
e
e
e
e
e
e
o
o
o
o
s
s
s
s
s
s
s
I
I
N
M
n
n
C
G
G
o
d
d
h
a
o
o
t
i
i
−
−
−
−
−
r
a
c
c
w
w
s
k
a
a
i
u
n
e
e
o
t
t
r
o
o
r
r
s
v
e
r
r
Training
⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ [
[
1
3
4
6
3
3
]
]
f
s
G
r
c
o
r
r
a
m
a
d
tc
ie
h
nt
D
D
i
i
ff
ff
e
e
r
r
e
e
n
n
t
t
i
i
a
a
b
b
l
l
e
e
Y
N
e
o
s N
N
o
o
N
N
o
o Y
N
e
o
s Y
N
e
o
s
N
N
o
o
−
−
2022⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪ [
[
[
3
2
2
6
7
9
6
8
7
]
]
]
T
f
B
B
r
r
l
l
o
a
a
a
m
c
c
in
k
k
i
-
-
n
b
b
g
o
o
x
x
D
A
A
g
g
iff
n
n
e
o
o
r
s
s
e
t
t
n
i
i
c
c
tiable
Y
N
N
e
o
o
s M
M
N
i
i
g
g
o
h
h
t
t
N
Y
Y
e
e
o
s
s
Y
N
N
e
o
o
s N
N
N
o
o
o
Y
Y
Y
e
e
e
s
s
s
Indi
−
−
cator
⎩
scratch
—Image:MNIST[213],EMNIST[66],CelebA[219],CheXpert[167],ImageNet[86],ISICSkin
Lesion[65],ADNI[245],ChestX-ray8[348].
6.2 MetricsforEvaluationofCounterfactualGenerationAlgorithms
Counterfactualsareconsideredasactionablefeedbacktoindividualswhohavereceivedundesir-
ableoutcomesfromautomateddecision-makers,andthereforeanidealevaluationwouldconsist
ofauser-study.However,userstudiesareexpensiveandthereforetheliteratureproposestouse
proxymetricstoevaluatetheeaseofactingonarecommendedcounterfactual:
(1) Validity: Validity measures the ratio of the counterfactuals that actually have the desired
class label to the total number of counterfactuals generated. Higher validity is preferable.
Mostpapersreportit.
(2) Proximity:Proximitymeasuresthedistanceofacounterfactualfromtheinputdatapoint.For
counterfactualstobeeasytoactupon,theyshouldbeclosetotheinputdatapoint.Distance
metricsliketheL1norm,L2norm,andMahalanobisdistancearecommon.Tohandlethevari-
abilityofrangeamongdifferentfeatures,somearticlesstandardizetheminpre-processing
ordivideL1normbymedianabsolutedeviationofrespectivefeatures[244,287,346],ordi-
videL1normbytherangeoftherespectivefeatures[75,182,183].Proximityforcategorical
6Maybepartiallyasitusescycleconsistencyloss.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:14 S.Vermaetal.
featuresistreatedasbinary(oneorzerodependingofwhetherthevaluechangedornot).
Somearticlestermproximityastheaveragedistanceofthegeneratedcounterfactualsfrom
theinput.Lowervaluesofaveragedistancearepreferable.
(3) Number of Features Changed: Shorter explanations are more comprehensible to humans
[238],therefore,counterfactualsideallyshouldprescribeachangeinasmallnumberoffea-
tures.Althoughaconsensusonahardcaponthenumberofmodifiedfeatureshasnotbeen
reached,KeaneandSmyth[188]capasparsecounterfactualtoatmosttwofeaturechanges.
(4) Counterfactual generation time: Intuitively, this measures the time required to generate
counterfactuals.Thismetriccanbeaveragedoverthegenerationofacounterfactualfora
batchofinputdatapointsorforthegenerationofmultiplecounterfactualsforasingleinput
datapoint.
(5) Diversity:Somealgorithmssupportthegenerationofmultiplecounterfactualsforasingle
input datapoint. The purposeof providing multiple counterfactuals is to increase the ease
forapplicantstoreachatleastonecounterfactualstate.Therefore,therecommendedcoun-
terfactualsshouldbediverse,allowingapplicantstochoosetheeasiestone.Ifanalgorithm
isstronglyenforcingsparsity,therecouldbemanydifferentsparsesubsetsofthefeatures
thatcouldbechanged.Therefore,havingadiversesetofcounterfactualsisuseful.Diversity
isencouragedbymaximizingthedistancebetweenthemultiplecounterfactualsbyadding
it as a term in the optimization objective [75, 244] or as a hard constraint [182, 241, 331],
or by minimizing the mutual information between all pairs of modified features [212].
Mothilal et al. [244] reported diversity as the feature-wise distance between each pair of
counterfactuals.Ahighervalueofdiversityispreferable.
(6) Closeness to the Training Data/Plausibility: Recent articles have considered the action-
ability and realisticness of the modified features by grounding them in the training data
distribution. This has been captured by measuring the average distance to the k-nearest
datapoints[75],ormeasuringthelocaloutlierfactor[179],ormeasuringthereconstruction
error from a VAE trained on the training data [229, 332], or measuring the PDF of such
datapoints using KDE [122], or measuring the maximum mean discrepancy (MMD)
between the original and counterfactual points [333]. A lower value of the distance and
reconstructionerrorispreferable.
(7) Causal Constraint Satisfaction (Feasibility): This metric captures how realistic the modifi-
cations in the counterfactual are by measuring if they satisfy the causal relation between
features.Mahajanetal.[229]evaluatedtheiralgorithmonthismetric.
OtherMetrics. Herewedescribethelesscommonlyusedmetrics:
(1) IM1andIM2:VanLooverenandKlaise[332]proposedtwointerpretabilitymetricsspecifi-
callyforalgorithmsthatuseauto-encoders.Letthecounterfactualclassbet,andtheoriginal
class beo.AE is the auto-encoder trained on training instances of classt, andAE is the
t o
auto-encodertrainedontraininginstancesofclasso.LetAEbetheauto-encodertrainedon
thefulltrainingdataset(allclasses):
(cid:6)x −AE (x )(cid:6)2
IM1= cf t cf 2 (6)
(cid:6)x −AE (x )(cid:6)2+ϵ
cf o cf 2
(cid:6)AE (x )−AE(x )(cid:6)2
IM2= t (cid:7) (cid:7) c x f (cid:7) (cid:7) +ϵ cf 2 (7)
cf 1
A lower value of IM1 implies that the counterfactual (x ) can be better reconstructed by
cf
the auto-encoder trained on the counterfactual class (AE ) compared to the auto-encoder
t
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:15
trainedontheoriginalclass(AE ),thusimplyingthatthecounterfactualisclosertothedata
o
manifoldofthecounterfactualclass.AlowervalueofIM2 impliesthatthereconstruction
fromtheauto-encodertrainedonthecounterfactualclassandtheauto-encodertrainedon
all classes is similar. Therefore, a lower value of IM1 and IM2 means a more interpretable
counterfactual, where interpretability refers to a plausible datapoint which is supposedly
moreinterpretable.
(2) LabelVariationScoreandOracleScore:Hvilshøjetal.[162]pointoutthatthepreviousmet-
ricsareunabletodetectout-of-distributionCFEs(especiallyforhigh-dimensionaldatasets)
andproposetwonewmetrics.LabelVariationScoreapplieswheneachdatapointhasmulti-
plelabels,andtheintuitionisthatCFEforaparticularlabelshouldnotaffectthepredictions
forotherlabels(unlesstheyarehighlycorrelated).Thisassumesthecaseofmultilabelclas-
sification,whereadatapointwithoriginalpredictionAisbeingcounterfactuallypredicted
asB.LVSstatesthatthepredictionprobabilitiesforclassesapartfromAandBshouldnot
change
(cid:8)
LVS = d [p (x),p (CFE(x))], (8)
div l l
l∈L
whereListhetotalnumberoflabelsforadatapointandp isthepredictedprobabilityfor
l
thespecificlabell,andd measuresthedivergencebetweenthepredictedprobabilityof
div
labell fortheoriginaldatapointx anditsCFE.
OracleScoreissimilartovalidity,however,withanadditionalclassifiertrainedonthesame
dataset as the original classifier. The intuition is that if a CFE is more like an adversarial
example for a classifier, the CFE would not be classified in the desired class by the other
classifier,andhenceweusethepredictionfromtheadditionalclassifierasthegroundtruth
validity.
Notethatseveraloftheevaluationmetricsmightbeatoddswitheachother,forexample,achiev-
inghighdiversitymightcomeatcostofbeingclosetothetrainingdata,orachievinghighvalidity
mightcomeatcostoflowproximity.
Someofthereviewedpapersdidnotevaluatetheiralgorithmonanyoftheabovemetrics.They
onlyshowedacoupleofexampleinputsandrespectiveCFEs(seeAppendixA).
6.3 OtherWorks
This section enlists works that talk about the desirable propertiesof counterfactualsor point to
their issues. We also talk about works that propose minor modifications to previous similar ap-
proaches.
WorksExploringDesirableCFEProperties.SokolandFlach[306]listseveraldesirableproperties
ofcounterfactualsinspiredfromMiller[238]andstatehowthemethodofflippinglogicalcondi-
tionsin adecisiontreesatisfiesmost ofthem. Laugel etal. [209] enlistproximity,connectedness,
andstabilityasthreedesirablepropertiesofaCFEandproposethemetricstomeasurethem.
Works Pointing to Issues with CFEs. Laugel et al. [211] say that if the explanation is not based
ontrainingdata,buttheartifactsofnon-robustnessoftheclassifier,itisunjustified.Theydefine
justifiedexplanationstobeconnectedtotrainingdatabyacontinuoussetofdatapoints,termed
E-chainability.Barocasetal.[30]statefivereasonsthathaveledtothesuccessofcounterfactual
explanationsandalsopointouttheoverlookedassumptions.Theymentiontheunavoidablecon-
flictswhichariseduetotheneedforprivacyinvasioninordertogeneratehelpfulexplanations.
MehediHasanandTalbert[236]statethatgeneratingmultipleCFEsforausermightoverwhelm
them in which case they might choose a suboptimal recourse. They propose a game-theoretic
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:16 S.Vermaetal.
frameworktoovercomethisproblem.KasirzadehandSmart[186]providephilosophicalinsight
intotheimplicitassumptionsandchoicesmadewhengeneratingCFEs.
Causal CFEs. Downs et al. [95] propose using conditional subspace VAEs (CSVAE), a vari-
antofVAEs,togenerateCFEsthatobeycorrelationsbetweenfeatures,causalrelationsbetween
features,andpersonalpreferences.Thismethodbuildsaprobabilisticdatamodelofthetraining
datausingaCSVAEandusesittogenerateCFEs.However,theseCFEsarenotwithrespecttoa
specificMLmodel.Crupietal.[73]proposeatechniquethatcanbeusedwithanycounterfactual
generationapproachtogeneratecausalityabidingCFEs.vonKügelgenetal.[343]extendKarimi
et al. [184]’s work to the setting where unobserved confounders may be present in the causal
setting. de Lara et al. [79] show that optimal transport-based methods are an approximation of
Pearl’sCFEsandhencecanbeusedtogeneratecausalCFEs.Beckers[34]delvesfurtherintothe
integrationofcausality,actualcausation,andCFEs.
CFE for Specific Models. Albini et al. [11] propose a CFE generation approach targeted for
Bayesiannetworkclassifiers.ArteltandHammer[18,19]enliststhecounterfactualoptimization
problemformulationforseveralmodel-specificcases,likegeneralizedlinearmodel,gaussiannaive
Bayes,andmentionthegeneralalgorithmtosolvethem.KoopmanandRenooij[198]proposea
BFS-basedtechniqueforgeneratingCFEsforBayesiannetworks.
WorksConsideringMulti-AgentScenariosofCFEs.TsirtsisandGomez-Rodriguez[327]castthe
counterfactual generation problem as a Stackelberg game between the decision maker and the
personreceivingtheprediction.GivenagroundsetofCFEs,theproposedalgorithmreturnsthe
top-k CFEs, which maximizes the utility of both the involved parties. Bordt et al. [41] point out
thattheinterestsoftheproviderandreceiverofmodelexplanationsmightbeinconflict,andthe
ambiguouspost-hoc explanationsmightbeunsuitableforachievingthepurposeoftransparency
asdesiredinGDPR.Thisalsorelatestofairwashing(seeresearchchallengeRC9).
GlobalCFEs.RawalandLakkaraju[278]proposeAReStogenerateruleliststhatactasglobal
CFEs.Leyetal.[216]andKanamorietal.[180]proposecomputationallymoreefficientimplemen-
tationofRawalandLakkaraju[278]’swork.Carrizosaetal.[53]proposeamixedintegerquadratic
modeltogenerateCFEsforagroupofdatapoints.Warrenetal.[354]andCarrizosaetal.[55]also
proposealgorithmstogenerategroupCFEs.Kooetal.[197]proposegeneratingCFEsforasetof
datapointsusingLagrangianandsubgradientmethods.Pedapatietal.[265]proposeatechnique
totrainagloballyinterpretablemodel(forablack-boxmodel)suchthatthismodelisconsistent
withthepertinentpositivesandpertinentnegatives[87]ofthetrainingdatapointsusedtotrain
theoriginalmodel.
Works Proposing Modifications to Previous Approaches. Chen et al. [63] and De Toni et al. [80]
use RL to generate CFE as was also proposedby Verma et al. [337]. Rasouli and Chieh Yu [272]
proposeageneticalgorithmtogenerateCFEsaswasalsoproposedbyDandletal.[75].Hashemi
andFathi[150]proposetousegeneticalgorithmforCFEgenerationsimilartoDandletal.[75]’s
work. Monteiro and Reynoso-Meza [242] propose extending Dandl et al. [75]’s approach using
U-NSGA-IIIevolutionaryalgorithm.Barretal.[31]extendMahajanetal.[229]’sworkbyinterpo-
latingbetweentheinputandCFEdatapointtogenerateCFEsclosertotheinputdatapoint.Sajja
etal.[289]proposeusingasemi-supervisedautoencoderinsteadofthetraditionalunsupervised
autoencodertogenerateCFEsclosetothetrainingdatamanifold.Huangetal.[160]proposeLORE-
LEYthatextendsLORE[139]togenerateCFEsformulti-classclassificationproblemsandaccount
forflowconstraints.Wijekoonetal.[360]usefeatureimportancesprovidedbyLIMEtoassistthe
case-based reasoning approach to generate CFEs. Delaney et al. [83] propose using trust scores
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:17
tomeasuretheout-of-distributionnessoftheCFEs.GuidottiandRuggieri[141]proposeusingan
ensembleofbaseCFEexplainerstogeneratediverseCFEs.
Benchmark and Dataset Curation. Mazzine and Martens [233] quantitatively compare 10 CFE
generatingapproachesusing22datasetsand9metrics.Pawelczyketal.[260]andArtelt[17]have
developed extensible toolboxes where several CFE approaches can be plugged in and compared
onspecificdatasets.
Semi-Factuals.Semi-factualsarerecentlyproposedkindofexplanationswherethegoalistonot
changethemodelprediction(unlikeCFEs),buttoimprovethecurrentoutcomebychangingthe
input. For example, if Alice’s loan request is approved but her rate of interest is high, how can
Alice change her features such as to get a lower rate of interest. Several works have proposed
novelalgorithmstogeneratesemi-factualexplanations[21,24,189,190].
Various Uncategorized Works. State [308] talks about generating CFEs with real-world con-
straints on features and adaptability with updating ML models using constraint logic program-
ming. Tahoun and Kassis [311] propose to disentangle actions from feature modifications to ad-
dressthelackofinterventiondataandappropriateactioncosts.Theusersshouldalreadydescribe
the actions they are willing to take, and a model should just choose the minimum cost action
thatgeneratestheCFE.Lucicetal.[220]proposeaCFEapproachtoprovidealowerandupper
bound for the feature values that get a low prediction error from the ML model for a datapoint
thatoriginallyhadahighpredictionerror.KorikovandBeck[199]andKorikovetal.[200]show
howCFEscanbegeneratedbyusingthegeneralizationofinversecombinatorialoptimizationand
solve it under two objectives. Pawelczyk et al. [261] provide a general upper bound on the cost
of counterfactual explanations under the phenomenon of predictive multiplicity, wherein more
than one trained model have the same test accuracy and there is no clear winner among them.
Fdez-Sánchezetal.[108]proposeahierarchicaldecompositions-basedmethodtoobtainCFEsfor
multi-classclassificationproblems.Bertossi[35]andMedeirosRaimundoetal.[234]proposebrute
forceapproachestogenerateCFEs.
7 CounterfactualExplanationsforOtherDataModalities
SincewerestrictthissurveytothepapersthatgenerateCFEsfortabulardata,inthissectionwe
pointthereaderstothepapersthatproposealgorithmstargetedtowardsotherdatamodalities:
(1) ImageData:[1,8,9,12,13,29,77,104,109,114,128,135,142,146,151,161,163,168,169,191,
192,207,217,218,237,255,256,266,284,291,304,320,333,334,340,347,359,368,370,377].
(2) TextData:[42,60,175,226,271,275,283,322,368–370].
(3) SpeechData:[375].
(4) Time-SeriesData:[26,82,159,185,310,326,333,351,352].
(5) GraphDataforGraphNeuralNetworks:[2,27,28,105,223,252,355].AsurveyforCFEon
graphneuralnetworks:[268].
(6) AgentAction(e.g.,reinforcementlearningorplanning):[43,257,309].
(7) RecommenderSystems:[81,129,130,176,296,313,324,364,378,380].
(8) FunctionalData:[54,201]andBehavioralData:[271].
8 OtherApplicationsofCounterfactualExplanations
Herewereferthereaderstootherapplicationswherecounterfactualexplanationsarebeingused
apartfromexplainingMLmodels:
(1) AnomalyandData-DriftDetection:HinderandHammer[153]proposetouseCFEstoexplain
datadrift.Sulemetal.[310]proposetouseCFEstoexplainanomaliesintime-seriesdatasets.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:18 S.Vermaetal.
Ravi et al. [276] wrote a survey on the explainability techniques for convolutional auto-
encodersforanomalydetectionofimages.Haldaretal.[148]proposetouseCFEstoexplain
anomalydetectionwhenusingautoencoders.Antoranetal.[15]useCFEstofindchanges
inadatapointthatwouldhelpaclassifierhaveahigherconfidenceinitsprediction.
(2) TrainingDatasetDebugging:YousefzadehandO’Leary[373]proposetouseCFEstodebug
MLmodelsbydiagnosingthebehaviorandusingsyntheticdatatoalterthedecisionbound-
aries. Qi and Chelmis [269] propose to use CFEs to debug potentially mislabeled datasets.
Ganetal.[124]proposetouseCFEstodetectbugsinfinancialmodels.HanandGhosh[149]
proposefindingaminimalsubsetoftrainingdatapointsthatareresponsibleforaparticular
predictionandhencecanbeusedtodebugtrainingdatasets.
(3) DataAugmentation:Yuanetal.[374]proposetouseCFEstoaugmenttrainingdatathatis
used to predict market volatility based on earning calls. Temraz and Keane [316] propose
usingCFEstoaugmenttrainingdatatotackletheclassimbalanceproblem.MehediHasan
and Talbert [235] and Rasouli and Yu [273] propose using CFEs for data augmentation of
tabulardatasetsforincreasedrobustness.Temrazetal.[317]proposeusingCFEstogenerate
datapointsthatcanbeusedtotrainMLmodelsthatpredictcropgrowth(afflictedbyclimate
change).
(4) DrugDesigning:Nguyenetal.[251]useCFEstofindchangesinadrugandproteinmolecule
thatwillincreasetheiraffinityforeachother.Theyusemulti-agentRLtothisend.
(5) ML Model Bias Detection: Myers et al. [246] build a visualization tool based on computing
CFEs to expose biases in ML models. Fawkes et al. [107] point out to the challenges with
usingCFEsfor fairness.OtherworksalsouseCFEstomeasureandmitigate modelbiases
[205,331].
(6) Various Applications: Mazzine et al. [232] propose to use CFEs in employment services to
helpjobseekersgetpersonalizedadviceforincreasingtheirpropensityforgettingrecom-
mendedforajobandtohelptheMLdeveloperstodetectpotentialbiasandotherissuesin
theirMLmodel.Sadleretal.[288]proposetouseCFEsforcommunitydetectioninsocial
networks.Fujiwaraetal.[121]proposetouseCFEstounderstandinteractivedimensionality
reduction.TsiakmakiandRagos[325]proposetouseCFEsforprovidingactionablesugges-
tionstoimprovestudentperformanceinauniversitycourse.Congetal.[69]proposeaCFE
approachtoexplainwhyatestsetfailstheKolmogorov-Smirnovtest.Marchezinietal.[230]
proposetouseCFEforalteringbothobservationalandlatentvariablestoreasonaboutmen-
talhealth.Yaoetal.[371]proposetousecounterfactualsforevaluatingtheexplanationsfor
recommender systems. Gupta et al. [144] use CFEs to propose changes to constraint satis-
faction problems that have no solutions. Teofili et al. [318] propose using CFEs to explain
entityresolutionmodels.Arteltetal.[22]useCFEstoexplainthedifferencesbetweenthe
learning of a pair of models. Frohberg and Binder [120] propose CRASS, a dataset to test
counterfactualreasoningofLLMs.
There has been one case of real-world deployment of CFEs in a hiring platform, Hired. Ne-
mirovskyetal.[249]useaGAN-basedapproach[250]togeneratecounterfactualsinordertoget
candidatesapprovedbytheHiredMarketplaceMLmodel.Theirapproachsatisfiesseveralofthe
desideratawediscussedinSection4.1,forexample:
(1) theyconsiderfeatureactionabilityandonlychangethemutablefeatureslikeexpectedsalary,
yearsofexperience,andskills;
(2) their loss function encourages proximity and they use L1 distance between the generated
counterfactualandtheinputdatapointtomeasureit;
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:19
(3) theyuseaGAN-basedapproachtogeneratecounterfactualsthatareclosetothedatamani-
foldanduseanauto-encoderreconstructionerrortomeasureit;
(4) their approach was designed to amortize the optimization process and they measure the
counterfactualgenerationtimetomeasurelatency.
9 OpenQuestionsandResearchProgress
Inthefirstversionofthissurveypaper,wedelineatedtheopenquestionsandchallengesyetto
betackledbytheexistingworkspertainingtoCFEs[336].Alotofprogresshasbeenmadebythe
researchcommunityandseveraloftheopenchallengeshavebeensolved(mentionedinthelater
section).Inthisversionofthepaper,wehighlightasetofmainresearchproblemsthatareyetto
beaddressedandinviteresearcherstotacklethem.
9.1 CurrentOpenQuestions
ResearchChallenge1. Counterfactualexplanationsshouldcapturetheapplicant’spreferences.
Along with the distinction between mutable and immutable features (finely classified into ac-
tionable, mutable, and immutable), counterfactual explanations should also capture preferences
specifictoanapplicant.Thisisimportantbecausetheeaseofchangingdifferentfeaturescandif-
feracrossapplicants.
Progress: Mahajan et al. [229] captures the applicant’s preferences using an oracle, but that
is expensive and is still a challenge. Rawal and Lakkaraju [278] use the Bradley-Terry model to
learn the pairwise cost for each feature pair and hence the preference among them. Yadav et al.
[366]arguethatassumingeachuser’scostofchangingdifferentfeaturesisthesameisunrealistic.
Theyproposeaskingfortheuser’scostfunctionorcomputingtheexpectationbysamplingcost
functionsfromadistribution.Despitetheprogress,incorporatinguserpreferenceshasnotbeen
standardizedandremainsanexpensiveandelusiveprocess.Ideally,atechniqueshouldbeableto
collectpreferencesasarankedlistoffeaturesandprovideCFEsthatadheretoit.
ResearchChallenge2. Counterfactualexplanationsshouldhandledynamics(datadrift,classi-
fierupdate,applicant’sutilityfunctionchanging,etc.)
Allcounterfactualexplanationpaperswereviewassumethattheunderlyingblackboxismono-
tonicanddoesnotchangeovertime.However,thismightnotbetrue;creditcardcompaniesand
banksupdatetheirmodelsasfrequentlyas12-18months[126].Therefore,counterfactualexpla-
nationalgorithmsshouldtakedatadriftandthedynamismandnon-monotonicityoftheclassifier
intoaccount.Therehasnotbeenmuchworkforaddressingthisresearchquestion.
ResearchChallenge3. Theabilityofcounterfactualexplanationstoworkwithmissingfeature
values.
Counterfactual explanation algorithms should also be able to handle missing feature values,
whichoftenhappensintherealworld[125].Therehasnotbeenmuchworkforaddressingthis
researchquestion.
ResearchChallenge4. Preservingmodelprivacy.
Privacy attacks on ML models can come in two major forms: member inference and model
extraction. Both of theseprivacy attackscan be enhanceddue to theprovision of CFEs. Aïvodji
et al. [7] empirically demonstrate that adversaries can train a surrogate model with very high
fidelitytotheoriginalmodel(i.e.,modelextractionattack)withasfewas1,000queriestothemodel
(whichisrequiredduringCFEgeneration).TheproblemisfurtheraggravatedwhendiverseCFEs
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:20 S.Vermaetal.
areprovided.Shokrietal.[299]havedemonstratedthatgradient-basedexplanationsmethodsleak
alotofinformationandmakethemodelsvulnerabletomembershipinferenceattacks.Miuraetal.
[240]proposeMEGEX,adata-freemodelextractionattackthatlearnsasurrogatemodelwithout
accesstoitstrainingdatabytrainingagenerativemodel.Wangetal.[350]proposeusingtheCFE
ofaCFEtotrainasurrogatemodelandshowthatitismoreefficientinmodelextractionwhen
comparedto[7].MostoftheworkspointouttothechallengesCFEpresentsfortheprivacyofthe
models,whilethesolutionsremainelusive.
ResearchChallenge5. Counterfactualexplanationsasaninteractiveservicetotheapplicants.
Counterfactualexplanationsshouldbeprovidedasaninteractiveinterface,whereanindividual
cancomeatregularintervals,informthesystemofthemodifiedstate,andgetupdatedinstructions
toachievethecounterfactualstate.Thiscanhelpwhentheindividualcouldnotpreciselyfollow
theearlieradviceforvariousreasons.
Progress: Hohman et al. [155] developed an interactive user-interface for providing expla-
nations to data scientists. They found out that data scientists used interactivity as the primary
mechanismforexploring,comparing,andexplainingpredictions.SokolandFlach[305]propose
toenhanceMLexplanationswithavoice-assistedinteractiveservice.Akulaetal.[9]proposeanap-
proachthatexplainsanMLmodelusinganinteractivesequenceofCFEs.Wangetal.[349]propose
refiningtheCFEsfordifferentfeaturechangecostsbasedonuserinteractions.Anidealapproach
to solve this problem would develop an interactive platform that will tailor a counterfactual for
theupdatedfeaturesateachstepoftheinteraction.
ResearchChallenge6. Counterfactualexplanationsshouldaccountforbiasintheclassifier.
Counterfactualspotentiallycaptureandreflectthebiasinthemodels.Tounderscorethisasa
possibility,Ustunetal.[331]experimentedonthedifferenceinthedifficultyofattainingacoun-
terfactualstateacrossgenders,whichclearlyshowedasignificantdifference.Moreworkmustbe
donetofindhowequallyeasycounterfactualexplanationscanbeprovidedacrossdifferentdemo-
graphicgroups,orhowadjustmentsshouldbemadetotheprescribedchangestoaccountforthe
bias.
Progress: RawalandLakkaraju[278]generaterecourserulesforasubgroupthattheyuseto
detectmodelbiases.Guptaetal.[145]proposeaddingaregularizerwhiletrainingaclassifierthat
encourages the classifier to maintain a similar distance of the decision boundary from different
demographic groups, thereby facilitating the opportunity of equal recourse across demographic
groups(whichistheirdefinitionoffairness).vonKügelgenetal.[344]extendthisfairnessnotion
whenthedistancebetweentherecourseismeasuredinacausalmanner.Galhotraetal.[123]pro-
poseLEWISthatusesCFEstoidentifyracialbiasinCOMPASandgenderinAdultdatasets.Dash
etal.[77]proposeusingCFEstodetectbiasinimageclassifiersandcounterfactualregularizerto
counteractthatbias.However,anapproachthatconsiderthebiasoftheclassifierwhilegenerating
CFEsstillsneedstoberesearched.
ResearchChallenge7. Generatingoptimalrecourseswhenconsideringamulti-agentscenario.
O’Brien and Kim [253] demonstrate the non-optimality of recourses generated when a single
agent’s interest is considered in a multi-agent scenario like the prisoner’s dilemma. In the real
world,anagent’sactionsaffectotheragents,hencegeneratingrecoursesthatconsidertheinterests
of multiple agents would be useful. Therehas not been much work for addressing this research
question.
Research Challenge 8. Strengthen the ties between machine learning and regulatory commu-
nities.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:21
Ajointstatementbetweenthemachinelearningcommunityandregulatorycommunity(OCC,
FederalReserve,FTC,CFPB)acknowledgingsuccessesandlimitationsofwherecounterfactualex-
planationswillbeadequateforlegalandconsumer-facingneedsandwouldimprovetheadoption
anduseofcounterfactualexplanationsincriticalsoftware.
Progress: Reed et al. [280] talk about how regulation and policies need to adapt to how ML
modelscanexplaintheirdecisions.Howevermuchmoreneedstobedoneinordertoenhancethe
adoptionofCFEs.
ResearchChallenge9. Guardingagainstfairwashing.
Aivodjietal.[5,6]havepointedouttheriskofanadversaryusingmodelexplanationstoratio-
nalizeamodel’sdecisionsandobscureitsbias.Itremainstobeseenifthefairrecourseapproaches
canguardagainstfairwashing.
ResearchChallenge10. Enhancereal-worlddeploymentofcounterfactuals.
Progress: Therehasbeenoneknowncaseofreal-worlddeploymentofcounterfactualsatHired
platformsforprovidingadvicetocandidatesseekingjobs[250].DeployingCFEsinmorerealworld
applicationswillimproveourunderstandingofuserpreferencesandhighlightnewresearchchal-
lenges.
Research Challenge 11. Counterfactual explanations should also inform the applicants about
whatmustnotchange
Suppose a CFE advises someone to increase their income but does not tell that their length of
last employment should not decrease. To increase their income, the applicant who switches to a
higher-payingjobmayfindthemselvesinaworsepositionthanearlier.Thus,byfailingtodisclose
whatmustnotchange,anexplanationmayleadtheapplicanttoanunsuccessfulstate[30].This
corroboratesRC5,wherebyanapplicantmightbeabletointeractwithaplatformtoseetheeffect
ofapotentialreal-worldactiontheyareconsideringtakingtoachievethecounterfactualstate.
9.2 QuestionswithSignificantResearchProgress
Inthissection,wehighlighttheresearchprogressmadefortowardspreviouslyopenquestions.
ResearchProblem1. Unifycounterfactualexplanationswithtraditional“explainableAI.”
Althoughcounterfactualexplanationshavebeencreditedtoelicitingcausalthinkingandprovid-
ingactionablefeedbacktousers,theydonottellwhichfeature(s)wastheprincipalreasonforthe
originaldecisionandwhy.Itwouldbeniceif,alongwithgivingactionablefeedback,counterfac-
tualexplanationsalsogavethereasonfortheoriginaldecision,whichcanhelpapplicantsunder-
standthemodel’slogic.Thisisaddressedbytraditional“explainableAI”methodslikeLIME[281],
Anchors[282],Grad-CAM[294].
Progress: Guidottietal.[139]haveattemptedthisunification,astheyfirstlearnalocaldeci-
siontreeandtheninterprettheinversionofdecisionnodesofthetreeascounterfactualexplana-
tions.However,theydonotshowtheCFEstheygenerate,andtheirtechniquealsomissesother
desiderataofcounterfactuals(seeSection4.1).KommiyaMothilaletal.[196]proposenecessityand
sufficiencyasthetwoimportantpropertiesofanexplanation.Featureattributionexplanationsfind
thefeaturevaluesthataresufficientforaprediction,whileCFEsfindthefeaturevaluesthatare
necessaryforaprediction.Theyproposemethodstofindthenecessityandsufficiencyofanyfea-
ture subset and discuss how that aligns with finding CFEs. Galhotra et al. [123] propose Lewis
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:22 S.Vermaetal.
thatalsoemphasizesthenecessityandsufficiencyscoresofafeaturesubsetinfindingitsglobalim-
portanceandingeneratingaCFEforlocalexplainability.Jiaetal.[171]proposetouseDeepLIFT
to assign contribution scores to the features that changed in a counterfactual datapoint. Ramon
etal.[271]rankthefeatureimportancesusingLIMEandSHAP,andthenremovethefeaturesin
decreasingorderofimportanceuntilaCFEisfound.Wiratungaetal.[361]proposetousemethods
likeLIMEandSHAPtofindfeatureimportancesandthenreplacethefeaturesindecreasingorder
ofimportancewiththevaluesborrowedfromthenearestunlikeneighbor(case-basedreasoning
approach).Albinietal.[10]proposetochangethebackgrounddistributionusedtocomputethe
Shapleyvaluestomakethefeatureattributionamounttothecounterfactual-abilityofthefeatures,
i.e., changing a feature with higher attribution would have a higher probability of changing the
prediction.WangandVasconcelos[347]proposetousethediscriminantattributionexplanations
asawaytoproduceCFEsforimages.Wijekoonetal.[360]useLIMEtoassistcase-basedreasoning
techniquestogenerateCFEs.Geetal.[127]proposeusingcounterfactual-abilityoffeaturesasa
metricfortheirfeatureimportance.
Research Problem 2. Provide counterfactual explanations as discrete and sequential steps of
actions.
Mostcounterfactualgenerationapproachesreturnthemodifieddatapoint,whichwouldreceive
the desired classification. The modified datapoint (state) reflects the idea of instantaneous and
continuousactions,butintherealworld,actionsarediscreteandoftensequential.Therefore,the
counterfactualgenerationprocessmusttakethediscretenessofactionsintoaccountandprovidea
seriesofactionsthatwouldtaketheindividualfromthecurrentstatetothemodifiedstate,which
hasthedesiredclasslabel.
Progress: Naumann and Ntoutsi [247] argue that to help an individual achieve the desired
goal, CFEs should be provided as a sequential step of actions instead of just providing the final
goal. Singh et al. [300] conduct a user study to show the high preference for a sequential step
of actions steps over a single-step goal. Ramakrishnan et al. [270] propose a program synthesis
basedtechniquetogeneratesuchsequences.Kanamorietal.[181]proposeamixed-integerbased
programmingmethodandVermaetal.[337]proposeanRL-basedmethodthatgeneratesordered
sequencesofactionsasaCFE.
Research Problem 3. The ability of counterfactual explanations to work with incomplete—or
missing—causalgraphs.
IncorporatingcausalityinthecounterfactualgenerationisessentialfortheCFEstobegrounded
inreality.Completecausalgraphsandstructuralequationsarerarelyavailableintherealworld,
andthereforethealgorithmshouldbeabletoworkwithincompletecausalgraphs.
Progress: Mahajanetal.[229]’sapproachwasthefirsttobecompatiblewithincompletecausal
graphs.NowotherworkslikeGalhotraetal.[123],Vermaetal.[337],Schleichetal.[292],Yang
etal.[367]canalsoworkwithpartialcausalgraphs.
ResearchProblem4. Scalabilityandthroughputofcounterfactualexplanationsgeneration.
AsweseeinTable1,mostapproachesneedtosolveanoptimizationproblemtogenerateone
counterfactualexplanation.Somepapersgeneratemultiplecounterfactualswhileoptimizingonce,
but they still need to optimize separately for different input datapoints. However, for industrial
deployment,thegenerationshouldbemorescalable.
Progress: Mahajan et al. [229] learn a VAE which can generate multiple CFEs for any given
inputdatapointaftertraining.Therefore,theirapproachishighlyscalableandistermedas“amor-
tizedinference”.Vermaetal.[337]proposedanRL-basedtechnique,FastAR,thatalsogenerates
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:23
amortized CFEs. Van Looveren et al. [333], Samoilescu et al. [290], Yang et al. [367], Rawal and
Lakkaraju[278],andNemirovskyetal.[250]alsoproposeapproachestothisend.
ResearchProblem5. Generaterobustcounterfactualexplanations[112,239].
Counterfactual explanation optimization problems force the modified datapoint to obtain the
desiredclasslabel.However,themodifieddatapointcouldbelabeledeitherinarobustmanneror
duetotheclassifier’snon-robustness,e.g.,anoverfittedclassifier.Laugeletal.[209]termthisas
thestabilitypropertyofacounterfactual.Therearethreekindsofrobustnessneeds:(1)robustness
tomodelchangeswhenmodelsareretrained,forexample,(2)robustnesstotheinputdatapoint
(twoindividualswithaslightchangeinfeaturesshouldbegivensimilarCFEs),and(3)robustness
tosmallchangesintheattainedCFE(aCFEwithminorchangestotheoriginallysuggestedCFE
shouldalsobeaccepted).
Progress: Slacketal.[302]underscorethischallengebyshowingthatsmallperturbationsin
theinputdatapointscanresultindrasticallydifferentCFEs.Rawaletal.[277]furtheremphasize
thischallengebyempiricallydemonstratingtheinvalidationofalreadyprescribedrecourseswhen
theMLmodelgetsretrainedondatasetswithtemporalorgeospatialdistributionshifts.Arteltetal.
[23]evaluatetherobustnessofclosestCFEswhencontrastedwithCFEsgeneratedwiththedata
manifoldconstraint.Bueffetal.[47]proposetheframeworktomeasuretherobustnessofmodels
by purposing generated CFEs as adversarial attack datasets. Virgolin and Fracaros [342] empiri-
callyshowthatnon-robustCFEsencounterahighercostofchangewhenadverseperturbations
areappliedtothedatapoint,thusconcludingthatrobustnessinCFEsshouldbeconsidered.
Upadhyayetal.[330]proposeatechniquenamedROAR thatusesadversarialtrainingtogen-
erate recourses robust to changes in an ML model that is retrained on a distributionally shifted
training dataset. Dominguez-Olmedo et al. [93] show that the CFEs that just cross the decision
boundaryareusuallynon-robustandformulateanoptimizationproblemthatgeneratesrobustre-
courseforlinearmodelsandneuralnetworks.Pawelczyketal.[262]proposeatechniquenamed
PROBE that generates robust CFEs while letting the users decide the tradeoff between the CFE
invalidationriskanditscost.Blacketal.[37]arguethatrobustCFEsshouldhavehigh=confidence
neighborhoodswithsmallLipschitzconstants,andproposeaStableNeighborSearchalgorithmto
thatend.Buietal.[48]proposeanalgorithmtogeneraterobustCFEsbyconsideringadistribution
overtheparametersofthemodelifretrained.Duttaetal. [103]proposecounterfactualstability
(the lower bound of the predicted class probability for the sampled datapoints in the neighbor-
hoodofagivenCFE)asametricforfilteringrobustCFEs.Bajajetal.[28]proposeatechniqueto
generaterobustCFEsforgraphneuralnetworks.
ResearchProblem6. Extendcounterfactualexplanationsbeyondclassification.
Progress: Recentworkhasbeenextendingcounterfactualexplanationstodifferenttasksand
model architectures. Spooner et al. [307] propose a Bayesian optimization-based technique for
generating CFEs for regression problems. Numeroso and Bacciu [252] propose an RL-based ap-
proachforgeneratingCFEsforgraphneuralnetworks,whichareusedtopredictchemicalmole-
culeproperties.Delaneyetal.[82]proposeacase-basedreasoningapproachtogenerateCFEsfor
atime-seriesclassifier.
ResearchProblem7. Handlingofcategoricalfeaturesincounterfactualexplanations
Differentarticleshavecomeupwithvariousmethodstohandlecategoricalfeatures,likecon-
verting them to one-hot encoding and then enforcing the sum of those columns to be 1 using
regularization or a hard constraint, or clamping an optimization problem to a specific categori-
cal value, or leaving them to be automatically handled by genetic approaches and SMT solvers.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:24 S.Vermaetal.
Measuringdistanceincategoricalfeaturesisalsonotobvious.Somearticlesuseanindicatorfunc-
tion, which equates to 1 for unequal values and 0 if the same; other papers convert to one-hot
encodingandusestandarddistancemetricslikeL1/L2norm,orusethedistanceinMarkovchains
[115].Therefore,handlingcategoricalvariableshavenotbeenstandardized,futureresearchmust
considerthisanddevelopappropriatemethods.
ResearchProblem8. Evaluatecounterfactualexplanationsusingauserstudy.
Theevaluationforcounterfactualexplanationsmustbedoneusingauserstudybecauseeval-
uationproxies(seeSection6)mightnotbeabletopreciselycapturethepsychologicalandother
intricaciesofhumancognitionontheeaseofactionabilityofacounterfactual.Keaneetal.[187]
emphasizetheimportanceofuserstudiesinthecontextofCFEs.
Progress: Förster et al. [116] conduct a user study with 144 participants to understand the
formatofexplanationtheyprefer.Theyconcludethatuserspreferconcrete,consistent,relevant
explanations,andlengthyexplanationsiftheyareconcrete.Försteretal.[115]conductauserstudy
with46participantswhowereaskedtoratetherealisticnessoftheCFEsgeneratedbytheirsand
a baseline approach. Using statistical tests, they concluded that the CFEs generated by their ap-
proach were perceived to be more real and typical. Rawal and Lakkaraju [278] conduct a user
studywith21participantswhowereaskedtodetectabiasintherecoursesummariesfordemo-
graphicgroups.Kanamorietal.[180]conductauserstudywith35participantstocomparetheir
globalCFEgeneratingtechniquewiththatofRawalandLakkaraju[278].Singhetal.[300]conduct
auserstudywith54participantsandfoundthatmostuserspreferspecificdirectivesovergeneric
andnon-directiveexplanations.Warrenetal.[353]conductauserstudywith127participantsand
foundthatcounterfactualexplanationselicitedhighertrustandsatisfactionthancausalexplana-
tions. Yacoby et al. [365] conduct a user study with eight U.S. state court judges to understand
theirresponsetoCFEsfrompretrialriskassessmentinstruments(PRAI).Theyconcludethat
judges ignored the CFEs and focused on the factual features of the defendant. Kuhl et al. [204]
conduct a user study with 74 users in an interactive game setting and found that users benefit
lessfromreceivingcomputationallyplausibleCFEsthantheclosestCFEs(measuredusingfeature
distance). Zhang. et al. [376] conduct a user study with 200 users to check their understanding
ofglobal,local,andCFexplanations.Caietal.[51]conductauserstudyon1070participantsto
understand how users perceive explanations when provided examples from the desired class vs.
whenprovidedexamplesfromallotherclasses.CelarandByrne[57]conductauserstudywith
731participantsandconcludedthatcounterfactualexplanationswereperceivedtobebetterexpla-
nationsthanfactualexplanations(explanationsjustifyingtheoriginalmodelprediction).Daietal.
[74]conductauserstudywith243participantsandfoundthatcounterfactualandprefactualexpla-
nationswereequallyhelpful.Delaneyetal.[84]conductauserstudyandfoundthatparticipants
preferlarge,meaningfuleditsforcounterfactualexplanationsforimages.
ResearchProblem9. Counterfactualexplanationsshouldbeintegratedwithdatavisualization
interfaces.
Counterfactualexplanationswilldirectlyinteractwithconsumerswithvaryingtechnicalknowl-
edge levels; therefore, counterfactual generation algorithms should be integrated with visualiza-
tion interfaces. We already know that visualization can influence human behavior [70], and a
collaborationbetweenmachinelearningandHCIcommunitiescouldhelpaddressthischallenge.
Progress: Chengetal.[64],Gomezetal.[132,133],Leungetal.[214],andWexleretal.[356]
havedevelopedinteractivegraphicaluserinterfacesfordisplayingCFEs.DECE[64]alsosumma-
rizesCFEsforsubgroupsthatcanhelpdetectmodelbiases,ifany.Tamagninietal.[312]develop
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:25
avisualizationtoolforCFEsfortextclassificationmodels.Hohmanetal.[155]alsobuildavisual
interactiveuserinterfaceforprovidingmodelexplanations.
ResearchProblem10. Incentivizeuserstoimprovefeaturesinnon-manipulativeways.
Anapproachthatprovidesarecoursetousersmightwanttopreventthe“gamification”ofthe
model (when users manipulate simple features like thepurposeof a loan to get approved). This
alsoprotectstheMLmodelsfromadversarialrobustnessattacks.
Progress: Chenetal.[62]proposetheoptimizationobjectiveforlinearclassificationmodels
when the goal is to develop an accurate model that encourages actual feature improvement for
users.Theycategorizefeaturesintothreecategories:improvement,manipulative,andimmutable.
Usersshouldbeencouragedtochangetheimprovementfeatures,notthemanipulativeoneswhen
optimizingforrecourse.Königetal.[206]suggestusingcausalitytogeneratemeaningfulrecourses
andpreventgamificationofthemodel.
10 Conclusions
In this article, we collected and reviewed more than 350 papers which proposed various algo-
rithmicsolutionstofindingcounterfactualexplanationsforthedecisionsproducedbyautomated
systems,specificallyautomatedbymachinelearning.Evaluatingallthepapersonthesamerubric
helpsinquicklyunderstandingthepeculiaritiesofdifferentapproachesandtheadvantages,and
disadvantagesofeachofthem,whichcanalsohelporganizationschoosethealgorithmbestsuited
to their application constraints. This has also helped us readily identify the gaps, which will be
beneficial to researchers scouring for open problems in this space and quickly sifting the large
bodyofliterature.Wehopethisarticlecanalsobethestartingpointforpeoplewantingtogetan
introductiontothebroadareaofcounterfactualexplanationsandguidethemtoproperresources
forthingstheymightbeinterestedin.
Appendices
A FullTable
Initially, we categorized the set of papers with more columns and in a much larger table. We
selectedthemostcriticalcolumnsandputtheminTable1.Thefulltableisavailablehere.
B BurgeoningLegalFrameworksaroundExplanationsinAI
To increase the accountability of automated decision systems—specifically, AI systems—laws
and regulations regarding the decisions produced by such systems have been proposed and
implemented across the globe [94]. The most recent version of the European Union’s General
Data Protection Regulation (GDPR), enforced starting on May 25, 2018, offered a right to
informationabouttheexistence,logic,andenvisagedconsequencesofsuchasystem[134].This
also includes the right to not be a subject of an automated decision-making system. Although
the closeness of this law to “right to explanation” is debatable and ambiguous [345], the official
interpretationbyWorkingPartyforArticle29hasconcludedthattheGDPRrequiresexplanations
of specific decisions, and therefore counterfactual explanations are apt. In the US, the Equal
Credit Opportunity Act (ECOA) and the Fair Credit Reporting Act (FCRA) require the
creditortoinform thereasonsforanadverseaction,suchasrejectionofaloanrequest[58,59].
Theygenerallycomparetheapplicant’sfeaturetotheaveragevalueinthepopulationtoarriveat
theprincipalreasons.GovernmentreportsfromtheUnitedKingdom[254]andFrance[166,341]
also touched on the issue of explainability in AI systems. In the US, Defense Advanced
Research Projects Agency (DARPA) launched the Explainable AI (XAI) program in 2016
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:26 S.Vermaetal.
to encourage research into designing explainable models, understanding the psychological
requirements of explanations, and the design of explanation interfaces [76]. The European
Union has taken similar initiatives as well [67, 329]. The US White House recently put forward
the Blueprint for an AI Bill of Rights [158] to modulate decisions from automated systems.
The Bill outlines five principles for operating such systems: (1) safe and effective systems, (2)
algorithmicdiscriminationprotections,(3)dataprivacy,(4)explanationsfordecisionsmadeusing
such systems, and (5) discussion about human alternatives. While many techniques have been
proposedforexplainablemachinelearning,itisyetunclearifandhowthesespecifictechniques
can help address the letter of the law. Future collaboration between AI researchers, regulators,
the legal community, and consumer watchdog groups will help ensure the development of
trustworthyAI.
Acknowledgments
WethankJasonWittenbach,AdityaKusupati,DivyatMahajan,JessicaDai,SoumyeSinghal,Harsh
Vardhan,andJesseMichelforhelpfulcomments.
References
[1] AbubakarAbid,MertYuksekgonul,andJamesZou.2022.Meaningfullydebuggingmodelmistakesusingconceptual
counterfactualexplanations.InProceedingsofthe39thInternationalConferenceonMachineLearning.PMLR,66–88.
https://proceedings.mlr.press/v162/abid22a.html
[2] CarloAbrateandFrancescoBonchi.2021.Counterfactualgraphsforexplainableclassificationofbrainnetworks
(KDD’21).ACM,NewYork,10.https://doi.org/10.1145/3447548.3467154
[3] AminaAdadiandMohammedBerrada.2018.Peekinginsidetheblack-box:Asurveyonexplainableartificialintelli-
gence(XAI).IEEEAccessPP(092018),1–1.https://doi.org/10.1109/ACCESS.2018.2870052
[4] CharuC.Aggarwal,ChenChen,andJiaweiHan.2010.Theinverseclassificationproblem.J.Comput.Sci.Technol.
(2010),458–468.https://doi.org/10.1007/s11390-010-9337-x
[5] UlrichAïvodji,HiromiArai,OlivierFortineau,SébastienGambs,SatoshiHara,andAlainTapp.2019.Fairwashing:
Theriskofrationalization.InProceedingsofthe36thInternationalConferenceonMachineLearning.PMLR.https://
proceedings.mlr.press/v97/aivodji19a.html
[6] UlrichAïvodji,HiromiArai,SébastienGambs,andSatoshiHara.2021.Characterizingtheriskoffairwashing.In
AdvancesinNeuralInformationProcessingSystems,Vol.34.CurranAssociates,Inc.https://proceedings.neurips.cc/
paper/2021/file/7caf5e22ea3eb8175ab518429c8589a4-Paper.pdf
[7] UlrichAïvodji,AlexandreBolot,andSébastienGambs.2020.Modelextractionfromcounterfactualexplanations.
arXiv:2009.01884(2020).
[8] ArjunAkula,ShuaiWang,andSong-ChunZhu.2020.CoCoX:Generatingconceptualandcounterfactualexplana-
tionsviafault-lines.InProceedingsoftheAAAIConferenceonArtificialIntelligence34,03(Apr.2020),2594–2601.
https://doi.org/10.1609/aaai.v34i03.5643
[9] ArjunR.Akula,KezeWang,ChangsongLiu,SariSaba-Sadiya,HongjingLu,SinisaTodorovic,JoyceChai,andSong-
ChunZhu.2022.CX-ToM:Counterfactualexplanationswiththeory-of-mindforenhancinghumantrustinimage
recognitionmodels.iScience25,1(2022),103581.https://doi.org/10.1016/j.isci.2021.103581
[10] EmanueleAlbini,JasonLong,DanialDervovic,andDanieleMagazzeni.2022.Counterfactualshapleyadditiveexpla-
nations(FAccT’22).ACM,NewYork,17.https://doi.org/10.1145/3531146.3533168
[11] EmanueleAlbini,AntonioRago,PietroBaroni,andFrancescaToni.2021.Influence-drivenexplanationsforBayesian
networkclassifiers.InPRICAI2021.Springer-Verlag,Berlin,,13.https://doi.org/10.1007/978-3-030-89188-67
[12] GoharAli,FerasAl-Obeidat,AbdallahTubaishat,TehseenZia,MuhammadIlyas,andAlvaroRocha.2021.Counter-
factualexplanationofBayesianmodeluncertainty.NeuralComputingandApplications(Sept.2021).https://doi.org/
10.1007/s00521-021-06528-z
[13] KamranAlipour,ArijitRay,XiaoLin,MichaelCogswell,JurgenP.Schulze,YiYao,andGiedriusT.Burachas.2021.
Improvingusers’mentalmodelwithattention-directedcounterfactualedits.AppliedAILetters 2,4(2021).https:
//doi.org/10.1002/ail2.47
[14] RobertAndrews,JoachimDiederich,andAlanB.Tickle.1995.Surveyandcritiqueoftechniquesforextractingrules
fromtrainedartificialneuralnetworks.Know.-BasedSyst.8,6(1995),17.https://doi.org/10.1016/0950-7051(96)81920-
4
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:27
[15] JavierAntoran,UmangBhatt,TameemAdel,AdrianWeller,andJoséMiguelHernández-Lobato.2021.Gettinga
CLUE:Amethodforexplaininguncertaintyestimates.InProceedingsoftheInternationalConferenceonLearning
Representations.https://openreview.net/forum?id=XSLF1XFq5h
[16] DanielApleyandJingyuZhu.2020.Visualizingtheeffectsofpredictorvariablesinblackboxsupervisedlearning
models.JournaloftheRoyalStatisticalSociety:SeriesB(StatisticalMethodology)82(4)(062020),1059–1086.https://
doi.org/10.1111/rssb.12377
[17] André Artelt. 2019 - 2021. CEML: Counterfactuals for Explaining Machine Learning Models. https://www.
github.com/andreArtelt/ceml
[18] AndréArteltandBarbaraHammer.2019.OntheComputationofCounterfactualExplanations–ASurvey.http://
arxiv.org/abs/1911.07749
[19] André Artelt and Barbara Hammer. 2020. Efficient Computation of Contrastive Explanations. https://doi.org/
10.48550/ARXIV.2010.02647
[20] AndréArteltandBarbaraHammer.2021.ConvexOptimizationforActionable&PlausibleCounterfactualExplana-
tions.https://doi.org/10.48550/ARXIV.2105.07630
[21] AndréArteltandBarbaraHammer.2022.“Evenif...”–DiverseSemifactualExplanationsofReject.arXiv:2207.01898
[22] AndréArtelt,FabianHinder,ValerieVaquet,RobertFeldhans,andBarbaraHammer.2021.Contrastiveexplana-
tionsforexplainingmodeladaptations.InAdvancesinComputationalIntelligence.SpringerInternationalPublishing,
Cham,101–112.https://doi.org/10.1007/978-3-030-85030-29
[23] AndréArtelt,ValerieVaquet,RizaVelioglu,FabianHinder,JohannesBrinkrolf,MalteSchilling,andBarbaraHammer.
2021.Evaluatingrobustnessofcounterfactualexplanations.InProceedingsofthe2021IEEESymposiumSerieson
ComputationalIntelligence(SSCI)(2021),01–09.https://doi.org/10.1109/SSCI50451.2021.9660058
[24] SaugatAryal.2024.Semi-factualexplanationsinAI.InProceedingsoftheAAAIConferenceonArtificialIntelligence
38(2024),23379–23380.https://doi.org/10.1609/aaai.v38i21.30390
[25] NicholasAsher,LucasDeLara,SoumyaPaul,andChrisRussell.2022.Counterfactualmodelsforfairandadequate
explanations.MachineLearningandKnowledgeExtraction4,2(2022),316–349.https://doi.org/10.3390/make4020014
[26] EmreAtes,BurakAksar,VitusJ.Leung,andAyseK.Coskun.2021.Counterfactualexplanationsformultivariate
timeseries.InProceedingsofthe2021InternationalConferenceonAppliedArtificialIntelligence(ICAPAI’21).1–8.https:
//doi.org/10.1109/ICAPAI49758.2021.9462056
[27] DavideBacciuandDaniloNumeroso.2022.Explainingdeepgraphnetworksviainputperturbation.IEEETransactions
onNeuralNetworksandLearningSystems(2022).https://doi.org/10.1109/TNNLS.2022.3165618
[28] MohitBajaj,LingyangChu,ZiYuXue,JianPei,LanjunWang,PeterCho-HoLam,andYongZhang.2021.Robust
CounterfactualExplanationsonGraphNeuralNetworks.https://doi.org/10.48550/ARXIV.2107.04086
[29] RachanaBalasubramanian,SamuelSharpe,BrianBarr,JasonWittenbach,andC.BayanBruss.2020.Latent-CF:A
SimpleBaselineforReverseCounterfactualExplanations.https://doi.org/10.48550/ARXIV.2012.09301
[30] SolonBarocas,AndrewD.Selbst,andManishRaghavan.2020.Thehiddenassumptionsbehindcounterfactualex-
planations and principal reasons. In Proceedings of the Conference on Fairness, Accountability, and Transparency
(FAccT’20)(FAT*’20).ACM,NewYork,10.https://doi.org/10.1145/3351095.3372830
[31] BrianBarr,MatthewR.Harrington,SamuelSharpe,andC.BayanBruss.2021.CounterfactualExplanationsviaLatent
SpaceProjectionandInterpolation.https://doi.org/10.48550/ARXIV.2112.00890
[32] C.VanFraassenBas.1980.TheScientificImage.OxfordUniversityPress.
[33] BarryBeckerandRonnyKohavi.1996.Adult.UCIMachineLearningRepository.https://doi.org/10.24432/C5XW20
[34] SanderBeckers.2022.CausalExplanationsandXAI.https://doi.org/10.48550/ARXIV.2201.13169
[35] LeopoldoBertossi.2021.Declarativeapproachestocounterfactualexplanationsforclassification.TheoryandPractice
ofLogicProgramming23(122021),1–35.https://doi.org/10.1017/S1471068421000582
[36] ReubenBinns,MaxVanKleek,MichaelVeale,UlrikLyngs,JunZhao,andNigelShadbolt.2018.’It’sreducingahuman
beingtoapercentage’:Perceptionsofjusticeinalgorithmicdecisions.InProceedingsofCHI2018.ACM,NewYork,
14.https://doi.org/10.1145/3173574.3173951
[37] EmilyBlack,ZifanWang,andMattFredrikson.2022.Consistentcounterfactualsfordeepmodels.InProceedingsof
theInternationalConferenceonLearningRepresentations.https://arxiv.org/abs/2110.03109
[38] JockBlackard.1998.Covertype.UCIMachineLearningRepository.https://doi.org/10.24432/C50K5N
[39] PierreBlanchart.2021.AnExactCounterfactual-example-basedApproachtoTree-ensembleModelsInterpretability.
https://doi.org/10.48550/ARXIV.2105.14820
[40] R.D.BochandM.Lieberman.1970.Fittingaresponsemodelforndichotomouslyscoreditems.Psychometrika35
(1970),179–97.
[41] SebastianBordt,MichèleFinck,EricRaidl,andUlrikevonLuxburg.2022.Post-HocExplanationsFailtoAchieve
theirPurposeinAdversarialContexts.https://arxiv.org/abs/2201.10295
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:28 S.Vermaetal.
[42] ZeydBoukhers,TimoHartmann,andJanJürjens.2022.COIN:CounterfactualImageGenerationforVQAInterpre-
tation.https://doi.org/10.48550/ARXIV.2201.03342
[43] MartimBrandão,GerardCanal,SenkaKrivić,PaulLuff,andAmandaColes.2021.How expertsexplainmotion
planneroutput:Apreliminaryuser-studytoinformthedesignofexplainableplanners.InProceedingsofthe2021
30thIEEEInternationalConferenceonRobot&HumanInteractiveCommunication(RO-MAN’21).299–306.https://
doi.org/10.1109/RO-MAN50785.2021.9515407
[44] KatherineElizabethBrown,DougTalbert,andSteveTalbert.2021.Theuncertaintyofcounterfactualsindeeplearn-
ing.InTheInternationalFLAIRSConferenceProceedings34(2021).https://doi.org/10.32473/flairs.v34i1.128795
[45] KieranBrowneandBenSwift.2020.SemanticsandExplanation:WhyCounterfactualExplanationsProduceAdver-
sarialExamplesinDeepNeuralNetworks.https://doi.org/10.48550/ARXIV.2012.10076
[46] DieterBrughmansandDavidMartens.2021.NICE:AnAlgorithmforNearestInstanceCounterfactualExplanations.
https://doi.org/10.48550/ARXIV.2104.07411
[47] AndreasC.Bueff,MateuszCytryński,RaffaellaCalabrese,MatthewJones,JohnRoberts,JonathonMoore,andIain
Brown.2022.Machinelearninginterpretabilityforastressscenariogenerationincreditscoringbasedoncounter-
factuals.ExpertSystemswithApplications202(2022).https://doi.org/10.1016/j.eswa.2022.117271
[48] NgocBui,DuyNguyen,andVietAnhNguyen.2022.CounterfactualPlansunderDistributionalAmbiguity.https://
doi.org/10.48550/ARXIV.2201.12487
[49] RuthByrne.2008.Therationalimagination:Howpeoplecreatealternativestoreality.TheBehavioralandBrain
Sciences30(2008),439–53;discussion453.https://doi.org/10.1017/S0140525X07002579
[50] RuthM.J.Byrne.2019.Counterfactualsinexplainableartificialintelligence(XAI):Evidencefromhumanreasoning.
InProceedingsofthe28thInternationalJointConferenceonArtificialIntelligence(IJCAI-19).InternationalJointCon-
ferencesonArtificialIntelligenceOrganization,California,USA,6276–6282.https://doi.org/10.24963/ijcai.2019/876
[51] CarrieJ.Cai,JonasJongejan,andJessHolbrook.2019.Theeffectsofexample-basedexplanationsinamachine
learninginterface(IUI’19).ACM,NewYork,258–262.https://doi.org/10.1145/3301275.3302289
[52] MiguelÁ.Carreira-PerpiñánandSuryabhanSinghHada.2021.Counterfactualexplanationsforobliquedecision
trees:Exact,efficientalgorithms.InProceedingsoftheAAAIConferenceonArtificialIntelligence35(May2021),6903–
6911.https://doi.org/10.1609/aaai.v35i8.16851
[53] Emilio Carrizosa, Jasone Ramirez-Ayerbe, and Dolores Romero Morales. 2021. Generating Collective Coun-
terfactual Explanations in Score-Based Classification via Mathematical Optimization. https://doi.org/10.13140/
RG.2.2.22996.12168/1
[54] EmilioCarrizosa,JasoneRamírez-Ayerbe,andDoloresRomeroMorales.2022.CounterfactualExplanationsforFunc-
tionalData:AMathematicalOptimizationApproach.https://doi.org/10.13140/RG.2.2.25682.68801
[55] EmilioCarrizosa,JasoneRamírez-Ayerbe,andDoloresRomeroMorales.2024.Mathematicaloptimizationmodelling
for group counterfactual explanations. European Journal of Operational Research (2024). https://doi.org/10.1016/
j.ejor.2024.01.002
[56] DiogoV.Carvalho,EduardoM.Pereira,andJaimeS.Cardoso.2019.Machinelearninginterpretability:Asurveyon
methodsandmetrics.Electronics8(2019),832.https://doi.org/10.3390/electronics8080832
[57] Lenart Celar and Ruth M. J. Byrne. 2023. How people reason with counterfactual and causal explanations for
artificialintelligencedecisionsinfamiliarandunfamiliardomains.Memory&Cognition51,7(2023),1481–1496.
https://doi.org/10.3758/s13421-023-01407-5
[58] CFPB. [n. d.]. Adverse Action Notice Requirements Under the ECOA and the FCRA. https://
consumercomplianceoutlook.org/2013/second-quarter/adverse-action-notice-requirements-under-ecoa-fcra/.
Accessed:2020-10-15.
[59] CFPB. [n. d.]. Notification of Action Taken, ECOA Notice, and Statement of Specific Reasons. https://www.
consumerfinance.gov/policy-compliance/rulemaking/regulations/1002/9/.Accessed:2020-10-15.
[60] QianglongChen,FengJi,XiangjiZeng,Feng-LinLi,JiZhang,HaiqingChen,andYinZhang.2021.KACE:Gen-
eratingknowledgeawarecontrastiveexplanationsfornaturallanguageinference.InProceedingsofthe59thAn-
nualMeetingoftheAssociationforComputationalLinguisticsandthe11thInternationalJointConferenceonNatu-
ralLanguageProcessing.AssociationforComputationalLinguistics,Online,2516–2527.https://doi.org/10.18653/v1/
2021.acl-long.196
[61] TsongYuehChen,Fei-ChingKuo,HuaiLiu,Pak-LokPoon,DaveTowey,T.H.Tse,andZhiQuanZhou.2018.Meta-
morphictesting:Areviewofchallengesandopportunities.ACMComput.Surv.51,1(2018),27.https://doi.org/
10.1145/3143561
[62] Yatong Chen, Jialu Wang, and Yang Liu. 2020. Strategic Recourse in Linear Classification. https:
//dynamicdecisions.github.io
[63] ZihengChen,FabrizioSilvestri,JiaWang,HeZhu,HongshikAhn,andGabrieleTolomei.2021.ReLAX:Reinforce-
mentLearningAgenteXplainerforArbitraryPredictiveModels.https://doi.org/10.48550/ARXIV.2110.11960
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:29
[64] FuruiCheng,YaoMing,andHuaminQu.2020.DECE:DecisionExplorerwithCounterfactualExplanationsforMa-
chineLearningModels.arXiv:cs.LG/2008.08353
[65] NoelCodella,VeronicaRotemberg,PhilippTschandl,M.EmreCelebi,StephenDusza,DavidGutman,BrianHelba,
AadiKalloo,KonstantinosLiopyris,MichaelMarchetti,HaraldKittler,andAllanHalpern.2019.SkinLesionAnalysis
TowardMelanomaDetection2018:AChallengeHostedbytheInternationalSkinImagingCollaboration(ISIC).https:
//doi.org/10.48550/ARXIV.1902.03368
[66] GregoryCohen,SaeedAfshar,JonathanC.Tapson,andAndrévanSchaik.2017.EMNIST:ExtendingMNISTto
handwrittenletters.InProceedingsofthe2017InternationalJointConferenceonNeuralNetworks(IJCNN) (2017),
2921–2926.https://doi.org/10.1109/IJCNN.2017.7966217
[67] European Commission. [n. d.]. Artificial Intelligence. https://ec.europa.eu/info/funding-tenders/opportunities/
portal/screen/opportunities/topic-details/ict-26-2018-2020.Accessed:2020-10-15.
[68] EuropeanCommission.[n.d.].REGULATION(EU)2016/679OFTHEEUROPEANPARLIAMENTANDOFTHE
COUNCILof27April2016ontheProtectionofNaturalPersonswithRegardtotheProcessingofPersonalData
andontheFreeMovementofSuchData,andRepealingDirective95/46/EC(GeneralDataProtectionRegulation).
https://eur-lex.europa.eu/eli/reg/2016/679/oj.Accessed:2020-10-15.
[69] ZicunCong,LingyangChu,YuYang,andJianPei.2021.ComprehensiblecounterfactualexplanationonKolmogorov-
Smirnovtest.Proc.VLDBEndow.14,9(2021),1583–1596.https://doi.org/10.14778/3461535.3461546
[70] MichaelCorrell.2019.Ethicaldimensionsofvisualizationresearch.InProceedingsof CHI’19.ACM,NewYork„13.
https://doi.org/10.1145/3290605.3300418
[71] PauloCortez.2014.StudentPerformance.UCIMachineLearningRepository.https://doi.org/10.24432/C5TG7T
[72] MarkW.CravenandJudeW.Shavlik.1995.Extractingtree-structuredrepresentationsoftrainednetworks.InPro-
ceedingsofthe8thInternationalConferenceonNeuralInformationProcessingSystems(NIPS’95).MITPress,Cambridge,
MA,USA,24–30.
[73] RiccardoCrupi,BeatrizSanMiguelGonzález,AlessandroCastelnovo,andDanieleRegoli.2022.Leveragingcausal
relationstoprovidecounterfactualexplanationsandfeasiblerecommendationstoendusers.InProceedingsofthe
14thInternationalConferenceonAgentsandArtificialIntelligence-Volume2:ICAART,.SciTePress,24–32.https://
doi.org/10.5220/0010761500003116
[74] XinyueDai,MarkT.Keane,LaurenceShalloo,ElodieRuelle,andRuthM.J.Byrne.2022.Counterfactualexplanations
forpredictionanddiagnosisinXAI.InProceedingsofthe2022AAAI/ACMConferenceonAI,Ethics,andSociety(AIES
’22).ACM,NewYork„12.https://doi.org/10.1145/3514094.3534144
[75] SusanneDandl,ChristophMolnar,MartinBinder,andBerndBischl.2020.Multi-objectivecounterfactualexplana-
tions.InProceedingsofPPSNXVI.SpringerInternationalPublishing,Cham,448–469.https://doi.org/10.1007/978-3-
030-58112-131
[76] DARPA.[n.d.].BroadAgencyAnnouncement:ExplainableArtificialIntelligence(XAI).https://www.darpa.mil/
attachments/DARPA-BAA-16-53.pdf.Accessed:2020-10-15.
[77] SaloniDash,VineethNBalasubramanian,andAmitSharma.2022.Evaluatingandmitigatingbiasinimageclassi-
fiers:Acausalperspectiveusingcounterfactuals.InProceedingsoftheIEEE/CVFWinterConferenceonApplications
ofComputerVision(WACV’22).915–924.https://doi.org/10.1109/WACV51458.2022.00393
[78] A.Datta,S.Sen,andY.Zick.2016.Algorithmictransparencyviaquantitativeinputinfluence:Theoryandexperi-
mentswithlearningsystems.InProceedingsof2016IEEESymposiumonSecurityandPrivacy(SP’16).IEEE,NewYork,
,598–617.https://doi.org/10.1109/SP.2016.42
[79] LucasdeLara,AlbertoGonzález-Sanz,NicholasAsher,andJean-MichelLoubes.2021.Transport-basedCounterfac-
tualModels.https://doi.org/10.48550/ARXIV.2108.13025
[80] GiovanniDeToni,BrunoLepri,andAndreaPasserini.2022.SynthesizingExplainableCounterfactualPoliciesfor
AlgorithmicRecoursewithProgramSynthesis.https://doi.org/10.48550/ARXIV.2201.07135
[81] Sarah Dean, Sarah Rich, and Benjamin Recht. 2020. Recommendations and user agency: The reachability of
collaboratively-filteredinformation.InProceedingsof FAT*’20.ACM,NewYork,10.https://doi.org/10.1145/3351095.
3372866
[82] EoinDelaney,DerekGreene,andMarkT.Keane.2021.Instance-basedcounterfactualexplanationsfortimeseries
classification.InProceedingsofthe29thInternationalConferenceonCase-BasedReasoningResearchandDevelopment
(ICCBR2021),(Salamanca,Spain,September13–16,2021).,.Springer-Verlag,Berlin,,32–47.https://doi.org/10.1007/
978-3-030-86957-13
[83] EoinDelaney,DerekGreene,andMarkT.Keane.2021.UncertaintyEstimationandOut-of-DistributionDetection
forCounterfactualExplanations:PitfallsandSolutions.https://arxiv.org/abs/2107.09734
[84] EoinDelaney,ArjunPakrashi,DerekGreene,andMarkT.Keane.2023.Counterfactualexplanationsformisclassi-
fiedimages:Howhumanandmachineexplanationsdiffer.ArtificialIntelligence324(2023),103995.https://doi.org/
10.1016/j.artint.2023.103995
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:30 S.Vermaetal.
[85] HoutaoDeng.2014.InterpretingtreeensembleswithinTrees.arXiv:1408.5456 (082014).https://doi.org/10.1007/
s41060-018-0144-8
[86] JiaDeng,WeiDong,RichardSocher,Li-JiaLi,KaiLi,andLiFei-Fei.2009.ImageNet:Alarge-scalehierarchical
imagedatabase.InProceedingsofthe2009IEEEConferenceonComputerVisionandPatternRecognition.248–255.
https://doi.org/10.1109/CVPR.2009.5206848
[87] AmitDhurandhar,Pin-YuChen,RonnyLuss,Chun-ChenTu,PaishunTing,KarthikeyanShanmugam,andPayelDas.
2018.Explanationsbasedonthemissing:Towardscontrastiveexplanationswithpertinentnegatives.InProceedings
oftheNeurIPS2018.CurranAssociatesInc.,590–601.
[88] AmitDhurandhar,TejaswiniPedapati,AvinashBalakrishnan,Pin-YuChen,KarthikeyanShanmugam,andRuchir
Puri.2019.ModelAgnosticContrastiveExplanationsforStructuredData.http://arxiv.org/abs/1906.00117
[89] EdsgerWDijkstra.1959.Anoteontwoproblemsinconnexionwithgraphs.NumerischeMathematik1,1(1959),
269–271.
[90] JonathanDodge,Q.VeraLiao,YunfengZhang,RachelK.E.Bellamy,andCaseyDugan.2019.Explainingmodels:
Anempiricalstudyofhowexplanationsimpactfairnessjudgment.InProceedingsofIUI2019.ACM,NewYork,11.
https://doi.org/10.1145/3301275.3302310
[91] CarlDoersch.2016.TutorialonVariationalAutoencoders.arXiv:stat.ML/1606.05908
[92] PedroDomingos.1998.Knowledgediscoveryviamultiplemodels.Intell.DataAnal.2,3(May1998),187–202.
[93] RicardoDominguez-Olmedo,AmirH.Karimi,andBernhardSchölkopf.2022.Ontheadversarialrobustnessofcausal
algorithmicrecourse.InProceedingsofthe39thInternationalConferenceonMachineLearning.PMLR,5324–5342.
https://proceedings.mlr.press/v162/dominguez-olmedo22a.html
[94] FinaleDoshi-Velez,MasonKortz,RyanBudish,ChrisBavitz,SamGershman,D.O’Brien,StuartSchieber,J.Waldo,
D.Weinberger,andAlexandraWood.2017.AccountabilityofAIUndertheLaw:TheRoleofExplanation.https://
doi.org/10.2139/ssrn.3064761
[95] MichaelDowns,JonathanChu,YanivYacoby,FinaleDoshi-Velez,andWeiwei.Pan.2020.CRUDS:Counterfactual
recourseusingdisentangledsubspaces.InProceedingsoftheWorkshoponHumanInterpretabilityinMachineLearn-
ing (WHI’20). https://finale.seas.harvard.edu/files/finale/files/cruds-_counterfactual_recourse_using_disentangled_
subspaces.pdf
[96] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository-AdultIncome.http://archive.ics.uci.edu/
ml/datasets/Adult
[97] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository-BreastCancer.https://archive.ics.uci.edu/
ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
[98] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository-Iris.https://archive.ics.uci.edu/ml/datasets/
iris
[99] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository-Shopping.https://archive.ics.uci.edu/ml/
datasets/Online+Shoppers+Purchasing+Intention+Dataset
[100] Dheeru Dua and Casey Graff. 2017. UCI Machine Learning Repository - Wine. https://archive.ics.uci.edu/ml/
datasets/wine
[101] JannikDunkelauandMichaelLeuschel.2019.Fairness-AwareMachineLearning.60pages.https://www.phil-fak.uni-
duesseldorf.de/fileadmin/Redaktion/Institute/Sozialwissenschaften/Kommunikations-_und_Medienwissenschaft/
KMW_I/Working_Paper/Dunkelau___Leuschel__2019__Fairness-Aware_Machine_Learning.pdf
[102] TriDungDuong,QianLi,andGuandongXu.2021.Prototype-basedCounterfactualExplanationforCausalClassifi-
cation.https://doi.org/10.48550/ARXIV.2105.00703
[103] SanghamitraDutta,JasonLong,SaumitraMishra,CeciliaTilli,andDanieleMagazzeni.2022.Robustcounterfactual
explanationsfortree-basedensembles.InProceedingsofthe39thInternationalConferenceonMachineLearning.PMLR,
5742–5756.https://proceedings.mlr.press/v162/dutta22a.html
[104] Andrew Elliott, Stephen Law, and Chris Russell. 2021. Explaining classifiers using adversarial perturbations on
theperceptualball.InProceedingsoftheConferenceonComputerVisionandPatternRecognition(CVPR’21).https://
doi.org/10.48550/ARXIV.1912.09405
[105] LukasFaber,AminK.Moghaddam,andRogerWattenhofer.2020.ContrastiveGraphNeuralNetworkExplanation.
https://doi.org/10.48550/ARXIV.2010.13663
[106] DanielFaggella.2020.MachineLearningforMedicalDiagnostics–4CurrentApplications.https://emerj.com/ai-
sector-overviews/machine-learning-medical-diagnostics-4-current-applications/.Accessed:2020-10-15.
[107] JakeFawkes,RobinEvans,andDinoSejdinovic.2022.Selection,IgnorabilityandChallengeswithCausalFairness.
https://doi.org/10.48550/ARXIV.2202.13774
[108] J.A.Fdez-Sánchez,J.D.Pascual-Triana,A.Fernández,andF.Herrera.2021.Learninginterpretablemulti-classmod-
elsbymeansofhierarchicaldecomposition:Thresholdcontrolfornesteddichotomies.Neurocomputing463(2021),
514–524.https://doi.org/10.1016/j.neucom.2021.07.097
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:31
[109] AmirH.Feghahati,ChristianR.Shelton,MichaelJ.Pazzani,andKevinTang.2020.CDeepEx:Contrastivedeep
explanations.InProceedingsofECAI.
[110] Rubén R. Fernández, Isaac Martín de Diego, Víctor Aceña, Alberto Fernández-Isabel, and Javier M. Moguerza.
2020.Randomforestexplainabilityusingcounterfactualsets.InformationFusion63(2020),196–207.https://doi.org/
10.1016/j.inffus.2020.07.001
[111] CarlosFernández-Loría,FosterProvost,andXintianHan.2020.ExplainingData-DrivenDecisionsmadebyAISys-
tems:TheCounterfactualApproach.http://arxiv.org/abs/2001.07417
[112] AndreaFerrarioandMicheleLoi.2020.ASeriesofUnfortunateCounterfactualEvents:theRoleofTimeinCounter-
factualExplanations.https://doi.org/10.48550/ARXIV.2010.04687
[113] FICO.2018.FICO(HELOC)Dataset.https://community.fico.com/s/explainable-machine-learning-challenge?tabset-
3158a=2
[114] GiorgosFilandrianos,KonstantinosThomas,EdmundDervakos,andGiorgosStamou.2022.Conceptualeditsas
counterfactualexplanations(CEURWorkshopProceedings).CEUR-WS.org.http://ceur-ws.org/Vol-3121/paper6.pdf
[115] MaximilianFörster,PhilippHühn,MathiasKlier,andKilianKluge.2021.Capturingusers’reality:Anovelapproach
togeneratecoherentcounterfactualexplanations.https://doi.org/10.24251/HICSS.2021.155
[116] MaximilianFörster,MathiasKlier,KilianKluge,andIrinaSigler.2020.EvaluatingexplainableArtificalintelligence–
Whatusersreallyappreciate.(2020).https://aisel.aisnet.org/ecis2020rp/195
[117] MaximilianBecker,NadiaBurkart,PascalBirnstill,andJürgenBeyerer.2021.Asteptowardsglobalcounterfactual
explanations:Approximatingthefeaturespacethroughhierarchicaldivisionandgraphsearch.Adv.Artif.Intell.
Mach.Learn.1,2(2021),90–110.
[118] Timo Freiesleben. 2022. The intriguing relation between counterfactual explanations and adversarial examples.
MindsMach.(Dordr.)(2022),77–109.
[119] JeromeH.Friedman.2001.Greedyfunctionapproximation:Agradientboostingmachine.TheAnnalsofStatistics29,
5(2001),1189–1232.http://www.jstor.org/stable/2699986
[120] JörgFrohbergandFrankBinder.2022.CRASS:Anoveldatasetandbenchmarktotestcounterfactualreasoning
oflargelanguagemodels.InProceedingsoftheLanguageResourcesandEvaluationConference.EuropeanLanguage
ResourcesAssociation,Marseille,France,2126–2140.https://aclanthology.org/2022.lrec-1.229
[121] TakanoriFujiwara,XinhaiWei,JianZhao,andKwan-LiuMa.2022.Interactivedimensionalityreductionforcompar-
ativeanalysis.IEEETransactionsonVisualizationandComputerGraphics(2022),758–768.https://doi.org/10.1109/
tvcg.2021.3114807
[122] MaximilianFörster,PhilippHühn,MathiasKlier,andKilianKluge.2021.Capturingusers’reality:Anovelapproach
togeneratecoherentcounterfactualexplanations.https://doi.org/10.24251/HICSS.2021.155
[123] SainyamGalhotra,RomilaPradhan,andBabakSalimi.2021.Explainingblack-boxalgorithmsusingprobabilistic
contrastivecounterfactuals.In:ProceedingsoftheInternationalConferenceonManagementofData(SIGMOD’21),
(VirtualEvent,China,June20–25,2021.)ACM.https://doi.org/10.1145/3448016.3458455
[124] JingweiGan,ShinanZhang,ChiZhang,andAndyLi.2021.Automatedcounterfactualgenerationinfinancialmodel
riskmanagement.InProceedingsofthe2021IEEEInternationalConferenceonBigData(BigData).4064–4068.https://
doi.org/10.1109/BigData52589.2021.9671561
[125] P.J.García-Laencina,J.Sancho-Gómez,andA.R.Figueiras-Vidal.2009.Patternclassificationwithmissingdata:A
review.NeuralComputingandApplications19(2009),263–282.
[126] Gordon Garisch. [n. d.]. Model Lifecycle Transformation: How Banks Are Unlocking Efficiencies. https:
//financialservicesblog.accenture.com/model-lifecycle-transformation-how-banks-are-unlocking-efficiencies. Ac-
cessed:2022-10-15.
[127] YingqiangGe,ShuchangLiu,ZelongLi,ShuyuanXu,ShijieGeng,YunqiLi,JuntaoTan,FeiSun,andYongfengZhang.
2021.CounterfactualEvaluationforExplainableAI.https://doi.org/10.48550/ARXIV.2109.01962
[128] AsmaGhandeharioun,BeenKim,Chun-LiangLi,BrendanJou,BrianEoff,andRosalindPicard.2022.DISSECT:
Disentangledsimultaneousexplanationsviaconcepttraversals.InProceedingsoftheInternationalConferenceon
LearningRepresentations.https://openreview.net/forum?id=qY79G8jGsep
[129] AzinGhazimatin,OanaBalalau,RishirajSahaRoy,andGerhardWeikum.2020.PRINCE:Provider-sideinterpretabil-
ity with counterfactual explanations in recommender systems (WSDM ’20). ACM, NewYork, 9. https://doi.org/
10.1145/3336191.3371824
[130] GiorgosGiannopoulos,GeorgePapastefanatos,DimitrisSacharidis,andKostasStefanidis.2021.Interactivity,Fairness
andExplanationsinRecommendations.ACM.NewYork.https://doi.org/10.1145/3450614.3462238
[131] AlexGoldstein,AdamKapelner,JustinBleich,andEmilPitkin.2013.Peekinginsidetheblackbox:Visualizingsta-
tisticallearningwithplotsofindividualconditionalexpectation.JournalofComputationalandGraphicalStatistics
24(092013).https://doi.org/10.1080/10618600.2014.907095
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:32 S.Vermaetal.
[132] OscarGomez,SteffenHolter,JunYuan,andEnricoBertini.2020.ViCE:Visualcounterfactualexplanationsforma-
chinelearningmodels.InProceedingsof IUI’20.5.https://doi.org/10.1145/3377325.3377536
[133] OscarGomez,SteffenHolter,JunYuan,andEnricoBertini.2021.AdViCE:AggregatedVisualCounterfactualExpla-
nationsforMachineLearningModelValidation.https://doi.org/10.48550/ARXIV.2109.05629
[134] BryceGoodmanandS.Flaxman.2016.EUregulationsonalgorithmicdecision-makinganda“RighttoExplanation”.
ArXivabs/1606.08813(2016).
[135] YashGoyal,ZiyanWu,JanErnst,DhruvBatra,DeviParikh,andStefanLee.2019.Counterfactualvisualexplanations.
InProceedingsofICML2019.PMLR,2376–2384.https://proceedings.mlr.press/v97/goyal19a.html
[136] PrestonGralla.2016.AmazonPrimeandtheRacistAlgorithms.https://www.computerworld.com/article/3068622/
amazon-prime-and-the-racist-algorithms.html
[137] RoryMcGrath,LucaCostabello,ChanLeVan,PaulSweeney,FarbodKamiab,ZhaoShen,andFreddyLecue.2018.
InterpretableCreditApplicationPredictionswithCounterfactualExplanations.http://arxiv.org/abs/1811.05245
[138] HomeCreditGroup.2018.HomeCreditDefaultRisk.https://www.kaggle.com/c/home-credit-default-risk/data
[139] RiccardoGuidotti,AnnaMonreale,SalvatoreRuggieri,DinoPedreschi,FrancoTurini,andFoscaGiannotti.2018.
LocalRule-BasedExplanationsofBlackBoxDecisionSystems.http://arxiv.org/abs/1805.10820
[140] RiccardoGuidotti,AnnaMonreale,SalvatoreRuggieri,FrancoTurini,FoscaGiannotti,andDinoPedreschi.2018.
Asurveyofmethodsforexplainingblackboxmodels.ACMComput.Surv.51,5,Article93(Aug.2018),42pages.
https://doi.org/10.1145/3236009
[141] RiccardoGuidottiandSalvatoreRuggieri.2021.Ensembleofcounterfactualexplainers.Springer-Verlag,Berlin, 11.
https://doi.org/10.1007/978-3-030-88942-528
[142] SadafGulshadandArnoldSmeulders.2021.Counterfactualattribute-basedvisualexplanationsforclassification.
InternationalJournalofMultimediaInformationRetrieval(2021),127–140.https://doi.org/10.1007/s13735-021-00208-
3
[143] HangzhiGuo,ThanhHongNguyen,andAmulyaYadav.2021.CounterNet:End-to-EndTrainingofCounterfactual
AwarePredictions.https://doi.org/10.48550/ARXIV.2109.07557
[144] SharmiDevGupta,BegumGenc,andBarryO’Sullivan.2022.FindingCounterfactualExplanationsthroughCon-
straintRelaxations.https://doi.org/10.48550/ARXIV.2204.03429
[145] VivekGupta,PegahNokhiz,ChitradeepDuttaRoy,andSureshVenkatasubramanian.2019.EqualizingRecourse
AcrossGroups.https://arxiv.org/abs/1909.03166
[146] VictorGuyomard,FrançoiseFessant,TassaditBouadi,andThomasGuyet.2021.Post-hoccounterfactualgeneration
withsupervisedautoencoder.https://doi.org/10.1007/978-3-030-93736-210
[147] SuryabhanSinghHadaandMiguelÁ.Carreira-Perpiñán.2021.Exploringcounterfactualexplanationsforclassifi-
cationandregressiontrees.InMachineLearningandPrinciplesandPracticeofKnowledgeDiscoveryinDatabases.
SpringerInternationalPublishing,Cham,489–504.https://doi.org/10.1007/978-3-030-93736-237
[148] SwastikHaldar,PhilipsGeorgeJohn,andDiptikalyanSaha.2021.Reliablecounterfactualexplanationsforautoen-
coder based anomalies. In Proceedings of the 8th ACM IKDD CODS and 26th COMAD. ACM. New York, 83–91.
https://doi.org/10.1145/3430984.3431015
[149] Xing Han and Joydeep Ghosh. 2021. Model-agnostic explanations using minimal forcing subsets. In Proceed-
ings of the 2021 International Joint Conference on Neural Networks (IJCNN’21). 1–8. https://doi.org/10.1109/
IJCNN52387.2021.9533992
[150] MasoudHashemiandAliFathi.2020.PermuteAttack:CounterfactualExplanationofMachineLearningCreditScore-
cards.https://doi.org/10.48550/ARXIV.2008.10138
[151] LisaAnneHendricks,RonghangHu,TrevorDarrell,andZeynepAkata.2018.GeneratingCounterfactualExplana-
tionswithNaturalLanguage.https://doi.org/10.48550/ARXIV.1806.09809
[152] AndreasHenelius,KaiPuolamäki,HenrikBoström,LarsAsker,andPanagiotisPapapetrou.2014.Apeekintothe
blackbox:Exploringclassifiersbyrandomization.DataMin.Knowl.Discov.28,5-6(2014),27.https://doi.org/10.1007/
s10618-014-0368-8
[153] FabianHinderandBarbaraHammer.2020.CounterfactualExplanationsofConceptDrift.https://doi.org/10.48550/
ARXIV.2006.12822
[154] HansHofmann.1994.Statlog(GermanCreditData).UCIMachineLearningRepository.https://doi.org/10.24432/
C5NC77
[155] FredHohman,AndrewHead,RichCaruana,RobertDeLine,andStevenMarkDrucker.2019.Gamut:Adesignprobe
tounderstandhowdatascientistsunderstandmachinelearningmodels.InProceedingsofthe2019CHIConference
onHumanFactorsinComputingSystems(2019).
[156] WooSukHong,AdrianDanielHaimovich,andR.AndrewTaylor.2018.Predictinghospitaladmissionatemergency
departmenttriageusingmachinelearning.PlosOne13,7(2018).https://doi.org/10.1371/journal.pone.0201016
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:33
[157] ReeberErikFormanGeorgeHopkins,MarkandJaapSuermondt.1999.Spambase.UCIMachineLearningRepository.
https://doi.org/10.24432/C53G6X
[158] TheUSWhiteHouse.2022.BlueprintforanAIBillofRights.https://www.whitehouse.gov/ostp/ai-bill-of-rights/
#discrimination
[159] ChihchengHsieh,CatarinaMoreira,andChunOuyang.2021.DiCE4EL:Interpretingprocesspredictionsusinga
milestone-awarecounterfactualapproach.InProceedingsofthe20213rdInternationalConferenceonProcessMining
(ICPM’21).88–95.https://doi.org/10.1109/ICPM53251.2021.9576881
[160] Tsung-HaoHuang,AndreasMetzger,andKlausPohl.2022.Counterfactualexplanationsforpredictivebusinesspro-
cessmonitoring.SpringerInternationalPublishing,Cham,399–413.https://doi.org/10.1007/978-3-030-95947-028
[161] FrederikHvilshøj,AlexandrosIosifidis,andIraAssent.2021.ECINN:EfficientCounterfactualsfromInvertibleNeural
Networks.https://doi.org/10.48550/ARXIV.2103.13701
[162] FrederikHvilshøj,AlexandrosIosifidis,andIraAssent.2021.OnQuantitativeEvaluationsofCounterfactuals.https:
//doi.org/10.48550/ARXIV.2111.00177
[163] BenediktHöltgen,LisaSchut,JanM.Brauner,andYarinGal.2021.DeDUCE:GeneratingCounterfactualExplanations
Efficiently.https://doi.org/10.48550/ARXIV.2111.15639
[164] GlobalWomeninDataScienceConferenceTheGlobalOpenSourceSeverityofIllnessScoreConsortium.2020.WiDS
Datathon2020.https://www.kaggle.com/c/widsdatathon2020
[165] AllstateInsurance.2011.AllstateClaimPredictionChallenge.https://www.kaggle.com/c/ClaimPredictionChallenge
[166] FranceIntelligenceArtificielle.[n.d.].RapportdeSyntheseFranceIntelligenceArtificielle.https://www.economie.
gouv.fr/files/files/PDF/2017/Rapport_synthese_France_IA_.pdf.Accessed:2020-10-15.
[167] JeremyIrvin,PranavRajpurkar,MichaelKo,YifanYu,SilvianaCiurea-Ilcus,ChrisChute,HenrikMarklund,Behzad
Haghgoo,RobynBall,KatieShpanskaya,JayneSeekins,DavidA.Mong,SafwanS.Halabi,JesseK.Sandberg,Ricky
Jones,DavidB.Larson,CurtisP.Langlotz,BhavikN.Patel,MatthewP.Lungren,andAndrewY.Ng.2019.CheX-
pert:ALargeChestRadiographDatasetwithUncertaintyLabelsandExpertComparison.https://doi.org/10.48550/
ARXIV.1901.07031
[168] PaulJacob,ÉloiZablocki,HédiBen-Younes,MickaëlChen,PatrickPérez,andMatthieuCord.[n.d.].STEEX:Steering
CounterfactualExplanationswithSemantics.https://doi.org/10.48550/ARXIV.2111.09094
[169] GuillaumeJeanneret,LoïcSimon,andFrédéricJurie.2022.DiffusionModelsforCounterfactualExplanations.https://
doi.org/10.48550/ARXIV.2203.15636
[170] Lauren Kirchner Jeff Larson, Surya Mattu and Julia Angwin. 2016. UCI Machine Learning Repository. https://
github.com/propublica/compas-analysis/
[171] YanJia,JohnMcDermid,andIbrahimHabli.2021.Enhancingthevalueofcounterfactualexplanationsfordeep
learning.InArtificialIntelligenceinMedicine.SpringerInternationalPublishing,Cham,389–394.https://doi.org/
10.1007/978-3-030-77211-646
[172] AlistairJohnson,LucasBulgarelli,TomPollard,StevenHorng,LeoAnthonyCeli,andRogerMark.2021.MIMIC-IV.
https://doi.org/10.13026/S6N6-XD98
[173] Kareem L. Jordan and Tina L. Freiburger. 2015. The effect of race/ethnicity on sentencing: Examining sentence
type,jaillength,andprisonlength.JournalofEthnicityinCriminalJustice 13,3(2015).https://doi.org/10.1080/
15377938.2014.984045
[174] ShalmaliJoshi,OluwasanmiKoyejo,WarutVijitbenjaronk,BeenKim,andJoydeepGhosh.2019.TowardsRealis-
ticIndividualRecourseandActionableExplanationsinBlack-BoxDecisionMakingSystems.http://arxiv.org/abs/
1907.09615
[175] Hong-GyuJung,Sin-HanKang,Hee-DongKim,Dong-OkWon,andSeong-WhanLee.2020.CounterfactualExpla-
nationBasedonGradualConstructionforDeepNetworks.https://doi.org/10.48550/ARXIV.2008.01897
[176] VassilisKaffes,DimitrisSacharidis,andGiorgosGiannopoulos.2021.Model-agnosticcounterfactualexplanationsof
recommendations(UMAP’21).ACM.NewYork,6.https://doi.org/10.1145/3450613.3456846
[177] Kaggle.2012.GiveMeSomeCredit.https://www.kaggle.com/c/GiveMeSomeCredit
[178] D.KahnemanandD.Miller.1986.Normtheory:Comparingrealitytoitsalternatives.PsychologicalReview93(1986),
136–153.
[179] KentaroKanamori,TakuyaTakagi,KenKobayashi,andHirokiArimura.2020.DACE:Distribution-awarecounterfac-
tualexplanationbymixed-integerlinearoptimization.InProceedingsoftheInternationalJointConferenceonArtificial
Intelligence(IJCAI’20).https://doi.org/10.24963/ijcai.2020/395
[180] KentaroKanamori,TakuyaTakagi,KenKobayashi,andYuichiIke.2022.Counterfactualexplanationtrees:Trans-
parentandconsistentactionablerecoursewithdecisiontree.InProceedingsofMachineLearningResearch(PMLR),
1846–1870.
[181] KentaroKanamori,TakuyaTakagi,KenKobayashi,YuichiIke,KentoUemura,andHirokiArimura.2021.Ordered
counterfactualexplanationbymixed-integerlinearoptimization.InProceedingsoftheAAAIConferenceonArtificial
Intelligence(2021),11.https://doi.org/10.1609/aaai.v35i13.17376
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:34 S.Vermaetal.
[182] A.-H.Karimi,G.Barthe,B.Balle,andI.Valera.2020.Model-AgnosticCounterfactualExplanationsforConsequential
Decisions.http://arxiv.org/abs/1905.11190
[183] Amir-HosseinKarimi,BernhardSchölkopf,andIsabelValera.2021.Algorithmicrecourse:Fromcounterfactualexpla-
nationstointerventions.InProceedingsofFAccT’21.ACM,NewYork,10.https://doi.org/10.1145/3442188.3445899
[184] Amir-HosseinKarimi,JuliusvonKügelgen,BernhardSchölkopf,andIsabelValera.2020.AlgorithmicRecourseunder
ImperfectCausalKnowledge:AProbabilisticApproach.http://arxiv.org/abs/2006.06831
[185] IsakKarlsson,JonathanRebane,PanagiotisPapapetrou,andAristidesGionis.2020.Locallyandgloballyexplainable
timeseriestweaking.Knowl.Inf.Syst.(2020),30.https://doi.org/10.1007/s10115-019-01389-4
[186] AtoosaKasirzadehandAndrewSmart.2021.Theuseandmisuseofcounterfactualsinethicalmachinelearning.In
Proceedingsofthe2021ACMConferenceonFairness,Accountability,andTransparency.ACM,NewYork,9.https://
doi.org/10.1145/3442188.3445886
[187] MarkT.Keane,EoinM.Kenny,EoinDelaney,andBarrySmyth.2021.Ifonlywehadbettercounterfactualexpla-
nations:FivekeydeficitstorectifyintheevaluationofcounterfactualXAItechniques.CoRR(2021).https://arxiv.
org/abs/2103.01035
[188] MarkT.KeaneandBarrySmyth.2020.GoodCounterfactualsandWheretoFindThem:ACase-BasedTechniquefor
GeneratingCounterfactualsforExplainableAI(XAI).arXiv:cs.AI/2005.13997
[189] EoinKennyandWeipengHuang.2023.Theutilityof“Evenif”semifactualexplanationtooptimisepositiveoutcomes.
InAdvancesinNeuralInformationProcessingSystems,A.Oh,T.Naumann,A.Globerson,K.Saenko,M.Hardt,and
S.Levine(Eds.),Vol.36.CurranAssociates,Inc.,52907–52935.https://proceedings.neurips.cc/paperfiles/paper/2023/
file/a5e146ca55a2b18be41942cfa677123d-Paper-Conference.pdf
[190] EoinM.KennyandMarkT.Keane.2020.OnGeneratingPlausibleCounterfactualandSemi-FactualExplanationsfor
DeepLearning.arXiv:2009.06399
[191] EoinM.KennyandMarkTKeane.2021.Ongeneratingplausiblecounterfactualandsemi-factualexplanationsfor
deeplearning.InProceedingsoftheAAAIConferenceonArtificialIntelligence35(May2021),11.https://ojs.aaai.org/
index.php/AAAI/article/view/17377
[192] SaeedKhorramandLiFuxin.2022.Cycle-consistentcounterfactualsbylatenttransformations.InProceedingsofthe
IEEE/CVFConferenceonComputerVisionandPatternRecognition(CVPR’22).10.
[193] BeenKim,RajivKhanna,andOluwasanmiO.Koyejo.2016.Examplesarenotenough,learntocriticize!criticismfor
interpretability.InAdvancesinNeuralInformationProcessingSystems,D.Lee,M.Sugiyama,U.Luxburg,I.Guyon,
and R. Garnett (Eds.), Vol. 29. Curran Associates, Inc. https://proceedings.neurips.cc/paperfiles/paper/2016/file/
5680522b8e2bb01943234bce7bf84534-Paper.pdf
[194] BorisKment.2006.Counterfactualsandexplanation.Mind115(2006).https://doi.org/10.1093/mind/fzl261
[195] WillKnight.2019.TheAppleCardDidn’t’See’Gender-andThat’stheProblem.https://www.wired.com/story/the-
apple-card-didnt-see-genderand-thats-the-problem/
[196] RamaravindKommiyaMothilal,DivyatMahajan,ChenhaoTan,andAmitSharma.2021.TowardsUnifyingFeature
AttributionandCounterfactualExplanations:DifferentMeanstotheSameEnd.ACM,NewYork.
[197] JaehoonKoo,DiegoKlabjan,andJeanUtke.2020.InverseClassificationwithLimitedBudgetandMaximumNumber
ofPerturbedSamples.https://doi.org/10.48550/ARXIV.2009.14111
[198] TaraKoopmanandSiljaRenooij.2021.PersuasivecontrastiveexplanationsforBayesiannetworks.InSymbolicand
QuantitativeApproachestoReasoningwithUncertainty.SpringerInternationalPublishing,Cham,229–242.https://
doi.org/10.1007/978-3-030-86772-0_17
[199] AntonKorikovandJ.ChristopherBeck.2021.Counterfactualexplanationsviainverseconstraintprogramming.In
Proceedingsofthe27thInternationalConferenceonPrinciplesandPracticeofConstraintProgramming(CP’21),Vol.210.
SchlossDagstuhl–Leibniz-ZentrumfürInformatik.https://doi.org/10.4230/LIPIcs.CP.2021.35
[200] AntonKorikov,AlexanderShleyfman,andJ.ChristopherBeck.2021.Counterfactualexplanationsforoptimization-
based decisions in the context of the GDPR. In Proceedings of IJCAI-21. 4097–4103. https://doi.org/10.24963/
ijcai.2021/564
[201] MaximKovalev,LevUtkin,FrankCoolen,andAndreiKonstantinov.2021.Counterfactualexplanationofmachine
learningsurvivalmodels.Informatica(2021),817–847.https://doi.org/10.15388/21-INFOR468
[202] R.Krishnan,G.Sivakumar,andP.Bhattacharya.1999.Extractingdecisiontreesfromtrainedneuralnetworks.Pattern
Recognition32,12(1999),1999–2009.https://doi.org/10.1016/S0031-3203(98)00181-2
[203] SanjayKrishnanandEugeneWu.2017.PALM:Machinelearningexplanationsforiterativedebugging.InProceedings
of HILDA’17.ACM.NewYork,6.https://doi.org/10.1145/3077257.3077271
[204] UlrikeKuhl,AndréArtelt,andBarbaraHammer.2022.Keepyourfriendscloseandyourcounterfactualscloser:
Improved learning from closest rather than plausible counterfactual explanations in an abstract setting. ArXiv
abs/2205.05515(2022).
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:35
[205] MattJ.Kusner,JoshuaLoftus,ChrisRussell,andRicardoSilva.2017.Counterfactualfairness.AdvancesinNeural
InformationProcessingSystems30(2017).
[206] GunnarKönig,TimoFreiesleben,andMoritzGrosse-Wentrup.2021.ACausalPerspectiveonMeaningfulandRobust
AlgorithmicRecourse.https://doi.org/10.48550/ARXIV.2107.07853
[207] JokinLabaien,EkhiZugasti,andXabierDeCarlos.2021.DA-DGCEx:EnsuringValidityofDeepGuidedCounterfac-
tualExplanationswithDistribution-AwareAutoencoderLoss.https://doi.org/10.48550/ARXIV.2104.09062
[208] MichaelT.Lash,QihangLin,WilliamNickStreet,JenniferG.Robinson,andJeffreyW.Ohlmann.2017.General-
izedinverseclassification.InProceedingsofSDM.SocietyforIndustrialandAppliedMathematics,Philadelphia,PA,
162–170.https://doi.org/10.1137/1.9781611974973.19
[209] ThibaultLaugel,Marie-JeanneLesot,ChristopheMarsala,andMarcinDetyniecki.2019.IssueswithPost-hocCoun-
terfactualExplanations:ADiscussion.arXiv:1906.04774
[210] ThibaultLaugel,Marie-JeanneLesot,ChristopheMarsala,XavierRenard,andMarcinDetyniecki.2018.Comparison-
basedinverseclassificationforinterpretabilityinmachinelearning.InProceedingsofInformationProcessingand
ManagementofUncertaintyinKnowledge-BasedSystems,TheoryandFoundations(IPMU’18).SpringerInternational
Publishing.https://doi.org/10.1007/978-3-319-91473-29
[211] ThibaultLaugel,Marie-JeanneLesot,ChristopheMarsala,XavierRenard,andMarcinDetyniecki.2019.TheDangers
ofPost-hocInterpretability:UnjustifiedCounterfactualExplanations.http://arxiv.org/abs/1907.09294
[212] ThaiLe,SuhangWang,andDongwonLee.2019.GRACE:GeneratingConciseandInformativeContrastiveSample
toExplainNeuralNetworkModel’sPrediction.arXiv:cs.LG/1911.02042
[213] Yann LeCun and Corinna Cortes. 2010. MNIST handwritten digit database. (2010). http://yann.lecun.com/exdb/
mnist/
[214] CarsonK.Leung,AdamG.M.Pazdor,andJoglasSouza.2021.Explainableartificialintelligencefordatascienceon
customerchurn.InProceedingsofthe2021IEEE8thInternationalConferenceonDataScienceandAdvancedAnalytics
(DSAA’21).1–10.https://doi.org/10.1109/DSAA53316.2021.9564166
[215] DavidLewis.1973.Counterfactuals.BlackwellPublishers,Oxford.
[216] DanLey,SaumitraMishra,andDanieleMagazzeni.2022.Globalcounterfactualexplanations:Investigations,im-
plementationsandimprovements.InProceedingsoftheICLRWorkshoponPrivacy,Accountability,Interpretability,
Robustness,ReasoningonStructuredData.
[217] Yan Li, Shasha Liu, Chunwei Wu, Xidong Xi, Guitao Cao, and Wenming Cao. 2021. DCFG: Discovering direc-
tionalCounterFactualgenerationforchestX-rays.InProceedingsofBIBM2021.972–979.https://doi.org/10.1109/
BIBM52615.2021.9669770
[218] ShusenLiu,BhavyaKailkhura,DonaldLoveland,andYongHan.2019.Generativecounterfactualintrospectionfor
explainabledeeplearning.InProceedingsofthe2019IEEEGlobalConferenceonSignalandInformationProcessing
(GlobalSIP’19).1–5.https://doi.org/10.1109/GlobalSIP45357.2019.8969491
[219] ZiweiLiu,PingLuo,XiaogangWang,andXiaoouTang.2014.Deeplearningfaceattributesinthewild.(112014).
https://doi.org/10.1109/ICCV.2015.425
[220] AnaLucic,HindaHaned,andMaartendeRijke.2020.Whydoesmymodelfail?Contrastivelocalexplanationsfor
retailforecasting.InProceedingsofthe2020ConferenceonFairness,Accountability,andTransparency.ACM,New
York,9.https://doi.org/10.1145/3351095.3372824
[221] AnaLucic,HarrieOosterhuis,HindaHaned,andMaartendeRijke.2019.FOCUS:FlexibleOptimizableCounterfac-
tualExplanationsforTreeEnsembles.https://doi.org/10.48550/ARXIV.1911.12199
[222] AnaLucic,HarrieOosterhuis,HindaHaned,andMaartendeRijke.2020.ActionableInterpretabilitythroughOpti-
mizableCounterfactualExplanationsforTreeEnsembles.http://arxiv.org/abs/1911.12199
[223] AnaLucic,MaartjeterHoeve,GabrieleTolomei,MaartendeRijke,andFabrizioSilvestri.2021.CF-GNNExplainer:
CounterfactualExplanationsforGraphNeuralNetworks.arXiv:cs.LG/2102.03322
[224] ScottM.LundbergandSu-InLee.2017.Aunifiedapproachtointerpretingmodelpredictions.InAdvancesinNeural
InformationProcessingSystems30.CurranAssociates,Inc.,4765–4774.
[225] FreddieMac.2019.SingleFamilyLoan-levelDataset.https://www.freddiemac.com/research/datasets/sf-loanlevel-
dataset
[226] NishthaMadaan,InkitPadhi,NaveenPanwar,andDiptikalyanSaha.2021.Generateyourcounterfactuals:Towards
controlledcounterfactualgenerationfortext.InProceedingsoftheAAAIConferenceonArtificialIntelligence35(May
2021),13516–13524.https://ojs.aaai.org/index.php/AAAI/article/view/17594
[227] Fannie Mae. 2020. Fannie Mae Dataset. https://www.fanniemae.com/portal/funding-the-market/data/loan-
performance-data.html
[228] AlessandroMagrini,StefanodiBlasi,andFedericoStefanini.2017.AconditionallinearGaussiannetworktoassess
theimpactofseveralagronomicsettingsonthequalityofTuscanSangiovesegrapes.BiometricalLetters54(062017),
25–42.https://doi.org/10.1515/bile-2017-0002
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:36 S.Vermaetal.
[229] DivyatMahajan,ChenhaoTan,andAmitSharma.2020.PreservingCausalConstraintsinCounterfactualExplana-
tionsforMachineLearningClassifiers.http://arxiv.org/abs/1912.03277
[230] GuilhermeF.Marchezini,AnisioM.Lacerda,GiseleL.Pappa,WagnerMeira,Jr.,DeboraMiranda,MarcoA.Romano-
Silva,DanielleS.Costa,andLeandroMalloyDiniz.2022.Counterfactualinferencewithlatentvariableanditsapplica-
tioninmentalhealthcare.DataMin.Knowl.Discov.36(2022),811–840.https://doi.org/10.1007/s10618-021-00818-9
[231] DavidMartensandFosterJ.Provost.2014.Explainingdata-drivendocumentclassifications.MISQ.38(2014),73–99.
https://doi.org/10.25300/MISQ/2014/38.1.04
[232] RaphaelMazzine,SofieGoethals,DieterBrughmans,andDavidMartens.2021.Counterfactualexplanationsforem-
ploymentservices.InProceedingsoftheInternationalWorkshoponFair,EffectiveandSustainableTalentManagement
usingDataScience.1–7.
[233] RaphaelMazzineandDavidMartens.2021.AFrameworkandBenchmarkingStudyforCounterfactualGenerating
MethodsonTabularData.https://doi.org/10.48550/ARXIV.2107.04680
[234] MarcosMedeirosRaimundo,LuisNonato,andJorgePoco.2021.MiningPareto-OptimalCounterfactualAntecedents
withaBranch-And-BoundModel-AgnosticAlgorithm.https://doi.org/10.21203/rs.3.rs-551661/v1
[235] Md. Golam Moula Mehedi Hasan and Douglas Talbert. 2022. Data augmentation using counterfactuals: Prox-
imity vs. diversity. In The International FLAIRS Conference Proceedings 35 (May 2022). https://doi.org/10.32473/
flairs.v35i.130705
[236] Md.GolamMoulaMehediHasanandDouglasTalbert.2022.MitigatingtheRashomoneffectincounterfactualex-
planation:Agame-theoreticapproach.InTheInternationalFLAIRSConferenceProceedings35(2022).https://doi.org/
10.32473/flairs.v35i.130711
[237] Silvan Mertes, Tobias Huber, Katharina Weitz, Alexander Heimerl, and Elisabeth André. 2022. GANterfactual–
counterfactualexplanationsformedicalnon-expertsusinggenerativeadversariallearning.FrontiersinArtificial
Intelligence5(2022).https://doi.org/10.3389/frai.2022.825565
[238] TimMiller.2019.Explanationinartificialintelligence:Insightsfromthesocialsciences.ArtificialIntelligence(2019),
1–38.https://doi.org/10.1016/j.artint.2018.07.007
[239] SaumitraMishra,SanghamitraDutta,JasonLong,andDanieleMagazzeni.2021.ASurveyontheRobustnessof
FeatureImportanceandCounterfactualExplanations.https://doi.org/10.48550/ARXIV.2111.00358
[240] TakayukiMiura,SatoshiHasegawa,andToshikiShibahara.2021.MEGEX:Data-freemodelextractionattackagainst
gradient-basedexplainableAI.ArXivabs/2107.08909(2021).
[241] Kiarash Mohammadi, Amir-Hossein Karimi, Gilles Barthe, and Isabel Valera. 2021. Scaling guarantees for near-
estcounterfactualexplanations.InProceedingsoftheACMConferenceonAI,Ethics,andSociety.ACM,NewYork,
177–187.https://doi.org/10.1145/3461702.3462514
[242] WellingtonRodrigoMonteiroandGilbertoReynoso-Meza.2022.Counterfactualgenerationthroughmulti-objective
constrainedoptimisation.(2022),23.https://www.researchsquare.com/article/rs-1325730/v1
[243] SérgioMoro,PauloCortez,andPauloRita.2014.Adata-drivenapproachtopredictthesuccessofbanktelemarketing.
DecisionSupportSystems62(2014),22–31.https://doi.org/10.1016/j.dss.2014.03.001
[244] RamaravindK.Mothilal,AmitSharma,andChenhaoTan.2020.Explainingmachinelearningclassifiersthrough
diversecounterfactualexplanations.InProceedingsoftheConferenceonFairness,Accountability,andTransparency
(FAccT’20)(FAT*’20).ACM,NewYork,https://doi.org/10.1145/3351095.3372850
[245] SusanneG.Mueller,MichaelW.Weiner,LeonJ.Thal,RonaldC.Petersen,CliffordJack,WilliamJagust,JohnQ.
Trojanowski,ArthurW.Toga,andLaurelBeckett.2008.Alzheimer’sdiseaseneuroimaginginitiative.InAdvancesin
Alzheimer’sandParkinson’sDisease.SpringerUS,183–189.https://doi.org/10.1007/978-0-387-72076-018
[246] ChelseaM.Myers,EvanFreed,LuisFernandoLarisPardo,AnushayFurqan,SebastianRisi,andJichenZhu.2020.
Revealing Neural Network Bias to Non-Experts Through Interactive Counterfactual Examples. https://doi.org/
10.48550/ARXIV.2001.02271
[247] Philip Naumann and Eirini Ntoutsi. 2021. Consequence-aware Sequential Counterfactual Generation.
arXiv:cs.LG/2104.05592
[248] GuillermoNavas-Palencia.2021.OptimalCounterfactualExplanationsforScorecardModelling.https://arxiv.org/
abs/2104.08619
[249] DanielNemirovsky,NicolasThiebaut,YeXu,andAbhishekGupta.2021.Providingactionablefeedbackinhiring
marketplaces using generative adversarial networks. In Proceedings of WSDM 2021. ACM, New York, 4. https://
doi.org/10.1145/3437963.3441705
[250] DanielNemirovsky,NicolasThiebaut,YeXu,andAbhishekGupta.2022.CounteRGAN:Generatingcounterfactuals
forreal-timerecourseandinterpretabilityusingresidualGANs.InProceedingsofUAI2022.PMLR,1488–1497.https://
proceedings.mlr.press/v180/nemirovsky22a.html
[251] TriMinhNguyen,ThomasP.Quinn,ThinNguyen,andTruyenTran.2021.CounterfactualExplanationwithMulti-
AgentReinforcementLearningforDrugTargetPrediction.arXiv:cs.AI/2103.12983
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:37
[252] DaniloNumerosoandDavideBacciu.2021.MEG:Generatingmolecularcounterfactualexplanationsfordeepgraph
networks. In 2021 International Joint Conference on Neural Networks (IJCNN). 1–8. DOI:https://doi.org/10.1109/
IJCNN52387.2021.9534266
[253] Andrew O’Brien and Edward Kim. 2021. Multi-Agent Algorithmic Recourse. https://doi.org/10.48550/
ARXIV.2110.00673
[254] House of Commons. [n. d.]. Algorithms in Decision Making. https://publications.parliament.uk/pa/cm201719/
cmselect/cmsctech/351/351.pdf.Accessed:2020-10-15.
[255] KwanseokOh,JeeSeokYoon,andHeung-IlSuk.2020.BornIdentityNetwork:Multi-wayCounterfactualMapGen-
erationtoExplainaClassifier’sDecision.https://doi.org/10.48550/ARXIV.2011.10381
[256] KwanseokOh,JeeSeokYoon,andHeung-IlSuk.2021.Learn-Explain-Reinforce:CounterfactualReasoningandIts
GuidancetoReinforceanAlzheimer’sDiseaseDiagnosisModel.https://doi.org/10.48550/ARXIV.2108.09451
[257] MatthewL.Olson,RoliKhanna,LawrenceNeal,FuxinLi,andWeng-KeenWong.2021.Counterfactualstateex-
planationsforreinforcementlearningagentsviagenerativedeeplearning.ArtificialIntelligence295(2021),103455.
https://doi.org/10.1016/j.artint.2021.103455
[258] AxelParmentierandThibautVidal.2021.OptimalCounterfactualExplanationsinTreeEnsembles.https://arxiv.org/
abs/2106.06631
[259] Martin Pawelczyk, Chirag Agarwal, Shalmali Joshi, Sohini Upadhyay, and Himabindu Lakkaraju. 2022. Explor-
ingcounterfactualexplanationsthroughthelensofadversarialexamples:Atheoreticalandempiricalanalysis.In
Proceedingsofthe25thInternationalConferenceonArtificialIntelligenceandStatistics.PMLR,4574–4594.https://
proceedings.mlr.press/v151/pawelczyk22a.html
[260] Martin Pawelczyk, Sascha Bielawski, Johannes van den Heuvel, Tobias Richter, and Gjergji Kasneci. 2021.
CARLA: A Python Library to Benchmark Algorithmic Recourse and Counterfactual Explanation Algorithms.
arXiv:cs.LG/2108.00783
[261] Martin Pawelczyk, Klaus Broelemann, and Gjergji. Kasneci. 2020. On counterfactual explanations under predic-
tivemultiplicity.InProceedingsofMachineLearningResearch.PMLR,Virtual,9.http://proceedings.mlr.press/v124/
pawelczyk20a.html
[262] MartinPawelczyk,TeresaDatta,Johannesvan-denHeuvel,GjergjiKasneci,andHimabinduLakkaraju.2022.Prob-
abilisticallyRobustRecourse:NavigatingtheTrade-offsbetweenCostsandRobustnessinAlgorithmicRecourse.
https://doi.org/10.48550/ARXIV.2203.06768
[263] MartinPawelczyk,KlausBroelemann,andGjergjiKasneci.2020.Learningmodel-agnosticcounterfactualexplana-
tionsfortabulardata.InProceedingsofTheWebConference.AssociationforComputingMachinery,NewYork,NY,
USA.DOI:https://doi.org/10.1145/3366423.3380087
[264] JudeaPearl.2000.Causality:Models,Reasoning,andInference.CambridgeUniversityPress,Cambridge,MA,USA.
[265] TejaswiniPedapati,AvinashBalakrishnan,KarthikeyanShanmugan,andAmitDhurandhar.2020.Learningglobal
transparentmodelsconsistentwithlocalcontrastiveexplanations.InProceedingsofNeurIPS2020.CurranAssociates
Inc.,11.
[266] Oana-IulianaPopescu,MahaShadaydeh,andJoachimDenzler.2021.CounterfactualGenerationwithKnockoffs.
https://doi.org/10.48550/ARXIV.2102.00951
[267] RafaelPoyiadzi,KacperSokol,RaulSantos-Rodriguez,TijlDeBie,andPeterFlach.2020.FACE:FeasibleandAction-
ableCounterfactualExplanations.https://doi.org/10.1145/3375627.3375850arXiv:1909.09369.
[268] MarioAlfonsoPrado-Romero,BardhPrenkaj,GiovanniStilo,andFoscaGiannotti.2022.ASurveyonGraphCoun-
terfactualExplanations:Definitions,Methods,Evaluation.https://doi.org/10.48550/ARXIV.2210.12089
[269] WentingQiandCharalamposChelmis.2021.Improvingalgorithmicdecision–makinginthepresenceofuntrust-
worthytrainingdata.InProceedingsofthe2021IEEEInternationalConferenceonBigData(BigData’21).1102–1108.
https://doi.org/10.1109/BigData52589.2021.9671677
[270] GouthamRamakrishnan,Y.C.Lee,andAwsAlbarghouthi.2020.Synthesizingactionsequencesformodifyingmodel
decisions.InProceedingsoftheConferenceonArtificialIntelligence(AAAI’20).AAAIpress,California,USA,16.http://
arxiv.org/abs/1910.00057
[271] YanouRamon,DavidMartens,FosterProvost,andTheodorosEvgeniou.2020.Acomparisonofinstance-levelcoun-
terfactualexplanationalgorithmsforbehavioralandtextualdata:SEDC,LIME-CandSHAP-C.AdvancesinData
AnalysisandClassification14,4(2020),801–819.DOI:https://doi.org/10.1007/s11634-020-00418-3
[272] PeymanRasouliandIngridChiehYu.2022.CARE:Coherentactionablerecoursebasedonsoundcounterfactual
explanations.InternationalJournalofDataScienceandAnalytics(2022),1–26.https://doi.org/10.1007/s41060-022-
00365-6
[273] PeymanRasouliandIngridChiehYu.2021.Analyzingandimprovingtherobustnessoftabularclassifiersusing
counterfactualexplanations.InProceedingsofthe202120thIEEEInternationalConferenceonMachineLearningand
Applications(ICMLA’21).1286–1293.https://doi.org/10.1109/ICMLA52953.2021.00209
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:38 S.Vermaetal.
[274] ShubhamRathi.2019.GeneratingCounterfactualandContrastiveExplanationsusingSHAP.http://arxiv.org/abs/
1906.09293arXiv:1906.09293.
[275] ShauliRavfogel,GrushaPrasad,TalLinzen,andYoavGoldberg.2021.Counterfactualinterventionsrevealthecausal
effectofrelativeclauserepresentationsonagreementprediction.InProceedingsofthe25thConferenceonComputa-
tionalNaturalLanguageLearning.AssociationforComputationalLinguistics,194–209.https://doi.org/10.18653/v1/
2021.conll-1.15
[276] AmbareeshRavi,XiaozhuoYu,IaraSantelices,FakhriKarray,andBarisFidan.2021.Generalframeworksforanomaly
detectionexplainability:Comparativestudy.InProceedingsofthe2021IEEEInternationalConferenceonAutonomous
Systems(ICAS’21).1–5.https://doi.org/10.1109/ICAS49788.2021.9551129
[277] KaivalyaRawal,EceKamar,andHimabinduLakkaraju.2021.AlgorithmicRecourseintheWild:Understandingthe
ImpactofDataandModelShifts.arXiv:cs.LG/2012.11788
[278] KaivalyaRawalandHimabinduLakkaraju.2020.Beyondindividualizedrecourse:Interpretableandinteractivesum-
mariesofactionablerecourses.InAdvancesinNeuralInformationProcessingSystems,Vol.33.CurranAssociates,Inc.,
12187–12198.https://proceedings.neurips.cc/paper/2020/file/8ee7730e97c67473a424ccfeff49ab20-Paper.pdf
[279] AnnabelleRedelmeier,MartinJullum,KjerstiAas,andAndersLøland.2021.MCCE:MonteCarloSamplingofReal-
isticCounterfactualExplanations.https://doi.org/10.48550/ARXIV.2111.09790
[280] ChrisReed,KeriGrieman,andJosephEarly.2021.Non-AsimovexplanationsregulatingAIthroughtransparency.In
QueenMaryLawResearchPaperNo.370/2021.https://ssrn.com/abstract=3970518
[281] MarcoTulioRibeiro,SameerSingh,andCarlosGuestrin.2016.“WhyShouldITrustYou?”:Explainingthepredictions
ofanyclassifier.InProceedingsofKDD’16.ACM,NewYork,10.https://doi.org/10.1145/2939672.2939778
[282] MarcoTulioRibeiro,SameerSingh,andCarlosGuestrin.2018.Anchors:High-precisionmodel-agnosticexplana-
tions.InProceedingsoftheConferenceonArtificialIntelligence(AAAI’18).AAAIPress,California,USA,9.https://
www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16982
[283] MarcelRobeer,FlorisBex,andAdFeelders.2021.Generatingrealisticnaturallanguagecounterfactuals.InFindingsof
theAssociationforComputationalLinguistics(EMNLP2021).AssociationforComputationalLinguistics,PuntaCana,
DominicanRepublic,3611–3625.https://doi.org/10.18653/v1/2021.findings-emnlp.306
[284] PauRodriguez,MassimoCaccia,AlexandreLacoste,LeeZamparo,IssamLaradji,LaurentCharlin,andDavidVazquez.
2021.BeyondTrivialCounterfactualExplanationswithDiverseValuableExplanations.https://doi.org/10.48550/
ARXIV.2103.10226
[285] AlexisRoss,HimabinduLakkaraju,andOsbertBastani.2021.Learningmodelsforactionablerecourse.InAdvancesin
NeuralInformationProcessingSystems,Vol.34.CurranAssociates,Inc.,18734–18746.https://proceedings.neurips.cc/
paper/2021/file/9b82909c30456ac902e14526e63081d4-Paper.pdf
[286] David-HillelRuben.1992.Counterfactuals.RoutledgePublishers.https://philarchive.org/archive/RUBEE-3
[287] ChrisRussell.2019.Efficientsearchfordiversecoherentexplanations.InProceedingsoftheConferenceonFairness,
Accountability,andTransparency(FAccT’19)(FAT*’19).ACM,NewYork,9.https://doi.org/10.1145/3287560.3287569
[288] SophieSadler,DerekGreene,andDanielW.Archambault.2021.Astudyofexplainablecommunity-levelfeatures.In
GEM:GraphEmbeddingandMining(ECML-PKDD2021Workshop+Tutorial).
[289] SuryaShravanKumarSajja,SumantaMukherjee,SatyamDwivedi,andVikasC.Raykar.2021.Semi-supervised
CounterfactualExplanations.https://openreview.net/forum?id=o6ndFLB1DST
[290] Robert-FlorianSamoilescu,ArnaudVanLooveren,andJanisKlaise.2021.Model-agnosticandScalableCounterfac-
tualExplanationsviaReinforcementLearning.https://doi.org/10.48550/ARXIV.2106.02597
[291] PedroSanchezandSotiriosA.Tsaftaris.2022.DiffusionCausalModelsforCounterfactualEstimation.https://doi.org/
10.48550/ARXIV.2202.10166
[292] MaximilianSchleich,ZixuanGeng,YihongZhang,andDanSuciu.2021.GeCo:QualityCounterfactualExplanations
inRealTime.arXiv:cs.LG/2101.01292
[293] LisaSchut,OscarKey,RoryMcGrath,LucaCostabello,BogdanSacaleanu,MedbCorcoran,andYarinGal.2021.Gen-
eratingInterpretableCounterfactualExplanationsByImplicitMinimisationofEpistemicandAleatoricUncertainties.
https://doi.org/10.48550/ARXIV.2103.08951
[294] R.R.Selvaraju,M.Cogswell,A.Das,R.Vedantam,D.Parikh,andD.Batra.2017.Grad-CAM:Visualexplanations
fromdeepnetworksviagradient-basedlocalization.InProceedingsoftheIEEEInternationalConferenceonComputer
Vision.618–626.https://doi.org/10.1109/ICCV.2017.74
[295] KumbaSennaar.2019.MachineLearningforRecruitingandHiring–6CurrentApplications.https://emerj.com/ai-
sector-overviews/machine-learning-for-recruiting-and-hiring/.Accessed:2020-10-15.
[296] RuoxiShang,K.J.KevinFeng,andChiragShah.2022.WhyamInotseeingit?Understandingusers’needsfor
counterfactualexplanationsineverydayrecommendations.InProceedingsof FAccT’22.ACM,NewYork,11.https://
doi.org/10.1145/3531146.3533189
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:39
[297] XiaotingShaoandKristianKersting.2022.Gradient-basedCounterfactualExplanationsusingTractableProbabilistic
Models.https://doi.org/10.48550/ARXIV.2205.07774
[298] ShubhamSharma,JetteHenderson,andJoydeepGhosh.2019.CERTIFAI:CounterfactualExplanationsforRobust-
ness,Transparency,Interpretability,andFairnessofArtificialIntelligencemodels.http://arxiv.org/abs/1905.07857
[299] RezaShokri,MartinStrobel,andYairZick.2021.Ontheprivacyrisksofmodelexplanations.InProceedingsofthe
2021AAAI/ACMConferenceonAI,Ethics,andSociety.ACM,NewYork,11.https://doi.org/10.1145/3461702.3462533
[300] RonalRajneshwarSingh,PaulDourish,PiersHowe,TimMiller,LizSonenberg,EduardoVelloso,andFrankVet-
ere.2021.DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications.https://doi.org/
10.1145/3579363
[301] SauravSingla.2020.MachineLearningtoPredictCreditRiskinLendingIndustry.https://www.aitimejournal.com/
@saurav.singla/machine-learning-to-predict-credit-risk-in-lending-industry.Accessed:2020-10-15.
[302] DylanSlack,SophieHilgard,HimabinduLakkaraju,andSameerSingh.2021.CounterfactualExplanationsCanBe
Manipulated.arXiv:cs.LG/2106.02666
[303] J.W.Smith,J.Everhart,W.C.Dickson,W.Knowler,andR.Johannes.1988.UsingtheADAPlearningalgorithmto
forecasttheonsetofdiabetesmellitus.InProceedingsoftheAnnualSymposiumonComputerApplicationinMedical
Care.AmericanMedicalInformaticsAssociation,Washington,D.C.,261–265.
[304] SimónC.SmithandSubramanianRamamoorthy.2020.Counterfactualexplanationandcausalinferenceinservice
ofrobustnessinrobotcontrol.InProceedingsofthe2020JointIEEE10thInternationalConferenceonDevelopmentand
LearningandEpigeneticRobotics(ICDL-EpiRob’20).1–8.https://doi.org/10.1109/ICDL-EpiRob48136.2020.9278061
[305] KacperSokolandPeterFlach.2018.Glass-Box:ExplainingAIdecisionswithcounterfactualstatementsthrough
conversation with a voice-enabled virtual assistant. In Proceedings of IJCAI’18. AAAI Press, 5868–5870. https://
doi.org/10.24963/ijcai.2018/865
[306] KacperSokolandPeterFlach.2019.Desiderataforinterpretability:Explainingdecisiontreepredictionswithcoun-
terfactuals.InProceedingsoftheConferenceonArtificialIntelligence(AAAI)33(July2019).https://doi.org/10.1609/
aaai.v33i01.330110035
[307] ThomasSpooner,DanialDervovic,JasonLong,JonShepard,JiahaoChen,andDanieleMagazzeni.2021.Counterfac-
tualExplanationsforArbitraryRegressionModels.https://arxiv.org/abs/2106.15212
[308] LauraState.2021.LogicprogrammingforXAI:Atechnicalperspective.InProceedingsoftheInternationalConference
onLogicProgramming2021Workshops(ICLP’21),Vol.2970.http://ceur-ws.org/Vol-2970/meepaper1.pdf
[309] Gregory Stein. 2021. Generating high-quality explanations for navigation in partially-revealed environments.
In Advances in Neural Information Processing Systems, Vol. 34. Curran Associates, Inc., 17493–17506. https://
proceedings.neurips.cc/paper/2021/file/926ec030f29f83ce5318754fdb631a33-Paper.pdf
[310] DeborahSulem,MicheleDonini,MuhammadBilalZafar,Francois-XavierAubet,JanGasthaus,TimJanuschowski,
SanjivDas,KrishnaramKenthapadi,andCedricArchambeau.2022.DiverseCounterfactualExplanationsforAnom-
alyDetectioninTimeSeries.https://doi.org/10.48550/ARXIV.2203.11103
[311] EzzeldinTahounandAndreKassis.2020.BeyondExplanations:RecourseviaActionableInterpretability-Extended.
https://doi.org/10.13140/RG.2.2.19076.14729
[312] PaoloTamagnini,JosuaKrause,AritraDasgupta,andEnricoBertini.2017.Interpretingblack-boxclassifiersusing
instance-levelvisualexplanations.InProceedingsofthe2ndWorkshoponHuman-In-the-LoopDataAnalytics.ACM,
NewYork,6.https://doi.org/10.1145/3077257.3077260
[313] JuntaoTan,ShuyuanXu,YingqiangGe,YunqiLi,XuChen,andYongfengZhang.2021.Counterfactualexplainable
recommendation.InProceedingsofthe30thACMInternationalConferenceonInformation&KnowledgeManagement.
ACM,NewYork,10.https://doi.org/10.1145/3459637.3482420
[314] Sarah Tan,Rich Caruana,Giles Hooker, andYin Lou. 2018.Distill-and-compare: Auditing black-boxmodels us-
ingtransparentmodeldistillation.InProceedingsofAIES’18.ACM,NewYork,8.https://doi.org/10.1145/3278721.
3278725
[315] JasonTashea.2017.CourtsAreUsingAItoSentenceCriminals.ThatMustStopNow.https://www.wired.com/2017/
04/courts-using-ai-sentence-criminals-must-stop-now/.Accessed:2020-10-15.
[316] MohammedTemrazandMarkT.Keane.2021.SolvingtheClassImbalanceProblemUsingaCounterfactualMethod
forDataAugmentation.https://doi.org/10.48550/ARXIV.2111.03516
[317] MohammedTemraz,EoinM.Kenny,ElodieRuelle,LaurenceShalloo,BarrySmyth,andMarkT.Keane.2021.Han-
dlingclimatechangeusingcounterfactuals:Usingcounterfactualsindataaugmentationtopredictcropgrowthin
anuncertainclimatefuture.InCase-BasedReasoningResearchandDevelopment.SpringerInternationalPublishing,
Cham,216–231.
[318] T.Teofili,D.Firmani,N.Koudas,V.Martello,P.Merialdo,andD.Srivastava.2022.Effectiveexplanationsforentity
resolutionmodels.InProceedingsofthe2022IEEE38thInternationalConferenceonDataEngineering(ICDE’22).IEEE
ComputerSociety,LosAlamitos,CA,USA,2709–2721.https://doi.org/10.1109/ICDE53745.2022.00248
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:40 S.Vermaetal.
[319] PaulThagard.1989.Explanatorycoherence.BehavioralandBrainSciences(1989),435–467.https://doi.org/10.1017/
S0140525X00057046
[320] JayaramanThiagarajan,VivekSivaramanNarayanaswamy,DeeptaRajan,JiaLiang,AkshayChaudhari,andAndreas
Spanias.2021.Designingcounterfactualgeneratorsusingdeepmodelinversion.InAdvancesinNeuralInformation
ProcessingSystems,Vol.34.CurranAssociates,Inc.,16873–16884.https://proceedings.neurips.cc/paper/2021/file/
8ca01ea920679a0fe3728441494041b9-Paper.pdf
[321] EricoTjoaandCuntaiGuan.2019.ASurveyonExplainableArtificialIntelligence(XAI):TowardsMedicalXAI.
arXiv:cs.LG/1907.07374
[322] GeorgeTolkachev,StephenMell,StephanZdancewic,andOsbertBastani.2022.Counterfactualexplanationsfornatu-
rallanguageinterfaces.InProceedingsofthe60thAnnualMeetingoftheAssociationforComputationalLinguistics(Vol-
ume2:ShortPapers).AssociationforComputationalLinguistics,Dublin,Ireland,113–118.https://aclanthology.org/
2022.acl-short.14
[323] GabrieleTolomei,FabrizioSilvestri,AndrewHaines,andMouniaLalmas.2017.Interpretablepredictionsoftree-
basedensemblesviaactionablefeaturetweaking.InProceedingsoftheInternationalConferenceonKnowledgeDiscov-
eryandDataMining(KDD’17).ACM,NewYork,10.https://doi.org/10.1145/3097983.3098039
[324] KhanhHiepTran,AzinGhazimatin,andRishirajSahaRoy.2021.CounterfactualExplanationsforNeuralRecom-
menders.ACM,NewYork,1627–1631.https://doi.org/10.1145/3404835.3463005
[325] MariaTsiakmakiandOmirosRagos.2021.Acasestudyofinterpretablecounterfactualexplanationsforthetaskof
predictingstudentacademicperformance.InProceedingsofthe202125thInternationalConferenceonCircuits,Systems,
CommunicationsandComputers(CSCC’21).https://doi.org/10.1109/CSCC53858.2021.00029
[326] StratisTsirtsis,AbirDe,andManuelRodriguez.2021.Counterfactualexplanationsinsequentialdecisionmaking
underuncertainty.InAdvancesinNeuralInformationProcessingSystems,Vol.34.CurranAssociates,Inc.,30127–
30139.https://proceedings.neurips.cc/paper/2021/file/fd0a5a5e367a0955d81278062ef37429-Paper.pdf
[327] StratisTsirtsisandManuelGomez-Rodriguez.2020.Decisions,CounterfactualExplanationsandStrategicBehavior.
arXiv:cs.LG/2002.04333
[328] RyanTurner.2016.Amodelexplanationsystem:Latestupdatesandextensions.ArXivabs/1606.09517(2016).
[329] AaltoUniversity.[n.d.].TheEuropeanCommissionOffersSignificantSupporttoEurope’sAIExcellence.https://
www.eurekalert.org/pub_releases/2020-03/au-tec031820.php.Accessed:2020-10-15.
[330] Sohini Upadhyay, Shalmali Joshi, and Himabindu Lakkaraju. 2021. Towards Robust and Reliable Algorithmic
Recourse.arXiv:cs.LG/2102.13620
[331] BerkUstun,AlexanderSpangher,andYangLiu.2019.Actionablerecourseinlinearclassification.InProceedings
oftheConferenceonFairness,Accountability,andTransparency(FAccT’19)(FAT*’19).ACM,NewYork,10.https://
doi.org/10.1145/3287560.3287566
[332] ArnaudVanLooverenandJanisKlaise.2020.InterpretableCounterfactualExplanationsGuidedbyPrototypes.http:
//arxiv.org/abs/1907.02584
[333] ArnaudVanLooveren,JanisKlaise,GiovanniVacanti,andOliverCobb.2021.ConditionalGenerativeModelsfor
CounterfactualExplanations.https://doi.org/10.48550/ARXIV.2101.10123
[334] SimonVandenhende,DhruvMahajan,FilipRadenovic,andDeeptiGhadiyaram.2022.Makingheadsortails:To-
wardssemanticallyconsistentvisualcounterfactuals.InProceedingsofECCV2022.https://doi.org/10.1007/978-3-
031-19775-816
[335] SahilVerma,JohnDickerson,andKeeganHines.2020.CounterfactualExplanationsforMachineLearning:AReview.
https://doi.org/10.48550/ARXIV.2010.10596
[336] SahilVerma,JohnDickerson,andKeeganHines.2021.CounterfactualExplanationsforMachineLearning:Chal-
lengesRevisited.https://doi.org/10.48550/ARXIV.2106.07756
[337] SahilVerma,KeeganHines,andJohnP.Dickerson.2021.AmortizedGenerationofSequentialCounterfactualExpla-
nationsforBlack-boxModels.arXiv:cs.LG/2106.03962
[338] SahilVermaandJuliaRubin.2018.Fairnessdefinitionsexplained.InProceedingsoftheInternationalWorkshopon
SoftwareFairness(FairWare’18).ACM,NewYork,1–7.https://doi.org/10.1145/3194770.3194776
[339] Sahil Verma, Chirag Shah, John P. Dickerson, Anurag Beniwal, Narayanan Sadagopan, and Arjun Se-
shadri. 2023. RecXplainer: Amortized Attribute-based Personalized Explanations for Recommender Systems.
arXiv:cs.IR/2211.14935
[340] TomVermeire,DieterBrughmans,SofieGoethals,RaphaelMazzineBarbossadeOliveira,andDavidMartens.[n.
d.].Explainableimageclassificationwithevidencecounterfactual.PatternAnal.Appl.([n.d.]),21.https://doi.org/
10.1007/s10044-021-01055-y
[341] Cédric Villani. [n. d.]. For a Meaningful Artificial Intelligence. https://www.aiforhumanity.fr/pdfs/
MissionVillaniReportENG-VF.pdf.Accessed:2020-10-15.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:41
[342] MarcoVirgolinandSaverioFracaros.2022.OntheRobustnessofSparseCounterfactualExplanationstoAdverse
Perturbations.https://doi.org/10.48550/ARXIV.2201.09051
[343] J.vonKügelgen,N.Agarwal,J.Zeitler,A.Mastouri,andB.Schölkopf.2021.Algorithmicrecourseinpartiallyand
fullyconfoundedsettingsthroughboundingcounterfactualeffects.InProceedingsoftheICML2021Workshopon
AlgorithmicRecourse.https://sites.google.com/view/recourse21/home
[344] J.vonKügelgen,A.-H.Karimi,U.Bhatt,I.Valera,A.Weller,andB.Schölkopf.2022.Onthefairnessofcausalalgo-
rithmicrecourse.InProceedingsofthe36thAAAIConferenceonArtificialIntelligence,Vol.9.AAAIPress,PaloAlto,
CA,9584–9594.https://doi.org/10.1609/aaai.v36i9.21192
[345] SandraWachter,BrentMittelstadt,andLucianoFloridi.2017.Whyarighttoexplanationofautomateddecision-
makingdoesnotexistinthegeneraldataprotectionregulation.InternationalDataPrivacyLaw7,2(062017).https:
//doi.org/10.1093/idpl/ipx005
[346] SandraWachter,BrentMittelstadt,andChrisRussell.2017.Counterfactualexplanationswithoutopeningtheblack
box:AutomateddecisionsandtheGDPR.SSRNElectronicJournal31,2(2017).https://doi.org/10.2139/ssrn.3063289
[347] PeiWangandNunoVasconcelos.2020.SCOUT:Self-awarediscriminantcounterfactualexplanations.InProceed-
ings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR’20). https://doi.org/10.1109/
CVPR42600.2020.00900
[348] XiaosongWang,YifanPeng,LeLu,ZhiyongLu,MohammadhadiBagheri,andRonaldM.Summers.2017.ChestX-
ray8:Hospital-scalechestX-Raydatabaseandbenchmarksonweakly-supervisedclassificationandlocalizationof
commonthoraxdiseases.InProceedingsofCVPR.https://doi.org/10.1007/978-3-030-13969-818
[349] YongjieWang,QinxuDing,KeWang,YueLiu,XingyuWu,JinglongWang,YongLiu,andChunyanMiao.2021.The
skylineofcounterfactualexplanationsformachinelearningdecisionmodels.InProceedingsofCIKM.ACM,New
York,10.https://doi.org/10.1145/3459637.3482397
[350] YongjieWang,HangweiQian,andChunyanMiao.2022.DualCF:Efficientmodelextractionattackfromcounterfac-
tualexplanations.InProceedingsofFAccT’22.ACM,NewYork.,12.https://doi.org/10.1145/3531146.3533188
[351] ZhendongWang,IsakSamsten,RamiMochaourab,andPanagiotisPapapetrou.2021.Learningtimeseriescounter-
factualsvialatentspacerepresentations.InDiscoveryScience.SpringerInternationalPublishing,Cham,369–384.
https://doi.org/10.1007/978-3-030-88942-529
[352] ZhendongWang,IsakSamsten,andPanagiotisPapapetrou.2021.Counterfactualexplanationsforsurvivalprediction
ofcardiovascularICUpatients.InArtificialIntelligenceinMedicine.SpringerInternationalPublishing,Cham,338–
348.https://doi.org/10.1007/978-3-030-77211-638
[353] Greta Warren, Mark T. Keane, and Ruth M. J. Byrne. 2022. Features of Explainability: How Users Understand
CounterfactualandCausalExplanationsforCategoricalandContinuousFeaturesinXAI.https://doi.org/10.48550/
ARXIV.2204.10152
[354] GretaWarren,MarkT.Keane,ChristopheGueret,andEoinDelaney.2023.ExplainingGroupsofInstancesCounter-
factuallyforXAI:AUseCase,AlgorithmandUserStudyforGroup-Counterfactuals.arXiv:cs.AI/2303.09297
[355] GeemiP.Wellawatte,AditiSeshadri,andAndrewD.White.2022.Modelagnosticgenerationofcounterfactualex-
planationsformolecules.Chem.Sci.13(2022),3697–3705.https://doi.org/10.1039/D1SC05259D
[356] J.Wexler,M.Pushkarna,T.Bolukbasi,M.Wattenberg,F.Viégas,andJ.Wilson.2020.TheWhat-Iftool:Interactive
probingofmachinelearningmodels.IEEETransactionsonVisualizationandComputerGraphics26,1(2020),56–65.
https://doi.org/10.1109/TVCG.2019.2934619
[357] AdamWhiteandArturd’AvilaGarcez.2019.MeasurableCounterfactualLocalExplanationsforAnyClassifier.http:
//arxiv.org/abs/1908.03020
[358] Adam White and Artur d’Avila Garcez. 2021. Counterfactual Instances Explain Little. https://doi.org/10.48550/
ARXIV.2109.09809
[359] AdamWhite,KwunHoNgan,JamesPhelan,SamanSadeghiAfgeh,KevinRyan,ConstantinoCarlosReyes-Aldasoro,
andArturd’AvilaGarcez.2021.ContrastiveCounterfactualVisualExplanationswithOverdetermination.https://
doi.org/10.48550/ARXIV.2106.14556
[360] AnjanaWijekoon,NirmalieWiratunga,IkechukwuNkisi-Orji,KyleMartin,ChamathPalihawadana,andDavidCor-
sar.2021.Counterfactualexplanationsforstudentoutcomepredictionwithmoodlefootprints.InProceedingsofthe
CEURWorkshop,1–8.https://rgu-repository.worktribe.com/output/1395861
[361] NirmalieWiratunga,AnjanaWijekoon,IkechukwuNkisi-Orji,KyleMartin,ChamathPalihawadana,andDavidCor-
sar.2021.DisCERN:Discoveringcounterfactualexplanationsusingrelevancefeaturesfromneighbourhoods.InPro-
ceedings ofthe2021IEEE33rdInternationalConferenceonToolswithArtificial Intelligence(ICTAI’21).1466–1473.
https://doi.org/10.1109/ICTAI52525.2021.00233
[362] JamesWoodward.2003.MakingThingsHappen:ATheoryofCausalExplanation.OxfordUniversityPress.
[363] Xintao Xiang and Artem Lenskiy. 2022. Realistic Counterfactual Explanations by Learned Relations. https://
arxiv.org/abs/2202.07356
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:42 S.Vermaetal.
[364] ShuyuanXu,YunqiLi,ShuchangLiu,ZuohuiFu,YingqiangGe,XuChen,andYongfengZhang.2021.Learningcausal
explanationsforrecommendation.CEURWorkshopProceedings2911(2021),13–25.
[365] YanivYacoby,BenGreen,ChristopherL.Griffin,andFinaleDoshiVelez.2022.“Ifitdidn’thappen,whywould
IChangemyDecision?”:HowJudgesRespondtoCounterfactualExplanationsforthePublicSafetyAssessment.
https://doi.org/10.48550/ARXIV.2205.05424
[366] PrateekYadav,PeterHase,andMohitBansal.2021.Low-CostAlgorithmicRecourseforUserswithUncertainCost
Functions.https://doi.org/10.48550/ARXIV.2111.01235
[367] FanYang,SahanSureshAlva,JiahaoChen,andXiaHu.2021.Model-basedcounterfactualsynthesizerforinterpre-
tation.InProceedingsof KDD’21.ACM,NewYork,1964–1974.https://doi.org/10.1145/3447548.3467333
[368] FanYang,NinghaoLiu,MengnanDu,andXiaHu.2021.Generativecounterfactualsforneuralnetworksviaattribute-
informedperturbation.SIGKDDExplor.Newsl.23(May2021),10.https://doi.org/10.1145/3468507.3468517
[369] LinyiYang,EoinKenny,TinLokJamesNg,YiYang,BarrySmyth,andRuihaiDong.2020.Generatingplausible
counterfactualexplanationsfordeeptransformersinfinancialtextclassification.InProceedingsofICCL.6150–6160.
https://doi.org/10.18653/v1/2020.coling-main.541
[370] NakyeongYang,TaegwanKang,andKyominJung.2022.Derivingexplainablediscriminativeattributesusingcon-
fusionaboutcounterfactualclass.InProceedingsofICASSP2022.1730–1734.https://doi.org/10.1109/ICASSP43922.
2022.9747693
[371] YuanshunYao,ChongWang,andHangLi.2022.CounterfactuallyEvaluatingExplanationsinRecommenderSystems.
https://doi.org/10.48550/ARXIV.2203.01310
[372] I-Cheng Yeh. 2016. Default of Credit Card Clients. UCI Machine Learning Repository. https://doi.org/10.24432/
C55S3H
[373] RoozbehYousefzadehandDianneP.O’Leary.2019.DebuggingTrainedMachineLearningModelsusingFlipPoints.
https://debug-ml-iclr2019.github.io/cameraready/DebugML-19paper11.pdf
[374] ZixuanYuan,YadaZhu,WeiZhang,ZimingHuang,GuangnanYe,andHuiXiong.2021.Multi-DomainTransformer-
BasedCounterfactualAugmentationforEarningsCallAnalysis.https://doi.org/10.48550/ARXIV.2112.00963
[375] WencanZhangandBrianYLim.2022.TowardsrelatableexplainableAIwiththeperceptualprocess.ACM,New
York,https://doi.org/10.1145/3491102.3501826
[376] YuhaoZhang.,KevinMcAreavey.,andWeiruLiu.2022.Developingandexperimentingonapproachestoexplainabil-
ityinAIsystems.InProceedingsofICAART.SciTePress,518–527.https://doi.org/10.5220/0010900300003116
[377] YunxiaZhao.2020.FastReal-timeCounterfactualExplanations.https://doi.org/10.48550/ARXIV.2007.05684
[378] JinfengZhongandElsaNegre.2022.Shap-enhancedcounterfactualexplanationsforrecommendations.InProceed-
ingsofthe37thACM/SIGAPPSymposiumonAppliedComputing.ACM,NewYork,1365–1372.https://doi.org/10.1145/
3477314.3507029
[379] B.Zhou,A.Khosla,A.Lapedriza,A.Oliva,andA.Torralba.2016.Learningdeepfeaturesfordiscriminativelocaliza-
tion.InProceedingsofCVPR.IEEE,NewYork,USA,2921–2929.https://doi.org/10.1109/CVPR.2016.319
[380] YaoZhou,HaonanWang,JingruiHe,andHaixunWang.2021.FromIntrinsictoCounterfactual:OntheExplainability
ofContextualizedRecommenderSystems.https://doi.org/10.48550/ARXIV.2110.14844
[381] Alexander Zien, Nicole Krämer, Sören Sonnenburg, and Gunnar Rätsch. 2009. The feature importance ranking
measure. In Machine Learning and Knowledge Discovery in Databases, Vol. 5782. Springer Berlin, Berlin. https://
doi.org/10.1007/978-3-642-04174-7_45
Received25July2023;revised21June2024;accepted5July2024
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.