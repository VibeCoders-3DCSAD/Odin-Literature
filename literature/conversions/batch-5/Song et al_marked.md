---
conversion_metadata:
  converted_at: "2026-07-21T08:48:23Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Song et al.pdf"
  source_pdf_sha256: "66f7972e3deb5b6fec0041204ab38eb0163f2d2b0aab99e21c2fb57e68852638"
  page_count: 67
  markdown_char_count: 425604
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Artificial Intelligence Review (2025) 58:23
https://doi.org/10.1007/s10462-024-10989-8

Deep learning-based time series forecasting

Xiaobao Song1,2 · Liwei Deng2 · Hao Wang1,2 · Yaoan Zhang2 · Yuxin He3 · 
Wenming Cao1,2

Accepted: 4 October 2024 / Published online: 25 November 2024
© The Author(s) 2024

Abstract
With  the  advancement  of  deep  learning  algorithms  and  the  growing  availability  of  com-
putational  power,  deep  learning-based  forecasting  methods  have  gained  significant  im-
portance  in  the  domain  of  time  series  forecasting.  In  the  past  decade,  there  has  been 
a  rapid  rise  in  time  series  forecasting  approaches.  This  paper  comprehensively  reviews 
the  advancements  in  deep  learning-based  forecasting  models  spanning  2014  to  2024. 
We  provide  a  comprehensive  examination  of  the  capabilities  of  these  models  in  captur-
ing  correlations  among  time  steps  and  time  series  variables.  Additionally,  we  explore 
methods  to  enhance  the  efficiency  of  long-term  time  series  forecasting  and  summarize 
the diverse loss functions employed in these models. Moreover, this study systematically 
evaluates  the  effectiveness  of  these  approaches  in  both  univariate  and  multivariate  time 
series forecasting tasks across diverse domains. We comprehensively discuss the strengths 
and  limitations  of  various  algorithms  from  multiple  perspectives,  analyze  their  capacity 
to capture different types of time series information, including trend and season patterns, 
and  compare  methods  for  enhancing  the  computational  efficiency  of  these  models.  Fi-
nally,  we  summarize  the  experimental  results  and  discuss  the  future  directions  in  time 
series  forecasting.  Codes  and  datasets  are  available  at  https://github.com/TCCofWANG/
Deep-Learning-based-Time-Series-Forecasting.

Keywords  Time series forecasting · Deep learning · Time series decomposition

1  Introduction

1.1  Objective

Time series forecasting plays a crucial role in numerous applications, such as energy con-
sumption (Wu et al. 2021; Guo et al. 2023; Son and Van Cuong 2023; Dinh et al. 2023), 
transportation planning (Venkateshwari et al. 2023; Hu and Xiong 2023; Chen et al. 2023) 
and weather forecasting (Ma et al. 2023; Mung and Phyu 2023; Chen et al. 2023). In these 
practical application scenarios, forecasting future time series with the help of historical data

Extended author information available on the last page of the article

1 3

---

<!-- PAGE 2 -->

23  Page 2 of 67

Fig. 1  Process of time series forecasting

is of great significance for long-term planning and early warning in related fields (Wang et 
al. 2023; Miller et al. 2024). This process can be shown in Fig. 1. Therefore, this paper aims 
to explore deep learning-based time series forecasting models from multiple perspectives, 
offering a comprehensive evaluation of current mainstream models and encouraging readers 
to consider future directions for development in this field.

1.2  Review of existing approaches

Next,  we  will  summarize  the  existing  methods  from  four  main  perspectives:  time-step 
dependencies, correlations between temporal variables, the trade-off between expanding the 
model’s receptive field and reducing computational costs, and loss functions.

Time  series  information  usually  consists  of  time-step  dependencies  and  correlations 
between  temporal  variables  (Parzen  1961;  Lacasa  et  al.  2015;  Hsieh  2004;  Orang  et  al. 
2023). Fully exploiting these two types of information plays a crucial role in improving the 
model’s  capability. Traditional  models  like  the  autoregressive  integrated  moving  average 
(ARIMA) (Zhang 2003; Ariyo et al. 2014; Contreras et al. 2003) rely on statistical proper-
ties to extract information. However, they often fall short in fully capturing the time-step 
dependencies within complex time series. This is because traditional models primarily focus 
on linear features, while real-time series data usually contains intricate nonlinear correla-
tions. As a result, traditional models struggle to adequately leverage these dependencies. 
In recent years, with the development of algorithms related to deep lCR121earning and the 
improvement of computational power, deep learning-based methods have become increas-
ingly crucial in time series forecasting. Autoencoder and Stacked Autoencoders (SAE) (Lv 
et al. 2014) are utilized to extract the time-step features of the time series and obtain the pre-
diction results directly. (CNNs) (Gudelek et al. 2017; Markova 2022; Lu et al. 2020; Zhao 
et al. 2017; Liu et al. 2018; Hatami et al. 2018) are often used to extract time-series features 
in the short-term range because of their ability to aggregate time-step data in the receptive 
field. To  capture  a  broader  range  of  temporal  dependencies,  the Temporal  Convolutional 
Network (TCN) (Bai et al. 2018) expands the receptive field of its convolutional kernel. 
Specifically, TCN introduces dilated causal convolutions to time-series forecasting tasks. In

---

<!-- PAGE 3 -->

Page 3 of 67  23

contrast, Recurrent Neural Networks (RNNs) (Shi et al. 2015; Dey and Salem 2017; Sali-
nas et al. 2020; Hajirahimi and Khashei 2023; Lai et al. 2018) are specialized for temporal 
sequences and, theoretically, do not suffer from the limited receptive fields characteristic of 
CNNs. However, related studies have shown that the recurrent structure of RNNs can lead 
to issues such as vanishing gradient, limiting their ability to leverage long-term dependen-
cies  in  time  series. To  address  this,  researchers  have  developed models  like Long  Short-
Term Memory (LSTM) (Shi et al. 2015; Fischer and Krauss 2018; Zheng et al. 2017) and 
Gated Recurrent Units (GRU) (Dey and Salem 2017), which employ gating mechanisms 
to better capture long-term temporal correlations. Despite these advancements, LSTM and 
GRU  models  still  face  challenges,  such  as  vanishing  gradient  (Pascanu  et  al.  2013;  Noh 
2021; Le and Zuidema 2016) and error accumulation during training (Tang et al. 2021; Fan 
et al. 2019; Liao et al. 20185), which are common in RNN architectures. The effectiveness 
(Hewamalage et al. 2021; Pavlov-Kagadejev et al. 2024) of RNN-based forecasting models 
declines with longer forecasting time steps.

Given the exceptional performance of Transformer models in both natural language pro-
cessing (Vaswani et al. 2017; Devlin et al. 2018) and image processing (Dosovitskiy et al. 
2020) domains, these models are now being introduced to time series forecasting (Wu et al. 
2021; Li et al. 2019; Zhou et al. 2021). Compared with RNN-based models, Transformer 
based models adopt an encoder-decoder structure (Wang et al. 2022; Woo et al. 2022; Lee et 
al. 2024) and the attention mechanism (Liu et al. 2023; Niu et al. 2021; Young et al. 2022). 
It can dramatically alleviate the error accumulation (Li et al. 2019; Zhou et al. 2021) in long-
term time-series forecasting tasks. However, the authors of DLinear (Yun et al. 2019) point 
out that the attention mechanism is permutation invariance. The Transformer model does 
not make good use of time series order information. To solve this problem, DLinear uses a 
linear layer to implement time series forecasting.

Generally speaking, the correlation between time steps in a time series comprises mul-
tiple patterns (Cleveland et al. 1990; Hyndman and Athanasopoulos 2018; Dagum 2010), 
including  trend  (Verbesselt  et  al.  2010)  [62]  (Qi  and  Zhang  2008;  Woodward  and  Gray 
1993), seasonal patterns (Bell and Hillmer 1984; De Livera et al. 2011), etc. To reduce the 
complexity  of  time  series  forecasting  and  capture  these  temporal  patterns,  some  models 
have introduced time series decomposition techniques (Wu et al. 2021; Zhou et al. 2022; 
Oreshkin  et  al.  2019;  Woo  et  al.  2022).  These  approaches  initially  decompose  the  time 
series into several components, usually containing trend information, seasonal information, 
time-scale information (Taylor and Letham 2018; Jiang et al. 2021; Murray et al. 2000), 
and other time-series information. Subsequently, the model analyzes these distinct elements 
using specialized modules. For instance, Autoformer (Wu et al. 2021) utilizes a mean filter 
to convolve the input sequence, extracting trend terms that represent the time series’ trend 
patterns. Similarly, Fedformer (Zhou et al. 2022) employs multiple mean filters of varying 
sizes to derive trend terms, effectively addressing the limited receptive field issue. LSTnet 
(Lai et al. 2018) employs linear mapping to extract trend information from sequences and 
incorporates a predefined window to minimize the impact of distant information on trend 
forecasting. N-BEATS (Oreshkin et al. 2019) adopts a polynomial fitting method to model 
the time series’ trend terms. Similarly, both DLinear (Yun et al. 2019) and TDformer (Zhang 
et al. 2022) utilize shallow linear layers for this purpose. For seasonal information, LSTnet 
introduces a skip-connection architecture based on LSTM, enabling the model to account 
for information from time steps preceding a fixed interval, thereby capturing seasonal infor-

---

<!-- PAGE 4 -->

23  Page 4 of 67

mation in the data. Autoformer enhances the ability of the attention mechanism to discern 
seasonal patterns by using time-delayed similarities of the input. Fedformer, on the other 
hand, transforms the input time series into the frequency domain and employs an attention 
mechanism to analyze similarities between frequency components, effectively capturing the 
periodicity of the time series. ETSformer (Woo et al. 2022) filters frequency components 
based  on  their  magnitude,  reducing  noise  interference  in  seasonal  information  capturing. 
Time-scale information (Zhai et al. 2023), referring to the correlation of time steps at dif-
ferent scales, is addressed by models like Scaleformer (Shabani et al. 2022) and Pyraformer 
(Liu et al. 2021). The former applies downsampling to acquire inputs at various temporal 
scales and uses a forecasting model for multi-scale predictions. The latter processes time 
series at different scales and employs an attention mechanism to derive cross-scale attention 
correlations.

In addition to time-step dependencies, the essence of time series information also lies in 
the cross-time-step correlations among variables (Chakraborty et al. 1992; Yin et al. 2019). 
Thus, feature extraction of time series variables and exploring the inter-variable correlations 
are crucial for accurate forecasting. The TFT (Lim et al. 2021) employs RNN for feature 
extraction from time series variables and incorporates a feature filtering module to identify 
and utilize valuable information within these features. Aliformer (Qi et al. 2021) catego-
rizes input time-series variables and incorporates future information about these variables, 
enhancing the model’s forecasting capabilities. Crossformer (Zhang and Yan 2022) lever-
ages  the  attention  mechanism  to  analyze  attention-based  correlations  between  variables, 
offering a nuanced approach to understanding their interplay. It is worth noting that in recent 
years, with the development of large language models(LLMS) (Zhao et al. 2023) like Chat-
GPT (Achiam et al. 2023), LLMs can directly or indirectly generate prediction sequences 
through prompt engineering (Liang et al. 2024; Zhang et al. 2024).

CNN models are constrained by their limited receptive field, hindering their ability to 
effectively capture long-term time series data (Tang et al. 2020; Gál et al. 2004; Luo et al. 
2016). The RNN model, due to the problems of error accumulation, vanishing gradient, and 
exploding gradient, also cannot handle the long-term time series prediction task well. While 
Transformer models circumvent these issues, the attention mechanism’s computational cost 
grows quadratically with the series length, rendering the traditional Transformer impractical 
for  long-term  forecasting  (Li  et  al.  2019). Therefore,  some  research  is  devoted  to  reduc-
ing the computational cost of the attention mechanism, primarily through sparse attention 
mechanisms or shortening time series length. Related studies based on the sparse attention 
mechanism  include:  LogTrans  (Li  et  al.  2019)  filters  the  target  of  attention  computation 
based on the distance between time steps, reducing computation. Reformer (Kitaev et al. 
2020) maps the data into a hash space and filters the target of attention computation based 
on the distance among time steps in the hash space. Informer (Zhou et al. 2021) filters the 
target of attention computation based on computational output distribution. Related studies 
on reducing series length include: Informer utilizes convolutional aggregation of time steps 
in the receptive field. Convolutional aggregation reduces the input series length of the atten-
tion mechanism. PatchTST (Nie et al. 2022) slices long sequences into multiple fixed-size 
patches, reducing the attention mechanism’s computational cost.

Regarding  loss  function,  the  above  deep  learning-based  models  commonly  use  Mean 
Absolute Error (MAE) or Mean Squared Error (MSE) to evaluate the gap between predic-
tions  and  actual  outcomes  (Li  et  al.  2019;  Zhou  et  al.  2021;  Kitaev  et  al.  2020;  Zhou  et

---

<!-- PAGE 5 -->

Page 5 of 67  23

al.  2022;  Oreshkin  et  al.  2019).  However,  using  MAE  or  MSE  as  the  sole  optimization 
objective  has  some  limitations  (Goodfellow  et  al.  2014;  Mogren  2016;  Lyu  et  al.  2019). 
In  response,  several  models  have  innovated  upon  the  traditional  loss  function  to  address 
this issue. For instance, DeepAR (Salinas et al. 2020) converts the model output from spe-
cific values to probability distributions, using negative log-likelihood as its loss function. 
Similarly, SSDNet (Lin et al. 2021) integrates negative log-likelihood with MAE to form a 
hybrid loss function, allowing for the assessment of discrepancies in both value and prob-
ability terms. AST (Wu et al. 2020) employs a strategy inspired by the training mechanism 
of generative adversarial networks (GANs) (Goodfellow et al. 2014), comprising both dis-
criminant loss and generative loss components. This approach facilitates the alignment of 
the predicted distribution with the actual data distribution.

Deep  learning  architectures  usually  require  large-scale  labeled  datasets  for  achieving 
good performance on forecasting time series. Recent techniques of self-supervised learn-
ing (Pöppelbaum et al. 2022; Jaiswal et al. 2020) have opened up new a research frontier 
where  deep  learning  architectures  can  learn  general  features  from  unlabeled  time  series. 
The task of self-supervised learning is usually accomplished with some sort of time-series 
augmentation such as flipping, random noise, time warping, and random smoothing. Based 
on these data augmentation methods (Wen et al. 2020; Cui 2016) and the strategy of contras-
tive training (Pöppelbaum et al. 2022; Al-Tahan and Mohsenzadeh 2021), deep learning-
based time-series prediction models can capture temporal features during the pre-training 
phase. Subsequently, with a small amount of labeled data, they train the predictor to carry 
out predictions. At the same time, recent technology has also leveraged Few-Shot Learn-
ing to address the challenge of limited large-scale labeled datasets. This approach involves 
training  the  model  on  various  public  datasets,  enabling  it  to  extract  time-series  features 
effectively and exhibit strong generalization capabilities. Such a strategy leads to enhanced 
performance  when  applied  to  new  datasets.  Methods  employing  Few-Shot  Learning  can 
be categorized into two distinct directions. In Direction 1, the Memory network (Weston 
et  al.  2014)  approach  is  utilized.  This  involves  encoding  historical  time-series  data  dur-
ing training and retrieving these encodings when presented with new time-series datasets. 
This  allows  the  model  to  identify  similar  patterns  and  make  accurate  predictions  (Iwata 
and Kumagai 2020). Direction 2 involves using pre-trained LLMs known for their robust 
generalization abilities to generate precise predictions for time series data (Jin et al. 2023).

1.3  Highlights

The contributions of this paper are as follows:

– This paper provides a systematic review of the evolution of deep learning-based time 
series forecasting models from multiple perspectives. It thoroughly examines the ability 
of various models to capture correlations both between time steps and among variables, 
explores  the  trade-offs  between  expanding  the  model’s  receptive  field  and  reducing 
computational costs, and analyzes commonly used loss functions.

– This paper conducts a comprehensive evaluation of the effectiveness of various deep 
learning-based time series forecasting models in both univariate and multivariate tasks 
across  different  domains. Through  experiments,  we  uncover  the  strengths  and  weak-
nesses of different algorithms, assess their ability to capture various types of time series

---

<!-- PAGE 6 -->

23  Page 6 of 67

patterns (including trends and seasonal variations), and discuss strategies to enhance the 
computational efficiency of these models.

– Finally, this paper discusses future directions in the field of time series forecasting based 
on the analysis results.The organization of this paper is as follows. Section 2 introduces 
the background knowledge used in this survey. Section 3 traces the progress of such 
models from 2014 to 2024, focusing on the logic behind time series information mining, 
including correlation among the time step and correlation among variables. Section 4 
discusses the strategies for reducing computational costs in long-term forecasting. Sec-
tion 5 summarizes the loss functions utilized in deep learning-based time series fore-
casting. In Sect. 6, we conduct experiments on the discussed models and methods across 
several  datasets.  We  demonstrate  the  advantages  and  disadvantages  of  various  algo-
rithms from different perspectives, such as prediction accuracy, information extraction 
capabilities, the ability to identify trend and seasonal patterns, and the impact of differ-
ent attention mechanisms. In Sect. 7, we summarize the experimental results and discuss 
the prospective directions for the future development of time series forecasting.

2  Background

In this section, we will briefly introduce the background information essential for this survey.

2.1  Time series forecasting

−

−

, xt

L:t = [xt

L , where D is the number 
L,
Given a historical time series X t
of  dimensions  and  L  is  the  length  of  the  historical  time  series. The  future  time  series  to 
O ,  with  O  being  the  forecast  horizon. 
be  predicted  is  X t:t+O = [xt,
∈
A time series forecasting model can predict the future sequence X t:t+O  from the historical 
O  
sequence  X t
and the prediction model is denoted as  ϕ(
), the task of the time series forecasting can be 
·
expressed as:

L:t . Assuming  that  the  predicted  sequence  is  denoted  as  ˜X t:t+O ∈

· · ·
RD

, xt+O

RD

RD

· · ·

1]

∈

1]

−

×

×

−

−

×

˜X t:t+O = ϕ(X t

L:t).

−

RD   denotes  the  time  step  at  time  t,  and  the  time  step  correlation  refers 
Note  that  xxxt ∈
to  the  interrelations  among  these  vectors.  The  time  series  can  also  be  represented  as 
RL  denotes the i-th time-series variable. The correlation 
XXX = [vvv(cid:31)1 ;
of the time-series variable is the vectors among different vvv  vectors.

; vvv(cid:31)D], where  vvv(cid:31)i ∈

· · ·

2.2  Time series decomposition

Time-step dependencies usually consist of various correlations, such as trend and season 
correlations. To more thoroughly explore these dependencies and simplify the forecasting 
process, some forecasting models incorporate the concept of time series decomposition, an 
approach rooted in traditional time series analysis (West 1997; Soltani 2002; Dagum 2010). 
This analysis posits that any given time series X  is composed of distinct components: a trend

---

<!-- PAGE 7 -->

Page 7 of 67  23

term (T ), indicative of the series’ long-term progression; a seasonal term (S ), representing 
systematic and predictable fluctuations tied to seasonal effects; a recurrent fluctuation term 
(C ), denoting periodic variations within a specific period of time; and an irregular fluctua-
tion term (N ), which accounts for random variability in the data. Decomposition models 
fall into two primary categories: additive and multiplicative. The additive model represents 
the time series as the sum of the four components, i.e., X = T + S + C + N . While, for 
N .
the multiplicative model, an arbitrary time series can be expressed as X = T

C

S

∗

∗

∗

3  The logic of time series information mining

In this section, we will review the development of models over the past decade, with the 
processing logic of time series as the main storyline. Generally, the processing logic of mod-
els for time series can be categorized into two types: mining correlations among time steps 
and mining correlations among variables.

3.1  Mining correlations among time steps

In this subsection, we introduce the models and methods used to extract correlations among 
time steps. Specifically, these approaches can be categorized into two main types: holistic 
mining and targeted information mining, such as extracting trend or seasonal patterns.

3.1.1  Holistic mining

Autoencoders (Lv et al. 2014) are effective in uncovering time-step dependencies in time 
series. They  typically  consist  of  three  components:  an  encoder,  a  decoder,  and  a  predic-
tion module, with the workflow divided into pretraining and prediction phases. During the 
pretraining phase, the encoder extracts features that are fed into the decoder, which then 
reconstructs the input sequence to train the model parameters. In the prediction phase, the 
extracted features are input into the predictor, generating the forecasted sequence. In con-
trast, DLinear (Yun et al. 2019) uses a single linear layer to map the input vector’s dimen-
sion  directly  to  the  desired  output  dimension.  Due  to  the  simplicity  of  autoencoders  and 
linear layers, they are generally considered inadequate for fully capturing time-step depen-
dencies in time series.

Given the success of CNNs in the image processing domain (He et al. 2016; Krizhevsky 
et al. 2017; Szegedy et al. 2015), they are also frequently utilized to identify temporal fea-
tures in time series (Markova 2022; Lu et al. 2020; Zhao et al. 2017). Through convolution 
and pooling operations, CNNs aggregate temporal information within their receptive field to 
uncover internal time-step dependencies. However, due to the inherently limited receptive 
field, CNNs primarily extract short-term and discontinuous dependencies. To broaden the 
receptive field of CNNs and uncover dependencies across a wider range, Temporal Con-
volutional Networks (TCN) incorporate Dilated Causal Convolution (DCC) into the CNN 
architecture. Dilated convolution extends the receptive field without altering the convolu-
tion  kernel’s  size  (Yu  and  Koltun  2015; Yazdanbakhsh  and  Dick  2019),  allowing  CNNs 
to  capture  more  extensive  time-step  relationships.  Furthermore,  TCN  enhances  dilated 
convolution  with  temporal  causality,  ensuring  that  each  time  step’s  output  is  only  influ-

---

<!-- PAGE 8 -->

23  Page 8 of 67

Fig. 2  Dilated casual convolution

Fig. 3  The structure of LSTM

enced by preceding inputs. The operational intricacies of DCC, TCN’s central component, 
are depicted in Fig. 2, showcasing how dilated causal convolution effectively satisfies the 
demands of temporal sequence analysis.

Meanwhile,  in  order  to  capture  time-step  dependencies,  researchers  have  proposed 
Recurrent Neural Networks (RNNs) for time series forecasting, drawing upon the distinc-
tive characteristics of time-series data (Shelatkar et al. 2020; Amalou et al. 2022; Tang et 
al. 2021). RNNs, utilizing their recurrent connections, enable the features of a preceding 
time  step  to  act  as  inputs  for  the  current  step,  thereby  encapsulating  the  temporal  attri-
butes of each step with information from its antecedents. Unconstrained by the receptive 
field, RNNs theoretically can capture more extensive time-step correlations. However, the 
increased  span  of  these  recurrent  connections  may  lead  to  problems  like  gradient  explo-
sion and vanishing. To counter these issues, Long Short-Term Memory (LSTM) (Shi et al. 
2015;  Fischer  and  Krauss  2018)  units  introduce  a  gate  mechanism  and  cell  states  within 
the RNN framework. Cell states hold crucial information for long durations, while the gate 
mechanism-comprising  input,  output,  and  forget  gates-regulates  the  flow  of  information. 
The input gate controls the incorporation of current input into the cell state, the forget gate 
determines the retention of cell memory, and the output gate dictates the utilization of cell 
information for current output, as depicted in Fig. 3. Thus, for a given input time step xxxt , 
LSTM’s output can be formulated as follows:

---

<!-- PAGE 9 -->

Page 9 of 67  23

iiit = σ(WWW xixxxt + WWW hihhht

−

1 + bbbi),

fff t = σ(WWW xfxxxt + WWW hfhhht

1 + bbbf),

−

ccct = tanh(WWW xcxxxt + WWW hchhht

−

1 + bbbc),

ooot = σ(WWW xoxxxt + WWW hohhht

1 + bbbo),

−

(cid:31)

ccct = fff t (cid:31)

ccct

1 + iiit (cid:31)

−

ccct,

hhht = ooot (cid:31)

tanh(ccct),

(1)

(2)

(3)

(cid:31)

where ititit ,  ftftft , ooot  respectively denote the input gate, the forget gate, and the output gate. 
ccct  is the cell state candidates, ccct  is the cell state at the t-th time step, and hhht  is the time-step 
feature extracted at the t-th time step.  WWW xi ,  WWW hi , and  bbbi  denote the weight matrices and 
bias vectors for the input gates. Similarly,  WWW xf ,  WWW hf , and  bbbf  correspond to the weight 
(cid:31)
matrices and bias vectors for the forget gates. For computing the cell states,  WWW xc ,  WWW hc , 
and bbbc  are used. Lastly, WWW xo , WWW ho , and bbbo  represent the weight matrices and bias vectors 
for the output gates.
The  gated  structure  allows  models  to  selectively  retain  information  from  past  time  steps 
along with current features (Weerakody et al. 2021; Lin et al. 2022). This helps mitigate 
issues like gradient explosion and vanishing gradients and also reduces the impact of noise 
in historical data. This capability allows LSTM units to extract long-term temporal informa-
tion more efficiently than traditional RNN models. Gated Recurrent Unit (GRU) simplifies 
LSTM’s  gate  mechanism,  which  can  be  regarded  as  a  simplified  version  of  LSTM  and 
will  not  be  introduced  in  detail  here.  For  multi-step  time  series  forecasting,  RNN-based 
models typically rely on autoregression for sequential prediction (Maggiolo and Spanakis 
2019; Binkowski et al. 2018), using outputs from one step as inputs for the next. However, 
this autoregressive approach may lead to error accumulation. Furthermore, as the sequence 
length processed by the model increases, RNNs face amplified risks of gradient explosion 
and error accumulation, challenges that gate mechanisms do not fully resolve.

Given  its  exceptional  performance  in  both  natural  language  and  image  processing 
domains  (Devlin  et  al.  2018;  Vaswani  et  al.  2017),  the  Transformer  model  is  frequently 
employed to analyze general time-series data (Wen et al. 2022; Cai et al. 2020). As depicted 
in  Fig.  4,  the  Transformer  mitigates  error  accumulation  in  long-term  forecasting  by  uti-
lizing  an  encoder-decoder  architecture.  It  encodes  the  temporal  information  of  historical 
time series via the encoder and then decodes this information with the decoder to produce 
predictions. At the heart of the Transformer is the self-attention mechanism, which initially 
maps the input time series XXX  into query  QQQ , key KKK , and value VVV  matrices. Subsequently, 
it computes a similarity matrix between  QQQ  and KKK  and adjusts VVV  accordingly. Therefore, 
the Attention mechanism’s output,  OOO = Atten(XXX, XXX, XXX), is determined by the following 
process:

QQQ = WWW (cid:31)QXXX, KKK = WWW (cid:31)KXXX, VVV = WWW (cid:31)V XXX,

AAA = QQQ(cid:31)KKK, OOO = VVV Softmax(

AAA
√Dk

),

(4)

(5)

where  QQQ, KKK, VVV

L  represents the similarity between the L time 
RL
×
steps of  the input time series, and  Softmax(
) transforms the similarity into an attention 
·
weight distribution. The value matrix VVV  is then weighted and summed based on the atten-

L . The AAA

RDk×

∈

∈

---

<!-- PAGE 10 -->

23  Page 10 of 67

Fig. 4  The structure of Transformer

Table 1  Deep learning time 
series prediction models using 
time series decomposition

Time series 
information
Trend 
Information

Seasonal 
information

Multi time scale 
information

Non-stationary 
information

Key methods

Autoformer (Wu et al. 2021), 
Fedformer (Zhou et al. 2022),
LSTnet (Lai et al. 2018), TD-
former (Zhang et al. 2022),
DLinear (Yun et al. 2019), N-
BEATS (Oreshkin et al. 2019),
ETSformer (Woo et al. 2022), 
PatchTST (Nie et al. 2022)
LSTnet (Lai et al. 2018), Au-
toformer (Wu et al. 2021),
Fedformer (Zhou et al. 2022), 
ETSformer (Woo et al. 2022),
TDformer (Zhang et al. 2022), 
N-BEATS (Oreshkin et al. 
2019)
Scaleformer (Shabani et al. 
2022), Pyraformer (Liu et al. 
2021)
RevIN (Kim et al. 2021), NS-
Transformer (Liu et al. 2022)

Implications of 
the information
Information 
on apparent 
persistence and 
regularity of 
change between 
time steps

Periodic informa-
tion with fixed 
time intervals 
between time 
steps

Time-series 
information at dif-
ferent time scales
Information on 
the statistical 
properties of the 
time series over 
time

---

<!-- PAGE 11 -->

Fig. 5  The slice of the patch, where p is 
the length of the sliding window, and s 
is the step size of the window

Page 11 of 67  23

tion weight distribution to obtain the time-series feature OOO . In this way, OOO  incorporates the 
similarity correlations between time steps.
In Fig. 4, the encoder layer of the Transformer encodes the temporal dependencies within 
the input time series, subsequently feeding the encoded data to the corresponding decoder 
layer. This decoder layer then generates the forecasted sequence, leveraging the identified 
temporal  dependencies.  Besides,  the  feed-forward  module  within  both  the  encoder  and 
decoder  consists  of  several  fully  connected  layers. With  multiple  layers  of  encoders  and 
decoders stacked, the Transformer architecture can capture extensive long-term temporal 
correlations. The core of Transformer in time series forecasting lies in storing the similar-
ity  relationships  between  historical  time  steps  and  predicting  future  time  steps  based  on 
these relationships. It is worth noting that existing large language models(LLM) (Zhao et al. 
2023) like ChatGPT (Achiam et al. 2023) can be directly used for time series forecasting. 
Currently, large language models are commonly involved in time series forecasting in two 
ways: (1) as a predictive model (Liang et al. 2024): directly achieving sequential prediction 
based on prompt engineering (Mao et al. 2023; Shin et al. 2020), and (2) not as a predictive 
model (Zhang et al. 2024): generating embeddings by taking in relevant text information 
and using these embeddings as auxiliary variables input into the predictive model.

3.1.2  Targeted information mining

To further explore the correlations among time steps, some models leverage the concept of 
time series decomposition by developing custom modules designed to extract targeted infor-
mation, such as trend or seasonal information. The final predictive output is then obtained 
by integrating the forecasting results of various types of target information. Current deep 
learning models that employ time series decomposition are listed in Table 1.

Trend Information Trend information represents the trend correlations exhibited by the 
series across time steps, where the term “trend correlations” denotes the discernible persis-
tence and regularity of fluctuations between consecutive time steps within a defined scope 
(Taylor and Letham 2018; Cleveland et al. 1990; Asadi and Regan 2020). In addressing the 
attributes of trend information, Autoformer (Wu et al. 2021) employs a mean filter to extract 
the trend features from the time series. This involves convolving the input time series with 
a mean filter using a sliding window approach. However, due to the limited receptive field 
of the mean filter, the trend information acquired through the sliding window method tends 
to be discontinuous and localized. To mitigate this limitation, Fedformer (Zhou et al. 2022)

---

<!-- PAGE 12 -->

23  Page 12 of 67

devises a set of mean filters with varying receptive fields, yielding trend terms correspond-
ing to different forecasting horizons. Subsequently, the model assigns learnable weights to 
aggregate the trend terms through weighted averaging. This approach enables Fedformer to 
incorporate trend information spanning diverse forecasting horizons.

Since trend information is usually more stable on a local scale, the time step to be pre-
dicted  is  more  correlated  with  trend  information  from  closer  historical  time  steps,  while 
data from distant steps are deemed less favorable for trend prediction (Li et al. 2019; Lai et 
al. 2018). To mitigate the influence of distant data on trend predictions, LSTnet (Lai et al. 
2018) incorporates a predefined window, confining trend predictions to temporal informa-
tion within the window nearest to the target prediction. Within this preset window, which 
includes k time steps, LSTnet employs linear mapping to capture the linear relationships 
within  the  sequence,  subsequently  leveraging  autoregression  to  forecast  the  trend  term. 
Thus, LSTnet’s prediction of the trend term at time t is expressed as:

yyyt =

k

1

−

i=0
(cid:31)

WWW ixxxt

−

k+i + bbb,

(6)

∈

−

k+i ∈
−
RD
×

RD   denotes  the  prediction  of  the  trend  term  at  time  t,  xxxt
k + i)th time step, WWW i ∈

RD   denotes 
where  yyyt ∈
D  is the weight 
historical value of the time series at the (t
RD  is the bias. LSTnet employs autoregression to generate trend term pre-
matrix and bbb
dictions for all target locations. Similarly, both TDformer (Zhang et al. 2022) and DLinear 
(Yun et al. 2019) adopt linear mapping techniques for trend term prediction.However, linear 
relationships inadequately characterize the trend information of time steps, leading to weak 
interpretability  of  trend  terms  obtained  through  linear  mapping. To  address  these  issues, 
N-BEATS (Oreshkin et al. 2019) introduces the Trend Stack module, aimed at capturing the 
trend information within time series data. This module primarily employs polynomial fitting 
techniques to model the trend relationships between time steps. For the input sequence X, 
the Trend Stack module initially employs a fully connected layer to extract time-series fea-
tures, obtaining parameters for polynomial fitting. Subsequently, it introduces the time vec-
tor ttt = [0,1,2,
RO  as the independent variable for the fitting process. The resulting 
trend term generated by the Trend Stack can be represented as:

,(O
···
O

∈

1)]

−

θθθ = XXXWWW + BBB, XXX T =

θθθittti,

h

i=0
(cid:31)

(7)

×

∈

RD

∈
RD

RD
×

h  is the fit factor for polynomial fitting,  WWW
h  is the bias. XXX T ∈
×

h  is the weight matrix, 
RL
where  θθθ
×
O  is the trend term generated by the Trend Stack. h is 
and BBB
the highest power in the polynomial fit, which is usually set to a small value (0 < h < 5) by 
N-BEATS to prevent overfitting.While LSTnet mitigates the influence of distant informa-
tion on trend term prediction by implementing a preset window, it maintains uniform atten-
tion across time steps within this window. In contrast, ETSformer (Woo et al. 2022) posits 
that data proximate to the prediction position holds greater significance in encoding trend 
terms, prioritizing time steps in close proximity to the prediction location.

∈

---

<!-- PAGE 13 -->

Page 13 of 67  23

Exponentially weighted average enables the prediction of trend terms to pay more atten-
tion to those closer historical time steps (Hyndman et al. 2008; Ensafi et al. 2022), strength-
ening  correlations  among  short-term  time  steps.  ETSformer  introduces  the  Exponential 
Smoothing Attention (ESA) module, integrating the concept of exponential weighted aver-
aging into the attention mechanism. For the output OOO  of the attention mechanism derived 
from Equation (5), the operation of ESA can be expressed as:

ˆOOOt = αOOOt + (1

α) ˆOOOt

1 =

−

−

1

t

−

j=0
(cid:31)

α(1

−

α)jOOOt

j + (1

−

−

α)tv0,

(8)

where 0 < α < 1 is the learnable smoothing parameter and v0 denotes the learnable initial 
state.The  aforementioned  models  primarily  capture  the  short-term  trends  within  the  time 
series, inadvertently overlooking the influence of long-term trend information. To address 
this limitation, PatchTST (Nie et al. 2022) draws inspiration from patch processing meth-
odologies prevalent in computer vision (Dosovitskiy et al. 2020; Liu et al. 2021), integrat-
ing the concept of patches into the attention mechanism. As depicted in Fig. 5, PatchTST 
initially  segments  the  input  time  series  into  fixed-length  patches  using  a  sliding  window 
approach. Subsequently, these patches serve as inputs to the attention mechanism. Unlike 
traditional attention mechanisms, PatchTST does not focus on correlations among time steps 
within the individual patch; instead, it treats each patch as a unit and employs the atten-
tion mechanism to assess the similarity between patches. These patches contain aggregated 
information from short-term time steps, facilitating the exploration of long-term dependen-
cies within the time series. For the input sequence XXX , this process can be represented as:

XXX p =Patch(XXX), QQQp = XXXpWWW Q + bbbQ, KKK p = XXX pWWW K + bbbK, VVV p = XXX pWWW V + bbbV ,

(9)

AAAp =QQQpKKK (cid:31)p , OOOp = VVV pSoftmax(

AAAp
√Dk

),

(10)

n

n

×

×

×

×

×

RD

RD

RD

p  is the set of sliced patches, n denotes the number of sliced patches, 
where  XXX p ∈
h  is the weight 
p
and p denotes the length of each individual patch. WWW Q, WWW K, WWW V ∈
×
n  is the attention matrix, which 
matrix, and h is the dimension of hidden layer. AAAp ∈
represents  the  similarity  relationship  between  n  patches.Seasonal  Information:  Seasonal 
information is very important in time series analysis (Edition et al. 2002; Rawat et al. 2019), 
as it indicates the periodic behavior within the data, elucidating correlations between time 
steps separated by fixed intervals. However, extracting seasonal information is often more 
challenging than trend information due to the intricate periodicity inherent in time series 
data. Approaches for predicting seasonal terms can be broadly categorized into two groups: 
time  domain-based  methods  and  frequency  domain-based  methods.  Time  domain-based 
methods directly model the complex periodicity within the time domain (Lai et al. 2018; 
Wu et al. 2021). In contrast, frequency domain-based methods first transform the input time 
series into the frequency domain using a Fourier transform (Zhou et al. 2022; Woo et al. 
2022; Zhang et al. 2022), then identify complex periodicities based on frequency compo-
nents. In the following, we will delve into the seasonal terms mining approaches in both the 
time and frequency domains.

---

<!-- PAGE 14 -->

23  Page 14 of 67

−

−

To enable RNNs to capture seasonal information within time series data, LSTnet (Lai 
et al. 2018) introduces a recurrent-skip network that contains skip connections. Incorporat-
ing  skip  connections  facilitates  direct  interaction  between  time  steps  separated  by  a  pre-
defined interval. As depicted in Fig. 6, LSTnet initially assumes a potential period p for the 
input sequence. Subsequently, connections are established between the tth time step and the 
p)th time step within the RNN. The update of the hidden layer state at the tth time step 
(t
encompasses information from the  (t
p)th time step, the current input, and the hidden 
layer state from the previous time step. The skip-connected RNN allows the state update at 
each time step to fully consider the information of the time steps before a fixed time interval.
The skip-connected RNN necessitates preset timing periods p and can only be utilized 
to extract a single periodic relation, rendering LSTnet inadequate for analyzing time series 
exhibiting  intricate  periodic  patterns. To  address  this  limitation  and  capture  the  complex 
periodic relations inherent in time series data, Autoformer (Wu et al. 2021) introduces the 
Auto-Correction module. This module aims to assess the time-delay similarity among input 
sequences to characterize the periodicity of the original sequences, where time-delay simi-
larity  denotes  the  likeness  between  time-delayed  sequences  and  the  original  ones. Time-
delayed  sequences  are  shifted  by  τ   time  steps. Autoformer  posits  that  if  a  time-delayed 
sequence with a τ -step delay exhibits significant similarity to the original sequence, τ  can 
be considered a period of the original sequence. To capture these complex period relations, 
as depicted in Fig. 7, the Auto-Correction module initially employs  Roll(
, τ ) to shift the 
·
input sequence by a length of τ , subsequently evaluating the similarity between the delayed 
sequence and the original one. This similarity is then utilized as a weighting factor to aver-
age and aggregate the time-delayed sequence, thereby generating the seasonal terms of the 
sequence. Thus, for the input time series X, the Auto-Correction process can be delineated 
as:

RXXX(τ ) = lim
→∞

L

L

xxxtxxxt

1
L

τ ,

τ1,

−

· · ·

, τk = arg T opK(RXXX(τ ))
τ

1,

∈{

···

,L
}

,

(11)

t=1
(cid:31)
, ˆRXXX(τk) = Softmax(RXXX(τ1),

, RXXX(τk)),

· · ·

(12)

ˆRXXX(τ1),

· · ·

Fig. 6  Recurrent-skip network

---

<!-- PAGE 15 -->

Page 15 of 67  23

Fig. 7  Auto-Correction in Autoformer

Fig. 8  FEA in Fedformer

Auto-Correlation(XXX) =

k

i=1
(cid:31)

Roll(XXX, τi) ˆRXXX (τi),

(13)

· · ·

where xxxt  denotes the tth time step of the input time series, RXXX(τ ) denotes the similarity 
between the original sequence X and its delayed sequence by a time delay of τ  time steps. 
τ1,
, τk  represent k time delays of the delayed sequence that has the highest similarity to 
the original sequence. Autoformer leverages the similarity of time delays to extract the peri-
odicity inherent in the input time series. It approximates the complexity of the time series’ 
periods by utilizing multiple time delays of different degrees.
According to the Fourier series (Mathieu et al. 2013; Celeghini et al. 2021), any periodic 
signal  can  be  expressed  as  a  linear  combination  of  sinusoids  with  different  frequencies. 
Consequently,  frequency  domain-based  processing  involves  transforming  the  time  series 
into the frequency domain via Fourier transform and subsequently analyzing the series in 
this domain. Frequency domain-based seasonal term mining algorithms are able to analyze 
the  frequency  components  directly,  thereby  extracting  complex  period  information  from 
the time series. Subsequently, we will delve into the seasonal term mining algorithm in the 
frequency domain.

Fedformer  (Zhou  et  al.  2022)  adopts  an  approach  by  directly  assessing  the  similarity 
between frequency components within the frequency domain space. Fedformer introduces 
the FEA (Frequency Enhanced Attention) module, which employs an attention mechanism

---

<!-- PAGE 16 -->

23  Page 16 of 67

to scrutinize frequency components in the frequency domain, thereby delving into the peri-
odic characteristics of the input time series.

In Fig. 8, the FEA module first transforms the input time series from the time domain to 
). To mitigate computational costs 
the frequency domain using the Fourier transform  F (
·
in the subsequent Attention mechanism and counteract the effects of noise, FEA employs 
Select(
) to randomly sample frequency components in the frequency domain. Subsequently, 
·
FEA  applies  the Attention  mechanism  to  these  selected  frequency  components,  deriving 
similarity relations among them and processing the components accordingly. Finally, FEA 
)
returns the processed results to the time domain using the inverse Fourier transform F −
. Consequently, the FEA processing, based on the provided description and Equation (5), 
can be expressed as:

1(
·

˜QQQ =Select(F (QQQ)),

˜KKK = Select(F (KKK)),

˜VVV = Select(F (VVV )),

˜OOO =Atten( ˜QQQ, ˜KKK, ˜VVV ), YYY S = F −

1(Padding( ˜OOO)),

(14)

(15)

×

∈

CI

where  ˜OOO
Dk , I denotes the number of frequency components in the frequency domain. 
To fulfill the forecasting task, FEA requires padding the processing results in the frequency 
domain using Padding(
) to ensure that the sequence meets length requirements.Since FEA 
·
performs a random selection of frequency components in the frequency domain, there’s a 
risk of losing crucial season information. To address this, ETSformer (Woo et al. 2022) fil-
ters frequency components based on their magnitudes, retaining the k components with the 
highest magnitude. For seasonal term processing, ETSformer introduces the FA (Frequency 
Attention)  module. This  module  first  transforms  the  input  time  series  into  the  frequency 
domain, preserving the k frequency components with the greatest magnitude. Subsequently, 
the FA module returns the retained frequency components to the time domain via Fourier 
inverse transform and outputs the predicted seasonal terms.

In contrast to Fedformer’s FEA module, ETSformer operates under the premise that noise 
in time series data typically resides in frequency components with lower energy. Hence, it 
prioritizes frequency components with higher magnitudes. Conversely, Fedformer assumes 
noise may be present across all frequency components and thus employs random selection 
for screening. TDformer’s (Zhang et al. 2022) approach to seasonal term processing is the 
same as that of Fedformer. Meanwhile, DLinear (Yun et al. 2019) utilizes a single linear 
layer to handle the seasonal terms.

To streamline the module for extracting seasonal terms, N-BEATS (Oreshkin et al. 2019) 
simplifies its approach by exclusively processing specific frequencies within the frequency 
domain. Specifically, N-BEATS introduces a Season Stack, which utilizes Fourier period 
coding to analyze the seasonality of the time series. As depicted in Fig. 9, N-BEATS feeds 
the input time series into the Season Stack. The stack utilizes a fully connected network 
(FC)  to  derive  Fourier  period  coding,  representing  the  amplitudes  of  specific  frequen-
cies.  Subsequently,  leveraging  the  Fourier  period  coding  alongside  the  input  time  vector 
ttt = [0,1,2,
RO ,  the  Season  Stack  employs  Fourier  series  to  predict  the  seasonal 
terms. Thus, the processing of seasonal terms can be expressed as:

,(O
···
O

∈

1)]

−

θθθ =XXXWWW + BBB,

(16)

---

<!-- PAGE 17 -->

Page 17 of 67  23

Fig. 9  Season Stack in N-BEATS

YYY S =

h
2 +1
(cid:30)

(cid:31)

i=0
(cid:31)

θθθicos(2πittt) + θθθi+

sin(2πittt),

h
2 (cid:30)

(cid:31)

(17)

×

×

∈

∈

RD

RD

RL
×

where WWW

h  denotes the weight matrix, θθθ

h  denotes the Fourier coefficients 
predicted by an FC network, and h denotes the number of frequency components processed 
O  denotes the seasonal terms 
by the season module in the frequency domain.  YYY S ∈
predicted by the season module. From the equation provided, it’s evident that, unlike Fed-
former, N-BEATS chooses to process specific frequency components, aiming to simplify 
the module’s task of extracting seasonal information.
Multi Scale Information: In addition to trend and seasonal information, models have begun 
to  target  other  time-series  features  such  as  multi-scale  and  non-stationary  information. 
Multi-scale information pertains to the temporal dependencies of a time series at different 
scales (Shabani et al. 2022; Challu et al. 2023). For instance, considering hourly observa-
tions as the finest scale, coarser scales could represent daily, weekly, or even monthly pat-
terns within the time series. Integrating multi-scale temporal information enables models 
to capture dependencies across various durations, crucial for accurate time series modeling 
and forecasting.

To facilitate the capture of information across diverse time scales, Scaleformer (Shabani 
et al. 2022) introduces a multi-scale iterative framework for time series forecasting. This 
framework employs existing models (e.g., Autoformer, Fedformer) as the primary forecast-
ing model and applies filtering operations to transform the input time series into different 
time  scales. As  illustrated  in  Fig.  10,  Scaleformer  comprises  multiple  processing  layers, 
with  each  layer’s  inputs  derived  from  downsampling  the  original  inputs  and  upsampling 
the outputs of the preceding layer. At the ith processing layer, Scaleformer first upsamples 
the output of the preceding layer  XXX out,i
1 to obtain  UUU i . Simultaneously, it downsamples 
the original input XXX  using a scale factor si  to obtain PPP i . These UUU i  and PPP i  are then nor-
malized across scales and fed into the forecasting model. The primary forecasting model 
produces the processing result XXX out,i  for the current layer, and the output of the final pro-
cessing layer yields the ultimate prediction YYY .

−

Since Scaleformer needs to get the prediction in different time scale iterations, the distri-
bution of the model’s intermediate variables can change dramatically, which may lead to the 
accumulation and propagation of erroneous distributional information. In order to eliminate 
the effect of time scale changes, Scaleformer will perform cross-scale normalization opera-
Lm , the 
tions on inputs UUU i  and PPP i  at each processing layer. For UUU i ∈
cross-scale normalization operation can be expressed as:

Ln  and PPP i ∈

RD

RD

×

×

---

<!-- PAGE 18 -->

23  Page 18 of 67

Fig. 10  The structure of Scaleformer

µµµi =

1
n + m

m

n

(

PPP i,t +

UUU i,t),

t=1
(cid:31)

t=1
(cid:31)

ˆPPP i = PPP i −

µµµi,

ˆUUU i = UUU i −

µµµi,

(18)

where  µµµi   is  the  cross-scale  mean  coefficient  of  the  ith  layer,  which  is  the  mean  of  UUU i  
and PPP i . The cross-scale normalization operation is essentially a "zero-mean" operation on 
UUU i  and  PPP i . Scaleformer enhances the primary prediction model’s ability to learn multi-
scale time-series information by feeding time series of different time scales into the primary 
prediction  model.To  enable  the  attention  mechanism  to  focus  on  multi-scale  time-series 
information,  Pyraformer  (Liu  et  al.  2021)  constructs  a  pyramid  diagram  comprising  lay-
ers representing different time scales. Initially, Pyraformer processes the input time series 
through  convolution,  aggregating  time  steps  within  a  receptive  field  to  generate  coarser 
time scales. As illustrated in Fig. 11, Pyraformer utilizes the original input time series as 
the bottom layer of the pyramid diagram to represent the finest time scales. Subsequently, 
it iteratively aggregates the bottom time steps via convolution, using the resultant coarse-
scale time series as the top layer of the pyramid graph. Pyraformer employs the Pyramidal 
Attention Module (PAM) for nodes within the pyramid graph, enabling extraction of cross-
time scale features. Finally, depending on specific prediction task requirements, Pyraformer 
feeds the features of the top nodes into different networks to obtain the final output. Hereaf-
ter, we delve into the principles of PAM.

In PAM, each node is only concerned with its adjacent nodes. Considering the pyramid 
structure depicted in Fig. 11, let n(s)
RD  denote the lth node in the sth layer of the pyra-
l ∈
mid graph. The node n(s)
(s)
 of its neighboring nodes in adjacent layers. 
 can obtain the set N
l
l
This set encompasses three  components:  (1)  neighboring A nodes within the same  layer, 
including the n(s)
; (2) the lower layer nodes, representing finer 
l
(s)
time scale nodes, denoted as C
; and (3) the upper layer nodes, representing the coarser 
l
(s)
time scale node, denoted as P
l

(s)
 node itself, denoted as A
l

. This set is expressed as follows:

---

<!-- PAGE 19 -->

Page 19 of 67  23

Fig. 11  Pyramid  structure  in  Pyraformer.  Different  layers  have  different  node  sizes,  and  the  node  size 
indicates the granularity of the time scale

Fig. 12  Triformer. Node size indicates the granularity of the time scale

(s)
l =A

N

(s)
l ∪

C

(s)
l ∪

(s)
P
l

,

(s)
l =
A

n(s)
j

:

{

l

j
|

−

| ≤

A

1

, 1

−
2

j

≤

≤

L
Cs

−

,

1 }

(s)
l =

C

{

1)

n(s
j

−

:

l

|

1

|

−

C < j

lC

,

}

≤

(s)
l =
P

{

n(s+1)
j

: j =

l
C

(cid:31)

,

}
(cid:30)

(19)

(20)

(21)

(22)

---

<!-- PAGE 20 -->

23  Page 20 of 67

Fig. 13  Left: The VSN structure in the TFT; Right: the GRN module in VSN

Fig. 14  AliAttention in Aliformer

Table 2  The space complexity of different Attention modules, where L denotes the input sequence length
Models for optimizing complexity
Transformer (Vaswani et al. 2017)

LogTrans (Li et al. 2019)

Reformer (Kitaev et al. 2020)

Informer (Zhou et al. 2021)

PatchTST (Nie et al. 2022)

Pyraformer (Liu et al. 2021)

Crossformer (Zhang and Yan 2022)
ap denotes the length of the patch and s denotes the stride
bS is the number of time scales

Space complexity of attention mechanism
O(L2)
O(L(log L)2)
O(L log L)
O(L ln L)
O(n2), n =
O( S
1√L) b
O(L)

p
−
s (cid:29)

+ 2a

(cid:31)

L

−

---

<!-- PAGE 21 -->

Page 21 of 67  23

Fig.  15  LogSparse  Self-Attention.  The  connecting  line  indicates  the  need  to  compute  the  similarity 
relationship

Fig. 16  LSH Attention. Different colors indicate different groups

Table 3  Commonly used time series datasets in time series prediction
Timesteps
Datasets
ETTm1 &ETTm2a
69680
ETTh1 &ETTh2a
17420
Elctricityb
26304
Exchangec
7588
Trafficd
17544
ILI e
966
ahttps://github.com/zhouhaoyi/ETDataset
bhttps://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
chttps://github.com/laiguokun/multivariate-time-series-data
dhttp://pems.dot.ca.gov
ehttps://gis.cdc.gov/grasp/fluview/fluportaldashboard.html

Variates
7
7
321
8
862
7

Granularity
5 min
1 h
1 h
1 day
1 h
1 week

---

<!-- PAGE 22 -->

23  Page 22 of 67

where  L  is  the  sequence  length  of  the  original  input  to  the  model,  while  A  denotes  a 
hyperparameter indicating the number of nodes selected at the same time scale. C serves as 
another hyperparameter designed to regulate the number of ensemble nodes. To ensure the 
model focuses on multi-scale time-series information, PAM lets nodes n(s)
 compute atten-
l
(s)
tion correlations within the set N
l

:

y =

(s)
(cid:31)i
N
(cid:30)
∈

exp

i

(s)
(cid:30)
N
l

∈

qkT
exp

i /√dK
qkT

vi
i /√dK
(cid:29)

(cid:28)

(cid:30)

,

(cid:29)

(23)

where  q  is the query vector generated by node n(s)
, and ki , vi  are key-value pairs gener-
l
(s)
ated by nodes in the set N
. Pyraformer aggregates time steps of fine time scales into coarse 
l
time scales through convolutional operations and captures similarity correlations across dif-
ferent  time  scales  using  the Attention  mechanism.Unlike  Pyraformer,  Triformer  (Cirstea 
et al. 2022) generates coarse time-scale time steps through the Attention mechanism and 
takes fine time-scale sequences as inputs when processing coarse time-scale sequences. As 
shown in Fig. 12, the Triformer consists of multiple processing layers stacked on top of each 
other, each of which corresponds to a different time scale. The results from the fine time-
scale processing in the lower layers are fed as inputs to the coarser time-scale processing 
layers. The outputs from all layers are integrated into Triformer’s prediction process. This 
mechanism  enables  Triformer  to  effectively  explore  multi-scale  time  series  information. 
Next, we will delve into the underlying principles of each processing layer in Triformer. Tri-
former initially divides the input sequence into multiple local short sequences and applies 
p  in 
the Attention mechanism within these segments. For a local short sequence XXX p ∈
this layer, where p represents the length of the local short sequence. The output of the Atten-
tion mechanism in Triformer can be expressed as:

RD

×

ooop = Atten(hhh, XXX p, XXX p),

(24)

RD  is the temporal feature vector at a short-term interval, corresponding to the 
where ooop ∈
RD  serves as the query vector, capturing the temporal 
coarser time scale. Meanwhile, hhh
information at the current scale. So hhh  necessitates re-initialization for each processing layer 
accommodating distinct time scales. It is worth noting that ooop  will be used as the time step 
in the input sequence of the next processing layer.

∈

Non-stationary Information:  Non-stationary information refers to variations in the sta-
tistical characteristics of a time series over time (Ulyanov et al. 2016; Du et al. 2021; Muan-
det et al. 2013; Zhong and Cambria 2023). The presence of non-stationary time series poses 
challenges for prediction tasks in deep learning models, as they complicate the modeling 
of sequences of statistically changing data during inference, typically manifested through 
shifts in mean and standard deviation. RevIN (Kim et al. 2021) addresses this issue by stan-
dardizing input sequences within the model, ensuring each processed sequence adheres to 
a consistent distribution, and subsequently reverting the model’s predicted sequences to the 
original distribution during the output stage. Hereafter, we delve into a detailed exposition 
of RevIN.

RevIN  is  a  flexible  end-to-end  method  that  can  be  applied  to  arbitrary  models  (Li  et 
al. 2023; Liu et al. 2024, 2022). To mitigate non-stationary effects in input time series, it

---

<!-- PAGE 23 -->

Page 23 of 67  23

initially normalizes each sequence within a defined lookback window. Unlike conventional 
normalization techniques applied during time series preprocessing, RevIN normalizes input 
sequences within the lookback window utilizing learnable affine parameters. The normal-
ized sequences are then fed into the forecasting model to generate predictions. During the 
output stage, RevIN reverses the normalization process to restore the non-stationary char-
acteristics of the time series. Formally, for an input time series XXX , RevIN’s processing can 
be represented as:

mmm =

1
L

L

j=1
(cid:31)

XXX j,

vvv =

1
L

L

j=1
(cid:31)

mmm)2,

ˆXXX = γγγ(

(XXX j −

mmm
XXX
−
√vvv + ε

) + βββ,

(25)

RD  denotes the mean and variance of the time series in the lookback win-
where mmm, vvv
RD  denotes the affine coefficients. Then  ˆXXX  is fed into an arbitrary model 
dow, and  γγγ, βββ
to get the prediction YYY . To restore the non-stationary information of the time series, RevIN 
denormalizes the prediction:

∈
∈

ˆYYY = √vvv + ε(

YYY

βββ

−
γγγ

) + mmm.

(26)

Non-stationary information within time series poses a significant challenge to accurate fore-
casting, it is widely acknowledged that preprocessing methods such as those discussed in 
(Kim et al. 2021; Liu et al. 2022; Passalis et al. 2019) can help mitigate the non-station-
ary  nature  of  the  original  input  series.  However,  removing  the  inherent  non-stationarity 
of sequences may lead to the problem of over-stationarization, which in turn can subject 
forecasting  models  to  severe  overfitting. To  tackle  this  issue,  NS-Transformer  (Liu  et  al. 
2022)  integrates  non-stationary  information  into  the Attention  mechanism,  compensating 
for information lost during the normalization of the sequence.NS-Transformer adopts the 
standard Transformer architecture but incorporates De-stationary Attention in place of con-
ventional Attention mechanisms. De-stationary Attention leverages statistical information, 
specifically mean and variance derived from instance normalization, enhancing the model’s 
ability to capture non-stationary patterns within the original time series. Since NS-Trans-
former assumes that the time series have the same variance in all variables, vvv  is simplified 
to the scalar v. Given the stationarized input sequence  ˆXXX , linear mappings yield  ˆQQQ ,  ˆKKK , 
ˆVVV , alongside statistical parameters mmm  and v from the original sequence. The computation 
process of De-stationary Attention is as follows:

ˆAAA = v ˆQQQ(cid:31) ˆKKK + 1mmm(cid:31)KKK,

ˆOOO = ˆVVV Softmax(

ˆAAA
√Dk

),

(27)

where  QQQ, KKK, VVV  are the query matrix, key matrix, and value matrix obtained by linear map-
ping  of  the  original  input  sequence.  mmm   denotes  the  mean  vector  statistically  obtained  in 
the normalization, and v denotes the variance statistically obtained in the normalization.In 
order to directly use deep learning implementation Equation(27), NS-Transformer uses a 
multi-layer perceptron MLP(
) to learn non-stationary information from the original input 
·
time series:

---

<!-- PAGE 24 -->

23  Page 24 of 67

log τ = MLP(v, XXX), ∆∆∆ = MLP(mmm, XXX), ,

ˆAAA = τ ˆQQQ(cid:31) ˆKKK + 1∆∆∆(cid:31),

(28)

where τ
R denotes the variance information learned from the non-stationary information 
∈
RL  denotes the mean information learned from the non-stationary information. 
and  ∆∆∆
For the prediction of the Transformer model, NS-Transformer similarly chooses to denor-
malize to restore the prediction’s non-stationary information.

∈

3.2  Mining correlations among variables

In the context of multivariate time series forecasting, each time series dimension represents 
a distinct univariate time series. In addition to considering time-step dependencies, correla-
tions among variables also play a crucial role in predicting multivariate time series (Cheng 
et al. 2022; Jin et al. 2022; Cao et al. 2020; Zhang et al. 2023). For example, when predicting 
future temperature for a given region, relying solely on historical temperature records from 
the region is insufficient. Instead, including historical wind speed data from the region and 
historical  temperature  data  from  neighboring  regions  can  significantly  enhance  the  accu-
racy of the prediction. Therefore, in addition to capturing time-step dependencies, an alter-
native approach to temporal processing is to capture the correlations among variables. In 
section 3.1, the previously discussed forecasting models mainly concentrate on exploring 
dependencies among time steps, often overlooking the exploration of correlations among 
variables. Particularly, PatchTST (Nie et al. 2022), a model incorporating the Channel Inde-
pendence (CI) strategy, entirely disregards correlations among variables. In the following, 
we will introduce models that explicitly extract correlations among variables.

To address variables at a more detailed level, TFT (Temporal Fusion Transformers) (Lim

et al. 2021) classifies the variables of the input time series into three categories:

1.  Static variables: variables remain constant over time.
2.  Time-dependent variables: variables exhibit temporal changes and require prediction.
3.  Future-known  variables:  These  variables  include  known  future  information  (e.g., 
upcoming  holiday  dates),  other  exogenous  time  series  (e.g.,  historical  customer  foot 
traffic), and static metadata (e.g., store location).To handle these categorized multiple 
variables, TFT incorporates a Variable Selection Network (VSN) module for filtering. 
The  structure  of VSN  is  schematically  represented  in  Fig.  13.  For  different  types  of 
input variables, the VSN guides them individually through the Gated Residual Network 
(GRN) module. Furthermore, the VSN plays a crucial role in regulating the representa-
tion for each variable by utilizing weighted averaging, serving as an effective mecha-
nism for variable filtering. Specifically, the formulations of GRN are given by:

eee =ELU(WWW xxxx + WWW cccc + bbbe),

ddd =WWW deee + bbbd,

GRN(xxx, ccc) =LayerNorm(xxx + GLU(ddd)),

(29)

(30)

(31)

where xxx

RL  and ccc

and the external context, ELU(
·

∈

∈

RL  are univariate time series respectively from the primary input 
) represents

) is the ELU activation function, LayerNorm(
·

---

<!-- PAGE 25 -->

layer  normalization,  and  WWW x, WWW c ∈
Additionally,  bbbe, bbbd ∈
hidden layer.  GLU(
·
) is as follows:
GLU(
·

Rh
×

h   are  learnable  weight  matrices. 
Rh
×
Rh  are learnable biases, and h denotes the dimension of the preset 
) refers to the gated linear unit. For the input  ddd , the computation of

L ,  WWW d ∈

Page 25 of 67  23

(32)

GLU(ddd) = (dddWWW 1 + bbb1)

σ(dddWWW 2 + bbb2),

⊗

⊗
h   are  learnable  weight  matrices,  and  bbb1, bbb2 ∈
Rh
Rh   are  learnable 
where  WWW 1, WWW 2 ∈
×
)  denotes  the  sigmoid 
  represents  the  Hadamard  product,  and  σ(
biases.  The  symbol 
·
activation function.In TFT, the VSN module assigns weights to different variables, which 
helps  suppress  certain  variables’  representation  and  remove  noisy  inputs. The VSN  only 
accepts an univariate sequence as input, thus its output weights cannot consider the correla-
tion between different variables. To address this issue, Aliformer (Qi et al. 2021) leverages 
the Attention mechanism to capture the similarity relationships among variables, which is 
called AliAttention. This innovative approach enables the fusion of attention graphs gener-
ated from different variables, allowing the Attention mechanism to consider the similarity 
relations among diverse variables simultaneously.

As depicted in Fig. 14, for the input variables XXX 1 ∈

L , AliAtten-
tion performs separate computations of attention graphs for each variable. These individual 
attention graphs are then combined to create a unified attention graph. The resulting atten-
tion graph is subsequently used to generate the outputs of the Attention mechanism. This 
process can be summarized as follows:

L  and XXX 2 ∈

RD2×

RD1×

AAA1 = QQQ(cid:31)1 KKK 1, AAA2 = QQQ(cid:31)2 KKK 2, AAA∗ = AAA1 + AAA2, OOO = Softmax(

AAA∗
2Dk

)VVV 1,

(33)

∈

RL
×

In the process,  QQQ1, KKK 1, VVV 1 are derived from variable XXX 1, while  QQQ2, KKK 2 are derived from 
variable  XXX 2. The  resulting  attention  graph,  denoted  as  AAA∗
L ,  is  a  newly  obtained 
graph that integrates the similarity matrices of different variables. By incorporating AliAt-
tention, the Attention mechanism can explore the interdependencies among the variables by 
fusing the attention graphs.To facilitate a comprehensive exploration of correlations among 
variables, Crossformer (Zhang and Yan 2022) introduces the concept of directly applying 
the Attention mechanism to the variables instead of fusing attention graphs. For this pur-
L , Crossformer 
pose, Crossformer proposes DAttention. For the input time series XXX
×
∈
D , and then 
RL
first transposes the dimension of input series to obtain transposed  XXX (cid:31)
×
feeds XXX (cid:31)  into the Attention mechanism. DAttention, based on Equation (4) and (5), can be 
mathematically expressed as:

RD

∈

AAA = QQQ(cid:31)KKK, OOO = VVV Softmax(

AAA
√Dk

),

(34)

∈

RDk×

D  are all computed based on the transposed input  XXX (cid:31) . Here,  QQQ  
where  QQQ, KKK, VVV
represents the query matrix, KKK  represents the key matrix and VVV  represents the value matrix. 
D  in DAttention captures the similarity relation-
Importantly, the attention graph AAA
ships between D variables.Indeed, the distinction between AliAttention and DAttention lies 
in how they utilize the Attention mechanism. AliAttention focuses on capturing similar rela-

RD

∈

×

---

<!-- PAGE 26 -->

23  Page 26 of 67

tionships of variables by fusing attention graphs derived from each variable. On the other 
hand, DAttention applies the Attention mechanism directly to the variables, allowing it to 
uncover the cross-time-step dependence of variables.

4  Long-term time series forecasting optimization

In the field of long-term time series forecasting, Transformer model (Wu et al. 2021; Zhou 
et al. 2021, 2022) is widely used. This is because Convolutional Neural Networks (CNNs) 
have  limitations  regarding  their  receptive  field,  and  Recurrent  Neural  Networks  (RNNs) 
suffer from issues like error accumulation and gradient explosion. However, the attention 
mechanism’s  computational  cost  grows  quadratically  with  the  series  length.  To  address 
these  challenges,  researchers  have  developed  various  methods  to  optimize  the  attention 
mechanism for long-term time series prediction, as shown in Table 2.

The computational cost of the attention mechanism mainly arises from computing the 
similarity relationships between time steps. To optimize the Attention mechanism, two main 
approaches have been proposed:

(1)  Shortening the length of the input sequence of the Attention mechanism: This approach 
aims  to  reduce  the  computational  complexity  by  processing  shorter  subsequences 
instead of the entire input sequence. Various techniques, such as window-based (Zhou 
et al. 2021; Cirstea et al. 2022), segment-based (Nie et al. 2022; Liu et al. 2021), and 
hierarchical methods (Zhang and Yan 2022), have been proposed to divide the input 
sequence into smaller parts before applying the attention mechanism.

(2)  Sparsifying the attention mechanism: This approach selectively computes and sparsifies 
the similarity relationships, reducing the required computations. Different methods like 
sparse Attention (Li et al. 2019), kernelized Attention (Kitaev et al. 2020), and low-rank 
Attention (Zhou et al. 2021) have been developed to exploit the sparsity or low-rank 
structure in the similarity matrix, resulting in computational savings.In the following 
sections, we will explore these two approaches as a guiding framework to introduce 
optimization methods for the Attention mechanism in long-term time series prediction.

Shorten the Length of Time Series Processed by Attention Mechanism: Informer (Zhou et 
al.  2021)  utilizes  the  Transformer  framework,  which  integrates  convolution  and  pooling 
operations  to  shorten  the  length  of  time  series  gradually.  This  sequential  aggregation  of 
time steps occurs at each layer. As a result, the computational burden of the Transformer is 
significantly diminished. Therefore, the input time series of the jth layer in Informer can be 
expressed as follows:

ˆXXX j = MaxPool

ELU(Conv1d( ˆXXX j
(cid:31)

−

1))

,

(cid:30)

(35)

×

RD

where  ˆXXX j ∈
Lj  represents the output time series of the jth layer, and  Lj  denotes its 
sequence length. The input of the jth layer, denoted as  ˆXXX j
1, is worth noting 
−
that Lj < Lj
1.Unlike Informer, PatchTST (Nie et al. 2022) takes a different approach by 
dividing the original input sequence into multiple fixed-length short sequences, as depicted

1 ∈

RD

Lj

−

×

−

---

<!-- PAGE 27 -->

Page 27 of 67  23

in  Fig.  5. This  decision  allows  the  model  to  transition  from  processing  a  single,  lengthy 
sequence to managing multiple, short sequences. Additionally, PatchTST treats these short 
sequences as cohesive units and employs its attention mechanism to compute their similar-
ity relationships. As a result, the space complexity of the attention mechanism in PatchTST 
is reduced from the original O(L2) to O(N 2), where L represents the length of the input 
sequence  and  N  denotes  the  number  of  units,  with  N
L .  Consequently,  PatchTST 
achieves significant reductions in space complexity. Other models, such as Pyraformer (Liu 
et  al.  2021)  and  Triformer  (Cirstea  et  al.  2022),  employ  a  similar  strategy  to  PatchTST 
in  optimizing  the  space  complexity  of  the  attention  mechanism.  Compared  to  Informer, 
PatchTST demonstrates a greater advantage in optimizing space complexity due to its treat-
ment of sliced short sequences during processing. Notably, this advantage becomes more 
pronounced when handling long-term time series, as the growth rate of N remains relatively 
slow compared to the progressive increase of L.

(cid:31)

Sparse  the  Attention  Mechanism:  Sparsing  the  attention  mechanism  involves  selectively 
computing the similarity between time steps within the mechanism while preserving the origi-
nal length of the input sequence. These approaches can also effectively address the space com-
plexity associated with the attention mechanism. Building upon this concept, LogTrans (Li et 
al. 2019) introduces the LogSparse Self-Attention mechanism. Illustrated in Fig. 15, for the tth 
time step of the input time sequence, LogSparse Self-Attention determines the index of the time 
step with which the similarity relationship needs to be computed as follows:

III t =

t

(cid:31)

log2 t

2(cid:30)

(cid:29), t

−

−

log2 t

2(cid:30)

1
(cid:29), t

−

−

log2 t

2(cid:30)

2
(cid:29),

−

, t

−

· · ·

20, t

,

(cid:30)

(36)

where III t  represents the index of the time step in the tth time step where similarity computation 
is required. LogSparse Self-Attention selectively filters similarity relationships based on their 
temporal proximity to the current time step, prioritizing relationships among nearby time steps. 
Additionally, LogSparse Self-Attention is causal, meaning that the current time step disregards 
similar information from future time steps.Unlike LogTrans, which utilizes distance between 
time steps as a filtering criterion, Reformer (Kitaev et al. 2020) aims to group time steps in the 
feature space and compute attention within the groups, thereby achieving sparsity in the atten-
tion mechanism. The challenge of rapidly finding nearest neighbors in high-dimensional spaces 
can be addressed by Locality-Sensitive Hashing(LSH). A hashing scheme that assigns each 
time step to a hash space is called locality-sensitive if nearby vectors get the same hash with 
high probability and distant ones do not. Based on the LSH, Reformer proposes the LSH Atten-
tion mechanism. LSH Attention maps the input time series into a hash space, allowing attention 
computations only between time steps close to each other within this space.

−

RRR(cid:31)xxx

RRR(cid:31)xxx,

To map time steps into the hash space, Reformer establishes the hash function as fol-
lows: h (xxx) = arg max
b/2, and b represents the number 
, where RRR
of hashes, which corresponds to the dimension of the hash space. As depicted in Fig. 16, the 
time steps within the input time series are mapped to the hash space using this hash function. 
Based on the positional relationship of the time steps in the hash space, Reformer organizes 
all time steps into distinct groups. Within each group, each time step computes the similarity 
relationship exclusively with other time steps belonging to the same group. This selective 
calculation significantly reduces the computation cost of the attention mechanism.

RD

(cid:31)(cid:30)

(cid:29)(cid:28)

∈

×

---

<!-- PAGE 28 -->

23  Page 28 of 67

Informer (Zhou et al. 2021) also incorporates sparsity within its attention mechanism. 
However, unlike LogTrans and Reformer, Informer adopts a unique filtering criterion for 
similarity relationships based on the following assumption: within the attention mechanism, 
if the query vector qqq  possesses intricate temporal information, its attention distribution with 
respect to all key vectors should deviate significantly from a uniform distribution. Based on 
this concept, Informer introduces ProbSparse Self-Attention, which selectively retains the 
computation results of the query according to the score of each query. The scoring function 
for query vector  qqq  can be expressed as follows:

L

M(qqq, KKK) = ln

exp

j=1
(cid:31)

qqqkkk(cid:31)j
√Dk

1
L

−

qqqkkk(cid:31)j
√Dk

,

L

j=1
(cid:31)

(37)

, kkkL] represents the key matrix containing all the key vectors in the time 
where KKK = [kkk1,
· · ·
RDk  denotes the key vector corresponding to the jth time step in the time 
series, and kkkj ∈
series. The scoring function primarily evaluates the query vectors qqq  by analyzing their simi-
larity distribution relative to the other key vectors kkk . Ultimately, ProbSparse Self-Attention 
selectively  retains  the  Top-U  query  vectors.LogTrans,  Reformer,  and  Informer  employ 
Sparse Attention mechanisms that rely on specific filtering criteria for computing similarity 
relationships. For example, LogTrans filters the target of attention computation based on the 
distance between time steps. Reformer maps the data into a hash space and filters the target 
of attention computation based on the distance among time steps in the hash space. Informer 
filters query vectors based on the distribution of similarities between the query vector and 
all key vectors. In contrast, Crossformer (Zhang and Yan 2022) adopts a different approach 
by not employing a specific filtering criterion to sparsify the attention mechanism. Instead, it 
introduces transition units to avoid direct similarity computations between time steps. This 
strategy effectively reduces the space complexity of the Attention mechanism.

In the Crossformer model, when processing the input time serok with a length of L using 
L . These transition 
the attention mechanism, c transition units are introduced, where c
units act as intermediate components for performing similarity computations between query 
vectors  and  key  vectors  within  the  attention  mechanism.  This  approach  helps  avoid  the 
space complexity of  O(L2) associated with direct similarity computations between query 
L , the 
vectors and key vectors. For a key matrix K
Attention mechanism with transition units can be expressed as follows:

L  and a value matrix V

RDk×

RDk×

(cid:31)

∈

∈

OOO1 =VVV Softmax(

KKK (cid:31)RRR
√Dk

),

QQQ2 =WWW QXXX, KKK2 = WWW KOOO1, VVV 2 = WWW V OOO1,

OOO2 =VVV 2Softmax(

KKK (cid:31)2 QQQ2
√Dk

),

(38)

(39)

(40)

c  represents the transition unit, which are learnable param-
where each column of R
eter vectors. As evident from the provided equations, the inclusion of these transition units

RDk×

∈

---

<!-- PAGE 29 -->

allows for a reduction in the space complexity of the attention mechanism from O(L2) to a 
linear complexity of O(2cL) = O(L).

Page 29 of 67  23

5  Loss function

According to the optimization objective, the loss function commonly used in time series 
prediction models can be classified into two main types:

(1)  Loss function with a single optimization objective. This type of loss function primarily 
focuses on optimizing the gap in value between the prediction and the ground truth. 
The simplicity of this category of loss functions makes it widely employed. However, it 
has the limitation of solely aiming to minimize the gap in value between the prediction 
and  the  ground  truth.  Consequently,  this  category  of  loss  functions  faces  challenges 
when dealing with time series that contain intricate temporal patterns and exhibit strong 
fluctuations.

(2)  Hybrid loss function that optimizes the multiple objectives. To address the aforemen-
tioned issue, an alternative group of models utilizes hybrid loss functions that optimize 
the multiple objectives. This category of loss functions aims to combine multiple loss 
functions to optimize different modules of the model, enabling collaborative predictions. 
In the following sections, we will discuss these two types of loss functions separately.

5.1  Single-objective loss function

MAE,  MSE:  Mean Absolute  Error  (MAE)  and  Mean  Square  Error  (MSE)  are  commonly 
utilized loss functions in time series prediction tasks. They are employed to optimize the gap 
in value between the predicted values and the ground truth. MAE calculates the average of 
the absolute value of the prediction errors, while MSE calculates the average of the squared 
prediction errors. The specific formulas are provided below:

MAE(YYY , ˆYˆYˆY ) =

1
O ×

1
D

MSE(YYY , ˆYˆYˆY ) =

1
O ×

1
D

yi,j −

|

,

ˆyi,j|

O

D

i=1
(cid:31)

j=1
(cid:31)

O

D

(yi,j −

j=1
(cid:31)

i=1
(cid:31)

ˆyi,j)2,

(41)

(42)

×

×

∈

∈

RO

RO

D  represents the ground truth,  ˆYˆYˆY

D  represents the prediction, and 
where  YYY
O is the length of the prediction and D is the number of variables. From this equation, it 
becomes evident that when dealing with challenging-to-predict data points, MSE exacer-
bates the gap in value between the prediction and the ground truth, imposing a more sub-
stantial penalty. On the other hand, MAE lacks this characteristic and treats all prediction 
points uniformly. In time series forecasting tasks, using MAE as the loss function can effec-
tively mitigate the impact of outliers during model training. This approach is particularly 
beneficial  for  datasets  like  electricity  and  wind  power  data.  Conversely,  when  the  chal-

---

<!-- PAGE 30 -->

23  Page 30 of 67

lenging prediction points in the time series dataset containning significant information, as 
observed in Traffic datasets (Wu et al. 2021) and Exchange Rate datasets (Lai et al. 2018), 
the model can opt for MSE as the loss function to emphasize their importance during the 
training process.In essence, employing MSE or MAE implies a disregard for the direction 
of the error (Wang and Bovik 2009), meaning we are indifferent to whether the prediction 
surpasses or falls short of the actual value. However, this characteristic becomes crucial in 
specific time prediction scenarios. For instance, when forecasting the remaining lifespan of 
an engine, our prediction must underestimate the true value to prevent potential accidents.
Quantile Loss: Quantile loss is commonly used as a loss function in time series predic-
tion tasks. Unlike MSE and MAE, quantile loss penalizes positive and negative deviations 
between predicted and true values differently. Given the prediction  ˆYˆYˆY  and the ground truth 
YYY , the quantile loss between them can be expressed as:

= q

∗

L

max(0, YYY

−

ˆYˆYˆY ) + (1

q)

∗

−

max(0, ˆYˆYˆY

YYY ),

−

(43)

∈

where the quantile coefficient  q
[0, 1] can be adjusted to meet the specific demands of 
the prediction task. For example, in aircraft remaining useful life prediction (Zhang et al. 
2023, 2023; Wang et al. 2023), it is often desired for the model’s predictions to be lower 
than  the  actual  lifespan  of  the  aircraft  to  minimize  potential  risks.  Therefore,  a  quantile 
coefficient  q < 0.5 can be used, which increases the penalty imposed by the loss function 
on  larger  predictions. This  setting  encourages  the  model  to  generate  smaller  predictions. 
However, a drawback of quantile loss is the requirement to specify a target quantile, which 
is  often  impractical  in  many  prediction  scenarios.In  summary,  MAE,  MSE,  and  quantile 
loss are commonly used loss functions for point forecasts in deep learning models for time 
series  prediction.  These  loss  functions  are  effective  for  both  univariate  and  multivariate 
predictions, as well as for single-step and multi-step forecasting. Among the three, MSE is 
suitable when prediction errors are expected to follow a Gaussian distribution. However, 
when a dataset contains numerous outliers, MSE can be heavily affected by these, poten-
tially  leading  to  model  failure.  In  such  cases,  MAE  might  be  a  better  choice  as  the  loss 
function. In specific scenarios, such as Remaining Useful Life (RUL) prediction (Zhang et 
al. 2023, 2023; Wang et al. 2023), where biased predictions are necessary, quantile loss is 
often employed.

Beyond point forecasts, interval forecasts (Armstrong 2001) represent another approach 
in time series prediction. As the name suggests, this method provides a range of possible 
outcomes rather than a single point, offering insights into the model’s confidence or predic-
tion uncertainty. For interval forecasts, deep learning models typically use quantile loss as 
the loss function. Unlike in point forecasts, when quantile loss is applied to interval fore-
casts, the quantile parameter q in (43) represents a range rather than a single value. Due to 
space limitations, this paper does not explore interval forecasting in detail.

5.2  Hybrid loss function

The shortcomings of the aforementioned loss functions lie in their optimization objectives, 
which solely focus on the numerical distance between predictions and ground truth. Addi-
tionally, models based on a single optimization target are often structurally simple and can-
not incorporate other structured predictive mechanisms such as SSM (State Space Model)

---

<!-- PAGE 31 -->

Page 31 of 67  23

(Salinas et al. 2020; Lin et al. 2021) or GAN (Generative Adversarial Network) (Wu et al. 
2020; Mogren 2016; Goodfellow et al. 2014). Therefore, in order to leverage these special-
ized  structures  for  collaborative  predictions,  some  models  utilize  a  joint  loss  function  to 
optimize multiple objectives introduced by different structures within the model.

Negative  Log-likelihood:  SSDNet  (Lin  et  al.  2021)  incorporates  MAE  alongside  the 
negative log-likelihood as its loss function. This loss function allows for the simultaneous 
consideration of the numerical gap and distributions between the prediction and the ground 
truth. By tuning a parameter, SSDNet balances the influences of the MAE and the negative 
log-likelihood. The SSDNet model comprises the Transformer and the SSM (State Space 
Model) network. The SSM network is a mathematical framework that describes the relation-
ship between latent states and observable data in a time series.

SSMs (Durbin and Koopman 2012; Hyndman 2008; Seeger et al. 2016) enable the incor-
poration of structural assumptions into the model, making them particularly well-suited for 
scenarios where the time series structure is well-understood. This approach enhances the 
model’s interpretability and promotes efficient data utilization during the learning process. 
However, traditional SSMs are limited in their ability to infer shared patterns from a dataset 
of similar time series, as they are fitted individually to each time series.

SSDNet utilizes the Transformer to learn and estimate the parameters of the SSM net-
work, enabling the generation of interpretable predictions through the SSM network. There-
fore,  SSDNet  requires  optimization  of  the  SSM  network’s  predictions  and  parameters. 
SSDNet employs a hybrid loss function that integrates MAE and negative log-likelihood. 
This approach serves the dual purpose of optimizing the model’s prediction through MAE 
and refining the parameters of the SSM network via negative log-likelihood.

The  negative  log-likelihood  loss  function  requires  the  model’s  output  to  represent  the 
parameters of a probability distribution. The objective of this loss function is to maximize 
the probability of a real sample satisfying the predicted distribution. Therefore, for a real 
sample Y = [y1,
, yO], and the parameters θθθ  representing the predicted probability dis-
tribution  by  the  model,  the  optimization  objective  of  the  negative  log-likelihood  can  be 
formulated as follows:

· · ·

θθθ∗ =argmin

θθθ

O

i=1
(cid:31)

logP (yyyi|

θθθ).

−

(44)

Generating Adversarial Loss Functions: Inspired by the training method of Generative 
Adversarial  Networks  (GANs)  (Goodfellow  et  al.  2014;  Wu  et  al.  2020;  Mogren  2016), 
some  models  aim  to  utilize  adversarial  training  to  sequences  generated  by  the  generator 
should closely resemble real sequences and remain indistinguishable by the discriminator. 
Therefore, its optimization objective can be represented as:

min
G

max
D

V (

D

, G) = Ex

pdata(x)[log

∼

D

(x)] + Ez

pz(z)[log(1

∼

− D

(G(z)))],

(45)

D

is the discriminator of the model, G is the generator of the model, x

pdata(x) 
where 
∼
denotes the data samples drawn from the true distribution, and z
pz(z) denotes the fake 
data samples generated by the generator. From Equation (45), it is evident that the optimiza-
 aims to distinguish between sequences generated 
tion goal is twofold: the discriminator

∼

D

---

<!-- PAGE 32 -->

23  Page 32 of 67

by the generator and real sequences, while the generator strives to produce fake sequences 
that the discriminator cannot differentiate from real ones. Next, we will use the AST (Wu et 
al. 2020) model as an example to introduce the loss function of the generative adversarial 
approach.AST introduces the integration of the GAN training method into time series pre-
diction tasks. It utilizes the Transformer model as a generator, referred to as G, to generate 
predictions. The predictions and the real samples are then fed into a discriminator, denoted 
as 
,  for  discrimination.  The  discriminator  consists  of  multiple  fully  connected  layers, 
forming a fully connected network. The GAN loss function consists of two main compo-
nents: the discriminator loss and the generator loss. In AST, the generator loss is derived 
from the quantile loss function Pρ(
), quantifying the numerical gap between the prediction 
·
and the real sample. Conversely, the discriminator loss is based on the log-likelihood loss, 
which evaluates the ability of the discriminator to distinguish the fake and real samples.

D

ˆYYY = Transformer(XXX), YYY fake = Concat(XXX, ˆYYY ),

Generator Loss = Pρ(YYY O, ˆYYY ) + λE[log(1

(YYY f ake))],

− D

Discriminator Loss = E[

log

D

−

(YYY real)

−

log(1

− D

(YYY f ake))],

= Generator Loss + Discriminator Loss,

L

(46)

(47)

(48)

(49)

×

∈

RD

where  ˆYYY
O  represents the prediction generated by the Transformer model. D rep-
resents  the  number  of  variables,  and  O  represents  the  length  of  the  prediction.  On  the 
other hand,  YYY O  refers to the corresponding ground truth for the prediction. Additionally, 
(L+O) denotes the fake samples generated by the generator, where L represents 
YYY fake ∈
the length of the input sequence preceding the prediction. These fake samples are generated 
(L+O) represents the real samples drawn 
based on the generator’s predictions. YYY real ∈
from the real dataset.

RD

RD

×

×

6  Experiments

In this section, we conduct extensive experiments to evaluate the performance of the afore-
mentioned methods on various real-world time series prediction scenarios.

6.1  Dataset

As shown in Table 3, our empirical results are based on datasets from diverse domains, such 
as  energy,  exchange  rate,  traffic,  and  disease.  Detailed  descriptions  of  these  datasets  are 
provided below:

(1)  Energy: The ETT (Electricity Transformer Temperature) dataset (Zhou et al. 2021) con-
sists of data collected from power transformers in a specific region of China, spanning 
from July 2016 to July 2018. It includes seven distinct features, such as the load and 
oil temperature of the power transformers. The ETTh1 and ETTh2 datasets encompass

---

<!-- PAGE 33 -->

Page 33 of 67  23

17,420 samples with a sampling interval of 1 h, covering 7 features. On the other hand, 
the ETTm1 and ETTm2 datasets comprise 69,680 samples with a sampling interval of 
5 min, also encompassing 7 features. The Electricity dataset (Wu et al. 2021) contains 
hourly  electricity  consumption  data  from  321  customers  from  2012  to  2014.  It  con-
sists of 321 features and a total of 26,304 samples. Due to the temporal characteristics 
of electricity, electricity datasets naturally exhibit strong periodicity. For instance, the 
electricity data shows evident monthly periodicity due to the influence of temperature 
during the summer and winter seasons. Additionally, the electricity dataset also exhibits 
pronounced daily periodicity across different time periods within a day.

(2)  Exchange Rates: The Exchange dataset (Lai et al. 2018) covers daily exchange rates 
for eight currencies from January 1990 to October 2010. It contains eight features and 
a total of 7,588 samples. Unlike other time series data, the exchange rate data does not 
exhibit significant periodicity patterns, and its fluctuation changes are more complex. 
Additionally, important time series information is often contained in the extreme points 
of the exchange rate data, making methods like smoothing potentially result in the loss 
of important information.

(3)  Traffic: The Traffic dataset (Wu et al. 2021) comprises hourly data from the Califor-
nia Department of Transportation for the years 2015-2016. It captures road occupancy, 
measured  by  various  San  Francisco  Bay Area  freeway  sensors. The  dataset  includes 
862 features and a total of 17,544 samples. Unlike electricity datasets, traffic datasets 
exhibit evident short-term periodic patterns. Moreover, traffic accidents frequently lead 
to abnormal occupancy rates on the associated roadways, resulting in a higher incidence 
of outliers in the traffic dataset, which can impact model performance.

(4)  Illness:  The  ILI  (Influenza-Like  Illness)  dataset  (Wu  et  al.  2021)  comprises  weekly 
records of patients diagnosed with influenza illness, as reported by the U.S. Centers for 
Disease Control and Prevention, spanning from 2002 to 2021. This dataset includes 7 
features, such as the proportion of patients with ILI and the total number of patients. It 
follows a sampling interval of 1 week and 966 samples. Due to the dynamics of disease 
transmission, the illness datasets exhibit fluctuations characterized by prominent long-
term yearly and monthly periodic patterns and noteworthy short-term trends.

6.2  Model

Table 4 summarizes all the models that appear in the experimental section. For the above 
models, we have referred to the optimal parameter settings in their respective papers and 
source code, and we have applied these parameter settings in the following experiments.

6.3  Evaluation metric

The time series forecasting task is typically categorized as a regression problem. Conse-
quently, evaluation metrics commonly used in regression tasks are employed to assess the 
forecasting performance of models in the time series forecasting task. Based on previous 
studies (Wu et al. 2021; Zhou et al. 2022; Li et al. 2019; Zhou et al. 2021), we utilize the 
mean absolute error (MAE) and mean square error (MSE) as fundamental metrics to evalu-
ate the performance of models. At the same time, to facilitate a more intuitive comparison

---

<!-- PAGE 34 -->

23  Page 34 of 67

of the prediction outcomes across various models, we integrated two supplementary evalu-
ation metrics, MAPE, and R2, in addition to MAE and MSE. MAPE measures the relative 
error between predicted and actual values, ranging from 0 to positive infinity; the closer to 0, 
the more accurate the predictions. R2 evaluates how well the independent variables explain 
the dependent variable, with values from 0 to 1; the closer to 1, the better the model fits the 
data.  Nonetheless,  we  presented  Mean Absolute  Percentage  Error(MAPE)  and  R2  solely 
in specific experiments due to space constraints. The definitions of all metrics are given by

MAE(

YYY

) =

ˆ
, ˆ
ˆ
Y
Y
Y

N

1
O

×

D

×

MSE(

YYY

) =

ˆ
ˆ
, ˆ
Y
Y
Y

N

MAPE(

YYY

) =

ˆ
ˆ
, ˆ
Y
Y
Y

N

1
O

1
O

×

×

N

O

D

n=1
(cid:31)

o=1
(cid:31)

N

O

(cid:31)d=1
D

(cid:30)
(cid:30)

yn
o,d −

ˆyn
o,d

,

(cid:30)
(cid:30)

ˆyn
o,d

2

,

(cid:29)

D

×

n=1
(cid:31)

o=1
(cid:31)

(cid:31)d=1

(cid:30)

yn
o,d −

N

O

D

D

×

n=1
(cid:31)

o=1
(cid:31)

ˆyn
o,d

yn
o,d + (cid:23)
−
yn
o,d + (cid:23)

,

(cid:30)
(cid:30)
(cid:30)
(cid:30)
(cid:30)

(cid:31)d=1 (cid:30)
(cid:30)
(cid:30)
(cid:30)
(cid:30)

Table 4  Summarizes all the models in the experimental section
Category
Statistic model ARIMA (Zhang

Model

Year Category
2003 Transformer-based CNN-1D (Gudelek et al.

Model

(50)

(51)

(52)

Year
2017

2019

2020

2020

2021
2021

2021

2017)
LogTrans (Li et al. 2019)

Reformer (Kitaev et al. 
2020)
AST (Wu et al. 2020)

Informer (Zhou et al. 2021)
Autoformer (Wu et al. 
2021)
Aliformer (Qi et al. 2021)

2022

2022

2021
2022

TFT (Lim et al. 2021)
TDformer (Zhang et al. 
2022)
Fedformer (Zhou et al. 
2022)
NS-Transformer (Liu et al. 
2022)
Pyraformer (Liu et al. 2021) 2022
2022
ETSformer (Woo et al. 
2022)
PatchTST (Nie et al. 2022)
Crossformer (Zhang and 
Yan 2022)
Scaleformer (Shabani et al. 
2022)
Triformer (Cirstea et al. 
2022)

2023
2024

2024

2024

FC-based

RNN-based

2003)
ETS (Hyndman and 
Khandakar 2008)

Autoencoder (Lv et 
al. 2014)
SAE (Lv et al. 2014)
Nbeat (Oreshkin et al. 
2019)
Dlinear (Yun et al. 
2019)

GRU (Dey and Salem 
2017)
LSTnet (Lai et al. 
2018)
DeepAR (Salinas et 
al. 2020)

2008

2014

2014
2020

2022

2018

2018

2020

CNN-based

CNN-1D (Gudelek et 
al. 2017)
TCN (Bai et al. 2018) 2018

2017

State space 
model

SSDNet (Lin et al. 
2021)

2021

---

<!-- PAGE 35 -->

Fig. 17  Validation split of datasets

Page 35 of 67  23

R2(

YYY

ˆ
, ˆ
ˆ
Y
Y
Y

) =1

N
n=1

O
o=1

D
d=1

− (cid:31)

N
n=1

(cid:31)

O
o=1

(cid:31)

D
(cid:30)
d=1

yn
o,d −
yn
o,d −

ˆyn
o,d

y

2
2 , 
(cid:29)

(53)

where  y =

1
O

D

×

N

×

N
n=1

O
o=1

(cid:31)
D
d=1(yn

(cid:31)
o,d),

(cid:31)
=

YYY

(cid:28)

(cid:27)
YYY 1, YYY 2, ..., YYY N
{

represents the set of

}

(cid:31)
ˆYYY
=
{

(cid:31)
1
, ˆYYY

2

(cid:31)
, ..., ˆYYY

N

ˆ
true values, and  ˆ
ˆ
 denotes the set of predicted values generated by 
Y
Y
Y
the model. Here, N signifies the number of elements within the set, indicating the presence 
of N instances. Each instance is characterized by two elements within the set with dimen-
D . The parameter (cid:31)  is a small value close to 0, introduced to prevent division 
sions of RO
by zero scenarios. In our code implementation, we have uniformly set  (cid:31)  to 0.005 across 
different models to handle such cases effectively.

}

×

6.4  Main results

In this section, we perform experimental analyses on the models and methods mentioned 
earlier, considering various perspectives:

1.  Comprehensive Prediction Accuracy Assessment: We will assess the prediction accu-
racy  of  all  the  mentioned  models  on  5  time  series  datasets  derived  from  4  distinct 
domains. This assessment aims to provide a comprehensive evaluation of the models’ 
performances.
Investigation of Limitations: Considering the limitations of current complex models, 
we will investigate the underlying causes by focusing on two aspects.

2.

(1)  Shuffling Analysis: By shuffling the input time series, we can analyze the model’s 
ability to capture the sequential order of the data. This analysis involves comparing 
the model’s prediction accuracy before and after shuffling.

(2)  Extending the Lookback Window Analysis: Another aspect involves extending the 
length  of  the  input  time  series  while  maintaining  a  consistent  prediction  length.

---

<!-- PAGE 36 -->

23  Page 36 of 67

8
6
0
0
.
0
±

7
4
5
4
.
0

1
4
0
1
.
0
±

3
8
4
2
.
0

9
1
0
0
.
0
±

0
3
6
2
.
0

2
7
8
0
.
0
±

5
3
4
2
.
0

2
0
3
1
.
0

4
7
0
1
.
0
−
±

5
1
2
2
.
0

6
8
5
0
.
0
−
±

2
9
6
6
.
0

0
8
2
4
.
0
−
±

8
8
2
2
.
1

6
2
3
0
.
0
−
±

1
6
6
4
.
1

1
7
1
2
.
0
−
±

8
6
1
0
.
0
±

7
2
9
2
.
0

8
0
2
0
.
0
±

0
5
2
0
.
0

9
1
7
1
.
0

9
0
2
0
.
0
−
±

6
8
2
0
.
0
±

5
7
4
6
.
0

7
3
0
0
.
0
±

2
6
2
4
.
0

7
4
2
3
.
0
±

7
4
0
0
.
0

8
6
1
0
.
0
±

%
8
3
.
5
4

3
5
6
0
.
0
±

%
5
9
.
3
5

1
3
0
0
.
0
±

%
7
4
.
8
4

0
0
5
0
.
0
±

%
5
1
.
4
6

8
6
1
0
.
0
±

%
7
7
.
6
6

7
2
1
0
.
0
±

%
2
4
.
9
5

8
0
4
0
.
0
±

%
2
9
.
7
3

6
0
0
0
.
0
±

%
0
6
.
3
4

3
4
1
0
.
0
±

%
6
4
.
5
4

4
2
1
0
.
0
±

%
5
5
.
5
3

5
2
0
0
.
0
±

%
2
0
.
2
4

2
4
0
0
.
0
±

%
5
7
.
5
3

4
2
1
0
.
0
±

%
0
3
.
1
3

7
6
1
0
.
0
±

%
8
3
.
3
4

4
1
1
0
.
0
±

%
5
8
.
1
3

2
R

E
P
A
M

5
1
9
9
.
0

E
S
M

3
8
4
6
.
0

E
A
M

I
L
I

4
0
9
7
.
0

2
R

E
P
A
M

%
2
2
.
2

9
0
5
0
.
0

E
S
M

e
g
n
a
h
c
x
E

9
2
6
1
.
0

E
A
M

7
4
8
4
.
0

2
R

E
P
A
M

9
8
1
4
.
0

E
S
M

1
h
T
T
E

a
t
a
D

E
A
M

c
i
r
t
e

M

t
n
e
m

i
r
e
p
x
e

g
n
i
t
s
a
c
e
r
o
f

s
e
i
r
e
s

e
m

i
t

e
t
a
i
r
a
v
i
t
l
u
m
e
h
t

f
o

s
t
l
u
s
e
r

l
a
i
t
r
a
P

5
e
l
b
a
T

l
e
d
o
M

7
3
1
0
.
0
±

4
8
0
0
.
0
±

3
0
0
0
.
0
±

0
0
0
0
.
0
±

2
0
0
0
.
0
±

9
0
0
0
.
0
±

4
6
0
0
.
0
±

1
0
7
1
.
0
±

4
3
7
0
.
0
±

9
7
7
3
.
1

4
2
0
8
.
0

5
5
0
0
.
0
±

7
2
0
0
.
0
±

1
0
5
3
.
1

1
1
9
7
.
0

6
9
3
1
.
0
±

2
0
6
0
.
0
±

9
7
6
3
.
1

9
5
0
8
.
0

8
2
3
1
.
0
±

0
3
5
0
.
0
±

3
0
4
9
.
1

8
8
7
9
.
0

1
8
4
0
.
0
±

2
4
0
0
.
0
±

3
8
6
9
.
1

6
2
0
0
.
1

2
6
6
3
.
0
±

1
4
5
0
.
2

6
8
4
0
.
0
±

3
5
2
4
.
2

2
4
1
1
.
0
±

2
1
5
9
.
0

7
1
1
0
.
0
±

8
9
8
0
.
1

2
1
4
1
.
0
±

4
4
4
0
.
0
±

7
6
0
8
.
2

8
8
9
1
.
1

3
5
0
0
.
0
±

8
8
0
0
.
0
±

7
6
5
9
.
0

0
4
4
6
.
0

6
0
1
0
.
0
±

8
6
0
0
.
0
±

2
6
1
2
.
1

9
9
6
7
.
0

6
3
1
0
.
0
±

3
5
0
0
.
0
±

2
5
4
2
.
1

4
9
9
7
.
0

8
4
1
0
.
0
±

5
9
0
0
.
0
±

7
0
3
5
.
0

4
8
5
4
.
0

5
5
7
0
.
0
±

7
1
3
0
.
0
±

2
0
9
9
.
0

0
8
1
6
.
0

4
0
0
2
.
0
±

5
3
0
1
.
0
±

3
7
3
1
.
1

4
2
4
7
.
0

3
9
8
0
.
0

±

6
1
0
0
−
.
0
±

3
0
0
0
.
0
±

4
2
0
0
.
0
±

9
2
0
0
.
0
±

6
4
3
0
.
0
±

%
7
3
.
5

9
9
6
2
.
0

7
1
9
3
.
0

3
4
2
2
.
0

9
5
1
0
.
0
±

5
0
0
0
.
0
±

9
2
0
0
.
0
±

7
4
0
0
.
0
±

6
3
0
0
.
0
±

1
8
2
6
.
0

%
9
0
.
3

4
4
9
0
.
0

7
6
2
2
.
0

0
0
1
4
.
0

0
9
3
0
.
0
±

7
1
0
0
.
0
±

2
5
0
0
.
0
±

9
2
1
0
.
0
±

4
9
5
1
.
0
±

4
5
1
8
.
0

%
9
8
.
1

1
4
3
0
.
0

1
4
3
1
.
0

4
3
1
4
.
0

8
4
2
0
.
0
±

7
0
0
0
.
0
±

5
2
0
0
.
0
±

6
6
0
0
.
0
±

7
6
6
1
.
0
±

9
5
4
7
.
0

%
0
4
.
2

0
5
5
0
.
0

3
2
7
1
.
0

4
9
1
3
.
0

1
5
1
0
.
0
±

7
0
0
0
.
0
±

1
7
0
0
.
0
±

3
6
0
0
.
0
±

0
4
6
1
.
0
±

7
7
2
2
.
0

%
7
3
.
4

7
8
7
1
.
0

2
4
1
3
.
0

1
8
5
1
.
0

1
4
0
0
.
0
±

3
0
0
0
.
0
±

6
1
0
0
.
0
±

1
3
0
0
.
0
±

1
9
2
0
.
0
±

3
9
2
8
.
0

%
1
9
.
1

2
5
3
0
.
0

7
5
3
1
.
0

4
8
5
5
.
0

0
0
6
0
.
0
±

4
0
0
0
.
0
±

5
1
0
0
.
0
±

9
3
0
0
.
0
±

0
9
1
0
.
0
±

7
5
8
4
.
0

%
7
1
.
3

1
0
9
0
.
0

0
2
2
2
.
0

5
9
6
4
.
0

3
4
2
0
.
1
±

7
6
5
4
,
1
-

5
5
0
0
.
0
±

1
9
5
0
.
0
±

0
1
4
0
.
0
±

2
3
4
1
.
0
±

%
3
5
.
6

5
0
5
3
.
0

9
1
5
4
.
0

5
7
1
1
.
0

1
0
0
0
.
0
±

0
0
0
0
.
0
±

0
±

1
0
0
0
.
0
±

6
6
1
0
.
0
±

9
4
6
8
.
0

%
4
5
.
1

6
5
2
0
.
0

4
0
1
1
.
0

8
6
7
5
.
0

0
5
0
0
.
0
±

3
0
0
0
.
0
±

5
1
0
0
.
0
±

3
2
0
0
.
0
±

2
4
2
0
.
0
±

1
8
7
7
.
0

%
0
2
.
2

6
9
4
0
.
0

6
7
5
1
.
0

7
4
9
4
.
0

4
7
4
0
.
0
±

5
0
0
0
.
0
±

3
3
0
0
.
0
±

6
3
0
0
.
0
±

6
1
3
0
.
0
±

8
2
9
1
.
0

%
7
1
.
4

1
6
5
1
.
0

3
8
9
2
.
0

2
2
6
3
.
0

2
4
0
0
.
0
±

0
0
0
0
.
0
±

3
0
0
0
.
0
±

7
0
0
0
.
0
±

7
1
2
0
.
0
±

2
4
4
8
.
0

%
5
5
.
1

1
7
2
0
.
0

5
1
1
1
.
0

9
4
7
5
.
0

3
6
1
0
.
0
±

2
0
0
0
.
0
±

4
1
0
0
.
0
±

2
1
0
0
.
0
±

1
0
3
0
.
0
±

6
9
3
7
.
0

%
2
2
.
2

3
2
5
0
.
0

6
8
5
1
.
0

5
7
8
4
.
0

9
3
1
0
.
0
±

2
0
0
0
.
0
±

8
2
0
0
.
0
±

2
2
0
0
.
0
±

3
7
3
0
.
0
±

3
9
3
1
.
0

%
2
5
.
4

9
7
9
1
.
0

9
1
2
3
.
0

3
5
1
3
.
0

0
0
3
0
.
0
±

%
8
2
.
8
6

9
0
7
0
.
0
±

%
5
7
.
6
7

2
4
1
0
.
0
±

%
8
4
.
3
8

2
0
2
0
.
0
±

%
3
6
.
8
6

7
2
2
0
.
0
±

%
7
6
.
3
7

6
1
1
0
.
0
±

%
7
0
.
4
8

0
7
0
0
.
0
±

%
4
4
.
2
6

8
4
1
0
.
0
±

%
2
6
.
8
6

4
8
8
0
.
0
±

%
8
7
.
1
9

0
1
0
0
.
0
±

%
4
1
.
6
6

6
3
0
0
.
0
±

%
5
9
.
1
7

4
8
0
0
.
0
±

%
1
6
.
1
8

6
2
0
0
.
0
±

%
2
6
.
5
6

3
4
0
0
.
0
±

%
9
1
.
2
7

3
8
0
0
.
0
±

%
8
3
.
4
8

7
9
0
0
.
0
±

3
6
0
0
.
0
±

4
5
7
4
.
0

5
3
9
4
.
0

r
a
l
u
g
e
R

5
2
1
0
.
0
±

6
2
0
0
.
0
±

2
9
0
0
.
0
±

5
7
0
0
.
0
±

9
7
9
5
.
0

4
1
7
5
.
0

g
n
o
L

5
5
8
1
.
0
±

4
1
8
0
.
0
±

4
7
0
6
.
0

4
1
4
5
.
0

r
a
l
u
g
e
R

3
2
4
5
.
0

6
2
0
5
.
0

t
r
o
h
S

r
e
m
r
o
f
S
T
E

8
9
0
2
.
0
±

1
8
8
0
.
0
±

4
5
9
1
.
0
±

6
0
9
0
.
0
±

3
1
1
7
.
0

0
4
1
6
.
0

3
7
2
0
.
0
±

8
8
7
3
.
0

8
1
1
0
.
0
±

2
3
1
4
.
0

g
n
o
L

t
r
o
h
S

r
e
m
r
o
f
s
s
o
r
C

3
9
1
0
.
0
±

4
4
0
0
.
0
±

9
8
8
1
.
0
±

0
9
7
0
.
0
±

7
0
0
8
.
0

9
1
3
6
.
0

0
7
1
0
.
0
±

5
5
0
0
.
0
±

3
6
6
3
.
0

9
7
9
3
.
0

g
n
o
L

t
r
o
h
S

3
9
3
4
.
0

2
2
5
4
.
0

r
a
l
u
g
e
R

0
4
2
0
.
0
±

3
7
0
0
.
0
±

7
8
2
0
.
0
±

7
9
1
5
.
0

5
1
1
0
.
0
±

2
5
0
5
.
0

g
n
o
L

9
2
2
4
.
0

0
6
3
4
.
0

r
a
l
u
g
e
R

r
a
e
n
i
l

D

8
0
2
0
.
0
±

8
6
0
0
.
0
±

3
5
2
4
.
0

1
0
4
4
.
0

r
a
l
u
g
e
R

8
9
2
0
.
0
±

7
9
0
0
.
0
±

3
0
3
0
.
0
±

9
0
5
5
.
0

3
1
1
0
.
0
±

5
1
2
5
.
0

g
n
o
L

4
7
6
3
.
0

8
0
0
4
.
0

t
r
o
h
S

T
S
T
h
c
t
a
P

6
6
5
4
.
0

t
r
o
h
S

r
e
m
r
o
f
d
e
F

---

<!-- PAGE 37 -->

Page 37 of 67  23

3
8
8
5
.
0

9
8
1
1
.
0
−
±

3
1
2
5
.
1

7
6
1
1
.
0
−
±

2
6
9
2
.
2

5
8
3
1
.
0
−
±

8
6
2
0
.
0
±

5
9
7
2
.
0

7
9
5
0
.
0
±

9
6
0
2
.
0

1
5
5
0
.
0
±

2
5
3
1
.
0

2
2
2
0
.
0
±

1
1
5
5
.
0

0
6
7
0
.
0
±

3
6
3
3
.
0

6
4
5
0
.
0
±

4
6
0
2
.
0

2
7
0
0
.
0
±

%
1
5
.
0
4

4
8
0
0
.
0
±

%
2
0
.
6
4

5
1
1
0
.
0
±

%
7
6
.
1
5

4
0
4
0
.
0
±

%
8
4
.
8
5

6
9
2
0
.
0
±

%
3
2
.
0
6

0
0
2
0
.
0
±

%
1
3
.
8
4

1
3
1
0
.
0
±

%
5
1
.
4
3

3
6
8
0
.
0
±

%
6
6
.
6
4

4
7
1
0
.
0
±

%
2
0
.
5
3

2
R

E
P
A
M

1
5
9
0
.
0
±

7
3
2
0
.
0
±

5
7
0
0
.
0
±

4
0
0
0
.
0
±

3
1
0
0
.
0
±

0
3
0
0
.
0
±

2
0
0
0
.
0
±

3
1
9
0
.
0
±

4
7
2
0
.
0
±

1
7
3
5
.
2

0
3
3
1
.
1

4
8
9
0
.
0
±

6
7
2
0
.
0
±

1
4
6
1
.
3

0
7
0
3
.
1

4
0
9
0
.
0
±

2
8
2
0
.
0
±

2
0
5
3
.
1

2
0
9
7
.
0

7
1
6
0
.
0
±

9
8
2
0
.
0
±

1
0
8
4
.
1

7
9
3
8
.
0

8
6
9
0
.
0
±

2
3
3
0
.
0
±

5
5
4
5
.
1

8
3
4
8
.
0

6
1
7
0
.
0
±

2
5
0
0
.
0
±

0
0
3
7
.
0

3
9
4
5
.
0

6
9
3
2
.
0
±

3
8
7
0
.
0
±

8
0
5
1
.
1

9
9
0
7
.
0

8
1
2
1
.
0
±

7
7
2
0
.
0
±

9
9
1
3
.
1

9
7
5
7
.
0

0
1
0
0
.
0
±

1
0
0
0
.
0
±

4
0
0
0
.
0
±

3
1
0
0
.
0
±

7
9
0
0
.
0
±

4
6
7
7
.
0

%
4
2
.
2

6
0
5
0
.
0

3
0
6
1
.
0

4
8
8
1
.
0

6
9
7
1
.
0
±

9
1
0
0
.
0
±

6
1
1
0
.
0
±

6
3
1
0
.
0
±

1
7
0
0
.
0
±

5
8
1
1
.
0

%
1
3
.
4

1
6
6
1
.
0

9
6
0
3
.
0

0
2
6
0
.
0

7
4
3
0
.
0
±

7
1
0
0
.
0
±

1
0
1
0
.
0
±

7
6
1
0
.
0
±

0
9
7
0
.
0
±

4
1
5
7
.
0

%
4
4
.
2

6
9
5
0
.
0

6
8
7
1
.
0

5
5
1
4
.
0

3
7
2
0
.
0
±

0
1
0
0
.
0
±

5
6
0
0
.
0
±

0
8
0
0
.
0
±

8
4
0
0
.
0
±

5
7
5
6
.
0

%
6
9
.
2

9
6
8
0
.
0

9
5
1
2
.
0

1
3
0
4
.
0

2
5
0
2
.
0

3
9
5
1
.
0
−
±

3
4
0
0
.
0
±

1
4
4
0
.
0
±

2
3
3
0
.
0
±

7
3
1
0
.
0
±

%
4
7
.
5

7
9
9
2
.
0

9
5
1
4
.
0

5
6
2
2
.
0

2
7
0
0
.
0
±

2
0
0
0
.
0
±

8
0
0
0
.
0
±

4
1
0
0
.
0
±

4
8
0
0
.
0
±

0
6
2
8
.
0

%
8
8
.
1

5
4
3
0
.
0

4
3
3
1
.
0

3
9
2
5
.
0

6
9
1
0
.
0
±

9
0
0
0
.
0
±

1
7
0
0
.
0
±

8
8
0
0
.
0
±

2
2
1
0
.
0
±

2
0
9
6
.
0

%
8
6
.
2

0
3
7
0
.
0

1
3
9
1
.
0

0
3
1
4
.
0

1
6
7
0
.
0
±

1
2
0
0
.
0
±

3
1
2
0
.
0
±

2
6
1
0
.
0
±

9
1
7
0
.
0
±

4
7
1
0
.
0

%
2
0
.
5

8
9
3
2
.
0

7
2
6
3
.
0

1
3
1
1
.
0

1
9
3
8
.
1

E
S
M

4
7
4
9
.
0

E
A
M

I
L
I

2
8
5
8
.
0

2
R

E
P
A
M

%
7
5
.
1

8
6
2
0
.
0

E
S
M

e
g
n
a
h
c
x
E

2
3
1
1
.
0

E
A
M

0
1
1
5
.
0

2
R

E
P
A
M

5
2
0
0
.
0
±

3
6
0
8
.
0

1
3
0
0
.
0
±

4
1
0
8
.
0

3
8
7
1
.
0
±

1
1
9
5
.
0

8
1
0
0
.
0
±

%
2
0
.
7
1

3
1
0
0
.
0
±

%
1
9
.
6
1

0
5
6
0
.
0
±

%
8
1
.
6
2

2
R

E
P
A
M

4
2
0
0
.
0
±

9
1
0
0
.
0
±

4
1
0
0
.
0
±

0
3
0
0
.
0
±

8
2
0
0
.
0
±

4
6
0
0
.
0
±

4
2
9
1
.
0

9
0
0
3
.
0

7
2
7
6
.
0

9
1
7
1
.
0
±

0
0
3
1
.
0
±

3
1
0
0
.
0
±

2
4
9
3
.
0

6
4
6
4
.
0

3
8
5
6
.
0

7
7
8
1
.
0

E
S
M

3
7
9
2
.
0

E
A
M

y
t
i
c
i
r
t
c
e
l
E

4
7
7
6
.
0

2
R

E
P
A
M

1
9
0
0
.
0
±

%
4
4
.
1
6

7
6
0
0
.
0
±

%
8
2
.
0
9

5
2
0
0
.
0
±

%
4
1
.
9
9

8
0
4
0
.
0
±

%
7
6
.
8
6

4
5
0
0
.
0
±

%
2
3
.
5
7

8
1
1
0
.
0
±

%
4
1
.
7
8

5
4
0
0
.
0
±

%
7
0
.
0
7

2
3
0
0
.
0
±

%
6
2
.
7
7

1
1
2
0
.
0
±

%
4
7
.
4
8

0
1
0
0
.
0
±

%
1
2
.
8
1

1
3
0
0
.
0
±

%
9
9
.
7
1

3
1
0
0
.
0
±

%
4
3
.
8
1

3
5
3
4
.
0

E
S
M

1
h
T
T
E

a
t
a
D

E
A
M

c
i
r
t
e

M

9
7
5
4
.
0

t
r
o
h
S

1
1
0
0
.
0
±

6
0
0
0
.
0
±

9
4
9
7
.
0

8
2
1
6
.
0

r
a
l
u
g
e
R

6
5
0
0
.
0
±

3
1
0
0
.
0
±

2
5
0
0
.
0
±

6
0
0
0
.
0
±

8
0
9
8
.
0

2
8
6
6
.
0

g
n
o
L

S
T
A
E
B
N

-

l
e
d
o
M

1
1
8
0
.
0
±

3
6
4
0
.
0
±

6
9
7
4
.
0

0
7
9
4
.
0

r
a
l
u
g
e
R

9
7
1
0
.
0
±

4
6
0
0
.
0
±

0
1
3
0
.
0
±

5
9
0
0
.
0
±

8
2
1
6
.
0

6
6
7
5
.
0

g
n
o
L

1
6
9
4
.
0

1
4
0
5
.
0

t
r
o
h
S

r
e
m
r
o
f
o
t
u
A

7
9
1
4
.
0

6
0
3
4
.
0

t
r
o
h
S

r
e
m
r
o
f
s
n
a
r
T
-
S
N

)
d
e
u
n
i
t
n
o
c
(

5
e
l
b
a
T

8
8
0
0
.
0
±

2
6
0
0
.
0
±

6
4
9
4
.
0

2
1
8
4
.
0

r
a
l
u
g
e
R

7
3
0
0
.
0
±

2
7
0
0
.
0
±

7
8
5
3
.
0
±

4
5
1
0
.
0
±

4
7
0
7
.
0

0
7
0
6
.
0

3
9
6
3
.
0

E
S
M

c
ffi
a
r
T

E
A
M

9
6
1
3
.
0

g
n
o
L

c
i
r
t
e

M

t
r
o
h
S

a
t
a
D

1
1
0
0
.
0
±

0
1
0
0
.
0
±

9
9
6
3
.
0

2
7
1
3
.
0

r
a
l
u
g
e
R

8
2
0
0
.
0
±

5
3
0
0
.
0
±

7
2
0
0
.
0
±

5
1
0
0
.
0
±

6
7
8
3
.
0

4
3
2
3
.
0

g
n
o
L

r
e
m
r
o
f
d
e
F

l
e
d
o
M

---

<!-- PAGE 38 -->

23  Page 38 of 67

8
1
0
0
.
0
±

8
6
7
7
.
0

0
1
0
0
.
0
±

2
9
4
7
.
0

2
1
0
0
.
0
±

1
7
0
7
.
0

5
5
0
0
.
0
±

6
9
4
8
.
0

2
8
0
0
.
0
±

1
0
3
8
.
0

3
7
0
0
.
0
±

7
0
9
7
.
0

3
0
0
0
.
0
±

2
3
8
7
.
0

4
1
0
0
.
0
±

3
4
9
7
.
0

2
0
0
0
.
0
±

1
3
8
7
.
0

8
0
0
0
.
0
±

1
8
0
8
.
0

2
0
0
0
.
0
±

9
4
0
8
.
0

3
0
0
0
.
0
±

4
3
8
7
.
0

1
1
0
0
.
0
±

4
5
0
7
.
0

3
2
0
0
.
0
±

0
6
5
1
.
0

4
0
0
0
.
0
±

5
3
6
0
.
0

4
0
0
0
.
0
±

%
8
1
.
9
1

4
0
0
0
.
0
±

%
5
3
.
0
2

5
0
0
0
.
0
±

%
1
9
.
1
2

2
2
0
0
.
0
±

%
8
8
.
0
1

2
3
0
0
.
0
±

%
7
5
.
1
1

3
3
0
0
.
0
±

%
8
4
.
3
1

3
0
0
0
.
0
±

%
8
8
.
4
1

7
1
0
0
.
0
±

%
9
8
.
4
1

%
8
9
.
4
1

1
0
0
.
0
±

1
1
0
0
.
0
±

%
9
3
.
4
1

4
0
0
0
.
0
±

%
5
0
.
4
1

1
0
0
0
.
0
±

%
0
2
.
4
1

4
1
0
0
.
0
±

%
3
7
.
8
1

6
1
0
0
.
0
±

%
1
2
.
9
3

5
1
0
0
.
0
±

%
9
7
.
1
4

2
R

E
P
A
M

0
1
0
0
.
0
±

9
0
0
0
.
0
±

1
4
1
0
.
0
±

0
3
4
2
.
0

0
7
3
3
.
0

3
8
4
4
.
0

2
1
0
0
.
0
±

6
0
0
0
.
0
±

4
2
2
0
.
0
±

4
2
8
2
.
0

2
4
6
3
.
0

9
5
0
4
.
0

4
5
0
0
.
0
±

9
3
0
0
.
0
±

4
2
0
0
.
0
±

8
5
4
1
.
0

2
4
3
2
.
0

9
2
3
7
.
0

0
8
0
0
.
0
±

6
4
0
0
.
0
±

3
1
0
0
.
0
±

7
4
6
1
.
0

5
8
4
2
.
0

8
9
9
6
.
0

3
6
1
2
.
0

E
S
M

5
8
1
3
.
0

E
A
M

7
1
0
0
.
0
±

5
0
0
0
.
0
±

y
t
i
c
i
r
t
c
e
l
E

9
1
1
0
.
0
±

3
2
6
4
.
0

2
R

E
P
A
M

8
5
0
0
.
0
±

%
4
6
.
7
2

8
0
0
0
.
0
±

%
7
5
.
7
2

1
5
0
0
.
0
±

%
5
3
.
7
2

1
0
0
0
.
0
±

%
9
2
.
5
1

1
0
0
0
.
0
±

%
6
2
.
7
1

6
1
0
0
.
0
±

5
1
0
0
.
0
±

2
5
4
3
.
0

8
1
7
2
.
0

r
a
l
u
g
e
R

8
7
0
6
.
0

E
S
M

c
ffi
a
r
T

E
A
M

2
5
6
4
.
0

c
i
r
t
e

M

t
r
o
h
S

a
t
a
D

2
4
1
0
.
0
±

1
4
1
0
.
0
±

1
2
7
4
.
0

1
2
7
4
.
0

r
a
l
u
g
e
R

r
e
m
r
o
f
S
T
E

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

5
e
l
b
a
T

3
8
0
0
.
0
±

3
8
0
0
.
0
±

5
5
2
0
.
0
±

9
9
0
0
.
0
±

9
9
7
6
.
0

0
0
8
4
.
0

0
3
0
0
.
0
±

3
2
0
0
.
0
±

5
8
0
3
.
0

3
5
4
2
.
0

g
n
o
L

t
r
o
h
S

r
e
m
r
o
f
s
s
o
r
C

1
7
0
0
.
0
±

2
2
0
2
.
0

5
4
0
0
.
0
±

2
8
8
2
.
0

–

–

–

–

g
n
o
L

3
0
0
0
.
0
±

3
0
0
0
.
0
±

3
0
0
0
.
0
±

4
0
0
2
.
0

6
7
6
2
.
0

1
3
2
5
.
0

3
1
0
0
.
0
±

0
2
0
0
.
0
±

3
0
0
0
.
0
±

2
9
9
1
.
0

1
4
7
2
.
0

8
4
5
5
.
0

2
0
0
0
.
0
±

1
0
0
0
.
0
±

1
0
0
0
.
0
±

5
9
0
2
.
0

6
1
9
2
.
0

5
5
9
5
.
0

8
0
0
0
.
0
±

2
1
0
0
.
0
±

0
6
8
1
.
0

4
7
5
2
.
0

9
1
0
0
.
0
±

7
4
0
7
.
0

2
0
0
0
.
0
±

4
0
0
0
.
0
±

2
1
0
0
.
0
±

1
9
8
1
.
0

1
3
6
2
.
0

8
4
8
6
.
0

2
0
0
0
.
0
±

2
9
0
2
.
0

1
6
8
2
.
0

6
8
6
6
.
0

0
±

2
0
0
0
.
0
±

1
1
0
0
.
0
±

7
0
0
0
.
0
±

9
2
0
0
.
0
±

5
5
8
2
.
0

0
6
7
3
.
0

7
1
7
4
.
0

2
2
0
0
.
0
±

1
0
0
0
.
0
±

5
0
0
0
.
0
±

6
7
1
8
.
0

3
0
9
6
.
0

1
5
6
0
.
0

3
0
0
0
.
0
±

5
0
0
0
.
0
±

8
0
0
0
.
0
±

4
4
0
9
.
0

4
7
3
7
.
0

2
1
0
0
.
0

2
0
0
0
.
0
±

%
3
8
.
4
2

1
0
0
0
.
0
±

%
2
9
.
2
2

5
0
0
0
.
0
±

%
1
5
.
1
2

5
0
0
0
.
0
±

%
3
0
.
7
1

5
0
0
0
.
0
±

%
7
5
.
7
1

%
0
0
.
8
1

3
0
0
0
.
0

6
0
0
0
.
0
±

%
1
9
.
4
2

9
0
0
0
.
0
±

%
0
4
.
1
3

6
1
0
0
.
0
±

%
8
7
.
1
3

2
2
0
0
.
0
±

0
1
0
0
.
0
±

5
1
6
3
.
0

5
5
7
2
.
0

r
a
l
u
g
e
R

4
1
0
0
.
0
±

3
1
0
0
.
0
±

2
0
0
0
.
0
±

3
0
0
0
.
0
±

7
5
8
3
.
0

5
3
8
2
.
0

g
n
o
L

3
0
0
0
.
0
±

2
0
0
0
.
0
±

5
7
0
5
.
0

8
7
4
3
.
0

r
a
l
u
g
e
R

3
0
0
0
.
0
±

2
0
0
0
.
0
±

1
0
0
0
.
0
±

2
0
0
0
.
0
±

1
8
6
4
.
0

2
9
2
3
.
0

g
n
o
L

7
1
4
5
.
0

8
3
7
3
.
0

t
r
o
h
S

r
a
e
n
i
l

D

9
7
3
3
.
0

4
5
6
2
.
0

t
r
o
h
S

T
S
T
h
c
t
a
P

3
3
0
0
.
0
±

8
0
0
0
.
0
±

8
1
4
0
.
1

2
6
8
6
.
0

r
a
l
u
g
e
R

5
0
0
0
.
0
±

2
0
0
0
.
0
±

7
0
0
0
.
0
±

0
2
0
0
.
0
±

8
7
2
1
.
1

0
0
4
7
.
0

g
n
o
L

6
8
0
6
.
0

6
8
8
3
.
0

t
r
o
h
S

S
T
A
E
B
N

-

---

<!-- PAGE 39 -->

Page 39 of 67  23

d
i
l
a
v

o
n

t
a
h
t

s
e
t
a
c
i
d
n
i

"
–
"

.
c
i
l
a
t
i

a

h
t
i

w
d
e
t
h
g
i
l
h
g
i
h

e
r
a

s
t
l
u
s
e
r

t
s
e
b

d
n
o
c
e
s

e
h
t

d
n
a

d
l
o
b

n
i

d
e
t
h
g
i
l
h
g
i
h

e
r
a

s
t
l
u
s
e
r

t
s
e
b

e
h
T

-
g
n
o
l

d
n
a

,

m

r
e
t
-
r
a
l
u
g
e
r

,

m

r
e
t
-
t
r
o
h
s

r
o
f

O
h
t
g
n
e
l

t
u
p
t
u
o

e
h
t

e
t
o
n
e
d

’
g
n
o
L
’

d
n
a

’
,
r
a
l
u
g
e
R

’

’
,
t
r
o
h
S
’

.
d
e
n
i
a
t
b
o

e
b

d
l
u
o
c

s
t
l
u
s
e
r

s
t
n
e
m

i
r
e
p
x
e

f
o

n
o
i
t
a
i
v
e
d

d
r
a
d
n
a
t
s

d
n
a

e
u
l
a
v
e
g
a
r
e
v
a

e
h
t

t
r
o
p
e
r

e

W

.
n
o
i
t
c
i
d
e
r
p

s
e
i
r
e
s

e
m

i
t

m

r
e
t

7
4
0
0
.
0
±

7
1
0
8
.
0

3
1
0
0
.
0
±

9
1
9
7
.
0

9
9
1
0
.
0
±

8
9
2
7
.
0

7
1
0
0
.
0
±

1
1
3
8
.
0

9
1
0
0
.
0
±

9
5
1
8
.
0

7
5
0
0
.
0
±

5
7
8
7
.
0

1
3
0
0
.
0
±

%
3
5
.
7
1

2
0
0
0
.
0
±

%
4
4
.
7
1

8
6
0
0
.
0
±

%
7
3
.
0
2

5
0
0
0
.
0
±

%
2
2
.
3
1

6
1
0
0
.
0
±

%
2
6
.
3
1

8
1
0
0
.
0
±

%
2
5
.
4
1

2
R

E
P
A
M

2
2
9
1
.
0

E
S
M

5
0
0
3
.
0

E
A
M

y
t
i
c
i
r
t
c
e
l
E

9
4
6
6
.
0

2
R

E
P
A
M

5
4
0
0
.
0
±

4
4
0
0
.
0
±

3
6
0
0
.
0
±

2
1
0
0
.
0
±

9
1
0
0
.
0
±

5
7
1
0
.
0
±

6
1
0
2
.
0

9
8
0
3
.
0

0
6
2
6
.
0

2
9
1
0
.
0
±

6
4
1
0
.
0
±

2
6
0
0
.
0
±

9
0
6
2
.
0

7
7
5
3
.
0

9
8
3
6
.
0

7
1
0
0
.
0
±

4
1
0
0
.
0
±

3
6
0
0
.
0
±

7
3
6
1
.
0

6
4
6
2
.
0

8
7
9
6
.
0

9
1
0
0
.
0
±

0
2
0
0
.
0
±

0
6
0
0
.
0
±

4
8
7
1
.
0

1
7
7
2
.
0

6
8
7
6
.
0

5
5
0
0
.
0
±

2
5
0
0
.
0
±

3
0
0
0
.
0
±

2
5
0
2
.
0

4
2
0
3
.
0

7
8
5
6
.
0

4
0
0
0
.
0
±

%
9
8
.
7
1

7
1
0
0
.
0
±

%
7
2
.
9
1

1
2
0
0
.
0
±

%
2
8
.
9
1

1
1
0
0
.
0
±

%
4
3
.
7
1

3
1
0
0
.
0
±

%
4
4
.
8
1

6
5
1
0
.
0
±

%
2
0
.
1
2

1
5
0
0
.
0
±

8
2
0
0
.
0
±

2
0
2
4
.
0

9
1
4
3
.
0

r
a
l
u
g
e
R

6
0
2
0
.
0
±

8
8
0
0
.
0
±

6
6
0
0
.
0
±

7
7
0
0
.
0
±

5
9
0
4
.
0

3
9
3
3
.
0

g
n
o
L

4
4
7
3
.
0

E
S
M

c
ffi
a
r
T

E
A
M

5
7
1
3
.
0

c
i
r
t
e

M

t
r
o
h
S

a
t
a
D

r
e
m
r
o
f
o
t
u
A

l
e
d
o
M

)
d
e
u
n
i
t
n
o
c
(

5
e
l
b
a
T

1
7
0
0
.
0
±

3
4
0
0
.
0
±

8
1
7
3
.
0

6
4
0
3
.
0

r
a
l
u
g
e
R

8
6
0
0
.
0
±

4
4
0
0
.
0
±

1
0
0
0
.
0
±

0
1
0
0
.
0
±

8
0
0
4
.
0

2
0
2
3
.
0

g
n
o
L

1
9
4
3
.
0

0
1
9
2
.
0

t
r
o
h
S

r
e
m
r
o
f
s
n
a
r
T
-
S
N

---

<!-- PAGE 40 -->

23  Page 40 of 67

0
7
9
0
.
0
−

1
4
2
6
.
0
±

9
7
1
9
.
0

2
7
8
5
.
1
−
±

4
5
4
2
.
6

5
2
0
4
.
5
−
±

3
9
7
5
.
0

9
7
9
7
.
0
−
±

9
9
2
0
.
1

7
9
3
6
.
0
−
±

0
0
2
6
.
5

3
7
9
3
.
4
−
±

1
9
9
6
.
8

9
0
0
7
.
7
−
±

4
4
7
9
.
6

0
9
9
.
2
−
±

2
R

8
7
5
8
.
9
1

3
6
7
3
.
3
1
−
±

8
7
4
2
.
2

2
6
5
8
.
1
−
±

5
1
1
7
.
5

9
3
4
1
.
4
−
±

5
8
2
7
.
3
1

1
2
2
1
.
0
1
−
±

E
P
A
M

%
3
6
.
7

6
6
4
2
.
0

E
S
M

3
5
0
4
.
0

E
A
M

I
L
I

0
6
4
8
.
0

2
R

E
P
A
M

%
5
4
.
1

1
8
2
0
.
0

E
S
M

e
g
n
a
h
c
x
E

8
9
2
1
.
0

E
A
M

9
3
2
5
.
0

2
R

E
P
A
M

2
9
9
1
.
0

E
S
M

1
h
T
T
E

a
t
a
D

E
A
M

c
i
r
t
e

M

t
n
e
m

i
r
e
p
x
e

g
n
i
t
s
a
c
e
r
o
f

s
e
i
r
e
s

e
m

i
t

e
t
a
i
r
a
v
i
n
u

e
h
t

f
o

s
t
l
u
s
e
r

l
a
i
t
r
a
P

6
e
l
b
a
T

l
e
d
o
M

0
3
0
0
.
0
±

1
5
7
0
.
0
±

3
3
9
0
.
0
±

7
3
0
0
.
0
±

0
0
0
0
.
0
±

7
0
0
0
.
0
±

5
1
0
0
.
0
±

9
5
0
0
.
0
±

7
7
0
0
.
0
±

6
5
7
1
.
0
±

4
0
5
1
.
0
±

3
0
2
0
.
0
±

6
0
0
0
.
0
±

6
3
0
0
.
0
±

8
5
0
0
.
0
±

%
5
9
.
8

7
8
9
2
.
0

3
9
4
4
.
0

1
8
5
6
.
0

%
9
1
.
2

7
1
6
0
.
0

0
3
9
1
.
0

3
1
1
0
.
0
±

9
8
6
4
.
0

6
0
0
0
.
0
±

%
7
6
.
0
1

7
5
0
0
.
0
±

%
1
3
.
1
1

8
4
1
0
.
0
±

%
0
7
.
6
1

2
2
2
0
.
0
±

%
4
0
.
6
1

9
8
3
0
.
0
±

%
7
1
.
5
2

2
1
0
0
.
0
±

%
3
2
.
0
3

5
1
1
0
.
0
±

%
3
6
.
8
2

7
2
0
0
.
0
±

%
3
4
.
4
1

7
3
0
0
.
0
±

%
9
6
.
9
1

1
1
0
0
.
0
±

%
1
1
.
1
2

1
2
8
1
.
0
±

6
2
3
1
.
0
±

6
6
4
4
.
0

5
9
5
5
.
0

2
3
9
1
.
0

2
9
5
0
.
0
−
±

6
0
0
0
.
0
±

7
9
0
0
.
0
±

9
6
0
0
.
0
±

8
6
1
0
.
0
±

%
7
9
.
3

5
6
0
2
.
0

1
5
5
3
.
0

9
3
0
3
.
0

1
7
8
0
.
0
±

9
2
6
0
.
0
±

6
6
0
0
.
0
±

4
0
0
0
.
0
±

2
1
0
0
.
0
±

1
5
0
0
.
0
±

7
1
2
0
.
0
±

4
4
7
3
.
0

0
9
7
4
.
0

9
4
0
9
.
0

%
5
1
.
1

4
7
1
0
.
0

4
4
0
1
.
0

3
3
2
5
.
0

7
4
0
1
.
0
±

3
8
5
0
.
0
±

7
6
1
0
.
0
±

8
0
0
0
.
0
±

0
3
0
0
.
0
±

5
8
0
0
.
0
±

2
9
3
0
.
0
±

4
6
1
4
.
0

1
1
4
5
.
0

1
3
2
8
.
0

%
3
5
.
1

9
1
3
0
.
0

6
8
3
1
.
0

3
0
5
4
.
0

6
5
6
1
.
0
±

0
3
2
5
.
0

0
1
1
1
.
0
±

2
0
3
6
.
0

6
7
6
0
.
0
±

4
2
0
0
.
0
±

0
3
1
0
.
0
±

9
9
2
0
.
0
±

2
4
9
0
.
0
±

8
7
1
4
.
0

%
1
8
.
2

4
1
0
1
.
0

9
5
5
2
.
0

4
7
4
2
.
0

2
6
3
4
.
1
±

2
6
4
3
.
0
±

5
5
1
0
.
0
±

0
1
0
0
.
0
±

8
2
0
0
.
0
±

6
1
1
0
.
0
±

4
5
1
0
.
0
±

8
4
8
1
.
2

1
2
8
1
.
1

1
2
7
8
.
0

%
5
3
.
1

3
3
2
0
.
0

9
2
2
1
.
0

7
2
6
5
.
0

0
7
4
3
.
0
±

8
4
5
5
.
1

1
1
8
0
.
0
±

0
8
4
1
.
1

3
7
3
0
.
0
±

3
1
0
0
.
0
±

8
6
0
0
.
0
±

9
5
1
0
.
0
±

0
9
2
7
.
0

%
6
9
.
1

9
8
4
0
.
0

1
1
8
1
.
0

7
1
1
0
.
0
±

8
2
9
4
.
0

5
7
1
1
.
0
±

9
0
7
0
.
0
±

5
1
1
0
.
0
±

3
0
0
0
.
0
±

1
1
0
0
.
0
±

4
5
0
0
.
0
±

7
8
1
0
.
0
±

8
3
1
5
.
1

6
0
6
1
.
1

2
3
3
3
.
0

%
9
1
.
3

2
7
1
1
.
0

6
3
9
2
.
0

7
7
5
2
.
0

6
9
9
1
.
0
±

9
7
3
1
.
0
±

3
0
0
0
.
0
±

0
0
0
0
.
0
±

1
2
1
7
.
0

0
7
9
6
.
0

1
1
2
9
.
0

%
2
0
.
1

1
0
0
0
.
0
±

4
4
1
0
.
0

2
0
0
0
.
0
±

7
2
9
0
.
0

1
2
7
2
.
0
±

3
6
4
1
.
0
±

5
3
2
0
.
0
±

3
0
0
0
.
0
±

2
8
1
0
.
0
±

4
4
3
0
.
0
±

2
3
0
1
.
1

3
7
3
9
.
0

2
6
5
6
.
0

%
9
4
.
1

9
2
5
0
.
0

8
6
7
1
.
0

8
9
1
2
.
0
±

6
7
0
1
.
0
±

2
5
2
0
.
1

0
4
3
9
.
0

9
1
5
0
.
0
±

6
0
5
4
.
0

7
0
0
0
.
0
±

%
4
7
.
2

6
9
9
0
.
0

5
8
0
0
.
0

7
7
0
0
.
0
±

5
6
4
2
.
0

4
8
1
0
.
0
±

7
6
8
5
.
0

6
9
1
0
.
0
±

1
3
3
5
.
0

0
0
2
0
.
0
±

8
4
8
3
.
0

0
9
0
0
.
0
±

%
6
0
.
0
2

1
0
1
0
.
0
±

%
3
9
.
1
2

2
1
0
0
.
0
±

%
4
4
.
3
2

8
0
0
0
.
0
±

%
4
9
.
9
1

6
2
0
0
.
0
±

%
7
3
.
1
2

4
9
0
0
.
0
±

%
6
5
.
3
2

5
2
0
0
.
0
±

%
6
3
.
9
1

8
2
0
0
.
0
±

%
4
4
.
0
2

0
4
0
0
.
0
±

%
6
8
.
4
2

5
3
0
0
.
0
±

%
8
3
.
8
1

4
4
0
0
.
0
±

%
6
6
.
9
1

2
6
0
0
.
0
±

%
3
9
.
1
2

5
2
0
0
.
0
±

7
2
0
0
.
0
±

0
2
2
2
.
0

5
5
5
3
.
0

r
a
l
u
g
e
R

8
4
0
0
.
0
±

3
5
0
0
.
0
±

4
5
0
0
.
0
±

9
3
0
0
.
0
±

7
7
7
2
.
0

1
0
0
4
.
0

g
n
o
L

5
8
0
0
.
0
±

6
0
1
0
.
0
±

8
9
2
2
.
0

4
0
6
3
.
0

r
a
l
u
g
e
R

4
6
1
0
.
0
±

8
4
1
0
.
0
±

3
0
4
0
.
0
±

3
8
2
0
.
0
±

5
0
0
3
.
0

4
9
1
4
.
0

g
n
o
L

4
9
9
1
.
0

9
2
3
3
.
0

t
r
o
h
S

r
e
m
r
o
f
S
T
E

1
6
0
0
.
0
±

4
5
0
0
.
0
±

0
2
1
2
.
0

4
0
4
3
.
0

r
a
l
u
g
e
R

9
2
8
1
.
0

6
4
1
3
.
0

t
r
o
h
S

r
e
m
r
o
f
s
s
o
r
C

5
2
3
3
.
0

t
r
o
h
S

r
e
m
r
o
f
d
e
F

9
4
0
0
.
0
±

1
3
0
0
.
0
±

7
5
0
0
.
0
±

6
5
0
0
.
0
±

0
6
9
2
.
0

2
9
1
4
.
0

2
7
0
0
.
0
±

9
2
7
1
.
0

2
8
0
0
.
0
±

2
5
9
1
.
0

4
0
1
0
.
0
±

5
5
4
2
.
0

9
6
0
0
.
0
±

7
8
9
2
.
0

7
6
0
0
.
0
±

9
8
0
0
.
0
±

2
1
7
3
.
0

g
n
o
L

4
1
2
3
.
0

r
a
l
u
g
e
R

g
n
o
L

t
r
o
h
S

r
a
e
n
i
l

D

---

<!-- PAGE 41 -->

3
7
2
3
.
0
±

9
1
0
3
.
0

6
6
0
3
.
0
−

9
5
5
7
.
0
±

4
3
4
5
.
4
−

7
3
1
9
.
3
±

2
R

2
3
4
7
.
6

1
4
0
9
.
3
−
±

1
5
5
4
.
9
1

6
2
9
1
.
2
1
−
±

7
0
5
4
.
5
3

4
8
4
4
.
3
2
−
±

6
8
9
3
.
0

2
4
1
9
.
0
−
±

7
9
4
4
.
1

5
0
7
4
.
1
−
±

1
3
2
6
.
6

1
3
0
6
.
5
−
±

3
6
3
1
.
0

3
9
0
9
.
0
−
±

5
4
5
6
.
0
−

7
2
4
9
.
0
±

9
1
3
4
.
2
−

2
9
3
1
.
2
±

Page 41 of 67  23

E
P
A
M

%
4
5
.
6

2
1
0
0
.
0
±

0
3
0
0
.
0
±

%
6
2
.
9

4
1
0
0
.
0
±

%
8
3
.
1
1

0
0
1
0
.
0
±

%
6
1
.
7
2

8
7
0
0
.
0
±

%
3
3
.
4
3

4
7
0
0
.
0
±

%
1
1
.
5
3

5
4
6
0
.
0
±

2
6
2
0
.
0
±

6
5
0
0
.
0
±

1
0
0
0
.
0
±

0
1
0
0
.
0
±

9
0
0
0
.
0
±

9
8
2
0
.
0
±

0
4
4
3
.
0

4
0
6
4
.
0

9
0
6
3
.
0

%
7
7
.
2

3
1
1
1
.
0

1
8
4
2
.
0

4
9
7
3
.
0

3
1
8
3
.
0
±

8
7
7
1
.
0
±

5
6
6
4
.
0
±

3
0
0
0
.
0
±

1
1
0
0
.
0
±

0
4
0
0
.
0
±

3
7
0
0
.
0
±

5
5
1
8
.
1

7
4
6
2
.
1

9
3
4
6
.
0

%
6
0
.
1

3
5
1
0
.
0

9
5
9
0
.
0

6
8
6
5
.
0

0
1
1
7
.
0
±

2
0
1
4
.
3

1
1
6
2
.
0
±

3
0
3
7
.
1

4
3
0
0
.
0
±

2
0
0
0
.
0
±

6
0
0
0
.
0
±

6
2
0
0
.
0
±

8
2
0
0
.
0
±

2
2
2
8
.
0

%
3
5
.
1

1
2
3
0
.
0

3
8
3
1
.
0

0
0
4
4
.
0

6
4
1
3
.
0
±

0
4
3
1
.
0
±

1
0
3
1
.
0
±

4
2
0
0
.
0
±

5
9
3
6
.
2

4
5
4
5
.
1

6
2
3
4
.
0

%
1
7
.
2

8
2
2
0
.
0
±

6
8
9
0
.
0

4
9
2
0
.
0
±

6
3
1
0
.
0
±

8
6
4
2
.
0

9
8
8
2
.
0

7
1
2
0
.
0
±

4
1
6
1
.
0

3
3
4
0
.
0
±

3
3
2
2
.
0

E
S
M

8
0
3
0
.
0
±

4
7
8
2
.
0

6
9
1
0
.
0
±

2
4
5
3
.
0

E
A
M

I
L
I

5
1
0
0
.
0
±

1
0
0
0
.
0
±

3
0
0
0
.
0
±

9
0
0
0
.
0
±

1
6
1
0
.
0
±

6
1
0
0
.
0
±

1
5
2
8
.
0

1
0
0
0
.
0
±

%
0
5
.
1

3
0
0
0
.
0
±

5
1
3
0
.
0

0
1
0
0
.
0
±

2
5
3
1
.
0

1
7
1
0
.
0
±

3
6
1
5
.
0

3
7
1
9
.
0

2
R

E
P
A
M

%
5
0
.
1

1
5
1
0
.
0

E
S
M

e
g
n
a
h
c
x
E

8
4
9
0
.
0

E
A
M

9
5
7
5
.
0

2
R

E
P
A
M

5
6
0
0
.
0
±

3
4
3
1
.
0
±

%
9
2
.
9

5
0
1
3
.
0

6
8
1
1
.
0
±

8
4
3
4
.
0

5
3
9
0
.
0
±

0
3
0
0
.
0
±

0
7
1
0
.
0
±

3
4
3
0
.
0
±

7
9
2
0
.
0
±

5
5
8
7
.
0

%
0
7
.
1

1
9
3
0
.
0

7
3
5
1
.
0

0
9
8
4
.
0

1
4
1
0
.
0
±

%
7
2
.
0
1

0
3
0
0
.
0
±

%
2
3
.
1
1

4
0
0
1
.
0
±

6
5
9
0
.
0
±

2
2
4
0
.
0
±

2
1
0
0
.
0
±

6
7
0
0
.
0
±

7
2
1
0
.
0
±

3
7
1
0
.
0
±

1
3
2
4
.
0

9
0
4
5
.
0

0
3
2
7
.
0

%
1
9
.
1

5
0
.
0

7
2
7
1
.
0

6
5
4
4
.
0

4
2
9
1
.
0
±

5
2
6
1
.
0
±

3
3
6
4
.
0
±

6
7
0
0
.
0
±

9
0
8
0
.
0
±

6
4
8
0
.
0
±

2
6
6
0
.
0
±

7
4
9
4
.
0

9
7
0
6
.
0

2
3
0
4
.
0

%
0
4
.
4

1
1
4
2
.
0

1
4
9
3
.
0

3
3
9
2
.
0

5
2
0
0
.
0
±

9
6
5
1
.
0
±

3
6
3
1
.
0
±

1
7
0
0
.
0
±

4
0
0
0
.
0
±

3
1
0
0
.
0
±

0
4
0
0
.
0
±

1
9
0
0
.
0
±

%
8
0
.
7

0
3
5
2
.
0

9
6
8
3
.
0

4
3
8
8
.
0

%
5
2
.
1

3
1
2
0
.
0

5
2
1
1
.
0

7
4
6
5
.
0

4
0
0
0
.
0
±

%
4
0
.
0
1

7
2
0
0
.
0
±

%
4
1
.
2
1

3
9
4
0
.
0
±

8
4
3
0
.
0
±

1
5
6
0
.
0
±

6
0
0
0
.
0
±

4
4
0
0
.
0
±

9
6
0
0
.
0
±

9
4
1
0
.
0
±

0
4
8
2
.
0

7
0
1
4
.
0

1
3
2
1
.
0

%
6
8
.
1

4
9
4
0
.
0

3
8
6
1
.
0

0
5
8
4
.
0

8
5
5
0
.
0
±

9
6
5
2
.
0

7
1
6
0
.
0
±

5
6
1
4
.
0

5
2
2
0
.
0

4
4
9
0
.
0
−
±

4
1
0
0
.
0
±

9
5
1
0
.
0
±

9
4
1
0
.
0
±

6
7
6
2
.
0
±

%
8
5
.
3

4
6
7
1
.
0

6
0
2
3
.
0

2
9
8
1
.
0

8
2
0
0
.
0
±

%
1
6
.
8
1

4
3
0
0
.
0
±

%
7
9
.
9
1

5
6
0
0
.
0
±

%
6
9
.
1
2

7
1
0
0
.
0
±

%
4
3
.
9
1

8
3
0
0
.
0
±

%
1
5
.
2
2

7
4
0
0
.
0
±

%
0
5
.
4
2

5
6
0
0
.
0
±

%
6
0
.
1
2

3
5
0
0
.
0
±

%
3
7
.
1
2

2
5
0
0
.
0
±

%
0
7
.
3
2

5
8
0
0
.
0
±

%
9
8
.
9
1

1
1
0
0
.
0
±

%
9
2
.
1
2

5
5
2
0
.
0
±

%
2
9
.
7
2

4
7
7
1
.
0

E
S
M

1
h
T
T
E

a
t
a
D

E
A
M

c
i
r
t
e

M

1
3
0
3
.
0

t
r
o
h
S

2
6
0
0
.
0
±

6
5
0
0
.
0
±

1
2
0
2
.
0

6
7
2
3
.
0

r
a
l
u
g
e
R

1
7
0
0
.
0
±

3
5
0
0
.
0
±

0
4
1
0
.
0
±

8
7
4
2
.
0

3
1
1
0
.
0
±

3
9
6
3
.
0

g
n
o
L

T
S
T
h
c
t
a
P

l
e
d
o
M

8
1
1
0
.
0
±

5
5
0
0
.
0
±

7
1
3
2
.
0

4
3
6
3
.
0

r
a
l
u
g
e
R

2
7
0
0
.
0
±

3
9
0
0
.
0
±

3
5
2
0
.
0
±

4
8
1
0
.
0
±

9
1
8
2
.
0

1
4
0
4
.
0

g
n
o
L

5
2
0
0
.
0
±

9
2
0
0
.
0
±

2
1
0
0
.
0
±

6
1
0
0
.
0
±

1
4
3
2
.
0

0
6
6
3
.
0

r
a
l
u
g
e
R

2
3
0
0
.
0
±

3
0
0
0
.
0
±

7
3
8
2
.
0

4
1
1
4
.
0

g
n
o
L

5
0
8
1
.
0

9
1
1
3
.
0

t
r
o
h
S

S
T
A
E
B
N

-

8
3
1
2
.
0

3
7
4
3
.
0

t
r
o
h
S

r
e
m
r
o
f
o
t
u
A

4
3
0
0
.
0
±

5
6
0
0
.
0
±

2
5
1
2
.
0

1
7
4
3
.
0

r
a
l
u
g
e
R

2
6
0
0
.
0
±

6
3
0
0
.
0
±

9
3
0
1
.
0
±

2
6
6
0
.
0
±

7
4
7
4
.
0

9
6
2
5
.
0

g
n
o
L

1
2
8
1
.
0

3
6
1
3
.
0

t
r
o
h
S

r
e
m
r
o
f
s
n
a
r
T
-
S
N

)
d
e
u
n
i
t
n
o
c
(

6
e
l
b
a
T

---

<!-- PAGE 42 -->

23  Page 42 of 67

1
8
0
0
.
0
±

5
6
5
7
.
0

7
1
1
0
.
0
±

0
4
0
8
.
0

2
3
9
4
.
0
±

4
6
5
3
.
0

1
5
2
0
.
0
±

7
1
5
4
.
0

1
2
1
0
.
0
±

5
0
5
3
.
0

6
0
0
0
.
0
±

7
9
1
2
.
0

2
9
6
0
.
0
±

4
6
7
7
.
0

0
8
1
0
.
0
±

6
1
2
8
.
0

4
2
5
0
.
0
±

8
0
6
7
.
0

2
2
0
0
.
0
±

0
8
7
0
.
0

7
8
0
0
.
0
±

4
4
0
3
.
0

8
0
0
0
.
0
±

8
0
2
5
.
0

8
4
0
0
.
0
±

4
4
6
3
.
0

5
4
0
0
.
0
±

9
9
1
5
.
0

6
6
0
0
.
0
±

5
8
4
6
.
0

2
8
1
0
.
0
±

%
3
2
.
8
2

0
9
0
0
.
0
±

%
1
1
.
4
2

2
2
1
2
.
0
±

%
9
5
.
9
4

4
1
1
0
.
0
±

%
1
0
.
7
4

9
3
0
0
.
0
±

%
1
5
.
3
5

0
2
0
0
.
0
±

%
5
4
.
2
6

4
3
1
0
.
0
±

%
5
8
.
8
1

2
2
2
0
.
0
±

%
0
1
.
0
2

3
1
3
0
.
0
±

%
5
9
.
4
2

0
1
0
0
.
0
±

%
8
0
.
9
5

7
1
0
0
.
0
±

%
7
3
.
0
5

2
0
0
0
.
0
±

%
9
4
.
9
3

4
1
0
0
.
0
±

%
4
8
.
1
5

%
9
3
.
2
4

3
4
0
0
.
0

8
2
0
0
.
0
±

%
5
9
.
1
3

2
R

E
P
A
M

0
8
4
2
.
0

E
S
M

2
3
7
3
.
0

E
A
M

y
t
i
c
i
r
t
c
e
l
E

0
5
7
7
.
0

2
R

E
P
A
M

2
8
0
0
.
0
±

1
8
0
0
.
0
±

5
5
0
0
.
0
±

9
1
1
0
.
0
±

4
2
1
0
.
0
±

6
0
1
0
.
0
±

7
6
9
1
.
0

0
5
2
3
.
0

2
9
6
7
.
0

6
3
0
5
.
0
±

6
9
8
2
.
0
±

3
5
0
0
.
0
±

1
7
5
6
.
0

3
6
1
6
.
0

2
4
6
7
.
0

5
5
2
0
.
0
±

9
0
1
0
.
0
±

1
3
0
0
.
0
±

4
8
5
5
.
0

3
7
6
5
.
0

9
0
1
6
.
0

3
2
1
0
.
0
±

7
6
0
0
.
0
±

4
0
0
0
.
0
±

0
2
6
6
.
0

5
1
3
6
.
0

5
5
9
5
.
0

6
0
0
0
.
0
±

9
2
0
0
.
0
±

7
6
9
7
.
0

9
0
7
6
.
0

5
0
7
0
.
0
±

7
7
2
2
.
0

3
8
1
0
.
0
±

8
1
8
1
.
0

7
7
4
0
.
0
±

3
3
0
3
.
0

8
3
1
0
.
0
±

6
9
7
2
.
0

5
3
5
0
.
0
±

5
2
2
0
.
0
±

3
4
4
2
.
0

0
5
3
3
.
0

4
1
1
0
.
0
±

3
0
7
5
.
0

3
7
0
0
.
0
±

3
3
7
7
.
0

1
1
0
0
.
0
±

2
7
7
7
.
0

–

–

–

–

g
n
o
L

6
2
0
0
.
0
±

%
1
9
.
1
1

6
6
0
0
.
0
±

%
0
4
.
2
1

9
2
0
0
.
0
±

%
5
1
.
2
1

2
2
0
0
.
0
±

%
5
3
.
6
1

5
0
0
0
.
0
±

%
0
3
.
6
1

8
1
0
0
.
0
±

%
4
3
.
6
1

5
4
0
0
.
0
±

%
0
5
.
4
1

0
1
0
0
.
0
±

%
4
9
.
1
1

6
2
8
2
.
0

E
S
M

c
ffi
a
r
T

E
A
M

0
1
2
4
.
0

c
i
r
t
e

M

t
r
o
h
S

a
t
a
D

0
7
0
0
.
0
±

6
6
0
0
.
0
±

1
9
8
2
.
0

1
6
2
4
.
0

r
a
l
u
g
e
R

7
3
1
0
.
0
±

4
3
1
0
.
0
±

6
6
0
0
.
0
±

0
6
0
0
.
0
±

8
3
9
2
.
0

1
8
2
4
.
0

g
n
o
L

r
e
m
r
o
f
d
e
F

l
e
d
o
M

9
3
0
0
.
0
±

4
6
0
0
.
0
±

7
6
0
5
.
0

2
7
6
5
.
0

r
a
l
u
g
e
R

2
0
0
0
.
0
±

2
0
0
0
.
0
±

3
4
1
0
.
0
±

4
8
0
0
.
0
±

5
5
3
5
.
0

6
5
7
5
.
0

g
n
o
L

5
8
8
4
.
0

3
9
5
5
.
0

t
r
o
h
S

r
e
m
r
o
f
S
T
E

2
9
0
0
.
0
±

1
8
0
0
.
0
±

4
1
0
0
.
0
±

0
9
7
2
.
0

3
2
0
0
.
0
±

4
8
7
3
.
0

r
a
l
u
g
e
R

6
4
8
2
.
0

5
1
9
3
.
0

t
r
o
h
S

r
e
m
r
o
f
s
s
o
r
C

)
d
e
u
n
i
t
n
o
c
(

6
e
l
b
a
T

2
2
0
0
.
0
±

8
1
0
0
.
0
±

3
2
0
0
.
0
±

0
9
3
9
.
0

5
7
9
6
.
0

3
7
6
6
.
0

9
8
0
0
.
0
±

5
2
0
0
.
0
±

5
0
0
0
.
0
±

0
9
0
7
.
0

0
6
9
5
.
0

7
5
9
6
.
0

9
0
0
0
.
0
±

5
0
0
0
.
0
±

1
0
0
0
.
0
±

3
9
8
4
.
0

4
6
8
4
.
0

9
3
2
7
.
0

9
4
0
0
.
0
±

5
2
0
0
.
0
±

3
7
4
6
.
0

9
4
2
5
.
0

6
4
0
0
.
0
±

6
3
0
0
.
0
±

3
9
8
4
.
0

7
3
4
4
.
0

7
6
0
0
.
0
±

7
3
0
0
.
0
±

9
8
5
3
.
0

0
7
7
3
.
0

2
0
0
0
.
0
±

8
1
0
8
.
0

0
1
0
0
.
0
±

8
1
9
7
.
0

1
0
0
0
.
0
±

5
1
8
7
.
0

5
0
0
0
.
0
±

%
9
1
.
4
1

3
0
0
0
.
0
±

%
9
1
.
3
1

1
0
0
0
.
0
±

%
3
9
.
2
1

5
0
0
0
.
0
±

%
3
3
.
0
1

3
0
0
0
.
0
±

%
1
5
.
0
1

3
0
0
0
.
0
±

%
0
0
.
1
1

9
2
0
0
.
0
±

2
4
0
0
.
0
±

1
1
8
3
.
0

8
9
3
4
.
0

r
a
l
u
g
e
R

7
7
1
4
.
0

7
8
6
4
.
0

t
r
o
h
S

r
a
e
n
i
l

D

6
0
0
0
.
0
±

3
0
0
0
.
0
±

2
0
0
0
.
0
±

2
0
0
0
.
0
±

3
4
4
3
.
0

1
0
2
4
.
0

3
0
0
0
.
0
±

8
8
4
2
.
0

3
1
0
0
.
0
±

6
0
6
2
.
0

2
0
0
0
.
0
±

2
2
7
2
.
0

9
0
0
0
.
0
±

4
1
5
3
.
0

6
0
0
0
.
0
±

2
0
0
0
.
0
±

0
0
7
3
.
0

g
n
o
L

0
1
6
3
.
0

r
a
l
u
g
e
R

g
n
o
L

t
r
o
h
S

T
S
T
h
c
t
a
P

---

<!-- PAGE 43 -->

Page 43 of 67  23

o
n

t
a
h
t

s
e
t
a
c
i
d
n
i

"
–
"

.
e
n
i
l
r
e
d
n
u

a

h
t
i

w
d
e
t
h
g
i
l
h
g
i
h

e
r
a

s
t
l
u
s
e
r

t
s
e
b

d
n
o
c
e
s

e
h
t

d
n
a

d
l
o
b

n
i

d
e
t
h
g
i
l
h
g
i
h

e
r
a

s
t
l
u
s
e
r

t
s
e
b

e
h
T

d
n
a

,

m

r
e
t
-
r
a
l
u
g
e
r

,

m

r
e
t
-
t
r
o
h
s

r
o
f

O
h
t
g
n
e
l

t
u
p
t
u
o

e
h
t

e
t
o
n
e
d

’
g
n
o
L
’

d
n
a

’
,
r
a
l
u
g
e
R

’

’
,
t
r
o
h
S
’

.
d
e
n
i
a
t
b
o

e
b

d
l
u
o
c

s
t
l
u
s
e
r

d
i
l
a
v

s
t
n
e
m

i
r
e
p
x
e

f
o

n
o
i
t
a
i
v
e
d

d
r
a
d
n
a
t
s

d
n
a

e
u
l
a
v

e
g
a
r
e
v
a

e
h
t

t
r
o
p
e
r

e

W

.
n
o
i
t
c
i
d
e
r
p

s
e
i
r
e
s

e
m

i
t

m

r
e
t
-
g
n
o
l

2
6
2
0
.
0
±

8
1
0
5
.
0

8
8
0
0
.
0
±

3
2
6
3
.
0

8
1
0
0
.
0
±

7
3
2
2
.
0

3
8
4
0
.
0
±

9
1
4
6
.
0

0
2
1
0
.
0
±

9
6
0
3
.
0

3
4
3
1
.
0
±

3
5
6
4
.
0

8
2
0
0
.
0
±

9
3
1
8
.
0

6
8
0
0
.
0
±

4
5
0
8
.
0

1
0
1
0
.
0
±

3
9
2
8
.
0

5
5
1
0
.
0
±

%
5
1
.
6
4

5
1
0
0
.
0
±

%
5
2
.
5
4

6
4
0
0
.
0
±

%
7
6
.
2
4

5
4
3
0
.
0
±

%
4
3
.
9
3

8
7
0
0
.
0
±

%
0
2
.
2
3

1
2
5
0
.
0
±

%
3
8
.
5
4

2
4
0
0
.
0
±

%
4
8
.
1
2

2
2
0
0
.
0
±

%
2
7
.
1
2

7
6
0
0
.
0
±

%
1
4
.
1
2

2
R

E
P
A
M

4
7
0
5
.
0

E
S
M

7
7
3
5
.
0

E
A
M

y
t
i
c
i
r
t
c
e
l
E

6
7
0
7
.
0

2
R

E
P
A
M

6
6
2
0
.
0
±

5
3
1
0
.
0
±

4
2
0
0
.
0
±

9
8
0
0
.
0
±

9
1
0
0
.
0
±

7
0
0
0
.
0
±

9
9
4
6
.
0

0
5
2
6
.
0

2
4
9
0
.
0

8
1
0
0
.
0
±

7
2
0
0
.
0
±

3
2
0
0
.
0
±

6
2
9
7
.
0

5
3
7
6
.
0

4
7
1
0
.
0

2
9
4
0
.
0
±

4
2
3
0
.
0
±

2
1
0
1
.
0
±

8
4
6
3
.
0

3
9
4
4
.
0

5
6
6
8
.
0

2
2
1
0
.
0
±

1
7
0
0
.
0
±

9
9
0
0
.
0
±

8
8
9
2
.
0

6
2
1
4
.
0

4
0
3
7
.
0

1
7
3
1
.
0
±

8
8
6
0
.
0
±

0
1
0
0
.
0
±

0
6
4
5
.
0

7
6
7
5
.
0

4
9
5
7
.
0

7
0
0
0
.
0
±

%
2
0
.
6
1

2
5
0
0
.
0
±

%
9
2
.
5
2

9
1
0
0
.
0
±

%
3
8
.
1
3

5
0
0
0
.
0
±

%
1
6
.
3
1

3
0
0
0
.
0
±

%
8
7
.
3
1

2
4
0
0
.
0
±

%
1
7
.
2
1

1
7
6
3
.
0

E
S
M

c
ffi
a
r
T

E
A
M

7
4
6
4
.
0

c
i
r
t
e

M

t
r
o
h
S

a
t
a
D

9
2
0
0
.
0
±

7
1
0
0
.
0
±

7
4
3
1
.
1

3
0
8
8
.
0

r
a
l
u
g
e
R

8
0
0
0
.
0
±

1
0
0
0
.
0
±

9
2
0
0
.
0
±

9
1
0
0
.
0
±

6
4
2
2
.
1

9
8
5
9
.
0

g
n
o
L

S
T
A
E
B
N

-

l
e
d
o
M

8
9
0
0
.
0
±

6
8
0
0
.
0
±

8
8
3
3
.
0

0
1
6
4
.
0

r
a
l
u
g
e
R

5
4
1
0
.
0
±

7
3
0
0
.
0
±

5
4
0
0
.
0
±

7
3
0
0
.
0
±

9
6
9
2
.
0

4
7
2
4
.
0

g
n
o
L

1
0
9
2
.
0

4
9
2
4
.
0

t
r
o
h
S

r
e
m
r
o
f
o
t
u
A

)
d
e
u
n
i
t
n
o
c
(

6
e
l
b
a
T

8
8
0
0
.
0
±

0
2
1
0
.
0
±

2
1
0
0
.
0
±

3
1
0
0
.
0
±

5
1
1
0
.
0
±

0
5
0
0
.
0
±

4
8
9
1
.
0

9
8
1
3
.
0

6
2
9
0
.
0

%
4
5
.
9

4
2
4
1
.
1

4
0
8
8
.
0

r
a
l
u
g
e
R

3
0
1
0
.
0
±

3
4
7
1
.
0

3
1
1
0
.
0
±

9
9
0
3
.
0

9
1
0
0
.
0
±

1
2
1
0
.
0

6
4
0
0
.
0
±

%
3
8
.
0
1

8
3
0
0
.
0
±

2
5
0
0
.
0
±

0
9
2
2
.
1

1
6
6
9
.
0

g
n
o
L

8
2
0
0
.
0
±

6
9
8
1
.
0

8
3
0
0
.
0
±

8
2
0
0
.
0
±

0
2
0
0
.
0
±

3
3
0
0
.
0
±

3
1
0
0
.
0
±

3
3
1
3
.
0

0
6
0
7
.
0

%
4
8
.
8

1
9
6
3
.
0

4
5
6
4
.
0

t
r
o
h
S

r
e
m
r
o
f
s
n
a
r
T
-
S
N

---

<!-- PAGE 44 -->

PatchTST

Crossformer

NS-Trans-
former

ETSformer

LSTnet

N-BEATS

TDformer

Autoformer

Fedformer

23  Page 44 of 67

0.4089
0.8234

Traffic
MAE
0.3495
0.7535

Table 7  The comparison of prediction results between the model before and after shuffling the input sequence
Dataset
Metric
DLinear

ETTh1
MAE MSE
0.4317
Ori.
Shuf. 0.6655
Drop 54.16% 101.37% 115.59% 124.16% 33.95% 53.37% 118.88% 342.09%
0.4070
Ori.
Shuf. 0.7860
Drop 93.12% 172.13% 130.22% 151.17% 63.43% 101.89% 288.07% 1092.50%
0.4454
Ori.
Shuf. 0.7744
Drop 73.84% 146.97%

1.0672
1.2951
21.35% 28.90% 153.98% 435.60%

ILI
MAE MSE
0.9440
1.2645

Exchange
MAE
0.1573
0.3443

MSE
0.5034
1.1284

MSE
0.0487
0.2153

1.1349
1.1493
1.27%

0.3329
0.7664

0.0520
0.6201

0.4160
1.0274

1.1853
2.3930

0.3865
1.0518

0.7055
1.1530

0.4540
1.1403

0.7634
0.7610

2.3385
3.2890

0.1118
0.5988

0.1609
0.6244

0.2575
0.6540

1.8397
2.8216

−
0.31%
0.3403
0.7617

0.1695
0.6183

1.7844
2.7962

0.7382
1.0340

0.4252
1.1400

0.8402
1.1948

0.6121
Ori.
Shuf. 0.7796
Drop 27.36% 40.07% 123.83% 168.11% 29.68% 56.70% 264.78% 983.19%
1.9351
0.5246
Ori.
2.1160
Shuf. 0.6653
Drop 26.82% 58.88% 64.19% 97.37% 11.81% 9.35%
2.7753
0.7115
0.6960
Ori.
Shuf. 0.7548
2.6412
0.7654
Drop 8.45% 10.49% 7.58%

0.1817
0.3195
75.84% 213.26%
0.8062
0.8217
1.92%

0.9279
1.1435
23.24%

0.8898
0.9303
4.55%

0.5397
0.8575

0.4722
0.7753

0.9896
1.1065

0.6042
1.1925

0.0565
0.6120

0.0596
0.1867

0.9192
1.0156

1.2103
1.1605

0.7883
0.6098
Ori.
Shuf. 0.6479
0.8235
Drop 6.25% 4.47%
0.7662
0.6742
Ori.
Shuf. 0.7689
1.0767
Drop 14.05% 40.52% 115.41% 166.54%

0.6878
0.7507
9.15%
0.3524
0.7591

1.0420
1.1260
8.06%
0.4342
1.1573

4.83%
2.7416
3.2442

4.11% −
−
1.2166
1.2702
4.41% 18.33% 115.33% 309.14%
1.4841
1.4038

0.1618
0.3484

0.0514
0.2103

3.2275
2.1344

1.5010
1.2450

3.6448
3.7931
4.07%

−5.41%
0.8414
1.1584

−17.06% −33.87%
0.0885
0.2162
0.5850
0.5779

0.5443
1.1000

0.3190
0.8059

0.3814
1.2024

0.5389
Ori.
Shuf. 0.8101
Drop 50.32% 102.09% 152.63% 215.26% 37.68% 43.60% 167.30% 561.02%
0.4980
Ori.
Shuf. 0.8130
Drop 63.25% 136.00% 153.66% 223.79% 49.25% 77.66% 155.68% 516.30%

1.5320
2.2000

0.2245
0.5740

0.0951
0.5861

0.3695
1.1964

0.8095
1.2082

0.3168
0.8036

1.3598
2.4158

0.4695
1.1080

Ori. denotes the original prediction accuracy, Shuf. denotes the prediction accuracy after the shuffling, and 
Drop is calculated as follows: Drop = (Shuf.
100%. The maximum results of the decline rate 
are highlighted in bold

Ori.)
−
Ori. ×

Through this analysis, we can examine the model’s susceptibility to overfitting and 
the level of interference caused by noise.

3.  Trend and Season Information Analysis: To evaluate the model’s capacity to capture 
trend  and  season  information,  experiments  will  be  conducted  on  an  artificial  dataset 
explicitly  incorporating  trend  and  season  terms. This  analysis  assesses  how  well  the 
models can capture such temporal patterns.

4.  Attention  Module  Evaluation  for  Transformer-based  Models:  For  the  Transformer-
based  models,  our  primary  focus  will  be  on  assessing  the  performance  of  different

---

<!-- PAGE 45 -->

Table 8  The prediction results 
for each model across various 
datasets, considering different 
lengths of the lookback window. 
The best results are highlighted 
in bold

Dataset
Metric
DLinear

PatchTST

Crossformer

NS-Transformer

Fedformer

Autoformer

N-BEATS

ETSformer

LSTnet

TDformer

ETTh1
MAE
0.4389
0.4317
0.4301
0.4434
0.4323
0.4289
0.4464
0.4454
0.4452
0.5164
0.4990
0.5115
0.4962
0.5082
0.5170
0.5388
0.5439
0.5521
0.6110
0.6099
0.6130
0.5061
0.5257
0.5482
0.6989
0.6991
0.7097
0.6514
0.6705
0.6845

MSE
0.4367
0.4089
0.3994
0.4459
0.4058
0.3965
0.4338
0.4157
0.4175
0.5420
0.5165
0.5360
0.4656
0.4748
0.4834
0.5289
0.5480
0.5536
0.7959
0.7874
0.7872
0.5318
0.5393
0.5604
0.9221
0.9270
0.9385
0.7323
0.7506
0.7826

48
96
192
48
96
192
48
96
192
48
96
192
48
96
192
48
96
192
48
96
192
48
96
192
48
96
192
48
96
192

Page 45 of 67  23

Exchange
MAE
0.1582
0.1572
0.1585
0.6148
0.6079
0.5881
0.5892
0.5743
0.5705
0.6182
0.6193
0.6023
0.1946
0.2255
0.2782
0.1997
0.2298
0.2290
0.1598
0.1633
0.1632
0.1795
0.1837
0.1842
0.8237
0.8073
0.7675
1.3290
1.4197
1.3507

MSE
0.0500
0.0487
0.0488
0.6097
0.5925
0.5371
0.5196
0.5051
0.5170
0.6200
0.6100
0.5655
0.0731
0.0937
0.1343
0.0767
0.0978
0.0909
0.0517
0.0522
0.0513
0.0581
0.0602
0.0611
0.9241
0.8907
0.8195
2.5359
2.9719
2.7163

Attention modules utilized in the models. To achieve this, a comparative experiment 
has been designed to evaluate the prediction accuracy and complexity associated with 
various Attention modules.These analyses aim to gain insights into the strengths, limi-
tations, performances, and characteristics of the models and methods mentioned earlier.

6.4.1  Evaluation of model prediction accuracy

In order to comprehensively evaluate the prediction accuracy of each model, this section 
presents  experimental  results  on  both  multivariate  and  univariate  time  series  prediction 
tasks.

As shown in Fig. 17, We employ two different validation set splitting methods: (1) simple 
time split validation and (2) sliding window validation. In simple time split validation (Wu 
et al. 2021; Zhou et al. 2021; Kitaev et al. 2020; Li et al. 2019), the training, validation, 
and test sets are sequentially divided based on time. Sliding window validation (Liu and

---

<!-- PAGE 46 -->

23  Page 46 of 67

Fig. 18  The prediction results for the trend term. The horizontal axis represents the time step index, and 
the  vertical  axis  represents  the  model’s  prediction  result.  Ground  Truth  represents  the  true  value  cor-
responding to the predicted segment, and we highlight the better-performing model results and Ground 
Truth

Fig. 19  The  prediction  results  for  the  season  term. The  horizontal  axis  represents  the  time  step  index, 
and the vertical axis represents the model’s prediction result. Ground Truth represents the true value cor-
responding to the predicted segment, and we highlight the better-performing model results and Ground 
Truth

Table 9  The prediction of the model for the trend and season term in the artificial dataset. The best results are 
highlighted in bold and the second best results are highlighted with a underline
Data
Metric
DLinear
Fedformer
Autoformer
N-BEATS
ETSformer
LSTnet
TDformer

Original Sequence
MAE
0.0145
0.0612
0.1246
0.0269
0.1705
0.0481
0.0718

Season Term
MAE
0.1500
0.0823
0.1861
0.9032
0.1162
0.4159
0.1122

Trend Term
MAE
0.1456
0.1074
0.1602
0.6359
0.1501
0.4210
0.1109

MSE
0.0351
0.0181
0.0433
0.4996
0.0351
0.1962
0.0193

MSE
0.0351
0.0115
0.0570
0.8704
0.0206
0.1921
0.0202

MSE
0.0003
0.0057
0.0276
0.0014
0.0447
0.0058
0.0106

---

<!-- PAGE 47 -->

Table 10  Comparison of predic-
tion results among different At-
tention modules with equivalent 
space complexity. We highlight 
in bold the results that show 
improvement compared to the 
vanilla Attention module

Dataset
Metric
Auto-Correction
LogSparse Attention
Patch Attention
Pyraformer Attention
Dttention
LSH Attention
ProSparse Attention
FA
Attention

Table 11  Time series prediction 
results of models based on At-
tention. The best results for each 
prediction length are highlighted 
in bold

Dataset
Metric
PatchTST

Crossformer

Transformer

Pyraformer

Reformer

Logtrans

Informer

Metric
O
Logtrans
Informer
Reformer
PatchTST
Crossformer
Transformer
Pyraformer

Table 12  The maximum memory 
occupation in MB of models 
during training

Page 47 of 67  23

ETTh1
MAE
0.5160
0.5285
0.4357
0.5110
0.5648
0.5805
0.6591
0.7975
0.5310

MSE
0.5331
0.5349
0.4015
0.5157
0.6112
0.6701
0.8632
1.1465
0.5741

Exchange
MAE
0.4882
0.4012
0.1594
0.5194
0.4739
0.5352
0.4840
1.1525
0.4605

MSE
0.3837
0.2340
0.0501
0.4060
0.3314
0.4877
0.3497
1.7961
0.3402

ETTh1
MAE
0.3932
0.4309
0.5126
0.5566
0.4454
0.5380
0.4745
0.5174
0.6636
0.4799
0.5358
0.6907
0.4986
0.5646
0.7690
0.5800
0.5846
0.7202
0.5099
0.6583
0.8301

MSE
0.3506
0.4027
0.5277
0.6142
0.4160
0.5800
0.4491
0.5291
0.8045
0.4682
0.5705
0.8723
0.4984
0.6062
1.0775
0.6109
0.5922
0.9112
0.5303
0.8626
1.3028

96
96
96
96
96
96
96
96
96

48
96
336
48
96
336
48
96
336
48
96
336
48
96
336
48
96
336
48
96
336

Maximum Memory Occupation (MB)
48
1512
1762
1639
1559
2489
1738
1659

96
1554
1846
1717
1586
2830
1821
1671

336
1799
2075
2110
1602
3748
2038
1745

---

<!-- PAGE 48 -->

23  Page 48 of 67

Yang 2022; Malenica et al. 2021; Mintarsih et al. 2023), on the other hand, uses a fixed-size 
window that continuously slides over time for training and validation. Compared to simple 
time split validation, sliding window validation traverses the entire time series, altering the 
training and validation sets as it progresses. This method is particularly suited for slightly 
stationary or concept-drifting time series, especially in financial datasets.

We initially apply simple time split validation to all datasets to assess the predictive accu-
racy of the models. Unless otherwise specified, the batch size for all experiments was set to 
16. To ensure robustness and reliability, all experimental results presented in this study are 
averaged over five trials. Consistent with previous work (Wu et al. 2021; Zhou et al. 2022; 
Woo et al. 2022; Zhou et al. 2021), we fixed the input length of the ILI dataset at L = 36 and 
set the output length O to 12, 24, 48 for short-term, regular-term, and long-term time series 
predictions, respectively. For the remaining datasets, we fixed the input length at  L = 96 
and set the output length O to 48, 96, 336 for short-term, regular-term, and long-term pre-
dictions, respectively. All hyperparameters for the deep learning models in the experiments 
were set according to the optimal configurations provided in their respective papers or code. 
For univariate time series prediction, we used the traditional ARIMA model as the baseline, 
while for multivariate time series prediction, we employed the VAR (Vector Autoregressive) 
model as the baseline.

The complete experimental results of the multivariate time series prediction task can be 
found in Table 13 in Appendix A. From the table, it is observed that among all the mentioned 
models, models utilizing the method of time series decomposition (e.g., Fedformer, ETS-
former) and Transformer-based approaches (e.g., Crossformer, PatchTST) exhibit signifi-
cantly superior prediction accuracy compared to the remaining models. Therefore, in Table 
5, we only present the experimental results of these two types of methods. It is worth noting 
that, to further evaluate the performance of these methods on slightly stationary time series, 
in Table 5, we applied sliding window validation with a window size set to one-tenth of the 
dataset length for the financial exchange dataset.

In the multivariate time-series forecasting experiment, we observe several noteworthy 
findings. DLinear (Yun et al. 2019), which directly extracts temporal features using linear 
layers. demonstrates commendable prediction accuracy across the vast majority of datas-
ets.  Specifically,  in Table  5,  we  observe  that  DLinear  outperforms  the  suboptimal  model 
PatchTST in terms of MAE and Fedformer in terms of MAPE for the ETTh1 dataset. It 
achieves improvements of 3.13% and 2.24% for prediction length of 336, respectively. Fur-
thermore, it is worth noting that DLinear also boosted performance by 14.87% on R2 for 
prediction  lengths  of  336  compared  with  the  suboptimal  model  PatchTST.  On  the  other 
hand,  Crossformer  (Zhang  and Yan  2022)  primarily  focuses  on  capturing  the  correlation 
among time-series variables, making it particularly effective for datasets characterized by 
intricate variables. For instance, in the Electricity dataset, which comprises 321 variables, 
surpassing other datasets in terms of the number of variables, Crossformer exhibits a dis-
tinct accuracy advantage over the suboptimal model NS-Transformer. It achieves improve-
ments of 10.93% and 17.70% in MSE and MAPE for prediction lengths of 48, respectively. 
However,  it  is  worth  noting  that  Crossformer’s  computational  cost  is  considerably  high, 
which  may  limit  its  feasibility  for  long-term  time  series  prediction  tasks  due  to  resource 
constraints.

PatchTST  (Nie  et  al.  2022),  on  the  other  hand,  demonstrates  enhanced  suitability  for 
datasets characterized by pronounced long-term periodicity and trends, such as exchange

---

<!-- PAGE 49 -->

Page 49 of 67  23

rate  and  illness  datasets.  By  dividing  the  input  time  series  into  fixed-length  patches  and 
emphasizing time-step dependencies between the patches, PatchTST is capable of uncov-
ering  long-term  temporal  relationships  and  achieves  notable  improvements  in  MSE  and 
R2  compared  to  other  models.  For  example,  in Table  5,  PatchTST  shows  improvements 
of 27.30% and 17.49% in MSE and R2, respectively, for a prediction length of 48 on the 
ILI  dataset  compared  to  the  suboptimal  model  NS-Transformer.  Similarly,  on  the Traffic 
dataset, PatchTST exhibits significant accuracy advantages over the suboptimal model NS-
Transformer, achieving improvements of 11.46% in MAE for a prediction length of 336.

The complete results of the univariate time series prediction experiment can be found in 
Table 14 in Appendix A. The findings in Table 14, consistent with those in the multivariate 
time series forecasting experiment, indicate that models based on time-series decomposition 
methods and Transformer-based models exhibit superior prediction accuracy for univariate 
time  series  forecasting  compared  to  other  models.  Therefore,  in  Table  6,  we  present  the 
results  of  these  two  categories  separately.  Similarly,  in  Table  6,  we  applied  sliding  win-
dow validation with a window size set to one-tenth of the dataset length for the financial 
exchange dataset.

In the univariate time series prediction task, both NS-Transformer (Liu et al. 2022) and 
DLinear model demonstrate superior performance across various datasets. For instance, in 
the long-term prediction task on the ILI dataset, NS-Transformer outperforms the subopti-
mal model PatchTST with improvements of 9.54%, 25.32%, 46.47% in MAE, MSE and R2
, respectively. Comparing the results of multivariate and univariate time series prediction 
experiments, it is evident that NS-Transformer exhibits inferior performance in multivariate 
scenarios  while  demonstrating  better  performance  in  univariate  scenarios. The  main  rea-
son is that NS-Transformer incorporates non-stationary information from variables into the 
attention mechanism and adjusts the output of the attention mechanism based on the non-
stationary information. However, in multivariate prediction tasks, an excessive amount of 
non-stationary information negatively impacts the output results of the attention mechanism.
Upon analyzing the empirical results of both multivariate and univariate time series pre-
diction,  we  observe  that  DLinear  consistently  demonstrates  superior  accuracy  compared 
to the majority of models. Interestingly, despite using a simpler linear layer for capturing 
time-step dependencies, DLinear outperforms numerous sophisticated models. This finding 
suggests that existing complex models may have limited capability in effectively capturing 
and utilizing time-step information, potentially leading to overfitting and noise interference. 
Additionally, compared to other models, DLinear makes more effective use of the sequential 
order of the input data, which is likely a key factor in its success.

6.4.2  Evaluation of information mining capabilities for complex models

Based on the analysis of results from both multivariate and univariate time series forecast-
ing experiments, we argue that current complex models are prone to issues such as overfit-
ting and still demonstrate deficiencies in capturing essential time-step dependencies. As a 
result, in this section, we will conduct an input shuffling experiment and extend the look-
back window experiment to explore further and clarify the limitations of complex models.

Input Shuffling Experiment: In time series forecasting, the sequential order of time series 
often carries significant sequential information. A reliable model should be able to effec-

---

<!-- PAGE 50 -->

23  Page 50 of 67

tively capture and understand the sequential order information. As a result, different sequen-
tial orders of input time series should lead to distinct predictions.

To evaluate the model’s ability to capture sequential order information across time steps, 
we shuffle the input time series of the model. By comparing the model’s prediction accuracy 
before and after shuffling, we can analyze the model’s capacity to capture the sequential 
information of the time series.

The  input  length  for  the  ILI  dataset  was  set  to  L = 36,  and  the  prediction  length  O 
was set to 24. Furthermore, for the other datasets, the input length was set to L = 96, and 
the prediction length was set to O = 96. All empirical results presented in this study were 
obtained by averaging the outputs of five randomized experiments. The prediction accuracy 
of the model is positively correlated with its capability to extract sequential information. 
Based on the analysis in Sect. 6.4.1, it is evident that DLinear and PatchTST exhibit sig-
nificant accuracy advantages over various existing complex models (such as Autoformer, 
TDformer, ETSformer, etc.) across all datasets despite maintaining a simpler model struc-
ture. Table 7 shows that PatchTST exhibits the most notable decline in prediction accuracy 
after shuffling the input sequence across the ETTh1, ILI, and Exchange datasets. Similarly, 
DLinear also experiences a substantial decline in model accuracy following order shuffling 
in these datasets. On the other hand, complex models like Autoformer, TDformer, and others 
demonstrate minimal impact on their prediction accuracy or even show slight improvements 
after input shuffling. For instance, TDformer demonstrates a remarkable 33.87% improve-
ment  in  MSE  on  the  Exchange  dataset  after  shuffling,  whereas  LSTnet  exhibits  a  4.83% 
enhancement in MSE on the ILI dataset after shuffling.

Based on the experimental results and the preceding analysis, we can conclude a posi-
tive correlation between the prediction accuracy of a model and its ability to capture the 
sequential order of the time series. Moreover, the existing complex models exhibit limited 
proficiency in effectively capturing the sequential order of the time series, which explains 
their comparatively lower prediction accuracy when compared to simpler models in both 
multivariate  and  univariate  time  series  forecasting  experiments. Apart  from  their  weaker 
capability to capture the time series sequential information, we also suggest that the com-
plex models face challenges such as overfitting and noise interference. Therefore, our sub-
sequent experiment investigates whether these issues affect these models.

Extending the Lookback Window Experiment: To investigate the potential overfitting and 
noise interference of complex models in time series prediction, we conduct extending look-
back  window  experiments. The  size  of  the  lookback  window  significantly  influences  the 
accuracy  of  time  series  prediction,  as  it  determines  the  amount  of  historical  information 
incorporated by the model. Generally, superior models achieve more accurate predictions 
using an extended lookback window. However, in the case of models affected by overfitting 
and noise interference, an extended lookback window introduces more noise. Due to over-
fitting, the model cannot effectively incorporate additional historical information, resulting 
in decreased prediction accuracy with an extended lookback window. Building on this con-
cept, this section presents the extending lookback window experiment.

In  our  experiment,  we  set  input  time  series  lengths  to  48,  96,  192  while  keeping  the 
output  prediction  length  fixed  at  96  for  the  time  series. We  then  examine  the  changes  in 
prediction  accuracy  for  each  model  as  the  lookback  window  is  extended.  It  is  important 
to note that all results presented in this study are obtained by averaging the outputs of five 
randomized experiments.

---

<!-- PAGE 51 -->

Page 51 of 67  23

The experimental results are depicted in Table 8. Complex models, including ETSformer, 
TDformer, and Autoformer, achieve their highest prediction accuracies only with the short-
est input time series. In contrast, their accuracies gradually decline as the input time series 
lengthens. We believe this is primarily due to their limited ability to handle lengthy input 
time series, leading to longer sequences introducing more noise and exacerbating overfit-
ting. However, PatchTST is the only model with optimal prediction accuracy for the longest 
input on both datasets. Additionally, on the ETTh1 dataset, DLinear demonstrates the high-
est prediction accuracy for the longest input time series.

Based on the analysis of the findings from the input shuffling experiment and extending 
the lookback window experiment, we propose that the insufficient prediction capabilities of 
current complex models can be primarily attributed to two key factors: (1) their limited abil-
ity to utilize the sequential information inherent in the time series effectively, and (2) their 
susceptibility to overfitting and noise interference.

6.4.3  Assessment of trend and season information mining capability

Based on the results of multivariate and univariate time series prediction experiments, it is 
apparent that models incorporating the method of time series decomposition tend to exhibit 
superior prediction accuracy. For models that employ time series decomposition methods, 
the trend term and the season term are the temporal terms they most aspire to extract. To 
further explore the performance of the aforementioned models in time series decomposition, 
trend, and seasonal term extraction, and overall prediction capabilities, we will train and test 
these models on an artificial dataset with the explicit trend and seasonal terms. Using this 
dataset, we can clearly observe the differences between the model outputs for the trend and 
seasonal terms and their corresponding true values. Next, we will provide an overview of 
the artificial dataset, including the process of generating the trend and seasonal terms.

1
eβ0(t

Artificial Dataset: The artificial dataset consists of two terms: the trend term and the sea-
son term. Specifically, the trend term at the tth time step in each instance follows the equation 
b(t) =
β1) , while the season term at the tth time step in each instance follows the equation 
−
s(t) = A1 cos(2πf1t) + A2 cos(2πf2t). The parameters used for generating the dataset are 
as follows: β0 =
13. In this experiment, 
the artificial dataset contains 16,847 instances. During the training phase, the instances in the 
training set are represented as xi = [b(1) + s(1 + i), . . . , b(L + O) + s(L + O + i)] + ξi ,  
where  ξi  represents Gaussian-distributed noise with a mean of 0 and a standard deviation 
of 0.05.

0.2, β1 = L , A1 = A2 = 0.15, f1 = 1

10, and f2 = 1

−

In this experiment, we set both the input and output lengths of the time series to 96. The 
dataset was partitioned into training, validation, and test sets following a ratio of 6:2:2, uti-
lizing a batch size of 16. The reported outcomes are derived from the mean results of five 
distinct and independent experiments.

Table  9  presents  the  predictions  of  different  models  incorporating  time-series  decom-
position on the artificial dataset. Figure 18 shows the models’ prediction accuracy for the 
trend terms. Among the models evaluated for trend term prediction on the artificial dataset, 
Fedformer,  TDformer,  and  DLinear  demonstrate  superior  performance.  Fedformer  is  the 
best, which shows improvements of 3.14% and 6.18% in MAE and MSE for trend term pre-
diction compared to TDformer, and 26.24% and 48.43% compared to DLinear. Fedformer, 
TDformer, and DLinear all use simple trend information extraction methods, such as mean

---

<!-- PAGE 52 -->

23  Page 52 of 67

filtering and linear layers. This indicates that simple techniques can effectively extract trend 
information, while complex methods like N-BEATS and ETSformer may suffer from a cer-
tain degree of overfitting in accurately predicting trend terms.

The predictions for the season term are depicted in Fig. 19, and Table 9 provides an over-
view of the season term predictions for each model. Based on the aforementioned findings, it 
becomes apparent that the top-performing models for season-term prediction are Fedformer, 
TDformer,  and  ETSformer.  Notably,  all  of  these  models  employ  frequency  domain-based 
approaches to process season terms. Among the three methods, Fedformer has the strongest 
ability to extract seasonal terms. Compared to TDformer, Fedformer improves the MAE and 
MSE  for  season-term  prediction  by  26.65%  and  43.07%,  respectively.  Similarly,  compared 
to ETSformer, Fedformer shows improvements of 29.17% in MAE and 44.17% in MSE for 
season-term prediction.

Based on the aforementioned results of season term prediction, it becomes evident that 
models that utilize frequency domain-based methods outperform other models that rely on 
time  domain-based  methods.  Therefore,  it  can  be  concluded  that  processing  the  Fourier 
components  in  the  frequency  domain  is  an  effective  approach  for  capturing  the  inherent 
periodic information present in the time series.

By integrating the predictions of both trend and season terms from the models, we notice 
a  positive  correlation  between  their  predictive  capabilities.  Specifically,  a  more  accurate 
prediction of season terms aligns with a better prediction of trend terms across the majority 
of  models. We  propose  that  this  phenomenon can  be  attributed to  most  models’  iterative 
decomposition  of  trend  and  season  terms.  The  prediction  accuracy  of  one  term  directly 
influences the subsequent decomposition of the remaining terms.

6.4.4  Assessing the efficacy of attention modules

Drawing upon the outcomes of multivariate and univariate time series prediction experi-
ments,  it  becomes  evident  that  most  Transformer-based  models  demonstrate  superior 
prediction  performance  compared  to  other  models.  The  main  difference  between  Trans-
former-based models lies in their internal Attention modules. Therefore, in the following we 
will analyze these Attention modules to explore their contributions to the models’ overall 
predictive capabilities and evaluate their complexities.

To examine the impact of different Attention modules on the model’s prediction capabil-
ity, we employ the Transformer as the baseline framework in our experiments. Subsequently, 
we replace the Attention modules with the test objects to facilitate a comparative analysis 
of their effects on prediction accuracy. Additionally, we fine-tune the hidden layer dimen-
sions of the test objects to ensure consistent space complexity. This adjustment is necessary 
because LogSparse Attention, LSH Attention, and ProSparse Attention have been optimized 
in terms of space complexity compared to the vanilla Attention modules. To ensure a fair 
comparison, we aligned the space complexity of the test subjects to a similar scale.

We keep a consistent batch size of 8 and set the model with an input time series length 
L = 96  and  a  predicted  time  series  length  O = 96. The  rest  of  the  experimental  config-
urations  align  with  those  utilized  in  the  multivariate  time  series  prediction  experiments 
described in Sect. 6.4.1.

---

<!-- PAGE 53 -->

Page 53 of 67  23

Table 10 demonstrates that Patch Attention in PatchTST significantly improves the predic-
tion capability of the Attention mechanism. When compared with the vanilla Attention mod-
ule, Patch Attention exhibits substantial accuracy enhancements on the ETTh1 dataset, with 
improvements  of  17.95%  and  30.06%  in  MAE  and  MSE,  respectively. Additionally,  Patch 
Attention  achieves  an  impressive  85.27%  improvement  in  MSE  on  the  Exchange  dataset. 
These results indicate that aggregating short-term time steps collectively significantly enhances 
the capacity of the attention mechanism to capture temporal information within a time series.

Furthermore, our experiments in Sect. 6.4.1 reveal the notable performance of Fedformer 
and  Crossformer.  However,  it  is  worth  noting  that  their  attention  modules,  FA  and  DAt-
tention,  exhibit  subpar  performance  in  this  specific  experiment.  We  believe  that  the  pri-
mary  factor  contributing  to  this  outcome  is  the  absence  of  space  complexity  limitations 
on their attention modules during the experiments conducted in Sect. 6.4.1. However, the 
space complexity of FA and DAttention significantly surpasses that of the vanilla Attention 
module. To maintain consistency in space complexity across all experimental subjects, the 
dimensions of the hidden layer in FA and DAttention are compressed to a smaller scale in 
this experiment, resulting in their subpar prediction accuracies.

According to the introduction in Sect. 4, numerous models based on the Attention mech-
anism have optimized their complexity to meet the demands of long-term time series fore-
casting tasks. Consequently, we delve into the complexity of these optimized models and 
examine their corresponding prediction performance.

We uniformly set the batch size to 8. All optimized models are trained on the ETTh1 
dataset  with  an  input  time  series  length  of  L = 96  and  predicted  time  series  lengths  of 
O =
. Following the original works (Nie et al. 2022; Zhang and Yan 2022; 
Liu et al. 2021; Kitaev et al. 2020; Li et al. 2019; Zhou et al. 2021), the remaining hyper-
parameters of these models are set to their optimal values.

48, 96, 336
}

{

Next, we will analyze the performance of these models from two perspectives: time com-
plexity and space complexity. Firstly, regarding time complexity, we observe that Reformer 
demonstrates  superior  prediction  performance  while  maintaining  a  low  time  complexity. 
This observation is illustrated in Fig. 20 and summarized in Table 11. Specifically, Reformer 
exhibits the shortest test time, reducing 10.14% compared to LogTrans, the model with the 
second-best test time. Additionally, on the ETTh1 dataset, Reformer showcases significant 
improvements  in  MAE  by  14.03%  and  MSE  by  18.42%  compared  to  LogTrans.  One  of 
the distinctive features of Reformer is incorporating the Locality-Sensitive Hashing (LSH) 
Attention mechanism. This mechanism partitions the time steps into groups using a hash 
function, limiting the computation of similarity relationships to time steps within the same 
group. As a result, the complexity of the Attention mechanism is effectively reduced.

When considering space complexity, our analysis reveals that models utilizing the patch 
slicing method, such as PatchTST and Pyraformer, demonstrate distinct advantages while 
maintaining high prediction accuracy. In particular, these models demonstrate even more 
pronounced  benefits  in  space  complexity  when  dealing  with  long-term  time  series.  In 
Fig. 21 and Table 12, we observe that for a prediction length of 336, PatchTST exhibits a 
memory occupation that is 10.93% lower than that of LogTrans. Additionally, PatchTST 
showcases significant improvements in MAE by 28.83% and in MSE by 42.09% compared

---

<!-- PAGE 54 -->

23  Page 54 of 67

Fig. 20  Inference time. The vertical axis represents the inference time of different models for the whole 
test  dataset. We  report  the  mean  inference  time  for  each  model  across  three  scenarios  with  prediction 
lengths of 48, 96, 336

Fig.  21  Maximum  memory  occupation  during  training.  The  horizontal  axis  represents  the  prediction 
length, and the vertical axis represents the maximum memory occupation

to LogTrans on the ETTh1 dataset. Similarly, for a prediction length of 336, Pyraformer 
exhibits a memory occupation that is 3.00% lower than LogTrans. Moreover, Pyraformer 
surpasses LogTrans in prediction accuracy with a 4.10% improvement in MAE and a 4.27% 
improvement in MSE on the ETTh1 dataset.

---

<!-- PAGE 55 -->

Page 55 of 67  23

Through an analysis of the prediction ability and complexity of the Attention module, we 
have observed that the patch-slicing approach effectively enhances the module’s prediction 
capability. Additionally, this approach significantly reduces the complexity of the Attention 
module by processing shorter lengths of time series data. The benefits of complexity opti-
mization through patch slicing become more apparent as the length of the input time series 
increases. While other sparse methods may also optimize the module’s complexity, they often 
result in information loss, potentially impacting the prediction performance to some extent.

7  Conclusion and future directions

In this paper, we comprehensively examine the principal models used for time series fore-
casting during the 10-year period from 2014 to 2024. Our focus is on analyzing the underly-
ing processing logic employed by these models. Specifically, we investigate the correlation 
relationships  between  time  steps  and  the  interdependencies  among  time  series  variables. 
We then present approaches explicitly tailored for long-term time series forecasting tasks. 
Furthermore, we provide a concise overview of commonly employed loss functions in time 
series forecasting. In the section dedicated to comparative experiments, we conduct thor-
ough investigations into the performance of the principal models for both univariate and 
multivariate  time  series  prediction  tasks. We  meticulously  explore  and  analyze  the  chal-
lenges  of  overfitting  and  noise  interference  in  existing  complex  models. Throughout  our 
investigation, we identify the distinct advantages of employing simple methods for trend 
term prediction and employing methods based on frequency domain for season term pre-
diction. Moreover, we validate the effectiveness of the patch-slicing method applied to the 
Attention  mechanism  by  assessing  its  performance  in  terms  of  prediction  accuracy  and 
complexity.  Drawing  on  a  comprehensive  analysis  of  existing  research  findings,  we  pro-
pose potential research directions within the field of time series prediction. These directions 
encompass the following areas:

Mining  Dependencies  among  Time  Steps:  Existing  models  have  utilized  time  series 
decomposition methods  to  extract  temporal information such  as  trends  and  seasonal  pat-
terns, but these models still face limitations in effectively mining this information. Explor-
ing seasonal information in the frequency domain remains a promising direction for future 
research. Additionally, capturing time-scale information, non-stationary patterns, and other 
relevant time series information is becoming increasingly important.

Mining  Relationships  among  Time-Series  Variables:  In  datasets  related  to  traffic  or 
weather, there is an inherent correlation among time-series signals from different sensors. 
Therefore, exploring the correlation information between time-series variables is crucial for 
such datasets. However, existing models have paid less attention to extracting relationships 
among time-series variables. Effectively utilizing these relationships remains an important 
research direction.

Complexity Optimization of Models for Long-term Time-Series Prediction: As the length 
of the predicted sequence increases, the computational cost of models becomes more bur-
densome. This issue is particularly prominent in Transformer-based models. Although some 
algorithms have explored complexity optimization for the Attention mechanism, they often 
face the challenge of information loss. Therefore, optimizing the computational cost of the

---

<!-- PAGE 56 -->

23  Page 56 of 67

Attention mechanism without sacrificing prediction accuracy remains a key area for further 
exploration and research.

Investigation  of  Overfitting  in  Complex  Models  for  Time-Series  Prediction:  Relevant 
experiments in this paper indicate that existing complex models often suffer from overfit-
ting  and  noise  interference,  leading  to  prediction  performance  that  is  sometimes  inferior 
to simpler models. Therefore, mitigating overfitting and reducing the impact of noise and 
outliers remain important research directions.

Exploring Flexible Prediction Models: Current time series prediction models are often 
constrained by the fixed length of input and output sequences, meaning they can only be 
used for predetermined prediction lengths. If the prediction length or position changes, these 
models  must  be  redesigned  and  retrained. There  is  a  critical  need  to  develop  time  series 
prediction models that can adapt to flexible prediction scenarios, accommodating changes in 
prediction length and position without requiring extensive redesign or retraining.

Addressing  the  non-stationarity  of  time  series: Although  deep  learning-based  models 
do  not  require  input  sequences  to  be  stationary,  the  non-stationarity  of  time  series,  par-
ticularly the differences in statistical characteristics between the training and test sets, can 
often impact the model’s predictive accuracy. Therefore, exploring and modeling changes 
in the statistical properties of time series is a crucial research direction that can significantly 
enhance predictive accuracy. Research in this area is still in its early stages.

Probabilistic Forecasting: Probabilistic forecasting (Gneiting et al. 2007; Salinas et al. 
2020), which involves estimating the future probability distribution of a time series based 
on its past behavior, is a key area for optimizing predictive models. This approach not only 
improves the robustness and interpretability of models but also equips them with capabili-
ties for risk assessment and management, which are essential in many real-world applica-
tions. Currently, deep learning models for probabilistic forecasting face several challenges, 
including the development of more effective loss functions, improved evaluation metrics, 
and novel model architectures tailored for random processes and probability estimation.

Additional information and experimental results

In this section, we provide additional information and experimental results that support the 
main body of the paper. Section A.1 presents the complete results of the multivariate and 
univariate time series forecasting experiments.

Results of multivariate and univariate time series forecasting 
experiments

---

<!-- PAGE 57 -->

Page 57 of 67  23

Table 13  Multivariate time series forecasting results
Model
ETTh1

Exchange

Model

Data
ILI
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE
Data
ILI
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE

Electricity

Electricity

Exchange

ETTh1

Traffic

Traffic

–

–

–

–

–

TCN

GRU

LSTnet

Trans-
former

ARIMA Short

1.2874 2.3800 1.1574 3.5088 1.0836 2.5038 0.7340 0.8655 1.0963 1.8875
Regular 1.4327 2.8096 1.3296 3.4915 1.0283 2.3477 0.7089 0.8121 0.9924 1.5787
1.0144 1.4551 1.1372 2.2342 0.9696 1.8138 0.7212 0.9080 0.9707 1.5114
Long
0.5794 0.6096 0.7574 0.7717 1.1983 2.7567 0.7619 1.1303 0.3990 0.3258
CNN_1D Short
Regular 0.6664 0.8049 0.8277 0.9209 1.2479 2.9318 0.7632 1.1347 0.5737 0.5905
0.8382 1.1594 0.8659 1.0250 1.3800 3.3879 0.7487 1.0399 –
Long
Short
0.6655 0.8862 0.1834 0.0617 1.1992 2.9021 0.5308 0.7229 0.3129 0.2719
Regular 0.4940 0.4853 0.2512 0.1067 1.3409 3.3631 0.4181 0.5460 0.3670 0.3415
0.6410 0.6933 0.3238 0.1769 1.2214 2.8402 0.5130 0.7605 0.3648 0.2775
Long
0.9030 1.3482 0.8777 1.1188 1.2294 2.8305 0.8119 1.1921 0.8560 1.0811
DeepAR Short
Regular 0.9240 1.3994 0.8975 1.2054 1.2870 3.0435 0.9628 1.6597 0.8409 1.0337
1.1843 2.2798 1.1901 2.2022 1.3712 3.3984 0.8752 1.3683 –
Long
Short
0.7803 1.0360 0.7621 0.0884 1.1508 2.4973 1.2360 2.0568 0.7838 0.8927
Regular 0.7493 0.9711 0.7812 0.8324 1.1799 2.0048 1.2360 2.0568 0.7829 0.8914
0.7687 1.0085 0.7398 0.7430 1.2922 3.0311 0.7532 1.0687 0.7838 0.8884
Long
Short
0.8130 1.1303 0.3699 0.2598 1.1298 2.0822 0.6480 0.8468 0.6181 0.6353
Regular 0.7601 0.9960 0.4955 0.4042 1.2103 2.7753 0.6793 0.9148 0.6986 0.7821
0.7644 0.9953 0.7643 0.8241 1.2546 2.7236 –
Long
Short
0.4745 0.4491 0.2807 0.1393 1.0202 2.1587 0.3148 0.3415 0.3969 0.3283
Regular 0.5174 0.5291 0.3404 0.1804 1.1004 2.3836 0.3896 0.5322 0.3996 0.3080
0.6636 0.8045 0.9066 1.2028 1.2277 2.8575 0.7488 1.0401 0.7871 1.0231
Long
0.5362 0.5482 0.3736 0.2137 0.7762 1.5743 0.5296 0.7651 0.3795 0.2930
LogTrans Short
Regular 0.6392 0.7138 0.3949 0.2508 0.7972 1.6156 0.3617 0.4842 0.4052 0.3248
0.8206 1.1379 0.7025 0.7366 0.8755 1.7925 0.3490 0.4619 0.4057 0.3242
Long
0.4986 0.4984 0.6313 0.5838 1.1229 2.4342 0.3855 0.4504 0.4408 0.3855
Reformer Short
Regular 0.5646 0.6062 0.8194 0.9184 1.2586 2.9970 0.7644 1.1385 0.5078 0.4575
0.7690 1.0775 0.9664 1.2704 1.4413 3.7349 0.7488 1.0402 0.8196 1.0802
Long
Short
0.5023 0.5197 0.3635 0.2122 0.8486 1.6803 0.3533 0.3963 0.4709 0.4322
Regular 0.6482 0.8527 0.4379 0.3113 0.9692 2.1427 0.5002 0.7643 0.4840 0.4424
0.6687 0.8390 0.6804 0.6786 1.0854 2.5005 0.7548 1.1833 0.7731 1.0135
Long
0.5041 0.4961 0.1812 0.0605 0.7902 1.3502 0.3175 0.3744 0.3335 0.1922
Short
Regular 0.4970 0.4796 0.2177 0.0886 0.8397 1.4801 0.3419 0.4202 0.3089 0.2016
0.5766 0.6128 0.3822 0.2579 0.8438 1,5455 0.3393 0.4095 0.3577 0.2609
Long
0.4566 0.4189 0.1815 0.0607 0.6483 0.9915 0.3169 0.3693 0.2973 0.1877
Fedformer Short
Regular 0.4935 0.4754 0.2174 0.0877 0.8024 1.3779 0.3172 0.3699 0.3009 0.1924
0.5714 0.5979 0.3694 0.2429 0.7911 1.3501 0.3234 0.3876 0.4646 0.3942
Long
Short
0.5026 0.5423 0.1159 0.0274 0.8059 1.3679 0.4652 0.6078 0.3185 0.2163
Regular 0.5414 0.6074 0.1693 0.0557 0.9788 1.9403 0.4721 0.6234 0.3370 0.2430
0.6140 0.7113 0.3211 0.1937 1.0026 1.9683 0.4800 0.6799 0.3642 0.2824
Long
0.5810 0.6334 0.5819 0.5126 1.1809 2.6896 0.3602 0.3676 0.4169 0.3459
TDformer Short
Regular 0.5963 0.6530 0.7822 0.8633 1.2581 2.9438 0.3677 0.5183 0.4174 0.3463
0.7826 1.0615 0.8391 1.0206 1.3461 3.3141 0.3816 0.5569 0.4575 0.4160
Long
Short
0.4410 0.4457 0.5003 0.3945 1.0302 2.3503 0.3106 0.3933 0.3696 0.2816
Regular 0.4998 0.5324 0.6505 0.6381 1.1992 2.9159 0.3180 0.4133 0.3706 0.2844
0.6059 0.7076 0.8950 1.1737 1.2093 2.9306 0.3572 0.4899 0.3892 0.3113
Long

ETS-
former

Auto-
former

Informer

AST

---

<!-- PAGE 58 -->

23  Page 58 of 67

Table 13  (continued)

Model

ETTh1

Data
ILI
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE

Electricity

Exchange

Traffic

–

DLinear

Cross-
former

Scal-
eformer

Aliformer Short

Pyrafor-
mer

NS-
Trans-
former

0.7668 1.0024 0.5696 0.5009 1.1775 2.6960 0.7502 1.0473 0.8223 0.9717
Regular 0.8467 1.2102 0.8112 0.8993 1.2329 2.8906 0.7632 1.1348 0.8250 0.9845
0.7632 0.9963 1.0791 1.5914 1.4442 3.7724 0.7487 1.0398 0.8221 0.9674
Long
Short
0.4306 0.4197 0.1199 0.0285 0.5493 0.7300 0.2910 0.3491 0.2646 0.1637
Regular 0.4812 0.4946 0.1695 0.0565 0.7099 1.1508 0.3046 0.3718 0.2771 0.1784
0.6070 0.7074 0.3403 0.2142 0.7579 1.3199 0.3202 0.4008 0.3024 0.2052
Long
Short
0.4132 0.3788 0.2005 0.0723 0.9512 2.0541 0.2453 0.3085 0.2342 0.1458
Regular 0.4522 0.4393 0.2575 0.1118 1.0898 2.4253 0.2718 0.3452 0.2485 0.1647
0.6319 0.8007 0.5546 0.5053 1.1988 2.8067 –
Long
0.2882 0.2022
Short
0.3979 0.3663 0.1109 0.0259 0.6440 0.9567 0.3738 0.5417 0.2676 0.2004
Regular 0.4360 0.4229 0.1775 0.0570 0.7699 1.2162 0.3478 0.5075 0.2741 0.1992
0.5052 0.5197 0.3117 0.1648 0.7994 1.2452 0.3292 0.4681 0.2916 0.2095
Long
Short
0.5480 0.6227 0.1858 0.0635 0.6766 1.0450 0.3054 0.3572 0.3390 0.2359
Regular 0.4643 0.4324 0.1761 0.0600 0.7967 1.4051 0.3159 0.3723 0.3515 0.2607
0.6311 0.7666 0.3905 0.2646 0.8967 1.6122 0.3387 0.4056 0.3749 0.2839
Long
Short
0.4799 0.4682 0.3796 0.2333 0.8096 1.6223 0.4478 0.5959 0.3821 0.2972
Regular 0.5358 0.5705 0.5940 0.5645 1.0740 1.9305 0.4984 0.6638 0.4037 0.3323
0.6907 0.8723 0.7570 0.8616 1.0720 2.3328 –
0.4242 0.3640
Long
0.4008 0.3674 0.1147 0.0283 0.4584 0.5307 0.2654 0.3379 0.2574 0.1860
PatchTST Short
Regular 0.4401 0.4253 0.1609 0.0520 0.6180 0.9902 0.2755 0.3615 0.2631 0.1891
0.5215 0.5509 0.3308 0.2087 0.7424 1.1373 0.2835 0.3857 0.2861 0.2092
Long
0.7668 1.0024 0.1678 0.0510 1.0915 2.4694 –
Triformer Short
Regular 0.4679 0.4429 0.1759 0.0560 1.1890 2.7092 –
0.5562 0.5877 0.5116 0.4676 1.2457 2.9084 –
Long
Short
0.4594 0.4663 0.1995 0.0694 1.3075 3.3835 –
Regular 0.5515 0.5552 0.2317 0.0928 1.2891 3.1048 –
0.5301 0.5571 0.6355 0.6263 1.5055 4.1189 –
Long
Short
0.8618 1.2990 0.4704 0.3884 1.3896 3.3878 –
Regular 0.7075 0.8740 0.3986 0.2668 1.4744 3.7407 –
Long
0.6555 0.6487 1.7026 4.7365 –
–
Short
0.7606 0.9954 0.1854 0.0633 1.2128 2.8800 0.7585 1.1517 0.8219 0.9705
Regular 0.5279 0.5809 0.3018 0.1569 1.2891 3.2390 0.7601 1.1585 0.8221 0.9707
0.7645 0.9986 1.0101 1.4107 1.4179 3.7566 0.7488 1.0398 0.8227 0.9695
Long
Short
0.4210 0.3778 0.8057 0.8961 1.1582 2.5776 0.3417 0.4537 0.3831 0.2984
Regular 0.7381 0.9107 1.0898 1.6129 1.2364 2.9496 0.3521 0.4877 0.4411 0.4289
0.7640 1.0732 1.1855 1.9782 1.3723 3.5140 0.7485 1.0401 0.8189 1.0621
Long
0.4579 0.4353 0.1151 0.0269 0.9474 1.8391 0.3886 0.6086 0.3760 0.2855
N-BEATS Short
Regular 0.6128 0.7949 0.1629 0.0581 1.1330 2.5371 0.6862 1.0418 0.6903 0.8176
0.6682 0.8908 0.3290 0.1797 1.3070 3.1641 0.7400 1.1278 0.7374 0.9044
Long

–
–
–
0.3568 0.2721
0.4493 0.4010
–
–
–
–

Auto-
encoder

–
–
–
–
–
–
–
–
–

SSDNet

–
–
–
–

–
–
–

SAE

TFT

–

–

The best results are highlighted in bold and the second best results are highlighted with a underline.. "–" 
indicates out of memory. ’Short’, ’Regular’, ’Long’ denotes the output length O for short-term, regular-
term and long-term time series prediction

---

<!-- PAGE 59 -->

Table 14  Univariate time series forecasting results
Model
ETTh1

Exchange

Data
ILI
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE

Electricity

Traffic

Page 59 of 67  23

–

–

–

–

–

–

TCN

GRU

LSTnet

Trans-
former

ARIMA Short

0.5341 0.2904 0.8298 0.6908 2.8446 8.1104 1.5089 2.9879 0.8334 0.9120
Regular 0.6769 0.4613 1.1036 1.2307 2.6658 7.1389 1.3781 2.4447 0.7523 0.7447
0.7517 0.5809 1.2046 1.4630 2.0703 4.7428 1.2276 2.1735 0.7134 0.6477
Long
0.5670 0.4782 0.3974 0.2305 0.9066 1.1410 0.8560 1.0486 0.4783 0.3992
CNN-1D Short
Regular 0.5670 0.4779 0.3071 0.1470 1.6404 3.1585 0.8193 0.9720 0.5042 0.4420
Long
0.5506 0.4552 0.6736 0.7026 1.3437 3.3111 0.8555 1.0478 0.5618 0.5150
0.3322 0.2075 0.3275 0.1818 1.4640 2.6350 0.4934 0.4646 0.8229 1.1922
Short
Regular 0.3619 0.2383 0.4640 0.3343 1.5244 2.8274 0.6185 0.6433 0.7375 0.9382
0.3683 0.2410 0.6464 0.6255 1.5310 2.7988 0.4309 0.3664 0.8169 1.0796
Long
0.4840 0.3610 0.9770 1.3248 1.4786 3.6056 1.2122 2.2182 1.1570 1.1570
DeepAR Short
Regular 0.6246 0.5837 0.9870 1.3568 1.4792 2.7966 1.2481 2.3466 1.1761 2.2091
0.7266 0.8006 1.0411 1.5027 1.8888 4.1431 –
Long
Short
0.7675 0.7355 0.8287 1.0144 1.3457 2.3184 1.0187 1.4046 0.8059 1.0043
Regular 0.8253 1.0101 0.8253 1.0101 1.3554 2.3010 1.0186 1.4047 0.8048 1.0039
Long
0.8268 1.0316 0.8268 1.0316 1.3623 2.2733 1.0218 1.4094 0.8020 1.0042
0.6540 0.5656 0.5887 0.4949 1.0897 1.5923 0.7020 0.7594 0.6927 0.6999
Short
Regular 0.6546 0.5675 0.6168 0.5340 1.2049 1.8884 0.7516 0.8135 0.7510 0.8845
0.6601 0.5914 0.9144 1.2287 1.2914 2.0774 –
Long
Short
0.3489 0.2109 0.3423 0.1711 0.7755 0.8995 0.7969 0.9045 0.3996 0.2803
Regular 0.3871 0.2612 0.3652 0.2087 0.8634 1.0702 0.7809 0.8834 0.4730 0.3934
0.5154 0.4288 0.5294 0.3849 0.9816 1.2789 0.8414 1.0310 0.4647 0.3873
Long
0.3415 0.1833 0.3250 0.1686 0.8294 0.8792 1.1643 1.8174 0.4389 0.3623
LogTrans Short
Regular 0.3571 0.2064 0.3857 0.2251 0.8593 0.9287 1.0159 1.4864 0.4432 0.3545
0.4776 0.3544 0.4997 0.3649 0.8999 0.9355 0.8352 1.0665 0.4696 0.4115
Long
0.4624 0.3293 0.5477 0.4349 0.9098 1.2002 0.8658 1.0754 0.5157 0.4667
Reformer Short
Regular 0.5138 0.4088 0.5974 0.5264 1.1512 1.8010 0.9858 1.3908 0.5350 0.4957
0.5397 0.4395 0.7098 0.7446 1.3585 2.2942 0.9435 1.3019 0.5228 0.4851
Long
Short
0.3855 0.2463 0.5156 0.4046 0.9464 1.2762 1.2931 2.3961 0.5526 0.5625
Regular 0.4711 0.3706 0.6412 0.5808 1.0865 1.5350 1.0285 1.5467 0.5740 0.5632
0.5258 0.4454 0.7829 0.8706 1.2137 1.7989 0.8971 1.2184 0.7572 0.9080
Long
Short
0.3437 0.2138 0.1946 0.0638 0.4348 0.3105 0.4294 0.2901 0.4493 0.3648
Regular 0.3634 0.2317 0.2645 0.1154 0.5409 0.4231 0.4619 0.3388 0.4126 0.2988
0.4041 0.2819 0.4783 0.3768 0.6079 0.4947 0.4274 0.2969 0.5767 0.5460
Long
0.3325 0.1992 0.2194 0.0798 0.4053 0.2466 0.4210 0.2826 0.3732 0.2480
Fedformer Short
Regular 0.3555 0.2220 0.2682 0.1212 0.4493 0.2987 0.4261 0.2891 0.3250 0.1967
0.4001 0.2777 0.4739 0.3685 0.5595 0.4466 0.4281 0.2938 0.6163 0.6571
Long
Short
0.3329 0.1994 0.3423 0.1711 0.4790 0.3744 0.5593 0.4885 0.5673 0.5584
Regular 0.3604 0.2298 0.2178 0.0735 0.5411 0.4164 0.5672 0.5067 0.6315 0.6620
0.4194 0.3005 0.3925 0.2265 0.6302 0.5230 0.5756 0.5355 0.6709 0.7967
Long
0.4272 0.3113 0.9326 1.2894 2.0571 4.9538 0.4244 0.3633 0.4163 0.3130
TDformer Short
Regular 0.4779 0.3727 1.1635 1.7472 1.1753 2.6595 0.4572 0.4127 0.4716 0.3981
0.4715 0.3780 1.2804 2.1319 2.1227 5.1123 0.4590 0.4144 0.4954 0.4201
Long
Short
0.5517 0.6820 0.4682 0.3521 1.1750 3.0143 0.3203 0.4072 0.3703 0.2837
Regular 0.5598 0.6656 0.8395 0.9553 1.1257 2.5269 0.3291 0.4288 0.3786 0.2925
0.6219 0.7784 0.9843 1.3628 1.3748 3.8622 0.3398 0.4497 0.3952 0.3203
Long

ETS-
former

Auto-
former

Informer

AST

---

<!-- PAGE 60 -->

23  Page 60 of 67

Table 14  (continued)

Model

ETTh1

Data
ILI
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE

Electricity

Exchange

Traffic

–

Dlinear

Cross-
former

Scal-
eformer

Aliformer Short

Pyrafor-
mer

NS-
Trans-
former

1.0248 1.2065 0.4364 0.2761 1.4713 2.6747 0.9729 1.1016 0.8180 1.0663
Regular 0.8248 1.1298 0.5353 0.3708 1.5087 2.7804 0.9811 1.1930 0.8166 1.0659
0.9166 0.9959 1.3951 2.3686 1.4399 3.7476 0.9827 1.1928 0.8190 1.0657
Long
Short
0.3163 0.1821 0.1541 0.0404 0.3869 0.2530 0.4654 0.3691 0.3133 0.1869
Regular 0.3471 0.2152 0.2235 0.0911 0.4107 0.2840 0.8804 1.1424 0.3189 0.1984
0.5269 0.4747 0.4828 0.3880 0.4165 0.2569 0.9661 1.2290 0.3099 0.1743
Long
Short
0.3146 0.1829 0.2728 0.1187 1.1821 2.1848 0.3915 0.2846 0.3033 0.2277
Regular 0.3404 0.2120 0.3820 0.2287 1.1480 1.5548 0.3784 0.2790 0.2796 0.1818
0.4192 0.2960 0.8162 1.0097 1.1606 1.5138 –
Long
0.3350 0.2443
Short
0.2987 0.1729 0.1413 0.0339 0.6970 0.7121 0.4687 0.4177 0.6975 0.9390
Regular 0.3214 0.1952 0.1953 0.0657 0.9373 1.1032 0.4398 0.3811 0.5960 0.7090
0.3712 0.2455 0.3847 0.2209 0.9340 1.0252 0.4201 0.3443 0.4864 0.4893
Long
Short
0.3003 0.1679 0.1674 0.0471 0.4511 0.3643 0.3051 0.1912 0.4147 0.3031
Regular 0.3131 0.1734 0.2249 0.0862 0.5383 0.4665 0.3163 0.1979 0.4337 0.3384
0.4234 0.3099 0.4641 0.3559 0.5628 0.4290 0.2908 0.1861 0.4706 0.4004
Long
Short
0.4021 0.2615 0.3448 0.1914 1.1677 1.7479 0.4151 0.3509 0.4523 0.3564
Regular 0.5803 0.5474 0.3467 0.1873 1.2846 2.2077 0.4145 0.3491 0.4717 0.3892
0.5070 0.4283 0.6196 0.5879 1.3637 2.2317 0.4308 0.3706 0.5145 0.4510
Long
0.3031 0.1774 0.1566 0.0425 0.2874 0.1614 0.3514 0.2488 0.5249 0.6473
PatchTST Short
Regular 0.3276 0.2021 0.2124 0.0789 0.3542 0.2233 0.3610 0.2606 0.4437 0.4893
0.3693 0.2478 0.4163 0.2917 0.4604 0.3440 0.3700 0.2722 0.3770 0.3589
Long
0.3149 0.1866 0.2410 0.0935 1.7262 3.4845 –
Triformer Short
Regular 0.3334 0.2071 0.3398 0.1900 1.7423 3.4663 –
0.4041 0.2843 0.6297 0.7034 1.4855 2.5357 –
Long
Short
0.3852 0.2125 0.5234 0.4296 1.2492 2.9732 –
Regular 0.3975 0.2325 0.6230 0.5707 1.2936 3.1257 –
0.6813 0.7711 0.5307 0.4244 1.3590 3.3232 –
Long
Short
0.3994 0.2447 0.5471 0.4941 1.2719 2.0677 –
Regular 0.4760 0.3493 0.6099 0.5869 1.3293 2.1916 –
Long
0.8132 1.0029 1.5207 2.7740 –
–
Short
0.3441 0.2095 0.4243 0.2946 1.2054 1.9340 0.7613 1.1320 0.8156 1.0888
Regular 0.3615 0.2281 0.5458 0.4641 1.3731 2.3999 0.9632 1.1615 0.8194 1.0719
0.5640 0.4772 0.7607 0.8692 1.4058 3.6954 0.9643 1.1710 0.8179 1.0794
Long
Short
0.4854 0.3539 0.3752 0.2119 1.1519 2.4958 0.3895 0.3295 0.4836 0.4035
Regular 0.5297 0.4225 0.4577 0.3130 1.6535 3.2258 0.4312 0.3777 0.5179 0.4563
0.7807 1.0845 0.7391 0.8023 1.8888 4.1431 0.4527 0.4081 0.5660 0.5481
Long
0.3119 0.1805 0.2950 0.1354 1.2647 1.8155 0.4647 0.3671 0.5377 0.5074
N-BEATS Short
Regular 0.3660 0.2341 0.3245 0.1733 1.7303 3.4102 0.8803 1.1347 0.6250 0.6499
0.4114 0.2837 0.4720 0.3880 1.5454 2.6395 0.9589 1.2246 0.6735 0.7926
Long

–
–
–
0.3568 0.2721
0.4369 0.3828
–
–
–
–

Auto-
encoder

–
–
–
–
–
–
–
–
–

SSDNet

–
–
–
–

–
–
–

SAE

TFT

–

The best results are highlighted in bold and the second best results are highlighted with a underline. "–" 
indicates out of memory. ’Short’, ’Regular’, ’Long’ denotes the output length O for short-term, regular-
term and long-term time series prediction

---

<!-- PAGE 61 -->

Page 61 of 67  23

Funding  This  work  was  supported  by  the  National  Natural  Science  Foundation  of  China  (Grant  No. 
62206178 and 72301180) and the Stable Support Plan for Higher Education Institutions in Shenzhen (Project 
No. 20231121221536001). The authors have no relevant financial or non-financial interests to disclose.

Open  Access    This  article  is  licensed  under  a  Creative  Commons  Attribution-NonCommercial-
NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and 
reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the 
source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. 
You do not have permission under this licence to share adapted material derived from this article or parts of it. 
The images or other third party material in this article are included in the article’s Creative Commons licence, 
unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative 
Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, 
you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit 
http://creativecommons.org/licenses/by-nc-nd/4.0/.

References

Achiam J, Adler S, Agarwal S, Ahmad L, Akkaya I, Aleman FL, Almeida D, Altenschmidt J, Altman S, Anad-

kat S, et al (2023) Gpt-4 technical report. arXiv preprint arXiv:2303.08774

Al-Tahan H, Mohsenzadeh Y (2021) Clar: Contrastive learning of auditory representations. In: International

conference on artificial intelligence and statistics, pp. 2530–2538. PMLR

Amalou I, Mouhni N, Abdali A (2022) Multivariate time series prediction by RNN architectures for energy

consumption forecasting. Energy Rep 8:1084–1091

Ariyo AA, Adewumi AO, Ayo CK (2014) Stock price prediction using the arima model. In: 2014 UKSim-
AMSS 16th international conference on computer modelling and simulation, pp. 106–112. IEEE
Armstrong JS (2001) Principles of forecasting: a handbook for researchers and practitioners, vol 30. Springer,

Berlin

Asadi R, Regan AC (2020) A spatio-temporal decomposition based deep neural network for time series fore-

casting. Appl Soft Comput 87:105963

Bai S, Kolter JZ, Koltun V (2018) An empirical evaluation of generic convolutional and recurrent networks

for sequence modeling. arXiv preprint arXiv:1803.01271

Bell WR, Hillmer SC (1984) Issues involved with the seasonal adjustment of economic time series. J Bus

Econ Stat 2(4):291–320

Binkowski M, Marti G, Donnat P (2018) Autoregressive convolutional neural networks for asynchronous

time series. In: International conference on machine learning, pp. 580–589. PMLR

Cai L, Janowicz K, Mai G, Yan B, Zhu R (2020) Traffic transformer: capturing the continuity and periodicity

of time series for traffic forecasting. Trans GIS 24(3):736–755

Cao  D, Wang Y,  Duan  J,  Zhang  C,  Zhu  X,  Huang  C, Tong Y,  Xu  B,  Bai  J, Tong  J  (2020)  Spectral  tem-
poral  graph  neural  network  for  multivariate  time-series  forecasting.  Adv  Neural  Inf  Process  Syst 
33:17766–17778

Celeghini E, Gadella M, Olmo MA (2021) Hermite functions and Fourier series. Symmetry 13(5):853
Chakraborty K, Mehrotra K, Mohan CK, Ranka S (1992) Forecasting the behavior of multivariate time series

using neural networks. Neural Netw 5(6):961–970

Challu C, Olivares KG, Oreshkin BN, Ramirez FG, Canseco MM, Dubrawski A (2023) Nhits: Neural hier-
archical interpolation for time series forecasting. In: Proceedings of the AAAI conference on artificial 
intelligence, vol. 37, pp. 6989–6997

Chen  Z,  Ma  M,  Li T, Wang  H,  Li  C  (2023)  Long  sequence  time-series  forecasting  with  deep  learning:  a

survey. Inf Fus 97:101819

Chen Y, Huang J, Xu H, Guo J, Su L (2023) Road traffic flow prediction based on dynamic spatiotemporal

graph attention network. Sci Rep 13(1):14729

Cheng D, Yang F, Xiang S, Liu J (2022) Financial time series forecasting with multi-modality graph neural

network. Pattern Recogn 121:108218

Cirstea R-G, Guo C, Yang B, Kieu T, Dong X, Pan S (2022) Triformer: Triangular, variable-specific attentions

for long sequence multivariate time series forecasting–full version. arXiv preprint arXiv:2204.13767

Cleveland RB, Cleveland WS, McRae JE, Terpenning I (1990) STL: a seasonal-trend decomposition. J Off

Stat 6(1):3–73

Contreras J, Espinola R, Nogales FJ, Conejo AJ (2003) Arima models to predict next-day electricity prices.

IEEE Trans Power Syst 18(3):1014–1020

---

<!-- PAGE 62 -->

23  Page 62 of 67

Cui  Z  (2016)  Multi-scale  convolutional  neural  networks  for  time  series  classification.  arXiv  preprint

arXiv:1603.06995

Dagum EB (2010) Time series modeling and decomposition. Statistica (Bologna) 70(4):433–457
De  Livera AM,  Hyndman  RJ,  Snyder  RD  (2011)  Forecasting  time  series  with  complex  seasonal  patterns

using exponential smoothing. J Am Stat Assoc 106(496):1513–1527

Devlin J, Chang M-W, Lee K, Toutanova K (2018) Bert: Pre-training of deep bidirectional transformers for

language understanding. arXiv preprint arXiv:1810.04805

Dey R, Salem FM (2017) Gate-variants of gated recurrent unit (gru) neural networks. In: 2017 IEEE 60th

international midwest symposium on circuits and systems (MWSCAS), pp. 1597–1600. IEEE

Dinh TN, Thirunavukkarasu GS, Seyedmahmoudian M, Mekhilef S, Stojcevski A (2023) Predicting commer-
cial building energy consumption using a multivariate multilayered long-short term memory time-series 
model. Appl Sci 13(13):7775

Dosovitskiy A, Beyer L, Kolesnikov A, Weissenborn D, Zhai X, Unterthiner T, Dehghani M, Minderer M, 
Heigold G, Gelly S et al. (2020) An image is worth 16x16 words: Transformers for image recognition 
at scale. arXiv preprint arXiv:2010.11929

Du Y, Wang J, Feng W, Pan S, Qin T, Xu R, Wang C (2021) Adarnn: Adaptive learning and forecasting of 
time series. In: Proceedings of the 30th ACM international conference on information and knowledge 
management, pp. 402–411

Durbin J, Koopman SJ (2012) Time series analysis by state space methods, vol 38. Oxford University Press,

Oxford

Edition F, Papoulis A, Pillai SU (2002) Probability, random variables, and stochastic processes. New York,

McGraw-Hill

Ensafi Y, Amin SH, Zhang G, Shah B (2022) Time-series forecasting of seasonal items sales using machine

learning-a comparative analysis. Int J Inf Manag Data Insights 2(1):100058

Fan C, Wang J, Gang W, Li S (2019) Assessment of deep recurrent neural network-based strategies for short-

term building energy predictions. Appl Energy 236:700–710

Fischer T, Krauss C (2018) Deep learning with long short-term memory networks for financial market predic-

tions. Eur J Oper Res 270(2):654–669

Gál V, Hámori J, Roska T, Bálya D, Borostyánkői Z, Brendel M, Lotz K, Négyessy L, Orzó L, Petrás I (2004)

Receptive field atlas and related CNN models. Int J Bifurc Chaos 14(02):551–584

Gneiting T, Balabdaoui F, Raftery AE (2007) Probabilistic forecasts, calibration and sharpness. J R Stat Soc

Ser B Stat Methodol 69(2):243–268

Goodfellow I, Pouget-Abadie J, Mirza M, Xu B, Warde-Farley D, Ozair S, Courville A, Bengio Y (2014)

Generative adversarial nets. Adv Neural Inf Process Syst. 27

Gudelek MU, Boluk SA, Ozbayoglu AM (2017) A deep learning based stock trading model with 2-D CNN 
trend detection. In: 2017 IEEE symposium series on computational intelligence (SSCI), pp. 1–8. IEEE
Guo J, Lin P, Zhang L, Pan Y, Xiao Z (2023) Dynamic adaptive encoder-decoder deep learning networks for

multivariate time series forecasting of building energy consumption. Appl Energy 350:121803

Hajirahimi Z, Khashei M (2023) Hybridization of hybrid structures for time series forecasting: a review. Artif

Intell Rev 56(2):1201–1261

Hatami N, Gavet Y, Debayle J (2018) Classification of time-series images using deep convolutional neural net-
works. In: Tenth international conference on machine vision (ICMV 2017), vol. 10696, pp. 242–249. SPIE
Hewamalage H, Bergmeir C, Bandara K (2021) Recurrent neural networks for time series forecasting: cur-

rent status and future directions. Int J Forecast 37(1):388–427

He K, Zhang X, Ren S, Sun J (2016) Deep residual learning for image recognition. In: Proceedings of the

IEEE conference on computer vision and pattern recognition, pp. 770–778

Hsieh WW (2004) Nonlinear multivariate and time series analysis by neural network methods. Rev Geophys.

https://doi.org/10.1029/2002RG000112

Hu S, Xiong C (2023) High-dimensional population inflow time series forecasting via an interpretable hier-

archical transformer. Transp Res Part C Emerg Technol 146:103962

Hyndman R (2008) Forecasting with Exponential Smoothing: The State Space Approach. Springer, Berlin
Hyndman RJ, Athanasopoulos G (2018) Forecasting: principles and practice. OTexts
Hyndman RJ, Khandakar Y (2008) Automatic time series forecasting: the forecast package for R. J Stat Softw

27:1–22

Hyndman  R,  Koehler AB,  Ord  JK,  Snyder  RD  (2008)  Forecasting  with  exponential  smoothing:  the  state

space approach. Springer, USA

Iwata T, Kumagai A (2020) Few-shot learning for time-series forecasting. arXiv preprint arXiv:2009.14379
Jaiswal A, Babu AR, Zadeh MZ, Banerjee D, Makedon F (2020) A survey on contrastive self-supervised

learning. Technologies 9(1):2

---

<!-- PAGE 63 -->

Page 63 of 67  23

Jiang S, Yu Z-G, Anh VV, Zhou Y (2021) Long-and short-term time series forecasting of air quality by a

multi-scale framework. Environ Pollut 271:116381

Jin M, Zheng Y, Li Y-F, Chen S, Yang B, Pan S (2022) Multivariate time series forecasting with dynamic

graph neural odes. IEEE Trans Knowl Data Eng 35:9168

Jin M, Wen Q, Liang Y, Zhang C, Xue S, Wang X, Zhang J, Wang Y, Chen H, Li X et al. (2023) Large models 
for time series and spatio-temporal data: a survey and outlook. arXiv preprint arXiv:2310.10196
Kim T, Kim J, Tae Y, Park C, Choi J-H, Choo J (2021) Reversible instance normalization for accurate time-
series forecasting against distribution shift. In: International conference on learning representations
Kitaev N, Kaiser Ł, Levskaya A (2020) Reformer: The efficient transformer. arXiv preprint arXiv:2001.04451
Krizhevsky A, Sutskever I, Hinton GE (2017) Imagenet classification with deep convolutional neural net-

works. Commun ACM 60(6):84–90

Lacasa L, Nicosia V, Latora V (2015) Network structure of multivariate time series. Sci Rep 5(1):15508
Lai G, Chang W-C, Yang Y, Liu H (2018) Modeling long-and short-term temporal patterns with deep neural 
networks. In: The 41st international ACM SIGIR conference on research & development in information 
retrieval, pp. 95–104

Le P, Zuidema W (2016) Quantifying the vanishing gradient and long distance dependency problem in recur-

sive neural networks and recursive lstms. arXiv preprint arXiv:1603.00423

Lee S, Hong J, Liu L, Choi W (2024) TS-Fastformer: fast transformer for time-series forecasting. ACM Trans

Intell SystTechnol 15(2):1–20

Li S, Jin X, Xuan Y, Zhou X, Chen W, Wang Y-X, Yan X (2019) Enhancing the locality and breaking the

memory bottleneck of transformer on time series forecasting. Adv Neural Inf Process Syst. 32

Liang Y, Liu Y, Wang X, Zhao Z (2024) Exploring large language models for human mobility prediction

under public events. Comput Environ Urban Syst 112:102153

Liao R, Xiong Y, Fetaya E, Zhang L, Yoon K, Pitkow X, Urtasun R, Zemel R (2018) Reviving and improving

recurrent back-propagation. In: International conference on machine learning, pp. 3082–3091. PMLR

Lim B, Arık SÖ, Loeff N, Pfister T (2021) Temporal fusion transformers for interpretable multi-horizon time

series forecasting. Int J Forecast 37(4):1748–1764

Li Z, Qi S, Li Y, Xu Z (2023) Revisiting long-term time series forecasting: An investigation on linear map-

ping. arXiv preprint arXiv:2305.10721

Lin Y, Koprinska I, Rana M (2021) SsdNet: State space decomposition neural network for time series fore-

casting. In: 2021 IEEE International conference on data mining (ICDM), pp. 370–378. IEEE

Lin H, Gharehbaghi A, Zhang Q, Band SS, Pai HT, Chau K-W, Mosavi A (2022) Time series-based ground-
water level forecasting using gated recurrent unit deep neural networks. Eng Appl Comput Fluid Mech 
16(1):1655–1672

Liu  Z, Yang  X  (2022)  Cross  validation  for  uncertain  autoregressive  model.  Commun  Stat  Simul  Comput

51(8):4715–4726

Liu C-L, Hsaio W-H, Tu Y-C (2018) Time series classification with multivariate convolutional neural net-

work. IEEE Trans Industr Electron 66(6):4788–4797

Liu Z, Lin Y, Cao Y, Hu H, Wei Y, Zhang Z, Lin S, Guo B (2021) Swin transformer: Hierarchical vision trans-
former  using  shifted  windows.  In:  Proceedings  of  the  IEEE/CVF  international  conference  on  computer 
vision, pp. 10012–10022

Liu S, Yu H, Liao C, Li J, Li W, Liu AX, Dustdar S (2021) Pyraformer: Low-complexity pyramidal atten-
tion  for  long-range  time  series  modeling  and  forecasting.  In:  International  conference  on  learning 
representations

Liu Y, Wu H, Wang J, Long M (2022) Non-stationary transformers: exploring the stationarity in time series

forecasting. Adv Neural Inf Process Syst 35:9881–9893

Liu Y, Hu T, Zhang H, Wu H, Wang S, Ma L, Long M (2023) itransformer: Inverted transformers are effective

for time series forecasting. arXiv preprint arXiv:2310.06625

Liu Z, Cheng M, Li Z, Huang Z, Liu Q, Xie Y, Chen E (2024) Adaptive normalization for non-stationary time

series forecasting: A temporal slice perspective. Adv Neural Inf Process Syst. 36

Lu W, Li J, Li Y, Sun A, Wang J (2020) A CNN-LSTM-based model to forecast stock prices. Complexity

2020:1–10

Luo W, Li Y, Urtasun R, Zemel R (2016) Understanding the effective receptive field in deep convolutional

neural networks. Adv Neural Inf Process Syst. 29

Lv Y, Duan Y, Kang W, Li Z, Wang F-Y (2014) Traffic flow prediction with big data: a deep learning approach.

IEEE Trans Intell Transp Syst 16(2):865–873

Lyu H, Sha N, Qin S, Yan M, Xie Y, Wang R (2019) Advances in neural information processing systems. Adv

Neural Inf Process Syst. 32

Ma M, Xie P, Teng F, Wang B, Ji S, Zhang J, Li T (2023) Histgnn: Hierarchical spatio-temporal graph neural

network for weather forecasting. Inf Sci 648:119580

---

<!-- PAGE 64 -->

23  Page 64 of 67

Maggiolo M, Spanakis G (2019) Autoregressive convolutional recurrent neural network for univariate and

multivariate time series prediction. arXiv preprint arXiv:1903.02540

Malenica I, Phillips RV, Pirracchio R, Chambaz A, Hubbard A, Laan MJ (2021) Personalized online machine

learning. arXiv preprint arXiv:2109.10452

Mao J, Middleton SE, Niranjan M (2023) Prompt position really matters in few-shot and zero-shot NLU

tasks. arXiv preprint arXiv:2305.14493

Markova M (2022) Convolutional neural networks for forex time series forecasting. In: AIP conference pro-

ceedings, vol. 2459. AIP Publishing

Mathieu M, Henaff M, LeCun Y (2013) Fast training of convolutional networks through ffts. arXiv preprint

arXiv:1312.5851

Miller JA, Aldosari M, Saeed F, Barna NH, Rana S, Arpinar IB, Liu N (2024) A survey of deep learning and

foundation models for time series forecasting. arXiv preprint arXiv:2401.13912

Mintarsih  F,  Rasyidi  MA,  Nurjannah  W,  Khairani  D,  Sukmana  HT(2023)  Lstm  variants  comparison  for 
exchange rate idr/usd forecasting with rolling window cross validation. In: 2023 Eighth international 
conference on informatics and computing (ICIC), pp. 1–4. IEEE

Mogren  O  (2016)  Continuous  recurrent  neural  networks  with  adversarial  training.  arXiv  preprint

arXiv:1611.09904

Muandet K, Balduzzi D, Schölkopf B (2013) Domain generalization via invariant feature representation. In:

International conference on machine learning, pp. 10–18. PMLR

Mung PS, Phyu S (2023) Time series weather data forecasting using deep learning. In: 2023 IEEE conference

on computer applications (ICCA), pp. 254–259. IEEE

Murray FT, Ringwood JV, Austin PC (2000) Integration of multi-time-scale models in time series forecast-

ing. Int J Syst Sci 31(10):1249–1260

Nie Y, Nguyen NH, Sinthong P, Kalagnanam J (2022) A time series is worth 64 words: Long-term forecasting

with transformers. arXiv preprint arXiv:2211.14730

Niu  Z,  Zhong  G, Yu  H  (2021) A  review  on  the  attention  mechanism  of  deep  learning.  Neurocomputing

452:48–62

Noh  S-H  (2021)  Analysis  of  gradient  vanishing  of  RNNS  and  performance  comparison.  Information

12(11):442

Orang O, Silva PC, Guimarães FG (2023) Time series forecasting using fuzzy cognitive maps: a survey. Artif

Intell Rev 56(8):7733–7794

Oreshkin BN, Carpov D, Chapados N, Bengio Y (2019) N-beats: Neural basis expansion analysis for inter-

pretable time series forecasting. arXiv preprint arXiv:1905.10437

Parzen E (1961) An approach to time series analysis. Ann Math Stat 32(4):951–989
Pascanu R, Mikolov T, Bengio Y (2013) On the difficulty of training recurrent neural networks. In: interna-

tional conference on machine learning, pp. 1310–1318. PMLR

Passalis N, Tefas A, Kanniainen J, Gabbouj M, Iosifidis A (2019) Deep adaptive input normalization for time

series forecasting. IEEE Trans Neural Netw Learn Syst 31(9):3760–3765

Pavlov-Kagadejev M, Jovanovic L, Bacanin N, Deveci M, Zivkovic M, Tuba M, Strumberger I, Pedrycz W 
(2024) Optimizing long-short-term memory models via metaheuristics for decomposition aided wind 
energy generation forecasting. Artif Intell Rev 57(3):45

Pöppelbaum J, Chadha GS, Schwung A (2022) Contrastive learning based self-supervised time-series analy-

sis. Appl Soft Comput 117:108397

Qi M, Zhang GP (2008) Trend time-series modeling and forecasting with neural networks. IEEE Trans Neu-

ral Netw 19(5):808–816

Qi X, Hou K, Liu T, Yu Z, Hu S, Ou W (2021) From known to unknown: Knowledge-guided transformer for

time-series sales forecasting in alibaba. arXiv preprint arXiv:2109.08381

Rawat AS, Chen J, Yu FXX, Suresh AT, Kumar S (2019) Sampled Softmax with random Fourier features.

Adv Neural Inf Process Syst. 32

Salinas D, Flunkert V, Gasthaus J, Januschowski T (2020) Deepar: probabilistic forecasting with autoregres-

sive recurrent networks. Int J Forecast 36(3):1181–1191

Seeger MW, Salinas D, Flunkert V (2016) Bayesian intermittent demand forecasting for large inventories.

Adv Neural Inf Process Syst. 29
Series ST forecasting seasonal time series
Shabani, A., Abdi, A., Meng, L., Sylvain, T.: Scaleformer: iterative multi-scale refining transformers for time

series forecasting. arXiv preprint arXiv:2206.04038 (2022)

Shelatkar T, Tondale S, Yadav S, Ahir S (2020) Web traffic time series forecasting using ARIMA and LSTM

RNN. In: ITM Web of Conferences, Vol 32, p. 03017. EDP Sciences

---

<!-- PAGE 65 -->

Page 65 of 67  23

Shi X, Chen Z, Wang H, Yeung D-Y, Wong W-K, Woo W-c (2015) Convolutional lstm network: a machine

learning approach for precipitation nowcasting. Adv Neural Inf Process Syst. 28

Shin T, Razeghi Y, Logan IV RL, Wallace E, Singh S (2020) Autoprompt: Eliciting knowledge from language

models with automatically generated prompts. arXiv preprint arXiv:2010.15980

Soltani  S  (2002)  On  the  use  of  the  wavelet  decomposition  for  time  series  prediction.  Neurocomputing

48(1–4):267–277

Son NN, Van Cuong N (2023) Neuro-evolutionary for time series forecasting and its application in hourly

energy consumption prediction. Neural Comput Appl 35(29):21697–21707

Szegedy C, Liu W, Jia Y, Sermanet P, Reed S, Anguelov D, Erhan D, Vanhoucke V, Rabinovich A (2015) 
Going deeper with convolutions. In: Proceedings of the IEEE conference on computer vision and pat-
tern recognition, pp. 1–9

Tang W, Long G, Liu L, Zhou T, Jiang J, Blumenstein M (2020) Rethinking 1d-cnn for time series classifica-

tion: A stronger baseline. arXiv preprint arXiv:2002.10061, 1–7

Tang Y, Yu F, Pedrycz W, Yang X, Wang J, Liu S (2021) Building trend fuzzy granulation-based LSTM recur-
rent neural network for long-term time-series forecasting. IEEE Trans Fuzzy Syst 30(6):1599–1613

Taylor SJ, Letham B (2018) Forecasting at scale. Am Stat 72(1):37–45
Ulyanov D, Vedaldi A, Lempitsky V (2016) Instance normalization: The missing ingredient for fast styliza-

tion. arXiv preprint arXiv:1607.08022

Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser Ł, Polosukhin I (2017) Attention

is all you need. Adv Neural Inf Process Syst. 30

Venkateshwari P, Veeraiah V, Talukdar V, Gupta DN, Anand R, Gupta A (2023) Smart city technical planning 
based on time series forecasting of iot data. In: 2023 international conference on sustainable emerging 
innovations in engineering and technology (ICSEIET), pp. 646–651. IEEE

Verbesselt J, Hyndman R, Newnham G, Culvenor D (2010) Detecting trend and seasonal changes in satellite

image time series. Remote Sens Environ 114(1):106–115

Wang Z, Bovik AC (2009) Mean squared error: love it or leave it? A new look at signal fidelity measures.

IEEE Signal Process Mag 26(1):98–117

Wang  X,  Cai  Z,  Luo Y, Wen  Z, Ying  S  (2022)  Long  time  series  deep  forecasting  with  multiscale  feature

extraction and seq2seq attention mechanism. Neural Process Lett 54(4):3443–3466

Wang Z, Liu N, Chen C, Guo Y (2023) Adaptive self-attention LSTM for RUL prediction of lithium-ion

batteries. Inf Sci 635:398–413

Wang S, Fan Y, Jin S, Takyi-Aninakwa P, Fernandez C (2023) Improved anti-noise adaptive long short-term 
memory neural network modeling for the robust remaining useful life prediction of lithium-ion batter-
ies. Reliab Eng Syst Safety 230:108920

Weerakody PB, Wong KW, Wang G, Ela W (2021) A review of irregular time series data handling with gated

recurrent neural networks. Neurocomputing 441:161–178

Wen Q, Sun L, Yang F, Song X, Gao J, Wang X, Xu H (2020) Time series data augmentation for deep learn-

ing: a survey. arXiv preprint arXiv:2002.12478

Wen Q, Zhou T, Zhang C, Chen W, Ma Z, Yan J, Sun L (2022) Transformers in time series: a survey. arXiv

preprint arXiv:2202.07125

West M (1997) Time series decomposition. Biometrika 84(2):489–494
Weston J, Chopra S, Bordes A (2014) Memory networks. arXiv preprint arXiv:1410.3916
Woo G, Liu C, Sahoo D, Kumar A, Hoi S (2022) Etsformer: Exponential smoothing transformers for time-

series forecasting. arXiv preprint arXiv:2202.01381

Woodward WA, Gray HL (1993) Global warming and the problem of testing for trend in time series data. J

Clim 6(5):953–962

Wu S, Xiao X, Ding Q, Zhao P, Wei Y, Huang J (2020) Adversarial sparse transformer for time series fore-

casting. Adv Neural Inf Process Syst 33:17105–17115

Wu H, Xu J, Wang J, Long M (2021) Autoformer: decomposition transformers with auto-correlation for long-

term series forecasting. Adv Neural Inf Process Syst 34:22419–22430

Yazdanbakhsh O,  Dick S  (2019) Multivariate time series classification using dilated convolutional neural

network. arXiv preprint arXiv:1905.01697

Yin J, Rao W, Yuan M, Zeng J, Zhao K, Zhang C, Li J, Zhao Q (2019) Experimental study of multivariate 
time series forecasting models. In: Proceedings of the 28th ACM international conference on informa-
tion and knowledge management, pp. 2833–2839

Young, J., Chen, J., Huang, F., Peng, J.: Dateformer: Time-modeling transformer for longer-term series fore-

casting. arXiv preprint arXiv:2207.05397 (2022)

---

<!-- PAGE 66 -->

23  Page 66 of 67

Yu  F,  Koltun  V  (2015)  Multi-scale  context  aggregation  by  dilated  convolutions.  arXiv  preprint

arXiv:1511.07122

Yun C, Bhojanapalli S, Rawat AS, Reddi SJ, Kumar S (2019) Are transformers universal approximators of

sequence-to-sequence functions? arXiv preprint arXiv:1912.10077

Zhai Y, Lv Z, Zhao J, Wang W (2023) Knowledge discovery and variable scale evaluation for long series

data. Artif Intell Rev 56(4):3157–3180

Zhang GP (2003) Time series forecasting using a hybrid ARIMA and neural network model. Neurocomput-

ing 50:159–175

Zhang Y, Yan J (2022) Crossformer: Transformer utilizing cross-dimension dependency for multivariate time

series forecasting. In: The eleventh international conference on learning representations

Zhang X, Jin X, Gopalswamy K, Gupta G, Park Y, Shi X, Wang H, Maddix DC, Wang Y (2022) First de-trend

then attend: Rethinking attention for time-series forecasting. arXiv preprint arXiv:2212.08151

Zhang X, Li Q, Liang D (2023) An adaptive spatio-temporal neural network for PM2.5 concentration fore-

casting. Artif Intell Rev 56(12):14483–14510

Zhang J, Li X, Tian J, Luo H, Yin S (2023) An integrated multi-head dual sparse self-attention network for

remaining useful life prediction. Reliab Eng Syst Safety 233:109096

Zhang K, Zhou F, Wu L, Xie N, He Z (2024) Semantic understanding and prompt engineering for large-scale

traffic data imputation. Inf Fus 102:102038

Zhao B, Lu H, Chen S, Liu J, Wu D (2017) Convolutional neural networks for time series classification. J

Syst Eng Electron 28(1):162–169

Zhao WX, Zhou K, Li J, Tang T, Wang X, Hou Y, Min Y, Zhang B, Zhang J, Dong Z, et al (2023) A survey

of large language models. Preprint at arXiv:2303.18223

Zheng S, Ristovski K, Farahat A, Gupta C (2017) Long short-term memory network for remaining useful life 
estimation. In: 2017 IEEE international conference on prognostics and health management (ICPHM), 
pp. 88–95. IEEE

Zhong  X,  Cambria  E  (2023)  Time  expression  recognition  and  normalization:  a  survey.  Artif  Intell  Rev

56(9):9115–9140

Zhou H, Zhang S, Peng J, Zhang S, Li J, Xiong H, Zhang W (2021) Informer: Beyond efficient transformer 
for long sequence time-series forecasting. In: Proceedings of the AAAI conference on artificial intel-
ligence, vol. 35, pp. 11106–11115

Zhou T, Ma Z, Wen Q, Wang X, Sun L, Jin R (2022) Fedformer: Frequency enhanced decomposed trans-
former for long-term series forecasting. In: International conference on machine learning, pp. 27268–
27286. PMLR

Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.

Authors and Affiliations

Xiaobao Song1,2 · Liwei Deng2 · Hao Wang1,2 · Yaoan Zhang2 · Yuxin He3 · 
Wenming Cao1,2

Hao Wang

haowang@szu.edu.cn

Xiaobao Song
2020284089@email.szu.edu.cn

Liwei Deng
2021280356@email.szu.edu.cn

Yaoan Zhang
2021280103@email.szu.edu.cn

Yuxin He
heyuxin@sztu.edu.cn

---

<!-- PAGE 67 -->

Page 67 of 67  23

Wenming Cao
wmcao@szu.edu.cn

1  Guangdong Provincial Key Laboratory of Intelligent Information Processing, Shenzhen

University, Shenzhen, China

2  Guangdong Multimedia Information Service Engineering Technology Research Cente,

Shenzhen University, Shenzhen, China

3  College of Urban Transportation and Logistics, Shenzhen Technology University, Shenzhen,

China

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Artificial Intelligence Review (2025) 58:23
https://doi.org/10.1007/s10462-024-10989-8
Deep learning-based time series forecasting
Xiaobao Song1,2 · Liwei Deng2 · Hao Wang1,2 · Yaoan Zhang2 · Yuxin He3 ·
Wenming Cao1,2
Accepted: 4 October 2024 / Published online: 25 November 2024
© The Author(s) 2024
Abstract
With the advancement of deep learning algorithms and the growing availability of com-
putational power, deep learning-based forecasting methods have gained significant im-
portance in the domain of time series forecasting. In the past decade, there has been
a rapid rise in time series forecasting approaches. This paper comprehensively reviews
the advancements in deep learning-based forecasting models spanning 2014 to 2024.
We provide a comprehensive examination of the capabilities of these models in captur-
ing correlations among time steps and time series variables. Additionally, we explore
methods to enhance the efficiency of long-term time series forecasting and summarize
the diverse loss functions employed in these models. Moreover, this study systematically
evaluates the effectiveness of these approaches in both univariate and multivariate time
series forecasting tasks across diverse domains. We comprehensively discuss the strengths
and limitations of various algorithms from multiple perspectives, analyze their capacity
to capture different types of time series information, including trend and season patterns,
and compare methods for enhancing the computational efficiency of these models. Fi-
nally, we summarize the experimental results and discuss the future directions in time
series forecasting. Codes and datasets are available at https://github.com/TCCofWANG/
Deep-Learning-based-Time-Series-Forecasting.
Keywords Time series forecasting · Deep learning · Time series decomposition
1 Introduction
1.1 Objective
Time series forecasting plays a crucial role in numerous applications, such as energy con-
sumption (Wu et al. 2021; Guo et al. 2023; Son and Van Cuong 2023; Dinh et al. 2023),
transportation planning (Venkateshwari et al. 2023; Hu and Xiong 2023; Chen et al. 2023)
and weather forecasting (Ma et al. 2023; Mung and Phyu 2023; Chen et al. 2023). In these
practical application scenarios, forecasting future time series with the help of historical data
Extended author information available on the last page of the article
1 3

23 Page 2 of 67 X. Song et al.
Fig. 1 Process of time series forecasting
is of great significance for long-term planning and early warning in related fields (Wang et
al. 2023; Miller et al. 2024). This process can be shown in Fig. 1. Therefore, this paper aims
to explore deep learning-based time series forecasting models from multiple perspectives,
offering a comprehensive evaluation of current mainstream models and encouraging readers
to consider future directions for development in this field.
1.2 Review of existing approaches
Next, we will summarize the existing methods from four main perspectives: time-step
dependencies, correlations between temporal variables, the trade-off between expanding the
model’s receptive field and reducing computational costs, and loss functions.
Time series information usually consists of time-step dependencies and correlations
between temporal variables (Parzen 1961; Lacasa et al. 2015; Hsieh 2004; Orang et al.
2023). Fully exploiting these two types of information plays a crucial role in improving the
model’s capability. Traditional models like the autoregressive integrated moving average
(ARIMA) (Zhang 2003; Ariyo et al. 2014; Contreras et al. 2003) rely on statistical proper-
ties to extract information. However, they often fall short in fully capturing the time-step
dependencies within complex time series. This is because traditional models primarily focus
on linear features, while real-time series data usually contains intricate nonlinear correla-
tions. As a result, traditional models struggle to adequately leverage these dependencies.
In recent years, with the development of algorithms related to deep lCR121earning and the
improvement of computational power, deep learning-based methods have become increas-
ingly crucial in time series forecasting. Autoencoder and Stacked Autoencoders (SAE) (Lv
et al. 2014) are utilized to extract the time-step features of the time series and obtain the pre-
diction results directly. (CNNs) (Gudelek et al. 2017; Markova 2022; Lu et al. 2020; Zhao
et al. 2017; Liu et al. 2018; Hatami et al. 2018) are often used to extract time-series features
in the short-term range because of their ability to aggregate time-step data in the receptive
field. To capture a broader range of temporal dependencies, the Temporal Convolutional
Network (TCN) (Bai et al. 2018) expands the receptive field of its convolutional kernel.
Specifically, TCN introduces dilated causal convolutions to time-series forecasting tasks. In
1 3

Deep learning-based time series forecasting Page 3 of 67 23
contrast, Recurrent Neural Networks (RNNs) (Shi et al. 2015; Dey and Salem 2017; Sali-
nas et al. 2020; Hajirahimi and Khashei 2023; Lai et al. 2018) are specialized for temporal
sequences and, theoretically, do not suffer from the limited receptive fields characteristic of
CNNs. However, related studies have shown that the recurrent structure of RNNs can lead
to issues such as vanishing gradient, limiting their ability to leverage long-term dependen-
cies in time series. To address this, researchers have developed models like Long Short-
Term Memory (LSTM) (Shi et al. 2015; Fischer and Krauss 2018; Zheng et al. 2017) and
Gated Recurrent Units (GRU) (Dey and Salem 2017), which employ gating mechanisms
to better capture long-term temporal correlations. Despite these advancements, LSTM and
GRU models still face challenges, such as vanishing gradient (Pascanu et al. 2013; Noh
2021; Le and Zuidema 2016) and error accumulation during training (Tang et al. 2021; Fan
et al. 2019; Liao et al. 20185), which are common in RNN architectures. The effectiveness
(Hewamalage et al. 2021; Pavlov-Kagadejev et al. 2024) of RNN-based forecasting models
declines with longer forecasting time steps.
Given the exceptional performance of Transformer models in both natural language pro-
cessing (Vaswani et al. 2017; Devlin et al. 2018) and image processing (Dosovitskiy et al.
2020) domains, these models are now being introduced to time series forecasting (Wu et al.
2021; Li et al. 2019; Zhou et al. 2021). Compared with RNN-based models, Transformer
based models adopt an encoder-decoder structure (Wang et al. 2022; Woo et al. 2022; Lee et
al. 2024) and the attention mechanism (Liu et al. 2023; Niu et al. 2021; Young et al. 2022).
It can dramatically alleviate the error accumulation (Li et al. 2019; Zhou et al. 2021) in long-
term time-series forecasting tasks. However, the authors of DLinear (Yun et al. 2019) point
out that the attention mechanism is permutation invariance. The Transformer model does
not make good use of time series order information. To solve this problem, DLinear uses a
linear layer to implement time series forecasting.
Generally speaking, the correlation between time steps in a time series comprises mul-
tiple patterns (Cleveland et al. 1990; Hyndman and Athanasopoulos 2018; Dagum 2010),
including trend (Verbesselt et al. 2010) [62] (Qi and Zhang 2008; Woodward and Gray
1993), seasonal patterns (Bell and Hillmer 1984; De Livera et al. 2011), etc. To reduce the
complexity of time series forecasting and capture these temporal patterns, some models
have introduced time series decomposition techniques (Wu et al. 2021; Zhou et al. 2022;
Oreshkin et al. 2019; Woo et al. 2022). These approaches initially decompose the time
series into several components, usually containing trend information, seasonal information,
time-scale information (Taylor and Letham 2018; Jiang et al. 2021; Murray et al. 2000),
and other time-series information. Subsequently, the model analyzes these distinct elements
using specialized modules. For instance, Autoformer (Wu et al. 2021) utilizes a mean filter
to convolve the input sequence, extracting trend terms that represent the time series’ trend
patterns. Similarly, Fedformer (Zhou et al. 2022) employs multiple mean filters of varying
sizes to derive trend terms, effectively addressing the limited receptive field issue. LSTnet
(Lai et al. 2018) employs linear mapping to extract trend information from sequences and
incorporates a predefined window to minimize the impact of distant information on trend
forecasting. N-BEATS (Oreshkin et al. 2019) adopts a polynomial fitting method to model
the time series’ trend terms. Similarly, both DLinear (Yun et al. 2019) and TDformer (Zhang
et al. 2022) utilize shallow linear layers for this purpose. For seasonal information, LSTnet
introduces a skip-connection architecture based on LSTM, enabling the model to account
for information from time steps preceding a fixed interval, thereby capturing seasonal infor-
1 3

23 Page 4 of 67 X. Song et al.
mation in the data. Autoformer enhances the ability of the attention mechanism to discern
seasonal patterns by using time-delayed similarities of the input. Fedformer, on the other
hand, transforms the input time series into the frequency domain and employs an attention
mechanism to analyze similarities between frequency components, effectively capturing the
periodicity of the time series. ETSformer (Woo et al. 2022) filters frequency components
based on their magnitude, reducing noise interference in seasonal information capturing.
Time-scale information (Zhai et al. 2023), referring to the correlation of time steps at dif-
ferent scales, is addressed by models like Scaleformer (Shabani et al. 2022) and Pyraformer
(Liu et al. 2021). The former applies downsampling to acquire inputs at various temporal
scales and uses a forecasting model for multi-scale predictions. The latter processes time
series at different scales and employs an attention mechanism to derive cross-scale attention
correlations.
In addition to time-step dependencies, the essence of time series information also lies in
the cross-time-step correlations among variables (Chakraborty et al. 1992; Yin et al. 2019).
Thus, feature extraction of time series variables and exploring the inter-variable correlations
are crucial for accurate forecasting. The TFT (Lim et al. 2021) employs RNN for feature
extraction from time series variables and incorporates a feature filtering module to identify
and utilize valuable information within these features. Aliformer (Qi et al. 2021) catego-
rizes input time-series variables and incorporates future information about these variables,
enhancing the model’s forecasting capabilities. Crossformer (Zhang and Yan 2022) lever-
ages the attention mechanism to analyze attention-based correlations between variables,
offering a nuanced approach to understanding their interplay. It is worth noting that in recent
years, with the development of large language models(LLMS) (Zhao et al. 2023) like Chat-
GPT (Achiam et al. 2023), LLMs can directly or indirectly generate prediction sequences
through prompt engineering (Liang et al. 2024; Zhang et al. 2024).
CNN models are constrained by their limited receptive field, hindering their ability to
effectively capture long-term time series data (Tang et al. 2020; Gál et al. 2004; Luo et al.
2016). The RNN model, due to the problems of error accumulation, vanishing gradient, and
exploding gradient, also cannot handle the long-term time series prediction task well. While
Transformer models circumvent these issues, the attention mechanism’s computational cost
grows quadratically with the series length, rendering the traditional Transformer impractical
for long-term forecasting (Li et al. 2019). Therefore, some research is devoted to reduc-
ing the computational cost of the attention mechanism, primarily through sparse attention
mechanisms or shortening time series length. Related studies based on the sparse attention
mechanism include: LogTrans (Li et al. 2019) filters the target of attention computation
based on the distance between time steps, reducing computation. Reformer (Kitaev et al.
2020) maps the data into a hash space and filters the target of attention computation based
on the distance among time steps in the hash space. Informer (Zhou et al. 2021) filters the
target of attention computation based on computational output distribution. Related studies
on reducing series length include: Informer utilizes convolutional aggregation of time steps
in the receptive field. Convolutional aggregation reduces the input series length of the atten-
tion mechanism. PatchTST (Nie et al. 2022) slices long sequences into multiple fixed-size
patches, reducing the attention mechanism’s computational cost.
Regarding loss function, the above deep learning-based models commonly use Mean
Absolute Error (MAE) or Mean Squared Error (MSE) to evaluate the gap between predic-
tions and actual outcomes (Li et al. 2019; Zhou et al. 2021; Kitaev et al. 2020; Zhou et
1 3

Deep learning-based time series forecasting Page 5 of 67 23
al. 2022; Oreshkin et al. 2019). However, using MAE or MSE as the sole optimization
objective has some limitations (Goodfellow et al. 2014; Mogren 2016; Lyu et al. 2019).
In response, several models have innovated upon the traditional loss function to address
this issue. For instance, DeepAR (Salinas et al. 2020) converts the model output from spe-
cific values to probability distributions, using negative log-likelihood as its loss function.
Similarly, SSDNet (Lin et al. 2021) integrates negative log-likelihood with MAE to form a
hybrid loss function, allowing for the assessment of discrepancies in both value and prob-
ability terms. AST (Wu et al. 2020) employs a strategy inspired by the training mechanism
of generative adversarial networks (GANs) (Goodfellow et al. 2014), comprising both dis-
criminant loss and generative loss components. This approach facilitates the alignment of
the predicted distribution with the actual data distribution.
Deep learning architectures usually require large-scale labeled datasets for achieving
good performance on forecasting time series. Recent techniques of self-supervised learn-
ing (Pöppelbaum et al. 2022; Jaiswal et al. 2020) have opened up new a research frontier
where deep learning architectures can learn general features from unlabeled time series.
The task of self-supervised learning is usually accomplished with some sort of time-series
augmentation such as flipping, random noise, time warping, and random smoothing. Based
on these data augmentation methods (Wen et al. 2020; Cui 2016) and the strategy of contras-
tive training (Pöppelbaum et al. 2022; Al-Tahan and Mohsenzadeh 2021), deep learning-
based time-series prediction models can capture temporal features during the pre-training
phase. Subsequently, with a small amount of labeled data, they train the predictor to carry
out predictions. At the same time, recent technology has also leveraged Few-Shot Learn-
ing to address the challenge of limited large-scale labeled datasets. This approach involves
training the model on various public datasets, enabling it to extract time-series features
effectively and exhibit strong generalization capabilities. Such a strategy leads to enhanced
performance when applied to new datasets. Methods employing Few-Shot Learning can
be categorized into two distinct directions. In Direction 1, the Memory network (Weston
et al. 2014) approach is utilized. This involves encoding historical time-series data dur-
ing training and retrieving these encodings when presented with new time-series datasets.
This allows the model to identify similar patterns and make accurate predictions (Iwata
and Kumagai 2020). Direction 2 involves using pre-trained LLMs known for their robust
generalization abilities to generate precise predictions for time series data (Jin et al. 2023).
1.3 Highlights
The contributions of this paper are as follows:
– This paper provides a systematic review of the evolution of deep learning-based time
series forecasting models from multiple perspectives. It thoroughly examines the ability
of various models to capture correlations both between time steps and among variables,
explores the trade-offs between expanding the model’s receptive field and reducing
computational costs, and analyzes commonly used loss functions.
– This paper conducts a comprehensive evaluation of the effectiveness of various deep
learning-based time series forecasting models in both univariate and multivariate tasks
across different domains. Through experiments, we uncover the strengths and weak-
nesses of different algorithms, assess their ability to capture various types of time series
1 3

23 Page 6 of 67 X. Song et al.
patterns (including trends and seasonal variations), and discuss strategies to enhance the
computational efficiency of these models.
– Finally, this paper discusses future directions in the field of time series forecasting based
on the analysis results.The organization of this paper is as follows. Section 2 introduces
the background knowledge used in this survey. Section 3 traces the progress of such
models from 2014 to 2024, focusing on the logic behind time series information mining,
including correlation among the time step and correlation among variables. Section 4
discusses the strategies for reducing computational costs in long-term forecasting. Sec-
tion 5 summarizes the loss functions utilized in deep learning-based time series fore-
casting. In Sect. 6, we conduct experiments on the discussed models and methods across
several datasets. We demonstrate the advantages and disadvantages of various algo-
rithms from different perspectives, such as prediction accuracy, information extraction
capabilities, the ability to identify trend and seasonal patterns, and the impact of differ-
ent attention mechanisms. In Sect. 7, we summarize the experimental results and discuss
the prospective directions for the future development of time series forecasting.
2 Background
In this section, we will briefly introduce the background information essential for this survey.
2.1 Time series forecasting
Given a historical time series X t L:t =[x t L , ,x t 1 ] RD × L, where D is the number
− − ··· − ∈
of dimensions and L is the length of the historical time series. The future time series to
be predicted is X t:t+O =[x t , ,x t+O 1 ] RD × O, with O being the forecast horizon.
A time series forecasting model · · c · an predi − ct th ∈ e future sequence X t:t+O from the historical
sequence X t L:t. Assuming that the predicted sequence is denoted as X˜ t:t+O RD × O
− ∈
and the prediction model is denoted as ϕ(), the task of the time series forecasting can be
·
expressed as:
X˜ =ϕ(X ).
t:t+O t L:t
−
Note that xxx
t
RD denotes the time step at time t, and the time step correlation refers
∈
to the interrelations among these vectors. The time series can also be represented as
XXX =[vvv
(cid:31)1
;
···
;vvv
(cid:31)D
], where vvv
(cid:31)i
∈
RL denotes the i-th time-series variable. The correlation
of the time-series variable is the vectors among different vvv vectors.
2.2 Time series decomposition
Time-step dependencies usually consist of various correlations, such as trend and season
correlations. To more thoroughly explore these dependencies and simplify the forecasting
process, some forecasting models incorporate the concept of time series decomposition, an
approach rooted in traditional time series analysis (West 1997; Soltani 2002; Dagum 2010).
This analysis posits that any given time series X is composed of distinct components: a trend
1 3

Deep learning-based time series forecasting Page 7 of 67 23
term (T), indicative of the series’ long-term progression; a seasonal term (S), representing
systematic and predictable fluctuations tied to seasonal effects; a recurrent fluctuation term
(C), denoting periodic variations within a specific period of time; and an irregular fluctua-
tion term (N), which accounts for random variability in the data. Decomposition models
fall into two primary categories: additive and multiplicative. The additive model represents
the time series as the sum of the four components, i.e., X =T +S+C+N. While, for
the multiplicative model, an arbitrary time series can be expressed as X =T S C N.
∗ ∗ ∗
3 The logic of time series information mining
In this section, we will review the development of models over the past decade, with the
processing logic of time series as the main storyline. Generally, the processing logic of mod-
els for time series can be categorized into two types: mining correlations among time steps
and mining correlations among variables.
3.1 Mining correlations among time steps
In this subsection, we introduce the models and methods used to extract correlations among
time steps. Specifically, these approaches can be categorized into two main types: holistic
mining and targeted information mining, such as extracting trend or seasonal patterns.
3.1.1 Holistic mining
Autoencoders (Lv et al. 2014) are effective in uncovering time-step dependencies in time
series. They typically consist of three components: an encoder, a decoder, and a predic-
tion module, with the workflow divided into pretraining and prediction phases. During the
pretraining phase, the encoder extracts features that are fed into the decoder, which then
reconstructs the input sequence to train the model parameters. In the prediction phase, the
extracted features are input into the predictor, generating the forecasted sequence. In con-
trast, DLinear (Yun et al. 2019) uses a single linear layer to map the input vector’s dimen-
sion directly to the desired output dimension. Due to the simplicity of autoencoders and
linear layers, they are generally considered inadequate for fully capturing time-step depen-
dencies in time series.
Given the success of CNNs in the image processing domain (He et al. 2016; Krizhevsky
et al. 2017; Szegedy et al. 2015), they are also frequently utilized to identify temporal fea-
tures in time series (Markova 2022; Lu et al. 2020; Zhao et al. 2017). Through convolution
and pooling operations, CNNs aggregate temporal information within their receptive field to
uncover internal time-step dependencies. However, due to the inherently limited receptive
field, CNNs primarily extract short-term and discontinuous dependencies. To broaden the
receptive field of CNNs and uncover dependencies across a wider range, Temporal Con-
volutional Networks (TCN) incorporate Dilated Causal Convolution (DCC) into the CNN
architecture. Dilated convolution extends the receptive field without altering the convolu-
tion kernel’s size (Yu and Koltun 2015; Yazdanbakhsh and Dick 2019), allowing CNNs
to capture more extensive time-step relationships. Furthermore, TCN enhances dilated
convolution with temporal causality, ensuring that each time step’s output is only influ-
1 3

23 Page 8 of 67 X. Song et al.
F ig. 2 Dilated casual convolution
Fig. 3 The structure of LSTM
enced by preceding inputs. The operational intricacies of DCC, TCN’s central component,
are depicted in Fig. 2, showcasing how dilated causal convolution effectively satisfies the
demands of temporal sequence analysis.
Meanwhile, in order to capture time-step dependencies, researchers have proposed
Recurrent Neural Networks (RNNs) for time series forecasting, drawing upon the distinc-
tive characteristics of time-series data (Shelatkar et al. 2020; Amalou et al. 2022; Tang et
al. 2021). RNNs, utilizing their recurrent connections, enable the features of a preceding
time step to act as inputs for the current step, thereby encapsulating the temporal attri-
butes of each step with information from its antecedents. Unconstrained by the receptive
field, RNNs theoretically can capture more extensive time-step correlations. However, the
increased span of these recurrent connections may lead to problems like gradient explo-
sion and vanishing. To counter these issues, Long Short-Term Memory (LSTM) (Shi et al.
2015; Fischer and Krauss 2018) units introduce a gate mechanism and cell states within
the RNN framework. Cell states hold crucial information for long durations, while the gate
mechanism-comprising input, output, and forget gates-regulates the flow of information.
The input gate controls the incorporation of current input into the cell state, the forget gate
determines the retention of cell memory, and the output gate dictates the utilization of cell
information for current output, as depicted in Fig. 3. Thus, for a given input time step xxx t,
LSTM’s output can be formulated as follows:
1 3

| Deep learning-based time series forecasting |     |     |     |     |     |     | Page 9 of 67  | 23  |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- |
iii =σ(WWW xxx +WWW hhh +bbb ), fff =σ(WWW xxx +WWW hhh +bbb ),  (1)
|   t | xi t | hi  | t 1 | i t | xf  | t   | hf t 1 f |     |
| --- | ---- | --- | --- | --- | --- | --- | -------- | --- |
|     |      |     | −   |     |     |     | −        |     |
ccc =tanh(WWW xxx +WWW hhh +bbb ), ooo =σ(WWW xxx +WWW hhh +bbb ),  (2)
|   t      | xc       | t hc       | t 1  | c            | t        | xo t     | ho t 1 o |     |
| -------- | -------- | ---------- | ---- | ------------ | -------- | -------- | -------- | --- |
|          |          |            | −    |              |          |          | −        |     |
| (cid:31) | ccc =fff | ccc        | +iii | ccc ,        | hhh =ooo | tanh(ccc | ),       | (3) |
|          | t        | t (cid:31) | t 1  | t (cid:31) t | t t      | (cid:31) | t        |     |
−
where iii , fff ttt, ooo t respectively denote th(cid:31)e input gate, the forget gate, and the output gate.
ttt
 is the cell state candidates, ccc t is the cell state at the t-th time step, and hhh
| ccc t |     |     |     |     |     |     | t  is the time-step  |     |
| ----- | --- | --- | --- | --- | --- | --- | -------------------- | --- |
feature extracted at the t-th time step. WWW , WWW , and bbb  denote the weight matrices and
|     |     |     |     | xi  | hi  | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
b(cid:31)ias vectors for the input gates. Similarly, WWW xf, WWW hf, and bbb f correspond to the weight
matrices and bias vectors for the forget gates. For computing the cell states, WWW xc , WWW hc ,
and bbb  are used. Lastly, WWW , WWW , and bbb  represent the weight matrices and bias vectors
| c   |     | xo  | ho  | o   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
for the output gates.
The gated structure allows models to selectively retain information from past time steps
along with current features (Weerakody et al. 2021; Lin et al. 2022). This helps mitigate
issues like gradient explosion and vanishing gradients and also reduces the impact of noise
in historical data. This capability allows LSTM units to extract long-term temporal informa-
tion more efficiently than traditional RNN models. Gated Recurrent Unit (GRU) simplifies
LSTM’s gate mechanism, which can be regarded as a simplified version of LSTM and
will not be introduced in detail here. For multi-step time series forecasting, RNN-based
models typically rely on autoregression for sequential prediction (Maggiolo and Spanakis
2019; Binkowski et al. 2018), using outputs from one step as inputs for the next. However,
this autoregressive approach may lead to error accumulation. Furthermore, as the sequence
length processed by the model increases, RNNs face amplified risks of gradient explosion
and error accumulation, challenges that gate mechanisms do not fully resolve.
Given its exceptional performance in both natural language and image processing
domains (Devlin et al. 2018; Vaswani et al. 2017), the Transformer model is frequently
employed to analyze general time-series data (Wen et al. 2022; Cai et al. 2020). As depicted
in Fig. 4, the Transformer mitigates error accumulation in long-term forecasting by uti-
lizing an encoder-decoder architecture. It encodes the temporal information of historical
time series via the encoder and then decodes this information with the decoder to produce
predictions. At the heart of the Transformer is the self-attention mechanism, which initially
maps the input time series XXX into query QQQ, key KKK, and value VVV matrices. Subsequently,
it computes a similarity matrix between QQQ and KKK and adjusts VVV accordingly. Therefore,
the Attention mechanism’s output, OOO =Atten(XXX,XXX,XXX), is determined by the following
process:
|     | QQQ=WWW |           | XXX, KKK | =WWW XXX, | VVV =WWW | XXX,      |     |     |
| --- | ------- | --------- | -------- | --------- | -------- | --------- | --- | --- |
|     |         | (cid:31)Q |          | (cid:31)K |          | (cid:31)V |     | (4) |
AAA
|     |     | AAA=QQQ | (cid:31) KKK, | OOO=VVVSoftmax( |     | ),  |     | (5) |
| --- | --- | ------- | ------------- | --------------- | --- | --- | --- | --- |
√D
|     |     |     |     |     |     | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
RDk× L. The AAA RL L represents the similarity between the L time
| where QQQ,KKK,VVV |     |     |     | ×   |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                   | ∈   |     |     | ∈   |     |     |     |     |
steps of the input time series, and Softmax() transforms the similarity into an attention
·
weight distribution. The value matrix VVV is then weighted and summed based on the atten-
1 3

23  Page 10 of 67 X. Song et al.
F ig. 4 The structure of Transformer

Table 1 Deep learning time  Time series  Implications of  Key methods
| series prediction models using  | information | the information |     |
| ------------------------------- | ----------- | --------------- | --- |
time series decomposition
|     | Trend       | Information      | Autoformer (Wu et al. 2021),  |
| --- | ----------- | ---------------- | ----------------------------- |
|     | Information | on apparent      | Fedformer (Zhou et al. 2022), |
|     |             | persistence and  | LSTnet (Lai et al. 2018), TD- |
|     |             | regularity of    | former (Zhang et al. 2022),   |
|     |             | change between   | DLinear (Yun et al. 2019), N- |
|     |             | time steps       | BEATS (Oreshkin et al. 2019), |
ETSformer (Woo et al. 2022),
PatchTST (Nie et al. 2022)
|     | Seasonal    | Periodic informa- | LSTnet (Lai et al. 2018), Au-  |
| --- | ----------- | ----------------- | ------------------------------ |
|     | information | tion with fixed   | toformer (Wu et al. 2021),     |
|     |             | time intervals    | Fedformer (Zhou et al. 2022),  |
|     |             | between time      | ETSformer (Woo et al. 2022),   |
|     |             | steps             | TDformer (Zhang et al. 2022),  |
N-BEATS (Oreshkin et al.
2019)
|     | Multi time scale  | Time-series         | Scaleformer (Shabani et al.    |
| --- | ----------------- | ------------------- | ------------------------------ |
|     | information       | information at dif- | 2022), Pyraformer (Liu et al.  |
|     |                   | ferent time scales  | 2021)                          |
|     | Non-stationary    | Information on      | RevIN (Kim et al. 2021), NS-   |
|     | information       | the statistical     | Transformer (Liu et al. 2022)  |
properties of the
time series over
time
1 3

Deep learning-based time series forecasting Page 11 of 67 23
F ig. 5 The slice of the patch, where p is
the length of the sliding window, and s
is the step size of the window
tion weight distribution to obtain the time-series feature OOO. In this way, OOO incorporates the
similarity correlations between time steps.
In Fig. 4, the encoder layer of the Transformer encodes the temporal dependencies within
the input time series, subsequently feeding the encoded data to the corresponding decoder
layer. This decoder layer then generates the forecasted sequence, leveraging the identified
temporal dependencies. Besides, the feed-forward module within both the encoder and
decoder consists of several fully connected layers. With multiple layers of encoders and
decoders stacked, the Transformer architecture can capture extensive long-term temporal
correlations. The core of Transformer in time series forecasting lies in storing the similar-
ity relationships between historical time steps and predicting future time steps based on
these relationships. It is worth noting that existing large language models(LLM) (Zhao et al.
2023) like ChatGPT (Achiam et al. 2023) can be directly used for time series forecasting.
Currently, large language models are commonly involved in time series forecasting in two
ways: (1) as a predictive model (Liang et al. 2024): directly achieving sequential prediction
based on prompt engineering (Mao et al. 2023; Shin et al. 2020), and (2) not as a predictive
model (Zhang et al. 2024): generating embeddings by taking in relevant text information
and using these embeddings as auxiliary variables input into the predictive model.
3.1.2 Targeted information mining
To further explore the correlations among time steps, some models leverage the concept of
time series decomposition by developing custom modules designed to extract targeted infor-
mation, such as trend or seasonal information. The final predictive output is then obtained
by integrating the forecasting results of various types of target information. Current deep
learning models that employ time series decomposition are listed in Table 1.
Trend Information Trend information represents the trend correlations exhibited by the
series across time steps, where the term “trend correlations” denotes the discernible persis-
tence and regularity of fluctuations between consecutive time steps within a defined scope
(Taylor and Letham 2018; Cleveland et al. 1990; Asadi and Regan 2020). In addressing the
attributes of trend information, Autoformer (Wu et al. 2021) employs a mean filter to extract
the trend features from the time series. This involves convolving the input time series with
a mean filter using a sliding window approach. However, due to the limited receptive field
of the mean filter, the trend information acquired through the sliding window method tends
to be discontinuous and localized. To mitigate this limitation, Fedformer (Zhou et al. 2022)
1 3

23 Page 12 of 67 X. Song et al.
devises a set of mean filters with varying receptive fields, yielding trend terms correspond-
ing to different forecasting horizons. Subsequently, the model assigns learnable weights to
aggregate the trend terms through weighted averaging. This approach enables Fedformer to
incorporate trend information spanning diverse forecasting horizons.
Since trend information is usually more stable on a local scale, the time step to be pre-
dicted is more correlated with trend information from closer historical time steps, while
data from distant steps are deemed less favorable for trend prediction (Li et al. 2019; Lai et
al. 2018). To mitigate the influence of distant data on trend predictions, LSTnet (Lai et al.
2018) incorporates a predefined window, confining trend predictions to temporal informa-
tion within the window nearest to the target prediction. Within this preset window, which
includes k time steps, LSTnet employs linear mapping to capture the linear relationships
within the sequence, subsequently leveraging autoregression to forecast the trend term.
Thus, LSTnet’s prediction of the trend term at time t is expressed as:
k 1
−
yyy t = WWW i xxx t k+i +bbb, (6)
−
i=0
(cid:31)
where yyy
t
RD denotes the prediction of the trend term at time t, xxx
t k+i
RD denotes
historical v ∈ alue of the time series at the (t − k+i)th time step, WWW i ∈ R −D × D ∈ is the weight
matrix and bbb RD is the bias. LSTnet employs autoregression to generate trend term pre-
∈
dictions for all target locations. Similarly, both TDformer (Zhang et al. 2022) and DLinear
(Yun et al. 2019) adopt linear mapping techniques for trend term prediction.However, linear
relationships inadequately characterize the trend information of time steps, leading to weak
interpretability of trend terms obtained through linear mapping. To address these issues,
N-BEATS (Oreshkin et al. 2019) introduces the Trend Stack module, aimed at capturing the
trend information within time series data. This module primarily employs polynomial fitting
techniques to model the trend relationships between time steps. For the input sequence X,
the Trend Stack module initially employs a fully connected layer to extract time-series fea-
tures, obtaining parameters for polynomial fitting. Subsequently, it introduces the time vec-
tor ttt= [0,1,2, ··· ,(O − 1)] RO as the independent variable for the fitting process. The resulting
O ∈
trend term generated by the Trend Stack can be represented as:
h
θθθ =XXXWWW +BBB, XXX T = θθθ i ttti, (7)
i=0
(cid:31)
where θθθ RD
×
h is the fit factor for polynomial fitting, WWW RL
×
h is the weight matrix,
and BBB
∈
∈ RD
×
h is the bias. XXX
T ∈
RD
×
O is the trend term gen ∈ erated by the Trend Stack. h is
the highest power in the polynomial fit, which is usually set to a small value (0<h<5) by
N-BEATS to prevent overfitting.While LSTnet mitigates the influence of distant informa-
tion on trend term prediction by implementing a preset window, it maintains uniform atten-
tion across time steps within this window. In contrast, ETSformer (Woo et al. 2022) posits
that data proximate to the prediction position holds greater significance in encoding trend
terms, prioritizing time steps in close proximity to the prediction location.
1 3

Deep learning-based time series forecasting Page 13 of 67  23
Exponentially weighted average enables the prediction of trend terms to pay more atten-
tion to those closer historical time steps (Hyndman et al. 2008; Ensafi et al. 2022), strength-
ening correlations among short-term time steps. ETSformer introduces the Exponential
Smoothing Attention (ESA) module, integrating the concept of exponential weighted aver-
aging into the attention mechanism. For the output OOO of the attention mechanism derived
from Equation (5), the operation of ESA can be expressed as:
t 1
|     | OOOˆ  | α)OOOˆ | −            |            |             |     |
| --- | ----- | ------ | ------------ | ---------- | ----------- | --- |
|     | =αOOO | +(1    | =            | α(1 α)jOOO | +(1 α)tv ,  | (8) |
|     | t t   | −      | t 1          | −          | t j − 0     |     |
|     |       |        | −            |            | −           |     |
|     |       |        | (cid:31) j=0 |            |             |     |
where 0<α<1 is the learnable smoothing parameter and v 0 denotes the learnable initial
state.The aforementioned models primarily capture the short-term trends within the time
series, inadvertently overlooking the influence of long-term trend information. To address
this limitation, PatchTST (Nie et al. 2022) draws inspiration from patch processing meth-
odologies prevalent in computer vision (Dosovitskiy et al. 2020; Liu et al. 2021), integrat-
ing the concept of patches into the attention mechanism. As depicted in Fig. 5, PatchTST
initially segments the input time series into fixed-length patches using a sliding window
approach. Subsequently, these patches serve as inputs to the attention mechanism. Unlike
traditional attention mechanisms, PatchTST does not focus on correlations among time steps
within the individual patch; instead, it treats each patch as a unit and employs the atten-
tion mechanism to assess the similarity between patches. These patches contain aggregated
information from short-term time steps, facilitating the exploration of long-term dependen-
cies within the time series. For the input sequence XXX, this process can be represented as:
XXX =Patch(XXX),QQQ =XXX WWW +bbb ,KKK =XXX WWW +bbb ,VVV =XXX WWW +bbb ,
|   p |     | p p Q | Q p | p K | K p p V | V (9) |
| --- | --- | ----- | --- | --- | ------- | ----- |
AAA
p
|     | AAA | p =QQQ p KKK (cid:31)p | , OOO p =VVV | p Softmax( | ),  | (10) |
| --- | --- | ---------------------- | ------------ | ---------- | --- | ---- |
√D
|     |     |     |     |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- |
RD n p is the set of sliced patches, n denotes the number of sliced patches,
| where XXX | p × × |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
∈
and p denotes the length of each individual patch. WWW ,WWW ,WWW RD p h is the weight
|     |     |     |     | Q   | K V × × |     |
| --- | --- | --- | --- | --- | ------- | --- |
matrix, and h is the dimension of hidden layer. AAA RD n n is the attention matrix, which  ∈
|     |     |     |     | p × | ×   |     |
| --- | --- | --- | --- | --- | --- | --- |
∈
represents the similarity relationship between n patches.Seasonal Information: Seasonal
information is very important in time series analysis (Edition et al. 2002; Rawat et al. 2019),
as it indicates the periodic behavior within the data, elucidating correlations between time
steps separated by fixed intervals. However, extracting seasonal information is often more
challenging than trend information due to the intricate periodicity inherent in time series
data. Approaches for predicting seasonal terms can be broadly categorized into two groups:
time domain-based methods and frequency domain-based methods. Time domain-based
methods directly model the complex periodicity within the time domain (Lai et al. 2018;
Wu et al. 2021). In contrast, frequency domain-based methods first transform the input time
series into the frequency domain using a Fourier transform (Zhou et al. 2022; Woo et al.
2022; Zhang et al. 2022), then identify complex periodicities based on frequency compo-
nents. In the following, we will delve into the seasonal terms mining approaches in both the
time and frequency domains.
1 3

23 Page 14 of 67 X. Song et al.
To enable RNNs to capture seasonal information within time series data, LSTnet (Lai
et al. 2018) introduces a recurrent-skip network that contains skip connections. Incorporat-
ing skip connections facilitates direct interaction between time steps separated by a pre-
defined interval. As depicted in Fig. 6, LSTnet initially assumes a potential period p for the
input sequence. Subsequently, connections are established between the tth time step and the
(t p)th time step within the RNN. The update of the hidden layer state at the tth time step
−
encompasses information from the (t p)th time step, the current input, and the hidden
−
layer state from the previous time step. The skip-connected RNN allows the state update at
each time step to fully consider the information of the time steps before a fixed time interval.
The skip-connected RNN necessitates preset timing periods p and can only be utilized
to extract a single periodic relation, rendering LSTnet inadequate for analyzing time series
exhibiting intricate periodic patterns. To address this limitation and capture the complex
periodic relations inherent in time series data, Autoformer (Wu et al. 2021) introduces the
Auto-Correction module. This module aims to assess the time-delay similarity among input
sequences to characterize the periodicity of the original sequences, where time-delay simi-
larity denotes the likeness between time-delayed sequences and the original ones. Time-
delayed sequences are shifted by τ time steps. Autoformer posits that if a time-delayed
sequence with a τ-step delay exhibits significant similarity to the original sequence, τ can
be considered a period of the original sequence. To capture these complex period relations,
as depicted in Fig. 7, the Auto-Correction module initially employs Roll(,τ) to shift the
·
input sequence by a length of τ, subsequently evaluating the similarity between the delayed
sequence and the original one. This similarity is then utilized as a weighting factor to aver-
age and aggregate the time-delayed sequence, thereby generating the seasonal terms of the
sequence. Thus, for the input time series X, the Auto-Correction process can be delineated
as:
L
1
R XXX (τ)= L l → im ∞ L (cid:31) t=1 xxx t xxx t − τ , τ 1 , ··· ,τ k =argT τ o ∈ p { K 1, ·· ( · R ,L } XXX (τ)), (11)
Rˆ
XXX
(τ
1
),
···
,Rˆ
XXX
(τ
k
)=Softmax(R
XXX
(τ
1
),
···
,R
XXX
(τ
k
)), (12)
F ig. 6 Recurrent-skip network
1 3

Deep learning-based time series forecasting Page 15 of 67 23
Fig. 7 Auto-Correction in Autoformer
Fig. 8 FEA in Fedformer
k
Auto-Correlation(XXX)= Roll(XXX,τ i )Rˆ XXX (τ i ), (13)
i=1
(cid:31)
where xxx t denotes the tth time step of the input time series, R XXX (τ) denotes the similarity
between the original sequence X and its delayed sequence by a time delay of τ time steps.
τ 1 , ,τ k represent k time delays of the delayed sequence that has the highest similarity to
···
the original sequence. Autoformer leverages the similarity of time delays to extract the peri-
odicity inherent in the input time series. It approximates the complexity of the time series’
periods by utilizing multiple time delays of different degrees.
According to the Fourier series (Mathieu et al. 2013; Celeghini et al. 2021), any periodic
signal can be expressed as a linear combination of sinusoids with different frequencies.
Consequently, frequency domain-based processing involves transforming the time series
into the frequency domain via Fourier transform and subsequently analyzing the series in
this domain. Frequency domain-based seasonal term mining algorithms are able to analyze
the frequency components directly, thereby extracting complex period information from
the time series. Subsequently, we will delve into the seasonal term mining algorithm in the
frequency domain.
Fedformer (Zhou et al. 2022) adopts an approach by directly assessing the similarity
between frequency components within the frequency domain space. Fedformer introduces
the FEA (Frequency Enhanced Attention) module, which employs an attention mechanism
1 3

23 Page 16 of 67 X. Song et al.
to scrutinize frequency components in the frequency domain, thereby delving into the peri-
odic characteristics of the input time series.
In Fig. 8, the FEA module first transforms the input time series from the time domain to
the frequency domain using the Fourier transform F(). To mitigate computational costs
·
in the subsequent Attention mechanism and counteract the effects of noise, FEA employs
Select() to randomly sample frequency components in the frequency domain. Subsequently,
·
FEA applies the Attention mechanism to these selected frequency components, deriving
similarity relations among them and processing the components accordingly. Finally, FEA
returns the processed results to the time domain using the inverse Fourier transform F − 1()
·
. Consequently, the FEA processing, based on the provided description and Equation (5),
can be expressed as:
QQQ˜ =Select(F(QQQ)), KKK˜ =Select(F(KKK)), VVV˜ =Select(F(VVV)), (14)
OOO˜ =Atten(QQQ˜,KKK˜,VVV˜), YYY S =F − 1(Padding(OOO˜)), (15)
where OOO˜ CI
×
Dk, I denotes the number of frequency components in the frequency domain.
∈
To fulfill the forecasting task, FEA requires padding the processing results in the frequency
domain using Padding() to ensure that the sequence meets length requirements.Since FEA
·
performs a random selection of frequency components in the frequency domain, there’s a
risk of losing crucial season information. To address this, ETSformer (Woo et al. 2022) fil-
ters frequency components based on their magnitudes, retaining the k components with the
highest magnitude. For seasonal term processing, ETSformer introduces the FA (Frequency
Attention) module. This module first transforms the input time series into the frequency
domain, preserving the k frequency components with the greatest magnitude. Subsequently,
the FA module returns the retained frequency components to the time domain via Fourier
inverse transform and outputs the predicted seasonal terms.
In contrast to Fedformer’s FEA module, ETSformer operates under the premise that noise
in time series data typically resides in frequency components with lower energy. Hence, it
prioritizes frequency components with higher magnitudes. Conversely, Fedformer assumes
noise may be present across all frequency components and thus employs random selection
for screening. TDformer’s (Zhang et al. 2022) approach to seasonal term processing is the
same as that of Fedformer. Meanwhile, DLinear (Yun et al. 2019) utilizes a single linear
layer to handle the seasonal terms.
To streamline the module for extracting seasonal terms, N-BEATS (Oreshkin et al. 2019)
simplifies its approach by exclusively processing specific frequencies within the frequency
domain. Specifically, N-BEATS introduces a Season Stack, which utilizes Fourier period
coding to analyze the seasonality of the time series. As depicted in Fig. 9, N-BEATS feeds
the input time series into the Season Stack. The stack utilizes a fully connected network
(FC) to derive Fourier period coding, representing the amplitudes of specific frequen-
cies. Subsequently, leveraging the Fourier period coding alongside the input time vector
ttt= [0,1,2, ··· ,(O − 1)] RO, the Season Stack employs Fourier series to predict the seasonal
O ∈
terms. Thus, the processing of seasonal terms can be expressed as:
θθθ =XXXWWW +BBB, (16)
1 3

Deep learning-based time series forecasting Page 17 of 67 23
Fig. 9 Season Stack in N-BEATS
h+1
(cid:31)2 (cid:30)
YYY = θθθcos(2πittt)+θθθ sin(2πittt), (17)
S i i+ h
i=0
(cid:31)2(cid:30)
(cid:31)
where WWW RL
×
h denotes the weight matrix, θθθ RD
×
h denotes the Fourier coefficients
∈ ∈
predicted by an FC network, and h denotes the number of frequency components processed
by the season module in the frequency domain. YYY
S
RD
×
O denotes the seasonal terms
∈
predicted by the season module. From the equation provided, it’s evident that, unlike Fed-
former, N-BEATS chooses to process specific frequency components, aiming to simplify
the module’s task of extracting seasonal information.
Multi Scale Information: In addition to trend and seasonal information, models have begun
to target other time-series features such as multi-scale and non-stationary information.
Multi-scale information pertains to the temporal dependencies of a time series at different
scales (Shabani et al. 2022; Challu et al. 2023). For instance, considering hourly observa-
tions as the finest scale, coarser scales could represent daily, weekly, or even monthly pat-
terns within the time series. Integrating multi-scale temporal information enables models
to capture dependencies across various durations, crucial for accurate time series modeling
and forecasting.
To facilitate the capture of information across diverse time scales, Scaleformer (Shabani
et al. 2022) introduces a multi-scale iterative framework for time series forecasting. This
framework employs existing models (e.g., Autoformer, Fedformer) as the primary forecast-
ing model and applies filtering operations to transform the input time series into different
time scales. As illustrated in Fig. 10, Scaleformer comprises multiple processing layers,
with each layer’s inputs derived from downsampling the original inputs and upsampling
the outputs of the preceding layer. At the ith processing layer, Scaleformer first upsamples
the output of the preceding layer XXX out,i 1 to obtain UUU i . Simultaneously, it downsamples
the original input XXX using a scale factor − s i to obtain PPP i . These UUU i and PPP i are then nor-
malized across scales and fed into the forecasting model. The primary forecasting model
produces the processing result XXX out,i for the current layer, and the output of the final pro-
cessing layer yields the ultimate prediction YYY.
Since Scaleformer needs to get the prediction in different time scale iterations, the distri-
bution of the model’s intermediate variables can change dramatically, which may lead to the
accumulation and propagation of erroneous distributional information. In order to eliminate
the effect of time scale changes, Scaleformer will perform cross-scale normalization opera-
tions on inputs UUU
i
and PPP
i
at each processing layer. For UUU
i
RD
×
Ln and PPP
i
RD
×
Lm, the
∈ ∈
cross-scale normalization operation can be expressed as:
1 3

23 Page 18 of 67 X. Song et al.
Fig. 10 The structure of Scaleformer
m n
1
µµµ i = ( PPP i,t + UUU i,t ), PPPˆ i =PPP i µµµ i , UUUˆ i =UUU i µµµ i , (18)
n+m − −
t=1 t=1
(cid:31) (cid:31)
where µµµ i is the cross-scale mean coefficient of the ith layer, which is the mean of UUU i
and PPP . The cross-scale normalization operation is essentially a "zero-mean" operation on
i
UUU and PPP . Scaleformer enhances the primary prediction model’s ability to learn multi-
i i
scale time-series information by feeding time series of different time scales into the primary
prediction model.To enable the attention mechanism to focus on multi-scale time-series
information, Pyraformer (Liu et al. 2021) constructs a pyramid diagram comprising lay-
ers representing different time scales. Initially, Pyraformer processes the input time series
through convolution, aggregating time steps within a receptive field to generate coarser
time scales. As illustrated in Fig. 11, Pyraformer utilizes the original input time series as
the bottom layer of the pyramid diagram to represent the finest time scales. Subsequently,
it iteratively aggregates the bottom time steps via convolution, using the resultant coarse-
scale time series as the top layer of the pyramid graph. Pyraformer employs the Pyramidal
Attention Module (PAM) for nodes within the pyramid graph, enabling extraction of cross-
time scale features. Finally, depending on specific prediction task requirements, Pyraformer
feeds the features of the top nodes into different networks to obtain the final output. Hereaf-
ter, we delve into the principles of PAM.
In PAM, each node is only concerned with its adjacent nodes. Considering the pyramid
structure depicted in Fig. 11, let n(s) RD denote the lth node in the sth layer of the pyra-
mid graph. The node n(s) can obtai l n t ∈ he set N (s) of its neighboring nodes in adjacent layers.
l l
This set encompasses three components: (1) neighboring A nodes within the same layer,
including the n(s) node itself, denoted as A (s); (2) the lower layer nodes, representing finer
l l
time scale nodes, denoted as C (s); and (3) the upper layer nodes, representing the coarser
l
time scale node, denoted as P (s). This set is expressed as follows:
l
1 3

Deep learning-based time series forecasting Page 19 of 67  23

Fig. 11 Pyramid structure in Pyraformer. Different layers have different node sizes, and the node size
indicates the granularity of the time scale

Fig. 12 Triformer. Node size indicates the granularity of the time scale
|     |     |        | N (s) | =A (s) C (s) | P (s),    | (19) |
| --- | --- | ------ | ----- | ------------ | --------- | ---- |
|     |     |        | l     | l l          | l         |      |
|     |     |        |       | ∪            | ∪         |      |
|     |     |        |       | A            | 1 L       |      |
|     | (s) | = n(s) | : j   | l            | ,1 j ,    |      |
|     | A   |        | j     | −            |           | (20) |
|     | l   | {      | |     | − |≤ 2       | ≤ ≤ Cs 1} |      |
−
|     |     | ( s) | n( s | 1)      |            |      |
| --- | --- | ---- | ---- | ------- | ---------- | ---- |
|     |     | C    | =    | − : l 1 | C <j lC ,  | (21) |
|     |     | l    | { j  | | − |   | ≤ }        |      |
l
|     |     |     | (s) | n(s+1) |                   |      |
| --- | --- | --- | --- | ------ | ----------------- | ---- |
|     |     |     | P = | :j     | = ,               | (22) |
|     |     |     | l   | { j    | C }               |      |
|     |     |     |     |        | (cid:31) (cid:30) |      |
1 3

23  Page 20 of 67 X. Song et al.

Fig. 13 Left: The VSN structure in the TFT; Right: the GRN module in VSN
F ig. 14 AliAttention in Aliformer
Table 2 The space complexity of different Attention modules, where L denotes the input sequence length
Models for optimizing complexity Space complexity of attention mechanism
| Transformer (Vaswani et al. 2017) | O(L2)       |     |
| --------------------------------- | ----------- | --- |
| LogTrans (Li et al. 2019)         | O(L(logL)2) |     |
| Reformer (Kitaev et al. 2020)     | O(LlogL)    |     |
Informer (Zhou et al. 2021)
O(LlnL)
| PatchTST (Nie et al. 2022) | O(n2),n= | L p |
| -------------------------- | -------- | --- |
−s +2a
(cid:31) (cid:29)
| Pyraformer (Liu et al. 2021) | O(S √1L)b |     |
| ---------------------------- | --------- | --- |
−
| Crossformer (Zhang and Yan 2022) | O(L) |     |
| -------------------------------- | ---- | --- |
ap denotes the length of the patch and s denotes the stride
bS is the number of time scales
1 3

Deep learning-based time series forecasting Page 21 of 67  23

Fig. 15 LogSparse Self-Attention. The connecting line indicates the need to compute the similarity
relationship

Fig. 16 LSH Attention. Different colors indicate different groups
Table 3 Commonly used time series datasets in time series prediction
| Datasets      | Timesteps | Variates | Granularity |
| ------------- | --------- | -------- | ----------- |
| ETTm1 &ETTm2a | 69680     | 7        | 5 min       |
ETTh1 &ETTh2a
|             | 17420 | 7   | 1 h   |
| ----------- | ----- | --- | ----- |
| Elctricityb | 26304 | 321 | 1 h   |
| Exchangec   | 7588  | 8   | 1 day |
| Trafficd    | 17544 | 862 | 1 h   |
ILI e
|     | 966 | 7   | 1 week |
| --- | --- | --- | ------ |
ahttps://github.com/zhouhaoyi/ETDataset
bhttps://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
chttps://github.com/laiguokun/multivariate-time-series-data
dhttp://pems.dot.ca.gov
ehttps://gis.cdc.gov/grasp/fluview/fluportaldashboard.html
1 3

23 Page 22 of 67 X. Song et al.
where L is the sequence length of the original input to the model, while A denotes a
hyperparameter indicating the number of nodes selected at the same time scale. C serves as
another hyperparameter designed to regulate the number of ensemble nodes. To ensure the
model focuses on multi-scale time-series information, PAM lets nodes n(s) compute atten-
l
tion correlations within the set N (s):
l
exp qkT/√d v
y = i K i ,
exp qkT/√d (23)
i(cid:31) ∈ N ( (cid:30) s) i ∈ N ( l s(cid:30)) i (cid:29) K
(cid:28) (cid:30) (cid:29)
where q is the query vector generated by node n( l s), and k i , v i are key-value pairs gener-
ated by nodes in the set N (s). Pyraformer aggregates time steps of fine time scales into coarse
l
time scales through convolutional operations and captures similarity correlations across dif-
ferent time scales using the Attention mechanism.Unlike Pyraformer, Triformer (Cirstea
et al. 2022) generates coarse time-scale time steps through the Attention mechanism and
takes fine time-scale sequences as inputs when processing coarse time-scale sequences. As
shown in Fig. 12, the Triformer consists of multiple processing layers stacked on top of each
other, each of which corresponds to a different time scale. The results from the fine time-
scale processing in the lower layers are fed as inputs to the coarser time-scale processing
layers. The outputs from all layers are integrated into Triformer’s prediction process. This
mechanism enables Triformer to effectively explore multi-scale time series information.
Next, we will delve into the underlying principles of each processing layer in Triformer. Tri-
former initially divides the input sequence into multiple local short sequences and applies
the Attention mechanism within these segments. For a local short sequence XXX p RD × p in
∈
this layer, where p represents the length of the local short sequence. The output of the Atten-
tion mechanism in Triformer can be expressed as:
ooo p =Atten(hhh,XXX p ,XXX p ), (24)
where ooo
p
RD is the temporal feature vector at a short-term interval, corresponding to the
∈
coarser time scale. Meanwhile, hhh RD serves as the query vector, capturing the temporal
∈
information at the current scale. So hhh necessitates re-initialization for each processing layer
accommodating distinct time scales. It is worth noting that ooo p will be used as the time step
in the input sequence of the next processing layer.
Non-stationary Information: Non-stationary information refers to variations in the sta-
tistical characteristics of a time series over time (Ulyanov et al. 2016; Du et al. 2021; Muan-
det et al. 2013; Zhong and Cambria 2023). The presence of non-stationary time series poses
challenges for prediction tasks in deep learning models, as they complicate the modeling
of sequences of statistically changing data during inference, typically manifested through
shifts in mean and standard deviation. RevIN (Kim et al. 2021) addresses this issue by stan-
dardizing input sequences within the model, ensuring each processed sequence adheres to
a consistent distribution, and subsequently reverting the model’s predicted sequences to the
original distribution during the output stage. Hereafter, we delve into a detailed exposition
of RevIN.
RevIN is a flexible end-to-end method that can be applied to arbitrary models (Li et
al. 2023; Liu et al. 2024, 2022). To mitigate non-stationary effects in input time series, it
1 3

Deep learning-based time series forecasting Page 23 of 67  23
initially normalizes each sequence within a defined lookback window. Unlike conventional
normalization techniques applied during time series preprocessing, RevIN normalizes input
sequences within the lookback window utilizing learnable affine parameters. The normal-
ized sequences are then fed into the forecasting model to generate predictions. During the
output stage, RevIN reverses the normalization process to restore the non-stationary char-
acteristics of the time series. Formally, for an input time series XXX, RevIN’s processing can
be represented as:
|     |      | L        |       | L        |      |             |       |           |      |
| --- | ---- | -------- | ----- | -------- | ---- | ----------- | ----- | --------- | ---- |
|     |      | 1        |       | 1        |      |             | XXX   | mmm       |      |
|     | mmm= |          | XXX , | vvv =    | (XXX | mmm)2, XXXˆ | =γγγ( | − )+βββ,  |      |
|     |      |          | j     |          | j    |             |       |           | (25) |
|     |      | L        |       | L        | −    |             | √vvv  | +ε        |      |
|     |      | j=1      |       | j=1      |      |             |       |           |      |
|     |      | (cid:31) |       | (cid:31) |      |             |       |           |      |
RD denotes the mean and variance of the time series in the lookback win-
where mmm,vvv
∈
dow, and γγγ,βββ RD denotes the affine coefficients. Then XXXˆ  is fed into an arbitrary model
∈
to get the prediction YYY. To restore the non-stationary information of the time series, RevIN
denormalizes the prediction:
|     |     |     |     |               | YYY | βββ     |     |     |     |
| --- | --- | --- | --- | ------------- | --- | ------- | --- | --- | --- |
|     |     |     |     | YYYˆ =√vvv+ε( | −   | )+mmm.  |     |     |     |
(26)
|     |     |     |     |     | γγγ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Non-stationary information within time series poses a significant challenge to accurate fore-
casting, it is widely acknowledged that preprocessing methods such as those discussed in
(Kim et al. 2021; Liu et al. 2022; Passalis et al. 2019) can help mitigate the non-station-
ary nature of the original input series. However, removing the inherent non-stationarity
of sequences may lead to the problem of over-stationarization, which in turn can subject
forecasting models to severe overfitting. To tackle this issue, NS-Transformer (Liu et al.
2022) integrates non-stationary information into the Attention mechanism, compensating
for information lost during the normalization of the sequence.NS-Transformer adopts the
standard Transformer architecture but incorporates De-stationary Attention in place of con-
ventional Attention mechanisms. De-stationary Attention leverages statistical information,
specifically mean and variance derived from instance normalization, enhancing the model’s
ability to capture non-stationary patterns within the original time series. Since NS-Trans-
former assumes that the time series have the same variance in all variables, vvv is simplified
to the scalar v. Given the stationarized input sequence XXXˆ , linear mappings yield QQQˆ , KKKˆ ,
VVVˆ, alongside statistical parameters mmm and v from the original sequence. The computation
process of De-stationary Attention is as follows:
AAAˆ
|     |     | AAAˆ | =vQQQˆ (cid:31)KKKˆ |                | OOOˆ | =VVVˆ    |     |     |      |
| --- | --- | ---- | ------------------- | -------------- | ---- | -------- | --- | --- | ---- |
|     |     |      |                     | +1mmm (cid:31) | KKK, | Softmax( |     | ),  | (27) |
√D
|     |     |     |     |     |     |     |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where QQQ,KKK,VVV are the query matrix, key matrix, and value matrix obtained by linear map-
ping of the original input sequence. mmm denotes the mean vector statistically obtained in
the normalization, and v denotes the variance statistically obtained in the normalization.In
order to directly use deep learning implementation Equation(27), NS-Transformer uses a
multi-layer perceptron MLP() to learn non-stationary information from the original input
·
time series:
1 3

23 Page 24 of 67 X. Song et al.
logτ =MLP(v,XXX), ∆∆∆=MLP(mmm,XXX),, AAAˆ =τQQQˆ (cid:31)KKKˆ +1∆∆∆
(cid:31)
, (28)
where τ R denotes the variance information learned from the non-stationary information
∈
and ∆∆∆ RL denotes the mean information learned from the non-stationary information.
∈
For the prediction of the Transformer model, NS-Transformer similarly chooses to denor-
malize to restore the prediction’s non-stationary information.
3.2 Mining correlations among variables
In the context of multivariate time series forecasting, each time series dimension represents
a distinct univariate time series. In addition to considering time-step dependencies, correla-
tions among variables also play a crucial role in predicting multivariate time series (Cheng
et al. 2022; Jin et al. 2022; Cao et al. 2020; Zhang et al. 2023). For example, when predicting
future temperature for a given region, relying solely on historical temperature records from
the region is insufficient. Instead, including historical wind speed data from the region and
historical temperature data from neighboring regions can significantly enhance the accu-
racy of the prediction. Therefore, in addition to capturing time-step dependencies, an alter-
native approach to temporal processing is to capture the correlations among variables. In
section 3.1, the previously discussed forecasting models mainly concentrate on exploring
dependencies among time steps, often overlooking the exploration of correlations among
variables. Particularly, PatchTST (Nie et al. 2022), a model incorporating the Channel Inde-
pendence (CI) strategy, entirely disregards correlations among variables. In the following,
we will introduce models that explicitly extract correlations among variables.
To address variables at a more detailed level, TFT (Temporal Fusion Transformers) (Lim
et al. 2021) classifies the variables of the input time series into three categories:
1. Static variables: variables remain constant over time.
2. Time-dependent variables: variables exhibit temporal changes and require prediction.
3. Future-known variables: These variables include known future information (e.g.,
upcoming holiday dates), other exogenous time series (e.g., historical customer foot
traffic), and static metadata (e.g., store location).To handle these categorized multiple
variables, TFT incorporates a Variable Selection Network (VSN) module for filtering.
The structure of VSN is schematically represented in Fig. 13. For different types of
input variables, the VSN guides them individually through the Gated Residual Network
(GRN) module. Furthermore, the VSN plays a crucial role in regulating the representa-
tion for each variable by utilizing weighted averaging, serving as an effective mecha-
nism for variable filtering. Specifically, the formulations of GRN are given by:
eee=ELU(WWW x xxx+WWW c ccc+bbb e ), (29)
ddd=WWW d eee+bbb d , (30)
GRN(xxx,ccc)=LayerNorm(xxx+GLU(ddd)), (31)
where xxx RL and ccc RL are univariate time series respectively from the primary input
∈ ∈
and the external context, ELU() is the ELU activation function, LayerNorm() represents
· ·
1 3

Deep learning-based time series forecasting Page 25 of 67  23
layer normalization, and WWW ,WWW Rh L, WWW Rh h are learnable weight matrices.
|     | x   | c ∈ × | d ∈ × |     |     |
| --- | --- | ----- | ----- | --- | --- |
Additionally, bbb ,bbb Rh are learnable biases, and h denotes the dimension of the preset
e d
| hidden layer. GLU() refers to the gated linear unit. For the input ddd, the computation of  | ∈   |     |     |     |     |
| ------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
·
GLU() is as follows:
·
|     | GLU(ddd)=(dddWWW | +bbb | ) σ(dddWWW | +bbb ),  |      |
| --- | ---------------- | ---- | ---------- | -------- | ---- |
|     |                  | 1 1  |            | 2 2      | (32) |
⊗
Rh h are learnable weight matrices, and  Rh are learnable
| where  WWW | 1 ,WWW 2 × |     |     | bbb 1 ,bbb 2 |     |
| ---------- | ---------- | --- | --- | ------------ | --- |
|            | ∈          |     |     | ∈            |     |
biases. The symbol   represents the Hadamard product, and σ() denotes the sigmoid
|     | ⊗   |     |     | ·   |     |
| --- | --- | --- | --- | --- | --- |
activation function.In TFT, the VSN module assigns weights to different variables, which
helps suppress certain variables’ representation and remove noisy inputs. The VSN only
accepts an univariate sequence as input, thus its output weights cannot consider the correla-
tion between different variables. To address this issue, Aliformer (Qi et al. 2021) leverages
the Attention mechanism to capture the similarity relationships among variables, which is
called AliAttention. This innovative approach enables the fusion of attention graphs gener-
ated from different variables, allowing the Attention mechanism to consider the similarity
relations among diverse variables simultaneously.
|                                                     |     |     | RD1× | L and XXX RD2× L, AliAtten- |     |
| --------------------------------------------------- | --- | --- | ---- | --------------------------- | --- |
| As depicted in Fig. 14, for the input variables XXX |     |     | 1    | 2                           |     |
|                                                     |     |     | ∈    | ∈                           |     |
tion performs separate computations of attention graphs for each variable. These individual
attention graphs are then combined to create a unified attention graph. The resulting atten-
tion graph is subsequently used to generate the outputs of the Attention mechanism. This
process can be summarized as follows:
AAA
∗
AAA 1 =QQQ (cid:31)1 KKK 1 , AAA 2 =QQQ (cid:31)2 KKK 2 , AAA ∗ =AAA 1 +AAA 2 , OOO =Softmax( )VVV 1 ,  (33)
2D
  k
In the process, QQQ ,KKK ,VVV 1 are derived from variable XXX , while QQQ ,KKK 2 are derived from
|              | 1 1                                               |     |     | 1 2                        |     |
| ------------ | ------------------------------------------------- | --- | --- | -------------------------- | --- |
| variable XXX |                                                   |     |     | RL L, is a newly obtained  |     |
|              | 2 . The resulting attention graph, denoted as AAA |     |     | ∗ ×                        |     |
∈
graph that integrates the similarity matrices of different variables. By incorporating AliAt-
tention, the Attention mechanism can explore the interdependencies among the variables by
fusing the attention graphs.To facilitate a comprehensive exploration of correlations among
variables, Crossformer (Zhang and Yan 2022) introduces the concept of directly applying
the Attention mechanism to the variables instead of fusing attention graphs. For this pur-
pose, Crossformer proposes DAttention. For the input time series XXX RD L, Crossformer
×
first transposes the dimension of input series to obtain transposed XXX(cid:31) ∈ RL D, and then
×
∈
feeds XXX(cid:31) into the Attention mechanism. DAttention, based on Equation (4) and (5), can be
mathematically expressed as:
AAA
|     | AAA=QQQ (cid:31) KKK, | OOO=VVVSoftmax( |     | ),  | (34) |
| --- | --------------------- | --------------- | --- | --- | ---- |
√D
|     |     |     |     | k   |     |
| --- | --- | --- | --- | --- | --- |
where QQQ,KKK,VVV RDk× D are all computed based on the transposed input XXX(cid:31). Here, QQQ
∈
represents the query matrix, KKK represents the key matrix and VVV represents the value matrix.
Importantly, the attention graph AAA RD D in DAttention captures the similarity relation-
×
| ships between D variables.Indeed, the distinction between AliAttention and DAttention lies  |     | ∈   |     |     |     |
| ------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
in how they utilize the Attention mechanism. AliAttention focuses on capturing similar rela-
1 3

23 Page 26 of 67 X. Song et al.
tionships of variables by fusing attention graphs derived from each variable. On the other
hand, DAttention applies the Attention mechanism directly to the variables, allowing it to
uncover the cross-time-step dependence of variables.
4 Long-term time series forecasting optimization
In the field of long-term time series forecasting, Transformer model (Wu et al. 2021; Zhou
et al. 2021, 2022) is widely used. This is because Convolutional Neural Networks (CNNs)
have limitations regarding their receptive field, and Recurrent Neural Networks (RNNs)
suffer from issues like error accumulation and gradient explosion. However, the attention
mechanism’s computational cost grows quadratically with the series length. To address
these challenges, researchers have developed various methods to optimize the attention
mechanism for long-term time series prediction, as shown in Table 2.
The computational cost of the attention mechanism mainly arises from computing the
similarity relationships between time steps. To optimize the Attention mechanism, two main
approaches have been proposed:
(1) Shortening the length of the input sequence of the Attention mechanism: This approach
aims to reduce the computational complexity by processing shorter subsequences
instead of the entire input sequence. Various techniques, such as window-based (Zhou
et al. 2021; Cirstea et al. 2022), segment-based (Nie et al. 2022; Liu et al. 2021), and
hierarchical methods (Zhang and Yan 2022), have been proposed to divide the input
sequence into smaller parts before applying the attention mechanism.
(2) Sparsifying the attention mechanism: This approach selectively computes and sparsifies
the similarity relationships, reducing the required computations. Different methods like
sparse Attention (Li et al. 2019), kernelized Attention (Kitaev et al. 2020), and low-rank
Attention (Zhou et al. 2021) have been developed to exploit the sparsity or low-rank
structure in the similarity matrix, resulting in computational savings.In the following
sections, we will explore these two approaches as a guiding framework to introduce
optimization methods for the Attention mechanism in long-term time series prediction.
Shorten the Length of Time Series Processed by Attention Mechanism: Informer (Zhou et
al. 2021) utilizes the Transformer framework, which integrates convolution and pooling
operations to shorten the length of time series gradually. This sequential aggregation of
time steps occurs at each layer. As a result, the computational burden of the Transformer is
significantly diminished. Therefore, the input time series of the jth layer in Informer can be
expressed as follows:
XXXˆ j =MaxPool ELU(Conv1d(XXXˆ j 1 )) , (35)
−
(cid:31) (cid:30)
where XXXˆ j RD × Lj represents the output time series of the jth layer, and L j denotes its
s th e a q t u L en j c < e l L e ∈ n j gt 1 h . . U T n h li e k e in I p n u fo t r o m f e t r h , e P j a t t h c h la T y S e T r, ( d N e i n e o e te t d a l a . s 2 0 XXXˆ 22 j − ) 1 ta ∈ ke R s D a × d L i j ff − e 1, r e i n s t w ap o p rt r h o a n c o h t i b n y g
−
dividing the original input sequence into multiple fixed-length short sequences, as depicted
1 3

Deep learning-based time series forecasting Page 27 of 67 23
in Fig. 5. This decision allows the model to transition from processing a single, lengthy
sequence to managing multiple, short sequences. Additionally, PatchTST treats these short
sequences as cohesive units and employs its attention mechanism to compute their similar-
ity relationships. As a result, the space complexity of the attention mechanism in PatchTST
is reduced from the original O(L2) to O(N2), where L represents the length of the input
sequence and N denotes the number of units, with N L. Consequently, PatchTST
(cid:31)
achieves significant reductions in space complexity. Other models, such as Pyraformer (Liu
et al. 2021) and Triformer (Cirstea et al. 2022), employ a similar strategy to PatchTST
in optimizing the space complexity of the attention mechanism. Compared to Informer,
PatchTST demonstrates a greater advantage in optimizing space complexity due to its treat-
ment of sliced short sequences during processing. Notably, this advantage becomes more
pronounced when handling long-term time series, as the growth rate of N remains relatively
slow compared to the progressive increase of L.
Sparse the Attention Mechanism: Sparsing the attention mechanism involves selectively
computing the similarity between time steps within the mechanism while preserving the origi-
nal length of the input sequence. These approaches can also effectively address the space com-
plexity associated with the attention mechanism. Building upon this concept, LogTrans (Li et
al. 2019) introduces the LogSparse Self-Attention mechanism. Illustrated in Fig. 15, for the tth
time step of the input time sequence, LogSparse Self-Attention determines the index of the time
step with which the similarity relationship needs to be computed as follows:
III t = t 2 (cid:30) log2t (cid:29) ,t 2 (cid:30) log2t − 1 (cid:29) ,t 2 (cid:30) log2t − 2 (cid:29) , ,t 20,t , (36)
− − − ··· −
(cid:31) (cid:30)
where III represents the index of the time step in the tth time step where similarity computation
t
is required. LogSparse Self-Attention selectively filters similarity relationships based on their
temporal proximity to the current time step, prioritizing relationships among nearby time steps.
Additionally, LogSparse Self-Attention is causal, meaning that the current time step disregards
similar information from future time steps.Unlike LogTrans, which utilizes distance between
time steps as a filtering criterion, Reformer (Kitaev et al. 2020) aims to group time steps in the
feature space and compute attention within the groups, thereby achieving sparsity in the atten-
tion mechanism. The challenge of rapidly finding nearest neighbors in high-dimensional spaces
can be addressed by Locality-Sensitive Hashing(LSH). A hashing scheme that assigns each
time step to a hash space is called locality-sensitive if nearby vectors get the same hash with
high probability and distant ones do not. Based on the LSH, Reformer proposes the LSH Atten-
tion mechanism. LSH Attention maps the input time series into a hash space, allowing attention
computations only between time steps close to each other within this space.
To map time steps into the hash space, Reformer establishes the hash function as fol-
lows: h(xxx)=argmax RRR (cid:31) xxx, − RRR (cid:31) xxx , where RRR ∈ RD × b/2, and b represents the number
of hashes, which corresponds to the dimension of the hash space. As depicted in Fig. 16, the
(cid:31)(cid:30) (cid:29)(cid:28)
time steps within the input time series are mapped to the hash space using this hash function.
Based on the positional relationship of the time steps in the hash space, Reformer organizes
all time steps into distinct groups. Within each group, each time step computes the similarity
relationship exclusively with other time steps belonging to the same group. This selective
calculation significantly reduces the computation cost of the attention mechanism.
1 3

| 23  Page 28 of 67 |     |     | X. Song et al. |     |
| ----------------- | --- | --- | -------------- | --- |
Informer (Zhou et al. 2021) also incorporates sparsity within its attention mechanism.
However, unlike LogTrans and Reformer, Informer adopts a unique filtering criterion for
similarity relationships based on the following assumption: within the attention mechanism,
if the query vector qqq possesses intricate temporal information, its attention distribution with
respect to all key vectors should deviate significantly from a uniform distribution. Based on
this concept, Informer introduces ProbSparse Self-Attention, which selectively retains the
computation results of the query according to the score of each query. The scoring function
for query vector qqq can be expressed as follows:
|     |               | L qqqkkk  | L                  |      |
| --- | ------------- | --------- | ------------------ | ---- |
|     |               | (cid:31)j | 1 qqqkkk (cid:31)j |      |
|     | M(qqq,KKK)=ln | exp√ D    | k ,                | (37) |
√D
−L k
|     |     | j=1      | j=1      |     |
| --- | --- | -------- | -------- | --- |
|     |     | (cid:31) | (cid:31) |     |
where KKK =[kkk , ,kkk ] represents the key matrix containing all the key vectors in the time
1 ··· L
series, and kkk RDk denotes the key vector corresponding to the jth time step in the time
j
| series. The scoring function primarily evaluates the query vectors qqq by analyzing their simi- ∈ |     |     |     |     |
| ------------------------------------------------------------------------------------------------- | --- | --- | --- | --- |
larity distribution relative to the other key vectors kkk. Ultimately, ProbSparse Self-Attention
selectively retains the Top-U query vectors.LogTrans, Reformer, and Informer employ
Sparse Attention mechanisms that rely on specific filtering criteria for computing similarity
relationships. For example, LogTrans filters the target of attention computation based on the
distance between time steps. Reformer maps the data into a hash space and filters the target
of attention computation based on the distance among time steps in the hash space. Informer
filters query vectors based on the distribution of similarities between the query vector and
all key vectors. In contrast, Crossformer (Zhang and Yan 2022) adopts a different approach
by not employing a specific filtering criterion to sparsify the attention mechanism. Instead, it
introduces transition units to avoid direct similarity computations between time steps. This
strategy effectively reduces the space complexity of the Attention mechanism.
In the Crossformer model, when processing the input time serok with a length of L using
the attention mechanism, c transition units are introduced, where c L. These transition
(cid:31)
units act as intermediate components for performing similarity computations between query
vectors and key vectors within the attention mechanism. This approach helps avoid the
space complexity of O(L2) associated with direct similarity computations between query
|     |     | RDk× | L and a value matrix V RDk× | L, the  |
| --- | --- | ---- | --------------------------- | ------- |
vectors and key vectors. For a key matrix K
|     |     | ∈   | ∈   |     |
| --- | --- | --- | --- | --- |
Attention mechanism with transition units can be expressed as follows:
KKK RRR
(cid:31)
|     | OOO              | =VVVSoftmax( | ),               | (38) |
| --- | ---------------- | ------------ | ---------------- | ---- |
|     |                  | 1            | √ D              |      |
|     |                  |              | k                |      |
|     | QQQ =WWW XXX,KKK | =WWW OOO     | ,VVV =WWW OOO ,  | (39) |
|     | 2 Q              | 2 K          | 1 2 V 1          |      |
KKK QQQ
(cid:31)2 2),
|     | OOO 2 | =VVV 2 Softmax( |     | (40) |
| --- | ----- | --------------- | --- | ---- |
√ D
|     |     |     | k   |     |
| --- | --- | --- | --- | --- |
where each column of R RDk× c represents the transition unit, which are learnable param-
∈
eter vectors. As evident from the provided equations, the inclusion of these transition units
1 3

Deep learning-based time series forecasting Page 29 of 67 23
allows for a reduction in the space complexity of the attention mechanism from O(L2) to a
linear complexity of O(2cL)=O(L).
5 Loss function
According to the optimization objective, the loss function commonly used in time series
prediction models can be classified into two main types:
(1) Loss function with a single optimization objective. This type of loss function primarily
focuses on optimizing the gap in value between the prediction and the ground truth.
The simplicity of this category of loss functions makes it widely employed. However, it
has the limitation of solely aiming to minimize the gap in value between the prediction
and the ground truth. Consequently, this category of loss functions faces challenges
when dealing with time series that contain intricate temporal patterns and exhibit strong
fluctuations.
(2) Hybrid loss function that optimizes the multiple objectives. To address the aforemen-
tioned issue, an alternative group of models utilizes hybrid loss functions that optimize
the multiple objectives. This category of loss functions aims to combine multiple loss
functions to optimize different modules of the model, enabling collaborative predictions.
In the following sections, we will discuss these two types of loss functions separately.
5.1 Single-objective loss function
MAE, MSE: Mean Absolute Error (MAE) and Mean Square Error (MSE) are commonly
utilized loss functions in time series prediction tasks. They are employed to optimize the gap
in value between the predicted values and the ground truth. MAE calculates the average of
the absolute value of the prediction errors, while MSE calculates the average of the squared
prediction errors. The specific formulas are provided below:
O D
1 1
MAE(YYY,YYYˆˆˆ)= O ×D | y i,j − yˆ i,j | , (41)
(cid:31)
i=1
(cid:31)
j=1
O D
1 1
MSE(YYY,YYYˆˆˆ)= O ×D (y i,j − yˆ i,j )2, (42)
(cid:31)
i=1
(cid:31)
j=1
where YYY
∈
RO
×
D represents the ground truth, YYYˆˆˆ
∈
RO
×
D represents the prediction, and
O is the length of the prediction and D is the number of variables. From this equation, it
becomes evident that when dealing with challenging-to-predict data points, MSE exacer-
bates the gap in value between the prediction and the ground truth, imposing a more sub-
stantial penalty. On the other hand, MAE lacks this characteristic and treats all prediction
points uniformly. In time series forecasting tasks, using MAE as the loss function can effec-
tively mitigate the impact of outliers during model training. This approach is particularly
beneficial for datasets like electricity and wind power data. Conversely, when the chal-
1 3

23 Page 30 of 67 X. Song et al.
lenging prediction points in the time series dataset containning significant information, as
observed in Traffic datasets (Wu et al. 2021) and Exchange Rate datasets (Lai et al. 2018),
the model can opt for MSE as the loss function to emphasize their importance during the
training process.In essence, employing MSE or MAE implies a disregard for the direction
of the error (Wang and Bovik 2009), meaning we are indifferent to whether the prediction
surpasses or falls short of the actual value. However, this characteristic becomes crucial in
specific time prediction scenarios. For instance, when forecasting the remaining lifespan of
an engine, our prediction must underestimate the true value to prevent potential accidents.
Quantile Loss: Quantile loss is commonly used as a loss function in time series predic-
tion tasks. Unlike MSE and MAE, quantile loss penalizes positive and negative deviations
between predicted and true values differently. Given the prediction YYYˆˆˆ and the ground truth
YYY, the quantile loss between them can be expressed as:
=q max(0,YYY YYYˆˆˆ)+(1 q) max(0,YYYˆˆˆ YYY), (43)
L ∗ − − ∗ −
where the quantile coefficient q [0,1] can be adjusted to meet the specific demands of
∈
the prediction task. For example, in aircraft remaining useful life prediction (Zhang et al.
2023, 2023; Wang et al. 2023), it is often desired for the model’s predictions to be lower
than the actual lifespan of the aircraft to minimize potential risks. Therefore, a quantile
coefficient q <0.5 can be used, which increases the penalty imposed by the loss function
on larger predictions. This setting encourages the model to generate smaller predictions.
However, a drawback of quantile loss is the requirement to specify a target quantile, which
is often impractical in many prediction scenarios.In summary, MAE, MSE, and quantile
loss are commonly used loss functions for point forecasts in deep learning models for time
series prediction. These loss functions are effective for both univariate and multivariate
predictions, as well as for single-step and multi-step forecasting. Among the three, MSE is
suitable when prediction errors are expected to follow a Gaussian distribution. However,
when a dataset contains numerous outliers, MSE can be heavily affected by these, poten-
tially leading to model failure. In such cases, MAE might be a better choice as the loss
function. In specific scenarios, such as Remaining Useful Life (RUL) prediction (Zhang et
al. 2023, 2023; Wang et al. 2023), where biased predictions are necessary, quantile loss is
often employed.
Beyond point forecasts, interval forecasts (Armstrong 2001) represent another approach
in time series prediction. As the name suggests, this method provides a range of possible
outcomes rather than a single point, offering insights into the model’s confidence or predic-
tion uncertainty. For interval forecasts, deep learning models typically use quantile loss as
the loss function. Unlike in point forecasts, when quantile loss is applied to interval fore-
casts, the quantile parameter q in (43) represents a range rather than a single value. Due to
space limitations, this paper does not explore interval forecasting in detail.
5.2 Hybrid loss function
The shortcomings of the aforementioned loss functions lie in their optimization objectives,
which solely focus on the numerical distance between predictions and ground truth. Addi-
tionally, models based on a single optimization target are often structurally simple and can-
not incorporate other structured predictive mechanisms such as SSM (State Space Model)
1 3

Deep learning-based time series forecasting Page 31 of 67 23
(Salinas et al. 2020; Lin et al. 2021) or GAN (Generative Adversarial Network) (Wu et al.
2020; Mogren 2016; Goodfellow et al. 2014). Therefore, in order to leverage these special-
ized structures for collaborative predictions, some models utilize a joint loss function to
optimize multiple objectives introduced by different structures within the model.
Negative Log-likelihood: SSDNet (Lin et al. 2021) incorporates MAE alongside the
negative log-likelihood as its loss function. This loss function allows for the simultaneous
consideration of the numerical gap and distributions between the prediction and the ground
truth. By tuning a parameter, SSDNet balances the influences of the MAE and the negative
log-likelihood. The SSDNet model comprises the Transformer and the SSM (State Space
Model) network. The SSM network is a mathematical framework that describes the relation-
ship between latent states and observable data in a time series.
SSMs (Durbin and Koopman 2012; Hyndman 2008; Seeger et al. 2016) enable the incor-
poration of structural assumptions into the model, making them particularly well-suited for
scenarios where the time series structure is well-understood. This approach enhances the
model’s interpretability and promotes efficient data utilization during the learning process.
However, traditional SSMs are limited in their ability to infer shared patterns from a dataset
of similar time series, as they are fitted individually to each time series.
SSDNet utilizes the Transformer to learn and estimate the parameters of the SSM net-
work, enabling the generation of interpretable predictions through the SSM network. There-
fore, SSDNet requires optimization of the SSM network’s predictions and parameters.
SSDNet employs a hybrid loss function that integrates MAE and negative log-likelihood.
This approach serves the dual purpose of optimizing the model’s prediction through MAE
and refining the parameters of the SSM network via negative log-likelihood.
The negative log-likelihood loss function requires the model’s output to represent the
parameters of a probability distribution. The objective of this loss function is to maximize
the probability of a real sample satisfying the predicted distribution. Therefore, for a real
sample Y=[y , ,y ], and the parameters θθθ representing the predicted probability dis-
1 ··· O
tribution by the model, the optimization objective of the negative log-likelihood can be
formulated as follows:
O
θθθ ∗ =argmin logP(yyy i θθθ). (44)
− |
θθθ
i=1
(cid:31)
Generating Adversarial Loss Functions: Inspired by the training method of Generative
Adversarial Networks (GANs) (Goodfellow et al. 2014; Wu et al. 2020; Mogren 2016),
some models aim to utilize adversarial training to sequences generated by the generator
should closely resemble real sequences and remain indistinguishable by the discriminator.
Therefore, its optimization objective can be represented as:
m
G
inmax V(
D
,G)=E
x ∼ pdata(x)
[log
D
(x)]+E
z ∼ pz(z)
[log(1
−D
(G(z)))],
(45)
D
where is the discriminator of the model, G is the generator of the model, x p data (x)
D ∼
denotes the data samples drawn from the true distribution, and z p z (z) denotes the fake
∼
data samples generated by the generator. From Equation (45), it is evident that the optimiza-
tion goal is twofold: the discriminator aims to distinguish between sequences generated
D
1 3

| 23  Page 32 of 67 |     |     |     | X. Song et al. |     |
| ----------------- | --- | --- | --- | -------------- | --- |
by the generator and real sequences, while the generator strives to produce fake sequences
that the discriminator cannot differentiate from real ones. Next, we will use the AST (Wu et
al. 2020) model as an example to introduce the loss function of the generative adversarial
approach.AST introduces the integration of the GAN training method into time series pre-
diction tasks. It utilizes the Transformer model as a generator, referred to as G, to generate
predictions. The predictions and the real samples are then fed into a discriminator, denoted
as  , for discrimination. The discriminator consists of multiple fully connected layers,
D
forming a fully connected network. The GAN loss function consists of two main compo-
nents: the discriminator loss and the generator loss. In AST, the generator loss is derived
from the quantile loss function P (), quantifying the numerical gap between the prediction
ρ
·
and the real sample. Conversely, the discriminator loss is based on the log-likelihood loss,
which evaluates the ability of the discriminator to distinguish the fake and real samples.
|     | YYYˆ               |        | =Concat(XXX,YYYˆ),   |            |      |
| --- | ------------------ | ------ | -------------------- | ---------- | ---- |
|     | =Transformer(XXX), |        | YYY                  |            | (46) |
|     |                    |        | fake                 |            |      |
|     |                    | Loss=P | (YYY ,YYYˆ)+λE[log(1 | (YYY ))],  |      |
|     | Generator          |        | ρ O                  | fake       | (47) |
−D
  Discriminator Loss=E[ log (YYY real ) log(1 (YYY fake ))],  (48)
|     |     |            | − D −              | −D     |      |
| --- | --- | ---------- | ------------------ | ------ | ---- |
|     |     | =Generator | Loss+Discriminator | Loss,  | (49) |
L
where YYYˆ
RD O represents the prediction generated by the Transformer model. D rep-
|     | ∈ × |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
resents the number of variables, and O represents the length of the prediction. On the
other hand, YYY  refers to the corresponding ground truth for the prediction. Additionally,
O
RD (L+O) denotes the fake samples generated by the generator, where L represents
| YYY | ×   |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
fake ∈
the length of the input sequence preceding the prediction. These fake samples are generated
|                                           |     |     | RD (L+O) represents the real samples drawn  |     |     |
| ----------------------------------------- | --- | --- | ------------------------------------------- | --- | --- |
| based on the generator’s predictions. YYY |     |     | real ×                                      |     |     |
∈
from the real dataset.
6  Experiments
In this section, we conduct extensive experiments to evaluate the performance of the afore-
mentioned methods on various real-world time series prediction scenarios.
6.1  Dataset
As shown in Table 3, our empirical results are based on datasets from diverse domains, such
as energy, exchange rate, traffic, and disease. Detailed descriptions of these datasets are
provided below:
(1)  Energy: The ETT (Electricity Transformer Temperature) dataset (Zhou et al. 2021) con-
sists of data collected from power transformers in a specific region of China, spanning
from July 2016 to July 2018. It includes seven distinct features, such as the load and
oil temperature of the power transformers. The ETTh1 and ETTh2 datasets encompass
1 3

Deep learning-based time series forecasting Page 33 of 67 23
17,420 samples with a sampling interval of 1 h, covering 7 features. On the other hand,
the ETTm1 and ETTm2 datasets comprise 69,680 samples with a sampling interval of
5 min, also encompassing 7 features. The Electricity dataset (Wu et al. 2021) contains
hourly electricity consumption data from 321 customers from 2012 to 2014. It con-
sists of 321 features and a total of 26,304 samples. Due to the temporal characteristics
of electricity, electricity datasets naturally exhibit strong periodicity. For instance, the
electricity data shows evident monthly periodicity due to the influence of temperature
during the summer and winter seasons. Additionally, the electricity dataset also exhibits
pronounced daily periodicity across different time periods within a day.
(2) Exchange Rates: The Exchange dataset (Lai et al. 2018) covers daily exchange rates
for eight currencies from January 1990 to October 2010. It contains eight features and
a total of 7,588 samples. Unlike other time series data, the exchange rate data does not
exhibit significant periodicity patterns, and its fluctuation changes are more complex.
Additionally, important time series information is often contained in the extreme points
of the exchange rate data, making methods like smoothing potentially result in the loss
of important information.
(3) Traffic: The Traffic dataset (Wu et al. 2021) comprises hourly data from the Califor-
nia Department of Transportation for the years 2015-2016. It captures road occupancy,
measured by various San Francisco Bay Area freeway sensors. The dataset includes
862 features and a total of 17,544 samples. Unlike electricity datasets, traffic datasets
exhibit evident short-term periodic patterns. Moreover, traffic accidents frequently lead
to abnormal occupancy rates on the associated roadways, resulting in a higher incidence
of outliers in the traffic dataset, which can impact model performance.
(4) Illness: The ILI (Influenza-Like Illness) dataset (Wu et al. 2021) comprises weekly
records of patients diagnosed with influenza illness, as reported by the U.S. Centers for
Disease Control and Prevention, spanning from 2002 to 2021. This dataset includes 7
features, such as the proportion of patients with ILI and the total number of patients. It
follows a sampling interval of 1 week and 966 samples. Due to the dynamics of disease
transmission, the illness datasets exhibit fluctuations characterized by prominent long-
term yearly and monthly periodic patterns and noteworthy short-term trends.
6.2 Model
Table 4 summarizes all the models that appear in the experimental section. For the above
models, we have referred to the optimal parameter settings in their respective papers and
source code, and we have applied these parameter settings in the following experiments.
6.3 Evaluation metric
The time series forecasting task is typically categorized as a regression problem. Conse-
quently, evaluation metrics commonly used in regression tasks are employed to assess the
forecasting performance of models in the time series forecasting task. Based on previous
studies (Wu et al. 2021; Zhou et al. 2022; Li et al. 2019; Zhou et al. 2021), we utilize the
mean absolute error (MAE) and mean square error (MSE) as fundamental metrics to evalu-
ate the performance of models. At the same time, to facilitate a more intuitive comparison
1 3

| 23  Page 34 of 67 |     |     |     |     | X. Song et al. |
| ----------------- | --- | --- | --- | --- | -------------- |
of the prediction outcomes across various models, we integrated two supplementary evalu-
ation metrics, MAPE, and R2, in addition to MAE and MSE. MAPE measures the relative
error between predicted and actual values, ranging from 0 to positive infinity; the closer to 0,
the more accurate the predictions. R2 evaluates how well the independent variables explain
the dependent variable, with values from 0 to 1; the closer to 1, the better the model fits the
data. Nonetheless, we presented Mean Absolute Percentage Error(MAPE) and R2 solely
in specific experiments due to space constraints. The definitions of all metrics are given by
N O D
1
|     | MAE( , ˆˆˆ)= |       | yn                               | yˆn ,    |      |
| --- | ------------ | ----- | -------------------------------- | -------- | ---- |
|     |              |       | o,d−                             | o,d      | (50) |
|     | YYY YYY      | N O D |                                  |          |      |
|     |              | × ×   | n=1 o=1 d=1                      |          |      |
|     |              |       | (cid:31)(cid:31)(cid:31)(cid:30) | (cid:30) |      |
|     |              |       | (cid:30)                         | (cid:30) |      |
N O D
|     |              | 1     |                                  | 2             |      |
| --- | ------------ | ----- | -------------------------------- | ------------- | ---- |
|     | MSE( , ˆˆˆ)= |       | yn                               | yˆn ,         | (51) |
|     | YYY YYY      | N O D | o,d−                             | o,d           |      |
|     |              | × ×   | n=1 o=1 d=1                      |               |      |
|     |              |       | (cid:31)(cid:31)(cid:31)(cid:30) | (cid:29)      |      |
|     |              |       | N O D yn                         | +(cid:23) yˆn |      |
|     | ˆˆˆ)=        | 1     | o,d                              | o,d           |      |
|     | MAPE( ,      |       |                                  | − ,           | (52) |
|     | YYY YYY      | N O D |                                  | y n +(cid:23) |      |
|     |              |       | (cid:30)                         | o ,d (cid:30) |      |
  × × (cid:31) n=1 (cid:31) o=1 (cid:31) d=1 (cid:30) (cid:30)
|     |     |     | (cid:30) | (cid:30) |     |
| --- | --- | --- | -------- | -------- | --- |
|     |     |     | (cid:30) | (cid:30) |     |
Table 4 Summarizes all the models in the experimental section (cid:30) (cid:30)
| Category | Model | Year Category | Model |     | Year |
| -------- | ----- | ------------- | ----- | --- | ---- |
Statistic model ARIMA (Zhang  2003 Transformer-based CNN-1D (Gudelek et al.  2017
|     | 2003)             |      | 2017)                     |     |      |
| --- | ----------------- | ---- | ------------------------- | --- | ---- |
|     | ETS (Hyndman and  | 2008 | LogTrans (Li et al. 2019) |     | 2019 |
Khandakar 2008)
|     |     |     | Reformer (Kitaev et al.  |     | 2020 |
| --- | --- | --- | ------------------------ | --- | ---- |
2020)
| FC-based | Autoencoder (Lv et  | 2014 | AST (Wu et al. 2020) |     | 2020 |
| -------- | ------------------- | ---- | -------------------- | --- | ---- |
al. 2014)
|     | SAE (Lv et al. 2014)    | 2014 | Informer (Zhou et al. 2021) |     | 2021 |
| --- | ----------------------- | ---- | --------------------------- | --- | ---- |
|     | Nbeat (Oreshkin et al.  | 2020 | Autoformer (Wu et al.       |     | 2021 |
|     | 2019)                   |      | 2021)                       |     |      |
|     | Dlinear (Yun et al.     | 2022 | Aliformer (Qi et al. 2021)  |     | 2021 |
2019)
|     |     |     | TFT (Lim et al. 2021) |     | 2021 |
| --- | --- | --- | --------------------- | --- | ---- |
RNN-based GRU (Dey and Salem  2018 TDformer (Zhang et al.  2022
|     | 2017)               |      | 2022)                        |     |      |
| --- | ------------------- | ---- | ---------------------------- | --- | ---- |
|     | LSTnet (Lai et al.  | 2018 | Fedformer (Zhou et al.       |     | 2022 |
|     | 2018)               |      | 2022)                        |     |      |
|     | DeepAR (Salinas et  | 2020 | NS-Transformer (Liu et al.   |     | 2022 |
|     | al. 2020)           |      | 2022)                        |     |      |
|     |                     |      | Pyraformer (Liu et al. 2021) |     | 2022 |
CNN-based CNN-1D (Gudelek et  2017 ETSformer (Woo et al.  2022
|     | al. 2017)             |      | 2022)                      |     |      |
| --- | --------------------- | ---- | -------------------------- | --- | ---- |
|     | TCN (Bai et al. 2018) | 2018 | PatchTST (Nie et al. 2022) |     | 2023 |
|     |                       |      | Crossformer (Zhang and     |     | 2024 |
Yan 2022)
State space  SSDNet (Lin et al.  2021 Scaleformer (Shabani et al.  2024
| model | 2021) |     | 2022)                      |     |      |
| ----- | ----- | --- | -------------------------- | --- | ---- |
|       |       |     | Triformer (Cirstea et al.  |     | 2024 |
2022)
1 3

Deep learning-based time series forecasting Page 35 of 67  23
F ig. 17 Validation split of datasets
2
|            | N O D                         | yn yˆn      |            |      |
| ---------- | ----------------------------- | ----------- | ---------- | ---- |
| R2( ˆˆˆ)=1 | n=1 o=1 d=1                   | o,d−        | o,d        |      |
| ,          |                               |             | ,          | (53) |
| YYY YYY −  |                               |             | 2          |      |
|            | (cid:31)N (cid:31)O (cid:31)D | (cid:30) yn | y (cid:29) |      |
|            | n=1 o=1 d=1                   | o,d−        |            |      |

(cid:28) (cid:27)
|     | (cid:31) (cid:31) (cid:31) |     |     |     |
| --- | -------------------------- | --- | --- | --- |
where y = 1 N O D (yn ),  = YYY1,YYY2,...,YYYN  represents the set of
| N O D n=1 o=1          | d=1 o,d  |     |     |     |
| ---------------------- | -------- | --- | --- | --- |
| × ×                    | YYY {    |     | }   |     |
| (cid:31) YYYˆ1(cid:31) | (cid:31) |     |     |     |
true values, and  ˆˆˆ = ,YYYˆ2 ,. ..,YYYˆN  denotes the set of predicted values generated by
| YYY { | }   |     |     |     |
| ----- | --- | --- | --- | --- |
the model. Here, N signifies the number of elements within the set, indicating the presence
of N instances. Each instance is characterized by two elements within the set with dimen-
sions of RO D. The parameter (cid:31) is a small value close to 0, introduced to prevent division
×
by zero scenarios. In our code implementation, we have uniformly set (cid:31) to 0.005 across
different models to handle such cases effectively.
6.4  Main results
In this section, we perform experimental analyses on the models and methods mentioned
earlier, considering various perspectives:
1.  Comprehensive Prediction Accuracy Assessment: We will assess the prediction accu-
racy of all the mentioned models on 5 time series datasets derived from 4 distinct
domains. This assessment aims to provide a comprehensive evaluation of the models’
performances.
2.  Investigation of Limitations: Considering the limitations of current complex models,
we will investigate the underlying causes by focusing on two aspects.
(1) Shuffling Analysis: By shuffling the input time series, we can analyze the model’s
ability to capture the sequential order of the data. This analysis involves comparing
the model’s prediction accuracy before and after shuffling.
(2) Extending the Lookback Window Analysis: Another aspect involves extending the
length of the input time series while maintaining a consistent prediction length.
1 3

X. Song et al.
tnemirepxe
gnitsacerof
seires
emit
etairavitlum
eht
fo
stluser
laitraP
5
elbaT
ILI
egnahcxE
1hTTE
ataD
ledoM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
cirteM
7454.0
%83.54
5199.0
3846.0
4097.0
%22.2
9050.0
9261.0
7484.0
%82.86
9814.0
6654.0
trohS
remrofdeF
8600.0
±
8610.0
±
7310.0
±
4800.0
±
3000.0
±
0000.0
±
2000.0
±
9000.0
±
4600.0
±
0030.0
±
7900.0
±
3600.0
±
3842.0
%59.35
9773.1
4208.0
1826.0
%90.3
4490.0
7622.0
0014.0
%57.67
4574.0
5394.0
ralugeR
1401.0
±
3560.0
±
1071.0
±
4370.0
±
9510.0
±
5000.0
±
9200.0
±
7400.0
±
6300.0
±
9070.0
±
5210.0
±
6200.0
±
0362.0
%74.84
1053.1
1197.0
3980.0
±
%73.5
9962.0
7193.0
3422.0
%84.38
9795.0
4175.0
gnoL
−
9100.0
±
1300.0
±
5500.0
±
7200.0
±
6100.0
±
3000.0
±
4200.0
±
9200.0
±
6430.0
±
2410.0
±
2900.0
±
5700.0
±
5342.0
%51.46
9763.1
9508.0
4518.0
%98.1
1430.0
1431.0
4314.0
%36.86
3245.0
6205.0
trohS
remrofSTE
2780.0
±
0050.0
±
6931.0
±
2060.0
±
0930.0
±
7100.0
±
2500.0
±
9210.0
±
4951.0
±
2020.0
±
5581.0
±
4180.0
±
2031.0
%77.66
3049.1
8879.0
9547.0
%04.2
0550.0
3271.0
4913.0
%76.37
4706.0
4145.0
ralugeR
−
4701.0
±
8610.0
±
8231.0
±
0350.0
±
8420.0
±
7000.0
±
5200.0
±
6600.0
±
7661.0
±
7220.0
±
8902.0
±
1880.0
±
5122.0
%24.95
3869.1
6200.1
7722.0
%73.4
7871.0
2413.0
1851.0
%70.48
3117.0
0416.0
gnoL
−
6850.0
±
7210.0
±
1840.0
±
2400.0
±
1510.0
±
7000.0
±
1700.0
±
3600.0
±
0461.0
±
6110.0
±
4591.0
±
6090.0
±
2966.0
%29.73
1450.2
2159.0
3928.0
%19.1
2530.0
7531.0
4855.0
%44.26
8873.0
2314.0
trohS
remrofssorC
−
0824.0
±
8040.0
±
2663.0
±
2411.0
±
1400.0
±
3000.0
±
6100.0
±
1300.0
±
1920.0
±
0700.0
±
3720.0
±
8110.0
±
8822.1
%06.34
3524.2
8980.1
7584.0
%71.3
1090.0
0222.0
5964.0
%26.86
3934.0
2254.0
ralugeR
−
6230.0
±
6000.0
±
6840.0
±
7110.0
±
0060.0
±
4000.0
±
5100.0
±
9300.0
±
0910.0
±
8410.0
±
3910.0
±
4400.0
±
1664.1
%64.54
7608.2
8891.1
7654,1-
%35.6
5053.0
9154.0
5711.0
%87.19
7008.0
9136.0
gnoL
−
1712.0
±
3410.0
±
2141.0
±
4440.0
±
3420.1
±
5500.0
±
1950.0
±
0140.0
±
2341.0
±
4880.0
±
9881.0
±
0970.0
±
7292.0
%55.53
7659.0
0446.0
9468.0
%45.1
6520.0
4011.0
8675.0
%41.66
3663.0
9793.0
trohS
raenilD
8610.0
±
4210.0
±
3500.0
±
8800.0
±
1000.0
±
0000.0
±
0
±
1000.0
±
6610.0
±
0100.0
±
0710.0
±
5500.0
±
0520.0
%20.24
2612.1
9967.0
1877.0
%02.2
6940.0
6751.0
7494.0
%59.17
9224.0
0634.0
ralugeR
8020.0
±
5200.0
±
6010.0
±
8600.0
±
0500.0
±
3000.0
±
5100.0
±
3200.0
±
2420.0
±
6300.0
±
0420.0
±
3700.0
±
9171.0
%57.53
2542.1
4997.0
8291.0
%71.4
1651.0
3892.0
2263.0
%16.18
7915.0
2505.0
gnoL
−
9020.0
±
2400.0
±
6310.0
±
3500.0
±
4740.0
±
5000.0
±
3300.0
±
6300.0
±
6130.0
±
4800.0
±
7820.0
±
5110.0
±
5746.0
%03.13
7035.0
4854.0
2448.0
%55.1
1720.0
5111.0
9475.0
%26.56
4763.0
8004.0
trohS
TSThctaP
6820.0
±
4210.0
±
8410.0
±
5900.0
±
2400.0
±
0000.0
±
3000.0
±
7000.0
±
7120.0
±
6200.0
±
8020.0
±
8600.0
±
2624.0
%83.34
2099.0
0816.0
6937.0
%22.2
3250.0
6851.0
5784.0
%91.27
3524.0
1044.0
ralugeR
7300.0
±
7610.0
±
5570.0
±
7130.0
±
3610.0
±
2000.0
±
4100.0
±
2100.0
±
1030.0
±
3400.0
±
8920.0
±
7900.0
±
7400.0
%58.13
3731.1
4247.0
3931.0
%25.4
9791.0
9123.0
3513.0
%83.48
9055.0
5125.0
gnoL
7423.0
±
4110.0
±
4002.0
±
5301.0
±
9310.0
±
2000.0
±
8200.0
±
2200.0
±
3730.0
±
3800.0
±
3030.0
±
3110.0
±
23 Page 36 of 67
1 3

Deep learning-based time series forecasting
)deunitnoc(
5
elbaT
ILI
egnahcxE
1hTTE
ataD
ledoM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
cirteM
3885.0
%15.04
1938.1
4749.0
2858.0
%75.1
8620.0
2311.0
0115.0
%44.16
3534.0
9754.0
trohS
STAEB-N
−
9811.0
±
2700.0
±
1590.0
±
7320.0
±
5700.0
±
4000.0
±
3100.0
±
0300.0
±
2000.0
±
1900.0
±
1100.0
±
6000.0
±
3125.1
%20.64
1735.2
0331.1
4677.0
%42.2
6050.0
3061.0
4881.0
%82.09
9497.0
8216.0
ralugeR
−
7611.0
±
4800.0
±
3190.0
±
4720.0
±
0100.0
±
1000.0
±
4000.0
±
3100.0
±
7900.0
±
7600.0
±
6500.0
±
3100.0
±
2692.2
%76.15
1461.3
0703.1
5811.0
%13.4
1661.0
9603.0
0260.0
%41.99
8098.0
2866.0
gnoL
−
5831.0
±
5110.0
±
4890.0
±
6720.0
±
6971.0
±
9100.0
±
6110.0
±
6310.0
±
1700.0
±
5200.0
±
2500.0
±
6000.0
±
5972.0
%84.85
2053.1
2097.0
4157.0
%44.2
6950.0
6871.0
5514.0
%76.86
1694.0
1405.0
trohS
remrofotuA
8620.0
±
4040.0
±
4090.0
±
2820.0
±
7430.0
±
7100.0
±
1010.0
±
7610.0
±
0970.0
±
8040.0
±
1180.0
±
3640.0
±
9602.0
%32.06
1084.1
7938.0
5756.0
%69.2
9680.0
9512.0
1304.0
%23.57
6974.0
0794.0
ralugeR
7950.0
±
6920.0
±
7160.0
±
9820.0
±
3720.0
±
0100.0
±
5600.0
±
0800.0
±
8400.0
±
4500.0
±
9710.0
±
4600.0
±
2531.0
%13.84
5545.1
8348.0
2502.0
%47.5
7992.0
9514.0
5622.0
%41.78
8216.0
6675.0
gnoL
−
1550.0
±
0020.0
±
8690.0
±
2330.0
±
3951.0
±
3400.0
±
1440.0
±
2330.0
±
7310.0
±
8110.0
±
0130.0
±
5900.0
±
1155.0
%51.43
0037.0
3945.0
0628.0
%88.1
5430.0
4331.0
3925.0
%70.07
7914.0
6034.0
trohS
remrofsnarT-SN
2220.0
±
1310.0
±
6170.0
±
2500.0
±
2700.0
±
2000.0
±
8000.0
±
4100.0
±
4800.0
±
5400.0
±
8800.0
±
2600.0
±
3633.0
%66.64
8051.1
9907.0
2096.0
%86.2
0370.0
1391.0
0314.0
%62.77
6494.0
2184.0
ralugeR
0670.0
±
3680.0
±
6932.0
±
3870.0
±
6910.0
±
9000.0
±
1700.0
±
8800.0
±
2210.0
±
2300.0
±
7300.0
±
2700.0
±
4602.0
%20.53
9913.1
9757.0
4710.0
%20.5
8932.0
7263.0
1311.0
%47.48
4707.0
0706.0
gnoL
6450.0
±
4710.0
±
8121.0
±
7720.0
±
1670.0
±
1200.0
±
3120.0
±
2610.0
±
9170.0
±
1120.0
±
7853.0
±
4510.0
±
yticirtcelE
cffiarT
ataD
ledoM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
cirteM
3608.0
%20.71
7781.0
3792.0
4776.0
%12.81
3963.0
9613.0
trohS
remrofdeF
5200.0
±
8100.0
±
4200.0
±
9100.0
±
4100.0
±
0100.0
±
1100.0
±
0100.0
±
4108.0
%19.61
4291.0
9003.0
7276.0
%99.71
9963.0
2713.0
ralugeR
1300.0
±
3100.0
±
0300.0
±
8200.0
±
4600.0
±
1300.0
±
8200.0
±
5300.0
±
1195.0
%81.62
2493.0
6464.0
3856.0
%43.81
6783.0
4323.0
gnoL
3871.0
±
0560.0
±
9171.0
±
0031.0
±
3100.0
±
3100.0
±
7200.0
±
5100.0
±
Page 37 of 67 23
1 3

X. Song et al.
)deunitnoc(
5
elbaT
yticirtcelE
cffiarT
ataD
ledoM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
cirteM
8677.0
%81.91
3612.0
5813.0
3264.0
%46.72
8706.0
2564.0
trohS
remrofSTE
8100.0
±
4000.0
±
7100.0
±
5000.0
±
9110.0
±
8500.0
±
2410.0
±
1410.0
±
2947.0
%53.02
0342.0
0733.0
3844.0
%75.72
1274.0
1274.0
ralugeR
0100.0
±
4000.0
±
0100.0
±
9000.0
±
1410.0
±
8000.0
±
3800.0
±
3800.0
±
1707.0
%19.12
4282.0
2463.0
9504.0
%53.72
9976.0
0084.0
gnoL
2100.0
±
5000.0
±
2100.0
±
6000.0
±
4220.0
±
1500.0
±
5520.0
±
9900.0
±
6948.0
%88.01
8541.0
2432.0
9237.0
%92.51
5803.0
3542.0
trohS
remrofssorC
5500.0
±
2200.0
±
4500.0
±
9300.0
±
4200.0
±
1000.0
±
0300.0
±
3200.0
±
1038.0
%75.11
7461.0
5842.0
8996.0
%62.71
2543.0
8172.0
ralugeR
2800.0
±
2300.0
±
0800.0
±
6400.0
±
3100.0
±
1000.0
±
6100.0
±
5100.0
±
7097.0
%84.31
2202.0
2882.0
–
–
–
–
gnoL
3700.0
±
3300.0
±
1700.0
±
5400.0
±
2387.0
%88.41
4002.0
6762.0
1325.0
%38.42
7145.0
8373.0
trohS
raenilD
3000.0
±
3000.0
±
3000.0
±
3000.0
±
3000.0
±
2000.0
±
3000.0
±
2000.0
±
3497.0
%98.41
2991.0
1472.0
8455.0
%29.22
5705.0
8743.0
ralugeR
4100.0
±
7100.0
±
3100.0
±
0200.0
±
3000.0
±
1000.0
±
3000.0
±
2000.0
±
1387.0
%89.41
5902.0
6192.0
5595.0
%15.12
1864.0
2923.0
gnoL
2000.0
±
100.0
±
2000.0
±
1000.0
±
1000.0
±
5000.0
±
1000.0
±
2000.0
±
1808.0
%93.41
0681.0
4752.0
7407.0
%30.71
9733.0
4562.0
trohS
TSThctaP
8000.0
±
1100.0
±
8000.0
±
2100.0
±
9100.0
±
5000.0
±
2200.0
±
0100.0
±
9408.0
%50.41
1981.0
1362.0
8486.0
%75.71
5163.0
5572.0
ralugeR
2000.0
±
4000.0
±
2000.0
±
4000.0
±
2100.0
±
5000.0
±
4100.0
±
3100.0
±
4387.0
%02.41
2902.0
1682.0
6866.0
%00.81
7583.0
5382.0
gnoL
3000.0
±
1000.0
±
2000.0
±
0
±
2000.0
±
3000.0
2000.0
±
3000.0
±
4507.0
%37.81
5582.0
0673.0
7174.0
%19.42
6806.0
6883.0
trohS
STAEB-N
1100.0
±
4100.0
±
1100.0
±
7000.0
±
9200.0
±
6000.0
±
3300.0
±
8000.0
±
0651.0
%12.93
6718.0
3096.0
1560.0
%04.13
8140.1
2686.0
ralugeR
3200.0
±
6100.0
±
2200.0
±
1000.0
±
5000.0
±
9000.0
±
5000.0
±
2000.0
±
5360.0
%97.14
4409.0
4737.0
2100.0
%87.13
8721.1
0047.0
gnoL
4000.0
±
5100.0
±
3000.0
±
5000.0
±
8000.0
±
6100.0
±
7000.0
±
0200.0
±
23 Page 38 of 67
1 3

Deep learning-based time series forecasting Page 39 of 67  23

 dilav on taht setacidni "–" .cilati a htiw dethgilhgih era stluser tseb dnoces eht dna dlob ni dethgilhgih era stluser tseb ehT -gnol dna ,mret-raluger ,mret-trohs rof O htgnel tuptuo eht etoned ’gnoL’ dna ’,ralugeR’ ’,trohS’ .deniatbo eb dluoc stluser
|     | 7400.0 ± 3100.0 ± 9910.0 ± | 7100.0 ±      | 9100.0 ± 7500.0 ± |     |
| --- | -------------------------- | ------------- | ----------------- | --- |
|     | 7108.0 9197.0 8927.0       | 1138.0 9518.0 | 5787.0            |     |
2R
|      | 1300.0 ± 2000.0 ± 8600.0 ± | 5000.0 ±      | 6100.0 ± 8100.0 ± |                                                                                                |
| ---- | -------------------------- | ------------- | ----------------- | ---------------------------------------------------------------------------------------------- |
| EPAM | %35.71 %44.71 %73.02       | %22.31 %26.31 | %25.41            |                                                                                                |
|      | 5400.0 ± 2100.0 ± 2910.0 ± | 7100.0 ±      | 9100.0 ± 5500.0 ± | stnemirepxe fo noitaived dradnats dna eulav egareva eht troper eW .noitciderp seires emit mret |
|      | 2291.0 6102.0 9062.0       | 7361.0 4871.0 | 2502.0            |                                                                                                |
ESM
yticirtcelE
|     | 4400.0 ± 9100.0 ± 6410.0 ± | 4100.0 ±      | 0200.0 ± 2500.0 ± |     |
| --- | -------------------------- | ------------- | ----------------- | --- |
|     | 5003.0 9803.0 7753.0       | 6462.0 1772.0 | 4203.0            |     |
EAM
|     | 3600.0 ± 5710.0 ± 2600.0 ± | 3600.0 ±      | 0600.0 ± 3000.0 ± |     |
| --- | -------------------------- | ------------- | ----------------- | --- |
|     | 9466.0 0626.0 9836.0       | 8796.0 6876.0 | 7856.0            |     |
2R
|     | 4000.0 ± 7100.0 ± 1200.0 ± | 1100.0 ±      | 3100.0 ± 6510.0 ± |     |
| --- | -------------------------- | ------------- | ----------------- | --- |
|     | %98.71 %72.91 %28.91       | %43.71 %44.81 | %20.12            |     |
EPAM
|     | 1500.0 ± 6020.0 ± 6600.0 ± | 1700.0 ±      | 8600.0 ± 1000.0 ± |     |
| --- | -------------------------- | ------------- | ----------------- | --- |
|     | 4473.0 2024.0 5904.0       | 1943.0 8173.0 | 8004.0            |     |
ESM
|         | 8200.0 ± 8800.0 ± 7700.0 ± | 3400.0 ±      | 4400.0 ± 0100.0 ± |     |
| ------- | -------------------------- | ------------- | ----------------- | --- |
| cffiarT | 5713.0 9143.0 3933.0       | 0192.0 6403.0 | 2023.0            |     |
EAM
|     | ralugeR | ralugeR |     |     |
| --- | ------- | ------- | --- | --- |
cirteM
| ataD | trohS gnoL | trohS | gnoL |     |
| ---- | ---------- | ----- | ---- | --- |
)deunitnoc( 5 elbaT
remrofsnarT-SN
remrofotuA
ledoM
1 3

X. Song et al.
tnemirepxe
gnitsacerof
seires
emit
etairavinu
eht
fo
stluser
laitraP
6
elbaT
ILI
egnahcxE
1hTTE
ataD
ledoM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
cirteM
0790.0−
%36.7
6642.0
3504.0
0648.0
%54.1
1820.0
8921.0
9325.0
%60.02
2991.0
5233.0
trohS
remrofdeF
1426.0
±
0300.0
±
1570.0
±
3390.0
±
7300.0
±
0000.0
±
7000.0
±
5100.0
±
9500.0
±
0900.0
±
5200.0
±
7200.0
±
9719.0
%59.8
7892.0
3944.0
1856.0
%91.2
7160.0
0391.0
9864.0
%39.12
0222.0
5553.0
ralugeR
−
2785.1
±
7700.0
±
6571.0
±
4051.0
±
3020.0
±
6000.0
±
6300.0
±
8500.0
±
3110.0
±
1010.0
±
8400.0
±
3500.0
±
4542.6
%76.01
6644.0
5955.0
2391.0
%79.3
5602.0
1553.0
9303.0
%44.32
7772.0
1004.0
gnoL
−
−
5204.5
±
6000.0
±
1281.0
±
6231.0
±
2950.0
±
6000.0
±
7900.0
±
9600.0
±
8610.0
±
2100.0
±
4500.0
±
9300.0
±
3975.0
%13.11
4473.0
0974.0
9409.0
%51.1
4710.0
4401.0
3325.0
%49.91
4991.0
9233.0
trohS
remrofSTE
−
9797.0
±
7500.0
±
1780.0
±
9260.0
±
6600.0
±
4000.0
±
2100.0
±
1500.0
±
7120.0
±
8000.0
±
5800.0
±
6010.0
±
9920.1
%07.61
4614.0
1145.0
1328.0
%35.1
9130.0
6831.0
3054.0
%73.12
8922.0
4063.0
ralugeR
−
7936.0
±
8410.0
±
7401.0
±
3850.0
±
7610.0
±
8000.0
±
0300.0
±
5800.0
±
2930.0
±
6200.0
±
4610.0
±
8410.0
±
0026.5
%40.61
0325.0
2036.0
8714.0
%18.2
4101.0
9552.0
4742.0
%65.32
5003.0
4914.0
gnoL
−
3793.4
±
2220.0
±
6561.0
±
0111.0
±
6760.0
±
4200.0
±
0310.0
±
9920.0
±
2490.0
±
4900.0
±
3040.0
±
3820.0
±
1996.8
%71.52
8481.2
1281.1
1278.0
%53.1
3320.0
9221.0
7265.0
%63.91
9281.0
6413.0
trohS
remrofssorC
−
9007.7
±
9830.0
±
2634.1
±
2643.0
±
5510.0
±
0100.0
±
8200.0
±
6110.0
±
4510.0
±
5200.0
±
1600.0
±
4500.0
±
4479.6
%32.03
8455.1
0841.1
0927.0
%69.1
9840.0
1181.0
8294.0
%44.02
0212.0
4043.0
ralugeR
−
099.2
±
2100.0
±
0743.0
±
1180.0
±
3730.0
±
3100.0
±
8600.0
±
9510.0
±
7110.0
±
8200.0
±
9400.0
±
1300.0
±
8758.91
%36.82
8315.1
6061.1
2333.0
%91.3
2711.0
6392.0
7752.0
%68.42
0692.0
2914.0
gnoL
−
3673.31
±
5110.0
±
5711.0
±
9070.0
±
5110.0
±
3000.0
±
1100.0
±
4500.0
±
7810.0
±
0400.0
±
7500.0
±
6500.0
±
8742.2
%34.41
1217.0
0796.0
1129.0
%20.1
4410.0
7290.0
7685.0
%83.81
9271.0
7892.0
trohS
raenilD
−
2658.1
±
7200.0
±
6991.0
±
9731.0
±
3000.0
±
0000.0
±
1000.0
±
2000.0
±
4810.0
±
5300.0
±
2700.0
±
9600.0
±
5117.5
%96.91
2301.1
3739.0
2656.0
%94.1
9250.0
8671.0
1335.0
%66.91
2591.0
4123.0
ralugeR
−
9341.4
±
7300.0
±
1272.0
±
3641.0
±
5320.0
±
3000.0
±
2810.0
±
4430.0
±
6910.0
±
4400.0
±
2800.0
±
7600.0
±
5827.31
%11.12
2520.1
0439.0
6054.0
%47.2
6990.0
5642.0
8483.0
%39.12
5542.0
2173.0
gnoL
−
1221.01
±
1100.0
±
8912.0
±
6701.0
±
9150.0
±
7000.0
±
5800.0
7700.0
±
0020.0
±
2600.0
±
4010.0
±
9800.0
±
23 Page 40 of 67
1 3

Deep learning-based time series forecasting
)deunitnoc(
6
elbaT
ILI
egnahcxE
1hTTE
ataD
ledoM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
cirteM
9103.0
%45.6
4161.0
4782.0
3719.0
%50.1
1510.0
8490.0
9575.0
%16.81
4771.0
1303.0
trohS
TSThctaP
3723.0
±
2100.0
±
7120.0
±
8030.0
±
5100.0
±
1000.0
±
3000.0
±
9000.0
±
1610.0
±
8200.0
±
2600.0
±
6500.0
±
6603.0−
%62.9
3322.0
2453.0
1528.0
%05.1
5130.0
2531.0
3615.0
%79.91
1202.0
6723.0
ralugeR
9557.0
±
0300.0
±
3340.0
±
6910.0
±
6100.0
±
1000.0
±
3000.0
±
0100.0
±
1710.0
±
4300.0
±
1700.0
±
3500.0
±
4345.4−
%83.11
0443.0
4064.0
9063.0
%77.2
3111.0
1842.0
4973.0
%69.12
8742.0
3963.0
gnoL
7319.3
±
4100.0
±
5460.0
±
2620.0
±
6500.0
±
1000.0
±
0100.0
±
9000.0
±
9820.0
±
5600.0
±
0410.0
±
3110.0
±
2347.6
%61.72
5518.1
7462.1
9346.0
%60.1
3510.0
9590.0
6865.0
%43.91
5081.0
9113.0
trohS
STAEB-N
−
1409.3
±
0010.0
±
3183.0
±
8771.0
±
5664.0
±
3000.0
±
1100.0
±
0400.0
±
3700.0
±
7100.0
±
5200.0
±
9200.0
±
1554.91
%33.43
2014.3
3037.1
2228.0
%35.1
1230.0
3831.0
0044.0
%15.22
1432.0
0663.0
ralugeR
−
6291.21
±
8700.0
±
0117.0
±
1162.0
±
4300.0
±
2000.0
±
6000.0
±
6200.0
±
8200.0
±
8300.0
±
2100.0
±
6100.0
±
7054.53
%11.53
5936.2
4545.1
6234.0
%17.2
6890.0
8642.0
9882.0
%05.42
7382.0
4114.0
gnoL
−
4844.32
±
4700.0
±
6413.0
±
0431.0
±
1031.0
±
4200.0
±
8220.0
±
4920.0
±
6310.0
±
7400.0
±
2300.0
±
3000.0
±
6893.0
%92.9
5013.0
8434.0
5587.0
%07.1
1930.0
7351.0
0984.0
%60.12
8312.0
3743.0
trohS
remrofotuA
−
2419.0
±
5600.0
±
3431.0
±
6811.0
±
5390.0
±
0300.0
±
0710.0
±
3430.0
±
7920.0
±
5600.0
±
8110.0
±
5500.0
±
7944.1
%72.01
1324.0
9045.0
0327.0
%19.1
50.0
7271.0
6544.0
%37.12
7132.0
4363.0
ralugeR
−
5074.1
±
1410.0
±
4001.0
±
6590.0
±
2240.0
±
2100.0
±
6700.0
±
7210.0
±
3710.0
±
3500.0
±
2700.0
±
3900.0
±
1326.6
%23.11
7494.0
9706.0
2304.0
%04.4
1142.0
1493.0
3392.0
%07.32
9182.0
1404.0
gnoL
−
1306.5
±
0300.0
±
4291.0
±
5261.0
±
3364.0
±
6700.0
±
9080.0
±
6480.0
±
2660.0
±
2500.0
±
3520.0
±
4810.0
±
3631.0
%80.7
0352.0
9683.0
4388.0
%52.1
3120.0
5211.0
7465.0
%98.91
1281.0
3613.0
trohS
remrofsnarT-SN
−
3909.0
±
5200.0
±
9651.0
±
3631.0
±
1700.0
±
4000.0
±
3100.0
±
0400.0
±
1900.0
±
5800.0
±
4300.0
±
5600.0
±
5456.0−
%40.01
0482.0
7014.0
1321.0
%68.1
4940.0
3861.0
0584.0
%92.12
2512.0
1743.0
ralugeR
7249.0
±
4000.0
±
3940.0
±
8430.0
±
1560.0
±
6000.0
±
4400.0
±
9600.0
±
9410.0
±
1100.0
±
2600.0
±
6300.0
±
9134.2−
%41.21
9652.0
5614.0
5220.0
%85.3
4671.0
6023.0
2981.0
%29.72
7474.0
9625.0
gnoL
−
2931.2
±
7200.0
±
8550.0
±
7160.0
±
4490.0
±
4100.0
±
9510.0
±
9410.0
±
6762.0
±
5520.0
±
9301.0
±
2660.0
±
Page 41 of 67 23
1 3

X. Song et al.
)deunitnoc(
6
elbaT
yticirtcelE
cffiarT
ataD
ledoM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
cirteM
5657.0
%32.82
0842.0
2373.0
0577.0
%19.11
6282.0
0124.0
trohS
remrofdeF
1800.0
±
2810.0
±
2800.0
±
1800.0
±
5500.0
±
6200.0
±
0700.0
±
6600.0
±
0408.0
%11.42
7691.0
0523.0
2967.0
%04.21
1982.0
1624.0
ralugeR
7110.0
±
0900.0
±
9110.0
±
4210.0
±
6010.0
±
6600.0
±
7310.0
±
4310.0
±
4653.0
%95.94
1756.0
3616.0
2467.0
%51.21
8392.0
1824.0
gnoL
2394.0
±
2212.0
±
6305.0
±
6982.0
±
3500.0
±
9200.0
±
6600.0
±
0600.0
±
7154.0
%10.74
4855.0
3765.0
9016.0
%53.61
5884.0
3955.0
trohS
remrofSTE
1520.0
±
4110.0
±
5520.0
±
9010.0
±
1300.0
±
2200.0
±
9300.0
±
4600.0
±
5053.0
%15.35
0266.0
5136.0
5595.0
%03.61
7605.0
2765.0
ralugeR
1210.0
±
9300.0
±
3210.0
±
7600.0
±
4000.0
±
5000.0
±
2000.0
±
2000.0
±
7912.0
%54.26
7697.0
9076.0
3075.0
%43.61
5535.0
6575.0
gnoL
6000.0
±
0200.0
±
6000.0
±
9200.0
±
4110.0
±
8100.0
±
3410.0
±
4800.0
±
4677.0
%58.81
7722.0
3303.0
3377.0
%05.41
6482.0
5193.0
trohS
remrofssorC
2960.0
±
4310.0
±
5070.0
±
7740.0
±
3700.0
±
5400.0
±
2900.0
±
1800.0
±
6128.0
%01.02
8181.0
6972.0
2777.0
%49.11
0972.0
4873.0
ralugeR
0810.0
±
2220.0
±
3810.0
±
8310.0
±
1100.0
±
0100.0
±
4100.0
±
3200.0
±
8067.0
%59.42
3442.0
0533.0
–
–
–
–
gnoL
4250.0
±
3130.0
±
5350.0
±
5220.0
±
0870.0
%80.95
0939.0
5796.0
3766.0
%91.41
7714.0
7864.0
trohS
raenilD
2200.0
±
0100.0
±
2200.0
±
8100.0
±
3200.0
±
5000.0
±
9200.0
±
2400.0
±
4403.0
%73.05
0907.0
0695.0
7596.0
%91.31
1183.0
8934.0
ralugeR
7800.0
±
7100.0
±
9800.0
±
5200.0
±
5000.0
±
3000.0
±
6000.0
±
3000.0
±
8025.0
%94.93
3984.0
4684.0
9327.0
%39.21
3443.0
1024.0
gnoL
8000.0
±
2000.0
±
9000.0
±
5000.0
±
1000.0
±
1000.0
±
2000.0
±
2000.0
±
4463.0
%48.15
3746.0
9425.0
8108.0
%33.01
8842.0
4153.0
trohS
TSThctaP
8400.0
±
4100.0
±
9400.0
±
5200.0
±
2000.0
±
5000.0
±
3000.0
±
9000.0
±
9915.0
%93.24
3984.0
7344.0
8197.0
%15.01
6062.0
0163.0
ralugeR
5400.0
±
3400.0
6400.0
±
6300.0
±
0100.0
±
3000.0
±
3100.0
±
6000.0
±
5846.0
%59.13
9853.0
0773.0
5187.0
%00.11
2272.0
0073.0
gnoL
6600.0
±
8200.0
±
7600.0
±
7300.0
±
1000.0
±
3000.0
±
2000.0
±
2000.0
±
23 Page 42 of 67
1 3

Deep learning-based time series forecasting
)deunitnoc(
6
elbaT
yticirtcelE
cffiarT
ataD
ledoM
2R
EPAM
ESM
EAM
2R
EPAM
ESM
EAM
cirteM
8105.0
%51.64
4705.0
7735.0
6707.0
%20.61
1763.0
7464.0
trohS
STAEB-N
2620.0
±
5510.0
±
6620.0
±
5310.0
±
4200.0
±
7000.0
±
9200.0
±
7100.0
±
3263.0
%52.54
9946.0
0526.0
2490.0
%92.52
7431.1
3088.0
ralugeR
8800.0
±
5100.0
±
9800.0
±
9100.0
±
7000.0
±
2500.0
±
8000.0
±
1000.0
±
7322.0
%76.24
6297.0
5376.0
4710.0
%38.13
6422.1
9859.0
gnoL
8100.0
±
6400.0
±
8100.0
±
7200.0
±
3200.0
±
9100.0
±
9200.0
±
9100.0
±
9146.0
%43.93
8463.0
3944.0
5668.0
%16.31
1092.0
4924.0
trohS
remrofotuA
3840.0
±
5430.0
±
2940.0
±
4230.0
±
2101.0
±
5000.0
±
8900.0
±
6800.0
±
9603.0
%02.23
8892.0
6214.0
4037.0
%87.31
8833.0
0164.0
ralugeR
0210.0
±
8700.0
±
2210.0
±
1700.0
±
9900.0
±
3000.0
±
5410.0
±
7300.0
±
3564.0
%38.54
0645.0
7675.0
4957.0
%17.21
9692.0
4724.0
gnoL
3431.0
±
1250.0
±
1731.0
±
8860.0
±
0100.0
±
2400.0
±
5400.0
±
7300.0
±
9318.0
%48.12
6981.0
3313.0
0607.0
%48.8
1963.0
4564.0
trohS
remrofsnarT-SN
8200.0
±
2400.0
±
8200.0
±
8300.0
±
8200.0
±
0200.0
±
3300.0
±
3100.0
±
4508.0
%27.12
4891.0
9813.0
6290.0
%45.9
4241.1
4088.0
ralugeR
6800.0
±
2200.0
±
8800.0
±
0210.0
±
2100.0
±
3100.0
±
5110.0
±
0500.0
±
3928.0
%14.12
3471.0
9903.0
1210.0
%38.01
0922.1
1669.0
gnoL
1010.0
±
7600.0
±
3010.0
±
3110.0
±
9100.0
±
6400.0
±
8300.0
±
2500.0
±
on
taht
setacidni
"–"
.enilrednu
a
htiw
dethgilhgih
era
stluser
tseb
dnoces
eht
dna
dlob
ni
dethgilhgih
era
stluser
tseb
ehT
dna
,mret-raluger
,mret-trohs
rof
O
htgnel
tuptuo
eht
etoned
’gnoL’
dna
’,ralugeR’
’,trohS’
.deniatbo
eb
dluoc
stluser
dilav
stnemirepxe
fo
noitaived
dradnats
dna
eulav
egareva
eht
troper
eW
.noitciderp
seires
emit
mret-gnol
Page 43 of 67 23
1 3

| 23  Page 44 of 67 |     |     |     |     | X. Song et al. |
| ----------------- | --- | --- | --- | --- | -------------- |
Table 7 The comparison of prediction results between the model before and after shuffling the input sequence
| Dataset | ETTh1 | Traffic | ILI     | Exchange |     |
| ------- | ----- | ------- | ------- | -------- | --- |
| Metric  | MAE   | MSE MAE | MSE MAE | MSE MAE  | MSE |
DLinear Ori. 0.4317 0.4089 0.3495 0.5034 0.9440 1.8397 0.1573 0.0487
Shuf. 0.6655 0.8234 0.7535 1.1284 1.2645 2.8216 0.3443 0.2153
Drop 54.16% 101.37% 115.59% 124.16% 33.95% 53.37% 118.88% 342.09%
PatchTST Ori. 0.4070 0.3865 0.3329 0.4540 0.7055 1.1853 0.1609 0.0520
Shuf. 0.7860 1.0518 0.7664 1.1403 1.1530 2.3930 0.6244 0.6201
Drop 93.12% 172.13% 130.22% 151.17% 63.43% 101.89% 288.07% 1092.50%
Crossformer Ori. 0.4454 0.4160 0.7634 1.1349 1.0672 2.3385 0.2575 0.1118
Shuf. 0.7744 1.0274 0.7610 1.1493 1.2951 3.2890 0.6540 0.5988
|     | Drop 73.84% | 146.97%   | 1.27% 21.35% | 28.90% 153.98% | 435.60% |
| --- | ----------- | --------- | ------------ | -------------- | ------- |
−
0.31%
NS-Trans- Ori. 0.6121 0.7382 0.3403 0.4252 0.8402 1.7844 0.1695 0.0565
former
Shuf. 0.7796 1.0340 0.7617 1.1400 1.1948 2.7962 0.6183 0.6120
Drop 27.36% 40.07% 123.83% 168.11% 29.68% 56.70% 264.78% 983.19%
ETSformer Ori. 0.5246 0.5397 0.4722 0.6042 0.9896 1.9351 0.1817 0.0596
Shuf. 0.6653 0.8575 0.7753 1.1925 1.1065 2.1160 0.3195 0.1867
|     | Drop 26.82% | 58.88% 64.19% | 97.37% 11.81% | 9.35% 75.84% | 213.26% |
| --- | ----------- | ------------- | ------------- | ------------ | ------- |
LSTnet Ori. 0.6960 0.9192 0.7115 0.9279 1.2103 2.7753 0.8062 0.8898
Shuf. 0.7548 1.0156 0.7654 1.1435 1.1605 2.6412 0.8217 0.9303
|     | Drop 8.45% | 10.49% 7.58% | 23.24% | 1.92% | 4.55% |
| --- | ---------- | ------------ | ------ | ----- | ----- |

|     |     |     | 4.11% − | 4.83% − |     |
| --- | --- | --- | ------- | ------- | --- |
N-BEATS Ori. 0.6098 0.7883 0.6878 1.0420 1.2166 2.7416 0.1618 0.0514
Shuf. 0.6479 0.8235 0.7507 1.1260 1.2702 3.2442 0.3484 0.2103
|     | Drop 6.25% | 4.47% 9.15% | 8.06% 4.41% | 18.33% 115.33% | 309.14% |
| --- | ---------- | ----------- | ----------- | -------------- | ------- |
TDformer Ori. 0.6742 0.7662 0.3524 0.4342 1.4841 3.6448 1.5010 3.2275
Shuf. 0.7689 1.0767 0.7591 1.1573 1.4038 3.7931 1.2450 2.1344
|     | Drop 14.05% | 40.52% 115.41% | 166.54% | 4.07%  |        |
| --- | ----------- | -------------- | ------- | ------ | ------ |
|     |             |                | −       | −      | −      |
|     |             |                | 5.41%   | 17.06% | 33.87% |
Autoformer Ori. 0.5389 0.5443 0.3190 0.3814 0.8414 1.5320 0.2162 0.0885
Shuf. 0.8101 1.1000 0.8059 1.2024 1.1584 2.2000 0.5779 0.5850
Drop 50.32% 102.09% 152.63% 215.26% 37.68% 43.60% 167.30% 561.02%
Fedformer Ori. 0.4980 0.4695 0.3168 0.3695 0.8095 1.3598 0.2245 0.0951
Shuf. 0.8130 1.1080 0.8036 1.1964 1.2082 2.4158 0.5740 0.5861
Drop 63.25% 136.00% 153.66% 223.79% 49.25% 77.66% 155.68% 516.30%
Ori. denotes the original prediction accuracy, Shuf. denotes the prediction accuracy after the shuffling, and
|     |     | (Shuf. | Ori.) |     |     |
| --- | --- | ------ | ----- | --- | --- |
Drop is calculated as follows: Drop= − 100%. The maximum results of the decline rate
Ori. ×
are highlighted in bold
Through this analysis, we can examine the model’s susceptibility to overfitting and
the level of interference caused by noise.
3.  Trend and Season Information Analysis: To evaluate the model’s capacity to capture
trend and season information, experiments will be conducted on an artificial dataset
explicitly incorporating trend and season terms. This analysis assesses how well the
models can capture such temporal patterns.
4.  Attention Module Evaluation for Transformer-based Models: For the Transformer-
based models, our primary focus will be on assessing the performance of different
1 3

Deep learning-based time series forecasting Page 45 of 67  23

| Table 8 The prediction results  | Dataset | ETTh1 | Exchange |     |
| ------------------------------- | ------- | ----- | -------- | --- |
for each model across various
|     | Metric | MAE | MSE MAE | MSE |
| --- | ------ | --- | ------- | --- |
datasets, considering different
lengths of the lookback window.  DLinear 48 0.4389 0.4367 0.1582 0.0500
The best results are highlighted  96 0.4317 0.4089 0.1572 0.0487
| in bold |                | 192 0.4301 | 0.3994 0.1585 | 0.0488 |
| ------- | -------------- | ---------- | ------------- | ------ |
|         | PatchTST       | 48 0.4434  | 0.4459 0.6148 | 0.6097 |
|         |                | 96 0.4323  | 0.4058 0.6079 | 0.5925 |
|         |                | 192 0.4289 | 0.3965 0.5881 | 0.5371 |
|         | Crossformer    | 48 0.4464  | 0.4338 0.5892 | 0.5196 |
|         |                | 96 0.4454  | 0.4157 0.5743 | 0.5051 |
|         |                | 192 0.4452 | 0.4175 0.5705 | 0.5170 |
|         | NS-Transformer | 48 0.5164  | 0.5420 0.6182 | 0.6200 |
|         |                | 96 0.4990  | 0.5165 0.6193 | 0.6100 |
|         |                | 192 0.5115 | 0.5360 0.6023 | 0.5655 |
|         | Fedformer      | 48 0.4962  | 0.4656 0.1946 | 0.0731 |
|         |                | 96 0.5082  | 0.4748 0.2255 | 0.0937 |
|         |                | 192 0.5170 | 0.4834 0.2782 | 0.1343 |
|         | Autoformer     | 48 0.5388  | 0.5289 0.1997 | 0.0767 |
|         |                | 96 0.5439  | 0.5480 0.2298 | 0.0978 |
|         |                | 192 0.5521 | 0.5536 0.2290 | 0.0909 |
|         | N-BEATS        | 48 0.6110  | 0.7959 0.1598 | 0.0517 |
|         |                | 96 0.6099  | 0.7874 0.1633 | 0.0522 |
|         |                | 192 0.6130 | 0.7872 0.1632 | 0.0513 |
|         | ETSformer      | 48 0.5061  | 0.5318 0.1795 | 0.0581 |
|         |                | 96 0.5257  | 0.5393 0.1837 | 0.0602 |
|         |                | 192 0.5482 | 0.5604 0.1842 | 0.0611 |
|         | LSTnet         | 48 0.6989  | 0.9221 0.8237 | 0.9241 |
|         |                | 96 0.6991  | 0.9270 0.8073 | 0.8907 |
|         |                | 192 0.7097 | 0.9385 0.7675 | 0.8195 |
|         | TDformer       | 48 0.6514  | 0.7323 1.3290 | 2.5359 |
|         |                | 96 0.6705  | 0.7506 1.4197 | 2.9719 |
|         |                | 192 0.6845 | 0.7826 1.3507 | 2.7163 |
Attention modules utilized in the models. To achieve this, a comparative experiment
has been designed to evaluate the prediction accuracy and complexity associated with
various Attention modules.These analyses aim to gain insights into the strengths, limi-
tations, performances, and characteristics of the models and methods mentioned earlier.
6.4.1  Evaluation of model prediction accuracy
In order to comprehensively evaluate the prediction accuracy of each model, this section
presents experimental results on both multivariate and univariate time series prediction
tasks.
As shown in Fig. 17, We employ two different validation set splitting methods: (1) simple
time split validation and (2) sliding window validation. In simple time split validation (Wu
et al. 2021; Zhou et al. 2021; Kitaev et al. 2020; Li et al. 2019), the training, validation,
and test sets are sequentially divided based on time. Sliding window validation (Liu and
1 3

| 23  Page 46 of 67 |     |     |     |     |     | X. Song et al. |
| ----------------- | --- | --- | --- | --- | --- | -------------- |

Fig. 18 The prediction results for the trend term. The horizontal axis represents the time step index, and
the vertical axis represents the model’s prediction result. Ground Truth represents the true value cor-
responding to the predicted segment, and we highlight the better-performing model results and Ground
Truth

Fig. 19 The prediction results for the season term. The horizontal axis represents the time step index,
and the vertical axis represents the model’s prediction result. Ground Truth represents the true value cor-
responding to the predicted segment, and we highlight the better-performing model results and Ground
Truth
Table 9 The prediction of the model for the trend and season term in the artificial dataset. The best results are
highlighted in bold and the second best results are highlighted with a underline
| Data       | Original Sequence |        | Trend Term |        | Season Term |        |
| ---------- | ----------------- | ------ | ---------- | ------ | ----------- | ------ |
| Metric     | MAE               | MSE    | MAE        | MSE    | MAE         | MSE    |
| DLinear    | 0.0145            | 0.0003 | 0.1456     | 0.0351 | 0.1500      | 0.0351 |
| Fedformer  | 0.0612            | 0.0057 | 0.1074     | 0.0181 | 0.0823      | 0.0115 |
| Autoformer | 0.1246            | 0.0276 | 0.1602     | 0.0433 | 0.1861      | 0.0570 |
| N-BEATS    | 0.0269            | 0.0014 | 0.6359     | 0.4996 | 0.9032      | 0.8704 |
| ETSformer  | 0.1705            | 0.0447 | 0.1501     | 0.0351 | 0.1162      | 0.0206 |
| LSTnet     | 0.0481            | 0.0058 | 0.4210     | 0.1962 | 0.4159      | 0.1921 |
| TDformer   | 0.0718            | 0.0106 | 0.1109     | 0.0193 | 0.1122      | 0.0202 |
1 3

Deep learning-based time series forecasting Page 47 of 67  23

| Table 10 Comparison of predic- | Dataset | ETTh1 | Exchange |     |
| ------------------------------ | ------- | ----- | -------- | --- |
tion results among different At-
|     | Metric | MAE | MSE MAE | MSE |
| --- | ------ | --- | ------- | --- |
tention modules with equivalent
space complexity. We highlight  Auto-Correction 96 0.5160 0.5331 0.4882 0.3837
in bold the results that show  LogSparse Attention 96 0.5285 0.5349 0.4012 0.2340
improvement compared to the  Patch Attention 96 0.4357 0.4015 0.1594 0.0501
vanilla Attention module
|     | Pyraformer Attention | 96 0.5110 | 0.5157 0.5194 | 0.4060 |
| --- | -------------------- | --------- | ------------- | ------ |
|     | Dttention            | 96 0.5648 | 0.6112 0.4739 | 0.3314 |
|     | LSH Attention        | 96 0.5805 | 0.6701 0.5352 | 0.4877 |
|     | ProSparse Attention  | 96 0.6591 | 0.8632 0.4840 | 0.3497 |
|     | FA                   | 96 0.7975 | 1.1465 1.1525 | 1.7961 |
|     | Attention            | 96 0.5310 | 0.5741 0.4605 | 0.3402 |

Table 11 Time series prediction
|     | Dataset |     | ETTh1 |     |
| --- | ------- | --- | ----- | --- |
results of models based on At-
|     | Metric |     | MAE | MSE |
| --- | ------ | --- | --- | --- |
tention. The best results for each
|     | PatchTST | 48  | 0.3932 | 0.3506 |
| --- | -------- | --- | ------ | ------ |
prediction length are highlighted
| in bold |             | 96  | 0.4309 | 0.4027 |
| ------- | ----------- | --- | ------ | ------ |
|         |             | 336 | 0.5126 | 0.5277 |
|         | Crossformer | 48  | 0.5566 | 0.6142 |
|         |             | 96  | 0.4454 | 0.4160 |
|         |             | 336 | 0.5380 | 0.5800 |
|         | Transformer | 48  | 0.4745 | 0.4491 |
|         |             | 96  | 0.5174 | 0.5291 |
|         |             | 336 | 0.6636 | 0.8045 |
|         | Pyraformer  | 48  | 0.4799 | 0.4682 |
|         |             | 96  | 0.5358 | 0.5705 |
|         |             | 336 | 0.6907 | 0.8723 |
|         | Reformer    | 48  | 0.4986 | 0.4984 |
|         |             | 96  | 0.5646 | 0.6062 |
|         |             | 336 | 0.7690 | 1.0775 |
|         | Logtrans    | 48  | 0.5800 | 0.6109 |
|         |             | 96  | 0.5846 | 0.5922 |
|         |             | 336 | 0.7202 | 0.9112 |
|         | Informer    | 48  | 0.5099 | 0.5303 |
|         |             | 96  | 0.6583 | 0.8626 |
|         |             | 336 | 0.8301 | 1.3028 |

Table 12 The maximum memory  Metric Maximum Memory Occupation (MB)
occupation in MB of models
|     | O   | 48  | 96  | 336 |
| --- | --- | --- | --- | --- |
during training
|     | Logtrans    | 1512 | 1554 | 1799 |
| --- | ----------- | ---- | ---- | ---- |
|     | Informer    | 1762 | 1846 | 2075 |
|     | Reformer    | 1639 | 1717 | 2110 |
|     | PatchTST    | 1559 | 1586 | 1602 |
|     | Crossformer | 2489 | 2830 | 3748 |
|     | Transformer | 1738 | 1821 | 2038 |
|     | Pyraformer  | 1659 | 1671 | 1745 |
1 3

23 Page 48 of 67 X. Song et al.
Yang 2022; Malenica et al. 2021; Mintarsih et al. 2023), on the other hand, uses a fixed-size
window that continuously slides over time for training and validation. Compared to simple
time split validation, sliding window validation traverses the entire time series, altering the
training and validation sets as it progresses. This method is particularly suited for slightly
stationary or concept-drifting time series, especially in financial datasets.
We initially apply simple time split validation to all datasets to assess the predictive accu-
racy of the models. Unless otherwise specified, the batch size for all experiments was set to
16. To ensure robustness and reliability, all experimental results presented in this study are
averaged over five trials. Consistent with previous work (Wu et al. 2021; Zhou et al. 2022;
Woo et al. 2022; Zhou et al. 2021), we fixed the input length of the ILI dataset at L=36 and
set the output length O to 12, 24, 48 for short-term, regular-term, and long-term time series
predictions, respectively. For the remaining datasets, we fixed the input length at L=96
and set the output length O to 48, 96, 336 for short-term, regular-term, and long-term pre-
dictions, respectively. All hyperparameters for the deep learning models in the experiments
were set according to the optimal configurations provided in their respective papers or code.
For univariate time series prediction, we used the traditional ARIMA model as the baseline,
while for multivariate time series prediction, we employed the VAR (Vector Autoregressive)
model as the baseline.
The complete experimental results of the multivariate time series prediction task can be
found in Table 13 in Appendix A. From the table, it is observed that among all the mentioned
models, models utilizing the method of time series decomposition (e.g., Fedformer, ETS-
former) and Transformer-based approaches (e.g., Crossformer, PatchTST) exhibit signifi-
cantly superior prediction accuracy compared to the remaining models. Therefore, in Table
5, we only present the experimental results of these two types of methods. It is worth noting
that, to further evaluate the performance of these methods on slightly stationary time series,
in Table 5, we applied sliding window validation with a window size set to one-tenth of the
dataset length for the financial exchange dataset.
In the multivariate time-series forecasting experiment, we observe several noteworthy
findings. DLinear (Yun et al. 2019), which directly extracts temporal features using linear
layers. demonstrates commendable prediction accuracy across the vast majority of datas-
ets. Specifically, in Table 5, we observe that DLinear outperforms the suboptimal model
PatchTST in terms of MAE and Fedformer in terms of MAPE for the ETTh1 dataset. It
achieves improvements of 3.13% and 2.24% for prediction length of 336, respectively. Fur-
thermore, it is worth noting that DLinear also boosted performance by 14.87% on R2 for
prediction lengths of 336 compared with the suboptimal model PatchTST. On the other
hand, Crossformer (Zhang and Yan 2022) primarily focuses on capturing the correlation
among time-series variables, making it particularly effective for datasets characterized by
intricate variables. For instance, in the Electricity dataset, which comprises 321 variables,
surpassing other datasets in terms of the number of variables, Crossformer exhibits a dis-
tinct accuracy advantage over the suboptimal model NS-Transformer. It achieves improve-
ments of 10.93% and 17.70% in MSE and MAPE for prediction lengths of 48, respectively.
However, it is worth noting that Crossformer’s computational cost is considerably high,
which may limit its feasibility for long-term time series prediction tasks due to resource
constraints.
PatchTST (Nie et al. 2022), on the other hand, demonstrates enhanced suitability for
datasets characterized by pronounced long-term periodicity and trends, such as exchange
1 3

Deep learning-based time series forecasting Page 49 of 67 23
rate and illness datasets. By dividing the input time series into fixed-length patches and
emphasizing time-step dependencies between the patches, PatchTST is capable of uncov-
ering long-term temporal relationships and achieves notable improvements in MSE and
R2 compared to other models. For example, in Table 5, PatchTST shows improvements
of 27.30% and 17.49% in MSE and R2, respectively, for a prediction length of 48 on the
ILI dataset compared to the suboptimal model NS-Transformer. Similarly, on the Traffic
dataset, PatchTST exhibits significant accuracy advantages over the suboptimal model NS-
Transformer, achieving improvements of 11.46% in MAE for a prediction length of 336.
The complete results of the univariate time series prediction experiment can be found in
Table 14 in Appendix A. The findings in Table 14, consistent with those in the multivariate
time series forecasting experiment, indicate that models based on time-series decomposition
methods and Transformer-based models exhibit superior prediction accuracy for univariate
time series forecasting compared to other models. Therefore, in Table 6, we present the
results of these two categories separately. Similarly, in Table 6, we applied sliding win-
dow validation with a window size set to one-tenth of the dataset length for the financial
exchange dataset.
In the univariate time series prediction task, both NS-Transformer (Liu et al. 2022) and
DLinear model demonstrate superior performance across various datasets. For instance, in
the long-term prediction task on the ILI dataset, NS-Transformer outperforms the subopti-
mal model PatchTST with improvements of 9.54%, 25.32%, 46.47% in MAE, MSE and R2
, respectively. Comparing the results of multivariate and univariate time series prediction
experiments, it is evident that NS-Transformer exhibits inferior performance in multivariate
scenarios while demonstrating better performance in univariate scenarios. The main rea-
son is that NS-Transformer incorporates non-stationary information from variables into the
attention mechanism and adjusts the output of the attention mechanism based on the non-
stationary information. However, in multivariate prediction tasks, an excessive amount of
non-stationary information negatively impacts the output results of the attention mechanism.
Upon analyzing the empirical results of both multivariate and univariate time series pre-
diction, we observe that DLinear consistently demonstrates superior accuracy compared
to the majority of models. Interestingly, despite using a simpler linear layer for capturing
time-step dependencies, DLinear outperforms numerous sophisticated models. This finding
suggests that existing complex models may have limited capability in effectively capturing
and utilizing time-step information, potentially leading to overfitting and noise interference.
Additionally, compared to other models, DLinear makes more effective use of the sequential
order of the input data, which is likely a key factor in its success.
6.4.2 Evaluation of information mining capabilities for complex models
Based on the analysis of results from both multivariate and univariate time series forecast-
ing experiments, we argue that current complex models are prone to issues such as overfit-
ting and still demonstrate deficiencies in capturing essential time-step dependencies. As a
result, in this section, we will conduct an input shuffling experiment and extend the look-
back window experiment to explore further and clarify the limitations of complex models.
Input Shuffling Experiment: In time series forecasting, the sequential order of time series
often carries significant sequential information. A reliable model should be able to effec-
1 3

23 Page 50 of 67 X. Song et al.
tively capture and understand the sequential order information. As a result, different sequen-
tial orders of input time series should lead to distinct predictions.
To evaluate the model’s ability to capture sequential order information across time steps,
we shuffle the input time series of the model. By comparing the model’s prediction accuracy
before and after shuffling, we can analyze the model’s capacity to capture the sequential
information of the time series.
The input length for the ILI dataset was set to L=36, and the prediction length O
was set to 24. Furthermore, for the other datasets, the input length was set to L=96, and
the prediction length was set to O =96. All empirical results presented in this study were
obtained by averaging the outputs of five randomized experiments. The prediction accuracy
of the model is positively correlated with its capability to extract sequential information.
Based on the analysis in Sect. 6.4.1, it is evident that DLinear and PatchTST exhibit sig-
nificant accuracy advantages over various existing complex models (such as Autoformer,
TDformer, ETSformer, etc.) across all datasets despite maintaining a simpler model struc-
ture. Table 7 shows that PatchTST exhibits the most notable decline in prediction accuracy
after shuffling the input sequence across the ETTh1, ILI, and Exchange datasets. Similarly,
DLinear also experiences a substantial decline in model accuracy following order shuffling
in these datasets. On the other hand, complex models like Autoformer, TDformer, and others
demonstrate minimal impact on their prediction accuracy or even show slight improvements
after input shuffling. For instance, TDformer demonstrates a remarkable 33.87% improve-
ment in MSE on the Exchange dataset after shuffling, whereas LSTnet exhibits a 4.83%
enhancement in MSE on the ILI dataset after shuffling.
Based on the experimental results and the preceding analysis, we can conclude a posi-
tive correlation between the prediction accuracy of a model and its ability to capture the
sequential order of the time series. Moreover, the existing complex models exhibit limited
proficiency in effectively capturing the sequential order of the time series, which explains
their comparatively lower prediction accuracy when compared to simpler models in both
multivariate and univariate time series forecasting experiments. Apart from their weaker
capability to capture the time series sequential information, we also suggest that the com-
plex models face challenges such as overfitting and noise interference. Therefore, our sub-
sequent experiment investigates whether these issues affect these models.
Extending the Lookback Window Experiment: To investigate the potential overfitting and
noise interference of complex models in time series prediction, we conduct extending look-
back window experiments. The size of the lookback window significantly influences the
accuracy of time series prediction, as it determines the amount of historical information
incorporated by the model. Generally, superior models achieve more accurate predictions
using an extended lookback window. However, in the case of models affected by overfitting
and noise interference, an extended lookback window introduces more noise. Due to over-
fitting, the model cannot effectively incorporate additional historical information, resulting
in decreased prediction accuracy with an extended lookback window. Building on this con-
cept, this section presents the extending lookback window experiment.
In our experiment, we set input time series lengths to 48, 96, 192 while keeping the
output prediction length fixed at 96 for the time series. We then examine the changes in
prediction accuracy for each model as the lookback window is extended. It is important
to note that all results presented in this study are obtained by averaging the outputs of five
randomized experiments.
1 3

Deep learning-based time series forecasting Page 51 of 67 23
The experimental results are depicted in Table 8. Complex models, including ETSformer,
TDformer, and Autoformer, achieve their highest prediction accuracies only with the short-
est input time series. In contrast, their accuracies gradually decline as the input time series
lengthens. We believe this is primarily due to their limited ability to handle lengthy input
time series, leading to longer sequences introducing more noise and exacerbating overfit-
ting. However, PatchTST is the only model with optimal prediction accuracy for the longest
input on both datasets. Additionally, on the ETTh1 dataset, DLinear demonstrates the high-
est prediction accuracy for the longest input time series.
Based on the analysis of the findings from the input shuffling experiment and extending
the lookback window experiment, we propose that the insufficient prediction capabilities of
current complex models can be primarily attributed to two key factors: (1) their limited abil-
ity to utilize the sequential information inherent in the time series effectively, and (2) their
susceptibility to overfitting and noise interference.
6.4.3 Assessment of trend and season information mining capability
Based on the results of multivariate and univariate time series prediction experiments, it is
apparent that models incorporating the method of time series decomposition tend to exhibit
superior prediction accuracy. For models that employ time series decomposition methods,
the trend term and the season term are the temporal terms they most aspire to extract. To
further explore the performance of the aforementioned models in time series decomposition,
trend, and seasonal term extraction, and overall prediction capabilities, we will train and test
these models on an artificial dataset with the explicit trend and seasonal terms. Using this
dataset, we can clearly observe the differences between the model outputs for the trend and
seasonal terms and their corresponding true values. Next, we will provide an overview of
the artificial dataset, including the process of generating the trend and seasonal terms.
Artificial Dataset: The artificial dataset consists of two terms: the trend term and the sea-
son term. Specifically, the trend term at the tth time step in each instance follows the equation
b(t)= 1 , while the season term at the tth time step in each instance follows the equation
eβ0(t
−
β1)
s(t)=A 1 cos(2πf 1 t)+A 2 cos(2πf 2 t). The parameters used for generating the dataset are
as follows: β 0 = − 0.2, β 1 =L, A 1 =A 2 =0.15, f 1 = 1 1 0 , and f 2 = 1 1 3 . In this experiment,
the artificial dataset contains 16,847 instances. During the training phase, the instances in the
training set are represented as x i =[b(1)+s(1+i),...,b(L+O)+s(L+O+i)]+ξ i,
where ξ i represents Gaussian-distributed noise with a mean of 0 and a standard deviation
of 0.05.
In this experiment, we set both the input and output lengths of the time series to 96. The
dataset was partitioned into training, validation, and test sets following a ratio of 6:2:2, uti-
lizing a batch size of 16. The reported outcomes are derived from the mean results of five
distinct and independent experiments.
Table 9 presents the predictions of different models incorporating time-series decom-
position on the artificial dataset. Figure 18 shows the models’ prediction accuracy for the
trend terms. Among the models evaluated for trend term prediction on the artificial dataset,
Fedformer, TDformer, and DLinear demonstrate superior performance. Fedformer is the
best, which shows improvements of 3.14% and 6.18% in MAE and MSE for trend term pre-
diction compared to TDformer, and 26.24% and 48.43% compared to DLinear. Fedformer,
TDformer, and DLinear all use simple trend information extraction methods, such as mean
1 3

23 Page 52 of 67 X. Song et al.
filtering and linear layers. This indicates that simple techniques can effectively extract trend
information, while complex methods like N-BEATS and ETSformer may suffer from a cer-
tain degree of overfitting in accurately predicting trend terms.
The predictions for the season term are depicted in Fig. 19, and Table 9 provides an over-
view of the season term predictions for each model. Based on the aforementioned findings, it
becomes apparent that the top-performing models for season-term prediction are Fedformer,
TDformer, and ETSformer. Notably, all of these models employ frequency domain-based
approaches to process season terms. Among the three methods, Fedformer has the strongest
ability to extract seasonal terms. Compared to TDformer, Fedformer improves the MAE and
MSE for season-term prediction by 26.65% and 43.07%, respectively. Similarly, compared
to ETSformer, Fedformer shows improvements of 29.17% in MAE and 44.17% in MSE for
season-term prediction.
Based on the aforementioned results of season term prediction, it becomes evident that
models that utilize frequency domain-based methods outperform other models that rely on
time domain-based methods. Therefore, it can be concluded that processing the Fourier
components in the frequency domain is an effective approach for capturing the inherent
periodic information present in the time series.
By integrating the predictions of both trend and season terms from the models, we notice
a positive correlation between their predictive capabilities. Specifically, a more accurate
prediction of season terms aligns with a better prediction of trend terms across the majority
of models. We propose that this phenomenon can be attributed to most models’ iterative
decomposition of trend and season terms. The prediction accuracy of one term directly
influences the subsequent decomposition of the remaining terms.
6.4.4 Assessing the efficacy of attention modules
Drawing upon the outcomes of multivariate and univariate time series prediction experi-
ments, it becomes evident that most Transformer-based models demonstrate superior
prediction performance compared to other models. The main difference between Trans-
former-based models lies in their internal Attention modules. Therefore, in the following we
will analyze these Attention modules to explore their contributions to the models’ overall
predictive capabilities and evaluate their complexities.
To examine the impact of different Attention modules on the model’s prediction capabil-
ity, we employ the Transformer as the baseline framework in our experiments. Subsequently,
we replace the Attention modules with the test objects to facilitate a comparative analysis
of their effects on prediction accuracy. Additionally, we fine-tune the hidden layer dimen-
sions of the test objects to ensure consistent space complexity. This adjustment is necessary
because LogSparse Attention, LSH Attention, and ProSparse Attention have been optimized
in terms of space complexity compared to the vanilla Attention modules. To ensure a fair
comparison, we aligned the space complexity of the test subjects to a similar scale.
We keep a consistent batch size of 8 and set the model with an input time series length
L=96 and a predicted time series length O =96. The rest of the experimental config-
urations align with those utilized in the multivariate time series prediction experiments
described in Sect. 6.4.1.
1 3

Deep learning-based time series forecasting Page 53 of 67 23
Table 10 demonstrates that Patch Attention in PatchTST significantly improves the predic-
tion capability of the Attention mechanism. When compared with the vanilla Attention mod-
ule, Patch Attention exhibits substantial accuracy enhancements on the ETTh1 dataset, with
improvements of 17.95% and 30.06% in MAE and MSE, respectively. Additionally, Patch
Attention achieves an impressive 85.27% improvement in MSE on the Exchange dataset.
These results indicate that aggregating short-term time steps collectively significantly enhances
the capacity of the attention mechanism to capture temporal information within a time series.
Furthermore, our experiments in Sect. 6.4.1 reveal the notable performance of Fedformer
and Crossformer. However, it is worth noting that their attention modules, FA and DAt-
tention, exhibit subpar performance in this specific experiment. We believe that the pri-
mary factor contributing to this outcome is the absence of space complexity limitations
on their attention modules during the experiments conducted in Sect. 6.4.1. However, the
space complexity of FA and DAttention significantly surpasses that of the vanilla Attention
module. To maintain consistency in space complexity across all experimental subjects, the
dimensions of the hidden layer in FA and DAttention are compressed to a smaller scale in
this experiment, resulting in their subpar prediction accuracies.
According to the introduction in Sect. 4, numerous models based on the Attention mech-
anism have optimized their complexity to meet the demands of long-term time series fore-
casting tasks. Consequently, we delve into the complexity of these optimized models and
examine their corresponding prediction performance.
We uniformly set the batch size to 8. All optimized models are trained on the ETTh1
dataset with an input time series length of L=96 and predicted time series lengths of
O = 48,96,336 . Following the original works (Nie et al. 2022; Zhang and Yan 2022;
{ }
Liu et al. 2021; Kitaev et al. 2020; Li et al. 2019; Zhou et al. 2021), the remaining hyper-
parameters of these models are set to their optimal values.
Next, we will analyze the performance of these models from two perspectives: time com-
plexity and space complexity. Firstly, regarding time complexity, we observe that Reformer
demonstrates superior prediction performance while maintaining a low time complexity.
This observation is illustrated in Fig. 20 and summarized in Table 11. Specifically, Reformer
exhibits the shortest test time, reducing 10.14% compared to LogTrans, the model with the
second-best test time. Additionally, on the ETTh1 dataset, Reformer showcases significant
improvements in MAE by 14.03% and MSE by 18.42% compared to LogTrans. One of
the distinctive features of Reformer is incorporating the Locality-Sensitive Hashing (LSH)
Attention mechanism. This mechanism partitions the time steps into groups using a hash
function, limiting the computation of similarity relationships to time steps within the same
group. As a result, the complexity of the Attention mechanism is effectively reduced.
When considering space complexity, our analysis reveals that models utilizing the patch
slicing method, such as PatchTST and Pyraformer, demonstrate distinct advantages while
maintaining high prediction accuracy. In particular, these models demonstrate even more
pronounced benefits in space complexity when dealing with long-term time series. In
Fig. 21 and Table 12, we observe that for a prediction length of 336, PatchTST exhibits a
memory occupation that is 10.93% lower than that of LogTrans. Additionally, PatchTST
showcases significant improvements in MAE by 28.83% and in MSE by 42.09% compared
1 3

23 Page 54 of 67 X. Song et al.
Fig. 20 Inference time. The vertical axis represents the inference time of different models for the whole
test dataset. We report the mean inference time for each model across three scenarios with prediction
lengths of 48, 96, 336
Fig. 21 Maximum memory occupation during training. The horizontal axis represents the prediction
length, and the vertical axis represents the maximum memory occupation
to LogTrans on the ETTh1 dataset. Similarly, for a prediction length of 336, Pyraformer
exhibits a memory occupation that is 3.00% lower than LogTrans. Moreover, Pyraformer
surpasses LogTrans in prediction accuracy with a 4.10% improvement in MAE and a 4.27%
improvement in MSE on the ETTh1 dataset.
1 3

Deep learning-based time series forecasting Page 55 of 67 23
Through an analysis of the prediction ability and complexity of the Attention module, we
have observed that the patch-slicing approach effectively enhances the module’s prediction
capability. Additionally, this approach significantly reduces the complexity of the Attention
module by processing shorter lengths of time series data. The benefits of complexity opti-
mization through patch slicing become more apparent as the length of the input time series
increases. While other sparse methods may also optimize the module’s complexity, they often
result in information loss, potentially impacting the prediction performance to some extent.
7 Conclusion and future directions
In this paper, we comprehensively examine the principal models used for time series fore-
casting during the 10-year period from 2014 to 2024. Our focus is on analyzing the underly-
ing processing logic employed by these models. Specifically, we investigate the correlation
relationships between time steps and the interdependencies among time series variables.
We then present approaches explicitly tailored for long-term time series forecasting tasks.
Furthermore, we provide a concise overview of commonly employed loss functions in time
series forecasting. In the section dedicated to comparative experiments, we conduct thor-
ough investigations into the performance of the principal models for both univariate and
multivariate time series prediction tasks. We meticulously explore and analyze the chal-
lenges of overfitting and noise interference in existing complex models. Throughout our
investigation, we identify the distinct advantages of employing simple methods for trend
term prediction and employing methods based on frequency domain for season term pre-
diction. Moreover, we validate the effectiveness of the patch-slicing method applied to the
Attention mechanism by assessing its performance in terms of prediction accuracy and
complexity. Drawing on a comprehensive analysis of existing research findings, we pro-
pose potential research directions within the field of time series prediction. These directions
encompass the following areas:
Mining Dependencies among Time Steps: Existing models have utilized time series
decomposition methods to extract temporal information such as trends and seasonal pat-
terns, but these models still face limitations in effectively mining this information. Explor-
ing seasonal information in the frequency domain remains a promising direction for future
research. Additionally, capturing time-scale information, non-stationary patterns, and other
relevant time series information is becoming increasingly important.
Mining Relationships among Time-Series Variables: In datasets related to traffic or
weather, there is an inherent correlation among time-series signals from different sensors.
Therefore, exploring the correlation information between time-series variables is crucial for
such datasets. However, existing models have paid less attention to extracting relationships
among time-series variables. Effectively utilizing these relationships remains an important
research direction.
Complexity Optimization of Models for Long-term Time-Series Prediction: As the length
of the predicted sequence increases, the computational cost of models becomes more bur-
densome. This issue is particularly prominent in Transformer-based models. Although some
algorithms have explored complexity optimization for the Attention mechanism, they often
face the challenge of information loss. Therefore, optimizing the computational cost of the
1 3

23 Page 56 of 67 X. Song et al.
Attention mechanism without sacrificing prediction accuracy remains a key area for further
exploration and research.
Investigation of Overfitting in Complex Models for Time-Series Prediction: Relevant
experiments in this paper indicate that existing complex models often suffer from overfit-
ting and noise interference, leading to prediction performance that is sometimes inferior
to simpler models. Therefore, mitigating overfitting and reducing the impact of noise and
outliers remain important research directions.
Exploring Flexible Prediction Models: Current time series prediction models are often
constrained by the fixed length of input and output sequences, meaning they can only be
used for predetermined prediction lengths. If the prediction length or position changes, these
models must be redesigned and retrained. There is a critical need to develop time series
prediction models that can adapt to flexible prediction scenarios, accommodating changes in
prediction length and position without requiring extensive redesign or retraining.
Addressing the non-stationarity of time series: Although deep learning-based models
do not require input sequences to be stationary, the non-stationarity of time series, par-
ticularly the differences in statistical characteristics between the training and test sets, can
often impact the model’s predictive accuracy. Therefore, exploring and modeling changes
in the statistical properties of time series is a crucial research direction that can significantly
enhance predictive accuracy. Research in this area is still in its early stages.
Probabilistic Forecasting: Probabilistic forecasting (Gneiting et al. 2007; Salinas et al.
2020), which involves estimating the future probability distribution of a time series based
on its past behavior, is a key area for optimizing predictive models. This approach not only
improves the robustness and interpretability of models but also equips them with capabili-
ties for risk assessment and management, which are essential in many real-world applica-
tions. Currently, deep learning models for probabilistic forecasting face several challenges,
including the development of more effective loss functions, improved evaluation metrics,
and novel model architectures tailored for random processes and probability estimation.
Additional information and experimental results
In this section, we provide additional information and experimental results that support the
main body of the paper. Section A.1 presents the complete results of the multivariate and
univariate time series forecasting experiments.
Results of multivariate and univariate time series forecasting
experiments
1 3

Deep learning-based time series forecasting Page 57 of 67 23
Table 13 Multivariate time series forecasting results
Model Data ETTh1 Exchange ILI Traffic Electricity
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE
Model Data ETTh1 Exchange ILI Traffic Electricity
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE
ARIMA Short 1.2874 2.3800 1.1574 3.5088 1.0836 2.5038 0.7340 0.8655 1.0963 1.8875
Regular 1.4327 2.8096 1.3296 3.4915 1.0283 2.3477 0.7089 0.8121 0.9924 1.5787
Long 1.0144 1.4551 1.1372 2.2342 0.9696 1.8138 0.7212 0.9080 0.9707 1.5114
CNN_1D Short 0.5794 0.6096 0.7574 0.7717 1.1983 2.7567 0.7619 1.1303 0.3990 0.3258
Regular 0.6664 0.8049 0.8277 0.9209 1.2479 2.9318 0.7632 1.1347 0.5737 0.5905
Long 0.8382 1.1594 0.8659 1.0250 1.3800 3.3879 0.7487 1.0399 – –
TCN Short 0.6655 0.8862 0.1834 0.0617 1.1992 2.9021 0.5308 0.7229 0.3129 0.2719
Regular 0.4940 0.4853 0.2512 0.1067 1.3409 3.3631 0.4181 0.5460 0.3670 0.3415
Long 0.6410 0.6933 0.3238 0.1769 1.2214 2.8402 0.5130 0.7605 0.3648 0.2775
DeepAR Short 0.9030 1.3482 0.8777 1.1188 1.2294 2.8305 0.8119 1.1921 0.8560 1.0811
Regular 0.9240 1.3994 0.8975 1.2054 1.2870 3.0435 0.9628 1.6597 0.8409 1.0337
Long 1.1843 2.2798 1.1901 2.2022 1.3712 3.3984 0.8752 1.3683 – –
GRU Short 0.7803 1.0360 0.7621 0.0884 1.1508 2.4973 1.2360 2.0568 0.7838 0.8927
Regular 0.7493 0.9711 0.7812 0.8324 1.1799 2.0048 1.2360 2.0568 0.7829 0.8914
Long 0.7687 1.0085 0.7398 0.7430 1.2922 3.0311 0.7532 1.0687 0.7838 0.8884
LSTnet Short 0.8130 1.1303 0.3699 0.2598 1.1298 2.0822 0.6480 0.8468 0.6181 0.6353
Regular 0.7601 0.9960 0.4955 0.4042 1.2103 2.7753 0.6793 0.9148 0.6986 0.7821
Long 0.7644 0.9953 0.7643 0.8241 1.2546 2.7236 – – – –
Trans- Short 0.4745 0.4491 0.2807 0.1393 1.0202 2.1587 0.3148 0.3415 0.3969 0.3283
former Regular 0.5174 0.5291 0.3404 0.1804 1.1004 2.3836 0.3896 0.5322 0.3996 0.3080
Long 0.6636 0.8045 0.9066 1.2028 1.2277 2.8575 0.7488 1.0401 0.7871 1.0231
LogTrans Short 0.5362 0.5482 0.3736 0.2137 0.7762 1.5743 0.5296 0.7651 0.3795 0.2930
Regular 0.6392 0.7138 0.3949 0.2508 0.7972 1.6156 0.3617 0.4842 0.4052 0.3248
Long 0.8206 1.1379 0.7025 0.7366 0.8755 1.7925 0.3490 0.4619 0.4057 0.3242
Reformer Short 0.4986 0.4984 0.6313 0.5838 1.1229 2.4342 0.3855 0.4504 0.4408 0.3855
Regular 0.5646 0.6062 0.8194 0.9184 1.2586 2.9970 0.7644 1.1385 0.5078 0.4575
Long 0.7690 1.0775 0.9664 1.2704 1.4413 3.7349 0.7488 1.0402 0.8196 1.0802
Informer Short 0.5023 0.5197 0.3635 0.2122 0.8486 1.6803 0.3533 0.3963 0.4709 0.4322
Regular 0.6482 0.8527 0.4379 0.3113 0.9692 2.1427 0.5002 0.7643 0.4840 0.4424
Long 0.6687 0.8390 0.6804 0.6786 1.0854 2.5005 0.7548 1.1833 0.7731 1.0135
Auto- Short 0.5041 0.4961 0.1812 0.0605 0.7902 1.3502 0.3175 0.3744 0.3335 0.1922
former Regular 0.4970 0.4796 0.2177 0.0886 0.8397 1.4801 0.3419 0.4202 0.3089 0.2016
Long 0.5766 0.6128 0.3822 0.2579 0.8438 1,5455 0.3393 0.4095 0.3577 0.2609
Fedformer Short 0.4566 0.4189 0.1815 0.0607 0.6483 0.9915 0.3169 0.3693 0.2973 0.1877
Regular 0.4935 0.4754 0.2174 0.0877 0.8024 1.3779 0.3172 0.3699 0.3009 0.1924
Long 0.5714 0.5979 0.3694 0.2429 0.7911 1.3501 0.3234 0.3876 0.4646 0.3942
ETS- Short 0.5026 0.5423 0.1159 0.0274 0.8059 1.3679 0.4652 0.6078 0.3185 0.2163
former Regular 0.5414 0.6074 0.1693 0.0557 0.9788 1.9403 0.4721 0.6234 0.3370 0.2430
Long 0.6140 0.7113 0.3211 0.1937 1.0026 1.9683 0.4800 0.6799 0.3642 0.2824
TDformer Short 0.5810 0.6334 0.5819 0.5126 1.1809 2.6896 0.3602 0.3676 0.4169 0.3459
Regular 0.5963 0.6530 0.7822 0.8633 1.2581 2.9438 0.3677 0.5183 0.4174 0.3463
Long 0.7826 1.0615 0.8391 1.0206 1.3461 3.3141 0.3816 0.5569 0.4575 0.4160
AST Short 0.4410 0.4457 0.5003 0.3945 1.0302 2.3503 0.3106 0.3933 0.3696 0.2816
Regular 0.4998 0.5324 0.6505 0.6381 1.1992 2.9159 0.3180 0.4133 0.3706 0.2844
Long 0.6059 0.7076 0.8950 1.1737 1.2093 2.9306 0.3572 0.4899 0.3892 0.3113
1 3

23 Page 58 of 67 X. Song et al.
T able 13 (continued)
Model Data ETTh1 Exchange ILI Traffic Electricity
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE
Aliformer Short 0.7668 1.0024 0.5696 0.5009 1.1775 2.6960 0.7502 1.0473 0.8223 0.9717
Regular 0.8467 1.2102 0.8112 0.8993 1.2329 2.8906 0.7632 1.1348 0.8250 0.9845
Long 0.7632 0.9963 1.0791 1.5914 1.4442 3.7724 0.7487 1.0398 0.8221 0.9674
NS- Short 0.4306 0.4197 0.1199 0.0285 0.5493 0.7300 0.2910 0.3491 0.2646 0.1637
Trans- Regular 0.4812 0.4946 0.1695 0.0565 0.7099 1.1508 0.3046 0.3718 0.2771 0.1784
former
Long 0.6070 0.7074 0.3403 0.2142 0.7579 1.3199 0.3202 0.4008 0.3024 0.2052
Cross- Short 0.4132 0.3788 0.2005 0.0723 0.9512 2.0541 0.2453 0.3085 0.2342 0.1458
former Regular 0.4522 0.4393 0.2575 0.1118 1.0898 2.4253 0.2718 0.3452 0.2485 0.1647
Long 0.6319 0.8007 0.5546 0.5053 1.1988 2.8067 – – 0.2882 0.2022
DLinear Short 0.3979 0.3663 0.1109 0.0259 0.6440 0.9567 0.3738 0.5417 0.2676 0.2004
Regular 0.4360 0.4229 0.1775 0.0570 0.7699 1.2162 0.3478 0.5075 0.2741 0.1992
Long 0.5052 0.5197 0.3117 0.1648 0.7994 1.2452 0.3292 0.4681 0.2916 0.2095
Scal- Short 0.5480 0.6227 0.1858 0.0635 0.6766 1.0450 0.3054 0.3572 0.3390 0.2359
eformer Regular 0.4643 0.4324 0.1761 0.0600 0.7967 1.4051 0.3159 0.3723 0.3515 0.2607
Long 0.6311 0.7666 0.3905 0.2646 0.8967 1.6122 0.3387 0.4056 0.3749 0.2839
Pyrafor- Short 0.4799 0.4682 0.3796 0.2333 0.8096 1.6223 0.4478 0.5959 0.3821 0.2972
mer Regular 0.5358 0.5705 0.5940 0.5645 1.0740 1.9305 0.4984 0.6638 0.4037 0.3323
Long 0.6907 0.8723 0.7570 0.8616 1.0720 2.3328 – – 0.4242 0.3640
PatchTST Short 0.4008 0.3674 0.1147 0.0283 0.4584 0.5307 0.2654 0.3379 0.2574 0.1860
Regular 0.4401 0.4253 0.1609 0.0520 0.6180 0.9902 0.2755 0.3615 0.2631 0.1891
Long 0.5215 0.5509 0.3308 0.2087 0.7424 1.1373 0.2835 0.3857 0.2861 0.2092
Triformer Short 0.7668 1.0024 0.1678 0.0510 1.0915 2.4694 – – – –
Regular 0.4679 0.4429 0.1759 0.0560 1.1890 2.7092 – – – –
Long 0.5562 0.5877 0.5116 0.4676 1.2457 2.9084 – – – –
TFT Short 0.4594 0.4663 0.1995 0.0694 1.3075 3.3835 – – 0.3568 0.2721
Regular 0.5515 0.5552 0.2317 0.0928 1.2891 3.1048 – – 0.4493 0.4010
Long 0.5301 0.5571 0.6355 0.6263 1.5055 4.1189 – – – –
SSDNet Short 0.8618 1.2990 0.4704 0.3884 1.3896 3.3878 – – – –
Regular 0.7075 0.8740 0.3986 0.2668 1.4744 3.7407 – – – –
Long – – 0.6555 0.6487 1.7026 4.7365 – – – –
Auto- Short 0.7606 0.9954 0.1854 0.0633 1.2128 2.8800 0.7585 1.1517 0.8219 0.9705
encoder Regular 0.5279 0.5809 0.3018 0.1569 1.2891 3.2390 0.7601 1.1585 0.8221 0.9707
Long 0.7645 0.9986 1.0101 1.4107 1.4179 3.7566 0.7488 1.0398 0.8227 0.9695
SAE Short 0.4210 0.3778 0.8057 0.8961 1.1582 2.5776 0.3417 0.4537 0.3831 0.2984
Regular 0.7381 0.9107 1.0898 1.6129 1.2364 2.9496 0.3521 0.4877 0.4411 0.4289
Long 0.7640 1.0732 1.1855 1.9782 1.3723 3.5140 0.7485 1.0401 0.8189 1.0621
N-BEATS Short 0.4579 0.4353 0.1151 0.0269 0.9474 1.8391 0.3886 0.6086 0.3760 0.2855
Regular 0.6128 0.7949 0.1629 0.0581 1.1330 2.5371 0.6862 1.0418 0.6903 0.8176
Long 0.6682 0.8908 0.3290 0.1797 1.3070 3.1641 0.7400 1.1278 0.7374 0.9044
The best results are highlighted in bold and the second best results are highlighted with a underline.. "–"
indicates out of memory. ’Short’, ’Regular’, ’Long’ denotes the output length O for short-term, regular-
term and long-term time series prediction
1 3

Deep learning-based time series forecasting Page 59 of 67 23
Table 14 Univariate time series forecasting results
Model Data ETTh1 Exchange ILI Traffic Electricity
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE
ARIMA Short 0.5341 0.2904 0.8298 0.6908 2.8446 8.1104 1.5089 2.9879 0.8334 0.9120
Regular 0.6769 0.4613 1.1036 1.2307 2.6658 7.1389 1.3781 2.4447 0.7523 0.7447
Long 0.7517 0.5809 1.2046 1.4630 2.0703 4.7428 1.2276 2.1735 0.7134 0.6477
CNN-1D Short 0.5670 0.4782 0.3974 0.2305 0.9066 1.1410 0.8560 1.0486 0.4783 0.3992
Regular 0.5670 0.4779 0.3071 0.1470 1.6404 3.1585 0.8193 0.9720 0.5042 0.4420
Long 0.5506 0.4552 0.6736 0.7026 1.3437 3.3111 0.8555 1.0478 0.5618 0.5150
TCN Short 0.3322 0.2075 0.3275 0.1818 1.4640 2.6350 0.4934 0.4646 0.8229 1.1922
Regular 0.3619 0.2383 0.4640 0.3343 1.5244 2.8274 0.6185 0.6433 0.7375 0.9382
Long 0.3683 0.2410 0.6464 0.6255 1.5310 2.7988 0.4309 0.3664 0.8169 1.0796
DeepAR Short 0.4840 0.3610 0.9770 1.3248 1.4786 3.6056 1.2122 2.2182 1.1570 1.1570
Regular 0.6246 0.5837 0.9870 1.3568 1.4792 2.7966 1.2481 2.3466 1.1761 2.2091
Long 0.7266 0.8006 1.0411 1.5027 1.8888 4.1431 – – – –
GRU Short 0.7675 0.7355 0.8287 1.0144 1.3457 2.3184 1.0187 1.4046 0.8059 1.0043
Regular 0.8253 1.0101 0.8253 1.0101 1.3554 2.3010 1.0186 1.4047 0.8048 1.0039
Long 0.8268 1.0316 0.8268 1.0316 1.3623 2.2733 1.0218 1.4094 0.8020 1.0042
LSTnet Short 0.6540 0.5656 0.5887 0.4949 1.0897 1.5923 0.7020 0.7594 0.6927 0.6999
Regular 0.6546 0.5675 0.6168 0.5340 1.2049 1.8884 0.7516 0.8135 0.7510 0.8845
Long 0.6601 0.5914 0.9144 1.2287 1.2914 2.0774 – – – –
Trans- Short 0.3489 0.2109 0.3423 0.1711 0.7755 0.8995 0.7969 0.9045 0.3996 0.2803
former Regular 0.3871 0.2612 0.3652 0.2087 0.8634 1.0702 0.7809 0.8834 0.4730 0.3934
Long 0.5154 0.4288 0.5294 0.3849 0.9816 1.2789 0.8414 1.0310 0.4647 0.3873
LogTrans Short 0.3415 0.1833 0.3250 0.1686 0.8294 0.8792 1.1643 1.8174 0.4389 0.3623
Regular 0.3571 0.2064 0.3857 0.2251 0.8593 0.9287 1.0159 1.4864 0.4432 0.3545
Long 0.4776 0.3544 0.4997 0.3649 0.8999 0.9355 0.8352 1.0665 0.4696 0.4115
Reformer Short 0.4624 0.3293 0.5477 0.4349 0.9098 1.2002 0.8658 1.0754 0.5157 0.4667
Regular 0.5138 0.4088 0.5974 0.5264 1.1512 1.8010 0.9858 1.3908 0.5350 0.4957
Long 0.5397 0.4395 0.7098 0.7446 1.3585 2.2942 0.9435 1.3019 0.5228 0.4851
Informer Short 0.3855 0.2463 0.5156 0.4046 0.9464 1.2762 1.2931 2.3961 0.5526 0.5625
Regular 0.4711 0.3706 0.6412 0.5808 1.0865 1.5350 1.0285 1.5467 0.5740 0.5632
Long 0.5258 0.4454 0.7829 0.8706 1.2137 1.7989 0.8971 1.2184 0.7572 0.9080
Auto- Short 0.3437 0.2138 0.1946 0.0638 0.4348 0.3105 0.4294 0.2901 0.4493 0.3648
former Regular 0.3634 0.2317 0.2645 0.1154 0.5409 0.4231 0.4619 0.3388 0.4126 0.2988
Long 0.4041 0.2819 0.4783 0.3768 0.6079 0.4947 0.4274 0.2969 0.5767 0.5460
Fedformer Short 0.3325 0.1992 0.2194 0.0798 0.4053 0.2466 0.4210 0.2826 0.3732 0.2480
Regular 0.3555 0.2220 0.2682 0.1212 0.4493 0.2987 0.4261 0.2891 0.3250 0.1967
Long 0.4001 0.2777 0.4739 0.3685 0.5595 0.4466 0.4281 0.2938 0.6163 0.6571
ETS- Short 0.3329 0.1994 0.3423 0.1711 0.4790 0.3744 0.5593 0.4885 0.5673 0.5584
former Regular 0.3604 0.2298 0.2178 0.0735 0.5411 0.4164 0.5672 0.5067 0.6315 0.6620
Long 0.4194 0.3005 0.3925 0.2265 0.6302 0.5230 0.5756 0.5355 0.6709 0.7967
TDformer Short 0.4272 0.3113 0.9326 1.2894 2.0571 4.9538 0.4244 0.3633 0.4163 0.3130
Regular 0.4779 0.3727 1.1635 1.7472 1.1753 2.6595 0.4572 0.4127 0.4716 0.3981
Long 0.4715 0.3780 1.2804 2.1319 2.1227 5.1123 0.4590 0.4144 0.4954 0.4201
AST Short 0.5517 0.6820 0.4682 0.3521 1.1750 3.0143 0.3203 0.4072 0.3703 0.2837
Regular 0.5598 0.6656 0.8395 0.9553 1.1257 2.5269 0.3291 0.4288 0.3786 0.2925
Long 0.6219 0.7784 0.9843 1.3628 1.3748 3.8622 0.3398 0.4497 0.3952 0.3203
1 3

23 Page 60 of 67 X. Song et al.
T able 14 (continued)
Model Data ETTh1 Exchange ILI Traffic Electricity
Metric MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE
Aliformer Short 1.0248 1.2065 0.4364 0.2761 1.4713 2.6747 0.9729 1.1016 0.8180 1.0663
Regular 0.8248 1.1298 0.5353 0.3708 1.5087 2.7804 0.9811 1.1930 0.8166 1.0659
Long 0.9166 0.9959 1.3951 2.3686 1.4399 3.7476 0.9827 1.1928 0.8190 1.0657
NS- Short 0.3163 0.1821 0.1541 0.0404 0.3869 0.2530 0.4654 0.3691 0.3133 0.1869
Trans- Regular 0.3471 0.2152 0.2235 0.0911 0.4107 0.2840 0.8804 1.1424 0.3189 0.1984
former
Long 0.5269 0.4747 0.4828 0.3880 0.4165 0.2569 0.9661 1.2290 0.3099 0.1743
Cross- Short 0.3146 0.1829 0.2728 0.1187 1.1821 2.1848 0.3915 0.2846 0.3033 0.2277
former Regular 0.3404 0.2120 0.3820 0.2287 1.1480 1.5548 0.3784 0.2790 0.2796 0.1818
Long 0.4192 0.2960 0.8162 1.0097 1.1606 1.5138 – – 0.3350 0.2443
Dlinear Short 0.2987 0.1729 0.1413 0.0339 0.6970 0.7121 0.4687 0.4177 0.6975 0.9390
Regular 0.3214 0.1952 0.1953 0.0657 0.9373 1.1032 0.4398 0.3811 0.5960 0.7090
Long 0.3712 0.2455 0.3847 0.2209 0.9340 1.0252 0.4201 0.3443 0.4864 0.4893
Scal- Short 0.3003 0.1679 0.1674 0.0471 0.4511 0.3643 0.3051 0.1912 0.4147 0.3031
eformer Regular 0.3131 0.1734 0.2249 0.0862 0.5383 0.4665 0.3163 0.1979 0.4337 0.3384
Long 0.4234 0.3099 0.4641 0.3559 0.5628 0.4290 0.2908 0.1861 0.4706 0.4004
Pyrafor- Short 0.4021 0.2615 0.3448 0.1914 1.1677 1.7479 0.4151 0.3509 0.4523 0.3564
mer Regular 0.5803 0.5474 0.3467 0.1873 1.2846 2.2077 0.4145 0.3491 0.4717 0.3892
Long 0.5070 0.4283 0.6196 0.5879 1.3637 2.2317 0.4308 0.3706 0.5145 0.4510
PatchTST Short 0.3031 0.1774 0.1566 0.0425 0.2874 0.1614 0.3514 0.2488 0.5249 0.6473
Regular 0.3276 0.2021 0.2124 0.0789 0.3542 0.2233 0.3610 0.2606 0.4437 0.4893
Long 0.3693 0.2478 0.4163 0.2917 0.4604 0.3440 0.3700 0.2722 0.3770 0.3589
Triformer Short 0.3149 0.1866 0.2410 0.0935 1.7262 3.4845 – – – –
Regular 0.3334 0.2071 0.3398 0.1900 1.7423 3.4663 – – – –
Long 0.4041 0.2843 0.6297 0.7034 1.4855 2.5357 – – – –
TFT Short 0.3852 0.2125 0.5234 0.4296 1.2492 2.9732 – – 0.3568 0.2721
Regular 0.3975 0.2325 0.6230 0.5707 1.2936 3.1257 – – 0.4369 0.3828
Long 0.6813 0.7711 0.5307 0.4244 1.3590 3.3232 – – – –
SSDNet Short 0.3994 0.2447 0.5471 0.4941 1.2719 2.0677 – – – –
Regular 0.4760 0.3493 0.6099 0.5869 1.3293 2.1916 – – – –
Long – – 0.8132 1.0029 1.5207 2.7740 – – – –
Auto- Short 0.3441 0.2095 0.4243 0.2946 1.2054 1.9340 0.7613 1.1320 0.8156 1.0888
encoder Regular 0.3615 0.2281 0.5458 0.4641 1.3731 2.3999 0.9632 1.1615 0.8194 1.0719
Long 0.5640 0.4772 0.7607 0.8692 1.4058 3.6954 0.9643 1.1710 0.8179 1.0794
SAE Short 0.4854 0.3539 0.3752 0.2119 1.1519 2.4958 0.3895 0.3295 0.4836 0.4035
Regular 0.5297 0.4225 0.4577 0.3130 1.6535 3.2258 0.4312 0.3777 0.5179 0.4563
Long 0.7807 1.0845 0.7391 0.8023 1.8888 4.1431 0.4527 0.4081 0.5660 0.5481
N-BEATS Short 0.3119 0.1805 0.2950 0.1354 1.2647 1.8155 0.4647 0.3671 0.5377 0.5074
Regular 0.3660 0.2341 0.3245 0.1733 1.7303 3.4102 0.8803 1.1347 0.6250 0.6499
Long 0.4114 0.2837 0.4720 0.3880 1.5454 2.6395 0.9589 1.2246 0.6735 0.7926
The best results are highlighted in bold and the second best results are highlighted with a underline. "–"
indicates out of memory. ’Short’, ’Regular’, ’Long’ denotes the output length O for short-term, regular-
term and long-term time series prediction
1 3

Deep learning-based time series forecasting Page 61 of 67 23
Funding This work was supported by the National Natural Science Foundation of China (Grant No.
62206178 and 72301180) and the Stable Support Plan for Higher Education Institutions in Shenzhen (Project
No. 20231121221536001). The authors have no relevant financial or non-financial interests to disclose.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-
NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it.
The images or other third party material in this article are included in the article’s Creative Commons licence,
unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative
Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use,
you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit
http://creativecommons.org/licenses/by-nc-nd/4.0/.
References
Achiam J, Adler S, Agarwal S, Ahmad L, Akkaya I, Aleman FL, Almeida D, Altenschmidt J, Altman S, Anad-
kat S, et al (2023) Gpt-4 technical report. arXiv preprint arXiv:2303.08774
Al-Tahan H, Mohsenzadeh Y (2021) Clar: Contrastive learning of auditory representations. In: International
conference on artificial intelligence and statistics, pp. 2530–2538. PMLR
Amalou I, Mouhni N, Abdali A (2022) Multivariate time series prediction by RNN architectures for energy
consumption forecasting. Energy Rep 8:1084–1091
Ariyo AA, Adewumi AO, Ayo CK (2014) Stock price prediction using the arima model. In: 2014 UKSim-
AMSS 16th international conference on computer modelling and simulation, pp. 106–112. IEEE
Armstrong JS (2001) Principles of forecasting: a handbook for researchers and practitioners, vol 30. Springer,
Berlin
Asadi R, Regan AC (2020) A spatio-temporal decomposition based deep neural network for time series fore-
casting. Appl Soft Comput 87:105963
Bai S, Kolter JZ, Koltun V (2018) An empirical evaluation of generic convolutional and recurrent networks
for sequence modeling. arXiv preprint arXiv:1803.01271
Bell WR, Hillmer SC (1984) Issues involved with the seasonal adjustment of economic time series. J Bus
Econ Stat 2(4):291–320
Binkowski M, Marti G, Donnat P (2018) Autoregressive convolutional neural networks for asynchronous
time series. In: International conference on machine learning, pp. 580–589. PMLR
Cai L, Janowicz K, Mai G, Yan B, Zhu R (2020) Traffic transformer: capturing the continuity and periodicity
of time series for traffic forecasting. Trans GIS 24(3):736–755
Cao D, Wang Y, Duan J, Zhang C, Zhu X, Huang C, Tong Y, Xu B, Bai J, Tong J (2020) Spectral tem-
poral graph neural network for multivariate time-series forecasting. Adv Neural Inf Process Syst
33:17766–17778
Celeghini E, Gadella M, Olmo MA (2021) Hermite functions and Fourier series. Symmetry 13(5):853
Chakraborty K, Mehrotra K, Mohan CK, Ranka S (1992) Forecasting the behavior of multivariate time series
using neural networks. Neural Netw 5(6):961–970
Challu C, Olivares KG, Oreshkin BN, Ramirez FG, Canseco MM, Dubrawski A (2023) Nhits: Neural hier-
archical interpolation for time series forecasting. In: Proceedings of the AAAI conference on artificial
intelligence, vol. 37, pp. 6989–6997
Chen Z, Ma M, Li T, Wang H, Li C (2023) Long sequence time-series forecasting with deep learning: a
survey. Inf Fus 97:101819
Chen Y, Huang J, Xu H, Guo J, Su L (2023) Road traffic flow prediction based on dynamic spatiotemporal
graph attention network. Sci Rep 13(1):14729
Cheng D, Yang F, Xiang S, Liu J (2022) Financial time series forecasting with multi-modality graph neural
network. Pattern Recogn 121:108218
Cirstea R-G, Guo C, Yang B, Kieu T, Dong X, Pan S (2022) Triformer: Triangular, variable-specific attentions
for long sequence multivariate time series forecasting–full version. arXiv preprint arXiv:2204.13767
Cleveland RB, Cleveland WS, McRae JE, Terpenning I (1990) STL: a seasonal-trend decomposition. J Off
Stat 6(1):3–73
Contreras J, Espinola R, Nogales FJ, Conejo AJ (2003) Arima models to predict next-day electricity prices.
IEEE Trans Power Syst 18(3):1014–1020
1 3

23 Page 62 of 67 X. Song et al.
Cui Z (2016) Multi-scale convolutional neural networks for time series classification. arXiv preprint
arXiv:1603.06995
Dagum EB (2010) Time series modeling and decomposition. Statistica (Bologna) 70(4):433–457
De Livera AM, Hyndman RJ, Snyder RD (2011) Forecasting time series with complex seasonal patterns
using exponential smoothing. J Am Stat Assoc 106(496):1513–1527
Devlin J, Chang M-W, Lee K, Toutanova K (2018) Bert: Pre-training of deep bidirectional transformers for
language understanding. arXiv preprint arXiv:1810.04805
Dey R, Salem FM (2017) Gate-variants of gated recurrent unit (gru) neural networks. In: 2017 IEEE 60th
international midwest symposium on circuits and systems (MWSCAS), pp. 1597–1600. IEEE
Dinh TN, Thirunavukkarasu GS, Seyedmahmoudian M, Mekhilef S, Stojcevski A (2023) Predicting commer-
cial building energy consumption using a multivariate multilayered long-short term memory time-series
model. Appl Sci 13(13):7775
Dosovitskiy A, Beyer L, Kolesnikov A, Weissenborn D, Zhai X, Unterthiner T, Dehghani M, Minderer M,
Heigold G, Gelly S et al. (2020) An image is worth 16x16 words: Transformers for image recognition
at scale. arXiv preprint arXiv:2010.11929
Du Y, Wang J, Feng W, Pan S, Qin T, Xu R, Wang C (2021) Adarnn: Adaptive learning and forecasting of
time series. In: Proceedings of the 30th ACM international conference on information and knowledge
management, pp. 402–411
Durbin J, Koopman SJ (2012) Time series analysis by state space methods, vol 38. Oxford University Press,
Oxford
Edition F, Papoulis A, Pillai SU (2002) Probability, random variables, and stochastic processes. New York,
McGraw-Hill
Ensafi Y, Amin SH, Zhang G, Shah B (2022) Time-series forecasting of seasonal items sales using machine
learning-a comparative analysis. Int J Inf Manag Data Insights 2(1):100058
Fan C, Wang J, Gang W, Li S (2019) Assessment of deep recurrent neural network-based strategies for short-
term building energy predictions. Appl Energy 236:700–710
Fischer T, Krauss C (2018) Deep learning with long short-term memory networks for financial market predic-
tions. Eur J Oper Res 270(2):654–669
Gál V, Hámori J, Roska T, Bálya D, Borostyánkői Z, Brendel M, Lotz K, Négyessy L, Orzó L, Petrás I (2004)
Receptive field atlas and related CNN models. Int J Bifurc Chaos 14(02):551–584
Gneiting T, Balabdaoui F, Raftery AE (2007) Probabilistic forecasts, calibration and sharpness. J R Stat Soc
Ser B Stat Methodol 69(2):243–268
Goodfellow I, Pouget-Abadie J, Mirza M, Xu B, Warde-Farley D, Ozair S, Courville A, Bengio Y (2014)
Generative adversarial nets. Adv Neural Inf Process Syst. 27
Gudelek MU, Boluk SA, Ozbayoglu AM (2017) A deep learning based stock trading model with 2-D CNN
trend detection. In: 2017 IEEE symposium series on computational intelligence (SSCI), pp. 1–8. IEEE
Guo J, Lin P, Zhang L, Pan Y, Xiao Z (2023) Dynamic adaptive encoder-decoder deep learning networks for
multivariate time series forecasting of building energy consumption. Appl Energy 350:121803
Hajirahimi Z, Khashei M (2023) Hybridization of hybrid structures for time series forecasting: a review. Artif
Intell Rev 56(2):1201–1261
Hatami N, Gavet Y, Debayle J (2018) Classification of time-series images using deep convolutional neural net-
works. In: Tenth international conference on machine vision (ICMV 2017), vol. 10696, pp. 242–249. SPIE
Hewamalage H, Bergmeir C, Bandara K (2021) Recurrent neural networks for time series forecasting: cur-
rent status and future directions. Int J Forecast 37(1):388–427
He K, Zhang X, Ren S, Sun J (2016) Deep residual learning for image recognition. In: Proceedings of the
IEEE conference on computer vision and pattern recognition, pp. 770–778
Hsieh WW (2004) Nonlinear multivariate and time series analysis by neural network methods. Rev Geophys.
https://doi.org/10.1029/2002RG000112
Hu S, Xiong C (2023) High-dimensional population inflow time series forecasting via an interpretable hier-
archical transformer. Transp Res Part C Emerg Technol 146:103962
Hyndman R (2008) Forecasting with Exponential Smoothing: The State Space Approach. Springer, Berlin
Hyndman RJ, Athanasopoulos G (2018) Forecasting: principles and practice. OTexts
Hyndman RJ, Khandakar Y (2008) Automatic time series forecasting: the forecast package for R. J Stat Softw
27:1–22
Hyndman R, Koehler AB, Ord JK, Snyder RD (2008) Forecasting with exponential smoothing: the state
space approach. Springer, USA
Iwata T, Kumagai A (2020) Few-shot learning for time-series forecasting. arXiv preprint arXiv:2009.14379
Jaiswal A, Babu AR, Zadeh MZ, Banerjee D, Makedon F (2020) A survey on contrastive self-supervised
learning. Technologies 9(1):2
1 3

Deep learning-based time series forecasting Page 63 of 67 23
Jiang S, Yu Z-G, Anh VV, Zhou Y (2021) Long-and short-term time series forecasting of air quality by a
multi-scale framework. Environ Pollut 271:116381
Jin M, Zheng Y, Li Y-F, Chen S, Yang B, Pan S (2022) Multivariate time series forecasting with dynamic
graph neural odes. IEEE Trans Knowl Data Eng 35:9168
Jin M, Wen Q, Liang Y, Zhang C, Xue S, Wang X, Zhang J, Wang Y, Chen H, Li X et al. (2023) Large models
for time series and spatio-temporal data: a survey and outlook. arXiv preprint arXiv:2310.10196
Kim T, Kim J, Tae Y, Park C, Choi J-H, Choo J (2021) Reversible instance normalization for accurate time-
series forecasting against distribution shift. In: International conference on learning representations
Kitaev N, Kaiser Ł, Levskaya A (2020) Reformer: The efficient transformer. arXiv preprint arXiv:2001.04451
Krizhevsky A, Sutskever I, Hinton GE (2017) Imagenet classification with deep convolutional neural net-
works. Commun ACM 60(6):84–90
Lacasa L, Nicosia V, Latora V (2015) Network structure of multivariate time series. Sci Rep 5(1):15508
Lai G, Chang W-C, Yang Y, Liu H (2018) Modeling long-and short-term temporal patterns with deep neural
networks. In: The 41st international ACM SIGIR conference on research & development in information
retrieval, pp. 95–104
Le P, Zuidema W (2016) Quantifying the vanishing gradient and long distance dependency problem in recur-
sive neural networks and recursive lstms. arXiv preprint arXiv:1603.00423
Lee S, Hong J, Liu L, Choi W (2024) TS-Fastformer: fast transformer for time-series forecasting. ACM Trans
Intell SystTechnol 15(2):1–20
Li S, Jin X, Xuan Y, Zhou X, Chen W, Wang Y-X, Yan X (2019) Enhancing the locality and breaking the
memory bottleneck of transformer on time series forecasting. Adv Neural Inf Process Syst. 32
Liang Y, Liu Y, Wang X, Zhao Z (2024) Exploring large language models for human mobility prediction
under public events. Comput Environ Urban Syst 112:102153
Liao R, Xiong Y, Fetaya E, Zhang L, Yoon K, Pitkow X, Urtasun R, Zemel R (2018) Reviving and improving
recurrent back-propagation. In: International conference on machine learning, pp. 3082–3091. PMLR
Lim B, Arık SÖ, Loeff N, Pfister T (2021) Temporal fusion transformers for interpretable multi-horizon time
series forecasting. Int J Forecast 37(4):1748–1764
Li Z, Qi S, Li Y, Xu Z (2023) Revisiting long-term time series forecasting: An investigation on linear map-
ping. arXiv preprint arXiv:2305.10721
Lin Y, Koprinska I, Rana M (2021) SsdNet: State space decomposition neural network for time series fore-
casting. In: 2021 IEEE International conference on data mining (ICDM), pp. 370–378. IEEE
Lin H, Gharehbaghi A, Zhang Q, Band SS, Pai HT, Chau K-W, Mosavi A (2022) Time series-based ground-
water level forecasting using gated recurrent unit deep neural networks. Eng Appl Comput Fluid Mech
16(1):1655–1672
Liu Z, Yang X (2022) Cross validation for uncertain autoregressive model. Commun Stat Simul Comput
51(8):4715–4726
Liu C-L, Hsaio W-H, Tu Y-C (2018) Time series classification with multivariate convolutional neural net-
work. IEEE Trans Industr Electron 66(6):4788–4797
Liu Z, Lin Y, Cao Y, Hu H, Wei Y, Zhang Z, Lin S, Guo B (2021) Swin transformer: Hierarchical vision trans-
former using shifted windows. In: Proceedings of the IEEE/CVF international conference on computer
vision, pp. 10012–10022
Liu S, Yu H, Liao C, Li J, Li W, Liu AX, Dustdar S (2021) Pyraformer: Low-complexity pyramidal atten-
tion for long-range time series modeling and forecasting. In: International conference on learning
representations
Liu Y, Wu H, Wang J, Long M (2022) Non-stationary transformers: exploring the stationarity in time series
forecasting. Adv Neural Inf Process Syst 35:9881–9893
Liu Y, Hu T, Zhang H, Wu H, Wang S, Ma L, Long M (2023) itransformer: Inverted transformers are effective
for time series forecasting. arXiv preprint arXiv:2310.06625
Liu Z, Cheng M, Li Z, Huang Z, Liu Q, Xie Y, Chen E (2024) Adaptive normalization for non-stationary time
series forecasting: A temporal slice perspective. Adv Neural Inf Process Syst. 36
Lu W, Li J, Li Y, Sun A, Wang J (2020) A CNN-LSTM-based model to forecast stock prices. Complexity
2020:1–10
Luo W, Li Y, Urtasun R, Zemel R (2016) Understanding the effective receptive field in deep convolutional
neural networks. Adv Neural Inf Process Syst. 29
Lv Y, Duan Y, Kang W, Li Z, Wang F-Y (2014) Traffic flow prediction with big data: a deep learning approach.
IEEE Trans Intell Transp Syst 16(2):865–873
Lyu H, Sha N, Qin S, Yan M, Xie Y, Wang R (2019) Advances in neural information processing systems. Adv
Neural Inf Process Syst. 32
Ma M, Xie P, Teng F, Wang B, Ji S, Zhang J, Li T (2023) Histgnn: Hierarchical spatio-temporal graph neural
network for weather forecasting. Inf Sci 648:119580
1 3

23 Page 64 of 67 X. Song et al.
Maggiolo M, Spanakis G (2019) Autoregressive convolutional recurrent neural network for univariate and
multivariate time series prediction. arXiv preprint arXiv:1903.02540
Malenica I, Phillips RV, Pirracchio R, Chambaz A, Hubbard A, Laan MJ (2021) Personalized online machine
learning. arXiv preprint arXiv:2109.10452
Mao J, Middleton SE, Niranjan M (2023) Prompt position really matters in few-shot and zero-shot NLU
tasks. arXiv preprint arXiv:2305.14493
Markova M (2022) Convolutional neural networks for forex time series forecasting. In: AIP conference pro-
ceedings, vol. 2459. AIP Publishing
Mathieu M, Henaff M, LeCun Y (2013) Fast training of convolutional networks through ffts. arXiv preprint
arXiv:1312.5851
Miller JA, Aldosari M, Saeed F, Barna NH, Rana S, Arpinar IB, Liu N (2024) A survey of deep learning and
foundation models for time series forecasting. arXiv preprint arXiv:2401.13912
Mintarsih F, Rasyidi MA, Nurjannah W, Khairani D, Sukmana HT(2023) Lstm variants comparison for
exchange rate idr/usd forecasting with rolling window cross validation. In: 2023 Eighth international
conference on informatics and computing (ICIC), pp. 1–4. IEEE
Mogren O (2016) Continuous recurrent neural networks with adversarial training. arXiv preprint
arXiv:1611.09904
Muandet K, Balduzzi D, Schölkopf B (2013) Domain generalization via invariant feature representation. In:
International conference on machine learning, pp. 10–18. PMLR
Mung PS, Phyu S (2023) Time series weather data forecasting using deep learning. In: 2023 IEEE conference
on computer applications (ICCA), pp. 254–259. IEEE
Murray FT, Ringwood JV, Austin PC (2000) Integration of multi-time-scale models in time series forecast-
ing. Int J Syst Sci 31(10):1249–1260
Nie Y, Nguyen NH, Sinthong P, Kalagnanam J (2022) A time series is worth 64 words: Long-term forecasting
with transformers. arXiv preprint arXiv:2211.14730
Niu Z, Zhong G, Yu H (2021) A review on the attention mechanism of deep learning. Neurocomputing
452:48–62
Noh S-H (2021) Analysis of gradient vanishing of RNNS and performance comparison. Information
12(11):442
Orang O, Silva PC, Guimarães FG (2023) Time series forecasting using fuzzy cognitive maps: a survey. Artif
Intell Rev 56(8):7733–7794
Oreshkin BN, Carpov D, Chapados N, Bengio Y (2019) N-beats: Neural basis expansion analysis for inter-
pretable time series forecasting. arXiv preprint arXiv:1905.10437
Parzen E (1961) An approach to time series analysis. Ann Math Stat 32(4):951–989
Pascanu R, Mikolov T, Bengio Y (2013) On the difficulty of training recurrent neural networks. In: interna-
tional conference on machine learning, pp. 1310–1318. PMLR
Passalis N, Tefas A, Kanniainen J, Gabbouj M, Iosifidis A (2019) Deep adaptive input normalization for time
series forecasting. IEEE Trans Neural Netw Learn Syst 31(9):3760–3765
Pavlov-Kagadejev M, Jovanovic L, Bacanin N, Deveci M, Zivkovic M, Tuba M, Strumberger I, Pedrycz W
(2024) Optimizing long-short-term memory models via metaheuristics for decomposition aided wind
energy generation forecasting. Artif Intell Rev 57(3):45
Pöppelbaum J, Chadha GS, Schwung A (2022) Contrastive learning based self-supervised time-series analy-
sis. Appl Soft Comput 117:108397
Qi M, Zhang GP (2008) Trend time-series modeling and forecasting with neural networks. IEEE Trans Neu-
ral Netw 19(5):808–816
Qi X, Hou K, Liu T, Yu Z, Hu S, Ou W (2021) From known to unknown: Knowledge-guided transformer for
time-series sales forecasting in alibaba. arXiv preprint arXiv:2109.08381
Rawat AS, Chen J, Yu FXX, Suresh AT, Kumar S (2019) Sampled Softmax with random Fourier features.
Adv Neural Inf Process Syst. 32
Salinas D, Flunkert V, Gasthaus J, Januschowski T (2020) Deepar: probabilistic forecasting with autoregres-
sive recurrent networks. Int J Forecast 36(3):1181–1191
Seeger MW, Salinas D, Flunkert V (2016) Bayesian intermittent demand forecasting for large inventories.
Adv Neural Inf Process Syst. 29
Series ST forecasting seasonal time series
Shabani, A., Abdi, A., Meng, L., Sylvain, T.: Scaleformer: iterative multi-scale refining transformers for time
series forecasting. arXiv preprint arXiv:2206.04038 (2022)
Shelatkar T, Tondale S, Yadav S, Ahir S (2020) Web traffic time series forecasting using ARIMA and LSTM
RNN. In: ITM Web of Conferences, Vol 32, p. 03017. EDP Sciences
1 3

Deep learning-based time series forecasting Page 65 of 67 23
Shi X, Chen Z, Wang H, Yeung D-Y, Wong W-K, Woo W-c (2015) Convolutional lstm network: a machine
learning approach for precipitation nowcasting. Adv Neural Inf Process Syst. 28
Shin T, Razeghi Y, Logan IV RL, Wallace E, Singh S (2020) Autoprompt: Eliciting knowledge from language
models with automatically generated prompts. arXiv preprint arXiv:2010.15980
Soltani S (2002) On the use of the wavelet decomposition for time series prediction. Neurocomputing
48(1–4):267–277
Son NN, Van Cuong N (2023) Neuro-evolutionary for time series forecasting and its application in hourly
energy consumption prediction. Neural Comput Appl 35(29):21697–21707
Szegedy C, Liu W, Jia Y, Sermanet P, Reed S, Anguelov D, Erhan D, Vanhoucke V, Rabinovich A (2015)
Going deeper with convolutions. In: Proceedings of the IEEE conference on computer vision and pat-
tern recognition, pp. 1–9
Tang W, Long G, Liu L, Zhou T, Jiang J, Blumenstein M (2020) Rethinking 1d-cnn for time series classifica-
tion: A stronger baseline. arXiv preprint arXiv:2002.10061, 1–7
Tang Y, Yu F, Pedrycz W, Yang X, Wang J, Liu S (2021) Building trend fuzzy granulation-based LSTM recur-
rent neural network for long-term time-series forecasting. IEEE Trans Fuzzy Syst 30(6):1599–1613
Taylor SJ, Letham B (2018) Forecasting at scale. Am Stat 72(1):37–45
Ulyanov D, Vedaldi A, Lempitsky V (2016) Instance normalization: The missing ingredient for fast styliza-
tion. arXiv preprint arXiv:1607.08022
Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser Ł, Polosukhin I (2017) Attention
is all you need. Adv Neural Inf Process Syst. 30
Venkateshwari P, Veeraiah V, Talukdar V, Gupta DN, Anand R, Gupta A (2023) Smart city technical planning
based on time series forecasting of iot data. In: 2023 international conference on sustainable emerging
innovations in engineering and technology (ICSEIET), pp. 646–651. IEEE
Verbesselt J, Hyndman R, Newnham G, Culvenor D (2010) Detecting trend and seasonal changes in satellite
image time series. Remote Sens Environ 114(1):106–115
Wang Z, Bovik AC (2009) Mean squared error: love it or leave it? A new look at signal fidelity measures.
IEEE Signal Process Mag 26(1):98–117
Wang X, Cai Z, Luo Y, Wen Z, Ying S (2022) Long time series deep forecasting with multiscale feature
extraction and seq2seq attention mechanism. Neural Process Lett 54(4):3443–3466
Wang Z, Liu N, Chen C, Guo Y (2023) Adaptive self-attention LSTM for RUL prediction of lithium-ion
batteries. Inf Sci 635:398–413
Wang S, Fan Y, Jin S, Takyi-Aninakwa P, Fernandez C (2023) Improved anti-noise adaptive long short-term
memory neural network modeling for the robust remaining useful life prediction of lithium-ion batter-
ies. Reliab Eng Syst Safety 230:108920
Weerakody PB, Wong KW, Wang G, Ela W (2021) A review of irregular time series data handling with gated
recurrent neural networks. Neurocomputing 441:161–178
Wen Q, Sun L, Yang F, Song X, Gao J, Wang X, Xu H (2020) Time series data augmentation for deep learn-
ing: a survey. arXiv preprint arXiv:2002.12478
Wen Q, Zhou T, Zhang C, Chen W, Ma Z, Yan J, Sun L (2022) Transformers in time series: a survey. arXiv
preprint arXiv:2202.07125
West M (1997) Time series decomposition. Biometrika 84(2):489–494
Weston J, Chopra S, Bordes A (2014) Memory networks. arXiv preprint arXiv:1410.3916
Woo G, Liu C, Sahoo D, Kumar A, Hoi S (2022) Etsformer: Exponential smoothing transformers for time-
series forecasting. arXiv preprint arXiv:2202.01381
Woodward WA, Gray HL (1993) Global warming and the problem of testing for trend in time series data. J
Clim 6(5):953–962
Wu S, Xiao X, Ding Q, Zhao P, Wei Y, Huang J (2020) Adversarial sparse transformer for time series fore-
casting. Adv Neural Inf Process Syst 33:17105–17115
Wu H, Xu J, Wang J, Long M (2021) Autoformer: decomposition transformers with auto-correlation for long-
term series forecasting. Adv Neural Inf Process Syst 34:22419–22430
Yazdanbakhsh O, Dick S (2019) Multivariate time series classification using dilated convolutional neural
network. arXiv preprint arXiv:1905.01697
Yin J, Rao W, Yuan M, Zeng J, Zhao K, Zhang C, Li J, Zhao Q (2019) Experimental study of multivariate
time series forecasting models. In: Proceedings of the 28th ACM international conference on informa-
tion and knowledge management, pp. 2833–2839
Young, J., Chen, J., Huang, F., Peng, J.: Dateformer: Time-modeling transformer for longer-term series fore-
casting. arXiv preprint arXiv:2207.05397 (2022)
1 3

23 Page 66 of 67 X. Song et al.
Yu F, Koltun V (2015) Multi-scale context aggregation by dilated convolutions. arXiv preprint
arXiv:1511.07122
Yun C, Bhojanapalli S, Rawat AS, Reddi SJ, Kumar S (2019) Are transformers universal approximators of
sequence-to-sequence functions? arXiv preprint arXiv:1912.10077
Zhai Y, Lv Z, Zhao J, Wang W (2023) Knowledge discovery and variable scale evaluation for long series
data. Artif Intell Rev 56(4):3157–3180
Zhang GP (2003) Time series forecasting using a hybrid ARIMA and neural network model. Neurocomput-
ing 50:159–175
Zhang Y, Yan J (2022) Crossformer: Transformer utilizing cross-dimension dependency for multivariate time
series forecasting. In: The eleventh international conference on learning representations
Zhang X, Jin X, Gopalswamy K, Gupta G, Park Y, Shi X, Wang H, Maddix DC, Wang Y (2022) First de-trend
then attend: Rethinking attention for time-series forecasting. arXiv preprint arXiv:2212.08151
Zhang X, Li Q, Liang D (2023) An adaptive spatio-temporal neural network for PM2.5 concentration fore-
casting. Artif Intell Rev 56(12):14483–14510
Zhang J, Li X, Tian J, Luo H, Yin S (2023) An integrated multi-head dual sparse self-attention network for
remaining useful life prediction. Reliab Eng Syst Safety 233:109096
Zhang K, Zhou F, Wu L, Xie N, He Z (2024) Semantic understanding and prompt engineering for large-scale
traffic data imputation. Inf Fus 102:102038
Zhao B, Lu H, Chen S, Liu J, Wu D (2017) Convolutional neural networks for time series classification. J
Syst Eng Electron 28(1):162–169
Zhao WX, Zhou K, Li J, Tang T, Wang X, Hou Y, Min Y, Zhang B, Zhang J, Dong Z, et al (2023) A survey
of large language models. Preprint at arXiv:2303.18223
Zheng S, Ristovski K, Farahat A, Gupta C (2017) Long short-term memory network for remaining useful life
estimation. In: 2017 IEEE international conference on prognostics and health management (ICPHM),
pp. 88–95. IEEE
Zhong X, Cambria E (2023) Time expression recognition and normalization: a survey. Artif Intell Rev
56(9):9115–9140
Zhou H, Zhang S, Peng J, Zhang S, Li J, Xiong H, Zhang W (2021) Informer: Beyond efficient transformer
for long sequence time-series forecasting. In: Proceedings of the AAAI conference on artificial intel-
ligence, vol. 35, pp. 11106–11115
Zhou T, Ma Z, Wen Q, Wang X, Sun L, Jin R (2022) Fedformer: Frequency enhanced decomposed trans-
former for long-term series forecasting. In: International conference on machine learning, pp. 27268–
27286. PMLR
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Authors and Affiliations
Xiaobao Song1,2 · Liwei Deng2 · Hao Wang1,2 · Yaoan Zhang2 · Yuxin He3 ·
Wenming Cao1,2
Hao Wang
haowang@szu.edu.cn
Xiaobao Song
2020284089@email.szu.edu.cn
Liwei Deng
2021280356@email.szu.edu.cn
Yaoan Zhang
2021280103@email.szu.edu.cn
Yuxin He
heyuxin@sztu.edu.cn
1 3

Deep learning-based time series forecasting Page 67 of 67 23
Wenming Cao
wmcao@szu.edu.cn
1 Guangdong Provincial Key Laboratory of Intelligent Information Processing, Shenzhen
University, Shenzhen, China
2 Guangdong Multimedia Information Service Engineering Technology Research Cente,
Shenzhen University, Shenzhen, China
3 College of Urban Transportation and Logistics, Shenzhen Technology University, Shenzhen,
China
1 3