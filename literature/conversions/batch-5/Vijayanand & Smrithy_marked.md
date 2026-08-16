---
conversion_metadata:
  converted_at: "2026-07-21T09:12:13Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Vijayanand & Smrithy.pdf"
  source_pdf_sha256: "afce7b3295139fc88d97139da884f203daa4ebfd17c192aec06e533fcbcecf27"
  page_count: 16
  markdown_char_count: 112252
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Research Article

Explainable AI - enhanced ensemble
learning for ﬁnancial fraud detection in
mobile money transactions

Intelligent Decision Technologies
2025, Vol. 19(1) 52–67
© The Author(s) 2024
Article reuse guidelines:
sagepub.com/journals-permissions
DOI: 10.1177/18724981241289751
journals.sagepub.com/home/idt

Deepshika Vijayanand and Girijakumari Sreekantan Smrithy

Abstract
This research paper addresses the pressing problem of ﬁnancial fraud in the changing context of digital banking by inte-
grating machine learning and explainable AI, speciﬁcally exploiting SHapley Additive exPlanations (SHAP). With a focus
on enhancing both accuracy and interpretability, this study utilizes a synthetically generated dataset from the PaySim
simulator, encompassing 6,362,620 records. The usefulness of an Ensemble Learning Model with a Voting Classiﬁer is
shown by its evaluation of different machine learning models, which achieves an excellent accuracy of 99.904%.Empha-
sizing transparency, accountability, and regulatory compliance, this work employs SHAP analysis to unveil attribute-level
interpretability, providing stakeholders with clear insights. The goal of this interdisciplinary endeavor is to provide a safe
space for digital ﬁnance by bridging the gap between precision and interpretability, which will aid in the creation of open
methods.

Keywords
Ensemble learning, explainable AI, feature importance, ﬁnancial fraud, interpretability, machine learning, mobile money,
SHAP analysis, transparency

Received: 15 April 2024; accepted: 17 September 2024

1 Introduction

In today’s digitally-dominated world, the simplicity and efﬁcacy of banking have changed due to the advancement of
ﬁnancial technology, bringing in a new era of previously unimaginable opportunities. Though there are many challenges
associated with this increase in digital ﬁnancial interactions, the growing threat of ﬁnancial fraud is one of the most critical
ones. There is an immediate a need reliable systems that can identify and stop fraudulent actions as they happen, as the
Association of Certiﬁed Fraud Examiners (ACFE) reports that worldwide fraud losses have reached a concerning 5% of
yearly income.1

The sheer volume of global digital payment transactions, projected to reach US$16.62tn by 2028 (Statista), underlines
the growing reliance on digital ﬁnancial interactions.2 Nevertheless, with this digital transformation comes an alarming
increase in the cost of cybercrime, projected to reach US$10.5 Trillion annually by 2025.3 The sophistication of modern
fraud schemes, leveraging advanced techniques such as machine learning to evade detection,4 poses not only a severe
ﬁnancial risk but also jeopardizes the trust that underpins the entire ﬁnancial ecosystem.

Financial institutions face a multifaceted challenge, with an estimated $4.23 loss for every dollar lost to fraud in 2022,5
considering both the immediate ﬁnancial impact and the long-term consequences. Regulation compliance, driven by the
GDPR and PSD2, necessitates accountability as well as transparency in processing of data and decisions. In response to this
evolving landscape, the adoption of machine learning in ﬁnancial services is growing, with 70% of ﬁnancial institutions
reporting its use for fraud detection as of 2020.6

School of Computer Science and Engineering, Vellore Institute of Technology, Chennai, India

Corresponding author:
Girijakumari Sreekantan Smrithy, School of Computer Science and Engineering, Vellore Institute of Technology, Chennai, Tamil Nadu, 600127, India.
Email: smrithy.gs@vit.ac.in

---

<!-- PAGE 2 -->

Vijayanand and Smrithy

53

Traditional machine learning models frequently function as opaque, or “black-box,” entities, making it challenging for
stakeholders to understand the logic underlying the models forecasts. Not only does a lack of transparency undermine
trust, but it also creates regulatory problems in sectors where explainability is essential. According to data scientists,
machine learning models can not be understood or trusted unless they are interpretable.7 Combining machine learning
with explainable AI is the focus of this study since it offers a solution to the problems of accuracy and interpretability in
ﬁnancial fraud detection systems.

Explainable AI becomes crucial for demystifying machine learning models’ decision-making processes, especially
with SHAP (SHapley Additive exPlanations). Explainable AI is essential for fostering trust in ﬁnancial institutions and
guaranteeing accountability in algorithmic decision-making, and its necessity extends beyond compliance. This research
combines the power of explainable AI with ensemble machine learning to create ﬁnancial fraud detection models that
perform well in accuracy and offer stakeholders interpretable insights. The ultimate objectives are to strengthen the barrier
against ﬁnancial fraud, promote trust in ﬁnancial institutions, and create a safe environment for digital ﬁnance.

2 Literature survey

The need for robust systems to detect and prevent fraudulent activities has become paramount, leading to a shift from
traditional approaches to more adaptive and intelligent solutions. Ali et al.8 reviewed ML applications in detecting
ﬁnancial fraud, emphasizing the limitations of traditional methods and highlighting SVM and ANN as key algorithms.
It addresses issues and gaps, suggesting exploration of ensemble methods and unsupervised learning like clustering.
Enhanced anomaly detection and incorporation of text-mining techniques such as Word2Vec, Doc2Vec, or BERT are
recommended for improved ML models in combating ﬁnancial fraud, providing a comprehensive overview and insights
for potential advancements. In their extensive review of 75 publications spanning 2009–2019, Al-Hashedi et al.9 classiﬁed
ﬁnancial fraud as follows: bank fraud, insurance fraud, ﬁnancial statement fraud, and cryptocurrency fraud. Of the 34
data mining methods that are included, SVM is the most popular, accounting for 23 percent of all uses. Naïve Bayes and
Random Forest follow closely behind (15 percent each). The majority of studies (81.33%) focus on bank and insurance
fraud, offering valuable insights for academia and industry. The review contributes signiﬁcant information to the ﬁeld by
expanding the sample and summarizing notable works. Wickramanayake et al.10 address card payment fraud, a signiﬁcant
challenge in the global digital economy. Using a taxonomy derived from studies conducted between 2009 and 2020,11 it
investigates fraud detection technologies that make use of data mining and machine learning advancements. Reviewing
45 papers, the survey highlights strategies that take into account how fraud affects businesses, use feature engineering to
proﬁle cardholders, and adjust to changing fraud trends. The paper concludes with a comparative evaluation of classiﬁca-
tion algorithms, aiming to provide a comprehensive overview for academia and commercial developers tackling payment
fraud detection.

A study conducted by Liu et al.12 focuses on creating a stable and interpretable model for ﬁnancial fraud detection,
particularly for imbalanced datasets. It identiﬁes Smote as the most effective oversampling algorithm and highlights Adap-
tive Lasso as the top performer for feature selection. LightGBM outperforms XGBoost and Random Forest in feature
importance ranking. The study emphasizes the signiﬁcance of NULL NUM in identifying fraudulent corporate data and
recommends incorporating WoE encoding and IV value testing for improved model performance. In conclusion, the paper
suggests future research directions, including larger sample sizes, exploration of deep learning, and integration of natural
language processing technologies for enhanced ﬁnancial statement fraud detection. Anomaly detection methods for ﬁnan-
cial fraud are reviewed by Hilal et al.,13 with an emphasis on how technologically driven fraud has led to recent advances
in unsupervised and semi-supervised learning. Issues with money laundering, insurance fraud, and credit card fraud are
addressed, with a focus on the transition from supervised to unsupervised and semi-supervised methods.11 Generative
models like GANs and AEs are highlighted for effective feature extraction, while deep learning architectures like CNNs
and LSTMs capture temporal relations. The paper suggests future research directions, advocating for combined models
and emphasizing interpretability in fraud detection.

Mittal S. & Tyagi S.14 examine security concerns in online credit card usage within the evolving e-commerce landscape
over the past 25 years. Credit card fraud may be difﬁcult to detect in real time, and skewed datasets are just two of the
problems highlighted in this analysis of attack routes and solutions.15 The review underscores the recent surge in credit card
transactions and subsequent fraud, leading to the development of machine learning-based models. Some of the problems
that have been identiﬁed include a lack of standard algorithms and a lack of understanding of credit card processing.11
Furthermore, the article stresses the importance of benchmark datasets and investigates the unrealized possibilities of big
data analytics and streaming data in relation to future advancements in fraud detection.15

Sadgali I. et al.16 evaluate machine learning techniques, emphasizing hybrid methods, for detecting various ﬁnancial
fraud types, including credit card fraud. In order to solve imbalanced datasets and increase accuracy in credit card fraud

---

<!-- PAGE 3 -->

54

Intelligent Decision Technologies 19(1)

detection, the conclusion calls for improved algorithms and hybrid models. The ﬁndings emphasize the effectiveness of
Support Vector Machines (SVMs) in instantaneous transactional fraud detection.16 In response to the growing problem
of ﬁnancial fraud in online services, Alghofaili Y. et al.17 provide a fresh strategy based on deep learning’s Long Short-
Term Memory (LSTM) for better detection. In less than a minute, the LSTM based model achieves 99.95% accuracy on
a genuine credit card fraud dataset, outperforming previous techniques and demonstrating its potential to advance fraud
detection for huge datasets and real-time processing demands.17

The study by Alarfaj F. K. et al.18 addresses credit card fraud detection challenges, proposing enhanced deep learning
algorithms. By improving its performance on the European card benchmark dataset, the model outperforms previous
techniques, earning a f1-score of 85.71 percent, a precision of 93.1 percent, and an area under the curve (AUC) of 98.0
percent.18 These ﬁndings demonstrate the promise of highly developed algorithms for the accurate identiﬁcation of credit
card fraud in the real world.18 For the purpose of detecting credit card fraud, Ileberi E. et al.19 use AdaBoost in conjunction
with a number of machine learning methods, such as Decision Trees, Random Forest, Extra Trees, XGBoost, Logistic
Regression, and Support Vector Machine.ET-AdaBoost achieves 99.98% accuracy and an MCC of 0.99 in the comparison
study conducted on the European fraudulent transactions with credit cards dataset, demonstrating exceptional levels of
accuracy.19 The suggested machine learning techniques utilizing AdaBoost demonstrate exceptional results when tested
on a biased artiﬁcial credit card fraud dataset.19 By combining an ensemble classiﬁer with an LSTM base learner in
AdaBoost and making use of SMOTE-ENN for hybrid resampling, Esenogho E. et al.20 presented a successful approach
to detecting credit card fraud. The suggested method outperforms other algorithms, achieving high speciﬁcity (0.998) and
sensitivity (0.996), indicating its potential to improve credit card fraud detection.20 The increased difﬁculty of credit card
fraud during the COVID-19 pandemic’s spike in online purchases was discussed by Alfaiz N. S., & Fati S. M..21 The
AllKNN-CatBoost model outperformed sixty-six other ML models on a real-world dataset, with an AUC of 97.94%, a
recall of 95.91%, and an F1-Score of 87.30%.21 The results emphasize its potential signiﬁcance in preventing fraudulent
credit card transactions during online activities, outperforming previous approaches.

Awosika T. et al.22 introduced a novel approach to address fraudulent transactions in the ﬁnancial sector, combining
Explainable AI (XAI) and Federated Learning (FL) to enhance transparency and interpretability in fraud detection sys-
tems. The integration of SHAP ensures accurate and understandable predictions, shedding light on inﬂuential features
and justifying decisions. This emphasis on transparency becomes crucial in sensitive domains, emphasizing that XAI is
essential for accountability, user trust, and regulatory compliance in FL-based fraud detection systems. Table 1 shows the
comparative analysis of various research works on ﬁnancial fraud detection using machine learning algorithms and deep
learning algorithms.

It is evident from the in-depth review of numerous sources on ﬁnancial fraud detection that machine learning (ML)
approaches are essential for tackling the difﬁculties associated with ﬁnancial fraud detection. SVMs, Decision Trees, Ran-
dom Forest, ANNs, and deep learning models such as LSTM are highly favored for their exceptional accuracy, according
to the reviewed literature.23,24 The emphasis on ensemble methods, data resampling techniques, and feature engineer-
ing highlights the ongoing pursuit of reﬁning existing models. Additionally, the incorporation of advanced technologies,
such as Generative Adversarial Networks (GANs) signals a growing awareness of the need for interpretability and trans-
parency in fraud detection systems. While the ﬁeld has made substantial progress, the papers collectively advocate for
future research directions, including exploration into less-studied algorithms, text-mining techniques, natural language
processing, and the integration of novel approaches like federated learning and Explainable AI (XAI). The continuous
evolution of ﬁnancial fraud detection methodologies remains critical to staying ahead of sophisticated fraudulent activities
and safeguarding ﬁnancial systems.

3 Proposed methodology

When someone “intentionally and knowingly deceives the victim by misrepresenting, concealing, or omitting facts about
promised goods, services, or other beneﬁts and consequences that are nonexistent, unnecessary, never intended to be
provided, or deliberately distorted for the purpose of monetary gain,” they are committing actions of ﬁnancial fraud.25
Financial fraud in mobile money transfers is the focus of this research work. Mobile money refers to monetary services
and transactions that may be carried out via a mobile device, such a phone or tablet.26 Connectivity to a bank account is
not always an option for these services.26

This research focuses on enhancing fraud prevention systems by not only prioritizing model accuracy but also empha-
sizing explainability through SHAP analysis as illustrated in Figure 1. The study’s overarching goal is to provide more
open and understandable methodology by deconstructing machine learning models, with a focus on their use in ﬁnan-
cial fraud scenarios. An ever-changing cybersecurity environment is being tackled by combining machine learning with

---

<!-- PAGE 4 -->

Vijayanand and Smrithy

55

p
e
e
d

f

o

e
s
u

e
k
a
m

l

d
u
o
h
s

e
r
u
t
u

f

e
h
t

n

i

h
c
r
a
e
s
e
R

l
a
r
u
t
a
n

i

,
g
n
n
r
a
e

l

l

.
s
e
p
m
a
s

r
e
t
a
e
r
g

d
n
a

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
g
a
u
g
n
a
l

d
n
a

s

m
h
t
i
r
o
g
l
a

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

f

o

n
o
i
t
a
r
o
p
x
E

l

d
e
c
n
a
h
n
e

g
n
i
s
s
e
r
d
d
a

d
e
c
n
a
l
a
b
m

i

d
n
a

s
t
e
s
a
t
a
d

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
m

i
t
-
l
a
e
r

o
t

i

s
e
u
q
n
h
c
e
t

i

g
n
c
n
a
l
a
b

a
t
a
D

t
i
d
e
r
c

