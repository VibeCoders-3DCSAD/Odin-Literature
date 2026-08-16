---
conversion_metadata:
  converted_at: "2026-07-21T13:55:24Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Lee J. et al.pdf"
  source_pdf_sha256: "62f18c100d67c78edb27b5950b647e9dda0997d910e6ac1755f0d0ad6e30c97b"
  page_count: 19
  markdown_char_count: 209695
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Medical Economics

ISSN: 1369-6998 (Print) 1941-837X (Online) Journal homepage: www.tandfonline.com/journals/tfocoll

Comparing deep learning and classical regression
approaches for predicting healthcare expenditure
and spending: a systematic review

John Tayu Lee, Melody Hsiao-San Yeh, Vincent Cheng-Sheng Li, Hsiao-Hui
Chen, Yi-Hsuan Liu, Yu-Chun Chen & David Bin-Chia Wu

To cite this article: John Tayu Lee, Melody Hsiao-San Yeh, Vincent Cheng-Sheng Li, Hsiao-
Hui Chen, Yi-Hsuan Liu, Yu-Chun Chen & David Bin-Chia Wu (2023) Comparing deep
learning and classical regression approaches for predicting healthcare expenditure
and spending: a systematic review, Journal of Medical Economics, 29:1, 654-671, DOI:
10.1080/13696998.2026.2630598

To link to this article:  https://doi.org/10.1080/13696998.2026.2630598

© 2026 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group

View supplementary material

Published online: 04 Mar 2026.

Submit your article to this journal

Article views: 640

View related articles

View Crossmark data

Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tfocoll

---

<!-- PAGE 2 -->

JOURNAL OF MEDICAL ECONOMICS
2026, VOL. 29, NO. 1, 654–671
https://doi.org/10.1080/13696998.2026.2630598
Article /2630598

ORIGINAL RESEARCH

Comparing deep learning and classical regression approaches for
predicting healthcare expenditure and spending: a systematic review

John Tayu Leea
Yi-Hsuan Liub

, Melody Hsiao-San Yeha

, Vincent Cheng-Sheng Lia

, Yu-Chun Chena and David Bin-Chia Wuc

, Hsiao-Hui Chena

,

aInstitute of Health Policy and Management, College of Public Health, National Taiwan University, Taipei, Taiwan; bMaster
Program of Statistics, National Taiwan University, Taipei, Taiwan; cSaw Swee Hock School of Public Health, National
University of Singapore, University Hall, Singapore

ARTICLE HISTORY
Received 11 December 2025
Revised 7 February 2026
Accepted 9 February 2026

KEYWORDS
Healthcare expenditure;
health spending; deep
learning; neural network;
predictive modeling; health
economics

JEL CODES
I13; I15; I28; H51

a

systematic

conducted

ABSTRACT
Aims: This study compares deep learning architectures with traditional regression and
tree-based models for individual-level healthcare cost prediction, with particular atten-
tion to performance differences across data contexts.
Methods: We
review (PROSPERO
preregistered
CRD420251129440). Web of Science, PubMed, Embase, and Scopus were searched
through August 2025. Eligible studies used real-world individual-level data (claims,
electronic health records, or registries) to predict cost-related outcomes with at least
one deep learning architecture and one classical regression comparator, and reported
quantitative performance. Data were extracted on population, predictors, outcome
horizon, model
type, validation strategy, performance metrics, calibration, and
interpretability.
Results: Eight studies met inclusion criteria, spanning the United States, Europe, and
Asia. In longitudinal designs—such as multi-year claims prediction and medication or
hospitalization time-series forecasting—sequential deep learning models, particularly
LSTM and CNN–LSTM hybrids, consistently outperformed regression and tree-based
algorithms. Reported gains included approximately 10–20% reductions in RMSE/MAE,
R2 improvements of 0.01–0.15, and AUROC values up to 0.78 for high-risk classifica-
tion. Across studies, prior costs and utilization were consistently the strongest predic-
In
tors, while social determinants and free-text features were rarely incorporated.
contrast, for low-dimensional, structured, cross-sectional medical data, generalized lin-
ear models and tree-based approaches remain robust baseline models due to their
interpretability and calibration stability.
Limitations: Evidence is based on a small and heterogeneous set of eight studies,
with limited external or temporal validation, short prediction horizons, and sparse
assessment of calibration, economic interpretability, and fairness, warranting cautious
interpretation.
Conclusions: Deep learning offers clear gains for longitudinal, sequence-rich cost fore-
casting, whereas tree-based methods remain highly competitive for cross-sectional
these findings are consistent with the proposed
tabular prediction. Overall,
Complexity–Performance Hypothesis, which posits that the predictive advantages of
deep learning emerge primarily when model capacity is well matched to data
complexity.

Introduction

Healthcare expenditures continue to rise globally, imposing escalating burdens on payers, governments,
and patients alike1–3. Accurate forecasts of individual and population-level health costs are crucial—not

CONTACT John Tayu Lee
Taiwan University, No. 17, Xu-Zhou Road, Zhongzheng District, Taipei, 100, Taiwan

johntayulee@ntu.edu.tw

Institute of Health Policy and Management, College of Public Health, National

Supplemental data for this article is available online at https://doi.org/10.1080/13696998.2026.2630598.

(cid:1) 2026 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group
This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivatives License (http://creativecommons.
org/licenses/by-nc-nd/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited,
and is not altered, transformed, or built upon in any way. The terms on which this article has been published allow the posting of the Accepted Manuscript in a
repository by the author(s) or with their consent.
www.tandfonline.com/ijme

---

<!-- PAGE 3 -->

JOURNAL OF MEDICAL ECONOMICS

655

only for academic modeling but also for practical applications in insurance underwriting, risk adjustment,
budget planning, and value-based payment strategies4. Traditional statistical approaches (e.g.
linear
models, generalized linear models, two-part models) frequently struggle to capture complex, nonlinear
interactions in health data and may underperform when faced with high-dimensional inputs5–7.

In recent years, deep learning and neural network architectures have garnered considerable attention
for their promise in modeling high-dimensional, heterogeneous data8,9. For example, Drewe-Boss et al.
(2022) applied a deep neural network to claims data of German insurees and demonstrated superior per-
formance over ridge regression in predicting next-year total healthcare costs10. Such applications under-
score the potential of neural networks to learn latent feature interactions, temporal patterns, and
nonlinearities that conventional models often miss7,8.

However, despite such advances, important methodological questions remain. It is still unclear how
extant studies differ in their policy or operational context, population and data sources, neural network
architectures and training strategies, sensitivity analyses, software platforms, and modes of result presen-
tation and interpretation11–13. Moreover, many papers provide limited comparisons between neural net-
work models and benchmark regression or machine learning alternatives, making it hard to judge when
neural networks truly add value11.

contributes

Healthcare expenditures are influenced by multiple interrelated factors. Demographic composition,
to a growing demand for healthcare services14,15.
particularly population aging,
Epidemiological,
lifestyle and environmental and socioeconomic factors also influence individual and
population health status, are also associated with healthcare spending14. Individual healthcare spending
is also shaped by utilization patterns, access to providers, and broader forces such as economic growth
and technological progress14,15. These determinants interact in nonlinear ways, producing highly skewed
and dynamic spending distributions. Capturing such complexity requires analytical frameworks capable
of modeling heterogeneity and temporal persistence in costs—motivating the application of neural net-
work approaches to health expenditure prediction.

This systematic review aims to map the evolving landscape of neural network-based healthcare cost
and expenditure prediction. Specifically, we systematically searched the literature to address the follow-
ing key questions: (1) What research objectives have been addressed (e.g. total cost, cost change, high-
cost classification)? (2) Which neural network methods—feedforward networks, convolutional nets, recur-
rent architectures (LSTM/GRU), hybrid models, or others—are used in health expenditure prediction?
(3) What evaluation frameworks and result presentation strategies (e.g. error metrics, calibration, classifi-
cation thresholds) are commonly employed? (4) How do neural network model performances compare
with classical regression or machine learning baselines across domains and settings?

Methods

This systematic review was conducted according to a pre-specified protocol and registered with the
International Prospective Register of Systematic Reviews (PROSPERO; registration number CRD420251129440).
A comprehensive search strategy was designed to identify relevant literature across multiple biblio-
graphic databases, including Web of Science, PubMed, EMBASE, and Scopus. The search covered all pub-
lications up to August 2025. Reference lists of included studies were additionally screened to capture
potentially eligible articles not retrieved through the database search.

Studies were considered eligible if they: (1) Applied deep learning or neural network algorithms (e.g.
feed-forward neural network, convolutional neural network, recurrent neural network, long short-term
memory [LSTM], DNN) for the prediction, estimation, or modeling of healthcare expenditure, cost, or
resource use; (2) Used real-world, individual-level health data such as insurance claims, electronic health
records (EHRs), administrative datasets, or registry data; (3) Reported model performance metrics (e.g.
RMSE, MAE, R2, AUC) or compared neural network models against classical or machine-learning base-
lines; and (4) Were published in English.

To ensure methodological comparability, only studies that directly implemented both a deep learning
(or neural network) model and at least one classical regression model (e.g. linear regression, GLM, ridge,
lasso) and quantitatively compared their predictive performance were included. Additionally, studies
were required to include an outcome variable explicitly representing healthcare expenditure, spending,

---

<!-- PAGE 4 -->

656

J. T. LEE ET AL.

cost, or a closely related economic measure (e.g. medical cost,
expressed in monetary units).

insurance charge, resource utilization

Studies were excluded if they: (i) focused exclusively on intervention cost-effectiveness or simulation
modeling without predictive application; used hypothetical, synthetic, or simulated data sources (e.g.
Kaggle or other artificially generated datasets) rather than real-world data; or (iii) applied machine-learn-
ing algorithms other than neural networks without neural network comparison. (iv) did not conduct a
direct comparative analysis between a classical regression model and a deep learning approach on cost-
or expenditure-related outcomes.

minology (e.g. “deep learning,” “neural network
“machine learning”);
(cid:1)
“estimate
,” “projection
(cid:1)
(cid:1)
(cid:1)
,” “health spending,” “treatment cost
,” “health expenditure
cost

Three conceptual domains guided the search formulation: (1) Deep learning and neural network ter-
(cid:1)
,” “CNN,” “RNN,” “LSTM,” “DNN,” “artificial intelligence,”
(cid:1)
(cid:1)
“model
,”
,”
,” “medical
,” “resource use,” “resource utilization”).
Alternative databases such as ACM Digital Library were evaluated but subsequently excluded due to

(cid:1)
,”
(2) Predictive modeling expressions
(cid:1)
(cid:1)”); and (3) Healthcare expenditure concepts (e.g. “healthcare cost

“forecast

“predict

(e.g.

limited coverage of health-economic literature.

During the initial screening stage, titles and abstracts were independently assessed by one trained
reviewer according to pre-specified eligibility criteria16. All records that were potentially eligible or for
which eligibility was unclear were retained for full-text review to avoid premature exclusion. Final inclu-
sion and exclusion decisions were jointly discussed by at least two team members; in cases of disagree-
ment, a third team member was consulted to resolve discrepancies and minimize the risk of systematic
selection bias.

Among excluded studies, the most common reason for exclusion was that the prediction target was
not healthcare cost or expenditure but alternative outcomes, such as disease incidence or hospitalisation
risk. Additional studies were excluded because they did not include a direct comparison between tradi-
tional regression or tree-based models and deep learning approaches. Studies relying on simulated or
synthetic data, or other non–real-world data sources, were also excluded. Based on these criteria, a total
of eight studies were ultimately included, all of which used real-world data, explicitly focused on health-
care cost prediction, and directly compared deep learning models with traditional regression or tree-
based approaches.

Data extraction was performed using a structured Excel framework. Extracted variables included bib-
liographic details, data source and setting, population characteristics, neural network architecture, input
variables, model evaluation metrics, comparator models, cost or outcome definitions, and key findings.

Findings were synthesized narratively and summarized in tabular form, categorizing studies by model
type, prediction task, dataset scale, and performance benchmark. Quantitative aggregation was limited
to descriptive reporting due to methodological heterogeneity among studies. The systematic review fol-
lowed the PRISMA 2020 reporting guidelines, and the completed checklist is provided in Supplementary
Table S1.

Results

The database search identified a total of 23,572 records: PubMed (n ¼ 1,525), Embase (n ¼ 9,532), Scopus
(n ¼ 43), and Web of Science (n ¼ 12,472). After removing 2,164 duplicate records, 21,408 unique records
were screened by title and abstract. Additionally, 11 records were identified through citation searching,
all of which were retrieved and assessed for eligibility, with 10 records excluded. Of these, 21,352 were
excluded as not relevant to the review objectives. 8 studies met the final inclusion criteria and were
included in this systematic review. The full study identification, screening, and inclusion process is illus-
trated in Figure 1 (PRISMA flow diagram).

Characteristics of identified studies

Table 1 showed the characteristics of the identified studies. A total of eight studies met the inclusion cri-
teria, conducted across the United States, predominantly private insurance system (n ¼ 5)17,18,20,22,23;
Europe, including Germany, which has single-payer systems (n ¼ 1)10, and France, which has universal

---

<!-- PAGE 5 -->

JOURNAL OF MEDICAL ECONOMICS

657

Figure 1. PRISMA flow diagram of study identification.

health insurance with multiple payers (n ¼ 1)21; and Asia (China ¼ 1)19. Sample sizes ranged from
approximately 50,000 to over 1.4 million individuals, encompassing data sources such as commercial
insurance claims (n ¼ 3)17,18,23, national health insurance databases (n ¼ 3)10,20,21, and electronic medical
records (EMR) (n ¼ 1)19, while one study used retail-level pharmacy transaction records (n ¼ 1)22.

Six studies adopted longitudinal designs (multi-year or time-series forecasting)10,17,18,20,22,23, while two
were cross-sectional cost-regression studies19,21. Table 2 also shows the outcome variables primarily
included: (1) Total annual or per-member-per-month expenditure (n ¼ 5)10,17,18,20,21, (2) Medication-spe-
cific or pharmacy expenditures (n ¼ 3)18,22,23, (3) Preventable cost17, and (4) In-hospital costs (n ¼ 1)19.

In the heart failure population study by Lewis et al. (2021), preventable costs were defined on the
basis of the follow-up period and operationalized using insurance claims data, in which hospitalizations
and emergency department visits classified as potentially avoidable—according to clinical quality indica-
tors and emergency care categorization algorithms—were aggregated into total reimbursed costs17.
Among the eight included studies, only this study explicitly focused on preventable costs as the primary
economic outcome, whereas the remaining studies primarily examined total medical expenditures or in-
hospital costs as the main economic indicators17.

classical

Deep learning architectures varied across studies:

feed-forward networks (DNN/MLP; n ¼ 2)10,21,
sequence-based models (LSTM, stacked LSTM, CNN-LSTM, RNN; n ¼ 4)17,18,20,23, hybrid or multi-view net-
works (n ¼ 1)19, and variance-based generative adversarial network (V-GAN; n ¼ 1)22. Comparators
included
LASSO regression
(n ¼ 6)10,17,18,20,21,23—and tree-based machine-learning methods including Random Forest (RF), Gradient
(n ¼ 4)17,20–22. Model performance was most commonly
Boosting Machine (GBM), or CatBoost
evaluated using R2 or adjusted R2 (n ¼ 5)10,18,20,21,23, MAE (n ¼ 3)18,19,21, RMSE (n ¼ 5)18–20,22,23, and AUC
(n ¼ 2)10,17; several studies additionally reported precision@k, cost-capture, or correlation coefficients
for discrimination and calibration assessment (n ¼ 3)10,17,19.

approaches—such

regression

ridge,

GLM,

and

as

Clinical and policy contexts of prediction

Based on the comparative models in Table 2, this section shows the methodological frameworks and
model performance of each included study. One U.S. study focused on population health management,
predicting preventable hospitalizations, emergency visits, and expenditures among heart failure patients

---

<!-- PAGE 6 -->

;

d
o
i
r
e
p

n
o
i
t
a
v
r
e
s
b
o

.
)
d
o
i
r
e
p

n
o
i
t
a
u
a
v
e

l

s
d
r
o
c
e
r

s

i

m
a
l
c

l

i

a
n
d
u
t
i
g
n
o

5
1
0
2
–
0
1
0
2
(

l

7
1
0
2
–
6
1
0
2

,

a
t
a
d

s

i

m
a
l
c

l

i

a
n
d
u
t
i
g
n
o

l

m
o
r
f

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
t
i

e
r
a
p
m
o
c

o
t

d
n
a

r
e
h
t
o

d
n
a

n
o
i
s
s
e
r
g
e
r

e
g
d
i
r

h
t
i

w

l

a
t
o
t

h
t
o
b

r
o
f

s
l
e
d
o
m
k
r
a
m
h
c
n
e
b

e
g
n
a
h
c
-
t
s
o
c

d
n
a

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

t
s
o
c

.

n
o
i
t
a
c
i
f
i
t
n
e
d

i

e
t
a
t
s

d
n
a

,

x
e
s

,

e
g
a

y
b

l

n
o
i
t
a
u
p
o
p

n
a
m
r
e
G

e
h
t

f
o

e
v
i
t
a
t
n
e
s
e
r
p
e
r

.

e
c
n
e
d
i
s
e
r

f
o

658

J. T. LEE ET AL.

:

.
)
1
2
7
(

:

s
t
e
s

g
n
i
t
s
e
t

d
n
a

s
t
n
e
i
t
a
p

)
F
H

(

e
r
u

l
i

a
f

t
r
a
e
h

g
n
o
m
a

i

g
n
d
n
e
p
s

e
r
a
c
h
t
l
a
e
h

d
n
a

,
s
t
i
s
i
v

,
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
t
i
p
s
o
h

l

e
b
a
t
n
e
v
e
r
p

)

D
E
(

t
n
e
m

t
r
a
p
e
d

y
c
n
e
g
r
e
m
e

,

n
o
i
t
a
d

i
l

a
v

,

i

g
n
n
a
r
t

i

o
t
n

i

d
e
d
v
d

i

i

g
n
i
t
c
i
d
e
r
p

r
o
f

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

e
s
a
b
a
t
a
d

e
c
n
a
r
u
s
n

i

l

a
i
c
r
e
m
m
o
c

n
g
i
s
e
d

l

a
r
o
p
m
e
T

n
g
i
s
e
d

y
d
u
t
S

s
e
v
i
t
c
e
b
o

j

d
n
a
m
A

i

e
z
i
s

l

e
p
m
a
s

d
n
a

l

n
o
i
t
a
u
p
o
p

y
d
u
t
S

y
r
t
n
u
o
C

l

a
n
r
u
o
J

f
o

)
7
1
0
2
–
6
0
0
2
(

s
t
n
e
i
t
a
p

;

a
t
a
d

s

i

m
a
l
c

l

a
i
c
r
e
m
m
o
c

l

a
n
o
i
t
i
d
a
r
t

h
t
i

w

)
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

.

.

S
U

e
g
r
a

l

a

n

i

)
7
1
0
2
–
6
1
0
2
(

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
1

g
n
i
s
u

-
n
o
n

d
n
a

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
(

s
e
h
c
a
o
r
p
p
a

o
w

t

r
o
f

d
e

l
l

o
r
n
e

y
l
s
u
o
u
n
i
t
n
o
c

)
s
r
a
e
y
2
1
(

l

i

a
n
d
u
t
i
g
n
o
L

g
n

i
l

e
d
o
m
c
i
t
s
o
n
g
o
r
p

e
v
i
t
c
e
p
s
o
r
t
e
R

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

e
r
a
p
m
o
c

o
T

e
r
u

l
i

a
f

t
r
a
e
h

h
t
i

w
s
t
l
u
d
a

0
6
2
3
9

,

s
e
t
a
t
S

d
e
t
i
n
U

s
t
r
o
p
e
R

c
i
f
i
t
n
e
i
c
S

.
l

a

7
1

)
1
2
0
2
(

t
e

s
i
w
e
L

y
d
u
t
S

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

e
r
u
t
i
d
n
e
p
x
e

e
r
a
c
h
t
l
a
e
h

r
o
f

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

n
o

i

s
e
d
u
t
s

d
e
d
u
l
c
n

i

f
o

s
c
i
t
s
i
r
e
t
c
a
r
a
h
C

.

1

e
l
b
a
T

)
r
a
e
y
-
i
t
l
u
m

(

l

i

a
n
d
u
t
i
g
n
o
L

d
e
s
a
b
-
n
o
i
t
a
u
p
o
p

l

e
v
i
t
c
e
p
s
o
r
t
e
R

p
e
e
d

a

e
t
a
u
a
v
e

l

d
n
a

l

p
o
e
v
e
d

o
T

m
o
r
f

d
n
a

l

t
n
e
m
p
o
e
v
e
d
-
l
e
d
o
m

g
n
i
s
u

y
d
u
t
s

n
o
s
i
r
a
p
m
o
c

s
t
s
o
c

e
r
a
c
-
h
t
l
a
e
h

e
r
u
t
u
f

r
a
e
y
-
e
n
o

g
n
i
t
c
i
d
e
r
p

r
o
f

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

0
6
>

(

e
s
a
b
a
t
a
d

f
e
G
n

I

e
h
t

s
l
a
u
d
v
d
n

i

i

i

d
e
r
u
s
n

i

,

6
4
3
3
0
4
1

,

h
t
l
a
e
h

y
r
o
t
u
t
a
t
s

n
a
m
r
e
G

,
)
7
1
0
2
–
0
1
0
2

,
s
e
c
n
a
r
u
s
n

i

y
n
a
m
r
e
G

l

a
c
i
d
e
M
C
M
B

.
l

a

t
e

n
o
i
s
i
c
e
D

d
n
a

s
c
i
t
a
m
r
o
f
n

I

g
n
i
k
a
M

0
1

)
2
2
0
2
(

s
s
o
B
-
e
w
e
r
D

)
y
a
t
s
-
n
h
t
i

i

w

(

l

a
n
o
i
t
c
e
s
-
s
s
o
r
C

y
d
u
t
s

l

a
n
o
i
t
a
v
r
e
s
b
o

e
v
i
t
c
e
p
s
o
r
t
e
R

e
c
r
u
o
s
e
r

l

a
t
i
p
s
o
h
-
n

i

t
c
i
d
e
r
p

o
T

s
d
r
o
c
e
r

t
n
e
i
t
a
p

d
e
g
r
a
h
c
s
i
d

0
0
0
0
5
7

,

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

l

e
b
m
e
s
n
e
M
T
S
L

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
n
o
i
t
i
d
a
r
t

i

t
s
n
a
g
a

.
s
l
e
d
o
m

)
.
S
U

.

(

e
s
a
b
a
t
a
d

s
r
e
t
n
u
o
c
n
E

d
n
a

s

i

m
a
C

l

l

a
i
c
r
e
m
m
o
C

i

a
n
h
C

d
e
s
a
B
-
e
g
d
e
w
o
n
K

l

9
1

)
1
2
0
2
(

.
l

a

t
e

u
Y

y
d
u
t
s

e
h
T

.

i

g
n
n
r
a
e

l

d
e
s
i
v
r
e
p
u
s

e
c
r
u
o
s
e
R
(

P
U
R

e
h
t

d
e
c
u
d
o
r
t
n

i

r
o
f

a
t
a
d

R
M
E

d
e
r
u
t
c
u
r
t
s
n
u

k
r
o
w
e
m
a
r
f

)
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

n
o
i
t
a
z
i
l
i
t
U

s
w
e
v

i

a
t
a
d

l

e
p
i
t
l
u
m
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

)
t
x
e
t

n
o
i
t
a
r
e
p
o

,
t
x
e
t

s
i
s
o
n
g
a
d

i

,
s
e
r
u
t
a
e
f

d
e
r
u
t
c
u
r
t
s

.

.

g
e
(

.
l

e
d
o
m
d
e
i
f
i
n
u

a

o
t
n

i

d
n
a

d
e
r
u
t
c
u
r
t
s

g
n
i
s
u

g
n
i
t
a
m

i
t
s
e

y
l
l

a
c
i
f
i
c
e
p
s

,

n
o
i
t
a
z
i
l
i
t
u

f
o

h
t
g
n
e

l

d
n
a

s
t
s
o
c

l

a
t
i
p
s
o
h
-
n

i

c
i
n
o
r
t
c
e
e

l

p
e
e
d

a

a
i
v

g
n
i
s
u

)
S
O
L
(

y
a
t
s

s
d
r
o
c
e
r

l

a
c
i
d
e
m

.

h
c
a
o
r
p
p
a

i

g
n
n
r
a
e

l

e
s
a
b
a
t
a
d

)
R
M
E
(

s
d
r
o
c
e
r

l

a
c
i
d
e
m

t
n
e
i
t
a
p

d
n
a

,
s
e
d
o
c

n
o
i
t
a
r
e
p
o

,
s
t
x
e
t

s
i
s
o
n
g
a
d

i

i

g
n
d
u
l
c
n

i

.
s
c
i
h
p
a
r
g
o
m
e
d

c
i
n
o
r
t
c
e
e

l

l

e
a
c
s
-
e
g
r
a

l

a
m
o
r
f

n
w
a
r
d

,
s
l
a
t
i
p
s
o
h

i

e
s
e
n
h
C
m
o
r
f

s

m
e
t
s
y
S

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

d
o
i
r
e
p
-
t
x
e
n

t
c
i
d
e
r
p

o
t

d
e
s
u

e
r
e
w

.
s
e
r
u
t
i
d
n
e
p
x
e

)
h
t
n
o
m
-
2
1
(

s
n
o
i
t
a
c
i
d
e
m
d
n
a

,
s
e
r
u
d
e
c
o
r
p

,
s
e
s
o
n
g
a
d

i

,
s
e
r
u
t
i
d
n
e
p
x
e

s

i

m
a
l
c

e
v
i
t
a
r
t
s
i
n
m
d
a

i

g
n
i
s
u

y
d
u
t
s

’

l

a
c
i
r
o
t
s
i
h

s

t
n
e
i
t
a
p

h
c
a
E

.

a
t
a
d

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

f
o

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

r
o
f

)
s
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

,
s
e
r
u
t
i
d
n
e
p
x
e

e
r
a
c
h
t
l
a
e
h

e
r
u
t
u
f

d
n
a

g
n
i
y
f
i
t
n
e
d

i

n
o

s
u
c
o
f

a

h
t
i

w

d
e
e
n
-
h
g
h

i

t
s
o
c
-
h
g
h

i

i

g
n
g
a
n
a
m

e
h
T

.
s
t
n
e
i
t
a
p

i

d
a
c
i
d
e
M

)

N
H
C
H

