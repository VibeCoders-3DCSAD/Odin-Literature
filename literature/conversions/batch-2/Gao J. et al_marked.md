---
conversion_metadata:
  converted_at: "2026-07-22T13:23:14Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Gao J. et al.pdf"
  source_pdf_sha256: "8316498cd84f685bd5345b3b25d702681ddfa84e36f20760b84cd4458543ebe9"
  page_count: 55
  markdown_char_count: 358682
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

et al. [full author details at the end of the article]

Artificial Intelligence Review (2025) 58:266
https://doi.org/10.1007/s10462-025-11255-1

Agent-in-the-loop to distill expert knowledge into artificial 
intelligence models: a survey

Jiayuan Gao1,2 · Yingwei Zhang1,2 · Yiqiang Chen1,2 · Yihan Dong3 · Yuanzhe Chen1,2 · 
Shuchao Song1,2 · Boshi Tang4 · Yang Gu1,2

Accepted: 2 May 2025 / Published online: 4 June 2025
© The Author(s) 2025

Abstract
Large-scale  neural  networks  have  revolutionized  many  general  knowledge  areas  (e.g., 
computer  vision  and  language  processing),  but  are  still  rarely  applied  in  many  expert 
knowledge areas (e.g., healthcare), due to data sparsity and high annotation expenses. Hu-
man-in-the-loop machine learning (HIL-ML) incorporates expert domain knowledge into 
the  modeling  process,  effectively  addressing  these  challenges.  Recently,  some  research-
ers have started using large models to substitute for certain tasks typically performed by 
humans. Although  large  models  have  limitations  in  expert  knowledge  areas,  after  being 
trained on trillions of examples, they have demonstrated advanced capabilities in reason-
ing,  semantic  understanding,  grounding,  and  planning.  These  capabilities  can  serve  as 
proxies  of  human,  which  introduces  new  opportunities  and  challenges  in  HIL-ML  area. 
Based on the above, we summarize a more comprehensive framework, Agent-in-the-Loop 
Machine Learning (AIL-ML), where agent represents both humans and large models. AIL-
ML can efficiently collaborate human and large model to construct vertical AI models with 
lower costs. This paper presents the first review of recent advancements in this area. First, 
we provide a formal definition of AIL-ML and discuss its related fields. Then, we catego-
rize  the AIL-ML  methods  based  on  data  processing  and  model  development,  providing 
formal  definitions  for  each,  and  present  representative  works  in  detail  for  each  category. 
Third,  we  highlight  relative  applications  of AIL-ML.  Finally,  we  summarize  the  current 
literature and highlight future research directions.

Keywords  Human-in-the-Loop · Machine learning · Deep learning · Large language 
models

1  Introduction

Over the past decade, large-scale neural networks (LeCun et al. 2015) have significantly 
advanced the development of computer vision, natural language processing, and other gen-
eral knowledge domains. These breakthroughs, such as applications in image recognition 
(Krizhevsky et al. 2012), have enabled technologies like autonomous vehicles and facial

Extended author information available on the last page of the article

1 3

---

<!-- PAGE 2 -->

266  Page 2 of 55

recognition systems. In the realm of natural language processing, large models like the GPT 
(Radford et al. 2018) series and BERT (Kenton and Toutanova 2019) have achieved near-
human capabilities in generating and understanding complex texts. These models have not 
only enhanced the accuracy of machine translation but also improved interactions between 
users  and  artificial  systems.  Furthermore,  the  adoption  of  these  technologies  has  driven 
innovations in intelligent customer service, showcasing their commercial potential.

Despite the remarkable achievements of large-scale neural networks in general knowl-
edge areas, they face numerous challenges in expert domains such as healthcare, law, and 
so on. These fields often involve highly specialized and sparse datasets that are expensive 
to  acquire  and  require  extensive  preprocessing  and  precise  manual  annotation  to  ensure 
data quality and usability. Additionally, traditional deep learning models are severely tested 
in their generalization capabilities within these domains (Zhang et al. 2021). The inability 
of training data to fully represent the complexities of the real world often means that these 
models may fail to accurately predict unseen scenarios, thereby limiting their reliability in 
professional applications. Data privacy becomes crucial when dealing with sensitive per-
sonal details in medical or legal contexts (Dwork 2006), demanding extra measures to sat-
isfy regulatory and ethical rules. These challenges demonstrate the need to integrate expert 
domain knowledge into AI systems, where high accuracy and explainable decision-making 
processes are necessary for gaining end-user trust. For instance, a medical diagnostic sys-
tem  must  be  able  to  clearly  justify  its  recommendations  to  physicians,  allowing  them  to 
make informed clinical decisions. Thus, integrating the knowledge and judgment of human 
experts into the AI model becomes essential.

Facing the challenges above, Human-in-the-Loop Machine Learning (HIL-ML) (Wu et 
al. 2022) offers an effective solution by incorporating human knowledge into the machine 
learning process. It also emphasizes iterative interaction between humans and systems. As 
shown in Fig. 1, in the HIL-ML framework, humans contribute at all stages of the machine 
learning  loop.  These  contributions  enable  machines  to  integrate  human  knowledge  and 
experience,  thereby  enhancing  model  accuracy  and  adaptability.  HIL-ML  distills  human 
expertise into machine learning through a dynamic feedback mechanism. Unlike static pipe-
lines,  the  framework  employs  an  adaptive  loop  architecture  where  data  and  model  influ-
ence each other iteratively. These human interventions allow machines to integrate human 
knowledge  and  experience,  thereby  enhancing  model  accuracy,  adaptability,  and  perfor-
mance on unseen data. By directly distilling deep expert knowledge into models, HIL-ML 
not only improves model performance but also enhances explainability, making the models 
more transparent and trustworthy for end-users. This approach also reduces potential pri-
vacy risks when handling sensitive information, as human experts can directly monitor and 
adjust the processing of such data. Therefore, HIL-ML not only addresses the limitations of

Fig. 1  The HIL-ML workflow which can be segmented into four main stages: Data Acquisition, Data Pro-
cessing, Model Development, and Model Optimization, with continuous human involvement throughout 
the process to ensure iterative refinement and optimization of the models

---

<!-- PAGE 3 -->

Page 3 of 55  266

traditional automation methods in professional fields but also enhances the reliability and 
effectiveness of AI systems in practical operations. By integrating human expert knowledge 
and  feedback,  HIL-ML  enables AI  systems  to  excel  both  in  technological  sophistication 
and practical application. Through human involvement, HIL-ML utilizes human knowledge 
for corrections and optimizations at various stages of modeling process, resulting in more 
precise and reliable machine learning models (Mosqueira-Rey et al. 2023a).

Recently, researchers have begun to employ large models to perform specific tasks tra-
ditionally executed by humans (Ding et al. 2022; Hsieh et al. 2023a). Although these large 
models hold some limitations in domains requiring expert knowledge, they have demon-
strated advanced capabilities in reasoning, semantic understanding, grounding, and planning 
after being trained on trillions of examples. Their deep contextual understanding enables 
them to generate and comprehend language like humans (Mondorf and Plank 2024). Large 
models, such as GPT (Radford et al. 2018) and LLaMA (Touvron et al. 2023), possess deep 
contextual understanding and can generate meaningful outputs with minimal human input. 
These capabilities allow large models to act as proxies for human intelligence, thereby intro-
ducing new opportunities and challenges in the HIL-ML area. However, Current reviews 
(Wu et al. 2022; Mosqueira-Rey et al. 2023a; Xin et al. 2018) about HIL-ML fail to explore 
how to address these challenges. Moreover, the potential role of Large Models (Brown et al. 
2020) as participants in HIL-ML has been largely overlooked. Building on these insights, 
we  propose  a  novel  concept  called  Large-Model-in-the-Loop  Machine  Learning  (LMIL-
ML).  In  the  LMIL-ML  framework,  large  models  are  integrated  into  the  modeling  loop, 
intervening at stages like data preprocessing or model development. By embedding large 
models into the training process, LMIL-ML reduces the reliance on human annotation. This 
framework achieves cost-efficient model training and improved accuracy by distilling large 
model expertise into more task-specific machine learning models.

Based  on  the  frameworks  of  HIL-ML  and  LMIL-ML,  we  further  introduce  a  unified 
and  comprehensive  framework, Agent  in  the  Loop  Machine  Learning  (AIL-ML).  In  this 
framework, agents include both humans and large models. This framework aims to leverage 
the  complementary  strengths  of  human  cognitive  skills  and  machine  efficiency. AIL-ML 
combines human intuition and expertise with the computational power and reasoning abil-
ity of large models, creating a balance that leverages the strengths of both. These agents 
interact with the model at various stages-data processing, model training, and optimization-
forming a machine learning loop. This dynamic process enhances the model’s adaptability 
to changing environments, improves predictive accuracy across diverse tasks, and reduces 
the cost of iterative development. This paper provides a comprehensive overview of recent 
advancements in this area.

This study employs an extensive literature survey method to ensure comprehensive and 
high-quality  research.  We  have  reviewed  works  published  at  top  computer  science  and 
human-computer interaction conferences from 2018 to 2024, such as IJCAI, ACL, KDD, 
AAAI,  NIPS,  ICML,  CVPR,  ICLR,  CHI,  IMWUT,  CSCW  and  so  on. Additionally,  we 
have also investigated the latest research on arXiv from 2023 and 2024. By reading titles 
and abstracts, we selected the most relevant papers, classified them, and conducted in-depth 
analyses to ensure a precise understanding of the methods. As shown in Fig. 2, the paper 
begins by defining the core processes of AIL-ML and provides a structured framework for 
understanding its mechanisms. We then discuss the methodologies used in AIL-ML, empha-
sizing the critical aspects of data acquisition and processing as well as model development

---

<!-- PAGE 4 -->

266  Page 4 of 55

Fig. 2  Framework for AIL-ML Methodology. The framework can be divided into two main phases: Data 
Acquisition and Processing, and Model Development and Optimization. The first phase contains Data 
Collection, Initialization, Quality Enhancement, and Annotation. The second phase involves Model Cold 
Start, Training, and Iterative Enhancement

and optimization. We also summarize applications of AIL-ML in domains requiring spe-
cialized  knowledge.  In  the  last  section,  we  highlight  the  current  challenges  within AIL-
ML research and outline future research directions, providing both theoretical and practical 
guidance for further development in the field.

The insights gained from this paper may contribute to a deeper understanding and practi-

cal application of AIL-ML. The paper’s contributions are as follows:

1.  We conduct a comprehensive literature review of existing works on AIL-ML, focusing 
on the role of agent in AIL-ML. Specifically, we summarize how humans and LLMs 
operate within the framework of AIL-ML.

2.  We offer a detailed and structured classification of data processing and model develop-
ment methods within AIL-ML. This taxonomy organizes methods into distinct catego-
ries, helping researchers select suitable approaches for specific problems.

3.  Based on the classification, we analyze and summarize the differences and relationships

between various methods in AIL-ML.

4.  We  propose  a  clear  methodological  framework  for AIL-ML,  by  formalizing  a  math-
ematical  description.  This  framework  simplifies  complex  concepts  and  processes,

---

<!-- PAGE 5 -->

enhancing their accessibility to researchers and practitioners. This formalization also 
establish a solid theoretical foundation for future work.

Page 5 of 55  266

2  Background

2.1  Related reviews

Human-in-the-loop has emerged as a prominent area of interest within the field of machine 
learning in recent years. With the expansion of machine learning applications across com-
puter vision, natural language processing, and speech processing, there has been a growing 
realization  that  reliance  solely  on  machine-driven  learning  is  limited.  Integrating  human 
domain knowledge and experience has proven to be more effective in addressing specific 
challenges.  In  the  realm  of  HIL  machine  learning,  several  comprehensive  review  papers 
have  been  published,  summarizing  various  techniques,  challenges,  and  future  directions 
within this field. These reviews not only define the various technologies but also discuss the 
interplay between them, providing researchers with a clear theoretical framework for further 
exploration. To provide a comprehensive understanding of the state-of-the-art in HIL-ML, 
we compare three representative surveys that focus on different aspects of this field. Table 1 
summarizes their key contexts, theoretical foundations, adaptation to LLMs, strengths, and 
weaknesses, offering insights into the distinct contributions and limitations of each work.

Wu et al. (2022) conducted a comprehensive overview of HIL-ML from the perspective 
of data management. They analyzed existing works on HIL, categorizing them into three 
progressively related categories: (1) efforts to enhance model performance through data pro-
cessing, (2) improvements in model performance via interventional model training, and (3) 
human-in-the-loop system design. Furthermore, the paper summarizes applications of HIL 
and discusses its technical merits and limitations in fields such as natural language process-
ing and computer vision. However, the survey lacks theoretical depth, as it does not formal-
ize the role of human involvement in HIL-ML through mathematical models. Additionally, 
it does not address the impact of large pre-trained models, which limits its relevance in the 
context of modern LLMs. Despite these limitations, the survey’s focus on practical system 
implementation offers valuable insights for engineering-focused studies in HIL-ML.

Beyond analyzing HIL from a data perspective, there has been significant research inter-
est  in  the  interaction  modalities  between  humans  and  machine  learning  algorithms  and 
leveraging these interactions to boost model performance. Eduardo Mosqueira-Rey et al. 
have contributed a thorough overview of this area, defining the forms of HIL machine learn-

Table 1  A comparative analysis of surveys on HIL-ML
A survey of 
Dimension
HIL-ML (Wu 
et al. 2022)

HIL-ML: state of 
the art (Mosqueira-
Rey et al. 2023a)

Covers end-to-end workflow of ML
Provides a clear theoretical foundation
Discusses adaptation to LLMs
Emphasizes user interaction and experi-
ence optimization
Shows innovative interaction design

✓
X
X
X

X

X

✓
X
X

X

Understanding 
interactions 
(Cui et al. 
2021)
X
X
X

✓

✓

Ours

✓
✓
✓
✓

✓

---

<!-- PAGE 6 -->

266  Page 6 of 55

ing such as Active Learning (AL), Interactive Machine Learning (IML), Machine Teaching 
(MT), Curriculum Learning (CL), and Explainable AI (XAI) (Mosqueira-Rey et al. 2023a). 
Their classification hinges on the locus of control within the learning process: active learn-
ing  with  the  system  in  control,  interactive  machine  learning  with  enhanced  user-system 
interaction, and machine teaching where human experts dictate the learning process. This 
work provides a delineation of the various interactions and demarcations among different 
HIL techniques, drawing connections and elucidating their influences. It offers a clear theo-
retical framework for researchers in the field, laying a foundational theory for the study of 
HIL. However, it does not address the challenges posed by LLMs, limiting its applicability.
Although the HIL-ML field has explored various interaction types like demonstrations 
and preferences, there is a notable lack of comparative analysis or guidelines for selecting 
the most effective type to solve specific learning problems. Yuchen Cui et al. have intro-
duced a set of principles for organizing HIL that examines how different interaction types 
affect  human  performance  and  the  quality  of  training  data  (Cui  et  al.  2021).  In  addition, 
they discuss strategies for selecting the most effective interaction type for particular learn-
ing issues and identify ongoing open questions in the field. While its focus on user-centric 
design is innovative, the survey covers a narrow scope, lacks concrete application scenarios, 
and provides minimal theoretical or experimental depth. Furthermore, it does not discuss the 
potential integration of LLMs with HIL systems, which limits its applicability in addressing 
contemporary challenges.

While previous reviews have comprehensively addressed the techniques, challenges, and 
future directions of HIL-ML, the advent of large models has introduced new dynamics and 
challenges into the HIL-ML landscape. Large models, equipped with extensive prior knowl-
edge, have reduced the reliance on human labor for traditionally labor-intensive tasks such 
as complex data labeling. Consequently, research in the era of large models has shifted its 
focus toward using human expertise for tasks like model fine-tuning, output validation, and 
high-level guidance. This shift has not only lowered the overall cost of HIL systems but also 
redefined the role of human involvement, making it more strategic and less resource-inten-
sive. To reflect these developments, we reviewed existing works and proposed an updated 
framework, Agent-in-the-Loop Machine Learning, which integrates human with large-scale 
models to address the evolving challenges in this domain.

2.2  Related research areas

There are several research fields closely related to AIL-ML, including but not limited to: 
HIL-ML,  Large  Models,  active  learning  and  knowledge  distillation.  We  briefly  describe 
them in the following.

Human-in-the-loop machine learning (Cui et al. 2021; Wu et al. 2022; Mosqueira-Rey 
et al. 2023a) is a method that integrates human knowledge to guide and enhance machine 
learning models. In HIL-ML framework, human participants contribute inputs not only dur-
ing data preprocessing, model training, and performance evaluation stages but also engage 
in  interactive  feedback  throughout  the  entire  machine  learning  workflow.  This  approach 
emphasizes the collaborative interaction between humans and algorithms with the goal of 
optimizing the learning process, thereby improving the accuracy, interpretability, and reli-
ability of the models. HIL-ML is particularly suited for tasks that are too complex for auto-
mated systems or require human intuition.

---

<!-- PAGE 7 -->

Page 7 of 55  266

Large model (Brown et al. 2020) typically refers to a type of machine learning model 
characterized by a substantial number of parameters, often scaling into the billions. These 
models, also known as large-scale models or foundation models (Bommasani et al. 2021), 
are designed to process and generate data across various tasks and domains. They leverage 
deep learning techniques and are predominantly neural network architectures such as trans-
formers (Vaswani 2017), which allow them to achieve state-of-the-art performance in areas 
like natural language processing and computer vision. Large models are famous for their 
ability to learn complex patterns and relationships within data, which facilitates advanced 
reasoning and generalization capabilities beyond specific tasks, contributing significantly to 
advancements in artificial intelligence.

Active  learning  (Settles  2009;  Mosqueira-Rey  et  al.  2023a)  is  a  machine  learning 
approach where the learner (often a model) selectively queries an oracle (typically a human 
annotator acting as a teacher) to label examples that are ambiguous but likely to provide sig-
nificant insights to the learning process. This targeted approach allows the learner to enhance 
their performance with fewer training examples. Active Learning is particularly effective in 
environments rich in unlabeled data where the annotation task is costly or time-consuming. 
This method strategically reduces the volume of data that needs labeling while maximizing 
learning efficiency and effectiveness. Active Learning is indeed a method within HIL-ML.

Knowledge  distillation  (Xu  et  al.  2024;  Gou  et  al.  2021;  Hinton  2015)  is  a  technique 
where knowledge is transferred from a larger, more complex model (often called the teacher) 
to a smaller, simpler model (often called the student). The goal of knowledge distillation is 
to enable the student model to achieve performance comparable to the teacher model but 
with reduced computational complexity and memory requirements. This is particularly use-
ful for deploying high-performing models on devices with limited resources, such as mobile 
phones and embedded systems. Knowledge distillation has become a popular method for 
model  compression  and  is  extensively  used  to  enhance  the  efficiency  of  deploying  deep 
learning models in resource-constrained environments.

3  Methodology

This  section  will  provide  a  detailed  introduction  to  the  implementation  of AIL-ML. As 
shown in Fig. 3, we categorize the existing work into two main parts: data acquisition and 
processing, and model development and optimization.

In data acquisition and processing, we discuss several key steps: first, during the data 
collection stage, we explain how agents participate in and optimize the data collection pro-
cess (Wu et al. 2020; Hiremath et al. 2022; Hancock et al. 2019; Xu et al. 2022; Long et al. 
2023; Ding et al. 2022; Xu et al. 2023; Sahu et al. 2023; Gao et al. 2023; Ye et al. 2022); 
second, in the data initialization stage, we explore how agents transform collected raw data 
into formats suitable for machine learning (Zhang et al. 2019; Oh et al. 2019; Kath et al. 
2023; Hsieh 2023b; Chen et al. 2021b; Cai et al. 2019; Park et al. 2023); next, during the 
data quality enhancement stage, we introduce how agents help improve the quality of data 
(Wu et al. 2020; Xu et al. 2022; Yu et al. 2015; Li 2017, 2017; Yao et al. 2019a; Liu et al. 
2021; Wallace et al. 2019; Bartolo et al. 2020; Arakawa et al. 2023; Cho et al. 2023; Wang 
et al. 2021; Hsieh et al. 2023a; Wang et al. 2023b; Dai et al. 2023; He et al. 2023a; Gao et al. 
2023); finally, in the data annotation stage, we explore how agents use their knowledge for

---

<!-- PAGE 8 -->

266  Page 8 of 55

Fig. 3  Taxonomy of Agent-in-the-Loop Machine Learning

precise and effective data labeling (Wu et al. 2020; Xu et al. 2022; Yu et al. 2015; Hancock 
et al. 2019; Hiremath et al. 2022; Li 2017; Zhang et al. 2019; Liu et al. 2021; Klie et al. 
2020; Qian et al. 2020; Kath et al. 2023; Hsieh 2023b; Hemmer et al. 2022; Cui et al. 2021; 
Koppol et al. 2021; Cai et al. 2019; Wang et al. 2021; Ding et al. 2022; He et al. 2023b; 
Hsieh et al. 2023a; Sahu et al. 2023; Wang et al. 2024; Lu et al. 2024).

In the model development and optimization part, the focus is on three core segments: 
firstly, we discuss how AIL-ML strategies effectively address the model cold start problem 
(Hiremath et al. 2022; Zhang et al. 2019; Wang et al. 2022; Ben-David et al. 2006; Zhuang 
et al. 2020; Xu et al. 2022; Arakawa et al. 2023; Wang et al. 2021; Ding et al. 2022; Xu et al. 
2023; Hsieh et al. 2023a; Ye et al. 2022; Li et al. 2024); secondly, during the model training 
phase, we detail how agents’ advanced knowledge is used to calibrate model parameters and 
optimize the learning framework (Arous et al. 2021; Oh et al. 2019; Kath et al. 2023; Wei et 
al. 2022; Wang et al. 2023a; Roels et al. 2019; Weber et al. 2020; Kwon and Michael 2023); 
and lastly, in the model iterative enhancement phase, we emphasize how continual interven-
tion and feedback from agents incrementally enhance the performance of machine learning 
models through multiple iterations (Wu et al. 2020; Hancock et al. 2019; Yao et al. 2019b; 
Qian et al. 2020; Stiennon et al. 2020; Ouyang et al. 2022; Crochepierre et al. 2022; Fan et 
al. 2024; Ahn et al. 2023; Arakawa et al. 2023; Ziegler et al. 2019; Xu et al. 2023; He et al. 
2023a; Sun et al. 2024; Klissarov et al. 2023; Guo et al. 2024).

By  introducing  the AIL-ML  concept,  we  effectively  leverage  the  strengths  of  human 
and large models to construct efficient, accurate, and adaptable machine learning models. 
Agents play a pivotal role in data acquisition and processing, as well as in model develop-
ment  and  optimization.  This  strategy  of  combining  human  wisdom  with  machine  power

---

<!-- PAGE 9 -->

Page 9 of 55  266

offers a new possibility for constructing efficient, precise machine learning models, pushing 
the technology to higher levels of achievement.

3.1  Data acquisition and processing

In the field of machine learning, data and models are intricately linked. The collection and 
initialization of data directly influence the construction and performance of models. More-
over, enhancing data quality is crucial for the iterative improvement of models. This inter-
action between data and models forms a mutually beneficial relationship, highlighting the 
importance of data quality in improving model performance. In this section, we investigate 
AIL-ML techniques that focus on optimizing the entire data lifecycle in machine learning. 
This includes a detailed examination of methods in the areas of Data Collection, Data Ini-
tialization, Data Quality Enhancement, and Data Annotation.

3.1.1  Data collection

In this section, we explore the data collection mechanisms within the AIL-ML framework, 
where agents can be humans, large models, or a combination of both. Agents play a crucial 
role in generating diverse, comprehensive, and representative data sets, essential for training 
complex machine learning models. This not only broadens the scope of training data but also 
enhances the model’s generalization capabilities and adaptability to complex environments.

3.1.1.1  Mathematical framework for data collection  In this part, we establish a foundational 
mathematical framework to systematically describe the data collection mechanisms within 
the AIL-ML architecture. This framework is summarized by the following general equa-
tions, which form the various data collection strategies discussed in subsequent sections.

xt = f (St, Dt, Mt, At)

(1)

where:

● xt represents the data generated by the agent at time t,
 ● St represents the seed datasets at time t,
 ● Dt and Mt represent the current dataset and model, respectively,
 ● At denotes the actions or decisions of the agent at time t, which may include inputs from

humans Ht and large models Lt,

● f  is a function defining how data is generated based on the current data set, model state,

agent state, and actions.

Additionally, the process by which agents generate data based on given labels can be for-
malized through a conditional probability model:

xt = p(x

|

y, St, Dt, Mt, At)

(2)

where:

---

<!-- PAGE 10 -->

266  Page 10 of 55

● xt is the data generated by the agent at time t,
 ● y is the provided label,
 ● p(x

|

y, St, Dt, Mt, At)  is  a  conditional  probability  distribution  indicating  the  likeli-
hood of generating data x given the label y, current seed dataset St, data set Dt, model 
state Mt, and agent actions At.

These  formulations  offer  a  comprehensive  description  of  data  collection  under  the AIL-
ML framework, illustrating how to utilize agents’ internal state, model state, and available 
data, along with potential external labels, to acquire data. This highlights the dynamic and 
adaptive nature of AIL-ML. In the subsequent sections of the chapter, each data collection 
strategy will be mapped to these general formulas.

Research analysis indicates that the AIL-ML framework utilizes three primary data col-
lection strategies, each corresponding to different stages of the machine model’s lifecycle. 
These strategies include data collection before model construction, during model construc-
tion, and after model construction.

3.1.1.2  Data collection before model construction  Before model construction, data collec-
tion is suitable for the following two scenarios. Firstly, these strategies are suitable for tasks 
that require highly specific data and lack large-scale public datasets (Long et al. 2023). For 
example, in the Internet of Things (IoT) context, various sensors are positioned at different 
locations. Due to the lack of public dataset, researchers need to collect the data. It is essential 
that the data should be not only abundant but also diverse and representative, to effectively 
capture the diverse potential states of the real-world environment. For instance, Hiremath 
et al. (2022) demonstrate how data is passively observed and collected through sensor net-
works installed in different locations within smart home systems. This network, containing 
door sensors, motion sensors, and temperature sensors, continuously monitors environmen-
tal changes and logs events with timestamps and sensor IDs. The data, stored in event logs 
on  local  servers  or  in  the  cloud,  forms  the  basis  for  subsequent  processing  and  analysis. 
Similarly, Wu  et  al.  (2020)  presented  a  system  that  automatically  collects  environmental 
sound  signals  through  smart  speakers. This  system  utilizes  unsupervised  clustering  tech-
niques to identify recurring activity types. Once the system can identify specific activities 
with high confidence, it starts a one-shot interaction with users through voice commands. 
This interaction is used to label these activities and create a labeled dataset. This approach 
allows the system to improve the accuracy of environmental sound recognition incremen-
tally through Continuous learning and in-situ training, without the need for predefined data. 
Consequently, it develops an accurate, environment-specific, acoustic signal-based activity 
recognition model. In this scenario, the data collection process can be modeled as:

xt = f (∅, ∅, ∅, At)

(3)

Here, ∅ indicates that the seed dataset St, the current dataset Dt and the model state Mt 
are not involved in the data generation process in this data collection strategy. This is due 
to the lack of this information before the model has been constructed. For convenience in 
expression throughout the remainder of this paper, ∅ will not be explained any more. At 
represents the user’s daily activities at time t. In this case, At represents the user’s daily

---

<!-- PAGE 11 -->

Page 11 of 55  266

activities, e.g., daily operations in the smart home, which generate corresponding data xt 
through sensor activation or sound recording. The function f defines how the sensor data is 
collected and generated based on the behavior At of the agent through sensor activations or 
sound recordings.

Secondly, data collection before model construction is suitable for tasks leveraging large 
models for data generation. Trained on vast amounts of data, large models have accumu-
lated extensive general knowledge and demonstrated remarkable abilities in reasoning and 
analysis. This allows researchers to use large models to generate high-quality data, signifi-
cantly reducing the time and costs. This enables both individuals and small organizations to 
utilize advanced AI technologies more effectively. Through well-designed prompt engineer-
ing, researchers can direct large models to generate specific datasets on demand, optimizing 
both the training process and model performance. Ding et al. (2022) proposed an approach 
named Prompt-Guided Training Data Generation (PGDG). This method leverages the gen-
erative capabilities of GPT-3 to produce labeled data pairs directly from specific prompts, 
significantly enhancing the efficiency and quality of data generation. For tasks such as senti-
ment analysis and relationship extraction, the data generated through this method matches 
or even surpasses the quality of manually annotated data with reducing time and cost. Addi-
tionally, large models can generate diverse data using seed datasets. In Xu et al. (2023), C 
Xu et al. detailed how to use seed datasets to collect high-quality, multi-turn dialogue data 
through self-chat. They chose platforms like Quora and Stack Overflow as seed datasets. 
These platforms provide a wealth of user-generated questions that guide the generation of 
dialogues by ChatGPT, which simulates both sides of a conversation. Each dialogue began 
with a seed question and naturally progressed through several rounds of exchanges until 
it  ended. To  ensure  the  quality  and  format  of  the  dialogues,  researchers  used  predefined 
templates to control the dialogue generation process. This method not only addresses the 
scarcity of high-quality, multi-turn dialogue but also offers a practical solution due to its 
efficiency and relatively low cost. To further enhance the diversity and quality of the gener-
ated data, researchers have designed various generation strategies (Ye et al. 2022; Gao et al. 
2023; Sahu et al. 2023), such as Greedy Search, Top-k Sampling, and Nucleus Sampling. 
These strategies aim to improve the diversity and quality of the generated text. Such inno-
vative techniques ensure that the data generated is both varied and of high quality, suitable 
for training robust models. This data generation process can be described by the equation:

xt = f (St, ∅, ∅, At)

(4)

where St represents the seed dataset, such as user questions from Quora and Stack Overflow 
in Xu et al. (2023). At denotes the agent’s actions, such as ChatGPT generating dialogues 
based on the seed questions. The function f  defines a function or process that generates data 
xt based on St and At.

3.1.1.3  Data collection during model construction  During model construction, the continu-
ous collection of data through agents can enable the model to better adapt and learn under 
complex or unfamiliar environmental conditions. Moreover, this can make model identify 
potential biases. In Hancock et al. (2019), data collection spans the entire lifecycle of the 
dialogue  model,  particularly  post-deployment. Through  real-time  interactions  with  users, 
the system continuously collects new training data, including Human-Bot (HB) dialogue

---

<!-- PAGE 12 -->

266  Page 12 of 55

data and user feedback data. When the model assesses high user satisfaction in a conversa-
tion,  the  user’s  responses  are  recorded  as  HB  dialogue  data.  Correspondingly,  when  the 
model anticipates potential errors, it requests feedback from users, which is then used to 
refine the model. This collected data, after processing and storage, is regularly utilized for 
retraining the model, enabling it to continually learn and improve in practical applications, 
thereby  enhancing  conversational  abilities  and  user  satisfaction.  This  approach  not  only 
reduces the dependency on manually annotated data but also allows the model to rapidly 
adapt to new conversational contexts, significantly improving user experience and model 
performance. The data collection process in this scenario can be represented by:

xt = f (∅, ∅, Mt, At)

(5)

In this context, Mt represents the state of the model at time t, such as the chatbot in Hancock 
et al. (2019). The state of the model evolves over time as more training data is accumulated 
and the model is updated. At denotes the agent’s actions, which include user interactions 
and feedback that generate new training data. And f is the core mapping function of the data 
collection process. In this context, it transfers the current model state Mt and agent’s action 
At to new training data xt.

3.1.1.4  Data collection after model construction  After model construction, the collection 
of data from agents can allow models to handle new types of tasks. For example, in ges-
ture recognition systems, allowing users to personalize their gestures can enhance gesture 
memorability, increase interaction efficiency, and improve accessibility for individuals with 
specific  needs.  Xu  et  al.  propose  a  framework  for  gesture  customization  using  few-shot 
learning, where users provide only a few custom gesture examples to the system (Xu et al. 
2022). This method enables the system to recognize customized gestures with high accuracy 
without compromising the performance of existing gestures. Specifically, users record new 
gestures on a smartwatch interface, and the system guides them through data collection via 
an interactive interface. The system continuously monitors performance and provides feed-
back to users. If the model’s accuracy falls below expectations, the system guides users to 
record more samples to further optimize the model. This data collection process can also be 
described by the equation:

xt = f (St, Dt, Mt, At)

(6)

where St is the seed dataset, such as negative samples (e.g., daily activities) and existing 
gestures.  Dt  represents  the  training  dataset  at  time  t,  which  evolves  as  new  customized 
gestures in Xu et al. 2022. Mt denotes the current model such as the gesture recognition 
model in Xu et al. 2022. And At stands for the agent’s actions, such as providing customized 
gesture data to the system in Xu et al. 2022. Through St, Dt and Mt, the system can prevent 
the agent’s custom gestures from being too similar to existing gestures, thereby avoiding 
overfitting to new gestures and forgetting old gestures. Additionally, by incorporating nega-
tive samples in St, the system can prevent conflicts between new gestures and the user’s 
daily activities.

---

<!-- PAGE 13 -->

Page 13 of 55  266

3.1.1.5  Analysis  of  data  collection  in AIL-ML  In  the  aforementioned  sections,  we  have 
provided  mathematical  representations  for  three  distinct  data  collection  strategies  corre-
sponding to different stages of the model lifecycle: before model construction, during model 
construction, and after model construction. These mathematical formulations vary in their 
functional structures and conditional elements, reflecting the unique data collection method-
ologies and technical characteristics inherent to each phase. By comparing these mathemati-
cal models, we can discern the specific features and limitations of each strategy, understand 
the trade-offs they entail, and identify the conditions under which the formulas might be 
extended to yield additional benefits.

Data Collection Before Model Construction primarily focuses on assembling comprehen-
sive and representative datasets necessary for initializing the model. At this stage, the data 
collection process is typically represented by the equations xt = f (At) or xt = f (St, At). 
Prior to model construction, researchers generally lack a trained model or sufficient existing 
data, rendering Mt and Dt either nonexistent or minimal. Consequently, data collection is 
primarily driven by external factors such as sensor monitoring, user activities, or data gen-
erated by large models based on seed datasets. The simplified function f (At) or f (St, At) 
reflects an externally driven data collection process, where user activities or prompts guide 
data generation without considering the model’s dynamic adaptation. This omission of Mt 
reduces the complexity but means that data quality and diversity rely only on external con-
ditions like activity patterns and the scope of seed datasets, lacking a feedback loop from 
the  model.  This  approach  offers  the  advantage  of  accumulating  substantial  data  prior  to 
model training, reducing potential data gaps in later stages, and leveraging large models to 
enhance data quality while minimizing annotation costs. However, the main challenge lies 
in designing effective data collection strategies and avoiding errors or biases in the data gen-
erated by large models. The absence of Mt leads to a more efficient and straightforward data 
generation process, but it sacrifices the ability to collect data tailored to the model’s evolv-
ing needs, highlighting the trade-off between simplifying data collection at the expense of 
adaptive data collection capabilities.

Data  Collection  During  Model  Construction  integrates  data  acquisition  into  the  train-
ing  process  itself.  During  this  phase,  the  data  collection  process  is  typically  modeled  as 
xt = f (Mt, At). Unlike the pre-construction stage, the model’s current state Mt plays a sig-
nificant role in guiding data collection. This phase utilizes real-time data generated through 
user interactions and user feedback. The model is in a transitional state, undergoing train-
ing or initial deployment with partial parameters and structures. The collected data reflects 
actual  usage  scenarios,  facilitating  rapid  model  adaptation  and  continuous  optimization. 
Incorporating Mt into the function allows data collection to be dynamically adjusted based 
on the model’s current performance and identified biases, facilitating continuous improve-
ment and adaptation. The key benefits include data that closely reflects deployment envi-
ronments,  enabling  rapid  iterations  and  mitigating  bias,  while  also  reducing  dependence 
on manual annotations. However, challenges related to data noise and variability in feed-
back quality remain, requiring robust feedback processing and ongoing model maintenance. 
Including Mt enhances data collection specificity and adaptability but introduces additional 
complexity. Real-time access to and processing of the model’s state require more advanced 
infrastructure, increasing both computational and operational overhead.

---

<!-- PAGE 14 -->

266  Page 14 of 55

Data Collection After Model Construction emphasizes the personalization and extension 
of the model’s capabilities to handle new tasks. In the post-construction phase, data collec-
tion is represented by xt = f (Dt, Mt, At), sometimes including St. This comprehensive 
formulation accounts for the existing dataset (Dt), the model’s state (Mt), and the agent’s 
actions (At). With a fully trained and deployed model, data collection focuses on personal-
ization and task extension. The existing dataset ensures consistency and prevents the model 
from forgetting previously learned information, while the model’s state guides the acquisi-
tion of new, relevant data. By integrating Dt and Mt, the system can effectively manage 
the  introduction  of  new  data,  ensuring  that  user-specific  data  do  not  overlap  excessively 
with existing data, thereby avoiding overfitting and maintaining overall model performance. 
Data collection mechanisms here are user-driven, with agents actively providing specific 
data samples based on performance feedback. This strategy allows for the addition of new 
tasks without degrading existing model performance by preventing overfitting to new data 
and forgetting previously learned information through the inclusion of negative samples. 
However, challenges include avoiding excessive bias towards individual users and ensuring 
a balanced integration of new data with existing knowledge.

The equation xt = f (St, Dt, Mt, At) can flexibly represent various data collection sce-
narios  by  selectively  omitting  certain  terms  based  on  the  specific  phase.  This  flexibility 
allows  the  framework  to  adapt  to  different  strategies  without  compromising  its  general 
applicability. Introducing additional terms such as Mt or Dt in specific contexts enables 
finer  control  and  optimization  of  data  collection  strategies.  For  example,  evolving  from 
f (At) to f (Mt, At) allows for model-driven data collection, enhancing iterative training 
and correction processes. From the analysis, we can derive the following high-level insights:

● Data  collection  strategies  can  align  with  the  model’s  lifecycle  stages.  Before  model 
construction, extensive data accumulation and generation are crucial for robust initial 
training.  During  construction,  real-time  data  collection  supports  continuous  learning 
and bias correction. After construction, personalized data collection enables the model 
to adapt to specific user needs and new tasks.

● Each phase involves trade-offs. Pre-construction strategies reduce annotation costs and 
ensure data diversity but require careful planning and quality control. During construc-
tion, real-time data accurately captures user interactions but introduces variability and 
noise.  Post-construction  strategies  enhance  personalization  and  adaptability  but  risk 
overfitting and require effective data management to preserve existing knowledge.
 ● Methodological versatility is essential, enabling researchers to select or combine strate-
gies based on task requirements, data availability, and resource constraints. This ensures 
data quality, diversity, and dynamic adaptability within the AIL-ML framework.

3.1.2  Data initialization and preprocessing

