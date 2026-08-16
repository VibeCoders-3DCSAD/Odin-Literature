---
conversion_metadata:
  converted_at: "2026-07-22T12:36:16Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Cao et al.pdf"
  source_pdf_sha256: "062d67e3fde89c3bf13d4d67b2c466e4c75451a020b92ad1d714fcba8ff6ec1c"
  page_count: 33
  markdown_char_count: 237081
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Published as a conference paper at ICLR 2024

TEMPO: PROMPT-BASED GENERATIVE PRE-TRAINED
TRANSFORMER FOR TIME SERIES FORECASTING

Defu Cao1, Furong Jia1, Sercan ¨O. Arık2, Tomas Pfister2, Yixiang Zheng1, Wen Ye1, Yan Liu1
1 University of Southern California
2 Google Cloud AI Research
{defucao, florajia, yixiangzheng, yewen, yanliu.cs}@usc.edu
{soarik, tpfister}@google.com,

ABSTRACT

The past decade has witnessed significant advances in time series modeling with
deep learning. While achieving state-of-the-art results, the best-performing ar-
chitectures vary highly across applications and domains. Meanwhile, for natural
language processing, the Generative Pre-trained Transformer (GPT) has demon-
strated impressive performance via training one general-purpose model across
various textual datasets. It is intriguing to explore whether GPT-type architec-
tures can be effective for time series, capturing the intrinsic dynamic attributes
and leading to significant accuracy improvements. In this paper, we propose a
novel framework, TEMPO, that can effectively learn time series representations.
We focus on utilizing two essential inductive biases of the time series task for
pre-trained models: (i) decomposition of the complex interaction between trend,
seasonal and residual components; and (ii) introducing the design of prompts to
facilitate distribution adaptation in different types of time series. TEMPO expands
the capability for dynamically modeling real-world temporal phenomena from data
within diverse domains. Our experiments demonstrate the superior performance of
TEMPO over state-of-the-art methods on zero shot setting for a number of time
series benchmark datasets. This performance gain is observed not only in scenarios
involving previously unseen datasets but also in scenarios with multi-modal inputs.
This compelling finding highlights TEMPO’s potential to constitute a foundational
model-building framework.

1

INTRODUCTION

Time series forecasting, i.e., predicting future data based on historical observations, has broad real-
world applications, such as health, transportation, finance and so on. In the past decade, numerous
deep neural network architectures have been applied to time series modeling, including convolutional
neural networks (CNN) (Bai et al., 2018), recurrent neural networks (RNN) (Siami-Namini et al.,
2018), graph neural networks (GNN) (Li et al., 2018; Cao et al., 2021), and Transformers (Liu et al.,
2021; Zhou et al., 2021; Wu et al., 2023; Zhou et al., 2022; Woo et al., 2022; Kitaev et al., 2020; Nie
et al., 2023), leading to state-of-the-arts results. While achieving strong prediction performance, some
of the previous works on time series mostly benefit from the advance in sequence modeling (from
RNN and GNN, to transformers) that captures temporal dependencies but have not fully capitalized
on the benefits of intricate patterns within time series data, such as seasonality, trend, and residual.
These components are the key differentiating factors of time series from classical sequence data
(Fildes et al., 1991). As a result, recent studies suggest that deep learning-based architectures might
not be as robust as previously thought and might even be outperformed by shallow neural networks
or even linear models on some benchmarks (Zeng et al., 2023; Zhang et al., 2022b; Wu et al., 2023;
Ekambaram et al., 2023; Fan et al., 2022). Despite the notable success of deep learning forecasters,
the vast majority of them still follow a conventional training mechanism, training and predicting
using the same datasets.

Meanwhile, the rise of foundation models in natural language processing (NLP) and computer vision
(CV), such as LLaMA (Touvron et al., 2023), CLIP (Radford et al., 2021) and ChatGPT, marks

1

---

<!-- PAGE 2 -->

Published as a conference paper at ICLR 2024

major milestones on effective representation learning. It is extremely intriguing to explore a pre-
trained path for foundation time series models with vast amounts of data, facilitating performance
improvement in downstream tasks. Some recent works shed light into the possibility of building
general transformers for time series (Zhou et al., 2023; Sun et al., 2023; Goswami et al., 2024;
Das et al., 2023b; Rasul et al., 2023). However, the theoretical and practical understanding of such
models has not reached the consensus observed in other domains where generative models have been
widely acknowledged (Garza & Mergenthaler-Canseco, 2023). In addition, prompting techniques in
LLM (such as InstructGPT (Ouyang et al., 2022)) provide a way to leverage the model’s existing
representations during pre-training instead of requiring learning from scratch. However, existing
backbone structures and prompt techniques in language models do not fully capture the evolution of
temporal patterns as in N-BEATS (Oreshkin et al., 2019) and AutoFormer (Wu et al., 2021), which
are fundamental for time series modeling.

In this paper, we make an attempt to address the timely challenges of adapting large pre-trained models
for time series forecasting tasks and developing a prompt-based generative pre-training transformer
for time series, namely TEMPO. TEMPO consists of two key analytical components for effective time
series representation learning: one focuses on modeling specific time series patterns, such as trends
and seasonality, and the other concentrates on obtaining more universal and transferrable insights
from the inherent properties of data through a prompt-based approach. Specifically, TEMPO firstly
decomposes time series input into three additive components, i.e., trend, seasonality, and residuals
via locally weighted scatterplot smoothing (Cleveland et al., 1990). Each of these temporal inputs is
subsequently mapped to its corresponding hidden space to construct the time series input embedding
of the generative pre-trained transformer (GPT). We conduct a formal analysis, bridging the time
series domain with the frequency domain, to highlight the necessity of decomposing such components
for time series analysis. In addition, we theoretically reveal that the attention mechanism is hard
to achieve the decomposition automatically. Second, TEMPO utilizes a soft prompt to efficiently
tune the GPT (Radford et al., 2019) for forecasting tasks by guiding the reuse of a collection of
learnable continuous vector representations that encode temporal knowledge of trend and seasonality.
In addition, we leverage the three key additive components of time series data—trend, seasonality,
and residuals— to provide an interpretable framework for comprehending the interactions among
input components (Hastie, 2017). Experiment results on zero shot setting and multimodal setting of
TEMPO pave the path to foundational models for time series. Besides, we demonstrate the stable
predictive power of our model on unseen samples with textual information on two multimodal datasets
including TETS (Text for Time Series) dataset, which is first introduced in this work to foster further
research topics of pre-trained time series models.

In summary, the main contributions of our paper include: (1) We introduce an interpretable prompt-
tuning-based generative transformer, TEMPO, for time series representation learning. It further
drives a paradigm shift in time series forecasting - from conventional deep learning methods to
pre-trained foundational models. (2) We adapt pre-trained models for time series by focusing on
two fundamental inductive biases: First, we utilize decomposed trend, seasonality, and residual
information. Second, we explore the soft prompt strategies to accommodate time series data’s
dynamic nature. (3) Through extensive experimentation on benchmark datasets and two multimodal
datasets, our model demonstrates superior performance. Notably, our robust results towards highlights
the potential of foundational models in the realm of time series forecasting.

2 RELATED WORKS

Pre-trained Large Language Models for Time Series. The recent development of Large Language
Models (LLMs) has opened up new possibilities for time-series modeling. LLMs, such as T5
(Raffel et al., 2020), GPT (Radford et al., 2018), GPT-2 (Radford et al., 2019), GPT-3 (Brown et al.,
2020), GPT-4 (OpenAI, 2023), LLaMA (Touvron et al., 2023), have demonstrated a strong ability to
understand complex dependencies of heterogeneous textual data and provide reasonable generations.
Recently, there is growing interest in applying language models to time series tasks (Jin et al., 2024a;
Gruver et al., 2024). For example, Xue & Salim naively convert time series data to text sequence
inputs and achieves encouraging results. Sun et al. propose text prototype-aligned embedding to
enable LLMs to handle time series data. In addition, Yu et al. present an innovative approach towards
leveraging LLMs for explainable financial time series forecasting. The works in (Zhou et al., 2023)
and (Chang et al., 2023) are the most relevant ones to our work, as they both introduce approaches for

2

---

<!-- PAGE 3 -->

Published as a conference paper at ICLR 2024

Figure 1: The architecture of proposed TEMPO-GPT. The trend XT , seasonal XS and residual XR components
are treated as different semantic inductive biases to feed into the pre-trained transformer.

time-series analysis by strategically leveraging and fine-tuning LLMs. However, these studies directly
employ time series data to construct embeddings, without adequately capturing the inherent and
unqiue characteristics of time series data which is challenging to decouple such information within
the LLMs (Shin et al., 2020). In addition, there is still very limited work on LLM for multimodal
data with time series. METS (Li et al., 2023) is one of the early works pursuing this direction. While
the experiment results are encouraging, it is difficult to extend METS to other modalities since the
embedding alignment between time series and texts are specific. Please refer to the suvery papers
(Jin et al., 2023; 2024b) for further references of time series meeting LLMs.

Prompt tuning. Prompt tuning is an efficient, low-cost way of adapting a pre-trained foundation
model to new downstream tasks which has been adapted to downstream tasks across various domains.
In NLP domain, soft prompts with trainable representation are used through prompt-tuning (Lester
et al., 2021) or prefix-tuning (Li & Liang, 2021). Prompting techniques have also been extended to CV
tasks like object detection(Li et al., 2022) and image captioning (Zhang et al., 2022a), etc and other
domains such as misinformation (Zhang et al., 2024). Multimodal works, such as CLIP (Radford
et al., 2021), use textual prompts to perform image classification and achieve SOTA performance. In
addition, L2P (Wang et al., 2022b) demonstrates the potential of learnable prompts stored in a shared
pool to enable continual learning without rehearsal buffer, and Dualprompt (Wang et al., 2022a)
introduces a dual-space prompt architecture, maintaining separate prompt encodings for general
knowledge and expert information, etc. Our research builds upon these concepts by exploring the
use of prompt design from indicative bias specifically for temporal reasoning and knowledge sharing
across time series forecasting problems.

3 METHODOLOGY

In our work, we adopt a hybrid approach that incorporates the robustness of statistical time series
analysis with the adaptability of data-driven methods. As shown in Figure 1, we propose a novel
integration of seasonal and trend decomposition from STL (Cleveland et al., 1990) into the pre-trained
transformers. This strategy allows us to exploit the unique strengths of both statistical and machine
learning methods, enhancing our model’s capacity to handle time series data efficiently. Moreover, a
semi-soft prompting approach is introduced to enhance the adaptability of pre-trained models for
handling time series data. This innovative approach enables the models to merge their extensive
learned knowledge with the unique requirements intrinsic to time series analysis.

3.1 PROBLEM DEFINITION

Given observed values of previous K timestamps, the task of multivariate time-series forecasting
aims to predict the values for the next H timestamps. That is,
t−K, ..., xi

t+H−1 = F (xi

t−1; Vi; Φ)

t, ..., ˆxi
ˆxi

(1)

3

---

<!-- PAGE 4 -->

Published as a conference paper at ICLR 2024

t, ..., ˆxi

where ˆxi
t+H−1 is the vector of H-step estimation from timestamp t of channel i corresponding
to the i-th feature. Given the historical values xi
t−1, it can be inferred by model F with
parameter Φ and prompt Vi. In anticipation of the foundational model’s strong generalization
capabilities across unseen datasets, we default to a zero-shot learning configuration in the absence of
specific indications. This approach entails that the model is not privy to the target dataset’s history
value and horizon value during the training process.

t−K, ..., xi

3.2 TIME SERIES INPUT REPRESENTATION

For time series data, representing the complex input by decomposing it into meaningful components,
such as trend and season components, can help extract information optimally. In this paper, given
the input X ∈ Rn×L, where n is the feature (channel) size and L it the length of the time series, the
additive STL decomposition (Cleveland et al., 1990) can be represented as:

(2)

(cid:80)k

X i = X i

S + X i
R.

T + X i
Here, i is the channel index (corresponding to a certain covariate) for multivariate time series input,
and the trend XT ∈ Rn×L = 1
j=−k Xt+j captures the underlying long-term pattern in the
m
data, where m = 2k + 1 and k is the averaging step size. The seasonal component XS ∈ Rn×L
encapsulates the repeating short-term cycles, which can be estimated after removing the trend
component. The residual component XR ∈ Rn×L represents the remainder of the data after the
trend and seasonality have been extracted. Note that, in practice, it is suggested to leverage as much
information as possible to achieve a more precise decomposition. However, in consideration of
computational efficiency, we opt not to use the STL decomposition on the largest possible data
window on each instance. Instead, we perform local decomposition within each instance using a fixed
window size. Inspired by N-BEATs (Oreshkin et al., 2019), we introduce learnable parameters for
estimating the various local decomposition components. Same for the others. This principle applies
to other components of the model as well. In Appendix G, we establish a connection between time
series forecasting and frequency domain prediction, where our findings indicate that decomposition
significantly simplifies the prediction process. Note that such decomposition is of more importance
in current transformer-based methods as the attention mechanism, in theory, may not disentangle the
disorthogonal trend and season signals automatically:

Theorem 3.1 Suppose that we have time series signal X = XT t + XSt + XRt, t ∈ [t1, tn]. Let
E = {e1, e2, ..., en} denote a set of orthogonal bases. Let ES ⊆ E denote the subset of E on which
XSt has non-zero eigenvalues and ET ⊆ E denote the subset of E on which XT t has non-zero
eigenvalues. If XSt and XT t are not orthogonal, i.e. (cid:80)n
T tX i
St ̸= 0, then ET ∩ ES ̸= ∅, i.e. E
can not disentangle the two signals onto two disjoint sets of bases.

i=1 X i

The proof can be found in Appendix G. Theorem 3.1 states that if trend and seasonal components
of a time series are non-orthogonal, they cannot be fully disentangled and separated by any set
of orthogonal bases. According to (Zhou et al., 2023), the self-attention layer naturally learns an
orthogonal transformation, akin to PCA’s decomposition into orthogonal principal components. Thus,
applying attention directly to a raw time series would be ineffective at disentangling non-orthogonal
trend and seasonal components. For the remainder of the methodology section, we will utilize the
trend component XT as the exemplary case. We first apply reverse instance normalization (Kim et al.,
2022) on each global component and local input respectively to facilitate knowledge transfer and
minimize losses introduced by distribution shifts. That is, for each sample xT t from XT ’s -th channel
(cid:3) are
of time t, ˆxT t = γT
the instance-specific mean and standard deviation; γT and βT are trainable affine parameter vectors
for trend component. In addition, we implement a mean square error (MSE) reconstruction loss
function to ensure that the local decomposition aligns with the global STL decomposition observed
in the training data. The decomposition loss function, denoted as LDec = fT (X, θT ) − ˆX g
T , where
fT is the function with learnable variables θT for mapping local decomposition to be aligned with
the global decomposition after normalization ˆX g
T . Then, following (Nie et al., 2023), we combine
time-series patching with temporal encoding to extract local semantics by aggregating adjacent
time steps into tokens, significantly increasing the historical horizon while reducing redundancy.
Specifically, we get the patched token for the i-th normalized trend component for fT (X i, θT ) with

+ βT , where Et [xT t] and Var (cid:2)xi

xT t − Et [xT t]/(cid:112)Var [xT t] + ϵT

T t

(cid:17)

(cid:16)

4

---

<!-- PAGE 5 -->

Published as a conference paper at ICLR 2024

T ∈ RLP ×N , where LP is the patch length, N =
P i
+ 2 is the number of patches and S is
the stride. We get patched tokens P i
R in the same way. Then, we feed the patched time series
T ) ∈ RP ×LE for the language
tokens to the embedding layer f to get the representation P i
model architecture to transfer its language capabilities to the novel sequential modality effectively,
where LE is the embedding size.

