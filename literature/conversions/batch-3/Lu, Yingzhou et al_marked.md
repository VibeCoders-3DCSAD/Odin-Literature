---
conversion_metadata:
  converted_at: "2026-07-21T14:06:46Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Lu, Yingzhou et al.pdf"
  source_pdf_sha256: "ed7034ff3db91e40968ec0558fe9920fde7b82f45f0ee08735f3ba43daa9d68b"
  page_count: 18
  markdown_char_count: 285500
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

1

Machine Learning for Synthetic Data Generation:
A Review
Yingzhou Lu§, Lulu Chen††, Yuanyuan Zhang‡‡, Minjie Shen†, Huazheng Wang‡, Xiao Wang∥, Capucine van
Rechem§, Tianfan Fu∗, Wenqi Wei∗∗¶

5
2
0
2

r
p
A
4

]

G
L
.
s
c
[

0
1
v
2
6
0
4
0
.
2
0
3
2
:
v
i
X
r
a

Abstract—Machine learning heavily relies on data, but real-
world applications often encounter various data-related issues.
These include data of poor quality, insufficient data points leading
to under-fitting of machine learning models, and difficulties in
data access due to concerns surrounding privacy, safety, and
regulations. In light of these challenges, the concept of synthetic
data generation emerges as a promising alternative that allows
for data sharing and utilization in ways that real-world data
cannot facilitate. This paper presents a comprehensive systematic
review of existing studies that employ machine learning models
for the purpose of generating synthetic data. The review en-
compasses various perspectives, starting with the applications
of synthetic data generation, spanning computer vision, speech,
natural language processing, healthcare, and business domains.
it explores different machine learning methods,
Additionally,
with particular emphasis on neural network architectures and
deep generative models. The paper also addresses the crucial
aspects of privacy and fairness concerns related to synthetic
data generation. Furthermore, this study identifies the challenges
and opportunities prevalent in this emerging field, shedding light
on the potential avenues for future research. By delving into
the intricacies of synthetic data generation, this paper aims to
contribute to the advancement of knowledge and inspire further
exploration in synthetic data generation.

Index Terms—data synthesis, machine learning, generative

modeling

I. INTRODUCTION

M ACHINE learning endows intelligent computer systems

with the capacity to autonomously tackle tasks, pushing
the envelope of industrial innovation [1]. By integrating high-
performance computing, contemporary modeling, and simu-
lations, machine learning has evolved into an indispensable
instrument for managing and analyzing massive volumes of
data [2], [3].

§Department of Pathology, Stanford University, Stanford, CA, 94305.
††Department of Electrical and Computer Engineering, Virginia Polytechnic
Institute and State University, Arlington, VA 22203, USA.
‡‡Department of Computer Science of Purdue University, West Lafayette, IN
47907, USA.
†The Bradley Department of Electrical and Computer Engineering, Virginia
Tech
‡School of Electrical Engineering and Computer Science, Oregon State
University, Corvallis, OR, 97331.
∥School of Computer Science & Engineering, University of Washington,
Seattle, WA, 98105.
∗Computer Science Department, Rensselaer Polytechnic Institute, Troy, NY,
12180.
∗∗Computer and Information Science Department, Fordham University, New
York City, NY, 10023.
¶Corresponding author.
E-mails: wenqiwei@fordham.edu.

Manuscript received xxxx xx, xxxx; revised xxxxx xx, xxxx.

it

Nonetheless,

is important

to recognize that machine
learning does not invariably resolve problems or yield the
optimal solution. Despite artificial
intelligence is currently
experiencing a golden age, numerous challenges persist in
the development and application of machine learning technol-
ogy [4]. As the field continues to advance, addressing these
obstacles will be essential for unlocking the full potential of
machine learning and its transformative impact on various
industries.

The process of collecting and annotating data is both time-
consuming and expensive [5], giving rise to numerous issues.
As machine learning is heavily dependent on data, some of
the key hurdles and challenges it faces include:

• Data quality. Ensuring data quality is one of the most
significant challenges confronting machine learning profes-
sionals. When data is of subpar quality, models may generate
incorrect or imprecise predictions due to confusion and
misinterpretation [6] [7].

• Data scarcity. A considerable portion of the contemporary
AI dilemma stems from inadequate data availability: either
the number of accessible datasets is insufficient, or manual
labeling is excessively costly [8].

• Data privacy and fairness. There are many areas in which
datasets cannot be publicly released due to privacy ad fair
issues. In these cases, generating synthetic data can be very
useful, and we will investigate ways of creating anonymized
datasets with differential privacy protections.

Tackling these issues is crucial to fully realizing the transfor-
mative power of machine learning across diverse sectors [9]–
[11]. Generally, synthetic data are defined as the artificially
annotated information generated by computer algorithms or
simulations [4], [12]. In many cases, synthetic data is nec-
essary when real data is either unavailable or must be kept
private due to privacy or compliance risks [10], [13], [14].
This technology is extensively utilized in various sectors, such
as healthcare, business, manufacturing, and agriculture, with
demand growing at an exponential rate [15].

The objective of this paper is to offer a high-level overview
of several state-of-the-art approaches currently being inves-
tigated by machine learning researchers for synthetic data
generation. For the reader’s convenience, we summarize the
paper’s main contributions as follows:

• We present pertinent ideas and background information
on synthetic data, serving as a guide for researchers
interested in this domain.

• We explore different real-world application domains and

---

<!-- PAGE 2 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

2

Fig. 1. Synthetic data generation.

emphasize the range of opportunities that GANs and
synthetic data generation can provide in bridging gaps
(Section II).

• We examine a diverse array of deep generative mod-
els dedicated to generating high-quality synthetic data,
present advanced generative models, and outline potential
avenues for future research (Section III).

• We address privacy and fairness concerns, as sensitive
information can be inferred from synthesized data, and
biases embedded in real-world data can be inherited.
We review current technological advancements and their
limitations in safeguarding data privacy and ensuring the
fairness of synthesized data (Section IV and V).

• We outline several general evaluation strategies to assess

the quality of synthetic data (Section VI).

• We identify challenges faced in generating synthetic data
and during the deployment process, highlighting poten-
tial future work that could further enhance functionality
(Section VII).

II. APPLICATION

Synthetic data offers a multitude of compelling advantages,
making it a highly appealing option for a wide range of
applications. By streamlining the processes of training, testing,
and deploying AI solutions, synthetic data facilitates more
efficient and effective development. Furthermore, this cutting-
edge technology reduces the risk of exposing sensitive infor-
mation, thereby ensuring customer security and privacy [4].

As researchers transition synthetic data from the lab to prac-
tical implementations, its real-world applications continue to
broaden. This section explores several notable domains where
synthetic data generation substantially impacts addressing real-
world challenges.

A. Vision

Supervised learning relies heavily on the availability of la-
beled data [51]. However, in many applications, particularly in
computer vision, manual labeling is often necessary [52], [53].
Tasks such as segmentation, depth estimation, and optical flow
estimation can be exceedingly challenging to label manually.
Synthetic data has emerged as a transformative solution in this
context, significantly improving the labeling process [54].

Sankaranarayanan et al. introduced a generative adversarial
network (GAN) that narrows the gap between embeddings in
the learned feature space, facilitating Visual Domain Adap-
tation [55]. This approach enables semantic segmentation
across different domains. The GAN uses a generator to project
features onto the image space, which the discriminator subse-
quently operates on. Adversarial losses can be derived from
the discriminator’s output [56]. Notably, applying adversarial
losses to the projected image space has been shown to yield
significantly better performance compared to applying them
directly to the feature space [55].

In a recent study, a Microsoft research team demonstrated
the effectiveness of synthetic data in face-related tasks by
combining a parametric 3D face model with an extensive
library of hand-crafted assets [57]. This approach rendered
training images with remarkable realism and diversity. The
researchers trained machine learning systems for tasks such
as landmark localization and face parsing using synthetic
data, showing that it can achieve comparable accuracy to real
data. Furthermore, synthetic data alone proved sufficient for
detecting faces in unconstrained settings [57].

B. Voice

The field of synthetic voice is at the forefront of tech-
nological advancement, and its evolution is happening at a
breakneck pace. With the advent of machine learning and
deep learning, creating synthetic voices for various applica-
tions such as video production, digital assistants, and video
games [58] has become easier and more accurate. This field
is an intersection of diverse disciplines, including acoustics,
linguistics, and signal processing. Researchers in this area
continuously strive to improve synthetic voices’ accuracy and
naturalness. As technology advances, we can expect to see
synthetic voices become even more prevalent in our daily lives,
assisting us in various ways and enriching our experiences in
many fields [59].

The earlier study includes spectral modeling for statis-
in which low-level, un-
tical parametric speech synthesis,
transformed spectral envelope parameters are used for voice
synthesis. The low-level spectral envelopes are represented
by graphical models incorporating multiple hidden variables,
such as restricted Boltzmann machines and deep belief
networks (DBNs) [60]. The proposed conventional hidden

---

<!-- PAGE 3 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

3

TABLE I
SUMMARIZATION OF REPRESENTATIVE WORKS IN SYNTHETIC DATA GENERATION.

Paper
MedGAN [16]

Application
healthcare

Generative AI
GAN

MMCGAN [17]
DeepSynth [18]
ChemSpaceE [19]
JTVAE [21]
REINVENT [22]
CORE [23]
RGA [24]
CorGAN [26]

healthcare & CV
healthcare & CV
drug
drug
drug
drug
drug
healthcare

GAN
GAN
VAE
VAE
RL
VAE
RL
GAN

DNN
MLP

CNN
CNN
GNN
GNN
RNN
GNN
geometric NN
CNN

DAAE [27]

healthcare

VAE+GAN

recurrent autoencoder

HAPNEST [28]

healthcare

synthpop [29]
CycleGAN [30]
DP-CGAN [31]
BigGANs [32]
VideoDiff [33]
VQ-VAE [34]
GIRAFFE [35]

Wavegrad [36]
TTS-GAN [37]
Seq-GAN [38]
BLEURT [39]
TextGen-RL [40]
SynBench [41]
RelGAN [42]
DPGM [43]

healthcare
vision
vision
vision
vision
vision
vision

TTS
TTS
NLP
NLP
NLP
NLP
image and text
audio and text

WaveGAN [44]
Wavenet [45]

audio
audio

Stutter-TTS [46]

audio

Quant GANs [47]

business

CGAN [48]

business

PATE-GAN [49]

business

approximate Bayesian compu-
tation (not deep learning)
proper synthesis
GAN
GAN
GAN
diffusion
VAE
GAN

diffusion
GAN
GAN+RL
Language model
RL
conditional Gaussian mixture
GAN
generative artificial neural net-
works
GAN
GAN

phonetic encoder and the de-
coder
GAN

GAN

GAN

CollGAN [50]

physics
collision)

(particle

VAE/GAN

NA (w.o. DNN)

Statistical hypothesis testing
CNN
deep CGAN
large scale GAN
CNN
PixelCNN
CNN

gradient-based sampling
auto-regressive model
CNN
BERT
LSTM

CNN
differentially private kernel k-
means
DCGAN
LSTM

CNN

MLP+ Temporal
tional networks(TCN)
CNN

convolu-

Aggregation

Private
Teacher Ensembles (PATE)
MLP

of

health

(Electronic

Dataset
MIMIC/Sutter
record)
chest CT images
rat kidney tissue (microscope image)
ZINC (drug molecule) [20]
ZINC (drug molecules) [20]
ZINC (drug molecules) [20]
ZINC (drug molecule) [20]
ZINC and TDC [25]
MIMIC-III dataset, UCI Epileptic
Seizure Recognition dataset
MIMIC-III, UT Physicians clinical
databases
Genomes Project and HGDP datasets

SD2011
pix2pix
MNIST
ImageNet
BAIR Robot Pushing, Kinetics-600
ImageNet
CompCars, LSUN Churches, and
FFHQ
LJ Speech
Tacotron2
Nottingham dataset
WebNLG Competition dataset

anonymized Call Detail

CIFAR10
COCO Image Captions dataset
MNIST,
Record (CDR)
Speech Commands Dataset
CSTR voice corpula (multi-channel
English audio)
recordings

simulated data

Vector autoregressive (VAR) time se-
ries
Kaggle

ATLAS

Markov model (HMM)-based speech synthesis system can
be significantly improved in terms of naturalness and over-
smoothing [61].

Synthetic data can also be applied to Text-to-Speech (TTS)
to achieve near-human naturalness [62], [63]. As an alternative
to sparse or limited data, synthetic speech (SynthASR) was
developed for automatic speech recognition. The combination
of weighted multi-style training, data augmentation, encoder
freezing, and parameter regularization is also employed to
address catastrophic forgetting. Using this novel model, the
researchers were able to apply state-of-the-art techniques to
train a wide range of end-to-end (E2E) automatic speech
recognition (ASR) models while reducing the need for pro-
duction data and the costs associated with it [62].

C. Natural Language Processing (NLP)

The increasing interest in synthetic data has spurred the
development of a wide array of deep generative models in

the field of natural language processing (NLP) [51]. In recent
years, a multitude of methods and models have illustrated
the capabilities of machine learning in categorizing, routing,
filtering, and searching for relevant information across various
domains [64].

Despite these advancements, challenges remain. For exam-
ple, the meaning of words and phrases can change depending
on their context, and homonyms with distinct definitions can
pose additional difficulties [65]. To tackle these challenges, the
BLEURT model was proposed, which models human judg-
ments using a limited number of potentially biased training
examples based on BERT. The researchers employed millions
of synthetic examples to develop an innovative pre-training
scheme, bolstering the model’s ability to generalize [66],
[67]. Experimental results indicate that BLEURT surpasses its
counterparts on both the WebNLG Competition dataset and
the WMT Metrics, highlighting its efficacy in NLP tasks [39].
Another significant breakthrough in text generation using
GANs is RelGAN, developed by Rice University. This model

---

<!-- PAGE 4 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

4

essentially molecular structures with desirable pharmaceutical
properties. The goal of de novo drug design is to produce novel
and desirable molecule structures from scratch. The word
“de novo” means from the beginning. The whole molecule
space is around 1060 [25], [76], [77]. Most of the existing
methods rely heavily on brute-force enumeration and are
computationally prohibitive. Generative models are able to
learn the distribution of drug molecules from the existing drug
database and then draw novel samples (i.e., drug molecules)
from the learned molecule distribution, including variational
autoencoder (VAE) [21], [78], [79], generative adversarial
network (GAN) [80], energy-based model (EBM) [81], [82],
diffusion model [83], reinforcement learning (RL) [22], [24],
[84], genetic algorithm [85], sampling-based methods [86],
[87], etc.

In healthcare, patient information is often stored in elec-
tronic health records (EHR) format [88]–[90]. Research in
medicine has been greatly facilitated by the availability of in-
formation from electronic health records [91], [92]. MedGAN,
an adversarial network model for generating realistic syn-
thetic patient records, has been proposed by Edward Choi
and other colleagues. With the help of an autoencoder and
generative adversarial networks, medGAN can generate high-
dimensional discrete variables (e.g., binary and count features)
based on real patient records [16]. Based on their evalua-
tions of medGAN’s performance on a set of diverse tasks
reported, including reporting distribution statistics, classifica-
tion performance [93], and expert review, medGAN exhibits
close-to-real-time performance [16], [94]–[97]. Using syn-
thetic data can help reduce the regulatory barriers preventing
the widespread sharing and integration of patient data across
multiple organizations in the past [98], [99]. Researchers
across the globe would be able to request access to synthetic
data from an institution to conduct their own research using
the data. Such capabilities can increase both the efficiency and
scope of the study as well as reduce the likelihood of biases
being introduced into the results [70], [100], [101].

E. Business

The inherent risk of compromising or exposing original
data persists as long as it remains in use, particularly in the
business sector, where data sharing is heavily constrained both
within and outside the organization [102]. Consequently, it is
crucial to explore methods for generating financial datasets
that emulate the properties of ”real data” while maintaining
the privacy of the involved parties [102].

Efforts have been made to secure original data using
technologies like encryption, anonymization, and cutting-edge
privacy preservation [103]. However,
information gleaned
from the data may still be employed to trace individuals,
thereby posing the risk [104]. A notable advantage of synthetic
data lies in its ability to eliminate the exposure of critical
data, thus ensuring privacy and security for both companies
and their customers [105]. Moreover, synthetic data enables
organizations to access data more rapidly, as it bypasses
privacy and security protocols [106]. In the past, institutions
possessing extensive data repositories could potentially assist

Fig. 2. Synthetic data applications

is comprised of three main components: a relational memory-
based generator, a Gumbel-Softmax relaxation algorithm, and
multiple embedded representations within the discriminator.
When benchmarked against several cutting-edge models, Rel-
GAN demonstrates superior performance in terms of sampling
quality and diversity. This showcases its potential for further
investigation and application in a wide range of NLP tasks
and challenges [42], [68].

D. Healthcare

In order to protect health information and improve repro-
ducibility in research, synthetic data has drawn mainstream
attention in the healthcare industry [69], [70]. Many labs
and companies have harnessed the tools of big data and
advanced computation tools to produce large quantities of
synthetic data, or digital twin [71], [72]. Modeled after patient
data, synthetic data generation is essential to understanding
diseases while maintaining patient confidentiality and privacy
simultaneously [73]. Theoretically, synthetic data can reflect
the original distribution of the data instead of revealing actual
patient data [73]–[75].

Synthetic data generation can also be utilized to discover
new scientific principles by grounding it in biological pri-
ors [69]. There have been a good number of models and
software developed, such as SynSys, which uses hidden
Markov models and regression models initially trained on real
datasets to generate synthetic time series data consisting of
nested sequences [70]; and corGAN, in which synthetic data is
generated by capturing correlations between adjacent medical
features in the data representation space [26].

Synthetic data generation has also been widely used in drug
discovery, especially de novo drug molecular design. Drugs are

---

<!-- PAGE 5 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

5

decision-makers in resolving a broad spectrum of issues.
However, accessing such data, even for internal purposes, was
hindered by confidentiality concerns. Presently, companies are
harnessing synthetic data to refresh and model original data,
generating continuous insights that contribute to enhancing the
organization’s performance [4].

F. Education

Synthetic data is gaining increasing attention in the field of
education due to its vast potential for research and teaching.
Synthetic data refers to computer-generated information that
mimics the properties of real-world data without disclosing
any personally identifiable information [107]. This approach
proves instrumental for educational settings, where ethical
the use of real-world student data.
constraints often limit
Therefore, synthetic data offers a robust solution for privacy-
concerned data sharing and analysis, enabling the creation
of accurate models and strategies to improve the teaching-
learning process.

A detailed example of synthetic data usage in education is
the simulation of student performance data to aid in designing
teaching strategies. Suppose an educational researcher wants
to investigate the impact of teaching styles on student per-
formance across different backgrounds and learning abilities.
However, obtaining real student data for such studies can be
ethically complex and potentially intrusive. In such a situation,
synthetic data can be generated that mirrors the demographic
learning patterns, and likely performance of
distributions,
a typical student population. This data can then be used
to model the effects of various teaching strategies without
compromising student privacy [108].

Furthermore, synthetic data can be a powerful tool in teacher
training programs. For example, teacher candidates can use
synthetic student data to practice data-driven instructional
strategies, including differentiated instruction and personalized
learning plans. They can analyze this synthetic data, identify
patterns, determine student needs, and adjust their instructional
plans accordingly. By using synthetic data, teacher candidates
gain practical experience in analyzing student data and adapt-
ing their teaching without infringing on the privacy of actual
students [109]. Thus, synthetic data serves as a valuable bridge
between theory and practice in education, driving innovation
while safeguarding privacy.

introduces an N-gram-based method to predict the following
position based on previous positions for publishing trajectory.
They exploit the prefix tree to describe the n-gram model while
combining it with differential privacy [114]. [115] extends the
n-gram model with local differential privacy and [116] further
replaces the n-gram model with key movement mobility for
differentially private trajectory generation. By comparison,
[117] proposes a synthetic trajectory strategy based on the
discretization of raw trajectories using hierarchical reference
systems to capture individual movements at differing speeds.
Their method adaptively selects a small set of reference
systems and constructs prefix tree counts with differential
privacy. Applying direction-weighted sampling, the decrease in
tree nodes reduces the amount of added noise and improves the
utility of the synthetic data. [118] constructs the differentially
private prefix tree and calibrates original trajectories against a
selection of anchor points. By extracting multiple differential
private distributions with redundant information [119], [120],
the authors generate a new trajectory with samples from these
distributions. By comparison, [121] estimates various distri-
butions of an attribute set to determine trajectories and [122]
consider the interactions between different attributes by group-
ing strongly correlated attributes into non-disjoint sets and
constructing a corresponding distribution for each set.

In addition to differential privacy, Bindschaedler and
Shokri [123] enforce plausible deniability to generate privacy-
preserving synthetic traces. It first introduces trace similarity
and intersection functions that map a fake trace to a real hint
under similarity and intersection constraints. Then, it generates
one fake trace by clustering the locations and replacing the
trajectory locations with those from the same group. If the
fake trace satisfies plausible deniability, i.e., there exist k other
real traces that can map to the fake trace, then it preserves the
privacy of the seed trace. While existing studies mainly use the
Markov chain model, [124] proposes PrivTrace, which controls
the space and time overhead by the first-order Markov chain
model and achieves good accuracy for next-step prediction
by the second-order Markov chain model. [125] considers the
location synthesizer that generates location traces, including
co-locations of friends, while offering node-level differential
privacy for the friendship and user-level differential privacy
for the co-location count matrix.

G. Location and Trajectory Generation

H. AI-Generated Content (AIGC)

Location and trajectory are a particular form of data that
could highly reflect users’ daily lives, habits, home addresses,
workplaces, etc. To protect location privacy, synthetic location
generation is introduced as opposed to location perturba-
tion [110]. The main challenge of generating synthetic location
and trajectory data is to resemble genuine user-produced data
while offering practical privacy protection simultaneously. One
approach to generating the location and trajectory data is
to inject a synthetic point-based site within a user’s trajec-
tory [111], [112].

Synthetic trajectory generation is frequently combined with
privacy-enhancing techniques to further prevent sensitive infer-
ence from the synthesized data. For example, Chen et al. [113]

AI-Generated Content (AIGC) stands at the forefront of
the technology and content creation industry, changing the
dynamics of content production. A typical example of AIGC is
OpenAI’s ChatGPT, an AI-driven platform generating human-
like text in response to prompts or questions. It leverages a vast
corpus of internet text to generate detailed responses, often
indistinguishable from those a human writer would produce.
This capacity extends beyond simple question-answer pairs to
crafting whole articles, stories, or technical explanations on a
wide range of topics, thus creating a novel way of producing
blog posts, articles, social media content, etc [126], [127].

Google’s Project Bard focuses more on the creative aspects
of text generation. It is designed to generate interactive fiction

---

<!-- PAGE 6 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

6

and assist in storytelling. Users can engage in an interactive
dialogue with the model, directing the course of a narrative by
providing prompts that the AI responds to, thus co-creating a
story. This opens up fascinating possibilities for interactive
entertainment and digital storytelling [128].

An innovative application of AIGC is in the field of news
reporting. News agencies increasingly use AI systems, such
as the GPT series, to generate news content. For instance,
the Associated Press uses AI to generate news articles about
corporate earnings automatically. The AI takes structured
data about company earnings and transforms it into a brief,
coherent, and accurate news report. This automation allows
the agency to cover many companies that would be possible
with human journalists alone [129].

Additionally, AIGC has found its place in the creative
domain, with AI systems being used to generate book de-
scriptions, plot outlines, and even full chapters of novels.
For instance, a novelist could use ChatGPT to generate a
synopsis for their upcoming book based on a few keywords
or prompts related to the story. Similarly, marketing teams
utilize AI to create compelling product descriptions for online
marketplaces [130]. This increases efficiency and provides a
level of uniformity and scalability that would be challenging
to achieve with human writers alone. Looking forward, AIGC
is profoundly impacting the landscape of content creation and
will continue to shape it in the future [128].

I. Finance

Synthetic data generation offers significant benefits for the
finance industry [104], as detailed below. First, financial data
is highly sensitive and subject to stringent privacy regula-
tions [131]. Synthetic data mimics real data without exposing
actual customer information, enabling institutions to comply
with privacy laws while still utilizing detailed datasets for
analysis and development. Second, synthetic data can be used
to test and validate financial algorithms and models under
various conditions. For example, trading algorithms can be
tested using synthetic market data to evaluate their perfor-
including rare or
mance under different market scenarios,
extreme events that may not be present in historical data [132].
Third, developing and testing financial algorithms requires
large volumes of high-quality data. Synthetic data provides an
endless supply of training data, enabling thorough backtesting
of trading strategies and machine learning models without the
risk of overfitting historical data [133].

Synthetic data generation also transforms the financial ser-
vices industry by enabling more accurate risk assessments and
fraud detection [104]. Synthetic data generation can identify
anomalies and potential risks by simulating financial trans-
actions and market behaviors, allowing financial institutions
to implement more effective fraud prevention measures and
develop more resilient financial strategies. Furthermore, syn-
thetic data generation can support compliance with regulatory
requirements by providing detailed, real-time reporting and
analysis of financial activities [47]. In the context of human
resources, synthetic data generations can model workforce
dynamics, including employee performance, engagement, and

turnover. By analyzing these models, businesses can develop
strategies to improve employee satisfaction, enhance produc-
tivity, and reduce turnover rates. For example, synthetic data
generation can simulate the impact of various HR policies on
workforce morale and performance, helping HR departments
to implement the most effective practices.

J. Other Applications

The techniques for synthetic data generation described in
this paper have far-reaching implications beyond the specific
domains covered. Here are some notable applications:
• Retail and Marketing: In retail, synthetic data can model
customer interactions, purchasing behaviors, and inventory
management [134]. This aids in developing personalized
marketing strategies, optimizing supply chains, and im-
proving customer service without infringing on individual
privacy.

• Environmental Studies: Synthetic data can simulate en-
vironmental conditions, weather patterns, and ecological
interactions [135]. This is particularly useful for studying
climate change, biodiversity, and conservation efforts, al-
lowing researchers to test hypotheses and model practical
scenarios without the constraints of limited real-world data.
• Urban Planning and Development: In urban planning, syn-
thetic data can be used to simulate population growth, traffic
flows, and infrastructure development [136]. This helps city
planners and developers make informed decisions about
resource allocation, transportation systems, and sustainable
development initiatives.

• Software Development and Testing: In software develop-
ment, synthetic code generation can simulate various coding
scenarios, bug patterns, and software behaviors [137]. This
is particularly useful for testing and debugging, as it allows
developers to identify and fix potential issues without the
constraints of existing codebases. Synthetic code can also
aid in developing personalized coding assistants, optimiz-
ing software performance, and improving the reliability of
code releases [138]. Additionally, by generating diverse and
extensive code samples, developers can enhance machine
learning models for code completion and error detection,
ultimately leading to more efficient and robust software
development processes.

III. GENERATIVE AI
Generative AI models refer to a wide class of AI methods
that could learn the data distribution from existing data objects
and generate novel structured data objects, which fall into
the category of unsupervised learning. Generative AI models,
also known as deep generative models, or distribution learning
methods, learn the data distribution and samples from the
learned distribution to produce novel data objects. In this
section, we investigate several generative AI models that
are frequently used in synthetic data generation, including
the language model in Section III-A, variational autoencoder
(VAE) in Section III-C, generative adversarial network (GAN)
in Section III-D, reinforcement learning (RL) in Section III-E,
and diffusion model in Section III-F. Table II compares various
generative AI methods from several aspects.

---

<!-- PAGE 7 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

7

TABLE II
COMPARISON OF ALL THE GENERATIVE AI METHODS FROM DIFFERENT ASPECTS.

Method

Supervision

NN Architecture

MLE

With latent
variable

Language model (LM)
self-supervised learning (SSL)
variational autoencoder (VAE)
generative adversarial network (GAN)
diffusion (score-based model) model
reinforcement learning (RL)

no
no
no
no
no
yes

autoregressive model
encoder (representation)
encoder-decoder
generator & discriminator
representation
policy
network

network

or Q-

yes
yes
yes
yes
yes
no

no
no
yes
yes
no
no

Paper

[139]

[140]
[141], [142]
[143]
[144]

A. Language Model

The language model was originally designed to model
natural language. It is able to learn structured knowledge from
massive unlabelled sequence data. Specifically, suppose the
sequence has N tokens, denoted X = [x1, · · · , xN ], then the
probability distribution of the sequence can be decomposed as
the product of a series of conditional probabilities,

p(X) = p(cid:0)[x1, · · · , xN ](cid:1) =

N
(cid:89)

i=1

p(xi|x1, · · · , xi−1),

(1)

where a single conditional probability p(xi|x1, · · · , xi−1)
denote the probability of the token xi given all the tokens
before xi. The conditional probability can be modeled by
the recurrent neural network (RNN). The language model
can be used to generate all types of sequence data, such as
natural language [139], electronic health records [145], etc.
The language model can be combined with other deep learning
models, such as variational autoencoder (VAE) and generative
adversarial network (GAN), which will be described later.

B. Self-Supervised Learning (SSL)

Labeled data are expensive to acquire so the number of
available labeled data is usually limited. To address this issue,
self-supervised learning (SSL) was proposed. This learning
paradigm curates the supervision signal from the data itself.
It is parallel to supervised learning and unsupervised learning.
Different from supervised learning, self-supervised learning
can learn from massive unlabeled data. Self-supervised learn-
ing is usually used as a pretraining strategy to learn the
representation from massive unlabelled data [146]. The core
idea of self-supervised learning is to mask a subset of the raw
data feature and build a machine learning model to predict
the masked data. then the pre-trained machine learning model
(usually a neural network) is used as a “warm start”, and is
furtherly finetuned for the downstream applications.

C. Variational Autoencoder (VAE)

Variational autoencoder (VAE) [140] employs a continuous
latent variable to characterize the data distribution. Specifi-
cally, it contains two neural network modules: encoder and
decoder. The objective of the encoder is to convert the data
object into a continuous latent variable. Then decoder takes
the latent variable as the input feature and reconstructs the
data object.

Formally, suppose the data object is denoted x, the latent
variable is a d-dimensional real-valued vector z, the encoder
is p(z|x), and the decoder is q(x|z). The learning objective
contains two parts: (1) reconstruct the data object x and (2)
encourage the distribution of latent variables to be close to the
normal distribution.

The Kullback-Leibler (KL) divergence measures the differ-
ence between two probability distributions. Given two prob-
ability distributions p1(x) and p2(x) on the same continuous
domain, KL divergence between them is formally defined as

KL(p1||p2) =

=

(cid:90)

x
(cid:90)

x

log p(x) = log

p1(x) log

p1(x)
p2(x)

dx

p1(x)(cid:2) log p1(x) − log p2(x)(cid:3)dx.
(cid:90)

p(z)p(x|z)dz
(cid:2) log p(x|z)(cid:3) − DKL(q(z|x)||p(z))

z
≥ Eq(z|x)
≜ ELBO.

where p(z) is the normal distribution and is used as the
prior distribution. VAE encourages the distribution of latent
variables to be close to normal distribution. Then during
the inference phase, we sample latent variables from the
normal distribution and generate the novel data objects. There
are several VAE variants, such as disentangled VAE [147],
hierarchical VAE [148], and sequence VAE [78].

D. Generative Adversarial Network (GAN)

Generative adversarial network (GAN) [141], [149], [150]
formulates the generation problem into a supervised learning
task. Specifically, it comprises two neural network modules:
discriminator and generator. The objective of the generator is
to generate data that are close to the real data, By comparison,
the objective of the discriminator is to discriminate the fake
data (generated by the generator) from the real ones. It
performs a binary classification task, where the real data from
the training set are regarded as the positive samples;
the
generated data (by generator) are regarded as the negative
samples. generator and discriminator are trained in a mini-
max manner.

---

<!-- PAGE 8 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

8

Formally, the generator is denoted G(z), and the discrim-
inator predicts a probabilistic score for a data object and is
denoted D(x). The learning objective is formulated as

min
G

max
D

L(D, G) = Ex∼training set[log D(x)]
(cid:2) log(1 − D(G(z))(cid:3),

+Ez∼p(z)

(2)

The objective function is not differentiable with parameter θ.
We use policy gradient to obtain an unbiased estimator of
the objective gradient ∇θL(θ) [144] and then use stochastic
optimization methods to maximize the expected reward. Gen-
erating synthesis data can be viewed as sequential decision-
making by sequentially generating one basic structure.

where z is the latent variable and is drawn from the normal
distribution p(z) to enhance the diversity of the generated data
objects.

When learning GAN, the generator and discriminator are

optimized alternatively.

• optimize generator and fix discriminator: the objective

function becomes

min L(G) = Ez∼p(z)

(cid:2) log(1 − D(G(z))(cid:3),

(3)

where the generator is optimized to generate data that is
close to the real data (with higher discriminator’s scores).
• optimize discriminator and fix generator: the objective

function reduces to a binary classification problem,

max L(D) = Ex∼training set[log D(x)]
(cid:2) log(1 − D(G(z))(cid:3),

+Ez∼p(z)

(4)

which can be seen as a cross-entropy loss function, where
the real data objects from the training set are seen as
positive samples while the synthetic data objects G(z)
are seen as negative samples.

Then we discuss a popular variant of GAN. The Wasserstein
Generative Adversarial Network (W-GAN) was proposed in
2017 and aims to enhance the stability of learning, accelerate
the training process, and get rid of problems like mode
collapse [151].

E. Reinforcement Learning (RL)

Reinforcement

learning (RL) focuses on addressing se-
quential decision-making problems [152]. It can be used in
synthesis data generation by growing a basic component at
one time and generating data objects sequentially. It formulates
sequential decision-making as a Markov decision process
(MDP) [144]. Markov decision process assumes that given the
current state, the future state of the stochastic process does not
depend on the historical states. Suppose the state at the time
t is xt, Markov decision process satisfies

p(xt+1|xt, xt−1, xt−2, ...) = p(xt+1|xt).

(5)

At the time t, given the state xt, the RL agent would generate
an action at from action space, which is denoted pθ(at|st), θ
is the parameter of the RL agent. After performing the action,
the system would jump into the next state xt+1, i.e., xt+1 =
f (xt, at). At the same time, the system would receive the
reward r(xt) from the environment, where r(·) is called the
reward function. The goal is to learn an agent that can receive
the maximal expected reward in total.

F. Diffusion Model

The diffusion model, also known as the score-based model
or score matching method, was proposed in recent years [143]
and is widely validated in many generative AI problems such
as speech synthesis [36].

Diffusion models

Specifically, suppose the data object is x, and the likelihood
function is denoted p(x). We are interested in estimating the
gradient of the logarithm of the likelihood function.
[153],

[154] are inspired by non-
equilibrium thermodynamics and can be split into the forward
and backward diffusion processes. During the forward diffu-
sion process, diffusion models will gradually add Gaussian
noise to the data, and the last-step data will follow an isotropic
Gaussian. The reverse diffusion process will revert such a
process and construct the data from noise distribution.

More rigorously, we can define the forward process as from
the actual data x0 ∼ p(x) to the random noise xT with T
diffusion steps. Let us first assume that for the forward process,
the Gaussian distribution is

q(xt|xt−1) = N (xt; (cid:112)1 − βtxt−1, βtI),
where βt ∈ (0, 1). Then, the corresponding backward process
is

pθ(xt−1|xt)

=N (xt−1; µθ(xt, t), Σθ(xt, t))

=N (xt−1;

1
√
αt

(cid:0)xt −

βt√

1 − ¯αt

ϵ(cid:1),

1 − ¯αt−1
1 − ¯αt

βt),

where ϵ ∼ N (0, I) follows the standard Gaussian, αt = 1−βt,
and ¯αt = (cid:81)t

i=1 αi.

The objective of diffusion models is to estimate the vari-
ational lower bound (VLB) of the negative log-likelihood of
data distribution:

log p(x) ≥ −Eq(x1:T |x0)[log

q(x1:T |x0)
pθ(x0:T )

] = −LVLB.

The VLB can be rewritten as:
LVLB = KL[q(xT |x0)||pθ(xT )]
(cid:125)

(cid:124)

(cid:123)(cid:122)
LT

+

T
(cid:88)

t=2

KL[q(xt−1|xt, x0)||pθ(xt−1|xt)]
(cid:123)(cid:122)
(cid:125)
(cid:124)
Lt−1

−Eq[log pθ(x0|x1)]
(cid:123)(cid:122)
(cid:125)
(cid:124)
L0

.

Here LT is a constant and can be ignored, and diffusion
models [154] have been using a separate model for estimating
L0. For {Lt−1}T
t=2, we model a neural network to approximate
the conditionals during the reverse process, i.e.,, we want to
ϵ(cid:1). If we plug this
train µθ(xt, t) to predict
into the closed-form solution of the KL-divergence between
two multivariate Gaussian distributions, we will have the
following for t = 1, · · · , T − 1:

(cid:0)xt − βt√

1− ¯αt

1√

αt

arg max
θ

L(θ) =

∞
(cid:88)

t=1

Epθ(at|xt)[r(xt)].

(6)

Lt = Ex0,z

(cid:104)
∥ϵt − ϵθ(

√

¯αtx0 +

√

1 − ¯αtϵt, t)∥2(cid:105)

.

---

<!-- PAGE 9 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

9

The diffusion model has achieved wide success in many
downstream synthetic problems [82], [155]–[157]. As a sum-
marization, Table II compares various generative AI methods
from several aspects.

G. Multimodal Learning

Multimodal data refers to datasets that integrate multiple
types of data, such as text, images, audio, and numerical
values. This type of data provides a comprehensive view by
combining different sources of information, which is crucial
for tasks requiring a holistic understanding of complex scenar-
ios. In fields like healthcare [158], finance, and autonomous
systems, multimodal data enables more accurate and robust
analysis and decision-making by leveraging the strengths of
each data type. For instance, in drug discovery, multimodal
data can combine genomic data, chemical structures, and
clinical outcomes to enhance the prediction of drug efficacy
and safety [95], [159].

Synthetic multimodal data generation involves creating ar-
tificial datasets that integrate multiple types of data, such as
text, images, audio, and numerical data, to simulate real-world
scenarios. This technique is particularly valuable in fields like
healthcare [16], finance [104], and education systems [109],
where data is often complex and heterogeneous.

Then, we review some cutting-edge techniques for synthetic
multimodal data generation. GANs can generate one type of
data from another, such as images from textual descriptions or
audio from images. This cross-modal generation capability is
essential for creating cohesive multimodal datasets [11]. Re-
cently, ChatGPT [129] supports multimodal data generation,
including image, text, and numerical features.

IV. PRIVACY RISKS AND PREVENTION
Open release and free data exchange would benefit research
and industry development. However, there are cases where
datasets exist but cannot be publicly disclosed due to privacy
concerns. Regulated data, such as clinical and genomics data
in raw form, may not be shared, and one solution is to share
synthesized data instead.

A. Privacy Risks in Data Synthesis

Due to the utility goal of data synthesis, the synthesized
data tends to preserve the distribution of the original data.
Therefore, the deployment of these models could be subject
to privacy leakage. For deep neural network-based approaches,
membership inference attack [160], [161] would identify if
an input
is in the training data or not and thus can be
used to determine how close the synthesized data is to the
original data. At the feature level, sensitive attributes such
as skin color can be inferred from the behavior of the deep
learning model [162], and even the single training instance
can be reconstructed [163]–[165]. For generative AI models,
the generative learning process and the high complexity of
the model jointly encourage a distribution that is concentrated
around training samples. By repeatedly sampling from the
distribution, there is a considerable chance of recovering the
training samples or attributes [166]–[172], or the membership
of the training data [173].

B. Privacy Protection in Data Synthesis

Solutions have been proposed in two broad categories. In the
first category, different data anonymization-based approaches
such as K-anonymity [209]–[211] and nearest marginal [212]
to sanitize data so that it cannot be easily re-identified. These
data anonymization approaches involve replacing sensitive
data with fictitious yet realistic data. It
is often used to
protect the data while maintaining its usability for testing or
development purposes. However, they often do not provide
rigorous privacy guarantees [14]. In the second category,
synthetic data generation approaches have been proposed to
generate realistic synthetic data using rigorous differential
privacy definitions [114], [174], [213] for various applications.
These approaches involves adding noise to the data to prevent
the identification of individuals in the dataset while preserving
the statistical properties of the data. This is particularly useful
in scenarios where data needs to be shared but individual
privacy must be maintained. In particular, Bindschaedler et
al. [174] introduced the idea of plausible deniability instead of
directly adding noise to the generative model. This mechanism
results in input indistinguishability that means by observing
the output set (i.e., synthetics) an adversary cannot make sure
whether a particular data record was in the input set (i.e., real
data). With the help of generative modeling, Acs et al. [43]
clusters the original datasets into k clusters with differentially
private kernel k-means and produce synthetic data for each
cluster. By comparison, Liu et al [205] introduce two-level
privacy-preserving synthetic data generation. At the data level,
a selection module is used to select the items which contribute
less to the user’s preference. At the item level, a synthetic item
generation module is developed to create the corresponding
synthetic item.

Taking advantage of the GAN, several methods are proposed
to generate synthetic data to get better effect [27], [49],
[176], [177], [183], [187], [188] which closely matches the
distribution of the source data than the hidden Markov model-
based approach [73], RBF based approach [194], Bayesian
network-based [204], and Auto-encoder based approach [14].
Xie et al [177] propose DPGAN by adding noise on the
gradient of the Wasserstein distance with respect to the training
data. This approach does not adopt the optimization strategy
to improve the training stability and convergence speed. To
address these problems, Zhang et al. [176] proposed dp-
GAN, a general private data publishing framework for rich
semantic data without
the requirement of tag information
compared to [183]. By comparison, Beaulieu-Jones et al. [183]
trained the discriminator under differentially private SGD,
which generates plausible individuals of clinical datasets.
Tseng and Wu [175] apply compressive privacy [214] for
CPGAN, which would generate compressing representations
that retain high utility. Jordon et al.
[49] modifies the
Private Aggregation of Teacher Ensembles (PATE) framework
and applies it to the discriminator of GANs. The proposed
approach perceives the discriminator as a classifier and utilizes
its output as knowledge such that the student learns from
noisy labels that are obtained through privately aggregating
the discriminator’ votes. This allows a tight bound on the

---

<!-- PAGE 10 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

10

TABLE III
SUMMARIZATION OF PRIVACY PREVENTION STRATEGIES IN SYNTHETIC DATA GENERATION.

Paper
[14]
[27]
[43]
[49]
[113]
[115]
[116]
[117]
[118]
[120]
[121]
[122]
[123]
[124]
[125]
[174]
[175]
[176]
[177]
[178]
[179]
[180]
[181]
[182]
[183]
[184]
[185]
[186]
[187]
[188]
[189]
[190]
[191]
[192]
[193]
[194]
[195]
[196]
[197]
[198]
[199]
[200]
[201]
[202]
[203]
[204]
[205]
[206]
[207]
[208]

Privacy-enhancing Techniques
differential privacy
differential privacy
differential privacy
differential privacy (PATE)
differential privacy
local differential privacy
local differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
plausible deniability
differential privacy
differential privacy
plausible deniability
compressive privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy (PATE)
local differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
differential privacy
data replacement and item regularizer
differential privacy
local differential privacy
differential privacy

Generative AI
autoencoder
VAE + GAN
generative artificial neural networks
GAN
n-gram
n-gram
Markov probabilistic model
Markov probabilistic model
Markov probabilistic model
Markov probabilistic model
distribution estimation
distribution estimation
Hidden Markov Models
Markov chain model
probabilistical transform
probabilistical transform
GAN
GAN
GAN
GAN
GAN
GAN
GAN
GAN
GAN
GAN
GAN
GAN
GAN
GAN
GAN
GAN
Maximum Mean Discrepancy
Maximum Mean Discrepancy
Markov random field
Markov random field
Probabilistic graphical models
Maximum Cardinality Matching
Bayesian network
Bayesian network
statistical database
statistical queries
statistical queries
Graduate Update Method
autoencoder
autoencoder
latent space projection
Langevin Markov chain Monte Carlo
Maximum Entropy estimation
Maximum Entropy estimation

DNN
autoencoder
recurrent autoencoder
kernel k-means
DNN
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
DNN
DNN
DNN
DNN
DNN
DNN
DNN
DNN
DNN
DNN
DNN
DNN
autoencoder
DNN
DNN
DNN
Hermite polynomial features
Random feature mean embeddings
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
NA (w.o. DNN)
A (w.o. DNN)
A (w.o. DNN)
NA (w.o. DNN)
autoencoder
autoencoder
MLP
Energy-based Model
NA (w.o. DNN)
NA (w.o. DNN)

Data Format
attribute
EHR
image and text
attribute
sequential/time series
trajectory
trajectory
trajectory
social media trajectory
trajectory
location
trajectory
trajectory
trajectory
trajectory
attribute
image
image
image and EHR
image
image
attribute (tabular) and graph
image and EHR
time series
attribute
attribute (tabular)
image
image
attribute
trajectory
image
spatial point
attribute (tabular) and image
image
attribute
attribute
attribute
attribute (tabular)
attribute
attribute
attribute
attribute
attribute
attribute
image and attribute
text/image QA and attribute
attributes
image
attribute
attribute

influence of any individual sample on the model, resulting
in tight differential privacy guarantees and thus an improved
performance over models for data synthesis. By comparison,
Long et at. [189] applies teacher-student-based differential
privacy to the generator. While most of these approaches inject
noise into the energy function, a differentially private GAN
called GANobfuscator [178] achieve differential privacy by
adding noise within the training procedure.

GAN for synthetic spatial point generation. Apart from LDP
in distributed setting, Triastcyn and Faltings [179] propose
federated generative privacy that utilizes insufficient local data
from multiple clients to train a GAN. The method shares only
generators that do not come directly into contact with data
and the discriminator remain private. This model can output
artificial data, not belonging to any real user in particular, but
coming from the common cross-user data distribution.

While centralized differential privacy assumes data aggrega-
tors are reliable, local differential privacy (LDP) [213] assumes
that aggregators cannot be trusted and relies on data providers
to perturb their own data and is used to generate private
synthetic datasets that is similar to the private dataset. [207]
is inspired by PriView [208] but for computing any k-way
marginals under the LDP setting for the marginal table release
problem. Furthermore, [190] considers DP at label-level on

These privacy-preserving data synthesis methods mainly
aim at structured data like tables, which cannot be applied
to high dimensionality and complexity. To solve this problem,
PriView [208] constructs the private k-way marginal tables
for k ≥ 3 by first extracting low-dimensional marginal views
from the flat data and adding noise to the views and then
applying a reprocessing technique to ensure the consistency
of the noisy views. [215]–[218] leverage copula functions for

---

<!-- PAGE 11 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

11

multi-dimensional differentially private synthesization. Zhang
et al. [198] consider repetitive perturbation of the original
data as a substitute to the original data with a synthetic
data generation technique called PrivBayes. PrivBayes decom-
poses high dimensional data into low dimensional marginals
by constructing a Bayesian network and injects noise into
these learned low dimensional marginals to ensure differential
privacy and the synthetic data is inferred from these noised
marginals. Instead of the Bayesian network, differentially
private auto-encoder [14] significantly improves the effec-
tiveness of differentially private synthetic data release. [199]
applies data cleaning method [219] to fix the violations on
the structure of the data in the synthetic data. Instead of
using graphical models as the summarization/representation
of a dataset [14], [174], [176], [200], [201], [202] proposes to
use a set of large number of low-degree marginals to represent
a dataset. The advantage of this approach is that it makes
weak assumptions about the conditional independence among
attributes, and simply tries to capture correlation relationships
that are in the dataset. Meanwhile, the method is especially
attractive under differential privacy for its straightforward
sensitivity measurement, reduced noise variance, and efficient
privacy cost. [191] leverages the Hermite polynomial features
to encapsulate a higher degree of information within a smaller
order of feature. [193] constructs a graph that explore pairwise
dependence between attributes and applies the junction tree
algorithm to obtain the Markov random field (MRF), from
which the noisy marginals are generated and the synthetic data
are sampled.

While private synthetic data generation algorithms are
agnostic to downstream tasks, it is important to meet the
utility requirements for downstream use. [220] proposes post-
processing via resampling from the synthetic data to filter out
samples that do not meet the selected utility measures, thus
improving the utility of synthetic data.

C. Privacy Threats in Foundation Models

Entering the era of foundation models, recent research has
demonstrated that training data can be exposed from large lan-
guage models [221] as well as stable diffusion [222]. In both
types of models, attackers can generate sequences from the
trained model and identify those memorized from the training
set. Studies have shown that a sequence that appears multiple
times in the training data is more likely to be generated
than a sequence that occurred only once [157], [223], [224].
Accordingly, Kandpal et al [225] propose to deduplicate the
training data that appears multiple times such that the privacy
risks in language models is mitigated. [226] is the first work to
enforce privacy using differentially private stochastic gradient
descent (DP-SGD) in diffusion models. Several attempts has
been made to reduces the noise in the gradient during DP-
SGD training and improves the generative quality in diffusion
models, via semantic-aware pretraining [227], [228], latent
information [229], and retrieval-augmented generation [230].
In the meantime, differential privacy has been heavily invested
in privacy protection of large language models [231].

Given that we are still at

the very early stage of the
generative foundational models, the potential of the foundation

models for data synthesis has not been fully explored. While
more possible privacy threats on the foundation models are yet
to be discovered, existing privacy measures may be inadequate
to meet its demands of privacy. Further investigation is needed
to design countermeasures that would mitigate the memoriza-
tion and generalization problems for privacy protection.

V. FAIRNESS

Generating synthetic data that reflect the important under-
lying statistical properties of the real-world data may also
inherit the bias from data preprocessing, collection, and algo-
rithms [232]. Minority groups can often end up being under-
represented in synthetic data [233]–[235]. The fairness prob-
lem is currently addressed by three types of methods [236]:
(i) preprocessing, which revises input data to remove informa-
tion correlated to sensitive attributes, usually via techniques
like massaging, reweighting, and sampling. (ii) in-processing,
which adds fairness constraints to the model learning process;
and (iii) post-processing, which adjusts model predictions after
the model is trained.

Most existing fairness-aware data synthesis methods lever-
age preprocessing techniques. The use of balanced synthetic
datasets created by GANs to augment classification training
has demonstrated the benefits for reducing disparate impact
due to minoritized subgroup imbalance [237]–[239]. [240]
models bias using a probabilistic network exploiting structural
equation modeling as the preprocessing to generate a fairness-
aware synthetic dataset. Authors in [241] leverage GAN as
the pre-processing for fair data generation that ensures the
generated data is discrimination free while maintaining high
data utility. By comparison, [242] is geared towards high
dimensional image data and proposes a novel auxiliary clas-
sifier GAN that strives for demographic parity or equality
of opportunity. However, preprocessing would require the
synthesized data provider to know all correlations, biases, and
distributions of variables in the existing datasets as a priori.
Compared to preprocessing, the latter two categories are less-
developed for fair data synthesis. [243] insert a structural
causal model in the input layers of the generator, allowing
each variable to be reconstructed conditioned on its causal
parents for inference time debiasing.

In the meantime, differential privacy amplifies the fairness
issues in the original data [244]. [131] demonstrate that
differential privacy does not introduce unfairness into the data
generation process or to standard group fairness measures
in the downstream classification models, but does unfairly
increase the influence of majority subgroups. Differential
privacy also significantly reduces the quality of the images
generated from the GANs, decreasing the synthetic data’s
utility in downstream tasks. To measure the fairness in synthe-
sized data, [94] develops two covariate-level disparity fairness
metrics for synthetic data. The authors analyze all subgroups
defined by protected attributes to analyze the bias.

In the emerging AIGC using foundation models, the gen-
erated images and texts may also inherit
the stereotypes,
exclusion and marginalization of certain groups and toxic
and offensive information in the real-world data. This would

---

<!-- PAGE 12 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

12

lead to discrimination and harm to certain social groups. The
misuse of such data synthesis approaches by misinformation
and manipulation would lead to further negative social im-
pact [245]. Given that the quality of the data generated by
foundation models is inextricably linked to the quality of
the training corpora, it is essential to regulate the real-world
data being used to form the data synthesis distribution. While
reducing bias in data is important, the remaining bias in the
data may also be amplified by the models [236] or the privacy-
enhancing components [244]. With frequent inspection and
sensitive and toxic information removal on both data and
model, it will help govern the information generated from
those foundation models and ensure the models would do no
harm.

VI. EVALUATION STRATEGY

In this section, we discuss various approaches to evaluating
the quality of synthesized data, which is essential for deter-
mining the effectiveness and applicability of synthetic data
generation methods in real-world scenarios. We categorize
these evaluation strategies as follows:
1) Human evaluation. This method is the most direct way
to assess the quality of synthesized data. Human evalua-
tion involves soliciting opinions from domain experts or
non-expert users to judge the synthesized data’s quality,
similarity to real data, or usability in specific applications.
For example, in speech synthesis, the human evaluator
rates the synthesized speech and real human speech in
a blind manner [44], [246]. However, human evaluation
has several drawbacks, including being expensive, time-
consuming, error-prone, and not scalable. Additionally, it
struggles with high-dimensional data that cannot be easily
visualized and evaluated by humans.

2) Statistical difference evaluation. This strategy involves
calculating various statistical metrics on both the synthe-
sized and real datasets and comparing the results. For
example, [53], [247] use first-moment statistics of individ-
ual features (e.g., medical concept frequency/correlation,
patient-level clinical feature) to evaluate the quality of gen-
erated electronic health record (EHR) data. The smaller the
differences between the statistical properties of synthetic
and real data, the better the quality of the synthesized data.
3) Evaluation using a pre-trained machine learning model.
As mentioned in Section III-D, in the generative adversarial
network (GAN), the discriminator differentiates fake data
(synthesized data) from real ones. Consequently, the output
of the discriminator can measure how closely synthetic data
resembles real data. The performance of the discriminator
on the synthesized data can be used as an indicator of how
well the generator produces realistic data. This strategy can
be applied not only to GANs but also to other generative
models where a pre-trained machine learning model is used
for evaluation.

4) Training on synthetic dataset and testing on the real
dataset (TSTR). This strategy involves using synthetic
data to train machine learning models and assessing their
prediction performance on real test data in downstream

