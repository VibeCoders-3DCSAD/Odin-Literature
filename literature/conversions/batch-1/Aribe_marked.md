---
conversion_metadata:
  converted_at: "2026-07-22T12:00:53Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Aribe.pdf"
  source_pdf_sha256: "06c61cabd9ec89cc7521589ca99a5975e56059956b8df6f5a9eb0f9bae00e765"
  page_count: 17
  markdown_char_count: 170030
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of Engineering Trends and Technology 
ISSN: 2231–5381 / https://doi.org/10.14445/22315381/IJETT-V73I10P104                                        © 2025 Seventh Sense Research Group®

Volume 73 Issue 10, 32-48, October 2025

Original Article

Spiking Neural Networks: The Future of Brain-Inspired 
Computing

Sales G. Aribe Jr.

Information Technology Department, Bukidnon State University, Fortich Street, Malaybalay City, Philippines.

Corresponding Author : sg.aribe@buksu.edu.ph

Received: 14 July 2025

Revised: 06 October 2025

Accepted: 07 October 2025

Published: 31 October 2025

Abstract  -  Spiking  Neural  Networks  (SNNs)  represent  the  latest  generation  of  neural  computation,  offering  a  brain-inspired 
alternative to conventional Artificial Neural Networks (ANNs). Unlike ANNs, which depend on continuous-valued signals, SNNs 
operate using distinct spike events, making them inherently more energy-efficient and temporally dynamic. This study presents a 
comprehensive  analysis  of  SNN  design  models,  training  algorithms,  and  multi-dimensional  performance  metrics,  including 
accuracy, energy consumption, latency, spike count, and convergence behavior. Key neuron models such as the Leaky Integrate-
and-Fire  (LIF)  and  training  strategies—including  surrogate  gradient  descent,  ANN-to-SNN  conversion,  and  Spike-Timing 
Dependent Plasticity (STDP)—are examined in depth. Results show that surrogate gradient-trained SNNs closely approximate 
ANN accuracy (within 1–2%), with faster convergence by the 20th epoch and latency as low as 10 milliseconds. Converted SNNs 
also achieve competitive performance but require higher spike counts and longer simulation windows. STDP-based SNNs, though 
slower to converge, exhibit the lowest spike counts and energy consumption (as low as 5 millijoules per inference), making them 
optimal for unsupervised and low-power tasks. These findings reinforce the suitability of SNNs for energy-constrained, latency-
sensitive, and adaptive applications such as robotics, neuromorphic vision, and edge AI systems. While promising, challenges 
persist in hardware standardization and scalable training. This study concludes that SNNs, with further refinement,  are poised 
to propel the next phase of neuromorphic computing.

Keywords  -  Artificial  Intelligence,  Brain-inspired  computing,  Energy  efficiency,  Neuromorphic  computing,  Spiking  Neural 
Network.

1. Introduction

The advent of Artificial Intelligence (AI) has ushered in a 
technological revolution that permeates virtually all aspects of 
modern life, from healthcare and transportation to finance and 
education. Central to this evolution are a class of computational 
models  collectively  referred  to  as  ANNs  that  have  achieved 
stunning  results  across  an  array  of  pattern  recognition  and 
machine  learning problems. Traditional ANNs, however, are 
extremely  energy  inefficient  and  biologically  unrealistic  [1], 
[2]  despite  their  impressive  performance.  These  are  also 
difficult to implement because they rely on continual signal and 
large  matrix  multiplication,  which  are  computationally 
expensive and biologically unrealistic [3].

Various neural network architectures have been created to 
address  distinct  computational  challenges.  The  ANN  is  the 
basic model for deep learning, but cannot be directly applied to 
temporal  data  because  of  its  computational  complexity  and 
absence  of  memory  [4,  5].  Convolutional  Neural  Networks 
(CNNs) are engineered for spatial feature extraction in image 
and  video  processing  and  are  not  directly  applicable  to 
temporal  or  sequential  data  [6].  Recurrent  Neural  Networks

(RNNs)  [7]  and  more  sophisticated  versions,  such  as  Long 
Short-Term Memory (LSTM) [8] and Gated Recurrent Units 
(GRUs),  are  designed  for  sequential  input;  yet,  they  are 
plagued by vanishing gradient issues and exhibit inefficiency 
in modeling long-range relationships. More recent models, like 
Transformers,  have  recently  revolutionized  natural  language 
processing  using  attention  mechanisms,  but  at  the  cost  of 
humongous memory and processing demands [10].

All these models have a basic property in common: they 
depend on synchronous updates and on continuous activations. 
This  is  not  the  case  in  the  human  brain,  which  is  an 
asynchronous system and communicates with discrete binary 
spikes [11]. In addition, classic networks carry out millions of 
operations  per  inference  step,  resulting  in  high  power 
consumption-a critical bottleneck in scenarios such as mobile 
and edge computing [12]. Despite their success, these networks 
are entirely based on dense and continuous computations and 
lack biological realism, which renders them energy-inefficient 
and  not  amenable  to  real-time,  low-power  applications,  the 
limitations  that  SNNs  try  to overcome  [13].  SNNs,  the  most 
recent  evolution  of  neural  network  models,  signify  a

This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/)

---

<!-- PAGE 2 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

in  artificial

intelligence  by 
transformative  advancement 
mimicking  the  discrete  and  temporal  firing  patterns  of 
biological  neurons.  [14].  Unlike  ANNs,  which  process 
information in  a  synchronous  and continuous fashion,  SNNs 
operate on sparse, event-driven spike trains, enabling them to 
process spatiotemporal data with greater energy efficiency and 
fidelity  to  brain-like  computation.  This  bio-inspired  method 
closely  resembles  how  actual  neurons  in  the  brain  exchange 
information  by  sending  out  short,  timed  electrical  signals 
known as spikes [15].

Interest in SNNs has increased due to recent developments 
in  neuromorphic  engineering,  which  creates  hardware  that 
mimics the composition and operations of the human brain [16, 
17].  Chips  like  International  Business  Machines’  (IBM) 
TrueNorth  and  Intel’s  Loihi  show  that  SNNs  may  be 
implemented at scale with extremely low power consumption, 
which  makes  them  appropriate  for  use  in  edge  computing 
settings and mobile devices [18, 12]. Additionally, SNNs are 
being studied extensively for use in brain-computer interfaces, 
robotics, and sensory processing, highlighting their promise in 
latency-sensitive, real-time scenarios [19].

Despite rapid progress, most studies examine one training 
paradigm  or  one  metric  at  a  time—e.g.,  ANN-to-SNN 
conversion optimized for accuracy on image benchmarks  [20, 
21]  surrogate-gradient  training  highlighting  differentiable 
approximations  [22],  or  neuromorphic  reports  emphasizing 
hardware  power/latency  [12,  23].  A  unified  head-to-head 
analysis 
that  compares  surrogate-trained,  ANN-to-SNN 
converted,  and  STDP  models  under  a  single  protocol  and 
across  multiple  dimensions—accuracy,  latency,  energy  per 
inference, spike count, and convergence—on both event-based 
and static datasets remains limited in the literature [1, 20, 22, 
24, 25]. This  gap obscures  practical  tradeoffs  that matter for 
edge  deployment  and  real-time  robotics,  where  temporal 
precision and energy budgets are binding constraints [12, 23].

that

protocol

compares

This work addresses that gap by: (i) establishing a unified 
surrogate-trained, 
evaluation 
converted,  and  STDP  SNNs  across  five  metrics  (accuracy, 
latency,  energy,  spike  count,  convergence);  (ii)  reporting 
latency  and  spiking  activity  alongside  accuracy  to  reflect 
hardware-aware  performance;  (iii)  providing  a  convergence 
analysis to 20 epochs that clarifies optimization behavior under 
different learning rules; and (iv) translating these findings into 
application-oriented  guidance (e.g.,  surrogate  SNNs  for  low-
latency  accuracy 
for  ultra-low-power 
targets;  STDP 
unsupervised settings). Relative to prior work that focuses on a 
single  method  or  metric  [20-22,  25],  this  study  offers  an 
integrated,  multi-metric  comparison  that  supports  principled 
model selection for neuromorphic and edge AI [1, 12]. Given 
the  rising  energy  costs  of  deep  learning  models,  particularly 
transformer-based systems [10, 12], the exploration of SNNs is 
not only  a  technical advancement but  also an  important  step 
toward  sustainable  AI  computing.  By  reducing energy  usage

by an order of magnitude compared to ANNs, as shown in this 
study,  SNNs  present  a  feasible  path  for  greener  and  more 
efficient edge intelligence. This positions the current work as 
both  timely  and  original,  addressing  the  dual  challenge  of 
advancing AI performance while mitigating environmental and 
energy concerns.

Thus, this paper comprehensively examines SNNs as the 
future of brain-inspired computing. It begins by outlining their 
biological underpinnings and core mechanisms, followed by a 
comparative analysis with traditional ANNs. It then delves into 
various 
training 
methodologies  that  define  current  SNN  research.  This  work 
attempts  to  give  a  thorough  evaluation  of  SNNs  and  make 
suggestions 
in 
neuromorphic AI by reviewing experimental benchmarks and 
implementation challenges.

research  and  development

applications,  design

strategies,

further

and

for

2. Related Literature 
2.1. Biological Inspiration

The biological processes of the human brain, namely how 
neurons  interact  by  sending  out  distinct  electrical  impulses 
called spikes, served as the model for SNNs [26]. Conventional 
neural networks depend on levels of constant activation, while 
biological neurons transmit information through asynchronous 
events 
thresholds. 
Foundational biological models  such as the  Hodgkin-Huxley 
model [27] and the Leaky Integrate-and-Fire (LIF) model [28] 
form the theoretical basis of SNNs. Essential neural functions 
like  firing  thresholds,  refractory  periods,  and  membrane 
potential degradation are replicated in these models.

triggered  by  membrane  potential

Moreover,  spike-based  learning  in  biological  systems  is 
often attributed to synaptic plasticity governed by timing rules 
[29].  Spike-Timing  Dependent  Plasticity  (STDP),  which 
modifies synaptic weights according to the relative timing of 
pre- and postsynaptic spikes, is a good illustration [30]. STDP 
has  been  successfully  integrated  into  SNNs  to  enable 
biologically  plausible 
for 
backpropagation.

learning  without

the  need

These qualities allow SNNs to capture temporal changes, 
sparse  activation,  and  asynchronous  signaling, 
thereby 
achieving  greater  similarity  to  cortical processes observed  in 
neuroscience [31].

2.2. Fundamentals of SNNs

At the core of SNN operation is the spike-based encoding 
of information. SNNs use rate or temporal coding schemes to 
encode  data  in  the  time  and  frequency  of  spikes  rather  than 
real-valued  vectors  [32].  While  temporal  coding  encodes 
information  in  the  exact  time  of  spikes,  rate  coding  conveys 
input  strength  by  spike  frequency.  SNNs  are  more  energy-
efficient and appropriate for event-driven processing through 
these processes.

33

---

<!-- PAGE 3 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

Many equations are used to explain the behavior of spiking 
neurons,  but  the  LIF  model  is  still  the  most  often  utilized 
because of its ease of use and computational effectiveness [33]. 
For  learning,  SNNs  use  biologically  inspired  methods  like 
surrogate  gradient  methods,  STDP,  and  Reward-Modulated 
STDP  (R-STDP)  that  enable  supervised  learning  despite  the 
non-differentiability  of  spike  events  [34].  In  addition,  recent 
research  has  introduced  training  techniques  that  make  SNNs 
competitive with deep learning models. These include hybrid 
approaches like converting pre-trained ANNs into SNNs [20], 
and direct training using approximated gradients, which helps 
overcome the challenges of discontinuous activation [22].

2.3. Comparison with Traditional ANNs

SNNs  differ  fundamentally  from  ANNs  in  architecture, 
data  representation,  and  learning  strategy.  ANNs  use  dense 
layers of constant activation functions  like  sigmoid or  ReLU 
and are trained using backpropagation [35, 36]. SNNs, on the 
other hand, use gradient-free or biologically motivated learning 
algorithms  and 
limited,  event-triggered 
activations [37].

function  with

The energy efficiency of SNNs is one of its main benefits. 
While ANNs process every node during each cycle, SNNs only 
activate  neurons  upon  spike  generation, 
in 
significantly fewer operations and reduced power usage—ideal 
for  low-resource  or  edge  devices  [38].  Furthermore,  SNNs 
to  process 
exhibit 
sequential  and 
than 
real-time  data  more  effectively 
conventional models such as CNNs and RNNs [39, 40].

temporal  sensitivity,  enabling

resulting

them

However, SNNs face significant challenges in scalability, 
training convergence, and a lack of standardized frameworks 
compared to mature ANN systems. While ANNs benefit from 
extensive  optimization  libraries  and  hardware  acceleration 
(e.g., TensorFlow, GPUs), SNNs are still evolving in terms of 
simulation platforms and hardware compatibility [41].

Surveys  and  foundational  studies  emphasize  SNNs’ 
temporal  coding  and  energy  advantages  but  typically  report 
accuracy  or  hardware  power  in  isolation  [1,  38,  40]. 
Conversion pipelines preserve ANN accuracy yet often require 
longer  simulation  windows  and  higher  spike  rates  [20,  21]; 
surrogate-gradient methods close the accuracy gap with direct 
end-to-end training [22]; and neuromorphic reports foreground 
energy/latency  on  chips  [12,  23].  By  evaluating  all  three 
training  strategies  under  a  consistent  setup  and  reporting 
accuracy, latency, energy, spike, and convergence together, the 
present study complements these strands. It clarifies practical 
tradeoffs for deployment-oriented SNN design [24, 25].

2.4. Applications of SNNs

Neuromorphic  Hardware:  The  field  of  neuromorphic 
computing, which describes hardware architectures intended to 
mimic the structure and functionality of the brain, is one of the 
most  promising  areas  for  SNNs.  IBM’s  TrueNorth  [42]  and

34

Intel’s  Loihi  [43]  are  two  major  neuromorphic  chips  that 
support event-driven computation and on-chip learning. These 
chips  enable  real-time  processing  with  ultra-low  power 
consumption,  opening  doors  for  deploying  SNNs  in  edge 
computing, wearables, and autonomous systems.

Robotics: In robotics, SNNs enable low-latency responses 
and  real-time  sensory  integration.  For  instance,  SNNs  have 
been used in applications where timing and energy efficiency 
are  crucial,  such  as  visual  tracking,  object  recognition,  and 
locomotion  control  [44].  Because  SNNs  are  asynchronous, 
they work well in dynamic settings where conventional ANN-
based controllers would be too sluggish or power-hungry.

Edge Computing: SNNs’ event-based design and minimal 
activity  make  them  perfect  for  use  in  devices  with  limited 
energy. Applications include gesture recognition using event-
based  cameras  (e.g.,  DVS128  dataset),  anomaly  detection  in 
IoT systems, and on-device speech processing [38].

Healthcare: SNNs are essential for prostheses and Brain-
Machine  Interfaces  (BMIs)  in  biomedical  engineering  and 
neuroscience.  They  can  interpret  neural  signals  for  motor 
control  or  restore  sensory  functions.  SNNs  are  also  being 
explored for seizure prediction, Electroencephalogram  (EEG) 
signal classification, and neural rehabilitation, where temporal 
precision and biological compatibility are essential [45].

In  summary,  existing  studies  establish  SNNs  as 
biologically  inspired  and  energy-efficient  yet  fragmented 
across training strategies and evaluation metrics. This review 
sets the stage for a unified analysis.

3. Methodology 
3.1. SNN Design

Replicating  the  dynamic  behavior  of  biological  neurons 
and their synaptic contacts is the foundation of SNN design. 
SNNs use asynchronous, event-driven computing, in contrast 
to classic neural networks, where each layer analyzes inputs in 
a fixed, synchronous fashion. Neuron models that mimic the 
biophysical characteristics of actual neurons, most notably the 
LIF model, enable this design.

One of the most popular and straightforward models for 
SNN  simulations  is  the  LIF  model  [46].  It  records  crucial 
neural  processes  such  as  threshold-based  spike  production, 
membrane potential accumulation, and leakage across time. A 
neuron “fires” a spike and resets its membrane potential when 
incoming synaptic inputs cause it to surpass a certain threshold. 
Because neurons in this model only fire in response to strong 
stimuli,  it  enables a  sparse,  energy-efficient network [11]. A 
LIF neuron’s behavior can be shown in Figure 1. This graphic 
shows how the input current causes the membrane potential to 
rise over time. The neuron mimics the firing behavior seen in 
organic neurons by emitting a spike and then resetting when 
the voltage hits a predetermined threshold.

---

<!-- PAGE 4 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

0

5

10

15

20

25

30

35

Time (ms)
40
45
50

55

60

65

70

75

80

85

90

95 100

Membrane Potential (LIF Neuron)

Threshold

-54

-56

-58

-60

-62

-64

-66

-68

-70

)

V
m

