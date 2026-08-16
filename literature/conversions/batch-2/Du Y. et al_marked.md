---
conversion_metadata:
  converted_at: "2026-07-22T13:13:15Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Du Y. et al.pdf"
  source_pdf_sha256: "1676d1f72b7616498e4cf337927738043d8c1a90f0dbb171b680a72e4e61cc45"
  page_count: 11
  markdown_char_count: 142633
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

PAnDA: Combating Negative Augmentation via Large Language
Models for User Cold-Start Recommendations
Rui Chen*
Harbin Engineering University
Harbin, China
ruichen@hrbeu.edu.cn

Yantong Du
Harbin Engineering University
Harbin, China
duyantong94@hrbeu.edu.cn

Xiangyu Zhao*
City University of Hong Kong
Hong Kong, China
xianzhao@cityu.edu.hk

Qilong Han
Harbin Engineering University
Harbin, China
hanqilong@hrbeu.edu.cn

A. K. Qin
Swinburne University of Technology
Hawthorn, Victoria 3122, Australia
kqin@swin.edu.au

Abstract
The cold-start problem remains a long-standing challenge in rec-
ommender systems. Recent advances in large language models
(LLMs) have opened new avenues for addressing cold-start sce-
narios through data augmentation. However, existing cold-start
augmentation methods often suffer from negative augmentation,
manifesting as incomplete augmentation, where generated interac-
tions fail to comprehensively reflect user preferences, and inaccurate
augmentation, where they conflict with user intent. These issues
largely stem from two limitations: (1) the inability to effectively
incorporate collaborative signals, which are critical for preference
alignment, and (2) the lack of awareness of the downstream model’s
learning dynamics during data augmentation. To the best of our
knowledge, the latter has not been studied in the literature.

Consequently, we propose a novel framework named PAnDA.
To address the incomplete augmentation issue, we propose a model-
agnostic preference-aligned augmentation module to iteratively
extract and fuse textual information and collaborative informa-
tion by user-user preference matching and user-item preference
coherence, which together form a contextual cue to guide the aug-
mentor to generate high-quality augmented data. To overcome
the inaccurate augmentation issue, we propose a model-specific
downstream-model-aware adaptation module to adaptively align
the augmented data with the model’s states during the training
process, guided by gradient similarity. Extensive experiments on
three public benchmark datasets demonstrate that PAnDA outper-
forms different groups of state-of-the-art cold-start recommenda-
tion methods in all scenarios. The source code is publicly available
at https://github.com/YantongDU/PAnDA.

CCS Concepts
• Information systems → Personalization; Information ex-
traction; • Computing methodologies → Machine learning.

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
CIKM ’25, Seoul, Republic of Korea
© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-2040-6/2025/11
https://doi.org/10.1145/3746252.3761080

Keywords
Cold-start recommendations; large language models; data augmen-
tation; meta-learning

ACM Reference Format:
Yantong Du, Rui Chen*, Xiangyu Zhao*, Qilong Han, and A. K. Qin. 2025.
PAnDA: Combating Negative Augmentation via Large Language Models
for User Cold-Start Recommendations. In Proceedings of the 34th ACM Inter-
national Conference on Information and Knowledge Management (CIKM ’25),
November 10–14, 2025, Seoul, Republic of Korea. ACM, New York, NY, USA,
11 pages. https://doi.org/10.1145/3746252.3761080

1 Introduction
Recommender systems have played a crucial role in mitigating
information overload in a wide range of real-world applications by
efficiently providing online users with relevant content. Existing
recommendation models, such as collaborative filtering [7] and
content-based methods [4, 8], typically recommend appropriate
items to users by learning user/item representations from their
historical interactions (e.g., clicks, ratings, purchases). It is natural
that this idea would fail in scenarios where user-item interactions
are limited, which is known as the cold-start problem [2, 32], a
long-standing challenge for recommender systems.

An intuitive strategy to address the cold-start problem is to gen-
erate additional user interactions (i.e., data augmentation) to enrich
user behaviors and further guide model learning. This allows rec-
ommendation models to capture more diverse user preferences, as
illustrated in Fig. 1(a). Some studies have explored multi-modal
augmentation, leveraging auxiliary information such as images[38],
audio [9], and text [30, 38] to simulate interactions that better repre-
sent users’ interests. More recently, the emergence of large language
models (LLMs) has opened up new opportunities for data augmen-
tation in recommendation tasks [22, 30]. Owing to their extensive
world knowledge and strong capabilities in language generation and
reasoning, LLMs are increasingly regarded as promising augmenta-
tion tools in cold-start scenarios [35]. They can complement sparse
user or item information and generate contextually appropriate aug-
mented interactions. However, existing augmentation methods still
suffer from significant limitations in cold-start settings. Due to the
difficulty of multi-modal alignment and limited model generative
capabilities, these methods struggle to accurately capture user pref-
erences and can result in augmented interactions that contradict
user intents, mislead model learning, and degrade recommendation

---

<!-- PAGE 2 -->

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

Yantong Du, Rui Chen, Xiangyu Zhao, Qilong Han, and A. K. Qin

performance, called negative augmentation, as shown in Fig. 1(b).
It can be further categorized into two core challenges. From the
data perspective, the reliance on multi-modal information often
results in incomplete augmentation, as it fails to comprehensively
capture user preferences. From the model perspective, limited gen-
erative capability can lead to inaccurate augmentation, where the
augmented interactions misalign with user intents.

To achieve complete data augmentation, recent methods have
attempted to integrate collaborative signals with multi-modal in-
formation [9, 31]. However, effectively fusing these heterogeneous
sources remains an open challenge. This challenge is further ex-
acerbated in cold-start scenarios, where limited interaction data
makes it even more difficult to balance the complementary strengths
of content semantics and collaborative patterns. As a result, aug-
mented interactions are often biased toward a single modality or
signal type, failing to provide a holistic representation of user pref-
erences and ultimately degrading the performance of downstream
recommendation models.

On the other hand, inaccurate augmentation arises from the capa-
bility limitations of generative models. For example, clickbait titles
or mismatched image-text pairs [8, 31, 40] may guide the model to
augment interactions that are superficially relevant but semanti-
cally inconsistent with the user’s true intent. Incorporating such
inaccurate augmentation into model training indiscriminately not
only introduces label noise but can also distort learned preference
distributions and increase overfitting risks. In extreme cases, this
may cause the model to over-personalize or recommend irrelevant
items, further deteriorating the user experience. Moreover, the aug-
mented data will be consumed by a downstream recommendation
model. Different models have disparate learning capabilities and
thus expect different extents/types of data augmentation (e.g., the
number of augmented interactions needed for a cold-start user),
suggesting that LLM-based data augmentation needs to be aware of
the downstream model. More specifically, the downstream model’s
training status needs to be considered in the data augmentation
process. Therefore, mitigating inaccuracy while ensuring compat-
ibility with the downstream recommendation model presents an
additional challenge for LLM-based data augmentation.

To address these two challenges, we propose a novel preference-
aligned and downstream-model-aware data augmentation frame-
work PAnDA inspired by the pre-train and fine-tune paradigm [16,
17, 38], which consists of two complementary modules, as shown in
Fig. 1(c). A model-agnostic preference-aligned augmentation module
like a pre-training stage, and a model-specific downstream-model-
aware adaptation module like a fine-tuning stage. Specifically, to
mitigate incomplete augmentation, we focus on generating diverse
and comprehensive user-item interactions. We perform the user-
user preference matching by focusing on preference differences
between users and designing a unique prompt to be used as a con-
textual cue to assist LLMs in generating augmented interactions.
Additionally, we leverage user-item preference coherence to fur-
ther model collaborative structures, enabling more personalised
and accurate augmentation. These two components work in tandem
to integrate both multi-modal content and collaborative signals,
achieving more complete data augmentation. To address inaccurate
augmentation, we further introduce a model-specific adaptation
module. This component dynamically assesses the relevance of

Figure 1: An illustration of different data augmentation meth-
ods in the cold-start recommendation scenario.

each augmented sample by monitoring the learning state of the
downstream recommender. By selectively incorporating or discard-
ing augmented interactions, it enhances the alignment between the
augmented data and the model’s learning objectives and prevents
noisy or harmful samples from degrading performance.

To summarize, the main contributions of our work are as follows:
• We are the first to identify and study the negative augmen-
tation in cold-start recommendation, highlighting that more
augmented data does not necessarily lead to better performance.
We reveal two underlying challenges: incomplete augmentation
from the data perspective and inaccurate augmentation from
the model perspective, which degrade the effectiveness of data
augmentation methods.

• We introduce a novel preference-aligned and downstream-model-
aware data augmentation framework PAnDA powered by LLMs.
It consists of a model-agnostic preference-aligned augmentation
module and a model-specific downstream-model-aware adapta-
tion module, which together effectively address the two limita-
tions. PAnDA also features a decoupled design to accommodate
different combinations of LLMs and downstream recommenda-
tion models.

• We have performed extensive experiments on three real-world

benchmark datasets and shown that PAnDA, being both preference-
aligned and downstream-model-aware, can consistently outper-
form different groups of state-of-the-art cold-start recommenda-
tion methods in all scenarios.

2 Preliminary
In this section, we first introduce the problem formulation and
notations, followed by a general overview of data augmentation in
recommender systems.
Problem Formulation. Let U and V denote the sets of users and
items, respectively. The user-item interaction matrix is defined as
𝑨 ∈ 0, 1| U | × | V | , where 𝐴𝑢𝑣 = 1 indicates that user 𝑢 has interacted
with item 𝑣. The interaction history of user 𝑢 is denoted by V𝑢 =
𝑣1, 𝑣2, . . . , 𝑣 | V𝑢 | . Collaborative filtering (CF) methods learn from 𝑨
to obtain user and item ID-based embeddings 𝑬 = {𝑬𝑢, 𝑬 𝑣 } for
prediction. However, such methods struggle in cold-start settings
where user/item IDs are unseen. To address this, profile-based CF
methods incorporate side information P = {P𝑈 , P𝑉 } for users and
items, and learn representations using a function 𝑓Θ𝑟𝑒𝑐 based on

---

<!-- PAGE 3 -->

PAnDA: Combating Negative Augmentation via Large Language Models for User Cold-Start Recommendations

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

both 𝑨 and P. The model is trained by maximizing the posterior:

Θ∗

𝑟𝑒𝑐 = arg max

Θ𝑟𝑒𝑐

𝑝 (Θ𝑟𝑒𝑐 |𝑨, P),

(1)

𝑠𝑢,𝑚 = 𝑨𝑢 ⊙ 𝑨𝑚,

(5)

where 𝑓Θ𝑟𝑒𝑐 will output the final user representation 𝒉𝑢 contain
both collaborative signals from 𝑬 and side information 𝑝𝑢 via:

𝒉𝑢 = 𝑓Θ𝑟𝑒𝑐 (𝑨, 𝑝𝑢 ).

(2)

The item’s final representation 𝒉𝑣 can also be obtained similarly.
Data augmentation for Recommender Systems. In cold-start
scenarios, the sparsity of interactions motivates the use of data
augmentation. Let 𝑓Θ𝑎𝑢𝑔 denote the augmentation function, which
generates synthetic interactions (cid:101)𝑨 from 𝑨 and P via:

(cid:101)𝑨 = 𝑓Θ𝑎𝑢𝑔 (𝑨, P).
(3)
The downstream recommender model 𝑓Θ𝑟𝑒𝑐 is then trained with
the augmented data 𝑨𝑎𝑢𝑔 = {𝑨, (cid:101)𝑨} to explore user preferences,
which can be expressed via:

Θ∗ = arg max

Θ

𝑝 (𝑨𝑎𝑢𝑔, P),

(4)

where Θ is the trainable parameter of the models, Θ = {Θ𝑎𝑢𝑔, Θ𝑟𝑒𝑐 }.
After training with augmented data 𝑨𝑎𝑢𝑔, the recommender model
𝑓Θ𝑟𝑒𝑐 is used to predict preference score ˆ𝑦𝑢,𝑣 by ranking the likeli-
hood of user 𝑢 will interact with item 𝑣.

3 Methodology
To address the user cold-start problem, we propose the PAnDA
framework, illustrated in Figure 2. First, we introduce a model-
agnostic preference-aligned augmentation module. It leverages tex-
tual and collaborative signals for user-user preference matching,
where LLMs serve as the Textual Information Augmentor (TIA).
Additionally, user-item preference coherence is used to capture user
interests and item features, with LLMs enhancing personaliza-
tion by guiding the integration of collaborative signals and mit-
igating incomplete augmentation. Second, we present a model-
specific downstream-model-aware adaptation module. This compo-
nent aligns augmented data with the training signals of downstream
recommenders, enabling effective preference-aligned augmentation
and alleviating data sparsity in cold-start scenarios.

3.1 Model-Agnostic Preference-Aligned

Augmentation

3.1.1 User-User Preference Matching. To address the cold-start
problem and effectively leverage auxiliary information for interpret-
ing user preferences and item characteristics, we focus on textual
signals and employ LLMs as the Textual Information Augmentor
(TIA). By converting the augmentation task into a natural language
description, LLMs generate meaningful user-item interaction pairs
for each user 𝑢, drawing on their strong reasoning capabilities and
broad knowledge. We also incorporate interaction histories from
similar users as references to enhance augmentation quality.

Specifically, for each user 𝑢, we construct a similar user set 𝑺𝑢 . In
cold-start scenarios, embedding-based similarity is often unreliable
due to sparse interactions. Instead, we measure similarity based
on interaction history. Let 𝑨𝑢 = {0, 1} ∈ R1× |𝑉 | denote the binary
interaction vector of user 𝑢, we compute similarity with user 𝑚 as:

where ⊙ denotes element-wise multiplication. We select the top-K
similar users 𝑺𝑢 as auxiliary context and combine each user’s profile
(e.g., age, gender), interaction history, and candidate item set 𝑪𝑢 to
construct a textual prompt P𝑢 for the LLM. The LLM then generates
an augmented interaction pair for user 𝑢, consisting of a preferred
item 𝑣 +,𝑡

𝑢 and a non-preferred item 𝑣 −,𝑡
𝑢

from 𝑪𝑢 via:

P𝑢 = Text(𝑢, 𝑺𝑢, 𝑪𝑢, 𝑨, P),
𝑢 } = LLM(P𝑢 ),