applications. High performance on real test data indicates
that the synthetic data has successfully captured essential
characteristics of the real data, making it a useful proxy
for training. For example, [248] employs synthetic data to
train machine learning models and assess their prediction
performance on real test data in downstream applications.
TSTR can provide insights into the effectiveness of syn-
thetic data for training machine learning models in a wide
range of tasks and domains.

5) Application-specific evaluation. Depending on the spe-
cific use case or domain, tailored evaluation methods may
be employed to assess the quality of synthesized data.
These evaluation methods can consider the unique require-
ments or constraints of the application, such as regulatory
compliance, privacy concerns, or specific performance met-
rics. By evaluating the synthesized data in the context of
its intended use, a more accurate assessment of its quality
and applicability can be obtained.
These evaluation strategies offer various ways to gauge the
quality of synthesized data, helping researchers and practition-
ers determine the effectiveness of synthetic data generation
methods and their applicability in real-world scenarios. Em-
ploying a combination of these strategies can provide a more
comprehensive understanding of the strengths and weaknesses
of the synthesized data, facilitating further improvements in
synthetic data generation techniques [249].

VII. CHALLENGES AND OPPORTUNITIES
The aim of this research is to present a comprehensive sur-
vey of synthetic data generation—a promising and emerging
technique in contemporary deep learning. This survey outlines
current real-world applications and identifies potential avenues
for future research in this field. The utilization of synthetic data
has been proven effective across a diverse array of tasks and
domains [9]. In this section, we delve into the challenges and
opportunities presented by this rapidly evolving area.

First and foremost, evaluation metrics for synthetic data
are essential to determine the reasonableness of the generated
data. In industries like healthcare, where data quality is of
paramount importance, clinical quality measures and evalu-
ation metrics are not always readily available for synthetic
data. Clinicians often struggle to interpret existing criteria
such as probability likelihood and divergence scores when
there is a
assessing generative models [69]. Concurrently,
pressing need to develop and adopt specific regulations for
the use of synthetic data in medicine and healthcare, ensuring
that the generated data meets the required quality standards
while minimizing potential risks.

Secondly, due to limited attention and the challenges as-
sociated with covering various domains using synthetic data,
current methods might not account for all outliers and corner
cases present in the original data. Investigating outliers and
regular instances and their impact on the parameterization of
existing methods could be a valuable research direction [250].
To enhance future detection methods, it may be beneficial
to examine the gap between the performance of detection
methods and a well-designed evaluation matrix, which could
provide insights into areas that require improvement.

---

<!-- PAGE 13 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

13

Thirdly, synthetic data generation may involve underlying
models with inherent biases, which might not be immediately
evident [94]. Factors such as sample selection biases and
class imbalances can contribute to these issues. Typically,
algorithms trained with biases in sample selection may un-
derperform when deployed in settings that deviate significantly
from the conditions in which the data was collected [69]. Thus,
it is crucial to develop methods and strategies that address
these biases, ensuring that synthetic data generation leads to
more accurate and reliable results across diverse applications
and domains.

Last but not the least, the rise of foundation models in
data synthesis presents both significant challenges and oppor-
tunities. On one hand, foundation models can be exploited
by malicious actors to create sophisticate jailbreak attacks,
deepfakes, discrimination, exclusion and toxicity problems,
misinformation harms, sensitive information disclosure, and
malicious use. These models can generate human-like text and
realistic images or videos, making it difficult for traditional
security measures to detect malicious content. Furthermore,
the accessibility and rapid advancement of these technologies
lower the barrier for cybercriminals, enabling more sophis-
ticated and widespread attacks. The ability to generate vast
amounts of realistic, yet fake, data can also overwhelm and
deceive traditional detection systems, leading to an increase in
false negatives and undetected breaches. On the other hand,
foundation models offer promising opportunities to bolster
cybersecurity defenses. AI-driven anomaly detection systems
can leverage generative models to simulate various attack
scenarios, improving their ability to recognize and mitigate
real-world threats. In the meantime, the quest for transparency
and interpretability in generative models promotes research
into explainable AI. By proactively addressing these machine
learning risks, synthetic data generation can evolve to deliver
more ethical, secure, and transparent solutions, ultimately
harnessing its full potential to benefit society while mitigating
its associated risks.

In general, the use of synthetic data is becoming a viable
alternative to training models with real data due to advances
in simulations and generative models. However, a number of
open challenges need to be overcome to achieve high perfor-
mance. These include the lack of standard tools, the difference
between synthetic and real data, and how much machine
learning algorithms can do to exploit imperfect synthetic data
effectively. Though this emerging approach is not perfect now,
with models, metrics, and technologies maturing, we believe
synthetic data generation will make a bigger impact in the
future.

VIII. CONCLUSION
In conclusion, machine learning has revolutionized various
industries by enabling intelligent computer systems to au-
tonomously tackle tasks, manage and analyze massive volumes
of data. However, it still faces several challenges, including
data quality, data scarcity, and data governance. These chal-
lenges can be addressed through synthetic data generation,
which involves the artificial annotation of information gener-
ated by computer algorithms or simulations. Synthetic data has

been extensively utilized in various sectors due to its ability
to bridge gaps, especially when real data is either unavailable
or must be kept private due to privacy or compliance risks.

This paper has provided a high-level overview of several
state-of-the-art approaches currently being investigated by
machine learning researchers for synthetic data generation. We
have explored different real-world application domains, and
examined a diverse array of deep neural network architectures
and deep generative models dedicated to generating high-
quality synthetic data.

To sum up, synthetic data generation has enormous potential
for unlocking the full potential of machine learning and its
impact on various industries. While challenges persist in the
development and application of machine learning technology,
synthetic data generation provides a promising solution that
can help address these obstacles. Future research can further
enhance the functionality of synthetic data generation.

REFERENCES

[1] A. Ng, “What artificial

intelligence can and can’t do right now,”

Harvard Business Review, vol. 9, no. 11, 2016.
[2] M. A. Boden, Artificial intelligence. Elsevier, 1996.
[3] M. Haenlein and A. Kaplan, “A brief history of artificial intelligence:
On the past, present, and future of artificial intelligence,” California
management review, vol. 61, no. 4, pp. 5–14, 2019.

[4] F. Lucini, “The real deal about synthetic data,” MIT Sloan Management

Review, vol. 63, no. 1, pp. 1–4, 2021.

[5] M. I. Jordan and T. M. Mitchell, “Machine learning: Trends, perspec-
tives, and prospects,” Science, vol. 349, no. 6245, pp. 255–260, 2015.
[6] L. L. Pipino, Y. W. Lee, and R. Y. Wang, “Data quality assessment,”
Communications of the ACM, vol. 45, no. 4, pp. 211–218, 2002.
[7] M. Shen, Y.-T. Chang, C.-T. Wu, S. J. Parker, G. Saylor, Y. Wang,
G. Yu, J. E. Van Eyk, R. Clarke, D. M. Herrington et al., “Comparative
assessment and novel strategy on methods for imputing proteomics
data,” Scientific reports, vol. 12, no. 1, p. 1067, 2022.

[8] R. Babbar and B. Sch¨olkopf, “Data scarcity, robustness and extreme
multi-label classification,” Machine Learning, vol. 108, no. 8, pp.
1329–1351, 2019.

[9] S. I. Nikolenko, Synthetic data for deep learning. Springer, 2021, vol.

174.

[10] V. Bol´on-Canedo, N. S´anchez-Maro˜no, and A. Alonso-Betanzos, “A
review of feature selection methods on synthetic data,” Knowledge and
information systems, vol. 34, no. 3, pp. 483–519, 2013.

[11] M. Frid-Adar, E. Klang, M. Amitai, J. Goldberger, and H. Greenspan,
“Synthetic data augmentation using gan for improved liver lesion clas-
sification,” in IEEE international symposium on biomedical imaging
(ISBI), 2018.

[12] Q. Wang, J. Gao, W. Lin, and Y. Yuan, “Learning from synthetic data
for crowd counting in the wild,” in IEEE/CVF conference on computer
vision and pattern recognition, 2019.

[13] J. M. Abowd and L. Vilhuber, “How protective are synthetic data?”
in International Conference on Privacy in Statistical Databases.
Springer, 2008.

[14] N. C. Abay, Y. Zhou, M. Kantarcioglu, B. Thuraisingham, and
L. Sweeney, “Privacy preserving synthetic data release using deep
learning,” in Joint European Conference on Machine Learning and
Knowledge Discovery in Databases. Springer, 2019.

[15] T. E. Raghunathan, “Synthetic data,” Annual Review of Statistics and

Its Application, vol. 8, pp. 129–140, 2021.

[16] E. Choi, S. Biswal, B. Malin, J. Duke, W. F. Stewart, and J. Sun, “Gen-
erating multi-label discrete patient records using generative adversarial
networks,” in Machine learning for healthcare conference.
PMLR,
2017.

[17] J. D. Ziegler, S. Subramaniam, M. Azzarito, O. Doyle, P. Krusche,
and T. Coroller, “Multi-modal conditional GAN: Data synthesis in the
medical domain,” in NeurIPS 2022 Workshop on Synthetic Data for
Empowering ML Research, 2022.

---

<!-- PAGE 14 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

14

[18] K. W. Dunn, C. Fu, D. J. Ho, S. Lee, S. Han, P. Salama, and E. J. Delp,
“DeepSynth: Three-dimensional nuclear segmentation of biological
images using neural networks trained with synthetic data,” Scientific
reports, vol. 9, no. 1, pp. 1–15, 2019.

[19] Y. Du, X. Liu, N. Shah, S. Liu, J. Zhang, and B. Zhou, “Chemspace:
Interpretable and interactive chemical space exploration,” 2022.
[20] T. Sterling and J. J. Irwin, “Zinc 15–ligand discovery for everyone,”
Journal of chemical information and modeling, vol. 55, no. 11, pp.
2324–2337, 2015.

[21] W. Jin, R. Barzilay, and T. S. Jaakkola, “Junction tree variational au-
toencoder for molecular graph generation,” in International Conference
on Machine Learning, 2018.

[22] M. Olivecrona, T. Blaschke, O. Engkvist, and H. Chen, “Molecular
learning,” Journal of

de-novo design through deep reinforcement
cheminformatics, vol. 9, no. 1, p. 48, 2017.

[23] T. Fu, C. Xiao, and J. Sun, “CORE: Automatic molecule optimization
using copy and refine strategy,” AAAI conference on artificial intelli-
gence, 2020.

[24] T. Fu, W. Gao, C. W. Coley, and J. Sun, “Reinforced genetic algorithm
for structure-based drug design,” in Advances in Neural Information
Processing Systems (NeurIPS), 2022.

[25] K. Huang, T. Fu, W. Gao, Y. Zhao, Y. Roohani, J. Leskovec, C. W.
Coley, C. Xiao, J. Sun, and M. Zitnik, “Artificial intelligence foundation
for therapeutic science,” Nature Chemical Biology, pp. 1–4, 2022.
[26] A. Torfi and E. A. Fox, “Corgan: Correlation-capturing convolutional
generative adversarial networks for generating synthetic healthcare
records,” in International Flairs Conference, 2020.