Data initialization and preprocessing are crucial steps that transform raw data into a format 
suitable for machine learning models. In this section, we will introduce the AIL-ML tech-
niques that initialize and preprocess data through agents.

---

<!-- PAGE 15 -->

Page 15 of 55  266

3.1.2.1  Mathematical framework for data initialization and preprocessing  How to utilize 
agents for data initialization and preprocessing can be described as follows:

Ft = ψ(Dt, At, Pf )

(7)

where:

● Ft represents the feature set derived at time t,
 ● as defined previously, Dt and At continue to denote the current data set and the agent’s

actions or decisions,

● function ψ serves as a data transformation function, incorporating all essential preproc-

essing steps such as data cleaning, normalization, and feature extraction,

● Pf  stands for the set of preprocessing parameters.

Upon  reviewing  AIL-ML  literature,  we  identified  two  main  methodologies  that  utilize 
agents for data initialization and preprocessing: Data Analysis and Feature Representation. 
These methodologies leverage agents to perform data analysis (Zhang et al. 2019; Hsieh 
2023b; Chen et al. 2021b), Wei et al. 2022 or to develop effective feature representation (Oh 
et al. 2019; Kath et al. 2023; Cai et al. 2019).

3.1.2.2  Data analysis  Data analysis by agents involves examining large datasets to discern 
underlying patterns and valuable insights that are not immediately apparent. This process is 
vital for preparing data in a way that significantly enhances the training and performance of 
machine learning models. Zhang et al. (2019) employed a high-recall regular expression to 
detect potential entity candidates within texts. Initially, experts design preliminary regular 
expressions suitable for specific entity extraction tasks, such as dates, email addresses, and 
course numbers, aiming to capture most target entities. Then, these expressions are used to 
scan documents, extracting all matching substrings. Each matched substring is expanded 
to  include  surrounding  text,  providing  sufficient  contextual  information  for  its  validation 
as a target entity. This method creates a collection of candidate substrings, encompassing 
all potential entities, significantly narrowing the scope of text that needs further process-
ing and thereby enhancing the efficiency of subsequent annotation and model training. For 
tasks that require expert knowledge, the AIL-ML strategy distills the deep knowledge and 
understanding of human experts into ML models through data analysis. Hsieh (2023b) lev-
eraged  expert  knowledge  in  the  data  initialization  and  preprocessing  stages. They  utilize 
chest  X-ray  images,  eye-tracking  data  from  radiologists,  and  patients’  clinical  data.  The 
eye-tracking data, which includes gaze points and sequences during the diagnostic process, 
is mapped to image coordinates to extract the visual search patterns of the radiologists. Con-
currently, clinical data is encoded and standardized to align dimensionally with 3D image 
data,  and  expanded  through  convolution  layers  for  effective  integration  with  image  data. 
Through these steps, the diagnostic behaviors and knowledge of human experts are effec-
tively distilled into the model, enabling it to learn from the experts’ diagnostic processes.

In this scenario, the data initialization and preprocessing can be formalized by Eq. 7. The

specific components of the formula are summarized in Table 2.

---

<!-- PAGE 16 -->

266  Page 16 of 55

Table 2  Symbol descriptions for 
data analysis

Symbol

Dt
At

Pf

HIL entity extraction (Zhang 
et al. 2019)
Text dataset
Design of regular expressions 
for entity extraction

Time allocation between con-
structing regular expressions 
and labeling data

Chest X-Ray diagno-
sis (Hsieh 2023b)
Chest X-ray images
Looking at the chest 
X-ray images during 
the diagnostic process
Parameters for 
data encoding and 
integration

3.1.2.3  Feature representation  On the other hand, agents are used for feature representa-
tion, which transforms raw data into a structured format more suitable for subsequent algo-
rithmic  processing.  This  transformation  ensures  that  the  data  are  formatted  to  maximize 
the  efficiency  and  accuracy  of  the  machine  learning  model.  In  Oh  et  al.  (2019),  agents’ 
interaction  and  feedback  play  important  roles  in  feature  representation.  Users  annotate 
video  frames,  for  instance  by  delineating  foreground  and  background,  providing  essen-
tial  feature  information.  These  annotations  are  used  to  generate  object  masks  and  serve 
as feature inputs to help the network and represent foreground objects. The user-provided 
data is then encoded into a format suitable for network processing, such as binary masks 
representing positive and negative examples. The interaction network combines this infor-
mation  with  video  frame  data  and  transforms  it  through  a  feature  encoding  module  into 
high-dimensional features suitable for model processing. Ultimately, these encoded data are 
integrated into a multi-channel input tensor for the interaction and propagation networks, 
ensuring the model effectively utilizes the initial information provided by users to enhance 
performance and prediction accuracy. Beyond low-dimensional data, agents can also repre-
sent feature for high-dimensional sensory data, such as images. Park et al. (2023) proposed 
Localized  Symbolic  Knowledge  Distillation  (LSKD),  a  framework  designed  for  efficient 
image feature representation. This framework leverages multi-modal large models to extract 
global image features, encompassing scenes, objects, and conceptual information, which are 
organized into Global Descriptors. Simultaneously, candidate regions within the image are 
identified, and fine-grained Local Descriptors are generated for each region using vision-
language  models. Additionally,  LLMs  generate  commonsense  knowledge  tied  to  specific 
regions, which is refined through a supervised"critic model"to remove inconsistencies. This 
approach effectively integrates global and local information. It also enhances semantic rep-
resentations through dynamic reasoning, providing robust inputs for subsequent inference 
and learning tasks.

Furthermore,  agents  can  optimize  feature  representation.  Kath  et  al.  (2023)  presented 
an  interactive  machine  learning  tool  for  annotating  passive  acoustic  monitoring  datasets 
created for wildlife monitoring. Users can select data points within a state-space representa-
tion and create new boundaries, further refining feature representation. Through real-time 
feedback, the model dynamically adjusts feature representations and prediction outcomes, 
gradually improving accuracy with each retraining cycle. Cai et al. (2019) developed tools 
that  helped  pathologists  cope  with  the  shortcomings  of  deep  learning  algorithms  during 
image retrieval. These tools are designed to adjust retrieval algorithms in real time to bet-
ter meet the diagnostic needs of doctors and enhance their trust in the algorithms. While 
using  the  SMILY  system,  pathologists  refine  and  optimize  image  feature  representations

---

<!-- PAGE 17 -->

Page 17 of 55  266

through tools like regional, example-based, and conceptual refinement. These tools allow 
pathologists to emphasize or remove irrelevant features, ensuring the model focuses on cor-
rect diagnostic features. This process of real-time interaction and feedback can be seen as 
a dynamic method of data preprocessing, aiding in the improvement of the model’s feature 
representation.

This kind of data initialization and preprocessing can be described by Eq. 7. A detailed

listing of the parameters involved is provided in Table 3

3.1.2.4  Analysis of data initialization and preprocessing in AIL-ML  We analyze two pri-
mary methodologies of data initialization and preprocessing in the AIL-ML literature: Data 
Analysis and Feature Representation.

Data Analysis  is  to  derive  richer  context  and  insights  from  raw  data. Agents  assist  in 
identifying critical patterns, candidate entities, and key structural elements that may not be 
easy to detect. For example, through expert-driven strategies such as hand-crafted regular 
expressions or the integration of human-derived signals (e.g., eye-tracking data from radi-
ologists), data analysis steps ensure that downstream ML models start from a more semanti-
cally meaningful and contextually informed baseline. Human expertise often guides data 
analysis through the design of rules or domain-specific entity extraction patterns. Agents 
can leverage human guidance to more efficiently sift through large datasets, reducing noise 
and focusing attention on key data segments.

Feature Representation focus on how to encode that information so it becomes directly 
usable  by  machine  learning  models.  Agents  and  users  collaboratively  shape  the  feature 
space  to  highlight  the  most  relevant  characteristics  of  the  data-refining  object  masks  in 
video frames, delineating meaningful acoustic signals from background noise, or emphasiz-
ing clinically significant image features. These approaches transfer high-dimensional data 
into representations that  enhance  learning performance. Agent feedback  can be real-time 
and iterative, allowing agents to refine, reshape, and optimize the feature space as the model 
trains.

3.1.3  Data quality enhancement

Data quality is important for model training and its subsequent performance. In this section, 
we explore AIL-ML methods related to enhance data quality. By identifying and correcting 
discrepancies, biases, and errors in raw data, agents significantly enhance the precision and

Table 3  Symbol descriptions for feature representation
User-guided video segmentation (Oh et 
Symbol
al. 2019)

Video frames
User annotations indicating foreground 
and background regions, directly influ-
encing the feature extraction process

HIL acoustic annotation (Hsieh 
2023b) and Human-centered medi-
cal tools (Cai et al. 2019)
Raw data
Real-time user feedback and 
interactions that guide feature 
refinement

Parameters related to mask generation

Parameters for feature 
optimization

Dt
At

Pf

LSKD 
(Park et al. 
2023)
Images
Generat-
ing global 
and local 
descriptions
Parameters 
for feature 
extraction

---

<!-- PAGE 18 -->

266  Page 18 of 55

consistency of the data. Moreover, agents play a key role in augmenting the diversity and 
richness of data

3.1.3.1  Mathematical  framework  for  data  quality  enhancement  To  explain  how  agents 
enhance data quality within AIL-ML framework, we adopt the following general formula:

Dt+1 = θ(Dt, At, Q)

(8)

where:

● Dt+1 denotes the enhanced dataset at time t + 1 after data quality enhancement,
 ● as defined previously, Dt and At continue to denote the current data set and the agent’s

actions or decisions,

● Q represents a set of parameters for data quality enhancement, defining specific quality 
control operations (e.g., noise thresholds, labeling consistency checks, or optimization 
strategies),

● θ represents a general-purpose function for enhancing data quality through a series of 
operations. These operations include data cleaning, data diversity enhancement by syn-
thesizing new samples and expanding the dataset, improving consistency and accuracy 
by adjusting mislabeled samples and reducing uncertainty and so on.

There are two primary AIL methodologies by which agents can enhance data quality: 1) 
improving data accuracy or consistency, (Wu et al. 2020; Yu et al. 2015; Li 2017; Arous et 
al. 2021; Arakawa et al. 2023; Cho et al. 2023; Gao et al. 2023, 2024) and 2) increasing data 
diversity (Xu et al. 2022; Yao et al. 2019a; Liu et al. 2021; Wallace et al. 2019; Bartolo et al. 
2020; Hsieh et al. 2023a; Dai et al. 2023).

3.1.3.2  Improving data accuracy  The first methodology focuses on improving the accuracy 
and  consistency  of  the  data.  For  machine  learning,  enhancing  data  precision  and  consis-
tency can improve model performance. The knowledge and analytical capabilities of agents 
can significantly augment data accuracy, thereby enhancing model precision. In the context 
of smart home environments, Cho et al. (2023) introduced a novel strategy named AI-to-
Human (AHA), which actively modifies environmental conditions to enhance the inferen-
tial accuracy of AI models. Unlike traditional smart devices, such as embedded vision AI 
sensors that passively monitor resident activities, AHA actively induces resident behaviors, 
facilitating more reliable AI inferences. Initially, AI sensors detect poor perception condi-
tions, such as orientations away from the camera or distances too close or too far from the 
camera.  Then,  the AHA  system  employs  smart  home  devices  like  speakers,  displays,  or 
ambient lighting to unremarkably guide resident behavior into more favorable perceptual 
conditions. The AHA system effectively improves data quality and overcomes the common 
challenges of passive perception inherent in traditional methods. Similarly, Listen Learner 
(Wu et al. 2020) employs an active learning approach that enhances data quality through 
various  interactive  strategies  with  users,  including  open-ended  questions,  confirmation 
questions, and refinement questions. When a new event falls into the decision boundary of 
the model, the system will ask a choice question as a confirmation question. This not only

---

<!-- PAGE 19 -->

Page 19 of 55  266

reduces the cognitive load on users but also enhances the quality of data, adapting dynami-
cally  to  different  environmental  sounds,  thus  improving  data  precision  and  the  accuracy 
of classification models. Furthermore, some AIL-ML methods enhance data precision by 
incorporating human reasoning. For instance, the MARTA framework (Arous et al. 2021) 
introduces human rationales combined with Bayesian methods to assess agent reliability, 
thereby enhancing data precision quality. Agents provide not only document labels but also 
rational segments supporting these labels. During training, the model weights these rational 
segments based on agent reliability, ensuring that high-quality rational segments contribute 
more.

Researchers  have  implemented  various  methods  to  manage  and  control  the  quality  of 
agent annotations. In LSUN (Yu et al. 2015), annotation quality control is achieved through 
several  strategies  including  redundant  annotations,  quality  checks,  and  detailed  annota-
tion  guidelines.  Specifically,  each  item  is  annotated  by  at  least  two  independent  annota-
tors to ensure consistency in the results. Items with known labels are embedded within the 
annotation  tasks  to  monitor  the  annotators’  performance.  Both  online  and  offline  quality 
control mechanisms ensure that annotators deliver high-quality results. Detailed annotation 
guidelines and examples help annotators understand the requirements of the task clearly. 
Together, these methods ensure the high quality and consistency of the annotated data.

Some  researchers  employed  agents  to  identify  and  correct  discrepancies,  biases,  and 
errors  in  raw  data,  significantly  enhancing  data  consistency  and  model  accuracy.  Gao  et 
al. (2024) proposed LLMIE-UHAR, which leverages Large Language Models (LLMs) and 
Iterative Evolution for Unsupervised Human Activity Recognition. This method capitalizes 
on the logical reasoning capabilities of LLMs to detect inconsistencies within datasets. This 
is particularly important for unsupervised learning where labels are absent. The effective-
ness of LLMIE-UHAR shows the potential of LLMs to improve data quality in real-world 
applications. This capability of agents to augment data quality forms a critical component in 
the development of more robust, efficient, and reliable machine learning systems.

There are some AIL methods that enhance data precision by reducing data noise. Ara-
kawa  et  al.  (2023)  proposed  PrISM-Tracker,  which  incorporates  human  input  to  manage 
data uncertainty. This framework actively interacts with user input when model predictions 
are uncertain, effectively reducing noise and uncertainty of data. Particularly in smart home 
environments, where sensor data may be noisy or the sequences of actions unclear. Addi-
tionally, to address the challenge of initial low-quality data generation by large models, Gao 
et al. (2023) introduced the SUNGEN framework, which uses language models to generate 
synthetic data with task descriptions and label information. This initial data often includes 
samples with incorrect labels or irrelevant content that can lead to model overfitting and 
reduced generalization. The SUNGEN framework fixes this by employing a dual-layer opti-
mization process: an inner loop optimizes model parameters using weighted cross-entropy 
loss, while an outer loop uses a noise-robust loss function to evaluate model performance 
on a synthetic validation set. This iterative process refines sample weights, enhancing the 
selection of high-quality data.

To make it clearer how the cited works integrate into Eq. 8, we present them in Table 4.

3.1.3.3  Enhancing  data  diversity  The  second  methodology  emphasizes  broadening  the 
range of data variability, which is vital for training robust models capable of performing

---

<!-- PAGE 20 -->

266  Page 20 of 55

Agent actions (At)

Table 4  Symbol description for methods emphasizing data accuracy and consistency
Data quality enhance-
Method
ment function (θ)
Detecting poor 
conditions and adjusts 
environment

Key parameters 
(Q)
Perception thresh-
olds, environment 
triggers

AHA (Cho et al. 
2023)

Modifying environ-
ment (e.g., lighting 
or orientation) to 
improve perception
Asking confirmation 
or refinement ques-
tions to users for 
uncertain events
Providing human 
rationales along with 
labels

Listen Learner 
(Wu et al. 2020)

MARTA (Arous 
et al. 2021)

Uncertainty 
bounds, question 
formats

Bayesian weight-
ing parameters

Identifying uncertain 
samples and refin-
ing labels via user 
feedback
Weighing agent reli-
ability and rationales 
to adjust final labels

LSUN (Yu et al. 
2015)

Providing multiple 
labels, with known-
label checks as a 
control

LLMIE-
UHAR (Gao et 
al. 2024)

Detecting and 
correcting dataset 
inconsistencies

Required an-
notations per 
item, known-
label embedding, 
online/offline QC 
thresholds
LLM prompts, 
logical constraints

PrISM-Track-
er (Arakawa et 
al. 2023)

Correcting the data 
when model predic-
tions are uncertain

Uncertainty trig-
gers, user feedback 
rules

SUNGEN (Gao 
et al. 2023)

Employs a dual-
layer optimization 
for synthetic data

Weighted cross-
entropy, noise-
robust loss

Merging annotator 
inputs and filters low-
quality labels

Using LLM reasoning 
to identify mis-
matched samples and 
correct them
Collects user clarifica-
tions to disambiguate 
noisy sensor data

Iteratively adjusts 
sample weights and 
filters out faulty 
synthetics

Output (Dt+1)

More accurate 
sensor data

Refined data-
set with reduced 
boundary noise

Refined labeling 
inDt+1, empha-
sizing high-qual-
ity rationales and 
improving overall 
data consistency
Consistent and 
high-quality data, 
reduced annotator 
errors

Logically consis-
tent data

Reduced noise 
and uncertainty in 
sensor readings, 
better clarity in 
time-series
Higher overall 
data quality, 
fewer mislabeled 
synthetic samples

well  across  diverse  scenarios.  Enhancing  the  diversity  of  data  can  not  only  improve  the 
generalization ability but also ensure superior performance on unseen samples of machine 
learning models.

Synthetic data generation is a prevalent method for enhancing data diversity in machine 
learning. This approach involves creating new data based on the characteristics of existing 
data to increase the diversity of the data available for model training. Liu et al. (2021) intro-
duced a method for global feature contribution analysis, which combined human evaluation 
to identify error features of the model. This method performs a local feature contribution 
analysis  and  quantifies  each  feature’s  contribution.  Subsequently,  it  calculates  the  global 
contributions of each feature to identify those with significant impacts on model predictions. 
Agents are employed to annotate and verify these global features, evaluating their contribu-
tion and correctness. This methodology not only improves the generalization capabilities 
of  the  data  but  also  model’s  performance  on  unseen  data,  enhancing  the  robustness  and 
reliability of model’s. Moreover, large models can synthesize data to increase diversity. In 
Hsieh et al. (2023a), after employing Chain-of-Thought prompting techniques, large models

---

<!-- PAGE 21 -->

Page 21 of 55  266

generate  natural  language  inferences  that  include  both  the  final  labels  and  detailed  inter-
mediary steps and logical explanations, providing richer and more useful training data for 
smaller models. The inferential content generated by large models significantly improves 
the context and detail quality of the training data.

By adding small perturbations to the original samples, adversarial examples can greatly 
reduce the accuracy of the original classifier and achieve the purpose of anti-deep learning 
Pan et al. (2020). Because past approaches expose superficial patterns, the resulting adver-
sarial  examples  are  limited  in  complexity  and  diversity.  To  address  these  shortcomings, 
Wallace et al. (2019) proposed an AIL-ML framework for generating adversarial examples. 
Researchers  have  applied  this  generation  framework  to  a  question  answering  task  called 
Quizbowl,  where  trivia  enthusiasts  craft  adversarial  questions.  The  questions  generated 
within this framework were tested through live human-computer matches, demonstrating 
that  while  these  questions  appeared  ordinary  to  human  participants,  they  systematically 
stump neural and information retrieval models. Agent-involved adversarial example genera-
tion is effective, which not only increases the diversity and complexity of the data but also 
enhances the models’ generalization capabilities (Bartolo et al. 2020).

Data  augmentation  plays  a  pivotal  role  in  enhancing  data  diversity.  Xu  et  al.  (2022) 
have developed a user-defined gesture recognition framework that requires participants to 
provide a few custom gesture examples. After acquiring these gestures, the system employs 
multiple data augmentation methods to generate additional samples: 1)zooming, to simulate 
different gesture speeds; scaling, to simulate different gesture strengths; time-warping, to 
simulate gesture temporal variance. Thus, these augmented samples increase the diversity 
of the data. Additionally, large models, pre-trained on extensive datasets, have been fine-
tuned with reinforcement learning from human feedback (RLHF) to generate text similar 
to human expression. Dai et al. (2023) utilized large models to generate diverse and high-
quality  textual  data  as  data  augmentation,  which  rephrases  each  sentence  in  the  training 
samples  into  multiple  conceptually  similar  but  semantically  different  samples.  The  aug-
mented samples can then be used in downstream model training. Data augmented through 
large models significantly boosts performance in few-shot learning tasks. This efficient and 
practical data augmentation method reduces reliance on manual annotation. This data aug-
mentation method is efficient and practical, reducing reliance on manual annotations.

These strategies demonstrate how researchers utilize AIL methods to realize data in data 
quality  enhancement  for  machine  learning,  ensuring  that  models  are  not  only  trained  on 
high-quality data but also adaptable to complex real-world environments.

Similarly, to clarify how these diversity-oriented approaches align with Eq. 8, we present

them in Table 5.

3.1.3.4  Analysis  of  data  quality  enhancement  in AIL-ML  As  discussed  above,  we  have 
introduced mathematical representations for two primary data quality enhancement meth-
odologies within the AIL-ML framework: Improving Data Accuracy and Consistency and 
Enhancing Data Diversity. These methodologies correspond to the Eq. (8). By comparing 
these methodologies across various aspects, we can gain a comprehensive understanding

---

<!-- PAGE 22 -->

266  Page 22 of 55

Table 5  Symbol description 
for methods emphasizing data 
diversity

Method

Agent ac-
tions (At)

Key param-
eters (Q)

HIL error 
detection 
(Liu et al. 
2021)

Annotating 
and verify-
ing global 
error 
features

Feature 
contribution 
thresholds, 
annotation 
rules, error 
detection 
criteria

Step-
by-step 
distilla-
tion (Hsieh 
et al. 
2023a)

AIL 
adversar-
ial exam-
ples (Wal-
lace et 
al. 2019; 
Bartolo et 
al. 2020)

Gesture 
augmenta-
tion (Xu et 
al. 2022)

Augpt (Dai 
et al. 2023)

Prompt 
design

Generating 
detailed 
reasoning 
steps

human 
interaction 
protocols, 
adversarial 
crafting 
strategies

Zoom fac-
tors, scaling 
intensity, 
time-warp 
parameters

RLHF 
fine-tuning 
configs, 
sampling 
settings

Crafting 
adversarial 
questions 
or inputs 
that inten-
tionally 
confuse 
models

Provid-
ing a few 
custom 
gestures 
from users, 
which 
are then 
augmented

Utiliz-
ing large 
models to 
rephrase 
or expand 
textual 
samples

Output 
(Dt+1)

A dataset with 
identified 
error features 
addressed, 
yielding better 
generalization 
and robustness

A refined 
dataset with 
enriched 
contextual

A dataset 
enriched with 
diverse and 
complex 
adversarial 
examples, im-
proving model 
robustness and 
generalization
A gesture da-
taset covering 
diverse speeds 
and strengths

A diversified 
text corpus 
with semanti-
cally varied 
samples

Data 
quality en-
hancement 
function (θ)
Refining 
data by 
combin-
ing feature 
contri-
bution 
analysis 
with human 
evaluation
Incor-
porates 
reasoning 
and expla-
nations into 
the original 
data
Generating 
adver-
sarial data 
to diversify 
training 
data

Applying 
various 
transfor-
mations 
(zoom, 
scale, 
warp) to 
user-
defined 
gestures
Using large 
models to 
generate 
multiple 
concep-
tually 
similar but 
semantical-
ly different 
variations 
of each 
sentence

of  their  distinct  roles,  advantages,  and  limitations  in  enhancing  data  quality  for  machine 
learning models.

Improving Data Accuracy and Consistency focuses on enhancing the precision and reli-
ability of the existing dataset by addressing errors, noise, and inconsistencies. This approach

---

<!-- PAGE 23 -->

Page 23 of 55  266

ensures that the data used for model training is accurate, thereby directly contributing to 
improved model performance. These methods can be detailed as follows:

● Correcting Mislabelled Samples: Utilizing agnet to rectify labeling errors.
 ● Label Refinement: Incorporating human rationales to enhance label quality.
 ● Consistency Checks: Implementing quality control mechanisms to ensure data consist-

ency.

These methods rely on quality control parameters, such as label accuracy thresholds, agent 
reliability metrics, and detailed annotation guidelines, to maintain high standards of data 
quality.  Consequently,  the  enhanced  dataset  Dt+1  is  characterized  by  higher  accuracy, 
reduced  noise,  and  greater  consistency,  which  will  enhance  the  model’s  precision  and 
reliability.

Enhancing Data Diversity aims to increase the variability and richness of the dataset to 
improve the model’s ability to generalize across diverse scenarios. This methodology intro-
duces new data samples or transforms existing ones to create a more varied dataset, thereby 
making the model more robust and adaptable. The specific strategies implemented include:

● Data Augmentation: Applying techniques such as scaling, time-warping, or zooming to

generate additional samples from existing data.

● Adversarial Example Generation: Creating challenging inputs designed to test and en-

hance model robustness.

● Synthetic  Data  Generation:  Utilizing  agent  to  produce  diverse  and  contextually  rich

training data.

These  methods  depend  on  specific  augmentation  parameters,  perturbation  strategies,  and 
prompt designs to ensure that the generated data effectively increases diversity while main-
taining quality. As a result, the enhanced dataset Dt+1 becomes more comprehensive and 
varied, thereby improving the model’s generalization capabilities and performance in real-
world applications.

Although improving data accuracy and enhancing data diversity have their own empha-
ses  in  the  framework  of AIL-ML,  they  complement  each  other  and  jointly  improve  data 
quality and model performance. The analysis them reveals several key insights:

● Complementary Objectives: Improving data accuracy ensures the reliability of the data-
set by minimizing errors and inconsistencies, which is essential for tasks requiring high 
precision. In contrast, enhancing data diversity broadens the dataset’s scope, enabling 
models to generalize better across varied and unseen scenarios.

● Different Agent Actions: Methods aimed at improving accuracy typically involve cor-
rective actions such as correcting mislabeled data, label refinement and removing incon-
sistencies. On the other hand, diversity enhancement methods focus on generating new 
samples, manipulating features, creating adversarial examples or transforming existing 
data through techniques such as data augmentation.

● Combining both methodologies leads to a dataset that is not only accurate and consist-
ent but also rich in diversity. High-accuracy data provides a reliable foundation, while 
diverse data ensures that the model can handle a wide range of inputs, enhancing overall

---

<!-- PAGE 24 -->

266  Page 24 of 55

performance and adaptability.

3.1.4  Data annotation

In  the  realms  of  deep  learning  and  machine  learning,  data  annotation  is  fundamentally 
crucial  due  to  the  dependency  of  model  learning  capabilities  on  extensive,  high-quality, 
annotated  datasets.  In  this  section,  we  introduce AIL-ML  methods  specifically  aimed  at 
enhancing the efficiency and accuracy of data annotation.

Initially, we present an overview of the current practices of agent-based annotation within 
the AIL framework, outlining how agents contribute to the data labeling process. Then, we 
explore  various  methodologies  focused  on  reducing  annotation  costs  and  increasing  the 
efficiency of the annotation process. The integration of these strategies ensures that the data 
annotation is not only cost-effective but also enhances the scalability and applicability of 
machine learning models in different applications.

3.1.4.1  Mathematical  framework  for  data  annotation  The  agent-assisted  data  annotation 
process within the AIL-ML framework can be modeled as an optimization problem, formu-
lated by the following equation:

Lt = γ(D′t, At, Σt, Ωt)

(9)

where:

● Lt represents the outputs at time t, which may include labels, confidence levels, and

explanations based on the output options Ωt.

● D′t denotes the subset of samples selected from the original dataset Dt for annotation.
 ● At is the inputs from the agent.
 ● Σt is a set of annotation strategies, such as fixed-choice, range selection, or open input, 
and how these strategies are implemented to reduce costs and increase efficiency.
 ● Ωt defines the output options, specifying which additional information should be gener-

ated.

● γ is the comprehensive annotation function responsible for generating the desired an-
notated data based on the selected samples St, agent inputs At, the annotation strategies 
Σt and the output options Ωt.

This  formulation  ensures  that  the  data  annotation  process  is  not  only  cost-effective  but 
also scalable and applicable to various machine learning models in different applications. 
By incorporating intelligent agent strategies, AIL-ML systems can enhance efficiency and 
reduce costs associated with data annotation.

---

<!-- PAGE 25 -->

3.1.4.2  Annotation methods categorized by degree of freedom  As illustrated in Fig. 4, the 
common methods used for annotation can be classified into three types based on the degree 
of freedom each method provides: fixed-choice, range selection, and open input.

Page 25 of 55  266

● The fixed-choice method, which offers the least freedom, requires agents to select from 
at least two predefined options. This is the most commonly used and universally ap-
plicable  annotation  method,  offering  minimal  cognitive  burden  to  agents  but  lacking 
flexibility compared to other methods (Wu et al. 2020).

● Range  selection,  offering  more  freedom  than  fixed-choice,  includes  choosing  within 
discrete or continuous sequences. Discrete sequences consist of clearly distinguishable 
units, such as text, while continuous sequences, like image pixels or signal durations, 
lack  clear  units  (Cai  et  al.  2019;  Xu  et  al.  2022).  In  these  instances,  individual  data 
points may not contain complete meaning on their own (e.g., pixels). For some unstruc-
tured data, researchers utilize dimension reduction to visualize the data on a graphical 
interface, allowing agents to select ranges by drawing boundary boxes on spectrograms 
to manually annotate events (Kath et al. 2023).

● The open input method provides the highest degree of freedom, where agents can input 
self-defined text. This method enables the generation of rich, diverse annotations, such 
as  dialogues  (Hancock  et  al.  2019)  or  rules  (Zhang  et  al.  2019).  Open  input  annota-
tions are particularly beneficial for tasks requiring complex data interpretation, allowing 
agents to offer detailed information that enhances model training and performance.

3.1.4.3  Strategies for reducing annotation costs  The reduction of annotation costs within 
the AIL-ML framework is a prominent research focus. Annotation for certain tasks can be

Fig. 4  Classification of annotation methods based on the degree of freedom. The fixed-choice method 
provides minimal freedom with predefined options for selection. Range selection allows choosing within 
discrete or continuous sequences, offering more flexibility. The open input method provides the highest 
degree of freedom, allowing free text input

---

<!-- PAGE 26 -->

266  Page 26 of 55

costly, demanding considerable time, energy, and expertise from annotators. As described in 
Fig. 5, the AIL-ML framework utilizes three kinds of strategies to reduce annotation costs:

1.  Data: selecting the most valuable samples for annotation to reduce the number of items

needing labels.

2.  Process Optimization: optimizing the annotation process to enhance efficiency.
3.  Agent: deploying hierarchical levels of agents to carry out these tasks, thereby dimin-

ishing the overall annotation costs.

3.1.4.4  Data: selecting the most valuable samples  In the context of enhancing efficiency 
in  machine  learning,  selecting  the  most  valuable  samples  for  agents  to  annotate  can  sig-
nificantly reduce the number of data points that need to be labeled. One effective approach 
is the cluster-then-label method, which reduces the volume of data needing annotation by 
selecting representative samples for labeling, as discussed in the works of Wu et al. (2020) 
and Hiremath et al. (2022) This approach uses unsupervised clustering to identify key data 
points that are then annotated, thus diminishing the overall volume of data requiring manual 
labels. In scenarios where the system can accurately recognize certain activities, it may initi-
ate a one-shot interaction for annotating such behaviors, thereby creating a labeled dataset. 
Data  points  with  low  confidence  or  high  uncertainty  in  current  ML  models  are  deemed 
highly  informative  and  prioritized  for  annotation.  In  parallel,  Qian  et  al.  introduced  the 
PARTNER  system  (Qian  et  al.  2020),  which  predicts  labels  for  all  unannotated  entities 
using the current model and ranks them based on uncertainty, focusing annotation efforts 
on the most uncertain instances. Following annotation, similar instances are identified and 
assigned pseudo-labels based on the annotated data, thereby augmenting the training dataset 
efficiently. This strategy effectively combines user involvement with model training, mini-
mizing the need for extensive manual annotations. Furthermore, boundary samples present 
classification challenges due to the inherent features of multiple categories. To address this, 
Sahu et al. (2023) introduced a method where large models re-annotate boundary samples to 
ensure accurate classification, thus enhancing both the accuracy and generalization capabil-
ity of the training models.

All the methods discussed above can be integrated into our proposed Eq. 9. Table 6 illus-

trates how each approach aligns with specific elements of our framework.

Fig. 5  Three primary strategies for reduce annotation costs within the AIL=ML framework. The strategies 
include: selecting the most valuable data samples, optimizing data interaction processes and leveraging 
diverse agents

---

<!-- PAGE 27 -->

Page 27 of 55  266

Σt

Ωt

Fixed-choice

Labels

Table 6  Symbol description for methods selecting the most valuable samples
Method

γ

At

Lt

D′t
Cluster centroids 
as representatives

Human 
labeling

Labels for 
selected 
clusters

A cluster-
ing step and 
a manual 
labeling step

Cluster-
then-
label (Wu 
et al. 2020; 
Hiremath et 
al. 2022)
PART-
NER (Qian 
et al. 2020)

Labels, par-
tial pseudo-
labels and 
confidence 
scores

Model pre-
diction, user 
correction 
and labeling

High-uncertainty 
instances for user 
labeling; others 
pseudo-labeled

Human 
labeling

Fixed-choice

Prompt-
Mix (Sahu 
et al. 2023)

Enhanced 
labels for 
classifica-
tion tasks

Boundary 
data gen-
eration and 
LLM-based 
re-labeling

Gener-
ated boundary 
samples via LLM

Data gen-
eration and 
re-labeling

Fixed-choice

Table 7  Symbol description for methods optimizing the annotation process
Method

γ

At

Lt

HIL entity 
linking (Klie 
et al. 2020)

Labels 
for entity 
linking 
tasks

LSUN (Yu et 
al. 2015)

Class 
labels

Recommenda-
tion algorithm 
and adaptive 
candidate 
ranking
Iterative anno-
tation pipeline

D′t
Samples selected 
by recommenda-
tion system

Human 
labeling

Σt

Fixed-choice

Selected via k-
means clustering 
and classifier 
confidence

Human 
labeling

Fixed-choice

Label 
and con-
fidence 
for 
pseudo-
labeled 
data
Labels 
with 
explana-
tions

Ωt

Labels 
with 
recom-
mended 
scores
Labels

3.1.4.5  Process  optimization:  optimizing  the  annotation  process  Optimizing  the  annota-
tion process to reduce workload and cost while enhancing efficiency is also a key focus in 
current research. Klie et al. (2020) have effectively utilized recommendation algorithms to 
propose potential concepts and adaptively prioritize candidates. Their approach has been 
proven to increase the speed of annotation by 35%, with users expressing a strong prefer-
ence for this system. Similarly, in the LSUN project led by Yu et al. (2015), the develop-
ment of an efficient graphical user interface significantly lightens the annotation load and 
enhances  productivity.  This  interface  focuses  the  annotator  on  a  single  image  at  a  time, 
providing thumbnails of previous and next images to ease understanding and reduce naviga-
tion time. Enhancements such as full-screen image display improve the visibility of visual 
details, leading to more accurate annotations. Moreover, the introduction of simplified key-
board shortcuts, like using the space bar for classification, greatly enhances the efficiency of 
operations. These interface innovations not only boost the efficiency of data annotation but 
also substantially lower the costs involved, providing robust support for building extensive 
image datasets.

Table 7 summarizes how each referenced work maps on Eq. 9.

---

<!-- PAGE 28 -->

266  Page 28 of 55

3.1.4.6  Agent: deploying hierarchical levels of agents  In the context of AIL-ML, agents 
can be categorized into three distinct types: LLMs, general users, and domain experts. As 
shown in Fig. 6, general users hold general knowledge, which is broad and encompasses a 
wide array of basic facts across various domains. LLMs, on the other hand, are trained on 
trillions of data points from extensive databases, encompassing not only general knowledge 
but also a significant amount of database-specific information. Domain experts stand out by 
their possession of both general knowledge and highly specialized expert knowledge, spe-
cific to their particular field of study. It is important to note that the knowledge capacity of 
LLMs is limited by the nature of their training data, which is generated by humans and may 
not cover the depth of expertise that domain experts achieve through specialized education 
and experience. Thus, the knowledge ceiling of LLMs is typically considered to be below 
that of domain experts.

Upon training with datasets consisting of trillions of data points, LLMs have developed 
capabilities that include reasoning, semantic understanding, grounding, and planning. These 
capabilities suggest that LLMs could serve effectively as proxies for humans in AIL con-
texts, potentially reducing the substantial costs associated with manual labor (Hsieh et al. 
2023a; He et al. 2023b). Researchers like Wang et al. (2021) have explored the use of GPT-3 
as  a  cost-effective  tool  for  data  annotation.  By  generating  pseudo-labels  through  GPT-3, 
this approach offers a more economical and faster alternative to traditional manual labeling 
methods. Compared to manual annotation, the use of GPT-3 can reduce costs by 50% to 
96%, owing to its ability to generate labels more swiftly and at a lower cost.

Various studies have explored strategies for distributing annotation tasks among different 
agent types, employing a multi-level agent architecture to lower annotation costs effectively 
(Wang et al. 2023b; He et al. 2023a). LLMs show considerable efficacy in handling tasks 
with limited label spaces, significantly reducing manual annotation costs and reaching qual-
ity levels akin to human annotations under specific conditions. However, their performance 
is less robust in scenarios with extensive labeling requirements and complex relationships 
(Ding et al. 2022). To optimize both cost and quality, integrating LLMs with human annota-
tors proves beneficial, particularly for critical tasks. Shuohang Wang and his team (Wang 
et al. 2021) have leveraged GPT-3 to generate pseudo-labels and their corresponding con-

Fig. 6  Three types of agents in the AIL-ML framework: general users, LLMs, and domain experts. Gen-
eral users hold general knowledge across various domains. LLMs are enhanced by training on extensive 
databases, holding both general and substantial database-specific knowledge. Domain experts, combine 
general  knowledge  and  expert  knowledge,  establishing  them  at  the  highest  level  of  knowledge  within 
their specific fields

---

<!-- PAGE 29 -->

Page 29 of 55  266

