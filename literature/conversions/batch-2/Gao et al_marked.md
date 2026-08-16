---
conversion_metadata:
  converted_at: "2026-07-22T13:23:48Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Gao et al.pdf"
  source_pdf_sha256: "25b02a9a4578cb68865d3144033639f976558800b6da7cc04797cdc1896fa0cc"
  page_count: 10
  markdown_char_count: 143709
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Leveraging Transferable Knowledge Concept Graph Embedding
for Cold-Start Cognitive Diagnosis
Hao Wang
Anhui Province Key Laboratory of
Big Data Analysis and Application,
University of Science and Technology
of China & State Key Laboratory of
Cognitive Intelligence
Hefei, China
wanghao3@ustc.edu.cn

Qi Liu∗
Anhui Province Key Laboratory of
Big Data Analysis and Application,
University of Science and Technology
of China & State Key Laboratory of
Cognitive Intelligence
Hefei, China
qiliuql@ustc.edu.cn

Weibo Gao
Anhui Province Key Laboratory of
Big Data Analysis and Application,
School of Computer Science and
Technology, University of Science and
Technology of China & State Key
Laboratory of Cognitive Intelligence
Hefei, China
weibogao@mail.ustc.edu.cn

Fei Wang
Anhui Province Key Laboratory of
Big Data Analysis and Application,
School of Computer Science and
Technology, University of Science and
Technology of China & State Key
Laboratory of Cognitive Intelligence
Hefei, China
wf314159@mail.ustc.edu.cn

Xin Lin
Anhui Province Key Laboratory of
Big Data Analysis and Application,
School of Computer Science and
Technology, University of Science and
Technology of China & State Key
Laboratory of Cognitive Intelligence
Hefei, China
linx@mail.ustc.edu.cn

Linan Yue
Anhui Province Key Laboratory of
Big Data Analysis and Application,
School of Data Science, University of
Science and Technology of China &
State Key Laboratory of Cognitive
Intelligence
Hefei, China
lnyue@mail.ustc.edu.cn

Zheng Zhang
Anhui Province Key Laboratory of
Big Data Analysis and Application,
School of Computer Science and
Technology, University of Science and
Technology of China & State Key
Laboratory of Cognitive Intelligence
Hefei, China
zhangzheng@mail.ustc.edu.cn

Rui Lv
Anhui Province Key Laboratory of
Big Data Analysis and Application,
School of Computer Science and
Technology, University of Science and
Technology of China & State Key
Laboratory of Cognitive Intelligence
Hefei, China
lvrui2018@mail.ustc.edu.cn

Shijin Wang
State Key Laboratory of Cognitive
Intelligence & iFLYTEK AI Research
(Central China), iFLYTEK Co., Ltd
Hefei, China
sjwang3@iflytek.com

ABSTRACT
Cognitive diagnosis (CD) aims to reveal the proficiency of students
on specific knowledge concepts and traits of test exercises (e.g.,
difficulty). It plays a critical role in intelligent education systems
by supporting personalized learning guidance. However, recent
developments in CD mostly concentrate on improving the accuracy
of diagnostic results and often overlook the important and practi-
cal task: domain-level zero-shot cognitive diagnosis (DZCD). The
primary challenge of DZCD is the deficiency of student behavior
data in the target domain due to the absence of student-exercise

∗Corresponding author.

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
SIGIR ’23, July 23–27, 2023, Taipei, Taiwan
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-9408-6/23/07. . . $15.00
https://doi.org/10.1145/3539618.3591774

interactions or unavailability of exercising records for training
purposes. To tackle the cold-start issue, we propose a two-stage
solution named TechCD (Transferable knowledgE Concept grapH
embedding framework for Cognitive Diagnosis). The fundamental
notion involves utilizing a pedagogical knowledge concept graph
(KCG) as a mediator to connect disparate domains, allowing the
transmission of student cognitive signals from established domains
to the zero-shot cold-start domain. Specifically, a naive yet effec-
tive graph convolutional network (GCN) with the bottom-layer
discarding operation is initially employed over the KCG to learn
transferable student cognitive states and domain-specific exercise
traits. Moreover, we give three implementations of the general
TechCD framework following the typical cognitive diagnosis solu-
tions. Finally, extensive experiments on real-world datasets not only
prove that Tech can effectively perform zero-shot diagnosis, but also
give some popular applications such as exercise recommendation.

CCS CONCEPTS
• Applied computing → E-learning.

---

<!-- PAGE 2 -->

SIGIR ’23, July 23–27, 2023, Taipei, Taiwan

Weibo Gao et al.

KEYWORDS
cognitive diagnosis; student performance prediction; cold-start;
knowledge concept graph

ACM Reference Format:
Weibo Gao, Hao Wang, Qi Liu, Fei Wang, Xin Lin, Linan Yue, Zheng Zhang,
Rui Lv, and Shijin Wang. 2023. Leveraging Transferable Knowledge Concept
Graph Embedding for Cold-Start Cognitive Diagnosis. In Proceedings of the
46th International ACM SIGIR Conference on Research and Development in
Information Retrieval (SIGIR ’23), July 23–27, 2023, Taipei, Taiwan. ACM,
New York, NY, USA, 10 pages. https://doi.org/10.1145/3539618.3591774

1 INTRODUCTION
Intelligent education systems facilitate the personalized learning
of students with computer-assisted technology by providing open
access to abundant learning materials (e.g., exercises). Their preva-
lence and convenience have received great attention from both
educators and the general public [27]. In these platforms, cogni-
tive diagnosis (CD) plays a crucial role in providing customized
applications tailored to individual needs [37]. Specifically, the goal
of CD is to profile students’ latent cognitive proficiency on spe-
cific knowledge concepts, as well as to reveal characteristics of
the test exercises such as difficulty and discrimination [9, 37]. As
the diagnostic results can support further educational applications,
such as exercise recommendation [19, 46] and learning path sugges-
tions [18, 39], a number of existing methods have tried to improve
the accuracy of diagnostic results by fully exploiting the students’
explicit response records (e.g., answering correctly or not).

However, many previous models face challenges with the "diag-
nostic system cold-start" problem. For instance, in online platforms,
it is common to launch new businesses, e.g., coursera.org plans to
release a series of new test exercises. For the new domain, there
are no student-exercise interaction records available. Hereby, the
diagnostic performance of previous approaches is often impaired
as they only address the CD task in mature source domains where
student-exercise interaction data are available. In this paper, we
call the diagnostic system cold-start task as domain-level zero-shot
cognitive diagnosis (DZCD). Different from previous studies on stu-
dents or exercises cold-start for CD within a well-established source
domain where interaction records are available [22, 33], in DZCD,
students partially overlap across domains, and the mature source
domains have rich student response records but the zero-shot target
domain is brand new without student-exercise interactions. The
DZCD is an important and practical task, typical applications in-
clude: (1) it is necessary to diagnose in advance when an online
learning system intends to launch a new business; (2) students’
behavior data in the target domain are unavailable due to collection
limitations like privacy protection policy. Nevertheless, to the best
of our knowledge, there is a severe lack of research on DZCD.

To provide reliable cognitive diagnosis for a zero-shot domain,
inspired by the success of cross-domain modeling in various fields
(e.g., recommender systems [25, 54]), one possible way is to define
common student state characteristics by analyzing their past behav-
iors from a few accessible source domains, and represent the test
exercises in the target domain using available features. The primary
obstacle is to locate an appropriate mediator that can transmit stu-
dent states between the established and target domains, enabling
the execution of DZCD [54]. Some related studies have attempted

Figure 1: The example of a knowledge concept graph (KCG)
connecting isolated exercises in each domain.
to utilize exercises’ textual contents as the intermediary by learning
universal and cross-domain exercise embeddings [22, 35]. However,
there are two main drawbacks to these approaches. First, exercises’
textual features may not accurately reflect the true meaning of
the exercise due to linguistic bias [24]. For example, two exercises
from course Math and course Programming may have the same
description "Calculate the circle’s area", but they are testing differ-
ent concepts, i.e., Geometry and Programming Language. Second,
to proficiently adjust to diverse domains, the exercise text encoder
necessitates domain-specific guidance, which has the potential to
overfit and obstruct the transmission of cognitive signals between
distinct domains [48, 54]. Therefore, it is desirable to find a more
suitable intermediary to connect different domains.

In this paper, we employ a pedagogical knowledge concept graph
(KCG) as the intermediary to facilitate the sharing of student cogni-
tive states across different domains. The underlying rationale is that
the KCG has the potential to connect different domains which can be
a bridge to propagate student cognitive states. To elaborate, a KCG
comprises numerous educational dependencies (as relations) to link
knowledge concepts (as entities), which has been widely used in
AI for Education [3, 34, 45]. Figure 1 illustrates an example of KCG
with some educational dependency relations, e.g., the similarity re-
lation links concept Cone and concept Cube since they belong to the
same topic Geometry, while Number is the prerequisite concept of
Arithmetic as the former is the learning basis of the latter logically.
Obviously, the KCG has the capability to bridge different domains
if it covers the knowledge concepts and associated exercises in
each domain. For example, for two course-level domains, the Math
(source domain) and Programming (target domain), each of their
exercises associates at least one knowledge concept. This allows
the two domains to be connected through the KCG as long as their
associated concepts occur in the KCG, even though their exercises
have no direct overlap. Thus, introducing a KCG as the intermediary
across domains to propagate student cognitive states is promising,
but also significantly challenging. Ideally, a proper KCG model for
CD should have four essential properties: (1) diagnosis-oriented:
the model can perform the CD task in the DZCD setting; (2) stu-
dent state propagation: the KCG model should extract universal and
transferable information for student embeddings so that student
cognitive signals can be shared across domains; (3) domain adap-
tion: for any cold-start domain which needs diagnosis, the model
is expected to be domain-adaptive. (4) application: the diagnostic
results can effectively support further intelligent services.

Motivated by the above considerations, we propose a general
Transferable knowledgE Concept grapH framework to perform

---

<!-- PAGE 3 -->

Leveraging Transferable Knowledge Concept Graph Embedding for Cold-Start Cognitive Diagnosis

SIGIR ’23, July 23–27, 2023, Taipei, Taiwan

the domain-level zero-shot Cognitive Diagnosis (abbreviated as
TechCD). The TechCD framework consists of two stages: the
knowledge concept graph embedding (KCGE) stage and the do-
main adaptive diagnosis (DAD) stage. In the KCGE stage, a naive
yet effective graph convolutional network (GCN) [49] is first em-
ployed over the KCG for representation learning by iteratively
fusing neighboring aggregations in the KCG. To take full advantage
of the connections between exercises and the KCG, we treat each
exercise as part of the KCG for joint modeling with concept entities,
so that the exercises can absorb structural information from the
graph as their semantic descriptions. The most difficult aspect in
this stage is to guarantee the student state propagation property.
To this end, inspired by [54], we construct transferable student
states by discarding the bottom layers of GCN (specific patterns)
and only aggregating high-level ones (universal patterns) so that
cognitive signals can be successfully propagated to other domains.
We build domain-specific exercises and concepts by incorporating
comprehensive semantic information from the KCG so that their
embeddings comprise both universal and specific patterns, which
ensures domain adaptation. In the DAD stage, the above embeddings
are further fused to construct the traits of students (i.e., proficiency)
and exercises (e.g., difficulty) by predicting student performance.
In this way, the traits of students and exercises that need to be
diagnosed can be refined satisfying the diagnosis-oriented prop-
erty. It is worth mentioning that our general TechCD framework
is well defined to be implemented by combining with existing CD
solutions. For instance, we can have Tech-IRT by combining with
IRT [9], Tech-MIRT with MIRT [30] and Tech-NeuralCD with Neu-
ralCD [41], respectively. Finally, we conduct extensive experiments
on four real-world datasets. The experimental results not only prove
that TechCD is more effective in zero-shot student performance
prediction since it can well capture the universal students’ cogni-
tive signals for propagation but also show the superior application
property of the TechCD. For instance, TechCD can facilitate some
personalized learning guidance such as exercise recommendation
in cold-start scenarios.

2 RELATED WORK
2.1 Cognitive Diagnosis
Cognitive diagnosis (CD) is a fundamental task in many real-world
scenarios such as games [4], medical diagnosis [47], and especially,
education [10, 23]. The key spirit of CD is that it can be used to
profile students’ latent cognitive proficiency on specific knowledge
concepts, as well as be applied to reveal characteristics of the test
exercises such as difficulty and discrimination [9, 37] via exploiting
student testing logs. These refined trait features could be applied
to many intelligent applications, such as exercise recommenda-
tion [19, 46] and learning path suggestions [18, 39]. In the early
years, cognitive diagnosis was mostly developed from the psycho-
metric assumption that student cognitive states are stable in a short
period of time (e.g., an exam) and thus can be diagnosed [10]. In
general, these methods devote much effort to the design of student-
exercise interaction functions, which are expected to automatically
infer students’ knowledge states. For instance, Item Response The-
ory (IRT) [9], Multidimensional IRT (MIRT) [30] and Deterministic
Inputs, Noisy-And gate (DINA) [5] model the interaction of students
and exercises linearly (e.g., leveraging the logistic-like function).

Based on these traditional methods, some researchers introduce
deep learning into cognitive diagnosis. For instance, Neural Cogni-
tive Diagnosis (NeuralCD) [41] and Deep-IRT [38] exploit neural
networks to learn the interaction function and trait embeddings
automatically. Recently, to alleviate issues of student or exercise
cold-start, and data sparsity in real-world scenarios, some studies
have also considered incorporating exercise texts [22], the concep-
tual relations [10, 21] and more exceptions (e.g., slip and guess) [23]
in students’ learning process to enhance the interactive relations
between students and exercises. However, to the best of our knowl-
edge, research on how to cold-start a CD system remains unsolved.

2.2 Cold-Start Intelligent Systems
Cold-starting an intelligent system without historical interactions
available for new users or items is a prevalent and practical concern
in many domains [15, 32, 33, 51, 52]. This paper focuses on the
task of cold-starting a cognitive diagnosis system in a zero-shot
domain, which is of paramount importance to understanding the
first batch of students’ learning process, analyzing their knowledge
proficiency and further helping improve equity in education [12].
To tackle this issue, many strategies have been utilized such as meta-
learning [40], cross-domain modeling [25, 54] and reinforcement
learning [7]. We pay attention to the idea of cross-domain modeling,
which aims to characterize student state features based on their
historical behaviors from some available source domains and repre-
sent the test exercises in the target domain with available features.
The key challenge is to find a suitable intermediary to connect
the mature and target domains. Some related studies on student
performance prediction tasks [22, 35] utilize exercises’ textual con-
tents as the intermediary by learning universal and cross-domain
exercise embeddings. However, these methods may be limited due
to linguistic bias and cannot adapt to different domains effectively.

2.3 Pedagogical Knowledge Concept Graph
A pedagogical KCG contains numerous educational dependencies
(as relations) to connect knowledge concepts (as entities). In gen-
eral, the dependencies are constructed manually by domain experts
or automatically through data-driven algorithms based on pedagog-
ical prior knowledge [28], Among them, the most significant and
common dependencies include similarity [26], collaboration [17],
prerequisite [3], remedial [34] and hierarchy [21]. For example,
a pair of concepts involved in the same topic or area or overlap-
ping in some knowledge can be assigned with similarity depen-
dency relations. Recently, some KCGs have been established in both
academia and industry such as OpenEduKG1 and SongshuAI KCG2.
On the basis of KCGs, researchers attempt to incorporate them into
many educational application tasks and obtain significant improve-
ments [10, 26, 36]. Our TechCD properly incorporates a tailored
pedagogical KCG into CD linking each domain so as to mitigate
the domain-level zero-shot issue.

3 PRELIMINARIES
3.1 Cognitive Diagnosis Model
We first briefly introduce cognitive diagnosis models (CDMs). CDMs
are developed to discover student proficiency levels on specific

1https://open.edukg.cn
2https://www.songshuai.com/education

---

<!-- PAGE 4 -->

SIGIR ’23, July 23–27, 2023, Taipei, Taiwan

Weibo Gao et al.

knowledge concepts as well as exercise traits (e.g., difficulty) through
fully exploiting their responses to several exercises [37]. Due to the
real proficiency of students cannot be quantified explicitly, almost
all of the previous CDMs are trained through the student perfor-
mance prediction task, i.e., FC D M (𝒖, 𝒗) → ˆ𝑦𝑢𝑣, where 𝒖 and 𝒗 are
the latent traits of students and exercises, FC D M (·) is the diag-
nostic interaction function, and ˆ𝑦𝑢𝑣 is the predicted performance
score. These traits of students and exercises can be refined with
the optimization target of minimizing the difference between the
predicted probability ˆ𝑦𝑢𝑣 and the true response 𝑦𝑢𝑣 [10].

Generally, the differences between CDMs consist of the de-
sign of FC D M (·) and the representations of trait 𝒖 and 𝒗. For
example, IRT [9] uses single-dimension variables to represent the
trait features and logistic-like function as the interaction function:
, where 𝜃𝑖 characterizes student
𝑃 (𝑦𝑖 𝑗 |𝜃𝑖, 𝑎 𝑗 , 𝑏 𝑗 ) =
𝑖’s knowledge proficiency, and 𝑎 𝑗 and 𝑏 𝑗 represent exercise 𝑗’s dis-
crimination and difficulty. NeuralCD [41] exploits neural networks
to fit the interaction function automatically: ˆ𝑦𝑖 𝑗 = 𝐹 (𝒖𝑖, 𝒗 𝑗 , Θ𝐶𝐷 ),
where 𝒖 and 𝒗 are the latent traits of students and exercises respec-
tively, and 𝐹 (·) is multi-layer neural networks. To summarize, we
have the following general form of CDMs:

1
1+𝑒 −1.7𝑎 𝑗 (𝜃𝑖 −𝑏 𝑗 )

ˆ𝑦𝑢𝑣 = FC D M (𝒖, 𝒗, Θ∗),
(1)
where Θ∗ is the model parameter. To be noticed that, to ensure
psychometric interpretability of prediction, CDMs should strictly
follow the Monotonicity assumption [37]: the probability of cor-
rectly answering the exercise monotonically increases with student
knowledge proficiency, i.e., 𝜕 F
> 0.
𝜕𝒖

3.2 Knowledge Concept Graph
A pedagogical KCG contains knowledge concept entities and con-
ceptual dependency relations, whereas, in the domain-level cold-
starting settings, it additionally includes exercise entities and exercise-
concept association relations.

Definition 1 (Knowledge concept graph). Formally, the Knowl-

edge concept graph (KCG) can be represented as G = {E, R, P}. E
is the set of entities including knowledge concept sets C and their
associated exercises. R is the set of relations including educational de-
pendency relations between concepts (e.g., prerequisite and similarity)
and association relations between exercises and concepts. P is offered
in the form of entity-relation-entity triplet set P = {(ℎ, 𝑟, 𝑡)|ℎ, 𝑡 ∈
E, 𝑟 ∈ R}, e.g., (concept cube, similarity, concept cone) and (exercise
𝑒1, association, concept function).