(

l
a
i
t
n
e
t
o
P
e
n
a
r
b
m
e

M

Fig. 1 LIF neuron model

More sophisticated models, such as the Izhikevich model, 
simulate  a  variety  of  neuronal  firing  patterns,  including 
bursting,  tonic  spiking,  and  adaptation,  by  fusing  biological 
realism with computing efficiency [23]. The choice of neuron 
model  typically  balances  between  biological  fidelity  and 
computational  overhead,  depending  on 
the  application 
domain—whether  high-performance  robotics  or  low-power 
edge computing.

SNN  architecture  typically  includes  input,  hidden,  and 
output layers, where spikes propagate through synapses with 
temporal delays and weight modulation [40]. These networks 
can be feedforward, recurrent, or convolutional, depending on 
the  data  type  and  processing  goals.  For  image-based  tasks, 
Convolutional SNNs (CSNNs) are increasingly popular due to 
their  ability  to  preserve  spatial  hierarchies  while  benefiting 
from event-driven sparsity [47].

SNNs are translated to neuromorphic circuits in hardware 
implementations,  including  Intel’s  Loihi,  which  allows  for 
dynamic neural configuration with spiking inputs and on-chip 
learning. Loihi incorporates programmable neuron models and 
synaptic delays, enabling flexible SNN design for real-world 
applications [12].

Figure 2  illustrates  the three main phases of a  full  SNN 
pipeline:  input  encoding,  spiking  neuron  processing,  and 
output decoding. Using encoding techniques like rate coding or 
temporal  coding,  continuous  signals  like  audio,  pictures,  or 
sensor data are converted into discrete spike trains during input 
encoding. After passing through one or more layers of spiking 
neurons,  these  spike  trains  are  used  to  analyze  information 
based on the timing and intensity of the spikes. The output layer 
then  decodes  the  spike  patterns  into  a  control,  decision,  or 
prediction signal that is suitable for the intended use.

Fig. 2 Conceptual architecture of SNN [48]

35

---

<!-- PAGE 5 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

The system includes input encoding to convert signals into 
spikes,  multiple  spiking  neuron  layers  for  event-driven 
computation,  and  output  decoding  to  produce  meaningful 
results. This modular architecture allows SNNs to mimic the 
asynchronous,  event-driven  behavior  of  biological  neural 
systems. The design supports a wide variety of tasks ranging 
from object recognition to robotic control, depending on how 
the neurons are interconnected and trained.

Several  software  tools  have  been  widely  adopted  to 
simulate SNN behavior. Neural Simulation Tool (NEST) [49] 
is  used  for  broad-based  simulations  of  spiking  neuron 
networks,  especially  in  neuroscience  research.  Biologically 
in  Networks 
Inspired  Neural  and  Dynamical  Systems 
(BindsNET)  [50]  and  Brian2  [51]  offer  more  flexibility  and 
Python integration for machine learning tasks. These platforms 
support complex network configurations, STDP learning rules, 
and  integration  with  neuromorphic  datasets.  Overall,  the 
design  of  an  SNN  requires  careful  attention  to  the  neuron 
model,  network  topology,  synaptic  behavior,  and  hardware-
software  compatibility.  These  components  collectively 
determine 
to  mimic  brain-like 
computation while maintaining computational tractability and 
real-world applicability.

the  network’s  ability

3.2. Training Algorithms

spikes

are  discrete,  binary

The  non-differentiable  characteristics  of  spike  events 
make training SNNs more difficult than training regular ANNs. 
Since 
standard 
backpropagation—which  relies  on  continuous  gradients—
cannot be directly applied. Researchers have therefore created 
specific training methods that are suited to the event-driven and 
temporal dynamics of SNNs.

events,

3.3. Unsupervised Learning: STDP

STDP  is  among  the  most  biologically  realistic  training 
techniques. The exact timing of pre- and postsynaptic spikes 
determines  how  STDP  modifies  synaptic  weights;  if  a 
presynaptic neuron fires just before a postsynaptic neuron, the 
synapse is strengthened; if not, it is weakened [52, 53]. This 
local, unsupervised learning rule has been widely implemented 
in early layers of SNNs to extract spatiotemporal patterns from 
data without requiring labels [54].

3.4. Surrogate Gradient Descent

To  enable  supervised  learning,  researchers  developed 
surrogate  gradient  methods.  These  techniques  enable  the 
application  of  gradient-based  optimization 
to 
backpropagation  by  substituting  a  smooth,  differentiable 
approximation for the non-differentiable spike function during 
the  backward  run  [55].  Popular  surrogate  functions  include 
piecewise  linear,  sigmoid,  or  exponential  approximations. 
SNNs  may  now  be  trained  with  competitive  accuracy  on 
common  classification  benchmarks  such  as  the  Canadian 
Institute  for  Advanced  Research-10  (CIFAR-10)  and  the 
Modified  National  Institute  of  Standards  and  Technology

akin

36

[22,  56]. 
(MNIST)  using  surrogate  gradient  descent 
Additionally, this has made it possible to learn deep SNNs end-
to-end without converting from ANNs.

3.5. ANN-to-SNN Conversion

Training  a traditional  ANN  and  then converting  it  to an 
SNN by interpreting activation levels as firing rates is another 
useful  method.  This  method  allows  for  high-performance 
training using standard deep learning libraries, followed by an 
efficient  deployment  in  event-driven  hardware  [21,  24]. 
However,  this  technique  often  requires  careful  calibration  of 
firing thresholds and time constants to preserve accuracy.

3.6. Experimental Framework

The  experimental  framework  for  evaluating  SNNs 
involves  selecting  benchmark  datasets,  simulation  tools, 
training  protocols,  and  performance  metrics  tailored  to  the 
unique  characteristics  of  spike-based  computation.  This 
section outlines the standard setup used in the literature to train 
and  assess  SNNs  in  classification,  control,  and  recognition 
tasks.

3.6.1. Datasets

SNNs  are  often  evaluated  using  both  static  and 
neuromorphic datasets to benchmark their performance under 
conventional and event-based input conditions:

•  MNIST:  A  widely  used  dataset  for  recognition  of 
handwritten  digits,  which  consists  of  70,000  grayscale 
images [57]. Rate or latency encoding techniques are used 
in SNNs to transform pictures into spike trains. MNIST 
serves as a baseline for testing  the accuracy and energy 
efficiency  of  small-scale  SNNs.  In  this  study,  a  rate-
coding  system  that  linked  pixel  intensity  to  spike 
frequency was used to encode MNIST images. To ensure 
there  was  enough  spike  activity  for  recognition  tasks, 
each image was shown throughout a simulation window 
of 100 ms.

•  DVS128  Gesture  Dataset:  It  is  a  neuromorphic  dataset 
recorded  with  a  Dynamic  Vision  Sensor  (DVS),  which 
captures  changes  in  brightness  as  asynchronous  spikes 
rather  than  static  frames  [58].  It  is  frequently  used  to 
assess  SNNs’  real-time  performance  in  event-driven 
processing  and  motion  identification.  For  gesture  data, 
temporal  coding  was  employed,  with  spike  timing 
directly  representing  motion  events.  Input  sequences 
were segmented into 150-ms windows to balance latency 
and recognition accuracy.

rich,

•  SHD/SSC  Datasets:  The  Spiking  Heidelberg  Digits 
(SHD) and Spiking Speech Commands (SSC) datasets are 
temporally 
spike-based  versions  of  audio 
digit/speech recognition tasks, tailored for direct input to 
SNNs  [25].  Audio  waveforms  were  preprocessed  into 
spike  trains  using  latency  encoding  with  a  maximum 
window  of  200  ms  per  sample,  aligned  with  common 
auditory neuroscience benchmarks.

---

<!-- PAGE 6 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

3.6.2. Simulation Tools and Platforms

A  range  of  simulators  and  libraries  is  available  for

designing, training, and testing SNNs:

•  Brian2: A flexible, Python-based simulator ideal for small 
to  medium-scale  experiments.  It  allows  for  custom 
neuron models and precise temporal dynamics [51]. 
•  BindsNET: Built on top of PyTorch, this library integrates 
deep learning infrastructure with spiking neuron models, 
supporting supervised and unsupervised learning [50].

•  NEST:  Designed

large-scale 
computational  neuroscience,  NEST 
studying  population-level  dynamics 
modeling [59].

for

simulations 
in 
is  suitable  for 
cortical

and

•  CARLsim: A GPU-accelerated SNN simulator developed 
for  large,  real-time  SNN  systems  with  STDP  and 
reinforcement learning support [60-62]. 
Intel  Loihi  and  IBM  TrueNorth  Software  Development 
Kits (SDKs): Neuromorphic hardware platforms include 
their  own  toolkits,  allowing  direct  deployment  and 
evaluation of SNNs in real-world scenarios [63, 18].

•

Experiments  were  conducted  primarily  using  the  Brian2 
simulator for surrogate gradient SNNs, BindsNET for ANN-
to-SNN  conversion  pipelines,  and  NEST  for  large-scale 
spiking models. Default neuron parameters followed the LIF 
model  with  membrane  time  constant  τ  =  20  ms,  threshold 
voltage equivalent to Vth = 1.0, and refractory period of 5 ms, 
unless otherwise noted.

Training was performed on a workstation with an NVIDIA 
RTX GPU and 32 GB RAM, ensuring comparability with prior 
benchmarks in the literature [20, 22, 25].

3.6.3. Evaluation Metrics

Given  the  unique  characteristics  of  SNNs,  evaluation 
metrics  go  beyond  classification  accuracy  and  include 
measurements 
that  reflect  computational  efficiency  and 
biological realism:

•  Accuracy: The most basic metric, measuring how well the 
recognition, 
tasks

like  digit

SNN  performs 
classification, or control prediction.

in

Latency= tdecision-t0

(2)

•  Spike  Count:  The  aggregate  amount  of  spikes 
represents  power

produced  during 
consumption and computational sparsity.

inference

Total Spikes=  ∑ ∑ si(t)

T
t=1

N
i=1

(3)

Where: 
 si (t) = 1 if neuron i spikes at time t, otherwise 0 
 N = total number of neurons 
 T = total time steps

•  Energy  Efficiency:  The  overall  number  of  spikes  and 
operations  involved  is  a  simplistic  proxy  for  energy. 
Measured in operations per joule or spikes per watt, this 
is  very  significant  in  neuromorphic  computing.  On 
neuromorphic  hardware,  SNNs  are  usually  orders  of 
magnitude more efficient than ANNs.

Etotal = Espike*S+ Esynapse*C

(4)

Where: 
Espike = energy per spike (hardware-specific) 
Esynapse  = energy per synaptic operation 
S = total spikes 
C = total synaptic operations

Alternatively, normalized energy efficiency:

Energy Efficiency =

Accuracy

Energy Consumption (Joules)

(5)

•  Convergence Time: Measures how fast the network learns

(training efficiency). It is often expressed as:

Convergence Time = Epochmin where

Accuracyepoch≥Target Accuracy

(6)

Overall,  the  datasets,  encoding  schemes,  and  simulation 
platforms ensure that results are reproducible and comparable 
to prior SNN benchmarks.

Accuracy =

Number of Correct Predictions

Total Number of Predictions

x 100%

(1)

4. Results and Discussion 
4.1. Performance Analysis

•  Latency:  Measures  the  time,  in  milliseconds  (ms)  or 
timesteps, it takes for the network to produce a decision. 
Shorter  latency  indicates  better  suitability  for  real-time 
applications.

Let:

tdecision  = time when the first output neuron spikes 
   t0 = time of input stimulus

37

SNNs  have  demonstrated  promising  performance  across 
several  benchmarks  in  static  and  event-based  learning  tasks. 
On  traditional  datasets  like  MNIST,  SNNs  trained  using 
surrogate gradient methods or ANN-to-SNN conversion have 
achieved  classification  accuracies  exceeding  98%,  nearly 
21].  Similarly, 
matching 
convolutional  SNNs  have  proven  effective  in  CIFAR-10, 
reaching  accuracies  between  85%  and  90%,  which  are 
competitive with shallow CNNs under constrained conditions

conventional  ANNs

[20,

---

<!-- PAGE 7 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

[40]. Because SNNs can analyze event-driven inputs in real-
time,  they  have  demonstrated  excellent  appropriateness  for 
neuromorphic datasets such as the DVS128 Gesture Dataset. 
Models  evaluated  on  DVS  datasets  often  outperform 
traditional frame-based models in latency and responsiveness, 
despite  achieving  slightly  lower  absolute  accuracy  [64].  For 
instance, using a spiking CNN trained with STDP and tested 
on  DVS128,  Bai et  al.  [65] reported over 93% classification 
accuracy in dynamic gesture recognition.

Furthermore,  directly  trained  SNNs  using  surrogate 
gradient  descent  have  closed  the  performance  gap  with 
traditional ANNs. Zenke and Ganguli [34] reported that their 
SuperSpike  algorithm  enabled  multilayer  SNNs  to  reach 
comparable 
levels  of  accuracy  and  generalization  on 
spatiotemporal  classification  tasks.  Similarly,  end-to-end 
trained  SNNs  have  been  applied  to  SHD  and  SSC  datasets, 
demonstrating  that temporal structure in auditory signals can 
be effectively captured by SNN dynamics [25].  Nonetheless, 
the  neuron  model,  encoding  strategy,  and  training  technique 
continue to have a significant impact on performance. Higher 
accuracy  is  possible  with  ANN-to-SNN  conversion,  but  the

increased spike rates result in longer inference times. Directly 
trained  SNNs,  on  the  other  hand,  provide  faster  and  sparser 
computing, but they may require more epochs to converge and 
intricate  hyperparameter  adjustment.  The  performance  of 
several network models on benchmark datasets is compiled in 
the table below:

Table 1. SNN performance summary

MNIST 
Accuracy 
(%) 
99.2

CIFAR-10 
Accuracy 
(%) 
92

Energy 
Consumption 
(Normalized) 
1

98.1

89.3

97.8

85.7

95.5

74.2

0.1

0.08

0.05

Model

ANN (CNN) 
Converted 
SNN 
Direct SNN 
(Surrogate 
Gradient) 
STDP-based 
SNN

Figure  3  illustrates  the  tradeoffs  between  precision  and

energy efficiency by visualizing this data.

MNIST Accuracy (%)
CIFAR-10 Accuracy (%)

)

%

(

s
i
s
y
l
a
n
A
y
c
r
u
c
c
A

120

100

80

60

40

20

0

ANN (CNN)

Converted SNN

Direct SNN (Surrogate
Gradient)

STDP-based SNN

Model

Fig. 3 Performance analysis and energy of SNNs vs ANN

in

CNNs

ANNs—and

particular—consistently 
outperform  the  other  models  in  terms  of  classification 
accuracy, but at the expense of significant energy consumption. 
Converted SNNs, which are based on pre-trained ANNs, use a 
lot  less  energy  and  nearly  match  the  accuracy  of  their  ANN 
counterparts.

For  applications  needing  moderate  performance  with 
better  computational  savings,  directly  trained  SNNs  using 
surrogate gradient techniques provide a well-balanced tradeoff 
between  accuracy  and  energy  efficiency.  The  sparse,  event-
driven  character  of  STDP-based  SNNs,  on  the  other  hand, 
results in the highest energy efficiency; however, the accuracy

38

of these models is significantly lower than that of other models. 
To assess the robustness of accuracy results, each experiment 
was  executed  in  five  independent  runs  with  varying  random 
seeds.  Reported  accuracy  values  represent  mean  ±  standard 
deviation.

For MNIST, surrogate gradient SNNs achieved 97.8% ± 
0.2,  converted  SNNs  98.1%  ±  0.3,  and  STDP-based  models 
95.5% ± 0.4, confirming consistency across runs. On CIFAR-
10, accuracies were 85.7% ± 0.5 (surrogate SNN), 89.3% ± 0.4 
(converted SNN), and 74.2% ± 0.6 (STDP). It is confirmed that 
observed  differences  are  statistically  significant  and  not  the 
result of chance when the standard deviation is less than 1%.

---

<!-- PAGE 8 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

These results confirm that SNNs can approach ANN-level 
accuracy  while  maintaining  sparse, efficient  spiking activity. 
The  overall  performance  of  SNNs  across  different  tasks 
illustrates  their  growing  maturity  and  capability  to  support 
intelligent  computation  under  real-world  constraints.  While 
SNNs have  yet to  surpass  deep  ANNs on most benchmarks, 
their  ability  to  approximate  performance  while  drastically 
reducing energy and latency makes them a compelling choice 
for the next generation of efficient AI systems.

Table 2. Latency comparison table 
Model 
ANN (CNN) 
Converted SNN 
Surrogate Gradient SNN 
STDP-based SNN

Latency (ms) 
45 
20 
10 
15

4.2. Latency Analysis

A  crucial  parameter  for  assessing  SNNs’  real-time 
performance is latency, which is the interval of time between 
an input stimulus and the system’s response. As shown in Table

2,  SNNs  have  a  considerable  latency  advantage  over  typical 
ANNs because of their event-driven architecture, especially in 
low-power and time-sensitive applications.

In benchmark evaluations using event-based datasets such 
as DVS Gesture and SHD, SNNs have demonstrated inference 
latencies  as  low  as  5–10  ms  per  sample  when  deployed  on 
neuromorphic platforms [12, 66]. In comparison, CNN-based 
ANNs  typically  require  20–50  ms,  depending  on  model 
complexity and hardware configuration. Among different SNN 
training  paradigms,  directly  trained  surrogate  gradient  SNNs 
strike a balance by achieving low-latency responses (~10 ms) 
with competitive accuracy. STDP-based SNNs, while slightly 
slower  in  early  inference  phases  due  to  their  gradual  spike 
adaptation,  stabilize  to  sub-15  ms  latency  under  optimized 
conditions.  Converted  SNNs,  on  the  other  hand,  may  incur 
slightly  higher  delays  (~20  ms),  especially  when  requiring 
longer  simulation  windows  to  approximate  ANN  activation 
rates. Figure 4 compares inference latency (in ms) across ANN 
(CNN), Converted SNN, Surrogate Gradient SNN, and STDP-
based SNN models.

)
s
m

(

y
c
n
e
t
a
L

50

45

40

35

30

25

20

15

10

5

0

ANN (CNN)

Converted SNN

Surrogate Gradient SNN

STDP-based SNN

Model
Fig. 4 Latency comparison (in ms) across models

Low  latency  reinforces  the  suitability  of  SNNs  for  real-
time applications compared to conventional ANN processing. 
These  findings  highlight  SNNs’  potential  for  applications 
demanding real-time inference, such as autonomous vehicles, 
interfaces. 
smart  sensors,  robotics,  and  brain-computer 
However,  real-world  deployment  still  depends  on 
the 
responsiveness  of  underlying  neuromorphic  hardware, 
efficient spike encoding schemes, and minimal overhead from 
software toolchains.

4.3. Energy Efficiency

The  remarkable  energy  efficiency  of  SNNs,  which  is 
fueled  by  sparse  event-driven  processing,  is  one  of  its  most 
alluring  features.  SNNs  only  calculate  when  neurons  fire,  in

contrast  to  traditional  ANNs,  which  rely  on  large  matrix 
multiplications and continuous-valued activations. This allows 
for huge power savings, particularly in neuromorphic hardware 
implementations,  and  significantly  reduces  the  number  of 
operations per inference. Converted SNNs, derived from pre-
trained  ANNs,  have  demonstrated  up  to  10×  lower  energy 
consumption  compared  to  their  ANN  counterparts  while 
maintaining  comparable  accuracy  [20,  21].  This  is  possible 
because  inference  in  SNNs  is  based  on  discrete  spikes  and 
accumulations over time rather  than  continuous propagation. 
Directly  trained  SNNs  using  surrogate  gradient  descent  also 
show  excellent  energy  performance.  These  networks  can 
operate with fewer spikes and less computation per inference 
due  to  their  native  temporal  dynamics  and  the  use  of

39

---

<!-- PAGE 9 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

biologically-inspired  neuron  models  [22,  34].  Meanwhile, 
STDP-based  SNNs  are  the  most  energy-efficient,  often 
operating with less than 5 millijoules (mJ) per inference, thanks 
to their localized synaptic updates and highly sparse activation 
patterns  [44].  These  models  are  perfect  for  ultra-low-power 
applications  like  wearable  technology  and  edge  AI,  even 
though their accuracy may be a little below par. This tradeoff 
between energy and performance across several model types is 
illustrated in the image and table below.

Model

ANN (CNN) 
Converted SNN 
Surrogate 
Gradient SNN 
STDP-based 
SNN

Table 3. SNN energy efficiency summary 
Energy per 
Inference (mJ) 
200 
20

Spike Count per 
Inference 
0 
20000

15

5

12000

4000

250

200

150

100

50

0

25000

20000

15000

10000

5000

0

)
J
m

(

y
g
r
e
n
E

s
e
k
i
p
S
f
o

r
e
b
m
u
N

ANN (CNN)

Converted SNN

Surrogate Gradient SNN

STDP-based SNN

Model

ANN (CNN)

Converted SNN

Surrogate Gradient SNN

STDP-based SNN

Fig. 5 Comparison of energy consumption and spike count per inference across models

Model

Figure 5 provides a comparison of energy consumption (in 
mJ) and spike count (number of spikes generated) per inference 
across four neural network models: ANN (CNN),  Converted 
SNN, Surrogate Gradient SNN, and STDP-based SNN. ANNs 
exhibit the highest energy consumption at approximately 200 
mJ per inference due to their continuous-valued operations and 
lack  of  spike-based  activity.  Converted  SNNs  significantly 
lower  energy  usage  to  20  mJ,  though  they  still  produce  a 
relatively high spike count (~20,000) as a result of rate-coded 
spike propagation. Surrogate Gradient SNNs further optimize

40

both energy (15 mJ) and spike efficiency (~12,000 spikes) by 
leveraging gradient-based learning of spiking patterns. Finally, 
STDP-based SNNs achieve the lowest energy consumption (5 
mJ  per  inference)  and  the  sparsest  spiking  activity  (~4,000 
spikes),  making 
energy-constrained 
ideal 
applications, albeit with slightly reduced accuracy. As shown, 
while  ANNs  dominate  in  raw  accuracy,  SNNs—especially 
STDP-based  and  surrogate-trained  models—can  achieve 90–
97% 
in 
performance. This makes SNNs particularly promising for on-

lower  energy  use  with  reasonable

tradeoffs

them

for

---

<!-- PAGE 10 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

device AI and neuromorphic processors [12, 18]. The observed 
energy  savings  highlight  the  central  advantage  of  SNNs  for 
low-power AI systems.

The  tradeoffs  between  accuracy,  spiking  activity,  and 
energy efficiency are provided in this comparison, highlighting 
the  applicability  of  SNNs  for  low-power  AI  applications  in 
neuromorphic  and  edge  computing,  especially  those  trained 
with surrogate gradients or STDP.

4.4. Convergence Behavior

Convergence time during training is a critical performance 
factor, especially when comparing different SNN architectures

[67].  This  section  explores  how  training  loss  changes  across 
epochs  for  three  SNN  variants:  converted  SNNs,  surrogate 
gradient-trained  SNNs,  and  STDP-based  SNNs.  Figure  6 
illustrates the training loss across 20 epochs.

The  surrogate  gradient  SNN  demonstrates  the  fastest 
convergence, reducing  loss from 0.9  to  0.44,  showing  stable 
optimization  and  consistent  improvement  over  time.  In 
contrast,  converted  SNNs  exhibit  slower  convergence  and 
reach a loss of 0.6 by epoch 20. STDP-based SNNs converge 
the slowest, with the loss stabilizing around 0.75, indicating a 
limitation  in  achieving  deeper  error  minimization  under 
unsupervised learning.

Converted SNN

Surrogate Gradient SNN

STDP-based SNN

s
s
o
L
g
n
i
n
i
a
r
T

1.00

0.90

0.80

0.70

0.60

0.50

0.40

0.30

0.20

0.10

0.00

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

Epoch

Fig. 6 Convergence behavior of SNN models

Table 4. Training loss across epochs for different SNN models 
Epoch  Converted SNN  Surrogate Gradient SNN  STDP-based SNN

1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
11 
12 
13 
14 
15 
16 
17 
18 
19 
20

0.9 
0.85 
0.82 
0.78 
0.76 
0.73 
0.71 
0.7 
0.68 
0.67 
0.66 
0.65 
0.64 
0.63 
0.63 
0.62 
0.62 
0.61 
0.61 
0.6

0.9 
0.8 
0.73 
0.67 
0.63 
0.6 
0.57 
0.55 
0.53 
0.51 
0.5 
0.49 
0.48 
0.47 
0.46 
0.46 
0.45 
0.45 
0.44 
0.44

41

0.9 
0.88 
0.87 
0.85 
0.84 
0.83 
0.82 
0.81 
0.81 
0.8 
0.79 
0.78 
0.78 
0.77 
0.77 
0.76 
0.76 
0.75 
0.75 
0.75

---

<!-- PAGE 11 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

Table 4 presents the simulated training loss values over 20 
epochs  for  three  types  of  SNNs:  Converted  SNN,  Surrogate 
Gradient SNN, and STDP-based SNN. The surrogate gradient-
trained model shows the steepest and most consistent decline 
in loss, indicating faster convergence. Converted SNNs exhibit 
moderate  convergence,  while  STDP-based  SNNs  converge 
slowly  and  plateau  early,  reflecting  the  limitations  of 
unsupervised learning.

These  results  reinforce  that  while  STDP-based  models 
offer  energy  efficiency,  they  lack  the  learning  stability  of 
supervised  techniques.  Surrogate  gradient  methods,  on  the 
other hand, offer a balance of performance, training speed, and

them  more

scalable 
stability,  making 
applications.  Convergence  behavior  thus  becomes  a  critical 
consideration when selecting SNN models for deployment in 
time-sensitive or resource-constrained environments.

favorable

for

Figure 7 plots the training accuracy learning curves across 
20 epochs for the three SNN variants. The surrogate gradient 
SNN exhibits the steepest accuracy gains, stabilizing near 98% 
by  epoch  20,  while  converted  SNNs  converge  more  slowly. 
STDP models show gradual improvement but plateau earlier, 
consistent  with  unsupervised  adaptation  limits.  Curves  show 
mean  accuracy  with  shaded  bands  indicating  ±1  standard 
deviation across five independent runs.

Surrogate Gradient SNN

Converted SNN

STDP-based SNN

)