[27] D. Lee, H. Yu, X. Jiang, D. Rogith, M. Gudala, M. Tejani, Q. Zhang,
and L. Xiong, “Generating sequential electronic health records using
dual adversarial autoencoder,” Journal of the American Medical Infor-
matics Association, vol. 27, no. 9, pp. 1411–1419, 2020.

[28] S. Wharrie, Z. Yang, V. Raj, R. Monti, R. Gupta, Y. Wang, A. Martin,
L. J. O’Connor, S. Kaski, P. Marttinen et al., “HAPNEST: an efficient
tool for generating large-scale genetics datasets from limited training
data,” in NeurIPS 2022 Workshop on Synthetic Data for Empowering
ML Research, 2022.

[29] B. Nowok, G. M. Raab, and C. Dibben, “synthpop: Bespoke creation
of synthetic data in R,” Journal of statistical software, vol. 74, pp.
1–26, 2016.

[30] J.-Y. Zhu, T. Park, P. Isola, and A. A. Efros, “Unpaired image-to-
image translation using cycle-consistent adversarial networks,” in IEEE
international conference on computer vision, 2017.

[31] R. Torkzadehmahani, P. Kairouz, and B. Paten, “Dp-cgan: Differentially
private synthetic data and label generation,” in IEEE/CVF Conference
on Computer Vision and Pattern Recognition Workshops, 2019.
[32] A. Brock, J. Donahue, and K. Simonyan, “Large scale GAN
image synthesis,” arXiv preprint

training for high fidelity natural
arXiv:1809.11096, 2018.

[33] J. Ho, T. Salimans, A. Gritsenko, W. Chan, M. Norouzi, and D. J. Fleet,
“Video diffusion models,” arXiv preprint arXiv:2204.03458, 2022.
[34] A. Razavi, A. Van den Oord, and O. Vinyals, “Generating diverse
high-fidelity images with vq-vae-2,” Advances in neural information
processing systems, vol. 32, 2019.

[35] M. Niemeyer and A. Geiger, “Giraffe: Representing scenes as compo-
sitional generative neural feature fields,” in IEEE/CVF Conference on
Computer Vision and Pattern Recognition, 2021.

[36] N. Chen, Y. Zhang, H. Zen, R. J. Weiss, M. Norouzi, and W. Chan,
“Wavegrad: Estimating gradients for waveform generation,” Interna-
tional Conference on Learning Representations (ICLR), 2021.
[37] H. Guo, F. K. Soong, L. He, and L. Xie, “A new GAN-based end-to-end
TTS training algorithm,” arXiv preprint arXiv:1904.04775, 2019.
[38] L. Yu, W. Zhang, J. Wang, and Y. Yu, “Seqgan: Sequence generative
adversarial nets with policy gradient,” in AAAI conference on artificial
intelligence, vol. 31, no. 1, 2017.

[39] T. Sellam, D. Das, and A. P. Parikh, “Bleurt: Learning robust metrics

for text generation,” arXiv preprint arXiv:2004.04696, 2020.

[40] Z. Shi, X. Chen, X. Qiu, and X. Huang, “Toward diverse text generation
with inverse reinforcement learning,” in International Joint Conference
on Artificial Intelligence, 2018.

[41] C.-Y. Ko, P.-Y. Chen, J. Mohapatra, P. Das, and L. Daniel, “Synbench:
Task-agnostic benchmarking of pretrained representations using syn-
thetic data,” arXiv preprint arXiv:2210.02989, 2022.

[43] G. Acs, L. Melis, C. Castelluccia, and E. De Cristofaro, “Differentially
private mixture of generative neural networks,” IEEE Transactions on
Knowledge and Data Engineering, vol. 31, no. 6, pp. 1109–1121, 2018.
[44] C. Donahue, J. McAuley, and M. Puckette, “Adversarial audio synthe-

sis,” arXiv preprint arXiv:1802.04208, 2018.

[45] A. v. d. Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals,
A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu, “Wavenet:
A generative model for raw audio,” arXiv preprint arXiv:1609.03499,
2016.

[46] X. Zhang, I. Vall´es-P´erez, A. Stolcke, C. Yu, J. Droppo, O. Shonibare,
R. Barra-Chicote, and V. Ravichandran, “Stutter-tts: Controlled syn-
thesis and improved recognition of stuttered speech,” arXiv preprint
arXiv:2211.09731, 2022.

[47] M. Wiese, R. Knobloch, R. Korn, and P. Kretschmer, “Quant GANs:
deep generation of financial time series,” Quantitative Finance, vol. 20,
no. 9, pp. 1419–1440, 2020.

[48] R. Fu, J. Chen, S. Zeng, Y. Zhuang, and A. Sudjianto, “Time series
simulation by conditional generative adversarial net,” arXiv preprint
arXiv:1904.11419, 2019.

[49] J. Jordon, J. Yoon, and M. Van Der Schaar, “Pate-gan: Generating
synthetic data with differential privacy guarantees,” in International
conference on learning representations, 2018.

[50] A. Collaboration et al., “Deep generative models for fast photon shower

simulation in atlas,” arXiv preprint arXiv:2210.06204, 2022.

[51] C. Dewi, R.-C. Chen, Y.-T. Liu, and S.-K. Tai, “Synthetic data
generation using dcgan for improved traffic sign recognition,” Neural
Computing and Applications, vol. 34, no. 24, pp. 21 465–21 480, 2022.
[52] Z. Zhao, K. Xu, S. Li, Z. Zeng, and C. Guan, “Mt-uda: Towards
unsupervised cross-modality medical image segmentation with limited
source labels,” in Medical Image Computing and Computer Assisted
Intervention (MICCAI). Springer, 2021.

[53] S. Yi, M. Lu, A. Yee, J. Harmon, F. Meng, and S. Hinduja, “Enhance
wound healing monitoring through a thermal imaging based smart-
phone app,” in Medical Imaging: Imaging Informatics for Healthcare,
Research, and Applications. SPIE, 2018.

[54] Y. Chen, W. Li, X. Chen, and L. V. Gool, “Learning semantic
segmentation from synthetic data: A geometrically guided input-output
adaptation approach,” in IEEE/CVF Conference on Computer Vision
and Pattern Recognition, 2019.

[55] S. Sankaranarayanan, Y. Balaji, A. Jain, S. N. Lim, and R. Chellappa,
“Learning from synthetic data: Addressing domain shift for semantic
segmentation,” in IEEE/CVF conference on computer vision and pat-
tern recognition, 2018.

[56] H.-W. Dong and Y.-H. Yang, “Towards a deeper understanding of

adversarial losses,” arXiv preprint arXiv:1901.08753, 2019.

[57] E. Wood, T. Baltruˇsaitis, C. Hewitt, S. Dziadzio, T. J. Cashman,
and J. Shotton, “Fake it till you make it: face analysis in the wild
using synthetic data alone,” in IEEE/CVF international conference on
computer vision, 2021.

[58] A. Werchniak, R. B. Chicote, Y. Mishchenko, J. Droppo, J. Condal,
P. Liu, and A. Shah, “Exploring the application of synthetic audio
in training keyword spotters,” in IEEE International Conference on
Acoustics, Speech and Signal Processing (ICASSP), 2021.

[59] W. Li, H. You, J. Zhu, and N. Chen, “Feature sparsity analysis for
i-vector based speaker verification,” Speech Communication, vol. 80,
pp. 60–70, 2016.

[60] Y. Qian, Y. Liu, and K. Yu, “Tandem deep features for text-dependent
speaker verification,” in Fifteenth Annual Conference of the Interna-
tional Speech Communication Association, 2014.

[61] Z.-H. Ling, L. Deng, and D. Yu, “Modeling spectral envelopes using
restricted boltzmann machines and deep belief networks for statistical
parametric speech synthesis,” IEEE transactions on audio, speech, and
language processing, vol. 21, no. 10, pp. 2129–2139, 2013.

[62] A. Fazel, W. Yang, Y. Liu, R. Barra-Chicote, Y. Meng, R. Maas, and
J. Droppo, “Synthasr: Unlocking synthetic data for speech recognition,”
arXiv preprint arXiv:2106.07803, 2021.

[63] W. Li and J. Zhu, “An improved i-vector extraction algorithm for
speaker verification,” EURASIP Journal on Audio, Speech, and Music
Processing, vol. 2015, pp. 1–9, 2015.

[64] G. Forman, “An extensive empirical study of feature selection metrics
for text classification,” Journal of Machine Learning Research, vol. 3,
pp. 1289–1305, 2003.

[42] W. Nie, N. Narodytska, and A. Patel, “Relgan: Relational generative
adversarial networks for text generation,” in International conference
on learning representations, 2018.

[65] X. Yue, H. A. Inan, X. Li, G. Kumar, J. McAnallen, H. Sun, D. Levitan,
and R. Sim, “Synthetic text generation with differential privacy: A
simple and practical recipe,” arXiv preprint arXiv:2210.14348, 2022.

---

<!-- PAGE 15 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

15

[66] X. Zheng, Y. Liu, D. Gunceler, and D. Willett, “Using synthetic audio
to improve the recognition of out-of-vocabulary words in end-to-end
asr systems,” in IEEE International Conference on Acoustics, Speech
and Signal Processing (ICASSP), 2021.

[67] Y. Fu, Y. Lu, Y. Wang, B. Zhang, Z. Zhang, G. Yu, C. Liu, R. Clarke,
D. M. Herrington, and Y. Wang, “Ddn3. 0: Determining significant
rewiring of biological network structure with differential dependency
networks,” Bioinformatics, p. btae376, 2024.

[68] Z. Zhao, A. Zhu, Z. Zeng, B. Veeravalli, and C. Guan, “Act-net:
Asymmetric co-teacher network for semi-supervised memory-efficient
medical image segmentation,” in IEEE International Conference on
Image Processing (ICIP).
IEEE, 2022.

[69] R. J. Chen, M. Y. Lu, T. Y. Chen, D. F. Williamson, and F. Mahmood,
“Synthetic data in machine learning for medicine and healthcare,”
Nature Biomedical Engineering, vol. 5, no. 6, pp. 493–497, 2021.
[70] A. Tucker, Z. Wang, Y. Rotalinti, and P. Myles, “Generating high-
fidelity synthetic patient data for assessing machine learning healthcare
software,” NPJ digital medicine, vol. 3, no. 1, pp. 1–13, 2020.
[71] Y. Wang, Y. Lu, Y. Xu, Z. Ma, H. Xu, B. Du, H. Gao, and J. Wu,
“Twin-gpt: Digital twins for clinical trials via large language model,”
arXiv preprint arXiv:2404.01273, 2024.

[72] Y. Lu, C.-T. Wu, S. J. Parker, Z. Cheng, G. Saylor, J. E. Van Eyk,
G. Yu, R. Clarke, D. M. Herrington, and Y. Wang, “Cot: an efficient and
accurate method for detecting marker genes among many subtypes,”
Bioinformatics Advances, vol. 2, no. 1, p. vbac037, 2022.

[73] J. Dahmen and D. Cook, “Synsys: A synthetic data generation system

for healthcare applications,” Sensors, vol. 19, no. 5, p. 1181, 2019.

[74] Y. Lu, Y.-T. Chang, E. P. Hoffman, G. Yu, D. M. Herrington, R. Clarke,
C.-T. Wu, L. Chen, and Y. Wang, “Integrated identification of disease
specific pathways using multi-omics data,” bioRxiv, p. 666065, 2019.
[75] Z. Wang, P. Myles, and A. Tucker, “Generating and evaluating cross-
sectional synthetic electronic healthcare data: Preserving data utility
and patient privacy,” Computational Intelligence, vol. 37, no. 2, pp.
819–851, 2021.

[76] R. S. Bohacek, C. McMartin, and W. C. Guida, “The art and practice
of structure-based drug design: a molecular modeling perspective,”
Medicinal research reviews, vol. 16, no. 1, pp. 3–50, 1996.

[77] K. Huang, T. Fu, L. M. Glass, M. Zitnik, C. Xiao, and J. Sun,
“DeepPurpose: a deep learning library for drug–target
interaction
prediction,” Bioinformatics, vol. 36, no. 22-23, pp. 5545–5547, 2020.
[78] R. G´omez-Bombarelli, J. N. Wei, D. Duvenaud, J. M. Hern´andez-
Lobato, B. S´anchez-Lengeling, D. Sheberla, J. Aguilera-Iparraguirre,
T. D. Hirzel, R. P. Adams, and A. Aspuru-Guzik, “Automatic chemical
design using a data-driven continuous representation of molecules,”
ACS central science, vol. 4, no. 2, pp. 268–276, 2018.

[79] B. Zhang, Y. Fu, Y. Lu, Z. Zhang, R. Clarke, J. E. Van Eyk,
D. M. Herrington, and Y. Wang, “DDN2.0: R and python packages
for differential dependency network analysis of biological systems,”
bioRxiv, pp. 2021–04, 2021.

[80] N. De Cao and T. Kipf, “MolGAN: An implicit generative model for
small molecular graphs,” arXiv preprint arXiv:1805.11973, 2018.
[81] T. Fu and J. Sun, “Antibody Complementarity Determining Regions
(CDRs) design using constrained energy model,” in ACM SIGKDD
Conference on Knowledge Discovery and Data Mining, 2022.
[82] T. Fu, W. Gao, C. Xiao, J. Yasonik, C. W. Coley, and J. Sun, “Dif-
ferentiable scaffolding tree for molecular optimization,” International
Conference on Learning Representations, 2022.

[83] M. Xu, L. Yu, Y. Song, C. Shi, S. Ermon, and J. Tang, “GeoDiff: A
geometric diffusion model for molecular conformation generation,” in
International Conference on Learning Representations, 2021.

[84] Z. Zhou, S. Kearnes, L. Li, R. N. Zare, and P. Riley, “Optimization of
molecules via deep reinforcement learning,” Scientific reports, vol. 9,
no. 1, pp. 1–10, 2019.

[85] J. H. Jensen, “A graph-based genetic algorithm and generative
model/monte carlo tree search for the exploration of chemical space,”
Chemical science, vol. 10, no. 12, pp. 3567–3572, 2019.

[86] T. Fu, C. Xiao, X. Li, L. M. Glass, and J. Sun, “MIMOSA: Multi-
constraint molecule sampling for molecule optimization,” in AAAI
Conference on Artificial Intelligence, 2021.

[87] T. Fu and J. Sun, “SIPF: Sampling method for inverse protein folding,”
in ACM SIGKDD Conference on Knowledge Discovery and Data
Mining, 2022.

[88] C. S. Kruse, B. Smith, H. Vanderlinden, and A. Nealand, “Security
techniques for the electronic health records,” Journal of medical
systems, vol. 41, no. 8, pp. 1–9, 2017.

[89] Q. Wen, Z. Ouyang, J. Zhang, Y. Qian, Y. Ye, and C. Zhang, “Dis-
entangled dynamic heterogeneous graph learning for opioid overdose
prediction,” in ACM SIGKDD Conference on Knowledge Discovery
and Data Mining, 2022.

[90] T. Fu, T. Gao, C. Xiao, T. Ma, and J. Sun, “Pearl: Prototype learning
via rule learning,” in ACM International Conference on Bioinformatics,
Computational Biology and Health Informatics, 2019, pp. 223–232.

[91] A. Goncalves, P. Ray, B. Soper, J. Stevens, L. Coyle, and A. P. Sales,
“Generation and evaluation of synthetic patient data,” BMC medical
research methodology, vol. 20, no. 1, pp. 1–40, 2020.

[92] D. Du, S. Bhardwaj, S. J. Parker, Z. Cheng, Z. Zhang, Y. Lu, J. E.
Van Eyk, G. Yu, R. Clarke, D. M. Herrington et al., “Abds: tool suite for
analyzing biologically diverse samples,” bioRxiv, pp. 2023–07, 2023.
[93] Y. Lu, “Multi-omics data integration for identifying disease specific

biological pathways,” Ph.D. dissertation, Virginia Tech, 2018.

[94] K. Bhanot, M. Qi, J. S. Erickson, I. Guyon, and K. P. Bennett, “The
problem of fairness in synthetic healthcare data,” Entropy, vol. 23,
no. 9, p. 1165, 2021.

[95] T. Fu, K. Huang, C. Xiao, L. M. Glass, and J. Sun, “HINT: Hierarchical
interaction network for clinical-trial-outcome predictions,” Patterns,
vol. 3, no. 4, p. 100445, 2022.

[96] T. Fu, T. N. Hoang, C. Xiao, and J. Sun, “DDL: Deep dictionary
learning for predictive phenotyping,” in International Joint Conference
on Artificial Intelligence, 2019.

[97] L. Chen, Y. Lu, C.-T. Wu, R. Clarke, G. Yu, J. E. Van Eyk, D. M.
Herrington, and Y. Wang, “Data-driven detection of subtype-specific
differentially expressed genes,” Scientific reports, vol. 11, no. 1, pp.
1–12, 2021.

[98] P. Eigenschink, S. Vamosi, R. Vamosi, C. Sun, T. Reutterer, and
K. Kalcher, “Deep generative models for synthetic data,” ACM Com-
puting Surveys, 2021.

[99] C.-T. Wu, M. Shen, D. Du, Z. Cheng, S. J. Parker, Y. Lu, J. E. Van Eyk,
G. Yu, R. Clarke, D. M. Herrington et al., “Cosbin: cosine score-based
iterative normalization of biologically diverse samples,” Bioinformatics
Advances, vol. 2, no. 1, p. vbac076, 2022.

[100] R. Wang and X. Qu, “Eeg daydreaming, a machine learning approach to
detect daydreaming activities,” in Augmented Cognition: International
Conference. Springer, 2022.

[101] Y. Du, T. Fu, J. Sun, and S. Liu, “Molgensurvey: A systematic
survey in machine learning models for molecule design,” arXiv preprint
arXiv:2203.14500, 2022.

[102] K. El Emam, L. Mosquera, and R. Hoptroff, Practical synthetic data
generation: balancing privacy and the broad availability of data.
O’Reilly Media, 2020.

[103] M. Mannino and A. Abouzied, “Is this real? generating synthetic data
that looks real,” in ACM Symposium on User Interface Software and
Technology, 2019.

[104] S. A. Assefa, D. Dervovic, M. Mahfouz, R. E. Tillman, P. Reddy,
and M. Veloso, “Generating synthetic data in finance: opportunities,
challenges and pitfalls,” in ACM International Conference on AI in
Finance, 2020.

[105] P.-H. Lu, P.-C. Wang, and C.-M. Yu, “Empirical evaluation on synthetic
data generation with generative adversarial network,” in International
Conference on Web Intelligence, Mining and Semantics, 2019.
[106] M. Hittmeir, A. Ekelhart, and R. Mayer, “On the utility of synthetic
data: An empirical evaluation on machine learning tasks,” in Interna-
tional Conference on Availability, Reliability and Security, 2019.
[107] A. M. Berg, S. T. Mol, G. Kismih´ok, and N. Sclater, “The role of a
reference synthetic data generator within the field of learning analytics.”
Journal of Learning Analytics, vol. 3, no. 1, pp. 107–128, 2016.
[108] B. Howe, J. Stoyanovich, H. Ping, B. Herman, and M. Gee, “Synthetic
data for social good,” arXiv preprint arXiv:1710.08874, 2017.
[109] P. Bautista and P. S. Inventado, “Protecting student privacy with
synthetic data from generative adversarial networks,” in International
Conference on Artificial Intelligence in Education. Springer, 2021.

[110] H. Jiang, J. Li, P. Zhao, F. Zeng, Z. Xiao, and A. Iyengar, “Location
privacy-preserving mechanisms in location-based services: A compre-
hensive survey,” ACM Computing Surveys (CSUR), vol. 54, no. 1, pp.
1–36, 2021.

[111] R. Kato, M. Iwata, T. Hara, A. Suzuki, X. Xie, Y. Arase, and S. Nishio,
“A dummy-based anonymization method based on user trajectory
with pauses,” in International Conference on Advances in Geographic
Information Systems, 2012.

[112] Y. Du, S. Wang, X. Guo, H. Cao, S. Hu, J. Jiang, A. Varala,
A. Angirekula, and L. Zhao, “GraphGT: Machine learning datasets
for graph generation and transformation,” in Neural Information Pro-
cessing Systems Datasets and Benchmarks Track, 2021.

---

<!-- PAGE 16 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

16

[113] R. Chen, G. Acs, and C. Castelluccia, “Differentially private sequential
data publication via variable-length n-grams,” in ACM conference on
Computer and communications security, 2012.

[136] G. Papyshev and M. Yarime, “Exploring city digital twins as policy
tools: A task-based approach to generating synthetic data on urban
mobility,” Data & Policy, vol. 3, p. e16, 2021.

[114] C. Dwork, A. Roth et al., “The algorithmic foundations of differential
privacy,” Foundations and Trends® in Theoretical Computer Science,
vol. 9, no. 3–4, pp. 211–407, 2014.

[115] T. Cunningham, G. Cormode, H. Ferhatosmanoglu, and D. Srivastava,
“Real-world trajectory sharing with local differential privacy,” Proceed-
ings of the VLDB Endowment, vol. 14, no. 11, pp. 2283–2295, 2021.
[116] Y. Du, Y. Hu, Z. Zhang, Z. Fang, L. Chen, B. Zheng, and Y. Gao, “Ldp-
trace: Locally differentially private trajectory synthesis,” Proceedings
of the VLDB Endowment, vol. 16, no. 8, pp. 1897–1909, 2023.
[117] X. He, G. Cormode, A. Machanavajjhala, C. M. Procopiuc, and
D. Srivastava, “Dpt: differentially private trajectory synthesis using
hierarchical reference systems,” VLDB Endowment, vol. 8, no. 11, pp.
1154–1165, 2015.

[118] S. Wang and R. O. Sinnott, “Protecting personal trajectories of so-
cial media users through differential privacy,” Computers & Security,
vol. 67, pp. 142–163, 2017.

[119] M. E. Gursoy, L. Liu, S. Truex, L. Yu, and W. Wei, “Utility-aware
synthesis of differentially private and attack-resilient location traces,”
in ACM SIGSAC conference on computer and communications security,
2018.

[120] M. E. Gursoy, L. Liu, S. Truex, and L. Yu, “Differentially private and
utility preserving publication of trajectory data,” IEEE Transactions on
Mobile Computing, vol. 18, no. 10, pp. 2315–2329, 2018.

[121] D. J. Mir, S. Isaacman, R. C´aceres, M. Martonosi, and R. N. Wright,
“Dp-where: Differentially private modeling of human mobility,” in
IEEE international conference on big data.

IEEE, 2013.

[122] H. Roy, M. Kantarcioglu, and L. Sweeney, “Practical differentially
private modeling of human movement data,” in Annual IFIP WG 11.3
Working Conference on Data and Applications Security and Privacy.
Springer, 2016.

[123] V. Bindschaedler and R. Shokri, “Synthesizing plausible privacy-
preserving location traces,” in IEEE Symposium on Security and
Privacy (SP), 2016.

[124] H. Wang, Z. Zhang, T. Wang, S. He, M. Backes, J. Chen, and
Y. Zhang, “Privtrace: Differentially private trajectory synthesis by
adaptive markov model,” in USENIX Security Symposium 2023, 2023.
[125] J. Narita, T. Murakami, H. Hino, M. Nishigaki, and T. Ohki, “Syn-
thesizing differentially private location traces including co-locations,”
International Journal of Information Security, vol. 23, no. 1, pp. 389–
410, 2024.

[126] Y. Cao, S. Li, Y. Liu, Z. Yan, Y. Dai, P. S. Yu, and L. Sun, “A
comprehensive survey of ai-generated content (aigc): A history of
generative ai from gan to chatgpt,” arXiv preprint arXiv:2303.04226,
2023.

[127] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N.
Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,”
Advances in neural information processing systems, 2017.

[128] W. Tao, S. Gao, and Y. Yuan, “Boundary crossing: an experimental
study of individual perceptions toward aigc,” Frontiers in Psychology,
vol. 14, 2023.

[129] R. J. M. Ventayen, “Openai chatgpt generated results: Similarity index
of artificial intelligence-based contents,” Available at SSRN 4332664,
2023.

[130] T. Yue, D. Au, C. C. Au, and K. Y. Iu, “Democratizing financial knowl-
edge with chatgpt by openai: Unleashing the power of technology,”
Available at SSRN 4346152, 2023.

[131] V. Cheng, V. M. Suriyakumar, N. Dullerud, S. Joshi, and M. Ghas-
semi, “Can you fake it until you make it? impacts of differentially
private synthetic data on downstream classification fairness,” in ACM
Conference on Fairness, Accountability, and Transparency, 2021.
[132] J. Hurst, K. Mayorov, and J. F. T. Tatsinkou, “The generation of
synthetic data for risk modelling,” Journal of Risk Management in
Financial Institutions, vol. 15, no. 3, pp. 260–269, 2022.

[133] Y.-L. Peng and W.-P. Lee, “Data selection to avoid overfitting for
foreign exchange intraday trading with machine learning,” Applied Soft
Computing, vol. 108, p. 107461, 2021.

[134] M. J. Schneider, S. Jagpal, S. Gupta, S. Li, and Y. Yu, “A flexible
method for protecting marketing data: An application to point-of-sale
data,” Marketing Science, vol. 37, no. 1, pp. 153–171, 2018.
[135] D. M. Smith, G. P. Clarke, and K. Harland, “Improving the synthetic
data generation process in spatial microsimulation models,” Environ-
ment and Planning A, vol. 41, no. 5, pp. 1251–1268, 2009.

[137] Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond,
T. Eccles, J. Keeling, F. Gimeno, A. Dal Lago et al., “Competition-
level code generation with alphacode,” Science, vol. 378, no. 6624, pp.
1092–1097, 2022.

[138] T. Ye, Y. Du, T. Ma, L. Wu, X. Zhang, S. Ji, and W. Wang, “Uncovering
llm-generated code: A zero-shot synthetic code detector via code
rewriting,” arXiv preprint arXiv:2405.16133, 2024.

[139] S. Ghosh, M. Chollet, E. Laksana, L.-P. Morency, and S. Scherer,
“Affect-LM: A neural language model for customizable affective text
generation,” in Annual Meeting of the Association for Computational
Linguistics, 2017.

[140] D. P. Kingma and M. Welling, “Auto-encoding variational bayes,”
International Conference on Learning Representations (ICLR), 2014.
[141] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,
S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial nets,”
in Advances in neural information processing systems, 2014.
[142] I. J. Goodfellow, “On distinguishability criteria for estimating genera-

tive models,” arXiv preprint arXiv:1412.6515, 2014.

[143] Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon,
and B. Poole, “Score-based generative modeling through stochastic
differential equations,” arXiv preprint arXiv:2011.13456, 2020.
[144] R. S. Sutton and A. G. Barto, Reinforcement learning: An introduction.

MIT press, 2018.

[145] S. H. Lee, “Natural language generation for electronic health records,”

NPJ digital medicine, vol. 1, no. 1, pp. 1–7, 2018.

[146] W. Hu, B. Liu, J. Gomes, M. Zitnik, P. Liang, V. Pande, and
J. Leskovec, “Strategies for pre-training graph neural networks,” in
International Conference on Learning Representations, 2019.
[147] C. P. Burgess, I. Higgins, A. Pal, L. Matthey, N. Watters, G. Des-
jardins, and A. Lerchner, “Understanding disentangling in β-vae,”
arXiv preprint arXiv:1804.03599, 2018.

[148] A. Vahdat and J. Kautz, “Nvae: A deep hierarchical variational autoen-
coder,” Advances in neural information processing systems, vol. 33,
2020.

[149] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,
S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial net-
works,” Communications of the ACM, vol. 63, no. 11, pp. 139–144,
2020.

[150] Y. Zhang, Y. Qian, Y. Fan, Y. Ye, X. Li, Q. Xiong, and F. Shao, “dstyle-
gan: Generative adversarial network based on writing and photography
styles for drug identification in darknet markets,” in Annual Computer
Security Applications Conference, 2020.

[151] M. Arjovsky, S. Chintala, and L. Bottou, “Wasserstein generative
adversarial networks,” in International conference on machine learning.
PMLR, 2017.

[152] Y. Zhang, Y. Qian, Y. Ye, and C. Zhang, “Adapting distilled knowledge
for few-shot relation reasoning over knowledge graphs,” in SIAM
International Conference on Data Mining (SDM), 2022.

[153] J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli,
“Deep unsupervised learning using nonequilibrium thermodynamics,”
in International Conference on Machine Learning. PMLR, 2015.

[154] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic
models,” in Advances in Neural Information Processing Systems, 2020.
[155] M. Liu, K. Yan, B. Oztekin, and S. Ji, “Graphebm: Molecu-
lar graph generation with energy-based models,” arXiv preprint
arXiv:2102.00546, 2021.

[156] L. Weng, “What are diffusion models?” lilianweng.github.io/lil-log,
2021. [Online]. Available: https://lilianweng.github.io/lil-log/2021/07/
11/diffusion-models.html

[157] G. Somepalli, V. Singla, M. Goldblum, J. Geiping, and T. Goldstein,
“Diffusion art or digital forgery? investigating data replication in
diffusion models,” arXiv preprint arXiv:2212.03860, 2022.

[158] K. Huang, T. Fu, W. Gao, Y. Zhao, Y. Roohani, J. Leskovec, C. W.
Coley, C. Xiao, J. Sun, and M. Zitnik, “Therapeutics data commons:
machine learning datasets and tasks for therapeutics,” NeurIPS Track
Datasets and Benchmarks, 2021.

[159] Y. Lu, T. Chen, N. Hao, C. Van Rechem, J. Chen, and T. Fu, “Un-
certainty quantification and interpretability for clinical trial approval
prediction,” Health Data Science, vol. 4, p. 0126, 2024.

[160] R. Shokri, M. Stronati, C. Song, and V. Shmatikov, “Membership in-
ference attacks against machine learning models,” in IEEE symposium
on security and privacy (SP), 2017.

---

<!-- PAGE 17 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

17

[161] S. Truex, L. Liu, M. E. Gursoy, L. Yu, and W. Wei, “Demystifying
membership inference attacks in machine learning as a service,” IEEE
Transactions on Services Computing, vol. 14, no. 6, pp. 2073–2089,
2019.

[162] L. Melis, C. Song, E. De Cristofaro, and V. Shmatikov, “Exploiting un-
intended feature leakage in collaborative learning,” in IEEE symposium
on security and privacy (SP), 2019.

[163] L. Zhu, Z. Liu, and S. Han, “Deep leakage from gradients,” Advances

in neural information processing systems, 2019.

[164] W. Wei, L. Liu, M. Loper, K.-H. Chow, M. E. Gursoy, S. Truex, and
Y. Wu, “A framework for evaluating client privacy leakages in federated
learning,” in European Symposium on Research in Computer Security.
Springer, 2020.

[165] J. Geiping, H. Bauermeister, H. Dr¨oge, and M. Moeller, “Inverting
to break privacy in federated learning?”

gradients-how easy is it
Advances in Neural Information Processing Systems, 2020.

[166] J. Hayes, L. Melis, G. Danezis, and E. De Cristofaro, “Logan: Mem-
bership inference attacks against generative models,” Proceedings on
Privacy Enhancing Technologies, 2019.

[167] B. Hitaj, G. Ateniese, and F. Perez-Cruz, “Deep models under the
gan: information leakage from collaborative deep learning,” in ACM
SIGSAC conference on computer and communications security, 2017.
[168] Z. Wang, M. Song, Z. Zhang, Y. Song, Q. Wang, and H. Qi, “Be-
yond inferring class representatives: User-level privacy leakage from
federated learning,” in IEEE conference on computer communications,
2019.

[169] G. Ganev and E. De Cristofaro, “On the inadequacy of similarity-
based privacy metrics: Reconstruction attacks against” truly anonymous
synthetic data”,” arXiv preprint arXiv:2312.05114, 2023.

[170] B. Hilprecht, M. H¨arterich, and D. Bernau, “Monte carlo and re-
construction membership inference attacks against generative models,”
Proceedings on Privacy Enhancing Technologies, 2019.

[171] Y. Xu, S. Mukherjee, X. Liu, S. Tople, R. M. Dodhia, and J. M. L. Fer-
res, “Mace: A flexible framework for membership privacy estimation
in generative models,” Transactions on Machine Learning Research,
2022.

and C. Troncoso,

[172] T. Stadler, B. Oprisanu,

“Synthetic data–
anonymisation groundhog day,” in USENIX Security Symposium, 2022.
[173] D. Chen, N. Yu, Y. Zhang, and M. Fritz, “Gan-leaks: A taxonomy
of membership inference attacks against generative models,” in ACM
SIGSAC conference on computer and communications security, 2020.
[174] V. Bindschaedler, R. Shokri, and C. A. Gunter, “Plausible deniability
for privacy-preserving data synthesis,” VLDB Endowment, vol. 10,
no. 5, 2017.