3.3 Problem Definition
In the domain-level zero-shot cognitive diagnosis (DZCD) scenario,
we represent the mature/available source domain as S and the
cold-start/zero-shot target domain as T . The student sets and ex-
ercise sets in source domain S are denoted as US, VS, and in
target domain T are denoted as UT , VT , where UT ⊂ US and
VS ∩ VT = ∅. All student-exercise performance records for train-
ing (with label) are collected from the source domain, depicted as
𝐿S = {(𝑢𝑖, 𝑣 𝑗 , 𝑦𝑖 𝑗 )|𝑦𝑖 𝑗 ∈ {0, 1}, 𝑢𝑖 ∈ US, 𝑣 𝑗 ∈ VS }, where 𝑦𝑖 𝑗 = 1
represents student 𝑢𝑖 answers exercise 𝑣 𝑗 correctly, and 𝑦𝑖 𝑗 = 0 oth-
erwise. The student-exercise interactions from the target domain
(without label), i.e., 𝐿T = {(𝑢𝑖, 𝑣 𝑗 )|𝑢𝑖 ∈ UT, 𝑣 𝑗 ∈ VT }, are used to
evaluate prediction performance in DZCD scenarios. Hereby, our
TechCD model for the DZCD task is defined as:

Definition 2 (Domain-level zero-shot cognitive diagnosis).
Given student exercising records 𝐿S in the source domain and the
KCG, G, the goal of TechCD for the DZCD task is to make the diag-
nosis on student and exercise traits in the target domain T through
fully exploiting student-exercise interactive records 𝐿S in the source
domain S with student performance predictions.

4 THE TECHCD FRAMEWORK
4.1 Framework Overview
Conducting cognitive diagnosis in domain-level zero-shot settings
is non-trivial. It presents a critical challenge in learning portable
and transferable student embeddings from their exercising perfor-
mance records in the source domain. To overcome this problem,
we propose a TechCD framework that incorporates a tailored peda-
gogical knowledge concept graph (KCG) as a bridge between the
source and target domains. Our proposed TechCD framework con-
sists of two stages: knowledge concept graph embedding (KCGE)
and domain adaptive diagnosis (DAD). The KCGE stage (detailed
in Section 4.2) learns entity embeddings from the semantic and
structural information of the KCG. The DAD stage (detailed in Sec-
tion 4.3) then conducts diagnosis by predicting student exercise
performance. The entire structure of TechCD is depicted in Figure 2.
In the KCGE stage, the critical obstacle is to propagate student
cognitive states from the source domain to the target domain. For
this goal, we customize a KCG as the intermediary to link exer-
cises in various domains. We use a straightforward but effective
graph convolutional network (GCN) [49, 54] on the KCG to con-
struct transferable student cognitive embeddings that transcend the
exercise-related performance confined to the source domain. Be-
sides learning transferable student embedding, this stage generates
specific embeddings of exercise and concept entities by integrating
the structure and semantic information from the KCG.

With the above embeddings, the DAD stage further constructs
student proficiency traits and exercise difficulty and discrimina-
tion traits for domain-adaptive cognitive diagnosis with existing
diagnostic models. The entire model is trained through predicting
student performance on exercises, i.e., ˆ𝑦𝑢𝑣 = FC D M (𝐿S, G, Θ∗),
where parameter Θ∗ is optimized from the source domain S as:

Θ∗ = arg min

L (𝑦 (𝐿S), G).

(2)

Θ

It is worth mentioning that the KCGE stage and the DAD stage
are trained in an end-to-end fashion with the above Eq. (2). Thus, the
refined traits of students and exercises can be the diagnostic results.
After training, TechCD can conduct zero-shot student performance
predictions in the zero-shot target domain T .

4.2 Knowledge Concept Graph Embedding
This stage aims to identify universal student states present in exer-
cises of the source domain that can be transferred to the zero-shot
domain via the customized KCG. For this goal, we apply a multi-
layer GCN network3 over the KCG to learn entity embeddings.

Generally, the KCG contains concept and exercise entities, as well
as multiple conceptual dependency relations and exercise-concept
association relations, as shown in Figure 2 (a). The educational

3Actually, various KCG embedding techniques have been proposed to extract meaning-
ful embeddings [42, 49]. Since our focus is not to devise more sophisticated techniques
for graph network embedding, we simply use a popular GCN to learn entity represen-
tations, to verify the effectiveness of incorporating the KCG into the DZCD.

---

<!-- PAGE 5 -->

Leveraging Transferable Knowledge Concept Graph Embedding for Cold-Start Cognitive Diagnosis

SIGIR ’23, July 23–27, 2023, Taipei, Taiwan

Figure 2: The overview architecture of TechCD: (a) a knowledge concept graph (KCG) links the source and the target domains;
(b) the knowledge concept graph embedding for entity representation learning; (c) the domain adaptive diagnosis for DZCD.

dependency relations reflect student learning rules and knowl-
edge transferring logically, which can implicitly propagate student
states [8], while the exercise-concept associations can enhance ex-
ercise representations by absorbing structural and semantic infor-
mation from the KCG. Thereby, for each entity embedding, it needs
to discriminate different relations by separately fusing neighboring
information of each type of relation. We directly use the learnable
embedding 𝒆𝑖 ∈ R𝑑 of each entity 𝑒𝑖 as the input of GCN, i.e.,
(0)
= 𝑐𝑖 , where 𝑑 is the embedding dimensional size. We conduct
𝒛
𝑖
convolution operation [44] of GCN over the KCG 𝐿 times with each
iteration considering each type of relation separately, to aggregate
𝐿 hop neighborhood information and generate 𝐿 entity embed-
∈ R𝑑 denotes the 𝑙-th layer
dings, [𝒛
output of entity 𝑒𝑖 . The GCN iteratively aggregates neighboring
information of each entity 𝑒𝑖 for each type of relation separately to
enhance its representation through the message-passing-receiving
mechanism [13, 43] as follows:

], where 𝒛

, . . . , 𝒛

(𝐿)
𝑖

(1)
𝑖

(2)
𝑖

(𝑙 )
𝑖

, 𝒛

(𝑙 )
𝑖 =

𝒛

∑︁

𝑟 ∈ R𝑖

1
|P𝑟
𝑖 |

∑︁

(𝑒 𝑗 ,𝑟,𝑒𝑖 ) ∈ P𝑟
𝑖

W𝑟 𝒛

(𝑙 −1)
𝑗

,

(3)

where R𝑖 is the subset of R consisting of the relation types of entity
𝑒𝑖 . P𝑟
is the subset of P contains all the triplets (𝑒 𝑗 , 𝑟, 𝑒𝑖 ) of entity
𝑖
𝑒𝑖 with relation 𝑟 . For each relation 𝑟 , we use a learnable matrix
W𝑟 ∈ R𝑑 ×𝑑 to transform each concept/exercise entity feature
vector to the same free embedding space.

After obtaining the above refined entity embeddings, the focus
is on representing transferable student embeddings to address the
challenge of student state propagation. We resort to the bottom-
discarding operation [54] which is naturally compatible. It argues
that the bottom layers of GCN preserve more domain-specific in-
formation, while the upper layers better represent universal and
transferable information. This is intuitively reasonable because in-
creasing the number of GCN layers can lead to over-smoothing,
resulting in the loss of discriminative information [16], which makes
it promising to effectively propagate student cognitive signals to
zero-shot domains. Thus, we discard the lower-level entity embed-
dings by settings a hyper-parameter 𝜆 to aggregate transferable
#
embeddings 𝒛
𝑖 . Additionally, we fuse all layer output embeddings
of GCN as well as the original entity embedding, resulting in a

complete semantic representation 𝒛∗

#
𝑖 =

𝒛

1
𝐿 − 𝜆 + 1

𝑖 , as Eq. (4).
𝐿
1
∑︁
𝐿 + 1

𝑖 =

, 𝒛∗

𝑙=0

𝐿
∑︁

(𝑙 )
𝑖

𝒛

𝑙=𝜆

(𝑙 )
𝑖

𝒛

.

(4)

Hereby, we construct the transferable cognitive state of student

𝑢 by absorbing general knowledge from the KCG as:

𝒉𝑢 =

1
|H S
𝑢 |

∑︁

#
𝑣 ,

𝒛

(5)

𝑣 ∈ HS
𝑢
where H S
𝑢 is the exercise set that student 𝑢 has interacted with
#
𝑣 to represent student states, as
in the source domain S. We use 𝒛
it captures entity-specific information in the bottom-layer output,
while 𝒛∗
𝑣 contains more general high-order information.

Besides generating student embeddings, this stage also outputs
exercise and knowledge concept representations. For the exercise
entity 𝑣, we directly assign its corresponding embedding 𝒛∗
𝑣 from
the entity 𝑒𝑣 in the KCG to it similar to [54], i.e., 𝒉𝑣 = 𝒛∗
𝑣. Note
that exercise embeddings incorporate both general and domain-
specific information by absorbing full semantic representations of
exercise entities in the KCG, which can fill in the domain-adaption
requirements intuitively. Similarly, we represent each concept 𝑐’s
𝑐 , i.e., 𝒉𝑐 = 𝒛∗
embedding 𝒉𝑐 with its full semantic representation 𝒛∗
𝑐 .

4.3 Domain Adaptive Diagnosis
In this stage, we conduct domain-adaptive cognitive diagnosis with
existing cognitive diagnosis models.
4.3.1 Diagnosed Trait Representation Modeling. In general,
a cognitive diagnosis model (CDM) takes the traits of students
(i.e., proficiency) and exercises (e.g., difficulties and discrimination)
as the basic input [41]. Thus, it is crucial to represent the above
traits that need to be diagnosed via the generated embeddings from
the KCGE stage. Inspired by [10, 21], to generate the proficiency
factor on each concept of each student, we incorporate the embed-
dings of knowledge concept entities into the transferable student’s
embedding. Thus, the student proficiency trait can be modeled as:

𝒑𝑢 = (𝑝𝑢1; 𝑝𝑢2; · · · ; 𝑝𝑢 | C | ), where 𝑝𝑢𝑐 = 𝑓𝑢 (𝒉𝑢 ⊕𝒉𝑐 ) ∈ (0, 1). (6)
In the above Eq. (6), vector 𝒑𝑢 is student 𝑢’s proficiency on |C|
knowledge concepts in the KCG. Each element of 𝒑𝑢 , i.e., 𝑝𝑢𝑐 , de-
notes student 𝑢’s mastery level on concept 𝑐. A full connection

---

<!-- PAGE 6 -->

SIGIR ’23, July 23–27, 2023, Taipei, Taiwan

Weibo Gao et al.

layer [50] 𝑓𝑢 (·) is used to fuse knowledge concept semantics into
the student embedding with concatenation ⊕. Similarly, we also
fuse knowledge concept information into exercise embeddings to
calculate each exercise 𝑣’s difficulty trait 𝒅𝑣 on all concepts with
the full connection layer 𝑓𝑣 (·) as Eq. (7).

𝒅𝑣 = (𝑑𝑣1; 𝑑𝑣2; · · · ; 𝑑𝑣 | C | ), where 𝑑𝑣𝑐 = 𝑓𝑣 (𝒉𝑣 ⊕ 𝒉𝑐 ) ∈ (0, 1).

(7)

Besides, the discrimination 𝛽𝑣 of each exercise 𝑣 is directly obtained
by transforming the exercise embedding to a latent factor with a
neural network 𝑓𝛽 (·), i.e., scalar 𝛽𝑣 = 𝑓𝛽 (𝒉𝑣) ∈ (0, 1), similar to [21].

4.3.2 Diagnostic Adaptor. Different diagnostic models charac-
terize student and exercise features in different forms. Our aim is
to establish a connection between students’ cognitive proficiency,
exercise traits, and the input forms of existing diagnostic mod-
els, through introducing the diagnostic adaptor. In general, for the
given student 𝑢 and exercise 𝑣, the CDM adaptor predicts student
performance score ˆ𝑦𝑢𝑣 as Eq. (8):

ˆ𝑦𝑢𝑣 = FC D M (𝜙𝑢 (𝒑𝑢 ), 𝜙𝑣 (𝒅𝑣), 𝛽𝑣),

(8)

where FC D M (·) represents the existing diagnostic model and can
be specified with many models like IRT [9], MIRT [30], etc. To cover
different diagnostic models, we employ two transform functions,
𝜙𝑢 (·) and 𝜙𝑣 (·), to standardize the form of student proficiency 𝒑𝑢
and exercise difficulty 𝒅𝑣 so as to satisfy the input form of the
adopted model. Besides, to ensure the monotonicity assumption
of cognitive diagnosis, we restrict each parameter of FC D M to be
positive, so that 𝜕 FCDM
> 0. Eq. (8) can be used to infer students’
𝜕𝜙𝑢 (𝒑𝑢 )
performance on exercises in both the source and target domains.

Finally, we use the popular cross-entropy loss function to opti-
mize the whole model by minimizing the difference between the
predicted probability ˆ𝑦𝑢𝑣 and the true response 𝑦𝑢𝑣.

L = −

∑︁

(𝑢,𝑣,𝑦𝑢𝑣 ) ∈𝐿S

(𝑦𝑢𝑣 log ˆ𝑦𝑢𝑣 + (1 − 𝑦𝑢𝑣) log (1 − ˆ𝑦𝑢𝑣)) .

(9)

By optimizing with the above loss, these input traits of the student
and the exercise in Eq. (8), i.e., 𝒑𝑢 , 𝒅𝑣 and 𝛽𝑣, can be jointly refined
serving as the diagnostic results of students and exercises.

Instantiating the TechCD. Taking the student trait 𝜙𝑢 (𝒑𝑢 )
4.3.3
and exercise traits 𝜙𝑣 (𝒅𝑣) and 𝛽𝑣 as input factors, we specify the
diagnostic adaptor FC D M (·) in Eq. (8) of TechCD with IRT, MIRT
and NeuralCD as follows:

IRT [9] takes the unidimensional student proficiency, exercise
difficulty and discrimination as input. To specify with IRT, we
project 𝒑𝑢 and 𝒅𝑣 to scalars 𝑝𝑢 and 𝑑𝑣 respectively by setting 𝜙𝑢
and 𝜙𝑣 as mean pooling. The FC D M (·) is a logistic-like function:
ˆ𝑦𝑢𝑣 = sigmoid(𝛽𝑣 · (𝑝𝑢 − 𝑑𝑣)).

MIRT [30] models the interaction between multidimensional
student proficiency 𝒑𝑢 and exercise difficulty 𝒅𝑣 using a logistic-
like function. We set the output dimensions of 𝜙𝑢 and 𝜙𝑣 as 𝐷 > 1.
The FC D M (·) is shown as: ˆ𝑦𝑢𝑣 = sigmoid(𝒑𝑇

𝑢 𝒅𝑣 + 𝛽𝑣).

NeuralCD [41] directly takes student proficiency 𝒑𝑢 and exer-
cise difficulty as input. Additionally, it requires masking the irrel-
evant knowledge proficiency by a vector 𝑸 𝑣 = {0, 1} | C | ×1 where
𝑞𝑣,𝑐 = 1 if exercise 𝑣 associates concept 𝑐 and 𝑞𝑣,𝑐 = 0 otherwise. C

Table 1: Some basic statistics of the datasets.

Datasets

CM

AM

Junyi ASSIST

#Student
#Exercise
#Knowledge concept
#Record
#Record per student

21,068
6,257
1,251
351,146
16.7

21,059
3,263
990
171,380
8.1

10,000
706
706
353,835
35.4

5,730
4,973
122
225,314
39.3

is the knowledge concept set. The FC D M (·) is a multi-layer neu-
ral networks 𝜙 with non-negative weights to keep explainability:
ˆ𝑦𝑢𝑣 = 𝜙 (𝑸𝒗 ◦ (𝒑𝑇

𝑢 − 𝒅𝑣) · 𝛽𝑣), where ◦ is element-wise product.

5 EXPERIMENTS
We conduct comprehensive experiments to address the following
research questions:
• RQ1 Can the TechCD framework effectively handle the domain-

level zero-shot cognitive diagnosis task?

• RQ2 How about the effectiveness of modeling the KCG by the

TechCD framework?

• RQ3 Can the TechCD utilize the out-of-domain datasets for the

performance improvement?

• RQ4 How to apply TechCD to provide personalized guidance?
5.1 Datasets
5.1.1 Basic Description. We conduct experiments on the following
four real-world representative datasets:
• Core Math (CM) and Advanced Math (AM) are two subsets of
the MATH-2021 dataset, collected supplied by iFLYTEK Co., Ltd.,
which is collected from the iFLYTEK Learning Machine4. They
have overlapping students while their exercises have no overlap.
• Junyi5 [2] contains student online learning logs on mathematical
exercises which is crawled from a Chinese online learning plat-
form. Nowadays Junyi is widely used in the evaluation of online
education tasks [10, 21]. We randomly select 10,000 students’
exercising records from Junyi for experiments.

• ASSISTments-2012-2013 (ASSIST)6 is an open dataset collected
by the ASSISTments online tutoring systems, which has become
popular benchmark datasets for cognitive diagnosis. We ran-
domly select about 5,000 exercises and their related records.

All the datasets provide student exercising records and exercise-
concept correlations, where each exercise associates one knowledge
concept. Besides, AM and CM provide the exercises’ contents, and
Junyi provides the conceptual prerequisite and similarity relations
labeled by experts. Each dataset is treated as a domain, i.e., the
source or target domain. Among them, there is no overlap between
the students in the Junyi and ASSIST datasets and those in the
MATH dataset. For each dataset, we reserve only the first attempt of
each exercise for each dataset to ensure that the attribute state of stu-
dents is static following the [10, 41]. We evaluate the performance
of DZCD on the target domain using the refined model trained
in the source domain. We split each source domain’s dataset by
randomly selecting two historical interactions from each student’s
logs for validation, with the remaining data serving as the training

4https://xxj.xunfei.cn/
5https://pslcdatashop.web.cmu.edu/DatasetInfo?datasetId=1198
6https://drive.google.com/file/d/1cU6Ft4R3hLqA7G1rIGArVfelSZvc6RxY/view

---

<!-- PAGE 7 -->

Leveraging Transferable Knowledge Concept Graph Embedding for Cold-Start Cognitive Diagnosis

SIGIR ’23, July 23–27, 2023, Taipei, Taiwan

Table 2: Some detailed statistics of the KCG.

• Random: The random method predicts the students’ scores ran-

Entity

#Concept
#Exercise
#Total

Relation #Total

2,594
15,199
17,793

5

Triple

#Conceptual dependency
7,926
#Exercise-concept association 15,469
23,395
#Total

set, similar to the widely used leave-one-out evaluation [14, 31].
Besides, to train the Oracle models (Section 5.2), we also split the
target domain’s dataset into training (70%), validation (10%), and
test sets (20%), similar to [54]. The basic statistics of the datasets
are presented in Table 1.
5.1.2 Knowledge Concept Graph Construction. To bridge exercises
across different domains, it needs to tailor a unified knowledge
concept graph (KCG) linking each domain. For this purpose, we
adopt a hierarchical mathematical KCG (abbreviated as MathKCG)
to connect all domains (i.e., all the datasets). Specifically, MathKCG
is published by the online education platform, i.e., Luna7. It cov-
ers 39.5% knowledge concepts in our datasets and provides two
significant types of conceptual relations, i.e., hierarchy [21] and
similarity [26] relations. We first align each exercise-related con-
cept in datasets and concepts in MathKCG based on conceptual
names. Then, for the isolated concepts in each dataset that cannot
be linked to MathKCG, we build conceptual similar and prerequisite
relations [3] between them via exploiting student performance logs
using the statistical method [10]. Hereby, based on the generated
relations, the MathKCG, and those relations provided by Junyi,
each concept can be linked to a KCG. Additionally, the exercises
are linked to their associated knowledge concept in the KCG. The
final KCG includes concept and exercise entities, and four types
of conceptual relations (i.e., hierarchy-in-MathKCG, similarity-in-
MathKCG, the constructed similarity and prerequisite relations via
our datasets) as well as the exercise-concept association relations.
We conduct all experiments on the same KCG. The detailed