(

t
n
e
r
r
u
c
e
r

i

g
n
d
u
l
c
n
i
(

s
l
e
d
o
m

l

a
r
o
p
m
e
t

y
f
i
t
n
a
u
q

o
t

d
e
m
a

i

y
d
u
t
s

i

t
s
n
a
g
a

s
l
e
d
o
m
g
n
n
r
a
e

i

l

p
e
e
d

k
r
a
m
h
c
n
e
b

o
t

d
n
a

i

g
n
d
n
e
p
s

.
s
e
h
c
a
o
r
p
p
a

n
o
i
s
s
e
r
g
e
r

l

a
c
i
s
s
a
l
c

e
r
a
c
h
t
l
a
e
h

n

i

e
c
n
e
t
s
i
s
r
e
p

-
h
g
h

i

t
s
o
c
-
h
g
h

i

d
n
a

l

n
o
i
t
a
u
p
o
p

,
s
p
u
o
r
g
b
u
s

)

N
H
C
H

(

d
e
e
n

l

e
p
m
a
S

.

a
t
a
d

s

i

m
a
l
c

l

i

a
n
d
u
t
i
g
n
o

l

f
o

s
r
a
e
y

l

a
r
e
v
e
s

g
n
i
s
u

d
e
z
y
l
a
n
a

t
u
b

,

d
e
t
r
o
p
e
r

y
l
t
i
c
i
l

p
x
e

t
o
n

e
z
i
s

f
o

s
n
o

i
l
l
i

m
d
e
n
a
t
n
o
c

i

t
e
s
a
t
a
d

e
h
t

l

a
r
e
n
e
g

h
t
o
b

i

g
n
d
u
l
c
n

i

s
d
r
o
c
e
r

r
e
b
m
e
m
y
l
h
t
n
o
m

f
o

s
r
a
e
y

l

e
p
i
t
l
u
m
g
n
i
r
e
v
o
c

.

y
r
o
t
s
i
h

e
r
u
t
i
d
n
e
p
x
e

)
r
a
e
y
-
i
t
l
u
m

(

l

i

a
n
d
u
t
i
g
n
o
L

t
r
o
h
o
c

l

i

a
n
d
u
t
i
g
n
o

l

e
v
i
t
c
e
p
s
o
r
t
e
R

e
v
i
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

e
t
a
u
a
v
e

l

o
T

,
s
a
x
e
T

n

i

s
t
n
e
i
t
a
p

d
e

l
l

i

o
r
n
e
-
d
a
c
i
d
e
M

s
e
t
a
t
S

d
e
t
i
n
U

g
n
E

d
e
M
o
B

i

e
n
i
L
n
O

0
2
)
8
1
0
2
(

.
l

a

t
e

g
n
a
Y

)
5
1
0
2
–
1
1
0
2
(

l

i

a
n
d
u
t
i
g
n
o
L

,
l

a
n
o
i
t
a
v
r
e
s
b
o

,

e
v
i
t
c
e
p
s
o
r
t
e
R

y
l
h
t
n
o
m
d
n
a

y
l
k
e
e
w

t
s
a
c
e
r
o
f

o
T

h
t
i

w
s
t
n
e
i
t
a
p

0
0
0
0
5

,

r
e
v
O

s
e
t
a
t
S

d
e
t
i
n
U

f
o

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
A

.
l

a

k
i
h
s
u
a
K

8
1

t
e

)
0
2
0
2
(

-
t
n
e
i
t
a
p

f
o

s
r
a
e
y

e
v
i
f

g
n
i
s
u

y
d
u
t
s

i

-
n
a
r
t

0
1
/
0
2
/
0
7

;

a
t
a
d

s

i

m
a
l
c

l

e
v
e

l

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
t
s
o
c

l

i

a
n
d
u
t
i
g
n
o

l

.
t
i
l

p
s

t
s
e
t
-
n
o
i
t
a
d

i
l

a
v

s
e
r
u
t
i
d
n
e
p
x
e

n
o
i
t
a
c
i
d
e
m

t
n
e
i
t
a
p

i

g
n
n
r
a
e
l
-
p
e
e
d

d
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
s
u

–
N
N
C

d
e
d
a
e
h
-
i
t
l
u
m
e
r
a
p
m
o
c

o
t

d
n
a

,
s
d
o
h
t
e
m

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

5
1
0
2

l
i
r
p
A

d
n
a

1
1
0
2

y
r
a
u
n
a
J

n
a
c
S
t
e
k
r
a
M
n
e
v
u
r
T

e
h
t

m
o
r
f

n
e
e
w
t
e
b

s

i

m
a
l
c

n
o
i
t
a
c
i
d
e
m

i

n
a
p

d
e
s
a
b
-
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
r
p

–

i

e
n
h
c
a
M

i

g
n
n
r
a
e
L

:

4
1

r
e
t
p
a
h
C

---

<!-- PAGE 7 -->

n
g
i
s
e
d

l

a
r
o
p
m
e
T

n
g
i
s
e
d

y
d
u
t
S

s
e
v
i
t
c
e
b
o

j

d
n
a
m
A

i

e
z
i
s

l

e
p
m
a
s

d
n
a

l

n
o
i
t
a
u
p
o
p

y
d
u
t
S

y
r
t
n
u
o
C

l

a
n
r
u
o
J

r
a
e
y

l

e
g
n
i
s
(

l

a
n
o
i
t
c
e
s
-
s
s
o
r
C

,
l

a
n
o
i
t
c
e
s
-
s
s
o
r
c

,

e
v
i
t
c
e
p
s
o
r
t
e
R

e
v
i
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

e
r
a
p
m
o
c

o
T

e
h
t

y
b

d
e
r
e
v
o
c

l

n
o
i
t
a
u
p
o
p

l

a
r
e
n
e
G

e
c
n
a
r
F

l

a
n
r
u
o
J

n
a
e
p
o
r
u
E

)
6
1
0
2

e
v
i
t
a
r
t
s
i
n
m
d
a

i

d
e
t
c
e

l
l

o
c

y
l
e
n
i
t
u
o
r

e
t
a
r
a
p
e
S

.

S
D
N
S
m
o
r
f

a
t
a
d

s

i

m
a
l
c

g
n
i
s
u

y
d
u
t
s

d
e
s
a
b
-
n
o
i
t
a
u
p
o
p

l

-
h
g
h

i

r
o
f

d
n
a

l

n
o
i
t
a
u
p
o
p

e
r
i
t
n
e

e
h
t

r
o
f

d
e
n
a
r
t

i

e
r
e
w
s
l
e
d
o
m

.
s
p
u
o
r
g
b
u
s

t
s
o
c

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

f
o

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

l

a
c
i
s
s
a
l
c

a

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

)
k
r
o
w
t
e
N

)

M
L
G

(

l

e
d
o
M

r
a
e
n
i
L

d
e
z
i
l

a
r
e
n
e
G

l

a
r
u
e
N

d
n
a

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
(

l

i

a
u
d
v
d
n

i

i

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

i

e
d
w
n
o
i
t
a
n

g
n
i
s
u

s
t
s
o
c

e
r
a
c
h
t
l
a
e
h

o
t

t
h
g
u
o
s

y
d
u
t
s

e
h
T

.

a
t
a
d

s

i

m
a
l
c

i

s
n
a
g

l

i

u
f
g
n
n
a
e
m

s
r
e
f
f
o

i

g
n
n
r
a
e

l

n

i

n
o
i
s
s
e
r
g
e
r

l

a
n
o
i
t
i
d
a
r
t

r
e
v
o

i

e
n
h
c
a
m

r
e
h
t
e
h
w
e
n
m
r
e
t
e
d

i

.

g
n

i
l

e
d
o
m

t
s
o
c

h
t
l
a
e
h

g
n
i
s
u

,
)
S
D
N
S
(

m
e
t
s
y
S

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

I

e
s
a
b
a
t
a
d

l

a
n
o
i
t
a
n

e
h
t

f
o

l

e
p
m
a
s

m
o
d
n
a
r

e
v
i
t
a
t
n
e
s
e
r
p
e
r

7
9
/
1

a

a
t
a
D

h
t
l
a
e
H

l

a
n
o
i
t
a
N

h
c
n
e
r
F

.

6
1
0
2

r
a
e
y

e
h
t

r
o
f

s
c
i
m
o
n
o
c
E

h
t
l
a
e
H

f
o

.
l

a

t
e

1
2

)
2
2
0
2
(

t
n
o
m
V

i

y
d
u
t
S

.

d
e
u
n
i
t
n
o
C

.

1

e
l
b
a
T

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

,
l

i

a
n
d
u
t
i
g
n
o
L

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

e
v
i
t
c
e
p
s
o
r
t
e
R

-
e
c
n
a
i
r
a
v

a

t
s
e
t

d
n
a

l

p
o
e
v
e
d

o
T

i

n
a
p

c
i
f
i
c
e
p
s

a

g
n
i
s
a
h
c
r
u
p

s
t
n
e
i
t
a
P

s
e
t
a
t
S

d
e
t
i
n
U

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

.
l

a

k
i
h
s
u
a
K

JOURNAL OF MEDICAL ECONOMICS

659

.

g
n
i
t
s
e
t

r
o
f

d
e
s
u

)
5
1
0
2
(

s
h
t
n
o
m
2
1

l

a
n
i
f

,

i

g
n
n
a
r
t

i

g
n
i
s
u

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

e
m

i
t

l

e
p
i
t
l
u
m

r
e
v
o

a
t
a
d

e
r
u
t
i
d
n
e
p
x
e

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

.
s
t
n
o
p

i

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

d
e
s
u

t
s
r
i
f

—
n
g
i
s
e
d

)
4
1
0
2
–
1
1
0
2
(

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

l

i

a
n
d
u
t
i
g
n
o
L

-
e
m

i
t

e
r
u
t
i
d
n
e
p
x
e

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
r
p

g
n
i
s
u

y
d
u
t
s

g
n

i
l

e
d
o
m

l

a
i
r
a
s
r
e
v
d
a

e
v
i
t
a
r
e
n
e
g

d
e
s
a
b

t
a
h
t

l

e
d
o
m

)

N
A
G
-
V
(

k
r
o
w
t
e
n

.

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

n

i

e
c
n
e
r
e
f
f
i
d

e
h
t

s
e
z
i
m
n
m

i

i

s

i

m
a
l
c

e
c
n
a
r
u
s
n

i

y
r
a
d
n
o
c
e
s

g
n
i
s
u

.

a
t
a
d

-
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
r
p

a

n
o

e
r
u
t
i
d
n
e
p
x
e

g
n
i
s
u

n
o
i
t
a
c
i
d
e
m
n
a
p

i

d
e
s
a
b

o
t

d
n
a

)

M
T
S
L
(

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

a

i

t
s
n
a
g
a

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

e
r
a
p
m
o
c

l

e
d
o
m

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

l

a
n
o
i
t
i
d
a
r
t

.
)

A
M
R
A

I

(

y
d
u
t
s

l

a
n
o
i
t
a
v
r
e
s
b
o

e
v
i
t
c
e
p
s
o
r
t
e
R

t
n
e
i
t
a
p
-
r
e
p

y
l
h
t
n
o
m

t
s
a
c
e
r
o
f

o
T

d
n
a

l

e
d
o
m
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
a
i
r
a
v

g
n
i
t
c
i
d
e
r
p

r
o
f

a
t
a
d

l

a
u
t
c
a

s
e
r
u
t
i
d
n
e
p
x
e

e
n
i
c
i
d
e
m

-
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
r
p

a

g
n
i
s
a
h
c
r
u
p

s
e
t
a
t
S

d
e
t
c
a
r
t
x
e

,

n
o
i
t
a
c
i
d
e
m
n
a
p

i

d
e
s
a
b

n
a
c
S
t
e
k
r
a
M
n
e
v
u
r
T

e
h
t

m
o
r
f

–
1
1
0
2
(

t
e
s
a
t
a
d

s

i

m
a
l
c

e
c
n
a
r
u
s
n

i

)
5
1
0
2

n
o

e
c
n
e
r
e
f
n
o
C

l

a
n
o
i
t
a
n
r
e
t
n

I

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

e
c
n
e
i
c
S

a
t
a
D

i

e
n
h
c
a
M

E
E
E
I

e
h
t

)
S
D
L
M

(

e
z
i
s

l

e
p
m
a
s

t
c
a
x
e

e
h
t

;

n
o
i
t
a
c
i
d
e
m

m
o
r
f

d
e
v
i
r
e
d

t
u
b

d
e
i
f
i
c
e
p
s

t
o
n

s
d
r
o
c
e
r

n
o
i
t
c
a
s
n
a
r
t

l

e
v
e
l
-
l
i

a
t
e
r

.
)
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
-
e
m

i
t
(

d
e
t
i
n
U

e
h
t

n

i

s
t
n
e
i
t
a
p

,

0
0
0
0
5
>

s
e
t
a
t
S

d
e
t
i
n
U

f
o

i

s
g
n
d
e
e
c
o
r
P

.
l

a

2
2

t
e

)
0
2
0
2
(

3
2
)
7
1
0
2
(

t
e

k
i
h
s
u
a
K

---

<!-- PAGE 8 -->

660

J. T. LEE ET AL.

d
e
s
a
b

s
e
m
o
c
t
u
o

l

e
b
a
t
n
e
v
e
r
P

s

m
h
t
i
r
o
g
a

l

g
n
i
t
s
i
x
e

n
o

l

a
n
r
e
t
n

i

m
o
d
n
a
r

d
n
o
y
e
b

n
o
i
t
a
d

i
l

a
v

l

a
n
r
e
t
x
e

o
N

y
a
m

)
I

Q
P

,
s
g
n

i
l
l
i

B
(

.
s
t
n
e
v
e

y
f
i
s
s
a
l
c
s
i

m

o
t

e
u
d

y
c
n
e
i
c
i
f
f
e
n

i

l

a
i
t
n
e
t
o
P

.

i

w
o
d
n
w
a
t
a
d

r
a
e
y
-
1
1

d
n
a

y
c
n
e
r
a
p
s
n
a
r
t

d
e
t
i

m
i
L

.
t
i
l

p
s

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

i

d
e
t
i

m

i
l

l

s
e
b
a
i
r
a
v

.
s
s
e
n
e
t
e
p
m
o
c

l

p
e
e
d

f
o

y
t
i
l
i

i

b
a
n
a
p
x
e

l

–

–

–

–

c
i
t
s
i
g
o

l

l
l

a

d
e
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

d
n
a

s
e
n

i
l

e
s
a
b

n
o
i
s
s
e
r
g
e
r

r
o
f

k
s
i
r

h
g
h

i

t
a

s
t
n
e
i
t
a
p

d
n
a

s
t
n
e
v
e

l

e
b
a
t
n
e
v
e
r
p

g
n
i
t
a
n
m

i

i
r
c
s
i
d

n

i

M
B
G

n
o
i
t
a
z
i
l
i
t
u

r
o
i
r
P

.

i

g
n
d
n
e
p
s

D
E

,

S
O
L

,
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
t
i
p
s
o
h
(

i

s
e
i
t
i
d
b
r
o
m
o
c

d
n
a

)
s
t
i
s
i
v

e
r
e
w

)
y
t
e
i
x
n
a

,

D
K
C

,

D
P
O
C
(

d
e
t
a
r
t
s
n
o
m
e
D

.
s
r
e
v
i
r
d

y
e
k

n
o
i
t
a
c
i
f
i
t
a
r
t
s

k
s
i
r

e
c
n
a
h
n
e

n
a
c

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

t
a
h
t

n

i

s
n
o
i
t
n
e
v
r
e
t
n

i

d
e
t
e
g
r
a
t

r
o
f

.

e
r
a
c

F
H

d
e
s
a
b
-
e
u
a
v

l

R
H
E

d
n
a

,

y
r
o
t
a
r
o
b
a

l

)

N
N
C

d
n
a
M
T
S
L

l

y
l
r
a
u
c
i
t
r
a
p
(

:

C
O
R
U
A

t
s
e
h
g
h

i

d
e
v
e
h
c
a

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

d
e
i
f
i
t
n
e
d

I

i

s
g
n
d
n
F

i

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
m
r
o
f
r
e
p

l

e
d
o
M

g
n
i
t
a
u
a
v
e

l

r
o
f

d
e
s
u

s
c
i
r
t
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

n

i

d
e
d
u
l
c
n

i

s
e
r
u
t
a
e
F

d
e
r
a
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
e
h
t

O

e
p
y
t

l

e
d
o
m
g
n
n
r
a
e

i

l

p
e
e
D

.

.

g
e
(

l

e
b
a
i
r
a
v

e
m
o
c
t
u
O

y
d
u
t
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
p

l

e
d
o
m

l

)
e
b
a
i
r
a
v

t
e
g
r
a
t

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

e
r
u
t
i
d
n
e
p
x
e

e
r
a
c
h
t
l
a
e
h

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
c
i
s
s
a
l
c

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

l

p
e
e
d

f
o

i

s
g
n
d
n
i
f

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

2

e
l
b
a
T

,
c
i
m
o
n
o
c
e
o
i
c
o
s

f
o

k
c
a
L

–

s
l
e
d
o
m
g
n
n
r
a
e

i

l

p
e
e
D

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

l

a
i
t
n
e
u
q
e
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

l

a
i
t
n
e
u
q
e
S

s
e
r
u
t
a
e
f

n
e
v
i
r
d
-
e
g
d
e
w
o
n
k

l

9
3
9

c
i
t
s
i
g
o

l

l

a
n
o
i
t
i
d
a
r
T

:

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

l

a
i
t
n
e
u
q
e
S

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
t
i
p
s
o
h

l

e
b
a
t
n
e
v
e
r
P

7
1

)
1
2
0
2
(

.
l

a

t
e

s
i
w
e
L

e
r
u
t
p
a
C

t
s
o
C

d
n
a

,
)

%
0
1

.

%
k

p
o
t

t
a

.
)
n
o
i
s
s
e
r
g
e
r

n
o
i
s
i
c
e
r
P

,
)
c
i
t
s
i
r
e
t
c
a
r
a
h
C

r
a
e
y
-
1
1
(

i

s
g
n
d
d
e
b
m
e

–
1
(

e
v
i
t
c
i
d
e
r
P

e
v
i
t
i
s
o
P
(

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

h
t
o
b

,
s
e
i
r
o
t
s
i
h

%
k

p
o
t

t
a

)
e
u
a
V

l

.
)
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
-
n
o
n

d
n
a

,
)
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
t
i
p
s
o
h
(

8
7
7
0

.

7
2
7
0

.

,
)
s
t
i
s
i
v