[175] B.-W. Tseng and P.-Y. Wu, “Compressive privacy generative adversarial
network,” IEEE Transactions on Information Forensics and Security,
vol. 15, pp. 2499–2513, 2020.

[176] X. Zhang, S. Ji, and T. Wang, “Differentially private releasing via deep
generative model (technical report),” arXiv preprint arXiv:1801.01594,
2018.

[177] L. Xie, K. Lin, S. Wang, F. Wang, and J. Zhou, “Differentially pri-
vate generative adversarial network,” arXiv preprint arXiv:1802.06739,
2018.

[178] C. Xu, J. Ren, D. Zhang, Y. Zhang, Z. Qin, and K. Ren, “Ganobfusca-
tor: Mitigating information leakage under gan via differential privacy,”
IEEE Transactions on Information Forensics and Security, vol. 14,
no. 9, pp. 2358–2371, 2019.

[179] A. Triastcyn and B. Faltings, “Federated generative privacy,” IEEE

Intelligent Systems, vol. 35, no. 4, pp. 50–57, 2020.

[180] P.-H. Lu and C.-M. Yu, “Poster: A unified framework of differentially
private synthetic data release with generative adversarial network,” in
ACM SIGSAC Conference on Computer and Communications Security,
2017.

[181] Y. Liu, J. Peng, J. James, and Y. Wu, “Ppgan: Privacy-preserving
generative adversarial network,” in IEEE international conference on
parallel and distributed systems (ICPADS).

IEEE, 2019.

[182] L. Frigerio, A. S. de Oliveira, L. Gomez, and P. Duverger, “Dif-
ferentially private generative adversarial networks for time series,
continuous, and discrete open data,” in IFIP TC 11 International
Conference on ICT Systems Security and Privacy Protection. Springer,
2019, pp. 151–164.

[183] B. K. Beaulieu-Jones, Z. S. Wu, C. Williams, R. Lee, S. P. Bhavnani,
J. B. Byrd, and C. S. Greene, “Privacy-preserving generative deep neu-
ral networks support clinical data sharing,” Circulation: Cardiovascular
Quality and Outcomes, vol. 12, no. 7, p. e005122, 2019.

[184] G. Astolfi and K. David, “Generating tabular data using generative ad-
versarial networks with differential privacy,” in Conference of European
Statisticians, 2021.

[185] D. Chen, T. Orekondy, and M. Fritz, “Gs-wgan: A gradient-sanitized
approach for learning differentially private generators,” Advances in
Neural Information Processing Systems, vol. 33, 2020.

[186] T. Cao, A. Bie, A. Vahdat, S. Fidler, and K. Kreis, “Don’t generate
me: Training differentially private generative models with sinkhorn
divergence,” Advances in Neural Information Processing Systems,
vol. 34, 2021.

[187] A. Torfi, E. A. Fox, and C. K. Reddy, “Differentially private synthetic
medical data generation using convolutional gans,” Information Sci-
ences, vol. 586, pp. 485–500, 2022.

[188] L. Fan and A. Pokkunuru, “Dpnet: Differentially private network
traffic synthesis with generative adversarial networks,” in IFIP Annual
Conference on Data and Applications Security and Privacy. Springer,
2021.

[189] Y. Long, B. Wang, Z. Yang, B. Kailkhura, A. Zhang, C. Gunter, and
B. Li, “G-pate: Scalable differentially private data generator via private
aggregation of teacher discriminators,” Advances in Neural Information
Processing Systems, vol. 34, 2021.

[190] T. Cunningham, K. Klemmer, H. Wen, and H. Ferhatosmanoglu, “Geo-
pointgan: Synthetic spatial data with local label differential privacy,”
arXiv preprint arXiv:2205.08886, 2022.

[191] M. Vinaroz, M.-A. Charusaie, F. Harder, K. Adamczewski, and M. J.
Park, “Hermite polynomial features for private data generation,” in
International Conference on Machine Learning. PMLR, 2022.
[192] F. Harder, K. Adamczewski, and M. Park, “Dp-merf: Differentially
private mean embeddings with randomfeatures for practical privacy-
preserving data generation,” in International conference on artificial
intelligence and statistics. PMLR, 2021.

[193] R. Chen, Q. Xiao, Y. Zhang, and J. Xu, “Differentially private high-
dimensional data publication via sampling-based inference,” in ACM
SIGKDD international conference on knowledge discovery and data
mining, 2015.

[194] K. Cai, X. Lei, J. Wei, and X. Xiao, “Data synthesis via differentially
private markov random fields,” VLDB Endowment, vol. 14, no. 11, pp.
2190–2202, 2021.

[195] R. McKenna, B. Mullins, D. Sheldon, and G. Miklau, “Aim: An
adaptive and iterative mechanism for differentially private synthetic
data,” arXiv preprint arXiv:2201.12677, 2022.

[196] C.-H. Lin, C.-M. Yu, and C.-Y. Huang, “Dpview: Differentially private
data synthesis through domain size information,” IEEE Internet of
Things Journal, vol. 9, no. 17, pp. 15 886–15 900, 2022.

[197] V. Chandrasekaran, D. Edge, S. Jha, A. Sharma, C. Zhang, and
S. Tople, “Causally constrained data synthesis for private data release,”
arXiv preprint arXiv:2105.13144, 2021.

[198] J. Zhang, G. Cormode, C. M. Procopiuc, D. Srivastava, and X. Xiao,
“Privbayes: Private data release via bayesian networks,” ACM Trans-
actions on Database Systems (TODS), vol. 42, no. 4, pp. 1–41, 2017.
[199] C. Ge, S. Mohapatra, X. He, and I. F. Ilyas, “Kamino: Constraint-aware
differentially private data synthesis,” arXiv preprint arXiv:2012.15713,
2020.

[200] M. Gaboardi, E. J. G. Arias, J. Hsu, A. Roth, and Z. S. Wu, “Dual
query: Practical private query release for high dimensional data,” in
International Conference on Machine Learning, 2014.

[201] M. Hardt, K. Ligett, and F. McSherry, “A simple and practical algorithm
for differentially private data release,” Advances in neural information
processing systems, 2012.

[202] Z. Zhang, T. Wang, N. Li, J. Honorio, M. Backes, S. He, J. Chen,
and Y. Zhang, “{PrivSyn}: Differentially private data synthesis,” in
USENIX Security Symposium, 2021.

[203] Q. Chen, C. Xiang, M. Xue, B. Li, N. Borisov, D. Kaarfar, and
H. Zhu, “Differentially private data generative models,” arXiv preprint
arXiv:1812.02274, 2018.

[204] E. Bao, X. Xiao, J. Zhao, D. Zhang, and B. Ding, “Synthetic data
generation with differential privacy via bayesian networks,” Journal of
Privacy and Confidentiality, 2021.

[205] F. Liu, Z. Cheng, H. Chen, Y. Wei, L. Nie, and M. Kankanhalli,
“Privacy-preserving synthetic data generation for recommendation sys-
tems,” in ACM SIGIR Conference on Research and Development in
Information Retrieval, 2022.

[206] J.-W. Chen, C.-M. Yu, C.-C. Kao, T.-W. Pang, and C.-S. Lu, “Dpgen:
Differentially private generative energy-guided network for natural
image synthesis,” in IEEE/CVF Conference on Computer Vision and
Pattern Recognition, 2022.

---

<!-- PAGE 18 -->

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021

18

private fine-tuning of language models,” in International Conference
on Learning Representations, 2021.

[232] W. Wei and L. Liu, “Trustworthy distributed ai systems: Robustness,

privacy, and governance,” ACM Computing Surveys, 2024.

[233] B. Oprisanu, G. Ganev, and E. De Cristofaro, “Measuring utility and
privacy of synthetic genomic data,” arXiv preprint arXiv:2102.03314,
2021.

[234] M. Pereira, M. Kshirsagar, S. Mukherjee, R. Dodhia, and J. Ferres, “An
analysis of the deployment of models trained on private tabular syn-
thetic data: Unexpected surprises,” arXiv preprint arXiv:2106.10241.
[235] G. Ganev, B. Oprisanu, and E. De Cristofaro, “Robin hood and matthew
effects: Differential privacy has disparate impact on synthetic data,” in
International Conference on Machine Learning. PMLR, 2022.
[236] N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman, and A. Galstyan,
“A survey on bias and fairness in machine learning,” ACM Computing
Surveys (CSUR), vol. 54, no. 6, pp. 1–35, 2021.

[237] A. Abusitta, E. A¨ımeur, and O. A. Wahab, “Generative adversarial
networks for mitigating biases in machine learning systems,” arXiv
preprint arXiv:1905.09972, 2019.

[238] F. H. K. d. S. Tanaka and C. Aranha, “Data augmentation using gans,”

arXiv preprint arXiv:1904.09135, 2019.

[239] G. Mariani, F. Scheidegger, R. Istrate, C. Bekas, and C. Malossi,
“Bagan: Data augmentation with balancing gan,” arXiv preprint
arXiv:1803.09655, 2018.

[240] E. Barbierato, M. L. D. Vedova, D. Tessera, D. Toti, and N. Vanoli,
“A methodology for controlling bias and fairness in synthetic data
generation,” Applied Sciences, vol. 12, no. 9, p. 4619, 2022.

[241] D. Xu, S. Yuan, L. Zhang, and X. Wu, “Fairgan: Fairness-aware
generative adversarial networks,” in IEEE International Conference on
Big Data, 2018.

[242] P. Sattigeri, S. C. Hoffman, V. Chenthamarakshan, and K. R. Varshney,
“Fairness gan: Generating datasets with fairness properties using a
generative adversarial network,” IBM Journal of Research and Devel-
opment, vol. 63, no. 4/5, pp. 3–1, 2019.

[243] B. Van Breugel, T. Kyono, J. Berrevoets, and M. Van der Schaar,
“Decaf: Generating fair synthetic data using causally-aware genera-
tive networks,” Advances in Neural Information Processing Systems,
vol. 34, 2021.

[244] E. Bagdasaryan, O. Poursaeed, and V. Shmatikov, “Differential privacy
has disparate impact on model accuracy,” Advances in neural informa-
tion processing systems, vol. 32, 2019.

[245] L. Weidinger, J. Mellor, M. Rauh, C. Griffin, J. Uesato, P.-S. Huang,
M. Cheng, M. Glaese, B. Balle, A. Kasirzadeh et al., “Ethical and social
risks of harm from language models,” arXiv preprint arXiv:2112.04359,
2021.

[246] G. K. Anumanchipalli, J. Chartier, and E. F. Chang, “Speech synthesis
from neural decoding of spoken sentences,” Nature, vol. 568, no. 7753,
pp. 493–498, 2019.

[247] C. Yan, Y. Yan, Z. Wan, Z. Zhang, L. Omberg, J. Guinney, S. D.
Mooney, and B. A. Malin, “A multifaceted benchmarking of synthetic
electronic health record generation models,” Nature Communications,
vol. 13, no. 1, pp. 1–18, 2022.

[248] C. Esteban, S. L. Hyland, and G. R¨atsch, “Real-valued (medical)
time series generation with recurrent conditional gans,” arXiv preprint
arXiv:1706.02633, 2017.

[249] Z. Zhao, F. Zhou, Z. Zeng, C. Guan, and S. K. Zhou, “Meta-
hallucinator: Towards few-shot cross-modality cardiac image segmenta-
tion,” in Medical Image Computing and Computer Assisted Intervention
(MICCAI). Springer, 2022.

[250] H. Huang, K. Mehrotra, and C. K. Mohan, “Rank-based outlier
detection,” Journal of Statistical Computation and Simulation, vol. 83,
no. 3, pp. 518–531, 2013.

[207] Z. Zhang, T. Wang, N. Li, S. He, and J. Chen, “Calm: Consistent
adaptive local marginal for marginal release under local differential
privacy,” in ACM SIGSAC Conference on Computer and Communica-
tions Security, 2018.

[208] W. Qardaji, W. Yang, and N. Li, “Priview: practical differentially
private release of marginal contingency tables,” in ACM SIGMOD
international conference on Management of data, 2014.

[209] L. Sweeney, “k-anonymity: A model for protecting privacy,” Interna-
tional journal of uncertainty, fuzziness and knowledge-based systems,
vol. 10, no. 05, pp. 557–570, 2002.

[210] P. Samarati and L. Sweeney, “Generalizing data to provide anonymity
when disclosing information,” in ACM SIGACT-SIGMOD-SIGART
Symposium on Principles of Database Systems, 1998.

[211] P. Samarati, “Protecting respondents identities in microdata release,”
IEEE transactions on Knowledge and Data Engineering, vol. 13, no. 6,
pp. 1010–1027, 2001.

[212] B. Barak, K. Chaudhuri, C. Dwork, S. Kale, F. McSherry, and
K. Talwar, “Privacy, accuracy, and consistency too: a holistic solution
to contingency table release,” in ACM SIGMOD-SIGACT-SIGART
symposium on Principles of database systems, 2007.

[213] J. C. Duchi, M. I. Jordan, and M. J. Wainwright, “Local privacy and
statistical minimax rates,” in IEEE Annual Symposium on Foundations
of Computer Science, 2013.

[214] S.-Y. Kung, “Compressive privacy: From information\/estimation the-
ory to machine learning,” IEEE Signal Processing Magazine, vol. 34,
no. 1, pp. 94–112, 2017.

[215] H. Li, L. Xiong, and X. Jiang, “Differentially private synthesization
of multi-dimensional data using copula functions,” in International
Conference on Extending Database Technology. NIH Public Access,
2014.

[216] N. Patki, R. Wedge, and K. Veeramachaneni, “The synthetic data
vault,” in IEEE international conference on data science and advanced
analytics (DSAA).

IEEE, 2016.

[217] S. Gambs, F. Ladouceur, A. Laurent, and A. Roy-Gaumond, “Growing
synthetic data through differentially-private vine copulas,” Proceedings
on Privacy Enhancing Technologies, 2021.

[218] H. J. Asghar, M. Ding, T. Rakotoarivelo, S. Mrabet, and M. A. Kaafar,
“Differentially private release of high-dimensional datasets using the
gaussian copula,” arXiv preprint arXiv:1902.01499, 2019.

[219] T. Rekatsinas, X. Chu, I. F. Ilyas, and C. R´e, “Holoclean: Holistic data
repairs with probabilistic inference,” arXiv preprint arXiv:1702.00820,
2017.

[220] H. Wang, S. Sudalairaj, J. Henning, K. Greenewald, and A. Srivastava,
“Post-processing private synthetic data for improving utility on selected
measures,” Advances in Neural Information Processing Systems, 2024.
[221] N. Carlini, F. Tramer, E. Wallace, M. Jagielski, A. Herbert-Voss,
K. Lee, A. Roberts, T. B. Brown, D. Song, U. Erlingsson et al.,
“Extracting training data from large language models.” in USENIX
Security Symposium, 2021.

[222] N. Carlini, J. Hayes, M. Nasr, M. Jagielski, V. Sehwag, F. Tramer,
B. Balle, D. Ippolito, and E. Wallace, “Extracting training data from
diffusion models,” arXiv preprint arXiv:2301.13188, 2023.

[223] C. Meehan, K. Chaudhuri, and S. Dasgupta, “A non-parametric test to
detect data-copying in generative models,” in International Conference
on Artificial Intelligence and Statistics, 2020.

[224] Q. Feng, C. Guo, F. Benitez-Quiroz, and A. M. Martinez, “When
do gans replicate? on the choice of dataset size,” in IEEE/CVF
International Conference on Computer Vision, 2021.

[225] N. Kandpal, E. Wallace, and C. Raffel, “Deduplicating training data
mitigates privacy risks in language models,” in International Confer-
ence on Machine Learning. PMLR, 2022.

[226] T. Dockhorn, T. Cao, A. Vahdat, and K. Kreis, “Differentially private

diffusion models,” arXiv preprint arXiv:2210.09929, 2022.

[227] Y.-L. Tsai, Y. Li, Z. Chen, P.-Y. Chen, C.-M. Yu, X. Ren, and F. Buet-
Golfouse, “Differentially private fine-tuning of diffusion models,” arXiv
preprint arXiv:2406.01355, 2024.

[228] H. Wang, S. Pang, Z. Lu, Y. Rao, Y. Zhou, and M. Xue, “dp-
promise: Differentially private diffusion probabilistic models for image
synthesis,” in USENIX Security Symposium, 2024.