statistics of the KCG are presented in Table 2.

5.2 Baselines
To verify the effectiveness of our model, we present three implemen-
tations based on TechCD framework that combine typical diagnosis
methods. In particular, we implement Tech-IRT, Tech-MIRT and
Tech-NeuralCD following IRT, MIRT and NeuralCD, respectively.
• IRT [9]: IRT models unidimensional students and exercises’ fea-

tures with a logistic-like function.

• MIRT [30]: As the multidimensional extension of IRT, MIRT
models multiple knowledge proficiency of students and exercises.
• NeuralCD [41]: NeuralCD is one of the most popular deep learning-
based CD methods, which models high-order and complex student-
exercise interaction functions with a multilayer perceptron (MLP).

We select a series of baselines for comparison. Among them, the
random and oracle methods indicate the lower and upper bounds of
performance, following the previous setups [54]. For each baseline
(excluding Random), we also select IRT, MIRT and NeuralCD as
their diagnostic functions. The details are listed as follows:

7https://luna.bdaa.pro

domly from 𝑈 𝑛𝑖 𝑓 𝑜𝑟𝑚(0, 1).

• Oracle: The oracle baseline is trained with the student-exercise
interactive records of both source and target domains. Hence, it
should perform better than other compared methods.

• NLP-based: Some related researches [22, 35] utilize exercises’ tex-
tual contents as an intermediary of the source and target domain
for student performance predictions. Thus, we adopt Bert [6]
as the encoder to encode exercises’ textual contents to gener-
ate their embeddings. To implement the NLP-based diagnosis
method, we use learnable embeddings as student proficiency and
introduce two functions to transform textual content features
into exercises’ difficulties and discrimination.

• GCN-based: We add a baseline that utilizes only the last-layer
output as entities’ embeddings and does not differentiate be-
tween the different relations in the KCG for comparison.

5.3 Evaluation Metrics and Other Settings
5.3.1 Metrics. To evaluate model performance, we adopt differ-
ent metrics from the perspectives of classification and regression
following the [10]. From the classification perspective, a student an-
swering incorrectly or correctly can be represented as a negative (0)
or positive (1) instance respectively. Thus, we use Accuracy (ACC)
and Area Under the ROC Curve (AUC) for measuring. From the
regression perspective, we select Root Mean Square Error (RMSE)
to quantify the distance between the predicted score (i.e., the prob-
ability that a student answers correctly) and the actual one.

Implementation Details. For those models that employ Neural-
5.3.2
CD and MIRT as diagnostic functions, we set the dimensions of
student and exercise vectors as the number of diagnosed knowledge
concepts |C|, similar to [41]. The dimensions of neural network
layers are 1024 and 512 for all models with NeuralCD diagnostic
function. Regarding the GCN layers, under the "AM as source" set-
ting, we use 5 layers for 𝐿 and a discarding parameter 𝜆 of 3. Under
the "CM as source" setting, we use 5 layers for 𝐿 and a discarding
parameter 𝜆 of 2. For training, all network parameters are initialized
with Xavier initialization [11]. Furthermore, we set the mini-batch
size as 256 and the learning rate as 0.0005 for each model. Each
model is implemented by PyTorch [29] and optimized by Adam
optimizer [20]. All experiments are run on a Linux server with two
3.00GHz Intel Xeon Gold 5317 CPUs and one Tesla A100 GPU. The
code is available at https://github.com/bigdata-ustc/TechCD.

5.4 Student Performance Prediction (RQ1)
To answer RQ1, we compare the performance of our model with sev-
eral baselines on the domain-level zero-shot student performance
prediction task. We switch CM and AM datasets as the target do-
main since their students overlap. It is worth mentioning that Junyi
and ASSIST are used in Section 5.6 to demonstrate how TechCD
utilizes out-domain datasets from other platforms for the DZCD
task, as they are collected from different platforms. The overall
prediction performance is reported in Table 3. The combination
of S-CM (AM) and T-AM (CM) denotes CM (AM) as the source
domain for training and AM (CM) as the target domain for testing.
We have the following observations: (1) For different diagnostic
implementations (i.e., IRT, MIRT and NeuralCD as Diagnostic func-
tion), our proposed TechCD framework almost outperforms all
baseline models (including Random, NLP-based and GCN-based

---

<!-- PAGE 8 -->

SIGIR ’23, July 23–27, 2023, Taipei, Taiwan

Weibo Gao et al.

Table 3: Performance comparison. The best zero-shot student performance prediction is highlighted in bold, the runner-up is
underlined, and ↑ (↓) means the higher (lower) score the better performance, the same as below. * indicates the oracle result.

Dataset

Metric Oracle NLP GCN TechCD Oracle NLP GCN TechCD Oracle NLP GCN TechCD

IRT

MIRT

NeuralCD

Random

S-CM
T-AM

S-AM
T-CM

ACC (%) ↑ 77.89∗ 59.84 56.72 63.45
AUC (%) ↑ 84.98∗ 65.32 56.62 67.42
RMSE (%) ↓ 38.91∗ 47.98 50.75 47.59
ACC (%) ↑ 77.67∗ 55.88 56.92 57.72
AUC (%) ↑ 85.50∗ 50.68 56.62 58.99
RMSE (%) ↓ 39.08∗ 53.21 54.46 52.85

73.83∗ 56.44 56.74 64.73
79.26∗ 65.52 56.60 68.90
48.40∗ 48.30 50.79 47.06
74.07∗ 55.88 56.92 57.78
81.16∗ 60.56 56.62 59.02
47.93∗ 48.52 50.50 52.85

74.65∗ 56.44 57.05 57.06
81.07∗ 57.09 57.44 53.68
41.17∗ 49.69 50.72 49.49
74.34∗ 55.88 56.80 56.99
81.61∗ 53.67 57.55 52.40
41.52∗ 49.87 50.72 49.57

50.13
50.14
57.70

49.91
49.89
57.78

Figure 3: The ACC and RMSE comparisons on S-AM and T-
CM. The darker (lighter) means the better for ACC (RMSE).
models) on both CM and AM target domains, which indicates the
effectiveness of TechCD on predicting student performance under
the cold-start setting. (2) Both GCN-based and TechCD employ the
knowledge concept graph linking both source and target domains.
However, GCN-based methods are unable to discard bottom-layer
information and discriminate different relations in the KCG. In con-
trast, TechCD outperforms GCN-based methods, which positively
supports its effectiveness.

In the following parts, we primarily present the experimental
results of Tech-NeuralCD as the representative ones, since other
diagnosis functions can be abstracted as the special cases of Neu-
ralCD [41].

5.5 Bottom-Layer Discarding Analysis (RQ2)
The TechCD framework relies on the bottom-layer discarding op-
eration [54] to generate transferable embeddings. We refer to the
operation of discarding bottom-layer embedding of student and
exercise embeddings as DS and DE, respectively. To evaluate the
impact of this operation, we perform various experiments with
different combinations of DS and DE. The comparisons of ACC and
RMSE scores under the setting of S-AM and T-CM are visualized
in Figure 3. The experimental results indicate that the best perfor-
mance is achieved by only discarding the bottom-layer output from
the KCG for students (DS), highlighting the effectiveness of extract-
ing transferable information. However, when both DS and DE are
used simultaneously, the performance is weakened, emphasizing
the importance of maintaining specific patterns for exercises.

5.6 Improving with Out-Domain Datasets (RQ3)
The tailored KCG can link different domains including those within
the same platform and those across platforms. The previous experi-
ments focus on evaluating performance within source and target
domains that share overlapping students. This part shows how
powerful is TechCD for utilizing out-domain datasets from other
platforms under two typical cold-start scenarios [54].
5.6.1 Accessible Student Records (ASD). In the scenario, student
performance records 𝐿S in the source domain S and out-domain
records 𝐿O in the target domain O are both available. Thus, 𝐿S and

Table 4: Performance of TechCD trained on different settings.

Training

Target ACC (%) ↑ AUC (%) ↑ RMSE (%) ↓

AM
Random
AM
CM
AM
(LA) Junyi
AM
(LA) Assist
AM
(ASD) CM+Junyi
(ASD) CM+Assist
AM
(ASD) CM+Junyi+Assist AM

50.13
57.06
53.71
54.83
56.60
57.08
56.73

50.14
53.68
50.49
49.77
52.10
51.95
52.11

57.70
49.49
49.80
49.85
49.84
49.69
49.57

𝐿O can be used to jointly train the model with Eq. (2) as:

Θ∗ = arg min

Θ

L (𝑦 (𝐿S + 𝐿O), G).

(10)

5.6.2 Limited Access (LA). In the setting, student performance
records are unavailable due to privacy protection policies. To ad-
dress this scenario, the out-domain O are introduced to refine the
KCG by replacing source domain’s datasets 𝐿S with out-domain
datasets 𝐿O in Eq. (2) as:

Θ∗ = arg min

Θ

L (𝑦 (𝐿O), G).

(11)

Table 4 lists the performance of Tech-NeuralCD, indicating the
following observations. In the ASD setting, the out-domain datasets
can partly improve the prediction performance of TechCD. In the LA
setting, with the out-domain datasets, TechCD can get a promising
performance compared with random predictions. These findings
confirm the KCG can absorb out-domain datasets effectively.

5.7 Popular Applications of TechCD (RQ4)
The above experiments have proved that TechCD can complete the
DZCD task effectively. In this part, we demonstrate two special
applications of our TechCD that are in need of industrial practice.

5.7.1 Diagnostic Report Generation. Providing diagnostic reports
to students via the CD method is one of the most typical intelli-
gent applications in intelligent education, which can help students
understand their learning process. Traditional diagnosis methods di-
agnose students’ proficiency on knowledge concepts limited in the
source domain, while our TechCD can further infer students’ cog-
nitive states in the target domain. We randomly select one student
in the CM datasets to generate her diagnostic reports using Tech-
NeuralCD and traditional NeuralCD trained on the CM dataset.
We also sample a subgraph of KCG which covers some knowledge
concepts of CM and Junyi with similarity and prerequisite relations.
Figure 4 (a) and (b) present diagnostic reports of both models and

---

<!-- PAGE 9 -->

Leveraging Transferable Knowledge Concept Graph Embedding for Cold-Start Cognitive Diagnosis

SIGIR ’23, July 23–27, 2023, Taipei, Taiwan

Table 5: Exercise recommendation of TechCD.

S-CMT-AM

1○ 2○ 3○ 4○ 5○ 6○ 7○ 8○ 9○ 10○

Figure 4: The example of diagnostic reports.
the cognitive graph of Tech-NeuralCD respectively. From the figure,
we observe that: (1) For the mastery levels of knowledge concepts
(1, 2 and 3) in CM, Tech-NeuralCD and NeurcalCD can output simi-
lar diagnosis results, indicating that both models can perform well
on in-domain datasets. (2) For those knowledge concepts (4 and 5)
sampled from Junyi (as a cold-start domain), NeuralCD is unable to
provide a diagnosis, while Tech-NeuralCD is still able to perform
effectively. (3) In the cognitive graph of Tech-NeuralCD, the deeper
the color of the concept entity, the higher its cognitive level. We
find the diagnosis results reasonable and interpretable. For exam-
ple, the student’s proficiency on concepts 3 and 4 is poor, which
is reflected in her poor mastery of concept 5. This is expected as
mastering concepts 3 and 4 are prerequisites for learning concept 5.
Additionally, the mastery levels on concepts 6 and 7 are similar as
they belong to the same topic (i.e., absolute value).
5.7.2 Exercise Recommendation. The diagnostic results can be uti-
lized to suggest appropriate exercises to students, rather than re-
lying on their own search efforts. A proper recommender system
generally takes into account two key objectives: (O1: smoothness)
the difficulty levels of a series of recommendations should avoid
drastic variations as students learn knowledge gradually [53]; (O2:
engagement) the recommendations should not be too challenging or
easy to keep students’ enthusiasm [18]. For these goals, we imple-
ment a simple yet effective strategy8 to recommend 𝑥 exercises for
each student. Concretely, with a refined CDM, we first predict each
student’s performance on each exercise as Eq. (8). All exercises can
be divided into two sets that answer correctly (positive samples)
or not (negative samples) according to prediction results. Then, we
sample 𝑥
2 exercises from each of the positive and negative samples.
For each sampling, we require the selected exercise’s difficulty to
be close to a threshold (0.5 in this paper) to ensure the smoothness
objective. Finally, we can get the recommendation lists for each
student, which satisfy the above objectives.

We conduct recommendations on the challenging target domain
that traditional CDMs are unable to handle. Table 5 lists ten exercise
recommendations on T-AM for a randomly selected student using
the refined Tech-NeuralCD model trained on S-CM dataset. The
table also includes the diagnosed exercise difficulties and student
mastery levels of the associated concepts, as well as the student’s
true performance on the exercises as recorded in the T-AM dataset.
We can see that: (1) The recommended exercises are tailored to the
student’s proficiency, neither too easy nor too difficult. Some of
them will challenge the student, while others will serve as "gifts"

8TechCD can support many complex and popular exercise recommendation approaches
like [1, 18], this part uses the simple recommendation method as an example.

×

×

30

220

123 2,003 3,020 175

Exercise id
232 1,632 2,432
250
67.23 38.24 40.07 23.00 48.63 57.30 84.33 54.27 48.24 57.78
Mastery (%)
Difficulty (%) 50.20 51.30 49.93 50.21 49.98 50.00 50.03 50.10 49.99 49.93
Performance ✓

×
that can help increase her engagement with the material. (2) For
exercises that the student answers correctly (incorrectly), the profi-
ciency of the corresponding concept is almost higher (lower) than
the exercise’s difficulty, indicating that students answer correctly
when their proficiency meets the difficulty. It confirms TechCD’s
diagnoses are effective in the cold-start domain.

✓

✓

✓

✓

✓

×

6 CONCLUSION
This paper presents a study on the domain-level zero-shot cogni-
tive diagnosis (DZCD) task. DZCD is an important task for the
lack of student behavior data in the target domain due to the ab-
sence of student-exercise interactions or unavailability of exercising
records for training. To tackle this, we propose a general and trans-
ferable framework TechCD that utilizes a pedagogical knowledge
concept graph (KCG) to connect different domains and propagate
students’ universal cognitive states. The learned student embed-
dings by TechCD are transferable, while the exercise embeddings
are domain-specific, enabling TechCD to perform domain-adaptive
zero-shot cognitive diagnosis in the target domain. Finally, exten-
sive experiments on real-world datasets not only prove that TechCD
can effectively make the cognitive diagnosis task for a zero-shot
domain and outperform several alternative baselines, but also show
the superior application potential such as personalized exercise rec-
ommendation of TechCD. In our future research, we will focus on
developing more advanced methods for constructing educational
KCGs that can better connect different domains. Additionally, we
plan to explore more sophisticated approaches for integrating con-
ceptual relationships to further improve TechCD’s performance in
the DZCD scenario. Ultimately, we hope that our work will inspire
and inform future studies and applications in this area.

Acknowledgements. This research was partially supported by
grants from the National Key Research and Development Program
of China (No. 2021YFF0901003), National Natural Science Founda-
tion of China (No. 62202443), and Open Research Fund of the State
Key Laboratory of Cognitive Intelligence (iED2022-002).

REFERENCES
[1] Haoyang Bi, Haiping Ma, Zhenya Huang, Yu Yin, Qi Liu, Enhong Chen, Yu Su,
and Shijin Wang. 2020. Quality meets Diversity: A Model-Agnostic Framework
for Computerized Adaptive Testing. In 2020 IEEE International Conference on Data
Mining (ICDM). IEEE, 42–51.

[2] Haw-Shiuan Chang, Hwai-Jung Hsu, and Kuan-Ta Chen. 2015. Modeling Exercise

Relationships in E-Learning: A Unified Approach.. In EDM. 532–535.

[3] Penghe Chen, Yu Lu, Vincent W Zheng, and Yang Pian. 2018. Prerequisite-driven
deep knowledge tracing. In 2018 IEEE International Conference on Data Mining
(ICDM). IEEE, 39–48.

[4] Shuo Chen and Thorsten Joachims. 2016. Predicting matchups and preferences
in context. In Proceedings of the 22nd ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining. 775–784.

[5] Jimmy De La Torre. 2009. DINA model and parameter estimation: A didactic.

Journal of educational and behavioral statistics 34, 1 (2009), 115–130.

[6] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018. Bert:
Pre-training of deep bidirectional transformers for language understanding. arXiv
preprint arXiv:1810.04805 (2018).

---

<!-- PAGE 10 -->

SIGIR ’23, July 23–27, 2023, Taipei, Taiwan

Weibo Gao et al.

[7] Nan Ding and Radu Soricut. 2017. Cold-start reinforcement learning with softmax
policy gradient. Advances in Neural Information Processing Systems 30 (2017).

[8] Henry C Ellis. 1965. The transfer of learning. (1965).
[9] Susan E Embretson and Steven P Reise. 2013. Item response theory. Psychology

Press.

[10] Weibo Gao, Qi Liu, Zhenya Huang, Yu Yin, Haoyang Bi, Mu-Chun Wang, Jianhui
Ma, Shijin Wang, and Yu Su. 2021. Rcd: Relation map driven cognitive diagnosis
for intelligent education systems. In Proceedings of the 44th International ACM
SIGIR Conference on Research and Development in Information Retrieval. 501–510.
[11] Xavier Glorot and Yoshua Bengio. 2010. Understanding the difficulty of training
deep feedforward neural networks. In Proceedings of the thirteenth International
conference on artificial intelligence and statistics. JMLR Workshop and Conference
Proceedings, 249–256.

[12] Margaret Grogan. 1999. Equity/equality issues of gender, race, and class. Educa-

tional Administration Quarterly 35, 4 (1999), 518–536.

[13] Xiangnan He, Kuan Deng, Xiang Wang, Yan Li, Yongdong Zhang, and Meng
Wang. 2020. Lightgcn: Simplifying and powering graph convolution network for
recommendation. In Proceedings of the 43rd International ACM SIGIR conference
on research and development in Information Retrieval. 639–648.

[14] Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie, Xia Hu, and Tat-Seng
Chua. 2017. Neural collaborative filtering. In Proceedings of the 26th International
conference on world wide web. 173–182.

[15] Minlie Huang, Xiaoyan Zhu, and Jianfeng Gao. 2020. Challenges in building
intelligent open-domain dialog systems. ACM Transactions on Information Systems
(TOIS) 38, 3 (2020), 1–32.

[16] Wenbing Huang, Yu Rong, Tingyang Xu, Fuchun Sun, and Junzhou Huang.
2020. Tackling over-smoothing for general graph convolutional networks. arXiv
preprint arXiv:2008.09864 (2020).