n

i

s
e
v
i
t
a
g
e
n

d
u
a
r
f

d
r
a
c

n
o
i
t
c
e
t
e
d

e
s
l
a
f

e
z
i
m
n
m

i

i

L
L
U
N

f

o
e
c
n
a
t
r
o
p
m

i

e
t
a
r
o
p
r
o
c

l

t
n
e
u
d
u
a
r
f

s
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
a
t
a
d

e
r
u
t
a
e
f

g
n
i
t
a
r
g
e
t
n

i

g
n
i
r
e
e
n
i
g
n
e

i

s
e
u
q
n
h
c
e
t

i

g
n
y
f
i
t
n
e
d

i

n

i

M
U
N

t
s
e
r
o
F
m
o
d
n
a
R

s
e
r
a
p
m
o
c

,
l

e
d
o
m

l

e
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
u
t
a
e
f

s
e
t
a
u
l
a
v
e

g
n

i
l

p
m
a
s
r
e
v
o

,
s

m
h
t
i
r
o
g
l
a

n
o
i
t
c
e
e
s

l

s
d
o
h
t
e
m

1
2
0
2

,

e
r
a
u
q
S

e
h
t

s
e
z
i
s
a
h
p
m
E

,

M
B
G

t
h
g
i
L

,
t
s
o
o
B
G
X

d
n
a

l

e
b
a
t
S

h
c
r
a
e
e
R

&

,
.

R

,

e
Y

,
.

2
1
.
R

,

e
Y

h
t
i

w
d
u
a
r
F

t
n
e
m
e
t
a
t
S

l

i

e
n
h
c
a
M
e
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

i

2
1
.
g
n
n
r
a
e
L

Z

,

u
L

i

l
a
i
c
n
a
n
F

i

g
n
i
t
c
e
t
e
D

1

e
h
t

s
e
z
i
s
a
h
p
m
E

,
s
k
r
o
w
t
e
N

f
e

i
l

e
B
n
a
i
s
e
y
a
B

n
o

d
e
s
a
b

s
d
o
h
t
e
M

a
i
d
e
c
o
r
P

,
l

e
a
S

,
.
I

,
i
l
a
g
d
a
S

f

o

s
i
s
y
l
a
n
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
P

2

L
M

f

o

s
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

s
s
o
r
c
a

i

s
e
u
q
n
h
c
e
t

d
e
c
n
a
u
n

d
u
a
r
f

t
n
e
r
e
f
f
i

d

r
o

f

s
e
t
a
c
o
v
d
a

,
s
e
i
r
o
g
e
t
a
c

s

m
h
t
i
r
o
g
l
a

d
e
c
n
a
h
n
e

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

d
e
t
s
e
g
g
u
s

e
h
t

,

d
u
a
r
f

d
r
a
c

t
i
d
e
r
c

l
a
u
t
c
a

n
o

d
e
t
a
u
l
a
v
e

n
e
h

W

e
h
t

s
t
a
e
b

l

e
d
o
m

t
r
a
-
e
h
t
-
f
o
-
e
t
a
t
s

.
s

m
h
t
i
r
o
g
l
a

l
a
r
u
e
N
d
n
a

,
s

m
h
t
i
r
o
g
l
A

s
k
r
o
w
t
e
N

n
o
i
s
i
c
e
D

i

,
s
e
n
h
c
a
M

r
o
t
c
e
V
t
r
o
p
p
u
S

c
i
t
e
n
e
G

,
s
e
e
r
T

i

g
n
n
r
a
e

l

i

e
n
h
c
a
m

e
h
t

o
t

d
e

i
l

p
p
a

d
u
a
r
f

l
a
i
c
n
a
n
ﬁ

n
o
i
t
c
e
t
e
d

f

o
m
e
b
o
r
p

l

,

8
4
1

,

e
c
n
e
i
c
S

r
e
t
u
p
m
o
C

9
1
0
2

,

u
o
b
b
a
n
e
B

6
1
F.

&

,
.

N

t
i
d
e
r
C
n

i

s

m
h
t
i
r
o
g
l
A

i

g
n
n
r
a
e
L

i

e
n
h
c
a
M

d
u
a
r
F

s
d
r
a
C

6
1
.
n
o
i
t
c
e
t
e
D

,
t
s
e
r
o
F
m
o
d
n
a
R

d
n
a

L
M

f

o

e
s
u

e
h
T

,

0
1

,
s
s
e
c
c
A
E
E
E
I

,
.

K
F.

,
j
a
f
r
a
l
A

d
u
a
r
F

d
r
a
C

t
i
d
e
r
C

3

d
n
a

,

M
V
S

,

n
o
i
s
s
e
r
g
e
R

i

g
n
n
r
a
e
L

e
m
e
r
t
x
E

n
o
i
s
i
c
e
D

,
t
s
o
o
B
G
X

c
i
t
s
i
g
o
L

,

e
e
r
T

d
o
h
t
e
M

r
o

f

s

m
h
t
i
r
o
g
l
a

L
D

f

o

n
o
i
t
c
e
t
e
d

e
h
t

d
u
a
r
f

d
r
a
c

t
i
d
e
r
c

2
2
0
2

,
.
I

,

k

i
l
a
M

,
.

U

.

H

,

n
a
h
K

,

m
a
l
l
a
s
u
m
A

l

,

n
a
z
m
a
R

,
.

N

,

d
e
m
h
A
&

,
.

M

8
1
.

M

d
n
a

i

g
n
n
r
a
e
L

i

e
n
h
c
a
M

g
n
i
s
U
n
o
i
t
c
e
t
e
D

t
r
A
-
e
h
t
-
f
o
-
e
t
a
t
S

i

g
n
n
r
a
e
L

p
e
e
D

8
1
.
s

m
h
t
i
r
o
g
l
A

t
i
d
e
r
c

l
a
n
o
i
t
i
d
d
a

n
o

k
r
o
w
e
m
a
r
f

m
o
r
f

s
t
e
s
a
t
a
d

d
u
a
r
f

d
r
a
c

s
n
o
i
t
u
t
i
t
s
n

i

l
a
i
c
n
a
n
ﬁ

o
t

s
e
i
t
i
n
u
t
r
o
p
p
o

e
h
t

e
v
o
r
p
m

i

f

o

n
o
i
t
c
e
t
e
d

d
u
a
r
f

d
r
a
c

t
i
d
e
r
c

t
h
g
i
l

h
g
i
H

r
o
i
r
e
p
u
s

i

t
i
b
h
x
e

t
s
o
o
B
a
d
A
h
t
i

w

-
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

%
8
9
9
9

.

d
e
v
e
h
c
a

i

C
C
M
d
n
a

y
c
a
r
u
c
c
a

r
e
h
t
o

s

m
r
o
f
r
e
p
t
u
o

s

m
h
t
i
r
o
g
l
a

M
T
S
L

d
e
s
o
p
o
r
P

l

e
b
m
e
s
n
e

9
9
0

.

f

o

m
o
d
n
a
R

,

n
o
i
s
s
e
r
g
e
R

,
s
e
e
r
T
a
r
t
x
E

,
t
s
e
r
o
F

,

M
V
S

,
t
s
o
o
B
G
X

t
s
o
o
B
a
d
A
T-
E

e
h
t

n

i

i

s
e
u
q
n
h
c
e
t

L
M

f

o

y
c
a
c
ﬁ
f
e

d
u
a
r
f

d
r
a
c

t
i
d
e
r
c

f

o

n
o
i
t
c
e
t
e
d

1
2
0
2

,
g
n
a

W
&

,

Y.

9
1
.
Z

d
r
a
C

i

g
n
n
r
a
e
L

i

e
n
h
c
a
M

r
o

f

i

s
e
u
q
n
h
c
e
T

t
i
d
e
r
C
g
n
i
t
c
e
t
e
D

9
1
.
d
u
a
r
F

d
e
s
a
B
-
t
s
o
o
B
a
d
A
d
n
a

k
r
o
w
t
e
n

l
a
r
u
e
N

d
u
a
r
f

d
r
a
c

t
i
d
e
r
C

,

0
1

,
s
s
e
c
c
A
E
E
E
I

,
.

E

,

o
h
g
o
n
e
s
E

d
e
r
e
e
n
i
g
n
E
-
e
r
u
t
a
e
F
A

5

,

M
T
S
L

,

l

e
b
m
e
s
n
e

N
N
E
-
E
T
O
M
S

,
t
s
o
o
B
a
d
A

a

g
n
i
s
u

n
o
i
t
c
e
t
e
d

k
r
o
w
t
e
n

l
a
r
u
e
n

d
n
a

l

e
b
m
e
s
n
e

g
n
i
r
e
e
n
i
g
n
e

e
r
u
t
a
e
f

2
2
0
2

,
.

D

.
I

,

e
y
n
e
M

i

,
.

G
T.

,
t
r
a
w
S

&

,
.

K

,
a
b
e
u
r
A

l

.

G

,

o
d
i
a
b
O

d
e
c
n
a
h
n
E

r
o

f

l

e
b
m
e
s
n
E

k
r
o
w
t
e
N

l
a
r
u
e
N

d
u
a
r
F

d
r
a
C

t
i
d
e
r
C

0
2
.
n
o
i
t
c
e
t
e
D

e
h
t

f

o

n
o
i
t
a
d

i
l
a
V

s
d
o
h
t
e
m
L
M
d
e
s
o
p
o
r
P

c
i
t
s
i
g
o
L

,
s
e
e
r
T
n
o
i
s
i
c
e
D

e
h
t

g
n
i
s
s
e
s
s
A

,

9

,
s
s
e
c
c
A
E
E
E
I

,

n
u
S

,
.

E

,
i
r
e
b
e
l
I

E
T
O
M
S

f

o

t
n
e
m

s
s
e
s
s
A

4

k
r
o
W

e
r
u
t
u
F

l

n
o
i
s
u
c
n
o
C

d
e
s
U
s
l
e
d
o
M

r
e
p
a
P

e
h
t

f

o

e
m
e
h
T

d
n
a

l
a
n
r
u
o

J

n
o
i
t
a
c
i
l

b
u
P

f

o

e
t
a
D

s
r
o
h
t
u
A

e
l
t
i
T

o
n
S

s

m
h
t
i
r
o
g
l
a

i

g
n
n
r
a
e

l

p
e
e
d

d
n
a

s

m
h
t
i
r
o
g
l
a

i

g
n
n
r
a
e

l

i

e
n
h
c
a
m
g
n
i
s
u

n
o
i
t
c
e
t
e
d

d
u
a
r
f

l
a
i
c
n
a
n
ﬁ

n
o

s
k
r
o
w
h
c
r
a
e
s
e
r

s
u
o
i
r
a
v

f

o

s
i
s
y
l
a
n
a

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

.

1

l

e
b
a
T

---

<!-- PAGE 5 -->

56

Intelligent Decision Technologies 19(1)

Figure 1. Architecture of the proposed methodology.

explainable AI. The goal is to strengthen defences and provide stakeholders with interpretable information to combat
ﬁnancial crime.27

3.1 Dataset description and data preprocessing

With this dataset, we want to address a knowledge vacuum in publicly available ﬁnancial services datasets, with a focus on
mobile money transactions as a relatively young industry. Many real-world datasets are not available to the public because
of the sensitive nature of ﬁnancial transactions.28 To get around this constraint, the dataset is artiﬁcially constructed using
a simulator called PaySim. To simulate mobile money transactions, PaySim uses a subset of real transactions extracted
from a provider’s monthly ﬁnancial data. A multinational ﬁrm is now running the mobile banking service in more than 14
countries across the world, and they are the ones who provided the initial logs.

The Swedish Knowledge Foundation (grant: 20140032) is supporting the study “Scalable resource-efﬁcient solutions
for big data analytics,” which includes this dataset.29 The dataset encompasses a comprehensive 6,362,620 records, of
which 6,354,407 are valid transactions, constituting 99.87%, and 8213 are fraudulent transactions, amounting to 0.13%.
Among the ﬂagged transactions, totaling 16, all fall under the “TRANSFER” type and are marked as fraudulent. The
transaction amounts in this subset range from 353,874.22 to 10,000,000.0.

In this preliminary phase, we commence by importing essential libraries and conducting a comprehensive examination
of the dataset. Our initial focus involves scrutinizing for any missing data and delving into the distribution patterns of both
valid and fraudulent transactions, establishing a foundational understanding for subsequent preprocessing steps.

In addition, we enhance our exploratory analysis through data visualization techniques, enabling a more insightful
understanding of the dataset’s characteristics and aiding in the identiﬁcation of patterns or trends that may inﬂuence the
subsequent modeling process. Figure 2 presents a pie chart illustrating the distribution of transaction types, revealing that
Transfer Transactions constitute 19%, while Cash Out Transactions dominate the majority with an 81% representation.

In Figure 3, a bar graph delineates the total monetary value associated with each transaction type. Cash Out trans-
actions exhibit a substantial total amount of 394,412,995,224, while Transfer transactions surpass with a total amount
of 485,291,987,263, offering a comprehensive visual representation of the ﬁnancial magnitudes associated with each
transaction category. In Figure 4, a bar graph meticulously portrays the incidence of fraudulent transactions within each
transaction type. Notably, Cash Out transactions account for 223,750 instances, while Transfer transactions reveal a higher
frequency with 532,909 cases, providing a nuanced insight into the distribution of fraudulent activities across different
transaction categories.

To fortify the robustness of our analysis, we diligently address potential imbalances inherent in the dataset. Moreover,
we meticulously investigate and rectify disparities in balances at both the origin and destination following transactions.

---

<!-- PAGE 6 -->

Vijayanand and Smrithy

57

Figure 2. Pie chart of ratio of transaction types.

Figure 3. Total amount transacted in each transaction type.

---

<!-- PAGE 7 -->

58

Intelligent Decision Technologies 19(1)

Figure 4. Fraudulent transactions types- cash out and transfer.

The identiﬁcation and analysis of transactions with amounts less than or equal to zero offer valuable insights into potential
anomalies that may impact the model’s performance. Table 2 shows different attributes of the dataset.

3.2 Feature engineering

Following the initial exploratory phase, we transition to a meticulous feature engineering process to enhance the dataset’s
suitability for machine learning model training. Begin with the 11 columns that make up the original features: “step,”
“type,” “amount,” “nameOrig,” “oldbalanceOrg,” “newbalanceOrig,” “nameDest,” “oldbalanceDest,” “newbalanceDest,”
“isFraud,” and “isFlaggedFraud.” Then we go on to the current features. Unwanted features such as “step,” “type,”
“nameOrig,” “nameDest,” “error_orig,” “error_dest,” and “isFlaggedFraud” are subsequently removed to streamline the
dataset.