fidence scores, allowing for selective human re-annotation of labels that demonstrate low 
confidence. This strategy significantly decreases the dependency on human resources with-
out compromising the quality of annotations, which is particularly critical when working 
within limited budgets on large-scale datasets. While LLMs offer efficiency and cost savings 
in generating annotations, their performance on complex or domain-specific tasks is typi-
cally flawed and may introduce biases relative to human annotations. To address these chal-
lenges, Wang et al. (2024) have introduced a collaborative method that utilizes the strengths 
of LLMs and human annotators to enhance annotation accuracy and reliability at low costs. 
This approach involves LLMs producing initial labels and explanations, followed by a vali-
dation model that evaluates these labels, with human annotators subsequently focusing on 
the instances scored lowest by the validation model. The LLM-generated explanations pro-
vide  additional  context  that  aids  human  annotators  in  refining  and  improving  the  labels, 
thus cost-effectively ensuring high-quality annotations. Annotating multimodal data, such 
as text and images from social media, is often chanllenged by its complexity and noise. To 
address these issues, Feihong Lu et al. proposed the Miko framework (Lu et al. 2024). This 
framework  leverages  the  collaboration  of  multimodal  large  language  models  (MLLMs), 
LLMs, and humans to achieve high-quality annotations. The process starts with MLLMs 
generating detailed image descriptions to refine and validate textual content, thereby reduc-
ing noise and enhancing multimodal data representation. Subsequently, LLMs extract and 
classify users’ potential intentions based on key dimensions such as concepts, actions, and 
emotions. Finally, human reviewers verify the generated intentions, ensuring their quality 
and relevance through systematic scoring. By combining the strengths of machine intelli-
gence and human judgment, Miko not only improves annotation efficiency but also enriches 
models’ understanding of user intentions, offering robust support for downstream tasks like 
recommendation systems and sentiment analysis.

In  recent  studies,  expert  agents  have  been  utilized  to  create  rules  that  significantly 
decrease the amount of data that needs to be annotated, thereby reducing costs associated 
with data labeling (Li 2017; Zhang et al. 2019). Zhang et al. (2019) developed a method 
where human experts use regular expressions to establish initial rules, generating weakly 
labeled data. While this data might contain noise, it serves as a valuable asset for the early 
stages of model training, particularly effective when labeled data are scarce. This approach 
accelerates the annotation process, improving the quality of ML models. However, when 
there is an abundance of labeled data, deep neural networks excel at uncovering more intri-
cate dependencies in the data. Data derived from regular expressions typically show lim-
ited  diversity  and  are  strongly  rule-oriented,  making  them  suitable  primarily  in  the  early 
stages of model training where labels are deficient. Hemmer et al. (2022) have explored a 
coordinated approach between classifier systems and expert agents. In their system, clas-
sifiers  are  trained  to  pinpoint  cases  that  are  difficult  for  human  experts  to  handle,  while 
an  assignment  system  efficiently  allocates  each  case  to  the  most  suitable  agent,  whether 
human or machine. This approach has been evaluated in several studies, including experi-
ments with"synthetic"experts and a real medical dataset annotated by multiple radiologists. 
Research indicates that this method outperforms previous approaches and provides more 
accurate results than either the best human experts or classifiers alone.

All these methods can be incorporated into our proposed Eq. 9. Table 8 provides an over-

view of how each method corresponds to different elements of our framework.

---

<!-- PAGE 30 -->

266  Page 30 of 55

Table 8  Symbol description for methods deploying hierarchical levels of agents
Method

γ

At

Lt

GPT3 for La-
beling (Wang 
et al. 2021)

LLM labels 
and human 
corrections

Labeling pipe-
line with GPT-3 
inference and 
human review

D′t
Low-
confidence 
subset

Human-LLM 
Annota-
tion (Wang et 
al. 2024)

HITL En-
tity Extrac-
tion (Zhang et 
al. 2019)

Labels and LLM 
explanations

LLM labeling 
and human 
re-labeling

Low-verifi-
cation-score 
data

Entity labels

Uncertainty 
data

Regex-generated 
weak labels 
and annotation 
on uncertain 
samples

Human-AI 
Teams (Hem-
mer et al. 
2022)
Miko (Lu et 
al. 2024)

Collaborative 
labels

Image descrip-
tions, key 
information and 
user intentions

Joint training 
pipeline for 
optimal team 
performance
Multi-stage an-
notation process

Dynamic 
samples

Clean, 
complete, 
and multi-
modal data 
(text + 
images)

Σt

Active 
labeling

Collabora-
tive label-
ing strategy

Collabora-
tive label-
ing strategy

Collabora-
tive label-
ing strategy

Multi-step 
annotation 
strategy

Ωt

Labels 
and con-
fidences

Labels, 
explana-
tions 
and veri-
fication 
scores
Labels 
with 
confi-
dence 
scores

Labels

Labels, 
explana-
tions, 
and 
intent 
classifi-
cations

GPT-3 pre-
dictions (la-
bels, logits) 
and human 
corrections
LLM outputs 
(labels, ex-
planations) 
and human 
corrections

Experts 
designing 
regex rules 
and general 
user labeling 
on uncertain 
samples
Multiple 
human ex-
perts and AI 
models
MLLM 
for image 
descriptions, 
LLM for key 
information 
extraction 
and intent 
generation 
and two-
stage human 
validation

3.1.4.7  Analysis  of  data  annotation  in AIL-ML  In  this  section,  we  introduce  three  data 
annotation  methods  categorized  by  degree  of  freedom:fixed-choice,  range  selection,  and 
open  input.  Fixed-choice  accelerates  labeling  but  may  overlook  details;  range  selection 
enhances  granularity  at  the  expense  of  increased  effort;  and  open  input  captures  deeper 
insights  though  it  risks  inconsistency  or  noise.  For  other  researchers,  an  effective  choice 
depends on matching the method’s flexibility to the complexity of the data and the goals of 
the annotation task, suggesting that assessing trade-offs between expressivity and cognitive 
burden is essential.

Selecting the Most Valuable Sample strategies aimed at minimizing redundant labeling. 
By identifying the most informative or representative items-for instance, via cluster-then-
label methods or uncertainty-based sampling-researchers can focus human resources where 
they  are  most  needed,  reducing  overall  annotation  volume  without  compromising  model 
performance. This selective approach ensures that each labeled instance contribute to train-
ing while preventing time-consuming manual labeling of uninformative samples.

Optimizing the Annotation Process emphasizes reveals that annotation efficiency is not 
only  about  data  but  also  the  manner  in  which  data  is  presented  and  processed.  Innova-

---

<!-- PAGE 31 -->

Page 31 of 55  266

tions like dynamic recommendation algorithms, adaptive interfaces, and simplifying agent’s 
workflows  can  yield  substantial  gains  in  speed  and  consistency.  However,  implementing 
these optimizations often requires iterative user testing and interface refinement. This high-
lights the importance of balancing technical algorithms and agent factors.

Deploying  Hierarchical  Levels  of Agents  can  utilize  the  advantage  of  different  agent 
types. LMs provide rapid, cost-effective pseudo-labeling but may introduce biases or errors 
if left unchecked, while domain experts can resolve intricate cases at a higher per-annotation 
cost. General users fill in the middle ground, handling moderately challenging tasks. This 
layered design encourages thoughtful distribution of effort and expertise but also requires 
continual calibration-researchers must ensure that each agent level is invoked where it adds 
value rather than extraneous complexity.

Effective data annotation relies on combining data selection, data sampling, workflow 
optimization,  and  appropriate  agent  collaboration.  Each  component  must  work  together, 
such as aligning data selection with interface design or involving experts to handle chal-
lenging edge cases. By integrating these elements, researchers can reduce labeling effort and 
ensure high-quality annotations, ultimately supporting the development of reliable machine 
learning models.

3.2  Model development and optimization

For machine learning, the development and optimization of models are also important. The 
methodologies adopted during the model development phase significantly impact the effec-
tiveness and efficiency. Moreover, continual refinement and optimization are essential for 
the enhancement of model performance. In this section, we investigate AIL-ML techniques 
that concentrate on model development and optimization. This includes a comprehensive 
analysis  of  methods  in  the  areas  of  Model  Cold  Start  Issue,  Model  Training,  and  Model 
Iterative Enhancement.

3.2.1  Model cold start issues

In machine learning, the model cold start problem refers to the challenge of initializing a 
model effectively when minimal or no historical data is available. This issue is particularly 
prevalent for machine learning that is data-driven. The lack of initial training data can sig-
nificantly lower model performance. In this section, we will explore various AIL-ML meth-
ods that address the model cold start problem, aiming to improve the effectiveness when 
models begin the learning process.

3.2.1.1  Mathematical framework for model cold start issues  Given the initial state

M0 and minimal or no historical data at time t = 0, how to utilize AIL-ML framework to

address model cold start issue can be defined as:

M1 = χ (M0, σ (A0, Pgen) , Pcold)

(10)

where:

---

<!-- PAGE 32 -->

266  Page 32 of 55

● M0 is the model’s initial state which is usually untrained or only configured.
 ● σ(A0, Pgen) represents the data generation function, influenced by agent’s input A0 and

data generation parameters Pgen.

● Pcold are the parameters specifically designed for rapid adaptation during the cold start

phase.

● χ is the cold start learning function, which is responsible for integrating the data gener-
ated by the agent with the learning parameters, and quickly updating the state from M0 
to M1.

After reviewing the relevant literature within the AIL-ML domain, we have identified two 
primary approaches to solve the cold start problem: 1) employing agents to generate an ini-
tial dataset, and 2) utilizing transfer learning and domain generalization techniques. The first 
approach involves using agents to generate the data that can serve as a preliminary train-
ing set. This leverages the agents’ capabilities to simulate realistic data scenarios that help 
bootstrap the model’s learning process. The second approach involves applying knowledge 
gained from one or more source domains to a target domain where data are scarce. This 
method not only addresses the scarcity of data in new applications but also enhances the 
model’s ability to generalize across different domains, thus providing a robust foundation 
for model training even in the absence of extensive domain-specific data.

3.2.1.2  Employing agents to generate an initial dataset  During the model cold start phase, 
a high-quality initial dataset is necessary for model training. Agents can provide or generate 
initial dataset, thus addressing the cold start problem. Large models can generate the data 
needed for initial training, enabling smaller task-specific models to begin training without 
data. Therefore, large models can resolve the cold start issue by supplying or creating initial 
training data (Ye et al. 2022). Wang et al. (2021) demonstrated how large models can be 
used to generate annotated data, rapidly assembling an initial dataset to overcome the cold 
start problem. Especially in low-resource settings, the label data produced by large mod-
els provide sufficient information. Large models can shorten the time of acquiring initial 
annotated data through few-shot learning. Additionally, the cost of using large models for 
data annotation is significantly lower than that of human annotation, which helps to quickly 
acquire  large-scale  high-quality  annotated  data  with  limited  budgets.  These  high-quality 
initial annotations can accelerate the early training process, enabling the model to quickly 
initiate  from  a  cold  start.  Besides  generating  data  labels,  large  models  can  also  produce 
inferences  (Hsieh  et  al.  2023a).  By  leveraging  inferences  and  labels  generated  by  large 
models, smaller models can gain rich contextual information and task knowledge from the 
start of training. This effectively addresses the cold start problem, allowing small models to 
quickly achieve better performance with limited training data. Large models significantly 
reduce the time and financial costs associated with acquiring high-quality datasets, provid-
ing  a  more  feasible  option  for  individuals  or  small  organizations  to  utilize  advanced AI 
capabilities (Ding et al. 2022).

We demonstrate in Table 9 how each referenced study corresponds to the symbols and

in Eq. 10.

---

<!-- PAGE 33 -->

Table 9  Symbol description for 
methods employing agents to 
generate an initial dataset

Page 33 of 55  266

Method

χ

GPT-3 for 
label-
ing (Wang 
et al. 2021)
Distilling 
Step-by-
step (Hsieh 
et al. 2023a)
GPT-3 for 
annota-
tion (Ding 
et al. 2022)

Using LM to 
generate init 
dataset

Integrating 
LM’s rationales 
to train the 
smaller model
Integrating 
GPT-3-generat-
ed dataset into 
the training loop 
to bootstrap the 
model

σ (A0, Pgen)
Generating dataset by 
LM in low-resource 
scenes, providing init 
training dataset
Generating rationales 
from the LM, expand-
ing dataset with step-
by-step explanations
Data generation meth-
ods (PGDA, PGDG, 
DADG) producing 
dataset for cold-start 
training

Pcold
Few-shot 
prompting 
strategies

Multi-task 
distillation 
parameters

Prompt 
configura-
tions and 
knowledge-
base usage 
parameters 
to enhance 
data quality

3.2.1.3  Utilizing  transfer  learning  and  domain  generalization  techniques  The  second 
approach to resolve the model cold start issue involves leveraging transfer learning, where 
knowledge from one or more well-resourced source domains is applied to a target domain 
that lacks sufficient data. This method not only addresses the scarcity of data in new appli-
cations but also enhances the model’s ability to generalize across different domains, thus 
providing a robust foundation for model training even in the absence of extensive domain-
specific data. Similarly, experts can utilize domain generalization to adjust models based 
on diverse tasks. This method involves learning from one or several related but different 
domains, allowing the model to generalize well to an unseen domain. Theoretical insights 
from Jindong Wang and Ben-David support this approach by indicating that invariant fea-
ture  representations  across  domains  ensure  the  generalizability  and  transferability  of  the 
model  (Wang  et  al.  2022;  Ben-David  et  al.  2006).  Consequently,  experts  may  utilize  the 
pretraining-finetuning strategy within transfer learning to adapt the model to new settings 
effectively (Zhuang et al. 2020).

3.2.1.4  Analysis of model cold start issues in AIL-ML  Employing agents to generate an 
initial dataset can effectively address the model cold start problem, particularly when work-
ing with limited or no labeled data. LLMs can rapidly produce training samples or annota-
tions, effectively training smaller models that would otherwise lack a representative dataset. 
Although the dataset may contain biases or errors from LLM, this method greatly lowers 
labeling effort and speeds up model deployment. Moreover, LM have the ability to create 
large-scale data at low cost, which helps smaller organizations that cannot afford expensive 
human annotation.

Meanwhile, utilizing transfer learning and domain generalization addresses cold starts 
from a different angle, emphasizing the transfer of robust, pre-learned feature representa-
tions from well-resourced domains to domains with sparse data. By aligning model param-
eters and feature spaces across different tasks or domains, researchers can equip a newly 
deployed  model  with  strong  priors  that  enable  quick  adaptation,  even  if  domain-specific

---

<!-- PAGE 34 -->

266  Page 34 of 55

data are scarce. Transfer learning provides a theoretical and empirical backbone for acceler-
ating cold starts, but its efficacy depends on the compatibility of source and target domains.
LLM-driven dataset creation directly addresses the absence of labeled data by quickly 
supplying training examples, while transfer learning and domain generalization reuse exist-
ing  knowledge  to  guide  model  parameter  initialization.  Researchers  must  balance  these 
approaches according to resource availability, domain similarity, and the potential overhead 
of data cleaning or adaptation.

3.2.2  Model training

In machine learning, the model training process involves the adjustment of model param-
eters using optimization algorithms. This procedure involves the selection of the model’s 
architecture, the loss function, and the optimizer to ensure effective learning. The model’s 
architecture influences the model’s capacity to capture relevant patterns in the data. More-
over,  the  loss  function  ensures  that  the  model’s  predictions  align  closely  with  the  actual 
outcomes. Similarly, the choice of optimizer affects the efficiency and speed with which the 
model converges to a solution. Agents can leverage their deep understanding of the prob-
lem, thereby offering essential insights to enhance model performance.

3.2.2.1  Mathematical framework for model training  The model training process, integrat-
ing agent’s insights into it, can be defined as follows:

Mt+1 = ϕ(Mt, Dt, At, Θt)

(11)

where:

● Mt and Mt+1 represent the model states at time t and t + 1, respectively.
 ● Dt is the training dataset at time t.
 ● At includes inputs from the agent, which may suggest modifications to the model archi-

tecture, loss function, or optimization strategy.

● Θt  encompasses  the  set  of  training  parameters,  which  integrates  training  parameters

with the insights provided by the agent.

● ϕ is the model update function that not only applies conventional optimization algo-
rithms but also integrates the agent’s guidance to achieve more effective learning and 
improved model performance.

Generally, AIL-ML framework integration in model training is in two ways: 1) agents use 
knowledge to optimize model training or 2) agents can be designed as a component of the 
machine learning network architecture.

3.2.2.2  Leveraging  agent  knowledge  for  optimized  model  learning  Agents  can  leverage 
their  knowledge  to  guide  the  design  and  training  of  models,  ensuring  that  these  models 
effectively capture the core patterns of the tasks. Agents can influence several aspects of 
model development, including selecting the appropriate model framework, loss functions, 
and optimization algorithms, as well as adjusting the training procedures such as the number

---

<!-- PAGE 35 -->

Page 35 of 55  266

of training iterations or epochs (Kath et al. 2023; Tchemeube et al. 2023). Roels et al. (2019) 
developed an AIL approach to address the explosion of data sets due to 3D technology in 
electron microscopy)(EM). They created an interactive graphical user interface that allows 
biologists to use the framework in an intuitive and user-friendly fashion. Experts directly 
interact with the model through this graphical interface to evaluate the performance of vari-
ous models and choose the most suitable one. Additionally, experts can select regions of 
interest  and  set  parameters  to  optimize  the  model,  ensuring  the  efficiency  and  reproduc-
ibility of the algorithms. A recent study by Metsch et al. (2024) provides a compelling dem-
onstration of integrating interactive graphical interfaces in the context of biomedical data. 
They introduced the CLARUS platform, an explainable AI tool designed for graph neural 
networks (GNNs) in the biomedical domain. CLARUS enables experts to manually modify 
patient-specific protein-protein interaction networks and evaluate the impact of these modi-
fications on GNN predictions through counterfactual analysis. This interactive process not 
only enhances the understanding of the model’s decision-making but also allows experts 
to retrain the model based on their domain knowledge, improving its interpretability and 
performance.

For ease of reference, Table 10 compiles the key elements of these approaches in relation

to Eq. 11.

3.2.2.3  Designing agents as architectural components in ML  Agents can be designed as a 
component of the machine learning network architecture. These agents continuously pro-
vide real-time feedback that adjusts the model’s behavior, thereby optimizing the training 
outcomes. Some researchers incorporated agents directly into the network architecture. Such 
designs allow the model to learn and adapt during training actively from agents, enhanc-
ing model’s ability to adjust internal feature representations based on agent inputs Wei et

Table 10  Symbol description 
for methods leveraging agent 
knowledge for optimized model 
learning

Method

ϕ

HITL in electron 
microscopy (Roels 
et al. 2019)

CLARUS (Metsch 
et al. 2024)

Executing 
the de-
noising 
algorithm 
with 
specified 
parameters 
based on 
expert 
input
Integrat-
ing expert 
modifica-
tions into 
the GNN 
training 
process, 
enabling 
analy-
sis and 
retraining

Θt
De-
noising 
algo-
rithm 
parame-
ters such 
as filter 
size and 
iteration 
count
GNN 
hyper-
param-
eters

Dt
3D EM 
image and 
expert-
specified 
Regions of 
Interest

Synthetic 
graph da-
taset and 
Patient-
specific 
protein-
protein 
interaction 
(PPI) 
networks 
from gene 
expression

At
Expert 
interac-
tions via 
the GUI, 
including 
algorithm 
choice and 
parameter 
adjustments

Expert 
modifica-
tions to the 
protein-
protein 
interaction 
networks, 
such as 
adding/
removing 
interactions 
based on 
domain 
knowledge

---

<!-- PAGE 36 -->

266  Page 36 of 55

al. 2022 Some researchers embedded agents into the network architecture as core elements 
by the interactive mechanisms and feedback loops (Oh et al. 2019; Weber et al. 2020). Oh 
et  al.  (2019)  presented  a  method  for  interactive  video  object  segmentation  where  agents 
annotate video frames (e.g., through scribbles). These annotations are utilized by an interac-
tive network to generate initial masks for foreground objects. The agent’s annotations not 
only serve as input to the interactive network but also continuously influence the network’s 
outputs through multiple rounds of interaction and feedback. Similarly, Wang et al. (2023a) 
introduced H-Gen, an automatic H-DNN compression framework that incorporates human 
input as a new hyperparameter for accurate and efficient DNN generation. When the model 
exhibits low confidence in certain inputs during training, the agent is triggered to gener-
ate precise label data for these samples. The H-DNNs generated by H-Gen outperform the 
original DNNs in terms of accuracy, latency, and energy consumption, significantly improv-
ing performance in resource-constrained environments. Large models can also be used as 
a component of the network (Kwon and Michael 2023; Ye et al. 2023). Kwon and Michael 
(2023) integrated LLMs into reinforcement learning frameworks as proxy reward functions. 
They input natural language prompts into the LLM. Then LLM evaluates the behavior of 
reinforcement learning (RL) agents based on the prompts and produces textual outputs as 
reward signals. These reward signals are subsequently parsed into numerical reward signals, 
which are utilized by the RL agents to update their strategies and undertake new training 
iterations. Although designing effective prompts requires careful consideration, the contex-
tual learning capability of the LLM allows it to capture human-like behavioral priors from 
minimal examples. This capability facilitates the efficient generation of reward signals that 
are well-aligned with the user’s objectives, thus training RL agents more effectively.

To provide a consolidated view, Table 11 organizes each referenced work according to

the parameters in Eq. (11).

3.2.2.4  Analysis  of  model  training  in  AIL-ML  Leveraging  Agent  Knowledge  for  Opti-
mized Model Learning demonstrates how agents refinie model training. By offering expert-
driven adjustments to model architecture, loss functions, and optimization strategies, agents 
ensure that models are tailored to capture the relevant patterns within complex datasets. This 
approach allows for more effective training, particularly in specialized domains where auto-
mated methods alone may fall short. Integrating agent expertise can lead to more targeted 
learning processes.

Designing Agents as Architectural Components in ML explores the integration of agents 
directly into the machine learning pipeline. This approach enables real-time feedback and 
adaptive learning, allowing agents to continuously influence the model’s behavior during 
training.  By  embedding  agents  within  the  network  architecture,  models  can  dynamically 
adjust their internal representations based on ongoing interactions and feedback.

The  effective  incorporation  of  agents  into  the  model  training  process  is  many-sided, 
requiring both the strategic utilization of agent expertise and the architectural embedding of 
agents within the learning framework. Moreover, this comprehensive approach encourages 
the development of models that can swiftly adapt to new challenges.

---

<!-- PAGE 37 -->

Table 11  Symbol description 
for methods designing agents as 
architectural components in ML

Page 37 of 55  266

Method

ϕ

User-guid-
ed video 
segmenta-
tion (Oh et 
al. 2019)

H-
Gen (Wang 
et al. 
2023a)

Processing 
agent feed-
back to 
refine and 
propagate 
masks with 
multi-
round 
training
Integrating 
agent into 
the DNN 
training 
process by 
knowledge 
distillation

Reward 
design 
with 
LM (Kwon 
and 
Michael 
2023)

Utilizing 
the LM’s 
output as 
reward to 
update the 
RL model

Dt
Video frames 
for object 
segmentation

Image

At
Providing 
annotations(e.g. 
scribbles) on 
video frames 
to guide model 
refine

Generating pre-
cise labels for 
low-confidence 
samples

User prefer-
ence text data

Generating 
reward signals 
for RL model 
training

Θt
Param-
eters of 
interac-
tive and 
propa-
gation 
net-
works

Param-
eters 
for 
H-DNN 
com-
pres-
sion 
and 
optimi-
zation
Param-
eters 
of RL 
model 
and the 
integra-
tion of 
agent

3.2.3  Model iterative refinement

The development of machine learning models is an iterative process that depends on con-
tinuous assessment and refinement. In real-world long-term machine learning systems, data 
changes over time. This is an important feature to consider, especially in systems that last 
for months or even years (Chen et al. 2021a). Therefore, when deployed for a long time, 
models frequent retraining and adjustments to maintain accuracy and relevance. Further-
more, the process of evaluating discrepancies between model predictions and actual out-
comes  generates  crucial  feedback,  which  is  fundamental  to  the  iterative  enhancement  of 
models. AIL-ML offers robust solutions to address these challenges. In this section, we will 
explore various AIL-ML methods that specifically focus on model iterative enhancement. 
AIL-ML methods facilitate the continuous integration of feedback into the learning cycle, 
enabling models to adapt proactively to changes in data patterns and environmental condi-
tions. This not only helps in fine-tuning the models based on real-time data but also enhances 
their ability to generalize across varying contexts and over time. By embedding agents that 
can assess, adjust, and refine model parameters continuously, AIL-ML systems ensure that 
machine  learning  models  remain  effective  and  responsive  to  the  evolving  nature  of  real-
world data, thereby sustaining their performance and relevance in long-term deployments.

---

<!-- PAGE 38 -->

266  Page 38 of 55

3.2.3.1  Mathematical framework for model iterative refinement  The iterative enhancement 
of the machine learning model under the AIL-ML framework can be mathematically repre-
sented by the following formula:

Mt+1 = ψ(Mt, Dt, At, Λt)

(12)

where:

● Mt and Mt+1 represent the model at time t and t + 1.
 ● Dt is the dataset at time t, which may evolve over time reflecting changes in data pat-

terns.

● At  denotes  the  feedback  obtained  from  agent,  evaluating  the  discrepancies  between

model predictions and actual outcomes.

● Λt encompass es a set of parameters guiding the model update process.
 ● ψ is the model update function that integrates both traditional data-driven updates and 
agent-based insights to adaptively refine the model in response to changing conditions.

3.2.3.2  Model iterative refinement based on human feedback  Incorporating human feed-
back into model iterations significantly enhances alignment with human intentions, particu-
larly within the field of NLP (Ahn et al. 2023). The use of AIL frameworks is essential in this 
context, as they enable models to navigate complex linguistic structures, cultural subtleties, 
and linguistic variations. Without the involvement of human expertise, machine process-
ing  tends  to  be  simple  and  rigid.  Retzlaff  et  al.  (2024)  further  emphasize  that  reinforce-
ment  learning,  inherently  a  Human-in-the-Loop  paradigm,  greatly  benefits  from  iterative 
processes integrating human preferences. This perspective aligns with the core principles 
of AIL  frameworks,  underscoring  the  pivotal  role  of  human  feedback  in  refining  models 
and  adapting  to  dynamic  environments.  For  instance,  in  dialogue  tasks,  human  involve-
ment is crucial to define conversational goals and maintain alignment with expected behav-
iors,  especially  in  dynamic,  user-driven  contexts.  Recent  advancements  demonstrate  that 
integrating human preference feedback through reinforcement learning effectively refines 
models via iterative enhancements (Ziegler et al. 2019; Stiennon et al. 2020; Ouyang et al. 
2022; Crochepierre et al. 2022; Fan et al. 2024). This method typically begins with develop-
ing a reward function trained on human feedback to capture task-specific priorities. Itera-
tive fine-tuning then adjusts policies to better reflect these priorities. Retzlaff et al. (2024) 
highlight the critical role of explainability and trust-building mechanisms in such iterative 
processes,  as  they  enable  productive  human-agent  interaction  and  ensure  models  remain 
adaptable to evolving user needs. For example, Ying Fan et al. proposed using online rein-
forcement learning to fine-tune text-to-image models. In this setup, the model continually 
generates new samples and adjusts its generation strategies based on human feedback (Fan 
et al. 2024). This online and iterative enhancement process heavily relies on the continuous 
input of human feedback, enabling gradual improvements with each iteration. The model 
enhances the quality and alignment of the generated images to better reflect human inten-
tions.  Direct  quality  assessments  provided  by  humans  train  the  reward  function,  thereby 
increasing both the accuracy and consistency of the model. This feedback assists in handling 
complex  generation  tasks,  such  as  creating  scenes  with  multiple  objects  or  specific  attri-

---

<!-- PAGE 39 -->

Page 39 of 55  266

butes like color, quantity, and placement, ensuring that the images accurately reflect the text 
descriptions. Human feedback also significantly extends the model’s generalization capabil-
ity, as it incorporates a broad spectrum of scenarios and descriptions, thus improving the 
model’s adaptability to various applications. Further, human inputs allow for ongoing opti-
mization, helping the model avoid local optima and adapt to new user demands in real-time, 
reducing training data biases and enhancing the fairness and quality of the outputs. Follow-
ing a similar methodology, Daniel M. Ziegler et al. have refined language processing tasks 
with a reward model derived from human preferences, overcoming the constraints imposed 
by fixed evaluation metrics such as BLEU or ROUGE (Ziegler et al. 2019). This strategy 
better aligns the model with genuine human linguistic practices and perceptions, thereby 
enhancing  the  model’s  learning  signals  and  exploratory  directions,  significantly  boosting 
the efficiency of model iterations and the quality of outputs (Crochepierre et al. 2022).

Models  can  enhance  their  performance  through  active  learning  and  interactive  refine-
ment,  leveraging  human  knowledge  to  identify  and  correct  their  gaps,  uncertainties,  or 
errors (Wu et al. 2020; Hancock et al. 2019; Qian et al. 2020). Arakawa et al. (2023) pro-
posed PrISM-Tracker, a multimodal procedure tracking framework that employs wearable 
sensors and state transition data for user-driven error and uncertainty resolution. This frame-
work actively queries users to address uncertainties encountered during tracking, showcas-
ing a method that combines active learning with time series analysis to enhance accuracy. 
User input allows the model to continually correct errors and optimize performance during 
practical usage, consistently obtaining high-quality annotated data. By dynamically updat-
ing the model, it adapts more effectively to user habits and environmental changes, reducing 
long-term uncertainties and enhancing the robustness and predictive accuracy of the system. 
Similarly in the paper (Yao et al. 2019b), the authors improve the performance of semantic 
parsing by incorporating user feedback, thus enabling iterative model enhancement. In each 
iteration, the model generates preliminary SQL queries and assesses uncertainties through 
an error detector, subsequently generating clarifying questions for the user. User feedback is 
then used to confirm or correct the model’s predictions, with the model updating its current 
state based on this feedback and re-predicting uncertain segments. After multiple iterations, 
the model progressively adapts to the patterns of user feedback, minimizing unnecessary 
queries and improving parsing accuracy.

We  summarize  in  Table  12  how  the  methodologies  cited  correspond  to  the  variables

defined in Eq. (12).

3.2.3.3  Model  iterative  refinement  based  on  large  model  feedback  Despite  the  success 
achieved  by  model  iteration  enhancements  through  human  feedback,  reliance  on  human 
supervision introduces challenges such as the high cost of manual oversight and issues related 
to quality, reliability, diversity, consistency, and potential biases. In response, researchers 
have turned to using feedback from LLMs to enhance models for more complex tasks (He 
et al. 2023a). Canwen Xu et al. have developed a method known as Self-Distillation with 
Feedback (SDF), which utilizes feedback from LLMs for iterative enhancement and fine-
tuning of models (Xu  et al. 2023). In  this approach, a  trained question-answering  model 
generates four distinct responses for each input prompt. These responses are then evaluated 
by ChatGPT based on usefulness, relevance, accuracy, and detail, with the highest-scoring 
response selected for further model fine-tuning. Fine-tuning employs newly introduced low-

---

<!-- PAGE 40 -->

266  Page 40 of 55

Table 12  Symbol description for 
model iterative refinement based 
on human feedback

Method

ψ

Reinforcement 
learning via 
human feed-
back (Ziegler 
et al. 2019; 
Stiennon et al. 
2020; Ouyang 
et al. 2022; 
Crochepierre et 
al. 2022; Fan et 
al. 2024)
PrISM-track-
er (Arakawa et 
al. 2023)

RL-based 
iterative up-
date, guided 
by human 
preference 
feedback

Refining 
model output 
based on user 
feedback

Dt
Text 
data; 
image-
to-text 
data

At
Providing 
preference 
feedback to 
the output of 
the model

Λt
RL 
hyper-
param-
eters

Correcting 
the model’s 
predictions 
at uncertain 
moments

Multi-
modal 
data from 
wearable 
sensors 
(motion 
+ audio) 
and state 
transition 
graph

Param-
eters 
for 
weight-
ing 
user 
feed-
back, 
query 
fre-
quency, 
etc
Thresh-
olds for 
error 
detec-
tion, 
query 
fre-
quency, 
etc

Model-based 
interactive 
semantic pars-
ing (Yao et al. 
2019b)

Confirming 
or correcting 
uncer-
tain SQL 
segments

Text-
to-SQL 
dataset 
(Wiki-
SQL, 
Spider, 
etc.)

Generating 
preliminary 
model out-
puts, detect-
ing errors, 
querying the 
user, and cor-
recting model 
outputs

rank adaptation modules that update only the low-rank matrices in the model’s linear layers, 
enabling efficient parameter tuning while avoiding the high computational costs associated 
with training reward models. This method enhances model performance by achieving fine-
grained optimization, capturing subtle feedback differences, and reducing the risk of cata-
strophic forgetting. It also offers significant advantages in training efficiency and resource 
utilization. Given that LLMs can partially substitute for human input, some researchers, like 
Martin Klissarov, have proposed reinforcement learning based on feedback from large mod-
els (Klissarov et al. 2023). Klissarov introduced a novel approach called “Motif,” which 
uses the prior knowledge of LLMs to construct intrinsic reward functions for RL agents, 
facilitating the learning of preferences. Researchers evaluate model outputs using LLMs, 
generate preference datasets, and then train reward models to fine-tune the original mod-
els. The intrinsic rewards generated by LLM significantly enhance model performance in 
complex tasks and guide the model to produce behaviors consistent with human intuition.

LLMs have the distinct capability to blend high-level knowledge into specialized models 
and ensure that model outputs are aligned with human ethical values and intentions (Guo 
et al. 2024). In this context, Sun et al. (2024) proposed the SELF-ALIGN method, which 
leverages principle-driven reasoning with the generative strengths of LLMs to enable AI 
agents to self-align with minimal human intervention. This method employs a set of manu-

---

<!-- PAGE 41 -->

Page 41 of 55  266

ally  defined  principles  to  direct  the  LLM’s  response  generation,  greatly  diminishing  the 
reliance on human supervisors. The team has developed 16 principles that specify the ideal 
characteristics of system-generated responses. These principles act as a framework for pro-
ducing responses that are not only useful but also ethical and dependable. Through a process 
of fine-tuning, these principles are incorporated into the LLM’s parameters, allowing the 
model to autonomously generate responses that adhere to these guidelines, eliminating the 
need for direct application of the principles and examples.

These approaches can be systematically integrated into the proposed framework. Table 13

details how each method relates to the terms of Eq. (12).

3.2.3.4  Analysis of model iterative refinement in AIL-ML  In Model Iterative Refinement, 
the kernel challenge lies in keeping a model’s performance and adaptability over extended 
deployments. Equation (12) highlights how a model transitions from one state

Mt to another Mt+1 by assimilating new data Dt and agent feedback At under specific 
update parameters Λt. By integrating feedback directly into the update loop, models evolve 
in response to both shifts in data distributions and performance gaps identified during real-
world usage.

Model  Iterative  Refinement  Based  on  Human  Feedback  refines  model  behavior  and 
resolve ambiguities, harnessing a key strength of humans to make context-sensitive judg-
ments. Although manual correcting can be costly or easy to variability, it also delivers a high 
degree of interpretability and domain expertise. This feedback loop is particularly potent in 
tasks where purely algorithmic metrics (e.g., BLEU scores in language tasks or standard 
accuracy measures) fail to capture domain-specific or user-centric nuances. Iterative refine-

Table 13  Symbol description for 
model iterative refinement based 
on large model feedback

Method

ψ

Baize (Xu et 
al. 2023)

Motif (Klis-
sarov et al. 
2023)

SELF-
ALIGN (Sun 
et al. 2024)

Iterative self-
distillation 
process select-
ing highest-
scoring 
response, then 
fine-tuning 
via LoRA
Updating RL 
model using 
a combined 
reward 
(intrinsic 
from LLM + 
extrinsic from 
environment)
Principle-
driven 
self-alignment 
procedure 
incorporat-
ing the 16 
principles

Dt
Generated 
candidate 
responses

Environ-
ment data

Expert-
defined 
principles 
and seed 
prompts

Λt
LoRA 
adapta-
tion 
param-
eters

RL 
hyperpa-
rameters

At
Ranking 
candidates 
to use 
the best 
response 
for model 
fine-tuning

Providing 
preference 
feedback 
to the 
output of 
the model