[17] Xiaoqing Huang, Qi Liu, Chao Wang, Haoyu Han, Jianhui Ma, Enhong Chen, Yu
Su, and Shijin Wang. 2019. Constructing Educational Concept Maps with Multiple
Relationships from Multi-Source Data. In 2019 IEEE ICDM. IEEE, 1108–1113.
[18] Zhenya Huang, Qi Liu, Chengxiang Zhai, Yu Yin, Enhong Chen, Weibo Gao,
and Guoping Hu. 2019. Exploring multi-objective exercise recommendations in
online education systems. In Proceedings of the 28th ACM International Conference
on Information and Knowledge Management. 1261–1270.

[19] Yujia Huo, Derek F Wong, Lionel M Ni, Lidia S Chao, and Jing Zhang. 2020. Knowl-
edge modeling via contextualized representations for LSTM-based personalized
exercise recommendation. Information Sciences 523 (2020), 266–278.

[20] Diederik P Kingma and Jimmy Ba. 2014. Adam: A method for stochastic opti-

mization. arXiv preprint arXiv:1412.6980 (2014).

[21] Jiatong Li, Fei Wang, Qi Liu, Mengxiao Zhu, Wei Huang, Zhenya Huang, Enhong
Chen, Yu Su, and Shijin Wang. 2022. HierCDF: A Bayesian Network-based
Hierarchical Cognitive Diagnosis Framework. In Proceedings of the 28th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining. 904–913.
[22] Qi Liu, Zhenya Huang, Yu Yin, Enhong Chen, Hui Xiong, Yu Su, and Guoping Hu.
2019. Ekt: Exercise-aware knowledge tracing for student performance prediction.
IEEE Transactions on Knowledge and Data Engineering 33, 1 (2019), 100–115.
[23] Qi Liu, Runze Wu, Enhong Chen, Guandong Xu, Yu Su, Zhigang Chen, and Guop-
ing Hu. 2018. Fuzzy cognitive diagnosis for modelling examinee performance.
ACM Transactions on Intelligent Systems and Technology (TIST) 9, 4 (2018), 1–26.
[24] Ye Liu, Han Wu, Zhenya Huang, Hao Wang, Jianhui Ma, Qi Liu, Enhong Chen,
Hanqing Tao, and Ke Rui. 2020. Technical phrase extraction for patent mining:
A multi-level approach. In 2020 IEEE International Conference on Data Mining
(ICDM). IEEE, 1142–1147.

[25] Nima Mirbakhsh and Charles X Ling. 2015. Improving top-n recommendation for
cold-start users via cross-domain information. ACM Transactions on Knowledge
Discovery from Data (TKDD) 9, 4 (2015), 1–19.

[26] Hiromi Nakagawa, Yusuke Iwasawa, and Yutaka Matsuo. 2019. Graph-based
Knowledge Tracing: Modeling Student Proficiency Using Graph Neural Network.
In 2019 IEEE/WIC/ACM International Conference on Web Intelligence (WI). IEEE,
156–163.

[27] Tuan Nguyen. 2015. The effectiveness of online learning: Beyond no significant
difference and future horizons. MERLOT Journal of online learning and teaching
11, 2 (2015), 309–319.

[28] Liangming Pan, Chengjiang Li, Juanzi Li, and Jie Tang. 2017. Prerequisite relation
learning for concepts in moocs. In Proceedings of the 55th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers). 1447–1456.

[29] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory
Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. 2019.
Pytorch: An imperative style, high-performance deep learning library. Advances
in neural information processing systems 32 (2019).

[30] Mark D Reckase. 2009. Multidimensional item response theory models.

In

Multidimensional item response theory. Springer, 79–112.

[31] Steffen Rendle, Christoph Freudenthaler, Zeno Gantner, and Lars Schmidt-Thieme.
2012. BPR: Bayesian personalized ranking from implicit feedback. arXiv preprint
arXiv:1205.2618 (2012).

[32] Andrew I Schein, Alexandrin Popescul, Lyle H Ungar, and David M Pennock.
2002. Methods and metrics for cold-start recommendations. In Proceedings of the

25th annual International ACM SIGIR conference on Research and development in
information retrieval. 253–260.

[33] Robin Schmucker and Tom M Mitchell. 2022. Transferable Student Performance
Modeling for Intelligent Tutoring Systems. arXiv preprint arXiv:2202.03980 (2022).
[34] Yi Shang, Hongchi Shi, and Su-Shing Chen. 2001. An intelligent distributed
environment for active learning. Journal on Educational Resources in Computing
(JERIC) 1, 2es (2001), 4–es.

[35] Yu Su, Qingwen Liu, Qi Liu, Zhenya Huang, Yu Yin, Enhong Chen, Chris Ding,
Si Wei, and Guoping Hu. 2018. Exercise-enhanced sequential modeling for stu-
dent performance prediction. In Proceedings of the AAAI Conference on Artificial
Intelligence, Vol. 32.

[36] Shan-Yun Teng, Jundong Li, Lo Pang-Yun Ting, Kun-Ta Chuang, and Huan Liu.
2018. Interactive unknowns recommendation in e-learning systems. In 2018 IEEE
International Conference on Data Mining (ICDM). IEEE, 497–506.

[37] Shiwei Tong, Jiayu Liu, Yuting Hong, Zhenya Huang, Le Wu, Qi Liu, Wei Huang,
Enhong Chen, and Dan Zhang. 2022. Incremental Cognitive Diagnosis for Intelli-
gent Education. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining. 1760–1770.

[38] Emiko Tsutsumi, Ryo Kinoshita, and Maomi Ueno. 2021. Deep-IRT with Indepen-
dent Student and Item Networks. International Educational Data Mining Society
(2021).

[39] Kurt VanLehn. 2011. The relative effectiveness of human tutoring, intelligent
tutoring systems, and other tutoring systems. Educational psychologist 46, 4
(2011), 197–221.

[40] Manasi Vartak, Arvind Thiagarajan, Conrado Miranda, Jeshua Bratman, and Hugo
Larochelle. 2017. A meta-learning perspective on cold-start recommendations
for items. Advances in neural information processing systems 30 (2017).

[41] Fei Wang, Qi Liu, Enhong Chen, Zhenya Huang, Yuying Chen, Yu Yin, Zai Huang,
and Shijin Wang. 2020. Neural cognitive diagnosis for intelligent education
systems. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 34.
6153–6161.

[42] Hao Wang, Enhong Chen, Qi Liu, Tong Xu, Dongfang Du, Wen Su, and Xiaopeng
Zhang. 2018. A united approach to learning sparse attributed network embedding.
In 2018 IEEE International Conference on Data Mining (ICDM). IEEE, 557–566.
[43] Hao Wang, Defu Lian, Hanghang Tong, Qi Liu, Zhenya Huang, and Enhong
Chen. 2021. Hypersorec: Exploiting hyperbolic user and item representations
with multiple aspects for social-aware recommendation. ACM Transactions on
Information Systems (TOIS) 40, 2 (2021), 1–28.

[44] Hao Wang, Tong Xu, Qi Liu, Defu Lian, Enhong Chen, Dongfang Du, Han Wu,
and Wen Su. 2019. MCNE: An end-to-end framework for learning multiple
conditional network representations of social network. In Proceedings of the 25th
ACM SIGKDD International Conference on Knowledge Discovery & Data Mining.
1064–1072.

[45] Minjie Wang, Da Zheng, Zihao Ye, Quan Gan, Mufei Li, Xiang Song, Jinjing
Zhou, Chao Ma, Lingfan Yu, Yu Gai, et al. 2019. Deep graph library: A graph-
centric, highly-performant package for graph neural networks. arXiv preprint
arXiv:1909.01315 (2019).

[46] Zhengyang Wu, Ming Li, Yong Tang, and Qingyu Liang. 2020. Exercise recom-
mendation based on knowledge concept prediction. Knowledge-Based Systems
210 (2020), 106481.

[47] Jie Xu, Cheng Deng, Xinbo Gao, Dinggang Shen, and Heng Huang. 2017. Pre-
dicting Alzheimer’s disease cognitive assessment via robust low-rank structured
sparse model. In IJCAI: proceedings of the conference, Vol. 2017. NIH Public Access,
3880.

[48] Linan Yue, Qi Liu, Yichao Du, Yanqing An, Li Wang, and Enhong Chen. 2022.
DARE: Disentanglement-Augmented Rationale Extraction. Advances in Neural
Information Processing Systems 35 (2022), 26603–26617.

[49] Si Zhang, Hanghang Tong, Jiejun Xu, and Ross Maciejewski. 2019. Graph convo-
lutional networks: a comprehensive review. Computational Social Networks 6, 1
(2019), 1–23.

[50] Hao Zhao, Ming Lu, Anbang Yao, Yurong Chen, and Li Zhang. 2020. Learning to
draw sight lines. International Journal of Computer Vision 128 (2020), 1076–1100.
[51] Hao Zhao, Ming Lu, Anbang Yao, Yiwen Guo, Yurong Chen, and Li Zhang.
2017. Physics inspired optimization on semantic transfer features: An alternative
method for room layout estimation. In Proceedings of the IEEE conference on
computer vision and pattern recognition. 10–18.

[52] Hao Zhao, Ming Lu, Anbang Yao, Yiwen Guo, Yurong Chen, and Li Zhang. 2020.
Pointly-supervised scene parsing with uncertainty mixture. Computer Vision and
Image Understanding 200 (2020), 103040.

[53] Wayne Xin Zhao, Wenhui Zhang, Yulan He, Xing Xie, and Ji-Rong Wen. 2018.
Automatically learning topics and difficulty levels of problems in online judge
systems. ACM Transactions on Information Systems (TOIS) 36, 3 (2018), 1–33.
[54] Jianhuan Zhuo, Jianxun Lian, Lanling Xu, Ming Gong, Linjun Shou, Daxin Jiang,
Xing Xie, and Yinliang Yue. 2022. Tiger: Transferable Interest Graph Embedding
for Domain-Level Zero-Shot Recommendation. In Proceedings of the 31st ACM
International Conference on Information & Knowledge Management. 2806–2816.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| Leveraging |          | Transferable   | Knowledge |           | Concept |           | Graph |     | Embedding |
| ---------- | -------- | -------------- | --------- | --------- | ------- | --------- | ----- | --- | --------- |
|            |          | for Cold-Start |           | Cognitive |         | Diagnosis |       |     |           |
|            | WeiboGao |                |           | HaoWang   |         |           |       |     | QiLiu∗    |
AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof
BigDataAnalysisandApplication, BigDataAnalysisandApplication, BigDataAnalysisandApplication,
SchoolofComputerScienceand UniversityofScienceandTechnology UniversityofScienceandTechnology
Technology,UniversityofScienceand ofChina&StateKeyLaboratoryof ofChina&StateKeyLaboratoryof
TechnologyofChina&StateKey CognitiveIntelligence CognitiveIntelligence
| LaboratoryofCognitiveIntelligence |             |     |                      | Hefei,China |     |     |     | Hefei,China         |     |
| --------------------------------- | ----------- | --- | -------------------- | ----------- | --- | --- | --- | ------------------- | --- |
|                                   | Hefei,China |     | wanghao3@ustc.edu.cn |             |     |     |     | qiliuql@ustc.edu.cn |     |
weibogao@mail.ustc.edu.cn
|     | FeiWang |     |     | XinLin |     |     |     | LinanYue |     |
| --- | ------- | --- | --- | ------ | --- | --- | --- | -------- | --- |
AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof
BigDataAnalysisandApplication, BigDataAnalysisandApplication, BigDataAnalysisandApplication,
SchoolofComputerScienceand SchoolofComputerScienceand SchoolofDataScience,Universityof
Technology,UniversityofScienceand Technology,UniversityofScienceand ScienceandTechnologyofChina&
TechnologyofChina&StateKey TechnologyofChina&StateKey StateKeyLaboratoryofCognitive
LaboratoryofCognitiveIntelligence LaboratoryofCognitiveIntelligence Intelligence
|     | Hefei,China |     |     | Hefei,China |     |     |     | Hefei,China |     |
| --- | ----------- | --- | --- | ----------- | --- | --- | --- | ----------- | --- |
wf314159@mail.ustc.edu.cn linx@mail.ustc.edu.cn lnyue@mail.ustc.edu.cn
|     | ZhengZhang |     |     | RuiLv |     |     |     | ShijinWang |     |
| --- | ---------- | --- | --- | ----- | --- | --- | --- | ---------- | --- |
AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof StateKeyLaboratoryofCognitive
BigDataAnalysisandApplication, BigDataAnalysisandApplication, Intelligence&iFLYTEKAIResearch
SchoolofComputerScienceand SchoolofComputerScienceand (CentralChina),iFLYTEKCo.,Ltd
Technology,UniversityofScienceand Technology,UniversityofScienceand Hefei,China
TechnologyofChina&StateKey TechnologyofChina&StateKey sjwang3@iflytek.com
| LaboratoryofCognitiveIntelligence |             |     | LaboratoryofCognitiveIntelligence |             |              |                   |     |               |                      |
| --------------------------------- | ----------- | --- | --------------------------------- | ----------- | ------------ | ----------------- | --- | ------------- | -------------------- |
|                                   | Hefei,China |     |                                   | Hefei,China |              |                   |     |               |                      |
| zhangzheng@mail.ustc.edu.cn       |             |     | lvrui2018@mail.ustc.edu.cn        |             |              |                   |     |               |                      |
|                                   |             |     |                                   |             | interactions | or unavailability |     | of exercising | records for training |
ABSTRACT
Cognitivediagnosis(CD)aimstorevealtheproficiencyofstudents purposes.Totacklethecold-startissue,weproposeatwo-stage
onspecificknowledgeconceptsandtraitsoftestexercises(e.g., solutionnamedTechCD(TransferableknowledgEConceptgrapH
embeddingframeworkforCognitiveDiagnosis).Thefundamental
difficulty).Itplaysacriticalroleinintelligenteducationsystems
notioninvolvesutilizingapedagogicalknowledgeconceptgraph
bysupportingpersonalizedlearningguidance.However,recent
(KCG)asamediatortoconnectdisparatedomains,allowingthe
developmentsinCDmostlyconcentrateonimprovingtheaccuracy
ofdiagnosticresultsandoftenoverlooktheimportantandpracti- transmissionofstudentcognitivesignalsfromestablisheddomains
caltask:domain-levelzero-shotcognitivediagnosis(DZCD).The tothezero-shotcold-startdomain.Specifically,anaiveyeteffec-
primarychallengeofDZCDisthedeficiencyofstudentbehavior tivegraphconvolutionalnetwork(GCN)withthebottom-layer
discardingoperationisinitiallyemployedovertheKCGtolearn
datainthetargetdomainduetotheabsenceofstudent-exercise
transferablestudentcognitivestatesanddomain-specificexercise
∗Correspondingauthor. traits. Moreover, we give three implementations of the general
TechCDframeworkfollowingthetypicalcognitivediagnosissolu-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed tions.Finally,extensiveexperimentsonreal-worlddatasetsnotonly
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation provethatTechcaneffectivelyperformzero-shotdiagnosis,butalso
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe givesomepopularapplicationssuchasexerciserecommendation.
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org.
SIGIR’23,July23–27,2023,Taipei,Taiwan
©2023Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM. CCSCONCEPTS
ACMISBN978-1-4503-9408-6/23/07...$15.00
https://doi.org/10.1145/3539618.3591774 •Appliedcomputing→E-learning.
983

SIGIR’23,July23–27,2023,Taipei,Taiwan WeiboGaoetal.
KEYWORDS Source domain Knowledge concept graph Target domain
Math Programming
cognitive diagnosis; student performance prediction; cold-start; Number Cube
knowledgeconceptgraph
Cone Array ?
ACMReferenceFormat:
WeiboGao,HaoWang,QiLiu,FeiWang,XinLin,LinanYue,ZhengZhang,
similarity ?
RuiLv,andShijinWang.2023.LeveragingTransferableKnowledgeConcept
GraphEmbeddingforCold-StartCognitiveDiagnosis.InProceedingsofthe Arithmetic List
46thInternationalACMSIGIRConferenceonResearchandDevelopmentin
InformationRetrieval(SIGIR’23),July23–27,2023,Taipei,Taiwan.ACM, Student: Concept: Exercise: Answering correctly/incorrectly: /
NewYork,NY,USA,10pages.https://doi.org/10.1145/3539618.3591774 “ ” demonstrates a linking from the mature domain to the new domain.
Figure1:Theexampleofaknowledgeconceptgraph(KCG)
1 INTRODUCTION
connectingisolatedexercisesineachdomain.
Intelligenteducationsystemsfacilitatethepersonalizedlearning toutilizeexercises’textualcontentsastheintermediarybylearning
ofstudentswithcomputer-assistedtechnologybyprovidingopen universalandcross-domainexerciseembeddings[22,35].However,
accesstoabundantlearningmaterials(e.g.,exercises).Theirpreva- therearetwomaindrawbackstotheseapproaches.First,exercises’
lenceandconveniencehavereceivedgreatattentionfromboth textual features may not accurately reflect the true meaning of
educatorsandthegeneralpublic[27].Intheseplatforms,cogni- theexerciseduetolinguisticbias[24].Forexample,twoexercises
tivediagnosis(CD)playsacrucialroleinprovidingcustomized fromcourseMathandcourseProgramming mayhavethesame
applicationstailoredtoindividualneeds[37].Specifically,thegoal description"Calculatethecircle’sarea",buttheyaretestingdiffer-
ofCDistoprofilestudents’latentcognitiveproficiency onspe- entconcepts,i.e.,GeometryandProgrammingLanguage.Second,
cificknowledgeconcepts,aswellastorevealcharacteristicsof toproficientlyadjusttodiversedomains,theexercisetextencoder
thetestexercisessuchasdifficultyanddiscrimination[9,37].As necessitatesdomain-specificguidance,whichhasthepotentialto
thediagnosticresultscansupportfurthereducationalapplications, overfitandobstructthetransmissionofcognitivesignalsbetween
suchasexerciserecommendation[19,46]andlearningpathsugges- distinctdomains[48,54].Therefore,itisdesirabletofindamore
tions[18,39],anumberofexistingmethodshavetriedtoimprove suitableintermediarytoconnectdifferentdomains.
theaccuracyofdiagnosticresultsbyfullyexploitingthestudents’ Inthispaper,weemployapedagogicalknowledgeconceptgraph
explicitresponserecords(e.g.,answeringcorrectlyornot). (KCG)astheintermediarytofacilitatethesharingofstudentcogni-
However,manypreviousmodelsfacechallengeswiththe"diag- tivestatesacrossdifferentdomains.Theunderlyingrationaleisthat
nosticsystemcold-start"problem.Forinstance,inonlineplatforms, theKCGhasthepotentialtoconnectdifferentdomainswhichcanbe
itiscommontolaunchnewbusinesses,e.g.,coursera.orgplansto abridgetopropagatestudentcognitivestates.Toelaborate,aKCG
releaseaseriesofnewtestexercises.Forthenewdomain,there comprisesnumerouseducationaldependencies(asrelations)tolink
arenostudent-exerciseinteractionrecordsavailable.Hereby,the knowledgeconcepts(asentities),whichhasbeenwidelyusedin
diagnosticperformanceofpreviousapproachesisoftenimpaired AIforEducation[3,34,45].Figure1illustratesanexampleofKCG
astheyonlyaddresstheCDtaskinmaturesourcedomainswhere withsomeeducationaldependencyrelations,e.g.,thesimilarityre-
student-exerciseinteractiondataareavailable.Inthispaper,we lationlinksconceptConeandconceptCubesincetheybelongtothe
callthediagnosticsystemcold-starttaskasdomain-levelzero-shot sametopicGeometry,whileNumberistheprerequisiteconceptof
cognitivediagnosis(DZCD).Differentfrompreviousstudiesonstu- Arithmeticastheformeristhelearningbasisofthelatterlogically.
dentsorexercisescold-startforCDwithinawell-establishedsource Obviously,theKCGhasthecapabilitytobridgedifferentdomains
domainwhereinteractionrecordsareavailable[22,33],inDZCD, if it covers the knowledge concepts and associated exercises in
studentspartiallyoverlapacrossdomains,andthematuresource eachdomain.Forexample,fortwocourse-leveldomains,theMath
domainshaverichstudentresponserecordsbutthezero-shottarget (sourcedomain)andProgramming(targetdomain),eachoftheir
domainisbrandnewwithoutstudent-exerciseinteractions.The exercisesassociatesatleastoneknowledgeconcept.Thisallows
DZCDisanimportantandpracticaltask,typicalapplicationsin- thetwodomainstobeconnectedthroughtheKCGaslongastheir
clude:(1)itisnecessarytodiagnoseinadvancewhenanonline associatedconceptsoccurintheKCG,eventhoughtheirexercises
learningsystemintendstolaunchanewbusiness;(2)students’ havenodirectoverlap.Thus,introducingaKCGastheintermediary
behaviordatainthetargetdomainareunavailableduetocollection acrossdomainstopropagatestudentcognitivestatesispromising,
limitationslikeprivacyprotectionpolicy.Nevertheless,tothebest butalsosignificantlychallenging.Ideally,aproperKCGmodelfor
ofourknowledge,thereisaseverelackofresearchonDZCD. CDshouldhavefouressentialproperties:(1)diagnosis-oriented:
Toprovidereliablecognitivediagnosisforazero-shotdomain, themodelcanperformtheCDtaskintheDZCDsetting;(2)stu-
inspiredbythesuccessofcross-domainmodelinginvariousfields dentstatepropagation:theKCGmodelshouldextractuniversaland
(e.g.,recommendersystems[25,54]),onepossiblewayistodefine transferableinformationforstudentembeddingssothatstudent
commonstudentstatecharacteristicsbyanalyzingtheirpastbehav- cognitivesignalscanbesharedacrossdomains;(3)domainadap-
iorsfromafewaccessiblesourcedomains,andrepresentthetest tion:foranycold-startdomainwhichneedsdiagnosis,themodel
exercisesinthetargetdomainusingavailablefeatures.Theprimary isexpectedtobedomain-adaptive.(4)application:thediagnostic
obstacleistolocateanappropriatemediatorthatcantransmitstu- resultscaneffectivelysupportfurtherintelligentservices.
dentstatesbetweentheestablishedandtargetdomains,enabling Motivatedbytheaboveconsiderations,weproposeageneral
theexecutionofDZCD[54].Somerelatedstudieshaveattempted TransferableknowledgEConceptgrapHframeworktoperform
984