To ensure uniformity, continuous values within the columns “amount,” “oldbalanceOrg,” “oldbalanceDest,” “newbal-
anceOrig,” and “newbalanceDest” are standardized to fall within the 0 to 1 range using the StandardScaler. One of the
most important steps in getting data ready to train machine learning models is employing the ‘train test split’ approach to
divide the resultant dataset into several sets: training and testing. To make sure the split is acceptable, we look at the size
of the training and testing sets.

Additionally, we conduct checks for missing values in the target variable, “isFraud,” and address them by dropping
rows with missing values. After cleaning the data, it is divided into two sets: one for testing and one for training. The
stratiﬁcation is kept and the test size is set at 20%. The ﬁnal dimensions of the split datasets are veriﬁed to conﬁrm the
successful completion of the preprocessing steps.

---

<!-- PAGE 8 -->

Vijayanand and Smrithy

Table 2. Detailed information of the dataset attributes

Attribute

Description

step
type
amount
nameOrig
oldbalanceOrg
newbalanceOrig
nameDest
oldbalanceDest
newbalanceDest
isFraud
isFlaggedFraud

A real-world time measure where one step is equivalent to one hour.
Type of Transaction: Transfer, Debit, Payment, Cash-In, Cash-Out.
The transaction amount expressed in local currency.
Transaction started by the customer.
Starting balance prior to the transaction.
New balance following the transaction.
Customer receiving the transaction.
The recipient’s starting balance prior to the transaction.
The recipient’s new balance following the transaction.
For transactions carried out by fraudulent agents in the simulation, a binary indicator (1 or 0).
A signal that suggests attempts to send more than $200,000 in a single transaction.

59

Data Type

int64
object
ﬂoat64
object
ﬂoat64
ﬂoat64
object
ﬂoat64
ﬂoat64
int64
int64

3.3 Classiﬁcation models

One of the most important uses of machine learning is fraud detection, where choosing the right model may have a huge
impact on efﬁciency. In this study, we dive headﬁrst into the complex world of fraud detection and analyse six well-
known machine learning models: Neural Network, XGBoost, Decision Tree, Random Forest, and Logistic Regression.
The research aims to provide a detailed and thorough knowledge of each model’s effectiveness and suitability for handling
the intricacies of fraud detection by carefully using several performance indicators, such as accuracy, F1 score, confusion
matrix, and ROC AUC score.

3.3.1 Logistic regression. David Cox developed the basic technique for creating a logistic model (sometimes called the
logit model) in 1958 and named it logistic regression. Due to its connection to logistic data distribution, its primary beneﬁt
is that it can be applied to both class probability estimation and classiﬁcation. It applies a nonlinear sigmoidal function as
shown in equation 1 on a linear combination of features.30

S(x) = 1 ÷ (1 + e(−x))

(1)

Logistic regression is both a robust and ﬂexible method for dichotomous classiﬁcation prediction, which involves making
predictions for states or outcomes that may be represented as yes/no, success/failure, or will occur/will not occur.31 Since
the classes in a supervised classiﬁcation issue are discrete, the goal of the methods is to ﬁnd the decision boundaries
between them.32

3.3.2 Decision tree. When it comes to supervised learning, decision trees are the way to go.33 To aid in decision-making,
decision trees use a tree structure that mimics human brain processes.33 Attribute selection as the decision tree’s root
node is the ﬁrst step.33 Additionally, for each single attribute value, it creates a branch and splits the instance into many
subgroups. Thirdly, there is a connection to a branch from the root node in each subset.34 With each branch completed,
the algorithm repeatedly continues the process.35

3.3.3 Random forest. When it comes to categorization, the Random Forest (RF) algorithm is among the top options. RF
is capable of properly categorizing massive volumes of data. This method of learning involves training a large number of
decision trees, with the goal of having each tree anticipate the modal outputs.36 According to,36 RF uses random vector
values for each tree as its predictors. The basic premise is that a group of “weak learners” may work together to create a
“strong learner."36–40

3.3.4 XGBoost. An implementation of Gradient Boosting that makes use of gradients derived from decision trees is
known as Extreme Gradient Boosting (XGBoost). Iteratively, it builds simple, brief decision trees. Because of its extreme
bias, every tree is referred to as a “weak learner.” XGBoost starts by constructing the ﬁrst, most basic tree, which performs
poorly. After then, it creates a second tree that is trained to predict actions that the previous tree—a poor learner—was
unable to do. The method generates progressively weaker learners, each of them ﬁxing the preceding tree before the
stopping condition—for example, the quantity of trees (estimators) that need to be produced—is satisﬁed. XGBoost offers
further beneﬁts: Training is quick and can be split up or divided among multiple clusters.41,42

---

<!-- PAGE 9 -->

60

Intelligent Decision Technologies 19(1)

Table 3. Cross validation results on accuracy (%)

Model

Logistic regression
Decision Tree
Random Forest
XGBoost
LightGBM
Neural Network

Fold 1

99.82
99.94
99.92
99.91
99.75
99.86

Fold 2

99.83
99.93
99.92
99.90
99.75
99.85

Fold 3

99.81
99.94
99.92
99.91
99.75
99.85

Fold 4

99.82
99.93
99.93
99.90
99.76
99.87

Fold 5

99.83
99.94
99.92
99.92
99.76
99.85

Table 4. Cross validation results on F1 scores

Model

Fold 1

Fold 2

Fold 3

Fold 4

Fold 5

Logistic regression
Decision Tree
Random Forest
XGBoost
LightGBM
Neural Network

0.60
0.89
0.86
0.83
0.51
0.68

0.62
0.90
0.85
0.83
0.50
0.68

0.61
0.89
0.85
0.82
0.51
0.69

0.60
0.90
0.85
0.83
0.50
0.68

0.60
0.89
0.86
0.83
0.50
0.68

Table 5. Cross validation results on ROC AUC scores

Model

Fold 1

Fold 2

Fold 3

Fold 4

Fold 5

Logistic regression
Decision Tree
Random Forest
XGBoost
LightGBM
Neural Network

0.98
0.94
0.99
0.99
0.64
0.98

0.98
0.94
0.99
0.99
0.64
0.98

0.97
0.94
0.99
0.99
0.64
0.98

0.98
0.94
0.99
0.99
0.64
0.98

0.98
0.94
0.99
0.99
0.65
0.98

3.3.5 LightGBM. LightGBM is a framework for gradient boosting that makes use of techniques for tree-based learning.
The following advantages are achieved by its efﬁcient distribution: quicker training speed, less memory use, higher accu-
racy, support for GPU, distributed, and parallel learning, and better efﬁciency overall.43 Many boosting programs employ
pre-sort-based algorithms for decision tree learning, such XGBoost’s default approach.44,45 It is not easy to optimize,
despite being a straightforward solution. LightGBM uses methods that are based on histograms,46–48 which divide the
values of continuous features (attributes) into discrete bins. This decreases memory use and speeds up training.49

3.3.6 Neural network. Neural networks (NNs) and artiﬁcial neural networks (ANNs) are two names for the same kind of
AI model that attempts to simulate brain activity. In the 1990s, they were presented as a different approach to address geo-
graphic issues, and more recently, they have grown because of developments in computer power, artiﬁcial intelligence, and
data availability, among other areas.50 Neural Networks can learn complex nonlinear relationships using training example
sets. They work particularly effectively in pattern identiﬁcation scenarios where complex trends in high-dimensional data
need to be identiﬁed.51

A stratiﬁed K-Fold cross validation was performed to ensure the reliability and robustness of the experiments. Tables 3,
4 and 5 show the cross validation results of various models on the metrics accuracy, F1 score and ROC AUC scores
respectively. We summarize the average performance characteristics of our machine learning models for classiﬁcation
in Table 6, providing a thorough understanding of their efﬁcacy. Accuracy, F1 score, and ROC AUC score are some of
the most important metrics that reveal the models’ overall classiﬁcation accuracy, precision-recall balance, and ability to
discern between positive and negative examples.

Additionally, Friedman’s statistical test is used to compare the performance of different models. The resulting p-value
is 0.000139 which is signiﬁcantly less than the signiﬁcance level 0.05 indicating that there are signiﬁcant differences
between the performances of the models. The Nemenyi post-hoc test provides pairwise comparisons between the models.
Table 7 shows the p-values for the comparisons.

---

<!-- PAGE 10 -->

Vijayanand and Smrithy

61

Table 6. Performance metrics of classiﬁcation machine learning models

Accuracy (%) of the
ML/DL Model

F1 Score of the
ML/DL Model

ROC AUC Score of the
ML/DL Model

Machine/Deep
Learning Model

Logistic Regression.30
Decision Tree.33
Random Forest.36
XGBoost.41,42
LightGBM.49
Neural Network.50,51

99.826
99.937
99.922
99.908
99.753
99.855

Table 7. Nemenyi Post-Hoc Test Results

0

1.000000
0.009434
0.114066
0.532706
0.900000
0.900000

1

0.009434
1.000000
0.900000
0.532706
0.001000
0.114066

2

0.114066
0.900000
1.000000
0.900000
0.009434
0.532706

0
1
2
3
4
5

Table 8. Cross validation results of ensemble learning classiﬁer

Metrics

Accuracy
F1 Score
ROC AUC Score

Fold 1

99.90
0.81
0.99

Fold 2

99.91
0.82
0.99

0.606
0.893
0.855
0.829
0.507
0.682

3

0.532706
0.532706
0.900000
1.000000
0.114066
0.900000

Fold 3

99.90
0.81
0.99

0.978
0.943
0.996
0.990
0.641
0.983

4

0.900000
0.001000
0.009434
0.114066
1.000000
0.532706

Fold 4

99.90
0.81
0.99

5

0.900000
0.114066
0.532706
0.900000
0.532706
1.000000

Fold 5

99.92
0.82
0.99

The results suggest that certain models such as Logistic Regression, Decision Trees, Random Forest, LightGBM have

performance differences that are statistically signiﬁcant.

4 Ensemble learning model- voting classiﬁer

When solving tasks like classiﬁcation, ensemble learning uses a combination of many learning models that have been
deliberately generated.52 This is based on the notion that two minds are preferable to one. Additionally, we gather infor-
mation from various sources and rank or combine them in order to make strategic judgments. A supervised learning
algorithm is an ensemble in and of itself. Many classiﬁer systems are another name for ensemble learning systems.32
Using the same data to train several models and then combining their predictions is known as ensemble learning.53 The
goal of ensemble learning is to improve performance above that of a single model by combining many models into a
single ensemble.53 The ﬁrst step is to determine how to build the ensemble models, and the second is to ﬁgure out how to
aggregate the forecasts of each member of the ensemble. One way to make predictions more accurate is to use ensemble
learning.54

This instance makes use of a meta classiﬁer, which is able to merge prediction models from different or comparable
machine learning datasets by means of a majority vote or soft voting. To choose the most likely class, soft voting aver-
ages the base models’ class pseudo-probabilities.55 The voting classiﬁer outperforms the other baseline models because
to its ability to incorporate the predictions of many ML and DL models.56 Figure 5 illustrates our proposed ensemble
model, a culmination of various classiﬁers aimed at elevating predictive performance through strategic combination. A
number of classiﬁers—including XGBoost, LightBGM, Neural Networks, Decision Tree Classiﬁer, and Random Forest
Classiﬁer—are part of this ensemble. Table 8 shows the Stratiﬁed K-Fold cross validation results of the ensemble learning
model.

Table 9 provides the average summary of the performance metrics of the ensemble learning model, with a focus on accu-
racy, F1 score, and ROC AUC score. The collective assessment highlights the model’s exceptional accuracy of 99.904%,
underscoring its efﬁcacy across diverse classiﬁcation scenarios.

---

<!-- PAGE 11 -->

62

Intelligent Decision Technologies 19(1)

Figure 5. Proposed ensemble model.

Table 9. Performance measure of ensemble learning classiﬁer

Ensemble Learning Model

99.904

0.814

0.990

Accuracy (%) of the Model

F1 Score of the Model

ROC AUC Score of the Model

Figure 6. Process of explainable AI.

5 Explainable AI

Coined by DARPA in 2016, Explainable AI (XAI) addresses the need for transparency in AI systems, countering the
‘black box’ nature of machine learning. Crucial in delicate ﬁelds like healthcare and banking, XAI seeks to ensure that AI
systems are transparent and easy to interpret. Using white-box models such as Concept Bottleneck Models, XAI justiﬁes
decisions, promoting trust and facilitating user comprehension. Symbolic regression is proposed for supervised machine
learning to ensure transparency and auditability. Overall, XAI seeks to demystify AI decisions, enhancing user trust and
understanding.57–60

In Figure 6, we can see how the requirements or application domain dictate the input data used to train the models, the
prediction approach that is selected, and the XAI methods that are used to explain the models’ inner workings and output

---

<!-- PAGE 12 -->

Vijayanand and Smrithy

Table 10. Average impact of attributes on model output

Attribute

OldBalanceOrg
NewBalanceOrg
Amount
NewBlanceDest
OldBalanceDest

63

Mean SHAP Value

0.065
0.055
0.04
0.03
0.03

Figure 7. Mean SHAP value (average impact of attribute on model output).

via an explanation interface.57 Because we are aware of Explainable AI’s results, we will be more conﬁdent in AI models.
Users can enhance the model’s accuracy and identify its shortcomings by using the output information. The end effect will
be that consumers are better able to decide how to enhance the model.61

In this study, we interpret machine learning model output using SHAP, a common explainability technique utilized in
Explainable AI (XAI). Basically, SHAP functions as a “feature attribution method”.62 Similar to a game theory approach,
SHAP enhances the readability of each prediction independently by determining the importance values for each attribute.
Three important attributes make up the aggregate degree of feature importance maintained by the SHAP values: “Missing-
ness, accuracy, and consistency”. In terms of interpretation, SHAP is more intuitive and simpler to compute.63 In addition
to being model-agnostic, it provides explanations that are both local and global and is more dependable when dealing with
any kind of data. In order to empower players according to their level of participation, we employ Shapley values, which
adhere to the four axioms of player engagement: “Efﬁciency, Symmetry, Dummy, Additive”.64 Shapley ﬁrst coined the
term SHAP in 1951. It is used to describe a certain output depending on how each input is involved in a prediction.

Table 10, along with Figures 7 and 8, unveils the mean SHAP values, shedding light on the pivotal role of selected
attributes within the framework of a predictive model. The utilization of SHAP values facilitates a nuanced understanding
of each attribute’s contribution to the model’s output. Remarkably, the OldBalanceOrg attribute takes precedence with the
highest mean SHAP value of 0.065, signifying its discernibly stronger impact on the model’s predictive outcomes. By
giving a quantiﬁable measure of attribute impact and providing insight into the model’s decision-making processes, these
values improve the interpretability and understanding of feature signiﬁcance.65

6 Result

