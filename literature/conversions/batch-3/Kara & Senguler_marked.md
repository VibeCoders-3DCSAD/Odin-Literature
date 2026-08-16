---
conversion_metadata:
  converted_at: "2026-07-21T13:41:00Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Kara & Senguler.pdf"
  source_pdf_sha256: "ee3a1f3befa3833b065b162fb84f3c6b4b6c9beaa00438226ad2e67f9c5cf80f"
  page_count: 18
  markdown_char_count: 196389
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Public Budgeting & Finance

ORIGINAL ARTICLE

A Comparative Analysis of Budget Forecasting
Methods: A Systematic Literature Review Covering
the 1983–2024 Period

Berat Kara

| Hasan Şengüler

Faculty of Political Science, Istanbul Medeniyet University, Istanbul, Turkey

Correspondence: Berat Kara (berat.kara@medeniyet.edu.tr)

Received: 11 September 2025 | Revised: 18 October 2025 | Accepted: 27 October 2025

Keywords: budget forecasting | machine learning | method comparison | performance metrics | systematic review

ABSTRACT
This study systematically analyzes 69 peer‐reviewed works comparing budget forecasting methods. It explores methodological
evolution, geographic distribution, and evaluation trends. Four phases of development are identified: statistical methods,
diversification, machine learning, and deep learning. A division emerges between traditional and next‐generation techniques.
Geographically, 43% of studies focus on the United States, while developing economies remain underrepresented. In evaluation,
MAPE, RMSE, and MAE dominate, with directional errors largely neglected. Findings show that optimal method choice
depends on context, supporting a pluralistic, context‐sensitive approach rather than universal reliance on a single forecasting
method.

1 |

Introduction

Public budgets, which lie at the core of fiscal management
systems, function both as instruments of economic policy and
as frameworks for managing public resources. The forecasts
used in budget preparation determine the government's future
fiscal capacity, spending priorities, and economic orientation.
The forecasting process is shaped by a wide range of factors,
including macroeconomic indicators, political preferences,
institutional capacity, and technical methodologies. In this
respect, budget forecasts go beyond being a merely technical
element of fiscal planning, constituting a strategic component of
the policy‐making process.

This strategic position necessitates that budget forecasts be
prepared in a realistic, reliable, and accurate manner. Efficient
allocation of scarce public resources and the successful coor-
dination of public–private sector planning are only possible
forecasts
through a budget process grounded in robust
(Krause and Corder 2007). Similarly, the timely and effective

implementation of fiscal policy measures (Botrić and Vizek
2012) and the design and execution of sound fiscal policies
(Derrick 2002; Danninger 2005) depend critically on the
accuracy of forecasts. Moreover, forecasts serve as key in-
dicators for economic agents: various financial
indicators,
particularly interest rates, are influenced by these forecasts;
households and financial market participants base their long‐
term decisions on them; and central banks that pursue
inflation targeting rely on such data to guide their policy
decisions.

Accurate forecasts serve as a fundamental tool for determining
the extent to which public services and programs can be
financed (Auld 1970; Bretschneider et al. 1989). The success of
forecasting is particularly critical for the efficient financing of
large future public expenditures (Auld 1970), as multiyear ex-
penditure forecasts represent an estimate of the cost of pro-
viding a certain level of public service (Schroeder 2007).
Furthermore, establishing a robust link between long‐term
planning and implementation depends on the accuracy of

© 2025 Public Financial Publications, Inc.

Public Budgeting & Finance, 2025; 1–18
https://doi.org/10.1111/pbaf.70008

1

---

<!-- PAGE 2 -->

Summary
• This study provides a systematic analysis of 69 peer‐
reviewed studies comparing budget forecasting meth-
ods, identifying four distinct phases of methodological
evolution from basic statistical models to the deep
learning era.

• The findings reveal that no single forecasting method is
universally superior; instead, the optimal choice criti-
cally depends on contextual factors such as the eco-
nomic environment, data quality, and the forecast
horizon.

• A significant finding is the pronounced geographical
concentration of research, with 43% of studies focused on
the United States, leaving forecasting methodologies in
developing economies substantially underrepresented.
• The field is further characterized by a hegemony of
certain performance metrics (MAPE, RMSE, and MAE),
which, while allowing for comparison, largely neglect
the critical policy dimension of directional
forecast
errors.

• Consequently, the study advocates for a shift away from
the quest for a single best model toward a more plu-
ralistic,
potentially hybrid
approach to budget forecasting.

context‐sensitive,

and

medium‐ and long‐term forecasts (Asher 1978; Jena 2006;
Zakaria and Ali 2010; Fedotov 2017). Having sufficient infor-
mation about available resources enables more effective man-
agement of long‐term programs and projects within the budget
process, while careful evaluation of this information guides
project and program selection, helping to determine what is
feasible in the medium term (Jena 2006). In this context, fore-
casts related to a country's key sectors provide a scientific
foundation for strategic planning (Fedotov 2017).

The realistic preparation of budget forecasts is also a critical
prerequisite for the government to achieve its planned objec-
tives (Khan and Anwar Hussain 2018; Bretschneider and Gorr
1992; Agostini 1991). As observed in modern economies, a
government's ability to respond effectively to any crisis is
directly influenced by the quality of the financial information
available to it, and consequently, by the accuracy of forecasts
(Willoughby and Guo 2008). In other words, the success of
forecasting shapes public perception regarding the effective-
ness of a government's fiscal policy (Leal et al. 2008). There-
fore, major errors in budget forecasting negatively affect the
outcomes of governmental programs and policies, potentially
leading to policy failure (Srinivasan and Misra 2020).
Accordingly, it can be argued that forecast accuracy plays a
significant role in the budgetary policy process by contributing
to transparency, accountability, and fiscal discipline (McNab
et al. 2005).

As a natural consequence of this strategic importance, efforts to
enhance the accuracy of budget forecasts have remained a
continuous focus in the field of public finance. Two principal

approaches emerge in this regard. The first involves identifying
the causes of past forecasting errors and developing remedial
mechanisms. This approach aims to eliminate recurring error
patterns by examining in detail the structural, institutional,
economic, and political
factors influencing the forecasting
process. The second approach focuses on improving the meth-
ods and models used in the preparation of forecasts. Such
methodological advancement encompasses both the refinement
of existing techniques and the implementation of new modeling
approaches, with the goal of strengthening the analytical
capacity of the forecasting process.

The literature contains numerous studies that focus on these two
approaches. These studies have compared the performance of
various forecasting techniques across different country contexts
and datasets. The models employed range widely, from simple
time‐series methods based on trend analysis to complex econo-
metric models, and from deterministic approaches to artificial
intelligence (AI) and machine learning (ML)‐based algorithms.
While simpler methods offer advantages such as ease of imple-
mentation and low data requirements, more complex techniques,
despite requiring greater computational power and extensive
data sources, possess the potential to capture dynamic relation-
ships. This diversity indicates that there is no single “ideal”
method for budget forecasting; rather, the choice of method
depends on factors such as economic conditions, data quality,
institutional capacity, and policy priorities.

The existing literature does not provide a homogeneous
assessment of the success of methods used in budget forecast-
ing, due to variations in datasets, time periods, countries, and
model types. Forecasts produced across a broad spectrum, from
simple time‐series techniques to complex ML approaches, ex-
hibit varying performance in different contexts. This situation
necessitates a systematic evaluation of which methods perform
better under specific conditions. Such an assessment would not
only contribute to the advancement of academic knowledge but
also serve as a practical guide for institutions, policymakers,
and analysts involved in the budget process regarding method
selection and model development. In response to this need, the
present study offers a comprehensive review of the existing
literature, providing a comparative evaluation of different
models and techniques.

The critical need for advancing budget forecasting accuracy is
further underscored by recent large‐scale efforts to define the
research priorities for the entire field of public budgeting and
finance. In a comprehensive agenda‐setting study, McDonald
et al. (2024) engaged a wide community of academics and
practitioners to identify the most pressing research needs.
Notably, their findings, derived from a ranked‐choice voting
process, highlighted “Data and Methods” as a top‐tier priority,
explicitly calling for research that improves “the accuracy of
budget and revenue forecasting.” This consensus positions
methodological investigations, such as the present study, at the
forefront of the field's agenda. Our systematic review directly
addresses this call by synthesizing the comparative performance
of a wide array of forecasting techniques over a four‐decade
period. By doing so, this study aims not only to contribute to
academic knowledge but also to provide a practical, evidence‐
based guide for practitioners in selecting and developing

2

Public Budgeting & Finance, 2025

---

<!-- PAGE 3 -->

forecasting models, thereby bridging the gap between academic
inquiry and the operational needs identified by the community
of practice.

The paper is structured as follows. First, the dataset used in the
analysis is introduced, detailing its scope, coverage, and key
characteristics. Second, the methodology is explained. Third,
the state of the literature on budget forecasting methods is ex-
amined, with a focus on comparative findings and methodo-
logical diversity. Finally, the conclusion section summarizes the
main findings and outlines implications for future research and
policy design.

instance, various variants of artificial neural networks (ANNs),
even when labeled with different prefixes in the original studies,
were grouped under the ANN category in the dataset. This
standardization enables accurate and meaningful comparisons
across methods.

The primary motivation for constructing this dataset is to en-
able an objective evaluation of the comparative performance of
budget forecasting methods and to conduct a systematic anal-
ysis of findings in the literature. In this way, the study aims to
provide clearer and more reliable insights into the conditions
under which different methods yield superior results, both for
the academic community and for practical applications.

2 | Data Set

The dataset constructed in this study encompasses the academic
literature in which budget
forecasting methods have been
comparatively evaluated. In creating the dataset, a series of
selection criteria was established to clearly define the scope and
ensure comparability. First, only articles published in peer‐
reviewed journals, books, book chapters, and scientific confer-
ence proceedings were included. This choice aims to ensure
that the methods employed and the results obtained have been
scrutinized according to academic standards and are highly
reliable. Reports, technical notes, or institutional assessments
that have not undergone a peer‐review process were excluded
from the dataset.

Second, since the focus of this study is on method comparison,
budget forecasting studies that employ only a single method
were not included. The dataset consists of research in which
multiple forecasting methods were applied within the same
study and their performance compared. This approach allows
for the direct observation and analysis of performance differ-
ences across methods.

Third, it was not sufficient for the included studies to provide
only forward‐looking forecasts; these forecasts were required to
be compared with actual outcomes for the corresponding peri-
ods. Studies that did not perform such comparisons were ex-
they could not objectively
cluded from the dataset, as
the forecasting methods. This
demonstrate the success of
requirement is critical for ensuring a robust assessment of
methodological performance, which constitutes the primary
motivation of the study.

In some studies, forecasts cover both past periods, for which
actual outcomes are available, and future periods, which have
not yet occurred. In such cases, only the periods with available
actual data were included in the dataset. For example, in a
study with a 10‐year forecasting horizon where actual outcomes
are available for only the first five years, the dataset represents
only the five‐year segment. This approach ensures that method
performance is measured solely over verifiable periods.

Finally,
terminological consistency was maintained in the
naming of methods within the study. In different studies, minor
variations in model structure or configuration often led to the
same method being referred to by different names; in the da-
taset, these were consolidated under a single heading. For

3 | Methods

or

journal

collaborations,

co‐authorship

The purpose of this study is to examine the distribution, tem-
poral trends, and interrelationships of methods and metrics
employed in the budget forecasting literature. While classical
bibliometric analyses are typically conducted through citation
co‐
networks,
occurrence mapping (Passas 2024), this study adopts a different
perspective. Instead of focusing on citation relationships or
collaborative networks, the analysis emphasizes the frequency
of method applications, the prevalence of metric preferences,
the characteristics of training datasets, the length of forecasting
horizons, and the interconnections among methods. Thus,
although the research shares certain features with biblio-
metrics, it is primarily designed within the framework of sta-
tistical analysis and network analysis. The analytical process
consists of three stages: (i) descriptive statistical analysis, (ii)
trend analysis, and (iii) network analysis.

3.1 | Descriptive Statistical Analysis

Descriptive statistical analysis aims to summarize the funda-
mental characteristics of collected data and provide an overall
framework for the research field (Cooksey 2020). Such analyses
are frequently used in bibliometric studies to reveal the quan-
titative structure of the literature (Castelino et al. 2024). In this
study, descriptive analyses include the frequency of method
applications, the annual distribution of publications, the geo-
graphical (country‐level) distribution of research, the extent of
metric preferences, and the length of forecasting horizons. The
findings are visualized through graphs, offering a general
overview of methodological diversity in the literature.

3.2 | Trend Analysis

Trend analysis is a method used to examine temporal changes
in a given phenomenon and to identify underlying patterns. It is
frequently employed to illustrate the evolution of research
thereby con-
domains and methodological
tributing to the understanding of the developmental trajectory
of a field (Li 2025). In this study, trend analysis was conducted
to investigate the intensity of method applications over time.
The results were visualized with line graphs, highlighting
methods that gained prominence during different periods.

transformations,

Public Budgeting & Finance, 2025

3

---

<!-- PAGE 4 -->

3.3 | Network Analysis

represent

Network analysis is a powerful method for examining structures
composed of nodes (e.g., methods, authors, or metrics) and
edges that
the connections among them. This
approach is widely used to investigate the structural char-
acteristics and methodological diversity of scientific domains
(Campbell et al. 2024), offering valuable insights into the in-
teractions among different components of the literature.

In this study, network analysis was performed using Gephi
software,
resulting in three distinct network structures:
method–method, method–year, and method–metric relation-
ships. Nodes represented methods, years, and metrics, while
edges denoted their co‐occurrences. This analysis enabled the
visualization of which methods were prominent in specific
periods, which metrics they were evaluated with, and which
methods tended to be employed jointly.

4 | Results

The table below provides a comprehensive summary of em-
pirical studies on budget forecasting methods. It systematically
classifies results based on different country contexts, data fre-
quencies, time periods, and types of methods, thereby high-
lighting the relative performance of various approaches. In this
way, the fragmented findings in the literature regarding the
success of budget forecasting methods can be evaluated from a
holistic perspective, allowing for a comparative assessment of
which methods perform better or worse under specific condi-
tions. Within this framework, the table not only serves as an
inventory of previous research but also makes methodological
diversity and performance differences, central to the motivation
of this paper, explicit, laying the groundwork for subsequent
analyses.

Academic interest in the comparative performance of budget
forecasting methods has shown a steady and remarkable
increase over the past four decades. The reviewed literature
reveals not only a numerical growth in studies but also a sig-
nificant evolution in terms of scope, methodology, and geo-
graphical diversity. Early contributions (e.g., Downs and Rocke
1983; Litterman and Thomas 1983) were largely confined to
advanced economies (particularly the United States) and relied
primarily on relatively simple time‐series models (ARMA and
ARIMA). Over time, however, research has expanded to include
developing countries as well as far more complex econometric
and AI‐based models. This expansion is a clear indication that
the pursuit of greater forecasting accuracy has taken on a global
and interdisciplinary character. Table 1 provides a systematic
summary of this rich and dynamic body of work, detailing the
scope, methods, and key findings of the 68 comparative studies
that form the basis of the present analysis.

From a methodological perspective, the literature exhibits a
clear trend toward increasing complexity and diversity. While
the 1980s and early 1990s were dominated by classical econo-
metric approaches such as ARIMA, VAR, and ECM, the 2000s
marked the entry of ML and deep learning (DL) algorithms into
the field. ANN, SVM, and, more recently, cutting‐edge methods

such as LSTM networks and XGBoost have been incorporated
into the forecasters' toolkit (e.g., Yang et al. 2023; M. Khalifa
et al. 2024). At the same time, hybrid models and innovative
approaches such as MIDAS, which address the issue of fre-
quency mismatch (Ghysels and Ozkan 2012, 2015), have gained
prominence in performance comparisons. This evolution dem-
onstrates that researchers have not only sought to improve
traditional methods but have also pushed the boundaries of
forecasting accuracy by leveraging data abundance and ad-
vances in computational power.

The expansion in geographical coverage is also noteworthy.
Whereas early studies were almost entirely United States‐
centered, recent years have witnessed significant contributions
from a wide range of economies, including China, Turkey,
Brazil, South Africa, India, and numerous Eastern European
countries, as illustrated in Table 1. This diffusion underscores
that budget forecasting is a universal issue in public finance and
highlights that method performance may vary across different
economic structures, institutional arrangements, and levels of
data quality.

Therefore, the findings in the literature are not homogeneous; a
method that delivers the “best” performance in one country or
period may yield only modest results in another context. This
heterogeneity further underscores the need for a systematic
assessment of which methods perform better under specific
conditions and reinforces the primary motivation of this study.

First, the distribution and frequency of forecasting methods
employed in the comparative studies under review were ana-
lyzed over time. This analysis provides an objective lens
through which to observe the evolution of methodological
trends, technological capabilities, and academic interest in the
budget forecasting literature. Such a historical perspective is
crucial for understanding which methods dominated in partic-
ular periods, how the popularity of specific models has shifted,
and when pioneering contributions introduced innovations to
the field.

The analysis of Figure 1 demonstrates that the methodological
trajectory of the budget forecasting literature can be characterized
as a four‐stage evolution. The first stage, emerging in the 1980s,
was dominated by basic statistical methods. During this period,
traditional time series and econometric models such as ARIMA,
VAR, and various regression techniques constituted the main
focus of academic studies. In subsequent years, greater diversifi-
cation and sophistication in modeling techniques became evident,
with more complex and theoretically grounded approaches such
as BVAR, ECM, and MIDAS being introduced. This phase marked
a period in which researchers sought to enhance forecasting power
by making model structures more dynamic and by integrating
different types of data. By the 2010s, a notable methodological shift
had occurred: ML algorithms such as ANN and SVM began to
feature regularly in the literature, bringing an interdisciplinary
dimension to the field. This transition was driven by the growing
availability of large datasets, advances in computational capacity,
and increasing interest
in modeling nonlinear relationships.
Finally, since the 2020s, the literature has entered the era of DL
and hybrid models. Cutting‐edge algorithms such as LSTM and
XGBoost have become frequently tested in comparative analyses.

4

Public Budgeting & Finance, 2025

---

<!-- PAGE 5 -->

E
S
M
R

;

E
A
M

;

E
M

R
A
V

A
M
I
R
A

C
F
O

;

M
C
E

;

R
A
V

;

A
M
I
R
A

7
8
9
1
–
0
8
9
1

y
l
r
e
t
r
a
u
Q

9
7
9
1
–
5
5
9
1

0
0
1