T = f (P i

S and P i

(cid:106) (L−LP )
S

(cid:107)

3.3 PROMPT DESIGN

Prompting techniques have demonstrated remarkable effectiveness across a wide range of applications
by leveraging the power of task-specific knowledge encoded within carefully crafted prompts. This
success can be attributed to the prompts’ ability to provide a structured framework that aligns the
model’s outputs with the desired objectives, resulting in enhanced accuracy, coherence, and overall
quality of the generated content. Previous works mostly focus on utilizing a fixed prompt to boost the
pre-trained models’ performance through fine-tuning (Brown et al., 2020). In pursuit of leveraging
the rich semantic information encapsulated within various time series components, our research
introduces a semi-soft prompting strategy. This approach involves the generation of distinct prompts
corresponding to each primary time series component: trend, seasonality, and residuals. ‘Predict
the future time step given the [trend, season, residual]’ serves as the template from which we derive
our component-specific prompts. These are subsequently concatenated with the relevant component
data, thereby enabling a more refined modeling approach that acknowledges the multifaceted nature
of time series data. Specifically, commence by translating the trend-specific prompts into the word
embedding space, followed by a linear transformation to derive the learnable trend prompt vector Vt.
This so-called ‘semi-soft’ prompt design thus strikes a balance between the interpretability and initial
guidance of a ‘hard’ prompt and the adaptability of a ‘soft’ prompt. The combined embedding of this
prompt with the time series representation is encapsulated by:

xT = [Vt; PT ]

(3)

Here, xT denotes the aggregation of embeddings along the temporal axis. This concatenation
procedure is mirrored for the seasonality and residual components, yielding xS and xR, respectively.
This framework allows for an instance to be associated with specific prompts as the inductive bias,
jointly encoding critical information relevant to the forecasting task, such as recurring patterns,
overarching trends, and inherent seasonality effects. It is of note that our prompt design maintains a
high degree of adaptability, ensuring compatibility with a broad spectrum of time series analyses. In
particular, similar with (Wang et al., 2022a), we introduce prompt pool as an extension of our design
of soft prompt in Appendix D, aimed at accommodating the characteristically non-stationary nature
of real-world time series data and the associated distributional shifts (Huang et al., 2020; Fan et al.,
2023). This adaptability underscores the potential of our prompting strategy to evolve in congruence
with the complexities presented by diverse time series datasets.

3.4 GENERATIVE PRE-TRAINED TRANSFORMER ARCHITECTURE

We use the decoder-based generative pre-trained transformer (GPT) as the backbone to build the
basis for the time-series representations. To utilize the decomposed semantic information in a
data-efficient way, we choose to concatenate the prompt and different components together and put
them into the GPT block. Specifically, the input of our time series embedding can be formulated
as: x = xT ⊕ xS ⊕ xR, where ⊕ corresponds to concatenate operation and x∗ can be treated as
different sentences. Note that, another alternative way is to build separate GPT blocks to handle
different types of time series components. Inside the GPT block, we adopt the strategy used in (Zhou
et al., 2023) and opt to update the gradients of the position embedding layer and layer normalization
layers. In addition, we employ LORA (Low-Rank Adaptation) (Hu et al., 2021) to adapt to varying
time series distributions efficiently as it performs adaptation with significantly fewer parameters.

The overall forecasting result should be an additive combination of the individual component pre-
dictions. Finally, the outputs Z of n features from the GPT block can be split into ZT , ZS, ZR ∈
Rn×P ×LE (output corresponding to trend, seasonality, and residual) based on their positions in
the input order. Each Z component is then fed into fully connected layers to generate predictions
Y∗ ∈ Rn×LH , where LH is the prediction length. The forecast results can be formulated as follows:
ˆY = ˆYT + ˆYS + ˆYR. After that, we de-normalize Y according to the corresponding statistics used in

5

---

<!-- PAGE 6 -->

Published as a conference paper at ICLR 2024

(cid:3). By recombining these additive
the normalization step: ˆY i
elements, our approach aims to reconstruct the full temporal trajectory most representative of the
underlying dynamics across varied timescales captured by the decomposed input representation.

Var (cid:2)xi

(cid:3) + ϵ ·

+ Et

t =

(cid:2)xi

t

t

(cid:17)

(cid:16) Y i
t −β
γ

(cid:113)

In order to achieve interpretability, we explore both linear and nonlinear interactions among trend,
seasonal, and residual components in their contribution to the final output. Therefore we construct an
interpretable generalized additive model (GAM) (Hastie, 2017) based on GPT’s output to learn how
the three components interact with each other, which is: g(Y ) = F∅ + (cid:80)
t FIt(xIt),
where F∅ is a normalizing constant, the footnote i corresponds to the trend, season, and residual
component. {It} is of a set of multiple interact components. Then, we can calculate the first-order
sensitivity index (Sobol’, 1990) or SHAP (SHapley Additive exPlanations) value (Lundberg & Lee,
2017) to measure the sensitivity of each component.

i Fi(xi) + (cid:80)

4 EXPERIMENTS

Our experiments are conducted using widely-recognized time series benchmark datasets, such as
those detailed in (Zhou et al., 2021), alongside the GDELT dataset (Jia et al., 2024) and our proposed
TETS dataset. These comprehensive datasets encompass a diverse array of domains, including, but
not limited to, electricity (ETTh1, ETTh2, ETTm1, ETTm2, Electricity), traffic (Traffic), climate
(Weather), news (GDELT), and finance (TETS), with data sampling frequencies ranging from minutes,
hours to days and quarters. The inclusion of such varied datasets ensures a thorough evaluation
of our experimental setups across multiple dimensions of time series data. Due to the absence
of a standard test split for zero-shot comparison, we adopt a uniform training methodology to
ensure fair performance assessment across datasets unseen during model training. Specifically, to
advance the paradigm of foundation models within the domain of transfer learning, we investigate
a zero-shot setting for our experiments, which is the ‘many-to-one’ scenario: training on multiple
source datasets followed by zero-shot forecasting on a distinct, unseen target dataset. For instance,
when evaluating performance on a ‘weather’ dataset, our model is pre-trained on diverse datasets
including ‘ETTm1, ETTm2, ETTh1, ETTh2, Electricity, and Traffic’ without exposure to the target
weather data. This ’many-to-one’ approach differs fundamentally from ‘one-to-one’ or ‘one-to-many’
configurations (Zhang et al., 2022c) by using diverse pre-training datasets from varied domains, like
traffic and weather data. This diversity, while rich, introduces complexity, as the model must identify
patterns across potentially misaligned samples, complicating learning compared to models trained
and tested on in distribution datasets.

We use GPT-2 (Radford et al., 2019) as our backbone to build TEMPO1 as shown in Figure 1. To
comprehensively demonstrate the performance of our model, we compare TEMPO with the following
baselines over long-term forecasting and short-term forecasting: (1) The pre-trained LLM-based
models, including Bert (Devlin et al., 2019), GPT2 (Radford et al., 2019; Zhou et al., 2023), T5 (Raffel
et al., 2020), and LLaMA (Touvron et al., 2023). (2) The Transformer-based models, including the
PatchTST (Nie et al., 2023), FEDformer (Zhou et al., 2022), ETSformer (Woo et al., 2022) and
Informer (Zhou et al., 2021). (3) The variant of Linear-based models, DLinear (Zeng et al., 2023)
model. (4) General 2D-variation model, TimesNet (Wu et al., 2023). Following traditional forecasting
works, we report the Mean Squared Error(MSE) and Mean Absolute Error (MAE) results in this
section. Please refer to the Appendix B and F for the detailed experiment setting and baselines.

4.1 ZERO SHOT LONG-TERM FORECASTING RESULTS

Table 1 presents the performance of multiple time series forecasting models on MSE and MAE metrics
across different prediction lengths under the ‘many-to-one’ setting, with lower scores indicating more
accurate forecasts. Our proposed model, TEMPO, surpassed existing baselines on average over all
prediction horizons across all datasets, highlighting the broad applicability of TEMPO. Our model
achieves the highest average performance scores. Specifically, it improves the weather and ETTm1
datasets by around 6.5% and 19.1%, respectively in MAE compared to the previous state-of-the-art
model, PatchTST. It also secures the lowest error rates across numerous individual dataset-prediction
length configurations. Compared to other pre-trained models for forecasting, TEMPO consistently
delivers the best results across different time series datasets. These results suggest that incorporating

1TEMPO’s source code can be found at: https://github.com/DC-research/TEMPO

6

---

<!-- PAGE 7 -->

Published as a conference paper at ICLR 2024

Table 1: Transfer learning of long-term forecasting results on time series benchmark datasets. We use
prediction length O ∈ {96, 192, 336, 720}. A lower MSE indicates better performance. Hereafter,
for the tables, the best results are marked in bold and the second optimal in underlined, respectively
with MSE/MAE.

Horizon

Model

96

192

336

720

Avg

TEMPO
GPT2
T5
PatchTST
Timesnet
FEDformer
ETSformer
Informer
DLinear

TEMPO
GPT2
T5
PatchTST
Timesnet
FEDformer
ETSformer
Informer
DLinear

TEMPO
GPT2
T5
PatchTST
Timesnet
FEDformer
ETSformer
Informer
DLinear

TEMPO
GPT2
T5
PatchTST
Timesnet
FEDformer
ETSformer
Informer
DLinear

TEMPO
GPT2
T5
PatchTST
Timesnet
FEDformer
ETSformer
Informer
DLinear

ECL

Etth1

Etth2

Ettm2

Traffic

Weather

Ettm1
MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE
0.301/0.353
0.438/0.424
0.178/0.276
0.320/0.363
0.486/0.438
0.193/0.288
0.328/0.366
0.529/0.464
0.185/0.282
0.379/0.412
0.733/0.554
0.489/0.546
0.315/0.362
0.518/0.470
0.293/0.369
0.385/0.426
0.698/0.553
0.300/0.399
0.405/0.428
1.117/0.678
0.707/0.638
0.704/0.651
0.880/0.657
0.512/0.531
0.334/0.389
0.624/0.522
0.195/0.292

0.400/0.406
0.400/0.416
0.400/0.409
0.57/0.518
0.407/0.423
0.509/0.502
0.469/0.457
0.642/0.562
0.414/0.421

0.185/0.267
0.193/0.273
0.190/0.268
0.273/0.345
0.202/0.290
0.665/0.634
0.353/0.404
0.263/0.360
0.264/0.352

0.476/0.343
0.522/0.380
0.508/0.366
1.023/0.641
0.585/0.401
0.835/0.564
1.419/0.795
1.400/0.830
0.609/0.424

0.211/0.254
0.226/0.274
0.217/0.271
0.247/0.301
0.247/0.295
0.292/0.346
0.453/0.416
0.837/0.711
0.212/0.275

0.198/0.293
0.207/0.300
0.205/0.302
0.465/0.535
0.283/0.366
0.390/0.468
0.721/0.645
0.625/0.619
0.204/0.300

0.209/0.309
0.231/0.324
0.229/0.321
0.531/0.569
0.733/0.633
0.317/0.406
0.862/0.707
1.222/0.863
0.231/0.325

0.279/0.355
0.262/0.347
0.266/0.351
0.475/0.532
1.166/0.859
0.423/0.48
0.666/0.640
0.881/0.778
0.259/0.352

0.216/0.308
0.223/0.315
0.221/0.314
0.49/0.545
0.619/0.557
0.358/0.439
0.750/0.664
0.810/0.698
0.222/0.317

0.496/0.355
0.533/0.387
0.524/0.374
0.992/0.633
0.64/0.431
0.869/0.579
0.995/0.658
0.872/0.506
0.595/0.412

0.503/0.356
0.566/0.421
0.550/0.391
0.987/0.626
1.609/0.864
1.006/0.640
0.940/0.621
0.978/0.507
0.624/0.427

0.538/0.376
0.596/0.399
0.578/0.404
1.152/0.706
1.974/0.971
0.965/0.652
0.798/0.518
1.532/0.800
0.623/0.42

0.503/0.358
0.554/0.397
0.540/0.384
1.039/0.652
1.202/0.667
0.919/0.609
1.038/0.648
1.196/0.661
0.613/0.421

0.254/0.298
0.273/0.312
0.277/0.321
0.277/0.324
0.316/0.342
0.372/0.426
0.545/0.466
0.431/0.455
0.259/0.308

0.292/0.332
0.441/0.379
0.330/0.330
0.317/0.347
0.359/0.372
0.639/0.600
0.487/0.444
0.370/0.412
0.304/0.342

0.370/0.379
0.484/0.422
0.528/0.451
0.375/0.388
0.423/0.405
0.409/0.425
0.592/0.506
1.133/0.842
0.363/0.389

0.282/0.316
0.356/0.347
0.338/0.343
0.304/0.340
0.336/0.354
0.428/0.449
0.519/0.458
0.693/0.605
0.284/0.329

0.461/0.432
0.516/0.461
0.523/0.454
0.739/0.563
0.55/0.490
0.819/0.608
1.598/0.803
1.461/0.892
0.599/0.511

0.515/0.467
0.571/0.502
0.572/0.504
0.755/0.576
0.638/0.532
0.785/0.624
1.154/0.682
0.949/0.631
0.622/0.534

0.591/0.509
0.646/0.54
0.694/0.568
0.739/0.57
0.723/0.577
0.816/0.614
1.038/0.665
0.779/0.616
0.639/0.559

0.501/0.458
0.555/0.485
0.58/0.498
0.741/0.566
0.607/0.517
0.780/0.600
1.227/0.707
1.017/0.699
0.621/0.531

0.243/0.304
0.254/0.312
0.246/0.306
0.299/0.355
0.261/0.318
0.358/0.416
0.390/0.416
0.494/0.516
0.292/0.365

0.309/0.345
0.315/0.35
0.316/0.346
0.342/0.382
0.38/0.392
0.372/0.424
0.409/0.428
0.788/0.622
0.361/0.411

0.386/0.395
0.394/0.397
0.394/0.397
0.421/0.421
0.399/0.409
0.455/0.462
0.444/0.438
1.075/0.725
0.515/0.490

0.280/0.328
0.289/0.333
0.287/0.329
0.334/0.376
0.311/0.352
0.463/0.484
0.399/0.422
0.655/0.556
0.358/0.405

0.426/0.421
0.441/0.433
0.428/0.426
0.580/0.528
0.439/0.439
0.683/0.596
0.548/0.503
0.798/0.632
0.439/0.437

0.441/0.430
0.449/0.440
0.442/0.438
0.677/0.573
0.555/0.503
0.582/0.542
0.728/0.585
1.125/0.810
0.463/0.464

0.443/0.451
0.445/0.454
0.443/0.458
0.540/0.521
0.438/0.461
0.688/0.618
0.615/0.561
0.836/0.687
0.467/0.481

0.428/0.427
0.436/0.436
0.428/0.433
0.592/0.535
0.460/0.457
0.616/0.565
0.590/0.527
0.850/0.673
0.446/0.451

0.355/0.389
0.381/0.402
0.413/0.410
0.387/0.417
0.394/0.406
0.921/0.748
0.476/0.468
0.455/0.883
0.381/0.415

0.379/0.408
0.394/0.416
0.416/0.427
0.386/0.425
0.384/0.413
-/5.755
0.446/0.451
1.389/0.848
0.471/0.482

0.409/0.440
0.434/0.448
0.425/0.440
0.425/0.448
0.394/0.431
0.427/0.452
0.446/0.466
1.330/0.866
0.639/0.559

0.361/0.398
0.382/0.407
0.396/0.411
0.394/0.425
0.372/0.403
-/1.845
0.443/0.453
0.970/0.812
0.456/0.461

LLM with the well-designed prompt and implementing time series decomposition can contribute
significantly to enhancing the accuracy and stability of zero-shot time series forecasting.

4.2 SHORT-TERM FORECASTING WITH CONTEXTUAL INFORMATION

Dataset and metrics. In this section, we introduce TETS, a new benchmark dataset built upon S&P
500 dataset combining contextual information and time series, to the community. Following (Cao
et al., 2023), we choose the symmetric mean absolute percentage error (SMAPE) as our metric in
this section. Moreover, the GDELT is also used to verify the effectiveness the our proposed method.
Please refer to Appendix B.2 and Appendix B.3 for the detailed dataset setting of TETS and GDELT;

7

---

<!-- PAGE 8 -->

Published as a conference paper at ICLR 2024

Table 2: SMAPE results of EBITDA from TETS and GDELT. The result of EBITDA includes
outliers removed where SMAPE exceeds 0.8/0.9. The best results are marked in bold and the second
optimal in underlined respectively with 0.8 & 0.9. (Sectors: CC: Consumer Cyclical; CD: Consumer
Defensive; Ind: Industrials; RE: Real Estate; Events: 11: Disapprove; 17: Coerce; 19:Fight.)

EBITDA Dataset

Sectors

TEMPO

LLaMA

GPT2

Bert

T5

Informer

PatchTST

Reformer

DLinear

CC

CD

Ind

RE

11

17

19

32.27/33.48 33.13/34.31 33.77/35.37 33.42/35.33 32.65/33.83 41.12/43.17 41.44/43.18 37.23/39.09 33.53/35.65

25.9/26.25 26.34/26.62 26.86/27.15 27.34/28.3 26.44/26.79 35.65/36.08 31.6/31.98 29.93/30.36 27.01/28.04

26.7/27.42 27.17/27.98 27.9/28.63 27.89/28.95 27.3/28.12 34.83/35.87 33.84/34.87 30.23/31.28 27.59/28.84

29.46/30.11 29.63/30.48 30.62/31.21 30.62/31.66 30.1/30.64

36.4/37.22 37.63/38.31 31.23/31.69 29.95/30.92

GDELT Dataset

38.77

41.02

44.03

40.23

42.50

45.49

39.03

41.20

44.17

38.89

41.10

44.09

39.04

41.24

44.29

42.00

44.44

47.45

40.45

42.72

45.49

46.72

48.08

48.30

40.14

42.45

45.40

Appendix H for the proposed pipeline of collecting TETS dataset with both time series and textual
information.

Contextual Information. In order to incorporate the contextual information into our proposed
TEMPO, we leverage the built-in tokenization capabilities of the generative pre-trained transformer to
derive embeddings of input text. Then, we utilize these text embeddings corresponding to each time
series instance, T ext, to construct soft prompts with learnable parameters and concatenate them at the
beginning of the input embedding, that is, x = T ext ⊕ xT ⊕ xS ⊕ xR. Where the x∗ for EBITDA
is conducted with semi-soft prompt. This method is not strictly confined to our proposed model
but can be feasibly applied in similar works to enhance their capability of handling and benefiting
from contextual information. Comparisons with other design strategies of contextual information are
provided in the Appendix D.4 for further reference.

Results. From the transfer learning perspective, we choose to report the setting of ‘many-to-many’,
which means we train a model using in-domain sectors data and directly do the zero-shot test on all
cross-domain sectors. The SMAPE results of using different baseline models and our model on the
TETS dataset and GDELT dataset are listed in Table 2 which is also zero-shot setting as data samples
from those sectors are not seen during the training stage. Examining the results across all sectors, our
proposed model, which combines time series data with supplementary summary (contextual) data,
outperforms all the baseline methods in cross-domain sectors. Besides, we observe that transformer-
based architectures training from scratch, specifically tailored for time series analysis—such as
PatchTST, Informer, and Reformer (Kitaev et al., 2020)—tend to underperform in comparison to
transformers pre-trained on linguistic datasets. This performance discrepancy indicates that the
parameter initialization derived from pre-trained language models confers a superior starting point
for model optimization. Consequently, these pre-trained models exhibit enhanced capabilities and
adaptability within zero-shot learning contexts. Furthermore, in instances where the time series data
exhibits a strong correlation to other modalities, such as textual information, devising an effective
strategy to amalgamate these distinct modalities could lead to enhanced performance gains.

5 ANALYSIS

5.1 ABLATION STUDY

The provided ablation study, Table 3, offers critical insights into the impact of the prompt and
decomposition components on the performance of our model. In this table, the MSE and MAE on
various datasets are reported for four scenarios: the original model configuration (‘TEMPO’); the
model without the prompt design and without decomposition, which is the setting of ‘w/o Dec’; the
model without prompt design (‘w/o Pro’) and the model without the decomposition loss alignment
(’w/o Dec Loss’). Averagely, the exclusion of the prompt component leads to a deterioration in
the model’s predictive accuracy, indicating the prompt can be an important factor in enhancing the
model’s overall performance. The omission of decomposition loss typically results in a decline
in model performance. Decomposition loss facilitates the use of a richer historical dataset, which

8

---

<!-- PAGE 9 -->

Published as a conference paper at ICLR 2024

TEMPO

w/o Dec

w/o Pro w/o Dec Loss

MSE/MAE MSE/MAE MSE/MAE MSE/MAE

96 0.178/0.276 0.195/0.294 0.185/0.281 0.191/0.293

192 0.198/0.293 0.210/0.301 0.196/0.295 0.205/0.305

ECL

336 0.209/0.309 0.237/0.328 0.225/0.318 0.243/0.337

720 0.279/0.355 0.271/0.351 0.269/0.359 0.262/0.353

Avg 0.216/0.308 0.228/0.319 0.219/0.313 0.225/0.322

96 0.438/0.424 0.516/0.447 0.452/0.431 0.428/0.425

192 0.461/0.432 0.518/0.462

0.47/0.45

0.494/0.463

Ettm1

336 0.515/0.467 0.622/0.515 0.519/0.474 0.544/0.492

720 0.591/0.509 0.644/0.50

0.582/0.51

0.594/0.521

Avg 0.501/0.458 0.575/0.481 0.506/0.466 0.515/0.475

Table 3: Ablation study on TEMPO.

Figure 2: The SHAP values of decomposed com-
ponents of TEMPO for ETTm1.

enhances the quality of individual decomposition components. This improvement in component
quality is important for the model’s forecasting accuracy. Note that employing the prompt design
in isolation, without the support of decomposition, can detrimentally impact the backbone model’s
performance in most cases. This can be due to the difficulties in effectively prompting time series
data from its raw form with limited semantic information. These findings underscore the essential
nature of both prompt and decomposition elements in achieving robust forecasting capabilities under
the zero-shot setting.

5.2

INTERPRETING MODEL PREDICTIONS

SHAP (SHapley Additive exPlanations) values serve as a comprehensive measure of feature impor-
tance, quantifying the average contribution of each feature to the prediction output across all possible
feature combinations. As shown in Figure 2, when applied to our seasonal and trend decomposition,
the SHAP values from the generalized additive model (GAM) suggest a dominant influence of the
seasonal component on the model’s predictions, implying a significant dependency of the model
on the overall recurring patterns within the data. While the directional shifts of ETTm1 dataset’s
contribution is relatively stable. The escalating values in the ’Error’ column, which denote the
discrepancy between the model’s predictions and the ground truth, indicate a potential decline in
the model’s accuracy as the prediction length increases which is indeed observed in most experi-
ments run. In this context, the STL decomposition proves invaluable as it enables us to identify and
quantify the individual contributions of each component to the overall predictions, as demonstrated
by the SHAP values. This detailed understanding can yield critical insights in how the pre-trained
transformer is interpreting and leveraging the decomposing pre-processing step, thereby providing a
robust foundation for model optimization and enhancement. SHAP values for weather dataset can be
found at Figure 14.

6 CONCLUSION

This paper proposes a soft prompt based generative transformer, TEMPO, which achieves state-of-the-
art performance in zero-shot time series forecasting. We introduce the novel integration of prompts and
seasonal trend decomposition together within a pre-trained Transformer-based backbone to allow the
model to focus on appropriately utilizing knowledge from different temporal semantics components.
Moreover, we demonstrate the effectiveness of TEMPO with multimodel input, effectively leveraging
contextual information in time series forecasting. Lastly, with extensive experiments, we highlight
the superiority of TEMPO in accuracy, and generalizability. One potential limitation worth further
investigation is that superior LLMs with better numerical reasoning capabilities might yield better
results. In addition, the encouraging results of TEMPO on the zero-shot experiments shed light into
effective foundational models for time series.

9

---

<!-- PAGE 10 -->

Published as a conference paper at ICLR 2024

ACKNOWLEDGEMENT

This work is partially supported by the NSF Award #2125142 and NSF Award #2226087. The funding
from these sources has been a cornerstone in enabling us to bring our project to fruition. We would
like to extend our thanks to Yizhou Zhang, James Enouen, Qiang Huang, Chuizheng Meng, and Hao
Niu for their invaluable discussions and insights in shaping the direction and execution of our work.
We are also deeply grateful to the anonymous reviewers for their rigorous review process. Their
detailed comments and constructive suggestions have significantly contributed to the improvement of
this paper. The time and effort they invested in providing feedback have been invaluable and have
greatly assisted us in refining our work.

REFERENCES

Shaojie Bai, J Zico Kolter, and Vladlen Koltun. An empirical evaluation of generic convolutional and

recurrent networks for sequence modeling. arXiv preprint arXiv:1803.01271, 2018.

Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss, Gretchen Krueger, T. J. Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler,
Jeff Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray,
Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever,
and Dario Amodei. Language models are few-shot learners. Advances in neural information
processing systems, abs/2005.14165, 2020.

Defu Cao, Yujing Wang, Juanyong Duan, Ce Zhang, Xia Zhu, Conguri Huang, Yunhai Tong, Bixiong
Xu, Jing Bai, Jie Tong, et al. Spectral temporal graph neural network for multivariate time-series
forecasting. Advances in neural information processing systems, 2021.

Defu Cao, Yixiang Zheng, Parisa Hassanzadeh, Simran Lamba, Xiaomo Liu, and Yan Liu. Large
scale financial time series forecasting with multi-faceted model. In Proceedings of the Fourth ACM
International Conference on AI in Finance, pp. 472–480, 2023.

Cristian Challu, Kin G Olivares, Boris N Oreshkin, Federico Garza Ramirez, Max Mergenthaler
Canseco, and Artur Dubrawski. Nhits: Neural hierarchical interpolation for time series forecasting.
In Proceedings of the AAAI Conference on Artificial Intelligence, volume 37, pp. 6989–6997, 2023.

Ching Chang, Wen-Chih Peng, and Tien-Fu Chen. Llm4ts: Two-stage fine-tuning for time-series

forecasting with pre-trained llms. arXiv preprint arXiv:2308.08469, 2023.

Robert B Cleveland, William S Cleveland, Jean E McRae, and Irma Terpenning. Stl: A seasonal-trend

decomposition. J. Off. Stat, 6(1):3–73, 1990.

Abhimanyu Das, Weihao Kong, Andrew Leach, Rajat Sen, and Rose Yu. Long-term forecasting with

tide: Time-series dense encoder. arXiv preprint arXiv:2304.08424, 2023a.

Abhimanyu Das, Weihao Kong, Rajat Sen, and Yichen Zhou. A decoder-only foundation model for

time-series forecasting. arXiv preprint arXiv:2310.10688, 2023b.

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: pre-training of deep
bidirectional transformers for language understanding. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for Computational Linguistics: Human Language
Technologies (NAACL-HLT), Minneapolis, MN, USA, June 2-7, 2019, pp. 4171–4186, 2019.

Vijay Ekambaram, Arindam Jati, Nam Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam.
Tsmixer: Lightweight mlp-mixer model for multivariate time series forecasting. In Proceed-
ings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, KDD
’23, pp. 459–469, New York, NY, USA, 2023. Association for Computing Machinery. ISBN
9798400701030. doi: 10.1145/3580305.3599533. URL https://doi.org/10.1145/
3580305.3599533.

Wei Fan, Shun Zheng, Xiaohan Yi, Wei Cao, Yanjie Fu, Jiang Bian, and Tie-Yan Liu. DEPTS: Deep
expansion learning for periodic time series forecasting. In International Conference on Learning
Representations, 2022.

10

---

<!-- PAGE 11 -->

Published as a conference paper at ICLR 2024

Wei Fan, Pengyang Wang, Dongkun Wang, Dongjie Wang, Yuanchun Zhou, and Yanjie Fu. Dish-ts:
a general paradigm for alleviating distribution shift in time series forecasting. In Proceedings of
the AAAI Conference on Artificial Intelligence, volume 37, pp. 7522–7529, 2023.

Robert Fildes, Andrew Harvey, Mike West, and Jeff Harrison. Forecasting, structural time series
models and the kalman filter. The Journal of the Operational Research Society, 42:1031, 11 1991.
doi: 10.2307/2583225.

Azul Garza and Max Mergenthaler-Canseco. Timegpt-1. arXiv preprint arXiv:2310.03589, 2023.

Mononito Goswami, Konrad Szafer, Arjun Choudhry, Yifu Cai, Shuo Li, and Artur Dubrawski.
Moment: A family of open time-series foundation models. arXiv preprint arXiv:2402.03885,
2024.

Nate Gruver, Marc Finzi, Shikai Qiu, and Andrew G Wilson. Large language models are zero-shot

time series forecasters. Advances in Neural Information Processing Systems, 36, 2024.

Trevor J Hastie. Generalized additive models. In Statistical models in S, pp. 249–307. Routledge,

2017.

Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
and Weizhu Chen. Lora: Low-rank adaptation of large language models. arXiv preprint
arXiv:2106.09685, 2021.

Biwei Huang, Kun Zhang, Jiji Zhang, Joseph Ramsey, Ruben Sanchez-Romero, Clark Glymour, and
Bernhard Sch¨olkopf. Causal discovery from heterogeneous/nonstationary data. The Journal of
Machine Learning Research, 21(1):3482–3534, 2020.

Rob J Hyndman and Yeasmin Khandakar. Automatic time series forecasting: the forecast package

for r. Journal of statistical software, 27:1–22, 2008.

Furong Jia, Kevin Wang, Yixiang Zheng, Defu Cao, and Yan Liu. Gpt4mts: Prompt-based large
language model for multimodal time-series forecasting. In The 14th Symposium on Educational
Advances in Artificial Intelligence (EAAI-24), 2024.

Ming Jin, Qingsong Wen, Yuxuan Liang, Chaoli Zhang, Siqiao Xue, Xue Wang, James Zhang,
Yi Wang, Haifeng Chen, Xiaoli Li, et al. Large models for time series and spatio-temporal data: A
survey and outlook. arXiv preprint arXiv:2310.10196, 2023.

Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y. Zhang, Xiaoming Shi, Pin-Yu Chen,
Yuxuan Liang, Yuan-Fang Li, Shirui Pan, and Qingsong Wen. Time-LLM: Time series forecasting
by reprogramming large language models. In The Twelfth International Conference on Learning
Representations, 2024a. URL https://openreview.net/forum?id=Unb5CVPtae.

Ming Jin, Yifan Zhang, Wei Chen, Kexin Zhang, Yuxuan Liang, Bin Yang, Jindong Wang, Shirui
Pan, and Qingsong Wen. Position paper: What can large language models tell us about time series
analysis. arXiv preprint arXiv:2402.02713, 2024b.

Taesung Kim, Jinhee Kim, Yunwon Tae, Cheonbok Park, Jang-Ho Choi, and Jaegul Choo. Re-
versible instance normalization for accurate time-series forecasting against distribution shift. In
International Conference on Learning Representations, 2022.

Nikita Kitaev, Lukasz Kaiser, and Anselm Levskaya. Reformer: The efficient transformer. In 8th
International Conference on Learning Representations (ICLR), Addis Ababa, Ethiopia, April 26-30,
2020, 2020.

Brian Lester, Rami Al-Rfou, and Noah Constant. The power of scale for parameter-efficient prompt

tuning. arXiv preprint arXiv:2104.08691, 2021.

Jun Li, Che Liu, Sibo Cheng, Rossella Arcucci, and Shenda Hong. Frozen language model helps ecg

zero-shot learning, 2023.

11

---

<!-- PAGE 12 -->

Published as a conference paper at ICLR 2024

Liunian Harold Li, Pengchuan Zhang, Haotian Zhang, Jianwei Yang, Chunyuan Li, Yiwu Zhong,
Lijuan Wang, Lu Yuan, Lei Zhang, Jenq-Neng Hwang, et al. Grounded language-image pre-training.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp.
10965–10975, 2022.

Xiang Lisa Li and Percy Liang. Prefix-tuning: Optimizing continuous prompts for generation. arXiv

preprint arXiv:2101.00190, 2021.

Yaguang Li, Rose Yu, Cyrus Shahabi, and Yan Liu. Diffusion convolutional recurrent neural network:
Data-driven traffic forecasting. In International Conference on Learning Representations (ICLR
’18), 2018.

Minhao Liu, Ailing Zeng, Muxi Chen, Zhijian Xu, Qiuxia Lai, Lingna Ma, and Qiang Xu. Scinet:
Time series modeling and forecasting with sample convolution and interaction. Advances in Neural
Information Processing Systems, 35:5816–5828, 2022.

Shizhan Liu, Hang Yu, Cong Liao, Jianguo Li, Weiyao Lin, Alex X Liu, and Schahram Dust-
dar. Pyraformer: Low-complexity pyramidal attention for long-range time series modeling and
forecasting. In International conference on learning representations, 2021.

Yong Liu, Tengge Hu, Haoran Zhang, Haixu Wu, Shiyu Wang, Lintao Ma, and Mingsheng Long.
itransformer: Inverted transformers are effective for time series forecasting. arXiv preprint
arXiv:2310.06625, 2023.

Scott M Lundberg and Su-In Lee. A unified approach to interpreting model predictions. Advances in

neural information processing systems, 30, 2017.

Yuqi Nie, Nam H. Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam. A time series is worth
64 words: Long-term forecasting with transformers. In International Conference on Learning
Representations (ICLR ’23), 2023.

OpenAI. Gpt-4 technical report, 2023.

Boris N Oreshkin, Dmitri Carpov, Nicolas Chapados, and Yoshua Bengio. N-beats: Neural basis
expansion analysis for interpretable time series forecasting. arXiv preprint arXiv:1905.10437,
2019.

Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton,
Luke E. Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Francis Christiano, Jan
Leike, and Ryan J. Lowe. Training language models to follow instructions with human feedback.
ArXiv, abs/2203.02155, 2022. URL https://api.semanticscholar.org/CorpusID:
246426909.

Antony Papadimitriou, Urjitkumar Patel, Lisa Kim, Grace Bang, Azadeh Nematzadeh, and Xiaomo
Liu. A multi-faceted approach to large scale financial forecasting. In Proceedings of the First ACM
International Conference on AI in Finance, pp. 1–8, 2020.

Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al.

Improving language

understanding by generative pre-training. 2018.

Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language

models are unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.

Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal,
Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual
models from natural language supervision. In International Conference on Machine Learning, pp.
8748–8763. PMLR, 2021.

Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text
transformer. The Journal of Machine Learning Research, 21(1):5485–5551, 2020.

12

---

<!-- PAGE 13 -->

Published as a conference paper at ICLR 2024

Kashif Rasul, Arjun Ashok, Andrew Robert Williams, Arian Khorasani, George Adamopoulos,
Rishika Bhagwatkar, Marin Biloˇs, Hena Ghonia, Nadhir Vincent Hassen, Anderson Schnei-
der, et al. Lag-llama: Towards foundation models for time series forecasting. arXiv preprint
arXiv:2310.08278, 2023.

Taylor Shin, Yasaman Razeghi, Robert L Logan IV, Eric Wallace, and Sameer Singh. Autoprompt:
Eliciting knowledge from language models with automatically generated prompts. In Proceedings
of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp.
4222–4235, 2020.

Sima Siami-Namini, Neda Tavakoli, and Akbar Siami Namin. A comparison of arima and lstm in
forecasting time series. In 2018 17th IEEE international conference on machine learning and
applications (ICMLA), pp. 1394–1401. IEEE, 2018.

Il’ya Meerovich Sobol’. On sensitivity estimation for nonlinear mathematical models. Matematich-

eskoe modelirovanie, 2(1):112–118, 1990.

Chenxi Sun, Yaliang Li, Hongyan Li, and Shenda Hong. Test: Text prototype aligned embedding to

activate llm’s ability for time series. arXiv preprint arXiv:2308.08241, 2023.

Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timoth´ee
Lacroix, Baptiste Rozi`ere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand
Joulin, Edouard Grave, and Guillaume Lample. Llama: Open and efficient foundation language
models. ArXiv, abs/2302.13971, 2023. URL https://api.semanticscholar.org/
CorpusID:257219404.

Zifeng Wang, Zizhao Zhang, Sayna Ebrahimi, Ruoxi Sun, Han Zhang, Chen-Yu Lee, Xiaoqi Ren,
Guolong Su, Vincent Perot, Jennifer Dy, et al. Dualprompt: Complementary prompting for
rehearsal-free continual learning. In European Conference on Computer Vision, pp. 631–648.
Springer, 2022a.

Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang, Ruoxi Sun, Xiaoqi Ren, Guolong Su, Vincent
Perot, Jennifer Dy, and Tomas Pfister. Learning to prompt for continual learning. In Proceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 139–149, 2022b.

Gerald Woo, Chenghao Liu, Doyen Sahoo, Akshat Kumar, and Steven Hoi. Etsformer: Exponential
smoothing transformers for time-series forecasting. arXiv preprint arXiv:2202.01381, 2022.

Gerald Woo, Chenghao Liu, Akshat Kumar, Caiming Xiong, Silvio Savarese, and Doyen Sahoo.
Unified training of universal time series forecasting transformers. arXiv preprint arXiv:2402.02592,
2024.

Haixu Wu, Jiehui Xu, Jianmin Wang, and Mingsheng Long. Autoformer: Decomposition transform-
ers with auto-correlation for long-term series forecasting. In Advances in Neural Information
Processing Systems (NeurIPS), pp. 101–112, 2021.

Haixu Wu, Tengge Hu, Yong Liu, Hang Zhou, Jianmin Wang, and Mingsheng Long. Timesnet:
Temporal 2d-variation modeling for general time series analysis. In The Eleventh International
Conference on Learning Representations, 2023. URL https://openreview.net/forum?
id=ju_Uqw384Oq.

Hao Xue and Flora D Salim. Promptcast: A new prompt-based learning paradigm for time series

forecasting. IEEE Transactions on Knowledge and Data Engineering, 2023.

Xinli Yu, Zheng Chen, Yuan Ling, Shujing Dong, Zongyi Liu, and Yanbin Lu. Temporal data meets

llm–explainable financial time series forecasting. arXiv preprint arXiv:2306.11025, 2023.

Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu. Are transformers effective for time series

forecasting? In Proceedings of the AAAI Conference on Artificial Intelligence, 2023.

Haotian Zhang, Pengchuan Zhang, Xiaowei Hu, Yen-Chun Chen, Liunian Li, Xiyang Dai, Lijuan
Wang, Lu Yuan, Jenq-Neng Hwang, and Jianfeng Gao. Glipv2: Unifying localization and vision-
language understanding. Advances in Neural Information Processing Systems, 35:36067–36080,
2022a.

13

---

<!-- PAGE 14 -->

Published as a conference paper at ICLR 2024

Tianping Zhang, Yizhuo Zhang, Wei Cao, Jiang Bian, Xiaohan Yi, Shun Zheng, and Jian Li. Less is
more: Fast multivariate time series forecasting with light sampling-oriented mlp structures. arXiv
preprint arXiv:2207.01186, 2022b.

Xiang Zhang, Ziyuan Zhao, Theodoros Tsiligkaridis, and Marinka Zitnik. Self-supervised contrastive
pre-training for time series via time-frequency consistency. Advances in Neural Information
Processing Systems, 35:3988–4003, 2022c.

Yizhou Zhang, Lun Du, Defu Cao, Qiang Fu, and Yan Liu. Guiding large language models with
divide-and-conquer program for discerning problem solving. arXiv preprint arXiv:2402.05359,
2024.

Yunhao Zhang and Junchi Yan. Crossformer: Transformer utilizing cross-dimension dependency
for multivariate time series forecasting. In The Eleventh International Conference on Learning
Representations, 2022.

Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, and Wancai Zhang.
Informer: Beyond efficient transformer for long sequence time-series forecasting. In Proceedings
of AAAI, 2021.

Tian Zhou, Ziqing Ma, Qingsong Wen, Xue Wang, Liang Sun, and Rong Jin. FEDformer: Frequency
enhanced decomposed transformer for long-term series forecasting. In Proc. 39th International
Conference on Machine Learning (ICML 2022), 2022.

Tian Zhou, Peisong Niu, Xue Wang, Liang Sun, and Rong Jin. One fits all: Power general time series

analysis by pretrained lm. Advances in neural information processing systems, 2023.

14

---

<!-- PAGE 15 -->

Published as a conference paper at ICLR 2024

A SHOWCASES

A.1 COMPARE WITH GPT4TS

In Figure 3, 4, 5, 6, 7, we plot the comparison of the predicted value from our model and GPT4TS
model given a look-back window. As shown in the datasets, we are able to predict close to the ground
truth, which is also shown through our superior performance over other models in table 1. We select
time series with different characteristics under different prediction lengths O ∈ {96, 192}: time
series with high variability (Figure 5 a), periodic (Figure 3 a, Figure 3 b, 4 a, 4 b), non-periodic with
a change in trend (Figure 6 a, Figure 6 b)

(a) prediction length O = 96

(b) prediction length O = 192

Figure 3: Visualization of long-term forecasting results. Compared between our model TEMPO and
GPT4TS on ETTh1 dataset

(a) prediction length O = 96

(b) prediction length O = 192

Figure 4: Visualization of long-term forecasting results. Compared between our model TEMPO and
GPT4TS on ETTh2 dataset

A.2 COMPARE WITH TIMEGPT

We also compare our results with TimeGPT (Garza & Mergenthaler-Canseco, 2023), which is
capable of generating accurate predictions for a diverse range of datasets not seen during training,
demonstrating superior performance in zero-shot inference compared to traditional statistical, machine
learning, and deep learning methods. Access to TimeGPT-1 (Beta) is provided through a Python
SDK and a REST API. This accessibility allows us to explore TimeGPT’s forecasting capabilities on
our datasets. As shown in Figure 8 and Figure 9, despite its design for various downstream tasks, it

15

---

<!-- PAGE 16 -->

Published as a conference paper at ICLR 2024

(a) prediction length O = 96

(b) prediction length O = 192

Figure 5: Visualization of long-term forecasting results. Compared between our model TEMPO and
GPT4TS on ETTm1 dataset

(a) prediction length O = 96

(b) prediction length O = 192

Figure 6: Visualization of long-term forecasting results. Compared between our model TEMPO and
GPT4TS on ETTm2 dataset

(a) prediction length O = 96

(b) prediction length O = 192

Figure 7: Visualization of long-term forecasting results on weather dataset. Compared between our
model TEMPO and GPT4TS on weather dataset

16

---

<!-- PAGE 17 -->

Published as a conference paper at ICLR 2024

(a) prediction length O = 96

(b) prediction length O = 192

Figure 8: Visualization of long-term forecasting results on ETTm1 dataset. Compared between our
model TEMPO and TimeGPT on weather dataset

(a) prediction length O = 96

(b) prediction length O = 192

Figure 9: Visualization of long-term forecasting results on ETTm2 dataset. Compared between our
model TEMPO and TimeGPT on weather dataset

is important to note that TimeGPT may not perform as well in long-term forecasting scenarios. In
contrast, our proposed model excels in zero-shot settings, including long-term forecasting, illustrating
the need for foundation models that can adapt to both the breadth of time series applications and the
depth of forecasting horizons.

B EXPERIMENT SETTING

B.1 TOWARDS FOUNDATION MODEL EXPERIMENTS DETAILS

Dataset

Sampling Period

Length Covariates

ETTh
ETTm
Weather
Electricity
Traffic

Table 4: Dataset details of benchmark dataset.

It has been well-established that
channel-independence works well for
time series datasets, so we treat each
multivariate time series as multiple in-
dependent univariate time series. We
use popular time series benchmark
datasets (Zhou et al., 2021): ETTm1,
ETTm2, ETTh1, ETTh2, Weather,
Electricity, Traffic, ILI and exchnge.
1) ETTm1, ETTm2, ETTh1, ETTh2
contain electricity load from two elec-
tricity stations at 15 minutes level and
hourly level. 2) Weather dataset contains 21 meteorological indicators of Germany within 1 year; 3)
Electricity dataset contains electricity consumption; 4) Traffic dataset contains the occupation rate
of the freeway system across the State of California. The lookback window L is following (Zhou
et al., 2023), and the prediction length O is set to {96, 192, 336, 720}. In this experiment part, our
experiments were conducted using single NVIDIA A100 GPU, with a batch size set to 256, and
focused on long-term forecasting by employing a Mean Squared Error (MSE) loss function. To

1 hour
15 min
10 min
1 hour
1 hour

17420
69680
52696
26304
17544

7
7
22
321
862

17

---

<!-- PAGE 18 -->

Published as a conference paper at ICLR 2024

ensure the reliability of our results, we performed three iterative loops and calculated the average of
the outcomes. Our exploration covered [3, 6] GPT layers and tested various weights, [0.001, 0.01,
and 1], for the MSE loss function applied to the reconstructed components of the time series. We
have documented the optimal results obtained from this search. A comprehensive analysis of the
impact that the number of GPT layers has on the performance will be addressed in future research.

Towards Foundation Model’s Zero Shot Setting For each prediction length, we train a model on
a mixture of training data from different domains and test the model on the target unseen domain’s
data. We construct the combined training dataset by pooling the training data and fullyshufflinge
them. To prevent undue bias and ensure fair representation of data from each domain in the combined
training data, we select an equal number of training examples from each domain’s training data.
We noted that the number of training samples that ETTh1 and ETTh2 has is on a much smaller
magnitude compared to the other three training datasets (ETTm1, Weather, Electricity), so selecting
the minimum number of training samples among all other training datasets would result in too much
data loss from ETTm1, Weather, and Electricity, etc. Therefore, we included all training examples
from ETTh1 and ETTh2 in the combined training dataset. Similar to traditional experimental settings,
each time series (ETTh1, ETTh2, ETTm1, Weather, Electricity, ETTm2, Traffic) is split into three
parts: training data, validation data, and test data following in 7:1:2 ratio in (Zhou et al., 2022), and
we only merge the training and validation data. For ETTm1, ETTm2, Weather and Electricity data,
the number of examples sampled to be pooled into the combined training dataset is chosen to be the
minimum number of training examples among these training datasets.

B.2 PROPOSED TETS DATASET SETTING

Figure 10: Example for designing prompts using OPENAI ChatGPT-3.5 API.

Data Collection Our time series data for financial analysis and forecasting are derived primarily
from the financial statements of companies including balance sheets, income statements, and cash
flow statements. Specifically, we utilize data from the 500 largest U.S. companies across 11 sectors as
listed in the Standard & Poor’s 500 Index (S&P 500), which we divide into two parts: the first seven
sectors for training and evaluation, and the remaining four for zero-shot forecasting tasks to test the
model’s ability to predict in unseen domains. While collecting corresponding contextual information
from the abundance of digital news sources is challenging, OpenAI’s ChatGPT API offers a solution
to gather and condense relevant news efficiently. By inputting key details into the API and limiting
the response to 110 tokens, as shown in Figure 10, we can swiftly extract pertinent contextual data to
improve our analysis. Please refer to Section H for further details of creating TETS dataset.

Prediction objective The primary objective of our experiment is to forecast the Earnings Before
Interest, Taxes, Depreciation and Amortization(EBITDA) for companies listed in S&P500, and
our data range from 2000 to 2022. Following the multivariate time series framework presented in
(Papadimitriou et al., 2020), we select foundational financial metrics from the income statements as
input features: cost of goods sold (COGS), selling, general and administrative expenses (SG&A), RD
expenses (RD EXP), EBITDA, and Revenue. Comparing with other metrics, the selected metrics
contain information more relevant to our prediction objective. For Large Language based models,

18

---

<!-- PAGE 19 -->

Published as a conference paper at ICLR 2024

including our model TEMPO, GPT4TS, and T5, we apply channel-independence strategy to perform
univariate time series forecasting tasks. All five features are used for training (predicting its future
value based on its past value), while only EBITDA is accessible during the training stage. Other
models follow the multivariate time series forecasting setting, treating the five features as multivariate
input and predicting the target, EBITDA, both in the training and testing stages.

We predict quarterly EBITDA based on the past 20 quarters’ data. This predicted value is then used
to forecast the next quarter’s EBITDA, iteratively four times, leading to a yearly prediction. In order
to measure the accuracy of these predictions based on the cumulative yearly value (sum of 4 quarters),
we employ the symmetric mean absolute percentage error (SMAPE) as the evaluation metric as well
as the forecasting loss function in this experimental part.

Data Split For companies under each sector, we employ the windowing method to generate
cohesive training and testing instances. Under the channel-independence setting where we separate
each feature to obtain univariate time series, we get 80,600 samples from the seven in-domain sectors,
and 9,199 samples from the four zero-shot sectors(also known as cross-domain sectors), five as
much as we get in the channel dependent setting. The sectors splitting is elaborated in H. In our
experiments shown in table 2, We use 70% of in-domain data for training, 10% of in-domain data for
evaluation, and all zero-shot data for unseen testing.

Symmetric Mean Absolute Percentage Error
In reality, the magnitude of financial metrics can
vary significantly among different companies. So, we choose the symmetric mean absolute percentage
error (SMAPE), a percentage-based accuracy measure, as our evaluation metric. For EBITDA, there
are many negative results that may influence the final SMAPE. We use the form of SMAPE-Abs
SMAPE:

AbsSMAPE =

200%
n

n
(cid:88)

t=1

|Ft − At|
|Ft| + |At|

,

(4)

Here, Ft represents the true value, At represents the predicted value in our system, and n represents
the total time steps we need to forecast.

SMAPE can be particularly sensitive to outliers. Specifically, when the true data and prediction have
opposite signs, the resulting error may be up to 200%, seriously distorting the final results. Following
the approach in (Papadimitriou et al., 2020), we filter out data points at the 80% and 90% thresholds
and find most of the outliers are related to significant financial shifts due to mergers & acquisitions
(M&A).

B.3 GDELT DATASET SETTING

We utilized the GDELT dataset
(Jia et al., 2024), which focuses on predicting the respective
mentions and mentions in the news media. We utilized the data collected from the 55 regions
under the US and the national data for the US and divided the 10 event root types in the dataset
into unseen and seen sets, as demonstrated in Table 5. We focused on predicting the three key
variables NumMentions, NumArticles, NumSources related to the particular event type within a given
timeframe and geographical region. We apply channel-independence strategy to perform univariate
time series forecasting tsks for all baseline models and our model. All three features are used for
training and evaluation (predicting its future value based on its past value).

We predict the future 7 days based on the past 15 days’ data directly. In other to measure the accuracy
of the predicitions, we use mean square error (MSE) and mean absolute error (MAE). For each
region, we employ the windowing method to generate cohesive training and testing instances for
each event root type. Under our channel-independence setting, we get 122,008 samples from the
seven in-domain sectors (seen sectors) for training, and 76,048 samples for evaluating under the three
zero-shot sectors (unseen sectors). In our experiments, we use 70% of in-domain data for training,
10% for evaluation and all zero-shot data for unseen testing.

19

---

<!-- PAGE 20 -->

Published as a conference paper at ICLR 2024

Event Number

Event Type Name

01
02
03
04
05
07
08
11
17
19

Make Public Statement
Appeal
Express Intent to Cooperate
Consult
Engage in Diplomatic Cooperation
Provide Aid
Yield
Disapprove
Coerce
Fight

Training Event

Test Event

Table 5: Event number to event type Name table

C FURTHER RESULTS

C.1 SELF-SUPERVISED REPRESENTATION LEARNING

Our proposed model architecture can be designed to support self-supervised learning and thus further
embrace foundation models for time series. Following (Nie et al., 2023), we mask a random subset
of patches by replacing them with zeros, where the patches are divided into non-overlapping patches
for simplicity and to avoid masked patches influencing predictions. The prediction head is removed
and replaced with a linear layer to reconstruct the masked patches. The model is trained to minimize
the MSE between the predicted and true masked patches. To handle multivariate time series with
varying numbers of features, we apply channel independence (Zeng et al., 2023) to model each time
series independently.

With the strong performance TEMPO showed under the experiment ’many-to-one’ zero-shot setting,
from the perspective of a self-supervised cross-domain foundational model, we further investigate if
using a TEMPO model trained on datasets across domains can still achieve comparable performance
on unseen domains. Here, we still use the ’many-to-one’ setting but the model is trained in a self-
supervised manner. Specifically, we first use all other domain’s data to train a representation model
then only use 5% data of the training data to fine turn the total model with the prediction layer as a
forecasting downstream task. Table 6 provides a comprehensive comparison of our model against
other baseline models on three multivariate time series datasets that are unseen by the models during
training, namely electricity and traffic and weather. All these selected 3 datasets are entirely dissimilar
to any data the model has encountered before. TEMPO outperforms baseline models, achieving the
lowest MSE and MAE in most cases. Note that TEMPO’s average MSE and MAE is 7.3% and
4.6% less than the best-performing baseline model (GPT2) for the weather dataset, respectively. This
finding shed light on the strong generalizability of TEMPO and indicated its potential of serving as a
foundational time series forecasting model, maintaining robust performance for unseen domains.

C.2 COMPARING WITH FULL-SHOT STATE-OF-THE-ARTS BASELINES

Towards foundation model training differs significantly from the one-to-one/many scenarios, where
pre-training involves a homogenous dataset, often with consistent season patterns, sampling rates,
and temporal scales. This homogeneity facilitates pattern learning transferable to fine-tuned datasets.
In contrast, towards foundation model training involves pre-training on highly diverse datasets, such
as merging traffic and weather data, which may hinder the model’s ability to discern underlying
patterns. In Table 7, we provide further results on ETTh1 and ETTh2 datasets, demonstrating that
the performance of TEMPO (zero-shot setting) surpasses that of state-of-the-art models specifically
designed for these target datasets with full-shot settings. The results in Table 7 are obtained from
(Liu et al., 2023), including but not limited to iTransformer(Liu et al., 2023), Crossformer (Zhang &
Yan, 2022), TiDE (Das et al., 2023a) and SCINet (Liu et al., 2022), which are also reported in our
contemporaneous work, MOIRAI (Woo et al., 2024).

20

---

<!-- PAGE 21 -->

Published as a conference paper at ICLR 2024

Table 6: Self-supervised representation learning results are fine-tuned on 5% in-domain datasets. We
use prediction length O ∈ {96, 192, 336, 720}. A lower MSE indicates better performance, and the
best results are in bold.

TEMPO

GPT4TS

T54TS

Bert4TS

PatchTST

MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE

96

0.19/0.29

0.202/0.301 0.199/0.293 0.202/0.298 0.21/0.308

192 0.211/0.31 0.217/0.313 0.238/0.337 0.227/0.321 0.223/0.312

ECL

336 0.229/0.323 0.258/0.353 0.273/0.364 0.256/0.345 0.282/0.357

720 0.375/0.444 0.43/0.475

0.455/0.49 0.442/0.479 0.606/0.561

Avg 0.251/0.342 0.277/0.361 0.291/0.371 0.282/0.361 0.33/0.385

96

0.56/0.411 0.607/0.417 0.543/0.408 0.591/0.423 0.577/0.403

192 0.575/0.419 0.603/0.421 0.594/0.431 0.613/0.432 0.596/0.411

Traffic

336 0.597/0.433 0.63/0.435 0.659/0.458 0.639/0.445 0.665/0.454

720 0.65/0.452 0.643/0.439

0.69/0.49

0.744/0.496 0.802/0.501

Avg 0.595/0.429 0.621/0.428 0.622/0.447 0.647/0.449 0.66/0.442

96 0.217/0.268 0.288/0.31 0.252/0.288 0.237/0.288 0.249/0.285

192 0.265/0.302 0.305/0.331 0.322/0.336 0.291/0.323 0.277/0.314

Weather

336 0.322/0.342 0.338/0.353 0.346/0.358 0.335/0.354 0.311/0.341

720 0.41/0.397 0.381/0.377 0.444/0.42 0.466/0.436 0.385/0.386

Avg 0.304/0.327 0.328/0.343 0.341/0.351 0.332/0.35 0.305/0.331

Table 7: Results of long term forecasting experiments on ETTh1 and ETTh2. The best results are
marked in bold and the second optimal in underlined, respectively with MSE/MAE. Note that the
TEMPO is under zero-shot setting and other models are under full-shot setting.

TEMPO

iTransformer

TimesNet

PatchTST

Crossformer

TiDE

DLinear

SCINet

FEDformer

MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE

96

192

336

720

0.400/0.406

0.386/0.405

0.384/0.402 0.414/0.419

0.423/0.448

0.479/0.464

0.386/0.400 0.654/0.599

0.376/0.419

0.426/0.421

0.441/0.436

0.436/0.429

0.460/0.445

0.471/0.474

0.525/0.492

0.437/0.432

0.719/0.631 0.420/0.448

0.441/0.430

0.487/0.458

0.491/0.469

0.501/0.466

0.570/0.546

0.565/0.515

0.481/0.459

0.778/0.659

0.459/0.465

0.443/0.451

0.503/0.491

0.521/0.500

0.500/0.488

0.653/0.621

0.594/0.558

0.519/0.516

0.836/0.699

0.506/0.507

Avg.

0.428/0.427

0.454/0.447

0.458/0.450

0.469/0.454

0.529/0.522

0.541/0.507

0.456/0.452

0.747/0.647

0.440/0.460

96

192

336

720

0.301/0.351

0.297/0.349

0.340/0.374

0.302/0.348

0.745/0.584

0.400/0.440

0.333/0.387

0.707/0.621

0.358/0.397

0.355/0.389

0.380/0.400

0.402/0.414

0.388/0.400

0.877/0.656

0.528/0.509

0.477/0.476

0.860/0.689

0.429/0.439

0.379/0.408

0.428/0.432

0.452/0.541

0.426/0.433

1.043/0.731

0.643/0.571

0.594/0.541

1.000/0.744

0.496/0.487

0.409/0.440

0.427/0.445

0.462/0.657

0.431/0.446

1.104/0.763

0.874/0.679

0.831/0.657

1.249/0.838

0.463/0.474

Avg.

0.361/0.398

0.383/0.407

0.414/0.427

0.387/0.407

0.942/0.684

0.611/0.550

0.559/0.515

0.954/0.723

0.437/0.449

1
h
T
T
E

2
h
T
T
E

21

---

<!-- PAGE 22 -->

Published as a conference paper at ICLR 2024

Table 8: Compare the results with ARIMA.

ECL

Traffic

Weather

Ettm2

TEMPO

ARIMA

TEMPO

ARIMA

TEMPO

ARIMA

TEMPO

ARIMA

MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE

96

0.178/0.276

1.220/0.814

0.476/0.343

1.997/0.924

0.211/0.254

0.217/0.258

0.185/0.267

0.225/0.301

192

336

720

0.198/0.293

1.264/0.842

0.496/0.355

2.044/0.944

0.254/0.298

0.263/0.299

0.243/0.304

0.298/0.345

0.209/0.309

1.311/0.866

0.503/0.356

2.096/0.960

0.292/0.332

0.330/0.347

0.309/0.345

0.370/0.386

0.279/0.355

1.364/0.891

0.538/0.376

2.138/0.971

0.393/0.387

0.425/0.405

0.386/0.395

0.478/0.445

Avg. 0.216/0.308

1.290/0.853

0.503/0.357

2.069/0.950

0.287/0.318

0.309/0.327

0.280/0.328

0.343/0.369

C.3 COMPARING WITH ARIMA

As a pioneering foundation model, TEMPO is engineered to forecast future values directly, eliminating
the necessity for retraining with each new data instance. Its underlying framework captures intricate
temporal patterns, granting it the versatility to generalize across various time series. In this study, we
compare TEMPO’s forecasting prowess with that of the ARIMA model (Hyndman & Khandakar,
2008), which is renowned for its capacity to make accurate predictions within a specific time
series once the initial model parameters have been set. While ARIMA models excel in continuing
predictions within the series they are configured for, they do not inherently possess the faculty to
forecast across disparate time series without recalibration. We obtain the ARIMA’s forecasting results
from (Challu et al., 2023). As shown in Table 8, the results highlight the superior adaptability of
our ‘towards foundation model’ – TEMPO – which retains its predictive accuracy even when applied
to time series beyond its training scope, thereby illustrating the feasibility of more universal and
resilient forecasting methodologies.

D FURTHER ANALYSIS

D.1 DESIGN OF PROMPT POOL

In this section, we propose another potential prompt design for addressing non-stationary nature of
real-world time series data with distributional shifts (Huang et al., 2020). Specifically, we introduce
a shared pool of prompts stored as distinct key-value pairs. Ideally, we want the model to leverage
related past experiences, where similar input time series tend to retrieve the same group of prompts
from the pool (Wang et al., 2022b). This would allow the model to selectively recall the most
representative prompts at the level of individual time series instance input. In addition, this approach
can enhance the modeling efficiency and predictive performance, as the model would be better
equipped to recognize and apply learned patterns across diverse datasets via a shared representation
pool. Prompts in the pool could encode temporal dependencies, trends, or seasonality effects relevant
to different time periods. Specifically, the pool of prompt key-value pairs is defined as:

VK = {(k1, V1) , (k2, V2) , · · · , (kM , VM )} ,
(5)
where M is length of prompt pool, Vm ∈ RLp×LE is a single prompt with token length Lp
m=1 with the shape of RLE .
and the same embedding size LE as P i
The score-matching process can be formulated with the score-matching function γ (cid:0)P i
(cid:1) =
T ∥∥km∥, where γ : RLE × RLE → R. The model is trained in an end-to-end way to
P i
optimize predictions with the prompts. The query P i
T that is used to retrieve the top-K corresponding
value comes from the patched time series input. Therefore, similar time series can be assigned to
similar prompts. Denoting {sj}K
j=1 as a subset of K indices for the selected top-K prompts, our input
embedding of trend is as follows:

T and km ∈ K = {km}M

T · km/∥P i

T , km

xT = [Vs1 ; · · · ; VsK ; PT ] ,

(6)
where we concatenate all the tokens along the temporal length dimension, so as xS, xR. Each
instance can be assigned to multiple prompts, which can jointly encode knowledge pertinent to
the forecasting task- such as periodic patterns exhibited by the time series, prevailing trends, or
seasonality effects.

1 ≤ K ≤ M,

22

---

<!-- PAGE 23 -->

Published as a conference paper at ICLR 2024

Table 9: Compare the different prompt designs on the ETTm2 dataset.

Semi-soft
mse/mae
0.182/0.263
0.243/0.304
0.309/0.344
0.384/0.392
0.280/0.326

Soft
mse/mae
0.189/0.271
0.252/0.307
0.306/0.348
0.386/0.394
0.283/0.330

Hard
mse/mae
0.182/0.267
0.243/0.302
0.299/0.340
0.380/0.392
0.276/0.325

Pool
mse/mae
0.185/0.267
0.242/0.304
0.289/0.336
0.373/0.386
0.273/0.323

Pool mask all
mse/mae
0.1952/0.274
0.2739/0.324
0.3131/0.354
0.3794/0.390
0.290/0.335

96
192
336
720
Avg.

D.2 RESULTS ON DIFFERENT PROMPT DESIGN

In this section, we examine the impact of various prompt designs on model performance. We utilize
the ‘semi-soft’ prompt as outlined in Section 3.3, where the prompt vectors are initialized semi-softly;
the soft prompt, which entails the random initialization of vectors of identical dimensions to the
‘semi-soft’ prompt; and the hard prompt, which is semantically meaningful and remains fixed post-
tokenization. Additionally, we explore the prompt pool, as described in Section D.1, and employ a
similar leave-one-out approach to mask all prompts within the pool to investigate its effectiveness.

The findings, presented in Table 9, reveal that, in the ETTm2 dataset, the prompt pool outperforms
the ‘semi-soft’ prompt in three out of four scenarios, underscoring the potential of prompts to enhance
model capacity and adaptability to shifts in data distribution. Furthermore, we observe that prompts
with explicit semantic content (Semi-soft and Hard) surpass the performance of simple soft prompts.
This suggests that incorporating semantic information as discrete indicators within a pre-trained
model can more effectively orchestrate domain knowledge. This understanding informs the design of
prompts for efficient interaction with language models, especially in applications where precision
and relevance of the output are crucial.

D.3 ANALYSIS ON PROMPT POOL

Here is a summary of how the prompts are initialized and trained in our work:

• Initialization: The prompt embeddings in the pool are randomly initialized from a normal

distribution, as is standard practice for trainable parameters in neural networks.

• Training: The prompts’ value and all other model parameters are trained in an end-to-end
manner to optimize the forecasting objective. This allows the prompts to be continuously
updated to encode relevant temporal knowledge.

The number of prompts and embedding dimensions are treated as hyperparameters and tuned for
good performance. Different pool settings, including pool size, top k number, and prompt length,
will lead to different results. To explore this, we conduct a total of 27 experiments, setting 3 distinct
values for each of the 3 settings: (1) pool size of 10, 20, and 30. (2) top k numbers of 1, 2, and 3. (3)
prompt lengths of 1, 2, and 3. We choose the combination with the best results for TEMPO settings.
For the long-term and short-term forecasting experiments, we choose a pool size with M = 30 and
K=3 and prompt length is 3. Detailed design analysis provides insights into prompt similarity and
selection. Note that, the prompt pool’s key in (Wang et al., 2022b) is trainable which allows us to
maintain consistent and distinct characteristics of time series data for analysis. Our work offers an
initial exploration into prompt-based tuning for time series forecasting, but substantial room remains
for advancing prompt pool design.

D.3.1 PROMPT SELECTION DISTRIBUTION

To elucidate the mechanics behind prompt selection, we have visualized the distribution histograms
for chosen prompts corresponding to the trend, seasonal, and residual elements of the ETTm2
dataset in Figure 11. In our experimental framework, each data point is permitted to select multiple
prompts—with three prompts being chosen per component. Consequently, the frequency is deter-
mined by the number of times a particular prompt is selected across the dataset. The histograms
reveal pronounced discrepancies in prompt preferences between periodic and seasonal components.

23

---

<!-- PAGE 24 -->

Published as a conference paper at ICLR 2024

Figure 11: Prompt Distribution for prompt pool selection.

For instance, within the ETTm2 dataset, prompts 11, 20, and 24 are predominantly selected for
capturing trends, whereas prompts 8, 10, and 29 are primarily chosen for seasonal fluctuations. This
observation substantiates the premise that the prompt pool is adept at furnishing specialized prompts
tailored to discrete characteristics of time series data.

D.4 ANALYSIS ON DESIGNS OF INJECTING CONTEXTUAL INFORMATION

Table 10: SMAPE results of GEBDIT dataset with different textual information injection.

Event Sum + TP SumP + TP Sum ⊕ TP SumP ⊕ TP Sum + Semi SumP + Semi Sum ⊕ Semi SumP ⊕ Semi

E 11
P
A
M
S

17

19

38.77

41.02

44.03

38.77

41.03

44.02

38.75

40.95

44.06

38.90

41.05

44.10

38.91

41.24

44.41

38.82

41.08

44.19

39.04

41.38

44.73

38.79

41.08

44.24

In this section, we investigate the influence of various configurations of textual injection and original
prompt design from multi-modality perspective. As depicted in Table 10, eight distinct prompt
designs were formulated. ’Sum’ denotes the utilization of a direct summary of textual data as a
prompt, while ’SumP’ signifies the use of textual information as a query within the prompt pool. The
symbols ’+’ and ’⊕’ represent summation and concatenation operations, respectively. ’TP’ stands
for ’time series prompt pool,’ and ’Semi’ indicates a ’semi-soft prompt’ where we manually design
the prompt, with trainable parameters, referred to as ”Predict the future time step given the {time
series data type}” for 3 different time series (Trend, Season, Residual) after decomposition. Each
design choice exerts a distinct impact on the performance metrics. The direct incorporation of textual
information along with the prompt pool yields the most optimal and near-optimal outcomes. In future
work, we aim to delve deeper into the analysis of multimodal solution design strategies for time series
forecasting.

D.5 HIDDEN REPRESENTATION

Figure 12 demonstrates the difference between the representation of the output hidden space from
the pre-trained langauge model. While the representation of time series learned from GPT4TS is
centered as a whole, the representation of the decomposed component from TEMPO implies a certain
soft boundary between the three components. This is a demonstration of how TEMPO is able to learn
the representation of trend, seasonality, residual parts respectively, which contributes to the superior
performance of our model TEMPO.

24

---

<!-- PAGE 25 -->

Published as a conference paper at ICLR 2024

(a) TEMPO-ETTh1

(b) GPT4TS-ETTh1

(c) TEMPO-ETTh2

(d) GPT4TS-ETTh2

(e) TEMPO-ETTm1

(f) GPT4TS-ETTm1

(g) TEMPO-ETTm2

(h) GPT4TS-ETTm2

Figure 12: Comparison of GPT4TS representation with TEMPO representation for prediction length
O = 96 using TSNE. Trend in red, seasonality in blue, residual in green.

25

---

<!-- PAGE 26 -->

Published as a conference paper at ICLR 2024

D.6 MODEL TRAINING TIME COMPARISON

Figure 13 illustrates the training time of other baseline models in comparison to our model TEMPO.
To ensure fairness, we calculated the percentage of runtime for models operating on identical machines
and utilizing equivalent computational resources. Each model’s training time is presented as a ratio
relative to TEMPO’s training time. A value less than 1 indicates that the model trains faster than
TEMPO, while a value greater than 1 suggests the opposite. We use horizontal bars to visually
represent each model’s relative training time, with the bars extending to the left or right of the central
vertical line based on whether they are faster or slower than our model TEMPO, respectively.

Figure 13: Visual Comparison on relative training time of other models and our proposed model
TEMPO under channel independent setting.

E THE ROLES OF GENERALIZED ADDITIVE MODELS (GAM) AND SHAPLEY

ADDITIVE EXPLANATIONS (SHAP)

In our paper, GAM and SHAP serve as instrumental tools, not only for affirming anticipated findings
but also for yielding deeper insights and explanations into the inner workings of intricate models.

• Role of GAM: GAM inherently models the effects of different features as additive compo-
nents. This characteristic of GAM provides intrinsic interpretability to TEMPO. It’s not
merely a tool for confirming the absence of patterns in residuals; it also helps us understand
how each feature contributes to the final prediction.

• Role of SHAP: SHAP helps in attributing feature effects post-hoc to explain the predictions

made by complex models, which may otherwise be opaque.

The utility of GAM and SHAP in our analysis can be detailed as follows:

• Confirmation of Assumptions: the analyses quantitatively confirm assumptions about model
behavior with data-driven evidence, rather than just intuition. This substantiation increases
the trust and transparency in the model’s predictions;

• Detecting Unexpected Behaviors: the component attribution could reveal unexpected be-
haviors if present. For example, residual impact being higher than expected could indicate
overfitting noise.

• Providing Nuanced Insights: SHAP provides nuance beyond high-level expectations, like

showing the increasing error of seasonal components in longer forecasts.

26

---

<!-- PAGE 27 -->

Published as a conference paper at ICLR 2024

Figure 14: The SHAP (SHapley Additive exPlanations) values of decomposed components of
TEMPO for weather dataset.

In our paper, we use the ETTm1 and weather datasets as detailed examples. The full results used
to calculate the SHAP value can be found at Table 11. In datasets exhibiting strong seasonality, the
seasonal component may display much larger variations than the residual component. Conversely,
in datasets with minimal seasonality, the variations between these two components should be more
comparable. We can calculate the strength of seasonality via:
Var (Rt)
Var (St) + Var (Rt)

S = max

0, 1 −

(7)

(cid:18)

(cid:19)

When we compare the seasonality strengths of different datasets, we find that ETTm1 (as shown in
Figure 2, with a seasonality strength of 0.99) constitutes strongly seasonal data, whereas the weather
dataset (depicted in Figure 14 with a seasonality strength of 0.476) exhibits less seasonality and a
more pronounced trend. These findings align with the conclusions drawn from the SHAP values.
The performance degradation of ETTm1, when the prediction length is increased, can be primarily
attributed to inaccuracies in the prediction of seasonal terms. In summary, SHAP provides pivotal
descriptive power for model transparency, moving beyond intuition. The ability to discern how much
and where components contribute enables targeted improvements. These insights can guide us in
better leveraging inductive bias to enhance both efficiency and effectiveness in the era of pre-training
models. One of the interesting future works is that we can adaptively and selectively optimize specific
components based on the GAM structure and SHAP scores during the training process. This approach
would allow us to focus our computational resources and efforts on the most influential components,
thereby improving the overall effectiveness of the model.

F BASELINE MODEL EXPLANATIONS

We demonstrate the baseline models we compared with in our experiments in the following:

• DLinear (Zeng et al., 2023): DLinear combines a decomposition scheme from Autoformer
and FEDformer with linear layers to predict time series data by modeling trend and seasonal
components separately and summing their features for enhanced performance in trend-rich
datasets.

• PatchTST (Nie et al., 2023): PatchTST is a Transformer-based model for multivariate time
series forecasting that segments data into subseries patches and uses a channel-independent
design to efficiently reduce computational costs while enhancing long-term prediction
accuracy.

27

---

<!-- PAGE 28 -->

Published as a conference paper at ICLR 2024

Table 11: SHAP original values for each component

w/o trend

w/o season w/o residual

trend

season

residual

empty set

complete set

MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE

96

0.437/0.432 0.670/0.526

0.457/0.441

0.663/0.541

0.472/0.455

0.680/0.535

1.104/0.790

0.438/0.424

ETTm1

192

336

720

0.466/0.447

0.646/0.518

0.488/0.455

0.682/0.529

0.483/0.455

0.666/0.526

1.101/0.789

0.461/0.432

0.505/0.466 0.672/0.530

0.526/0.476

0.680/0.531

0.524/0.475

0.707/0.543

1.102/0.790

0.515/0.467

0.579/0.507 0.678/0.549

0.586/0.508

0.684/0.548

0.592/0.509

0.709/0.558

1.105/0.794

0.591/0.509

Avg

0.497/0.463 0.666/0.531

0.514/0.470

0.677/0.537

0.518/0.474

0.691/0.540

1.103/0.791

0.501/0.458

96

0.213/0.267

0.202/0.261

0.205/0.264

0.223/0.289

0.234/0.293

0.220/0.284

0.637/0.608

0.211/0.254

Weather

192

336

720

0.266/0.317

0.251/0.297

0.256/0.306

0.254/0.304

0.290/0.335

0.262/0.316

0.638/0.608

0.254/0.298

0.317/0.356

0.290/0.333

0.295/0.331

0.293/0.331

0.328/0.357

0.313/0.356

0.640/0.609

0.292/0.332

0.402/0.401

0.371/0.383

0.377/0.380

0.364/0.378

0.389/0.393

0.385/0.398

0.638/0.610

0.370/0.379

Avg

0.300/0.335

0.279/0.318

0.283/0.320

0.283/0.325

0.310/0.345

0.295/0.339

0.638/0.609

0.282/0.316

• FEDformer (Zhou et al., 2022): FEDformer combines seasonal-trend decomposition with
Transformers for time series forecasting, leveraging frequency insights for efficiency and
accuracy, outperforming state-of-the-art methods.

• Informer (Zhou et al., 2021): Informer is a transformer-based model optimized for long
sequence time-series forecasting, leveraging ProbSparse self-attention for efficiency, self-
attention distilling for handling long inputs, and a generative decoder for rapid predictions.
• ETSformer (Woo et al., 2022): ETSformer is a novel Transformer architecture for time-
series forecasting that integrates exponential smoothing principles, replacing traditional
self-attention with exponential smoothing attention and frequency attention, to enhance
accuracy, efficiency, and interpretability.

• TimesNet (Wu et al., 2023): TimesNet transforms 1D time series into 2D tensors capturing
intra- and inter-period variations and uses TimesBlock with an inception block to extract
complex temporal patterns, excelling in multiple time series tasks.

• GPT-2 (Radford et al., 2019): GPT-2 is a decoder-based language model developed by
OpenAI, designed to generate coherent and diverse textual content from a given prompt. In
our work, we use the GPT-2 with 6 layers as the backbone, which is adapted from GPT4TS
(Zhou et al., 2023).

• BERT (Devlin et al., 2019): BERT (Bidirectional Encoder Representations from Trans-
formers) is an encoder-based deep learning model utilizing the Transformer architecture
designed by Google to understand the context of words in a sentence by analyzing text
bi-directionally.

• T5 (Raffel et al., 2020): T5 (Text-to-Text Transfer Transformer) is a state-of-the-art neural
network model with encoder-decoder based architecture designed by Google that converts
every language problem into a text-to-text format.

• LLaMA (Touvron et al., 2023): LLaMA (Large Langauge Model Meta AI) is a collection of
state-of-the-art foundation language models ranging from 7B to 65B parameters delivering
exceptional performance, while significantly reducing the needed computational power and
resources. In our work, we use the first 6 layers of 7B LLaMA.

G THEORICAL ANALYSIS

G.1 PROOF OF THEOREM 3.1

Theorem G.1 Suppose that we have time series signal Y (t) = S(t) + T (t) + R(t), t ∈ [t1, tn],
where S(t) is the seasonal signal (periodical), T (t) is the trend signal (non-periodical) and R(t) is
the residual signal. Let E = {e1, e2, ..., en} denote a set of orthogonal bases. Let ES ⊆ E denote
the subset of E on which S(t) has non-zero eigenvalues and ET ⊆ E denote the subset of E on
which T (t) has non-zero eigenvalues. If S(t) and T (t) are not orthogonal, i.e. (cid:80)n
i=1 S(ti)T (ti) ̸= 0,
then ET ∩ ES ̸= ∅, i.e. E can not disentangle the two signals onto two disjoint sets of bases.

28

---

<!-- PAGE 29 -->

Published as a conference paper at ICLR 2024

Proof 1 We decompose S(t) and T (t) onto E and acquire that S(t) = (cid:80) aiei and T (t) = (cid:80) biei.
Then it is obvious that ei ∈ ES ⇐⇒ ai ̸= 0 and ei ∈ ET ⇐⇒ bi ̸= 0. Now, let us consider the
inner product of S(t) and T (t):

n
(cid:88)

i=1

S(ti)T (ti) = S(t) · T (t) = (

(cid:88)

(cid:88)

aiei) · (

biei) =

(cid:88)

i,j

aibjeiej

(8)

Note that the components found by PCA is a set of orthogonal basis. Thus, for any i ̸= j, we have
eiej = 0. Thus, we have:

n
(cid:88)

i=1

S(ti)T (ti) = S(t) · T (t) = (

(cid:88)

(cid:88)

aiei) · (

biei) =

aibi||ei||2
2

(cid:88)

i

(9)

Note that (cid:80)n
ei ∈ ES and ei ∈ ET , in other words, ET ∩ ES ̸= ∅.

i=1 S(ti)T (ti) = 0. Thus, there must be at least one i such that ai ̸= 0 and bi ̸= 0. Thus,

The above theorem proves that if T (t) and S(t) are not orthogonal, then there does not exist a set
of orthogonal bases that disentangle S(t) and T (t) onto two disjoint sets of bases. Note that it is
common that a periodical signal is not orthogonal with a non-periodical signal. This is because
the spectrum of a periodical signal is discrete and the spectrum of a periodical signal is continuous.
Thus, it is very likely that there exist overlaps on those non-zero frequencies of the periodical signal.
Note that PCA also aims at learning a set of orthogonal bases on the data. We can quickly acquire
a corollary that PCA can not disentangle the two signals into two disjoint sets of bases. Based
on (Zhou et al., 2023)’s Theorem 1, we can reveal that self-attention in pre-trained large models
learns to perform a function closely related to PCA. Therefore, the self-attention mechanism cannot
automatically decompose the time series into its trend and seasonal components unless we manually
perform this operation.

G.2

INTERPRETING MODEL PREDICTIONS FROM FREQUENCY DOMAIN

In addition to Section 5.2, which gives an experimental perspective on why decomposition can aid
forecasting results, we provide a theoretical analysis from the spectral domain. Specifically, time
series signals can be represented as a combination of different frequencies in the spectral domain.
Forecasting is challenging because real-world series comprises convoluted mixtures of variations
with overlapping periodicities. However, by shifting our view to the frequency domain, we can
identify distinct components via STL decomposition containing isolated frequencies that stand out
clearly from the rest of the spectrum. This separation of dominant periodic patterns is crucial because
forecasting future values equates to predicting how these underlying frequencies evolve over time:

Proposition G.2 (Equivalence of time domain forecasting and frequency domain forecasting )
Assume x0, x1, ..., xN −1 and ˆx0, ˆx1..., ˆxN −1, ˆxN are the input and output sequences of the frequency
model. Then, ˆxN transferred from the frequency domain is the predicted value at timestamp N .

Given input sequence {xt|t = 0, 1, ..., N − 1}, where N is the number of discrete timestamps, in
the time domain, the Discrete Fourier Transform (DFT, F ) and inverse Discrete Fourier Transform
(iDFT, f ) operation to obtain the frequency domain can be defined as:

F (u) =

1
N

N −1
(cid:88)

x=0

f (x)e

−i2πux
N

, u = 0, 1, . . . , N − 1,

f (x) =

N −1
(cid:88)

u=0

F (u)e

i2πux

N , x = 0, 1, . . . , N − 1.

(10)

(11)

According to Proposition G.2, assuming that the next value of F (u), can be predicted as F ′(N ),
other unknown variables in the time and frequency domains, including the (N + 1)th discrete sample
f (N ) and the new DFT’s result F ′(u), u = 0, 1, 2, . . . , N − 1 are determined by the given F ′(N ).

29

---

<!-- PAGE 30 -->

Published as a conference paper at ICLR 2024

Proof 2 Let

then we have:

A =

N −1
(cid:88)

x=0

f (x)(

N

e− i2πux
N

−

N +1

e− i2πux
N + 1

),

B =

1
N + 1

N −1
(cid:88)

x=0

f (x)e− i2πN x
N +1 ,

f (N ) = (N + 1)(F ′(N ) − B)e− i2πN 2
N +1 ,

F ′(u) = A + (F ′(N ) − B)e

i2π(N −u)N
N +1

.

For u = 0, 1, 2, ..., N − 1, the value of F ′(u) − F (u) can be represented as:

F ′(u) − F (u) = A +

1
N + 1

f (N )e− i2πuN
N +1 .

For u = N , the value of F ′(N ) can be represented as

F ′(N ) = B +

1
N + 1

f (N )e− i2πN 2

N +1

.

Given F ′(N ), we can inference F ′(u) by:

F ′(u) = A + (F ′(N ) − B)e

i2π(N −u)N
N +1

, u = 0, 1, 2, ..., N − 1.

and f (N ) by:

Thus, the only variable that needs to be predicted is F ′(N ).

f (N ) = (N + 1)(F ′(N ) − B)e− i2πN 2
N +1 ,

(12)

(13)

(14)

(15)

(16)

(17)

(18)

(19)

This proposition reveals that if it is easy to predict patterns in the frequency domain, we can more
easily predict the time series’ future values. Forecasting equates to predicting the evolution of
the underlying frequencies that make up the time series signal. STL decomposition significantly
aids this task by separating components with distinct dominant periodic patterns. With STL, each
component presents far fewer intertwining periodic influences to disentangle, which notably simplifies
the prediction problem. For instance, the trend component may exhibit a lone annual cycle that
clearly dominates its spectrum. A targeted predictive model focusing solely on accurately estimating
the progression of this isolated frequency can generate accurate forecasts. Likewise, the seasonal
element neatly isolates recurring daily or weekly frequencies. Models tailored specifically for these
known periodicities allow for highly predictable extrapolations. In contrast, directly modeling the
raw data’s condensed spectrum with numerous blended periodic components yields unsatisfactory
approximations. The overlapping frequencies are difficult to distinguish and predict independently.

Conceptualizing forecasting through a frequency domain lens reveals how STL decomposes complex
spectral mixtures into distinguishable frequency-based sub-problems. This allows implementation
optimized predictive strategies to uncover patterns in each component for markedly improved time
series predictions. In essence, STL facilitates accurate future predictions by disentangling the spectral
content into simpler predictable forms.

H DETAIL OF THE TETS DATASET

Time series data Analyzing and forecasting a company’s future profitability and viability are
essential for its development and investment strategies. Financial assessment and prediction are
data-driven, mostly relying on the combination of diverse data types including company reports, etc.
In this project, our primary sources are the company’s financial statements: balanced sheet, income
statements, and cash flow statements.

The Standard & Poor’s 500 Index (S&P 500) represents a stock market index that measures the
stock performance of the 500 largest companies in the U.S.11 sectors in the S&P500 are included

30

---

<!-- PAGE 31 -->

Published as a conference paper at ICLR 2024

in our dataset: Basic Materials (21 companies), Communication Services (26 companies), Energy
(22 companies), Financial Services (69 companies), Healthcare (65 companies), Technology (71
companies), Utilities (30 companies), Consumer Cyclical (58 companies), Consumer Defensive (36
companies), Industrials (73 companies), Real Estate (32 companies). In terms of dataset division, we
separate the sectors in our dataset to achieve both in-domain task setting and zero-shot task setting.
The first seven sectors are treated as training and evaluation sectors, while the last four sectors are
reserved as unseen sectors for zero-shot forecasting task.

To address missing numerical information for companies in the S&P 500 that lack data prior to 2010,
we apply linear interpolation after experimenting with various methods. Linear interpolation is a
technique that estimates a value within a range using two known end-point values. For missing values
in research and development expenses, we adopted a zero-filling strategy. This is because null entries
in these statements typically indicate that the company did not make any investment in that area.

Contextual data collection This rise of Large-scale pre-trained models (LLMs) in the field of
Natural Langauge Processing has provided new possibilities for their application in time seris analysis.
LLMs have proven useful for analyzing and learning complicated relationships and making inferences
across different time series sequences. However, most existing approaches primarily convert time
series data to direct input into LLMs, overlooking the fact that the LLMs are pre-trained specifically
for natural language and thus neglecting the incorporation of contextual data.

Further, the information contained in time series data is limited, especially in the financial field. Time
series data in the financial field, such as company statements, primarily reflect the financial numeric
changes based on the company’s historical strategy and broader macroeconomic shifts. These data
contain the company’s internal historical information. However, the broader market environment,
referred to as external information, also plays an important role in the company’s future development.
For example, medicine and healthcare companies experienced steady growth before the outbreak of
COVID-19. But between 2019 and 2020, after the outbreak of the pandemic, the financial statements
of such companies were impacted significantly. As a result, we recognize the value of integrating
news and reports as external data sources to complement internal information contained in time
series data. The information contained in the external data mainly includes 3 parts: (i). Policy shifts
across regions (ii). Significant events occurring globally (iii). Public reaction to companies’ products.
Together, these elements provide supplementary information missing in time series data (internal
data), therefore enhancing our forecasting capabilities.

Extracting contextual data, such as news and reports, from varied sources presents a significant
challenge. In today’s digital age, numerous news websites and apps deliver a wide range of world
news, spanning from influential news affecting entire industries to trivial, minor reports. Thus, it is
crucial to filter and summarize the information, distinguishing between pivotal and less significant
news. Fortunately, the recently released ChatGPT API2 by Open AI offers the capability of collecting
and summarizing news and reports for a specified duration.

Through consolidating all relevant details – query, quarter, yearly context, company information,
and specific requirements – into user message and setting a cap at 110 tokens for response, we can
efficiently obtain the desired contextual information from ChatGPT API. For illustration, Figure 10
displays an example from company A, showcasing designed prompts and corresponding responses
from ChatGPT 3.5. If the contextual information can not be generated, the API often returns messages
with keywords such as ’unfortunately’ and ’sorry’. We detect and replace them with the term ’None’,
representing neutral contextual information. Additionally, Figure 15 and 17 provide a illustration of
our dataset, encompassing both time series data and the corresponding contextual texts. A detailed
view of the contextual texts can be seen in Figure 16 and 18.

2https://platform.openai.com/docs/guides/gpt

31

---

<!-- PAGE 32 -->

Published as a conference paper at ICLR 2024

Figure 15: EBITDA for Company A with contextual information

Figure 16: Example of generated contextual information for Company A marked in Figure 15

Figure 17: EBITDA for Company B with contextual informatino

32

---

<!-- PAGE 33 -->

Published as a conference paper at ICLR 2024

Figure 18: Example of generated contextual information for Company B marked in Figure 17

Table 12: Table of Main Notation on TEMPO

Notation

Description

ˆxi
t
xi
t

Φ

V

X

XT t, XSt, XRt
xi
ˆxi

T t

T t

ith channel prediction at time step t
ith channel look back window/historical values at time step t

model parameter

prompt value from prompt pool

input data which can be decomposed into XT XS XR

trend, season, residual component set in time t
ith channel tth timestep of xi
T

predict value of trend component

P

km

Vm

Vk

K

M
Z ∗

LH

LE

Y∗
ˆY∗

patch of input data
mth key in prompt pool
mth value in prompt pool

prompt pool

hyperparameter, number of prompts to choose

hyperparameter, length of prompt pool

GPT output for * (trend, seasonal, residual)

prediction length

embedding vector length

final predict value before de-normalization

final predict value

33

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

PublishedasaconferencepaperatICLR2024
| TEMPO:      |     | PROMPT-BASED |     |     | GENERATIVE |        |             | PRE-TRAINED |     |
| ----------- | --- | ------------ | --- | --- | ---------- | ------ | ----------- | ----------- | --- |
| TRANSFORMER |     |              |     |     | TIME       | SERIES | FORECASTING |             |     |
FOR
DefuCao1,FurongJia1,SercanO¨.Arık2,TomasPfister2,YixiangZheng1,WenYe1,YanLiu1
1UniversityofSouthernCalifornia
2GoogleCloudAIResearch
| {defucao, |     | florajia,             | yixiangzheng, |     | yewen, | yanliu.cs}@usc.edu |     |     |     |
| --------- | --- | --------------------- | ------------- | --- | ------ | ------------------ | --- | --- | --- |
| {soarik,  |     | tpfister}@google.com, |               |     |        |                    |     |     |     |
ABSTRACT
Thepastdecadehaswitnessedsignificantadvancesintimeseriesmodelingwith
|     | deep                                               | learning. | While | achieving | state-of-the-art |     | results, | the best-performing  | ar- |
| --- | -------------------------------------------------- | --------- | ----- | --------- | ---------------- | --- | -------- | -------------------- | --- |
|     | chitecturesvaryhighlyacrossapplicationsanddomains. |           |       |           |                  |     |          | Meanwhile,fornatural |     |
languageprocessing,theGenerativePre-trainedTransformer(GPT)hasdemon-
|     | strated | impressive | performance    |          | via training      | one        | general-purpose | model              | across |
| --- | ------- | ---------- | -------------- | -------- | ----------------- | ---------- | --------------- | ------------------ | ------ |
|     | various | textual    | datasets.      | It       | is intriguing     | to explore | whether         | GPT-type architec- |        |
|     | tures   | can be     | effective      | for time | series, capturing |            | the intrinsic   | dynamic attributes |        |
|     | and     | leading    | to significant | accuracy | improvements.     |            | In this         | paper, we propose  | a      |
novelframework,TEMPO,thatcaneffectivelylearntimeseriesrepresentations.
|     | We focus           | on  | utilizing                                            | two essential | inductive | biases | of  | the time series | task for |
| --- | ------------------ | --- | ---------------------------------------------------- | ------------- | --------- | ------ | --- | --------------- | -------- |
|     | pre-trainedmodels: |     | (i)decompositionofthecomplexinteractionbetweentrend, |               |           |        |     |                 |          |
seasonalandresidualcomponents;and(ii)introducingthedesignofpromptsto
|     | facilitatedistributionadaptationindifferenttypesoftimeseries. |     |     |     |     |     |     | TEMPOexpands |     |
| --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- |
thecapabilityfordynamicallymodelingreal-worldtemporalphenomenafromdata
|     | withindiversedomains. |     |     | Ourexperimentsdemonstratethesuperiorperformanceof |     |     |     |     |     |
| --- | --------------------- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
TEMPOoverstate-of-the-artmethodsonzeroshotsettingforanumberoftime
|     | seriesbenchmarkdatasets. |     |     | Thisperformancegainisobservednotonlyinscenarios |     |     |     |     |     |
| --- | ------------------------ | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
involvingpreviouslyunseendatasetsbutalsoinscenarioswithmulti-modalinputs.
ThiscompellingfindinghighlightsTEMPO’spotentialtoconstituteafoundational
model-buildingframework.
1 INTRODUCTION
Timeseriesforecasting,i.e.,predictingfuturedatabasedonhistoricalobservations,hasbroadreal-
worldapplications,suchashealth,transportation,financeandsoon. Inthepastdecade,numerous
deepneuralnetworkarchitectureshavebeenappliedtotimeseriesmodeling,includingconvolutional
neuralnetworks(CNN)(Baietal.,2018),recurrentneuralnetworks(RNN)(Siami-Naminietal.,
2018),graphneuralnetworks(GNN)(Lietal.,2018;Caoetal.,2021),andTransformers(Liuetal.,
2021;Zhouetal.,2021;Wuetal.,2023;Zhouetal.,2022;Wooetal.,2022;Kitaevetal.,2020;Nie
etal.,2023),leadingtostate-of-the-artsresults.Whileachievingstrongpredictionperformance,some
ofthepreviousworksontimeseriesmostlybenefitfromtheadvanceinsequencemodeling(from
RNNandGNN,totransformers)thatcapturestemporaldependenciesbuthavenotfullycapitalized
onthebenefitsofintricatepatternswithintimeseriesdata,suchasseasonality,trend,andresidual.
These components are the key differentiating factors of time series from classical sequence data
(Fildesetal.,1991). Asaresult,recentstudiessuggestthatdeeplearning-basedarchitecturesmight
notbeasrobustaspreviouslythoughtandmightevenbeoutperformedbyshallowneuralnetworks
orevenlinearmodelsonsomebenchmarks (Zengetal.,2023;Zhangetal.,2022b;Wuetal.,2023;
Ekambarametal.,2023;Fanetal.,2022). Despitethenotablesuccessofdeeplearningforecasters,
thevastmajorityofthemstillfollowaconventionaltrainingmechanism, trainingandpredicting
usingthesamedatasets.
Meanwhile,theriseoffoundationmodelsinnaturallanguageprocessing(NLP)andcomputervision
(CV), such as LLaMA (Touvron et al., 2023), CLIP (Radford et al., 2021) and ChatGPT, marks
1

PublishedasaconferencepaperatICLR2024
majormilestonesoneffectiverepresentationlearning. Itisextremelyintriguingtoexploreapre-
trainedpathforfoundationtimeseriesmodelswithvastamountsofdata,facilitatingperformance
improvementindownstreamtasks. Somerecentworksshedlightintothepossibilityofbuilding
general transformers for time series (Zhou et al., 2023; Sun et al., 2023; Goswami et al., 2024;
Dasetal.,2023b;Rasuletal.,2023). However,thetheoreticalandpracticalunderstandingofsuch
modelshasnotreachedtheconsensusobservedinotherdomainswheregenerativemodelshavebeen
widelyacknowledged(Garza&Mergenthaler-Canseco,2023). Inaddition,promptingtechniquesin
LLM(suchasInstructGPT(Ouyangetal.,2022))provideawaytoleveragethemodel’sexisting
representationsduringpre-traininginsteadofrequiringlearningfromscratch. However,existing
backbonestructuresandprompttechniquesinlanguagemodelsdonotfullycapturetheevolutionof
temporalpatternsasinN-BEATS(Oreshkinetal.,2019)andAutoFormer(Wuetal.,2021),which
arefundamentalfortimeseriesmodeling.
Inthispaper,wemakeanattempttoaddressthetimelychallengesofadaptinglargepre-trainedmodels
fortimeseriesforecastingtasksanddevelopingaprompt-basedgenerativepre-trainingtransformer
fortimeseries,namelyTEMPO.TEMPOconsistsoftwokeyanalyticalcomponentsforeffectivetime
seriesrepresentationlearning: onefocusesonmodelingspecifictimeseriespatterns,suchastrends
andseasonality,andtheotherconcentratesonobtainingmoreuniversalandtransferrableinsights
fromtheinherentpropertiesofdatathroughaprompt-basedapproach. Specifically,TEMPOfirstly
decomposestimeseriesinputintothreeadditivecomponents,i.e.,trend,seasonality,andresiduals
vialocallyweightedscatterplotsmoothing(Clevelandetal.,1990). Eachofthesetemporalinputsis
subsequentlymappedtoitscorrespondinghiddenspacetoconstructthetimeseriesinputembedding
ofthegenerativepre-trainedtransformer(GPT).Weconductaformalanalysis,bridgingthetime
seriesdomainwiththefrequencydomain,tohighlightthenecessityofdecomposingsuchcomponents
fortimeseriesanalysis. Inaddition,wetheoreticallyrevealthattheattentionmechanismishard
toachievethedecompositionautomatically. Second,TEMPOutilizesasoftprompttoefficiently
tunetheGPT (Radfordetal.,2019)forforecastingtasksbyguidingthereuseofacollectionof
learnablecontinuousvectorrepresentationsthatencodetemporalknowledgeoftrendandseasonality.
Inaddition,weleveragethethreekeyadditivecomponentsoftimeseriesdata—trend,seasonality,
andresiduals—toprovideaninterpretableframeworkforcomprehendingtheinteractionsamong
inputcomponents(Hastie,2017). Experimentresultsonzeroshotsettingandmultimodalsettingof
TEMPOpavethepathtofoundationalmodelsfortimeseries. Besides,wedemonstratethestable
predictivepowerofourmodelonunseensampleswithtextualinformationontwomultimodaldatasets
includingTETS(TextforTimeSeries)dataset,whichisfirstintroducedinthisworktofosterfurther
researchtopicsofpre-trainedtimeseriesmodels.
Insummary,themaincontributionsofourpaperinclude: (1)Weintroduceaninterpretableprompt-
tuning-based generative transformer, TEMPO, for time series representation learning. It further
drives a paradigm shift in time series forecasting - from conventional deep learning methods to
pre-trainedfoundationalmodels. (2)Weadaptpre-trainedmodelsfortimeseriesbyfocusingon
two fundamental inductive biases: First, we utilize decomposed trend, seasonality, and residual
information. Second, we explore the soft prompt strategies to accommodate time series data’s
dynamicnature. (3)Throughextensiveexperimentationonbenchmarkdatasetsandtwomultimodal
datasets,ourmodeldemonstratessuperiorperformance.Notably,ourrobustresultstowardshighlights
thepotentialoffoundationalmodelsintherealmoftimeseriesforecasting.
2 RELATED WORKS
Pre-trainedLargeLanguageModelsforTimeSeries. TherecentdevelopmentofLargeLanguage
Models (LLMs) has opened up new possibilities for time-series modeling. LLMs, such as T5
(Raffeletal.,2020),GPT(Radfordetal.,2018),GPT-2(Radfordetal.,2019),GPT-3(Brownetal.,
2020),GPT-4(OpenAI,2023),LLaMA(Touvronetal.,2023),havedemonstratedastrongabilityto
understandcomplexdependenciesofheterogeneoustextualdataandprovidereasonablegenerations.
Recently,thereisgrowinginterestinapplyinglanguagemodelstotimeseriestasks(Jinetal.,2024a;
Gruveretal.,2024). Forexample,Xue&Salimnaivelyconverttimeseriesdatatotextsequence
inputsandachievesencouragingresults. Sunetal. proposetextprototype-alignedembeddingto
enableLLMstohandletimeseriesdata. Inaddition,Yuetal. presentaninnovativeapproachtowards
leveragingLLMsforexplainablefinancialtimeseriesforecasting. Theworksin(Zhouetal.,2023)
and(Changetal.,2023)arethemostrelevantonestoourwork,astheybothintroduceapproachesfor
2

PublishedasaconferencepaperatICLR2024
Prompt Module

Add & Norm
|     |                            |              |  ...Trend ...   | Val |                      | Attention   |          |     |
| --- | -------------------------- | ------------ | --------------- | --- | -------------------- | ----------- | -------- | --- |
|     | Trainable Blocks           |              | ...Seasonal ... | Val | Feed Forward Layer   |             |          |     |
|     |                            |              |                 |     |                      | Q           | K V      |     |
|     | Frozen Blocks              |              | ...Residual ... | Val | 6 x Add & Norm       |             |          |     |
|     |                            |              |                 |     |                      | L o RA      | L o R A  |     |
|     | Pr e -t ra in e d  P a r a | m et e r s
 |                 |     | Multi-head Attention |             |          |     |
|     | f ro m  G e n e ra t i v   | e P r e -    |                 |     |                      | Hi d d en S | t a t es |     |
trained Transformer
Prompt
|     |       | Normalize |          | Embedding |             |        |              |     |
| --- | ----- | --------- | -------- | --------- | ----------- | ------ | ------------ | --- |
|     |       |           |          |           | Tra n s f o | r mer  | De-Normalize |     |
|     | Trend |           | Patching |           | B l o c     | k s    |              |     |
Prompt
|                   |          | Normalize |          | Embedding |     |     | De-Normalize | Prediction |
| ----------------- | -------- | --------- | -------- | --------- | --- | --- | ------------ | ---------- |
| time series input | Seasonal |           | Patching |           |     |     |              |            |
Positional
Embedding
Prompt
De-Normalize
|     |          | Normalize |          | Embedding |     |     |     |     |
| --- | -------- | --------- | -------- | --------- | --- | --- | --- | --- |
|     | Residual |           | Patching |           |     |     |     |     |
Linear Output Layer
Figure1:ThearchitectureofproposedTEMPO-GPT.ThetrendX ,seasonalX andresidualX components
|     |     |     |     |     |     | T S | R   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
aretreatedasdifferentsemanticinductivebiasestofeedintothepre-trainedtransformer.
time-seriesanalysisbystrategicallyleveragingandfine-tuningLLMs. However,thesestudiesdirectly
employ time series data to construct embeddings, without adequately capturing the inherent and
unqiuecharacteristicsoftimeseriesdatawhichischallengingtodecouplesuchinformationwithin
theLLMs(Shinetal.,2020). Inaddition,thereisstillverylimitedworkonLLMformultimodal
datawithtimeseries. METS(Lietal.,2023)isoneoftheearlyworkspursuingthisdirection. While
theexperimentresultsareencouraging,itisdifficulttoextendMETStoothermodalitiessincethe
embeddingalignmentbetweentimeseriesandtextsarespecific. Pleaserefertothesuverypapers
(Jinetal.,2023;2024b)forfurtherreferencesoftimeseriesmeetingLLMs.
Prompttuning. Prompttuningisanefficient,low-costwayofadaptingapre-trainedfoundation
modeltonewdownstreamtaskswhichhasbeenadaptedtodownstreamtasksacrossvariousdomains.
InNLPdomain,softpromptswithtrainablerepresentationareusedthroughprompt-tuning(Lester
etal.,2021)orprefix-tuning(Li&Liang,2021).PromptingtechniqueshavealsobeenextendedtoCV
taskslikeobjectdetection(Lietal.,2022)andimagecaptioning(Zhangetal.,2022a),etcandother
domainssuchasmisinformation(Zhangetal.,2024). Multimodalworks,suchasCLIP(Radford
etal.,2021),usetextualpromptstoperformimageclassificationandachieveSOTAperformance. In
addition,L2P(Wangetal.,2022b)demonstratesthepotentialoflearnablepromptsstoredinashared
pool to enable continual learning without rehearsal buffer, and Dualprompt (Wang et al., 2022a)
introduces a dual-space prompt architecture, maintaining separate prompt encodings for general
knowledgeandexpertinformation,etc. Ourresearchbuildsupontheseconceptsbyexploringthe
useofpromptdesignfromindicativebiasspecificallyfortemporalreasoningandknowledgesharing
acrosstimeseriesforecastingproblems.
3 METHODOLOGY
Inourwork,weadoptahybridapproachthatincorporatestherobustnessofstatisticaltimeseries
analysiswiththeadaptabilityofdata-drivenmethods. AsshowninFigure1,weproposeanovel
integrationofseasonalandtrenddecompositionfromSTL(Clevelandetal.,1990)intothepre-trained
transformers. Thisstrategyallowsustoexploittheuniquestrengthsofbothstatisticalandmachine
learningmethods,enhancingourmodel’scapacitytohandletimeseriesdataefficiently. Moreover,a
semi-softpromptingapproachisintroducedtoenhancetheadaptabilityofpre-trainedmodelsfor
handlingtimeseriesdata. Thisinnovativeapproachenablesthemodelstomergetheirextensive
learnedknowledgewiththeuniquerequirementsintrinsictotimeseriesanalysis.
3.1 PROBLEMDEFINITION
GivenobservedvaluesofpreviousK timestamps,thetaskofmultivariatetime-seriesforecasting
| aimstopredictthevaluesforthenextH |     |     |             | timestamps. | Thatis, |        |     |     |
| --------------------------------- | --- | --- | ----------- | ----------- | ------- | ------ | --- | --- |
|                                   |     |     | xˆi,...,xˆi | =F(xi       | ,...,xi | ;Vi;Φ) |     | (1) |
|                                   |     |     | t t+H−1     |             | t−K     | t−1    |     |     |
3

PublishedasaconferencepaperatICLR2024
wherexˆi,...,xˆi isthevectorofH-stepestimationfromtimestamptofchannelicorresponding
|     | t t+H−1 |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
tothei-thfeature. Giventhehistoricalvaluesxi ,...,xi ,itcanbeinferredbymodelF with
|     |     |     |     |     | t−K | t−1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
parameter Φ and prompt Vi. In anticipation of the foundational model’s strong generalization
capabilitiesacrossunseendatasets,wedefaulttoazero-shotlearningconfigurationintheabsenceof
specificindications. Thisapproachentailsthatthemodelisnotprivytothetargetdataset’shistory
valueandhorizonvalueduringthetrainingprocess.
3.2 TIMESERIESINPUTREPRESENTATION
Fortimeseriesdata,representingthecomplexinputbydecomposingitintomeaningfulcomponents,
suchastrendandseasoncomponents,canhelpextractinformationoptimally. Inthispaper,given
theinputX ∈Rn×L,wherenisthefeature(channel)sizeandLitthelengthofthetimeseries,the
additiveSTLdecomposition(Clevelandetal.,1990)canberepresentedas:
|     |     |     |     | Xi =Xi | +Xi | +Xi. |     |     | (2) |
| --- | --- | --- | --- | ------ | --- | ---- | --- | --- | --- |
|     |     |     |     |        | T   | S R  |     |     |     |
Here,iisthechannelindex(correspondingtoacertaincovariate)formultivariatetimeseriesinput,
and the trend X ∈ Rn×L = 1 (cid:80)k X captures the underlying long-term pattern in the
|     |     | T   |     | j=−k | t+j |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
m
data,wherem = 2k+1andk istheaveragingstepsize. TheseasonalcomponentX ∈ Rn×L
S
encapsulates the repeating short-term cycles, which can be estimated after removing the trend
|     |     |     |     | X   | ∈ Rn×L |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
component. The residual component R represents the remainder of the data after the
trendandseasonalityhavebeenextracted. Notethat,inpractice,itissuggestedtoleverageasmuch
information as possible to achieve a more precise decomposition. However, in consideration of
computational efficiency, we opt not to use the STL decomposition on the largest possible data
windowoneachinstance. Instead,weperformlocaldecompositionwithineachinstanceusingafixed
windowsize. InspiredbyN-BEATs(Oreshkinetal.,2019),weintroducelearnableparametersfor
estimatingthevariouslocaldecompositioncomponents. Samefortheothers. Thisprincipleapplies
toothercomponentsofthemodelaswell. InAppendixG,weestablishaconnectionbetweentime
seriesforecastingandfrequencydomainprediction,whereourfindingsindicatethatdecomposition
significantlysimplifiesthepredictionprocess. Notethatsuchdecompositionisofmoreimportance
incurrenttransformer-basedmethodsastheattentionmechanism,intheory,maynotdisentanglethe
disorthogonaltrendandseasonsignalsautomatically:
Theorem3.1 SupposethatwehavetimeseriessignalX = X +X +X ,t ∈ [t ,t ]. Let
|     |     |     |     |     |     |     | Tt St | Rt  | 1 n |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
E ={e ,e ,...,e }denoteasetoforthogonalbases. LetE ⊆E denotethesubsetofE onwhich
|     | 1 2 | n   |     |     |     |     | S   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X has non-zero eigenvalues and E ⊆ E denote the subset of E on which X has non-zero
| St  |     |     |     | T   |     |     |     | Tt  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eigenvalues. IfX andX arenotorthogonal,i.e. (cid:80)n Xi Xi ̸=0,thenE ∩E ̸=∅,i.e. E
|     |     | St  | Tt  |     |     | i=1 | Tt St | T   | S   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
cannotdisentanglethetwosignalsontotwodisjointsetsofbases.
TheproofcanbefoundinAppendixG.Theorem 3.1statesthatiftrendandseasonalcomponents
of a time series are non-orthogonal, they cannot be fully disentangled and separated by any set
oforthogonalbases. Accordingto (Zhouetal.,2023),theself-attentionlayernaturallylearnsan
orthogonaltransformation,akintoPCA’sdecompositionintoorthogonalprincipalcomponents. Thus,
applyingattentiondirectlytoarawtimeserieswouldbeineffectiveatdisentanglingnon-orthogonal
trendandseasonalcomponents. Fortheremainderofthemethodologysection,wewillutilizethe
trendcomponentX astheexemplarycase. Wefirstapplyreverseinstancenormalization(Kimetal.,
T
2022)oneachglobalcomponentandlocalinputrespectivelytofacilitateknowledgetransferand
minimizelossesintroducedbydistributionshifts. Thatis,foreachsamplex fromX ’s-thchannel
|     |     |          |     |           |     |          |     | Tt T |                 |
| --- | --- | -------- | --- | --------- | --- | -------- | --- | ---- | --------------- |
|     |     | (cid:16) |     | (cid:112) |     | (cid:17) |     |      | (cid:2) (cid:3) |
oftimet,xˆ = γ x −E [x ]/ Var[x ]+ϵ +β ,whereE [x ]andVar xi are
|     | Tt  | T Tt | t   | Tt  | Tt  | T   | T   | t Tt | Tt  |
| --- | --- | ---- | --- | --- | --- | --- | --- | ---- | --- |
theinstance-specificmeanandstandarddeviation;γ andβ aretrainableaffineparametervectors
|     |     |     |     |     |     | T   | T   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for trend component. In addition, we implement a mean square error (MSE) reconstruction loss
functiontoensurethatthelocaldecompositionalignswiththeglobalSTLdecompositionobserved
inthetrainingdata. Thedecompositionlossfunction,denotedasL =f (X,θ )−Xˆg,where
|     |     |     |     |     |     |     | Dec | T T | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f isthefunctionwithlearnablevariablesθ formappinglocaldecompositiontobealignedwith
| T   |     |     |     |     | T   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theglobaldecompositionafternormalizationXˆg.
|     |     |     |     |     |     | Then,following | (Nieetal.,2023),wecombine |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | ------------------------- | --- | --- |
T
time-series patching with temporal encoding to extract local semantics by aggregating adjacent
time steps into tokens, significantly increasing the historical horizon while reducing redundancy.
Specifically,wegetthepatchedtokenforthei-thnormalizedtrendcomponentforf (Xi,θ )with
|     |     |     |     |     |     |     |     | T   | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4

PublishedasaconferencepaperatICLR2024
(cid:106) (cid:107)
P
T
i ∈RLP×N,whereL
P
isthepatchlength,N = (L−
S
LP) +2isthenumberofpatchesandS is
thestride. WegetpatchedtokensPi andPi inthesameway. Then,wefeedthepatchedtimeseries
S R
tokenstotheembeddinglayerf togettherepresentationPi =f(Pi)∈RP×LE forthelanguage
T T
modelarchitecturetotransferitslanguagecapabilitiestothenovelsequentialmodalityeffectively,
whereL istheembeddingsize.
E
3.3 PROMPTDESIGN
Promptingtechniqueshavedemonstratedremarkableeffectivenessacrossawiderangeofapplications
byleveragingthepoweroftask-specificknowledgeencodedwithincarefullycraftedprompts. This
successcanbeattributedtotheprompts’abilitytoprovideastructuredframeworkthatalignsthe
model’soutputswiththedesiredobjectives,resultinginenhancedaccuracy,coherence,andoverall
qualityofthegeneratedcontent. Previousworksmostlyfocusonutilizingafixedprompttoboostthe
pre-trainedmodels’performancethroughfine-tuning(Brownetal.,2020). Inpursuitofleveraging
the rich semantic information encapsulated within various time series components, our research
introducesasemi-softpromptingstrategy. Thisapproachinvolvesthegenerationofdistinctprompts
correspondingtoeachprimarytimeseriescomponent: trend,seasonality,andresiduals. ‘Predict
thefuturetimestepgiventhe[trend,season,residual]’servesasthetemplatefromwhichwederive
ourcomponent-specificprompts. Thesearesubsequentlyconcatenatedwiththerelevantcomponent
data,therebyenablingamorerefinedmodelingapproachthatacknowledgesthemultifacetednature
oftimeseriesdata. Specifically,commencebytranslatingthetrend-specificpromptsintotheword
embeddingspace,followedbyalineartransformationtoderivethelearnabletrendpromptvectorV .
t
Thisso-called‘semi-soft’promptdesignthusstrikesabalancebetweentheinterpretabilityandinitial
guidanceofa‘hard’promptandtheadaptabilityofa‘soft’prompt. Thecombinedembeddingofthis
promptwiththetimeseriesrepresentationisencapsulatedby:
x =[V ;P ] (3)
T t T
Here, x denotes the aggregation of embeddings along the temporal axis. This concatenation
T
procedureismirroredfortheseasonalityandresidualcomponents,yieldingx andx ,respectively.
S R
Thisframeworkallowsforaninstancetobeassociatedwithspecificpromptsastheinductivebias,
jointly encoding critical information relevant to the forecasting task, such as recurring patterns,
overarchingtrends,andinherentseasonalityeffects. Itisofnotethatourpromptdesignmaintainsa
highdegreeofadaptability,ensuringcompatibilitywithabroadspectrumoftimeseriesanalyses. In
particular,similarwith (Wangetal.,2022a),weintroducepromptpoolasanextensionofourdesign
ofsoftpromptinAppendix D,aimedataccommodatingthecharacteristicallynon-stationarynature
ofreal-worldtimeseriesdataandtheassociateddistributionalshifts(Huangetal.,2020;Fanetal.,
2023). Thisadaptabilityunderscoresthepotentialofourpromptingstrategytoevolveincongruence
withthecomplexitiespresentedbydiversetimeseriesdatasets.
3.4 GENERATIVEPRE-TRAINEDTRANSFORMERARCHITECTURE
Weusethedecoder-basedgenerativepre-trainedtransformer(GPT)asthebackbonetobuildthe
basis for the time-series representations. To utilize the decomposed semantic information in a
data-efficientway,wechoosetoconcatenatethepromptanddifferentcomponentstogetherandput
themintotheGPTblock. Specifically,theinputofourtimeseriesembeddingcanbeformulated
as: x = x ⊕x ⊕x ,where⊕correspondstoconcatenateoperationandx canbetreatedas
T S R ∗
differentsentences. Notethat, anotheralternativewayistobuildseparateGPTblockstohandle
differenttypesoftimeseriescomponents. InsidetheGPTblock,weadoptthestrategyusedin(Zhou
etal.,2023)andopttoupdatethegradientsofthepositionembeddinglayerandlayernormalization
layers. Inaddition,weemployLORA(Low-RankAdaptation)(Huetal.,2021)toadapttovarying
timeseriesdistributionsefficientlyasitperformsadaptationwithsignificantlyfewerparameters.
Theoverallforecastingresultshouldbeanadditivecombinationoftheindividualcomponentpre-
dictions. Finally,theoutputsZ ofnfeaturesfromtheGPTblockcanbesplitintoZ ,Z ,Z ∈
T S R
Rn×P×LE (output corresponding to trend, seasonality, and residual) based on their positions in
theinputorder. EachZ componentisthenfedintofullyconnectedlayerstogeneratepredictions
Y
∗
∈Rn×LH,whereL
H
isthepredictionlength. Theforecastresultscanbeformulatedasfollows:
Yˆ =Yˆ +Yˆ +Yˆ . Afterthat,wede-normalizeY accordingtothecorrespondingstatisticsusedin
T S R
5

PublishedasaconferencepaperatICLR2024
thenormalizationstep: Yˆ t i = (cid:113) Var (cid:2) xi t (cid:3) +ϵ· (cid:16) Y t i γ −β (cid:17) +E t (cid:2) xi t (cid:3) . Byrecombiningtheseadditive
elements,ourapproachaimstoreconstructthefulltemporaltrajectorymostrepresentativeofthe
underlyingdynamicsacrossvariedtimescalescapturedbythedecomposedinputrepresentation.
Inordertoachieveinterpretability,weexplorebothlinearandnonlinearinteractionsamongtrend,
seasonal,andresidualcomponentsintheircontributiontothefinaloutput. Thereforeweconstructan
interpretablegeneralizedadditivemodel(GAM)(Hastie,2017)basedonGPT’soutputtolearnhow
(cid:80) (cid:80)
thethreecomponentsinteractwitheachother,whichis: g(Y)=F + F (x )+ F (x ),
∅ i i i t It It
whereF isanormalizingconstant, thefootnoteicorrespondstothetrend, season, andresidual
∅
component. {I }isofasetofmultipleinteractcomponents. Then,wecancalculatethefirst-order
t
sensitivityindex (Sobol’,1990)orSHAP(SHapleyAdditiveexPlanations)value(Lundberg&Lee,
2017)tomeasurethesensitivityofeachcomponent.
4 EXPERIMENTS
Ourexperimentsareconductedusingwidely-recognizedtimeseriesbenchmarkdatasets,suchas
thosedetailedin(Zhouetal.,2021),alongsidetheGDELTdataset(Jiaetal.,2024)andourproposed
TETSdataset. Thesecomprehensivedatasetsencompassadiversearrayofdomains,including,but
notlimitedto,electricity(ETTh1,ETTh2,ETTm1,ETTm2,Electricity),traffic(Traffic),climate
(Weather),news(GDELT),andfinance(TETS),withdatasamplingfrequenciesrangingfromminutes,
hours to days and quarters. The inclusion of such varied datasets ensures a thorough evaluation
of our experimental setups across multiple dimensions of time series data. Due to the absence
of a standard test split for zero-shot comparison, we adopt a uniform training methodology to
ensurefairperformanceassessmentacrossdatasetsunseenduringmodeltraining. Specifically,to
advancetheparadigmoffoundationmodelswithinthedomainoftransferlearning,weinvestigate
azero-shotsettingforourexperiments,whichisthe‘many-to-one’scenario: trainingonmultiple
sourcedatasetsfollowedbyzero-shotforecastingonadistinct,unseentargetdataset. Forinstance,
whenevaluatingperformanceona‘weather’dataset,ourmodelispre-trainedondiversedatasets
including‘ETTm1,ETTm2,ETTh1,ETTh2,Electricity,andTraffic’withoutexposuretothetarget
weatherdata. This’many-to-one’approachdiffersfundamentallyfrom‘one-to-one’or‘one-to-many’
configurations(Zhangetal.,2022c)byusingdiversepre-trainingdatasetsfromvarieddomains,like
trafficandweatherdata. Thisdiversity,whilerich,introducescomplexity,asthemodelmustidentify
patternsacrosspotentiallymisalignedsamples,complicatinglearningcomparedtomodelstrained
andtestedonindistributiondatasets.
WeuseGPT-2(Radfordetal.,2019)asourbackbonetobuildTEMPO1 asshowninFigure1. To
comprehensivelydemonstratetheperformanceofourmodel,wecompareTEMPO withthefollowing
baselinesoverlong-termforecastingandshort-termforecasting: (1)Thepre-trainedLLM-based
models,includingBert(Devlinetal.,2019),GPT2(Radfordetal.,2019;Zhouetal.,2023),T5(Raffel
etal.,2020),andLLaMA(Touvronetal.,2023). (2)TheTransformer-basedmodels,includingthe
PatchTST (Nie et al., 2023), FEDformer (Zhou et al., 2022), ETSformer (Woo et al., 2022) and
Informer(Zhouetal.,2021). (3)ThevariantofLinear-basedmodels,DLinear(Zengetal.,2023)
model.(4)General2D-variationmodel,TimesNet(Wuetal.,2023).Followingtraditionalforecasting
works,wereporttheMeanSquaredError(MSE)andMeanAbsoluteError(MAE)resultsinthis
section. PleaserefertotheAppendixBandFforthedetailedexperimentsettingandbaselines.
4.1 ZEROSHOTLONG-TERMFORECASTINGRESULTS
Table 1presentstheperformanceofmultipletimeseriesforecastingmodelsonMSEandMAEmetrics
acrossdifferentpredictionlengthsunderthe‘many-to-one’setting,withlowerscoresindicatingmore
accurateforecasts. Ourproposedmodel,TEMPO,surpassedexistingbaselinesonaverageoverall
predictionhorizonsacrossalldatasets,highlightingthebroadapplicabilityofTEMPO.Ourmodel
achievesthehighestaverageperformancescores. Specifically,itimprovestheweatherandETTm1
datasetsbyaround6.5%and19.1%,respectivelyinMAEcomparedtothepreviousstate-of-the-art
model,PatchTST.Italsosecuresthelowesterrorratesacrossnumerousindividualdataset-prediction
lengthconfigurations. Comparedtootherpre-trainedmodelsforforecasting,TEMPO consistently
deliversthebestresultsacrossdifferenttimeseriesdatasets. Theseresultssuggestthatincorporating
1TEMPO’ssourcecodecanbefoundat:https://github.com/DC-research/TEMPO
6

PublishedasaconferencepaperatICLR2024
Table1: Transferlearningoflong-termforecastingresultsontimeseriesbenchmarkdatasets. Weuse
predictionlengthO ∈{96,192,336,720}.
|     |     |     | AlowerMSEindicatesbetterperformance. |     |     |     | Hereafter, |
| --- | --- | --- | ------------------------------------ | --- | --- | --- | ---------- |
forthetables,thebestresultsaremarkedinboldandthesecondoptimalinunderlined,respectively
withMSE/MAE.
|     | ECL | Traffic | Weather | Ettm1 | Ettm2 | Etth1 | Etth2 |
| --- | --- | ------- | ------- | ----- | ----- | ----- | ----- |
Horizon Model
|          | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     |
| -------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| TEMPO    | 0.178/0.276 | 0.476/0.343 | 0.211/0.254 | 0.438/0.424 | 0.185/0.267 | 0.400/0.406 | 0.301/0.353 |
| GPT2     | 0.193/0.288 | 0.522/0.380 | 0.226/0.274 | 0.486/0.438 | 0.193/0.273 | 0.400/0.416 | 0.320/0.363 |
| T5       | 0.185/0.282 | 0.508/0.366 | 0.217/0.271 | 0.529/0.464 | 0.190/0.268 | 0.400/0.409 | 0.328/0.366 |
| PatchTST | 0.489/0.546 | 1.023/0.641 | 0.247/0.301 | 0.733/0.554 | 0.273/0.345 | 0.57/0.518  | 0.379/0.412 |
96 Timesnet 0.293/0.369 0.585/0.401 0.247/0.295 0.518/0.470 0.202/0.290 0.407/0.423 0.315/0.362
| FEDformer | 0.300/0.399 | 0.835/0.564 | 0.292/0.346 | 0.698/0.553 | 0.665/0.634 | 0.509/0.502 | 0.385/0.426 |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.707/0.638 | 1.419/0.795 | 0.453/0.416 | 1.117/0.678 | 0.353/0.404 | 0.469/0.457 | 0.405/0.428 |
| Informer  | 0.512/0.531 | 1.400/0.830 | 0.837/0.711 | 0.880/0.657 | 0.263/0.360 | 0.642/0.562 | 0.704/0.651 |
| DLinear   | 0.195/0.292 | 0.609/0.424 | 0.212/0.275 | 0.624/0.522 | 0.264/0.352 | 0.414/0.421 | 0.334/0.389 |
| TEMPO     | 0.198/0.293 | 0.496/0.355 | 0.254/0.298 | 0.461/0.432 | 0.243/0.304 | 0.426/0.421 | 0.355/0.389 |
| GPT2      | 0.207/0.300 | 0.533/0.387 | 0.273/0.312 | 0.516/0.461 | 0.254/0.312 | 0.441/0.433 | 0.381/0.402 |
| T5        | 0.205/0.302 | 0.524/0.374 | 0.277/0.321 | 0.523/0.454 | 0.246/0.306 | 0.428/0.426 | 0.413/0.410 |
| PatchTST  | 0.465/0.535 | 0.992/0.633 | 0.277/0.324 | 0.739/0.563 | 0.299/0.355 | 0.580/0.528 | 0.387/0.417 |
192 Timesnet 0.283/0.366 0.64/0.431 0.316/0.342 0.55/0.490 0.261/0.318 0.439/0.439 0.394/0.406
| FEDformer | 0.390/0.468 | 0.869/0.579 | 0.372/0.426 | 0.819/0.608 | 0.358/0.416 | 0.683/0.596 | 0.921/0.748 |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.721/0.645 | 0.995/0.658 | 0.545/0.466 | 1.598/0.803 | 0.390/0.416 | 0.548/0.503 | 0.476/0.468 |
| Informer  | 0.625/0.619 | 0.872/0.506 | 0.431/0.455 | 1.461/0.892 | 0.494/0.516 | 0.798/0.632 | 0.455/0.883 |
| DLinear   | 0.204/0.300 | 0.595/0.412 | 0.259/0.308 | 0.599/0.511 | 0.292/0.365 | 0.439/0.437 | 0.381/0.415 |
| TEMPO     | 0.209/0.309 | 0.503/0.356 | 0.292/0.332 | 0.515/0.467 | 0.309/0.345 | 0.441/0.430 | 0.379/0.408 |
| GPT2      | 0.231/0.324 | 0.566/0.421 | 0.441/0.379 | 0.571/0.502 | 0.315/0.35  | 0.449/0.440 | 0.394/0.416 |
| T5        | 0.229/0.321 | 0.550/0.391 | 0.330/0.330 | 0.572/0.504 | 0.316/0.346 | 0.442/0.438 | 0.416/0.427 |
| PatchTST  | 0.531/0.569 | 0.987/0.626 | 0.317/0.347 | 0.755/0.576 | 0.342/0.382 | 0.677/0.573 | 0.386/0.425 |
336 Timesnet 0.733/0.633 1.609/0.864 0.359/0.372 0.638/0.532 0.38/0.392 0.555/0.503 0.384/0.413
| FEDformer | 0.317/0.406 | 1.006/0.640 | 0.639/0.600 | 0.785/0.624 | 0.372/0.424 | 0.582/0.542 | -/5.755     |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.862/0.707 | 0.940/0.621 | 0.487/0.444 | 1.154/0.682 | 0.409/0.428 | 0.728/0.585 | 0.446/0.451 |
| Informer  | 1.222/0.863 | 0.978/0.507 | 0.370/0.412 | 0.949/0.631 | 0.788/0.622 | 1.125/0.810 | 1.389/0.848 |
| DLinear   | 0.231/0.325 | 0.624/0.427 | 0.304/0.342 | 0.622/0.534 | 0.361/0.411 | 0.463/0.464 | 0.471/0.482 |
| TEMPO     | 0.279/0.355 | 0.538/0.376 | 0.370/0.379 | 0.591/0.509 | 0.386/0.395 | 0.443/0.451 | 0.409/0.440 |
| GPT2      | 0.262/0.347 | 0.596/0.399 | 0.484/0.422 | 0.646/0.54  | 0.394/0.397 | 0.445/0.454 | 0.434/0.448 |
| T5        | 0.266/0.351 | 0.578/0.404 | 0.528/0.451 | 0.694/0.568 | 0.394/0.397 | 0.443/0.458 | 0.425/0.440 |
| PatchTST  | 0.475/0.532 | 1.152/0.706 | 0.375/0.388 | 0.739/0.57  | 0.421/0.421 | 0.540/0.521 | 0.425/0.448 |
720 Timesnet 1.166/0.859 1.974/0.971 0.423/0.405 0.723/0.577 0.399/0.409 0.438/0.461 0.394/0.431
| FEDformer | 0.423/0.48  | 0.965/0.652 | 0.409/0.425 | 0.816/0.614 | 0.455/0.462 | 0.688/0.618 | 0.427/0.452 |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.666/0.640 | 0.798/0.518 | 0.592/0.506 | 1.038/0.665 | 0.444/0.438 | 0.615/0.561 | 0.446/0.466 |
| Informer  | 0.881/0.778 | 1.532/0.800 | 1.133/0.842 | 0.779/0.616 | 1.075/0.725 | 0.836/0.687 | 1.330/0.866 |
| DLinear   | 0.259/0.352 | 0.623/0.42  | 0.363/0.389 | 0.639/0.559 | 0.515/0.490 | 0.467/0.481 | 0.639/0.559 |
| TEMPO     | 0.216/0.308 | 0.503/0.358 | 0.282/0.316 | 0.501/0.458 | 0.280/0.328 | 0.428/0.427 | 0.361/0.398 |
| GPT2      | 0.223/0.315 | 0.554/0.397 | 0.356/0.347 | 0.555/0.485 | 0.289/0.333 | 0.436/0.436 | 0.382/0.407 |
| T5        | 0.221/0.314 | 0.540/0.384 | 0.338/0.343 | 0.58/0.498  | 0.287/0.329 | 0.428/0.433 | 0.396/0.411 |
| PatchTST  | 0.49/0.545  | 1.039/0.652 | 0.304/0.340 | 0.741/0.566 | 0.334/0.376 | 0.592/0.535 | 0.394/0.425 |
Avg Timesnet 0.619/0.557 1.202/0.667 0.336/0.354 0.607/0.517 0.311/0.352 0.460/0.457 0.372/0.403
| FEDformer | 0.358/0.439 | 0.919/0.609 | 0.428/0.449 | 0.780/0.600 | 0.463/0.484 | 0.616/0.565 | -/1.845     |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.750/0.664 | 1.038/0.648 | 0.519/0.458 | 1.227/0.707 | 0.399/0.422 | 0.590/0.527 | 0.443/0.453 |
| Informer  | 0.810/0.698 | 1.196/0.661 | 0.693/0.605 | 1.017/0.699 | 0.655/0.556 | 0.850/0.673 | 0.970/0.812 |
| DLinear   | 0.222/0.317 | 0.613/0.421 | 0.284/0.329 | 0.621/0.531 | 0.358/0.405 | 0.446/0.451 | 0.456/0.461 |
LLMwiththewell-designedpromptandimplementingtimeseriesdecompositioncancontribute
significantlytoenhancingtheaccuracyandstabilityofzero-shottimeseriesforecasting.
4.2 SHORT-TERMFORECASTINGWITHCONTEXTUALINFORMATION
Datasetandmetrics. Inthissection,weintroduceTETS,anewbenchmarkdatasetbuiltuponS&P
500datasetcombiningcontextualinformationandtimeseries,tothecommunity. Following (Cao
etal.,2023),wechoosethesymmetricmeanabsolutepercentageerror(SMAPE)asourmetricin
thissection. Moreover,theGDELTisalsousedtoverifytheeffectivenesstheourproposedmethod.
PleaserefertoAppendixB.2andAppendixB.3forthedetaileddatasetsettingofTETSandGDELT;
7

PublishedasaconferencepaperatICLR2024
Table 2: SMAPE results of EBITDA from TETS and GDELT. The result of EBITDA includes
outliersremovedwhereSMAPEexceeds0.8/0.9. Thebestresultsaremarkedinboldandthesecond
optimalinunderlinedrespectivelywith0.8&0.9. (Sectors: CC:ConsumerCyclical;CD:Consumer
Defensive;Ind: Industrials;RE:RealEstate;Events: 11: Disapprove;17: Coerce;19:Fight.)
EBITDADataset
Sectors TEMPO LLaMA GPT2 Bert T5 Informer PatchTST Reformer DLinear
CC 32.27/33.48 33.13/34.31 33.77/35.37 33.42/35.33 32.65/33.83 41.12/43.17 41.44/43.18 37.23/39.09 33.53/35.65
CD 25.9/26.25 26.34/26.62 26.86/27.15 27.34/28.3 26.44/26.79 35.65/36.08 31.6/31.98 29.93/30.36 27.01/28.04
Ind 26.7/27.42 27.17/27.98 27.9/28.63 27.89/28.95 27.3/28.12 34.83/35.87 33.84/34.87 30.23/31.28 27.59/28.84
RE 29.46/30.11 29.63/30.48 30.62/31.21 30.62/31.66 30.1/30.64 36.4/37.22 37.63/38.31 31.23/31.69 29.95/30.92
GDELTDataset
11 38.77 40.23 39.03 38.89 39.04 42.00 40.45 46.72 40.14
17 41.02 42.50 41.20 41.10 41.24 44.44 42.72 48.08 42.45
19 44.03 45.49 44.17 44.09 44.29 47.45 45.49 48.30 45.40
AppendixHfortheproposedpipelineofcollectingTETSdatasetwithbothtimeseriesandtextual
information.
Contextual Information. In order to incorporate the contextual information into our proposed
TEMPO,weleveragethebuilt-intokenizationcapabilitiesofthegenerativepre-trainedtransformerto
deriveembeddingsofinputtext. Then,weutilizethesetextembeddingscorrespondingtoeachtime
seriesinstance,Text,toconstructsoftpromptswithlearnableparametersandconcatenatethematthe
beginningoftheinputembedding,thatis,x=Text⊕x ⊕x ⊕x . Wherethex forEBITDA
T S R ∗
is conducted with semi-soft prompt. This method is not strictly confined to our proposed model
butcanbefeasiblyappliedinsimilarworkstoenhancetheircapabilityofhandlingandbenefiting
fromcontextualinformation. Comparisonswithotherdesignstrategiesofcontextualinformationare
providedintheAppendixD.4forfurtherreference.
Results. Fromthetransferlearningperspective,wechoosetoreportthesettingof‘many-to-many’,
whichmeanswetrainamodelusingin-domainsectorsdataanddirectlydothezero-shottestonall
cross-domainsectors. TheSMAPEresultsofusingdifferentbaselinemodelsandourmodelonthe
TETSdatasetandGDELTdatasetarelistedinTable2whichisalsozero-shotsettingasdatasamples
fromthosesectorsarenotseenduringthetrainingstage. Examiningtheresultsacrossallsectors,our
proposedmodel,whichcombinestimeseriesdatawithsupplementarysummary(contextual)data,
outperformsallthebaselinemethodsincross-domainsectors. Besides,weobservethattransformer-
based architectures training from scratch, specifically tailored for time series analysis—such as
PatchTST,Informer,andReformer(Kitaevetal.,2020)—tendtounderperformincomparisonto
transformers pre-trained on linguistic datasets. This performance discrepancy indicates that the
parameterinitializationderivedfrompre-trainedlanguagemodelsconfersasuperiorstartingpoint
formodeloptimization. Consequently,thesepre-trainedmodelsexhibitenhancedcapabilitiesand
adaptabilitywithinzero-shotlearningcontexts. Furthermore,ininstanceswherethetimeseriesdata
exhibitsastrongcorrelationtoothermodalities,suchastextualinformation,devisinganeffective
strategytoamalgamatethesedistinctmodalitiescouldleadtoenhancedperformancegains.
5 ANALYSIS
5.1 ABLATIONSTUDY
The provided ablation study, Table 3, offers critical insights into the impact of the prompt and
decompositioncomponentsontheperformanceofourmodel. Inthistable,theMSEandMAEon
variousdatasetsarereportedforfourscenarios: theoriginalmodelconfiguration(‘TEMPO’);the
modelwithoutthepromptdesignandwithoutdecomposition,whichisthesettingof‘w/oDec’;the
modelwithoutpromptdesign(‘w/oPro’)andthemodelwithoutthedecompositionlossalignment
(’w/o Dec Loss’). Averagely, the exclusion of the prompt component leads to a deterioration in
themodel’spredictiveaccuracy,indicatingthepromptcanbeanimportantfactorinenhancingthe
model’s overall performance. The omission of decomposition loss typically results in a decline
inmodelperformance. Decompositionlossfacilitatestheuseofaricherhistoricaldataset,which
8

PublishedasaconferencepaperatICLR2024
| TEMPO | w/oDec w/oPro | w/oDecLoss |     |     |     |
| ----- | ------------- | ---------- | --- | --- | --- |
1.0
| MSE/MAE         | MSE/MAE MSE/MAE         | MSE/MAE     |     |     |     |
| --------------- | ----------------------- | ----------- | --- | --- | --- |
| 96 0.178/0.276  | 0.195/0.294 0.185/0.281 | 0.191/0.293 | 0.8 |     |     |
| 192 0.198/0.293 | 0.210/0.301 0.196/0.295 | 0.205/0.305 |     |     |     |
egatnecreP tnenopmoC
| ECL 336 0.209/0.309 | 0.237/0.328 0.225/0.318 | 0.243/0.337 | 0.6 |     |     |
| ------------------- | ----------------------- | ----------- | --- | --- | --- |
| 720 0.279/0.355     | 0.271/0.351 0.269/0.359 | 0.262/0.353 |     |     |     |
| Avg 0.216/0.308     | 0.228/0.319 0.219/0.313 | 0.225/0.322 | 0.4 |     |     |
| 96 0.438/0.424      | 0.516/0.447 0.452/0.431 | 0.428/0.425 |     |     |     |
| 192 0.461/0.432     | 0.518/0.462 0.47/0.45   | 0.494/0.463 | 0.2 |     |     |
Trend Seasonality
| Ettm1 336 0.515/0.467 | 0.622/0.515 0.519/0.474 | 0.544/0.492 | Residual |     |     |
| --------------------- | ----------------------- | ----------- | -------- | --- | --- |
Error
| 720 0.591/0.509 | 0.644/0.50 0.582/0.51 | 0.594/0.521 | 0.0 96 | 192 336 | 720 |
| --------------- | --------------------- | ----------- | ------ | ------- | --- |
Prediction Length
| Avg 0.501/0.458 | 0.575/0.481 0.506/0.466 | 0.515/0.475 |     |     |     |
| --------------- | ----------------------- | ----------- | --- | --- | --- |
Figure2:TheSHAPvaluesofdecomposedcom-
| Table3: | AblationstudyonTEMPO. |     | ponentsofTEMPOforETTm1. |     |     |
| ------- | --------------------- | --- | ----------------------- | --- | --- |
enhances the quality of individual decomposition components. This improvement in component
qualityisimportantforthemodel’sforecastingaccuracy. Notethatemployingthepromptdesign
inisolation,withoutthesupportofdecomposition,candetrimentallyimpactthebackbonemodel’s
performanceinmostcases. Thiscanbeduetothedifficultiesineffectivelypromptingtimeseries
datafromitsrawformwithlimitedsemanticinformation. Thesefindingsunderscoretheessential
natureofbothpromptanddecompositionelementsinachievingrobustforecastingcapabilitiesunder
thezero-shotsetting.
5.2 INTERPRETINGMODELPREDICTIONS
SHAP(SHapleyAdditiveexPlanations)valuesserveasacomprehensivemeasureoffeatureimpor-
tance,quantifyingtheaveragecontributionofeachfeaturetothepredictionoutputacrossallpossible
featurecombinations. AsshowninFigure2,whenappliedtoourseasonalandtrenddecomposition,
theSHAPvaluesfromthegeneralizedadditivemodel(GAM)suggestadominantinfluenceofthe
seasonalcomponentonthemodel’spredictions, implyingasignificantdependencyofthemodel
ontheoverallrecurringpatternswithinthedata. WhilethedirectionalshiftsofETTm1dataset’s
contribution is relatively stable. The escalating values in the ’Error’ column, which denote the
discrepancybetweenthemodel’spredictionsandthegroundtruth,indicateapotentialdeclinein
themodel’saccuracyasthepredictionlengthincreaseswhichisindeedobservedinmostexperi-
mentsrun. Inthiscontext,theSTLdecompositionprovesinvaluableasitenablesustoidentifyand
quantifytheindividualcontributionsofeachcomponenttotheoverallpredictions,asdemonstrated
bytheSHAPvalues. Thisdetailedunderstandingcanyieldcriticalinsightsinhowthepre-trained
transformerisinterpretingandleveragingthedecomposingpre-processingstep,therebyprovidinga
robustfoundationformodeloptimizationandenhancement. SHAPvaluesforweatherdatasetcanbe
foundatFigure14.
6 CONCLUSION
Thispaperproposesasoftpromptbasedgenerativetransformer,TEMPO,whichachievesstate-of-the-
artperformanceinzero-shottimeseriesforecasting.Weintroducethenovelintegrationofpromptsand
seasonaltrenddecompositiontogetherwithinapre-trainedTransformer-basedbackbonetoallowthe
modeltofocusonappropriatelyutilizingknowledgefromdifferenttemporalsemanticscomponents.
Moreover,wedemonstratetheeffectivenessofTEMPOwithmultimodelinput,effectivelyleveraging
contextualinformationintimeseriesforecasting. Lastly,withextensiveexperiments,wehighlight
thesuperiorityofTEMPOinaccuracy,andgeneralizability. Onepotentiallimitationworthfurther
investigationisthatsuperiorLLMswithbetternumericalreasoningcapabilitiesmightyieldbetter
results. Inaddition,theencouragingresultsofTEMPOonthezero-shotexperimentsshedlightinto
effectivefoundationalmodelsfortimeseries.
9

PublishedasaconferencepaperatICLR2024
ACKNOWLEDGEMENT
ThisworkispartiallysupportedbytheNSFAward#2125142andNSFAward#2226087.Thefunding
fromthesesourceshasbeenacornerstoneinenablingustobringourprojecttofruition. Wewould
liketoextendourthankstoYizhouZhang,JamesEnouen,QiangHuang,ChuizhengMeng,andHao
Niufortheirinvaluablediscussionsandinsightsinshapingthedirectionandexecutionofourwork.
Wearealsodeeplygratefultotheanonymousreviewersfortheirrigorousreviewprocess. Their
detailedcommentsandconstructivesuggestionshavesignificantlycontributedtotheimprovementof
thispaper. Thetimeandefforttheyinvestedinprovidingfeedbackhavebeeninvaluableandhave
greatlyassistedusinrefiningourwork.
REFERENCES
ShaojieBai,JZicoKolter,andVladlenKoltun. Anempiricalevaluationofgenericconvolutionaland
recurrentnetworksforsequencemodeling. arXivpreprintarXiv:1803.01271,2018.
TomB.Brown,BenjaminMann,NickRyder,MelanieSubbiah,JaredKaplan,PrafullaDhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss,GretchenKrueger,T.J.Henighan,RewonChild,AdityaRamesh,DanielM.Ziegler,
JeffWu,ClemensWinter,ChristopherHesse,MarkChen,EricSigler,MateuszLitwin,ScottGray,
BenjaminChess,JackClark,ChristopherBerner,SamMcCandlish,AlecRadford,IlyaSutskever,
and Dario Amodei. Language models are few-shot learners. Advances in neural information
processingsystems,abs/2005.14165,2020.
DefuCao,YujingWang,JuanyongDuan,CeZhang,XiaZhu,ConguriHuang,YunhaiTong,Bixiong
Xu,JingBai,JieTong,etal. Spectraltemporalgraphneuralnetworkformultivariatetime-series
forecasting. Advancesinneuralinformationprocessingsystems,2021.
DefuCao,YixiangZheng,ParisaHassanzadeh,SimranLamba,XiaomoLiu,andYanLiu. Large
scalefinancialtimeseriesforecastingwithmulti-facetedmodel. InProceedingsoftheFourthACM
InternationalConferenceonAIinFinance,pp.472–480,2023.
CristianChallu, KinGOlivares, BorisNOreshkin, FedericoGarzaRamirez, MaxMergenthaler
Canseco,andArturDubrawski. Nhits: Neuralhierarchicalinterpolationfortimeseriesforecasting.
InProceedingsoftheAAAIConferenceonArtificialIntelligence,volume37,pp.6989–6997,2023.
ChingChang,Wen-ChihPeng,andTien-FuChen. Llm4ts: Two-stagefine-tuningfortime-series
forecastingwithpre-trainedllms. arXivpreprintarXiv:2308.08469,2023.
RobertBCleveland,WilliamSCleveland,JeanEMcRae,andIrmaTerpenning.Stl:Aseasonal-trend
decomposition. J.Off.Stat,6(1):3–73,1990.
AbhimanyuDas,WeihaoKong,AndrewLeach,RajatSen,andRoseYu. Long-termforecastingwith
tide: Time-seriesdenseencoder. arXivpreprintarXiv:2304.08424,2023a.
AbhimanyuDas,WeihaoKong,RajatSen,andYichenZhou. Adecoder-onlyfoundationmodelfor
time-seriesforecasting. arXivpreprintarXiv:2310.10688,2023b.
JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. BERT:pre-trainingofdeep
bidirectionaltransformersforlanguageunderstanding. InProceedingsofthe2019Conferenceof
theNorthAmericanChapteroftheAssociationforComputationalLinguistics: HumanLanguage
Technologies(NAACL-HLT),Minneapolis,MN,USA,June2-7,2019,pp.4171–4186,2019.
Vijay Ekambaram, Arindam Jati, Nam Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam.
Tsmixer: Lightweight mlp-mixer model for multivariate time series forecasting. In Proceed-
ings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, KDD
’23, pp. 459–469, New York, NY, USA, 2023. Association for Computing Machinery. ISBN
9798400701030. doi: 10.1145/3580305.3599533. URL https://doi.org/10.1145/
3580305.3599533.
WeiFan,ShunZheng,XiaohanYi,WeiCao,YanjieFu,JiangBian,andTie-YanLiu. DEPTS:Deep
expansionlearningforperiodictimeseriesforecasting. InInternationalConferenceonLearning
Representations,2022.
10

PublishedasaconferencepaperatICLR2024
WeiFan,PengyangWang,DongkunWang,DongjieWang,YuanchunZhou,andYanjieFu. Dish-ts:
ageneralparadigmforalleviatingdistributionshiftintimeseriesforecasting. InProceedingsof
theAAAIConferenceonArtificialIntelligence,volume37,pp.7522–7529,2023.
RobertFildes,AndrewHarvey,MikeWest,andJeffHarrison. Forecasting,structuraltimeseries
modelsandthekalmanfilter. TheJournaloftheOperationalResearchSociety,42:1031,111991.
doi: 10.2307/2583225.
AzulGarzaandMaxMergenthaler-Canseco. Timegpt-1. arXivpreprintarXiv:2310.03589,2023.
Mononito Goswami, Konrad Szafer, Arjun Choudhry, Yifu Cai, Shuo Li, and Artur Dubrawski.
Moment: A family of open time-series foundation models. arXiv preprint arXiv:2402.03885,
2024.
NateGruver,MarcFinzi,ShikaiQiu,andAndrewGWilson. Largelanguagemodelsarezero-shot
timeseriesforecasters. AdvancesinNeuralInformationProcessingSystems,36,2024.
TrevorJHastie. Generalizedadditivemodels. InStatisticalmodelsinS,pp.249–307.Routledge,
2017.
EdwardJHu,YelongShen,PhillipWallis,ZeyuanAllen-Zhu,YuanzhiLi,SheanWang,LuWang,
and Weizhu Chen. Lora: Low-rank adaptation of large language models. arXiv preprint
arXiv:2106.09685,2021.
BiweiHuang,KunZhang,JijiZhang,JosephRamsey,RubenSanchez-Romero,ClarkGlymour,and
BernhardScho¨lkopf. Causaldiscoveryfromheterogeneous/nonstationarydata. TheJournalof
MachineLearningResearch,21(1):3482–3534,2020.
RobJHyndmanandYeasminKhandakar. Automatictimeseriesforecasting: theforecastpackage
forr. Journalofstatisticalsoftware,27:1–22,2008.
FurongJia,KevinWang,YixiangZheng,DefuCao,andYanLiu. Gpt4mts: Prompt-basedlarge
languagemodelformultimodaltime-seriesforecasting. InThe14thSymposiumonEducational
AdvancesinArtificialIntelligence(EAAI-24),2024.
Ming Jin, Qingsong Wen, Yuxuan Liang, Chaoli Zhang, Siqiao Xue, Xue Wang, James Zhang,
YiWang,HaifengChen,XiaoliLi,etal. Largemodelsfortimeseriesandspatio-temporaldata: A
surveyandoutlook. arXivpreprintarXiv:2310.10196,2023.
Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y. Zhang, Xiaoming Shi, Pin-Yu Chen,
YuxuanLiang,Yuan-FangLi,ShiruiPan,andQingsongWen. Time-LLM:Timeseriesforecasting
byreprogramminglargelanguagemodels. InTheTwelfthInternationalConferenceonLearning
Representations,2024a. URLhttps://openreview.net/forum?id=Unb5CVPtae.
MingJin,YifanZhang,WeiChen,KexinZhang,YuxuanLiang,BinYang,JindongWang,Shirui
Pan,andQingsongWen. Positionpaper: Whatcanlargelanguagemodelstellusabouttimeseries
analysis. arXivpreprintarXiv:2402.02713,2024b.
Taesung Kim, Jinhee Kim, Yunwon Tae, Cheonbok Park, Jang-Ho Choi, and Jaegul Choo. Re-
versibleinstancenormalizationforaccuratetime-seriesforecastingagainstdistributionshift. In
InternationalConferenceonLearningRepresentations,2022.
NikitaKitaev,LukaszKaiser,andAnselmLevskaya. Reformer: Theefficienttransformer. In8th
InternationalConferenceonLearningRepresentations(ICLR),AddisAbaba,Ethiopia,April26-30,
2020,2020.
BrianLester,RamiAl-Rfou,andNoahConstant. Thepowerofscaleforparameter-efficientprompt
tuning. arXivpreprintarXiv:2104.08691,2021.
JunLi,CheLiu,SiboCheng,RossellaArcucci,andShendaHong. Frozenlanguagemodelhelpsecg
zero-shotlearning,2023.
11

PublishedasaconferencepaperatICLR2024
LiunianHaroldLi,PengchuanZhang,HaotianZhang,JianweiYang,ChunyuanLi,YiwuZhong,
LijuanWang,LuYuan,LeiZhang,Jenq-NengHwang,etal.Groundedlanguage-imagepre-training.
InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition,pp.
10965–10975,2022.
XiangLisaLiandPercyLiang. Prefix-tuning: Optimizingcontinuouspromptsforgeneration. arXiv
preprintarXiv:2101.00190,2021.
YaguangLi,RoseYu,CyrusShahabi,andYanLiu. Diffusionconvolutionalrecurrentneuralnetwork:
Data-driventrafficforecasting. InInternationalConferenceonLearningRepresentations(ICLR
’18),2018.
MinhaoLiu,AilingZeng,MuxiChen,ZhijianXu,QiuxiaLai,LingnaMa,andQiangXu. Scinet:
Timeseriesmodelingandforecastingwithsampleconvolutionandinteraction. AdvancesinNeural
InformationProcessingSystems,35:5816–5828,2022.
Shizhan Liu, Hang Yu, Cong Liao, Jianguo Li, Weiyao Lin, Alex X Liu, and Schahram Dust-
dar. Pyraformer: Low-complexitypyramidalattentionforlong-rangetimeseriesmodelingand
forecasting. InInternationalconferenceonlearningrepresentations,2021.
YongLiu,TenggeHu,HaoranZhang,HaixuWu,ShiyuWang,LintaoMa,andMingshengLong.
itransformer: Inverted transformers are effective for time series forecasting. arXiv preprint
arXiv:2310.06625,2023.
ScottMLundbergandSu-InLee. Aunifiedapproachtointerpretingmodelpredictions. Advancesin
neuralinformationprocessingsystems,30,2017.
YuqiNie,NamH.Nguyen,PhanwadeeSinthong,andJayantKalagnanam. Atimeseriesisworth
64words: Long-termforecastingwithtransformers. InInternationalConferenceonLearning
Representations(ICLR’23),2023.
OpenAI. Gpt-4technicalreport,2023.
BorisNOreshkin,DmitriCarpov,NicolasChapados,andYoshuaBengio. N-beats: Neuralbasis
expansionanalysisforinterpretabletimeseriesforecasting. arXivpreprintarXiv:1905.10437,
2019.
LongOuyang,JeffWu,XuJiang,DiogoAlmeida,CarrollL.Wainwright,PamelaMishkin,Chong
Zhang,SandhiniAgarwal,KatarinaSlama,AlexRay,JohnSchulman,JacobHilton,FraserKelton,
LukeE.Miller, MaddieSimens, AmandaAskell, PeterWelinder, PaulFrancisChristiano, Jan
Leike,andRyanJ.Lowe. Traininglanguagemodelstofollowinstructionswithhumanfeedback.
ArXiv,abs/2203.02155,2022. URLhttps://api.semanticscholar.org/CorpusID:
246426909.
AntonyPapadimitriou,UrjitkumarPatel,LisaKim,GraceBang,AzadehNematzadeh,andXiaomo
Liu. Amulti-facetedapproachtolargescalefinancialforecasting. InProceedingsoftheFirstACM
InternationalConferenceonAIinFinance,pp.1–8,2020.
Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al. Improving language
understandingbygenerativepre-training. 2018.
AlecRadford,JeffreyWu,RewonChild,DavidLuan,DarioAmodei,IlyaSutskever,etal. Language
modelsareunsupervisedmultitasklearners. OpenAIblog,1(8):9,2019.
AlecRadford, JongWookKim, ChrisHallacy, AdityaRamesh, GabrielGoh, SandhiniAgarwal,
GirishSastry,AmandaAskell,PamelaMishkin,JackClark,etal. Learningtransferablevisual
modelsfromnaturallanguagesupervision. InInternationalConferenceonMachineLearning,pp.
8748–8763.PMLR,2021.
ColinRaffel,NoamShazeer,AdamRoberts,KatherineLee,SharanNarang,MichaelMatena,Yanqi
Zhou,WeiLi,andPeterJLiu. Exploringthelimitsoftransferlearningwithaunifiedtext-to-text
transformer. TheJournalofMachineLearningResearch,21(1):5485–5551,2020.
12

PublishedasaconferencepaperatICLR2024
Kashif Rasul, Arjun Ashok, Andrew Robert Williams, Arian Khorasani, George Adamopoulos,
Rishika Bhagwatkar, Marin Bilosˇ, Hena Ghonia, Nadhir Vincent Hassen, Anderson Schnei-
der, et al. Lag-llama: Towards foundation models for time series forecasting. arXiv preprint
arXiv:2310.08278,2023.
TaylorShin,YasamanRazeghi,RobertLLoganIV,EricWallace,andSameerSingh. Autoprompt:
Elicitingknowledgefromlanguagemodelswithautomaticallygeneratedprompts. InProceedings
ofthe2020ConferenceonEmpiricalMethodsinNaturalLanguageProcessing(EMNLP),pp.
4222–4235,2020.
SimaSiami-Namini,NedaTavakoli,andAkbarSiamiNamin. Acomparisonofarimaandlstmin
forecastingtimeseries. In201817thIEEEinternationalconferenceonmachinelearningand
applications(ICMLA),pp.1394–1401.IEEE,2018.
Il’yaMeerovichSobol’. Onsensitivityestimationfornonlinearmathematicalmodels. Matematich-
eskoemodelirovanie,2(1):112–118,1990.
ChenxiSun,YaliangLi,HongyanLi,andShendaHong. Test: Textprototypealignedembeddingto
activatellm’sabilityfortimeseries. arXivpreprintarXiv:2308.08241,2023.
HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-AnneLachaux,Timothe´e
Lacroix,BaptisteRozie`re,NamanGoyal,EricHambro,FaisalAzhar,AurelienRodriguez,Armand
Joulin,EdouardGrave,andGuillaumeLample. Llama: Openandefficientfoundationlanguage
models. ArXiv, abs/2302.13971, 2023. URL https://api.semanticscholar.org/
CorpusID:257219404.
ZifengWang,ZizhaoZhang,SaynaEbrahimi,RuoxiSun,HanZhang,Chen-YuLee,XiaoqiRen,
Guolong Su, Vincent Perot, Jennifer Dy, et al. Dualprompt: Complementary prompting for
rehearsal-free continual learning. In European Conference on Computer Vision, pp. 631–648.
Springer,2022a.
ZifengWang,ZizhaoZhang,Chen-YuLee,HanZhang,RuoxiSun,XiaoqiRen,GuolongSu,Vincent
Perot,JenniferDy,andTomasPfister. Learningtopromptforcontinuallearning. InProceedings
oftheIEEE/CVFConferenceonComputerVisionandPatternRecognition,pp.139–149,2022b.
GeraldWoo,ChenghaoLiu,DoyenSahoo,AkshatKumar,andStevenHoi. Etsformer: Exponential
smoothingtransformersfortime-seriesforecasting. arXivpreprintarXiv:2202.01381,2022.
GeraldWoo, Chenghao Liu, AkshatKumar, Caiming Xiong, Silvio Savarese, andDoyen Sahoo.
Unifiedtrainingofuniversaltimeseriesforecastingtransformers.arXivpreprintarXiv:2402.02592,
2024.
HaixuWu,JiehuiXu,JianminWang,andMingshengLong. Autoformer: Decompositiontransform-
ers with auto-correlation for long-term series forecasting. In Advances in Neural Information
ProcessingSystems(NeurIPS),pp.101–112,2021.
Haixu Wu, Tengge Hu, Yong Liu, Hang Zhou, Jianmin Wang, and Mingsheng Long. Timesnet:
Temporal2d-variationmodelingforgeneraltimeseriesanalysis. InTheEleventhInternational
ConferenceonLearningRepresentations,2023. URLhttps://openreview.net/forum?
id=ju_Uqw384Oq.
HaoXueandFloraDSalim. Promptcast: Anewprompt-basedlearningparadigmfortimeseries
forecasting. IEEETransactionsonKnowledgeandDataEngineering,2023.
XinliYu,ZhengChen,YuanLing,ShujingDong,ZongyiLiu,andYanbinLu. Temporaldatameets
llm–explainablefinancialtimeseriesforecasting. arXivpreprintarXiv:2306.11025,2023.
Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu. Are transformers effective for time series
forecasting? InProceedingsoftheAAAIConferenceonArtificialIntelligence,2023.
HaotianZhang,PengchuanZhang,XiaoweiHu,Yen-ChunChen,LiunianLi,XiyangDai,Lijuan
Wang,LuYuan,Jenq-NengHwang,andJianfengGao. Glipv2: Unifyinglocalizationandvision-
languageunderstanding. AdvancesinNeuralInformationProcessingSystems,35:36067–36080,
2022a.
13

PublishedasaconferencepaperatICLR2024
TianpingZhang,YizhuoZhang,WeiCao,JiangBian,XiaohanYi,ShunZheng,andJianLi. Lessis
more: Fastmultivariatetimeseriesforecastingwithlightsampling-orientedmlpstructures. arXiv
preprintarXiv:2207.01186,2022b.
XiangZhang,ZiyuanZhao,TheodorosTsiligkaridis,andMarinkaZitnik. Self-supervisedcontrastive
pre-training for time series via time-frequency consistency. Advances in Neural Information
ProcessingSystems,35:3988–4003,2022c.
YizhouZhang,LunDu,DefuCao,QiangFu,andYanLiu. Guidinglargelanguagemodelswith
divide-and-conquerprogramfordiscerningproblemsolving. arXivpreprintarXiv:2402.05359,
2024.
YunhaoZhangandJunchiYan. Crossformer: Transformerutilizingcross-dimensiondependency
formultivariatetimeseriesforecasting. InTheEleventhInternationalConferenceonLearning
Representations,2022.
HaoyiZhou,ShanghangZhang,JieqiPeng,ShuaiZhang,JianxinLi,HuiXiong,andWancaiZhang.
Informer: Beyondefficienttransformerforlongsequencetime-seriesforecasting. InProceedings
ofAAAI,2021.
TianZhou,ZiqingMa,QingsongWen,XueWang,LiangSun,andRongJin. FEDformer: Frequency
enhanceddecomposedtransformerforlong-termseriesforecasting. InProc.39thInternational
ConferenceonMachineLearning(ICML2022),2022.
TianZhou,PeisongNiu,XueWang,LiangSun,andRongJin. Onefitsall: Powergeneraltimeseries
analysisbypretrainedlm. Advancesinneuralinformationprocessingsystems,2023.
14

PublishedasaconferencepaperatICLR2024
A SHOWCASES
A.1 COMPAREWITHGPT4TS
InFigure3,4,5,6,7,weplotthecomparisonofthepredictedvaluefromourmodelandGPT4TS
modelgivenalook-backwindow. Asshowninthedatasets,weareabletopredictclosetotheground
truth,whichisalsoshownthroughoursuperiorperformanceoverothermodelsintable1. Weselect
time series with different characteristics under different prediction lengths O ∈ {96,192}: time
serieswithhighvariability(Figure5a),periodic(Figure3a,Figure3b,4a,4b),non-periodicwith
achangeintrend(Figure6a,Figure6b)
| 1                        |       |     | 1                         |                   |             |
| ------------------------ | ----- | --- | ------------------------- | ----------------- | ----------- |
| 0                        |       |     | 0                         |                   |             |
| 1                        |       |     | 1                         |                   |             |
| 2                        |       |     | 2                         |                   |             |
| 3                        |       |     | 3                         |                   |             |
| GroundTruth              |       |     |                           | GroundTruth       |             |
| 4                        |       |     | 4                         |                   |             |
| GPT4TS Prediction        |       |     |                           | GPT4TS Prediction |             |
| Ours Prediction          |       |     |                           | Ours Prediction   |             |
| 0 20                     | 40 60 | 80  | 0 25 50                   | 75 100 125        | 150 175 200 |
| (a) predictionlengthO=96 |       |     | (b) predictionlengthO=192 |                   |             |
Figure3: Visualizationoflong-termforecastingresults. ComparedbetweenourmodelTEMPOand
GPT4TSonETTh1dataset
| 1.0 |     |     | 0.50 |     |     |
| --- | --- | --- | ---- | --- | --- |
| 0.5 |     |     | 0.25 |     |     |
0.00
0.0
0.25
0.5
0.50
1.0
|     |     |     | 0.75 |     | GroundTruth |
| --- | --- | --- | ---- | --- | ----------- |
1.5 GroundTruth
| GPT4TS Prediction |     |     |      |     | GPT4TS Prediction |
| ----------------- | --- | --- | ---- | --- | ----------------- |
|                   |     |     | 1.00 |     | Ours Prediction   |
Ours Prediction
| 0 20 | 40 60 | 80  | 0 25 | 50 75 100 | 125 150 175 200 |
| ---- | ----- | --- | ---- | --------- | --------------- |
(b) predictionlengthO=192
(a) predictionlengthO=96
Figure4: Visualizationoflong-termforecastingresults. ComparedbetweenourmodelTEMPOand
GPT4TSonETTh2dataset
A.2 COMPAREWITHTIMEGPT
We also compare our results with TimeGPT (Garza & Mergenthaler-Canseco, 2023), which is
capableofgeneratingaccuratepredictionsforadiverserangeofdatasetsnotseenduringtraining,
demonstratingsuperiorperformanceinzero-shotinferencecomparedtotraditionalstatistical,machine
learning,anddeeplearningmethods. AccesstoTimeGPT-1(Beta)isprovidedthroughaPython
SDKandaRESTAPI.ThisaccessibilityallowsustoexploreTimeGPT’sforecastingcapabilitieson
ourdatasets. AsshowninFigure8andFigure9,despiteitsdesignforvariousdownstreamtasks,it
15

PublishedasaconferencepaperatICLR2024
2
2
1
1
0
0
1
1
2
2
| GroundTruth       |       |     | GroundTruth       |        |                 |
| ----------------- | ----- | --- | ----------------- | ------ | --------------- |
| 3                 |       |     | 3                 |        |                 |
| GPT4TS Prediction |       |     | GPT4TS Prediction |        |                 |
| Ours Prediction   |       |     | Ours Prediction   |        |                 |
| 0 20              | 40 60 | 80  | 0 25 50           | 75 100 | 125 150 175 200 |
(b) predictionlengthO=192
| (a) predictionlengthO=96 |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- |
Figure5: Visualizationoflong-termforecastingresults. ComparedbetweenourmodelTEMPOand
GPT4TSonETTm1dataset
0.4
GroundTruth
0.2
| 0.2 |     |     | GPT4TS Prediction |     |     |
| --- | --- | --- | ----------------- | --- | --- |
Ours Prediction
| 0.0 |     |     | 0.4 |     |     |
| --- | --- | --- | --- | --- | --- |
| 0.2 |     |     | 0.6 |     |     |
0.4
0.8
0.6
1.0
0.8
1.2
1.0
GroundTruth
| 1.2 GPT4TS Prediction |     |     | 1.4 |     |     |
| --------------------- | --- | --- | --- | --- | --- |
Ours Prediction
|                          |       |     | 0 25                      | 50 75 100 | 125 150 175 200 |
| ------------------------ | ----- | --- | ------------------------- | --------- | --------------- |
| 0 20                     | 40 60 | 80  |                           |           |                 |
| (a) predictionlengthO=96 |       |     | (b) predictionlengthO=192 |           |                 |
Figure6: Visualizationoflong-termforecastingresults. ComparedbetweenourmodelTEMPOand
GPT4TSonETTm2dataset
| 0.375 |     |     | 1.2 |     | GroundTruth |
| ----- | --- | --- | --- | --- | ----------- |
GPT4TS Prediction
| 0.400 |     |     |     |     | Ours Prediction |
| ----- | --- | --- | --- | --- | --------------- |
1.0
0.425
| 0.450 |     |     | 0.8 |     |     |
| ----- | --- | --- | --- | --- | --- |
0.475
0.6
0.500
| 0.525 |     |     | 0.4 |     |     |
| ----- | --- | --- | --- | --- | --- |
GroundTruth
0.550 GPT4TS Prediction
| Ours Prediction |     |     | 0.2 |     |     |
| --------------- | --- | --- | --- | --- | --- |
0.575
| 0 20                     | 40 60 | 80  | 0 25 50 | 75 100 | 125 150 175 200 |
| ------------------------ | ----- | --- | ------- | ------ | --------------- |
| (a) predictionlengthO=96 |       |     |         |        |                 |
(b) predictionlengthO=192
Figure7: Visualizationoflong-termforecastingresultsonweatherdataset. Comparedbetweenour
modelTEMPOandGPT4TSonweatherdataset
16

PublishedasaconferencepaperatICLR2024
GroundTruth 2
| 2   |     |     | TimeGPT Prediction |     |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
GPT4TS Prediction 1
| 1   |     |     | Ours Prediction |     |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| 0   |     |     |                 | 0   |     |     |     |     |     |
| 1   |     |     |                 | 1   |     |     |     |     |     |
| 2   |     |     |                 | 2   |     |     |     |     |     |
GroundTruth
|     |     |     |     | T i | m e G P T  P re d i c t io n |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
| 3   |     |     |     | 3 G | P T 4 T S  P re d ic t i o n |     |     |     |     |
Ours Prediction
0 0 3 0 0 0 3 0 0 0 3 0 0 0 3 0 0 0 3 0 0 0 3 0 0 0 3 0 0 0 -08 14:30 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -09 13:00
02-07 16: -07 17: -07 19: -07 20: -07 22: -07 23: -08 01: -08 02: -08 04: -08 05: -08 07: -08 08: -08 10: -08 11: -08 13: 02-07 16: -07 19: -07 22: -08 01: -08 04: -08 07: -08 10: -08 13: -08 16: -08 19: -08 22: -09 01: -09 04: -09 07: -09 10:
| 2 2 | 2 2 2 2 2                | 2 2 2 2 2 | 2 2 2 | 2   | 2 2 2 | 2 2                   | 2 2 2 | 2 2   | 2 2 2 2 |
| --- | ------------------------ | --------- | ----- | --- | ----- | --------------------- | ----- | ----- | ------- |
| 0 0 | 0 0 0 0 0                | 0 0 0 0 0 | 0 0 0 | 0   | 0 0 0 | 0 0                   | 0 0 0 | 0 0 0 | 0 0 0   |
|     | (a) predictionlengthO=96 |           |       |     | (b)   | predictionlengthO=192 |       |       |         |
Figure8: Visualizationoflong-termforecastingresultsonETTm1dataset. Comparedbetweenour
modelTEMPOandTimeGPTonweatherdataset
| 1.0 GroundTruth     |                 |     |     |     | GroundTruth                    |     |     |     |     |
| ------------------- | --------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
| T i m e G P T  P    | re d i c t io n |     |     | 0.5 | T i m e G P T  P re d i c t io | n   |     |     |     |
| G P T 4 T S  P re   | d ic t i o n    |     |     |     | G P T 4 T S  P re d ic t i o n |     |     |     |     |
| 0.5 Ours Prediction |                 |     |     |     | Ours Prediction                |     |     |     |     |
0.0
0.0
0.5
0.5
1.0
1.0
1.5
11-25 14: 3 0 -25 16: 0 0 -25 17: 3 0 -25 19: 0 0 -25 20: 3 0 -25 22: 0 0 -25 23: 3 0 -26 01: 0 0 -26 02: 3 0 -26 04: 0 0 -26 05: 3 0 -26 07: 0 0 -26 08: 3 0 -26 10: 0 0 -26 11: 3 0 -26 13:00 12-01 14: 3 0 -01 17: 3 0 -01 20: 3 0 -01 23: 3 0 -02 02: 3 0 -02 05: 3 0 -02 08: 3 0 -02 11: 3 0 -02 14: 3 0 -02 17: 3 0 -02 20: 3 0 -02 23: 3 0 -03 02: 3 0 -03 05: 3 0 -03 08: 3 0 -03 11:30
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
|     | (a) predictionlengthO=96 |     |     |     | (b) | predictionlengthO=192 |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --------------------- | --- | --- | --- |
Figure9: Visualizationoflong-termforecastingresultsonETTm2dataset. Comparedbetweenour
modelTEMPOandTimeGPTonweatherdataset
isimportanttonotethatTimeGPTmaynotperformaswellinlong-termforecastingscenarios. In
contrast,ourproposedmodelexcelsinzero-shotsettings,includinglong-termforecasting,illustrating
theneedforfoundationmodelsthatcanadapttoboththebreadthoftimeseriesapplicationsandthe
depthofforecastinghorizons.
| B EXPERIMENT | SETTING |     |     |     |     |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
B.1 TOWARDSFOUNDATIONMODELEXPERIMENTSDETAILS
|     |     |     |     |     | It  | has been | well-established |     | that |
| --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ---- |
channel-independenceworkswellfor
| Table4: | Datasetdetailsofbenchmarkdataset. |     |     |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
timeseriesdatasets,sowetreateach
multivariatetimeseriesasmultiplein-
|             |        |            |                |     | dependentunivariatetimeseries. |         |          |        | We           |
| ----------- | ------ | ---------- | -------------- | --- | ------------------------------ | ------- | -------- | ------ | ------------ |
| Dataset     | Length | Covariates | SamplingPeriod |     |                                |         |          |        |              |
|             |        |            |                |     | use                            | popular | time     | series | benchmark    |
| ETTh        | 17420  | 7          | 1hour          |     | datasets(Zhouetal.,2021):      |         |          |        | ETTm1,       |
| ETTm        | 69680  | 7          | 15min          |     | ETTm2,                         | ETTh1,  |          | ETTh2, | Weather,     |
| Weather     | 52696  | 22         | 10min          |     |                                |         |          |        |              |
|             |        |            |                |     | Electricity,                   |         | Traffic, | ILI    | and exchnge. |
| Electricity | 26304  | 321        | 1hour          |     |                                |         |          |        |              |
|             |        |            |                |     | 1)ETTm1,                       |         | ETTm2,   | ETTh1, | ETTh2        |
| Traffic     | 17544  | 862        | 1hour          |     |                                |         |          |        |              |
containelectricityloadfromtwoelec-
tricitystationsat15minutesleveland
hourlylevel. 2)Weatherdatasetcontains21meteorologicalindicatorsofGermanywithin1year;3)
Electricitydatasetcontainselectricityconsumption;4)Trafficdatasetcontainstheoccupationrate
ofthefreewaysystemacrosstheStateofCalifornia. ThelookbackwindowLisfollowing (Zhou
etal.,2023),andthepredictionlengthOissetto{96,192,336,720}. Inthisexperimentpart,our
experimentswereconductedusingsingleNVIDIAA100GPU,withabatchsizesetto256, and
focused on long-term forecasting by employing a Mean Squared Error (MSE) loss function. To
17