The assessment of individual machine learning models underscores their exceptional performance in detecting ﬁnancial
fraud, with the Decision Tree model showcasing remarkable results. An F1 Score of 0.893, a ROC AUC Score of 0.943,
and a maximum accuracy of 99.937 percent distinguish the Decision Tree model as the best performer among the models
that were evaluated.

---

<!-- PAGE 13 -->

64

Intelligent Decision Technologies 19(1)

Figure 8. SHAP value and feature value.

With a 99.904% accuracy rate, an F1 Score of 0.814, and a remarkable ROC AUC Score of 0.990, the Ensemble Learn-
ing Model—implemented via a Voting Classiﬁer—demonstrates itself as a strong solution. This collective performance
underscores the efﬁcacy of amalgamating diverse models for enhanced fraud detection.

To delve into the interpretability of these models, a thorough SHAP analysis was conducted, revealing key attributes and
their mean SHAP values. Particularly noteworthy were attributes such as OldBalanceOrg, NewBalanceOrg, Amount, New-
BlanceDest, and OldBalanceDest, which exhibited signiﬁcant impacts on model outputs. These insights provide valuable
clarity to stakeholders, fostering a deeper understanding of the models’ decision-making processes and thereby augmenting
transparency and interpretability in the realm of ﬁnancial fraud detection.

7 Conclusion

In this research, we tackled the growing challenges in ﬁnancial technology, speciﬁcally addressing the rising threat of fraud
in mobile money transactions. While digital ﬁnance brings convenience, it also exposes institutions to sophisticated fraud.
Our study emphasized both high model accuracy and explainability by integrating machine learning with Explainable AI,
leveraging SHAP analysis. This work not only advances fraud prevention in digital ﬁnance but also sets a precedent for
transparent and interpretable machine learning systems. By prioritizing clarity, it empowers stakeholders with effective
decision-making tools in the evolving cybersecurity landscape, marking a signiﬁcant stride against ﬁnancial fraud in the
digital era.

8 Future work

The future of ﬁnancial fraud detection and prevention involves integrating cutting-edge technologies to combat sophisti-
cated fraud schemes. Key advancements include the development of real-time analysis and adaptive systems for dynamic
threat response, the use of behavioral biometrics for enhanced user recognition, blockchain technology for immutable
and transparent ledgers, quantum-resistant encryption methods, collaborative threat intelligence sharing, the examination
of non-ﬁnancial data for contextual insights, regulatory compliance solutions leveraging advanced technologies, and AI-
driven user authentication processes. These innovations aim to create more resilient and intelligent systems, crucial for
staying ahead in the ever-evolving landscape of digital ﬁnance.

Statements and declarations
Ethical approval

Informed consent

Funding
The authors received no ﬁnancial support for the research, authorship, and/or publication of this article.

---

<!-- PAGE 14 -->

Vijayanand and Smrithy

65

Declaration of conﬂicting interests
The authors declared no potential conﬂicts of interest with respect to the research, authorship, and/or publication of this article.

References
1. https://www.acfe.com/about-the-acfe/newsroom-for-media/press-releases/press-release-detail?s=ACFE-Estimates-Organizations-

Lose-5-percent-to-Fraud

2. https://www.statista.com/outlook/dmo/ﬁntech/digital-payments/worldwide
3. https://cybersecurityventures.com/cybercrime-damages-6-trillion-by-2021/
4. https://www.europol.europa.eu/cms/sites/default/ﬁles/documents/Spotlight-Report_Online-fraud-schemes.pdf
5. https://risk.lexisnexis.com/about-us/press-room/press-release/20221116-study-ﬁnds-fraud-costs
6. https://www.forbes.com/sites/louiscolumbus/2020/10/31/the-state-of-ai-adoption-in-ﬁnancial-services/?sh=739a49282aac
7. Hall P and Gill N. An introduction to machine learning interpretability. Sebastopol, CA: O’Reilly Media, Incorporated, 2019.
8. Ali A, Abd Razak S, Othman SH, et al. Financial fraud detection based on machine learning: a systematic literature review. Appl

Sci 2022; 12: 9637.

9. Al-Hashedi KG and Magalingam P. Financial fraud detection applying data mining techniques: a comprehensive review from 2009

to 2019. Comput Sci Rev 2021; 40: 100402.

10. Wickramanayake B, Geeganage DK, Ouyang C, et al. A survey of online card payment fraud detection using data mining-based

methods. arXiv preprint arXiv:2011.14024 (2020).

11. Sengupta K and Das PK. Detection of ﬁnancial fraud: comparisons of some tree-based machine learning approaches. J Data Inf

Manag 2023; 5: 23–37.

12. Liu Z, Ye R and Ye R. Detecting ﬁnancial statement fraud with interpretable machine learning, 2021.
13. Hilal W, Gadsden SA and Yawney J. Financial fraud: a review of anomaly detection techniques and recent advances. Expert Syst

Appl 2022; 193: 116429.

14. Mittal S and Tyagi S. Computational techniques for real-time credit card fraud detection. Handbook of computer networks and

cyber security: principles and paradigms, 2020, pp.653–681.

15. Gupta BB, Perez GM, Agrawal DP, et al. Handbook of computer networks and cyber security. Springer 2020; 10: 978–973.
16. Sadgali I, Sael N and Benabbou F. Performance of machine learning techniques in the detection of ﬁnancial frauds. Proc Comput

Sci 2019; 148: 45–54.

17. Alghofaili Y, Albattah A and Rassam MA. A ﬁnancial fraud detection model based on LSTM deep learning technique. J Appl

Secur Res 2020; 15: 498–516.

18. Alarfaj FK, Malik I, Khan HU, et al. Credit card fraud detection using state-of-the-art machine learning and deep learning

19.

algorithms. IEEE Access 2022; 10: 39700–39715.
Ileberi E, Sun Y and Wang Z. Performance evaluation of machine learning methods for credit card fraud detection using SMOTE
and AdaBoost. IEEE Access 2021; 9: 165286–165294.

20. Esenogho E, Mienye ID, Swart TG, et al. A neural network ensemble with feature engineering for improved credit card fraud

detection. IEEE Access 2022; 10: 16400–16407.

21. Alfaiz NS and Fati SM. Enhanced credit card fraud detection model using machine learning. Electronics 2022; 11: 662.
22. Awosika T, Shukla RM and Pranggono B. Transparency and privacy: the role of explainable AI and federated learning in ﬁnancial

23.

fraud detection. arXiv preprint arXiv:2312.13334, 2023.
Jayasinghe SL, Thomas DT, Anderson JP, et al. Global application of regenerative agriculture: a review of deﬁnitions and
assessment approaches. Sustainability 2023; 15: 15941.

24. Sharma N, Chakrabarti A and Balas VE. Data management, analytics and innovation. Proc ICDMAI 2019; 1: 1–740.
25. https://bjs.ojp.gov/taxonomy/term/ﬁnancial-fraud
26. https://www.itu.int/en/ITU-T/techwatch/Pages/mobile-money-standards.aspx#:∼:text=Mobile%20money%20refers%20to%20

ﬁnancial,directly%20to%20a%20bank%20account

27. Muna RK, Hossain MI, Alam MGR, et al. Demystifying machine learning models of massive IoT attack detection with explainable

AI for sustainable and secure future smart cities. IoT 2023; 24: 100919.

28. Gardner C. Classifying imbalanced ﬁnancial fraud data utilizing enhanced random forest algorithm, 2020.
29. Lopez-Rojas EA, Elmir A and Axelsson S. PaySim: A ﬁnancial mobile money simulator for fraud detection. In: The 28th European

Modeling and Simulation Symposium-EMSS, Larnaca, Cyprus, 2016.

30. Ashenden SK, ed. The era of artiﬁcial intelligence, machine learning, and data science in the pharmaceutical industry. Cambridge,

MA: Academic Press, 2021.

31. Seufert EB. The freemium business model. Freemium Economics, 2014, pp.1–27.
32. Gudivada VN, Irfan MT, Fathi E, et al. Cognitive analytics: going beyond big data analytics and machine learning. In: Handbook

of statistics. Vol. 35. Amsterdam, Netherlands: Elsevier, 2016, pp.169–205.

---

<!-- PAGE 15 -->

66

Intelligent Decision Technologies 19(1)

33. Al Mamun MH and Keikhosrokiani P. Predicting onset (type-2) of diabetes from medical records using binary class classiﬁcation.

In: Big data analytics for healthcare. Cambridge, MA: Academic Press, 2022, pp.301–312.

34. Keikhosrokiani P, ed. Big data analytics for healthcare: datasets, techniques, life cycles, management, and applications.

Cambridge, MA: Academic Press, 2022.

35. Kohavi R. Scaling up the accuracy of naive-bayes classiﬁers: A decision-tree hybrid. In Kdd, 1996, August, Vol. 96, pp.202–207.
36. Chatterjee A, Bala P, Gedam S, et al. Machine learning and deep learning-based advanced classiﬁcation techniques for the detection

of major depressive disorder. Aslib J Inf Manag 2023.

37. Mishra A and Suhas MV. Classiﬁcation of benign and malignant bone lesions on CT images using random forest. In 2016
IEEE international conference on recent trends in electronics, Information & Communication Technology (RTEICT), 2016, May,
pp.1807–1810). IEEE.

38. Chu G, Lo P, Ramakrishna B, et al. Bone tumor segmentation on bone scans using context information and random forests.
In Medical Image Computing and Computer-Assisted Intervention–MICCAI 2014: 17th International Conference, Boston, MA,
USA, September 14–18, 2014, Proceedings, Part I 17, 2014, pp.601–608. Springer International Publishing.

39. Nguyen C, Wang Y and Nguyen HN. Random forest classiﬁer combined with feature selection for breast cancer diagnosis and

prognostic. 2013.

40. Shrivastava D, Sanyal S, Maji AK, et al. Bone cancer detection using machine learning techniques. In: Smart healthcare for disease

diagnosis and prevention. Cambridge, MA: Academic Press, 2020, pp.175–183.

41. Ramraj S, Uzir N, Sunil R, et al. Experimenting XGBoost algorithm for prediction and classiﬁcation of different datasets. Int J

Control Theory Appl 2016; 9: 651–662.

42. Subasi A, Panigrahi SS, Patil BS, et al. Advanced pattern recognition tools for disease diagnosis. In: 5G Iot and edge computing

for smart healthcare. Cambridge, MA: Academic Press, 2022, pp.195–229.

43. https://lightgbm.readthedocs.io/
44. Mehta M, Agrawal R and Rissanen J. SLIQ: A fast scalable classiﬁer for data mining. In Advances in Database
Technology—EDBT’96: 5th International Conference on Extending Database Technology Avignon, France, March 25–29, 1996
Proceedings 5, 1996, pp.18–32. Springer Berlin Heidelberg.

45. Shafer J, Agrawal R and Mehta M. SPRINT: A scalable parallel classiﬁer for data mining. In Vldb, 1996, September, Vol. 96,

pp.544–555.

46. Alsabti K, Ranka S and Singh V. CLOUDS: A decision tree classiﬁer for large datasets, 1998.
47.

Jin R and Agrawal G. Communication and memory efﬁcient parallel decision tree construction. In Proceedings of the 2003 SIAM
international conference on data mining, 2003, May, pp.119–129. Society for Industrial and Applied Mathematics.

48. Li P, Wu Q and Burges C. Mcrank: Learning to rank using multiple classiﬁcation and gradient boosting. Adv Neur Inf Process Syst

2007; 20: 897–904.

49. https://lightgbm.readthedocs.io/en/latest/README.html
50. Kobayashi A. International encyclopedia of human geography. Amsterdam, Netherlands: Elsevier, 2019.
51. Guenther FH. Neural networks: Biological models and applications. Oxford: International Encyclopedia of the Social &

Behavioral Sciences, 2001, pp.10534–10537.

52. Polikar R. Ensemble learning. Ensemble machine learning: Methods and applications, 2012, pp.1–34.
53. BENNOUH R and Oussama AIADI. A healthcare system using deep learning (Doctoral dissertation), 2022.
54. Schneider P and Xhafa F. Anomaly detection and complex event processing over IoT data streams: with application to EHealth

and patient data monitoring. Cambridge, MA: Academic Press, 2022.

55. Manconi A, Armano G, Gnocchi M, et al. A soft-voting ensemble classiﬁer for detecting patients affected by COVID-19. Appl Sci

2022; 12: 7554.

56. Aftabi SZ, Ahmadi A and Farzi S. Fraud detection in ﬁnancial statements using data mining and GAN models. Expert Syst Appl

2023; 227: 120144.

57. Saranya A and Subhashini R. A systematic review of Explainable Artiﬁcial Intelligence models and applications: recent

developments and future trends. Decis Anal J 2023: 100230.
58. https://www.darpa.mil/program/explainable-artiﬁcial-intelligence
59. https://onlinelibrary.wiley.com/toc/26895595/2021/2/4
60. https://xaitk.org/
61. https://higherlogicdownload.s3.amazonaws.com/ISACA/71336a0d-5200-45d1-ba3d-b1b5116f8456/UploadedImages/2023_

Documents/ISACA_KE_Newsletter_2023_Edition.pdf

62. Van den Broeck G, Lykov A, Schleich M, et al. On the tractability of SHAP explanations. J Artif Intell Res 2022; 74: 851–886.
63. Linardatos P, Papastefanopoulos V and Kotsiantis S. Explainable AI: a review of machine learning interpretability methods.

Entropy 2021; 23: 18.

---

<!-- PAGE 16 -->

Vijayanand and Smrithy

67

64. Loh HW, Ooi CP, Seoni S, et al. Application of explainable artiﬁcial intelligence for healthcare: a systematic review of the last

decade (2011–2022). Comput Methods Programs Biomed 2022; 226: 107161.

65. Kadem M, Noseworthy M and Doyle T. XGBoost for interpretable Alzheimer’s decision support. Proc AAAI Sympos Ser 2023;

1: 135–141.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