Principle-
driven 
feedback 
by LM 
(replacing 
extensive 
human 
supervision

Param-
eters or 
strategies 
for incor-
porating 
these 
principles 
into the 
model

---

<!-- PAGE 42 -->

266  Page 42 of 55

ment not only improves immediate performance but also reveals new data facets or user 
needs over time, leading to gradually richer and more accurate models.

Model Iterative Refinement Based on Large Model Feedback-where LLMs supply itera-
tive feedback signals-extends scalability by partially or entirely substituting human. This 
approach retains a continuous learning loop but relies on LLMs as proxies for human judg-
ment, offering faster turnaround and reduced manual overhead. Although such model-gen-
erated feedback can accelerate refinements, it also introduces potential biases or knowledge 
gaps  originating  from  the  LLM  itself. Therefore,  researchers  need  to  balance  the  conve-
nience and scalability of automated feedback against the risk of recursive error propaga-
tion, ensuring that checks and balances remain in place to maintain reliability and ethical 
alignment.

4  Overview of application domains

4.1  Applications in general knowledge domain

In the domain of general knowledge within AIL-ML, various innovative applications have 
been developed to enhance computational experiences, making them more enriching, help-
ful, and adaptable to specific deployment environments.

In the context of intelligent home environments, the incorporation of AIL-ML is gradu-
ally  reshaping  the  interaction  dynamics  between  users  and  automated  systems,  enabling 
these systems to better understand and adapt to user behaviors through iterative feedback 
loops. As shown in Fig. 7, this adaptation process leverages real-time data and agent inputs 
to continuously refine and optimize the performance of smart home devices. Bootstrapping 
methods for Human Activity Recognition in smart homes initiate with passive observation, 
gradually building activity models through minimal supervision, thereby recognizing fre-
quent activities with significant precision (Hiremath et al. 2022). Additionally, applications 
such as the “Listen Learner” (Wu et al. 2020) leverage user interactions for activity recogni-
tion, minimizing user effort while enhancing system adaptability to specific environments. 
The PrISM-Tracker framework (Arakawa et al. 2023) employs wearable sensors and graph-
based state transitions, coupled with user inputs, to refine procedure tracking, addressing 
uncertainties in real-time. The AI-to-Human Actuation (Cho et al. 2023) approach actively 
makes user modify environmental conditions to improve the robustness of visual AI sensors, 
aligning system responses with human activities more accurately. Additionally, Jiayuan Gao 
et al. proposed LLMIE-UHAR (Gao et al. 2024), a method that leverages LLMs and itera-
tive evolution to achieve unsupervised HAR. In an IoT environment, multiple smart devices 
generate vast streams of data. These data not only consist of raw information but also con-
tain rich contextual and semantic information, such as the background, time, location, and 
interactions between devices. LLMIE-UHAR uses prompt engineering to transform sensor 
data into textual descriptions rich in contextual information, making it comprehensible to 
LLMs. Then, the LLM is used for analysis and inference, enabling precise annotation of 
the sensor data. These applications highlight the integration of agent insights with machine 
learning algorithms to enhance smart home ecosystems.

In the intelligent dialogue systems domain, the focus is on refining conversational agents 
to offer more human-like interactions through advanced natural language processing and

---

<!-- PAGE 43 -->

Page 43 of 55  266

Fig. 7  Frameworks of AIL-ML application in smart home environments. a Arakawa et al. (2023): Over-
view of PrISM-Tracker architecture which utilizes a transition graph and user-provided simulated oracles 
to enhance the robustness and accuracy of HAR systems in procedural tracking. b Hiremath et al. (2022): 
Overview of our bootstrapping method. Phase 1 involves representation learning and clustering to iden-
tify action units. Phase 2 focuses on discovering higher-level features, and Phase 3 involves deploying the 
activity detection method within the smart home environment. c Wu et al. (2020): Listen Learner architec-
ture, a self-supervised algorithm that detects salient acoustic events and generates classifiers for activity 
recognition, effectively minimizing user involvement. d Gao et al. (2024): Overview of LLMIE-UHAR 
that leverages large language models and iterative evolution to realize unsupervised HAR. e Cho et al. 
(2023): An example of how AI-to-human actuation complements an AI sensor under perception difficulty. 
Note: The figures provide a rough conceptual understanding, and the text is not intended to be read in full 
detail. The figures are borrowed from the following papers: (a) Arakawa et al. (2023), (b) Hiremath et al. 
(2022), (c) Wu et al. (2020), (d) Gao et al. (2024), (e) Cho et al. (2023)

context management. The use of AIL-ML is key, enabling these systems to learn from user 
interactions and improve over time (Hancock et al. 2019). AIL-ML can not only efficiently 
utilize real-time conversational data for training but also dynamically adjust based on user 
feedback and satisfaction, leading to an improvement in both the overall model performance 
and user experience.

---

<!-- PAGE 44 -->

266  Page 44 of 55

4.2  Applications in specialized knowledge domain

4.2.1  Medicine and healthcare

The significance of AIL-ML is increasingly recognized in specialized fields such as medi-
cine or healthcare (Budd et al. 2021). Despite the promising capabilities of large language 
models in medicine, the enhancement of Clinical Decision Support systems and complex 
clinical  areas  requires  the  incorporation  of  human  insights  through  AIL  methodologies. 
As shown in Fig. 8a, in (Liu et al. 2023), clinical decision support logic summaries were 
provided  to  ChatGPT,  an  AI-based  question-and-answer  tool  developed  from  large  lan-
guage models, to generate recommendations. These AI-generated recommendations were 
reviewed by multiple clinicians and found to be high in understanding and relevance. How-
ever,  they  scored  lower  in  terms  of  utility,  acceptance,  bias,  inversion,  and  redundancy. 
In applications like Medical Decision-Making, particularly with image retrieval systems, 
machine learning algorithms fall short of capturing the nuanced understanding of similarity 
as perceived by experts. This gap led to the development of a tool named SMILY (Cai et 
al. 2019). It can be observed from Fig. 8 that the tool allows clinicians to directly influence 
search algorithms, translating certain parameters into refined medical concepts for enhanced 
diagnostic effectiveness and algorithmic trust without sacrificing accuracy. This approach 
not only improves the diagnostic process but also enables users to adopt innovative strate-
gies for a deeper understanding and rectification of both machine learning and human errors.
The application of AIL-ML extends to dealing with computationally intensive tasks such 
as subspace clustering, protein folding, and the K-anonymization of health data. In these 
scenarios, the exponential search space can be significantly reduced with the aid of human 
expertise through the heuristic selection of samples. In the context of health informatics, 
particularly when tackling limited datasets or rare occurrences, the limitations of automated 
machine learning due to insufficient training samples become evident. A study advocates 
for the adoption of interactive machine learning, described as algorithms that enhance their 
learning outcomes through interactions with agents, including humans (Holzinger 2016). 
This approach allows AIL-ML to utilize human knowledge and experience, optimizing the 
learning trajectories of machine learning models and thereby elevating their accuracy and 
efficiency.

The  deployment  of  AIL-ML  in  disease  diagnosis,  such  as  Coronary  Artery  Disease, 
leverages  expert  insights  integrated  into  the  classification  process,  enhancing  diagnostic 
accuracy (Samaras et al. 2023). This approach not only augments the interpretability and 
transparency  of  the  models  but  also  bolsters  their  reliability. AIL-ML  applications  effec-
tively  address  data  bottlenecks  in  the  treatment  of  various  diseases,  including  pancreatic 
cancer. According  to  Fig.  8c,  by  incorporating  nuanced  human  judgments  and  expertise, 
these  systems  enhance  the  efficiency  and  outcomes  of  medical  interventions,  as  demon-
strated in recent studies (Mosqueira-Rey et al. 2023b).

4.2.2  Finance

AIL-ML is a paradigm that integrates agents into the machine learning loop, making it par-
ticularly suitable for fields that require strict supervision, such as finance. The application of

---

<!-- PAGE 45 -->

Page 45 of 55  266

Fig. 8  Frameworks of AIL-ML application for specialized knowledge domain. a Liu et al. (2023) A pro-
totype of potential implementation in EHR system-AI decision support editors. b Cai et al. (2019) Key 
components of SMILY. c Mosqueira-Rey et al. (2023b) The workflow of the AITL system which is de-
signed for expert to resolve the data bottleneck problem for the treatment of pancreatic cancer. Note: The 
figures provide a rough conceptual understanding, and the text is not intended to be read in full detail. The 
figures are borrowed from the following papers: (a) Liu et al. (2023), (b) Cai et al. (2019), (c) Mosqueira-
Rey et al. (2023b)

---

<!-- PAGE 46 -->

266  Page 46 of 55

AIL-ML in finance is growing in importance since it enhances the safety and interpretability 
of ML models.

Despite the growing use of ML in finance, the"black box"problem remains a major bar-
rier.  Specifically,  the"black  box"is  the  risk  that  ML  models’  outputs  and  operations  are 
unknown to and uncontrolled by human. Buckley et al. (2021) suggest that the most effec-
tive way to address this black box issue is by bringing humans into the ML loop, strength-
ening internal governance where external financial supervision may not be sufficient. They 
propose three key AIL tools: (1) AI due diligence, which involves a thorough human evalu-
ation of potential risks before the development and deployment of AI; (2) AI explainability, 
which ensures transparency in the model’s decision-making process, making it understand-
able to humans; and (3) AI review committees, where human oversight is responsible for 
ethical decision-making, ensuring accountability for AI actions.

4.2.3  Law

Legal services is important in protecting individual rights and maintaining social fairness 
(Auerbach 1977; Tushnet 2009; Cui et al. 2024). However, these services face many chal-
lenges, such as high costs, limited resources, complex legal terminology, frequent legisla-
tive  changes  and  so  on.  Despite  the  impressive  performance  of  large  models  in  various 
domains, they encounter the"hallucination problem"in the legal field, where generated con-
tent may be inaccurate or outdated, which will cause legal risks.

A notable example of applying AIL-ML in the legal domain is Chatlaw (Cui et al. 2024), 
a multi-agent collaborative framework designed for intelligent legal consultation. As shown 
in Fig. 9, agents are involved at multiple stages of the system. During the data preprocessing 
stage, human refine and annotate the cleansed dataset, enabling the construction of high-
quality  knowledge  graphs  and  question-answer  pairs.  Furthermore,  agents  are  integrated 
into  the  core  workflow  of  Chatlaw.  Multiple  agents,  such  as  legal  assistants  and  senior 
lawyers,  interact  with  users,  dynamically  updating  knowledge  graph  nodes,  generating 
legal advice, and validating the relevance and legality of retrieved legal cases and clauses. 
This process ensures the generated legal advice is accuracy and authority. Chatlaw not only 
addresses  the  inherent  interpretability  challenges  of  legal  tasks  but  also  offers  valuable 
insights for developing reliable and context-aware legal support systems.

5  Discussion about limitation and future work

5.1  Limitation

AIL-ML, as a process-oriented paradigm, spans multiple research domains but lacks well-
defined  research  objectives  and  standardized  methodologies  characteristic  of  fields  like 
transfer learning or domain generalization. While it is widely applied in areas such as data 
acquisition, model training, cold-start problems, and data annotation, AIL-ML incorporates 
diverse techniques, including human feedback, active learning, and LLMs. Due to the broad 
range of applications and the variety of  techniques involved, AIL-ML methods  are chal-
lenging to describe in a precise and detailed manner. Instead, they can be summarized by 
focusing on optimization strategies in data acquisition, processing, and model development,

---

<!-- PAGE 47 -->

Page 47 of 55  266

Fig. 9  Framework of Chatlaw (Cui et al. 2024). Note: The figure is borrowed from Cui et al. (2024)

such as reducing annotation costs, improving data initialization, or enhancing model train-
ing through agents. This high-level abstraction provides flexibility and broad applicability 
but also introduces the limitation of lacking standardization in research methods. Conse-
quently, much of the ongoing work focuses on integrating existing techniques within the 
AIL-ML framework, without establishing a unified technical process or evaluation criteria. 
Therefore, AIL-ML  functions  more  as  a  guiding  philosophy  than  as  a  specific  technical 
toolkit. Future research should prioritize the development of domain-specific methodolo-
gies and standardized frameworks to enhance the consistency and practicality of AIL-ML 
applications.

A potential limitation of the AIL-ML framework lies in its reliance on the performance 
of  LLMs.  While  LLMs  provide  advanced  capabilities  in  reasoning  and  language  under-

---

<!-- PAGE 48 -->

266  Page 48 of 55

standing, their outputs in specialized domains may be inaccurate or misleading, potentially 
lowering the overall system performance. Additionally, LLMs are often considered"black 
boxes,"lacking transparency and interpretability. This limitation can hinder the adoption of 
AIL-ML in fields requiring high levels of trust and explainability, such as medical diagnos-
tics. AIL-ML relies on a combination of human input and agent feedback, making it more 
dependent on the quality and reliability of the agents used within the system. This distinc-
tion highlights the need for further research into improving the transparency and accuracy 
of LLMs when integrated into the AIL-ML framework.

5.2  Future directions

Building Trust in AIL-ML Systems with Counterfactual Explanations One critical aspect of 
AIL-ML systems is establishing trust between agnets and the models. Trust can be achieved 
through counterfactual explanations, which help users understand how and why a model’s 
output changes under hypothetical input conditions. This aligns with human reasoning pro-
cesses, enabling non-experts to familiarize themselves with the decision boundaries of ML 
models. Del Ser et al. (2024) conduct a generative framework that employs counterfactual 
explanations to balance plausibility, change intensity, and adversarial power through multi-
objective optimization. This approach not only enhances interpretability but also uncovers 
concept-based biases and misrepresented features within the model, making it a valuable 
tool for fostering trust. This facilitates better understanding of model limitations, encour-
ages informed decision-making, and ensures that AIL-ML systems are perceived as reliable 
and transparent. Future research could explore combining counterfactual explanations with 
other interpretability techniques to create a more comprehensive trust-building framework, 
further advancing AIL-ML’s applicability in sensitive and high-stakes environments.

Reducing  Bias  in AIL-ML  Framework.  In AIL-ML,  how  to  reduce  bias  is  an  impor-
tant and valuable research direction. Currently, both LLMs and human experts are inher-
ently biased. For instance, LLMs may exhibit selection bias by being overly sensitive to 
changes  in  input  options’  order  or  position  (Zheng  et  al.  2023)  and  the  training  data  for 
LLMs often contains embedded social, cultural, or historical biases that can be amplified 
in  outputs. Additionally,  human  experts  involved  in  the AIL  process  may  also  have  cog-
nitive  biases,  which  can  result  in  unbalanced  or  biased  knowledge  being  introduced  into 
the ML. Therefore, future research must focus on developing methods to ensure unbiased 
knowledge injection within the AIL-ML framework. This involves not only mitigating bias 
at  the  source  (from  both  agents  like  LLMs  and  human  contributors)  but  also  establish-
ing  mechanisms  to  detect  and  correct  biases  during  data  annotation,  model  training,  and 
feedback loops. Approaches could include designing fairer selection mechanisms, imple-
menting diverse annotation strategies, and employing de-biasing techniques to counteract 
both selection and data biases. Moreover, algorithms capable of identifying and rectifying 
potential biases in human and LLM-based annotations will further enhance the fairness and 
reliability of AIL-ML systems. By systematically addressing bias, AIL-ML can improve its 
applicability to high-stakes domains such as healthcare and legal decision-making, where 
trust  and  explainability  are  important,  while  also  promoting  fairness  and  generalizability 
across  diverse  applications. This  research  direction  is  crucial  not  only  for  enhancing  the 
technical performance of AIL-ML systems but also for advancing the social responsibility 
of AI technologies.

---

<!-- PAGE 49 -->

Page 49 of 55  266

Enabling Agents to Handle High-Dimensional and Unstructured Data in AIL-ML. A sig-
nificant research direction for AIL-ML is finding effective methods to enable agents to pro-
cess high-dimensional and unstructured data. Currently, most AIL-ML systems are designed 
to handle low-dimensional data or natural language, with limited exploration of unstruc-
tured data types such as images, sensor signals, and acoustic data. In practical applications 
like smart homes and healthcare, the lack of context-awareness for these unstructured data 
types limits the potential of intelligent systems. Addressing this challenge by developing 
techniques  that  allow  agents  to  handle  complex,  high-dimensional  data  can  unlock  new 
possibilities  for  AIL-ML,  enabling  more  robust  contextual  understanding  and  improved 
performance in diverse environments. This direction holds great promise for enhancing the 
adaptability and intelligence of systems in fields like IoT and smart healthcare, where deal-
ing with unstructured data is crucial.

Enhancing Collaboration Between Large Models and Humans in AIL-ML. A promising 
future direction for AIL-ML research is focusing on improving the collaboration between 
LLMs  and  humans. As AIL  systems  continue  to  evolve,  the  autonomy  and  collaboration 
mechanisms  in  multi-agent  systems  become  critical.  Future  research  can  explore  how  to 
establish effective collaboration frameworks among multiple agents, including domain-spe-
cific LLMs and human experts. These agents can collaborate and share knowledge, enabling 
more  effective handling  of  complex  tasks.  By  fostering  better  cooperation between  large 
models and human experts, AIL-ML systems can significantly enhance their performance 
and adaptability across diverse applications. This direction opens up new possibilities for 
optimizing human-AI interaction, making AIL systems more versatile and capable in vari-
ous real-world scenarios.

6  Conclusion

Human-in-the-Loop Machine Learning (HIL-ML) has become an important research topic 
in machine learning research. The development and popularization of large models intro-
duce both challenges and opportunities to this field. In this paper, we present a comprehen-
sive  survey  of AIL-ML  (which  is  also  called AIL-ML),  providing  an  in-depth  review  of 
its methodologies across key stages of machine learning, including a structured review of 
data collection, data initialization, data quality enhancement, data annotation, model cold 
start, model training, and iterative model refinement. Furthermore, we summarize AIL-ML 
applications in diverse fields. Finally, we analyze the current challenges and highlight future 
directions. We hope that this survey will serve as a valuable resource for researchers, offer-
ing insights that encourage further exploration and development in AIL-ML.

Acknowledgements  This work is supported by the Natural Science Foundation of China (No.62302487), 
Improvement Project of Chinese Academy of Sciences (No.GSZXKYZB2025007), the Science and Tech-
nology  Innovation  Program  of  Hunan  Province  (No.2022RC4006,  No.2024  JJ9031),  and  the  Innovation 
Funding of ICT, CAS.

Author  contributions  Jiayuan  Gao  conducted  the  literature  review,  developed  the  framework,  wrote  the 
manuscript, drafted the figures, prepared Figures 6,7,8 and coordinated the work among the authors. Yingwei 
Zhang and Yiqiang Chen contributed to the framework development. Yihan Dong conducted the literature 
review and prepared Figures 1 and 2. Yuanzhe Chen contributed to writing the manuscript and prepared Fig-
ure 3. Shuchao Song prepared Figures 4 and 5. Boshi Tang and Yang Gu provided suggestions for manuscript 
revisions. All authors reviewed the manuscript.

---

<!-- PAGE 50 -->

266  Page 50 of 55

Data availability  No datasets were generated or analysed during the current study.

Declarations

Conflict of interest  The authors declare no Conflict of interest.

Open  Access    This  article  is  licensed  under  a  Creative  Commons  Attribution-NonCommercial-
NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and 
reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the 
source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. 
You do not have permission under this licence to share adapted material derived from this article or parts of it. 
The images or other third party material in this article are included in the article’s Creative Commons licence, 
unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative 
Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, 
you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h 
t t p : /  / c r e a  t i v e c o  m m o n  s . o r g  / l i c e  n s e s / b  y - n c  - n d / 4 . 0 /.

References

Ahn Y, Lin Y-R, Xu P, Dai Z (2023) Escape: countering systematic errors from machine’s blind spots via 
interactive visual analysis. In: Proceedings of the 2023 CHI Conference on Human Factors in Comput-
ing Systems, pp 1–16

Arakawa R, Yakura H, Mollyn V, Nie S, Russell E, DeMeo DP, Reddy HA, Maytin AK, Carroll BT, Lehman 
JF et al (2023) Prism-tracker: A framework for multimodal procedure tracking using wearable sensors 
and state transition information with user-driven handling of errors and uncertainty. Proceedings of the 
ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 6(4):1–27

Arous  I,  Dolamic  L, Yang  J,  Bhardwaj A,  Cuccu  G,  Cudré-Mauroux  P  (2021)  Marta:  leveraging  human 
rationales for explainable text classification. In: Proceedings of the AAAI Conference on Artificial Intel-
ligence, vol 35, pp. 5868–5876

Auerbach  JS  (1977)  Unequal  justice:  lawyers  and  social  change  in  modern America.  Oxford  University

Press, Oxford

Bartolo M, Roberts A, Welbl J, Riedel S, Stenetorp P (2020) Beat the ai: investigating adversarial human

annotation for reading comprehension. Trans Assoc Comput Linguist 8:662–678

Ben-David S, Blitzer J, Crammer K, Pereira F (2006) Analysis of representations for domain adaptation. Adv

Neural Inf Process Syst.  h t t p s :  / / d o i  . o r g / 1  0 . 7 5  5 1 / m i  t p r e s  s / 7 5 0 3  . 0 0 3  . 0 0 2 2

Bommasani R, Hudson DA, Adeli E, Altman R, Arora S, Arx S, Bernstein MS, Bohg J, Bosselut A, Brunskill 
E, et al (2021) On the opportunities and risks of foundation models. Preprint at  h t t p s : / / a r x i v . o r g / a b s / q 
u a n t - p h / 2 1 0 8 . 0 7 2 5 8

Brown T, Mann B, Ryder N, Subbiah M, Kaplan JD, Dhariwal P, Neelakantan A, Shyam P, Sastry G, Askell 
A et al (2020) Language models are few-shot learners. Adv Neural Inf Process Syst 33:1877–1901
Buckley RP, Zetzsche DA, Arner DW, Tang BW (2021) Regulating artificial intelligence in finance: putting

the human in the loop. Sydney Law Rev 43(1):43–81

Budd S, Robinson EC, Kainz B (2021) A survey on active learning and human-in-the-loop deep learning for

medical image analysis. Med Image Anal 71:102062

Cai CJ, Reif E, Hegde N, Hipp J, Kim B, Smilkov D, Wattenberg M, Viegas F, Corrado GS, Stumpe MC, et al 
(2019) Human-centered tools for coping with imperfect algorithms during medical decision-making. In: 
Proceedings of the 2019 Chi Conference on Human Factors in Computing Systems, pp 1–14

Chen K, Zhang D, Yao L, Guo B, Yu Z, Liu Y (2021a) Deep learning for sensor-based human activity recog-

nition: overview, challenges, and opportunities. ACM Comput Surv (CSUR) 54(4):1–40

Chen X, Jiang M, Zhao Q (2021b) Leveraging human attention in novel object captioning. In: International

Joint Conference on Artificial Intelligence

Cho S, Kim Y, Jang J, Hwang I (2023) Ai-to-human actuation: Boosting unmodified ai’s robustness by pro-
actively inducing favorable human sensing conditions. Proceedings of the ACM on Interactive, Mobile, 
Wearable and Ubiquitous Technologies 7(1):1–32

Crochepierre L, Boudjeloud-Assala L, Barbesant V (2022) Interactive reinforcement learning for symbolic 
regression from multi-format human-preference feedbacks. In: 31st International Joint Conference on 
Artificial Intelligence (IJCAI 2022)

---

<!-- PAGE 51 -->

Page 51 of 55  266

Cui Y, Koppol P, Admoni H, Niekum S, Simmons R, Steinfeld A, Fitzgerald T (2021) Understanding the rela-
tionship between interactions and outcomes in human-in-the-loop machine learning. In: International 
Joint Conference on Artificial Intelligence

Cui J, Ning M, Li Z, Chen B, Yan Y, Li H, Ling B, Tian Y, Yuan L (2024) Chatlaw: a multi-agent collabora-
tive legal assistant with knowledge graph enhanced mixture-of-experts large language model. Preprint 
at https://arxiv.org/abs/quant-ph/2306.16092

Dai H, Liu Z, Liao W, Huang X, Cao Y, Wu Z, Zhao L, Xu S, Liu W, Liu N et al (2023) Auggpt: leveraging

chatgpt for text data augmentation. Preprint at https://arxiv.org/abs/quant-ph/2302.13007

Del Ser J, Barredo-Arrieta A, Díaz-Rodríguez N, Herrera F, Saranti A, Holzinger A (2024) On generating 
trustworthy counterfactual explanations. Inf Sci 655:119898. https://doi.org/10.1016/j.ins.2023.119898
Ding B, Qin C, Liu L, Bing L, Joty SR, Li BA (2022) Is gpt-3 a good data annotator? In: Annual meeting 
of the Association for Computational Linguistics.  h t t p s :  / / a p i  . s e m a n  t i c s  c h o l a  r . o r g  / C o r p u  s I D :  2 5 4 8 7 7 1 7 1
Dwork C (2006) Differential privacy. International colloquium on automata, languages, and programming.

Springer, Cham, pp 1–12

Fan Y, Watkins O, Du Y, Liu H, Ryu M, Boutilier C, Abbeel P, Ghavamzadeh M, Lee K, Lee K (2024) Rein-
forcement learning for fine-tuning text-to-image diffusion models. Adv Neural Inf Process Syst.  h t t p s : / 
/ d o i . o r g / 1 0 . 4 8 5 5 0 / a r X i v . 2 3 0 5 . 1 6 3 8 1

Gao  J,  Pi  R,  Lin Y,  Xu  H, Ye  J, Wu  Z,  Zhang W,  Liang  X,  Li  Z,  Kong  L  (2023)  Self-guided  noise-free 
data generation for efficient zero-shot learning. In: The Twelfth International Conference on Learning 
Representations

Gao J, Zhang Y, Chen Y, Zhang T, Tang B, Wang X (2024) Unsupervised human activity recognition via 
large language models and iterative evolution. In: ICASSP 2024-2024 IEEE International Conference 
on Acoustics, Speech and Signal Processing (ICASSP), IEEE, pp 91–95

Gou J, Yu B, Maybank SJ, Tao D (2021) Knowledge distillation: a survey. Int J Comput Vis 129(6):1789–1819
Guo S, Zhang B, Liu T, Liu T, Khalman M, Llinares F, Rame A, Mesnard T, Zhao Y, Piot B, et al (2024) 
Direct language model alignment from online ai feedback. Preprint at  h t t p s : / / a r x i v . o r g / a b s / q u a n t - p h / 2 
4 0 2 . 0 4 7 9 2

Hancock B, Bordes A, Mazare P-E, Weston J (2019) Learning from dialogue after deployment: feed yourself,

chatbot! Preprint at https://arxiv.org/abs/quant-ph/1901.05415

He  Z,  Ribeiro  MT,  Khani  F  (2023a)  Targeted  data  generation:  finding  and  fixing  model  weaknesses.  In: 
Rogers A, Boyd-Graber J, Okazaki N (eds) Proceedings of the 61st Annual Meeting of the Associa-
tion for Computational Linguistics (Vol 1: Long Papers), Association for Computational Linguistics, 
Toronto,  pp  8506–8520.   h t t p s :  / / d o i  . o r g / 1  0 . 1 8  6 5 3 / v  1 / 2 0 2  3 . a c l -  l o n g  . 4 7 4.   h t t p s : / / a c l a n t h o l o g y . o r g / 2 0 2 3 
. a c l - l o n g . 4 7 4

He X, Lin Z, Gong Y, Jin A, Zhang H, Lin C, Jiao J, Yiu SM, Duan N, Chen W, et al (2023b) Annollm: mak-
ing large language models to be better crowdsourced annotators. Preprint at  h t t p s : / / a r x i v . o r g / a b s / q u a n 
t - p h / 2 3 0 3 . 1 6 8 5 4

Hemmer P, Schellhammer S, Vössing M, Jakubik J, Satzger G (2022) Forming effective human-ai teams: 
building  machine  learning  models  that  complement  the  capabilities  of  multiple  experts.  Preprint  at 
https://arxiv.org/abs/quant-ph/2206.07948

Hinton G (2015) Distilling the knowledge in a neural network. Preprint at  h t t p s : / / a r x i v . o r g / a b s / q u a n t - p h / 1 5

0 3 . 0 2 5 3 1

Hiremath SK, Nishimura Y, Chernova S, Plötz T (2022) Bootstrapping human activity recognition systems 
for smart homes from scratch. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiqui-
tous Technologies 6(3):1–27

Holzinger A (2016) Interactive machine learning for health informatics: when do we need the human-in-the-

loop? Brain Inform 3(2):119–131

Hsieh C-Y, Li C-L, Yeh C-K, Nakhost H, Fujii Y, Ratner A, Krishna R, Lee C-Y, Pfister T (2023a) Distilling 
step-by-step! outperforming larger language models with less training data and smaller model sizes. In: 
Rogers A, Boyd-Graber J, Okazaki N (eds) Findings of the Association for Computational Linguistics: 
ACL 2023, Association for Computational Linguistics, Toronto, pp 8003–8017.  h t t p s :  / / d o i  . o r g / 1  0 . 1 8  6 5 
3 / v  1 / 2 0 2  3 . fi  n d  i n g s  - a c l . 5 0 7.  h t t p s :  / / a c l  a n t h o l  o g y .  o r g / 2  0 2 3 . fi   n d i n g  s - a c  l . 5 0 7

Hsieh C (2023b) Human-centred multimodal deep learning models for chest x-ray diagnosis. In: Proceedings

of the Thirty-Second International Joint Conference on Artificial Intelligence, pp 7085–7086

Kath H, Gouvêa TS, Sonntag D (2023) A human-in-the-loop tool for annotating passive acoustic monitoring 
datasets. In: Proceedings of the 32nd International Joint Conference on Artificial Intelligence, IJCAI
Kenton JDMWC, Toutanova LK (2019) Bert: pre-training of deep bidirectional transformers for language

understanding. In: Proceedings of NAACL-HLT, pp 4171–4186

Klie  J-C,  Castilho  RE,  Gurevych  I  (2020)  From  zero  to  hero:  Human-in-the-loop  entity  linking  in  low 
resource domains. In: Proceedings of the 58th Annual Meeting of the Association for Computational 
Linguistics, pp 6982–6993

---

<!-- PAGE 52 -->

266  Page 52 of 55

Klissarov  M,  D’Oro  P,  Sodhani  S,  Raileanu  R,  Bacon  P-L, Vincent  P,  Zhang A,  Henaff  M  (2023)  Motif:

intrinsic motivation from artificial intelligence feedback

Koppol P, Admoni H, Simmons RG (2021) Interaction considerations in learning from humans. In: IJCAI,

pp 283–291

Krizhevsky A, Sutskever I, Hinton GE (2012) Imagenet classification with deep convolutional neural net-

works. Adv Neural Inf Process Syst 25

Kwon M, Michael S (2023) Reward design with language models. In: International Conference on Learning

Representations (ICLR)

LeCun Y, Bengio Y, Hinton G (2015) Deep learning. Nature 521(7553):436–444
Li G (2017) Human-in-the-loop data integration. Proc VLDB Endow 10(12):2006–2017
Li H, Dong Q, Tang Z, Wang C, Zhang X, Huang H, Huang S, Huang X, Huang Z, Zhang D et al (2024) 
Synthetic data (almost) from scratch: generalized instruction tuning for language models. Preprint at 
https://arxiv.org/abs/quant-ph/2402.13064

Liu Z, Guo Y, Mahmud J (2021) When and why a model fails? a human-in-the-loop error detection frame-
work for sentiment analysis. In: Proceedings of the 2021 Conference of the North American Chapter 
of the Association for Computational Linguistics: human language technologies: Industry Papers, pp 
170–177

Liu S, Wright AP, Patterson BL, Wanderer JP, Turer RW, Nelson SD, McCoy AB, Sittig DF, Wright A (2023) 
Using ai-generated suggestions from chatgpt to optimize clinical decision support. J Am Med Inform 
Assoc 30(7):1237–1245

Long Y, Wei W, Huang T, Wang Y, Dou Q (2023) Human-in-the-loop embodied intelligence with interactive

simulation environment for surgical robot learning. IEEE Robot Autom Lett 8:4441–8

Lu F, Wang W, Luo Y, Zhu Z, Sun Q, Xu B, Shi H, Gao S, Li Q, Song Y, et al (2024) Miko: multimodal inten-
tion knowledge distillation from large language models for social-media commonsense discovery. In: 
Proceedings of the 32nd ACM International Conference on Multimedia, pp 3303–3312

Metsch  JM,  Saranti A, Angerschmid A,  Pfeifer  B,  Klemt  V,  Holzinger A,  Hauschild A-C  (2024)  Clarus: 
An interactive explainable ai platform for manual counterfactuals in graph neural networks. J Biomed 
Inform 150:104600. https://doi.org/10.1016/j.jbi.2024.104600

Mondorf P, Plank B (2024) Beyond accuracy: evaluating the reasoning behavior of large language models—a

survey. Preprint at https://arxiv.org/abs/quant-ph/2404.01869

Mosqueira-Rey  E,  Hernández-Pereira  E,  Alonso-Ríos  D,  Bobes-Bascarán  J,  Fernández-Leal  Á  (2023a)

Human-in-the-loop machine learning: a state of the art. Artif Intell Rev 56(4):3005–3054

Mosqueira-Rey E, Hernández-Pereira E, Bobes-Bascarán J, Alonso-Ríos D, Pérez-Sánchez A, Fernández-
Leal Á, Moret-Bonillo V, Vidal-Ínsua Y, Vázquez-Rivera F (2023b) Addressing the data bottleneck in 
medical deep learning models using a human-in-the-loop machine learning approach. Neural Comput 
Appl 36:2597

Oh  SW,  Lee  J-Y,  Xu  N,  Kim  SJ  (2019)  Fast  user-guided  video  object  segmentation  by  interaction-and-
propagation networks. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern 
Recognition, pp 5247–5256

Ouyang L, Wu J, Jiang X, Almeida D, Wainwright C, Mishkin P, Zhang C, Agarwal S, Slama K, Ray A et al 
(2022) Training language models to follow instructions with human feedback. Adv Neural Inf Process 
Syst 35:27730–27744

Pan W, Wang X, Song M, Chen C (2020) Survey on generating adversarial examples. Ruan Jian Xue Bao/J

Softw 31(1):67–81 (in Chinese)

Park JS, Hessel J, Chandu K, Liang PP, Lu X, West P, Yu Y, Huang Q, Gao J, Farhadi A et al (2023) Local-
ized  symbolic  knowledge  distillation  for  visual  commonsense  models. Adv  Neural  Inf  Process  Syst 
36:11338–11352

Qian K, Raman PC, Li Y, Popa L (2020) Partner: Human-in-the-loop entity name understanding with deep

learning. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol 34, pp 13634–13635

Radford A, Narasimhan K, Salimans T, Sutskever I, et al (2018) Improving language understanding by gen-

erative pre-training.

Retzlaff  CO,  Das  S, Wayllace  C,  Mousavi  P, Afshari  M, Yang T,  Saranti A, Angerschmid A, Taylor  ME, 
Holzinger A (2024) Human-in-the-loop reinforcement learning: a survey and position on requirements, 
challenges, and opportunities. J Artif Int Res. https://doi.org/10.1613/jair.1.15348

Roels J, Vernaillen F, Kremer A, Gonçalves A, Aelterman J, Luong HQ, Goossens B, Philips W, Lippens 
S,  Saeys Y  (2019) A  ‘human-in-the-loop’approach  for  semi-automated  image  restoration  in  electron 
microscopy. BioRxiv. https://doi.org/10.1101/644146

---

<!-- PAGE 53 -->

Page 53 of 55  266

Sahu G, Vechtomova O, Bahdanau D, Laradji I (2023) Promptmix: a class boundary augmentation method 
for large language model distillation. In: Bouamor H, Pino J, Bali K. (eds) Proceedings of the 2023 
Conference on Empirical Methods in Natural Language Processing, Association for Computational Lin-
guistics, Singapore, pp 5316–5327  h t t p s :  / / d o i  . o r g / 1  0 . 1 8  6 5 3 / v  1 / 2 0 2  3 . e m n l  p - m a  i n . 3 2 3.  h t t p s : / / a c l a n t h o 
l o g y . o r g / 2 0 2 3 . e m n l p - m a i n . 3 2 3

Samaras A-D,  Moustakidis  S, Apostolopoulos  ID,  Papandrianos  N,  Papageorgiou  E  (2023)  Classification 
models for assessing coronary artery disease instances using clinical and biometric data: an explainable 
man-in-the-loop approach. Scientific Rep 13(1):6668

Settles B (2009) Active learning literature survey
Stiennon N, Ouyang L, Wu J, Ziegler D, Lowe R, Voss C, Radford A, Amodei D, Christiano PF (2020) Learn-

ing to summarize with human feedback. Adv Neural Inf Process Syst 33:3008–3021

Sun Z, Shen Y, Zhou Q, Zhang H, Chen Z, Cox D, Yang Y, Gan C (2024) Principle-driven self-alignment of

language models from scratch with minimal human supervision. Adv Neural Inf Process Syst 36:2511
Tchemeube RB, Ens J, Plut C, Pasquier P, Safi M, Grabit Y, Rolland J-B (2023) Evaluating human-ai interac-
tion via usability, user experience and acceptance measures for mmm-c: a creative ai system for music 
composition. In: Proceedings of the Thirty-Second International Joint Conference on Artificial Intel-
ligence, pp 5769–5778

Touvron H, Lavril T, Izacard G, Martinet X, Lachaux M-A, Lacroix T, Rozière B, Goyal N, Hambro E, Azhar 
F, et al (2023) Llama: open and efficient foundation language models. Preprint at  h t t p s : / / a r x i v . o r g / a b s / 
q u a n t - p h / 3 0 2 . 1 3 9 7 1

Tushnet  MV  (2009)  The  rights  revolution  in  the  twentieth  century.  American  Historical  Association,

Washington

Vaswani A (2017) Attention is all you need. Adv Neural Inf Process Syst 30:1
Wallace E, Rodriguez P, Feng S, Yamada I, Boyd-Graber J (2019) Trick me if you can: human-in-the-loop

generation of adversarial examples for question answering. Trans Assoc Comput Linguist 7:387–401

Wang  S,  Liu Y,  Xu Y,  Zhu  C,  Zeng  M  (2021) Want  to  reduce  labeling  cost?  GPT-3  can  help.  In:  Moens 
M.-F, Huang X, Specia L, Yih SW-T (eds) Findings of the Association for Computational Linguistics: 
EMNLP 2021, Association for Computational Linguistics, Punta Cana, pp 4195–4205.  h t t p s :  / / d o i  . o r g / 1  
0 . 1 8  6 5 3 / v  1 / 2 0 2  1 . fi  n d  i n g s  - e m n l p . 3 5 4.  h t t p s :  / / a c l  a n t h o l  o g y .  o r g / 2  0 2 1 . fi   n d i n g  s - e m  n l p . 3 5 4

Wang  J,  Lan  C,  Liu  C,  Ouyang Y,  Qin  T,  Lu  W,  Chen Y,  Zeng  W, Yu  P  (2022)  Generalizing  to  unseen

domains: a survey on domain generalization. IEEE Trans Knowl Data Eng 35:8052

Wang Y, Yu Z, Liu S, Zhou Z, Guo B (2023a) Genie in the model: Automatic generation of human-in-the-loop 
deep neural networks for mobile applications. Proceedings of the ACM on Interactive, Mobile, Wear-
able and Ubiquitous Technologies 7(1):1–29

Wang Y, Kordi Y, Mishra S, Liu A, Smith NA, Khashabi D, Hajishirzi H (2023b) Self-instruct: aligning lan-
guage models with self-generated instructions. In: Rogers A, Boyd-Graber J, Okazaki N (eds) Proceed-
ings of the 61st Annual Meeting of the Association for Computational Linguistics (Vol 1: Long Papers), 
Association for Computational Linguistics, Toronto, pp 13484–13508.  h t t p s :  / / d o i  . o r g / 1  0 . 1 8  6 5 3 / v  1 / 2 0 2  
3 . a c l -  l o n g  . 7 5 4. https://aclanthology.org/2023.acl-long.754

Wang X, Kim H, Rahman S, Mitra K, Miao Z (2024) Human-llm collaborative annotation through effective 
verification  of  llm  labels.  In:  Proceedings  of  the  CHI  Conference  on  Human  Factors  in  Computing 
Systems, pp 1–21

Weber T, Hußmann H, Han Z, Matthes S, Liu Y (2020) Draw with me: human-in-the-loop for image restora-

tion. In: Proceedings of the 25th International Conference on Intelligent User Interfaces, pp 243–253

Wei J, Xie H, Chang C, Yang X (2022) Fine-tuning Deep Neural Networks by Interactively Refining the 2D 
Latent Space of Ambiguous Images. In: International Joint Conference on Artificial Intelligence
Wu J, Harrison C, Bigham JP, Laput G (2020) Automated class discovery and one-shot interactions for acous-
tic activity recognition. In: Proceedings of the 2020 CHI Conference on Human Factors in Computing 
Systems, pp 1–14

Wu X, Xiao L, Sun Y, Zhang J, Ma T, He L (2022) A survey of human-in-the-loop for machine learning.

Future Gener Comput Syst 135:364–381. https://doi.org/10.1016/j.future.2022.05.014

Xin D, Ma L, Liu J, Macke S, Song S, Parameswaran A (2018) Accelerating human-in-the-loop machine 
learning: challenges and opportunities. In: Proceedings of the second workshop on data management 
for end-to-end machine learning, pp 1–4

Xu X, Gong J, Brum C, Liang L, Suh B, Gupta SK, Agarwal Y, Lindsey L, Kang R, Shahsavari B, et al (2022) 
Enabling hand gesture customization on wrist-worn devices. In: Proceedings of the 2022 CHI Confer-
ence on Human Factors in Computing Systems, pp 1–19

---

<!-- PAGE 54 -->

266  Page 54 of 55

Xu C, Guo D, Duan N, McAuley J (2023) Baize: an open-source chat model with parameter-efficient tuning 
on self-chat data. In: Bouamor H, Pino J, Bali K (eds) Proceedings of the 2023 Conference on Empirical 
Methods in Natural Language Processing, Association for Computational Linguistics, Singapore, pp. 
6268–6278.  h t t p s :  / / d o i  . o r g / 1  0 . 1 8  6 5 3 / v  1 / 2 0 2  3 . e m n l  p - m a  i n . 3 8 5.  h t t p s : / / a c l a n t h o l o g y . o r g / 2 0 2 3 . e m n l p - m 
a i n . 3 8 5

Xu X, Li M, Tao C, Shen T, Cheng R, Li J, Xu C, Tao D, Zhou T (2024) A survey on knowledge distillation

of large language models. Preprint at https://arxiv.org/abs/quant-ph/2402.13116

Yao Z, Li X, Gao J, Sadler B, Sun H (2019a) Interactive semantic parsing for if-then recipes via hierarchical 
reinforcement learning. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol 33, pp 
2547–2554

Yao Z, Su Y, Sun H, Yih W-T (2019b) Model-based interactive semantic parsing: a unified formulation and 
a text-to-sql case study. In: 2019 Conference on Empirical Methods in Natural Language Processing 
(EMNLP’19)

Ye J, Gao J, Li Q, Xu H, Feng J, Wu Z, Yu T, Kong L (2022) ZeroGen: efficient zero-shot learning via dataset 
generation. In: Goldberg Y, Kozareva Z, Zhang Y (eds) Proceedings of the 2022 Conference on Empiri-
cal Methods in Natural Language Processing, Association for Computational Linguistics, Abu Dhabi, 
pp 11653–11669.  h t t p s :   /  / d o  i . o r  g /  1 0 .  1 8 6  5 3   / v 1 / 2   0 2 2 . e   m n l  p -  m a i n . 8 0 1.  h t t p s : / / a c l a n t h o l o g y . o r g / 2 0 2 2 . e m 
n l p - m a i n . 8 0 1

Ye  W,  Zhang  Y,  Wang  M,  Wang  S,  Gu  X, Abbeel  P,  Gao  Y  (2023)  Foundation  reinforcement  learning: 
towards embodied generalist agents with foundation prior assistance. Preprint at  h t t p s : / / a r x i v . o r g / a b s 
/ q u a n t - p h / 2 3 1 0 . 0 2 6 3 5

Yu F, Seff A, Zhang Y, Song S, Funkhouser T, Xiao J (2015) Lsun: construction of a large-scale image data-
set using deep learning with humans in the loop. Preprint at https://arxiv.org/abs/quant-ph/1506.03365
Zhang S, He L, Dragut E, Vucetic S (2019) How to invest my time: lessons from human-in-the-loop entity 
extraction. In: Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discov-
ery & Data Mining, pp 2305–2313

Zhang C, Bengio S, Hardt M, Recht B, Vinyals O (2021) Understanding deep learning (still) requires rethink-

ing generalization. Commun ACM 64(3):107–115

Zheng C, Zhou H, Meng F, Zhou J, Huang M (2023) Large language models are not robust multiple choice

selectors. In: The Twelfth International Conference on Learning Representations

Zhuang F, Qi Z, Duan K, Xi D, Zhu Y, Zhu H, Xiong H, He Q (2020) A comprehensive survey on transfer

learning. Proc IEEE 109(1):43–76

Ziegler DM, Stiennon N, Wu J, Brown TB, Radford A, Amodei D, Christiano P, Irving G (2019) Fine-tuning 
language models from human preferences. Preprint at https://arxiv.org/abs/quant-ph/1909.08593

Publisher's Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.

Authors and Affiliations

Jiayuan Gao1,2 · Yingwei Zhang1,2 · Yiqiang Chen1,2 · Yihan Dong3 · Yuanzhe Chen1,2 · 
Shuchao Song1,2 · Boshi Tang4 · Yang Gu1,2

Yiqiang Chen

yqchen@ict.ac.cn

Jiayuan Gao
gaojiayuan20z@ict.ac.cn

Yingwei Zhang
zhangyingwei@ict.ac.cn

Yihan Dong
3120215895@bit.edu.cn

Yuanzhe Chen
chenyuanzhe21s@ict.ac.cn

Shuchao Song

---

<!-- PAGE 55 -->

Page 55 of 55  266

songshuchao22b@ict.ac.cn

Boshi Tang
tbs22@mails.tsinghua.edu.cn

Yang Gu
guyang@ict.ac.cn

1  Beijing Key Laboratory of Mobile Computing and Pervasive Device, Institute of Computing

Technology, Chinese Academy of Sciences, Beijing, China
2  University of Chinese Academy of Sciences, Beijing, China
3  Beijing Institute of Technology, Beijing, China
4  Tsinghua University, Beijing, China

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

et al. [full author details at the end of the article]
Artificial Intelligence Review (2025) 58:266
https://doi.org/10.1007/s10462-025-11255-1
Agent-in-the-loop to distill expert knowledge into artificial
intelligence models: a survey
Jiayuan Gao1,2 · Yingwei Zhang1,2 · Yiqiang Chen1,2 · Yihan Dong3 · Yuanzhe Chen1,2 ·
Shuchao Song1,2 · Boshi Tang4 · Yang Gu1,2
Accepted: 2 May 2025 / Published online: 4 June 2025
© The Author(s) 2025
Abstract
Large-scale neural networks have revolutionized many general knowledge areas (e.g.,
computer vision and language processing), but are still rarely applied in many expert
knowledge areas (e.g., healthcare), due to data sparsity and high annotation expenses. Hu-
man-in-the-loop machine learning (HIL-ML) incorporates expert domain knowledge into
the modeling process, effectively addressing these challenges. Recently, some research-
ers have started using large models to substitute for certain tasks typically performed by
humans. Although large models have limitations in expert knowledge areas, after being
trained on trillions of examples, they have demonstrated advanced capabilities in reason-
ing, semantic understanding, grounding, and planning. These capabilities can serve as
proxies of human, which introduces new opportunities and challenges in HIL-ML area.
Based on the above, we summarize a more comprehensive framework, Agent-in-the-Loop
Machine Learning (AIL-ML), where agent represents both humans and large models. AIL-
ML can efficiently collaborate human and large model to construct vertical AI models with
lower costs. This paper presents the first review of recent advancements in this area. First,
we provide a formal definition of AIL-ML and discuss its related fields. Then, we catego-
rize the AIL-ML methods based on data processing and model development, providing
formal definitions for each, and present representative works in detail for each category.
Third, we highlight relative applications of AIL-ML. Finally, we summarize the current
literature and highlight future research directions.
Keywords Human-in-the-Loop · Machine learning · Deep learning · Large language
models
1 Introduction
Over the past decade, large-scale neural networks (LeCun et al. 2015) have significantly
advanced the development of computer vision, natural language processing, and other gen-
eral knowledge domains. These breakthroughs, such as applications in image recognition
(Krizhevsky et al. 2012), have enabled technologies like autonomous vehicles and facial
Extended author information available on the last page of the article
1 3

266 Page 2 of 55 J. Gao et al.
recognition systems. In the realm of natural language processing, large models like the GPT
(Radford et al. 2018) series and BERT (Kenton and Toutanova 2019) have achieved near-
human capabilities in generating and understanding complex texts. These models have not
only enhanced the accuracy of machine translation but also improved interactions between
users and artificial systems. Furthermore, the adoption of these technologies has driven
innovations in intelligent customer service, showcasing their commercial potential.
Despite the remarkable achievements of large-scale neural networks in general knowl-
edge areas, they face numerous challenges in expert domains such as healthcare, law, and
so on. These fields often involve highly specialized and sparse datasets that are expensive
to acquire and require extensive preprocessing and precise manual annotation to ensure
data quality and usability. Additionally, traditional deep learning models are severely tested
in their generalization capabilities within these domains (Zhang et al. 2021). The inability
of training data to fully represent the complexities of the real world often means that these
models may fail to accurately predict unseen scenarios, thereby limiting their reliability in
professional applications. Data privacy becomes crucial when dealing with sensitive per-
sonal details in medical or legal contexts (Dwork 2006), demanding extra measures to sat-
isfy regulatory and ethical rules. These challenges demonstrate the need to integrate expert
domain knowledge into AI systems, where high accuracy and explainable decision-making
processes are necessary for gaining end-user trust. For instance, a medical diagnostic sys-
tem must be able to clearly justify its recommendations to physicians, allowing them to
make informed clinical decisions. Thus, integrating the knowledge and judgment of human
experts into the AI model becomes essential.
Facing the challenges above, Human-in-the-Loop Machine Learning (HIL-ML) (Wu et
al. 2022) offers an effective solution by incorporating human knowledge into the machine
learning process. It also emphasizes iterative interaction between humans and systems. As
shown in Fig. 1, in the HIL-ML framework, humans contribute at all stages of the machine
learning loop. These contributions enable machines to integrate human knowledge and
experience, thereby enhancing model accuracy and adaptability. HIL-ML distills human
expertise into machine learning through a dynamic feedback mechanism. Unlike static pipe-
lines, the framework employs an adaptive loop architecture where data and model influ-
ence each other iteratively. These human interventions allow machines to integrate human
knowledge and experience, thereby enhancing model accuracy, adaptability, and perfor-
mance on unseen data. By directly distilling deep expert knowledge into models, HIL-ML
not only improves model performance but also enhances explainability, making the models
more transparent and trustworthy for end-users. This approach also reduces potential pri-
vacy risks when handling sensitive information, as human experts can directly monitor and
adjust the processing of such data. Therefore, HIL-ML not only addresses the limitations of
Fig. 1 The HIL-ML workflow which can be segmented into four main stages: Data Acquisition, Data Pro-
cessing, Model Development, and Model Optimization, with continuous human involvement throughout
the process to ensure iterative refinement and optimization of the models
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 3 of 55 266
traditional automation methods in professional fields but also enhances the reliability and
effectiveness of AI systems in practical operations. By integrating human expert knowledge
and feedback, HIL-ML enables AI systems to excel both in technological sophistication
and practical application. Through human involvement, HIL-ML utilizes human knowledge
for corrections and optimizations at various stages of modeling process, resulting in more
precise and reliable machine learning models (Mosqueira-Rey et al. 2023a).
Recently, researchers have begun to employ large models to perform specific tasks tra-
ditionally executed by humans (Ding et al. 2022; Hsieh et al. 2023a). Although these large
models hold some limitations in domains requiring expert knowledge, they have demon-
strated advanced capabilities in reasoning, semantic understanding, grounding, and planning
after being trained on trillions of examples. Their deep contextual understanding enables
them to generate and comprehend language like humans (Mondorf and Plank 2024). Large
models, such as GPT (Radford et al. 2018) and LLaMA (Touvron et al. 2023), possess deep
contextual understanding and can generate meaningful outputs with minimal human input.
These capabilities allow large models to act as proxies for human intelligence, thereby intro-
ducing new opportunities and challenges in the HIL-ML area. However, Current reviews
(Wu et al. 2022; Mosqueira-Rey et al. 2023a; Xin et al. 2018) about HIL-ML fail to explore
how to address these challenges. Moreover, the potential role of Large Models (Brown et al.
2020) as participants in HIL-ML has been largely overlooked. Building on these insights,
we propose a novel concept called Large-Model-in-the-Loop Machine Learning (LMIL-
ML). In the LMIL-ML framework, large models are integrated into the modeling loop,
intervening at stages like data preprocessing or model development. By embedding large
models into the training process, LMIL-ML reduces the reliance on human annotation. This
framework achieves cost-efficient model training and improved accuracy by distilling large
model expertise into more task-specific machine learning models.
Based on the frameworks of HIL-ML and LMIL-ML, we further introduce a unified
and comprehensive framework, Agent in the Loop Machine Learning (AIL-ML). In this
framework, agents include both humans and large models. This framework aims to leverage
the complementary strengths of human cognitive skills and machine efficiency. AIL-ML
combines human intuition and expertise with the computational power and reasoning abil-
ity of large models, creating a balance that leverages the strengths of both. These agents
interact with the model at various stages-data processing, model training, and optimization-
forming a machine learning loop. This dynamic process enhances the model’s adaptability
to changing environments, improves predictive accuracy across diverse tasks, and reduces
the cost of iterative development. This paper provides a comprehensive overview of recent
advancements in this area.
This study employs an extensive literature survey method to ensure comprehensive and
high-quality research. We have reviewed works published at top computer science and
human-computer interaction conferences from 2018 to 2024, such as IJCAI, ACL, KDD,
AAAI, NIPS, ICML, CVPR, ICLR, CHI, IMWUT, CSCW and so on. Additionally, we
have also investigated the latest research on arXiv from 2023 and 2024. By reading titles
and abstracts, we selected the most relevant papers, classified them, and conducted in-depth
analyses to ensure a precise understanding of the methods. As shown in Fig. 2, the paper
begins by defining the core processes of AIL-ML and provides a structured framework for
understanding its mechanisms. We then discuss the methodologies used in AIL-ML, empha-
sizing the critical aspects of data acquisition and processing as well as model development
1 3

266 Page 4 of 55 J. Gao et al.
Fig. 2 Framework for AIL-ML Methodology. The framework can be divided into two main phases: Data
Acquisition and Processing, and Model Development and Optimization. The first phase contains Data
Collection, Initialization, Quality Enhancement, and Annotation. The second phase involves Model Cold
Start, Training, and Iterative Enhancement
and optimization. We also summarize applications of AIL-ML in domains requiring spe-
cialized knowledge. In the last section, we highlight the current challenges within AIL-
ML research and outline future research directions, providing both theoretical and practical
guidance for further development in the field.
The insights gained from this paper may contribute to a deeper understanding and practi-
cal application of AIL-ML. The paper’s contributions are as follows:
1. We conduct a comprehensive literature review of existing works on AIL-ML, focusing
on the role of agent in AIL-ML. Specifically, we summarize how humans and LLMs
operate within the framework of AIL-ML.
2. We offer a detailed and structured classification of data processing and model develop-
ment methods within AIL-ML. This taxonomy organizes methods into distinct catego-
ries, helping researchers select suitable approaches for specific problems.
3. Based on the classification, we analyze and summarize the differences and relationships
between various methods in AIL-ML.
4. We propose a clear methodological framework for AIL-ML, by formalizing a math-
ematical description. This framework simplifies complex concepts and processes,
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 5 of 55  266
enhancing their accessibility to researchers and practitioners. This formalization also
establish a solid theoretical foundation for future work.
2  Background
2.1  Related reviews
Human-in-the-loop has emerged as a prominent area of interest within the field of machine
learning in recent years. With the expansion of machine learning applications across com-
puter vision, natural language processing, and speech processing, there has been a growing
realization that reliance solely on machine-driven learning is limited. Integrating human
domain knowledge and experience has proven to be more effective in addressing specific
challenges. In the realm of HIL machine learning, several comprehensive review papers
have been published, summarizing various techniques, challenges, and future directions
within this field. These reviews not only define the various technologies but also discuss the
interplay between them, providing researchers with a clear theoretical framework for further
exploration. To provide a comprehensive understanding of the state-of-the-art in HIL-ML,
we compare three representative surveys that focus on different aspects of this field. Table 1
summarizes their key contexts, theoretical foundations, adaptation to LLMs, strengths, and
weaknesses, offering insights into the distinct contributions and limitations of each work.
Wu et al. (2022) conducted a comprehensive overview of HIL-ML from the perspective
of data management. They analyzed existing works on HIL, categorizing them into three
progressively related categories: (1) efforts to enhance model performance through data pro-
cessing, (2) improvements in model performance via interventional model training, and (3)
human-in-the-loop system design. Furthermore, the paper summarizes applications of HIL
and discusses its technical merits and limitations in fields such as natural language process-
ing and computer vision. However, the survey lacks theoretical depth, as it does not formal-
ize the role of human involvement in HIL-ML through mathematical models. Additionally,
it does not address the impact of large pre-trained models, which limits its relevance in the
context of modern LLMs. Despite these limitations, the survey’s focus on practical system
implementation offers valuable insights for engineering-focused studies in HIL-ML.
Beyond analyzing HIL from a data perspective, there has been significant research inter-
est in the interaction modalities between humans and machine learning algorithms and
leveraging these interactions to boost model performance. Eduardo Mosqueira-Rey et al.
have contributed a thorough overview of this area, defining the forms of HIL machine learn-
Table 1 A comparative analysis of surveys on HIL-ML
| Dimension | A survey of  | HIL-ML: state of    | Understanding  | Ours |
| --------- | ------------ | ------------------- | -------------- | ---- |
|           | HIL-ML (Wu   | the art (Mosqueira- | interactions   |      |
|           | et al. 2022) | Rey et al. 2023a)   | (Cui et al.    |      |
2021)
| Covers end-to-end workflow of ML        |     | X   | X   |     |
| --------------------------------------- | --- | --- | --- | --- |
|                                         | ✓   |     |     | ✓   |
| Provides a clear theoretical foundation | X   | ✓   | X   | ✓   |
| Discusses adaptation to LLMs            | X   | X   | X   | ✓   |
| Emphasizes user interaction and experi- | X   | X   | ✓   | ✓   |
ence optimization
| Shows innovative interaction design | X   | X   |     |     |
| ----------------------------------- | --- | --- | --- | --- |
|                                     |     |     | ✓   | ✓   |
1 3

266 Page 6 of 55 J. Gao et al.
ing such as Active Learning (AL), Interactive Machine Learning (IML), Machine Teaching
(MT), Curriculum Learning (CL), and Explainable AI (XAI) (Mosqueira-Rey et al. 2023a).
Their classification hinges on the locus of control within the learning process: active learn-
ing with the system in control, interactive machine learning with enhanced user-system
interaction, and machine teaching where human experts dictate the learning process. This
work provides a delineation of the various interactions and demarcations among different
HIL techniques, drawing connections and elucidating their influences. It offers a clear theo-
retical framework for researchers in the field, laying a foundational theory for the study of
HIL. However, it does not address the challenges posed by LLMs, limiting its applicability.
Although the HIL-ML field has explored various interaction types like demonstrations
and preferences, there is a notable lack of comparative analysis or guidelines for selecting
the most effective type to solve specific learning problems. Yuchen Cui et al. have intro-
duced a set of principles for organizing HIL that examines how different interaction types
affect human performance and the quality of training data (Cui et al. 2021). In addition,
they discuss strategies for selecting the most effective interaction type for particular learn-
ing issues and identify ongoing open questions in the field. While its focus on user-centric
design is innovative, the survey covers a narrow scope, lacks concrete application scenarios,
and provides minimal theoretical or experimental depth. Furthermore, it does not discuss the
potential integration of LLMs with HIL systems, which limits its applicability in addressing
contemporary challenges.
While previous reviews have comprehensively addressed the techniques, challenges, and
future directions of HIL-ML, the advent of large models has introduced new dynamics and
challenges into the HIL-ML landscape. Large models, equipped with extensive prior knowl-
edge, have reduced the reliance on human labor for traditionally labor-intensive tasks such
as complex data labeling. Consequently, research in the era of large models has shifted its
focus toward using human expertise for tasks like model fine-tuning, output validation, and
high-level guidance. This shift has not only lowered the overall cost of HIL systems but also
redefined the role of human involvement, making it more strategic and less resource-inten-
sive. To reflect these developments, we reviewed existing works and proposed an updated
framework, Agent-in-the-Loop Machine Learning, which integrates human with large-scale
models to address the evolving challenges in this domain.
2.2 Related research areas
There are several research fields closely related to AIL-ML, including but not limited to:
HIL-ML, Large Models, active learning and knowledge distillation. We briefly describe
them in the following.
Human-in-the-loop machine learning (Cui et al. 2021; Wu et al. 2022; Mosqueira-Rey
et al. 2023a) is a method that integrates human knowledge to guide and enhance machine
learning models. In HIL-ML framework, human participants contribute inputs not only dur-
ing data preprocessing, model training, and performance evaluation stages but also engage
in interactive feedback throughout the entire machine learning workflow. This approach
emphasizes the collaborative interaction between humans and algorithms with the goal of
optimizing the learning process, thereby improving the accuracy, interpretability, and reli-
ability of the models. HIL-ML is particularly suited for tasks that are too complex for auto-
mated systems or require human intuition.
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 7 of 55 266
Large model (Brown et al. 2020) typically refers to a type of machine learning model
characterized by a substantial number of parameters, often scaling into the billions. These
models, also known as large-scale models or foundation models (Bommasani et al. 2021),
are designed to process and generate data across various tasks and domains. They leverage
deep learning techniques and are predominantly neural network architectures such as trans-
formers (Vaswani 2017), which allow them to achieve state-of-the-art performance in areas
like natural language processing and computer vision. Large models are famous for their
ability to learn complex patterns and relationships within data, which facilitates advanced
reasoning and generalization capabilities beyond specific tasks, contributing significantly to
advancements in artificial intelligence.
Active learning (Settles 2009; Mosqueira-Rey et al. 2023a) is a machine learning
approach where the learner (often a model) selectively queries an oracle (typically a human
annotator acting as a teacher) to label examples that are ambiguous but likely to provide sig-
nificant insights to the learning process. This targeted approach allows the learner to enhance
their performance with fewer training examples. Active Learning is particularly effective in
environments rich in unlabeled data where the annotation task is costly or time-consuming.
This method strategically reduces the volume of data that needs labeling while maximizing
learning efficiency and effectiveness. Active Learning is indeed a method within HIL-ML.
Knowledge distillation (Xu et al. 2024; Gou et al. 2021; Hinton 2015) is a technique
where knowledge is transferred from a larger, more complex model (often called the teacher)
to a smaller, simpler model (often called the student). The goal of knowledge distillation is
to enable the student model to achieve performance comparable to the teacher model but
with reduced computational complexity and memory requirements. This is particularly use-
ful for deploying high-performing models on devices with limited resources, such as mobile
phones and embedded systems. Knowledge distillation has become a popular method for
model compression and is extensively used to enhance the efficiency of deploying deep
learning models in resource-constrained environments.
3 Methodology
This section will provide a detailed introduction to the implementation of AIL-ML. As
shown in Fig. 3, we categorize the existing work into two main parts: data acquisition and
processing, and model development and optimization.
In data acquisition and processing, we discuss several key steps: first, during the data
collection stage, we explain how agents participate in and optimize the data collection pro-
cess (Wu et al. 2020; Hiremath et al. 2022; Hancock et al. 2019; Xu et al. 2022; Long et al.
2023; Ding et al. 2022; Xu et al. 2023; Sahu et al. 2023; Gao et al. 2023; Ye et al. 2022);
second, in the data initialization stage, we explore how agents transform collected raw data
into formats suitable for machine learning (Zhang et al. 2019; Oh et al. 2019; Kath et al.
2023; Hsieh 2023b; Chen et al. 2021b; Cai et al. 2019; Park et al. 2023); next, during the
data quality enhancement stage, we introduce how agents help improve the quality of data
(Wu et al. 2020; Xu et al. 2022; Yu et al. 2015; Li 2017, 2017; Yao et al. 2019a; Liu et al.
2021; Wallace et al. 2019; Bartolo et al. 2020; Arakawa et al. 2023; Cho et al. 2023; Wang
et al. 2021; Hsieh et al. 2023a; Wang et al. 2023b; Dai et al. 2023; He et al. 2023a; Gao et al.
2023); finally, in the data annotation stage, we explore how agents use their knowledge for
1 3

266 Page 8 of 55 J. Gao et al.
Fig. 3 Taxonomy of Agent-in-the-Loop Machine Learning
precise and effective data labeling (Wu et al. 2020; Xu et al. 2022; Yu et al. 2015; Hancock
et al. 2019; Hiremath et al. 2022; Li 2017; Zhang et al. 2019; Liu et al. 2021; Klie et al.
2020; Qian et al. 2020; Kath et al. 2023; Hsieh 2023b; Hemmer et al. 2022; Cui et al. 2021;
Koppol et al. 2021; Cai et al. 2019; Wang et al. 2021; Ding et al. 2022; He et al. 2023b;
Hsieh et al. 2023a; Sahu et al. 2023; Wang et al. 2024; Lu et al. 2024).
In the model development and optimization part, the focus is on three core segments:
firstly, we discuss how AIL-ML strategies effectively address the model cold start problem
(Hiremath et al. 2022; Zhang et al. 2019; Wang et al. 2022; Ben-David et al. 2006; Zhuang
et al. 2020; Xu et al. 2022; Arakawa et al. 2023; Wang et al. 2021; Ding et al. 2022; Xu et al.
2023; Hsieh et al. 2023a; Ye et al. 2022; Li et al. 2024); secondly, during the model training
phase, we detail how agents’ advanced knowledge is used to calibrate model parameters and
optimize the learning framework (Arous et al. 2021; Oh et al. 2019; Kath et al. 2023; Wei et
al. 2022; Wang et al. 2023a; Roels et al. 2019; Weber et al. 2020; Kwon and Michael 2023);
and lastly, in the model iterative enhancement phase, we emphasize how continual interven-
tion and feedback from agents incrementally enhance the performance of machine learning
models through multiple iterations (Wu et al. 2020; Hancock et al. 2019; Yao et al. 2019b;
Qian et al. 2020; Stiennon et al. 2020; Ouyang et al. 2022; Crochepierre et al. 2022; Fan et
al. 2024; Ahn et al. 2023; Arakawa et al. 2023; Ziegler et al. 2019; Xu et al. 2023; He et al.
2023a; Sun et al. 2024; Klissarov et al. 2023; Guo et al. 2024).
By introducing the AIL-ML concept, we effectively leverage the strengths of human
and large models to construct efficient, accurate, and adaptable machine learning models.
Agents play a pivotal role in data acquisition and processing, as well as in model develop-
ment and optimization. This strategy of combining human wisdom with machine power
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 9 of 55 266
offers a new possibility for constructing efficient, precise machine learning models, pushing
the technology to higher levels of achievement.
3.1 Data acquisition and processing
In the field of machine learning, data and models are intricately linked. The collection and
initialization of data directly influence the construction and performance of models. More-
over, enhancing data quality is crucial for the iterative improvement of models. This inter-
action between data and models forms a mutually beneficial relationship, highlighting the
importance of data quality in improving model performance. In this section, we investigate
AIL-ML techniques that focus on optimizing the entire data lifecycle in machine learning.
This includes a detailed examination of methods in the areas of Data Collection, Data Ini-
tialization, Data Quality Enhancement, and Data Annotation.
3.1.1 Data collection
In this section, we explore the data collection mechanisms within the AIL-ML framework,
where agents can be humans, large models, or a combination of both. Agents play a crucial
role in generating diverse, comprehensive, and representative data sets, essential for training
complex machine learning models. This not only broadens the scope of training data but also
enhances the model’s generalization capabilities and adaptability to complex environments.
3.1.1.1 Mathematical framework for data collection In this part, we establish a foundational
mathematical framework to systematically describe the data collection mechanisms within
the AIL-ML architecture. This framework is summarized by the following general equa-
tions, which form the various data collection strategies discussed in subsequent sections.
x t =f(S t ,D t ,M t ,A t ) (1)
where:
● x t represents the data generated by the agent at time t,
● S t represents the seed datasets at time t,
● D t and M t represent the current dataset and model, respectively,
● A t denotes the actions or decisions of the agent at time t, which may include inputs from
humans H t and large models L t,
● f is a function defining how data is generated based on the current data set, model state,
agent state, and actions.
Additionally, the process by which agents generate data based on given labels can be for-
malized through a conditional probability model:
x t =p(x y,S t ,D t ,M t ,A t ) (2)
|
where:
1 3

266 Page 10 of 55 J. Gao et al.
● x t is the data generated by the agent at time t,
● y is the provided label,
● p(x y,S t ,D t ,M t ,A t ) is a conditional probability distribution indicating the likeli-
|
hood of generating data x given the label y, current seed dataset S t, data set D t, model
state M t, and agent actions A t.
These formulations offer a comprehensive description of data collection under the AIL-
ML framework, illustrating how to utilize agents’ internal state, model state, and available
data, along with potential external labels, to acquire data. This highlights the dynamic and
adaptive nature of AIL-ML. In the subsequent sections of the chapter, each data collection
strategy will be mapped to these general formulas.
Research analysis indicates that the AIL-ML framework utilizes three primary data col-
lection strategies, each corresponding to different stages of the machine model’s lifecycle.
These strategies include data collection before model construction, during model construc-
tion, and after model construction.
3.1.1.2 Data collection before model construction Before model construction, data collec-
tion is suitable for the following two scenarios. Firstly, these strategies are suitable for tasks
that require highly specific data and lack large-scale public datasets (Long et al. 2023). For
example, in the Internet of Things (IoT) context, various sensors are positioned at different
locations. Due to the lack of public dataset, researchers need to collect the data. It is essential
that the data should be not only abundant but also diverse and representative, to effectively
capture the diverse potential states of the real-world environment. For instance, Hiremath
et al. (2022) demonstrate how data is passively observed and collected through sensor net-
works installed in different locations within smart home systems. This network, containing
door sensors, motion sensors, and temperature sensors, continuously monitors environmen-
tal changes and logs events with timestamps and sensor IDs. The data, stored in event logs
on local servers or in the cloud, forms the basis for subsequent processing and analysis.
Similarly, Wu et al. (2020) presented a system that automatically collects environmental
sound signals through smart speakers. This system utilizes unsupervised clustering tech-
niques to identify recurring activity types. Once the system can identify specific activities
with high confidence, it starts a one-shot interaction with users through voice commands.
This interaction is used to label these activities and create a labeled dataset. This approach
allows the system to improve the accuracy of environmental sound recognition incremen-
tally through Continuous learning and in-situ training, without the need for predefined data.
Consequently, it develops an accurate, environment-specific, acoustic signal-based activity
recognition model. In this scenario, the data collection process can be modeled as:
x t =f(∅,∅,∅,A t ) (3)
Here, ∅ indicates that the seed dataset S t, the current dataset D t and the model state M t
are not involved in the data generation process in this data collection strategy. This is due
to the lack of this information before the model has been constructed. For convenience in
expression throughout the remainder of this paper, ∅ will not be explained any more. A t
represents the user’s daily activities at time t. In this case, A t represents the user’s daily
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 11 of 55 266
activities, e.g., daily operations in the smart home, which generate corresponding data x t
through sensor activation or sound recording. The function f defines how the sensor data is
collected and generated based on the behavior A t of the agent through sensor activations or
sound recordings.
Secondly, data collection before model construction is suitable for tasks leveraging large
models for data generation. Trained on vast amounts of data, large models have accumu-
lated extensive general knowledge and demonstrated remarkable abilities in reasoning and
analysis. This allows researchers to use large models to generate high-quality data, signifi-
cantly reducing the time and costs. This enables both individuals and small organizations to
utilize advanced AI technologies more effectively. Through well-designed prompt engineer-
ing, researchers can direct large models to generate specific datasets on demand, optimizing
both the training process and model performance. Ding et al. (2022) proposed an approach
named Prompt-Guided Training Data Generation (PGDG). This method leverages the gen-
erative capabilities of GPT-3 to produce labeled data pairs directly from specific prompts,
significantly enhancing the efficiency and quality of data generation. For tasks such as senti-
ment analysis and relationship extraction, the data generated through this method matches
or even surpasses the quality of manually annotated data with reducing time and cost. Addi-
tionally, large models can generate diverse data using seed datasets. In Xu et al. (2023), C
Xu et al. detailed how to use seed datasets to collect high-quality, multi-turn dialogue data
through self-chat. They chose platforms like Quora and Stack Overflow as seed datasets.
These platforms provide a wealth of user-generated questions that guide the generation of
dialogues by ChatGPT, which simulates both sides of a conversation. Each dialogue began
with a seed question and naturally progressed through several rounds of exchanges until
it ended. To ensure the quality and format of the dialogues, researchers used predefined
templates to control the dialogue generation process. This method not only addresses the
scarcity of high-quality, multi-turn dialogue but also offers a practical solution due to its
efficiency and relatively low cost. To further enhance the diversity and quality of the gener-
ated data, researchers have designed various generation strategies (Ye et al. 2022; Gao et al.
2023; Sahu et al. 2023), such as Greedy Search, Top-k Sampling, and Nucleus Sampling.
These strategies aim to improve the diversity and quality of the generated text. Such inno-
vative techniques ensure that the data generated is both varied and of high quality, suitable
for training robust models. This data generation process can be described by the equation:
x t =f(S t ,∅,∅,A t ) (4)
where S t represents the seed dataset, such as user questions from Quora and Stack Overflow
in Xu et al. (2023). A t denotes the agent’s actions, such as ChatGPT generating dialogues
based on the seed questions. The function f defines a function or process that generates data
x t based on S t and A t.
3.1.1.3 Data collection during model construction During model construction, the continu-
ous collection of data through agents can enable the model to better adapt and learn under
complex or unfamiliar environmental conditions. Moreover, this can make model identify
potential biases. In Hancock et al. (2019), data collection spans the entire lifecycle of the
dialogue model, particularly post-deployment. Through real-time interactions with users,
the system continuously collects new training data, including Human-Bot (HB) dialogue
1 3

266 Page 12 of 55 J. Gao et al.
data and user feedback data. When the model assesses high user satisfaction in a conversa-
tion, the user’s responses are recorded as HB dialogue data. Correspondingly, when the
model anticipates potential errors, it requests feedback from users, which is then used to
refine the model. This collected data, after processing and storage, is regularly utilized for
retraining the model, enabling it to continually learn and improve in practical applications,
thereby enhancing conversational abilities and user satisfaction. This approach not only
reduces the dependency on manually annotated data but also allows the model to rapidly
adapt to new conversational contexts, significantly improving user experience and model
performance. The data collection process in this scenario can be represented by:
x t =f(∅,∅,M t ,A t ) (5)
In this context, M t represents the state of the model at time t, such as the chatbot in Hancock
et al. (2019). The state of the model evolves over time as more training data is accumulated
and the model is updated. A t denotes the agent’s actions, which include user interactions
and feedback that generate new training data. And f is the core mapping function of the data
collection process. In this context, it transfers the current model state M t and agent’s action
A t to new training data x t.
3.1.1.4 Data collection after model construction After model construction, the collection
of data from agents can allow models to handle new types of tasks. For example, in ges-
ture recognition systems, allowing users to personalize their gestures can enhance gesture
memorability, increase interaction efficiency, and improve accessibility for individuals with
specific needs. Xu et al. propose a framework for gesture customization using few-shot
learning, where users provide only a few custom gesture examples to the system (Xu et al.
2022). This method enables the system to recognize customized gestures with high accuracy
without compromising the performance of existing gestures. Specifically, users record new
gestures on a smartwatch interface, and the system guides them through data collection via
an interactive interface. The system continuously monitors performance and provides feed-
back to users. If the model’s accuracy falls below expectations, the system guides users to
record more samples to further optimize the model. This data collection process can also be
described by the equation:
x t =f(S t ,D t ,M t ,A t ) (6)
where S t is the seed dataset, such as negative samples (e.g., daily activities) and existing
gestures. D t represents the training dataset at time t, which evolves as new customized
gestures in Xu et al. 2022. M t denotes the current model such as the gesture recognition
model in Xu et al. 2022. And A t stands for the agent’s actions, such as providing customized
gesture data to the system in Xu et al. 2022. Through S t, D t and M t, the system can prevent
the agent’s custom gestures from being too similar to existing gestures, thereby avoiding
overfitting to new gestures and forgetting old gestures. Additionally, by incorporating nega-
tive samples in S t, the system can prevent conflicts between new gestures and the user’s
daily activities.
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 13 of 55 266
3.1.1.5 Analysis of data collection in AIL-ML In the aforementioned sections, we have
provided mathematical representations for three distinct data collection strategies corre-
sponding to different stages of the model lifecycle: before model construction, during model
construction, and after model construction. These mathematical formulations vary in their
functional structures and conditional elements, reflecting the unique data collection method-
ologies and technical characteristics inherent to each phase. By comparing these mathemati-
cal models, we can discern the specific features and limitations of each strategy, understand
the trade-offs they entail, and identify the conditions under which the formulas might be
extended to yield additional benefits.
Data Collection Before Model Construction primarily focuses on assembling comprehen-
sive and representative datasets necessary for initializing the model. At this stage, the data
collection process is typically represented by the equations x t =f(A t ) or x t =f(S t ,A t ).
Prior to model construction, researchers generally lack a trained model or sufficient existing
data, rendering M t and D t either nonexistent or minimal. Consequently, data collection is
primarily driven by external factors such as sensor monitoring, user activities, or data gen-
erated by large models based on seed datasets. The simplified function f(A t ) or f(S t ,A t )
reflects an externally driven data collection process, where user activities or prompts guide
data generation without considering the model’s dynamic adaptation. This omission of M t
reduces the complexity but means that data quality and diversity rely only on external con-
ditions like activity patterns and the scope of seed datasets, lacking a feedback loop from
the model. This approach offers the advantage of accumulating substantial data prior to
model training, reducing potential data gaps in later stages, and leveraging large models to
enhance data quality while minimizing annotation costs. However, the main challenge lies
in designing effective data collection strategies and avoiding errors or biases in the data gen-
erated by large models. The absence of M t leads to a more efficient and straightforward data
generation process, but it sacrifices the ability to collect data tailored to the model’s evolv-
ing needs, highlighting the trade-off between simplifying data collection at the expense of
adaptive data collection capabilities.
Data Collection During Model Construction integrates data acquisition into the train-
ing process itself. During this phase, the data collection process is typically modeled as
x t =f(M t ,A t ). Unlike the pre-construction stage, the model’s current state M t plays a sig-
nificant role in guiding data collection. This phase utilizes real-time data generated through
user interactions and user feedback. The model is in a transitional state, undergoing train-
ing or initial deployment with partial parameters and structures. The collected data reflects
actual usage scenarios, facilitating rapid model adaptation and continuous optimization.
Incorporating M t into the function allows data collection to be dynamically adjusted based
on the model’s current performance and identified biases, facilitating continuous improve-
ment and adaptation. The key benefits include data that closely reflects deployment envi-
ronments, enabling rapid iterations and mitigating bias, while also reducing dependence
on manual annotations. However, challenges related to data noise and variability in feed-
back quality remain, requiring robust feedback processing and ongoing model maintenance.
Including M t enhances data collection specificity and adaptability but introduces additional
complexity. Real-time access to and processing of the model’s state require more advanced
infrastructure, increasing both computational and operational overhead.
1 3

266 Page 14 of 55 J. Gao et al.
Data Collection After Model Construction emphasizes the personalization and extension
of the model’s capabilities to handle new tasks. In the post-construction phase, data collec-
tion is represented by x t =f(D t ,M t ,A t ), sometimes including S t. This comprehensive
formulation accounts for the existing dataset (D t), the model’s state (M t), and the agent’s
actions (A t). With a fully trained and deployed model, data collection focuses on personal-
ization and task extension. The existing dataset ensures consistency and prevents the model
from forgetting previously learned information, while the model’s state guides the acquisi-
tion of new, relevant data. By integrating D t and M t, the system can effectively manage
the introduction of new data, ensuring that user-specific data do not overlap excessively
with existing data, thereby avoiding overfitting and maintaining overall model performance.
Data collection mechanisms here are user-driven, with agents actively providing specific
data samples based on performance feedback. This strategy allows for the addition of new
tasks without degrading existing model performance by preventing overfitting to new data
and forgetting previously learned information through the inclusion of negative samples.
However, challenges include avoiding excessive bias towards individual users and ensuring
a balanced integration of new data with existing knowledge.
The equation x t =f(S t ,D t ,M t ,A t ) can flexibly represent various data collection sce-
narios by selectively omitting certain terms based on the specific phase. This flexibility
allows the framework to adapt to different strategies without compromising its general
applicability. Introducing additional terms such as M t or D t in specific contexts enables
finer control and optimization of data collection strategies. For example, evolving from
f(A t ) to f(M t ,A t ) allows for model-driven data collection, enhancing iterative training
and correction processes. From the analysis, we can derive the following high-level insights:
● Data collection strategies can align with the model’s lifecycle stages. Before model
construction, extensive data accumulation and generation are crucial for robust initial
training. During construction, real-time data collection supports continuous learning
and bias correction. After construction, personalized data collection enables the model
to adapt to specific user needs and new tasks.
● Each phase involves trade-offs. Pre-construction strategies reduce annotation costs and
ensure data diversity but require careful planning and quality control. During construc-
tion, real-time data accurately captures user interactions but introduces variability and
noise. Post-construction strategies enhance personalization and adaptability but risk
overfitting and require effective data management to preserve existing knowledge.
● Methodological versatility is essential, enabling researchers to select or combine strate-
gies based on task requirements, data availability, and resource constraints. This ensures
data quality, diversity, and dynamic adaptability within the AIL-ML framework.
3.1.2 Data initialization and preprocessing
Data initialization and preprocessing are crucial steps that transform raw data into a format
suitable for machine learning models. In this section, we will introduce the AIL-ML tech-
niques that initialize and preprocess data through agents.
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 15 of 55 266
3.1.2.1 Mathematical framework for data initialization and preprocessing How to utilize
agents for data initialization and preprocessing can be described as follows:
F t =ψ(D t ,A t ,P f ) (7)
where:
● F t represents the feature set derived at time t,
● as defined previously, D t and A t continue to denote the current data set and the agent’s
actions or decisions,
● function ψ serves as a data transformation function, incorporating all essential preproc-
essing steps such as data cleaning, normalization, and feature extraction,
● P f stands for the set of preprocessing parameters.
Upon reviewing AIL-ML literature, we identified two main methodologies that utilize
agents for data initialization and preprocessing: Data Analysis and Feature Representation.
These methodologies leverage agents to perform data analysis (Zhang et al. 2019; Hsieh
2023b; Chen et al. 2021b), Wei et al. 2022 or to develop effective feature representation (Oh
et al. 2019; Kath et al. 2023; Cai et al. 2019).
3.1.2.2 Data analysis Data analysis by agents involves examining large datasets to discern
underlying patterns and valuable insights that are not immediately apparent. This process is
vital for preparing data in a way that significantly enhances the training and performance of
machine learning models. Zhang et al. (2019) employed a high-recall regular expression to
detect potential entity candidates within texts. Initially, experts design preliminary regular
expressions suitable for specific entity extraction tasks, such as dates, email addresses, and
course numbers, aiming to capture most target entities. Then, these expressions are used to
scan documents, extracting all matching substrings. Each matched substring is expanded
to include surrounding text, providing sufficient contextual information for its validation
as a target entity. This method creates a collection of candidate substrings, encompassing
all potential entities, significantly narrowing the scope of text that needs further process-
ing and thereby enhancing the efficiency of subsequent annotation and model training. For
tasks that require expert knowledge, the AIL-ML strategy distills the deep knowledge and
understanding of human experts into ML models through data analysis. Hsieh (2023b) lev-
eraged expert knowledge in the data initialization and preprocessing stages. They utilize
chest X-ray images, eye-tracking data from radiologists, and patients’ clinical data. The
eye-tracking data, which includes gaze points and sequences during the diagnostic process,
is mapped to image coordinates to extract the visual search patterns of the radiologists. Con-
currently, clinical data is encoded and standardized to align dimensionally with 3D image
data, and expanded through convolution layers for effective integration with image data.
Through these steps, the diagnostic behaviors and knowledge of human experts are effec-
tively distilled into the model, enabling it to learn from the experts’ diagnostic processes.
In this scenario, the data initialization and preprocessing can be formalized by Eq. 7. The
specific components of the formula are summarized in Table 2.
1 3

266 Page 16 of 55 J. Gao et al.
Table 2 Symbol descriptions for Symbol HIL entity extraction (Zhang Chest X-Ray diagno-
data analysis et al. 2019) sis (Hsieh 2023b)
Dt Text dataset Chest X-ray images
At Design of regular expressions Looking at the chest
for entity extraction X-ray images during
the diagnostic process
Pf Time allocation between con- Parameters for
structing regular expressions data encoding and
and labeling data integration
3.1.2.3 Feature representation On the other hand, agents are used for feature representa-
tion, which transforms raw data into a structured format more suitable for subsequent algo-
rithmic processing. This transformation ensures that the data are formatted to maximize
the efficiency and accuracy of the machine learning model. In Oh et al. (2019), agents’
interaction and feedback play important roles in feature representation. Users annotate
video frames, for instance by delineating foreground and background, providing essen-
tial feature information. These annotations are used to generate object masks and serve
as feature inputs to help the network and represent foreground objects. The user-provided
data is then encoded into a format suitable for network processing, such as binary masks
representing positive and negative examples. The interaction network combines this infor-
mation with video frame data and transforms it through a feature encoding module into
high-dimensional features suitable for model processing. Ultimately, these encoded data are
integrated into a multi-channel input tensor for the interaction and propagation networks,
ensuring the model effectively utilizes the initial information provided by users to enhance
performance and prediction accuracy. Beyond low-dimensional data, agents can also repre-
sent feature for high-dimensional sensory data, such as images. Park et al. (2023) proposed
Localized Symbolic Knowledge Distillation (LSKD), a framework designed for efficient
image feature representation. This framework leverages multi-modal large models to extract
global image features, encompassing scenes, objects, and conceptual information, which are
organized into Global Descriptors. Simultaneously, candidate regions within the image are
identified, and fine-grained Local Descriptors are generated for each region using vision-
language models. Additionally, LLMs generate commonsense knowledge tied to specific
regions, which is refined through a supervised"critic model"to remove inconsistencies. This
approach effectively integrates global and local information. It also enhances semantic rep-
resentations through dynamic reasoning, providing robust inputs for subsequent inference
and learning tasks.
Furthermore, agents can optimize feature representation. Kath et al. (2023) presented
an interactive machine learning tool for annotating passive acoustic monitoring datasets
created for wildlife monitoring. Users can select data points within a state-space representa-
tion and create new boundaries, further refining feature representation. Through real-time
feedback, the model dynamically adjusts feature representations and prediction outcomes,
gradually improving accuracy with each retraining cycle. Cai et al. (2019) developed tools
that helped pathologists cope with the shortcomings of deep learning algorithms during
image retrieval. These tools are designed to adjust retrieval algorithms in real time to bet-
ter meet the diagnostic needs of doctors and enhance their trust in the algorithms. While
using the SMILY system, pathologists refine and optimize image feature representations
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 17 of 55 266
through tools like regional, example-based, and conceptual refinement. These tools allow
pathologists to emphasize or remove irrelevant features, ensuring the model focuses on cor-
rect diagnostic features. This process of real-time interaction and feedback can be seen as
a dynamic method of data preprocessing, aiding in the improvement of the model’s feature
representation.
This kind of data initialization and preprocessing can be described by Eq. 7. A detailed
listing of the parameters involved is provided in Table 3
3.1.2.4 Analysis of data initialization and preprocessing in AIL-ML We analyze two pri-
mary methodologies of data initialization and preprocessing in the AIL-ML literature: Data
Analysis and Feature Representation.
Data Analysis is to derive richer context and insights from raw data. Agents assist in
identifying critical patterns, candidate entities, and key structural elements that may not be
easy to detect. For example, through expert-driven strategies such as hand-crafted regular
expressions or the integration of human-derived signals (e.g., eye-tracking data from radi-
ologists), data analysis steps ensure that downstream ML models start from a more semanti-
cally meaningful and contextually informed baseline. Human expertise often guides data
analysis through the design of rules or domain-specific entity extraction patterns. Agents
can leverage human guidance to more efficiently sift through large datasets, reducing noise
and focusing attention on key data segments.
Feature Representation focus on how to encode that information so it becomes directly
usable by machine learning models. Agents and users collaboratively shape the feature
space to highlight the most relevant characteristics of the data-refining object masks in
video frames, delineating meaningful acoustic signals from background noise, or emphasiz-
ing clinically significant image features. These approaches transfer high-dimensional data
into representations that enhance learning performance. Agent feedback can be real-time
and iterative, allowing agents to refine, reshape, and optimize the feature space as the model
trains.
3.1.3 Data quality enhancement
Data quality is important for model training and its subsequent performance. In this section,
we explore AIL-ML methods related to enhance data quality. By identifying and correcting
discrepancies, biases, and errors in raw data, agents significantly enhance the precision and
Table 3 Symbol descriptions for feature representation
Symbol User-guided video segmentation (Oh et HIL acoustic annotation (Hsieh LSKD
al. 2019) 2023b) and Human-centered medi- (Park et al.
cal tools (Cai et al. 2019) 2023)
Dt Video frames Raw data Images
At User annotations indicating foreground Real-time user feedback and Generat-
and background regions, directly influ- interactions that guide feature ing global
encing the feature extraction process refinement and local
descriptions
Pf Parameters related to mask generation Parameters for feature Parameters
optimization for feature
extraction
1 3

266 Page 18 of 55 J. Gao et al.
consistency of the data. Moreover, agents play a key role in augmenting the diversity and
richness of data
3.1.3.1 Mathematical framework for data quality enhancement To explain how agents
enhance data quality within AIL-ML framework, we adopt the following general formula:
D t+1 =θ(D t ,A t ,Q) (8)
where:
● D t+1 denotes the enhanced dataset at time t+1 after data quality enhancement,
● as defined previously, D t and A t continue to denote the current data set and the agent’s
actions or decisions,
● Q represents a set of parameters for data quality enhancement, defining specific quality
control operations (e.g., noise thresholds, labeling consistency checks, or optimization
strategies),
● θ represents a general-purpose function for enhancing data quality through a series of
operations. These operations include data cleaning, data diversity enhancement by syn-
thesizing new samples and expanding the dataset, improving consistency and accuracy
by adjusting mislabeled samples and reducing uncertainty and so on.
There are two primary AIL methodologies by which agents can enhance data quality: 1)
improving data accuracy or consistency, (Wu et al. 2020; Yu et al. 2015; Li 2017; Arous et
al. 2021; Arakawa et al. 2023; Cho et al. 2023; Gao et al. 2023, 2024) and 2) increasing data
diversity (Xu et al. 2022; Yao et al. 2019a; Liu et al. 2021; Wallace et al. 2019; Bartolo et al.
2020; Hsieh et al. 2023a; Dai et al. 2023).
3.1.3.2 Improving data accuracy The first methodology focuses on improving the accuracy
and consistency of the data. For machine learning, enhancing data precision and consis-
tency can improve model performance. The knowledge and analytical capabilities of agents
can significantly augment data accuracy, thereby enhancing model precision. In the context
of smart home environments, Cho et al. (2023) introduced a novel strategy named AI-to-
Human (AHA), which actively modifies environmental conditions to enhance the inferen-
tial accuracy of AI models. Unlike traditional smart devices, such as embedded vision AI
sensors that passively monitor resident activities, AHA actively induces resident behaviors,
facilitating more reliable AI inferences. Initially, AI sensors detect poor perception condi-
tions, such as orientations away from the camera or distances too close or too far from the
camera. Then, the AHA system employs smart home devices like speakers, displays, or
ambient lighting to unremarkably guide resident behavior into more favorable perceptual
conditions. The AHA system effectively improves data quality and overcomes the common
challenges of passive perception inherent in traditional methods. Similarly, Listen Learner
(Wu et al. 2020) employs an active learning approach that enhances data quality through
various interactive strategies with users, including open-ended questions, confirmation
questions, and refinement questions. When a new event falls into the decision boundary of
the model, the system will ask a choice question as a confirmation question. This not only
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 19 of 55 266
reduces the cognitive load on users but also enhances the quality of data, adapting dynami-
cally to different environmental sounds, thus improving data precision and the accuracy
of classification models. Furthermore, some AIL-ML methods enhance data precision by
incorporating human reasoning. For instance, the MARTA framework (Arous et al. 2021)
introduces human rationales combined with Bayesian methods to assess agent reliability,
thereby enhancing data precision quality. Agents provide not only document labels but also
rational segments supporting these labels. During training, the model weights these rational
segments based on agent reliability, ensuring that high-quality rational segments contribute
more.
Researchers have implemented various methods to manage and control the quality of
agent annotations. In LSUN (Yu et al. 2015), annotation quality control is achieved through
several strategies including redundant annotations, quality checks, and detailed annota-
tion guidelines. Specifically, each item is annotated by at least two independent annota-
tors to ensure consistency in the results. Items with known labels are embedded within the
annotation tasks to monitor the annotators’ performance. Both online and offline quality
control mechanisms ensure that annotators deliver high-quality results. Detailed annotation
guidelines and examples help annotators understand the requirements of the task clearly.
Together, these methods ensure the high quality and consistency of the annotated data.
Some researchers employed agents to identify and correct discrepancies, biases, and
errors in raw data, significantly enhancing data consistency and model accuracy. Gao et
al. (2024) proposed LLMIE-UHAR, which leverages Large Language Models (LLMs) and
Iterative Evolution for Unsupervised Human Activity Recognition. This method capitalizes
on the logical reasoning capabilities of LLMs to detect inconsistencies within datasets. This
is particularly important for unsupervised learning where labels are absent. The effective-
ness of LLMIE-UHAR shows the potential of LLMs to improve data quality in real-world
applications. This capability of agents to augment data quality forms a critical component in
the development of more robust, efficient, and reliable machine learning systems.
There are some AIL methods that enhance data precision by reducing data noise. Ara-
kawa et al. (2023) proposed PrISM-Tracker, which incorporates human input to manage
data uncertainty. This framework actively interacts with user input when model predictions
are uncertain, effectively reducing noise and uncertainty of data. Particularly in smart home
environments, where sensor data may be noisy or the sequences of actions unclear. Addi-
tionally, to address the challenge of initial low-quality data generation by large models, Gao
et al. (2023) introduced the SUNGEN framework, which uses language models to generate
synthetic data with task descriptions and label information. This initial data often includes
samples with incorrect labels or irrelevant content that can lead to model overfitting and
reduced generalization. The SUNGEN framework fixes this by employing a dual-layer opti-
mization process: an inner loop optimizes model parameters using weighted cross-entropy
loss, while an outer loop uses a noise-robust loss function to evaluate model performance
on a synthetic validation set. This iterative process refines sample weights, enhancing the
selection of high-quality data.
To make it clearer how the cited works integrate into Eq. 8, we present them in Table 4.
3.1.3.3 Enhancing data diversity The second methodology emphasizes broadening the
range of data variability, which is vital for training robust models capable of performing
1 3