PublishedasaconferencepaperatICLR2024
ensurethereliabilityofourresults,weperformedthreeiterativeloopsandcalculatedtheaverageof
theoutcomes. Ourexplorationcovered[3,6]GPTlayersandtestedvariousweights,[0.001,0.01,
and1],fortheMSElossfunctionappliedtothereconstructedcomponentsofthetimeseries. We
havedocumentedtheoptimalresultsobtainedfromthissearch. Acomprehensiveanalysisofthe
impactthatthenumberofGPTlayershasontheperformancewillbeaddressedinfutureresearch.
TowardsFoundationModel’sZeroShotSetting Foreachpredictionlength,wetrainamodelon
amixtureoftrainingdatafromdifferentdomainsandtestthemodelonthetargetunseendomain’s
data. Weconstructthecombinedtrainingdatasetbypoolingthetrainingdataandfullyshufflinge
them. Topreventunduebiasandensurefairrepresentationofdatafromeachdomaininthecombined
training data, we select an equal number of training examples from each domain’s training data.
We noted that the number of training samples that ETTh1 and ETTh2 has is on a much smaller
magnitudecomparedtotheotherthreetrainingdatasets(ETTm1,Weather,Electricity),soselecting
theminimumnumberoftrainingsamplesamongallothertrainingdatasetswouldresultintoomuch
datalossfromETTm1,Weather,andElectricity,etc. Therefore,weincludedalltrainingexamples
fromETTh1andETTh2inthecombinedtrainingdataset. Similartotraditionalexperimentalsettings,
eachtimeseries(ETTh1,ETTh2,ETTm1,Weather,Electricity,ETTm2,Traffic)issplitintothree
parts: trainingdata,validationdata,andtestdatafollowingin7:1:2ratioin (Zhouetal.,2022),and
weonlymergethetrainingandvalidationdata. ForETTm1,ETTm2,WeatherandElectricitydata,
thenumberofexamplessampledtobepooledintothecombinedtrainingdatasetischosentobethe
minimumnumberoftrainingexamplesamongthesetrainingdatasets.
B.2 PROPOSEDTETSDATASETSETTING
Prompt:
Suppose you are living in {Year: 2000}, can you help me summarize the news and reports in {Year:
2000}’s {quarter: second quarter} for {company name: Company A}, which is an {company sector:
Technology} company. Please directly give me the answer limited to 2 sentences without apology.
GPT Response:
Description:

In the second quarter of 2000, Company A reported a net profit of $233 million, up from $123 million
in the same quarter of the previous year, driven by strong sales of its X computers and Products Y.
However, the company's stock price dropped after warning that its third-quarter profits would be
below expectations due to slower sales.
Figure10: ExamplefordesigningpromptsusingOPENAIChatGPT-3.5API.
DataCollection Ourtimeseriesdataforfinancialanalysisandforecastingarederivedprimarily
fromthefinancialstatementsofcompaniesincludingbalancesheets,incomestatements,andcash
flowstatements. Specifically,weutilizedatafromthe500largestU.S.companiesacross11sectorsas
listedintheStandard&Poor’s500Index(S&P500),whichwedivideintotwoparts: thefirstseven
sectorsfortrainingandevaluation,andtheremainingfourforzero-shotforecastingtaskstotestthe
model’sabilitytopredictinunseendomains. Whilecollectingcorrespondingcontextualinformation
fromtheabundanceofdigitalnewssourcesischallenging,OpenAI’sChatGPTAPIoffersasolution
togatherandcondenserelevantnewsefficiently. ByinputtingkeydetailsintotheAPIandlimiting
theresponseto110tokens,asshowninFigure10,wecanswiftlyextractpertinentcontextualdatato
improveouranalysis. PleaserefertoSectionHforfurtherdetailsofcreatingTETSdataset.
Predictionobjective TheprimaryobjectiveofourexperimentistoforecasttheEarningsBefore
Interest, Taxes, Depreciation and Amortization(EBITDA) for companies listed in S&P500, and
ourdatarangefrom2000to2022. Followingthemultivariatetimeseriesframeworkpresentedin
(Papadimitriouetal.,2020),weselectfoundationalfinancialmetricsfromtheincomestatementsas
inputfeatures: costofgoodssold(COGS),selling,generalandadministrativeexpenses(SG&A),RD
expenses(RD EXP),EBITDA,andRevenue. Comparingwithothermetrics,theselectedmetrics
containinformationmorerelevanttoourpredictionobjective. ForLargeLanguagebasedmodels,
18