ResearchArticle
IntelligentDecisionTechnologies
Explainable AI - enhanced ensemble 2025,Vol.19(1)52–67
©TheAuthor(s)2024
learning for financial fraud detection in Articlereuseguidelines:
sagepub.com/journals-permissions
DOI:10.1177/18724981241289751
mobile money transactions journals.sagepub.com/home/idt
Deepshika Vijayanand and Girijakumari Sreekantan Smrithy
Abstract
This research paper addresses the pressing problem of financial fraud in the changing context of digital banking by inte-
grating machine learning and explainable AI, specifically exploiting SHapley Additive exPlanations (SHAP). With a focus
on enhancing both accuracy and interpretability, this study utilizes a synthetically generated dataset from the PaySim
simulator, encompassing 6,362,620 records. The usefulness of an Ensemble Learning Model with a Voting Classifier is
shown by its evaluation of different machine learning models, which achieves an excellent accuracy of 99.904%.Empha-
sizingtransparency,accountability,andregulatorycompliance,thisworkemploysSHAPanalysistounveilattribute-level
interpretability,providingstakeholderswithclearinsights.Thegoalofthisinterdisciplinaryendeavoristoprovideasafe
spacefordigitalfinancebybridgingthegapbetweenprecisionandinterpretability,whichwillaidinthecreationofopen
methods.
Keywords
Ensemble learning, explainable AI, feature importance, financial fraud, interpretability, machine learning, mobile money,
SHAPanalysis,transparency
Received:15April2024;accepted:17September2024
1 Introduction
In today’s digitally-dominated world, the simplicity and efficacy of banking have changed due to the advancement of
financialtechnology,bringinginaneweraofpreviouslyunimaginableopportunities.Thoughtherearemanychallenges
associatedwiththisincreaseindigitalfinancialinteractions,thegrowingthreatoffinancialfraudisoneofthemostcritical
ones.Thereisanimmediateaneedreliablesystemsthatcanidentifyandstopfraudulentactionsastheyhappen, asthe
AssociationofCertifiedFraudExaminers(ACFE)reportsthatworldwidefraudlosseshavereachedaconcerning5%of
yearlyincome.1
Thesheervolumeofglobaldigitalpaymenttransactions,projectedtoreachUS$16.62tnby2028(Statista),underlines
the growing reliance on digital financial interactions.2 Nevertheless, with this digital transformation comes an alarming
increaseinthecostofcybercrime,projectedtoreachUS$10.5Trillionannuallyby2025.3 Thesophisticationofmodern
fraud schemes, leveraging advanced techniques such as machine learning to evade detection,4 poses not only a severe
financialriskbutalsojeopardizesthetrustthatunderpinstheentirefinancialecosystem.
Financialinstitutionsfaceamultifacetedchallenge,withanestimated$4.23lossforeverydollarlosttofraudin2022,5
consideringboththeimmediatefinancialimpactandthelong-termconsequences.Regulationcompliance,drivenbythe
GDPRandPSD2,necessitatesaccountabilityaswellastransparencyinprocessingofdataanddecisions.Inresponsetothis
evolvinglandscape,theadoptionofmachinelearninginfinancialservicesisgrowing,with70%offinancialinstitutions
reportingitsuseforfrauddetectionasof2020.6
SchoolofComputerScienceandEngineering,VelloreInstituteofTechnology,Chennai,India
Correspondingauthor:
GirijakumariSreekantanSmrithy,SchoolofComputerScienceandEngineering,VelloreInstituteofTechnology,Chennai,TamilNadu,600127,India.
Email:smrithy.gs@vit.ac.in

VijayanandandSmrithy 53
Traditionalmachinelearningmodelsfrequentlyfunctionasopaque,or“black-box,”entities,makingitchallengingfor
stakeholders to understand the logic underlying the models forecasts. Not only does a lack of transparency undermine
trust, but it also creates regulatory problems in sectors where explainability is essential. According to data scientists,
machine learning models can not be understood or trusted unless they are interpretable.7 Combining machine learning
withexplainableAIisthefocusofthisstudysinceitoffersasolutiontotheproblemsofaccuracyandinterpretabilityin
financialfrauddetectionsystems.
Explainable AI becomes crucial for demystifying machine learning models’ decision-making processes, especially
with SHAP (SHapley Additive exPlanations). Explainable AI is essential for fostering trust in financial institutions and
guaranteeingaccountabilityinalgorithmicdecision-making,anditsnecessityextendsbeyondcompliance.Thisresearch
combines the power of explainable AI with ensemble machine learning to create financial fraud detection models that
performwellinaccuracyandofferstakeholdersinterpretableinsights.Theultimateobjectivesaretostrengthenthebarrier
againstfinancialfraud,promotetrustinfinancialinstitutions,andcreateasafeenvironmentfordigitalfinance.
2 Literature survey
The need for robust systems to detect and prevent fraudulent activities has become paramount, leading to a shift from
traditional approaches to more adaptive and intelligent solutions. Ali et al.8 reviewed ML applications in detecting
financial fraud, emphasizing the limitations of traditional methods and highlighting SVM and ANN as key algorithms.
It addresses issues and gaps, suggesting exploration of ensemble methods and unsupervised learning like clustering.
Enhanced anomaly detection and incorporation of text-mining techniques such as Word2Vec, Doc2Vec, or BERT are
recommendedforimprovedMLmodelsincombatingfinancialfraud,providingacomprehensiveoverviewandinsights
forpotentialadvancements.Intheirextensivereviewof75publicationsspanning2009–2019,Al-Hashedietal.9classified
financial fraud as follows: bank fraud, insurance fraud, financial statement fraud, and cryptocurrency fraud. Of the 34
dataminingmethodsthatareincluded,SVMisthemostpopular,accountingfor23percentofalluses.NaïveBayesand
Random Forest followclosely behind (15percent each). The majority of studies (81.33%) focus on bank and insurance
fraud,offeringvaluableinsightsforacademiaandindustry.Thereviewcontributessignificantinformationtothefieldby
expandingthesampleandsummarizingnotableworks.Wickramanayakeetal.10addresscardpaymentfraud,asignificant
challengeintheglobaldigitaleconomy.Usingataxonomyderivedfromstudiesconductedbetween2009and2020,11 it
investigates fraud detection technologies that make use of data mining and machine learning advancements. Reviewing
45papers,thesurveyhighlightsstrategiesthattakeintoaccounthowfraudaffectsbusinesses,usefeatureengineeringto
profilecardholders,andadjusttochangingfraudtrends.Thepaperconcludeswithacomparativeevaluationofclassifica-
tionalgorithms,aimingtoprovideacomprehensiveoverviewforacademiaandcommercialdeveloperstacklingpayment
frauddetection.
A study conducted by Liu et al.12 focuses on creating a stable and interpretable model for financial fraud detection,
particularlyforimbalanceddatasets.ItidentifiesSmoteasthemosteffectiveoversamplingalgorithmandhighlightsAdap-
tive Lasso as the top performer for feature selection. LightGBM outperforms XGBoost and Random Forest in feature
importanceranking.ThestudyemphasizesthesignificanceofNULLNUMinidentifyingfraudulentcorporatedataand
recommendsincorporatingWoEencodingandIVvaluetestingforimprovedmodelperformance.Inconclusion,thepaper
suggestsfutureresearchdirections,includinglargersamplesizes,explorationofdeeplearning,andintegrationofnatural
languageprocessingtechnologiesforenhancedfinancialstatementfrauddetection.Anomalydetectionmethodsforfinan-
cialfraudarereviewedbyHilaletal.,13 withanemphasisonhowtechnologicallydrivenfraudhasledtorecentadvances
in unsupervised and semi-supervised learning. Issues with money laundering, insurance fraud, and credit card fraud are
addressed, with a focus on the transition from supervised to unsupervised and semi-supervised methods.11 Generative
modelslikeGANsandAEsarehighlightedforeffectivefeatureextraction,whiledeeplearningarchitectureslikeCNNs
and LSTMs capture temporal relations. The paper suggests future research directions, advocating for combined models
andemphasizinginterpretabilityinfrauddetection.
MittalS.&TyagiS.14examinesecurityconcernsinonlinecreditcardusagewithintheevolvinge-commercelandscape
over the past 25 years. Credit card fraud may be difficult to detect in real time, and skewed datasets are just two of the
problemshighlightedinthisanalysisofattackroutesandsolutions.15Thereviewunderscorestherecentsurgeincreditcard
transactionsandsubsequentfraud,leadingtothedevelopmentofmachinelearning-basedmodels.Someoftheproblems
that have been identified include a lack of standard algorithms and a lack of understanding of credit card processing.11
Furthermore,thearticlestressestheimportanceofbenchmarkdatasetsandinvestigatestheunrealizedpossibilitiesofbig
dataanalyticsandstreamingdatainrelationtofutureadvancementsinfrauddetection.15
Sadgali I. et al.16 evaluate machine learning techniques, emphasizing hybrid methods, for detecting various financial
fraudtypes,includingcreditcardfraud.Inordertosolveimbalanceddatasetsandincreaseaccuracyincreditcardfraud

54 IntelligentDecisionTechnologies19(1)
detection, the conclusion calls for improved algorithms and hybrid models. The findings emphasize the effectiveness of
Support Vector Machines (SVMs) in instantaneous transactional fraud detection.16 In response to the growing problem
offinancialfraudinonlineservices,AlghofailiY.etal.17 provideafreshstrategybasedondeeplearning’sLongShort-
TermMemory(LSTM)forbetterdetection.Inlessthanaminute,theLSTMbasedmodelachieves99.95%accuracyon
a genuine credit card fraud dataset, outperforming previous techniques and demonstrating its potential to advance fraud
detectionforhugedatasetsandreal-timeprocessingdemands.17
ThestudybyAlarfajF.K.etal.18 addressescreditcardfrauddetectionchallenges,proposingenhanceddeeplearning
algorithms. By improving its performance on the European card benchmark dataset, the model outperforms previous
techniques, earning a f1-score of 85.71 percent, a precision of 93.1 percent, and an area under the curve (AUC) of 98.0
percent.18 Thesefindingsdemonstratethepromiseofhighlydevelopedalgorithmsfortheaccurateidentificationofcredit
cardfraudintherealworld.18Forthepurposeofdetectingcreditcardfraud,IleberiE.etal.19useAdaBoostinconjunction
with a number of machine learning methods, such as Decision Trees, Random Forest, Extra Trees, XGBoost, Logistic
Regression,andSupportVectorMachine.ET-AdaBoostachieves99.98%accuracyandanMCCof0.99inthecomparison
study conducted on the European fraudulent transactions with credit cards dataset, demonstrating exceptional levels of
accuracy.19 The suggested machine learning techniques utilizing AdaBoost demonstrate exceptional results when tested
on a biased artificial credit card fraud dataset.19 By combining an ensemble classifier with an LSTM base learner in
AdaBoostandmakinguseofSMOTE-ENNforhybridresampling,EsenoghoE.etal.20 presentedasuccessfulapproach
todetectingcreditcardfraud.Thesuggestedmethodoutperformsotheralgorithms,achievinghighspecificity(0.998)and
sensitivity(0.996),indicatingitspotentialtoimprovecreditcardfrauddetection.20 Theincreaseddifficultyofcreditcard
fraud during the COVID-19 pandemic’s spike in online purchases was discussed by Alfaiz N. S., & Fati S. M..21 The
AllKNN-CatBoost model outperformed sixty-six other ML models on a real-world dataset, with an AUC of 97.94%, a
recallof95.91%,andanF1-Scoreof87.30%.21 Theresultsemphasizeitspotentialsignificanceinpreventingfraudulent
creditcardtransactionsduringonlineactivities,outperformingpreviousapproaches.
Awosika T. et al.22 introduced a novel approach to address fraudulent transactions in the financial sector, combining
Explainable AI (XAI) and Federated Learning (FL) to enhance transparency and interpretability in fraud detection sys-
tems. The integration of SHAP ensures accurate and understandable predictions, shedding light on influential features
and justifying decisions. This emphasis on transparency becomes crucial in sensitive domains, emphasizing that XAI is
essentialforaccountability,usertrust,andregulatorycomplianceinFL-basedfrauddetectionsystems.Table1showsthe
comparativeanalysisofvariousresearchworksonfinancialfrauddetectionusingmachinelearningalgorithmsanddeep
learningalgorithms.
It is evident from the in-depth review of numerous sources on financial fraud detection that machine learning (ML)
approachesareessentialfortacklingthedifficultiesassociatedwithfinancialfrauddetection.SVMs,DecisionTrees,Ran-
domForest,ANNs,anddeeplearningmodelssuchasLSTMarehighlyfavoredfortheirexceptionalaccuracy,according
to the reviewed literature.23,24 The emphasis on ensemble methods, data resampling techniques, and feature engineer-
inghighlightstheongoingpursuitofrefiningexistingmodels.Additionally,theincorporationofadvancedtechnologies,
suchasGenerativeAdversarialNetworks(GANs)signalsagrowingawarenessoftheneedforinterpretabilityandtrans-
parency in fraud detection systems. While the field has made substantial progress, the papers collectively advocate for
future research directions, including exploration into less-studied algorithms, text-mining techniques, natural language
processing, and the integration of novel approaches like federated learning and Explainable AI (XAI). The continuous
evolutionoffinancialfrauddetectionmethodologiesremainscriticaltostayingaheadofsophisticatedfraudulentactivities
andsafeguardingfinancialsystems.
3 Proposed methodology
Whensomeone“intentionallyandknowinglydeceivesthevictimbymisrepresenting,concealing,oromittingfactsabout
promised goods, services, or other benefits and consequences that are nonexistent, unnecessary, never intended to be
provided, or deliberately distorted for the purpose of monetary gain,” they are committing actions of financial fraud.25
Financialfraudinmobilemoneytransfersisthefocusofthisresearchwork. Mobilemoneyreferstomonetaryservices
andtransactionsthatmaybecarriedoutviaamobiledevice,suchaphoneortablet.26 Connectivitytoabankaccountis
notalwaysanoptionfortheseservices.26
Thisresearchfocusesonenhancingfraudpreventionsystemsbynotonlyprioritizingmodelaccuracybutalsoempha-
sizing explainability through SHAP analysis as illustrated in Figure 1. The study’s overarching goal is to provide more
open and understandable methodology by deconstructing machine learning models, with a focus on their use in finan-
cial fraud scenarios. An ever-changing cybersecurity environment is being tackled by combining machine learning with