[229] S. Lyu, M. F. Liu, M. Vinaroz, and M. Park, “Differentially private
latent diffusion models,” arXiv preprint arXiv:2305.15759, 2023.
[230] J. Lebensold, M. Sanjabi, P. Astolfi, A. Romero-Soriano, K. Chaudhuri,
M. Rabbat, and C. Guo, “Dp-rdm: Adapting diffusion models to private
domains without fine-tuning,” arXiv preprint arXiv:2403.14421, 2024.
[231] D. Yu, S. Naik, A. Backurs, S. Gopi, H. A. Inan, G. Kamath,
J. Kulkarni, Y. T. Lee, A. Manoel, L. Wutschitz et al., “Differentially

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 1
Machine Learning for Synthetic Data Generation:
A Review
Yingzhou Lu§, Lulu Chen††, Yuanyuan Zhang‡‡, Minjie Shen†, Huazheng Wang‡, Xiao Wang∥, Capucine van
Rechem§, Tianfan Fu∗, Wenqi Wei∗∗¶
Abstract—Machine learning heavily relies on data, but real- Nonetheless, it is important to recognize that machine
world applications often encounter various data-related issues. learning does not invariably resolve problems or yield the
Theseincludedataofpoorquality,insufficientdatapointsleading optimal solution. Despite artificial intelligence is currently
to under-fitting of machine learning models, and difficulties in
experiencing a golden age, numerous challenges persist in
data access due to concerns surrounding privacy, safety, and
regulations. In light of these challenges, the concept of synthetic the development and application of machine learning technol-
data generation emerges as a promising alternative that allows ogy [4]. As the field continues to advance, addressing these
for data sharing and utilization in ways that real-world data obstacles will be essential for unlocking the full potential of
cannotfacilitate.Thispaperpresentsacomprehensivesystematic
machine learning and its transformative impact on various
review of existing studies that employ machine learning models
industries.
for the purpose of generating synthetic data. The review en-
compasses various perspectives, starting with the applications The process of collecting and annotating data is both time-
of synthetic data generation, spanning computer vision, speech, consuming and expensive [5], giving rise to numerous issues.
natural language processing, healthcare, and business domains. As machine learning is heavily dependent on data, some of
Additionally, it explores different machine learning methods,
the key hurdles and challenges it faces include:
with particular emphasis on neural network architectures and
deep generative models. The paper also addresses the crucial • Data quality. Ensuring data quality is one of the most
aspects of privacy and fairness concerns related to synthetic significant challenges confronting machine learning profes-
datageneration.Furthermore,thisstudyidentifiesthechallenges
sionals.Whendataisofsubparquality,modelsmaygenerate
andopportunitiesprevalentinthisemergingfield,sheddinglight
incorrect or imprecise predictions due to confusion and
on the potential avenues for future research. By delving into
the intricacies of synthetic data generation, this paper aims to misinterpretation [6] [7].
contribute to the advancement of knowledge and inspire further • Data scarcity. A considerable portion of the contemporary
exploration in synthetic data generation. AI dilemma stems from inadequate data availability: either
Index Terms—data synthesis, machine learning, generative the number of accessible datasets is insufficient, or manual
modeling labeling is excessively costly [8].
• Data privacy and fairness. There are many areas in which
datasets cannot be publicly released due to privacy ad fair
I. INTRODUCTION
issues. In these cases, generating synthetic data can be very
MACHINElearningendowsintelligentcomputersystems useful,andwewillinvestigatewaysofcreatinganonymized
withthecapacitytoautonomouslytackletasks,pushing datasets with differential privacy protections.
the envelope of industrial innovation [1]. By integrating high- Tacklingtheseissuesiscrucialtofullyrealizingthetransfor-
performance computing, contemporary modeling, and simu- mative power of machine learning across diverse sectors [9]–
lations, machine learning has evolved into an indispensable [11]. Generally, synthetic data are defined as the artificially
instrument for managing and analyzing massive volumes of annotated information generated by computer algorithms or
data [2], [3]. simulations [4], [12]. In many cases, synthetic data is nec-
essary when real data is either unavailable or must be kept
§DepartmentofPathology,StanfordUniversity,Stanford,CA,94305.
††DepartmentofElectricalandComputerEngineering,VirginiaPolytechnic private due to privacy or compliance risks [10], [13], [14].
InstituteandStateUniversity,Arlington,VA22203,USA. Thistechnologyisextensivelyutilizedinvarioussectors,such
‡‡DepartmentofComputerScienceofPurdueUniversity,WestLafayette,IN
as healthcare, business, manufacturing, and agriculture, with
47907,USA.
†The Bradley Department of Electrical and Computer Engineering, Virginia demand growing at an exponential rate [15].
Tech The objective of this paper is to offer a high-level overview
‡School of Electrical Engineering and Computer Science, Oregon State of several state-of-the-art approaches currently being inves-
University,Corvallis,OR,97331.
∥ tigated by machine learning researchers for synthetic data
School of Computer Science & Engineering, University of Washington,
Seattle,WA,98105. generation. For the reader’s convenience, we summarize the
∗ComputerScienceDepartment,RensselaerPolytechnicInstitute,Troy,NY,
paper’s main contributions as follows:
12180.
∗∗ComputerandInformationScienceDepartment,FordhamUniversity,New • We present pertinent ideas and background information
YorkCity,NY,10023. on synthetic data, serving as a guide for researchers
¶Correspondingauthor.
interested in this domain.
E-mails:wenqiwei@fordham.edu.
Manuscriptreceivedxxxxxx,xxxx;revisedxxxxxxx,xxxx. • We explore different real-world application domains and
5202
rpA
4
]GL.sc[
01v26040.2032:viXra

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     | 2   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.1. Syntheticdatageneration.
emphasize the range of opportunities that GANs and Sankaranarayanan et al. introduced a generative adversarial
synthetic data generation can provide in bridging gaps network (GAN) that narrows the gap between embeddings in
(Section II). the learned feature space, facilitating Visual Domain Adap-
• We examine a diverse array of deep generative mod- tation [55]. This approach enables semantic segmentation
els dedicated to generating high-quality synthetic data, acrossdifferentdomains.TheGANusesageneratortoproject
presentadvancedgenerativemodels,andoutlinepotential features onto the image space, which the discriminator subse-
avenues for future research (Section III). quently operates on. Adversarial losses can be derived from
We address privacy and fairness concerns, as sensitive the discriminator’s output [56]. Notably, applying adversarial
•
information can be inferred from synthesized data, and losses to the projected image space has been shown to yield
biases embedded in real-world data can be inherited. significantly better performance compared to applying them
We review current technological advancements and their directly to the feature space [55].
limitations in safeguarding data privacy and ensuring the In a recent study, a Microsoft research team demonstrated
fairness of synthesized data (Section IV and V). the effectiveness of synthetic data in face-related tasks by
• We outline several general evaluation strategies to assess combining a parametric 3D face model with an extensive
the quality of synthetic data (Section VI). library of hand-crafted assets [57]. This approach rendered
• We identify challenges faced in generating synthetic data training images with remarkable realism and diversity. The
and during the deployment process, highlighting poten- researchers trained machine learning systems for tasks such
tial future work that could further enhance functionality as landmark localization and face parsing using synthetic
(Section VII). data, showing that it can achieve comparable accuracy to real
|           |             |     |             |               |             | data. Furthermore, |       | synthetic        |     | data alone | proved | sufficient | for |
| --------- | ----------- | --- | ----------- | ------------- | ----------- | ------------------ | ----- | ---------------- | --- | ---------- | ------ | ---------- | --- |
|           |             |     |             |               |             | detecting          | faces | in unconstrained |     | settings   | [57].  |            |     |
|           |             | II. | APPLICATION |               |             |                    |       |                  |     |            |        |            |     |
| Synthetic | data offers | a   | multitude   | of compelling | advantages, |                    |       |                  |     |            |        |            |     |
B. Voice
| making it | a highly | appealing | option | for | a wide range | of  |     |     |     |     |     |     |     |
| --------- | -------- | --------- | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
applications.Bystreamliningtheprocessesoftraining,testing, The field of synthetic voice is at the forefront of tech-
|               |     |            |           |      |             | nological | advancement, |     | and | its evolution | is  | happening | at a |
| ------------- | --- | ---------- | --------- | ---- | ----------- | --------- | ------------ | --- | --- | ------------- | --- | --------- | ---- |
| and deploying | AI  | solutions, | synthetic | data | facilitates | more      |              |     |     |               |     |           |      |
efficient and effective development. Furthermore, this cutting- breakneck pace. With the advent of machine learning and
edge technology reduces the risk of exposing sensitive infor- deep learning, creating synthetic voices for various applica-
mation, thereby ensuring customer security and privacy [4]. tions such as video production, digital assistants, and video
Asresearcherstransitionsyntheticdatafromthelabtoprac- games [58] has become easier and more accurate. This field
|                        |     |     |            |              |          | is an intersection |     | of  | diverse | disciplines, | including | acoustics, |     |
| ---------------------- | --- | --- | ---------- | ------------ | -------- | ------------------ | --- | --- | ------- | ------------ | --------- | ---------- | --- |
| tical implementations, |     | its | real-world | applications | continue | to                 |     |     |         |              |           |            |     |
broaden. This section explores several notable domains where linguistics, and signal processing. Researchers in this area
syntheticdatagenerationsubstantiallyimpactsaddressingreal- continuously strive to improve synthetic voices’ accuracy and
world challenges. naturalness. As technology advances, we can expect to see
syntheticvoicesbecomeevenmoreprevalentinourdailylives,
|     |     |     |     |     |     | assisting | us in | various | ways | and enriching | our | experiences | in  |
| --- | --- | --- | --- | --- | --- | --------- | ----- | ------- | ---- | ------------- | --- | ----------- | --- |
A. Vision
|     |     |     |     |     |     | many fields | [59]. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
Supervised learning relies heavily on the availability of la- The earlier study includes spectral modeling for statis-
beleddata[51].However,inmanyapplications,particularlyin tical parametric speech synthesis, in which low-level, un-
computervision,manuallabelingisoftennecessary[52],[53]. transformed spectral envelope parameters are used for voice
Taskssuchassegmentation,depthestimation,andopticalflow synthesis. The low-level spectral envelopes are represented
estimation can be exceedingly challenging to label manually. by graphical models incorporating multiple hidden variables,
Syntheticdatahasemergedasatransformativesolutioninthis such as restricted Boltzmann machines and deep belief
context, significantly improving the labeling process [54]. networks (DBNs) [60]. The proposed conventional hidden

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 3
TABLEI
SUMMARIZATIONOFREPRESENTATIVEWORKSINSYNTHETICDATAGENERATION.
| Paper | Application | GenerativeAI | DNN |     | Dataset |     |
| ----- | ----------- | ------------ | --- | --- | ------- | --- |
MedGAN[16] healthcare GAN MLP MIMIC/Sutter (Electronic health
record)
| MMCGAN[17] | healthcare&CV | GAN | CNN |     | chestCTimages |     |
| ---------- | ------------- | --- | --- | --- | ------------- | --- |
DeepSynth[18] healthcare&CV GAN CNN ratkidneytissue(microscopeimage)
| ChemSpaceE[19] | drug | VAE | GNN         |     | ZINC(drugmolecule)[20]  |     |
| -------------- | ---- | --- | ----------- | --- | ----------------------- | --- |
| JTVAE[21]      | drug | VAE | GNN         |     | ZINC(drugmolecules)[20] |     |
| REINVENT[22]   | drug | RL  | RNN         |     | ZINC(drugmolecules)[20] |     |
| CORE[23]       | drug | VAE | GNN         |     | ZINC(drugmolecule)[20]  |     |
| RGA[24]        | drug | RL  | geometricNN |     | ZINCandTDC[25]          |     |
CorGAN[26] healthcare GAN CNN MIMIC-III dataset, UCI Epileptic
SeizureRecognitiondataset
DAAE[27] healthcare VAE+GAN recurrentautoencoder MIMIC-III, UT Physicians clinical
databases
HAPNEST[28] healthcare approximate Bayesian compu- NA(w.o.DNN) GenomesProjectandHGDPdatasets
tation(notdeeplearning)
synthpop[29] healthcare propersynthesis Statisticalhypothesistesting SD2011
| CycleGAN[30] | vision | GAN | CNN           |     | pix2pix  |     |
| ------------ | ------ | --- | ------------- | --- | -------- | --- |
| DP-CGAN[31]  | vision | GAN | deepCGAN      |     | MNIST    |     |
| BigGANs[32]  | vision | GAN | largescaleGAN |     | ImageNet |     |
VideoDiff[33] vision diffusion CNN BAIRRobotPushing,Kinetics-600
| VQ-VAE[34]  | vision | VAE | PixelCNN |     | ImageNet       |               |
| ----------- | ------ | --- | -------- | --- | -------------- | ------------- |
| GIRAFFE[35] | vision | GAN | CNN      |     | CompCars, LSUN | Churches, and |
FFHQ
| Wavegrad[36]   | TTS          | diffusion                  | gradient-basedsampling |     | LJSpeech                 |     |
| -------------- | ------------ | -------------------------- | ---------------------- | --- | ------------------------ | --- |
| TTS-GAN[37]    | TTS          | GAN                        | auto-regressivemodel   |     | Tacotron2                |     |
| Seq-GAN[38]    | NLP          | GAN+RL                     | CNN                    |     | Nottinghamdataset        |     |
| BLEURT[39]     | NLP          | Languagemodel              | BERT                   |     | WebNLGCompetitiondataset |     |
| TextGen-RL[40] | NLP          | RL                         | LSTM                   |     |                          |     |
| SynBench[41]   | NLP          | conditionalGaussianmixture |                        |     | CIFAR10                  |     |
| RelGAN[42]     | imageandtext | GAN                        | CNN                    |     | COCOImageCaptionsdataset |     |
DPGM[43] audioandtext generativeartificialneuralnet- differentiallyprivatekernelk- MNIST, anonymized Call Detail
|             |       | works | means |     | Record(CDR)           |                |
| ----------- | ----- | ----- | ----- | --- | --------------------- | -------------- |
| WaveGAN[44] | audio | GAN   | DCGAN |     | SpeechCommandsDataset |                |
| Wavenet[45] | audio | GAN   | LSTM  |     | CSTR voice corpula    | (multi-channel |
Englishaudio)
Stutter-TTS[46] audio phonetic encoder and the de- CNN recordings
coder
QuantGANs[47] business GAN MLP+ Temporal convolu- simulateddata
tionalnetworks(TCN)
| CGAN[48] | business | GAN | CNN |     | Vectorautoregressive(VAR)timese- |     |
| -------- | -------- | --- | --- | --- | -------------------------------- | --- |
ries
| PATE-GAN[49] | business | GAN | Private | Aggregation | of Kaggle |     |
| ------------ | -------- | --- | ------- | ----------- | --------- | --- |
TeacherEnsembles(PATE)
| CollGAN[50] | physics (particle | VAE/GAN | MLP |     | ATLAS |     |
| ----------- | ----------------- | ------- | --- | --- | ----- | --- |
collision)
Markov model (HMM)-based speech synthesis system can the field of natural language processing (NLP) [51]. In recent
be significantly improved in terms of naturalness and over- years, a multitude of methods and models have illustrated
smoothing [61]. the capabilities of machine learning in categorizing, routing,
Synthetic data can also be applied to Text-to-Speech (TTS) filtering,andsearchingforrelevantinformationacrossvarious
| toachievenear-humannaturalness[62],[63].Asanalternative |     |     | domains | [64]. |     |     |
| ------------------------------------------------------- | --- | --- | ------- | ----- | --- | --- |
to sparse or limited data, synthetic speech (SynthASR) was Despite these advancements, challenges remain. For exam-
developed for automatic speech recognition. The combination ple, the meaning of words and phrases can change depending
of weighted multi-style training, data augmentation, encoder on their context, and homonyms with distinct definitions can
freezing, and parameter regularization is also employed to poseadditionaldifficulties[65].Totacklethesechallenges,the
address catastrophic forgetting. Using this novel model, the BLEURT model was proposed, which models human judg-
researchers were able to apply state-of-the-art techniques to ments using a limited number of potentially biased training
train a wide range of end-to-end (E2E) automatic speech examples based on BERT. The researchers employed millions
recognition (ASR) models while reducing the need for pro- of synthetic examples to develop an innovative pre-training
duction data and the costs associated with it [62]. scheme, bolstering the model’s ability to generalize [66],
[67].ExperimentalresultsindicatethatBLEURTsurpassesits
|                     |            |       | counterparts | on both | the WebNLG Competition | dataset and |
| ------------------- | ---------- | ----- | ------------ | ------- | ---------------------- | ----------- |
| C. Natural Language | Processing | (NLP) |              |         |                        |             |
theWMTMetrics,highlightingitsefficacyinNLPtasks[39].
The increasing interest in synthetic data has spurred the Another significant breakthrough in text generation using
development of a wide array of deep generative models in GANs is RelGAN, developed by Rice University. This model

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |             |           |            |     |      |           |                | 4   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------- | --- | ---- | --------- | -------------- | --- |
|                                                 |     |     |     |     |     |     |     | essentially | molecular | structures |     | with | desirable | pharmaceutical |     |
properties.Thegoalofdenovodrugdesignistoproducenovel
|     |     |     |     |     |     |     |     | and desirable   |        | molecule     | structures     |            | from scratch. |       | The word     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ------------ | -------------- | ---------- | ------------- | ----- | ------------ |
|     |     |     |     |     |     |     |     | “de novo”       | means  | from         | the beginning. |            | The           | whole | molecule     |
|     |     |     |     |     |     |     |     | space is        | around | 1060         | [25], [76],    | [77].      | Most          | of    | the existing |
|     |     |     |     |     |     |     |     | methods         | rely   | heavily      | on brute-force |            | enumeration   |       | and are      |
|     |     |     |     |     |     |     |     | computationally |        | prohibitive. |                | Generative | models        |       | are able to  |
learnthedistributionofdrugmoleculesfromtheexistingdrug
|     |     |     |     |     |     |     |     | database       | and then  | draw     | novel         | samples        | (i.e.,     | drug         | molecules)  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | -------- | ------------- | -------------- | ---------- | ------------ | ----------- |
|     |     |     |     |     |     |     |     | from the       | learned   | molecule | distribution, |                | including  |              | variational |
|     |     |     |     |     |     |     |     | autoencoder    | (VAE)     | [21],    | [78],         | [79],          | generative |              | adversarial |
|     |     |     |     |     |     |     |     | network        | (GAN)     | [80],    | energy-based  |                | model      | (EBM)        | [81], [82], |
|     |     |     |     |     |     |     |     | diffusion      | model     | [83],    | reinforcement |                | learning   | (RL)         | [22], [24], |
|     |     |     |     |     |     |     |     | [84], genetic  | algorithm |          | [85],         | sampling-based |            | methods      | [86],       |
|     |     |     |     |     |     |     |     | [87], etc.     |           |          |               |                |            |              |             |
|     |     |     |     |     |     |     |     | In healthcare, |           | patient  | information   |                | is often   | stored       | in elec-    |
|     |     |     |     |     |     |     |     | tronic health  | records   |          | (EHR)         | format         | [88]–[90]. |              | Research in |
|     |     |     |     |     |     |     |     | medicine       | has been  | greatly  | facilitated   |                | by the     | availability | of in-      |
formationfromelectronichealthrecords[91],[92].MedGAN,
|     |     |     |     |     |     |     |     | an adversarial |             | network | model     | for      | generating | realistic    | syn-  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | ------- | --------- | -------- | ---------- | ------------ | ----- |
|     |     |     |     |     |     |     |     | thetic patient | records,    |         | has been  | proposed |            | by Edward    | Choi  |
|     |     |     |     |     |     |     |     | and other      | colleagues. |         | With the  | help     | of an      | autoencoder  | and   |
|     |     |     |     |     |     |     |     | generative     | adversarial |         | networks, | medGAN   |            | can generate | high- |
dimensionaldiscretevariables(e.g.,binaryandcountfeatures)
Fig.2. Syntheticdataapplications
|                  |          |                  |             |     |              |                    |      | based on           | real      | patient     | records    | [16].        | Based       | on         | their evalua- |
| ---------------- | -------- | ---------------- | ----------- | --- | ------------ | ------------------ | ---- | ------------------ | --------- | ----------- | ---------- | ------------ | ----------- | ---------- | ------------- |
|                  |          |                  |             |     |              |                    |      | tions of           | medGAN’s  | performance |            | on           | a set       | of diverse | tasks         |
| is comprised     | of       | three main       | components: |     | a relational | memory-            |      |                    |           |             |            |              |             |            |               |
|                  |          |                  |             |     |              |                    |      | reported,          | including | reporting   |            | distribution | statistics, |            | classifica-   |
| based generator, |          | a Gumbel-Softmax |             |     | relaxation   | algorithm,         | and  |                    |           |             |            |              |             |            |               |
|                  |          |                  |             |     |              |                    |      | tion performance   |           | [93],       | and expert | review,      |             | medGAN     | exhibits      |
| multiple         | embedded | representations  |             |     | within       | the discriminator. |      |                    |           |             |            |              |             |            |               |
|                  |          |                  |             |     |              |                    |      | close-to-real-time |           | performance |            | [16],        | [94]–[97].  |            | Using syn-    |
| When benchmarked |          | against          | several     |     | cutting-edge | models,            | Rel- |                    |           |             |            |              |             |            |               |
|                  |          |                  |             |     |              |                    |      | thetic data        | can       | help reduce | the        | regulatory   |             | barriers   | preventing    |
GANdemonstratessuperiorperformanceintermsofsampling
|                |            |             |           |           |               |        |         | the widespread |                | sharing | and integration |            | of        | patient  | data across  |
| -------------- | ---------- | ----------- | --------- | --------- | ------------- | ------ | ------- | -------------- | -------------- | ------- | --------------- | ---------- | --------- | -------- | ------------ |
| quality and    | diversity. | This        | showcases |           | its potential | for    | further |                |                |         |                 |            |           |          |              |
|                |            |             |           |           |               |        |         | multiple       | organizations  |         | in the          | past       | [98],     | [99].    | Researchers  |
| investigation  | and        | application |           | in a wide | range         | of NLP | tasks   |                |                |         |                 |            |           |          |              |
|                |            |             |           |           |               |        |         | across the     | globe          | would   | be able         | to request |           | access   | to synthetic |
| and challenges | [42],      | [68].       |           |           |               |        |         |                |                |         |                 |            |           |          |              |
|                |            |             |           |           |               |        |         | data from      | an institution |         | to conduct      |            | their own | research | using        |
thedata.Suchcapabilitiescanincreaseboththeefficiencyand
D. Healthcare
|     |     |     |     |     |     |     |     | scope of | the study | as  | well as | reduce | the likelihood |     | of biases |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ------- | ------ | -------------- | --- | --------- |
In order to protect health information and improve repro- being introduced into the results [70], [100], [101].
| ducibility    | in research, |            | synthetic | data     | has   | drawn mainstream |      |             |     |     |     |     |     |     |     |
| ------------- | ------------ | ---------- | --------- | -------- | ----- | ---------------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| attention     | in the       | healthcare |           | industry | [69], | [70]. Many       | labs |             |     |     |     |     |     |     |     |
|               |              |            |           |          |       |                  |      | E. Business |     |     |     |     |     |     |     |
| and companies |              | have       | harnessed | the      | tools | of big data      | and  |             |     |     |     |     |     |     |     |
advanced computation tools to produce large quantities of The inherent risk of compromising or exposing original
syntheticdata,ordigitaltwin[71],[72].Modeledafterpatient data persists as long as it remains in use, particularly in the
data, synthetic data generation is essential to understanding businesssector,wheredatasharingisheavilyconstrainedboth
diseases while maintaining patient confidentiality and privacy within and outside the organization [102]. Consequently, it is
|                |     |                      |     |     |           |          |         | crucial to | explore | methods | for | generating |     | financial | datasets |
| -------------- | --- | -------------------- | --- | --- | --------- | -------- | ------- | ---------- | ------- | ------- | --- | ---------- | --- | --------- | -------- |
| simultaneously |     | [73]. Theoretically, |     |     | synthetic | data can | reflect |            |         |         |     |            |     |           |          |
the original distribution of the data instead of revealing actual that emulate the properties of ”real data” while maintaining
patient data [73]–[75]. the privacy of the involved parties [102].
Synthetic data generation can also be utilized to discover Efforts have been made to secure original data using
new scientific principles by grounding it in biological pri- technologieslikeencryption, anonymization,andcutting-edge
|           |       |      |      |        |        |           |     | privacy | preservation |     | [103]. | However, | information |     | gleaned |
| --------- | ----- | ---- | ---- | ------ | ------ | --------- | --- | ------- | ------------ | --- | ------ | -------- | ----------- | --- | ------- |
| ors [69]. | There | have | been | a good | number | of models | and |         |              |     |        |          |             |     |         |
software developed, such as SynSys, which uses hidden from the data may still be employed to trace individuals,
Markovmodelsandregressionmodelsinitiallytrainedonreal therebyposingtherisk[104].Anotableadvantageofsynthetic
datasets to generate synthetic time series data consisting of data lies in its ability to eliminate the exposure of critical
nestedsequences[70];andcorGAN,inwhichsyntheticdatais data, thus ensuring privacy and security for both companies
generated by capturing correlations between adjacent medical and their customers [105]. Moreover, synthetic data enables
features in the data representation space [26]. organizations to access data more rapidly, as it bypasses
Syntheticdatagenerationhasalsobeenwidelyusedindrug privacy and security protocols [106]. In the past, institutions
discovery,especiallydenovodrugmoleculardesign.Drugsare possessing extensive data repositories could potentially assist

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 5
decision-makers in resolving a broad spectrum of issues. introduces an N-gram-based method to predict the following
However,accessingsuchdata,evenforinternalpurposes,was position based on previous positions for publishing trajectory.
hinderedbyconfidentialityconcerns.Presently,companiesare Theyexploittheprefixtreetodescribethen-grammodelwhile
harnessing synthetic data to refresh and model original data, combiningitwithdifferentialprivacy[114].[115]extendsthe
generatingcontinuousinsightsthatcontributetoenhancingthe n-grammodelwithlocaldifferentialprivacyand[116]further
organization’s performance [4]. replaces the n-gram model with key movement mobility for
differentially private trajectory generation. By comparison,
F. Education [117] proposes a synthetic trajectory strategy based on the
Synthetic data is gaining increasing attention in the field of discretization of raw trajectories using hierarchical reference
education due to its vast potential for research and teaching. systems to capture individual movements at differing speeds.
Synthetic data refers to computer-generated information that Their method adaptively selects a small set of reference
mimics the properties of real-world data without disclosing systems and constructs prefix tree counts with differential
any personally identifiable information [107]. This approach privacy.Applyingdirection-weightedsampling,thedecreasein
proves instrumental for educational settings, where ethical treenodesreducestheamountofaddednoiseandimprovesthe
constraints often limit the use of real-world student data. utility of the synthetic data. [118] constructs the differentially
Therefore, synthetic data offers a robust solution for privacy- private prefix tree and calibrates original trajectories against a
concerned data sharing and analysis, enabling the creation selection of anchor points. By extracting multiple differential
of accurate models and strategies to improve the teaching- private distributions with redundant information [119], [120],
learning process. the authors generate a new trajectory with samples from these
A detailed example of synthetic data usage in education is distributions. By comparison, [121] estimates various distri-
thesimulationofstudentperformancedatatoaidindesigning butions of an attribute set to determine trajectories and [122]
teaching strategies. Suppose an educational researcher wants considertheinteractionsbetweendifferentattributesbygroup-
to investigate the impact of teaching styles on student per- ing strongly correlated attributes into non-disjoint sets and
formance across different backgrounds and learning abilities. constructing a corresponding distribution for each set.
However, obtaining real student data for such studies can be In addition to differential privacy, Bindschaedler and
ethicallycomplexandpotentiallyintrusive.Insuchasituation, Shokri[123]enforceplausibledeniabilitytogenerateprivacy-
synthetic data can be generated that mirrors the demographic preserving synthetic traces. It first introduces trace similarity
distributions, learning patterns, and likely performance of and intersection functions that map a fake trace to a real hint
a typical student population. This data can then be used undersimilarityandintersectionconstraints.Then,itgenerates
to model the effects of various teaching strategies without one fake trace by clustering the locations and replacing the
compromising student privacy [108]. trajectory locations with those from the same group. If the
Furthermore,syntheticdatacanbeapowerfultoolinteacher faketracesatisfiesplausibledeniability,i.e.,thereexistkother
training programs. For example, teacher candidates can use realtracesthatcanmaptothefaketrace,thenitpreservesthe
synthetic student data to practice data-driven instructional privacyoftheseedtrace.Whileexistingstudiesmainlyusethe
strategies,includingdifferentiatedinstructionandpersonalized Markovchainmodel,[124]proposesPrivTrace,whichcontrols
learning plans. They can analyze this synthetic data, identify the space and time overhead by the first-order Markov chain
patterns,determinestudentneeds,andadjusttheirinstructional model and achieves good accuracy for next-step prediction
plans accordingly. By using synthetic data, teacher candidates by the second-order Markov chain model. [125] considers the
gain practical experience in analyzing student data and adapt- location synthesizer that generates location traces, including
ing their teaching without infringing on the privacy of actual co-locations of friends, while offering node-level differential
students[109].Thus,syntheticdataservesasavaluablebridge privacy for the friendship and user-level differential privacy
between theory and practice in education, driving innovation for the co-location count matrix.
while safeguarding privacy.
G. Location and Trajectory Generation H. AI-Generated Content (AIGC)
Location and trajectory are a particular form of data that AI-Generated Content (AIGC) stands at the forefront of
could highly reflect users’ daily lives, habits, home addresses, the technology and content creation industry, changing the
workplaces,etc.Toprotectlocationprivacy,syntheticlocation dynamicsofcontentproduction.AtypicalexampleofAIGCis
generation is introduced as opposed to location perturba- OpenAI’sChatGPT,anAI-drivenplatformgeneratinghuman-
tion[110].Themainchallengeofgeneratingsyntheticlocation liketextinresponsetopromptsorquestions.Itleveragesavast
and trajectory data is to resemble genuine user-produced data corpus of internet text to generate detailed responses, often
whileofferingpracticalprivacyprotectionsimultaneously.One indistinguishable from those a human writer would produce.
approach to generating the location and trajectory data is This capacity extends beyond simple question-answer pairs to
to inject a synthetic point-based site within a user’s trajec- crafting whole articles, stories, or technical explanations on a
tory [111], [112]. wide range of topics, thus creating a novel way of producing
Synthetic trajectory generation is frequently combined with blog posts, articles, social media content, etc [126], [127].
privacy-enhancingtechniquestofurtherpreventsensitiveinfer- Google’s Project Bard focuses more on the creative aspects
encefromthesynthesizeddata.Forexample,Chenetal.[113] oftextgeneration.Itisdesignedtogenerateinteractivefiction

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     | 6   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and assist in storytelling. Users can engage in an interactive turnover. By analyzing these models, businesses can develop
dialoguewiththemodel,directingthecourseofanarrativeby strategies to improve employee satisfaction, enhance produc-
providing prompts that the AI responds to, thus co-creating a tivity, and reduce turnover rates. For example, synthetic data
story. This opens up fascinating possibilities for interactive generation can simulate the impact of various HR policies on
entertainment and digital storytelling [128]. workforce morale and performance, helping HR departments
An innovative application of AIGC is in the field of news to implement the most effective practices.
| reporting. | News | agencies | increasingly | use | AI systems, | such |     |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | ------------ | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
as the GPT series, to generate news content. For instance, J. Other Applications
the Associated Press uses AI to generate news articles about The techniques for synthetic data generation described in
corporate earnings automatically. The AI takes structured this paper have far-reaching implications beyond the specific
data about company earnings and transforms it into a brief, domains covered. Here are some notable applications:
coherent, and accurate news report. This automation allows • Retail and Marketing: In retail, synthetic data can model
the agency to cover many companies that would be possible customer interactions, purchasing behaviors, and inventory
| with human | journalists | alone | [129]. |     |     |     |            |        |      |      |               |     |              |     |
| ---------- | ----------- | ----- | ------ | --- | --- | --- | ---------- | ------ | ---- | ---- | ------------- | --- | ------------ | --- |
|            |             |       |        |     |     |     | management | [134]. | This | aids | in developing |     | personalized |     |
Additionally, AIGC has found its place in the creative marketing strategies, optimizing supply chains, and im-
domain, with AI systems being used to generate book de- proving customer service without infringing on individual
| scriptions, | plot | outlines, | and even | full | chapters | of novels. | privacy. |     |     |     |     |     |     |     |
| ----------- | ---- | --------- | -------- | ---- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
For instance, a novelist could use ChatGPT to generate a Environmental Studies: Synthetic data can simulate en-
•
| synopsis | for their | upcoming | book | based | on a few | keywords |             |             |     |         |           |     |                |     |
| -------- | --------- | -------- | ---- | ----- | -------- | -------- | ----------- | ----------- | --- | ------- | --------- | --- | -------------- | --- |
|          |           |          |      |       |          |          | vironmental | conditions, |     | weather | patterns, |     | and ecological |     |
or prompts related to the story. Similarly, marketing teams interactions [135]. This is particularly useful for studying
utilize AI to create compelling product descriptions for online climate change, biodiversity, and conservation efforts, al-
marketplaces [130]. This increases efficiency and provides a lowing researchers to test hypotheses and model practical
level of uniformity and scalability that would be challenging scenarios without the constraints of limited real-world data.
| to achieve | with | human writers | alone. | Looking | forward, | AIGC |                  |     |                  |     |     |       |           |      |
| ---------- | ---- | ------------- | ------ | ------- | -------- | ---- | ---------------- | --- | ---------------- | --- | --- | ----- | --------- | ---- |
|            |      |               |        |         |          |      | • Urban Planning |     | and Development: |     | In  | urban | planning, | syn- |
is profoundly impacting the landscape of content creation and theticdatacanbeusedtosimulatepopulationgrowth,traffic
will continue to shape it in the future [128]. flows, and infrastructure development [136]. This helps city
|     |     |     |     |     |     |     | planners | and developers |                | make | informed |     | decisions       | about |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | -------------- | ---- | -------- | --- | --------------- | ----- |
|     |     |     |     |     |     |     | resource | allocation,    | transportation |      | systems, |     | and sustainable |       |
I. Finance
|     |     |     |     |     |     |     | development | initiatives. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- |
Synthetic data generation offers significant benefits for the • Software Development and Testing: In software develop-
finance industry [104], as detailed below. First, financial data ment,syntheticcodegenerationcansimulatevariouscoding
| is highly | sensitive | and | subject to | stringent | privacy | regula- |            |               |     |     |          |           |        |      |
| --------- | --------- | --- | ---------- | --------- | ------- | ------- | ---------- | ------------- | --- | --- | -------- | --------- | ------ | ---- |
|           |           |     |            |           |         |         | scenarios, | bug patterns, |     | and | software | behaviors | [137]. | This |
tions [131]. Synthetic data mimics real data without exposing is particularly useful for testing and debugging, as it allows
| actual customer |     | information, | enabling | institutions |     | to comply |            |             |     |         |           |        |         |     |
| --------------- | --- | ------------ | -------- | ------------ | --- | --------- | ---------- | ----------- | --- | ------- | --------- | ------ | ------- | --- |
|                 |     |              |          |              |     |           | developers | to identify |     | and fix | potential | issues | without | the |
with privacy laws while still utilizing detailed datasets for constraints of existing codebases. Synthetic code can also
analysis and development. Second, synthetic data can be used aid in developing personalized coding assistants, optimiz-
| to test | and validate | financial | algorithms |     | and models | under |              |              |     |     |           |     |             |     |
| ------- | ------------ | --------- | ---------- | --- | ---------- | ----- | ------------ | ------------ | --- | --- | --------- | --- | ----------- | --- |
|         |              |           |            |     |            |       | ing software | performance, |     | and | improving | the | reliability | of  |
various conditions. For example, trading algorithms can be codereleases[138].Additionally,bygeneratingdiverseand
tested using synthetic market data to evaluate their perfor- extensive code samples, developers can enhance machine
mance under different market scenarios, including rare or learning models for code completion and error detection,
extremeeventsthatmaynotbepresentinhistoricaldata[132]. ultimately leading to more efficient and robust software
| Third, developing |     | and testing | financial |     | algorithms | requires |             |            |     |     |     |     |     |     |
| ----------------- | --- | ----------- | --------- | --- | ---------- | -------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
|                   |     |             |           |     |            |          | development | processes. |     |     |     |     |     |     |
largevolumesofhigh-qualitydata.Syntheticdataprovidesan
endless supply of training data, enabling thorough backtesting III. GENERATIVEAI
| of trading | strategies | and | machine learning |     | models | without the |            |           |     |       |           |       |       |         |
| ---------- | ---------- | --- | ---------------- | --- | ------ | ----------- | ---------- | --------- | --- | ----- | --------- | ----- | ----- | ------- |
|            |            |     |                  |     |        |             | Generative | AI models |     | refer | to a wide | class | of AI | methods |
risk of overfitting historical data [133]. thatcouldlearnthedatadistributionfromexistingdataobjects
Synthetic data generation also transforms the financial ser- and generate novel structured data objects, which fall into
vicesindustrybyenablingmoreaccurateriskassessmentsand the category of unsupervised learning. Generative AI models,
fraud detection [104]. Synthetic data generation can identify alsoknownasdeepgenerativemodels,ordistributionlearning
anomalies and potential risks by simulating financial trans- methods, learn the data distribution and samples from the
actions and market behaviors, allowing financial institutions learned distribution to produce novel data objects. In this
to implement more effective fraud prevention measures and section, we investigate several generative AI models that
develop more resilient financial strategies. Furthermore, syn- are frequently used in synthetic data generation, including
thetic data generation can support compliance with regulatory the language model in Section III-A, variational autoencoder
requirements by providing detailed, real-time reporting and (VAE)inSectionIII-C,generativeadversarialnetwork(GAN)
analysis of financial activities [47]. In the context of human inSectionIII-D,reinforcementlearning(RL)inSectionIII-E,
resources, synthetic data generations can model workforce anddiffusionmodelinSectionIII-F.TableIIcomparesvarious
dynamics, including employee performance, engagement, and generative AI methods from several aspects.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 7
TABLEII
COMPARISONOFALLTHEGENERATIVEAIMETHODSFROMDIFFERENTASPECTS.
Method Supervision NNArchitecture MLE With latent Paper
variable
Languagemodel(LM) no autoregressivemodel yes no [139]
self-supervisedlearning(SSL) no encoder(representation) yes no
variationalautoencoder(VAE) no encoder-decoder yes yes [140]
generativeadversarialnetwork(GAN) no generator&discriminator yes yes [141],[142]
diffusion(score-basedmodel)model no representation yes no [143]
reinforcementlearning(RL) yes policy network or Q- no no [144]
network
A. Language Model Formally, suppose the data object is denoted x, the latent
variable is a d-dimensional real-valued vector z, the encoder
The language model was originally designed to model
is p(z|x), and the decoder is q(x|z). The learning objective
naturallanguage.Itisabletolearnstructuredknowledgefrom
contains two parts: (1) reconstruct the data object x and (2)
massive unlabelled sequence data. Specifically, suppose the
encouragethedistributionoflatentvariablestobeclosetothe
sequence has N tokens, denoted X =[x ,··· ,x ], then the
1 N
normal distribution.
probabilitydistributionofthesequencecanbedecomposedas
the product of a series of conditional probabilities, The Kullback-Leibler (KL) divergence measures the differ-
ence between two probability distributions. Given two prob-
N
p(X)=p (cid:0) [x ,··· ,x ] (cid:1) = (cid:89) p(x |x ,··· ,x ), (1) ability distributions p 1 (x) and p 2 (x) on the same continuous
1 N i 1 i−1
domain, KL divergence between them is formally defined as
i=1
where a single conditional probability p(x |x ,··· ,x )
i 1 i−1
denote the probability of the token x i given all the tokens (cid:90) p (x)
before x . The conditional probability can be modeled by KL(p ||p )= p (x)log 1 dx
i 1 2 1 p (x)
the recurrent neural network (RNN). The language model x 2
(cid:90)
can be used to generate all types of sequence data, such as = p (x) (cid:2) logp (x)−logp (x) (cid:3) dx.
1 1 2
natural language [139], electronic health records [145], etc. x
(cid:90)
Thelanguagemodelcanbecombinedwithotherdeeplearning logp(x)=log p(z)p(x|z)dz
models,suchasvariationalautoencoder(VAE)andgenerative z
adversarial network (GAN), which will be described later. ≥E (cid:2) logp(x|z) (cid:3) −D (q(z|x)||p(z))
q(z|x) KL
≜ELBO.
B. Self-Supervised Learning (SSL)
Labeled data are expensive to acquire so the number of where p(z) is the normal distribution and is used as the
available labeled datais usually limited. To addressthis issue, prior distribution. VAE encourages the distribution of latent
self-supervised learning (SSL) was proposed. This learning variables to be close to normal distribution. Then during
paradigm curates the supervision signal from the data itself. the inference phase, we sample latent variables from the
Itisparalleltosupervisedlearningandunsupervisedlearning. normal distribution and generate the novel data objects. There
Different from supervised learning, self-supervised learning are several VAE variants, such as disentangled VAE [147],
can learn from massive unlabeled data. Self-supervised learn- hierarchical VAE [148], and sequence VAE [78].
ing is usually used as a pretraining strategy to learn the
representation from massive unlabelled data [146]. The core
idea of self-supervised learning is to mask a subset of the raw
data feature and build a machine learning model to predict D. Generative Adversarial Network (GAN)
the masked data. then the pre-trained machine learning model
Generative adversarial network (GAN) [141], [149], [150]
(usually a neural network) is used as a “warm start”, and is
formulates the generation problem into a supervised learning
furtherly finetuned for the downstream applications.
task. Specifically, it comprises two neural network modules:
discriminator and generator. The objective of the generator is
C. Variational Autoencoder (VAE)
togeneratedatathatareclosetotherealdata,Bycomparison,
Variational autoencoder (VAE) [140] employs a continuous the objective of the discriminator is to discriminate the fake
latent variable to characterize the data distribution. Specifi- data (generated by the generator) from the real ones. It
cally, it contains two neural network modules: encoder and performs a binary classification task, where the real data from
decoder. The objective of the encoder is to convert the data the training set are regarded as the positive samples; the
object into a continuous latent variable. Then decoder takes generated data (by generator) are regarded as the negative
the latent variable as the input feature and reconstructs the samples. generator and discriminator are trained in a mini-
data object. max manner.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 8
Formally, the generator is denoted G(z), and the discrim- The objective function is not differentiable with parameter θ.
inator predicts a probabilistic score for a data object and is We use policy gradient to obtain an unbiased estimator of
denoted D(x). The learning objective is formulated as the objective gradient ∇ L(θ) [144] and then use stochastic
θ
optimization methods to maximize the expected reward. Gen-
minmaxL(D,G)= E [logD(x)]
x∼trainingset erating synthesis data can be viewed as sequential decision-
G D (2)
+E (cid:2) log(1−D(G(z)) (cid:3) , making by sequentially generating one basic structure.
z∼p(z)
where z is the latent variable and is drawn from the normal
F. Diffusion Model
distributionp(z)toenhancethediversityofthegenerateddata
The diffusion model, also known as the score-based model
objects.
orscorematchingmethod,wasproposedinrecentyears[143]
When learning GAN, the generator and discriminator are
and is widely validated in many generative AI problems such
optimized alternatively.
as speech synthesis [36].
• optimize generator and fix discriminator: the objective Specifically,supposethedataobjectisx,andthelikelihood
function becomes function is denoted p(x). We are interested in estimating the
minL(G)=E (cid:2) log(1−D(G(z)) (cid:3) , (3) gradient of the logarithm of the likelihood function.
z∼p(z) Diffusion models [153], [154] are inspired by non-
where the generator is optimized to generate data that is equilibrium thermodynamics and can be split into the forward
closetotherealdata(withhigherdiscriminator’sscores). and backward diffusion processes. During the forward diffu-
• optimize discriminator and fix generator: the objective sion process, diffusion models will gradually add Gaussian
function reduces to a binary classification problem, noisetothedata,andthelast-stepdatawillfollowanisotropic
Gaussian. The reverse diffusion process will revert such a
maxL(D)=E [logD(x)]
x∼trainingset process and construct the data from noise distribution.
(4)
+E (cid:2) log(1−D(G(z)) (cid:3) , Morerigorously,wecandefinetheforwardprocessasfrom
z∼p(z)
the actual data x ∼ p(x) to the random noise x with T
whichcanbeseenasacross-entropylossfunction,where 0 T
diffusionsteps.Letusfirstassumethatfortheforwardprocess,
the real data objects from the training set are seen as
the Gaussian distribution is
positive samples while the synthetic data objects G(z)
(cid:112)
are seen as negative samples. q(x |x )=N(x ; 1−β x ,β I),
t t−1 t t t−1 t
ThenwediscussapopularvariantofGAN.TheWasserstein where β ∈(0,1). Then, the corresponding backward process
t
Generative Adversarial Network (W-GAN) was proposed in is
2017 and aims to enhance the stability of learning, accelerate p θ (x t−1 |x t )
the training process, and get rid of problems like mode =N(x t−1 ;µ θ (x t ,t),Σ θ (x t ,t))
collapse [151]. =N(x ;√ 1 (cid:0) x − √ β t ϵ (cid:1) , 1−α¯ t−1β ),
t−1 α t t 1−α¯ t 1−α¯ t t
whereϵ∼N(0,I)followsthestandardGaussian,α =1−β ,
E. Reinforcement Learning (RL) t t
and α¯ =
(cid:81)t
α .
t i=1 i
Reinforcement learning (RL) focuses on addressing se-
The objective of diffusion models is to estimate the vari-
quential decision-making problems [152]. It can be used in
ational lower bound (VLB) of the negative log-likelihood of
synthesis data generation by growing a basic component at
data distribution:
onetimeandgeneratingdataobjectssequentially.Itformulates
q(x |x )
sequential decision-making as a Markov decision process logp(x)≥−E [log 1:T 0 ]=−L .
q(x1:T|x0) p (x ) VLB
(MDP)[144].Markovdecisionprocessassumesthatgiventhe θ 0:T
currentstate,thefuturestateofthestochasticprocessdoesnot The VLB can be rewritten as:
depend on the historical states. Suppose the state at the time L VLB =KL[q(x T |x 0 )||p θ (x T )]
t is xt, Markov decision process satisfies (cid:124) (cid:123)(cid:122) (cid:125)
LT
T
p(xt+1|xt,xt−1,xt−2,...)=p(xt+1|xt). (5) + (cid:88) KL[q(x |x ,x )||p (x |x )]−E [logp (x |x )].
t−1 t 0 θ t−1 t q θ 0 1
At the time t, given the state xt, the RL agent would generate
t=2(cid:124)
L
(cid:123)
t−
(cid:122)
1
(cid:125)(cid:124)
L
(cid:123)(cid:122)
0
(cid:125)
an action at from action space, which is denoted p θ (at|st), θ Here L T is a constant and can be ignored, and diffusion
is the parameter of the RL agent. After performing the action, models[154]havebeenusingaseparatemodelforestimating
the system would jump into the next state xt+1, i.e., xt+1 = L .For{L }T ,wemodelaneuralnetworktoapproximate
0 t−1 t=2
f(xt,at). At the same time, the system would receive the the conditionals during the reverse process, i.e.,, we want to
r r e e w wa ar rd df r u ( n x c t t ) io f n r . om The th g e o e a n l v is iro to nm le e a n rn t, a w n h a e g r e e n r t ( t · h ) at is ca c n al r le e d ce t i h ve e t i r n a t i o n t µ he θ ( c x l t o , s t e ) d t - o fo p rm red s i o ct lu √ ti 1 o α n t (cid:0) o x f t − the √ K 1 β − L t α¯ -d t ϵ iv (cid:1) e . r I g f en w c e e p b l e u t g w t e h e i n s
the maximal expected reward in total. two multivariate Gaussian distributions, we will have the
∞ following for t=1,··· ,T −1:
(cid:88)
argmax L(θ)= E [r(xt)]. (6) (cid:104) √ √ (cid:105)
pθ(at|xt) L =E ∥ϵ −ϵ ( α¯ x + 1−α¯ ϵ ,t)∥2 .
θ
t=1
t x0,z t θ t 0 t t

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     | 9   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The diffusion model has achieved wide success in many B. Privacy Protection in Data Synthesis
| downstream | synthetic | problems |     | [82], [155]–[157]. |     | As  | a sum- |     |     |     |     |     |     |     |
| ---------- | --------- | -------- | --- | ------------------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
marization, Table II compares various generative AI methods Solutionshavebeenproposedintwobroadcategories.Inthe
from several aspects. first category, different data anonymization-based approaches
|     |     |     |     |     |     |     | such as | K-anonymity | [209]–[211] |     | and | nearest | marginal | [212] |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ----------- | --- | --- | ------- | -------- | ----- |
G. Multimodal Learning to sanitize data so that it cannot be easily re-identified. These
|            |      |        |     |          |                |          | data anonymization |     | approaches |     | involve | replacing |     | sensitive |
| ---------- | ---- | ------ | --- | -------- | -------------- | -------- | ------------------ | --- | ---------- | --- | ------- | --------- | --- | --------- |
| Multimodal | data | refers | to  | datasets | that integrate | multiple |                    |     |            |     |         |           |     |           |
types of data, such as text, images, audio, and numerical data with fictitious yet realistic data. It is often used to
|              |           |         |          |                 |       |      | protect     | the data  | while | maintaining | its  | usability | for    | testing or |
| ------------ | --------- | ------- | -------- | --------------- | ----- | ---- | ----------- | --------- | ----- | ----------- | ---- | --------- | ------ | ---------- |
| values. This | type      | of data | provides | a comprehensive |       | view | by          |           |       |             |      |           |        |            |
|              |           |         |          |                 |       |      | development | purposes. |       | However,    | they | often     | do not | provide    |
| combining    | different | sources | of       | information,    | which | is   | crucial     |           |       |             |      |           |        |            |
fortasksrequiringaholisticunderstandingofcomplexscenar- rigorous privacy guarantees [14]. In the second category,
|                |      |            |        |          |     |            | synthetic | data | generation | approaches |     | have | been proposed | to  |
| -------------- | ---- | ---------- | ------ | -------- | --- | ---------- | --------- | ---- | ---------- | ---------- | --- | ---- | ------------- | --- |
| ios. In fields | like | healthcare | [158], | finance, | and | autonomous |           |      |            |            |     |      |               |     |
systems, multimodal data enables more accurate and robust generate realistic synthetic data using rigorous differential
privacydefinitions[114],[174],[213]forvariousapplications.
| analysis  | and decision-making |               |     | by leveraging |            | the strengths | of               |     |          |        |       |     |          |            |
| --------- | ------------------- | ------------- | --- | ------------- | ---------- | ------------- | ---------------- | --- | -------- | ------ | ----- | --- | -------- | ---------- |
|           |                     |               |     |               |            |               | These approaches |     | involves | adding | noise | to  | the data | to prevent |
| each data | type.               | For instance, |     | in drug       | discovery, | multimodal    |                  |     |          |        |       |     |          |            |
data can combine genomic data, chemical structures, and theidentificationofindividualsinthedatasetwhilepreserving
|          |          |            |     |                |     |                  | the statistical | properties |     | of the | data. This | is  | particularly | useful |
| -------- | -------- | ---------- | --- | -------------- | --- | ---------------- | --------------- | ---------- | --- | ------ | ---------- | --- | ------------ | ------ |
| clinical | outcomes | to enhance |     | the prediction |     | of drug efficacy |                 |            |     |        |            |     |              |        |
and safety [95], [159]. in scenarios where data needs to be shared but individual
Synthetic multimodal data generation involves creating ar- privacy must be maintained. In particular, Bindschaedler et
al.[174]introducedtheideaofplausibledeniabilityinsteadof
| tificial datasets |     | that integrate |     | multiple | types of | data, such | as  |     |     |     |     |     |     |     |
| ----------------- | --- | -------------- | --- | -------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
text,images,audio,andnumericaldata,tosimulatereal-world directlyaddingnoisetothegenerativemodel.Thismechanism
|            |      |           |                 |     |          |           | results | in input | indistinguishability |     |     | that means | by  | observing |
| ---------- | ---- | --------- | --------------- | --- | -------- | --------- | ------- | -------- | -------------------- | --- | --- | ---------- | --- | --------- |
| scenarios. | This | technique | is particularly |     | valuable | in fields | like    |          |                      |     |     |            |     |           |
healthcare [16], finance [104], and education systems [109], the output set (i.e., synthetics) an adversary cannot make sure
where data is often complex and heterogeneous. whether a particular data record was in the input set (i.e., real
|     |     |     |     |     |     |     | data). With | the | help of | generative | modeling, |     | Acs | et al. [43] |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ---------- | --------- | --- | --- | ----------- |
Then,wereviewsomecutting-edgetechniquesforsynthetic
multimodal data generation. GANs can generate one type of clusters the original datasets into k clusters with differentially
|     |     |     |     |     |     |     | private | kernel | k-means | and | produce | synthetic | data | for each |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------- | --- | ------- | --------- | ---- | -------- |
datafromanother,suchasimagesfromtextualdescriptionsor
|            |         |      |             |            |     |            | cluster. | By comparison, |     | Liu | et al [205] | introduce |     | two-level |
| ---------- | ------- | ---- | ----------- | ---------- | --- | ---------- | -------- | -------------- | --- | --- | ----------- | --------- | --- | --------- |
| audio from | images. | This | cross-modal | generation |     | capability | is       |                |     |     |             |           |     |           |
essential for creating cohesive multimodal datasets [11]. Re- privacy-preservingsyntheticdatageneration.Atthedatalevel,
aselectionmoduleisusedtoselecttheitemswhichcontribute
| cently, ChatGPT |     | [129] | supports | multimodal |     | data generation, |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | -------- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
including image, text, and numerical features. lesstotheuser’spreference.Attheitemlevel,asyntheticitem
|     |                               |     |     |     |     |     | generation | module | is  | developed | to  | create | the corresponding |     |
| --- | ----------------------------- | --- | --- | --- | --- | --- | ---------- | ------ | --- | --------- | --- | ------ | ----------------- | --- |
|     | IV. PRIVACYRISKSANDPREVENTION |     |     |     |     |     | synthetic  | item.  |     |           |     |        |                   |     |
Openreleaseandfreedataexchangewouldbenefitresearch TakingadvantageoftheGAN,severalmethodsareproposed
| and industry | development. |     | However, |     | there are | cases | where       |           |     |      |        |        |        |             |
| ------------ | ------------ | --- | -------- | --- | --------- | ----- | ----------- | --------- | --- | ---- | ------ | ------ | ------ | ----------- |
|              |              |     |          |     |           |       | to generate | synthetic |     | data | to get | better | effect | [27], [49], |
datasets exist but cannot be publicly disclosed due to privacy [176], [177], [183], [187], [188] which closely matches the
concerns. Regulated data, such as clinical and genomics data distributionofthesourcedatathanthehiddenMarkovmodel-
in raw form, may not be shared, and one solution is to share based approach [73], RBF based approach [194], Bayesian
synthesized data instead. network-based [204], and Auto-encoder based approach [14].
|            |       |         |           |     |     |     | Xie et | al [177] | propose | DPGAN |     | by adding | noise | on the |
| ---------- | ----- | ------- | --------- | --- | --- | --- | ------ | -------- | ------- | ----- | --- | --------- | ----- | ------ |
| A. Privacy | Risks | in Data | Synthesis |     |     |     |        |          |         |       |     |           |       |        |
gradientoftheWassersteindistancewithrespecttothetraining
Due to the utility goal of data synthesis, the synthesized data. This approach does not adopt the optimization strategy
data tends to preserve the distribution of the original data. to improve the training stability and convergence speed. To
Therefore, the deployment of these models could be subject address these problems, Zhang et al. [176] proposed dp-
toprivacyleakage.Fordeepneuralnetwork-basedapproaches, GAN, a general private data publishing framework for rich
membership inference attack [160], [161] would identify if semantic data without the requirement of tag information
an input is in the training data or not and thus can be comparedto[183].Bycomparison,Beaulieu-Jonesetal.[183]
used to determine how close the synthesized data is to the trained the discriminator under differentially private SGD,
original data. At the feature level, sensitive attributes such which generates plausible individuals of clinical datasets.
as skin color can be inferred from the behavior of the deep Tseng and Wu [175] apply compressive privacy [214] for
learning model [162], and even the single training instance CPGAN, which would generate compressing representations
can be reconstructed [163]–[165]. For generative AI models, that retain high utility. Jordon et al. [49] modifies the
the generative learning process and the high complexity of PrivateAggregationof TeacherEnsembles(PATE)framework
the model jointly encourage a distribution that is concentrated and applies it to the discriminator of GANs. The proposed
around training samples. By repeatedly sampling from the approachperceivesthediscriminatorasaclassifierandutilizes
distribution, there is a considerable chance of recovering the its output as knowledge such that the student learns from
training samples or attributes [166]–[172], or the membership noisy labels that are obtained through privately aggregating
of the training data [173]. the discriminator’ votes. This allows a tight bound on the

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 10
TABLEIII
SUMMARIZATIONOFPRIVACYPREVENTIONSTRATEGIESINSYNTHETICDATAGENERATION.
Paper Privacy-enhancingTechniques GenerativeAI DNN DataFormat
| [14] differentialprivacy | autoencoder | autoencoder          | attribute |
| ------------------------ | ----------- | -------------------- | --------- |
| [27] differentialprivacy | VAE+GAN     | recurrentautoencoder | EHR       |
[43] differentialprivacy generativeartificialneuralnetworks kernelk-means imageandtext
| [49] differentialprivacy(PATE) | GAN | DNN | attribute |
| ------------------------------ | --- | --- | --------- |
[113] differentialprivacy n-gram NA(w.o.DNN) sequential/timeseries
| [115] localdifferentialprivacy | n-gram | NA(w.o.DNN) | trajectory |
| ------------------------------ | ------ | ----------- | ---------- |
[116] localdifferentialprivacy Markovprobabilisticmodel NA(w.o.DNN) trajectory
[117] differentialprivacy Markovprobabilisticmodel NA(w.o.DNN) trajectory
[118] differentialprivacy Markovprobabilisticmodel NA(w.o.DNN) socialmediatrajectory
[120] differentialprivacy Markovprobabilisticmodel NA(w.o.DNN) trajectory
[121] differentialprivacy distributionestimation NA(w.o.DNN) location
[122] differentialprivacy distributionestimation NA(w.o.DNN) trajectory
[123] plausibledeniability HiddenMarkovModels NA(w.o.DNN) trajectory
[124] differentialprivacy Markovchainmodel NA(w.o.DNN) trajectory
[125] differentialprivacy probabilisticaltransform NA(w.o.DNN) trajectory
[174] plausibledeniability probabilisticaltransform NA(w.o.DNN) attribute
| [175] compressiveprivacy        | GAN | DNN         | image                      |
| ------------------------------- | --- | ----------- | -------------------------- |
| [176] differentialprivacy       | GAN | DNN         | image                      |
| [177] differentialprivacy       | GAN | DNN         | imageandEHR                |
| [178] differentialprivacy       | GAN | DNN         | image                      |
| [179] differentialprivacy       | GAN | DNN         | image                      |
| [180] differentialprivacy       | GAN | DNN         | attribute(tabular)andgraph |
| [181] differentialprivacy       | GAN | DNN         | imageandEHR                |
| [182] differentialprivacy       | GAN | DNN         | timeseries                 |
| [183] differentialprivacy       | GAN | DNN         | attribute                  |
| [184] differentialprivacy       | GAN | DNN         | attribute(tabular)         |
| [185] differentialprivacy       | GAN | DNN         | image                      |
| [186] differentialprivacy       | GAN | DNN         | image                      |
| [187] differentialprivacy       | GAN | autoencoder | attribute                  |
| [188] differentialprivacy       | GAN | DNN         | trajectory                 |
| [189] differentialprivacy(PATE) | GAN | DNN         | image                      |
| [190] localdifferentialprivacy  | GAN | DNN         | spatialpoint               |
[191] differentialprivacy MaximumMeanDiscrepancy Hermitepolynomialfeatures attribute(tabular)andimage
[192] differentialprivacy MaximumMeanDiscrepancy Randomfeaturemeanembeddings image
[193] differentialprivacy Markovrandomfield NA(w.o.DNN) attribute
[194] differentialprivacy Markovrandomfield NA(w.o.DNN) attribute
[195] differentialprivacy Probabilisticgraphicalmodels NA(w.o.DNN) attribute
[196] differentialprivacy MaximumCardinalityMatching NA(w.o.DNN) attribute(tabular)
[197] differentialprivacy Bayesiannetwork NA(w.o.DNN) attribute
[198] differentialprivacy Bayesiannetwork NA(w.o.DNN) attribute
[199] differentialprivacy statisticaldatabase NA(w.o.DNN) attribute
[200] differentialprivacy statisticalqueries A(w.o.DNN) attribute
[201] differentialprivacy statisticalqueries A(w.o.DNN) attribute
[202] differentialprivacy GraduateUpdateMethod NA(w.o.DNN) attribute
[203] differentialprivacy autoencoder autoencoder imageandattribute
[204] differentialprivacy autoencoder autoencoder text/imageQAandattribute
[205] datareplacementanditemregularizer latentspaceprojection MLP attributes
[206] differentialprivacy LangevinMarkovchainMonteCarlo Energy-basedModel image
[207] localdifferentialprivacy MaximumEntropyestimation NA(w.o.DNN) attribute
[208] differentialprivacy MaximumEntropyestimation NA(w.o.DNN) attribute
influence of any individual sample on the model, resulting GAN for synthetic spatial point generation. Apart from LDP
in tight differential privacy guarantees and thus an improved in distributed setting, Triastcyn and Faltings [179] propose
performance over models for data synthesis. By comparison, federatedgenerativeprivacythatutilizesinsufficientlocaldata
Long et at. [189] applies teacher-student-based differential frommultipleclientstotrainaGAN.Themethodsharesonly
privacytothegenerator.Whilemostoftheseapproachesinject generators that do not come directly into contact with data
noise into the energy function, a differentially private GAN and the discriminator remain private. This model can output
called GANobfuscator [178] achieve differential privacy by artificial data, not belonging to any real user in particular, but
adding noise within the training procedure. coming from the common cross-user data distribution.
Whilecentralizeddifferentialprivacyassumesdataaggrega- These privacy-preserving data synthesis methods mainly
torsarereliable,localdifferentialprivacy(LDP)[213]assumes aim at structured data like tables, which cannot be applied
thataggregatorscannotbetrustedandreliesondataproviders to high dimensionality and complexity. To solve this problem,
to perturb their own data and is used to generate private PriView [208] constructs the private k-way marginal tables
synthetic datasets that is similar to the private dataset. [207] for k ≥3 by first extracting low-dimensional marginal views
is inspired by PriView [208] but for computing any k-way from the flat data and adding noise to the views and then
marginalsundertheLDPsettingforthemarginaltablerelease applying a reprocessing technique to ensure the consistency
problem. Furthermore, [190] considers DP at label-level on of the noisy views. [215]–[218] leverage copula functions for

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     | 11  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
multi-dimensional differentially private synthesization. Zhang models for data synthesis has not been fully explored. While
et al. [198] consider repetitive perturbation of the original morepossibleprivacythreatsonthefoundationmodelsareyet
data as a substitute to the original data with a synthetic tobediscovered,existingprivacymeasuresmaybeinadequate
datagenerationtechniquecalledPrivBayes.PrivBayesdecom- tomeetitsdemandsofprivacy.Furtherinvestigationisneeded
poses high dimensional data into low dimensional marginals to design countermeasures that would mitigate the memoriza-
by constructing a Bayesian network and injects noise into tion and generalization problems for privacy protection.
theselearnedlowdimensionalmarginalstoensuredifferential
| privacy    | and the | synthetic | data         | is inferred | from     | these noised   |     |     |             |     |     |     |
| ---------- | ------- | --------- | ------------ | ----------- | -------- | -------------- | --- | --- | ----------- | --- | --- | --- |
|            |         |           |              |             |          |                |     |     | V. FAIRNESS |     |     |     |
| marginals. | Instead | of        | the Bayesian |             | network, | differentially |     |     |             |     |     |     |
private auto-encoder [14] significantly improves the effec- Generating synthetic data that reflect the important under-
tiveness of differentially private synthetic data release. [199] lying statistical properties of the real-world data may also
|         |               |     |        |          |                    |     | inherit the | bias from data | preprocessing, |     | collection, | and algo- |
| ------- | ------------- | --- | ------ | -------- | ------------------ | --- | ----------- | -------------- | -------------- | --- | ----------- | --------- |
| applies | data cleaning |     | method | [219] to | fix the violations | on  |             |                |                |     |             |           |
the structure of the data in the synthetic data. Instead of rithms [232]. Minority groups can often end up being under-
using graphical models as the summarization/representation represented in synthetic data [233]–[235]. The fairness prob-
of a dataset [14], [174], [176], [200], [201], [202] proposes to lem is currently addressed by three types of methods [236]:
useasetoflargenumberoflow-degreemarginalstorepresent (i)preprocessing,whichrevisesinputdatatoremoveinforma-
|            |     |           |     |               |         |          | tion correlated | to sensitive | attributes, | usually | via | techniques |
| ---------- | --- | --------- | --- | ------------- | ------- | -------- | --------------- | ------------ | ----------- | ------- | --- | ---------- |
| a dataset. | The | advantage | of  | this approach | is that | it makes |                 |              |             |         |     |            |
weak assumptions about the conditional independence among like massaging, reweighting, and sampling. (ii) in-processing,
attributes, and simply tries to capture correlation relationships which adds fairness constraints to the model learning process;
that are in the dataset. Meanwhile, the method is especially and(iii)post-processing,whichadjustsmodelpredictionsafter
attractive under differential privacy for its straightforward the model is trained.
|             |              |     |         |       |           |               | Most existing | fairness-aware | data | synthesis | methods | lever- |
| ----------- | ------------ | --- | ------- | ----- | --------- | ------------- | ------------- | -------------- | ---- | --------- | ------- | ------ |
| sensitivity | measurement, |     | reduced | noise | variance, | and efficient |               |                |      |           |         |        |
privacy cost. [191] leverages the Hermite polynomial features age preprocessing techniques. The use of balanced synthetic
toencapsulateahigherdegreeofinformationwithinasmaller datasets created by GANs to augment classification training
orderoffeature.[193]constructsagraphthatexplorepairwise has demonstrated the benefits for reducing disparate impact
dependence between attributes and applies the junction tree due to minoritized subgroup imbalance [237]–[239]. [240]
algorithm to obtain the Markov random field (MRF), from modelsbiasusingaprobabilisticnetworkexploitingstructural
whichthenoisymarginalsaregeneratedandthesyntheticdata equationmodelingasthepreprocessingtogenerateafairness-
are sampled. aware synthetic dataset. Authors in [241] leverage GAN as
|       |         |           |      |            |            |     | the pre-processing | for | fair data | generation | that | ensures the |
| ----- | ------- | --------- | ---- | ---------- | ---------- | --- | ------------------ | --- | --------- | ---------- | ---- | ----------- |
| While | private | synthetic | data | generation | algorithms | are |                    |     |           |            |      |             |
agnostic to downstream tasks, it is important to meet the generated data is discrimination free while maintaining high
utility requirements for downstream use. [220] proposes post- data utility. By comparison, [242] is geared towards high
processing via resampling from the synthetic data to filter out dimensional image data and proposes a novel auxiliary clas-
samples that do not meet the selected utility measures, thus sifier GAN that strives for demographic parity or equality
|           |     |            |           |       |     |     | of opportunity. | However,   | preprocessing        |     | would | require the |
| --------- | --- | ---------- | --------- | ----- | --- | --- | --------------- | ---------- | -------------------- | --- | ----- | ----------- |
| improving | the | utility of | synthetic | data. |     |     |                 |            |                      |     |       |             |
|           |     |            |           |       |     |     | synthesizeddata | providerto | knowallcorrelations, |     |       | biases,and  |
C. Privacy Threats in Foundation Models distributions of variables in the existing datasets as a priori.
Entering the era of foundation models, recent research has Compared to preprocessing, the latter two categories are less-
demonstratedthattrainingdatacanbeexposedfromlargelan- developed for fair data synthesis. [243] insert a structural
|              |       |     |         |                  |        |         | causal model | in the input | layers | of the | generator, | allowing |
| ------------ | ----- | --- | ------- | ---------------- | ------ | ------- | ------------ | ------------ | ------ | ------ | ---------- | -------- |
| guage models | [221] | as  | well as | stable diffusion | [222]. | In both |              |              |        |        |            |          |
types of models, attackers can generate sequences from the each variable to be reconstructed conditioned on its causal
trained model and identify those memorized from the training parents for inference time debiasing.
set. Studies have shown that a sequence that appears multiple In the meantime, differential privacy amplifies the fairness
times in the training data is more likely to be generated issues in the original data [244]. [131] demonstrate that
|                 |     |               |     |           |        |               | differential | privacy does | not introduce | unfairness |     | into the data |
| --------------- | --- | ------------- | --- | --------- | ------ | ------------- | ------------ | ------------ | ------------- | ---------- | --- | ------------- |
| than a sequence |     | that occurred |     | only once | [157], | [223], [224]. |              |              |               |            |     |               |
Accordingly, Kandpal et al [225] propose to deduplicate the generation process or to standard group fairness measures
training data that appears multiple times such that the privacy in the downstream classification models, but does unfairly
risksinlanguagemodelsismitigated.[226]isthefirstworkto increase the influence of majority subgroups. Differential
enforce privacy using differentially private stochastic gradient privacy also significantly reduces the quality of the images
|         |          |     |           |         |         |              | generated | from the GANs, | decreasing |     | the synthetic | data’s |
| ------- | -------- | --- | --------- | ------- | ------- | ------------ | --------- | -------------- | ---------- | --- | ------------- | ------ |
| descent | (DP-SGD) | in  | diffusion | models. | Several | attempts has |           |                |            |     |               |        |
been made to reduces the noise in the gradient during DP- utilityindownstreamtasks.Tomeasurethefairnessinsynthe-
SGD training and improves the generative quality in diffusion sizeddata,[94]developstwocovariate-leveldisparityfairness
models, via semantic-aware pretraining [227], [228], latent metrics for synthetic data. The authors analyze all subgroups
information [229], and retrieval-augmented generation [230]. defined by protected attributes to analyze the bias.
|     |     |     |     |     |     |     | In the emerging | AIGC | using foundation |     | models, | the gen- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---- | ---------------- | --- | ------- | -------- |
Inthemeantime,differentialprivacyhasbeenheavilyinvested
in privacy protection of large language models [231]. erated images and texts may also inherit the stereotypes,
Given that we are still at the very early stage of the exclusion and marginalization of certain groups and toxic
generativefoundationalmodels,thepotentialofthefoundation and offensive information in the real-world data. This would

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     | 12  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lead to discrimination and harm to certain social groups. The applications. High performance on real test data indicates
misuse of such data synthesis approaches by misinformation that the synthetic data has successfully captured essential
and manipulation would lead to further negative social im- characteristics of the real data, making it a useful proxy
pact [245]. Given that the quality of the data generated by for training. For example, [248] employs synthetic data to
foundation models is inextricably linked to the quality of train machine learning models and assess their prediction
the training corpora, it is essential to regulate the real-world performance on real test data in downstream applications.
data being used to form the data synthesis distribution. While TSTR can provide insights into the effectiveness of syn-
reducing bias in data is important, the remaining bias in the thetic data for training machine learning models in a wide
datamayalsobeamplifiedbythemodels[236]ortheprivacy- range of tasks and domains.
enhancing components [244]. With frequent inspection and 5) Application-specific evaluation. Depending on the spe-
sensitive and toxic information removal on both data and cific use case or domain, tailored evaluation methods may
model, it will help govern the information generated from be employed to assess the quality of synthesized data.
those foundation models and ensure the models would do no Theseevaluationmethodscanconsidertheuniquerequire-
harm. ments or constraints of the application, such as regulatory
compliance,privacyconcerns,orspecificperformancemet-
|     |     |     |     |     |     |     | rics. By | evaluating | the synthesized |     | data | in the context | of  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --------------- | --- | ---- | -------------- | --- |
VI. EVALUATIONSTRATEGY
|             |                   |                   |            |              |               |        | its intended      | use,       | a more     | accurate  | assessment | of its        | quality |
| ----------- | ----------------- | ----------------- | ---------- | ------------ | ------------- | ------ | ----------------- | ---------- | ---------- | --------- | ---------- | ------------- | ------- |
| In this     | section, we       | discuss various   | approaches |              | to evaluating |        |                   |            |            |           |            |               |         |
|             |                   |                   |            |              |               |        | and applicability |            | can be     | obtained. |            |               |         |
| the quality | of synthesized    | data,             | which      | is essential | for           | deter- |                   |            |            |           |            |               |         |
|             |                   |                   |            |              |               |        | These             | evaluation | strategies | offer     | various    | ways to gauge | the     |
| mining      | the effectiveness | and applicability |            | of           | synthetic     | data   |                   |            |            |           |            |               |         |
qualityofsynthesizeddata,helpingresearchersandpractition-
generation methods in real-world scenarios. We categorize ers determine the effectiveness of synthetic data generation
| these evaluation | strategies | as follows: |     |     |     |     |         |           |               |     |            |            |     |
| ---------------- | ---------- | ----------- | --- | --- | --- | --- | ------- | --------- | ------------- | --- | ---------- | ---------- | --- |
|                  |            |             |     |     |     |     | methods | and their | applicability | in  | real-world | scenarios. | Em- |
1) Human evaluation. This method is the most direct way ploying a combination of these strategies can provide a more
| to assess | the quality | of synthesized |     | data. Human | evalua- |     |     |     |     |     |     |     |     |
| --------- | ----------- | -------------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
comprehensiveunderstandingofthestrengthsandweaknesses
tion involves soliciting opinions from domain experts or of the synthesized data, facilitating further improvements in
non-expert users to judge the synthesized data’s quality, synthetic data generation techniques [249].
| similarity | to real data, | or usability      | in  | specific  | applications. |     |     |                                 |     |     |     |     |     |
| ---------- | ------------- | ----------------- | --- | --------- | ------------- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
|            |               |                   |     |           |               |     |     | VII. CHALLENGESANDOPPORTUNITIES |     |     |     |     |     |
| For        | example, in   | speech synthesis, |     | the human | evaluator     |     |     |                                 |     |     |     |     |     |
rates the synthesized speech and real human speech in The aim of this research is to present a comprehensive sur-
a blind manner [44], [246]. However, human evaluation vey of synthetic data generation—a promising and emerging
has several drawbacks, including being expensive, time- techniqueincontemporarydeeplearning.Thissurveyoutlines
| consuming, | error-prone, | and | not scalable. | Additionally, |     | it  |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
currentreal-worldapplicationsandidentifiespotentialavenues
struggles with high-dimensional data that cannot be easily forfutureresearchinthisfield.Theutilizationofsyntheticdata
visualized and evaluated by humans. has been proven effective across a diverse array of tasks and
2) Statistical difference evaluation. This strategy involves domains [9]. In this section, we delve into the challenges and
calculating various statistical metrics on both the synthe- opportunities presented by this rapidly evolving area.
sized and real datasets and comparing the results. For First and foremost, evaluation metrics for synthetic data
example, [53],[247]usefirst-momentstatisticsofindivid- are essential to determine the reasonableness of the generated
ual features (e.g., medical concept frequency/correlation, data. In industries like healthcare, where data quality is of
patient-levelclinicalfeature)toevaluatethequalityofgen- paramount importance, clinical quality measures and evalu-
eratedelectronichealthrecord(EHR)data.Thesmallerthe ation metrics are not always readily available for synthetic
differences between the statistical properties of synthetic data. Clinicians often struggle to interpret existing criteria
andrealdata,thebetterthequalityofthesynthesizeddata. such as probability likelihood and divergence scores when
3) Evaluationusingapre-trainedmachinelearningmodel. assessing generative models [69]. Concurrently, there is a
AsmentionedinSectionIII-D,inthegenerativeadversarial pressing need to develop and adopt specific regulations for
network (GAN), the discriminator differentiates fake data the use of synthetic data in medicine and healthcare, ensuring
(synthesizeddata)fromrealones.Consequently,theoutput that the generated data meets the required quality standards
ofthediscriminatorcanmeasurehowcloselysyntheticdata while minimizing potential risks.
resembles real data. The performance of the discriminator Secondly, due to limited attention and the challenges as-
onthesynthesizeddatacanbeusedasanindicatorofhow sociated with covering various domains using synthetic data,
wellthegeneratorproducesrealisticdata.Thisstrategycan current methods might not account for all outliers and corner
be applied not only to GANs but also to other generative cases present in the original data. Investigating outliers and
modelswhereapre-trainedmachinelearningmodelisused regular instances and their impact on the parameterization of
for evaluation. existingmethodscouldbeavaluableresearchdirection[250].
4) Training on synthetic dataset and testing on the real To enhance future detection methods, it may be beneficial
dataset (TSTR). This strategy involves using synthetic to examine the gap between the performance of detection
data to train machine learning models and assessing their methods and a well-designed evaluation matrix, which could
prediction performance on real test data in downstream provide insights into areas that require improvement.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 13
Thirdly, synthetic data generation may involve underlying been extensively utilized in various sectors due to its ability
models with inherent biases, which might not be immediately to bridge gaps, especially when real data is either unavailable
evident [94]. Factors such as sample selection biases and or must be kept private due to privacy or compliance risks.
class imbalances can contribute to these issues. Typically, This paper has provided a high-level overview of several
algorithms trained with biases in sample selection may un- state-of-the-art approaches currently being investigated by
derperformwhendeployedinsettingsthatdeviatesignificantly machinelearningresearchersforsyntheticdatageneration.We
fromtheconditionsinwhichthedatawascollected[69].Thus, have explored different real-world application domains, and
it is crucial to develop methods and strategies that address examinedadiversearrayofdeepneuralnetworkarchitectures
these biases, ensuring that synthetic data generation leads to and deep generative models dedicated to generating high-
more accurate and reliable results across diverse applications quality synthetic data.
and domains. Tosumup,syntheticdatagenerationhasenormouspotential
Last but not the least, the rise of foundation models in for unlocking the full potential of machine learning and its
data synthesis presents both significant challenges and oppor- impact on various industries. While challenges persist in the
tunities. On one hand, foundation models can be exploited development and application of machine learning technology,
by malicious actors to create sophisticate jailbreak attacks, synthetic data generation provides a promising solution that
deepfakes, discrimination, exclusion and toxicity problems, can help address these obstacles. Future research can further
misinformation harms, sensitive information disclosure, and enhance the functionality of synthetic data generation.
malicioususe.Thesemodelscangeneratehuman-liketextand
realistic images or videos, making it difficult for traditional
security measures to detect malicious content. Furthermore,
the accessibility and rapid advancement of these technologies REFERENCES
lower the barrier for cybercriminals, enabling more sophis-
[1] A. Ng, “What artificial intelligence can and can’t do right now,”
ticated and widespread attacks. The ability to generate vast
HarvardBusinessReview,vol.9,no.11,2016.
amounts of realistic, yet fake, data can also overwhelm and [2] M.A.Boden,Artificialintelligence. Elsevier,1996.
deceivetraditionaldetectionsystems,leadingtoanincreasein [3] M.HaenleinandA.Kaplan,“Abriefhistoryofartificialintelligence:
On the past, present, and future of artificial intelligence,” California
false negatives and undetected breaches. On the other hand,
managementreview,vol.61,no.4,pp.5–14,2019.
foundation models offer promising opportunities to bolster [4] F.Lucini,“Therealdealaboutsyntheticdata,”MITSloanManagement
cybersecurity defenses. AI-driven anomaly detection systems Review,vol.63,no.1,pp.1–4,2021.
[5] M.I.JordanandT.M.Mitchell,“Machinelearning:Trends,perspec-
can leverage generative models to simulate various attack
tives,andprospects,”Science,vol.349,no.6245,pp.255–260,2015.
scenarios, improving their ability to recognize and mitigate [6] L.L.Pipino,Y.W.Lee,andR.Y.Wang,“Dataqualityassessment,”
real-worldthreats.Inthemeantime,thequestfortransparency CommunicationsoftheACM,vol.45,no.4,pp.211–218,2002.
[7] M. Shen, Y.-T. Chang, C.-T. Wu, S. J. Parker, G. Saylor, Y. Wang,
and interpretability in generative models promotes research
G.Yu,J.E.VanEyk,R.Clarke,D.M.Herringtonetal.,“Comparative
into explainable AI. By proactively addressing these machine assessment and novel strategy on methods for imputing proteomics
learning risks, synthetic data generation can evolve to deliver data,”Scientificreports,vol.12,no.1,p.1067,2022.
[8] R. Babbar and B. Scho¨lkopf, “Data scarcity, robustness and extreme
more ethical, secure, and transparent solutions, ultimately
multi-label classification,” Machine Learning, vol. 108, no. 8, pp.
harnessing its full potential to benefit society while mitigating 1329–1351,2019.
its associated risks. [9] S.I.Nikolenko,Syntheticdatafordeeplearning. Springer,2021,vol.
In general, the use of synthetic data is becoming a viable 174.
[10] V. Bolo´n-Canedo, N. Sa´nchez-Maron˜o, and A. Alonso-Betanzos, “A
alternative to training models with real data due to advances
reviewoffeatureselectionmethodsonsyntheticdata,”Knowledgeand
in simulations and generative models. However, a number of informationsystems,vol.34,no.3,pp.483–519,2013.
open challenges need to be overcome to achieve high perfor- [11] M.Frid-Adar,E.Klang,M.Amitai,J.Goldberger,andH.Greenspan,
“Syntheticdataaugmentationusingganforimprovedliverlesionclas-
mance.Theseincludethelackofstandardtools,thedifference
sification,” in IEEE international symposium on biomedical imaging
between synthetic and real data, and how much machine (ISBI),2018.
learning algorithms can do to exploit imperfect synthetic data [12] Q.Wang,J.Gao,W.Lin,andY.Yuan,“Learningfromsyntheticdata
forcrowdcountinginthewild,”inIEEE/CVFconferenceoncomputer
effectively.Thoughthisemergingapproachisnotperfectnow,
visionandpatternrecognition,2019.
with models, metrics, and technologies maturing, we believe [13] J. M. Abowd and L. Vilhuber, “How protective are synthetic data?”
synthetic data generation will make a bigger impact in the in International Conference on Privacy in Statistical Databases.
Springer,2008.
future.
[14] N. C. Abay, Y. Zhou, M. Kantarcioglu, B. Thuraisingham, and
L. Sweeney, “Privacy preserving synthetic data release using deep
VIII. CONCLUSION learning,” in Joint European Conference on Machine Learning and
KnowledgeDiscoveryinDatabases. Springer,2019.
In conclusion, machine learning has revolutionized various
[15] T.E.Raghunathan,“Syntheticdata,” AnnualReviewofStatisticsand
industries by enabling intelligent computer systems to au- ItsApplication,vol.8,pp.129–140,2021.
tonomouslytackletasks,manageandanalyzemassivevolumes [16] E.Choi,S.Biswal,B.Malin,J.Duke,W.F.Stewart,andJ.Sun,“Gen-
eratingmulti-labeldiscretepatientrecordsusinggenerativeadversarial
of data. However, it still faces several challenges, including
networks,” in Machine learning for healthcare conference. PMLR,
data quality, data scarcity, and data governance. These chal- 2017.
lenges can be addressed through synthetic data generation, [17] J. D. Ziegler, S. Subramaniam, M. Azzarito, O. Doyle, P. Krusche,
andT.Coroller,“Multi-modalconditionalGAN:Datasynthesisinthe
which involves the artificial annotation of information gener-
medical domain,” in NeurIPS 2022 Workshop on Synthetic Data for
atedbycomputeralgorithmsorsimulations.Syntheticdatahas EmpoweringMLResearch,2022.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 14
[18] K.W.Dunn,C.Fu,D.J.Ho,S.Lee,S.Han,P.Salama,andE.J.Delp, [43] G.Acs,L.Melis,C.Castelluccia,andE.DeCristofaro,“Differentially
“DeepSynth: Three-dimensional nuclear segmentation of biological privatemixtureofgenerativeneuralnetworks,”IEEETransactionson
images using neural networks trained with synthetic data,” Scientific KnowledgeandDataEngineering,vol.31,no.6,pp.1109–1121,2018.
reports,vol.9,no.1,pp.1–15,2019. [44] C.Donahue,J.McAuley,andM.Puckette,“Adversarialaudiosynthe-
[19] Y.Du,X.Liu,N.Shah,S.Liu,J.Zhang,andB.Zhou,“Chemspace: sis,”arXivpreprintarXiv:1802.04208,2018.
Interpretableandinteractivechemicalspaceexploration,”2022. [45] A. v. d. Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals,
[20] T. Sterling and J. J. Irwin, “Zinc 15–ligand discovery for everyone,” A.Graves,N.Kalchbrenner,A.Senior,andK.Kavukcuoglu,“Wavenet:
Journal of chemical information and modeling, vol. 55, no. 11, pp. Agenerativemodelforrawaudio,”arXivpreprintarXiv:1609.03499,
2324–2337,2015. 2016.
[21] W.Jin,R.Barzilay,andT.S.Jaakkola,“Junctiontreevariationalau- [46] X.Zhang,I.Valle´s-Pe´rez,A.Stolcke,C.Yu,J.Droppo,O.Shonibare,
toencoderformoleculargraphgeneration,”inInternationalConference R. Barra-Chicote, and V. Ravichandran, “Stutter-tts: Controlled syn-
onMachineLearning,2018. thesis and improved recognition of stuttered speech,” arXiv preprint
[22] M. Olivecrona, T. Blaschke, O. Engkvist, and H. Chen, “Molecular arXiv:2211.09731,2022.
de-novo design through deep reinforcement learning,” Journal of [47] M. Wiese, R. Knobloch, R. Korn, and P. Kretschmer, “Quant GANs:
cheminformatics,vol.9,no.1,p.48,2017. deepgenerationoffinancialtimeseries,”QuantitativeFinance,vol.20,
[23] T.Fu,C.Xiao,andJ.Sun,“CORE:Automaticmoleculeoptimization no.9,pp.1419–1440,2020.
using copy and refine strategy,” AAAI conference on artificial intelli- [48] R. Fu, J. Chen, S. Zeng, Y. Zhuang, and A. Sudjianto, “Time series
gence,2020. simulation by conditional generative adversarial net,” arXiv preprint
[24] T.Fu,W.Gao,C.W.Coley,andJ.Sun,“Reinforcedgeneticalgorithm arXiv:1904.11419,2019.
for structure-based drug design,” in Advances in Neural Information [49] J. Jordon, J. Yoon, and M. Van Der Schaar, “Pate-gan: Generating
ProcessingSystems(NeurIPS),2022. synthetic data with differential privacy guarantees,” in International
[25] K. Huang, T. Fu, W. Gao, Y. Zhao, Y. Roohani, J. Leskovec, C. W. conferenceonlearningrepresentations,2018.
Coley,C.Xiao,J.Sun,andM.Zitnik,“Artificialintelligencefoundation [50] A.Collaborationetal.,“Deepgenerativemodelsforfastphotonshower
fortherapeuticscience,”NatureChemicalBiology,pp.1–4,2022. simulationinatlas,”arXivpreprintarXiv:2210.06204,2022.
[26] A.TorfiandE.A.Fox,“Corgan:Correlation-capturingconvolutional [51] C. Dewi, R.-C. Chen, Y.-T. Liu, and S.-K. Tai, “Synthetic data
generative adversarial networks for generating synthetic healthcare generationusingdcganforimprovedtrafficsignrecognition,”Neural
records,”inInternationalFlairsConference,2020. ComputingandApplications,vol.34,no.24,pp.21465–21480,2022.
[27] D.Lee,H.Yu,X.Jiang,D.Rogith,M.Gudala,M.Tejani,Q.Zhang, [52] Z. Zhao, K. Xu, S. Li, Z. Zeng, and C. Guan, “Mt-uda: Towards
and L. Xiong, “Generating sequential electronic health records using unsupervisedcross-modalitymedicalimagesegmentationwithlimited
dualadversarialautoencoder,”JournaloftheAmericanMedicalInfor- source labels,” in Medical Image Computing and Computer Assisted
maticsAssociation,vol.27,no.9,pp.1411–1419,2020. Intervention(MICCAI). Springer,2021.
[28] S.Wharrie,Z.Yang,V.Raj,R.Monti,R.Gupta,Y.Wang,A.Martin, [53] S.Yi,M.Lu,A.Yee,J.Harmon,F.Meng,andS.Hinduja,“Enhance
L.J.O’Connor,S.Kaski,P.Marttinenetal.,“HAPNEST:anefficient wound healing monitoring through a thermal imaging based smart-
tool for generating large-scale genetics datasets from limited training phoneapp,”inMedicalImaging:ImagingInformaticsforHealthcare,
data,”inNeurIPS2022WorkshoponSyntheticDataforEmpowering Research,andApplications. SPIE,2018.
MLResearch,2022. [54] Y. Chen, W. Li, X. Chen, and L. V. Gool, “Learning semantic
[29] B.Nowok,G.M.Raab,andC.Dibben,“synthpop:Bespokecreation segmentationfromsyntheticdata:Ageometricallyguidedinput-output
of synthetic data in R,” Journal of statistical software, vol. 74, pp. adaptation approach,” in IEEE/CVF Conference on Computer Vision
1–26,2016. andPatternRecognition,2019.
[30] J.-Y. Zhu, T. Park, P. Isola, and A. A. Efros, “Unpaired image-to- [55] S.Sankaranarayanan,Y.Balaji,A.Jain,S.N.Lim,andR.Chellappa,
imagetranslationusingcycle-consistentadversarialnetworks,”inIEEE “Learning from synthetic data: Addressing domain shift for semantic
internationalconferenceoncomputervision,2017. segmentation,” in IEEE/CVF conference on computer vision and pat-
[31] R.Torkzadehmahani,P.Kairouz,andB.Paten,“Dp-cgan:Differentially ternrecognition,2018.
privatesyntheticdataandlabelgeneration,”inIEEE/CVFConference [56] H.-W. Dong and Y.-H. Yang, “Towards a deeper understanding of
onComputerVisionandPatternRecognitionWorkshops,2019. adversariallosses,”arXivpreprintarXiv:1901.08753,2019.
[32] A. Brock, J. Donahue, and K. Simonyan, “Large scale GAN [57] E. Wood, T. Baltrusˇaitis, C. Hewitt, S. Dziadzio, T. J. Cashman,
training for high fidelity natural image synthesis,” arXiv preprint and J. Shotton, “Fake it till you make it: face analysis in the wild
arXiv:1809.11096,2018. usingsyntheticdataalone,”inIEEE/CVFinternationalconferenceon
[33] J.Ho,T.Salimans,A.Gritsenko,W.Chan,M.Norouzi,andD.J.Fleet, computervision,2021.
“Videodiffusionmodels,”arXivpreprintarXiv:2204.03458,2022. [58] A. Werchniak, R. B. Chicote, Y. Mishchenko, J. Droppo, J. Condal,
[34] A. Razavi, A. Van den Oord, and O. Vinyals, “Generating diverse P. Liu, and A. Shah, “Exploring the application of synthetic audio
high-fidelity images with vq-vae-2,” Advances in neural information in training keyword spotters,” in IEEE International Conference on
processingsystems,vol.32,2019. Acoustics,SpeechandSignalProcessing(ICASSP),2021.
[35] M.NiemeyerandA.Geiger,“Giraffe:Representingscenesascompo- [59] W. Li, H. You, J. Zhu, and N. Chen, “Feature sparsity analysis for
sitionalgenerativeneuralfeaturefields,”inIEEE/CVFConferenceon i-vector based speaker verification,” Speech Communication, vol. 80,
ComputerVisionandPatternRecognition,2021. pp.60–70,2016.
[36] N. Chen, Y. Zhang, H. Zen, R. J. Weiss, M. Norouzi, and W. Chan, [60] Y.Qian,Y.Liu,andK.Yu,“Tandemdeepfeaturesfortext-dependent
“Wavegrad: Estimating gradients for waveform generation,” Interna- speaker verification,” in Fifteenth Annual Conference of the Interna-
tionalConferenceonLearningRepresentations(ICLR),2021. tionalSpeechCommunicationAssociation,2014.
[37] H.Guo,F.K.Soong,L.He,andL.Xie,“AnewGAN-basedend-to-end [61] Z.-H. Ling, L. Deng, and D. Yu, “Modeling spectral envelopes using
TTStrainingalgorithm,”arXivpreprintarXiv:1904.04775,2019. restrictedboltzmannmachinesanddeepbeliefnetworksforstatistical
[38] L.Yu,W.Zhang,J.Wang,andY.Yu,“Seqgan:Sequencegenerative parametricspeechsynthesis,”IEEEtransactionsonaudio,speech,and
adversarialnetswithpolicygradient,”inAAAIconferenceonartificial languageprocessing,vol.21,no.10,pp.2129–2139,2013.
intelligence,vol.31,no.1,2017. [62] A.Fazel,W.Yang,Y.Liu,R.Barra-Chicote,Y.Meng,R.Maas,and
[39] T.Sellam,D.Das,andA.P.Parikh,“Bleurt:Learningrobustmetrics J.Droppo,“Synthasr:Unlockingsyntheticdataforspeechrecognition,”
fortextgeneration,”arXivpreprintarXiv:2004.04696,2020. arXivpreprintarXiv:2106.07803,2021.
[40] Z.Shi,X.Chen,X.Qiu,andX.Huang,“Towarddiversetextgeneration [63] W. Li and J. Zhu, “An improved i-vector extraction algorithm for
withinversereinforcementlearning,”inInternationalJointConference speakerverification,”EURASIPJournalonAudio,Speech,andMusic
onArtificialIntelligence,2018. Processing,vol.2015,pp.1–9,2015.
[41] C.-Y.Ko,P.-Y.Chen,J.Mohapatra,P.Das,andL.Daniel,“Synbench: [64] G.Forman,“Anextensiveempiricalstudyoffeatureselectionmetrics
Task-agnostic benchmarking of pretrained representations using syn- fortextclassification,”JournalofMachineLearningResearch,vol.3,
theticdata,”arXivpreprintarXiv:2210.02989,2022. pp.1289–1305,2003.
[42] W. Nie, N. Narodytska, and A. Patel, “Relgan: Relational generative [65] X.Yue,H.A.Inan,X.Li,G.Kumar,J.McAnallen,H.Sun,D.Levitan,
adversarial networks for text generation,” in International conference and R. Sim, “Synthetic text generation with differential privacy: A
onlearningrepresentations,2018. simpleandpracticalrecipe,”arXivpreprintarXiv:2210.14348,2022.

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     | 15  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[66] X.Zheng,Y.Liu,D.Gunceler,andD.Willett,“Usingsyntheticaudio [89] Q. Wen, Z. Ouyang, J. Zhang, Y. Qian, Y. Ye, and C. Zhang, “Dis-
to improve the recognition of out-of-vocabulary words in end-to-end entangled dynamic heterogeneous graph learning for opioid overdose
asr systems,” in IEEE International Conference on Acoustics, Speech prediction,” in ACM SIGKDD Conference on Knowledge Discovery
| andSignalProcessing(ICASSP),2021. |     |     |     |     |     |     | andDataMining,2022. |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
[67] Y.Fu,Y.Lu,Y.Wang,B.Zhang,Z.Zhang,G.Yu,C.Liu,R.Clarke, [90] T.Fu,T.Gao,C.Xiao,T.Ma,andJ.Sun,“Pearl:Prototypelearning
D. M. Herrington, and Y. Wang, “Ddn3. 0: Determining significant viarulelearning,”inACMInternationalConferenceonBioinformatics,
ComputationalBiologyandHealthInformatics,2019,pp.223–232.
| rewiring | of biological | network | structure | with | differential | dependency |     |     |     |     |     |     |     |     |
| -------- | ------------- | ------- | --------- | ---- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
networks,”Bioinformatics,p.btae376,2024. [91] A.Goncalves,P.Ray,B.Soper,J.Stevens,L.Coyle,andA.P.Sales,
[68] Z. Zhao, A. Zhu, Z. Zeng, B. Veeravalli, and C. Guan, “Act-net: “Generation and evaluation of synthetic patient data,” BMC medical
Asymmetricco-teachernetworkforsemi-supervisedmemory-efficient researchmethodology,vol.20,no.1,pp.1–40,2020.
medical image segmentation,” in IEEE International Conference on [92] D. Du, S. Bhardwaj, S. J. Parker, Z. Cheng, Z. Zhang, Y. Lu, J. E.
VanEyk,G.Yu,R.Clarke,D.M.Herringtonetal.,“Abds:toolsuitefor
| ImageProcessing(ICIP). |     |     | IEEE,2022. |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
analyzingbiologicallydiversesamples,”bioRxiv,pp.2023–07,2023.
[69] R.J.Chen,M.Y.Lu,T.Y.Chen,D.F.Williamson,andF.Mahmood,
“Synthetic data in machine learning for medicine and healthcare,” [93] Y. Lu, “Multi-omics data integration for identifying disease specific
NatureBiomedicalEngineering,vol.5,no.6,pp.493–497,2021. biologicalpathways,”Ph.D.dissertation,VirginiaTech,2018.
[70] A. Tucker, Z. Wang, Y. Rotalinti, and P. Myles, “Generating high- [94] K. Bhanot, M. Qi, J. S. Erickson, I. Guyon, and K. P. Bennett, “The
|     |     |     |     |     |     |     | problem | of  | fairness | in synthetic | healthcare | data,” | Entropy, | vol. 23, |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | ------------ | ---------- | ------ | -------- | -------- |
fidelitysyntheticpatientdataforassessingmachinelearninghealthcare
no.9,p.1165,2021.
software,”NPJdigitalmedicine,vol.3,no.1,pp.1–13,2020.
[95] T.Fu,K.Huang,C.Xiao,L.M.Glass,andJ.Sun,“HINT:Hierarchical
| [71] Y. Wang, | Y. Lu, | Y. Xu, | Z. Ma, | H. Xu, B. | Du, H. | Gao, and J. Wu, |             |     |         |                            |     |               |     |           |
| ------------- | ------ | ------ | ------ | --------- | ------ | --------------- | ----------- | --- | ------- | -------------------------- | --- | ------------- | --- | --------- |
|               |        |        |        |           |        |                 | interaction |     | network | for clinical-trial-outcome |     | predictions,” |     | Patterns, |
“Twin-gpt:Digitaltwinsforclinicaltrialsvialargelanguagemodel,”
arXivpreprintarXiv:2404.01273,2024. vol.3,no.4,p.100445,2022.
|             |           |               |     |        |            |                | [96] T. | Fu, T. N. | Hoang, | C. Xiao, | and J. | Sun, “DDL: | Deep | dictionary |
| ----------- | --------- | ------------- | --- | ------ | ---------- | -------------- | ------- | --------- | ------ | -------- | ------ | ---------- | ---- | ---------- |
| [72] Y. Lu, | C.-T. Wu, | S. J. Parker, | Z.  | Cheng, | G. Saylor, | J. E. Van Eyk, |         |           |        |          |        |            |      |            |
learningforpredictivephenotyping,”inInternationalJointConference
G.Yu,R.Clarke,D.M.Herrington,andY.Wang,“Cot:anefficientand
onArtificialIntelligence,2019.
| accurate | method | for detecting | marker | genes | among | many subtypes,” |         |          |           |        |         |           |        |            |
| -------- | ------ | ------------- | ------ | ----- | ----- | --------------- | ------- | -------- | --------- | ------ | ------- | --------- | ------ | ---------- |
|          |        |               |        |       |       |                 | [97] L. | Chen, Y. | Lu, C.-T. | Wu, R. | Clarke, | G. Yu, J. | E. Van | Eyk, D. M. |
BioinformaticsAdvances,vol.2,no.1,p.vbac037,2022. Herrington, and Y. Wang, “Data-driven detection of subtype-specific
[73] J.DahmenandD.Cook,“Synsys:Asyntheticdatagenerationsystem differentially expressed genes,” Scientific reports, vol. 11, no. 1, pp.
forhealthcareapplications,”Sensors,vol.19,no.5,p.1181,2019.
1–12,2021.
[74] Y.Lu,Y.-T.Chang,E.P.Hoffman,G.Yu,D.M.Herrington,R.Clarke,
|     |     |     |     |     |     |     | [98] P. | Eigenschink, | S.  | Vamosi, | R. Vamosi, | C. Sun, | T. Reutterer, | and |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------- | ---------- | ------- | ------------- | --- |
C.-T.Wu,L.Chen,andY.Wang,“Integratedidentificationofdisease
|                                                              |     |     |     |     |     |     | K.                  | Kalcher, | “Deep generative |     | models for | synthetic | data,” | ACM Com- |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------------- | -------- | ---------------- | --- | ---------- | --------- | ------ | -------- |
| specificpathwaysusingmulti-omicsdata,”bioRxiv,p.666065,2019. |     |     |     |     |     |     | putingSurveys,2021. |          |                  |     |            |           |        |          |
[75] Z.Wang,P.Myles,andA.Tucker,“Generatingandevaluatingcross- [99] C.-T.Wu,M.Shen,D.Du,Z.Cheng,S.J.Parker,Y.Lu,J.E.VanEyk,
sectional synthetic electronic healthcare data: Preserving data utility G.Yu,R.Clarke,D.M.Herringtonetal.,“Cosbin:cosinescore-based
| and | patient privacy,” | Computational |     | Intelligence, | vol. | 37, no. 2, pp. |     |     |     |     |     |     |     |     |
| --- | ----------------- | ------------- | --- | ------------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
iterativenormalizationofbiologicallydiversesamples,”Bioinformatics
819–851,2021.
Advances,vol.2,no.1,p.vbac076,2022.
[76] R.S.Bohacek,C.McMartin,andW.C.Guida,“Theartandpractice [100] R.WangandX.Qu,“Eegdaydreaming,amachinelearningapproachto
of structure-based drug design: a molecular modeling perspective,” detectdaydreamingactivities,”inAugmentedCognition:International
Medicinalresearchreviews,vol.16,no.1,pp.3–50,1996. Conference. Springer,2022.
[77] K. Huang, T. Fu, L. M. Glass, M. Zitnik, C. Xiao, and J. Sun, [101] Y. Du, T. Fu, J. Sun, and S. Liu, “Molgensurvey: A systematic
“DeepPurpose: a deep learning library for drug–target interaction surveyinmachinelearningmodelsformoleculedesign,”arXivpreprint
prediction,”Bioinformatics,vol.36,no.22-23,pp.5545–5547,2020. arXiv:2203.14500,2022.
[78] R. Go´mez-Bombarelli, J. N. Wei, D. Duvenaud, J. M. Herna´ndez- [102] K.ElEmam,L.Mosquera,andR.Hoptroff,Practicalsyntheticdata
Lobato, B. Sa´nchez-Lengeling, D. Sheberla, J. Aguilera-Iparraguirre, generation: balancing privacy and the broad availability of data.
T.D.Hirzel,R.P.Adams,andA.Aspuru-Guzik,“Automaticchemical O’ReillyMedia,2020.
design using a data-driven continuous representation of molecules,” [103] M.ManninoandA.Abouzied,“Isthisreal?generatingsyntheticdata
ACScentralscience,vol.4,no.2,pp.268–276,2018. that looks real,” in ACM Symposium on User Interface Software and
[79] B. Zhang, Y. Fu, Y. Lu, Z. Zhang, R. Clarke, J. E. Van Eyk, Technology,2019.
D. M. Herrington, and Y. Wang, “DDN2.0: R and python packages [104] S. A. Assefa, D. Dervovic, M. Mahfouz, R. E. Tillman, P. Reddy,
for differential dependency network analysis of biological systems,” and M. Veloso, “Generating synthetic data in finance: opportunities,
|                          |     |     |     |     |     |     |            |     |                | ACM | International | Conference |     | on AI in |
| ------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | ------------- | ---------- | --- | -------- |
| bioRxiv,pp.2021–04,2021. |     |     |     |     |     |     | challenges |     | and pitfalls,” | in  |               |            |     |          |
Finance,2020.
[80] N.DeCaoandT.Kipf,“MolGAN:Animplicitgenerativemodelfor
[105] P.-H.Lu,P.-C.Wang,andC.-M.Yu,“Empiricalevaluationonsynthetic
smallmoleculargraphs,”arXivpreprintarXiv:1805.11973,2018.
datagenerationwithgenerativeadversarialnetwork,”inInternational
| [81] T. Fu | and J. Sun, | “Antibody | Complementarity |     | Determining | Regions |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --------- | --------------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
(CDRs) design using constrained energy model,” in ACM SIGKDD ConferenceonWebIntelligence,MiningandSemantics,2019.
|     |     |     |     |     |     |     | [106] M. | Hittmeir, | A. Ekelhart, | and | R. Mayer, | “On the | utility | of synthetic |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------ | --- | --------- | ------- | ------- | ------------ |
ConferenceonKnowledgeDiscoveryandDataMining,2022.
data:Anempiricalevaluationonmachinelearningtasks,”inInterna-
| [82] T. Fu, | W. Gao, | C. Xiao, | J. Yasonik, | C. W. | Coley, | and J. Sun, “Dif- |     |     |     |     |     |     |     |     |
| ----------- | ------- | -------- | ----------- | ----- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionalConferenceonAvailability,ReliabilityandSecurity,2019.
| ferentiable | scaffolding | tree | for molecular | optimization,” |     | International |          |          |            |               |     |             |      |           |
| ----------- | ----------- | ---- | ------------- | -------------- | --- | ------------- | -------- | -------- | ---------- | ------------- | --- | ----------- | ---- | --------- |
|             |             |      |               |                |     |               | [107] A. | M. Berg, | S. T. Mol, | G. Kismiho´k, | and | N. Sclater, | “The | role of a |
ConferenceonLearningRepresentations,2022.
referencesyntheticdatageneratorwithinthefieldoflearninganalytics.”
[83] M. Xu, L. Yu, Y. Song, C. Shi, S. Ermon, and J. Tang, “GeoDiff: A JournalofLearningAnalytics,vol.3,no.1,pp.107–128,2016.
geometricdiffusionmodelformolecularconformationgeneration,”in
[108] B.Howe,J.Stoyanovich,H.Ping,B.Herman,andM.Gee,“Synthetic
InternationalConferenceonLearningRepresentations,2021.
dataforsocialgood,”arXivpreprintarXiv:1710.08874,2017.
[84] Z.Zhou,S.Kearnes,L.Li,R.N.Zare,andP.Riley,“Optimizationof
|     |     |     |     |     |     |     | [109] P. | Bautista | and P. | S. Inventado, | “Protecting | student | privacy | with |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------ | ------------- | ----------- | ------- | ------- | ---- |
moleculesviadeepreinforcementlearning,”Scientificreports,vol.9,
|     |     |     |     |     |     |     | synthetic | data | from | generative | adversarial | networks,” | in International |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ---- | ---------- | ----------- | ---------- | ---------------- | --- |
no.1,pp.1–10,2019. ConferenceonArtificialIntelligenceinEducation. Springer,2021.
[85] J. H. Jensen, “A graph-based genetic algorithm and generative [110] H.Jiang,J.Li,P.Zhao,F.Zeng,Z.Xiao,andA.Iyengar,“Location
model/montecarlotreesearchfortheexplorationofchemicalspace,” privacy-preservingmechanismsinlocation-basedservices:Acompre-
Chemicalscience,vol.10,no.12,pp.3567–3572,2019.
hensivesurvey,”ACMComputingSurveys(CSUR),vol.54,no.1,pp.
| [86] T. Fu, | C. Xiao, | X. Li, L. | M. Glass, | and | J. Sun, “MIMOSA: | Multi- |     |     |     |     |     |     |     |     |
| ----------- | -------- | --------- | --------- | --- | ---------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
1–36,2021.
constraint molecule sampling for molecule optimization,” in AAAI [111] R.Kato,M.Iwata,T.Hara,A.Suzuki,X.Xie,Y.Arase,andS.Nishio,
ConferenceonArtificialIntelligence,2021. “A dummy-based anonymization method based on user trajectory
[87] T.FuandJ.Sun,“SIPF:Samplingmethodforinverseproteinfolding,” withpauses,”inInternationalConferenceonAdvancesinGeographic
in ACM SIGKDD Conference on Knowledge Discovery and Data InformationSystems,2012.
Mining,2022.
|     |     |     |     |     |     |     | [112] Y. | Du, S. | Wang, | X. Guo, | H. Cao, | S. Hu, J. | Jiang, | A. Varala, |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | ------- | ------- | --------- | ------ | ---------- |
[88] C. S. Kruse, B. Smith, H. Vanderlinden, and A. Nealand, “Security A. Angirekula, and L. Zhao, “GraphGT: Machine learning datasets
techniques for the electronic health records,” Journal of medical forgraphgenerationandtransformation,”inNeuralInformationPro-
systems,vol.41,no.8,pp.1–9,2017. cessingSystemsDatasetsandBenchmarksTrack,2021.

JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 16
[113] R.Chen,G.Acs,andC.Castelluccia,“Differentiallyprivatesequential [136] G. Papyshev and M. Yarime, “Exploring city digital twins as policy
data publication via variable-length n-grams,” in ACM conference on tools: A task-based approach to generating synthetic data on urban
Computerandcommunicationssecurity,2012. mobility,”Data&Policy,vol.3,p.e16,2021.
[114] C.Dwork,A.Rothetal.,“Thealgorithmicfoundationsofdifferential [137] Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond,
privacy,” Foundations and Trends® in Theoretical Computer Science, T. Eccles, J. Keeling, F. Gimeno, A. Dal Lago et al., “Competition-
vol.9,no.3–4,pp.211–407,2014. levelcodegenerationwithalphacode,”Science,vol.378,no.6624,pp.
[115] T.Cunningham,G.Cormode,H.Ferhatosmanoglu,andD.Srivastava, 1092–1097,2022.
“Real-worldtrajectorysharingwithlocaldifferentialprivacy,”Proceed- [138] T.Ye,Y.Du,T.Ma,L.Wu,X.Zhang,S.Ji,andW.Wang,“Uncovering
ingsoftheVLDBEndowment,vol.14,no.11,pp.2283–2295,2021. llm-generated code: A zero-shot synthetic code detector via code
[116] Y.Du,Y.Hu,Z.Zhang,Z.Fang,L.Chen,B.Zheng,andY.Gao,“Ldp- rewriting,”arXivpreprintarXiv:2405.16133,2024.
trace: Locally differentially private trajectory synthesis,” Proceedings [139] S. Ghosh, M. Chollet, E. Laksana, L.-P. Morency, and S. Scherer,
oftheVLDBEndowment,vol.16,no.8,pp.1897–1909,2023. “Affect-LM: Aneural language modelfor customizableaffective text
[117] X. He, G. Cormode, A. Machanavajjhala, C. M. Procopiuc, and generation,” in Annual Meeting of the Association for Computational
D. Srivastava, “Dpt: differentially private trajectory synthesis using Linguistics,2017.
hierarchicalreferencesystems,”VLDBEndowment,vol.8,no.11,pp. [140] D. P. Kingma and M. Welling, “Auto-encoding variational bayes,”
1154–1165,2015. InternationalConferenceonLearningRepresentations(ICLR),2014.
[118] S. Wang and R. O. Sinnott, “Protecting personal trajectories of so- [141] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,
cial media users through differential privacy,” Computers & Security, S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial nets,”
vol.67,pp.142–163,2017. inAdvancesinneuralinformationprocessingsystems,2014.
[119] M. E. Gursoy, L. Liu, S. Truex, L. Yu, and W. Wei, “Utility-aware [142] I.J.Goodfellow,“Ondistinguishabilitycriteriaforestimatinggenera-
synthesis of differentially private and attack-resilient location traces,” tivemodels,”arXivpreprintarXiv:1412.6515,2014.
inACMSIGSACconferenceoncomputerandcommunicationssecurity, [143] Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon,
2018. and B. Poole, “Score-based generative modeling through stochastic
[120] M.E.Gursoy,L.Liu,S.Truex,andL.Yu,“Differentiallyprivateand differentialequations,”arXivpreprintarXiv:2011.13456,2020.
utilitypreservingpublicationoftrajectorydata,”IEEETransactionson [144] R.S.SuttonandA.G.Barto,Reinforcementlearning:Anintroduction.
MobileComputing,vol.18,no.10,pp.2315–2329,2018. MITpress,2018.
[121] D.J.Mir,S.Isaacman,R.Ca´ceres,M.Martonosi,andR.N.Wright, [145] S.H.Lee,“Naturallanguagegenerationforelectronichealthrecords,”
“Dp-where: Differentially private modeling of human mobility,” in NPJdigitalmedicine,vol.1,no.1,pp.1–7,2018.
IEEEinternationalconferenceonbigdata. IEEE,2013. [146] W. Hu, B. Liu, J. Gomes, M. Zitnik, P. Liang, V. Pande, and
[122] H. Roy, M. Kantarcioglu, and L. Sweeney, “Practical differentially J. Leskovec, “Strategies for pre-training graph neural networks,” in
privatemodelingofhumanmovementdata,”inAnnualIFIPWG11.3 InternationalConferenceonLearningRepresentations,2019.
Working Conference on Data and Applications Security and Privacy. [147] C. P. Burgess, I. Higgins, A. Pal, L. Matthey, N. Watters, G. Des-
Springer,2016. jardins, and A. Lerchner, “Understanding disentangling in β-vae,”
[123] V. Bindschaedler and R. Shokri, “Synthesizing plausible privacy- arXivpreprintarXiv:1804.03599,2018.
preserving location traces,” in IEEE Symposium on Security and [148] A.VahdatandJ.Kautz,“Nvae:Adeephierarchicalvariationalautoen-
Privacy(SP),2016. coder,” Advances in neural information processing systems, vol. 33,
[124] H. Wang, Z. Zhang, T. Wang, S. He, M. Backes, J. Chen, and 2020.
Y. Zhang, “Privtrace: Differentially private trajectory synthesis by [149] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,
adaptivemarkovmodel,”inUSENIXSecuritySymposium2023,2023. S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial net-
[125] J. Narita, T. Murakami, H. Hino, M. Nishigaki, and T. Ohki, “Syn- works,” Communications of the ACM, vol. 63, no. 11, pp. 139–144,
thesizing differentially private location traces including co-locations,” 2020.
InternationalJournalofInformationSecurity,vol.23,no.1,pp.389– [150] Y.Zhang,Y.Qian,Y.Fan,Y.Ye,X.Li,Q.Xiong,andF.Shao,“dstyle-
410,2024. gan:Generativeadversarialnetworkbasedonwritingandphotography
[126] Y. Cao, S. Li, Y. Liu, Z. Yan, Y. Dai, P. S. Yu, and L. Sun, “A stylesfordrugidentificationindarknetmarkets,”inAnnualComputer
comprehensive survey of ai-generated content (aigc): A history of SecurityApplicationsConference,2020.
generative ai from gan to chatgpt,” arXiv preprint arXiv:2303.04226, [151] M. Arjovsky, S. Chintala, and L. Bottou, “Wasserstein generative
2023. adversarialnetworks,”inInternationalconferenceonmachinelearning.
[127] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. PMLR,2017.
Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” [152] Y.Zhang,Y.Qian,Y.Ye,andC.Zhang,“Adaptingdistilledknowledge
Advancesinneuralinformationprocessingsystems,2017. for few-shot relation reasoning over knowledge graphs,” in SIAM
[128] W. Tao, S. Gao, and Y. Yuan, “Boundary crossing: an experimental InternationalConferenceonDataMining(SDM),2022.
studyofindividualperceptionstowardaigc,”FrontiersinPsychology, [153] J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli,
vol.14,2023. “Deep unsupervised learning using nonequilibrium thermodynamics,”
[129] R.J.M.Ventayen,“Openaichatgptgeneratedresults:Similarityindex inInternationalConferenceonMachineLearning. PMLR,2015.
of artificial intelligence-based contents,” Available at SSRN 4332664, [154] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic
2023. models,”inAdvancesinNeuralInformationProcessingSystems,2020.
[130] T.Yue,D.Au,C.C.Au,andK.Y.Iu,“Democratizingfinancialknowl- [155] M. Liu, K. Yan, B. Oztekin, and S. Ji, “Graphebm: Molecu-
edge with chatgpt by openai: Unleashing the power of technology,” lar graph generation with energy-based models,” arXiv preprint
AvailableatSSRN4346152,2023. arXiv:2102.00546,2021.
[131] V. Cheng, V. M. Suriyakumar, N. Dullerud, S. Joshi, and M. Ghas- [156] L. Weng, “What are diffusion models?” lilianweng.github.io/lil-log,
semi, “Can you fake it until you make it? impacts of differentially 2021. [Online]. Available: https://lilianweng.github.io/lil-log/2021/07/
private synthetic data on downstream classification fairness,” in ACM 11/diffusion-models.html
ConferenceonFairness,Accountability,andTransparency,2021. [157] G. Somepalli, V. Singla, M. Goldblum, J. Geiping, and T. Goldstein,
[132] J. Hurst, K. Mayorov, and J. F. T. Tatsinkou, “The generation of “Diffusion art or digital forgery? investigating data replication in
synthetic data for risk modelling,” Journal of Risk Management in diffusionmodels,”arXivpreprintarXiv:2212.03860,2022.
FinancialInstitutions,vol.15,no.3,pp.260–269,2022. [158] K. Huang, T. Fu, W. Gao, Y. Zhao, Y. Roohani, J. Leskovec, C. W.
[133] Y.-L. Peng and W.-P. Lee, “Data selection to avoid overfitting for Coley, C. Xiao, J. Sun, and M. Zitnik, “Therapeutics data commons:
foreignexchangeintradaytradingwithmachinelearning,”AppliedSoft machine learning datasets and tasks for therapeutics,” NeurIPS Track
Computing,vol.108,p.107461,2021. DatasetsandBenchmarks,2021.
[134] M. J. Schneider, S. Jagpal, S. Gupta, S. Li, and Y. Yu, “A flexible [159] Y. Lu, T. Chen, N. Hao, C. Van Rechem, J. Chen, and T. Fu, “Un-
methodforprotectingmarketingdata:Anapplicationtopoint-of-sale certainty quantification and interpretability for clinical trial approval
data,”MarketingScience,vol.37,no.1,pp.153–171,2018. prediction,”HealthDataScience,vol.4,p.0126,2024.
[135] D.M.Smith,G.P.Clarke,andK.Harland,“Improvingthesynthetic [160] R.Shokri,M.Stronati,C.Song,andV.Shmatikov,“Membershipin-
data generation process in spatial microsimulation models,” Environ- ferenceattacksagainstmachinelearningmodels,”inIEEEsymposium
mentandPlanningA,vol.41,no.5,pp.1251–1268,2009. onsecurityandprivacy(SP),2017.

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     | 17  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[161] S. Truex, L. Liu, M. E. Gursoy, L. Yu, and W. Wei, “Demystifying [184] G.AstolfiandK.David,“Generatingtabulardatausinggenerativead-
membershipinferenceattacksinmachinelearningasaservice,”IEEE versarialnetworkswithdifferentialprivacy,”inConferenceofEuropean
| Transactions |     | on Services | Computing, | vol. | 14, no. | 6, pp. 2073–2089, | Statisticians,2021. |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | ---------- | ---- | ------- | ----------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
2019. [185] D. Chen, T. Orekondy, and M. Fritz, “Gs-wgan: A gradient-sanitized
[162] L.Melis,C.Song,E.DeCristofaro,andV.Shmatikov,“Exploitingun- approach for learning differentially private generators,” Advances in
intendedfeatureleakageincollaborativelearning,”inIEEEsymposium NeuralInformationProcessingSystems,vol.33,2020.
onsecurityandprivacy(SP),2019. [186] T. Cao, A. Bie, A. Vahdat, S. Fidler, and K. Kreis, “Don’t generate
L.Zhu,Z.Liu,andS.Han,“Deepleakagefromgradients,”Advances me: Training differentially private generative models with sinkhorn
[163]
inneuralinformationprocessingsystems,2019. divergence,” Advances in Neural Information Processing Systems,
| [164] W.Wei,L.Liu,M.Loper,K.-H.Chow,M.E.Gursoy,S.Truex,and |     |     |     |     |     |     | vol.34,2021. |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Y.Wu,“Aframeworkforevaluatingclientprivacyleakagesinfederated [187] A.Torfi,E.A.Fox,andC.K.Reddy,“Differentiallyprivatesynthetic
learning,”inEuropeanSymposiumonResearchinComputerSecurity. medical data generation using convolutional gans,” Information Sci-
ences,vol.586,pp.485–500,2022.
Springer,2020.
|                   |     |                  |     |         |        |                     | [188] L. | Fan and | A. Pokkunuru, | “Dpnet: | Differentially |     | private | network |
| ----------------- | --- | ---------------- | --- | ------- | ------ | ------------------- | -------- | ------- | ------------- | ------- | -------------- | --- | ------- | ------- |
| [165] J. Geiping, |     | H. Bauermeister, | H.  | Dro¨ge, | and M. | Moeller, “Inverting |          |         |               |         |                |     |         |         |
gradients-how easy is it to break privacy in federated learning?” trafficsynthesiswithgenerativeadversarialnetworks,”inIFIPAnnual
AdvancesinNeuralInformationProcessingSystems,2020. ConferenceonDataandApplicationsSecurityandPrivacy. Springer,
| [166] J.Hayes,L.Melis,G.Danezis,andE.DeCristofaro,“Logan:Mem- |     |     |     |     |     |     | 2021. |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
bership inference attacks against generative models,” Proceedings on [189] Y. Long, B. Wang, Z. Yang, B. Kailkhura, A. Zhang, C. Gunter, and
B.Li,“G-pate:Scalabledifferentiallyprivatedatageneratorviaprivate
PrivacyEnhancingTechnologies,2019.
aggregationofteacherdiscriminators,”AdvancesinNeuralInformation
| [167] B. Hitaj, | G.  | Ateniese, | and F. | Perez-Cruz, | “Deep | models under the |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ------ | ----------- | ----- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
gan: information leakage from collaborative deep learning,” in ACM ProcessingSystems,vol.34,2021.
SIGSACconferenceoncomputerandcommunicationssecurity,2017. [190] T.Cunningham,K.Klemmer,H.Wen,andH.Ferhatosmanoglu,“Geo-
[168] Z. Wang, M. Song, Z. Zhang, Y. Song, Q. Wang, and H. Qi, “Be- pointgan: Synthetic spatial data with local label differential privacy,”
arXivpreprintarXiv:2205.08886,2022.
| yond | inferring | class representatives: |     | User-level | privacy | leakage from |     |     |     |     |     |     |     |     |
| ---- | --------- | ---------------------- | --- | ---------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[191] M.Vinaroz,M.-A.Charusaie,F.Harder,K.Adamczewski,andM.J.
federatedlearning,”inIEEEconferenceoncomputercommunications,
|     |     |     |     |     |     |     | Park, | “Hermite | polynomial | features | for private | data | generation,” | in  |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ---------- | -------- | ----------- | ---- | ------------ | --- |
2019.
|                |     |       |             |         |            |                | InternationalConferenceonMachineLearning. |     |     |     |     | PMLR,2022. |     |     |
| -------------- | --- | ----- | ----------- | ------- | ---------- | -------------- | ----------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- |
| [169] G. Ganev | and | E. De | Cristofaro, | “On the | inadequacy | of similarity- |                                           |     |     |     |     |            |     |     |
basedprivacymetrics:Reconstructionattacksagainst”trulyanonymous [192] F. Harder, K. Adamczewski, and M. Park, “Dp-merf: Differentially
syntheticdata”,”arXivpreprintarXiv:2312.05114,2023. private mean embeddings with randomfeatures for practical privacy-
|                     |     |                |     |            |        |               | preserving                 |     | data generation,” | in         | International | conference | on  | artificial |
| ------------------- | --- | -------------- | --- | ---------- | ------ | ------------- | -------------------------- | --- | ----------------- | ---------- | ------------- | ---------- | --- | ---------- |
| [170] B. Hilprecht, |     | M. Ha¨rterich, | and | D. Bernau, | “Monte | carlo and re- |                            |     |                   |            |               |            |     |            |
|                     |     |                |     |            |        |               | intelligenceandstatistics. |     |                   | PMLR,2021. |               |            |     |            |
constructionmembershipinferenceattacksagainstgenerativemodels,”
|     |     |     |     |     |     |     | [193] R. | Chen, Q. | Xiao, Y. Zhang, | and | J. Xu, “Differentially |     | private | high- |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------------- | --- | ---------------------- | --- | ------- | ----- |
ProceedingsonPrivacyEnhancingTechnologies,2019.
|     |     |     |     |     |     |     | dimensional |     | data publication | via | sampling-based | inference,” |     | in ACM |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------------- | --- | -------------- | ----------- | --- | ------ |
[171] Y.Xu,S.Mukherjee,X.Liu,S.Tople,R.M.Dodhia,andJ.M.L.Fer-
res, “Mace: A flexible framework for membership privacy estimation SIGKDD international conference on knowledge discovery and data
mining,2015.
| in generative |     | models,” | Transactions | on  | Machine | Learning Research, |     |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ------------ | --- | ------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[194] K.Cai,X.Lei,J.Wei,andX.Xiao,“Datasynthesisviadifferentially
2022.
privatemarkovrandomfields,”VLDBEndowment,vol.14,no.11,pp.
| [172] T. | Stadler, | B. Oprisanu, | and | C. Troncoso, |     | “Synthetic data– |     |     |     |     |     |     |     |     |
| -------- | -------- | ------------ | --- | ------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2190–2202,2021.
anonymisationgroundhogday,”inUSENIXSecuritySymposium,2022.
|     |     |     |     |     |     |     | [195] R. | McKenna, | B. Mullins, | D.  | Sheldon, and | G. Miklau, | “Aim: | An  |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----------- | --- | ------------ | ---------- | ----- | --- |
[173] D. Chen, N. Yu, Y. Zhang, and M. Fritz, “Gan-leaks: A taxonomy adaptive and iterative mechanism for differentially private synthetic
ACM
of membership inference attacks against generative models,” in data,”arXivpreprintarXiv:2201.12677,2022.
SIGSACconferenceoncomputerandcommunicationssecurity,2020.
[196] C.-H.Lin,C.-M.Yu,andC.-Y.Huang,“Dpview:Differentiallyprivate
| [174] V. Bindschaedler, |                    | R. Shokri, | andC.            | A. Gunter, | “Plausible      | deniability |      |           |         |        |                    |     |               |     |
| ----------------------- | ------------------ | ---------- | ---------------- | ---------- | --------------- | ----------- | ---- | --------- | ------- | ------ | ------------------ | --- | ------------- | --- |
|                         |                    |            |                  |            |                 |             | data | synthesis | through | domain | size information,” |     | IEEE Internet | of  |
| for                     | privacy-preserving |            | data synthesis,” |            | VLDB Endowment, | vol. 10,    |      |           |         |        |                    |     |               |     |
ThingsJournal,vol.9,no.17,pp.15886–15900,2022.
no.5,2017.
|     |     |     |     |     |     |     | [197] V. | Chandrasekaran, | D.  | Edge, | S. Jha, A. | Sharma, | C. Zhang, | and |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ----- | ---------- | ------- | --------- | --- |
[175] B.-W.TsengandP.-Y.Wu,“Compressiveprivacygenerativeadversarial S.Tople,“Causallyconstraineddatasynthesisforprivatedatarelease,”
network,” IEEE Transactions on Information Forensics and Security, arXivpreprintarXiv:2105.13144,2021.
vol.15,pp.2499–2513,2020.
[198] J.Zhang,G.Cormode,C.M.Procopiuc,D.Srivastava,andX.Xiao,
[176] X.Zhang,S.Ji,andT.Wang,“Differentiallyprivatereleasingviadeep
|     |     |     |     |     |     |     | “Privbayes: |     | Private data | release | via bayesian | networks,” | ACM | Trans- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | ------- | ------------ | ---------- | --- | ------ |
generativemodel(technicalreport),”arXivpreprintarXiv:1801.01594,
actionsonDatabaseSystems(TODS),vol.42,no.4,pp.1–41,2017.
2018.
[199] C.Ge,S.Mohapatra,X.He,andI.F.Ilyas,“Kamino:Constraint-aware
[177] L. Xie, K. Lin, S. Wang, F. Wang, and J. Zhou, “Differentially pri- differentiallyprivatedatasynthesis,”arXivpreprintarXiv:2012.15713,
| vategenerativeadversarialnetwork,”arXivpreprintarXiv:1802.06739, |     |     |     |     |     |     | 2020. |     |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
2018.
|     |     |     |     |     |     |     | [200] M. | Gaboardi, | E. J. G. Arias, | J.  | Hsu, A. Roth, | and | Z. S. Wu, | “Dual |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --------------- | --- | ------------- | --- | --------- | ----- |
[178] C.Xu,J.Ren,D.Zhang,Y.Zhang,Z.Qin,andK.Ren,“Ganobfusca-
|     |     |     |     |     |     |     | query: | Practical | private | query release | for | high dimensional |     | data,” in |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------- | ------------- | --- | ---------------- | --- | --------- |
tor:Mitigatinginformationleakageunderganviadifferentialprivacy,”
InternationalConferenceonMachineLearning,2014.
IEEE Transactions on Information Forensics and Security, vol. 14, [201] M.Hardt,K.Ligett,andF.McSherry,“Asimpleandpracticalalgorithm
no.9,pp.2358–2371,2019. fordifferentiallyprivatedatarelease,”Advancesinneuralinformation
[179] A. Triastcyn and B. Faltings, “Federated generative privacy,” IEEE processingsystems,2012.
IntelligentSystems,vol.35,no.4,pp.50–57,2020. [202] Z. Zhang, T. Wang, N. Li, J. Honorio, M. Backes, S. He, J. Chen,
[180] P.-H.LuandC.-M.Yu,“Poster:Aunifiedframeworkofdifferentially and Y. Zhang, “{PrivSyn}: Differentially private data synthesis,” in
privatesyntheticdatareleasewithgenerativeadversarialnetwork,”in USENIXSecuritySymposium,2021.
ACMSIGSACConferenceonComputerandCommunicationsSecurity, [203] Q. Chen, C. Xiang, M. Xue, B. Li, N. Borisov, D. Kaarfar, and
2017. H.Zhu,“Differentiallyprivatedatagenerativemodels,”arXivpreprint
[181] Y. Liu, J. Peng, J. James, and Y. Wu, “Ppgan: Privacy-preserving arXiv:1812.02274,2018.
generative adversarial network,” in IEEE international conference on [204] E. Bao, X. Xiao, J. Zhao, D. Zhang, and B. Ding, “Synthetic data
| parallelanddistributedsystems(ICPADS). |     |     |     |     | IEEE,2019. |     |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
generationwithdifferentialprivacyviabayesiannetworks,”Journalof
[182] L. Frigerio, A. S. de Oliveira, L. Gomez, and P. Duverger, “Dif- PrivacyandConfidentiality,2021.
ferentially private generative adversarial networks for time series, [205] F. Liu, Z. Cheng, H. Chen, Y. Wei, L. Nie, and M. Kankanhalli,
continuous, and discrete open data,” in IFIP TC 11 International “Privacy-preservingsyntheticdatagenerationforrecommendationsys-
ConferenceonICTSystemsSecurityandPrivacyProtection. Springer, tems,” in ACM SIGIR Conference on Research and Development in
| 2019,pp.151–164. |     |     |     |     |     |     | InformationRetrieval,2022. |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
[183] B.K.Beaulieu-Jones,Z.S.Wu,C.Williams,R.Lee,S.P.Bhavnani, [206] J.-W.Chen,C.-M.Yu,C.-C.Kao,T.-W.Pang,andC.-S.Lu,“Dpgen:
J.B.Byrd,andC.S.Greene,“Privacy-preservinggenerativedeepneu- Differentially private generative energy-guided network for natural
ralnetworkssupportclinicaldatasharing,”Circulation:Cardiovascular image synthesis,” in IEEE/CVF Conference on Computer Vision and
QualityandOutcomes,vol.12,no.7,p.e005122,2019. PatternRecognition,2022.