PublishedasaconferencepaperatICLR2024
includingourmodelTEMPO,GPT4TS,andT5,weapplychannel-independencestrategytoperform
univariatetimeseriesforecastingtasks. Allfivefeaturesareusedfortraining(predictingitsfuture
valuebasedonitspastvalue), whileonlyEBITDAisaccessibleduringthetrainingstage. Other
modelsfollowthemultivariatetimeseriesforecastingsetting,treatingthefivefeaturesasmultivariate
inputandpredictingthetarget,EBITDA,bothinthetrainingandtestingstages.
WepredictquarterlyEBITDAbasedonthepast20quarters’data. Thispredictedvalueisthenused
toforecastthenextquarter’sEBITDA,iterativelyfourtimes,leadingtoayearlyprediction. Inorder
tomeasuretheaccuracyofthesepredictionsbasedonthecumulativeyearlyvalue(sumof4quarters),
weemploythesymmetricmeanabsolutepercentageerror(SMAPE)astheevaluationmetricaswell
astheforecastinglossfunctioninthisexperimentalpart.
Data Split For companies under each sector, we employ the windowing method to generate
cohesivetrainingandtestinginstances. Underthechannel-independencesettingwhereweseparate
eachfeaturetoobtainunivariatetimeseries,weget80,600samplesfromthesevenin-domainsectors,
and 9,199 samples from the four zero-shot sectors(also known as cross-domain sectors), five as
muchaswegetinthechanneldependentsetting. Thesectorssplittingiselaboratedin H.Inour
experimentsshownintable2,Weuse70%ofin-domaindatafortraining,10%ofin-domaindatafor
evaluation,andallzero-shotdataforunseentesting.
SymmetricMeanAbsolutePercentageError Inreality,themagnitudeoffinancialmetricscan
varysignificantlyamongdifferentcompanies.So,wechoosethesymmetricmeanabsolutepercentage
error(SMAPE),apercentage-basedaccuracymeasure,asourevaluationmetric. ForEBITDA,there
aremanynegativeresultsthatmayinfluencethefinalSMAPE.WeusetheformofSMAPE-Abs
SMAPE:
n
AbsSMAPE=
200%(cid:88) |F
t
−A
t
|
, (4)
n |F |+|A |
t t
t=1
Here,F representsthetruevalue,A representsthepredictedvalueinoursystem,andnrepresents
t t
thetotaltimestepsweneedtoforecast.
SMAPEcanbeparticularlysensitivetooutliers. Specifically,whenthetruedataandpredictionhave
oppositesigns,theresultingerrormaybeupto200%,seriouslydistortingthefinalresults. Following
theapproachin(Papadimitriouetal.,2020),wefilteroutdatapointsatthe80%and90%thresholds
andfindmostoftheoutliersarerelatedtosignificantfinancialshiftsduetomergers&acquisitions
(M&A).
B.3 GDELTDATASETSETTING
We utilized the GDELT dataset (Jia et al., 2024), which focuses on predicting the respective
mentions and mentions in the news media. We utilized the data collected from the 55 regions
under the US and the national data for the US and divided the 10 event root types in the dataset
into unseen and seen sets, as demonstrated in Table 5. We focused on predicting the three key
variablesNumMentions,NumArticles,NumSourcesrelatedtotheparticulareventtypewithinagiven
timeframeandgeographicalregion. Weapplychannel-independencestrategytoperformunivariate
timeseriesforecastingtsksforallbaselinemodelsandourmodel. Allthreefeaturesareusedfor
trainingandevaluation(predictingitsfuturevaluebasedonitspastvalue).
Wepredictthefuture7daysbasedonthepast15days’datadirectly. Inothertomeasuretheaccuracy
of the predicitions, we use mean square error (MSE) and mean absolute error (MAE). For each
region,weemploythewindowingmethodtogeneratecohesivetrainingandtestinginstancesfor
eacheventroottype. Underourchannel-independencesetting,weget122,008samplesfromthe
sevenin-domainsectors(seensectors)fortraining,and76,048samplesforevaluatingunderthethree
zero-shotsectors(unseensectors). Inourexperiments,weuse70%ofin-domaindatafortraining,
10%forevaluationandallzero-shotdataforunseentesting.
19