LeveragingTransferableKnowledgeConceptGraphEmbeddingforCold-StartCognitiveDiagnosis SIGIR’23,July23–27,2023,Taipei,Taiwan
thedomain-levelzero-shotCognitiveDiagnosis(abbreviatedas Basedonthesetraditionalmethods,someresearchersintroduce
TechCD). The TechCD framework consists of two stages: the deeplearningintocognitivediagnosis.Forinstance,NeuralCogni-
knowledgeconceptgraphembedding(KCGE)stageandthedo- tiveDiagnosis(NeuralCD)[41]andDeep-IRT[38]exploitneural
mainadaptivediagnosis(DAD)stage.IntheKCGEstage,anaive networkstolearntheinteractionfunctionandtraitembeddings
yeteffectivegraphconvolutionalnetwork(GCN)[49]isfirstem- automatically.Recently,toalleviateissuesofstudentorexercise
ployed over the KCG for representation learning by iteratively cold-start,anddatasparsityinreal-worldscenarios,somestudies
fusingneighboringaggregationsintheKCG.Totakefulladvantage havealsoconsideredincorporatingexercisetexts[22],theconcep-
oftheconnectionsbetweenexercisesandtheKCG,wetreateach tualrelations[10,21]andmoreexceptions(e.g.,slipandguess)[23]
exerciseaspartoftheKCGforjointmodelingwithconceptentities, instudents’learningprocesstoenhancetheinteractiverelations
sothattheexercisescanabsorbstructuralinformationfromthe betweenstudentsandexercises.However,tothebestofourknowl-
graphastheirsemanticdescriptions.Themostdifficultaspectin edge,researchonhowtocold-startaCDsystemremainsunsolved.
thisstageistoguaranteethestudentstatepropagationproperty.
2.2 Cold-StartIntelligentSystems
Tothisend,inspiredby[54],weconstructtransferablestudent
Cold-startinganintelligentsystemwithouthistoricalinteractions
statesbydiscardingthebottomlayersofGCN(specificpatterns)
availablefornewusersoritemsisaprevalentandpracticalconcern
andonlyaggregatinghigh-levelones(universalpatterns)sothat
inmanydomains[15,32,33,51,52].Thispaperfocusesonthe
cognitivesignalscanbesuccessfullypropagatedtootherdomains.
taskofcold-startingacognitivediagnosissysteminazero-shot
Webuilddomain-specificexercisesandconceptsbyincorporating
domain,whichisofparamountimportancetounderstandingthe
comprehensivesemanticinformationfromtheKCGsothattheir
firstbatchofstudents’learningprocess,analyzingtheirknowledge
embeddingscomprisebothuniversalandspecificpatterns,which
proficiencyandfurtherhelpingimproveequityineducation[12].
ensuresdomainadaptation.IntheDADstage,theaboveembeddings
Totacklethisissue,manystrategieshavebeenutilizedsuchasmeta-
arefurtherfusedtoconstructthetraitsofstudents(i.e.,proficiency)
learning[40],cross-domainmodeling[25,54]andreinforcement
andexercises(e.g.,difficulty)bypredictingstudentperformance.
learning[7].Wepayattentiontotheideaofcross-domainmodeling,
Inthisway,thetraitsofstudentsandexercisesthatneedtobe
whichaimstocharacterizestudentstatefeaturesbasedontheir
diagnosedcanberefinedsatisfyingthediagnosis-oriented prop-
historicalbehaviorsfromsomeavailablesourcedomainsandrepre-
erty.ItisworthmentioningthatourgeneralTechCDframework
sentthetestexercisesinthetargetdomainwithavailablefeatures.
iswelldefinedtobeimplementedbycombiningwithexistingCD
The keychallenge isto find asuitable intermediary toconnect
solutions.Forinstance,wecanhaveTech-IRTbycombiningwith
thematureandtargetdomains.Somerelatedstudiesonstudent
IRT[9],Tech-MIRTwithMIRT[30]andTech-NeuralCDwithNeu-
performancepredictiontasks[22,35]utilizeexercises’textualcon-
ralCD[41],respectively.Finally,weconductextensiveexperiments
tentsastheintermediarybylearninguniversalandcross-domain
onfourreal-worlddatasets.Theexperimentalresultsnotonlyprove
exerciseembeddings.However,thesemethodsmaybelimiteddue
thatTechCDismoreeffectiveinzero-shotstudentperformance
tolinguisticbiasandcannotadapttodifferentdomainseffectively.
predictionsinceitcanwellcapturetheuniversalstudents’cogni-
tivesignalsforpropagationbutalsoshowthesuperiorapplication 2.3 PedagogicalKnowledgeConceptGraph
propertyoftheTechCD.Forinstance,TechCDcanfacilitatesome ApedagogicalKCGcontainsnumerouseducationaldependencies
personalizedlearningguidancesuchasexerciserecommendation (asrelations)toconnectknowledgeconcepts(asentities).Ingen-
incold-startscenarios. eral,thedependenciesareconstructedmanuallybydomainexperts
orautomaticallythroughdata-drivenalgorithmsbasedonpedagog-
2 RELATEDWORK
icalpriorknowledge[28],Amongthem,themostsignificantand
2.1 CognitiveDiagnosis commondependenciesincludesimilarity[26],collaboration[17],
Cognitivediagnosis(CD)isafundamentaltaskinmanyreal-world prerequisite [3], remedial [34] and hierarchy [21]. For example,
scenariossuchasgames[4],medicaldiagnosis[47],andespecially, apairofconceptsinvolvedinthesametopicorareaoroverlap-
education[10,23].ThekeyspiritofCDisthatitcanbeusedto pinginsomeknowledgecanbeassignedwithsimilaritydepen-
profilestudents’latentcognitiveproficiencyonspecificknowledge dencyrelations.Recently,someKCGshavebeenestablishedinboth
concepts,aswellasbeappliedtorevealcharacteristicsofthetest academiaandindustrysuchasOpenEduKG1andSongshuAIKCG2.
exercisessuchasdifficultyanddiscrimination[9,37]viaexploiting OnthebasisofKCGs,researchersattempttoincorporatetheminto
studenttestinglogs.Theserefinedtraitfeaturescouldbeapplied manyeducationalapplicationtasksandobtainsignificantimprove-
to many intelligent applications, such as exercise recommenda- ments[10,26,36].OurTechCDproperlyincorporatesatailored
tion[19,46]andlearningpathsuggestions[18,39].Intheearly pedagogicalKCGintoCDlinkingeachdomainsoastomitigate
years,cognitivediagnosiswasmostlydevelopedfromthepsycho- thedomain-levelzero-shotissue.
metricassumptionthatstudentcognitivestatesarestableinashort
periodoftime(e.g.,anexam)andthuscanbediagnosed[10].In 3 PRELIMINARIES
general,thesemethodsdevotemuchefforttothedesignofstudent-
3.1 CognitiveDiagnosisModel
exerciseinteractionfunctions,whichareexpectedtoautomatically
Wefirstbrieflyintroducecognitivediagnosismodels(CDMs).CDMs
inferstudents’knowledgestates.Forinstance,ItemResponseThe-
aredevelopedtodiscoverstudentproficiencylevelsonspecific
ory(IRT)[9],MultidimensionalIRT(MIRT)[30]andDeterministic
Inputs,Noisy-Andgate(DINA)[5]modeltheinteractionofstudents
1https://open.edukg.cn
andexerciseslinearly(e.g.,leveragingthelogistic-likefunction). 2https://www.songshuai.com/education
985

SIGIR’23,July23–27,2023,Taipei,Taiwan WeiboGaoetal.
knowledgeconceptsaswellasexercisetraits(e.g.,difficulty)through Definition2(Domain-levelzero-shotcognitivediagnosis).
fullyexploitingtheirresponsestoseveralexercises[37].Duetothe Givenstudentexercisingrecords𝐿 S inthesourcedomainandthe
realproficiencyofstudentscannotbequantifiedexplicitly,almost KCG,G,thegoalofTechCDfortheDZCDtaskistomakethediag-
allofthepreviousCDMsaretrainedthroughthestudentperfor- nosisonstudentandexercisetraitsinthetargetdomainT through
mancepredictiontask,i.e.,F CDM (𝒖,𝒗)→𝑦ˆ 𝑢𝑣 ,where𝒖and𝒗are fullyexploitingstudent-exerciseinteractiverecords𝐿 S inthesource
thelatenttraitsofstudentsandexercises,F
CDM
(·) isthediag- domainSwithstudentperformancepredictions.
nosticinteractionfunction,and𝑦ˆ isthepredictedperformance
𝑢𝑣
score.Thesetraitsofstudentsandexercisescanberefinedwith 4 THETECHCDFRAMEWORK
theoptimizationtargetofminimizingthedifferencebetweenthe 4.1 FrameworkOverview
predictedprobability𝑦ˆ andthetrueresponse𝑦 [10]. Conductingcognitivediagnosisindomain-levelzero-shotsettings
𝑢𝑣 𝑢𝑣
Generally, the differences between CDMs consist of the de- isnon-trivial.Itpresentsacriticalchallengeinlearningportable
sign of F CDM (·) and the representations of trait 𝒖 and 𝒗. For andtransferablestudentembeddingsfromtheirexercisingperfor-
example,IRT[9]usessingle-dimensionvariablestorepresentthe mancerecordsinthesourcedomain.Toovercomethisproblem,
traitfeaturesandlogistic-likefunctionastheinteractionfunction: weproposeaTechCDframeworkthatincorporatesatailoredpeda-
𝑖 𝑃 ’s (𝑦 k 𝑖 n 𝑗| o 𝜃 w 𝑖 , l 𝑎 e 𝑗 d , g 𝑏 e 𝑗) pr = ofi 1 c + ie 𝑒 n −1 c .7 y 𝑎 1 , 𝑗 a (𝜃 n 𝑖 d −𝑏 𝑎 𝑗) , a w nd he 𝑏 re r 𝜃 e 𝑖 pr c e h s a e r n a t c e te x r e i r z c e i s se st 𝑗 u ’s de d n is t - g so o u g r i c c e al a k n n d o t w ar l g e e d t g d e o c m on ai c n e s p . t O g u r r ap p h ro ( p K o C se G d ) T as ec a h b C r D id f g r e am be e t w w o e r e k n c t o h n e -
𝑗 𝑗
criminationanddifficulty.NeuralCD[41]exploitsneuralnetworks sistsoftwostages:knowledgeconceptgraphembedding(KCGE)
tofittheinteractionfunctionautomatically:𝑦ˆ
𝑖𝑗
=𝐹(𝒖𝑖 ,𝒗𝑗 ,Θ 𝐶𝐷), anddomainadaptivediagnosis(DAD).TheKCGEstage(detailed
where𝒖and𝒗arethelatenttraitsofstudentsandexercisesrespec- inSection4.2)learnsentityembeddingsfromthesemanticand
tively,and𝐹(·)ismulti-layerneuralnetworks.Tosummarize,we structuralinformationoftheKCG.TheDADstage(detailedinSec-
havethefollowinggeneralformofCDMs: tion4.3)thenconductsdiagnosisbypredictingstudentexercise
𝑦ˆ 𝑢𝑣 =F CDM (𝒖,𝒗,Θ∗), (1) per I f n or t m he an K c C e G .T E h s e ta en ge ti , r t e h s e tr c u r c it t i u c r a e l o o f b T s e ta c c h l C e D is i t s o d p ep ro ic p t a e g d a i t n e F s i t g u u d r e e n 2 t .
whereΘ∗ isthemodelparameter.Tobenoticedthat,toensure
cognitivestatesfromthesourcedomaintothetargetdomain.For
psychometricinterpretabilityofprediction,CDMsshouldstrictly
thisgoal,wecustomizeaKCGastheintermediarytolinkexer-
followtheMonotonicity assumption[37]:theprobabilityofcor-
cisesinvariousdomains.Weuseastraightforwardbuteffective
rectlyansweringtheexercisemonotonicallyincreaseswithstudent
graphconvolutionalnetwork(GCN)[49,54]ontheKCGtocon-
knowledgeproficiency,i.e., 𝜕F >0.
𝜕𝒖 structtransferablestudentcognitiveembeddingsthattranscendthe
exercise-relatedperformanceconfinedtothesourcedomain.Be-
3.2 KnowledgeConceptGraph
sideslearningtransferablestudentembedding,thisstagegenerates
ApedagogicalKCGcontainsknowledgeconceptentitiesandcon-
specificembeddingsofexerciseandconceptentitiesbyintegrating
ceptualdependencyrelations,whereas,inthedomain-levelcold-
thestructureandsemanticinformationfromtheKCG.
startingsettings,itadditionallyincludesexerciseentitiesandexercise-
Withtheaboveembeddings,theDADstagefurtherconstructs
conceptassociationrelations.
studentproficiencytraitsandexercisedifficultyanddiscrimina-
Definition1(Knowledgeconceptgraph). Formally,theKnowl- tiontraitsfordomain-adaptivecognitivediagnosiswithexisting
edgeconceptgraph(KCG)canberepresentedasG = {E,R,P}.E diagnosticmodels.Theentiremodelistrainedthroughpredicting
isthesetofentitiesincludingknowledgeconceptsets C andtheir studentperformanceonexercises,i.e.,𝑦ˆ 𝑢𝑣 = F CDM (𝐿 S ,G,Θ∗),
associatedexercises.Risthesetofrelationsincludingeducationalde- whereparameterΘ∗isoptimizedfromthesourcedomainSas:
pendencyrelationsbetweenconcepts(e.g.,prerequisiteandsimilarity)
Θ∗=argminL(𝑦(𝐿 ),G). (2)
andassociationrelationsbetweenexercisesandconcepts.Pisoffered S
Θ
intheformofentity-relation-entitytripletsetP = {(ℎ,𝑟,𝑡)|ℎ,𝑡 ∈ ItisworthmentioningthattheKCGEstageandtheDADstage
E,𝑟 ∈R},e.g.,(conceptcube,similarity,conceptcone)and(exercise aretrainedinanend-to-endfashionwiththeaboveEq.(2).Thus,the
𝑒1,association,conceptfunction). refinedtraitsofstudentsandexercisescanbethediagnosticresults.
Aftertraining,TechCDcanconductzero-shotstudentperformance
3.3 ProblemDefinition
predictionsinthezero-shottargetdomainT.
Inthedomain-levelzero-shotcognitivediagnosis(DZCD)scenario,
we represent the mature/available source domain as S and the 4.2 KnowledgeConceptGraphEmbedding
cold-start/zero-shottargetdomainasT.Thestudentsetsandex- Thisstageaimstoidentifyuniversalstudentstatespresentinexer-
ercise sets in source domain S are denoted as U , V , and in cisesofthesourcedomainthatcanbetransferredtothezero-shot
S S
targetdomainT aredenotedasU ,V ,whereU ⊂ U and domainviathecustomizedKCG.Forthisgoal,weapplyamulti-
T T T S
V
S
∩V
T
=∅.Allstudent-exerciseperformancerecordsfortrain- layerGCNnetwork3overtheKCGtolearnentityembeddings.
ing(withlabel)arecollectedfromthesourcedomain,depictedas Generally,theKCGcontainsconceptandexerciseentities,aswell
𝐿 S = {(𝑢 𝑖 ,𝑣 𝑗 ,𝑦 𝑖𝑗)|𝑦 𝑖𝑗 ∈ {0,1},𝑢 𝑖 ∈ U S ,𝑣 𝑗 ∈ V S },where𝑦 𝑖𝑗 =1 asmultipleconceptualdependencyrelationsandexercise-concept
representsstudent𝑢 𝑖 answersexercise𝑣 𝑗 correctly,and𝑦 𝑖𝑗 =0oth- associationrelations,asshowninFigure2(a).Theeducational
erwise.Thestudent-exerciseinteractionsfromthetargetdomain
3Actually,variousKCGembeddingtechniqueshavebeenproposedtoextractmeaning-
(withoutlabel),i.e.,𝐿 T ={(𝑢 𝑖 ,𝑣 𝑗)|𝑢 𝑖 ∈U T ,𝑣 𝑗 ∈V T },areusedto fulembeddings[42,49].Sinceourfocusisnottodevisemoresophisticatedtechniques
evaluatepredictionperformanceinDZCDscenarios.Hereby,our forgraphnetworkembedding,wesimplyuseapopularGCNtolearnentityrepresen-
TechCDmodelfortheDZCDtaskisdefinedas: tations,toverifytheeffectivenessofincorporatingtheKCGintotheDZCD.
986