{𝑣 +,𝑡

𝑢 , 𝑣 −,𝑡

(6)

𝑢

𝑢 }𝑢 ∈ U and { (cid:101)V −,𝑡

where Text(·) denotes the prompt construction function. The can-
didate set 𝑪𝑢 is obtained by hard sampling high-ranking items
from a base recommender (e.g., BPR [21], LightGCN [6]). This pro-
cess yields the positive and negative augmented interaction sets
}𝑢 ∈ U, where | (cid:101)V+,𝑡
{ (cid:101)V+,𝑡
| = 𝑀 for each
user 𝑢. By constraining augmentation to a pre-filtered candidate
set and incorporating similar users’ interactions as context, we
enhance generation accuracy and mitigate noise from sparse data.
Considering token-length limits of LLMs [3, 43], we avoid feeding
the full item set and instead rely on a compact, informative sub-
set. Overall, the proposed Textual Interaction Augmentation (TIA)
module enables text-driven augmentation guided by collaborative
signals, balancing interpretability and personalization.

| = | (cid:101)V −,𝑡

𝑢

𝑢

3.1.2 User-Item Preference Coherence. Although LLMs, as the TIA,
fully leverage auxiliary information, they have a critical limita-
tion: the upper bound of the augmented data quality depends on
the candidate item set 𝐶𝑢 . Unfortunately, due to the constraints
of the cold-start scenario, the base recommender also struggles to
accurately capture user preferences, leading to varying quality for
candidate sets. Additionally, LLMs primarily rely on processing and
understanding input text, which leads to the fact that the augmented
data generated by LLMs still has limitations. Due to the input token
limitations of LLMs and the difficulty of incorporating collaborative
signals from interaction data into LLMs and further gaining atten-
tion, we generate augmented data complemented by collaborative
signals and propose the Collaborative Signal Augmentor (CSA).

3.1.3 Meta Masked Autoencoder (MetaMAE). To leverage collabo-
rative information, we fine-tune the pre-trained model 𝑓
. For
Θ𝑝𝑡
𝑟𝑒𝑐
user 𝑢 and augmented interacted item set V𝑢,𝑡 = V𝑢 ∪ (cid:101)V+,𝑡
𝑢 , we
can obtain the item set representations via:

𝑯 𝑢 = 𝑆𝑡𝑎𝑐𝑘 ({𝒉𝑖 }𝑖 ∈ V𝑢,𝑡 ),

(7)

which 𝑆𝑡𝑎𝑐𝑘 (·) is the vector stacking operation. 𝒉𝑖 ∈ R𝑑 is the repre-
sentation of item 𝑖 and obtained through Eq. (2), and 𝑯 𝑢 ∈ R| V𝑢,𝑡 | ×𝑑 .
To learn an accurate and comprehensive representation of the user,
we utilize the augmented interactions generated by LLMs from
the perspective of items to guide the model’s learning, thereby in-
corporating rich textual information into the item representations.
To mitigate the impact of incomplete augmentation, we employ a
Masked Autoencoder (MAE) to enhance the user/item representa-
tions of users and items.

---

<!-- PAGE 4 -->

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

Yantong Du, Rui Chen, Xiangyu Zhao, Qilong Han, and A. K. Qin

Figure 2: The architecture of the proposed PAnDA model. (a) demonstrates the textual information data augmentation process
with LLMs. (b) describes the MetaMAE augment data with the collaborative signals. (c) introduces the downstream-model-aware
filtering strategy for filtering model-mismatched interactions.

capability of items, we use a feature restoration loss via:

𝛾

L𝑢

𝑓 𝑟 =

1
|V𝑢,𝑡 |

∑︁

𝑣 ∈ V𝑢,𝑡

1 −

(cid:98)𝑯 𝑢 · 𝑯 𝑢
(cid:13)
(cid:13)
(cid:13)

(cid:13)
(cid:13)
(cid:13)(cid:98)𝑯 𝑢

· ∥𝑯 𝑢 ∥

(cid:169)
(cid:173)
(cid:173)
(cid:171)

(cid:170)
(cid:174)
(cid:174)
(cid:172)

,

(10)

where 𝛾 is the scaling factor, which is a hyperparameter.

Last, we aggregate the latent representation of user 𝑢 that in-
corporates item-level collaborative signals and textual information,
𝑧𝑢 , with the profile-based user representation, ℎ𝑢 obtained through
Eq. (2), to conduct the user’s final collaborative representation via:
𝒇 𝑢 = (1 − 𝛼)𝒉𝑢 + 𝛼𝒛𝑢,
(11)
where 𝛼 is the trainable parameter. Then, we can conduct the pre-
diction score of the user 𝑢 to the item 𝑣 via:

ˆ𝑦𝑐
𝑢,𝑣 = 𝒇 𝑢 · 𝒉𝑣 .
(12)
Subsequently, we select the top-𝑀 items with the highest pre-
diction scores as augmented positive samples V+,𝑐
𝑢 . Conversely,
we select the bottom-𝑀 items with the lowest scores as negative
samples V −,𝑐
. The collaborative signal will then be fed into the
next iteration to refine the candidate item set 𝑪𝑢 .

𝑢

3.1.4 Meta optimization for MetaMAE. Since each user’s prefer-
ences are different, using a shared-parameter autoencoder would
struggle to capture the personalized differences among users ac-
curately. In cold-start scenarios, the limited interaction data can
also lead to undifferentiated representations of users or items. In-
spired by meta-learning [33, 42], we designed a meta-optimization
strategy to ensure each user has a personalized autoencoder that
captures their unique preferences via:

∑︁

L𝑟𝑒𝑐 (V𝑢, (cid:101)V𝑡

𝑢 , (cid:101)V𝑐

𝑢 (𝜃𝑢,∗

𝐴𝐸 ); Θ),

min
Θ

𝑢 ∈ U
𝑠.𝑡 ., 𝜃𝑢,∗
𝐴𝐸 ← arg min

𝜃𝐴𝐸

L𝑓 𝑟 (V𝑢, (cid:101)V𝑡

𝑢 , Θ𝑝𝑡

𝑟𝑒𝑐 ; 𝜃𝐴𝐸),

(13)

Figure 3: An illustration of the structure of prompts. The
figure shows the prompt designed for movie datasets. For
the Book-Crossing dataset, we use [id], [book title], [author],
[genre] as descriptors.

First, for user 𝑢 and the set of positive samples V+

𝑢 generated
by LLMs, we select a subset (cid:101)v𝑢 ⊆ (cid:101)V+,𝑡
and mask their representa-
tions with a mask token [𝑀𝐴𝑆𝐾], represented as 𝒉[𝑀𝐴𝑆𝐾 ] (e.g., a
learnable vector or mean pooling). The masking operation via:

𝑢

(cid:101)𝒉𝑣 =

(cid:26) 𝒉𝑣

𝒉[MASK]

if 𝑣 ∉ (cid:101)v𝑢
if 𝑣 ∈ (cid:101)v𝑢 .

(8)

It is worth noting that we only perform the mask operation on
the augmented interactions to make the model more robust without
losing the original information.

Second, we use the masked user interaction set V𝑀

𝑢 as the input

to the autoencoder and reconstruct the representations via:
(cid:98)𝑯 𝑢, 𝒛𝑢 = 𝐴𝑢𝑡𝑜𝐸𝑛𝑐𝑜𝑑𝑒𝑟 (𝑯

(9)
where 𝒛𝑢 represents the latent representation of user 𝑢. 𝜃𝐴𝐸 is the
trainable parameter of the autoencoder.

𝑀
𝑢 ; 𝜃𝐴𝐸),

Third, we attempt to reconstruct the representation of the in-
teracted item set V𝑢,𝑡 for user 𝑢. To enhance the representational

---

<!-- PAGE 5 -->

PAnDA: Combating Negative Augmentation via Large Language Models for User Cold-Start Recommendations

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

𝑢

𝑢

𝑢 = { (cid:101)V+,𝑡
𝑢 (𝜃𝑢,∗

where 𝜃𝑢,∗
𝐴𝐸 represents the personalized autoencoder parameters
for user 𝑢 after convergence through training with the augmented
interaction data. 𝑉𝑢 denotes the original set of interacted items
𝑢 , (cid:101)V −,𝑡
for the user 𝑢, while (cid:101)V𝑡
} represents the item pairs
𝑢 , (cid:101)V −,𝑐
𝐴𝐸 ) = { (cid:101)V+,𝑐
augmented by the TIA. (cid:101)V𝑐
} denotes the item
pairs augmented by the CSA using parameters 𝜃𝑢,∗
𝐴𝐸 . L𝑟𝑒𝑐 is the
recommendation loss of the downstream recommender model 𝑓Θ,
which will be elaborated later. To fully integrate with the train-
ing process of the downstream recommender system, we adopted
the end-to-end optimization strategy. Therefore, we employed the
reparameterization trick [15] to implement the data augmentation
process of the CSA. MetaMAE incorporates textual information
to enhance the representation capability of the model, learning
comprehensive user/item representations that integrate both col-
laborative signals and textual information. Additionally, using a
bi-level meta-optimization strategy distinguishes between differ-
ent users when generating augmented data, thereby producing
comprehensive and personalized augmented data. This approach
effectively addresses the issue of incomplete augmentation.

3.2 Model-Specific Downstream-Model-Aware

Adaptation

𝑢 , (cid:101)V𝑐

We obtain augmented interactions for user 𝑢, (cid:101)V𝑢 = (cid:101)V𝑡
𝑢 , in-
cluding true positives and preference-aligned samples. However,
not all of these interactions are equally useful for the downstream
recommender. In cold-start settings, the quality of augmented data
varies, and limited user understanding may cause some samples to
diverge from the model’s current learning trajectory. Training on
all samples indiscriminately risks noise, misleading optimization,
and performance drops. Since models differ in training dynamics,
they may react differently to the same data. Thus, it is essential
to check each interaction’s compatibility with the model’s current
state. Inspired by curriculum learning, we evaluate sample–model
alignment at each iteration, enabling the model to emphasize infor-
mative data and filter mismatched ones, improving representations
without distorting user intent.

Specifically, we define the training loss for user 𝑢’s interactions:

L (V𝑢 ) =

∑︁

𝑣+,𝑣− ∈ V𝑢

L𝑟𝑒𝑐 (𝑢, 𝑣 +, 𝑣 −),

(14)

where L𝑟𝑒𝑐 (·) is the loss function of the downstream recommender
parameterized by Θ. Some prior work filters out augmented inter-
actions with high loss, assuming they are model-mismatched. How-
ever, this overlooks a key limitation: high loss does not necessarily
imply low quality. In many cases, such interactions are informa-
tive hard examples that can improve model robustness. Discarding
them may lead to underfitting and missed learning opportunities.
Conversely, low-loss interactions may be uninformative or even
misleading if they poorly reflect user preferences. Therefore, loss
alone is not a reliable signal for evaluating augmentation quality.
Instead, we propose to use gradient signals [1, 11] to assess the
alignment between each augmented interaction and the model’s
current learning direction. By measuring the gradient similarity
between augmented and original interactions, we can more accu-
rately identify and retain useful samples while filtering out those
inconsistent with the model’s optimization path.

First, we compute the average gradient of the loss over the origi-
nal interaction set V𝑢 , which represents the model’s direction for
updating parameters based on the user’s actual preferences via:
∑︁

∇ΘL𝑟𝑒𝑐 (𝑢, 𝑣 +, 𝑣 −),

(15)

∇ΘL (V𝑢 ) =

{𝑣+,𝑣− } ∈ V𝑢
Second, for each augmented interaction pair ˜𝑣 +, ˜𝑣 −, we calculate
the cosine similarity between its gradient and the gradient of the
original user interactions to evaluate alignment via:

1
|V𝑢 |

𝑠𝑖𝑚({ ˜𝑣 +, ˜𝑣 − }, V𝑢 ) = (cid:10)∇ΘL𝑟𝑒𝑐 (𝑢, ˜𝑣 +, ˜𝑣 −), ∇ΘL (V𝑢 )(cid:11) ,

(16)
where ⟨·, ·⟩ denotes a cosine similarity operator between gradients.
Last, for each user 𝑢, we sort all augmented interaction pairs
{ ˜𝑣 +, ˜𝑣 − } ∈ (cid:101)V𝑢 by their similarity scores and discard those with the
lowest alignment. The model then updates its parameters Θ using
the remaining interactions, ensuring that training is guided by
interactions consistent with the user’s original preference signals.

3.3 Model Optimization
After obtaining the comprehensive augmented interactions (cid:101)V𝑢
from TIA and CSA, we use them to train a new recommender
model 𝑓Θ. The goal is to address the cold-start challenge by lever-
aging high-quality augmented data to learn accurate and expres-
sive user/item representations, thereby enhancing recommendation
performance. To better capture the underlying relationships from
limited interactions, we adopt Bayesian Personalized Ranking (BPR)
as the training objective via:

L𝑟𝑒𝑐 (𝑢, 𝑣 +, 𝑣 −) = − log(𝜎 ( ˆ𝑦𝑢,𝑣+ − ˆ𝑦𝑢,𝑣− )),
(17)
where each training triplet (𝑢, 𝑣 +, 𝑣 −) is sampled from the union
of the user’s historical and augmented interactions, i.e., V𝑢 ∪ (cid:101)V𝑢.
The predicted scores ˆ𝑦𝑢,𝑣+ and ˆ𝑦𝑢,𝑣− are generated by 𝑓Θ.

The entire model adopts a bi-level optimization end-to-end train-
ing strategy, where the training parameters include the parameters
𝜃𝐴𝐸 of the MetaMAE and the parameters Θ of the downstream rec-
ommender model. The objective is shown in Eq. (13). Similar to the
training approach in meta-learning, the model training primarily
consists of inner-loop optimization and outer-loop optimization.
Inner-Loop Optimization. The primary goal of this optimiza-
tion is to obtain the user-specific personalized autoencoder 𝜃𝑢,∗
𝐴𝐸 for
user 𝑢 through rapid gradient descent, thereby obtaining a com-
prehensive and accurate representation 𝒇 𝑢 as shown in Eq. (11).
Then, we can generate augmented interactions V𝑐
𝑢 that primarily
contain collaborative signals supplemented by textual signals, as
shown in Eq. (12). As advised by [19], we use one gradient descent
to approximate the final optimized result via:
𝜃𝑢,∗
𝐴𝐸 ≈ 𝜃𝐴𝐸 − 𝜔1∇𝜃𝐴𝐸 L𝑢
𝑓 𝑟 ,

(18)

where 𝜔1 is the learning rate of inner-loop optimization.
Outer-Loop Optimization. The optimization objective of this
optimization, as shown in Eq. (13), remains to enhance the final
recommendation performance of recommender system 𝑓Θ. Addi-
tionally, to fully utilize the augmented data obtained from textual
information and collaborative signals, we adaptively filter out aug-
mented interactions that do not match the model with the help of
the training signals. This approach helps the model learn more accu-
rate user/item representations without altering the user’s original

---

<!-- PAGE 6 -->

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

Yantong Du, Rui Chen, Xiangyu Zhao, Qilong Han, and A. K. Qin

intent. Ultimately, we update the parameters 𝜃𝐴𝐸 of the MetaMAE
and the parameters Θ of the downstream recommender model via:

𝜃𝐴𝐸 = 𝜃𝐴𝐸 − 𝜔2

∑︁

𝑢 ∈ U

∇𝜃𝐴𝐸 L (V𝑢, (cid:101)V𝑡

𝑢 , (cid:101)V𝑐

𝑢 (𝜃𝑢,∗

𝐴𝐸 )),

Θ = Θ − 𝜔3

∑︁

∇ΘL (V𝑢 ),

(19)

𝑢 ∈ U
where 𝜔2, 𝜔3 are the learning rates of outer-loop optimization. It
is worth mentioning that we focus on updating the meta-model
parameters 𝜃𝐴𝐸 rather than the user-specific personalized autoen-
coder 𝜃𝑢,∗

𝐴𝐸 obtained in the inner-loop optimization.

4 Experiments
In this section, we conduct experiments to answer the following
research questions (RQs):
• RQ1: How does our PAnDA perform in the cold-start scenario

compared to the current state-of-the-art baselines?

• RQ2: What is the impact of critical components on the perfor-

mance?

• RQ3: How do different LLMs impact PAnDA?
• RQ4: How sensitive is the model to different parameters?
• RQ5: How does the model augmented sample differ from other

samples?

4.1 Experimental Setup
4.1.1 Datasets. We evaluate PAnDA on three widely used real-
world benchmark datasets: (1) MovieLens (ML-1M)1, (2) Netflix2,
(3) Book-Crossing3.

Following prior works [13, 14, 18], we simulate cold-start sce-
narios by retaining only users with no more than 100 interactions.
Each dataset is split into training, validation, and test sets with a
ratio of 8:1:1. Dataset statistics are summarized in Table 1.

4.1.2 Evaluation Metrics. We assess model performance using:
(1) Recall@K (R@K), (2) Normalized Discounted Cumulative Gain
(N@K), and (3) Precision@K (P@K). To mitigate test sampling bias,
we adopt the all-ranking evaluation strategy [31]. Results are av-
eraged over five independent runs, with 𝐾 set to 10, 20, and 50.
Statistical significance is assessed via 𝑝-values computed against
the best-performing baseline.

4.1.3 Competing models. To demonstrate the effectiveness of PAnDA,
we compare our model with: (i) CF-based methods including BPR [21],
LightGCN [6] and NGCF [28]. (ii) Augmentation-based methods
including DropoutNet [24], CL4SRec [36], L2Aug [25], KAR [34]
and LLMRec [30]. (iii) Cold-start methods including M2EU [33]
and TDAS [42].

Implementation details. We fix the embedding size of each
4.1.4
profile feature (e.g., age, gender) to 32 and set the training batch
size to 2048 for both datasets. Embedding parameters are initial-
ized using a Gaussian distribution [23]. We apply early stopping
when N@50 does not improve for more than 10 consecutive it-
erations, selecting the best-performing model during training as
the final one. For all baseline models, hyperparameters are either

set according to their original papers or carefully tuned on the
validation set, with the best results reported. We choose the temper-
ature 𝛾 from 0, 0.6, 0.8, 1, and initialize the aggregation parameter
𝛼 to 0.01. The learning rates 𝜔1, 𝜔2, 𝜔3 are searched in the ranges
[5e−5, 1e−3], [1e−4, 8e−4], and [1e−4, 8e−4], respectively. We set the
number of candidate items to 20 for all datasets. Each user receives
5 augmented positive and 5 negative samples, and 3 item pairs
are filtered out using a downstream-model-aware strategy. The
LLM used in PAnDA (Table 2) is GPT-4o4, while KAR and LLMRec
use LLaMA3-8B-Chat5 due to cost considerations. We also report
PAnDA’s performance with LLaMA3-8B-Chat for comparison. Our
implementation is based on PyTorch 2.0.0 and Python 3.11.1, with
the RecBole library [41]. Experiments are run on a workstation
with an Intel Xeon Platinum 2.40GHz CPU, NVIDIA Quadro RTX
8000 GPU, and 754GB RAM.

4.2 Overall Performance Comparison (RQ1)
We report the main experimental results in Table 2. From the results,
we can draw the following conclusions:

First, our model, PAnDA, consistently outperforms all other
baseline models, indicating its robustness and effectiveness in ad-
dressing the cold-start. This superiority is achieved by incorpo-
rating a high-quality data augmentation strategy that generates
comprehensive augmented data and adaptively selects high-quality
augmented samples based on model training signals. This adaptive
approach ensures that the model benefits from the most relevant
and informative data, leading to significant performance gains.

Second, PAnDA demonstrates substantial improvements over
traditional cold-start recommender models such as DropoutNet and
state-of-the-art MAML-based methods. This result underscores the
importance of leveraging textual signals in cold-start scenarios, as
these signals provide crucial contextual information that needs to be
included in sparse user-item interaction data. Moreover, the results
highlight that data augmentation, particularly when combined with
adaptive selection mechanisms, offers a promising and practical
direction for overcoming the limitations of cold-start scenarios.

At last, PAnDA also demonstrates substantial improvements
over traditional cold-start recommendation methods, such as Dropout-
Net, and state-of-the-art MAML-based methods, such as TDAS
and M2EU. These textual signals provide essential contextual in-
formation that complements collaborative signals, particularly in
cold-start scenarios where interaction data is limited. Furthermore,
the results highlight the critical role of adaptive data selection
mechanisms. By dynamically filtering and selecting the most rel-
evant augmented samples, PAnDA ensures that the model learns
from preference-aligned, contextually aligned data, setting a new
benchmark for addressing cold-start challenges in recommendation
systems. In summary, the experimental results validate the effective-
ness of PAnDA in overcoming the limitations of existing cold-start
recommendation methods. By integrating textual and collaborative
signals into a unified augmentation framework and employing an
adaptive filtering strategy, PAnDA delivers state-of-the-art perfor-
mance across multiple datasets and metrics, establishing a robust
and scalable solution for cold-start scenarios.

1https://movielens.org/
2https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data
3http://www2.informatik.uni-freiburg.de/~cziegler/BX/

4https://platform.openai.com/
5https://llama.meta.com/

---

<!-- PAGE 7 -->

PAnDA: Combating Negative Augmentation via Large Language Models for User Cold-Start Recommendations

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

Table 1: Statistics of the experimental datasets

Statistics

ML-1M

Netflix

Book-Crossing

#User
#Item
#Interaction
Sparsity
Avg. #interactions per user
user profiles

3,132
3,354
156,507
98.5101%
49.9862
age, gender, occupation, zip_code

245,281
17,761
10,627,773
99.7560%
43.3291
age, gender, occupation, zip_code

item profiles

movie_title, release_year, class

movie_title, release_year, class

Range of ratings

1∼5

1∼5

103,459
189,284
493,175
99.9975%
4.7669
location, age
book_title, book_author, publi-
cation_year, publisher, genre
1∼10

Table 2: The experimental comparison between PAnDA and the SOTA cold-start methods on the two benchmark datasets. The
best results are marked in bold, and the second-best results are underlined. All improvements are significant under a two-sided
t-test with 𝑝 < 0.05 over the best baselines.

Datasets Metrics

CF-based methods

Augmentation-based Methods

Cold-start Methods

BPR

LightGCN NGCF DropoutNet CL4SRec

L2Aug

KAR
(LLM-based)

LLMRec
(LLM-based)

TDAS

M2EU

PAnDA Improv.

ML-1M

R@10

0.2049

0.2081

0.18

N@10

0.1708

0.1727

0.1505

R@20

0.3015

0.3082

0.2717

N@20

0.2099

0.2127

0.187

R@50

0.4707

0.4752

0.4331

N@50

0.2638

0.266

0.2376

R@10

0.015

0.0158

0.0088

N@10

0.0082

0.0091

0.0066

Book
-Crossing

R@20

0.0243

0.0259

0.0159

N@20

0.0107

0.0118

0.0079

R@50

0.0419

0.0466

0.0256

N@50

0.0144

0.0162

0.0091

R@10

0.045

0.0458

0.0388

N@10

0.0382

0.0391

0.0352

R@20

0.0543

0.0559

0.0414

N@20

0.0407

0.0418

0.0366

R@50

0.0719

0.0766

0.0556

N@50

0.0444

0.0462

0.0391

Netflix

0.2719

0.2584

0.3689

0.2912

0.5165

0.3284

0.0164

0.0092

0.0268

0.0121

0.0471

0.0171

0.0464

0.0392

0.0568

0.0421

0.0771

0.0471

0.1478

0.2641

0.0767

0.1343

0.1837

0.3804

0.0873

0.1634

0.2845

0.5506

0.1204

0.1972

0.0115

0.0202

0.0059

0.0098

0.0154

0.0324

0.0072

0.0143

0.0292

0.0564

0.0103

0.0203

0.0207

0.0497

0.0115

0.0213

0.0326

0.0634

0.0143

0.0272

0.0482

0.0861

0.0176

0.0314

0.5084

0.5148

0.5933

0.5367

0.7415

0.6067

0.0229

0.0101

0.0331

0.0150

0.0607

0.0263

0.0529

0.0415

0.0639

0.0394

0.0906

0.0523

0.5106

0.4845

0.6184

0.5087

0.7612

0.5536

0.0229

0.0115

0.0349

0.0157

0.0631

0.0278

0.0529

0.0415

0.0649

0.0457

0.0931

0.0578

0.4591

0.4266

0.5315

0.4598

0.6847

0.2964

0.0281

0.0151

0.0382

0.0191

0.0701

0.0324

0.0482

0.0397

0.0581

0.0424

0.0781

0.0484

0.4813

0.4548

0.5798

0.4757

0.7214

0.5249

0.0197

0.0104

0.0307

0.0144

0.0568

0.0204

0.0497

0.0404

0.0607

0.0444

0.0868

0.0504

0.5891

15.37%

0.5643

16.47%

0.6997

13.15%

0.6017

18.28%

0.8516

11.88%

0.6644

20.01%

0.0315

37.55%

0.0161

40.00%

0.0486

39.26%

0.0233

48.41%

0.0811

28.53%

0.0351

26.26%

0.0615

16.26%

0.0461

11.08%

0.0786

21.11%

0.0533

16.63%

0.1111

19.33%

0.0651

12.63%

Table 3: Ablation study on ML-1M. LLMRec emerges as the
second-best performing baseline overall.

Variants

N@10

R@20

N@20

R@50

N@50

LLMRec

0.4845

0.6184

0.5087

0.7612

0.5536

w/o TIA

0.4415

0.5626

0.4703

0.7056

0.5184

w/o CSA 0.5007

0.6176

0.5174

0.7749

0.5689

w/o DFS

0.4688

0.5991

0.4954

0.7167

0.5411

PAnDA

0.5643

0.6997

0.6017

0.8516

0.6644

4.3 Ablation Study (RQ2)
We conducted a series of ablation experiments on ML-1M to in-
vestigate the contribution of components applied within PAnDA,
as shown in Table 3. w/o TIA: The removal of TIA leads to a sub-
stantial drop in performance across all metrics. This is primarily
because, without integrating textual signals, the augmented samples
generated lack sufficient contextual richness, thereby increasing
the prevalence of false positive samples. These results underscore
the importance of textual information in enhancing the model’s
understanding of user preferences. The ability of LLMs to process
and integrate these textual signals plays a pivotal role in improving
the overall quality of the augmented data. w/o CSA: The exclu-
sion of CSA also results in noticeable performance degradation.

---

<!-- PAGE 8 -->

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

Yantong Du, Rui Chen, Xiangyu Zhao, Qilong Han, and A. K. Qin

Table 4: Ablation study on ML-1M. Impact of different LLMs
on accuracy, cost, and latency

LLMs

R@20

N@20

Cost

Latency

LLama2-7B-chat
LLama3-8B-chat
gpt-3.5-turbo
gpt-4o-mini
gpt-4o

0.6178
0.6813
0.6345
0.6807
0.6997

0.4981
0.5847
0.5381
0.5833
0.6017

-
-
$24.2
$2.4
$40.3

33s
1.5s
27s
13s
18s

Table 5: Analysis of |C| on ML-1M and Book-Crossing.

|C|

3
10
20
30

R@20
0.6514
0.6866
0.6997
0.6915

ML-1M

N@20
0.5814
0.5948
0.6017
0.6003

Book-Crossing

P@20
0.1849
0.1906
0.1987
0.1954

R@20
0.0407
0.0467
0.0486
0.0479

N@20
0.0204
0.0228
0.0233
0.0231

P@20
0.0048
0.0051
0.0053
0.0052

Without CSA, the model relies solely on LLM-generated augmen-
tations, which often produce partially aligned samples that fail
to capture user preferences. This incomplete alignment hampers
the downstream recommender model’s ability to accurately and
comprehensively learn user/item representations, highlighting col-
laborative signals’ crucial role in ensuring the augmented data’s
robustness and accuracy. w/o DFS: The absence of downstream-
model training feedback signals leads to a decline in performance,
as it hinders the model’s ability to filter out samples mismatched
with the model’s current training trajectory. Without this prun-
ing, the model struggles to adapt to the diverse set of augmented
samples, resulting in less consistent user/item representations and
ultimately leading to suboptimal recommendation performance.
This emphasizes the necessity of integrating feedback signals to
maintain the relevance and quality of the training data.

4.4 LLMs Analysis (RQ3)
Table 4 presents the results of the ablation study analyzing the
impact of different LLMs as textual information augmentors on
PAnDA. We include both open-source models (LLaMA series) and
closed-source models (ChatGPT series), and compare their effects
on accuracy, cost, and latency. The results show that the choice
of LLM has a substantial influence on performance: stronger mod-
els such as GPT-4o achieve the best Recall@20 and NDCG@20,
while LLaMA3-8B-chat also delivers competitive accuracy at negli-
gible cost and extremely low latency when deployed on optimized
hardware. This indicates a clear correlation between model scale
and performance, with larger and more advanced LLMs providing
more accurate recommendations. Overall, the findings demonstrate
that employing higher-capacity LLMs can significantly improve
PAnDA, highlighting the importance of carefully selecting models
that balance accuracy gains with efficiency and cost considerations.

4.5 Hyperparameter Analysis (RQ4)
Analysis of |C|. Since the input token constraints of the LLMs,
coupled with the problem of false positive augmented samples, we
use the candidate item set C to limit the candidate items based on
the LLMs augmented samples. Due to cost constraints, we explored

Figure 4: Performance comparison (Recall@20 and
NDCG@20) with varying numbers of augmented data pairs.

Figure 5: Performance comparison (Recall@20 and
NDCG@20) with discard augmented data pairs.
{3, 10, 20, 30}, and Table 5 shows that |C| = 20 gives the best re-
sults. Smaller values limit the choices, while larger values make the
recommendation more difficult.
Analysis of the #.augmented data pairs. We can observe from
Figure 4 that the impact of the number of augmented sample pairs
varies across different datasets. Unlike ML-1M, the Book-Crossing
dataset is sparse, making it difficult to generate comprehensive and
accurate augmented samples. As a result, the model is more sensi-
tive to the number of augmented samples. This also indicates that
the quality of generated augmented samples is critically important.
Analysis of the #.discard augmented data pairs. We can observe
from Figure 5 that there are model mismatched augmented samples.
The model’s performance improves by discarding these samples
based on the model’s training signals. However, excessive discard-
ing may lead to the loss of highly informative and high-quality
augmented data, harming the model’s performance.
Analysis of the #.similar user. We can observe from Figure 6
that although the introduction of similar users can improve LLM’s
ability to understand user preferences, over-information brings
performance degradation because there is too much textual infor-
mation, and it is difficult for LLM to focus on the key information.

4.6 Case Study (RQ5)
As shown in Figure 7, the differences in augmented data generated
by various methods for cold-start tasks are evident. The left side
shows the ground truth user interaction data and the right side
displays the augmented data distribution. We assess the quality of
augmented samples using the maximum cosine similarity, denoted
as 𝑞, between each augmented sample’s embedding and the ground
truth samples. This metric indicates the quality of the augmented
samples. Traditional methods like L2Aug struggle with accurately
capturing user preferences, leading to many false-positive samples
(𝑞 ≤ 0.25), which negatively impact model learning. LLM-based

---

<!-- PAGE 9 -->

PAnDA: Combating Negative Augmentation via Large Language Models for User Cold-Start Recommendations

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

Large Language Models (LLMs) for Recommendation. LLMs
have garnered attention in recommender systems, with various ef-
forts made to model user behavior with LLMs [10, 20, 29]. LLMs
have been employed as inference models in various recommenda-
tion tasks, such as rating prediction, sequential recommendation,
and direct recommendation. Recent work has further explored their
potential in addressing cold-start challenges, such as leveraging
language-model priors to overcome item cold-start [26], and using
keyword-driven retrieval-augmented LLMs to alleviate user cold-
start issues [12]. However, most previous approaches primarily uti-
lized LLMs as recommenders [3], focusing on their text-processing
capabilities while overlooking the collaborative signals that tradi-
tional recommender systems excel at capturing. In this paper, we
combine LLM-based data augmentation [30, 43] with traditional
data augmentation methods based on collaborative signals, combin-
ing both at two levels to achieve preference-aligned augmentation
and improve the performance of downstream recommender models.
Data Augmentation for Recommendation. Data augmen-
tation has been a long-standing research focus in recommender
systems. Common augmentation operations include permutation,
deletion, swapping, insertion, and duplication [17], as well as more
recent strategies such as counterfactual reasoning [39] and con-
trastive learning [27]. Despite these efforts, the quality of aug-
mented data remains an open problem, particularly in sparse or
cold-start settings. In this work, we revisit insertion and deletion
operations from the perspective of user preference alignment and
propose PAnDA tailored for the cold-start scenario.

6 Conclusion
In this paper, we addressed user cold-start recommendation via
data augmentation. We analyzed limitations of existing LLM-based
methods and identified two key properties of high-quality augmen-
tation: preference alignment and downstream-model awareness.
Based on this, we proposed PAnDA, a novel LLM-powered frame-
work that iteratively integrates textual and collaborative signals at
both interaction and representation levels, while adaptively filter-
ing inconsistent samples during training. Extensive experiments
on three real-world datasets confirmed the benefits of generating
preference-aligned and downstream-model-aware augmented data
for recommendation tasks. For future work, we plan to enhance
scalability and efficiency of the bi-level optimization and conduct
more rigorous validations of alignment with true user preferences.

Figure 6: Analysis of the #similar users on ML-1M and Book-
Crossing.

Figure 7: Case study on augmentation samples by different
augmentors.

methods (LLMRec) use world knowledge to generate preference-
aligned samples but still produce partially aligned and false-positive
samples, showing the limitations of relying solely on textual infor-
mation. In contrast, PAnDA generates augmented data that closely
aligns with valid user preferences, effectively capturing accurate
preferences and eliminating false-positive and partially aligned sam-
ples. By combining textual augmentation, collaborative signals, and
a downstream-model-aware filtering strategy, PAnDA addresses
data sparsity and quality issues in cold-start scenarios, providing
high-quality, preference-aligned augmented samples.

5 Related Work
Cold-start Recommendation. To address this issue, many works
use auxiliary information to improve cold-start user or item repre-
sentations, such as social networks [16] or cross-domain data [4].
Graph Neural Networks (GNNs) further capture high-order seman-
tics from knowledge graphs [5] and heterogeneous networks [37].
When side information is limited, contrastive learning [27] helps
refine collaborative embeddings. More recently, meta-learning [5,
33, 42] has emerged as a dominant solution. Our method instead
leverages LLMs to generate contextually relevant samples while re-
taining collaborative signals, allowing PAnDA to handle cold-start
more robustly without complex auxiliary data or graph structures.

Acknowledgments
This work was supported by the Heilongjiang Key R&D Program
of China under Grant No.GA23A915, Australian Research Coun-
cil (ARC) under Grant No. DP200102611, Hong Kong Research
Grants Council’s Research Impact Fund (No.R1015-23), Collabo-
rative Research Fund (No.C1043-24GF), General Research Fund
(No.11218325), Institute of Digital Medicine of City University of
Hong Kong (No.9229503), Huawei (Huawei Innovation Research
Program), Tencent (CCF-Tencent Open Fund, Tencent Rhino-Bird
Focused Research Program), Alibaba (CCF-Alimama Tech Kanga-
roo Fund No. 2024002), Ant Group (CCF-Ant Research Fund), Didi
(CCF-Didi Gaia Scholars Research Fund), Kuaishou, and Bytedance.

---

<!-- PAGE 10 -->

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

Yantong Du, Rui Chen, Xiangyu Zhao, Qilong Han, and A. K. Qin

7 GenAI Disclosure Statement
GenAI tools were actively used as part of the research methodology
in this work. Specifically, LLMs were employed to generate aug-
mented training samples for cold-start users within the proposed
PAnDA framework. These augmented interactions were integrated
into the data augmentation pipeline under the authors’ full supervi-
sion. In addition, LLMs were also used to assist with minor editing
and wording improvements in the manuscript. All AI-generated
content was carefully reviewed and validated by the authors to
ensure accuracy, relevance, and alignment with the research goals.

References
[1] Sungyong Baik, Janghoon Choi, Heewon Kim, Dohee Cho, Jaesik Min, and Ky-
oung Mu Lee. 2021. Meta-learning with task-adaptive loss function for few-shot
learning. In Proceedings of the IEEE/CVF international conference on computer
vision. IEEE, 9465–9474.

[2] Yuwei Cao, Liangwei Yang, Chen Wang, Zhiwei Liu, Hao Peng, Chenyu You,
and Philip S Yu. 2023. Multi-task item-attribute graph pre-training for strict
cold-start item recommendation. In Proceedings of the 17th ACM Conference on
Recommender Systems. 322–333.

[3] Zhikai Chen, Haitao Mao, Hang Li, Wei Jin, Hongzhi Wen, Xiaochi Wei,
Shuaiqiang Wang, Dawei Yin, Wenqi Fan, Hui Liu, et al. 2024. Exploring the
potential of large language models (llms) in learning on graphs. ACM SIGKDD
Explorations Newsletter 25, 2 (2024), 42–61.

[4] Wenjing Fu, Zhaohui Peng, Senzhang Wang, Yang Xu, and Jin Li. 2019. Deeply
fusing reviews and contents for cold start users in cross-domain recommendation
systems. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 33.
AAAI Press, Palo Alto, California, USA, 94–101.

[5] Di Han, Xiaotian Jing, Yijun Chen, Junmin Liu, Kai Liao, and Wenting Li. 2025.
Cold-start recommendation based on knowledge graph and meta-learning under
positive and negative sampling. ACM Transactions on Recommender Systems 3, 3
(2025), 1–24.

[6] Xiangnan He, Kuan Deng, Xiang Wang, Yan Li, Yongdong Zhang, and Meng
Wang. 2020. Lightgcn: Simplifying and powering graph convolution network for
recommendation. In Proceedings of the 43rd International ACM SIGIR Conference
on Research and Development in Information Retrieval. ACM, New York, NY, USA,
639–648.

[7] Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie, Xia Hu, and Tat-Seng
Chua. 2017. Neural collaborative filtering. In Proceedings of the 26th International
Conference on World Wide Web. International World Wide Web Conferences
Steering Committee, Geneva, Switzerland, 173–182.

[8] Nicole Immorlica, Meena Jagadeesan, and Brendan Lucier. 2024. Clickbait vs.
quality: How engagement-based optimization shapes the content landscape in
online platforms. In Proceedings of the ACM Web Conference 2024. 36–45.

[9] Yangqin Jiang, Lianghao Xia, Wei Wei, Da Luo, Kangyi Lin, and Chao Huang.
2024. Diffmm: Multi-modal diffusion model for recommendation. In Proceedings
of the 32nd ACM International Conference on Multimedia (ACM MM). ACM, New
York, NY, USA, 7591–7599.

[10] Wang-Cheng Kang, Jianmo Ni, Nikhil Mehta, Maheswaran Sathiamoorthy,
Lichan Hong, Ed Chi, and Derek Zhiyuan Cheng. 2023. Do LLMs Understand
User Preferences? Evaluating LLMs on User Rating Prediction. arXiv preprint
arXiv:2305.06474 (2023).

[11] Mikhail Khodak, Maria-Florina F Balcan, and Ameet S Talwalkar. 2019. Adaptive
gradient-based meta-learning methods. Advances in Neural Information Processing
Systems 32 (2019).

[12] Hai-Dang Kieu, Minh-Duc Nguyen, Thanh-Son Nguyen, and Dung D Le. 2025.
Keyword-driven retrieval-augmented large language models for cold-start user
recommendations. In Companion Proceedings of the ACM on Web Conference 2025.
2717–2721.

[13] Hoyeop Lee, Jinbae Im, Seongwon Jang, Hyunsouk Cho, and Sehee Chung. 2019.
Melu: Meta-learned user preference estimator for cold-start recommendation. In
Proceedings of the 25th ACM SIGKDD. 1073–1082.

[14] Xixun Lin, Jia Wu, Chuan Zhou, Shirui Pan, Yanan Cao, and Bin Wang. 2021.
Task-adaptive neural process for user cold-start recommendation. In Proceedings
of the Web Conference 2021. 1306–1316.

[15] Huafeng Liu, Jingxuan Wen, Liping Jing, and Jian Yu. 2019. Deep generative rank-
ing for personalized recommendation. In Proceedings of the 13th ACM Conference
on Recommender Systems. 34–42.

[16] Siwei Liu, Xi Wang, Craig Macdonald, and Iadh Ounis. 2024. A Social-aware
Gaussian Pre-trained model for effective cold-start recommendation. Information
Processing & Management 61, 2 (2024), 103601.

[17] Zhiwei Liu, Ziwei Fan, Yu Wang, and Philip S Yu. 2021. Augmenting sequential
recommendation with pseudo-prior items via reversely pre-training transformer.

In Proceedings of the 44th international ACM SIGIR conference on Research and
development in information retrieval. 1608–1612.

[18] Yuanfu Lu, Yuan Fang, and Chuan Shi. 2020. Meta-learning on heterogeneous
information networks for cold-start recommendation. In Proceedings of the 26th
ACM SIGKDD international conference on knowledge discovery & data mining.
1563–1573.

[19] Alex Nichol, Joshua Achiam, and John Schulman. 2018. On first-order meta-

learning algorithms. arXiv preprint arXiv:1803.02999 (2018).

[20] Xubin Ren, Wei Wei, Lianghao Xia, Lixin Su, Suqi Cheng, Junfeng Wang, Dawei
Yin, and Chao Huang. 2024. Representation learning with large language models
for recommendation. In Proceedings of the ACM on Web Conference 2024. 3464–
3475.

[21] Steffen Rendle, Christoph Freudenthaler, Zeno Gantner, and Lars Schmidt-Thieme.
2012. BPR: Bayesian personalized ranking from implicit feedback. arXiv preprint
arXiv:1205.2618 (2012).

[22] Scott Sanner, Krisztian Balog, Filip Radlinski, Ben Wedin, and Lucas Dixon.
2023. Large language models are competitive near cold-start recommenders for
language-and item-based preferences. In Proceedings of the 17th ACM conference
on recommender systems. 890–896.

[23] Luke Vilnis and Andrew McCallum. 2014. Word representations via gaussian

embedding. arXiv preprint arXiv:1412.6623 (2014).

[24] Maksims Volkovs, Guangwei Yu, and Tomi Poutanen. 2017. Dropoutnet: Ad-
dressing cold start in recommender systems. Advances in neural information
processing systems 30 (2017).

[25] Jianling Wang, Ya Le, Bo Chang, Yuyan Wang, Ed H Chi, and Minmin Chen. 2022.
Learning to augment for casual user recommendation. In Proceedings of the ACM
Web Conference 2022. 2183–2194.

[26] Shiyu Wang, Hao Ding, Yupeng Gu, Sergul Aydore, Kousha Kalantari, and
Branislav Kveton. 2024. Language-model prior overcomes cold-start items. arXiv
preprint arXiv:2411.09065 (2024).

[27] Wenbo Wang, Bingquan Liu, Lili Shan, Chengjie Sun, Ben Chen, and Jian Guan.
2024. Preference Aware Dual Contrastive Learning for Item Cold-Start Recom-
mendation. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38.
9125–9132.

[28] Xiang Wang, Xiangnan He, Meng Wang, Fuli Feng, and Tat-Seng Chua. 2019.
Neural graph collaborative filtering. In Proceedings of the 42nd international ACM
SIGIR conference on Research and development in Information Retrieval. 165–174.
[29] Xiaolei Wang, Xinyu Tang, Wayne Xin Zhao, Jingyuan Wang, and Ji-Rong Wen.
2023. Rethinking the evaluation for conversational recommendation in the era
of large language models. arXiv preprint arXiv:2305.13112 (2023).

[30] Wei Wei, Xubin Ren, Jiabin Tang, Qinyong Wang, Lixin Su, Suqi Cheng, Jun-
feng Wang, Dawei Yin, and Chao Huang. 2024. Llmrec: Large language models
with graph augmentation for recommendation. In Proceedings of the 17th ACM
International Conference on Web Search and Data Mining. 806–815.

[31] Yinwei Wei, Xiang Wang, Xiangnan He, Liqiang Nie, Yong Rui, and Tat-Seng Chua.
2021. Hierarchical user intent graph network for multimedia recommendation.
IEEE Transactions on Multimedia 24 (2021), 2701–2712.

[32] Xuansheng Wu, Huachi Zhou, Yucheng Shi, Wenlin Yao, Xiao Huang, and Ning-
hao Liu. 2024. Could Small Language Models Serve as Recommenders? Towards
Data-centric Cold-start Recommendation. In Proceedings of the ACM on Web
Conference 2024. 3566–3575.

[33] Zhenchao Wu and Xiao Zhou. 2023. M2eu: Meta learning for cold-start recom-
mendation via enhancing user preference estimation. In Proceedings of the 46th
International ACM SIGIR. 1158–1167.

[34] Yunjia Xi, Weiwen Liu, Jianghao Lin, Xiaoling Cai, Hong Zhu, Jieming Zhu, Bo
Chen, Ruiming Tang, Weinan Zhang, and Yong Yu. 2024. Towards open-world
recommendation with knowledge augmentation from large language models. In
Proceedings of the 18th ACM Conference on Recommender Systems. 12–22.
[35] Changrong Xiao, Sean Xin Xu, Kunpeng Zhang, Yufang Wang, and Lei Xia. 2023.
Evaluating reading comprehension exercises generated by LLMs: A showcase
of ChatGPT in education applications. In Proceedings of the 18th Workshop on
Innovative Use of NLP for Building Educational Applications (BEA 2023). 610–625.
[36] Xu Xie, Fei Sun, Zhaoyang Liu, Shiwen Wu, Jinyang Gao, Jiandong Zhang, Bolin
Ding, and Bin Cui. 2022. Contrastive learning for sequential recommendation. In
2022 IEEE 38th international conference on data engineering (ICDE). IEEE, 1259–
1273.

[37] Guangping Zhang, Dongsheng Li, Hansu Gu, Tun Lu, and Ning Gu. 2024. Het-
erogeneous Graph Neural Network with Personalized and Adaptive Diversity
for News Recommendation. ACM Transactions on the Web 18, 3 (2024), 1–33.
[38] Lingzi Zhang, Xin Zhou, Zhiwei Zeng, and Zhiqi Shen. 2024. Multimodal Pre-
training for Sequential Recommendation via Contrastive Learning. ACM Trans-
actions on Recommender Systems 3, 1 (2024), 1–23.

[39] Shengyu Zhang, Dong Yao, Zhou Zhao, Tat-Seng Chua, and Fei Wu. 2021.
Causerec: Counterfactual user sequence synthesis for sequential recommen-
dation. In Proceedings of the 44th International ACM SIGIR Conference on Research
and Development in Information Retrieval. 367–377.

[40] Yan Zhang, Changyu Li, Ivor W Tsang, Hui Xu, Lixin Duan, Hongzhi Yin, Wen
Li, and Jie Shao. 2022. Diverse preference augmentation with multiple domains

---

<!-- PAGE 11 -->

PAnDA: Combating Negative Augmentation via Large Language Models for User Cold-Start Recommendations

CIKM ’25, November 10–14, 2025, Seoul, Republic of Korea

for cold-start recommendations. In 2022 IEEE 38th International Conference on
Data Engineering (ICDE). IEEE, 2942–2955.

[41] Wayne Xin Zhao, Shanlei Mu, Yupeng Hou, Zihan Lin, Kaiyuan Li, Yushuo Chen,
YujieF Lu, Hui Wang, Changxin Tian, Xingyu Pan, Yingqian Min, Zhichao Feng,
Xinyan Fan, Xu Chen, Pengfei Wang, Wendi Ji, Yaliang Li, Xiaoling Wang, and
Ji-Rong Wen. 2021. Recbole: Towards a unified, comprehensive and efficient
framework for recommendation algorithms. In CIKM.

[42] Xuhao Zhao, Yanmin Zhu, Chunyang Wang, Mengyuan Jing, Jiadi Yu, and Feilong
Tang. 2023. Task-difficulty-aware meta-learning with adaptive update strategies
for user cold-start recommendation. In Proceedings of the 32nd ACM International
Conference on Information and Knowledge Management. 3484–3493.

[43] Zhi Zheng, Wenshuo Chao, Zhaopeng Qiu, Hengshu Zhu, and Hui Xiong. 2024.
Harnessing large language models for text-rich sequential recommendation. In
Proceedings of the ACM on Web Conference 2024. 3207–3216.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

PAnDA: Combating Negative Augmentation via Large Language
Models for User Cold-Start Recommendations
YantongDu RuiChen* XiangyuZhao*
HarbinEngineeringUniversity HarbinEngineeringUniversity CityUniversityofHongKong
Harbin,China Harbin,China HongKong,China
duyantong94@hrbeu.edu.cn ruichen@hrbeu.edu.cn xianzhao@cityu.edu.hk
QilongHan A.K.Qin
HarbinEngineeringUniversity SwinburneUniversityofTechnology
Harbin,China Hawthorn,Victoria3122,Australia
hanqilong@hrbeu.edu.cn kqin@swin.edu.au
Abstract Keywords
Thecold-startproblemremainsalong-standingchallengeinrec- Cold-startrecommendations;largelanguagemodels;dataaugmen-
ommender systems. Recent advances in large language models tation;meta-learning
(LLMs)haveopenednewavenuesforaddressingcold-startsce-
ACMReferenceFormat:
nariosthroughdataaugmentation.However,existingcold-start
YantongDu,RuiChen*,XiangyuZhao*,QilongHan,andA.K.Qin.2025.
augmentationmethodsoftensufferfromnegativeaugmentation,
PAnDA:CombatingNegativeAugmentationviaLargeLanguageModels
manifestingasincompleteaugmentation,wheregeneratedinterac-
forUserCold-StartRecommendations.InProceedingsofthe34thACMInter-
tionsfailtocomprehensivelyreflectuserpreferences,andinaccurate nationalConferenceonInformationandKnowledgeManagement(CIKM’25),
augmentation,wheretheyconflictwithuserintent.Theseissues November10–14,2025,Seoul,RepublicofKorea.ACM,NewYork,NY,USA,
largelystemfromtwolimitations:(1)theinabilitytoeffectively 11pages.https://doi.org/10.1145/3746252.3761080
incorporatecollaborativesignals,whicharecriticalforpreference
alignment,and(2)thelackofawarenessofthedownstreammodel’s 1 Introduction
learningdynamicsduringdataaugmentation.Tothebestofour
Recommender systems have played a crucial role in mitigating
knowledge,thelatterhasnotbeenstudiedintheliterature.
informationoverloadinawiderangeofreal-worldapplicationsby
Consequently,weproposeanovelframeworknamedPAnDA.
efficientlyprovidingonlineuserswithrelevantcontent.Existing
Toaddresstheincompleteaugmentationissue,weproposeamodel-
recommendationmodels,suchascollaborativefiltering[7]and
agnosticpreference-alignedaugmentationmoduletoiteratively
content-basedmethods[4,8],typicallyrecommendappropriate
extract and fuse textual information and collaborative informa-
itemstousersbylearninguser/itemrepresentationsfromtheir
tionbyuser-userpreferencematchinganduser-itempreference
historicalinteractions(e.g.,clicks,ratings,purchases).Itisnatural
coherence,whichtogetherformacontextualcuetoguidetheaug-
thatthisideawouldfailinscenarioswhereuser-iteminteractions
mentor to generate high-quality augmented data. To overcome
arelimited,whichisknownasthecold-start problem[2,32],a
theinaccurateaugmentationissue,weproposeamodel-specific
long-standingchallengeforrecommendersystems.
downstream-model-awareadaptationmoduletoadaptivelyalign
Anintuitivestrategytoaddressthecold-startproblemistogen-
theaugmenteddatawiththemodel’sstatesduringthetraining
erateadditionaluserinteractions(i.e.,dataaugmentation)toenrich
process,guidedbygradientsimilarity.Extensiveexperimentson
userbehaviorsandfurtherguidemodellearning.Thisallowsrec-
threepublicbenchmarkdatasetsdemonstratethatPAnDAoutper-
ommendationmodelstocapturemorediverseuserpreferences,as
formsdifferentgroupsofstate-of-the-artcold-startrecommenda-
illustratedinFig.1(a).Somestudieshaveexploredmulti-modal
tionmethodsinallscenarios.Thesourcecodeispubliclyavailable
augmentation,leveragingauxiliaryinformationsuchasimages[38],
athttps://github.com/YantongDU/PAnDA.
audio[9],andtext[30,38]tosimulateinteractionsthatbetterrepre-
sentusers’interests.Morerecently,theemergenceoflargelanguage
CCSConcepts
models(LLMs)hasopenedupnewopportunitiesfordataaugmen-
•Informationsystems→Personalization;Informationex-
tationinrecommendationtasks[22,30].Owingtotheirextensive
traction;•Computingmethodologies→Machinelearning.
worldknowledgeandstrongcapabilitiesinlanguagegenerationand
reasoning,LLMsareincreasinglyregardedaspromisingaugmenta-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
tiontoolsincold-startscenarios[35].Theycancomplementsparse
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation useroriteminformationandgeneratecontextuallyappropriateaug-
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe mentedinteractions.However,existingaugmentationmethodsstill
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
sufferfromsignificantlimitationsincold-startsettings.Duetothe
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. difficultyofmulti-modalalignmentandlimitedmodelgenerative
CIKM’25,Seoul,RepublicofKorea capabilities,thesemethodsstruggletoaccuratelycaptureuserpref-
©2025Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
erencesandcanresultinaugmentedinteractionsthatcontradict
ACMISBN979-8-4007-2040-6/2025/11
https://doi.org/10.1145/3746252.3761080 userintents,misleadmodellearning,anddegraderecommendation
3844

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
performance,callednegativeaugmentation,asshowninFig.1(b). User
Itcanbefurthercategorizedintotwocorechallenges.Fromthe
dataperspective,therelianceonmulti-modalinformationoften Item
resultsinincompleteaugmentation,asitfailstocomprehensively
Collaborative captureuserpreferences.Fromthemodelperspective,limitedgen- Data Augmentator signals
erativecapabilitycanleadtoinaccurateaugmentation,wherethe
augmentedinteractionsmisalignwithuserintents.
Toachievecompletedataaugmentation,recentmethodshave
attemptedtointegratecollaborativesignalswithmulti-modalin- User Collaborative signals
formation[9,31].However,effectivelyfusingtheseheterogeneous
Item
sourcesremainsanopenchallenge.Thischallengeisfurtherex-
acerbatedincold-startscenarios,wherelimitedinteractiondata
(a) Traditional data augmentation
makesitevenmoredifficulttobalancethecomplementarystrengths
ofcontentsemanticsandcollaborativepatterns.Asaresult,aug-
mentedinteractionsareoftenbiasedtowardasinglemodalityor
signaltype,failingtoprovideaholisticrepresentationofuserpref-
erencesandultimatelydegradingtheperformanceofdownstream
recommendationmodels.
Ontheotherhand,inaccurateaugmentationarisesfromthecapa-
bilitylimitationsofgenerativemodels.Forexample,clickbaittitles
ormismatchedimage-textpairs[8,31,40]mayguidethemodelto
augmentinteractionsthataresuperficiallyrelevantbutsemanti-
callyinconsistentwiththeuser’strueintent.Incorporatingsuch
inaccurateaugmentationintomodeltrainingindiscriminatelynot
onlyintroduceslabelnoisebutcanalsodistortlearnedpreference
distributionsandincreaseoverfittingrisks.Inextremecases,this
maycausethemodeltoover-personalizeorrecommendirrelevant
items,furtherdeterioratingtheuserexperience.Moreover,theaug-
menteddatawillbeconsumedbyadownstreamrecommendation
model.Differentmodelshavedisparatelearningcapabilitiesand
thusexpectdifferentextents/typesofdataaugmentation(e.g.,the
numberofaugmentedinteractionsneededforacold-startuser),
suggestingthatLLM-baseddataaugmentationneedstobeawareof
thedownstreammodel.Morespecifically,thedownstreammodel’s
trainingstatusneedstobeconsideredinthedataaugmentation
process.Therefore,mitigatinginaccuracywhileensuringcompat-
ibilitywiththedownstreamrecommendationmodelpresentsan
additionalchallengeforLLM-baseddataaugmentation.
Toaddressthesetwochallenges,weproposeanovelpreference-
alignedanddownstream-model-awaredataaugmentationframe-
workPAnDAinspiredbythepre-trainandfine-tuneparadigm[16,
17,38],whichconsistsoftwocomplementarymodules,asshownin
Fig.1(c).Amodel-agnosticpreference-alignedaugmentationmodule
likeapre-trainingstage,andamodel-specificdownstream-model-
awareadaptationmodulelikeafine-tuningstage.Specifically,to
mitigateincompleteaugmentation,wefocusongeneratingdiverse
andcomprehensiveuser-iteminteractions.Weperformtheuser-
userpreferencematchingbyfocusingonpreferencedifferences
betweenusersanddesigningauniqueprompttobeusedasacon-
textualcuetoassistLLMsingeneratingaugmentedinteractions.
Additionally,weleverageuser-itempreferencecoherencetofur-
thermodelcollaborativestructures,enablingmorepersonalised
andaccurateaugmentation.Thesetwocomponentsworkintandem
tointegratebothmulti-modalcontentandcollaborativesignals,
achievingmorecompletedataaugmentation.Toaddressinaccurate
augmentation,wefurtherintroduceamodel-specificadaptation
module. This component dynamically assesses the relevance of
Representations
User
Item
Representations
User Multi-modal data
Item
(b) Multi-modal data augmentation
Representations
Multi-modal data Similar user
Data Augmentator Guide i M nf u o l r t m i-m at o io d n a s l
Data Augmentator
Multi-modal fusion Guide
User Multi-modal Negative User informations
augmentation
Item Item
Ideal augmentation Incomplete augmentation Inaccurate augmentation Dynamic accuracy augmentation
(c) Our method
Figure1:Anillustrationofdifferentdataaugmentationmeth-
odsinthecold-startrecommendationscenario.
eachaugmentedsamplebymonitoringthelearningstateofthe
downstreamrecommender.Byselectivelyincorporatingordiscard-
ingaugmentedinteractions,itenhancesthealignmentbetweenthe
augmenteddataandthemodel’slearningobjectivesandprevents
noisyorharmfulsamplesfromdegradingperformance.
Tosummarize,themaincontributionsofourworkareasfollows:
• Wearethefirsttoidentifyandstudythenegativeaugmen-
tation in cold-start recommendation, highlighting that more
augmenteddatadoesnotnecessarilyleadtobetterperformance.
Werevealtwounderlyingchallenges:incompleteaugmentation
fromthedataperspectiveandinaccurateaugmentationfrom
themodelperspective,whichdegradetheeffectivenessofdata
augmentationmethods.
• Weintroduceanovelpreference-alignedanddownstream-model-
awaredataaugmentationframeworkPAnDApoweredbyLLMs.
Itconsistsofamodel-agnosticpreference-alignedaugmentation
moduleandamodel-specificdownstream-model-awareadapta-
tionmodule,whichtogethereffectivelyaddressthetwolimita-
tions.PAnDAalsofeaturesadecoupleddesigntoaccommodate
differentcombinationsofLLMsanddownstreamrecommenda-
tionmodels.
• Wehaveperformedextensiveexperimentsonthreereal-world
benchmarkdatasetsandshownthatPAnDA,beingbothpreference-
alignedanddownstream-model-aware,canconsistentlyoutper-
formdifferentgroupsofstate-of-the-artcold-startrecommenda-
tionmethodsinallscenarios.
2 Preliminary
In this section, we first introduce the problem formulation and
notations,followedbyageneraloverviewofdataaugmentationin
recommendersystems.
ProblemFormulation.LetUandVdenotethesetsofusersand
items,respectively.Theuser-iteminteractionmatrixisdefinedas
𝑨∈0,1|U|×|V|,where𝐴 𝑢𝑣 =1indicatesthatuser𝑢hasinteracted
withitem𝑣.Theinteractionhistoryofuser𝑢isdenotedbyV𝑢 =
𝑣
1
,𝑣
2
,...,𝑣 |V𝑢|.Collaborativefiltering(CF)methodslearnfrom𝑨
toobtainuseranditemID-basedembeddings 𝑬 = {𝑬𝑢 ,𝑬𝑣} for
prediction.However,suchmethodsstruggleincold-startsettings
whereuser/itemIDsareunseen.Toaddressthis,profile-basedCF
methodsincorporatesideinformationP ={P𝑈,P𝑉}forusersand
items,andlearnrepresentationsusingafunction 𝑓 Θ𝑟𝑒𝑐 basedon
3845

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
both𝑨andP.Themodelistrainedbymaximizingtheposterior:
|     | Θ   | ∗ =argmax𝑝(Θ | 𝑟𝑒𝑐|𝑨,P), |     |     |     |     |     |     | 𝑠 =𝑨𝑢 | ⊙𝑨𝑚 , |     | (5) |
| --- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- |
|     |     | 𝑟 𝑒𝑐         |           |     |     | (1) |     |     |     | 𝑢,𝑚   |       |     |     |
Θ𝑟𝑒𝑐
where⊙denoteselement-wisemultiplication.Weselectthetop-K
| w h e re 𝑓 Θ | w i l l ou | t p u t th e fi na | l u s er r | e pr es en ta | t io n 𝒉 𝑢 | c o n tain |     |     |     |     |     |     |     |
| ------------ | ---------- | ------------------ | ---------- | ------------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
𝑟 𝑒𝑐 similarusers𝑺𝑢asauxiliarycontextandcombineeachuser’sprofile
| bo t h co l la | b or at i v e | si g n a ls f ro m 𝑬 | a n d si | d e in fo rm | a t io n 𝑝 | v ia : |                                                            |     |     |     |     |     |     |
| -------------- | ------------- | -------------------- | -------- | ------------ | ---------- | ------ | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                |               |                      |          |              | 𝑢          |        | (e.g.,age,gender),interactionhistory,andcandidateitemset𝑪𝑢 |     |     |     |     |     | to  |
=𝑓 (𝑨,𝑝 𝑢). constructatextualpromptP 𝑢fortheLLM.TheLLMthengenerates
|     |     | 𝒉𝑢 Θ𝑟𝑒𝑐 |     |     |     | (2) |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anaugmentedinteractionpairforuser𝑢,consistingofapreferred
Theitem’sfinalrepresentation𝒉𝑣 canalsobeobtainedsimilarly. item𝑣 +,𝑡 andanon-preferreditem𝑣 −,𝑡
|     |     |     |     |     |     |     |     | 𝑢   |     |     | 𝑢 from𝑪𝑢 | via: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- |
DataaugmentationforRecommenderSystems.Incold-start
scenarios,thesparsityofinteractionsmotivatestheuseofdata
augmentation.Let𝑓 denotetheaugmentationfunction,which P =Text(𝑢,𝑺𝑢 ,𝑪𝑢 ,𝑨,P),
|     |     | Θ𝑎𝑢𝑔 |     |     |     |     |     |     |     | 𝑢   |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(6)
generatessyntheticinteractions𝑨(cid:101)from𝑨andPvia: {𝑣 +,𝑡,𝑣 −,𝑡}=LLM(P 𝑢),
|     |     |              |        |     |     |     |     |     | 𝑢 𝑢 |     |     |     |     |
| --- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 𝑨(cid:101)=𝑓 | (𝑨,P). |     |     | (3) |     |     |     |     |     |     |     |
Θ𝑎𝑢𝑔 whereText(·)denotesthepromptconstructionfunction.Thecan-
Thedownstreamrecommendermodel𝑓 didate set 𝑪𝑢 is obtained by hard sampling high-ranking items
Θ𝑟𝑒𝑐 isthentrainedwith
fromabaserecommender(e.g.,BPR[21],LightGCN[6]).Thispro-
| theaugmenteddata𝑨𝑎𝑢𝑔 |     | = {𝑨,𝑨(cid:101)} | toexploreuserpreferences, |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ---------------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichcanbeexpressedvia: cessyieldsthepositiveandnegativeaugmentedinteractionsets
|     |     |                 |     |      |     |     |              | +, 𝑡}           | − , 𝑡}           |             | + ,𝑡|               | − ,𝑡             |                    |
| --- | --- | --------------- | --- | ---- | --- | --- | ------------ | --------------- | ---------------- | ----------- | ------------------- | ---------------- | ------------------ |
|     |     |                 |     |      |     |     | {V (cid:101) | 𝑢 𝑢 a n d       | { V(cid:101) 𝑢 𝑢 | , w h e     | r e |V (cid:101)𝑢 = | |V (cid:101) 𝑢 | | = 𝑀 f or e a c h   |
|     |     | Θ∗=argmax𝑝(𝑨𝑎𝑢𝑔 |     | ,P), |     |     |              | ∈ U             |                  | ∈ U         |                     |                  |                    |
|     |     |                 |     |      |     | (4) | u s e        | r 𝑢 . B y c o n | str a in i n g   | a u g m e n | t a tio n to a pr   | e - fi l te r    | ed ca n di d a t e |
Θ
|                                               |     |     |     |     |     |     | set | and incorporating | similar | users’ | interactions | as  | context, we |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | ------ | ------------ | --- | ----------- |
| whereΘisthetrainableparameterofthemodels,Θ={Θ |     |     |     |     |     | ,Θ  |     |                   |         |        |              |     |             |
𝑎𝑢𝑔 𝑟𝑒𝑐}.
enhancegenerationaccuracyandmitigatenoisefromsparsedata.
Aftertrainingwithaugmenteddata𝑨𝑎𝑢𝑔,therecommendermodel
Consideringtoken-lengthlimitsofLLMs[3,43],weavoidfeeding
| 𝑓 isusedtopredictpreferencescore𝑦ˆ𝑢,𝑣 |     |     |     | byrankingthelikeli- |     |     |                                                        |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ------------------- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| Θ𝑟𝑒𝑐                                  |     |     |     |                     |     |     | thefullitemsetandinsteadrelyonacompact,informativesub- |     |     |     |     |     |     |
hoodofuser𝑢willinteractwithitem𝑣.
set.Overall,theproposedTextualInteractionAugmentation(TIA)
moduleenablestext-drivenaugmentationguidedbycollaborative
3 Methodology
signals,balancinginterpretabilityandpersonalization.
Toaddresstheusercold-startproblem,weproposethePAnDA
|            |             |           |           |              |     |        | 3.1.2 | User-ItemPreferenceCoherence. |           |              | AlthoughLLMs,astheTIA, |            |         |
| ---------- | ----------- | --------- | --------- | ------------ | --- | ------ | ----- | ----------------------------- | --------- | ------------ | ---------------------- | ---------- | ------- |
| framework, | illustrated | in Figure | 2. First, | we introduce | a   | model- |       |                               |           |              |                        |            |         |
|            |             |           |           |              |     |        | fully | leverage                      | auxiliary | information, | they have              | a critical | limita- |
agnosticpreference-alignedaugmentationmodule.Itleveragestex-
tual and collaborative signals for user-user preference matching, tion:theupperboundoftheaugmenteddataqualitydependson
thecandidateitemset𝐶
whereLLMsserveastheTextualInformationAugmentor(TIA). 𝑢.Unfortunately,duetotheconstraints
ofthecold-startscenario,thebaserecommenderalsostrugglesto
Additionally,user-itempreferencecoherenceisusedtocaptureuser
accuratelycaptureuserpreferences,leadingtovaryingqualityfor
| interests | and item | features, with | LLMs | enhancing | personaliza- |     |     |     |     |     |     |     |     |
| --------- | -------- | -------------- | ---- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
candidatesets.Additionally,LLMsprimarilyrelyonprocessingand
tionbyguidingtheintegrationofcollaborativesignalsandmit-
igating incomplete augmentation. Second, we present a model- understandinginputtext,whichleadstothefactthattheaugmented
specificdownstream-model-awareadaptationmodule.Thiscompo- datageneratedbyLLMsstillhaslimitations.Duetotheinputtoken
nentalignsaugmenteddatawiththetrainingsignalsofdownstream limitationsofLLMsandthedifficultyofincorporatingcollaborative
signalsfrominteractiondataintoLLMsandfurthergainingatten-
recommenders,enablingeffectivepreference-alignedaugmentation
tion,wegenerateaugmenteddatacomplementedbycollaborative
andalleviatingdatasparsityincold-startscenarios.
signalsandproposetheCollaborativeSignalAugmentor(CSA).
3.1 Model-AgnosticPreference-Aligned
|     |     |     |     |     |     |     | 3.1.3 | MetaMaskedAutoencoder(MetaMAE). |     |     |     | Toleveragecollabo- |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------------------------- | --- | --- | --- | ------------------ | --- |
Augmentation rativeinformation,wefine-tunethepre-trainedmodel𝑓
|     |     |     |     |     |     |     |     |     |     |     |     |     | Θ𝑟 𝑝 𝑡 .For |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- |
𝑒 𝑐
3.1.1 User-User Preference Matching. To address the cold-start user𝑢 andaugmentedinteracteditemsetV𝑢,𝑡 =V𝑢 ∪V(cid:101)𝑢 +,𝑡 ,we
problemandeffectivelyleverageauxiliaryinformationforinterpret-
canobtaintheitemsetrepresentationsvia:
inguserpreferencesanditemcharacteristics,wefocusontextual
signalsandemployLLMsastheTextualInformationAugmentor 𝑯𝑢 =𝑆𝑡𝑎𝑐𝑘({𝒉𝑖}𝑖∈V𝑢,𝑡 ), (7)
(TIA).Byconvertingtheaugmentationtaskintoanaturallanguage
|     |     |     |     |     |     |     | which𝑆𝑡𝑎𝑐𝑘(·)isthevectorstackingoperation.𝒉𝑖 |     |     |     |     | ∈R𝑑istherepre- |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | -------------- | --- |
description,LLMsgeneratemeaningfuluser-iteminteractionpairs
foreachuser𝑢,drawingontheirstrongreasoningcapabilitiesand sentationofitem𝑖andobtainedthroughEq.(2),and𝑯𝑢 ∈R|V𝑢,𝑡|×𝑑.
broadknowledge.Wealsoincorporateinteractionhistoriesfrom Tolearnanaccurateandcomprehensiverepresentationoftheuser,
similarusersasreferencestoenhanceaugmentationquality. weutilizetheaugmentedinteractionsgeneratedbyLLMsfrom
Specifically,foreachuser𝑢,weconstructasimilaruserset𝑺𝑢.In theperspectiveofitemstoguidethemodel’slearning,therebyin-
cold-startscenarios,embedding-basedsimilarityisoftenunreliable corporatingrichtextualinformationintotheitemrepresentations.
duetosparseinteractions.Instead,wemeasuresimilaritybased Tomitigatetheimpactofincompleteaugmentation,weemploya
={0,1}∈R1×|𝑉|
oninteractionhistory.Let𝑨𝑢 denotethebinary MaskedAutoencoder(MAE)toenhancetheuser/itemrepresenta-
interactionvectorofuser𝑢,wecomputesimilaritywithuser𝑚as: tionsofusersanditems.
3846

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
|     | Similar User Set |     |     |     | (a) User-User Preference  |     |     |     | History  |     |     |     |
| --- | ---------------- | --- | --- | --- | ------------------------- | --- | --- | --- | -------- | --- | --- | --- |
Gradient
|     |     |     |     |                    |                     | Matching |     |     | Interactions |     |            |     |
| --- | --- | --- | --- | ------------------ | ------------------- | -------- | --- | --- | ------------ | --- | ---------- | --- |
|     |     |     |     |                    |    LLM as Augmentor |          |     |     |              |     | Similarity |     |
|     |     | ... |     | Prompt Constructor |                     |          |     |     |              |     |            |     |
，
|     |     |     |     |     |     |     |     |     |     |  Recommender System | (   | 1,  2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------ |
Cold-Start
...
|     | Candidate Item Set |     |     |     |     |     |     |     |     |     |     | 1   |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
User
2
|     |     |     |     |     |     | ，   |     |     | Preference- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |

Aligned
Augmentation
|     |     |     |     |     |     |     |     |     | ，   |     |     | ，   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | ，   |     | ，   |     |
Pre-Trained Model
|     |     |     |           |     |     | ，   |     |     | ，   |     | ，   |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |   MetaMAE |     |     | ... |     |     |     |     |     |     |
|     |     |     |           |     |     |     |     |     | ，   |     | ，   |     |
(c) Model-Guided
，
|     | (b) User-Item Preference Coherence |     |     |     |     |     |     |     |     | Filtering Strategy |     |     |
| --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- |
|     |                                    |     |     |     |     |     |     |     |     |                    |     |     |
ℒ
Figure2:ThearchitectureoftheproposedPAnDAmodel.(a)demonstratesthetextualinformationdataaugmentationprocess
withLLMs.(b)describestheMetaMAEaugmentdatawiththecollaborativesignals.(c)introducesthedownstream-model-aware
filteringstrategyforfilteringmodel-mismatchedinteractions.
| T a s k    D e s        | c r i p t i o n                           |                                   |                       |                                                           |                                                                                   |              |        |          |              |                      |                  |     |
| ----------------------- | ----------------------------------------- | --------------------------------- | --------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------ | ------ | -------- | ------------ | -------------------- | ---------------- | --- |
|                         |                                           |                                   |                       |                                                           |                                                                                   | capabilityof | it e m | s, w e u | s e a f e at | u r er e st o r a ti | o n lo s s v ia: |     |
| Y o u   a r e   a   m o | v i e   r e c o m m e n d a t i o n   s y | s t e m   a n d   r e q u i r e d |   t o   Y r o e u q u | a i r r e e d a   t m o o   v r i e e c o r m e m c e o n | m d m   e u n s d e a r t   i A o   n w h s o y   i s t s e   m a   a 2 n 5 d -   |              |        |          |              |                      |                  |     |
r e c o m m e n d   u s e r   A   w h o   i s   a   [ a g e ] - y e a r - o l d   [ g e n d e r ]   y e a r - o l d   m a l e   p e r s o n   a n d   t h e   o c c u p a t i o n   i s     𝛾
| p e r s o n   a n d   t | h e   o c c u p a t i o n   i s   [ o c c | u p a t i o n ]   w i t h   m o v | i e s   w r i t | e r   w i t h   m o v i e s   b | a s e d   o n   u s e r   h i s t o r y   |     |     |     |     |     |     |     |
| ----------------------- | ----------------------------------------- | --------------------------------- | --------------- | ------------------------------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
b a s e d   o n   u s e r   h i s t o r y   t h a t   e a c h   m o v i e   w i t h   t i t l e ,  y e a r ,  t h a t   e a c h   m o v i e   w i t h   t i t l e ,   y e a r ,   t y p e .   1 ∑︁ 𝑯(cid:98) · 𝑯
t y p e .   F o r   r e f e r e n c e ,   w e   a l s o   w i l l  l i s t   a   s i m i l a r   u s e r   F o r   r   e f e r   e n c e ,   w e   a l s o   w i l l   l i s t   a   s i m i l a r     L 𝑢 = (cid:169) − 𝑢 𝑢 (cid:170) ,
B ’ s   h i s t o r y . u U s s e e r r   B A ’ ’ s s   h h i i s s t t o o r r y y . : 𝑓 𝑟 (cid:173) 1 (cid:13) (cid:13) (cid:174) (10)
|     |     |     | B u t c | h   C a s s i d y   a n d   t h | e  S u n d a n c e  K i d ,  1 9 6 9 ,   |     |     | | V 𝑢, | 𝑡 | | (cid:173) (cid:13) 𝑯(cid:98) (cid:13) · ∥ | 𝑯 ∥ (cid:174) |     |
| --- | --- | --- | ------- | ------------------------------- | ---------------------------------------- | --- | --- | ------ | --- | ----------------------------------------- | ------------- | --- |
P r o m p t A c t i o n   C o m e d y   W e s t e r n 𝑣∈ V 𝑢 ,𝑡 (cid:13) 𝑢 (cid:13) 𝑢
|                                                 |                                                     |         | H o m e         |   A l o n e ,   1 9 9 0 ,   C h                             | i l d r e n ' s   C o m e d y               |              |          |              |              | (cid:171)            | (cid:172)         |     |
| ----------------------------------------------- | --------------------------------------------------- | ------- | --------------- | ----------------------------------------------------------- | ------------------------------------------- | ------------ | -------- | ------------ | ------------ | -------------------- | ----------------- | --- |
| U [ s m e o r v i   e A ’   s t   i h t i l s e | t ] o , r   y [ : r e l e a s e   y e a r ] ,   [ t | yp e ]  | U s e r         |   B ’ s     h i s t o r   y :                               |                                             |              |          |              |              |                      |                   |     |
|                                                 |                                                     |         | S T a w b e r l | i v n e a   , M o 1 n 9 k 9 e y 5 , s , C   o 1 m 9 e 9 d 5 | y ,   R D o r m a a m n a c   S e c i - F i | wh e re 𝛾 is | th e s c | a li n g f a | c to r , w h | ic h i s a h y p e r | p ar a m e t e r. |     |
| . [ . m . o v i e   t i t l e                   | ] ,   [ r e l e a s e   y e a r ] ,   [ t           | y p e ] | W h i l         | e   Y o u  W e r e   S l e e p                              | i n g ,  1 9 9 5 ,   C o m e d y            |              |          |              |              |                      |                   |     |
R o m a n c e L a st ,w e a gg r e g a t e t h e l a t en t r ep r e se n t a ti o n o f u s e r 𝑢 thatin-
| U [ s m e o r v   i B e   ’ s t   i t h l i e s | ] t o ,   ry [ : r e l e a s e   y e a r ] ,   [ t | y p e ] | C a n d | i d a t e s : |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | -------------------------------------------------- | ------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[ 2 0 4 ]   B a c k  t o  t h e  F u t u r e ,  1 9 8 5 ,  C o m e d y   corporatesitem-levelcollaborativesignalsandtextualinformation,
| . [ . m . ovie title], [release year], [type] |     |     | S c i - | F   i Silence of the Lambs, The, 1991,  |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | ------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
C a n d id a t e s : [ D 9 r 8 a ] m a  T h r i l l e r 𝑧 𝑢,withtheprofile-baseduserrepresentation,ℎ
[ i d ]  [ m o v i e title], [release year], [type] [ 5 0 ]  S t a r   W a r s, 1977, Action Adventure  𝑢 obtainedthrough
| . . . |     |     | R o m a | n c e   S c i - F i   W a r |     |     |     |     |     |     |     |     |
| ----- | --- | --- | ------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[ i d ]   [ mo v i e   t it l e ],   [ r e l e a se   y e a r ] ,   [ t y p e ] P l e a s e   o u t p u t  t h e   i n d e x   o f  u s e r  A ' s   Eq.(2),toconducttheuser’sfinalcollaborativerepresentationvia:
| P l e a s e  o u t p u                                       | t  t h e  i n d e x   o f  u s e r   A | ' s   f a v o r ite and least  | f a v o                        | r  t i t e     a n d   l e   a s t     f | a  f v o r i t  c e   m o v i e .   P lease   |     |     |     |              |     |     |      |
| ------------------------------------------------------------ | -------------------------------------- | ------------------------------ | ------------------------------ | ---------------------------------------- | --------------------------------------------- | --- | --- | --- | ------------ | --- | --- | ---- |
| f a v o r i t e   m o vie. Please give the index in [] from  |                                        |                                | gi ve                          | h e i n d e x i n [ ]                    | r o m a n d i d a t e s .                     |     |     |     |              |     |     |      |
| c a n d i d a t e s .                                        |                                        |                                |       20 4                     | 98                                       |                                               |     |     | 𝒇𝑢  | =(1−𝛼)𝒉𝑢+𝛼𝒛𝑢 | ,   |     | (11) |
| （a）Thestru ctureo ft he LLM augmentat iontask                |                                        |                                | （b）Exa mpleo fL LM aumentation |                                          |                                               |     |     |     |              |     |     |      |
where𝛼 isthetrainableparameter.Then,wecanconductthepre-
Figure3:Anillustrationofthestructureofprompts.The dictionscoreoftheuser𝑢totheitem𝑣via:
figureshowsthepromptdesignedformoviedatasets.For
|                                                         |     |     |     |     |     |     |     |     | 𝑦ˆ𝑢 𝑐 =𝒇𝑢 | ·𝒉𝑣 . |     | (12) |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- | ---- |
| theBook-Crossingdataset,weuse[id],[booktitle],[author], |     |     |     |     |     |     |     |     | ,𝑣        |       |     |      |
[genre]asdescriptors. Subsequently,weselectthetop-𝑀 itemswiththehighestpre-
|     |     |     |     |     |     | dictionscoresasaugmentedpositivesamplesV𝑢 |     |     |     |     | +,𝑐 |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
First,foruser𝑢andthesetofpositivesamplesV 𝑢 +generated .Conversely,
-𝑀
b y L L M s , w e se l e ct a s u bs e t v𝑢 ⊆ V + ,𝑡 a n d m a sk th e ir r e p re se n t a - w e s e l e ct th e b o t to m it e m s w it h t h e l ow e s t s c o re s a s n eg at i v e
|     |     | (cid:101) | (cid:101) 𝑢 |     |     |     | − ,𝑐 |     |     |     |     |     |
| --- | --- | --------- | ----------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
[ 𝑀 𝐴 𝑆𝐾 ] sa m p l e s V 𝑢 . T h e co llab o r at iv e s ig n a l w il l t h e n b e f e d in to t h e
| ti on s w i t | h a m a s k to k e | n   | , r e p r es e | n te d as 𝒉 | [𝑀 𝐴 𝑆 𝐾 ] (e .g . , a |     |     |     |     |     |     |     |
| ------------- | ------------------ | --- | -------------- | ----------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
nextiterationtorefinethecandidateitemset𝑪𝑢.
learnablevectorormeanpooling).Themaskingoperationvia:
|     |     | (cid:26) | 𝑣   |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝒉𝑣 i f ∉ (cid:101) v 𝑢 3 .1 .4 M e ta o p t i m i z a t i on f o r M e t a M A E . S i n c e e a c h u s e r ’s p r ef e r -
|     | (cid:101)𝒉𝑣 = |     | 𝑣   | .   | (8) |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝒉 [MASK] i f ∈ v 𝑢 en c esa re d iff e r e n t , u s i n g a s h ar e d - pa r a m e t e r a u t o en c o d e r w o u l d
(cid:101)
struggletocapturethepersonalizeddifferencesamongusersac-
Itisworthnotingthatweonlyperformthemaskoperationon
curately.Incold-startscenarios,thelimitedinteractiondatacan
theaugmentedinteractionstomakethemodelmorerobustwithout
alsoleadtoundifferentiatedrepresentationsofusersoritems.In-
losingtheoriginalinformation.
spiredbymeta-learning[33,42],wedesignedameta-optimization
| Second,weusethemaskeduserinteractionsetV |     |     |     |     | 𝑀 astheinput |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
𝑢
totheautoencoderandreconstructtherepresentationsvia: strategytoensureeachuserhasapersonalizedautoencoderthat
capturestheiruniquepreferencesvia:
|     | ,𝒛𝑢        | =𝐴𝑢𝑡𝑜𝐸𝑛𝑐𝑜𝑑𝑒𝑟(𝑯𝑢 | 𝑀               | ;𝜃 𝐴𝐸), |     |     |     |     |     |                             |     |     |
| --- | ---------- | --------------- | --------------- | ------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
|     | 𝑯(cid:98)𝑢 |                 |                 |         | (9) |     |     |     |     |                             |     |     |
|     |            |                 | tationofuser𝑢.𝜃 |         |     |     |     | ∑︁  |     | 𝑡,V(cid:101)𝑢 𝑐(𝜃 𝑢, ∗);Θ), |     |     |
w h e r e 𝒛 𝑢 re p re s e n t s th e l at e n t r e p r e se n 𝐴𝐸 isthe m in L𝑟𝑒𝑐(V𝑢 ,V(cid:101)𝑢
|     |     |     |     |     |     |     | Θ   |     |     | 𝐴 𝐸 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tra i n a b le p a ra m e t e r o f th e a u t o e n c o d e r. 𝑢 ∈U
(13)
T h i r d, w ea t t em p t t o re c o n s t r u ct t h e r e p re se n t a t io n o f t h e in - 𝑠.𝑡.,𝜃 𝑢, ∗←arg ,V(cid:101)𝑢 𝑡,Θ 𝑝 𝑡 𝑐;𝜃 𝐴𝐸),
|              |                      |                  |             |              |                         |     |     |     | m inL𝑓𝑟(V𝑢 |     | 𝑟 𝑒 |     |
| ------------ | -------------------- | ---------------- | ----------- | ------------ | ----------------------- | --- | --- | --- | ---------- | --- | --- | --- |
| ter ac t e d | it em s e t V 𝑢, 𝑡 f | or u s e r 𝑢 . T | o e n h a n | c e th e r e | p r e se n ta t io n al |     |     | 𝐴 𝐸 |            |     |     |     |
|              |                      |                  |             |              |                         |     |     |     | 𝜃𝐴 𝐸       |     |     |     |
3847

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
where𝜃𝑢,∗ represents the personalized autoencoder parameters First,wecomputetheaveragegradientofthelossovertheorigi-
𝐴𝐸
foruser𝑢afterconvergencethroughtrainingwiththeaugmented nalinteractionsetV𝑢,whichrepresentsthemodel’sdirectionfor
data.𝑉
interaction 𝑢 denotes the original set of interacted items updatingparametersbasedontheuser’sactualpreferencesvia:
|     |     | 𝑡   | ,   | 𝑡, ,𝑡 |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f o r t h e u s e r 𝑢 ,w h i le V(cid:101) = { V(cid:101) 𝑢 + V(cid:101) 𝑢 − } r e p r es e n ts th e i te m p a i rs 1 ∑︁
|     |     | 𝑢   |     |     |     |     |     |     | ∇ΘL(V𝑢)= |     |     | ∇ΘL𝑟𝑒𝑐(𝑢,𝑣+,𝑣−), |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---------------- | --- | --- | --- |
a u g m e n t e d b y th e T IA . V(cid:101) 𝑐( 𝜃 𝑢 , ∗ ) = { V(cid:101) +,𝑐 , V − ,𝑐 } d en o te s t he it e m (15)
|                 |     |        | 𝑢 𝐴 𝐸     | 𝑢           | (cid:101) 𝑢 |          |        |     |     |     | |V 𝑢|      |     |     |     |     |
| --------------- | --- | ------ | --------- | ----------- | ----------- | -------- | ------ | --- | --- | --- | ---------- | --- | --- | --- | --- |
|                 |     |        |           | parameters𝜃 |             | 𝑢, ∗.    |        |     |     |     | {𝑣+,𝑣−}∈V𝑢 |     |     |     |     |
| pairs augmented |     | by the | CSA using |             |             | 𝐴 𝐸 L𝑟𝑒𝑐 | is the |     |     |     |            |     |     |     |     |
recommendationlossofthedownstreamrecommendermodel𝑓 Second,foreachaugmentedinteractionpair𝑣˜+,𝑣˜−,wecalculate
Θ,
whichwillbeelaboratedlater.Tofullyintegratewiththetrain- thecosinesimilaritybetweenitsgradientandthegradientofthe
ingprocessofthedownstreamrecommendersystem,weadopted originaluserinteractionstoevaluatealignmentvia:
theend-to-endoptimizationstrategy.Therefore,weemployedthe (cid:10) (cid:11),
|     |     |     |     |     |     |     |     |     | 𝑠𝑖𝑚({𝑣˜+,𝑣˜−},V𝑢)= |     | ∇ΘL𝑟𝑒𝑐(𝑢,𝑣˜+,𝑣˜−),∇ΘL(V𝑢) |     |     |     | (16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------------------- | --- | --- | --- | ---- |
reparameterizationtrick[15]toimplementthedataaugmentation
where⟨·,·⟩denotesacosinesimilarityoperatorbetweengradients.
processoftheCSA.MetaMAEincorporatestextualinformation
Last,foreachuser𝑢,wesortallaugmentedinteractionpairs
toenhancetherepresentationcapabilityofthemodel,learning
{𝑣˜+,𝑣˜−}∈V(cid:101)𝑢
comprehensiveuser/itemrepresentationsthatintegratebothcol- bytheirsimilarityscoresanddiscardthosewiththe
lowestalignment.ThemodelthenupdatesitsparametersΘusing
laborativesignalsandtextualinformation.Additionally,usinga
|     |     |     |     |     |     |     |     | the | remaining | interactions, | ensuring |     | that training | is  | guided by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | -------- | --- | ------------- | --- | --------- |
bi-levelmeta-optimizationstrategydistinguishesbetweendiffer-
interactionsconsistentwiththeuser’soriginalpreferencesignals.
| ent users | when generating |     | augmented |     | data, thereby | producing |     |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | --------- | --- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
comprehensiveandpersonalizedaugmenteddata.Thisapproach
|     |     |     |     |     |     |     |     | 3.3 | ModelOptimization |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
effectivelyaddressestheissueofincompleteaugmentation.
|     |     |     |     |     |     |     |     | AfterobtainingthecomprehensiveaugmentedinteractionsV(cid:101) |     |     |     |     |     |     | 𝑢   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
3.2 Model-SpecificDownstream-Model-Aware
|     |     |     |     |     |     |     |     | from | TIA and | CSA, we | use them | to train | a new | recommender |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ------- | -------- | -------- | ----- | ----------- | --- |
model𝑓
Adaptation Θ.Thegoalistoaddressthecold-startchallengebylever-
aginghigh-qualityaugmenteddatatolearnaccurateandexpres-
| Weobtainaugmentedinteractionsforuser𝑢,V(cid:101)𝑢 |     |     |     |     |     | = V(cid:101)𝑢 | 𝑡,V(cid:101)𝑢 𝑐,in- |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
siveuser/itemrepresentations,therebyenhancingrecommendation
cludingtruepositivesandpreference-alignedsamples.However,
performance.Tobettercapturetheunderlyingrelationshipsfrom
notalloftheseinteractionsareequallyusefulforthedownstream
limitedinteractions,weadoptBayesianPersonalizedRanking(BPR)
recommender.Incold-startsettings,thequalityofaugmenteddata
asthetrainingobjectivevia:
varies,andlimiteduserunderstandingmaycausesomesamplesto
L𝑟𝑒𝑐(𝑢,𝑣+,𝑣−)=−log(𝜎(𝑦ˆ𝑢,𝑣+−𝑦ˆ𝑢,𝑣−)),
divergefromthemodel’scurrentlearningtrajectory.Trainingon (17)
allsamplesindiscriminatelyrisksnoise,misleadingoptimization,
whereeachtrainingtriplet(𝑢,𝑣+,𝑣−)issampledfromtheunion
andperformancedrops.Sincemodelsdifferintrainingdynamics, oftheuser’shistoricalandaugmentedinteractions,i.e.,V𝑢∪V(cid:101) 𝑢.
theymayreactdifferentlytothesamedata.Thus,itisessential Thepredictedscores𝑦ˆ𝑢,𝑣+ and𝑦ˆ𝑢,𝑣− aregeneratedby𝑓
Θ.
tocheckeachinteraction’scompatibilitywiththemodel’scurrent
Theentiremodeladoptsabi-leveloptimizationend-to-endtrain-
state.Inspiredbycurriculumlearning,weevaluatesample–model
ingstrategy,wherethetrainingparametersincludetheparameters
alignmentateachiteration,enablingthemodeltoemphasizeinfor-
|     |     |     |     |     |     |     |     | 𝜃 𝐴𝐸 | oftheMetaMAEandtheparametersΘofthedownstreamrec- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
mativedataandfiltermismatchedones,improvingrepresentations ommendermodel.TheobjectiveisshowninEq.(13).Similartothe
withoutdistortinguserintent.
trainingapproachinmeta-learning,themodeltrainingprimarily
Specifically,wedefinethetraininglossforuser𝑢’sinteractions:
consistsofinner-loopoptimizationandouter-loopoptimization.
∑︁ L𝑟𝑒𝑐(𝑢,𝑣+,𝑣−), I n n e r- L o o p O p ti m i z a t io n . T h e p r im a r y g o a l o f t h is o p ti m i z a -
|     | L(V𝑢)= |     |          |     |     |     | (14) |        |                                               |            |               |               |              |            | 𝑢 ,∗         |
| --- | ------ | --- | -------- | --- | --- | --- | ---- | ------ | --------------------------------------------- | ---------- | ------------- | ------------- | ------------ | ---------- | ------------ |
|     |        |     |          |     |     |     |      | ti o n | is t o o b tai n                              | th e u s e | r- s pe c ifi | c p e rs o na | l i ze d a u | to e n c o | de r 𝜃 f o r |
|     |        |     | 𝑣+,𝑣−∈V𝑢 |     |     |     |      |        |                                               |            |               |               |              |            | 𝐴 𝐸          |
|     |        |     |          |     |     |     |      | user𝑢  | throughrapidgradientdescent,therebyobtaininga |            |               |               |              |            | c om-        |
whereL𝑟𝑒𝑐(·)isthelossfunctionofthedownstreamrecommender prehensiveandaccuraterepresentation𝒇𝑢 asshowninEq.(11).
| parameterizedbyΘ.Somepriorworkfiltersoutaugmentedinter- |     |     |     |     |     |     |     |                                          |     |     |     |     |     | 𝑐               |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- |
|                                                         |     |     |     |     |     |     |     | Then,wecangenerateaugmentedinteractionsV |     |     |     |     |     | 𝑢 thatprimarily |     |
actionswithhighloss,assumingtheyaremodel-mismatched.How- containcollaborativesignalssupplementedbytextualsignals,as
ever,thisoverlooksakeylimitation:highlossdoesnotnecessarily showninEq.(12).Asadvisedby[19],weuseonegradientdescent
implylowquality.Inmanycases,suchinteractionsareinforma- toapproximatethefinaloptimizedresultvia:
| t i v e ha rd | ex a m p l es | t h a t c a | n im p r | o ve m o | d e l r o b u | s tn e ss . D | i s c a rd i n g |     |     |      |          |      |      |     |      |
| ------------- | ------------- | ----------- | -------- | -------- | ------------- | ------------- | ---------------- | --- | --- | ---- | -------- | ---- | ---- | --- | ---- |
|               |               |             |          |          |               |               |                  |     |     | 𝜃 𝑢, | ∗≈𝜃 𝐴𝐸−𝜔 | ∇𝜃𝐴𝐸 | L𝑢 , |     | (18) |
t h e m m ay le a d t o u n d e r fi t tin g a n d m is s e d l e a r n in g o p p o r t u n it i e s. 𝐴 𝐸 1 𝑓𝑟
where𝜔
Conversely,low-lossinteractionsmaybeuninformativeoreven 1 isthelearningrateofinner-loopoptimization.
misleadingiftheypoorlyreflectuserpreferences.Therefore,loss Outer-Loop Optimization. The optimization objective of this
aloneisnotareliablesignalforevaluatingaugmentationquality. optimization,asshowninEq.(13),remainstoenhancethefinal
Instead,weproposetousegradientsignals[1,11]toassessthe recommendationperformanceofrecommendersystem𝑓 Θ.Addi-
alignmentbetweeneachaugmentedinteractionandthemodel’s tionally,tofullyutilizetheaugmenteddataobtainedfromtextual
currentlearningdirection.Bymeasuringthegradientsimilarity informationandcollaborativesignals,weadaptivelyfilteroutaug-
betweenaugmentedandoriginalinteractions,wecanmoreaccu- mentedinteractionsthatdonotmatchthemodelwiththehelpof
ratelyidentifyandretainusefulsampleswhilefilteringoutthose thetrainingsignals.Thisapproachhelpsthemodellearnmoreaccu-
inconsistentwiththemodel’soptimizationpath. rateuser/itemrepresentationswithoutalteringtheuser’soriginal
3848

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
intent.Ultimately,weupdatetheparameters𝜃 𝐴𝐸 oftheMetaMAE set according to their original papers or carefully tuned on the
andtheparametersΘofthedownstreamrecommendermodelvia: validationset,withthebestresultsreported.Wechoosethetemper-
𝜃 𝐴𝐸 =𝜃 𝐴𝐸−𝜔 2 ∑︁ ∇𝜃𝐴𝐸 L(V𝑢 ,V(cid:101)𝑢 𝑡,V(cid:101)𝑢 𝑐(𝜃 𝐴 𝑢, 𝐸 ∗)), 𝛼 atu to re 0 𝛾 .01 fr . o T m he 0, le 0 a .6 r , n 0 i . n 8 g ,1 r , a a t n es d 𝜔 ini , t 𝜔 ial , i 𝜔 zet a h r e e a s g ea g r r c e h g e a d tio in n t p h a e ra r m an e g t e e s r
𝑢∈U
∑︁ (19) [5e−5,1e−3],[1e−4,8e−4],and[
1
1e−
2
4,8e
3
−4],respectively.Wesetthe
Θ=Θ−𝜔
3
∇ΘL(V𝑢),
numberofcandidateitemsto20foralldatasets.Eachuserreceives
𝑢∈U 5 augmented positive and 5 negative samples, and 3 item pairs
where𝜔 2 ,𝜔 3 arethelearningratesofouter-loopoptimization.It arefilteredoutusingadownstream-model-awarestrategy.The
isworthmentioningthatwefocusonupdatingthemeta-model LLMusedinPAnDA(Table2)isGPT-4o4,whileKARandLLMRec
parameters𝜃 𝐴𝐸 ratherthantheuser-specificpersonalizedautoen- useLLaMA3-8B-Chat5duetocostconsiderations.Wealsoreport
coder𝜃
𝐴
𝑢,
𝐸
∗obtainedintheinner-loopoptimization.
PAnDA’sperformancewithLLaMA3-8B-Chatforcomparison.Our
implementationisbasedonPyTorch2.0.0andPython3.11.1,with
4 Experiments
theRecBolelibrary[41].Experimentsarerunonaworkstation
Inthissection,weconductexperimentstoanswerthefollowing withanIntelXeonPlatinum2.40GHzCPU,NVIDIAQuadroRTX
researchquestions(RQs): 8000GPU,and754GBRAM.
• RQ1:HowdoesourPAnDAperforminthecold-startscenario
4.2 OverallPerformanceComparison(RQ1)
comparedtothecurrentstate-of-the-artbaselines?
• RQ2:Whatistheimpactofcriticalcomponentsontheperfor- WereportthemainexperimentalresultsinTable2.Fromtheresults,
mance? wecandrawthefollowingconclusions:
• RQ3:HowdodifferentLLMsimpactPAnDA? First,ourmodel,PAnDA,consistentlyoutperformsallother
• RQ4:Howsensitiveisthemodeltodifferentparameters? baselinemodels,indicatingitsrobustnessandeffectivenessinad-
• RQ5:Howdoesthemodelaugmentedsampledifferfromother dressingthecold-start.Thissuperiorityisachievedbyincorpo-
samples? ratingahigh-qualitydataaugmentationstrategythatgenerates
comprehensiveaugmenteddataandadaptivelyselectshigh-quality
4.1 ExperimentalSetup augmentedsamplesbasedonmodeltrainingsignals.Thisadaptive
4.1.1 Datasets. WeevaluatePAnDAonthreewidelyusedreal- approachensuresthatthemodelbenefitsfromthemostrelevant
worldbenchmarkdatasets:(1)MovieLens(ML-1M)1,(2)Netflix2, andinformativedata,leadingtosignificantperformancegains.
(3)Book-Crossing3. Second,PAnDAdemonstratessubstantialimprovementsover
Followingpriorworks[13,14,18],wesimulatecold-startsce- traditionalcold-startrecommendermodelssuchasDropoutNetand
nariosbyretainingonlyuserswithnomorethan100interactions. state-of-the-artMAML-basedmethods.Thisresultunderscoresthe
Eachdatasetissplitintotraining,validation,andtestsetswitha importanceofleveragingtextualsignalsincold-startscenarios,as
ratioof8:1:1.DatasetstatisticsaresummarizedinTable1. thesesignalsprovidecrucialcontextualinformationthatneedstobe
includedinsparseuser-iteminteractiondata.Moreover,theresults
4.1.2 Evaluation Metrics. We assess model performance using:
highlightthatdataaugmentation,particularlywhencombinedwith
(1)Recall@K (R@K),(2)NormalizedDiscountedCumulativeGain
adaptiveselectionmechanisms,offersapromisingandpractical
(N@K),and(3)Precision@K (P@K).Tomitigatetestsamplingbias,
directionforovercomingthelimitationsofcold-startscenarios.
weadopttheall-rankingevaluationstrategy[31].Resultsareav-
Atlast,PAnDAalsodemonstratessubstantialimprovements
eragedoverfiveindependentruns,with𝐾 setto10,20,and50.
overtraditionalcold-startrecommendationmethods,suchasDropout-
Statisticalsignificanceisassessedvia𝑝-valuescomputedagainst
Net, and state-of-the-art MAML-based methods, such as TDAS
thebest-performingbaseline.
andM2EU.Thesetextualsignalsprovideessentialcontextualin-
4.1.3 Competingmodels. TodemonstratetheeffectivenessofPAnDA, formationthatcomplementscollaborativesignals,particularlyin
wecompareourmodelwith:(i)CF-basedmethodsincludingBPR[21], cold-startscenarioswhereinteractiondataislimited.Furthermore,
LightGCN[6]andNGCF[28].(ii)Augmentation-basedmethods the results highlight the critical role of adaptive data selection
includingDropoutNet[24],CL4SRec[36],L2Aug[25],KAR[34] mechanisms.Bydynamicallyfilteringandselectingthemostrel-
andLLMRec[30].(iii)Cold-startmethodsincludingM2EU[33] evantaugmentedsamples,PAnDAensuresthatthemodellearns
andTDAS[42]. frompreference-aligned,contextuallyaligneddata,settinganew
benchmarkforaddressingcold-startchallengesinrecommendation
4.1.4 Implementationdetails. Wefixtheembeddingsizeofeach
systems.Insummary,theexperimentalresultsvalidatetheeffective-
profilefeature(e.g.,age,gender)to32andsetthetrainingbatch
nessofPAnDAinovercomingthelimitationsofexistingcold-start
sizeto2048forbothdatasets.Embeddingparametersareinitial-
recommendationmethods.Byintegratingtextualandcollaborative
izedusingaGaussiandistribution[23].Weapplyearlystopping
signalsintoaunifiedaugmentationframeworkandemployingan
whenN@50doesnotimproveformorethan10consecutiveit-
adaptivefilteringstrategy,PAnDAdeliversstate-of-the-artperfor-
erations,selectingthebest-performingmodelduringtrainingas
manceacrossmultipledatasetsandmetrics,establishingarobust
thefinalone.Forallbaselinemodels,hyperparametersareeither
andscalablesolutionforcold-startscenarios.
1https://movielens.org/
2https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data 4https://platform.openai.com/
3http://www2.informatik.uni-freiburg.de/~cziegler/BX/ 5https://llama.meta.com/
3849

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
Table1:Statisticsoftheexperimentaldatasets
|                          | Statistics   |     |     | ML-1M    |     | Netflix    |     | Book-Crossing |
| ------------------------ | ------------ | --- | --- | -------- | --- | ---------- | --- | ------------- |
|                          | #User        |     |     | 3,132    |     | 245,281    |     | 103,459       |
|                          | #Item        |     |     | 3,354    |     | 17,761     |     | 189,284       |
|                          | #Interaction |     |     | 156,507  |     | 10,627,773 |     | 493,175       |
|                          | Sparsity     |     |     | 98.5101% |     | 99.7560%   |     | 99.9975%      |
| Avg.#interactionsperuser |              |     |     | 49.9862  |     | 43.3291    |     | 4.7669        |
userprofiles age,gender,occupation,zip_code age,gender,occupation,zip_code location,age
book_title,book_author,publi-
itemprofiles movie_title,release_year,class movie_title,release_year,class
cation_year,publisher,genre
|     | Rangeofratings |     |     | 1∼5 |     | 1∼5 |     | 1∼10 |
| --- | -------------- | --- | --- | --- | --- | --- | --- | ---- |
Table2:TheexperimentalcomparisonbetweenPAnDAandtheSOTAcold-startmethodsonthetwobenchmarkdatasets.The
bestresultsaremarkedinbold,andthesecond-bestresultsareunderlined.Allimprovementsaresignificantunderatwo-sided
| t-testwith𝑝 | <0.05overthebestbaselines. |                 |      |            |                           |            |                   |               |
| ----------- | -------------------------- | --------------- | ---- | ---------- | ------------------------- | ---------- | ----------------- | ------------- |
|             |                            | CF-basedmethods |      |            | Augmentation-basedMethods |            | Cold-startMethods |               |
| Datasets    | Metrics                    |                 |      |            |                           | KAR LLMRec |                   | PAnDA Improv. |
|             |                            | BPR LightGCN    | NGCF | DropoutNet | CL4SRec L2Aug             |            | TDAS              | M2EU          |
(LLM-based) (LLM-based)
R@10 0.2049 0.2081 0.18 0.2719 0.1478 0.2641 0.5084 0.5106 0.4591 0.4813 0.5891 15.37%
N@10 0.1708 0.1727 0.1505 0.2584 0.0767 0.1343 0.5148 0.4845 0.4266 0.4548 0.5643 16.47%
R@20 0.3015 0.3082 0.2717 0.3689 0.1837 0.3804 0.5933 0.6184 0.5315 0.5798 0.6997 13.15%
ML-1M
N@20 0.2099 0.2127 0.187 0.2912 0.0873 0.1634 0.5367 0.5087 0.4598 0.4757 0.6017 18.28%
R@50 0.4707 0.4752 0.4331 0.5165 0.2845 0.5506 0.7415 0.7612 0.6847 0.7214 0.8516 11.88%
N@50 0.2638 0.266 0.2376 0.3284 0.1204 0.1972 0.6067 0.5536 0.2964 0.5249 0.6644 20.01%
R@10 0.015 0.0158 0.0088 0.0164 0.0115 0.0202 0.0229 0.0229 0.0281 0.0197 0.0315 37.55%
N@10 0.0082 0.0091 0.0066 0.0092 0.0059 0.0098 0.0101 0.0115 0.0151 0.0104 0.0161 40.00%
Book R@20 0.0243 0.0259 0.0159 0.0268 0.0154 0.0324 0.0331 0.0349 0.0382 0.0307 0.0486 39.26%
-Crossing
N@20 0.0107 0.0118 0.0079 0.0121 0.0072 0.0143 0.0150 0.0157 0.0191 0.0144 0.0233 48.41%
R@50 0.0419 0.0466 0.0256 0.0471 0.0292 0.0564 0.0607 0.0631 0.0701 0.0568 0.0811 28.53%
N@50 0.0144 0.0162 0.0091 0.0171 0.0103 0.0203 0.0263 0.0278 0.0324 0.0204 0.0351 26.26%
R@10 0.045 0.0458 0.0388 0.0464 0.0207 0.0497 0.0529 0.0529 0.0482 0.0497 0.0615 16.26%
N@10 0.0382 0.0391 0.0352 0.0392 0.0115 0.0213 0.0415 0.0415 0.0397 0.0404 0.0461 11.08%
R@20 0.0543 0.0559 0.0414 0.0568 0.0326 0.0634 0.0639 0.0649 0.0581 0.0607 0.0786 21.11%
Netflix
N@20 0.0407 0.0418 0.0366 0.0421 0.0143 0.0272 0.0394 0.0457 0.0424 0.0444 0.0533 16.63%
R@50 0.0719 0.0766 0.0556 0.0771 0.0482 0.0861 0.0906 0.0931 0.0781 0.0868 0.1111 19.33%
N@50 0.0444 0.0462 0.0391 0.0471 0.0176 0.0314 0.0523 0.0578 0.0484 0.0504 0.0651 12.63%
Table3:AblationstudyonML-1M.LLMRecemergesasthe
4.3 AblationStudy(RQ2)
second-bestperformingbaselineoverall.
WeconductedaseriesofablationexperimentsonML-1Mtoin-
vestigatethecontributionofcomponentsappliedwithinPAnDA,
| Variants |     | N@10 R@20 | N@20 | R@50 | N@50 |     |     |     |
| -------- | --- | --------- | ---- | ---- | ---- | --- | --- | --- |
asshowninTable3.w/oTIA:TheremovalofTIAleadstoasub-
LLMRec 0.4845 0.6184 0.5087 0.7612 0.5536 stantialdropinperformanceacrossallmetrics.Thisisprimarily
because,withoutintegratingtextualsignals,theaugmentedsamples
| w/oTIA |     | 0.4415 0.5626 | 0.4703 | 0.7056 | 0.5184 |     |     |     |
| ------ | --- | ------------- | ------ | ------ | ------ | --- | --- | --- |
generatedlacksufficientcontextualrichness,therebyincreasing
| w/oCSA |     | 0.5007 0.6176 | 0.5174 | 0.7749 | 0.5689 |     |     |     |
| ------ | --- | ------------- | ------ | ------ | ------ | --- | --- | --- |
theprevalenceoffalsepositivesamples.Theseresultsunderscore
w/oDFS 0.4688 0.5991 0.4954 0.7167 0.5411 theimportanceoftextualinformationinenhancingthemodel’s
understandingofuserpreferences.TheabilityofLLMstoprocess
| PAnDA |     | 0.5643 0.6997 | 0.6017 | 0.8516 | 0.6644 |     |     |     |
| ----- | --- | ------------- | ------ | ------ | ------ | --- | --- | --- |
andintegratethesetextualsignalsplaysapivotalroleinimproving
theoverallqualityoftheaugmenteddata.w/oCSA:Theexclu-
sionofCSAalsoresultsinnoticeableperformancedegradation.
3850

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
| Table4:AblationstudyonML-1M.ImpactofdifferentLLMs |     |     |     |     |     |     | 0.8 |     |     | 0.1  |      |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
| onaccuracy,cost,andlatency                        |     |     |     |     |     |     |     |     |     |      | R@20 |     |
|                                                   |     |     |     |     |     |     | 0.6 |     |     | 0.08 |      |     |
N@20
|     | LLMs |     | R@20 | N@20 | Cost | Latency |     |     |     | 0.06 |     |     |
| --- | ---- | --- | ---- | ---- | ---- | ------- | --- | --- | --- | ---- | --- | --- |
0.4
0.04
|     | LLama2-7B-chat |     | 0.6178 | 0.4981 | -     | 33s  |     |                   | R@20 |      |                    |     |
| --- | -------------- | --- | ------ | ------ | ----- | ---- | --- | ----------------- | ---- | ---- | ------------------ | --- |
|     | LLama3-8B-chat |     | 0.6813 | 0.5847 | -     | 1.5s | 0.2 |                   | N@20 | 0.02 |                    |     |
|     | gpt-3.5-turbo  |     | 0.6345 | 0.5381 | $24.2 | 27s  |     |                   |      |      |                    |     |
|     |                |     |        |        |       |      | 0   |                   |      |      | 0                  |     |
|     | gpt-4o-mini    |     | 0.6807 | 0.5833 | $2.4  | 13s  | 1   | 3                 | 5    | 7    | 1 3                | 5 7 |
|     |                |     |        |        |       |      |     | (a) MovieLens-1M  |      |      | (b) Book-Crossing  |     |
|     | gpt-4o         |     | 0.6997 | 0.6017 | $40.3 | 18s  |     |                   |      |      |                    |     |
Table5:Analysisof|C|onML-1MandBook-Crossing. Figure 4: Performance comparison (Recall@20 and
NDCG@20)withvaryingnumbersofaugmenteddatapairs.
|     |     | ML-1M |     |     | Book-Crossing |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|C|
|     |      |      |      |      |      |      | 0.8 |     |     | 0.1  |     |      |
| --- | ---- | ---- | ---- | ---- | ---- | ---- | --- | --- | --- | ---- | --- | ---- |
|     | R@20 | N@20 | P@20 | R@20 | N@20 | P@20 |     |     |     |      |     |      |
|     |      |      |      |      |      |      |     |     |     | 0.08 |     | R@20 |
0.6
|     | 3 0.6514 | 0.5814 | 0.1849 | 0.0407 | 0.0204 | 0.0048 |     |     |     |     |     | N@20 |
| --- | -------- | ------ | ------ | ------ | ------ | ------ | --- | --- | --- | --- | --- | ---- |
0.06
| 10  | 0.6866 | 0.5948 | 0.1906 | 0.0467 | 0.0228 | 0.0051 |     |     |     |     |     |     |
| --- | ------ | ------ | ------ | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- |
0.4
| 20  | 0.6997 | 0.6017 | 0.1987 | 0.0486 | 0.0233 | 0.0053 |     |      |     | 0.04 |     |     |
| --- | ------ | ------ | ------ | ------ | ------ | ------ | --- | ---- | --- | ---- | --- | --- |
| 30  | 0.6915 | 0.6003 | 0.1954 | 0.0479 | 0.0231 | 0.0052 | 0.2 | R@20 |     |      |     |     |
0.02
N@20
| WithoutCSA,themodelreliessolelyonLLM-generatedaugmen- |       |       |                   |     |                 |           | 0   |                   |     |     | 0                  |     |
| ----------------------------------------------------- | ----- | ----- | ----------------- | --- | --------------- | --------- | --- | ----------------- | --- | --- | ------------------ | --- |
|                                                       |       |       |                   |     |                 |           | 1   | 3                 | 5   | 7   | 1 3                | 5 7 |
| tations,                                              | which | often | produce partially |     | aligned samples | that fail |     |                   |     |     |                    |     |
|                                                       |       |       |                   |     |                 |           |     | (a) MovieLens-1M  |     |     | (b) Book-Crossing  |     |
tocaptureuserpreferences.Thisincompletealignmenthampers
|     |     |     |     |     |     |     | Figure | 5: Performance |     | comparison | (Recall@20 | and |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | ---------- | ---------- | --- |
thedownstreamrecommendermodel’sabilitytoaccuratelyand
NDCG@20)withdiscardaugmenteddatapairs.
comprehensivelylearnuser/itemrepresentations,highlightingcol-
laborativesignals’crucialroleinensuringtheaugmenteddata’s {3,10,20,30},andTable5showsthat |C| = 20givesthebestre-
robustnessandaccuracy.w/oDFS:Theabsenceofdownstream-
sults.Smallervalueslimitthechoices,whilelargervaluesmakethe
modeltrainingfeedbacksignalsleadstoadeclineinperformance,
recommendationmoredifficult.
asithindersthemodel’sabilitytofilteroutsamplesmismatched
Analysisofthe#.augmenteddatapairs.Wecanobservefrom
withthemodel’scurrenttrainingtrajectory.Withoutthisprun- Figure4thattheimpactofthenumberofaugmentedsamplepairs
ing,themodelstrugglestoadapttothediversesetofaugmented variesacrossdifferentdatasets.UnlikeML-1M,theBook-Crossing
samples,resultinginlessconsistentuser/itemrepresentationsand
datasetissparse,makingitdifficulttogeneratecomprehensiveand
ultimatelyleadingtosuboptimalrecommendationperformance.
accurateaugmentedsamples.Asaresult,themodelismoresensi-
Thisemphasizesthenecessityofintegratingfeedbacksignalsto
tivetothenumberofaugmentedsamples.Thisalsoindicatesthat
maintaintherelevanceandqualityofthetrainingdata. thequalityofgeneratedaugmentedsamplesiscriticallyimportant.
Analysisofthe#.discardaugmenteddatapairs.Wecanobserve
4.4 LLMsAnalysis(RQ3)
fromFigure5thattherearemodelmismatchedaugmentedsamples.
Table4presentstheresultsoftheablationstudyanalyzingthe Themodel’sperformanceimprovesbydiscardingthesesamples
impactofdifferentLLMsastextualinformationaugmentorson basedonthemodel’strainingsignals.However,excessivediscard-
PAnDA.Weincludebothopen-sourcemodels(LLaMAseries)and ingmayleadtothelossofhighlyinformativeandhigh-quality
closed-sourcemodels(ChatGPTseries),andcomparetheireffects augmenteddata,harmingthemodel’sperformance.
onaccuracy,cost,andlatency.Theresultsshowthatthechoice
Analysisofthe#.similaruser.WecanobservefromFigure6
ofLLMhasasubstantialinfluenceonperformance:strongermod- thatalthoughtheintroductionofsimilaruserscanimproveLLM’s
elssuchasGPT-4oachievethebestRecall@20andNDCG@20, ability to understand user preferences, over-information brings
whileLLaMA3-8B-chatalsodeliverscompetitiveaccuracyatnegli- performancedegradationbecausethereistoomuchtextualinfor-
giblecostandextremelylowlatencywhendeployedonoptimized mation,anditisdifficultforLLMtofocusonthekeyinformation.
hardware.Thisindicatesaclearcorrelationbetweenmodelscale
4.6 CaseStudy(RQ5)
andperformance,withlargerandmoreadvancedLLMsproviding
moreaccuraterecommendations.Overall,thefindingsdemonstrate AsshowninFigure7,thedifferencesinaugmenteddatagenerated
thatemployinghigher-capacityLLMscansignificantlyimprove
byvariousmethodsforcold-starttasksareevident.Theleftside
PAnDA,highlightingtheimportanceofcarefullyselectingmodels
showsthegroundtruthuserinteractiondataandtherightside
thatbalanceaccuracygainswithefficiencyandcostconsiderations.
displaystheaugmenteddatadistribution.Weassessthequalityof
augmentedsamplesusingthemaximumcosinesimilarity,denoted
4.5 HyperparameterAnalysis(RQ4)
as𝑞,betweeneachaugmentedsample’sembeddingandtheground
|C|.SincetheinputtokenconstraintsoftheLLMs,
Analysisof truthsamples.Thismetricindicatesthequalityoftheaugmented
coupledwiththeproblemoffalsepositiveaugmentedsamples,we samples.TraditionalmethodslikeL2Augstrugglewithaccurately
usethecandidateitemsetCtolimitthecandidateitemsbasedon capturinguserpreferences,leadingtomanyfalse-positivesamples
theLLMsaugmentedsamples.Duetocostconstraints,weexplored (𝑞 ≤ 0.25),whichnegativelyimpactmodellearning.LLM-based
3851

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
1 1
0 0
0 1 3 5
02@R 02@N
0.08 0.08
0 0
0 1 3 5
02@R 02@N
1 1
0 0
0 1 3 5
05@R 05@N
0.1 0.06
0 0
0 1 3 5
05@R 05@N
LargeLanguageModels(LLMs)forRecommendation.LLMs
havegarneredattentioninrecommendersystems,withvariousef-
fortsmadetomodeluserbehaviorwithLLMs[10,20,29].LLMs
havebeenemployedasinferencemodelsinvariousrecommenda-
tiontasks,suchasratingprediction,sequentialrecommendation,
anddirectrecommendation.Recentworkhasfurtherexploredtheir
potentialinaddressingcold-startchallenges,suchasleveraging
language-modelpriorstoovercomeitemcold-start[26],andusing
keyword-drivenretrieval-augmentedLLMstoalleviateusercold-
startissues[12].However,mostpreviousapproachesprimarilyuti-
lizedLLMsasrecommenders[3],focusingontheirtext-processing
capabilitieswhileoverlookingthecollaborativesignalsthattradi-
(a) MovieLens-1M (b) Book-Crossing
Figure6:Analysisofthe#similarusersonML-1MandBook- tionalrecommendersystemsexcelatcapturing.Inthispaper,we
Crossing. combineLLM-baseddataaugmentation[30,43]withtraditional
dataaugmentationmethodsbasedoncollaborativesignals,combin-
ingbothattwolevelstoachievepreference-alignedaugmentation
Ground truth 1259 2065 1266 737 590 736 1270
andimprovetheperformanceofdownstreamrecommendermodels.
LLM as DataAugmentationforRecommendation.Dataaugmen-
augmentor 1259 2065 1266 737 149 94 736 15 tationhasbeenalong-standingresearchfocusinrecommender
（LLMRec）
systems.Commonaugmentationoperationsincludepermutation,
RSs as
augmentor 1259 2065 1266 481 590 36 481 1597 deletion,swapping,insertion,andduplication[17],aswellasmore
（L2Aug)
recentstrategiessuchascounterfactualreasoning[39]andcon-
trastive learning [27]. Despite these efforts, the quality of aug-
Ours 1259 2065 1266 737 590 94 736 1270 menteddataremainsanopenproblem,particularlyinsparseor
cold-startsettings.Inthiswork,werevisitinsertionanddeletion
Available data when
Augmented data operationsfromtheperspectiveofuserpreferencealignmentand
model training
proposePAnDAtailoredforthecold-startscenario.
Available data when model training High-quality augmentations ( )
Augmented data for training Partially-aligned augmentatioqns≥ (0.75 )
0.25<q<0.75 6 Conclusion
Ground truth False-positive augmentations ( )
Figure7:Casestudyonaugmentationsamplqe≤s0b.25ydifferent Inthispaper,weaddressedusercold-startrecommendationvia
augmentors. dataaugmentation.WeanalyzedlimitationsofexistingLLM-based
methodsandidentifiedtwokeypropertiesofhigh-qualityaugmen-
tation:preferencealignmentanddownstream-modelawareness.
methods(LLMRec)useworldknowledgetogeneratepreference-
Basedonthis,weproposedPAnDA,anovelLLM-poweredframe-
alignedsamplesbutstillproducepartiallyalignedandfalse-positive
workthatiterativelyintegratestextualandcollaborativesignalsat
samples,showingthelimitationsofrelyingsolelyontextualinfor-
bothinteractionandrepresentationlevels,whileadaptivelyfilter-
mation.Incontrast,PAnDAgeneratesaugmenteddatathatclosely
inginconsistentsamplesduringtraining.Extensiveexperiments
alignswithvaliduserpreferences,effectivelycapturingaccurate
onthreereal-worlddatasetsconfirmedthebenefitsofgenerating
preferencesandeliminatingfalse-positiveandpartiallyalignedsam-
preference-alignedanddownstream-model-awareaugmenteddata
ples.Bycombiningtextualaugmentation,collaborativesignals,and
forrecommendationtasks.Forfuturework,weplantoenhance
adownstream-model-awarefilteringstrategy,PAnDAaddresses
scalabilityandefficiencyofthebi-leveloptimizationandconduct
datasparsityandqualityissuesincold-startscenarios,providing
morerigorousvalidationsofalignmentwithtrueuserpreferences.
high-quality,preference-alignedaugmentedsamples.
5 RelatedWork Acknowledgments
Cold-startRecommendation.Toaddressthisissue,manyworks ThisworkwassupportedbytheHeilongjiangKeyR&DProgram
useauxiliaryinformationtoimprovecold-startuseroritemrepre- ofChinaunderGrantNo.GA23A915,AustralianResearchCoun-
sentations,suchassocialnetworks[16]orcross-domaindata[4]. cil (ARC) under Grant No. DP200102611, Hong Kong Research
GraphNeuralNetworks(GNNs)furthercapturehigh-orderseman- GrantsCouncil’sResearchImpactFund(No.R1015-23),Collabo-
ticsfromknowledgegraphs[5]andheterogeneousnetworks[37]. rative Research Fund (No.C1043-24GF), General Research Fund
Whensideinformationislimited,contrastivelearning[27]helps (No.11218325),InstituteofDigitalMedicineofCityUniversityof
refinecollaborativeembeddings.Morerecently,meta-learning[5, HongKong(No.9229503),Huawei(HuaweiInnovationResearch
33,42]hasemergedasadominantsolution.Ourmethodinstead Program),Tencent(CCF-TencentOpenFund,TencentRhino-Bird
leveragesLLMstogeneratecontextuallyrelevantsampleswhilere- FocusedResearchProgram),Alibaba(CCF-AlimamaTechKanga-
tainingcollaborativesignals,allowingPAnDAtohandlecold-start rooFundNo.2024002),AntGroup(CCF-AntResearchFund),Didi
morerobustlywithoutcomplexauxiliarydataorgraphstructures. (CCF-DidiGaiaScholarsResearchFund),Kuaishou,andBytedance.
3852

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
7 GenAIDisclosureStatement
InProceedingsofthe44thinternationalACMSIGIRconferenceonResearchand
developmentininformationretrieval.1608–1612.
GenAItoolswereactivelyusedaspartoftheresearchmethodology
[18] YuanfuLu,YuanFang,andChuanShi.2020.Meta-learningonheterogeneous
inthiswork.Specifically,LLMswereemployedtogenerateaug- informationnetworksforcold-startrecommendation.InProceedingsofthe26th
mentedtrainingsamplesforcold-startuserswithintheproposed ACMSIGKDDinternationalconferenceonknowledgediscovery&datamining.
1563–1573.
PAnDAframework.Theseaugmentedinteractionswereintegrated [19] AlexNichol,JoshuaAchiam,andJohnSchulman.2018. Onfirst-ordermeta-
intothedataaugmentationpipelineundertheauthors’fullsupervi- learningalgorithms.arXivpreprintarXiv:1803.02999(2018).
[20] XubinRen,WeiWei,LianghaoXia,LixinSu,SuqiCheng,JunfengWang,Dawei
sion.Inaddition,LLMswerealsousedtoassistwithminorediting
Yin,andChaoHuang.2024.Representationlearningwithlargelanguagemodels
andwordingimprovementsinthemanuscript.AllAI-generated forrecommendation.InProceedingsoftheACMonWebConference2024.3464–
contentwascarefullyreviewedandvalidatedbytheauthorsto 3475.
[21] SteffenRendle,ChristophFreudenthaler,ZenoGantner,andLarsSchmidt-Thieme.
ensureaccuracy,relevance,andalignmentwiththeresearchgoals.
2012.BPR:Bayesianpersonalizedrankingfromimplicitfeedback.arXivpreprint
arXiv:1205.2618(2012).
References [22] ScottSanner,KrisztianBalog,FilipRadlinski,BenWedin,andLucasDixon.
2023.Largelanguagemodelsarecompetitivenearcold-startrecommendersfor
[1] SungyongBaik,JanghoonChoi,HeewonKim,DoheeCho,JaesikMin,andKy- language-anditem-basedpreferences.InProceedingsofthe17thACMconference
oungMuLee.2021.Meta-learningwithtask-adaptivelossfunctionforfew-shot onrecommendersystems.890–896.
learning.InProceedingsoftheIEEE/CVFinternationalconferenceoncomputer [23] LukeVilnisandAndrewMcCallum.2014. Wordrepresentationsviagaussian
vision.IEEE,9465–9474. embedding.arXivpreprintarXiv:1412.6623(2014).
[2] YuweiCao,LiangweiYang,ChenWang,ZhiweiLiu,HaoPeng,ChenyuYou, [24] MaksimsVolkovs,GuangweiYu,andTomiPoutanen.2017. Dropoutnet:Ad-
andPhilipSYu.2023. Multi-taskitem-attributegraphpre-trainingforstrict dressingcoldstartinrecommendersystems. Advancesinneuralinformation
cold-startitemrecommendation.InProceedingsofthe17thACMConferenceon processingsystems30(2017).
RecommenderSystems.322–333. [25] JianlingWang,YaLe,BoChang,YuyanWang,EdHChi,andMinminChen.2022.
[3] Zhikai Chen, Haitao Mao, Hang Li, Wei Jin, Hongzhi Wen, Xiaochi Wei, Learningtoaugmentforcasualuserrecommendation.InProceedingsoftheACM
ShuaiqiangWang,DaweiYin,WenqiFan,HuiLiu,etal.2024. Exploringthe WebConference2022.2183–2194.
potentialoflargelanguagemodels(llms)inlearningongraphs.ACMSIGKDD [26] ShiyuWang,HaoDing,YupengGu,SergulAydore,KoushaKalantari,and
ExplorationsNewsletter25,2(2024),42–61. BranislavKveton.2024.Language-modelpriorovercomescold-startitems.arXiv
[4] WenjingFu,ZhaohuiPeng,SenzhangWang,YangXu,andJinLi.2019.Deeply preprintarXiv:2411.09065(2024).
fusingreviewsandcontentsforcoldstartusersincross-domainrecommendation [27] WenboWang,BingquanLiu,LiliShan,ChengjieSun,BenChen,andJianGuan.
systems.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.33. 2024.PreferenceAwareDualContrastiveLearningforItemCold-StartRecom-
AAAIPress,PaloAlto,California,USA,94–101. mendation.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.38.
[5] DiHan,XiaotianJing,YijunChen,JunminLiu,KaiLiao,andWentingLi.2025. 9125–9132.
Cold-startrecommendationbasedonknowledgegraphandmeta-learningunder [28] XiangWang,XiangnanHe,MengWang,FuliFeng,andTat-SengChua.2019.
positiveandnegativesampling.ACMTransactionsonRecommenderSystems3,3 Neuralgraphcollaborativefiltering.InProceedingsofthe42ndinternationalACM
(2025),1–24. SIGIRconferenceonResearchanddevelopmentinInformationRetrieval.165–174.
[6] XiangnanHe,KuanDeng,XiangWang,YanLi,YongdongZhang,andMeng [29] XiaoleiWang,XinyuTang,WayneXinZhao,JingyuanWang,andJi-RongWen.
Wang.2020.Lightgcn:Simplifyingandpoweringgraphconvolutionnetworkfor 2023.Rethinkingtheevaluationforconversationalrecommendationintheera
recommendation.InProceedingsofthe43rdInternationalACMSIGIRConference oflargelanguagemodels.arXivpreprintarXiv:2305.13112(2023).
onResearchandDevelopmentinInformationRetrieval.ACM,NewYork,NY,USA, [30] WeiWei,XubinRen,JiabinTang,QinyongWang,LixinSu,SuqiCheng,Jun-
639–648. fengWang,DaweiYin,andChaoHuang.2024.Llmrec:Largelanguagemodels
[7] XiangnanHe,LiziLiao,HanwangZhang,LiqiangNie,XiaHu,andTat-Seng withgraphaugmentationforrecommendation.InProceedingsofthe17thACM
Chua.2017.Neuralcollaborativefiltering.InProceedingsofthe26thInternational InternationalConferenceonWebSearchandDataMining.806–815.
ConferenceonWorldWideWeb.InternationalWorldWideWebConferences [31] YinweiWei,XiangWang,XiangnanHe,LiqiangNie,YongRui,andTat-SengChua.
SteeringCommittee,Geneva,Switzerland,173–182. 2021.Hierarchicaluserintentgraphnetworkformultimediarecommendation.
[8] NicoleImmorlica,MeenaJagadeesan,andBrendanLucier.2024. Clickbaitvs. IEEETransactionsonMultimedia24(2021),2701–2712.
quality:Howengagement-basedoptimizationshapesthecontentlandscapein [32] XuanshengWu,HuachiZhou,YuchengShi,WenlinYao,XiaoHuang,andNing-
onlineplatforms.InProceedingsoftheACMWebConference2024.36–45. haoLiu.2024.CouldSmallLanguageModelsServeasRecommenders?Towards
[9] YangqinJiang,LianghaoXia,WeiWei,DaLuo,KangyiLin,andChaoHuang. Data-centricCold-startRecommendation.InProceedingsoftheACMonWeb
2024.Diffmm:Multi-modaldiffusionmodelforrecommendation.InProceedings Conference2024.3566–3575.
ofthe32ndACMInternationalConferenceonMultimedia(ACMMM).ACM,New [33] ZhenchaoWuandXiaoZhou.2023.M2eu:Metalearningforcold-startrecom-
York,NY,USA,7591–7599. mendationviaenhancinguserpreferenceestimation.InProceedingsofthe46th
[10] Wang-Cheng Kang, Jianmo Ni, Nikhil Mehta, Maheswaran Sathiamoorthy, InternationalACMSIGIR.1158–1167.
LichanHong,EdChi,andDerekZhiyuanCheng.2023.DoLLMsUnderstand [34] YunjiaXi,WeiwenLiu,JianghaoLin,XiaolingCai,HongZhu,JiemingZhu,Bo
UserPreferences?EvaluatingLLMsonUserRatingPrediction.arXivpreprint Chen,RuimingTang,WeinanZhang,andYongYu.2024.Towardsopen-world
arXiv:2305.06474(2023). recommendationwithknowledgeaugmentationfromlargelanguagemodels.In
[11] MikhailKhodak,Maria-FlorinaFBalcan,andAmeetSTalwalkar.2019.Adaptive Proceedingsofthe18thACMConferenceonRecommenderSystems.12–22.
gradient-basedmeta-learningmethods.AdvancesinNeuralInformationProcessing [35] ChangrongXiao,SeanXinXu,KunpengZhang,YufangWang,andLeiXia.2023.
Systems32(2019). EvaluatingreadingcomprehensionexercisesgeneratedbyLLMs:Ashowcase
[12] Hai-DangKieu,Minh-DucNguyen,Thanh-SonNguyen,andDungDLe.2025. ofChatGPTineducationapplications.InProceedingsofthe18thWorkshopon
Keyword-drivenretrieval-augmentedlargelanguagemodelsforcold-startuser InnovativeUseofNLPforBuildingEducationalApplications(BEA2023).610–625.
recommendations.InCompanionProceedingsoftheACMonWebConference2025. [36] XuXie,FeiSun,ZhaoyangLiu,ShiwenWu,JinyangGao,JiandongZhang,Bolin
2717–2721. Ding,andBinCui.2022.Contrastivelearningforsequentialrecommendation.In
[13] HoyeopLee,JinbaeIm,SeongwonJang,HyunsoukCho,andSeheeChung.2019. 2022IEEE38thinternationalconferenceondataengineering(ICDE).IEEE,1259–
Melu:Meta-learneduserpreferenceestimatorforcold-startrecommendation.In 1273.
Proceedingsofthe25thACMSIGKDD.1073–1082. [37] GuangpingZhang,DongshengLi,HansuGu,TunLu,andNingGu.2024.Het-
[14] XixunLin,JiaWu,ChuanZhou,ShiruiPan,YananCao,andBinWang.2021. erogeneousGraphNeuralNetworkwithPersonalizedandAdaptiveDiversity
Task-adaptiveneuralprocessforusercold-startrecommendation.InProceedings forNewsRecommendation.ACMTransactionsontheWeb18,3(2024),1–33.
oftheWebConference2021.1306–1316. [38] LingziZhang,XinZhou,ZhiweiZeng,andZhiqiShen.2024.MultimodalPre-
[15] HuafengLiu,JingxuanWen,LipingJing,andJianYu.2019.Deepgenerativerank- trainingforSequentialRecommendationviaContrastiveLearning.ACMTrans-
ingforpersonalizedrecommendation.InProceedingsofthe13thACMConference actionsonRecommenderSystems3,1(2024),1–23.
onRecommenderSystems.34–42. [39] ShengyuZhang,DongYao,ZhouZhao,Tat-SengChua,andFeiWu.2021.
[16] SiweiLiu,XiWang,CraigMacdonald,andIadhOunis.2024. ASocial-aware Causerec:Counterfactualusersequencesynthesisforsequentialrecommen-
GaussianPre-trainedmodelforeffectivecold-startrecommendation.Information dation.InProceedingsofthe44thInternationalACMSIGIRConferenceonResearch
Processing&Management61,2(2024),103601. andDevelopmentinInformationRetrieval.367–377.
[17] ZhiweiLiu,ZiweiFan,YuWang,andPhilipSYu.2021.Augmentingsequential [40] YanZhang,ChangyuLi,IvorWTsang,HuiXu,LixinDuan,HongzhiYin,Wen
recommendationwithpseudo-prioritemsviareverselypre-trainingtransformer. Li,andJieShao.2022.Diversepreferenceaugmentationwithmultipledomains
3853

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
forcold-startrecommendations.In2022IEEE38thInternationalConferenceon [42] XuhaoZhao,YanminZhu,ChunyangWang,MengyuanJing,JiadiYu,andFeilong
DataEngineering(ICDE).IEEE,2942–2955. Tang.2023.Task-difficulty-awaremeta-learningwithadaptiveupdatestrategies
[41] WayneXinZhao,ShanleiMu,YupengHou,ZihanLin,KaiyuanLi,YushuoChen, forusercold-startrecommendation.InProceedingsofthe32ndACMInternational
YujieFLu,HuiWang,ChangxinTian,XingyuPan,YingqianMin,ZhichaoFeng, ConferenceonInformationandKnowledgeManagement.3484–3493.
XinyanFan,XuChen,PengfeiWang,WendiJi,YaliangLi,XiaolingWang,and [43] ZhiZheng,WenshuoChao,ZhaopengQiu,HengshuZhu,andHuiXiong.2024.
Ji-RongWen.2021. Recbole:Towardsaunified,comprehensiveandefficient Harnessinglargelanguagemodelsfortext-richsequentialrecommendation.In
frameworkforrecommendationalgorithms.InCIKM. ProceedingsoftheACMonWebConference2024.3207–3216.
3854