PublishedasaconferencepaperatICLR2024
| EventNumber   | EventTypeName               |         |
| ------------- | --------------------------- | ------- |
|               | 01 MakePublicStatement      |         |
|               | 02                          | Appeal  |
|               | 03 ExpressIntenttoCooperate |         |
| TrainingEvent | 04                          | Consult |
05 EngageinDiplomaticCooperation
|           | 07  | ProvideAid |
| --------- | --- | ---------- |
|           | 08  | Yield      |
|           | 11  | Disapprove |
| TestEvent | 17  | Coerce     |
|           | 19  | Fight      |
Table5: EventnumbertoeventtypeNametable
C FURTHER RESULTS
C.1 SELF-SUPERVISEDREPRESENTATIONLEARNING
Ourproposedmodelarchitecturecanbedesignedtosupportself-supervisedlearningandthusfurther
embracefoundationmodelsfortimeseries. Following (Nieetal.,2023),wemaskarandomsubset
ofpatchesbyreplacingthemwithzeros,wherethepatchesaredividedintonon-overlappingpatches
forsimplicityandtoavoidmaskedpatchesinfluencingpredictions. Thepredictionheadisremoved
andreplacedwithalinearlayertoreconstructthemaskedpatches. Themodelistrainedtominimize
theMSEbetweenthepredictedandtruemaskedpatches. Tohandlemultivariatetimeserieswith
varyingnumbersoffeatures,weapplychannelindependence(Zengetal.,2023)tomodeleachtime
seriesindependently.
WiththestrongperformanceTEMPOshowedundertheexperiment’many-to-one’zero-shotsetting,
fromtheperspectiveofaself-supervisedcross-domainfoundationalmodel,wefurtherinvestigateif
usingaTEMPOmodeltrainedondatasetsacrossdomainscanstillachievecomparableperformance
onunseendomains. Here,westillusethe’many-to-one’settingbutthemodelistrainedinaself-
supervisedmanner. Specifically,wefirstuseallotherdomain’sdatatotrainarepresentationmodel
thenonlyuse5%dataofthetrainingdatatofineturnthetotalmodelwiththepredictionlayerasa
forecastingdownstreamtask. Table6providesacomprehensivecomparisonofourmodelagainst
otherbaselinemodelsonthreemultivariatetimeseriesdatasetsthatareunseenbythemodelsduring
training,namelyelectricityandtrafficandweather.Alltheseselected3datasetsareentirelydissimilar
toanydatathemodelhasencounteredbefore. TEMPOoutperformsbaselinemodels,achievingthe
lowest MSE and MAE in most cases. Note that TEMPO’s average MSE and MAE is 7.3% and
4.6%lessthanthebest-performingbaselinemodel(GPT2)fortheweatherdataset,respectively. This
findingshedlightonthestronggeneralizabilityofTEMPOandindicateditspotentialofservingasa
foundationaltimeseriesforecastingmodel,maintainingrobustperformanceforunseendomains.
C.2 COMPARINGWITHFULL-SHOTSTATE-OF-THE-ARTSBASELINES
Towardsfoundationmodeltrainingdifferssignificantlyfromtheone-to-one/manyscenarios,where
pre-traininginvolvesahomogenousdataset,oftenwithconsistentseasonpatterns,samplingrates,
andtemporalscales. Thishomogeneityfacilitatespatternlearningtransferabletofine-tuneddatasets.
Incontrast,towardsfoundationmodeltraininginvolvespre-trainingonhighlydiversedatasets,such
as merging traffic and weather data, which may hinder the model’s ability to discern underlying
patterns. InTable7,weprovidefurtherresultsonETTh1andETTh2datasets,demonstratingthat
theperformanceofTEMPO(zero-shotsetting)surpassesthatofstate-of-the-artmodelsspecifically
designedforthesetargetdatasetswithfull-shotsettings. TheresultsinTable7areobtainedfrom
(Liuetal.,2023),includingbutnotlimitedtoiTransformer(Liuetal.,2023),Crossformer(Zhang&
Yan,2022),TiDE(Dasetal.,2023a)andSCINet(Liuetal.,2022),whicharealsoreportedinour
contemporaneouswork,MOIRAI(Wooetal.,2024).
20