VijayanandandSmrithy 55
|     | peedfoesuekam |     |     |     |     |     | tidercnisevitagen |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
larutan,gninrael .selpmasretaerg tiderclanoitidda otseitinutroppo duarfdractiderc
|     |                            | dna,gnissecorp |               | dnasmhtirogla |                       |               |                     |                             |              |              |                        |     |
| --- | -------------------------- | -------------- | ------------- | ------------- | --------------------- | ------------- | ------------------- | --------------------------- | ------------ | ------------ | ---------------------- | --- |
|     | ehtnihcraeseR dluohserutuf |                |               | sledomdirbyh  |                       | otseuqinhcet  | eslafeziminim       | ehtfonoitadilaV nokrowemarf | morfstesatad |              |                        |     |
|     |                            |                | fonoitarolpxE |               | dnastesatad           | gnicnalabataD |                     |                             |              |              | ehtevorpmi fonoitceted |     |
|     | kroWerutuF                 |                |               |               | gnisserdda decnalabmi | gnissecorp    |                     |                             |              | snoitutitsni |                        |     |
|     |                            |                |               | decnahne      | emit-laer             |               | duarfdrac noitceted |                             | duarfdrac    |              |                        |     |
|     |                            | egaugnal       |               |               |                       |               |                     |                             |              | laicnanfi    |                        |     |
thgilhgiH
|     | LLUNfoecnatropmi | etaroproctneluduarf |     | LMfosecnamrofrep | smhtirogladecnahne |     | detsegguseht,duarf | sdohtemLMdesoporP |     |     |     |     |
| --- | ---------------- | ------------------- | --- | ---------------- | ------------------ | --- | ------------------ | ----------------- | --- | --- | --- | --- |
gniyfitnediniMUN sdnemmocer,atad erutaefgnitargetni sledomdirbyhdna CCMdnaycarucca rehtosmrofreptuo
|     |     |     |     | ssorcaseuqinhcet |     | nodetaulavenehW dractiderclautca |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
smhtiroglagninraelpeeddnasmhtiroglagninraelenihcamgnisunoitcetedduarflaicnanfinoskrowhcraesersuoiravfosisylanaevitarapmoC ehtstaebledom roirepustibihxe %89.99deveihca
|     |     |     |     |     | duarftnereffid |     | tra-eht-fo-etats | tsooBadAhtiw |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | ---------------- | ------------ | --- | --- | --- | --- |
ehtsezisahpmE ehtsezisahpmE rofsetacovda -ecnamrofrep MTSLdesoporP
gnireenigne
|     |            |     | seuqinhcet |     | ,seirogetac |     | .smhtirogla |     |     |     | smhtirogla |     |
| --- | ---------- | --- | ---------- | --- | ----------- | --- | ----------- | --- | --- | --- | ---------- | --- |
|     | noisulcnoC |     |            |     |             |     |             |     |     |     | elbmesne   |     |
decnaun
99.0fo
|     |                   |     | ,skrowteNfeileBnaiseyaB |     | larueNdna,smhtiroglA |                  |                    |                        |                    |     |     |     |
| --- | ----------------- | --- | ----------------------- | --- | -------------------- | ---------------- | ------------------ | ---------------------- | ------------------ | --- | --- | --- |
|     |                   |     |                         |     |                      |                  | dna,MVS,noissergeR | citsigoL,seerTnoisiceD |                    |     |     |     |
|     | ,MBGthgiL,tsooBGX |     |                         |     |                      | noisiceD,tsooBGX |                    | modnaR,noissergeR      | ,seerTartxE,tseroF |     |     |     |
noisiceD,senihcaM
|     |              |     |     |               |     |     | gninraeLemertxE |     |              |     | ,MTSL,elbmesne |     |
| --- | ------------ | --- | --- | ------------- | --- | --- | --------------- | --- | ------------ | --- | -------------- | --- |
|     | tseroFmodnaR |     |     | rotceVtroppuS |     |     |                 |     | ,MVS,tsooBGX |     |                |     |
citeneG,seerT
|     |            |     |     |     |          | ,tseroFmodnaR | citsigoL,eerT |     | tsooBadA-TE | krowtenlarueN | NNE-ETOMS |     |
| --- | ---------- | --- | --- | --- | -------- | ------------- | ------------- | --- | ----------- | ------------- | --------- | --- |
|     | desUsledoM |     |     |     | skrowteN |               |               |     |             |               | ,tsooBadA |     |
dohteM
|     | repaPehtfoemehT |                  |                |                 |                | rofsmhtiroglaLD |                 |              |                                 |                 |                 |             |
| --- | --------------- | ---------------- | -------------- | --------------- | -------------- | --------------- | --------------- | ------------ | ------------------------------- | --------------- | --------------- | ----------- |
|     | serapmoc,ledom  | erutaefsetaulave |                | gninraelenihcam |                | dnaLMfoesuehT   | duarfdractiderc |              | ehtniseuqinhcet duarfdractiderc |                 | agnisunoitceted |             |
|     |                 |                  | nodesabsdohteM |                 |                |                 | fonoitcetedeht  |              |                                 | duarfdractiderC | krowtenlaruen   |             |
|     |                 |                  |                | ehtotdeilppa    | duarflaicnanfi |                 |                 | LMfoycacfife |                                 |                 | dnaelbmesne     |             |
|     | elbaterpretni   | gnilpmasrevo     |                |                 |                |                 |                 |              | fonoitceted                     |                 |                 |             |
|     |                 | ,smhtirogla      |                | fomelborp       |                |                 |                 | ehtgnissessA |                                 |                 |                 | gnireenigne |
noitceted
noitceles sdohtem
|     | dnaelbatS   |     |     |              |     |                |     |               |     |                |     | erutaef |
| --- | ----------- | --- | --- | ------------ | --- | -------------- | --- | ------------- | --- | -------------- | --- | ------- |
|     |             |     |     |              |     | ,01,sseccAEEEI |     |               |     | ,01,sseccAEEEI |     |         |
|     | 1202,erauqS |     |     | ,841,ecneicS |     |                |     | ,9,sseccAEEEI |     |                |     |         |
retupmoC
dnalanruoJ noitacilbuP
aidecorP
| foetaD | hcraeeR                                 |     |                       | 9102               |     | 2202          |                                   | 1202                      |                     |                     | 2202                      |           |
| ------ | --------------------------------------- | --- | --------------------- | ------------------ | --- | ------------- | --------------------------------- | ------------------------- | ------------------- | ------------------- | ------------------------- | --------- |
|        | &,.R,eY,.Z,uiL                          |     |                       |                    |     |               | ,demhA&,.M                        |                           |                     |                     | ,.D.I,eyneiM &,.K,abelurA |           |
|        |                                         |     | ,leaS,.I,ilagdaS      |                    |     |               | ,.U.H,nahK ,mallasumlA ,nazmaR,.N | ,nuS,.E,irebelI ,gnaW&,.Y |                     |                     | ,.G.T,trawS               |           |
|        |                                         |     |                       | ,uobbaneB          |     | ,.K.F,jafralA |                                   |                           |                     | ,.E,ohgonesE        |                           | .G,odiabO |
|        | 21.R,eY                                 |     |                       |                    |     | ,.I,kilaM     |                                   |                           |                     |                     |                           |           |
|        | srohtuA                                 |     |                       | &,.N               |     |               |                                   |                           |                     |                     |                           |           |
|        |                                         |     |                       | 61.F               |     |               |                                   | 81.M                      | 91.Z                |                     |                           |           |
|        |                                         |     |                       |                    |     |               |                                   |                           | draCtiderCgnitceteD |                     | decnahnErofelbmesnE       |           |
|        | htiwduarFtnemetatS enihcaMelbaterpretnI |     | fosisylanAecnamrofreP | tiderCnismhtiroglA |     |               | dnagninraeLenihcaM                | desaB-tsooBadAdna         |                     |                     |                           |           |
|        |                                         |     |                       |                    |     |               |                                   | ETOMSfotnemssessA         |                     | dereenignE-erutaeFA |                           |           |
duarFdraCtiderC
|     |                    |     |     | gninraeLenihcaM |              |                                |                  |     | gninraeLenihcaM |     | krowteNlarueN |              |
| --- | ------------------ | --- | --- | --------------- | ------------ | ------------------------------ | ---------------- | --- | --------------- | --- | ------------- | ------------ |
|     | laicnaniFgnitceteD |     |     |                 |              | duarFdraCtiderC gnisUnoitceteD | trA-eht-fo-etatS |     |                 |     |               |              |
|     |                    |     |     |                 |              |                                | gninraeLpeeD     |     | rofseuqinhceT   |     |               |              |
|     |                    |     |     |                 | 61.noitceteD |                                | 81.smhtiroglA    |     |                 |     |               | 02.noitceteD |
duarFsdraC
21.gninraeL
91.duarF
eltiT
.1 elbaT
onS
|     | 1   |     | 2   |     |     | 3   |     | 4   |     | 5   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

56 IntelligentDecisionTechnologies19(1)
Figure 1. Architectureoftheproposedmethodology.
explainable AI. The goal is to strengthen defences and provide stakeholders with interpretable information to combat
financialcrime.27
3.1 Dataset description and data preprocessing
Withthisdataset,wewanttoaddressaknowledgevacuuminpubliclyavailablefinancialservicesdatasets,withafocuson
mobilemoneytransactionsasarelativelyyoungindustry.Manyreal-worlddatasetsarenotavailabletothepublicbecause
ofthesensitivenatureoffinancialtransactions.28Togetaroundthisconstraint,thedatasetisartificiallyconstructedusing
a simulator called PaySim. To simulate mobile money transactions, PaySim uses a subset of real transactions extracted
fromaprovider’smonthlyfinancialdata.Amultinationalfirmisnowrunningthemobilebankingserviceinmorethan14
countriesacrosstheworld,andtheyaretheoneswhoprovidedtheinitiallogs.
TheSwedishKnowledgeFoundation(grant:20140032)issupportingthestudy“Scalableresource-efficientsolutions
for big data analytics,” which includes this dataset.29 The dataset encompasses a comprehensive 6,362,620 records, of
which6,354,407arevalidtransactions,constituting99.87%,and8213arefraudulenttransactions,amountingto0.13%.
Among the flagged transactions, totaling 16, all fall under the “TRANSFER” type and are marked as fraudulent. The
transactionamountsinthissubsetrangefrom353,874.22to10,000,000.0.
Inthispreliminaryphase,wecommencebyimportingessentiallibrariesandconductingacomprehensiveexamination
ofthedataset.Ourinitialfocusinvolvesscrutinizingforanymissingdataanddelvingintothedistributionpatternsofboth
validandfraudulenttransactions,establishingafoundationalunderstandingforsubsequentpreprocessingsteps.
In addition, we enhance our exploratory analysis through data visualization techniques, enabling a more insightful
understandingofthedataset’scharacteristicsandaidingintheidentificationofpatternsortrendsthatmayinfluencethe
subsequentmodelingprocess.Figure2presentsapiechartillustratingthedistributionoftransactiontypes,revealingthat
TransferTransactionsconstitute19%,whileCashOutTransactionsdominatethemajoritywithan81%representation.
In Figure 3, a bar graph delineates the total monetary value associated with each transaction type. Cash Out trans-
actions exhibit a substantial total amount of 394,412,995,224, while Transfer transactions surpass with a total amount
of 485,291,987,263, offering a comprehensive visual representation of the financial magnitudes associated with each
transactioncategory.InFigure4,abargraphmeticulouslyportraystheincidenceoffraudulenttransactionswithineach
transactiontype.Notably,CashOuttransactionsaccountfor223,750instances,whileTransfertransactionsrevealahigher
frequency with 532,909 cases, providing a nuanced insight into the distribution of fraudulent activities across different
transactioncategories.
Tofortifytherobustnessofouranalysis,wediligentlyaddresspotentialimbalancesinherentinthedataset.Moreover,
we meticulously investigate and rectify disparities in balances at both the origin and destination following transactions.

VijayanandandSmrithy 57
Figure 2. Piechartofratiooftransactiontypes.
Figure 3. Totalamounttransactedineachtransactiontype.

58 IntelligentDecisionTechnologies19(1)
Figure 4. Fraudulenttransactionstypes-cashoutandtransfer.
Theidentificationandanalysisoftransactionswithamountslessthanorequaltozerooffervaluableinsightsintopotential
anomaliesthatmayimpactthemodel’sperformance.Table2showsdifferentattributesofthedataset.
3.2 Feature engineering
Followingtheinitialexploratoryphase,wetransitiontoameticulousfeatureengineeringprocesstoenhancethedataset’s
suitability for machine learning model training. Begin with the 11 columns that make up the original features: “step,”
“type,”“amount,”“nameOrig,”“oldbalanceOrg,”“newbalanceOrig,”“nameDest,”“oldbalanceDest,”“newbalanceDest,”
“isFraud,” and “isFlaggedFraud.” Then we go on to the current features. Unwanted features such as “step,” “type,”
“nameOrig,”“nameDest,”“error_orig,”“error_dest,”and“isFlaggedFraud”aresubsequentlyremovedtostreamlinethe
dataset.
Toensureuniformity,continuousvalueswithinthecolumns“amount,”“oldbalanceOrg,”“oldbalanceDest,”“newbal-
anceOrig,” and “newbalanceDest” are standardized to fall within the 0 to 1 range using the StandardScaler. One of the
mostimportantstepsingettingdatareadytotrainmachinelearningmodelsisemployingthe‘traintestsplit’approachto
dividetheresultantdatasetintoseveralsets:trainingandtesting.Tomakesurethesplitisacceptable,welookatthesize
ofthetrainingandtestingsets.
Additionally, we conduct checks for missing values in the target variable, “isFraud,” and address them by dropping
rows with missing values. After cleaning the data, it is divided into two sets: one for testing and one for training. The
stratification is kept and the test size is set at 20%. The final dimensions of the split datasets are verified to confirm the
successfulcompletionofthepreprocessingsteps.

VijayanandandSmrithy 59
Table 2. Detailedinformationofthedatasetattributes
Attribute Description DataType
step Areal-worldtimemeasurewhereonestepisequivalenttoonehour. int64
type TypeofTransaction:Transfer,Debit,Payment,Cash-In,Cash-Out. object
amount Thetransactionamountexpressedinlocalcurrency. float64
nameOrig Transactionstartedbythecustomer. object
oldbalanceOrg Startingbalancepriortothetransaction. float64
newbalanceOrig Newbalancefollowingthetransaction. float64
nameDest Customerreceivingthetransaction. object
oldbalanceDest Therecipient’sstartingbalancepriortothetransaction. float64
newbalanceDest Therecipient’snewbalancefollowingthetransaction. float64
isFraud Fortransactionscarriedoutbyfraudulentagentsinthesimulation,abinaryindicator(1or0). int64
isFlaggedFraud Asignalthatsuggestsattemptstosendmorethan$200,000inasingletransaction. int64
3.3 Classification models
Oneofthemostimportantusesofmachinelearningisfrauddetection,wherechoosingtherightmodelmayhaveahuge
impact on efficiency. In this study, we dive headfirst into the complex world of fraud detection and analyse six well-
known machine learning models: Neural Network, XGBoost, Decision Tree, Random Forest, and Logistic Regression.
Theresearchaimstoprovideadetailedandthoroughknowledgeofeachmodel’seffectivenessandsuitabilityforhandling
theintricaciesoffrauddetectionbycarefullyusingseveralperformanceindicators,suchasaccuracy,F1score,confusion
matrix,andROCAUCscore.
3.3.1 Logistic regression. David Cox developed the basic technique for creating a logistic model (sometimes called the
logitmodel)in1958andnameditlogisticregression.Duetoitsconnectiontologisticdatadistribution,itsprimarybenefit
isthatitcanbeappliedtobothclassprobabilityestimationandclassification.Itappliesanonlinearsigmoidalfunctionas
showninequation1onalinearcombinationoffeatures.30
S(x)=1÷(1+e (−x)) (1)
Logisticregressionisbotharobustandflexiblemethodfordichotomousclassificationprediction,whichinvolvesmaking
predictionsforstatesoroutcomesthatmayberepresentedasyes/no,success/failure,orwilloccur/willnotoccur.31 Since
the classes in a supervised classification issue are discrete, the goal of the methods is to find the decision boundaries
betweenthem.32
3.3.2 Decisiontree. Whenitcomestosupervisedlearning,decisiontreesarethewaytogo.33Toaidindecision-making,
decision trees use a tree structure that mimics human brain processes.33 Attribute selection as the decision tree’s root
nodeisthefirststep.33 Additionally,foreachsingleattributevalue,itcreatesabranchandsplitstheinstanceintomany
subgroups. Thirdly, there is a connection to a branch from the root node in each subset.34 With each branch completed,
thealgorithmrepeatedlycontinuestheprocess.35
3.3.3 Randomforest. Whenitcomestocategorization,theRandomForest(RF)algorithmisamongthetopoptions.RF
iscapableofproperlycategorizingmassivevolumesofdata.Thismethodoflearninginvolvestrainingalargenumberof
decision trees,with thegoal of having each treeanticipate themodal outputs.36 According to,36 RFuses random vector
valuesforeachtreeasitspredictors.Thebasicpremiseisthatagroupof“weaklearners”mayworktogethertocreatea
“stronglearner."36–40
3.3.4 XGBoost. An implementation of Gradient Boosting that makes use of gradients derived from decision trees is
knownasExtremeGradientBoosting(XGBoost).Iteratively,itbuildssimple,briefdecisiontrees.Becauseofitsextreme
bias,everytreeisreferredtoasa“weaklearner.”XGBooststartsbyconstructingthefirst,mostbasictree,whichperforms
poorly. After then, it creates a second tree that is trained to predict actions that the previous tree—a poor learner—was
unable to do. The method generates progressively weaker learners, each of them fixing the preceding tree before the
stoppingcondition—forexample,thequantityoftrees(estimators)thatneedtobeproduced—issatisfied.XGBoostoffers
furtherbenefits:Trainingisquickandcanbesplitupordividedamongmultipleclusters.41,42