A
S
U

)
s
(
c
i
r
t
e
M

e
n
o
N

E
P

;

E
A
M

E
S
M
R

E
P

E
S
M

E
M

;

E
A
M

;

E
S
M
R

t
s
r
o
W

W
R

C
F
O

R
G
R

R
A
V

t
f
i
r
D

R
G
R

E
P

;

E
P
A

;

E
P
A
M

;

E
S
M
R

C
F
O

E
P

;

E
S
M
R

E
P
A
M

A
M
I
R
A

t
i
F
e
v
r
u
C

t
s
e
B

A
M
R
A

F
O
C

A
M
R
A

A
M
I
R
A

F
O
C

A
M
I
R
A

F
O
C

A
M

W
H

R
G
R

;

A
M
R
A

R
A
V

;

A
M
I
R
A

F
O
C

;
t
f
i
r
D

;

A
M
I
R
A

A
M
I
R
A

;

R
G
R

C
F
O

;

F
O
C

;

A
M
I
R
A

t
i
F
e
v
r
u
C

;

A
M
I
R
A

;

W
H

;
S
E

;

A
M

C
F
O

;

F
O
C

;

F
A
G

;

W
H

;
S
E

;

A
M

3
8
9
1
–
1
8
9
1

4
8
9
1
–
3
8
9
1

3
8
9
1
–
0
8
9
1

2
8
9
1
–
1
8
9
1

5
8
9
1
–
2
8
9
1

6
8
9
1

8
8
9
1

y
l
r
e
t
r
a
u
Q

y
l
h
t
n
o
M

l
a
u
n
n
A

y
l
r
e
t
r
a
u
Q

y
l
r
e
t
r
a
u
Q

y
l
h
t
n
o
M

y
l
h
t
n
o
M

0
8
9
1
–
0
7
9
1

4
8
9
1
–
0
7
9
1

0
8
9
1
–
4
7
9
1

0
8
9
1
–
0
7
9
1

1
8
9
1
–
8
7
9
1

5
8
9
1
–
2
8
9
1

7
8
9
1
–
3
8
9
1

4
4

6
5
1

2
6
4

4
4

6
1

8
4

0
6

W
R

;

A
M

;

A
M
R
A

C
F
O

;

F
O
C

;

R
A
V

9
7
9
1
−
6
4
9
1

2
8
9
1
–
1
7
9
1

l
a
u
n
n
A

y
l
r
e
t
r
a
u
Q

8
7
9
1
–
6
4
9
1

2
8
9
1
−
7
6
9
1

1
6

4
6

A
S
U

A
S
U

A
S
U

A
S
U

A
S
U

A
S
U

A
S
U

A
S
U

A
S
U

)
3
8
9
1
(

e
k
c
o
R

d
n
a

s
n
w
o
D

d
n
a

n
a
m
r
e
t
t
i
L

)
3
8
9
1
(

s
a
m
o
h
T

)
5
8
9
1
(

g
n
o
W
d
n
a

s
e
n
n
i
e
t
S

)
5
8
9
1
(

e
n
a
J

d
n
a

i

m
z
a
N

)
7
8
9
1
(

n
o
t
x
e
S

)
8
8
9
1
(

d
l
o
h
t
u
e
L

d
n
a

i

m
z
a
N

)
9
8
9
1
(

n
o
t
r
e
l
l

u
F

)
0
9
9
1
(

k
n
a
r
F

)
0
9
9
1
(

s
o
m

i
s
a
r
e
G
d
n
a
k
n
a
r
F

s
d
o
h
t
e
M

.
r
e
p

.
r
o
F

.

q
e
r
f

.
s
b
O

R
Y
T

O
T

y
r
t
n
u
o
C

)
s
(
r
o
h
t
u
A

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

t
e
g
d
u
b

n

i

s
l
e
d
o
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
c

e
h
t

n
o
w
e
i
v
e
r

e
r
u
t
a
r
e
t
i
L

|

1

E
L
B
A
T

E
P
M

;

E
P
A
M

E
P
A
M

E
P
A
M

E
P
A
M

E
A
M

;

E
S
M
R

E
P
A
M

F
K
S
M

W
H

R
G
R

A
M

C
F
O

A
M

R
A
V
B

S
E

t
i
F
e
v
r
u
C

C
F
O

;

R
A
V
B

;

R
G
R

;

A
M
I
R
A

;
S
E

;

A
M

F
K
S
M
C

‐

A
M
I
R
A

;
S
E

;

W
H

;

A
M

;

R
G
R

;

F
A
G

;

A
M
I
R
A

0
9
9
1

F
K
S
M
C

‐

;

F
K
S
M

6
8
9
1
–
9
7
9
1

l
a
u
n
n
A

y
l
h
t
n
o
M

6
8
9
1
–
2
7
9
1

0
9
9
1
–
3
8
9
1

S
E

;
S
E

;

R
G
R

t
i
F
e
v
r
u
C

;

R
G
R

;
S
E

;

n
a
e
M

;

A
M

;

F
C
O
L

2
9
9
1
–
0
9
9
1

5
8
9
1
–
0
8
9
1

l
a
u
n
n
A

l
a
u
n
n
A

2
9
9
1
–
5
7
9
1

5
8
9
1
–
5
7
9
1

E
A
M

;

E
S
M
R

M
C
M

;

R
A
V

A
M
R
A

F
O
C

;

M
C
M

;

M
C
S

;

R
A
V

;

A
M
R
A

E
P

E
P
A
M

E
S
M
R

E
P
A
M

N
N
A

n
a
e
M

W
R

M
C
E

C
F
O

;

N
N
A

C
F
O

;

N
N
A

R
G
R

F
O
C

R
G
R

n
a
e
M

;
t
f
i
r
D

;

T
R
L

;

R
G
R

;

C
F
O

C
F
O

;

W
R

;

F
O
C

;

R
G
R

M
C
E

;

R
G
R

7
9
9
1
–
0
9
9
1

6
9
9
1
–
5
9
9
1

2
0
0
2
–
6
9
9
1

0
0
0
2
–
5
9
9
1

1
0
0
2
–
5
9
9
1

3
0
0
2
–
4
9
9
1

5
0
0
2
–
3
0
0
2

y
l
r
e
t
r
a
u
Q

n
o
M

,
a
u
Q

l
a
u
n
n
a
i
B

y
l
r
e
t
r
a
u
Q

l
a
u
n
n
A

y
l
r
e
t
r
a
u
Q

y
l
r
e
t
r
a
u
Q

7
9
9
1
–
3
8
9
1

6
9
9
1
–
0
9
9
1

5
9
9
1
–
1
8
9
1

0
0
0
2
–
5
7
9
1

1
0
0
2
–
5
8
9
1

3
0
0
2
–
0
7
9
1

5
0
0
2
–
8
9
9
1

0
0
6

2
7

8
1

0
0
7

8
5

9
9

0
3

4
0
1

7
1

6
3
1

8
2

A
S
U

A
S
U

A
S
U

A
S
U

A
S
U

A
S
U

l
e
n
a
P

A
S
U

A
S
U

l
e
n
a
P

a
i
n
a
u
h
t
i
L

)
3
9
9
1
(

.
l
a

t
e

n
a
c
n
u
D

d
n
a

i

n
a
t
s
e
h
g
a
B

)
2
9
9
1
(

n
w
o
N
c
M

)
3
9
9
1
(

d
r
a
w
o
H

d
n
a

s
i
k
a
n
a
i
G

)
4
9
9
1
(

g
n
a
W
d
n
a

k
n
a
r
F

)
4
9
9
1
(

y
a
l
K
d
n
a

e
l
z
z
i
r
G

)
7
9
9
1
(

s
e
l
r
a
h
C
d
n
a

k
o
r
t
O

)
9
9
9
1
(

.
l
a

t
e

e
n
o
i
c
n
i
r
i
C

)
5
0
0
2
(

o
n

i
l
l
e
c
r
a
M

d
n
a

o
r
e
v
a
F

)
6
0
0
2
(

s
e
e
h
r
o
o
V

)
7
0
0
2
(

)
7
0
0
2
(

g
n
o
K

)
7
0
0
2
(

z
e
r
é
P

d
n
a

s
i
k
z
d
u
R

ė

t
y
t
i
a
l
u
i

č
a
M

)
s
e
u
n
i
t
n
o
C
(

;

E
S
M
R

E
P
A
M

;

E
A
M

E
P

E
P
A
M

C
F
O

A
M
I
R
A

C
F
O

;

A
M
I
R
A

4
0
0
2
–
2
0
0
2

y
l
h
t
n
o
M

4
0
0
2
–
6
9
9
1

8
0
1

e
c
n
a
r
F

)
8
0
0
2
(

.
l
a

t
e

i

n
i
r
t
s
e
v
l
i
S

C
F
O

N
N
A

A
M
I
R
A

M
V
S

C
F
O

;

A
M
I
R
A

M
G

;

M
V
S

;

N
N
A

6
0
0
2
–
9
7
9
1

1
0
0
2
–
9
9
9
1

l
a
u
n
n
A

l
a
u
n
n
A

6
0
0
2
–
5
4
9
1

8
9
9
1
–
0
9
9
1

2
6

9

d
n
a
l
r
e
z
t
i

w
S

)
2
1
0
2
(

l
e
u
g
o
S

d
n
a

y
n
g
a
t
a
h
C

i

a
n
h
C

)
9
0
0
2
(

.
l
a

t
e

u
L

Public Budgeting & Finance, 2025

5

---

<!-- PAGE 6 -->

E
S
A
M

;

E
P
M

;

E
S
M
R

E
P
A
M

;

E
A
M

;

E
S
M
R

E
P
A
M

;

E
A
M

)
s
(
c
i
r
t
e
M

E
S
M
R

t
s
r
o
W

W
R

E
P
A
M

A
M
I
R
A

E
S
R
R

;

E
A
R

E
S
M
R

M
D

;

E
S
M
R

E
A
M

;

E
S
M
R

E
P
A
M

E
P
A
M

E
P
A
M

E
S
M
R

E
P
M

;

E
P
A
M

E
S
M
R

R
G
R

W
R

W
R

t
f
i
r
D

S
E

N
N
A

t
s
e
B

X
I
M

M
C
E

M
V
S

R
A
V
B

X
I
M

F
O
C

F
O
C

M
V
S

s
d
o
h
t
e
M

W
R

;

X
I
M

A
M
I
R
A

;

M
C
E

;

R
G
R

;

M
V
S

;

N
N
A

W
R

;

R
A
V
B

;

R
A
V

W
R

;

M
C
E

;

X
I
M

;

R
A

C
F
O

;
t
f
i
r
D

;

F
O
C

;

W
H

;

A
M
I
R
A

F
O
C

;
S
E

;

M
G

M
V
S

;

N
N
A

R
G
R

;

A
M
I
R
A

M
C
E

;

W
R

M
C
E

;

R
G
R

;

A
M
I
R
A

;

W
R

;
t
f
i
r
D

R
A

W
H

n
a
e
M

S
A
D
M

I

F
O
C

;

L
D
A

;

R
A

;
S
A
D
M

I

A
M
I
R
A
S

t
f
i
r
D

;

A
M
I
R
A
S

;

R
G
R

;

W
H

S
A
D
M

I

C
F
O

;

n
a
e
M

;
S
A
D
M

I

E
P
A
M

;

E
S
M

;

E
P
M

A
M
I
R
A
S

A
M
S
W
H

;

A
M
S
W
H

;

A
M
I
R
A
S

E
P
S
M

;

E
P
A
M

A
M
R
A

E
M
R

;

E
S
M
R

E
S
M
R

C
F
O

R
A

N
N
A

M
V
S

M
V
S

;

A
M
R
A

;

N
N
A

C
F
O

;

M
V
S

S
A
D
M

I

F
O
C

;

L
D
A

;

R
A

;
S
A
D
M

I

E
S
M
R

E
A
M

;

E
S
M
R

e
n
o
N

A
M

E
S
M
R

;

E
A
M

;

E
M

X
A
M
I
R
A

;

E
A
M

;

E
S
M
R

;

E
M

A
M
I
R
A
S

E
R

;

E
P
A
M

C
F
O

e
n
o
N

F
O
C

R
A
V
B

F
O
C

W
H

C
F
O

;

A
A
S
W
H

N
N
A

A
M

;

H
C
R
A
G

;

F
O
C

;

A
M
R
A

X
A
M
I
R
A

;
S
A
D
M

I

;

R
A
V
B

C
F
O

;

F
O
C

;

L
A
G

;

N
N
A

R
G
R

;

A
M
I
R
A
S

;

W
H

7
0
0
2
–
1
0
0
2

1
0
0
2

6
0
0
2
–
3
0
0
2

9
0
0
2
–
4
0
0
2

6
0
0
2
–
4
9
9
1

1
1
0
2
–
8
9
9
1

9
0
0
2
–
9
9
9
1

3
0
0
2
–
3
9
9
1

8
0
0
2
–
7
0
0
2

1
1
0
2
–
0
9
9
1

2
1
0
2
–
7
9
9
1

1
1
0
2
–
8
0
0
2

1
1
0
2
–
8
0
0
2

2
1
0
2
–
0
8
9
1

2
1
0
2
–
3
9
9
1

3
1
0
2
–
4
0
0
2

9
0
0
2
–
7
0
0
2

5
1
0
2
–
4
1
0
2

4
1
0
2
–
0
1
0
2

4
1
0
2
–
3
1
0
2

7
1
0
2
–
5
1
0
2

,

n
n
A

n
o
M

,
a
u
Q

y
l
h
t
n
o
M

l
a
u
n
n
A

y
l
r
e
t
r
a
u
Q

y
l
h
t
n
o
M

l
a
u
n
n
A

l
a
u
n
n
A

l
a
u
n
n
A

y
l
r
e
t
r
a
u
Q

y
l
r
e
t
r
a
u
Q

y
l
h
t
n
o
M

y
l
r
e
t
r
a
u
Q

l
a
u
n
n
A

l
a
u
n
n
A

l
a
u
n
n
A

y
l
h
t
n
o
M

7
0
0
2
–
4
8
9
1

3
0
0
2
–
9
7
9
1

6
1
0
2
–
3
6
9
1

7
9
9
1
–
0
7
9
1

9
0
0
2
–
9
9
9
1

9
9
9
1
–
0
9
9
1

8
0
0
2
–
5
9
9
1

1
1
0
2
–
8
6
9
1

2
1
0
2
–
7
9
9
1

2
1
0
2
–
1
9
9
1

1
1
0
2
–
0
8
9
1

2
1
0
2
–
0
8
9
1

2
1
0
2
–
6
5
9
1

2
1
0
2
–
4
0
0
2

0
0
1

2
7
3

8
2

1
1

0
1

0
0
1

6
7
1

2
9
1

6
1
1

2
3

3
3

7
5

A
S
U

l
e
n
a
P

A
S
U

i

a
n
h
C

i

a
n
h
C

A
S
U

l
a
p
e
N

l
e
n
a
P

i

a
n
h
C

i

a
n
h
C

A
S
U

1
0
0
2
–
5
9
9
1

5
8

l
i
z
a
r
B

6
0
0
2
–
3
0
0
2

8
0
8
1

a
i
h
c
e
z
C

a
i
t
a
o
r
C

)
2
1
0
2
(

k
e
z
i
V
d
n
a

)
1
1
0
2
(

.
l
a

t
e

a
i
x
‐
L

i

ć

i
r
t
o
B

)
1
1
0
2
(

h
s
o
t
n
I
c

M
d
n
a

e
k
o
o
C

)
1
1
0
2
(

g
n
a
h
Z

i
e
f
u
R

d
n
a

u
i
L

)
0
1
0
2
(

.
l
a

t
e

e
t
n
a
r
o
n
O

)
0
1
0
2
(

.
l
a

t
e

o
ã
l
a
v
r
o
C

)
0
1
0
2
(

j
e
l
O
d
n
a

k
e
j
á
H

)
0
1
0
2
(

l
o
r
K

)
2
1
0
2
(

n
a
k
z
O
d
n
a

s
l
e
s
y
h
G

n
a
o
J

d
n
a

s
o
l
u
o
p
o
k
a
m

i
s
A

)
2
1
0
2
(

a
l
a
r
i
o
K

)
3
1
0
2
(

s
e
d
e
r
a
P

)
3
1
0
2
(

n
u
j
i

h
Z

)
4
1
0
2
(

g
n
a
h
Z

)
5
1
0
2
(

n
a
k
z
O
d
n
a

s
l
e
s
y
h
G

r
i
s
a
t
n
u
M
d
n
a

i
d
n
a
N

)
5
1
0
2
(

y
r
u
h
d
u
a
h
C

)
6
1
0
2
(

.
l
a

t
e

i
r
a
d
m
a
l
A

)
7
1
0
2
(

a
l
i
l
i

i

m
h
C

1
0
1

h
s
e
d
a
l
g
n
a
B

l
a
u
n
n
A

y
l
h
t
n
o
M

y
l
r
e
t
r
a
u
Q

6
0
0
2
–
3
6
9
1

5
1
0
2
–
0
0
0
2

4
1
0
2
–
3
9
9
1

4
4

2
8
1

0
1
1

n
a
r
I

a
i
n
a
z
n
a
T

y
l
h
t
n
o
M

2
1
0
2
–
0
0
0
2

4
4
1

l
i
z
a
r
B

y
l
r
e
t
r
a
u
Q

7
1
0
2
–
9
0
0
2

6
3

a
c
i
r
f
A
h
t
u
o
S

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

a
n
o
c
i
T

)
7
1
0
2
(

r
e
g
r
e
b
l
o
S

d
n
a

a
s
i
n
a
n
a
k
a
M

)
8
1
0
2
(

o
r
e
r
E

n
e
d
e
w
S

n
i
t
r
a
M
d
n
a

n
a
i
r
a
z
a
n
h
a
h
S

C
F
O

;

F
O
C

;

A
M
I
R
A
S

C
F
O

F
O
C

;

R
A
V
B

;

R
A
V

;

M
C
E

;

W
H

;

W
R

5
1
0
2
–
1
1
0
2

y
l
r
e
t
r
a
u
Q

6
1
0
2
–
5
0
0
2

5
5

a
i
n
a
b
l
A

)
8
1
0
2
(

i
c
e
v
h
a
K
d
n
a

j
a
b
a
S

R
A

A
M
I
R
A

R
A
V

;

A
M
I
R
A

;

R
A

7
1
0
2

y
l
h
t
n
o
M

6
1
0
2
–
5
8
9
1

8
7
3

n
a
t
s
i
k
a
P

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

e
n
e
i
k
i
m
i
e
r
t
S

)
s
e
u
n
i
t
n
o
C
(

E
P
A
M

A
M
I
R
A

P
L
M

M
T
S
L

;

P
L
M

;

A
M
I
R
A

8
1
0
2
–
5
1
0
2

y
l
r
e
t
r
a
u
Q

8
1
0
2
–
9
9
9
1

0
7
7

A
S
U

)
9
1
0
2
(

.
l
a

t
e

n
o
t
x
u
B

.
r
e
p

.
r
o
F

.

q
e
r
f

.
s
b
O

R
Y
T

O
T

8
8
2

y
r
t
n
u
o
C

)
s
(
r
o
h
t
u
A

l
e
n
a
P

)
0
1
0
2
(

z
e
r
é
P

d
n
a

l
a
g
e
r
d
e
P

)
d
e
u
n
i
t
n
o
C
(

|

1

E
L
B
A
T

6

Public Budgeting & Finance, 2025

---

<!-- PAGE 7 -->

)
s
(
c
i
r
t
e
M

;

E
A
M

;

E
S
M
R

;

E
M

;

E
P
A
M

E
S
A
M

;

E
P
M

;

E
S
M
R

E
P
A
M

;

E
A
M

t
s
r
o
W

W
R

t
s
e
B

S
T
A
B

C
F
O

;
S
T
A
B

;

A
M
I
R
A
S

;

W
R

8
1
0
2
–
5
1
0
2

y
l
h
t
n
o
M

4
1
0
2
–
6
0
0
2

s
d
o
h
t
e
M

.
r
e
p

.
r
o
F

.

q
e
r
f

.
s
b
O

R
Y
T

O
T

8
0
1

y
r
t
n
u
o
C

e
y
i
k
r
ü
T

)
d
e
u
n
i
t
n
o
C
(

|

1

E
L
B
A
T

)
9
1
0
2
(

l

z
a
m
u
r
o
Y

d
n
a

u
d
ğ
o
d
r
E

)
s
(
r
o
h
t
u
A

W
R

R
A
V
B

W
R

;

R
A
V
B

;

R
A
V

;

R
A

4
1
0
2
–
9
0
0
2

l
a
u
n
n
A

8
0
0
2
–
7
7
9
1

2
3

A
S
U

)
9
1
0
2
(

s
e
d
r
o
C
d
n
a

a
e
h
S
c
M

E
A
M

;

E
S
M
R

A
M
I
R
A

S
E

;

R
A
V
B

S
E

;

A
M
I
R
A

;

R
A
V
B

I

S
A
D
M
R
A

‐

C
F
O

I

;
S
A
D
M
R
A

‐

A
M
I
R
A

‐

A
C
P

R
V
S
K
W

‐

C
F
O

;

A
M
I
R
A

;

R
V
S
K
A
C
P

‐

;

R
V
S
K
W

‐

;

R
V
S
K

R
V
S
K
W
A
C
P

‐

‐

5
1
0
2
–
2
1
0
2

7
1
0
2
–
5
1
0
2

9
1
0
2
–
7
1
0
2

y
l
r
e
t
r
a
u
Q

y
l
h
t
n
o
M

y
l
r
e
t
r
a
u
Q

2
1
0
2
–
8
9
9
1

4
1
0
2
–
6
0
0
2

6
1
0
2
–
1
8
9
1

6
5

a
c
i
r
f
A
h
t
u
o
S

)
9
1
0
2
(

.
l
a

t
e

o
p
a
l
o
M

8
0
1

4
4
1

e
y
i
k
r
ü
T

a
i
r
e
g
i
N

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

n
a
s
s
a
h
A

l

)
9
1
0
2
(

z
a
m

l

ı

Y

7
1
0
2
–
6
1
0
2

y
l
r
e
t
r
a
u
Q

6
1
0
2
–
3
9
9
1

2
9

o
h
t
o
s
e
L

)
0
2
0
2
(

e
n
a
m
a
D

;

E
S
M
R

E
P
A
M

;

E
A
M

;

E
A
M

E
P
A
M

;

E
S
M
R

;

E
P
A
M

E
S
M
R

;

E
S
M

;

E
A
M

;

E
P
A
M

E
S
M
R

;

E
S
M

;

E
S
M
R

E
P
A
M

;

E
A
M

E
P
A
M

;

E
S
M
R

e
n
o
N

E
S
M

;

E
P
A
M

E
S
M
R

;

E
A
M

;

E
S
M
R

E
P
A
M

;

E
P
M

;

R
V
S
K
W

‐

R
V
S
K
A
C
P

‐

C
F
O

W
H

C
F
O

T
R
A
C

W
R

W
R

E
P
M

C
F
O

)
s
e
u
n
i
t
n
o
C
(

E
P
A
M

;

E
A
M

E
A
M

;

E
S
M
R

R
L
M

R
G
R

O
S
S
A
L

;

R
A

;

R
G
R

;

O
S
S
A
L

;

F
R

;

W
R

;

R
A

N
N
A

;

T
S
O
O
B
G
X

N
N
A

t
f
i
r
D

N
N
A

;

R
L
M

t
f
i
r
D

;

n
a
e
M

;

F
C
O
L

;

T
R
L

;

T
S
O
O
B
G
X

E
S
M
R

;

E
P
A
M

A
M
I
R
A
S

R
A
V

A
M
I
R
A
S

;

R
A
V

3
2
0
2
–
1
2
0
2

y
l
r
e
t
r
a
u
Q

3
2
0
2
–
1
1
0
2

9
4

t
a
r
a
h
B

N
N
A

F
O
C

F
O
C

;

N
N
A

;
S
E

;
S
T
A
B
T

2
2
0
2
–
1
2
0
2

y
l
h
t
n
o
M

2
2
0
2
–
7
1
0
2

4
4

t
a
r
a
h
B

E
P
A
M

n
a
e
M

;

N
N
A

;

T
R
L

;

N
N
K

;

N
N
A

;

N
N
K

;
S
E

;

A
M
I
R
A

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

n
n
A

n
o
M

,
a
u
Q

5
1
0
2
–
1
9
9
1

5
0
0
1

A
S
U

)
4
2
0
2
(

n
o
t
r
e
v
O
d
n
a

n
o
s
r
a
L

U
R
G

;

N
N
R
S
A

s
e
y
a
B

e
v
ï
a
N

;

N
N
K

s
e
y
a
B

e
v
ï
a
N

M
T
S
L

;

T
S
O
O
B
G
X

;

F
R

;

M
T
S
L

;

A
M
I
R
A

3
2
0
2
–
9
1
0
2

a
u
Q

,

n
n
A

3
2
0
2
–
9
1
0
2

0
2

t
p
y
g
E

)
4
2
0
2
(

.
l
a

t
e

a
f
i
l
a
h
K

.

M

;

N
N
R
B

i

;

M
T
S
L

;

N
N
C

A
M
I
R
A

U
R
G

;

T
S
O
O
B
G
X

;

R
V
S

;
S
T
E

;

A
M
I
R
A

0
2
0
2
–
5
1
0
2

l
a
u
n
n
A

0
2
0
2
–
0
9
9
1

1
3

l
e
n
a
P

)
3
2
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

1
2
0
2
–
9
1
0
2

9
1
0
2
–
9
0
0
2

l
a
u
n
n
A

y
l
r
e
t
r
a
u
Q

1
2
0
2
–
2
0
0
2

9
0
0
2
–
2
9
9
1

0
3

1
7

i

a
n
h
C

a
i
l
a
r
t
s
u
A

)
4
2
0
2
(

a
L

d
n
a

g
n
o
W

)
4
2
0
2
(

e
i
X

A
M
I
R
A

W
H

;

A
M
I
R
A

9
1
0
2
–
7
1
0
2

y
l
h
t
n
o
M

6
1
0
2
–
2
0
0
2

0
8
1

a
n
a
h
G

T
R
A
C

;

N
N
K

M
G

C
F
O

;

M
G

A
M
I
R
A

;

N
N
A

;

A
M
I
R
A

;
S
E

;

A
M

9
1
0
2
–
7
1
0
2

4
1
0
2
–
4
9
9
1

l
a
u
n
n
A

l
a
u
n
n
A

6
1
0
2
–
6
0
0
2

4
1
0
2
–
4
9
9
1

S
A
D
M

I

W
R

;

F
O
C

;

L
D
A

;

R
A

;
S
A
D
M

I

B
G
C

C
F
O

;

B
G
C

;

W
R

;

O
S
S
A
L

;
S
A
D
M

I

8
1
0
2
–
9
9
9
1

1
2
0
2
–
0
2
0
2

l
a
u
n
n
A

n
o
M

,
a
u
Q

2
1
0
2
–
8
5
9
1

1
2
0
2
–
6
0
0
2

1
1

6
1
1

1
4

4
7
1

e
y
i
k
r
ü
T

A
S
U

A
S
U

A
S
U

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

g
n
u
h
C

)
0
2
0
2

.
l
a

t
e

l
a
s
n
Ü

l
e
b
A
d
n
a