PublishedasaconferencepaperatICLR2024
Table6: Self-supervisedrepresentationlearningresultsarefine-tunedon5%in-domaindatasets. We
usepredictionlengthO ∈{96,192,336,720}. AlowerMSEindicatesbetterperformance,andthe
bestresultsareinbold.
|         | TEMPO           | GPT4TS      | T54TS       | Bert4TS     | PatchTST    |
| ------- | --------------- | ----------- | ----------- | ----------- | ----------- |
|         | MSE/MAE         | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     |
|         | 96 0.19/0.29    | 0.202/0.301 | 0.199/0.293 | 0.202/0.298 | 0.21/0.308  |
|         | 192 0.211/0.31  | 0.217/0.313 | 0.238/0.337 | 0.227/0.321 | 0.223/0.312 |
| ECL     | 336 0.229/0.323 | 0.258/0.353 | 0.273/0.364 | 0.256/0.345 | 0.282/0.357 |
|         | 720 0.375/0.444 | 0.43/0.475  | 0.455/0.49  | 0.442/0.479 | 0.606/0.561 |
|         | Avg 0.251/0.342 | 0.277/0.361 | 0.291/0.371 | 0.282/0.361 | 0.33/0.385  |
|         | 96 0.56/0.411   | 0.607/0.417 | 0.543/0.408 | 0.591/0.423 | 0.577/0.403 |
|         | 192 0.575/0.419 | 0.603/0.421 | 0.594/0.431 | 0.613/0.432 | 0.596/0.411 |
| Traffic | 336 0.597/0.433 | 0.63/0.435  | 0.659/0.458 | 0.639/0.445 | 0.665/0.454 |
|         | 720 0.65/0.452  | 0.643/0.439 | 0.69/0.49   | 0.744/0.496 | 0.802/0.501 |
|         | Avg 0.595/0.429 | 0.621/0.428 | 0.622/0.447 | 0.647/0.449 | 0.66/0.442  |
|         | 96 0.217/0.268  | 0.288/0.31  | 0.252/0.288 | 0.237/0.288 | 0.249/0.285 |
|         | 192 0.265/0.302 | 0.305/0.331 | 0.322/0.336 | 0.291/0.323 | 0.277/0.314 |
| Weather | 336 0.322/0.342 | 0.338/0.353 | 0.346/0.358 | 0.335/0.354 | 0.311/0.341 |
|         | 720 0.41/0.397  | 0.381/0.377 | 0.444/0.42  | 0.466/0.436 | 0.385/0.386 |
|         | Avg 0.304/0.327 | 0.328/0.343 | 0.341/0.351 | 0.332/0.35  | 0.305/0.331 |
Table7: ResultsoflongtermforecastingexperimentsonETTh1andETTh2. Thebestresultsare
markedinboldandthesecondoptimalinunderlined,respectivelywithMSE/MAE.Notethatthe
TEMPOisunderzero-shotsettingandothermodelsareunderfull-shotsetting.
TEMPO iTransformer TimesNet PatchTST Crossformer TiDE DLinear SCINet FEDformer
MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE
96 0.400/0.406 0.386/0.405 0.384/0.402 0.414/0.419 0.423/0.448 0.479/0.464 0.386/0.400 0.654/0.599 0.376/0.419
192 0.426/0.421 0.441/0.436 0.436/0.429 0.460/0.445 0.471/0.474 0.525/0.492 0.437/0.432 0.719/0.631 0.420/0.448
1hTTE
336 0.441/0.430 0.487/0.458 0.491/0.469 0.501/0.466 0.570/0.546 0.565/0.515 0.481/0.459 0.778/0.659 0.459/0.465
720 0.443/0.451 0.503/0.491 0.521/0.500 0.500/0.488 0.653/0.621 0.594/0.558 0.519/0.516 0.836/0.699 0.506/0.507
Avg. 0.428/0.427 0.454/0.447 0.458/0.450 0.469/0.454 0.529/0.522 0.541/0.507 0.456/0.452 0.747/0.647 0.440/0.460
96 0.301/0.351 0.297/0.349 0.340/0.374 0.302/0.348 0.745/0.584 0.400/0.440 0.333/0.387 0.707/0.621 0.358/0.397
192 0.355/0.389 0.380/0.400 0.402/0.414 0.388/0.400 0.877/0.656 0.528/0.509 0.477/0.476 0.860/0.689 0.429/0.439
2hTTE
336 0.379/0.408 0.428/0.432 0.452/0.541 0.426/0.433 1.043/0.731 0.643/0.571 0.594/0.541 1.000/0.744 0.496/0.487
0.409/0.440
720 0.427/0.445 0.462/0.657 0.431/0.446 1.104/0.763 0.874/0.679 0.831/0.657 1.249/0.838 0.463/0.474
Avg. 0.361/0.398 0.383/0.407 0.414/0.427 0.387/0.407 0.942/0.684 0.611/0.550 0.559/0.515 0.954/0.723 0.437/0.449
21

PublishedasaconferencepaperatICLR2024
Table8: ComparetheresultswithARIMA.
ECL Traffic Weather Ettm2
TEMPO ARIMA TEMPO ARIMA TEMPO ARIMA TEMPO ARIMA
MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE
96 0.178/0.276 1.220/0.814 0.476/0.343 1.997/0.924 0.211/0.254 0.217/0.258 0.185/0.267 0.225/0.301
192 0.198/0.293 1.264/0.842 0.496/0.355 2.044/0.944 0.254/0.298 0.263/0.299 0.243/0.304 0.298/0.345
336 0.209/0.309 1.311/0.866 0.503/0.356 2.096/0.960 0.292/0.332 0.330/0.347 0.309/0.345 0.370/0.386
720 0.279/0.355 1.364/0.891 0.538/0.376 2.138/0.971 0.393/0.387 0.425/0.405 0.386/0.395 0.478/0.445
Avg. 0.216/0.308 1.290/0.853 0.503/0.357 2.069/0.950 0.287/0.318 0.309/0.327 0.280/0.328 0.343/0.369
C.3 COMPARINGWITHARIMA
Asapioneeringfoundationmodel,TEMPOisengineeredtoforecastfuturevaluesdirectly,eliminating
thenecessityforretrainingwitheachnewdatainstance. Itsunderlyingframeworkcapturesintricate
temporalpatterns,grantingittheversatilitytogeneralizeacrossvarioustimeseries. Inthisstudy,we
compareTEMPO’sforecastingprowesswiththatoftheARIMAmodel(Hyndman&Khandakar,
2008), which is renowned for its capacity to make accurate predictions within a specific time
seriesoncetheinitialmodelparametershavebeenset. WhileARIMAmodelsexcelincontinuing
predictionswithintheseriestheyareconfiguredfor,theydonotinherentlypossessthefacultyto
forecastacrossdisparatetimeserieswithoutrecalibration. WeobtaintheARIMA’sforecastingresults
from (Challuetal.,2023). AsshowninTable8,theresultshighlightthesuperioradaptabilityof
our‘towardsfoundationmodel’–TEMPO–whichretainsitspredictiveaccuracyevenwhenapplied
totimeseriesbeyonditstrainingscope, therebyillustratingthefeasibilityofmoreuniversaland
resilientforecastingmethodologies.
D FURTHER ANALYSIS
D.1 DESIGNOFPROMPTPOOL
Inthissection,weproposeanotherpotentialpromptdesignforaddressingnon-stationarynatureof
real-worldtimeseriesdatawithdistributionalshifts(Huangetal.,2020). Specifically,weintroduce
asharedpoolofpromptsstoredasdistinctkey-valuepairs. Ideally,wewantthemodeltoleverage
relatedpastexperiences,wheresimilarinputtimeseriestendtoretrievethesamegroupofprompts
from the pool (Wang et al., 2022b). This would allow the model to selectively recall the most
representativepromptsatthelevelofindividualtimeseriesinstanceinput. Inaddition,thisapproach
can enhance the modeling efficiency and predictive performance, as the model would be better
equippedtorecognizeandapplylearnedpatternsacrossdiversedatasetsviaasharedrepresentation
pool. Promptsinthepoolcouldencodetemporaldependencies,trends,orseasonalityeffectsrelevant
todifferenttimeperiods. Specifically,thepoolofpromptkey-valuepairsisdefinedas:
V ={(k ,V ),(k ,V ),··· ,(k ,V )}, (5)
K 1 1 2 2 M M
where M is length of prompt pool, V
m
∈ RLp×LE is a single prompt with token length L
p
and the same embedding size L
E
as P
T
i and k
m
∈ K = {k
m
}M
m=1
with the shape of RLE.
The score-matching process can be formulated with the score-matching function γ (cid:0) Pi,k (cid:1) =
T m
P
T
i ·k
m
/∥P
T
i∥∥k
m
∥,whereγ : RLE ×RLE → R. Themodelistrainedinanend-to-endwayto
optimizepredictionswiththeprompts. ThequeryPi thatisusedtoretrievethetop-Kcorresponding
T
valuecomesfromthepatchedtimeseriesinput. Therefore,similartimeseriescanbeassignedto
similarprompts. Denoting{s }K asasubsetofKindicesfortheselectedtop-Kprompts,ourinput
j j=1
embeddingoftrendisasfollows:
x =[V ;··· ;V ;P ], 1≤K≤M, (6)
T s1 sK T
where we concatenate all the tokens along the temporal length dimension, so as x ,x . Each
S R
instance can be assigned to multiple prompts, which can jointly encode knowledge pertinent to
the forecasting task- such as periodic patterns exhibited by the time series, prevailing trends, or
seasonalityeffects.
22

PublishedasaconferencepaperatICLR2024
Table9: ComparethedifferentpromptdesignsontheETTm2dataset.
Semi-soft Soft Hard Pool Poolmaskall
mse/mae mse/mae mse/mae mse/mae mse/mae
96 0.182/0.263 0.189/0.271 0.182/0.267 0.185/0.267 0.1952/0.274
192 0.243/0.304 0.252/0.307 0.243/0.302 0.242/0.304 0.2739/0.324
336 0.309/0.344 0.306/0.348 0.299/0.340 0.289/0.336 0.3131/0.354
720 0.384/0.392 0.386/0.394 0.380/0.392 0.373/0.386 0.3794/0.390
Avg. 0.280/0.326 0.283/0.330 0.276/0.325 0.273/0.323 0.290/0.335
D.2 RESULTSONDIFFERENTPROMPTDESIGN
Inthissection,weexaminetheimpactofvariouspromptdesignsonmodelperformance. Weutilize
the‘semi-soft’promptasoutlinedinSection3.3,wherethepromptvectorsareinitializedsemi-softly;
the soft prompt, which entails the random initialization of vectors of identical dimensions to the
‘semi-soft’prompt;andthehardprompt,whichissemanticallymeaningfulandremainsfixedpost-
tokenization. Additionally,weexplorethepromptpool,asdescribedinSection D.1,andemploya
similarleave-one-outapproachtomaskallpromptswithinthepooltoinvestigateitseffectiveness.
Thefindings,presentedinTable 9,revealthat,intheETTm2dataset,thepromptpooloutperforms
the‘semi-soft’promptinthreeoutoffourscenarios,underscoringthepotentialofpromptstoenhance
modelcapacityandadaptabilitytoshiftsindatadistribution. Furthermore,weobservethatprompts
withexplicitsemanticcontent(Semi-softandHard)surpasstheperformanceofsimplesoftprompts.
This suggests that incorporating semantic information as discrete indicators within a pre-trained
modelcanmoreeffectivelyorchestratedomainknowledge. Thisunderstandinginformsthedesignof
promptsforefficientinteractionwithlanguagemodels,especiallyinapplicationswhereprecision
andrelevanceoftheoutputarecrucial.
D.3 ANALYSISONPROMPTPOOL
Hereisasummaryofhowthepromptsareinitializedandtrainedinourwork:
• Initialization: Thepromptembeddingsinthepoolarerandomlyinitializedfromanormal
distribution,asisstandardpracticefortrainableparametersinneuralnetworks.
• Training: Theprompts’valueandallothermodelparametersaretrainedinanend-to-end
mannertooptimizetheforecastingobjective. Thisallowsthepromptstobecontinuously
updatedtoencoderelevanttemporalknowledge.
Thenumberofpromptsandembeddingdimensionsaretreatedashyperparametersandtunedfor
goodperformance. Differentpoolsettings,includingpoolsize,topknumber,andpromptlength,
willleadtodifferentresults. Toexplorethis,weconductatotalof27experiments,setting3distinct
valuesforeachofthe3settings: (1)poolsizeof10,20,and30. (2)topknumbersof1,2,and3. (3)
promptlengthsof1,2,and3. WechoosethecombinationwiththebestresultsforTEMPO settings.
Forthelong-termandshort-termforecastingexperiments,wechooseapoolsizewithM =30and
K=3andpromptlengthis3. Detaileddesignanalysisprovidesinsightsintopromptsimilarityand
selection. Notethat,thepromptpool’skeyin (Wangetal.,2022b)istrainablewhichallowsusto
maintainconsistentanddistinctcharacteristicsoftimeseriesdataforanalysis. Ourworkoffersan
initialexplorationintoprompt-basedtuningfortimeseriesforecasting,butsubstantialroomremains
foradvancingpromptpooldesign.
D.3.1 PROMPTSELECTIONDISTRIBUTION
Toelucidatethemechanicsbehindpromptselection,wehavevisualizedthedistributionhistograms
for chosen prompts corresponding to the trend, seasonal, and residual elements of the ETTm2
datasetinFigure11. Inourexperimentalframework,eachdatapointispermittedtoselectmultiple
prompts—withthreepromptsbeingchosenpercomponent. Consequently,thefrequencyisdeter-
minedbythenumberoftimesaparticularpromptisselectedacrossthedataset. Thehistograms
revealpronounceddiscrepanciesinpromptpreferencesbetweenperiodicandseasonalcomponents.
23

PublishedasaconferencepaperatICLR2024
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0.0
01234567891011121314151617181920212223242526272829
Prompt ID
ycneuqerF
Trend
Season
Noise
Figure11: PromptDistributionforpromptpoolselection.
For instance, within the ETTm2 dataset, prompts 11, 20, and 24 are predominantly selected for
capturingtrends,whereasprompts8,10,and29areprimarilychosenforseasonalfluctuations. This
observationsubstantiatesthepremisethatthepromptpoolisadeptatfurnishingspecializedprompts
tailoredtodiscretecharacteristicsoftimeseriesdata.
D.4 ANALYSISONDESIGNSOFINJECTINGCONTEXTUALINFORMATION
Table10: SMAPEresultsofGEBDITdatasetwithdifferenttextualinformationinjection.
Event Sum+TP SumP+TP Sum⊕TP SumP⊕TP Sum+Semi SumP+Semi Sum⊕Semi SumP⊕Semi
EPAMS 11 38.77 38.77 38.75 38.90 38.91 38.82 39.04 38.79
17 41.02 41.03 40.95 41.05 41.24 41.08 41.38 41.08
19 44.03 44.02 44.06 44.10 44.41 44.19 44.73 44.24
Inthissection,weinvestigatetheinfluenceofvariousconfigurationsoftextualinjectionandoriginal
prompt design from multi-modality perspective. As depicted in Table 10, eight distinct prompt
designs were formulated. ’Sum’ denotes the utilization of a direct summary of textual data as a
prompt,while’SumP’signifiestheuseoftextualinformationasaquerywithinthepromptpool. The
symbols’+’and’⊕’representsummationandconcatenationoperations,respectively. ’TP’stands
for’timeseriespromptpool,’and’Semi’indicatesa’semi-softprompt’wherewemanuallydesign
theprompt,withtrainableparameters,referredtoas”Predictthefuturetimestepgiventhe{time
seriesdatatype}”for3differenttimeseries(Trend,Season,Residual)afterdecomposition. Each
designchoiceexertsadistinctimpactontheperformancemetrics. Thedirectincorporationoftextual
informationalongwiththepromptpoolyieldsthemostoptimalandnear-optimaloutcomes. Infuture
work,weaimtodelvedeeperintotheanalysisofmultimodalsolutiondesignstrategiesfortimeseries
forecasting.
D.5 HIDDENREPRESENTATION
Figure12demonstratesthedifferencebetweentherepresentationoftheoutputhiddenspacefrom
thepre-trainedlangaugemodel. WhiletherepresentationoftimeserieslearnedfromGPT4TSis
centeredasawhole,therepresentationofthedecomposedcomponentfromTEMPOimpliesacertain
softboundarybetweenthethreecomponents. ThisisademonstrationofhowTEMPOisabletolearn
therepresentationoftrend,seasonality,residualpartsrespectively,whichcontributestothesuperior
performanceofourmodelTEMPO.
24