LeveragingTransferableKnowledgeConceptGraphEmbeddingforCold-StartCognitiveDiagnosis SIGIR’23,July23–27,2023,Taipei,Taiwan
1
|     |     |     |     |     |     |     |     |     | ℎ𝑢  |     |     | 𝒅𝒗  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑓𝛽
ℎ𝑐
ℎ𝑣
|     |     |     |     |     |     |     |     |     |     | ℎ𝑢  | ℎ𝑐  | ℎ𝑣  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure2:TheoverviewarchitectureofTechCD:(a)aknowledgeconceptgraph(KCG)linksthesourceandthetargetdomains;
(b)theknowledgeconceptgraphembeddingforentityrepresentationlearning;(c)thedomainadaptivediagnosisforDZCD.
dependency relations reflect student learning rules and knowl- completesemanticrepresentation𝒛𝑖 ∗,asEq.(4).
edgetransferringlogically,whichcanimplicitlypropagatestudent 𝐿 𝐿
|     |     |     |     |     |     |     |     | 1   | ∑︁  |     | 1 ∑︁ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
states[8],whiletheexercise-conceptassociationscanenhanceex- # (𝑙),𝒛𝑖 ∗= (𝑙). (4)
|     |     |     |     |     |     |     | 𝒛𝑖 = | 𝐿− 𝜆+1 | 𝒛𝑖  |     | 𝐿+ 1 | 𝒛𝑖  |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --- | --- | ---- | --- |
erciserepresentationsbyabsorbingstructuralandsemanticinfor-
|     |     |     |     |     |     |     |     |     | 𝑙=𝜆 |     | 𝑙=0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hereby,weconstructthetransferablecognitivestateofstudent
mationfromtheKCG.Thereby,foreachentityembedding,itneeds
todiscriminatedifferentrelationsbyseparatelyfusingneighboring 𝑢byabsorbinggeneralknowledgefromtheKCGas:
i n f o r m a t i o n o f e a c h t y p e o f r e l a t i o n . W e d i r e c t l y u s e t h e le a r n a b l e 1
|     |     |     |     |     |     |     |     |     |     | ∑︁  | # , | ( 5 ) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
e m b e d d i n g ∈ R 𝑑 o f e a c h e n t it y 𝑒 a s t h e i n p u t o f G C N , i . e . , 𝒉 𝑢 = 𝒛 𝑣
|       | 𝒆 𝑖 |     |     | 𝑖   |     |     |     |     | | H S | |      |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- |
| ( 0 ) |     |     |     |     |     |     |     |     | 𝑢     | 𝑣∈ H S |     |     |
𝒛 = 𝑐 𝑖 , w h e r e 𝑑 i s t h e e m b e d d i n g d i m e n s i o n a l si z e . W e c o n d u c t 𝑢
𝑖 whereH𝑢 S istheexer c ise s e t t ha t st u de n t 𝑢 hasinteractedwi t h
| c o n v o lu | t i o n o p e r | a t i o n [ 4 | 4 ] o f G C N | o v e r t h e K C G 𝐿 t i m | e s w i t h e a c h |                           |     |     |     |                               |     |     |
| ------------ | --------------- | ------------- | ------------- | --------------------------- | ------------------- | ------------------------- | --- | --- | --- | ----------------------------- | --- | --- |
|              |                 |               |               |                             |                     | inthesourcedomainS.Weuse𝒛 |     |     |     | # torepresentstudentstates,as |     |     |
iterationconsideringeachtypeofrelationseparately,toaggregate 𝑣
itcapturesentity-specificinformationinthebottom-layeroutput,
| 𝐿 hop | neighborhood | information |     | and generate𝐿 entity | embed- |     |     |     |     |     |     |     |
| ----- | ------------ | ----------- | --- | -------------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
∗
(1),𝒛𝑖 (2),...,𝒛𝑖 (𝐿) (𝑙) wh il e 𝒛 𝑣 c o n t a in s m o re g e n e r a l hi g h - o r d e r i n f o r m a t io n .
| dings,[𝒛𝑖                |     |                                         | ],where𝒛𝑖                         | ∈R𝑑 denotesthe𝑙-thlayer |     |                                                           |                |              |               |             |                    |                   |
| ------------------------ | --- | --------------------------------------- | --------------------------------- | ----------------------- | --- | --------------------------------------------------------- | -------------- | ------------ | ------------- | ----------- | ------------------ | ----------------- |
|                          |     |                                         |                                   |                         |     | B e s                                                     | id e s g e n e | ra t in g st | u d e n t e m | b e d d i n | g s , t h i s s ta | g e a l sooutputs |
| outputofentity𝑒          |     | .TheGCNiterativelyaggregatesneighboring |                                   |                         |     |                                                           |                |              |               |             |                    |                   |
|                          |     | 𝑖                                       |                                   |                         |     | exerciseandknowledgeconceptrepresentations.Fortheexercise |                |              |               |             |                    |                   |
| informationofeachentity𝑒 |     |                                         | foreachtypeofrelationseparatelyto |                         |     |                                                           |                |              |               |             |                    |                   |
|                          |     |                                         | 𝑖                                 |                         |     | entity𝑣,wedirectlyassignitscorrespondingembedding𝒛∗       |                |              |               |             |                    | from              |
𝑣
enhanceitsrepresentationt hroughthemessage-passing-receiving theentity𝑒 intheKCGtoitsimilarto[54],i.e.,𝒉𝑣 𝒛∗ .Note
|     |     |     |     |     |     |     | 𝑣   |     |     |     |     | = 𝑣 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mechanism[13,43]asfollows:
thatexerciseembeddingsincorporatebothgeneralanddomain-
(𝑙) ∑︁ 1 ∑︁ 𝑙−1), s p e c ifi c i n fo r m at i on b y a b so r b in g fu l l se m a nt i c re p r es e n t a t i o n s o f
|     | 𝒛𝑖  | =   |     | W𝑟𝒛 ( | (3) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑟| 𝑗 e x er c is e e n ti t ies i n th e K C G , w h ic h c a n fi ll in t h e d o m a i n - a d a p t io n
|     |     |     | |P 𝑖 | 𝑟   |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑟∈R𝑖 (𝑒𝑗,𝑟,𝑒𝑖)∈P 𝑖 requirementsintuitively.Similarly,werepresenteachconcept𝑐’s
whereR𝑖 isthesubsetofRconsistingoftherelationtypesofentity embedding𝒉𝑐 withitsfullsemanticrepresentation𝒛𝑐 ∗,i.e.,𝒉𝑐 ∗.
=𝒛𝑐
| 𝑒 .P 𝑟 isthesubsetofPcontainsallthetriplets(𝑒 |     |     |     | ,𝑟,𝑒 | 𝑖)ofentity |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| 𝑖 𝑖                                           |     |     |     | 𝑗    |            |     |     |     |     |     |     |     |
4.3 DomainAdaptiveDiagnosis
𝑒 𝑖 withrelation𝑟.Foreachrelation𝑟,weusealearnablematrix
W𝑟 ∈ R𝑑×𝑑 to transform each concept/exercise entity feature Inthisstage,weconductdomain-adaptivecognitivediagnosiswith
vectortothesamefreeembeddingspace. existingcognitivediagnosismodels.
Afterobtainingtheaboverefinedentityembeddings,thefocus
|     |     |     |     |     |     | 4.3.1 | DiagnosedTraitRepresentationModeling. |     |     |     |     | Ingeneral, |
| --- | --- | --- | --- | --- | --- | ----- | ------------------------------------- | --- | --- | --- | --- | ---------- |
isonrepresentingtransferablestudentembeddingstoaddressthe
|     |     |     |     |     |     | a cognitive | diagnosis |     | model (CDM) | takes | the traits | of students |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ----------- | ----- | ---------- | ----------- |
challengeofstudentstatepropagation.Weresorttothebottom- (i.e.,proficiency)andexercises(e.g.,difficultiesanddiscrimination)
discardingoperation[54]whichisnaturallycompatible.Itargues asthebasicinput[41].Thus,itiscrucialtorepresenttheabove
thatthebottomlayersofGCNpreservemoredomain-specificin- traitsthatneedtobediagnosedviathegeneratedembeddingsfrom
formation,whiletheupperlayersbetterrepresentuniversaland
theKCGEstage.Inspiredby[10,21],togeneratetheproficiency
transferableinformation.Thisisintuitivelyreasonablebecausein-
factoroneachconceptofeachstudent,weincorporatetheembed-
creasingthenumberofGCNlayerscanleadtoover-smoothing, dingsofknowledgeconceptentitiesintothetransferablestudent’s
resultinginthelossofdiscriminativeinformation[16],whichmakes embedding.Thus,thestudentproficiencytraitcanbemodeledas:
itpromisingtoeffectivelypropagatestudentcognitivesignalsto
|     |     |     |     |     |     | =(𝑝 | ;𝑝  | ;··· ;𝑝 | ), where𝑝 |     | =𝑓  | (0,1). (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --- | ---------- |
zero-shotdomains.Thus,wediscardthelower-levelentityembed- 𝒑𝑢 𝑢1 𝑢2 𝑢|C| 𝑢𝑐 𝑢(𝒉𝑢⊕𝒉𝑐) ∈
dingsbysettingsahyper-parameter𝜆toaggregatetransferable IntheaboveEq.(6),vector𝒑𝑢 isstudent𝑢’sproficiencyon
|C|
embeddings𝒛𝑖 #.Additionally,wefusealllayeroutputembeddings knowledgeconceptsintheKCG.Eachelementof𝒑𝑢 ,i.e.,𝑝 ,de-
𝑢𝑐
ofGCNaswellastheoriginalentityembedding,resultingina notesstudent𝑢’smasterylevelonconcept𝑐.Afullconnection
987

| SIGIR’23,July23–27,2023,Taipei,Taiwan |     |     |     |     |     |     |     |     |     | WeiboGaoetal. |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
layer[50]𝑓 𝑢(·)isusedtofuseknowledgeconceptsemanticsinto Table1:Somebasicstatisticsofthedatasets.
thestudentembeddingwithconcatenation⊕.Similarly,wealso
|     |     |     |     |     |     |     | Datasets |     | CM AM | Junyi ASSIST |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- | ------------ |
fuseknowledgeconceptinformationintoexerciseembeddingsto
|     |     |     |     |     |     |     | #Student |     | 21,068 21,059 | 10,000 5,730 |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | ------------ |
calculateeachexercise𝑣’sdifficultytrait𝒅𝑣 onallconceptswith #Exercise 6,257 3,263 706 4,973
thefullconnectionlayer𝑓 𝑣(·)asEq.(7). #Knowledgeconcept 1,251 990 706 122
|     |     |     |     |     |     |     | #Record |     | 351,146 171,380 | 353,835 225,314 |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------------- | --------------- |
𝒅𝑣 =(𝑑 𝑣1 ;𝑑 𝑣2 ;··· ;𝑑 𝑣|C| ), where𝑑 𝑣𝑐 =𝑓 𝑣(𝒉𝑣 ⊕𝒉𝑐) ∈ (0,1). (7) #Recordperstudent 16.7 8.1 35.4 39.3
| Besides,thediscrimination𝛽 |     |     | ofeachexercise𝑣isdirectlyobtained |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
𝑣
|                                                        |                   |     |                                  |            |                        |     | istheknowledgeconceptset.TheF |                                              |                                 | (·)isamulti-layerneu- |
| ------------------------------------------------------ | ----------------- | --- | -------------------------------- | ---------- | ---------------------- | --- | ----------------------------- | -------------------------------------------- | ------------------------------- | --------------------- |
| bytransformingtheexerciseembeddingtoalatentfactorwitha |                   |     |                                  |            |                        |     |                               |                                              | CDM                             |                       |
|                                                        |                   |     |                                  |            |                        |     | ralnetworks𝜙                  | withnon-negativeweightstokeepexplainability: |                                 |                       |
| neuralnetwork𝑓                                         | 𝛽(·),i.e.,scalar𝛽 |     |                                  | 𝑣 =𝑓 𝛽(𝒉𝑣) | ∈ (0,1),similarto[21]. |     |                               |                                              |                                 |                       |
|                                                        |                   |     |                                  |            |                        |     | 𝑦ˆ =𝜙(𝑸𝒗                      | 𝑇 −𝒅𝑣)·𝛽                                     | 𝑣),where◦iselement-wiseproduct. |                       |
|                                                        |                   |     |                                  |            |                        |     | 𝑢𝑣                            | ◦(𝒑 𝑢                                        |                                 |                       |
| 4.3.2 DiagnosticAdaptor.                               |                   |     | Differentdiagnosticmodelscharac- |            |                        |     |                               |                                              |                                 |                       |
terizestudentandexercisefeaturesindifferentforms.Ouraimis 5 EXPERIMENTS
toestablishaconnectionbetweenstudents’cognitiveproficiency, Weconductcomprehensiveexperimentstoaddressthefollowing
| exercise traits, | and | the input | forms | of  | existing diagnostic | mod- |     |     |     |     |
| ---------------- | --- | --------- | ----- | --- | ------------------- | ---- | --- | --- | --- | --- |
researchquestions:
els,throughintroducingthediagnosticadaptor.Ingeneral,forthe
|     |     |     |     |     |     |     | • RQ1CantheTechCDframeworkeffectivelyhandlethedomain- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
givenstudent𝑢andexercise𝑣,theCDMadaptorpredictsstudent levelzero-shotcognitivediagnosistask?
| performancescore𝑦ˆ |     | 𝑢𝑣 asEq.(8): |     |     |     |     |                                                    |     |     |     |
| ------------------ | --- | ------------ | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
|                    |     |              |     |     |     |     | • RQ2HowabouttheeffectivenessofmodelingtheKCGbythe |     |     |     |
TechCDframework?
|     | 𝑦ˆ 𝑢𝑣 | =F  | (𝜙 𝑢(𝒑𝑢),𝜙 |     | 𝑣(𝒅𝑣),𝛽 𝑣), | (8) |                                                        |     |     |     |
| --- | ----- | --- | ---------- | --- | ----------- | --- | ------------------------------------------------------ | --- | --- | --- |
|     |       | CDM |            |     |             |     | • RQ3CantheTechCDutilizetheout-of-domaindatasetsforthe |     |     |     |
performanceimprovement?
| whereF CDM | (·)representstheexistingdiagnosticmodelandcan |     |     |     |     |     |     |     |     |     |
| ---------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RQ4HowtoapplyTechCDtoprovidepersonalizedguidance?
| bespecifiedwithmanymodelslikeIRT[9],MIRT[30],etc.Tocover |     |     |     |     |     |     | •   |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
differentdiagnosticmodels,weemploytwotransformfunctions,
|            |                                                 |     |     |     |     |     | 5.1 Datasets |     |     |     |
| ---------- | ----------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 𝜙 𝑢(·)and𝜙 | 𝑣(·),tostandardizetheformofstudentproficiency𝒑𝑢 |     |     |     |     |     |              |     |     |     |
Weconductexperimentsonthefollowing
and exercise difficulty so as to satisfy the input form of the 5.1.1 BasicDescription.
|     |     | 𝒅𝑣  |     |     |     |     | fourreal-worldrepresentativedatasets: |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
adoptedmodel.Besides,toensurethemonotonicityassumption
|                                                 |         |                                    |     |     |     |      | • CoreMath(CM)andAdvancedMath(AM)aretwosubsetsof        |     |     |     |
| ----------------------------------------------- | ------- | ---------------------------------- | --- | --- | --- | ---- | ------------------------------------------------------- | --- | --- | --- |
| ofcognitivediagnosis,werestricteachparameterofF |         |                                    |     |     |     | tobe |                                                         |     |     |     |
|                                                 |         |                                    |     |     | CDM |      | theMATH-2021dataset,collectedsuppliedbyiFLYTEKCo.,Ltd., |     |     |     |
| positive,sothat                                 | 𝜕FCDM   | >0.Eq.(8)canbeusedtoinferstudents’ |     |     |     |      |                                                         |     |     |     |
|                                                 | 𝜕𝜙𝑢(𝒑𝑢) |                                    |     |     |     |      | whichiscollectedfromtheiFLYTEKLearningMachine4.They     |     |     |     |
performanceonexercisesinboththesourceandtargetdomains.
haveoverlappingstudentswhiletheirexerciseshavenooverlap.
Finally,weusethepopularcross-entropylossfunctiontoopti-
|     |     |     |     |     |     |     | • Junyi5[2]containsstudentonlinelearninglogsonmathematical |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- |
mizethewholemodelbyminimizingthedifferencebetweenthe
exerciseswhichiscrawledfromaChineseonlinelearningplat-
| predictedprobability𝑦ˆ |     |     | andthetrueresponse𝑦 |     | .   |     |                                                       |     |     |     |
| ---------------------- | --- | --- | ------------------- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
|                        |     | 𝑢𝑣  |                     |     | 𝑢𝑣  |     | form.NowadaysJunyiiswidelyusedintheevaluationofonline |     |     |     |
educationtasks[10,21].Werandomlyselect10,000students’
∑︁
| L=− |     | (𝑦 𝑢𝑣 | log𝑦ˆ 𝑢𝑣+(1−𝑦 |     | 𝑢𝑣)log(1−𝑦ˆ 𝑢𝑣)). | (9) |     |     |     |     |
| --- | --- | ----- | ------------- | --- | ----------------- | --- | --- | --- | --- | --- |
exercisingrecordsfromJunyiforexperiments.
(𝑢,𝑣,𝑦𝑢𝑣)∈𝐿
|     |     | S   |     |     |     |     | • ASSISTments-2012-2013(ASSIST)6isanopendatasetcollected |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
Byoptimizingwiththeaboveloss,theseinputtraitsofthestudent bytheASSISTmentsonlinetutoringsystems,whichhasbecome
andtheexerciseinEq.(8),i.e.,𝒑𝑢 ,𝒅𝑣 and𝛽 ,canbejointlyrefined popularbenchmarkdatasetsforcognitivediagnosis.Weran-
𝑣
servingasthediagnosticresultsofstudentsandexercises. domlyselectabout5,000exercisesandtheirrelatedrecords.
Takingthestudenttrait𝜙 Allthedatasetsprovidestudentexercisingrecordsandexercise-
| 4.3.3 InstantiatingtheTechCD. |     |     |     |     |     | 𝑢(𝒑𝑢) |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
conceptcorrelations,whereeachexerciseassociatesoneknowledge
| andexercisetraits𝜙 |     | 𝑣(𝒅𝑣)and𝛽 |     | 𝑣 asinputfactors,wespecifythe |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
diagnosticadaptorF (·)inEq.(8)ofTechCDwithIRT,MIRT concept.Besides,AMandCMprovidetheexercises’contents,and
CDM
andNeuralCDasfollows: Junyiprovidestheconceptualprerequisiteandsimilarityrelations
IRT[9]takestheunidimensionalstudentproficiency,exercise labeledbyexperts.Eachdatasetistreatedasadomain,i.e.,the
difficulty and discrimination as input. To specify with IRT, we sourceortargetdomain.Amongthem,thereisnooverlapbetween
thestudentsintheJunyiandASSISTdatasetsandthoseinthe
| project𝒑𝑢 | and𝒅𝑣 | toscalars𝑝 | 𝑢 and𝑑 | 𝑣   | respectivelybysetting𝜙 | 𝑢   |     |     |     |     |
| --------- | ----- | ---------- | ------ | --- | ---------------------- | --- | --- | --- | --- | --- |
MATHdataset.Foreachdataset,wereserveonlythefirstattemptof
| and𝜙 𝑣 asmeanpooling.TheF |     |     |     | (·)isalogistic-likefunction: |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
CDM
𝑦ˆ =sigmoid(𝛽 𝑣·(𝑝 𝑢−𝑑 𝑣)). eachexerciseforeachdatasettoensurethattheattributestateofstu-
𝑢𝑣
MIRT[30]modelstheinteractionbetweenmultidimensional dentsisstaticfollowingthe[10,41].Weevaluatetheperformance
studentproficiency𝒑𝑢 andexercisedifficulty𝒅𝑣 usingalogistic- ofDZCDonthetargetdomainusingtherefinedmodeltrained
inthesourcedomain.Wespliteachsourcedomain’sdatasetby
| likefunction.Wesettheoutputdimensionsof𝜙 |     |     |     |     | 𝑢 and𝜙 𝑣 | as𝐷 >1. |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | -------- | ------- | --- | --- | --- | --- |
randomlyselectingtwohistoricalinteractionsfromeachstudent’s
| TheF | (·)isshownas:𝑦ˆ |     | 𝑢𝑣 =sigmoid(𝒑 |     | 𝑇 𝑢𝒅𝑣+𝛽 𝑣). |     |     |     |     |     |
| ---- | --------------- | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- |
CDM
NeuralCD[41]directlytakesstudentproficiency𝒑𝑢 andexer- logsforvalidation,withtheremainingdataservingasthetraining
cisedifficultyasinput.Additionally,itrequiresmaskingtheirrel-
4
| evantknowledgeproficiencybyavector𝑸𝑣 |     |     |     |     | ={0,1}|C|×1where |     | h t t p s : / / x x j .x | u n fe i. cn /                                        |     |     |
| ------------------------------------ | --- | --- | --- | --- | ---------------- | --- | ------------------------ | ----------------------------------------------------- | --- | --- |
|                                      |     |     |     |     |                  |     | 5 h t t p s : / / p sl c | d a ta sh o p .web.cmu.edu/DatasetInfo?datasetId=1198 |     |     |
𝑞 𝑣,𝑐 =1ifexercise𝑣associatesconcept𝑐and𝑞 𝑣,𝑐 =0otherwise.C 6https://drive.google.com/file/d/1cU6Ft4R3hLqA7G1rIGArVfelSZvc6RxY/view
988

LeveragingTransferableKnowledgeConceptGraphEmbeddingforCold-StartCognitiveDiagnosis SIGIR’23,July23–27,2023,Taipei,Taiwan
Table2:SomedetailedstatisticsoftheKCG. • Random:Therandommethodpredictsthestudents’scoresran-
#Concept 2,594 domlyfrom𝑈𝑛𝑖𝑓𝑜𝑟𝑚(0,1).
Entity #Exercise 15,199 • Oracle:Theoraclebaselineistrainedwiththestudent-exercise
#Total 17,793 interactiverecordsofbothsourceandtargetdomains.Hence,it
shouldperformbetterthanothercomparedmethods.
Relation #Total 5
• NLP-based:Somerelatedresearches[22,35]utilizeexercises’tex-
#Conceptualdependency 7,926
tualcontentsasanintermediaryofthesourceandtargetdomain
Triple #Exercise-conceptassociation 15,469
forstudentperformancepredictions.Thus,weadoptBert[6]
#Total 23,395
astheencodertoencodeexercises’textualcontentstogener-
atetheirembeddings.ToimplementtheNLP-baseddiagnosis
set,similartothewidelyusedleave-one-out evaluation[14,31].
method,weuselearnableembeddingsasstudentproficiencyand
Besides,totraintheOraclemodels(Section5.2),wealsosplitthe
introducetwofunctionstotransformtextualcontentfeatures
targetdomain’sdatasetintotraining(70%),validation(10%),and
intoexercises’difficultiesanddiscrimination.
testsets(20%),similarto[54].Thebasicstatisticsofthedatasets
• GCN-based:Weaddabaselinethatutilizesonlythelast-layer
arepresentedinTable1.
output asentities’ embeddingsand does notdifferentiatebe-
5.1.2 KnowledgeConceptGraphConstruction. Tobridgeexercises
tweenthedifferentrelationsintheKCGforcomparison.
acrossdifferentdomains,itneedstotailoraunifiedknowledge
conceptgraph(KCG)linkingeachdomain.Forthispurpose,we 5.3 EvaluationMetricsandOtherSettings
adoptahierarchicalmathematicalKCG(abbreviatedasMathKCG) 5.3.1 Metrics. Toevaluatemodelperformance,weadoptdiffer-
toconnectalldomains(i.e.,allthedatasets).Specifically,MathKCG entmetricsfromtheperspectivesofclassificationandregression
ispublishedbytheonlineeducationplatform,i.e.,Luna7.Itcov- followingthe[10].Fromtheclassificationperspective,astudentan-
ers39.5%knowledgeconceptsinourdatasetsandprovidestwo sweringincorrectlyorcorrectlycanberepresentedasanegative(0)
significanttypesofconceptualrelations,i.e.,hierarchy[21]and orpositive(1)instancerespectively.Thus,weuseAccuracy(ACC)
similarity[26]relations.Wefirstaligneachexercise-relatedcon- and Area Under the ROC Curve (AUC) for measuring. From the
ceptindatasetsandconceptsinMathKCGbasedonconceptual regressionperspective,weselectRootMeanSquareError(RMSE)
names.Then,fortheisolatedconceptsineachdatasetthatcannot toquantifythedistancebetweenthepredictedscore(i.e.,theprob-
belinkedtoMathKCG,webuildconceptualsimilarandprerequisite abilitythatastudentanswerscorrectly)andtheactualone.
relations[3]betweenthemviaexploitingstudentperformancelogs 5.3.2 ImplementationDetails. ForthosemodelsthatemployNeural-
usingthestatisticalmethod[10].Hereby,basedonthegenerated CDandMIRTasdiagnosticfunctions,wesetthedimensionsof
relations, the MathKCG, and those relations provided by Junyi, studentandexercisevectorsasthenumberofdiagnosedknowledge
eachconceptcanbelinkedtoaKCG.Additionally,theexercises concepts |C|,similarto[41].Thedimensionsofneuralnetwork
arelinkedtotheirassociatedknowledgeconceptintheKCG.The layersare1024and512forallmodelswithNeuralCDdiagnostic
finalKCGincludesconceptandexerciseentities,andfourtypes function.RegardingtheGCNlayers,underthe"AMassource"set-
ofconceptualrelations(i.e.,hierarchy-in-MathKCG,similarity-in- ting,weuse5layersfor𝐿andadiscardingparameter𝜆of3.Under
MathKCG,theconstructedsimilarityandprerequisiterelationsvia the"CMassource"setting,weuse5layersfor𝐿andadiscarding
ourdatasets)aswellastheexercise-conceptassociationrelations. parameter𝜆of2.Fortraining,allnetworkparametersareinitialized
We conduct all experiments on the same KCG. The detailed withXavierinitialization[11].Furthermore,wesetthemini-batch
statisticsoftheKCGarepresentedinTable2. sizeas256andthelearningrateas0.0005foreachmodel.Each
modelisimplementedbyPyTorch[29]andoptimizedbyAdam
5.2 Baselines
optimizer[20].AllexperimentsarerunonaLinuxserverwithtwo
Toverifytheeffectivenessofourmodel,wepresentthreeimplemen-
3.00GHzIntelXeonGold5317CPUsandoneTeslaA100GPU.The
tationsbasedonTechCDframeworkthatcombinetypicaldiagnosis
codeisavailableathttps://github.com/bigdata-ustc/TechCD.
methods.Inparticular,weimplementTech-IRT,Tech-MIRTand
Tech-NeuralCDfollowingIRT,MIRTandNeuralCD,respectively. 5.4 StudentPerformancePrediction(RQ1)
• IRT[9]:IRTmodelsunidimensionalstudentsandexercises’fea- ToanswerRQ1,wecomparetheperformanceofourmodelwithsev-
tureswithalogistic-likefunction. eralbaselinesonthedomain-levelzero-shotstudentperformance
• MIRT [30]: As the multidimensional extension of IRT, MIRT predictiontask.WeswitchCMandAMdatasetsasthetargetdo-
modelsmultipleknowledgeproficiencyofstudentsandexercises. mainsincetheirstudentsoverlap.ItisworthmentioningthatJunyi
• NeuralCD[41]:NeuralCDisoneofthemostpopulardeeplearning- andASSISTareusedinSection5.6todemonstratehowTechCD
basedCDmethods,whichmodelshigh-orderandcomplexstudent- utilizesout-domaindatasetsfromotherplatformsfortheDZCD
exerciseinteractionfunctionswithamultilayerperceptron(MLP). task,astheyarecollectedfromdifferentplatforms.Theoverall
predictionperformanceisreportedinTable3.Thecombination
Weselectaseriesofbaselinesforcomparison.Amongthem,the
ofS-CM(AM)andT-AM(CM)denotesCM(AM)asthesource
randomandoraclemethodsindicatethelowerandupperboundsof
domainfortrainingandAM(CM)asthetargetdomainfortesting.
performance,followingtheprevioussetups[54].Foreachbaseline
Wehavethefollowingobservations:(1)Fordifferentdiagnostic
(excludingRandom),wealsoselectIRT,MIRTandNeuralCDas
implementations(i.e.,IRT,MIRTandNeuralCDasDiagnosticfunc-
theirdiagnosticfunctions.Thedetailsarelistedasfollows:
tion), our proposed TechCD framework almost outperforms all
7https://luna.bdaa.pro baselinemodels(includingRandom,NLP-basedandGCN-based
989

| SIGIR’23,July23–27,2023,Taipei,Taiwan |     |     |     |     |     |     |     |     |     |     |     | WeiboGaoetal. |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
Table3:Performancecomparison.Thebestzero-shotstudentperformancepredictionishighlightedinbold,therunner-upis
underlined,and↑(↓)meansthehigher(lower)scorethebetterperformance,thesameasbelow.*indicatestheoracleresult.
|     |     |     |     | IRT |     |     | MIRT |     |     | NeuralCD |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | -------- | --- | --- | --- |
Random
Dataset Metric Oracle NLP GCNTechCD Oracle NLP GCNTechCD Oracle NLP GCN TechCD
ACC(%)↑ 77.89∗ 59.84 56.72 73.83∗ 56.44 56.74 74.65∗ 56.44 57.05 50.13
|     | S-CM |     |        |     | 63.45 |        |     | 64.73 |        |     | 57.06 |     |     |
| --- | ---- | --- | ------ | --- | ----- | ------ | --- | ----- | ------ | --- | ----- | --- | --- |
|     |      |     | 84.98∗ |     |       | 79.26∗ |     |       | 81.07∗ |     |       |     |     |
AUC(%)↑ 65.32 56.62 67.42 65.52 56.60 68.90 57.09 57.44 53.68 50.14
T-AM
RMSE(%)↓ 38.91∗ 47.98 50.75 47.59 48.40∗ 48.30 50.79 47.06 41.17∗ 49.69 50.72 49.49 57.70
ACC(%)↑ 77.67∗ 55.88 56.92 57.72 74.07∗ 55.88 56.92 57.78 74.34∗ 55.88 56.80 56.99 49.91
S-AM
AUC(%)↑ 85.50∗ 50.68 56.62 81.16∗ 56.62 59.02 81.61∗ 53.67 52.40 49.89
|     | T-CM |     |     |     | 58.99 |     | 60.56 |     |     | 57.55 |     |     |     |
| --- | ---- | --- | --- | --- | ----- | --- | ----- | --- | --- | ----- | --- | --- | --- |
RMSE(%)↓ 39.08∗ 53.21 54.46 52.85 47.93∗ 48.52 50.50 52.85 41.52∗ 49.87 50.72 49.57 57.78
ACC RMSE Table4:PerformanceofTechCDtrainedondifferentsettings.
True
|     | DS    |            | True     |      |       |     |          |     |     |                |             |          |       |
| --- | ----- | ---------- | -------- | ---- | ----- | --- | -------- | --- | --- | -------------- | ----------- | -------- | ----- |
|     |       |            |          |      |       |     | Training |     |     | Target ACC(%)↑ | AUC(%)↑     | RMSE(%)↓ |       |
|     | False |            | DS False |      |       |     |          |     |     |                |             |          |       |
|     |       |            |          |      |       |     | Random   |     |     | AM             | 50.13 50.14 |          | 57.70 |
|     |       | True False |          | True | False |     |          |     |     |                |             |          |       |
|     |       | DE         |          |      |       |     | CM       |     |     | AM             | 57.06 53.68 | 49.49    |       |
DE
Figure3:TheACCandRMSEcomparisonsonS-AMandT- (LA)Junyi AM 53.71 50.49 49.80
CM.Thedarker(lighter)meansthebetterforACC(RMSE). (LA)Assist AM 54.83 49.77 49.85
|     |     |     |     |     |     |     | (ASD)CM+Junyi |     |     | AM  | 56.60 52.10 |     | 49.84 |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | ----------- | --- | ----- |
models)onbothCMandAMtargetdomains,whichindicatesthe (ASD)CM+Assist AM 51.95 49.69
57.08
effectivenessofTechCDonpredictingstudentperformanceunder (ASD)CM+Junyi+Assist AM 56.73 52.11 49.57
thecold-startsetting.(2)BothGCN-basedandTechCDemploythe
knowledgeconceptgraphlinkingbothsourceandtargetdomains.
𝐿 canbeusedtojointlytrainthemodelwithEq.(2)as:
O
However,GCN-basedmethodsareunabletodiscardbottom-layer
|     |     |     |     |     |     |     |     |     | Θ∗=argminL(𝑦(𝐿 |     | +𝐿 ),G). |     | (10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --- | ---- |
informationanddiscriminatedifferentrelationsintheKCG.Incon- S O
Θ
trast,TechCDoutperformsGCN-basedmethods,whichpositively
|     |     |     |     |     |     |     | 5.6.2 | Limited | Access | (LA). In the | setting, student | performance |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------ | ------------ | ---------------- | ----------- | --- |
supportsitseffectiveness.
recordsareunavailableduetoprivacyprotectionpolicies.Toad-
Inthefollowingparts,weprimarilypresenttheexperimental
dressthisscenario,theout-domainOareintroducedtorefinethe
resultsofTech-NeuralCDastherepresentativeones,sinceother KCGbyreplacingsourcedomain’sdatasets𝐿 without-domain
S
diagnosisfunctionscanbeabstractedasthespecialcasesofNeu-
|            |                                     |     |     |     |     |     | datasets𝐿 | inEq.(2)as: |                |     |       |     |      |
| ---------- | ----------------------------------- | --- | --- | --- | --- | --- | --------- | ----------- | -------------- | --- | ----- | --- | ---- |
| ralCD[41]. |                                     |     |     |     |     |     |           | O           |                |     |       |     |      |
|            |                                     |     |     |     |     |     |           |             | Θ∗=argminL(𝑦(𝐿 |     | ),G). |     | (11) |
| 5.5        | Bottom-LayerDiscardingAnalysis(RQ2) |     |     |     |     |     |           |             |                |     | O     |     |      |
Θ
TheTechCDframeworkreliesonthebottom-layerdiscardingop- Table4liststheperformanceofTech-NeuralCD,indicatingthe
eration[54]togeneratetransferableembeddings.Werefertothe followingobservations.IntheASDsetting,theout-domaindatasets
operationofdiscardingbottom-layerembeddingofstudentand canpartlyimprovethepredictionperformanceofTechCD.IntheLA
exerciseembeddingsasDSandDE,respectively.Toevaluatethe setting,withtheout-domaindatasets,TechCDcangetapromising
impactofthisoperation,weperformvariousexperimentswith performancecomparedwithrandompredictions.Thesefindings
differentcombinationsofDSandDE.ThecomparisonsofACCand confirmtheKCGcanabsorbout-domaindatasetseffectively.
RMSEscoresunderthesettingofS-AMandT-CMarevisualized
inFigure3.Theexperimentalresultsindicatethatthebestperfor- 5.7 PopularApplicationsofTechCD(RQ4)
manceisachievedbyonlydiscardingthebottom-layeroutputfrom
TheaboveexperimentshaveprovedthatTechCDcancompletethe
theKCGforstudents(DS),highlightingtheeffectivenessofextract-
DZCDtaskeffectively.Inthispart,wedemonstratetwospecial
ingtransferableinformation.However,whenbothDSandDEare applicationsofourTechCDthatareinneedofindustrialpractice.
usedsimultaneously,theperformanceisweakened,emphasizing
theimportanceofmaintainingspecificpatternsforexercises. 5.7.1 DiagnosticReportGeneration. Providingdiagnosticreports
tostudentsviatheCDmethodisoneofthemosttypicalintelli-
5.6 ImprovingwithOut-DomainDatasets(RQ3)
gentapplicationsinintelligenteducation,whichcanhelpstudents
ThetailoredKCGcanlinkdifferentdomainsincludingthosewithin understandtheirlearningprocess.Traditionaldiagnosismethodsdi-
thesameplatformandthoseacrossplatforms.Thepreviousexperi- agnosestudents’proficiencyonknowledgeconceptslimitedinthe
mentsfocusonevaluatingperformancewithinsourceandtarget
sourcedomain,whileourTechCDcanfurtherinferstudents’cog-
| domains | that | share overlapping | students. | This | part shows | how |     |     |     |     |     |     |     |
| ------- | ---- | ----------------- | --------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
nitivestatesinthetargetdomain.Werandomlyselectonestudent
powerfulisTechCDforutilizingout-domaindatasetsfromother
intheCMdatasetstogenerateherdiagnosticreportsusingTech-
platformsundertwotypicalcold-startscenarios[54]. NeuralCDandtraditionalNeuralCDtrainedontheCMdataset.
Inthescenario,student WealsosampleasubgraphofKCGwhichcoverssomeknowledge
5.6.1 AccessibleStudentRecords(ASD).
performancerecords𝐿 inthesourcedomainSandout-domain conceptsofCMandJunyiwithsimilarityandprerequisiterelations.
S
records𝐿 inthetargetdomainOarebothavailable.Thus,𝐿 and Figure4(a)and(b)presentdiagnosticreportsofbothmodelsand
|     | O   |     |     |     |     | S   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
990

LeveragingTransferableKnowledgeConceptGraphEmbeddingforCold-StartCognitiveDiagnosis SIGIR’23,July23–27,2023,Taipei,Taiwan
Tech-NueralCD NeuralCD similarity prerequisite Table5:ExerciserecommendationofTechCD.
1 Mastery
5 0
0 1
.
. .
5
8 0
2
6
1
3
4
5 1.0 S-CMT-AM ○1 ○2 ○3 ○4 ○5 ○6 ○7 ○8 ○9 ○10
0.3 Exerciseid 232 1,632 2,432 30 123 2,003 3,020 175 220 250
0.0 2 0.5
8 Mastery(%) 67.23 38.24 40.07 23.00 48.63 57.30 84.33 54.27 48.24 57.78
7
4 3 CM Junyi 0.0 Difficulty(%) 50.20 51.30 49.93 50.21 49.98 50.00 50.03 50.10 49.99 49.93
(a) Diagnostic Report (b) Cognitive graph of Tech-NeuralCD Performance ✓ × × × ✓ ✓ ✓ × ✓ ✓
1. absolute value 5. negative number word problems thatcanhelpincreaseherengagementwiththematerial.(2)For
2. absolute value multiply 6. absolute values’ meaning
3. absolute value divide 7. absolute value add sub exercisesthatthestudentanswerscorrectly(incorrectly),theprofi-
4. adding negative numbers 8. comparing negative values ciencyofthecorrespondingconceptisalmosthigher(lower)than
Figure4:Theexampleofdiagnosticreports. theexercise’sdifficulty,indicatingthatstudentsanswercorrectly
thecognitivegraphofTech-NeuralCDrespectively.Fromthefigure, whentheirproficiencymeetsthedifficulty.ItconfirmsTechCD’s
weobservethat:(1)Forthemasterylevelsofknowledgeconcepts diagnosesareeffectiveinthecold-startdomain.
(1,2and3)inCM,Tech-NeuralCDandNeurcalCDcanoutputsimi-
6 CONCLUSION
lardiagnosisresults,indicatingthatbothmodelscanperformwell
Thispaperpresentsastudyonthedomain-levelzero-shotcogni-
onin-domaindatasets.(2)Forthoseknowledgeconcepts(4and5)
tivediagnosis(DZCD)task.DZCDisanimportanttaskforthe
sampledfromJunyi(asacold-startdomain),NeuralCDisunableto
lackofstudentbehaviordatainthetargetdomainduetotheab-
provideadiagnosis,whileTech-NeuralCDisstillabletoperform
senceofstudent-exerciseinteractionsorunavailabilityofexercising
effectively.(3)InthecognitivegraphofTech-NeuralCD,thedeeper
recordsfortraining.Totacklethis,weproposeageneralandtrans-
thecoloroftheconceptentity,thehigheritscognitivelevel.We
ferableframeworkTechCDthatutilizesapedagogicalknowledge
findthediagnosisresultsreasonableandinterpretable.Forexam-
conceptgraph(KCG)toconnectdifferentdomainsandpropagate
ple,thestudent’sproficiencyonconcepts3and4ispoor,which
students’universalcognitivestates.Thelearnedstudentembed-
isreflectedinherpoormasteryofconcept5.Thisisexpectedas
dingsbyTechCDaretransferable,whiletheexerciseembeddings
masteringconcepts3and4areprerequisitesforlearningconcept5.
aredomain-specific,enablingTechCDtoperformdomain-adaptive
Additionally,themasterylevelsonconcepts6and7aresimilaras
zero-shotcognitivediagnosisinthetargetdomain.Finally,exten-
theybelongtothesametopic(i.e.,absolutevalue).
siveexperimentsonreal-worlddatasetsnotonlyprovethatTechCD
5.7.2 ExerciseRecommendation. Thediagnosticresultscanbeuti-
caneffectivelymakethecognitivediagnosistaskforazero-shot
lizedtosuggestappropriateexercisestostudents,ratherthanre-
domainandoutperformseveralalternativebaselines,butalsoshow
lyingontheirownsearchefforts.Aproperrecommendersystem
thesuperiorapplicationpotentialsuchaspersonalizedexerciserec-
generallytakesintoaccounttwokeyobjectives:(O1:smoothness)
ommendationofTechCD.Inourfutureresearch,wewillfocuson
thedifficultylevelsofaseriesofrecommendationsshouldavoid
developingmoreadvancedmethodsforconstructingeducational
drasticvariationsasstudentslearnknowledgegradually[53];(O2:
KCGsthatcanbetterconnectdifferentdomains.Additionally,we
engagement)therecommendationsshouldnotbetoochallengingor
plantoexploremoresophisticatedapproachesforintegratingcon-
easytokeepstudents’enthusiasm[18].Forthesegoals,weimple-
mentasimpleyeteffectivestrategy8torecommend𝑥 exercisesfor ceptualrelationshipstofurtherimproveTechCD’sperformancein
theDZCDscenario.Ultimately,wehopethatourworkwillinspire
eachstudent.Concretely,witharefinedCDM,wefirstpredicteach
andinformfuturestudiesandapplicationsinthisarea.
student’sperformanceoneachexerciseasEq.(8).Allexercisescan
bedividedintotwosetsthatanswercorrectly(positivesamples)
Acknowledgements.Thisresearchwaspartiallysupportedby
grantsfromtheNationalKeyResearchandDevelopmentProgram
ornot(negativesamples)accordingtopredictionresults.Then,we
sample 𝑥 exercisesfromeachofthepositiveandnegativesamples. ofChina(No.2021YFF0901003),NationalNaturalScienceFounda-
2 tionofChina(No.62202443),andOpenResearchFundoftheState
Foreachsampling,werequiretheselectedexercise’sdifficultyto
KeyLaboratoryofCognitiveIntelligence(iED2022-002).
beclosetoathreshold(0.5inthispaper)toensurethesmoothness
objective.Finally,wecangettherecommendationlistsforeach
REFERENCES
student,whichsatisfytheaboveobjectives.
Weconductrecommendationsonthechallengingtargetdomain [1] HaoyangBi,HaipingMa,ZhenyaHuang,YuYin,QiLiu,EnhongChen,YuSu,
andShijinWang.2020.QualitymeetsDiversity:AModel-AgnosticFramework
thattraditionalCDMsareunabletohandle.Table5liststenexercise forComputerizedAdaptiveTesting.In2020IEEEInternationalConferenceonData
recommendationsonT-AMforarandomlyselectedstudentusing Mining(ICDM).IEEE,42–51.
[2] Haw-ShiuanChang,Hwai-JungHsu,andKuan-TaChen.2015.ModelingExercise
therefinedTech-NeuralCDmodeltrainedonS-CMdataset.The
RelationshipsinE-Learning:AUnifiedApproach..InEDM.532–535.
tablealsoincludesthediagnosedexercisedifficultiesandstudent [3] PengheChen,YuLu,VincentWZheng,andYangPian.2018.Prerequisite-driven
masterylevelsoftheassociatedconcepts,aswellasthestudent’s deepknowledgetracing.In2018IEEEInternationalConferenceonDataMining
trueperformanceontheexercisesasrecordedintheT-AMdataset.
(ICDM).IEEE,39–48.
[4] ShuoChenandThorstenJoachims.2016.Predictingmatchupsandpreferences
Wecanseethat:(1)Therecommendedexercisesaretailoredtothe incontext.InProceedingsofthe22ndACMSIGKDDInternationalConferenceon
student’sproficiency,neithertooeasynortoodifficult.Someof KnowledgeDiscoveryandDataMining.775–784.
[5] JimmyDeLaTorre.2009. DINAmodelandparameterestimation:Adidactic.
themwillchallengethestudent,whileotherswillserveas"gifts" Journalofeducationalandbehavioralstatistics34,1(2009),115–130.
[6] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova.2018.Bert:
8TechCDcansupportmanycomplexandpopularexerciserecommendationapproaches Pre-trainingofdeepbidirectionaltransformersforlanguageunderstanding.arXiv
like[1,18],thispartusesthesimplerecommendationmethodasanexample. preprintarXiv:1810.04805(2018).
991

SIGIR’23,July23–27,2023,Taipei,Taiwan WeiboGaoetal.
[7] NanDingandRaduSoricut.2017.Cold-startreinforcementlearningwithsoftmax 25thannualInternationalACMSIGIRconferenceonResearchanddevelopmentin
policygradient.AdvancesinNeuralInformationProcessingSystems30(2017). informationretrieval.253–260.
[8] HenryCEllis.1965.Thetransferoflearning.(1965). [33] RobinSchmuckerandTomMMitchell.2022.TransferableStudentPerformance
[9] SusanEEmbretsonandStevenPReise.2013.Itemresponsetheory.Psychology ModelingforIntelligentTutoringSystems.arXivpreprintarXiv:2202.03980(2022).
Press. [34] YiShang,HongchiShi,andSu-ShingChen.2001. Anintelligentdistributed
[10] WeiboGao,QiLiu,ZhenyaHuang,YuYin,HaoyangBi,Mu-ChunWang,Jianhui environmentforactivelearning.JournalonEducationalResourcesinComputing
Ma,ShijinWang,andYuSu.2021.Rcd:Relationmapdrivencognitivediagnosis (JERIC)1,2es(2001),4–es.
forintelligenteducationsystems.InProceedingsofthe44thInternationalACM [35] YuSu,QingwenLiu,QiLiu,ZhenyaHuang,YuYin,EnhongChen,ChrisDing,
SIGIRConferenceonResearchandDevelopmentinInformationRetrieval.501–510. SiWei,andGuopingHu.2018.Exercise-enhancedsequentialmodelingforstu-
[11] XavierGlorotandYoshuaBengio.2010.Understandingthedifficultyoftraining dentperformanceprediction.InProceedingsoftheAAAIConferenceonArtificial
deepfeedforwardneuralnetworks.InProceedingsofthethirteenthInternational Intelligence,Vol.32.
conferenceonartificialintelligenceandstatistics.JMLRWorkshopandConference [36] Shan-YunTeng,JundongLi,LoPang-YunTing,Kun-TaChuang,andHuanLiu.
Proceedings,249–256. 2018.Interactiveunknownsrecommendationine-learningsystems.In2018IEEE
[12] MargaretGrogan.1999.Equity/equalityissuesofgender,race,andclass.Educa- InternationalConferenceonDataMining(ICDM).IEEE,497–506.
tionalAdministrationQuarterly35,4(1999),518–536. [37] ShiweiTong,JiayuLiu,YutingHong,ZhenyaHuang,LeWu,QiLiu,WeiHuang,
[13] XiangnanHe,KuanDeng,XiangWang,YanLi,YongdongZhang,andMeng EnhongChen,andDanZhang.2022.IncrementalCognitiveDiagnosisforIntelli-
Wang.2020.Lightgcn:Simplifyingandpoweringgraphconvolutionnetworkfor gentEducation.InProceedingsofthe28thACMSIGKDDConferenceonKnowledge
recommendation.InProceedingsofthe43rdInternationalACMSIGIRconference DiscoveryandDataMining.1760–1770.
onresearchanddevelopmentinInformationRetrieval.639–648. [38] EmikoTsutsumi,RyoKinoshita,andMaomiUeno.2021.Deep-IRTwithIndepen-
[14] XiangnanHe,LiziLiao,HanwangZhang,LiqiangNie,XiaHu,andTat-Seng dentStudentandItemNetworks.InternationalEducationalDataMiningSociety
Chua.2017.Neuralcollaborativefiltering.InProceedingsofthe26thInternational (2021).
conferenceonworldwideweb.173–182. [39] KurtVanLehn.2011. Therelativeeffectivenessofhumantutoring,intelligent
[15] MinlieHuang,XiaoyanZhu,andJianfengGao.2020. Challengesinbuilding tutoringsystems,andothertutoringsystems. Educationalpsychologist46,4
intelligentopen-domaindialogsystems.ACMTransactionsonInformationSystems (2011),197–221.
(TOIS)38,3(2020),1–32. [40] ManasiVartak,ArvindThiagarajan,ConradoMiranda,JeshuaBratman,andHugo
[16] WenbingHuang,YuRong,TingyangXu,FuchunSun,andJunzhouHuang. Larochelle.2017.Ameta-learningperspectiveoncold-startrecommendations
2020.Tacklingover-smoothingforgeneralgraphconvolutionalnetworks.arXiv foritems.Advancesinneuralinformationprocessingsystems30(2017).
preprintarXiv:2008.09864(2020). [41] FeiWang,QiLiu,EnhongChen,ZhenyaHuang,YuyingChen,YuYin,ZaiHuang,
[17] XiaoqingHuang,QiLiu,ChaoWang,HaoyuHan,JianhuiMa,EnhongChen,Yu andShijinWang.2020. Neuralcognitivediagnosisforintelligenteducation
Su,andShijinWang.2019.ConstructingEducationalConceptMapswithMultiple systems.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.34.
RelationshipsfromMulti-SourceData.In2019IEEEICDM.IEEE,1108–1113. 6153–6161.
[18] ZhenyaHuang,QiLiu,ChengxiangZhai,YuYin,EnhongChen,WeiboGao, [42] HaoWang,EnhongChen,QiLiu,TongXu,DongfangDu,WenSu,andXiaopeng
andGuopingHu.2019.Exploringmulti-objectiveexerciserecommendationsin Zhang.2018.Aunitedapproachtolearningsparseattributednetworkembedding.
onlineeducationsystems.InProceedingsofthe28thACMInternationalConference In2018IEEEInternationalConferenceonDataMining(ICDM).IEEE,557–566.
onInformationandKnowledgeManagement.1261–1270. [43] HaoWang,DefuLian,HanghangTong,QiLiu,ZhenyaHuang,andEnhong
[19] YujiaHuo,DerekFWong,LionelMNi,LidiaSChao,andJingZhang.2020.Knowl- Chen.2021.Hypersorec:Exploitinghyperbolicuseranditemrepresentations
edgemodelingviacontextualizedrepresentationsforLSTM-basedpersonalized withmultipleaspectsforsocial-awarerecommendation.ACMTransactionson
exerciserecommendation.InformationSciences523(2020),266–278. InformationSystems(TOIS)40,2(2021),1–28.
[20] DiederikPKingmaandJimmyBa.2014.Adam:Amethodforstochasticopti- [44] HaoWang,TongXu,QiLiu,DefuLian,EnhongChen,DongfangDu,HanWu,
mization.arXivpreprintarXiv:1412.6980(2014). andWenSu.2019. MCNE:Anend-to-endframeworkforlearningmultiple
[21] JiatongLi,FeiWang,QiLiu,MengxiaoZhu,WeiHuang,ZhenyaHuang,Enhong conditionalnetworkrepresentationsofsocialnetwork.InProceedingsofthe25th
Chen,YuSu,andShijinWang.2022. HierCDF:ABayesianNetwork-based ACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining.
HierarchicalCognitiveDiagnosisFramework.InProceedingsofthe28thACM 1064–1072.
SIGKDDConferenceonKnowledgeDiscoveryandDataMining.904–913. [45] MinjieWang,DaZheng,ZihaoYe,QuanGan,MufeiLi,XiangSong,Jinjing
[22] QiLiu,ZhenyaHuang,YuYin,EnhongChen,HuiXiong,YuSu,andGuopingHu. Zhou,ChaoMa,LingfanYu,YuGai,etal.2019. Deepgraphlibrary:Agraph-
2019.Ekt:Exercise-awareknowledgetracingforstudentperformanceprediction. centric,highly-performantpackageforgraphneuralnetworks.arXivpreprint
IEEETransactionsonKnowledgeandDataEngineering33,1(2019),100–115. arXiv:1909.01315(2019).
[23] QiLiu,RunzeWu,EnhongChen,GuandongXu,YuSu,ZhigangChen,andGuop- [46] ZhengyangWu,MingLi,YongTang,andQingyuLiang.2020.Exerciserecom-
ingHu.2018.Fuzzycognitivediagnosisformodellingexamineeperformance. mendationbasedonknowledgeconceptprediction.Knowledge-BasedSystems
ACMTransactionsonIntelligentSystemsandTechnology(TIST)9,4(2018),1–26. 210(2020),106481.
[24] YeLiu,HanWu,ZhenyaHuang,HaoWang,JianhuiMa,QiLiu,EnhongChen, [47] JieXu,ChengDeng,XinboGao,DinggangShen,andHengHuang.2017.Pre-
HanqingTao,andKeRui.2020.Technicalphraseextractionforpatentmining: dictingAlzheimer’sdiseasecognitiveassessmentviarobustlow-rankstructured
Amulti-levelapproach.In2020IEEEInternationalConferenceonDataMining sparsemodel.InIJCAI:proceedingsoftheconference,Vol.2017.NIHPublicAccess,
(ICDM).IEEE,1142–1147. 3880.
[25] NimaMirbakhshandCharlesXLing.2015.Improvingtop-nrecommendationfor [48] LinanYue,QiLiu,YichaoDu,YanqingAn,LiWang,andEnhongChen.2022.
cold-startusersviacross-domaininformation.ACMTransactionsonKnowledge DARE:Disentanglement-AugmentedRationaleExtraction.AdvancesinNeural
DiscoveryfromData(TKDD)9,4(2015),1–19. InformationProcessingSystems35(2022),26603–26617.
[26] HiromiNakagawa,YusukeIwasawa,andYutakaMatsuo.2019. Graph-based [49] SiZhang,HanghangTong,JiejunXu,andRossMaciejewski.2019.Graphconvo-
KnowledgeTracing:ModelingStudentProficiencyUsingGraphNeuralNetwork. lutionalnetworks:acomprehensivereview.ComputationalSocialNetworks6,1
In2019IEEE/WIC/ACMInternationalConferenceonWebIntelligence(WI).IEEE, (2019),1–23.
156–163. [50] HaoZhao,MingLu,AnbangYao,YurongChen,andLiZhang.2020.Learningto
[27] TuanNguyen.2015.Theeffectivenessofonlinelearning:Beyondnosignificant drawsightlines.InternationalJournalofComputerVision128(2020),1076–1100.
differenceandfuturehorizons.MERLOTJournalofonlinelearningandteaching [51] HaoZhao,MingLu,AnbangYao,YiwenGuo,YurongChen,andLiZhang.
11,2(2015),309–319. 2017.Physicsinspiredoptimizationonsemantictransferfeatures:Analternative
[28] LiangmingPan,ChengjiangLi,JuanziLi,andJieTang.2017.Prerequisiterelation methodforroomlayoutestimation.InProceedingsoftheIEEEconferenceon
learningforconceptsinmoocs.InProceedingsofthe55thAnnualMeetingofthe computervisionandpatternrecognition.10–18.
AssociationforComputationalLinguistics(Volume1:LongPapers).1447–1456. [52] HaoZhao,MingLu,AnbangYao,YiwenGuo,YurongChen,andLiZhang.2020.
[29] AdamPaszke,SamGross,FranciscoMassa,AdamLerer,JamesBradbury,Gregory Pointly-supervisedsceneparsingwithuncertaintymixture.ComputerVisionand
Chanan,TrevorKilleen,ZemingLin,NataliaGimelshein,LucaAntiga,etal.2019. ImageUnderstanding200(2020),103040.
Pytorch:Animperativestyle,high-performancedeeplearninglibrary.Advances [53] WayneXinZhao,WenhuiZhang,YulanHe,XingXie,andJi-RongWen.2018.
inneuralinformationprocessingsystems32(2019). Automaticallylearningtopicsanddifficultylevelsofproblemsinonlinejudge
[30] MarkDReckase.2009. Multidimensionalitemresponsetheorymodels. In systems.ACMTransactionsonInformationSystems(TOIS)36,3(2018),1–33.
Multidimensionalitemresponsetheory.Springer,79–112. [54] JianhuanZhuo,JianxunLian,LanlingXu,MingGong,LinjunShou,DaxinJiang,
[31] SteffenRendle,ChristophFreudenthaler,ZenoGantner,andLarsSchmidt-Thieme. XingXie,andYinliangYue.2022.Tiger:TransferableInterestGraphEmbedding
2012.BPR:Bayesianpersonalizedrankingfromimplicitfeedback.arXivpreprint forDomain-LevelZero-ShotRecommendation.InProceedingsofthe31stACM
arXiv:1205.2618(2012). InternationalConferenceonInformation&KnowledgeManagement.2806–2816.
[32] AndrewISchein,AlexandrinPopescul,LyleHUngar,andDavidMPennock.
2002.Methodsandmetricsforcold-startrecommendations.InProceedingsofthe
992