266 Page 20 of 55 J. Gao et al.
Table 4 Symbol description for methods emphasizing data accuracy and consistency
Method Agent actions (At) Key parameters Data quality enhance- Output (Dt+1)
(Q) ment function (θ)
AHA (Cho et al. Modifying environ- Perception thresh- Detecting poor More accurate
2023) ment (e.g., lighting olds, environment conditions and adjusts sensor data
or orientation) to triggers environment
improve perception
Listen Learner Asking confirmation Uncertainty Identifying uncertain Refined data-
(Wu et al. 2020) or refinement ques- bounds, question samples and refin- set with reduced
tions to users for formats ing labels via user boundary noise
uncertain events feedback
MARTA (Arous Providing human Bayesian weight- Weighing agent reli- Refined labeling
et al. 2021) rationales along with ing parameters ability and rationales inDt+1, empha-
labels to adjust final labels sizing high-qual-
ity rationales and
improving overall
data consistency
LSUN (Yu et al. Providing multiple Required an- Merging annotator Consistent and
2015) labels, with known- notations per inputs and filters low- high-quality data,
label checks as a item, known- quality labels reduced annotator
control label embedding, errors
online/offline QC
thresholds
LLMIE- Detecting and LLM prompts, Using LLM reasoning Logically consis-
UHAR (Gao et correcting dataset logical constraints to identify mis- tent data
al. 2024) inconsistencies matched samples and
correct them
PrISM-Track- Correcting the data Uncertainty trig- Collects user clarifica- Reduced noise
er (Arakawa et when model predic- gers, user feedback tions to disambiguate and uncertainty in
al. 2023) tions are uncertain rules noisy sensor data sensor readings,
better clarity in
time-series
SUNGEN (Gao Employs a dual- Weighted cross- Iteratively adjusts Higher overall
et al. 2023) layer optimization entropy, noise- sample weights and data quality,
for synthetic data robust loss filters out faulty fewer mislabeled
synthetics synthetic samples
well across diverse scenarios. Enhancing the diversity of data can not only improve the
generalization ability but also ensure superior performance on unseen samples of machine
learning models.
Synthetic data generation is a prevalent method for enhancing data diversity in machine
learning. This approach involves creating new data based on the characteristics of existing
data to increase the diversity of the data available for model training. Liu et al. (2021) intro-
duced a method for global feature contribution analysis, which combined human evaluation
to identify error features of the model. This method performs a local feature contribution
analysis and quantifies each feature’s contribution. Subsequently, it calculates the global
contributions of each feature to identify those with significant impacts on model predictions.
Agents are employed to annotate and verify these global features, evaluating their contribu-
tion and correctness. This methodology not only improves the generalization capabilities
of the data but also model’s performance on unseen data, enhancing the robustness and
reliability of model’s. Moreover, large models can synthesize data to increase diversity. In
Hsieh et al. (2023a), after employing Chain-of-Thought prompting techniques, large models
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 21 of 55 266
generate natural language inferences that include both the final labels and detailed inter-
mediary steps and logical explanations, providing richer and more useful training data for
smaller models. The inferential content generated by large models significantly improves
the context and detail quality of the training data.
By adding small perturbations to the original samples, adversarial examples can greatly
reduce the accuracy of the original classifier and achieve the purpose of anti-deep learning
Pan et al. (2020). Because past approaches expose superficial patterns, the resulting adver-
sarial examples are limited in complexity and diversity. To address these shortcomings,
Wallace et al. (2019) proposed an AIL-ML framework for generating adversarial examples.
Researchers have applied this generation framework to a question answering task called
Quizbowl, where trivia enthusiasts craft adversarial questions. The questions generated
within this framework were tested through live human-computer matches, demonstrating
that while these questions appeared ordinary to human participants, they systematically
stump neural and information retrieval models. Agent-involved adversarial example genera-
tion is effective, which not only increases the diversity and complexity of the data but also
enhances the models’ generalization capabilities (Bartolo et al. 2020).
Data augmentation plays a pivotal role in enhancing data diversity. Xu et al. (2022)
have developed a user-defined gesture recognition framework that requires participants to
provide a few custom gesture examples. After acquiring these gestures, the system employs
multiple data augmentation methods to generate additional samples: 1)zooming, to simulate
different gesture speeds; scaling, to simulate different gesture strengths; time-warping, to
simulate gesture temporal variance. Thus, these augmented samples increase the diversity
of the data. Additionally, large models, pre-trained on extensive datasets, have been fine-
tuned with reinforcement learning from human feedback (RLHF) to generate text similar
to human expression. Dai et al. (2023) utilized large models to generate diverse and high-
quality textual data as data augmentation, which rephrases each sentence in the training
samples into multiple conceptually similar but semantically different samples. The aug-
mented samples can then be used in downstream model training. Data augmented through
large models significantly boosts performance in few-shot learning tasks. This efficient and
practical data augmentation method reduces reliance on manual annotation. This data aug-
mentation method is efficient and practical, reducing reliance on manual annotations.
These strategies demonstrate how researchers utilize AIL methods to realize data in data
quality enhancement for machine learning, ensuring that models are not only trained on
high-quality data but also adaptable to complex real-world environments.
Similarly, to clarify how these diversity-oriented approaches align with Eq. 8, we present
them in Table 5.
3.1.3.4 Analysis of data quality enhancement in AIL-ML As discussed above, we have
introduced mathematical representations for two primary data quality enhancement meth-
odologies within the AIL-ML framework: Improving Data Accuracy and Consistency and
Enhancing Data Diversity. These methodologies correspond to the Eq. (8). By comparing
these methodologies across various aspects, we can gain a comprehensive understanding
1 3