i
r
o
f
O

)
0
2
0
2
(

y
e
m
u
F

)
2
2
0
2
(

g
n
a
Y

d
n
a

i
r
i
h
a
L

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

s
l
e
s
y
h
G

)
3
2
0
2
(

a
y
r
a
h
c
a
t
t
a
h
B

d
n
a

e
e
j
r
e
h
k
u
M

)
3
2
0
2
(

.
l
a

t
e

b
i
y
y
a
h
T

Public Budgeting & Finance, 2025

7

---

<!-- PAGE 8 -->

s
u
o
n
e
g
o
x
E

h
t
i

w
e
g
a
r
e
v
A
g
n
i
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

,

X
A
M
I
R
A

;
e
g
a
r
e
v
A
g
n
i
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

e
v
i
s
s
e
r
g
e
r
o
t
u
A

,

A
M
I
R
A

;
e
v
i
s
s
e
r
g
e
r
o
t
u
A

,

R
A

;

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

l
a
i
c
i
f
i
t
r
A

,

N
N
A

;
g
a
L

d
e
t
u
b
i
r
t
s
i
D
d
e
t
n
e
m
g
u
A

,

L
D
A

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

l
a
n
o
i
t
c
e
r
i
d
i
B

,

N
N
R
B

i

;

n
o
i
t
a
m
r
o
f
s
n
a
r
T
x
o
C
–
x
o
B
h
t
i

w

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
l
o
v
n
o
C

,

N
N
C

;
r
e
t
l
i

F

n
a
m
l
a
K
e
t
a
t
S
‐

j

i
t
l
u
M
d
e
t
s
u
d
A
y
l
l
a
n
o
i
t
c
e
S
‐

l
e
d
o
M
e
c
a
p
S
e
t
a
t
S
g
n
h
t
o
o
m
S
l
a
i
t
n
e
n
o
p
x
E

i

,

S
T
A
B

;

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
d
e
s
a
B
‐
n
o
i
t
n
e
t
t

A

,

N
N
R
S
A

;
e
g
a
r
e
v
A
‐
g
n
i
v
o
M
e
v
i
s
s
e
r
g
e
r
o
t
u
A

‐

‐

s
s
o
r
C

,

F
K
S
M
C

;
g
n
i
t
s
o
o
B

t
n
e
i
d
a
r
G
e
s
i

W

t
n
e
n
o
p
m
o
C

,

B
G
C

;
e
e
r
T

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

d
n
a

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
C

,

T
R
A
C

;

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
o
t
u
A
r
o
t
c
e
V
n
a
i
s
e
y
a
B

,

R
A
V
B

;

k
r
o
w
t
e
N

:
s
n
o
i
t
a
i
v
e
r
b
b
A

,

A
M
R
A

;
s
t
u
p
n
I

F
O
C

;

A
M
I
R
A

)
s
(
c
i
r
t
e
M

E
P
A
M

t
s
r
o
W

A
M
I
R
A

t
s
e
B

W
H

;

N
N
K

;

A
M
I
R
A

;

W
H

F
C
O
L

;

N
N
R
G

9
1
0
2
–
7
1
0
2

y
l
h
t
n
o
M

9
1
0
2
–
9
0
0
2

s
d
o
h
t
e
M

.
r
e
p

.
r
o
F

.

q
e
r
f

.
s
b
O

R
Y
T

O
T

0
2
1

y
r
t
n
u
o
C

A
S
U

)
5
2
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
u
h
C

)
s
(
r
o
h
t
u
A

E
P
A
M

t
e
h
p
o
r
P

;

M
T
S
L

A
M
I
R
A
S

;
t
e
h
p
o
r
P

;

M
T
S
L

;

W
H

4
2
0
2
–
3
2
0
2

y
l
h
t
n
o
M

2
2
0
2
–
5
0
0
2

6
1
2

e
y
i
k
r
ü
T

)
5
2
0
2
(

a
r
a
K
d
n
a

r
e
l
ü
g
n
e
Ş

E
P
A
M

n
a
e
M

;

N
N
A

F
C
O
L

;
t
f
i
r
D

;

N
N
A

;

N
N
K

;

R
G
R

;
S
E

;

A
M
I
R
A

7
1
0
2
–
6
1
0
2

F
C
O
L

;

n
a
e
M

;
t
f
i
r
D

;

T
S
O
O
B
G
X

,

n
n
A

n
o
M

,
a
u
Q

5
1
0
2
–
1
9
9
1

5
0
0
1

A
S
U

)
5
2
0
2
(

n
o
t
r
e
v
O
d
n
a

n
o
s
r
a
L

)
d
e
u
n
i
t
n
o
C
(

|

1

E
L
B
A
T

8

‐

‐

‐

y
a
r
G

,

M
G

;
y
t
i
c
i
t
s
a
d
e
k
s
o
r
e
t
e
H

l
a
n
o
i
t
i
d
n
o
C
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

,

H
C
R
A
G

;
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
c
i
t
e
n
e
G

,

L
A
G

;
g
n
i
r
e
t
l
i

F
e
v
i
t
p
a
d
A

l
a
r
e
n
e
G

,

F
A
G

i

;
g
n
h
t
o
o
m
S
l
a
i
t
n
e
n
o
p
x
E

,

S
E

;

n
o
i
t
c
e
r
r
o
C
r
o
r
r
E

,

M
C
E

;
s
t
s
a
c
e
r
o
F
f
o
g
n
n
i
b
m
o
C

i

,

F
O
C

;

k
r
o
w
t
e
N

‐

‐

e
v
i
t
i
d
d
A

l
a
n
o
s
a
e
S

r
e
t
n
W

i

t
l
o
H

,

A
A
S
W
H

;

h
c
a
o
r
p
p
A
e
v
i
t
a
c
i
l
p
i
t
l
u
M

l
a
n
o
s
a
e
S

r
e
t
n
W

i

t
l
o
H

,

A
M
S
W
H

;
s
r
e
t
n
W

i

t
l
o
H

,

W
H

;

d
o
i
r
e
P
d
e
t
s
a
c
e
r
o
F

,
.
r
e
p

.
r
o
F

;
t
i
n
U

t
n
e
r
r
u
c
e
R
d
e
t
a
G

,

U
R
G

;

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

,

N
N
R
G

;
l
e
d
o
M

l
a
r
u
t
c
u
r
t
S

y
r
t
n
u
o
C

i
t
l
u
M

,

M
C
M

;
e
g
a
r
e
v
A
g
n
i
v
o
M

,

A
M

;

k
r
o
w
t
e
N
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

t
r
o
h
S

g
n
o
L

,

M
T
S
L

;

d
n
e
r
T
r
a
e
n
L

i

,

T
R
L

;

d
r
a
w
r
o
F

d
e
i
r
r
a
C
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
O

t
s
a
L

,

F
C
O
L

;
r
o
t
a
r
e
p
O
n
o
i
t
c
e
l
e
S

d
n
a

e
g
a
k
n
i
r
h
S

e
t
u
l
o
s
b
A

t
s
a
e
L

,

O
S
S
A
L

;

h
c
a
o
r
p
p
A

,

A
C
P

;
y
c
n
e
u
q
e
r
F

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
O

,
.

q
e
r
f

.
s
b
O

;
s
t
s
a
c
e
r
o
F

l
a
i
c
i
f
f

O

,

C
F
O

;
r
e
t
l
i

F

n
a
m
l
a
K
e
t
a
t
S
‐

i
t
l
u
M

,

F
K
S
M

;

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
L

i

e
l
p
i
t
l
u
M

,

R
L
M

;

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

r
e
y
a
L
‐

i
t
l
u
M

,

P
L
M

;
y
c
n
e
u
q
e
r
F
‐
d
e
x
i
M

,

X
I
M

;
g
n

i
l
p
m
a
S

a
t
a
D
‐
d
e
x
i
M

,

S
A
D
M

I

;
l
e
d
o
M

,

R
V
S

i

;
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

,

M
V
S

;
l
e
d
o
M

l
a
r
u
t
c
u
r
t
S

y
r
t
n
u
o
C
e
l
g
n
i
S

,

M
C
S

;
e
g
a
r
e
v
A
g
n
i
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

e
v
i
s
s
e
r
g
e
r
o
t
u
A

l
a
n
o
s
a
e
S

,

A
M
I
R
A
S

;

k
l
a
W
m
o
d
n
a
R

,

W
R

;

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

R
G
R

;
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

,

F
R

;
s
i
s
y
l
a
n
A

t
n
e
n
o
p
m
o
C

l
a
p
i
c
n
i
r
P

,

R
A
V

;
e
g
n
a
r

s
r
a
e
y

'

s
a
t
a
d

i

g
n
n
i
a
r
T

,

R
Y
T

;
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
a
r
t

o
t

d
e
s
u

s
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

l
a
t
o
T

,

O
T

;
s
t
n
e
n
o
p
m
o
C

l
a
n
o
s
a
e
S

d
n
a

.
g
n
i
t
s
o
o
B

t
n
e
i
d
a
r
G
e
m
e
r
t
x
E

,

T
S
O
O
B
G
X

;

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

l
e
n
r
e
K
h
t
i

w

t
e
l
e
v
a
W

,

R
V
S
K
W

;

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
o
t
u
A
r
o
t
c
e
V

‐

d
n
e
r
T
—

s
r
o
r
r
E
A
M
R
A
—
n
o
i
t
a
m
r
o
f
s
n
a
r
T

x
o
C
–
x
o
B
—

y
t
i
l
a
n
o
s
a
e
S

c
i
r
t
e
m
o
n
o
g
i
r
T

,

S
T
A
B
T

;

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

In particular, the emergence of complex hybrid models supported
by PCA represents a new stage in which researchers strategically
combine feature engineering with advanced algorithms to maxi-
mize model performance.

The overall assessment of this methodological evolution reveals
that the field of budget forecasting is not static but rather a
dynamic area of research, constantly interacting with develop-
ments in neighboring disciplines such as econometrics, opera-
tions research, and AI. The journey from simple time‐series
models to complex neural networks reflects both the methodo-
logical maturity and the accumulated intellectual capital of the
field. At the same time, however, the dense methodological
diversity illustrated in Figure 1 suggests the presence of a
“methodological inflation” in the literature, a phenomenon that
increasingly complicates the task of selecting an optimal method
within a given context for policymakers and practitioners.

Second, the frequency with which different forecasting methods
are used together within the same study has been examined.
This analysis makes it possible to understand which methods
researchers most frequently evaluate side by side when con-
ducting performance comparisons, and thus which methodo-
logical combinations have gained wider acceptance.

The connections in Figure 2 indicate which pairs of methods are
most frequently tested together in comparative studies in the
literature. The analyses clearly show that traditional methods are
often used both among themselves and in conjunction with next‐
generation techniques for comparison purposes. For instance,
ARIMA is frequently compared not only with its own derivatives,
such as SARIMA, which incorporate seasonal variations, but also
with ML‐based methods, such as ANN or SVM. Similarly, official
agency forecasts and various regression techniques appear to
serve as a benchmark for almost all methodological classes. In
particular, when evaluating the performance of ML algorithms
(XGBoost, LSTM, and SVM), comparisons with these traditional
methods emerge as a widespread trend. It is also noteworthy that
variations within the same model family (e.g., VAR vs. BVAR or
AR vs. ARIMA) are frequently analyzed together. This suggests
that researchers aim to understand how different specifications
or enhancements within a given model family, such as Bayesian
approaches or seasonal adjustments, affect forecasting perform-
ance. In sum, this visual network structure reveals that com-
parative analyses in the budget forecasting literature follow a
certain systematic pattern: the validity and contribution of a new
method are most often assessed against established and widely
accepted traditional methods, while the relative strengths and
weaknesses of different methodological families are empirically
evaluated through these typical comparisons.

Third, the changing trends in the popularity of specific forecasting
methods over time have been examined. This analysis makes it
possible to objectively observe the shifts in academic interest to-
ward particular methodologies and the dominance cycles of cer-
tain methods within the literature. The graph displays the
changing frequencies of use over the years for the six most fre-
quently compared methods in the analyzed studies.

The findings derived from Graph 1 clearly reveal shifts in academic
forecasts were frequently used as benchmark
trends. Official

Public Budgeting & Finance, 2025

---

<!-- PAGE 9 -->

FIGURE 1

| Evolution of forecasting methods in budgeting literature over time.

FIGURE 2

| Co‐occurrence of forecasting methods in comparative budget studies.

references. The ARIMA model, however, has remained a con-
sistently popular tool for comparison since the 1990s. Regression‐
based methods experienced a resurgence in the early 2000s, but
their popularity subsequently declined somewhat. ML methods,
such as ANN, have increasingly featured in comparative studies
since the 2010s. COF, on the other hand, has maintained a stable
presence among the methods consistently used for comparison
throughout the entire period under review. These trends indicate
that the literature has preserved its reference points based on tra-
ditional methodologies while gradually transitioning toward new‐

generation, AI‐based approaches. Overall, the current methodo-
logical spectrum has expanded to encompass both basic statistical
models and advanced computational techniques (Tables 2–4).

Fourth, the structural characteristics of the datasets used in the
training of forecasting models in the reviewed studies have been
analyzed. This analysis is critical for understanding the capacity
and diversity of the data sources feeding the models. Below,
an assessment is presented showing the distributions of the
training datasets in terms of time span (number of years),

Public Budgeting & Finance, 2025

9

---

<!-- PAGE 10 -->

GRAPH 1

| Trends in the popularity of key forecasting methods over time (best 5).

TABLE 2

| Characteristics of training datasets in budget forecasting studies.

Period
1–5 years
6–10 years
11–15 years
16–20 years
21–25 years
26–30 years
31–35 years
35–50 years

50+ years

Studies (N)

4

13

17

10

9

2

7

4

3

Observation range
1–25
26–50
51–75
76–100
101–150
151–250
251–400
401–1000

1000+

Studies (N)

Frequency

Studies (N)

Quarterly

Annual

Monthly

Biannual

28

26

23

1

8

16

10

6

12

7

3

4

3

| Country‐level distribution of budget forecasting

TABLE 4

| Number of studies using each evaluation metric.

TABLE 3
research.

Countries

USA

China

Panel

Türkiye

Bharat

Brazil

South Africa

Others*

*17 different countries studied once.

Studies (N)

30

6

6

4

2

2

2

17

Metric

MAPE

RMSE

MAE

MPE

PE

MSE

ME

Others

None

Frequency

38

36

22

7

6

5

5

9

2

number of observations, and the most commonly used data
frequencies (Graph 2).

Examining the distribution of the time spans of the training da-
tasets, it is evident that the vast majority of studies (over 60%) rely

on datasets covering 6–25 years. Notably, datasets spanning
11–15 years are the most commonly used period (17 studies),
indicating a clear tendency in the literature toward a medium‐
term forecasting horizon. This approach allows for capturing
macroeconomic cycles by maintaining sufficient historical depth

10

Public Budgeting & Finance, 2025

---

<!-- PAGE 11 -->

GRAPH 2

| Average training data span by forecasting model (best 10).

while limiting potential parameter instability issues associated
with very long time series. On the other hand, studies using da-
tasets of 31 years or more are relatively few (14 studies in total),
reflecting both the accessibility challenges and methodological
risks posed by structural breaks in very long series. Conversely, the
small number of studies (4 studies) relying solely on short‐term
data of 1–5 years can be considered characteristic of contexts with
limited data depth, particularly in developing economies.

In terms of the number of observations, the literature exhibits
considerable diversity. A significant portion of studies is con-
centrated in the 26–50 observation range (16 studies), while
those based on more than 100 observations also constitute a
notable group (28 studies). However, only 16 of these 28 studies
contain 150 or more observations, indicating that studies rely-
ing on long series remain relatively limited in the literature. The
presence of eight studies with only 1–25 observations raises
serious concerns regarding the reliability of the models used.
Forecasting based on such short series entails substantial
methodological weaknesses, particularly in terms of testing the
statistical significance of parameters and producing robust
forecasts. This issue may prevent data‐intensive methods, such
as DL, from being fully evaluated, highlighting varying levels of
reliability in the literature and necessitating cautious interpre-
tation of results from studies with limited observations.

Examining data frequencies, it is observed that quarterly (28
studies), annual (26 studies), and monthly (23 studies) data are
chosen with relatively similar frequency. This distribution indi-
cates that, rather than a concentration on a single frequency,
different frequencies are used at comparable rates. Accordingly,
researchers' choices are largely shaped by data availability, the
scope of the study, and the intended forecasting horizon.

The findings on the average training periods of models in
Figure 3 show significant alignment when considered alongside

the tabular data. Notably, studies based on relatively simple
models such as ADL and AR have average training periods
exceeding 40 years, indicating that long series are necessary to
ensure the parametric stability of these models. In contrast,
more complex models such as MIDAS or ARMA can be applied
with comparatively shorter datasets, demonstrating the adapt-
ability of methods to series of different lengths. However, it is
noteworthy that
type and
number of observations does not follow a linear pattern. While
some short‐term studies correspond to low‐complexity models,
long‐term series tend to be associated with models sensitive to
parametric stability. This suggests that the alignment between
model choice and training data length is shaped not only by
technical considerations but also by data accessibility and the
objectives of the study.

the relationship between model

Fifth, the average forecasting horizons of the methods used in the
reviewed studies have been analyzed. This analysis provides
important insights into which time spans are preferred for dif-
ferent methodological approaches and whether certain methods
are characteristically associated with short‐ or long‐term forecasts.

The findings in Graph 3 indicate a clear clustering of methods
in terms of forecasting horizons. Traditional statistical methods,
such as AR and MA models, stand out with long average
horizons of 14.3 and 12 years, respectively. Similarly,
the
MIDAS method, with an average horizon of 9.7 years, is among
the methods used for long‐term forecasts. This suggests that
relatively simple linear methods tend to provide a more stable
option for long‐term forecasts.

forecasting horizons. For

In contrast, parametric and multivariate models tend to focus
on shorter
example, ARIMA
(5.5 years), VAR (5.1 years), and BVAR (4.7 years) are predom-
inantly applied in short‐ to medium‐term forecasts. This pattern
indicates that as the number of parameters and the modeling

Public Budgeting & Finance, 2025

11

---

<!-- PAGE 12 -->

FIGURE 3

| Relationship between methods and performance metrics.

GRAPH 3

| Average forecasting horizons by method in reviewed studies.

flexibility of these models increase, their stability diminishes in
the face of long‐term uncertainty.

In ML‐ and DL‐based methods, the forecasting horizon is notably
shorter. ANN stands out with an average horizon of 5.3 years, while
LSTM is limited to only 3.3 years. These results indicate that such
methods are strong in capturing complex, nonlinear relationships
over short‐term periods but are more constrained in long‐term
forecasts due to risks of parameter instability and overfitting.

Overall, a methodological division of labor emerges among
forecasting methods: simple linear statistical methods are

concentrated in relatively long‐term forecasts, parametric and
multivariate models in medium‐term horizons, and ML and DL
methods in short‐term forecasts. This distribution indicates that
forecasting horizons are determined not only by researchers'
preferences but also by the structural limitations inherent in
each method.

Sixth, the geographic distribution of the reviewed comparative
studies has been analyzed. This analysis provides important
insights into which countries and regions academic research on
budget forecasting methods is concentrated, thereby shedding
light on the geographic coverage of the existing literature.

12

Public Budgeting & Finance, 2025

---

<!-- PAGE 13 -->

The findings on country distribution reveal a pronounced
concentration and imbalance in the literature. The United
States accounts for the largest share with 30 studies, followed by
China (6), panel datasets (6), and Turkey (4). Brazil, India, and
South Africa are represented by two studies each. The
remaining 17 countries are covered only once and are grouped
under the “Others” category. This pattern indicates that em-
pirical research is heavily focused on a limited set of countries,
while a wide range of other nations receives very limited
attention.

The reasons for the United States' clear predominance include
easy access to data, long historical macroeconomic series, the
perception of U.S. data as a global benchmark in academic
publications, and the dominance of Anglo‐Saxon literature. In
contrast, for developing countries, both difficulties in accessing
long‐term reliable data series and differences in institutional
contexts result in their underrepresentation in studies. Turkey's
representation by only four studies serves as a concrete example
of this overall imbalance.

On the other hand, the presence of six studies using panel da-
tasets indicates that researchers have also pursued cross‐
country comparisons rather than focusing solely on single‐
country analyses. However, the limited number of panel studies
suggests that the literature has not yet fully developed a com-
parative perspective capable of providing generalizable insights
and revealing cross‐country differences.

Seventh, the distribution of metrics used to evaluate forecasting
performance in the reviewed comparative studies has been
analyzed. This analysis provides important insights into which
evaluation criteria are prioritized in the literature and, conse-
quently, which dimensions of error are considered most critical
in method comparisons.

for the vast majority of usage, establishing a dominant position
in assessing forecasting accuracy. The prominence of MAPE
and RMSE can be explained by their ease of interpretation and
their suitability for comparisons across series of different
magnitudes.

In contrast, metrics such as MPE (7 studies), ME (5 studies),
MSE (5 studies), and PE (6 studies) are used relatively infre-
quently. Their limited representation indicates that the litera-
ture tends
to favor standardized metrics that allow for
international comparisons. Additionally, in nine studies cate-
gorized as “Others,” more specific or context‐specific metrics
were employed, while two studies did not report any perform-
ance metric at all. The latter case can be regarded as a signifi-
cant shortcoming in terms of methodological transparency.

The network structure in the graph further clarifies the re-
lationships between methods and metrics. RMSE and MAPE
stand out as nodes with the most extensive connections,
showing strong associations with widely used methods such as
ARIMA, ANN, HW, VAR, OFC, COF, and SARIMA. This
finding indicates that performance evaluations of prominent
methods in the literature generally rely on the same set of
metrics, and comparability is largely established around these
measures. In contrast, less frequently used methods such as
LSTM, XGBoost, or Prophet are linked to a relatively limited
number of metrics, suggesting both low methodological diver-
sity and the absence of a standardized approach for evaluating
the performance of these methods.

Eighth and finally, the relationship between method diversity
and academic impact in the reviewed comparative studies has
been analyzed. This analysis provides important insights into
whether the number of methods compared in a study has any
effect on the number of citations the study receives (Graph 4).

Examining the metrics used to evaluate method performance, a
clear concentration is observed in the literature. The most fre-
quently used evaluation criteria are MAPE (38 studies), RMSE
(36 studies), and MAE (22 studies). These three metrics account

The analysis results indicate a notable but nonlinear relation-
ship between the number of methods in a study and its citation
count. The vast majority of the reviewed studies (over 70%)
compare between 2 and 5 methods. Studies with 2 methods

GRAPH 4

| Relationship between studies, methods, and citations.

Public Budgeting & Finance, 2025

13

---

<!-- PAGE 14 -->

represent the most common category with 18 cases, followed by
3‐method studies with 15 cases and 4‐method studies with 14
cases. In terms of citation counts, the highest average citation
performance is observed among studies comparing between 3
and 6 methods. Studies with 3 methods receive an average of 26
citations, while those with 6 methods reach a similar average of
26 citations. This finding suggests that a moderate level of
method diversity may enhance academic impact.

However, it is also evident that citation performance does not
increase consistently with the number of methods. Studies
including 7 or more methods exhibit a noticeable decline in
citation counts. This suggests that comparisons involving an
excessive number of methods may be less favored by readers
and researchers or that such studies may give the impression of
emphasizing methodological breadth over analytical depth.
Interestingly, studies employing only a single method are quite
rare (3 studies), and their average citation count (7 citations)
that non‐
remains
comparative studies may have a more limited academic impact
compared to comparative studies.

relatively low. This

finding suggests

In conclusion, this analysis suggests the existence of an optimal
range for method diversity. Comparisons with very few meth-
ods are considered insufficient, while studies including an ex-
cessive number of methods may be less favored by readers.
Studies comparing between 3 and 6 methods exhibit the highest
academic impact, indicating that comprehensive yet focused
comparisons contribute more valuable insights to the literature.

5 | Discussion and Policy Recommendations

The comprehensive analysis presented in this study offers a
multidimensional examination of the comparative structure of
the budget forecasting literature, characterized by methodo-
logical diversity, geographic biases, and the ongoing tension
between model complexity and practical applicability within a
dynamic and evolving field. The following discussion synthe-
sizes these findings to draw broader implications, address
inherent tensions in the field, and suggest directions for future
research and practice.

5.1 | Methodological Diversity and the Quest for
the Optimal Model

The most striking finding of this study is the relentless diversi-
fication of forecasting methods. The evolution from simple AR-
IMA models to sophisticated LSTM networks and hybrid PCA‐
W‐KSVR frameworks represents a true methodological arms
race. This expansion is undoubtedly fueled by the quest for
accuracy, supported by increasing computational power and ri-
cher data availability. However, the analyses indicate that this
proliferation does not yield a universally superior algorithm;
rather, it has led to a form of methodological inflation that can
overwhelm practitioners and obscure clear guidance. The
absence of a single “best” method should not be viewed as a
failure of the research community but as a reflection of the
inherent complexity of budgetary processes. Budget data are the

product not of a single, static process, but of political negotia-
tions, economic shocks, institutional changes, and administrative
rules. Accordingly, the focus should shift from finding the opti-
mal model to identifying the right model for the right context.

5.2 | The Enduring Role of Simple Models and
the Benchmarking Paradox

Despite the influx of complex techniques, simple models such
as OFC, RW, and various regression approaches remain not
only relevant but also serve as fundamental benchmarks. Any
new model must consistently outperform these naïve or simple
standards to justify its added complexity. The fact that these
simple models still frequently rank among the top performers,
or at least are not consistently the worst, in comparative studies
serves as a cautionary reminder for the field. It underscores that
statistical sophistication does not automatically translate into
forecasting superiority, particularly in contexts where data are
noisy, short, and subject to unpredictable political interven-
tions. This creates a paradox: as research energy increasingly
focuses on developing complex models, the practical value of
these advancements often remains marginal when compared
against well‐defined, simple benchmarks.

5.3 | Data Quality, Quantity, and the Global
Inequality Issue

The analysis of training data characteristics highlights a sig-
nificant and often overlooked challenge: data constraints. The
prevalence of studies using 11–15 years of data indicates that
many models are built on relatively limited information sets.
This poses a critical limitation for data‐hungry methods such
as DL, potentially leading to overfitting and reduced out‐of‐
sample generalization performance. The geographic distribu-
tion of studies further exposes a substantial data gap. The
dominance of United States‐based research reflects not merely
academic preference but is directly linked to data availability,
quality, and length. The underrepresentation of developing
economies constitutes a critical gap in the literature. Budgetary
processes, institutional frameworks, and economic fluctuations
in these contexts differ substantially. Models optimized on long,
stable U.S. time series may fail when applied to economies
prone to fiscal shocks, characterized by lower data quality and
shorter historical records.

5.4 | Evaluation Inconsistency and the
Hegemony of Metrics

The near‐absolute dominance of MAPE, RMSE, and MAE as
performance metrics provides a common language for compari-
son but also poses a potential pitfall: the tyranny of averages.
These metrics measure the magnitude of errors but remain lar-
gely agnostic to the direction and timing of mistakes. In a bud-
getary context, the cost of overestimating a deficit (potentially
leading to unnecessary austerity measures) is substantially dif-
ferent from the cost of underestimating it (potentially triggering a
fiscal crisis). The near‐complete neglect of directional metrics

14

Public Budgeting & Finance, 2025

---

<!-- PAGE 15 -->

such as MPE in the current literature represents a significant
shortcoming. Evaluations should incorporate asymmetric loss
functions that reflect the real‐world political and economic costs
of errors, rather than solely their statistical properties.

horizon. The resilience of traditional statistical methods in long‐
term forecasts, alongside the strength of ML and DL approaches
in capturing short‐term complex relationships, indicates the
existence of a methodological division of labor.

5.5 | Academia–Practice Gap

Citation impact analysis provides a striking insight into the
sociology of the field. The higher citation rates of studies
comparing 3–6 methods suggest that the academic community
values comprehensive yet focused comparisons. However, this
academic ideal does not always align with practical needs. A
practitioner in a treasury department does not require a com-
parison of six different ML models; they need a single, robust,
interpretable, and operationally feasible model tailored to their
specific national context. This points to a potential academia–
practice disconnect. The complexity of state‐of‐the‐art models
(e.g., LSTMs and XGBoost) often renders them opaque “black
boxes” for policymakers. Simpler models or official forecasts,
even if slightly less accurate by some metrics, offer transparency
and accountability. Future research should address this gap by
not only reporting accuracy metrics but also considering oper-
ational aspects, such as computational requirements,
inter-
pretability, and integration into existing budgetary processes.

5.6 | Rise of Hybrid and Ensemble Approaches

The emergence of hybrid models points, albeit modestly, toward
a promising direction for the field. Rather than treating meth-
ods as competitors, the discipline is gradually recognizing the
value of hybridization and ensemble techniques. The strengths
of one model can compensate for the weaknesses of another.
For instance, a classical statistical model may capture long‐term
trends, while an ANN can adjust for recent nonlinear devia-
tions. Combining forecasts from different model families often
yields more accurate and robust results than any single model.
This meta‐modeling approach, which focuses on integrating
information rather than selecting a single “winner,” appears to
be a more efficient pathway than developing isolated, increas-
ingly complex algorithms.

6 | Conclusion

This study systematically analyzes the literature examining the
comparative performance of budget forecasting methods, pro-
viding a comprehensive overview of the field's methodological
evolution, geographic distribution, data characteristics, and
performance evaluation trends. The findings indicate that
budget forecasting is not a static domain but a dynamic research
area in continuous evolution, deeply influenced by develop-
ments in related disciplines.

The analyses of this study clearly demonstrate that there is no
single, universally optimal method for budget
forecasting.
Instead, the performance of forecasting methods varies subs-
tantially depending on contextual factors such as economic
conditions, data quality, institutional structures, and forecast

The pronounced geographic concentration in the literature,
particularly the underrepresentation of emerging economies,
poses significant limitations to the generalizability of existing
findings. Similarly, the near‐absolute dominance of metrics
such as MAPE, RMSE, and MAE in performance evaluation
leads to the neglect of critical dimensions, including the direc-
tion of errors and asymmetric costs.

The findings of this study offer important implications for
future research. First, contextual appropriateness should take
precedence over methodological complexity. Second, the geo-
graphic scope should be expanded to include emerging econo-
mies, and datasets should be enriched accordingly. Third,
performance evaluation criteria should be diversified to reflect
the policy costs of forecast errors. Finally, hybrid and ensemble
learning approaches warrant further investigation to leverage
the relative strengths of different methods.

For policymakers and practitioners, this study emphasizes the
importance of avoiding dogmatic method selection in budget
forecasting. Adopting a flexible and pluralistic approach, taking
into account institutional capacity, data quality, and forecasting
objectives, can contribute to producing more realistic and reli-
able budget forecasts.

In conclusion, progress in the field of budget forecasting depends
less on developing increasingly complex models and more on
managing the existing methodological diversity in a systematic
and context‐sensitive manner. This study provides a compre-
hensive foundation for such efforts and aims to contribute to the
development of budget forecasting as both a science and an art.

References

Agostini, S. J. 1991. “Searching for a Better Forecast: San Francisco's
Revenue Forecasting Model.” Government Finance Review 7, no. 6:
13–16.

Alamdari, S. H., H. Khalizadeh, and A. Zayer. 2016. “Forecasting the
Iranian Tax Revenues: Application of Nonlinear Models.” Journal of
International Economics and Management Studies 1, no. 2: 21–48.

Alhassan, B. G., F. B. Yusof, and S. M. Norrulashikin. 2020. “Assimi-
lation of Principal Component Analysis and Wavelet With Kernel
Support Vector Regression for Medium‐Term Financial Time Series
Forecasting.” International Journal of Management and Humanities 4,
no. 7: 40–48.

Asher, M. G. 1978. “Accuracy of Budgetary Forecasts of Central Gov-
ernment, 1967‐68 to 1975‐76.” Economic and Political Weekly 13, no. 8:
423–432.

Asimakopoulos, S., Joan Paredes, and Thomas Warmedinger. “Fore-
casting Fiscal Time Series Using Mixed Frequency Data.” ECB Working
Paper No. 1550, 2013.

Auld, D. A. L. 1970. “Fiscal Marksmanship in Canada.” Canadian
Journal of Economics 3, no. 3: 507–511.

Baghestani, H., and R. McNown. 1992. “Forecasting the Federal Budget
With Time‐Series Models.” Journal of Forecasting 11, no. 2: 127–139.

Public Budgeting & Finance, 2025

15

---

<!-- PAGE 16 -->

Botrić, V., and M. Vizek. 2012. “Forecasting Fiscal Revenues in a
Transition Country: The Case of Croatia.” Zagreb International Review
of Economics & Business 15, no. 1: 23–36.

Favero, C. A., and M. Marcellino. 2005. “Modelling and Forecasting
Fiscal Variables for the Euro Area.” Oxford Bulletin of Economics and
Statistics 67, no. 1: 755–783.

Bretschneider, S. I., W. L. Gorr, G. Grizzle, and E. Klay. 1989. “Political and
Organizational Influences on the Accuracy of Forecasting State Govern-
ment Revenues.” International Journal of Forecasting 5, no. 3: 307–319.

Fedotov, D. Y. 2017. “Forecasting of Regional Economic Development
and Budget Based on the Example of Irkutsk Oblast.” Studies on
Russian Economic Development 28, no. 4: 416–422.

Bretschneider, S., and W. Gorr. 1992. “Economic, Organizational, and
Political Influences on Biases in Forecasting State Sales Tax Receipts.”
International Journal of Forecasting 7, no. 4: 457–466.

Frank, H. A. 1990. “Municipal Revenue Forecasting With Time. Series
Models: A Florida Case Study.” American Review of Public Administration
20, no. 1: 45–59.

Buxton, E. K., A. K. Kenneth, M. Cremeens, and K. Jay. 2019. “An Auto
Regressive Deep Learning Model for Sales Tax Forecasting From Mul-
tiple Short Time Series.” In 18th IEEE International Conference on
Machine Learning and Applications, 1359–1364. IEEE.

Campbell, J. E., M. E. Ogunsanya, N. Holmes, T. VanWagoner, and
J. James. 2024. “Bibliometric and Social Network Analysis of a Clinical
and Translational Resource Awardee: An Oklahoma Experience
2014–2021.” Journal of Clinical and Translational Science 8: e10.

Castelino, M. S., R. C. B. Belluzzo, J. P. Albino, and V. C. P. N. Valente.
2024. “Bibliometric Analysis: Literature Review and Proposal of a Meth-
odological Framework in 12 Steps.” Revista Aracê 6, no. 4: 13421–13446.
https://doi.org/10.56238/arev6n4-146.

Chatagny, F., and N. C. Soguel. 2012. “The Effect of Tax Revenue
Budgeting Errors on Fiscal Balance: Evidence From the Swiss Cantons.”
International Tax and Public Finance 19: 319–337.

Chimilila, C. 2017. “Forecasting Tax Revenue and Its Volatility in
Tanzania.” African Journal of Economic Review 5, no. 1: 84–109.

Chung, I. H., B. Kara, M. McShea, R. Pathak, and D. Williams. 2025.
“Using Large Language Models to Forecast Local Government Reve-
nue.” Public Finance Journal 2, no. 2: 85–98.

Chung, I. H., W. W. Daniel, and M. R. Do. 2022. “For Better or Worse?
Revenue Forecasting With Machine Learning Approaches.” Public
Performance & Management Review 45, no. 5: 1133–1154.

Cirincione, C., G. A. Gurrieri, and B. van de Sande. 1999. “Municipal
Government Revenue Forecasting: Issues of Method and Data.” Public
Budgeting & Finance 19, no. 1: 26–46.

Cooke, S., and C. McIntosh. 2011. “Forecasting General Fund Revenue: An
Analysis of Idaho FY 1998 to FY 2011.” Public Budgeting & Finance 31, no. 4:
51–73.

Cooksey, R. W. 2020. Descriptive Statistics for Summarising Data.
Springer Singapore.

Corvalão, E., R. W. Daniel, Samohyl, and G. H. Brasil. 2010. “Forecasting the
Collection of the State Value Added Tax (ICMS) in Santa Catarina: The
General to Specific Approach in Regression Analysis.” Brazilian Journal of
Operations & Production Management 7, no. 1: 105–121.

Damane, M. 2020. “Forecasting the Government of Lesotho's Budget: An
AR‐MIDAS Approach.” African Journal of Economic and Sustainable
Development 7, no. 3: 256–285.

Danninger, S. 2005. “Revenue Forecasts as Performance Targets.” IMF
Working Paper, 1–20. https://doi.org/10.5089/9781451860337.001.

Derrick, R. A. 2002. Better Revenue Forecasting: Is Fiscal Stress a Stim-
ulant? A Look at Nevada Local Governments. UNLV Theses, Disserta-
tions, Professional Papers, and Capstones.

Downs, G. W., and D. M. Rocke. 1983. “Municipal Budget Forecasting With
Multivariate ARMA Models.” Journal of Forecasting 2, no. 4: 377–387.

Frank, H. A., and A. G. Gerasimos. 1990. “Raising the Bridge Using
Time Series Forecasting Models.” Public Productivity & Management
Review 14, no. 2: 171–188.

Frank, H. A., and X. H. Wang. 1994. “Judgmental vs. Time Series Vs.
Deterministic Models in Local Revenue Forecasting: A Florida Case Study.”
Journal of Public Budgeting, Accounting & Financial Management 6, no. 4:
493–517.

Fullerton, T. M. 1989. “A Composite Approach to Forecasting State
the Idaho Sales Tax.”
Government Revenues: Case Study of
International Journal of Forecasting 5, no. 3: 373–380.

Ghysels, E., and N. Ozkan. 2015. “Real‐Time Forecasting of the US Federal
Government Budget: A Simple Mixed Frequency Data Regression
Approach.” International Journal of Forecasting 31, no. 4: 1009–1020.

Ghysels, E., and N. Ozkan. Real‐Time Predictions of the U.S. Federal
Government Budget: Expenditures, Revenues and Deficits. UNC
Kenan‐Flagler Research Paper, 2012.

Ghysels, E., F. Grigoris, and N. Özkan. 2022. “Real‐Time Forecasts of
State and Local Government Budgets With an Application to the
COVID‐19 Pandemic.” National Tax Journal 75, no. 4: 731–763.

Gianakis, G. A., and A. F. Howard. 1993. “Implementing Time Series
Forecasting Models: Considerations for Local Governments.” State &
Local Government Review 25, no. 2: 130–144.

Grizzle, G., and W. E. Klay. 1994. “Forecasting State Sales Tax Reve-
nues: Comparing the Accuracy of Different Methods.” State & Local
Government Review 26, no. 3: 142–152.

Hájek, P., and V. Olej. 2010. “Municipal Revenue Prediction by En-
sembles of Neural Networks and Support Vector Machines.” WSEAS
Transactions on Computers 9, no. 11: 1255–1264.

Jena, P. R. 2006. “Fiscal Marksmanship: Link Between Forecasting
Central Tax Revenues and State Fiscal Management.” Economic and
Political Weekly 41, no. 37: 3971–3976.

Khan, T., Anwar Hussain, and Z. K. M. 2018. “Fiscal Marksmanship in
Pakistan: With Special Focus on Province Khyber Pakhtunkhwa.”
Pakistan Journal of Economic Studies 1, no. 1: 21–43.

Koirala, T. P. 2012. “Government Revenue Forecasting in Nepal.” NRB
Economic Review 24, no. 2: 47–60.

Kong, D. 2007. “Local Government Revenue Forecasting: The California
County Experience.” Journal of Public Budgeting, Accounting &
Financial Management 19, no. 2: 178–199.

Krause, G. A., and J. K. Corder. 2007. “Explaining Bureaucratic Optimism:
Theory and Evidence From U.S. Executive Agency Macroeconomic Fore-
casts.” American Political Science Review 101, no. 1: 129–142.

Krol, R. 2010. Forecasting State Tax Revenue: A Bayesian Vector Auto-
regression Approach, 1–18. California State University, Department of
Economics.

Duncan, G., W. Gorr, and J. Szczypula. 1993. “Bayesian Forecasting for
Seemingly Unrelated Time Series: Application to Local Government
Revenue Forecasting.” Management Science 39, no. 3: 275–293.

Lahiri, K., and C. Yang. 2022. “Boosting Tax Revenues With Mixed‐
Frequency Data in the Aftermath of Covid‐19: The Case of New York.”
International Journal of Forecasting 38, no. 2: 545–566.

Erdoğdu, H., and R. Yorulmaz. 2019. “Comparison of Tax Revenue
Forecasting Models for Turkey.” In 34. International Public Finance
Conference, 482–492.

Larson, S., and M. Overton. 2024. “Modeling Approach Matters, But Not as
Much as Preprocessing: Comparison of Machine Learning and Traditional
Revenue Forecasting Techniques.” Public Finance Journal 1, no. 1: 29–48.

16

Public Budgeting & Finance, 2025

---

<!-- PAGE 17 -->

Larson, S., and M. Overton. 2025. “Is There a Gold Standard or Need for
a City‐Centric Approach for Sales Tax Revenue Forecasting.” Public
Finance Journal 2, no. 2: 99–120. https://doi.org/10.59469/pfj.2025.45.

Leal, T., J. J. Pérez, M. Tujula, and J. P. Vidal. 2008. “Fiscal Forecasting:
Lessons From the Literature and Challenges.” Fiscal Studies 29, no. 3:
347–386.

Otrok, C., and H. W. Charles. 1997. “What To Do When the Crystal Ball
Is Cloudy: Conditional and Unconditional Forecasting in Iowa.”
Proceedings. Annual Conference on Taxation and Minutes of the Annual
Meeting of the National Tax Association 90: 326–334.

Passas, I. 2024. “Bibliometric Analysis: The Main Steps.” Encyclopedia
4: 1014–1025.

Li‐xia, L., Z. Yi‐Qi, and X. Liu. 2011. “Tax Forecasting Theory and
Model Based on SVM Optimized by PSO.” Expert Systems With
Applications 38, no. 1: 116–120.

Pedregal, D. J., and J. J. Pérez. 2010. “Should Quarterly Government
Finance Statistics Be Used for Fiscal Surveillance in Europe?”
International Journal of Forecasting 26, no. 4: 794–807.

Li, W., Q. Xie, J. Ao, et al. 2025. “Systematic Review: A Scientometric
Analysis of the Status, Trends and Challenges in the Application of
Digital Technology to Cultural Heritage Conservation (2019–2024).” npj
Heritage Science 13. https://doi.org/10.1038/s40494-025-01636-8.

Litterman, R. B., and M. S. Thomas. 1983. “Using Vector Autoregres-
sions to Measure the Uncertainty in Minnesota's Revenue Forecasts.”
Federal Reserve Bank of Minneapolis Quarterly Review 7, no. 2: 10–22.

Liu, D., Rufei Zhang, and Jaun Li. 2011. “Tax Revenue Combination
Forecast of Hebei Province Based on the IOWA Operator.” In Fourth
International Joint Conference on Computational Sciences and Optimi-
zation, 516–519. IEEE.

Lu, S., Zhong‐jian Cai, and X.‐bin Zhang. 2009. “Application of GA‐
SVM Time Series Prediction in Tax Forecasting.” In 2nd IEEE Inter-
national Conference on Computer Science and Information Technology,
34–36. IEEE.

M. Khalifa, H., S. I. al‐Said, and S. Aboul Fotouh Saleh. 2024. “A Smart
Approach For Budget Deficits Prediction Under Economic Shocks.”
International Journal of Accounting and Management Sciences 3, no. 3:
276–308.

Pérez, J. J. 2007. “Leading Indicators for Euro Area Government Defi-
cits.” International Journal of Forecasting 23, no. 2: 259–275.

Rudzkis, R., and E. Mačiulaitytė. 2007. “Econometrical Modelling of
Profit Tax Revenue.” Nonlinear Analysis: Modelling and Control 12,
no. 1: 95–112.

Sabaj, E., and M. Kahveci. 2018. Forecasting Tax Revenues in an
Emerging Economy: The Case of Albania. University Library of Munich
MPRA Paper 84404.

Schroeder, L. 2007. “Forecasting Local Revenues and Expenditures.” In
Local Budgeting, edited by Anwar Shah, 53–79. World Bank.

Şengüler, H., and B. Kara. 2025. “Forecasting the Inflation for Budget
Forecasters: An Analysis of ANN Model Performance in Türkiye.”
Ekonomi Politika ve Finans Arastirmalari Dergisi 10, no. 1: 58–91.

Sexton, T. A. 1987. “Forecasting Property Taxes: A Comparison and
Evaluation of Methods.” National Tax Journal 40, no. 1: 47–59.

Shahnazarian, H., Martin Solberger, and E. Spanberg. 2017. “Forecast-
ing and Analyzing Corporate Tax Revenues in Sweden Using Bayesian
VAR Models.” Finnish Economic Papers 28, no. 1: 50–74.

Makananisa, M. P., and J. L. Erero. 2018. “Predicting South African
Personal Income Tax—Using Holt–Winters and SARIMA.” Journal of
Economics and Management 31, no. 1: 24–49.

Silvestrini, A., M. Salto, L. Moulin, and D. Veredas. 2008. “Monitoring
and Forecasting Annual Public Deficit Every Month: The Case of
France.” Empirical Economics 34: 493–524.

McDonald, B., S. Larson, C. Maher, et al. 2024. “Establishing an Agenda
for Public Budgeting and Finance Research.” Public Finance Journal 1,
no. 1: 9–28.

McNab, R., M. Rider, and K. Wall. Are Errors in Official U.S. Budget
Receipts Forecasts Just Noise? Andrew Young School of Policy Studies
Research Paper No. 07‐22, 2005.

McShea, M., and J. Cordes. 2019. “Forecasting Post‐Crisis Virginia Tax
Revenue.” In The Palgrave Handbook of Government Budget Forecasting,
by Daniel Williams and Thad Calabrese, 177–200. Palgrave Macmillan.

Molapo, M. A., J. O. Olaomi, and N. O. Ama. 2019. “Bayesian Vector
Auto‐Regression Method as an Alternative Technique for Forecasting
South African Tax Revenue.” Southern African Business Review 23: 1–28.

Mukherjee, S., and R. Bhattacharya. 2023. “Revenue Forecasting of
Corporate Income Tax (CIT) in India.” Indian Economic Review 58:
329–349.

Nandi, B. K., Muntasir Chaudhury, and G. Q. Hasan. 2015. “Univariate
Time Series Forecasting: A Study of Monthly Tax Revenue of Bangla-
desh.” East West Journal of Business and Social Studies 4: 1–28.

Nazmi, N., and H. L. Jane. Forecasting State Income Tax Receipts: A
Time Series Approach. BEBR Faculty Working Paper No. 1105, 1985.

Nazmi, N., and J. H. Leuthold. 1988. “Forecasting Economic Time
Series That Require a Power Transformation: Case of State Tax
Receipts.” Journal of Forecasting 7, no. 3: 173–184.

Ofori, M. S., Abel Fumey, and E. Nketiah‐Amponsah. 2020. “Forecast-
ing Value Added Tax Revenue in Ghana.” Journal of Economics and
Financial Analysis 4, no. 2: 63–99.

Onorante, L., D. J. Pedregal, J. J. Pérez, and S. Signorini. 2010. “The
Usefulness of Infra‐Annual Government Cash Budgetary Data for Fiscal
Forecasting in the Euro Area.” Journal of Policy Modeling 32, no. 1:
98–119.

Srinivasan, S., and P. Misra. 2020. “Grants From Centre and States'
Fiscal Marksmanship.” Indian Public Policy Review 2, no. 1: 65–83.

Steinnes, D., and S. Wong. Forecasting State Tax Revenues: A Simple
Alternative. Working Paper No. 85‐16, Bureau of Business and Eco-
nomic Research, 1985.

Streimikiene, D., R. Raheem Ahmed, J. Vveinhardt, S. P. Ghauri, and
S. Zahid. 2018. “Forecasting Tax Revenues Using Time Series
Techniques—A Case of Pakistan.” Economic Research‐Ekonomska
Istraživanja 31, no. 1: 722–754.

Thayyib, P. V., Muhammed Navas Thorakkattle, F. Usmani,
A. T. Yahya, and N. H. S. Farhan. 2023. “Forecasting Indian Goods and
Services Tax Revenue Using TBATS, ETS, Neural Networks, and Hybrid
Time Series Models.” Cogent Economics & Finance 11, no. 2: 1–23.

Ticona, W., K. Figueiredo, and M. Vellasco. 2017. “Hybrid Model Based
on Genetic Algorithms and Neural Networks to Forecast Tax Collec-
tion.” In XXIV International Conference on Electronics, Electrical En-
gineering and Computing (INTERCON), 1–4. IEEE.

Ünsal, H., A. Çalişkan, Deniz Koçak, and Yasin Ertürk. 2020. “Kamu
Mali̇ Yöneti̇mi̇ Kapsaminda çok Deği̇şkenli̇ gri̇ Tahmi̇n Modeli̇ i̇le Vergi̇
Geli̇rleri̇ Tahmi̇ni̇.” Mehmet Akif Ersoy Üniversitesi İktisadi ve İdari
Bilimler Fakültesi Dergisi 7, Özel Sayı: 1104–1120.

Voorhees, W. R. 2006. “Neural Networks and Revenue Forecasting: A
Smarter Forecast?” International Journal of Public Policy 1, no. 4:
379–388.

Willoughby, K., and H. Guo. 2008. “The State of the Art: Revenue
Forecasting in US State Governments.” In Government Budget Fore-
casting: Theory and Practice, edited by Jinping Sun and Thomas Lynch,
27–42. Taylor & Francis Group.

Wong (Jeffrey), C. H., and N. La. 2024. “Applying Machine Learning in
Tax Revenue Forecasting.” Victoria's Economic Bulletin 8, no. 2: 1–12.

Public Budgeting & Finance, 2025

17

---

<!-- PAGE 18 -->

Xie, H. 2024. “Research on the Models for Forecast of Tax Revenue of
Wenzhou City.” Highlights in Science, Engineering and Technology 88:
1043–1049.

Yang, C. H., T. Molefyane, and Y. D. Lin. 2023. “The Forecasting of a
Leading Country's Government Expenditure Using a Recurrent Neural
Network With a Gated Recurrent Unit.” Mathematics 11, no. 14: 3085.

Yılmaz, E. 2019. “Vergi Gelirlerinin Tahminlenmesine Yönelik Eko-
nometrik Model.” Vergi Dünyası 38, no. 449: 38–47.

Zakaria, M., and S. Ali. 2010. “Fiscal Marksmanship in Pakistan.”
Lahore Journal of Economics 15, no. 2: 113–133.

Zhang, Y. 2014. “Research on the Model of Tax Revenue Forecast of
Jilin Province Based on Gray Correlation Analysis.” In Sixth Interna-
tional Conference on Intelligent Human‐Machine Systems and Cyber-
netics, 30–33. IEEE.

Zhijun, Y. 2013. “RBF Neural Networks Optimization Algorithm and
Application on Tax Forecasting.” Indonesian Journal of Electrical
Engineering 11, no. 7: 3491–3497.

18

Public Budgeting & Finance, 2025

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| Public Budgeting |         | & Finance    |     |            |     |             |          |     |     |
| ---------------- | ------- | ------------ | --- | ---------- | --- | ----------- | -------- | --- | --- |
| ORIGINAL         | ARTICLE |              |     |            |     |             |          |     |     |
| A Comparative    |         | Analysis     |     | of Budget  |     | Forecasting |          |     |     |
| Methods:         |         | A Systematic |     | Literature |     | Review      | Covering |     |     |
–
| the | 1983 2024 | Period |     |     |     |     |     |     |     |
| --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Şengüler
| BeratKara | | Hasan |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
FacultyofPoliticalScience,IstanbulMedeniyetUniversity,Istanbul,Turkey
Correspondence:BeratKara(berat.kara@medeniyet.edu.tr)
| Received:11September2025 |     | | Revised:18October2025 |     | | Accepted:27October2025 |     |     |     |     |     |
| ------------------------ | --- | ----------------------- | --- | ------------------------ | --- | --- | --- | --- | --- |
Keywords:budgetforecasting|machinelearning|methodcomparison|performancemetrics|systematicreview
ABSTRACT
Thisstudysystematicallyanalyzes69peer‐reviewedworkscomparingbudgetforecastingmethods.Itexploresmethodological
evolution, geographic distribution, and evaluation trends. Four phases of development are identified: statistical methods,
diversification,machinelearning,anddeeplearning.Adivisionemergesbetweentraditionalandnext‐generationtechniques.
Geographically,43%ofstudiesfocusontheUnitedStates,whiledevelopingeconomiesremainunderrepresented.Inevaluation,
MAPE, RMSE, and MAE dominate, with directional errors largely neglected. Findings show that optimal method choice
dependsoncontext,supportingapluralistic,context‐sensitiveapproachratherthanuniversalrelianceonasingleforecasting
method.
(Botrić
1 | Introduction implementation of fiscal policy measures and Vizek
|     |     |     |     |     | 2012) | and the design | and execution | of sound fiscal | policies |
| --- | --- | --- | --- | --- | ----- | -------------- | ------------- | --------------- | -------- |
Public budgets, which lie at the core of fiscal management (Derrick 2002; Danninger 2005) depend critically on the
systems, function both as instruments of economic policy and accuracy of forecasts. Moreover, forecasts serve as key in-
as frameworks for managing public resources. The forecasts dicators for economic agents: various financial indicators,
used in budget preparation determine the government's future particularly interest rates, are influenced by these forecasts;
fiscal capacity, spending priorities, and economic orientation. householdsandfinancialmarketparticipantsbasetheirlong‐
The forecasting process is shaped by a wide range of factors, term decisions on them; and central banks that pursue
including macroeconomic indicators, political preferences, inflation targeting rely on such data to guide their policy
| institutional | capacity,        | and technical   | methodologies. | In this   | decisions. |     |     |     |     |
| ------------- | ---------------- | --------------- | -------------- | --------- | ---------- | --- | --- | --- | --- |
| respect,      | budget forecasts | go beyond being | a merely       | technical |            |     |     |     |     |
elementoffiscalplanning,constitutingastrategiccomponentof Accurateforecastsserveasafundamentaltoolfordetermining
thepolicy‐making process. the extent to which public services and programs can be
financed(Auld1970;Bretschneideretal.1989).Thesuccessof
This strategic position necessitates that budget forecasts be forecasting is particularly critical for the efficient financing of
preparedinarealistic,reliable,andaccuratemanner.Efficient large future public expenditures (Auld 1970), as multiyear ex-
allocation of scarce public resources and the successful coor- penditure forecasts represent an estimate of the cost of pro-
public–private
dination of sector planning are only possible viding a certain level of public service (Schroeder 2007).
through a budget process grounded in robust forecasts Furthermore, establishing a robust link between long‐term
(Krause and Corder 2007). Similarly, the timely and effective planning and implementation depends on the accuracy of
©2025PublicFinancialPublications,Inc.
| PublicBudgeting&Finance,2025;1–18 |     |     |     |     |     |     |     |     | 1   |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1111/pbaf.70008

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
approachesemergeinthisregard.Thefirstinvolvesidentifying
Summary
|     |     |     |     |     |     |       | the causes | of past | forecasting |     | errors and | developing |     | remedial |
| --- | --- | --- | --- | --- | --- | ----- | ---------- | ------- | ----------- | --- | ---------- | ---------- | --- | -------- |
| •   |     |     |     |     |     | peer‐ |            |         |             |     |            |            |     |          |
This study provides a systematic analysis of 69 mechanisms. This approach aims to eliminate recurring error
| reviewed         | studies | comparing     | budget | forecasting       |     | meth- |           |              |           |           |                 |     |                 |     |
| ---------------- | ------- | ------------- | ------ | ----------------- | --- | ----- | --------- | ------------ | --------- | --------- | --------------- | --- | --------------- | --- |
|                  |         |               |        |                   |     |       | patterns  | by examining |           | in detail | the structural, |     | institutional,  |     |
| ods, identifying |         | four distinct | phases | of methodological |     |       |           |              |           |           |                 |     |                 |     |
|                  |         |               |        |                   |     |       | economic, | and          | political | factors   | influencing     |     | the forecasting |     |
evolution from basic statistical models to the deep process. The second approach focuses on improving the meth-
learning era. ods and models used in the preparation of forecasts. Such
• Thefindingsrevealthatnosingleforecastingmethodis methodologicaladvancementencompassesboththerefinement
universally superior; instead, the optimal choice criti- ofexistingtechniquesandtheimplementationofnewmodeling
|       |         |               |         |      |        |      | approaches, | with | the | goal | of strengthening |     | the analytical |     |
| ----- | ------- | ------------- | ------- | ---- | ------ | ---- | ----------- | ---- | --- | ---- | ---------------- | --- | -------------- | --- |
| cally | depends | on contextual | factors | such | as the | eco- |             |      |     |      |                  |     |                |     |
nomic environment, data quality, and the forecast capacityofthe forecastingprocess.
horizon.
Theliteraturecontainsnumerousstudiesthatfocusonthesetwo
| • A significant |     | finding is | the pronounced |     | geographical |     |             |       |         |      |          |     |             |     |
| --------------- | --- | ---------- | -------------- | --- | ------------ | --- | ----------- | ----- | ------- | ---- | -------- | --- | ----------- | --- |
|                 |     |            |                |     |              |     | approaches. | These | studies | have | compared | the | performance | of  |
concentrationofresearch,with43%ofstudiesfocusedon
|            |         |         |             |               |     |     | various forecasting |     | techniques |          | across different |         | country | contexts |
| ---------- | ------- | ------- | ----------- | ------------- | --- | --- | ------------------- | --- | ---------- | -------- | ---------------- | ------- | ------- | -------- |
| the United | States, | leaving | forecasting | methodologies |     | in  |                     |     |            |          |                  |         |         |          |
|            |         |         |             |               |     |     | and datasets.       | The | models     | employed | range            | widely, | from    | simple   |
developingeconomiessubstantiallyunderrepresented.
|             |     |                       |     |      |          |     | time‐series    | methods | based    | on            | trend analysis | to         | complex | econo-     |
| ----------- | --- | --------------------- | --- | ---- | -------- | --- | -------------- | ------- | -------- | ------------- | -------------- | ---------- | ------- | ---------- |
| • The field | is  | further characterized |     | by a | hegemony | of  |                |         |          |               |                |            |         |            |
|             |     |                       |     |      |          |     | metric models, |         | and from | deterministic |                | approaches | to      | artificial |
certainperformancemetrics(MAPE,RMSE,andMAE), intelligence (AI) and machine learning (ML)‐based algorithms.
which, while allowing for comparison, largely neglect While simpler methods offer advantages such as ease of imple-
| the critical |     | policy dimension | of  | directional | forecast |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mentationandlowdatarequirements,morecomplextechniques,
errors. despite requiring greater computational power and extensive
• data sources, possess the potential to capture dynamic relation-
Consequently,thestudyadvocatesforashiftawayfrom
“ideal”
the quest for a single best model toward a more plu- ships. This diversity indicates that there is no single
ralistic, context‐sensitive, and potentially hybrid method for budget forecasting; rather, the choice of method
|            |                    |     |     |     |     |     | depends | on factors | such | as economic | conditions, |     | data | quality, |
| ---------- | ------------------ | --- | --- | --- | --- | --- | ------- | ---------- | ---- | ----------- | ----------- | --- | ---- | -------- |
| approachto | budgetforecasting. |     |     |     |     |     |         |            |      |             |             |     |      |          |
institutionalcapacity,andpolicypriorities.
|             |           |           |        |       |      |       | The existing |               | literature | does         | not provide |          | a homogeneous |           |
| ----------- | --------- | --------- | ------ | ----- | ---- | ----- | ------------ | ------------- | ---------- | ------------ | ----------- | -------- | ------------- | --------- |
|             |           |           |        |       |      |       | assessment   | of the        | success    | of methods   | used        | in       | budget        | forecast- |
| medium‐ and | long‐term | forecasts | (Asher | 1978; | Jena | 2006; |              |               |            |              |             |          |               |           |
|             |           |           |        |       |      |       | ing, due     | to variations |            | in datasets, | time        | periods, | countries,    | and       |
Zakaria and Ali 2010; Fedotov 2017). Having sufficient infor- modeltypes.Forecastsproducedacrossabroadspectrum,from
mation about available resources enables more effective man- simple time‐series techniques to complex ML approaches, ex-
agementoflong‐termprogramsandprojectswithinthebudget
|     |     |     |     |     |     |     | hibit varying | performance |     | in  | different | contexts. | This | situation |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | --- | --------- | --------- | ---- | --------- |
process, while careful evaluation of this information guides necessitatesasystematicevaluationofwhichmethodsperform
project and program selection, helping to determine what is betterunderspecificconditions.Suchanassessmentwouldnot
feasible in the medium term (Jena 2006). In this context, fore- onlycontributetotheadvancementofacademicknowledgebut
casts related to a country's key sectors provide a scientific also serve as a practical guide for institutions, policymakers,
foundationfor strategicplanning (Fedotov 2017). and analysts involved in the budget process regarding method
selectionandmodeldevelopment.Inresponsetothisneed,the
The realistic preparation of budget forecasts is also a critical present study offers a comprehensive review of the existing
prerequisite for the government to achieve its planned objec- literature, providing a comparative evaluation of different
tives(KhanandAnwarHussain2018;BretschneiderandGorr models andtechniques.
| 1992; Agostini | 1991). | As observed | in  | modern | economies, | a   |     |     |     |     |     |     |     |     |
| -------------- | ------ | ----------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
government's ability to respond effectively to any crisis is The critical need for advancing budget forecasting accuracy is
directlyinfluenced bythequality ofthefinancialinformation further underscored by recent large‐scale efforts to define the
available to it, and consequently, by the accuracy of forecasts research priorities for the entire field of public budgeting and
agenda‐setting
(Willoughby and Guo 2008). In other words, the success of finance. In a comprehensive study, McDonald
forecasting shapes public perception regarding the effective- et al. (2024) engaged a wide community of academics and
ness of a government's fiscal policy (Leal et al. 2008). There- practitioners to identify the most pressing research needs.
ranked‐choice
fore, major errors in budget forecasting negatively affect the Notably, their findings, derived from a voting
|     |     |     |     |     |     |     |     |     | “Data |     | Methods” |     | top‐tier |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | --- | -------- | --- |
outcomes of governmental programs and policies, potentially process, highlighted and as a priority,
leading to policy failure (Srinivasan and Misra 2020). explicitly calling for research that improves “the accuracy of
Accordingly, it can be argued that forecast accuracy plays a forecasting.”
|     |     |     |     |     |     |     | budget | and revenue |     |     | This | consensus | positions |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | --- | ---- | --------- | --------- | --- |
significantroleinthebudgetarypolicyprocessbycontributing methodologicalinvestigations,suchasthepresentstudy,atthe
to transparency, accountability, and fiscal discipline (McNab forefront of the field's agenda. Our systematic review directly
et al. 2005). addressesthiscallbysynthesizingthecomparativeperformance
four‐decade
|     |     |     |     |     |     |     | of a wide | array | of forecasting |     | techniques | over | a   |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | -------------- | --- | ---------- | ---- | --- | --- |
Asanaturalconsequenceofthisstrategicimportance,effortsto period. By doing so, this study aims not only to contribute to
enhance the accuracy of budget forecasts have remained a academic knowledge but also to provide a practical, evidence‐
continuous focus in the field of public finance. Two principal based guide for practitioners in selecting and developing
| 2   |     |     |     |     |     |     |     |     |     |     | PublicBudgeting&Finance,2025 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
forecastingmodels,therebybridgingthegapbetweenacademic instance,variousvariantsofartificialneuralnetworks(ANNs),
inquiryandtheoperationalneedsidentifiedbythecommunity evenwhenlabeledwithdifferentprefixesintheoriginalstudies,
ofpractice. were grouped under the ANN category in the dataset. This
|                                                         |             |           |            |           |     | standardization | enables | accurate | and meaningful |     | comparisons |
| ------------------------------------------------------- | ----------- | --------- | ---------- | --------- | --- | --------------- | ------- | -------- | -------------- | --- | ----------- |
| Thepaperisstructuredasfollows.First,thedatasetusedinthe |             |           |            |           |     | acrossmethods.  |         |          |                |     |             |
| analysis is                                             | introduced, | detailing | its scope, | coverage, | and | key             |         |          |                |     |             |
characteristics. Second, the methodology is explained. Third, The primary motivation for constructing this dataset is to en-
the state of the literature on budget forecasting methods is ex- ableanobjectiveevaluationofthecomparativeperformanceof
amined, with a focus on comparative findings and methodo- budget forecasting methods and to conduct a systematic anal-
logicaldiversity.Finally,theconclusionsectionsummarizesthe ysisoffindingsintheliterature.Inthisway,thestudyaimsto
mainfindingsandoutlinesimplicationsforfutureresearchand provide clearer and more reliable insights into the conditions
policydesign. under which different methods yield superior results, both for
|          |     |     |     |     |     | theacademic | community | andforpractical |     | applications. |     |
| -------- | --- | --- | --- | --- | --- | ----------- | --------- | --------------- | --- | ------------- | --- |
| 2 | Data | Set |     |     |     |     |             |           |                 |     |               |     |
|          |     |     |     |     |     | 3 | Methods |           |                 |     |               |     |
Thedatasetconstructedinthisstudyencompassestheacademic
literature in which budget forecasting methods have been The purpose of this study is to examine the distribution, tem-
comparatively evaluated. In creating the dataset, a series of poral trends, and interrelationships of methods and metrics
selectioncriteriawasestablishedtoclearlydefinethescopeand employed in the budget forecasting literature. While classical
peer‐
ensure comparability. First, only articles published in bibliometric analyses are typically conducted through citation
|     |     |     |     |     |     |     | co‐authorship |     |     |     | co‐ |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
reviewed journals, books, book chapters, and scientific confer- networks, collaborations, or journal
ence proceedings were included. This choice aims to ensure occurrencemapping(Passas2024),thisstudyadoptsadifferent
thatthemethodsemployedandtheresultsobtainedhavebeen perspective. Instead of focusing on citation relationships or
scrutinized according to academic standards and are highly collaborative networks, the analysis emphasizes the frequency
reliable. Reports, technical notes, or institutional assessments of method applications, the prevalence of metric preferences,
that have not undergone a peer‐review process were excluded thecharacteristicsoftrainingdatasets,thelengthofforecasting
from thedataset. horizons, and the interconnections among methods. Thus,
|     |     |     |     |     |     | although | the research | shares | certain | features | with biblio- |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ------ | ------- | -------- | ------------ |
Second,sincethefocusofthisstudyisonmethodcomparison, metrics, it is primarily designed within the framework of sta-
budget forecasting studies that employ only a single method tistical analysis and network analysis. The analytical process
were not included. The dataset consists of research in which consists of three stages: (i) descriptive statistical analysis, (ii)
multiple forecasting methods were applied within the same trend analysis, and(iii)network analysis.
| study and           | their performance |     | compared. This  | approach    | allows |                   |     |             |          |     |     |
| ------------------- | ----------------- | --- | --------------- | ----------- | ------ | ----------------- | --- | ----------- | -------- | --- | --- |
| for the direct      | observation       |     | and analysis of | performance |        | differ-           |     |             |          |     |     |
| encesacrossmethods. |                   |     |                 |             |        | 3.1 | Descriptive |     | Statistical | Analysis |     |     |
Third, it was not sufficient for the included studies to provide Descriptive statistical analysis aims to summarize the funda-
onlyforward‐lookingforecasts;theseforecastswererequiredto mental characteristics of collected data and provide an overall
be compared with actual outcomes for thecorresponding peri- frameworkfortheresearchfield(Cooksey2020).Suchanalyses
ods. Studies that did not perform such comparisons were ex- are frequently used in bibliometric studies to reveal the quan-
cluded from the dataset, as they could not objectively titativestructureoftheliterature(Castelinoetal.2024).Inthis
demonstrate the success of the forecasting methods. This study, descriptive analyses include the frequency of method
requirement is critical for ensuring a robust assessment of applications, the annual distribution of publications, the geo-
(country‐level)
methodological performance, which constitutes the primary graphical distribution of research, the extent of
motivation ofthestudy. metricpreferences,andthelengthofforecastinghorizons.The
|     |     |     |     |     |     | findings | are visualized | through | graphs, | offering | a general |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | ------- | ------- | -------- | --------- |
In some studies, forecasts cover both past periods, for which overviewofmethodological diversity intheliterature.
| actual outcomes | are | available, | and future | periods, | which | have |     |     |     |     |     |
| --------------- | --- | ---------- | ---------- | -------- | ----- | ---- | --- | --- | --- | --- | --- |
notyetoccurred.Insuchcases,onlytheperiodswithavailable
|             |               |     |                 |              |     | 3.2 | Trend | Analysis |     |     |     |     |
| ----------- | ------------- | --- | --------------- | ------------ | --- | ----------- | -------- | --- | --- | --- | --- |
| actual data | were included |     | in the dataset. | For example, |     | in a        |          |     |     |     |     |
studywitha10‐yearforecastinghorizonwhereactualoutcomes
areavailableforonlythefirstfiveyears,thedatasetrepresents Trend analysis is a method used to examine temporal changes
onlythefive‐yearsegment.Thisapproachensuresthatmethod
inagivenphenomenonandtoidentifyunderlyingpatterns.Itis
performanceis measured solelyover verifiableperiods. frequently employed to illustrate the evolution of research
|     |     |     |     |     |     | domains | and methodological |     | transformations, |     | thereby con- |
| --- | --- | --- | --- | --- | --- | ------- | ------------------ | --- | ---------------- | --- | ------------ |
Finally, terminological consistency was maintained in the tributing to the understanding of the developmental trajectory
namingofmethodswithinthestudy.Indifferentstudies,minor ofafield(Li2025).Inthisstudy,trendanalysiswasconducted
variations in model structure or configuration often led to the to investigate the intensity of method applications over time.
same method being referred to by different names; in the da- The results were visualized with line graphs, highlighting
taset, these were consolidated under a single heading. For methodsthat gained prominenceduring different periods.
PublicBudgeting&Finance,2025 3

3.3 | Network Analysis such as LSTM networks and XGBoost have been incorporated
into the forecasters' toolkit (e.g., Yang et al. 2023; M. Khalifa
Networkanalysisisapowerfulmethodforexaminingstructures et al. 2024). At the same time, hybrid models and innovative
composed of nodes (e.g., methods, authors, or metrics) and approaches such as MIDAS, which address the issue of fre-
edges that represent the connections among them. This quencymismatch(GhyselsandOzkan2012,2015),havegained
approach is widely used to investigate the structural char- prominence in performance comparisons. This evolution dem-
acteristics and methodological diversity of scientific domains onstrates that researchers have not only sought to improve
(Campbell et al. 2024), offering valuable insights into the in- traditional methods but have also pushed the boundaries of
teractions amongdifferentcomponents ofthe literature. forecasting accuracy by leveraging data abundance and ad-
vancesin computational power.
In this study, network analysis was performed using Gephi
software, resulting in three distinct network structures: The expansion in geographical coverage is also noteworthy.
method–method, method–year, and method–metric relation- Whereas early studies were almost entirely United States‐
ships. Nodes represented methods, years, and metrics, while centered, recent years have witnessed significant contributions
edges denoted their co‐occurrences. This analysis enabled the from a wide range of economies, including China, Turkey,
visualization of which methods were prominent in specific Brazil, South Africa, India, and numerous Eastern European
periods, which metrics they were evaluated with, and which countries, as illustrated in Table 1. This diffusion underscores
methodstended to beemployed jointly. thatbudgetforecastingisauniversalissueinpublicfinanceand
highlights that method performance may vary across different
economic structures, institutional arrangements, and levels of
4 | Results data quality.
The table below provides a comprehensive summary of em- Therefore,thefindingsintheliteraturearenothomogeneous;a
piricalstudiesonbudgetforecastingmethods.Itsystematically methodthatdeliversthe“best”performanceinonecountryor
classifies results based on different country contexts, data fre- period may yield only modest results in another context. This
quencies, time periods, and types of methods, thereby high- heterogeneity further underscores the need for a systematic
lightingtherelativeperformanceofvariousapproaches.Inthis assessment of which methods perform better under specific
way, the fragmented findings in the literature regarding the conditionsandreinforcestheprimarymotivationofthisstudy.
successofbudgetforecastingmethodscanbeevaluatedfroma
holistic perspective, allowing for a comparative assessment of First, the distribution and frequency of forecasting methods
which methods perform better or worse under specific condi- employed in the comparative studies under review were ana-
tions. Within this framework, the table not only serves as an lyzed over time. This analysis provides an objective lens
inventory of previous research but also makes methodological through which to observe the evolution of methodological
diversityandperformancedifferences,centraltothemotivation trends, technological capabilities, and academic interest in the
of this paper, explicit, laying the groundwork for subsequent budget forecasting literature. Such a historical perspective is
analyses. crucial for understanding whichmethods dominatedin partic-
ularperiods,howthepopularityofspecificmodelshasshifted,
Academic interest in the comparative performance of budget and when pioneering contributions introduced innovations to
forecasting methods has shown a steady and remarkable thefield.
increase over the past four decades. The reviewed literature
reveals not only a numerical growth in studies but also a sig- The analysis of Figure 1 demonstrates that the methodological
nificant evolution in terms of scope, methodology, and geo- trajectoryofthebudgetforecastingliteraturecanbecharacterized
graphicaldiversity.Earlycontributions(e.g.,DownsandRocke as a four‐stage evolution. The first stage, emerging in the 1980s,
1983; Litterman and Thomas 1983) were largely confined to was dominated by basic statistical methods. During this period,
advancedeconomies(particularlytheUnitedStates)andrelied traditional time series and econometric models such as ARIMA,
primarily on relatively simple time‐series models (ARMA and VAR, and various regression techniques constituted the main
ARIMA).Overtime,however,researchhasexpandedtoinclude focus of academic studies. In subsequent years, greater diversifi-
developing countries as well as far more complex econometric cationandsophisticationinmodelingtechniquesbecameevident,
and AI‐based models. Thisexpansion is a clear indication that with more complex and theoretically grounded approaches such
thepursuitofgreaterforecastingaccuracyhastakenonaglobal asBVAR,ECM,andMIDASbeingintroduced.Thisphasemarked
and interdisciplinary character. Table 1 provides a systematic aperiodinwhichresearcherssoughttoenhanceforecastingpower
summary of this rich anddynamic body ofwork, detailing the by making model structures more dynamic and by integrating
scope,methods,andkeyfindingsofthe68comparativestudies differenttypesofdata.Bythe2010s,anotablemethodologicalshift
that form thebasisof thepresent analysis. had occurred: ML algorithms such as ANN and SVM began to
feature regularly in the literature, bringing an interdisciplinary
From a methodological perspective, the literature exhibits a dimensiontothefield.Thistransitionwasdrivenbythegrowing
clear trend toward increasing complexity and diversity. While availabilityoflargedatasets,advancesincomputationalcapacity,
the 1980s and early 1990s were dominated by classical econo- and increasing interest in modeling nonlinear relationships.
metricapproaches suchas ARIMA,VAR,andECM, the2000s Finally, since the 2020s, the literature has entered the era of DL
markedtheentryofMLanddeeplearning(DL)algorithmsinto and hybrid models. Cutting‐edge algorithms such as LSTM and
thefield.ANN,SVM,and,morerecently,cutting‐edgemethods XGBoosthavebecomefrequentlytestedincomparativeanalyses.
4 PublicBudgeting&Finance,2025
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