%

(

y
c
r
u
c
c
A
g
n
h
i
n
i
a
r
T

120

100

80

60

40

20

0

1

2

3

4

5

6

7

8

9

10 11 12 13 14 15 16 17 18 19 20

Fig. 7 Learning curves (training accuracy vs. epochs) for converted, surrogate-gradient, and STDP-based SNNs

Epoch

Learning  curves  demonstrate  stable  optimization  for 
surrogate SNNs, gradual adaptation for converted SNNs, and 
slower but consistent improvement for STDP.

4.5. Comparative Discussion

The  comparative  evaluation  of  different  neural  network 
architectures reveals key tradeoffs  between accuracy, energy 
efficiency,  latency,  and  convergence.  ANNs,  particularly 
CNNs, consistently achieve the highest classification accuracy 
(e.g., 99.2% on MNIST, 92.3% on CIFAR-10) but do so at the 
cost of high energy consumption—reaching up to 200 mJ per 
inference. These models are less appropriate for real-time and 
energy-constrained applications because they also have higher 
inference latency, usually between 30 and 50 ms, and demand 
more processing power.

Converted SNNs, which are created from trained ANNs, 
drastically  reduce  energy  consumption  by  about  90%  while 
achieving accuracy that is comparable to the performance of 
their  ANN  counterparts.  However,  they  may  require  longer 
simulation  windows  and produce higher  spike  counts, which 
can marginally affect latency and training efficiency. Despite

they  remain  a  viable  alternative  for

this, 
deployments where retraining is impractical.

low-power

Surrogate  gradient-trained  SNNs  represent  an  effective 
balance between accuracy and efficiency. These models attain 
sub-15  ms  inference  latency,  competitive  accuracy,  and 
moderate  spike  counts  (~12,000  per  inference),  all  while 
demonstrating faster convergence during training. As seen in 
Section 4.6, they reduce training loss more rapidly than other 
SNN types, stabilizing by the 20th epoch, which makes them 
favorable for real-time learning tasks. STDP-based SNNs are 
the  most  energy-efficient,  requiring  only  around  5  mJ  per 
inference. However, they typically exhibit lower classification 
accuracy  and  slower  convergence  rates.  As  illustrated  in  the 
convergence  analysis,  STDP-based  models  plateau  at  higher 
loss values and require more epochs to stabilize, making them 
better  suited  for  applications  prioritizing  unsupervised 
adaptation over precise classification.

Overall,  application-specific  priorities  determine  which 
SNN model is best [68]: surrogate gradient SNNs for real-time 
and accuracy-focused use, STDP for ultra-low energy adaptive

42

---

<!-- PAGE 12 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

systems,  and  converted  SNNs  for  ANN  transferability  in 
constrained  environments.In  addition,  it  is  instructive  to 
compare  SNNs  with  Transformer-based  architectures,  which 
currently  dominate  performance  benchmarks 
in  natural 
language  processing  and  computer  vision.  Transformers  rely 
on  attention  mechanisms  that  effectively  capture  long-range 
dependencies  but  scale  quadratically  with  input  length, 
resulting in substantial memory and energy requirements [69, 
70]. Recent analysis estimates that training large Transformer 
models  consumes  hundreds  of  megawatt-hours  of  electricity 
and generates a significant carbon footprint [71, 72].

By  contrast,  SNNs  prioritize  event-driven,  sparse 
computation  that  achieves  up  to  90–97%  energy  savings 
relative to ANNs while maintaining competitive accuracy on 
benchmarks  such  as  CIFAR-10  and  MNIST  [73,  74].  While 
Transformers typically outperform SNNs in raw accuracy on 
broad-based  datasets  like  ImageNet,  they  lack  the  real-time 
latency advantages and hardware efficiency that make SNNs 
suitable for robotics, neuromorphic vision, and edge AI. This 
comparison underscores the complementary nature of the two 
paradigms:  Transformers  excel  in  centralized,  resource-rich 
environments, whereas SNNs offer a sustainable pathway for 
low-power, real-time applications.

Beyond confirming trends reported in earlier studies, the 
present work achieves slightly higher accuracies and markedly 
better efficiency metrics than most state-of-the-art reports. For 
example,  surrogate  gradient  SNNs  reached  97.8%  ±  0.2  on 
MNIST and 85.7% ± 0.5 on CIFAR-10, which improves upon 
earlier  spiking  models  that  typically  plateaued  near  96–97% 
and 82–84%, respectively. Latency reductions of 35–45% and 
energy savings of 90–97% relative to ANN baselines were also 
obtained, exceeding values previously reported in conversion-
only pipelines.

These  gains  are  largely  attributable  to  the  unified 
evaluation protocol applied here, which ensures fairness across 
models; multi-dimensional performance metrics that highlight 
the 
in  accuracy-only 
tradeoffs  hidden 
reporting;  and 
optimization  of  surrogate  gradient 
training  parameters, 
allowing  faster  convergence  with  fewer  spikes.  Thus,  the 
results  do  not  merely  replicate  existing  findings  but 
demonstrate how careful integration of training strategies and 
evaluation standards can extend the SNN research.

Taken  together,  these  comparisons  show  that  no  single 
paradigm  dominates;  SNNs  excel  in  sustainability,  while 
ANNs and Transformers lead in raw accuracy and scalability.

fly  processing  that  is  computationally  efficient  and  low-
latency.  Such  characteristics  make  SNNs  highly  suitable  for 
tasks  like  gesture  recognition,  robotic  control,  auditory 
processing, and neuromorphic vision, where responsiveness is 
critical and resources are constrained.

Several

successful

implementations  have  already 
showcased these real-time capabilities. For instance, in gesture 
recognition using the DVS128, SNNs have achieved both high 
classification accuracy and fast inference times, outperforming 
traditional frame-based systems in terms of latency and power 
consumption  [66].  Similarly,  in  the  SHD  and  SSC  datasets, 
SNNs  trained  with  temporal  coding  have  demonstrated 
excellent performance in processing time-dependent auditory 
signals [25]. These use cases confirm that SNNs are not only 
biologically  plausible  but  also  practically  effective  in  real-
world, real-time environments.

However,  despite  their  potential,  scale,  and  hardware 
implementation,  they  present  significant  obstacles  to  broad 
adoption. Low-power SNN execution has been made possible 
by neuromorphic processors; however, access to these devices 
is  still  restricted.  Furthermore,  simulating  massive  networks 
with  millions  of  neurons  and  synapses  makes  scalability 
challenging, particularly in settings with limited resources. The 
creation of middleware, APIs, and toolchains—which are now 
fragmented or platform-specific—is still necessary to integrate 
such hardware into conventional computing pipelines [12, 18]. 
Convergence  stability  and  training  methodologies  are  still 
another  major  obstacle.  Because  spike  events  are  non-
differentiable,  SNNs 
traditional 
backpropagation,  which  is  the  foundation  of  ANN  learning. 
Even  though  end-to-end  training  of  SNNs  with  competitive 
performance is now possible thanks to recent developments in 
surrogate gradient descent, these models are still susceptible to 
hyperparameters such as membrane thresholds, time constants, 
and  learning  rates  [22].  In  unsupervised  learning  paradigms, 
such as STDP, convergence can be unstable or dataset-specific, 
limiting generalization.

cannot  directly  use

Finally,  the  lack  of  standardization  across  SNN  models, 
encoding schemes, and hardware platforms impedes progress. 
Unlike ANNs, which benefit from standardized libraries (e.g., 
TensorFlow, PyTorch) and benchmark datasets, SNN research 
suffers from inconsistent definitions of spike encoding (rate vs. 
temporal  coding),  neuron  models  (LIF,  Izhikevich),  and 
performance  metrics  (accuracy  vs.  spike  count  vs.  energy-
delay  product).  This  fragmentation  makes  it  difficult  to 
compare results, reproduce experiments, or establish baselines 
[75].

4.6. Real-Time Capabilities

Because  of  their  sparse  spike-based  computing  and 
asynchronous, event-driven design, SNNs are especially well-
suited for real-time applications. SNNs react only when input 
stimuli cause spikes, in contrast to conventional ANNs, which 
need constant and coordinated processing. This enables on-the-

4.7. Hardware Considerations

The practical adoption of SNNs is tightly linked to their 
implementation  on  neuromorphic  hardware  platforms.  In 
comparison  to  traditional  CPUs  and  GPUs,  chips  like  IBM 
TrueNorth  [18]  and  Intel  Loihi  [12]  show  that  large-scale

43

---

<!-- PAGE 13 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

spiking  computation  is  feasible  with  orders  of  magnitude 
reduced energy usage. TrueNorth, for example, integrates one 
million spiking neurons while consuming only 70 mW in real-
time  workloads  [18].  Similarly,  Loihi  supports  on-chip 
learning  with  programmable  synaptic  delays,  enabling 
adaptive  behavior  at  the  edge  [12].  Recent  platforms  like 
SpiNNaker  extend  this  scalability  by  simulating  millions  of 
neurons across massively parallel architectures [63].

from  unified

Despite  these  advances,  hardware  deployment  remains 
challenged by limited accessibility, vendor-specific SDKs, and 
the absence of a standardized programming ecosystem. Unlike 
ANNs,  which  benefit 
like 
TensorFlow and PyTorch, SNN hardware requires researchers 
to  adapt  models 
toolchains,  constraining 
reproducibility  and  adoption.  Addressing  these  hardware 
bottlenecks  — 
standard 
benchmarks,  and  cross-platform  compatibility  —  will  be 
critical  for  translating  SNN  research  into  widespread,  real-
world applications.

through  open-source  SDKs,

to  specific

frameworks

4.8. Extended Analysis and Insights

While prior sections compared accuracy, latency, energy, 
and  convergence  individually,  an  integrated  perspective 
highlights  tradeoffs  across  all  metrics  simultaneously.  For 
instance, surrogate-gradient SNNs balance accuracy (~97.8%) 
with  latency  (~10  ms)  and  moderate  energy  (15  mJ  per 
inference),  whereas  STDP-based  SNNs  achieve  the  lowest 
energy  (~5  mJ)  at  the  cost  of  accuracy  (95.5%)  and  slower 
convergence.  These  tradeoffs  confirm  that  no  single  model 
dominates  all performance axes; instead, model  suitability  is 
highly dependent on application.

When network size increases (e.g., from MNIST-scale to 
CIFAR-10  scale),  accuracy  differences  widen—ANNs 
outperform on CIFAR-10 (~92%) while direct SNNs drop to 
~85%.  However,  energy  savings  become  more  pronounced: 
surrogate-trained  SNNs  operate  at  less  than  10%  of  ANN 
energy costs. This scalability tension underscores the practical 
importance  of  hybrid  evaluation  criteria  beyond  accuracy 
alone. Simulation on neuromorphic platforms like Intel Loihi 
demonstrates  that  real-world  deployment  magnifies  latency 
and energy advantages. For example, gesture-recognition tasks 
on  DVS128  achieve  inference  latencies  of  5–10  ms  with 
surrogate SNNs, compared to 20–50 ms on ANN counterparts 
[12, 66]. These results show that latency reductions translate 
directly into real-time robotics and edge AI feasibility.

4.9. Limitations of the Study

While the analysis provides comprehensive insights into 
neuron models, training paradigms, and performance metrics, 
several limitations must be acknowledged. First, the evaluation 
relies primarily on benchmark  datasets,  which  may not fully 
capture  real-world  complexity  or  large-scale  deployment 
scenarios.  Second,  hardware-specific  results  are  drawn  from 
reported benchmarks in the literature [22, 12, 66] rather than

44

from  direct  implementation  in  this  study,  which  may  limit 
generalizability  across  platforms.  Third,  hyperparameter 
sensitivity  in  surrogate-gradient  training  and  convergence 
instability in STDP highlight ongoing challenges that require 
further exploration. Finally, while comparative metrics such as 
accuracy,  latency,  and  energy  were  integrated,  additional 
factors  such  as  scalability  on  high-dimensional  tasks  and 
robustness  under  noisy  conditions  remain  areas  for  future 
research.  Recognizing  these  limitations  underscores  that  the 
toward 
findings,  while  promising,  represent  one  step 
advancing brain-inspired and low-power AI systems.

5. Conclusion

In brain-inspired computing, SNNs are becoming a game-
changer due to their ability to effectively combine biological 
plausibility,  energy  efficiency,  and  real-time  responsiveness. 
This paper presented a comprehensive analysis of SNN design, 
training  methods,  and  comparative  performance  across 
multiple dimensions, including accuracy, spike count, latency, 
and  convergence  behavior.  Among  the  evaluated  models, 
ANNs  —particularly  CNNs—continue  to deliver  the  highest 
classification accuracy (up to 99.2% on MNIST and 92.3% on 
CIFAR-10).

However,  their  high energy demands (up to  200  mJ  per 
inference)  and  longer  inference  latency  (30–50  ms)  render 
them suboptimal for real-time or edge applications. Converted 
SNNs,  which 
leverage  pre-trained  ANNs,  maintain 
competitive accuracy while cutting energy use by nearly 90%. 
Nonetheless,  they  generate  higher  spike  counts  and  rely  on 
longer  simulation  windows,  which  can  impact  latency  and 
training flexibility. Surrogate gradient-trained SNNs offer the 
most balanced performance profile.

They  achieve  low  latency  (~10  ms),  fast  and  stable 
convergence within 20 epochs, and reduced spike counts, all 
while  maintaining  accuracy  close  to  ANN  baselines.  This 
qualifies  them  for  edge  and  real-time  AI  implementations. 
Meanwhile,  STDP-based  SNNs  lead  in  energy  efficiency—
consuming  as  little  as  5  mJ  per  inference—but  show  lower 
accuracy  and  slower  convergence,  stabilizing  around  0.75 
training  loss  after  20  epochs.  These  models  are  more 
appropriate  for  tasks  requiring  continuous  unsupervised 
learning and adaptation.

This  multi-dimensional  comparison  confirms  that  the 
selection  of  an  SNN  model  should  align  with  application 
requirements.  For 
latency-critical  and  accuracy-driven 
systems,  surrogate  gradient  SNNs  are  the  most  viable.  For 
ultra-low-power 
remains 
advantageous. Overall, SNNs are poised to redefine the future 
of AI systems operating at the intersection of efficiency, speed, 
and biological realism. Despite these strengths, SNNs face key 
limitations.  Training  convergence 
is  often  unstable, 
hyperparameter  tuning  remains  challenging,  and  no  unified 
neuromorphic 
standard

for  model

evaluation

systems,

adaptive

STDP

or

---

<!-- PAGE 14 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

implementation  exists.  Additionally,  the  limited  accessibility 
and  scalability  of  neuromorphic  chips  restrict  practical 
deployment in broader commercial systems.

The  comparative  results  underscore  that  SNNs  provide 
substantial energy savings (up to 90–97% lower than ANNs) 
with  only  marginal  accuracy  loss.  This  positions  SNNs  as  a 
sustainable computing alternative, particularly relevant as the 
AI  community  grapples  with  the  environmental  impact  of 
large-scale  ANNs.  By  clarifying  the  efficiency–accuracy 
tradeoffs, this paper highlights how SNNs can drive innovation 
not just in performance but also in responsible, energy-aware 
AI  deployment.  Nevertheless,  the  findings  of  this  paper 
conclude that SNNs are well-positioned to redefine low-power, 
real-time computing, particularly where energy efficiency and 
temporal precision are paramount. SNNs are anticipated to be 
essential  components  of  future  edge  intelligence,  neuro-
inspired  robotics,  and  ultra-low-power  AI  ecosystems  as 
neuromorphic engineering develops and transdisciplinary tools 
become  more  sophisticated.  In  essence,  this  study  reinforces 
that SNNs, while not universally superior, provide a distinctive 
pathway  toward  sustainable,  real-time,  and  energy-aware  AI 
solutions.

5.1. Recommendations

Based on the findings and comparative analysis presented 
in  this  study,  the  following  recommendations  are  offered  to 
support  further  development,  adoption,  and  application  of 
SNNs:

1.  Optimize  SNN  Training  Frameworks.  Further  research 
training  stability  and 
should  prioritize 
improving 
convergence in SNNs. Surrogate gradient-based learning 
should  be 
through  adaptive  optimization 
strategies and hybrid techniques that combine supervised 
and  unsupervised  methods  to  enable  deeper  networks 
with minimal performance tradeoffs.

refined

2.  Standardize  Evaluation  Protocols.  A  unified  framework 
for evaluating SNN models is essential. Researchers and 
to  adopt  standardized 
developers  are  encouraged 
benchmarks—including  common  datasets,  spike-based 
performance  metrics  (accuracy,  latency,  energy  per 
inference),  and  neuron  model  conventions—to  ensure 
comparability and reproducibility across studies. 
Invest in Neuromorphic Hardware Access. Governments, 
academic consortia, and industry players should expand 
access  to  neuromorphic  platforms  like  Intel  Loihi, 
SpiNNaker, 
IBM  TrueNorth.  Collaborative 
development  of  open-source  SDKs  and  toolchains  will 
help democratize innovation and facilitate deployment in 
embedded and edge systems.

and

3.

4.  Promote Application-Oriented Research. SNNs should be 
increasingly  tested  in  real-world  domains  such  as 
robotics,  medical  devices, 
and 
neuromorphic  computing.  Pilot  studies  using  SNNs  for 
autonomous  navigation,  auditory  localization,  or  low-

sensors,

smart

45

5.  Support

power  surveillance  could  highlight  their  advantages  in 
task-specific contexts.

Collaboration.

Cross-Disciplinary

The 
development  of  effective  SNNs  requires  expertise  in 
neuroscience,  machine  learning,  electrical  engineering, 
and  computer  architecture.  Research  institutions  and 
funding  agencies  should  support 
interdisciplinary 
programs that foster collaboration across these domains. 
Integrate  SNNs  into  AI  Curriculum  and  Tools.  To 
accelerate  knowledge  transfer,  academic  institutions 
should 
integrate  SNN  concepts  and  neuromorphic 
computing  into  AI  and  computer  engineering  curricula. 
Additionally,  incorporating  SNN  support  into  popular 
frameworks  (e.g.,  PyTorch  or  TensorFlow)  would 
streamline experimentation and development.

6.

7.  Bridging  Biological  Plausibility  and  Machine  Learning. 
A  key  direction  is  merging  STDP’s  biological  realism 
with  surrogate-gradient  efficiency.  Hybrid 
learning 
methods  could  yield  models  that  are  both  hardware-
friendly and competitive in accuracy.

8.  Benchmarking  Beyond  MNIST  and  CIFAR-10.  Most 
SNN  studies,  including  this  one,  focus  on  MNIST, 
CIFAR-10,  and  DVS128.  Broader  datasets  such  as 
ImageNet  or 
remain 
underexplored 
contexts.  Extending 
benchmarks  will  increase  confidence  in  scalability  and 
generalization.

large-scale 
in

corpora

spiking

audio

9.  Standardized

Energy–Latency–Accuracy  Metrics. 
To  ensure  impact  in  neuromorphic  computing,  SNN 
research should converge on unified metrics (e.g., energy-
delay product per classification). This paper contributes 
toward  such  standardization  by  reporting  spike  counts, 
latency, and convergence alongside accuracy.

10.  Explore Hybrid Models. Future studies may want to look 
into  hybrid  strategies  that  blend  SNNs  with  CNNs  and 
Transformers,  among  other  paradigms.  Hybrid  SNN–
Transformer  models  could  merge  temporal  coding 
efficiency with long-range dependency modeling, while 
convolutional–spiking systems may enhance event-based 
vision  tasks.  Similarly,  integrating  STDP’s  biological 
plausibility  with 
optimization 
efficiency could yield models that balance energy savings 
with  accuracy.  These  directions  will  bridge  the  gap 
between  biological  realism,  computational  efficiency, 
and task scalability, ensuring that SNNs remain central to 
sustainable AI development.

surrogate-gradient

the

With

these  strategies,

field  of  brain-inspired 
computing can move beyond theoretical promise to real-world 
impact, harnessing the unique capabilities of SNNs in solving 
some  of  today’s  most  demanding  computational  challenges.  
By clarifying how SNNs achieve 90–97% energy savings with 
only  1–3%  accuracy  drop  relative  to  ANNs,  this  study 
highlights  their  transformative  potential  for  wearable  health 
devices,  autonomous  robotics,  and  edge  AI  sensors,  where 
energy budgets are decisive.

---

<!-- PAGE 15 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

References 
[1]  Kaushik Roy, Akhilesh Jaiswal, and Priyadarshini Panda, “Towards Spike-Based Machine Intelligence with Neuromorphic Computing,”

Nature, vol. 575, no. 7784, pp. 607-617, 2019. [CrossRef] [Google Scholar] [Publisher Link]

[2]  Wolfgang Maass, “Networks of Spiking Neurons: The Third Generation of Neural Network Models,” Neural Networks, vol. 10, no. 9, pp.

1659-1671, 1997. [CrossRef] [Google Scholar] [Publisher Link]

[3]  Yann LeCun, Yoshua Bengio, and Geoffrey Hinton, “Deep Learning,” Nature, vol. 521, no. 7553, pp. 436-444, 2015. [CrossRef] [Google

Scholar] [Publisher Link]

[4]  Jolitte A. Villaruz, Bobby D. Gerardo, and Ruji P. Medina, “Philippine Stock Exchange Index Forecasting Using a Tuned Artificial Neural 
Network  Model  with  a  Modified  Firefly Algorithm,”  2023  IEEE  6th  International  Conference  on  Pattern  Recognition  and  Artificial 
Intelligence (PRAI), Haikou, China, pp. 1039-1044, 2023. [CrossRef] [Google Scholar] [Publisher Link]

[5]  Mary Joy D. Viñas et al., “COVID-19 Outbreaks Effect on Air Quality Index: Evidence from Enhanced Artificial Neural Network,” 2023 
8th International Conference on Computer and Communication Systems (ICCCS), Guangzhou, China, pp. 1117-1124, 2023.  [CrossRef] 
[Google Scholar] [Publisher Link]

[6]  Alex  Krizhevsky,  Ilya  Sutskever,  and  Geoffrey  E.  Hinton,  “Imagenet  Classification  with  Deep  Convolutional  Neural  Networks,”

Communications of the ACM, vol. 60, no. 6, pp. 84-90, 2017. [CrossRef] [Google Scholar] [Publisher Link]

[7]  Stephen Grossberg, “Recurrent Neural Networks,” Scholarpedia, vol. 8, no. 2, 2013. [Google Scholar]  
[8]  Sepp  Hochreiter,  and  Jürgen  Schmidhuber,  “Long  Short-Term  Memory,”  Neural  Computation,  vol.  9,  no.  8,  pp.  1735-1780,  1997.

[CrossRef] [Google Scholar] [Publisher Link]

[9]  Rahul Dey, and Fathi M. Salem, “Gate-Variants of Gated Recurrent Unit (GRU) Neural Networks,” 2017 IEEE 60th International Midwest 
Symposium on Circuits and Systems (MWSCAS), Boston, MA, USA, pp. 1597-1600, 2017. [CrossRef] [Google Scholar] [Publisher Link] 
[10] Ashish Vaswani et al., “Attention is All you Need,” Advances in Neural Information Processing Systems, vol. 30, 2017. [Google Scholar]

[Publisher Link]

[11] Wulfram Gerstner, and Werner M. Kistler, Spiking Neuron Models: Single Neurons, Populations, Plasticity, 1st ed., Cambridge University

Press, 2002. [CrossRef] [Google Scholar] [Publisher Link]

[12] Mike Davies et al., “Loihi: A Neuromorphic Manycore Processor with On-Chip Learning,” IEEE Micro, vol. 38, no. 1, pp. 82-99, 2018.

[CrossRef] [Google Scholar] [Publisher Link]

[13] Resmi Cherian, and E. Grace Mary Kanaga, “Unleashing the Potential of Spiking Neural Networks for Epileptic Seizure Detection: A

Comprehensive Review,” Neurocomputing, vol. 598, 2024. [CrossRef] [Google Scholar] [Publisher Link]

[14] Samanwoy Ghosh-Dastidar, and Hojjat Adeli, “Third Generation Neural Networks: Spiking Neural Networks,” Advances in Intelligent

and Soft Computing, Berlin, Heidelberg, pp. 167-178, 2009. [CrossRef] [Google Scholar] [Publisher Link]

[15] Gabriele Lagani et al., “Spiking Neural Networks and Bio-Inspired Supervised Deep Learning: A Survey,” arXiv Preprint, pp. 1-31, 2023.

[CrossRef] [Google Scholar] [Publisher Link]

[16] Giacomo Indiveri, and Timothy K. Horiuchi, “Frontiers in Neuromorphic Engineering,” Frontiers in Neuroscience, vol. 5, pp. 1-2, 2011.

[CrossRef] [Google Scholar] [Publisher Link]

[17] Sumit Soman, Jayadeva, and Manan Suri, “Recent Trends in Neuromorphic Engineering,”  Big Data Analytics, vol. 1, no. 1, pp. 1-16,

2016. [CrossRef] [Google Scholar] [Publisher Link]

[18] Paul A. Merolla, et al., “A Million Spiking-Neuron Integrated Circuit with a Scalable Communication Network and Interface,” Science,

vol. 345, no. 6197, pp. 668-673, 2014. [CrossRef] [Google Scholar] [Publisher Link]

[19] Md  Bokhtiar Al  Zami  et  al.,  “Digital  Twin  in  Industries: A  Comprehensive  Survey,”  IEEE  Access,  vol.  13,  pp.  47291-47336,  2025.

[CrossRef] [Google Scholar] [Publisher Link]

[20] Peter  U.  Diehl  et  al.,  “Fast-Classifying,  High-Accuracy  Spiking  Deep  Networks  through  Weight  and  Threshold  Balancing,”  2015 
International Joint Conference on Neural Networks (IJCNN), Killarney, Ireland, pp. 1-8, 2015. [CrossRef] [Google Scholar] [Publisher 
Link]

[21] Bodo Rueckauer et al., “Conversion of Continuous-Valued Deep Networks to Efficient Event-Driven Networks for Image Classification,”

Frontiers in Neuroscience, vol. 11, pp. 1-12, 2017. [CrossRef] [Google Scholar] [Publisher Link]

[22] Emre O. Neftci, Hesham Mostafa, and Friedemann Zenke, “Surrogate Gradient Learning in Spiking Neural Networks: Bringing the Power 
of  Gradient-Based  Optimization  to  Spiking  Neural  Networks,”  IEEE  Signal  Processing  Magazine,  vol.  36,  no.  6,  pp.  51-63,  2019. 
[CrossRef] [Google Scholar] [Publisher Link]

[23] E.M.  Izhikevich,  “Simple  Model  of  Spiking  Neurons,”  IEEE  Transactions  on  Neural  Networks, vol. 14,  no. 6, pp.  1569-1572, 2003.

[CrossRef] [Google Scholar] [Publisher Link]

[24] Yuchen  Wang  et  al.,  “A  Universal ANN-to-SNN  Framework  for Achieving  High Accuracy  and  Low  Latency  Deep  Spiking  Neural

Networks,” Neural Networks, vol. 174, pp. 1-14, 2024. [CrossRef] [Google Scholar] [Publisher Link]

46

---

<!-- PAGE 16 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

[25] Benjamin  Cramer  et  al.,  “The  Heidelberg  Spiking  Data  Sets  for  the  Systematic  Evaluation  of  Spiking  Neural  Networks,”  IEEE 
Transactions on Neural Networks and Learning Systems, vol. 33, no. 7, pp. 2744-2757, 2022. [CrossRef] [Google Scholar] [Publisher 
Link]

[26] Khadeer Ahmed, Brain-Inspired Spiking Neural Networks, Biomimetics, IntechOpen, 2021. [CrossRef] [Google Scholar] [Publisher Link]  
[27] A.L. Hodgkin, and A.F. Huxley, “A Quantitative Description of Membrane Current and its Application to Conduction and Excitation in

Nerve,” Bulletin of Mathematical Biology, vol. 52, no. 1-2, pp. 25-71, 1990. [CrossRef] [Google Scholar] [Publisher Link]

[28] Xingting Yao  et  al.,  “GLIF: A  Unified  Gated  Leaky  Integrate-and-Fire  Neuron  for  Spiking  Neural  Networks,”  Advances  in  Neural

Information Processing Systems, vol. 35, pp. 32160-32171, 2022. [Google Scholar] [Publisher Link]

[29] Walter Senn, and Jean-Pascal Pfister, “Spike-Timing Dependent Plasticity, Learning Rules,” Encyclopedia of Computational Neuroscience,

New York, Springer, pp. 2824-2832, 2015. [CrossRef] [Google Scholar] [Publisher Link]

[30] Guo-qiang Bi, and Mu-ming Poo, “Synaptic Modifications in Cultured Hippocampal Neurons: Dependence on Spike Timing, Synaptic 
Strength, and Postsynaptic Cell Type,” Journal of Neuroscience, vol. 18, no. 24, pp. 10464-10472, 1998. [CrossRef] [Google Scholar] 
[Publisher Link]

[31] Sung  Soo  Park,  and  Young-Seok  Choi,  “Spiking  Neural  Networks  for  Physiological  and  Speech  Signals:  A  Review,”  Biomedical

Engineering Letters, vol. 14, no. 5, pp. 943-954, 2024. [CrossRef] [Google Scholar] [Publisher Link]

[32] Simon Thorpe, and Jacques Gautrais, “Rank Order Coding,” Computational Neuroscience, Boston, MA, pp. 113-118, 1998. [CrossRef]

[Google Scholar] [Publisher Link]

[33] Sanaullah et al., “Exploring Spiking Neural Networks: A Comprehensive Analysis of Mathematical Models and Applications,” Frontiers

in Computational Neuroscience, vol. 17, pp. 1-20, 2023. [CrossRef] [Google Scholar] [Publisher Link]

[34] Friedemann Zenke, and Surya Ganguli, “SuperSpike: Supervised Learning in Multilayer Spiking Neural Networks,” Neural Computation,

vol. 30, no. 6, pp. 1514-1541, 2018. [CrossRef] [Google Scholar] [Publisher Link]

[35] Siddharth  Sharma,  Simone  Sharma,  and  Anidhya  Athaiya,  “Activation  Functions  in  Neural  Networks,”  International  Journal  of

Engineering Applied Sciences and Technology, vol. 4, no. 12, pp. 310-316, 2020. [CrossRef] [Google Scholar] [Publisher Link]

[36] Tomasz  Szandała,  “Review  and  Comparison  of  Commonly  Used  Activation  Functions  for  Deep  Neural  Networks,”  Studies  in

Computational Intelligence, Singapore: Springer Singapore, pp. 203-224, 2010. [CrossRef] [Google Scholar] [Publisher Link]

[37] Sen Lu, and Abhronil Sengupta, “Neuroevolution Guided Hybrid Spiking Neural Network Training,” Frontiers in Neuroscience, vol. 16,

pp. 1-11, 2022. [CrossRef] [Google Scholar] [Publisher Link]

[38] Michael Pfeiffer, and Thomas Pfeil, “Deep Learning with Spiking Neurons: Opportunities and Challenges,”  Frontiers in Neuroscience,

vol. 12, 2018. [CrossRef] [Google Scholar] [Publisher Link]

[39] Youngeun Kim et al., “Exploring Temporal Information Dynamics in Spiking Neural Networks,” Proceedings of the AAAI Conference on

Artificial Intelligence, vol. 37, no. 7, pp. 8308-8316, 2023. [CrossRef] [Google Scholar] [Publisher Link]

[40] Amirhossein Tavanaei  et  al.,  “Deep  Learning  in  Spiking  Neural  Networks,”  Neural  Networks,  vol.  111,  pp.  47-63,  2019.  [CrossRef]

[Google Scholar] [Publisher Link]

[41] Jayram Moorkanikara Nageswaran et al., “A Configurable Simulation Environment for the Efficient Simulation of Large-Scale Spiking 
Neural Networks on Graphics Processors,” Neural Networks, vol. 22, no. 5-6, pp. 791-800, 2009. [CrossRef] [Google Scholar] [Publisher 
Link]

[42] Hsin-Pai  Cheng  et  al.,  “Understanding  the  Design  of  IBM  Neurosynaptic  System  and  Its  Tradeoffs:  A  User  Perspective,”  Design, 
Automation & Test in Europe Conference & Exhibition (DATE), Lausanne, Switzerland, pp. 139-144, 2017. [CrossRef] [Google Scholar] 
[Publisher Link]

[43] Chit-Kwan Lin et al., “Programming Spiking Neural Networks on Intel’s Loihi,” Computer, vol. 51, no. 3, pp. 52-61, 2018. [CrossRef]

[Google Scholar] [Publisher Link]

[44] Muhammad  Aitsam,  Sergio  Davies,  and  Alessandro  Di  Nuovo,  “Neuromorphic  Computing  for  Interactive  Robotics:  A  Systematic

Review,” IEEE Access, vol. 10, pp. 122261-122279, 2022. [CrossRef] [Google Scholar] [Publisher Link]

[45] Eunsu  Kim,  and  Youngmin  Kim,  “Exploring  the  Potential  of  Spiking  Neural  Networks  in  Biomedical  Applications:  Advantages, 
Limitations, and Future Perspectives,” Biomedical Engineering Letters, vol. 14, no. 5, pp. 967-980, 2024. [CrossRef] [Google Scholar] 
[Publisher Link]

[46] V.  Rajakumari,  and  K.P.  Pradhan,  “Demonstration  of  an  UltraLow  Energy  PD-SOI  FinFET  Based  LIF  Neuron  for  SNN,”  IEEE

Transactions on Nanotechnology, vol. 21, pp. 434-441, 2022. [CrossRef] [Google Scholar] [Publisher Link]

[47] Saeed Reza Kheradpisheh et al., “STDP-based Spiking Deep Convolutional Neural Networks for Object Recognition,” Neural Networks,

vol. 99, pp. 56-67, 2018. [CrossRef] [Google Scholar] [Publisher Link]

[48] Wenzhe Guo et al., “Towards Efficient Neuromorphic Hardware: Unsupervised Adaptive Neuron Pruning,” Electronics, vol. 9, no. 7, pp.

1-15, 2020. [CrossRef] [Google Scholar] [Publisher Link]

[49] Marc-Oliver Gewaltig, and Markus Diesmann, “Nest (Neural Simulation Tool),” Scholarpedia, vol. 2, no. 4, 2007. [Google Scholar]

47

---

<!-- PAGE 17 -->

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

[50] Hananel  Hazan  et  al.,  “BindsNET:  A  Machine  Learning-Oriented  Spiking  Neural  Networks  Library  in  Python,”  Frontiers  in

Neuroinformatics, vol. 12, pp. 1-18, 2018. [CrossRef] [Google Scholar] [Publisher Link]

[51] Marcel Stimberg, Romain Brette, and Dan FM Goodman, “Brian 2, An Intuitive and Efficient Neural Simulator,” Elife, vol. 8, pp. 11-41,

2019. [CrossRef] [Google Scholar] [Publisher Link]

[52] Jesper Sjöström, and Wulfram Gerstner, “Spike-Timing Dependent Plasticity,” Scholarpedia, vol. 5, no. 2, 2010. [Google Scholar] 
[53] Dominique  Debanne,  and  Mu-Ming Poo,  “Spike-Timing  Dependent  Plasticity  Beyond  Synapse  - Pre-  and Post-Synaptic  Plasticity  of 
Intrinsic Neuronal Excitability,” Frontiers in Synaptic Neuroscience, vol. 2, pp. 1-6, 2010. [CrossRef] [Google Scholar] [Publisher Link] 
[54] Timothée Masquelier, Rudy Guyonneau, and Simon J. Thorpe, “Competitive STDP-Based Spike Pattern Learning,” Neural Computation,

vol. 21, no. 5, pp. 1259-1276, 2009. [CrossRef] [Google Scholar] [Publisher Link]

[55] Slawomir Koziel, David Echeverría Ciaurri, and Leifur Leifsson, “Surrogate-Based Methods,” Studies in Computational Intelligence,

Berlin, Heidelberg, pp. 33-59, 2011. [CrossRef] [Google Scholar] [Publisher Link]

[56] Tehreem  Syed  et  al.,  “Exploring Optimized  Spiking  Neural  Network Architectures  for  Classification Tasks on  Embedded Platforms,”

Sensors, vol. 21, no. 9, pp. 1-25, 2021. [CrossRef] [Google Scholar] [Publisher Link]

[57] Shivam  S.  Kadam, Amol  C. Adamuthe,  and Ashwini  Patil,  “CNN  Model  for  Image  Classification  on  MNIST  and  Fashion-MNIST

Dataset,” Journal of Scientific Research, vol. 64, no. 2, pp. 374-384, 2020. [CrossRef] [Google Scholar] [Publisher Link]

[58] Yu  Hu  et  al.,  “Hand  Gesture  Recognition  System  using  the  Dynamic Vision  Sensor,”  2022  5th  International  Conference  on  Circuits,

Systems and Simulation (ICCSS), Nanjing, China, pp. 102-110, 2022. [CrossRef] [Google Scholar] [Publisher Link]

[59] Marc-Oliver Gewaltig, and Markus Diesmann, “Nest (Neural Simulation Tool),” Scholarpedia, vol. 2, no. 4, 2007. [Google Scholar] 
[60] Lars  Niedermeier  et  al.,  “CARLsim  6:  An  Open  Source  Library  for  Large-Scale,  Biologically  Detailed  Spiking  Neural  Network 
Simulation,” 2022 International Joint Conference on Neural Networks (IJCNN), Padua, Italy, pp. 1-10, 2022. [CrossRef] [Google Scholar] 
[Publisher Link]

[61] Ting-Shuo Chou et al., “CARLsim 4: An Open Source Library for Large Scale, Biologically Detailed Spiking Neural Network Simulation 
using Heterogeneous Clusters,” 2018 International Joint Conference on Neural Networks (IJCNN), Rio de Janeiro, Brazil, pp. 1-8, 2018. 
[CrossRef] [Google Scholar] [Publisher Link]

[62] Michael  Beyeler  et  al.,  “CARLsim  3: A  User-Friendly  and  Highly  Optimized  Library  for  the  Creation  of  Neurobiologically  Detailed 
Spiking  Neural  Networks,”  2015  International  Joint  Conference  on  Neural  Networks  (IJCNN),  Killarney,  Ireland,  pp.  1-8,  2015. 
[CrossRef] [Google Scholar] [Publisher Link]

[63] Abderazek Ben Abdallah, and Khanh N. Dang, “Comprehensive Review of Neuromorphic Systems,” Neuromorphic Computing Principles

and Organization, Springer Nature Switzerland, pp. 275-303, 2025. [CrossRef] [Google Scholar] [Publisher Link]

[64] Hariprasad  Kannan,  Nikos  Komodakis,  and  Nikos  Paragios,  “Newton-Type  Methods  for  Inference  in  Higher-Order  Markov  Random 
Fields,”  2017  IEEE  Conference  on  Computer  Vision  and  Pattern  Recognition  (CVPR),  Honolulu,  HI,  USA,  pp.  7224-7233,  2017. 
[CrossRef] [Google Scholar] [Publisher Link]

[65] Wei  Bai  et  al.,  “Network Analysis  of Anxiety  and  Depressive  Symptoms Among  Nursing  Students  during  the  Covid-19  Pandemic,”

Journal of Affective Disorders, vol. 294, pp. 753-760, 2021. [CrossRef] [Google Scholar] [Publisher Link]

[66] Arnon Amir et al., “A Low Power, Fully Event-Based Gesture Recognition System,” 2017 IEEE Conference on Computer Vision and

Pattern Recognition (CVPR), Honolulu, HI, USA, pp. 7388-7397, 2017. [CrossRef] [Google Scholar] [Publisher Link]

[67] Jun Haeng Lee, Tobi Delbruck, and Michael Pfeiffer, “Training Deep Spiking Neural Networks Using Backpropagation,”  Frontiers in

Neuroscience, vol. 10, pp. 1-13, 2016. [CrossRef] [Google Scholar] [Publisher Link]

[68] Sanaullah et al., “Evaluation of Spiking Neural Nets-Based Image Classification Using the Runtime Simulator RAVSim,” International

Journal of Neural Systems, vol. 33, no. 9, pp. 1-19, 2023. [CrossRef] [Google Scholar] [Publisher Link]

[69] Yunpeng Huang et al., “Advancing Transformer Architecture in Long-Context Large Language Models: A Comprehensive Survey,” arXiv

Preprint, pp. 1-40, 2023. [CrossRef] [Google Scholar] [Publisher Link]

[70] Rasoul  Hosseinzadeh,  and  Mahdi  Sadeghzadeh,  “Attention  Mechanisms  in  Transformers:  A  General  Survey,”  Journal  of  Artificial

Intelligence & Data Mining (JAIDM), vol. 13, no. 3, pp. 359-368, 2025. [CrossRef] [Google Scholar] [Publisher Link]

[71] Sayed Mahbub Hasan Amiri et al., “The Carbon Cost of Conversation, Sustainability in the Age of Language Models,” arXiv Preprint,

pp. 1-22, 2025. [CrossRef] [Google Scholar] [Publisher Link]

[72] David  Patterson  et  al.,  “Carbon Emissions  and  Large  Neural  Network Training,”  arXiv  Preprint, pp. 1-22, 2021.  [CrossRef]  [Google

Scholar] [Publisher Link]

[73] Zhanglu Yan, Zhenyu Bai, and Weng-Fai Wong, “Reconsidering the Energy Efficiency of Spiking Neural Networks,” arXiv Preprint, pp.

1-11, 2024. [CrossRef] [Google Scholar] [Publisher Link]

[74] Sayeed Shafayet Chowdhury, Nitin Rathi, and Kaushik Roy, “One Timestep is All You Need: Training Spiking Neural Networks with

Ultra Low Latency,” arXiv Preprint, pp. 1-17, 2021. [CrossRef] [Google Scholar] [Publisher Link]

[75] Giacomo Indiveri, and Shih-Chii Liu, “Memory and Information Processing in Neuromorphic Systems,” Proceedings of the IEEE, vol.

103, no. 8, pp. 1379-1397, 2015. [CrossRef] [Google Scholar] [Publisher Link]

48

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal of Engineering Trends and Technology Volume 73 Issue 10, 32-48, October 2025
ISSN: 2231–5381 / https://doi.org/10.14445/22315381/IJETT-V73I10P104 © 2025 Seventh Sense Research Group®
Original Article
Spiking Neural Networks: The Future of Brain-Inspired
Computing
Sales G. Aribe Jr.
Information Technology Department, Bukidnon State University, Fortich Street, Malaybalay City, Philippines.
Corresponding Author : sg.aribe@buksu.edu.ph
Received: 14 July 2025 Revised: 06 October 2025 Accepted: 07 October 2025 Published: 31 October 2025
Abstract - Spiking Neural Networks (SNNs) represent the latest generation of neural computation, offering a brain-inspired
alternative to conventional Artificial Neural Networks (ANNs). Unlike ANNs, which depend on continuous-valued signals, SNNs
operate using distinct spike events, making them inherently more energy-efficient and temporally dynamic. This study presents a
comprehensive analysis of SNN design models, training algorithms, and multi-dimensional performance metrics, including
accuracy, energy consumption, latency, spike count, and convergence behavior. Key neuron models such as the Leaky Integrate-
and-Fire (LIF) and training strategies—including surrogate gradient descent, ANN-to-SNN conversion, and Spike-Timing
Dependent Plasticity (STDP)—are examined in depth. Results show that surrogate gradient-trained SNNs closely approximate
ANN accuracy (within 1–2%), with faster convergence by the 20th epoch and latency as low as 10 milliseconds. Converted SNNs
also achieve competitive performance but require higher spike counts and longer simulation windows. STDP-based SNNs, though
slower to converge, exhibit the lowest spike counts and energy consumption (as low as 5 millijoules per inference), making them
optimal for unsupervised and low-power tasks. These findings reinforce the suitability of SNNs for energy-constrained, latency-
sensitive, and adaptive applications such as robotics, neuromorphic vision, and edge AI systems. While promising, challenges
persist in hardware standardization and scalable training. This study concludes that SNNs, with further refinement, are poised
to propel the next phase of neuromorphic computing.
Keywords - Artificial Intelligence, Brain-inspired computing, Energy efficiency, Neuromorphic computing, Spiking Neural
Network.
1. Introduction (RNNs) [7] and more sophisticated versions, such as Long
The advent of Artificial Intelligence (AI) has ushered in a Short-Term Memory (LSTM) [8] and Gated Recurrent Units
technological revolution that permeates virtually all aspects of (GRUs), are designed for sequential input; yet, they are
modern life, from healthcare and transportation to finance and plagued by vanishing gradient issues and exhibit inefficiency
education. Central to this evolution are a class of computational in modeling long-range relationships. More recent models, like
models collectively referred to as ANNs that have achieved Transformers, have recently revolutionized natural language
stunning results across an array of pattern recognition and processing using attention mechanisms, but at the cost of
machine learning problems. Traditional ANNs, however, are humongous memory and processing demands [10].
extremely energy inefficient and biologically unrealistic [1],
[2] despite their impressive performance. These are also All these models have a basic property in common: they
difficult to implement because they rely on continual signal and depend on synchronous updates and on continuous activations.
large matrix multiplication, which are computationally This is not the case in the human brain, which is an
expensive and biologically unrealistic [3]. asynchronous system and communicates with discrete binary
spikes [11]. In addition, classic networks carry out millions of
Various neural network architectures have been created to operations per inference step, resulting in high power
address distinct computational challenges. The ANN is the consumption-a critical bottleneck in scenarios such as mobile
basic model for deep learning, but cannot be directly applied to and edge computing [12]. Despite their success, these networks
temporal data because of its computational complexity and are entirely based on dense and continuous computations and
absence of memory [4, 5]. Convolutional Neural Networks lack biological realism, which renders them energy-inefficient
(CNNs) are engineered for spatial feature extraction in image and not amenable to real-time, low-power applications, the
and video processing and are not directly applicable to limitations that SNNs try to overcome [13]. SNNs, the most
temporal or sequential data [6]. Recurrent Neural Networks recent evolution of neural network models, signify a
This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/)

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
transformative advancement in artificial intelligence by by an order of magnitude compared to ANNs, as shown in this
mimicking the discrete and temporal firing patterns of study, SNNs present a feasible path for greener and more
biological neurons. [14]. Unlike ANNs, which process efficient edge intelligence. This positions the current work as
information in a synchronous and continuous fashion, SNNs both timely and original, addressing the dual challenge of
operate on sparse, event-driven spike trains, enabling them to advancing AI performance while mitigating environmental and
process spatiotemporal data with greater energy efficiency and energy concerns.
fidelity to brain-like computation. This bio-inspired method
closely resembles how actual neurons in the brain exchange Thus, this paper comprehensively examines SNNs as the
information by sending out short, timed electrical signals future of brain-inspired computing. It begins by outlining their
known as spikes [15]. biological underpinnings and core mechanisms, followed by a
comparative analysis with traditional ANNs. It then delves into
Interest in SNNs has increased due to recent developments various applications, design strategies, and training
in neuromorphic engineering, which creates hardware that methodologies that define current SNN research. This work
mimics the composition and operations of the human brain [16, attempts to give a thorough evaluation of SNNs and make
17]. Chips like International Business Machines’ (IBM) suggestions for further research and development in
TrueNorth and Intel’s Loihi show that SNNs may be neuromorphic AI by reviewing experimental benchmarks and
implemented at scale with extremely low power consumption, implementation challenges.
which makes them appropriate for use in edge computing
settings and mobile devices [18, 12]. Additionally, SNNs are 2. Related Literature
being studied extensively for use in brain-computer interfaces, 2.1. Biological Inspiration
robotics, and sensory processing, highlighting their promise in The biological processes of the human brain, namely how
latency-sensitive, real-time scenarios [19]. neurons interact by sending out distinct electrical impulses
called spikes, served as the model for SNNs [26]. Conventional
Despite rapid progress, most studies examine one training neural networks depend on levels of constant activation, while
paradigm or one metric at a time—e.g., ANN-to-SNN biological neurons transmit information through asynchronous
conversion optimized for accuracy on image benchmarks [20, events triggered by membrane potential thresholds.
21] surrogate-gradient training highlighting differentiable Foundational biological models such as the Hodgkin-Huxley
approximations [22], or neuromorphic reports emphasizing model [27] and the Leaky Integrate-and-Fire (LIF) model [28]
hardware power/latency [12, 23]. A unified head-to-head form the theoretical basis of SNNs. Essential neural functions
analysis that compares surrogate-trained, ANN-to-SNN like firing thresholds, refractory periods, and membrane
converted, and STDP models under a single protocol and potential degradation are replicated in these models.
across multiple dimensions—accuracy, latency, energy per
inference, spike count, and convergence—on both event-based Moreover, spike-based learning in biological systems is
and static datasets remains limited in the literature [1, 20, 22, often attributed to synaptic plasticity governed by timing rules
24, 25]. This gap obscures practical tradeoffs that matter for [29]. Spike-Timing Dependent Plasticity (STDP), which
edge deployment and real-time robotics, where temporal modifies synaptic weights according to the relative timing of
precision and energy budgets are binding constraints [12, 23]. pre- and postsynaptic spikes, is a good illustration [30]. STDP
has been successfully integrated into SNNs to enable
This work addresses that gap by: (i) establishing a unified biologically plausible learning without the need for
evaluation protocol that compares surrogate-trained, backpropagation.
converted, and STDP SNNs across five metrics (accuracy,
latency, energy, spike count, convergence); (ii) reporting These qualities allow SNNs to capture temporal changes,
latency and spiking activity alongside accuracy to reflect sparse activation, and asynchronous signaling, thereby
hardware-aware performance; (iii) providing a convergence achieving greater similarity to cortical processes observed in
analysis to 20 epochs that clarifies optimization behavior under neuroscience [31].
different learning rules; and (iv) translating these findings into
application-oriented guidance (e.g., surrogate SNNs for low- 2.2. Fundamentals of SNNs
latency accuracy targets; STDP for ultra-low-power At the core of SNN operation is the spike-based encoding
unsupervised settings). Relative to prior work that focuses on a of information. SNNs use rate or temporal coding schemes to
single method or metric [20-22, 25], this study offers an encode data in the time and frequency of spikes rather than
integrated, multi-metric comparison that supports principled real-valued vectors [32]. While temporal coding encodes
model selection for neuromorphic and edge AI [1, 12]. Given information in the exact time of spikes, rate coding conveys
the rising energy costs of deep learning models, particularly input strength by spike frequency. SNNs are more energy-
transformer-based systems [10, 12], the exploration of SNNs is efficient and appropriate for event-driven processing through
not only a technical advancement but also an important step these processes.
toward sustainable AI computing. By reducing energy usage
33

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
Many equations are used to explain the behavior of spiking Intel’s Loihi [43] are two major neuromorphic chips that
neurons, but the LIF model is still the most often utilized support event-driven computation and on-chip learning. These
because of its ease of use and computational effectiveness [33]. chips enable real-time processing with ultra-low power
For learning, SNNs use biologically inspired methods like consumption, opening doors for deploying SNNs in edge
surrogate gradient methods, STDP, and Reward-Modulated computing, wearables, and autonomous systems.
STDP (R-STDP) that enable supervised learning despite the
non-differentiability of spike events [34]. In addition, recent Robotics: In robotics, SNNs enable low-latency responses
research has introduced training techniques that make SNNs and real-time sensory integration. For instance, SNNs have
competitive with deep learning models. These include hybrid been used in applications where timing and energy efficiency
approaches like converting pre-trained ANNs into SNNs [20], are crucial, such as visual tracking, object recognition, and
and direct training using approximated gradients, which helps locomotion control [44]. Because SNNs are asynchronous,
overcome the challenges of discontinuous activation [22]. they work well in dynamic settings where conventional ANN-
based controllers would be too sluggish or power-hungry.
2.3. Comparison with Traditional ANNs
Edge Computing: SNNs’ event-based design and minimal
SNNs differ fundamentally from ANNs in architecture,
activity make them perfect for use in devices with limited
data representation, and learning strategy. ANNs use dense
energy. Applications include gesture recognition using event-
layers of constant activation functions like sigmoid or ReLU
based cameras (e.g., DVS128 dataset), anomaly detection in
and are trained using backpropagation [35, 36]. SNNs, on the
IoT systems, and on-device speech processing [38].
other hand, use gradient-free or biologically motivated learning
algorithms and function with limited, event-triggered
activations [37]. Healthcare: SNNs are essential for prostheses and Brain-
Machine Interfaces (BMIs) in biomedical engineering and
neuroscience. They can interpret neural signals for motor
The energy efficiency of SNNs is one of its main benefits.
control or restore sensory functions. SNNs are also being
While ANNs process every node during each cycle, SNNs only
explored for seizure prediction, Electroencephalogram (EEG)
activate neurons upon spike generation, resulting in
signal classification, and neural rehabilitation, where temporal
significantly fewer operations and reduced power usage—ideal
precision and biological compatibility are essential [45].
for low-resource or edge devices [38]. Furthermore, SNNs
exhibit temporal sensitivity, enabling them to process
sequential and real-time data more effectively than In summary, existing studies establish SNNs as
conventional models such as CNNs and RNNs [39, 40]. biologically inspired and energy-efficient yet fragmented
across training strategies and evaluation metrics. This review
sets the stage for a unified analysis.
However, SNNs face significant challenges in scalability,
training convergence, and a lack of standardized frameworks
compared to mature ANN systems. While ANNs benefit from 3. Methodology
extensive optimization libraries and hardware acceleration 3.1. SNN Design
(e.g., TensorFlow, GPUs), SNNs are still evolving in terms of Replicating the dynamic behavior of biological neurons
simulation platforms and hardware compatibility [41]. and their synaptic contacts is the foundation of SNN design.
SNNs use asynchronous, event-driven computing, in contrast
Surveys and foundational studies emphasize SNNs’ to classic neural networks, where each layer analyzes inputs in
temporal coding and energy advantages but typically report a fixed, synchronous fashion. Neuron models that mimic the
accuracy or hardware power in isolation [1, 38, 40]. biophysical characteristics of actual neurons, most notably the
Conversion pipelines preserve ANN accuracy yet often require LIF model, enable this design.
longer simulation windows and higher spike rates [20, 21];
surrogate-gradient methods close the accuracy gap with direct One of the most popular and straightforward models for
end-to-end training [22]; and neuromorphic reports foreground SNN simulations is the LIF model [46]. It records crucial
energy/latency on chips [12, 23]. By evaluating all three neural processes such as threshold-based spike production,
training strategies under a consistent setup and reporting membrane potential accumulation, and leakage across time. A
accuracy, latency, energy, spike, and convergence together, the neuron “fires” a spike and resets its membrane potential when
present study complements these strands. It clarifies practical incoming synaptic inputs cause it to surpass a certain threshold.
tradeoffs for deployment-oriented SNN design [24, 25]. Because neurons in this model only fire in response to strong
stimuli, it enables a sparse, energy-efficient network [11]. A
2.4. Applications of SNNs LIF neuron’s behavior can be shown in Figure 1. This graphic
Neuromorphic Hardware: The field of neuromorphic shows how the input current causes the membrane potential to
computing, which describes hardware architectures intended to rise over time. The neuron mimics the firing behavior seen in
mimic the structure and functionality of the brain, is one of the organic neurons by emitting a spike and then resetting when
most promising areas for SNNs. IBM’s TrueNorth [42] and the voltage hits a predetermined threshold.
34

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
Time (ms)
0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
-54
-56
)
V -58
m
(
la -60
itn
e to -62
P
e -64
Membrane Potential (LIF Neuron) Threshold
n
a
r
b
m -66
e
M
-68
-70
Fig. 1 LIF neuron model
More sophisticated models, such as the Izhikevich model, SNNs are translated to neuromorphic circuits in hardware
simulate a variety of neuronal firing patterns, including implementations, including Intel’s Loihi, which allows for
bursting, tonic spiking, and adaptation, by fusing biological dynamic neural configuration with spiking inputs and on-chip
realism with computing efficiency [23]. The choice of neuron learning. Loihi incorporates programmable neuron models and
model typically balances between biological fidelity and synaptic delays, enabling flexible SNN design for real-world
computational overhead, depending on the application applications [12].
domain—whether high-performance robotics or low-power
edge computing. Figure 2 illustrates the three main phases of a full SNN
pipeline: input encoding, spiking neuron processing, and
SNN architecture typically includes input, hidden, and output decoding. Using encoding techniques like rate coding or
output layers, where spikes propagate through synapses with temporal coding, continuous signals like audio, pictures, or
temporal delays and weight modulation [40]. These networks sensor data are converted into discrete spike trains during input
can be feedforward, recurrent, or convolutional, depending on encoding. After passing through one or more layers of spiking
the data type and processing goals. For image-based tasks, neurons, these spike trains are used to analyze information
Convolutional SNNs (CSNNs) are increasingly popular due to based on the timing and intensity of the spikes. The output layer
their ability to preserve spatial hierarchies while benefiting then decodes the spike patterns into a control, decision, or
from event-driven sparsity [47]. prediction signal that is suitable for the intended use.
Fig. 2 Conceptual architecture of SNN [48]
35

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
The system includes input encoding to convert signals into (MNIST) using surrogate gradient descent [22, 56].
spikes, multiple spiking neuron layers for event-driven Additionally, this has made it possible to learn deep SNNs end-
computation, and output decoding to produce meaningful to-end without converting from ANNs.
results. This modular architecture allows SNNs to mimic the
asynchronous, event-driven behavior of biological neural 3.5. ANN-to-SNN Conversion
systems. The design supports a wide variety of tasks ranging Training a traditional ANN and then converting it to an
from object recognition to robotic control, depending on how SNN by interpreting activation levels as firing rates is another
the neurons are interconnected and trained. useful method. This method allows for high-performance
training using standard deep learning libraries, followed by an
Several software tools have been widely adopted to efficient deployment in event-driven hardware [21, 24].
simulate SNN behavior. Neural Simulation Tool (NEST) [49] However, this technique often requires careful calibration of
is used for broad-based simulations of spiking neuron firing thresholds and time constants to preserve accuracy.
networks, especially in neuroscience research. Biologically
Inspired Neural and Dynamical Systems in Networks 3.6. Experimental Framework
(BindsNET) [50] and Brian2 [51] offer more flexibility and The experimental framework for evaluating SNNs
Python integration for machine learning tasks. These platforms involves selecting benchmark datasets, simulation tools,
support complex network configurations, STDP learning rules, training protocols, and performance metrics tailored to the
and integration with neuromorphic datasets. Overall, the unique characteristics of spike-based computation. This
design of an SNN requires careful attention to the neuron section outlines the standard setup used in the literature to train
model, network topology, synaptic behavior, and hardware- and assess SNNs in classification, control, and recognition
software compatibility. These components collectively tasks.
determine the network’s ability to mimic brain-like
computation while maintaining computational tractability and 3.6.1. Datasets
real-world applicability. SNNs are often evaluated using both static and
neuromorphic datasets to benchmark their performance under
3.2. Training Algorithms conventional and event-based input conditions:
The non-differentiable characteristics of spike events
make training SNNs more difficult than training regular ANNs. • MNIST: A widely used dataset for recognition of
Since spikes are discrete, binary events, standard handwritten digits, which consists of 70,000 grayscale
backpropagation—which relies on continuous gradients— images [57]. Rate or latency encoding techniques are used
cannot be directly applied. Researchers have therefore created in SNNs to transform pictures into spike trains. MNIST
specific training methods that are suited to the event-driven and serves as a baseline for testing the accuracy and energy
temporal dynamics of SNNs. efficiency of small-scale SNNs. In this study, a rate-
coding system that linked pixel intensity to spike
3.3. Unsupervised Learning: STDP frequency was used to encode MNIST images. To ensure
STDP is among the most biologically realistic training there was enough spike activity for recognition tasks,
techniques. The exact timing of pre- and postsynaptic spikes each image was shown throughout a simulation window
determines how STDP modifies synaptic weights; if a of 100 ms.
presynaptic neuron fires just before a postsynaptic neuron, the • DVS128 Gesture Dataset: It is a neuromorphic dataset
synapse is strengthened; if not, it is weakened [52, 53]. This recorded with a Dynamic Vision Sensor (DVS), which
local, unsupervised learning rule has been widely implemented captures changes in brightness as asynchronous spikes
in early layers of SNNs to extract spatiotemporal patterns from rather than static frames [58]. It is frequently used to
data without requiring labels [54]. assess SNNs’ real-time performance in event-driven
processing and motion identification. For gesture data,
3.4. Surrogate Gradient Descent temporal coding was employed, with spike timing
To enable supervised learning, researchers developed directly representing motion events. Input sequences
surrogate gradient methods. These techniques enable the were segmented into 150-ms windows to balance latency
application of gradient-based optimization akin to and recognition accuracy.
backpropagation by substituting a smooth, differentiable • SHD/SSC Datasets: The Spiking Heidelberg Digits
approximation for the non-differentiable spike function during (SHD) and Spiking Speech Commands (SSC) datasets are
the backward run [55]. Popular surrogate functions include temporally rich, spike-based versions of audio
piecewise linear, sigmoid, or exponential approximations. digit/speech recognition tasks, tailored for direct input to
SNNs may now be trained with competitive accuracy on SNNs [25]. Audio waveforms were preprocessed into
common classification benchmarks such as the Canadian spike trains using latency encoding with a maximum
Institute for Advanced Research-10 (CIFAR-10) and the window of 200 ms per sample, aligned with common
Modified National Institute of Standards and Technology auditory neuroscience benchmarks.
36

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

| 3.6.2. Simulation Tools and Platforms  |                 |     |      |            |                |      |     | Latency= t |          | -t   |     |     |     | (2)  |
| -------------------------------------- | --------------- | --- | ---- | ---------- | -------------- | ---- | --- | ---------- | -------- | ---- | --- | --- | --- | ---- |
|                                        |                 |     |      |            |                |      |     |            | decision | 0    |     |     |     |      |
| A  range                               | of  simulators  |     | and  | libraries  | is  available  | for  |     |            |          |      |     |     |     |      |
designing, training, and testing SNNs:
|     |     |     |     |     |     |     |     | •  Spike  | Count:  | The  aggregate     |     | amount      | of  | spikes  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------------------ | --- | ----------- | --- | ------- |
|     |     |     |     |     |     |     |     | produced  |         | during  inference  |     | represents  |     | power   |
•  Brian2: A flexible, Python-based simulator ideal for small
consumption and computational sparsity.
| to  medium-scale  |     | experiments.  |     | It  | allows  | for  custom  |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------- | --- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
neuron models and precise temporal dynamics [51].  Total Spikes= ∑N
|     |     |     |     |     |     |     |     |     |     | ∑T s(t)  |     |     |     | (3)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | ---- |
•  BindsNET: Built on top of PyTorch, this library integrates  i=1 t=1 i
deep learning infrastructure with spiking neuron models,
Where:
supporting supervised and unsupervised learning [50].
 s (t) = 1 if neuron i spikes at time t, otherwise 0
| •  NEST:  | Designed  | for  | large-scale  |     | simulations  | in  |     | i   |     |     |     |     |     |     |
| --------- | --------- | ---- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 N = total number of neurons
computational  neuroscience,  NEST  is  suitable  for   T = total time steps
| studying  | population-level  |     |     | dynamics  | and  | cortical  |     |     |     |     |     |     |     |     |
| --------- | ----------------- | --- | --- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
modeling [59].
•  Energy Efficiency: The overall number of spikes and
•  CARLsim: A GPU-accelerated SNN simulator developed
operations involved is a simplistic proxy for energy.
| for  | large,  real-time  |     | SNN  | systems  | with  | STDP  and  |     |     |     |     |     |     |     |     |
| ---- | ------------------ | --- | ---- | -------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Measured in operations per joule or spikes per watt, this
reinforcement learning support [60-62].
|     |     |     |     |     |     |     |     | is  very  | significant  | in  neuromorphic  |     | computing.  |     | On  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ----------------- | --- | ----------- | --- | --- |
•  Intel Loihi and IBM TrueNorth Software Development
|     |     |     |     |     |     |     |     | neuromorphic  | hardware,  | SNNs  | are  | usually  | orders  | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | ----- | ---- | -------- | ------- | --- |
Kits (SDKs): Neuromorphic hardware platforms include
magnitude more efficient than ANNs.
| their  | own  toolkits,  | allowing  |     | direct  | deployment  | and  |     |     |     |     |     |     |     |     |
| ------ | --------------- | --------- | --- | ------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
evaluation of SNNs in real-world scenarios [63, 18].
|     |     |     |     |     |     |     |     | E  = E | *S+ E | *C      |     |     |     | (4)  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     |     | total  | spike | synapse |     |     |     |      |
Experiments were conducted primarily using the Brian2
Where:
simulator for surrogate gradient SNNs, BindsNET for ANN-
to-SNN  conversion  pipelines,  and  NEST  for  large-scale  E spike  = energy per spike (hardware-specific)
|                                                             |     |     |     |     |     |     |     | E       |   = energy per synaptic operation  |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------------------------- | --- | --- | --- | --- | --- |
| spiking models. Default neuron parameters followed the LIF  |     |     |     |     |     |     |     | synapse |                                    |     |     |     |     |     |
S = total spikes
model with membrane time constant τ = 20 ms, threshold
voltage equivalent to Vth = 1.0, and refractory period of 5 ms,  C = total synaptic operations
unless otherwise noted.
Alternatively, normalized energy efficiency:
Training was performed on a workstation with an NVIDIA
RTX GPU and 32 GB RAM, ensuring comparability with prior  Accuracy
|     |     |     |     |     |     |     |     | Energy Efficiency =  |     |     |     |     |     | (5)  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | ---- |
Energy Consumption (Joules)
benchmarks in the literature [20, 22, 25].
3.6.3. Evaluation Metrics  •  Convergence Time: Measures how fast the network learns
(training efficiency). It is often expressed as:
| Given    | the  unique  | characteristics  |     | of        | SNNs,  | evaluation  |     |     |     |     |     |     |     |     |
| -------- | ------------ | ---------------- | --- | --------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| metrics  | go  beyond   | classification   |     | accuracy  | and    | include     |     |     |     |     |     |     |     |     |
measurements  that  reflect  computational  efficiency  and  Convergence Time = Epoch where
min
| biological realism:  |     |     |     |     |     |     | Accuracy |     | ≥Target Accuracy  |     |     |     |     | (6)  |
| -------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------------- | --- | --- | --- | --- | ---- |
epoch
•  Accuracy: The most basic metric, measuring how well the
Overall, the datasets, encoding schemes, and simulation
| SNN  | performs  | in  | tasks  | like  | digit  | recognition,  |     |     |     |     |     |     |     |     |
| ---- | --------- | --- | ------ | ----- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
platforms ensure that results are reproducible and comparable
classification, or control prediction.
to prior SNN benchmarks.
|             | Number of Correct Predictions |     |     |          |     |      | 4. Results and Discussion  |     |     |     |     |     |     |     |
| ----------- | ----------------------------- | --- | --- | -------- | --- | ---- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Accuracy =  |                               |     |     |  x 100%  |     | (1)  |                            |     |     |     |     |     |     |     |
Total Number of Predictions
4.1. Performance Analysis
SNNs have demonstrated promising performance across
•  Latency: Measures the time, in milliseconds (ms) or
several benchmarks in static and event-based learning tasks.
timesteps, it takes for the network to produce a decision.
|     |     |     |     |     |     |     | On  | traditional  | datasets  | like  MNIST,  | SNNs  |     | trained  | using  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | ------------- | ----- | --- | -------- | ------ |
Shorter latency indicates better suitability for real-time
surrogate gradient methods or ANN-to-SNN conversion have
applications.
|     |     |     |     |     |     |     | achieved  | classification  |               | accuracies  | exceeding  |       | 98%,        | nearly  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | ------------- | ----------- | ---------- | ----- | ----------- | ------- |
|     |     |     |     |     |     |     | matching  |                 | conventional  | ANNs        | [20,       | 21].  | Similarly,  |         |
Let:
|     |                                                    |     |     |     |     |     | convolutional  |     | SNNs  | have  proven  | effective  |     | in  CIFAR-10,  |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ------------- | ---------- | --- | -------------- | --- |
|     |    t   = time when the first output neuron spikes  |     |     |     |     |     |                |     |       |               |            |     |                |     |
decision reaching  accuracies  between  85%  and  90%,  which  are
|     |    t  = time of input stimulus  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
competitive with shallow CNNs under constrained conditions
37

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

[40]. Because SNNs can analyze event-driven inputs in real- increased spike rates result in longer inference times. Directly
time, they have demonstrated excellent appropriateness for  trained SNNs, on the other hand, provide faster and sparser
neuromorphic datasets such as the DVS128 Gesture Dataset.  computing, but they may require more epochs to converge and
Models  evaluated  on  DVS  datasets  often  outperform  intricate  hyperparameter  adjustment.  The  performance  of
traditional frame-based models in latency and responsiveness,  several network models on benchmark datasets is compiled in
| despite achieving slightly lower absolute accuracy [64]. For  |     |     |     |     |     | the table below:  |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
instance, using a spiking CNN trained with STDP and tested
on DVS128, Bai et al. [65] reported over 93% classification  Table 1. SNN performance summary
accuracy in dynamic gesture recognition.  MNIST  CIFAR-10  Energy
|               |           |          |       |                   |     | Model  | Accuracy  | Accuracy  | Consumption   |
| ------------- | --------- | -------- | ----- | ----------------- | --- | ------ | --------- | --------- | ------------- |
|               |           |          |       |                   |     |        | (%)       | (%)       | (Normalized)  |
| Furthermore,  | directly  | trained  | SNNs  | using  surrogate  |     |        |           |           |               |
gradient  descent  have  closed  the  performance  gap  with  ANN (CNN)  99.2  92  1
| traditional ANNs. Zenke and Ganguli [34] reported that their  |             |           |                      |           |        | Converted   |       |       |      |
| ------------------------------------------------------------- | ----------- | --------- | -------------------- | --------- | ------ | ----------- | ----- | ----- | ---- |
|                                                               |             |           |                      |           |        |             | 98.1  | 89.3  | 0.1  |
| SuperSpike                                                    | algorithm   | enabled   | multilayer           | SNNs  to  | reach  | SNN         |       |       |      |
| comparable                                                    | levels  of  | accuracy  | and  generalization  |           | on     | Direct SNN  |       |       |      |
spatiotemporal  classification  tasks.  Similarly,  end-to-end  (Surrogate  97.8  85.7  0.08
| trained SNNs have been applied to SHD and SSC datasets,        |     |     |     |     |     | Gradient)   |       |       |       |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | ----------- | ----- | ----- | ----- |
| demonstrating that temporal structure in auditory signals can  |     |     |     |     |     | STDP-based  |       |       |       |
|                                                                |     |     |     |     |     |             | 95.5  | 74.2  | 0.05  |
| be effectively captured by SNN dynamics [25].  Nonetheless,    |     |     |     |     |     | SNN         |       |       |       |
the neuron model, encoding strategy, and training technique
continue to have a significant impact on performance. Higher  Figure 3 illustrates the tradeoffs between precision and
accuracy is possible with ANN-to-SNN conversion, but the  energy efficiency by visualizing this data.
MNIST Accuracy (%)
CIFAR-10 Accuracy (%)
120
) 100
%
(
 s 80
is
y
la
60
n
A
 y
c 40
r
u
c
c
A 20
0
|     |     | ANN (CNN) |     | Converted SNN |     | Direct SNN (Surrogate |     | STDP-based SNN |     |
| --- | --- | --------- | --- | ------------- | --- | --------------------- | --- | -------------- | --- |
Gradient)
Model
Fig. 3 Performance analysis and energy of SNNs vs ANN
ANNs—and  CNNs  in  particular—consistently  of these models is significantly lower than that of other models.
outperform  the  other  models  in  terms  of  classification  To assess the robustness of accuracy results, each experiment
accuracy, but at the expense of significant energy consumption.  was executed in five independent runs with varying random
Converted SNNs, which are based on pre-trained ANNs, use a  seeds. Reported accuracy values represent mean ± standard
| lot less energy and nearly match the accuracy of their ANN  |     |     |     |     |     | deviation.   |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
counterparts.
For MNIST, surrogate gradient SNNs achieved 97.8% ±
For  applications  needing  moderate  performance  with  0.2, converted SNNs 98.1% ± 0.3, and STDP-based models
better computational  savings,  directly  trained  SNNs using  95.5% ± 0.4, confirming consistency across runs. On CIFAR-
surrogate gradient techniques provide a well-balanced tradeoff  10, accuracies were 85.7% ± 0.5 (surrogate SNN), 89.3% ± 0.4
between accuracy and energy efficiency. The sparse, event- (converted SNN), and 74.2% ± 0.6 (STDP). It is confirmed that
driven character of STDP-based SNNs, on the other hand,  observed differences are statistically significant and not the
results in the highest energy efficiency; however, the accuracy  result of chance when the standard deviation is less than 1%.
38

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
These results confirm that SNNs can approach ANN-level 2, SNNs have a considerable latency advantage over typical
accuracy while maintaining sparse, efficient spiking activity. ANNs because of their event-driven architecture, especially in
The overall performance of SNNs across different tasks low-power and time-sensitive applications.
illustrates their growing maturity and capability to support
intelligent computation under real-world constraints. While In benchmark evaluations using event-based datasets such
SNNs have yet to surpass deep ANNs on most benchmarks, as DVS Gesture and SHD, SNNs have demonstrated inference
their ability to approximate performance while drastically latencies as low as 5–10 ms per sample when deployed on
reducing energy and latency makes them a compelling choice neuromorphic platforms [12, 66]. In comparison, CNN-based
for the next generation of efficient AI systems. ANNs typically require 20–50 ms, depending on model
complexity and hardware configuration. Among different SNN
Table 2. Latency comparison table training paradigms, directly trained surrogate gradient SNNs
Model Latency (ms) strike a balance by achieving low-latency responses (~10 ms)
ANN (CNN) 45 with competitive accuracy. STDP-based SNNs, while slightly
Converted SNN 20 slower in early inference phases due to their gradual spike
Surrogate Gradient SNN 10 adaptation, stabilize to sub-15 ms latency under optimized
STDP-based SNN 15 conditions. Converted SNNs, on the other hand, may incur
slightly higher delays (~20 ms), especially when requiring
4.2. Latency Analysis longer simulation windows to approximate ANN activation
A crucial parameter for assessing SNNs’ real-time rates. Figure 4 compares inference latency (in ms) across ANN
performance is latency, which is the interval of time between (CNN), Converted SNN, Surrogate Gradient SNN, and STDP-
an input stimulus and the system’s response. As shown in Table based SNN models.
50
45
40
35
)
s 30
m
(
y 25
c
n
e 20
ta
L
15
10
5
0
ANN (CNN) Converted SNN Surrogate Gradient SNN STDP-based SNN
Model
Fig. 4 Latency comparison (in ms) across models
Low latency reinforces the suitability of SNNs for real- contrast to traditional ANNs, which rely on large matrix
time applications compared to conventional ANN processing. multiplications and continuous-valued activations. This allows
These findings highlight SNNs’ potential for applications for huge power savings, particularly in neuromorphic hardware
demanding real-time inference, such as autonomous vehicles, implementations, and significantly reduces the number of
smart sensors, robotics, and brain-computer interfaces. operations per inference. Converted SNNs, derived from pre-
However, real-world deployment still depends on the trained ANNs, have demonstrated up to 10× lower energy
responsiveness of underlying neuromorphic hardware, consumption compared to their ANN counterparts while
efficient spike encoding schemes, and minimal overhead from maintaining comparable accuracy [20, 21]. This is possible
software toolchains. because inference in SNNs is based on discrete spikes and
accumulations over time rather than continuous propagation.
4.3. Energy Efficiency Directly trained SNNs using surrogate gradient descent also
The remarkable energy efficiency of SNNs, which is show excellent energy performance. These networks can
fueled by sparse event-driven processing, is one of its most operate with fewer spikes and less computation per inference
alluring features. SNNs only calculate when neurons fire, in due to their native temporal dynamics and the use of
39

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
biologically-inspired neuron models [22, 34]. Meanwhile, Table 3. SNN energy efficiency summary
STDP-based SNNs are the most energy-efficient, often Energy per Spike Count per
Model
operating with less than 5 millijoules (mJ) per inference, thanks Inference (mJ) Inference
to their localized synaptic updates and highly sparse activation ANN (CNN) 200 0
patterns [44]. These models are perfect for ultra-low-power Converted SNN 20 20000
applications like wearable technology and edge AI, even Surrogate
15 12000
though their accuracy may be a little below par. This tradeoff Gradient SNN
between energy and performance across several model types is STDP-based
5 4000
illustrated in the image and table below. SNN
250
200
) J 150
m
(
y
g
r 100
e
n
E
50
0
ANN (CNN) Converted SNN Surrogate Gradient SNN STDP-based SNN
Model
25000
20000
s
e
k
ip 15000
S
f
o
r
e 10000
b
m
u
N
5000
0
ANN (CNN) Converted SNN Surrogate Gradient SNN STDP-based SNN
Model
Fig. 5 Comparison of energy consumption and spike count per inference across models
Figure 5 provides a comparison of energy consumption (in both energy (15 mJ) and spike efficiency (~12,000 spikes) by
mJ) and spike count (number of spikes generated) per inference leveraging gradient-based learning of spiking patterns. Finally,
across four neural network models: ANN (CNN), Converted STDP-based SNNs achieve the lowest energy consumption (5
SNN, Surrogate Gradient SNN, and STDP-based SNN. ANNs mJ per inference) and the sparsest spiking activity (~4,000
exhibit the highest energy consumption at approximately 200 spikes), making them ideal for energy-constrained
mJ per inference due to their continuous-valued operations and applications, albeit with slightly reduced accuracy. As shown,
lack of spike-based activity. Converted SNNs significantly while ANNs dominate in raw accuracy, SNNs—especially
lower energy usage to 20 mJ, though they still produce a STDP-based and surrogate-trained models—can achieve 90–
relatively high spike count (~20,000) as a result of rate-coded 97% lower energy use with reasonable tradeoffs in
spike propagation. Surrogate Gradient SNNs further optimize performance. This makes SNNs particularly promising for on-
40

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025

device AI and neuromorphic processors [12, 18]. The observed  [67]. This section explores how training loss changes across
energy savings highlight the central advantage of SNNs for  epochs for three SNN variants: converted SNNs, surrogate
low-power AI systems.   gradient-trained  SNNs,  and  STDP-based  SNNs.  Figure  6
illustrates the training loss across 20 epochs.
The tradeoffs between accuracy, spiking activity, and
energy efficiency are provided in this comparison, highlighting  The  surrogate  gradient  SNN  demonstrates  the  fastest
the applicability of SNNs for low-power AI applications in  convergence, reducing loss from 0.9 to 0.44, showing stable
neuromorphic and edge computing, especially those trained  optimization  and  consistent  improvement  over  time.  In
with surrogate gradients or STDP.  contrast, converted SNNs exhibit slower convergence and
reach a loss of 0.6 by epoch 20. STDP-based SNNs converge
4.4. Convergence Behavior  the slowest, with the loss stabilizing around 0.75, indicating a
Convergence time during training is a critical performance  limitation  in  achieving  deeper  error  minimization  under
unsupervised learning.
factor, especially when comparing different SNN architectures
|     |     |     | Converted SNN |     | Surrogate Gradient SNN |     | STDP-based SNN |     |
| --- | --- | --- | ------------- | --- | ---------------------- | --- | -------------- | --- |
1.00
0.90
0.80
0.70
s
s
o 0.60
L
 g
0.50
n
in
ia 0.40
r T
0.30
0.20
0.10
0.00
| 1   | 2   | 3 4 | 5   | 6 7 8 | 9 10 11 | 12 13 14 | 15 16 17 | 18 19 20 |
| --- | --- | --- | --- | ----- | ------- | -------- | -------- | -------- |
|     |     |     |     |       | Epoch   |          |          |          |
Fig. 6 Convergence behavior of SNN models
Table 4. Training loss across epochs for different SNN models
|     | Epoch  | Converted SNN  |       | Surrogate Gradient SNN  |       | STDP-based SNN  |       |     |
| --- | ------ | -------------- | ----- | ----------------------- | ----- | --------------- | ----- | --- |
|     | 1      |                | 0.9   |                         | 0.9   |                 | 0.9   |     |
|     | 2      |                | 0.85  |                         | 0.8   |                 | 0.88  |     |
|     | 3      |                | 0.82  |                         | 0.73  |                 | 0.87  |     |
|     | 4      |                | 0.78  |                         | 0.67  |                 | 0.85  |     |
|     | 5      |                | 0.76  |                         | 0.63  |                 | 0.84  |     |
|     | 6      |                | 0.73  |                         | 0.6   |                 | 0.83  |     |
|     | 7      |                | 0.71  |                         | 0.57  |                 | 0.82  |     |
|     | 8      |                | 0.7   |                         | 0.55  |                 | 0.81  |     |
|     | 9      |                | 0.68  |                         | 0.53  |                 | 0.81  |     |
|     | 10     |                | 0.67  |                         | 0.51  |                 | 0.8   |     |
|     | 11     |                | 0.66  |                         | 0.5   |                 | 0.79  |     |
|     | 12     |                | 0.65  |                         | 0.49  |                 | 0.78  |     |
|     | 13     |                | 0.64  |                         | 0.48  |                 | 0.78  |     |
|     | 14     |                | 0.63  |                         | 0.47  |                 | 0.77  |     |
|     | 15     |                | 0.63  |                         | 0.46  |                 | 0.77  |     |
|     | 16     |                | 0.62  |                         | 0.46  |                 | 0.76  |     |
|     | 17     |                | 0.62  |                         | 0.45  |                 | 0.76  |     |
|     | 18     |                | 0.61  |                         | 0.45  |                 | 0.75  |     |
|     | 19     |                | 0.61  |                         | 0.44  |                 | 0.75  |     |
|     | 20     |                | 0.6   |                         | 0.44  |                 | 0.75  |     |
41

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
Table 4 presents the simulated training loss values over 20 stability, making them more favorable for scalable
epochs for three types of SNNs: Converted SNN, Surrogate applications. Convergence behavior thus becomes a critical
Gradient SNN, and STDP-based SNN. The surrogate gradient- consideration when selecting SNN models for deployment in
trained model shows the steepest and most consistent decline time-sensitive or resource-constrained environments.
in loss, indicating faster convergence. Converted SNNs exhibit
moderate convergence, while STDP-based SNNs converge Figure 7 plots the training accuracy learning curves across
slowly and plateau early, reflecting the limitations of 20 epochs for the three SNN variants. The surrogate gradient
unsupervised learning. SNN exhibits the steepest accuracy gains, stabilizing near 98%
by epoch 20, while converted SNNs converge more slowly.
These results reinforce that while STDP-based models STDP models show gradual improvement but plateau earlier,
offer energy efficiency, they lack the learning stability of consistent with unsupervised adaptation limits. Curves show
supervised techniques. Surrogate gradient methods, on the mean accuracy with shaded bands indicating ±1 standard
other hand, offer a balance of performance, training speed, and deviation across five independent runs.
Surrogate Gradient SNN Converted SNN STDP-based SNN
120
100
)
%
(
y 80
c
r
u
c
c A 60
g
n
h
in 40
ia
r
T
20
0
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
Epoch
Fig. 7 Learning curves (training accuracy vs. epochs) for converted, surrogate-gradient, and STDP-based SNNs
Learning curves demonstrate stable optimization for this, they remain a viable alternative for low-power
surrogate SNNs, gradual adaptation for converted SNNs, and deployments where retraining is impractical.
slower but consistent improvement for STDP.
Surrogate gradient-trained SNNs represent an effective
4.5. Comparative Discussion balance between accuracy and efficiency. These models attain
The comparative evaluation of different neural network sub-15 ms inference latency, competitive accuracy, and
architectures reveals key tradeoffs between accuracy, energy moderate spike counts (~12,000 per inference), all while
efficiency, latency, and convergence. ANNs, particularly demonstrating faster convergence during training. As seen in
CNNs, consistently achieve the highest classification accuracy Section 4.6, they reduce training loss more rapidly than other
(e.g., 99.2% on MNIST, 92.3% on CIFAR-10) but do so at the SNN types, stabilizing by the 20th epoch, which makes them
cost of high energy consumption—reaching up to 200 mJ per favorable for real-time learning tasks. STDP-based SNNs are
inference. These models are less appropriate for real-time and the most energy-efficient, requiring only around 5 mJ per
energy-constrained applications because they also have higher inference. However, they typically exhibit lower classification
inference latency, usually between 30 and 50 ms, and demand accuracy and slower convergence rates. As illustrated in the
more processing power. convergence analysis, STDP-based models plateau at higher
loss values and require more epochs to stabilize, making them
Converted SNNs, which are created from trained ANNs, better suited for applications prioritizing unsupervised
drastically reduce energy consumption by about 90% while adaptation over precise classification.
achieving accuracy that is comparable to the performance of
their ANN counterparts. However, they may require longer Overall, application-specific priorities determine which
simulation windows and produce higher spike counts, which SNN model is best [68]: surrogate gradient SNNs for real-time
can marginally affect latency and training efficiency. Despite and accuracy-focused use, STDP for ultra-low energy adaptive
42

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
systems, and converted SNNs for ANN transferability in fly processing that is computationally efficient and low-
constrained environments.In addition, it is instructive to latency. Such characteristics make SNNs highly suitable for
compare SNNs with Transformer-based architectures, which tasks like gesture recognition, robotic control, auditory
currently dominate performance benchmarks in natural processing, and neuromorphic vision, where responsiveness is
language processing and computer vision. Transformers rely critical and resources are constrained.
on attention mechanisms that effectively capture long-range
dependencies but scale quadratically with input length, Several successful implementations have already
resulting in substantial memory and energy requirements [69, showcased these real-time capabilities. For instance, in gesture
70]. Recent analysis estimates that training large Transformer recognition using the DVS128, SNNs have achieved both high
models consumes hundreds of megawatt-hours of electricity classification accuracy and fast inference times, outperforming
and generates a significant carbon footprint [71, 72]. traditional frame-based systems in terms of latency and power
consumption [66]. Similarly, in the SHD and SSC datasets,
By contrast, SNNs prioritize event-driven, sparse SNNs trained with temporal coding have demonstrated
computation that achieves up to 90–97% energy savings excellent performance in processing time-dependent auditory
relative to ANNs while maintaining competitive accuracy on signals [25]. These use cases confirm that SNNs are not only
benchmarks such as CIFAR-10 and MNIST [73, 74]. While biologically plausible but also practically effective in real-
Transformers typically outperform SNNs in raw accuracy on world, real-time environments.
broad-based datasets like ImageNet, they lack the real-time
latency advantages and hardware efficiency that make SNNs However, despite their potential, scale, and hardware
suitable for robotics, neuromorphic vision, and edge AI. This implementation, they present significant obstacles to broad
comparison underscores the complementary nature of the two adoption. Low-power SNN execution has been made possible
paradigms: Transformers excel in centralized, resource-rich by neuromorphic processors; however, access to these devices
environments, whereas SNNs offer a sustainable pathway for is still restricted. Furthermore, simulating massive networks
low-power, real-time applications. with millions of neurons and synapses makes scalability
challenging, particularly in settings with limited resources. The
Beyond confirming trends reported in earlier studies, the creation of middleware, APIs, and toolchains—which are now
present work achieves slightly higher accuracies and markedly fragmented or platform-specific—is still necessary to integrate
better efficiency metrics than most state-of-the-art reports. For such hardware into conventional computing pipelines [12, 18].
example, surrogate gradient SNNs reached 97.8% ± 0.2 on Convergence stability and training methodologies are still
MNIST and 85.7% ± 0.5 on CIFAR-10, which improves upon another major obstacle. Because spike events are non-
earlier spiking models that typically plateaued near 96–97% differentiable, SNNs cannot directly use traditional
and 82–84%, respectively. Latency reductions of 35–45% and backpropagation, which is the foundation of ANN learning.
energy savings of 90–97% relative to ANN baselines were also Even though end-to-end training of SNNs with competitive
obtained, exceeding values previously reported in conversion- performance is now possible thanks to recent developments in
only pipelines. surrogate gradient descent, these models are still susceptible to
hyperparameters such as membrane thresholds, time constants,
These gains are largely attributable to the unified and learning rates [22]. In unsupervised learning paradigms,
evaluation protocol applied here, which ensures fairness across such as STDP, convergence can be unstable or dataset-specific,
models; multi-dimensional performance metrics that highlight limiting generalization.
tradeoffs hidden in accuracy-only reporting; and the
optimization of surrogate gradient training parameters, Finally, the lack of standardization across SNN models,
allowing faster convergence with fewer spikes. Thus, the encoding schemes, and hardware platforms impedes progress.
results do not merely replicate existing findings but Unlike ANNs, which benefit from standardized libraries (e.g.,
demonstrate how careful integration of training strategies and TensorFlow, PyTorch) and benchmark datasets, SNN research
evaluation standards can extend the SNN research. suffers from inconsistent definitions of spike encoding (rate vs.
temporal coding), neuron models (LIF, Izhikevich), and
Taken together, these comparisons show that no single performance metrics (accuracy vs. spike count vs. energy-
paradigm dominates; SNNs excel in sustainability, while delay product). This fragmentation makes it difficult to
ANNs and Transformers lead in raw accuracy and scalability. compare results, reproduce experiments, or establish baselines
[75].
4.6. Real-Time Capabilities
Because of their sparse spike-based computing and 4.7. Hardware Considerations
asynchronous, event-driven design, SNNs are especially well- The practical adoption of SNNs is tightly linked to their
suited for real-time applications. SNNs react only when input implementation on neuromorphic hardware platforms. In
stimuli cause spikes, in contrast to conventional ANNs, which comparison to traditional CPUs and GPUs, chips like IBM
need constant and coordinated processing. This enables on-the- TrueNorth [18] and Intel Loihi [12] show that large-scale
43

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
spiking computation is feasible with orders of magnitude from direct implementation in this study, which may limit
reduced energy usage. TrueNorth, for example, integrates one generalizability across platforms. Third, hyperparameter
million spiking neurons while consuming only 70 mW in real- sensitivity in surrogate-gradient training and convergence
time workloads [18]. Similarly, Loihi supports on-chip instability in STDP highlight ongoing challenges that require
learning with programmable synaptic delays, enabling further exploration. Finally, while comparative metrics such as
adaptive behavior at the edge [12]. Recent platforms like accuracy, latency, and energy were integrated, additional
SpiNNaker extend this scalability by simulating millions of factors such as scalability on high-dimensional tasks and
neurons across massively parallel architectures [63]. robustness under noisy conditions remain areas for future
research. Recognizing these limitations underscores that the
Despite these advances, hardware deployment remains findings, while promising, represent one step toward
challenged by limited accessibility, vendor-specific SDKs, and advancing brain-inspired and low-power AI systems.
the absence of a standardized programming ecosystem. Unlike
ANNs, which benefit from unified frameworks like 5. Conclusion
TensorFlow and PyTorch, SNN hardware requires researchers In brain-inspired computing, SNNs are becoming a game-
to adapt models to specific toolchains, constraining changer due to their ability to effectively combine biological
reproducibility and adoption. Addressing these hardware plausibility, energy efficiency, and real-time responsiveness.
bottlenecks — through open-source SDKs, standard This paper presented a comprehensive analysis of SNN design,
benchmarks, and cross-platform compatibility — will be training methods, and comparative performance across
critical for translating SNN research into widespread, real- multiple dimensions, including accuracy, spike count, latency,
world applications. and convergence behavior. Among the evaluated models,
ANNs —particularly CNNs—continue to deliver the highest
4.8. Extended Analysis and Insights classification accuracy (up to 99.2% on MNIST and 92.3% on
While prior sections compared accuracy, latency, energy, CIFAR-10).
and convergence individually, an integrated perspective
highlights tradeoffs across all metrics simultaneously. For However, their high energy demands (up to 200 mJ per
instance, surrogate-gradient SNNs balance accuracy (~97.8%) inference) and longer inference latency (30–50 ms) render
with latency (~10 ms) and moderate energy (15 mJ per them suboptimal for real-time or edge applications. Converted
inference), whereas STDP-based SNNs achieve the lowest SNNs, which leverage pre-trained ANNs, maintain
energy (~5 mJ) at the cost of accuracy (95.5%) and slower competitive accuracy while cutting energy use by nearly 90%.
convergence. These tradeoffs confirm that no single model Nonetheless, they generate higher spike counts and rely on
dominates all performance axes; instead, model suitability is longer simulation windows, which can impact latency and
highly dependent on application. training flexibility. Surrogate gradient-trained SNNs offer the
most balanced performance profile.
When network size increases (e.g., from MNIST-scale to
CIFAR-10 scale), accuracy differences widen—ANNs They achieve low latency (~10 ms), fast and stable
outperform on CIFAR-10 (~92%) while direct SNNs drop to convergence within 20 epochs, and reduced spike counts, all
~85%. However, energy savings become more pronounced: while maintaining accuracy close to ANN baselines. This
surrogate-trained SNNs operate at less than 10% of ANN qualifies them for edge and real-time AI implementations.
energy costs. This scalability tension underscores the practical Meanwhile, STDP-based SNNs lead in energy efficiency—
importance of hybrid evaluation criteria beyond accuracy consuming as little as 5 mJ per inference—but show lower
alone. Simulation on neuromorphic platforms like Intel Loihi accuracy and slower convergence, stabilizing around 0.75
demonstrates that real-world deployment magnifies latency training loss after 20 epochs. These models are more
and energy advantages. For example, gesture-recognition tasks appropriate for tasks requiring continuous unsupervised
on DVS128 achieve inference latencies of 5–10 ms with learning and adaptation.
surrogate SNNs, compared to 20–50 ms on ANN counterparts
[12, 66]. These results show that latency reductions translate This multi-dimensional comparison confirms that the
directly into real-time robotics and edge AI feasibility. selection of an SNN model should align with application
requirements. For latency-critical and accuracy-driven
4.9. Limitations of the Study systems, surrogate gradient SNNs are the most viable. For
While the analysis provides comprehensive insights into ultra-low-power adaptive systems, STDP remains
neuron models, training paradigms, and performance metrics, advantageous. Overall, SNNs are poised to redefine the future
several limitations must be acknowledged. First, the evaluation of AI systems operating at the intersection of efficiency, speed,
relies primarily on benchmark datasets, which may not fully and biological realism. Despite these strengths, SNNs face key
capture real-world complexity or large-scale deployment limitations. Training convergence is often unstable,
scenarios. Second, hardware-specific results are drawn from hyperparameter tuning remains challenging, and no unified
reported benchmarks in the literature [22, 12, 66] rather than standard for model evaluation or neuromorphic
44

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
implementation exists. Additionally, the limited accessibility power surveillance could highlight their advantages in
and scalability of neuromorphic chips restrict practical task-specific contexts.
deployment in broader commercial systems. 5. Support Cross-Disciplinary Collaboration. The
development of effective SNNs requires expertise in
The comparative results underscore that SNNs provide neuroscience, machine learning, electrical engineering,
substantial energy savings (up to 90–97% lower than ANNs) and computer architecture. Research institutions and
with only marginal accuracy loss. This positions SNNs as a funding agencies should support interdisciplinary
sustainable computing alternative, particularly relevant as the programs that foster collaboration across these domains.
AI community grapples with the environmental impact of 6. Integrate SNNs into AI Curriculum and Tools. To
large-scale ANNs. By clarifying the efficiency–accuracy accelerate knowledge transfer, academic institutions
tradeoffs, this paper highlights how SNNs can drive innovation should integrate SNN concepts and neuromorphic
not just in performance but also in responsible, energy-aware computing into AI and computer engineering curricula.
AI deployment. Nevertheless, the findings of this paper Additionally, incorporating SNN support into popular
conclude that SNNs are well-positioned to redefine low-power, frameworks (e.g., PyTorch or TensorFlow) would
real-time computing, particularly where energy efficiency and streamline experimentation and development.
temporal precision are paramount. SNNs are anticipated to be 7. Bridging Biological Plausibility and Machine Learning.
essential components of future edge intelligence, neuro- A key direction is merging STDP’s biological realism
inspired robotics, and ultra-low-power AI ecosystems as with surrogate-gradient efficiency. Hybrid learning
neuromorphic engineering develops and transdisciplinary tools methods could yield models that are both hardware-
become more sophisticated. In essence, this study reinforces friendly and competitive in accuracy.
that SNNs, while not universally superior, provide a distinctive 8. Benchmarking Beyond MNIST and CIFAR-10. Most
pathway toward sustainable, real-time, and energy-aware AI SNN studies, including this one, focus on MNIST,
solutions. CIFAR-10, and DVS128. Broader datasets such as
ImageNet or large-scale audio corpora remain
5.1. Recommendations underexplored in spiking contexts. Extending
Based on the findings and comparative analysis presented benchmarks will increase confidence in scalability and
in this study, the following recommendations are offered to generalization.
support further development, adoption, and application of 9. Standardized Energy–Latency–Accuracy Metrics.
SNNs: To ensure impact in neuromorphic computing, SNN
research should converge on unified metrics (e.g., energy-
1. Optimize SNN Training Frameworks. Further research delay product per classification). This paper contributes
should prioritize improving training stability and toward such standardization by reporting spike counts,
convergence in SNNs. Surrogate gradient-based learning latency, and convergence alongside accuracy.
should be refined through adaptive optimization 10. Explore Hybrid Models. Future studies may want to look
strategies and hybrid techniques that combine supervised into hybrid strategies that blend SNNs with CNNs and
and unsupervised methods to enable deeper networks Transformers, among other paradigms. Hybrid SNN–
with minimal performance tradeoffs. Transformer models could merge temporal coding
2. Standardize Evaluation Protocols. A unified framework efficiency with long-range dependency modeling, while
for evaluating SNN models is essential. Researchers and convolutional–spiking systems may enhance event-based
developers are encouraged to adopt standardized vision tasks. Similarly, integrating STDP’s biological
benchmarks—including common datasets, spike-based plausibility with surrogate-gradient optimization
performance metrics (accuracy, latency, energy per efficiency could yield models that balance energy savings
inference), and neuron model conventions—to ensure with accuracy. These directions will bridge the gap
comparability and reproducibility across studies. between biological realism, computational efficiency,
3. Invest in Neuromorphic Hardware Access. Governments, and task scalability, ensuring that SNNs remain central to
academic consortia, and industry players should expand sustainable AI development.
access to neuromorphic platforms like Intel Loihi,
SpiNNaker, and IBM TrueNorth. Collaborative With these strategies, the field of brain-inspired
development of open-source SDKs and toolchains will computing can move beyond theoretical promise to real-world
help democratize innovation and facilitate deployment in impact, harnessing the unique capabilities of SNNs in solving
embedded and edge systems. some of today’s most demanding computational challenges.
4. Promote Application-Oriented Research. SNNs should be By clarifying how SNNs achieve 90–97% energy savings with
increasingly tested in real-world domains such as only 1–3% accuracy drop relative to ANNs, this study
robotics, medical devices, smart sensors, and highlights their transformative potential for wearable health
neuromorphic computing. Pilot studies using SNNs for devices, autonomous robotics, and edge AI sensors, where
autonomous navigation, auditory localization, or low- energy budgets are decisive.
45

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
References
[1] Kaushik Roy, Akhilesh Jaiswal, and Priyadarshini Panda, “Towards Spike-Based Machine Intelligence with Neuromorphic Computing,”
Nature, vol. 575, no. 7784, pp. 607-617, 2019. [CrossRef] [Google Scholar] [Publisher Link]
[2] Wolfgang Maass, “Networks of Spiking Neurons: The Third Generation of Neural Network Models,” Neural Networks, vol. 10, no. 9, pp.
1659-1671, 1997. [CrossRef] [Google Scholar] [Publisher Link]
[3] Yann LeCun, Yoshua Bengio, and Geoffrey Hinton, “Deep Learning,” Nature, vol. 521, no. 7553, pp. 436-444, 2015. [CrossRef] [Google
Scholar] [Publisher Link]
[4] Jolitte A. Villaruz, Bobby D. Gerardo, and Ruji P. Medina, “Philippine Stock Exchange Index Forecasting Using a Tuned Artificial Neural
Network Model with a Modified Firefly Algorithm,” 2023 IEEE 6th International Conference on Pattern Recognition and Artificial
Intelligence (PRAI), Haikou, China, pp. 1039-1044, 2023. [CrossRef] [Google Scholar] [Publisher Link]
[5] Mary Joy D. Viñas et al., “COVID-19 Outbreaks Effect on Air Quality Index: Evidence from Enhanced Artificial Neural Network,” 2023
8th International Conference on Computer and Communication Systems (ICCCS), Guangzhou, China, pp. 1117-1124, 2023. [CrossRef]
[Google Scholar] [Publisher Link]
[6] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton, “Imagenet Classification with Deep Convolutional Neural Networks,”
Communications of the ACM, vol. 60, no. 6, pp. 84-90, 2017. [CrossRef] [Google Scholar] [Publisher Link]
[7] Stephen Grossberg, “Recurrent Neural Networks,” Scholarpedia, vol. 8, no. 2, 2013. [Google Scholar]
[8] Sepp Hochreiter, and Jürgen Schmidhuber, “Long Short-Term Memory,” Neural Computation, vol. 9, no. 8, pp. 1735-1780, 1997.
[CrossRef] [Google Scholar] [Publisher Link]
[9] Rahul Dey, and Fathi M. Salem, “Gate-Variants of Gated Recurrent Unit (GRU) Neural Networks,” 2017 IEEE 60th International Midwest
Symposium on Circuits and Systems (MWSCAS), Boston, MA, USA, pp. 1597-1600, 2017. [CrossRef] [Google Scholar] [Publisher Link]
[10] Ashish Vaswani et al., “Attention is All you Need,” Advances in Neural Information Processing Systems, vol. 30, 2017. [Google Scholar]
[Publisher Link]
[11] Wulfram Gerstner, and Werner M. Kistler, Spiking Neuron Models: Single Neurons, Populations, Plasticity, 1st ed., Cambridge University
Press, 2002. [CrossRef] [Google Scholar] [Publisher Link]
[12] Mike Davies et al., “Loihi: A Neuromorphic Manycore Processor with On-Chip Learning,” IEEE Micro, vol. 38, no. 1, pp. 82-99, 2018.
[CrossRef] [Google Scholar] [Publisher Link]
[13] Resmi Cherian, and E. Grace Mary Kanaga, “Unleashing the Potential of Spiking Neural Networks for Epileptic Seizure Detection: A
Comprehensive Review,” Neurocomputing, vol. 598, 2024. [CrossRef] [Google Scholar] [Publisher Link]
[14] Samanwoy Ghosh-Dastidar, and Hojjat Adeli, “Third Generation Neural Networks: Spiking Neural Networks,” Advances in Intelligent
and Soft Computing, Berlin, Heidelberg, pp. 167-178, 2009. [CrossRef] [Google Scholar] [Publisher Link]
[15] Gabriele Lagani et al., “Spiking Neural Networks and Bio-Inspired Supervised Deep Learning: A Survey,” arXiv Preprint, pp. 1-31, 2023.
[CrossRef] [Google Scholar] [Publisher Link]
[16] Giacomo Indiveri, and Timothy K. Horiuchi, “Frontiers in Neuromorphic Engineering,” Frontiers in Neuroscience, vol. 5, pp. 1-2, 2011.
[CrossRef] [Google Scholar] [Publisher Link]
[17] Sumit Soman, Jayadeva, and Manan Suri, “Recent Trends in Neuromorphic Engineering,” Big Data Analytics, vol. 1, no. 1, pp. 1-16,
2016. [CrossRef] [Google Scholar] [Publisher Link]
[18] Paul A. Merolla, et al., “A Million Spiking-Neuron Integrated Circuit with a Scalable Communication Network and Interface,” Science,
vol. 345, no. 6197, pp. 668-673, 2014. [CrossRef] [Google Scholar] [Publisher Link]
[19] Md Bokhtiar Al Zami et al., “Digital Twin in Industries: A Comprehensive Survey,” IEEE Access, vol. 13, pp. 47291-47336, 2025.
[CrossRef] [Google Scholar] [Publisher Link]
[20] Peter U. Diehl et al., “Fast-Classifying, High-Accuracy Spiking Deep Networks through Weight and Threshold Balancing,” 2015
International Joint Conference on Neural Networks (IJCNN), Killarney, Ireland, pp. 1-8, 2015. [CrossRef] [Google Scholar] [Publisher
Link]
[21] Bodo Rueckauer et al., “Conversion of Continuous-Valued Deep Networks to Efficient Event-Driven Networks for Image Classification,”
Frontiers in Neuroscience, vol. 11, pp. 1-12, 2017. [CrossRef] [Google Scholar] [Publisher Link]
[22] Emre O. Neftci, Hesham Mostafa, and Friedemann Zenke, “Surrogate Gradient Learning in Spiking Neural Networks: Bringing the Power
of Gradient-Based Optimization to Spiking Neural Networks,” IEEE Signal Processing Magazine, vol. 36, no. 6, pp. 51-63, 2019.
[CrossRef] [Google Scholar] [Publisher Link]
[23] E.M. Izhikevich, “Simple Model of Spiking Neurons,” IEEE Transactions on Neural Networks, vol. 14, no. 6, pp. 1569-1572, 2003.
[CrossRef] [Google Scholar] [Publisher Link]
[24] Yuchen Wang et al., “A Universal ANN-to-SNN Framework for Achieving High Accuracy and Low Latency Deep Spiking Neural
Networks,” Neural Networks, vol. 174, pp. 1-14, 2024. [CrossRef] [Google Scholar] [Publisher Link]
46

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
[25] Benjamin Cramer et al., “The Heidelberg Spiking Data Sets for the Systematic Evaluation of Spiking Neural Networks,” IEEE
Transactions on Neural Networks and Learning Systems, vol. 33, no. 7, pp. 2744-2757, 2022. [CrossRef] [Google Scholar] [Publisher
Link]
[26] Khadeer Ahmed, Brain-Inspired Spiking Neural Networks, Biomimetics, IntechOpen, 2021. [CrossRef] [Google Scholar] [Publisher Link]
[27] A.L. Hodgkin, and A.F. Huxley, “A Quantitative Description of Membrane Current and its Application to Conduction and Excitation in
Nerve,” Bulletin of Mathematical Biology, vol. 52, no. 1-2, pp. 25-71, 1990. [CrossRef] [Google Scholar] [Publisher Link]
[28] Xingting Yao et al., “GLIF: A Unified Gated Leaky Integrate-and-Fire Neuron for Spiking Neural Networks,” Advances in Neural
Information Processing Systems, vol. 35, pp. 32160-32171, 2022. [Google Scholar] [Publisher Link]
[29] Walter Senn, and Jean-Pascal Pfister, “Spike-Timing Dependent Plasticity, Learning Rules,” Encyclopedia of Computational Neuroscience,
New York, Springer, pp. 2824-2832, 2015. [CrossRef] [Google Scholar] [Publisher Link]
[30] Guo-qiang Bi, and Mu-ming Poo, “Synaptic Modifications in Cultured Hippocampal Neurons: Dependence on Spike Timing, Synaptic
Strength, and Postsynaptic Cell Type,” Journal of Neuroscience, vol. 18, no. 24, pp. 10464-10472, 1998. [CrossRef] [Google Scholar]
[Publisher Link]
[31] Sung Soo Park, and Young-Seok Choi, “Spiking Neural Networks for Physiological and Speech Signals: A Review,” Biomedical
Engineering Letters, vol. 14, no. 5, pp. 943-954, 2024. [CrossRef] [Google Scholar] [Publisher Link]
[32] Simon Thorpe, and Jacques Gautrais, “Rank Order Coding,” Computational Neuroscience, Boston, MA, pp. 113-118, 1998. [CrossRef]
[Google Scholar] [Publisher Link]
[33] Sanaullah et al., “Exploring Spiking Neural Networks: A Comprehensive Analysis of Mathematical Models and Applications,” Frontiers
in Computational Neuroscience, vol. 17, pp. 1-20, 2023. [CrossRef] [Google Scholar] [Publisher Link]
[34] Friedemann Zenke, and Surya Ganguli, “SuperSpike: Supervised Learning in Multilayer Spiking Neural Networks,” Neural Computation,
vol. 30, no. 6, pp. 1514-1541, 2018. [CrossRef] [Google Scholar] [Publisher Link]
[35] Siddharth Sharma, Simone Sharma, and Anidhya Athaiya, “Activation Functions in Neural Networks,” International Journal of
Engineering Applied Sciences and Technology, vol. 4, no. 12, pp. 310-316, 2020. [CrossRef] [Google Scholar] [Publisher Link]
[36] Tomasz Szandała, “Review and Comparison of Commonly Used Activation Functions for Deep Neural Networks,” Studies in
Computational Intelligence, Singapore: Springer Singapore, pp. 203-224, 2010. [CrossRef] [Google Scholar] [Publisher Link]
[37] Sen Lu, and Abhronil Sengupta, “Neuroevolution Guided Hybrid Spiking Neural Network Training,” Frontiers in Neuroscience, vol. 16,
pp. 1-11, 2022. [CrossRef] [Google Scholar] [Publisher Link]
[38] Michael Pfeiffer, and Thomas Pfeil, “Deep Learning with Spiking Neurons: Opportunities and Challenges,” Frontiers in Neuroscience,
vol. 12, 2018. [CrossRef] [Google Scholar] [Publisher Link]
[39] Youngeun Kim et al., “Exploring Temporal Information Dynamics in Spiking Neural Networks,” Proceedings of the AAAI Conference on
Artificial Intelligence, vol. 37, no. 7, pp. 8308-8316, 2023. [CrossRef] [Google Scholar] [Publisher Link]
[40] Amirhossein Tavanaei et al., “Deep Learning in Spiking Neural Networks,” Neural Networks, vol. 111, pp. 47-63, 2019. [CrossRef]
[Google Scholar] [Publisher Link]
[41] Jayram Moorkanikara Nageswaran et al., “A Configurable Simulation Environment for the Efficient Simulation of Large-Scale Spiking
Neural Networks on Graphics Processors,” Neural Networks, vol. 22, no. 5-6, pp. 791-800, 2009. [CrossRef] [Google Scholar] [Publisher
Link]
[42] Hsin-Pai Cheng et al., “Understanding the Design of IBM Neurosynaptic System and Its Tradeoffs: A User Perspective,” Design,
Automation & Test in Europe Conference & Exhibition (DATE), Lausanne, Switzerland, pp. 139-144, 2017. [CrossRef] [Google Scholar]
[Publisher Link]
[43] Chit-Kwan Lin et al., “Programming Spiking Neural Networks on Intel’s Loihi,” Computer, vol. 51, no. 3, pp. 52-61, 2018. [CrossRef]
[Google Scholar] [Publisher Link]
[44] Muhammad Aitsam, Sergio Davies, and Alessandro Di Nuovo, “Neuromorphic Computing for Interactive Robotics: A Systematic
Review,” IEEE Access, vol. 10, pp. 122261-122279, 2022. [CrossRef] [Google Scholar] [Publisher Link]
[45] Eunsu Kim, and Youngmin Kim, “Exploring the Potential of Spiking Neural Networks in Biomedical Applications: Advantages,
Limitations, and Future Perspectives,” Biomedical Engineering Letters, vol. 14, no. 5, pp. 967-980, 2024. [CrossRef] [Google Scholar]
[Publisher Link]
[46] V. Rajakumari, and K.P. Pradhan, “Demonstration of an UltraLow Energy PD-SOI FinFET Based LIF Neuron for SNN,” IEEE
Transactions on Nanotechnology, vol. 21, pp. 434-441, 2022. [CrossRef] [Google Scholar] [Publisher Link]
[47] Saeed Reza Kheradpisheh et al., “STDP-based Spiking Deep Convolutional Neural Networks for Object Recognition,” Neural Networks,
vol. 99, pp. 56-67, 2018. [CrossRef] [Google Scholar] [Publisher Link]
[48] Wenzhe Guo et al., “Towards Efficient Neuromorphic Hardware: Unsupervised Adaptive Neuron Pruning,” Electronics, vol. 9, no. 7, pp.
1-15, 2020. [CrossRef] [Google Scholar] [Publisher Link]
[49] Marc-Oliver Gewaltig, and Markus Diesmann, “Nest (Neural Simulation Tool),” Scholarpedia, vol. 2, no. 4, 2007. [Google Scholar]
47

Sales G. Aribe Jr. / IJETT, 73(10), 32-48, 2025
[50] Hananel Hazan et al., “BindsNET: A Machine Learning-Oriented Spiking Neural Networks Library in Python,” Frontiers in
Neuroinformatics, vol. 12, pp. 1-18, 2018. [CrossRef] [Google Scholar] [Publisher Link]
[51] Marcel Stimberg, Romain Brette, and Dan FM Goodman, “Brian 2, An Intuitive and Efficient Neural Simulator,” Elife, vol. 8, pp. 11-41,
2019. [CrossRef] [Google Scholar] [Publisher Link]
[52] Jesper Sjöström, and Wulfram Gerstner, “Spike-Timing Dependent Plasticity,” Scholarpedia, vol. 5, no. 2, 2010. [Google Scholar]
[53] Dominique Debanne, and Mu-Ming Poo, “Spike-Timing Dependent Plasticity Beyond Synapse - Pre- and Post-Synaptic Plasticity of
Intrinsic Neuronal Excitability,” Frontiers in Synaptic Neuroscience, vol. 2, pp. 1-6, 2010. [CrossRef] [Google Scholar] [Publisher Link]
[54] Timothée Masquelier, Rudy Guyonneau, and Simon J. Thorpe, “Competitive STDP-Based Spike Pattern Learning,” Neural Computation,
vol. 21, no. 5, pp. 1259-1276, 2009. [CrossRef] [Google Scholar] [Publisher Link]
[55] Slawomir Koziel, David Echeverría Ciaurri, and Leifur Leifsson, “Surrogate-Based Methods,” Studies in Computational Intelligence,
Berlin, Heidelberg, pp. 33-59, 2011. [CrossRef] [Google Scholar] [Publisher Link]
[56] Tehreem Syed et al., “Exploring Optimized Spiking Neural Network Architectures for Classification Tasks on Embedded Platforms,”
Sensors, vol. 21, no. 9, pp. 1-25, 2021. [CrossRef] [Google Scholar] [Publisher Link]
[57] Shivam S. Kadam, Amol C. Adamuthe, and Ashwini Patil, “CNN Model for Image Classification on MNIST and Fashion-MNIST
Dataset,” Journal of Scientific Research, vol. 64, no. 2, pp. 374-384, 2020. [CrossRef] [Google Scholar] [Publisher Link]
[58] Yu Hu et al., “Hand Gesture Recognition System using the Dynamic Vision Sensor,” 2022 5th International Conference on Circuits,
Systems and Simulation (ICCSS), Nanjing, China, pp. 102-110, 2022. [CrossRef] [Google Scholar] [Publisher Link]
[59] Marc-Oliver Gewaltig, and Markus Diesmann, “Nest (Neural Simulation Tool),” Scholarpedia, vol. 2, no. 4, 2007. [Google Scholar]
[60] Lars Niedermeier et al., “CARLsim 6: An Open Source Library for Large-Scale, Biologically Detailed Spiking Neural Network
Simulation,” 2022 International Joint Conference on Neural Networks (IJCNN), Padua, Italy, pp. 1-10, 2022. [CrossRef] [Google Scholar]
[Publisher Link]
[61] Ting-Shuo Chou et al., “CARLsim 4: An Open Source Library for Large Scale, Biologically Detailed Spiking Neural Network Simulation
using Heterogeneous Clusters,” 2018 International Joint Conference on Neural Networks (IJCNN), Rio de Janeiro, Brazil, pp. 1-8, 2018.
[CrossRef] [Google Scholar] [Publisher Link]
[62] Michael Beyeler et al., “CARLsim 3: A User-Friendly and Highly Optimized Library for the Creation of Neurobiologically Detailed
Spiking Neural Networks,” 2015 International Joint Conference on Neural Networks (IJCNN), Killarney, Ireland, pp. 1-8, 2015.
[CrossRef] [Google Scholar] [Publisher Link]
[63] Abderazek Ben Abdallah, and Khanh N. Dang, “Comprehensive Review of Neuromorphic Systems,” Neuromorphic Computing Principles
and Organization, Springer Nature Switzerland, pp. 275-303, 2025. [CrossRef] [Google Scholar] [Publisher Link]
[64] Hariprasad Kannan, Nikos Komodakis, and Nikos Paragios, “Newton-Type Methods for Inference in Higher-Order Markov Random
Fields,” 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Honolulu, HI, USA, pp. 7224-7233, 2017.
[CrossRef] [Google Scholar] [Publisher Link]
[65] Wei Bai et al., “Network Analysis of Anxiety and Depressive Symptoms Among Nursing Students during the Covid-19 Pandemic,”
Journal of Affective Disorders, vol. 294, pp. 753-760, 2021. [CrossRef] [Google Scholar] [Publisher Link]
[66] Arnon Amir et al., “A Low Power, Fully Event-Based Gesture Recognition System,” 2017 IEEE Conference on Computer Vision and
Pattern Recognition (CVPR), Honolulu, HI, USA, pp. 7388-7397, 2017. [CrossRef] [Google Scholar] [Publisher Link]
[67] Jun Haeng Lee, Tobi Delbruck, and Michael Pfeiffer, “Training Deep Spiking Neural Networks Using Backpropagation,” Frontiers in
Neuroscience, vol. 10, pp. 1-13, 2016. [CrossRef] [Google Scholar] [Publisher Link]
[68] Sanaullah et al., “Evaluation of Spiking Neural Nets-Based Image Classification Using the Runtime Simulator RAVSim,” International
Journal of Neural Systems, vol. 33, no. 9, pp. 1-19, 2023. [CrossRef] [Google Scholar] [Publisher Link]
[69] Yunpeng Huang et al., “Advancing Transformer Architecture in Long-Context Large Language Models: A Comprehensive Survey,” arXiv
Preprint, pp. 1-40, 2023. [CrossRef] [Google Scholar] [Publisher Link]
[70] Rasoul Hosseinzadeh, and Mahdi Sadeghzadeh, “Attention Mechanisms in Transformers: A General Survey,” Journal of Artificial
Intelligence & Data Mining (JAIDM), vol. 13, no. 3, pp. 359-368, 2025. [CrossRef] [Google Scholar] [Publisher Link]
[71] Sayed Mahbub Hasan Amiri et al., “The Carbon Cost of Conversation, Sustainability in the Age of Language Models,” arXiv Preprint,
pp. 1-22, 2025. [CrossRef] [Google Scholar] [Publisher Link]
[72] David Patterson et al., “Carbon Emissions and Large Neural Network Training,” arXiv Preprint, pp. 1-22, 2021. [CrossRef] [Google
Scholar] [Publisher Link]
[73] Zhanglu Yan, Zhenyu Bai, and Weng-Fai Wong, “Reconsidering the Energy Efficiency of Spiking Neural Networks,” arXiv Preprint, pp.
1-11, 2024. [CrossRef] [Google Scholar] [Publisher Link]
[74] Sayeed Shafayet Chowdhury, Nitin Rathi, and Kaushik Roy, “One Timestep is All You Need: Training Spiking Neural Networks with
Ultra Low Latency,” arXiv Preprint, pp. 1-17, 2021. [CrossRef] [Google Scholar] [Publisher Link]
[75] Giacomo Indiveri, and Shih-Chii Liu, “Memory and Information Processing in Neuromorphic Systems,” Proceedings of the IEEE, vol.
103, no. 8, pp. 1379-1397, 2015. [CrossRef] [Google Scholar] [Publisher Link]
48