266  Page 22 of 55 J. Gao et al.

Table 5 Symbol description  Method Agent ac- Key param- Data  Output
for methods emphasizing data  tions (At) eters (Q) quality en- (Dt+1)
diversity hancement
function (θ)
| HIL error  Annotating    | Feature  Refining        | A dataset with   |
| ------------------------ | ------------------------ | ---------------- |
| detection  and verify-   | contribution  data by    | identified       |
| (Liu et al.  ing global  | thresholds,  combin-     | error features   |
| 2021) error              | annotation  ing feature  | addressed,       |
| features                 | rules, error  contri-    | yielding better  |
|                          | detection  bution        | generalization   |
|                          | criteria analysis        | and robustness   |
with human
evaluation
| Step- Generating     | Prompt  Incor-  | A refined     |
| -------------------- | --------------- | ------------- |
| by-step  detailed    | design porates  | dataset with  |
| distilla- reasoning  | reasoning       | enriched      |
| tion (Hsieh  steps   | and expla-      | contextual    |
et al.  nations into
2023a) the original
data
| AIL  Crafting          | human  Generating          | A dataset       |
| ---------------------- | -------------------------- | --------------- |
| adversar- adversarial  | interaction  adver-        | enriched with   |
| ial exam- questions    | protocols,  sarial data    | diverse and     |
| ples (Wal- or inputs   | adversarial  to diversify  | complex         |
| lace et  that inten-   | crafting  training         | adversarial     |
| al. 2019;  tionally    | strategies data            | examples, im-   |
| Bartolo et  confuse    |                            | proving model   |
| al. 2020) models       |                            | robustness and  |
generalization
| Gesture  Provid-     | Zoom fac- Applying      | A gesture da-   |
| -------------------- | ----------------------- | --------------- |
| augmenta- ing a few  | tors, scaling  various  | taset covering  |
| tion (Xu et  custom  | intensity,  transfor-   | diverse speeds  |
| al. 2022) gestures   | time-warp  mations      | and strengths   |
from users,  parameters (zoom,
which  scale,
are then  warp) to
augmented user-
defined
gestures
| Augpt (Dai  Utiliz-     | RLHF  Using large       | A diversified  |
| ----------------------- | ----------------------- | -------------- |
| et al. 2023) ing large  | fine-tuning  models to  | text corpus    |
| models to               | configs,  generate      | with semanti-  |
| rephrase                | sampling  multiple      | cally varied   |
| or expand               | settings concep-        | samples        |
textual  tually
samples similar but
semantical-
ly different
variations
of each
sentence
of their distinct roles, advantages, and limitations in enhancing data quality for machine
learning models.
Improving Data Accuracy and Consistency focuses on enhancing the precision and reli-
ability of the existing dataset by addressing errors, noise, and inconsistencies. This approach
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 23 of 55 266
ensures that the data used for model training is accurate, thereby directly contributing to
improved model performance. These methods can be detailed as follows:
● Correcting Mislabelled Samples: Utilizing agnet to rectify labeling errors.
● Label Refinement: Incorporating human rationales to enhance label quality.
● Consistency Checks: Implementing quality control mechanisms to ensure data consist-
ency.
These methods rely on quality control parameters, such as label accuracy thresholds, agent
reliability metrics, and detailed annotation guidelines, to maintain high standards of data
quality. Consequently, the enhanced dataset D t+1 is characterized by higher accuracy,
reduced noise, and greater consistency, which will enhance the model’s precision and
reliability.
Enhancing Data Diversity aims to increase the variability and richness of the dataset to
improve the model’s ability to generalize across diverse scenarios. This methodology intro-
duces new data samples or transforms existing ones to create a more varied dataset, thereby
making the model more robust and adaptable. The specific strategies implemented include:
● Data Augmentation: Applying techniques such as scaling, time-warping, or zooming to
generate additional samples from existing data.
● Adversarial Example Generation: Creating challenging inputs designed to test and en-
hance model robustness.
● Synthetic Data Generation: Utilizing agent to produce diverse and contextually rich
training data.
These methods depend on specific augmentation parameters, perturbation strategies, and
prompt designs to ensure that the generated data effectively increases diversity while main-
taining quality. As a result, the enhanced dataset D t+1 becomes more comprehensive and
varied, thereby improving the model’s generalization capabilities and performance in real-
world applications.
Although improving data accuracy and enhancing data diversity have their own empha-
ses in the framework of AIL-ML, they complement each other and jointly improve data
quality and model performance. The analysis them reveals several key insights:
● Complementary Objectives: Improving data accuracy ensures the reliability of the data-
set by minimizing errors and inconsistencies, which is essential for tasks requiring high
precision. In contrast, enhancing data diversity broadens the dataset’s scope, enabling
models to generalize better across varied and unseen scenarios.
● Different Agent Actions: Methods aimed at improving accuracy typically involve cor-
rective actions such as correcting mislabeled data, label refinement and removing incon-
sistencies. On the other hand, diversity enhancement methods focus on generating new
samples, manipulating features, creating adversarial examples or transforming existing
data through techniques such as data augmentation.
● Combining both methodologies leads to a dataset that is not only accurate and consist-
ent but also rich in diversity. High-accuracy data provides a reliable foundation, while
diverse data ensures that the model can handle a wide range of inputs, enhancing overall
1 3

266 Page 24 of 55 J. Gao et al.
performance and adaptability.
3.1.4 Data annotation
In the realms of deep learning and machine learning, data annotation is fundamentally
crucial due to the dependency of model learning capabilities on extensive, high-quality,
annotated datasets. In this section, we introduce AIL-ML methods specifically aimed at
enhancing the efficiency and accuracy of data annotation.
Initially, we present an overview of the current practices of agent-based annotation within
the AIL framework, outlining how agents contribute to the data labeling process. Then, we
explore various methodologies focused on reducing annotation costs and increasing the
efficiency of the annotation process. The integration of these strategies ensures that the data
annotation is not only cost-effective but also enhances the scalability and applicability of
machine learning models in different applications.
3.1.4.1 Mathematical framework for data annotation The agent-assisted data annotation
process within the AIL-ML framework can be modeled as an optimization problem, formu-
lated by the following equation:
L t =γ(D t′,A t ,Σ t ,Ω t ) (9)
where:
● L t represents the outputs at time t, which may include labels, confidence levels, and
explanations based on the output options Ω t.
● D t′ denotes the subset of samples selected from the original dataset D t for annotation.
● A t is the inputs from the agent.
● Σ t is a set of annotation strategies, such as fixed-choice, range selection, or open input,
and how these strategies are implemented to reduce costs and increase efficiency.
● Ω t defines the output options, specifying which additional information should be gener-
ated.
● γ is the comprehensive annotation function responsible for generating the desired an-
notated data based on the selected samples S t, agent inputs A t, the annotation strategies
Σ t and the output options Ω t.
This formulation ensures that the data annotation process is not only cost-effective but
also scalable and applicable to various machine learning models in different applications.
By incorporating intelligent agent strategies, AIL-ML systems can enhance efficiency and
reduce costs associated with data annotation.
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 25 of 55 266
3.1.4.2 Annotation methods categorized by degree of freedom As illustrated in Fig. 4, the
common methods used for annotation can be classified into three types based on the degree
of freedom each method provides: fixed-choice, range selection, and open input.
● The fixed-choice method, which offers the least freedom, requires agents to select from
at least two predefined options. This is the most commonly used and universally ap-
plicable annotation method, offering minimal cognitive burden to agents but lacking
flexibility compared to other methods (Wu et al. 2020).
● Range selection, offering more freedom than fixed-choice, includes choosing within
discrete or continuous sequences. Discrete sequences consist of clearly distinguishable
units, such as text, while continuous sequences, like image pixels or signal durations,
lack clear units (Cai et al. 2019; Xu et al. 2022). In these instances, individual data
points may not contain complete meaning on their own (e.g., pixels). For some unstruc-
tured data, researchers utilize dimension reduction to visualize the data on a graphical
interface, allowing agents to select ranges by drawing boundary boxes on spectrograms
to manually annotate events (Kath et al. 2023).
● The open input method provides the highest degree of freedom, where agents can input
self-defined text. This method enables the generation of rich, diverse annotations, such
as dialogues (Hancock et al. 2019) or rules (Zhang et al. 2019). Open input annota-
tions are particularly beneficial for tasks requiring complex data interpretation, allowing
agents to offer detailed information that enhances model training and performance.
3.1.4.3 Strategies for reducing annotation costs The reduction of annotation costs within
the AIL-ML framework is a prominent research focus. Annotation for certain tasks can be
Fig. 4 Classification of annotation methods based on the degree of freedom. The fixed-choice method
provides minimal freedom with predefined options for selection. Range selection allows choosing within
discrete or continuous sequences, offering more flexibility. The open input method provides the highest
degree of freedom, allowing free text input
1 3

266 Page 26 of 55 J. Gao et al.
costly, demanding considerable time, energy, and expertise from annotators. As described in
Fig. 5, the AIL-ML framework utilizes three kinds of strategies to reduce annotation costs:
1. Data: selecting the most valuable samples for annotation to reduce the number of items
needing labels.
2. Process Optimization: optimizing the annotation process to enhance efficiency.
3. Agent: deploying hierarchical levels of agents to carry out these tasks, thereby dimin-
ishing the overall annotation costs.
3.1.4.4 Data: selecting the most valuable samples In the context of enhancing efficiency
in machine learning, selecting the most valuable samples for agents to annotate can sig-
nificantly reduce the number of data points that need to be labeled. One effective approach
is the cluster-then-label method, which reduces the volume of data needing annotation by
selecting representative samples for labeling, as discussed in the works of Wu et al. (2020)
and Hiremath et al. (2022) This approach uses unsupervised clustering to identify key data
points that are then annotated, thus diminishing the overall volume of data requiring manual
labels. In scenarios where the system can accurately recognize certain activities, it may initi-
ate a one-shot interaction for annotating such behaviors, thereby creating a labeled dataset.
Data points with low confidence or high uncertainty in current ML models are deemed
highly informative and prioritized for annotation. In parallel, Qian et al. introduced the
PARTNER system (Qian et al. 2020), which predicts labels for all unannotated entities
using the current model and ranks them based on uncertainty, focusing annotation efforts
on the most uncertain instances. Following annotation, similar instances are identified and
assigned pseudo-labels based on the annotated data, thereby augmenting the training dataset
efficiently. This strategy effectively combines user involvement with model training, mini-
mizing the need for extensive manual annotations. Furthermore, boundary samples present
classification challenges due to the inherent features of multiple categories. To address this,
Sahu et al. (2023) introduced a method where large models re-annotate boundary samples to
ensure accurate classification, thus enhancing both the accuracy and generalization capabil-
ity of the training models.
All the methods discussed above can be integrated into our proposed Eq. 9. Table 6 illus-
trates how each approach aligns with specific elements of our framework.
Fig. 5 Three primary strategies for reduce annotation costs within the AIL=ML framework. The strategies
include: selecting the most valuable data samples, optimizing data interaction processes and leveraging
diverse agents
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 27 of 55  266
Table 6 Symbol description for methods selecting the most valuable samples
| Method | Lt γ | D t′ | At Σt | Ωt  |
| ------ | ---- | ---- | ----- | --- |
Cluster- Labels for  A cluster- Cluster centroids  Human  Fixed-choice Labels
| then-         | selected  ing step and  | as representatives | labeling |     |
| ------------- | ----------------------- | ------------------ | -------- | --- |
| label (Wu     | clusters a manual       |                    |          |     |
| et al. 2020;  | labeling step           |                    |          |     |
Hiremath et
al. 2022)
PART- Labels, par- Model pre- High-uncertainty  Human  Fixed-choice Label
NER (Qian  tial pseudo- diction, user  instances for user  labeling and con-
et al. 2020) labels and  correction  labeling; others  fidence
|     | confidence  and labeling | pseudo-labeled |     | for     |
| --- | ------------------------ | -------------- | --- | ------- |
|     | scores                   |                |     | pseudo- |
labeled
data
Prompt- Enhanced  Boundary  Gener- Data gen- Fixed-choice Labels
Mix (Sahu  labels for  data gen- ated boundary  eration and  with
et al. 2023) classifica- eration and  samples via LLM re-labeling explana-
|     | tion tasks LLM-based  |     |     | tions |
| --- | --------------------- | --- | --- | ----- |
re-labeling
Table 7 Symbol description for methods optimizing the annotation process
γ
| Method | Lt  | D t′ | At Σt | Ωt  |
| ------ | --- | ---- | ----- | --- |
HIL entity  Labels  Recommenda- Samples selected  Human  Fixed-choice Labels
linking (Klie  for entity  tion algorithm  by recommenda- labeling with
| et al. 2020) | linking  and adaptive  | tion system |     | recom-  |
| ------------ | ---------------------- | ----------- | --- | ------- |
|              | tasks candidate        |             |     | mended  |
|              | ranking                |             |     | scores  |
LSUN (Yu et  Class  Iterative anno- Selected via k- Human  Fixed-choice Labels
| al. 2015) | labels tation pipeline | means clustering  | labeling |     |
| --------- | ---------------------- | ----------------- | -------- | --- |
and classifier
confidence
3.1.4.5 Process optimization: optimizing the annotation process Optimizing the annota-
tion process to reduce workload and cost while enhancing efficiency is also a key focus in
current research. Klie et al. (2020) have effectively utilized recommendation algorithms to
propose potential concepts and adaptively prioritize candidates. Their approach has been
proven to increase the speed of annotation by 35%, with users expressing a strong prefer-
ence for this system. Similarly, in the LSUN project led by Yu et al. (2015), the develop-
ment of an efficient graphical user interface significantly lightens the annotation load and
enhances productivity. This interface focuses the annotator on a single image at a time,
providing thumbnails of previous and next images to ease understanding and reduce naviga-
tion time. Enhancements such as full-screen image display improve the visibility of visual
details, leading to more accurate annotations. Moreover, the introduction of simplified key-
board shortcuts, like using the space bar for classification, greatly enhances the efficiency of
operations. These interface innovations not only boost the efficiency of data annotation but
also substantially lower the costs involved, providing robust support for building extensive
image datasets.
Table 7 summarizes how each referenced work maps on Eq. 9.
1 3

266 Page 28 of 55 J. Gao et al.
3.1.4.6 Agent: deploying hierarchical levels of agents In the context of AIL-ML, agents
can be categorized into three distinct types: LLMs, general users, and domain experts. As
shown in Fig. 6, general users hold general knowledge, which is broad and encompasses a
wide array of basic facts across various domains. LLMs, on the other hand, are trained on
trillions of data points from extensive databases, encompassing not only general knowledge
but also a significant amount of database-specific information. Domain experts stand out by
their possession of both general knowledge and highly specialized expert knowledge, spe-
cific to their particular field of study. It is important to note that the knowledge capacity of
LLMs is limited by the nature of their training data, which is generated by humans and may
not cover the depth of expertise that domain experts achieve through specialized education
and experience. Thus, the knowledge ceiling of LLMs is typically considered to be below
that of domain experts.
Upon training with datasets consisting of trillions of data points, LLMs have developed
capabilities that include reasoning, semantic understanding, grounding, and planning. These
capabilities suggest that LLMs could serve effectively as proxies for humans in AIL con-
texts, potentially reducing the substantial costs associated with manual labor (Hsieh et al.
2023a; He et al. 2023b). Researchers like Wang et al. (2021) have explored the use of GPT-3
as a cost-effective tool for data annotation. By generating pseudo-labels through GPT-3,
this approach offers a more economical and faster alternative to traditional manual labeling
methods. Compared to manual annotation, the use of GPT-3 can reduce costs by 50% to
96%, owing to its ability to generate labels more swiftly and at a lower cost.
Various studies have explored strategies for distributing annotation tasks among different
agent types, employing a multi-level agent architecture to lower annotation costs effectively
(Wang et al. 2023b; He et al. 2023a). LLMs show considerable efficacy in handling tasks
with limited label spaces, significantly reducing manual annotation costs and reaching qual-
ity levels akin to human annotations under specific conditions. However, their performance
is less robust in scenarios with extensive labeling requirements and complex relationships
(Ding et al. 2022). To optimize both cost and quality, integrating LLMs with human annota-
tors proves beneficial, particularly for critical tasks. Shuohang Wang and his team (Wang
et al. 2021) have leveraged GPT-3 to generate pseudo-labels and their corresponding con-
Fig. 6 Three types of agents in the AIL-ML framework: general users, LLMs, and domain experts. Gen-
eral users hold general knowledge across various domains. LLMs are enhanced by training on extensive
databases, holding both general and substantial database-specific knowledge. Domain experts, combine
general knowledge and expert knowledge, establishing them at the highest level of knowledge within
their specific fields
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 29 of 55 266
fidence scores, allowing for selective human re-annotation of labels that demonstrate low
confidence. This strategy significantly decreases the dependency on human resources with-
out compromising the quality of annotations, which is particularly critical when working
within limited budgets on large-scale datasets. While LLMs offer efficiency and cost savings
in generating annotations, their performance on complex or domain-specific tasks is typi-
cally flawed and may introduce biases relative to human annotations. To address these chal-
lenges, Wang et al. (2024) have introduced a collaborative method that utilizes the strengths
of LLMs and human annotators to enhance annotation accuracy and reliability at low costs.
This approach involves LLMs producing initial labels and explanations, followed by a vali-
dation model that evaluates these labels, with human annotators subsequently focusing on
the instances scored lowest by the validation model. The LLM-generated explanations pro-
vide additional context that aids human annotators in refining and improving the labels,
thus cost-effectively ensuring high-quality annotations. Annotating multimodal data, such
as text and images from social media, is often chanllenged by its complexity and noise. To
address these issues, Feihong Lu et al. proposed the Miko framework (Lu et al. 2024). This
framework leverages the collaboration of multimodal large language models (MLLMs),
LLMs, and humans to achieve high-quality annotations. The process starts with MLLMs
generating detailed image descriptions to refine and validate textual content, thereby reduc-
ing noise and enhancing multimodal data representation. Subsequently, LLMs extract and
classify users’ potential intentions based on key dimensions such as concepts, actions, and
emotions. Finally, human reviewers verify the generated intentions, ensuring their quality
and relevance through systematic scoring. By combining the strengths of machine intelli-
gence and human judgment, Miko not only improves annotation efficiency but also enriches
models’ understanding of user intentions, offering robust support for downstream tasks like
recommendation systems and sentiment analysis.
In recent studies, expert agents have been utilized to create rules that significantly
decrease the amount of data that needs to be annotated, thereby reducing costs associated
with data labeling (Li 2017; Zhang et al. 2019). Zhang et al. (2019) developed a method
where human experts use regular expressions to establish initial rules, generating weakly
labeled data. While this data might contain noise, it serves as a valuable asset for the early
stages of model training, particularly effective when labeled data are scarce. This approach
accelerates the annotation process, improving the quality of ML models. However, when
there is an abundance of labeled data, deep neural networks excel at uncovering more intri-
cate dependencies in the data. Data derived from regular expressions typically show lim-
ited diversity and are strongly rule-oriented, making them suitable primarily in the early
stages of model training where labels are deficient. Hemmer et al. (2022) have explored a
coordinated approach between classifier systems and expert agents. In their system, clas-
sifiers are trained to pinpoint cases that are difficult for human experts to handle, while
an assignment system efficiently allocates each case to the most suitable agent, whether
human or machine. This approach has been evaluated in several studies, including experi-
ments with"synthetic"experts and a real medical dataset annotated by multiple radiologists.
Research indicates that this method outperforms previous approaches and provides more
accurate results than either the best human experts or classifiers alone.
All these methods can be incorporated into our proposed Eq. 9. Table 8 provides an over-
view of how each method corresponds to different elements of our framework.
1 3