.gnitsaceroftegdubnisledomfoecnamrofrepevitarapmocehtnoweivererutaretiL
|
1ELBAT
)s(cirteM
tsroW
tseB
sdohteM
.rep.roF
.qerf
.sbO
RYT
OT
yrtnuoC
)s(rohtuA
enoN
WR
AMRA
WR;AM;AMRA
9791−6491
launnA
8791–6491
16
ASU
)3891(
ekcoRdnasnwoD
EP;EAM
CFO
FOC
CFO;FOC
;RAV
2891–1791
ylretrauQ
2891−7691
46
ASU
dna
namrettiL
)3891(samohT
ESMR
RGR
AMRA
RGR;AMRA
3891–1891
ylretrauQ
0891–0791
44
ASU
)5891(enaJdnaimzaN
EP
RAV
AMIRA
RAV;AMIRA
4891–3891
ylhtnoM
4891–0791
651
ASU
)5891(gnoWdnasennietS
ESM
tfirD
FOC
FOC
;tfirD
;AMIRA
3891–0891
launnA
0891–4791
264
ASU
)7891(notxeS
EM
;EAM;ESMR
RGR
AMIRA
AMIRA
;RGR
2891–1891
ylretrauQ
0891–0791
44
ASU
)8891(
dlohtueLdnaimzaN
EP
;ESMR
AMIRA
FOC
CFO;FOC
;AMIRA
5891–2891
ylretrauQ
1891–8791
61
ASU
)9891(notrelluF
EPAM
tiFevruC
AM
tiFevruC
;AMIRA
;WH;SE
;AM
6891
ylhtnoM
5891–2891
84
ASU
)0991(knarF
;EPAM;ESMR
CFO
WH
CFO;FOC
;FAG
;WH
;SE;AM
8891
ylhtnoM
7891–3891
06
ASU
)0991(somisareGdnaknarF
EP;EPA
ESMR
;EAM;EM
RAV
AMIRA
CFO;MCE
;RAV
;AMIRA
7891–0891
ylretrauQ
9791–5591
001
ASU
dna inatsehgaB )2991(nwoNcM
EPM
;EPAM
FKSM
FKSM‐C
FKSM‐C;FKSM
6891–9791
launnA
6891–2791
006
ASU
)3991(.latenacnuD
EPAM
WH
AMIRA
;SE;WH
;AM
;RGR
0991
ylhtnoM
0991–3891
27
ASU
dnasikanaiG
;FAG
;AMIRA
)3991(
drawoH
EPAM
RGR
SE
;SE
;RGR
2991–0991
launnA
2991–5791
81
ASU
)4991(gnaWdnaknarF
EPAM
AM
tiFevruC
;RGR
;SE;naeM
;AM
;FCOL
5891–0891
launnA
5891–5791
007
ASU
)4991(yalK
dnaelzzirG
tiFevruC
EAM
;ESMR
CFO
RAVB
CFO;RAVB
7991–0991
ylretrauQ
7991–3891
85
ASU
)7991(selrahCdna
kortO
EPAM
AM
SE
;RGR
;AMIRA;SE
;AM
6991–5991
noM
,auQ
6991–0991
99
ASU
)9991(.la
teenoicniriC
EAM
;ESMR
MCM
;RAV
AMRA
FOC
;MCM;MCS
;RAV;AMRA
2002–6991
launnaiB
5991–1891
03
lenaP
dnaorevaF
)5002(onillecraM
EP
NNA
CFO
;NNA
CFO
;NNA
0002–5991
ylretrauQ
0002–5791
401
ASU
)6002(seehrooV
EPAM
naeM
RGR
naeM
;tfirD
;TRL;RGR;CFO
1002–5991
launnA
1002–5891
71
ASU
)7002(gnoK
ESMR
WR
FOC
CFO
;WR;FOC;RGR
3002–4991
ylretrauQ
3002–0791
631
lenaP
)7002(zeréP
EPAM
MCE
RGR
MCE
;RGR
5002–3002
ylretrauQ
5002–8991
82
ainauhtiL
dnasikzduR
)7002(ėtytialuičaM
;ESMR
CFO
AMIRA
CFO;AMIRA
4002–2002
ylhtnoM
4002–6991
801
ecnarF
)8002(.lateinirtsevliS
EPAM;EAM
EP
CFO
AMIRA
CFO;AMIRA
6002–9791
launnA
6002–5491
26
dnalreztiwS
)2102(leugoSdnayngatahC
EPAM
NNA
MVS
MG
;MVS
;NNA
1002–9991
launnA
8991–0991
9
anihC
)9002(
.lateuL
)seunitnoC(
PublicBudgeting&Finance,2025 5
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on [27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by the
applicable
Creative
Commons
License

)deunitnoC(
|
1ELBAT
)s(cirteM
tsroW
tseB
sdohteM
.rep.roF
.qerf
.sbO
RYT
OT
yrtnuoC
)s(rohtuA
ESMR
WR
XIM
WR
;XIM
7002–1002
,nnA
7002–4891
882
lenaP
)0102(
zeréPdnalagerdeP
noM
,auQ
EPAM
AMIRA
MCE
AMIRA;MCE
1002
ylhtnoM
1002–5991
58
lizarB
)0102(.la
teoãlavroC
ESRR;EAR
RGR
MVS
;RGR;MVS
;NNA
6002–3002
launnA
6002–3002
8081
aihcezC
)0102(jelOdna
kejáH
ESMR
WR
RAVB
WR;RAVB;RAV
9002–4002
ylretrauQ
3002–9791
001
ASU
)0102(lorK
MD
;ESMR
WR
XIM
WR;MCE;XIM
;RA
6002–4991
ylhtnoM
6102–3691
273
lenaP
)0102(.la
teetnaronO
EAM
;ESMR
tfirD
FOC
CFO
;tfirD;FOC;WH
;AMIRA
1102–8991
launnA
7991–0791
82
ASU
)1102(
hsotnIcMdnaekooC
EPAM
SE
FOC
FOC
;SE
;MG
9002–9991
launnA
9002–9991
11
anihC
)1102(gnahZ
iefuRdnauiL
EPAM
NNA
MVS
MVS
;NNA
3002–3991
launnA
9991–0991
01
anihC
)1102(.la
teaix‐iL
EPAM
RGR
;AMIRA
MCE
;WR
MCE
;RGR;AMIRA
;WR
;tfirD
8002–7002
ylretrauQ
8002–5991
001
aitaorC
)2102(keziVdna
ćirtoB
ESMR
RA
SADIM
FOC;LDA
;RA
;SADIM
1102–0991
ylretrauQ
1102–8691
671
ASU
)2102(
nakzOdnaslesyhG
EPM
;EPAM
WH
AMIRAS
tfirD;AMIRAS
;RGR
;WH
2102–7991
ylhtnoM
2102–7991
291
lapeN
)2102(
alarioK
ESMR
naeM
SADIM
CFO
;naeM
;SADIM
1102–8002
ylretrauQ
2102–1991
611
lenaP
naoJdnasoluopokamisA
)3102(sederaP
EPSM
;EPAM
AMRA
NNA
MVS;AMRA
;NNA
1102–8002
launnA
1102–0891
23
anihC
)3102(nujihZ
EMR
;ESMR
CFO
MVS
CFO
;MVS
2102–0891
launnA
2102–0891
33
anihC
)4102(gnahZ
ESMR
RA
SADIM
FOC;LDA
;RA
;SADIM
2102–3991
launnA
2102–6591
75
ASU
)5102(
nakzOdnaslesyhG
EPAM;ESM;EPM
AMIRAS
AMSWH
;AMSWH;AMIRAS
3102–4002
ylhtnoM
2102–4002
101
hsedalgnaB
risatnuMdnaidnaN
CFO;AASWH
)5102(yruhduahC
ESMR
enoN
enoN
NNA
9002–7002
launnA
6002–3691
44
narI
)6102(.la
teiradmalA
EAM
;ESMR
AM
FOC
AM
;HCRAG;FOC;AMRA
5102–4102
ylhtnoM
5102–0002
281
ainaznaT
)7102(
alilimihC
ESMR
;EAM;EM
XAMIRA
RAVB
XAMIRA
;SADIM;RAVB
4102–0102
ylretrauQ
4102–3991
011
nedewS
nitraMdnanairazanhahS
)7102(regrebloS
ER;EPAM
CFO
FOC
CFO;FOC
;LAG
;NNA
4102–3102
ylhtnoM
2102–0002
441
lizarB
)7102(.late
anociT
;EAM;ESMR
;EM
AMIRAS
WH
RGR
;AMIRAS
;WH
7102–5102
ylretrauQ
7102–9002
63
acirfAhtuoS
dnaasinanakaM
ESAM;EPM
)8102(orerE
;ESMR
CFO
FOC
;RAVB;RAV
;MCE;WH
;WR
5102–1102
ylretrauQ
6102–5002
55
ainablA
)8102(icevhaKdna
jabaS
EPAM;EAM
CFO;FOC
;AMIRAS
;ESMR
RA
AMIRA
RAV
;AMIRA
;RA
7102
ylhtnoM
6102–5891
873
natsikaP
)8102(.la
teeneikimiertS
EPAM;EAM
EPAM
AMIRA
PLM
MTSL
;PLM;AMIRA
8102–5102
ylretrauQ
8102–9991
077
ASU
)9102(.la
tenotxuB
)seunitnoC(
6 PublicBudgeting&Finance,2025
15405850,
0, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles are
governed
by the applicable
Creative
Commons
License

)deunitnoC(
| 1ELBAT
)s(cirteM
tsroW
tseB
sdohteM
.rep.roF
.qerf
.sbO
RYT
OT
yrtnuoC
)s(rohtuA
;EAM;ESMR
WR
STAB
CFO;STAB
;AMIRAS
;WR
8102–5102
ylhtnoM
4102–6002
801
eyikrüT
dna
udğodrE
;EM;EPAM
)9102(zamluroY
ESAM;EPM
;ESMR
WR
RAVB
WR;RAVB
;RAV
;RA
4102–9002
launnA
8002–7791
23
ASU
)9102(sedroCdnaaehScM
EPAM;EAM EAM
;ESMR
AMIRA
SE;RAVB
SE;AMIRA;RAVB
5102–2102
ylretrauQ
2102–8991
65
acirfAhtuoS
)9102(.la
teopaloM
EPM
CFO
AMIRA
CFO;AMIRA
7102–5102
ylhtnoM
4102–6002
801
eyikrüT
)9102(zamlıY
;EAM;EPAM
;RVSK‐W
‐ACP
;RVSK‐ACP;RVSK‐W
;RVSK
9102–7102
ylretrauQ
6102–1891
441
airegiN
)0202(.la
tenassahlA
ESMR
;ESM
RVSK‐ACP
RVSK‐W
RVSK‐W‐ACP
;ESMR
CFO
SADIM‐RA
CFO
;SADIM‐RA
7102–6102
ylretrauQ
6102–3991
29
ohtoseL
)0202(enamaD
EPAM;EAM EPAM
;ESMR
WH
AMIRA
WH ;AMIRA
9102–7102
ylhtnoM
6102–2002
081
anahG
lebA
dnairofO
)0202(yemuF
enoN
CFO
MG
CFO
;MG
9102–7102
launnA
6102–6002
11
eyikrüT
)0202.la
telasnÜ
ESM;EPAM
TRAC
AMIRA
;NNA
;AMIRA;SE
;AM
4102–4991
launnA
4102–4991
611
ASU
)2202(.la
tegnuhC
TRAC;NNK
ESMR
WR
SADIM
WR
;FOC;LDA
;RA
;SADIM
8102–9991
launnA
2102–8591
14
ASU
)2202(.la
teslesyhG
;EAM;ESMR
WR
BGC
CFO;BGC;WR;OSSAL;SADIM
1202–0202
noM
,auQ
1202–6002
471
ASU
)2202(gnaYdnairihaL
EPAM
;EPM
ESMR;EPAM
AMIRAS
RAV
AMIRAS
;RAV
3202–1202
ylretrauQ
3202–1102
94
tarahB
dnaeejrehkuM
)3202(ayrahcattahB
;ESMR
NNA
FOC
FOC
;NNA;SE
;STABT
2202–1202
ylhtnoM
2202–7102
44
tarahB
)3202(.late
biyyahT
EPAM;EAM
;EAM
AMIRA
URG
;TSOOBGX
;RVS;STE
;AMIRA
0202–5102
launnA
0202–0991
13
lenaP
)3202(.lategnaY
EPAM
;ESMR
;NNRiB;MTSL;NNC
URG ;NNRSA
;EPAM
seyaBevïaN
MTSL
;TSOOBGX
;FR;MTSL;AMIRA
3202–9102
auQ,nnA
3202–9102
02
tpygE
)4202(.la
teafilahK.M
ESMR
;ESM
seyaBevïaN
;NNK
EPAM
naeM
;NNA
;TRL;NNK
;NNA
;NNK;SE
;AMIRA
7102–6102
,nnA
5102–1991
5001
ASU
)4202(notrevOdnanosraL
tfirD
;naeM
;FCOL;TRL
;TSOOBGX
noM
,auQ
tfirD
EPAM;EAM
RLM
NNA
NNA
;RLM
1202–9102
launnA
1202–2002
03
anihC
)4202(eiX
EAM
;ESMR
RGR
OSSAL
;RA
;RGR;OSSAL;FR
;WR
;RA
9102–9002
ylretrauQ
9002–2991
17
ailartsuA
)4202(
aLdnagnoW
NNA
;TSOOBGX
)seunitnoC(
PublicBudgeting&Finance,2025 7
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by Berat
Kara
- Istanbul
Medeniyet
University
, Wiley Online
Library
on [27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the applicable
Creative
Commons
License

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
larueNtnerruceRlanoitceridiB,NNRiB;noitamrofsnarTxoC–xoBhtiwledoMecapSetatSgnihtoomSlaitnenopxE,STAB;krowteNlarueNtnerruceRlaitneuqeSdesaB‐noitnettA,NNRSA;egarevA‐gnivoMevissergerotuA,AMRA;stupnI larueNlanoitulovnoC,NNC;retliFnamlaKetatS‐itluMdetsujdAyllanoitceS‐ssorC,FKSM‐C;gnitsooBtneidarGesiW‐tnenopmoC,BGC;eerTnoissergeRdnanoitacifissalC,TRAC;noissergerotuArotceVnaiseyaB,RAVB;krowteN yarG,MG;yticitsadeksoreteHlanoitidnoCevissergeRotuAdezilareneG,HCRAG;smhtiroglAciteneG,LAG;gniretliFevitpadAlareneG,FAG;gnihtoomSlaitnenopxE,SE;noitcerroCrorrE,MCE;stsaceroFfogninibmoC,FOC;krowteN evitiddAlanosaeSretniW‐tloH,AASWH;hcaorppAevitacilpitluMlanosaeSretniW‐tloH,AMSWH;sretniW‐tloH,WH;doirePdetsaceroF,.rep.roF;tinUtnerruceRdetaG,URG;krowteNlarueNnoissergeRdezilareneG,NNRG;ledoM larutcurtSyrtnuoC‐itluM,MCM;egarevAgnivoM,AM;krowteNyromeMmreTtrohSgnoL,MTSL;dnerTraeniL,TRL;drawroFdeirraCnoitavresbOtsaL,FCOL;rotarepOnoitceleSdnaegaknirhSetulosbAtsaeL,OSSAL;hcaorppA ,RVS;enihcaMrotceVtroppuS,MVS;ledoMlarutcurtSyrtnuoC‐elgniS,MCS;egarevAgnivoMdetargetnIevissergerotuAlanosaeS,AMIRAS;klaWmodnaR,WR;noissergeR,RGR;tseroFmodnaR,FR;sisylanAtnenopmoClapicnirP ,RAV;egnarsraeys'atadgniniarT,RYT;ledomehtniartotdesusnoitavresbolatoT,OT;stnenopmoClanosaeSdnadnerT—srorrEAMRA—noitamrofsnarTxoC–xoB—ytilanosaeScirtemonogirT,STABT;noissergeRrotceVtroppuS Inparticular,theemergenceofcomplexhybridmodelssupported
suonegoxEhtiwegarevAgnivoMdetargetnIevissergeRotuA,XAMIRA;egarevAgnivoMdetargetnIevissergerotuA,AMIRA;evissergerotuA,RA;krowteNlarueNlaicifitrA,NNA;gaLdetubirtsiDdetnemguA,LDA:snoitaiverbbA ,ACP;ycneuqerFnoitavresbO,.qerf.sbO;stsaceroFlaiciffO,CFO;retliFnamlaKetatS‐itluM,FKSM;noissergeRraeniLelpitluM,RLM;nortpecrePreyaL‐itluM,PLM;ycneuqerF‐dexiM,XIM;gnilpmaSataD‐dexiM,SADIM;ledoM
byPCArepresentsanewstageinwhichresearchersstrategically
|     | combine | feature | engineering | with | advanced | algorithms |     | to maxi- |
| --- | ------- | ------- | ----------- | ---- | -------- | ---------- | --- | -------- |
)s(cirteM
EPAM EPAM EPAM
mizemodelperformance.
|     | The overall | assessment | of        | this methodological |             | evolution |      | reveals  |
| --- | ----------- | ---------- | --------- | ------------------- | ----------- | --------- | ---- | -------- |
|     | that the    | field of   | budget    | forecasting         | is not      | static    | but  | rather a |
|     | dynamic     | area of    | research, | constantly          | interacting |           | with | develop- |
tehporP;MTSL ments in neighboring disciplines such as econometrics, opera-
naeM
AMIRA tions research, and AI. The journey from simple time‐series
tsroW
|     | models to | complex | neural | networks | reflects | both | the methodo- |     |
| --- | --------- | ------- | ------ | -------- | -------- | ---- | ------------ | --- |
;NNA
|     | logical maturity |             | and the accumulated |          | intellectual |       | capital        | of the |
| --- | ---------------- | ----------- | ------------------- | -------- | ------------ | ----- | -------------- | ------ |
|     | field. At        | the same    | time,               | however, | the          | dense | methodological |        |
|     | diversity        | illustrated | in Figure           |          | 1 suggests   | the   | presence       | of a   |
FCOL “methodologicalinflation”intheliterature,aphenomenonthat
AMIRAS
tseB WH increasinglycomplicatesthetaskofselectinganoptimalmethod
| ;tfirD | withinagivencontextforpolicymakersandpractitioners. |     |     |     |     |     |     |     |
| ------ | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Second,thefrequencywithwhichdifferentforecastingmethods
;NNA FCOL are used together within the same study has been examined.
|     | This analysis | makes | it possible |     | to understand | which | methods |     |
| --- | ------------- | ----- | ----------- | --- | ------------- | ----- | ------- | --- |
;NNK ;tehporP;MTSL
;NNK ;naeM;tfirD researchers most frequently evaluate side by side when con-
FCOL;NNRG FOC;AMIRA
|     | ducting performance |     | comparisons, |     | and | thus which | methodo- |     |
| --- | ------------------- | --- | ------------ | --- | --- | ---------- | -------- | --- |
sdohteM
;AMIRA;WH
| ;RGR;SE | logicalcombinations |     | havegained |     | wider acceptance. |     |     |     |
| ------- | ------------------- | --- | ---------- | --- | ----------------- | --- | --- | --- |
TheconnectionsinFigure2indicatewhichpairsofmethodsare
;TSOOBGX
;WH most frequently tested together in comparative studies in the
;AMIRA
literature.Theanalysesclearlyshowthattraditionalmethodsare
oftenusedbothamongthemselvesandinconjunctionwithnext‐
.gnitsooBtneidarGemertxE,TSOOBGX;noissergeRrotceVtroppuSlenreKhtiwtelevaW,RVSK‐W;noissergerotuArotceV
|     | generation | techniques | for | comparison | purposes. |     | For instance, |     |
| --- | ---------- | ---------- | --- | ---------- | --------- | --- | ------------- | --- |
.rep.roF 9102–7102 4202–3202 7102–6102 ARIMAisfrequentlycomparednotonlywithitsownderivatives,
suchasSARIMA,whichincorporateseasonalvariations,butalso
withML‐basedmethods,suchasANNorSVM.Similarly,official
|     | agency forecasts |           | and various | regression |                    | techniques | appear   | to  |
| --- | ---------------- | --------- | ----------- | ---------- | ------------------ | ---------- | -------- | --- |
|     | serve as a       | benchmark | for         | almost     | all methodological |            | classes. | In  |
.qerf ylhtnoM ylhtnoM noM particular, when evaluating the performance of ML algorithms
| ,nnA | (XGBoost,LSTM,andSVM),comparisonswiththesetraditional |     |     |     |     |     |     |     |
| ---- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
.sbO ,auQ
methodsemergeasawidespreadtrend.Itisalsonoteworthythat
variationswithinthesamemodelfamily(e.g.,VARvs.BVARor
|     | AR vs. ARIMA)are |     | frequently | analyzed | together. |     | This | suggests |
| --- | ---------------- | --- | ---------- | -------- | --------- | --- | ---- | -------- |
9102–9002 2202–5002 5102–1991
|     | that researchers |     | aim to understand |     | how different |     | specifications |     |
| --- | ---------------- | --- | ----------------- | --- | ------------- | --- | -------------- | --- |
RYT
orenhancementswithinagivenmodelfamily,suchasBayesian
|     | approaches | or seasonal | adjustments, |         | affect    | forecasting | perform- |      |
| --- | ---------- | ----------- | ------------ | ------- | --------- | ----------- | -------- | ---- |
|     | ance. In   | sum, this   | visual       | network | structure | reveals     | that     | com- |
5001
OT 021 612 parative analyses in the budget forecasting literature follow a
certainsystematicpattern:thevalidityandcontributionofanew
|     | method are | most | often assessed |     | against established |     | and | widely |
| --- | ---------- | ---- | -------------- | --- | ------------------- | --- | --- | ------ |
yrtnuoC
eyikrüT
ASU ASU accepted traditional methods, while the relative strengths and
|     | weaknesses | of different | methodological |     | families |     | are empirically |     |
| --- | ---------- | ------------ | -------------- | --- | -------- | --- | --------------- | --- |
evaluatedthroughthesetypicalcomparisons.
)5202(notrevOdnanosraL Third,thechangingtrendsinthepopularityofspecificforecasting
)5202(araKdnarelügneŞ
|     | methods | over time | have been | examined. |     | This analysis | makes | it  |
| --- | ------- | --------- | --------- | --------- | --- | ------------- | ----- | --- |
)deunitnoC(
|     | possible to | objectively | observe | the | shifts in | academic | interest | to- |
| --- | ----------- | ----------- | ------- | --- | --------- | -------- | -------- | --- |
)5202(.la
|     | ward particular | methodologies |        | and         | the dominance |         | cycles   | of cer- |
| --- | --------------- | ------------- | ------ | ----------- | ------------- | ------- | -------- | ------- |
|     | tain methods    | within        | the    | literature. | The           | graph   | displays | the     |
|     | changing        | frequencies   | of use | over        | the years     | for the | six most | fre-    |
)s(rohtuA
|
tegnuhC quentlycomparedmethodsintheanalyzedstudies.
1ELBAT
ThefindingsderivedfromGraph1clearlyrevealshiftsinacademic
|     | trends. Official |     | forecasts | were frequently |     | used | as benchmark |     |
| --- | ---------------- | --- | --------- | --------------- | --- | ---- | ------------ | --- |
8 PublicBudgeting&Finance,2025

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| FIGURE1 | | Evolutionofforecastingmethodsinbudgetingliteratureovertime.  |     |     |     |
| ------- | -------------------------------------------------------------- | --- | --- | --- |
| FIGURE2 | | Co‐occurrenceofforecastingmethodsincomparativebudgetstudies. |     |     |     |
AI‐based
references. The ARIMA model, however, has remained a con- generation, approaches. Overall, the current methodo-
sistentlypopulartoolforcomparisonsincethe1990s.Regression‐ logicalspectrumhasexpandedtoencompassbothbasicstatistical
modelsandadvancedcomputationaltechniques(Tables2–4).
| based methods    | experienced  | a resurgence | in the early 2000s,   | but |
| ---------------- | ------------ | ------------ | --------------------- | --- |
| their popularity | subsequently | declined     | somewhat. ML methods, |     |
such as ANN, have increasingly featured in comparative studies Fourth,thestructuralcharacteristicsofthedatasetsusedinthe
sincethe2010s.COF,ontheotherhand,hasmaintainedastable trainingofforecastingmodelsinthereviewedstudieshavebeen
presence among the methods consistently used for comparison analyzed.Thisanalysisiscriticalforunderstandingthecapacity
throughout the entire period under review. These trends indicate and diversity of the data sources feeding the models. Below,
thattheliteraturehaspreserveditsreferencepointsbasedontra- an assessment is presented showing the distributions of the
whilegraduallytransitioningtowardnew‐
ditionalmethodologies training datasets in terms of time span (number of years),
PublicBudgeting&Finance,2025 9

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
GRAPH1 | Trendsinthepopularityofkeyforecastingmethodsovertime(best5).
TABLE2 | Characteristicsoftrainingdatasetsinbudgetforecastingstudies.
Period Studies(N) Observation range Studies(N) Frequency Studies(N)
| 1–5years   |     | 1–25     |     |     |           |     |
| ---------- | --- | -------- | --- | --- | --------- | --- |
|            | 4   |          |     | 8   | Quarterly | 28  |
| 6–10years  |     | 26–50    |     |     |           |     |
|            | 13  |          |     | 16  | Annual    | 26  |
| 11–15years |     | 51–75    |     |     |           |     |
|            | 17  |          |     | 10  | Monthly   | 23  |
| 16–20years |     | 76–100   |     |     |           |     |
|            | 10  |          |     | 6   | Biannual  | 1   |
| 21–25years |     | 101–150  |     |     |           |     |
|            | 9   |          |     | 12  |           |     |
| 26–30years |     | 151–250  |     |     |           |     |
|            | 2   |          |     | 7   |           |     |
| 31–35years |     | 251–400  |     |     |           |     |
|            | 7   |          |     | 3   |           |     |
| 35–50years |     | 401–1000 |     |     |           |     |
|            | 4   |          |     | 4   |           |     |
| 50+years   | 3   | 1000+    |     | 3   |           |     |
Country‐leveldistributionofbudgetforecasting
| TABLE3 | |     |     | TABLE4 | | Numberofstudiesusingeachevaluationmetric. |     |     |
| -------- | --- | --- | ------ | ------------------------------------------- | --- | --- |
research.
|             |     |            | Metric |     |     | Frequency |
| ----------- | --- | ---------- | ------ | --- | --- | --------- |
| Countries   |     | Studies(N) |        |     |     |           |
|             |     |            | MAPE   |     |     | 38        |
| USA         |     | 30         | RMSE   |     |     | 36        |
| China       |     | 6          | MAE    |     |     | 22        |
| Panel       |     | 6          | MPE    |     |     | 7         |
| Türkiye     |     | 4          | PE     |     |     | 6         |
| Bharat      |     | 2          | MSE    |     |     | 5         |
| Brazil      |     | 2          | ME     |     |     | 5         |
| SouthAfrica |     | 2          | Others |     |     | 9         |
| Others*     |     | 17         | None   |     |     | 2         |
*17differentcountriesstudiedonce.
6–25years.
number of observations, and the most commonly used data on datasets covering Notably, datasets spanning
frequencies(Graph2). 11–15years are the most commonly used period (17 studies),
|     |     |     | indicating | a clear tendency | in the literature toward | a medium‐ |
| --- | --- | --- | ---------- | ---------------- | ------------------------ | --------- |
Examining the distribution of the time spans of the training da- term forecasting horizon. This approach allows for capturing
tasets,itisevidentthatthevastmajorityofstudies(over60%)rely macroeconomic cycles by maintaining sufficient historical depth
| 10  |     |     |     |     | PublicBudgeting&Finance,2025 |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- |

GRAPH2 | Averagetrainingdataspanbyforecastingmodel(best10).
while limiting potential parameter instability issues associated the tabular data. Notably, studies based on relatively simple
with very long time series. On the other hand, studies using da- models such as ADL and AR have average training periods
tasets of 31years or more are relatively few (14 studies in total), exceeding 40years, indicating that long seriesarenecessaryto
reflecting both the accessibility challenges and methodological ensure the parametric stability of these models. In contrast,
risksposedbystructuralbreaksinverylongseries.Conversely,the morecomplexmodelssuchasMIDASorARMAcanbeapplied
small number of studies (4 studies) relying solely on short‐term with comparatively shorter datasets, demonstrating the adapt-
dataof1–5yearscanbeconsideredcharacteristicofcontextswith ability of methods to series of different lengths. However, it is
limiteddatadepth,particularlyindevelopingeconomies. noteworthy that the relationship between model type and
numberofobservationsdoesnotfollowalinearpattern.While
In terms of the number of observations, the literature exhibits someshort‐term studiescorrespondto low‐complexitymodels,
considerable diversity. A significant portion of studies is con- long‐term seriestend to be associated with models sensitive to
centrated in the 26–50 observation range (16 studies), while parametric stability. This suggests that the alignment between
those based on more than 100 observations also constitute a model choice and training data length is shaped not only by
notablegroup(28studies).However,only16ofthese28studies technical considerations but also by data accessibility and the
contain 150 or more observations, indicating that studies rely- objectives ofthestudy.
ingonlongseriesremainrelativelylimitedintheliterature.The
presence of eight studies with only 1–25 observations raises Fifth,theaverageforecastinghorizonsofthemethodsusedinthe
serious concerns regarding the reliability of the models used. reviewed studies have been analyzed. This analysis provides
Forecasting based on such short series entails substantial important insights into which time spans are preferred for dif-
methodologicalweaknesses,particularlyintermsoftestingthe ferent methodological approaches and whether certain methods
statistical significance of parameters and producing robust arecharacteristicallyassociatedwithshort‐orlong‐termforecasts.
forecasts.Thisissuemaypreventdata‐intensivemethods,such
asDL,frombeingfullyevaluated,highlightingvaryinglevelsof The findingsin Graph 3 indicateaclear clusteringof methods
reliability in the literature and necessitating cautious interpre- intermsofforecastinghorizons.Traditionalstatisticalmethods,
tationof resultsfrom studieswith limited observations. such as AR and MA models, stand out with long average
horizons of 14.3 and 12years, respectively. Similarly, the
Examining data frequencies, it is observed that quarterly (28 MIDASmethod,withanaveragehorizonof9.7years,isamong
studies), annual (26 studies), and monthly (23 studies) data are the methods used for long‐term forecasts. This suggests that
chosen with relatively similar frequency. This distribution indi- relatively simple linear methods tend to provide a more stable
cates that, rather than a concentration on a single frequency, optionfor long‐term forecasts.
different frequenciesareusedatcomparablerates. Accordingly,
researchers' choices are largely shaped by data availability, the In contrast, parametric and multivariate models tend to focus
scopeofthestudy,andtheintendedforecastinghorizon. on shorter forecasting horizons. For example, ARIMA
(5.5years), VAR (5.1years), and BVAR (4.7years) are predom-
The findings on the average training periods of models in inantlyappliedinshort‐tomedium‐termforecasts.Thispattern
Figure3showsignificantalignmentwhenconsideredalongside indicates that as the number of parameters and the modeling
PublicBudgeting&Finance,2025 11
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| FIGURE3 |                                                     | Relationshipbetweenmethodsandperformancemetrics. |     |
| ------------------------------------------------------------- | ------------------------------------------------ | --- |
| GRAPH3 | Averageforecastinghorizonsbymethodinreviewedstudies. |                                                  |     |
long‐term
flexibilityofthesemodelsincrease,theirstabilitydiminishesin concentrated in relatively forecasts, parametric and
thefaceof long‐termuncertainty. multivariatemodelsinmedium‐termhorizons,andMLandDL
methodsinshort‐termforecasts.Thisdistributionindicatesthat
| InML‐ DL‐based |     |     |
| -------------- | --- | --- |
and methods,the forecastinghorizonis notably forecasting horizons are determined not only by researchers'
shorter.ANNstandsoutwithanaveragehorizonof5.3years,while preferences but also by the structural limitations inherent in
LSTMislimitedtoonly3.3years.Theseresultsindicatethatsuch eachmethod.
| methods are strong | in capturing complex, | nonlinear relationships |
| ------------------ | --------------------- | ----------------------- |
short‐term long‐term
over periods but are more constrained in Sixth, the geographic distribution of the reviewed comparative
forecastsduetorisksofparameterinstabilityandoverfitting. studies has been analyzed. This analysis provides important
insightsintowhichcountriesandregionsacademicresearchon
Overall, a methodological division of labor emerges among budget forecasting methods is concentrated, thereby shedding
forecasting methods: simple linear statistical methods are light onthe geographiccoverageof theexistingliterature.
12 PublicBudgeting&Finance,2025

The findings on country distribution reveal a pronounced forthevastmajorityofusage,establishingadominantposition
concentration and imbalance in the literature. The United in assessing forecasting accuracy. The prominence of MAPE
Statesaccountsforthelargestsharewith30studies,followedby andRMSEcanbeexplainedbytheireaseofinterpretationand
China(6),paneldatasets(6),andTurkey(4).Brazil,India,and their suitability for comparisons across series of different
South Africa are represented by two studies each. The magnitudes.
remaining17countriesarecoveredonlyonceandaregrouped
under the “Others” category. This pattern indicates that em- In contrast, metrics such as MPE (7 studies), ME (5 studies),
piricalresearchisheavilyfocusedonalimitedsetofcountries, MSE (5 studies), and PE (6 studies) are used relatively infre-
while a wide range of other nations receives very limited quently. Their limited representation indicates that the litera-
attention. ture tends to favor standardized metrics that allow for
international comparisons. Additionally, in nine studies cate-
The reasons for the United States' clear predominance include gorized as “Others,” more specific or context‐specific metrics
easy access to data, long historical macroeconomic series, the were employed, while two studies did not report any perform-
perception of U.S. data as a global benchmark in academic ance metric at all. The latter case can be regarded as a signifi-
publications, and the dominance of Anglo‐Saxon literature. In cantshortcoming interms ofmethodological transparency.
contrast,fordevelopingcountries,bothdifficultiesinaccessing
long‐term reliable data series and differences in institutional The network structure in the graph further clarifies the re-
contextsresultintheirunderrepresentationinstudies.Turkey's lationships between methods and metrics. RMSE and MAPE
representationbyonlyfourstudiesservesasaconcreteexample stand out as nodes with the most extensive connections,
ofthis overall imbalance. showingstrongassociationswithwidelyusedmethodssuchas
ARIMA, ANN, HW, VAR, OFC, COF, and SARIMA. This
On the other hand, the presence of six studies using panel da- finding indicates that performance evaluations of prominent
tasets indicates that researchers have also pursued cross‐ methods in the literature generally rely on the same set of
country comparisons rather than focusing solely on single‐ metrics, and comparability is largely established around these
countryanalyses.However,thelimitednumberofpanelstudies measures. In contrast, less frequently used methods such as
suggests that the literature has not yet fully developed a com- LSTM, XGBoost, or Prophet are linked to a relatively limited
parativeperspectivecapableofprovidinggeneralizableinsights number of metrics, suggesting both low methodological diver-
andrevealing cross‐countrydifferences. sityandtheabsenceofastandardizedapproachfor evaluating
theperformanceof thesemethods.
Seventh,thedistributionofmetricsusedtoevaluateforecasting
performance in the reviewed comparative studies has been Eighth and finally, the relationship between method diversity
analyzed. This analysisprovides important insights into which and academic impact in the reviewed comparative studies has
evaluation criteria are prioritized in the literature and, conse- been analyzed. This analysis provides important insights into
quently,whichdimensionsoferrorareconsideredmostcritical whether the number of methods compared in a study has any
in methodcomparisons. effect onthe number ofcitationsthestudy receives(Graph4).
Examiningthemetricsusedtoevaluatemethodperformance,a The analysis results indicate a notable but nonlinear relation-
clear concentration is observed in the literature. The most fre- shipbetweenthenumberofmethodsinastudyanditscitation
quently used evaluation criteria are MAPE (38 studies), RMSE count. The vast majority of the reviewed studies (over 70%)
(36studies),andMAE(22studies).Thesethreemetricsaccount compare between 2 and 5 methods. Studies with 2 methods
GRAPH4 | Relationshipbetweenstudies,methods,andcitations.
PublicBudgeting&Finance,2025 13
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
representthemostcommoncategorywith18cases,followedby product not of a single, static process, but of political negotia-
| 3‐method |     |     |     |     | 4‐method |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
studies with 15 cases and studies with 14 tions,economicshocks,institutionalchanges,andadministrative
cases. In terms of citation counts, the highest average citation rules.Accordingly, thefocus shouldshift fromfinding theopti-
performance is observed among studies comparing between 3 malmodeltoidentifyingtherightmodelfortherightcontext.
and6methods.Studieswith3methodsreceiveanaverageof26
citations,whilethosewith6methodsreachasimilaraverageof
| 26 citations. |     | This | finding | suggests | that | a moderate | level of |       |              |     |      |           |        |     |     |
| ------------- | --- | ---- | ------- | -------- | ---- | ---------- | -------- | ----- | ------------ | --- | ---- | --------- | ------ | --- | --- |
|               |     |      |         |          |      |            |          | 5.2 | | The Enduring |     | Role | of Simple | Models |     | and |
method diversitymayenhance academic impact. the Benchmarking Paradox
| However, | it  | is also | evident | that citation |     | performance | does not |         |            |            |             |     |        |        |      |
| -------- | --- | ------- | ------- | ------------- | --- | ----------- | -------- | ------- | ---------- | ---------- | ----------- | --- | ------ | ------ | ---- |
|          |     |         |         |               |     |             |          | Despite | the influx | of complex | techniques, |     | simple | models | such |
increase consistently with the number of methods. Studies as OFC, RW, and various regression approaches remain not
| including | 7       | or more | methods  | exhibit | a           | noticeable | decline in   |               |     |            |     |             |             |     |     |
| --------- | ------- | ------- | -------- | ------- | ----------- | ---------- | ------------ | ------------- | --- | ---------- | --- | ----------- | ----------- | --- | --- |
|           |         |         |          |         |             |            |              | only relevant | but | also serve | as  | fundamental | benchmarks. |     | Any |
| citation  | counts. | This    | suggests | that    | comparisons |            | involving an |               |     |            |     |             |             |     |     |
newmodelmustconsistentlyoutperformthesenaïveorsimple
excessive number of methods may be less favored by readers standards to justify its added complexity. The fact that these
andresearchersorthatsuchstudiesmaygivetheimpressionof
|             |     |                |     |         |      |            |        | simple models | still | frequently | rank | among | the | top performers, |     |
| ----------- | --- | -------------- | --- | ------- | ---- | ---------- | ------ | ------------- | ----- | ---------- | ---- | ----- | --- | --------------- | --- |
| emphasizing |     | methodological |     | breadth | over | analytical | depth. |               |       |            |      |       |     |                 |     |
oratleastarenotconsistentlytheworst,incomparativestudies
Interestingly,studiesemployingonlyasinglemethodarequite
servesasacautionaryreminderforthefield.Itunderscoresthat
rare (3 studies), and their average citation count (7 citations) statistical sophistication does not automatically translate into
| remains | relatively |     | low. | This finding |     | suggests | that non‐ |             |              |     |              |     |          |       |          |
| ------- | ---------- | --- | ---- | ------------ | --- | -------- | --------- | ----------- | ------------ | --- | ------------ | --- | -------- | ----- | -------- |
|         |            |     |      |              |     |          |           | forecasting | superiority, |     | particularly | in  | contexts | where | data are |
comparativestudiesmayhaveamorelimitedacademicimpact
|     |     |     |     |     |     |     |     | noisy, short, | and | subject | to unpredictable |     | political |     | interven- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ---------------- | --- | --------- | --- | --------- |
compared tocomparative studies. tions. This creates a paradox: as research energy increasingly
|     |     |     |     |     |     |     |     | focuses | on developing | complex |     | models, | the practical |     | value of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ------- | --- | ------- | ------------- | --- | -------- |
Inconclusion,thisanalysissuggeststheexistenceofanoptimal
|     |     |     |     |     |     |     |     | these advancements |     | often | remains | marginal |     | when compared |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----- | ------- | -------- | --- | ------------- | --- |
range for method diversity. Comparisons with very few meth- against well‐defined, simple benchmarks.
| ods are | considered |     | insufficient, | while | studies | including | an ex-      |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ------------- | ----- | ------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| cessive | number     | of  | methods       | may   | be less | favored   | by readers. |     |     |     |     |     |     |     |     |
Studiescomparingbetween3and6methodsexhibitthehighest
|          |         |            |     |      |               |     |             | 5.3 |      | Data Quality, |     | Quantity, |     | and the | Global |     |
| -------- | ------- | ---------- | --- | ---- | ------------- | --- | ----------- | ---------- | ------------- | --- | --------- | --- | ------- | ------ | --- |
| academic | impact, | indicating |     | that | comprehensive |     | yet focused |            |               |     |           |     |         |        |     |
|          |         |            |     |      |               |     |             | Inequality | Issue         |     |           |     |         |        |     |
comparisonscontributemorevaluableinsightstotheliterature.
|     |     |     |     |     |     |     |     | The analysis | of        | training   | data characteristics |     | highlights |              | a sig- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | ---------- | -------------------- | --- | ---------- | ------------ | ------ |
|     |     |     |     |     |     |     |     | nificant     | and often | overlooked | challenge:           |     | data       | constraints. | The    |
5 | Discussion and Policy Recommendations prevalence of studies using 11–15 years of data indicates that
|     |     |     |     |     |     |     |     | many models | are | built | on relatively |     | limited information |     | sets. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ------------- | --- | ------------------- | --- | ----- |
The comprehensive analysis presented in this study offers a This poses a critical limitation for data‐hungry methods such
multidimensional examination of the comparative structure of as DL, potentially leading to overfitting and reduced out‐of‐
| the budget |     | forecasting | literature, |     | characterized |     | by methodo- |        |                |              |     |     |            |     |           |
| ---------- | --- | ----------- | ----------- | --- | ------------- | --- | ----------- | ------ | -------------- | ------------ | --- | --- | ---------- | --- | --------- |
|            |     |             |             |     |               |     |             | sample | generalization | performance. |     | The | geographic |     | distribu- |
logical diversity, geographic biases, and the ongoing tension tion of studies further exposes a substantial data gap. The
between model complexity and practical applicability within a dominance of United States‐based research reflects not merely
| dynamic | and   | evolving | field.  | The     | following | discussion    | synthe- |          |             |     |                     |        |     |                    |     |
| ------- | ----- | -------- | ------- | ------- | --------- | ------------- | ------- | -------- | ----------- | --- | ------------------- | ------ | --- | ------------------ | --- |
|         |       |          |         |         |           |               |         | academic | preference  | but | is directly         | linked | to  | data availability, |     |
| sizes   | these | findings | to draw | broader |           | implications, | address |          |             |     |                     |        |     |                    |     |
|         |       |          |         |         |           |               |         | quality, | and length. | The | underrepresentation |        |     | of developing      |     |
inherenttensionsinthefield,andsuggestdirectionsforfuture economiesconstitutesacriticalgapintheliterature.Budgetary
researchandpractice. processes,institutionalframeworks,andeconomicfluctuations
inthesecontextsdiffersubstantially.Modelsoptimizedonlong,
|             |                  |         |     |            |     |                |           | stable U.S.       | time           | series          | may fail | when | applied   | to economies |     |
| ----------- | ---------------- | ------- | --- | ---------- | --- | -------------- | --------- | ----------------- | -------------- | --------------- | -------- | ---- | --------- | ------------ | --- |
|             |                  |         |     |            |     |                |           | proneto           | fiscal shocks, | characterizedby |          |      | lowerdata | quality      | and |
| 5.1         | | Methodological |         |     | Diversity  | and | the            | Quest for |                   |                |                 |          |      |           |              |     |
| the Optimal |                  | Model   |     |            |     |                |           | shorterhistorical |                | records.        |          |      |           |              |     |
| The most    | striking         | finding | of  | this study | is  | the relentless | diversi-  |                   |                |                 |          |      |           |              |     |
fication offorecasting methods.The evolution from simple AR- 5.4 | Evaluation Inconsistency and the
|     |        |                  |     |      |          |     | PCA‐   | Hegemony | of  | Metrics |     |     |     |     |     |
| --- | ------ | ---------------- | --- | ---- | -------- | --- | ------ | -------- | --- | ------- | --- | --- | --- | --- | --- |
| IMA | models | to sophisticated |     | LSTM | networks | and | hybrid |          |     |         |     |     |     |     |     |
W‐KSVR
|     | frameworks |     | represents |     | a true | methodological | arms |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ---------- | --- | ------ | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
race. This expansion is undoubtedly fueled by the quest for The near‐absolute dominance of MAPE, RMSE, and MAE as
| accuracy, | supported |     | by increasing |     | computational |     | power and ri- |                            |     |     |                            |     |     |     |     |
| --------- | --------- | --- | ------------- | --- | ------------- | --- | ------------- | -------------------------- | --- | --- | -------------------------- | --- | --- | --- | --- |
|           |           |     |               |     |               |     |               | performancemetricsprovides |     |     | acommonlanguageforcompari- |     |     |     |     |
cher data availability. However, the analyses indicate that this son but also poses a potential pitfall: the tyranny of averages.
proliferation does not yield a universally superior algorithm; These metrics measure themagnitudeof errors but remain lar-
rather, ithas led to a formof methodological inflation that can gelyagnostic to thedirection and timingofmistakes. Ina bud-
overwhelm practitioners and obscure clear guidance. The getary context, the cost of overestimating a deficit (potentially
absence of a single “best” method should not be viewed as a leading to unnecessary austerity measures) is substantially dif-
failure of the research community but as a reflection of the ferentfromthecostofunderestimatingit(potentiallytriggeringa
near‐complete
inherentcomplexityofbudgetaryprocesses.Budgetdataarethe fiscal crisis). The neglect of directional metrics
| 14  |     |     |     |     |     |     |     |     |     |     |     | PublicBudgeting&Finance,2025 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
horizon.Theresilienceoftraditionalstatisticalmethodsinlong‐
| such as | MPE in | the current |     | literature | represents | a   | significant |     |     |     |     |     |     |     |     |
| ------- | ------ | ----------- | --- | ---------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
shortcoming. Evaluations should incorporate asymmetric loss termforecasts,alongsidethestrengthofMLandDLapproaches
functionsthatreflectthereal‐worldpoliticalandeconomiccosts in capturing short‐term complex relationships, indicates the
oferrors,ratherthansolelytheirstatisticalproperties. existenceofamethodological division oflabor.
|           |                   |          |          |        |          |         |            | The pronounced    |            | geographic          | concentration |                      |             | in the | literature, |
| --------- | ----------------- | -------- | -------- | ------ | -------- | ------- | ---------- | ----------------- | ---------- | ------------------- | ------------- | -------------------- | ----------- | ------ | ----------- |
|           |                   |          |          |        |          |         |            | particularly      | the        | underrepresentation |               |                      | of emerging |        | economies,  |
| 5.5 |     | Academia–Practice |          |          | Gap    |          |         |            |                   |            |                     |               |                      |             |        |             |
|           |                   |          |          |        |          |         |            | poses significant |            | limitations         | to            | the generalizability |             |        | of existing |
|           |                   |          |          |        |          |         |            | findings.         | Similarly, | the                 | near‐absolute |                      | dominance   |        | of metrics  |
| Citation  | impact            | analysis | provides | a      | striking | insight | into the   |                   |            |                     |               |                      |             |        |             |
|           |                   |          |          |        |          |         |            | such as           | MAPE,      | RMSE,               | and MAE       | in                   | performance |        | evaluation  |
| sociology | of the            | field.   | The      | higher | citation | rates   | of studies |                   |            |                     |               |                      |             |        |             |
comparing 3–6 methods suggestthat theacademic community leads to theneglectof criticaldimensions, including thedirec-
|                      |       |          |             |              |      |           |          | tionoferrors | andasymmetriccosts. |     |     |     |     |     |     |
| -------------------- | ----- | -------- | ----------- | ------------ | ---- | --------- | -------- | ------------ | ------------------- | --- | --- | --- | --- | --- | --- |
| values comprehensive |       |          | yet focused | comparisons. |      | However,  | this     |              |                     |     |     |     |     |     |     |
| academic             | ideal | does not | always      | align        | with | practical | needs. A |              |                     |     |     |     |     |     |     |
practitioner in a treasury department does not require a com- The findings of this study offer important implications for
|         |                  |     |            |     |           |           |         | future research. |      | First, contextual |     | appropriateness |     | should  | take     |
| ------- | ---------------- | --- | ---------- | --- | --------- | --------- | ------- | ---------------- | ---- | ----------------- | --- | --------------- | --- | ------- | -------- |
| parison | of six different |     | ML models; |     | they need | a single, | robust, |                  |      |                   |     |                 |     |         |          |
|         |                  |     |            |     |           |           |         | precedence       | over | methodological    |     | complexity.     |     | Second, | the geo- |
interpretable,andoperationallyfeasiblemodeltailoredtotheir
|          |          |          |      |        |                |     |           | graphic | scope should | be  | expanded | to  | include | emerging | econo- |
| -------- | -------- | -------- | ---- | ------ | -------------- | --- | --------- | ------- | ------------ | --- | -------- | --- | ------- | -------- | ------ |
| specific | national | context. | This | points | to a potential |     | academia– |         |              |     |          |     |         |          |        |
practice disconnect. The complexity of state‐of‐the‐art models mies, and datasets should be enriched accordingly. Third,
|              |     |          |       |         |      |        | “black | performance | evaluation |     | criteria | should | be diversified |     | to reflect |
| ------------ | --- | -------- | ----- | ------- | ---- | ------ | ------ | ----------- | ---------- | --- | -------- | ------ | -------------- | --- | ---------- |
| (e.g., LSTMs | and | XGBoost) | often | renders | them | opaque |        |             |            |     |          |        |                |     |            |
thepolicycostsofforecasterrors.Finally,hybridandensemble
| boxes” for | policymakers. |     | Simpler | models | or  | official | forecasts, |     |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | ------- | ------ | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
evenifslightlylessaccuratebysomemetrics,offertransparency learning approaches warrant further investigation to leverage
|     |     |     |     |     |     |     |     | therelativestrengths |     | ofdifferentmethods. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------------------- | --- | --- | --- | --- | --- |
andaccountability.Futureresearchshouldaddressthisgapby
| not only | reporting | accuracy | metrics |     | but also | considering | oper- |     |     |     |     |     |     |     |     |
| -------- | --------- | -------- | ------- | --- | -------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ational aspects, such as computational requirements, inter- For policymakers and practitioners, this study emphasizes the
|                            |     |     |                       |     |     |     |            | importance | of  | avoiding | dogmatic | method | selection |     | in budget |
| -------------------------- | --- | --- | --------------------- | --- | --- | --- | ---------- | ---------- | --- | -------- | -------- | ------ | --------- | --- | --------- |
| pretability,andintegration |     |     | intoexistingbudgetary |     |     |     | processes. |            |     |          |          |        |           |     |           |
forecasting.Adoptingaflexibleandpluralisticapproach,taking
intoaccountinstitutionalcapacity,dataquality,andforecasting
|       |         |        |     |          |     |            |     | objectives, | can | contribute | to producing |     | more | realistic | and reli- |
| ----- | ------- | ------ | --- | -------- | --- | ---------- | --- | ----------- | --- | ---------- | ------------ | --- | ---- | --------- | --------- |
| 5.6 | | Rise of | Hybrid | and | Ensemble |     | Approaches |     |             |     |            |              |     |      |           |           |
able budgetforecasts.
Theemergenceofhybridmodelspoints,albeitmodestly,toward
Inconclusion,progressinthefieldofbudgetforecastingdepends
| a promising         | direction |     | for the    | field. Rather | than      | treating    | meth- |          |            |                         |     |         |           |      |            |
| ------------------- | --------- | --- | ---------- | ------------- | --------- | ----------- | ----- | -------- | ---------- | ----------------------- | --- | ------- | --------- | ---- | ---------- |
|                     |           |     |            |               |           |             |       | less on  | developing | increasingly            |     | complex | models    | and  | more on    |
| ods as competitors, |           | the | discipline | is            | gradually | recognizing | the   |          |            |                         |     |         |           |      |            |
|                     |           |     |            |               |           |             |       | managing | the        | existing methodological |     |         | diversity | in a | systematic |
valueofhybridizationandensembletechniques.Thestrengths context‐sensitive
|              |     |            |     |         |            |     |             | and |     | manner. |     | This study | provides |     | a compre- |
| ------------ | --- | ---------- | --- | ------- | ---------- | --- | ----------- | --- | --- | ------- | --- | ---------- | -------- | --- | --------- |
| of one model | can | compensate |     | for the | weaknesses |     | of another. |     |     |         |     |            |          |     |           |
hensivefoundationforsucheffortsandaimstocontributetothe
Forinstance,aclassicalstatisticalmodelmaycapturelong‐term
developmentofbudgetforecastingasbothascienceandanart.
| trends, while    | an  | ANN       | can adjust | for       | recent | nonlinear | devia- |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | ---------- | --------- | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| tions. Combining |     | forecasts | from       | different | model  | families  | often  |     |     |     |     |     |     |     |     |
yieldsmoreaccurateandrobustresultsthananysinglemodel.
| meta‐modeling |     |           |     |       |         |     |             | References |     |     |     |     |     |     |     |
| ------------- | --- | --------- | --- | ----- | ------- | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| This          |     | approach, |     | which | focuses | on  | integrating |            |     |     |     |     |     |     |     |
informationratherthanselectingasingle“winner,”appearsto “Searching
|     |     |     |     |     |     |     |     | Agostini, | S. J. 1991. |     | for | a Better | Forecast: | San | Francisco's |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | --- | -------- | --------- | --- | ----------- |
Model.”
be a more efficient pathway than developing isolated, increas- Revenue Forecasting Government Finance Review 7, no. 6:
13–16.
inglycomplexalgorithms.
“Forecasting
|     |     |     |     |     |     |     |     | Alamdari, | S. H., | H. Khalizadeh, | and | A. Zayer. | 2016. |     | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------------- | --- | --------- | ----- | --- | --- |
Models.”
|     |     |     |     |     |     |     |     | Iranian | Tax Revenues: | Application |     | of Nonlinear |     |     | Journal of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ----------- | --- | ------------ | --- | --- | ---------- |
InternationalEconomicsandManagementStudies1,no.2:21–48.
6 | Conclusion
“Assimi-
|     |     |     |     |     |     |     |     | Alhassan, | B. G.,    | F. B. Yusof, | and S.   | M. Norrulashikin. |             | 2020. |        |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------ | -------- | ----------------- | ----------- | ----- | ------ |
|     |     |     |     |     |     |     |     | lation of | Principal | Component    | Analysis |                   | and Wavelet | With  | Kernel |
Thisstudysystematicallyanalyzestheliteratureexaminingthe Medium‐Term
|             |               |     |               |        |                       |                |      | Support       | Vector        | Regression | for                   |            | Financial |                  | Time Series |
| ----------- | ------------- | --- | ------------- | ------ | --------------------- | -------------- | ---- | ------------- | ------------- | ---------- | --------------------- | ---------- | --------- | ---------------- | ----------- |
| comparative | performance   |     | of            | budget | forecasting           | methods,       | pro- | Forecasting.” |               |            |                       |            |           |                  |             |
|             |               |     |               |        |                       |                |      |               | International |            | Journalof             | Management |           | and Humanities4, |             |
| viding a    | comprehensive |     | overview      | of     | the field's           | methodological |      | no.7:40–48.   |               |            |                       |            |           |                  |             |
| evolution,  | geographic    |     | distribution, |        | data characteristics, |                | and  |               |               |            |                       |            |           |                  |             |
|             |               |     |               |        |                       |                |      | Asher, M.     | G.1978.       | “Accuracy  | of BudgetaryForecasts |            |           | of Central       | Gov-        |
| performance | evaluation    |     | trends.       | The    | findings              | indicate       | that |               |               |            |                       |            |           |                  |             |
ernment,1967‐68to1975‐76.”EconomicandPoliticalWeekly13,no.8:
budgetforecastingisnotastaticdomainbutadynamicresearch
423–432.
| area in | continuous | evolution, |     | deeply | influenced |     | by develop- |                |     |                   |     |            |              |     |        |
| ------- | ---------- | ---------- | --- | ------ | ---------- | --- | ----------- | -------------- | --- | ----------------- | --- | ---------- | ------------ | --- | ------ |
|         |            |            |     |        |            |     |             | Asimakopoulos, |     | S., Joan Paredes, |     | and Thomas | Warmedinger. |     | “Fore- |
ments in relateddisciplines.
castingFiscalTimeSeriesUsingMixedFrequencyData.”ECBWorking
PaperNo.1550,2013.
| The analyses | of          | this study | clearly | demonstrate |            | that | there is no  |          |       |               |              |     |     |          |          |
| ------------ | ----------- | ---------- | ------- | ----------- | ---------- | ---- | ------------ | -------- | ----- | ------------- | ------------ | --- | --- | -------- | -------- |
|              |             |            |         |             |            |      |              | Auld, D. | A. L. | 1970. “Fiscal | Marksmanship |     | in  | Canada.” | Canadian |
| single,      | universally | optimal    |         | method      | for budget |      | forecasting. |          |       |               |              |     |     |          |          |
JournalofEconomics3,no.3:507–511.
| Instead, | the performance |     | of  | forecasting | methods |     | varies subs- |     |     |     |     |     |     |     |     |
| -------- | --------------- | --- | --- | ----------- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
tantially depending on contextual factors such as economic Baghestani,H.,andR.McNown.1992.“ForecastingtheFederalBudget
WithTime‐SeriesModels.”JournalofForecasting11,no.2:127–139.
| conditions,                  | data | quality, | institutional |     | structures, | and | forecast |     |     |     |     |     |     |     |     |
| ---------------------------- | ---- | -------- | ------------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| PublicBudgeting&Finance,2025 |      |          |               |     |             |     |          |     |     |     |     |     |     |     | 15  |

Botrić, V., and M. Vizek. 2012. “Forecasting Fiscal Revenues in a Favero, C. A., and M. Marcellino. 2005. “Modelling and Forecasting
TransitionCountry:TheCaseofCroatia.”ZagrebInternationalReview FiscalVariablesfortheEuroArea.”OxfordBulletinofEconomicsand
ofEconomics&Business15,no.1:23–36. Statistics67,no.1:755–783.
Bretschneider,S.I.,W.L.Gorr,G.Grizzle,andE.Klay.1989.“Politicaland Fedotov,D.Y.2017.“ForecastingofRegionalEconomicDevelopment
Organizational Influences on the Accuracy of Forecasting State Govern- and Budget Based on the Example of Irkutsk Oblast.” Studies on
mentRevenues.”InternationalJournalofForecasting5,no.3:307–319. RussianEconomicDevelopment28,no.4:416–422.
Bretschneider,S.,andW.Gorr.1992.“Economic,Organizational,and Frank, H. A. 1990. “Municipal Revenue Forecasting With Time. Series
PoliticalInfluencesonBiasesinForecastingStateSalesTaxReceipts.” Models:AFloridaCaseStudy.”AmericanReviewofPublicAdministration
InternationalJournalofForecasting7,no.4:457–466. 20,no.1:45–59.
Buxton,E.K.,A.K.Kenneth,M.Cremeens,andK.Jay.2019.“AnAuto Frank, H. A., and A. G. Gerasimos. 1990. “Raising the Bridge Using
RegressiveDeepLearningModelforSalesTaxForecastingFromMul- Time Series Forecasting Models.” Public Productivity & Management
tiple Short Time Series.” In 18th IEEE International Conference on Review14,no.2:171–188.
MachineLearningandApplications,1359–1364.IEEE.
Frank, H. A., and X. H. Wang. 1994. “Judgmental vs. Time Series Vs.
Campbell, J. E., M. E. Ogunsanya, N. Holmes, T. VanWagoner, and DeterministicModelsinLocalRevenueForecasting:AFloridaCaseStudy.”
J.James.2024.“BibliometricandSocialNetworkAnalysisofaClinical JournalofPublicBudgeting,Accounting&FinancialManagement6,no.4:
and Translational Resource Awardee: An Oklahoma Experience 493–517.
2014–2021.”JournalofClinicalandTranslationalScience8:e10.
Fullerton, T. M. 1989. “A Composite Approach to Forecasting State
Castelino,M.S.,R.C.B.Belluzzo,J.P.Albino,andV.C.P.N.Valente. Government Revenues: Case Study of the Idaho Sales Tax.”
2024.“BibliometricAnalysis:LiteratureReviewandProposalofaMeth- InternationalJournalofForecasting5,no.3:373–380.
odologicalFrameworkin12Steps.”RevistaAracê6,no.4:13421–13446.
Ghysels,E.,andN.Ozkan.2015.“Real‐TimeForecastingoftheUSFederal
https://doi.org/10.56238/arev6n4-146.
Government Budget: A Simple Mixed Frequency Data Regression
Chatagny, F., and N. C. Soguel. 2012. “The Effect of Tax Revenue Approach.”InternationalJournalofForecasting31,no.4:1009–1020.
BudgetingErrorsonFiscalBalance:EvidenceFromtheSwissCantons.”
Ghysels, E., and N. Ozkan. Real‐Time Predictions of the U.S. Federal InternationalTaxandPublicFinance19:319–337.
Government Budget: Expenditures, Revenues and Deficits. UNC
Chimilila, C. 2017. “Forecasting Tax Revenue and Its Volatility in Kenan‐FlaglerResearchPaper,2012.
Tanzania.”AfricanJournalofEconomicReview5,no.1:84–109. Ghysels,E., F.Grigoris, and N.Özkan. 2022.“Real‐Time Forecastsof
Chung, I. H., B. Kara, M. McShea, R. Pathak, and D. Williams. 2025. State and Local Government Budgets With an Application to the
“Using Large Language Models to Forecast Local Government Reve- COVID‐19Pandemic.”NationalTaxJournal75,no.4:731–763.
nue.”PublicFinanceJournal2,no.2:85–98.
Gianakis, G.A., and A. F. Howard. 1993. “Implementing Time Series
Chung,I.H.,W.W.Daniel,andM.R.Do.2022.“ForBetterorWorse? Forecasting Models: Considerations for Local Governments.” State &
Revenue Forecasting With Machine Learning Approaches.” Public LocalGovernmentReview25,no.2:130–144.
Performance&ManagementReview45,no.5:1133–1154.
Grizzle, G., and W. E. Klay. 1994. “Forecasting State Sales Tax Reve-
Cirincione,C.,G.A.Gurrieri,andB. vandeSande.1999.“Municipal nues: Comparing the Accuracy of Different Methods.” State & Local
GovernmentRevenueForecasting:IssuesofMethodandData.”Public GovernmentReview26,no.3:142–152.
Budgeting&Finance19,no.1:26–46.
Hájek, P., and V. Olej. 2010. “Municipal Revenue Prediction by En-
Cooke,S.,andC.McIntosh.2011.“ForecastingGeneralFundRevenue:An sembles of Neural Networks and Support Vector Machines.” WSEAS
AnalysisofIdahoFY1998toFY2011.”PublicBudgeting&Finance31,no.4: TransactionsonComputers9,no.11:1255–1264.
51–73.
Jena, P. R. 2006. “Fiscal Marksmanship: Link Between Forecasting
Cooksey, R. W. 2020. Descriptive Statistics for Summarising Data. Central Tax Revenues and State Fiscal Management.” Economic and
SpringerSingapore. PoliticalWeekly41,no.37:3971–3976.
Corvalão,E.,R.W.Daniel,Samohyl,andG.H.Brasil.2010.“Forecastingthe Khan,T.,AnwarHussain,andZ.K.M.2018.“FiscalMarksmanshipin
Collection of the State Value Added Tax (ICMS) in Santa Catarina: The Pakistan: With Special Focus on Province Khyber Pakhtunkhwa.”
GeneraltoSpecificApproachinRegressionAnalysis.”BrazilianJournalof PakistanJournalofEconomicStudies1,no.1:21–43.
Operations&ProductionManagement7,no.1:105–121.
Koirala,T.P.2012.“GovernmentRevenueForecastinginNepal.”NRB
Damane,M.2020.“ForecastingtheGovernmentofLesotho'sBudget:An EconomicReview24,no.2:47–60.
AR‐MIDAS Approach.” African Journal of Economic and Sustainable
Kong,D.2007.“LocalGovernmentRevenueForecasting:TheCalifornia
Development7,no.3:256–285.
County Experience.” Journal of Public Budgeting, Accounting &
Danninger,S.2005.“RevenueForecastsasPerformanceTargets.”IMF FinancialManagement19,no.2:178–199.
WorkingPaper,1–20.https://doi.org/10.5089/9781451860337.001.
Krause,G.A.,andJ.K.Corder.2007.“ExplainingBureaucraticOptimism:
Derrick,R.A.2002.BetterRevenueForecasting:IsFiscalStressaStim- Theoryand EvidenceFromU.S.Executive AgencyMacroeconomic Fore-
ulant? A Look at Nevada Local Governments. UNLV Theses, Disserta- casts.”AmericanPoliticalScienceReview101,no.1:129–142.
tions,ProfessionalPapers,andCapstones.
Krol,R. 2010.ForecastingState TaxRevenue:ABayesianVectorAuto-
Downs,G.W.,andD.M.Rocke.1983.“MunicipalBudgetForecastingWith regression Approach, 1–18. California State University, Department of
MultivariateARMAModels.”JournalofForecasting2,no.4:377–387. Economics.
Duncan,G.,W.Gorr,andJ.Szczypula.1993.“BayesianForecastingfor Lahiri, K., and C. Yang. 2022. “Boosting Tax Revenues With Mixed‐
Seemingly Unrelated Time Series: Application to Local Government FrequencyDataintheAftermathofCovid‐19:TheCaseofNewYork.”
RevenueForecasting.”ManagementScience39,no.3:275–293. InternationalJournalofForecasting38,no.2:545–566.
Erdoğdu, H., and R. Yorulmaz. 2019. “Comparison of Tax Revenue Larson,S.,andM.Overton.2024.“ModelingApproachMatters,ButNotas
Forecasting Models for Turkey.” In 34. International Public Finance MuchasPreprocessing:ComparisonofMachineLearningandTraditional
Conference,482–492. RevenueForecastingTechniques.”PublicFinanceJournal1,no.1:29–48.
16 PublicBudgeting&Finance,2025
15405850,
0, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Larson,S.,andM.Overton.2025.“IsThereaGoldStandardorNeedfor Otrok,C.,andH.W.Charles.1997.“WhatToDoWhentheCrystalBall
a City‐Centric Approach for Sales Tax Revenue Forecasting.” Public Is Cloudy: Conditional and Unconditional Forecasting in Iowa.”
FinanceJournal2,no.2:99–120.https://doi.org/10.59469/pfj.2025.45. Proceedings.AnnualConferenceonTaxationandMinutesoftheAnnual
MeetingoftheNationalTaxAssociation90:326–334.
Leal,T.,J.J.Pérez,M.Tujula,andJ.P.Vidal.2008.“FiscalForecasting:
LessonsFromtheLiteratureandChallenges.”FiscalStudies29,no.3: Passas,I.2024.“BibliometricAnalysis:TheMainSteps.”Encyclopedia
347–386. 4:1014–1025.
Li‐xia, L., Z. Yi‐Qi, and X. Liu. 2011. “Tax Forecasting Theory and Pedregal, D. J., and J. J. Pérez. 2010. “Should Quarterly Government
Model Based on SVM Optimized by PSO.” Expert Systems With Finance Statistics Be Used for Fiscal Surveillance in Europe?”
Applications38,no.1:116–120. InternationalJournalofForecasting26,no.4:794–807.
Li,W.,Q.Xie,J.Ao,etal.2025.“SystematicReview:AScientometric Pérez,J.J.2007.“LeadingIndicatorsforEuroAreaGovernmentDefi-
Analysis of the Status, Trends and Challenges in the Application of cits.”InternationalJournalofForecasting23,no.2:259–275.
DigitalTechnologytoCulturalHeritageConservation(2019–2024).”npj
Rudzkis, R., and E. Mačiulaitytė. 2007. “Econometrical Modelling of
HeritageScience13.https://doi.org/10.1038/s40494-025-01636-8.
Profit Tax Revenue.” Nonlinear Analysis: Modelling and Control 12,
Litterman, R. B., and M. S. Thomas. 1983. “Using Vector Autoregres- no.1:95–112.
sions to Measure the Uncertainty in Minnesota's Revenue Forecasts.”
Sabaj, E., and M. Kahveci. 2018. Forecasting Tax Revenues in an FederalReserveBankofMinneapolisQuarterlyReview7,no.2:10–22.
EmergingEconomy:TheCaseofAlbania.UniversityLibraryofMunich
Liu, D., Rufei Zhang, and Jaun Li. 2011. “Tax Revenue Combination MPRAPaper84404.
Forecast of Hebei Province Based on the IOWA Operator.” In Fourth
Schroeder,L.2007.“ForecastingLocalRevenuesandExpenditures.”In
International Joint Conference on Computational Sciences and Optimi-
LocalBudgeting,editedbyAnwarShah,53–79.WorldBank.
zation,516–519.IEEE.
Şengüler,H.,andB.Kara.2025.“ForecastingtheInflationforBudget
Lu, S., Zhong‐jian Cai, and X.‐bin Zhang. 2009. “Application of GA‐ Forecasters: An Analysis of ANN Model Performance in Türkiye.”
SVM Time Series Prediction in Tax Forecasting.” In 2nd IEEE Inter-
EkonomiPolitikaveFinansArastirmalariDergisi10,no.1:58–91.
nationalConferenceonComputerScienceandInformationTechnology,
34–36.IEEE. Sexton, T. A. 1987. “Forecasting Property Taxes: A Comparison and
EvaluationofMethods.”NationalTaxJournal40,no.1:47–59. M.Khalifa,H.,S.I.al‐Said,andS.AboulFotouhSaleh.2024.“ASmart
Approach For Budget Deficits Prediction Under Economic Shocks.” Shahnazarian,H.,MartinSolberger,andE.Spanberg.2017.“Forecast-
InternationalJournalofAccountingandManagementSciences3,no.3: ingandAnalyzingCorporateTaxRevenuesinSwedenUsingBayesian
276–308. VARModels.”FinnishEconomicPapers28,no.1:50–74.
Makananisa, M. P., and J. L. Erero. 2018. “Predicting South African Silvestrini,A.,M.Salto,L.Moulin,andD.Veredas.2008.“Monitoring
Personal Income Tax—Using Holt–Winters and SARIMA.” Journal of and Forecasting Annual Public Deficit Every Month: The Case of
EconomicsandManagement31,no.1:24–49. France.”EmpiricalEconomics34:493–524.
McDonald,B.,S.Larson,C.Maher,etal.2024.“EstablishinganAgenda Srinivasan, S., and P. Misra. 2020. “Grants From Centre and States'
forPublicBudgetingandFinanceResearch.”PublicFinanceJournal1, FiscalMarksmanship.”IndianPublicPolicyReview2,no.1:65–83.
no.1:9–28.
Steinnes, D.,and S. Wong. ForecastingState TaxRevenues: ASimple
McNab, R.,M. Rider, and K. Wall. AreErrors in OfficialU.S. Budget Alternative. Working Paper No. 85‐16, Bureau of Business and Eco-
ReceiptsForecastsJustNoise?AndrewYoungSchoolofPolicyStudies nomicResearch,1985.
ResearchPaperNo.07‐22,2005.
Streimikiene,D.,R.RaheemAhmed,J.Vveinhardt,S.P.Ghauri,and
McShea, M., and J. Cordes. 2019. “Forecasting Post‐Crisis Virginia Tax S. Zahid. 2018. “Forecasting Tax Revenues Using Time Series
Revenue.”InThePalgraveHandbookofGovernmentBudgetForecasting, Techniques—A Case of Pakistan.” Economic Research‐Ekonomska
byDanielWilliamsandThadCalabrese,177–200.PalgraveMacmillan. Istraživanja31,no.1:722–754.
Molapo,M. A.,J. O.Olaomi, and N.O. Ama. 2019.“BayesianVector Thayyib, P. V., Muhammed Navas Thorakkattle, F. Usmani,
Auto‐Regression Method as an Alternative Technique for Forecasting A.T.Yahya,andN.H.S.Farhan.2023.“ForecastingIndianGoodsand
SouthAfricanTaxRevenue.”SouthernAfricanBusinessReview23:1–28. ServicesTaxRevenueUsingTBATS,ETS,NeuralNetworks,andHybrid
TimeSeriesModels.”CogentEconomics&Finance11,no.2:1–23.
Mukherjee, S., and R. Bhattacharya. 2023. “Revenue Forecasting of
Corporate Income Tax (CIT) in India.” Indian Economic Review 58: Ticona,W.,K.Figueiredo,andM.Vellasco.2017.“HybridModelBased
329–349. on Genetic Algorithms and Neural Networks to Forecast Tax Collec-
Nandi,B.K.,MuntasirChaudhury,andG.Q.Hasan.2015.“Univariate tion.” In XXIV International Conference on Electronics, Electrical En-
gineeringandComputing(INTERCON),1–4.IEEE.
TimeSeriesForecasting:AStudyofMonthly TaxRevenueofBangla-
desh.”EastWestJournalofBusinessandSocialStudies4:1–28. Ünsal,H., A. Çalişkan, DenizKoçak, and YasinErtürk. 2020. “Kamu
Mali
̇
Yönetim
̇
i
̇ KapsamindaçokDeğiş̇
kenli
̇
gri
̇
Tahmin
̇
Modeli
̇
il
̇
eVergi
̇
Nazmi, N., and H. L. Jane. Forecasting State Income Tax Receipts: A Gelir ̇ leri ̇ Tahmin ̇ i. ̇” Mehmet Akif Ersoy Üniversitesi İktisadi ve İdari
TimeSeriesApproach.BEBRFacultyWorkingPaperNo.1105,1985.
BilimlerFakültesiDergisi7,ÖzelSayı:1104–1120.
Nazmi, N., and J. H. Leuthold. 1988. “Forecasting Economic Time
Series That Require a Power Transformation: Case of State Tax
Voorhees,W.R.2006.“NeuralNetworksandRevenueForecasting:A
Receipts.”JournalofForecasting7,no.3:173–184. Smarter Forecast?” International Journal of Public Policy 1, no. 4:
379–388.
Ofori,M.S.,AbelFumey,andE.Nketiah‐Amponsah.2020.“Forecast-
ing Value Added Tax Revenue in Ghana.” Journal of Economics and Willoughby, K., and H. Guo. 2008. “The State of the Art: Revenue
FinancialAnalysis4,no.2:63–99. Forecasting in US State Governments.” In Government Budget Fore-
casting:TheoryandPractice,editedbyJinpingSunandThomasLynch, Onorante, L., D. J. Pedregal, J. J. Pérez, and S. Signorini. 2010. “The 27–42.Taylor&FrancisGroup.
UsefulnessofInfra‐AnnualGovernmentCashBudgetaryDataforFiscal
Forecasting in the Euro Area.” Journal of Policy Modeling 32, no. 1: Wong(Jeffrey),C.H.,andN.La.2024.“ApplyingMachineLearningin
98–119. TaxRevenueForecasting.”Victoria'sEconomicBulletin8,no.2:1–12.
PublicBudgeting&Finance,2025 17
15405850,
0, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Xie,H.2024.“ResearchontheModelsforForecastofTaxRevenueof
Wenzhou City.” Highlights in Science, Engineering and Technology 88:
1043–1049.
Yang,C.H.,T.Molefyane,andY.D.Lin.2023.“TheForecastingofa
LeadingCountry'sGovernmentExpenditureUsingaRecurrentNeural
NetworkWithaGatedRecurrentUnit.”Mathematics11,no.14:3085.
Yılmaz, E. 2019. “Vergi Gelirlerinin Tahminlenmesine Yönelik Eko-
nometrikModel.”VergiDünyası38,no.449:38–47.
Zakaria, M., and S. Ali. 2010. “Fiscal Marksmanship in Pakistan.”
LahoreJournalofEconomics15,no.2:113–133.
Zhang, Y. 2014. “Research on the Model of Tax Revenue Forecast of
Jilin Province Based on Gray Correlation Analysis.” In Sixth Interna-
tional Conference on Intelligent Human‐Machine Systems and Cyber-
netics,30–33.IEEE.
Zhijun, Y. 2013. “RBF Neural Networks Optimization Algorithm and
Application on Tax Forecasting.” Indonesian Journal of Electrical
Engineering11,no.7:3491–3497.
18 PublicBudgeting&Finance,2025
15405850,
0, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License