PublishedasaconferencepaperatICLR2024
|     | Trend | 100 |     | Original Time Series |
| --- | ----- | --- | --- | -------------------- |
Seasonality
| 100 | Residual | 75  |     |     |
| --- | -------- | --- | --- | --- |
50
50
| 2 noisnemid ENS-t |     | 2 noisnemid ENS-t 25 |     |     |
| ----------------- | --- | -------------------- | --- | --- |
| 0                 |     | 0                    |     |     |
25
50
50
75
100
| 100 50 t-SNE dim0ension 1 | 50 100 | 100 100 | 50 t-SNE dim0ension 1 | 50 100               |
| ------------------------- | ------ | ------- | --------------------- | -------------------- |
| (a) TEMPO-ETTh1           |        | (b)     | GPT4TS-ETTh1          |                      |
|                           | Trend  |         |                       | Original Time Series |
Seasonality
| 100 | Residual | 75  |     |     |
| --- | -------- | --- | --- | --- |
50
50
| 2 noisnemid ENS-t |     | 2 noisnemid ENS-t 25 |     |     |
| ----------------- | --- | -------------------- | --- | --- |
| 0                 |     | 0                    |     |     |
25
50
50
| 100 |     | 75  |     |     |
| --- | --- | --- | --- | --- |
100
| 100 50 t-SNE dime0nsion 1 | 50 100 | 100 75 | 50 25t-SNE di0mension 125 | 50 75 100            |
| ------------------------- | ------ | ------ | ------------------------- | -------------------- |
| (c) TEMPO-ETTh2           |        | (d)    | GPT4TS-ETTh2              |                      |
|                           | Trend  | 100    |                           | Original Time Series |
Seasonality
| 100               | Residual | 75                |     |     |
| ----------------- | -------- | ----------------- | --- | --- |
| 50                |          | 50                |     |     |
| 2 noisnemid ENS-t |          | 2 noisnemid ENS-t |     |     |
25
| 0   |     | 0   |     |     |
| --- | --- | --- | --- | --- |
25
50
50
| 100                       |                 | 75     |                           |                      |
| ------------------------- | --------------- | ------ | ------------------------- | -------------------- |
| 100 50 t-SNE dime0nsion 1 | 50 100          | 100 75 | 50 25t-SNE dim0ension 125 | 50 75 100            |
| (e) TEMPO-ETTm1           |                 | (f)    | GPT4TS-ETTm1              |                      |
|                           | T r e n d       |        |                           | Original Time Series |
|                           | S e a s onality | 100    |                           |                      |
| 100                       | Residual        |        |                           |                      |
75
| 50                |     | 50                |     |     |
| ----------------- | --- | ----------------- | --- | --- |
| 2 noisnemid ENS-t |     | 2 noisnemid ENS-t |     |     |
25
| 0   |     | 0   |     |     |
| --- | --- | --- | --- | --- |
25
50
50
75
100
100
| 100 50 t-SNE0 dimension 1 | 50 100 | 75 50 | 25 t-SNE d0imension 125 | 50 75 100 |
| ------------------------- | ------ | ----- | ----------------------- | --------- |
| (g) TEMPO-ETTm2           |        | (h)   | GPT4TS-ETTm2            |           |
Figure12: ComparisonofGPT4TSrepresentationwithTEMPOrepresentationforpredictionlength
O =96usingTSNE.Trendinred,seasonalityinblue,residualingreen.
25

PublishedasaconferencepaperatICLR2024
D.6 MODELTRAININGTIMECOMPARISON
Figure 13illustratesthetrainingtimeofotherbaselinemodelsincomparisontoourmodelTEMPO.
Toensurefairness,wecalculatedthepercentageofruntimeformodelsoperatingonidenticalmachines
andutilizingequivalentcomputationalresources. Eachmodel’strainingtimeispresentedasaratio
relativetoTEMPO’strainingtime. Avaluelessthan1indicatesthatthemodeltrainsfasterthan
TEMPO, while a value greater than 1 suggests the opposite. We use horizontal bars to visually
representeachmodel’srelativetrainingtime,withthebarsextendingtotheleftorrightofthecentral
verticallinebasedonwhethertheyarefasterorslowerthanourmodelTEMPO,respectively.
Figure13: VisualComparisononrelativetrainingtimeofothermodelsandourproposedmodel
TEMPO underchannelindependentsetting.
BERT 0.32
LLAMA 4.62
TimesNet 5.70
DLinear 0.02
LightTS 0.03
PatchTST 0.20
FEDformer 3.45
ETSformer 0.77
T5 0.43
GPT4TS 0.24
TEMPO 1.00
0 1 2 3 4 5 6
E THE ROLES OF GENERALIZED ADDITIVE MODELS (GAM) AND SHAPLEY
ADDITIVE EXPLANATIONS (SHAP)
Inourpaper,GAMandSHAPserveasinstrumentaltools,notonlyforaffirminganticipatedfindings
butalsoforyieldingdeeperinsightsandexplanationsintotheinnerworkingsofintricatemodels.
• RoleofGAM:GAMinherentlymodelstheeffectsofdifferentfeaturesasadditivecompo-
nents. ThischaracteristicofGAMprovidesintrinsicinterpretabilitytoTEMPO.It’snot
merelyatoolforconfirmingtheabsenceofpatternsinresiduals;italsohelpsusunderstand
howeachfeaturecontributestothefinalprediction.
• RoleofSHAP:SHAPhelpsinattributingfeatureeffectspost-hoctoexplainthepredictions
madebycomplexmodels,whichmayotherwisebeopaque.
TheutilityofGAMandSHAPinouranalysiscanbedetailedasfollows:
• ConfirmationofAssumptions: theanalysesquantitativelyconfirmassumptionsaboutmodel
behaviorwithdata-drivenevidence,ratherthanjustintuition. Thissubstantiationincreases
thetrustandtransparencyinthemodel’spredictions;
• DetectingUnexpectedBehaviors: thecomponentattributioncouldrevealunexpectedbe-
haviorsifpresent. Forexample,residualimpactbeinghigherthanexpectedcouldindicate
overfittingnoise.
• ProvidingNuancedInsights: SHAPprovidesnuancebeyondhigh-levelexpectations,like
showingtheincreasingerrorofseasonalcomponentsinlongerforecasts.
26

PublishedasaconferencepaperatICLR2024
1.0
0.8
0.6
0.4
0.2
0.0
96 192 336 720
Prediction Length
egatnecreP
tnenopmoC
Trend
Seasonality
Residual
Error
Figure 14: The SHAP (SHapley Additive exPlanations) values of decomposed components of
TEMPOforweatherdataset.
Inourpaper,weusetheETTm1andweatherdatasetsasdetailedexamples. Thefullresultsused
tocalculatetheSHAPvaluecanbefoundatTable11. Indatasetsexhibitingstrongseasonality,the
seasonalcomponentmaydisplaymuchlargervariationsthantheresidualcomponent. Conversely,
indatasetswithminimalseasonality,thevariationsbetweenthesetwocomponentsshouldbemore
comparable. Wecancalculatethestrengthofseasonalityvia:
(cid:18) (cid:19)
Var(R )
S=max 0,1− t (7)
Var(S )+Var(R )
t t
Whenwecomparetheseasonalitystrengthsofdifferentdatasets,wefindthatETTm1(asshownin
Figure2,withaseasonalitystrengthof0.99)constitutesstronglyseasonaldata,whereastheweather
dataset(depictedinFigure14withaseasonalitystrengthof0.476)exhibitslessseasonalityanda
morepronouncedtrend. ThesefindingsalignwiththeconclusionsdrawnfromtheSHAPvalues.
TheperformancedegradationofETTm1,whenthepredictionlengthisincreased,canbeprimarily
attributedtoinaccuraciesinthepredictionofseasonalterms. Insummary,SHAPprovidespivotal
descriptivepowerformodeltransparency,movingbeyondintuition. Theabilitytodiscernhowmuch
andwherecomponentscontributeenablestargetedimprovements. Theseinsightscanguideusin
betterleveraginginductivebiastoenhancebothefficiencyandeffectivenessintheeraofpre-training
models. Oneoftheinterestingfutureworksisthatwecanadaptivelyandselectivelyoptimizespecific
componentsbasedontheGAMstructureandSHAPscoresduringthetrainingprocess.Thisapproach
wouldallowustofocusourcomputationalresourcesandeffortsonthemostinfluentialcomponents,
therebyimprovingtheoveralleffectivenessofthemodel.
F BASELINE MODEL EXPLANATIONS
Wedemonstratethebaselinemodelswecomparedwithinourexperimentsinthefollowing:
• DLinear(Zengetal.,2023): DLinearcombinesadecompositionschemefromAutoformer
andFEDformerwithlinearlayerstopredicttimeseriesdatabymodelingtrendandseasonal
componentsseparatelyandsummingtheirfeaturesforenhancedperformanceintrend-rich
datasets.
• PatchTST(Nieetal.,2023): PatchTSTisaTransformer-basedmodelformultivariatetime
seriesforecastingthatsegmentsdataintosubseriespatchesandusesachannel-independent
design to efficiently reduce computational costs while enhancing long-term prediction
accuracy.
27

PublishedasaconferencepaperatICLR2024
Table11: SHAPoriginalvaluesforeachcomponent
| w/otrend        | w/oseason   | w/oresidual | trend       | season      | residual emptyset       | completeset |
| --------------- | ----------- | ----------- | ----------- | ----------- | ----------------------- | ----------- |
| MSE/MAE         | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE MSE/MAE         | MSE/MAE     |
| 96 0.437/0.432  | 0.670/0.526 | 0.457/0.441 | 0.663/0.541 | 0.472/0.455 | 0.680/0.535 1.104/0.790 | 0.438/0.424 |
| 192 0.466/0.447 | 0.646/0.518 | 0.488/0.455 | 0.682/0.529 | 0.483/0.455 | 0.666/0.526 1.101/0.789 | 0.461/0.432 |
ETTm1 336 0.505/0.466 0.672/0.530 0.526/0.476 0.680/0.531 0.524/0.475 0.707/0.543 1.102/0.790 0.515/0.467
| 720 0.579/0.507 | 0.678/0.549 | 0.586/0.508 | 0.684/0.548 | 0.592/0.509 | 0.709/0.558 1.105/0.794 | 0.591/0.509 |
| --------------- | ----------- | ----------- | ----------- | ----------- | ----------------------- | ----------- |
| Avg 0.497/0.463 | 0.666/0.531 | 0.514/0.470 | 0.677/0.537 | 0.518/0.474 | 0.691/0.540 1.103/0.791 | 0.501/0.458 |
| 96 0.213/0.267  | 0.202/0.261 | 0.205/0.264 | 0.223/0.289 | 0.234/0.293 | 0.220/0.284 0.637/0.608 | 0.211/0.254 |
| 192 0.266/0.317 | 0.251/0.297 | 0.256/0.306 | 0.254/0.304 | 0.290/0.335 | 0.262/0.316 0.638/0.608 | 0.254/0.298 |
Weather 336 0.317/0.356 0.290/0.333 0.295/0.331 0.293/0.331 0.328/0.357 0.313/0.356 0.640/0.609 0.292/0.332
| 720 0.402/0.401 | 0.371/0.383 | 0.377/0.380 | 0.364/0.378 | 0.389/0.393 | 0.385/0.398 0.638/0.610 | 0.370/0.379 |
| --------------- | ----------- | ----------- | ----------- | ----------- | ----------------------- | ----------- |
| Avg 0.300/0.335 | 0.279/0.318 | 0.283/0.320 | 0.283/0.325 | 0.310/0.345 | 0.295/0.339 0.638/0.609 | 0.282/0.316 |
• FEDformer (Zhouetal.,2022): FEDformercombinesseasonal-trenddecompositionwith
Transformersfortimeseriesforecasting,leveragingfrequencyinsightsforefficiencyand
accuracy,outperformingstate-of-the-artmethods.
• Informer (Zhouetal.,2021): Informerisatransformer-basedmodeloptimizedforlong
sequencetime-seriesforecasting,leveragingProbSparseself-attentionforefficiency,self-
attentiondistillingforhandlinglonginputs,andagenerativedecoderforrapidpredictions.
• ETSformer (Wooetal.,2022): ETSformerisanovelTransformerarchitecturefortime-
series forecasting that integrates exponential smoothing principles, replacing traditional
self-attention with exponential smoothing attention and frequency attention, to enhance
accuracy,efficiency,andinterpretability.
• TimesNet(Wuetal.,2023): TimesNettransforms1Dtimeseriesinto2Dtensorscapturing
intra-andinter-periodvariationsandusesTimesBlockwithaninceptionblocktoextract
complextemporalpatterns,excellinginmultipletimeseriestasks.
• GPT-2 (Radford et al., 2019): GPT-2 is a decoder-based language model developed by
OpenAI,designedtogeneratecoherentanddiversetextualcontentfromagivenprompt. In
ourwork,weusetheGPT-2with6layersasthebackbone,whichisadaptedfromGPT4TS
(Zhouetal.,2023).
• BERT (Devlinetal.,2019): BERT(BidirectionalEncoderRepresentationsfromTrans-
formers)isanencoder-baseddeeplearningmodelutilizingtheTransformerarchitecture
designed by Google to understand the context of words in a sentence by analyzing text
bi-directionally.
• T5 (Raffeletal.,2020): T5(Text-to-TextTransferTransformer)isastate-of-the-artneural
networkmodelwithencoder-decoderbasedarchitecturedesignedbyGooglethatconverts
everylanguageproblemintoatext-to-textformat.
• LLaMA (Touvronetal.,2023):LLaMA(LargeLangaugeModelMetaAI)isacollectionof
state-of-the-artfoundationlanguagemodelsrangingfrom7Bto65Bparametersdelivering
exceptionalperformance,whilesignificantlyreducingtheneededcomputationalpowerand
resources. Inourwork,weusethefirst6layersof7BLLaMA.
G THEORICAL
ANALYSIS
| G.1 PROOFOFTHEOREM | 3.1 |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- |
TheoremG.1 Suppose that we have time series signal Y(t) = S(t)+T(t)+R(t),t ∈ [t ,t ],
1 n
whereS(t)istheseasonalsignal(periodical),T(t)isthetrendsignal(non-periodical)andR(t)is
theresidualsignal. LetE ={e ,e ,...,e }denoteasetoforthogonalbases. LetE ⊆E denote
|     |     | 1 2 | n   |     |     | S   |
| --- | --- | --- | --- | --- | --- | --- |
thesubsetofE onwhichS(t)hasnon-zeroeigenvaluesandE ⊆ E denotethesubsetofE on
|     |     |     |     |     | T (cid:80)n |     |
| --- | --- | --- | --- | --- | ----------- | --- |
whichT(t)hasnon-zeroeigenvalues. IfS(t)andT(t)arenotorthogonal,i.e. S(t )T(t )̸=0,
i=1 i i
thenE ∩E ̸=∅,i.e. E cannotdisentanglethetwosignalsontotwodisjointsetsofbases.
T S
28

PublishedasaconferencepaperatICLR2024
|     |     |     |     |     |     |     |     |     | (cid:80) |     | (cid:80) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- |
Proof1 WedecomposeS(t)andT(t)ontoE andacquirethatS(t)= a e andT(t)= b e .
|     |     |     |     |     |     |     |     |     |     | i i | i i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thenitisobviousthate ∈E ⇐⇒ a ̸=0ande ∈E ⇐⇒ b ̸=0. Now,letusconsiderthe
|     |     |     | i   | S   | i   |     | i T |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
innerproductofS(t)andT(t):
n
|     |     | (cid:88) |      |               |     | (cid:88) |         | (cid:88) | (cid:88) |         |     |
| --- | --- | -------- | ---- | ------------- | --- | -------- | ------- | -------- | -------- | ------- | --- |
|     |     | S(t      | )T(t | )=S(t)·T(t)=( |     |          | a e )·( | b e      | )=       | a b e e | (8) |
|     |     |          | i    | i             |     |          | i i     | i        | i        | i j i j |     |
|     |     | i=1      |      |               |     |          |         |          |          | i,j     |     |
NotethatthecomponentsfoundbyPCAisasetoforthogonalbasis. Thus,foranyi̸=j,wehave
| e e | =0. Thus,wehave: |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i j
n
|     |     | (cid:88) |        |                 |     | (cid:88) | (cid:88)    |       | (cid:88) | ||2           |     |
| --- | --- | -------- | ------ | --------------- | --- | -------- | ----------- | ----- | -------- | ------------- | --- |
|     |     | S(t      | i )T(t | i )=S(t)·T(t)=( |     |          | a i e i )·( | b i e | i )=     | a i b i ||e i | (9) |
2
|     |     | i=1 |     |     |     |     |     |     |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:80)n
Notethat S(t )T(t )=0. Thus,theremustbeatleastoneisuchthata ̸=0andb ̸=0. Thus,
|      |      | i=1 | i i             |     |     |     |      |     |     | i i |     |
| ---- | ---- | --- | --------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
| e ∈E | ande | ∈E  | ,inotherwords,E |     |     | ∩E  | ̸=∅. |     |     |     |     |
| i    | S    | i   | T               |     | T   | S   |      |     |     |     |     |
TheabovetheoremprovesthatifT(t)andS(t)arenotorthogonal,thentheredoesnotexistaset
oforthogonalbasesthatdisentangleS(t)andT(t)ontotwodisjointsetsofbases. Notethatitis
common that a periodical signal is not orthogonal with a non-periodical signal. This is because
thespectrumofaperiodicalsignalisdiscreteandthespectrumofaperiodicalsignaliscontinuous.
Thus,itisverylikelythatthereexistoverlapsonthosenon-zerofrequenciesoftheperiodicalsignal.
NotethatPCAalsoaimsatlearningasetoforthogonalbasesonthedata. Wecanquicklyacquire
a corollary that PCA can not disentangle the two signals into two disjoint sets of bases. Based
on (Zhouetal.,2023)’sTheorem1,wecanrevealthatself-attentioninpre-trainedlargemodels
learnstoperformafunctioncloselyrelatedtoPCA.Therefore,theself-attentionmechanismcannot
automaticallydecomposethetimeseriesintoitstrendandseasonalcomponentsunlesswemanually
performthisoperation.
G.2 INTERPRETINGMODELPREDICTIONSFROMFREQUENCYDOMAIN
InadditiontoSection5.2,whichgivesanexperimentalperspectiveonwhydecompositioncanaid
forecastingresults,weprovideatheoreticalanalysisfromthespectraldomain. Specifically,time
seriessignalscanberepresentedasacombinationofdifferentfrequenciesinthespectraldomain.
Forecastingischallengingbecausereal-worldseriescomprisesconvolutedmixturesofvariations
with overlapping periodicities. However, by shifting our view to the frequency domain, we can
identifydistinctcomponentsviaSTLdecompositioncontainingisolatedfrequenciesthatstandout
clearlyfromtherestofthespectrum. Thisseparationofdominantperiodicpatternsiscrucialbecause
forecastingfuturevaluesequatestopredictinghowtheseunderlyingfrequenciesevolveovertime:
PropositionG.2(Equivalenceoftimedomainforecastingandfrequencydomainforecasting)
Assumex ,x ,...,x andxˆ ,xˆ ...,xˆ ,xˆ aretheinputandoutputsequencesofthefrequency
|     | 0   | 1   | N−1 | 0   | 1 N−1 | N   |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
model. Then,xˆ transferredfromthefrequencydomainisthepredictedvalueattimestampN.
N
Giveninputsequence{x |t = 0,1,...,N −1},whereN isthenumberofdiscretetimestamps,in
t
thetimedomain,theDiscreteFourierTransform(DFT,F)andinverseDiscreteFourierTransform
(iDFT,f)operationtoobtainthefrequencydomaincanbedefinedas:
N−1
|     |     |     |       | 1   | (cid:88) | −i2πux |              |     |     |     |      |
| --- | --- | --- | ----- | --- | -------- | ------ | ------------ | --- | --- | --- | ---- |
|     |     |     | F(u)= |     | f(x)e    |        | ,u=0,1,...,N |     | −1, |     | (10) |
|     |     |     |       | N   |          |        | N            |     |     |     |      |
x=0
N−1
(cid:88)
|     |     |     |     | f(x)= | F(u)ei2π |     | ux,x=0,1,...,N |     | −1. |     | (11) |
| --- | --- | --- | --- | ----- | -------- | --- | -------------- | --- | --- | --- | ---- |
N
u=0
AccordingtoPropositionG.2, assumingthatthenextvalueofF(u), canbepredictedasF′(N),
otherunknownvariablesinthetimeandfrequencydomains,includingthe(N +1)thdiscretesample
f(N)andthenewDFT’sresultF′(u),u=0,1,2,...,N −1aredeterminedbythegivenF′(N).
29

PublishedasaconferencepaperatICLR2024
Proof2 Let
|     |     |     | N −1     | e−i2π ux | e−i 2π u x |     |      |
| --- | --- | --- | -------- | -------- | ---------- | --- | ---- |
|     |     |     | (cid:88) | N        | N + 1      |     |      |
|     |     | A=  | f(x)(    |          | − ),       |     | (12) |
|     |     |     |          | N        | N +1       |     |      |
x=0
N−1
|     |     |     | 1   | (cid:88) f(x)e−i2 | π N x, |     |      |
| --- | --- | --- | --- | ----------------- | ------ | --- | ---- |
|     |     |     | B = |                   | N + 1  |     | (13) |
N +1
x=0
thenwehave:
2
|     |     | f(N)=(N            | +1)(F′(N)−B)e−i2 |     | π N ,          |     |      |
| --- | --- | ------------------ | ---------------- | --- | -------------- | --- | ---- |
|     |     |                    |                  |     | N + 1          |     | (14) |
|     |     | F′(u)=A+(F′(N)−B)e |                  |     | i2π( N − u)N . |     | (15) |
N + 1
| Foru=0,1,2,...,N | −1,thevalueofF′(u)−F(u)canberepresentedas: |               |     |     |                 |     |      |
| ---------------- | ------------------------------------------ | ------------- | --- | --- | --------------- | --- | ---- |
|                  |                                            |               |     | 1   | f(N)e−i2 π u N. |     |      |
|                  |                                            | F′(u)−F(u)=A+ |     |     | N + 1           |     | (16) |
N +1
Foru=N,thevalueofF′(N)canberepresentedas
|     |     |     |          | 1        | 2   |     |      |
| --- | --- | --- | -------- | -------- | --- | --- | ---- |
|     |     |     | F′(N)=B+ | f(N)e−i2 | π N |     | (17) |
N + 1
N +1
.
GivenF′(N),wecaninferenceF′(u)by:
i2π( N − u)N
|     | F′(u)=A+(F′(N)−B)e |     |     | N + 1 | ,u=0,1,2,...,N | −1. | (18) |
| --- | ------------------ | --- | --- | ----- | -------------- | --- | ---- |
andf(N)by:
|     |     |         | +1)(F′(N)−B)e−i2 |     | π N 2   |     |      |
| --- | --- | ------- | ---------------- | --- | ------- | --- | ---- |
|     |     | f(N)=(N |                  |     | N + 1 , |     | (19) |
Thus,theonlyvariablethatneedstobepredictedisF′(N).
Thispropositionrevealsthatifitiseasytopredictpatternsinthefrequencydomain,wecanmore
easily predict the time series’ future values. Forecasting equates to predicting the evolution of
theunderlyingfrequenciesthatmakeupthetimeseriessignal. STLdecompositionsignificantly
aidsthistaskbyseparatingcomponentswithdistinctdominantperiodicpatterns. WithSTL,each
componentpresentsfarfewerintertwiningperiodicinfluencestodisentangle,whichnotablysimplifies
the prediction problem. For instance, the trend component may exhibit a lone annual cycle that
clearlydominatesitsspectrum. Atargetedpredictivemodelfocusingsolelyonaccuratelyestimating
theprogressionofthisisolatedfrequencycangenerateaccurateforecasts. Likewise,theseasonal
elementneatlyisolatesrecurringdailyorweeklyfrequencies. Modelstailoredspecificallyforthese
knownperiodicitiesallowforhighlypredictableextrapolations. Incontrast,directlymodelingthe
rawdata’scondensedspectrumwithnumerousblendedperiodiccomponentsyieldsunsatisfactory
approximations. Theoverlappingfrequenciesaredifficulttodistinguishandpredictindependently.
ConceptualizingforecastingthroughafrequencydomainlensrevealshowSTLdecomposescomplex
spectralmixturesintodistinguishablefrequency-basedsub-problems. Thisallowsimplementation
optimizedpredictivestrategiestouncoverpatternsineachcomponentformarkedlyimprovedtime
seriespredictions. Inessence,STLfacilitatesaccuratefuturepredictionsbydisentanglingthespectral
contentintosimplerpredictableforms.
| H DETAIL | OF THE | TETS | DATASET |     |     |     |     |
| -------- | ------ | ---- | ------- | --- | --- | --- | --- |
Time series data Analyzing and forecasting a company’s future profitability and viability are
essential for its development and investment strategies. Financial assessment and prediction are
data-driven,mostlyrelyingonthecombinationofdiversedatatypesincludingcompanyreports,etc.
Inthisproject,ourprimarysourcesarethecompany’sfinancialstatements: balancedsheet,income
statements,andcashflowstatements.
The Standard & Poor’s 500 Index (S&P 500) represents a stock market index that measures the
stockperformanceofthe500largestcompaniesintheU.S.11sectorsintheS&P500areincluded
30

PublishedasaconferencepaperatICLR2024
inourdataset: BasicMaterials(21companies),CommunicationServices(26companies),Energy
(22 companies), Financial Services (69 companies), Healthcare (65 companies), Technology (71
companies),Utilities(30companies),ConsumerCyclical(58companies),ConsumerDefensive(36
companies),Industrials(73companies),RealEstate(32companies). Intermsofdatasetdivision,we
separatethesectorsinourdatasettoachievebothin-domaintasksettingandzero-shottasksetting.
Thefirstsevensectorsaretreatedastrainingandevaluationsectors,whilethelastfoursectorsare
reservedasunseensectorsforzero-shotforecastingtask.
ToaddressmissingnumericalinformationforcompaniesintheS&P500thatlackdatapriorto2010,
weapplylinearinterpolationafterexperimentingwithvariousmethods. Linearinterpolationisa
techniquethatestimatesavaluewithinarangeusingtwoknownend-pointvalues. Formissingvalues
inresearchanddevelopmentexpenses,weadoptedazero-fillingstrategy. Thisisbecausenullentries
inthesestatementstypicallyindicatethatthecompanydidnotmakeanyinvestmentinthatarea.
Contextual data collection This rise of Large-scale pre-trained models (LLMs) in the field of
NaturalLangaugeProcessinghasprovidednewpossibilitiesfortheirapplicationintimeserisanalysis.
LLMshaveprovenusefulforanalyzingandlearningcomplicatedrelationshipsandmakinginferences
acrossdifferenttimeseriessequences. However,mostexistingapproachesprimarilyconverttime
seriesdatatodirectinputintoLLMs,overlookingthefactthattheLLMsarepre-trainedspecifically
fornaturallanguageandthusneglectingtheincorporationofcontextualdata.
Further,theinformationcontainedintimeseriesdataislimited,especiallyinthefinancialfield. Time
seriesdatainthefinancialfield,suchascompanystatements,primarilyreflectthefinancialnumeric
changesbasedonthecompany’shistoricalstrategyandbroadermacroeconomicshifts. Thesedata
containthecompany’sinternalhistoricalinformation. However,thebroadermarketenvironment,
referredtoasexternalinformation,alsoplaysanimportantroleinthecompany’sfuturedevelopment.
Forexample,medicineandhealthcarecompaniesexperiencedsteadygrowthbeforetheoutbreakof
COVID-19. Butbetween2019and2020,aftertheoutbreakofthepandemic,thefinancialstatements
ofsuchcompanieswereimpactedsignificantly. Asaresult,werecognizethevalueofintegrating
news and reports as external data sources to complement internal information contained in time
seriesdata. Theinformationcontainedintheexternaldatamainlyincludes3parts: (i). Policyshifts
acrossregions(ii). Significanteventsoccurringglobally(iii). Publicreactiontocompanies’products.
Together,theseelementsprovidesupplementaryinformationmissingintimeseriesdata(internal
data),thereforeenhancingourforecastingcapabilities.
Extracting contextual data, such as news and reports, from varied sources presents a significant
challenge. Intoday’sdigitalage,numerousnewswebsitesandappsdeliverawiderangeofworld
news,spanningfrominfluentialnewsaffectingentireindustriestotrivial,minorreports. Thus,itis
crucialtofilterandsummarizetheinformation,distinguishingbetweenpivotalandlesssignificant
news. Fortunately,therecentlyreleasedChatGPTAPI2byOpenAIoffersthecapabilityofcollecting
andsummarizingnewsandreportsforaspecifiedduration.
Throughconsolidatingallrelevantdetails–query, quarter, yearlycontext, companyinformation,
andspecificrequirements–intousermessageandsettingacapat110tokensforresponse,wecan
efficientlyobtainthedesiredcontextualinformationfromChatGPTAPI.Forillustration,Figure 10
displaysanexamplefromcompanyA,showcasingdesignedpromptsandcorrespondingresponses
fromChatGPT3.5.Ifthecontextualinformationcannotbegenerated,theAPIoftenreturnsmessages
withkeywordssuchas’unfortunately’and’sorry’. Wedetectandreplacethemwiththeterm’None’,
representingneutralcontextualinformation. Additionally,Figure 15and 17provideaillustrationof
ourdataset,encompassingbothtimeseriesdataandthecorrespondingcontextualtexts. Adetailed
viewofthecontextualtextscanbeseeninFigure 16and 18.
2https://platform.openai.com/docs/guides/gpt
31

PublishedasaconferencepaperatICLR2024
Figure15: EBITDAforCompanyAwithcontextualinformation
Company A reported a net profit of $32 million, its highest third-quarter profit in four 1
years, and released its new Product M.
2002 third quarter
In the second quarter of 2005, Company A's profits rose 425%, with Product P sales 2
accounting for most of the increase. The company also announced plans to start using I
technique in their computers. 2005 second quarter
3
In the fourth quarter of 2007, Company A announced record-breaking sales of over 2
million Product S, and also launched their revamped line of Product N.
2007 fourth quarter
In the first quarter of 2009, Company A reported a 1% decline in sales and a 17% drop in
4
profits compared to the same period in the previous year, citing the global economic
downturn as a contributing factor. The company also announced the release of the U
technique software and the new Product IS. 2008 first quarter
Figure16: ExampleofgeneratedcontextualinformationforCompanyAmarkedinFigure15
Figure17: EBITDAforCompanyBwithcontextualinformatino
32

PublishedasaconferencepaperatICLR2024
Company B reported fourth-quarter earnings of $189 million, supported by continued  1
growth in its electronics unit. The company also announced plans to acquire the
company C for $143 million
2006 fourth quarter
Company B reported a net income of $0.95 per share for Q4 of 2008, down from $1.21  2
per share in the same quarter of the previous year. The company also experienced a
decrease in sales due to the economic recession. 2008 fourth quarter
In 2012's third quarter, Company B reported weaker-than-expected earnings due to a
3
decline in its business, but it still projected higher sales and profits for the year. The
company also announced plans to expand its production facilities D in Russia. 2012 third quarter
In 4Q 2012, Company B reported a net income of $138.7 million, down from $289.3  4
million in the same quarter of 2011; the company's revenue also decreased by 6.2% to
$2.56 billion. 2012 fourth quarter
Figure18: ExampleofgeneratedcontextualinformationforCompanyBmarkedinFigure17
| Table12: | TableofMainNotationonTEMPO |     |
| -------- | -------------------------- | --- |
Notation Description
| xˆi | ithchannelpredictionattimestept |     |
| --- | ------------------------------- | --- |
t
| xi  | ithchannellookbackwindow/historicalvaluesattimestept |     |
| --- | ---------------------------------------------------- | --- |
t
Φ modelparameter
V promptvaluefrompromptpool
| X   | inputdatawhichcanbedecomposedintoX | X X |
| --- | ---------------------------------- | --- |
T S R
| X ,X ,X | trend,season,residualcomponentsetintimet |     |
| ------- | ---------------------------------------- | --- |
Tt St Rt
xi ithchanneltthtimestepofxi
| Tt  |     | T   |
| --- | --- | --- |
xˆi
| Tt  | predictvalueoftrendcomponent |     |
| --- | ---------------------------- | --- |
P patchofinputdata
mthkeyinpromptpool
k m
mthvalueinpromptpool
V m
V promptpool
k
| K   | hyperparameter,numberofpromptstochoose |     |
| --- | -------------------------------------- | --- |
| M   | hyperparameter,lengthofpromptpool      |     |
| Z∗  | GPToutputfor*(trend,seasonal,residual) |     |
L predictionlength
H
L embeddingvectorlength
E
| Y   | finalpredictvaluebeforede-normalization |     |
| --- | --------------------------------------- | --- |
∗
Yˆ finalpredictvalue
∗
33