266 Page 30 of 55 J. Gao et al.
Table 8 Symbol description for methods deploying hierarchical levels of agents
Method Lt γ D t′ At Σt Ωt
GPT3 for La- LLM labels Labeling pipe- Low- GPT-3 pre- Active Labels
beling (Wang and human line with GPT-3 confidence dictions (la- labeling and con-
et al. 2021) corrections inference and subset bels, logits) fidences
human review and human
corrections
Human-LLM Labels and LLM LLM labeling Low-verifi- LLM outputs Collabora- Labels,
Annota- explanations and human cation-score (labels, ex- tive label- explana-
tion (Wang et re-labeling data planations) ing strategy tions
al. 2024) and human and veri-
corrections fication
scores
HITL En- Entity labels Regex-generated Uncertainty Experts Collabora- Labels
tity Extrac- weak labels data designing tive label- with
tion (Zhang et and annotation regex rules ing strategy confi-
al. 2019) on uncertain and general dence
samples user labeling scores
on uncertain
samples
Human-AI Collaborative Joint training Dynamic Multiple Collabora- Labels
Teams (Hem- labels pipeline for samples human ex- tive label-
mer et al. optimal team perts and AI ing strategy
2022) performance models
Miko (Lu et Image descrip- Multi-stage an- Clean, MLLM Multi-step Labels,
al. 2024) tions, key notation process complete, for image annotation explana-
information and and multi- descriptions, strategy tions,
user intentions modal data LLM for key and
(text + information intent
images) extraction classifi-
and intent cations
generation
and two-
stage human
validation
3.1.4.7 Analysis of data annotation in AIL-ML In this section, we introduce three data
annotation methods categorized by degree of freedom:fixed-choice, range selection, and
open input. Fixed-choice accelerates labeling but may overlook details; range selection
enhances granularity at the expense of increased effort; and open input captures deeper
insights though it risks inconsistency or noise. For other researchers, an effective choice
depends on matching the method’s flexibility to the complexity of the data and the goals of
the annotation task, suggesting that assessing trade-offs between expressivity and cognitive
burden is essential.
Selecting the Most Valuable Sample strategies aimed at minimizing redundant labeling.
By identifying the most informative or representative items-for instance, via cluster-then-
label methods or uncertainty-based sampling-researchers can focus human resources where
they are most needed, reducing overall annotation volume without compromising model
performance. This selective approach ensures that each labeled instance contribute to train-
ing while preventing time-consuming manual labeling of uninformative samples.
Optimizing the Annotation Process emphasizes reveals that annotation efficiency is not
only about data but also the manner in which data is presented and processed. Innova-
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 31 of 55 266
tions like dynamic recommendation algorithms, adaptive interfaces, and simplifying agent’s
workflows can yield substantial gains in speed and consistency. However, implementing
these optimizations often requires iterative user testing and interface refinement. This high-
lights the importance of balancing technical algorithms and agent factors.
Deploying Hierarchical Levels of Agents can utilize the advantage of different agent
types. LMs provide rapid, cost-effective pseudo-labeling but may introduce biases or errors
if left unchecked, while domain experts can resolve intricate cases at a higher per-annotation
cost. General users fill in the middle ground, handling moderately challenging tasks. This
layered design encourages thoughtful distribution of effort and expertise but also requires
continual calibration-researchers must ensure that each agent level is invoked where it adds
value rather than extraneous complexity.
Effective data annotation relies on combining data selection, data sampling, workflow
optimization, and appropriate agent collaboration. Each component must work together,
such as aligning data selection with interface design or involving experts to handle chal-
lenging edge cases. By integrating these elements, researchers can reduce labeling effort and
ensure high-quality annotations, ultimately supporting the development of reliable machine
learning models.
3.2 Model development and optimization
For machine learning, the development and optimization of models are also important. The
methodologies adopted during the model development phase significantly impact the effec-
tiveness and efficiency. Moreover, continual refinement and optimization are essential for
the enhancement of model performance. In this section, we investigate AIL-ML techniques
that concentrate on model development and optimization. This includes a comprehensive
analysis of methods in the areas of Model Cold Start Issue, Model Training, and Model
Iterative Enhancement.
3.2.1 Model cold start issues
In machine learning, the model cold start problem refers to the challenge of initializing a
model effectively when minimal or no historical data is available. This issue is particularly
prevalent for machine learning that is data-driven. The lack of initial training data can sig-
nificantly lower model performance. In this section, we will explore various AIL-ML meth-
ods that address the model cold start problem, aiming to improve the effectiveness when
models begin the learning process.
3.2.1.1 Mathematical framework for model cold start issues Given the initial state
M and minimal or no historical data at time t=0, how to utilize AIL-ML framework to
0
address model cold start issue can be defined as:
M 1 =χ(M 0 ,σ(A 0 ,P gen ),P cold ) (10)
where:
1 3

266 Page 32 of 55 J. Gao et al.
● M 0 is the model’s initial state which is usually untrained or only configured.
● σ(A 0 ,P gen ) represents the data generation function, influenced by agent’s input A 0 and
data generation parameters P .
gen
● P cold are the parameters specifically designed for rapid adaptation during the cold start
phase.
● χ is the cold start learning function, which is responsible for integrating the data gener-
ated by the agent with the learning parameters, and quickly updating the state from M
0
to M .
1
After reviewing the relevant literature within the AIL-ML domain, we have identified two
primary approaches to solve the cold start problem: 1) employing agents to generate an ini-
tial dataset, and 2) utilizing transfer learning and domain generalization techniques. The first
approach involves using agents to generate the data that can serve as a preliminary train-
ing set. This leverages the agents’ capabilities to simulate realistic data scenarios that help
bootstrap the model’s learning process. The second approach involves applying knowledge
gained from one or more source domains to a target domain where data are scarce. This
method not only addresses the scarcity of data in new applications but also enhances the
model’s ability to generalize across different domains, thus providing a robust foundation
for model training even in the absence of extensive domain-specific data.
3.2.1.2 Employing agents to generate an initial dataset During the model cold start phase,
a high-quality initial dataset is necessary for model training. Agents can provide or generate
initial dataset, thus addressing the cold start problem. Large models can generate the data
needed for initial training, enabling smaller task-specific models to begin training without
data. Therefore, large models can resolve the cold start issue by supplying or creating initial
training data (Ye et al. 2022). Wang et al. (2021) demonstrated how large models can be
used to generate annotated data, rapidly assembling an initial dataset to overcome the cold
start problem. Especially in low-resource settings, the label data produced by large mod-
els provide sufficient information. Large models can shorten the time of acquiring initial
annotated data through few-shot learning. Additionally, the cost of using large models for
data annotation is significantly lower than that of human annotation, which helps to quickly
acquire large-scale high-quality annotated data with limited budgets. These high-quality
initial annotations can accelerate the early training process, enabling the model to quickly
initiate from a cold start. Besides generating data labels, large models can also produce
inferences (Hsieh et al. 2023a). By leveraging inferences and labels generated by large
models, smaller models can gain rich contextual information and task knowledge from the
start of training. This effectively addresses the cold start problem, allowing small models to
quickly achieve better performance with limited training data. Large models significantly
reduce the time and financial costs associated with acquiring high-quality datasets, provid-
ing a more feasible option for individuals or small organizations to utilize advanced AI
capabilities (Ding et al. 2022).
We demonstrate in Table 9 how each referenced study corresponds to the symbols and
in Eq. 10.
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 33 of 55  266

| Table 9 Symbol description for  | Method χ | σ(A0,Pgen) | Pcold |
| ------------------------------- | -------- | ---------- | ----- |
methods employing agents to
|     | GPT-3 for  Using LM to  | Generating dataset by  | Few-shot  |
| --- | ----------------------- | ---------------------- | --------- |
generate an initial dataset
|     | label- generate init            | LM in low-resource      | prompting     |
| --- | ------------------------------- | ----------------------- | ------------- |
|     | ing (Wang  dataset              | scenes, providing init  | strategies    |
|     | et al. 2021)                    | training dataset        |               |
|     | Distilling  Integrating         | Generating rationales   | Multi-task    |
|     | Step-by- LM’s rationales        | from the LM, expand-    | distillation  |
|     | step (Hsieh  to train the       | ing dataset with step-  | parameters    |
|     | et al. 2023a) smaller model     | by-step explanations    |               |
|     | GPT-3 for  Integrating          | Data generation meth-   | Prompt        |
|     | annota- GPT-3-generat-          | ods (PGDA, PGDG,        | configura-    |
|     | tion (Ding  ed dataset into     | DADG) producing         | tions and     |
|     | et al. 2022) the training loop  | dataset for cold-start  | knowledge-    |
|     | to bootstrap the                | training                | base usage    |
model parameters
to enhance
data quality
3.2.1.3 Utilizing  transfer  learning  and  domain  generalization  techniques The  second
approach to resolve the model cold start issue involves leveraging transfer learning, where
knowledge from one or more well-resourced source domains is applied to a target domain
that lacks sufficient data. This method not only addresses the scarcity of data in new appli-
cations but also enhances the model’s ability to generalize across different domains, thus
providing a robust foundation for model training even in the absence of extensive domain-
specific data. Similarly, experts can utilize domain generalization to adjust models based
on diverse tasks. This method involves learning from one or several related but different
domains, allowing the model to generalize well to an unseen domain. Theoretical insights
from Jindong Wang and Ben-David support this approach by indicating that invariant fea-
ture representations across domains ensure the generalizability and transferability of the
model (Wang et al. 2022; Ben-David et al. 2006). Consequently, experts may utilize the
pretraining-finetuning strategy within transfer learning to adapt the model to new settings
effectively (Zhuang et al. 2020).
3.2.1.4 Analysis of model cold start issues in AIL-ML Employing agents to generate an
initial dataset can effectively address the model cold start problem, particularly when work-
ing with limited or no labeled data. LLMs can rapidly produce training samples or annota-
tions, effectively training smaller models that would otherwise lack a representative dataset.
Although the dataset may contain biases or errors from LLM, this method greatly lowers
labeling effort and speeds up model deployment. Moreover, LM have the ability to create
large-scale data at low cost, which helps smaller organizations that cannot afford expensive
human annotation.
Meanwhile, utilizing transfer learning and domain generalization addresses cold starts
from a different angle, emphasizing the transfer of robust, pre-learned feature representa-
tions from well-resourced domains to domains with sparse data. By aligning model param-
eters and feature spaces across different tasks or domains, researchers can equip a newly
deployed model with strong priors that enable quick adaptation, even if domain-specific
1 3

266 Page 34 of 55 J. Gao et al.
data are scarce. Transfer learning provides a theoretical and empirical backbone for acceler-
ating cold starts, but its efficacy depends on the compatibility of source and target domains.
LLM-driven dataset creation directly addresses the absence of labeled data by quickly
supplying training examples, while transfer learning and domain generalization reuse exist-
ing knowledge to guide model parameter initialization. Researchers must balance these
approaches according to resource availability, domain similarity, and the potential overhead
of data cleaning or adaptation.
3.2.2 Model training
In machine learning, the model training process involves the adjustment of model param-
eters using optimization algorithms. This procedure involves the selection of the model’s
architecture, the loss function, and the optimizer to ensure effective learning. The model’s
architecture influences the model’s capacity to capture relevant patterns in the data. More-
over, the loss function ensures that the model’s predictions align closely with the actual
outcomes. Similarly, the choice of optimizer affects the efficiency and speed with which the
model converges to a solution. Agents can leverage their deep understanding of the prob-
lem, thereby offering essential insights to enhance model performance.
3.2.2.1 Mathematical framework for model training The model training process, integrat-
ing agent’s insights into it, can be defined as follows:
M t+1 =ϕ(M t ,D t ,A t ,Θ t ) (11)
where:
● M t and M t+1 represent the model states at time t and t+1, respectively.
● D t is the training dataset at time t.
● A t includes inputs from the agent, which may suggest modifications to the model archi-
tecture, loss function, or optimization strategy.
● Θ t encompasses the set of training parameters, which integrates training parameters
with the insights provided by the agent.
● ϕ is the model update function that not only applies conventional optimization algo-
rithms but also integrates the agent’s guidance to achieve more effective learning and
improved model performance.
Generally, AIL-ML framework integration in model training is in two ways: 1) agents use
knowledge to optimize model training or 2) agents can be designed as a component of the
machine learning network architecture.
3.2.2.2 Leveraging agent knowledge for optimized model learning Agents can leverage
their knowledge to guide the design and training of models, ensuring that these models
effectively capture the core patterns of the tasks. Agents can influence several aspects of
model development, including selecting the appropriate model framework, loss functions,
and optimization algorithms, as well as adjusting the training procedures such as the number
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 35 of 55  266
of training iterations or epochs (Kath et al. 2023; Tchemeube et al. 2023). Roels et al. (2019)
developed an AIL approach to address the explosion of data sets due to 3D technology in
electron microscopy)(EM). They created an interactive graphical user interface that allows
biologists to use the framework in an intuitive and user-friendly fashion. Experts directly
interact with the model through this graphical interface to evaluate the performance of vari-
ous models and choose the most suitable one. Additionally, experts can select regions of
interest and set parameters to optimize the model, ensuring the efficiency and reproduc-
ibility of the algorithms. A recent study by Metsch et al. (2024) provides a compelling dem-
onstration of integrating interactive graphical interfaces in the context of biomedical data.
They introduced the CLARUS platform, an explainable AI tool designed for graph neural
networks (GNNs) in the biomedical domain. CLARUS enables experts to manually modify
patient-specific protein-protein interaction networks and evaluate the impact of these modi-
fications on GNN predictions through counterfactual analysis. This interactive process not
only enhances the understanding of the model’s decision-making but also allows experts
to retrain the model based on their domain knowledge, improving its interpretability and
performance.
For ease of reference, Table 10 compiles the key elements of these approaches in relation
to Eq. 11.
3.2.2.3 Designing agents as architectural components in ML Agents can be designed as a
component of the machine learning network architecture. These agents continuously pro-
vide real-time feedback that adjusts the model’s behavior, thereby optimizing the training
outcomes. Some researchers incorporated agents directly into the network architecture. Such
designs allow the model to learn and adapt during training actively from agents, enhanc-
ing model’s ability to adjust internal feature representations based on agent inputs Wei et

| Table 10 Symbol description  | Method | ϕ Dt | At Θt |
| ---------------------------- | ------ | ---- | ----- |
for methods leveraging agent
|     | HITL in electron  | Executing  3D EM  | Expert  De- |
| --- | ----------------- | ----------------- | ----------- |
knowledge for optimized model
learning microscopy (Roels  the de- image and  interac- noising
|     | et al. 2019) | noising  expert-      | tions via  algo-       |
| --- | ------------ | --------------------- | ---------------------- |
|     |              | algorithm  specified  | the GUI,  rithm        |
|     |              | with  Regions of      | including  parame-     |
|     |              | specified  Interest   | algorithm  ters such   |
|     |              | parameters            | choice and  as filter  |
|     |              | based on              | parameter  size and    |
|     |              | expert                | adjustments iteration  |
input count
|     | CLARUS (Metsch  | Integrat- Synthetic    | Expert  GNN          |
| --- | --------------- | ---------------------- | -------------------- |
|     | et al. 2024)    | ing expert  graph da-  | modifica- hyper-     |
|     |                 | modifica- taset and    | tions to the  param- |
|     |                 | tions into  Patient-   | protein- eters       |
|     |                 | the GNN  specific      | protein              |
|     |                 | training  protein-     | interaction          |
|     |                 | process,  protein      | networks,            |
|     |                 | enabling  interaction  | such as              |
|     |                 | analy- (PPI)           | adding/              |
|     |                 | sis and  networks      | removing             |
|     |                 | retraining from gene   | interactions         |
expression based on
domain
knowledge
1 3

266 Page 36 of 55 J. Gao et al.
al. 2022 Some researchers embedded agents into the network architecture as core elements
by the interactive mechanisms and feedback loops (Oh et al. 2019; Weber et al. 2020). Oh
et al. (2019) presented a method for interactive video object segmentation where agents
annotate video frames (e.g., through scribbles). These annotations are utilized by an interac-
tive network to generate initial masks for foreground objects. The agent’s annotations not
only serve as input to the interactive network but also continuously influence the network’s
outputs through multiple rounds of interaction and feedback. Similarly, Wang et al. (2023a)
introduced H-Gen, an automatic H-DNN compression framework that incorporates human
input as a new hyperparameter for accurate and efficient DNN generation. When the model
exhibits low confidence in certain inputs during training, the agent is triggered to gener-
ate precise label data for these samples. The H-DNNs generated by H-Gen outperform the
original DNNs in terms of accuracy, latency, and energy consumption, significantly improv-
ing performance in resource-constrained environments. Large models can also be used as
a component of the network (Kwon and Michael 2023; Ye et al. 2023). Kwon and Michael
(2023) integrated LLMs into reinforcement learning frameworks as proxy reward functions.
They input natural language prompts into the LLM. Then LLM evaluates the behavior of
reinforcement learning (RL) agents based on the prompts and produces textual outputs as
reward signals. These reward signals are subsequently parsed into numerical reward signals,
which are utilized by the RL agents to update their strategies and undertake new training
iterations. Although designing effective prompts requires careful consideration, the contex-
tual learning capability of the LLM allows it to capture human-like behavioral priors from
minimal examples. This capability facilitates the efficient generation of reward signals that
are well-aligned with the user’s objectives, thus training RL agents more effectively.
To provide a consolidated view, Table 11 organizes each referenced work according to
the parameters in Eq. (11).
3.2.2.4 Analysis of model training in AIL-ML Leveraging Agent Knowledge for Opti-
mized Model Learning demonstrates how agents refinie model training. By offering expert-
driven adjustments to model architecture, loss functions, and optimization strategies, agents
ensure that models are tailored to capture the relevant patterns within complex datasets. This
approach allows for more effective training, particularly in specialized domains where auto-
mated methods alone may fall short. Integrating agent expertise can lead to more targeted
learning processes.
Designing Agents as Architectural Components in ML explores the integration of agents
directly into the machine learning pipeline. This approach enables real-time feedback and
adaptive learning, allowing agents to continuously influence the model’s behavior during
training. By embedding agents within the network architecture, models can dynamically
adjust their internal representations based on ongoing interactions and feedback.
The effective incorporation of agents into the model training process is many-sided,
requiring both the strategic utilization of agent expertise and the architectural embedding of
agents within the learning framework. Moreover, this comprehensive approach encourages
the development of models that can swiftly adapt to new challenges.
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 37 of 55  266

| Table 11 Symbol description  | Method ϕ | Dt  | At  | Θt  |
| ---------------------------- | -------- | --- | --- | --- |
for methods designing agents as
|     | User-guid- Processing  | Video frames  | Providing  | Param- |
| --- | ---------------------- | ------------- | ---------- | ------ |
architectural components in ML
|     | ed video  agent feed-    | for object   | annotations(e.g.  | eters of  |
| --- | ------------------------ | ------------ | ----------------- | --------- |
|     | segmenta- back to        | segmentation | scribbles) on     | interac-  |
|     | tion (Oh et  refine and  |              | video frames      | tive and  |
|     | al. 2019) propagate      |              | to guide model    | propa-    |
|     | masks with               |              | refine            | gation    |
multi- net-
round  works
training
|     | H- Integrating         | Image | Generating pre-  | Param- |
| --- | ---------------------- | ----- | ---------------- | ------ |
|     | Gen (Wang  agent into  |       | cise labels for  | eters  |
|     | et al.  the DNN        |       | low-confidence   | for    |
|     | 2023a) training        |       | samples          | H-DNN  |
process by  com-
knowledge  pres-
distillation sion
and
optimi-
zation
|     | Reward  Utilizing    | User prefer-   | Generating      | Param-   |
| --- | -------------------- | -------------- | --------------- | -------- |
|     | design  the LM’s     | ence text data | reward signals  | eters    |
|     | with  output as      |                | for RL model    | of RL    |
|     | LM (Kwon  reward to  |                | training        | model    |
|     | and  update the      |                |                 | and the  |
|     | Michael  RL model    |                |                 | integra- |
|     | 2023)                |                |                 | tion of  |
agent
3.2.3  Model iterative refinement
The development of machine learning models is an iterative process that depends on con-
tinuous assessment and refinement. In real-world long-term machine learning systems, data
changes over time. This is an important feature to consider, especially in systems that last
for months or even years (Chen et al. 2021a). Therefore, when deployed for a long time,
models frequent retraining and adjustments to maintain accuracy and relevance. Further-
more, the process of evaluating discrepancies between model predictions and actual out-
comes generates crucial feedback, which is fundamental to the iterative enhancement of
models. AIL-ML offers robust solutions to address these challenges. In this section, we will
explore various AIL-ML methods that specifically focus on model iterative enhancement.
AIL-ML methods facilitate the continuous integration of feedback into the learning cycle,
enabling models to adapt proactively to changes in data patterns and environmental condi-
tions. This not only helps in fine-tuning the models based on real-time data but also enhances
their ability to generalize across varying contexts and over time. By embedding agents that
can assess, adjust, and refine model parameters continuously, AIL-ML systems ensure that
machine learning models remain effective and responsive to the evolving nature of real-
world data, thereby sustaining their performance and relevance in long-term deployments.
1 3

266 Page 38 of 55 J. Gao et al.
3.2.3.1 Mathematical framework for model iterative refinement The iterative enhancement
of the machine learning model under the AIL-ML framework can be mathematically repre-
sented by the following formula:
M t+1 =ψ(M t ,D t ,A t ,Λ t ) (12)
where:
● M t and M t+1 represent the model at time t and t+1.
● D t is the dataset at time t, which may evolve over time reflecting changes in data pat-
terns.
● A t denotes the feedback obtained from agent, evaluating the discrepancies between
model predictions and actual outcomes.
● Λ t encompass es a set of parameters guiding the model update process.
● ψ is the model update function that integrates both traditional data-driven updates and
agent-based insights to adaptively refine the model in response to changing conditions.
3.2.3.2 Model iterative refinement based on human feedback Incorporating human feed-
back into model iterations significantly enhances alignment with human intentions, particu-
larly within the field of NLP (Ahn et al. 2023). The use of AIL frameworks is essential in this
context, as they enable models to navigate complex linguistic structures, cultural subtleties,
and linguistic variations. Without the involvement of human expertise, machine process-
ing tends to be simple and rigid. Retzlaff et al. (2024) further emphasize that reinforce-
ment learning, inherently a Human-in-the-Loop paradigm, greatly benefits from iterative
processes integrating human preferences. This perspective aligns with the core principles
of AIL frameworks, underscoring the pivotal role of human feedback in refining models
and adapting to dynamic environments. For instance, in dialogue tasks, human involve-
ment is crucial to define conversational goals and maintain alignment with expected behav-
iors, especially in dynamic, user-driven contexts. Recent advancements demonstrate that
integrating human preference feedback through reinforcement learning effectively refines
models via iterative enhancements (Ziegler et al. 2019; Stiennon et al. 2020; Ouyang et al.
2022; Crochepierre et al. 2022; Fan et al. 2024). This method typically begins with develop-
ing a reward function trained on human feedback to capture task-specific priorities. Itera-
tive fine-tuning then adjusts policies to better reflect these priorities. Retzlaff et al. (2024)
highlight the critical role of explainability and trust-building mechanisms in such iterative
processes, as they enable productive human-agent interaction and ensure models remain
adaptable to evolving user needs. For example, Ying Fan et al. proposed using online rein-
forcement learning to fine-tune text-to-image models. In this setup, the model continually
generates new samples and adjusts its generation strategies based on human feedback (Fan
et al. 2024). This online and iterative enhancement process heavily relies on the continuous
input of human feedback, enabling gradual improvements with each iteration. The model
enhances the quality and alignment of the generated images to better reflect human inten-
tions. Direct quality assessments provided by humans train the reward function, thereby
increasing both the accuracy and consistency of the model. This feedback assists in handling
complex generation tasks, such as creating scenes with multiple objects or specific attri-
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 39 of 55 266
butes like color, quantity, and placement, ensuring that the images accurately reflect the text
descriptions. Human feedback also significantly extends the model’s generalization capabil-
ity, as it incorporates a broad spectrum of scenarios and descriptions, thus improving the
model’s adaptability to various applications. Further, human inputs allow for ongoing opti-
mization, helping the model avoid local optima and adapt to new user demands in real-time,
reducing training data biases and enhancing the fairness and quality of the outputs. Follow-
ing a similar methodology, Daniel M. Ziegler et al. have refined language processing tasks
with a reward model derived from human preferences, overcoming the constraints imposed
by fixed evaluation metrics such as BLEU or ROUGE (Ziegler et al. 2019). This strategy
better aligns the model with genuine human linguistic practices and perceptions, thereby
enhancing the model’s learning signals and exploratory directions, significantly boosting
the efficiency of model iterations and the quality of outputs (Crochepierre et al. 2022).
Models can enhance their performance through active learning and interactive refine-
ment, leveraging human knowledge to identify and correct their gaps, uncertainties, or
errors (Wu et al. 2020; Hancock et al. 2019; Qian et al. 2020). Arakawa et al. (2023) pro-
posed PrISM-Tracker, a multimodal procedure tracking framework that employs wearable
sensors and state transition data for user-driven error and uncertainty resolution. This frame-
work actively queries users to address uncertainties encountered during tracking, showcas-
ing a method that combines active learning with time series analysis to enhance accuracy.
User input allows the model to continually correct errors and optimize performance during
practical usage, consistently obtaining high-quality annotated data. By dynamically updat-
ing the model, it adapts more effectively to user habits and environmental changes, reducing
long-term uncertainties and enhancing the robustness and predictive accuracy of the system.
Similarly in the paper (Yao et al. 2019b), the authors improve the performance of semantic
parsing by incorporating user feedback, thus enabling iterative model enhancement. In each
iteration, the model generates preliminary SQL queries and assesses uncertainties through
an error detector, subsequently generating clarifying questions for the user. User feedback is
then used to confirm or correct the model’s predictions, with the model updating its current
state based on this feedback and re-predicting uncertain segments. After multiple iterations,
the model progressively adapts to the patterns of user feedback, minimizing unnecessary
queries and improving parsing accuracy.
We summarize in Table 12 how the methodologies cited correspond to the variables
defined in Eq. (12).
3.2.3.3 Model iterative refinement based on large model feedback Despite the success
achieved by model iteration enhancements through human feedback, reliance on human
supervision introduces challenges such as the high cost of manual oversight and issues related
to quality, reliability, diversity, consistency, and potential biases. In response, researchers
have turned to using feedback from LLMs to enhance models for more complex tasks (He
et al. 2023a). Canwen Xu et al. have developed a method known as Self-Distillation with
Feedback (SDF), which utilizes feedback from LLMs for iterative enhancement and fine-
tuning of models (Xu et al. 2023). In this approach, a trained question-answering model
generates four distinct responses for each input prompt. These responses are then evaluated
by ChatGPT based on usefulness, relevance, accuracy, and detail, with the highest-scoring
response selected for further model fine-tuning. Fine-tuning employs newly introduced low-
1 3

| 266  Page 40 of 55 |     |     |     | J. Gao et al. |
| ------------------ | --- | --- | --- | ------------- |

| Table 12 Symbol description for  | Method | ψ   | Dt At | Λt  |
| -------------------------------- | ------ | --- | ----- | --- |
model iterative refinement based
|     | Reinforcement  | RL-based  | Text  Providing  | RL  |
| --- | -------------- | --------- | ---------------- | --- |
on human feedback
|     | learning via     | iterative up- | data;  preference       | hyper- |
| --- | ---------------- | ------------- | ----------------------- | ------ |
|     | human feed-      | date, guided  | image- feedback to      | param- |
|     | back (Ziegler    | by human      | to-text  the output of  | eters  |
|     | et al. 2019;     | preference    | data the model          |        |
|     | Stiennon et al.  | feedback      |                         |        |
2020; Ouyang
et al. 2022;
Crochepierre et
al. 2022; Fan et
al. 2024)
|     | PrISM-track-    | Refining       | Multi- Correcting       | Param-  |
| --- | --------------- | -------------- | ----------------------- | ------- |
|     | er (Arakawa et  | model output   | modal  the model’s      | eters   |
|     | al. 2023)       | based on user  | data from  predictions  | for     |
|     |                 | feedback       | wearable  at uncertain  | weight- |
|     |                 |                | sensors  moments        | ing     |
|     |                 |                | (motion                 | user    |
|     |                 |                | + audio)                | feed-   |
|     |                 |                | and state               | back,   |
|     |                 |                | transition              | query   |
|     |                 |                | graph                   | fre-    |
quency,
etc
|     | Model-based      | Generating     | Text- Confirming       | Thresh-   |
| --- | ---------------- | -------------- | ---------------------- | --------- |
|     | interactive      | preliminary    | to-SQL  or correcting  | olds for  |
|     | semantic pars-   | model out-     | dataset  uncer-        | error     |
|     | ing (Yao et al.  | puts, detect-  | (Wiki- tain SQL        | detec-    |
|     | 2019b)           | ing errors,    | SQL,  segments         | tion,     |
|     |                  | querying the   | Spider,                | query     |
|     |                  | user, and cor- | etc.)                  | fre-      |
|     |                  | recting model  |                        | quency,   |
|     |                  | outputs        |                        | etc       |
rank adaptation modules that update only the low-rank matrices in the model’s linear layers,
enabling efficient parameter tuning while avoiding the high computational costs associated
with training reward models. This method enhances model performance by achieving fine-
grained optimization, capturing subtle feedback differences, and reducing the risk of cata-
strophic forgetting. It also offers significant advantages in training efficiency and resource
utilization. Given that LLMs can partially substitute for human input, some researchers, like
Martin Klissarov, have proposed reinforcement learning based on feedback from large mod-
els (Klissarov et al. 2023). Klissarov introduced a novel approach called “Motif,” which
uses the prior knowledge of LLMs to construct intrinsic reward functions for RL agents,
facilitating the learning of preferences. Researchers evaluate model outputs using LLMs,
generate preference datasets, and then train reward models to fine-tune the original mod-
els. The intrinsic rewards generated by LLM significantly enhance model performance in
complex tasks and guide the model to produce behaviors consistent with human intuition.
LLMs have the distinct capability to blend high-level knowledge into specialized models
and ensure that model outputs are aligned with human ethical values and intentions (Guo
et al. 2024). In this context, Sun et al. (2024) proposed the SELF-ALIGN method, which
leverages principle-driven reasoning with the generative strengths of LLMs to enable AI
agents to self-align with minimal human intervention. This method employs a set of manu-
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 41 of 55  266
ally defined principles to direct the LLM’s response generation, greatly diminishing the
reliance on human supervisors. The team has developed 16 principles that specify the ideal
characteristics of system-generated responses. These principles act as a framework for pro-
ducing responses that are not only useful but also ethical and dependable. Through a process
of fine-tuning, these principles are incorporated into the LLM’s parameters, allowing the
model to autonomously generate responses that adhere to these guidelines, eliminating the
need for direct application of the principles and examples.
These approaches can be systematically integrated into the proposed framework. Table 13
details how each method relates to the terms of Eq. (12).
3.2.3.4 Analysis of model iterative refinement in AIL-ML In Model Iterative Refinement,
the kernel challenge lies in keeping a model’s performance and adaptability over extended
deployments. Equation (12) highlights how a model transitions from one state
M t to another M  by assimilating new data D t and agent feedback A t under specific
t+1
update parameters Λ t. By integrating feedback directly into the update loop, models evolve
in response to both shifts in data distributions and performance gaps identified during real-
world usage.
Model Iterative Refinement Based on Human Feedback refines model behavior and
resolve ambiguities, harnessing a key strength of humans to make context-sensitive judg-
ments. Although manual correcting can be costly or easy to variability, it also delivers a high
degree of interpretability and domain expertise. This feedback loop is particularly potent in
tasks where purely algorithmic metrics (e.g., BLEU scores in language tasks or standard
accuracy measures) fail to capture domain-specific or user-centric nuances. Iterative refine-