| 60  |     |     | IntelligentDecisionTechnologies19(1) |     |     |
| --- | --- | --- | ------------------------------------ | --- | --- |
Table 3. Crossvalidationresultsonaccuracy(%)
| Model              | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 |
| ------------------ | ----- | ----- | ----- | ----- | ----- |
| Logisticregression | 99.82 | 99.83 | 99.81 | 99.82 | 99.83 |
| DecisionTree       | 99.94 | 99.93 | 99.94 | 99.93 | 99.94 |
| RandomForest       | 99.92 | 99.92 | 99.92 | 99.93 | 99.92 |
| XGBoost            | 99.91 | 99.90 | 99.91 | 99.90 | 99.92 |
| LightGBM           | 99.75 | 99.75 | 99.75 | 99.76 | 99.76 |
| NeuralNetwork      | 99.86 | 99.85 | 99.85 | 99.87 | 99.85 |
Table 4. CrossvalidationresultsonF1scores
| Model              | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 |
| ------------------ | ----- | ----- | ----- | ----- | ----- |
| Logisticregression | 0.60  | 0.62  | 0.61  | 0.60  | 0.60  |
| DecisionTree       | 0.89  | 0.90  | 0.89  | 0.90  | 0.89  |
| RandomForest       | 0.86  | 0.85  | 0.85  | 0.85  | 0.86  |
| XGBoost            | 0.83  | 0.83  | 0.82  | 0.83  | 0.83  |
| LightGBM           | 0.51  | 0.50  | 0.51  | 0.50  | 0.50  |
| NeuralNetwork      | 0.68  | 0.68  | 0.69  | 0.68  | 0.68  |
Table 5. CrossvalidationresultsonROCAUCscores
| Model              | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 |
| ------------------ | ----- | ----- | ----- | ----- | ----- |
| Logisticregression | 0.98  | 0.98  | 0.97  | 0.98  | 0.98  |
| DecisionTree       | 0.94  | 0.94  | 0.94  | 0.94  | 0.94  |
| RandomForest       | 0.99  | 0.99  | 0.99  | 0.99  | 0.99  |
| XGBoost            | 0.99  | 0.99  | 0.99  | 0.99  | 0.99  |
| LightGBM           | 0.64  | 0.64  | 0.64  | 0.64  | 0.65  |
| NeuralNetwork      | 0.98  | 0.98  | 0.98  | 0.98  | 0.98  |
3.3.5 LightGBM. LightGBMisaframeworkforgradientboostingthatmakesuseoftechniquesfortree-basedlearning.
Thefollowingadvantagesareachievedbyitsefficientdistribution:quickertrainingspeed,lessmemoryuse,higheraccu-
racy,supportforGPU,distributed,andparallellearning,andbetterefficiencyoverall.43 Manyboostingprogramsemploy
pre-sort-based algorithms for decision tree learning, such XGBoost’s default approach.44,45 It is not easy to optimize,
histograms,46–48
despite being a straightforward solution. LightGBM uses methods that are based on which divide the
valuesofcontinuousfeatures(attributes)intodiscretebins.Thisdecreasesmemoryuseandspeedsuptraining.49
3.3.6 Neuralnetwork. Neuralnetworks(NNs)andartificialneuralnetworks(ANNs)aretwonamesforthesamekindof
AImodelthatattemptstosimulatebrainactivity.Inthe1990s,theywerepresentedasadifferentapproachtoaddressgeo-
graphicissues,andmorerecently,theyhavegrownbecauseofdevelopmentsincomputerpower,artificialintelligence,and
dataavailability,amongotherareas.50NeuralNetworkscanlearncomplexnonlinearrelationshipsusingtrainingexample
sets.Theyworkparticularlyeffectivelyinpatternidentificationscenarioswherecomplextrendsinhigh-dimensionaldata
needtobeidentified.51
AstratifiedK-Foldcrossvalidationwasperformedtoensurethereliabilityandrobustnessoftheexperiments.Tables3,
4 and 5 show the cross validation results of various models on the metrics accuracy, F1 score and ROC AUC scores
respectively. We summarize the average performance characteristics of our machine learning models for classification
in Table 6, providing a thorough understanding of their efficacy. Accuracy, F1 score, and ROC AUC score are some of
themostimportantmetricsthatrevealthemodels’overallclassificationaccuracy,precision-recallbalance,andabilityto
discernbetweenpositiveandnegativeexamples.
Additionally,Friedman’sstatisticaltestisusedtocomparetheperformanceofdifferentmodels.Theresultingp-value
is 0.000139 which is significantly less than the significance level 0.05 indicating that there are significant differences
betweentheperformancesofthemodels.TheNemenyipost-hoctestprovidespairwisecomparisonsbetweenthemodels.
Table7showsthep-valuesforthecomparisons.

| VijayanandandSmrithy |     |     |     |     |     | 61  |
| -------------------- | --- | --- | --- | --- | --- | --- |
Table 6. Performancemetricsofclassificationmachinelearningmodels
| Machine/Deep          |     | Accuracy(%)ofthe |     | F1Scoreofthe | ROCAUCScoreofthe |     |
| --------------------- | --- | ---------------- | --- | ------------ | ---------------- | --- |
| LearningModel         |     | ML/DLModel       |     | ML/DLModel   | ML/DLModel       |     |
| LogisticRegression.30 |     | 99.826           |     | 0.606        | 0.978            |     |
| DecisionTree.33       |     | 99.937           |     | 0.893        | 0.943            |     |
| RandomForest.36       |     | 99.922           |     | 0.855        | 0.996            |     |
| XGBoost.41,42         |     | 99.908           |     | 0.829        | 0.990            |     |
LightGBM.49
|                     |     | 99.753 |     | 0.507 | 0.641 |     |
| ------------------- | --- | ------ | --- | ----- | ----- | --- |
| NeuralNetwork.50,51 |     | 99.855 |     | 0.682 | 0.983 |     |
Table 7. NemenyiPost-HocTestResults
|     | 0        | 1        | 2        | 3        | 4        | 5        |
| --- | -------- | -------- | -------- | -------- | -------- | -------- |
| 0   | 1.000000 | 0.009434 | 0.114066 | 0.532706 | 0.900000 | 0.900000 |
| 1   | 0.009434 | 1.000000 | 0.900000 | 0.532706 | 0.001000 | 0.114066 |
| 2   | 0.114066 | 0.900000 | 1.000000 | 0.900000 | 0.009434 | 0.532706 |
| 3   | 0.532706 | 0.532706 | 0.900000 | 1.000000 | 0.114066 | 0.900000 |
| 4   | 0.900000 | 0.001000 | 0.009434 | 0.114066 | 1.000000 | 0.532706 |
| 5   | 0.900000 | 0.114066 | 0.532706 | 0.900000 | 0.532706 | 1.000000 |
Table 8. Crossvalidationresultsofensemblelearningclassifier
| Metrics     |     | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 |
| ----------- | --- | ----- | ----- | ----- | ----- | ----- |
| Accuracy    |     | 99.90 | 99.91 | 99.90 | 99.90 | 99.92 |
| F1Score     |     | 0.81  | 0.82  | 0.81  | 0.81  | 0.82  |
| ROCAUCScore |     | 0.99  | 0.99  | 0.99  | 0.99  | 0.99  |
TheresultssuggestthatcertainmodelssuchasLogisticRegression,DecisionTrees,RandomForest,LightGBMhave
performancedifferencesthatarestatisticallysignificant.
| 4 Ensemble | learning | model- voting | classifier |     |     |     |
| ---------- | -------- | ------------- | ---------- | --- | --- | --- |
When solving tasks like classification, ensemble learning uses a combination of many learning models that have been
deliberatelygenerated.52 Thisisbasedonthenotionthattwomindsarepreferabletoone.Additionally,wegatherinfor-
mation from various sources and rank or combine them in order to make strategic judgments. A supervised learning
algorithm is an ensemble in and of itself. Many classifier systems are another name for ensemble learning systems.32
Usingthesamedatatotrainseveralmodelsandthencombiningtheirpredictionsisknownasensemblelearning.53
The
goal of ensemble learning is to improve performance above that of a single model by combining many models into a
singleensemble.53 Thefirststepistodeterminehowtobuildtheensemblemodels,andthesecondistofigureouthowto
aggregatetheforecastsofeachmemberoftheensemble.Onewaytomakepredictionsmoreaccurateistouseensemble
learning.54
This instance makes use of a meta classifier, which is able to merge prediction models from different or comparable
machine learning datasets by means of a majority vote or soft voting. To choose the most likely class, soft voting aver-
ages the base models’ class pseudo-probabilities.55 The voting classifier outperforms the other baseline models because
to its ability to incorporate the predictions of many ML and DL models.56 Figure 5 illustrates our proposed ensemble
model, a culmination of various classifiers aimed at elevating predictive performance through strategic combination. A
number of classifiers—including XGBoost, LightBGM, Neural Networks, Decision Tree Classifier, and Random Forest
Classifier—arepartofthisensemble.Table8showstheStratifiedK-Foldcrossvalidationresultsoftheensemblelearning
model.
Table9providestheaveragesummaryoftheperformancemetricsoftheensemblelearningmodel,withafocusonaccu-
racy,F1score,andROCAUCscore.Thecollectiveassessmenthighlightsthemodel’sexceptionalaccuracyof99.904%,
underscoringitsefficacyacrossdiverseclassificationscenarios.

62 IntelligentDecisionTechnologies19(1)
Figure 5. Proposedensemblemodel.
Table 9. Performancemeasureofensemblelearningclassifier
Accuracy(%)oftheModel F1ScoreoftheModel ROCAUCScoreoftheModel
EnsembleLearningModel 99.904 0.814 0.990
Figure 6. ProcessofexplainableAI.
5 Explainable AI
Coined by DARPA in 2016, Explainable AI (XAI) addresses the need for transparency in AI systems, countering the
‘blackbox’natureofmachinelearning.Crucialindelicatefieldslikehealthcareandbanking,XAIseekstoensurethatAI
systemsaretransparentandeasytointerpret.Usingwhite-boxmodelssuchasConceptBottleneckModels,XAIjustifies
decisions,promotingtrustandfacilitatingusercomprehension.Symbolicregressionisproposedforsupervisedmachine
learningtoensuretransparencyandauditability.Overall,XAIseekstodemystifyAIdecisions,enhancingusertrustand
understanding.57–60
InFigure6,wecanseehowtherequirementsorapplicationdomaindictatetheinputdatausedtotrainthemodels,the
predictionapproachthatisselected,andtheXAImethodsthatareusedtoexplainthemodels’innerworkingsandoutput

VijayanandandSmrithy 63
Table 10. Averageimpactofattributesonmodeloutput
Attribute MeanSHAPValue
OldBalanceOrg 0.065
NewBalanceOrg 0.055
Amount 0.04
NewBlanceDest 0.03
OldBalanceDest 0.03
Figure 7. MeanSHAPvalue(averageimpactofattributeonmodeloutput).
viaanexplanationinterface.57BecauseweareawareofExplainableAI’sresults,wewillbemoreconfidentinAImodels.
Userscanenhancethemodel’saccuracyandidentifyitsshortcomingsbyusingtheoutputinformation.Theendeffectwill
bethatconsumersarebetterabletodecidehowtoenhancethemodel.61
Inthisstudy,weinterpretmachinelearningmodeloutputusingSHAP,acommonexplainabilitytechniqueutilizedin
ExplainableAI(XAI).Basically,SHAPfunctionsasa“featureattributionmethod”.62Similartoagametheoryapproach,
SHAPenhancesthereadabilityofeachpredictionindependentlybydeterminingtheimportancevaluesforeachattribute.
ThreeimportantattributesmakeuptheaggregatedegreeoffeatureimportancemaintainedbytheSHAPvalues:“Missing-
ness,accuracy,andconsistency”.Intermsofinterpretation,SHAPismoreintuitiveandsimplertocompute.63Inaddition
tobeingmodel-agnostic,itprovidesexplanationsthatarebothlocalandglobalandismoredependablewhendealingwith
anykindofdata.Inordertoempowerplayersaccordingtotheirlevelofparticipation,weemployShapleyvalues,which
adhere to the four axioms of player engagement: “Efficiency, Symmetry, Dummy, Additive”.64 Shapley first coined the
termSHAPin1951.Itisusedtodescribeacertainoutputdependingonhoweachinputisinvolvedinaprediction.
Table 10, along with Figures 7 and 8, unveils the mean SHAP values, shedding light on the pivotal role of selected
attributeswithintheframeworkofapredictivemodel.TheutilizationofSHAPvaluesfacilitatesanuancedunderstanding
ofeachattribute’scontributiontothemodel’soutput.Remarkably,theOldBalanceOrgattributetakesprecedencewiththe
highest mean SHAP value of 0.065, signifying its discernibly stronger impact on the model’s predictive outcomes. By
givingaquantifiablemeasureofattributeimpactandprovidinginsightintothemodel’sdecision-makingprocesses,these
valuesimprovetheinterpretabilityandunderstandingoffeaturesignificance.65
6 Result
The assessment of individual machine learning models underscores their exceptional performance in detecting financial
fraud,withtheDecisionTreemodelshowcasingremarkableresults.AnF1Scoreof0.893,aROCAUCScoreof0.943,
andamaximumaccuracyof99.937percentdistinguishtheDecisionTreemodelasthebestperformeramongthemodels
thatwereevaluated.