D
E
(

1
8
6
0

.

.
)
s
t
s
o
c
(

%
3
4
–
9
3

:

%
1

c
i
t
s
i
g
o

l

r
o
f

%
5
1
–
2
1

p
o
t

t
a

n
o
i
s
i
c
e
r
P

.
s
v
(

g
n
i
t
a
r
e
p
O

i

r
e
v
e
c
e
R

c
e
V
2
d
r
o
W
g
n
i
s
u

s

i

m
a
l
c
m
o
r
f

.
)

M
B
G

(

l

e
d
o
M
g
n
i
t
s
o
o
B

1
8
6
0

.

,
)
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
t
i
p
s
o
h
(

.
)
s
t
s
o
c
(

7
2
7
0

.

,
)
s
t
i
s
i
v

D
E
(

e
h
t

r
e
d
n
U

a
e
r
A

(

C
O
R
U
A

-
a
t
a
d

d
n
a

)
s
d
n
e
r
t

n
o
i
t
a
z
i
l
i
t
u

d
e
t
a
r
e
n
e
g

s
e
r
u
t
a
e
f

n
e
v
i
r
d

,
s
t
s
o
c

,
s
n
o
i
t
a
c
i
d
e
m

c
i
t
s
i
g
o

l

d
e
c
n
a
h
n
E

9
3
9
(

n
o
i
s
s
e
r
g
e
r

i

t
n
e
d
a
r
G

;
)
s
e
r
u
t
a
e
f

t
s
e
h
g
h

i

d
e
v
e
h
c
a

i

8
7
7
0

.

:

C
O
R
U
A

,
s
e
r
u
d
e
c
o
r
p

i

,
s
e
i
t
i
d
b
r
o
m
o
c

;
)
s
e
r
u
t
a
e
f

d
e
t
i

m

i
l

h
t
i

w

,
s
c
i
h
p
a
r
g
o
m
e
d
(

s
t
n
a
i
r
a
v

o
w

t
(

n
o
i
s
s
e
r
g
e
r

h
t
i

w

)

M
T
S
L
(

y
r
o
m
e
M

;

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
r
u
e
N

l

a
n
o
i
t
u
o
v
n
o
C

l

-
n
o
N

.
)

N
N
C
(

k
r
o
w
t
e
N

m
r
e
T
-
t
r
o
h
S

g
n
o
L

p
e
e
D

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

d
r
a
w
r
o
F
-
d
e
e
F

:

i

g
n
n
r
a
e
L

.
)

N
N
F
(

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

-
6
(

s
t
i
s
i
v

D
E

l

e
b
a
t
n
e
v
e
r
P

-
1
(

s
t
s
o
c

l

e
b
a
t
n
e
v
e
r
P

)
3
(

;
)
n
o
z
i
r
o
h

h
t
n
o
m

)
n
o
z
i
r
o
h

r
a
e
y

-
6
(

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
t
i
p
s
o
h

)
2
(

;
)
n
o
z
i
r
o
h

h
t
n
o
m

l

e
b
a
t
n
e
v
e
r
P

)
1
(

e
r
u
t
a
e
f

r
a
e
l
c

s
k
c
a

l

.
s
e
r
u
t
i
d
n
e
p
x
e

l

e
v
e
l
-
t
n
e
i
t
a
p

.

-
h
t
l
a
e
h

l

a
r
e
n
e
g

o
n
(

t
e
s
a
t
a
d

n
e
v
u
r
T
m
o
r
f

s
e
r
u
t
i
d
n
e
p
x
e

i

.
s
t
n
a
n
m
r
e
t
e
d

l

i

a
r
o
v
a
h
e
b

r
o

l

a
i
c
o
s

f
o

n
o
i
s
u
l
c
n

i

o
N

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

d
e
t
s
e
g
g
u
S

.
)
s
t
s
o
c
m
e
t
s
y
s

o
t

d
e
t
c
i
r
t
s
e
r

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

l

d
e
t
a
e
r
-
n
o
i
t
a
c
i
d
e
m

.

n
o
i
t
u
b
i
r
t
t
a

–

–

–

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

n

i

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

e
r
u
t
i
d
n
e
p
x
e

r
e
d
a
o
r
b

n
o

g
n
i
t
s
e
t

d
n
a

.

k
r
o
w
e
r
u
t
u
f

)
P
A
H
S

.

.

g
e
(

I

A

l

e
b
a
n
a
p
x
e

l

i

.

i

g
n
n
n
a
p

l

e
c
r
u
o
s
e
r

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

h
t
o
b

d
e
r
u
t
p
a
c

m
r
e
t
-
g
n
o

l

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

r
o
f

l

a
i
t
n
e
t
o
p

i

g
n
w
o
h
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

d
n
e
r
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

t
s
o
c

e
r
a
c
h
t
l
a
e
h

.
)

N
N
C

,

M
T
S
L

,

A
M
R
A

I

(

y
l
e
v
i
t
c
e
f
f
e

l

e
b
m
e
s
n
e

s
e
n

i
l

e
s
a
b

l

a
c
i
s
s
a
l
c

r
o

d
e
d
a
e
h

M
T
S
L
-
N
N
C

d
i
r
b
y
h

e
h
T

l

-
e
g
n
i
s

l
l

a

d
e
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

t
I

y
l
t
n
a
c
i
f
i
n
g
i
s

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
s
e
n
t
s
u
b
o
r

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

d
e
v
o
r
p
m

i

–
3
(cid:3)
E
P
A
M

,

.

2
0
1
(cid:4)
5
3
(cid:3)
E
A
M

.

3
9
0
–
1
9
0
(cid:3)

.

2
R

,

%
4

t
s
e
b

e
h
t

d
e
v
e
h
c
a

i

:

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

g
n
i
s
u

e
t
i
p
s
e
d

d
e
t
i

m

i
l

i

n
a
m
e
r

n
o
i
t
a
m

i
t
s
e

i

y
t
n
a
t
r
e
c
n
u

.
s
t
n
e
d
a
r
g

i

d
e
t
a
r
g
e
t
n

i

e
d
i
s
t
u
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
v

l

a
n
r
e
t
x
e

o
N

–

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

i

l

e
d
o
M
–

.
s
l
e
d
o
m
g
n
n
r
a
e

i

l

l

a
i
c
o
s

f
o

n
o
i
s
u
l
c
n

i

t
i
c
i
l

p
x
e

o
N

n
o

d
e
d
e
e
n

h
c
r
a
e
s
e
r

r
e
h
t
r
u
F

d
n
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

l

a
m

i
t
p
o

r
e
h
t
o

o
t

n
o
i
t
a
z
i
l

a
r
e
n
e
g

.
s
r
o
t
c
a
f

l

a
t
n
e
m
n
o
r
i
v
n
e

r
o

i

s
t
n
a
n
m
r
e
t
e
d

d
n
a

s
d
a
e
h

l

e
p
i
t
l
u
m
o
t

e
u
d

e
v
i
s
n
e
t
n

i

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
C

.
s
e
p
y
t
o
n
e
h
p

i

g
n
d
o
c

r
o

s
n
o
i
t
a
u
g
e
r

l

g
n

i
l
l
i

b

n

i

s
e
g
n
a
h
c

.
s
e
c
i
t
c
a
r
p

–

–

–

y
b

d
e
t
c
e
f
f
a

e
b

y
a
m

l

e
d
o
M
–

.
t
e
s
a
t
a
d

f
e
G
n

I

e
h
t

;

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

l

e
d
o
M
–

.

e
r
u
t
c
u
r
t
s

l

e
b
m
e
s
n
e

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

t
a
h
t

l

d
e
a
e
v
e
r

-

D
C
I
(

s
i
s
o
n
g
a
d

i

l

i

u
f
g
n
n
a
e
m

s
e
d
o
c

)
C
T
A

(

g
u
r
d

d
n
a

)
0
1

y
l
l

a
c
i
n

i
l
c

n
o

e
r
o
m
d
e

i
l

e
r

.

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

l

a
c
i
d
e
m

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
t
s
e
g
g
u
s

,
s
e
d
o
c

g
n

i
l
l
i

b

n
a
h
t

i

s
t
n
e
d
a
r
g

d
e
t
a
r
g
e
t
n

I

s
t
s
o
c

g
n
i
s
a
e
r
c
e
d

;
)
e
g
d
i
r

4
0
0

.

1
2
0

.

s
v
(

.

4
2
0
¼
C
R
P
U
A

.
)
e
g
d
i
r

.

n
o
i
t
a
c
i
f
i
s
s
a
l
c

e
r
u
t
a
e
f

l

i

a
n
o
i
s
n
e
m
d
-
4
2
0
3
3
3

,

r
e
t
f
a

t
n
e
i
t
a
p

r
e
p

r
o
t
c
e
v

.

g
n
i
r
e
t
l
i
f

y
c
n
e
u
q
e
r
f

l

e
b
m
e
s
n
e

d
e
d
a
e
h
-
i
t
l
u
M

M
T
S
L
-
N
N
C

l

e
b
m
e
s
n
e

e
h
T

,
)
E
A
M

(

r
o
r
r
E

l

e
t
u
o
s
b
A

n
a
e
M

,
r
e
d
n
e
g

,

e
g
a
(

s
c
i
h
p
a
r
g
o
m
e
D

d
e
t
a
r
g
e
t
n

I

e
v
i
s
s
e
r
g
e
R

o
t
u
A

M
T
S
L

d
e
d
a
e
H
-
i
t
l
u
M

l

e
v
e
l
-
t
n
e
i
t
a
p

e
g
a
r
e
v
A

i

.
s
w
o
d
n
w
n
o
i
t
a
v
r
e
s
b
o

s
v
(

.

8
0
0
¼
C
R
P
U
A

:
s
t
n
e
i
t
a
p

e
g
n
a
h
c
-
t
s
o
c

r
o
f

C
O
R
U
A

g
n
i
s
a
e
r
c
n
i
-
t
s
o
c

g
n
i
y
f
i
t
n
e
d

i

d
n
a

)
C
R
P
U
A

(

e
v
r
u
c

d
n
a

!

,

e
g
a

,

x
e
s

,
)

G
F
(

s
y
e
k

s
t
s
o
c

c
i
f
i
c
e
p
s
-
r
o
t
c
e
s

.

.
)
6
2
0
(cid:3)

2
R
(

A
S
R
-
i
b
r
o
M

l
l

a
c
e
R
–
n
o
i
s
i
c
e
r
P

r
e
d
n
u

y
t
l
a
i
c
e
p
s

n
a
i
c
i
s
y
h
p

,
s
e
d
o
c

l

a
n
o
i
t
i
d
a
r
t

d
n
a

n
o
i
s
s
e
r
g
e
r

t
s
o
c

l
l

a
r
e
v
o

r
o
f

s
e
n

i
l

e
s
a
b

e
g
n
a
h
c
-
t
s
o
c

d
n
a

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

.

n
o
i
t
a
c
i
f
i
t
n
e
d

i

r
e
g
r
a

l

h
t
i

w
d
e
v
o
r
p
m

i

e
g
d
i
r

d
e
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

y
l
l

a
i
t
n
a
t
s
b
u
s

k
r
o
w
t
e
n

p
e
e
d

e
h
T

r
e
g
n
o

l

d
n
a

a
t
a
d

i

g
n
n
a
r
t

i

d
n
a

r
o
F

E
P
A
M

,

.

2
3
6
0
¼
q

M
P
C

,

.

6
6
2
0
¼

2
R

i

g
n
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

–

,

,

7
2
5
0
¼

.

r

4
0
0
2
e
¼

.

6
2
3
0
¼

)
6
2
1
2
e
¼
E
P
A
M

¼

2
R
(

n
o
i
s
s
e
r
g
e
r

e
g
d
i
r

,

0
6
2
0

.

l

:
)
e
b
m
e
s
n
e
(

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

,
)
r
(

n
o
i
t
a
e
r
r
o
c

l

n
o
s
r
a
e
P

l

a
n
o
i
s
n
e
m
d
-
h
g
H

i

i

n
a
e
M

,
)

q

(

n
a
m
r
a
e
p
S

r
e
p

s

i

m
a
l
c

f
o

n
o
i
t
a
t
n
e
s
e
r
p
e
r

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

l

e
t
u
o
s
b
A

-

D
C

I

:
)
s
r
e
t
r
a
u
q

4
2
(

r
e
t
r
a
u
q

,
2
R

,
)
e

,

E
P
A
M

(

r
o
r
r
E

g
u
r
d

C
T
A

i

,
s
e
s
o
n
g
a
d
M
G
-
0
1

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

i

s
g
n
m
m
u
C

’

a
e
r
A

,
)

M
P
C
(

e
r
u
s
a
e
M

g
n

i
l
l
i

b

S
P
O

,

G
R
D

,
s
e
d
o
c

P
O
G

,
s
e
r
u
d
e
c
o
r
p

,

h
c
a
e

s
n
o
r
u
e
n

0
5

,
s
r
e
y
a

l

t
u
o
p
o
r
d

,

n
o
i
t
a
v
i
t
c
a

U
L
e
R

,
r
e
z
i
m

i
t
p
o
M
A
D
A

,

5
2
0

.

.
)
s
n
u
r

5

f
o

l

e
b
m
e
s
n
e

e
s
a
e
r
c
e
d

r
o

e
s
a
e
r
c
n
i
(

n
e
e
w
t
e
b

l

d
o
f
-
0
0
1
>

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

e
g
n
a
h
c

.
)
s
d
o
i
r
e
p

n
o
i
s
s
e
r
g
e
r

e
g
d
R

i

r
e
y
a

l
i
t
l
u
m
d
e
t
c
e
n
n
o
c
-
y
l
l

u
F

e
r
a
c
-
h
t
l
a
e
h

r
a
e
y
-
e
n
o

l

a
t
o
T

.
l

a

t
e

s
s
o
B
-
e
w
e
r
D

n
e
d
d
h

i

4
(

n
o
r
t
p
e
c
r
e
p

t
s
o
c

d
n
a

)
s
o
r
u
E
(

s
t
s
o
c

0
1

)
2
2
0
2
(

8
1

)
0
2
0
2
(

.
l

a

t
e

k
i
h
s
u
a
K

d
e
r
a
u
q
S

n
a
e
M

t
o
o
R

n
a
e
M

,
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
E

e
g
a
t
n
e
c
r
e
P

l

e
t
u
o
s
b
A

2
R

d
n
a

,
)
E
P
A
M

(

r
o
r
r
E

.
)
n
o
i
t
a
n
m
r
e
t
e
D

i

f
o

t
n
e
i
c
i
f
f
e
o
C
(

i

y
t
i
d
b
r
o
m
o
c

,
s
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
r
p

n
o
i
t
a
z
i
l
i
t
u

g
u
r
d

,
s
r
o
t
a
c
i
d
n

i

f
o

r
e
b
m
u
n

,
)
n
o
g
e
r

i

i

s
u
o
v
e
r
p

d
n
a

,
s
e
t
a
r

.
s
d
n
e
r
t

e
r
u
t
i
d
n
e
p
x
e

e
g
a
r
e
v
A

i

g
n
v
o
M

d
e
d
a
e
H
-
i
t
l
u
M

/
)

M
T
S
L
H
M

(

)

A
M
R
A

I

(

d
i
r
b
y
H
/
)
N
N
C
H
M

(

N
N
C

l

e
b
m
e
s
n
e
M
T
S
L
-
N
N
C

l

e
d
o
m
M
T
S
L

d
e
k
c
a
t
S

e
m

i
t

r
e
p

s
e
r
u
t
i
d
n
e
p
x
e

/
y
l
k
e
e
w

(

d
o
i
r
e
p

.
)
y
l
h
t
n
o
m

r
o
(

e
r
a
c
h
t
l
a
e
h

)
n
o
i
t
a
c
i
d
e
m

---

<!-- PAGE 9 -->

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

d
e
i
f
i
t
n
e
d

I

-
i
t
l
u
m

f
o

t
s
o
c

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
C

p
e
e
d

k
s
a
t
-
i
t
l
u
m
d
n
a
w
e
v

i

y
t
i
l
i

b
a
z
i
l

a
r
e
n
e
g

d
e
t
i

m
i
L

R
M
E

e
s
e
n
h
C

i

d
n
o
y
e
b

.
s

m
e
t
s
y
s

.

i

g
n
n
a
r
t

i

i

g
n
n
r
a
e

l

o
t
n

i

t
h
g
i
s
n

i

d
e
t
i

m

i
l

i

s
e
d
v
o
r
p

t
c
e
f
f
a

s
e
r
u
t
a
e
f

l

a
u
t
x
e
t

w
o
h

s
l
a
t
i
p
s
o
h

s
s
o
r
c
a

n
o
i
t
a
d

i
l

a
v

.
s
e
i
r
t
n
u
o
c

r
o

g
n
i
s
s
i

m
o
t

e
u
d

s
a
b

i

l

a
i
t
n
e
t
o
P

R
M
E

s
s
o
r
c
a

s
e
i
c
n
e
t
s
i
s
n
o
c
n

i

i

g
n
d
o
c

r
o

a
t
a
d

l

a
n
r
e
t
x
e

f
o

e
c
n
e
s
b
A

.
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

x
o
b
-
k
c
a
b
(

l

s
t
u
p
t
u
o

l

e
d
o
m

d
n
a

y
c
n
e
r
a
p
s
n
a
r
t

f
o

k
c
a
L

N
N
R

n

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

i

c
i
m
o
n
o
c
e
o
i
c
o
s

f
o

e
c
n
e
s
b
A

-
s

i

m
a
l
c

d
n
o
y
e
b

l

s
e
b
a
i
r
a
v

y
t
i
l
i

b
a
z
i
l

a
r
e
n
e
g

d
e
t
i

m
i
L

i

d
a
c
i
d
e
M
e
h
t

e
d
i
s
t
u
o

.
s
e
r
u
t
a
e
f

d
e
s
a
b

.

l

n
o
i
t
a
u
p
o
p

.
)
n
o
i
t
a
t
i

m

i
l

.
s

m
e
t
s
y
s

s
i
s
y
l
a
n
a

y
t
i
u
q
e

r
o

s
s
e
n
r
i
a
f

o
N

e
v
i
s
n
e
t
n

i

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
C

.

d
e
d
u
l
c
n

i

P
U
R

:

y
t
i
l
i

i

b
a
n
a
p
x
e

l

d
e
t
i

m
i
L

.

i

g
n
n
u
t

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
p
y
h

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
d

d
e
t
i

m

i
l

d
n
a

i

g
n
n
a
r
t

i

–

–

–

–

–

–

–

–

–

–

JOURNAL OF MEDICAL ECONOMICS

661

l

e
p
m
a
s

l
l

a
m

s

o
t

d
e
t
u
b
i
r
t
t
a

.

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
e
t
i

m

i
l

d
n
a

.
)
y
l
n
o

a
t
a
d

l

a
n
o
i
t
c
e
s
-
s
s
o
r
c
(

e
u
d

F
R

n

i

g
n
i
t
t
i
f
r
e
v
o

l

e
b
i
s
s
o
P

s
e
r
u
t
a
e
f

l

a
r
o
p
m
e
t

f
o

k
c
a
L

–

–

:

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
r
e
d
n
u

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

d
e
t
i

m

i
l

i

n
a
m
e
r

y
c
n
e
r
a
p
s
n
a
r
t

.
s
e
h
c
a
o
r
p
p
a

L
M

r
o
f

o
t

e
z
i
l

a
r
e
n
e
g

t
o
n

y
a
m

s
t
l
u
s
e
R

r
o

s

m
e
t
s
y
s

e
r
a
c
h
t
l
a
e
h

r
e
h
t
o

–

.
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
s
o
c

.
t
e
s

l

e
b
a
i
r
a
v

e
g
r
a

l

o
t

d
n
a

y
t
i
l
i

i

b
a
n
a
p
x
e

l

l

e
d
o
M
–

d
e
e
n
-
h
g
h

i

t
s
o
c
-
h
g
h

i

g
n
o
m
a

l

y
l
r
a
u
c
i
t
r
a
p

,
s
e
r
u
t
i
d
n
e
p
x
e

l

e
d
o
m
N
N
R

e
h
T

.
s
t
n
e
i
t
a
p

l

a
c
i
s
s
a
l
c

d
e
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

r
a
e
n
i
L

,

O
S
S
A
L
(

n
o
i
s
s
e
r
g
e
r

l

e
b
m
e
s
n
e

d
n
a

)
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

g
n
i
t
h
g

i
l

h
g
h

i

,
)

M
B
G

(

s
l
e
d
o
m

o
s
l
a

t
I

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

i

g
n
d
n
e
p
s

l

a
r
o
p
m
e
t

t
a
h
t

d
e
z
i
s
a
h
p
m
e

t
n
e
c
e
r

.

.

g
e
(

s
e
r
u
t
a
e
f

e
r
e
w

)
s
e
i
r
o
t
c
e
j
a
r
t

i

g
n
d
n
e
p
s

c
i
t
a
t
s

n
a
h
t

e
v
i
t
c
i
d
e
r
p

e
r
o
m

r
o

s
c
i
h
p
a
r
g
o
m
e
d

t
n
e
i
t
a
p

r
o
f

i

g
n
n
r
a
e

l

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

e
r
a
c
h
t
l
a
e
h

c
i
m
a
n
y
d

f
o

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

e
h
t

.
s
e
s
o
n
g
a
d

i

i

R
H

¼

,

,

8
3
3
1
e
¼
E
A
M

,

5
7
4
0

.

2
R
-
j
d
a

:

M
L
G

–

;
.

%
7
6
¼

i

R
H

,

,

5
3
6
1
e
¼
E
A
M

,

7
4
3
0

.

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

–

;
.

%
8
5
¼

¼
E
A
M

,

.

6
1
3
0
¼

.

%
5
5
¼
R
H

i

,

2
R
-
j
d
a

0
6
6
1
e

,

i

g
n
w
o
h
s

,
s
d
o
i
r
e
p

t
s
o
c

r
o
i
r
p

-
e
m

i
t

e
r
u
t
p
a
c

o
t

y
t
i
l
i

b
a

s
t
i

.
s
n
r
e
t
t
a
p

t
s
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

e
t
a
u
a
v
e

l

o
t

d
e
d
u
l
c
n

i

e
r
e
w

.

e
c
n
e
t
s
i
s
r
e
p

l

a
r
o
p
m
e
t

n

i

e
c
n
e
t
s
i
s
r
e
p

l

a
r
o
p
m
e
t

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

n

i

O
S
S
A
L

,
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
E

d
e
r
a
u
q
S

,
)
n
o
g
e
r

i

,
r
e
d
n
e
g

,

e
g
a
(

d
n
a

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

O
S
S
A
L

g
n
i
r
u
t
p
a
c

,
)

N
N
R
(

d
e
s
a
b
-
e
e
r
t

d
n
a

n
o
i
s
s
e
r
g
e
r

,
s
c
i
r
t
e
m

l
l

a

s
s
o
r
c
a

s
l
e
d
o
m

l

a
n
o
i
t
i
d
a
r
t

d
e
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

y
t
i
l
i

b
a
p
a
c

s
t
i

g
n
i
t
a
r
t
s
n
o
m
e
d

.

y
l
e
v
i
t
c
e
f
f
e

a
t
a
d

d
e
r
u
t
c
u
r
t
s

/
s
i
s
o
n
g
a
d

i

f
o

n
o
i
s
u
l
c
n

i

e
h
T

d
n
a

l

a
u
t
x
e
t

e
t
a
r
g
e
t
n

i

o
t

s
a
w
n
o
i
s
u
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
t
n
e
t
t
a

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

r
o
f

l

a
c
i
t
i
r
c

d
n
a

s
t
x
e
t

n
o
i
t
a
r
e
p
o

)
P
U
R
(

h
c
a
o
r
p
p
a

.
s
n
a
g

i

l
l

a

n
a
h
t

r
e
w
o

l

y
l
t
n
a
c
i
f
i
n
g
i
s

.

.
)
1
0
0
0
<
p
(

s
e
n

i
l

e
s
a
b

d
n
a

t
s
o
c

r
o
f

.

S
O
L

r
o
f

.

0
8
0
>

.

1
5
4
0

.

.

5
8
0
>

:

E
A
M
–

:

C
C
P

–

e
h
t

,

F
R

d
n
a
M
B
G

o
t

d
e
r
a
p
m
o
C

d
e
c
u
d
e
r

l

e
d
o
m
P
U
R

y
b

r
o
r
r
e

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

%
5
1
–
2
1
(cid:5)

.
)
C
C
P
(

t
n
e
i
c
i
f
f
e
o
C

s
i
s
o
n
g
a
d

i

n
o
i
s
s
i

m
d
a

d
n
a

.

e
d
o
c

m
o
d
n
a
R

,

e
e
r
T

l

e
d
o
M

i

t
n
e
d
a
r
G

,
)
F
R
(

t
s
e
r
o
F

l

n
o
i
t
a
e
r
r
o
C

,
s
u
t
a
t
s

e
g
r
a
h
c
s
i
d

,
s
r
o
t
a
c
i
d
n

i

5
M

,
)
T
D

(

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

s
i
s
o
n
g
a
D

i

:

a
t
a
d

d
e
r
u
t
c
u
r
t
s
n
U

)

M
B
G

(

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
t
s
o
o
B

m
o
r
f

s
t
x
e
t

d
r
o
w
a
i
v

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
n
a

d
e
d
o
c
n
e

s
R
M
E

i

.
s
g
n
d
d
e
b
m
e

,
s
r
o
t
a
c
i
d
n

i

l

e
v
e
l
-
t
n
e
m

t
r
a
p
e
d

.
s
e
d
o
c

p
u
o
r
g

e
c
r
u
o
s
e
r

d
n
a

d
e
t
a
g
e
r
g
g
A

:
s
e
r
u
t
a
e
f

d
e
v
i
r
e
D

,
s
t
n
u
o
c

n
o
i
t
a
r
e
p
o

n
o
i
t
n
e
t
t
a
þ
g
n
d
d
e
b
m
e

i

g
n
i
s
u
(

r
e
d
o
c
n
e

d
r
o
c
e
r

s
u
o
e
n
e
g
o
r
e
t
e
h

e
r
u
t
p
a
c

w
e
v

i

h
c
a
E

.
s
e
c
r
u
o
s

a
t
a
d

s
i
s
o
n
g
a
d

i

,

d
e
r
u
t
c
u
r
t
s
(

s
a
w

)
t
x
e
t

n
o
i
t
a
r
e
p
o

,
t
x
e
t

d
n
a

y
l
e
t
a
r
a
p
e
s

d
e
d
o
c
n
e

.

n
o
i
s
u
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
t
n
e
t
t
a

h
g
u
o
r
h
t

d
e
t
a
r
g
e
t
n

i

o
t

r
o
t
c
i
d
e
r
p

e
c
r
u
o
s
e
r

a

d
n
a

)
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

k
s
a
t
-
i
t
l
u
m
a
i
v

y
l
t
n
o

i

j

e
r
e
w
h
t
o
B

d
e
t
c
i
d
e
r
p

.

i

g
n
n
r
a
e

l

,
)
t
s
o
c
(

3
9
6
0

.

:

E
S
M
R

:

d
e
v
e
h
c
a

i

–

l

e
t
u
o
s
b
A

n
a
e
M

,
)
E
S
M
R
(

n
o
s
r
a
e
P

,
)
E
A
M

(

r
o
r
r
E

n
o
i
t
a
r
e
p
o

,

e
p
y
t

n
o
i
s
s
i

m
d
a

,
t
n
e
m

t
r
a
p
e
d

l

a
t
i
p
s
o
h

,
)
R
V
S
(

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

a

i

s
e
n
b
m
o
c

)
k
r
o
w
t
e
n

–

l

a
r
u
e
n

k
s
a
t
-
i
t
l
u
m

d
n
a

)
Y
N
C
(

s
t
s
o
c

l

a
t
i
p
s
o
h

.
)
s
y
a
d
(

y
a
t
s

f
o

h
t
g
n
e

l

i

g
n
n
r
a
e

l

i

p
e
e
d
w
e
v
-
i
t
l
u
m
e
h
T

l

e
d
o
m
g
n
n
r
a
e

i

l

p
e
e
d

P
U
R

e
h
T

r
o
r
r
E

d
e
r
a
u
q
S

n
a
e
M

t
o
o
R

,

x
e
s

,

e
g
A

:

a
t
a
d

d
e
r
u
t
c
u
r
t
S

,
)
R
L
(

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

r
a
e
n
i
L

,

i

w
e
v
-
i
t
l
u
m

(

l

e
d
o
m
P
U
R

-
n

i

:
s
t
e
g
r
a
t

s
u
o
u
n
i
t
n
o
c

o
w
T

9
1

)
1
2
0
2
(

.
l

a

t
e

u
Y

i

s
g
n
d
n
F

i

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
m
r
o
f
r
e
p

l

e
d
o
M

g
n
i
t
a
u
a
v
e

l

r
o
f

d
e
s
u

s
c
i
r
t
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

n

i

d
e
d
u
l
c
n

i

s
e
r
u
t
a
e
F

d
e
r
a
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
e
h
t
O

e
p
y
t

l

e
d
o
m
g
n
n
r
a
e

i

l

p
e
e
D

.

.

g
e
(

l

e
b
a
i
r
a
v

e
m
o
c
t
u
O

y
d
u
t
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
p

l

e
d
o
m

l

)
e
b
a
i
r
a
v

t
e
g
r
a
t

.

d
e
u
n
i
t
n
o
C

.

2

e
l
b
a
T

g
n
o
r
t
s

d
n
u
o
f

y
d
u
t
s

e
h
T

d
n
a
M
B
G

d
e
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

N
N
R

n
a
e
M

t
o
o
R

,
)

2
R
(

d
e
r
a
u
q
s
-
R

s
c
i
t
s
i
r
e
t
c
a
r
a
h
c

c
i
h
p
a
r
g
o
m
e
D

,
)
R
L
(

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

r
a
e
n
i
L

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

t
n
e
r
r
u
c
e
R

h
t
n
o
M

r
e
P

r
e
b
m
e
M

r
e
P

0
2

)
8
1
0
2
(

.
l

a

t
e

g
n
a
Y

e
r
a
c
h
t
l
a
e
h

l

i

a
u
d
v
d
n

i

i

s
e
u
a
v

l

d
e
r
a
u
q
s
-
R

.

y
c
a
r
u
c
c
a

N
H
C
H

r
o
f

r
o
r
r
e

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

e
h
t

o
t

d
e
r
a
p
m
o
c

s
t
n
e
i
t
a
p

N
N
R

.

l

n
o
i
t
a
u
p
o
p

l

a
r
e
n
e
g

r
e
w
o

l

;

7
0

.

n
a
h
t

r
e
t
a
e
r
g

4
–
3

g
n
i
t
a
r
o
p
r
o
c
n

i

n
e
h
w

d
e
v
o
r
p
m

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
c

d
n
a

r
o
r
r
e

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
s
o
r
c
a

s
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

s
i
s
o
n
g
a
d
(

i

s
e
r
u
t
a
e
f

l

a
c
i
n

i
l
c

l

a
c
i
r
o
t
s
i
h

,
)
e
s
u

n
o
i
t
a
c
i
d
e
m

,
s
e
d
o
c

e
r
u
d
e
c
o
r
p

,
s
e
d
o
c

g
n
i
t
s
o
o
B

i

t
n
e
d
a
r
G

y
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

l
l

a

–

)

M
B
G

(

i

e
n
h
c
a
M

e
c
n
e
u
q
e
s

d
n
a

l

e
b
a
i
r
a
v

s
u
o
u
n
i
t
n
o
c

i

t
s
n
a
g
a

d
e
k
r
a
m
h
c
n
e
b

s
s
o
r
c
a

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
r
u
t
u
f

l

a
t
o
t

g
n
i
t
n
e
s
e
r
p
e
r

)
s
h
t
n
o
m
4
–
1

l

e
p
i
t
l
u
m

r
e
v
o

s
t
s
o
c

r
o
i
r
P

f
o

s
g
a
l
(

s
d
o
i
r
e
p

.
s
r
o
t
a
c
i
d
n

i

i

y
t
i
d
b
r
o
m
o
c

d
n
a

.
s
t
i
l

p
s

.

a
t
a
d

n
o
i
t
a
z
i
l
i
t
u

d
n
a

t
s
o
c

.
s
l
e
d
o
m

,
s
n
r
e
t
t
a
p

n
o
i
t
a
z
i
l
i
t
u

d
n
a

t
s
o
c

a
t
a
d

l

a
c
i
t
n
e
d

i

r
o
f

N
N
R

r
o
i
r
p

f
o

s
h
t
n
o
m
e
p
i
t
l
u
m

l

.
t
n
e
i
t
a
p

r
e
p

t
s
o
c

e
r
a
c
h
t
l
a
e
h

)

M
P
M
P
(

—

e
r
u
t
i
d
n
e
p
x
e

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

–

¼

2
R
-
j
d
a

:
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

–

,

5
7
4
0

.

f
o

2
R
-
j
d
a

n
a

d
e
v
e
h
c
a

i

F
R

,
)

2
R
-
j
d
a
(

d
e
r
a
u
q
s
-
R

d
e
t
s
u
d
A

j

g
n
i
t
s
i
x
e
-
e
r
p

,
r
e
d
n
e
g

,

e
g
A

l

e
d
o
M

r
a
e
n
i
L

d
e
z
i
l

a
r
e
n
e
G

l

a
r
u
e
N

d
r
a
w
r
o
f
-
d
e
e
F

l

i

a
u
d
v
d
n

i

i

l

a
u
n
n
A

1
2

)
2
2
0
2
(

.
l

a

t
e

t
n
o
m
V

i

E
A
M

,

6
1
3
0

.

f
o

2
R
-
j
d
a

n
a

d
a
h

%
5
5

f
o

i

R
H

d
n
a

,

0
6
6
1
e

f
o

l

a
u
t
c
a

f
o

e

l
i
c
e
d

p
o
t

e
h
t

.

e
r
u
t
i
d
n
e
p
x
e

l

a
t
o
t

r
a
e
y
-
r
o
i
r
p

d
n
a

.
s
t
s
o
c

e
r
a
c
h
t
l
a
e
h

n

i

s
l
a
u
d
v
d
n

i

i

i

t
s
o
c
-
h
g
h

i

i

,
)
g
n
g
a
m

i

,
s
n
o
i
t
a
c
i
d
e
m

,
s
y
a
t
s

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

;

%
8
5

f
o

i

R
H

d
e
i
f
i
t
n
e
d

i

y
l
t
c
e
r
r
o
c

f
o

l

a
t
i
p
s
o
h

,
s
n
o
i
t
a
t
l
u
s
n
o
c
(

.
)
F
R
(

t
s
e
r
o
F

.
s
e
t
a
i
r
a
v
o
c

f
o

2
R
-
j
d
a

n
a

d
n
a

,

5
3
6
1
e

d
a
h
M
L
G

;

%
7
6

f
o

E
A
M

,

7
4
3
0

.

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

o
i
t
a
R

t
i
H

d
n
a

,
)
E
A
M

e
h
t
—
)
R
H

i

(

(

f
o

i

R
H

d
n
a

,

8
3
3
1
e

f
o

E
A
M

r
o
r
r
E

l

e
t
u
o
s
b
A

n
a
e
M

n
o
s
l
r
a
h
C

,
s
n
o
i
t
i
d
n
o
c

,

x
e
d
n

i

i

y
t
i
d
b
r
o
m
o
c

n
o
i
t
a
z
i
l
i
t
u

e
r
a
c
h
t
l
a
e
h

g
o

l

h
t
i

w
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

,
s
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
a
v
i
t
c
a

s
u
o
u
n
i
t
n
o
c
(

6
1
0
2

n

i

a
m
m
a
g
(

)

M
L
G

(

r
a
e
n

i
l

n
o
n

h
t
i

w
k
r
o
w
t
e
N

e
r
u
t
i
d
n
e
p
x
e

e
r
a
c
h
t
l
a
e
h

m
o
d
n
a
R

d
n
a

)
k
n

i
l

l

e
v
e
l
-
t
n
e
i
t
a
p

n
o

d
e
n
a
r
t

i

.
)
s
o
r
u
e

n

i

,

l

e
b
a
i
r
a
v

---

<!-- PAGE 10 -->

662

J. T. LEE ET AL.

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

d
e
i
f
i
t
n
e
d

I

e
h
t

f
o

–

s
s
e
n
e
v
i
t
a
t
n
e
s
e
r
p
e
r

t
e
s
a
t
a
d

n
o
i
t
a
c
i
d
e
m

l

e
g
n
i
s

a

o
t

d
e
t
i

m

i
l

r
a
e
l
c
n
u

d
n
a

n
o
i
t
a
d

i
l

a
v

l

a
n
r
e
t
x
e

f
o

e
c
n
e
s
b
A

–

t
s
o
c

d
n
a

a
e
r
a

c
i
t
u
e
p
a
r
e
h
t

f
o

k
c
a

l

–

e
p
y
t

l

a
c
i
n

i
l
c

d
n
a

c
i
m
o
n
o
c
e
o
i
c
o
s

r
e
d
a
o
r
b

–

i

g
n
d
n
e
p
s

e
r
a
c
h
t
l
a
e
h

o
t

y
t
i
l
i

b
a
z
i
l

a
r
e
n
e
g

s
t
c
i
r
t
s
e
r

s
e
r
u
t
a
e
f

t
o
n

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

l

e
d
o
m

e
t
a
i
r
a
v
n
u

i

o
t

d
e
t
i

m

i
l

l

e
d
o
M
–

.

d
e
s
s
u
c
s
i
d

d
e
t
a
r
e
n
e
g

d
n
a

l

a
e
r

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
a
p
e
r
c
s
i
d

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
c
u
d
e
r

y
l
l

u
f
s
s
e
c
c
u
s

,
s
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

e
r
u
t
i
d
n
e
p
x
e

l

a
n
o
i
t
i
d
a
r
t

i

g
n
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

,

M
T
S
L
(

s
e
n

i
l

e
s
a
b

i

g
n
n
r
a
e

l

d
e
v
o
r
p

l

e
d
o
m
e
h
T

.
)
P
L
M

r
o
f

e
v
i
t
c
e
f
f
e

l

y
l
r
a
u
c
i
t
r
a
p

y
r
a
n
o
i
t
a
t
s
-
n
o
n

g
n

i
l

e
d
o
m

e
r
u
t
i
d
n
e
p
x
e

e
r
a
c
h
t
l
a
e
h

p
e
e
d

d
n
a

n
o
i
s
s
e
r
g
e
r

s
l
e
d
o
m
M
T
S
L

h
t
o
B

.
s
e
i
r
e
s

.
)
s
e
t
a
i
r
a
v
o
c

c
i
m
o
n
o
c
e
o
i
c
o
s

n
o
i
t
a
d

i
l

a
v

l

a
n
r
e
t
x
e

f
o

k
c
a
L

o
n
(

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

r
o

c
i
h
p
a
r
g
o
m
e
d

d
e
s
a
b

s
t
l
u
s
e
R

.
s
n
o
i
t
a
u
p
o
p

l

–

r
o

s
e
p
y
t

n
o
i
t
a
c
i
d
e
m

s
s
o
r
c
a

y
r
o
g
e
t
a
c

g
u
r
d

l

e
g
n
i
s

a

n
o

g
n
i
t
i

m

i
l

,
)
n
o
i
t
a
c
i
d
e
m
n
a
p
(

i

d
e
s
o
p
o
r
p

k
r
o
w
e
r
u
t
u
F

.

y
t
i
l
i

b
a
z
i
l

a
r
e
n
e
g

g
n
i
t
a
r
o
p
r
o
c
n

i

s
l
e
d
o
m
M
T
S
L

r
o
f

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

n
o
i
t
a
c
i
d
e
m

t
s
o
c

e
r
a
c
h
t
l
a
e
h

r
e
d
a
o
r
b

l

e
p
i
t
l
u
m
o
t

i

g
n
d
n
a
p
x
e

d
n
a

s
c
i
h
p
a
r
g
o
m
e
d

.

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
g
n
p
o
e
v
e
d

l

i

–

–

.

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

e
v
i
t
c
i
d
e
r
p

t
s
e
b

e
h
t

i

d
e
v
e
h
c
a
M
T
S
L

d
e
k
c
a
t
S

.

A
M
R
A

I

d
e
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

,
t
s
u
b
o
r

e
r
o
m
e
r
e
w
s

M
T
S
L

r
e
t
t
e
b

d
n
a

,
c
i
r
t
e
m
a
r
a
p
n
o
n

l

a
r
o
p
m
e
t

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

:

n
o
i
t
a
c
i
l

p
m

I

.
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

d
n
a

e
r
u
t
i
d
n
e
p
x
e

e
r
a
c
h
t
l
a
e
h

.

g
n
i
k
a
m
y
c
i
l

o
p

t
r
o
p
p
u
s

l

d
u
o
c

s

M
T
S
L

n

i

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

l

i

i

a
m
n
m
e
h
t

s
a

d
e
t
a
c
i
d
n

i

)
.
s
r
o
t
a
r
a
p
m
o
c

g
n
o
m
a

¼

2
R

,

.

5
5
8
6
1
¼
E
S
M
R

:

A
M
R
A

I

5
4
0
8
0

.

¼

¼

2
R

,

.

7
1
6
4
1
¼
E
S
M
R

y
r
o
m
e
m
7
(

M
T
S
L

:
)
s
l
l

e
c

d
r
a
d
n
a
t
S

2
R

,

.

3
9
6
3
1
¼
E
S
M
R

:
)
s
l
l

e
c

y
r
o
m
e
m
4
þ
4
(

M
T
S
L

d
e
k
c
a
t
S

8
4
0
8
0

.

9
5
1
8
0

.

k
r
o
w
e
m
a
r
f

N
A
G
-
V

e
h
T

t
s
e
w
o

l

e
h
t

d
e
v
e
h
c
a

i

N
A
G
-
V

e
h
T

r
o
r
r
E

e
r
a
u
q
S

n
a
e
M

t
o
o
R

d
n
a

s
c
i
h
p
a
r
g
o
m
e
d

t
n
e
i
t
a
P

,
)
R
L
(

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

r
a
e
n
i
L

e
v
i
t
a
r
e
n
e
G

d
e
s
a
B
-
e
c
n
a
i
r
a
V

e
r
u
t
i
d
n
e
p
x
e

e
g
a
r
e
v
a

y
l
i

a
D

i

s
g
n
d
n
F

i

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
m
r
o
f
r
e
p

l

e
d
o
M

g
n
i
t
a
u
a
v
e

l

r
o
f

d
e
s
u

s
c
i
r
t
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

n

i

d
e
d
u
l
c
n

i

s
e
r
u
t
a
e
F

d
e
r
a
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
e
h
t
O

e
p
y
t

l

e
d
o
m
g
n
n
r
a
e

i

l

p
e
e
D

.

.

g
e
(

l

e
b
a
i
r
a
v

e
m
o
c
t
u
O

y
d
u
t
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
p

l

e
d
o
m

l

)
e
b
a
i
r
a
v

t
e
g
r
a
t

.

d
e
u
n
i
t
n
o
C

.

2

e
l
b
a
T

l
l

a

o
t

d
e
r
a
p
m
o
c

E
S
M
R

,
s
l
e
d
o
m
k
r
a
m
h
c
n
e
b

r
o
i
r
e
p
u
s

g
n
i
t
a
r
t
s
n
o
m
e
d

t
c
a
x
E
(

.

y
c
a
r
u
c
c
a

e
v
i
t
c
i
d
e
r
p

y
l
l

a
c
i
r
e
m
u
n

t
o
n

E
S
M
R

t
u
b

t
x
e
t

n

i

d
e
t
r
o
p
e
r

)
E
S
M
R
(

l

a
c
i
n

i
l
c

f
o

n
o
i
t
n
e
m
o
n

;

a
t
a
d

s
e
t
a
i
r
a
v
o
c

c
i
m
o
n
o
c
e
o
i
c
o
s

r
o

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
r
u
t
i
d
n
e
p
x
e

/
e
s
a
h
c
r
u
p

l

a
c
i
r
o
t
s
i
h

g
n
i
t
s
o
o
B

i

t
n
e
d
a
r
G

)
R
B
G

(

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

-
V
(

k
r
o
w
t
e
N

l

a
i
r
a
s
r
e
v
d
A

r
o
t
a
r
e
n
e
g

d
e
s
a
b
-
M
T
S
L

n
a

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

)

N
A
G

d
e
s
a
b
-
N
N
C

a

d
n
a

r
e
y
a

l
i
t
l
u
M

.
r
o
t
a
n
m

i

i
r
c
s
i
d

d
n
a

,
)
P
L
M

(

n
o
r
t
p
e
c
r
e
P

-
t
r
o
h
S

g
n
o
L

d
r
a
d
n
a
t
s

)

M
T
S
L
(

y
r
o
m
e
M
m
r
e
T

k
r
o
w
t
e
n

i

n
a
p

c
i
f
i
c
e
p
s

a

n
o

.

n
o
i
t
a
c
i
d
e
m

2
2

)
0
2
0
2
(

.
l

a

t
e

k
i
h
s
u
a
K

3
2

)
7
1
0
2
(

.
l

a

t
e

k
i
h
s
u
a
K

i

n
a
m
n

i

d
e
s
u

t
o
n

t
u
b

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
d
e
s
o
p
o
r
p

k
r
o
w
e
r
u
t
u
f
(

s
l
e
d
o
m

)
s
l
e
d
o
m

r
o
r
r
E

e
r
a
u
q
S

n
a
e
M

t
o
o
R

f
o

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
-
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
n
U

i

e
v
i
s
s
e
r
g
e
R

o
t
u
A

(

A
M
R
A

I

M
T
S
L

)
a

l
l
i

n
a
v
(

d
r
a
d
n
a
t
S

)
1
(

t
n
e
i
t
a
p

y
l
h
t
n
o
m
e
g
a
r
e
v
A

i

)
n
o
i
t
a
n
m
r
e
t
e
D

f
o

t
n
e
i
c
i
f
f
e
o
C
(

)
E
S
M
R
(

2
R

c
i
h
p
a
r
g
o
m
e
d

;
s
e
r
u
t
i
d
n
e
p
x
e

)
k
r
a
m
h
c
n
e
b

,

e
g
a
r
e
v
A

)
2
(

d
n
a

)
s
l
l

e
c

y
r
o
m
e
m
7
(

n
o
i
t
a
c
i
d
e
m
y
l
h
t
n
o
m

i

g
n
v
o
M
d
e
t
a
r
g
e
t
n

I

r
e
y
a

l

n
e
d
d
h

i

e
n
o

h
t
i

w

r
o
f

d
e
s
o
p
o
r
p
(

s
l
e
d
o
m
n
a
m

i

.
)
k
r
o
w
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
r
u
t
u
f

n

i

d
e
s
u

t
o
n

t
u
b

l

e
b
a

l
i

a
v
a

e
r
e
w

)
r
a
e
y

h
t
r
i
b

,

i

n
o
g
e
r

,
r
e
d
n
e
g

,

e
g
a
(

l

s
e
b
a
i
r
a
v

,
)
r
a
e
y

h
t
r
i
b

,

i

n
o
g
e
r

,
r
e
d
n
e
g

,

e
g
a
(

l

e
b
a

l
i

a
v
a

s
c
i
h
p
a
r
g
o
m
e
D

o
w

t

h
t
i

w
M
T
S
L

d
e
k
c
a
t
S

y
r
o
m
e
m
4
(

s
r
e
y
a

l

M
T
S
L

.
)
h
c
a
e

s
l
l

e
c

n
o
i
t
a
c
i
d
e
m
n
a
p

i

c
i
f
i
c
e
p
s

,

i

g
n
d
n
e
p
s

t
e
k
c
o
p
-
f
o
-
t
u
o
(

i

d
a
p
-
r
e
r
u
s
n

i

i

g
n
d
u
l
c
x
e

a

n
o

e
r
u
t
i
d
n
e
p
x
e

.
)
t
n
u
o
m
a

---

<!-- PAGE 11 -->

JOURNAL OF MEDICAL ECONOMICS

663

using LSTM and CNN models to support risk stratification and care coordination under value-based care
frameworks17. Two studies from Germany and France examined risk adjustment and insurance premium
prediction, using large national claims datasets to forecast annual healthcare costs and assess whether
deep or tree-based models improved fairness and predictive accuracy in reimbursement and capitation
formulas10,22. Both were conducted within statutory health insurance systems, emphasizing model trans-
parency and calibration for regulatory use10,21. A U.S. Medicaid study analyzed high-need, high-cost
(HCHN) populations, applying recurrent neural networks to predict per-member-per-month expendi-
tures20. A Chinese study using electronic medical records focused on hospital resource utilization, pre-
dicting in-hospital costs and length of stay with a multi-view DNN that combined structured and
unstructured clinical data19. This work supports hospital efficiency improvement and DRG-based pay-
linking predictive analytics to provider-level financial management19. Finally, three U.S.
ment reform,
studies addressed pharmaceutical expenditure forecasting, using claims or retail transaction data to pre-
dict weekly, monthly, or daily medication spending18,22,23.

Neural network architectures in the included studies

Neural network architectures were applied according to input type and temporal structure. Feedforward
deep neural networks handled static or high-dimensional features, capturing nonlinear relationships in
cross-sectional data. Recurrent networks (RNNs/LSTMs) modeled temporal dependencies in longitudinal
or multi-wave sequences. More complex architectures—including hybrid CNN-LSTM models, multi-head
ensembles, and generative frameworks (V-GANs)—were used for heterogeneous or non-stationary data,
integrating structured and unstructured inputs.

Across the studies, neural network design generally reflected data characteristics (see Table 3).
Feedforward DNN models were applied to static features21, while Vimont et al., 202221 included a simple
neural network alongside statistical models for comparison. Recurrent architectures captured temporal
dependencies when explicitly implemented, with convolutional neural networks (CNNs) and fully con-
nected networks (FCNs) used to process spatial and static features, respectively (e.g. Lewis et al. 202117)
Hybrid or generative models addressed complex temporal or heterogeneous inputs (Kaushik et al.
201723; 202022; Yu et al. 202119) However, some studies (e.g. Yang et al. 201820) primarily relied on tradi-
tional machine learning approaches.

Evaluation frameworks and performance metrics

All eight studies evaluated model performance using quantitative metrics aligned with their clinical or
policy objectives10,17–23. Six studies employed internal multi-split validation (train–validation–test or
cross-validation)17–19,21–23, while two—Drewe-Boss et al. (2022) and Yang et al. (2018)—used temporal
holdout samples to assess generalizability10,20. None performed full external validation across independ-
ent datasets.

Longitudinal prediction studies (n ¼ 6)—Drewe-Boss et al. (2022), two studies from Kaushik et al.
(2020), Kaushik et al. (2017), Yang et al. (2018), and Lewis et al. (2021)—focused on forecasting accuracy
reported RMSE (n ¼ 4)18–20,22,23 and some reported MAE
and discrimination10,17,18,20,22,23. Most
(n ¼ 2)10,18 and R2 or correlation coefficients (r, q) to quantify fit. Lewis et al. (2021) also included
AUROC, precision@k, and cost-capture to evaluate high-risk identification17, while Drewe-Boss et al.

Table 3. Neural network architectures applied in the included studies.
Neural network architecture

Data type

Models

Feedforward/DNN
Simple neural network

Static or high-dimensional data
Static or high-dimensional data

Standard deep neural network
Simple neural network

(comparison with statistical
models)

Recurrent

Longitudinal or time-dependent

RNN, LSTM (auxiliary: CNN, FCN)

Hybrid/generative

Complex temporal patterns,
heterogeneous data

Hybrid or generative models

(e.g. V-GAN)

data

Studies

Drewe-Boss et al. 202210
Vimont et al., 202221

Lewis et al. 202117

Kaushik et al. 201723; 202018;
202022; Yu et al. 202119

---

<!-- PAGE 12 -->

664

J. T. LEE ET AL.

(2022) and Kaushik et al. (2020) added AUPRC and Mean Absolute Percentage Error (MAPE), respectively,
for trend and cost-change detection10,18. Sequential models such as LSTM and CNN-LSTM were assessed
primarily on temporal forecasting stability and error reduction18,23.

Cross-sectional studies (n ¼ 2)—Vimont et al. (2022) and Yu et al. (2021)—emphasized model fit and
numerical error for static cost prediction19,21. Vimont et al. (2022) used adjusted R2, MAE, and Hit Ratio
to compare neural networks with GLM and Random Forest for national reimbursement modeling21. Yu
et al. (2021) evaluated RMSE, MAE, and Pearson correlation coefficient for in-hospital cost and length-of-
stay prediction19.

Across all papers, R2/adjusted R2 (n ¼ 5), MAE (n ¼ 4), RMSE (n ¼ 5), and AUC or related discrimination
metrics (n ¼ 2) were most frequently reported10,17–23. Only one study addressed calibration to a limited
extent19, and none included decision-curve, net-benefit, or fairness analyses.

Explainability frameworks such as Integrated Gradients was carried out in Drewe-Boss et al. (2022)10.

Comparative performance of neural networks versus classical models

Across studies comparing neural architectures with classical regression and ensemble methods, neural
models generally performed best when applied to longitudinal or temporally rich healthcare data10,17–23.
Recurrent and hybrid architectures captured temporal persistence and nonlinear dynamics that tradi-
tional approaches often missed. In a U.S. Medicaid study, Yang et al. (2018) showed that, for predicting
raw Per Member Per Month (PMPM) dollar amount expenditures, a recurrent neural network increased
test R2 from about 0.14–0.17 (for linear regression and GBM) to 0.30 and reduced RMSE by roughly one-
third, with similar improvements in RMSE among the top 10% highest-cost patients; on log- and per-
centile-transformed outcomes, R2 differences across models were smaller, but the RNN still achieved
lower overall and high-cost error.20 Kaushik et al. (2017) likewise found that stacked LSTMs improved
RMSE by nearly 19% over ARIMA forecasts for a medication-spending time series23, while a later multi-
headed CNN–LSTM, Convolutional LSTM, and CNN-LSTM ensemble achieved even stronger performance
with R2 values around 0.8–0.9 in patient-level forecasting18. Lewis et al. (2021) also reported that sequen-
tial deep models outperformed gradient boosting and logistic regression in predicting preventable hos-
pitalizations and costs, attaining AUROCs up to approximately 0.78.17

The picture was more mixed in cross-sectional cost prediction. In a French nationwide claims study,
Vimont et al. (2022) found that a relatively shallow two-hidden-layer MLP performed similarly to a gener-
alized linear model but was clearly outperformed by a random forest (adj-R2 0.475 vs.0.347 and 0.316
for GLM and neural network; MAE e1,338 vs. e1,635 and e1,660), suggesting limited benefit of shallow
neural architectures on tabular cost data21. By contrast,
in China, Yu et al. (2021) demonstrated that
when rich structured and textual EMR inputs were available, a multi-view deep learning model integrat-
ing diagnosis and operation text with structured features clearly surpassed all regression and tree-based
baselines, reducing prediction error by roughly 12–15%.19

Figure 2 illustrates roughly how predictive performance evolves as data become richer and more com-
plex. The x-axis moves from simple cross-sectional claims to increasingly heterogeneous, longitudinal, and
multimodal data; the y-axis represents relative model performance. Classical regression performs well for
simple, low-dimensional tabular inputs but tends to plateau as complexity increases. Tree-based machine-
learning models (e.g. random forests, gradient boosting) extend performance by capturing nonlinearities,
typically outperforming regression across most settings. It is important to note that Figure 2 is a concep-
tual framework developed to synthesize the evidence reviewed in this study and to illustrate the proposed
Complexity–Performance Hypothesis24. The figure is intended to visualize the overall performance trends
of different model families as data complexity increases and does not represent empirical estimates
derived directly from any individual study.

Shallow feed-forward neural networks (green) show the weakest performance in the cross-sectional
regime—consistent with Vimont et al. (2022), where a two-layer MLP achieved an adjusted R2 of only
0.316, below both RF (0.475) and GLM (0.347)21. Without sequential structure or rich feature representa-
tions, shallow networks offer limited advantage over traditional methods. However, deep neural architec-
tures (red) behave differently. Even in cross-sectional settings, when richer
input modalities are
available—as in the multi-view RUP model using structured and textual EMR features (Yu et al. 2021)—

---

<!-- PAGE 13 -->

JOURNAL OF MEDICAL ECONOMICS

665

Figure 2. Model performance by data complexity.

deep learning can clearly outperform both regression and tree-based baselines.19 As data become
increasingly high-dimensional, sequential, or multimodal, deep networks benefit from their higher cap-
acity and representation learning capabilities. This produces the strongest gains in the longitudinal/
multimodal regime, where studies such as Lewis et al. (2021), Yang et al. (2018), Kaushik et al. (2017/
2020), and Kaushik et al. (2020 V-GAN) show that recurrent, convolutional, and hybrid deep models out-
perform classical and ensemble methods by substantial margins17,18,20,22,23.

Building on these findings, we formulate what we term the Complexity–Performance Hypothesis,
which posits that model accuracy is maximized when the capacity of the modeling approach is matched
to the complexity of the data. When data are simple and homogeneous, classical regression performs
competitively, reflecting its efficiency in low-dimensional settings. As data gain nonlinear structure or
moderate dimensionality, tree-based machine-learning methods begin to offer clear advantages by cap-
turing interactions and flexible decision boundaries. With further increases in data richness—such as
large-scale, temporal, or multimodal inputs—DNN models provide the greatest performance gains, often
surpassing alternative approaches by a wide margin.

Discussion

Primary findings

Across the eight included studies, deep learning models demonstrated consistent performance gains
over classical regression, though the magnitude and nature of improvement varied by study design and
data type. The strongest advantages were observed in longitudinal analyses, while cross-sectional appli-
cations yielded smaller or mixed results. These results provide empirical support for the Complexity–
Performance Hypothesis, which proposes that predictive accuracy depends on how well a model’s archi-
tecture is matched to the underlying structure and complexity of the data.

In longitudinal or time-series prediction tasks, such as forecasting healthcare expenditures, hospitaliza-
tions, or medication costs, neural networks with sequential structures—particularly LSTM and CNN-
LSTM—achieved notable accuracy improvements, typically showing roughly 10–20% lower prediction
error (RMSE or MAE) and absolute R2 improvements of about 1–15 percentage points compared with
classical regression or autoregressive models. These architectures effectively captured temporal persist-
ence, nonlinear cost dynamics, and patterns of high-cost episodes that static models failed to represent.
In contrast, cross-sectional models predicting single-year or aggregated costs showed more limited
improvements. Shallow feed-forward neural networks performed similarly to or worse than classical
regressions—while tree-based methods such as random forests and gradient boosting often matched or
exceeded neural performance in overall fit and calibration. However, when unstructured or multimodal
inputs such as EMR text were incorporated, deep learning achieved clearer advantages, yielding larger

---

<!-- PAGE 14 -->

666

J. T. LEE ET AL.

error reductions and demonstrating greater flexibility in modeling heterogeneous clinical
information.
Taken together, these findings suggest that deep learning delivers its greatest advantages in settings
with temporal depth or multimodal complexity, whereas classical and ensemble methods can remain
competitive—or superior—when the task is cross-sectional and inputs are purely tabular or the neural
architecture is relatively shallow.

Across studies, feature importance patterns were highly consistent. Prior costs and utilization emerged
as the dominant predictors, followed by comorbidities, procedures, and medication use. Very few models
incorporated social determinants, behavioral data, or text-based clinical variables, limiting interpretability
and potential policy translation.

When compared across methodological families, deep learning outperformed classical regression in nearly
all contexts, but tree-based models remained highly competitive in cross-sectional settings that emphasize
transparency and calibration. Overall, the evidence suggests that deep learning excels when data are longitu-
dinal, high-dimensional, or sequential, while classical and tree-based methods continue to provide stable,
interpretable baselines for policy-oriented modeling such as risk adjustment and premium setting.

Although most included studies involved large sample sizes, often ranging from tens of thousands to sev-
eral million observations, these studies generally possessed sufficient statistical power to detect meaningful
performance improvements, such as significant reductions in RMSE or MAE. Nevertheless, the overall conclu-
sions remain influenced by contextual factors, including the concentration of studies within specific countries
or insurance systems and the reliance on single-database observational designs. Importantly, these limitations
do not overturn the overarching conclusion that deep learning offers advantages over traditional regression
in longitudinal time-series cost prediction. However, effect size estimates—particularly across specific popula-
tions, subgroups, or neural network architectures—should be interpreted with caution.

Through the integration of theoretical considerations and empirical evidence, this review articulates
the Complexity–Performance Hypothesis as a unifying framework to explain these findings. In data sce-
narios characterized by relatively low dimensionality or limited complexity, traditional regression models
are often sufficient to achieve effective prediction. As data complexity increases—through greater nonli-
nearity or interaction effects—tree-based machine learning models begin to demonstrate advantages in
flexibility and fit. When data are both high-dimensional and longitudinal or multimodal, DNN models
with hierarchical feature-learning capabilities exhibit the greatest potential to improve overall prediction
Importantly, this hypothesis is derived inductively from the eight
error and identify high-cost tails.
included empirical studies and is presented as a conceptual framework to guide model selection across
data structures and application scenarios, rather than as a precise estimate of a single causal effect.

Implications for health economics and policy

From a health economics and healthcare finance perspective, these findings translate into operational
guidance regarding when deep learning is most appropriate for real-world application. Specifically, deep
learning models are most relevant for healthcare cost prediction tasks that integrate longitudinal data or
multiple data modalities25. Under such conditions, neural networks tend to achieve lower overall predic-
tion error and demonstrate superior ability to identify high-cost populations, compared with traditional
In practice, this improved discrimination can support earlier
regression and some tree-based models.
identification of high-risk individuals and inform budget planning and resource allocation decisions26.

When sufficient data infrastructure, computational resources, and institutional support are available,
deploying high-complexity deep learning models can be cost-effective and analytically justified. By con-
trast, in cross-sectional risk-adjustment or insurance estimation settings—where available predictors are
limited to standard claims data or a small number of structured covariates—the empirical evidence indi-
cates that shallow neural architectures yield only marginal improvements in explanatory power or cali-
bration. In such scenarios, tree-based machine learning models often achieve comparable or superior
performance, while offering greater interpretability.

Moreover, under regulatory and governance constraints, tree-based models typically impose lower com-
munication and transparency costs when engaging with policymakers and supervisory agencies27.
Accordingly, GLM-based two-part models and selected tree-based approaches remain appropriate baseline
choices for many applied health economics analyses. Adoption of deep learning in these contexts should be

---

<!-- PAGE 15 -->

JOURNAL OF MEDICAL ECONOMICS

667

contingent upon direct head-to-head comparisons conducted on identical datasets and data partitions, dem-
onstrating reproducible and policy-relevant improvements in cost capture, budget accuracy, and high-cost
population monitoring.

including computational

Finally, practical deployment of deep learning models requires careful consideration of downstream
resource requirements,
infrastructure, MLOps maturity, and the capacity to
explain model behavior to decision-makers and regulators28. Within health economics, the Complexity–
Performance Hypothesis therefore implies not only a statistical matching between model capacity and
data structure, but also a balanced assessment of predictive gains, transparency, and institutional feasi-
bility. Given that most routine analytic workflows in insurance and public health agencies continue to
rely on GLM and tree-based models, the limited availability of readily deployable deep learning plat-
forms remains a non-trivial barrier to widespread adoption29.

Future directions and fundamental challenges

To guide future research, this review delineates five fundamental challenges in applying deep learning
to healthcare expenditure prediction, outlines actionable strategies for their resolution, and identifies pri-
orities for collaboration between machine learning scientists and health economists (see Table 4).

Challenge 1: limited economic interpretability
Despite the high predictive accuracy of deep learning architectures, their opaque internal representa-
tions constrain economic interpretation and policy translation34. The “black-box” nature of neural net-
works obscures causal pathways and cost-driver interactions, limiting their relevance for accountability
and decision-making in health financing27. To align model outputs with economic reasoning, deep learn-
ing models should integrate explainable-AI (XAI) approaches—such as SHAP,
Integrated Gradients, or
Layer-wise Relevance Propagation—and report marginal effects comparable to those derived from gen-
eralized linear or two-part models. Developing hybrid “interpretable-deep” frameworks that embed
econometric constraints within neural architectures may reconcile predictive precision with transparency,
facilitating their integration into budget-impact and resource-allocation analyses35.

Table 4. Challenges of deep learning in predicting healthcare spending and expenditure, and how they may be over-
come with future development.
Challenges

Current status

Strategies

Limited economic
interpretability

Deep learning models achieve high

predictive accuracy but provide limited
transparency for economic reasoning,
policy translation, or causal inference.

Insufficient benchmarking

against classical
regression

Short temporal prediction

horizons31

Many studies lack direct, standardized
comparisons between deep learning
models and established regression
frameworks (GLM, two-part, or hurdle
models)30.

Most models predict one-year costs,

overlooking long-term expenditure
dynamics or persistence of high-cost
status.

Limited data diversity and

Current studies rely heavily on single-

generalizability

country or proprietary datasets, restricting
generalization across systems and
populations32.

Underuse of social and

behavioral determinants

Models predominantly use demographic and

clinical variables, neglecting social
determinants of health (SDOH) and
behavioral predictors33.

(cid:6)

(cid:6)

(cid:6)

(cid:6)

(cid:6)

Incorporate explainable AI (XAI) frameworks such as
SHAP or Integrated Gradients.
Report marginal effects and sensitivity analyses
comparable to traditional regression outputs.
(cid:6) Develop hybrid interpretable-deep models tailored
for cost drivers and budget impact interpretation.
Require side-by-side benchmarking using identical
datasets and performance metrics.
Emphasize calibration, fairness, and welfare
implications beyond accuracy.
Promote transparent reporting of incremental
predictive and economic gains.
Extend modeling horizons to multi-year predictions.
Incorporate longitudinal claims data and time-
dependent survival or sequence models.
Evaluate temporal generalization via rolling-window
validation.
Promote multi-country, multi-payer benchmarking
datasets.
Integrate open, de-identified EHR or administrative
data with harmonized coding.
Implement domain adaptation and federated
learning for privacy-preserving collaboration.
Link cost data with area deprivation, socioeconomic,
or behavioral risk indices.

(cid:6)
(cid:6)

(cid:6)

(cid:6)

(cid:6)

(cid:6)

(cid:6)

(cid:6) Quantify incremental explanatory power of SDOH

(cid:6)

variables on expenditure prediction.
Integrate SDOH embeddings in multimodal
architectures.

---

<!-- PAGE 16 -->

668

J. T. LEE ET AL.

Challenge 2: insufficient benchmarking against classical regression
The absence of standardized benchmarking between deep learning models and traditional regression frame-
works remains a major methodological gap36. Many studies neglect formal comparisons with generalized lin-
ear, hurdle, or two-part models, or apply inconsistent data partitions and performance metrics, precluding
rigorous assessment of incremental value. Future research should direct, head-to-head benchmarking using
identical datasets, covariates, and validation procedures36. Evaluation must extend beyond statistical accuracy
to encompass calibration, discrimination, and welfare-relevant metrics such as cost-capture or decision-curve
analysis37. Transparent reporting of incremental explanatory power relative to GLM baselines will clarify
when the additional complexity of deep learning models is justified38.

All eight studies included in this review met the pre-specified minimum comparison criteria by incor-
porating at least one traditional or tree-based comparator10,17–23. However, only Drewe-Boss et al. (2022)
and Vimont et al. (2022) partially satisfied more stringent benchmarking requirements, including consist-
ent sample splits direct comparison with GLM two-part models10,21. The remaining studies reported
results under heterogeneous subgroup definitions or outcome specifications, limiting their suitability as
complete benchmarking cases17–20,22,23.

Drawing on principles articulated in DECIDE-AI, we emphasize the importance of clearly defining
application scenarios, target populations, comparator models, and evaluation structures a priori36.
Although not specific to economic evaluation, these principles provide a useful framework for structur-
ing systematic and transparent benchmarking between neural networks and classical cost-prediction
models.

Challenge 3: short temporal prediction horizons
Most existing models focus on one-year prediction horizons, reflecting budget-cycle pragmatism but
neglecting the persistence and temporal dependencies of high-cost conditions31. Extending prediction
windows to multi-year horizons using longitudinal claims and EHR data would better capture dynamic
health-state transitions39. Sequence-based architectures (e.g. LSTM, GRU, transformer models), combined
with rolling-window validation, should be used to assess temporal stability39.

Across the included studies, training windows often exceeded the prediction horizon. For example,
Drewe-Boss et al. (2022) used data from 2010–2015 to predict costs in 2016–201710, while Lewis et al.
(2021) analyzed commercial claims data spanning 2006–2017.17 Kaushik et al. (2017, 2020a, 2020b) typic-
ally employed four to five years of training data with the final year reserved for testing18,22,23, whereas
Vimont et al. (2022) and Yu et al. (2021) relied primarily on cross-sectional designs19,21. However, details
regarding training and observation periods were often confined to tables and not fully discussed in the
main text. Future studies should provide explicit disclosure of calendar years and observation windows
to strengthen assessment of longitudinal performance and cross-context generalizability.

Challenge 4: limited data diversity and generalizability
Most studies rely on single-country, single-payer, or proprietary datasets, limiting external validity and
constraining cross-system generalization40. Differences in coding standards, benefit structures, and reim-
bursement schemes further impede model transferability. Addressing this challenge requires the estab-
lishment of multi-country, multi-payer benchmark datasets with harmonized variable definitions and cost
metrics41. Privacy-preserving and federated learning architectures can facilitate cross-institutional collab-
oration without compromising confidentiality41. Domain-adaptation techniques should be developed to
recalibrate models for heterogeneous populations and health systems. Publicly accessible, de-identified
datasets adhering to FAIR (Findable, Accessible, Interoperable, Reusable) data principles are essential for
reproducibility and methodological transparency42.

Challenge 5: underuse of social and behavioral determinants
Current deep learning cost-prediction models overwhelmingly depend on demographic and clinical variables,
with limited incorporation of social determinants of health (SDOH) or behavioral risk factors. Yet socioeco-
nomic conditions, education, and lifestyle behaviors exert substantial influence on utilization patterns and
cost trajectories43. Integrating SDOH requires linking administrative and clinical data with census, deprivation,

---

<!-- PAGE 17 -->

or behavioral datasets, and representing these inputs through multimodal embeddings that capture latent
social context44. Quantifying the incremental explanatory and policy value of SDOH variables will help iden-
tify structural cost drivers and guide equitable allocation of healthcare resources.

JOURNAL OF MEDICAL ECONOMICS

669

Study limitations

This systematic review included only eight studies, and substantial heterogeneity was observed in
research design, data sources, healthcare systems, outcome definitions, and performance metrics. As a
result, quantitative meta-analysis was not feasible, and findings were synthesized narratively by identify-
ing consistent directional patterns. Most studies relied on single-country, single-database designs and
lacked external validation across time periods or healthcare systems. Additionally, the predominance of
one-year prediction horizons
and generalizability.
Consequently, the Complexity–Performance Hypothesis should be viewed as a working hypothesis,
requiring further systematic validation rather than a definitively established causal mechanism.

long-term robustness

assessment of

limits

Conclusion

Although the studies reviewed offer preliminary support for the Complexity–Performance Hypothesis,
rigorous empirical validation is still
in its early stages. Future research should conduct head-to-head
benchmarking of modeling approaches on the same datasets, systematically varying dimensionality and
temporal depth to determine the threshold at which adopting deep neural networks becomes justified
over classical
longitudinal,
regression or ensemble methods. Deep learning offers clear gains for
sequence-rich cost forecasting, whereas tree-based methods remain highly competitive for cross-sec-
these findings are consistent with the proposed Complexity–
tional
Performance Hypothesis, which posits that the predictive advantages of deep learning emerge primarily
when model capacity is well matched to data complexity.

tabular prediction. Overall,

Transparency

Declaration of funding

This research was supported by the National Health Research Institutes (NHRI)
Integrated Research Grant for
Biomedical and Health-Related Sciences Innovative Research Grant (IRG) (NHRI-EX114-11421PI) and the Mount Jade
Project Yushan Fellow Program of the Ministry of Education (MOE), Taiwan (MOE-112-YSFMN-0003-002-P1).

Declaration of financial/other interests

D.B.-C. W. is employed by Johnson & Johnson; this position is independent of and unrelated to the research pre-
sented in this manuscript. All other authors declare that they have no conflicts of interest relevant to the content of
this article. Peer reviewers on this manuscript have no relevant financial or other relationships to disclose.

Author contributions

J.T.L. conceived and designed the study, conducted the analysis, and led the manuscript writing. M.H.-S.Y. performed
the literature search and screening. All authors contributed to drafting and refining the of the manuscript. All
authors read and approved the final manuscript.

Acknowledgements

JTL is partly funded by the Ministry of Education, Taiwan, through the Mount Jade Fellowship and the Mount Jade
Project Yushan Fellow Program (MOE-112-YSFMN-0003-002-P1) as well as by the National Health Research Institutes
(NHRI) Integrated Research Grant for Biomedical and Health-Related Sciences Innovative Research Grant (IRG) (NHRI-
EX114-11421PI)

---

<!-- PAGE 18 -->

670

J. T. LEE ET AL.

Use of generative AI

The authors used ChatGPT (OpenAI, GPT-4o, 2025) to assist with language polishing and grammar/word checking
only.

Data availability statement

This systematic review is based solely on data extracted from published articles. No new datasets were created.
Extracted data tables and the PRISMA checklist can be provided upon reasonable request.

ORCID

John Tayu Lee
Melody Hsiao-San Yeh
Vincent Cheng-Sheng Li
Hsiao-Hui Chen
Yi-Hsuan Liu
David Bin-Chia Wu

http://orcid.org/0000-0002-1551-4923

http://orcid.org/0009-0009-4116-0637

http://orcid.org/0009-0006-8719-1699

http://orcid.org/0000-0001-7897-3118

http://orcid.org/0009-0007-5727-8328

http://orcid.org/0000-0002-0313-5758

References

[1]

[2]

[3]

[4]

[5]

[6]

[7]

Dieleman JL, Campbell M, Chapin A, et al. Future and potential spending on health 2015–40: development
assistance for health, and government, prepaid private, and out-of-pocket health spending in 184 countries.
The Lancet. 2017;389(10083):2005–2030. doi: 10.1016/S0140-6736(17)30873-5.
Rao KD, et al. Future health expenditures and its determinants in Latin America and the Caribbean: a multi-
country projection study. The Lancet Regional Health–Americas; 2025.
American Medical Association. Trends in health care spending. Chicago,
2023.
Holster T, Ji SX, Marttinen P. Risk adjustment for regional healthcare funding allocations with ensemble meth-
ods: an empirical study and interpretation. Eur J Health Econ. 2024;25(7):1117–1131. doi: 10.1007/s10198-023-
01656-w.
Henley SS, Golden RM, Kashner TM. Statistical modeling methods: challenges and strategies. Biostat
Epidemiol. 2020;4(1):105–139. doi: 10.1080/24709360.2019.1618653.
Rahnenf€uhrer J, De Bin R, Benner A, et al. Statistical analysis of high-dimensional biomedical data: a gentle
introduction to analytical goals, common approaches and challenges. BMC Med. 2023;21(1):182. doi: 10.1186/
s12916-023-02858-y.
Esteva A, Robicquet A, Ramsundar B, et al. A guide to deep learning in healthcare. Nat Med. 2019;25(1):24–
29. doi: 10.1038/s41591-018-0316-z.

IL: American Medical Association;

[8] Miotto R, Wang F, Wang S, et al. Deep learning for healthcare: review, opportunities and challenges. Briefings

[9]
[10]

[11]

[12]

[13]

[14]

[15]

[16]

[17]

Bioinformat. 2018;19(6):1236–1246. doi: 10.1093/bib/bbx044.
LeCun Y, Bengio Y, Hinton G. Deep learning. Nature. 2015;521(7553):436–444. doi: 10.1038/nature14539.
Drewe-Boss P, Enders D, Walker J, et al. Deep learning for prediction of population health costs. BMC Med
Inform Decis Mak. 2022;22(1):32. doi: 10.1186/s12911-021-01743-z.
Topol EJ. High-performance medicine: the convergence of human and artificial intelligence. Nat Med. 2019;
25(1):44–56. doi: 10.1038/s41591-018-0300-7.
Liu X, Faes L, Kale AU, et al. A comparison of deep learning performance against health-care professionals in
detecting diseases from medical imaging: a systematic review and meta-analysis. Lancet Digit Health. 2019;
1(6):e271–e297. doi: 10.1016/S2589-7500(19)30123-2.
He J, Baxter SL, Xu J, et al. The practical implementation of artificial intelligence technologies in medicine.
Nat Med. 2019;25(1):30–36. doi: 10.1038/s41591-018-0307-0.
Amiri MM, et al. Systematic review of factors determining health care expenditures. Health Policy Technol.
2021;10(2):100498.
Ke X, Saksena P, Holly A. The determinants of health expenditure: a country-level panel data analysis.
Geneva: World Health Organization; 2011. p. 1–28.
Page MJ, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ.
2021;372:n71.
Lewis M, Elad G, Beladev M, et al. Comparison of deep learning with traditional models to predict prevent-
able acute care use and spending among heart failure patients. Sci Rep. 2021;11(1):1164. doi: 10.1038/s41598-
020-80856-3.

---

<!-- PAGE 19 -->

JOURNAL OF MEDICAL ECONOMICS

671

[18]

[19]

[20]

[21]

[22]

[23]

[24]

[25]

[26]

[27]

[28]

Kaushik S, et al. Ensemble of multi-headed machine learning architectures for time-series forecasting of
healthcare expenditures. In: Applications of machine learning. Singapore: Springer; 2020. p. 199–216. doi: 10.
1007/978-981-15-3357-0_14.
Yu K, Yang Z, Wu C, et al. In-hospital resource utilization prediction from electronic medical records with
deep learning. Knowl Based Syst. 2021;223:107052. doi: 10.1016/j.knosys.2021.107052.
Yang C, Delcher C, Shenkman E, et al. Machine learning approaches for predicting high cost high need patient
expenditures in health care. Biomed Eng Online. 2018;17(Suppl 1):131. doi: 10.1186/s12938-018-0568-3.
Vimont A, Leleu H, Durand-Zaleski I. Machine learning versus regression modelling in predicting individual
healthcare costs from a representative sample of the nationwide claims database in France. Eur J Health
Econ. 2022;23(2):211–223. doi: 10.1007/s10198-021-01363-4.
Kaushik S, Choudhury A, Natarajan S, et al. Medicine expenditure prediction via a variance-based generative
adversarial network. IEEE Access. 2020;8:110947–110958. doi: 10.1109/access.2020.3002346.
Kaushik S, et al. Using LSTMs for predicting patient’s expenditure on medications.
Conference on Machine Learning and Data Science (MLDS). IEEE; 2017. doi: 10.1109/MLDS.2017.9.
Laqtib S, Yassini KE, Hasnaoui ML. A deep learning methods for intrusion detection systems based machine
learning in MANET. Proceedings of the 4th International Conference on Smart City Applications; 2019.
Teles AS, de Moura IR, Silva F, et al. EHR-based prediction modelling meets multimodal deep learning: a sys-
tematic review of structured and textual data fusion methods. Information Fusion. 2025;118:102981. doi: 10.
1016/j.inffus.2025.102981.
Smith J. Predictive analytics in healthcare: powering proactive patient care in the era of value-based care;
2025.
Hassija V, Chamola V, Mahapatra A, et al. Interpreting black-box models: a review on explainable artificial
intelligence. Cogn Comput. 2024;16(1):45–74. doi: 10.1007/s12559-023-10179-8.
Sendak MP, et al. A path for translation of machine learning products into healthcare delivery. EMJ Innov.
2020;10:19–00172.

In: 2017 International

[29] Obermeyer Z, Emanuel EJ. Predicting the future—big data, machine learning, and clinical medicine. N Engl J

[30]

[31]

[32]

[33]

[34]

[35]

[36]

[37]

[38]

[39]

[40]

[41]

Med. 2016;375(13):1216–1219. doi: 10.1056/NEJMp1606181.
Bodha S. A comparative study of machine learning and deep learning models for predicting medical insur-
ance costs with explainable AI; 2025.
Sohn JH, Chen Y, Lituiev D, et al. Prediction of future healthcare expenses of patients from chest radiographs
using deep learning: a pilot study. Sci Rep. 2022;12(1):8344. doi: 10.1038/s41598-022-12551-4.
Futoma J, Simons M, Panch T, et al. The myth of generalisability in clinical research and machine learning in
health care. Lancet Digit Health. 2020;2(9):e489–e492. doi: 10.1016/S2589-7500(20)30186-2.
Tan M, Hatef E, Taghipour D, et al. Including social and behavioral determinants in predictive models: trends,
challenges, and opportunities. JMIR Med Inform. 2020;8(9):e18084. doi: 10.2196/18084.
Yoon CH, Torrance R, Scheinerman N. Machine learning in medicine: should the pursuit of enhanced inter-
pretability be abandoned? J Med Ethics. 2022;48(9):581–585. doi: 10.1136/medethics-2020-107102.
De Bock KW, Coussement K, Caigny AD, et al. Explainable AI for operational research: a defining framework,
methods, applications, and a research agenda. Eur J Oper Res. 2024;317(2):249–272. doi: 10.1016/j.ejor.2023.
09.026.
Vasey B, Nagendran M, Campbell B, et al. Reporting guideline for the early stage clinical evaluation of deci-
sion support systems driven by artificial
intelligence: DECIDE-AI. BMJ. 2022;377:e070904. doi: 10.1136/bmj-
2022-070904.
Collins GS, Reitsma JB, Altman DG, et al. Transparent reporting of a multivariable prediction model for indi-
vidual prognosis or diagnosis (TRIPOD): the TRIPOD statement. Br J Surg. 2015;102(3):148–158. doi: 10.1002/
bjs.9736.
Steyerberg EW, Vickers AJ, Cook NR, et al. Assessing the performance of prediction models: a framework for
traditional and novel measures. Epidemiology. 2010;21(1):128–138. doi: 10.1097/EDE.0b013e3181c30fb2.
Choi E, et al. Doctor AI: predicting clinical events via recurrent neural networks.
Healthcare Conference. PMLR; 2016.
Rasmy L, Wu Y, Wang N, et al. A study of generalizability of recurrent neural network-based predictive models
for heart failure onset risk using a large and heterogeneous EHR data set. J Biomed Inform. 2018;84:11–16.
doi: 10.1016/j.jbi.2018.06.011.
Kaissis GA, Makowski MR, R€uckert D, et al. Secure, privacy-preserving and federated machine learning in med-
ical imaging. Nat Mach Intell. 2020;2(6):305–311. doi: 10.1038/s42256-020-0186-1.

In: Machine Learning for

[42] Wilkinson MD, Dumontier M, Aalbersberg IJ, et al. The FAIR guiding principles for scientific data management

[43]

[44]

and stewardship. Sci Data. 2016;3(1):1–9. doi: 10.1038/sdata.2016.18.
Lee NS, Whitman N, Vakharia N, et al. High-cost patients: hot-spotters don’t explain the half of it. J Gen
Intern Med. 2017;32(1):28–34. doi: 10.1007/s11606-016-3790-3.
Rajkomar A, Hardt M, Howell MD, et al. Ensuring fairness in machine learning to advance health equity. Ann
Intern Med. 2018;169(12):866–872. doi: 10.7326/M18-1990.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Medical Economics
ISSN: 1369-6998 (Print) 1941-837X (Online) Journal homepage: www.tandfonline.com/journals/tfocoll
Comparing deep learning and classical regression
approaches for predicting healthcare expenditure
and spending: a systematic review
John Tayu Lee, Melody Hsiao-San Yeh, Vincent Cheng-Sheng Li, Hsiao-Hui
Chen, Yi-Hsuan Liu, Yu-Chun Chen & David Bin-Chia Wu
To cite this article: John Tayu Lee, Melody Hsiao-San Yeh, Vincent Cheng-Sheng Li, Hsiao-
Hui Chen, Yi-Hsuan Liu, Yu-Chun Chen & David Bin-Chia Wu (2023) Comparing deep
learning and classical regression approaches for predicting healthcare expenditure
and spending: a systematic review, Journal of Medical Economics, 29:1, 654-671, DOI:
10.1080/13696998.2026.2630598
To link to this article: https://doi.org/10.1080/13696998.2026.2630598
© 2026 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group
View supplementary material
Published online: 04 Mar 2026.
Submit your article to this journal
Article views: 640
View related articles
View Crossmark data
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tfocoll

JOURNALOFMEDICALECONOMICS
2026,VOL.29,NO.1,654–671
https://doi.org/10.1080/13696998.2026.2630598
Article/2630598
ORIGINAL RESEARCH
Comparing deep learning and classical regression approaches for
predicting healthcare expenditure and spending: a systematic review
John Tayu Leea , Melody Hsiao-San Yeha , Vincent Cheng-Sheng Lia , Hsiao-Hui Chena ,
Yi-Hsuan Liub , Yu-Chun Chena and David Bin-Chia Wuc
aInstitute ofHealth PolicyandManagement,Collegeof PublicHealth, NationalTaiwan University, Taipei, Taiwan;bMaster
Program ofStatistics, NationalTaiwan University, Taipei, Taiwan;cSaw Swee HockSchool ofPublic Health, National
University ofSingapore, UniversityHall, Singapore
ABSTRACT ARTICLEHISTORY
Aims: This study compares deep learning architectureswith traditionalregression and Received11December2025
tree-based modelsforindividual-level healthcare cost prediction, with particularatten- Revised7February2026
tiontoperformancedifferencesacrossdatacontexts. Accepted9February2026
Methods: We conducted a preregistered systematic review (PROSPERO
KEYWORDS
CRD420251129440). Web of Science, PubMed, Embase, and Scopus were searched
Healthcareexpenditure;
through August 2025. Eligible studies used real-world individual-level data (claims,
healthspending;deep
electronic health records, or registries) to predict cost-related outcomes with at least learning;neuralnetwork;
one deep learning architecture and one classical regression comparator, and reported predictivemodeling;health
quantitative performance. Data were extracted on population, predictors, outcome economics
horizon, model type, validation strategy, performance metrics, calibration, and
JELCODES
interpretability.
Results: Eight studies met inclusion criteria, spanning the United States, Europe, and I13;I15;I28;H51
Asia. In longitudinal designs—such as multi-year claims prediction and medication or
hospitalization time-series forecasting—sequential deep learning models, particularly
LSTM and CNN–LSTM hybrids, consistently outperformed regression and tree-based
algorithms. Reported gains included approximately 10–20% reductions in RMSE/MAE,
R2 improvements of 0.01–0.15, and AUROC values up to 0.78 for high-risk classifica-
tion. Across studies, prior costs and utilization were consistently the strongest predic-
tors, while social determinants and free-text features were rarely incorporated. In
contrast, for low-dimensional, structured, cross-sectional medical data, generalized lin-
ear models and tree-based approaches remain robust baseline models due to their
interpretabilityandcalibrationstability.
Limitations: Evidence is based on a small and heterogeneous set of eight studies,
with limited external or temporal validation, short prediction horizons, and sparse
assessment of calibration, economic interpretability, and fairness, warranting cautious
interpretation.
Conclusions:Deeplearningofferscleargainsforlongitudinal,sequence-richcostfore-
casting, whereas tree-based methods remain highly competitive for cross-sectional
tabular prediction. Overall, these findings are consistent with the proposed
Complexity–Performance Hypothesis, which posits that the predictive advantages of
deep learning emerge primarily when model capacity is well matched to data
complexity.
Introduction
Healthcare expenditures continue to rise globally, imposing escalating burdens on payers, governments,
and patients alike1–3. Accurate forecasts of individual and population-level health costs are crucial—not
CONTACT John Tayu Lee johntayulee@ntu.edu.tw Institute of Health Policy and Management, College of Public Health, National
TaiwanUniversity,No.17,Xu-ZhouRoad,ZhongzhengDistrict,Taipei,100,Taiwan
Supplementaldataforthisarticleisavailableonlineathttps://doi.org/10.1080/13696998.2026.2630598.
(cid:1)2026TheAuthor(s).PublishedbyInformaUKLimited,tradingasTaylor&FrancisGroup
ThisisanOpenAccessarticledistributedunderthetermsoftheCreativeCommonsAttribution-NonCommercial-NoDerivativesLicense(http://creativecommons.
org/licenses/by-nc-nd/4.0/),whichpermitsnon-commercial re-use,distribution,andreproduction inany medium,providedthe originalworkis properlycited,
andisnotaltered,transformed,orbuiltuponinanyway.ThetermsonwhichthisarticlehasbeenpublishedallowthepostingoftheAcceptedManuscriptina
repositorybytheauthor(s)orwiththeirconsent.
www.tandfonline.com/ijme

JOURNALOFMEDICALECONOMICS 655
only for academic modeling but also for practical applications in insurance underwriting, risk adjustment,
budget planning, and value-based payment strategies4. Traditional statistical approaches (e.g. linear
models, generalized linear models, two-part models) frequently struggle to capture complex, nonlinear
interactions in health data and may underperform when faced with high-dimensional
inputs5–7.
In recent years, deep learning and neural network architectures have garnered considerable attention
for their promise in modeling high-dimensional, heterogeneous data8,9. For example, Drewe-Boss et al.
(2022) applied a deep neural network to claims data of German insurees and demonstrated superior per-
formance over ridge regression in predicting next-year total healthcare costs10. Such applications under-
score the potential of neural networks to learn latent feature interactions, temporal patterns, and
nonlinearities that conventional models often miss7,8.
However, despite such advances, important methodological questions remain. It is still unclear how
extant studies differ in their policy or operational context, population and data sources, neural network
architectures and training strategies, sensitivity analyses, software platforms, and modes of result presen-
tation and
interpretation11–13.
Moreover, many papers provide limited comparisons between neural net-
work models and benchmark regression or machine learning alternatives, making it hard to judge when
neural networks truly add value11.
Healthcare expenditures are influenced by multiple interrelated factors. Demographic composition,
particularly population aging, contributes to a growing demand for healthcare services14,15.
Epidemiological, lifestyle and environmental and socioeconomic factors also influence individual and
population health status, are also associated with healthcare spending14. Individual healthcare spending
is also shaped by utilization patterns, access to providers, and broader forces such as economic growth
and technological progress14,15. These determinants interact in nonlinear ways, producing highly skewed
and dynamic spending distributions. Capturing such complexity requires analytical frameworks capable
of modeling heterogeneity and temporal persistence in costs—motivating the application of neural net-
work approaches to health expenditure prediction.
This systematic review aims to map the evolving landscape of neural network-based healthcare cost
and expenditure prediction. Specifically, we systematically searched the literature to address the follow-
ing key questions: (1) What research objectives have been addressed (e.g. total cost, cost change, high-
cost classification)? (2) Which neural network methods—feedforward networks, convolutional nets, recur-
rent architectures (LSTM/GRU), hybrid models, or others—are used in health expenditure prediction?
(3) What evaluation frameworks and result presentation strategies (e.g. error metrics, calibration, classifi-
cation thresholds) are commonly employed? (4) How do neural network model performances compare
with classical regression or machine learning baselines across domains and settings?
Methods
This systematic review was conducted according to a pre-specified protocol and registered with the
International Prospective Register of Systematic Reviews (PROSPERO; registration number CRD420251129440).
A comprehensive search strategy was designed to identify relevant literature across multiple biblio-
graphic databases, including Web of Science, PubMed, EMBASE, and Scopus. The search covered all pub-
lications up to August 2025. Reference lists of included studies were additionally screened to capture
potentially eligible articles not retrieved through the database search.
Studies were considered eligible if they: (1) Applied deep learning or neural network algorithms (e.g.
feed-forward neural network, convolutional neural network, recurrent neural network, long short-term
memory [LSTM], DNN) for the prediction, estimation, or modeling of healthcare expenditure, cost, or
resource use; (2) Used real-world, individual-level health data such as insurance claims, electronic health
records (EHRs), administrative datasets, or registry data; (3) Reported model performance metrics (e.g.
RMSE, MAE, R2, AUC) or compared neural network models against classical or machine-learning base-
lines; and (4) Were published in English.
To ensure methodological comparability, only studies that directly implemented both a deep learning
(or neural network) model and at least one classical regression model (e.g. linear regression, GLM, ridge,
lasso) and quantitatively compared their predictive performance were included. Additionally, studies
were required to include an outcome variable explicitly representing healthcare expenditure, spending,

656 J.T.LEEETAL.
cost, or a closely related economic measure (e.g. medical cost, insurance charge, resource utilization
expressed in monetary units).
Studies were excluded if they: (i) focused exclusively on intervention cost-effectiveness or simulation
modeling without predictive application; used hypothetical, synthetic, or simulated data sources (e.g.
Kaggle or other artificially generated datasets) rather than real-world data; or (iii) applied machine-learn-
ing algorithms other than neural networks without neural network comparison. (iv) did not conduct a
direct comparative analysis between a classical regression model and a deep learning approach on cost-
or expenditure-related outcomes.
Three conceptual domains guided the search formulation: (1) Deep learning and neural network ter-
(cid:1)
minology (e.g. “deep learning,” “neural network ,” “CNN,” “RNN,” “LSTM,” “DNN,” “artificial intelligence,”
(cid:1) (cid:1) (cid:1)
“machine learning”); (2) Predictive modeling expressions (e.g. “predict ,” “forecast ,” “model ,”
(cid:1) (cid:1) (cid:1)
“estimate ,” “projection ”); and (3) Healthcare expenditure concepts (e.g. “healthcare cost ,” “medical
(cid:1) (cid:1) (cid:1)
cost ,” “health expenditure ,” “health spending,” “treatment cost ,” “resource use,” “resource utilization”).
Alternative databases such as ACM Digital Library were evaluated but subsequently excluded due to
limited coverage of health-economic literature.
During the initial screening stage, titles and abstracts were independently assessed by one trained
reviewer according to pre-specified eligibility criteria16. All records that were potentially eligible or for
which eligibility was unclear were retained for full-text review to avoid premature exclusion. Final inclu-
sion and exclusion decisions were jointly discussed by at least two team members; in cases of disagree-
ment, a third team member was consulted to resolve discrepancies and minimize the risk of systematic
selection bias.
Among excluded studies, the most common reason for exclusion was that the prediction target was
not healthcare cost or expenditure but alternative outcomes, such as disease incidence or hospitalisation
risk. Additional studies were excluded because they did not include a direct comparison between tradi-
tional regression or tree-based models and deep learning approaches. Studies relying on simulated or
synthetic data, or other non–real-world data sources, were also excluded. Based on these criteria, a total
of eight studies were ultimately included, all of which used real-world data, explicitly focused on health-
care cost prediction, and directly compared deep learning models with traditional regression or tree-
based approaches.
Data extraction was performed using a structured Excel framework. Extracted variables included bib-
liographic details, data source and setting, population characteristics, neural network architecture, input
variables, model evaluation metrics, comparator models, cost or outcome definitions, and key findings.
Findings were synthesized narratively and summarized in tabular form, categorizing studies by model
type, prediction task, dataset scale, and performance benchmark. Quantitative aggregation was limited
to descriptive reporting due to methodological heterogeneity among studies. The systematic review fol-
lowed the PRISMA 2020 reporting guidelines, and the completed checklist is provided in Supplementary
Table S1.
Results
The database search identified a total of 23,572 records: PubMed (n¼1,525), Embase (n¼9,532), Scopus
(n¼43), and Web of Science (n¼12,472). After removing 2,164 duplicate records, 21,408 unique records
were screened by title and abstract. Additionally, 11 records were identified through citation searching,
all of which were retrieved and assessed for eligibility, with 10 records excluded. Of these, 21,352 were
excluded as not relevant to the review objectives. 8 studies met the final inclusion criteria and were
included in this systematic review. The full study identification, screening, and inclusion process is illus-
trated in Figure 1 (PRISMA flow diagram).
Characteristics of identified studies
Table 1 showed the characteristics of the identified studies. A total of eight studies met the inclusion cri-
teria, conducted across the United States, predominantly private insurance system (n¼5)17,18,20,22,23;
Europe, including Germany, which has single-payer systems (n¼1)10, and France, which has universal

JOURNALOFMEDICALECONOMICS 657
Figure 1. PRISMA flow diagram of study identification.
health insurance with multiple payers (n¼1)21; and Asia (China ¼ 1)19. Sample sizes ranged from
approximately 50,000 to over 1.4 million individuals, encompassing data sources such as commercial
insurance claims (n¼3)17,18,23, national health insurance databases (n¼3)10,20,21, and electronic medical
records (EMR) (n¼1)19, while one study used retail-level pharmacy transaction records (n¼1)22.
Six studies adopted longitudinal designs (multi-year or time-series forecasting)10,17,18,20,22,23, while two
were cross-sectional cost-regression studies19,21. Table 2 also shows the outcome variables primarily
included: (1) Total annual or per-member-per-month expenditure (n¼5)10,17,18,20,21, (2) Medication-spe-
cific or pharmacy expenditures (n¼3)18,22,23, (3) Preventable cost17, and (4) In-hospital costs (n¼1)19.
In the heart failure population study by Lewis et al. (2021), preventable costs were defined on the
basis of the follow-up period and operationalized using insurance claims data, in which hospitalizations
and emergency department visits classified as potentially avoidable—according to clinical quality indica-
tors and emergency care categorization algorithms—were aggregated into total reimbursed costs17.
Among the eight included studies, only this study explicitly focused on preventable costs as the primary
economic outcome, whereas the remaining studies primarily examined total medical expenditures or in-
hospital costs as the main economic indicators17.
Deep learning architectures varied across studies: feed-forward networks (DNN/MLP; n¼2)10,21,
sequence-based models (LSTM, stacked LSTM, CNN-LSTM, RNN; n¼4)17,18,20,23, hybrid or multi-view net-
works (n¼1)19, and variance-based generative adversarial network (V-GAN; n¼1)22. Comparators
included classical regression approaches—such as GLM, ridge, and LASSO regression
(n¼6)10,17,18,20,21,23—and tree-based machine-learning methods including Random Forest (RF), Gradient
Boosting Machine (GBM), or CatBoost
(n¼4)17,20–22.
Model performance was most commonly
evaluated using R2 or adjusted R2 (n¼5)10,18,20,21,23, MAE (n¼3)18,19,21, RMSE (n ¼ 5)18–20,22,23, and AUC
(n ¼ 2)10,17; several studies additionally reported precision@k, cost-capture, or correlation coefficients
for discrimination and calibration assessment (n¼3)10,17,19.
Clinical and policy contexts of prediction
Based on the comparative models in Table 2, this section shows the methodological frameworks and
model performance of each included study. One U.S. study focused on population health management,
predicting preventable hospitalizations, emergency visits, and expenditures among heart failure patients

658 J.T.LEEETAL.
)deunitnoc(
)yats-nihtiw(lanoitces-ssorC
|     |     |     | )raey-itlum(lanidutignoL |     | )5102–1102(lanidutignoL |     |     |     |     | )raey-itlum(lanidutignoL |     |     |
| --- | --- | --- | ------------------------ | --- | ----------------------- | --- | --- | --- | --- | ------------------------ | --- | --- |
ngisedlaropmeT
)sraey21(lanidutignoL
stneitap;atadsmialclaicremmoc -tneitapfosraeyevifgnisuyduts -niart01/02/07;atadsmialclevel krowemarf)noitciderPnoitazilitU smialcevitartsinimdagnisuyduts doirep-txentciderpotdesuerew
|     | gniledomcitsongorpevitcepsorteR | ,noitadilav,gniniartotnidedivid |     | ;doirepnoitavresbo5102–0102( |     |     |     |     | sweivatadelpitlumgnitargetni |     |     |     |
| --- | ------------------------------- | ------------------------------- | --- | ---------------------------- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
fo)7102–6002(sraey21gnisu .)doirepnoitaulave7102–6102 ydutslanoitavresboevitcepsorteR ydutsehT.gninraeldesivrepus ecruoseR(PURehtdecudortni )txetnoitarepo,txetsisongaid trohoclanidutignolevitcepsorteR lacirotsihs’tneitaphcaE.atad
|     |     |                        | desab-noitalupopevitcepsorteR |                           |                              | gnitsacerof-tsoclanidutignol |     |                        |                          |     |                         | snoitacidemdna,serudecorp |
| --- | --- | ---------------------- | ----------------------------- | ------------------------- | ---------------------------- | ---------------------------- | --- | ---------------------- | ------------------------ | --- | ----------------------- | ------------------------- |
|     |     |                        |                               | sdrocersmialclanidutignol |                              |                              |     | rofatadRMEderutcurtsnu |                          |     |                         |                           |
|     |     |                        |                               | dnatnempoleved-ledom      | ,lanoitavresbo,evitcepsorteR |                              |     |                        |                          |     |                         | .serutidnepxe)htnom-21(   |
|     |     | .)1:2:7(stesgnitsetdna |                               | gnisuydutsnosirapmoc      |                              |                              |     |                        | ,serutaefderutcurts.g.e( |     | ,sesongaid,serutidnepxe |                           |
ngisedydutS
|     |     |     |     |     |     |     | dnaderutcurtsgnisu |     |     | .ledomdeifinuaotni |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ------------------ | --- | --- |
.tilpstset-noitadilav
-nondnalaitneuqes(sehcaorppa stneitap)FH(eruliaftraehgnoma stsocerac-htlaeherutufraey-eno ecnamrofrepstierapmocotdna latothtobrofsledomkramhcneb serutidnepxenoitacidemtneitap gnitamitseyllacificeps,noitazilitu gninraelenihcamfoecnamrofrep laropmetyfitnauqotdemiayduts
gnitciderprofnoissergercitsigol gnidnepserachtlaehdna,stisiv rehtodnanoissergeregdirhtiw egnahc-tsocdnanoitciderptsoc gnitsacerofrof)skrowtenlaruen ,serutidnepxeerachtlaeherutuf dnagniyfitnedinosucofahtiw deen-hgihtsoc-hgihgniganam .sehcaorppanoissergerlacissalc
peedaetaulavednapolevedoT gnitciderprofkrowtenlaruen ,atadsmialclanidutignolmorf ylhtnomdnaylkeewtsacerofoT gninrael-peeddecnavdagnisu gnitsaceroflanoitidarttsniaga fohtgneldnastsoclatipsoh-ni ehT.stneitapdiacideM)NHCH( tsniagasledomgninraelpeed
.noitciderp ,snoitazilatipsohelbatneverp )DE(tnemtrapedycnegreme otdna,sdohtemseires-emit –NNCdedaeh-itlumerapmoc serutcetihcraelbmesneMTSL ecruoserlatipsoh-nitciderpoT kramhcnebotdnagnidneps
|     |                       | lanoitidarthtiw)laitneuqes |     |     |     |     |     | cinortcelegnisu)SOL(yats peedaaivsdrocerlacidem |     |                         | tnerrucergnidulcni(sledom |                         |
| --- | --------------------- | -------------------------- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | ----------------------- | ------------------------- | ----------------------- |
|     | sevitcejbodnamiA      |                            |     |     |     |     |     |                                                 |     |                         |                           | erachtlaehniecnetsisrep |
|     | gninraelpeederapmocoT |                            |     |     |     |     |     |                                                 |     | evitciderpehtetaulaveoT |                           |                         |
.hcaorppagninrael
erutidnepxe
.noitacifitnedi
.sledom
erachtlaeh
eziselpmasdnanoitalupopydutS .S.Uegralani)7102–6102(sraey etatsdna,xes,egaybnoitalupop ,saxeTnistneitapdellorne-diacideM elpmaS.atadsmialclanidutignol fosnoillimdeniatnoctesatadeht
esabatadecnarusnilaicremmoc morfslaudividniderusni643,304,1 sdrocertneitapdegrahcsid000,057 esabatad)RME(sdrocerlacidem -hgihtsoc-hgihdnanoitalupop fosraeylarevesgnisudezylana tub,detroperylticilpxetonezis
|              | owtrofdellorneylsuounitnoc   |     |     | namreGehtfoevitatneserper                    |                        |                                                  | nward,slatipsohesenihCmorf |                            |                           |     |                      |                         |
| ------------ | ---------------------------- | --- | --- | -------------------------------------------- | ---------------------- | ------------------------------------------------ | -------------------------- | -------------------------- | ------------------------- | --- | -------------------- | ----------------------- |
| rof          | eruliaftraehhtiwstluda062,39 |     |     |                                              |                        | 5102lirpAdna1102yraunaJ nacStekraMnevurTehtmorf  |                            | cinortceleelacs-egralamorf | tneitapdna,sedocnoitarepo |     |                      |                         |
|              |                              |     |     |                                              |                        | neewtebsmialcnoitacidem ).S.U(esabatadsretnuocnE |                            |                            |                           |     |                      | fosraeyelpitlumgnirevoc |
|              |                              |     |     | 06>(esabatadfeGnIeht                         |                        |                                                  |                            | ,stxetsisongaidgnidulcni   |                           |     | ,spuorgbus)NHCH(deen | sdrocerrebmemylhtnom    |
| snoitacilppa |                              |     |     | htlaehyrotutatsnamreG ,)7102–0102,secnarusni | htiwstneitap000,05revO | niapdesab-noitpircserp dnasmialClaicremmoC       |                            |                            |                           |     |                      |                         |
lareneghtobgnidulcni
.yrotsiherutidnepxe
.scihpargomed
.ecnediserfo
gninrael
peed
|     | setatSdetinU |     |     |     | setatSdetinU |     |     |     |     | setatSdetinU |     |     |
| --- | ------------ | --- | --- | --- | ------------ | --- | --- | --- | --- | ------------ | --- | --- |
no yrtnuoC
ynamreG
seiduts
anihC
dedulcni
|     | stropeRcifitneicS |     |            |             |                |                      | desaB-egdelwonK |     |     |           |        |     |
| --- | ----------------- | --- | ---------- | ----------- | -------------- | -------------------- | --------------- | --- | --- | --------- | ------ | --- |
|     |                   |     |            | noisiceDdna | fosnoitacilppA |                      |                 |     |     |           |        |     |
|     |                   |     |            | scitamrofnI |                | –gninraeL :41retpahC |                 |     |     |           |        |     |
|     | lanruoJ           |     | lacideMCMB |             |                |                      |                 |     |     | gnEdeMoiB |        |     |
|     |                   |     |            |             |                | enihcaM              | smetsyS         |     |     |           |        |     |
| fo  |                   |     |            | gnikaM      |                |                      |                 |     |     |           | eniLnO |     |
scitsiretcarahC
|     |     |     | .latessoB-ewerD |     |     |     | 91)1202(.lateuY |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
.latekihsuaK
|     | .latesiweL 71)1202( |     |     | 01)2202( |     | 81)0202( |     |     |     | .lategnaY | 02)8102( |     |
| --- | ------------------- | --- | --- | -------- | --- | -------- | --- | --- | --- | --------- | -------- | --- |
.1 elbaT ydutS

JOURNALOFMEDICALECONOMICS 659
|                | raeyelgnis(lanoitces-ssorC                                   |     |                          | gnisuledomgnitsacerof emitelpitlumrevoatad | shtnom84tsrif—ngised          | shtnom21lanif,gniniart .gnitsetrofdesu)5102( |
| -------------- | ------------------------------------------------------------ | --- | ------------------------ | ------------------------------------------ | ----------------------------- | -------------------------------------------- |
|                |                                                              |     | seires-emit,lanidutignoL | erutidnepxelaitneuqes                      |                               | rofdesu)4102–1102(                           |
| ngisedlaropmeT |                                                              |     |                          |                                            | seires-emitlanidutignoL       |                                              |
|                | )6102                                                        |     |                          | .stniop                                    |                               |                                              |
|                | evitartsinimdadetcellocylenituor etarapeS.SDNSmorfatadsmialc |     |                          |                                            | smialcecnarusniyradnocesgnisu |                                              |
-hgihrofdnanoitalupoperitne
|     | gnisuydutsdesab-noitalupop |     |     | -emiterutidnepxenoitpircserp | ydutslanoitavresboevitcepsorteR |     |
| --- | -------------------------- | --- | --- | ---------------------------- | ------------------------------- | --- |
ehtrofdeniarterewsledom
,lanoitces-ssorc,evitcepsorteR
lanoitatupmocevitcepsorteR
| ngisedydutS |     |     |     | gnisuydutsgniledom |     |     |
| ----------- | --- | --- | --- | ------------------ | --- | --- |
.spuorgbustsoc
.atadseires
.atad
ediwnoitangnisustsocerachtlaeh
|     | gninraelenihcamfoecnamrofrep lacissalcahtiwsledom)krowteN | otthguosydutsehT.atadsmialc sniaglufgninaemsreffogninrael |     |     |     |                            |
| --- | --------------------------------------------------------- | --------------------------------------------------------- | --- | --- | --- | -------------------------- |
|     | )MLG(ledoMraeniLdezilareneG                               |                                                           |     |     |     | atsniagaecnamrofreperapmoc |
-noitpircserpanoerutidnepxe
|                  |                                                | enihcamrehtehwenimreted | ninoissergerlanoitidartrevo -ecnairavatsetdnapolevedoT | lairasrevdaevitarenegdesab tahtledom)NAG-V(krowten dnaledomneewtebecnairav | tneitap-repylhtnomtsacerofoT | gnisunoitacidemniapdesab otdna)MTSL(gninraelpeed |
| ---------------- | ---------------------------------------------- | ----------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------ |
|                  | larueNdnatseroFmodnaR(                         |                         |                                                        | niecnereffidehtseziminim                                                   |                              | ledomlacitsitatslanoitidart                      |
| sevitcejbodnamiA |                                                |                         |                                                        | gnitciderprofatadlautca                                                    |                              |                                                  |
|                  | evitciderpehterapmocoT laudividnignitsacerofni |                         |                                                        |                                                                            |                              |                                                  |
|                  |                                                |                         | .gniledomtsochtlaeh                                    |                                                                            | serutidnepxeenicidem         |                                                  |
.)AMIRA(
| eziselpmasdnanoitalupopydutS | gnisu,)SDNS(metsySnoitamrofnI                             |     |                                 | eziselpmastcaxeeht;noitacidem                             | -noitpircserpagnisahcrupsetatS | detcartxe,noitacidemniapdesab |
| ---------------------------- | --------------------------------------------------------- | --- | ------------------------------- | --------------------------------------------------------- | ------------------------------ | ----------------------------- |
|                              | ehtybderevocnoitalupoplareneG esabatadlanoitanehtfoelpmas |     | niapcificepsagnisahcrupstneitaP |                                                           |                                | –1102(tesatadsmialcecnarusni  |
|                              | modnarevitatneserper79/1a                                 |     |                                 | morfdeviredtubdeificepston sdrocernoitcasnartlevel-liater |                                |                               |
|                              | ataDhtlaeHlanoitaNhcnerF                                  |     |                                 |                                                           | detinUehtnistneitap000,05>     | nacStekraMnevurTehtmorf       |
|                              | .6102raeyehtrof                                           |     |                                 | .)atadseires-emit(                                        |                                |                               |
)5102
|     |     |     | setatSdetinU |     | setatSdetinU |     |
| --- | --- | --- | ------------ | --- | ------------ | --- |
yrtnuoC
ecnarF
|     | lanruoJnaeporuE |     |     |     |     | noecnerefnoC                          |
| --- | --------------- | --- | --- | --- | --- | ------------------------------------- |
|     |                 |     |     |     |     | lanoitanretnI dnagninraeL ecneicSataD |
fosgnideecorP
lanruoJ htlaeHfo scimonocE
|     |     |     | sseccAEEEI |     | EEEIeht | enihcaM |
| --- | --- | --- | ---------- | --- | ------- | ------- |
)SDLM(
.deunitnoC
|     |     |     | .latekihsuaK |     | .latekihsuaK |     |
| --- | --- | --- | ------------ | --- | ------------ | --- |
.latetnomiV
|     | 12)2202( |     |     | 22)0202( | 32)7102( |     |
| --- | -------- | --- | --- | -------- | -------- | --- |
.1 elbaT ydutS

660 J.T.LEEETAL.
|     |     |                           |     |                             |                           | gnisuetipseddetimilniamer edistuonoitadilavlanretxeoN– |                              |                                                  |                       |                                |                                                | )deunitnoc(                                     |
| --- | --- | ------------------------- | --- | --------------------------- | ------------------------- | ------------------------------------------------------ | ---------------------------- | ------------------------------------------------ | --------------------- | ------------------------------ | ---------------------------------------------- | ----------------------------------------------- |
|     |     | desabsemoctuoelbatneverP– |     | oteudycneiciffenilaitnetoP– |                           |                                                        | laicosfonoisulcniticilpxeoN– |                                                  | dnasdaehelpitlumoteud | ;detimilytilibaterpretniledoM– | -htlaehlarenegon(tesatad                       |                                                 |
|     |     |                           |     |                             | dnaytilibaterpretniledoM– | ybdetceffaebyamledoM–                                  |                              | nodedeenhcraeserrehtruF– dnaserutcetihcralamitpo |                       |                                | nevurTmorfserutidnepxe .stnanimretedlaroivaheb | )PAHS.g.e(IAelbanialpxe niseirogetacerutidnepxe |
segnellahcdeifitnedI lanretnimodnardnoyeb dnaycnerapsnartdetimiL– rehtootnoitazilareneg evisnetniyllanoitatupmoC– rolaicosfonoisulcnioN– redaorbnognitsetdna
|     | ,cimonoceoicosfokcaL– | smhtiroglagnitsixeno |     | .wodniwatadraey-11 | peedfoytilibanialpxe noitamitseytniatrecnu | .stneidargdetargetni | gnidocrosnoitaluger | .srotcaflatnemnorivne |     |     | otdetcirtsernoitadilaV– |     |
| --- | --------------------- | -------------------- | --- | ------------------ | ------------------------------------------ | -------------------- | ------------------- | --------------------- | --- | --- | ----------------------- | --- |
RHEdna,yrotarobal dnaytilibaterpretni noitadilavlanretxeoN– .erutcurtselbmesne gnitargetnidetsegguS–
|     |     |                  | yam)IQP,sgnilliB( .stneveyfissalcsim |     |                 | .tesatadfeGnIeht | gnillibnisegnahc |                |             | erutaefraelcskcal | detaler-noitacidem |             |
| --- | --- | ---------------- | ------------------------------------ | --- | --------------- | ---------------- | ---------------- | -------------- | ----------- | ----------------- | ------------------ | ----------- |
|     |     | detimilselbairav |                                      |     | .sledomgninrael |                  |                  | rostnanimreted |             |                   |                    |             |
|     |     | .ssenetelpmoc    |                                      |     |                 |                  |                  |                |             |                   | .)stsocmetsys      |             |
|     |     |                  |                                      |     |                 |                  |                  |                | .sepytonehp |                   |                    | .krowerutuf |
|     |     |                  |                                      |     |                 |                  | .secitcarp       |                |             | .noitubirtta      |                    |             |
.tilps
|     | )NNCdnaMTSLylralucitrap( |                                                                                           |                                                                           | nisnoitnevretnidetegratrof                        | yllaitnatsbuskrowtenpeedehT | egnahc-tsocdnanoitciderp                            | gninraelpeedtahtdelaever | -DCI(sisongaidlufgninaem |                            |                                                    |                                                  |     |
| --- | ------------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------- | --------------------------------------------------- | ------------------------ | ------------------------ | -------------------------- | -------------------------------------------------- | ------------------------------------------------ | --- |
|     |                          |                                                                                           | noitazilituroirP.gnidneps DE,SOL,snoitazilatipsoh( erew)yteixna,DKC,DPOC( | detartsnomeD.srevirdyek noitacifitartsksirecnahne |                             | lanoitidartdnanoisserger ecnamrofreP.noitacifitnedi |                          | sedoc)CTA(gurddna)01     | yltnacifingisserutcetihcra | gnitsacerofnissentsubor .serutidnepxelevel-tneitap | mret-trohshtobderutpac gnitsaceroftsocerachtlaeh |     |
|     |                          | citsigolllademrofreptuo dnasenilesabnoisserger rofksirhgihtastneitap dnastneveelbatneverp | seitidibromocdna)stisiv                                                   |                                                   |                             | tsocllarevorofsenilesab                             | regnoldnaatadgniniart    | yllacinilcnoeromdeiler   | .ytilibaterpretnilacidem   | dnaycaruccadevorpmi                                | mret-gnoldnalaropmet                             |     |
gnitanimircsidniMBG nacgninraelpeedtaht regralhtiwdevorpmi .swodniwnoitavresbo decnahnegnitseggus MTSL-NNCdirbyhehT roflaitnetopgniwohs .gninnalpecruoserdna
|     |                    |     |     |     | .eracFHdesab-eulav egdirdemrofreptuo |     | stneidargdetargetnI |                   | elbmesnededaeh-itluM |     | ylevitceffeelbmesne ,seicnednepeddnert |     |
| --- | ------------------ | --- | --- | --- | ------------------------------------ | --- | ------------------- | ----------------- | -------------------- | --- | -------------------------------------- | --- |
|     | sledomgninraelpeeD |     |     |     |                                      |     |                     | ,sedocgnillibnaht |                      |     |                                        |     |
sgnidniF
|     |                                               |                                                |     |     |                          | dna)6212e¼EPAM,062.0                                                  | sv(80.0¼CRPUA:stneitap stsocgnisaerced;)egdir40.0 |     |                     |                                       | senilesablacissalcrodedaeh |     |
| --- | --------------------------------------------- | ---------------------------------------------- | --- | --- | ------------------------ | --------------------------------------------------------------------- | ------------------------------------------------- | --- | ------------------- | ------------------------------------- | -------------------------- | --- |
|     | scirtemecnamrofrepledoM :CORUAtsehgihdeveihca | %34–93:%1pottanoisicerP                        |     |     | EPAM,236.0¼q,725.0¼r     | MPC,662.0¼2R,4002e¼ gnimrofreptuo–623.0¼ roF.)62.0(cid:3)2R(ASR-ibroM | gnisaercni-tsocgniyfitnedi                        |     |                     | –3(cid:3)EPAM,201(cid:4)5.3(cid:3)EAM |                            |     |
|     |                                               | ,)snoitazilatipsoh(877.0 citsigolrof%51–21.sv( |     |     | :)elbmesne(krowtenlarueN |                                                                       |                                                   |     |                     |                                       |                            |     |
|     | gninraeLpeeDlaitneuqeS                        | 727.0,)stisivDE(186.0                          |     |     |                          | ¼2R(noissergeregdir                                                   | 12.0sv(42.0¼CRPUA                                 |     | MTSL-NNCelbmesneehT | -elgnisllademrofreptuotI              |                            |     |
|     |                                               |                                                |     |     |                          |                                                                       |                                                   |     |                     | .39.0–19.0(cid:3)2R,%4                | .)NNC,MTSL,AMIRA(          |     |
tsebehtdeveihca
:ecnamrofrep
.)noisserger
|     |                          | .)stsoc(                                    |                                               |     |                        |                                           |                     | .)egdir |                         |                                      |     |     |
| --- | ------------------------ | ------------------------------------------- | --------------------------------------------- | --- | ---------------------- | ----------------------------------------- | ------------------- | ------- | ----------------------- | ------------------------------------ | --- | --- |
|     | gnitaulaverofdesuscirteM | .)stsoc(727.0,)stisivDE( ehtrednUaerA(CORUA | noisicerP,)citsiretcarahC erutpaCtsoCdna,)%01 |     |                        |                                           |                     |         | ,)EAM(rorrEetulosbAnaeM |                                      |     |     |
|     | gninraeLpeeDlaitneuqeS   | 186.0,)snoitazilatipsoh(                    |                                               |     |                        | noitciderPs’gnimmuC llaceR–noisicerPrednu | egnahc-tsocrofCORUA |         |                         |                                      |     |     |
|     | ecnamrofrepledom         |                                             | –1(%kpotta)eulaV                              |     | naeM,)q(namraepS       | aerA,)MPC(erusaeM                         |                     |         | derauqSnaeMtooR         | egatnecrePetulosbA 2Rdna,)EPAM(rorrE |     |     |
|     |                          | gnitarepOrevieceR                           | evitciderPevitisoP(                           |     | ,)r(noitalerrocnosraeP | noitciderPetulosbA ,2R,)e,EPAM(rorrE      | dna)CRPUA(evruc     |         |                         | naeM,)ESMR(rorrE                     |     |     |
tsehgihdeveihca
|             |                             |                                                    |                          |          |                           |                          |                                                                  |     |                          | fotneiciffeoC(             | .)noitanimreteD |     |
| ----------- | --------------------------- | -------------------------------------------------- | ------------------------ | -------- | ------------------------- | ------------------------ | ---------------------------------------------------------------- | --- | ------------------------ | -------------------------- | --------------- | --- |
|             |                             | 877.0:CORUA                                        |                          |          |                           |                          | .noitacifissalc                                                  |     |                          |                            |                 |     |
| .noitciderp |                             |                                                    |                          | .%kpotta |                           |                          |                                                                  |     |                          |                            |                 |     |
| erutidnepxe | ledomehtnidedulcniserutaeF  | -ataddna)sdnertnoitazilitu ceV2droWgnisusmialcmorf |                          |          | repsmialcfonoitatneserper | gurdCTA,sesongaidMG-01   | erutaeflanoisnemid-420,333                                       |     |                          |                            |                 |     |
|             | serutaefnevird-egdelwonk939 | ,serudecorp,seitidibromoc                          |                          |          |                           | -DCI:)sretrauq42(retrauq |                                                                  |     |                          | noitazilitugurd,srotacidni |                 |     |
|             |                             | detarenegserutaefnevird                            | laitneuqeshtob,seirotsih |          |                           | ytlaicepsnaicisyhp,sedoc |                                                                  |     | ,redneg,ega(scihpargomeD | ytidibromoc,snoitpircserp  |                 |     |
|             |                             |                                                    |                          |          |                           | gnillibPOG,serudecorp    | dna,ega,xes,)GF(syek !stsoccificeps-rotces retfatneitapreprotcev |     |                          |                            |                 |     |
raey-11(sgniddebme .)laitneuqes-nondna
|     |     | ,stsoc,snoitacidem |     |     |     |     |     | .gniretlifycneuqerf | forebmun,)noiger | suoiverpdna,setar .sdnerterutidnepxe |     |     |
| --- | --- | ------------------ | --- | --- | --- | --- | --- | ------------------- | ---------------- | ------------------------------------ | --- | --- |
SPO,GRD,sedoc
,scihpargomed(
lanoisnemid-hgiH
erachtlaeh
| rof | derapmocledomrehtO stnairavowt(noisserger | .)MBG(ledoMgnitsooB |     |     |     |     |     |     | detargetnIevissergeRotuA |     |     |     |
| --- | ----------------------------------------- | ------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |
;)serutaefdetimilhtiw
tneidarG;)serutaef
| sledom |                     | citsigoldecnahnE |     |     |     |     |     |     |               |     |     |     |
| ------ | ------------------- | ---------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
|        | citsigollanoitidarT | 939(noisserger   |     |     |     |     |     |     | egarevAgnivoM |     |     |     |
noissergeregdiR
)AMIRA(
lacissalc
tuopord,noitavitcaULeR
|          | epytledomgninraelpeeD :gninraeLpeeDlaitneuqeS |                                                                            | drawroF-deeF:gninraeL |     | reyalitlumdetcennoc-ylluF | ,hcaesnoruen05,sreyal                 |     |     | dedaeH-itluM/)MTSLHM( |                                    |     |     |
| -------- | --------------------------------------------- | -------------------------------------------------------------------------- | --------------------- | --- | ------------------------- | ------------------------------------- | --- | --- | --------------------- | ---------------------------------- | --- | --- |
| dna      |                                               | htiw)MTSL(yromeM ;msinahcemnoitnetta larueNlanoitulovnoC -noN.)NNC(krowteN | .)NNF(krowteNlarueN   |     | neddih4(nortpecrep        | ,rezimitpoMADA,52.0 .)snur5foelbmesne |     |     |                       | dirbyH/)NNCHM(NNC elbmesneMTSL-NNC |     |     |
|          | mreT-trohSgnoL                                |                                                                            |                       |     |                           |                                       |     |     |                       | ledomMTSLdekcatS                   |     |     |
| gninrael |                                               | peeDlaitneuqes                                                             |                       |     |                           |                                       |     |     | MTSLdedaeH-itluM      |                                    |     |     |
peed
| fo       | snoitazilatipsohelbatneverP | -6(stisivDEelbatneverP                                  |     |     |                                              |                     |     |     |                      |                     |     |     |
| -------- | --------------------------- | ------------------------------------------------------- | --- | --- | -------------------------------------------- | ------------------- | --- | --- | -------------------- | ------------------- | --- | --- |
|          | .g.e(elbairavemoctuO        |                                                         |     |     | erac-htlaehraey-enolatoT tsocdna)soruE(stsoc | esaercedroesaercni( |     |     |                      | emitrepserutidnepxe |     |     |
| sgnidnif |                             | )2(;)nozirohhtnom )3(;)nozirohhtnom -1(stsocelbatneverP |     |     |                                              | neewtebdlof-001>    |     |     |                      |                     |     |     |
|          | )elbairavtegrat             | -6(snoitazilatipsoh                                     |     |     |                                              | seirogetacegnahc    |     |     | level-tneitapegarevA |                     |     |     |
|          | elbatneverP)1(              |                                                         |     |     |                                              |                     |     |     |                      | /ylkeew(doirep      |     |     |
ro(erachtlaeh
|     |     |     | )nozirohraey |     |     |     |     |     |     | )noitacidem |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
.)ylhtnom
.)sdoirep
evitarapmoC
71)1202(.latesiweL
.latessoB-ewerD
.latekihsuaK
.2 01)2202( 81)0202(
elbaT
ydutS

|     |     |     |     |     |     |     |     | JOURNALOFMEDICALECONOMICS |     |     | 661 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- |
)deunitnoc(
-itlumfotsoclanoitatupmoC– otnithgisnidetimilsedivorp tceffaserutaeflautxetwoh gnissimoteudsaiblaitnetoP– sisylanaytiuqerossenriafoN– eudFRnignittifrevoelbissoP– detimilniamerycnerapsnart otezilarenegtonyamstluseR– rosmetsyserachtlaehrehto
|     |     | peedksat-itlumdnaweiv PUR:ytilibanialpxedetimiL– | slatipsohssorcanoitadilav | RMEssorcaseicnetsisnocni | xob-kcalb(stuptuoledom cimonoceoicosfoecnesbA– |     |     |     | elpmasllamsotdetubirtta .noitazimitpodetimildna | .)ylnoatadlanoitces-ssorc( |     |
| --- | --- | ------------------------------------------------ | ------------------------- | ------------------------ | ---------------------------------------------- | --- | --- | --- | ----------------------------------------------- | -------------------------- | --- |
segnellahcdeifitnedI dnaycnerapsnartfokcaL– -smialcdnoyebselbairav evisnetniyllanoitatupmoC– .gninutretemaraprepyh serutaeflaropmetfokcaL– dnaytilibanialpxeledoM–
|     | ytilibazilarenegdetimiL– RMEesenihCdnoyeb |                   |                    |     | NNRniytilibaterpretni | ytilibazilarenegdetimiL– diacideMehtedistuo |                    |     |                  |                                      |     |
| --- | ----------------------------------------- | ----------------- | ------------------ | --- | --------------------- | ------------------------------------------- | ------------------ | --- | ---------------- | ------------------------------------ | --- |
|     |                                           |                   |                    |     |                       |                                             | detimildnagniniart |     |                  | .teselbairavegralot .sehcaorppaLMrof |     |
|     |                                           | .gniniartgninrael | lanretxefoecnesbA– |     |                       |                                             |                    |     | ecnamrofreprednu |                                      |     |
.serutaefdesab
|     |     |     |              | gnidocroatad |     |     |                          |     | krowtenlarueN– |     | .serutcurtstsoc |
| --- | --- | --- | ------------ | ------------ | --- | --- | ------------------------ | --- | -------------- | --- | --------------- |
|     |     |     | .snoitciderp | .seirtnuocro |     |     | .noitalupop fonoissucsid |     |                |     |                 |
.)noitatimil
|     | .smetsys                  |                                                 |                                                     |     | .smetsys                                 |                                                                     | .dedulcni                                          |                                                    |                                                              |                       |     |
| --- | ------------------------- | ----------------------------------------------- | --------------------------------------------------- | --- | ---------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------ | --------------------- | --- |
|     |                           | ytilibapacstignitartsnomed                      | sawnoisufdesab-noitnetta                            |     | deen-hgihtsoc-hgihgnoma                  |                                                                     | gnithgilhgih,)MBG(sledom oslatI.noitciderpgnidneps | erew)seirotcejartgnidneps citatsnahtevitciderperom |                                                              | :krowteNlarueN–;.%85¼ |     |
|     | gninraelpeedweiv-itlumehT | desab-eertdnanoisserger ,scirtemllassorcasledom | .ylevitceffeatadderutcurts /sisongaidfonoisulcniehT |     | ylralucitrap,serutidnepxe                | ledomNNRehT.stneitap raeniL,OSSAL(noisserger elbmesnedna)noissergeR | laropmettahtdezisahpme                             |                                                    | RiH,833,1e¼EAM,574.0 ¼2R-jda:MLG–;.%76¼ RiH,536,1e¼EAM,743.0 |                       |     |
|     | lanoitidartdemrofreptuo   | dnalautxetetargetniot                           | ecnamrofreproflacitirc                              |     | niecnetsisreplaropmet                    |                                                                     |                                                    | roscihpargomedtneitap                              | ¼2R-jda:tseroFmodnaR–                                        | ¼EAM,613.0¼2R-jda     |     |
|     |                           |                                                 |                                                     |     |                                          | lacissalcdemrofreptuo                                               | rofgninraellaitneuqes                              |                                                    |                                                              |                       |     |
|     |                           |                                                 | dnastxetnoitarepo                                   |     | gnortsdnuofydutsehT erachtlaehlaudividni |                                                                     | erachtlaehcimanyd tnecer.g.e(serutaef              |                                                    |                                                              | .%55¼RiH,066,1e       |     |
fosegatnavdaeht
sgnidniF )PUR(hcaorppa
.sesongaid
.sniag
|     |     |     | eht,FRdnaMBGotderapmoC |     |     |     |     |     | ,574.0fo2R-jdanadeveihcaFR fo2R-jdanadahMLG;%76 | krowtenlaruen;%85foRiH EAM,613.0fo2R-jdanadah |     |
| --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | ----------------------------------------------- | --------------------------------------------- | --- |
scirtemecnamrofrepledoM ledomgninraelpeedPURehT llanahtrewolyltnacifingis seulavderauqs-R.ycarucca NHCHrofrorrenoitciderp ehtotderapmocstneitap gniwohs,sdoireptsocroirp -emiterutpacotytilibasti foRiHdna,8331efoEAM dna,5361efoEAM,743.0 %55foRiHdna,0661efo
|     |     |                      |                 |     | dnaMBGdemrofreptuoNNR | NNR.noitalupoplareneg 4–3gnitaroprocninehw | .snrettaptsoctnedneped |     |     |     |     |
| --- | --- | -------------------- | --------------- | --- | --------------------- | ------------------------------------------ | ---------------------- | --- | --- | --- | --- |
|     |     | dnatsocrof58.0>:CCP– |                 |     | rewol;7.0nahtretaerg  | devorpmiecnamrofrep                        |                        |     |     |     |     |
|     |     | .)100.0<p(senilesab  | decuderledomPUR |     | noitciderpniOSSAL     |                                            |                        |     |     |     |     |
ybrorrenoitciderp
,)tsoc(396.0:ESMR–
.SOLrof08.0>
|     |     | .154.0:EAM– | .%51–21(cid:5) |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
:deveihca
| gnitaulaverofdesuscirteM |     |     |     |     |     |     |     |     | ,)2R-jda(derauqs-RdetsujdA |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
rorrEderauqSnaeMtooR etulosbAnaeM,)ESMR( naeMtooR,)2R(derauqs-R ,)ESMR(rorrEderauqS egatnecrepeht—)RiH( nislaudividnitsoc-hgih lautcafoelicedpoteht
ecnamrofrepledom nosraeP,)EAM(rorrE rorrEetulosbAnaeM oitaRtiHdna,)EAM( deifitnediyltcerrocfo
|     |     |     |     |     | fonosirapmocdna ssorcasnoitubirtsid |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
.)CCP(tneiciffeoC
rorrenoitciderp
.erutidnepxe
noitalerroC
.sledom
ledomehtnidedulcniserutaeF ,snrettapnoitazilitudnatsoc )shtnom4–1fosgal(sdoirep ,)gnigami,snoitacidem,syats
|     |                         | ,sutatsegrahcsid,srotacidni                      |                                                                     | ,srotacidnilevel-tnemtraped .sedocpuorgecruoserdna | sisongaid(serutaeflacinilc lacirotsih,)esunoitacidem | .srotacidniytidibromocdna | etaulaveotdedulcnierew |     |                                               |                         |     |
| --- | ----------------------- | ------------------------------------------------ | ------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------- | ------------------------- | ---------------------- | --- | --------------------------------------------- | ----------------------- | --- |
|     | noitarepo,epytnoissimda | sisongaidnoissimdadna sisongaiD:atadderutcurtsnU | morfstxetnoitarepodna drowaivdedocnesRME detagerggA:serutaefdevireD |                                                    | scitsiretcarahccihpargomeD ,sedocerudecorp,sedoc     | elpitlumrevostsocroirP    |                        |     |                                               |                         |     |
|     | ,xes,egA:atadderutcurtS |                                                  |                                                                     |                                                    |                                                      |                           |                        |     |                                               | latipsoh,snoitatlusnoc( |     |
|     | ,tnemtrapedlatipsoh     |                                                  |                                                                     |                                                    | ,)noiger,redneg,ega(                                 |                           | .ecnetsisreplaropmet   |     | gnitsixe-erp,redneg,egA noitazilituerachtlaeh |                         |     |
|     |                         |                                                  |                                                                     |                                                    |                                                      |                           |                        |     | noslrahC,snoitidnoc ,xedniytidibromoc         | latotraey-roirpdna      |     |
|     |                         |                                                  | ,stnuocnoitarepo                                                    |                                                    |                                                      |                           |                        |     |                                               | .stsocerachtlaeh        |     |
.sgniddebme
.edoc
)MBG(enihcaMgnitsooB
|                    |                       | 5M,)TD(eerTnoisiceD                  |     |     | dna,noissergeROSSAL                    |                     |     |     |                                            |     |     |
| ------------------ | --------------------- | ------------------------------------ | --- | --- | -------------------------------------- | ------------------- | --- | --- | ------------------------------------------ | --- | --- |
| derapmocledomrehtO |                       | modnaR,eerTledoM tneidarG,)FR(tseroF |     |     | tsniagadekramhcneb                     | atadlacitnedirofNNR |     |     | ledoMraeniLdezilareneG golhtiwnoitubirtsid |     |     |
|                    | ,)RL(noissergeRraeniL |                                      |     |     | ,)RL(noissergeRraeniL lla–)MBG(enihcaM |                     |     |     |                                            |     |     |
|                    | ,)RVS(noissergeR      |                                      |     |     | gnitsooBtneidarG                       |                     |     |     | modnaRdna)knil                             |     |     |
|                    | rotceVtroppuS         |                                      |     |     |                                        |                     |     |     | ammag()MLG(                                |     |     |
.)FR(tseroF
.stilps
roirpfoshtnomelpitlum .atadnoitazilitudnatsoc
epytledomgninraelpeeD asenibmoc–)krowten noitnettaþgniddebme suoenegoreteherutpac weivhcaE.secruosatad saw)txetnoitarepo,txet dnayletarapesdedocne .noisufdesab-noitnetta raenilnonhtiwkrowteN level-tneitapnodeniart
|     |                      | gnisu(redocnedrocer otrotciderpecruoser | sisongaid,derutcurts( |                   | krowteNlarueNtnerruceR ycnednepedlaropmet |     |     |     |                      |     |     |
| --- | -------------------- | --------------------------------------- | --------------------- | ----------------- | ----------------------------------------- | --- | --- | --- | -------------------- | --- | --- |
|     | ,weiv-itlum(ledomPUR | adna)smsinahcem                         |                       | hguorhtdetargetni |                                           |     |     |     | ,snoitcnufnoitavitca |     |     |
|     |                      |                                         |                       |                   | ssorcanoitamrofni                         |     |     |     | larueNdrawrof-deeF   |     |     |
|     | laruenksat-itlum     |                                         |                       |                   | gnirutpac,)NNR(                           |     |     |     |                      |     |     |
ecneuqesdna
.setairavoc
|                      | -ni:stegratsuounitnocowT dna)YNC(stsoclatipsoh | ksat-itlumaivdetciderp |     |     | erutuflatotgnitneserper              |     |     |     |                       |     |     |
| -------------------- | ---------------------------------------------- | ---------------------- | --- | --- | ------------------------------------ | --- | --- | --- | --------------------- | --- | --- |
| .g.e(elbairavemoctuO | .)syad(yatsfohtgnel                            |                        |     |     |                                      |     |     |     | erutidnepxeerachtlaeh |     |     |
|                      |                                                |                        |     |     | htnoMrePrebmeMreP elbairavsuounitnoc |     |     |     | suounitnoc(6102ni     |     |     |
|                      | )elbairavtegrat                                | yltniojerewhtoB        |     |     | erachtlaeh)MPMP(                     |     |     |     | .)sorueni,elbairav    |     |     |
.tneitapreptsoc
|     |     |     |     |     | —erutidnepxe |     |     |     | laudividnilaunnA |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ---------------- | --- | --- |
.gninrael
.deunitnoC
02)8102(.lategnaY
91)1202(.lateuY
.2 .latetnomiV 12)2202(
elbaT
ydutS

.deunitnoC
.2 elbaT
segnellahcdeifitnedI
sgnidniF
scirtemecnamrofrepledoM
gnitaulaverofdesuscirteM
ledomehtnidedulcniserutaeF
derapmocledomrehtO
epytledomgninraelpeeD
.g.e(elbairavemoctuO
ydutS
ecnamrofrepledom
)elbairavtegrat
lanretxefoecnesbA–
krowemarfNAG-VehT
tsewolehtdeveihcaNAG-VehT
rorrEerauqSnaeMtooR
dnascihpargomedtneitaP
,)RL(noissergeRraeniL
evitareneGdesaB-ecnairaV
erutidnepxeegarevayliaD
.latekihsuaK
raelcnudnanoitadilav
decuderyllufsseccus
llaotderapmocESMR
)ESMR(
/esahcruplacirotsih
gnitsooBtneidarG
-V(krowteNlairasrevdA
niapcificepsano
22)0202(
ehtfossenevitatneserper
seicnapercsidecnairav
,sledomkramhcneb
seires-emiterutidnepxe
)RBG(noissergeR
nagnitargetni)NAG
.noitacidem
–tesatadnoitacidem
detarenegdnalaerneewteb
roirepusgnitartsnomed
lacinilcfonoitnemon;atad
rotarenegdesab-MTSL
elgnisaotdetimil
,snoitubirtsiderutidnepxe
tcaxE(.ycaruccaevitciderp
setairavoccimonoceoicosro
desab-NNCadna
tsocdnaaeracituepareht
lanoitidartgnimrofreptuo
yllaciremuntonESMR
reyalitluM.rotanimircsid
fokcal–epyt
peeddnanoisserger
tubtxetnidetroper
dna,)PLM(nortpecreP
lacinilcdnacimonoceoicos
,MTSL(senilesabgninrael
laminimehtsadetacidni
-trohSgnoLdradnats
stcirtserserutaef
devorpledomehT.)PLM
).srotarapmocgnoma
)MTSL(yromeMmreT
redaorbotytilibazilareneg
rofevitceffeylralucitrap
krowten
–gnidnepserachtlaeh
yranoitats-nongniledom
tonytilibaterpretniledom
erutidnepxeerachtlaeh
.dessucsid
.seires
etairavinuotdetimilledoM–
sledomMTSLhtoB
¼2R,558.61¼ESMR:AMIRA
rorrEerauqSnaeMtooR
foatadseires-emitetairavinU
evissergeRotuA(AMIRA
MTSL)allinav(dradnatS)1(
tneitapylhtnomegarevA
.latekihsuaK
on(gnitsacerof
.AMIRAdemrofreptuo
5408.0
)ESMR(
noitacidemylhtnom
gnivoMdetargetnI
reyalneddihenohtiw
anoerutidnepxe
32)7102(
rocihpargomed
ehtdeveihcaMTSLdekcatS
yromem7(MTSLdradnatS
fotneiciffeoC(2R
cihpargomed;serutidnepxe
)kramhcneb,egarevA
)2(dna)sllecyromem7(
noitacidemniapcificeps
.)setairavoccimonoceoicos
.ecnamrofrepevitciderptseb
¼2R,716.41¼ESMR:)sllec
)noitanimreteD
,redneg,ega(selbairav
owthtiwMTSLdekcatS
,gnidnepstekcop-fo-tuo(
noitadilavlanretxefokcaL–
,tsuboreromerewsMTSL
8408.0
erew)raeyhtrib,noiger
yromem4(sreyalMTSL
diap-rerusnignidulcxe
rosepytnoitacidemssorca
rettebdna,cirtemarapnon
yromem4þ4(MTSLdekcatS
nidesutontubelbaliava
.)hcaesllec
.)tnuoma
desabstluseR–.snoitalupop
laropmetgnirutpacta
¼2R,396.31¼ESMR:)sllec
rofdesoporp(sledomniam
yrogetacgurdelgnisano
:noitacilpmI.seicnedneped
9518.0
.)krowetairavitlumerutuf
gnitimil,)noitacidemniap(
troppusdluocsMTSL
,ega(elbaliavascihpargomeD
.ytilibazilareneg
nisksatgnitsacerof
,)raeyhtrib,noiger,redneg
desoporpkrowerutuF–
dnaerutidnepxeerachtlaeh
niamnidesutontub
etairavitlumgnipoleved
.gnikamycilop
krowerutuf(sledom
gnitaroprocnisledomMTSL
etairavitlumdesoporp
dnascihpargomed
)sledom
elpitlumotgnidnapxe
rofseirogetacnoitacidem
tsocerachtlaehredaorb
.gnitsacerof
662 J.T.LEEETAL.

JOURNALOFMEDICALECONOMICS 663
using LSTM and CNN models to support risk stratification and care coordination under value-based care
frameworks17. Two studies from Germany and France examined risk adjustment and insurance premium
prediction, using large national claims datasets to forecast annual healthcare costs and assess whether
deep or tree-based models improved fairness and predictive accuracy in reimbursement and capitation
formulas10,22. Both were conducted within statutory health insurance systems, emphasizing model trans-
parency and calibration for regulatory use10,21. A U.S. Medicaid study analyzed high-need, high-cost
(HCHN) populations, applying recurrent neural networks to predict per-member-per-month expendi-
tures20. A Chinese study using electronic medical records focused on hospital resource utilization, pre-
dicting in-hospital costs and length of stay with a multi-view DNN that combined structured and
unstructured clinical data19. This work supports hospital efficiency improvement and DRG-based pay-
ment reform, linking predictive analytics to provider-level financial management19. Finally, three U.S.
studies addressed pharmaceutical expenditure forecasting, using claims or retail transaction data to pre-
dict weekly, monthly, or daily medication spending18,22,23.
Neural network architectures in the included studies
Neural network architectures were applied according to input type and temporal structure. Feedforward
deep neural networks handled static or high-dimensional features, capturing nonlinear relationships in
cross-sectional data. Recurrent networks (RNNs/LSTMs) modeled temporal dependencies in longitudinal
or multi-wave sequences. More complex architectures—including hybrid CNN-LSTM models, multi-head
ensembles, and generative frameworks (V-GANs)—were used for heterogeneous or non-stationary data,
integrating structured and unstructured inputs.
Across the studies, neural network design generally reflected data characteristics (see Table 3).
Feedforward DNN models were applied to static features21, while Vimont et al., 202221 included a simple
neural network alongside statistical models for comparison. Recurrent architectures captured temporal
dependencies when explicitly implemented, with convolutional neural networks (CNNs) and fully con-
nected networks (FCNs) used to process spatial and static features, respectively (e.g. Lewis et al. 202117)
Hybrid or generative models addressed complex temporal or heterogeneous inputs (Kaushik et al.
201723; 202022; Yu et al. 202119) However, some studies (e.g. Yang et al. 201820) primarily relied on tradi-
tional machine learning approaches.
Evaluation frameworks and performance metrics
All eight studies evaluated model performance using quantitative metrics aligned with their clinical or
policy objectives10,17–23. Six studies employed internal multi-split validation (train–validation–test or
cross-validation)17–19,21–23, while two—Drewe-Boss et al. (2022) and Yang et al. (2018)—used temporal
holdout samples to assess generalizability10,20. None performed full external validation across independ-
ent datasets.
Longitudinal prediction studies (n¼6)—Drewe-Boss et al. (2022), two studies from Kaushik et al.
(2020), Kaushik et al. (2017), Yang et al. (2018), and Lewis et al. (2021)—focused on forecasting accuracy
and discrimination10,17,18,20,22,23. Most reported RMSE (n¼4)18–20,22,23 and some reported MAE
(n¼2)10,18 and R2 or correlation coefficients (r, q) to quantify fit. Lewis et al. (2021) also included
AUROC, precision@k, and cost-capture to evaluate high-risk identification17, while Drewe-Boss et al.
Table 3. Neural network architectures applied in the included studies.
Neuralnetworkarchitecture Datatype Models Studies
Feedforward/DNN Staticorhigh-dimensionaldata Standarddeepneuralnetwork Drewe-Bossetal.202210
Simpleneuralnetwork Staticorhigh-dimensionaldata Simpleneuralnetwork Vimontetal.,202221
(comparisonwithstatistical
models)
Recurrent Longitudinalortime-dependent RNN,LSTM(auxiliary:CNN,FCN) Lewisetal.202117
data
Hybrid/generative Complextemporalpatterns, Hybridorgenerativemodels Kaushiketal.201723;202018;
heterogeneousdata (e.g.V-GAN) 202022;Yuetal.202119

664 J.T.LEEETAL.
(2022) and Kaushik et al. (2020) added AUPRC and Mean Absolute Percentage Error (MAPE), respectively,
for trend and cost-change detection10,18. Sequential models such as LSTM and CNN-LSTM were assessed
primarily on temporal forecasting stability and error reduction18,23.
Cross-sectional studies (n¼2)—Vimont et al. (2022) and Yu et al. (2021)—emphasized model fit and
numerical error for static cost prediction19,21. Vimont et al. (2022) used adjusted R2, MAE, and Hit Ratio
to compare neural networks with GLM and Random Forest for national reimbursement modeling21. Yu
et al. (2021) evaluated RMSE, MAE, and Pearson correlation coefficient for in-hospital cost and length-of-
stay prediction19.
Across all papers, R2/adjusted R2 (n¼5), MAE (n¼4), RMSE (n¼5), and AUC or related discrimination
metrics (n¼2) were most frequently reported10,17–23. Only one study addressed calibration to a limited
extent19, and none included decision-curve, net-benefit, or fairness analyses.
Explainability frameworks such as Integrated Gradients was carried out in Drewe-Boss et al. (2022)10.
Comparative performance of neural networks versus classical models
Across studies comparing neural architectures with classical regression and ensemble methods, neural
models generally performed best when applied to longitudinal or temporally rich healthcare
data10,17–23.
Recurrent and hybrid architectures captured temporal persistence and nonlinear dynamics that tradi-
tional approaches often missed. In a U.S. Medicaid study, Yang et al. (2018) showed that, for predicting
raw Per Member Per Month (PMPM) dollar amount expenditures, a recurrent neural network increased
test R2 from about 0.14–0.17 (for linear regression and GBM) to 0.30 and reduced RMSE by roughly one-
third, with similar improvements in RMSE among the top 10% highest-cost patients; on log- and per-
centile-transformed outcomes, R2 differences across models were smaller, but the RNN still achieved
lower overall and high-cost error.20 Kaushik et al. (2017) likewise found that stacked LSTMs improved
RMSE by nearly 19% over ARIMA forecasts for a medication-spending time series23, while a later multi-
headed CNN–LSTM, Convolutional LSTM, and CNN-LSTM ensemble achieved even stronger performance
with R2 values around 0.8–0.9 in patient-level forecasting18. Lewis et al. (2021) also reported that sequen-
tial deep models outperformed gradient boosting and logistic regression in predicting preventable hos-
pitalizations and costs, attaining AUROCs up to approximately 0.78.17
The picture was more mixed in cross-sectional cost prediction. In a French nationwide claims study,
Vimont et al. (2022) found that a relatively shallow two-hidden-layer MLP performed similarly to a gener-
alized linear model but was clearly outperformed by a random forest (adj-R2 0.475 vs.0.347 and 0.316
for GLM and neural network; MAE e1,338 vs. e1,635 and e1,660), suggesting limited benefit of shallow
neural architectures on tabular cost data21. By contrast, in China, Yu et al. (2021) demonstrated that
when rich structured and textual EMR inputs were available, a multi-view deep learning model integrat-
ing diagnosis and operation text with structured features clearly surpassed all regression and tree-based
baselines, reducing prediction error by roughly 12–15%.19
Figure 2 illustrates roughly how predictive performance evolves as data become richer and more com-
plex. The x-axis moves from simple cross-sectional claims to increasingly heterogeneous, longitudinal, and
multimodal data; the y-axis represents relative model performance. Classical regression performs well for
simple, low-dimensional tabular inputs but tends to plateau as complexity increases. Tree-based machine-
learning models (e.g. random forests, gradient boosting) extend performance by capturing nonlinearities,
typically outperforming regression across most settings. It is important to note that Figure 2 is a concep-
tual framework developed to synthesize the evidence reviewed in this study and to illustrate the proposed
Complexity–Performance Hypothesis24. The figure is intended to visualize the overall performance trends
of different model families as data complexity increases and does not represent empirical estimates
derived directly from any individual study.
Shallow feed-forward neural networks (green) show the weakest performance in the cross-sectional
regime—consistent with Vimont et al. (2022), where a two-layer MLP achieved an adjusted R2 of only
0.316, below both RF (0.475) and GLM (0.347)21. Without sequential structure or rich feature representa-
tions, shallow networks offer limited advantage over traditional methods. However, deep neural architec-
tures (red) behave differently. Even in cross-sectional settings, when richer input modalities are
available—as in the multi-view RUP model using structured and textual EMR features (Yu et al. 2021)—

JOURNALOFMEDICALECONOMICS 665
Figure 2. Model performance by data complexity.
deep learning can clearly outperform both regression and tree-based baselines.19 As data become
increasingly high-dimensional, sequential, or multimodal, deep networks benefit from their higher cap-
acity and representation learning capabilities. This produces the strongest gains in the longitudinal/
multimodal regime, where studies such as Lewis et al. (2021), Yang et al. (2018), Kaushik et al. (2017/
2020), and Kaushik et al. (2020V-GAN) show that recurrent, convolutional, and hybrid deep models out-
perform classical and ensemble methods by substantial margins17,18,20,22,23.
Building on these findings, we formulate what we term the Complexity–Performance Hypothesis,
which posits that model accuracy is maximized when the capacity of the modeling approach is matched
to the complexity of the data. When data are simple and homogeneous, classical regression performs
competitively, reflecting its efficiency in low-dimensional settings. As data gain nonlinear structure or
moderate dimensionality, tree-based machine-learning methods begin to offer clear advantages by cap-
turing interactions and flexible decision boundaries. With further increases in data richness—such as
large-scale, temporal, or multimodal inputs—DNN models provide the greatest performance gains, often
surpassing alternative approaches by a wide margin.
Discussion
Primary findings
Across the eight included studies, deep learning models demonstrated consistent performance gains
over classical regression, though the magnitude and nature of improvement varied by study design and
data type. The strongest advantages were observed in longitudinal analyses, while cross-sectional appli-
cations yielded smaller or mixed results. These results provide empirical support for the Complexity–
Performance Hypothesis, which proposes that predictive accuracy depends on how well a model’s archi-
tecture is matched to the underlying structure and complexity of the data.
In longitudinal or time-series prediction tasks, such as forecasting healthcare expenditures, hospitaliza-
tions, or medication costs, neural networks with sequential structures—particularly LSTM and CNN-
LSTM—achieved notable accuracy improvements, typically showing roughly 10–20% lower prediction
error (RMSE or MAE) and absolute R2 improvements of about 1–15 percentage points compared with
classical regression or autoregressive models. These architectures effectively captured temporal persist-
ence, nonlinear cost dynamics, and patterns of high-cost episodes that static models failed to represent.
In contrast, cross-sectional models predicting single-year or aggregated costs showed more limited
improvements. Shallow feed-forward neural networks performed similarly to or worse than classical
regressions—while tree-based methods such as random forests and gradient boosting often matched or
exceeded neural performance in overall fit and calibration. However, when unstructured or multimodal
inputs such as EMR text were incorporated, deep learning achieved clearer advantages, yielding larger

666 J.T.LEEETAL.
error reductions and demonstrating greater flexibility in modeling heterogeneous clinical information.
Taken together, these findings suggest that deep learning delivers its greatest advantages in settings
with temporal depth or multimodal complexity, whereas classical and ensemble methods can remain
competitive—or superior—when the task is cross-sectional and inputs are purely tabular or the neural
architecture is relatively shallow.
Across studies, feature importance patterns were highly consistent. Prior costs and utilization emerged
as the dominant predictors, followed by comorbidities, procedures, and medication use. Very few models
incorporated social determinants, behavioral data, or text-based clinical variables, limiting interpretability
and potential policy translation.
When compared across methodological families, deep learning outperformed classical regression in nearly
all contexts, but tree-based models remained highly competitive in cross-sectional settings that emphasize
transparency and calibration. Overall, the evidence suggests that deep learning excels when data are longitu-
dinal, high-dimensional, or sequential, while classical and tree-based methods continue to provide stable,
interpretable baselines for policy-oriented modeling such as risk adjustment and premium setting.
Although most included studies involved large sample sizes, often ranging from tens of thousands to sev-
eral million observations, these studies generally possessed sufficient statistical power to detect meaningful
performance improvements, such as significant reductions in RMSE or MAE. Nevertheless, the overall conclu-
sions remain influenced by contextual factors, including the concentration of studies within specific countries
or insurance systems and the reliance on single-database observational designs. Importantly, these limitations
do not overturn the overarching conclusion that deep learning offers advantages over traditional regression
in longitudinal time-series cost prediction. However, effect size estimates—particularly across specific popula-
tions, subgroups, or neural network architectures—should be interpreted with caution.
Through the integration of theoretical considerations and empirical evidence, this review articulates
the Complexity–Performance Hypothesis as a unifying framework to explain these findings. In data sce-
narios characterized by relatively low dimensionality or limited complexity, traditional regression models
are often sufficient to achieve effective prediction. As data complexity increases—through greater nonli-
nearity or interaction effects—tree-based machine learning models begin to demonstrate advantages in
flexibility and fit. When data are both high-dimensional and longitudinal or multimodal, DNN models
with hierarchical feature-learning capabilities exhibit the greatest potential to improve overall prediction
error and identify high-cost tails. Importantly, this hypothesis is derived inductively from the eight
included empirical studies and is presented as a conceptual framework to guide model selection across
data structures and application scenarios, rather than as a precise estimate of a single causal effect.
Implications for health economics and policy
From a health economics and healthcare finance perspective, these findings translate into operational
guidance regarding when deep learning is most appropriate for real-world application. Specifically, deep
learning models are most relevant for healthcare cost prediction tasks that integrate longitudinal data or
multiple data modalities25. Under such conditions, neural networks tend to achieve lower overall predic-
tion error and demonstrate superior ability to identify high-cost populations, compared with traditional
regression and some tree-based models. In practice, this improved discrimination can support earlier
identification of high-risk individuals and inform budget planning and resource allocation decisions26.
When sufficient data infrastructure, computational resources, and institutional support are available,
deploying high-complexity deep learning models can be cost-effective and analytically justified. By con-
trast, in cross-sectional risk-adjustment or insurance estimation settings—where available predictors are
limited to standard claims data or a small number of structured covariates—the empirical evidence indi-
cates that shallow neural architectures yield only marginal improvements in explanatory power or cali-
bration. In such scenarios, tree-based machine learning models often achieve comparable or superior
performance, while offering greater interpretability.
Moreover, under regulatory and governance constraints, tree-based models typically impose lower com-
munication and transparency costs when engaging with policymakers and supervisory agencies27.
Accordingly, GLM-based two-part models and selected tree-based approaches remain appropriate baseline
choices for many applied health economics analyses. Adoption of deep learning in these contexts should be

JOURNALOFMEDICALECONOMICS 667
contingent upon direct head-to-head comparisons conducted on identical datasets and data partitions, dem-
onstrating reproducible and policy-relevant improvements in cost capture, budget accuracy, and high-cost
| population | monitoring. |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- |
Finally, practical deployment of deep learning models requires careful consideration of downstream
resource requirements, including computational infrastructure, MLOps maturity, and the capacity to
explain model behavior to decision-makers and regulators28. Within health economics, the Complexity–
Performance Hypothesis therefore implies not only a statistical matching between model capacity and
data structure, but also a balanced assessment of predictive gains, transparency, and institutional feasi-
bility. Given that most routine analytic workflows in insurance and public health agencies continue to
rely on GLM and tree-based models, the limited availability of readily deployable deep learning plat-
| forms remains     | a non-trivial | barrier     | to widespread | adoption29. |     |     |
| ----------------- | ------------- | ----------- | ------------- | ----------- | --- | --- |
| Future directions | and           | fundamental | challenges    |             |     |     |
To guide future research, this review delineates five fundamental challenges in applying deep learning
to healthcare expenditure prediction, outlines actionable strategies for their resolution, and identifies pri-
orities for collaboration between machine learning scientists and health economists (see Table 4).
| Challenge | 1: limited economic | interpretability |     |     |     |     |
| --------- | ------------------- | ---------------- | --- | --- | --- | --- |
Despite the high predictive accuracy of deep learning architectures, their opaque internal representa-
tions constrain economic interpretation and policy translation34. The “black-box” nature of neural net-
works obscures causal pathways and cost-driver interactions, limiting their relevance for accountability
and decision-making in health financing27. To align model outputs with economic reasoning, deep learn-
ing models should integrate explainable-AI (XAI) approaches—such as SHAP, Integrated Gradients, or
Propagation—and
Layer-wise Relevance report marginal effects comparable to those derived from gen-
eralized linear or two-part models. Developing hybrid “interpretable-deep” frameworks that embed
econometric constraints within neural architectures may reconcile predictive precision with transparency,
analyses35.
| facilitating | their integration | into budget-impact |     | and resource-allocation |     |     |
| ------------ | ----------------- | ------------------ | --- | ----------------------- | --- | --- |
Table 4. Challenges of deep learning in predicting healthcare spending and expenditure, and how they may be over-
| come with  | future development. |     |               |     |     |            |
| ---------- | ------------------- | --- | ------------- | --- | --- | ---------- |
| Challenges |                     |     | Currentstatus |     |     | Strategies |
Limitedeconomic Deeplearningmodelsachievehigh (cid:6) IncorporateexplainableAI(XAI)frameworkssuchas
interpretability predictiveaccuracybutprovidelimited SHAPorIntegratedGradients.
|     |     | transparencyforeconomicreasoning,    |     |     | (cid:6) Reportmarginaleffectsandsensitivityanalyses |     |
| --- | --- | ------------------------------------ | --- | --- | --------------------------------------------------- | --- |
|     |     | policytranslation,orcausalinference. |     |     | comparabletotraditionalregressionoutputs.           |     |
(cid:6) Develophybridinterpretable-deepmodelstailored
forcostdriversandbudgetimpactinterpretation.
Insufficientbenchmarking Manystudieslackdirect,standardized (cid:6) Requireside-by-sidebenchmarkingusingidentical
againstclassical comparisonsbetweendeeplearning datasetsandperformancemetrics.
(cid:6)
regression modelsandestablishedregression Emphasizecalibration,fairness,andwelfare
|     |     | frameworks(GLM,two-part,orhurdle |     |     | implicationsbeyondaccuracy.                      |     |
| --- | --- | -------------------------------- | --- | --- | ------------------------------------------------ | --- |
|     |     | models)30.                       |     |     | (cid:6) Promotetransparentreportingofincremental |     |
predictiveandeconomicgains.
Shorttemporalprediction Mostmodelspredictone-yearcosts, (cid:6) Extendmodelinghorizonstomulti-yearpredictions.
| horizons31 |     |                                  |     |     | (cid:6)                                   |     |
| ---------- | --- | -------------------------------- | --- | --- | ----------------------------------------- | --- |
|            |     | overlookinglong-termexpenditure  |     |     | Incorporatelongitudinalclaimsdataandtime- |     |
|            |     | dynamicsorpersistenceofhigh-cost |     |     | dependentsurvivalorsequencemodels.        |     |
status. (cid:6) Evaluatetemporalgeneralizationviarolling-window
validation.
Limiteddatadiversityand Currentstudiesrelyheavilyonsingle- (cid:6) Promotemulti-country,multi-payerbenchmarking
| generalizability |     | countryorproprietarydatasets,restricting |     |     | datasets.                                              |     |
| ---------------- | --- | ---------------------------------------- | --- | --- | ------------------------------------------------------ | --- |
|                  |     | generalizationacrosssystemsand           |     |     | (cid:6) Integrateopen,de-identifiedEHRoradministrative |     |
|                  |     | populations32.                           |     |     | datawithharmonizedcoding.                              |     |
(cid:6) Implementdomainadaptationandfederated
learningforprivacy-preservingcollaboration.
(cid:6)
Underuseofsocialand Modelspredominantlyusedemographicand Linkcostdatawithareadeprivation,socioeconomic,
behavioraldeterminants clinicalvariables,neglectingsocial orbehavioralriskindices.
|     |     | determinantsofhealth(SDOH)and |     |     | (cid:6) QuantifyincrementalexplanatorypowerofSDOH |     |
| --- | --- | ----------------------------- | --- | --- | ------------------------------------------------- | --- |
|     |     | behavioralpredictors33.       |     |     | variablesonexpenditureprediction.                 |     |
(cid:6) IntegrateSDOHembeddingsinmultimodal
architectures.

668 J.T.LEEETAL.
Challenge 2: insufficient benchmarking against classical regression
The absence of standardized benchmarking between deep learning models and traditional regression frame-
works remains a major methodological gap36. Many studies neglect formal comparisons with generalized lin-
ear, hurdle, or two-part models, or apply inconsistent data partitions and performance metrics, precluding
rigorous assessment of incremental value. Future research should direct, head-to-head benchmarking using
identical datasets, covariates, and validation procedures36. Evaluation must extend beyond statistical accuracy
to encompass calibration, discrimination, and welfare-relevant metrics such as cost-capture or decision-curve
analysis37. Transparent reporting of incremental explanatory power relative to GLM baselines will clarify
when the additional complexity of deep learning models is justified38.
All eight studies included in this review met the pre-specified minimum comparison criteria by incor-
porating at least one traditional or tree-based
comparator10,17–23.
However, only Drewe-Boss et al. (2022)
and Vimont et al. (2022) partially satisfied more stringent benchmarking requirements, including consist-
ent sample splits direct comparison with GLM two-part models10,21. The remaining studies reported
results under heterogeneous subgroup definitions or outcome specifications, limiting their suitability as
complete benchmarking
cases17–20,22,23.
Drawing on principles articulated in DECIDE-AI, we emphasize the importance of clearly defining
application scenarios, target populations, comparator models, and evaluation structures a priori36.
Although not specific to economic evaluation, these principles provide a useful framework for structur-
ing systematic and transparent benchmarking between neural networks and classical cost-prediction
models.
Challenge 3: short temporal prediction horizons
Most existing models focus on one-year prediction horizons, reflecting budget-cycle pragmatism but
neglecting the persistence and temporal dependencies of high-cost conditions31. Extending prediction
windows to multi-year horizons using longitudinal claims and EHR data would better capture dynamic
health-state transitions39. Sequence-based architectures (e.g. LSTM, GRU, transformer models), combined
with rolling-window validation, should be used to assess temporal stability39.
Across the included studies, training windows often exceeded the prediction horizon. For example,
Drewe-Boss et al. (2022) used data from 2010–2015 to predict costs in 2016–201710, while Lewis et al.
(2021) analyzed commercial claims data spanning 2006–2017.17 Kaushik et al. (2017, 2020a, 2020b) typic-
ally employed four to five years of training data with the final year reserved for testing18,22,23, whereas
Vimont et al. (2022) and Yu et al. (2021) relied primarily on cross-sectional designs19,21. However, details
regarding training and observation periods were often confined to tables and not fully discussed in the
main text. Future studies should provide explicit disclosure of calendar years and observation windows
to strengthen assessment of longitudinal performance and cross-context generalizability.
Challenge 4: limited data diversity and generalizability
Most studies rely on single-country, single-payer, or proprietary datasets, limiting external validity and
constraining cross-system generalization40. Differences in coding standards, benefit structures, and reim-
bursement schemes further impede model transferability. Addressing this challenge requires the estab-
lishment of multi-country, multi-payer benchmark datasets with harmonized variable definitions and cost
metrics41. Privacy-preserving and federated learning architectures can facilitate cross-institutional collab-
oration without compromising confidentiality41. Domain-adaptation techniques should be developed to
recalibrate models for heterogeneous populations and health systems. Publicly accessible, de-identified
datasets adhering to FAIR (Findable, Accessible, Interoperable, Reusable) data principles are essential for
reproducibility and methodological transparency42.
Challenge 5: underuse of social and behavioral determinants
Current deep learning cost-prediction models overwhelmingly depend on demographic and clinical variables,
with limited incorporation of social determinants of health (SDOH) or behavioral risk factors. Yet socioeco-
nomic conditions, education, and lifestyle behaviors exert substantial influence on utilization patterns and
cost trajectories43. Integrating SDOH requires linking administrative and clinical data with census, deprivation,

JOURNALOFMEDICALECONOMICS 669
or behavioral datasets, and representing these inputs through multimodal embeddings that capture latent
social context44. Quantifying the incremental explanatory and policy value of SDOH variables will help iden-
tify structural cost drivers and guide equitable allocation of healthcare resources.
Study limitations
This systematic review included only eight studies, and substantial heterogeneity was observed in
research design, data sources, healthcare systems, outcome definitions, and performance metrics. As a
result, quantitative meta-analysis was not feasible, and findings were synthesized narratively by identify-
ing consistent directional patterns. Most studies relied on single-country, single-database designs and
lacked external validation across time periods or healthcare systems. Additionally, the predominance of
one-year prediction horizons limits assessment of long-term robustness and generalizability.
Consequently, the Complexity–Performance Hypothesis should be viewed as a working hypothesis,
requiring further systematic validation rather than a definitively established causal mechanism.
Conclusion
Although the studies reviewed offer preliminary support for the Complexity–Performance Hypothesis,
rigorous empirical validation is still in its early stages. Future research should conduct head-to-head
benchmarking of modeling approaches on the same datasets, systematically varying dimensionality and
temporal depth to determine the threshold at which adopting deep neural networks becomes justified
over classical regression or ensemble methods. Deep learning offers clear gains for longitudinal,
sequence-rich cost forecasting, whereas tree-based methods remain highly competitive for cross-sec-
tional tabular prediction. Overall, these findings are consistent with the proposed Complexity–
Performance Hypothesis, which posits that the predictive advantages of deep learning emerge primarily
when model capacity is well matched to data complexity.
Transparency
Declaration of funding
This research was supported by the National Health Research Institutes (NHRI) Integrated Research Grant for
Biomedical and Health-Related Sciences Innovative Research Grant (IRG) (NHRI-EX114-11421PI) and the Mount Jade
ProjectYushan Fellow Program oftheMinistryof Education(MOE),Taiwan (MOE-112-YSFMN-0003-002-P1).
Declaration of financial/other interests
D.B.-C. W. is employed by Johnson & Johnson; this position is independent of and unrelated to the research pre-
sented in this manuscript. All other authors declare that they have no conflicts of interest relevant to the content of
this article.Peerreviewerson thismanuscript havenorelevant financialor other relationshipsto disclose.
Author contributions
J.T.L.conceivedanddesignedthestudy,conductedtheanalysis,andledthemanuscriptwriting.M.H.-S.Y.performed
the literature search and screening. All authors contributed to drafting and refining the of the manuscript. All
authorsread andapproved thefinalmanuscript.
Acknowledgements
JTL is partly funded by the Ministry of Education, Taiwan, through the Mount Jade Fellowship and the Mount Jade
Project Yushan Fellow Program (MOE-112-YSFMN-0003-002-P1) as well as by the National Health Research Institutes
(NHRI) Integrated Research Grant for Biomedical and Health-Related Sciences Innovative Research Grant (IRG) (NHRI-
EX114-11421PI)

670 J.T.LEEETAL.
| Use of generative | AI  |     |
| ----------------- | --- | --- |
The authors used ChatGPT (OpenAI, GPT-4o, 2025) to assist with language polishing and grammar/word checking
only.
| Data availability | statement |     |
| ----------------- | --------- | --- |
This systematic review is based solely on data extracted from published articles. No new datasets were created.
Extracteddatatablesandthe PRISMAchecklist canbe providedupon reasonable request.
ORCID
| JohnTayu Lee http://orcid.org/0000-0002-1551-4923   |                                         |     |
| --------------------------------------------------- | --------------------------------------- | --- |
| Melody Hsiao-San Yeh                                | http://orcid.org/0009-0009-4116-0637    |     |
| VincentCheng-Sheng                                  | Li http://orcid.org/0009-0006-8719-1699 |     |
| Hsiao-Hui Chen http://orcid.org/0000-0001-7897-3118 |                                         |     |
Yi-HsuanLiu http://orcid.org/0009-0007-5727-8328
| DavidBin-Chia Wu | http://orcid.org/0000-0002-0313-5758 |     |
| ---------------- | ------------------------------------ | --- |
References
[1] Dieleman JL, Campbell M, Chapin A, et al. Future and potential spending on health 2015–40: development
assistance for health, and government, prepaid private, and out-of-pocket health spending in 184 countries.
Lancet.2017;389(10083):2005–2030.
| The |     | doi: 10.1016/S0140-6736(17)30873-5. |
| --- | --- | ----------------------------------- |
[2] Rao KD, et al. Future health expenditures and its determinants in Latin America and the Caribbean: a multi-
| country projection | study. TheLancet | Regional Health–Americas;2025. |
| ------------------ | ---------------- | ------------------------------ |
[3] American Medical Association. Trends in health care spending. Chicago, IL: American Medical Association;
2023.
[4] Holster T, Ji SX, Marttinen P.Risk adjustment forregional healthcarefunding allocations with ensemble meth-
2024;25(7):1117–1131.
ods: an empirical study and interpretation. Eur J Health Econ. doi: 10.1007/s10198-023-
01656-w.
[5] Henley SS, Golden RM, Kashner TM. Statistical modeling methods: challenges and strategies. Biostat
2020;4(1):105–139.doi:
| Epidemiol. |     | 10.1080/24709360.2019.1618653. |
| ---------- | --- | ------------------------------ |
Rahnenfu€hrer
[6] J, De Bin R, Benner A, et al. Statistical analysis of high-dimensional biomedical data: a gentle
introduction to analytical goals, common approaches and challenges. BMC Med. 2023;21(1):182. doi: 10.1186/
s12916-023-02858-y.
2019;25(1):24–
[7] Esteva A, Robicquet A, Ramsundar B, et al. A guide to deep learning in healthcare. Nat Med.
29. doi:10.1038/s41591-018-0316-z.
[8] Miotto R, Wang F, Wang S, et al. Deep learning for healthcare: review, opportunities and challenges. Briefings
Bioinformat.2018;19(6):1236–1246.
doi: 10.1093/bib/bbx044.
[9] LeCunY, BengioY, Hinton G.Deeplearning.Nature.2015;521(7553):436–444.doi: 10.1038/nature14539.
[10] Drewe-Boss P, Enders D, Walker J, et al. Deep learning for prediction of population health costs. BMC Med
| Inform DecisMak. | 2022;22(1):32.doi: | 10.1186/s12911-021-01743-z. |
| ---------------- | ------------------ | --------------------------- |
[11] Topol EJ. High-performance medicine: the convergence of human and artificial intelligence. Nat Med. 2019;
| 25(1):44–56.doi: | 10.1038/s41591-018-0300-7. |     |
| ---------------- | -------------------------- | --- |
[12] Liu X, Faes L, Kale AU, et al. A comparison of deep learning performance against health-care professionals in
detecting diseases from medical imaging: a systematic review and meta-analysis. Lancet Digit Health. 2019;
| 1(6):e271–e297. | doi: 10.1016/S2589-7500(19)30123-2. |     |
| --------------- | ----------------------------------- | --- |
[13] He J, Baxter SL, Xu J, et al. The practical implementation of artificial intelligence technologies in medicine.
Med.2019;25(1):30–36.
| Nat | doi: 10.1038/s41591-018-0307-0. |     |
| --- | ------------------------------- | --- |
[14] Amiri MM, et al. Systematic review of factors determining health care expenditures. Health Policy Technol.
2021;10(2):100498.
[15] Ke X, Saksena P, Holly A. The determinants of health expenditure: a country-level panel data analysis.
| Geneva: WorldHealthOrganization; |     | 2011. p.1–28. |
| -------------------------------- | --- | ------------- |
[16] Page MJ, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ.
2021;372:n71.
[17] Lewis M, Elad G, Beladev M, et al. Comparison of deep learning with traditional models to predict prevent-
able acutecare use andspendingamong heartfailure patients.Sci Rep.2021;11(1):1164.doi: 10.1038/s41598-
020-80856-3.

JOURNALOFMEDICALECONOMICS 671
[18] Kaushik S, et al. Ensemble of multi-headed machine learning architectures for time-series forecasting of
healthcare expenditures. In: Applications of machine learning. Singapore: Springer; 2020. p. 199–216. doi: 10.
1007/978-981-15-3357-0_14.
[19] Yu K, Yang Z, Wu C, et al. In-hospital resource utilization prediction from electronic medical records with
deep learning.Knowl BasedSyst.2021;223:107052. doi:10.1016/j.knosys.2021.107052.
[20] Yang C, Delcher C, Shenkman E, et al. Machine learningapproachesfor predictinghighcosthighneed patient
expendituresinhealthcare.BiomedEngOnline.2018;17(Suppl1):131.doi:10.1186/s12938-018-0568-3.
[21] Vimont A, Leleu H, Durand-Zaleski I. Machine learning versus regression modelling in predicting individual
healthcare costs from a representative sample of the nationwide claims database in France. Eur J Health
Econ.2022;23(2):211–223.doi: 10.1007/s10198-021-01363-4.
[22] Kaushik S, Choudhury A, Natarajan S, et al. Medicine expenditure prediction via a variance-based generative
adversarialnetwork. IEEEAccess.2020;8:110947–110958. doi:10.1109/access.2020.3002346.
[23] Kaushik S, et al. Using LSTMs for predicting patient’s expenditure on medications. In: 2017 International
Conferenceon MachineLearning andDataScience (MLDS).IEEE;2017. doi:10.1109/MLDS.2017.9.
[24] Laqtib S, Yassini KE, Hasnaoui ML. A deep learning methods for intrusion detection systems based machine
learning inMANET.Proceedings ofthe4thInternational ConferenceonSmart CityApplications; 2019.
[25] Teles AS, de Moura IR, Silva F, et al. EHR-based prediction modelling meets multimodal deep learning: a sys-
tematic review of structured and textual data fusion methods. Information Fusion. 2025;118:102981. doi: 10.
1016/j.inffus.2025.102981.
[26] Smith J. Predictive analytics in healthcare: powering proactive patient care in the era of value-based care;
2025.
[27] Hassija V, Chamola V, Mahapatra A, et al. Interpreting black-box models: a review on explainable artificial
intelligence.Cogn Comput. 2024;16(1):45–74. doi: 10.1007/s12559-023-10179-8.
[28] Sendak MP, et al. A path for translation of machine learning products into healthcare delivery. EMJ Innov.
2020;10:19–00172.
[29] Obermeyer Z, Emanuel EJ. Predicting the future—big data, machine learning, and clinical medicine. N Engl J
Med. 2016;375(13):1216–1219.doi: 10.1056/NEJMp1606181.
[30] Bodha S. A comparative study of machine learning and deep learning models for predicting medical insur-
ancecosts withexplainable AI; 2025.
[31] Sohn JH, Chen Y, Lituiev D, et al. Prediction of future healthcare expenses of patients from chest radiographs
usingdeep learning: apilotstudy. Sci Rep.2022;12(1):8344.doi: 10.1038/s41598-022-12551-4.
[32] Futoma J, Simons M, Panch T, et al. The myth of generalisability in clinical research and machine learning in
healthcare. Lancet DigitHealth. 2020;2(9):e489–e492. doi:10.1016/S2589-7500(20)30186-2.
[33] Tan M, Hatef E, Taghipour D, et al. Including social and behavioral determinants in predictive models: trends,
challenges,andopportunities. JMIR Med Inform.2020;8(9):e18084. doi: 10.2196/18084.
[34] Yoon CH, Torrance R, Scheinerman N. Machine learning in medicine: should the pursuit of enhanced inter-
pretabilitybe abandoned? JMed Ethics. 2022;48(9):581–585.doi: 10.1136/medethics-2020-107102.
[35] De Bock KW, Coussement K, Caigny AD, et al. Explainable AI for operational research: a defining framework,
methods, applications, and a research agenda. Eur J Oper Res. 2024;317(2):249–272. doi: 10.1016/j.ejor.2023.
09.026.
[36] Vasey B, Nagendran M, Campbell B, et al. Reporting guideline for the early stage clinical evaluation of deci-
sion support systems driven by artificial intelligence: DECIDE-AI. BMJ. 2022;377:e070904. doi: 10.1136/bmj-
2022-070904.
[37] Collins GS, Reitsma JB, Altman DG, et al. Transparent reporting of a multivariable prediction model for indi-
vidual prognosis or diagnosis (TRIPOD): the TRIPOD statement. Br J Surg. 2015;102(3):148–158. doi: 10.1002/
bjs.9736.
[38] Steyerberg EW, Vickers AJ, Cook NR, et al. Assessing the performance of prediction models: a framework for
traditional andnovelmeasures. Epidemiology.2010;21(1):128–138.doi: 10.1097/EDE.0b013e3181c30fb2.
[39] Choi E, et al. Doctor AI: predicting clinical events via recurrent neural networks. In: Machine Learning for
Healthcare Conference.PMLR;2016.
[40] RasmyL,WuY,WangN,etal.Astudyofgeneralizabilityofrecurrentneuralnetwork-basedpredictivemodels
for heart failure onset risk using a large and heterogeneous EHR data set. J Biomed Inform. 2018;84:11–16.
doi: 10.1016/j.jbi.2018.06.011.
[41] Kaissis GA, Makowski MR, Ru€ckert D, et al. Secure, privacy-preserving andfederated machine learning inmed-
icalimaging. NatMach Intell.2020;2(6):305–311.doi:10.1038/s42256-020-0186-1.
[42] Wilkinson MD, Dumontier M, Aalbersberg IJ, et al. The FAIR guiding principles for scientific data management
andstewardship. Sci Data.2016;3(1):1–9.doi: 10.1038/sdata.2016.18.
[43] Lee NS, Whitman N, Vakharia N, et al. High-cost patients: hot-spotters don’t explain the half of it. J Gen
InternMed. 2017;32(1):28–34. doi:10.1007/s11606-016-3790-3.
[44] Rajkomar A, Hardt M, Howell MD, et al. Ensuring fairness in machine learning to advance health equity. Ann
InternMed. 2018;169(12):866–872.doi: 10.7326/M18-1990.