| JOURNALOFLATEXCLASSFILES,VOL.14,NO.8,AUGUST2021 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 18  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[207] Z. Zhang, T. Wang, N. Li, S. He, and J. Chen, “Calm: Consistent private fine-tuning of language models,” in International Conference
adaptive local marginal for marginal release under local differential onLearningRepresentations,2021.
privacy,”inACMSIGSACConferenceonComputerandCommunica- [232] W. Wei and L. Liu, “Trustworthy distributed ai systems: Robustness,
tionsSecurity,2018. privacy,andgovernance,”ACMComputingSurveys,2024.
[208] W. Qardaji, W. Yang, and N. Li, “Priview: practical differentially [233] B. Oprisanu, G. Ganev, and E. De Cristofaro, “Measuring utility and
private release of marginal contingency tables,” in ACM SIGMOD privacyofsyntheticgenomicdata,”arXivpreprintarXiv:2102.03314,
| internationalconferenceonManagementofdata,2014. |     |     |     |     |     |     |     | 2021. |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
[209] L. Sweeney, “k-anonymity: A model for protecting privacy,” Interna- [234] M.Pereira,M.Kshirsagar,S.Mukherjee,R.Dodhia,andJ.Ferres,“An
tionaljournalofuncertainty,fuzzinessandknowledge-basedsystems, analysis of the deployment of models trained on private tabular syn-
vol.10,no.05,pp.557–570,2002. theticdata:Unexpectedsurprises,”arXivpreprintarXiv:2106.10241.
[210] P.SamaratiandL.Sweeney,“Generalizingdatatoprovideanonymity [235] G.Ganev,B.Oprisanu,andE.DeCristofaro,“Robinhoodandmatthew
effects:Differentialprivacyhasdisparateimpactonsyntheticdata,”in
| when | disclosing | information,” |     | in ACM | SIGACT-SIGMOD-SIGART |     |     |     |     |     |     |     |     |     |     |
| ---- | ---------- | ------------- | --- | ------ | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SymposiumonPrinciplesofDatabaseSystems,1998. InternationalConferenceonMachineLearning. PMLR,2022.
[211] P. Samarati, “Protecting respondents identities in microdata release,” [236] N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman, and A. Galstyan,
IEEEtransactionsonKnowledgeandDataEngineering,vol.13,no.6, “Asurveyonbiasandfairnessinmachinelearning,”ACMComputing
| pp.1010–1027,2001. |           |            |     |        |          |              |     | Surveys(CSUR),vol.54,no.6,pp.1–35,2021. |           |             |     |              |             |     |             |
| ------------------ | --------- | ---------- | --- | ------ | -------- | ------------ | --- | --------------------------------------- | --------- | ----------- | --- | ------------ | ----------- | --- | ----------- |
|                    |           |            |     |        |          |              |     | [237] A.                                | Abusitta, | E. A¨ımeur, | and | O. A. Wahab, | “Generative |     | adversarial |
| [212] B.           | Barak, K. | Chaudhuri, | C.  | Dwork, | S. Kale, | F. McSherry, | and |                                         |           |             |     |              |             |     |             |
K.Talwar,“Privacy,accuracy,andconsistencytoo:aholisticsolution networks for mitigating biases in machine learning systems,” arXiv
to contingency table release,” in ACM SIGMOD-SIGACT-SIGART preprintarXiv:1905.09972,2019.
symposiumonPrinciplesofdatabasesystems,2007. [238] F.H.K.d.S.TanakaandC.Aranha,“Dataaugmentationusinggans,”
arXivpreprintarXiv:1904.09135,2019.
| [213] J. | C. Duchi, | M. I. Jordan, | and | M. J. Wainwright, |     | “Local | privacy and |          |          |                 |     |             |           |     |             |
| -------- | --------- | ------------- | --- | ----------------- | --- | ------ | ----------- | -------- | -------- | --------------- | --- | ----------- | --------- | --- | ----------- |
|          |           |               |     |                   |     |        |             | [239] G. | Mariani, | F. Scheidegger, |     | R. Istrate, | C. Bekas, | and | C. Malossi, |
statisticalminimaxrates,”inIEEEAnnualSymposiumonFoundations
|     |     |     |     |     |     |     |     | “Bagan: | Data | augmentation |     | with balancing | gan,” | arXiv | preprint |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------------ | --- | -------------- | ----- | ----- | -------- |
ofComputerScience,2013.
[214] S.-Y.Kung,“Compressiveprivacy:Frominformation\/estimationthe- arXiv:1803.09655,2018.
orytomachinelearning,”IEEESignalProcessingMagazine,vol.34, [240] E. Barbierato, M. L. D. Vedova, D. Tessera, D. Toti, and N. Vanoli,
|     |     |     |     |     |     |     |     | “A  | methodology | for | controlling | bias and | fairness | in synthetic | data |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | -------- | -------- | ------------ | ---- |
no.1,pp.94–112,2017.
generation,”AppliedSciences,vol.12,no.9,p.4619,2022.
| [215] H. | Li, L. Xiong,     | and | X. Jiang,  | “Differentially |             | private synthesization |     |          |        |          |        |            |           |                |     |
| -------- | ----------------- | --- | ---------- | --------------- | ----------- | ---------------------- | --- | -------- | ------ | -------- | ------ | ---------- | --------- | -------------- | --- |
|          |                   |     |            |                 |             |                        |     | [241] D. | Xu, S. | Yuan, L. | Zhang, | and X. Wu, | “Fairgan: | Fairness-aware |     |
| of       | multi-dimensional |     | data using | copula          | functions,” | in International       |     |          |        |          |        |            |           |                |     |
ConferenceonExtendingDatabaseTechnology. NIHPublicAccess, generativeadversarialnetworks,”inIEEEInternationalConferenceon
| 2014.    |           |        |        |                 |     |                |      | BigData,2018.                                                     |      |            |          |      |          |            |         |
| -------- | --------- | ------ | ------ | --------------- | --- | -------------- | ---- | ----------------------------------------------------------------- | ---- | ---------- | -------- | ---- | -------- | ---------- | ------- |
|          |           |        |        |                 |     |                |      | [242] P.Sattigeri,S.C.Hoffman,V.Chenthamarakshan,andK.R.Varshney, |      |            |          |      |          |            |         |
| [216] N. | Patki, R. | Wedge, | and K. | Veeramachaneni, |     | “The synthetic | data |                                                                   |      |            |          |      |          |            |         |
|          |           |        |        |                 |     |                |      | “Fairness                                                         | gan: | Generating | datasets | with | fairness | properties | using a |
vault,”inIEEEinternationalconferenceondatascienceandadvanced
generativeadversarialnetwork,”IBMJournalofResearchandDevel-
| analytics(DSAA). |     |     | IEEE,2016. |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
opment,vol.63,no.4/5,pp.3–1,2019.
[217] S.Gambs,F.Ladouceur,A.Laurent,andA.Roy-Gaumond,“Growing
syntheticdatathroughdifferentially-privatevinecopulas,”Proceedings [243] B. Van Breugel, T. Kyono, J. Berrevoets, and M. Van der Schaar,
|     |     |     |     |     |     |     |     | “Decaf: | Generating | fair | synthetic | data | using causally-aware |     | genera- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ---- | --------- | ---- | -------------------- | --- | ------- |
onPrivacyEnhancingTechnologies,2021.
|     |     |     |     |     |     |     |     | tive | networks,” | Advances | in  | Neural Information |     | Processing | Systems, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | -------- | --- | ------------------ | --- | ---------- | -------- |
[218] H.J.Asghar,M.Ding,T.Rakotoarivelo,S.Mrabet,andM.A.Kaafar,
vol.34,2021.
| “Differentially |     | private | release | of high-dimensional |     | datasets | using the |                                                                     |     |     |     |     |     |     |     |
| --------------- | --- | ------- | ------- | ------------------- | --- | -------- | --------- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                 |     |         |         |                     |     |          |           | [244] E.Bagdasaryan,O.Poursaeed,andV.Shmatikov,“Differentialprivacy |     |     |     |     |     |     |     |
gaussiancopula,”arXivpreprintarXiv:1902.01499,2019.
[219] T.Rekatsinas,X.Chu,I.F.Ilyas,andC.Re´,“Holoclean:Holisticdata hasdisparateimpactonmodelaccuracy,”Advancesinneuralinforma-
tionprocessingsystems,vol.32,2019.
repairswithprobabilisticinference,”arXivpreprintarXiv:1702.00820,
|     |     |     |     |     |     |     |     | [245] L. | Weidinger, | J. Mellor, | M. Rauh, | C.Griffin, | J.  | Uesato, | P.-S. Huang, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ---------- | -------- | ---------- | --- | ------- | ------------ |
2017.
M.Cheng,M.Glaese,B.Balle,A.Kasirzadehetal.,“Ethicalandsocial
[220] H.Wang,S.Sudalairaj,J.Henning,K.Greenewald,andA.Srivastava,
risksofharmfromlanguagemodels,”arXivpreprintarXiv:2112.04359,
“Post-processingprivatesyntheticdataforimprovingutilityonselected
| measures,”AdvancesinNeuralInformationProcessingSystems,2024. |          |            |             |     |            |                  |     | 2021.                                                             |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | -------- | ---------- | ----------- | --- | ---------- | ---------------- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                                                              |          |            |             |     |            |                  |     | [246] G.K.Anumanchipalli,J.Chartier,andE.F.Chang,“Speechsynthesis |     |     |     |     |     |     |     |
| [221] N.                                                     | Carlini, | F. Tramer, | E. Wallace, | M.  | Jagielski, | A. Herbert-Voss, |     |                                                                   |     |     |     |     |     |     |     |
fromneuraldecodingofspokensentences,”Nature,vol.568,no.7753,
| K.  | Lee, A. | Roberts, | T. B. Brown, | D.  | Song, | U. Erlingsson | et al., |     |     |     |     |     |     |     |     |
| --- | ------- | -------- | ------------ | --- | ----- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.493–498,2019.
| “Extracting |     | training | data from | large | language | models.” | in USENIX |          |         |              |     |           |         |             |       |
| ----------- | --- | -------- | --------- | ----- | -------- | -------- | --------- | -------- | ------- | ------------ | --- | --------- | ------- | ----------- | ----- |
|             |     |          |           |       |          |          |           | [247] C. | Yan, Y. | Yan, Z. Wan, | Z.  | Zhang, L. | Omberg, | J. Guinney, | S. D. |
SecuritySymposium,2021.
Mooney,andB.A.Malin,“Amultifacetedbenchmarkingofsynthetic
[222] N. Carlini, J. Hayes, M. Nasr, M. Jagielski, V. Sehwag, F. Tramer, electronic health record generation models,” Nature Communications,
| B.  | Balle, D. | Ippolito, | and E. Wallace, |     | “Extracting | training | data from |     |     |     |     |     |     |     |     |
| --- | --------- | --------- | --------------- | --- | ----------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
vol.13,no.1,pp.1–18,2022.
diffusionmodels,”arXivpreprintarXiv:2301.13188,2023.
|     |     |     |     |     |     |     |     | [248] C. | Esteban, | S. L. Hyland, | and | G. Ra¨tsch, | “Real-valued |     | (medical) |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------------- | --- | ----------- | ------------ | --- | --------- |
[223] C.Meehan,K.Chaudhuri,andS.Dasgupta,“Anon-parametrictestto
timeseriesgenerationwithrecurrentconditionalgans,”arXivpreprint
detectdata-copyingingenerativemodels,”inInternationalConference arXiv:1706.02633,2017.
onArtificialIntelligenceandStatistics,2020. [249] Z. Zhao, F. Zhou, Z. Zeng, C. Guan, and S. K. Zhou, “Meta-
[224] Q. Feng, C. Guo, F. Benitez-Quiroz, and A. M. Martinez, “When hallucinator:Towardsfew-shotcross-modalitycardiacimagesegmenta-
| do  | gans replicate? |     | on the choice | of  | dataset | size,” in | IEEE/CVF |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | ------------- | --- | ------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
tion,”inMedicalImageComputingandComputerAssistedIntervention
InternationalConferenceonComputerVision,2021.
|     |     |     |     |     |     |     |     | (MICCAI). |     | Springer,2022. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- |
[225] N. Kandpal, E. Wallace, and C. Raffel, “Deduplicating training data [250] H. Huang, K. Mehrotra, and C. K. Mohan, “Rank-based outlier
mitigates privacy risks in language models,” in International Confer- detection,”JournalofStatisticalComputationandSimulation,vol.83,
| enceonMachineLearning. |     |     | PMLR,2022. |     |     |     |     | no.3,pp.518–531,2013. |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ---------- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
[226] T.Dockhorn,T.Cao,A.Vahdat,andK.Kreis,“Differentiallyprivate
diffusionmodels,”arXivpreprintarXiv:2210.09929,2022.
[227] Y.-L.Tsai,Y.Li,Z.Chen,P.-Y.Chen,C.-M.Yu,X.Ren,andF.Buet-
Golfouse,“Differentiallyprivatefine-tuningofdiffusionmodels,”arXiv
preprintarXiv:2406.01355,2024.
| [228] H. | Wang, S. | Pang, | Z. Lu, Y. | Rao, | Y. Zhou, | and M. | Xue, “dp- |     |     |     |     |     |     |     |     |
| -------- | -------- | ----- | --------- | ---- | -------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
promise:Differentiallyprivatediffusionprobabilisticmodelsforimage
synthesis,”inUSENIXSecuritySymposium,2024.
| [229] S. | Lyu, M. | F. Liu, | M. Vinaroz, | and M. | Park, | “Differentially | private |     |     |     |     |     |     |     |     |
| -------- | ------- | ------- | ----------- | ------ | ----- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
latentdiffusionmodels,”arXivpreprintarXiv:2305.15759,2023.
[230] J.Lebensold,M.Sanjabi,P.Astolfi,A.Romero-Soriano,K.Chaudhuri,
M.Rabbat,andC.Guo,“Dp-rdm:Adaptingdiffusionmodelstoprivate
domainswithoutfine-tuning,”arXivpreprintarXiv:2403.14421,2024.
| [231] D. | Yu, S. | Naik, A. | Backurs, | S. Gopi, | H.  | A. Inan, | G. Kamath, |     |     |     |     |     |     |     |     |
| -------- | ------ | -------- | -------- | -------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
J.Kulkarni,Y.T.Lee,A.Manoel,L.Wutschitzetal.,“Differentially