| Table 13 Symbol description for  | Method ψ | Dt At | Λt  |
| -------------------------------- | -------- | ----- | --- |
model iterative refinement based
on large model feedback Baize (Xu et  Iterative self- Generated  Ranking  LoRA
|     | al. 2023) distillation  | candidate  candidates  | adapta- |
| --- | ----------------------- | ---------------------- | ------- |
|     | process select-         | responses to use       | tion    |
ing highest- the best  param-
scoring  response  eters
response, then  for model
fine-tuning  fine-tuning
via LoRA
|     | Motif (Klis- Updating RL   | Environ- Providing    | RL       |
| --- | -------------------------- | --------------------- | -------- |
|     | sarov et al.  model using  | ment data preference  | hyperpa- |
|     | 2023) a combined           | feedback              | rameters |
reward  to the
(intrinsic  output of
from LLM +  the model
extrinsic from
environment)
|     | SELF- Principle-             | Expert- Principle-    | Param-      |
| --- | ---------------------------- | --------------------- | ----------- |
|     | ALIGN (Sun  driven           | defined  driven       | eters or    |
|     | et al. 2024) self-alignment  | principles  feedback  | strategies  |
|     | procedure                    | and seed  by LM       | for incor-  |
|     | incorporat-                  | prompts (replacing    | porating    |
ing the 16  extensive  these
principles human  principles
supervision into the
model
1 3

266 Page 42 of 55 J. Gao et al.
ment not only improves immediate performance but also reveals new data facets or user
needs over time, leading to gradually richer and more accurate models.
Model Iterative Refinement Based on Large Model Feedback-where LLMs supply itera-
tive feedback signals-extends scalability by partially or entirely substituting human. This
approach retains a continuous learning loop but relies on LLMs as proxies for human judg-
ment, offering faster turnaround and reduced manual overhead. Although such model-gen-
erated feedback can accelerate refinements, it also introduces potential biases or knowledge
gaps originating from the LLM itself. Therefore, researchers need to balance the conve-
nience and scalability of automated feedback against the risk of recursive error propaga-
tion, ensuring that checks and balances remain in place to maintain reliability and ethical
alignment.
4 Overview of application domains
4.1 Applications in general knowledge domain
In the domain of general knowledge within AIL-ML, various innovative applications have
been developed to enhance computational experiences, making them more enriching, help-
ful, and adaptable to specific deployment environments.
In the context of intelligent home environments, the incorporation of AIL-ML is gradu-
ally reshaping the interaction dynamics between users and automated systems, enabling
these systems to better understand and adapt to user behaviors through iterative feedback
loops. As shown in Fig. 7, this adaptation process leverages real-time data and agent inputs
to continuously refine and optimize the performance of smart home devices. Bootstrapping
methods for Human Activity Recognition in smart homes initiate with passive observation,
gradually building activity models through minimal supervision, thereby recognizing fre-
quent activities with significant precision (Hiremath et al. 2022). Additionally, applications
such as the “Listen Learner” (Wu et al. 2020) leverage user interactions for activity recogni-
tion, minimizing user effort while enhancing system adaptability to specific environments.
The PrISM-Tracker framework (Arakawa et al. 2023) employs wearable sensors and graph-
based state transitions, coupled with user inputs, to refine procedure tracking, addressing
uncertainties in real-time. The AI-to-Human Actuation (Cho et al. 2023) approach actively
makes user modify environmental conditions to improve the robustness of visual AI sensors,
aligning system responses with human activities more accurately. Additionally, Jiayuan Gao
et al. proposed LLMIE-UHAR (Gao et al. 2024), a method that leverages LLMs and itera-
tive evolution to achieve unsupervised HAR. In an IoT environment, multiple smart devices
generate vast streams of data. These data not only consist of raw information but also con-
tain rich contextual and semantic information, such as the background, time, location, and
interactions between devices. LLMIE-UHAR uses prompt engineering to transform sensor
data into textual descriptions rich in contextual information, making it comprehensible to
LLMs. Then, the LLM is used for analysis and inference, enabling precise annotation of
the sensor data. These applications highlight the integration of agent insights with machine
learning algorithms to enhance smart home ecosystems.
In the intelligent dialogue systems domain, the focus is on refining conversational agents
to offer more human-like interactions through advanced natural language processing and
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 43 of 55 266
Fig. 7 Frameworks of AIL-ML application in smart home environments. a Arakawa et al. (2023): Over-
view of PrISM-Tracker architecture which utilizes a transition graph and user-provided simulated oracles
to enhance the robustness and accuracy of HAR systems in procedural tracking. b Hiremath et al. (2022):
Overview of our bootstrapping method. Phase 1 involves representation learning and clustering to iden-
tify action units. Phase 2 focuses on discovering higher-level features, and Phase 3 involves deploying the
activity detection method within the smart home environment. c Wu et al. (2020): Listen Learner architec-
ture, a self-supervised algorithm that detects salient acoustic events and generates classifiers for activity
recognition, effectively minimizing user involvement. d Gao et al. (2024): Overview of LLMIE-UHAR
that leverages large language models and iterative evolution to realize unsupervised HAR. e Cho et al.
(2023): An example of how AI-to-human actuation complements an AI sensor under perception difficulty.
Note: The figures provide a rough conceptual understanding, and the text is not intended to be read in full
detail. The figures are borrowed from the following papers: (a) Arakawa et al. (2023), (b) Hiremath et al.
(2022), (c) Wu et al. (2020), (d) Gao et al. (2024), (e) Cho et al. (2023)
context management. The use of AIL-ML is key, enabling these systems to learn from user
interactions and improve over time (Hancock et al. 2019). AIL-ML can not only efficiently
utilize real-time conversational data for training but also dynamically adjust based on user
feedback and satisfaction, leading to an improvement in both the overall model performance
and user experience.
1 3

266 Page 44 of 55 J. Gao et al.
4.2 Applications in specialized knowledge domain
4.2.1 Medicine and healthcare
The significance of AIL-ML is increasingly recognized in specialized fields such as medi-
cine or healthcare (Budd et al. 2021). Despite the promising capabilities of large language
models in medicine, the enhancement of Clinical Decision Support systems and complex
clinical areas requires the incorporation of human insights through AIL methodologies.
As shown in Fig. 8a, in (Liu et al. 2023), clinical decision support logic summaries were
provided to ChatGPT, an AI-based question-and-answer tool developed from large lan-
guage models, to generate recommendations. These AI-generated recommendations were
reviewed by multiple clinicians and found to be high in understanding and relevance. How-
ever, they scored lower in terms of utility, acceptance, bias, inversion, and redundancy.
In applications like Medical Decision-Making, particularly with image retrieval systems,
machine learning algorithms fall short of capturing the nuanced understanding of similarity
as perceived by experts. This gap led to the development of a tool named SMILY (Cai et
al. 2019). It can be observed from Fig. 8 that the tool allows clinicians to directly influence
search algorithms, translating certain parameters into refined medical concepts for enhanced
diagnostic effectiveness and algorithmic trust without sacrificing accuracy. This approach
not only improves the diagnostic process but also enables users to adopt innovative strate-
gies for a deeper understanding and rectification of both machine learning and human errors.
The application of AIL-ML extends to dealing with computationally intensive tasks such
as subspace clustering, protein folding, and the K-anonymization of health data. In these
scenarios, the exponential search space can be significantly reduced with the aid of human
expertise through the heuristic selection of samples. In the context of health informatics,
particularly when tackling limited datasets or rare occurrences, the limitations of automated
machine learning due to insufficient training samples become evident. A study advocates
for the adoption of interactive machine learning, described as algorithms that enhance their
learning outcomes through interactions with agents, including humans (Holzinger 2016).
This approach allows AIL-ML to utilize human knowledge and experience, optimizing the
learning trajectories of machine learning models and thereby elevating their accuracy and
efficiency.
The deployment of AIL-ML in disease diagnosis, such as Coronary Artery Disease,
leverages expert insights integrated into the classification process, enhancing diagnostic
accuracy (Samaras et al. 2023). This approach not only augments the interpretability and
transparency of the models but also bolsters their reliability. AIL-ML applications effec-
tively address data bottlenecks in the treatment of various diseases, including pancreatic
cancer. According to Fig. 8c, by incorporating nuanced human judgments and expertise,
these systems enhance the efficiency and outcomes of medical interventions, as demon-
strated in recent studies (Mosqueira-Rey et al. 2023b).
4.2.2 Finance
AIL-ML is a paradigm that integrates agents into the machine learning loop, making it par-
ticularly suitable for fields that require strict supervision, such as finance. The application of
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 45 of 55 266
Fig. 8 Frameworks of AIL-ML application for specialized knowledge domain. a Liu et al. (2023) A pro-
totype of potential implementation in EHR system-AI decision support editors. b Cai et al. (2019) Key
components of SMILY. c Mosqueira-Rey et al. (2023b) The workflow of the AITL system which is de-
signed for expert to resolve the data bottleneck problem for the treatment of pancreatic cancer. Note: The
figures provide a rough conceptual understanding, and the text is not intended to be read in full detail. The
figures are borrowed from the following papers: (a) Liu et al. (2023), (b) Cai et al. (2019), (c) Mosqueira-
Rey et al. (2023b)
1 3

266 Page 46 of 55 J. Gao et al.
AIL-ML in finance is growing in importance since it enhances the safety and interpretability
of ML models.
Despite the growing use of ML in finance, the"black box"problem remains a major bar-
rier. Specifically, the"black box"is the risk that ML models’ outputs and operations are
unknown to and uncontrolled by human. Buckley et al. (2021) suggest that the most effec-
tive way to address this black box issue is by bringing humans into the ML loop, strength-
ening internal governance where external financial supervision may not be sufficient. They
propose three key AIL tools: (1) AI due diligence, which involves a thorough human evalu-
ation of potential risks before the development and deployment of AI; (2) AI explainability,
which ensures transparency in the model’s decision-making process, making it understand-
able to humans; and (3) AI review committees, where human oversight is responsible for
ethical decision-making, ensuring accountability for AI actions.
4.2.3 Law
Legal services is important in protecting individual rights and maintaining social fairness
(Auerbach 1977; Tushnet 2009; Cui et al. 2024). However, these services face many chal-
lenges, such as high costs, limited resources, complex legal terminology, frequent legisla-
tive changes and so on. Despite the impressive performance of large models in various
domains, they encounter the"hallucination problem"in the legal field, where generated con-
tent may be inaccurate or outdated, which will cause legal risks.
A notable example of applying AIL-ML in the legal domain is Chatlaw (Cui et al. 2024),
a multi-agent collaborative framework designed for intelligent legal consultation. As shown
in Fig. 9, agents are involved at multiple stages of the system. During the data preprocessing
stage, human refine and annotate the cleansed dataset, enabling the construction of high-
quality knowledge graphs and question-answer pairs. Furthermore, agents are integrated
into the core workflow of Chatlaw. Multiple agents, such as legal assistants and senior
lawyers, interact with users, dynamically updating knowledge graph nodes, generating
legal advice, and validating the relevance and legality of retrieved legal cases and clauses.
This process ensures the generated legal advice is accuracy and authority. Chatlaw not only
addresses the inherent interpretability challenges of legal tasks but also offers valuable
insights for developing reliable and context-aware legal support systems.
5 Discussion about limitation and future work
5.1 Limitation
AIL-ML, as a process-oriented paradigm, spans multiple research domains but lacks well-
defined research objectives and standardized methodologies characteristic of fields like
transfer learning or domain generalization. While it is widely applied in areas such as data
acquisition, model training, cold-start problems, and data annotation, AIL-ML incorporates
diverse techniques, including human feedback, active learning, and LLMs. Due to the broad
range of applications and the variety of techniques involved, AIL-ML methods are chal-
lenging to describe in a precise and detailed manner. Instead, they can be summarized by
focusing on optimization strategies in data acquisition, processing, and model development,
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 47 of 55 266
Fig. 9 Framework of Chatlaw (Cui et al. 2024). Note: The figure is borrowed from Cui et al. (2024)
such as reducing annotation costs, improving data initialization, or enhancing model train-
ing through agents. This high-level abstraction provides flexibility and broad applicability
but also introduces the limitation of lacking standardization in research methods. Conse-
quently, much of the ongoing work focuses on integrating existing techniques within the
AIL-ML framework, without establishing a unified technical process or evaluation criteria.
Therefore, AIL-ML functions more as a guiding philosophy than as a specific technical
toolkit. Future research should prioritize the development of domain-specific methodolo-
gies and standardized frameworks to enhance the consistency and practicality of AIL-ML
applications.
A potential limitation of the AIL-ML framework lies in its reliance on the performance
of LLMs. While LLMs provide advanced capabilities in reasoning and language under-
1 3

266 Page 48 of 55 J. Gao et al.
standing, their outputs in specialized domains may be inaccurate or misleading, potentially
lowering the overall system performance. Additionally, LLMs are often considered"black
boxes,"lacking transparency and interpretability. This limitation can hinder the adoption of
AIL-ML in fields requiring high levels of trust and explainability, such as medical diagnos-
tics. AIL-ML relies on a combination of human input and agent feedback, making it more
dependent on the quality and reliability of the agents used within the system. This distinc-
tion highlights the need for further research into improving the transparency and accuracy
of LLMs when integrated into the AIL-ML framework.
5.2 Future directions
Building Trust in AIL-ML Systems with Counterfactual Explanations One critical aspect of
AIL-ML systems is establishing trust between agnets and the models. Trust can be achieved
through counterfactual explanations, which help users understand how and why a model’s
output changes under hypothetical input conditions. This aligns with human reasoning pro-
cesses, enabling non-experts to familiarize themselves with the decision boundaries of ML
models. Del Ser et al. (2024) conduct a generative framework that employs counterfactual
explanations to balance plausibility, change intensity, and adversarial power through multi-
objective optimization. This approach not only enhances interpretability but also uncovers
concept-based biases and misrepresented features within the model, making it a valuable
tool for fostering trust. This facilitates better understanding of model limitations, encour-
ages informed decision-making, and ensures that AIL-ML systems are perceived as reliable
and transparent. Future research could explore combining counterfactual explanations with
other interpretability techniques to create a more comprehensive trust-building framework,
further advancing AIL-ML’s applicability in sensitive and high-stakes environments.
Reducing Bias in AIL-ML Framework. In AIL-ML, how to reduce bias is an impor-
tant and valuable research direction. Currently, both LLMs and human experts are inher-
ently biased. For instance, LLMs may exhibit selection bias by being overly sensitive to
changes in input options’ order or position (Zheng et al. 2023) and the training data for
LLMs often contains embedded social, cultural, or historical biases that can be amplified
in outputs. Additionally, human experts involved in the AIL process may also have cog-
nitive biases, which can result in unbalanced or biased knowledge being introduced into
the ML. Therefore, future research must focus on developing methods to ensure unbiased
knowledge injection within the AIL-ML framework. This involves not only mitigating bias
at the source (from both agents like LLMs and human contributors) but also establish-
ing mechanisms to detect and correct biases during data annotation, model training, and
feedback loops. Approaches could include designing fairer selection mechanisms, imple-
menting diverse annotation strategies, and employing de-biasing techniques to counteract
both selection and data biases. Moreover, algorithms capable of identifying and rectifying
potential biases in human and LLM-based annotations will further enhance the fairness and
reliability of AIL-ML systems. By systematically addressing bias, AIL-ML can improve its
applicability to high-stakes domains such as healthcare and legal decision-making, where
trust and explainability are important, while also promoting fairness and generalizability
across diverse applications. This research direction is crucial not only for enhancing the
technical performance of AIL-ML systems but also for advancing the social responsibility
of AI technologies.
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 49 of 55 266
Enabling Agents to Handle High-Dimensional and Unstructured Data in AIL-ML. A sig-
nificant research direction for AIL-ML is finding effective methods to enable agents to pro-
cess high-dimensional and unstructured data. Currently, most AIL-ML systems are designed
to handle low-dimensional data or natural language, with limited exploration of unstruc-
tured data types such as images, sensor signals, and acoustic data. In practical applications
like smart homes and healthcare, the lack of context-awareness for these unstructured data
types limits the potential of intelligent systems. Addressing this challenge by developing
techniques that allow agents to handle complex, high-dimensional data can unlock new
possibilities for AIL-ML, enabling more robust contextual understanding and improved
performance in diverse environments. This direction holds great promise for enhancing the
adaptability and intelligence of systems in fields like IoT and smart healthcare, where deal-
ing with unstructured data is crucial.
Enhancing Collaboration Between Large Models and Humans in AIL-ML. A promising
future direction for AIL-ML research is focusing on improving the collaboration between
LLMs and humans. As AIL systems continue to evolve, the autonomy and collaboration
mechanisms in multi-agent systems become critical. Future research can explore how to
establish effective collaboration frameworks among multiple agents, including domain-spe-
cific LLMs and human experts. These agents can collaborate and share knowledge, enabling
more effective handling of complex tasks. By fostering better cooperation between large
models and human experts, AIL-ML systems can significantly enhance their performance
and adaptability across diverse applications. This direction opens up new possibilities for
optimizing human-AI interaction, making AIL systems more versatile and capable in vari-
ous real-world scenarios.
6 Conclusion
Human-in-the-Loop Machine Learning (HIL-ML) has become an important research topic
in machine learning research. The development and popularization of large models intro-
duce both challenges and opportunities to this field. In this paper, we present a comprehen-
sive survey of AIL-ML (which is also called AIL-ML), providing an in-depth review of
its methodologies across key stages of machine learning, including a structured review of
data collection, data initialization, data quality enhancement, data annotation, model cold
start, model training, and iterative model refinement. Furthermore, we summarize AIL-ML
applications in diverse fields. Finally, we analyze the current challenges and highlight future
directions. We hope that this survey will serve as a valuable resource for researchers, offer-
ing insights that encourage further exploration and development in AIL-ML.
Acknowledgements This work is supported by the Natural Science Foundation of China (No.62302487),
Improvement Project of Chinese Academy of Sciences (No.GSZXKYZB2025007), the Science and Tech-
nology Innovation Program of Hunan Province (No.2022RC4006, No.2024 JJ9031), and the Innovation
Funding of ICT, CAS.
Author contributions Jiayuan Gao conducted the literature review, developed the framework, wrote the
manuscript, drafted the figures, prepared Figures 6,7,8 and coordinated the work among the authors. Yingwei
Zhang and Yiqiang Chen contributed to the framework development. Yihan Dong conducted the literature
review and prepared Figures 1 and 2. Yuanzhe Chen contributed to writing the manuscript and prepared Fig-
ure 3. Shuchao Song prepared Figures 4 and 5. Boshi Tang and Yang Gu provided suggestions for manuscript
revisions. All authors reviewed the manuscript.
1 3

266 Page 50 of 55 J. Gao et al.
Data availability No datasets were generated or analysed during the current study.
Declarations
Conflict of interest The authors declare no Conflict of interest.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-
NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it.
The images or other third party material in this article are included in the article’s Creative Commons licence,
unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative
Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use,
you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit h
t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 /.
References
Ahn Y, Lin Y-R, Xu P, Dai Z (2023) Escape: countering systematic errors from machine’s blind spots via
interactive visual analysis. In: Proceedings of the 2023 CHI Conference on Human Factors in Comput-
ing Systems, pp 1–16
Arakawa R, Yakura H, Mollyn V, Nie S, Russell E, DeMeo DP, Reddy HA, Maytin AK, Carroll BT, Lehman
JF et al (2023) Prism-tracker: A framework for multimodal procedure tracking using wearable sensors
and state transition information with user-driven handling of errors and uncertainty. Proceedings of the
ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 6(4):1–27
Arous I, Dolamic L, Yang J, Bhardwaj A, Cuccu G, Cudré-Mauroux P (2021) Marta: leveraging human
rationales for explainable text classification. In: Proceedings of the AAAI Conference on Artificial Intel-
ligence, vol 35, pp. 5868–5876
Auerbach JS (1977) Unequal justice: lawyers and social change in modern America. Oxford University
Press, Oxford
Bartolo M, Roberts A, Welbl J, Riedel S, Stenetorp P (2020) Beat the ai: investigating adversarial human
annotation for reading comprehension. Trans Assoc Comput Linguist 8:662–678
Ben-David S, Blitzer J, Crammer K, Pereira F (2006) Analysis of representations for domain adaptation. Adv
Neural Inf Process Syst. h t t p s : / / d o i . o r g / 1 0 . 7 5 5 1 / m i t p r e s s / 7 5 0 3 . 0 0 3 . 0 0 2 2
Bommasani R, Hudson DA, Adeli E, Altman R, Arora S, Arx S, Bernstein MS, Bohg J, Bosselut A, Brunskill
E, et al (2021) On the opportunities and risks of foundation models. Preprint at h t t p s : / / a r x i v . o r g / a b s / q
u a n t - p h / 2 1 0 8 . 0 7 2 5 8
Brown T, Mann B, Ryder N, Subbiah M, Kaplan JD, Dhariwal P, Neelakantan A, Shyam P, Sastry G, Askell
A et al (2020) Language models are few-shot learners. Adv Neural Inf Process Syst 33:1877–1901
Buckley RP, Zetzsche DA, Arner DW, Tang BW (2021) Regulating artificial intelligence in finance: putting
the human in the loop. Sydney Law Rev 43(1):43–81
Budd S, Robinson EC, Kainz B (2021) A survey on active learning and human-in-the-loop deep learning for
medical image analysis. Med Image Anal 71:102062
Cai CJ, Reif E, Hegde N, Hipp J, Kim B, Smilkov D, Wattenberg M, Viegas F, Corrado GS, Stumpe MC, et al
(2019) Human-centered tools for coping with imperfect algorithms during medical decision-making. In:
Proceedings of the 2019 Chi Conference on Human Factors in Computing Systems, pp 1–14
Chen K, Zhang D, Yao L, Guo B, Yu Z, Liu Y (2021a) Deep learning for sensor-based human activity recog-
nition: overview, challenges, and opportunities. ACM Comput Surv (CSUR) 54(4):1–40
Chen X, Jiang M, Zhao Q (2021b) Leveraging human attention in novel object captioning. In: International
Joint Conference on Artificial Intelligence
Cho S, Kim Y, Jang J, Hwang I (2023) Ai-to-human actuation: Boosting unmodified ai’s robustness by pro-
actively inducing favorable human sensing conditions. Proceedings of the ACM on Interactive, Mobile,
Wearable and Ubiquitous Technologies 7(1):1–32
Crochepierre L, Boudjeloud-Assala L, Barbesant V (2022) Interactive reinforcement learning for symbolic
regression from multi-format human-preference feedbacks. In: 31st International Joint Conference on
Artificial Intelligence (IJCAI 2022)
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 51 of 55 266
Cui Y, Koppol P, Admoni H, Niekum S, Simmons R, Steinfeld A, Fitzgerald T (2021) Understanding the rela-
tionship between interactions and outcomes in human-in-the-loop machine learning. In: International
Joint Conference on Artificial Intelligence
Cui J, Ning M, Li Z, Chen B, Yan Y, Li H, Ling B, Tian Y, Yuan L (2024) Chatlaw: a multi-agent collabora-
tive legal assistant with knowledge graph enhanced mixture-of-experts large language model. Preprint
at https://arxiv.org/abs/quant-ph/2306.16092
Dai H, Liu Z, Liao W, Huang X, Cao Y, Wu Z, Zhao L, Xu S, Liu W, Liu N et al (2023) Auggpt: leveraging
chatgpt for text data augmentation. Preprint at https://arxiv.org/abs/quant-ph/2302.13007
Del Ser J, Barredo-Arrieta A, Díaz-Rodríguez N, Herrera F, Saranti A, Holzinger A (2024) On generating
trustworthy counterfactual explanations. Inf Sci 655:119898. https://doi.org/10.1016/j.ins.2023.119898
Ding B, Qin C, Liu L, Bing L, Joty SR, Li BA (2022) Is gpt-3 a good data annotator? In: Annual meeting
of the Association for Computational Linguistics. h t t p s : / / a p i . s e m a n t i c s c h o l a r . o r g / C o r p u s I D : 2 5 4 8 7 7 1 7 1
Dwork C (2006) Differential privacy. International colloquium on automata, languages, and programming.
Springer, Cham, pp 1–12
Fan Y, Watkins O, Du Y, Liu H, Ryu M, Boutilier C, Abbeel P, Ghavamzadeh M, Lee K, Lee K (2024) Rein-
forcement learning for fine-tuning text-to-image diffusion models. Adv Neural Inf Process Syst. h t t p s : /
/ d o i . o r g / 1 0 . 4 8 5 5 0 / a r X i v . 2 3 0 5 . 1 6 3 8 1
Gao J, Pi R, Lin Y, Xu H, Ye J, Wu Z, Zhang W, Liang X, Li Z, Kong L (2023) Self-guided noise-free
data generation for efficient zero-shot learning. In: The Twelfth International Conference on Learning
Representations
Gao J, Zhang Y, Chen Y, Zhang T, Tang B, Wang X (2024) Unsupervised human activity recognition via
large language models and iterative evolution. In: ICASSP 2024-2024 IEEE International Conference
on Acoustics, Speech and Signal Processing (ICASSP), IEEE, pp 91–95
Gou J, Yu B, Maybank SJ, Tao D (2021) Knowledge distillation: a survey. Int J Comput Vis 129(6):1789–1819
Guo S, Zhang B, Liu T, Liu T, Khalman M, Llinares F, Rame A, Mesnard T, Zhao Y, Piot B, et al (2024)
Direct language model alignment from online ai feedback. Preprint at h t t p s : / / a r x i v . o r g / a b s / q u a n t - p h / 2
4 0 2 . 0 4 7 9 2
Hancock B, Bordes A, Mazare P-E, Weston J (2019) Learning from dialogue after deployment: feed yourself,
chatbot! Preprint at https://arxiv.org/abs/quant-ph/1901.05415
He Z, Ribeiro MT, Khani F (2023a) Targeted data generation: finding and fixing model weaknesses. In:
Rogers A, Boyd-Graber J, Okazaki N (eds) Proceedings of the 61st Annual Meeting of the Associa-
tion for Computational Linguistics (Vol 1: Long Papers), Association for Computational Linguistics,
Toronto, pp 8506–8520. h t t p s : / / d o i . o r g / 1 0 . 1 8 6 5 3 / v 1 / 2 0 2 3 . a c l - l o n g . 4 7 4. h t t p s : / / a c l a n t h o l o g y . o r g / 2 0 2 3
. a c l - l o n g . 4 7 4
He X, Lin Z, Gong Y, Jin A, Zhang H, Lin C, Jiao J, Yiu SM, Duan N, Chen W, et al (2023b) Annollm: mak-
ing large language models to be better crowdsourced annotators. Preprint at h t t p s : / / a r x i v . o r g / a b s / q u a n
t - p h / 2 3 0 3 . 1 6 8 5 4
Hemmer P, Schellhammer S, Vössing M, Jakubik J, Satzger G (2022) Forming effective human-ai teams:
building machine learning models that complement the capabilities of multiple experts. Preprint at
https://arxiv.org/abs/quant-ph/2206.07948
Hinton G (2015) Distilling the knowledge in a neural network. Preprint at h t t p s : / / a r x i v . o r g / a b s / q u a n t - p h / 1 5
0 3 . 0 2 5 3 1
Hiremath SK, Nishimura Y, Chernova S, Plötz T (2022) Bootstrapping human activity recognition systems
for smart homes from scratch. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiqui-
tous Technologies 6(3):1–27
Holzinger A (2016) Interactive machine learning for health informatics: when do we need the human-in-the-
loop? Brain Inform 3(2):119–131
Hsieh C-Y, Li C-L, Yeh C-K, Nakhost H, Fujii Y, Ratner A, Krishna R, Lee C-Y, Pfister T (2023a) Distilling
step-by-step! outperforming larger language models with less training data and smaller model sizes. In:
Rogers A, Boyd-Graber J, Okazaki N (eds) Findings of the Association for Computational Linguistics:
ACL 2023, Association for Computational Linguistics, Toronto, pp 8003–8017. h t t p s : / / d o i . o r g / 1 0 . 1 8 6 5
3 / v 1 / 2 0 2 3 . fi n d i n g s - a c l . 5 0 7. h t t p s : / / a c l a n t h o l o g y . o r g / 2 0 2 3 . fi n d i n g s - a c l . 5 0 7
Hsieh C (2023b) Human-centred multimodal deep learning models for chest x-ray diagnosis. In: Proceedings
of the Thirty-Second International Joint Conference on Artificial Intelligence, pp 7085–7086
Kath H, Gouvêa TS, Sonntag D (2023) A human-in-the-loop tool for annotating passive acoustic monitoring
datasets. In: Proceedings of the 32nd International Joint Conference on Artificial Intelligence, IJCAI
Kenton JDMWC, Toutanova LK (2019) Bert: pre-training of deep bidirectional transformers for language
understanding. In: Proceedings of NAACL-HLT, pp 4171–4186
Klie J-C, Castilho RE, Gurevych I (2020) From zero to hero: Human-in-the-loop entity linking in low
resource domains. In: Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics, pp 6982–6993
1 3

266 Page 52 of 55 J. Gao et al.
Klissarov M, D’Oro P, Sodhani S, Raileanu R, Bacon P-L, Vincent P, Zhang A, Henaff M (2023) Motif:
intrinsic motivation from artificial intelligence feedback
Koppol P, Admoni H, Simmons RG (2021) Interaction considerations in learning from humans. In: IJCAI,
pp 283–291
Krizhevsky A, Sutskever I, Hinton GE (2012) Imagenet classification with deep convolutional neural net-
works. Adv Neural Inf Process Syst 25
Kwon M, Michael S (2023) Reward design with language models. In: International Conference on Learning
Representations (ICLR)
LeCun Y, Bengio Y, Hinton G (2015) Deep learning. Nature 521(7553):436–444
Li G (2017) Human-in-the-loop data integration. Proc VLDB Endow 10(12):2006–2017
Li H, Dong Q, Tang Z, Wang C, Zhang X, Huang H, Huang S, Huang X, Huang Z, Zhang D et al (2024)
Synthetic data (almost) from scratch: generalized instruction tuning for language models. Preprint at
https://arxiv.org/abs/quant-ph/2402.13064
Liu Z, Guo Y, Mahmud J (2021) When and why a model fails? a human-in-the-loop error detection frame-
work for sentiment analysis. In: Proceedings of the 2021 Conference of the North American Chapter
of the Association for Computational Linguistics: human language technologies: Industry Papers, pp
170–177
Liu S, Wright AP, Patterson BL, Wanderer JP, Turer RW, Nelson SD, McCoy AB, Sittig DF, Wright A (2023)
Using ai-generated suggestions from chatgpt to optimize clinical decision support. J Am Med Inform
Assoc 30(7):1237–1245
Long Y, Wei W, Huang T, Wang Y, Dou Q (2023) Human-in-the-loop embodied intelligence with interactive
simulation environment for surgical robot learning. IEEE Robot Autom Lett 8:4441–8
Lu F, Wang W, Luo Y, Zhu Z, Sun Q, Xu B, Shi H, Gao S, Li Q, Song Y, et al (2024) Miko: multimodal inten-
tion knowledge distillation from large language models for social-media commonsense discovery. In:
Proceedings of the 32nd ACM International Conference on Multimedia, pp 3303–3312
Metsch JM, Saranti A, Angerschmid A, Pfeifer B, Klemt V, Holzinger A, Hauschild A-C (2024) Clarus:
An interactive explainable ai platform for manual counterfactuals in graph neural networks. J Biomed
Inform 150:104600. https://doi.org/10.1016/j.jbi.2024.104600
Mondorf P, Plank B (2024) Beyond accuracy: evaluating the reasoning behavior of large language models—a
survey. Preprint at https://arxiv.org/abs/quant-ph/2404.01869
Mosqueira-Rey E, Hernández-Pereira E, Alonso-Ríos D, Bobes-Bascarán J, Fernández-Leal Á (2023a)
Human-in-the-loop machine learning: a state of the art. Artif Intell Rev 56(4):3005–3054
Mosqueira-Rey E, Hernández-Pereira E, Bobes-Bascarán J, Alonso-Ríos D, Pérez-Sánchez A, Fernández-
Leal Á, Moret-Bonillo V, Vidal-Ínsua Y, Vázquez-Rivera F (2023b) Addressing the data bottleneck in
medical deep learning models using a human-in-the-loop machine learning approach. Neural Comput
Appl 36:2597
Oh SW, Lee J-Y, Xu N, Kim SJ (2019) Fast user-guided video object segmentation by interaction-and-
propagation networks. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp 5247–5256
Ouyang L, Wu J, Jiang X, Almeida D, Wainwright C, Mishkin P, Zhang C, Agarwal S, Slama K, Ray A et al
(2022) Training language models to follow instructions with human feedback. Adv Neural Inf Process
Syst 35:27730–27744
Pan W, Wang X, Song M, Chen C (2020) Survey on generating adversarial examples. Ruan Jian Xue Bao/J
Softw 31(1):67–81 (in Chinese)
Park JS, Hessel J, Chandu K, Liang PP, Lu X, West P, Yu Y, Huang Q, Gao J, Farhadi A et al (2023) Local-
ized symbolic knowledge distillation for visual commonsense models. Adv Neural Inf Process Syst
36:11338–11352
Qian K, Raman PC, Li Y, Popa L (2020) Partner: Human-in-the-loop entity name understanding with deep
learning. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol 34, pp 13634–13635
Radford A, Narasimhan K, Salimans T, Sutskever I, et al (2018) Improving language understanding by gen-
erative pre-training.
Retzlaff CO, Das S, Wayllace C, Mousavi P, Afshari M, Yang T, Saranti A, Angerschmid A, Taylor ME,
Holzinger A (2024) Human-in-the-loop reinforcement learning: a survey and position on requirements,
challenges, and opportunities. J Artif Int Res. https://doi.org/10.1613/jair.1.15348
Roels J, Vernaillen F, Kremer A, Gonçalves A, Aelterman J, Luong HQ, Goossens B, Philips W, Lippens
S, Saeys Y (2019) A ‘human-in-the-loop’approach for semi-automated image restoration in electron
microscopy. BioRxiv. https://doi.org/10.1101/644146
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 53 of 55 266
Sahu G, Vechtomova O, Bahdanau D, Laradji I (2023) Promptmix: a class boundary augmentation method
for large language model distillation. In: Bouamor H, Pino J, Bali K. (eds) Proceedings of the 2023
Conference on Empirical Methods in Natural Language Processing, Association for Computational Lin-
guistics, Singapore, pp 5316–5327 h t t p s : / / d o i . o r g / 1 0 . 1 8 6 5 3 / v 1 / 2 0 2 3 . e m n l p - m a i n . 3 2 3. h t t p s : / / a c l a n t h o
l o g y . o r g / 2 0 2 3 . e m n l p - m a i n . 3 2 3
Samaras A-D, Moustakidis S, Apostolopoulos ID, Papandrianos N, Papageorgiou E (2023) Classification
models for assessing coronary artery disease instances using clinical and biometric data: an explainable
man-in-the-loop approach. Scientific Rep 13(1):6668
Settles B (2009) Active learning literature survey
Stiennon N, Ouyang L, Wu J, Ziegler D, Lowe R, Voss C, Radford A, Amodei D, Christiano PF (2020) Learn-
ing to summarize with human feedback. Adv Neural Inf Process Syst 33:3008–3021
Sun Z, Shen Y, Zhou Q, Zhang H, Chen Z, Cox D, Yang Y, Gan C (2024) Principle-driven self-alignment of
language models from scratch with minimal human supervision. Adv Neural Inf Process Syst 36:2511
Tchemeube RB, Ens J, Plut C, Pasquier P, Safi M, Grabit Y, Rolland J-B (2023) Evaluating human-ai interac-
tion via usability, user experience and acceptance measures for mmm-c: a creative ai system for music
composition. In: Proceedings of the Thirty-Second International Joint Conference on Artificial Intel-
ligence, pp 5769–5778
Touvron H, Lavril T, Izacard G, Martinet X, Lachaux M-A, Lacroix T, Rozière B, Goyal N, Hambro E, Azhar
F, et al (2023) Llama: open and efficient foundation language models. Preprint at h t t p s : / / a r x i v . o r g / a b s /
q u a n t - p h / 3 0 2 . 1 3 9 7 1
Tushnet MV (2009) The rights revolution in the twentieth century. American Historical Association,
Washington
Vaswani A (2017) Attention is all you need. Adv Neural Inf Process Syst 30:1
Wallace E, Rodriguez P, Feng S, Yamada I, Boyd-Graber J (2019) Trick me if you can: human-in-the-loop
generation of adversarial examples for question answering. Trans Assoc Comput Linguist 7:387–401
Wang S, Liu Y, Xu Y, Zhu C, Zeng M (2021) Want to reduce labeling cost? GPT-3 can help. In: Moens
M.-F, Huang X, Specia L, Yih SW-T (eds) Findings of the Association for Computational Linguistics:
EMNLP 2021, Association for Computational Linguistics, Punta Cana, pp 4195–4205. h t t p s : / / d o i . o r g / 1
0 . 1 8 6 5 3 / v 1 / 2 0 2 1 . fi n d i n g s - e m n l p . 3 5 4. h t t p s : / / a c l a n t h o l o g y . o r g / 2 0 2 1 . fi n d i n g s - e m n l p . 3 5 4
Wang J, Lan C, Liu C, Ouyang Y, Qin T, Lu W, Chen Y, Zeng W, Yu P (2022) Generalizing to unseen
domains: a survey on domain generalization. IEEE Trans Knowl Data Eng 35:8052
Wang Y, Yu Z, Liu S, Zhou Z, Guo B (2023a) Genie in the model: Automatic generation of human-in-the-loop
deep neural networks for mobile applications. Proceedings of the ACM on Interactive, Mobile, Wear-
able and Ubiquitous Technologies 7(1):1–29
Wang Y, Kordi Y, Mishra S, Liu A, Smith NA, Khashabi D, Hajishirzi H (2023b) Self-instruct: aligning lan-
guage models with self-generated instructions. In: Rogers A, Boyd-Graber J, Okazaki N (eds) Proceed-
ings of the 61st Annual Meeting of the Association for Computational Linguistics (Vol 1: Long Papers),
Association for Computational Linguistics, Toronto, pp 13484–13508. h t t p s : / / d o i . o r g / 1 0 . 1 8 6 5 3 / v 1 / 2 0 2
3 . a c l - l o n g . 7 5 4. https://aclanthology.org/2023.acl-long.754
Wang X, Kim H, Rahman S, Mitra K, Miao Z (2024) Human-llm collaborative annotation through effective
verification of llm labels. In: Proceedings of the CHI Conference on Human Factors in Computing
Systems, pp 1–21
Weber T, Hußmann H, Han Z, Matthes S, Liu Y (2020) Draw with me: human-in-the-loop for image restora-
tion. In: Proceedings of the 25th International Conference on Intelligent User Interfaces, pp 243–253
Wei J, Xie H, Chang C, Yang X (2022) Fine-tuning Deep Neural Networks by Interactively Refining the 2D
Latent Space of Ambiguous Images. In: International Joint Conference on Artificial Intelligence
Wu J, Harrison C, Bigham JP, Laput G (2020) Automated class discovery and one-shot interactions for acous-
tic activity recognition. In: Proceedings of the 2020 CHI Conference on Human Factors in Computing
Systems, pp 1–14
Wu X, Xiao L, Sun Y, Zhang J, Ma T, He L (2022) A survey of human-in-the-loop for machine learning.
Future Gener Comput Syst 135:364–381. https://doi.org/10.1016/j.future.2022.05.014
Xin D, Ma L, Liu J, Macke S, Song S, Parameswaran A (2018) Accelerating human-in-the-loop machine
learning: challenges and opportunities. In: Proceedings of the second workshop on data management
for end-to-end machine learning, pp 1–4
Xu X, Gong J, Brum C, Liang L, Suh B, Gupta SK, Agarwal Y, Lindsey L, Kang R, Shahsavari B, et al (2022)
Enabling hand gesture customization on wrist-worn devices. In: Proceedings of the 2022 CHI Confer-
ence on Human Factors in Computing Systems, pp 1–19
1 3

266 Page 54 of 55 J. Gao et al.
Xu C, Guo D, Duan N, McAuley J (2023) Baize: an open-source chat model with parameter-efficient tuning
on self-chat data. In: Bouamor H, Pino J, Bali K (eds) Proceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing, Association for Computational Linguistics, Singapore, pp.
6268–6278. h t t p s : / / d o i . o r g / 1 0 . 1 8 6 5 3 / v 1 / 2 0 2 3 . e m n l p - m a i n . 3 8 5. h t t p s : / / a c l a n t h o l o g y . o r g / 2 0 2 3 . e m n l p - m
a i n . 3 8 5
Xu X, Li M, Tao C, Shen T, Cheng R, Li J, Xu C, Tao D, Zhou T (2024) A survey on knowledge distillation
of large language models. Preprint at https://arxiv.org/abs/quant-ph/2402.13116
Yao Z, Li X, Gao J, Sadler B, Sun H (2019a) Interactive semantic parsing for if-then recipes via hierarchical
reinforcement learning. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol 33, pp
2547–2554
Yao Z, Su Y, Sun H, Yih W-T (2019b) Model-based interactive semantic parsing: a unified formulation and
a text-to-sql case study. In: 2019 Conference on Empirical Methods in Natural Language Processing
(EMNLP’19)
Ye J, Gao J, Li Q, Xu H, Feng J, Wu Z, Yu T, Kong L (2022) ZeroGen: efficient zero-shot learning via dataset
generation. In: Goldberg Y, Kozareva Z, Zhang Y (eds) Proceedings of the 2022 Conference on Empiri-
cal Methods in Natural Language Processing, Association for Computational Linguistics, Abu Dhabi,
pp 11653–11669. h t t p s : / / d o i . o r g / 1 0 . 1 8 6 5 3 / v 1 / 2 0 2 2 . e m n l p - m a i n . 8 0 1. h t t p s : / / a c l a n t h o l o g y . o r g / 2 0 2 2 . e m
n l p - m a i n . 8 0 1
Ye W, Zhang Y, Wang M, Wang S, Gu X, Abbeel P, Gao Y (2023) Foundation reinforcement learning:
towards embodied generalist agents with foundation prior assistance. Preprint at h t t p s : / / a r x i v . o r g / a b s
/ q u a n t - p h / 2 3 1 0 . 0 2 6 3 5
Yu F, Seff A, Zhang Y, Song S, Funkhouser T, Xiao J (2015) Lsun: construction of a large-scale image data-
set using deep learning with humans in the loop. Preprint at https://arxiv.org/abs/quant-ph/1506.03365
Zhang S, He L, Dragut E, Vucetic S (2019) How to invest my time: lessons from human-in-the-loop entity
extraction. In: Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discov-
ery & Data Mining, pp 2305–2313
Zhang C, Bengio S, Hardt M, Recht B, Vinyals O (2021) Understanding deep learning (still) requires rethink-
ing generalization. Commun ACM 64(3):107–115
Zheng C, Zhou H, Meng F, Zhou J, Huang M (2023) Large language models are not robust multiple choice
selectors. In: The Twelfth International Conference on Learning Representations
Zhuang F, Qi Z, Duan K, Xi D, Zhu Y, Zhu H, Xiong H, He Q (2020) A comprehensive survey on transfer
learning. Proc IEEE 109(1):43–76
Ziegler DM, Stiennon N, Wu J, Brown TB, Radford A, Amodei D, Christiano P, Irving G (2019) Fine-tuning
language models from human preferences. Preprint at https://arxiv.org/abs/quant-ph/1909.08593
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Authors and Affiliations
Jiayuan Gao1,2 · Yingwei Zhang1,2 · Yiqiang Chen1,2 · Yihan Dong3 · Yuanzhe Chen1,2 ·
Shuchao Song1,2 · Boshi Tang4 · Yang Gu1,2
Yiqiang Chen
yqchen@ict.ac.cn
Jiayuan Gao
gaojiayuan20z@ict.ac.cn
Yingwei Zhang
zhangyingwei@ict.ac.cn
Yihan Dong
3120215895@bit.edu.cn
Yuanzhe Chen
chenyuanzhe21s@ict.ac.cn
Shuchao Song
1 3

Agent-in-the-loop to distill expert knowledge into artificial intelligence… Page 55 of 55 266
songshuchao22b@ict.ac.cn
Boshi Tang
tbs22@mails.tsinghua.edu.cn
Yang Gu
guyang@ict.ac.cn
1 Beijing Key Laboratory of Mobile Computing and Pervasive Device, Institute of Computing
Technology, Chinese Academy of Sciences, Beijing, China
2 University of Chinese Academy of Sciences, Beijing, China
3 Beijing Institute of Technology, Beijing, China
4 Tsinghua University, Beijing, China
1 3