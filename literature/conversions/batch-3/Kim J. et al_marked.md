---
conversion_metadata:
  converted_at: "2026-07-21T13:47:59Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Kim J. et al.pdf"
  source_pdf_sha256: "a7f453644374906969d9bbf8282b81fb068ad34f57e60b22d2f8b0a9fca3944a"
  page_count: 95
  markdown_char_count: 634027
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Artificial Intelligence Review (2025) 58:216
https://doi.org/10.1007/s10462-025-11223-9

A comprehensive survey of deep learning for time series 
forecasting: architectural diversity and open challenges

Jongseon Kim1,4 · Hyungjoon Kim1,5 · HyunGi Kim2 · Dongjun Lee1 · Sungroh Yoon1,2,3

Accepted: 4 April 2025 / Published online: 23 April 2025
© The Author(s) 2025

Abstract
Time series forecasting is a critical task that provides key information for decision-making 
across various fields, such as economic planning, supply chain management, and medical 
diagnosis. After  the  use  of  traditional  statistical  methodologies  and  machine  learning  in 
the  past,  various  fundamental  deep  learning  architectures  such  as  MLPs,  CNNs,  RNNs, 
and  GNNs  have  been  developed  and  applied  to  solve  time  series  forecasting  problems. 
However,  the  structural  limitations  caused  by  the  inductive  biases  of  each  deep  learning 
architecture constrained their performance. Transformer models, which excel at handling 
long-term dependencies, have become significant architectural components for time series 
forecasting.  However,  recent  research  has  shown  that  alternatives  such  as  simple  linear 
layers can outperform Transformers. These findings have opened up new possibilities for 
using diverse architectures, ranging from fundamental deep learning models to emerging 
architectures  and  hybrid  approaches.  In  this  context  of  exploration  into  various  models, 
the architectural modeling of time series forecasting has now entered a renaissance. This 
survey  not  only  provides  a  historical  context  for  time  series  forecasting  but  also  offers 
comprehensive and timely analysis of the movement toward architectural diversification. 
By comparing and re-examining various deep learning models, we uncover new perspec-
tives  and  present  the  latest  trends  in  time  series  forecasting,  including  the  emergence  of 
hybrid models, diffusion models, Mamba models, and foundation models. By focusing on 
the inherent characteristics of time series data, we also address open challenges that have 
gained attention in time series forecasting, such as channel dependency, distribution shift, 
causality,  and  feature  extraction.  This  survey  explores  vital  elements  that  can  enhance 
forecasting performance through diverse approaches. These contributions help lower entry 
barriers  for  newcomers  by  providing  a  systematic  understanding  of  the  diverse  research 
areas  in  time  series  forecasting  (TSF),  while  offering  seasoned  researchers  broader  per-
spectives and new opportunities through in-depth exploration of TSF challenges.

Keywords  Time series forecasting · Deep learning · Foundation model · Distribution 
shift · Causality

Jongseon Kim and Hyungjoon Kim have contributed equally to this work.

Extended author information available on the last page of the article

1 3

---

<!-- PAGE 2 -->

216  Page 2 of 95

1  Introduction

Time series forecasting (TSF) is a task that predicts future values based on sequential his-
torical data (Cryer 1986). It is utilized as a key decision-making tool in various fields, such 
as economics and finance, supply chain management, transportation, energy, weather, and 
healthcare (Danese and Kalchschmidt 2011; Abu-Mostafa and Atiya 1996; Alghamdi et al 
2019; Nti et al 2020; Dimri et al 2020; Soyiri and Reidpath 2013). Such applications offer 
various  opportunities,  including  cost  reduction,  increased  efficiency,  and  enhanced  com-
petitiveness (Danese and Kalchschmidt 2011). The diversity and complexity of time series 
data make forecasting challenging. In addition to apparent information, hidden patterns and 
irregular values pose challenges in learning temporal dependencies (Chen et al 2024d).

In multivariate problems, additional factors such as channel correlation make the task 
even more difficult (Sect. 2.1). Furthermore, time series data exhibits different characteris-
tics depending on the domain, and the various times and environments in which the series 
is collected result in significantly different patterns (Sect. 2.3). Because of this, TSF prob-
lems exhibit limited model generalizability, requiring diverse architectures and approaches. 
The increasingly complicated TSF problems are presenting researchers with growing chal-
lenges, which has recently led to the active development of new methodologies and algo-
rithms to address these issues (Lim and Zohren 2021).

TSF  is  closely  connected  to  core AI  challenges,  and  solving  these  problems  plays  a 
crucial role in advancing the field of AI. For instance, the generalization of AI models is 
essential for ensuring stable performance on new data. However, time series data presents 
unique  characteristics  and  domain-specific  patterns  that  make  generalization  particularly 
challenging (Han et al 2023b). Solutions to generalization in TSF provide new insights that 
are applicable to other fields, such as Natural Language Processing (NLP) and Computer 
Vision (CV). The distribution of real-world time series data can change over time, and mod-
els must effectively handle these changes (Sect. 5.2). TSF plays a crucial role in addressing 
distribution shift issues, and the techniques developed to solve these problems can extend 
to  other AI  domains,  such  as  image,  video,  and  NLP.  Moreover,  attempts  to  understand 
models are crucial for improving their trustworthiness in real-world applications (Han et al 
2023a). In mission-critical fields such as healthcare and finance, the explainability of time 
series prediction models is essential. For example, explaining how stock price predictions or 
patient vital sign forecasts are made can help users better understand and trust the model’s 
decisions.  Thus,  TSF  research  in  explainability  provides  practical  solutions  for  other AI 
applications (Sect. 5.6). Recently, TSF has evolved beyond simple forecasting, establish-
ing itself as a practical platform for addressing key AI challenges. Solving these problems 
within TSF highlights the potential for AI to develop in a complementary and synergistic 
way.To address these diverse challenges and recent approaches, our survey is organized as 
illustrated in Fig. 1, which outlines the overall framework.

Figure 2 shows the number of papers on time series forecasting presented at major AI and 
machine  learning  conferences. This  explosive  increase  demonstrates  the  growing  impor-
tance of TSF research in the AI and machine learning fields. As various studies addressing 
time series forecasting problems are being actively conducted, survey papers are also being 
frequently published. Over time, numerous survey papers have systematically organized the 
vast landscape of TSF, offering in-depth research that has provided valuable guidance and 
direction for researchers. However, existing survey papers still have room for improvement,

---

<!-- PAGE 3 -->

Page 3 of 95  216

Fig. 1  Overview of this survey

---

<!-- PAGE 4 -->

216  Page 4 of 95

Fig. 2  Number of top-tier AI and ML conference papers on time series forecasting

particularly in addressing the inevitable increase in model diversity and the open challenges 
in the field, as summarized in Table 1. This survey aims to reorganize the extensive dis-
course on TSF by providing essential and comprehensive information. At the same time, it 
explores model diversity to deliver the latest TSF trends and uniquely highlights open chal-
lenges, clearly presenting them to readers.

Models for TSF have undergone various stages of development over an extended period. 
In the past, statistical methods based on moving averages were predominantly used, which 
later evolved into traditional approaches such as Exponential Smoothing and ARIMA (Box 
et al 1970). Machine learning techniques such as Tree Models (Quinlan 1986) and Support 
Vector Machines (SVM) (Cortes 1995) have also been frequently used, but they had limita-
tions in learning complex nonlinear patterns (Sect. 3.1). With the increase in available data 
and advancements in hardware computing power, various deep learning architectures such 
as MLPs (Rumelhart et al 1986), RNNs (Hopfield 1982), CNNs (LeCun et al 1998), and 
GNNs (Scarselli et al 2008) were developed, enabling the learning of more complex pat-
terns. However, the performance of these early deep learning architectures was constrained 
by their intrinsic designs. To overcome these structural limitations, variants such as Long 
Short-Term Memory (LSTM) (Hochreiter and Schmidhuber 1997) and Temporal Convolu-
tional Networks (TCN) (Bai et al 2018) have been widely utilized (Sect. 3.2). Transform-
ers (Vaswani et al 2017), known for their ability to handle long-term dependencies, have 
demonstrated excellent performance in natural language processing and have been naturally 
extended to time series data as well. While Transformers have shown good performance in 
TSF and become widely popular, recent cases have shown that simple linear models can 
outperform Transformer models (Sect. 3.3). As a result, there has been a significant increase 
in  reconsidering  fundamental  deep  learning  methodologies,  along  with  growing  interest 
in various architectures such as foundation models, diffusion models, and Mamba models 
(Sects. 4.2, 4.3, 4.4, 4.5). The Transformer model continues to improve in performance and 
still plays a significant role (Sect. 4.1). In this way, TSF has entered a renaissance of model-
ing, with various methodologies actively competing without being dominated by any single 
approach (Fig. 3). In this context, this survey offers two major strengths that set it apart from 
previous TSF survey papers.

---

<!-- PAGE 5 -->

Page 5 of 95  216

)
1
2
0
2
(

n
e
r
h
o
Z

d
n
a
m
L

i

l
a

t
e

s
i
d
i
n
e
B

)
2
2
0
2
(

l
a

t
e

d
e
m
h
A

)
2
2
0
2
(

l
a

t
e

u
i
L

)
b
1
2
0
2
(

l
a

t
e

n
e
W

)
3
2
0
2
(

l
a

t
e

n
e
h
C

)
3
2
0
2
(

l
a

t
e

i
n
i
s
a

M

l
a

t
e

n
i
L

)
a
4
2
0
2
(

)
3
2
0
2
(

)
4
2
0
2
(

n
e
h
C

d
n
a

r
e
j
i
e

M

l
a

t
e

g
n
a
i
L

)
c
4
2
0
2
(

l
a

t
e

g
n
a
h
Z

)
d
4
2
0
2
(

)
4
2
0
2
(

l
a

t
e

e
Y

n
a
r
a
w
s
e
e
n
g
A

d
n
a

o
r
t
a
P

)
a
4
2
0
2
(

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

L
D
d
n
a

,

L
M

,
l
a
c
i
t
s
i
t
a
t
s

:
s
d
o
h
t
e
m
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
u
o
i
r
a
v

f
o

n
o
i
t
a
z
i
r
o
g
e
t
a
C

n
o
i
t
a
t
u
p
m
o
c

l
e
l
l
a
r
a
p

d
n
a

,
g
n
i
l
e
d
o
m

,
g
n
i
s
s
e
c
o
r
p
e
r
p

n
i

s
e
g
n
e
l
l
a
h
C

t
r
o
p
p
u
s

n
o
i
s
i
c
e
d

r
o
f

e
c
n
e
r
e
f
n
i

l
a
s
u
a
c

d
n
a

y
t
i
l
i
b
a
t
e
r
p
r
e
t
n
I

s
l
e
d
o
m
d
i
r
b
y
h

d
n
a

s
e
r
u
t
c
u
r
t
s

r
e
d
o
c
e
d
–
r
e
d
o
c
n
E

⋅

⋅

⋅

⋅

s
t
n
e
m
e
v
o
r
p
m

i

l
a
r
u
t
c
e
t
i
h
c
r
a

d
n
a

s
n
o
i
t
a
i
r
a
v

e
r
u
t
c
u
r
t
s

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

n
o
i
t
a
z
i
m

i
t
p
o

d
n
a

,
n
o
i
t
a
c
i
l
p
p
a

,
n
o
i
t
a
t
n
e
m
e
l
p
m

i

n
o

s
e
n
i
l
e
d
i
u
G

s
l
e
d
o
m

l
a
i
t
n
e
u
q
e
s

p
e
e
d

n
o
m
m
o
C

⋅

⋅

⋅

F
S
T
L
D

f
o

s
t
n
e
n
o
p
m
o
c

y
e
K

y
t
i
l
i
b
a
c
i
l
p
p
a

l
a
c
i
t
c
a
r
P
⋅

s
d
o
h
t
e
m
n
o
i
t
a
u
l
a
v
e

e
c
n
a
m
r
o
f
r
e
p

d
n
a
m
e
t
s
y
s

n
o
i
t
a
c
fi

i
s
s
a
l
c
w
e
N

s
i
s
y
l
a
n
a

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

n
i

s
l
e
d
o
m
n
o
i
s
u
ff
D

i

r
a
e
n
i
l
n
o
n

d
n
a

r
a
e
n
i
l

o
t
n
i

d
e
z
i
r
o
g
e
t
a
C

F
S
T

l
a
i
c
n
a
n
fi

/
c
i
m
o
n
o
c
E

s
i
s
y
l
a
n
a

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

n
i

s
l
e
d
o
m
n
o
i
t
a
d
n
u
o
f

f
o

n
o
i
t
a
c
i
l
p
p
A

s
e
i
d
u
t
s

e
s
a
c

h
t
i

w
s
l
e
d
o
m
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

d
e
s
a
b
-
n
o
i
s
u
ff
D

i

s
i
s
y
l
a
n
a

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

n
i

s

M
L
L
d
n
a

s
l
e
d
o
m
n
o
i
t
a
d
n
u
o
F
o
t

s
e
h
c
a
o
r
p
p
A

e
c
n
a
m
r
o
f
r
e
p

d
n
a

s
n
o
i
t
a
c
i
l
p
p
a

c
fi
i
c
e
p
s
-
n
i
a
m
o
d

f
o

n
o
s
i
r
a
p
m
o
C

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

g
n
o
l

n
i

s
e
g
a
t
n
a
v
d
a

M
S
S
n
o

s
i
s
a
h
p
m
E

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

n
i

s

M
L
L
r
o
f

s
e
i
g
o
l
o
d
o
h
t
e
m

f
o

n
o
i
t
a
z
i
r
o
g
e
t
a
C

s
p
a
g

y
t
i
l
a
d
o
m
g
n
i
g
d
i
r
b

f
o

n
o
i
t
a
n
a
l
p
x
E

⋅

⋅

⋅

⋅

⋅

⋅

⋅

⋅

⋅

⋅

⋅

s
u
o
i
r
a
v
m
o
r
f

s
e
g
n
e
l
l
a
h
c

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

e
c
n
e
u
q
e
s

g
n
o
l

f
o

n
o
i
t
i
n
fi
e
D

s
e
v
i
t
c
e
p
s
r
e
p

⋅

⋅

:
g
n
i
n
r
a
e
l

p
e
e
d

h
t
i

w
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
-
e
m
T

i

y
e
v
r
u
s

a

a

:
a
t
a
d

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

r
o
f

s
d
o
h
t
e
m

t
s
a
c
e
r
o
F

y
e
v
r
u
s

:
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

r
o
f

g
n
i
n
r
a
e
l

p
e
e
D

y
e
v
r
u
s

e
r
u
t
a
r
e
t
i
l

d
n
a

l
a
i
r
o
t
u
t

r
o
f

s
l
e
d
o
m

l
a
i
t
n
e
u
q
e
s

p
e
e
d

n
o
w
e
i
v
e
r

A

a
t
a
d
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

y
e
v
r
u
s

a

:
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

n
i

s
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

h
t
i

w
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
-
e
m

i
t

e
c
n
e
u
q
e
s

g
n
o
L

y
e
v
r
u
s

a

:
g
n
i
n
r
a
e
l

p
e
e
d

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

r
o
f

s
e
c
n
a
v
d
a

g
n
i
n
r
a
e
l

e
n
i
h
c
a

M

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

-
a
c
i
l
p
p
a

s
e
i
r
e
s
-
e
m

i
t

r
o
f

s
l
e
d
o
m
n
o
i
s
u
ff
D

i

y
e
v
r
u
s

a

:
s
n
o
i
t

s
e
i
r
e
s
-
e
m

i
t

n
i

s
l
e
d
o
m
n
o
i
s
u
ff
i
d
f
o

e
s
i
r

e
h
T

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

:
s
i
s
y
l
a
n
a

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

r
o
f

s
l
e
d
o
m
n
o
i
t
a
d
n
u
o
F

y
e
v
r
u
s

d
n
a

l
a
i
r
o
t
u
t

a

a

:
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

r
o
f

s
l
e
d
o
m
e
g
a
u
g
n
a
l

e
g
r
a
L

y
e
v
r
u
s

s
l
e
d
o
m
n
o
i
t
a
d
n
u
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

f
o

y
e
v
r
u
s
A

s
l
e
d
o
m
e
c
a
p
s

e
t
a
t
s

f
o

y
e
v
r
u
s

:
0
6
3
-
a
b
m
a
M

s
e
c
n
e
r
e
f
e
R

-
e
R

t
n
e
c

k
r
o
w

s
e
g
n
e
l
l
a
h
c

F
S
T

-
r
a

d
a
o
r
B

e
r
u
t
c
e
t
i
h
c

w
e
i
v
e
r

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

n
o

s
r
e
p
a
p

y
e
v
r
u
s

f
o

y
r
a
m
m
u
S

1
e
l
b
a
T

s
u
c
o
F

s
e
l
c
i
t
r

A

---

<!-- PAGE 6 -->

216  Page 6 of 95

s
e
c
n
e
r
e
f
e
R

-
e
R

t
n
e
c

k
r
o
w

✓

s
e
g
n
e
l
l
a
h
c

F
S
T

-
r
a

d
a
o
r
B

e
r
u
t
c
e
t
i
h
c

w
e
i
v
e
r

s
u
c
o
F

✓

✓

g
n
i
c
u
d
o
r
t
n
i

,
s
l
e
d
o
m
F
S
T
f
o

n
o
i
t
u
l
o
v
e

e
h
t

f
o
w
e
i
v
r
e
v
o

e
v
i
s
n
e
h
e
r
p
m
o
c
A

h
t
i

w
g
n
o
l
a

,
s
k
s
a
t

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

n
i

s
e
g
n
e
l
l
a
h
c

n
e
p
o

l
a
c
i
t
i
r
c

f
o

n
o
i
s
s
u
c
s
i
D

m
e
h
t

s
s
e
r
d
d
a

o
t

s
n
o
i
t
u
l
o
s

d
e
c
n
a
v
d
a

s
e
r
u
t
c
e
t
i
h
c
r
a

e
v
i
t
a
v
o
n
n
i

⋅

⋅

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

1
e
l
b
a
T

s
e
l
c
i
t
r

A

y
e
v
r
u
s

s
i
h
T

---

<!-- PAGE 7 -->

Page 7 of 95  216

First, we focus on the inevitable diversification of architectures, providing a timely and 
comprehensive view to understand the current trend of architecture diversification. Existing 
TSF survey papers, such as (Wen et al 2023; Zhang et al 2024d; Lin et al 2024a; Meijer 
and Chen 2024; Patro and Agneeswaran 2024a), focus on providing detailed analyses of 
specific  architectures  but  have  limitations  when  it  comes  to  broadly  comparing  diversi-
fied  architectures,  including  newly  emerging  ones.  This  paper  systematically  compares 
the developmental progress of various architectures (MLPs, CNNs, RNNs, GNNs, Trans-
former, Diffusion, foundation models, Mamba) and analyzes the strengths, weaknesses, and 
contributions of each. In addition, it addresses the performance of hybrid models that com-
bine  the  strengths  of  multiple  architectures,  clearly  highlighting  key  trends  in TSF. With 
these contributions, readers can effectively understand the continuously evolving trends and 
directions of advancement in the field. Through this, it lowers the entry barrier for newcom-
ers to TSF and provides a comprehensive roadmap that opens up new research opportunities 
for established researchers.

Second,  we  explore  from  the  perspective  of  open  challenges.  Although  numerous 
advanced architectures have resolved many issues, the core challenges in TSF continue to 
persist. In particular, issues such as channel correlation, distribution shifts, causality, and 
feature extraction (Sect. 5) remain significant challenges that need to be addressed (Fig. 4). 
This  survey  explores  the  latest  methodologies  aimed  at  addressing  these  challenges  and 
provides readers with valuable insights for problem-solving. While some existing surveys 
address these TSF challenges, they often focus on only a few problems. In contrast, this 
paper takes an issue-driven approach, deeply examining seven key TSF problems and orga-
nizing new solutions.

This survey covers the fundamental concepts of time series data and the problem defini-
tion of forecasting in Sect. 2, followed by an examination of the evolution of past meth-
odologies in Sect. 3. Section 4 analyzes the key features of the latest models, and finally, 
Sect. 5, explores the open challenges in TSF and their solutions. Through this, readers will 
gain a broad understanding of the past and present of TSF research and acquire new ideas 
for future studies.

2  Background

In this section, before exploring time series forecasting models, we explain the definition 
and key characteristics of time series data to provide the necessary background. We also 
define the problem of time series forecasting tasks, discussing related datasets and evalu-
ation metrics. This establishes the basic concepts of time series forecasting and provides 
preliminary information to help understand the models discussed in the following sections.

2.1  Time-series data

Time series data is a collection of sequential data points gathered at regular time intervals, 
representing a series of observations of phenomena that change over time. This temporal 
continuity allows for the understanding and analysis of phenomena that evolve according to 
time order. Each data point represents the state or value at a specific moment, and through 
the observation of these data points, various patterns such as long-term trends, seasonality,

---

<!-- PAGE 8 -->

216  Page 8 of 95

s
l
e
d
o
m
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

f
o

n
o
i
t
u
l
o
v
E

3

.

g
i
F

---

<!-- PAGE 9 -->

Page 9 of 95  216

cyclicality, and irregularities can be recognized. These patterns provide valuable informa-
tion for predicting future values or detecting changes at critical moments. By extracting and 
studying the meaningful information provided by time series data, researchers can develop 
practical applications to address challenges in various disciplines.

Characteristics of time series data
Time series data encapsulates various characteristics that play a critical role in explaining 
the diverse patterns and fluctuations within time series. Understanding these characteristic 
elements is essential for analyzing and predicting data. The key properties are explained in 
Fig. 5.

In  time  series  data,  the  above  features  frequently  appear  in  a  mixed  form. Therefore, 
decomposition is commonly used to separate the components for detailed analysis, or dis-
tribution shift alleviation methods are widely applied. Many time series datasets provide 
information on multivariate variables. Sometimes, these data provide additional information 
that univariate data cannot, and it is important to understand this for many problems. The 
main properties are explained in Fig. 6.

These additional features convey the complexity of the real world in greater detail and 
sometimes provide reasons for significant pattern changes. Considering this information can 
lead to more precise time series analysis and forecasting.

2.2  Time-series forecasting

Time series forecasting involves analyzing historical time-series data to predict future val-
ues. This process entails analyzing inherent temporal patterns in the data, such as trends and 
seasonality, using past observations to estimate future values. The goal of time series fore-
casting is to support decision-making by providing information about an uncertain future, 
such as predicting future demand changes or fluctuations in prices. Time series forecast-
ing  can  employ  various  methodologies,  including  statistical  methods,  machine  learning, 
and deep learning. These methodologies focus on capturing the characteristics of data as it 
changes over time.
Univariate time series forecasting (UTSF)

Univariate forecasting refers to making predictions using only one variable. For exam-
ple,  predicting  the  next  day’s  temperature  based  solely  on  past  temperature  data  from  a 
weather station is a univariate forecast. The advantage of univariate forecasting is that the 
models are simple and computationally efficient. Since the data consists of a single variable, 
the model is relatively straightforward and easy to understand, making data collection and 
management easier. However, it may only utilize limited information as it cannot account 
for important external factors or interactions between different variables.

ˆxt+1:t+h = f (xt

p:t)

−

(1)

The formula representing UTSF is shown in Eq. (1). The model takes the past p + 1 time 
p  to  t,  as  input  to  make  predictions.  Here,  ˆxt+1:t+h 
steps,  specifically  the  data  from  t
represents the predicted values from t + 1 to t + h. Single-step forecasting predicts only 
one value when h = 1, while multi-step forecasting predicts multiple values when h > 1.
Multivariate Time Series Forecasting (MTSF)

−

---

<!-- PAGE 10 -->

216  Page 10 of 95

Fig. 4  Overview of latest open challenges in time series forecasting

Multivariate forecasting involves making predictions using multiple variables simultane-
ously. For instance, in weather forecasting, predicting the next day’s temperature by con-
sidering various variables such as temperature, humidity, and wind speed is an example of 
multivariate  forecasting.  By  incorporating  interactions  and  correlations  between  multiple 
variables, multivariate forecasting can capture complex relationships, offering higher pre-
dictive accuracy. However, these models tend to be more complex, require more data, and 
can be more challenging to handle, increasing the risk of overfitting.

To  incorporate  other  influencing  variables,  we  can  extend  the  model  to  a  multivariate

approach.

ˆXt+1:t+h = f (Xt

p:t)

−

(2)

The formula representing MTSF is shown in Eq. (2). Xt
p:t is a set of vectors over the 
past p + 1 time steps, where each vector contains the values of multiple variables at time t
. This model takes multiple variables from the past p + 1 time steps, specifically Xt
p:t, as 
input to generate the multivariate predicted values from t + 1 to t + h, denoted as ˆXt+1:t+h
. This multivariate approach allows for more comprehensive modeling by considering both 
the target variable’s history and the effects of other relevant factors. Figure 7 illustrates how 
a multivariate forecasting model uses a past lookback window to predict future intervals.

−

−

---

<!-- PAGE 11 -->

Page 11 of 95  216

Fig. 5  Properties of time series data

Short-term time series forecasting (STSF)

Short-term time series forecasting focuses on predictions for the near future, making it 
suitable for tasks that require quick responses, such as immediate operational planning or 
short-term decision-making. The models are simple, making them easy to train and imple-
ment, and they often demonstrate relatively high accuracy. However, because the forecast 
range  is  short,  it  cannot  capture  long-term  trends  or  complex  variations,  which  limits  its 
applicability.
Long-term time series forecasting (LTSF)

Long-term time series forecasting deals with predictions for the distant future, with fore-
cast horizons increasingly extending to several months, years, or beyond. It is valuable for 
long-term  strategy  planning,  investment  decisions,  and  policy-making,  addressing  many

---

<!-- PAGE 12 -->

216  Page 12 of 95

Fig. 6  Properties of multivariate time series data

Fig. 7  Diagram of multivariate time series forecasting

real-world problems. By identifying long-term trends and cycles, organizations can prepare 
accordingly, highlighting its significance. However, predicting the distant future is challeng-
ing, and extensive research is being conducted to improve accuracy.

2.3  Time series forecasting datasets

Models for Time Series Forecasting (TSF) are primarily trained and evaluated using open 
benchmark datasets. Open datasets offer data that has already been collected across vari-
ous fields, allowing researchers to use them without going through separate data collection 
processes. Additionally, researchers can objectively compare the performance of different 
models and convincingly demonstrate the contributions of their developed models.

Datasets frequently used by time series forecasting models in various domains, such as 
energy consumption, traffic, weather, exchange rates, and disease outbreaks, are listed in

---

<!-- PAGE 13 -->

Page 13 of 95  216

Table 2. These time series datasets are typically collected in real-time via sensors, recorded 
as  transaction  logs  in  financial  markets,  accumulated  as  server  logs,  or  gathered  through 
periodic surveys.

Time  series  data  exist  across  a  wide  range  of  domains,  each  exhibiting  unique  char-
acteristics.  This  diversity  is  due  to  the  nature  of  time  series  data,  which  addresses  real-
world problems in various fields and can display highly varied patterns depending on time 
and environmental factors. For example, stock price data often show long-term upward or 
downward  trends.  Stock  market  fluctuations  tend  to  move  in  specific  directions  over  the 
long term due to complex influences such as economic conditions, corporate performance, 
and policy changes. In contrast, electricity consumption data exhibit pronounced periodicity 
throughout the day, with higher consumption during daytime hours and lower consumption 
at night. There are also seasonal patterns, with different consumption rates during summer 
and winter.

Monash Time Series Forecasting Archive (Godahewa et al 2021l) points out that there 
is no comprehensive time series dataset archive and thus provides a thorough time series 
repository. This repository offers 30 datasets for real-world data and competition purposes, 
covering various domains such as energy, economics, nature, and sales. Details are specified 
in Table 3.

Time  series  data  exhibit  a  greater  variety  of  domain-specific  characteristics  compared 
to Natural Language Processing (NLP). These differences in dataset characteristics make 
time series forecasting problems more diverse and complex, reducing the generalizability 
of time series forecasting models. Consequently, developing foundation models for TSF is 
more challenging compared to NLP. Time series data lack the well-designed vocabulary and 
grammar found in NLP, and obtaining vast amounts of data is more difficult than in fields 
like Computer Vision (CV) or NLP. In the CV field, there are general benchmark datasets 
such as MNIST and ImageNet, while in NLP, there are datasets like GLUE (General Lan-
guage Understanding Evaluation) and SQuAD (Stanford Question Answering Dataset). In 
contrast,  the  time  series  analysis  field  lacks  large-scale  general  benchmark  datasets  and 
large-scale challenges like those in image and language domains. The most famous time 
series forecasting competition is the M-Competitions, which started in 1982 and has only 
been held six times to date. The paper “Time Series Dataset Survey for Forecasting with 
Deep Learning” (Hahn et al 2023) highlights the lack of general benchmark datasets for 
TSF and analyzes the statistical characteristics of datasets across various domains, cluster-
ing  them  to  provide  easily  accessible  information  for  researchers.  We  do  not  delve  into 
the characteristics of the datasets in detail, but instead provide a brief overview of the key 
datasets. Recently, the development of foundation models for time series has begun, leading 
to the gradual emergence of general datasets for TSF. Details about TSF foundation models 
will be discussed in Sect. 4.3.

2.4  Evaluation metrics

The evaluation metrics used in TSF play a crucial role in objectively comparing and assess-
ing model performance. Common metrics for deterministic models include Mean Absolute 
Error (MAE) and Mean Squared Error (MSE), which are easy to use because they allow 
intuitive comparisons of prediction errors. On the other hand, probabilistic models that can 
reflect uncertainty typically use Continuous Ranked Probability Score (CRPS), which mea-

---

<!-- PAGE 14 -->

216  Page 14 of 95

s
l
e
d
o
m
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

n
i

d
e
s
u

y
l
t
n
e
u
q
e
r
f

s
t
e
s
a
t
a
D

t
e
s
a
t
a
D
T
E

t
e
s
a
t
a
D
T
E

e
v
i
h
c
r
A

I

C
U

s
n
i
m
5
1

y
l
r
u
o
H

y
l
r
u
o
H

e
c
r
u
o
S

y
c
n
e
u
q
e
r
F

s
r
a
e
y

s
r
a
e
y

2

2

r
o
f

a
n
i
h
C
n
i

s
e
i
t
n
u
o
c

o
w

t

m
o
r
f

a
t
a
d

e
r
u
t
a
r
e
p
m
e
t

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
t

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

r
o
f

a
n
i
h
C
n
i

s
e
i
t
n
u
o
c

o
w

t

m
o
r
f

a
t
a
d

e
r
u
t
a
r
e
p
m
e
t

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
t

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
1
0
2

o
t

2
1
0
2
m
o
r
f

s
t
n
e
i
l
c

f
o

a
t
a
d

n
o
i
t
p
m
u
s
n
o
c

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
e

y
l
r
u
o
H

n
o
i
t
p
i
r
c
s
e
D

S
M
e
P

y
l
k
e
e
w

,
y
l
r
u
o
H

s
h
t
n
o
m
8
4

r
o
f

s
y
a
w
e
e
r
f

a
e
r
a

y
a
B
o
c
s
i
c
n
a
r
F
n
a
S
n
o

s
e
t
a
r

y
c
n
a
p
u
c
c
o

d
a
o
r

y
l
r
u
o
H

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
M

s
e
i
r
e
S
e
m
T

i

a
n
e
J
C
G
B

a
t
a
D

s
n
i
m
0
1

y
l
i
a
D

y
n
a
m
r
e
G
n
i

)
e
r
u
t
a
r
e
p
m
e
t

,
y
t
i
d
i
m
u
h

,
.
g
.
e
(

a
t
a
d

l
a
c
i
g
o
l
o
r
o
e
t
e

M

6
1
0
2

o
t

0
9
9
1
m
o
r
f

s
e
i
r
t
n
u
o
c

t
h
g
i
e

f
o

s
e
t
a
r

e
g
n
a
h
c
x
e

y
l
i
a
D

)
6
1
0
2
–
5
1
0
2
(

h
t
g
n
e
L

0
8
6
,
9
6

0
2
4
,
7
1

4
0
3
,
6
2

4
4
5
,
7
1

6
9
6
,
2
5

8
8
5
7

w
e
i
V
u
l
F
C
D
C

y
l
k
e
e

W

C
D
C

.

.

S
U
e
h
t

m
o
r
f

a
t
a
d

s
s
e
n
l
l
i

e
k
i
l
-
a
z
n
e
u
fl
n
i

y
l
k
e
e

W

6
6
9

l
e
n
n
a
h
C

1
2
3

2
6
8

7

7

1
2

8

7

2
m
T
T
E

,
1
m
T
T
E

2
h
T
T
E

,
1
h
T
T
E

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

c
ffi
a
r
T

e
g
n
a
h
c
x
E

r
e
h
t
a
e

W

I
L
I

2
e
l
b
a
T

t
e
s
a
t
a
D

---

<!-- PAGE 15 -->

Page 15 of 95  216

sures the accuracy of distribution forecasts by evaluating the difference between predicted 
and actual distributions (Matheson and Winkler 1976). However, the limitations of these 
traditional evaluation metrics have been noted, leading to the proposal of various perfor-
mance metrics (Thompson 1990).

The distinct characteristics of time series data necessitate the use of diverse metrics in 
TSF. It is essential to assess not only the magnitude of errors but also how well the model 
learns the temporal patterns and various features of time series data. Table 4 categorizes 
evaluation metrics by type and explains each metric.

Error-based metrics for deterministic models measure the difference between predicted 
and actual values. Explained variance metrics assess how well the model explains the vari-
ance of the data (Chicco et al 2021). These metrics evaluate how well the model captures key 
patterns such as seasonality or trends in the data, thereby aiding in the structural understand-
ing of the predictions. Error metrics focus on accuracy, but they do not assess overfitting, 
whereas  explained  variance  evaluates  the  model’s  generalization  ability.  Model  selection 
metrics help identify the optimal model (Portet 2020). These metrics take into account fac-
tors such as sample size and the number of parameters, playing a key role in selecting the 
optimal model. Thus, they are particularly useful for choosing the most appropriate model 
for a given dataset. For instance, in noisy environments, MAE is preferred over MSE due 
to its reduced sensitivity to outliers. Additionally, when evaluating non-stationary data, it is 
important to use metrics that effectively capture changes in trends and seasonality. In such 
cases, cumulative error-based metrics or explained variance metrics can be useful.

Probabilistic  model  evaluation  metrics,  on  the  other  hand,  account  for  uncertainty, 
enabling the assessment of both the confidence and variability of predictions. These met-
rics help evaluate not only the predicted values but also the uncertainty surrounding them. 
Beyond  basic  error-based  metrics,  several  advanced  metrics  are  used.  Interval  Metrics 
assess  the  confidence  intervals  of  the  predictions,  considering  both  the  predicted  values 
and their associated uncertainty (Khosravi et al 2011). These metrics are especially useful 
in fields such as financial market forecasting and risk management. Quantile Metrics evalu-
ate the accuracy of specific quantiles of predicted values, making them particularly useful 
when assessing how well various quantiles match the actual values in situations with high 
uncertainty (Koenker and Bassett Jr 1978). Quantile Metrics are beneficial in areas such as 
weather forecasting and insurance, where forecasts are assessed across different risk levels. 
Sharpness Metrics, which evaluate the width of predicted confidence intervals, are used to 
assess how narrow and accurate the prediction intervals are (Zhao et al 2020). This metric is 
valuable in logistics and supply chain forecasting, where minimizing the width of prediction 
intervals is crucial.

Thus, various evaluation metrics are crucial in assessing model performance, and each 
should be chosen based on the specific characteristics of the data and the requirements of 
the problem. In real-world scenarios, the appropriate use of metrics allows for the selection 
of the most effective model, which can then be leveraged for efficient decision-making. In 
contrast, in the field of deep learning research, MSE and MAE remain widely used due to 
their simplicity, intuitiveness, and the fact that they have been extensively utilized in previ-
ous studies, making them suitable for performance comparison (Chen et al 2023).

---

<!-- PAGE 16 -->

216  Page 16 of 95

)
0
0
0
2
(

n
o
b
i
H
d
n
a

s
i
k
a
d
i
r
k
a
M

)
1
1
0
2
(

l
a

t
e

s
o
l
u
o
p
o
s
a
n
a
h
t
A

)
7
1
0
2
(

a
d
r
u
B
d
n
a

a
k
č
i
n
p
ě
t
Š

)
0
2
0
2
(

l
a

t
e

s
i
k
a
d
i
r
k
a
M

)
2
8
9
1
(

l
a

t
e

s
i
k
a
d
i
r
k
a
M

)
e
1
2
0
2
(

l
a

t
e

a
w
e
h
a
d
o
G

)
9
1
0
2
(

l
e
h
c
i

M
-
n
a
e
J

)
c
1
2
0
2

,
b
1
2
0
2
(

l
a

t
e

a
w
e
h
a
d
o
G

)
g
1
2
0
2

,
f
1
2
0
2
(

l
a

t
e

a
w
e
h
a
d
o
G

)
0
2
0
2
(

e
n
r
u
o
b
l
e

M

f
o

y
t
i

C

)
5
1
0
2
(

t
h
g
i
e
y
t
r
i
h
t
e
v
fi

)
0
2
0
2
(

r
e
t
n
e
C

)
0
2
0
2
(

l
a

t
e

s
k
r
a
p
S

)
2
1
0
2
(

l
a

t
e

b
e
i
a
T

)
8
1
0
2
(

p
u
C
D
D
K

)
7
1
0
2
(

e
l
g
o
o
G

)
0
2
0
2
(

r
a
l
o
S

)
0
2
0
2
(

I

C
U

)
5
1
0
2
(
n
a
m
d
n
y
H

)
i
1
2
0
2

,
h
1
2
0
2
(

l
a

t
e

a
w
e
h
a
d
o
G

)
6
1
0
2
(

g
N
d
n
a

n
e
k
c
a
r
C
c
M

)
0
2
0
2
(

s
n
a
r
t
l
a
C

)
5
1
0
2
(
n
a
m
d
n
y
H

)
0
2
0
2
(

y
t
i
s
r
e
v
i
n
U
s
n
i
k
p
o
H
s
n
h
o
J

)
k
1
2
0
2

,
j
1
2
0
2
(

l
a

t
e

a
w
e
h
a
d
o
G

)
3
1
0
2
(
n
o
e
w
G
d
n
a

d
o
e
L
c
M

)
3
1
0
2
(

n
o
e
w
G
d
n
a

d
o
e
L
c
M

)
5
1
0
2
(

t
o
p
s
n
u
S

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

s
e
Y

s
e
Y

s
e
Y

s
e
Y

s
e
Y

s
e
Y

s
e
Y

s
e
Y

s
e
Y

s
e
Y

s
e
Y

o
N

o
N

o
N

s
e
Y

s
e
Y

s
e
Y

s
e
Y

s
e
Y

o
N

o
N

o
N

o
N

o
N

o
N

o
N

s
e
Y

o
N

s
e
Y

s
e
Y

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

o
N

0
5
1

4
4
1

3
3
9
9

3
3
3

0
2
1

2
7
2
,
2
3
2

0
4
0
,
7
2
5

8
4
6
,
9
3

1
8
5
4

3
9
3

4
2
4
,
6
9

3
4
2

0
2
9
,
0
1

1
8
9
,
5
6

0
6
5
,
2
5

4
0
3
,
6
2

1
9
7

3
0
8

8
2
7

1
5

4
4
5
,
7
1

1
4
5

4
8

2
1
2

5
2
7

1
3
9
,
3
7

1
4
7
,
3
2

5
0
3
7

5
1

0
2

9
1

1
1

4
3

6
3
7
,
0
3
2

8
8
2

5
4
3
6

9
5
6
2

8
2

6
7
5

0
7

4
0
5
9

2
3
3
1

1
9
7

3
0
8

0
6
5
,
2
5

4
0
3
,
6
2

4
4
5
,
7
1

8
2
7

1
5

1
4
5

4
8

2
1
2

5
2
7

1
3
9
,
3
7

1
4
7
,
3
2

5
0
3
7

0
0
0
,
0
0
1

1
0
0
1

3
0
0
3

1
1
3
1

2
7

0
6
5
5

9
3
3

5

4
0
7
,
5
1
1

8
1

6
6

9
2
3

0
7
2

0
1
0
3

1
1
1

3
6
0
,
5
4
1

7
3
1

1
2
3

4
7
6
2

7
0
1

2
6
8

4
0
3
2

7
6
7

6
6
2

2
7
0
,
2
3

1

1

1

e
c
r
u
o
S

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
M

n
o
i
t
i
t
e
p
m
o
C

h
t
g
n
e
L

.
x
a
M

h
t
g
n
e
L

.
n
i
M

s
e
i
r
e
S

.
o
N

n
i
a
m
o
D

e
l
p
i
t
l
u
M

e
l
p
i
t
l
u
M

e
l
p
i
t
l
u
M

m
s
i
r
u
o
T

g
n
i
k
n
a
B

y
g
r
e
n
E

y
g
r
e
n
E

y
g
r
e
n
E

s
e
l
a
S

c
i
m
o
n
o
c
E

t
r
o
p
s
n
a
r
T

t
r
o
p
s
n
a
r
T

e
r
u
t
a
N

e
r
u
t
a
N

g
n
i
k
n
a
B

y
g
r
e
n
E

y
g
r
e
n
E

s
e
l
a
S

b
e
W

c
i
m
o
n
o
c
E

t
r
o
p
s
n
a
r
T

t
r
o
p
s
n
a
r
T

h
t
l
a
e
H

e
r
u
t
a
N

e
r
u
t
a
N

e
r
u
t
a
n

e
r
u
t
a
N

e
r
u
t
a
N

d
n
a
m
e
d

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
e

.
s
u
A

s
r
e
t
e
m

t
r
a
m

s

n
o
d
n
o
L

6
1
0
2
F
I
C

m

s
i
r
u
o
T

s
t
n
u
o
c

n
a
i
r
t
s
e
d
e
P

8
1
0
2

p
u
C
D
D
K

s
p
i
r
t

e
l
c
i
h
e
V

s

m
r
a
f

d
n
i
W

k
c
i
n
i
m
o
D

n
i
o
c
t
i

B

c
ffi
a
r
T
o
c
s
i
c
n
a
r
F
n
a
S

n
i
a
r

e
r
u
t
a
r
e
p
m
e
T

s
h
t
a
e
d
D
V
O
C

I

t
o
p
s
n
u
S

w
o
fl
r
e
v
i
r

n
e
e
g
u
a
S

s
h
t
r
i
b
S
U

e
r
a
h
s
e
d
i
R

l
a
t
i
p
s
o
H

c
ffi
a
r
T
b
e
W

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

s
t
r
a
P
r
a
C

-

D
M
D
E
R
F

r
a
l
o
S

r
e
h
t
a
e

W

5
N
N

3
e
l
b
a
T

t
e
s
a
t
a
D

1
M

3
M

4
M

)
l
1
2
0
2
l
a

t
e

a
w
e
h
a
d
o
G

(

e
v
i
h
c
r
a

h
s
a
n
o
m
m
o
r
f

s
n
i
a
m
o
d

s
s
o
r
c
a

s
t
e
s
a
t
a
d
f
o

y
r
a
m
m
u
S

---

<!-- PAGE 17 -->

Page 17 of 95  216

)
a
1
2
0
2
(

l
a

t
e

a
w
e
h
a
d
o
G

)
d
1
2
0
2
(

l
a

t
e

a
w
e
h
a
d
o
G

o
N

o
N

o
N

o
N

2
2
2
,
7
9
3
,
7

7
4
1
,
7
9
3
,
7

2
2
2
,
7
9
3
,

7

7
4
1
,
7
9
3
,

7

1

1

e
c
r
u
o
S

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
M

n
o
i
t
i
t
e
p
m
o
C

h
t
g
n
e
L

.
x
a
M

h
t
g
n
e
L

.
n
i
M

s
e
i
r
e
S

.
o
N

n
i
a
m
o
D

y
g
r
e
n
E

y
g
r
e
n
E

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

3
e
l
b
a
T

r
e
w
o
p

r
a
l
o
S

r
e
w
o
p

d
n
i
W

t
e
s
a
t
a
D

---

<!-- PAGE 18 -->

t
n
e
r
e
ff
i
d

h
t
i

I

w
C
B
d
n
a
C
A
o
t

I

e
v
i
t
a
n
r
e
t
l

A

e
l
p
m
a
s

l
l
a
m

s

r
o
f

n
o
i
t
c
e
r
r
o
c

h
t
i

w
C
A

I

s
e
z
i
s

s

m
r
e
t

y
t
l
a
n
e
p

1

−

−

k

n

)
1
+
k
(
k
2
+
)
ˆL
(
n
l
2

−

k
2
=
c
C
A

I

1

−

−

k

n

)
1
+
k
(
k
2
+
C
I
A

216  Page 18 of 95

-
n
o
c

t
u
o
h
t
i

w

,
s
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

f
o
t
e
s

a

n
i

s
r
o
r
r
e

e
h
t

f
o
e
d
u
t
i
n
g
a
m
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

s
e
r
u
s
a
e

M

n
o
i
t
c
e
r
i
d

r
i
e
h
t

g
n
i
r
e
d
i
s

d
e
r
a
u
q
s

e
h
t

f
o

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

s
e
r
u
s
a
e

M

s
r
o
r
r
e

-
r
e

d
e
r
a
u
q
s

f
o

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

f
o

t
o
o
r

e
r
a
u
q
S

s
r
o
r
r
e

r
e
g
r
a
l

o
t

t
h
g
i
e
w

r
e
h
g
i
h

g
n
i
v
i
g

,
s
r
o
r

-
t
n
e
c
r
e
p

n
i

r
o
r
r
e

e
h
t

f
o

e
z
i
s

e
h
t

s
e
r
u
s
a
e

M

s
m
r
e
t

e
g
a

e
v
i
t
a
l
e
r

n
o

d
e
s
a
b

y
c
a
r
u
c
c
a

e
h
t

s
e
r
u
s
a
e

M

r
o
r
r
e

s
a
i
b

g
n
i
t
a
c
i
d
n
i

,
s
r
o
r
r
e

t
s
a
c
e
r
o
f

f
o

e
g
a
r
e
v
A

l
a
t
o
t

s
e
r
u
s
a
e
m

,
s
r
o
r
r
e

t
s
a
c
e
r
o
f

l
l
a

f
o
m
u
S

n
o
z
i
r
o
h

t
s
a
c
e
r
o
f

e
h
t

r
e
v
o
s
a
i
b

e
v
i
a
n

a

f
o
E
A
M

e
h
t

y
b

d
e
l
a
c
s
E
A
M

t
s
a
c
e
r
o
f

n
o
i
t
a
n
a
l
p
x
E

e
h
t

y
b

d
e
n
i
a
l
p
x
e

e
c
n
a
i
r
a
v

f
o

n
o
i
t
r
o
p
o
r
P

l
e
d
o
m

s
r
o
t
c
i
d
e
r
p

f
o

r
e
b
m
u
n
e
h
t

r
o
f

d
e
t
s
u
j
d
a

²

R

e
c
n
a
i
r
a
v

f
o

n
o
i
t
r
o
p
o
r
p

e
h
t

s
e
r
u
s
a
e

M

l
e
d
o
m
e
h
t

y
b

d
e
n
i
a
l
p
x
e

d
n
a

t
fi
f
o

s
s
e
n
d
o
o
g

n
e
e
w
t
e
b
ff
o
-
e
d
a
r
T

y
t
i
x
e
l
p
m
o
c

l
e
d
o
m

r
o
f

y
t
l
a
n
e
p

r
e
g
n
o
r
t
s

a

h
t
i

I

w
C
A
o
t

r
a
l
i

m
i
S

s
r
e
t
e
m
a
r
a
p

e
r
o
m
h
t
i

w
s
l
e
d
o
m

0
0
1

×
2
/
)

|

|

t
t
ˆy
(cid:30)(cid:30)
ˆy
−
+
t
y

t
y

|

|

|

|

(
(cid:30)(cid:30)

1
=
n t
(cid:31)

)
t
ˆy

)
t
ˆy

−

t
y
(

1
=
n t
∑

−

t
y
(

1
=
∑
n t

1n

1n

e
g
a
t
n
e
c
r
e
p

e
t
u
l
o
s
b
a

n
a
e
m
c
i
r
t
e
m
m
y
S

)
E
F
M

(

r
o
r
r
e

t
s
a
c
e
r
o
f

n
a
e

M

)
E
P
A
M

s
(

r
o
r
r
e

)
E
F
C

(

r
o
r
r
e

t
s
a
c
e
r
o
f

e
v
i
t
a
l
u
m
u
C

:
d
e
s
a
b
-
r
o
r
r
E

e
v
i
t
a
l
u
m
u
c

0
0
1

×

t
ˆy

t
y

t
−
y

1
∑
=
n t

√

1n

r
o
r
r
e

e
g
a
t
n
e
c
r
e
p

e
t
u
l
o
s
b
a

n
a
e

M

:
d
e
s
a
B

-
r
o
r
r
E

)
E
P
A
M

(

e
v
i
t
a
l
e
R

|

t
ˆy

−

t
y

|

1
=
n t

2
)
t
ˆy

−

t
y
(

1
=
n t

∑

1n

1n

a
l
u
m
r
o
F

2
)
t
ˆy

−

t
y
(

1
=
n t

∑

1n

)
E
S
M
R

(

r
o
r
r
e

d
e
r
a
u
q
s

n
a
e
m

t
o
o
R

)
E
S
M

(

r
o
r
r
e

d
e
r
a
u
q
s

n
a
e

M

)
E
A
M

(

r
o
r
r
e

e
t
u
l
o
s
b
a

n
a
e

M

:
d
e
s
a
b
-
r
o
r
r
E

c
i
t
s
i
n
i
m
r
e
t
e
D

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

r
o
f

s
c
i
r
t
e
m
n
o
i
t
a
u
l
a
v
E

4
e
l
b
a
T

c
i
r
t
e

M

y
r
o
g
e
t
a
C

e
p
y
t

n
o
i
t
a
u
l
a
v
E

e
t
u
l
o
s
b
a

|

1

−

t
y

−

|

t
ˆy

−

t
y

|

t
y

|

1
=
n t

2
=
n t

2

)
t
ˆy

−

t
y
(

2
)
¯y

−

t
y
(

1
=
n t

1
=
n t

∑

∑

1n

∑

1

1

−

n

)
1

n
(
)

−

1

−

k

n

2
−
R
−
∑
∑
−

1
(

−

)
t
ˆy

t
y
(
r
a
V

−

)
t
y
(
r
a
V

−

1

1

1

)
ˆL
(
n
l
2

−

)
n
(
n
l
k

)
ˆL
(
n
l
2

−

k
2

)

C
B

I

(

n
o
i
r
e
t
i
r
c

n
o
i
t
a
m
r
o
f
n
i

n
a
i
s
e
y
a
B

)

C
Q
H

(

n
o
i
r
e
t
i
r
c

n
n
i
u
Q
–
n
a
n
n
a
H

n
o
i
r
e
t
i
r
c

n
o
i
t
a
m
r
o
f
n
i

e
k
i
a
k
a

d
e
t
c
e
r
r
o
C

)
c
C
A

I

(

n
o
i
t
a
n
i
m
r
e
t
e
d

f
o

t
n
e
i
c
ffi
e
o
c

d
e
t
s
u
j
d
A

)
²

R
d
e
t
s
u
j
d
A

(

)
S
V
E
(

e
r
o
c
s

e
c
n
a
i
r
a
v

d
e
n
i
a
l
p
x
E

)
E
S
A
M

(

r
o
r
r
e

d
e
l
a
c
s

e
t
u
l
o
s
b
a

n
a
e

M

:
d
e
s
a
b
-
r
o
r
r
E

d
e
l
a
c
s

)
²

R

(

n
o
i
t
a
n
i
m
r
e
t
e
d

f
o

t
n
e
i
c
ffi
e
o
C

-
i
r
a
v

d
e
n
i
a
l
p
x
E

s
c
i
r
t
e
m
e
c
n
a

)

I

C
A

(

n
o
i
r
e
t
i
r
c

n
o
i
t
a
m
r
o
f
n
i

e
k
i
a
k
A

n
o
i
t
c
e
l
e
s

l
e
d
o
M

s
c
i
r
t
e
m

---

<!-- PAGE 19 -->

Page 19 of 95  216

s
e
m
o
c
t
u
o

l
a
u
t
c
a

d
n
a

s
e
i
t
i
l
i
b
a
b
o
r
p

d
e
t
c
i
d

-
e
r
p

n
e
e
w
t
e
b

e
c
n
e
r
e
ff
i
d

e
h
t

s
e
t
a
u
l
a
v
E

n
o
i
t
c
n
u
f

c
i
m
h
t
i
r
a
g
o
l

a

g
n
i
s
u

e
v
i
t
a
l
u
m
u
c

e
h
t

g
n
i
s
u

e
u
l
a
v

d
e
v
r
e
s
b
o

e
h
t

e
h
t

n
e
e
w
t
e
b

e
c
n
e
r
e
ff
i
d

e
h
t

s
e
t
a
u
l
a
v
E

d
n
a

n
o
i
t
u
b
i
r
t
s
i
d

y
t
i
l
i
b
a
b
o
r
p

d
e
t
c
i
d
e
r
p

n
o
i
t
c
n
u
f

n
o
i
t
u
b
i
r
t
s
i
d

-
l
a
v

d
e
v
r
e
s
b
o

f
o

n
o
i
t
r
o
p
o
r
p

e
h
t

s
e
r
u
s
a
e

M

s
l
a
v
r
e
t
n
i

d
e
t
c
i
d
e
r
p

e
h
t

n
i
h
t
i

w

l
l
a
f

t
a
h
t

s
e
u

e
h
t

g
n
i
r
u
s
a
e
m
y
b

n
o
i
s
i
c
e
r
p
s
e
t
a
u
l
a
v
E

s
l
a
v
r
e
t
n
i

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

f
o

h
t
d
i
w

s
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
-
r
e
d
n
u

d
n
a

-
r
e
v
o

s
e
z
i
l
a
n
e
P

τ

e
l
i
t
n
a
u
q

n
o

d
e
s
a
b

h
t
d
i
w
e
h
t

y
b

n
o
i
t
a
r
t
n
e
c
n
o
c

e
h
t

s
e
t
a
u
l
a
v
E

e
c
n
a
i
r
a
v

r
o

s
l
a
v
r
e
t
n
i

f
o

n
o
i
t
a
n
a
l
p
x
E

t
ˆy

t
ˆy
<
≥

t
y

t
y

f
i

f
i

)

)
t
y

−

·

−

)
t
ˆy

t
ˆy
(
−
)
τ

t
y
(

·

1
(

τ

(

1
=
n t

∑

{

)
i
ˆy
(
r
a
V
1
=
n i
∑

]
t
,
r
e
p
p
u
ˆy

,
t
,
r
e
w
o
l
ˆy

[

∈

t
y

I

1
=
n t

)

t
,
r
e
w
o
l
ˆy

−

t
,
r
e
p
p
u
(
ˆy

1
=
n t
∑

∑

∫

1n

1n

1n

1n

)

W
I
P
(

h
t
d
i
w

l
a
v
r
e
t
n
i

n
o
i
t
c
i
d
e
r
P

)
P
C
I
P
(

y
t
i
l
i
b
a
b
o
r
p

e
g
a
r
e
v
o
c

l
a
v
r
e
t
n
i

n
o
i
t
c
i
d
e
r
P

s
c
i
r
t
e
m

l
a
v
r
e
t
n
I

)
s
s
o
l

l
l
a
b
n
i

P
(

s
s
o
l

e
l
i
t
n
a
u
Q

s
c
i
r
t
e
m
e
l
i
t
n
a
u
Q

s
s
e
n
p
r
a
h
S

s
s
e
n
p
r
a
h
S

s
c
i
r
t
e
m

z
d
2
)
)
t
y

≥

z
(
1

−

)
z
(
ˆF
(

∞
∞ −

∑

e
r
o
c
s

y
t
i
l
i
b
a
b
o
r
p

d
e
k
n
a
r

s
u
o
u
n
i
t
n
o
C

)
S
P
R
C

(

)
t
p
(
g
o
l

1
=
n t

1n
−

a
l
u
m
r
o
F

)
e
r
o
c
s

g
o
L
(

e
r
o
c
s

c
i
m
h
t
i
r
a
g
o
L

d
e
s
a
b
-
r
o
r
r
E

s
c
i
r
t
e
m

c
i
t
s
i
l
i
b
a
b
o
r
P

c
i
r
t
e

M

y
r
o
g
e
t
a
C

e
p
y
t

n
o
i
t
a
u
l
a
v
E

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

4
e
l
b
a
T

---

<!-- PAGE 20 -->

216  Page 20 of 95

3  Historical TSF models

3.1  Conventional methods (before deep learning)

3.1.1  Statistical models

Prior to machine learning and deep learning, traditional statistical models, which laid the 
foundation for analyzing sequential data, were commonly utilized for time series forecast-
ing.  Exponential  smoothing  was  introduced  by  Brown  (1959),  Holt  (1957),  and  Winters 
(1960) as a method to forecast future values using a weighted average of past data. This 
method  operates  by  computing  an  exponential  weight  decay  of  historical  data,  assign-
ing  greater  weight  to  more  recent  data.  The Autoregressive  Integrated  Moving Average 
(ARIMA) model was formalized through the work of George Box and Gwilym Jenkins in 
their book “Time Series Analysis: Forecasting and Control” (Box et al 1970). The ARIMA 
model  predicts  future  values  by  leveraging  the  autocorrelation  in  data  and  is  composed 
of three main components. AutoRegressive (AR) uses a linear combination of past values 
to predict the current value. Moving Average (MA) employs a linear combination of past 
error terms to predict the current value. Integrated (I) removes non-stationarity (the property 
where mean and variance change over time) by differencing the data to achieve stationarity. 
While exponential smoothing models are advantageous for real-time data analysis due to 
their simplicity, ARIMA models are better suited for capturing complex patterns, making 
them ideal for long-term forecasting. The SARIMA model extends ARIMA by incorporat-
ing seasonal differencing, along with seasonal autoregressive and moving average compo-
nents, allowing it to effectively model and predict data with regular cyclical patterns. These 
statistical models are based on specific assumptions and are simple, intuitive, and useful for 
identifying basic patterns in data.

3.1.2  Machine learning models

While statistical methods struggle to capture complex patterns in time series data due to 
their reliance on predefined linear relationships, machine learning models excel in learn-
ing  nonlinear  patterns  directly  from  the  data  without  relying  on  such  assumptions.  To 
address  the  limitations  of  statistical  methods,  traditional  machine  learning  models  have 
been  increasingly  applied  to  time  series  forecasting.  Decision  Trees  (Quinlan  1986)  are 
machine learning models that use a tree structure for classification or prediction. The term 
“classification  and  regression  tree  (CART)  analysis”  was  first  introduced  by  Barlin  et  al 
(2013), and in time series forecasting, regression decision trees are used to split data into 
a tree structure to predict continuous values. While they are intuitive and easy to interpret, 
they are prone to overfitting. Support Vector Machines (SVM), introduced by Cortes and 
Vapnik (Cortes 1995), are supervised learning models used for classification and regression 
analysis, characterized by finding the maximum margin. They handle high-dimensional data 
and non-linearities effectively, making them robust for classification and regression tasks. 
Support Vector Regression (SVR) applies SVM concepts to regression problems, predict-
ing data points using an optimal hyperplane (Vapnik et al 1996). This hyperplane is trained 
to minimize errors between data points, ensuring errors do not exceed a certain threshold. 
Gradient Boosting Machines (GBM) were developed in 1999 with an explicit regression

---

<!-- PAGE 21 -->

Page 21 of 95  216

gradient boosting algorithm. This method uses ensemble learning to combine multiple weak 
models  into  a  single,  strong  predictive  model  (Friedman  2001).  This  method  iteratively 
improves the model, offering high predictive performance. XGBoost, an extension of the 
Gradient Boosting algorithm (Chen and Guestrin 2016), incorporates various optimization 
techniques  to  enhance  efficiency  and  performance.  It  gained  significant  attention  for  its 
outstanding performance in machine learning competitions, particularly in time series fore-
casting challenges. These machine learning models outperform traditional statistical mod-
els in capturing data structures and patterns, demonstrating high predictive power on large 
datasets (Kontopoulou et al 2023). Their ability to automatically learn and optimize various 
data features and relationships has led to their widespread use in time series forecasting.

3.2  Fundamental deep learning models

3.2.1  MLPs: The emergence and constraints of early artificial neural networks

The  development  of  the  Multi-layer  Perceptron  (MLP)  (Rumelhart  et  al  1986)  and  the 
backpropagation algorithm established the foundation for artificial neural networks. Early 
artificial neural network models utilizing these MLPs demonstrated strong performance in 
modeling nonlinear patterns, prompting numerous attempts to apply them to time series data 
processing. However, several key limitations, as outlined below, restricted the training of 
deep neural networks using MLPs.

● Limited in learning temporal dependencies: MLPs are well-suited for processing fixed-
length  input  vectors  but  struggle  to  adequately  capture  the  temporal  dependencies  in 
time series data.

● Vanishing gradient issue: The vanishing gradient problem in deep networks made train-

ing difficult.

● Lack of data and computing resources: The scarcity of large-scale datasets and high-
performance computing resources made it challenging to effectively train complex neu-
ral network models.

At that time, artificial neural network technology was still immature, and there was a lack 
of deep understanding and effective methodologies for dealing with time series data. Con-
sequently, traditional statistical methods and machine learning models previously discussed 
continued to be widely used for time series analysis.

3.2.2  RNNs: The first neural network capable of processing sequential data and 
modeling temporal dependencies

The emergence and early applications of RNNs

Recurrent  neural  networks  (RNNs)  (Hopfield  1982)  emerged,  opening  up  new  possi-
bilities for processing time series data. RNNs are specialized models designed to process 
sequential data, such as time series data, and were utilized to overcome the limitations of 
MLPs. The structure of an RNN consists of an input layer, a hidden layer, and an output 
layer, and it uses the output from previous time steps(hidden layer output) as the input for 
the current time step. This structural feature allows RNNs to naturally model the dependen-

---

<!-- PAGE 22 -->

216  Page 22 of 95

cies  in  data  over  time. The  hidden  state  preserves  past  information  by  storing  data  from 
the previous step and passing it on to the next step, thereby maintaining historical context. 
Additionally, it is parametrically efficient because the same weights are used for calcula-
tions across all time steps, regardless of the sequence length.

Due to these features, RNNs have been utilized in various fields where sequential data 
modeling is crucial, such as time series data analysis, natural language processing (NLP), 
and so on. However, early RNNs had the following issues.

● Vanishing gradient problem: When RNNs learn long sequences, the gradient gradually 
diminishes during the backpropagation process, causing information from earlier time 
steps to fail to reach later time steps. Thus, this made it difficult to learn long-term de-
pendencies.

● Exploding gradient problem: In contrast to the vanishing gradient problem, the gradient

values could become excessively large, making the training process unstable.

● Difficulty in parallel processing: Due to the sequential nature of RNNs, where the com-
putation at each time step depends  on  the previous one, parallel processing becomes 
challenging. This leads to high computational costs and slow learning speeds.

Because of these critical drawbacks, RNNs were not widely used until the early 2000s.
Overcoming the limitations of RNNs

To address the aforementioned issues with vanilla RNNs, researchers began developing 
various models. Notably, the Long Short-Term Memory (LSTM) (Hochreiter and Schmid-
huber 1997) model was developed to address the long-term dependency issues of vanilla 
RNNs. With the cell state and gate mechanisms (input, output, and forget gates), LSTMs 
preserve crucial information over extended periods and discard unnecessary information. 
The  Gated  Recurrent  Unit  (GRU)  (Cho  et  al  2014)  emerged  as  a  simpler  alternative  to 
LSTM, offering similar performance while using a more straightforward structure(update 
and reset gates) to manage information. These two models effectively addressed the vanish-
ing gradient problem and sparked a boom in RNN-based models for time series analysis. 
Many subsequent RNN-based models used these two as their backbone, making them pow-
erful tools for handling time series data until the advent of Transformers.
Notable RNN variants

The Dilated RNN (Chang et al 2017) proposed Dilated Recurrent Skip Connections as a 
solution to various issues inherent in fundamental vanilla RNNs. This approach enhanced 
parameter efficiency in long sequences and enabled the network to effectively learn complex 
dependencies across diverse temporal scales. The DA-RNN (Qin et al 2017) attempted to 
effectively address long-term dependencies, which were challenging for existing methods, 
by  employing  a  dual-stage  attention  mechanism.  Utilizing  an  encoder  with  Input Atten-
tion and a decoder with Temporal Attention, it adaptively selected salient information from 
input features and temporal steps, thereby enhancing the accuracy and performance of time 
series  predictions. Additionally,  the  MQ-RNN  (Wen  et  al  2017)  combined  the  Sequence-
to-Sequence neural network framework with Quantile Regression to provide probabilistic 
forecasts, thereby reflecting uncertainties across various scenarios. This model simultane-
ously  generated  multiple  forecast  horizons  at  each  time  step  and  employed  the  Forking-
Sequences training method to enhance the stability and performance of the RNN.

---

<!-- PAGE 23 -->

Page 23 of 95  216

3.2.3  CNNs: Extracting key patterns in time series data beyond just images

The emergence and early applications of CNNs

The  Neocognitron  (Fukushima  1980)  was  designed  for  visual  pattern  recognition  and 
served as an early form of Convolutional Neural Networks (CNNs), introducing the funda-
mental concepts of CNNs. The CNN architecture, which became more widely known with 
the development of LeNet (LeCun et al 1998), learned spatial patterns in images through a 
combination of convolutional and pooling layers. These features made CNNs well-suited 
for handling image data, leading early CNN-based models to primarily focus on image data 
without being directly applied to time series data. However, over time, their potential for 
handling time series data has also been recognized.
Attempts to apply CNNs to time series data

1D CNNs use one-dimensional convolutional filters to learn local patterns in time series 
data, allowing them to extract features that consider the temporal structure of the data. A 
prominent example is WaveNet (Van Den Oord et al 2016), which utilized 1D convolutions 
and dilated convolutions to model speech signals, effectively capturing long-term depen-
dencies in audio signals. WaveNet demonstrated the utility of CNN-based models in speech 
synthesis  and  time  series  prediction,  leading  to  the  widespread  adoption  of  CNN-based 
models for time series analysis. The development of the Temporal Convolutional Networks 
(TCNs) (Bai et al 2018) model further highlighted the potential of CNN-based models in the 
time series domain. TCN consists of multiple layers of 1D convolutional networks, using 
dilated convolutions at each layer to achieve a wide receptive field, enabling the construc-
tion of deeper networks. This allows TCNs to effectively learn from long sequences of data. 
TCNs have demonstrated excellent performance in various sequential domains, including 
time series prediction, signal processing, and natural language processing.
CNN and RNN Hybrid models

Building on the popularity of fundamental time series forecasting models like RNNs and 
the emerging interest in CNN models, hybrid CNN-RNN models began to emerge, com-
bining the strengths of both architectures. Models that combined CNNs and LSTMs were 
particularly advantageous for simultaneously learning local patterns and long-term depen-
dencies in time series data. The structure involved using CNNs to extract complex features 
from the time series data and LSTMs to learn temporal dependencies.

DCRNN (Li et al 2018) modeled traffic flow as a diffusion process on a directed graph, 
capturing  both  temporal  and  spatial  dependencies.  The  Diffusion  Convolution  leveraged 
bidirectional random walks on the graph to capture spatial dependencies within the traffic 
network,  while  the  Gated  Recurrent  Units  (GRU)  modeled  temporal  dependencies.  The 
introduction of the Diffusion Convolutional Gated Recurrent Unit (DCGRU) enabled the 
effective processing of temporal information. TPA-LSTM (Shih et al 2019) combined CNN 
and LSTM with an added attention mechanism, introducing the Temporal Pattern Attention 
(TPA)  methodology  to  learn  important  patterns  in  time  series  data.  Local  patterns  were 
extracted using CNN, while the combination of LSTM and the attention mechanism cap-
tured significant temporal patterns.

3.2.4  GNNs: Structurally modeling relationships between variables

The emergence and slow growth of GNN-based models

---

<!-- PAGE 24 -->

216  Page 24 of 95

Graph Neural Networks (GNNs) (Scarselli et al 2008) were primarily developed to pro-
cess graph-structured data because they can effectively model the complex structural rela-
tionships between nodes and edges in graph data. Over time, GNNs gradually began to be 
applied to time series data analysis, primarily because multivariate time-series data often 
encapsulates intricate structural relationships.

During  their  initial  development,  GNNs  were  less  popular  compared  to  widely  used 
RNN  or  CNN-based  models. The  prevailing  belief  was  that  GNNs  were  not  suitable  for 
time  series  analysis  compared  to  CNNs  which  are  effective  at  extracting  local  patterns, 
and  RNNs  which  are  strong  at  learning  long-term  dependencies.  However,  as  the  range 
and complexity of time-series data increased, understanding their structural characteristics 
became more important. Consequently, GNNs began to gain prominence in fields such as 
traffic prediction and social networks. Research on applying GNNs to time-series data has 
primarily focused on capturing the dynamic characteristics of graph data, and the structural 
learning  capabilities  of  GNNs  have  proven  to  be  highly  useful  in  capturing  the  complex 
patterns within time-series data.
Development and expansion of GNN applications

Until the development of Transformers, GNNs consistently garnered interest, showing 
consistent yet slow growth compared to RNNs and CNNs. The development of Graph Con-
volutional  Networks  (GCNs)  (Kipf  and  Welling  2017)  marked  another  turning  point  for 
GNNs. GCNs learn node features through convolution operations on graph structures and 
are powerful tools for processing graph data. This advancement positioned GCNs as a ver-
satile solution for addressing a wide range of graph-based challenges.

GCNs were more effective at learning the relationships between variables in time series 
and temporal locality, and subsequently, GNNs began to be widely used for time-series data. 
Spatial-Temporal Graph Convolutional Networks (ST-GCN) (Yan et al 2018) were devel-
oped as a model combining GCNs and RNNs to learn complex patterns in spatio-temporal 
data. By leveraging GCNs to learn spatial patterns and RNNs to capture temporal patterns 
effectively, ST-GCN demonstrated the potential of GNNs in time-series problems, such as 
traffic  prediction.  Graph  Attention  Networks  (GATs)  (Veličković  et  al  2018)  were  intro-
duced, learning relationships between nodes using an attention mechanism. This allowed 
GATs to capture the importance of nodes, making them advantageous for identifying sig-
nificant events in time-series data. Dynamic graph neural networks (DyGNNs) (Ma et al 
2020) were developed to learn graph structures that change over time. Designed to reflect 
the  dynamic  characteristics  of  time-series  data,  DyGNNs  could  effectively  capture  com-
plex temporal dependencies and structural relationships by allowing the graph structure to 
evolve over time. Temporal Graph Networks (TGNs) (Rossi et al 2020) were introduced as 
a model in which the nodes of a graph change over time, enabling the learning of temporal 
patterns in time-series data. By using a memory module to track the temporal state changes 
of nodes, TGNs learn the information of neighboring nodes whose importance varies over 
time, thus providing a basis for predicting future states.

After the era of traditional statistical techniques and machine learning methodologies, 
fundamental deep learning approaches such as RNNs, CNNs, and GNNs were widely used 
for time-series analysis and prediction over a long period. However, the advent of Trans-
formers brought a revolutionary change to the AI field. Upon their introduction, Transform-
ers  outperformed  all  existing  methods  across  various  domains  and  continue  to  dominate 
as the leading foundation model. In the time-series domain, a similar trend was observed.

---

<!-- PAGE 25 -->

Page 25 of 95  216

Beginning with the introduction of the Logsparse Transformer (Li et al 2019), numerous 
transformer-based models emerged, achieving state-of-the-art performance. As a result, fun-
damental deep learning methods experienced a period akin to the Ice Age. The remarkable 
historical TSF models mentioned above are organized chronologically in Fig. 8.

3.3  The prominence of transformer-based models

Transformer  (Vaswani  et  al  2017),  is  an  innovative  model  designed  to  perform  com-
plex  sequence-to-sequence  tasks  in  natural  language  processing.  This  model  features  an 
encoder–decoder structure and utilizes a self-attention mechanism to capture the relation-
ships between tokens in the input sequence.

Modeling  approaches  in  self-attention  can  be  broadly  categorized  into  unidirectional 
and  bidirectional  paradigms.  Unidirectional  modeling  restricts  the  self-attention  mecha-
nism  to  consider  only  the  tokens  preceding  the  current  token  in  the  sequence.  For  a 
sequence  (x1, x2, . . . , xL),  the  attention  for  token  xt  is  computed  over  the  subsequence 
(x1, x2, . . . , xt) to ensure causality, where L denotes the length of the input sequence. The 
unidirectional modeling is predominantly employed in tasks requiring sequential genera-
tion,  such  as  language  generation  (Brown  et  al  2020;  Dai  et  al  2019).  In  contrast,  bidi-
rectional modeling allows the self-attention mechanism to utilize the entire sequence. For 
token xt, attention is computed over (x1, x2, . . . , xL), thereby leveraging both preceding 
and succeeding tokens. The bidirectional modeling is employed in tasks requiring holistic 
context, such as masked token prediction (Devlin et al 2019; Clark et al 2020).

As  a  result,  Transformers  have  gained  significant  attention  for  replacing  fundamental 
RNN-based  models,  offering  parallel  processing  capabilities,  and  effectively  addressing 
long-term dependency issues. Transformers’ success with sequential data naturally led to 
their extension into time series applications. The attention mechanism plays a significant 
role  in TSF  by  considering  the  relationships  across  all  time  steps  simultaneously,  giving 
more weight to important moments, and effectively learning the trends and patterns in the 
data.

This  section  explores  various  Transformer  variants  that  address  the  limitations  of  the 
original  Transformer  for  time  series  forecasting  tasks.  It  discusses  the  background  of 
these variants, how they improve upon the original Transformer, and the reasons for their

Fig. 8  Remarkable historical TSF models

---

<!-- PAGE 26 -->

216  Page 26 of 95

enhanced  performance  in  time  series  prediction. Additionally,  it  addresses  the  remaining 
limitations of these variant models.

3.3.1  Transformer variants

In recent years, substantial research has focused on transformer-based time series analysis, 
particularly  long-term  time  series  forecasting  (LTSF),  which  has  led  to  the  development 
of various models (Zeng et al 2023). The original Transformer model has several limita-
tions  when  applied  to  long-term  time  series  forecasting  (TSF). These  limitations  include 
quadratic time and memory complexity, as well as error accumulation caused by the auto-
regressive decoder design. Specifically, the time and memory complexity of self-attention 
increases quadratically with the length of the input sequence, denoted as O(L2), where L 
represents the length of the input sequence.

This high complexity can become a computational bottleneck, especially for time series 
forecasting  tasks  that  rely  on  long-term  historical  information.  To  address  these  issues, 
Transformer  variants  primarily  focus  on  reducing  time  and  memory  complexity.  BAn 
attention pattern determines which tokens a token attends to. Figure 9 compares Full Self-
Attention and Sparse Self-Attention patterns to illustrate the efficiency of Sparse Attention 
(Beltagy et al 2020). In Fig. 9a, all tokens attend to each other, sharing global information. 
In contrast, Fig. 9b shows that only a subset of tokens is attended to, reducing computational 
cost while preserving essential information.

LogTrans (Li et al 2019) leverages the efficiency of Log Sparse attention mechanisms to 
reduce time and memory complexity to O(LlogL), making it well-suited for long sequence 
forecasting tasks. This model assumes recent data is more relevant than older data, utilizing 
positional sparsity to focus attention only on relevant data. Reformer (Kitaev et al 2020) 
enhances efficiency through locality-sensitive hashing and reversible residual layers, reduc-
ing memory and computational requirements to O(LlogL) while maintaining performance 
on  long  sequences.  Locality-sensitive  hashing  (LSH)  approximates  attention  by  cluster-
ing similar items and performing attention partially on these clusters. Informer (Zhou et al 
2021)  improves  computational  and  memory  efficiency  to  O(LlogL)  by  utilizing  a  Prob-
Sparse self-attention mechanism and a generative-style decoder. It effectively handles long 
sequences  and  captures  dependencies  across  various  time  scales.  Informer  addresses  the

Fig. 9  BComparison of full and sparse self-attention patterns

---

<!-- PAGE 27 -->

Page 27 of 95  216

limitations of Reformer, which performs well only on extremely long sequences, and Log-
Trans,  which  uses  heuristic  positional-based  attention.  ProbSparse  self-attention  features 
dynamic query selection based on query sparsity measurement. Autoformer (Wu et al 2021) 
integrates  time  series  decomposition  into  the  internal  blocks  of  the Transformer  and  uti-
lizes an auto-correlation mechanism to aggregate similar sub-series. Autoformer improves 
upon  previous  methods  by  addressing  point-wise  dependency  and  aggregation  issues.  It 
employs a decomposition architecture to handle complex temporal patterns by separating 
seasonal and trend components. Pyraformer (Liu et al 2021a) introduces a novel pyramid 
attention mechanism designed to efficiently model long-term dependencies in time series 
data. By using a hierarchical structure to progressively reduce sequence length, Pyraformer 
significantly lowers computational complexity compared to fundamental Transformer mod-
els. Fedformer (Zhou et al 2022) combines Fourier-enhanced decomposition blocks with 
frequency  domain  sparse  representations,  integrating  seasonal-trend  decomposition  from 
Autoformer  and  offering  a  more  effective  representation  of  time  series  data.  The  sparse 
representation basis can be Fourier-based or Wavelet-based, encompassing a subset of fre-
quency components, including both high and low frequencies. Additionally, attempts have 
been made to overcome the limitations of normalized Transformers, which often produce 
indistinguishable attention patterns and fail to capture significant temporal dependencies. 
Non-stationary Transformer (Liu et al 2022) identifies this issue as excessive normalization 
and addresses it with De-stationary Attention, which allows for the use of non-normalized 
data during QKV computations.

3.3.2  Limitation of transformer-based models

However,  even  the  models  designed  specifically  for  time  series  forecasting  based  on  the 
original Transformer still have the following limitations.
Efficiency challenges

Efforts  to  overcome  the  primary  drawback  of  quadratic  scaling  in  computational  and 
memory  complexity  with  window  length  have  not  fully  resolved  the  issues.  Various 
approaches  to  reduce  this  complexity  have  been  proposed,  but  the  attention  mechanism 
inherently incurs higher computational and memory costs compared to MLP-based or con-
volutional models with O(L) complexity. Applying Transformers to the time domain does 
not easily mitigate this problem. Models such as Fedformer (Zhou et al 2022), which uses 
Fourier  or Wavelet  transformations  to  operate  in  the  frequency  domain,  have  been  made 
to  address  these  issues. Although  research  into  more  efficient  attention  variants  is  ongo-
ing  (Tay  et  al  2020),  these  solutions  often  sacrifice  some  of  the  effective  characteristics 
of Transformers. Sparse attention mechanisms, used to reduce Self-Attention complexity, 
may result in the omission of important information. Models like LogTrans and Pyraformer 
introduce explicit sparsity biases in the attention mechanism but may suffer from significant 
performance degradation due to the loss of crucial information. None of these variants have 
yet been proven effective across diverse domains (Gu and Dao 2024).
Context window limited to current input

In principle, Transformers can handle inputs of arbitrary length, provided there are suf-
ficient computational resources. However, transformers must process the entire context at 
once in a single input, causing the memory and computation requirements to grow substan-
tially with longer context length. By contrast, RNNs and State Space Models (SSMs) main-

---

<!-- PAGE 28 -->

216  Page 28 of 95

tain hidden states over time, allowing them to preserve context beyond the immediate input. 
We highlight this practical limitation, which often arises when handling very long contexts.

Ineffectiveness of expanding input window length
Another significant issue is the minimal or no performance improvement observed when 
increasing the input window length. Strong time series forecasting (TSF) models are gener-
ally expected to achieve better results with larger look-back window sizes due to their robust 
temporal relationship extraction capabilities. However, research (Zeng et al 2023; Zhou et al 
2021; Wen et al 2023) indicates that the performance of Transformers either deteriorates or 
remains stable as the look-back window increases, in contrast to improvements seen with 
linear-based methods (Zeng et al 2023). This suggests that transformer-based models tend to 
overfit noise rather than extract long-term temporal information when provided with longer 
sequences.

In conclusion, while transformer-based models have made significant advancements in 
time series forecasting, they still face limitations. Therefore, future research will continue to 
address these limitations and will also serve as a catalyst for re-exploring various alternative 
architectures.

3.4  Uprising of non-transformer-based models

As previously discussed, transformer-based models demonstrate strong performance in pro-
cessing time series data. However, they have several limitations when dealing with long-
term time series data.

● The  point-wise  operations  of  the  self-attention  mechanism  have  quadratic  time  com-
plexity. Therefore, as sequence length increases, the computational load grows expo-
nentially, making it challenging to handle long-term historical information.

● Because storing the relationship information for all input token pairs requires substan-
tial memory usage, applying Transformers in environments with limited GPU memory 
becomes challenging.

● When  the  length  of  the  look-back  window  exceeds  the  structural  capacity,  learning

long-term dependencies becomes challenging.

● Due to the high complexity of the model, large-scale and high-quality datasets are re-
quired. In the absence of sufficient data, overfitting can occur leading to a drop in model 
performance.

Contemporary TSF  tasks  increasingly  require  the  prediction  of  diverse  multivariates  and 
long  sequences.  Unlike  earlier  tasks  that  involved  relatively  short  sequences,  the  limita-
tions of transformer-based models have become more pronounced when dealing with long 
sequences.  Researchers  adhering  to  the  Transformer’s  philosophy  have  begun  focusing 
intensively on two aspects to address these issues: reducing computational complexity and 
enhancing long-term dependency learning. Conversely, some researchers have reverted to 
non-transformer  methodologies,  renewing  interest  in  fundamental  deep  learning  models

---

<!-- PAGE 29 -->

Page 29 of 95  216

such as RNNs, CNNs, GNNs, and MLPs. Non-transformer-based models have the poten-
tial to overcome the limitations of Transformers, and research has begun to leverage these 
strengths to move beyond the hegemony of the Transformer backbone.

RNN-based models sequentially process input data, retaining the previous state at each 
time step to predict the next state. This enables the natural modeling of long-term depen-
dencies  and  helps  overcome  the  limitations  of Transformers  by  leveraging  time-ordering 
learning. They require relatively less data and memory, making them less restrictive in their 
application. Additionally, their ability to handle real-time streaming data enhances their ver-
satility across various applications.

Convolution operations in CNN-based models offer lower time complexity and reduced 
memory  requirements  compared  to  the  self-attention  mechanism  in  Transformers.  Since 
time series data often exhibit periodic trends and seasonality, the ability of convolution to 
extract local patterns complements Transformers’ specialization in learning global patterns, 
addressing their shortcomings.

GNN-based  models  can  effectively  represent  and  learn  the  complex  relationships  and 
structures of time series data through nodes and edges. They integrate localities efficiently 
through  local  operations,  resulting  in  lower  memory  usage. Additionally,  their  ability  to 
model both spatial and temporal relationships simultaneously makes them advantageous for 
handling multivariate datasets.

The primary advantage of MLP-based models lies in their simple structure, which facili-
tates  efficient  training,  fast  inference,  and  straightforward  handling.  Current  AI  models 
require  lightweight  designs  suitable  for  mobile  applications,  and  MLP-based  models  are 
well-suited for environments with many constraints.

Especially, the counterattack of simple linear models based on MLPs is one of the nota-
ble trend shifts. The emergence of LTSF-Linear (Zeng et al 2023) models which surpass 
transformer-based models using only simple linear layers has triggered this change. One 
of the key characteristics of time series data is that the time ordering of data points holds 
important  meaning.  Conversely,  the  permutation-invariant  nature  of  the  Transformer’s 
attention mechanism, which emphasizes relationships between data points, is argued to be 
inherently unsuitable for time series data. Although positional embedding attempts to pre-
serve time order, the multi-head attention process inevitably leads to information loss (Zhou 
et al 2021).

LTSF-Linear models highlighted the critical limitations of Transformers in handling long 
sequences,  demonstrating  that  simple  linear  models  could  better  preserve  time-ordering 
information and extract features related to trends and seasonality.

This claim gained further traction through subsequent studies, leading to a more diversi-
fied interest in backbone models across various architectures. The emergence of this model 
sparked skepticism regarding the performance of Transformer-based models and served as 
a catalyst for the exploration of various alternative architectures. The era of Transformer 
prevalence has come to an end, ushering in a renaissance in time series research, character-
ized by a reevaluation of fundamental DNNs, the emergence of novel models like Mamba, 
and new approaches such as the utilization of LMMs.

---

<!-- PAGE 30 -->

216  Page 30 of 95

4  New exploration of TSF models

4.1  Overcoming limitations of transformer

As  previously  mentioned  in  3.4,  the  performance  of  simple  linear  models  in  LTSF-Lin-
ear (Zeng et al 2023) surpassing fundamental transformer-based models has raised doubts 
about the effectiveness of Transformers. However, in the field of NLP, Transformers still 
demonstrate superior performance in handling long-term dependencies in sequential data 
compared to other models (Patwardhan et al 2023). This observation suggests that while 
Transformers have great potential, researchers have not fully leveraged their capabilities in 
time series analysis.

Therefore,  various  methods  have  emerged  in  time  series  forecasting  to  overcome  the 
limitations of existing Transformer-based models. This section categorizes and explains in 
detail the specific limitations of existing models and how these limitations are addressed. 
The structure begins with an introduction to the patching technique, followed by the use of 
cross-dimension and exogenous variables, and then provides a detailed explanation of other 
approaches, concluding with a summary of key points in Table 5.

4.1.1  Patching technique

Transformers were originally developed for natural language processing (NLP), and apply-
ing them to time-series analysis requires appropriate adjustments to fit the domain of time 
series. Different from the rich semantic information carried by individual word tokens in 
NLP, individual data points in time series are often similar to their neighboring values, lack-
ing substantial information (Nie et al 2023). Therefore, the point-wise attention mechanism 
of fundamental models fails to consider the broader context or patterns that may span mul-
tiple consecutive time steps and only calculates attention for individual time steps, which 
makes it difficult to capture the characteristics of time series data. For this reason, consider-
ing the surrounding context along with a single time point provides more information in 
time series data.

Patching  refers  to  the  technique  of  dividing  input  sequences  into  multiple  patches,  as 
illustrated  in  Fig.  10.  This  method  preserves  the  information  within  each  patch,  thereby 
enhancing locality. By processing patches instead of individual points, the model processes 
fewer tokens, thereby reducing the computational complexity of the attention mechanism. 
This approach helps overcome the issue of prediction performance degradation, which can 
occur when sparse attention is used to make self-attention more efficient, potentially miss-
ing critical information.

×

PatchTST (Nie et al 2023), inspired by Vision Transformer’s (Dosovitskiy et al 2021) 
division of images into 16
16 patches for capturing local semantic information, divides 
time series into 64 patches. This approach allows for utilizing a longer look-back window 
by  grouping  data  into  patches.  By  processing  time-series  data  in  patch  units,  PatchTST 
maximizes  the  advantages  of Transformer  models  for  time-series  applications,  achieving 
better  performance  than  LTSF-Linear.  PatchTST  employs  only  the Transformer  encoder, 
flattens the encoder output, and uses a linear layer for the final predictions. Additionally, 
the  study  shows  that  channel  independence  (CI)  yields  better  performance,  highlighting 
the limitations in learning channel correlations despite the intuitive consideration of chan-

---

<!-- PAGE 31 -->

Table 5  Taxonomy and methodologies of transformer models for time series forecasting
Main improvement

Main methodology

Model name

Channel 
correlation

Patching technique

PatchTST

MTST

PETformer

Cross-dimension

Crossformer

DSformer

CARD

iTransformer

VCformer

GridTST

UniTST
DeformTime
TimeXer

TGTSF

Exogenous variable

Generalization

SAMformer

Minusformer

Multi-scale

Scaleformer

CI

CI

CI

CD

CD

CD

CD

⋅ Patching
⋅ Channel independence
⋅ Multiple patch-based 
tokenizations
⋅ Placeholder-enhanced 
technique
⋅ Dual attention: cross-time and 
Cross-dimension
⋅ Dual sampling and Dual 
attention
⋅ Dual attention
⋅ Token blend module for 
multi-scale
⋅ Attention on inverted 
dimension
⋅ Variable correlation attention 
considering time lag
⋅ Koopman temporal detector 
for non-stationarity
⋅ Dual attention with original 
transformer
⋅ Unified attention by flattening CD
CD
⋅ Deformable attention blocks
CD
⋅ Integration of endogenous 
and exogenous information
⋅ Exogenous variable with 
description, news
⋅ SAM (sharpness-aware 
minimization)
⋅ Dual-stream and subtraction 
mechanism
⋅ Multi-scale framework

CD

CD

CD

CD

CD

Any

Pathformer

⋅ Adaptive multi-scale blocks

Decoder-only

CATS

Feature enhancement

Fredformer
BasisFormer

⋅ Cross-attention-only 
transformer
⋅ Frequency debias
⋅ Automatic learning of a self-
adjusting basis

CD

CI

CD
CD

Page 31 of 95  216

Enc/
Dec 
usage
Enc

Pub-
lica-
tion
2023

Enc

2024

Enc

2022

Enc and 
Dec
Enc

2023

2023

Enc

2024

Enc

2024

Enc

2024

Enc

2024

Enc
Enc
Enc

2024
2024
2024

Enc and 
Dec
Enc

2024

2024

Enc

2024

Enc and 
Dec
Enc and 
Dec
Dec

2023

2024

2024

Enc
Dec

2024
2023

nel dependencies (CD) in multivariate scenarios. MTST (Zhang et al 2024e) addresses the 
limitation  of  PatchTST  in  learning  patterns  across  different  scales  present  in  time-series 
data. By adopting a multi-scale approach, MTST proposes an effective model utilizing both 
shorter and longer patches for locality and long-term trend analysis. PETformer (Lin et al 
2024c) critiques the flattening of Transformer encoder output in PatchTST, which results in 
a  significant  increase  in  parameters.  PETformer  introduces  a  placeholder-enhanced  tech-
nique, modeling past and future data on the same time scale, thereby reducing the number

---

<!-- PAGE 32 -->

216  Page 32 of 95

Fig. 10  Patching technique in self-attention for time series forecasting

of parameters by over 95% compared to PatchTST. This reduction enhances generalization 
performance while using less memory and computational resources. The model also lever-
ages rich context information by allowing direct interaction between past and future data, 
maintaining the continuity of time-series data.

By applying the patching technique, it was possible to refute the notion that traditional 
linear models are superior to Transformers. This led to the patching technique becoming a 
widely adopted approach.

4.1.2  Cross-dimension

In multivariate time-series forecasting, understanding the relationships between variables is 
crucial for improving prediction accuracy. Intuitively, higher temperatures lead to increased 
ice cream sales, indicating a relationship between variables. Despite this apparent correla-
tion,  surprising  results  have  shown  that  models  treating  channels  independently,  such  as 
LTSF-Linear, PatchTST, and PETformer, often outperform those considering inter-channel 
correlations. This result implies that current models fail to effectively capture the relation-
ships  between  variables.  Time  series  analysis  differs  significantly  from  natural  language 
processing (NLP) and computer vision (CV) in terms of channel correlation. In NLP, there 
is no clear concept of channels. In CV, although channels exist, their relationships are tightly 
intertwined and well-defined, as seen in the RGB representation of images.

Conversely, in time series analysis, channel relationships can be either independent or 
interdependent  and  often  hidden,  adding  complexity  to  the  task.  Therefore,  time  series 
analysis  requires  models  capable  of  capturing  these  intricate  correlations.  While  earlier 
Transformer-based  models  primarily  focused  on  temporal  attention,  recent  models  have 
increasingly focused on explicitly modeling the correlations between variables.

Figure 11 illustrates the explicit modeling of relationships between variables using the

attention mechanism.

---

<!-- PAGE 33 -->

Page 33 of 95  216

Fig. 11  Cross-dimensional self-attention for modeling variable relationships

The  overall  progression  of  advancements  is  as  follows.  It  begins  with  modeling  that 
explicitly accounts for correlations between variables. This progresses to directly model-
ing the relationships between both temporal and variable aspects. Additionally, the model 
incorporates the possibility of time lags in the relationships between variables, allowing it 
to flexibly learn dependencies.

Crossformer  (Zhang  and  Yan  2023)  breaks  away  from  solely  temporal  attention  by 
employing a Two-Stage Attention mechanism that sequentially processes Cross-Time and 
Cross-Dimension stages. It divides each dimension’s time series into patches, embeds them 
into 2D vectors, and performs attention. Crossformer incorporates a router mechanism in 
the Cross-Dimension stage to handle the increased complexity of dual attention. This hier-
archical structure across multiple scales enables Crossformer to effectively model both tem-
poral dependencies and inter-dimensional correlations, significantly enhancing multivariate 
time series forecasting performance. DSformer (Yu et al 2023) criticizes Crossformer for 
emphasizing global interactions between variables in time series data, while overlooking 
the importance of local information, such as short-term variations and patterns. DSformer 
addresses this by using double sampling, obtaining global information via downsampling 
and local information through piecewise sampling. These samples undergo parallel tempo-
ral variable attention, allowing the model to integrate global, local, and inter-variable cor-
relations in multivariate time series data through dual sampling and time-variable attention 
mechanisms. CARD (Wang et al 2024b) points out the structural complexity and high com-
putational cost of Crossformer’s hierarchical attention mechanism. Simplifying the struc-
ture, CARD employs only the encoder and uses a lightweight token blend module instead 
of explicitly generating token hierarchies. This module merges adjacent tokens to represent 
larger ranges, efficiently leveraging multi-scale information and enhancing prediction accu-
racy. A robust loss function is introduced to prevent overfitting, adjusting weights to favor 
near-future data over far-future data, which shows less temporal correlation. iTransformer 
(Liu  et  al  2024c)  innovatively  reverses  the  time  and  variable  dimensions  in  the  standard 
Transformer model, learning inter-variable correlations. By embedding each variable into

---

<!-- PAGE 34 -->

216  Page 34 of 95

variate tokens via a Transformer encoder and performing temporal predictions through a 
feed-forward network, iTransformer surprisingly outperforms Crossformer, highlighting the 
limitations of merely adding explicit channel attention. Its advantage lies in not needing to 
alter the original Transformer structure. VCformer (Yang et al 2024b) addresses the issue 
of  neglecting  time  lags  in  variable  correlations.  Its  variable  correlation  attention  module 
calculates cross-correlation scores between queries and keys across various lags using FFT 
(Fast Fourier Transform), efficiently exploring and adaptively integrating correlations for 
each lag. GridTST (Cheng et al 2024c) transforms time series data into a grid format, apply-
ing horizontal and vertical attention mechanisms to model time and variable correlations 
effectively. Like PatchTST and iTransformer, GridTST leverages the original Transformer, 
distinguishing itself from the more complex Crossformer. It experiments with three con-
figurations: time-first, channel-first, and cross-application, finding that prioritizing channel 
attention yields the best performance, aligning with human intuitive analysis of inter-vari-
able relationships. UniTST (Liu et al 2024b) critiques the inability of cross-time and cross-
dimension  attention  methods  to  directly  and  explicitly  learn  complex  inter-variable  and 
intra-variable dependencies. It proposes a unified attention mechanism by flattening patch 
tokens.  To  mitigate  the  increased  computational  cost,  UniTST  incorporates  a  dispatcher 
module  to  reduce  memory  complexity  and  enhance  model  feasibility.  DeformTime  (Shu 
and Lampos 2024) introduces deformable attention, dynamically adjusting to recognize and 
adapt to important data features instead of fixed attention areas. Parallel deformable atten-
tion  mechanisms  within  the  Transformer  encoder  capture  correlations  between  variables 
and time, adaptively extracting critical information across various time intervals and vari-
able combinations, significantly improving prediction accuracy and generalizability.

4.1.3  Exogenous variable

Most  existing  research  primarily  utilizes  endogenous  variables  for  prediction.  However, 
in real-world scenarios, relying solely on endogenous variables can be insufficient due to 
the complexity of various influencing factors. For instance, stock price predictions are sig-
nificantly affected by external factors such as economic indicators, political changes, and 
technological advancements. Ignoring these external factors and relying only on past data of 
endogenous variables can lead to failures in accurately predicting market volatility. There-
fore,  incorporating  exogenous  variables  as  supplementary  information  has  emerged  as  a 
method to improve prediction performance.

TimeXer (Wang et al 2024c) proposes a method to integrate exogenous variables into the 
canonical Transformer model without structural changes. It operates by dividing the time 
series  data  of  endogenous  variables  into  patches,  learning  the  temporal  dependencies  of 
each patch through self-attention. Then, it generates variate tokens summarizing the entire 
series of endogenous and exogenous variables and learns their interactions using a cross-
attention mechanism. Through this process, TimeXer simultaneously considers the temporal 
patterns of endogenous variables and the impact of exogenous variables, enabling more pre-
cise and in-depth time-series predictions. However, TimeXer requires manual identification 
and input of appropriate exogenous variables. If unsuitable data is provided, it can hinder 
the model’s predictive accuracy. TGTSF (Xu et al 2024b) integrates text data from channel 
descriptions and news messages to enhance prediction accuracy. It embeds channel descrip-
tions and news messages using a pre-trained text model, transforming them into a sequence

---

<!-- PAGE 35 -->

Page 35 of 95  216

of vectors over time. The cross-attention layer then calculates the relevance of the text to 
each channel. By incorporating text data into the time series prediction model, TGTSF not 
only improves prediction accuracy but also allows for direct comparison of the impact of 
textual information on predictive performance.

4.1.4  Additional approaches

Beyond  the  topics  discussed  above,  there  are  various  other  approaches  to  time  series 
forecasting.
Generalization

Research  has  been  conducted  to  improve  model  generalization,  avoid  overfitting,  and 
achieve  consistent  performance  across  diverse  datasets.  SAMformer  (Ilbert  et  al  2024) 
addresses the issue of self-attention mechanisms converging to sharp local minima, causing 
entropy collapse during training, and demonstrates that applying SAM (Sharpness-Aware 
Minimization)  can  significantly  enhance  performance.  Minusformer  (Liang  et  al  2024b) 
highlights the redundancy and overfitting caused by a large number of parameters in Trans-
formers. To combat this, it employs a boosting ensemble method, where each subsequent 
model predicts the residuals of the previous model’s outputs, thus reducing redundancy and 
improving generalization.
Multi-scale

The multi-scale approach extracts more information from time series data across vari-
ous scales, offering distinct advantages. Scaleformer (Shabani et al 2023) proposes a gen-
eral framework by stacking existing models across different scales, resulting in improved 
performance. Pathformer (Chen et al 2024b), on the other hand, allows the model to learn 
adaptive scales independently, rather than relying on fixed scales.
Decoder-only

Large-scale language models (LLMs) like LLaMA3 (Dubey et al 2024) have been suc-
cessfully implemented using only a decoder without the need for an encoder. The decoder-
only  architecture  is  simpler  and  involves  less  complex  computations,  resulting  in  faster 
training  and  inference. Additionally,  the  decoder-only  structure  helps  avoid  the  temporal 
information loss often associated with the self-attention mechanism in encoders. This has 
led to a research proposal aimed at improving performance in time series forecasting using 
a decoder-only structure. CATS (Kim et al 2024) addresses the high time and memory com-
plexity of self-attention in Transformer encoders and the loss of temporal order informa-
tion. It proposes a structure using only cross-attention, focusing solely on the relationship 
between  future  and  past  data  with  a  decoder-only  architecture,  which  reduces  parameter 
count and enhances efficiency. In contrast to the encoder-only structure of most models dis-
cussed CATS demonstrates the effectiveness of using only the decoder in achieving superior 
performance.
Feature enhancement

Fredformer (Piao et al 2024) identifies the issue of frequency bias in time series data, 
where  learning  tends  to  focus  disproportionately  on  either  low  or  high  frequencies.  It 
addresses this by normalizing the frequencies to eliminate bias. Basisformer (Ni et al 2024) 
proposes a method to construct flexible relationships with each time series by leveraging 
biases learned through contrastive learning.

---

<!-- PAGE 36 -->

216  Page 36 of 95

4.2  Growth of fundamental deep learning models

Since  the  advent  of  simple  linear  models,  there  has  been  a  surge  in  research  focused  on 
non-transformer-based models. Attention has shifted to various architectures such as MLP, 
RNN, CNN, and GNN, with many models surpassing Transformers and achieving remark-
able performance improvements. Although transformer-based models exhibit excellent per-
formance across numerous fields, they have structural limitations in learning temporal order 
information, which is crucial for time series problems. While past tasks were simple and 
general enough to overlook these limitations, current real-world tasks involve many con-
straints and data-specific issues with diverse variables, necessitating approaches from vari-
ous perspectives. Each architecture has its own strengths, and these characteristics provide 
valuable solutions for addressing diverse contemporary time series forecasting challenges. 
In this section, we will investigate the latest major models for each architecture and analyze 
their  technical features. The  key  characteristics of  each  backbone  architecture have  been 
briefly summarized in comparison to Transformers in Table 6.

4.2.1  MLP-based models

MLP-based models have recently emerged as a key methodology for replacing Transform-
ers in time series forecasting tasks. The simple structure of MLPs makes them easy to han-
dle and interpret. Additionally, they perform well even in constrained environments with 
limited computational resources and limited data. Their lightweight architectures enable fast 
training and inference, making them increasingly important and widely used in contempo-
rary industries. Previously, interest in MLPs diminished due to their structural limitations, 
such  as  the  lack  of  sequential  dependency,  challenges  with  long-term  dependency,  diffi-
culties in processing high-dimensional data, and limitations in capturing periodic patterns. 
However, recent advancements have enabled long-sequence learning and various technical 
enhancements, leading to remarkable performance improvements.

N-BEATS (Oreshkin et al 2020), consisting of simple Fully Connected (FC) layers, dem-
onstrated superior performance compared to traditional statistical models. This model uti-
lizes  a  block-based  architecture  with  repeatedly  stacked  backcast  and  forecast  paths  and 
enhances generalization performance through ensemble learning. By applying decomposi-
tion, it separates trend and seasonality, modeling them using Polynomial Basis and Fourier 
Basis, respectively, making it highly interpretable. BMoreover, recent studies have improved 
the N-BEATS model to predict various quantiles, enabling probabilistic forecasting (Smyl 
et al 2024). The improved N-HiTS (Challu et al 2023) model can handle multivariate data 
and  overcomes  the  limitations  of  N-BEATS  by  employing  techniques  such  as  multi-rate 
signal  sampling,  non-linear  regression,  and  hierarchical  interpolation.  Koopa  (Liu  et  al 
2024d) is a model designed to effectively handle non-stationary time series data by utilizing 
Koopman theory to predict the dynamic changes of components. It uses a Fourier filter to 
separate time-invariant and time-variant elements, which are then fed into respective Koop-
man  predictors(KP).  In  KP,  nonlinear  time  series  data  are  linearly  transformed,  making 
them  easier  to  manage. To  effectively  capture  the  characteristics  of  each  component,  the 
time-invariant  KP  uses  a  globally  learned  Koopman  operator,  while  the  time-variant  KP 
computes a local operator for predictions. TSMixer (Ekambaram et al 2023) is a lightweight 
patch-based  model  that  introduces  the  MLP-mixer  from  the  computer  vision  field  to  the

---

<!-- PAGE 37 -->

Page 37 of 95  216

time-series  domain.  It  efficiently  learns  long-term  and  short-term  dependencies  through 
inter-patch and intra-patch mixers respectively, and explicitly learns channel relationships 
through an inter-channel mixer. To enhance the understanding of inter-channel correlations, 
it adjusts the original forecast results using reconciliation heads and employs gated attention 
to filter important features. By introducing these techniques, TSMixer upgrades the simple 
MLP structure, resulting in improved performance that outperforms complex Transformer 
models. FreTS (Yi et al 2024) is a model that leverages two key characteristics of the fre-
quency domain-global view and energy compaction-to directly train an MLP model in the 
frequency domain. While existing models primarily use frequency transformation to verify 
the periodicity of the model, this model distinguishes between channel and temporal depen-
dencies in the frequency domain as real and imaginary parts, respectively, and learns them 
directly to better extract hidden features. TSP (Wang et al 2024e) utilizes a PrecMLP block 
with  a  precurrent  mechanism  to  effectively  model  temporal  locality  and  channel  depen-
dency. The precurrent mechanism combines previous information with current information 
to create hybrid features at each time point, serving as a computationally-free method to 
effectively recognize and process temporal locality. This lightweight MLP model comprises 
an encoder, consisting of tMLP operating in the time dimension and vMLP operating in the 
variable dimension, and a decoder using a linear model. FITS (Xu et al 2024c) is a very 
lightweight model with fewer than 10,000 parameters, yet it demonstrates competitive per-
formance comparable to larger models. It performs interpolation through a complex linear 
layer  that  learns  amplitude  scaling  and  phase  shifts  in  the  frequency  domain,  thereby 
expanding the frequency representation of the input time series. By using a low-pass filter 
to remove high-frequency components, which are often noise, the model efficiently repre-
sents the data and reduces the number of learnable parameters. U-Mixer (Ma et al 2024) 
utilizes a hierarchical structure of U-Net’s encoder–decoder composed of MLPs to extract 
and combine low-dimensional and high-dimensional features. Each MLP block processes 
temporal dependencies and channel interactions separately, enabling stable feature extrac-
tion. Additionally, the model employs a stationary correction method to limit the differences 
in data distribution before and after processing, thereby restoring the non-stationary infor-
mation of the data. By calculating the transformation matrix and mean difference between 
the input and output data, the model adjusts the output to maintain temporal dependency, 
thereby  enhancing  its  prediction  performance.  TTMs  (Ekambaram  et  al  2024)  is  a  time 
series foundation model that uses TSMixer as its backbone and relies solely on time series 
data for rapid pre-training. This model is trained on the extensive collection of time series 
datasets with diverse channels and resolutions from the Monash archive (Table 3). Despite 
the  data-specific  characteristics  of  the  time  series  datasets,  TTMs  demonstrate  efficient 
transfer learning and high generalization performance. TimeMixer (Wang et al 2024a) lever-
ages  the  observation  that  time  series  data  exhibit  distinct  patterns  at  different  sampling 
scales. To extract important information from past data, multi-scale time series are gener-
ated through downsampling. In the Past-Decomposable-Mixing (PDM) block, the seasonal 
and trend components are decomposed and mixed separately. The Future-Multipredictor-
Mixing (FMM) block then integrates predictions by ensembling multiple predictors, which 
utilize the past information extracted at various scales. CATS (Lu et al 2024) enhances the 
performance  of  multivariate  time  series  forecasting  by  generating Auxiliary  Time  Series 
(ATS) from the Original Time Series (OTS) and integrating them into the prediction pro-
cess. The model proposes various types of ATS constructors, each with different roles and

---

<!-- PAGE 38 -->

216  Page 38 of 95

s
p
i
h
s
n
o
i
t
a
l
e
r

s
e
c
n
e
u
q
e
s

g
n
o
l

h
t
i

w
e
l
g
g
u
r
t
s

x
e
l
p
m
o
c

g
n
i
r
u
t
p
a
c

y
l
e
v
i
t
c
e
ff
e

y
a
m

t
u
b

s
e
i
c
n
e
d
n
e
p
e
d

l
a
r
o
p
m
e
t

s
n
r
e
t
t
a
p

l
a
c
o
l

t
e
r
p
r
e
t
n
i

,
s
e
r
u
t
c
u
r
t
s

h
p
a
r
g

g
n
i
s
u

s
e
d
o
n

g
n
i
l
d
n
a
h

y
l
e
v
i
t
c
e
ff
e

,
g
n
i
s
s
e
c
o
r
p

c
fi
i
c
e
p
s

g
n
i
r
u
t
p
a
c

y
l
e
v
i
t
c
e
ff
e

d
n
a

t
n
e
m
e
l
p
m

i

o
t

y
s
a
e

m
s
i
n
a
h
c
e
m

n
e
e
w
t
e
b

s
p
i
h
s
n
o
i
t
a
l
e
r

s
n
r
a
e
L

a
t
a
d

l
a
i
t
n
e
u
q
e
s

n
i

d
e
z
i
l
a
i
c
e
p
S

,
s
r
e
y
a
l

l
a
n
o
i
t
u
l
o
v
n
o
c

s
e
z
i
l
i
t

U

y
l
e
v
i
t
a
l
e
r

,
r
e
y
a
l

e
l
p
m
S

i

n
o
i
t
n
e
t
t
a
-
f
l
e
s

x
e
l
p
m
o
C

e
r
u
t
c
u
r
t

S

s
l
e
d
o
m
d
e
s
a
b
-
N
C
G
N
N
G

/

s
l
e
d
o
m
d
e
s
a
b
-
N
N
R

s
l
e
d
o
m
d
e
s
a
b
-
N
N
C

s
l
e
d
o
m
d
e
s
a
b
-
P
L
M

d
e
s
a
b
-
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

a
i
r
e
t
i
r
c

f
o

s
m
r
e
t

n
i

s
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
t

h
t
i

w
s
l
e
d
o
m
g
n
i
n
r
a
e
l

p
e
e
d

r
e
h
t
o
f
o

n
o
s
i
r
a
p
m
o
C

6
e
l
b
a
T

a
i
r
e
t
i
r

C

s
l
e
d
o
m

-
r
e
p

h
g
i
h

g
n
i
v
e
i
h
c
a

,
y
t
i
x
e
l
p
m
o
c

s
r
e
t
e
m
a
r
a
p

r
e
w
e
f

h
t
i

w
e
c
n
a
m
r
o
f

d
n
a

e
z
i
s

h
p
a
r
g

n
o

s
d
n
e
p
e
D

s

m
e
l
b
o
r
p

c
fi
i
c
e
p
s

n
i

a
t
a
d

d
e
t
i

m

i
l

y
t
i
x
e
l
p
m
o
c

g
n
o
l

r
o
f

w
o
l
s

e
b

n
a
c

t
u
b
s
t
e
s
a
t
a
d

s
n
o
i
t
a
t
u
p
m
o
c

d
e
z
i

h
p
a
r
g

n
o

g
n
i
d
n
e
p
e
d

s
e
i
r
a
V

r
e
l
l
a
m
s

n
o

y
l
e
v
i
t
c
e
ff
e

s
n
i
a
r
T

-
l
a
c
o
l

o
t

e
u
d

r
e
t
s
a
f

y
l
l
a
r
e
n
e
G

t
s
a
f

y
l
e
v
i
t
a
l
e
R

s
t
e
s
a
t
a
d

l
l
a
m

s

y
l
e
v
i
t
a
l
e
r

h
t
i

w

h
t
i

w
g
n
i
n
i
a
r
t

k
c
i
u
q

r
o
f

e
l
b
a
t
i
u
s

s
t
e
s
a
t
a
d

e
c
n
a
m
r
o
f
r
e
p

h
g
i
h

e
v
e
i
h
c
a

n
a
C

,
s
t
e
s
a
t
a
d

r
e
l
l
a
m
s

n
o

n
i
a
r
t

n
a
C

s
t
e
s
a
t
a
d

r
e
l
l
a
m
s

n
o

n
i
a
r
t

n
a
C

r
e
l
l
a
m
s

n
o

n
i
a
r
t

n
a
C

s
t
e
s
a
t
a
d

e
g
r
a
l

s
e
r
i
u
q
e
R

s
e
c
n
e
u
q
e
s

l
l
a
m
s

y
l
e
v
i
t
a
r
a
p
m
o
C

e
r
o
m
d
n
a

r
e
l
l
a
m
s

y
l
l
a
c
i
p
y
T

y
l
e
v
i
t
a
r
a
p
m
o
C

t
i

g
n
i
k
a
m

,
t
n
e
i
c
ffi
e
-
r
e
t
e
m
a
r
a
p

f
o

e
s
u

t
n
e
i
c
ffi
e

,
l
l
a
m
s

e
l
b
a
l
a
c
s

d
n
a

t
n
e
i
c
ffi
e
-
e
c
r
u
o
s
e
r

s
e
c
r
u
o
s
e
r

e
v
i
s
n
e
t
n
i
-
r
e
t
e
m
a
r
a
p

e
u
d
w
o
l
s

y
l
e
v
i
t
a
l
e
R

n
o
i
t
n
e
t
t
a

l
a
b
o
l
g

o
t

y
l
e
v
i
t
a
r
a
p
m
o
C

e
r
o
m
d
n
a

r
e
g
r
a
l

s
m
s
i
n
a
h
c
e
m

s
t
n
e
m
e
r
i
u
q
e
r

a
t
a
D

e
m

i
t

g
n
i
n
i
a
r
T

e
z
i
s

l
e
d
o
M

s
e
r
u
t
c
u
r
t
s
d
n
a

s
e
p
y
t

a
t
a
d
t
n
e
r
e
ff
i
d

o
t

e
l
b
a
t
p
a
d
a

,
s
t
a
m
r
o
f

d
n
a

s
e
r
u
t

s
e
r
u
t
c
e
t
i
h
c
r
a

s
n
o
i
t
u
l
o
v
n
o
c

f
o

s
e
p
y
t

s
u
o

s
m
e
l
b
o
r
p

c
fi

i
c
e
p
s

s
t
n
e
m
t
s
u
j
d
a

g
n
i
n
r
a
e
l

n
i

e
c
n
a
m
r
o
f
r
e
p

h
g
i
h

g
n
i

n
i

e
c
n
a
m
r
o
f
r
e
p

t
n
e
i
c
ffi
u
s

g
n
i

l
a
c
o
l

g
n
o
r
t
s

h
t
i

w
s
m
e
l
b
o
r
p

r
o
f

n
i

e
c
n
a
m
r
o
f
r
e
p

t
n
e
i
c
fi

s
n
r
e
t
t
a
p

p
i
h
s
n
o
i
t
a
l
e
r

c
fi
i
c
e
p
s

s
m
e
l
b
o
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

c
fi
i
c
e
p
s

s
n
r
e
t
t
a
p

s
e
s
a
c

y
n
a
m

y
t
i
x
e
l
p
m
o
c

r
o
i
v
a
h
e
b

s
p
a
m
e
r
u
t
a
e
f

-
d
n
e
p
e
d

e
l
b
a
t
e
r
p
r
e
t
n
i

y
l
e
t
a
r
e
d
o
M

r
e
i
s
a
e

,
e
l
b
a
t
e
r
p
r
e
t
n
i

y
l
e
t
a
r
e
d
o
M

l
e
d
o
m
d
n
a

e
r
u
t
c
u
r
t
s

h
p
a
r
g

n
o

g
n
i

l
e
d
o
m
n
i
a
l
p
x
e

d
n
a

d
n
a
t
s
r
e
d
n
u

o
t

h
g
u
o
r
h
t

e
l
b
a
t
e
r
p
r
e
t
n
i

e
r
o
M

d
n
a

s
r
e
t
l
fi
f
o

s
n
o
i
t
a
z
i
l
a
u
s
i
v

h
g
i
h

y
l
e
v
i
t
a
l
e
R

y
t
i
l
i
b
a
t
e
r
p
r
e
t
n
i

t
e
r
p
r
e
t
n
i

o
t

t
l
u
c
ffi
D

i

y
t
i
l
i
b
a
t
e
r
p
r
e
t
n
I

-
r
e
ff
o

,
s
e
d
o
n

n
e
e
w
t
e
b

s
e
i
c
n
e
d
n
e
p

-
d
i
v
o
r
p

,
s
e
i
c
n
e
d
n
e
p
e
d

l
a
i
t
n
e
u
q
e
s

r
o
i
r
e
p
u
s

,
s
e
i
c
n
e
d
n
e
p
e
d

l
a
r
o
p

-
f
u
s

h
t
i

w
s
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
c
n
e
d
n
e
p
e
d
m
r
e
t
-
g
n
o
l

-
e
d

x
e
l
p
m
o
c

g
n
i
n
r
a
e
l

t
a

s
l
e
c
x
E

d
n
a
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

e
l
b
a
t
i
u
S

-

m
e
t

l
a
c
o
l

g
n
i
r
u
t
p
a
c

t
a

s
l
e
c
x
E

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

e
l
b
a
t
i
u
S

g
n
i
n
r
a
e
l

r
o
f

e
l
b
a
t
i
u
S

e
c
n
a
m
r
o
f
r
e
P

-
c
u
r
t
s

h
p
a
r
g

s
u
o
i
r
a
v
e
l
d
n
a
h

n
a
C

N
N
R
s
u
o
i
r
a
v

h
t
i

w
e
l
b
i
s
n
e
t
x
E

-
i
r
a
v

h
t
i

w
e
l
b
a
z
i
m
o
t
s
u
c

y
l
i
s
a
E

r
o
f

e
l
b
a
t
s
u
j
d
a

y
l
i
s
a
E

x
e
l
p
m
o
c

s
e
r
i
u
q
e
R

y
t
i
l
i
b
i
x
e
l

F

s
h
p
a
r
g

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
d
n
a

s
n
o
i
t
a
c
fi
i
d
o
m

t
u
o
h
t
i

w
s
e
i
c
n
e
d

s
m
e
l
b
o
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

f
o
e
g
n
a
r

-
t
e
n

l
a
i
c
o
s

e
k
i
l

s
k
s
a
t

n
i

s
e
r
u
t
c
u
r
t
s

t
u
b

,
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

d
n
a

l
a
r
o
p
m
e
t
d
n
a

l
a
i
t
a
p
s

g
n
i
r
i
u
q
e
r

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

l
a
r
e
n
e
g

r
o

s
m
e
l
b
o
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

,
s

m
e
t
s
y
s

n
o
i
t
a
d
n
e
m
m
o
c
e
r

,
s
k
r
o
w

-
n
e
p
e
d
m
r
e
t
-
g
n
o
l

h
t
i

w
s
e
l
g
g
u
r
t
s

e
d
i
w
a

r
o
f

e
v
i
t
c
e
ff
e

,
y
t
i
l
a
c
o
l

s
m
e
l
b
o
r
p

s
k
s
a
t

d
e
t
a
l
e
r
-
P
L
N

h
p
a
r
g

x
e
l
p
m
o
c

r
o
f

e
l
b
a
t
i
u
S

a
t
a
d

l
a
i
t
n
e
u
q
e
s

r
o
f

e
v
i
t
c
e
ff
E

s
n
o
i
t
a
c
i
l
p
p
a

r
o
f

d
e
t
i
u
s
-
l
l
e

W

s
u
o
i
r
a
v

r
o
f

e
l
i
t
a
s
r
e
V

x
e
l
p
m
o
c

r
o
f

e
l
b
a
t
i
u
S

n
o
i
t
a
c
i
l
p
p
A

---

<!-- PAGE 39 -->

Page 39 of 95  216

n
o

s
d
n
e
p
e
d
t
u
b
w
o
l

y
l
l
a
r
e
n
e
G

l
e
l
l
a
r
a
p

n
o

t
n
e
i
c
ffi
e
n
i

t
u
b
w
o
L

e
z
i
s

h
p
a
r
g

e
r
a
w
d
r
a
h

d
n
a

l
a
n
o
i
t
a
t
u
p
m
o
c

r
e
w
o
L

s
t
n
e
m
e
r
i
u
q
e
r

y
r
o
m
e
m

d
n
a

e
r
u
t
c
u
r
t
s

r
e
l
p
m
i
s

l
a
n
o
i
t
a
t
u
p
m
o
c

r
e
w
e
f

r
i
e
h
t

o
t

e
u
d

r
e
w
o
L

y
l
l
a
n
o
i
t
a
t
u
p
m
o
c

d
n
a

e
r
u
t
c
u
r
t
s

x
e
l
p
m
o
c

r
i
e
h
t

o
t

e
u
d

h
g
i
H

s
d
n
a
m
e
d

n
o
i
t
n
e
t
t
a
-
f
l
e
s

e
v
i
s
n
e
t
n
i

s
m
s
i
n
a
h
c
e
m

s
l
e
d
o
m

s
t
n
e
m
e
r
i
u
q
e
r

e
r
a
w
d
r
a
H

s
l
e
d
o
m
d
e
s
a
b
-
N
C
G
N
N
G

/

s
l
e
d
o
m
d
e
s
a
b
-
N
N
R

s
l
e
d
o
m
d
e
s
a
b
-
N
N
C

s
l
e
d
o
m
d
e
s
a
b
-
P
L
M

d
e
s
a
b
-
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

a
i
r
e
t
i
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

n
o

s
d
n
e
p
e
d
t
u
b
w
o
l

y
l
l
a
r
e
n
e
G

h
t
i

w
e
s
a
e
r
c
n
i

n
a
c

t
u
b
w
o
L

o
t

e
u
d
e
g
a
s
u

y
r
o
m
e
m

r
e
w
o
L

e
g
a
s
u

y
r
o
m
e
m

r
e
w
o
L

e
g
a
s
u

y
r
o
m
e
m

r
e
h
g
i
H

e
g
a
s
u

y
r
o
m
e
M

e
z
i
s

h
p
a
r
g

h
t
g
n
e
l

e
c
n
e
u
q
e
s

s
n
o
i
t
a
r
e
p
o

d
e
z
i
l
a
c
o
l

e
l
p
m
i
s

r
i
e
h
t

o
t

e
u
d

r
e
w
e
f

d
n
a

e
r
u
t
c
u
r
t
s

s
r
e
t
e
m
a
r
a
p

e
c
n
e
u
q
e
s

l
l
u
f

o
t

e
u
d

n
o
i
t
n
e
t
t
a

e
r
u
t
c
u
r
t
s

h
p
a
r
g

o
t

e
u
d

t
l
u
c
ffi
D

i

e
c
n
e
u
q
e
s

o
t

e
u
d

t
l
u
c
ffi
D

i

e
u
d
e
l
b
a
z
i
l
e
l
l
a
r
a
p

y
l
h
g
i
H

e
l
b
a
z
i
l
e
l
l
a
r
a
p

y
l
h
g
i
H

e
l
b
a
z
i
l
e
l
l
a
r
a
p

y
l
h
g
i
H

s
e
i
c
n
e
d
n
e
p
e
d

s
e
i
c
n
e
d
n
e
p
e
d

n
o
i
t
u
l
o
v
n
o
c

t
n
e
d
n
e
p
e
d
n
i

o
t

t
n
e
d
n
e
p
e
d
n
i

o
t

e
u
d

-
i
n
o
r
h
c
n
y
s

s
e
r
i
u
q
e
r

t
u
b

g
n
i
s
s
e
c
o
r
p

l
e
l
l
a
r
a
P

s
n
o
i
t
a
r
e
p
o

s
n
o
i
t
a
t
u
p
m
o
c

n
o
i
t
n
e
t
t
a

o
t

e
u
d

n
o
i
t
a
z

s
m
s
i
n
a
h
c
e
m

---

<!-- PAGE 40 -->

216  Page 40 of 95

objectives,  combining  them  to  maximize  predictive  performance. To  effectively  generate 
and utilize ATS, the model structure and loss function incorporate three key principles: con-
tinuity,  sparsity,  and  variability.  Despite  using  a  simple  two-layer  MLP  predictor  as  the 
foundation,  CATS  effectively  predicts  multivariate  information  through  the  use  of ATS. 
HDMixer (Huang et al 2024a) is a model that applies a Length-Extendable Patcher to over-
come  the  limitations  of  fixed-length  patching.  It  measures  the  point-wise  similarity  with 
fixed  patches  and  compares  the  patch  entropy  loss,  updating  parameters  to  increase  the 
complexity  of  the  extendable  patches.  Through  the  Hierarchical  Dependency  Explorer 
mixer,  it  learns  long-term,  short-term  dependencies  and  cross-variable  dependencies. 
SOFTS (Han et al 2024) proposes the STar Aggregate-Redistribute (STAR) Module to effec-
tively learn the relationships between channels. It converts the data from each channel into 
high-dimensional vectors and then aggregates these vectors to extract comprehensive infor-
mation, referred to as the core. The generated core representation is then combined with the 
time series representation of each channel and converted back to the time series dimension, 
reducing complexity and enhancing robustness. SparseTSF (Lin et al 2024b) is an extremely 
lightweight  model  that  uses  fewer  than  1,000  parameters  while  demonstrating  excellent 
generalization performance. It downsamples the data into multiple periods, performs pre-
dictions on each generated sub-sequence, and then upsamples to create the overall predic-
tion sequence. While it shows limited performance only on data with clear periodic patterns, 
it efficiently handles complex temporal dependencies with minimal computational resources. 
TEFN (Zhan et al 2024) proposes a novel backbone model from the perspective of informa-
tion  fusion  to  extract  latent  distributions  from  simple  data  structures.  Based  on  evidence 
theory (Shafer 1976), the Basic Probability Assignment Module maps each time and chan-
nel dimension of the time series data to a mass function in the event space. This mass func-
tion assigns probabilities to multiple possibilities for each data point, allowing for explicit 
modeling of uncertainty. The generated mass functions are fused using their expected values 
to derive the final predictions. This model achieves high predictive performance with few 
parameters and fast training times. PDMLP (Tang and Zhang 2024) surpasses the perfor-
mance of complex transformer-based models using only simple linear layers and patching. 
It divides the data into patches of various scales and embeds each patch with a single linear 
layer. The embedding vectors are then decomposed into smooth components and residual 
components containing noise, allowing the model to process the sequences in two ways: 
intra-variable and inter-variable. AMD (Hu et al 2024b) introduces the AMS block, which 
assesses the importance of various temporal patterns and generates appropriate weights for 
each pattern. By simultaneously modeling the temporal and channel dependencies of the 
input  information  decomposed  into  multiple  scales,  it  effectively  captures  interactions  at 
different scales. Instead of merely integrating the results from each scale, it improves pre-
diction performance by reflecting the importance of each pattern through the weights.

4.2.2  CNN-based models

CNNs were primarily developed for image recognition and processing tasks because they 
are highly effective at identifying 2D spatial patterns. Some studies have begun utilizing 
Temporal Convolutional Networks (TCNs), which are 1D CNNs that move along the time 
axis to recognize local patterns, effectively extracting key features of time series data. Addi-
tionally, CNNs can use filters of various sizes to capture patterns at multiple scales, allowing

---

<!-- PAGE 41 -->

Page 41 of 95  216

them to effectively learn both short-term and long-term patterns in time series data. CNN’s 
deep network technology and parallelism, which have been developed over a long period of 
time, have provided high performance and reliability for time series forecasting. However, 
the fixed filter size of CNNs lacks flexibility in learning complex patterns of long sequences 
and  poses  challenges  in  capturing  long-term  dependencies.  Furthermore,  as  the  network 
depth increases, there are limitations such as information loss, increased computational cost, 
and higher memory usage. For these reasons, the relatively flexible Transformer, which is 
advantageous for learning long-term dependencies, has gained more attention in time series 
data  processing.  However,  due  to  their  superior  ability  to  capture  diverse  local  patterns 
within long sequences, CNNs are once again receiving attention as a backbone architecture.
Recently, 3D convolution methodologies have been actively studied for handling com-
plex spatio-temporal time series data (Chen et al 2021c; Feng et al 2024a). 3D convolution 
processes  input  data  in  three  dimensions  (2D  spatial  axes  +  temporal  axis)  using  convo-
lution  operations.  This  approach  enables  the  extraction  of  richer  patterns  by  processing 
not only the temporal axis but also spatial or multi-dimensional aspects of the data. Such 
methods have demonstrated high performance in region-based prediction tasks, and future 
research  is  expected  to  focus  on  developing  more  sophisticated  data  representations  and 
learning structures.

TimesNet  (Wu  et  al  2023)  introduces  the  TimesBlock,  which  embeds  1D  time  series 
into 2D tensors for analysis to effectively capture multi-periodicity. Extracting key frequen-
cies via Fast Fourier Transformation (FFT) expands the data into a 2D tensor, representing 
intra-period variation  in  columns and inter-period  variation  in rows. It  uses  a parameter-
efficient Inception module with 2D kernels to capture temporal variations across various 
scales. After  converting  back  to  a  1D  tensor,  it  adaptively  aggregates  the  data  based  on 
the importance of frequency amplitude values. PatchMixer (Gong et al 2023) introduces a 
patch-mixing design to efficiently replace the permutation invariant property of the Trans-
former’s  attention  mechanism.  It  learns  intra-patch  correlations  using  single-scale  depth-
wise separable convolutions and inter-patch correlations using point-wise convolutions on 
the patched input sequence. ModernTCN (Luo and Wang 2024) enhances the fundamen-
tal TCNs  to  make  them  more  suitable  for  time  series  analysis.  Using  larger  kernels  than 
conventional  TCNs  expands  the  effective  receptive  field,  reducing  the  number  of  layers 
and effectively capturing long-term dependencies. It separates depth-wise convolution and 
point-wise convolution to independently learn temporal dependencies and feature depen-
dencies,  thereby  enhancing  computational  efficiency.  Additionally,  it  explicitly  handles 
cross-variable  dependency  in  multivariate  time  series  data,  resulting  in  improved  perfor-
mance. ConvTimeNet (Cheng et al 2024b) follows the framework of a Transformer encoder, 
replacing the role of self-attention with depthwise convolution and the role of multi-head 
attention with convolutions of various kernel sizes to increase computational efficiency. It 
uses Deformable Patch Embedding, which adaptively adjusts each patch’s size and posi-
tion based on the data. Depthwise convolutions capture temporal features for each chan-
nel, while point-wise convolutions model channel dependencies. ACNet (Zhang and Wang 
2024) aims to effectively model temporal dependencies and nonlinear features. It starts by 
removing unnecessary noise from the data using Wavelet Denoising. Then, it extracts tem-
poral features through Multi-Resolution Dilated Convolution and Global Adaptive Average 
Pooling. To more accurately capture nonlinear features, Gated Deformable Convolution is 
employed, which adaptively adjusts the sampling positions. Additionally, ACNet employs

---

<!-- PAGE 42 -->

216  Page 42 of 95

dynamic prediction, retraining the model with new data if prediction performance declines. 
FTMixer (Li et al 2024d) leverages the observation that the time domain effectively captures 
local dependencies while the frequency domain excels at learning global dependencies. It 
applies convolution in the frequency domain to capture global dependencies. Meanwhile, it 
converts multi-scale patches using Discrete Cosine Transformation (DCT), which is com-
putationally simpler than Discrete Fourier Transformation (DFT), and then applies convolu-
tion to capture local dependencies.

4.2.3  RNN-based models

RNNs were fundamentally developed to process sequential data. Their recurrent structure 
can  effectively  model  the  temporal  dependencies  of  time  series  data.  Gated  RNN  mod-
els, such as LSTM and GRU, have partially alleviated the long-term dependency issues of 
vanilla RNNs. However, RNNs are difficult to parallelize because they process data sequen-
tially.  This  slow  speed  is  particularly  detrimental  when  handling  long  sequences.  RNNs 
also have inherent limitations in learning long-term dependencies and global information. 
Transformers  have  effectively  addressed  these  issues  through  self-attention  mechanisms. 
However, unlike Transformers, which rely on large datasets, RNN-based models can learn 
effectively with smaller amounts of data. They also use memory efficiently and are well-
suited for real-time data processing due to their sequential nature, making them advanta-
geous  for  online  streaming  applications. Additionally,  because  time  ordering  is  naturally 
learned, RNNs still have inherent advantages over Transformers for time series processing.
PA-RNN (Zhang et al 2024c) aims to address prediction Uncertainty Quantification and 
Model  Compression  issues  for  dependent  time  series  data  by  proposing  an  optimization 
methodology for Sparse Deep Learning. It applies a Mixture of Gaussian Prior to introduc-
ing sparsity to the parameters and uses a Prior Annealing technique to gradually increase 
the strength of the prior distribution during the training process. Properties such as Poste-
rior  Consistency,  Structure  Selection  Consistency,  and Asymptotic  Normality  ensure  the 
model’s theoretical validity. WITRAN (Jia et al 2024) proposes a new paradigm by imple-
menting information transmission in bi-granular flows to capture long-term and short-term 
repetitive patterns. It models global and local correlations through the Horizontal Vertical 
Gated Selective Unit (HVGSU), which uses bidirectional Gated Selective Cells (GSC). To 
enhance the efficiency of information transmission through parallel processing, it applies the 
Recurrent Acceleration Network (RAN). This approach results in excellent prediction per-
formance while reducing time complexity and maintaining memory complexity. SutraNets 
(Bergsma et al 2023) transforms long sequences into multiple lower-frequency sub-series 
in  order  to  effectively  predict  long  sequence  time  series  data.  It  performs  autoregressive 
predictions among the sub-series, with each sub-series being conditionally predicted based 
on the values of other sub-series. This approach reduces the signal path length and allows 
for the generation of long sequences in fewer steps. Consequently, it mitigates the common 
RNN problem of error accumulation and models long-distance dependencies better. Cross-
WaveNet (Huang et al 2024b) uses a dual-channel network to separate and process the sea-
sonality and trend-cyclic components of data. The input data are initially decomposed into 
individual elements through series decomposition, and features are extracted using enriched 
LSTM and GRU structures. These extracted features undergo a cross-decomposition pro-
cess  to  further  refine  the  elements,  which  are  then  sent  to  each  channel  for  integration.

---

<!-- PAGE 43 -->

Page 43 of 95  216

Series  decomposition  is  performed  at  each  RNN  step,  progressively  filtering  and  reinte-
grating the seasonality and trend components to learn precise information. DAN (Li et al 
2024c) proposes a new model that utilizes Polar Representation learning to predict long-
term time series data with high volatility. The Distance-weighted Auto-regularized Neural 
network  (DAN)  distinguishes  and  learns  the  polar  representations  of  distant  and  nearby 
data, combining them to enhance prediction performance. It addresses the imbalance prob-
lem of extreme data, which occur infrequently but are critical for accurate predictions, using 
Kruskal-Wallis Sampling and employs a Multi-Loss Regularization Method to effectively 
learn both extreme and normal values simultaneously. RWKV-TS (Hou and Yu 2024) pro-
poses an efficient Recurrent Weighted Key-Value (RWKV) backbone characterized by lin-
ear time complexity and memory usage. It uses a Multi-head Weighted Key-Value (WKV) 
Operator,  which  is  similar  to  the  self-attention  mechanism  but  maintains  linear  time  and 
space complexity. Each head captures different temporal patterns, increasing the represen-
tational power of the information and enabling parallel computation, thus providing high 
computational efficiency. This  allows  RWKV-TS  to  capture  longer  sequence  information 
more effectively than fundamental RNNs. CONTIME (Jhin et al 2024) introduces Continu-
ous GRU to minimize the prediction delay issue in time series forecasting. This approach 
applies Neural ODE to the existing GRU, modeling data changes continuously over time. 
The bi-directional structure integrates forward and backward through the time series data, 
capturing more accurate temporal dependencies. By employing Time-Derivative Regular-
ization, the model is guided to learn the rate of change in predictions over time, enhancing 
both the accuracy and speed of predictions.

4.2.4  GNN-based models

GNNs or GCNs are specialized in processing graph-structured data, being suitable for mod-
eling complex interactions and learning local patterns in time series data. Multivariate time 
series  data  often  involve  interactions  between  variables,  which  can  be  effectively  repre-
sented as relationships between nodes and edges. By assigning various attributes to nodes 
and edges, richer representations can be learned, and the structural characteristics of specific 
domains can be better reflected. Traditionally, various approaches such as GCN, ST-GCN, 
GAT,  and  TGN  have  been  proposed,  contributing  to  the  advancement  of  the  time  series 
forecasting field.

However,  these  models  primarily  focus  on  learning  local  information  from  adjacent 
nodes, leading to a lack of capability in learning global information and difficulty in cap-
turing long-term dependencies with distant nodes. The sequential calculation of nodes and 
edges makes parallel processing challenging, and the models’ specificity to particular graph 
structures reduces their generalization ability. These drawbacks have diminished interest in 
GNN-based models. However, with the recent advancements in social networks, much of 
current data naturally follows a graph structure. Various optimization techniques and hard-
ware acceleration technologies have been developed, making it possible to process large-
scale  graph  data. Additionally,  the  increased  practical  relevance  due  to  the  flexibility  in 
dynamically handling time-varying data has once again drawn researchers’ attention to this 
architecture.

MSGNet (Cai et al 2024a) effectively learns the complex correlations of MTS data by 
combining frequency domain analysis with adaptive graph convolution. It uses Fast Fourier

---

<!-- PAGE 44 -->

216  Page 44 of 95

Transformation  to  identify  key  periods  and  transform  time  series  data  into  various  time 
scales. Then, it employs Mixhop graph convolution to learn inter-channel correlations and 
uses Multi-head Attention and Scale Aggregation to capture intra-series correlations. TMP-
Nets (Coskunuzer et al 2024) is a model proposed to learn features extracted from Temporal 
MultiPersistence (TMP) vectorization and capture key topological patterns. It combines two 
advanced  topological  data  analysis  techniques,  Multipersistence  and  Zigzag  Persistence, 
to  effectively  capture  topological  shape  changes  in  the  data.  Spatial  Graph  Convolution 
is  used  to  model  dependencies  between  nodes  in  the  graph,  and  the  topological  features 
extracted with TMP vectors are learned using CNN. HD-TTS (Marisca et al 2024) is a model 
that demonstrates high performance even with missing data through masking and hierarchi-
cal  downsampling.  It  incrementally  reduces  data  in  the  temporal  and  spatial  processing 
modules, learning various temporal and spatial dependencies. The model uses an attention 
mechanism to learn the patterns of missing values and combines them with weights to gen-
erate the final prediction. ForecastGrapher (Cai et al 2024b) is based on the finding that the 
attention mechanism is more suitable for modeling inter-channel correlations than temporal 
correlations. Utilizing the similarity between GNN’s neighborhood aggregation and atten-
tion  mechanisms,  it  linearly  embeds  each  channel  as  a  node  and  learns  the  relationships 
between channels using GNN. Each GNN layer employs a self-learnable adjacency matrix 
to independently learn the interactions between nodes. It uses learnable scalers to divide 
node features into multiple groups and applies 1D convolution to each group.

4.2.5  Model-agnostic frameworks

Some studies propose model-agnostic methodologies that can be universally applied with-
out being limited to a specific model backbone. These studies focus on the intrinsic charac-
teristics of time series data or specific problems, improving model robustness by addressing 
these issues. Model-agnostic architectures, not being tied to a particular model, allow for 
flexible selection of the optimal model through various comparisons. They are also highly 
reusable  and  make  it  easier  to  interpret  and  understand  the  model’s  predictions,  making 
them applicable to a wide range of domains and scenarios.

These models primarily address the distribution shift problem, which is one of the core 
issues in time series forecasting, and propose various plug-and-play alleviation methods. 
The details related to this will be discussed in Sect. 5, while here, we will focus on other 
methodologies, excluding distribution shift alleviation methods.

RobustTSF  (Cheng  et  al  2024a)  introduces  a  selective  sampling  algorithm  to  train  a 
resilient prediction model in Time Series Forecasting with Anomalies (TSFA). It calculates 
anomaly  scores  based  on  the  difference  between  the  trend  and  the  actual  data,  selecting 
samples with scores below a certain threshold to train the model, thereby minimizing the 
impact of anomalies. By analyzing three types of anomalies (Constant, Missing, Gaussian), 
it identifies the most robust loss function as MAE. This approach addresses the discontinu-
ity issues of the traditional detection-imputation-retraining pipeline, enabling the model to 
deliver more stable and consistent performance. PDLS (Hounie et al 2024) proposes a con-
strained learning approach by setting an upper bound on the loss at each time step. It controls 
the loss by setting a constant upper bound (ϵ) for all time steps and introduces a variable 
(ζ) that relaxes the constraints, allowing automatic adjustment during training. This model 
overcomes the problem of existing methodologies that focus on averaging prediction per-

---

<!-- PAGE 45 -->

Page 45 of 95  216

formance, which often leads to uneven error distributions. Leddam (Yu et al 2024) proposes 
two independently usable modules, Learnable Decomposition and Dual Attention, to effec-
tively capture the complex patterns of inter-series dependencies and intra-series variations 
in  MTS.  The  Learnable  Decomposition  module  replaces  the  traditional  moving  average 
kernel with a learnable 1D convolution kernel initialized with a Gaussian distribution for 
decomposition, making it more sensitive to critical information. The Dual Attention module 
simultaneously models inter-data dependencies and intra-series variability using channel-
wise  self-attention  and  auto-regressive  self-attention.  InfoTime  (Qi  et  al  2024)  proposes 
a  method  to  effectively utilize inter-channel  and  temporal correlations.  For  channel  mix-
ing, it employs Cross-variable Decorrelation Aware feature Modeling (CDAM) to minimize 
redundant information between channels and enhance useful mutual information. Addition-
ally,  it  uses TAM(Temporal  correlation Aware  Modeling)  to  maximize  the  temporal  cor-
relations between the predicted future sequence and the target sequence. CCM (Chen et al 
2024a) combines the strengths of the traditional channel-independent and channel-depen-
dent strategies to overcome their limitations. It dynamically clusters channels based on their 
inherent similarities and learns representative patterns for each cluster to generate prototype 
embeddings. Separate FFNs are used for each cluster to perform predictions for the channels 
within the cluster, and the prototype embeddings enable zero-shot predictions. HCAN (Sun 
et al 2024b) addresses the issue of excessive flattening caused by using the MSE loss func-
tion and proposes reconfiguring the prediction problem as a classification problem to better 
learn high-entropy features. It extracts important features from the backbone model, divides 
them into multiple layers and categories, and uses an Uncertainty-Aware Classifier at each 
layer to reduce uncertainty. It learns relative prediction values within each classified cate-
gory and integrates the prediction results from multiple layers through the Hierarchy-Aware 
Attention module. This approach effectively captures the complex patterns and variability 
in time series data. TDT Loss (Xiong et al 2024) points out the error accumulation issue in 
the traditional auto-regressive approach which recursively models Temporal Dependencies 
among Targets (TDT). To effectively capture changes between consecutive time points, it 
represents TDT using first-order differencing. The final TDT loss combines the target pre-
diction  loss, TDT  values  prediction  loss,  and  an  adaptive  weight,  allowing  the  model  to 
dynamically balance between target prediction and TDT learning. Thus, TDT loss replaces 
the optimization objective of non-autoregressive models.

The different deep learning models and their methodologies discussed so far are sum-

marized in Table 7.

4.3  Emergence of foundation models

In recent years, foundation models have demonstrated remarkable performance and strong 
zero-shot capabilities across various tasks and domains, leading to increased focus (Touvron 
et al 2023; Liu et al 2024a; Li et al 2023; Achiam et al 2023; Gallifant et al 2024; Radford 
et al 2021). While significant progress has been made in domains like vision and language, 
developing foundation models for time series data has faced several challenges. Firstly, time 
series data exhibit distinct characteristics depending on the dataset. For instance, electro-
cardiogram (ECG), weather, and sensor data from industrial processes have unique proper-
ties in terms of variables, frequency, periodicity, and noise, often requiring domain-specific 
knowledge for effective modeling. Additionally, unlike the vision and language domains,

---

<!-- PAGE 46 -->

216  Page 46 of 95

Table 7  Taxonomy and methodologies of fundamental deep learning architectures for time series forecasting
Model name

Main methodology

Base

N-BEATS

MLP

N-HiTS

Koopa

TSMixer

FreTS
TSP

FITS

U-Mixer

TTMs

TimeMixer

CATS

HDMixer

SOFTS

SparseTSF
TEFN

PDMLP

AMD

⋅ Neural basis expansion (polyno-
mial basis and Fourier basis)
⋅ Neural hierarchical interpolation
⋅ Multi-rate data sampling
⋅ Koopa block with koopman 
predictor(KP)
⋅ MLP mixer layer architecture
⋅ Gated attention (GA) block
⋅ Online hierarchical patch recon-
ciliation head
⋅ Frequency-domain MLPs
⋅ PrecMLP block with precurrent 
mechanism
⋅ Complex frequency linear 
interpolation
⋅ Low pass filter (LPF)
⋅ Unet Encoder–decoder with MLPs
⋅ Stationarity correction
⋅ Multi-resolution pre-training via 
TTM backbone (TSMixer blocks)
⋅ Exogenous mixer
⋅ Past-decomposable-mixing 
(PDM) block
⋅ Future-multipredictor-mixing 
(FMM) block
⋅ Auxiliary time series (ATS) 
constructor
⋅ Length-extendable patcher
⋅ Patch entropy loss
⋅ Hierarchical dependency explorer
⋅ STar Aggregate-redistribute 
module
⋅ Cross-period sparse forecasting
⋅ Basic probability assignment 
(BPA) module
⋅ Multi-scale patch embedding and 
feature decomposition
⋅ Intra-, Inter-variable MLP
⋅ Multi-scale decomposable mixing 
(MDM) block
⋅ Dual dependency interaction 
(DDI) Block
⋅ Adaptive multi-predictor synthesis 
(AMS) block

Channel 
correlation
CI

Publi-
cation
2020

CI

CD

CI/CD

CD
CD

CI

CD

CD

CD

CD

CD

CD

CI
CD

CD

CD

2023

2023

2023

2023
2024

2024

2024

2024

2024

2024

2024

2024

2024
2024

2024

2024

---

<!-- PAGE 47 -->

Base

CNN

Table 7  (continued)

Model name

TimesNet

PatchMixer

ModernTCN

ConvTimeNet

ACNet

FTMixer

PA-RNN

RNN

WITRAN

SutraNets

CrossWaveNet

DAN

RWKV-TS

CONTIME

MSGNet

GNN/GCN

TMP-Nets

HD-TTS

ForecastGrapher

Page 47 of 95  216

Channel 
correlation
CD

Publi-
cation
2023

CI

CD

CD

CD

CD

CI

CI

CI

CD

CI

CD

CI

CD

CD

CD

2023

2024

2024

2024

2024

2023

2023

2023

2024

2024

2024

2024

2024

2024

2024

CD

2024

Main methodology

⋅ Transform 1D-variatios into 
2D-variations
⋅ Timesblock
⋅ Patch embedding
⋅ PatchMixer layer with patch-
mixing design
⋅ ModernTCN block with DWConv 
and ConvFFN
⋅ Deformable patch embedding
⋅ Fully convolutional blocks
⋅ Temporal feature extraction 
module
⋅ Nonlinear feature adaptive extrac-
tion module
⋅ Frequency channel convolution
⋅ Windowing frequency convolution
⋅ Mixture Gaussian prior
⋅ Prior annealing algorithm
⋅ Horizontal vertical gated selective 
unit
⋅ Recurrent acceleration network
⋅ Sub-series autoregressive 
networks
⋅ Deep cross-decomposition
⋅ Dual-channel network
⋅ RepGen and RepMerg with polar 
representation learning
⋅ Distance-weighted multi-loss 
mechanism
⋅ Kruskal–Wallis sampling
⋅ RWKV blocks with multi-head 
WKV operator
⋅ Bi-directional continuous GRU 
with neural ODE
⋅ ScaleGraph block with scale 
identification
⋅ Multi-scale adaptive graph 
convolution
⋅ Multi-head attention and scale 
aggregation
⋅ Temporal MultiPersistence (TMP) 
vectorization
⋅ Temporal processing module with 
Temporal message passing
⋅ Spatial processing module with 
Spatial message passing
⋅ Group feature convolution GNN 
(GFC-GNN)

---

<!-- PAGE 48 -->

216  Page 48 of 95

Table 7  (continued)

Model name

Base

Main methodology

RobustTSF
PDLS

Model-agnostic

Leddam

InfoTime

CCM

HCAN

TDT loss

⋅ RobustTSF Algorithm
⋅ Loss shaping constraints
⋅ Empirical dual resilient and con-
strained learning
⋅ Learnable decomposition module
⋅ Dual attention module
⋅ Cross-variable decorrelation 
aware feature modeling (CDAM)
⋅ Temporal aware modeling (TAM)
⋅ Channel clustering and Cluster 
loss
⋅ Cluster-aware feed forward
⋅ Uncertainty-aware classifier 
(UAC)
⋅ Hierarchical consistency loss 
(HCL)
⋅ Hierarchy-aware attention (HAA)
⋅ Temporal dependencies among 
targets (TDT) loss

Channel 
correlation
–
–

Publi-
cation
2024
2024

CD

CD

CD

–

–

2024

2024

2024

2024

2024

-: Indicates that the feature is model-agnostic and depends on which backbone model is applied

where  large-scale  pre-training  corpora  can  be  relatively  easily  constructed  from  publicly 
available sources like the web, collecting time series data is more difficult due to high acqui-
sition costs and security concerns. Despite these obstacles, research on time series founda-
tion models is essential for improving model scalability and generality. This necessity has 
led  to  active  exploration  in  several  key  directions,  particularly  in  the  field  of  time  series 
forecasting (Table 8).

4.3.1  Sequence modeling with LLMs

One  prominent  approach  leverages  the  sequence  modeling  capabilities  of  LLMs.  LLMs 
have revolutionized deep learning with their groundbreaking generalizable sequence mod-
eling. Given the sequential nature of both text and time series data, extending the sequen-
tial capabilities of language models to time series is a natural progression. Early research 
includes GPT4TS (Zhou et al 2023), which demonstrates that by freezing most of the lan-
guage model’s backbone and fine-tuning only the layer normalization parameters and posi-
tional embeddings on time series data, GPT4TS can serve as a general time series task solver 
for forecasting, anomaly detection, and classification. Additionally, PromptCast (Xue and 
Salim 2023) introduces a framework where numerical time series sequences are input as 
text prompts to a large language model. Then the model outputs the forecasting results in 
a question-answering format. This approach integrates domain-specific knowledge through 
text and provides forecasting results in a human-friendly format.

Both GPT4TS and PromptCast rely on fine-tuning to achieve their results. In contrast, 
without fine-tuning, LLMTime (Gruver et al 2023) has demonstrated impressive zero-shot 
forecasting capabilities. The main idea of LLMTime is encoding time series data as a string 
of  numerical  digits,  which  emphasizes  the  importance  of  preprocessing  and  its  inherent

---

<!-- PAGE 49 -->

Table 8  Taxonomy and methodologies of foundation models for time series forecasting
Approach
Sequential mod-
eling with LLM

Model name
GPT4TS

Page 49 of 95  216

Main improvement and methodology
⋅ Demonstrate the effectiveness of LLM for time series 
modeling
⋅ Fine-tune the layer normalization and positional em-
bedding parameters
⋅ Enable text-level domain-specific knowledge for TSF
⋅ Cast TSF problem into question and answering format
⋅ Zero-shot TSF with pre-trained LLMs
⋅ Covert time series input into a string of digits
⋅ Align time series modality into text modality
⋅ Introduce patch reprogramming to mitigate a large 
reprogramming space
⋅ First pre-training based time series foundation model
⋅ Pre-train a decoder-only model with autoregressive 
loss
⋅ Pre-trained with hundreds of billions time steps
⋅ Autoregressive decoding with arbitrary forecasting 
length
⋅ Learning the language of time series
⋅ Utilize tokenizer to capture the intrinsic language of 
time series
⋅ Explicit consideration of multivariate TSF
⋅ Provide variate IDs to directly consider multiple 
variables

Publication
2023

2023

2023

2024

2024

2024

2024

2024

PromptCast

LLMTime

Time-LLM

Pre-training

Lag-Llama

TimesFM

CHRONOS

UniTS

dependencies. To align the time series modality with the language modality, Time-LLM (Jin 
et al 2024) introduces the concept of patch reprogramming. This concept aims to mitigate 
the challenges of a large reprogramming space and attempts to connect time series local 
characteristics with language semantics, such as “short up”. While patch reprogramming 
offers more flexibility by reducing the reliance on large-scale time series corpora, it also 
presents the challenge of adapting time series data to fit the characteristics of large language 
models.

4.3.2  Pre-training

Another approach that focuses on building large-scale time series corpora to pre-train time 
series foundation models from scratch has emerged. An example is Lag-LLaMA (Rasul et al 
2024),  which  uses  a  decoder-only  Transformer  to  generate  forecasting  results,  enabling 
probabilistic forecasting. Lag-LLaMA also consolidates 27 publicly available forecasting 
datasets from various domains to create a comprehensive pre-training corpus. On the other 
hand, TimesFM (Das et al 2024) extends beyond publicly available forecasting datasets by 
incorporating additional pre-training corpora based on Google Trends and Wiki Pageview 
statistics. It also utilizes synthetic datasets generated from piece-wise linear trends, autore-
gressive processes, and sine and cosine functions to capture universal characteristics. The 
entire pre-training corpus spans hundreds of billions of time steps. While most of the time 
series foundation models rely on temporal embedding, CHRONOS (Ansari et al 2024) takes 
a different idea by learning a patch-based tokenizer, similar to conventional language mod-
els, to capture the intrinsic “language” of time series data.

---

<!-- PAGE 50 -->

216  Page 50 of 95

Conventional foundation models often overlook the relationships between variables in 
multivariate time series forecasting, typically extending to multivariate forecasting by inde-
pendently  combining  univariate  forecasts  based  on  channel  independence.  Uni2TS  (Woo 
et al 2024) addresses this limitation by explicitly considering the expansion to arbitrary mul-
tivariate time series using variate IDs. Additionally, it leverages a large-scale time series data-
set called LOTSA, which accounts for multi-domain and multi-frequency characteristics.

4.4  Advance of diffusion models

Diffusion models are renowned generative models that have gained prominence for their 
ability to produce high-quality images, as demonstrated by DALL-E2 (Ramesh et al 2022), 
Stable Diffusion (Rombach et al 2022), and Imagen (Saharia et al 2022). In addition to their 
success in image generation, diffusion models have shown excellent performance in various 
fields,  such  as  audio  generation,  natural  language  processing,  and  video  generation  (Cao 
et al 2024). Consequently, there has been a growing number of research papers exploring 
their application in time series forecasting.

Diffusion models, theoretically proposed by Sohl-Dickstein et al (2015), are inspired by 
non-equilibrium  statistical  physics. They  learn  by  progressively  adding  noise  to  the  data 
and then gradually reversing the process to recover the original data. However, this initial 
research lacked concrete methods for training, making practical implementation challeng-
ing. This issue was addressed by Denoising Diffusion Probabilistic Models (DDPM) (Ho 
et al 2020) and Noise Conditional Score Networks (NCSN) (Song and Ermon 2019). DDPM 
models  the  forward  and  reverse  processes  explicitly  based  on  a  probabilistic  approach, 
enabling efficient learning. NCSN, on the other hand, employs score matching techniques 
to refine the noise removal process, resulting in the generation of higher-quality samples.

A diffusion model operates through two primary processes: the forward process and the 
reverse process. In the forward process, noise is gradually added to the data until it trans-
forms  into  complete  noise.  Conversely,  the  reverse  process  reconstructs  meaningful  data 
from random noise. By training a denoising network, the model generates data by injecting 
random values and processing them through the reverse process.

Diffusion models have a significant advantage in modeling uncertainty through the for-
ward and reverse processes. By providing multiple possible prediction outcomes instead of 
a single prediction, it can reflect the uncertainty of the real world, making it highly benefi-
cial for TSF. Therefore, it can offer prediction confidence intervals or enable probabilistic 
forecasting, thereby contributing to decision-making.

For forecasting tasks, it is crucial to employ conditional generation, where conditions are 
incorporated into the model to produce data that aligns with the given conditions. In this 
context, historical data is used as a condition and injected into the model to enable it to learn 
and predict future values. Figure 12 illustrates the diffusion model process, visualizing the 
transition from data to noise and back to data. Here, the addition of conditions explains the 
concept of the conditional diffusion model.

Diffusion-based models for time series forecasting have achieved significant performance 
improvements through the introduction of effective conditional embedding, the integration 
of time series feature extraction, and advancements in the diffusion models themselves. The 
following sections explain the key characteristics of diffusion-based models according to 
these classification criteria, and Table 9 provides a clear summary of this information.

---

<!-- PAGE 51 -->

Page 51 of 95  216

Fig. 12  Conditional diffusion process for time series data

Table 9  Taxonomy and methodologies of diffusion models for time series forecasting
Diffusion 
Main 
type
improvement

Main methodology

Model name

Conditional 
type

Effective condi-
tional embedding

TimeGrad

CSDI

SSSD
TimeDiff

TMDM

Time-series fea-
ture extraction

Diffusion-TS

Diffusion in 
frequency
MG-TSD

mr-Diff

SDE

ScoreGrad

D⌃3 M

Latent diffusion 
model

LDT

Guidance

TSDiff

⋅ Autoregressive DDPM using 
RNN and dilated convolution
⋅ 2D Attention for temporal and 
Feature dependency
⋅ Self-supervised training for 
imputation
⋅ Combination of S4 model
⋅ Future mixup
⋅ Autoregressive initialization
⋅ Integration of diffusion and 
transformer-based models
⋅ Decomposition techniques
⋅ Instance-aware guidance 
strategy
⋅ Diffusing in the frequency 
domain
⋅ Multi-granularity data 
generator
⋅ Temporal process module
⋅ Guided diffusion process 
module
⋅ Integration of decomposi-
tion and multiple temporal 
resolutions
⋅ Continuous energy-based 
generative model
⋅ Decomposable denoising dif-
fusion model based on explicit 
solutions
⋅ Symmetric time series 
compression
⋅ Latent diffusion transformer
⋅ Observation self-guidance

Pub-
lica-
tion
2021

DDPM Explicit

DDPM Explicit

2021

DDPM Explicit
DDPM Explicit

2023
2023

DDPM Explicit

2024

DDPM Guidance

2024

SDE

Explicit

2024

DDPM Explicit

2024

DDPM Explicit

2024

SDE

Explicit

2021

SDE

Explicit

2024

DDPM Guidance

2024

DDPM Guidance

2023

---

<!-- PAGE 52 -->

216  Page 52 of 95

4.4.1  Effective conditional embedding

Early diffusion-based models for time series forecasting focused on effective conditional 
embedding to guide the reverse process (Li et al 2024b). Typically, for forecasting tasks, 
conditional diffusion models use past data as a condition to predict the future. Therefore, the 
meticulous construction of the condition is paramount for the denoising model to effectively 
learn the data and enhance prediction performance. This highlights the importance of data 
preparation in the forecasting process. This preparation allows the model to effectively uti-
lize past information, thereby enhancing the accuracy of future time-series predictions and 
improving the model’s ability to learn from historical data.

TimeGrad (Rasul et al 2021) is the first notable diffusion model that operates using an 
autoregressive Denoising Diffusion Probabilistic Model (DDPM) (Ho et al 2020) approach. 
It encodes past data with an RNN, using the hidden state in a conditional diffusion model 
for forecasting. The hidden state encapsulates information from past sequential data, captur-
ing temporal dependencies effectively. The denoising network employs dilated ConvNets 
with  residual  connections,  adopted  from  WaveNet  (Van  Den  Oord  et  al  2016)  and  Dif-
fWave (Kong et al 2021), which are designed for audio generation. Unlike the commonly 
used  U-net  for  image  synthesis  in  diffusion  models,  TimeGrad  utilizes  a  broader  recep-
tive  field  suitable  for  time  series  data,  similar  to  audio.  CSDI  (Tashiro  et  al  2021)  cap-
tures temporal and feature dependencies of time series using a two-dimensional attention 
mechanism. Designed for both forecasting and imputation tasks, CSDI replaces RNNs with 
Transformers for imputation since RNNs are not suitable. The attention mechanism learns 
the relationships across all positions in the input sequence, capturing long-term dependen-
cies  effectively. Therefore,  for  long-term  time  series  forecasting,  using  attention  is  more 
advantageous than RNNs and dilated convolution, as seen in TimeGrad. SSSD (Alcaraz and 
Strodthoff 2023) demonstrates that replacing the Transformer used as the denoising network 
in CSDI with the S4 model (Gu et al 2022) yields superior performance. This is because 
S4 is more efficient and better at capturing long-term dependencies compared to the high 
computational  complexity  required  for Transformer  attention.  TimeDiff  (Shen  and  Kwok 
2023)  enhances  prediction  accuracy  by  using  future  mixups  during  training,  mixing  past 
data with actual future values to generate conditional signals. Including some actual future 
values helps the model create effective conditional signals for more accurate predictions. 
Additionally, it addresses the boundary disharmony issue in non-autoregressive models like 
CSDI and SSSD. TimeDiff uses a simple statistical model, the Linear Autoregressive model, 
to provide an initial guess, alleviating the boundary disharmony problem. TMDM (Li et al 
2024b)  offers  an  extreme  form  of  effective  conditional  embedding.  It  states  that  the  best 
condition  is  the  prediction  itself,  using  prediction  values  from  transformer-based  models 
like Informer (Zhou et al 2021) or Autoformer (Wu et al 2021), which have shown good 
performance in time series forecasting tasks, as the condition. This allows the Transformer 
to handle the estimated mean while the diffusion model focuses on uncertainty estimation. 
Unlike previous researches that utilize conditional embeddings only in the reverse process, 
TMDM uses conditional information as prior knowledge for both the forward and reverse 
processes.

---

<!-- PAGE 53 -->

Page 53 of 95  216

4.4.2  Time series feature extraction

Time  series  data  hides  various  features,  and  there  are  techniques  to  extract  these  unique 
characteristics effectively. Thus, many works have emerged that combine time series feature 
extraction methods with diffusion models to understand the complex patterns in time series 
data and improve prediction performance.
Decomposition

Decomposition techniques involve breaking down time series data into components such 
as trend, seasonality, and irregularity, analyzing the unique patterns of each component. Dif-
fusion-TS (Yuan and Qiao 2024) points out that conventional methods cannot properly learn 
each  component  because  the  forward  process  causes  the  components  to  collapse. There-
fore, it models the decomposed time series data individually during the diffusion process, 
learning each component, such as trend, seasonality, and residuals, independently and then 
recombining them to restore the entire time series data.
Frequency domain

Fourier analysis, a type of decomposition technique, converts time series data into the 
frequency  domain  to  analyze  periodic  components.  This  method  helps  identify  periodic 
patterns and remove noise. Crabbé et al (2024) explore the idea that the representation of 
time series data in the frequency domain can provide useful inductive biases for score-based 
diffusion models. This paper demonstrates that the components of time series data are more 
clearly represented in the frequency domain, and diffusion models in the frequency domain 
outperform those in the time domain.
Multi-scale

Multi-scale techniques analyze time series data at various time scales, effectively extract-
ing long-term trends and diverse features. This approach plays a crucial role in understand-
ing the complex patterns of time series data to improve prediction performance. MG-TSD 
(Fan et al 2024b) observes that the forward process of diffusion models aligns with gradu-
ally smoothing fine data into coarser representations. It suggests that coarse-granularity data 
can serve as effective guides in the intermediate stages of diffusion models. In other words, 
the initial stages of the reverse process involve coarse-granularity data, guiding the process 
to intermediate-stage targets. This multi-granularity level approach helps learn various lev-
els of information, enhancing prediction stability and accuracy. mr-Diff (Shen et al 2024) 
constructs time series data at multiple resolutions, performing sequential predictions at each 
resolution. In the initial stages, it predicts coarse data, and in subsequent stages, it uses these 
predictions as conditions to generate finer data gradually. This structure incrementally adds 
finer patterns and noise at each stage, ultimately reconstructing high-resolution time series 
data. This allows for effective prediction of both long-term trends and short-term fluctua-
tions in time series data.

4.4.3  Additional approaches

Beyond the two main approaches mentioned earlier, there are numerous examples where 
techniques  evolving  from  the  diffusion  framework  itself  are  applied  to  models  for  time 
series forecasting.
Score-based generative modeling through SDEs

---

<!-- PAGE 54 -->

216  Page 54 of 95

Score-Based  Generative  Modeling  through  Stochastic  Differential  Equations  (SDEs) 
(Song et al 2021) serves as continuous energy-based generative models, handling data in 
a continuous time domain, thus reflecting natural and precise changes and noise in the real 
world. The previously discussed methods are based on DDPM (Ho et al 2020), which add 
and  remove  noise  incrementally  using  fixed-time  steps.  However,  the  DDPM  approach 
faces challenges such as specific functional constraints and sensitivity to hyperparameters. 
Some research applying SDEs overcomes these limitations and explores diverse approaches. 
ScoreGrad (Yan et al 2021) is the first work to apply SDE, overcoming the constraints of 
DDPM-based  models  and  offering  a  more  flexible  and  powerful  generative  model.  D3M 
(Yan et al 2024) addresses the limitations of conventional SDEs, such as the complexity of 
determining drift and diffusion coefficients and slow generation speed, by utilizing a decom-
posable  noise-removal  diffusion  model  based  on  explicit  solutions. This  method  reduces 
computational complexity through clear SDE formulations and separates the signal decay 
and noise injection processes in model design. As a result, it enhances model efficiency and 
accuracy while accelerating generation speed. Crabbé et al (2024) improve denoising score 
matching in the frequency domain by using mirrored Brownian motions instead of standard 
Brownian motion, emphasizing the symmetry between components when applying SDEs.
Latent diffusion model

Latent Diffusion Model (Rombach et al 2022) is a generative model that operates not on 
the original data directly but within a latent space where the diffusion process takes place. 
Transforming data into the latent space reduces complexity and stabilizes the training pro-
cess, resulting in high-quality outputs. LDT (Feng et al 2024b) applies the concept of the 
latent diffusion model to time series data, addressing the non-stationarity issues that often 
arise during the compression into the latent space. Dynamically updating statistical proper-
ties  during  the  autoencoder  training  process  effectively  overcomes  these  challenges  and 
enhances model performance.
Guidance

Some  works  use  guidance  instead  of  explicitly  feeding  conditions  into  the  denoising 
network for forecasting. Diffusion-TS (Yuan and Qiao 2024) employs classifier guidance, 
using a separate classifier to guide the sampling process through the gradients of the clas-
sifier.  This  method  maintains  the  basic  unconditional  diffusion  model  while  performing 
conditional generation tasks through various classifiers. It generates samples that are bet-
ter aligned with specific conditions, resulting in higher-quality outputs. However, classifier 
guidance requires a classifier for each time step, which necessitates training a new classifier 
instead  of  using  pre-trained  ones.  LDT  (Feng  et  al  2024b)  uses  classifier-free  guidance, 
learning both conditional and unconditional models within a single model to perform con-
ditional sampling. This work eliminates the need for an additional classifier and implicitly 
obtains a classifier, making implementation simpler and more efficient. TSDiff (Kollovieh 
et al 2024) proposes observation self-guidance, allowing the use of an unconditional dif-
fusion model for conditional generation without separate networks or modifications to the 
training process.

---

<!-- PAGE 55 -->

Page 55 of 95  216

4.5  Debut of the Mamba

4.5.1  History of the state space models (SSMs)

One of the notable recent developments is the emergence of a new architecture called Mamba 
(Gu and Dao 2024). In an atmosphere previously influenced by Transformers, Mamba has 
garnered significant interest from researchers and is rapidly establishing its own ecosystem.
RNNs,  which  were  once  the  mainstream  in  sequence  modeling,  lost  their  dominance 
after the advent of Transformers. This was due to the limitations in information encapsula-
tion  of  a  “context”  (single  vector)  in  RNN-based  encoder–decoder  models  and  the  slow 
training speed inherent in their recurrent nature. In contrast, the parallelism of the attention 
mechanism and its ability to focus on all individual pieces of information overcame the limi-
tations of RNNs and demonstrated superior performance. However, new challenges have 
emerged with Transformers, such as the quadratic computational complexity, which limits 
the window length, and the increased memory requirements for processing long sequences. 
Subsequently, many efforts have been made to overcome the limitations of both approaches 
while preserving their advantages. In this context, some research that continues the philoso-
phy of RNNs has turned its attention to state space models (SSMs) (Kalman 1960).

SSM  is  a  mathematical  framework  used  to  model  the  dynamic  state  of  a  system  that 
changes over time, compressing only the essential information for effective sequential mod-
eling. SSM describes the relationship between the internal state of the system and external 
observations and is used in various fields such as control theory, signal processing, and time 
series analysis. It comprises a ‘State equation’ that explains how the internal state changes 
over time and an ‘Observation equation’ that explains how the internal state is transformed 
into external observations. Although it is a continuous model that performs linear transfor-
mations on the current hidden state and input, it can handle discrete sequences like time 
series through discretization (Fig. 13). It closely resembles RNNs in that it combines obser-
vation data and hidden state data.

However,  SSMs  have  different  characteristics  from  RNNs  in  that  they  are  linear  and 
time-invariant (LTI). This means that the operations performed on each token do not vary, 
allowing for the pre-computation of global kernels. In other words, the parameter matrices 
of the system do not change over time and operate consistently across time. Therefore, the

Fig. 13  Diagram of discretized state space model

---

<!-- PAGE 56 -->

216  Page 56 of 95

ability  to  precompute  globally  applicable  kernels  enables  parallel  processing,  which  can 
overcome the limitations of RNNs.

Early  applications  of  SSMs,  such  as  the  S4  (Gu  et  al  2021)  model,  utilized  diagonal-
ization  of  the  transition  matrix  to  effectively  model  long-term  dependencies  in  long  and 
complex sequence data. These models were able to achieve high performance when com-
bined with deep learning architectures like Transformers, RNNs, and CNNs. Subsequently, 
based on S4, advanced blocks like H3 (Fu et al 2023) were developed, which hierarchically 
structured convolution, gating, and MLP to provide more efficient and powerful sequence 
modeling (Fig. 14).

4.5.2  Introduction of the Mamba

SSMs have fixed state transition and observation equations, which limits their ability to flex-
ibly handle input data. Furthermore, due to their inherent continuous system origins, they 
are weaker in information-dense and discrete domains such as text.

Mamba  addresses  these  limitations  of  SSMs  by  introducing  an  advanced  deep  struc-
tured  SSM  model  with  selective  SSM.  It  is  designed  so  that  the  parameters  of  the  SSM 
dynamically change depending on the input, allowing for selective memory or disregard of 
specific parts of the sequence, enabling efficient data processing. However, this approach, 
while enhancing the system’s flexibility to better learn complex patterns, sacrifices the par-
allel processing advantages of SSMs. To compensate, traditional techniques such as kernel 
fusion, parallel scan, and recomputation are applied to efficiently implement selective SSMs 
on GPUs. Mamba adopts a simplified architecture centered around selective SSM, replacing 
the first multiplicative gate in the traditional H3 block with an activation function and incor-
porating an SSM into the gated MLP block. Due to the absence of attention mechanisms or 
separate MLP blocks, computational complexity is reduced, resulting in efficient training, 
fast inference, and high scalability and versatility.

Fig. 14  Structure of the Mamba block

---

<!-- PAGE 57 -->

Page 57 of 95  216

4.5.3  Applications of the Mamba

In the field of time-series forecasting, there is a growing trend to apply Mamba. A lot of 
variants based on Mamba have been proposed to address TSF tasks, and these models are 
reported to exceed the performance of Transformer SOTA models.

Most of these models typically share the following common features:

● They aim to ensure stability in large networks. Mamba, based on SSM, heavily relies 
on the eigenvalues of the system’s dynamic matrix. Since the general solution of the 
system is expressed as an exponential function of the eigenvalues, if the real part of the 
eigenvalues is positive, the system cannot converge and becomes unstable. Therefore, a 
key feature is the ideation aimed at improving this instability.

● They  explicitly  incorporate  the  learning  of  channel  correlations.  Recent  research  has 
demonstrated the superiority of channel dependence (CD) learning strategies, and the 
adoption of the CD strategy by the iTransformer, which shows SOTA performance, has 
further heightened this trend. This is a common feature observed in other foundational 
models as well.

● They  incorporate  various  techniques  from  transformer-based  models.  Mamba-based 
models, which integrate various techniques from Transformers such as patching, fre-
quency domain application, bidirectional processing, and FFN incorporation, are dem-
onstrating  significant  performance  improvements.  The  diverse  techniques  developed 
over  many  years  of  research  on  Transformer  models  provide  valuable  ideation  for 
Mamba variants.

The following are representative examples of Mamba-based models for handling TSF tasks 
and their key technical features (Table 10).
Embedding and multi-scale learning

In  this  section,  we  introduce  methodologies  for  embedding  and  learning  from  data  at 
various scales. These approaches primarily focus on richly extracting information to capture 
long-term dependencies and context.

TimeMachine (Ahamed and Cheng 2024) aims to capture long-term dependencies and 
context  at  different  scales  through  two-stage  embeddings.  It  is  divided  into  internal  and 
external  embeddings  based  on  embedding  dimensions,  and  each  section  consists  of  two 
parallel  Mamba  modules  that  explore  temporal  dependencies  and  channel  dependencies, 
respectively. The internal Mamba module operates at a low resolution to capture both global 
and local contexts, while the external Mamba module operates at a high resolution to cap-
ture the global context.
Channel correlation learning

Next, we examine models that focus explicitly on learning the inter-channel correlations 
in time series data. These models are centered around techniques that effectively integrate 
information from each channel and model their interdependencies.

S-Mamba  (Wang  et  al  2024d)  features  bi-directional  Mamba  blocks  to  consider  both 
past and future information, enabling the learning of inter-channel correlations. The role of 
learning temporal dependencies is assigned to the Feed Forward Network (FFN). By clearly 
separating  the  roles  of  Mamba  blocks  and  FFN,  computational  efficiency  is  improved, 
ensuring the stability of the Mamba architecture in large networks. In SiMBA (Patro and

---

<!-- PAGE 58 -->

216  Page 58 of 95

Model name

Main methodology

Table 10  Taxonomy and methodologies of mamba models for time series forecasting
Main 
improvement
Embedding 
and multi-scale 
learning
Channel correla-
tion learning

⋅ Integrated quadruple 
Mambas

Channel 
correlation
CD

TimeMachine

S-Mamba

CD

Base

Mamba

Publi-
cation
2024

Mamba MLP 2024

SiMBA

MambaTS

C-Mamba

Sequence 
information and 
dependency 
learning

Mambaformer

Bi-Mamba+

Theoretical 
frameworks and 
efficient modeling

DTMamba

Time-SSM

Chimera

⋅ Channel mixing: Mamba 
VC Encoding layer
⋅ Sequence modeling: FFN 
TD encoding layer
⋅ Channel mixing: Einstein 
FFT (EinFFT)
⋅ Sequence modeling: 
Mamba
⋅ Temporal Mamba Block 
(TMB)
⋅ Variable permutation 
training (VPT)
⋅ Channel mixup
⋅ C-Mamba block 
(PatchMamba + channel 
attention)
⋅ Mambaformer (Attention 
+ Mamba) layer
⋅ Series-relation-aware 
(SRA) Decider
⋅ Mamba+ Block
⋅ Bidirectional Mamba+ 
Encoder
⋅ Dual Twin Mamba 
Blocks
⋅ Dynamic spectral opera-
tor with Hippo-LegP
⋅ 2-Dimensional state 
space model

CD

Mamba

2024

CD

Mamba

2024

CD

Mamba

2024

CI

CI/CD

Mamba 
Transformer
Mamba

2024

2024

CI

CD

CD

Mamba

Mamba

Mamba

2024

2024

2024

Agneeswaran 2024b), channel modeling is achieved through Einstein FFT (EinFFT), while 
sequence modeling is handled by Mamba modules. After applying the Fast Fourier Trans-
form  (FFT),  the  real  and  imaginary  parts  are  separated,  and  their  respective  weights  are 
learned. Channel mixing is performed through Einstein Matrix Multiplication (EMM), cre-
ating  new  data  that  reflects  the  relational  information  between  channels,  thus  internaliz-
ing channel relationships. Additionally, to ensure system stability, eigenvalues of the state 
matrix  are  adjusted  to  be  negative  through  Fourier  transformation  and  nonlinear  layers. 
MambaTS (Cai et al 2024c) reconstructs sequences by integrating past information of all 
variables to learn channel correlations. Since variable information is integrated in advance, 
unnecessary convolution in Mamba blocks is removed to enhance computational efficiency, 
and dropout is applied to Temporal Mamba Blocks (TMB) to reduce overfitting. Addition-
ally, Variable Permutation Training (VPT) is introduced to dynamically determine the opti-
mal  order  of  integrated  variable  information,  enabling  predictions  based  on  the  optimal 
sequence of variables. C-Mamba (Zeng et al 2024) generates new virtual sample data by 
linearly combining different channels (channel mixup), which is expected to enhance gen-

---

<!-- PAGE 59 -->

Page 59 of 95  216

eralization performance. It uses a main block that combines patched Mamba modules with 
attention modules for learning channel relationships.
Sequence information and dependency learning

This category emphasizes methods for learning the sequential information and depen-
dencies in time series data. It proposes various techniques for modeling both long-term and 
short-term dependencies within the series.

Mambaformer (Xu et al 2024a) is a hybrid model that combines Mamba with a Trans-
former decoder framework. Since the Mamba block naturally internalizes the sequence order 
information,  positional  embedding  is  unnecessary.  Long-term  dependencies  are  learned 
through  the  Mamba  block,  while  short-term  dependencies  are  captured  through  the  self-
attention  layer,  effectively  capturing  the  overall  dependencies. This  approach  overcomes 
the computational efficiency limitations of attention mechanisms. Bi-Mamba+ (Liang et al 
2024a) integrates patching techniques to finely learn inter-dependencies in the data. To pre-
serve long-term information, it introduces Mamba+ blocks, which add a forget gate to the 
Mamba block. It also employs a Bi-Mamba+ encoder to process input sequences bidirection-
ally. Using the Spearman correlation coefficient, the Series-Relation-Aware (SRA) decider 
is designed to automatically select channel tokenization strategies (CI or CD). DTMamba 
(Wu et al 2024b) is composed of Dual Twin Mamba blocks, effectively learning long-term 
dependencies in time series data channel independently. Each Twin Mamba block consists 
of two parallel Mamba structures that process the same input data to capture different pat-
terns effectively. One Mamba structure learns detailed patterns and short-term variations, 
while the other learns overall patterns and long-term trends.
Theoretical frameworks and efficient modeling

Lastly, we explore models that introduce new theoretical frameworks or propose efficient 
modeling techniques. These models focus on effectively capturing the dynamic characteris-
tics of time series data and employ theoretical approaches and methodologies that enhance 
computational efficiency.

Time-SSM (Hu et al 2024a) proposes a theoretical framework called the Dynamic Spec-
tral Operator, which extends the Generalized Orthogonal Basis Projection (GOBP) theory 
for efficient use of SSM. The Dynamic Spectral Operator explores the changing spectral 
space over time to effectively capture the dynamic characteristics of time series data. To 
implement this, a novel variant of the SSM basis called Hippo-LegP is proposed, enabling 
more  precise  modeling  of  time  series  data  and  achieving  optimal  performance  through 
S4D-real initialization. This allows it to demonstrate excellent performance with only about 
one-seventh of the parameters required by Mamba models. Chimera (Behrouz et al 2024) 
features the use of 2D SSM to capture dependencies independently along the time and vari-
able axes. By updating states in parallel along both axes, it achieves efficient computation.
The emergence of a new deep learning architecture, Mamba, is causing a shift in the long-
standing hegemony of deep learning architectures. In current TSF tasks, which increasingly 
deal with long-term sequences, Mamba’s strengths-efficient sequence processing, selective 
information retention, simplified architecture, and hardware optimization-prove to be highly 
valuable. These features allow Mamba-based models to overcome the limitations of Trans-
formers, showing rapid performance improvements in a short period and suggesting a new 
direction for deep learning modeling. The growth trajectory of Mamba raises attention to 
whether it will become the new dominance in this field.

---

<!-- PAGE 60 -->

216  Page 60 of 95

5  TSF latest open challenges and handling methods

5.1  Channel dependency comprehension

Spread of channel independent strategy

Multi-variate time series (MTS) forecasting primarily hinges on how well it can learn the 
short-term and long-term temporal dependencies. However, many recent real-world data-
sets predominantly deal with multivariate data, where the relationships between variables 
carry significant semantic information. As the relationships between variables become more 
complex, models can provide more information and thus improve predictive performance 
by leveraging this complexity.

Traditionally, it has been vaguely assumed that understanding the relationships between 
variables in time series forecasting problems would make better performance. Despite being 
obtained from different instruments, the data observe the same phenomenon, which intui-
tively suggests that they offer rich interpretations from various perspectives. However, with 
the  PatchTST  (Nie  et  al  2023)  model  adopting  a  channel-independent  (CI)  strategy  and 
achieving state-of-the-art (SOTA) performance, research has begun to question the previ-
ously assumed channel-dependent (CD) strategy. These studies have shown that high per-
formance can be attained without learning the interactions between variables.

The CI strategy simplifies the model by excluding inter-variable modeling, allowing it to 
focus solely on learning the temporal dependencies of each channel. This approach reduces 
model complexity and enables faster inference, while also mitigating the risk of overfitting 
due to noise from inter-variable interactions. Additionally, since the addition of new chan-
nels does not affect the model, it can adapt flexibly to changes in data. These advantages 
have led many studies to adopt the CI strategy, resulting in improved performance. How-
ever, the CI strategy did not consistently show superior performance across all studies. The 
CD strategy still demonstrated high performance in many studies, such as iTransformer (Liu 
et al 2024c). Additionally, both strategies showed inconsistent performance depending on 
the datasets used. Consequently, without clear justification, both CI and CD strategies were 
employed according to the researchers’ preferences for a period of time.
Importance of learning channel correlations

Learning  the  correlations  between  variables  remains  important.  In  multivariate  time 
series  data,  each  variable  does  not  change  independently  but  is  interdependently  related 
to others. Even if these relationships sometimes introduce noise or fail to provide critical 
information, the relationships themselves are not devoid of meaning. The information from 
multivariate variables often intertwines to create complex patterns that cannot be captured 
by a single variable. Understanding the correlations between multiple variables helps inter-
pret these complex patterns.

Modeling  the  correlations  between  variables  is  also  crucial  for  improving  prediction 
accuracy. Especially when dealing with long sequence patterns, it is essential to understand 
the numerous local patterns within them. During this process, important causal relationships 
are often derived from other variables or exogenous factors. In the case of noisy data, learn-
ing the correlations between variables can help extract key information effectively. By com-
prehensively observing the information from multiple variables, it is possible to emphasize 
important features and complement missing information.
What makes CI look better?

---

<!-- PAGE 61 -->

Page 61 of 95  216

If the CD strategy is important and has the potential for significant performance improve-
ments, why do many studies show that the CI strategy performs better? To answer this ques-
tion, some research has been conducted, and the following summary can be provided based 
on the “The capacity and robustness trade-off: Revisiting the channel independent strategy 
for multivariate time series forecasting” (Lu Han 2024) paper.

According to the study, an examination of the Auto-correlation Function (ACF) values 
between the training set and test set of the benchmark data, which have been used in various 
experiments,  revealed  a  distribution  shift. The ACF  can  identify  the  correlation  between 
data values at specific time lags in time series data.

A distribution shift refers to the difference in statistical properties between the training 
data and test data extracted from the same dataset. Distribution shifts can occur for various 
reasons, often due to anomalies in the training series or variations in the trend, but some-
times the exact cause cannot be clearly defined. An important finding from the study is that 
the CI strategy demonstrates relatively greater robustness to distribution shifts. Since the CI 
strategy relies on the average ACF of all channels, it is less sensitive to distribution shifts 
compared to the CD strategy, which depends on the ACF variations of individual channels. 
Additionally, by excluding inter-variable relationships, the CI strategy simplifies the model, 
reducing the likelihood of overfitting and enhancing robustness. Therefore, the CI strategy 
has been able to demonstrate good performance on benchmark datasets where distribution 
shifts are present.

However, this does not imply that the CI strategy is superior to the CD strategy. It merely 
suggests that, in some datasets, the positive effects resulting from the robustness of the CI 
strategy outweigh the advantages of learning inter-variable relationships. Conversely, if dis-
tribution shifts can be effectively alleviated, the CD strategy can provide much more useful 
information than the CI strategy. To this end, even the application of simple regularization 
methods, such as Predict Residual with Regularization (PRReg), adapting low-rank layers, 
and using the MAE loss function, can reverse the performance gap. Furthermore, various 
distribution shift alleviation methodologies have been researched, and these can be applied 
in a model-agnostic manner. The details of these methodologies will be discussed in the next 
section, and the previous content has been illustrated in Fig. 15
Recent approaches

As the effectiveness of learning channel correlation has been validated, recent multivari-
ate time series forecasting problems have predominantly adopted the CD strategy. In con-
trast, the CI strategy is increasingly applied in a limited way, primarily in univariate models 
focused on temporal dependency.

Approaches to addressing recent MTS problems can be broadly categorized into three 
types. The first approach involves explicitly integrating modules for channel mixing into 
the  backbone  model.  Most  models  adopt  this  strategy,  aiming  to  maximize  effectiveness 
by explicitly incorporating channel correlation. However, as discussed earlier, distribution 
shifts in the dataset can potentially degrade the performance of the CD strategy, necessitat-
ing the introduction of appropriate alleviation methods. By employing this combination, the 
strengths of learning channel correlations can be applied more reliably, leading to enhanced 
model performance. The distribution shift alleviation methods will be discussed in detail in 
Sect. 5.2.

The second approach implicitly incorporates channel correlations into the input. Instead 
of  explicitly  integrating  channel  learning  modules  into  the  backbone  model,  this  method

---

<!-- PAGE 62 -->

216  Page 62 of 95

Fig. 15  Comparison of CI and CD strategies in channel correlations

takes a preprocessing approach by mixing channel information in advance to create a new 
input,  which  is  then  fed  into  the  prediction  model.  This  new  input  combines  the  mixed 
channel information with the original individual channel data before being processed by the 
prediction model. By inherently reflecting the relationships between channels, this method 
allows  even  a  simple  CI  backbone  to  achieve  the  effectiveness  of  a  more  complex  CD 
model.  Models  like  SOFTS  (Han  et  al  2024)  and  C-LoRA  (Nie  et  al  2024)  fall  into  this 
category.

The third approach adaptively selects between the CI and CD strategies. The model is 
designed to operate in both directions, allowing it to choose the most effective strategy based 
on the characteristics of the dataset being used. In some cases, like TSMixer (Ekambaram 
et al 2023), the user can manually select the appropriate strategy, while in others, such as Bi-
Mamba+ (Liang et al 2024a), the model automatically determines the optimal strategy. The 
second and third approaches both utilize the CI strategy alongside the CD strategy, aiming 
to integrate the advantages of both into the model. A summary of the criteria for selecting 
these strategies is presented in Fig. 16

In  the  past,  the  criteria  for  selecting  channel  strategies  were  ambiguous,  but  recent 
research has provided clear guidelines. Based on these advancements, users can now choose 
the appropriate channel strategy according to the characteristics of their dataset, effectively 
improving model performance through various approaches.

5.2  Alleviation of distribution shift

Many real-world time series data exhibit non-stationarity, where their distribution gradu-
ally changes. For instance, trends such as increasing electricity consumption and shifts in

---

<!-- PAGE 63 -->

Page 63 of 95  216

Fig. 16  Recent approaches to channel strategies

consumer preferences can lead to changes in data distribution. This non-stationarity intro-
duces challenges for the generalization of time series forecasting (TSF) models by creating 
distribution discrepancies within the training data and between the training and test data. To 
mitigate the issue of distribution shift caused by non-stationarity in time series forecasting, 
various research efforts have been proposed.

Representative  approaches  for  addressing  distribution  shifts  include  Domain Adapta-
tion, Transfer Learning, and Robustness Techniques. Domain Adaptation aims to reduce the 
distribution differences between the source and target domains to improve generalization 
performance across domains. This approach is divided into supervised domain adaptation, 
which uses some labeled data from the target domain, and unsupervised domain adaptation 
which  aligns  feature  distributions  using  unlabeled  datasets.  Unsupervised  domain  adap-
tation  began  with  the  introduction  of  Maximum  Mean  Discrepancy  (MMD)  (Wang  et  al 
2023a) -based methods and advanced with the emergence of Generative Adversarial Net-
works (GANs) (Sankaranarayanan et al 2018), which led to the development of adversarial 
domain adaptation techniques. Transfer Learning (Pan and Yang 2009) refers to applying a 
model trained in one domain or task to a new dataset. This includes Feature Transfer, which 
reuses or retrains specific layers of a pre-trained network for a new task, and Fine-Tuning 
which adjusts the entire pre-trained model to fit the new dataset. Transfer learning originated 
from pre-trained embeddings in NLP in the late 1990s, expanded through CNNs, and even-
tually evolved with LLMs. Robustness Techniques enhance a model’s ability to maintain 
performance despite data uncertainties, such as noise, outliers, and data scarcity. Methods 
such as Dropout (Srivastava et al 2014) and Data Augmentation (Wong et al 2016) help 
models handle noise, while robust loss functions like the Huber loss (Huber 1992) reduce 
sensitivity to outliers. These techniques have been widely adopted in time series forecasting 
models since 2020.

This survey focuses on one prominent approach that introduces normalization and denor-
malization modules  within  a  normalization-TSF model-denormalization framework. This

---

<!-- PAGE 64 -->

216  Page 64 of 95

framework has evolved as a specialized approach for mitigating non-stationarity within the 
same domain of time series data. Here, normalization is applied to the look-back window 
before  feeding  it  into  the  TSF  model,  aiming  to  remove  input  statistics. As  a  result,  the 
TSF model processes inputs from a less time-variant distribution. Denormalization is then 
applied  to  the  forecasting  window  obtained  from  the  TSF  model  to  restore  the  original 
statistics.  The  denormalized  forecasting  window  is  ultimately  used  as  the  final  forecast. 
However,  calculating  the  appropriate  statistics  for  normalization  and  denormalization  in 
non-stationary  scenarios  is  a  non-trivial  task,  and  numerous  studies  have  been  proposed 
within this framework to address this challenge (Table 11).

DAIN (Passalis et al 2019) introduces a Deep Adaptive Input Normalization layer that 
learns how much to shift and scale each observation end-to-end. Considering the chang-
ing distribution characteristics of time series data, this approach outperforms widely used 
normalization methods like batch normalization (Ioffe and Szegedy 2015) and instance nor-
malization  (Ulyanov  et  al  2016)  across  various  domains,  highlighting  the  importance  of 
normalization techniques in TSF. However, DAIN omits a denormalization step, meaning 
it does not account for restoring statistics in the forecasting results. In contrast, RevIN (Kim 
et al 2021), which extends instance normalization to be reversible, adopts a normalization-
denormalization  framework.  RevIN  performs  instance  normalization  on  each  look-back 
window, followed by variable-wise multiplication of a learnable scale factor and addition of 
a bias factor. During de-normalization, the same parameters are applied in reverse. NST (Liu 
et al 2022) normalizes the look-back window in a non-parametric manner without a learn-
able affine transformation and then de-normalizes the prediction window using the mean 
and standard deviation of the look-back window. Dish-TS (Fan et al 2023) learns a mod-
ule that predicts the statistics of the prediction window, considering the distribution shift 
between the look-back window and subsequent prediction windows, and performs normal-
ization and de-normalization accordingly. SAN (Liu et al 2024e) considers the distribution

Table 11  Normalization-denor-
malization-based approaches to 
alleviate distribution shifts in 
time series forecasting

Model name

Main improvement and methodology

DAIN

RevIN

NST

Dish-TS

SAN

⋅ Introduce adaptive normalization
⋅ Adaptive scaling, shift, and gating layers 
to normalize look-back window
⋅ Introduce normalization-denormalization 
framework
⋅ Denormalize prediction with reversible 
affine transformation parameters
⋅ Non-parametric 
normalization-denormalization
⋅ Normalize and denormalize using mean 
and std of look-back window without 
learnable parameters
⋅ Divides distribution shifts: (1) within 
look-back window and (2) between look-
back window and forecasting window
⋅ Introduce Dual-CONET modules for 
statistics prediction
⋅ Predict statistics in slice-level
⋅ Slice forecasting windows and predict 
mean and std for each slice

Publi-
cation
2019

2022

2022

2023

2023

---

<!-- PAGE 65 -->

Page 65 of 95  216

shift within both the look-back window and prediction windows, performing statistical pre-
diction on smaller slices.

5.3  Enhancing causality

Why causal analysis is essential for accurate time series forecasting

Causal analysis is crucial in achieving accurate time series forecasting by better under-
standing the underlying factors driving data patterns. Time series data often exhibit correla-
tions that can be misleading without a proper understanding of causality. For instance, two 
variables may show a strong correlation simply due to coincidence or because they are both 
influenced by a third, unobserved variable. Without distinguishing between correlation and 
causation, forecasting models risk attributing changes in the data to irrelevant or spurious 
factors, leading to inaccurate predictions. Causal analysis helps overcome this by identify-
ing the true cause-and-effect relationships, ensuring the model is grounded in reality rather 
than coincidental patterns.

Moreover, causal analysis enhances the interpretability and practical application of fore-
casting models. By explaining how different variables influence the outcome, causal models 
uncover the underlying mechanisms driving the forecast, which is crucial for decision-mak-
ing. Businesses and policymakers can use these insights to predict the impact of specific 
actions, such as policy changes or marketing strategies, and make informed decisions based 
on the likely effects. This ability to simulate interventions and conduct counterfactual sce-
narios makes causal analysis an indispensable tool for accurate and actionable time series 
forecasting.
Research on TSF with causality

As  mentioned  earlier,  utilizing  causality  in  time  series  forecasting  not  only  improves 
prediction  accuracy  but  also  enhances  model  interpretability.  For  these  reasons,  research 
applying causal discovery information to time series forecasting models is actively ongo-
ing. In particular, various methodologies have been proposed in fields such as healthcare, 
environmental science, and social sciences, where causal discovery is actively researched.
In TSF, various causal inference methods are employed to identify cause-and-effect rela-
tionships within the data. The Granger Causality Test (Granger 1969) examines whether 
the historical information of one variable helps predict the future of another variable. This 
method detects the direction of causal influence based on regression analysis. However, it 
has limitations in fully excluding indirect correlations caused by the presence of a third vari-
able. Structural Causal Models (SCM) (Pearl et al 2000) utilize causal graphs and structural 
equations to model the relationships between variables. These models enable intervention 
simulations and counterfactual analyses, providing a visual representation of causal relation-
ships to aid interpretation and integrate interactions across multiple variables. Do-Calculus 
(Pearl 1995) is an intervention analysis technique for quantitatively analyzing the effects 
of interventions by computing the impact that changes in specific variables have on others, 
thereby supporting causal predictions. Propensity Score Matching (PSM) (Rosenbaum and 
Rubin 1983) is a method for performing causal inference by matching groups with similar 
characteristics. This approach minimizes the influence of confounders and more accurately 
evaluates  the  effects  of  interventions.  Directed  Acyclic  Graphs  (DAGs)  (Pearl  1998)  are 
directional, non-cyclic graphs that visually represent the relationships between causes and 
effects. DAGs help clearly identify causal structures and understand complex interactions

---

<!-- PAGE 66 -->

216  Page 66 of 95

among variables. Various attempts are being made to enhance the causality of TSF by utiliz-
ing these diverse causal inference methods (Runge et al 2019; Schölkopf et al 2021).

Qian  et  al  (2023)  introduce  a  model  to  predict  Kuroshio  Volume  Transport  (KVT). 
It  employs  multivariate  causal  analysis  to  discover  causal  relationships  and  selects  only 
the  variables  with  causal  relationships  to  make  predictions  using  an  LSTM  model.  This 
approach captures meaningful information from causally related variables and prevents the 
model from being confused by unrelated variables. Mu et al (2023) propose a model for 
predicting the North Atlantic Oscillation. It uses information obtained through causal dis-
covery not only for variable selection but also by directly applying it to a GCN (Graph Con-
volutional Network). The overall structure utilizes a symmetrical encoder and decoder of 
ConvLSTM, with the GCN acting as a coupler in between. Sharma et al (2022) focuses on a 
model for energy consumption. It applies the Granger causality test to determine the causal 
relationship between weather conditions and energy consumption and then integrates this 
causal information into a Bi-LSTM to improve energy consumption prediction accuracy. 
CausalGNN (Wang et al 2022b) is a model aimed at epidemic forecasting. It extracts causal 
features  using  the  SIRD  model  and  incorporates  them  into  an Attention-Based  Dynamic 
GNN  module  to  learn  spatio-temporal  patterns.  Caformer  (Zhang  et  al  2024b)  criticizes 
existing methods for failing to learn causal relationships effectively due to false correlations 
caused by environmental factors. To address this, it explicitly models environmental influ-
ences and removes them to obtain reliable causal relationships.

5.4  Time series feature extraction

Time Series Feature Extraction is the process of extracting useful information from time 
series data to enhance model performance. In other words, it involves identifying and quan-
tifying time series data into key patterns, trends, seasonality, outliers, periodicity, and sta-
tistical characteristics to transform it into a form that is suitable for model training. This 
process clarifies the unique patterns or characteristics of time series data, allowing models to 
learn them more effectively. This enhances the understanding of data, improves the predic-
tive performance of models, and increases efficiency through data compression. The reasons 
why Time Series Feature Extraction is necessary are as follows:

● Understanding the characteristics of data Time series data, which is ordered sequen-
tially over time, possesses unique characteristics such as various patterns, seasonality, 
and periodicity. However, these data are complex and high-dimensional, making these 
features not easily apparent. The continuous values in time series data tend to be similar 
to adjacent values, which makes it challenging to accurately distinguish the context and 
meaning of each data point, often resulting in a lack of semantic information. Therefore, 
the process of transforming time series data into an analyzable format and extracting 
key features is crucial for understanding the inherent behaviors and interactions within 
the data.

● Explainability of data Unlike traditional machine learning methods, deep learning mod-
els automatically learn useful features from data without requiring manual feature ex-
traction. However, due to the nonlinear structure of deep learning models, it is often 
difficult for humans to interpret the learned features. The extracted features can better 
explain the structural characteristics of the data, helping to interpret and understand its

---

<!-- PAGE 67 -->

Page 67 of 95  216

meaning. This process provides critical insights for making data-driven decisions and 
contributes to improving explainability in complex model architectures.

● Enhancing Model Performance By summarizing complex time series data and remov-
ing noise, it emphasizes the essential signals of the data, reducing the computational 
burden  on  models  and  improving  predictive  performance.  Focusing  on  critical  infor-
mation  allows  the  model  to  avoid  overfitting  to  the  training  data  and  develop  strong 
generalization capabilities.

Decomposing or transforming time series data into different forms before feeding it into the 
model is a widely used and researched approach for feature extraction. These approaches 
help the model focus on learning the critical information in the data, thereby reducing sen-
sitivity  to  noise  and  overfitting.  These  methods  are  not  limited  to  specific  architectures 
and can be applied across various models. Figure 17 presents the key techniques for time 
series feature extraction, followed by an explanation of related application models for these 
approaches.

Fig. 17  Key techniques in time series feature extraction

---

<!-- PAGE 68 -->

216  Page 68 of 95

5.4.1  Decomposition

Time series decomposition has long been used as a fundamental time series feature extrac-
tion technique, which involves separating time series data into components such as trend, 
seasonality, periodicity, and residual. The advantage of decomposition is that it simplifies 
complex  time  series  data  by  breaking  it  down  into  understandable,  independent  compo-
nents, enabling more accurate model predictions and easier analysis and interpretation.
Moving average kernel

Many models apply a Moving Average kernel to the input sequence to separate trend and 
seasonality  components.  In  this  process,  high-frequency  noise  or  short-term  fluctuations 
are removed, allowing long-term trends to be more clearly captured and overall patterns of 
increase and decrease to be emphasized. The method of using a Moving Average Kernel is 
widely adopted due to its computational simplicity and efficiency. However, it has limita-
tions when dealing with complex nonlinear patterns.

Autoformer (Wu et al 2021) goes beyond using decomposition techniques merely as pre-
processing for forecasting tasks by progressively decomposing time series data throughout 
the prediction process within the model itself. Similarly, CrossWaveNet (Huang et al 2024b) 
employs  a  dual-channel  network  to  perform  gradual  deep  cross-decomposition,  enabling 
it to capture complex temporal patterns effectively. Likewise, models such as FEDformer 
(Zhou et al 2022), LTSF-Linear (Zeng et al 2023), and PDMLP (Tang and Zhang 2024) 
utilize a moving average kernel to individually model each component of the time series 
data, which are then recombined to make effective predictions. However, the Moving Aver-
age method lacks robustness because it is not learnable by the model. Additionally, since it 
assigns equal weights to each data point within the sliding window, it has limited ability to 
identify specific patterns. To address these limitations, Leddam (Yu et al 2024) use learn-
able 1D convolutional kernels, which can better capture nonlinear structures and dynamic 
variations.  Meanwhile,  diffusion-based  models  face  challenges  as  components  like  trend 
and  seasonality  can  easily  collapse  during  the  diffusion  process.  Diffusion-TS  (Yuan  and 
Qiao 2024) overcomes this by applying the diffusion process after decomposition, thereby 
preserving the characteristics of each component more effectively. Through this approach, 
the traditional limitations of time series decomposition are overcome, allowing for a more 
effective separation of trend and seasonal components.
Downsampling

The technique of using downsampling for decomposition is also frequently employed. 
Originating from signal processing, downsampling involves reducing the number of sam-
ples from the original signal, effectively decreasing the data by a specific ratio. Time series 
forecasting  is  typically  achieved  through  pooling  methods,  where  representative  values 
are extracted from specific segments of the time series data, thereby suppressing high-fre-
quency components and emphasizing low-frequency components. By adjusting the pooling 
size, various downsampling levels can be achieved, allowing for the exploration of multiple 
patterns within the data.

SparseTSF (Lin et al 2024b) and SutraNets (Bergsma et al 2023) use downsampling to 
separate data into trend and periodic components, predicting each subseries independently. 
This allows the model to learn each component separately and better understand the influ-
ence of each on the complex time series data, enhancing prediction accuracy. By dividing the 
complex time series data into various sub-series, it can be decomposed into a simpler form,

---

<!-- PAGE 69 -->

Page 69 of 95  216

thereby reducing the overall complexity of the model. Therefore, this approach enhances the 
model’s generalization ability and helps prevent overfitting.
Non-linear methods

While Moving Average Kernel and Downsampling are linear methods, Empirical Mode 
Decomposition (EMD) (Huang et al 1998) is a non-linear and non-stationary signal analy-
sis technique that decomposes time series data into a number of Intrinsic Mode Functions 
(IMFs). EMD involves finding local extrema in the signal and using linear interpolation for 
the upper and lower envelopes, and by subtracting their average, it extracts high-frequency 
components as IMFs iteratively. The final residual signal, also known as the residue, reveals 
the  long-term  trend.  EMD  is  advantageous  for  processing  non-linear  and  non-stationary 
time series data due to its adaptive nature, effectively separating and analyzing complex pat-
terns and changes in the time series. EMD-BI-LSTM (Mounir et al 2023) proposes a method 
that combines EMD with a conventional Bi-LSTM model for forecasting electric load time 
series data. By applying EMD, the model effectively captures complex non-linear relation-
ships, thereby enhancing forecasting performance.

However, EMD has a mode mixing problem, where signals of different frequencies are 
mixed within the same IMF (Xu et al 2019). In the signal decomposition process of EMD, 
IMF is generated based on local extrema, which causes difficulties in independently sepa-
rating components for signals with sudden changes, such as intermittent signals. This leads 
to  a  failure  in  frequency  separation,  which  not  only  reduces  prediction  performance  but 
also impairs interpretability. Ensemble Empirical Mode Decomposition (EEMD) (Wu and 
Huang 2009) addresses this mode mixing problem by adding noise to the original signal and 
repeating the decomposition process, averaging the results. Through this process, signals 
with different scales are properly aligned into the correct IMFs. Through successive itera-
tions, the influence of the noise is reduced, and the components of the original signal are 
emphasized, providing more physically meaningful results and enabling more accurate and 
stable time series decomposition. Yang and Yang (2020) proposes models applying EEMD 
to LSTM, linear regression, and Bayesian ridge regression for forecasting.

Variational Mode Decomposition (VMD) (Dragomiretskiy and Zosso 2013) is a method 
that  uses  variational  optimization  to  separate  signals  into  modes  with  specific  frequency 
bands.  Each  mode’s  frequency  center  and  bandwidth  are  determined  through  variational 
optimization. As the frequency ranges do not overlap, the separation is clearer and more 
stable. However, compared to EMD, which requires relatively simple calculations, VMD is 
computationally more complex due to its use of variational optimization. Peng et al (2023) 
proposes a new model for crude oil price forecasting that applies VMD. By decomposing 
the time series data with VMD, transforming it into images, and extracting features with 
CNN, this method improves forecasting performance for oil prices. It effectively utilizes 
the  advantages  of VMD  by  making  predictions  with  Bidirectional  Gated  Recurrent  Unit 
(BGRU).

Various  decomposition  methods  are  widely  used  in  time  series  forecasting.  However, 
decomposition methods also have some drawbacks. When the data is divided into separate 
components based on different rules, the model predicts each component independently. As 
a result, important interactions or relationships may not be considered, which can lead to 
underutilization of necessary information for prediction and degrade performance. Never-
theless, considering the characteristics of time series, such as periodicity, trends, and noise, 
decomposition remains a powerful technique. Moreover, since time series data is more dif-

---

<!-- PAGE 70 -->

216  Page 70 of 95

ficult to intuitively interpret compared to other data types, decomposition provides interpret-
ability, which helps increase the model’s trustworthiness.

5.4.2  Multi-scale

The multi-scale approach analyzes data at various time scales, capturing patterns and trends 
at multiple levels simultaneously. This method is beneficial not only for time series data but 
also in fields like computer vision and natural language processing (Fan et al 2021; Nawrot 
et al 2021). By integrating information from longer time frames, the multi-scale approach 
plays a significant role in improving performance in time series forecasting.

MTST  (Zhang  et  al  2024e),  PDMLP  (Tang  and  Zhang  2024),  and  FTMixer  (Li  et  al 
2024d) extend the patching application to a multi-scale framework, where shorter patches 
effectively learn high-frequency patterns and longer patches capture long-term trends. Time-
Mixer (Wang et al 2024a) and AMD (Hu et al 2024b) leverage multi-scale decomposition 
to capitalize on the strengths of each scale, enabling the model to make more accurate pre-
dictions. HD-TTS (Marisca et al 2024) uses spatiotemporal downsampling to decompose 
data into various scales across both time and space. Scaleformer (Shabani et al 2023) and 
Pathformer (Chen et al 2024b) apply the multi-scale concept to the overall model architec-
ture, while HD-TTS hierarchically implements temporal and spatial downsampling. MG-
TSD (Fan et al 2024b) and mr-Diff (Shen et al 2024) successfully integrate multi-scale by 
incorporating inductive biases that prioritize generating coarse data in the early stages of the 
diffusion reverse process.

5.4.3  Domain transformation

A common method for enhancing the expression of latent periodic features in time series 
data is to transform the data into the frequency domain. Techniques such as Fourier trans-
formation, Wavelet transformation, and Cosine transformation are commonly used for this 
purpose. Generally, time series data exhibits periodicity, which refers to patterns that repeat 
at regular intervals. Frequency transformations effectively explore this periodicity. In time 
series analysis, frequency transformations are used with two main approaches: extracting 
periodic components and direct learning in the frequency domain.
Periodicity extraction

Periodicity in time series data serves as critical information for predictive models, where 
features that may be hidden in the time domain can be more easily uncovered in the fre-
quency domain. Frequency transformations are advantageous because they can remove high-
frequency noise while retaining important low-frequency components, thereby improving 
data quality. By selectively extracting key frequency components and feeding them into the 
model, the process helps in learning essential patterns, enhances computational efficiency, 
and reduces model complexity. Some models leverage these characteristics to identify and 
extract various periodic patterns in the data. These adaptively extracted patterns are used 
either as inputs for the model or integrated into the learning process, thereby enhancing the 
model’s predictive performance.

Autoformer (Wu et al 2021) utilizes periodicity extracted through auto-correlation within 
the Attention mechanism. TimesNet (Wu et al 2023) transforms periodic components into a 
2D format to train the time series with CNNs. MSGNet (Cai et al 2024a) uses periodic com-

---

<!-- PAGE 71 -->

Page 71 of 95  216

ponents to allow the model to determine appropriate scale levels for multi-scale analysis 
autonomously. However, since the periodicity extracted in this manner is based on selective 
sampling, it does not encompass all the latent information, and if critical information is not 
selected, performance degradation becomes inevitable.
Training in the frequency domain

The approach of directly training models in the frequency domain is widely studied as 
it overcomes these limitations by evenly learning all latent frequency components, ensur-
ing that critical information is not missed. While time series data can exhibit complex and 
varied patterns in the time domain, these patterns can often be succinctly represented by a 
few dominant frequency components when transformed into the frequency domain (Zhou 
et al 2022). This simplification makes the learning process more straightforward, as most of 
the information can be captured with a minimal set of frequency components. This method 
allows for an easy transition to the frequency domain while preserving the original informa-
tion, thanks to various transformation and inverse transformation techniques. When time 
series  data  exhibit  nonlinear  characteristics,  learning  in  the  frequency  domain  can  better 
capture these complex patterns than in the time domain. The frequency domain approach 
doesn’t require consideration of time-axis variations, enabling stable performance even with 
non-stationary data. Furthermore, this method allows for efficient learning by compressing 
the data without losing important characteristics.

In the frequency domain, each frequency component is represented as a complex num-
ber, consisting of a real part and an imaginary part, each conveying different information. 
The real part is related to the magnitude (amplitude) of the time series data, indicating how 
prominent the periodic components are. The imaginary part, on the other hand, relates to 
the phase information of the data, determining the temporal positioning of the frequency 
components. By simultaneously understanding the amplitude and phase information in the 
frequency domain, models can accurately capture and predict complex periodic patterns in 
the data. The research initially focused on simply changing the domain, but more recently, it 
has been moving towards expanding the expressiveness of the frequency domain.

FreTS (Yi et al 2024) and Crabbé et al (2024) transform data into the frequency domain 
before feeding it into the model and then convert the predicted values back into the time 
domain. Simply converting data to the frequency domain has limitations in achieving good 
model performance, leading to the development of models that overcome these challenges. 
Research continues to expand the representation in the frequency domain to fully utilize 
its  rich  features.  FEDformer  (Zhou  et  al  2022)  applies  season-trend  decomposition  and 
then performs attention in the frequency domain, facilitating independent modeling of key 
information components. Fredformer (Piao et al 2024) not only transforms data into the fre-
quency domain but also investigates frequency bias through experiments, addressing issues 
in the frequency domain using frequency normalization techniques. FITS (Xu et al 2024c) 
utilizes distinct complex-valued linear layers in the frequency domain to learn amplitude 
scaling and phase changes, thereby enhancing the frequency representation of input time 
series through interpolation learning. DERITS (Fan et al 2024a) effectively handles the non-
stationarity of time series data by differentiating frequency components and representing 
them in a static form that is easier to predict. SiMBA (Patro and Agneeswaran 2024b) trans-
forms time series data into the frequency domain using Fourier transforms, learning real 
and imaginary components separately, thus allowing more precise analysis of data in the 
frequency  domain  and  improving  model  prediction  performance. While  frequency  bands

---

<!-- PAGE 72 -->

216  Page 72 of 95

capture  global  dependencies  well,  they  often  struggle  with  local  dependency  capture. To 
overcome this, WaveForM (Yang et al 2023a) uses discrete wavelet transforms (DWT) to 
decompose time series data into various frequency bands while preserving the time informa-
tion of each band. This approach captures frequency changes within specific time intervals, 
simultaneously capturing features from both time and frequency domains. FTMixer (Li et al 
2024d)  proposes  a  method  that  directly  utilizes  data  from  both  domains  to  leverage  the 
strengths of global dependency extraction in the frequency domain and local dependency 
extraction in the time domain.

5.4.4  Additional approach

In  addition  to  the  methods  previously  described,  various  other  approaches  have  been 
explored. A notable example is the use of High-Dimensional Embedding, which generates 
high-dimensional representations to better capture the essential information of the data. This 
approach extracts complex, multidimensional information from the original time series data 
and integrates it to enhance the model’s predictive capabilities. For instance, CATS (Lu et al 
2024) creates a new Auxiliary Time Series (ATS) by combining variables from the input 
data and then utilizes these for prediction. SOFTS (Han et al 2024) focuses on extracting 
common features (Core) from the variables and incorporating them into the learning pro-
cess.  Furthermore,  BSA  (Kang  et  al  2024)  enhances  feature  representation  by  leveraging 
temporal correlations between continuously streaming input samples, rather than depend-
ing  solely  on  a  single  current  input.  The  method  accumulates  multiple  scales  of  feature 
transformations over time via an exponential moving average (EMA), then applies Spectral 
Attention to these multi-scale momentums to capture long-range dependencies and enrich 
the resulting features.

Efforts to effectively represent the complex features of time series data for better model 
learning  are  being  explored  in  various  forms.  These  efforts  are  essential  research  topics 
for  improving  performance  in  the  challenging  field  of  time  series  forecasting. Addition-
ally,  integrating  these  feature  extraction  techniques  appropriately  within  the  basic  struc-
ture of existing deep learning models can create synergy, enhancing the model’s predictive 
accuracy.

5.4.5  Automated feature engineering and self-supervised learning

In  TSF,  extracting  meaningful  features  has  traditionally  required  domain  expertise  and 
extensive manual work. However, such approaches are often time-consuming and costly, 
and they may miss critical patterns when dealing with complex data. To address these chal-
lenges, automated feature engineering has become increasingly important for automatically 
identifying key patterns in the data. One of the core techniques for automated feature engi-
neering is self-supervised learning (Zhang et al 2024a).

Self-supervised learning is a pretraining approach that enables models to automatically 
learn important features from unlabeled datasets by identifying patterns directly from the 
data itself. This allows the model to capture structural patterns without relying on manual 
feature extraction, reducing the dependency on labeled data. Key approaches in self-super-
vised learning for TSF are as follows. Transformation-based approach learns key features 
by comparing patterns before and after data transformations, such as time shifts and scaling.

---

<!-- PAGE 73 -->

Page 73 of 95  216

For example, TS-TCC (Eldele et al 2021) enhances features by applying various transforma-
tions and learning the pattern similarities between the transformed data. Time Correlation 
Learning extracts temporal dependencies in time series data by learning the relationships 
between past and future time points. Contrastive Predictive Coding (CPC) (Oord et al 2018) 
divides the data into multiple time segments and learns the correlations between these seg-
ments. Mask-based Learning involves masking specific time points in the time series data 
and predicting these masked points based on the remaining data to learn key patterns (Wang 
et al 2022a). The application of such self-supervised learning approaches can enhance the 
performance of TSF (Xu et al 2022; Wu et al 2023).

Self-supervised learning enables models to automatically recognize and extract key pat-
terns  and  nonlinear  relationships  from  data  without  labeled  examples.  It  can  effectively 
learn from small datasets, addressing the issue of label scarcity and contributing to model 
lightweight  and  algorithm  optimization.  In  particular,  multimodal  self-supervised  learn-
ing techniques, which integrate time series data with other data types such as images and 
text, are expected to advance, enabling the model to learn richer patterns. Such multimodal 
learning can significantly contribute to solving complex decision-making problems, such 
as healthcare diagnostics and disaster prediction. Additionally, research on converting the 
learned  features  into  interpretable  forms  will  become  increasingly  important.  This  will 
enhance the interpretability and reliability of the model and improve trust in data-driven 
decision-making processes.

In  conclusion,  self-supervised  learning-based  automated  feature  engineering  is  a  piv-
otal  research  area  for  effectively  understanding  complex  patterns  in  time  series  data  and 
enhancing predictive performance. Research combining this approach with data efficiency 
improvements,  multimodal  learning,  and  explainable  AI  (XAI)  is  expected  to  further 
increase the practicality and reliability of TSF.

5.5  Model combination techniques

The instability of single models in time series forecasting has been a persistent challenge 
from the past to the present. Due to the complexity, volatility, and distinguishing charac-
teristics of time series data, the use of a single model can lead to overfitting and unstable 
forecasting performance. Therefore, methods for combining models offer a simple yet effec-
tive approach to overcome these issues. Model combination techniques reduce forecasting 
uncertainty  and  enable  more  robust  predictions.  Makridakis  et  al  (2020)  experimentally 
demonstrates  that  model  combination,  as  applied  in  the  M4  Competition  task,  improves 
forecast  accuracy  over  single  models  or  model  selection.  However,  Model  combination 
techniques can face issues such as model redundancy, increased computational costs, and 
reduced interpretability due to the complexity of the combined models. To maximize the 
combination effect, it is necessary to properly leverage model diversity or use sophisticated 
combination methods.

5.5.1  Ensemble models

Ensemble models combine the independent predictions of several models to complement 
the weaknesses of individual models and generate a final forecast. Ganaie et al (2022) sum-
marizes the theoretical aspects of ensemble learning’s success based on existing research,

---

<!-- PAGE 74 -->

216  Page 74 of 95

Fig. 18  BKey ensemble techniques

arguing that combining predictions from multiple models is an effective way to improve 
model performance. This section explores key ensemble methods, including bagging, boost-
ing, and stacking, as illustrated in Fig. 18.

Bootstrap Aggregating (Bagging) involves randomly sampling the data to train several 
independent models and then combining their results through averaging or voting (Breiman 
1996). Petropoulos et al (2018) explains why bagging is effective for time series forecasting 
by  addressing  data  uncertainty,  model  uncertainty,  and  parameter  uncertainty,  improving 
forecasting performance. Kim and Baek (2022) combines Wavelet transforms with bagging 
techniques in MLP to improve univariate time series forecasting performance. Using the 
Maximum Overlap Discrete Wavelet Transform (MODWT) (Nason et al 2000), the signal 
is decomposed, and bagging is applied only to the detail part, excluding trends. This creates 
data diversity by preserving the main trend while altering the detailed fluctuations.

Boosting overcomes the issue of model diversity by sequential training and combining 
weak learners (Freund and Schapire 1997). This approach addresses the diversity problem 
that can arise in bagging when each model is trained in a very similar manner. Each model 
places more weight on the data that was incorrectly predicted by the previous models, aim-
ing to reduce bias. This creates a strong learner by combining weak learners and ensures 
added diversity. Gradient boosting is an algorithm that optimizes models using the gradient 
of the loss function within the boosting framework (Friedman 2001). XGBoost (eXtreme 
Gradient  Boosting)  executes  the  gradient  boosting  algorithm  in  parallel,  making  it  faster 
and more effective in handling sparse data while improving learning speed and predictive 
performance  (Chen  and  Guestrin  2016).  In  the  2015  Kaggle  (https://www.kaggle.com) 
machine  learning  competition, 17  out  of  29  winning  solutions  used  XGBoost  (Chen  and 
Guestrin 2016). As deep learning advanced, various works combining DL with XGBoost 
emerged.  LightGBM  (Ke  et  al  2017)  is  a  boosting-based  algorithm  with  a  leaf-wise  tree

---

<!-- PAGE 75 -->

Page 75 of 95  216

splitting method, and Sui et al (2024) uses an ensemble approach that combines traditional 
and advanced methods for stock prediction. Specifically, the integration of LSTM, GRU, 
LR, and LightGBM models enhances forecasting performance. However, boosting is gen-
erally not applied to deep learning models, as boosting typically uses simple weak learn-
ers  that  are  repeatedly  trained  to  improve  performance.  Deep  learning  models  like  MLP 
already learn complex patterns effectively with large amounts of data, so the need for itera-
tive error correction is minimal. Thus, simpler machine learning methods are typically used 
to construct weak learners instead of deep neural networks. Truchan et al (2024) proposes 
predicting trends using linear models and then applying boosting to the residuals with tree-
based models for forecasting. This model combines the simple trend estimation capability 
of linear models with the nonlinear pattern learning ability of tree-based models, achieving 
more precise and effective predictions in LTSF. However, there is also a case where boosting 
principles are applied to deep learning models, such as Liang et al (2024b), which integrates 
boosting’s progressive residual learning approach into deep learning to enhance time series 
forecasting.

Stacking combines the predictions of several models to generate a final forecast (Wolp-
ert 1992). Stacked Generalization involves training several base learners, and then feeding 
their prediction results into a meta-model to generate the final prediction. Unlike bagging 
and boosting, stacking does not directly combine the predictions of the models; instead, it 
inputs the prediction results into a new model to make the final forecast. Stacking is dis-
tinctive in that it incorporates model weightings and analysis, enabling more refined and 
comprehensive predictions (Sharma et al 2021). Massaoudi et al (2021) suggests stacking 
LightGBM and eXtreme Gradient Boosting (XGB) to tackle stochastic variations in short-
term load forecasting, where the meta data generated by both models is input to an MLP for 
the final prediction. Furthermore, the use of MLP as a meta-model instead of traditional ML 
models like linear regression enables the learning of more complex, nonlinear relationships, 
improving prediction performance. The results demonstrate the model’s generalization abil-
ity and superior performance across various datasets. BStacking can be applied not only to 
deterministic forecasting but also to probabilistic forecasting, and some studies have shown 
that stacking is effective in handling uncertainty (Pavlyshenko 2020; Dudek 2024). Hasson 
et al (2023) explores the theoretical aspects of stacked generalization. Through cross-vali-
dation, it provides theoretical guarantees that the performance of a stacked generalization 
model selected through cross-validation does not fall significantly behind that of an oracle 
model, the best performing individual model. The paper also explains that extending the 
basic models used in stacking to learnable models, rather than constant models, provides 
better theoretical guarantees.

Ensemble models require significant training resources since each model must be trained 
independently.  Nevertheless,  ensemble  techniques  combine  diverse,  high-performance 
models to complement each other and can be implemented in a relatively simple manner. 
Due to these characteristics, ensemble learning can enhance prediction stability and gener-
alization capabilities in application fields, penetrating nearly all industries, from grain prod-
uct distribution, semiconductor manufacturing, and sensor design to commercial software 
development and testing services (Lin and Huang 2022).

---

<!-- PAGE 76 -->

216  Page 76 of 95

5.5.2  Hybrid models

Hybrid models combine different types of models or techniques to leverage the strengths of 
individual models while compensating for their weaknesses. These models employ a more 
sophisticated structural integration approach compared to ensembles, encompassing various 
strategies such as combining statistical models, machine learning models, and deep learning 
models.

ESRNN (Smyl 2020), a hybrid model that combines statistical models with deep learn-
ing architectures, integrates exponential smoothing (ES) and LSTM to leverage the inter-
pretability of statistical methods alongside the powerful nonlinear learning capabilities of 
deep learning. Through ES, the model effectively captures key components of individual 
time series, such as level, trend, and seasonality, while LSTM learns the correlations and 
nonlinear  patterns  across  multiple  time  series. Additionally,  the  use  of  dynamic  compu-
tation  graphs  and  a  hierarchical  design  provides  strong  performance  and  interpretability 
in real-world applications. This model highlights the potential of hybrid models for time 
series forecasting with its superior performance. BMoreover, AQ-ESRNN (Smyl et al 2024) 
model, an extension beyond deterministic forecasting to probabilistic forecasting, enables 
distributional  forecasting  by  quantifying  prediction  uncertainty.  Subsequently,  hybrid 
models combining deep learning architectures have advanced, and this section focuses on 
explaining such combinations of deep learning architectures.

Particularly,  time  series  data  often  involve  not  only  temporal  dependencies  but  also 
important interactions between variables. Therefore, many models explicitly learn the inter-
dependencies between variables in addition to temporal dependencies. However, incorpo-
rating all this information into a single architecture can lead to overfitting, which may limit 
the learning process. Recent models often combine two or more architectures to efficiently 
learn by distinguishing the roles based on the nature of the information.

WaveForM (Yang et al 2023a) improves prediction performance by transforming time 
series  data  into  the  wavelet  domain  and  combining  it  with  GNN.  The  Discrete  Wavelet 
Transformation (DWT) uses High-Pass and Low-Pass Filters to decompose the time series 
data into small wavelets. This process removes noise and allows CNN to efficiently cap-
ture temporal and frequency characteristics. The GNN is then used to model the interac-
tions between these components. TSLANet (Eldele et al 2024) is a model that replaces the 
computationally expensive attention mechanism with CNN in the Transformer framework. 
It incorporates frequency analysis and a learnable threshold to selectively attenuate high-
frequency noise, effectively learning long-term and short-term interactions. Additionally, it 
uses parallel convolution layers with different kernel sizes to capture both local patterns and 
long-term dependencies. This approach effectively compensates for the typical CNN’s limi-
tations in modeling long-term dependencies. DERITS (Fan et al 2024a) enhances the predic-
tion performance of non-stationary time series data by combining convolution operations 
in the frequency domain with MLP in the time domain. The Frequency Derivative Trans-
formation (FDT) converts time series signals into the frequency domain and then differenti-
ates the frequency components to represent them in a static form that is easier to predict. 
The  Order-adaptive  Fourier  Convolution  Network  (OFCN)  is  responsible  for  frequency 
filtering and learning dependencies in the frequency domain. To improve prediction perfor-
mance, it processes and fuses derivative information of various orders in parallel, utilizing 
a Parallel-stacked Architecture. BiTGraph (Chen et al 2024c) focuses on improving perfor-

---

<!-- PAGE 77 -->

Page 77 of 95  216

mance in situations with missing data by capturing both temporal dependencies and spatial 
structures. The Multi-Scale Instance Partial TCN module learns short-term and long-term 
dependencies through kernels of various sizes and can also compensate for missing values 
through partial TCN. The Biased GCN module for inter-channel relationship learning rep-
resents the relationships between data points as a graph structure and adjusts the strength 
of information propagation between nodes, considering the missing patterns. Zhang et al 
(2021a) proposes a hybrid model for wind speed forecasting. By performing decomposition 
using Singular Spectrum Analysis (SSA) and Multivariate Empirical Mode Decomposition 
(MEMD), the model removes noise and separates the trend and various frequency compo-
nents of the time series data, enabling more accurate forecasting. Then, by combining CNN 
with attention mechanism and Bidirectional Long Short-Term Memory, the model extracts 
spatial correlations and learns temporal dependencies, optimizing the wind speed forecast-
ing performance. Zhang et al (2021b) also uses both ensemble and hybrid models for TSF. 
The ensemble deep learning model, which combines various deep learning models such as 
CNN, MLP, and LSTM, demonstrates excellent performance in forecasting real-world time 
series data, including PM2.5 concentration, wind speed, and electricity prices. The model 
utilizes Extended AdaBoost (Freund and Schapire 1997) to generate diverse base predictors, 
followed by applying a stacking method to use Kernel Ridge Regression as a meta-predictor 
to produce the final forecast.

In  hybrid  models,  optimization  processes  such  as  hyperparameter  tuning,  regulariza-
tion techniques, and cross-validation can help reduce the risk of overfitting caused by the 
interdependence and complexity between multiple models. Additionally, evolutionary algo-
rithms can be used to explore and optimize model structures (Wei et al 2022). Hybrid mod-
els may increase training time and resource consumption, and they can have limitations in 
interpretability and maintenance. Therefore, techniques like model compression or feature 
selection can be applied, and model interpretability issues can be addressed using interpreta-
tion methods.

5.6  Interpretability and explainability

Although AI models exhibit outstanding performance, their black-box nature often under-
mines trust in decision-making processes (Xua and Yang 2024). In mission-critical domains, 
particularly  those  dealing  with  human  life  and  safety,  understanding  the  reasons  behind 
model decisions is crucial, which has led to restrictions on the use of deep learning models 
(Papapetrou and Lee 2024). The European Union, through the General Data Protection Reg-
ulation (GDPR), mandates the explanation of automated decisions, ensuring that individuals 
can understand the rationale behind decisions made by automated systems like AI models 
(Hamon et al 2022). As data-driven decision-making becomes more widespread, the need 
to understand how a model arrives at specific predictions and why such outcomes occur is 
growing (Lim and Zohren 2021).

Interpretability and explainability aim to ensure model understanding and transparency, 
making it possible to know how and why a model produces certain results. These two con-
cepts can be applied in various ways. For example, consumers might demand explanations 
when they notice anomalies in model outcomes, while AI researchers could use these con-
cepts  to  improve  model  performance.  Ultimately,  interpretability  and  explainability  pro-
mote not only research on AI models but also their expansion into various fields, enhancing

---

<!-- PAGE 78 -->

216  Page 78 of 95

performance and usability, which could drive fundamental changes in industries and soci-
etal paradigms (Han et al 2023a; Jung et al 2020; Kim et al 2020).

These concepts are particularly important in time series data, where interpretability helps 
in understanding how a model recognizes and predicts periodic and repetitive patterns. Fur-
thermore, explainability is necessary for anomaly detection models to clarify how anoma-
lies are detected and which features are abnormal, thereby aiding decision-making.

The  machine  learning  community  has  noted  that  there  is  no  universally  agreed-upon 
definition for the terms interpretability and explainability (Lipton 2018). Consequently, in 
various studies, these terms are often used interchangeably, even though they carry different 
meanings and are used differently across domains (Graziani et al 2023). To avoid confu-
sion for our readers, we define and explain these terms as follows. Interpretability focuses 
on understanding the internal workings of a model, providing transparency about how the 
model makes predictions (ŞAHiN et al 2024). Interpretability requires an intuitive under-
standing of the model’s structure, feature selection, and prediction process. Explainability, 
on the other hand, is concerned with providing reasons for a model’s outputs in a way that 
humans can comprehend. It is a technical approach that helps make the decision-making 
process of the model more understandable. In summary, interpretability is about understand-
ing how the model works, while explainability is about providing understandable reasons 
for the model’s predictions.

5.6.1  Interpretability

Interpretability  can  be  achieved  through  the  following  representative  models.  Temporal 
Fusion Transformer (TFT) (Lim et al 2021) is a deep learning model for multi-horizon fore-
casting proposed by the Google Cloud AI team, which utilizes the attention mechanism to 
effectively learn the interactions between static and time-dependent input data. This model 
incorporates a static feature encoder, a variable selection gating mechanism, and interpre-
table weights, allowing the model to better capture the characteristics of time series data 
and significantly improve interpretability compared to a standard Transformer. The gating 
mechanism suppresses unnecessary inputs, enhancing model efficiency, while the static fea-
ture encoder converts static data into contextual vectors that are incorporated into predic-
tions. The following two models enhance the interpretability of the TFT model for wind 
speed prediction by applying a two-stage decomposition approach. Given the high volatility 
and multi-resolution modes of wind speed data, the decomposition technique described in 
Sect.  5.4.1  allows  for  the  independent  analysis  of  the  impact  of  each  component  on  the 
prediction  results,  thus  improving  interpretability.  EMD-EEMD-JADE-TFT  decomposes 
the  data  using  Empirical  Mode  Decomposition  (EMD)  and  Ensemble  Empirical  Mode 
Decomposition  (EEMD)  and  optimizes  the  TFT’s  hyperparameters  using  Adaptive  Dif-
ferential Evolution with optional external archive (JADE) (Wu and Wang 2024). IEEMD-
EWT-JADE-TFT model, on the other hand, uses Improved Complete Ensemble Empirical 
Mode  Decomposition  with Adaptive  Noise  (IEEMD)  and  Empirical  Wavelet  Transform 
(EWT) for decomposition, and similarly optimizes TFT hyperparameters with JADE (Wu 
et al 2024a). Additionally, meteorological feature engineering combines statistical features 
to enhance both performance and interpretability.

---

<!-- PAGE 79 -->

Page 79 of 95  216

5.6.2  Explainability

Different methodologies exist for models focused on explainability. Simple machine learn-
ing models, such as Linear Regression or Decision Trees, are transparent and provide an 
intuitive understanding of predictions by themselves. These models have intrinsic explain-
ability, which falls under ante-hoc explainability, meaning their predictions can be easily 
explained from the design stage. On the other hand, deep learning models are highly com-
plex and learn high-dimensional features, making it difficult to achieve intrinsic explainabil-
ity through simple aggregation methods. Therefore, post-hoc explainability techniques are 
primarily used for deep learning models. Post-hoc explainability refers to approaches that 
interpret and explain the prediction or decision-making process after the model has already 
been trained. Post-hoc interpretability can be divided into several subcategories.

Surrogate models are used to explain the predictions of complex models by training a 
simpler, interpretable model to explain the predictions. Local Interpretable Model-Agnostic 
Explanations (LIME) is a representative surrogate model that provides local explanations 
for individual predictions (Ribeiro et al 2016). LIME works by generating perturbated sam-
ple data around a data point and obtaining predictions from the black-box model. Based on 
this, a simple linear model is trained to identify the important features in that prediction. 
Yang et al (2023b) proposes an improved LIME algorithm to address the interpretability 
issues of black-box models in wind power forecasting and applies it to a wind power predic-
tion model. This model introduces a trust index to quantify how reliable the features used by 
the prediction model are and analyzes how the black-box model handles important features 
in the prediction. Additionally, this model proposes global trust modeling and interpretable 
feature  selection  methods,  demonstrating  that  these  approaches  can  enhance  the  model’s 
reliability and reduce prediction errors.

Feature attribution is a method that calculates how much each input feature contributed 
to  the  model’s  prediction  and  evaluates  the  contribution  of  input  features  for  a  specific 
prediction.  SHapley Additive  exPlanations  (SHAP)  is  a  representative  feature  attribution 
technique based on the Shapley value concept from game theory (Lundberg and Lee 2017). 
SHAP fairly measures the contribution of each feature to model predictions. SHAP visu-
alizes the importance of features from both global and local perspectives and helps iden-
tify interactions between model predictions and features. The key idea behind SHAP is to 
compute the average contribution of each feature across all possible feature combinations, 
which allows the decomposition of predictions into feature contributions, providing intui-
tive and interpretable results. García and Aznarte (2020) uses an LSTM model to predict 
NO2 concentrations and presents a method for interpreting the prediction results based on 
SHAP. While SHAP values are typically applied to linear models, this study extends SHAP 
by  applying  Deep  SHAP  to  accommodate  the  nonlinear  characteristics  of  deep  learning 
models, making it easier to understand the complex decision-making process of deep learn-
ing models (Chen et al 2022).

Counterfactual explanations describe what inputs need to be altered to change a specific 
prediction (Wachter et al 2017). Counterfactual explanations generate counterfactual inputs 
that  would  alter  the  prediction.  In  time  series  research,  counterfactual  explanations  have 
been  widely  used  in  classification  tasks,  but  their  application  to  forecasting  models  has 
been  relatively  underexplored  (Wang  et  al  2023b).  In  time  series  forecasting,  exogenous 
variables make predictions more complex, which highlights the importance of setting range

---

<!-- PAGE 80 -->

216  Page 80 of 95

constraints (Papapetrou and Lee 2024). ForecastCF is a model that generates counterfactual 
explanations to explain the predictions of time series forecasting models (Wang et al 2023b). 
This model modifies the time series data through gradient-based perturbation to ensure the 
model’s predictions fall within a specified range, thus improving the model’s explainability. 
Specifically, users define the desired prediction range, and the model generates predictions 
that satisfy these constraints, making the predictions more intuitive and understandable.

5.7  Spatio-temporal time series forecasting

As the structure of time series data becomes increasingly complex, spatial information is 
now  frequently  incorporated  into  the  datasets.  Spatio-temporal  time  series  data  refers  to 
datasets that simultaneously capture temporal variations and spatial distributions. This type 
of data consists of values that change over time at specific locations, possessing both spatial 
interactions  and  temporal  dependencies.  Due  to  these  characteristics,  it  provides  critical 
information not only from patterns extracted along the time axis but also from spatial depen-
dencies caused by interactions between locations. For example, region-based traffic flow, air 
pollution levels, climate change, and electricity consumption are representative cases. The 
rapid advancements in technologies such as satellite data and GPS have led to an explo-
sive increase in location-based data. Therefore, spatio-temporal data modeling has become 
increasingly  important,  as  many  real-world  problems  cannot  be  adequately  explained  by 
temporal variations alone (Sun et al 2024a). Conventional multivariate time series models 
often fail to adequately address spatial correlations or network structures, necessitating their 
extension to spatio-temporal models. To address this, numerous approaches utilizing GNNs 
and Transformers have been actively explored (Jin et al 2023; Yang et al 2024a; Chen et al 
2021a; Park et al 2020).

Several representative approaches for handling spatio-temporal data are as follows. One 
is the Graph-Based Method for spatio-temporal modeling. Data is represented as a graph, 
where  spatial  relationships  between  locations  (nodes)  are  expressed  as  edges.  GCNs  or 
graph-based  RNNs  are  used  to  simultaneously  learn  spatial  and  temporal  dependencies. 
This  approach  effectively  models  non-euclidean  structured  data  but  has  drawbacks,  such 
as complex preprocessing and high computational costs. These approaches are well-suited 
for  applications  such  as  traffic  flow  prediction  by  modeling  road  networks  or  electricity 
demand forecasting by modeling connections between substations. DCRNN (Li et al 2018) 
models traffic networks as directed graphs using Diffusion Convolution, effectively captur-
ing  spatial  dependencies,  including  upstream  and  downstream  node  relationships.  It  also 
leverages GRU to capture temporal patterns and non-linearities, making it a representative 
graph-based model for handling complex time series data. ST-GCN (Yan et al 2018) mod-
els skeleton dataset as graphs and extends GCN along the temporal axis to simultaneously 
model spatial and temporal dependencies. DB-STGCN (Li et al 2024a) predicts train delays 
by integrating dynamic adjacency matrices generated through Dynamic Bayesian Networks 
(DBN) into ST-GCN to capture spatio-temporal dependencies. It improves prediction accu-
racy and interpretability through the integration of attention mechanisms and the combina-
tion of GCN and GRU.

Another approach is the raster-based method. Data is converted into a 2D grid (raster) or 
video format to learn spatial locations and temporal patterns. Grid-based data representa-
tion: A specific space is divided into grids, and data over time is collected for each grid cell.

---

<!-- PAGE 81 -->

Page 81 of 95  216

Video-based data representation: Data is transformed into a 3D tensor, including the time 
axis. This format allows easy application of image processing techniques, such as CNNs, 
and 3D CNNs are particularly effective for directly learning spatio-temporal patterns. How-
ever, there are limitations in learning overly complex spatial relationships. They are suit-
able for modeling climate data from satellite imagery or recognizing actions in video data 
through spatiotemporal dynamics. ConvLSTM (Shi et al 2015) replaces the fully connected 
state transitions of conventional LSTM with convolutions to learn spatial correlations, mak-
ing it a representative early raster-based method. It represents all inputs, hidden states, and 
cell states as 3D tensors to maintain the grid-like spatial structure. ST-ResNet (Zhang et al 
2017) models citywide crowd flows based on residual learning. It partitions the city into a 
grid structure and represents the inflow and outflow of each grid cell as 2-channel image 
data. Residual networks are employed to effectively learn interactions between both nearby 
and  distant  regions.  SLCNN  (Zhang  et  al  2020)  utilizes  Structure  Learning  Convolution 
(SLC) to define graphs as learnable parameters for the effective modeling of both global 
static structures and dynamic structures within datasets. It replaces conventional CNN con-
volutions with SLC tailored to graph structures, generating graph-specific representations 
at each layer.

Recently, there have also been efforts to combine graph-based and raster-based method-
ologies to more effectively model both spatial structures and temporal dependencies. They 
are ideal for representing traffic flow as graphs and enabling detailed analysis of each node 
in smart city data. GMAN (Zheng et al 2020) effectively learns the dynamic spatio-temporal 
relationships in traffic networks through Spatio-Temporal Embedding (STE) and ST-Atten-
tion Block. It utilizes spatial attention to capture dynamic relationships between sensors, 
temporal attention to learn nonlinear temporal patterns, and gated fusion to integrate these 
features  seamlessly.  STSGCN  (Song  et  al  2020)  employs  the  Spatial-Temporal  Synchro-
nous Graph Convolutional Module (STSGCM) to synchronize and learn spatial and tem-
poral dependencies. It constructs a localized spatial-temporal graph to model relationships 
between neighboring nodes within the same time frame and nodes from past or future time 
frames  simultaneously.  GCN-SBULSTM  (Chen  et  al  2021b)  proposes  a  model  that  com-
bines  GCN  with  Stacked  Bidirectional  Unidirectional  LSTM  (SBULSTM). The  Bidirec-
tional LSTM captures temporal patterns, while GCN learns spatial dependencies, enabling 
integrated modeling of spatio-temporal interactions. Additionally, sequence-based methods 
process spatio-temporal data in sequence form, focusing primarily on temporal dynamics.

The  primary  objective  of  spatio-temporal  time  series  prediction  models  is  to  address 
the challenging task of integrating complex data structures while simultaneously learning 
temporal dependencies and spatial interactions. This enables accurate future state prediction 
and helps solve various real-world problems, facilitating precise decision-making.

6  Conclusion

This survey has been prepared to broaden the expertise of existing researchers and to assist 
beginners in gaining a fundamental understanding amid the rapid growth of time series fore-
casting (TSF) research. By integrating key concepts of time series and the latest techniques, 
we  aim  to  provide  researchers  with  clear  direction  and  insights,  fostering  the  continued 
advancement of this field. This survey paper comprehensively reviews recent advancements

---

<!-- PAGE 82 -->

216  Page 82 of 95

in TSF, focusing on deep learning models. It also incorporates key papers from major AI 
and ML conferences, as well as several notable papers from the arXiv preprint repository 
(https://arxiv.org).

TSF is a highly regarded topic, gradually expanding from the prominence of Transformer 
models  to  various  architecture-based  models.  Fundamental  deep  learning  models  like 
MLPs, CNNs, RNNs, and GNNs are being reassessed, and Transformers are also advanc-
ing by overcoming their previous limitations. Additionally, innovative models like Mamba 
are emerging, and models such as Diffusion are also entering the field, experiencing rapid 
growth.  Furthermore,  as  the  demand  for  foundation  models  in  the  field  of  TSF  intensi-
fies, pre-trained models based on large language models (LLMs) are emerging. To create 
a powerful predictive model, researchers need to be aware of these trends and understand 
both the characteristics of time series data and the strengths and weaknesses of different 
architectures.

Taking it a step further, we aim to address common challenges in TSF and provide deep 
insights into future development directions. In particular, we reviewed various studies that 
focus on approaches to channel correlation and address the challenges of distribution shift, 
which frequently occur in real-world scenarios. Additionally, we emphasized the need for 
research  that  leverages  causality  to  eliminate  spurious  correlations,  thereby  enabling  a 
deeper understanding of the underlying essence. We also discussed the importance of stud-
ies focused on effectively extracting features from complex time series data. In addition, we 
explored model combination techniques aimed at enhancing model performance, as well as 
spatio-temporal TSF problems to address complex real-world issues. Furthermore, we pro-
vided insights into improving model reliability by addressing interpretability and explain-
ability. Through this, we aim to present readers with potential directions for future research.
Limitations and future work

This survey acknowledges several limitations that could be addressed in future research.

● We  skipped  the  detailed  theoretical  backgrounds  of  the  models. This  survey  aims  to 
provide a comprehensive overview, facilitating comparison and analysis, thereby allow-
ing researchers to explore areas of interest more effectively. Although comprehensive 
information is primarily provided, readers can access additional details through refer-
ence links if needed.

● We left the specific differences in characteristics across various time series datasets for 
future  work.  Time  series  data  is  often  domain-specific,  requiring  expert  knowledge, 
which can be integrated into models to enhance performance. This underscores the im-
portance of interdisciplinary collaboration, and future research should continue to de-
velop in this direction. By integrating insights from a wide range of academic fields into 
TSF, it can contribute to the development of robust and generalized models.

● The aspect of expanding Artificial General Intelligence (AGI) and Adaptive Modeling 
could  be  further  explored.  Research  on  techniques  such  as  meta-learning,  reinforce-
ment learning, and neuro-symbolic AI can enhance the generalization and adaptability 
of models. In the current TSF field, time series-specific models and deep learning-based 
standard methodologies are dominant. However, as TSF problems become increasingly 
complex, research on generalization and adaptability holds great potential.

---

<!-- PAGE 83 -->

Page 83 of 95  216

Acknowledgements  This work was supported by Institute of Information & communications Technology 
Planning & Evaluation (IITP) grant funded by the Korea government (MSIT) [No. RS-2021-II211343, Arti-
ficial Intelligence Graduate School Program (Seoul National University); IITP-2025-RS-2024-00397085, the 
Leading Generative AI Human Resources Development], the National Research Foundation of Korea (NRF) 
grant funded by the Korea government (MSIT) (No. 2022R1A3B1077720; No. 2022R1A5A708390811), the 
BK21 FOUR program of the Education and the Research Program for Future ICT Pioneers, Seoul National 
University in 2025. H.G. Kim and S. Yoon were supported by Samsung Electronics Co., Ltd (IO240124-
08661-01).We would like to express our heartfelt gratitude to Jisoo Mok, Hyeongrok Han, Bonggyun Kang, 
Junyong Ahn, Jiin Kim, Youngwoo Kimh, Hyungyu Lee, Juhyeon Shin, Jaihyun Lew, and Jieun Byeon from 
our  research  lab  for  their  invaluable  assistance  in  reviewing  and  providing  feedback  on  this  paper. Their 
insights and suggestions have significantly enhanced the quality of our work.

Author Contributions  Jongseon Kim and Hyungjoon Kim contributed equally as co-first authors. They were 
responsible for setting the research direction and overall organization, conducting literature review and anal-
ysis, writing the manuscript, creating visual materials, and final revision. HyunGi Kim, as the third author, 
contributed to the literature review and draft writing of the sections on foundation models, distribution shift, 
and causality. Dongjun Lee, as the fourth author, contributed to the literature review and draft writing of the 
initial transformer-based models section. Sungroh Yoon guided the literature survey and the writing of the 
main manuscript text as the corresponding author. All the authors participated in writing and reviewing the 
manuscript.

Data Availability  No datasets were generated or analysed during the current study.

Declarations

Competing interests  The authors declare no competing interests.

Open  Access    This  article  is  licensed  under  a  Creative  Commons Attribution  4.0  International  License, 
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as 
you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons 
licence,  and  indicate  if  changes  were  made.  The  images  or  other  third  party  material  in  this  article  are 
included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. 
If material is not included in the article’s Creative Commons licence and your intended use is not permitted 
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the 
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

Abu-Mostafa YS, Atiya AF (1996) Introduction to financial forecasting. Appl Intell 6:205–213
Achiam J, Adler S, Agarwal S, et al (2023) Gpt-4 technical report. Preprint at arXiv:2303.08774
Ahamed MA, Cheng Q (2024) TimeMachine: a time series is worth 4 Mambas for long-term forecasting. IOS

Press. https://doi.org/10.3233/faia240677 (http://dx.doi.org/10.3233/faia240677)

Ahmed DM, Hassan MM, Mstafa RJ (2022) A review on deep sequential models for forecasting time series

data. Appl Comput Intell Soft Comput 1:6596397

Alcaraz JL, Strodthoff N (2023) Diffusion-based time series imputation and forecasting with structured state 
space models. Transactions on Machine Learning Research  h t t p s : / / o p e n r e v i e w . n e t / f o r u m ? i d = h H i I b k 7 
A p W

Alghamdi T, Elgazzar K, Bayoumi M, et al (2019) Forecasting traffic congestion using arima modeling. In: 
2019 15th international wireless communications & mobile computing conference (IWCMC), IEEE, 
pp 1227–1232

Ansari AF, Stella L, Turkmen AC, et al (2024) Chronos: Learning the language of time series. Transactions 
on Machine Learning Research https://openreview.net/forum?id=gerNCVqqtR, Expert Certification
Athanasopoulos G, Hyndman RJ, Song H et al (2011) The tourism forecasting competition. Int J Forecast

27(3):822–844

Bai S, Kolter JZ, Koltun V (2018) An empirical evaluation of generic convolutional and recurrent networks

for sequence modeling. Preprint at arXiv:1803.01271

---

<!-- PAGE 84 -->

216  Page 84 of 95

Barlin JN, Zhou Q, Clair CMS et al (2013) Classification and regression tree (cart) analysis of endometrial

carcinoma: seeing the forest for the trees. Gynecol Oncol 130(3):452–456

Behrouz A, Santacatterina M, Zabih R (2024) Chimera: Effectively modeling multivariate time series with 
2-dimensional  state  space  models.  In:  The  Thirty-eighth Annual  Conference  on  Neural  Information 
Processing Systems, https://openreview.net/forum?id=ncYGjx2vnE

Beltagy  I,  Peters  ME,  Cohan  A  (2020)  Longformer:  The  long-document  transformer.  Preprint  at

arXiv:2004.05150

Benidis K, Rangapuram SS, Flunkert V et al (2022) Deep learning for time series forecasting: Tutorial and

literature survey. ACM Comput Surv 55(6):1–36

Bergsma S, Zeyl T, Guo L (2023) Sutranets: sub-series autoregressive networks for long-sequence, probabi-

listic forecasting. Adv Neural Inf Process Syst 36:30518–30533

Box GE, Jenkins GM, Reinsel G et al (1970) Forecasting and control. Time Series. Analysis 3(75):1970
Breiman L (1996) Bagging predictors. Mach Learning 24:123–140
Brown RG (1959) Statistical forecasting for inventory control. (No Title)
Brown T, Mann B, Ryder N et al (2020) Language models are few-shot learners. Adv Neural Inf Process

Syst 33:1877–1901

Cai W, Liang Y, Liu X, et al (2024a) Msgnet: Learning multi-scale inter-series correlations for multivari-
ate  time  series  forecasting.  In:  Proceedings  of  the  AAAI  Conference  on  Artificial  Intelligence,  pp 
11141–11149

Cai W, Wang K, Wu H, et al (2024b) Forecastgrapher: Redefining multivariate time series forecasting with

graph neural networks. Preprint at arXiv:2405.18036

Cai X, Zhu Y, Wang X, et al (2024c) Mambats: Improved selective state space models for long-term time

series forecasting. Preprint at arXiv:2405.16440

Cao H, Tan C, Gao Z, et al (2024) A survey on generative diffusion models. IEEE Transactions on Knowledge

and Data Engineering

Center JMK (2020) Dominick’s dataset
Challu C, Olivares KG, Oreshkin BN, et al (2023) Nhits: Neural hierarchical interpolation for time series

forecasting. In: Proceedings of the AAAI conference on artificial intelligence, pp 6989–6997

Chang S, Zhang Y, Han W, et al (2017) Dilated recurrent neural networks. Adv Neural Inform Process Syst 30
Chen P, Fu X, Wang X (2021) A graph convolutional stacked bidirectional unidirectional-LSTM neural net-

work for metro ridership prediction. IEEE Trans Intell Transp Syst 23(7):6950–6962

Chen Y, Zou X, Li K et al (2021) Multiple local 3D CNNs for region-based prediction in smart cities. Inf

Sci 542:476–491

Chen H, Lundberg SM, Lee SI (2022) Explaining a series of models by propagating Shapley values. Nat

Commun 13(1):4512

Chen Z, Ma M, Li T et al (2023) Long sequence time-series forecasting with deep learning: a survey. Inform

Fusion 97:101819

Chen K, Chen G, Xu D, et al (2021a) Nast: Non-autoregressive spatial-temporal transformer for time series

forecasting. Preprint at arXiv:2102.05624

Cheng X, Chen X, Li S, et al (2024c) Leveraging 2D information for long-term time series forecasting with

vanilla transformers. Preprint at arXiv:2405.13810

Chen T, Guestrin C (2016) Xgboost: A scalable tree boosting system. In: Proceedings of the 22nd ACM SIG-

KDD international conference on knowledge discovery and data mining, pp 785–794

Cheng H, Wen Q, Liu Y, et al (2024a) Robusttsf: Towards theory and design of robust time series forecasting

with anomalies. ICRL

Cheng M, Yang J, Pan T, et al (2024b) Convtimenet: A deep hierarchical fully convolutional model for mul-

tivariate time series analysis. Preprint at arXiv:2403.01493

Chen J, Lenssen JE, Feng A, et al (2024a) From similarity to superiority: Channel clustering for time series 
forecasting.  In:  The  Thirty-eighth  Annual  Conference  on  Neural  Information  Processing  Systems, 
https://openreview.net/forum?id=MDgn9aazo0

Chen X, Li X, Liu B, et al (2024c) Biased temporal convolution graph network for time series forecasting

with missing values. In: The Twelfth International Conference on Learning Representations

Chen Y, Ren K, Wang Y, et al (2024d) Contiformer: Continuous-time transformer for irregular time series

modeling. Adv Neural Inform Process Syst 36

Chen P, ZHANG Y, Cheng Y, et al (2024b) Pathformer: Multi-scale transformers with adaptive pathways for 
time series forecasting. In: The Twelfth International Conference on Learning Representations,  h t t p s : / / 
o p e n r e v i e w . n e t / f o r u m ? i d = l J k O C M P 2 a W

Chicco D, Warrens MJ, Jurman G (2021) The coefficient of determination r-squared is more informative than

SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation. Peer J Comput Sci 7:e623

---

<!-- PAGE 85 -->

Page 85 of 95  216

Cho K, van Merriënboer B, Gulcehre C, et al (2014) Learning phrase representations using RNN encoder–
decoder for statistical machine translation. In: Moschitti A, Pang B, Daelemans W (eds) Proceedings 
of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP). Association 
for Computational Linguistics, Doha, Qatar, pp 1724–1734, https://doi.org/10.3115/v1/D14-1179,  h t t p 
s : / / a c l a n t h o l o g y . o r g / D 1 4 - 1 1 7 9 /

Clark K, Luong MT, Le QV, et al (2020) Electra: Pre-training text encoders as discriminators rather than 
generators.  In:  International  Conference  on  Learning  Representations,   h t t p s : / / o p e n r e v i e w . n e t / f o r u m ? 
i d = r 1 x M H 1 B t v B

Cortes C (1995) Support-vector networks. Machine Learning
Coskunuzer  B,  Segovia-Dominguez  I,  Chen  Y,  et  al  (2024)  Time-aware  knowledge  representations  of 
dynamic objects with multidimensional persistence. In: Proceedings of the AAAI Conference on Arti-
ficial Intelligence, pp 11678–11686

Crabbé J, Huynh N, Stanczuk JP, et al (2024) Time series diffusion in the frequency domain. In: Forty-first 
International Conference on Machine Learning, https://openreview.net/forum?id=W9GaJUVLCT

Cryer JD (1986) Time series analysis, vol 286. Duxbury Press Boston
Dai  Z,  Yang  Z,  Yang  Y,  et  al  (2019)  Transformer-XL: Attentive  language  models  beyond  a  fixed-length 
context. In: Korhonen A, Traum D, Màrquez L (eds) Proceedings of the 57th Annual Meeting of the 
Association for Computational Linguistics. Association for Computational Linguistics, Florence, Italy, 
pp 2978–2988, https://doi.org/10.18653/v1/P19-1285, https://aclanthology.org/P19-1285

Danese P, Kalchschmidt M (2011) The role of the forecasting process in improving forecast accuracy and 
operational performance. Int J Prod Econ 131(1):204–214. https://doi.org/10.1016/j.ijpe.2010.09.006 ( 
h t t p s :  / / w w w  . s c i e n  c e d i  r e c t .  c o m / s  c i e n c e  / a r t  i c l e /  p i i / S  0 9 2 5 5 2  7 3 1 0  0 0 3 2 8 2 ,   i n n s b r u c k   2 0 0 8)

Das A, Kong W, Sen R, et al (2024) A decoder-only foundation model for time-series forecasting. In: Forty-
first International Conference on Machine Learning, https://openreview.net/forum?id=jn2iTJas6h
Devlin J, Chang MW, Lee K, et al (2019) BERT: Pre-training of deep bidirectional transformers for language 
understanding.  In:  Burstein  J,  Doran  C,  Solorio T  (eds)  Proceedings  of  the  2019  Conference  of  the 
North American  Chapter  of  the Association  for  Computational  Linguistics:  Human  Language Tech-
nologies, Volume 1 (Long and Short Papers). Association for Computational Linguistics, Minneapolis, 
Minnesota, pp 4171–4186, https://doi.org/10.18653/v1/N19-1423, https://aclanthology.org/N19-1423

Dimri  T,  Ahmad  S,  Sharif  M  (2020)  Time  series  analysis  of  climate  variables  using  seasonal  ARIMA

approach. J Earth Syst Sci 129:1–16

Dosovitskiy A, Beyer L, Kolesnikov A, et al (2021) An image is worth 16x16 words: Transformers for image 
recognition at scale. In: International Conference on Learning Representations,  h t t p s : / / o p e n r e v i e w . n e t 
/ f o r u m ? i d = Y i c b F d N T T y

Dragomiretskiy  K,  Zosso  D  (2013)  Variational  mode  decomposition.  IEEE  Trans  Signal  Process

62(3):531–544

Dubey A, Jauhri A, Pandey A, et al (2024) The llama 3 herd of models. Preprint at arXiv:2407.21783
Dudek G (2024) Stacking for probabilistic short-term load forecasting. In: International Conference on Com-

putational Science, Springer, pp 3–18

Ekambaram V, Jati A, Dayama P, et al (2024) Tiny time mixers (ttms): Fast pre-trained models for enhanced

zero/few-shot forecasting of multivariate time series. CoRR

Ekambaram V, Jati A, Nguyen N, et al (2023) TSMIXER: Lightweight MLP-mixer model for multivariate 
time series forecasting. In: Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discov-
ery and Data Mining, pp 459–469

Eldele E, Ragab M, Chen Z, et al (2021) Time-series representation learning via temporal and contextual con-
trasting. Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21)
Eldele  E,  Ragab  M,  Chen  Z,  et  al  (2024)  Tslanet:  Rethinking  transformers  for  time  series  representation

learning. International Conference on Machine Learning

Fan W, Wang P, Wang D, et al (2023) DISH-TS: a general paradigm for alleviating distribution shift in time 
series forecasting. In: Proceedings of the AAAI Conference on Artificial Intelligence, pp 7522–7529
Fan  X, Wu Y,  Xu  C,  et  al  (2024b)  MG-TSD:  Multi-granularity  time  series  diffusion  models  with  guided 
learning process. In: The Twelfth International Conference on Learning Representations,  h t t p s : / / o p e n r 
e v i e w . n e t / f o r u m ? i d = C Z i Y 6 O L k t d

Fan H, Xiong B, Mangalam K, et al (2021) Multiscale vision transformers. In: Proceedings of the IEEE/CVF

international conference on computer vision, pp 6824–6835

Fan W, Yi K, Ye H, et al (2024a) Deep frequency derivative learning for non-stationary time series forecast-

ing. IJCAI

Feng R, Chen M, Song Y (2024) Learning traffic as videos: short-term traffic flow prediction using mixed-

pointwise convolution and channel attention mechanism. Expert Syst Appl 240:122468

Feng S, Miao C, Zhang Z, et al (2024b) Latent diffusion transformer for probabilistic time series forecasting.

In: Proceedings of the AAAI Conference on Artificial Intelligence, pp 11979–11987

---

<!-- PAGE 86 -->

216  Page 86 of 95

Freund Y, Schapire RE (1997) A decision-theoretic generalization of on-line learning and an application to

boosting. J Comput Syst Sci 55(1):119–139

Friedman JH (2001) Greedy function approximation: a gradient boosting machine. Annals of statistics pp

1189–1232

Fu DY, Dao T, Saab KK, et al (2023) Hungry hungry hippos: Towards language modeling with state space

models. In The International Conference on Learning Representations (ICLR)

Fukushima K (1980) Neocognitron: a self-organizing neural network model for a mechanism of pattern rec-

ognition unaffected by shift in position. Biol Cybern 36(4):193–202

Gallifant J, Fiske A, Levites Strekalova YA et al (2024) Peer review of GPT-4 technical report and systems

card. PLOS Digital Health 3(1):e0000417

Ganaie MA, Hu M, Malik AK et al (2022) Ensemble deep learning: a review. Eng Appl Artif Intell 115:105151
García MV, Aznarte JL (2020) Shapley additive explanations for no2 forecasting. Eco Inform 56:101039
Godahewa R, Bergmeir C, Webb G, et al (2021a) Solar power dataset (4 seconds observations).  h t t p s : / / d o i .

o r g / 1 0 . 5 2 8 1 / z e n o d o . 4 6 5 6 0 2 7

Godahewa R, Bergmeir C, Webb G et al (2021b) Wind farms dataset (with missing values).  h t t p s : / / d o i . o r g /

1 0 . 5 2 8 1 / z e n o d o . 4 6 5 4 9 0 9

Godahewa R, Bergmeir C, Webb G et al (2021c) Wind farms dataset (without missing values).  h t t p s : / / d o i . o

r g / 1 0 . 5 2 8 1 / z e n o d o . 4 6 5 4 8 5 8

Godahewa R, Bergmeir C, Webb G et al (2021e) Australian electricity demand dataset.  h t t p s : / / d o i . o r g / 1 0 . 5

2 8 1 / z e n o d o . 4 6 5 9 7 2 7

Godahewa R, Bergmeir C, Webb G et al (2021f) Bitcoin dataset with missing values.  h t t p s : / / d o i . o r g / 1 0 . 5 2 8

1 / z e n o d o . 5 1 2 1 9 6 5

Godahewa R, Bergmeir C, Webb G et al (2021g) Bitcoin dataset without missing values.  h t t p s : / / d o i . o r g / 1 0 .

5 2 8 1 / z e n o d o . 5 1 2 2 1 0 1

Godahewa R, Bergmeir C, Webb G et al (2021h) Rideshare dataset with missing values.  h t t p s : / / d o i . o r g / 1 0 . 5

2 8 1 / z e n o d o . 5 1 2 2 1 1 4

Godahewa R, Bergmeir C, Webb G et al (2021i) Rideshare dataset without missing values.  h t t p s : / / d o i . o r g / 1

0 . 5 2 8 1 / z e n o d o . 5 1 2 2 2 3 2

Godahewa R, Bergmeir C, Webb G et al (2021j) Temperature rain dataset with missing values.  h t t p s : / / d o i . o

r g / 1 0 . 5 2 8 1 / z e n o d o . 5 1 2 9 0 7 3

Godahewa R, Bergmeir C, Webb G et al (2021k) Temperature rain dataset without missing values.  h t t p s : / / d

o i . o r g / 1 0 . 5 2 8 1 / z e n o d o . 5 1 2 9 0 9 1

Godahewa RW, Bergmeir C, Webb GI, et al (2021l) Monash time series forecasting archive. In: Thirty-fifth 
Conference  on  Neural  Information  Processing  Systems  Datasets  and  Benchmarks  Track  (Round  2), 
https://openreview.net/forum?id=wEc1mgAjU-

Godahewa R, Bergmeir C, Webb G, et al (2021d) Wind power dataset (4 seconds observations).  h t t p s : / / d o i .

o r g / 1 0 . 5 2 8 1 / z e n o d o . 4 6 5 6 0 3 2

Gong Z, Tang Y, Liang J (2023) Patchmixer: A patch-mixing architecture for long-term time series forecast-

ing. Preprint at arXiv:2310.00655

Granger  CW  (1969)  Investigating  causal  relations  by  econometric  models  and  cross-spectral  methods.

Econometrica: J Econom Soc 424–438

Graziani  M,  Dutkiewicz  L,  Calvaresi  D  et  al  (2023) A  global  taxonomy  of  interpretable AI:  unifying  the

terminology for the technical and social sciences. Artif Intell Rev 56(4):3473–3504

Gruver N, Finzi MA, Qiu S, et al (2023) Large language models are zero-shot time series forecasters. In: 
Thirty-seventh Conference on Neural Information Processing Systems,  h t t p s : / / o p e n r e v i e w . n e t / f o r u m ? 
i d = m d 6 8 e 8 i Z K 1

Gu A, Johnson I, Goel K et al (2021) Combining recurrent, convolutional, and continuous-time models with

linear state space layers. Adv Neural Inf Process Syst 34:572–585

Gu A, Dao T (2024) Mamba: Linear-time sequence modeling with selective state spaces. In: First Conference

on Language Modeling, https://openreview.net/forum?id=tEYskw1VY2

Gu A, Goel K, Re C (2022) Efficiently modeling long sequences with structured state spaces. In: International

Conference on Learning Representations, https://openreview.net/forum?id=uYLFoz1vlAC

Hahn Y, Langer T, Meyes R et al (2023) Time series dataset survey for forecasting with deep learning. Fore-

casting 5(1):315–335

Hamon  R,  Junklewitz  H,  Sanchez  I  et  al  (2022)  Bridging  the  gap  between AI  and  explainability  in  the 
GDPR:  towards  trustworthiness-by-design  in  automated  decision-making.  IEEE  Comput  Intell  Mag 
17(1):72–85

Han H, Park S, Min S et al (2023) Improving generalization performance of electrocardiogram classification

models. Physiol Meas 44(5):054003

---

<!-- PAGE 87 -->

Page 87 of 95  216

Han L, Chen XY, Ye HJ, et al (2024) SOFTS: Efficient multivariate time series forecasting with series-core 
fusion. In: The Thirty-eighth Annual Conference on Neural Information Processing Systems,  h t t p s : / / o p 
e n r e v i e w . n e t / f o r u m ? i d = 8 9 A U i 5 L 1 u A

Han H, Kim S, Choi HS, et al (2023a) On the impact of knowledge distillation for model interpretability. In:

Proceedings of the 40th International Conference on Machine Learning. JMLR.org, ICML’23

Hasson H, Maddix DC, Wang B, et al (2023) Theoretical guarantees of learning ensembling strategies with 
applications to time series forecasting. In: International Conference on Machine Learning, PMLR, pp 
12616–12632

Ho  J,  Jain  A,  Abbeel  P  (2020)  Denoising  diffusion  probabilistic  models.  Adv  Neural  Inf  Process  Syst

33:6840–6851

Hochreiter S, Schmidhuber J (1997) Long short-term memory. Neural Comput 9(8):1735–1780
Holt CC (1957) Forecasting trends and seasonals by exponentially weighted averages. Carnegie institute of

technology. Pittsburgh ONR memorandum

Hopfield JJ (1982) Neural networks and physical systems with emergent collective computational abilities.

Proc Natl Acad Sci 79(8):2554–2558

Hounie I, Porras-Valenzuela J, Ribeiro A (2024) Transformers with loss shaping constraints for long-term

time series forecasting. In: Forty-first International Conference on Machine Learning

Hou H, Yu FR (2024) Rwkv-ts: Beyond traditional recurrent neural network for time series tasks. Preprint

at arXiv:2401.09093

Huang NE, Shen Z, Long SR et al (1998) The empirical mode decomposition and the Hilbert spectrum for

nonlinear and non-stationary time series analysis. Proc R Soc Lond Ser A 454(1971):903–995

Huang S, Liu Y, Zhang F et al (2024) Crosswavenet: a dual-channel network with deep cross-decomposition

for long-term time series forecasting. Expert Syst Appl 238:121642

Huang Q, Shen L, Zhang R, et al (2024a) HDMIXER: Hierarchical dependency with extendable patch for 
multivariate time series forecasting. In: Proceedings of the AAAI Conference on Artificial Intelligence, 
pp 12608–12616

Huber PJ (1992) Robust estimation of a location parameter. In: Breakthroughs in statistics: Methodology and

distribution. Springer, pp 492–518

Hu J, Lan D, Zhou Z, et al (2024a) Time-ssm: Simplifying and unifying state space models for time series

forecasting. CoRR abs/2405.16312. https://doi.org/10.48550/arXiv.2405.16312

Hu Y, Liu P, Zhu P, et al (2024b) Adaptive multi-scale decomposition framework for time series forecasting.

CoRR abs/2406.03751. https://doi.org/10.48550/arXiv.2406.03751

Ilbert R, Odonnat A, Feofanov V, et al (2024) SAMformer: Unlocking the potential of transformers in time 
series forecasting with sharpness-aware minimization and channel-wise attention. In: Salakhutdinov R, 
Kolter Z, Heller K, et al (eds) Proceedings of the 41st International Conference on Machine Learning, 
Proceedings of Machine Learning Research, vol 235. PMLR, pp 20924–20954,  h t t p s :  / / p r o  c e e d i n  g s . m  l 
r . p r  e s s / v  2 3 5 / i l  b e r t  2 4 a . h t m l

Ioffe  S,  Szegedy  C  (2015)  Batch  normalization: Accelerating  deep  network  training  by  reducing  internal

covariate shift. In: International conference on machine learning, pmlr, pp 448–456

Jhin SY, Kim S, Park N (2024) Addressing prediction delays in time series forecasting: A continuous gru 
approach  with  derivative  regularization.  In:  Proceedings  of  the  30th ACM  SIGKDD  Conference  on 
Knowledge Discovery and Data Mining, pp 1234–1245

Jia Y, Lin Y, Hao X, et al (2024) Witran: Water-wave information transmission and recurrent acceleration

network for long-range time series forecasting. Adv Neural Inform Process Syst 36

Jin M, Wang S, Ma L, et al (2024) Time-LLM: Time series forecasting by reprogramming large language

models. In: International Conference on Learning Representations (ICLR)

Jin M, Wen Q, Liang Y, et al (2023) Large models for time series and Spatio-temporal data: a survey and

outlook. Preprint at arXiv:2310.10196

Jung D, Lee J, Yi J, et al (2020) ICAPS: an interpretable classifier via disentangled capsule networks. In:

European Conference on Computer Vision, Springer, pp 314–330

Kalman RE (1960) A new approach to linear filtering and prediction problems. Transact ASME-J Basic Eng

82(1):35–45

Kang BG, Lee D, Kim H, et al (2024) Introducing spectral attention for long-range dependency in time series

forecasting. Adv Neural Inform Process Syst

Ke G, Meng Q, Finley T, et al (2017) LIGHTGBM: A highly efficient gradient boosting decision tree. Adv

Neural Inform Process Syst 30

Khosravi A, Mazloumi E, Nahavandi S et al (2011) Prediction intervals to account for uncertainties in travel

time prediction. IEEE Trans Intell Transp Syst 12(2):537–547

Kim D, Baek JG (2022) Bagging ensemble-based novel data generation method for univariate time series

forecasting. Expert Syst Appl 203:117366

---

<!-- PAGE 88 -->

216  Page 88 of 95

Kim T,  Kim  J, Tae Y,  et  al  (2021)  Reversible  instance  normalization  for  accurate  time-series  forecasting

against distribution shift. In: International Conference on Learning Representations

Kim D, Park J, Lee J, et al (2024) Are self-attentions effective for time series forecasting? In: The Thirty-
eighth Annual Conference on Neural Information Processing Systems,  h t t p s : / / o p e n r e v i e w . n e t / f o r u m ? i 
d = i N 4 3 s J o i b 7

Kim S, Yi J, Kim E, et al (2020) Interpretation of NLP models through input marginalization. In: Webber B, 
Cohn T, He Y, et al (eds) Proceedings of the 2020 Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP). Association for Computational Linguistics, Online, pp 3154–3167,  h t t p s :  / 
/ d o i  . o r g / 1  0 . 1 8  6 5 3 / v  1 / 2 0 2  0 . e m n l  p - m a  i n . 2 5 5,  h t t p s :  / / a c l  a n t h o l  o g y .  o r g / 2 0 2 0 . e m n l p - m a i n . 2 5 5 /

Kipf TN, Welling M (2017) Semi-supervised classification with graph convolutional networks. In: Interna-

tional Conference on Learning Representations, https://openreview.net/forum?id=SJU4ayYgl

Kitaev N, Kaiser L, Levskaya A (2020) Reformer: The efficient transformer. In: International Conference on

Learning Representations, https://openreview.net/forum?id=rkgNKkHtvB

Koenker R, Bassett Jr G (1978) Regression quantiles. Econometrica: J Econom Soc 33–50
Kollovieh M, Ansari AF, Bohlke-Schneider M, et al (2024) Predict, refine, synthesize: Self-guiding diffusion

models for probabilistic time series forecasting. Adv Neural Inform Process Syst 36

Kong Z, Ping W, Huang J, et al (2021) Diffwave: A versatile diffusion model for audio synthesis. In: Interna-
tional Conference on Learning Representations, https://openreview.net/forum?id=a-xFK8Ymz5J
Kontopoulou VI, Panagopoulos AD, Kakkos I et al (2023) A review of Arima vs. machine learning approaches

for time series forecasting in data driven networks. Future Internet 15(8):255

LeCun Y, Bottou L, Bengio Y et al (1998) Gradient-based learning applied to document recognition. Proc

IEEE 86(11):2278–2324

Liang A, Jiang X, Sun Y, et al (2024a) Bi-mamba4ts: Bidirectional mamba for time series forecasting. Pre-

print at arXiv:2404.15772

Liang Y, Wen H, Nie Y, et al (2024c) Foundation models for time series analysis: A tutorial and survey. Pre-

print at arXiv:2403.14735

Liang D, Zhang H, Yuan D, et al (2024b) Minusformer: Improving time series forecasting by progressively

learning residuals. Preprint at arXiv:2402.02332

Li Y, Chen W, Hu X, et al (2024b) Transformer-modulated diffusion models for probabilistic multivariate 
time series forecasting. In: The Twelfth International Conference on Learning Representations,  h t t p s : / / 
o p e n r e v i e w . n e t / f o r u m ? i d = q a e 0 4 Y A C H s

Li S, Jin X, Xuan Y, et al (2019) Enhancing the locality and breaking the memory bottleneck of transformer

on time series forecasting. Adv Neural Inform Process Syst 32

Li J, Li D, Savarese S, et al (2023) Blip-2: Bootstrapping language-image pre-training with frozen image 
encoders  and  large  language  models.  In:  International  conference  on  machine  learning,  PMLR,  pp 
19730–19742

Lim  B,  Zohren  S  (2021)  Time-series  forecasting  with  deep  learning:  a  survey.  Phil  Trans  R  Soc  A

379(2194):20200209

Lim B, Arık SÖ, Loeff N et al (2021) Temporal fusion transformers for interpretable multi-horizon time series

forecasting. Int J Forecast 37(4):1748–1764

Lin  K,  Huang  C  (2022)  Ensemble  learning  applications  in  multiple  industries:  a  review.  Inf  Dyn  Appl

1(1):44–58

Lin L, Li Z, Li R et al (2024) Diffusion models for time-series applications: a survey. Front Inform Technol

Electron Eng 25(1):19–41

Lin S, Lin W, Wu W et al (2024) SPARSETSF: Modeling long-term time series forecasting with 1k parameters
Lin S, Lin W, Wu W, et al (2024c) PETformer: Long-term time series forecasting via placeholder-enhanced

transformer. https://openreview.net/forum?id=u3RJbzzBZj

Lipton ZC (2018) The mythos of model interpretability: in machine learning, the concept of interpretability

is both important and slippery. Queue 16(3):31–57

Li Z, Qin Y, Cheng X, et al (2024d) Ftmixer: Frequency and time domain representations fusion for time

series modeling. Preprint at arXiv:2405.15256

Liu Z, Zhu Z, Gao J et al (2021) Forecast methods for time series data: a survey. IEEE Access 9:91896–91912
Liu Y, Wu H, Wang J et al (2022) Non-stationary transformers: exploring the stationarity in time series fore-

casting. Adv Neural Inf Process Syst 35:9881–9893

Liu Z,  Cheng M,  Li Z,  et al (2024e) Adaptive normalization for  non-stationary  time series forecasting: a

temporal slice perspective. Adv Neural Inform Process Syst 36

Liu Y, Hu T, Zhang H, et al (2024c) itransformer: Inverted transformers are effective for time series forecast-
ing. In: The Twelfth International Conference on Learning Representations,  h t t p s : / / o p e n r e v i e w . n e t / f o r 
u m ? i d = J e P f A I 8 f a h

Liu J, Liu C, Woo G, et al (2024b) Unitst: Effectively modeling inter-series and intra-series dependencies for

multivariate time series forecasting. Preprint at arXiv:2406.04975

---

<!-- PAGE 89 -->

Page 89 of 95  216

Liu Y,  Li  C, Wang  J,  et  al  (2024d)  Koopa:  Learning  non-stationary  time  series  dynamics  with  Koopman

predictors. Adv Neural Inform Process Syst 36

Liu H, Li C, Wu Q, et al (2024a) Visual instruction tuning. Adv Neural Inform Process Syst 36
Liu  S, Yu  H,  Liao  C,  et  al  (2021a)  Pyraformer:  Low-complexity  pyramidal  attention  for  long-range  time

series modeling and forecasting. In: International conference on learning representations

Li Y, Xu J, Anastasiu D (2024c) Learning from polar representation: An extreme-adaptive model for long-
term  time  series  forecasting.  In:  Proceedings  of  the AAAI  Conference  on Artificial  Intelligence,  pp 
171–179

Li J, Xu X, Ding X, et al (2024a) Bayesian spatio-temporal graph convolutional network for railway train

delay prediction. IEEE Transactions on Intelligent Transportation Systems

Li Y, Yu R, Shahabi C, et al (2018) Diffusion convolutional recurrent neural network: Data-driven traffic 
forecasting. In: International Conference on Learning Representations,  h t t p s : / / o p e n r e v i e w . n e t / f o r u m ? 
i d = S J i H X G W A Z

Lu Han DCZHan-Jia Ye (2024) The capacity and robustness trade-off: Revisiting the channel independent 
strategy for multivariate time series forecasting. IEEE Transactions on Knowledge and Data Engineer-
ing pp 1–14

Lu J, Han X, Sun Y, et al (2024) Cats: Enhancing multivariate time series forecasting by constructing auxil-

iary time series as exogenous variables. Int Conf Mach Learn

Lundberg SM, Lee SI (2017) A unified approach to interpreting model predictions. In: Guyon I, Luxburg 
UV, Bengio S, et al (eds) Advances in Neural Information Processing Systems, vol 30. Curran Associ-
ates, Inc.,  h t t p s :  / / p r o  c e e d i n  g s . n  e u r i p  s . c c /  p a p e r _  fi  l e  s / p a p  e r / 2 0  1 7 / fi  l  e / 8 a  2 0 a 8 6  2 1 9 7 8  6 3 2 d 7 6  c 4 3 d  f d 2 8 b 6 
7 7 6 7 - P a p e r . p d f

Luo D, Wang X (2024) Moderntcn: A modern pure convolution structure for general time series analysis. In:

The Twelfth International Conference on Learning Representations

Ma Y, Guo Z, Ren Z, et al (2020) Streaming graph neural networks. In: Proceedings of the 43rd international

ACM SIGIR conference on research and development in information retrieval, pp 719–728

Makridakis S, Hibon M (2000) The M3-competition: results, conclusions and implications. Int J Forecast

16(4):451–476

Makridakis  S, Andersen A,  Carbone  R  et  al  (1982) The  accuracy  of  extrapolation  (time  series)  methods:

Results of a forecasting competition. J Forecast 1(2):111–153

Makridakis S, Spiliotis E, Assimakopoulos V (2020) The M4 competition: 100,000 time series and 61 fore-

casting methods. Int J Forecast 36(1):54–74

Ma X, Li X, Fang L, et al (2024) U-mixer: An unet-mixer architecture with stationarity correction for time 
series forecasting. In: Proceedings of the AAAI Conference on Artificial Intelligence, pp 14255–14262
Marisca I, Alippi C, Bianchi FM (2024) Graph-based forecasting with missing data through spatiotemporal

downsampling

Masini  RP,  Medeiros  MC,  Mendes  EF  (2023)  Machine  learning  advances  for  time  series  forecasting.  J

Econom Surv 37(1):76–111

Massaoudi M, Refaat SS, Chihi I et al (2021) A novel stacked generalization ensemble-based hybrid LGBM-

XGB-MLP model for short-term load forecasting. Energy 214:118874

Matheson  JE,  Winkler  RL  (1976)  Scoring  rules  for  continuous  probability  distributions.  Manage  Sci

22(10):1087–1096

McCracken  MW,  Ng  S  (2016)  FRED-MD:  a  monthly  database  for  macroeconomic  research.  J  Business

Econom Stat 34(4):574–589

McLeod A,  Gweon  H  (2013)  Optimal deseasonalization for  monthly and  daily  geophysical time series.  J

Environ Stat 4(11):1–11

Meijer C, Chen LY (2024) The rise of diffusion models in time-series forecasting. Preprint at arXiv:2401.03006
Mounir N, Ouadi H, Jrhilifa I (2023) Short-term electric load forecasting using an EMD-BI-LSTM approach

for smart grid energy management system. Energy Build 288:113022

Mu B, Jiang X, Yuan S et al (2023) Nao seasonal forecast using a multivariate air-sea coupled deep learning

model combined with causal discovery. Atmosphere 14(5):792

Nason GP, Von Sachs R, Kroisandt G (2000) Wavelet processes and adaptive estimation of the evolutionary

wavelet spectrum. J R Stat Soc 62(2):271–292

Nawrot  P, Tworkowski  S, Tyrolski  M,  et  al  (2021)  Hierarchical  transformers  are  more  efficient  language

models. Preprint at arXiv:2110.13711

Nie T, Mei Y, Qin G, et al (2024) Channel-aware low-rank adaptation in time series forecasting. Conference

on Information and Knowledge Management

Nie Y, Nguyen NH, Sinthong P, et al (2023) A time series is worth 64 words: Long-term forecasting with 
transformers. In: The Eleventh International Conference on Learning Representations,  h t t p s : / / o p e n r e v i 
e w . n e t / f o r u m ? i d = J b d c 0 v T O c o l

---

<!-- PAGE 90 -->

216  Page 90 of 95

Ni Z, Yu H, Liu S, et al (2024) Basisformer: Attention-based time series forecasting with learnable and inter-

pretable basis. Adv Neural Inform Process Syst 36

Nti IK, Teimeh M, Nyarko-Boateng O et al (2020) Electricity load forecasting: a systematic review. J Electric

Syst Inform Technol 7:1–19

Oord Avd, Li Y, Vinyals O (2018) Representation learning with contrastive predictive coding. Preprint at

arXiv:1807.03748

Oreshkin BN, Carpov D, Chapados N, et al (2020) N-beats: Neural basis expansion analysis for interpretable 
time series forecasting. In: International Conference on Learning Representations,  h t t p s : / / o p e n r e v i e w . 
n e t / f o r u m ? i d = r 1 e c q n 4 Y w B

Pan SJ, Yang Q (2009) A survey on transfer learning. IEEE Trans Knowl Data Eng 22(10):1345–1359
Papapetrou P, Lee Z (2024) Interpretable and explainable time series mining. In: 2024 IEEE 11th Interna-

tional Conference on Data Science and Advanced Analytics (DSAA), IEEE, pp 1–3

Park C, Lee C, Bahng H, et al (2020) St-grat: A novel spatio-temporal graph attention networks for accurately 
forecasting dynamically changing road speed. In: Proceedings of the 29th ACM international confer-
ence on information & knowledge management, pp 1215–1224

Passalis N, Tefas A, Kanniainen J et al (2019) Deep adaptive input normalization for time series forecasting.

IEEE Transact Neural Netw Learn Syst 31(9):3760–3765

Patro BN, Agneeswaran VS (2024a) Mamba-360: Survey of state space models as transformer alternative for

long sequence modelling: Methods, applications, and challenges. Preprint at arXiv:2404.16112

Patro BN, Agneeswaran VS (2024b) Simba: Simplified mamba-based architecture for vision and multivariate

time series. Preprint at arXiv:2403.15360

Patwardhan N, Marrone S, Sansone C (2023) Transformers in the real world: a survey on NLP applications.

Information 14(4):242

Pavlyshenko BM (2020) Using bayesian regression for stacking time series predictive models. In: 2020 IEEE 
Third International Conference on Data Stream Mining & Processing (DSMP), pp 305–309,  h t t p s :  / / d o i  
. o r g / 1  0 . 1 1  0 9 / D S  M P 4 7 3  6 8 . 2 0 2  0 . 9 2  0 4 3 1 2

Pearl J (1995) Causal diagrams for empirical research. Biometrika 82(4):669–688
Pearl J (1998) Graphs, causality, and structural equation models. Sociol Methods Res 27(2):226–284
Pearl J et al (2000) Models, reasoning and inference, vol 19. Cambridge University Press, Cambridge, p 3
Peng Zj, Zhang C, Tian Yx (2023) Crude oil price time series forecasting: a novel approach based on varia-

tional mode decomposition, time-series imaging, and deep learning. IEEE Access

Petropoulos F, Hyndman RJ, Bergmeir C (2018) Exploring the sources of uncertainty: why does bagging for

time series forecasting work? Eur J Oper Res 268(2):545–554

Piao X, Chen Z, Murayama T, et al (2024) Fredformer: Frequency debiased transformer for time series fore-

casting. In: KDD, pp 2400–2410, https://doi.org/10.1145/3637528.3671928

Portet S (2020) A primer on model selection using the Akaike information criterion. Infectious Disease Mod-

elling 5:111–128

Qian J, Wang Q, Wu Y, et al (2023) Causality-based deep learning forecast of the Kuroshio volume transport

in the east china sea. Earth Space Sci 10(2):e2022EA002722

Qin Y, Song D, Chen H, et al (2017) A dual-stage attention-based recurrent neural network for time series pre-
diction. In: Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence, 
IJCAI-17, pp 2627–2633, https://doi.org/10.24963/ijcai.2017/366

Qi  S, Wen  L,  Li Y,  et  al  (2024)  Enhancing  multivariate  time  series  forecasting  with  mutual  information-

driven cross-variable and temporal modeling. Preprint at arXiv:2403.00869

Quinlan JR (1986) Induction of decision trees. Mach learning 1:81–106
Radford A,  Kim  JW,  Hallacy  C,  et  al  (2021)  Learning  transferable  visual  models  from  natural  language

supervision. In: International conference on machine learning, PMLR, pp 8748–8763

Ramesh A, Dhariwal P, Nichol A, et al (2022) Hierarchical text-conditional image generation with clip latent.

Preprint at arXiv:2204.06125 1(2):3

Rasul K, Ashok A, Williams AR, et al (2024) Lag-llama: Towards foundation models for probabilistic time

series forecasting. Preprint at arXiv:2310.08278

Rasul  K,  Seward  C,  Schuster  I,  et  al  (2021) Autoregressive  denoising  diffusion  models  for  multivariate 
probabilistic  time  series  forecasting.  In:  International  Conference  on  Machine  Learning,  PMLR,  pp 
8857–8868

Ribeiro MT, Singh S, Guestrin C (2016) " why should i trust you?" explaining the predictions of any classi-
fier. In: Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and 
data mining, pp 1135–1144

Rombach  R,  Blattmann A,  Lorenz  D,  et  al  (2022)  High-resolution  image  synthesis  with  latent  diffusion 
models. In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp 
10684–10695

---

<!-- PAGE 91 -->

Page 91 of 95  216

Rosenbaum PR, Rubin DB (1983) The central role of the propensity score in observational studies for causal

effects. Biometrika 70(1):41–55

Rossi  E,  Chamberlain  B,  Frasca  F,  et  al  (2020)  Temporal  graph  networks  for  deep  learning  on  dynamic

graphs. In: ICML 2020 Workshop on Graph Representation Learning

Rumelhart DE, Hinton GE, Williams RJ (1986) Learning representations by back-propagating errors. Nature

323(6088):533–536

Runge J, Nowack P, Kretschmer M, et al (2019) Detecting and quantifying causal associations in large non-

linear time series datasets. Sci Adv 5(11):eaau4996

Saharia C, Chan W, Saxena S et al (2022) Photorealistic text-to-image diffusion models with deep language

understanding. Adv Neural Inf Process Syst 35:36479–36494

ŞAHiN E, Arslan NN, Özdemir D (2024) Unlocking the black box: an in-depth review on interpretability,

explainability, and reliability in deep learning. Neural Computing and Applications pp 1–107

Sankaranarayanan  S,  Balaji Y,  Castillo  CD,  et  al  (2018)  Generate  to  adapt: Aligning  domains  using  gen-
erative adversarial networks. In: Proceedings of the IEEE conference on computer vision and pattern 
recognition, pp 8503–8512

Scarselli F, Gori M, Tsoi AC et al (2008) The graph neural network model. IEEE Trans Neural Networks

20(1):61–80

Schölkopf  B,  Locatello  F,  Bauer  S  et  al  (2021)  Toward  causal  representation  learning.  Proc  IEEE

109(5):612–634

Shabani MA, Abdi AH, Meng L, et al (2023) Scaleformer: Iterative multi-scale refining transformers for time 
series forecasting. In: The Eleventh International Conference on Learning Representations,  h t t p s : / / o p e 
n r e v i e w . n e t / f o r u m ? i d = s C r n l l C t j o E

Shafer G (1976) A Mathematical Theory of Evidence. Princeton University Press, Princeton
Sharma N, Mangla M, Mohanty SN et al (2021) Employing stacked ensemble approach for time series fore-

casting. Int J Inf Technol 13:2075–2080

Sharma K, Dwivedi YK, Metri B (2022) Incorporating causality in energy consumption forecasting using

deep neural networks. Annals of Operations Research pp 1–36

Shen  L,  Chen  W,  Kwok  J  (2024)  Multi-resolution  diffusion  models  for  time  series  forecasting.  In:  The

Twelfth International Conference on Learning Representations

Shen L, Kwok J (2023) Non-autoregressive conditional diffusion models for time series prediction. In: Inter-

national Conference on Machine Learning, PMLR, pp 31016–31029

Shi X, Chen Z, Wang H, et al (2015) Convolutional LSTM network: a machine learning approach for precipi-

tation nowcasting. Adv Neural Inform Process Syst 28

Shih SY, Sun FK, Hy Lee (2019) Temporal pattern attention for multivariate time series forecasting. Mach

Learn 108:1421–1441

Shu Y, Lampos V (2024) Deformtime: Capturing variable dependencies with deformable attention for time

series forecasting. Preprint at arXiv:2406.07438

Smyl  S  (2020) A  hybrid  method  of  exponential  smoothing  and  recurrent  neural  networks  for  time  series

forecasting. Int J Forecast 36(1):75–85

Smyl S, Oreshkin BN, Pełka P, et al (2024) Any-quantile probabilistic forecasting of short-term electricity

demand. Preprint at arXiv:2404.17451

Sohl-Dickstein J, Weiss E, Maheswaranathan N, et al (2015) Deep unsupervised learning using nonequilib-
rium thermodynamics. In: International conference on machine learning, PMLR, pp 2256–2265
Song Y, Ermon S (2019) Generative modeling by estimating gradients of the data distribution. Adv Neural

Inform Process Syst 32

Song  C,  Lin Y,  Guo  S,  et  al  (2020)  Spatial-temporal  synchronous  graph  convolutional  networks: A  new 
framework for spatial-temporal network data forecasting. In: Proceedings of the AAAI conference on 
artificial intelligence, pp 914–921

Song Y, Sohl-Dickstein J, Kingma DP, et al (2021) Score-based generative modeling through stochastic dif-
ferential equations. In: International Conference on Learning Representations,  h t t p s : / / o p e n r e v i e w . n e t / f 
o r u m ? i d = P x T I G 1 2 R R H S

Soyiri IN, Reidpath DD (2013) An overview of health forecasting. Environ Health Prev Med 18:1–9
Sparks AH, Carroll J, Goldie J, et al (2020) Bomrang: Australian government bureau of meteorology (BOM)

data client. R package version 07.0 https://CRAN.R-project.org/package=bomrang

Srivastava N, Hinton G, Krizhevsky A et al (2014) Dropout: a simple way to prevent neural networks from

overfitting. J Mach Learn Res 15(1):1929–1958

Štěpnička M, Burda M (2017) On the results and observations of the time series forecasting competition cif

2016. In: 2017 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), IEEE, pp 1–6

---

<!-- PAGE 92 -->

216  Page 92 of 95

Sui M, Zhang C, Zhou L et al (2024) An ensemble approach to stock price prediction using deep learning and 
time series models. 2024 IEEE 6th International Conference on Power. IEEE, Intelligent Computing 
and Systems (ICPICS), pp 793–797

Sun F, Hao W, Zou A, et al (2024a) A survey on spatio-temporal series prediction with deep learning: tax-

onomy, applications, and future directions. Neural Computing and Applications pp 1–25

Sun Y, Xie Z, Chen D, et al (2024b) Hierarchical classification auxiliary network for time series forecasting.

Preprint at arXiv:2405.18975

Taieb SB, Bontempi G, Atiya AF et al (2012) A review and comparison of strategies for multi-step ahead

time series forecasting based on the NN5 forecasting competition. Expert Syst Appl 39(8):7067–7083
Tang P, Zhang W (2024) PDMLP: Patch-based decomposed MLP for long-term time series forecastin. Pre-

print at arXiv:2405.13575

Tashiro Y, Song J, Song Y et al (2021) CSDI: Conditional score-based diffusion models for probabilistic time

series imputation. Adv Neural Inf Process Syst 34:24804–24816

Tay Y, Dehghani M, Bahri D, et al (2020) Efficient transformers: a survey. ACM Comput Surv 55:1–28.  h t t p

s :  / / a p i  . s e m a n  t i c s  c h o l a  r . o r g  / C o r p u  s I D :  2 2 1 7 0 2 8 5 8

Thompson  PA  (1990)  An  MSE  statistic  for  comparing  forecast  accuracy  across  series.  Int  J  Forecast

6(2):219–227

Touvron H, Martin L, Stone K, et al (2023) LLAMA 2: Open foundation and fine-tuned chat models. Preprint

at arXiv:2307.09288

Truchan H, Kalfar C, Ahmadi Z (2024) LTBOOST: Boosted hybrids of ensemble linear and gradient algo-
rithms for the long-term time series forecasting. In: Proceedings of the 33rd ACM International Confer-
ence on Information and Knowledge Management, pp 2271–2281

Ulyanov D, Vedaldi A, Lempitsky V (2016) Instance normalization: The missing ingredient for fast styliza-

tion. Preprint at arXiv:1607.08022

Van Den Oord A, Dieleman S, Zen H, et al (2016) Wavenet: a generative model for raw audio. Preprint at

arXiv:1609.03499 12

Vapnik V, Golowich S, Smola A (1996) Support vector method for function approximation, regression esti-

mation and signal processing. Adv Neural Inform Process Syst 9

Vaswani A, Shazeer N, Parmar N, et al (2017) Attention is all you need. Adv Neural Inform Process Syst 30
Veličković P, Cucurull G, Casanova A, et al (2018) Graph attention networks. In: International Conference on

Learning Representations, https://openreview.net/forum?id=rJXMpikCZ

Wachter  S,  Mittelstadt  B,  Russell  C  (2017)  Counterfactual  explanations  without  opening  the  black  box:

Automated decisions and the GDPR. Harv JL Tech 31:841

Wang W, Li H, Ding Z et al (2023) Rethinking maximum mean discrepancy for visual domain adaptation. 
IEEE Transact Neural Netw Learn Syst 34(1):264–277. https://doi.org/10.1109/TNNLS.2021.3093468
Wang Z, Ruan S, Huang T et al (2024) A lightweight multi-layer perceptron for efficient multivariate time

series forecasting. Knowl-Based Syst 288:111463

Wang L, Adiga A, Chen J, et al (2022b) Causalgnn: Causal-based graph neural networks for spatio-temporal 
epidemic forecasting. In: Proceedings of the AAAI conference on artificial intelligence, pp 12191–12199
Wang  J,  Jatowt A, Yoshikawa  M  (2022a)  Timebert:  Extending  pre-trained  language  representations  with

temporal information. Preprint at arXiv:2204.13032

Wang  Z,  Kong  F,  Feng  S,  et  al  (2024d)  Is  mamba  effective  for  time  series  forecasting?  Preprint  at

arXiv:2403.11144

Wang Z, Miliou I, Samsten I, et al (2023b) Counterfactual explanations for time series forecasting. In: 2023

IEEE International Conference on Data Mining (ICDM), IEEE, pp 1391–1396

Wang Y, Wu H, Dong J, et al (2024c) Timexer: Empowering transformers for time series forecasting with 
exogenous variables. In: The Thirty-eighth Annual Conference on Neural Information Processing Sys-
tems, https://openreview.net/forum?id=INAeUQ04lT

Wang S, Wu H, Shi X, et al (2024a) Timemixer: Decomposable multiscale mixing for time series forecasting.

International Conference on Learning Representations

Wang X, Zhou T, Wen Q, et al (2024b) Card: Channel aligned robust blend transformer for time series fore-

casting. In: The Twelfth International Conference on Learning Representations

Wei  C,  Niu  C,  Tang  Y  et  al  (2022)  NPENAS:  Neural  predictor  guided  evolution  for  neural  architecture

search. IEEE Transact Neural Netw Learn Syst 34(11):8441–8455

Wen R, Torkkola K, Narayanaswamy B, et al (2017) A multi-horizon quantile recurrent forecaster. Preprint

at arXiv:1711.11053

---

<!-- PAGE 93 -->

Page 93 of 95  216

Wen Q, Zhou T, Zhang C, et al (2023) Transformers in time series: A survey. In: Elkind E (ed) Proceedings 
of the Thirty-Second International Joint Conference on Artificial Intelligence, IJCAI-23. International 
Joint Conferences on Artificial Intelligence Organization, pp 6778–6786,  h t t p s : / / d o i . o r g / 1 0 . 2 4 9 6 3 / i j c a 
i . 2 0 2 3 / 7 5 9     , (survey Track)

Winters PR (1960) Forecasting sales by exponentially weighted moving averages. Manage Sci 6(3):324–342
Wolpert DH (1992) Stacked generalization. Neural Netw 5(2):241–259
Wong  SC,  Gatt A,  Stamatescu  V,  et  al  (2016)  Understanding  data  augmentation  for  classification:  when 
to  warp?  In:  2016  international  conference  on  digital  image  computing:  techniques  and  applications 
(DICTA), IEEE, pp 1–6

Woo G, Liu C, Kumar A, et al (2024) Unified training of universal time series forecasting transformers. In:

Forty-first International Conference on Machine Learning

Wu Z, Huang NE (2009) Ensemble empirical mode decomposition: a noise-assisted data analysis method.

Adv Adapt Data Anal 1(01):1–41

Wu  B, Wang  L  (2024) Two-stage  decomposition  and  temporal  fusion  transformers  for  interpretable  wind

speed forecasting. Energy 288:129728

Wu H, Xu J, Wang J et al (2021) Autoformer: Decomposition transformers with auto-correlation for long-

term series forecasting. Adv Neural Inf Process Syst 34:22419–22430

Wu B, Yu S, Peng L et al (2024) Interpretable wind speed forecasting with meteorological feature exploring

and two-stage decomposition. Energy 294:130782

Wu  Z,  Gong  Y,  Zhang  A  (2024b)  Dtmamba:  Dual  twin  mamba  for  time  series  forecasting.  Preprint  at

arXiv:2405.07022

Wu H, Hu T, Liu Y, et al (2023) Timesnet: Temporal 2d-variation modeling for general time series analysis.

International Conference on Learning Representations

Xiong Q, Tang K, Ma M, et al (2024) Tdt loss takes it all: Integrating temporal dependencies among targets

into non-autoregressive time series forecasting. Preprint at arXiv:2406.04777

Xu B, Sheng Y, Li P et al (2019) Causes and classification of EMD mode mixing. Vibroengineering Procedia

22:158–164

Xua B, Yang G (2024) Interpretability research of deep learning: a literature survey. Information Fusion p

102721

Xu Z, Bian Y, Zhong J, et al (2024b) Beyond trend and periodicity: Guiding time series forecasting with

textual cues. Preprint at arXiv:2405.13522

Xu  X,  Chen  Z,  Xu  D,  et  al  (2022)  Mixing  signals:  Data  augmentation  approach  for  deep  learning  based

modulation recognition. Preprint at arXiv:2204.03737

Xue  H,  Salim  FD  (2023)  Promptcast:  a  new  prompt-based  learning  paradigm  for  time  series  forecasting.

IEEE Transactions on Knowledge and Data Engineering

Xu X, Liang Y, Huang B, et al (2024a) Integrating mamba and transformer for long-short range time series

forecasting. Preprint at arXiv:2404.14757

Xu Z, Zeng A, Xu Q (2024) Fits: Modeling time series with [CDATA[10 k ]]10k parameters
Yang Y, Yang Y (2020) Hybrid method for short-term time series forecasting based on EEMD. IEEE Access

8:61915–61928

Yang Y, Jin M, Wen H, et al (2024a) A survey on diffusion models for time series and Spatio-temporal data.

Preprint at arXiv:2404.18886

Yang F, Li X, Wang M, et al (2023a) Waveform: Graph enhanced wavelet learning for long sequence fore-
casting of multivariate time series. In: Proceedings of the AAAI Conference on Artificial Intelligence, 
pp 10754–10761

Yan T, Gong H, Yongping H, et al (2024) Probabilistic time series modeling with decomposable denoising 
diffusion model. In: Salakhutdinov R, Kolter Z, Heller K, et al (eds) Proceedings of the 41st Interna-
tional Conference on Machine Learning, Proceedings of Machine Learning Research, vol 235. PMLR, 
pp 55759–55777,  h t t p s :   /  / p r o c e e d i n g  s .  m l  r . p  r e  s s /  v 2  3 5 /  y a n   2 4 b . h t m l

Yang M, Xu C, Bai Y, et al (2023b) Investigating black-box model for wind power forecasting using local 
interpretable model-agnostic explanations algorithm: why should a model be trusted? CSEE J Power 
Energy Syst

Yang Y, Zhu Q, Chen J (2024b) Vcformer: Variable correlation transformer with inherent lagged correlation 
for multivariate time series forecasting. In: Larson K (ed) Proceedings of the Thirty-Third International 
Joint Conference on Artificial Intelligence, IJCAI-24. International Joint Conferences on Artificial Intel-
ligence Organization, pp 5335–5343, https://doi.org/10.24963/ijcai.2024/590, (Main Track)

Yan S, Xiong Y, Lin D (2018) Spatial temporal graph convolutional networks for skeleton-based action rec-

ognition. In: Proceedings of the AAAI conference on artificial intelligence

---

<!-- PAGE 94 -->

216  Page 94 of 95

Yan T, Zhang H, Zhou T, et al (2021) Scoregrad: Multivariate probabilistic time series forecasting with con-

tinuous energy-based generative models. Preprint at arXiv:2106.10121

Ye J, Zhang W, Yi K, et al (2024) A survey of time series foundation models: Generalizing time series repre-

sentation with large language mode. Preprint at arXiv:2405.02358

Yi K, Zhang Q, Fan W, et al (2024) Frequency-domain mlps are more effective learners in time series fore-

casting. Adv Neural Inform Process Syst 36

Yuan X, Qiao Y (2024) Diffusion-TS: Interpretable diffusion for general time series generation. In: The Twelfth

International Conference on Learning Representations, https://openreview.net/forum?id=4h1apFjO99

Yu C, Wang F, Shao Z, et al (2023) Dsformer: A double sampling transformer for multivariate time series 
long-term prediction. In: Proceedings of the 32nd ACM international conference on information and 
knowledge management, pp 3062–3072

Yu G, Zou J, Hu X, et al (2024) Revitalizing multivariate time series forecasting: Learnable decomposition

with inter-series dependencies and intra-series variations modeling. Int Conf Mach Learn

Zeng A, Chen M, Zhang L, et al (2023) Are transformers effective for time series forecasting? In: Proceedings

of the AAAI conference on artificial intelligence, pp 11121–11128

Zeng C, Liu Z, Zheng G, et al (2024) C-mamba: Channel correlation enhanced state space models for multi-

variate time series forecasting. Preprint at arXiv:2406.05316

Zhang S, Chen Y, Xiao J et al (2021) Hybrid wind speed forecasting model based on multivariate data sec-
ondary decomposition approach and deep learning algorithm with attention mechanism. Renew Energy 
174:688–704

Zhang S, Chen Y, Zhang W et al (2021) A novel ensemble deep learning model with dynamic error correction

and multi-objective ensemble pruning for time series forecasting. Inf Sci 544:427–445

Zhang Q, Chang J, Meng G, et al (2020) Spatio-temporal graph structure learning for traffic forecasting. In:

Proceedings of the AAAI conference on artificial intelligence, pp 1177–1185

Zhang X, Chowdhury RR, Gupta RK, et al (2024d) Large language models for time series: A survey. In: 
Larson K (ed) Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, 
IJCAI-24.  International  Joint  Conferences  on  Artificial  Intelligence  Organization,  pp  8335–8343, 
https://doi.org/10.24963/ijcai.2024/921, (Survey Track)

Zhang Y, Ma L, Pal S, et al (2024e) Multi-resolution time-series transformer for long-term forecasting. In:

International Conference on Artificial Intelligence and Statistics, PMLR, pp 4222–4230

Zhang M, Sun Y, Liang F (2024c) Sparse deep learning for time series data: theory and applications. Adv

Neural Inform Process Syst 36

Zhang D, Wang Y (2024) Adaptive extraction network for multivariate long sequence time-series forecasting.

Preprint at arXiv:2405.12038

Zhang K, Wen Q, Zhang C, et al (2024a) Self-supervised learning for time series analysis: Taxonomy, prog-

ress, and prospects. IEEE Transactions on Pattern Analysis and Machine Intelligence

Zhang Y, Yan J (2023) Crossformer: Transformer utilizing cross-dimension dependency for multivariate time

series forecasting. In: The eleventh international conference on learning representations

Zhang J, Zheng Y, Qi D (2017) Deep spatio-temporal residual networks for citywide crowd flows prediction.

In: Proceedings of the AAAI conference on artificial intelligence

Zhang K, Zou X, Tang Y (2024b) Caformer: Rethinking time series analysis from causal perspective. Preprint

at arXiv:2403.08572

Zhan T, He Y, Li Z, et al (2024) Time evidence fusion network: Multi-source view in long-term time series

forecasting. Preprint at arXiv:2405.06419

Zhao S, Ma T, Ermon S (2020) Individual calibration with randomized forecasting. In: International Confer-

ence on Machine Learning, PMLR, pp 11387–11397

Zheng C, Fan X, Wang C, et al (2020) Gman: A graph multi-attention network for traffic prediction. In: Pro-

ceedings of the AAAI conference on artificial intelligence, pp 1234–1241

Zhou T, Ma Z, Wen Q, et al (2022) Fedformer: Frequency enhanced decomposed transformer for long-term

series forecasting. In: International conference on machine learning, PMLR, pp 27268–27286

Zhou T, Niu P, Wang X, et al (2023) One fits all: Power general time series analysis by pretrained LM. In: 
Thirty-seventh Conference on Neural Information Processing Systems,  h t t p s : / / o p e n r e v i e w . n e t / f o r u m ? 
i d = g M S 6 F V Z v m F

Zhou H, Zhang S, Peng J, et al (2021) Informer: Beyond efficient transformer for long sequence time-series

forecasting. In: Proceedings of the AAAI conference on artificial intelligence, pp 11106–11115

Publisher's Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.

---

<!-- PAGE 95 -->

Authors and Affiliations

Jongseon Kim1,4 · Hyungjoon Kim1,5 · HyunGi Kim2 · Dongjun Lee1 · Sungroh Yoon1,2,3

Page 95 of 95  216

Sungroh Yoon

sryoon@snu.ac.kr

Jongseon Kim
hallooawooye@snu.ac.kr

Hyungjoon Kim
khjn81@snu.ac.kr

HyunGi Kim
rlagusrl0128@snu.ac.kr

Dongjun Lee
elite1717@snu.ac.kr

1

Interdisciplinary Program in Artificial Intelligence, Seoul National University, Seoul, South 
Korea

2  Department of Electrical and Computer Engineering, Seoul National University, Seoul, South

Korea

3  AIIS, ASRI, and INMC, Seoul National University, Seoul, South Korea
4  R&D Department, LG Chem, Seoul, South Korea
5  R&D Department, Samsung SDI, Yongin, South Korea

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Artificial Intelligence Review (2025) 58:216
https://doi.org/10.1007/s10462-025-11223-9
A comprehensive survey of deep learning for time series
forecasting: architectural diversity and open challenges
Jongseon Kim1,4 · Hyungjoon Kim1,5 · HyunGi Kim2 · Dongjun Lee1 · Sungroh Yoon1,2,3
Accepted: 4 April 2025 / Published online: 23 April 2025
© The Author(s) 2025
Abstract
Time series forecasting is a critical task that provides key information for decision-making
across various fields, such as economic planning, supply chain management, and medical
diagnosis. After the use of traditional statistical methodologies and machine learning in
the past, various fundamental deep learning architectures such as MLPs, CNNs, RNNs,
and GNNs have been developed and applied to solve time series forecasting problems.
However, the structural limitations caused by the inductive biases of each deep learning
architecture constrained their performance. Transformer models, which excel at handling
long-term dependencies, have become significant architectural components for time series
forecasting. However, recent research has shown that alternatives such as simple linear
layers can outperform Transformers. These findings have opened up new possibilities for
using diverse architectures, ranging from fundamental deep learning models to emerging
architectures and hybrid approaches. In this context of exploration into various models,
the architectural modeling of time series forecasting has now entered a renaissance. This
survey not only provides a historical context for time series forecasting but also offers
comprehensive and timely analysis of the movement toward architectural diversification.
By comparing and re-examining various deep learning models, we uncover new perspec-
tives and present the latest trends in time series forecasting, including the emergence of
hybrid models, diffusion models, Mamba models, and foundation models. By focusing on
the inherent characteristics of time series data, we also address open challenges that have
gained attention in time series forecasting, such as channel dependency, distribution shift,
causality, and feature extraction. This survey explores vital elements that can enhance
forecasting performance through diverse approaches. These contributions help lower entry
barriers for newcomers by providing a systematic understanding of the diverse research
areas in time series forecasting (TSF), while offering seasoned researchers broader per-
spectives and new opportunities through in-depth exploration of TSF challenges.
Keywords Time series forecasting · Deep learning · Foundation model · Distribution
shift · Causality
Jongseon Kim and Hyungjoon Kim have contributed equally to this work.
Extended author information available on the last page of the article
1 3

216 Page 2 of 95 J. Kim et al.
1 Introduction
Time series forecasting (TSF) is a task that predicts future values based on sequential his-
torical data (Cryer 1986). It is utilized as a key decision-making tool in various fields, such
as economics and finance, supply chain management, transportation, energy, weather, and
healthcare (Danese and Kalchschmidt 2011; Abu-Mostafa and Atiya 1996; Alghamdi et al
2019; Nti et al 2020; Dimri et al 2020; Soyiri and Reidpath 2013). Such applications offer
various opportunities, including cost reduction, increased efficiency, and enhanced com-
petitiveness (Danese and Kalchschmidt 2011). The diversity and complexity of time series
data make forecasting challenging. In addition to apparent information, hidden patterns and
irregular values pose challenges in learning temporal dependencies (Chen et al 2024d).
In multivariate problems, additional factors such as channel correlation make the task
even more difficult (Sect. 2.1). Furthermore, time series data exhibits different characteris-
tics depending on the domain, and the various times and environments in which the series
is collected result in significantly different patterns (Sect. 2.3). Because of this, TSF prob-
lems exhibit limited model generalizability, requiring diverse architectures and approaches.
The increasingly complicated TSF problems are presenting researchers with growing chal-
lenges, which has recently led to the active development of new methodologies and algo-
rithms to address these issues (Lim and Zohren 2021).
TSF is closely connected to core AI challenges, and solving these problems plays a
crucial role in advancing the field of AI. For instance, the generalization of AI models is
essential for ensuring stable performance on new data. However, time series data presents
unique characteristics and domain-specific patterns that make generalization particularly
challenging (Han et al 2023b). Solutions to generalization in TSF provide new insights that
are applicable to other fields, such as Natural Language Processing (NLP) and Computer
Vision (CV). The distribution of real-world time series data can change over time, and mod-
els must effectively handle these changes (Sect. 5.2). TSF plays a crucial role in addressing
distribution shift issues, and the techniques developed to solve these problems can extend
to other AI domains, such as image, video, and NLP. Moreover, attempts to understand
models are crucial for improving their trustworthiness in real-world applications (Han et al
2023a). In mission-critical fields such as healthcare and finance, the explainability of time
series prediction models is essential. For example, explaining how stock price predictions or
patient vital sign forecasts are made can help users better understand and trust the model’s
decisions. Thus, TSF research in explainability provides practical solutions for other AI
applications (Sect. 5.6). Recently, TSF has evolved beyond simple forecasting, establish-
ing itself as a practical platform for addressing key AI challenges. Solving these problems
within TSF highlights the potential for AI to develop in a complementary and synergistic
way.To address these diverse challenges and recent approaches, our survey is organized as
illustrated in Fig. 1, which outlines the overall framework.
Figure 2 shows the number of papers on time series forecasting presented at major AI and
machine learning conferences. This explosive increase demonstrates the growing impor-
tance of TSF research in the AI and machine learning fields. As various studies addressing
time series forecasting problems are being actively conducted, survey papers are also being
frequently published. Over time, numerous survey papers have systematically organized the
vast landscape of TSF, offering in-depth research that has provided valuable guidance and
direction for researchers. However, existing survey papers still have room for improvement,
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 3 of 95 216
Fig. 1 Overview of this survey
1 3

216 Page 4 of 95 J. Kim et al.
Fig. 2 Number of top-tier AI and ML conference papers on time series forecasting
particularly in addressing the inevitable increase in model diversity and the open challenges
in the field, as summarized in Table 1. This survey aims to reorganize the extensive dis-
course on TSF by providing essential and comprehensive information. At the same time, it
explores model diversity to deliver the latest TSF trends and uniquely highlights open chal-
lenges, clearly presenting them to readers.
Models for TSF have undergone various stages of development over an extended period.
In the past, statistical methods based on moving averages were predominantly used, which
later evolved into traditional approaches such as Exponential Smoothing and ARIMA (Box
et al 1970). Machine learning techniques such as Tree Models (Quinlan 1986) and Support
Vector Machines (SVM) (Cortes 1995) have also been frequently used, but they had limita-
tions in learning complex nonlinear patterns (Sect. 3.1). With the increase in available data
and advancements in hardware computing power, various deep learning architectures such
as MLPs (Rumelhart et al 1986), RNNs (Hopfield 1982), CNNs (LeCun et al 1998), and
GNNs (Scarselli et al 2008) were developed, enabling the learning of more complex pat-
terns. However, the performance of these early deep learning architectures was constrained
by their intrinsic designs. To overcome these structural limitations, variants such as Long
Short-Term Memory (LSTM) (Hochreiter and Schmidhuber 1997) and Temporal Convolu-
tional Networks (TCN) (Bai et al 2018) have been widely utilized (Sect. 3.2). Transform-
ers (Vaswani et al 2017), known for their ability to handle long-term dependencies, have
demonstrated excellent performance in natural language processing and have been naturally
extended to time series data as well. While Transformers have shown good performance in
TSF and become widely popular, recent cases have shown that simple linear models can
outperform Transformer models (Sect. 3.3). As a result, there has been a significant increase
in reconsidering fundamental deep learning methodologies, along with growing interest
in various architectures such as foundation models, diffusion models, and Mamba models
(Sects. 4.2, 4.3, 4.4, 4.5). The Transformer model continues to improve in performance and
still plays a significant role (Sect. 4.1). In this way, TSF has entered a renaissance of model-
ing, with various methodologies actively competing without being dominated by any single
approach (Fig. 3). In this context, this survey offers two major strengths that set it apart from
previous TSF survey papers.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 5 of 95  216
| )1202( nerhoZ |                             |             |               |                          | )4202( la te eY  narawseengA |
| ------------- | --------------------------- | ----------- | ------------- | ------------------------ | ---------------------------- |
|               |  la te sidineB  la te demhA |             |  la te inisaM | )4202( nehC              |                              |
| secnerefeR    |                             |             |               |  dna rejieM  la te gnaiL |  la te gnahZ                 |
|               |  la te neW                  |  la te nehC |               |                          |  dna ortaP                   |
 dna miL  la te uiL )b1202(  la te niL )a4202( )c4202( )d4202( )a4202(
|     | )2202( )2202( | )3202( )3202( | )3202( |     |     |
| --- | ------------- | ------------- | ------ | --- | --- |
 tnec krow
-eR
|     |     |     |     | ✓   | ✓ ✓ ✓ ✓ |
| --- | --- | --- | --- | --- | ------- |
segnellahc
 FST
| ✓   |     | ✓ ✓ |     |     |     |
| --- | --- | --- | --- | --- | --- |
-ra daorB  erutcetihc
weiver
| ✓   | ✓ ✓ ✓ | ✓   | ✓   |     |     |
| --- | ----- | --- | --- | --- | --- |
LD dna ,LM ,lacitsitats :sdohtem gnitsacerof suoirav fo noitazirogetaC ⋅
sisylana seires emit ni sMLL dna sledom noitadnuoF ot sehcaorppA ⋅
noitatupmoc lellarap dna ,gniledom ,gnissecorperp ni segnellahC ⋅
stnemevorpmi larutcetihcra dna snoitairav erutcurts remrofsnarT ⋅  suoirav morf segnellahc gnitsacerof ecneuqes gnol fo noitinfieD ⋅ sdohtem noitaulave ecnamrofrep dna metsys noitacfiissalc weN ⋅
ecnamrofrep dna snoitacilppa cfiiceps-niamod fo nosirapmoC ⋅
noitazimitpo dna ,noitacilppa ,noitatnemelpmi no senilediuG ⋅
seires emit ni sMLL rof seigolodohtem fo noitazirogetaC ⋅
| troppus noisiced rof ecnerefni lasuac dna ytilibaterpretnI ⋅ |     |     |     | sisylana seires emit ni sledom noitadnuof fo noitacilppA ⋅ |     |
| ------------------------------------------------------------ | --- | --- | --- | ---------------------------------------------------------- | --- |
seiduts esac htiw sledom gnitsacerof desab-noisuffiD ⋅
seires emit gnol ni segatnavda MSS no sisahpmE ⋅
sledom dirbyh dna serutcurts redoced–redocnE ⋅
sisylana seires emit ni sledom noisuffiD ⋅
spag ytiladom gnigdirb fo noitanalpxE ⋅
raenilnon dna raenil otni dezirogetaC ⋅
sledom laitneuqes peed nommoC ⋅
FST LD fo stnenopmoc yeK ⋅
FST laicnanfi/cimonocE ⋅
ytilibacilppa lacitcarP ⋅
gnitsacerof seires emit no srepap yevrus fo yrammuS 1 elbaT
sevitcepsrep
sucoF
|  :gninrael peed htiw gnitsacerof seires-emiT |                                             |  htiw gnitsacerof seires-emit ecneuqes gnoL |                                            |  :sisylana seires emit rof sledom noitadnuoF |                                                                                   |
| -------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------ | -------------------------------------------- | --------------------------------------------------------------------------------- |
|                                              |  :gnitsacerof seires emit rof gninrael peeD |                                             |  seires emit rof secnavda gninrael enihcaM |  seires-emit ni sledom noisuffid fo esir ehT | sledom noitadnuof seires emit fo yevrus A sledom ecaps etats fo yevrus :063-abmaM |
|  a :atad seires emit rof sdohtem tsaceroF    |  rof sledom laitneuqes peed no weiver A     |                                             | -acilppa seires-emit rof sledom noisuffiD  |                                              |  a :seires emit rof sledom egaugnal egraL                                         |
yevrus a :seires emit ni sremrofsnarT
yevrus erutaretil dna lairotut
atad seires emit gnitsacerof
yevrus a :gninrael peed
yevrus dna lairotut a
yevrus a :snoit
|     |     |     | gnitsacerof | gnitsacerof |     |
| --- | --- | --- | ----------- | ----------- | --- |
selcitrA yevrus a
|     | yevrus |     |     |     | yevrus |
| --- | ------ | --- | --- | --- | ------ |
1 3

J. Kim et al.
)deunitnoc(
1
elbaT
secnerefeR
-eR
FST
-ra
daorB
sucoF
selcitrA
tnec
segnellahc
erutcetihc
krow
weiver
✓
✓
✓
gnicudortni
,sledom
FST
fo
noitulove
eht
fo
weivrevo
evisneherpmoc
A
⋅
yevrus
sihT
serutcetihcra
evitavonni
htiw
gnola
,sksat
gnitsacerof
ni
segnellahc
nepo
lacitirc
fo
noissucsiD
⋅
meht
sserdda
ot
snoitulos
decnavda
216 Page 6 of 95
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 7 of 95 216
First, we focus on the inevitable diversification of architectures, providing a timely and
comprehensive view to understand the current trend of architecture diversification. Existing
TSF survey papers, such as (Wen et al 2023; Zhang et al 2024d; Lin et al 2024a; Meijer
and Chen 2024; Patro and Agneeswaran 2024a), focus on providing detailed analyses of
specific architectures but have limitations when it comes to broadly comparing diversi-
fied architectures, including newly emerging ones. This paper systematically compares
the developmental progress of various architectures (MLPs, CNNs, RNNs, GNNs, Trans-
former, Diffusion, foundation models, Mamba) and analyzes the strengths, weaknesses, and
contributions of each. In addition, it addresses the performance of hybrid models that com-
bine the strengths of multiple architectures, clearly highlighting key trends in TSF. With
these contributions, readers can effectively understand the continuously evolving trends and
directions of advancement in the field. Through this, it lowers the entry barrier for newcom-
ers to TSF and provides a comprehensive roadmap that opens up new research opportunities
for established researchers.
Second, we explore from the perspective of open challenges. Although numerous
advanced architectures have resolved many issues, the core challenges in TSF continue to
persist. In particular, issues such as channel correlation, distribution shifts, causality, and
feature extraction (Sect. 5) remain significant challenges that need to be addressed (Fig. 4).
This survey explores the latest methodologies aimed at addressing these challenges and
provides readers with valuable insights for problem-solving. While some existing surveys
address these TSF challenges, they often focus on only a few problems. In contrast, this
paper takes an issue-driven approach, deeply examining seven key TSF problems and orga-
nizing new solutions.
This survey covers the fundamental concepts of time series data and the problem defini-
tion of forecasting in Sect. 2, followed by an examination of the evolution of past meth-
odologies in Sect. 3. Section 4 analyzes the key features of the latest models, and finally,
Sect. 5, explores the open challenges in TSF and their solutions. Through this, readers will
gain a broad understanding of the past and present of TSF research and acquire new ideas
for future studies.
2 Background
In this section, before exploring time series forecasting models, we explain the definition
and key characteristics of time series data to provide the necessary background. We also
define the problem of time series forecasting tasks, discussing related datasets and evalu-
ation metrics. This establishes the basic concepts of time series forecasting and provides
preliminary information to help understand the models discussed in the following sections.
2.1 Time-series data
Time series data is a collection of sequential data points gathered at regular time intervals,
representing a series of observations of phenomena that change over time. This temporal
continuity allows for the understanding and analysis of phenomena that evolve according to
time order. Each data point represents the state or value at a specific moment, and through
the observation of these data points, various patterns such as long-term trends, seasonality,
1 3

J. Kim et al.
sledom
gnitsacerof
seires
emit
fo
noitulovE
3
.giF
216 Page 8 of 95
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 9 of 95 216
cyclicality, and irregularities can be recognized. These patterns provide valuable informa-
tion for predicting future values or detecting changes at critical moments. By extracting and
studying the meaningful information provided by time series data, researchers can develop
practical applications to address challenges in various disciplines.
Characteristics of time series data
Time series data encapsulates various characteristics that play a critical role in explaining
the diverse patterns and fluctuations within time series. Understanding these characteristic
elements is essential for analyzing and predicting data. The key properties are explained in
Fig. 5.
In time series data, the above features frequently appear in a mixed form. Therefore,
decomposition is commonly used to separate the components for detailed analysis, or dis-
tribution shift alleviation methods are widely applied. Many time series datasets provide
information on multivariate variables. Sometimes, these data provide additional information
that univariate data cannot, and it is important to understand this for many problems. The
main properties are explained in Fig. 6.
These additional features convey the complexity of the real world in greater detail and
sometimes provide reasons for significant pattern changes. Considering this information can
lead to more precise time series analysis and forecasting.
2.2 Time-series forecasting
Time series forecasting involves analyzing historical time-series data to predict future val-
ues. This process entails analyzing inherent temporal patterns in the data, such as trends and
seasonality, using past observations to estimate future values. The goal of time series fore-
casting is to support decision-making by providing information about an uncertain future,
such as predicting future demand changes or fluctuations in prices. Time series forecast-
ing can employ various methodologies, including statistical methods, machine learning,
and deep learning. These methodologies focus on capturing the characteristics of data as it
changes over time.
Univariate time series forecasting (UTSF)
Univariate forecasting refers to making predictions using only one variable. For exam-
ple, predicting the next day’s temperature based solely on past temperature data from a
weather station is a univariate forecast. The advantage of univariate forecasting is that the
models are simple and computationally efficient. Since the data consists of a single variable,
the model is relatively straightforward and easy to understand, making data collection and
management easier. However, it may only utilize limited information as it cannot account
for important external factors or interactions between different variables.
xˆ t+1:t+h =f(x t p:t ) (1)
−
The formula representing UTSF is shown in Eq. (1). The model takes the past p+1 time
steps, specifically the data from t
−
p to t, as input to make predictions. Here, xˆ t+1:t+h
represents the predicted values from t+1 to t+h. Single-step forecasting predicts only
one value when h=1, while multi-step forecasting predicts multiple values when h>1.
Multivariate Time Series Forecasting (MTSF)
1 3

216 Page 10 of 95 J. Kim et al.
Fig. 4 Overview of latest open challenges in time series forecasting
Multivariate forecasting involves making predictions using multiple variables simultane-
ously. For instance, in weather forecasting, predicting the next day’s temperature by con-
sidering various variables such as temperature, humidity, and wind speed is an example of
multivariate forecasting. By incorporating interactions and correlations between multiple
variables, multivariate forecasting can capture complex relationships, offering higher pre-
dictive accuracy. However, these models tend to be more complex, require more data, and
can be more challenging to handle, increasing the risk of overfitting.
To incorporate other influencing variables, we can extend the model to a multivariate
approach.
Xˆ
t+1:t+h
=f(Xt
p:t
) (2)
−
The formula representing MTSF is shown in Eq. (2). Xt p:t is a set of vectors over the
−
past p+1 time steps, where each vector contains the values of multiple variables at time t
. This model takes multiple variables from the past p+1 time steps, specifically Xt p:t, as
input to generate the multivariate predicted values from t+1 to t+h, denoted as Xˆ t − +1:t+h
. This multivariate approach allows for more comprehensive modeling by considering both
the target variable’s history and the effects of other relevant factors. Figure 7 illustrates how
a multivariate forecasting model uses a past lookback window to predict future intervals.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 11 of 95 216
Fig. 5 Properties of time series data
Short-term time series forecasting (STSF)
Short-term time series forecasting focuses on predictions for the near future, making it
suitable for tasks that require quick responses, such as immediate operational planning or
short-term decision-making. The models are simple, making them easy to train and imple-
ment, and they often demonstrate relatively high accuracy. However, because the forecast
range is short, it cannot capture long-term trends or complex variations, which limits its
applicability.
Long-term time series forecasting (LTSF)
Long-term time series forecasting deals with predictions for the distant future, with fore-
cast horizons increasingly extending to several months, years, or beyond. It is valuable for
long-term strategy planning, investment decisions, and policy-making, addressing many
1 3

216 Page 12 of 95 J. Kim et al.
Fig. 6 Properties of multivariate time series data
Fig. 7 Diagram of multivariate time series forecasting
real-world problems. By identifying long-term trends and cycles, organizations can prepare
accordingly, highlighting its significance. However, predicting the distant future is challeng-
ing, and extensive research is being conducted to improve accuracy.
2.3 Time series forecasting datasets
Models for Time Series Forecasting (TSF) are primarily trained and evaluated using open
benchmark datasets. Open datasets offer data that has already been collected across vari-
ous fields, allowing researchers to use them without going through separate data collection
processes. Additionally, researchers can objectively compare the performance of different
models and convincingly demonstrate the contributions of their developed models.
Datasets frequently used by time series forecasting models in various domains, such as
energy consumption, traffic, weather, exchange rates, and disease outbreaks, are listed in
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 13 of 95 216
Table 2. These time series datasets are typically collected in real-time via sensors, recorded
as transaction logs in financial markets, accumulated as server logs, or gathered through
periodic surveys.
Time series data exist across a wide range of domains, each exhibiting unique char-
acteristics. This diversity is due to the nature of time series data, which addresses real-
world problems in various fields and can display highly varied patterns depending on time
and environmental factors. For example, stock price data often show long-term upward or
downward trends. Stock market fluctuations tend to move in specific directions over the
long term due to complex influences such as economic conditions, corporate performance,
and policy changes. In contrast, electricity consumption data exhibit pronounced periodicity
throughout the day, with higher consumption during daytime hours and lower consumption
at night. There are also seasonal patterns, with different consumption rates during summer
and winter.
Monash Time Series Forecasting Archive (Godahewa et al 2021l) points out that there
is no comprehensive time series dataset archive and thus provides a thorough time series
repository. This repository offers 30 datasets for real-world data and competition purposes,
covering various domains such as energy, economics, nature, and sales. Details are specified
in Table 3.
Time series data exhibit a greater variety of domain-specific characteristics compared
to Natural Language Processing (NLP). These differences in dataset characteristics make
time series forecasting problems more diverse and complex, reducing the generalizability
of time series forecasting models. Consequently, developing foundation models for TSF is
more challenging compared to NLP. Time series data lack the well-designed vocabulary and
grammar found in NLP, and obtaining vast amounts of data is more difficult than in fields
like Computer Vision (CV) or NLP. In the CV field, there are general benchmark datasets
such as MNIST and ImageNet, while in NLP, there are datasets like GLUE (General Lan-
guage Understanding Evaluation) and SQuAD (Stanford Question Answering Dataset). In
contrast, the time series analysis field lacks large-scale general benchmark datasets and
large-scale challenges like those in image and language domains. The most famous time
series forecasting competition is the M-Competitions, which started in 1982 and has only
been held six times to date. The paper “Time Series Dataset Survey for Forecasting with
Deep Learning” (Hahn et al 2023) highlights the lack of general benchmark datasets for
TSF and analyzes the statistical characteristics of datasets across various domains, cluster-
ing them to provide easily accessible information for researchers. We do not delve into
the characteristics of the datasets in detail, but instead provide a brief overview of the key
datasets. Recently, the development of foundation models for time series has begun, leading
to the gradual emergence of general datasets for TSF. Details about TSF foundation models
will be discussed in Sect. 4.3.
2.4 Evaluation metrics
The evaluation metrics used in TSF play a crucial role in objectively comparing and assess-
ing model performance. Common metrics for deterministic models include Mean Absolute
Error (MAE) and Mean Squared Error (MSE), which are easy to use because they allow
intuitive comparisons of prediction errors. On the other hand, probabilistic models that can
reflect uncertainty typically use Continuous Ranked Probability Score (CRPS), which mea-
1 3

J. Kim et al.
sledom
gnitsacerof
seires
emit
ni
desu
yltneuqerf
stesataD
2
elbaT
ecruoS
ycneuqerF
noitpircseD
htgneL
lennahC
tesataD
tesataDTE
snim
51
sraey
2
rof
anihC
ni
seitnuoc
owt
morf
atad
erutarepmet
remrofsnart
yticirtcelE
086,96
7
2mTTE
,1mTTE
tesataDTE
ylruoH
sraey
2
rof
anihC
ni
seitnuoc
owt
morf
atad
erutarepmet
remrofsnart
yticirtcelE
024,71
7
2hTTE
,1hTTE
evihcrA
ICU
ylruoH
4102
ot
2102
morf
stneilc
fo
atad
noitpmusnoc
yticirtcele
ylruoH
403,62
123
yticirtcelE
SMeP
ylkeew
,ylruoH
shtnom
84
rof
syaweerf
aera
yaB
ocsicnarF
naS
no
setar
ycnapucco
daor
ylruoH
445,71
268
cffiarT
)6102–5102(
aneJ
CGB
snim
01
ynamreG
ni
)erutarepmet
,ytidimuh
,.g.e(
atad
lacigoloroeteM
696,25
12
rehtaeW
etairavitluM
yliaD
6102
ot
0991
morf
seirtnuoc
thgie
fo
setar
egnahcxe
yliaD
8857
8
egnahcxE
seireS
emiT ataD
weiVulF
CDC
ylkeeW
CDC
.S.U
eht
morf
atad
ssenlli
ekil-azneuflni
ylkeeW
669
7
ILI
216 Page 14 of 95
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 15 of 95 216
sures the accuracy of distribution forecasts by evaluating the difference between predicted
and actual distributions (Matheson and Winkler 1976). However, the limitations of these
traditional evaluation metrics have been noted, leading to the proposal of various perfor-
mance metrics (Thompson 1990).
The distinct characteristics of time series data necessitate the use of diverse metrics in
TSF. It is essential to assess not only the magnitude of errors but also how well the model
learns the temporal patterns and various features of time series data. Table 4 categorizes
evaluation metrics by type and explains each metric.
Error-based metrics for deterministic models measure the difference between predicted
and actual values. Explained variance metrics assess how well the model explains the vari-
ance of the data (Chicco et al 2021). These metrics evaluate how well the model captures key
patterns such as seasonality or trends in the data, thereby aiding in the structural understand-
ing of the predictions. Error metrics focus on accuracy, but they do not assess overfitting,
whereas explained variance evaluates the model’s generalization ability. Model selection
metrics help identify the optimal model (Portet 2020). These metrics take into account fac-
tors such as sample size and the number of parameters, playing a key role in selecting the
optimal model. Thus, they are particularly useful for choosing the most appropriate model
for a given dataset. For instance, in noisy environments, MAE is preferred over MSE due
to its reduced sensitivity to outliers. Additionally, when evaluating non-stationary data, it is
important to use metrics that effectively capture changes in trends and seasonality. In such
cases, cumulative error-based metrics or explained variance metrics can be useful.
Probabilistic model evaluation metrics, on the other hand, account for uncertainty,
enabling the assessment of both the confidence and variability of predictions. These met-
rics help evaluate not only the predicted values but also the uncertainty surrounding them.
Beyond basic error-based metrics, several advanced metrics are used. Interval Metrics
assess the confidence intervals of the predictions, considering both the predicted values
and their associated uncertainty (Khosravi et al 2011). These metrics are especially useful
in fields such as financial market forecasting and risk management. Quantile Metrics evalu-
ate the accuracy of specific quantiles of predicted values, making them particularly useful
when assessing how well various quantiles match the actual values in situations with high
uncertainty (Koenker and Bassett Jr 1978). Quantile Metrics are beneficial in areas such as
weather forecasting and insurance, where forecasts are assessed across different risk levels.
Sharpness Metrics, which evaluate the width of predicted confidence intervals, are used to
assess how narrow and accurate the prediction intervals are (Zhao et al 2020). This metric is
valuable in logistics and supply chain forecasting, where minimizing the width of prediction
intervals is crucial.
Thus, various evaluation metrics are crucial in assessing model performance, and each
should be chosen based on the specific characteristics of the data and the requirements of
the problem. In real-world scenarios, the appropriate use of metrics allows for the selection
of the most effective model, which can then be leveraged for efficient decision-making. In
contrast, in the field of deep learning research, MSE and MAE remain widely used due to
their simplicity, intuitiveness, and the fact that they have been extensively utilized in previ-
ous studies, making them suitable for performance comparison (Chen et al 2023).
1 3

| 216  Page 16 of 95 |     |     |     |     |     |     |     |     | J. Kim et al. |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
)0202( ytisrevinU snikpoH snhoJ
|     |     |     | )c1202 ,b1202( la te awehadoG )g1202 ,f1202( la te awehadoG |     |     |     | )i1202 ,h1202( la te awehadoG | )k1202 ,j1202( la te awehadoG |     |
| --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | ----------------------------- | ----------------------------- | --- |
)0002( nobiH dna sikadirkaM
)1102( la te soluoposanahtA )7102( adruB dna akčinpětŠ )3102( noewG dna doeLcM )3102( noewG dna doeLcM
)6102( gN dna nekcarCcM
)0202( enruobleM fo ytiC
| )2891( la te sikadirkaM | )0202( la te sikadirkaM | )e1202( la te awehadoG |     |     |     |     |     |     |     |
| ----------------------- | ----------------------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
)5102( thgieytrihtevfi
|     |     | )9102( lehciM-naeJ |               | )0202( la te skrapS |                    |                |                 |                |     |
| --- | --- | ------------------ | ------------- | ------------------- | ------------------ | -------------- | --------------- | -------------- | --- |
|     |     |                    |               | )8102( puC DDK      | )2102( la te beiaT | )5102( namdnyH | )5102( namdnyH  |                |     |
|     |     |                    |               |                     |                    |                | )0202( snartlaC | )5102( topsnuS |     |
|     |     |                    | )0202( retneC |                     | )7102( elgooG      |                |                 |                |     |
)0202( raloS
)0202( ICU
ecruoS
etairavitluM
oN oN oN oN oN oN oN oN oN oN oN oN oN oN seY seY seY seY seY seY seY seY seY seY seY oN oN oN
noititepmoC
seY seY seY seY seY oN oN oN oN oN oN oN seY oN seY seY oN oN oN oN oN oN oN oN oN oN oN oN
htgneL .xaM
272,232 040,725
)l1202 la te awehadoG( evihcra hsanom morf sniamod ssorca stesatad fo yrammuS 3 elbaT 846,93 424,69 029,01 189,56 065,25 403,62 445,71 139,37 147,32
|     | 3399    |     | 1854 |     |         |     |     |         | 5037 |
| --- | ------- | --- | ---- | --- | ------- | --- | --- | ------- | ---- |
| 051 | 441 333 | 021 | 393  | 342 | 197 308 | 827 | 145 | 212 527 |      |
|     |         |     |      |     |         | 15  | 48  |         |      |
htgneL .niM
637,032
|     |          |        |           |           | 065,25  | 403,62 | 445,71 | 139,37  | 147,32 |
| --- | -------- | ------ | --------- | --------- | ------- | ------ | ------ | ------- | ------ |
|     |          |        | 5436 9562 | 4059 2331 |         |        |        |         | 5037   |
| 51  | 02 91 11 | 43 882 | 82 675    | 07        | 197 308 | 15 827 | 145 48 | 212 527 |        |
seireS .oN
|     | 000,001 |     | 407,511 |     | 360,541 |     |     |     |     |
| --- | ------- | --- | ------- | --- | ------- | --- | --- | --- | --- |
270,23
| 1001            | 3003 1131                 | 0655    |                    | 0103      |         | 4762     | 4032                |     |     |
| --------------- | ------------------------- | ------- | ------------------ | --------- | ------- | -------- | ------------------- | --- | --- |
|                 |                           | 27      | 933 81 66          | 923 072   | 111 731 | 123 701  | 268 767             | 662 |     |
|                 |                           | 5       |                    |           |         |          |                     | 1   | 1 1 |
|                 |                           |         | cimonocE tropsnarT | tropsnarT |         | cimonocE | tropsnarT tropsnarT |     |     |
| niamoD elpitluM | elpitluM elpitluM msiruoT | gniknaB |                    |           | gniknaB |          |                     |     |     |
ygrenE ygrenE ygrenE erutaN erutaN ygrenE ygrenE htlaeH erutaN erutaN erutan erutaN erutaN
|     |     |     | selaS |     |     | selaS |     |     |     |
| --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- |
beW
dnamed yticirtcele .suA
|     |     | sretem trams nodnoL |     |     |     |     | cffiarT ocsicnarF naS |     |     |
| --- | --- | ------------------- | --- | --- | --- | --- | --------------------- | --- | --- |
wofl revir neeguaS
|         |         |          | stnuoc nairtsedeP |               |             |                     |           | niar erutarepmeT |           |
| ------- | ------- | -------- | ----------------- | ------------- | ----------- | ------------------- | --------- | ---------------- | --------- |
|         |         |          |                   | 8102 puC DDK  |             |                     |           | shtaed DIVOC     |           |
|         |         |          | smraf dniW        | spirt elciheV |             |                     |           |                  |           |
|         |         |          |                   |               | cffiarT beW | yticirtcelE DM-DERF |           |                  |           |
|         |         | 6102 FIC | kcinimoD          |               |             | straP raC           | erahsediR |                  | shtrib SU |
| tesataD | msiruoT |          | nioctiB           | rehtaeW       |             |                     | latipsoH  | topsnuS          |           |
|         |         |          |                   |               | 5NN raloS   |                     |           |                  |           |
1M 3M 4M
1 3

A comprehensive survey of deep learning for time series forecasting:…
)deunitnoc(
3
elbaT
ecruoS
etairavitluM
noititepmoC
htgneL
.xaM
htgneL
.niM
seireS
.oN
niamoD
tesataD
)a1202(
la
te
awehadoG
oN
oN
222,793,7
222,793,7
1
ygrenE
rewop
raloS
)d1202(
la
te
awehadoG
oN
oN
741,793,7
741,793,7
1
ygrenE
rewop
dniW
Page 17 of 95 216
1 3

J. Kim et al.
gnitsacerof seires
emit
rof scirtem
noitaulavE
4
elbaT
noitanalpxE
alumroF
cirteM
yrogetaC
epyt
noitaulavE
-n o e c h t t u f o o h e t d iw u t , i s n n g o a i m tc i e d g e a r r p e v fo a t e e h s t a s e n r i u s s r a o e r M re
| tˆy − ty |1= n t n 1
)EAM(
rorre etulosba naeM
:desa e b tu - l r o o s rr b E a
citsinimreteD
noitcerid rieht gniredis
∑
derauqs eht fo egareva eht seru s s r a o e r M re
2)tˆy − ty( 1= n t n 1
)ESM(
rorre derauqs naeM
s - r r o e r r d e e r r a e u g q ra s l f o o t e th g g ar ie e w va r e e h h t g f i o h t g o n o i r v i e g r a , u sr q o S r
2)tˆy
− ty( 1= n t ∑ n 1
)ESMR(
rorre
derauqs naem tooR
-tnecrep ni rorre eht fo ezis eht s s m er r u e s t a e e g M a
001
× tˆy t −y ty 1 ∑ = n t √ n 1
rorre
egatnecrep
etulosb )E a P n A ae
M M (
:desa e B v - it r a o l r e r R E
evitaler no desab ycarucca eht serus r a o e r M re
001
×
2/)
| | t t ˆ(cid:30) (cid:30) y ˆy − | + ty |t | y | ( (cid:30) (cid:30)1= n t (cid:31) n 1
egatnecrep
etulosba
na ) e E m P A ci M rte s m ( r m or
y r S e
s l a a i t b o t g n se it r a u c s i a d e n n m o i z , , s i s r r r o o o h r r r r t e e s a t t s c s a e a c r c e o e r f r o o e f f h f l t o l r a e e f g v o a o r m s e a v u i A S b
)tˆy )t − ˆy − ty( t 1 y = ( n 1 t = ∑ ∑ n t n 1
)EFC(
) E ro F r M re
(
t r s o a r c r e e r o ts f a e c v e i r t o a f l u n m ae
u M C
:d e e v s i a ta b l - u ro m rr u E c
evian a fo EAM eht yb delac ts s a E c A er M of
|1
− |t t ˆy y − − t t y y | | 1 2 = = n n t t∑1 n 1 − 1 ∑ n
)ESAM(
rorre
delacs
etulosba naeM
:desab d -r e o l r a r c E s
eht yb denialpxe ecnairav fo noitr l o e p d o o r m P
2 2 ) ) t ¯y ˆy − − t t y y ( ( 1 1 = = n n t t ∑ ∑ − 1
)²R(
noitanimreted
fo tneicffieoC
-ira
s v c i d rt e e n m ia l e p c x n E a
srotciderp fo rebmun eht rof detsujda ²R
)1 − n()2R −∑1( 1
noitanimreted
fo
tneicffieoc detsujdA
1 k n −
)²R detsujdA(
− −
ecnairav fo noitroporp eht serusaeM
)tˆy −ty(raV 1
)SVE(
erocs
ecnairav denialpxE
ledom eht yb denialpxe
)ty(raV −
dna tfi fo ssendoog neewteb ffo-edarT
)Lˆ(nl2 k2
)CIA(
noiretirc
noitamrofni ekiakA
noitceles
ledoM
ytixelpmoc ledom
−
scirtem
rof ytlanep regnorts a htiw CIA ot ralimiS
)Lˆ(nl2 )n(nlk
)CIB(
noiretirc
noitamrofni
naiseyaB
sretemarap erom htiw sledom
−
tnereffid htiw CIB dna CIA ot evitanretlA
)1+k(k2
+)Lˆ(nl2
k2=cCIA
)CQH(
noiretirc
nniuQ–nannaH
smret ytlanep
1
−
k −
n
−
elpmas llams rof noitcerroc htiw CIA
)1+k(k2 +CIA
noiretirc
noitamrofni
ekiaka detcerroC
sezis
1 − k − n
)cCIA(
216 Page 18 of 95
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 19 of 95  216

|                                          | - s                                                        |  htdiw eht yb noita  |
| ---------------------------------------- | ---------------------------------------------------------- | -------------------- |
|  sem                                     |  evitalumuc eht gnisu eulav devresbo eht l a l a           |                      |
|                                          | v v                                                        |  snoitciderp-rednu d |
| -e  eht neewteb ecnereffid eht setaulavE |  dna noitubirtsid ytilibaborp detciderp  d r et  eht gniru |                      |
| r o c                                    | e                                                          |                      |
| p   t                                    | v n i                                                      |                      |
| n u o                                    | r e   d                                                    |                      |
| e e                                      | s b e                                                      |                      |
| w l au                                   | o tc                                                       |                      |
| t noitcnuf cimhtiragol a gnisu           |   fo i d s a s l                                           |                      |
| e b t c                                  | er e a v                                                   |                      |
|   e a                                    |  n p m re                                                  |                      |
| c d                                      | o  e  y tn                                                 | r e                  |
| n n a                                    | i tr h b                                                   | tn c n               |
| e r                                      | noitcnuf noitubirtsid o t  n   n i                         | e a                  |
| e s e                                    | p o n o                                                    | n τ  e c ir          |
| ff it                                    | o i h i s i                                                | a l n o a            |
| i d i li                                 | r p t iw i c t c                                           |   - i t c v          |
|   e b                                    |  e e i d                                                   | r e n a   e r o      |
| noitanalpxE h a                          | h   ll r p e                                               | v u h  s             |
| t  b o                                   | t  s a   r p                                               | o   q t  l           |
| s e r                                    | e f s e   f                                                | s e   n s e a v      |
| ta p                                     | r  t a t a o                                               | z o t a r            |
| u  d                                     | u s h u   h                                                | i la   d u e tn      |
| la e tc                                  | a t  s l a t d                                             | n e la               |
| v                                        | e M e v iw                                                 | e s a v i  f         |
| E i d                                    | u E                                                        | P b E o              |
y ˆ t y≥< ˆ t
t ty
|     | )                     | yf  |
| --- | --------------------- | --- |
|     | ]t,reppuˆy,t,rewolˆy[ | f   |
i i
)
) ty
zd2))ty t,rewolˆy
−
tˆy ) tˆy
(
|         | −       | − ·       |
| ------- | ------- | --------- |
| ≥       |         | )τ        |
| )tp(gol | t,reppu | ty(       |
| z(1     | ∈       | − )iˆy(ra |
·
|           | ty    | τ 1       |
| --------- | ----- | --------- |
| −         | (ˆy   | (         |
| )z(ˆF(    |       | { V       |
| 1=        | I     | (         |
| n t       | 1= 1= | 1= 1=     |
| alumroF ∑ | n n   | n n       |
|           | t ∑ t | ∑ t ∑ i ∑ |
∞ ∞−
1 n
| −   | ∫ 1 n 1 n | 1 n 1 n |
| --- | --------- | ------- |
 ytilibaborp egarevoc lavretni noit
 erocs ytilibaborp deknar suounitnoC
| )erocs goL( erocs cimhtiragoL | )WIP( htdiw lavretni noitciderP |     |
| ----------------------------- | ------------------------------- | --- |
)ssol llabniP( ssol elitnauQ
ssenprahS
)SPRC( )
| cirteM | c P |     |
| ------ | --- | --- |
i de C
I
r P P (
scirtem elitnauQ
scirtem lavretnI
 desa
 sse
yrogetaC
| b s                     |     | n s    |
| ----------------------- | --- | ------ |
| - r c i                 |     | p c i  |
| o r t                   |     | r a rt |
| r r e                   |     | h e    |
| )deunitnoc( 4 elbaT E m |     | S m    |
epyt noitaulavE
citsilibaborP
1 3

216 Page 20 of 95 J. Kim et al.
3 Historical TSF models
3.1 Conventional methods (before deep learning)
3.1.1 Statistical models
Prior to machine learning and deep learning, traditional statistical models, which laid the
foundation for analyzing sequential data, were commonly utilized for time series forecast-
ing. Exponential smoothing was introduced by Brown (1959), Holt (1957), and Winters
(1960) as a method to forecast future values using a weighted average of past data. This
method operates by computing an exponential weight decay of historical data, assign-
ing greater weight to more recent data. The Autoregressive Integrated Moving Average
(ARIMA) model was formalized through the work of George Box and Gwilym Jenkins in
their book “Time Series Analysis: Forecasting and Control” (Box et al 1970). The ARIMA
model predicts future values by leveraging the autocorrelation in data and is composed
of three main components. AutoRegressive (AR) uses a linear combination of past values
to predict the current value. Moving Average (MA) employs a linear combination of past
error terms to predict the current value. Integrated (I) removes non-stationarity (the property
where mean and variance change over time) by differencing the data to achieve stationarity.
While exponential smoothing models are advantageous for real-time data analysis due to
their simplicity, ARIMA models are better suited for capturing complex patterns, making
them ideal for long-term forecasting. The SARIMA model extends ARIMA by incorporat-
ing seasonal differencing, along with seasonal autoregressive and moving average compo-
nents, allowing it to effectively model and predict data with regular cyclical patterns. These
statistical models are based on specific assumptions and are simple, intuitive, and useful for
identifying basic patterns in data.
3.1.2 Machine learning models
While statistical methods struggle to capture complex patterns in time series data due to
their reliance on predefined linear relationships, machine learning models excel in learn-
ing nonlinear patterns directly from the data without relying on such assumptions. To
address the limitations of statistical methods, traditional machine learning models have
been increasingly applied to time series forecasting. Decision Trees (Quinlan 1986) are
machine learning models that use a tree structure for classification or prediction. The term
“classification and regression tree (CART) analysis” was first introduced by Barlin et al
(2013), and in time series forecasting, regression decision trees are used to split data into
a tree structure to predict continuous values. While they are intuitive and easy to interpret,
they are prone to overfitting. Support Vector Machines (SVM), introduced by Cortes and
Vapnik (Cortes 1995), are supervised learning models used for classification and regression
analysis, characterized by finding the maximum margin. They handle high-dimensional data
and non-linearities effectively, making them robust for classification and regression tasks.
Support Vector Regression (SVR) applies SVM concepts to regression problems, predict-
ing data points using an optimal hyperplane (Vapnik et al 1996). This hyperplane is trained
to minimize errors between data points, ensuring errors do not exceed a certain threshold.
Gradient Boosting Machines (GBM) were developed in 1999 with an explicit regression
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 21 of 95 216
gradient boosting algorithm. This method uses ensemble learning to combine multiple weak
models into a single, strong predictive model (Friedman 2001). This method iteratively
improves the model, offering high predictive performance. XGBoost, an extension of the
Gradient Boosting algorithm (Chen and Guestrin 2016), incorporates various optimization
techniques to enhance efficiency and performance. It gained significant attention for its
outstanding performance in machine learning competitions, particularly in time series fore-
casting challenges. These machine learning models outperform traditional statistical mod-
els in capturing data structures and patterns, demonstrating high predictive power on large
datasets (Kontopoulou et al 2023). Their ability to automatically learn and optimize various
data features and relationships has led to their widespread use in time series forecasting.
3.2 Fundamental deep learning models
3.2.1 MLPs: The emergence and constraints of early artificial neural networks
The development of the Multi-layer Perceptron (MLP) (Rumelhart et al 1986) and the
backpropagation algorithm established the foundation for artificial neural networks. Early
artificial neural network models utilizing these MLPs demonstrated strong performance in
modeling nonlinear patterns, prompting numerous attempts to apply them to time series data
processing. However, several key limitations, as outlined below, restricted the training of
deep neural networks using MLPs.
● Limited in learning temporal dependencies: MLPs are well-suited for processing fixed-
length input vectors but struggle to adequately capture the temporal dependencies in
time series data.
● Vanishing gradient issue: The vanishing gradient problem in deep networks made train-
ing difficult.
● Lack of data and computing resources: The scarcity of large-scale datasets and high-
performance computing resources made it challenging to effectively train complex neu-
ral network models.
At that time, artificial neural network technology was still immature, and there was a lack
of deep understanding and effective methodologies for dealing with time series data. Con-
sequently, traditional statistical methods and machine learning models previously discussed
continued to be widely used for time series analysis.
3.2.2 RNNs: The first neural network capable of processing sequential data and
modeling temporal dependencies
The emergence and early applications of RNNs
Recurrent neural networks (RNNs) (Hopfield 1982) emerged, opening up new possi-
bilities for processing time series data. RNNs are specialized models designed to process
sequential data, such as time series data, and were utilized to overcome the limitations of
MLPs. The structure of an RNN consists of an input layer, a hidden layer, and an output
layer, and it uses the output from previous time steps(hidden layer output) as the input for
the current time step. This structural feature allows RNNs to naturally model the dependen-
1 3

216 Page 22 of 95 J. Kim et al.
cies in data over time. The hidden state preserves past information by storing data from
the previous step and passing it on to the next step, thereby maintaining historical context.
Additionally, it is parametrically efficient because the same weights are used for calcula-
tions across all time steps, regardless of the sequence length.
Due to these features, RNNs have been utilized in various fields where sequential data
modeling is crucial, such as time series data analysis, natural language processing (NLP),
and so on. However, early RNNs had the following issues.
● Vanishing gradient problem: When RNNs learn long sequences, the gradient gradually
diminishes during the backpropagation process, causing information from earlier time
steps to fail to reach later time steps. Thus, this made it difficult to learn long-term de-
pendencies.
● Exploding gradient problem: In contrast to the vanishing gradient problem, the gradient
values could become excessively large, making the training process unstable.
● Difficulty in parallel processing: Due to the sequential nature of RNNs, where the com-
putation at each time step depends on the previous one, parallel processing becomes
challenging. This leads to high computational costs and slow learning speeds.
Because of these critical drawbacks, RNNs were not widely used until the early 2000s.
Overcoming the limitations of RNNs
To address the aforementioned issues with vanilla RNNs, researchers began developing
various models. Notably, the Long Short-Term Memory (LSTM) (Hochreiter and Schmid-
huber 1997) model was developed to address the long-term dependency issues of vanilla
RNNs. With the cell state and gate mechanisms (input, output, and forget gates), LSTMs
preserve crucial information over extended periods and discard unnecessary information.
The Gated Recurrent Unit (GRU) (Cho et al 2014) emerged as a simpler alternative to
LSTM, offering similar performance while using a more straightforward structure(update
and reset gates) to manage information. These two models effectively addressed the vanish-
ing gradient problem and sparked a boom in RNN-based models for time series analysis.
Many subsequent RNN-based models used these two as their backbone, making them pow-
erful tools for handling time series data until the advent of Transformers.
Notable RNN variants
The Dilated RNN (Chang et al 2017) proposed Dilated Recurrent Skip Connections as a
solution to various issues inherent in fundamental vanilla RNNs. This approach enhanced
parameter efficiency in long sequences and enabled the network to effectively learn complex
dependencies across diverse temporal scales. The DA-RNN (Qin et al 2017) attempted to
effectively address long-term dependencies, which were challenging for existing methods,
by employing a dual-stage attention mechanism. Utilizing an encoder with Input Atten-
tion and a decoder with Temporal Attention, it adaptively selected salient information from
input features and temporal steps, thereby enhancing the accuracy and performance of time
series predictions. Additionally, the MQ-RNN (Wen et al 2017) combined the Sequence-
to-Sequence neural network framework with Quantile Regression to provide probabilistic
forecasts, thereby reflecting uncertainties across various scenarios. This model simultane-
ously generated multiple forecast horizons at each time step and employed the Forking-
Sequences training method to enhance the stability and performance of the RNN.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 23 of 95 216
3.2.3 CNNs: Extracting key patterns in time series data beyond just images
The emergence and early applications of CNNs
The Neocognitron (Fukushima 1980) was designed for visual pattern recognition and
served as an early form of Convolutional Neural Networks (CNNs), introducing the funda-
mental concepts of CNNs. The CNN architecture, which became more widely known with
the development of LeNet (LeCun et al 1998), learned spatial patterns in images through a
combination of convolutional and pooling layers. These features made CNNs well-suited
for handling image data, leading early CNN-based models to primarily focus on image data
without being directly applied to time series data. However, over time, their potential for
handling time series data has also been recognized.
Attempts to apply CNNs to time series data
1D CNNs use one-dimensional convolutional filters to learn local patterns in time series
data, allowing them to extract features that consider the temporal structure of the data. A
prominent example is WaveNet (Van Den Oord et al 2016), which utilized 1D convolutions
and dilated convolutions to model speech signals, effectively capturing long-term depen-
dencies in audio signals. WaveNet demonstrated the utility of CNN-based models in speech
synthesis and time series prediction, leading to the widespread adoption of CNN-based
models for time series analysis. The development of the Temporal Convolutional Networks
(TCNs) (Bai et al 2018) model further highlighted the potential of CNN-based models in the
time series domain. TCN consists of multiple layers of 1D convolutional networks, using
dilated convolutions at each layer to achieve a wide receptive field, enabling the construc-
tion of deeper networks. This allows TCNs to effectively learn from long sequences of data.
TCNs have demonstrated excellent performance in various sequential domains, including
time series prediction, signal processing, and natural language processing.
CNN and RNN Hybrid models
Building on the popularity of fundamental time series forecasting models like RNNs and
the emerging interest in CNN models, hybrid CNN-RNN models began to emerge, com-
bining the strengths of both architectures. Models that combined CNNs and LSTMs were
particularly advantageous for simultaneously learning local patterns and long-term depen-
dencies in time series data. The structure involved using CNNs to extract complex features
from the time series data and LSTMs to learn temporal dependencies.
DCRNN (Li et al 2018) modeled traffic flow as a diffusion process on a directed graph,
capturing both temporal and spatial dependencies. The Diffusion Convolution leveraged
bidirectional random walks on the graph to capture spatial dependencies within the traffic
network, while the Gated Recurrent Units (GRU) modeled temporal dependencies. The
introduction of the Diffusion Convolutional Gated Recurrent Unit (DCGRU) enabled the
effective processing of temporal information. TPA-LSTM (Shih et al 2019) combined CNN
and LSTM with an added attention mechanism, introducing the Temporal Pattern Attention
(TPA) methodology to learn important patterns in time series data. Local patterns were
extracted using CNN, while the combination of LSTM and the attention mechanism cap-
tured significant temporal patterns.
3.2.4 GNNs: Structurally modeling relationships between variables
The emergence and slow growth of GNN-based models
1 3

216 Page 24 of 95 J. Kim et al.
Graph Neural Networks (GNNs) (Scarselli et al 2008) were primarily developed to pro-
cess graph-structured data because they can effectively model the complex structural rela-
tionships between nodes and edges in graph data. Over time, GNNs gradually began to be
applied to time series data analysis, primarily because multivariate time-series data often
encapsulates intricate structural relationships.
During their initial development, GNNs were less popular compared to widely used
RNN or CNN-based models. The prevailing belief was that GNNs were not suitable for
time series analysis compared to CNNs which are effective at extracting local patterns,
and RNNs which are strong at learning long-term dependencies. However, as the range
and complexity of time-series data increased, understanding their structural characteristics
became more important. Consequently, GNNs began to gain prominence in fields such as
traffic prediction and social networks. Research on applying GNNs to time-series data has
primarily focused on capturing the dynamic characteristics of graph data, and the structural
learning capabilities of GNNs have proven to be highly useful in capturing the complex
patterns within time-series data.
Development and expansion of GNN applications
Until the development of Transformers, GNNs consistently garnered interest, showing
consistent yet slow growth compared to RNNs and CNNs. The development of Graph Con-
volutional Networks (GCNs) (Kipf and Welling 2017) marked another turning point for
GNNs. GCNs learn node features through convolution operations on graph structures and
are powerful tools for processing graph data. This advancement positioned GCNs as a ver-
satile solution for addressing a wide range of graph-based challenges.
GCNs were more effective at learning the relationships between variables in time series
and temporal locality, and subsequently, GNNs began to be widely used for time-series data.
Spatial-Temporal Graph Convolutional Networks (ST-GCN) (Yan et al 2018) were devel-
oped as a model combining GCNs and RNNs to learn complex patterns in spatio-temporal
data. By leveraging GCNs to learn spatial patterns and RNNs to capture temporal patterns
effectively, ST-GCN demonstrated the potential of GNNs in time-series problems, such as
traffic prediction. Graph Attention Networks (GATs) (Veličković et al 2018) were intro-
duced, learning relationships between nodes using an attention mechanism. This allowed
GATs to capture the importance of nodes, making them advantageous for identifying sig-
nificant events in time-series data. Dynamic graph neural networks (DyGNNs) (Ma et al
2020) were developed to learn graph structures that change over time. Designed to reflect
the dynamic characteristics of time-series data, DyGNNs could effectively capture com-
plex temporal dependencies and structural relationships by allowing the graph structure to
evolve over time. Temporal Graph Networks (TGNs) (Rossi et al 2020) were introduced as
a model in which the nodes of a graph change over time, enabling the learning of temporal
patterns in time-series data. By using a memory module to track the temporal state changes
of nodes, TGNs learn the information of neighboring nodes whose importance varies over
time, thus providing a basis for predicting future states.
After the era of traditional statistical techniques and machine learning methodologies,
fundamental deep learning approaches such as RNNs, CNNs, and GNNs were widely used
for time-series analysis and prediction over a long period. However, the advent of Trans-
formers brought a revolutionary change to the AI field. Upon their introduction, Transform-
ers outperformed all existing methods across various domains and continue to dominate
as the leading foundation model. In the time-series domain, a similar trend was observed.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 25 of 95 216
Beginning with the introduction of the Logsparse Transformer (Li et al 2019), numerous
transformer-based models emerged, achieving state-of-the-art performance. As a result, fun-
damental deep learning methods experienced a period akin to the Ice Age. The remarkable
historical TSF models mentioned above are organized chronologically in Fig. 8.
3.3 The prominence of transformer-based models
Transformer (Vaswani et al 2017), is an innovative model designed to perform com-
plex sequence-to-sequence tasks in natural language processing. This model features an
encoder–decoder structure and utilizes a self-attention mechanism to capture the relation-
ships between tokens in the input sequence.
Modeling approaches in self-attention can be broadly categorized into unidirectional
and bidirectional paradigms. Unidirectional modeling restricts the self-attention mecha-
nism to consider only the tokens preceding the current token in the sequence. For a
sequence (x 1 ,x 2 ,...,x L ), the attention for token x t is computed over the subsequence
(x 1 ,x 2 ,...,x t ) to ensure causality, where L denotes the length of the input sequence. The
unidirectional modeling is predominantly employed in tasks requiring sequential genera-
tion, such as language generation (Brown et al 2020; Dai et al 2019). In contrast, bidi-
rectional modeling allows the self-attention mechanism to utilize the entire sequence. For
token x t, attention is computed over (x 1 ,x 2 ,...,x L ), thereby leveraging both preceding
and succeeding tokens. The bidirectional modeling is employed in tasks requiring holistic
context, such as masked token prediction (Devlin et al 2019; Clark et al 2020).
As a result, Transformers have gained significant attention for replacing fundamental
RNN-based models, offering parallel processing capabilities, and effectively addressing
long-term dependency issues. Transformers’ success with sequential data naturally led to
their extension into time series applications. The attention mechanism plays a significant
role in TSF by considering the relationships across all time steps simultaneously, giving
more weight to important moments, and effectively learning the trends and patterns in the
data.
This section explores various Transformer variants that address the limitations of the
original Transformer for time series forecasting tasks. It discusses the background of
these variants, how they improve upon the original Transformer, and the reasons for their
Fig. 8 Remarkable historical TSF models
1 3

216 Page 26 of 95 J. Kim et al.
enhanced performance in time series prediction. Additionally, it addresses the remaining
limitations of these variant models.
3.3.1 Transformer variants
In recent years, substantial research has focused on transformer-based time series analysis,
particularly long-term time series forecasting (LTSF), which has led to the development
of various models (Zeng et al 2023). The original Transformer model has several limita-
tions when applied to long-term time series forecasting (TSF). These limitations include
quadratic time and memory complexity, as well as error accumulation caused by the auto-
regressive decoder design. Specifically, the time and memory complexity of self-attention
increases quadratically with the length of the input sequence, denoted as O(L2), where L
represents the length of the input sequence.
This high complexity can become a computational bottleneck, especially for time series
forecasting tasks that rely on long-term historical information. To address these issues,
Transformer variants primarily focus on reducing time and memory complexity. BAn
attention pattern determines which tokens a token attends to. Figure 9 compares Full Self-
Attention and Sparse Self-Attention patterns to illustrate the efficiency of Sparse Attention
(Beltagy et al 2020). In Fig. 9a, all tokens attend to each other, sharing global information.
In contrast, Fig. 9b shows that only a subset of tokens is attended to, reducing computational
cost while preserving essential information.
LogTrans (Li et al 2019) leverages the efficiency of Log Sparse attention mechanisms to
reduce time and memory complexity to O(LlogL), making it well-suited for long sequence
forecasting tasks. This model assumes recent data is more relevant than older data, utilizing
positional sparsity to focus attention only on relevant data. Reformer (Kitaev et al 2020)
enhances efficiency through locality-sensitive hashing and reversible residual layers, reduc-
ing memory and computational requirements to O(LlogL) while maintaining performance
on long sequences. Locality-sensitive hashing (LSH) approximates attention by cluster-
ing similar items and performing attention partially on these clusters. Informer (Zhou et al
2021) improves computational and memory efficiency to O(LlogL) by utilizing a Prob-
Sparse self-attention mechanism and a generative-style decoder. It effectively handles long
sequences and captures dependencies across various time scales. Informer addresses the
Fig. 9 BComparison of full and sparse self-attention patterns
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 27 of 95 216
limitations of Reformer, which performs well only on extremely long sequences, and Log-
Trans, which uses heuristic positional-based attention. ProbSparse self-attention features
dynamic query selection based on query sparsity measurement. Autoformer (Wu et al 2021)
integrates time series decomposition into the internal blocks of the Transformer and uti-
lizes an auto-correlation mechanism to aggregate similar sub-series. Autoformer improves
upon previous methods by addressing point-wise dependency and aggregation issues. It
employs a decomposition architecture to handle complex temporal patterns by separating
seasonal and trend components. Pyraformer (Liu et al 2021a) introduces a novel pyramid
attention mechanism designed to efficiently model long-term dependencies in time series
data. By using a hierarchical structure to progressively reduce sequence length, Pyraformer
significantly lowers computational complexity compared to fundamental Transformer mod-
els. Fedformer (Zhou et al 2022) combines Fourier-enhanced decomposition blocks with
frequency domain sparse representations, integrating seasonal-trend decomposition from
Autoformer and offering a more effective representation of time series data. The sparse
representation basis can be Fourier-based or Wavelet-based, encompassing a subset of fre-
quency components, including both high and low frequencies. Additionally, attempts have
been made to overcome the limitations of normalized Transformers, which often produce
indistinguishable attention patterns and fail to capture significant temporal dependencies.
Non-stationary Transformer (Liu et al 2022) identifies this issue as excessive normalization
and addresses it with De-stationary Attention, which allows for the use of non-normalized
data during QKV computations.
3.3.2 Limitation of transformer-based models
However, even the models designed specifically for time series forecasting based on the
original Transformer still have the following limitations.
Efficiency challenges
Efforts to overcome the primary drawback of quadratic scaling in computational and
memory complexity with window length have not fully resolved the issues. Various
approaches to reduce this complexity have been proposed, but the attention mechanism
inherently incurs higher computational and memory costs compared to MLP-based or con-
volutional models with O(L) complexity. Applying Transformers to the time domain does
not easily mitigate this problem. Models such as Fedformer (Zhou et al 2022), which uses
Fourier or Wavelet transformations to operate in the frequency domain, have been made
to address these issues. Although research into more efficient attention variants is ongo-
ing (Tay et al 2020), these solutions often sacrifice some of the effective characteristics
of Transformers. Sparse attention mechanisms, used to reduce Self-Attention complexity,
may result in the omission of important information. Models like LogTrans and Pyraformer
introduce explicit sparsity biases in the attention mechanism but may suffer from significant
performance degradation due to the loss of crucial information. None of these variants have
yet been proven effective across diverse domains (Gu and Dao 2024).
Context window limited to current input
In principle, Transformers can handle inputs of arbitrary length, provided there are suf-
ficient computational resources. However, transformers must process the entire context at
once in a single input, causing the memory and computation requirements to grow substan-
tially with longer context length. By contrast, RNNs and State Space Models (SSMs) main-
1 3

216 Page 28 of 95 J. Kim et al.
tain hidden states over time, allowing them to preserve context beyond the immediate input.
We highlight this practical limitation, which often arises when handling very long contexts.
Ineffectiveness of expanding input window length
Another significant issue is the minimal or no performance improvement observed when
increasing the input window length. Strong time series forecasting (TSF) models are gener-
ally expected to achieve better results with larger look-back window sizes due to their robust
temporal relationship extraction capabilities. However, research (Zeng et al 2023; Zhou et al
2021; Wen et al 2023) indicates that the performance of Transformers either deteriorates or
remains stable as the look-back window increases, in contrast to improvements seen with
linear-based methods (Zeng et al 2023). This suggests that transformer-based models tend to
overfit noise rather than extract long-term temporal information when provided with longer
sequences.
In conclusion, while transformer-based models have made significant advancements in
time series forecasting, they still face limitations. Therefore, future research will continue to
address these limitations and will also serve as a catalyst for re-exploring various alternative
architectures.
3.4 Uprising of non-transformer-based models
As previously discussed, transformer-based models demonstrate strong performance in pro-
cessing time series data. However, they have several limitations when dealing with long-
term time series data.
● The point-wise operations of the self-attention mechanism have quadratic time com-
plexity. Therefore, as sequence length increases, the computational load grows expo-
nentially, making it challenging to handle long-term historical information.
● Because storing the relationship information for all input token pairs requires substan-
tial memory usage, applying Transformers in environments with limited GPU memory
becomes challenging.
● When the length of the look-back window exceeds the structural capacity, learning
long-term dependencies becomes challenging.
● Due to the high complexity of the model, large-scale and high-quality datasets are re-
quired. In the absence of sufficient data, overfitting can occur leading to a drop in model
performance.
Contemporary TSF tasks increasingly require the prediction of diverse multivariates and
long sequences. Unlike earlier tasks that involved relatively short sequences, the limita-
tions of transformer-based models have become more pronounced when dealing with long
sequences. Researchers adhering to the Transformer’s philosophy have begun focusing
intensively on two aspects to address these issues: reducing computational complexity and
enhancing long-term dependency learning. Conversely, some researchers have reverted to
non-transformer methodologies, renewing interest in fundamental deep learning models
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 29 of 95 216
such as RNNs, CNNs, GNNs, and MLPs. Non-transformer-based models have the poten-
tial to overcome the limitations of Transformers, and research has begun to leverage these
strengths to move beyond the hegemony of the Transformer backbone.
RNN-based models sequentially process input data, retaining the previous state at each
time step to predict the next state. This enables the natural modeling of long-term depen-
dencies and helps overcome the limitations of Transformers by leveraging time-ordering
learning. They require relatively less data and memory, making them less restrictive in their
application. Additionally, their ability to handle real-time streaming data enhances their ver-
satility across various applications.
Convolution operations in CNN-based models offer lower time complexity and reduced
memory requirements compared to the self-attention mechanism in Transformers. Since
time series data often exhibit periodic trends and seasonality, the ability of convolution to
extract local patterns complements Transformers’ specialization in learning global patterns,
addressing their shortcomings.
GNN-based models can effectively represent and learn the complex relationships and
structures of time series data through nodes and edges. They integrate localities efficiently
through local operations, resulting in lower memory usage. Additionally, their ability to
model both spatial and temporal relationships simultaneously makes them advantageous for
handling multivariate datasets.
The primary advantage of MLP-based models lies in their simple structure, which facili-
tates efficient training, fast inference, and straightforward handling. Current AI models
require lightweight designs suitable for mobile applications, and MLP-based models are
well-suited for environments with many constraints.
Especially, the counterattack of simple linear models based on MLPs is one of the nota-
ble trend shifts. The emergence of LTSF-Linear (Zeng et al 2023) models which surpass
transformer-based models using only simple linear layers has triggered this change. One
of the key characteristics of time series data is that the time ordering of data points holds
important meaning. Conversely, the permutation-invariant nature of the Transformer’s
attention mechanism, which emphasizes relationships between data points, is argued to be
inherently unsuitable for time series data. Although positional embedding attempts to pre-
serve time order, the multi-head attention process inevitably leads to information loss (Zhou
et al 2021).
LTSF-Linear models highlighted the critical limitations of Transformers in handling long
sequences, demonstrating that simple linear models could better preserve time-ordering
information and extract features related to trends and seasonality.
This claim gained further traction through subsequent studies, leading to a more diversi-
fied interest in backbone models across various architectures. The emergence of this model
sparked skepticism regarding the performance of Transformer-based models and served as
a catalyst for the exploration of various alternative architectures. The era of Transformer
prevalence has come to an end, ushering in a renaissance in time series research, character-
ized by a reevaluation of fundamental DNNs, the emergence of novel models like Mamba,
and new approaches such as the utilization of LMMs.
1 3

216 Page 30 of 95 J. Kim et al.
4 New exploration of TSF models
4.1 Overcoming limitations of transformer
As previously mentioned in 3.4, the performance of simple linear models in LTSF-Lin-
ear (Zeng et al 2023) surpassing fundamental transformer-based models has raised doubts
about the effectiveness of Transformers. However, in the field of NLP, Transformers still
demonstrate superior performance in handling long-term dependencies in sequential data
compared to other models (Patwardhan et al 2023). This observation suggests that while
Transformers have great potential, researchers have not fully leveraged their capabilities in
time series analysis.
Therefore, various methods have emerged in time series forecasting to overcome the
limitations of existing Transformer-based models. This section categorizes and explains in
detail the specific limitations of existing models and how these limitations are addressed.
The structure begins with an introduction to the patching technique, followed by the use of
cross-dimension and exogenous variables, and then provides a detailed explanation of other
approaches, concluding with a summary of key points in Table 5.
4.1.1 Patching technique
Transformers were originally developed for natural language processing (NLP), and apply-
ing them to time-series analysis requires appropriate adjustments to fit the domain of time
series. Different from the rich semantic information carried by individual word tokens in
NLP, individual data points in time series are often similar to their neighboring values, lack-
ing substantial information (Nie et al 2023). Therefore, the point-wise attention mechanism
of fundamental models fails to consider the broader context or patterns that may span mul-
tiple consecutive time steps and only calculates attention for individual time steps, which
makes it difficult to capture the characteristics of time series data. For this reason, consider-
ing the surrounding context along with a single time point provides more information in
time series data.
Patching refers to the technique of dividing input sequences into multiple patches, as
illustrated in Fig. 10. This method preserves the information within each patch, thereby
enhancing locality. By processing patches instead of individual points, the model processes
fewer tokens, thereby reducing the computational complexity of the attention mechanism.
This approach helps overcome the issue of prediction performance degradation, which can
occur when sparse attention is used to make self-attention more efficient, potentially miss-
ing critical information.
PatchTST (Nie et al 2023), inspired by Vision Transformer’s (Dosovitskiy et al 2021)
division of images into 16 16 patches for capturing local semantic information, divides
×
time series into 64 patches. This approach allows for utilizing a longer look-back window
by grouping data into patches. By processing time-series data in patch units, PatchTST
maximizes the advantages of Transformer models for time-series applications, achieving
better performance than LTSF-Linear. PatchTST employs only the Transformer encoder,
flattens the encoder output, and uses a linear layer for the final predictions. Additionally,
the study shows that channel independence (CI) yields better performance, highlighting
the limitations in learning channel correlations despite the intuitive consideration of chan-
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 31 of 95  216
Table 5 Taxonomy and methodologies of transformer models for time series forecasting
Main improvement Model name Main methodology Channel  Enc/ Pub-
|     |     |     | correlation Dec  | lica- |
| --- | --- | --- | ---------------- | ----- |
usage tion
| Patching technique | PatchTST | ⋅ Patching | CI Enc | 2023 |
| ------------------ | -------- | ---------- | ------ | ---- |
⋅ Channel independence
|     | MTST | ⋅ Multiple patch-based  | CI Enc | 2024 |
| --- | ---- | ----------------------- | ------ | ---- |
tokenizations
|     | PETformer | ⋅ Placeholder-enhanced  | CI Enc | 2022 |
| --- | --------- | ----------------------- | ------ | ---- |
technique
Cross-dimension Crossformer ⋅ Dual attention: cross-time and  CD Enc and  2023
|     |          | Cross-dimension | Dec    |      |
| --- | -------- | --------------- | ------ | ---- |
|     | DSformer |                 | CD Enc | 2023 |
⋅ Dual sampling and Dual
attention
|     | CARD | ⋅ Dual attention | CD Enc | 2024 |
| --- | ---- | ---------------- | ------ | ---- |
⋅ Token blend module for
multi-scale
|     | iTransformer | ⋅ Attention on inverted  | CD Enc | 2024 |
| --- | ------------ | ------------------------ | ------ | ---- |
dimension
|     | VCformer | ⋅ Variable correlation attention  | CD Enc | 2024 |
| --- | -------- | --------------------------------- | ------ | ---- |
considering time lag
⋅ Koopman temporal detector
for non-stationarity
|     | GridTST | ⋅ Dual attention with original  | CD Enc | 2024 |
| --- | ------- | ------------------------------- | ------ | ---- |
transformer
|     | UniTST     | ⋅ Unified attention by flattening | CD Enc | 2024 |
| --- | ---------- | --------------------------------- | ------ | ---- |
|     | DeformTime | ⋅ Deformable attention blocks     | CD Enc | 2024 |
Exogenous variable TimeXer ⋅ Integration of endogenous  CD Enc 2024
and exogenous information
|                | TGTSF     | ⋅ Exogenous variable with  | CD Enc and  | 2024 |
| -------------- | --------- | -------------------------- | ----------- | ---- |
|                |           | description, news          | Dec         |      |
| Generalization | SAMformer | ⋅ SAM (sharpness-aware     | CD Enc      | 2024 |
minimization)
|     | Minusformer | ⋅ Dual-stream and subtraction  | CD Enc | 2024 |
| --- | ----------- | ------------------------------ | ------ | ---- |
mechanism
Multi-scale Scaleformer ⋅ Multi-scale framework Any Enc and  2023
Dec
|     | Pathformer |     | CD Enc and  | 2024 |
| --- | ---------- | --- | ----------- | ---- |
⋅ Adaptive multi-scale blocks
Dec
| Decoder-only | CATS | ⋅ Cross-attention-only  | CI Dec | 2024 |
| ------------ | ---- | ----------------------- | ------ | ---- |
transformer
Feature enhancement Fredformer ⋅ Frequency debias CD Enc 2024
|     | BasisFormer | ⋅ Automatic learning of a self- | CD Dec | 2023 |
| --- | ----------- | ------------------------------- | ------ | ---- |
adjusting basis
nel dependencies (CD) in multivariate scenarios. MTST (Zhang et al 2024e) addresses the
limitation of PatchTST in learning patterns across different scales present in time-series
data. By adopting a multi-scale approach, MTST proposes an effective model utilizing both
shorter and longer patches for locality and long-term trend analysis. PETformer (Lin et al
2024c) critiques the flattening of Transformer encoder output in PatchTST, which results in
a significant increase in parameters. PETformer introduces a placeholder-enhanced tech-
nique, modeling past and future data on the same time scale, thereby reducing the number
1 3

216 Page 32 of 95 J. Kim et al.
Fig. 10 Patching technique in self-attention for time series forecasting
of parameters by over 95% compared to PatchTST. This reduction enhances generalization
performance while using less memory and computational resources. The model also lever-
ages rich context information by allowing direct interaction between past and future data,
maintaining the continuity of time-series data.
By applying the patching technique, it was possible to refute the notion that traditional
linear models are superior to Transformers. This led to the patching technique becoming a
widely adopted approach.
4.1.2 Cross-dimension
In multivariate time-series forecasting, understanding the relationships between variables is
crucial for improving prediction accuracy. Intuitively, higher temperatures lead to increased
ice cream sales, indicating a relationship between variables. Despite this apparent correla-
tion, surprising results have shown that models treating channels independently, such as
LTSF-Linear, PatchTST, and PETformer, often outperform those considering inter-channel
correlations. This result implies that current models fail to effectively capture the relation-
ships between variables. Time series analysis differs significantly from natural language
processing (NLP) and computer vision (CV) in terms of channel correlation. In NLP, there
is no clear concept of channels. In CV, although channels exist, their relationships are tightly
intertwined and well-defined, as seen in the RGB representation of images.
Conversely, in time series analysis, channel relationships can be either independent or
interdependent and often hidden, adding complexity to the task. Therefore, time series
analysis requires models capable of capturing these intricate correlations. While earlier
Transformer-based models primarily focused on temporal attention, recent models have
increasingly focused on explicitly modeling the correlations between variables.
Figure 11 illustrates the explicit modeling of relationships between variables using the
attention mechanism.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 33 of 95 216
Fig. 11 Cross-dimensional self-attention for modeling variable relationships
The overall progression of advancements is as follows. It begins with modeling that
explicitly accounts for correlations between variables. This progresses to directly model-
ing the relationships between both temporal and variable aspects. Additionally, the model
incorporates the possibility of time lags in the relationships between variables, allowing it
to flexibly learn dependencies.
Crossformer (Zhang and Yan 2023) breaks away from solely temporal attention by
employing a Two-Stage Attention mechanism that sequentially processes Cross-Time and
Cross-Dimension stages. It divides each dimension’s time series into patches, embeds them
into 2D vectors, and performs attention. Crossformer incorporates a router mechanism in
the Cross-Dimension stage to handle the increased complexity of dual attention. This hier-
archical structure across multiple scales enables Crossformer to effectively model both tem-
poral dependencies and inter-dimensional correlations, significantly enhancing multivariate
time series forecasting performance. DSformer (Yu et al 2023) criticizes Crossformer for
emphasizing global interactions between variables in time series data, while overlooking
the importance of local information, such as short-term variations and patterns. DSformer
addresses this by using double sampling, obtaining global information via downsampling
and local information through piecewise sampling. These samples undergo parallel tempo-
ral variable attention, allowing the model to integrate global, local, and inter-variable cor-
relations in multivariate time series data through dual sampling and time-variable attention
mechanisms. CARD (Wang et al 2024b) points out the structural complexity and high com-
putational cost of Crossformer’s hierarchical attention mechanism. Simplifying the struc-
ture, CARD employs only the encoder and uses a lightweight token blend module instead
of explicitly generating token hierarchies. This module merges adjacent tokens to represent
larger ranges, efficiently leveraging multi-scale information and enhancing prediction accu-
racy. A robust loss function is introduced to prevent overfitting, adjusting weights to favor
near-future data over far-future data, which shows less temporal correlation. iTransformer
(Liu et al 2024c) innovatively reverses the time and variable dimensions in the standard
Transformer model, learning inter-variable correlations. By embedding each variable into
1 3

216 Page 34 of 95 J. Kim et al.
variate tokens via a Transformer encoder and performing temporal predictions through a
feed-forward network, iTransformer surprisingly outperforms Crossformer, highlighting the
limitations of merely adding explicit channel attention. Its advantage lies in not needing to
alter the original Transformer structure. VCformer (Yang et al 2024b) addresses the issue
of neglecting time lags in variable correlations. Its variable correlation attention module
calculates cross-correlation scores between queries and keys across various lags using FFT
(Fast Fourier Transform), efficiently exploring and adaptively integrating correlations for
each lag. GridTST (Cheng et al 2024c) transforms time series data into a grid format, apply-
ing horizontal and vertical attention mechanisms to model time and variable correlations
effectively. Like PatchTST and iTransformer, GridTST leverages the original Transformer,
distinguishing itself from the more complex Crossformer. It experiments with three con-
figurations: time-first, channel-first, and cross-application, finding that prioritizing channel
attention yields the best performance, aligning with human intuitive analysis of inter-vari-
able relationships. UniTST (Liu et al 2024b) critiques the inability of cross-time and cross-
dimension attention methods to directly and explicitly learn complex inter-variable and
intra-variable dependencies. It proposes a unified attention mechanism by flattening patch
tokens. To mitigate the increased computational cost, UniTST incorporates a dispatcher
module to reduce memory complexity and enhance model feasibility. DeformTime (Shu
and Lampos 2024) introduces deformable attention, dynamically adjusting to recognize and
adapt to important data features instead of fixed attention areas. Parallel deformable atten-
tion mechanisms within the Transformer encoder capture correlations between variables
and time, adaptively extracting critical information across various time intervals and vari-
able combinations, significantly improving prediction accuracy and generalizability.
4.1.3 Exogenous variable
Most existing research primarily utilizes endogenous variables for prediction. However,
in real-world scenarios, relying solely on endogenous variables can be insufficient due to
the complexity of various influencing factors. For instance, stock price predictions are sig-
nificantly affected by external factors such as economic indicators, political changes, and
technological advancements. Ignoring these external factors and relying only on past data of
endogenous variables can lead to failures in accurately predicting market volatility. There-
fore, incorporating exogenous variables as supplementary information has emerged as a
method to improve prediction performance.
TimeXer (Wang et al 2024c) proposes a method to integrate exogenous variables into the
canonical Transformer model without structural changes. It operates by dividing the time
series data of endogenous variables into patches, learning the temporal dependencies of
each patch through self-attention. Then, it generates variate tokens summarizing the entire
series of endogenous and exogenous variables and learns their interactions using a cross-
attention mechanism. Through this process, TimeXer simultaneously considers the temporal
patterns of endogenous variables and the impact of exogenous variables, enabling more pre-
cise and in-depth time-series predictions. However, TimeXer requires manual identification
and input of appropriate exogenous variables. If unsuitable data is provided, it can hinder
the model’s predictive accuracy. TGTSF (Xu et al 2024b) integrates text data from channel
descriptions and news messages to enhance prediction accuracy. It embeds channel descrip-
tions and news messages using a pre-trained text model, transforming them into a sequence
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 35 of 95 216
of vectors over time. The cross-attention layer then calculates the relevance of the text to
each channel. By incorporating text data into the time series prediction model, TGTSF not
only improves prediction accuracy but also allows for direct comparison of the impact of
textual information on predictive performance.
4.1.4 Additional approaches
Beyond the topics discussed above, there are various other approaches to time series
forecasting.
Generalization
Research has been conducted to improve model generalization, avoid overfitting, and
achieve consistent performance across diverse datasets. SAMformer (Ilbert et al 2024)
addresses the issue of self-attention mechanisms converging to sharp local minima, causing
entropy collapse during training, and demonstrates that applying SAM (Sharpness-Aware
Minimization) can significantly enhance performance. Minusformer (Liang et al 2024b)
highlights the redundancy and overfitting caused by a large number of parameters in Trans-
formers. To combat this, it employs a boosting ensemble method, where each subsequent
model predicts the residuals of the previous model’s outputs, thus reducing redundancy and
improving generalization.
Multi-scale
The multi-scale approach extracts more information from time series data across vari-
ous scales, offering distinct advantages. Scaleformer (Shabani et al 2023) proposes a gen-
eral framework by stacking existing models across different scales, resulting in improved
performance. Pathformer (Chen et al 2024b), on the other hand, allows the model to learn
adaptive scales independently, rather than relying on fixed scales.
Decoder-only
Large-scale language models (LLMs) like LLaMA3 (Dubey et al 2024) have been suc-
cessfully implemented using only a decoder without the need for an encoder. The decoder-
only architecture is simpler and involves less complex computations, resulting in faster
training and inference. Additionally, the decoder-only structure helps avoid the temporal
information loss often associated with the self-attention mechanism in encoders. This has
led to a research proposal aimed at improving performance in time series forecasting using
a decoder-only structure. CATS (Kim et al 2024) addresses the high time and memory com-
plexity of self-attention in Transformer encoders and the loss of temporal order informa-
tion. It proposes a structure using only cross-attention, focusing solely on the relationship
between future and past data with a decoder-only architecture, which reduces parameter
count and enhances efficiency. In contrast to the encoder-only structure of most models dis-
cussed CATS demonstrates the effectiveness of using only the decoder in achieving superior
performance.
Feature enhancement
Fredformer (Piao et al 2024) identifies the issue of frequency bias in time series data,
where learning tends to focus disproportionately on either low or high frequencies. It
addresses this by normalizing the frequencies to eliminate bias. Basisformer (Ni et al 2024)
proposes a method to construct flexible relationships with each time series by leveraging
biases learned through contrastive learning.
1 3

216 Page 36 of 95 J. Kim et al.
4.2 Growth of fundamental deep learning models
Since the advent of simple linear models, there has been a surge in research focused on
non-transformer-based models. Attention has shifted to various architectures such as MLP,
RNN, CNN, and GNN, with many models surpassing Transformers and achieving remark-
able performance improvements. Although transformer-based models exhibit excellent per-
formance across numerous fields, they have structural limitations in learning temporal order
information, which is crucial for time series problems. While past tasks were simple and
general enough to overlook these limitations, current real-world tasks involve many con-
straints and data-specific issues with diverse variables, necessitating approaches from vari-
ous perspectives. Each architecture has its own strengths, and these characteristics provide
valuable solutions for addressing diverse contemporary time series forecasting challenges.
In this section, we will investigate the latest major models for each architecture and analyze
their technical features. The key characteristics of each backbone architecture have been
briefly summarized in comparison to Transformers in Table 6.
4.2.1 MLP-based models
MLP-based models have recently emerged as a key methodology for replacing Transform-
ers in time series forecasting tasks. The simple structure of MLPs makes them easy to han-
dle and interpret. Additionally, they perform well even in constrained environments with
limited computational resources and limited data. Their lightweight architectures enable fast
training and inference, making them increasingly important and widely used in contempo-
rary industries. Previously, interest in MLPs diminished due to their structural limitations,
such as the lack of sequential dependency, challenges with long-term dependency, diffi-
culties in processing high-dimensional data, and limitations in capturing periodic patterns.
However, recent advancements have enabled long-sequence learning and various technical
enhancements, leading to remarkable performance improvements.
N-BEATS (Oreshkin et al 2020), consisting of simple Fully Connected (FC) layers, dem-
onstrated superior performance compared to traditional statistical models. This model uti-
lizes a block-based architecture with repeatedly stacked backcast and forecast paths and
enhances generalization performance through ensemble learning. By applying decomposi-
tion, it separates trend and seasonality, modeling them using Polynomial Basis and Fourier
Basis, respectively, making it highly interpretable. BMoreover, recent studies have improved
the N-BEATS model to predict various quantiles, enabling probabilistic forecasting (Smyl
et al 2024). The improved N-HiTS (Challu et al 2023) model can handle multivariate data
and overcomes the limitations of N-BEATS by employing techniques such as multi-rate
signal sampling, non-linear regression, and hierarchical interpolation. Koopa (Liu et al
2024d) is a model designed to effectively handle non-stationary time series data by utilizing
Koopman theory to predict the dynamic changes of components. It uses a Fourier filter to
separate time-invariant and time-variant elements, which are then fed into respective Koop-
man predictors(KP). In KP, nonlinear time series data are linearly transformed, making
them easier to manage. To effectively capture the characteristics of each component, the
time-invariant KP uses a globally learned Koopman operator, while the time-variant KP
computes a local operator for predictions. TSMixer (Ekambaram et al 2023) is a lightweight
patch-based model that introduces the MLP-mixer from the computer vision field to the
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 37 of 95 216
time-series domain. It efficiently learns long-term and short-term dependencies through
inter-patch and intra-patch mixers respectively, and explicitly learns channel relationships
through an inter-channel mixer. To enhance the understanding of inter-channel correlations,
it adjusts the original forecast results using reconciliation heads and employs gated attention
to filter important features. By introducing these techniques, TSMixer upgrades the simple
MLP structure, resulting in improved performance that outperforms complex Transformer
models. FreTS (Yi et al 2024) is a model that leverages two key characteristics of the fre-
quency domain-global view and energy compaction-to directly train an MLP model in the
frequency domain. While existing models primarily use frequency transformation to verify
the periodicity of the model, this model distinguishes between channel and temporal depen-
dencies in the frequency domain as real and imaginary parts, respectively, and learns them
directly to better extract hidden features. TSP (Wang et al 2024e) utilizes a PrecMLP block
with a precurrent mechanism to effectively model temporal locality and channel depen-
dency. The precurrent mechanism combines previous information with current information
to create hybrid features at each time point, serving as a computationally-free method to
effectively recognize and process temporal locality. This lightweight MLP model comprises
an encoder, consisting of tMLP operating in the time dimension and vMLP operating in the
variable dimension, and a decoder using a linear model. FITS (Xu et al 2024c) is a very
lightweight model with fewer than 10,000 parameters, yet it demonstrates competitive per-
formance comparable to larger models. It performs interpolation through a complex linear
layer that learns amplitude scaling and phase shifts in the frequency domain, thereby
expanding the frequency representation of the input time series. By using a low-pass filter
to remove high-frequency components, which are often noise, the model efficiently repre-
sents the data and reduces the number of learnable parameters. U-Mixer (Ma et al 2024)
utilizes a hierarchical structure of U-Net’s encoder–decoder composed of MLPs to extract
and combine low-dimensional and high-dimensional features. Each MLP block processes
temporal dependencies and channel interactions separately, enabling stable feature extrac-
tion. Additionally, the model employs a stationary correction method to limit the differences
in data distribution before and after processing, thereby restoring the non-stationary infor-
mation of the data. By calculating the transformation matrix and mean difference between
the input and output data, the model adjusts the output to maintain temporal dependency,
thereby enhancing its prediction performance. TTMs (Ekambaram et al 2024) is a time
series foundation model that uses TSMixer as its backbone and relies solely on time series
data for rapid pre-training. This model is trained on the extensive collection of time series
datasets with diverse channels and resolutions from the Monash archive (Table 3). Despite
the data-specific characteristics of the time series datasets, TTMs demonstrate efficient
transfer learning and high generalization performance. TimeMixer (Wang et al 2024a) lever-
ages the observation that time series data exhibit distinct patterns at different sampling
scales. To extract important information from past data, multi-scale time series are gener-
ated through downsampling. In the Past-Decomposable-Mixing (PDM) block, the seasonal
and trend components are decomposed and mixed separately. The Future-Multipredictor-
Mixing (FMM) block then integrates predictions by ensembling multiple predictors, which
utilize the past information extracted at various scales. CATS (Lu et al 2024) enhances the
performance of multivariate time series forecasting by generating Auxiliary Time Series
(ATS) from the Original Time Series (OTS) and integrating them into the prediction pro-
cess. The model proposes various types of ATS constructors, each with different roles and
1 3

| 216  Page 38 of 95 |                                                                                             |                            |                                                                                                    |                                                                    |                                                                  | J. Kim et al.                                                        |
| ------------------ | ------------------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------- | -------------------------------------------------------------------- |
|                    |                                                                                             |                            |  sretemarap rewef htiw ecnamrof -dneped elbaterpretni yletaredoM  ledom dna erutcurts hparg no gni | -reffo ,sedon neewteb seicnednep  gninrael ni ecnamrofrep hgih gni | serutcurts dna sepyt atad tnereffid                              | -ten laicos ekil sksat ni serutcurts  ,smetsys noitadnemmocer ,skrow |
|                    |  ecnamrofrep hgih eveihca naC                                                               |                            | -rep hgih gniveihca ,ytixelpmoc                                                                    |                                                                    | -curts hparg suoirav eldnah naC  ot elbatpada ,stamrof dna serut |                                                                      |
|                    |  neewteb spihsnoitaler snraeL  ,serutcurts hparg gnisu sedon  xelpmoc gnirutpac ylevitceffe |                            |                                                                                                    | -ed xelpmoc gninrael ta slecxE                                     |                                                                  |                                                                      |
|                    | stesatad llams ylevitaler htiw                                                              |                            |                                                                                                    |                                                                    | snrettap pihsnoitaler cfiiceps                                   |                                                                      |
|                    |                                                                                             |  hparg no gnidneped seiraV |  dna ezis hparg no sdnepeD                                                                         |                                                                    |                                                                  |  hparg xelpmoc rof elbatiuS                                          |
sledom desab-NCG/NNG
shparg seires emit dna
smelborp cfiiceps ni
spihsnoitaler
|     |     | ytixelpmoc |     | ytixelpmoc |     |     |
| --- | --- | ---------- | --- | ---------- | --- | --- |
 gnol rof wols eb nac tub stesatad
 gnildnah ylevitceffe ,gnissecorp  yam tub seicnedneped laropmet  reisae ,elbaterpretni yletaredoM  ledom nialpxe dna dnatsrednu ot -divorp ,seicnedneped laitneuqes  tub ,gnitsacerof seires emit dna -neped mret-gnol htiw selggurts
|     |  atad laitneuqes ni dezilaicepS  htiw gniniart kciuq rof elbatius |     |     |     |     |     |
| --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
secneuqes gnol htiw elggurts  ,stesatad rellams no niart naC  rellams no ylevitceffe sniarT  ni ecnamrofrep tneicffius gni smelborp seires emit cfiiceps  NNR suoirav htiw elbisnetxE  atad laitneuqes rof evitceffE snoitacfiidom tuohtiw seicned
 dna mret-trohs rof elbatiuS
llams ylevitarapmoC
sledom desab-NNR
|     | atad detimil |     |     |     | serutcetihcra |     |
| --- | ------------ | --- | --- | --- | ------------- | --- |
secneuqes
roivaheb
 ,sreyal lanoitulovnoc sezilitU  ti gnikam ,tneicffie-retemarap elbalacs dna tneicffie-ecruoser -met lacol gnirutpac ta slecxE  lacol gnorts htiw smelborp rof -irav htiw elbazimotsuc ylisaE  laropmet dna laitaps gniriuqer
 cfiiceps gnirutpac ylevitceffe stesatad rellams no niart naC -lacol ot eud retsaf yllareneG  roirepus ,seicnedneped larop  snoitacilppa rof detius-lleW  ediw a rof evitceffe ,ytilacol smelborp seires emit fo egnar
|     |     |     |  erom dna rellams yllacipyT  hguorht elbaterpretni eroM  dna sretlfi fo snoitazilausiv |     |     |     |
| --- | --- | --- | -------------------------------------------------------------------------------------- | --- | --- | --- |
snoitulovnoc fo sepyt suo
sledom desab-NNC
| airetirc fo smret ni sremrofsnart htiw sledom gninrael peed rehto fo nosirapmoC 6 elbaT |                | snoitatupmoc dezi |     |              |     |     |
| --------------------------------------------------------------------------------------- | -------------- | ----------------- | --- | ------------ | --- | --- |
|                                                                                         | snrettap lacol |                   |     | spam erutaef |     |     |
snrettap
|     |  ylevitaler ,reyal elpmiS  dna tnemelpmi ot ysae |     |                          |  mret-trohs rof elbatiuS  ni ecnamrofrep tneicfi |                        |     |
| --- | ------------------------------------------------ | --- | ------------------------ | ------------------------------------------------ | ---------------------- | --- |
|     |  rellams no niart naC                            |     |  fo esu tneicffie ,llams |                                                  |  rof elbatsujda ylisaE |     |
sledom desab-PLM -fus htiw snoitciderp  suoirav rof elitasreV  gnitsacerof lareneg
smelborp cfiiceps
|     |     |     |  ylevitarapmoC  hgih ylevitaleR ytilibaterpretni |     |     |     |
| --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
tsaf ylevitaleR
sesac ynam
|     | terpretni |     | secruoser |     |     | smelborp |
| --- | --------- | --- | --------- | --- | --- | -------- |
stesatad
 noitnetta-fles xelpmoC stesatad egral seriuqeR seicnedneped mret-gnol  ro smelborp seires emit
 xelpmoc rof elbatiuS
|                    |     |  eud wols ylevitaleR | terpretni ot tlucffiiD |  gninrael rof elbatiuS |                   |     |
| ------------------ | --- | -------------------- | ---------------------- | ---------------------- | ----------------- | --- |
|  desab-remrofsnarT |     |  noitnetta labolg ot | evisnetni-retemarap    |                        |  xelpmoc seriuqeR |     |
sksat detaler-PLN
 ylevitarapmoC  erom dna regral
smsinahcem
|     | msinahcem |     |     |     | stnemtsujda |     |
| --- | --------- | --- | --- | --- | ----------- | --- |
sledom
ytilibaterpretnI
emit gniniarT
|     | stnemeriuqer |     |            | ecnamrofreP |             | noitacilppA |
| --- | ------------ | --- | ---------- | ----------- | ----------- | ----------- |
|     |              |     | ezis ledoM |             | ytilibixelF |             |
erutcurtS
airetirC
 ataD
1 3

A comprehensive survey of deep learning for time series forecasting:…
)deunitnoc(
6
elbaT
sledom
desab-NCG/NNG
sledom
desab-NNR
sledom
desab-NNC
sledom
desab-PLM
desab-remrofsnarT
airetirC
sledom
no
sdneped
tub
wol
yllareneG
lellarap
no
tneicffieni
tub
woL
dna
lanoitatupmoc
rewoL
rieht
ot
eud
rewoL
rieht
ot
eud
hgiH
erawdraH
ezis
hparg
erawdrah
stnemeriuqer
yromem
dna
erutcurts
relpmis
erutcurts
xelpmoc
stnemeriuqer
lanoitatupmoc
rewef
yllanoitatupmoc
dna
sdnamed
noitnetta-fles
evisnetni
smsinahcem
no
sdneped
tub
wol
yllareneG
htiw
esaercni
nac
tub
woL
ot
eud
egasu
yromem
rewoL
egasu
yromem
rewoL
egasu
yromem
rehgiH
egasu
yromeM
ezis
hparg
htgnel
ecneuqes
snoitarepo
dezilacol
elpmis
rieht
ot
eud
ecneuqes
lluf
ot
eud
rewef
dna
erutcurts
noitnetta
sretemarap
erutcurts
hparg
ot
eud
tlucffiiD
ecneuqes
ot
eud
tlucffiiD
eud
elbazilellarap
ylhgiH
elbazilellarap
ylhgiH
elbazilellarap
ylhgiH
lellaraP
seicnedneped
seicnedneped
noitulovnoc
tnednepedni
ot
tnednepedni
ot
eud
-inorhcnys
seriuqer
tub
gnissecorp
snoitarepo
snoitatupmoc
noitnetta
ot
eud
noitaz
smsinahcem
Page 39 of 95 216
1 3

216 Page 40 of 95 J. Kim et al.
objectives, combining them to maximize predictive performance. To effectively generate
and utilize ATS, the model structure and loss function incorporate three key principles: con-
tinuity, sparsity, and variability. Despite using a simple two-layer MLP predictor as the
foundation, CATS effectively predicts multivariate information through the use of ATS.
HDMixer (Huang et al 2024a) is a model that applies a Length-Extendable Patcher to over-
come the limitations of fixed-length patching. It measures the point-wise similarity with
fixed patches and compares the patch entropy loss, updating parameters to increase the
complexity of the extendable patches. Through the Hierarchical Dependency Explorer
mixer, it learns long-term, short-term dependencies and cross-variable dependencies.
SOFTS (Han et al 2024) proposes the STar Aggregate-Redistribute (STAR) Module to effec-
tively learn the relationships between channels. It converts the data from each channel into
high-dimensional vectors and then aggregates these vectors to extract comprehensive infor-
mation, referred to as the core. The generated core representation is then combined with the
time series representation of each channel and converted back to the time series dimension,
reducing complexity and enhancing robustness. SparseTSF (Lin et al 2024b) is an extremely
lightweight model that uses fewer than 1,000 parameters while demonstrating excellent
generalization performance. It downsamples the data into multiple periods, performs pre-
dictions on each generated sub-sequence, and then upsamples to create the overall predic-
tion sequence. While it shows limited performance only on data with clear periodic patterns,
it efficiently handles complex temporal dependencies with minimal computational resources.
TEFN (Zhan et al 2024) proposes a novel backbone model from the perspective of informa-
tion fusion to extract latent distributions from simple data structures. Based on evidence
theory (Shafer 1976), the Basic Probability Assignment Module maps each time and chan-
nel dimension of the time series data to a mass function in the event space. This mass func-
tion assigns probabilities to multiple possibilities for each data point, allowing for explicit
modeling of uncertainty. The generated mass functions are fused using their expected values
to derive the final predictions. This model achieves high predictive performance with few
parameters and fast training times. PDMLP (Tang and Zhang 2024) surpasses the perfor-
mance of complex transformer-based models using only simple linear layers and patching.
It divides the data into patches of various scales and embeds each patch with a single linear
layer. The embedding vectors are then decomposed into smooth components and residual
components containing noise, allowing the model to process the sequences in two ways:
intra-variable and inter-variable. AMD (Hu et al 2024b) introduces the AMS block, which
assesses the importance of various temporal patterns and generates appropriate weights for
each pattern. By simultaneously modeling the temporal and channel dependencies of the
input information decomposed into multiple scales, it effectively captures interactions at
different scales. Instead of merely integrating the results from each scale, it improves pre-
diction performance by reflecting the importance of each pattern through the weights.
4.2.2 CNN-based models
CNNs were primarily developed for image recognition and processing tasks because they
are highly effective at identifying 2D spatial patterns. Some studies have begun utilizing
Temporal Convolutional Networks (TCNs), which are 1D CNNs that move along the time
axis to recognize local patterns, effectively extracting key features of time series data. Addi-
tionally, CNNs can use filters of various sizes to capture patterns at multiple scales, allowing
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 41 of 95 216
them to effectively learn both short-term and long-term patterns in time series data. CNN’s
deep network technology and parallelism, which have been developed over a long period of
time, have provided high performance and reliability for time series forecasting. However,
the fixed filter size of CNNs lacks flexibility in learning complex patterns of long sequences
and poses challenges in capturing long-term dependencies. Furthermore, as the network
depth increases, there are limitations such as information loss, increased computational cost,
and higher memory usage. For these reasons, the relatively flexible Transformer, which is
advantageous for learning long-term dependencies, has gained more attention in time series
data processing. However, due to their superior ability to capture diverse local patterns
within long sequences, CNNs are once again receiving attention as a backbone architecture.
Recently, 3D convolution methodologies have been actively studied for handling com-
plex spatio-temporal time series data (Chen et al 2021c; Feng et al 2024a). 3D convolution
processes input data in three dimensions (2D spatial axes + temporal axis) using convo-
lution operations. This approach enables the extraction of richer patterns by processing
not only the temporal axis but also spatial or multi-dimensional aspects of the data. Such
methods have demonstrated high performance in region-based prediction tasks, and future
research is expected to focus on developing more sophisticated data representations and
learning structures.
TimesNet (Wu et al 2023) introduces the TimesBlock, which embeds 1D time series
into 2D tensors for analysis to effectively capture multi-periodicity. Extracting key frequen-
cies via Fast Fourier Transformation (FFT) expands the data into a 2D tensor, representing
intra-period variation in columns and inter-period variation in rows. It uses a parameter-
efficient Inception module with 2D kernels to capture temporal variations across various
scales. After converting back to a 1D tensor, it adaptively aggregates the data based on
the importance of frequency amplitude values. PatchMixer (Gong et al 2023) introduces a
patch-mixing design to efficiently replace the permutation invariant property of the Trans-
former’s attention mechanism. It learns intra-patch correlations using single-scale depth-
wise separable convolutions and inter-patch correlations using point-wise convolutions on
the patched input sequence. ModernTCN (Luo and Wang 2024) enhances the fundamen-
tal TCNs to make them more suitable for time series analysis. Using larger kernels than
conventional TCNs expands the effective receptive field, reducing the number of layers
and effectively capturing long-term dependencies. It separates depth-wise convolution and
point-wise convolution to independently learn temporal dependencies and feature depen-
dencies, thereby enhancing computational efficiency. Additionally, it explicitly handles
cross-variable dependency in multivariate time series data, resulting in improved perfor-
mance. ConvTimeNet (Cheng et al 2024b) follows the framework of a Transformer encoder,
replacing the role of self-attention with depthwise convolution and the role of multi-head
attention with convolutions of various kernel sizes to increase computational efficiency. It
uses Deformable Patch Embedding, which adaptively adjusts each patch’s size and posi-
tion based on the data. Depthwise convolutions capture temporal features for each chan-
nel, while point-wise convolutions model channel dependencies. ACNet (Zhang and Wang
2024) aims to effectively model temporal dependencies and nonlinear features. It starts by
removing unnecessary noise from the data using Wavelet Denoising. Then, it extracts tem-
poral features through Multi-Resolution Dilated Convolution and Global Adaptive Average
Pooling. To more accurately capture nonlinear features, Gated Deformable Convolution is
employed, which adaptively adjusts the sampling positions. Additionally, ACNet employs
1 3

216 Page 42 of 95 J. Kim et al.
dynamic prediction, retraining the model with new data if prediction performance declines.
FTMixer (Li et al 2024d) leverages the observation that the time domain effectively captures
local dependencies while the frequency domain excels at learning global dependencies. It
applies convolution in the frequency domain to capture global dependencies. Meanwhile, it
converts multi-scale patches using Discrete Cosine Transformation (DCT), which is com-
putationally simpler than Discrete Fourier Transformation (DFT), and then applies convolu-
tion to capture local dependencies.
4.2.3 RNN-based models
RNNs were fundamentally developed to process sequential data. Their recurrent structure
can effectively model the temporal dependencies of time series data. Gated RNN mod-
els, such as LSTM and GRU, have partially alleviated the long-term dependency issues of
vanilla RNNs. However, RNNs are difficult to parallelize because they process data sequen-
tially. This slow speed is particularly detrimental when handling long sequences. RNNs
also have inherent limitations in learning long-term dependencies and global information.
Transformers have effectively addressed these issues through self-attention mechanisms.
However, unlike Transformers, which rely on large datasets, RNN-based models can learn
effectively with smaller amounts of data. They also use memory efficiently and are well-
suited for real-time data processing due to their sequential nature, making them advanta-
geous for online streaming applications. Additionally, because time ordering is naturally
learned, RNNs still have inherent advantages over Transformers for time series processing.
PA-RNN (Zhang et al 2024c) aims to address prediction Uncertainty Quantification and
Model Compression issues for dependent time series data by proposing an optimization
methodology for Sparse Deep Learning. It applies a Mixture of Gaussian Prior to introduc-
ing sparsity to the parameters and uses a Prior Annealing technique to gradually increase
the strength of the prior distribution during the training process. Properties such as Poste-
rior Consistency, Structure Selection Consistency, and Asymptotic Normality ensure the
model’s theoretical validity. WITRAN (Jia et al 2024) proposes a new paradigm by imple-
menting information transmission in bi-granular flows to capture long-term and short-term
repetitive patterns. It models global and local correlations through the Horizontal Vertical
Gated Selective Unit (HVGSU), which uses bidirectional Gated Selective Cells (GSC). To
enhance the efficiency of information transmission through parallel processing, it applies the
Recurrent Acceleration Network (RAN). This approach results in excellent prediction per-
formance while reducing time complexity and maintaining memory complexity. SutraNets
(Bergsma et al 2023) transforms long sequences into multiple lower-frequency sub-series
in order to effectively predict long sequence time series data. It performs autoregressive
predictions among the sub-series, with each sub-series being conditionally predicted based
on the values of other sub-series. This approach reduces the signal path length and allows
for the generation of long sequences in fewer steps. Consequently, it mitigates the common
RNN problem of error accumulation and models long-distance dependencies better. Cross-
WaveNet (Huang et al 2024b) uses a dual-channel network to separate and process the sea-
sonality and trend-cyclic components of data. The input data are initially decomposed into
individual elements through series decomposition, and features are extracted using enriched
LSTM and GRU structures. These extracted features undergo a cross-decomposition pro-
cess to further refine the elements, which are then sent to each channel for integration.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 43 of 95 216
Series decomposition is performed at each RNN step, progressively filtering and reinte-
grating the seasonality and trend components to learn precise information. DAN (Li et al
2024c) proposes a new model that utilizes Polar Representation learning to predict long-
term time series data with high volatility. The Distance-weighted Auto-regularized Neural
network (DAN) distinguishes and learns the polar representations of distant and nearby
data, combining them to enhance prediction performance. It addresses the imbalance prob-
lem of extreme data, which occur infrequently but are critical for accurate predictions, using
Kruskal-Wallis Sampling and employs a Multi-Loss Regularization Method to effectively
learn both extreme and normal values simultaneously. RWKV-TS (Hou and Yu 2024) pro-
poses an efficient Recurrent Weighted Key-Value (RWKV) backbone characterized by lin-
ear time complexity and memory usage. It uses a Multi-head Weighted Key-Value (WKV)
Operator, which is similar to the self-attention mechanism but maintains linear time and
space complexity. Each head captures different temporal patterns, increasing the represen-
tational power of the information and enabling parallel computation, thus providing high
computational efficiency. This allows RWKV-TS to capture longer sequence information
more effectively than fundamental RNNs. CONTIME (Jhin et al 2024) introduces Continu-
ous GRU to minimize the prediction delay issue in time series forecasting. This approach
applies Neural ODE to the existing GRU, modeling data changes continuously over time.
The bi-directional structure integrates forward and backward through the time series data,
capturing more accurate temporal dependencies. By employing Time-Derivative Regular-
ization, the model is guided to learn the rate of change in predictions over time, enhancing
both the accuracy and speed of predictions.
4.2.4 GNN-based models
GNNs or GCNs are specialized in processing graph-structured data, being suitable for mod-
eling complex interactions and learning local patterns in time series data. Multivariate time
series data often involve interactions between variables, which can be effectively repre-
sented as relationships between nodes and edges. By assigning various attributes to nodes
and edges, richer representations can be learned, and the structural characteristics of specific
domains can be better reflected. Traditionally, various approaches such as GCN, ST-GCN,
GAT, and TGN have been proposed, contributing to the advancement of the time series
forecasting field.
However, these models primarily focus on learning local information from adjacent
nodes, leading to a lack of capability in learning global information and difficulty in cap-
turing long-term dependencies with distant nodes. The sequential calculation of nodes and
edges makes parallel processing challenging, and the models’ specificity to particular graph
structures reduces their generalization ability. These drawbacks have diminished interest in
GNN-based models. However, with the recent advancements in social networks, much of
current data naturally follows a graph structure. Various optimization techniques and hard-
ware acceleration technologies have been developed, making it possible to process large-
scale graph data. Additionally, the increased practical relevance due to the flexibility in
dynamically handling time-varying data has once again drawn researchers’ attention to this
architecture.
MSGNet (Cai et al 2024a) effectively learns the complex correlations of MTS data by
combining frequency domain analysis with adaptive graph convolution. It uses Fast Fourier
1 3

216 Page 44 of 95 J. Kim et al.
Transformation to identify key periods and transform time series data into various time
scales. Then, it employs Mixhop graph convolution to learn inter-channel correlations and
uses Multi-head Attention and Scale Aggregation to capture intra-series correlations. TMP-
Nets (Coskunuzer et al 2024) is a model proposed to learn features extracted from Temporal
MultiPersistence (TMP) vectorization and capture key topological patterns. It combines two
advanced topological data analysis techniques, Multipersistence and Zigzag Persistence,
to effectively capture topological shape changes in the data. Spatial Graph Convolution
is used to model dependencies between nodes in the graph, and the topological features
extracted with TMP vectors are learned using CNN. HD-TTS (Marisca et al 2024) is a model
that demonstrates high performance even with missing data through masking and hierarchi-
cal downsampling. It incrementally reduces data in the temporal and spatial processing
modules, learning various temporal and spatial dependencies. The model uses an attention
mechanism to learn the patterns of missing values and combines them with weights to gen-
erate the final prediction. ForecastGrapher (Cai et al 2024b) is based on the finding that the
attention mechanism is more suitable for modeling inter-channel correlations than temporal
correlations. Utilizing the similarity between GNN’s neighborhood aggregation and atten-
tion mechanisms, it linearly embeds each channel as a node and learns the relationships
between channels using GNN. Each GNN layer employs a self-learnable adjacency matrix
to independently learn the interactions between nodes. It uses learnable scalers to divide
node features into multiple groups and applies 1D convolution to each group.
4.2.5 Model-agnostic frameworks
Some studies propose model-agnostic methodologies that can be universally applied with-
out being limited to a specific model backbone. These studies focus on the intrinsic charac-
teristics of time series data or specific problems, improving model robustness by addressing
these issues. Model-agnostic architectures, not being tied to a particular model, allow for
flexible selection of the optimal model through various comparisons. They are also highly
reusable and make it easier to interpret and understand the model’s predictions, making
them applicable to a wide range of domains and scenarios.
These models primarily address the distribution shift problem, which is one of the core
issues in time series forecasting, and propose various plug-and-play alleviation methods.
The details related to this will be discussed in Sect. 5, while here, we will focus on other
methodologies, excluding distribution shift alleviation methods.
RobustTSF (Cheng et al 2024a) introduces a selective sampling algorithm to train a
resilient prediction model in Time Series Forecasting with Anomalies (TSFA). It calculates
anomaly scores based on the difference between the trend and the actual data, selecting
samples with scores below a certain threshold to train the model, thereby minimizing the
impact of anomalies. By analyzing three types of anomalies (Constant, Missing, Gaussian),
it identifies the most robust loss function as MAE. This approach addresses the discontinu-
ity issues of the traditional detection-imputation-retraining pipeline, enabling the model to
deliver more stable and consistent performance. PDLS (Hounie et al 2024) proposes a con-
strained learning approach by setting an upper bound on the loss at each time step. It controls
the loss by setting a constant upper bound (ϵ) for all time steps and introduces a variable
(ζ) that relaxes the constraints, allowing automatic adjustment during training. This model
overcomes the problem of existing methodologies that focus on averaging prediction per-
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 45 of 95 216
formance, which often leads to uneven error distributions. Leddam (Yu et al 2024) proposes
two independently usable modules, Learnable Decomposition and Dual Attention, to effec-
tively capture the complex patterns of inter-series dependencies and intra-series variations
in MTS. The Learnable Decomposition module replaces the traditional moving average
kernel with a learnable 1D convolution kernel initialized with a Gaussian distribution for
decomposition, making it more sensitive to critical information. The Dual Attention module
simultaneously models inter-data dependencies and intra-series variability using channel-
wise self-attention and auto-regressive self-attention. InfoTime (Qi et al 2024) proposes
a method to effectively utilize inter-channel and temporal correlations. For channel mix-
ing, it employs Cross-variable Decorrelation Aware feature Modeling (CDAM) to minimize
redundant information between channels and enhance useful mutual information. Addition-
ally, it uses TAM(Temporal correlation Aware Modeling) to maximize the temporal cor-
relations between the predicted future sequence and the target sequence. CCM (Chen et al
2024a) combines the strengths of the traditional channel-independent and channel-depen-
dent strategies to overcome their limitations. It dynamically clusters channels based on their
inherent similarities and learns representative patterns for each cluster to generate prototype
embeddings. Separate FFNs are used for each cluster to perform predictions for the channels
within the cluster, and the prototype embeddings enable zero-shot predictions. HCAN (Sun
et al 2024b) addresses the issue of excessive flattening caused by using the MSE loss func-
tion and proposes reconfiguring the prediction problem as a classification problem to better
learn high-entropy features. It extracts important features from the backbone model, divides
them into multiple layers and categories, and uses an Uncertainty-Aware Classifier at each
layer to reduce uncertainty. It learns relative prediction values within each classified cate-
gory and integrates the prediction results from multiple layers through the Hierarchy-Aware
Attention module. This approach effectively captures the complex patterns and variability
in time series data. TDT Loss (Xiong et al 2024) points out the error accumulation issue in
the traditional auto-regressive approach which recursively models Temporal Dependencies
among Targets (TDT). To effectively capture changes between consecutive time points, it
represents TDT using first-order differencing. The final TDT loss combines the target pre-
diction loss, TDT values prediction loss, and an adaptive weight, allowing the model to
dynamically balance between target prediction and TDT learning. Thus, TDT loss replaces
the optimization objective of non-autoregressive models.
The different deep learning models and their methodologies discussed so far are sum-
marized in Table 7.
4.3 Emergence of foundation models
In recent years, foundation models have demonstrated remarkable performance and strong
zero-shot capabilities across various tasks and domains, leading to increased focus (Touvron
et al 2023; Liu et al 2024a; Li et al 2023; Achiam et al 2023; Gallifant et al 2024; Radford
et al 2021). While significant progress has been made in domains like vision and language,
developing foundation models for time series data has faced several challenges. Firstly, time
series data exhibit distinct characteristics depending on the dataset. For instance, electro-
cardiogram (ECG), weather, and sensor data from industrial processes have unique proper-
ties in terms of variables, frequency, periodicity, and noise, often requiring domain-specific
knowledge for effective modeling. Additionally, unlike the vision and language domains,
1 3

| 216  Page 46 of 95 |     |     | J. Kim et al. |
| ------------------ | --- | --- | ------------- |
Table 7 Taxonomy and methodologies of fundamental deep learning architectures for time series forecasting
| Model name | Base | Main methodology | Channel  Publi- |
| ---------- | ---- | ---------------- | --------------- |
correlation cation
| N-BEATS | MLP | ⋅ Neural basis expansion (polyno- | CI 2020 |
| ------- | --- | --------------------------------- | ------- |
mial basis and Fourier basis)
| N-HiTS |     | ⋅ Neural hierarchical interpolation | CI 2023 |
| ------ | --- | ----------------------------------- | ------- |
⋅ Multi-rate data sampling
| Koopa |     | ⋅ Koopa block with koopman  | CD 2023 |
| ----- | --- | --------------------------- | ------- |
predictor(KP)
| TSMixer |     | ⋅ MLP mixer layer architecture | CI/CD 2023 |
| ------- | --- | ------------------------------ | ---------- |
⋅ Gated attention (GA) block
⋅ Online hierarchical patch recon-
ciliation head
| FreTS |     | ⋅ Frequency-domain MLPs          | CD 2023 |
| ----- | --- | -------------------------------- | ------- |
| TSP   |     | ⋅ PrecMLP block with precurrent  | CD 2024 |
mechanism
| FITS |     | ⋅ Complex frequency linear  | CI 2024 |
| ---- | --- | --------------------------- | ------- |
interpolation
⋅ Low pass filter (LPF)
| U-Mixer |     | ⋅ Unet Encoder–decoder with MLPs | CD 2024 |
| ------- | --- | -------------------------------- | ------- |
⋅ Stationarity correction
| TTMs |     | ⋅ Multi-resolution pre-training via  | CD 2024 |
| ---- | --- | ------------------------------------ | ------- |
TTM backbone (TSMixer blocks)
⋅ Exogenous mixer
| TimeMixer |     | ⋅ Past-decomposable-mixing  | CD 2024 |
| --------- | --- | --------------------------- | ------- |
(PDM) block
⋅ Future-multipredictor-mixing
(FMM) block
| CATS |     |     | CD 2024 |
| ---- | --- | --- | ------- |
⋅ Auxiliary time series (ATS)
constructor
| HDMixer |     | ⋅ Length-extendable patcher | CD 2024 |
| ------- | --- | --------------------------- | ------- |
⋅ Patch entropy loss
⋅ Hierarchical dependency explorer
| SOFTS |     | ⋅ STar Aggregate-redistribute  | CD 2024 |
| ----- | --- | ------------------------------ | ------- |
module
| SparseTSF |     | ⋅ Cross-period sparse forecasting | CI 2024 |
| --------- | --- | --------------------------------- | ------- |
| TEFN      |     | ⋅ Basic probability assignment    | CD 2024 |
(BPA) module
| PDMLP |     | ⋅ Multi-scale patch embedding and  | CD 2024 |
| ----- | --- | ---------------------------------- | ------- |
feature decomposition
⋅ Intra-, Inter-variable MLP
| AMD |     |     | CD 2024 |
| --- | --- | --- | ------- |
⋅ Multi-scale decomposable mixing
(MDM) block
⋅ Dual dependency interaction
(DDI) Block
⋅ Adaptive multi-predictor synthesis
(AMS) block
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 47 of 95  216
T able 7 (continued)
| Model name | Base | Main methodology | Channel  Publi- |
| ---------- | ---- | ---------------- | --------------- |
correlation cation
| TimesNet | CNN | ⋅ Transform 1D-variatios into  | CD 2023 |
| -------- | --- | ------------------------------ | ------- |
2D-variations
⋅ Timesblock
| PatchMixer |     | ⋅ Patch embedding | CI 2023 |
| ---------- | --- | ----------------- | ------- |
⋅ PatchMixer layer with patch-
mixing design
| ModernTCN |     | ⋅ ModernTCN block with DWConv  | CD 2024 |
| --------- | --- | ------------------------------ | ------- |
and ConvFFN
| ConvTimeNet |     | ⋅ Deformable patch embedding | CD 2024 |
| ----------- | --- | ---------------------------- | ------- |
⋅ Fully convolutional blocks
| ACNet |     | ⋅ Temporal feature extraction  | CD 2024 |
| ----- | --- | ------------------------------ | ------- |
module
⋅ Nonlinear feature adaptive extrac-
tion module
| FTMixer |     | ⋅ Frequency channel convolution | CD 2024 |
| ------- | --- | ------------------------------- | ------- |
⋅ Windowing frequency convolution
| PA-RNN | RNN | ⋅ Mixture Gaussian prior | CI 2023 |
| ------ | --- | ------------------------ | ------- |
⋅ Prior annealing algorithm
| WITRAN |     | ⋅ Horizontal vertical gated selective  | CI 2023 |
| ------ | --- | -------------------------------------- | ------- |
unit
⋅ Recurrent acceleration network
| SutraNets |     | ⋅ Sub-series autoregressive  | CI 2023 |
| --------- | --- | ---------------------------- | ------- |
networks
| CrossWaveNet |     | ⋅ Deep cross-decomposition | CD 2024 |
| ------------ | --- | -------------------------- | ------- |
⋅ Dual-channel network
| DAN |     | ⋅ RepGen and RepMerg with polar  | CI 2024 |
| --- | --- | -------------------------------- | ------- |
representation learning
⋅ Distance-weighted multi-loss
mechanism
⋅ Kruskal–Wallis sampling
| RWKV-TS |     | ⋅ RWKV blocks with multi-head  | CD 2024 |
| ------- | --- | ------------------------------ | ------- |
WKV operator
| CONTIME |     | ⋅ Bi-directional continuous GRU  | CI 2024 |
| ------- | --- | -------------------------------- | ------- |
with neural ODE
| MSGNet | GNN/GCN | ⋅ ScaleGraph block with scale  | CD 2024 |
| ------ | ------- | ------------------------------ | ------- |
identification
⋅ Multi-scale adaptive graph
convolution
⋅ Multi-head attention and scale
aggregation
| TMP-Nets |     | ⋅ Temporal MultiPersistence (TMP)  | CD 2024 |
| -------- | --- | ---------------------------------- | ------- |
vectorization
| HD-TTS |     | ⋅ Temporal processing module with  | CD 2024 |
| ------ | --- | ---------------------------------- | ------- |
Temporal message passing
⋅ Spatial processing module with
Spatial message passing
| ForecastGrapher |     | ⋅ Group feature convolution GNN  | CD 2024 |
| --------------- | --- | -------------------------------- | ------- |
(GFC-GNN)
1 3

216 Page 48 of 95 J. Kim et al.
T able 7 (continued)
Model name Base Main methodology Channel Publi-
correlation cation
RobustTSF Model-agnostic ⋅ RobustTSF Algorithm – 2024
PDLS ⋅ Loss shaping constraints – 2024
⋅ Empirical dual resilient and con-
strained learning
Leddam ⋅ Learnable decomposition module CD 2024
⋅ Dual attention module
InfoTime ⋅ Cross-variable decorrelation CD 2024
aware feature modeling (CDAM)
⋅ Temporal aware modeling (TAM)
CCM ⋅ Channel clustering and Cluster CD 2024
loss
⋅ Cluster-aware feed forward
HCAN ⋅ Uncertainty-aware classifier – 2024
(UAC)
⋅ Hierarchical consistency loss
(HCL)
⋅ Hierarchy-aware attention (HAA)
TDT loss ⋅ Temporal dependencies among – 2024
targets (TDT) loss
-: Indicates that the feature is model-agnostic and depends on which backbone model is applied
where large-scale pre-training corpora can be relatively easily constructed from publicly
available sources like the web, collecting time series data is more difficult due to high acqui-
sition costs and security concerns. Despite these obstacles, research on time series founda-
tion models is essential for improving model scalability and generality. This necessity has
led to active exploration in several key directions, particularly in the field of time series
forecasting (Table 8).
4.3.1 Sequence modeling with LLMs
One prominent approach leverages the sequence modeling capabilities of LLMs. LLMs
have revolutionized deep learning with their groundbreaking generalizable sequence mod-
eling. Given the sequential nature of both text and time series data, extending the sequen-
tial capabilities of language models to time series is a natural progression. Early research
includes GPT4TS (Zhou et al 2023), which demonstrates that by freezing most of the lan-
guage model’s backbone and fine-tuning only the layer normalization parameters and posi-
tional embeddings on time series data, GPT4TS can serve as a general time series task solver
for forecasting, anomaly detection, and classification. Additionally, PromptCast (Xue and
Salim 2023) introduces a framework where numerical time series sequences are input as
text prompts to a large language model. Then the model outputs the forecasting results in
a question-answering format. This approach integrates domain-specific knowledge through
text and provides forecasting results in a human-friendly format.
Both GPT4TS and PromptCast rely on fine-tuning to achieve their results. In contrast,
without fine-tuning, LLMTime (Gruver et al 2023) has demonstrated impressive zero-shot
forecasting capabilities. The main idea of LLMTime is encoding time series data as a string
of numerical digits, which emphasizes the importance of preprocessing and its inherent
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 49 of 95 216
Table 8 Taxonomy and methodologies of foundation models for time series forecasting
Approach Model name Main improvement and methodology Publication
Sequential mod- GPT4TS ⋅ Demonstrate the effectiveness of LLM for time series 2023
eling with LLM modeling
⋅ Fine-tune the layer normalization and positional em-
bedding parameters
PromptCast ⋅ Enable text-level domain-specific knowledge for TSF 2023
⋅ Cast TSF problem into question and answering format
LLMTime ⋅ Zero-shot TSF with pre-trained LLMs 2023
⋅ Covert time series input into a string of digits
Time-LLM ⋅ Align time series modality into text modality 2024
⋅ Introduce patch reprogramming to mitigate a large
reprogramming space
Pre-training Lag-Llama ⋅ First pre-training based time series foundation model 2024
⋅ Pre-train a decoder-only model with autoregressive
loss
TimesFM ⋅ Pre-trained with hundreds of billions time steps 2024
⋅ Autoregressive decoding with arbitrary forecasting
length
CHRONOS ⋅ Learning the language of time series 2024
⋅ Utilize tokenizer to capture the intrinsic language of
time series
UniTS ⋅ Explicit consideration of multivariate TSF 2024
⋅ Provide variate IDs to directly consider multiple
variables
dependencies. To align the time series modality with the language modality, Time-LLM (Jin
et al 2024) introduces the concept of patch reprogramming. This concept aims to mitigate
the challenges of a large reprogramming space and attempts to connect time series local
characteristics with language semantics, such as “short up”. While patch reprogramming
offers more flexibility by reducing the reliance on large-scale time series corpora, it also
presents the challenge of adapting time series data to fit the characteristics of large language
models.
4.3.2 Pre-training
Another approach that focuses on building large-scale time series corpora to pre-train time
series foundation models from scratch has emerged. An example is Lag-LLaMA (Rasul et al
2024), which uses a decoder-only Transformer to generate forecasting results, enabling
probabilistic forecasting. Lag-LLaMA also consolidates 27 publicly available forecasting
datasets from various domains to create a comprehensive pre-training corpus. On the other
hand, TimesFM (Das et al 2024) extends beyond publicly available forecasting datasets by
incorporating additional pre-training corpora based on Google Trends and Wiki Pageview
statistics. It also utilizes synthetic datasets generated from piece-wise linear trends, autore-
gressive processes, and sine and cosine functions to capture universal characteristics. The
entire pre-training corpus spans hundreds of billions of time steps. While most of the time
series foundation models rely on temporal embedding, CHRONOS (Ansari et al 2024) takes
a different idea by learning a patch-based tokenizer, similar to conventional language mod-
els, to capture the intrinsic “language” of time series data.
1 3

216 Page 50 of 95 J. Kim et al.
Conventional foundation models often overlook the relationships between variables in
multivariate time series forecasting, typically extending to multivariate forecasting by inde-
pendently combining univariate forecasts based on channel independence. Uni2TS (Woo
et al 2024) addresses this limitation by explicitly considering the expansion to arbitrary mul-
tivariate time series using variate IDs. Additionally, it leverages a large-scale time series data-
set called LOTSA, which accounts for multi-domain and multi-frequency characteristics.
4.4 Advance of diffusion models
Diffusion models are renowned generative models that have gained prominence for their
ability to produce high-quality images, as demonstrated by DALL-E2 (Ramesh et al 2022),
Stable Diffusion (Rombach et al 2022), and Imagen (Saharia et al 2022). In addition to their
success in image generation, diffusion models have shown excellent performance in various
fields, such as audio generation, natural language processing, and video generation (Cao
et al 2024). Consequently, there has been a growing number of research papers exploring
their application in time series forecasting.
Diffusion models, theoretically proposed by Sohl-Dickstein et al (2015), are inspired by
non-equilibrium statistical physics. They learn by progressively adding noise to the data
and then gradually reversing the process to recover the original data. However, this initial
research lacked concrete methods for training, making practical implementation challeng-
ing. This issue was addressed by Denoising Diffusion Probabilistic Models (DDPM) (Ho
et al 2020) and Noise Conditional Score Networks (NCSN) (Song and Ermon 2019). DDPM
models the forward and reverse processes explicitly based on a probabilistic approach,
enabling efficient learning. NCSN, on the other hand, employs score matching techniques
to refine the noise removal process, resulting in the generation of higher-quality samples.
A diffusion model operates through two primary processes: the forward process and the
reverse process. In the forward process, noise is gradually added to the data until it trans-
forms into complete noise. Conversely, the reverse process reconstructs meaningful data
from random noise. By training a denoising network, the model generates data by injecting
random values and processing them through the reverse process.
Diffusion models have a significant advantage in modeling uncertainty through the for-
ward and reverse processes. By providing multiple possible prediction outcomes instead of
a single prediction, it can reflect the uncertainty of the real world, making it highly benefi-
cial for TSF. Therefore, it can offer prediction confidence intervals or enable probabilistic
forecasting, thereby contributing to decision-making.
For forecasting tasks, it is crucial to employ conditional generation, where conditions are
incorporated into the model to produce data that aligns with the given conditions. In this
context, historical data is used as a condition and injected into the model to enable it to learn
and predict future values. Figure 12 illustrates the diffusion model process, visualizing the
transition from data to noise and back to data. Here, the addition of conditions explains the
concept of the conditional diffusion model.
Diffusion-based models for time series forecasting have achieved significant performance
improvements through the introduction of effective conditional embedding, the integration
of time series feature extraction, and advancements in the diffusion models themselves. The
following sections explain the key characteristics of diffusion-based models according to
these classification criteria, and Table 9 provides a clear summary of this information.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 51 of 95  216

Fig. 12 Conditional diffusion process for time series data
Table 9 Taxonomy and methodologies of diffusion models for time series forecasting
Main  Model name Main methodology Diffusion  Conditional  Pub-
| improvement |     |     | type type | lica- |
| ----------- | --- | --- | --------- | ----- |
tion
Effective condi- TimeGrad ⋅ Autoregressive DDPM using  DDPM Explicit 2021
| tional embedding |      | RNN and dilated convolution      |               |      |
| ---------------- | ---- | -------------------------------- | ------------- | ---- |
|                  | CSDI | ⋅ 2D Attention for temporal and  | DDPM Explicit | 2021 |
Feature dependency
⋅ Self-supervised training for
imputation
|     | SSSD     | ⋅ Combination of S4 model | DDPM Explicit | 2023 |
| --- | -------- | ------------------------- | ------------- | ---- |
|     | TimeDiff | ⋅ Future mixup            | DDPM Explicit | 2023 |
⋅ Autoregressive initialization
|     | TMDM | ⋅ Integration of diffusion and  | DDPM Explicit | 2024 |
| --- | ---- | ------------------------------- | ------------- | ---- |
transformer-based models
Time-series fea- Diffusion-TS ⋅ Decomposition techniques DDPM Guidance 2024
| ture extraction |     | ⋅ Instance-aware guidance  |     |     |
| --------------- | --- | -------------------------- | --- | --- |
strategy
Diffusion in  ⋅ Diffusing in the frequency  SDE Explicit 2024
|     | frequency | domain                    |               |      |
| --- | --------- | ------------------------- | ------------- | ---- |
|     | MG-TSD    | ⋅ Multi-granularity data  | DDPM Explicit | 2024 |
generator
⋅ Temporal process module
⋅ Guided diffusion process
module
|     | mr-Diff | ⋅ Integration of decomposi- | DDPM Explicit | 2024 |
| --- | ------- | --------------------------- | ------------- | ---- |
tion and multiple temporal
resolutions
| SDE | ScoreGrad | ⋅ Continuous energy-based  | SDE Explicit | 2021 |
| --- | --------- | -------------------------- | ------------ | ---- |
generative model
|     | D⌃3 M | ⋅ Decomposable denoising dif- | SDE Explicit | 2024 |
| --- | ----- | ----------------------------- | ------------ | ---- |
fusion model based on explicit
solutions
Latent diffusion  LDT ⋅ Symmetric time series  DDPM Guidance 2024
| model |     | compression |     |     |
| ----- | --- | ----------- | --- | --- |
⋅ Latent diffusion transformer
Guidance TSDiff ⋅ Observation self-guidance DDPM Guidance 2023
1 3

216 Page 52 of 95 J. Kim et al.
4.4.1 Effective conditional embedding
Early diffusion-based models for time series forecasting focused on effective conditional
embedding to guide the reverse process (Li et al 2024b). Typically, for forecasting tasks,
conditional diffusion models use past data as a condition to predict the future. Therefore, the
meticulous construction of the condition is paramount for the denoising model to effectively
learn the data and enhance prediction performance. This highlights the importance of data
preparation in the forecasting process. This preparation allows the model to effectively uti-
lize past information, thereby enhancing the accuracy of future time-series predictions and
improving the model’s ability to learn from historical data.
TimeGrad (Rasul et al 2021) is the first notable diffusion model that operates using an
autoregressive Denoising Diffusion Probabilistic Model (DDPM) (Ho et al 2020) approach.
It encodes past data with an RNN, using the hidden state in a conditional diffusion model
for forecasting. The hidden state encapsulates information from past sequential data, captur-
ing temporal dependencies effectively. The denoising network employs dilated ConvNets
with residual connections, adopted from WaveNet (Van Den Oord et al 2016) and Dif-
fWave (Kong et al 2021), which are designed for audio generation. Unlike the commonly
used U-net for image synthesis in diffusion models, TimeGrad utilizes a broader recep-
tive field suitable for time series data, similar to audio. CSDI (Tashiro et al 2021) cap-
tures temporal and feature dependencies of time series using a two-dimensional attention
mechanism. Designed for both forecasting and imputation tasks, CSDI replaces RNNs with
Transformers for imputation since RNNs are not suitable. The attention mechanism learns
the relationships across all positions in the input sequence, capturing long-term dependen-
cies effectively. Therefore, for long-term time series forecasting, using attention is more
advantageous than RNNs and dilated convolution, as seen in TimeGrad. SSSD (Alcaraz and
Strodthoff 2023) demonstrates that replacing the Transformer used as the denoising network
in CSDI with the S4 model (Gu et al 2022) yields superior performance. This is because
S4 is more efficient and better at capturing long-term dependencies compared to the high
computational complexity required for Transformer attention. TimeDiff (Shen and Kwok
2023) enhances prediction accuracy by using future mixups during training, mixing past
data with actual future values to generate conditional signals. Including some actual future
values helps the model create effective conditional signals for more accurate predictions.
Additionally, it addresses the boundary disharmony issue in non-autoregressive models like
CSDI and SSSD. TimeDiff uses a simple statistical model, the Linear Autoregressive model,
to provide an initial guess, alleviating the boundary disharmony problem. TMDM (Li et al
2024b) offers an extreme form of effective conditional embedding. It states that the best
condition is the prediction itself, using prediction values from transformer-based models
like Informer (Zhou et al 2021) or Autoformer (Wu et al 2021), which have shown good
performance in time series forecasting tasks, as the condition. This allows the Transformer
to handle the estimated mean while the diffusion model focuses on uncertainty estimation.
Unlike previous researches that utilize conditional embeddings only in the reverse process,
TMDM uses conditional information as prior knowledge for both the forward and reverse
processes.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 53 of 95 216
4.4.2 Time series feature extraction
Time series data hides various features, and there are techniques to extract these unique
characteristics effectively. Thus, many works have emerged that combine time series feature
extraction methods with diffusion models to understand the complex patterns in time series
data and improve prediction performance.
Decomposition
Decomposition techniques involve breaking down time series data into components such
as trend, seasonality, and irregularity, analyzing the unique patterns of each component. Dif-
fusion-TS (Yuan and Qiao 2024) points out that conventional methods cannot properly learn
each component because the forward process causes the components to collapse. There-
fore, it models the decomposed time series data individually during the diffusion process,
learning each component, such as trend, seasonality, and residuals, independently and then
recombining them to restore the entire time series data.
Frequency domain
Fourier analysis, a type of decomposition technique, converts time series data into the
frequency domain to analyze periodic components. This method helps identify periodic
patterns and remove noise. Crabbé et al (2024) explore the idea that the representation of
time series data in the frequency domain can provide useful inductive biases for score-based
diffusion models. This paper demonstrates that the components of time series data are more
clearly represented in the frequency domain, and diffusion models in the frequency domain
outperform those in the time domain.
Multi-scale
Multi-scale techniques analyze time series data at various time scales, effectively extract-
ing long-term trends and diverse features. This approach plays a crucial role in understand-
ing the complex patterns of time series data to improve prediction performance. MG-TSD
(Fan et al 2024b) observes that the forward process of diffusion models aligns with gradu-
ally smoothing fine data into coarser representations. It suggests that coarse-granularity data
can serve as effective guides in the intermediate stages of diffusion models. In other words,
the initial stages of the reverse process involve coarse-granularity data, guiding the process
to intermediate-stage targets. This multi-granularity level approach helps learn various lev-
els of information, enhancing prediction stability and accuracy. mr-Diff (Shen et al 2024)
constructs time series data at multiple resolutions, performing sequential predictions at each
resolution. In the initial stages, it predicts coarse data, and in subsequent stages, it uses these
predictions as conditions to generate finer data gradually. This structure incrementally adds
finer patterns and noise at each stage, ultimately reconstructing high-resolution time series
data. This allows for effective prediction of both long-term trends and short-term fluctua-
tions in time series data.
4.4.3 Additional approaches
Beyond the two main approaches mentioned earlier, there are numerous examples where
techniques evolving from the diffusion framework itself are applied to models for time
series forecasting.
Score-based generative modeling through SDEs
1 3

216 Page 54 of 95 J. Kim et al.
Score-Based Generative Modeling through Stochastic Differential Equations (SDEs)
(Song et al 2021) serves as continuous energy-based generative models, handling data in
a continuous time domain, thus reflecting natural and precise changes and noise in the real
world. The previously discussed methods are based on DDPM (Ho et al 2020), which add
and remove noise incrementally using fixed-time steps. However, the DDPM approach
faces challenges such as specific functional constraints and sensitivity to hyperparameters.
Some research applying SDEs overcomes these limitations and explores diverse approaches.
ScoreGrad (Yan et al 2021) is the first work to apply SDE, overcoming the constraints of
DDPM-based models and offering a more flexible and powerful generative model. D3M
(Yan et al 2024) addresses the limitations of conventional SDEs, such as the complexity of
determining drift and diffusion coefficients and slow generation speed, by utilizing a decom-
posable noise-removal diffusion model based on explicit solutions. This method reduces
computational complexity through clear SDE formulations and separates the signal decay
and noise injection processes in model design. As a result, it enhances model efficiency and
accuracy while accelerating generation speed. Crabbé et al (2024) improve denoising score
matching in the frequency domain by using mirrored Brownian motions instead of standard
Brownian motion, emphasizing the symmetry between components when applying SDEs.
Latent diffusion model
Latent Diffusion Model (Rombach et al 2022) is a generative model that operates not on
the original data directly but within a latent space where the diffusion process takes place.
Transforming data into the latent space reduces complexity and stabilizes the training pro-
cess, resulting in high-quality outputs. LDT (Feng et al 2024b) applies the concept of the
latent diffusion model to time series data, addressing the non-stationarity issues that often
arise during the compression into the latent space. Dynamically updating statistical proper-
ties during the autoencoder training process effectively overcomes these challenges and
enhances model performance.
Guidance
Some works use guidance instead of explicitly feeding conditions into the denoising
network for forecasting. Diffusion-TS (Yuan and Qiao 2024) employs classifier guidance,
using a separate classifier to guide the sampling process through the gradients of the clas-
sifier. This method maintains the basic unconditional diffusion model while performing
conditional generation tasks through various classifiers. It generates samples that are bet-
ter aligned with specific conditions, resulting in higher-quality outputs. However, classifier
guidance requires a classifier for each time step, which necessitates training a new classifier
instead of using pre-trained ones. LDT (Feng et al 2024b) uses classifier-free guidance,
learning both conditional and unconditional models within a single model to perform con-
ditional sampling. This work eliminates the need for an additional classifier and implicitly
obtains a classifier, making implementation simpler and more efficient. TSDiff (Kollovieh
et al 2024) proposes observation self-guidance, allowing the use of an unconditional dif-
fusion model for conditional generation without separate networks or modifications to the
training process.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 55 of 95 216
4.5 Debut of the Mamba
4.5.1 History of the state space models (SSMs)
One of the notable recent developments is the emergence of a new architecture called Mamba
(Gu and Dao 2024). In an atmosphere previously influenced by Transformers, Mamba has
garnered significant interest from researchers and is rapidly establishing its own ecosystem.
RNNs, which were once the mainstream in sequence modeling, lost their dominance
after the advent of Transformers. This was due to the limitations in information encapsula-
tion of a “context” (single vector) in RNN-based encoder–decoder models and the slow
training speed inherent in their recurrent nature. In contrast, the parallelism of the attention
mechanism and its ability to focus on all individual pieces of information overcame the limi-
tations of RNNs and demonstrated superior performance. However, new challenges have
emerged with Transformers, such as the quadratic computational complexity, which limits
the window length, and the increased memory requirements for processing long sequences.
Subsequently, many efforts have been made to overcome the limitations of both approaches
while preserving their advantages. In this context, some research that continues the philoso-
phy of RNNs has turned its attention to state space models (SSMs) (Kalman 1960).
SSM is a mathematical framework used to model the dynamic state of a system that
changes over time, compressing only the essential information for effective sequential mod-
eling. SSM describes the relationship between the internal state of the system and external
observations and is used in various fields such as control theory, signal processing, and time
series analysis. It comprises a ‘State equation’ that explains how the internal state changes
over time and an ‘Observation equation’ that explains how the internal state is transformed
into external observations. Although it is a continuous model that performs linear transfor-
mations on the current hidden state and input, it can handle discrete sequences like time
series through discretization (Fig. 13). It closely resembles RNNs in that it combines obser-
vation data and hidden state data.
However, SSMs have different characteristics from RNNs in that they are linear and
time-invariant (LTI). This means that the operations performed on each token do not vary,
allowing for the pre-computation of global kernels. In other words, the parameter matrices
of the system do not change over time and operate consistently across time. Therefore, the
Fig. 13 Diagram of discretized state space model
1 3

216 Page 56 of 95 J. Kim et al.
ability to precompute globally applicable kernels enables parallel processing, which can
overcome the limitations of RNNs.
Early applications of SSMs, such as the S4 (Gu et al 2021) model, utilized diagonal-
ization of the transition matrix to effectively model long-term dependencies in long and
complex sequence data. These models were able to achieve high performance when com-
bined with deep learning architectures like Transformers, RNNs, and CNNs. Subsequently,
based on S4, advanced blocks like H3 (Fu et al 2023) were developed, which hierarchically
structured convolution, gating, and MLP to provide more efficient and powerful sequence
modeling (Fig. 14).
4.5.2 Introduction of the Mamba
SSMs have fixed state transition and observation equations, which limits their ability to flex-
ibly handle input data. Furthermore, due to their inherent continuous system origins, they
are weaker in information-dense and discrete domains such as text.
Mamba addresses these limitations of SSMs by introducing an advanced deep struc-
tured SSM model with selective SSM. It is designed so that the parameters of the SSM
dynamically change depending on the input, allowing for selective memory or disregard of
specific parts of the sequence, enabling efficient data processing. However, this approach,
while enhancing the system’s flexibility to better learn complex patterns, sacrifices the par-
allel processing advantages of SSMs. To compensate, traditional techniques such as kernel
fusion, parallel scan, and recomputation are applied to efficiently implement selective SSMs
on GPUs. Mamba adopts a simplified architecture centered around selective SSM, replacing
the first multiplicative gate in the traditional H3 block with an activation function and incor-
porating an SSM into the gated MLP block. Due to the absence of attention mechanisms or
separate MLP blocks, computational complexity is reduced, resulting in efficient training,
fast inference, and high scalability and versatility.
Fig. 14 Structure of the Mamba block
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 57 of 95 216
4.5.3 Applications of the Mamba
In the field of time-series forecasting, there is a growing trend to apply Mamba. A lot of
variants based on Mamba have been proposed to address TSF tasks, and these models are
reported to exceed the performance of Transformer SOTA models.
Most of these models typically share the following common features:
● They aim to ensure stability in large networks. Mamba, based on SSM, heavily relies
on the eigenvalues of the system’s dynamic matrix. Since the general solution of the
system is expressed as an exponential function of the eigenvalues, if the real part of the
eigenvalues is positive, the system cannot converge and becomes unstable. Therefore, a
key feature is the ideation aimed at improving this instability.
● They explicitly incorporate the learning of channel correlations. Recent research has
demonstrated the superiority of channel dependence (CD) learning strategies, and the
adoption of the CD strategy by the iTransformer, which shows SOTA performance, has
further heightened this trend. This is a common feature observed in other foundational
models as well.
● They incorporate various techniques from transformer-based models. Mamba-based
models, which integrate various techniques from Transformers such as patching, fre-
quency domain application, bidirectional processing, and FFN incorporation, are dem-
onstrating significant performance improvements. The diverse techniques developed
over many years of research on Transformer models provide valuable ideation for
Mamba variants.
The following are representative examples of Mamba-based models for handling TSF tasks
and their key technical features (Table 10).
Embedding and multi-scale learning
In this section, we introduce methodologies for embedding and learning from data at
various scales. These approaches primarily focus on richly extracting information to capture
long-term dependencies and context.
TimeMachine (Ahamed and Cheng 2024) aims to capture long-term dependencies and
context at different scales through two-stage embeddings. It is divided into internal and
external embeddings based on embedding dimensions, and each section consists of two
parallel Mamba modules that explore temporal dependencies and channel dependencies,
respectively. The internal Mamba module operates at a low resolution to capture both global
and local contexts, while the external Mamba module operates at a high resolution to cap-
ture the global context.
Channel correlation learning
Next, we examine models that focus explicitly on learning the inter-channel correlations
in time series data. These models are centered around techniques that effectively integrate
information from each channel and model their interdependencies.
S-Mamba (Wang et al 2024d) features bi-directional Mamba blocks to consider both
past and future information, enabling the learning of inter-channel correlations. The role of
learning temporal dependencies is assigned to the Feed Forward Network (FFN). By clearly
separating the roles of Mamba blocks and FFN, computational efficiency is improved,
ensuring the stability of the Mamba architecture in large networks. In SiMBA (Patro and
1 3

| 216  Page 58 of 95 |     |     |     | J. Kim et al. |
| ------------------ | --- | --- | --- | ------------- |
Table 10 Taxonomy and methodologies of mamba models for time series forecasting
| Main             | Model name  | Main methodology        | Channel  Base | Publi- |
| ---------------- | ----------- | ----------------------- | ------------- | ------ |
| improvement      |             |                         | correlation   | cation |
| Embedding        | TimeMachine | ⋅ Integrated quadruple  | CD Mamba      | 2024   |
| and multi-scale  |             | Mambas                  |               |        |
learning
Channel correla- S-Mamba ⋅ Channel mixing: Mamba  CD Mamba MLP 2024
| tion learning |     | VC Encoding layer |     |     |
| ------------- | --- | ----------------- | --- | --- |
⋅ Sequence modeling: FFN
TD encoding layer
|     | SiMBA | ⋅ Channel mixing: Einstein  | CD Mamba | 2024 |
| --- | ----- | --------------------------- | -------- | ---- |
FFT (EinFFT)
⋅ Sequence modeling:
Mamba
|     | MambaTS | ⋅ Temporal Mamba Block  | CD Mamba | 2024 |
| --- | ------- | ----------------------- | -------- | ---- |
(TMB)
⋅ Variable permutation
training (VPT)
|     | C-Mamba |     | CD Mamba | 2024 |
| --- | ------- | --- | -------- | ---- |
⋅ Channel mixup
⋅ C-Mamba block
(PatchMamba + channel
attention)
Sequence  Mambaformer ⋅ Mambaformer (Attention  CI Mamba  2024
| information and  |     | + Mamba) layer | Transformer |     |
| ---------------- | --- | -------------- | ----------- | --- |
dependency
|          | Bi-Mamba+ | ⋅ Series-relation-aware  | CI/CD Mamba | 2024 |
| -------- | --------- | ------------------------ | ----------- | ---- |
| learning |           | (SRA) Decider            |             |      |
⋅ Mamba+ Block
⋅ Bidirectional Mamba+
Encoder
|     | DTMamba | ⋅ Dual Twin Mamba  | CI Mamba | 2024 |
| --- | ------- | ------------------ | -------- | ---- |
Blocks
| Theoretical  | Time-SSM |     | CD Mamba | 2024 |
| ------------ | -------- | --- | -------- | ---- |
⋅ Dynamic spectral opera-
| frameworks and  |     | tor with Hippo-LegP |     |     |
| --------------- | --- | ------------------- | --- | --- |
efficient modeling
|     | Chimera | ⋅ 2-Dimensional state  | CD Mamba | 2024 |
| --- | ------- | ---------------------- | -------- | ---- |
space model
Agneeswaran 2024b), channel modeling is achieved through Einstein FFT (EinFFT), while
sequence modeling is handled by Mamba modules. After applying the Fast Fourier Trans-
form (FFT), the real and imaginary parts are separated, and their respective weights are
learned. Channel mixing is performed through Einstein Matrix Multiplication (EMM), cre-
ating new data that reflects the relational information between channels, thus internaliz-
ing channel relationships. Additionally, to ensure system stability, eigenvalues of the state
matrix are adjusted to be negative through Fourier transformation and nonlinear layers.
MambaTS (Cai et al 2024c) reconstructs sequences by integrating past information of all
variables to learn channel correlations. Since variable information is integrated in advance,
unnecessary convolution in Mamba blocks is removed to enhance computational efficiency,
and dropout is applied to Temporal Mamba Blocks (TMB) to reduce overfitting. Addition-
ally, Variable Permutation Training (VPT) is introduced to dynamically determine the opti-
mal order of integrated variable information, enabling predictions based on the optimal
sequence of variables. C-Mamba (Zeng et al 2024) generates new virtual sample data by
linearly combining different channels (channel mixup), which is expected to enhance gen-
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 59 of 95 216
eralization performance. It uses a main block that combines patched Mamba modules with
attention modules for learning channel relationships.
Sequence information and dependency learning
This category emphasizes methods for learning the sequential information and depen-
dencies in time series data. It proposes various techniques for modeling both long-term and
short-term dependencies within the series.
Mambaformer (Xu et al 2024a) is a hybrid model that combines Mamba with a Trans-
former decoder framework. Since the Mamba block naturally internalizes the sequence order
information, positional embedding is unnecessary. Long-term dependencies are learned
through the Mamba block, while short-term dependencies are captured through the self-
attention layer, effectively capturing the overall dependencies. This approach overcomes
the computational efficiency limitations of attention mechanisms. Bi-Mamba+ (Liang et al
2024a) integrates patching techniques to finely learn inter-dependencies in the data. To pre-
serve long-term information, it introduces Mamba+ blocks, which add a forget gate to the
Mamba block. It also employs a Bi-Mamba+ encoder to process input sequences bidirection-
ally. Using the Spearman correlation coefficient, the Series-Relation-Aware (SRA) decider
is designed to automatically select channel tokenization strategies (CI or CD). DTMamba
(Wu et al 2024b) is composed of Dual Twin Mamba blocks, effectively learning long-term
dependencies in time series data channel independently. Each Twin Mamba block consists
of two parallel Mamba structures that process the same input data to capture different pat-
terns effectively. One Mamba structure learns detailed patterns and short-term variations,
while the other learns overall patterns and long-term trends.
Theoretical frameworks and efficient modeling
Lastly, we explore models that introduce new theoretical frameworks or propose efficient
modeling techniques. These models focus on effectively capturing the dynamic characteris-
tics of time series data and employ theoretical approaches and methodologies that enhance
computational efficiency.
Time-SSM (Hu et al 2024a) proposes a theoretical framework called the Dynamic Spec-
tral Operator, which extends the Generalized Orthogonal Basis Projection (GOBP) theory
for efficient use of SSM. The Dynamic Spectral Operator explores the changing spectral
space over time to effectively capture the dynamic characteristics of time series data. To
implement this, a novel variant of the SSM basis called Hippo-LegP is proposed, enabling
more precise modeling of time series data and achieving optimal performance through
S4D-real initialization. This allows it to demonstrate excellent performance with only about
one-seventh of the parameters required by Mamba models. Chimera (Behrouz et al 2024)
features the use of 2D SSM to capture dependencies independently along the time and vari-
able axes. By updating states in parallel along both axes, it achieves efficient computation.
The emergence of a new deep learning architecture, Mamba, is causing a shift in the long-
standing hegemony of deep learning architectures. In current TSF tasks, which increasingly
deal with long-term sequences, Mamba’s strengths-efficient sequence processing, selective
information retention, simplified architecture, and hardware optimization-prove to be highly
valuable. These features allow Mamba-based models to overcome the limitations of Trans-
formers, showing rapid performance improvements in a short period and suggesting a new
direction for deep learning modeling. The growth trajectory of Mamba raises attention to
whether it will become the new dominance in this field.
1 3

216 Page 60 of 95 J. Kim et al.
5 TSF latest open challenges and handling methods
5.1 Channel dependency comprehension
Spread of channel independent strategy
Multi-variate time series (MTS) forecasting primarily hinges on how well it can learn the
short-term and long-term temporal dependencies. However, many recent real-world data-
sets predominantly deal with multivariate data, where the relationships between variables
carry significant semantic information. As the relationships between variables become more
complex, models can provide more information and thus improve predictive performance
by leveraging this complexity.
Traditionally, it has been vaguely assumed that understanding the relationships between
variables in time series forecasting problems would make better performance. Despite being
obtained from different instruments, the data observe the same phenomenon, which intui-
tively suggests that they offer rich interpretations from various perspectives. However, with
the PatchTST (Nie et al 2023) model adopting a channel-independent (CI) strategy and
achieving state-of-the-art (SOTA) performance, research has begun to question the previ-
ously assumed channel-dependent (CD) strategy. These studies have shown that high per-
formance can be attained without learning the interactions between variables.
The CI strategy simplifies the model by excluding inter-variable modeling, allowing it to
focus solely on learning the temporal dependencies of each channel. This approach reduces
model complexity and enables faster inference, while also mitigating the risk of overfitting
due to noise from inter-variable interactions. Additionally, since the addition of new chan-
nels does not affect the model, it can adapt flexibly to changes in data. These advantages
have led many studies to adopt the CI strategy, resulting in improved performance. How-
ever, the CI strategy did not consistently show superior performance across all studies. The
CD strategy still demonstrated high performance in many studies, such as iTransformer (Liu
et al 2024c). Additionally, both strategies showed inconsistent performance depending on
the datasets used. Consequently, without clear justification, both CI and CD strategies were
employed according to the researchers’ preferences for a period of time.
Importance of learning channel correlations
Learning the correlations between variables remains important. In multivariate time
series data, each variable does not change independently but is interdependently related
to others. Even if these relationships sometimes introduce noise or fail to provide critical
information, the relationships themselves are not devoid of meaning. The information from
multivariate variables often intertwines to create complex patterns that cannot be captured
by a single variable. Understanding the correlations between multiple variables helps inter-
pret these complex patterns.
Modeling the correlations between variables is also crucial for improving prediction
accuracy. Especially when dealing with long sequence patterns, it is essential to understand
the numerous local patterns within them. During this process, important causal relationships
are often derived from other variables or exogenous factors. In the case of noisy data, learn-
ing the correlations between variables can help extract key information effectively. By com-
prehensively observing the information from multiple variables, it is possible to emphasize
important features and complement missing information.
What makes CI look better?
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 61 of 95 216
If the CD strategy is important and has the potential for significant performance improve-
ments, why do many studies show that the CI strategy performs better? To answer this ques-
tion, some research has been conducted, and the following summary can be provided based
on the “The capacity and robustness trade-off: Revisiting the channel independent strategy
for multivariate time series forecasting” (Lu Han 2024) paper.
According to the study, an examination of the Auto-correlation Function (ACF) values
between the training set and test set of the benchmark data, which have been used in various
experiments, revealed a distribution shift. The ACF can identify the correlation between
data values at specific time lags in time series data.
A distribution shift refers to the difference in statistical properties between the training
data and test data extracted from the same dataset. Distribution shifts can occur for various
reasons, often due to anomalies in the training series or variations in the trend, but some-
times the exact cause cannot be clearly defined. An important finding from the study is that
the CI strategy demonstrates relatively greater robustness to distribution shifts. Since the CI
strategy relies on the average ACF of all channels, it is less sensitive to distribution shifts
compared to the CD strategy, which depends on the ACF variations of individual channels.
Additionally, by excluding inter-variable relationships, the CI strategy simplifies the model,
reducing the likelihood of overfitting and enhancing robustness. Therefore, the CI strategy
has been able to demonstrate good performance on benchmark datasets where distribution
shifts are present.
However, this does not imply that the CI strategy is superior to the CD strategy. It merely
suggests that, in some datasets, the positive effects resulting from the robustness of the CI
strategy outweigh the advantages of learning inter-variable relationships. Conversely, if dis-
tribution shifts can be effectively alleviated, the CD strategy can provide much more useful
information than the CI strategy. To this end, even the application of simple regularization
methods, such as Predict Residual with Regularization (PRReg), adapting low-rank layers,
and using the MAE loss function, can reverse the performance gap. Furthermore, various
distribution shift alleviation methodologies have been researched, and these can be applied
in a model-agnostic manner. The details of these methodologies will be discussed in the next
section, and the previous content has been illustrated in Fig. 15
Recent approaches
As the effectiveness of learning channel correlation has been validated, recent multivari-
ate time series forecasting problems have predominantly adopted the CD strategy. In con-
trast, the CI strategy is increasingly applied in a limited way, primarily in univariate models
focused on temporal dependency.
Approaches to addressing recent MTS problems can be broadly categorized into three
types. The first approach involves explicitly integrating modules for channel mixing into
the backbone model. Most models adopt this strategy, aiming to maximize effectiveness
by explicitly incorporating channel correlation. However, as discussed earlier, distribution
shifts in the dataset can potentially degrade the performance of the CD strategy, necessitat-
ing the introduction of appropriate alleviation methods. By employing this combination, the
strengths of learning channel correlations can be applied more reliably, leading to enhanced
model performance. The distribution shift alleviation methods will be discussed in detail in
Sect. 5.2.
The second approach implicitly incorporates channel correlations into the input. Instead
of explicitly integrating channel learning modules into the backbone model, this method
1 3

216 Page 62 of 95 J. Kim et al.
Fig. 15 Comparison of CI and CD strategies in channel correlations
takes a preprocessing approach by mixing channel information in advance to create a new
input, which is then fed into the prediction model. This new input combines the mixed
channel information with the original individual channel data before being processed by the
prediction model. By inherently reflecting the relationships between channels, this method
allows even a simple CI backbone to achieve the effectiveness of a more complex CD
model. Models like SOFTS (Han et al 2024) and C-LoRA (Nie et al 2024) fall into this
category.
The third approach adaptively selects between the CI and CD strategies. The model is
designed to operate in both directions, allowing it to choose the most effective strategy based
on the characteristics of the dataset being used. In some cases, like TSMixer (Ekambaram
et al 2023), the user can manually select the appropriate strategy, while in others, such as Bi-
Mamba+ (Liang et al 2024a), the model automatically determines the optimal strategy. The
second and third approaches both utilize the CI strategy alongside the CD strategy, aiming
to integrate the advantages of both into the model. A summary of the criteria for selecting
these strategies is presented in Fig. 16
In the past, the criteria for selecting channel strategies were ambiguous, but recent
research has provided clear guidelines. Based on these advancements, users can now choose
the appropriate channel strategy according to the characteristics of their dataset, effectively
improving model performance through various approaches.
5.2 Alleviation of distribution shift
Many real-world time series data exhibit non-stationarity, where their distribution gradu-
ally changes. For instance, trends such as increasing electricity consumption and shifts in
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 63 of 95 216
Fig. 16 Recent approaches to channel strategies
consumer preferences can lead to changes in data distribution. This non-stationarity intro-
duces challenges for the generalization of time series forecasting (TSF) models by creating
distribution discrepancies within the training data and between the training and test data. To
mitigate the issue of distribution shift caused by non-stationarity in time series forecasting,
various research efforts have been proposed.
Representative approaches for addressing distribution shifts include Domain Adapta-
tion, Transfer Learning, and Robustness Techniques. Domain Adaptation aims to reduce the
distribution differences between the source and target domains to improve generalization
performance across domains. This approach is divided into supervised domain adaptation,
which uses some labeled data from the target domain, and unsupervised domain adaptation
which aligns feature distributions using unlabeled datasets. Unsupervised domain adap-
tation began with the introduction of Maximum Mean Discrepancy (MMD) (Wang et al
2023a) -based methods and advanced with the emergence of Generative Adversarial Net-
works (GANs) (Sankaranarayanan et al 2018), which led to the development of adversarial
domain adaptation techniques. Transfer Learning (Pan and Yang 2009) refers to applying a
model trained in one domain or task to a new dataset. This includes Feature Transfer, which
reuses or retrains specific layers of a pre-trained network for a new task, and Fine-Tuning
which adjusts the entire pre-trained model to fit the new dataset. Transfer learning originated
from pre-trained embeddings in NLP in the late 1990s, expanded through CNNs, and even-
tually evolved with LLMs. Robustness Techniques enhance a model’s ability to maintain
performance despite data uncertainties, such as noise, outliers, and data scarcity. Methods
such as Dropout (Srivastava et al 2014) and Data Augmentation (Wong et al 2016) help
models handle noise, while robust loss functions like the Huber loss (Huber 1992) reduce
sensitivity to outliers. These techniques have been widely adopted in time series forecasting
models since 2020.
This survey focuses on one prominent approach that introduces normalization and denor-
malization modules within a normalization-TSF model-denormalization framework. This
1 3

216 Page 64 of 95 J. Kim et al.
framework has evolved as a specialized approach for mitigating non-stationarity within the
same domain of time series data. Here, normalization is applied to the look-back window
before feeding it into the TSF model, aiming to remove input statistics. As a result, the
TSF model processes inputs from a less time-variant distribution. Denormalization is then
applied to the forecasting window obtained from the TSF model to restore the original
statistics. The denormalized forecasting window is ultimately used as the final forecast.
However, calculating the appropriate statistics for normalization and denormalization in
non-stationary scenarios is a non-trivial task, and numerous studies have been proposed
within this framework to address this challenge (Table 11).
DAIN (Passalis et al 2019) introduces a Deep Adaptive Input Normalization layer that
learns how much to shift and scale each observation end-to-end. Considering the chang-
ing distribution characteristics of time series data, this approach outperforms widely used
normalization methods like batch normalization (Ioffe and Szegedy 2015) and instance nor-
malization (Ulyanov et al 2016) across various domains, highlighting the importance of
normalization techniques in TSF. However, DAIN omits a denormalization step, meaning
it does not account for restoring statistics in the forecasting results. In contrast, RevIN (Kim
et al 2021), which extends instance normalization to be reversible, adopts a normalization-
denormalization framework. RevIN performs instance normalization on each look-back
window, followed by variable-wise multiplication of a learnable scale factor and addition of
a bias factor. During de-normalization, the same parameters are applied in reverse. NST (Liu
et al 2022) normalizes the look-back window in a non-parametric manner without a learn-
able affine transformation and then de-normalizes the prediction window using the mean
and standard deviation of the look-back window. Dish-TS (Fan et al 2023) learns a mod-
ule that predicts the statistics of the prediction window, considering the distribution shift
between the look-back window and subsequent prediction windows, and performs normal-
ization and de-normalization accordingly. SAN (Liu et al 2024e) considers the distribution
Table 11 Normalization-denor- Model name Main improvement and methodology Publi-
malization-based approaches to cation
alleviate distribution shifts in
time series forecasting DAIN ⋅ Introduce adaptive normalization 2019
⋅ Adaptive scaling, shift, and gating layers
to normalize look-back window
RevIN ⋅ Introduce normalization-denormalization 2022
framework
⋅ Denormalize prediction with reversible
affine transformation parameters
NST ⋅ Non-parametric 2022
normalization-denormalization
⋅ Normalize and denormalize using mean
and std of look-back window without
learnable parameters
Dish-TS ⋅ Divides distribution shifts: (1) within 2023
look-back window and (2) between look-
back window and forecasting window
⋅ Introduce Dual-CONET modules for
statistics prediction
SAN ⋅ Predict statistics in slice-level 2023
⋅ Slice forecasting windows and predict
mean and std for each slice
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 65 of 95 216
shift within both the look-back window and prediction windows, performing statistical pre-
diction on smaller slices.
5.3 Enhancing causality
Why causal analysis is essential for accurate time series forecasting
Causal analysis is crucial in achieving accurate time series forecasting by better under-
standing the underlying factors driving data patterns. Time series data often exhibit correla-
tions that can be misleading without a proper understanding of causality. For instance, two
variables may show a strong correlation simply due to coincidence or because they are both
influenced by a third, unobserved variable. Without distinguishing between correlation and
causation, forecasting models risk attributing changes in the data to irrelevant or spurious
factors, leading to inaccurate predictions. Causal analysis helps overcome this by identify-
ing the true cause-and-effect relationships, ensuring the model is grounded in reality rather
than coincidental patterns.
Moreover, causal analysis enhances the interpretability and practical application of fore-
casting models. By explaining how different variables influence the outcome, causal models
uncover the underlying mechanisms driving the forecast, which is crucial for decision-mak-
ing. Businesses and policymakers can use these insights to predict the impact of specific
actions, such as policy changes or marketing strategies, and make informed decisions based
on the likely effects. This ability to simulate interventions and conduct counterfactual sce-
narios makes causal analysis an indispensable tool for accurate and actionable time series
forecasting.
Research on TSF with causality
As mentioned earlier, utilizing causality in time series forecasting not only improves
prediction accuracy but also enhances model interpretability. For these reasons, research
applying causal discovery information to time series forecasting models is actively ongo-
ing. In particular, various methodologies have been proposed in fields such as healthcare,
environmental science, and social sciences, where causal discovery is actively researched.
In TSF, various causal inference methods are employed to identify cause-and-effect rela-
tionships within the data. The Granger Causality Test (Granger 1969) examines whether
the historical information of one variable helps predict the future of another variable. This
method detects the direction of causal influence based on regression analysis. However, it
has limitations in fully excluding indirect correlations caused by the presence of a third vari-
able. Structural Causal Models (SCM) (Pearl et al 2000) utilize causal graphs and structural
equations to model the relationships between variables. These models enable intervention
simulations and counterfactual analyses, providing a visual representation of causal relation-
ships to aid interpretation and integrate interactions across multiple variables. Do-Calculus
(Pearl 1995) is an intervention analysis technique for quantitatively analyzing the effects
of interventions by computing the impact that changes in specific variables have on others,
thereby supporting causal predictions. Propensity Score Matching (PSM) (Rosenbaum and
Rubin 1983) is a method for performing causal inference by matching groups with similar
characteristics. This approach minimizes the influence of confounders and more accurately
evaluates the effects of interventions. Directed Acyclic Graphs (DAGs) (Pearl 1998) are
directional, non-cyclic graphs that visually represent the relationships between causes and
effects. DAGs help clearly identify causal structures and understand complex interactions
1 3

216 Page 66 of 95 J. Kim et al.
among variables. Various attempts are being made to enhance the causality of TSF by utiliz-
ing these diverse causal inference methods (Runge et al 2019; Schölkopf et al 2021).
Qian et al (2023) introduce a model to predict Kuroshio Volume Transport (KVT).
It employs multivariate causal analysis to discover causal relationships and selects only
the variables with causal relationships to make predictions using an LSTM model. This
approach captures meaningful information from causally related variables and prevents the
model from being confused by unrelated variables. Mu et al (2023) propose a model for
predicting the North Atlantic Oscillation. It uses information obtained through causal dis-
covery not only for variable selection but also by directly applying it to a GCN (Graph Con-
volutional Network). The overall structure utilizes a symmetrical encoder and decoder of
ConvLSTM, with the GCN acting as a coupler in between. Sharma et al (2022) focuses on a
model for energy consumption. It applies the Granger causality test to determine the causal
relationship between weather conditions and energy consumption and then integrates this
causal information into a Bi-LSTM to improve energy consumption prediction accuracy.
CausalGNN (Wang et al 2022b) is a model aimed at epidemic forecasting. It extracts causal
features using the SIRD model and incorporates them into an Attention-Based Dynamic
GNN module to learn spatio-temporal patterns. Caformer (Zhang et al 2024b) criticizes
existing methods for failing to learn causal relationships effectively due to false correlations
caused by environmental factors. To address this, it explicitly models environmental influ-
ences and removes them to obtain reliable causal relationships.
5.4 Time series feature extraction
Time Series Feature Extraction is the process of extracting useful information from time
series data to enhance model performance. In other words, it involves identifying and quan-
tifying time series data into key patterns, trends, seasonality, outliers, periodicity, and sta-
tistical characteristics to transform it into a form that is suitable for model training. This
process clarifies the unique patterns or characteristics of time series data, allowing models to
learn them more effectively. This enhances the understanding of data, improves the predic-
tive performance of models, and increases efficiency through data compression. The reasons
why Time Series Feature Extraction is necessary are as follows:
● Understanding the characteristics of data Time series data, which is ordered sequen-
tially over time, possesses unique characteristics such as various patterns, seasonality,
and periodicity. However, these data are complex and high-dimensional, making these
features not easily apparent. The continuous values in time series data tend to be similar
to adjacent values, which makes it challenging to accurately distinguish the context and
meaning of each data point, often resulting in a lack of semantic information. Therefore,
the process of transforming time series data into an analyzable format and extracting
key features is crucial for understanding the inherent behaviors and interactions within
the data.
● Explainability of data Unlike traditional machine learning methods, deep learning mod-
els automatically learn useful features from data without requiring manual feature ex-
traction. However, due to the nonlinear structure of deep learning models, it is often
difficult for humans to interpret the learned features. The extracted features can better
explain the structural characteristics of the data, helping to interpret and understand its
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 67 of 95 216
meaning. This process provides critical insights for making data-driven decisions and
contributes to improving explainability in complex model architectures.
● Enhancing Model Performance By summarizing complex time series data and remov-
ing noise, it emphasizes the essential signals of the data, reducing the computational
burden on models and improving predictive performance. Focusing on critical infor-
mation allows the model to avoid overfitting to the training data and develop strong
generalization capabilities.
Decomposing or transforming time series data into different forms before feeding it into the
model is a widely used and researched approach for feature extraction. These approaches
help the model focus on learning the critical information in the data, thereby reducing sen-
sitivity to noise and overfitting. These methods are not limited to specific architectures
and can be applied across various models. Figure 17 presents the key techniques for time
series feature extraction, followed by an explanation of related application models for these
approaches.
Fig. 17 Key techniques in time series feature extraction
1 3

216 Page 68 of 95 J. Kim et al.
5.4.1 Decomposition
Time series decomposition has long been used as a fundamental time series feature extrac-
tion technique, which involves separating time series data into components such as trend,
seasonality, periodicity, and residual. The advantage of decomposition is that it simplifies
complex time series data by breaking it down into understandable, independent compo-
nents, enabling more accurate model predictions and easier analysis and interpretation.
Moving average kernel
Many models apply a Moving Average kernel to the input sequence to separate trend and
seasonality components. In this process, high-frequency noise or short-term fluctuations
are removed, allowing long-term trends to be more clearly captured and overall patterns of
increase and decrease to be emphasized. The method of using a Moving Average Kernel is
widely adopted due to its computational simplicity and efficiency. However, it has limita-
tions when dealing with complex nonlinear patterns.
Autoformer (Wu et al 2021) goes beyond using decomposition techniques merely as pre-
processing for forecasting tasks by progressively decomposing time series data throughout
the prediction process within the model itself. Similarly, CrossWaveNet (Huang et al 2024b)
employs a dual-channel network to perform gradual deep cross-decomposition, enabling
it to capture complex temporal patterns effectively. Likewise, models such as FEDformer
(Zhou et al 2022), LTSF-Linear (Zeng et al 2023), and PDMLP (Tang and Zhang 2024)
utilize a moving average kernel to individually model each component of the time series
data, which are then recombined to make effective predictions. However, the Moving Aver-
age method lacks robustness because it is not learnable by the model. Additionally, since it
assigns equal weights to each data point within the sliding window, it has limited ability to
identify specific patterns. To address these limitations, Leddam (Yu et al 2024) use learn-
able 1D convolutional kernels, which can better capture nonlinear structures and dynamic
variations. Meanwhile, diffusion-based models face challenges as components like trend
and seasonality can easily collapse during the diffusion process. Diffusion-TS (Yuan and
Qiao 2024) overcomes this by applying the diffusion process after decomposition, thereby
preserving the characteristics of each component more effectively. Through this approach,
the traditional limitations of time series decomposition are overcome, allowing for a more
effective separation of trend and seasonal components.
Downsampling
The technique of using downsampling for decomposition is also frequently employed.
Originating from signal processing, downsampling involves reducing the number of sam-
ples from the original signal, effectively decreasing the data by a specific ratio. Time series
forecasting is typically achieved through pooling methods, where representative values
are extracted from specific segments of the time series data, thereby suppressing high-fre-
quency components and emphasizing low-frequency components. By adjusting the pooling
size, various downsampling levels can be achieved, allowing for the exploration of multiple
patterns within the data.
SparseTSF (Lin et al 2024b) and SutraNets (Bergsma et al 2023) use downsampling to
separate data into trend and periodic components, predicting each subseries independently.
This allows the model to learn each component separately and better understand the influ-
ence of each on the complex time series data, enhancing prediction accuracy. By dividing the
complex time series data into various sub-series, it can be decomposed into a simpler form,
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 69 of 95 216
thereby reducing the overall complexity of the model. Therefore, this approach enhances the
model’s generalization ability and helps prevent overfitting.
Non-linear methods
While Moving Average Kernel and Downsampling are linear methods, Empirical Mode
Decomposition (EMD) (Huang et al 1998) is a non-linear and non-stationary signal analy-
sis technique that decomposes time series data into a number of Intrinsic Mode Functions
(IMFs). EMD involves finding local extrema in the signal and using linear interpolation for
the upper and lower envelopes, and by subtracting their average, it extracts high-frequency
components as IMFs iteratively. The final residual signal, also known as the residue, reveals
the long-term trend. EMD is advantageous for processing non-linear and non-stationary
time series data due to its adaptive nature, effectively separating and analyzing complex pat-
terns and changes in the time series. EMD-BI-LSTM (Mounir et al 2023) proposes a method
that combines EMD with a conventional Bi-LSTM model for forecasting electric load time
series data. By applying EMD, the model effectively captures complex non-linear relation-
ships, thereby enhancing forecasting performance.
However, EMD has a mode mixing problem, where signals of different frequencies are
mixed within the same IMF (Xu et al 2019). In the signal decomposition process of EMD,
IMF is generated based on local extrema, which causes difficulties in independently sepa-
rating components for signals with sudden changes, such as intermittent signals. This leads
to a failure in frequency separation, which not only reduces prediction performance but
also impairs interpretability. Ensemble Empirical Mode Decomposition (EEMD) (Wu and
Huang 2009) addresses this mode mixing problem by adding noise to the original signal and
repeating the decomposition process, averaging the results. Through this process, signals
with different scales are properly aligned into the correct IMFs. Through successive itera-
tions, the influence of the noise is reduced, and the components of the original signal are
emphasized, providing more physically meaningful results and enabling more accurate and
stable time series decomposition. Yang and Yang (2020) proposes models applying EEMD
to LSTM, linear regression, and Bayesian ridge regression for forecasting.
Variational Mode Decomposition (VMD) (Dragomiretskiy and Zosso 2013) is a method
that uses variational optimization to separate signals into modes with specific frequency
bands. Each mode’s frequency center and bandwidth are determined through variational
optimization. As the frequency ranges do not overlap, the separation is clearer and more
stable. However, compared to EMD, which requires relatively simple calculations, VMD is
computationally more complex due to its use of variational optimization. Peng et al (2023)
proposes a new model for crude oil price forecasting that applies VMD. By decomposing
the time series data with VMD, transforming it into images, and extracting features with
CNN, this method improves forecasting performance for oil prices. It effectively utilizes
the advantages of VMD by making predictions with Bidirectional Gated Recurrent Unit
(BGRU).
Various decomposition methods are widely used in time series forecasting. However,
decomposition methods also have some drawbacks. When the data is divided into separate
components based on different rules, the model predicts each component independently. As
a result, important interactions or relationships may not be considered, which can lead to
underutilization of necessary information for prediction and degrade performance. Never-
theless, considering the characteristics of time series, such as periodicity, trends, and noise,
decomposition remains a powerful technique. Moreover, since time series data is more dif-
1 3

216 Page 70 of 95 J. Kim et al.
ficult to intuitively interpret compared to other data types, decomposition provides interpret-
ability, which helps increase the model’s trustworthiness.
5.4.2 Multi-scale
The multi-scale approach analyzes data at various time scales, capturing patterns and trends
at multiple levels simultaneously. This method is beneficial not only for time series data but
also in fields like computer vision and natural language processing (Fan et al 2021; Nawrot
et al 2021). By integrating information from longer time frames, the multi-scale approach
plays a significant role in improving performance in time series forecasting.
MTST (Zhang et al 2024e), PDMLP (Tang and Zhang 2024), and FTMixer (Li et al
2024d) extend the patching application to a multi-scale framework, where shorter patches
effectively learn high-frequency patterns and longer patches capture long-term trends. Time-
Mixer (Wang et al 2024a) and AMD (Hu et al 2024b) leverage multi-scale decomposition
to capitalize on the strengths of each scale, enabling the model to make more accurate pre-
dictions. HD-TTS (Marisca et al 2024) uses spatiotemporal downsampling to decompose
data into various scales across both time and space. Scaleformer (Shabani et al 2023) and
Pathformer (Chen et al 2024b) apply the multi-scale concept to the overall model architec-
ture, while HD-TTS hierarchically implements temporal and spatial downsampling. MG-
TSD (Fan et al 2024b) and mr-Diff (Shen et al 2024) successfully integrate multi-scale by
incorporating inductive biases that prioritize generating coarse data in the early stages of the
diffusion reverse process.
5.4.3 Domain transformation
A common method for enhancing the expression of latent periodic features in time series
data is to transform the data into the frequency domain. Techniques such as Fourier trans-
formation, Wavelet transformation, and Cosine transformation are commonly used for this
purpose. Generally, time series data exhibits periodicity, which refers to patterns that repeat
at regular intervals. Frequency transformations effectively explore this periodicity. In time
series analysis, frequency transformations are used with two main approaches: extracting
periodic components and direct learning in the frequency domain.
Periodicity extraction
Periodicity in time series data serves as critical information for predictive models, where
features that may be hidden in the time domain can be more easily uncovered in the fre-
quency domain. Frequency transformations are advantageous because they can remove high-
frequency noise while retaining important low-frequency components, thereby improving
data quality. By selectively extracting key frequency components and feeding them into the
model, the process helps in learning essential patterns, enhances computational efficiency,
and reduces model complexity. Some models leverage these characteristics to identify and
extract various periodic patterns in the data. These adaptively extracted patterns are used
either as inputs for the model or integrated into the learning process, thereby enhancing the
model’s predictive performance.
Autoformer (Wu et al 2021) utilizes periodicity extracted through auto-correlation within
the Attention mechanism. TimesNet (Wu et al 2023) transforms periodic components into a
2D format to train the time series with CNNs. MSGNet (Cai et al 2024a) uses periodic com-
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 71 of 95 216
ponents to allow the model to determine appropriate scale levels for multi-scale analysis
autonomously. However, since the periodicity extracted in this manner is based on selective
sampling, it does not encompass all the latent information, and if critical information is not
selected, performance degradation becomes inevitable.
Training in the frequency domain
The approach of directly training models in the frequency domain is widely studied as
it overcomes these limitations by evenly learning all latent frequency components, ensur-
ing that critical information is not missed. While time series data can exhibit complex and
varied patterns in the time domain, these patterns can often be succinctly represented by a
few dominant frequency components when transformed into the frequency domain (Zhou
et al 2022). This simplification makes the learning process more straightforward, as most of
the information can be captured with a minimal set of frequency components. This method
allows for an easy transition to the frequency domain while preserving the original informa-
tion, thanks to various transformation and inverse transformation techniques. When time
series data exhibit nonlinear characteristics, learning in the frequency domain can better
capture these complex patterns than in the time domain. The frequency domain approach
doesn’t require consideration of time-axis variations, enabling stable performance even with
non-stationary data. Furthermore, this method allows for efficient learning by compressing
the data without losing important characteristics.
In the frequency domain, each frequency component is represented as a complex num-
ber, consisting of a real part and an imaginary part, each conveying different information.
The real part is related to the magnitude (amplitude) of the time series data, indicating how
prominent the periodic components are. The imaginary part, on the other hand, relates to
the phase information of the data, determining the temporal positioning of the frequency
components. By simultaneously understanding the amplitude and phase information in the
frequency domain, models can accurately capture and predict complex periodic patterns in
the data. The research initially focused on simply changing the domain, but more recently, it
has been moving towards expanding the expressiveness of the frequency domain.
FreTS (Yi et al 2024) and Crabbé et al (2024) transform data into the frequency domain
before feeding it into the model and then convert the predicted values back into the time
domain. Simply converting data to the frequency domain has limitations in achieving good
model performance, leading to the development of models that overcome these challenges.
Research continues to expand the representation in the frequency domain to fully utilize
its rich features. FEDformer (Zhou et al 2022) applies season-trend decomposition and
then performs attention in the frequency domain, facilitating independent modeling of key
information components. Fredformer (Piao et al 2024) not only transforms data into the fre-
quency domain but also investigates frequency bias through experiments, addressing issues
in the frequency domain using frequency normalization techniques. FITS (Xu et al 2024c)
utilizes distinct complex-valued linear layers in the frequency domain to learn amplitude
scaling and phase changes, thereby enhancing the frequency representation of input time
series through interpolation learning. DERITS (Fan et al 2024a) effectively handles the non-
stationarity of time series data by differentiating frequency components and representing
them in a static form that is easier to predict. SiMBA (Patro and Agneeswaran 2024b) trans-
forms time series data into the frequency domain using Fourier transforms, learning real
and imaginary components separately, thus allowing more precise analysis of data in the
frequency domain and improving model prediction performance. While frequency bands
1 3

216 Page 72 of 95 J. Kim et al.
capture global dependencies well, they often struggle with local dependency capture. To
overcome this, WaveForM (Yang et al 2023a) uses discrete wavelet transforms (DWT) to
decompose time series data into various frequency bands while preserving the time informa-
tion of each band. This approach captures frequency changes within specific time intervals,
simultaneously capturing features from both time and frequency domains. FTMixer (Li et al
2024d) proposes a method that directly utilizes data from both domains to leverage the
strengths of global dependency extraction in the frequency domain and local dependency
extraction in the time domain.
5.4.4 Additional approach
In addition to the methods previously described, various other approaches have been
explored. A notable example is the use of High-Dimensional Embedding, which generates
high-dimensional representations to better capture the essential information of the data. This
approach extracts complex, multidimensional information from the original time series data
and integrates it to enhance the model’s predictive capabilities. For instance, CATS (Lu et al
2024) creates a new Auxiliary Time Series (ATS) by combining variables from the input
data and then utilizes these for prediction. SOFTS (Han et al 2024) focuses on extracting
common features (Core) from the variables and incorporating them into the learning pro-
cess. Furthermore, BSA (Kang et al 2024) enhances feature representation by leveraging
temporal correlations between continuously streaming input samples, rather than depend-
ing solely on a single current input. The method accumulates multiple scales of feature
transformations over time via an exponential moving average (EMA), then applies Spectral
Attention to these multi-scale momentums to capture long-range dependencies and enrich
the resulting features.
Efforts to effectively represent the complex features of time series data for better model
learning are being explored in various forms. These efforts are essential research topics
for improving performance in the challenging field of time series forecasting. Addition-
ally, integrating these feature extraction techniques appropriately within the basic struc-
ture of existing deep learning models can create synergy, enhancing the model’s predictive
accuracy.
5.4.5 Automated feature engineering and self-supervised learning
In TSF, extracting meaningful features has traditionally required domain expertise and
extensive manual work. However, such approaches are often time-consuming and costly,
and they may miss critical patterns when dealing with complex data. To address these chal-
lenges, automated feature engineering has become increasingly important for automatically
identifying key patterns in the data. One of the core techniques for automated feature engi-
neering is self-supervised learning (Zhang et al 2024a).
Self-supervised learning is a pretraining approach that enables models to automatically
learn important features from unlabeled datasets by identifying patterns directly from the
data itself. This allows the model to capture structural patterns without relying on manual
feature extraction, reducing the dependency on labeled data. Key approaches in self-super-
vised learning for TSF are as follows. Transformation-based approach learns key features
by comparing patterns before and after data transformations, such as time shifts and scaling.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 73 of 95 216
For example, TS-TCC (Eldele et al 2021) enhances features by applying various transforma-
tions and learning the pattern similarities between the transformed data. Time Correlation
Learning extracts temporal dependencies in time series data by learning the relationships
between past and future time points. Contrastive Predictive Coding (CPC) (Oord et al 2018)
divides the data into multiple time segments and learns the correlations between these seg-
ments. Mask-based Learning involves masking specific time points in the time series data
and predicting these masked points based on the remaining data to learn key patterns (Wang
et al 2022a). The application of such self-supervised learning approaches can enhance the
performance of TSF (Xu et al 2022; Wu et al 2023).
Self-supervised learning enables models to automatically recognize and extract key pat-
terns and nonlinear relationships from data without labeled examples. It can effectively
learn from small datasets, addressing the issue of label scarcity and contributing to model
lightweight and algorithm optimization. In particular, multimodal self-supervised learn-
ing techniques, which integrate time series data with other data types such as images and
text, are expected to advance, enabling the model to learn richer patterns. Such multimodal
learning can significantly contribute to solving complex decision-making problems, such
as healthcare diagnostics and disaster prediction. Additionally, research on converting the
learned features into interpretable forms will become increasingly important. This will
enhance the interpretability and reliability of the model and improve trust in data-driven
decision-making processes.
In conclusion, self-supervised learning-based automated feature engineering is a piv-
otal research area for effectively understanding complex patterns in time series data and
enhancing predictive performance. Research combining this approach with data efficiency
improvements, multimodal learning, and explainable AI (XAI) is expected to further
increase the practicality and reliability of TSF.
5.5 Model combination techniques
The instability of single models in time series forecasting has been a persistent challenge
from the past to the present. Due to the complexity, volatility, and distinguishing charac-
teristics of time series data, the use of a single model can lead to overfitting and unstable
forecasting performance. Therefore, methods for combining models offer a simple yet effec-
tive approach to overcome these issues. Model combination techniques reduce forecasting
uncertainty and enable more robust predictions. Makridakis et al (2020) experimentally
demonstrates that model combination, as applied in the M4 Competition task, improves
forecast accuracy over single models or model selection. However, Model combination
techniques can face issues such as model redundancy, increased computational costs, and
reduced interpretability due to the complexity of the combined models. To maximize the
combination effect, it is necessary to properly leverage model diversity or use sophisticated
combination methods.
5.5.1 Ensemble models
Ensemble models combine the independent predictions of several models to complement
the weaknesses of individual models and generate a final forecast. Ganaie et al (2022) sum-
marizes the theoretical aspects of ensemble learning’s success based on existing research,
1 3

216 Page 74 of 95 J. Kim et al.
Fig. 18 BKey ensemble techniques
arguing that combining predictions from multiple models is an effective way to improve
model performance. This section explores key ensemble methods, including bagging, boost-
ing, and stacking, as illustrated in Fig. 18.
Bootstrap Aggregating (Bagging) involves randomly sampling the data to train several
independent models and then combining their results through averaging or voting (Breiman
1996). Petropoulos et al (2018) explains why bagging is effective for time series forecasting
by addressing data uncertainty, model uncertainty, and parameter uncertainty, improving
forecasting performance. Kim and Baek (2022) combines Wavelet transforms with bagging
techniques in MLP to improve univariate time series forecasting performance. Using the
Maximum Overlap Discrete Wavelet Transform (MODWT) (Nason et al 2000), the signal
is decomposed, and bagging is applied only to the detail part, excluding trends. This creates
data diversity by preserving the main trend while altering the detailed fluctuations.
Boosting overcomes the issue of model diversity by sequential training and combining
weak learners (Freund and Schapire 1997). This approach addresses the diversity problem
that can arise in bagging when each model is trained in a very similar manner. Each model
places more weight on the data that was incorrectly predicted by the previous models, aim-
ing to reduce bias. This creates a strong learner by combining weak learners and ensures
added diversity. Gradient boosting is an algorithm that optimizes models using the gradient
of the loss function within the boosting framework (Friedman 2001). XGBoost (eXtreme
Gradient Boosting) executes the gradient boosting algorithm in parallel, making it faster
and more effective in handling sparse data while improving learning speed and predictive
performance (Chen and Guestrin 2016). In the 2015 Kaggle (https://www.kaggle.com)
machine learning competition, 17 out of 29 winning solutions used XGBoost (Chen and
Guestrin 2016). As deep learning advanced, various works combining DL with XGBoost
emerged. LightGBM (Ke et al 2017) is a boosting-based algorithm with a leaf-wise tree
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 75 of 95 216
splitting method, and Sui et al (2024) uses an ensemble approach that combines traditional
and advanced methods for stock prediction. Specifically, the integration of LSTM, GRU,
LR, and LightGBM models enhances forecasting performance. However, boosting is gen-
erally not applied to deep learning models, as boosting typically uses simple weak learn-
ers that are repeatedly trained to improve performance. Deep learning models like MLP
already learn complex patterns effectively with large amounts of data, so the need for itera-
tive error correction is minimal. Thus, simpler machine learning methods are typically used
to construct weak learners instead of deep neural networks. Truchan et al (2024) proposes
predicting trends using linear models and then applying boosting to the residuals with tree-
based models for forecasting. This model combines the simple trend estimation capability
of linear models with the nonlinear pattern learning ability of tree-based models, achieving
more precise and effective predictions in LTSF. However, there is also a case where boosting
principles are applied to deep learning models, such as Liang et al (2024b), which integrates
boosting’s progressive residual learning approach into deep learning to enhance time series
forecasting.
Stacking combines the predictions of several models to generate a final forecast (Wolp-
ert 1992). Stacked Generalization involves training several base learners, and then feeding
their prediction results into a meta-model to generate the final prediction. Unlike bagging
and boosting, stacking does not directly combine the predictions of the models; instead, it
inputs the prediction results into a new model to make the final forecast. Stacking is dis-
tinctive in that it incorporates model weightings and analysis, enabling more refined and
comprehensive predictions (Sharma et al 2021). Massaoudi et al (2021) suggests stacking
LightGBM and eXtreme Gradient Boosting (XGB) to tackle stochastic variations in short-
term load forecasting, where the meta data generated by both models is input to an MLP for
the final prediction. Furthermore, the use of MLP as a meta-model instead of traditional ML
models like linear regression enables the learning of more complex, nonlinear relationships,
improving prediction performance. The results demonstrate the model’s generalization abil-
ity and superior performance across various datasets. BStacking can be applied not only to
deterministic forecasting but also to probabilistic forecasting, and some studies have shown
that stacking is effective in handling uncertainty (Pavlyshenko 2020; Dudek 2024). Hasson
et al (2023) explores the theoretical aspects of stacked generalization. Through cross-vali-
dation, it provides theoretical guarantees that the performance of a stacked generalization
model selected through cross-validation does not fall significantly behind that of an oracle
model, the best performing individual model. The paper also explains that extending the
basic models used in stacking to learnable models, rather than constant models, provides
better theoretical guarantees.
Ensemble models require significant training resources since each model must be trained
independently. Nevertheless, ensemble techniques combine diverse, high-performance
models to complement each other and can be implemented in a relatively simple manner.
Due to these characteristics, ensemble learning can enhance prediction stability and gener-
alization capabilities in application fields, penetrating nearly all industries, from grain prod-
uct distribution, semiconductor manufacturing, and sensor design to commercial software
development and testing services (Lin and Huang 2022).
1 3

216 Page 76 of 95 J. Kim et al.
5.5.2 Hybrid models
Hybrid models combine different types of models or techniques to leverage the strengths of
individual models while compensating for their weaknesses. These models employ a more
sophisticated structural integration approach compared to ensembles, encompassing various
strategies such as combining statistical models, machine learning models, and deep learning
models.
ESRNN (Smyl 2020), a hybrid model that combines statistical models with deep learn-
ing architectures, integrates exponential smoothing (ES) and LSTM to leverage the inter-
pretability of statistical methods alongside the powerful nonlinear learning capabilities of
deep learning. Through ES, the model effectively captures key components of individual
time series, such as level, trend, and seasonality, while LSTM learns the correlations and
nonlinear patterns across multiple time series. Additionally, the use of dynamic compu-
tation graphs and a hierarchical design provides strong performance and interpretability
in real-world applications. This model highlights the potential of hybrid models for time
series forecasting with its superior performance. BMoreover, AQ-ESRNN (Smyl et al 2024)
model, an extension beyond deterministic forecasting to probabilistic forecasting, enables
distributional forecasting by quantifying prediction uncertainty. Subsequently, hybrid
models combining deep learning architectures have advanced, and this section focuses on
explaining such combinations of deep learning architectures.
Particularly, time series data often involve not only temporal dependencies but also
important interactions between variables. Therefore, many models explicitly learn the inter-
dependencies between variables in addition to temporal dependencies. However, incorpo-
rating all this information into a single architecture can lead to overfitting, which may limit
the learning process. Recent models often combine two or more architectures to efficiently
learn by distinguishing the roles based on the nature of the information.
WaveForM (Yang et al 2023a) improves prediction performance by transforming time
series data into the wavelet domain and combining it with GNN. The Discrete Wavelet
Transformation (DWT) uses High-Pass and Low-Pass Filters to decompose the time series
data into small wavelets. This process removes noise and allows CNN to efficiently cap-
ture temporal and frequency characteristics. The GNN is then used to model the interac-
tions between these components. TSLANet (Eldele et al 2024) is a model that replaces the
computationally expensive attention mechanism with CNN in the Transformer framework.
It incorporates frequency analysis and a learnable threshold to selectively attenuate high-
frequency noise, effectively learning long-term and short-term interactions. Additionally, it
uses parallel convolution layers with different kernel sizes to capture both local patterns and
long-term dependencies. This approach effectively compensates for the typical CNN’s limi-
tations in modeling long-term dependencies. DERITS (Fan et al 2024a) enhances the predic-
tion performance of non-stationary time series data by combining convolution operations
in the frequency domain with MLP in the time domain. The Frequency Derivative Trans-
formation (FDT) converts time series signals into the frequency domain and then differenti-
ates the frequency components to represent them in a static form that is easier to predict.
The Order-adaptive Fourier Convolution Network (OFCN) is responsible for frequency
filtering and learning dependencies in the frequency domain. To improve prediction perfor-
mance, it processes and fuses derivative information of various orders in parallel, utilizing
a Parallel-stacked Architecture. BiTGraph (Chen et al 2024c) focuses on improving perfor-
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 77 of 95 216
mance in situations with missing data by capturing both temporal dependencies and spatial
structures. The Multi-Scale Instance Partial TCN module learns short-term and long-term
dependencies through kernels of various sizes and can also compensate for missing values
through partial TCN. The Biased GCN module for inter-channel relationship learning rep-
resents the relationships between data points as a graph structure and adjusts the strength
of information propagation between nodes, considering the missing patterns. Zhang et al
(2021a) proposes a hybrid model for wind speed forecasting. By performing decomposition
using Singular Spectrum Analysis (SSA) and Multivariate Empirical Mode Decomposition
(MEMD), the model removes noise and separates the trend and various frequency compo-
nents of the time series data, enabling more accurate forecasting. Then, by combining CNN
with attention mechanism and Bidirectional Long Short-Term Memory, the model extracts
spatial correlations and learns temporal dependencies, optimizing the wind speed forecast-
ing performance. Zhang et al (2021b) also uses both ensemble and hybrid models for TSF.
The ensemble deep learning model, which combines various deep learning models such as
CNN, MLP, and LSTM, demonstrates excellent performance in forecasting real-world time
series data, including PM2.5 concentration, wind speed, and electricity prices. The model
utilizes Extended AdaBoost (Freund and Schapire 1997) to generate diverse base predictors,
followed by applying a stacking method to use Kernel Ridge Regression as a meta-predictor
to produce the final forecast.
In hybrid models, optimization processes such as hyperparameter tuning, regulariza-
tion techniques, and cross-validation can help reduce the risk of overfitting caused by the
interdependence and complexity between multiple models. Additionally, evolutionary algo-
rithms can be used to explore and optimize model structures (Wei et al 2022). Hybrid mod-
els may increase training time and resource consumption, and they can have limitations in
interpretability and maintenance. Therefore, techniques like model compression or feature
selection can be applied, and model interpretability issues can be addressed using interpreta-
tion methods.
5.6 Interpretability and explainability
Although AI models exhibit outstanding performance, their black-box nature often under-
mines trust in decision-making processes (Xua and Yang 2024). In mission-critical domains,
particularly those dealing with human life and safety, understanding the reasons behind
model decisions is crucial, which has led to restrictions on the use of deep learning models
(Papapetrou and Lee 2024). The European Union, through the General Data Protection Reg-
ulation (GDPR), mandates the explanation of automated decisions, ensuring that individuals
can understand the rationale behind decisions made by automated systems like AI models
(Hamon et al 2022). As data-driven decision-making becomes more widespread, the need
to understand how a model arrives at specific predictions and why such outcomes occur is
growing (Lim and Zohren 2021).
Interpretability and explainability aim to ensure model understanding and transparency,
making it possible to know how and why a model produces certain results. These two con-
cepts can be applied in various ways. For example, consumers might demand explanations
when they notice anomalies in model outcomes, while AI researchers could use these con-
cepts to improve model performance. Ultimately, interpretability and explainability pro-
mote not only research on AI models but also their expansion into various fields, enhancing
1 3

216 Page 78 of 95 J. Kim et al.
performance and usability, which could drive fundamental changes in industries and soci-
etal paradigms (Han et al 2023a; Jung et al 2020; Kim et al 2020).
These concepts are particularly important in time series data, where interpretability helps
in understanding how a model recognizes and predicts periodic and repetitive patterns. Fur-
thermore, explainability is necessary for anomaly detection models to clarify how anoma-
lies are detected and which features are abnormal, thereby aiding decision-making.
The machine learning community has noted that there is no universally agreed-upon
definition for the terms interpretability and explainability (Lipton 2018). Consequently, in
various studies, these terms are often used interchangeably, even though they carry different
meanings and are used differently across domains (Graziani et al 2023). To avoid confu-
sion for our readers, we define and explain these terms as follows. Interpretability focuses
on understanding the internal workings of a model, providing transparency about how the
model makes predictions (ŞAHiN et al 2024). Interpretability requires an intuitive under-
standing of the model’s structure, feature selection, and prediction process. Explainability,
on the other hand, is concerned with providing reasons for a model’s outputs in a way that
humans can comprehend. It is a technical approach that helps make the decision-making
process of the model more understandable. In summary, interpretability is about understand-
ing how the model works, while explainability is about providing understandable reasons
for the model’s predictions.
5.6.1 Interpretability
Interpretability can be achieved through the following representative models. Temporal
Fusion Transformer (TFT) (Lim et al 2021) is a deep learning model for multi-horizon fore-
casting proposed by the Google Cloud AI team, which utilizes the attention mechanism to
effectively learn the interactions between static and time-dependent input data. This model
incorporates a static feature encoder, a variable selection gating mechanism, and interpre-
table weights, allowing the model to better capture the characteristics of time series data
and significantly improve interpretability compared to a standard Transformer. The gating
mechanism suppresses unnecessary inputs, enhancing model efficiency, while the static fea-
ture encoder converts static data into contextual vectors that are incorporated into predic-
tions. The following two models enhance the interpretability of the TFT model for wind
speed prediction by applying a two-stage decomposition approach. Given the high volatility
and multi-resolution modes of wind speed data, the decomposition technique described in
Sect. 5.4.1 allows for the independent analysis of the impact of each component on the
prediction results, thus improving interpretability. EMD-EEMD-JADE-TFT decomposes
the data using Empirical Mode Decomposition (EMD) and Ensemble Empirical Mode
Decomposition (EEMD) and optimizes the TFT’s hyperparameters using Adaptive Dif-
ferential Evolution with optional external archive (JADE) (Wu and Wang 2024). IEEMD-
EWT-JADE-TFT model, on the other hand, uses Improved Complete Ensemble Empirical
Mode Decomposition with Adaptive Noise (IEEMD) and Empirical Wavelet Transform
(EWT) for decomposition, and similarly optimizes TFT hyperparameters with JADE (Wu
et al 2024a). Additionally, meteorological feature engineering combines statistical features
to enhance both performance and interpretability.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 79 of 95 216
5.6.2 Explainability
Different methodologies exist for models focused on explainability. Simple machine learn-
ing models, such as Linear Regression or Decision Trees, are transparent and provide an
intuitive understanding of predictions by themselves. These models have intrinsic explain-
ability, which falls under ante-hoc explainability, meaning their predictions can be easily
explained from the design stage. On the other hand, deep learning models are highly com-
plex and learn high-dimensional features, making it difficult to achieve intrinsic explainabil-
ity through simple aggregation methods. Therefore, post-hoc explainability techniques are
primarily used for deep learning models. Post-hoc explainability refers to approaches that
interpret and explain the prediction or decision-making process after the model has already
been trained. Post-hoc interpretability can be divided into several subcategories.
Surrogate models are used to explain the predictions of complex models by training a
simpler, interpretable model to explain the predictions. Local Interpretable Model-Agnostic
Explanations (LIME) is a representative surrogate model that provides local explanations
for individual predictions (Ribeiro et al 2016). LIME works by generating perturbated sam-
ple data around a data point and obtaining predictions from the black-box model. Based on
this, a simple linear model is trained to identify the important features in that prediction.
Yang et al (2023b) proposes an improved LIME algorithm to address the interpretability
issues of black-box models in wind power forecasting and applies it to a wind power predic-
tion model. This model introduces a trust index to quantify how reliable the features used by
the prediction model are and analyzes how the black-box model handles important features
in the prediction. Additionally, this model proposes global trust modeling and interpretable
feature selection methods, demonstrating that these approaches can enhance the model’s
reliability and reduce prediction errors.
Feature attribution is a method that calculates how much each input feature contributed
to the model’s prediction and evaluates the contribution of input features for a specific
prediction. SHapley Additive exPlanations (SHAP) is a representative feature attribution
technique based on the Shapley value concept from game theory (Lundberg and Lee 2017).
SHAP fairly measures the contribution of each feature to model predictions. SHAP visu-
alizes the importance of features from both global and local perspectives and helps iden-
tify interactions between model predictions and features. The key idea behind SHAP is to
compute the average contribution of each feature across all possible feature combinations,
which allows the decomposition of predictions into feature contributions, providing intui-
tive and interpretable results. García and Aznarte (2020) uses an LSTM model to predict
NO2 concentrations and presents a method for interpreting the prediction results based on
SHAP. While SHAP values are typically applied to linear models, this study extends SHAP
by applying Deep SHAP to accommodate the nonlinear characteristics of deep learning
models, making it easier to understand the complex decision-making process of deep learn-
ing models (Chen et al 2022).
Counterfactual explanations describe what inputs need to be altered to change a specific
prediction (Wachter et al 2017). Counterfactual explanations generate counterfactual inputs
that would alter the prediction. In time series research, counterfactual explanations have
been widely used in classification tasks, but their application to forecasting models has
been relatively underexplored (Wang et al 2023b). In time series forecasting, exogenous
variables make predictions more complex, which highlights the importance of setting range
1 3

216 Page 80 of 95 J. Kim et al.
constraints (Papapetrou and Lee 2024). ForecastCF is a model that generates counterfactual
explanations to explain the predictions of time series forecasting models (Wang et al 2023b).
This model modifies the time series data through gradient-based perturbation to ensure the
model’s predictions fall within a specified range, thus improving the model’s explainability.
Specifically, users define the desired prediction range, and the model generates predictions
that satisfy these constraints, making the predictions more intuitive and understandable.
5.7 Spatio-temporal time series forecasting
As the structure of time series data becomes increasingly complex, spatial information is
now frequently incorporated into the datasets. Spatio-temporal time series data refers to
datasets that simultaneously capture temporal variations and spatial distributions. This type
of data consists of values that change over time at specific locations, possessing both spatial
interactions and temporal dependencies. Due to these characteristics, it provides critical
information not only from patterns extracted along the time axis but also from spatial depen-
dencies caused by interactions between locations. For example, region-based traffic flow, air
pollution levels, climate change, and electricity consumption are representative cases. The
rapid advancements in technologies such as satellite data and GPS have led to an explo-
sive increase in location-based data. Therefore, spatio-temporal data modeling has become
increasingly important, as many real-world problems cannot be adequately explained by
temporal variations alone (Sun et al 2024a). Conventional multivariate time series models
often fail to adequately address spatial correlations or network structures, necessitating their
extension to spatio-temporal models. To address this, numerous approaches utilizing GNNs
and Transformers have been actively explored (Jin et al 2023; Yang et al 2024a; Chen et al
2021a; Park et al 2020).
Several representative approaches for handling spatio-temporal data are as follows. One
is the Graph-Based Method for spatio-temporal modeling. Data is represented as a graph,
where spatial relationships between locations (nodes) are expressed as edges. GCNs or
graph-based RNNs are used to simultaneously learn spatial and temporal dependencies.
This approach effectively models non-euclidean structured data but has drawbacks, such
as complex preprocessing and high computational costs. These approaches are well-suited
for applications such as traffic flow prediction by modeling road networks or electricity
demand forecasting by modeling connections between substations. DCRNN (Li et al 2018)
models traffic networks as directed graphs using Diffusion Convolution, effectively captur-
ing spatial dependencies, including upstream and downstream node relationships. It also
leverages GRU to capture temporal patterns and non-linearities, making it a representative
graph-based model for handling complex time series data. ST-GCN (Yan et al 2018) mod-
els skeleton dataset as graphs and extends GCN along the temporal axis to simultaneously
model spatial and temporal dependencies. DB-STGCN (Li et al 2024a) predicts train delays
by integrating dynamic adjacency matrices generated through Dynamic Bayesian Networks
(DBN) into ST-GCN to capture spatio-temporal dependencies. It improves prediction accu-
racy and interpretability through the integration of attention mechanisms and the combina-
tion of GCN and GRU.
Another approach is the raster-based method. Data is converted into a 2D grid (raster) or
video format to learn spatial locations and temporal patterns. Grid-based data representa-
tion: A specific space is divided into grids, and data over time is collected for each grid cell.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 81 of 95 216
Video-based data representation: Data is transformed into a 3D tensor, including the time
axis. This format allows easy application of image processing techniques, such as CNNs,
and 3D CNNs are particularly effective for directly learning spatio-temporal patterns. How-
ever, there are limitations in learning overly complex spatial relationships. They are suit-
able for modeling climate data from satellite imagery or recognizing actions in video data
through spatiotemporal dynamics. ConvLSTM (Shi et al 2015) replaces the fully connected
state transitions of conventional LSTM with convolutions to learn spatial correlations, mak-
ing it a representative early raster-based method. It represents all inputs, hidden states, and
cell states as 3D tensors to maintain the grid-like spatial structure. ST-ResNet (Zhang et al
2017) models citywide crowd flows based on residual learning. It partitions the city into a
grid structure and represents the inflow and outflow of each grid cell as 2-channel image
data. Residual networks are employed to effectively learn interactions between both nearby
and distant regions. SLCNN (Zhang et al 2020) utilizes Structure Learning Convolution
(SLC) to define graphs as learnable parameters for the effective modeling of both global
static structures and dynamic structures within datasets. It replaces conventional CNN con-
volutions with SLC tailored to graph structures, generating graph-specific representations
at each layer.
Recently, there have also been efforts to combine graph-based and raster-based method-
ologies to more effectively model both spatial structures and temporal dependencies. They
are ideal for representing traffic flow as graphs and enabling detailed analysis of each node
in smart city data. GMAN (Zheng et al 2020) effectively learns the dynamic spatio-temporal
relationships in traffic networks through Spatio-Temporal Embedding (STE) and ST-Atten-
tion Block. It utilizes spatial attention to capture dynamic relationships between sensors,
temporal attention to learn nonlinear temporal patterns, and gated fusion to integrate these
features seamlessly. STSGCN (Song et al 2020) employs the Spatial-Temporal Synchro-
nous Graph Convolutional Module (STSGCM) to synchronize and learn spatial and tem-
poral dependencies. It constructs a localized spatial-temporal graph to model relationships
between neighboring nodes within the same time frame and nodes from past or future time
frames simultaneously. GCN-SBULSTM (Chen et al 2021b) proposes a model that com-
bines GCN with Stacked Bidirectional Unidirectional LSTM (SBULSTM). The Bidirec-
tional LSTM captures temporal patterns, while GCN learns spatial dependencies, enabling
integrated modeling of spatio-temporal interactions. Additionally, sequence-based methods
process spatio-temporal data in sequence form, focusing primarily on temporal dynamics.
The primary objective of spatio-temporal time series prediction models is to address
the challenging task of integrating complex data structures while simultaneously learning
temporal dependencies and spatial interactions. This enables accurate future state prediction
and helps solve various real-world problems, facilitating precise decision-making.
6 Conclusion
This survey has been prepared to broaden the expertise of existing researchers and to assist
beginners in gaining a fundamental understanding amid the rapid growth of time series fore-
casting (TSF) research. By integrating key concepts of time series and the latest techniques,
we aim to provide researchers with clear direction and insights, fostering the continued
advancement of this field. This survey paper comprehensively reviews recent advancements
1 3

216 Page 82 of 95 J. Kim et al.
in TSF, focusing on deep learning models. It also incorporates key papers from major AI
and ML conferences, as well as several notable papers from the arXiv preprint repository
(https://arxiv.org).
TSF is a highly regarded topic, gradually expanding from the prominence of Transformer
models to various architecture-based models. Fundamental deep learning models like
MLPs, CNNs, RNNs, and GNNs are being reassessed, and Transformers are also advanc-
ing by overcoming their previous limitations. Additionally, innovative models like Mamba
are emerging, and models such as Diffusion are also entering the field, experiencing rapid
growth. Furthermore, as the demand for foundation models in the field of TSF intensi-
fies, pre-trained models based on large language models (LLMs) are emerging. To create
a powerful predictive model, researchers need to be aware of these trends and understand
both the characteristics of time series data and the strengths and weaknesses of different
architectures.
Taking it a step further, we aim to address common challenges in TSF and provide deep
insights into future development directions. In particular, we reviewed various studies that
focus on approaches to channel correlation and address the challenges of distribution shift,
which frequently occur in real-world scenarios. Additionally, we emphasized the need for
research that leverages causality to eliminate spurious correlations, thereby enabling a
deeper understanding of the underlying essence. We also discussed the importance of stud-
ies focused on effectively extracting features from complex time series data. In addition, we
explored model combination techniques aimed at enhancing model performance, as well as
spatio-temporal TSF problems to address complex real-world issues. Furthermore, we pro-
vided insights into improving model reliability by addressing interpretability and explain-
ability. Through this, we aim to present readers with potential directions for future research.
Limitations and future work
This survey acknowledges several limitations that could be addressed in future research.
● We skipped the detailed theoretical backgrounds of the models. This survey aims to
provide a comprehensive overview, facilitating comparison and analysis, thereby allow-
ing researchers to explore areas of interest more effectively. Although comprehensive
information is primarily provided, readers can access additional details through refer-
ence links if needed.
● We left the specific differences in characteristics across various time series datasets for
future work. Time series data is often domain-specific, requiring expert knowledge,
which can be integrated into models to enhance performance. This underscores the im-
portance of interdisciplinary collaboration, and future research should continue to de-
velop in this direction. By integrating insights from a wide range of academic fields into
TSF, it can contribute to the development of robust and generalized models.
● The aspect of expanding Artificial General Intelligence (AGI) and Adaptive Modeling
could be further explored. Research on techniques such as meta-learning, reinforce-
ment learning, and neuro-symbolic AI can enhance the generalization and adaptability
of models. In the current TSF field, time series-specific models and deep learning-based
standard methodologies are dominant. However, as TSF problems become increasingly
complex, research on generalization and adaptability holds great potential.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 83 of 95 216
Acknowledgements This work was supported by Institute of Information & communications Technology
Planning & Evaluation (IITP) grant funded by the Korea government (MSIT) [No. RS-2021-II211343, Arti-
ficial Intelligence Graduate School Program (Seoul National University); IITP-2025-RS-2024-00397085, the
Leading Generative AI Human Resources Development], the National Research Foundation of Korea (NRF)
grant funded by the Korea government (MSIT) (No. 2022R1A3B1077720; No. 2022R1A5A708390811), the
BK21 FOUR program of the Education and the Research Program for Future ICT Pioneers, Seoul National
University in 2025. H.G. Kim and S. Yoon were supported by Samsung Electronics Co., Ltd (IO240124-
08661-01).We would like to express our heartfelt gratitude to Jisoo Mok, Hyeongrok Han, Bonggyun Kang,
Junyong Ahn, Jiin Kim, Youngwoo Kimh, Hyungyu Lee, Juhyeon Shin, Jaihyun Lew, and Jieun Byeon from
our research lab for their invaluable assistance in reviewing and providing feedback on this paper. Their
insights and suggestions have significantly enhanced the quality of our work.
Author Contributions Jongseon Kim and Hyungjoon Kim contributed equally as co-first authors. They were
responsible for setting the research direction and overall organization, conducting literature review and anal-
ysis, writing the manuscript, creating visual materials, and final revision. HyunGi Kim, as the third author,
contributed to the literature review and draft writing of the sections on foundation models, distribution shift,
and causality. Dongjun Lee, as the fourth author, contributed to the literature review and draft writing of the
initial transformer-based models section. Sungroh Yoon guided the literature survey and the writing of the
main manuscript text as the corresponding author. All the authors participated in writing and reviewing the
manuscript.
Data Availability No datasets were generated or analysed during the current study.
Declarations
Competing interests The authors declare no competing interests.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License,
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as
you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons
licence, and indicate if changes were made. The images or other third party material in this article are
included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material.
If material is not included in the article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Abu-Mostafa YS, Atiya AF (1996) Introduction to financial forecasting. Appl Intell 6:205–213
Achiam J, Adler S, Agarwal S, et al (2023) Gpt-4 technical report. Preprint at arXiv:2303.08774
Ahamed MA, Cheng Q (2024) TimeMachine: a time series is worth 4 Mambas for long-term forecasting. IOS
Press. https://doi.org/10.3233/faia240677 (http://dx.doi.org/10.3233/faia240677)
Ahmed DM, Hassan MM, Mstafa RJ (2022) A review on deep sequential models for forecasting time series
data. Appl Comput Intell Soft Comput 1:6596397
Alcaraz JL, Strodthoff N (2023) Diffusion-based time series imputation and forecasting with structured state
space models. Transactions on Machine Learning Research h t t p s : / / o p e n r e v i e w . n e t / f o r u m ? i d = h H i I b k 7
A p W
Alghamdi T, Elgazzar K, Bayoumi M, et al (2019) Forecasting traffic congestion using arima modeling. In:
2019 15th international wireless communications & mobile computing conference (IWCMC), IEEE,
pp 1227–1232
Ansari AF, Stella L, Turkmen AC, et al (2024) Chronos: Learning the language of time series. Transactions
on Machine Learning Research https://openreview.net/forum?id=gerNCVqqtR, Expert Certification
Athanasopoulos G, Hyndman RJ, Song H et al (2011) The tourism forecasting competition. Int J Forecast
27(3):822–844
Bai S, Kolter JZ, Koltun V (2018) An empirical evaluation of generic convolutional and recurrent networks
for sequence modeling. Preprint at arXiv:1803.01271
1 3

216 Page 84 of 95 J. Kim et al.
Barlin JN, Zhou Q, Clair CMS et al (2013) Classification and regression tree (cart) analysis of endometrial
carcinoma: seeing the forest for the trees. Gynecol Oncol 130(3):452–456
Behrouz A, Santacatterina M, Zabih R (2024) Chimera: Effectively modeling multivariate time series with
2-dimensional state space models. In: The Thirty-eighth Annual Conference on Neural Information
Processing Systems, https://openreview.net/forum?id=ncYGjx2vnE
Beltagy I, Peters ME, Cohan A (2020) Longformer: The long-document transformer. Preprint at
arXiv:2004.05150
Benidis K, Rangapuram SS, Flunkert V et al (2022) Deep learning for time series forecasting: Tutorial and
literature survey. ACM Comput Surv 55(6):1–36
Bergsma S, Zeyl T, Guo L (2023) Sutranets: sub-series autoregressive networks for long-sequence, probabi-
listic forecasting. Adv Neural Inf Process Syst 36:30518–30533
Box GE, Jenkins GM, Reinsel G et al (1970) Forecasting and control. Time Series. Analysis 3(75):1970
Breiman L (1996) Bagging predictors. Mach Learning 24:123–140
Brown RG (1959) Statistical forecasting for inventory control. (No Title)
Brown T, Mann B, Ryder N et al (2020) Language models are few-shot learners. Adv Neural Inf Process
Syst 33:1877–1901
Cai W, Liang Y, Liu X, et al (2024a) Msgnet: Learning multi-scale inter-series correlations for multivari-
ate time series forecasting. In: Proceedings of the AAAI Conference on Artificial Intelligence, pp
11141–11149
Cai W, Wang K, Wu H, et al (2024b) Forecastgrapher: Redefining multivariate time series forecasting with
graph neural networks. Preprint at arXiv:2405.18036
Cai X, Zhu Y, Wang X, et al (2024c) Mambats: Improved selective state space models for long-term time
series forecasting. Preprint at arXiv:2405.16440
Cao H, Tan C, Gao Z, et al (2024) A survey on generative diffusion models. IEEE Transactions on Knowledge
and Data Engineering
Center JMK (2020) Dominick’s dataset
Challu C, Olivares KG, Oreshkin BN, et al (2023) Nhits: Neural hierarchical interpolation for time series
forecasting. In: Proceedings of the AAAI conference on artificial intelligence, pp 6989–6997
Chang S, Zhang Y, Han W, et al (2017) Dilated recurrent neural networks. Adv Neural Inform Process Syst 30
Chen P, Fu X, Wang X (2021) A graph convolutional stacked bidirectional unidirectional-LSTM neural net-
work for metro ridership prediction. IEEE Trans Intell Transp Syst 23(7):6950–6962
Chen Y, Zou X, Li K et al (2021) Multiple local 3D CNNs for region-based prediction in smart cities. Inf
Sci 542:476–491
Chen H, Lundberg SM, Lee SI (2022) Explaining a series of models by propagating Shapley values. Nat
Commun 13(1):4512
Chen Z, Ma M, Li T et al (2023) Long sequence time-series forecasting with deep learning: a survey. Inform
Fusion 97:101819
Chen K, Chen G, Xu D, et al (2021a) Nast: Non-autoregressive spatial-temporal transformer for time series
forecasting. Preprint at arXiv:2102.05624
Cheng X, Chen X, Li S, et al (2024c) Leveraging 2D information for long-term time series forecasting with
vanilla transformers. Preprint at arXiv:2405.13810
Chen T, Guestrin C (2016) Xgboost: A scalable tree boosting system. In: Proceedings of the 22nd ACM SIG-
KDD international conference on knowledge discovery and data mining, pp 785–794
Cheng H, Wen Q, Liu Y, et al (2024a) Robusttsf: Towards theory and design of robust time series forecasting
with anomalies. ICRL
Cheng M, Yang J, Pan T, et al (2024b) Convtimenet: A deep hierarchical fully convolutional model for mul-
tivariate time series analysis. Preprint at arXiv:2403.01493
Chen J, Lenssen JE, Feng A, et al (2024a) From similarity to superiority: Channel clustering for time series
forecasting. In: The Thirty-eighth Annual Conference on Neural Information Processing Systems,
https://openreview.net/forum?id=MDgn9aazo0
Chen X, Li X, Liu B, et al (2024c) Biased temporal convolution graph network for time series forecasting
with missing values. In: The Twelfth International Conference on Learning Representations
Chen Y, Ren K, Wang Y, et al (2024d) Contiformer: Continuous-time transformer for irregular time series
modeling. Adv Neural Inform Process Syst 36
Chen P, ZHANG Y, Cheng Y, et al (2024b) Pathformer: Multi-scale transformers with adaptive pathways for
time series forecasting. In: The Twelfth International Conference on Learning Representations, h t t p s : / /
o p e n r e v i e w . n e t / f o r u m ? i d = l J k O C M P 2 a W
Chicco D, Warrens MJ, Jurman G (2021) The coefficient of determination r-squared is more informative than
SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation. Peer J Comput Sci 7:e623
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 85 of 95 216
Cho K, van Merriënboer B, Gulcehre C, et al (2014) Learning phrase representations using RNN encoder–
decoder for statistical machine translation. In: Moschitti A, Pang B, Daelemans W (eds) Proceedings
of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP). Association
for Computational Linguistics, Doha, Qatar, pp 1724–1734, https://doi.org/10.3115/v1/D14-1179, h t t p
s : / / a c l a n t h o l o g y . o r g / D 1 4 - 1 1 7 9 /
Clark K, Luong MT, Le QV, et al (2020) Electra: Pre-training text encoders as discriminators rather than
generators. In: International Conference on Learning Representations, h t t p s : / / o p e n r e v i e w . n e t / f o r u m ?
i d = r 1 x M H 1 B t v B
Cortes C (1995) Support-vector networks. Machine Learning
Coskunuzer B, Segovia-Dominguez I, Chen Y, et al (2024) Time-aware knowledge representations of
dynamic objects with multidimensional persistence. In: Proceedings of the AAAI Conference on Arti-
ficial Intelligence, pp 11678–11686
Crabbé J, Huynh N, Stanczuk JP, et al (2024) Time series diffusion in the frequency domain. In: Forty-first
International Conference on Machine Learning, https://openreview.net/forum?id=W9GaJUVLCT
Cryer JD (1986) Time series analysis, vol 286. Duxbury Press Boston
Dai Z, Yang Z, Yang Y, et al (2019) Transformer-XL: Attentive language models beyond a fixed-length
context. In: Korhonen A, Traum D, Màrquez L (eds) Proceedings of the 57th Annual Meeting of the
Association for Computational Linguistics. Association for Computational Linguistics, Florence, Italy,
pp 2978–2988, https://doi.org/10.18653/v1/P19-1285, https://aclanthology.org/P19-1285
Danese P, Kalchschmidt M (2011) The role of the forecasting process in improving forecast accuracy and
operational performance. Int J Prod Econ 131(1):204–214. https://doi.org/10.1016/j.ijpe.2010.09.006 (
h t t p s : / / w w w . s c i e n c e d i r e c t . c o m / s c i e n c e / a r t i c l e / p i i / S 0 9 2 5 5 2 7 3 1 0 0 0 3 2 8 2 , i n n s b r u c k 2 0 0 8)
Das A, Kong W, Sen R, et al (2024) A decoder-only foundation model for time-series forecasting. In: Forty-
first International Conference on Machine Learning, https://openreview.net/forum?id=jn2iTJas6h
Devlin J, Chang MW, Lee K, et al (2019) BERT: Pre-training of deep bidirectional transformers for language
understanding. In: Burstein J, Doran C, Solorio T (eds) Proceedings of the 2019 Conference of the
North American Chapter of the Association for Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers). Association for Computational Linguistics, Minneapolis,
Minnesota, pp 4171–4186, https://doi.org/10.18653/v1/N19-1423, https://aclanthology.org/N19-1423
Dimri T, Ahmad S, Sharif M (2020) Time series analysis of climate variables using seasonal ARIMA
approach. J Earth Syst Sci 129:1–16
Dosovitskiy A, Beyer L, Kolesnikov A, et al (2021) An image is worth 16x16 words: Transformers for image
recognition at scale. In: International Conference on Learning Representations, h t t p s : / / o p e n r e v i e w . n e t
/ f o r u m ? i d = Y i c b F d N T T y
Dragomiretskiy K, Zosso D (2013) Variational mode decomposition. IEEE Trans Signal Process
62(3):531–544
Dubey A, Jauhri A, Pandey A, et al (2024) The llama 3 herd of models. Preprint at arXiv:2407.21783
Dudek G (2024) Stacking for probabilistic short-term load forecasting. In: International Conference on Com-
putational Science, Springer, pp 3–18
Ekambaram V, Jati A, Dayama P, et al (2024) Tiny time mixers (ttms): Fast pre-trained models for enhanced
zero/few-shot forecasting of multivariate time series. CoRR
Ekambaram V, Jati A, Nguyen N, et al (2023) TSMIXER: Lightweight MLP-mixer model for multivariate
time series forecasting. In: Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discov-
ery and Data Mining, pp 459–469
Eldele E, Ragab M, Chen Z, et al (2021) Time-series representation learning via temporal and contextual con-
trasting. Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21)
Eldele E, Ragab M, Chen Z, et al (2024) Tslanet: Rethinking transformers for time series representation
learning. International Conference on Machine Learning
Fan W, Wang P, Wang D, et al (2023) DISH-TS: a general paradigm for alleviating distribution shift in time
series forecasting. In: Proceedings of the AAAI Conference on Artificial Intelligence, pp 7522–7529
Fan X, Wu Y, Xu C, et al (2024b) MG-TSD: Multi-granularity time series diffusion models with guided
learning process. In: The Twelfth International Conference on Learning Representations, h t t p s : / / o p e n r
e v i e w . n e t / f o r u m ? i d = C Z i Y 6 O L k t d
Fan H, Xiong B, Mangalam K, et al (2021) Multiscale vision transformers. In: Proceedings of the IEEE/CVF
international conference on computer vision, pp 6824–6835
Fan W, Yi K, Ye H, et al (2024a) Deep frequency derivative learning for non-stationary time series forecast-
ing. IJCAI
Feng R, Chen M, Song Y (2024) Learning traffic as videos: short-term traffic flow prediction using mixed-
pointwise convolution and channel attention mechanism. Expert Syst Appl 240:122468
Feng S, Miao C, Zhang Z, et al (2024b) Latent diffusion transformer for probabilistic time series forecasting.
In: Proceedings of the AAAI Conference on Artificial Intelligence, pp 11979–11987
1 3

216 Page 86 of 95 J. Kim et al.
Freund Y, Schapire RE (1997) A decision-theoretic generalization of on-line learning and an application to
boosting. J Comput Syst Sci 55(1):119–139
Friedman JH (2001) Greedy function approximation: a gradient boosting machine. Annals of statistics pp
1189–1232
Fu DY, Dao T, Saab KK, et al (2023) Hungry hungry hippos: Towards language modeling with state space
models. In The International Conference on Learning Representations (ICLR)
Fukushima K (1980) Neocognitron: a self-organizing neural network model for a mechanism of pattern rec-
ognition unaffected by shift in position. Biol Cybern 36(4):193–202
Gallifant J, Fiske A, Levites Strekalova YA et al (2024) Peer review of GPT-4 technical report and systems
card. PLOS Digital Health 3(1):e0000417
Ganaie MA, Hu M, Malik AK et al (2022) Ensemble deep learning: a review. Eng Appl Artif Intell 115:105151
García MV, Aznarte JL (2020) Shapley additive explanations for no2 forecasting. Eco Inform 56:101039
Godahewa R, Bergmeir C, Webb G, et al (2021a) Solar power dataset (4 seconds observations). h t t p s : / / d o i .
o r g / 1 0 . 5 2 8 1 / z e n o d o . 4 6 5 6 0 2 7
Godahewa R, Bergmeir C, Webb G et al (2021b) Wind farms dataset (with missing values). h t t p s : / / d o i . o r g /
1 0 . 5 2 8 1 / z e n o d o . 4 6 5 4 9 0 9
Godahewa R, Bergmeir C, Webb G et al (2021c) Wind farms dataset (without missing values). h t t p s : / / d o i . o
r g / 1 0 . 5 2 8 1 / z e n o d o . 4 6 5 4 8 5 8
Godahewa R, Bergmeir C, Webb G et al (2021e) Australian electricity demand dataset. h t t p s : / / d o i . o r g / 1 0 . 5
2 8 1 / z e n o d o . 4 6 5 9 7 2 7
Godahewa R, Bergmeir C, Webb G et al (2021f) Bitcoin dataset with missing values. h t t p s : / / d o i . o r g / 1 0 . 5 2 8
1 / z e n o d o . 5 1 2 1 9 6 5
Godahewa R, Bergmeir C, Webb G et al (2021g) Bitcoin dataset without missing values. h t t p s : / / d o i . o r g / 1 0 .
5 2 8 1 / z e n o d o . 5 1 2 2 1 0 1
Godahewa R, Bergmeir C, Webb G et al (2021h) Rideshare dataset with missing values. h t t p s : / / d o i . o r g / 1 0 . 5
2 8 1 / z e n o d o . 5 1 2 2 1 1 4
Godahewa R, Bergmeir C, Webb G et al (2021i) Rideshare dataset without missing values. h t t p s : / / d o i . o r g / 1
0 . 5 2 8 1 / z e n o d o . 5 1 2 2 2 3 2
Godahewa R, Bergmeir C, Webb G et al (2021j) Temperature rain dataset with missing values. h t t p s : / / d o i . o
r g / 1 0 . 5 2 8 1 / z e n o d o . 5 1 2 9 0 7 3
Godahewa R, Bergmeir C, Webb G et al (2021k) Temperature rain dataset without missing values. h t t p s : / / d
o i . o r g / 1 0 . 5 2 8 1 / z e n o d o . 5 1 2 9 0 9 1
Godahewa RW, Bergmeir C, Webb GI, et al (2021l) Monash time series forecasting archive. In: Thirty-fifth
Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2),
https://openreview.net/forum?id=wEc1mgAjU-
Godahewa R, Bergmeir C, Webb G, et al (2021d) Wind power dataset (4 seconds observations). h t t p s : / / d o i .
o r g / 1 0 . 5 2 8 1 / z e n o d o . 4 6 5 6 0 3 2
Gong Z, Tang Y, Liang J (2023) Patchmixer: A patch-mixing architecture for long-term time series forecast-
ing. Preprint at arXiv:2310.00655
Granger CW (1969) Investigating causal relations by econometric models and cross-spectral methods.
Econometrica: J Econom Soc 424–438
Graziani M, Dutkiewicz L, Calvaresi D et al (2023) A global taxonomy of interpretable AI: unifying the
terminology for the technical and social sciences. Artif Intell Rev 56(4):3473–3504
Gruver N, Finzi MA, Qiu S, et al (2023) Large language models are zero-shot time series forecasters. In:
Thirty-seventh Conference on Neural Information Processing Systems, h t t p s : / / o p e n r e v i e w . n e t / f o r u m ?
i d = m d 6 8 e 8 i Z K 1
Gu A, Johnson I, Goel K et al (2021) Combining recurrent, convolutional, and continuous-time models with
linear state space layers. Adv Neural Inf Process Syst 34:572–585
Gu A, Dao T (2024) Mamba: Linear-time sequence modeling with selective state spaces. In: First Conference
on Language Modeling, https://openreview.net/forum?id=tEYskw1VY2
Gu A, Goel K, Re C (2022) Efficiently modeling long sequences with structured state spaces. In: International
Conference on Learning Representations, https://openreview.net/forum?id=uYLFoz1vlAC
Hahn Y, Langer T, Meyes R et al (2023) Time series dataset survey for forecasting with deep learning. Fore-
casting 5(1):315–335
Hamon R, Junklewitz H, Sanchez I et al (2022) Bridging the gap between AI and explainability in the
GDPR: towards trustworthiness-by-design in automated decision-making. IEEE Comput Intell Mag
17(1):72–85
Han H, Park S, Min S et al (2023) Improving generalization performance of electrocardiogram classification
models. Physiol Meas 44(5):054003
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 87 of 95 216
Han L, Chen XY, Ye HJ, et al (2024) SOFTS: Efficient multivariate time series forecasting with series-core
fusion. In: The Thirty-eighth Annual Conference on Neural Information Processing Systems, h t t p s : / / o p
e n r e v i e w . n e t / f o r u m ? i d = 8 9 A U i 5 L 1 u A
Han H, Kim S, Choi HS, et al (2023a) On the impact of knowledge distillation for model interpretability. In:
Proceedings of the 40th International Conference on Machine Learning. JMLR.org, ICML’23
Hasson H, Maddix DC, Wang B, et al (2023) Theoretical guarantees of learning ensembling strategies with
applications to time series forecasting. In: International Conference on Machine Learning, PMLR, pp
12616–12632
Ho J, Jain A, Abbeel P (2020) Denoising diffusion probabilistic models. Adv Neural Inf Process Syst
33:6840–6851
Hochreiter S, Schmidhuber J (1997) Long short-term memory. Neural Comput 9(8):1735–1780
Holt CC (1957) Forecasting trends and seasonals by exponentially weighted averages. Carnegie institute of
technology. Pittsburgh ONR memorandum
Hopfield JJ (1982) Neural networks and physical systems with emergent collective computational abilities.
Proc Natl Acad Sci 79(8):2554–2558
Hounie I, Porras-Valenzuela J, Ribeiro A (2024) Transformers with loss shaping constraints for long-term
time series forecasting. In: Forty-first International Conference on Machine Learning
Hou H, Yu FR (2024) Rwkv-ts: Beyond traditional recurrent neural network for time series tasks. Preprint
at arXiv:2401.09093
Huang NE, Shen Z, Long SR et al (1998) The empirical mode decomposition and the Hilbert spectrum for
nonlinear and non-stationary time series analysis. Proc R Soc Lond Ser A 454(1971):903–995
Huang S, Liu Y, Zhang F et al (2024) Crosswavenet: a dual-channel network with deep cross-decomposition
for long-term time series forecasting. Expert Syst Appl 238:121642
Huang Q, Shen L, Zhang R, et al (2024a) HDMIXER: Hierarchical dependency with extendable patch for
multivariate time series forecasting. In: Proceedings of the AAAI Conference on Artificial Intelligence,
pp 12608–12616
Huber PJ (1992) Robust estimation of a location parameter. In: Breakthroughs in statistics: Methodology and
distribution. Springer, pp 492–518
Hu J, Lan D, Zhou Z, et al (2024a) Time-ssm: Simplifying and unifying state space models for time series
forecasting. CoRR abs/2405.16312. https://doi.org/10.48550/arXiv.2405.16312
Hu Y, Liu P, Zhu P, et al (2024b) Adaptive multi-scale decomposition framework for time series forecasting.
CoRR abs/2406.03751. https://doi.org/10.48550/arXiv.2406.03751
Ilbert R, Odonnat A, Feofanov V, et al (2024) SAMformer: Unlocking the potential of transformers in time
series forecasting with sharpness-aware minimization and channel-wise attention. In: Salakhutdinov R,
Kolter Z, Heller K, et al (eds) Proceedings of the 41st International Conference on Machine Learning,
Proceedings of Machine Learning Research, vol 235. PMLR, pp 20924–20954, h t t p s : / / p r o c e e d i n g s . m l
r . p r e s s / v 2 3 5 / i l b e r t 2 4 a . h t m l
Ioffe S, Szegedy C (2015) Batch normalization: Accelerating deep network training by reducing internal
covariate shift. In: International conference on machine learning, pmlr, pp 448–456
Jhin SY, Kim S, Park N (2024) Addressing prediction delays in time series forecasting: A continuous gru
approach with derivative regularization. In: Proceedings of the 30th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining, pp 1234–1245
Jia Y, Lin Y, Hao X, et al (2024) Witran: Water-wave information transmission and recurrent acceleration
network for long-range time series forecasting. Adv Neural Inform Process Syst 36
Jin M, Wang S, Ma L, et al (2024) Time-LLM: Time series forecasting by reprogramming large language
models. In: International Conference on Learning Representations (ICLR)
Jin M, Wen Q, Liang Y, et al (2023) Large models for time series and Spatio-temporal data: a survey and
outlook. Preprint at arXiv:2310.10196
Jung D, Lee J, Yi J, et al (2020) ICAPS: an interpretable classifier via disentangled capsule networks. In:
European Conference on Computer Vision, Springer, pp 314–330
Kalman RE (1960) A new approach to linear filtering and prediction problems. Transact ASME-J Basic Eng
82(1):35–45
Kang BG, Lee D, Kim H, et al (2024) Introducing spectral attention for long-range dependency in time series
forecasting. Adv Neural Inform Process Syst
Ke G, Meng Q, Finley T, et al (2017) LIGHTGBM: A highly efficient gradient boosting decision tree. Adv
Neural Inform Process Syst 30
Khosravi A, Mazloumi E, Nahavandi S et al (2011) Prediction intervals to account for uncertainties in travel
time prediction. IEEE Trans Intell Transp Syst 12(2):537–547
Kim D, Baek JG (2022) Bagging ensemble-based novel data generation method for univariate time series
forecasting. Expert Syst Appl 203:117366
1 3

216 Page 88 of 95 J. Kim et al.
Kim T, Kim J, Tae Y, et al (2021) Reversible instance normalization for accurate time-series forecasting
against distribution shift. In: International Conference on Learning Representations
Kim D, Park J, Lee J, et al (2024) Are self-attentions effective for time series forecasting? In: The Thirty-
eighth Annual Conference on Neural Information Processing Systems, h t t p s : / / o p e n r e v i e w . n e t / f o r u m ? i
d = i N 4 3 s J o i b 7
Kim S, Yi J, Kim E, et al (2020) Interpretation of NLP models through input marginalization. In: Webber B,
Cohn T, He Y, et al (eds) Proceedings of the 2020 Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP). Association for Computational Linguistics, Online, pp 3154–3167, h t t p s : /
/ d o i . o r g / 1 0 . 1 8 6 5 3 / v 1 / 2 0 2 0 . e m n l p - m a i n . 2 5 5, h t t p s : / / a c l a n t h o l o g y . o r g / 2 0 2 0 . e m n l p - m a i n . 2 5 5 /
Kipf TN, Welling M (2017) Semi-supervised classification with graph convolutional networks. In: Interna-
tional Conference on Learning Representations, https://openreview.net/forum?id=SJU4ayYgl
Kitaev N, Kaiser L, Levskaya A (2020) Reformer: The efficient transformer. In: International Conference on
Learning Representations, https://openreview.net/forum?id=rkgNKkHtvB
Koenker R, Bassett Jr G (1978) Regression quantiles. Econometrica: J Econom Soc 33–50
Kollovieh M, Ansari AF, Bohlke-Schneider M, et al (2024) Predict, refine, synthesize: Self-guiding diffusion
models for probabilistic time series forecasting. Adv Neural Inform Process Syst 36
Kong Z, Ping W, Huang J, et al (2021) Diffwave: A versatile diffusion model for audio synthesis. In: Interna-
tional Conference on Learning Representations, https://openreview.net/forum?id=a-xFK8Ymz5J
Kontopoulou VI, Panagopoulos AD, Kakkos I et al (2023) A review of Arima vs. machine learning approaches
for time series forecasting in data driven networks. Future Internet 15(8):255
LeCun Y, Bottou L, Bengio Y et al (1998) Gradient-based learning applied to document recognition. Proc
IEEE 86(11):2278–2324
Liang A, Jiang X, Sun Y, et al (2024a) Bi-mamba4ts: Bidirectional mamba for time series forecasting. Pre-
print at arXiv:2404.15772
Liang Y, Wen H, Nie Y, et al (2024c) Foundation models for time series analysis: A tutorial and survey. Pre-
print at arXiv:2403.14735
Liang D, Zhang H, Yuan D, et al (2024b) Minusformer: Improving time series forecasting by progressively
learning residuals. Preprint at arXiv:2402.02332
Li Y, Chen W, Hu X, et al (2024b) Transformer-modulated diffusion models for probabilistic multivariate
time series forecasting. In: The Twelfth International Conference on Learning Representations, h t t p s : / /
o p e n r e v i e w . n e t / f o r u m ? i d = q a e 0 4 Y A C H s
Li S, Jin X, Xuan Y, et al (2019) Enhancing the locality and breaking the memory bottleneck of transformer
on time series forecasting. Adv Neural Inform Process Syst 32
Li J, Li D, Savarese S, et al (2023) Blip-2: Bootstrapping language-image pre-training with frozen image
encoders and large language models. In: International conference on machine learning, PMLR, pp
19730–19742
Lim B, Zohren S (2021) Time-series forecasting with deep learning: a survey. Phil Trans R Soc A
379(2194):20200209
Lim B, Arık SÖ, Loeff N et al (2021) Temporal fusion transformers for interpretable multi-horizon time series
forecasting. Int J Forecast 37(4):1748–1764
Lin K, Huang C (2022) Ensemble learning applications in multiple industries: a review. Inf Dyn Appl
1(1):44–58
Lin L, Li Z, Li R et al (2024) Diffusion models for time-series applications: a survey. Front Inform Technol
Electron Eng 25(1):19–41
Lin S, Lin W, Wu W et al (2024) SPARSETSF: Modeling long-term time series forecasting with 1k parameters
Lin S, Lin W, Wu W, et al (2024c) PETformer: Long-term time series forecasting via placeholder-enhanced
transformer. https://openreview.net/forum?id=u3RJbzzBZj
Lipton ZC (2018) The mythos of model interpretability: in machine learning, the concept of interpretability
is both important and slippery. Queue 16(3):31–57
Li Z, Qin Y, Cheng X, et al (2024d) Ftmixer: Frequency and time domain representations fusion for time
series modeling. Preprint at arXiv:2405.15256
Liu Z, Zhu Z, Gao J et al (2021) Forecast methods for time series data: a survey. IEEE Access 9:91896–91912
Liu Y, Wu H, Wang J et al (2022) Non-stationary transformers: exploring the stationarity in time series fore-
casting. Adv Neural Inf Process Syst 35:9881–9893
Liu Z, Cheng M, Li Z, et al (2024e) Adaptive normalization for non-stationary time series forecasting: a
temporal slice perspective. Adv Neural Inform Process Syst 36
Liu Y, Hu T, Zhang H, et al (2024c) itransformer: Inverted transformers are effective for time series forecast-
ing. In: The Twelfth International Conference on Learning Representations, h t t p s : / / o pe n r e v i e w . n e t / f o r
u m ? i d = J e P f A I 8 f a h
Liu J, Liu C, Woo G, et al (2024b) Unitst: Effectively modeling inter-series and intra-series dependencies for
multivariate time series forecasting. Preprint at arXiv:2406.04975
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 89 of 95 216
Liu Y, Li C, Wang J, et al (2024d) Koopa: Learning non-stationary time series dynamics with Koopman
predictors. Adv Neural Inform Process Syst 36
Liu H, Li C, Wu Q, et al (2024a) Visual instruction tuning. Adv Neural Inform Process Syst 36
Liu S, Yu H, Liao C, et al (2021a) Pyraformer: Low-complexity pyramidal attention for long-range time
series modeling and forecasting. In: International conference on learning representations
Li Y, Xu J, Anastasiu D (2024c) Learning from polar representation: An extreme-adaptive model for long-
term time series forecasting. In: Proceedings of the AAAI Conference on Artificial Intelligence, pp
171–179
Li J, Xu X, Ding X, et al (2024a) Bayesian spatio-temporal graph convolutional network for railway train
delay prediction. IEEE Transactions on Intelligent Transportation Systems
Li Y, Yu R, Shahabi C, et al (2018) Diffusion convolutional recurrent neural network: Data-driven traffic
forecasting. In: International Conference on Learning Representations, h t t p s : / / o p e n r e v i e w . n e t / f o r u m ?
i d = S J i H X G W A Z
Lu Han DCZHan-Jia Ye (2024) The capacity and robustness trade-off: Revisiting the channel independent
strategy for multivariate time series forecasting. IEEE Transactions on Knowledge and Data Engineer-
ing pp 1–14
Lu J, Han X, Sun Y, et al (2024) Cats: Enhancing multivariate time series forecasting by constructing auxil-
iary time series as exogenous variables. Int Conf Mach Learn
Lundberg SM, Lee SI (2017) A unified approach to interpreting model predictions. In: Guyon I, Luxburg
UV, Bengio S, et al (eds) Advances in Neural Information Processing Systems, vol 30. Curran Associ-
ates, Inc., h t t p s : / / p r o c e e d i n g s . n e u r i p s . c c / p a p e r _ fi l e s / p a p e r / 2 0 1 7 / fi l e / 8 a 2 0 a 8 6 2 1 9 7 8 6 3 2 d 7 6 c 4 3 d f d 2 8 b 6
7 7 6 7 - P a p e r . p d f
Luo D, Wang X (2024) Moderntcn: A modern pure convolution structure for general time series analysis. In:
The Twelfth International Conference on Learning Representations
Ma Y, Guo Z, Ren Z, et al (2020) Streaming graph neural networks. In: Proceedings of the 43rd international
ACM SIGIR conference on research and development in information retrieval, pp 719–728
Makridakis S, Hibon M (2000) The M3-competition: results, conclusions and implications. Int J Forecast
16(4):451–476
Makridakis S, Andersen A, Carbone R et al (1982) The accuracy of extrapolation (time series) methods:
Results of a forecasting competition. J Forecast 1(2):111–153
Makridakis S, Spiliotis E, Assimakopoulos V (2020) The M4 competition: 100,000 time series and 61 fore-
casting methods. Int J Forecast 36(1):54–74
Ma X, Li X, Fang L, et al (2024) U-mixer: An unet-mixer architecture with stationarity correction for time
series forecasting. In: Proceedings of the AAAI Conference on Artificial Intelligence, pp 14255–14262
Marisca I, Alippi C, Bianchi FM (2024) Graph-based forecasting with missing data through spatiotemporal
downsampling
Masini RP, Medeiros MC, Mendes EF (2023) Machine learning advances for time series forecasting. J
Econom Surv 37(1):76–111
Massaoudi M, Refaat SS, Chihi I et al (2021) A novel stacked generalization ensemble-based hybrid LGBM-
XGB-MLP model for short-term load forecasting. Energy 214:118874
Matheson JE, Winkler RL (1976) Scoring rules for continuous probability distributions. Manage Sci
22(10):1087–1096
McCracken MW, Ng S (2016) FRED-MD: a monthly database for macroeconomic research. J Business
Econom Stat 34(4):574–589
McLeod A, Gweon H (2013) Optimal deseasonalization for monthly and daily geophysical time series. J
Environ Stat 4(11):1–11
Meijer C, Chen LY (2024) The rise of diffusion models in time-series forecasting. Preprint at arXiv:2401.03006
Mounir N, Ouadi H, Jrhilifa I (2023) Short-term electric load forecasting using an EMD-BI-LSTM approach
for smart grid energy management system. Energy Build 288:113022
Mu B, Jiang X, Yuan S et al (2023) Nao seasonal forecast using a multivariate air-sea coupled deep learning
model combined with causal discovery. Atmosphere 14(5):792
Nason GP, Von Sachs R, Kroisandt G (2000) Wavelet processes and adaptive estimation of the evolutionary
wavelet spectrum. J R Stat Soc 62(2):271–292
Nawrot P, Tworkowski S, Tyrolski M, et al (2021) Hierarchical transformers are more efficient language
models. Preprint at arXiv:2110.13711
Nie T, Mei Y, Qin G, et al (2024) Channel-aware low-rank adaptation in time series forecasting. Conference
on Information and Knowledge Management
Nie Y, Nguyen NH, Sinthong P, et al (2023) A time series is worth 64 words: Long-term forecasting with
transformers. In: The Eleventh International Conference on Learning Representations, h t t p s : / / o pe n r e v i
e w . n e t / f o r u m ? i d = J b d c 0 v T O c o l
1 3

216 Page 90 of 95 J. Kim et al.
Ni Z, Yu H, Liu S, et al (2024) Basisformer: Attention-based time series forecasting with learnable and inter-
pretable basis. Adv Neural Inform Process Syst 36
Nti IK, Teimeh M, Nyarko-Boateng O et al (2020) Electricity load forecasting: a systematic review. J Electric
Syst Inform Technol 7:1–19
Oord Avd, Li Y, Vinyals O (2018) Representation learning with contrastive predictive coding. Preprint at
arXiv:1807.03748
Oreshkin BN, Carpov D, Chapados N, et al (2020) N-beats: Neural basis expansion analysis for interpretable
time series forecasting. In: International Conference on Learning Representations, h t t p s : / / o p e n r e v i e w .
n e t / f o r u m ? i d = r 1 e c q n 4 Y w B
Pan SJ, Yang Q (2009) A survey on transfer learning. IEEE Trans Knowl Data Eng 22(10):1345–1359
Papapetrou P, Lee Z (2024) Interpretable and explainable time series mining. In: 2024 IEEE 11th Interna-
tional Conference on Data Science and Advanced Analytics (DSAA), IEEE, pp 1–3
Park C, Lee C, Bahng H, et al (2020) St-grat: A novel spatio-temporal graph attention networks for accurately
forecasting dynamically changing road speed. In: Proceedings of the 29th ACM international confer-
ence on information & knowledge management, pp 1215–1224
Passalis N, Tefas A, Kanniainen J et al (2019) Deep adaptive input normalization for time series forecasting.
IEEE Transact Neural Netw Learn Syst 31(9):3760–3765
Patro BN, Agneeswaran VS (2024a) Mamba-360: Survey of state space models as transformer alternative for
long sequence modelling: Methods, applications, and challenges. Preprint at arXiv:2404.16112
Patro BN, Agneeswaran VS (2024b) Simba: Simplified mamba-based architecture for vision and multivariate
time series. Preprint at arXiv:2403.15360
Patwardhan N, Marrone S, Sansone C (2023) Transformers in the real world: a survey on NLP applications.
Information 14(4):242
Pavlyshenko BM (2020) Using bayesian regression for stacking time series predictive models. In: 2020 IEEE
Third International Conference on Data Stream Mining & Processing (DSMP), pp 305–309, h t t p s : / / d o i
. o r g / 1 0 . 1 1 0 9 / D S M P 4 7 3 6 8 . 2 0 2 0 . 9 2 0 4 3 1 2
Pearl J (1995) Causal diagrams for empirical research. Biometrika 82(4):669–688
Pearl J (1998) Graphs, causality, and structural equation models. Sociol Methods Res 27(2):226–284
Pearl J et al (2000) Models, reasoning and inference, vol 19. Cambridge University Press, Cambridge, p 3
Peng Zj, Zhang C, Tian Yx (2023) Crude oil price time series forecasting: a novel approach based on varia-
tional mode decomposition, time-series imaging, and deep learning. IEEE Access
Petropoulos F, Hyndman RJ, Bergmeir C (2018) Exploring the sources of uncertainty: why does bagging for
time series forecasting work? Eur J Oper Res 268(2):545–554
Piao X, Chen Z, Murayama T, et al (2024) Fredformer: Frequency debiased transformer for time series fore-
casting. In: KDD, pp 2400–2410, https://doi.org/10.1145/3637528.3671928
Portet S (2020) A primer on model selection using the Akaike information criterion. Infectious Disease Mod-
elling 5:111–128
Qian J, Wang Q, Wu Y, et al (2023) Causality-based deep learning forecast of the Kuroshio volume transport
in the east china sea. Earth Space Sci 10(2):e2022EA002722
Qin Y, Song D, Chen H, et al (2017) A dual-stage attention-based recurrent neural network for time series pre-
diction. In: Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence,
IJCAI-17, pp 2627–2633, https://doi.org/10.24963/ijcai.2017/366
Qi S, Wen L, Li Y, et al (2024) Enhancing multivariate time series forecasting with mutual information-
driven cross-variable and temporal modeling. Preprint at arXiv:2403.00869
Quinlan JR (1986) Induction of decision trees. Mach learning 1:81–106
Radford A, Kim JW, Hallacy C, et al (2021) Learning transferable visual models from natural language
supervision. In: International conference on machine learning, PMLR, pp 8748–8763
Ramesh A, Dhariwal P, Nichol A, et al (2022) Hierarchical text-conditional image generation with clip latent.
Preprint at arXiv:2204.06125 1(2):3
Rasul K, Ashok A, Williams AR, et al (2024) Lag-llama: Towards foundation models for probabilistic time
series forecasting. Preprint at arXiv:2310.08278
Rasul K, Seward C, Schuster I, et al (2021) Autoregressive denoising diffusion models for multivariate
probabilistic time series forecasting. In: International Conference on Machine Learning, PMLR, pp
8857–8868
Ribeiro MT, Singh S, Guestrin C (2016) " why should i trust you?" explaining the predictions of any classi-
fier. In: Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and
data mining, pp 1135–1144
Rombach R, Blattmann A, Lorenz D, et al (2022) High-resolution image synthesis with latent diffusion
models. In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp
10684–10695
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 91 of 95 216
Rosenbaum PR, Rubin DB (1983) The central role of the propensity score in observational studies for causal
effects. Biometrika 70(1):41–55
Rossi E, Chamberlain B, Frasca F, et al (2020) Temporal graph networks for deep learning on dynamic
graphs. In: ICML 2020 Workshop on Graph Representation Learning
Rumelhart DE, Hinton GE, Williams RJ (1986) Learning representations by back-propagating errors. Nature
323(6088):533–536
Runge J, Nowack P, Kretschmer M, et al (2019) Detecting and quantifying causal associations in large non-
linear time series datasets. Sci Adv 5(11):eaau4996
Saharia C, Chan W, Saxena S et al (2022) Photorealistic text-to-image diffusion models with deep language
understanding. Adv Neural Inf Process Syst 35:36479–36494
ŞAHiN E, Arslan NN, Özdemir D (2024) Unlocking the black box: an in-depth review on interpretability,
explainability, and reliability in deep learning. Neural Computing and Applications pp 1–107
Sankaranarayanan S, Balaji Y, Castillo CD, et al (2018) Generate to adapt: Aligning domains using gen-
erative adversarial networks. In: Proceedings of the IEEE conference on computer vision and pattern
recognition, pp 8503–8512
Scarselli F, Gori M, Tsoi AC et al (2008) The graph neural network model. IEEE Trans Neural Networks
20(1):61–80
Schölkopf B, Locatello F, Bauer S et al (2021) Toward causal representation learning. Proc IEEE
109(5):612–634
Shabani MA, Abdi AH, Meng L, et al (2023) Scaleformer: Iterative multi-scale refining transformers for time
series forecasting. In: The Eleventh International Conference on Learning Representations, h t t p s : / / o pe
n r e v i e w . n e t / f o r u m ? i d = s C r n l l C t j o E
Shafer G (1976) A Mathematical Theory of Evidence. Princeton University Press, Princeton
Sharma N, Mangla M, Mohanty SN et al (2021) Employing stacked ensemble approach for time series fore-
casting. Int J Inf Technol 13:2075–2080
Sharma K, Dwivedi YK, Metri B (2022) Incorporating causality in energy consumption forecasting using
deep neural networks. Annals of Operations Research pp 1–36
Shen L, Chen W, Kwok J (2024) Multi-resolution diffusion models for time series forecasting. In: The
Twelfth International Conference on Learning Representations
Shen L, Kwok J (2023) Non-autoregressive conditional diffusion models for time series prediction. In: Inter-
national Conference on Machine Learning, PMLR, pp 31016–31029
Shi X, Chen Z, Wang H, et al (2015) Convolutional LSTM network: a machine learning approach for precipi-
tation nowcasting. Adv Neural Inform Process Syst 28
Shih SY, Sun FK, Hy Lee (2019) Temporal pattern attention for multivariate time series forecasting. Mach
Learn 108:1421–1441
Shu Y, Lampos V (2024) Deformtime: Capturing variable dependencies with deformable attention for time
series forecasting. Preprint at arXiv:2406.07438
Smyl S (2020) A hybrid method of exponential smoothing and recurrent neural networks for time series
forecasting. Int J Forecast 36(1):75–85
Smyl S, Oreshkin BN, Pełka P, et al (2024) Any-quantile probabilistic forecasting of short-term electricity
demand. Preprint at arXiv:2404.17451
Sohl-Dickstein J, Weiss E, Maheswaranathan N, et al (2015) Deep unsupervised learning using nonequilib-
rium thermodynamics. In: International conference on machine learning, PMLR, pp 2256–2265
Song Y, Ermon S (2019) Generative modeling by estimating gradients of the data distribution. Adv Neural
Inform Process Syst 32
Song C, Lin Y, Guo S, et al (2020) Spatial-temporal synchronous graph convolutional networks: A new
framework for spatial-temporal network data forecasting. In: Proceedings of the AAAI conference on
artificial intelligence, pp 914–921
Song Y, Sohl-Dickstein J, Kingma DP, et al (2021) Score-based generative modeling through stochastic dif-
ferential equations. In: International Conference on Learning Representations, h t t p s : / / o pe n r e v i e w . n e t / f
o r u m ? i d = P x T I G 1 2 R R H S
Soyiri IN, Reidpath DD (2013) An overview of health forecasting. Environ Health Prev Med 18:1–9
Sparks AH, Carroll J, Goldie J, et al (2020) Bomrang: Australian government bureau of meteorology (BOM)
data client. R package version 07.0 https://CRAN.R-project.org/package=bomrang
Srivastava N, Hinton G, Krizhevsky A et al (2014) Dropout: a simple way to prevent neural networks from
overfitting. J Mach Learn Res 15(1):1929–1958
Štěpnička M, Burda M (2017) On the results and observations of the time series forecasting competition cif
2016. In: 2017 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), IEEE, pp 1–6
1 3

216 Page 92 of 95 J. Kim et al.
Sui M, Zhang C, Zhou L et al (2024) An ensemble approach to stock price prediction using deep learning and
time series models. 2024 IEEE 6th International Conference on Power. IEEE, Intelligent Computing
and Systems (ICPICS), pp 793–797
Sun F, Hao W, Zou A, et al (2024a) A survey on spatio-temporal series prediction with deep learning: tax-
onomy, applications, and future directions. Neural Computing and Applications pp 1–25
Sun Y, Xie Z, Chen D, et al (2024b) Hierarchical classification auxiliary network for time series forecasting.
Preprint at arXiv:2405.18975
Taieb SB, Bontempi G, Atiya AF et al (2012) A review and comparison of strategies for multi-step ahead
time series forecasting based on the NN5 forecasting competition. Expert Syst Appl 39(8):7067–7083
Tang P, Zhang W (2024) PDMLP: Patch-based decomposed MLP for long-term time series forecastin. Pre-
print at arXiv:2405.13575
Tashiro Y, Song J, Song Y et al (2021) CSDI: Conditional score-based diffusion models for probabilistic time
series imputation. Adv Neural Inf Process Syst 34:24804–24816
Tay Y, Dehghani M, Bahri D, et al (2020) Efficient transformers: a survey. ACM Comput Surv 55:1–28. h t t p
s : / / a p i . s e m a n t i c s c h o l a r . o r g / C o r p u s I D : 2 2 1 7 0 2 8 5 8
Thompson PA (1990) An MSE statistic for comparing forecast accuracy across series. Int J Forecast
6(2):219–227
Touvron H, Martin L, Stone K, et al (2023) LLAMA 2: Open foundation and fine-tuned chat models. Preprint
at arXiv:2307.09288
Truchan H, Kalfar C, Ahmadi Z (2024) LTBOOST: Boosted hybrids of ensemble linear and gradient algo-
rithms for the long-term time series forecasting. In: Proceedings of the 33rd ACM International Confer-
ence on Information and Knowledge Management, pp 2271–2281
Ulyanov D, Vedaldi A, Lempitsky V (2016) Instance normalization: The missing ingredient for fast styliza-
tion. Preprint at arXiv:1607.08022
Van Den Oord A, Dieleman S, Zen H, et al (2016) Wavenet: a generative model for raw audio. Preprint at
arXiv:1609.03499 12
Vapnik V, Golowich S, Smola A (1996) Support vector method for function approximation, regression esti-
mation and signal processing. Adv Neural Inform Process Syst 9
Vaswani A, Shazeer N, Parmar N, et al (2017) Attention is all you need. Adv Neural Inform Process Syst 30
Veličković P, Cucurull G, Casanova A, et al (2018) Graph attention networks. In: International Conference on
Learning Representations, https://openreview.net/forum?id=rJXMpikCZ
Wachter S, Mittelstadt B, Russell C (2017) Counterfactual explanations without opening the black box:
Automated decisions and the GDPR. Harv JL Tech 31:841
Wang W, Li H, Ding Z et al (2023) Rethinking maximum mean discrepancy for visual domain adaptation.
IEEE Transact Neural Netw Learn Syst 34(1):264–277. https://doi.org/10.1109/TNNLS.2021.3093468
Wang Z, Ruan S, Huang T et al (2024) A lightweight multi-layer perceptron for efficient multivariate time
series forecasting. Knowl-Based Syst 288:111463
Wang L, Adiga A, Chen J, et al (2022b) Causalgnn: Causal-based graph neural networks for spatio-temporal
epidemic forecasting. In: Proceedings of the AAAI conference on artificial intelligence, pp 12191–12199
Wang J, Jatowt A, Yoshikawa M (2022a) Timebert: Extending pre-trained language representations with
temporal information. Preprint at arXiv:2204.13032
Wang Z, Kong F, Feng S, et al (2024d) Is mamba effective for time series forecasting? Preprint at
arXiv:2403.11144
Wang Z, Miliou I, Samsten I, et al (2023b) Counterfactual explanations for time series forecasting. In: 2023
IEEE International Conference on Data Mining (ICDM), IEEE, pp 1391–1396
Wang Y, Wu H, Dong J, et al (2024c) Timexer: Empowering transformers for time series forecasting with
exogenous variables. In: The Thirty-eighth Annual Conference on Neural Information Processing Sys-
tems, https://openreview.net/forum?id=INAeUQ04lT
Wang S, Wu H, Shi X, et al (2024a) Timemixer: Decomposable multiscale mixing for time series forecasting.
International Conference on Learning Representations
Wang X, Zhou T, Wen Q, et al (2024b) Card: Channel aligned robust blend transformer for time series fore-
casting. In: The Twelfth International Conference on Learning Representations
Wei C, Niu C, Tang Y et al (2022) NPENAS: Neural predictor guided evolution for neural architecture
search. IEEE Transact Neural Netw Learn Syst 34(11):8441–8455
Wen R, Torkkola K, Narayanaswamy B, et al (2017) A multi-horizon quantile recurrent forecaster. Preprint
at arXiv:1711.11053
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 93 of 95 216
Wen Q, Zhou T, Zhang C, et al (2023) Transformers in time series: A survey. In: Elkind E (ed) Proceedings
of the Thirty-Second International Joint Conference on Artificial Intelligence, IJCAI-23. International
Joint Conferences on Artificial Intelligence Organization, pp 6778–6786, h t t p s : / / d o i . o r g / 1 0 . 2 4 9 6 3 / i j c a
i . 2 0 2 3 / 7 5 9 , (survey Track)
Winters PR (1960) Forecasting sales by exponentially weighted moving averages. Manage Sci 6(3):324–342
Wolpert DH (1992) Stacked generalization. Neural Netw 5(2):241–259
Wong SC, Gatt A, Stamatescu V, et al (2016) Understanding data augmentation for classification: when
to warp? In: 2016 international conference on digital image computing: techniques and applications
(DICTA), IEEE, pp 1–6
Woo G, Liu C, Kumar A, et al (2024) Unified training of universal time series forecasting transformers. In:
Forty-first International Conference on Machine Learning
Wu Z, Huang NE (2009) Ensemble empirical mode decomposition: a noise-assisted data analysis method.
Adv Adapt Data Anal 1(01):1–41
Wu B, Wang L (2024) Two-stage decomposition and temporal fusion transformers for interpretable wind
speed forecasting. Energy 288:129728
Wu H, Xu J, Wang J et al (2021) Autoformer: Decomposition transformers with auto-correlation for long-
term series forecasting. Adv Neural Inf Process Syst 34:22419–22430
Wu B, Yu S, Peng L et al (2024) Interpretable wind speed forecasting with meteorological feature exploring
and two-stage decomposition. Energy 294:130782
Wu Z, Gong Y, Zhang A (2024b) Dtmamba: Dual twin mamba for time series forecasting. Preprint at
arXiv:2405.07022
Wu H, Hu T, Liu Y, et al (2023) Timesnet: Temporal 2d-variation modeling for general time series analysis.
International Conference on Learning Representations
Xiong Q, Tang K, Ma M, et al (2024) Tdt loss takes it all: Integrating temporal dependencies among targets
into non-autoregressive time series forecasting. Preprint at arXiv:2406.04777
Xu B, Sheng Y, Li P et al (2019) Causes and classification of EMD mode mixing. Vibroengineering Procedia
22:158–164
Xua B, Yang G (2024) Interpretability research of deep learning: a literature survey. Information Fusion p
102721
Xu Z, Bian Y, Zhong J, et al (2024b) Beyond trend and periodicity: Guiding time series forecasting with
textual cues. Preprint at arXiv:2405.13522
Xu X, Chen Z, Xu D, et al (2022) Mixing signals: Data augmentation approach for deep learning based
modulation recognition. Preprint at arXiv:2204.03737
Xue H, Salim FD (2023) Promptcast: a new prompt-based learning paradigm for time series forecasting.
IEEE Transactions on Knowledge and Data Engineering
Xu X, Liang Y, Huang B, et al (2024a) Integrating mamba and transformer for long-short range time series
forecasting. Preprint at arXiv:2404.14757
Xu Z, Zeng A, Xu Q (2024) Fits: Modeling time series with [CDATA[10 k ]]10k parameters
Yang Y, Yang Y (2020) Hybrid method for short-term time series forecasting based on EEMD. IEEE Access
8:61915–61928
Yang Y, Jin M, Wen H, et al (2024a) A survey on diffusion models for time series and Spatio-temporal data.
Preprint at arXiv:2404.18886
Yang F, Li X, Wang M, et al (2023a) Waveform: Graph enhanced wavelet learning for long sequence fore-
casting of multivariate time series. In: Proceedings of the AAAI Conference on Artificial Intelligence,
pp 10754–10761
Yan T, Gong H, Yongping H, et al (2024) Probabilistic time series modeling with decomposable denoising
diffusion model. In: Salakhutdinov R, Kolter Z, Heller K, et al (eds) Proceedings of the 41st Interna-
tional Conference on Machine Learning, Proceedings of Machine Learning Research, vol 235. PMLR,
pp 55759–55777, h t t p s : / / p r o c e e d i n g s . m l r . p r e s s / v 2 3 5 / y a n 2 4 b . h t m l
Yang M, Xu C, Bai Y, et al (2023b) Investigating black-box model for wind power forecasting using local
interpretable model-agnostic explanations algorithm: why should a model be trusted? CSEE J Power
Energy Syst
Yang Y, Zhu Q, Chen J (2024b) Vcformer: Variable correlation transformer with inherent lagged correlation
for multivariate time series forecasting. In: Larson K (ed) Proceedings of the Thirty-Third International
Joint Conference on Artificial Intelligence, IJCAI-24. International Joint Conferences on Artificial Intel-
ligence Organization, pp 5335–5343, https://doi.org/10.24963/ijcai.2024/590, (Main Track)
Yan S, Xiong Y, Lin D (2018) Spatial temporal graph convolutional networks for skeleton-based action rec-
ognition. In: Proceedings of the AAAI conference on artificial intelligence
1 3

216 Page 94 of 95 J. Kim et al.
Yan T, Zhang H, Zhou T, et al (2021) Scoregrad: Multivariate probabilistic time series forecasting with con-
tinuous energy-based generative models. Preprint at arXiv:2106.10121
Ye J, Zhang W, Yi K, et al (2024) A survey of time series foundation models: Generalizing time series repre-
sentation with large language mode. Preprint at arXiv:2405.02358
Yi K, Zhang Q, Fan W, et al (2024) Frequency-domain mlps are more effective learners in time series fore-
casting. Adv Neural Inform Process Syst 36
Yuan X, Qiao Y (2024) Diffusion-TS: Interpretable diffusion for general time series generation. In: The Twelfth
International Conference on Learning Representations, https://openreview.net/forum?id=4h1apFjO99
Yu C, Wang F, Shao Z, et al (2023) Dsformer: A double sampling transformer for multivariate time series
long-term prediction. In: Proceedings of the 32nd ACM international conference on information and
knowledge management, pp 3062–3072
Yu G, Zou J, Hu X, et al (2024) Revitalizing multivariate time series forecasting: Learnable decomposition
with inter-series dependencies and intra-series variations modeling. Int Conf Mach Learn
Zeng A, Chen M, Zhang L, et al (2023) Are transformers effective for time series forecasting? In: Proceedings
of the AAAI conference on artificial intelligence, pp 11121–11128
Zeng C, Liu Z, Zheng G, et al (2024) C-mamba: Channel correlation enhanced state space models for multi-
variate time series forecasting. Preprint at arXiv:2406.05316
Zhang S, Chen Y, Xiao J et al (2021) Hybrid wind speed forecasting model based on multivariate data sec-
ondary decomposition approach and deep learning algorithm with attention mechanism. Renew Energy
174:688–704
Zhang S, Chen Y, Zhang W et al (2021) A novel ensemble deep learning model with dynamic error correction
and multi-objective ensemble pruning for time series forecasting. Inf Sci 544:427–445
Zhang Q, Chang J, Meng G, et al (2020) Spatio-temporal graph structure learning for traffic forecasting. In:
Proceedings of the AAAI conference on artificial intelligence, pp 1177–1185
Zhang X, Chowdhury RR, Gupta RK, et al (2024d) Large language models for time series: A survey. In:
Larson K (ed) Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence,
IJCAI-24. International Joint Conferences on Artificial Intelligence Organization, pp 8335–8343,
https://doi.org/10.24963/ijcai.2024/921, (Survey Track)
Zhang Y, Ma L, Pal S, et al (2024e) Multi-resolution time-series transformer for long-term forecasting. In:
International Conference on Artificial Intelligence and Statistics, PMLR, pp 4222–4230
Zhang M, Sun Y, Liang F (2024c) Sparse deep learning for time series data: theory and applications. Adv
Neural Inform Process Syst 36
Zhang D, Wang Y (2024) Adaptive extraction network for multivariate long sequence time-series forecasting.
Preprint at arXiv:2405.12038
Zhang K, Wen Q, Zhang C, et al (2024a) Self-supervised learning for time series analysis: Taxonomy, prog-
ress, and prospects. IEEE Transactions on Pattern Analysis and Machine Intelligence
Zhang Y, Yan J (2023) Crossformer: Transformer utilizing cross-dimension dependency for multivariate time
series forecasting. In: The eleventh international conference on learning representations
Zhang J, Zheng Y, Qi D (2017) Deep spatio-temporal residual networks for citywide crowd flows prediction.
In: Proceedings of the AAAI conference on artificial intelligence
Zhang K, Zou X, Tang Y (2024b) Caformer: Rethinking time series analysis from causal perspective. Preprint
at arXiv:2403.08572
Zhan T, He Y, Li Z, et al (2024) Time evidence fusion network: Multi-source view in long-term time series
forecasting. Preprint at arXiv:2405.06419
Zhao S, Ma T, Ermon S (2020) Individual calibration with randomized forecasting. In: International Confer-
ence on Machine Learning, PMLR, pp 11387–11397
Zheng C, Fan X, Wang C, et al (2020) Gman: A graph multi-attention network for traffic prediction. In: Pro-
ceedings of the AAAI conference on artificial intelligence, pp 1234–1241
Zhou T, Ma Z, Wen Q, et al (2022) Fedformer: Frequency enhanced decomposed transformer for long-term
series forecasting. In: International conference on machine learning, PMLR, pp 27268–27286
Zhou T, Niu P, Wang X, et al (2023) One fits all: Power general time series analysis by pretrained LM. In:
Thirty-seventh Conference on Neural Information Processing Systems, h t t p s : / / o p e n r e v i e w . n e t / f o r u m ?
i d = g M S 6 F V Z v m F
Zhou H, Zhang S, Peng J, et al (2021) Informer: Beyond efficient transformer for long sequence time-series
forecasting. In: Proceedings of the AAAI conference on artificial intelligence, pp 11106–11115
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
1 3

A comprehensive survey of deep learning for time series forecasting:… Page 95 of 95 216
Authors and Affiliations
Jongseon Kim1,4 · Hyungjoon Kim1,5 · HyunGi Kim2 · Dongjun Lee1 · Sungroh Yoon1,2,3
Sungroh Yoon
sryoon@snu.ac.kr
Jongseon Kim
hallooawooye@snu.ac.kr
Hyungjoon Kim
khjn81@snu.ac.kr
HyunGi Kim
rlagusrl0128@snu.ac.kr
Dongjun Lee
elite1717@snu.ac.kr
1 Interdisciplinary Program in Artificial Intelligence, Seoul National University, Seoul, South
Korea
2 Department of Electrical and Computer Engineering, Seoul National University, Seoul, South
Korea
3 AIIS, ASRI, and INMC, Seoul National University, Seoul, South Korea
4 R&D Department, LG Chem, Seoul, South Korea
5 R&D Department, Samsung SDI, Yongin, South Korea
1 3