64 IntelligentDecisionTechnologies19(1)
Figure 8. SHAPvalueandfeaturevalue.
Witha99.904%accuracyrate,anF1Scoreof0.814,andaremarkableROCAUCScoreof0.990,theEnsembleLearn-
ing Model—implemented via a Voting Classifier—demonstrates itself as a strong solution. This collective performance
underscorestheefficacyofamalgamatingdiversemodelsforenhancedfrauddetection.
Todelveintotheinterpretabilityofthesemodels,athoroughSHAPanalysiswasconducted,revealingkeyattributesand
theirmeanSHAPvalues.ParticularlynoteworthywereattributessuchasOldBalanceOrg,NewBalanceOrg,Amount,New-
BlanceDest,andOldBalanceDest,whichexhibitedsignificantimpactsonmodeloutputs.Theseinsightsprovidevaluable
claritytostakeholders,fosteringadeeperunderstandingofthemodels’decision-makingprocessesandtherebyaugmenting
transparencyandinterpretabilityintherealmoffinancialfrauddetection.
7 Conclusion
Inthisresearch,wetackledthegrowingchallengesinfinancialtechnology,specificallyaddressingtherisingthreatoffraud
inmobilemoneytransactions.Whiledigitalfinancebringsconvenience,italsoexposesinstitutionstosophisticatedfraud.
OurstudyemphasizedbothhighmodelaccuracyandexplainabilitybyintegratingmachinelearningwithExplainableAI,
leveragingSHAPanalysis.Thisworknotonlyadvances fraudpreventionindigitalfinancebutalsosetsaprecedentfor
transparent and interpretable machine learning systems. By prioritizing clarity, it empowers stakeholders with effective
decision-makingtoolsintheevolvingcybersecuritylandscape,markingasignificantstrideagainstfinancialfraudinthe
digitalera.
8 Future work
Thefutureoffinancialfrauddetectionandpreventioninvolvesintegratingcutting-edgetechnologiestocombatsophisti-
catedfraudschemes.Keyadvancementsincludethedevelopmentofreal-timeanalysisandadaptivesystemsfordynamic
threat response, the use of behavioral biometrics for enhanced user recognition, blockchain technology for immutable
andtransparentledgers,quantum-resistantencryptionmethods,collaborativethreatintelligencesharing,theexamination
ofnon-financialdataforcontextualinsights,regulatorycompliancesolutionsleveragingadvancedtechnologies,andAI-
driven user authentication processes. These innovations aim to create more resilient and intelligent systems, crucial for
stayingaheadintheever-evolvinglandscapeofdigitalfinance.
Statementsanddeclarations
Ethicalapproval
Informedconsent
Funding
Theauthorsreceivednofinancialsupportfortheresearch,authorship,and/orpublicationofthisarticle.

VijayanandandSmrithy 65
Declarationofconflictinginterests
Theauthorsdeclarednopotentialconflictsofinterestwithrespecttotheresearch,authorship,and/orpublicationofthisarticle.
References
1. https://www.acfe.com/about-the-acfe/newsroom-for-media/press-releases/press-release-detail?s=ACFE-Estimates-Organizations-
Lose-5-percent-to-Fraud
2. https://www.statista.com/outlook/dmo/fintech/digital-payments/worldwide
3. https://cybersecurityventures.com/cybercrime-damages-6-trillion-by-2021/
4. https://www.europol.europa.eu/cms/sites/default/files/documents/Spotlight-Report_Online-fraud-schemes.pdf
5. https://risk.lexisnexis.com/about-us/press-room/press-release/20221116-study-finds-fraud-costs
6. https://www.forbes.com/sites/louiscolumbus/2020/10/31/the-state-of-ai-adoption-in-financial-services/?sh=739a49282aac
7. HallPandGillN.Anintroductiontomachinelearninginterpretability.Sebastopol,CA:O’ReillyMedia,Incorporated,2019.
8. AliA,AbdRazakS,OthmanSH,etal.Financialfrauddetectionbasedonmachinelearning:asystematicliteraturereview.Appl
Sci2022;12:9637.
9. Al-HashediKGandMagalingamP.Financialfrauddetectionapplyingdataminingtechniques:acomprehensivereviewfrom2009
to2019.ComputSciRev2021;40:100402.
10. WickramanayakeB,GeeganageDK,OuyangC,etal.Asurveyofonlinecardpaymentfrauddetectionusingdatamining-based
methods.arXivpreprintarXiv:2011.14024(2020).
11. SenguptaKandDasPK.Detectionoffinancialfraud:comparisonsofsometree-basedmachinelearningapproaches.JDataInf
Manag2023;5:23–37.
12. LiuZ,YeRandYeR.Detectingfinancialstatementfraudwithinterpretablemachinelearning,2021.
13. HilalW,GadsdenSAandYawneyJ.Financialfraud:areviewofanomalydetectiontechniquesandrecentadvances.ExpertSyst
Appl2022;193:116429.
14. MittalSandTyagiS.Computationaltechniquesforreal-timecreditcardfrauddetection.Handbookofcomputernetworksand
cybersecurity:principlesandparadigms,2020,pp.653–681.
15. GuptaBB,PerezGM,AgrawalDP,etal.Handbookofcomputernetworksandcybersecurity.Springer2020;10:978–973.
16. SadgaliI,SaelNandBenabbouF.Performanceofmachinelearningtechniquesinthedetectionoffinancialfrauds.ProcComput
Sci2019;148:45–54.
17. AlghofailiY,AlbattahAandRassamMA.AfinancialfrauddetectionmodelbasedonLSTMdeeplearningtechnique.JAppl
SecurRes2020;15:498–516.
18. Alarfaj FK, Malik I, Khan HU, et al. Credit card fraud detection using state-of-the-art machine learning and deep learning
algorithms.IEEEAccess2022;10:39700–39715.
19. IleberiE,SunYandWangZ.PerformanceevaluationofmachinelearningmethodsforcreditcardfrauddetectionusingSMOTE
andAdaBoost.IEEEAccess2021;9:165286–165294.
20. Esenogho E, Mienye ID, Swart TG, et al. A neural network ensemble with feature engineering for improved credit card fraud
detection.IEEEAccess2022;10:16400–16407.
21. AlfaizNSandFatiSM.Enhancedcreditcardfrauddetectionmodelusingmachinelearning.Electronics2022;11:662.
22. AwosikaT,ShuklaRMandPranggonoB.Transparencyandprivacy:theroleofexplainableAIandfederatedlearninginfinancial
frauddetection.arXivpreprintarXiv:2312.13334,2023.
23. Jayasinghe SL, Thomas DT, Anderson JP, et al. Global application of regenerative agriculture: a review of definitions and
assessmentapproaches.Sustainability2023;15:15941.
24. SharmaN,ChakrabartiAandBalasVE.Datamanagement,analyticsandinnovation.ProcICDMAI2019;1:1–740.
25. https://bjs.ojp.gov/taxonomy/term/financial-fraud
26. https://www.itu.int/en/ITU-T/techwatch/Pages/mobile-money-standards.aspx#:∼:text=Mobile%20money%20refers%20to%20
financial,directly%20to%20a%20bank%20account
27. MunaRK,HossainMI,AlamMGR,etal.DemystifyingmachinelearningmodelsofmassiveIoTattackdetectionwithexplainable
AIforsustainableandsecurefuturesmartcities.IoT2023;24:100919.
28. GardnerC.Classifyingimbalancedfinancialfrauddatautilizingenhancedrandomforestalgorithm,2020.
29. Lopez-RojasEA,ElmirAandAxelssonS.PaySim:Afinancialmobilemoneysimulatorforfrauddetection.In:The28thEuropean
ModelingandSimulationSymposium-EMSS,Larnaca,Cyprus,2016.
30. AshendenSK,ed.Theeraofartificialintelligence,machinelearning,anddatascienceinthepharmaceuticalindustry. Cambridge,
MA:AcademicPress,2021.
31. SeufertEB.Thefreemiumbusinessmodel.FreemiumEconomics,2014,pp.1–27.
32. GudivadaVN,IrfanMT,FathiE,etal.Cognitiveanalytics:goingbeyondbigdataanalyticsandmachinelearning.In:Handbook
ofstatistics.Vol.35.Amsterdam,Netherlands:Elsevier,2016,pp.169–205.

66 IntelligentDecisionTechnologies19(1)
33. AlMamunMHandKeikhosrokianiP.Predictingonset(type-2)ofdiabetesfrommedicalrecordsusingbinaryclassclassification.
In:Bigdataanalyticsforhealthcare.Cambridge,MA:AcademicPress,2022,pp.301–312.
34. Keikhosrokiani P, ed. Big data analytics for healthcare: datasets, techniques, life cycles, management, and applications.
Cambridge,MA:AcademicPress,2022.
35. KohaviR.Scalinguptheaccuracyofnaive-bayesclassifiers:Adecision-treehybrid.InKdd,1996,August,Vol.96,pp.202–207.
36. ChatterjeeA,BalaP,GedamS,etal.Machinelearninganddeeplearning-basedadvancedclassificationtechniquesforthedetection
ofmajordepressivedisorder.AslibJInfManag2023.
37. Mishra A and Suhas MV. Classification of benign and malignant bone lesions on CT images using random forest. In 2016
IEEEinternationalconferenceonrecenttrendsinelectronics,Information&CommunicationTechnology(RTEICT),2016,May,
pp.1807–1810).IEEE.
38. Chu G, Lo P, Ramakrishna B, et al. Bone tumor segmentation on bone scans using context information and random forests.
InMedicalImageComputingandComputer-AssistedIntervention–MICCAI2014:17thInternationalConference,Boston,MA,
USA,September14–18,2014,Proceedings,PartI17,2014,pp.601–608.SpringerInternationalPublishing.
39. NguyenC,WangYandNguyenHN.Randomforestclassifiercombinedwithfeatureselectionforbreastcancerdiagnosisand
prognostic.2013.
40. ShrivastavaD,SanyalS,MajiAK,etal.Bonecancerdetectionusingmachinelearningtechniques.In:Smarthealthcarefordisease
diagnosisandprevention.Cambridge,MA:AcademicPress,2020,pp.175–183.
41. RamrajS,UzirN,SunilR,etal.ExperimentingXGBoostalgorithmforpredictionandclassificationofdifferentdatasets.IntJ
ControlTheoryAppl2016;9:651–662.
42. SubasiA,PanigrahiSS,PatilBS,etal.Advancedpatternrecognitiontoolsfordiseasediagnosis.In:5GIotandedgecomputing
forsmarthealthcare.Cambridge,MA:AcademicPress,2022,pp.195–229.
43. https://lightgbm.readthedocs.io/
44. Mehta M, Agrawal R and Rissanen J. SLIQ: A fast scalable classifier for data mining. In Advances in Database
Technology—EDBT’96:5thInternationalConferenceonExtendingDatabaseTechnologyAvignon,France,March25–29,1996
Proceedings5,1996,pp.18–32.SpringerBerlinHeidelberg.
45. ShaferJ,AgrawalRandMehtaM.SPRINT:Ascalableparallelclassifierfordatamining.InVldb,1996,September,Vol.96,
pp.544–555.
46. AlsabtiK,RankaSandSinghV.CLOUDS:Adecisiontreeclassifierforlargedatasets,1998.
47. JinRandAgrawalG.Communicationandmemoryefficientparalleldecisiontreeconstruction.InProceedingsofthe2003SIAM
internationalconferenceondatamining,2003,May,pp.119–129.SocietyforIndustrialandAppliedMathematics.
48. LiP,WuQandBurgesC.Mcrank:Learningtorankusingmultipleclassificationandgradientboosting.AdvNeurInfProcessSyst
2007;20:897–904.
49. https://lightgbm.readthedocs.io/en/latest/README.html
50. KobayashiA.Internationalencyclopediaofhumangeography.Amsterdam,Netherlands:Elsevier,2019.
51. Guenther FH. Neural networks: Biological models and applications. Oxford: International Encyclopedia of the Social &
BehavioralSciences,2001,pp.10534–10537.
52. PolikarR.Ensemblelearning.Ensemblemachinelearning:Methodsandapplications,2012,pp.1–34.
53. BENNOUHRandOussamaAIADI.Ahealthcaresystemusingdeeplearning(Doctoraldissertation),2022.
54. SchneiderPandXhafaF.AnomalydetectionandcomplexeventprocessingoverIoTdatastreams:withapplicationtoEHealth
andpatientdatamonitoring.Cambridge,MA:AcademicPress,2022.
55. ManconiA,ArmanoG,GnocchiM,etal.Asoft-votingensembleclassifierfordetectingpatientsaffectedbyCOVID-19.ApplSci
2022;12:7554.
56. AftabiSZ,AhmadiAandFarziS.FrauddetectioninfinancialstatementsusingdataminingandGANmodels.ExpertSystAppl
2023;227:120144.
57. Saranya A and Subhashini R. A systematic review of Explainable Artificial Intelligence models and applications: recent
developmentsandfuturetrends.DecisAnalJ2023:100230.
58. https://www.darpa.mil/program/explainable-artificial-intelligence
59. https://onlinelibrary.wiley.com/toc/26895595/2021/2/4
60. https://xaitk.org/
61. https://higherlogicdownload.s3.amazonaws.com/ISACA/71336a0d-5200-45d1-ba3d-b1b5116f8456/UploadedImages/2023_
Documents/ISACA_KE_Newsletter_2023_Edition.pdf
62. VandenBroeckG,LykovA,SchleichM,etal.OnthetractabilityofSHAPexplanations.JArtifIntellRes2022;74:851–886.
63. Linardatos P, Papastefanopoulos V and Kotsiantis S. Explainable AI: a review of machine learning interpretability methods.
Entropy2021;23:18.

VijayanandandSmrithy 67
64. LohHW,OoiCP,SeoniS,etal.Applicationofexplainableartificialintelligenceforhealthcare:asystematicreviewofthelast
decade(2011–2022).ComputMethodsProgramsBiomed2022;226:107161.
65. KademM,NoseworthyMandDoyleT.XGBoostforinterpretableAlzheimer’sdecisionsupport.ProcAAAISymposSer2023;
1:135–141.