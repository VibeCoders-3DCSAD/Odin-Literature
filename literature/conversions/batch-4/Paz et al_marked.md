---
conversion_metadata:
  converted_at: "2026-07-21T08:06:59Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Paz et al.pdf"
  source_pdf_sha256: "8c9e68ba90f8c2e65dd1a82959f4871af2bb7d57ebd0efdb83bb9b70122f0715"
  page_count: 44
  markdown_char_count: 234532
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Article
Interpretable Binary Classification Under Constraints for
Financial Compliance Modeling

Álex Paz 1,2
Felipe Cisternas-Caneo 3
and Ricardo Soto 3

, Broderick Crawford 3,*

, Eric Monfroy 2

, Eduardo Rodriguez-Tello 4

, Benjamín López Cortés 3

, Yoslandy Lazo 3

, Andrés Yáñez 1,2

, José Barrera-García 5,*

,
, Álvaro Peña Fritz 1

1

2

3

Escuela de Ingeniería en Construcción y Transporte, Pontificia Universidad Católica de Valparaíso,
Avenida Brasil 2147, Valparaíso 2362804, Chile; alex.paz@pucv.cl (Á.P.); andres.yanez@pucv.cl (A.Y.);
alvaro.pena@ucv.cl (Á.P.F.)
Laboratoire d’Étude et de Recherche en Informatique d’Angers (LERIA), Université d’Angers, UFR Sciences, 2
Bd de Lavoisier, 49000 Angers, France; eric.monfroy@univ-angers.fr
Escuela de Ingeniería Informática, Pontificia Universidad Católica de Valparaíso, Avenida Brasil 2241,
Valparaíso 2362807, Chile; felipe.cisternas.c@mail.pucv.cl (F.C.-C.); benjamin.lopez.c@mail.pucv.cl (B.L.C.);
yoslandy.lazo@pucv.cl (Y.L.); ricardo.soto@pucv.cl (R.S.)

4 Cinvestav Unidad Tamaulipas, Km. 5.5 Carretera Victoria-Soto La Marina,

5

Victoria 87130, Tamaulipas, Mexico; ertello@cinvestav.mx
Escuela de Negocios y Economía, Pontificia Universidad Católica de Valparaíso, Amunátegui 1838,
Viña del Mar 2580129, Chile

* Correspondence: broderick.crawford@pucv.cl (B.C.); jose.barrera@pucv.cl (J.B.-G.)

Abstract

This study addresses an interpretable supervised binary classification problem under con-
strained feature availability and class imbalance. The objective is to evaluate whether
reliable predictive performance can be achieved using exclusively pre-event administrative
variables while preserving transparency and analytical traceability of model decisions.
A comparative framework is developed using linear and ensemble-based classifiers, com-
bined with resampling strategies and exhaustive hyperparameter optimization embedded
within cross-validation. Model performance is evaluated using standard classification met-
rics, with particular emphasis on the Matthews correlation coefficient as a robust measure
under imbalance. In addition to predictive accuracy, the analysis incorporates global, struc-
tural, and local interpretability mechanisms, including permutation feature importance,
explicit decision paths derived from tree-based models, and additive local explanations.
Experimental results show that optimized ensemble models achieve consistent performance
gains over linear baselines while maintaining a balanced error structure across classes.
Importantly, the most influential predictors exhibit stable rankings across models and
explanation methods, indicating a concentrated and robust discriminative signal within
the constrained feature space. The interpretability analysis demonstrates that complex
classifiers can be decomposed into verifiable decision rules and locally coherent feature
contributions. Overall, the findings confirm that interpretable supervised classification can
be reliably conducted under administrative data constraints, providing a reproducible mod-
eling framework that balances predictive performance, error analysis, and explainability in
applied mathematical settings.

Keywords: binary classification; supervised learning; class imbalance; error analysis;
Matthews correlation coefficient; model interpretability; higher education finance

MSC: 62H30; 62P20; 68T37

Academic Editor: Zengjing Chen

Received: 31 December 2025

Revised: 18 January 2026

Accepted: 23 January 2026

Published: 26 January 2026

Copyright: © 2026 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license.

Mathematics 2026, 14, 429

https://doi.org/10.3390/math14030429

---

<!-- PAGE 2 -->

Mathematics 2026, 14, 429

2 of 44

1. Introduction
1.1. Background and Motivation

Income-contingent student loan systems rely on annual borrower compliance to ensure
both equity and financial sustainability. From a computational perspective, monitoring
such compliance can be formulated as a prediction problem under uncertainty, where
decisions must be made using limited and heterogeneous information available prior
to critical administrative deadlines. In this context, supervised learning models offer a
systematic framework for estimating the likelihood of borrower compliance based on
historical academic and administrative records [1,2].

In Chile, the University Credit Solidarity Fund (Fondo Solidario de Crédito Universi-
tario, FSCU) constitutes a large-scale income-contingent loan system administered at the
institutional level. The program generates extensive structured data describing academic
trajectories, loan characteristics, and administrative events, which can be represented as
high-dimensional feature spaces suitable for predictive modeling. However, the effective
use of this information is challenged by class imbalance, delayed outcomes, and the need
for transparent decision rules [3,4].

At the Pontificia Universidad Católica de Valparaíso (PUCV), a significant proportion
of undergraduate students are beneficiaries of the FSCU, making early identification of
non-compliance patterns a recurring operational problem. While detailed administrative
records are routinely collected, their potential for predictive analysis has not been fully
exploited. This motivates the application of machine learning techniques that can transform
institutional data into quantitative risk estimates, enabling anticipatory decision-making.
Beyond this specific case, the problem addressed in this study reflects a broader
class of data-driven classification tasks in which outcomes depend on socioeconomic and
behavioral variables observed prior to an event of interest. As such, it provides a relevant
setting for evaluating supervised learning models under realistic constraints of imbalance,
interpretability, and limited observability.

1.2. Problem Statement in the Context of FSCU

The University Credit Solidarity Fund (Fondo Solidario de Crédito Universitario, FSCU)
is a state-backed student loan system applied at Chilean universities affiliated with the
Council of Rectors (CRUCH) [5]. Its operational design establishes a repayment mechanism
that relies on the borrower’s annual income declaration to determine whether the debt
installment is adjusted to income or fixed under statutory rules.

From a modeling perspective, this mechanism induces a binary observable outcome
at the borrower level. Let yi ∈ {0, 1} denote the declaration status of borrower i, where
yi = 1 represents the timely submission of the income declaration and yi = 0 otherwise.
The outcome is governed by the legal framework established by Law No. 19,287 [6] and
its amendment in Law No. 20,572 [7], which mandate annual declarations and impose
asymmetric consequences for compliant and non-compliant borrowers.

Official institutional reports document persistent levels of non-declaration and repay-
ment difficulties among FSCU beneficiaries, particularly among borrowers with incomplete
academic trajectories or greater socioeconomic vulnerability [8,9]. In addition, the structure,
availability, and accounting treatment of the administrative records used for monitoring
and collection are formally defined by regulatory guidelines issued by the Superintendence
of Higher Education [10]. These elements establish the empirical and operational context
in which declaration outcomes are observed and recorded.

Crucially, the declaration decision must be made using only information available
before the declaration deadline. Let X ∈ Rn×p denote the matrix of pre-declaration features
describing academic trajectories, loan characteristics, and administrative records for a

https://doi.org/10.3390/math14030429

---

<!-- PAGE 3 -->

Mathematics 2026, 14, 429

3 of 44

cohort of n borrowers. The problem addressed in this study consists of estimating the
conditional probability of declaration compliance under conditions of class imbalance,
heterogeneous features, and delayed outcome realization, defined as

P(y = 1 | X),

(1)

where y = 1 indicates timely submission of the income declaration.

The FSCU collection process further constrains the prediction task. Borrowers who
submit their income declaration are assigned a variable installment proportional to their
reported income. In contrast, non-compliant borrowers are automatically assigned fixed
installments with longer repayment horizons and the loss of associated benefits [11]. These
asymmetric outcomes create a strong incentive structure, making early identification of
non-compliance particularly relevant for institutional planning.

Accordingly, the problem can be formalized as a supervised binary classification task
with interpretability requirements, where predictions are intended to support anticipatory
decision-making rather than automated enforcement. This formulation enables analysis of
the FSCU case within a general mathematical framework applicable to income-contingent
mechanisms and compliance-related prediction problems.

1.3. Research Objectives and Questions

The objective of this study is to construct and evaluate supervised classification models
that estimate whether a beneficiary of the FSCU at the Pontificia Universidad Católica de
Valparaíso (PUCV) will submit their first annual income declaration. The prediction is
performed using exclusively pre-declaration academic, socioeconomic, and administra-
tive features, framing the task as a binary classification problem under institutional and
informational constraints.

More specifically, this study aims to

•

•

Identify the pre-declaration variables that contribute most to the prediction of income
declaration compliance.
Evaluate the predictive performance of multiple supervised machine learning algo-
rithms under class imbalance conditions.

• Assess the interpretability of model outputs through feature importance and explana-

tion techniques in an institutional data setting.

Based on these objectives, the following research questions are formulated:

1.

2.

3.

RQ1: Which pre-declaration variables exhibit the strongest predictive contribution to
income declaration compliance?
RQ2: How accurately can supervised learning models predict declaration outcomes
using only information available before the declaration cycle?
RQ3: To what extent can interpretable classification models provide transparent
and reliable predictions under institutional data constraints, beyond predictive accu-
racy alone?

This study does not aim to introduce new learning algorithms nor novel imbalance-
handling techniques. Instead, it adopts a deliberately applied and institutionally grounded
perspective. The originality of the work lies in the formulation and validation of a predictive
framework designed under realistic administrative constraints, where only pre-declaration
information is available and severe class imbalance is inherent to the problem. By prioritiz-
ing operational feasibility, methodological coherence, and audit-oriented interpretability
over algorithmic novelty, the study addresses a gap in applied machine learning research,
where predictive models are often evaluated under conditions misaligned with real-world
institutional deployment.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 4 -->

Mathematics 2026, 14, 429

4 of 44

1.4. Intended Contributions

This study makes the following contributions to the applied machine learning literature:

• A pre-event predictive problem formulation grounded in realistic administrative
constraints, explicitly reflecting the information available to institutions before the
target compliance behavior occurs.

• A controlled and reproducible methodological pipeline for benchmarking established
supervised learning models and imbalance-handling strategies under a unified valida-
tion and partitioning protocol.

• An imbalance-appropriate evaluation strategy that prioritizes the Matthews Correla-
tion Coefficient (MCC) as the primary performance metric, explicitly linking model
assessment to the balanced management of Type I and Type II errors in severely
imbalanced settings.

• A triangulated interpretability design that combines global, structural, and local
explanation methods, positioned as an audit mechanism to support institutional
decision-making rather than as a claim of direct model transparency.
A transferability analysis that distinguishes context-specific elements from pipeline-level
methodological insights applicable to other income-contingent financing schemes and
administrative compliance prediction problems under similar pre-event constraints.

•

1.5. Structure of the Paper

The remainder of this paper is organized as follows: Section 2 reviews the most
relevant studies and outlines the main research gaps identified in the literature. Section 3
describes the databases, selection criteria, and methodological framework adopted for the
empirical analysis. Section 4 details the experimental design and evaluation procedures
applied to ensure replicability and transparency. Section 5 presents the main findings
obtained from the comparative analysis. Section 6 discusses these findings in light of
existing evidence and highlights the implications for future research. Finally, Section 7
summarizes the conclusions and proposes potential directions for further investigation.

2. Related Work
2.1. Abandonment and Default Risk Prediction

Student loan repayment and abandonment have become persistent concerns in higher
education financing systems, particularly in contexts where repayment depends on long-
term income trajectories rather than fixed installment schedules. In income-contingent
systems such as those implemented in Australia and the United Kingdom, legal default
is relatively uncommon; instead, the central challenge lies in anticipating long-run non-
repayment and associated fiscal risks [12,13]. Conversely, systems with weaker collection
mechanisms or limited income linkage tend to exhibit higher levels of arrears and bor-
rower distress [14,15]. These contrasting designs highlight the importance of early risk
identification over ex post recovery.

Comparative policy analyses consistently identify academic non-completion and so-
cioeconomic vulnerability as primary structural drivers of repayment difficulties [8,15].
Borrowers who fail to complete their programs or who enter informal labor markets ex-
hibit reduced repayment capacity and higher probabilities of falling into arrears. From
a modeling perspective, these findings motivate the use of predictive approaches capa-
ble of integrating academic, socioeconomic, and administrative information to estimate
repayment or compliance risk before adverse outcomes materialize.

Recent studies have demonstrated the effectiveness of machine learning techniques for
predicting repayment-related outcomes. Thuy et al. [16] showed that machine learning and
deep learning models outperform traditional statistical approaches in student credit scoring

https://doi.org/10.3390/math14030429

---

<!-- PAGE 5 -->

Mathematics 2026, 14, 429

5 of 44

tasks. Related work in educational analytics further supports the use of institutional admin-
istrative data for early risk detection. For instance, Suleiman and Anane [17] and Yakubu
and Abubakar [18] applied supervised learning models to academic and socioeconomic
data to predict student performance and progression, demonstrating that profile-based
representations improve predictive accuracy.

Taken together, the literature indicates that repayment distress and non-compliance
behaviors can be framed as predictive problems driven by multidimensional risk factors
observable before default or abandonment. This perspective supports the development of
supervised classification models that estimate the likelihood of adverse outcomes using
pre-event institutional data, providing the methodological foundation for the approach
adopted in this study.

2.2. Profile-Based Representation in Predictive Modeling

The representation of individuals through multidimensional profiles plays a central
role in predictive modeling for higher education and credit-related applications. Tradi-
tional econometric approaches typically rely on a limited set of explanatory variables, such
as income, loan amount, or repayment history, to model default or non-compliance out-
comes [19]. While these models offer interpretability, they often fail to capture the complex
interactions that arise when academic, socioeconomic, and administrative factors jointly
influence borrower behavior, a limitation that has motivated the adoption of machine
learning techniques in both educational and credit risk settings [20].

From a machine learning perspective, profile-based modeling represents each individ-
ual as a feature vector in a multidimensional space, allowing heterogeneous attributes to be
integrated within a unified predictive framework. Institutional datasets commonly include
variables describing academic trajectories, enrollment continuity, completion status, and
financial characteristics, which can be transformed into structured feature representations
suitable for supervised learning. Empirical evidence suggests that such representations
often contribute more to predictive performance than the specific choice of algorithm. For
example, Suleiman and Anane [17] demonstrated that regression-based machine learning
applied to institutional data can successfully identify at-risk students, emphasizing the
importance of feature construction. Similarly, Yakubu and Abubakar [18] showed that com-
bining socioeconomic, demographic, and academic variables improves predictive accuracy
in educational contexts.

In credit management settings, the same representational logic applies. Borrower
profiles that integrate academic progression, socioeconomic background, and adminis-
trative engagement can reveal latent patterns associated with future non-compliance or
repayment distress. By embedding these profiles in a high-dimensional feature space,
machine learning models can capture nonlinear relationships among variables that are not
readily captured by linear modeling assumptions [21].

Overall, the literature supports the view that profile-based representation is a critical
determinant of model effectiveness in predictive tasks involving heterogeneous institu-
tional data. This insight motivates the adoption of supervised learning models that leverage
structured feature spaces to estimate compliance-related outcomes, forming a key method-
ological pillar of the approach proposed in this study.

Taken together, the reviewed literature highlights two converging insights. First,
repayment distress and compliance-related outcomes in student loan systems are driven by
multidimensional factors that extend beyond purely financial attributes. Second, integrat-
ing academic, socioeconomic, and administrative data into profile-based representations
enables more accurate and robust predictive modeling. These findings motivate the devel-
opment of supervised learning approaches that treat compliance behavior as a classification

https://doi.org/10.3390/math14030429

---

<!-- PAGE 6 -->

Mathematics 2026, 14, 429

6 of 44

problem in heterogeneous feature spaces under class-imbalance constraints. Building on
this methodological foundation, the following section describes the data sources, feature
construction, and modeling procedures adopted in this study.

3. Materials and Methods
3.1. Data Sources and Legal Context

Each year, the PUCV Finance Department requests that borrowers submit their income
declaration by 31 May. The declaration form includes personal identification, contact
information, pension affiliation, and the borrower’s monthly gross income, as well as that
of the spouse, when applicable. Supporting documents are required for verification. All
information is integrated into the university system and stored in a relational database.

In this study, we set a cutoff date of 24 April 2024, and restrict the analysis to obligations
maturing from 2012 onward, following the 2012 legal reform that standardized the annual
income-declaration process. Focusing on the post-reform period ensures a consistent
operational regime and avoids structural breaks caused by legacy rules.

3.2. Database Schema

The source database comprises eight relational tables with historical records of the
FSCU portfolio and enrollment information: Person, Promissory Note, Due Group, Debt,
Installment, Payment Slip, Income Declaration, and Enrollments. For data management and
query performance, the contents were migrated to PostgreSQL prior to dataset construction.

3.3. Cohort Definition and Target

The working dataset is constructed at the borrower level using exclusively information
available prior to the first income-declaration deadline. Let yi ∈ {0, 1} denote the declara-
tion outcome for borrower i, where yi = 1 indicates submission of the first income declara-
tion and yi = 0 otherwise. To ensure consistency with the current operational regime, only
records corresponding to obligations maturing from 2012 onward were included, following
the legislative reform that standardized the annual income-declaration process.

The feature space comprises numerical, categorical, and date-derived variables describ-
ing borrower demographics, loan characteristics, and academic trajectory. Exact variable
counts by type are reported in Table 1. In total, the initial dataset consists of the binary
target variable and a heterogeneous collection of features derived from administrative and
academic records available before the declaration event.

As discussed in Section 1, compliance with the income-declaration requirement plays
a central role in the functioning of income-contingent loan systems. From a modeling
perspective, understanding the factors associated with first-time declaration behavior is
essential for characterizing compliance patterns under informational constraints.

Accordingly, this study focuses on predicting whether a borrower will submit the first
income declaration using pre-declaration information only, including attributes related
to the borrower profile, loan characteristics, and academic history. By analyzing both
compliant and non-compliant cases, the objective is to identify systematic patterns that can
inform classification-based risk estimation within a supervised learning framework.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 7 -->

Mathematics 2026, 14, 429

7 of 44

Table 1. Initial feature pool prior to preprocessing.

Name

Data Type

Feature Type

Detail

Boolean
estado_civil
Boolean
nacionalidad
Boolean
sexo
Date
fecha_nacimiento
Integer
edad
Integer
edad_dias
deud_monto
Float
deud_fecha_exigibilidad Date
deud_t_deuda
tiene_declaracion
monto_total_pagare
conteo_pagare
anio_ult_matr
e_ult_matr
cod_carr_ult_matr
carr_t_carrera
cod_inst_ult_matr
conteo_matr
facultad
escuela
stem

Integer
Boolean
Float
Integer
Integer
Integer
Integer
Integer
Integer
Integer
String
String
Boolean

Categorical
Categorical
Categorical
Date
Numerical
Numerical
Numerical
Date
Categorical
Target
Numerical
Numerical
Categorical
Categorical
Categorical
Categorical
Categorical
Numerical
Categorical
Categorical
Categorical

1 and 2
1 and 2
M and F
1 January 1900 to 26 March 1991
21 to 119
7860 to 43,646
0.571 to 1285.762
1 January 1994 to 1 January 2023
1 value
0 and 1
1.32 to 922.22
1 to 29
13 values
1 value
80 values
1 value
1 value
1 to 31
9 values
34 values
0 and 1

3.4. Feature Construction

The feature construction process was guided by the need to balance predictive ex-
pressiveness, interpretability, and strict temporal validity. In particular, all representations
were deliberately constrained to borrower-level summaries observable before the first
income-declaration deadline, reflecting the information realistically available for institu-
tional decision-making at that stage.

The predictive task requires a borrower-level representation in which each observation
corresponds to the information available before the first income-declaration deadline. Ac-
cordingly, a flat dataset was constructed, where each row represents a unique borrower and
each column corresponds to a pre-declaration attribute derived from academic, financial,
or administrative records.

Let D = {(Xi, yi)}n

i=1 denote the resulting dataset, where Xi ∈ Rp is the feature vector
associated with borrower i, and yi ∈ {0, 1} indicates whether the borrower submitted
the first income declaration. Feature construction was strictly constrained to information
observable before the declaration deadline to prevent temporal leakage.

The original data are stored in a relational schema comprising multiple tables with one-
to-many relationships, such as enrollment records and promissory notes. To obtain a fixed-
dimensional representation suitable for supervised learning, borrower-level aggregation
operators were applied to recurring records. In particular, count-based and sum-based
aggregations were used to summarize enrollment history and loan-related information,
yielding scalar features that preserve cumulative exposure while ensuring dimensional
consistency across observations.

Two additional categorical attributes describing the undergraduate program were
appended after extraction. These variables are static with respect to the prediction horizon
and do not depend on post-declaration information, making them admissible for inclusion
in the pre-declaration feature space.

A small subset of borrowers holds more than one loan in the source database (166 cases,
representing less than 0.01% of the sample). To preserve a consistent unit of analysis

https://doi.org/10.3390/math14030429

---

<!-- PAGE 8 -->

Mathematics 2026, 14, 429

8 of 44

and avoid duplicate borrower histories, only the first loan per borrower was retained.
Previously, for borrowers with multiple loans, the feature vector Xi was constructed from
the earliest loan record, ensuring that each observation corresponds to a single, well-defined
prediction instance.

As a result, the final feature matrix X ∈ Rn×p provides a borrower-centric, fixed-
dimensional representation that integrates academic trajectory, loan characteristics, and
institutional attributes available prior to the declaration event. This construction enables
the application of standard supervised classification algorithms while maintaining a clear
correspondence between model inputs and the underlying administrative processes.

3.5. Feature Set Overview

The modeling process begins with an initial pool of features extracted from academic
and administrative records available prior to the first income-declaration deadline. This ini-
tial feature pool is subsequently refined through the data cleaning, consolidation, encoding,
and transformation steps described in the following subsections, yielding a reduced and
consistent feature set used for model training and evaluation.

For transparency and reproducibility, both the initial feature pool and the final feature
set are reported. Table 1 summarizes the variables initially extracted from the source
databases, while Table 2 provides semantic descriptions of the initially extracted variables
prior to any preprocessing, consolidation, or feature selection steps. Variable names are
retained in their original Spanish form, as they correspond directly to field identifiers used
in the official FSCU administrative databases. In Table 3 reports the variables exhibiting
missing observations. Table 4 reports the features retained after preprocessing and feature
engineering. Preserving this nomenclature ensures traceability, consistency, and alignment
with operational institutional data structures. For clarity, all variables are explicitly de-
scribed and interpreted in English within the table, allowing international readers to follow
the analysis without ambiguity.

Table 2. Feature set: detailed descriptions of each variable.

Feature

Description

estado_civil
nacionalidad
sexo
fecha_nacimiento
edad
edad_dias
deud_monto
deud_fecha_exigibilidad Date of enforceability of the loan
deud_t_deuda

Last known marital status of the debtor. It can take the following values: 1 not married, 2 married
Whether the debtor is Chilean or foreign. 1 means Chilean, 2 means foreign
Gender of the debtor. M means male and F means Female
Birth date of the debtor
Age in years of the debtor at the moment that the debt is enforceable
Age in days of the debtor at the moment that the debt is enforceable.
Total loan amount

tiene_declaración

monto_total_pagare
conteo_pagare
anio_ult_matr
e_ult_matr
cod_carr_ult_matr
carr_t_carrera
cod_inst_ult_matr
conteo_matr
facultad
escuela

stem

Type of loan contracted
Whether the debtor handed their first income declaration or not. 1 Means they handed it and 0 means
they did not. Target Variable
Total value of promissory notes signed by the debtor
Amount of promissory notes signed by the debtor
Year of the last college enrollment of the debtor
Status of the last college enrollment of the debtor. 1 means the enrollment has a valid status
Code of the degree program covered by the loan
Type of degree program in the last college enrollment of the debtor. 1 means undergraduate program
Institution code in the last college enrollment of the debtor
Total amount of enrollments of the debtor within the degree program covered by the loan
Faculty of the degree program
School of the degree program
Whether the degree program covered by the loan is a STEM one or not. 1 means the degree program is
a STEM program, 0 means it is not

https://doi.org/10.3390/math14030429

---

<!-- PAGE 9 -->

Mathematics 2026, 14, 429

9 of 44

Reporting both the initial and final feature sets allows the reader to trace how method-
ological decisions progressively reduce dimensionality while preserving institutional mean-
ing, thereby supporting transparency and reliability in an applied administrative context.

3.6. Data Cleaning and Preprocessing

Data cleaning and preprocessing decisions were driven by the dual objective of pre-
serving as much administratively meaningful information as possible while ensuring
numerical stability and interpretability under severe class imbalance. Rather than ap-
plying aggressive filtering or imputation, the adopted strategy prioritizes conservative
transformations aligned with institutional data quality and deployment constraints.

3.6.1. Missing Values

Figure 1 summarizes the number of missing values observed in each extracted feature.
This exploratory analysis enables the identification of variables affected by incomplete
information and guides subsequent preprocessing decisions.

Figure 1. Missing values across dataset features compared to the dataset size (red-dotted line).

Five variables exhibit missing observations, as reported in Table 3. The variables
fecha_nacimiento, edad, and edad_dias present identical missingness patterns, since the latter
two are deterministically derived from the birth date. Given the high proportion and
complete overlap of missing values across these three attributes, they were excluded from
the feature set to avoid redundant loss of information and unstable imputations.

Formally, let X ∈ Rn×p denote the original feature matrix. The filtered feature matrix
X′ was obtained by removing the columns corresponding to the affected variables such that

X′ = X \ {fecha_nacimiento, edad, edad_dias}.

(2)

In contrast, the variable escuela presents a small number of missing values corre-
sponding to degree programs without an associated school. Rather than discarding these
observations, a dedicated categorical level was introduced to encode the absence of an as-
signed school, thereby preserving the affected records and retaining potentially informative
structure in the data.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 10 -->

Mathematics 2026, 14, 429

10 of 44

Table 3. Features with missing values.

Column Name

sexo
fecha_nacimiento
edad
edad_dias
escuela

Missing Values

9583
9614
9614
9614
22

This handling strategy reflects a deliberate trade-off between information retention
and model robustness, favoring the exclusion of highly incomplete and redundant variables
while preserving partially missing categorical information through explicit encoding.

3.6.2. Class Consolidation and Rare Categories

Class consolidation decisions were guided by the need to reduce sparsity and unstable
parameter estimation while maintaining a semantically coherent representation aligned
with institutional practice.

To assess the distributional properties of the constructed feature space, an exploratory
analysis was performed on both numerical and categorical variables. Figures 2–4 sum-
marize the empirical distributions observed across the dataset and provide guidance for
subsequent consolidation decisions.

(a) conteo_matr Distribution

(b) conteo_pagare Distribution

(c) deud_monto Distribution

(d) monto_total_pagare Distribution

Figure 2. Distribution of selected numerical features.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 11 -->

Mathematics 2026, 14, 429

11 of 44

(a) estado_civil Distribution

(b) deud_t_deuda Distribution

(c) tiene_declaracion Distribution

(d) anio_ult_matr Distribution

(e) e_ult_matr Distribution

Figure 3. Distribution of selected categorical features (Part I).

Numerical Feature Distribution

Figure 2 present the distributions of selected numerical variables, including the
number of enrollments (conteo_matr), the number of promissory notes (conteo_pagare),
the outstanding debt amount (deud_monto), and the total value of promissory notes
(monto_total_pagare).

Although some variables exhibit similar distributional shapes (e.g., Figure 2c,d), none
of the numerical features display degenerate or constant behavior. Consequently, all

https://doi.org/10.3390/math14030429

---

<!-- PAGE 12 -->

Mathematics 2026, 14, 429

12 of 44

numerical variables were retained at this stage and further examined through correlation
analysis to evaluate potential redundancy, as discussed in Section 3.6.3.

(a) carr_t_carrera Distribution

(b) cod_inst_ult_matr Distribution

(c) facultad Distribution

(d) stem Distribution

Figure 4. Distribution of selected categorical features (Part II).

Categorical Feature Distribution

Figures 3–6 illustrate the empirical distributions of the categorical variables. These
features describe marital status, loan attributes, declaration status, academic trajectory,
and institutional affiliation. The visual inspection highlights dominant categories, sparsity
patterns, and variables with limited variability.

Categorical variables exhibiting invariant behavior within the analyzed cohort were re-
moved, as they provide no discriminative information for the classification task. Specifically,
the features carr_t_carrera, cod_inst_ult_matr, deud_t_deuda, and e_ult_matr were excluded
from the feature set.

Very low-frequency categories were also addressed to reduce sparsity and prevent
unstable parameter estimation. The “foreign” category in nacionalidad, comprising six ob-
servations, was removed due to its negligible representation. Similarly, a single observation
corresponding to the year 2008 in anio_ult_matr was excluded. To further control categorical
cardinality, the variables cod_carr_ult_matr and escuela were consolidated at the facultad
level, yielding a more compact and semantically coherent representation.

In addition, a small subset of borrowers holds more than one FSCU debt associated
with the same institution (166 cases, representing less than 0.01% of the final sample after
excluding non-PUCV loans). These records correspond to second or subsequent debts
acquired by the same borrower, rather than to independent or parallel loan events. To
preserve a consistent and institutionally meaningful unit of analysis, only the first FSCU

https://doi.org/10.3390/math14030429

---

<!-- PAGE 13 -->

Mathematics 2026, 14, 429

13 of 44

debt per borrower was retained. Including secondary debts as separate observations would
implicitly introduce a longitudinal dimension based on a very limited number of cases,
increasing model complexity while risking bias toward atypical borrower trajectories.

Figure 5. cod_carr_ult_matr Distribution.

Figure 6. escuela Distribution.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 14 -->

Mathematics 2026, 14, 429

14 of 44

This aggregation strategy was further validated in consultation with the FSCU man-
agement unit at PUCV, which confirmed that the first debt constitutes the primary admin-
istrative reference for enforceability and early-stage monitoring processes. Accordingly,
the resulting dataset adopts a borrower-centric representation aligned with institutional
practice while avoiding unnecessary dimensional expansion or instability in subsequent
modeling stages.

After consolidating categorical variables and reducing sparsity, the resulting feature
space was examined for redundancy among numerical attributes, as detailed in the follow-
ing subsection.

3.6.3. Correlation Screening

Correlation screening was introduced as a pragmatic dimensionality-reduction step to
mitigate multicollinearity effects that could distort both model estimation and downstream
interpretability analyses.

To identify potential redundancy among numerical variables, pairwise linear depen-
dence was assessed using Pearson’s correlation coefficient. Let xj and xk denote two
numerical features. Their Pearson correlation is defined as

rjk =

cov(xj, xk)
σxj σxk

,

(3)

where cov(·, ·) denotes covariance and σx the standard deviation of variable x.

Figure 7 presents the empirical correlation matrix computed over the numerical feature
subset. A threshold of |rjk| ≥ 0.70 was adopted as a pragmatic criterion to flag pairs of
variables exhibiting strong linear association and, therefore, potential collinearity.

Figure 7. Pearson correlation heatmap among numerical features.

Three variable pairs exceeded the selected threshold: (deud_monto, monto_total_pagare),
(monto_total_pagare, conteo_pagare), and (deud_monto, conteo_pagare). To mitigate multi-
collinearity effects, only one representative variable from this correlated group was retained.
Specifically, deud_monto was preserved due to its direct interpretability and explicit associa-
tion with the loan magnitude, while monto_total_pagare and conteo_pagare were removed
from the feature set.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 15 -->

Mathematics 2026, 14, 429

15 of 44

Formally, let Fnum denote the set of numerical features prior to screening and F ′

num

the reduced set after correlation filtering. The selection can be expressed as

F ′

num = Fnum \ {monto_total_pagare, conteo_pagare}.

(4)

This selection balances dimensional parsimony and interpretability, ensuring that
strongly collinear monetary variables do not distort model estimation, numerical stability,
or feature importance analyses in subsequent classification stages.

3.6.4. Encoding and Scaling

To ensure compatibility with supervised learning algorithms and to avoid introducing
artificial ordinal relationships, categorical variables were transformed using one-hot en-
coding. Let x(c) ∈ C denote a categorical feature taking values in a finite set of categories.
The encoding maps x(c) to a binary vector in {0, 1}|C|, where each component indicates the
presence of a specific category. This transformation preserves category membership while
enabling linear and non-linear classifiers to operate on a numerical feature space.

This choice ensures that categorical distinctions are preserved without imposing artifi-
cial ordinality, while numerical scaling supports stable optimization across heterogeneous
model families.

Numerical variables were standardized to ensure comparable scales and stable nu-
merical behavior during model training. Given a numerical feature x, standardization was
performed using the z-score transformation

z =

x − µ
σ

,

(5)

where µ and σ denote the sample mean and standard deviation, respectively. This transfor-
mation yields features with zero mean and unit variance, reducing scale dominance effects
in distance-based and gradient-based learning algorithms.

The combined preprocessing pipeline can be viewed as a transformation

Φ : X → ˜X,

(6)

where X denotes the original feature matrix and ˜X the encoded and standardized represen-
tation used for model estimation.

This preprocessing strategy preserves interpretability while improving numerical sta-
bility and reducing noise during training. In particular, by retaining a single representative
monetary feature following correlation screening, the transformation avoids redundancy
among variables expressing similar financial magnitude and maintains a clear conceptual
link between financial exposure and the probability of non-compliance.

After encoding categorical variables and scaling numerical ones, temporal features

were processed separately, as described in the following subsection.

3.6.5. Date Handling

Temporal variables were handled with particular caution to retain interpretability while
avoiding unnecessary dimensional expansion in a setting with limited temporal granularity.
After preprocessing categorical and numerical variables, temporal information was
handled separately. Only one date-related attribute remains in the feature set, namely
deud_fecha_exigibilidad. Its empirical distribution, as shown in Figure 8, exhibits two pro-
nounced density valleys associated with specific enforceability periods, while the remaining
dates present relatively uniform frequencies. The aforementioned valleys are specifically

https://doi.org/10.3390/math14030429

---

<!-- PAGE 16 -->

Mathematics 2026, 14, 429

16 of 44

January first of 2013 with six values and January second of 2022 with one value. For context,
January third of 2013 has 1109 values, while January first of 2022 has 1006 values.

Figure 8. Distribution of enforceability dates (deud_fecha_exigibilidad).

To obtain a numerical representation suitable for supervised learning, the date variable
was decomposed into its constituent components: day, month, and year. Let di denote the
enforceability date associated with borrower i. The transformation can be expressed as

di (cid:55)−→ (dayi, monthi, yeari).

(7)

The resulting marginal distributions of these components are shown in Figure 9 as
Histograms with a Kernel Density Estimate to provide a smooth picture of the distribution.
As all observations correspond to the same calendar month (May), as evidenced in Figure 9b,
the month component exhibits zero variance across the dataset and therefore provides no
discriminative information for the classification task. Consequently, it was excluded from
the feature set.

(a) Day Distribution

(b) Month Distribution

(c) Year Distribution

Figure 9. Decomposition of enforceability dates into day, month, and year components.

The retained temporal components thus define a reduced representation (dayi, yeari),
operationalized in the final dataset as the variables dia_exigibilidad and anio_exigibilidad.
This decomposition ensures that the numerical encoding of dates remains informative yet
parsimonious, facilitating consistent scaling and interpretation within the machine learning
pipeline and allowing temporal information to contribute meaningfully to the estimation
of classification functions without introducing unnecessary dimensional complexity.

The resulting feature matrix and target variable, presented in Table 4, were subsequently
used to train and evaluate supervised classification models under a consistent validation
protocol. The next section describes the computational setup, training and testing strategy,
and evaluation metrics.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 17 -->

Mathematics 2026, 14, 429

17 of 44

Table 4. Final feature set used for model training after preprocessing and feature engineering.

Name

Data Type

Feature Type Detail

estado_civil
nacionalidad
sexo
deud_monto
dia_exigibilidad
anio_exigibilidad
anio_ult_matr
conteo_matr
facultad
stem

Boolean
Boolean
Boolean
Float
Integer
Integer
Integer
Integer
String
Boolean

Categorical
Categorical
Categorical
Numerical
Numerical
Numerical
Categorical
Numerical
Categorical
Categorical

1 and 2
Filtered (foreign category removed)
M and F
standardized
1 to 31
multiple years
filtered values
1 to 31
9 values
0 and 1

tiene_declaracion Boolean

Target

0 and 1

4. Experimental Setup

This section describes the complete experimental configuration used to evaluate the
proposed supervised binary classification framework. All stages of data partitioning, pre-
processing, resampling, model training, hyperparameter optimization, and evaluation were
designed to ensure methodological rigor and to prevent information leakage, supporting
reliable and auditable empirical assessment.

4.1. Computational Environment

All experiments were executed on a dedicated server equipped with an Intel Core
i9-10900K CPU and 64 GB of DDR4 RAM. Data manipulation and numerical operations
were conducted using Pandas (v2.1.4) and NumPy (v1.26.3). Machine learning models were
implemented using scikit-learn (v1.7.1), while gradient boosting models were trained
using LightGBM (v4.6.0). Class imbalance techniques were applied via imbalanced-learn
(v0.14.0). Feature attribution analyses were supported by the SHAP library (v0.48.0).

4.2. Data Partitioning and Validation Protocol

The dataset was initially divided into a training set (70%) and an independent test set
(30%) as a widely adopted practice in the machine learning literature (e.g., [22,23]), and
because it provides a sufficiently large hold-out set to obtain stable and reliable estimates
of performance metrics under class imbalance. From an operational perspective, this split
enables a clear separation between model development and final evaluation, with the test
set serving as a proxy for unseen future cohorts, while preserving enough training data to
support robust model fitting and cross-validated hyperparameter tuning.

Within the training set, all model selection and hyperparameter tuning procedures
were conducted using stratified K-fold cross-validation. This strategy ensures that class
proportions remain consistent across folds and provides an unbiased estimate of gener-
alization performance. At each fold, preprocessing, resampling, and model fitting were
performed exclusively on the corresponding training partition, thereby preventing any
form of data leakage.

4.3. Pipeline Structure

Each experiment followed a unified pipeline architecture composed of the following

sequential stages:

Training–validation split according to the cross-validation fold.
Feature scaling when required by the learning algorithm.

1.
2.
3. Application of class imbalance handling techniques.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 18 -->

Mathematics 2026, 14, 429

18 of 44

4. Model training using a specific hyperparameter configuration.
5.

Validation performance estimation using predefined evaluation metrics.

All transformations were fitted exclusively on training data within each fold and
subsequently applied to the corresponding validation subset. This pipeline was applied
uniformly across all experiments.

4.4. Predictive Models

Seven supervised learning algorithms were evaluated: K Nearest Neighbors, Naive
Bayes, Logistic Regression, Linear Support Vector Classifier, Decision Tree, Random Forest,
and Light Gradient Boosting Machine. Non-linear kernel variants of Support Vector
Machines were excluded after preliminary analysis due to consistently inferior performance
on the studied feature space.

4.5. Class Imbalance Handling

The target variable exhibits a pronounced class imbalance, with the non-declaration
class representing the minority group. To address this issue, three resampling strate-
gies were evaluated within the training folds, following standard approaches for learn-
ing from imbalanced data [3]. The resampling procedures were implemented using the
imbalanced-learn library [24]:

Synthetic Minority Over-Sampling Technique (SMOTE),

•
• Adaptive Synthetic Sampling (ADASYN),
•

Random Under-Sampling of the majority class.

The choice of resampling method and its associated parameters were treated as hy-
perparameters and jointly optimized with the classifier configuration. Resampling was
applied exclusively to the training portion of each cross-validation fold.

4.6. Hyperparameter Optimization

Model and sampling hyperparameters were optimized using an exhaustive grid
search strategy embedded within the cross-validation procedure applied to the training set.
Let Θ denote the discrete search space defined by the Cartesian product of all candidate
hyperparameter values for a given model–sampling configuration. For each θ ∈ Θ, model
performance was estimated using stratified K-fold cross-validation.

Formally, let MCCk(θ) denote the Matthews Correlation Coefficient obtained on the
validation subset of the k-th fold when training the model with configuration θ. The
optimal hyperparameter configuration ˆθ was selected by maximizing the mean validation
performance across folds, defined as

ˆθ = arg max
θ∈Θ

1
K

K
∑
k=1

MCCk(θ).

(8)

This optimization process was applied consistently across all classifiers and resam-
pling strategies. The complete hyperparameter grids explored for predictive models and
sampling methods are reported in Tables 5 and 6, respectively.

Although exhaustive grid search entails a higher computational cost compared to
heuristic or randomized alternatives, it ensures a systematic exploration of the predefined
parameter space and avoids biases associated with ad hoc hyperparameter selection. This
design choice supports a fair and methodologically controlled comparison across models
and configurations.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 19 -->

Mathematics 2026, 14, 429

19 of 44

Table 5. Hyperparameter grid used for model grid search strategy.

Model

KNN

Hyperparameter

Values

n_neighbors
weights
p

5, 7, 9, 11, 14, 18, 22, 25, 28, 35, 40, 45, 50, 70
“uniform”, “distance”
1, 2

n_estimators
max_depth
min_samples_split
min_samples_leaf
max_features

20, 50, 100, 200, 500, 800
None, 5, 10, 20, 50, 70
2, 10, 20, 50, 70, 100
1, 2, 4, 6, 10, 30
“sqrt”, “log2”

n_estimators
max_depth
learning_rate
num_leaves

20, 30, 50, 100, 500, 600, 800, 1000
None, 5, 10, 20, 50,70
0.01, 0.05, 0.1, 0.12, 0.15, 0.2
2, 4, 8, 15, 31, 50, 100

Random Forest

LightGBM

SVM

Logistic Regression

C
loss
penalty

C
solver

Naive Bayes

var_smoothing

0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10
“hinge”, “squared_hinge”
‘l1’, ‘l2’

0.01, 0.1, 1, 5, 10
“lbfgs”, “sag”, “saga”
1 × 10−9, 1 × 10−8, 1 × 10−7, 1 × 10−6,
1 × 10−4, 1 × 10−2

Decision Tree

max_depth
min_samples_split
min_samples_leaf
max_features

None, 5, 10, 20, 50, 70
2, 10, 20, 50, 70, 100
1, 2, 4, 6, 10, 30
“sqrt”, “log2”

Table 6. Hyperparameter grid used for Sampling grid search strategy.

Sampling Strategy

Hyperparameter

Values

OverSampling
UnderSampling

Ratio
Target Sample Values

0.6, 0.7, 0.8, 1
4000, 5000, 5500, 6000

4.7. Evaluation Metrics

Model performance was assessed using five complementary metrics derived from
the confusion matrix: Accuracy, Precision, Recall, F1-score, and Matthews Correlation
Coefficient (MCC). These metrics capture distinct aspects of classification behavior and are
particularly appropriate for binary classification problems under class imbalance.

Let TP, FP, TN, and FN denote the number of true positives, false positives, true
negatives, and false negatives, respectively. Accuracy measures the proportion of correctly
classified instances over the total number of observations:

Accuracy =

TP + TN
TP + TN + FP + FN

.

(9)

Although widely used, Accuracy may provide misleading assessments when class distribu-
tions are highly unbalanced.

Precision quantifies the proportion of positive predictions that are correctly classified,

and is defined as:

Precision =

TP
TP + FP

.

(10)

https://doi.org/10.3390/math14030429

---

<!-- PAGE 20 -->

Mathematics 2026, 14, 429

20 of 44

Recall measures the proportion of actual positive instances that are correctly identified:

Recall =

TP
TP + FN

.

(11)

Precision and Recall characterize complementary aspects of classification error, particularly
in scenarios where the costs of false positives and false negatives differ.

The F1-score corresponds to the harmonic mean of Precision and Recall, providing a

balanced summary of both measures:

F1 = 2 ·

Precision · Recall
Precision + Recall

.

(12)

Finally, the Matthews Correlation Coefficient (MCC) provides a comprehensive evalu-

ation by incorporating all four elements of the confusion matrix:

MCC =

TP · TN − FP · FN
(cid:112)(TP + FP)(TP + FN)(TN + FP)(TN + FN)

.

(13)

MCC ranges from −1 to 1, where values close to 1 indicate perfect classification, 0 cor-
responds to random prediction, and negative values indicate systematic disagreement
between predictions and true labels. This metric is particularly robust in imbalanced
classification settings, as it accounts for all four components of the confusion matrix and
provides a balanced evaluation even when class distributions are skewed [25].

All reported results correspond to performance on the held-out test set using the

hyperparameter configuration selected during cross-validation.

4.8. Feature Importance Analysis

To analyze the contribution of individual predictors, both model-specific and model-
agnostic feature importance techniques were employed. For classifiers providing intrinsic
interpretability, native importance measures were extracted, including impurity-based
importance for tree-based models and coefficient magnitudes for linear models.

Additionally, permutation feature importance was computed as a model-agnostic
approach [26]. This method quantifies the decrease in predictive performance induced
by randomly permuting a single feature, thereby breaking its association with the target
variable. Formally, the importance of feature fj is defined as:

ij = s −

1
R

R
∑
r=1

sr,j

(14)

where s denotes the original model score and sr,j represents the score obtained after the
r-th permutation of feature fj.

This analysis was conducted on validation data and enables consistent comparison of
feature relevance across heterogeneous model families, subject to known limitations in the
presence of highly correlated predictors.

4.9. Reproducibility

All experiments were conducted using fixed random seeds for data partitioning,
resampling, and model initialization. Software versions and experimental configurations
were explicitly controlled to ensure that results could be consistently replicated under
identical conditions. This design supports transparent verification of the reported findings
and facilitates methodological scrutiny in applied institutional settings.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 21 -->

Mathematics 2026, 14, 429

21 of 44

5. Results

This section presents the results obtained from the experiments described in the
previous sections. Section 5.1 summarizes the evaluation metrics achieved by each al-
gorithm introduced in Section 4.4, including both the baseline configurations and those
incorporating data-balancing techniques discussed in Section 4.5. In the best-performing
configurations reported in this section, the synthetic oversampling methods SMOTE and
ADASYN used a sample ratio of 0.7, while Random Undersampling reduced the majority
class to 5500 instances. Each configuration was also tested with and without hyperparame-
ter optimization, as described in Section 4.6, resulting in eight experimental combinations
per algorithm.

Section 5.2 complements this analysis by presenting the confusion matrices of the
best-performing experiment for each model, providing a detailed view of error distribution
and class-level performance.

Finally, Section 5.3 explores the factors that drive the models’ predictions, combining
global and local interpretability analyses. It integrates permutation importance and model-
wise feature analyses with visual inspections of Decision Tree structures at multiple depths
(Section 5.3.3) and SHAP value visualizations (Section 5.3.4). Together, these results provide
both aggregate and instance-level explanations, offering a comprehensive understanding
of how model decisions align with observable borrower behavior.

5.1. Model Performance

Tables 7–13 summarize the test-set performance of all algorithms under the eight
experimental configurations described earlier. As the primary selection criterion, MCC
differentiates the most competitive configurations under class imbalance, while Accuracy,
Precision, Recall, and the F1-score provide complementary views of classification behavior.
Unoptimized Decision Trees and Naive Bayes pipelines show weaker performance, whereas
their optimized variants improve substantially.

Table 7. K-Nearest Neighbors Results.

Pipeline

Accuracy

Precision

Recall

F1-Score

MCC

0.746
KNN
0.701
Smote KNN
0.701
Adasyn KNN
0.720
RUS KNN
0.765
OPT KNN
OPT Smote KNN
0.746
OPT Adasyn KNN 0.740
0.763
OPT RUS KNN

0.795
0.814
0.817
0.805
0.785
0.814
0.823
0.804

0.872
0.758
0.753
0.807
0.928
0.839
0.814
0.887

0.832
0.785
0.784
0.806
0.850
0.826
0.819
0.843

0.323
0.298
0.303
0.304
0.344
0.354
0.361
0.366

Precision, recall, and the F1-score followed a consistent trend across models, generally
remaining above 0.80, while MCC exhibited greater sensitivity to model and sampling
choices. Slight deviations were observed in a few configurations, such as the KNN with
ADASYN, where precision reached 0.785, and the unoptimized Naive Bayes, where recall
dropped to 0.449 and F1-scores remained below 0.70. Once optimized, however, all Naive
Bayes variants improved notably, reaching F1-scores of approximately 0.80. This pattern
indicates that even simple models benefit from parameter adjustment when trained on
administrative data with moderate class imbalance.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 22 -->

Mathematics 2026, 14, 429

22 of 44

Table 8. Gaussian Naive Bayes Results.

Pipeline

Accuracy Precision Recall

F1-Score MCC

Naive Bayes
Smote Naive Bayes
Adasyn Naive Bayes
RUS Naive Bayes
OPT Naive Bayes
OPT Smote Naive Bayes
OPT Adasyn Naive Bayes
OPT RUS Naive Bayes

0.615
0.569
0.562
0.599
0.715
0.754
0.735
0.725

0.874
0.892
0.888
0.875
0.847
0.810
0.827
0.835

0.543
0.458
0.449
0.518
0.738
0.860
0.800
0.770

0.670
0.605
0.596
0.651
0.789
0.835
0.813
0.801

0.309
0.293
0.282
0.296
0.366
0.361
0.360
0.360

Table 9. Logistic Regression Results.

Pipeline

Accuracy Precision Recall

F1-Score MCC

Logistic Regression
Smote Logistic Regression
Adasyn Logistic Regression
RUS Logistic Regression
OPT Logistic Regression
OPT Smote Logistic Regression
OPT Adasyn Logistic Regression
OPT RUS Logistic Regression

0.770
0.729
0.729
0.753
0.770
0.752
0.738
0.756

0.792
0.847
0.850
0.821
0.792
0.822
0.840
0.820

0.923
0.760
0.757
0.841
0.922
0.837
0.785
0.846

0.853
0.802
0.801
0.831
0.852
0.830
0.812
0.833

0.366
0.383
0.387
0.376
0.364
0.377
0.384
0.379

Table 10. Linear Support Vector Machine Results.

Pipeline

Accuracy

Precision Recall

F1-Score MCC

0.775
Linear SVM
0.727
Smote Linear SVM
0.729
Adasyn Linear SVM
0.754
RUS Linear SVM
OPT Linear SVM
0.776
OPT Smote Linear SVM 0.729
OPT Adasyn Linear SVM 0.750
0.726
OPT RUS Linear SVM

0.788
0.847
0.851
0.818
0.789
0.840
0.828
0.846

0.939
0.758
0.756
0.846
0.940
0.770
0.824
0.758

0.857
0.800
0.801
0.832
0.858
0.804
0.826
0.800

0.374
0.380
0.388
0.373
0.376
0.373
0.382
0.377

Table 11. Decision Tree Results.

Pipeline

Accuracy

Precision Recall

F1-Score MCC

DecisionTree
Smote DecisionTree
Adasyn DecisionTree
RUS DecisionTree
OPT DecisionTree
OPT Smote DecisionTree
OPT Adasyn DecisionTree
OPT RUS DecisionTree

0.716
0.702
0.695
0.688
0.764
0.704
0.735
0.742

0.804
0.818
0.811
0.808
0.791
0.868
0.841
0.844

0.801
0.755
0.751
0.743
0.913
0.696
0.780
0.787

0.802
0.785
0.780
0.774
0.848
0.772
0.809
0.814

0.297
0.306
0.286
0.273
0.351
0.384
0.381
0.394

The Matthews Correlation Coefficient (MCC) displayed higher variability across exper-
iments, as expected under class imbalance, ranging from approximately 0.28 to 0.42. Models
such as Naive Bayes and Decision Tree showed the greatest sensitivity to hyperparame-
ter tuning, while the Random Forest and LightGBM achieved consistent improvements
after optimization. In particular, LightGBM achieved the highest MCC values across all
experiments (up to 0.419), suggesting that boosting methods capture nonlinear interactions
among financial and academic features more effectively than other algorithms.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 23 -->

Mathematics 2026, 14, 429

23 of 44

Table 12. Random Forest Results.

Pipeline

Accuracy Precision Recall

F1-Score MCC

Random Forest
Smote Random Forest
Adasyn Random Forest
RUS Random Forest
OPT Random Forest
OPT Smote Random Forest
OPT Adasyn Random Forest
OPT RUS Random Forest

0.741
0.733
0.733
0.720
0.786
0.770
0.762
0.752

0.808
0.818
0.821
0.816
0.802
0.828
0.834
0.844

0.840
0.808
0.804
0.788
0.933
0.859
0.835
0.805

0.824
0.813
0.813
0.802
0.863
0.843
0.835
0.824

0.337
0.343
0.348
0.323
0.416
0.412
0.407
0.408

Table 13. Light Gradient Boosting Machine Results.

Pipeline

Accuracy

Precision Recall

F1-Score MCC

0.786
LightGBM
0.760
Smote LightGBM
0.765
Adasyn LightGBM
0.765
RUS LightGBM
OPT LightGBM
0.786
OPT Smote LightGBM 0.756
OPT Adasyn LightGBM 0.758
0.750
OPT RUS LightGBM

0.807
0.825
0.832
0.825
0.803
0.836
0.836
0.838

0.922
0.845
0.843
0.855
0.931
0.823
0.826
0.809

0.861
0.835
0.838
0.840
0.862
0.829
0.831
0.823

0.418
0.392
0.409
0.400
0.415
0.403
0.405
0.397

Overall, the results indicate that both linear and ensemble classifiers achieve reliable
generalization on the held-out test set using exclusively pre-declaration features. Linear
models (Logistic Regression and Linear SVM) yield stable performance with transparent
decision functions, while ensemble methods (Random Forest and LightGBM) provide a
modest gain in predictive power, as reflected by their higher MCC values. From an error-
analysis standpoint, the joint inspection of Precision, Recall, and MCC shows that competitive
configurations maintain a favorable trade-off between false positives and false negatives
under class imbalance, without collapsing into degenerate majority-class predictions.

From an operational perspective, differences in Matthews Correlation Coefficient
(MCC) translate into meaningful trade-offs between Type I and Type II errors, which are
directly relevant for institutional decision-making. In the present context, Type I errors (false
positives) correspond to borrowers incorrectly classified as compliant, potentially delaying
preventive outreach, whereas Type II errors (false negatives) correspond to borrowers
incorrectly classified as non-compliant, potentially triggering unnecessary monitoring
actions. Because MCC jointly accounts for all cells of the confusion matrix, improvements
in MCC reflect a more balanced reduction of both error types, rather than gains driven by
majority-class dominance or asymmetric error minimization.

Consequently, configurations achieving higher MCC values—such as optimized Ran-
dom Forest and LightGBM models—offer more robust discrimination capacity under
uncertainty, supporting earlier and more proportionate administrative responses. Impor-
tantly, these gains should not be interpreted as deterministic decision thresholds, but as
improvements in risk ranking quality that enhance the efficiency of targeted communication
and follow-up strategies while preserving institutional discretion.

These findings address RQ2 by showing that supervised models can predict declara-
tion outcomes with consistent performance using only pre-event information. They also
support RQ3 by demonstrating that interpretability can be preserved under constrained
administrative feature spaces: linear decision functions and tree-based structures pro-
vide explicit, verifiable decision criteria, while the cross-model stability of the top-ranked
predictors motivates the interpretability analyses developed in the subsequent subsections.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 24 -->

Mathematics 2026, 14, 429

24 of 44

Regarding computational cost, the full experimental training pipeline was executed on
a standard commercial off-the-shelf workstation (as described in Section 4.1) and required
approximately three days to complete, including hyperparameter optimization and cross-
validation across all evaluated configurations. Once trained, inference is computationally
lightweight: the average prediction time is approximately 0.002 seconds per instance on
the held-out test set.

Given that the institutional dataset comprises on the order of 103 records per year,
batch inference over new cohorts can be performed in negligible time on conventional
hardware, without imposing any operational burden. From an institutional deployment
perspective, this clear separation between moderate offline training cost and negligible
online inference cost makes the proposed framework fully feasible for routine use in
administrative settings.

5.2. Confusion Matrices

Figures 10 and 11 display the confusion matrices corresponding to the best-performing
experiment for each model. These visualizations provide a more granular view of how each
classifier distinguishes between borrowers who submitted their first income declaration
and those who did not.

(a) Optimized HP KNN with RUS

(b) Optimized HP Naive Bayes

(c) Logistic Regression with ADASYN

(d) Linear SVM with ADASYN

Figure 10. Confusion Matrices (Part I).

Overall, all models exhibit a strong ability to differentiate between the two classes,
though the nature of the misclassifications varies. Some models show a tendency toward
Type I errors (false positives—predicting a borrower will declare when they will not), while
others lean toward Type II errors (false negatives—predicting a borrower will not declare
when they actually do).

https://doi.org/10.3390/math14030429

---

<!-- PAGE 25 -->

Mathematics 2026, 14, 429

25 of 44

(a) Optimized HP DT with RUS

(b) Optimized HP Random Forest

(c) Base Light Gradient Boosting Machine

Figure 11. Confusion Matrices (Part II).

The confusion matrices for Naive Bayes, Logistic Regression, Linear SVM, and De-
cision Tree reveal a predominance of Type II errors, consistent with their lower recall
values reported in Section 5.1. These models tend to miss a portion of actual declarants,
prioritizing conservative classifications that favor the majority class.

In contrast, KNN, Random Forest, and LightGBM display a stronger inclination toward
Type I errors, predicting more declarants than those who actually filed. Although this
behavior slightly reduces precision, it prevents severe drops in recall and yields higher
overall F1-scores. In practical terms, this trade-off is favorable for early-warning systems,
as it minimizes the risk of failing to identify potential defaulting borrowers.

From an error-analysis perspective, the observed asymmetry between Type I and
Type II errors has direct implications for model selection under uncertainty. Configurations
exhibiting a mild bias toward Type I errors prioritize higher recall at the cost of a moderate
increase in false positives, whereas models dominated by Type II errors achieve higher
precision but risk systematically missing true positive cases. This trade-off is consistent
with the metric profiles reported in Section 5.1, particularly the joint behavior of Recall,
F1-score, and MCC.

Under a constrained feature setting and class imbalance, ensemble models such as
Random Forest and LightGBM exhibit a more balanced error structure, avoiding extreme
concentration on either error type. Their confusion matrices show that gains in recall

https://doi.org/10.3390/math14030429

---

<!-- PAGE 26 -->

Mathematics 2026, 14, 429

26 of 44

are not achieved at the expense of severe precision degradation, which explains their
consistently higher MCC values. From a computational standpoint, this balance indicates a
more robust discrimination capacity across both classes, rather than reliance on majority-
class dominance.

5.3. Model Interpretability

This section analyzes which variables most strongly drive the predictive behavior
of the models and how these relationships can be interpreted to provide transparent and
verifiable explanations of model predictions. Beyond supporting transparency, this inter-
pretability layer also plays a key role in identifying and monitoring potential socioeconomic
biases present in the underlying administrative data. By making feature contributions,
split thresholds, and decision rules explicit, the proposed approach allows institutional
analysts to detect patterns that may disproportionately affect specific groups, enabling
informed oversight and periodic review. Importantly, interpretability is not presented as
a bias-mitigation mechanism per se, but as a diagnostic tool to support responsible use,
human judgment, and the design of complementary governance or corrective strategies
when needed.

Section 5.3.1 reports the average permutation feature importance (PFI) across all
trained models, providing a global view of variable relevance. Section 5.3.2 presents the top
fifteen model-wise importances for the best-performing experiment of each interpretable
model, highlighting differences between linear and tree-based algorithms.

To complement these aggregate analyses, Section 5.3.3 illustrates decision paths ex-
tracted from the optimized Decision Tree (OPT RUS DecisionTree) at multiple depths, show-
ing how model structure can be translated into human-readable rules. Finally, Section 5.3.4
introduces SHAP value visualizations, which quantify the individual contribution of each
feature to specific predictions, enhancing transparency and case-level explainability.

5.3.1. Permutation Feature Importance Results

Figure 12 shows the averaged PFI computed for every model. To reduce the effect of
random shuffling, the procedure was repeated thirty-one times per model and the results
were averaged.

Two features stand out clearly: deud_monto (total loan amount) and conteo_matr
(total number of enrollments). They are followed by estado_civil (marital status) and
anio_exigibilidad (year of enforceability). The consistent prominence of these four variables
across models indicates that financial exposure, academic trajectory, and basic demograph-
ics jointly explain most of the predictive signal.

The remaining variables contribute progressively less. Most faculty dummies have
limited impact, with the notable exception of the indicator corresponding to the FACULTY
OF LAW (see Table 14), which ranks among the top features and suggests program-specific
differences in declaration behavior.
This result indicates that representing academic
affiliation at the faculty level provides sufficient and stable information to capture program-
level trends, allowing newly introduced academic programs to be accommodated through
their faculty assignment without altering the model structure.

At the lower end of the chart, some features exhibit slightly negative average PFI
values. Given their very small magnitude and the known sensitivity of permutation to
sampling noise and collinearity, these values do not by themselves justify feature removal.
While a formal feature ablation study was not conducted, the permutation feature
importance analysis provides an indirect indication of model sensitivity to reduced feature
availability. Across all evaluated models, predictive performance is largely driven by a small
subset of highly influential features, whereas the permutation of remaining variables results

https://doi.org/10.3390/math14030429

---

<!-- PAGE 27 -->

Mathematics 2026, 14, 429

27 of 44

in negligible changes in performance. This suggests that the learned decision structure is
not critically dependent on a large number of marginal features. However, it should be
noted that permutation importance reflects sensitivity to information degradation rather
than actual feature removal; a systematic retraining-based ablation analysis is therefore left
as future work.

Figure 12. Average Permutation Feature Importance of all Models.

Table 14. Faculty Dummy Feature Values.

Dummy Feature

Real Value

0
1
2
3
4
5
6
7
8

Ecclesiastical Faculty of Theology
Faculty of Sciences
Faculty of Philosophy and Education
Faculty of Economic and Administrative Sciences
Faculty of Engineering
Faculty of Marine and Geographical Sciences
Faculty of Agronomic and Food Sciences
Faculty of Law
Faculty of Architecture and Urbanism

5.3.2. Model-Wise Feature Importance

Figure 13 shows the feature importances for the best experiments of the linear models,

while Figure 14 reports the importances for the best tree-based models.

For the linear models, the coefficient-based importances in Figure 13 show that es-
tado_civil (marital status) dominates the decision boundaries in both Logistic Regression
and Linear SVMs, reflecting its strong marginal effect under the standardized feature space.
In the Logistic Regression model, academic and institutional variables such as facultad_7
(Faculty of Law), the STEM indicator, and several anio_ult_matr dummies are also influ-

https://doi.org/10.3390/math14030429

---

<!-- PAGE 28 -->

Mathematics 2026, 14, 429

28 of 44

ential, suggesting that the academic program and enrollment history contribute to the
likelihood of timely declaration. In contrast, the Linear SVM assigns higher relative weights
to recent enrollment years (anio_ult_matr_2011, 2015, and 2020) and to the total debt amount
(deud_monto), capturing the impact of both temporal and financial dimensions. These differ-
ences are expected, since permutation importance evaluates overall predictive dependence,
whereas linear coefficients reflect local marginal effects conditioned on feature scaling.

(a) Logistic Regression With ADASYN Feature Importance

(b) Linear SVM with ADASYN Feature Importance

Figure 13. Linear Models Feature Importance.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 29 -->

Mathematics 2026, 14, 429

29 of 44

(a) Optimized HP DT with Random Undersampling of Feature
Importance

(b) Optimized HP Random Forest Feature Importance

(c) Base Light Gradient Boosting Machine Feature Importance

Figure 14. Tree-Based Models for Feature Importance.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 30 -->

Mathematics 2026, 14, 429

30 of 44

For the tree-based models (Figure 14), the feature importance rankings are broadly
consistent across the Decision Tree, Random Forest, and LightGBM. In all three cases, the same
dominant predictors identified by permutation importance define the core predictive structure.
The Decision Tree model assigns the greatest weight to conteo_matr, followed closely
by estado_civil and deud_monto, indicating that a single borrower’s academic trajectory
and financial exposure are key splitting criteria. Random Forest and LightGBM rein-
force this pattern but invert the top two variables—deud_monto slightly surpasses con-
teo_matr—highlighting that ensemble averaging emphasizes financial magnitude over
enrollment frequency. The consistent presence of anio_exigibilidad among the top features
across all three models underscores the importance of the repayment timeline in distin-
guishing between declaring and non-declaring borrowers.

Lower-ranked variables, such as facultad indicators and STEM affiliation, contribute
marginally to model performance, offering limited incremental information once the main
financial and academic variables are included. This stability of rankings across indepen-
dent tree-based architectures suggests that the predictive signal is dominated by a small,
interpretable subset of features directly linked to borrower behavior and loan structure.

From a predictive and interpretability standpoint, these results align with the perfor-
mance analysis. Variables related to debt magnitude and academic trajectory consistently
carry the strongest explanatory weight across models, indicating that a small subset of
administrative features concentrates most of the discriminative signal. This concentra-
tion supports stable interpretation under uncertainty, as the same variables govern both
predictive accuracy and explanatory structure.

5.3.3. Decision Tree Snapshots at Different Depths

To illustrate how model structure supports decision-making, Figures 15–17 display
the same Decision Tree trained under one of the best-performing configurations, namely
the Optimized Random under-sampling Decision Tree (OPT RUS DecisionTree) described
in Section 5.1, and visualized at three different depths (d = 4, d = 5, and d = 11). These
visualizations are intended as illustrative artifacts rather than as objects of exhaustive node-
by-node inspection. The shallow representations (d = 4 and d = 5) highlight a small set of
high-yield splits that can be readily examined, whereas the deeper tree (d = 11) introduces
finer partitions that capture niche interactions at the cost of interpretability, exemplify-
ing how structural complexity rapidly limits direct human inspection in administrative
prediction settings.

From an institutional perspective, the decision tree structure enables the extraction
of explicit and auditable decision rules that can be interpreted as early-warning signals
rather than deterministic prescriptions. Split thresholds and branch conditions identify
combinations of administrative and academic attributes that are systematically associated
with elevated risk of non-submission. When used with appropriate caution, these rules
can inform high-level monitoring criteria or screening heuristics to prioritize outreach,
communication, or follow-up actions while avoiding automated enforcement or exclusion.
Importantly, these rule-based patterns are intended to support human oversight and
contextual judgment, not to replace institutional decision-making processes.

At d = 4, the tree typically places estado_civil, anio_exigibilidad and facultad_4 among
the first splits, followed by conteo_matr and deud_monto. These nodes yield compact rules
with broad coverage. For example, a Single debtor, a low loan amount, combined with low
enrollments, may increase the probability of not submitting the first income declaration.
Such rules are easy to operationalize as “portfolio filters” for early outreach.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 31 -->

Mathematics 2026, 14, 429

31 of 44

Figure 15. Decision Tree Snapshot of Model OPTRUSDecisionTree at Depth = 4. Blue (orange)
nodes indicate higher association with declaration (non-declaration), with color intensity reflecting
node purity.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 32 -->

Mathematics 2026, 14, 429

32 of 44

Figure 16. Decision Tree Snapshot of Model OPTRUSDecisionTree at Depth = 5. Blue (orange) nodes
indicate higher association with declaration (non-declaration), with color intensity reflecting node
purity; boxes (“...”) denote truncated branches beyond the selected tree depth.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 33 -->

Mathematics 2026, 14, 429

33 of 44

Figure 17. Decision Tree Snapshot of Model OPTRUSDecisionTree at Depth = 11. Blue (orange) nodes
indicate higher association with declaration (non-declaration), with color intensity reflecting node
purity. boxes (“...”) denote truncated branches beyond the selected tree depth.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 34 -->

Mathematics 2026, 14, 429

34 of 44

At d = 5, the model refines these segments, introducing thresholds that separate
borderline cases (for instance, specific ranges in deud_monto, faculties (facultad_X), or
if the undergraduate program is a STEM program (stem)). This level balances fidelity
and interpretability.

At increasing depths, the Decision Tree exposes progressively finer-grained interac-
tions among features. While deeper representations (d = 11) may improve local fit by
capturing higher-order combinations, they also reduce transparency and increase sensitiv-
ity to sampling variability. In contrast, shallower trees (d = 4 and d = 5) emphasize a small
set of high-yield splits that yield compact and stable decision rules. From an interpretability
standpoint, these shallow structures provide a favorable balance between expressive power
and human verifiability, making them suitable for analytical inspection and rule-based
reasoning under uncertainty.

These structural observations are consistent with the global and model-wise impor-
tance analyses: the first-level splits systematically involve the same dominant variables
(estado_civil, deud_monto, conteo_matr, and anio_exigibilidad) identified by permutation im-
portance and ensemble-based rankings. This alignment indicates that the learned decision
paths are not artifacts of model depth, but rather reflect stable predictive signals present
in the restricted administrative feature space. Consequently, the extracted rules provide
explicit, auditable explanations of individual predictions, reinforcing the interpretability
claims examined in relation to RQ3.

To illustrate the internal reasoning of the chosen model, Table 15 summarizes one
representative decision path extracted from the tree with depth d = 4. This path shows
how a borrower’s characteristics sequentially lead the model to predict a higher probability
of not submitting the first income declaration.

Table 15. Example decision path from the optimized Decision Tree (depth = 4).

Observed Value Split Condition

Feature Meaning

Branch Taken

1

2019

−0.5

−0.4

2019

estado_civil ≤ 1.5

anio_exigibilidad ≤ 2018.5

conteo_matr ≤ −0.696

deud_monto ≤ −0.478

anio_exigibilidad ≤ 2020.5

Borrower is single or without
dependents
Loan enforceability year (2019)
Total number of enrollments
(standardized)
Total debt amount
(standardized)
Loan enforceability year (2021)

True (left branch)

False (right branch)

True (left branch)

True (left branch)

End branch

Predicted class: Never Declared (estimated probability ≈ 0.85, 282 cases of no declaration over 333 total in this node)

This path illustrates a borrower whose marital status corresponds to a single individual
(estado_civil = 1), with a loan enforceable in 2019 and below-average academic enrollments
(conteo_matr standardized value = −0.5). The model first follows the left branch for single
borrowers, then the right branch for recent enforceability years, and subsequently the left
branches for both low enrollment count and below-average debt (deud_monto = −0.4).

The resulting classification, Never Declared, arises from the combination of limited
academic continuity (fewer than average enrollments) and less-than-average financial
exposure (a total amount of debt below the average). The probability related to the outcome
of the model, in this case 85% corresponds to the class proportion at the terminal node
reached by this path. This value corresponds to the empirical class frequency observed at
the leaf node and does not represent a calibrated posterior probability.

This example shows how the decision tree structure enables a transparent, rule-based
explanation of predictions: each split represents a human-interpretable condition that

https://doi.org/10.3390/math14030429

---

<!-- PAGE 35 -->

Mathematics 2026, 14, 429

35 of 44

links administrative attributes to behavioral outcomes. Such explicit reasoning enables
predictions to be traced, verified, and analytically justified through a sequence of human-
interpretable conditions defined on observed features.

5.3.4. Shap Values for Light Gradient Boosting Machine

Figure 18 shows the SHAP value distribution for all features in the Base Light Gradient
Boosting Machine (LGBM) model. The TreeExplainer method from the SHAP library was
applied, as it provides accurate local attributions for ensemble-based algorithms. Each point
represents a single observation: its position along the x-axis indicates the magnitude and
direction of its contribution to the model output, while the color encodes the original feature
value (blue for low and red for high). Points distributed farther from zero correspond to
stronger impacts on the final prediction.

Figure 18. SHAP Values for LGBM.

The SHAP summary plot reveals patterns consistent with the permutation and tree-
based feature importance analyses (Figures 12 and 14). The dominant variables—deud_monto
(loan amount), conteo_matr (number of enrollments), estado_civil (marital status), and
anio_exigibilidad (loan enforceability year)—exhibit the largest SHAP magnitudes. These
features drive the model’s predictions in interpretable directions: high deud_monto, high
conteo_matr, and higher estado_civil codes (married borrowers) tend to push predictions
toward the Declares class, while older anio_exigibilidad values (earlier repayment years) shift
the prediction toward Never Declared.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 36 -->

Mathematics 2026, 14, 429

36 of 44

Features related to academic programs (faculty dummies and the STEM indicator)
show minimal dispersion around zero, confirming their marginal influence on model
decisions. Notably, the dummy variable corresponding to the Faculty of Law (facultad_7)
displays a slightly asymmetric distribution, suggesting a weak but consistent positive
contribution to declaration probability.

These patterns indicate that marital status exerts a moderate but consistent influence
on declaration behavior, with married or partnered borrowers showing slightly higher
compliance. Financial exposure also plays a central role: larger loan amounts are associ-
ated with higher declaration probability, whereas smaller debts correspond to increased
non-declaration risk. Academic continuity further contributes to the model output, as a
lower number of enrollments (conteo_matr) is systematically linked to reduced declara-
tion likelihood. Temporal effects are present but weaker, with earlier enforceability years
(anio_exigibilidad) marginally increasing the probability of declaration. Finally, program-
related variables such as faculty affiliation exhibit only secondary effects, with the Faculty
of Law showing a small but consistent positive contribution relative to other faculties.

Overall, the SHAP analysis complements the global and model-wise interpretability
results by providing instance-level attributions that are consistent with the previously
identified feature rankings. The agreement between permutation importance, tree-based
importances, and SHAP value distributions indicates that the contribution of the dominant
predictors is stable across explanation paradigms and model families.

From a formal interpretability perspective, SHAP values offer a locally additive de-
composition of the model output, enabling each prediction to be expressed as a sum
of feature-level contributions relative to a baseline expectation. This property ensures
traceability and internal coherence of explanations, even in ensemble-based models with
complex nonlinear decision functions. Under the restriction to pre-declaration adminis-
trative features, such locally consistent explanations allow predictions to be examined,
compared, and validated without reliance on latent or post-event information.

Taken together, the stability of feature rankings, the availability of explicit decision
rules in tree-based models, and the locally faithful explanations provided by SHAP jointly
address RQ3. They demonstrate that reliable interpretability can be achieved in supervised
classification tasks operating on constrained institutional datasets, supporting transparent
reasoning about predictions under uncertainty rather than opaque score-based classification.

5.3.5. Consistency and Complementarity Across Interpretation Layers

The interpretability framework adopted in this study integrates global (permutation
feature importance), structural (decision paths), and local (SHAP) explanation methods,
each addressing a distinct aspect of model behavior. These approaches are not expected to
yield identical explanations, as they operate at different analytical levels and respond to
different interpretative questions.

Global explanations identify variables that exert consistent influence across the bor-
rower population, structural explanations reveal how such variables are combined within
the internal decision logic of the models, and local explanations provide instance-level
attributions for individual predictions. Apparent discrepancies between explanation layers
are therefore not treated as methodological inconsistencies, but rather as complementary
perspectives that jointly characterize predictive behavior.

From an institutional perspective, this layered interpretability strategy supports
decision-making at multiple levels. Global explanations inform strategic prioritization
and policy-level resource allocation, structural explanations enhance transparency and
auditability of decision rules, and local explanations enable case-by-case review when
targeted monitoring or preventive actions are considered. Rather than resolving disagree-

https://doi.org/10.3390/math14030429

---

<!-- PAGE 37 -->

Mathematics 2026, 14, 429

37 of 44

ments by privileging a single interpretability method, the proposed framework emphasizes
triangulation across explanation layers to ensure robust, interpretable, and context-aware
decision support.

5.4. Rule-Based Threshold Baseline Comparison

To contextualize the performance gains achieved by the machine learning models, a
simple rule-based baseline was implemented using threshold rules on debt amount and
enrollment count, which were consistently identified as the most influential numerical
features across the interpretability analyses (Sections 5.3.2–5.3.4). High-risk cases were
defined as those exceeding the fourth quartile of each respective distribution.

As reported in Table 16, this baseline exhibits high precision but very low recall,
resulting in poor overall performance, as reflected by low F1-score and MCC values.
This behavior indicates that the rule-based approach captures only a small subset of
extreme-risk borrowers while failing to identify a large proportion of non-compliant cases.
The corresponding confusion matrix (Figure 19) confirms this pattern, showing a limited
number of true positives alongside a substantial number of false negatives.

In contrast, the Light Gradient Boosting Machine achieves substantially higher and
more balanced performance (e.g., F1 = 0.861 and MCC = 0.418; see Table 13), demonstrating
its ability to exploit multivariate and non-linear relationships beyond simple threshold
rules. These results highlight the limitations of practical rule-based heuristics and un-
derscore the added value of machine learning models for early risk identification in this
institutional context.

Table 16. Applied Practical Threshold Metrics.

Pipeline

Accuracy

Precision

Recall

F1-Score

Practical Threshold 0.385

0.876

0.172

0.288

MCC

0.141

Figure 19. Confusion matrix for the rule-based threshold baseline.

6. Discussion

The findings of this work is methodological and institutional rather than algorithmic.
The findings should be read as evidence about what can be achieved with established mod-
els when the problem is formulated under realistic administrative constraints, evaluated

https://doi.org/10.3390/math14030429

---

<!-- PAGE 38 -->

Mathematics 2026, 14, 429

38 of 44

with imbalance-appropriate metrics, and accompanied by interpretability mechanisms
designed for auditability. Accordingly, the manuscript does not claim new learning theory
or new imbalance-handling methods, but provides a defensible blueprint for deploying
predictive decision support in comparable administrative compliance settings.

Given the breadth of evaluated configurations, the interpretation in this section em-
phasizes cross-model patterns and relative performance tiers rather than isolated numerical
differences. While full metric tables are retained for transparency and completeness, the
discussion focuses on aggregated trends—such as the comparative behavior of linear versus
ensemble models, the effect of optimization and sampling strategies, and the stability of
MCC across configurations—where additional numerical detail does not yield proportional
interpretive value.

This aggregation strategy avoids overemphasis on marginal metric fluctuations and
aligns the analysis with the study’s applied objective: assessing whether administratively
deployable models achieve reliable, interpretable, and operationally meaningful perfor-
mance under realistic data constraints.

6.1. Model Performance and Interpretability

Although non-submission of the first income declaration may, in general, reflect het-
erogeneous behavioral conditions, the present study considers this outcome within the
specific institutional context of the FSCU system. The obligation to submit the declara-
tion is contractually established, becomes enforceable after a defined grace period, and
is supported by systematic informational and reminder mechanisms. Accordingly, first-
time non-submission is interpreted as an early manifestation of non-compliance within
a fully informed contractual framework, rather than as a consequence of lack of aware-
ness. While individual circumstances may differ, such distinctions cannot be reliably
inferred from pre-declaration administrative data alone. Consequently, the interpretability
analyses presented in this study should be understood as identifying correlates of ele-
vated early non-compliance risk, rather than as causal explanations of distinct underlying
behavioral mechanisms.

Across all experiments, most algorithms achieved strong and stable predictive per-
formance. Linear models, particularly Logistic Regression and the Linear Support Vector
Machine, consistently achieved F1-scores above 0.85 and Matthews Correlation Coeffi-
cients (MCC) near 0.37, indicating balanced performance between the two classes despite
a moderate imbalance in the dataset. Tree-based ensemble methods, such as Random
Forest and LightGBM, achieved slightly higher MCC values (around 0.41–0.42), suggest-
ing that non-linear relationships exist between borrower characteristics and repayment
behavior. However, the gap in performance between ensemble and linear models was
narrow, reflecting that the underlying patterns can be captured effectively without complex
architectures. This consistency across algorithms indicates that administrative data contain
a strong and stable signal that can be modeled reliably through interpretable approaches
under constrained feature spaces and that assessing classification quality through MCC,
which is particularly appropriate in imbalanced settings because it accounts for all cells
of the confusion matrix, supports more reliable identification and prioritization of bor-
rowers at elevated non-compliance risk. In operational terms, this can inform earlier and
more targeted outreach (e.g., reminders and guidance) and a more efficient allocation of
administrative follow-up resources, without treating the model output as a deterministic
decision rule.

The confusion matrix analysis confirmed these trends: linear models favored con-
servative classifications with higher precision but lower recall (Type II errors), whereas
ensemble methods offered more balanced results, slightly increasing false positives (Type I

https://doi.org/10.3390/math14030429

---

<!-- PAGE 39 -->

Mathematics 2026, 14, 429

39 of 44

errors) to improve recall for non-declarants. Hyperparameter tuning produced marginal
yet consistent improvements across all models, while Random Under Sampling often en-
hanced minority-class recall without substantial accuracy loss. Synthetic oversampling
methods (SMOTE and ADASYN) achieved similar effects, marginally improving precision
in some configurations.

Interpretability analyses further strengthened the robustness and transparency of
these results. Permutation feature importance and model-specific coefficients consistently
highlighted financial and academic variables—particularly total debt (deud_monto), en-
rollment count (conteo_matr), marital status (estado_civil), and loan enforceability year
(anio_exigibilidad)—as the main determinants of first-declaration behavior. The decision-tree
visualizations provided concrete rule-based explanations, showing how these variables
interact to form decision paths (e.g., combinations of high debt and limited enrollment pre-
dicting non-declaration). Complementarily, SHAP value analysis quantified each feature’s
contribution to individual predictions, confirming that higher debt levels and continuous
enrollment increase the probability of compliance, whereas more recent enforceability years
and single marital status lean toward non-declaration.

It should be noted that these interpretability techniques do not address identical ex-
planatory questions and may therefore yield partially divergent insights. Permutation
Feature Importance (PFI) captures global sensitivity by measuring performance degrada-
tion under feature perturbation, whereas SHAP values provide conditional, instance-level
attributions, and decision trees offer simplified structural approximations of learned re-
lationships. As a result, discrepancies between global rankings and local explanations
are expected and should be interpreted as complementary perspectives rather than as
methodological contradictions.

Together, these interpretability layers—global (PFI), structural (tree paths), and local
(SHAP)—provide a comprehensive understanding of model behavior. They ensure that
predictions can be traced, analytically justified, and examined across multiple levels of
abstraction, reinforcing the reliability of supervised learning models operating under
constrained administrative feature spaces.

At the same time, the interpretability of ensemble models should be understood as me-
diated rather than intrinsic. While post-hoc explanation tools enable analytical inspection of
model behavior, ensemble methods such as Random Forests and gradient boosting do not
yield transparent decision rules in a strict sense. Accordingly, the explanations presented
in this study should be viewed as audit-oriented approximations that support diagnostic
reasoning and institutional scrutiny, rather than as fully transparent representations of the
underlying decision logic.

At the current stage, no institution-specific decision threshold is defined for translating
predicted risk scores into automatic actions. This reflects the fact that, within the FSCU
system, formalized risk tolerance criteria and cost-sensitive decision policies have not
yet been established. Consequently, the proposed models are conceived as an initial
screening and monitoring tool, providing continuous risk indicators rather than binary
decision triggers. These outputs are intended to support early identification, targeted
communication, and preventive follow-up strategies, leaving final decisions to institutional
judgment. The definition of optimized thresholds aligned with explicit institutional risk
preferences is therefore identified as a natural extension of this work, once such policies are
formally specified.

From an operational standpoint, the interpretability framework is intended to support
institutional processes rather than individual-level adjudication. For example, a borrower
characterized by high outstanding debt, limited enrollment history, and a recent enforce-
ability year may be flagged as presenting elevated early non-compliance risk. In such cases,

https://doi.org/10.3390/math14030429

---

<!-- PAGE 40 -->

Mathematics 2026, 14, 429

40 of 44

interpretability outputs can guide targeted communication, administrative follow-up, or
preventive guidance, without being used as deterministic or punitive decision rules.

6.2. Implications for Predictive Modeling Under Administrative Constraints

This study illustrates how supervised learning models trained on routinely collected
administrative data can anticipate borrower declaration behavior under information con-
straints. From a modeling perspective, the results demonstrate that pre-event academic
and financial variables contain sufficient signal to support reliable binary classification,
even in the presence of moderate class imbalance.

The combination of predictive performance and interpretability indicates that complex
behavioral outcomes can be approximated using transparent decision structures. Rule-
based paths extracted from decision trees and locally additive SHAP explanations allow
predictions to be decomposed into verifiable feature contributions, facilitating analytical
scrutiny rather than opaque score assignment.

More broadly, the proposed framework exemplifies how predictive modeling can
be integrated into administrative data environments without reliance on latent variables
or post-event information. This characteristic supports transferability to other income-
contingent loan systems or institutional datasets with similar structural limitations, where
explainability and traceability are as critical as predictive accuracy.

The generalizability of these findings should be interpreted with appropriate scope.
Several elements of the results are inherently context-specific, including the exact distri-
bution of declaration outcomes, the magnitude of predictive performance metrics, the
relative importance of individual features, and the absence of institutionally defined deci-
sion thresholds. These aspects reflect the regulatory framework, borrower population, and
administrative practices of the FSCU system at the PUCV, and should not be assumed to
transfer directly to other institutions or funding schemes.

In contrast, the methodological structure of the proposed framework is potentially
transferable across administrative compliance contexts. Specifically, the pre-event formula-
tion of the predictive task under informational constraints, the use of a unified and leakage-
aware validation protocol, the prioritization of imbalance-appropriate evaluation metrics
such as the Matthews Correlation Coefficient, and the positioning of interpretability mech-
anisms as audit-oriented decision support tools are applicable to other income-contingent
loan systems and regulated administrative domains where outcomes are delayed and class
imbalance is structural.

6.3. Limitations

Several limitations should be acknowledged. First, the study is constrained by the
scope and structure of the available administrative data, which, while comprehensive,
exclude certain socioeconomic variables that could further explain borrower behavior (e.g.,
employment type or household composition). Second, the analysis focuses exclusively on
first-declaration outcomes; subsequent declarations and long-term repayment behavior
remain outside the scope of the present study. Extending the framework to a longitudi-
nal setting would allow the identification of recurrent non-compliance patterns and the
assessment of persistence in compliance behavior over time.

Another limitation concerns generalizability. The data and administrative context
correspond to a single higher education institution. Although the proposed modeling
framework is transferable, predictive performance and feature relevance may vary across
universities with different borrower profiles, regulatory environments, or collection prac-
tices. Future research should validate the approach using multi-institutional data, particu-

https://doi.org/10.3390/math14030429

---

<!-- PAGE 41 -->

Mathematics 2026, 14, 429

41 of 44

larly within the CRUCH network, to assess external validity and support the development
of standardized predictive tools for income-contingent student loan management in Chile.
Finally, although models are trained on data pooled across multiple cohorts and
enforceability periods, the present study adopts a cross-sectional predictive perspective
rather than a time-aware longitudinal one. Potential temporal drift arising from regula-
tory changes, labour-market conditions, or evolving institutional practices is therefore
acknowledged but not explicitly modelled. This limitation also constrains the feasibility
of time-aware validation strategies, as implementing cohort-based training and testing
would require a longer and more stable post-reform observation window to avoid con-
flating gradual temporal drift with structural breaks induced by legislative changes and
exogenous shocks. Assessing robustness across cohorts under such conditions is identified
as an important direction for future research.

7. Conclusions and Future Work
7.1. Summary of Main Findings

This study developed a predictive framework for estimating whether borrowers of
the Fondo Solidario de Crédito Universitario (FSCU) at the Pontificia Universidad Católica de
Valparaíso (PUCV) would submit their first income declaration using only pre-declaration
administrative and academic data. By combining standard machine learning algorithms with
rigorous preprocessing, the models achieved strong and consistent predictive performance.
Linear classifiers—Logistic Regression and a Support Vector Machine—demonstrated
high interpretability and stability, while ensemble models such as the Random Forest and
LightGBM offered slightly higher predictive accuracy, reaching F1-scores above 0.85 and
Matthews Correlation Coefficients around 0.41. Interpretability analyses, including permu-
tation importance, decision-tree visualization, and SHAP values, consistently identified fi-
nancial and academic features—particularly total debt (deud_monto), number of enrollments
(conteo_matr), marital status (estado_civil), and loan enforceability year (anio_exigibilidad)—as
the most influential determinants of declaration behavior. Together, these results validate
the feasibility of leveraging administrative data for anticipating declaration behavior and
demonstrate that transparent, interpretable models can achieve reliable performance within
income-contingent loan settings.

7.2. Methodological Implications

From a methodological perspective, the study highlights the importance of combining
predictive performance with interpretability when modeling compliance-related outcomes
using administrative data. The results show that relatively simple classifiers, when properly
tuned and evaluated, can achieve competitive performance while preserving transparency
and analytical tractability.

The integration of interpretable structures—such as explicit decision paths and ad-
ditive explanation models—demonstrates that complex ensemble methods can remain
accessible to inspection and validation. This balance between accuracy and explainability
is particularly relevant for modeling tasks involving regulated or high-stakes outcomes,
where understanding the contribution of individual features is as important as predictive
accuracy itself.

7.3. Directions for Future Research

While the results are encouraging, several research opportunities remain open. Fu-
ture work should extend the predictive framework to longitudinal analysis, examining
how borrower behavior evolves across successive income declarations and repayment
cycles. Incorporating additional socioeconomic variables—such as employment stability,

https://doi.org/10.3390/math14030429

---

<!-- PAGE 42 -->

Mathematics 2026, 14, 429

42 of 44

regional context, or household composition—could further enhance predictive performance
and interpretability.

From a machine learning point of view, a natural extension is the incorporation of
cost-sensitive or constrained learning strategies. In this domain, their meaningful adoption
requires an explicit institutional definition of misclassification costs, since the operational
consequences of false positives and false negatives are administrative-policy-dependent.
Future work should formalize these cost structures and evaluate cost-sensitive learning
under the same pre-event constraints.

Methodologically, integrating advanced explainable AI techniques (e.g., SHAP interac-
tion values, LIME, or counterfactual explanations) would allow for a deeper understanding
of feature contributions at both the individual and subgroup levels. Expanding the dataset
to include multiple universities or linking it with national administrative records could
test the model’s generalizability and scalability. Ultimately, these extensions would con-
tribute to the development of adaptive and transparent predictive frameworks suitable for
complex, regulated administrative datasets in Chile and comparable contexts worldwide.
An additional avenue for future research is to examine the extent to which the pro-
posed framework generalizes across administrative contexts with different structural char-
acteristics. In particular, controlled sensitivity analyses under alternative class imbalance
ratios or simulated administrative conditions would allow for a systematic assessment
of robustness beyond the specific distributional properties of the FSCU system. Such
extensions would help clarify which performance and interpretability patterns are stable
across institutions and which are contingent on local regulatory or population features,
while preserving the pre-event and audit-oriented design principles adopted in this study.
Overall, the results confirm the achievement of this study’s objectives: the predictive
models identify the key factors associated with first-declaration behavior while maintaining
reliable performance and interpretability under administrative constraints. This work
contributes a replicable modeling framework that bridges supervised learning, explainable
AI, and real-world administrative data, reinforcing the role of transparent predictive
methods in applied computational research.

Author Contributions: Conceptualization, Á.P., B.C., E.M., E.R.-T., J.B.-G., F.C.-C., B.L.C., A.Y. and
Á.P.F.; methodology, Á.P., B.C., E.M., E.R.-T. and R.S.; software, Á.P., J.B.-G., F.C.-C., B.L.C. and Y.L.;
validation, Á.P., B.C., E.M., E.R.-T., J.B.-G., F.C.-C., B.L.C., Y.L., A.Y., Á.P.F. and R.S.; formal analysis,
Á.P., J.B.-G., F.C.-C., B.L.C., Y.L. and A.Y.; investigation, Á.P., J.B.-G., F.C.-C., B.L.C. and Y.L.; resources,
B.C. and Á.P.F.; data curation, Á.P., J.B.-G., F.C.-C., B.L.C. and Y.L.; writing—original draft, Á.P.,
J.B.-G., F.C.-C., B.L.C. and Y.L.; writing—review & editing, Á.P., B.C., J.B.-G., F.C.-C., B.L.C., Y.L.,
Á.P.F. and R.S.; visualization, Á.P., J.B.-G., F.C.-C., B.L.C., Y.L. and A.Y.; supervision, B.C., E.M. and
R.S.; project administration, Á.P. and B.C. All authors have read and agreed to the published version
of the manuscript.

Funding: This research received no external funding.

Data Availability Statement: The raw data supporting the conclusions of this article will be made
available by the authors on request.

Acknowledgments: José Barrera-García is supported by the National Agency for Research and Devel-
opment (ANID)/Scholarship Program/DOCTORADO NACIONAL/2024-21242516. Felipe Cisternas-
Caneo is supported by the National Agency for Research and Development (ANID)/Scholarship
Program/DOCTORADO NACIONAL/2023-21230203.

Conflicts of Interest: The authors declare no conflicts of interest.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 43 -->

Mathematics 2026, 14, 429

References

43 of 44

1.

2.

Romero, C.; Ventura, S. Educational data mining: A review of the state of the art. IEEE Trans. Syst. Man Cybern. Part C (Appl.
Rev.) 2010, 40, 601–618. [CrossRef]
Paz, Á.; Crawford, B.; Monfroy, E.; Barrera-García, J.; Peña Fritz, Á.; Soto, R.; Cisternas-Caneo, F.; Yáñez, A. Machine Learning
and Metaheuristics Approach for Individual Credit Risk Assessment: A Systematic Literature Review. Biomimetics 2025, 10, 326.
[CrossRef] [PubMed]

3. He, H.; Garcia, E.A. Learning from imbalanced data. IEEE Trans. Knowl. Data Eng. 2009, 21, 1263–1284. [CrossRef]
4.
5.

Doshi-Velez, F.; Kim, B. Towards a rigorous science of interpretable machine learning. arXiv 2017, arXiv:1702.08608. [CrossRef]
Consejo de Rectoras y Rectores de las Universidades Chilenas. Universidades CRUCH a lo Largo de Chile. 2025. Available
online: https://consejoderectores.cl/el-consejo/universidades-cruch/ (accessed on 16 October 2025).
Biblioteca Nacional del Congreso de Chile. Ley Fondos Solidatiros de Crédito Universitario. 1994 Available online: https:
//www.bcn.cl/leychile/navegar?idNorma=30654 (accessed on 16 October 2025).
Biblioteca Nacional del Congreso de Chile. Modificación Ley Fondos Solidatiros de Crédito Universitario. 2012. Avail-
able online: https://www.bcn.cl/leychile/navegar?idNorma=1036996&idParte=9235355&idVersion=2012-02-04 (accessed on
16 October 2025).
Subsecretaría de Educación Superior, MINEDUC. Primer Informe Crédito con Aval del Estado: Características de la población
deudora e impactos, Julio 2022. Available online: https://educacionsuperior.mineduc.cl/wp-content/uploads/sites/49/2022/
07/PrimerInformeCAE-1.pdf (accessed on 30 December 2025).
Consejo de Rectoras y Rectores de las Universidades Chilenas (CRUCH). Deudores Morosos de Fondo Solidario de Crédito
Universitario (publicaciones anuales). 2025. Available online: https://consejoderectores.cl/en/fondo-solidario-de-credito-
universitario/ (accessed on 6 September 2025).
Superintendencia de Educación Superior. Norma de Carácter General N°3: Registros y contabilidad del FSCU. 2024. Available
online: https://www.sesuperior.cl/wp-content/uploads/2024/04/NCG-3-FSCU.pdf (accessed on 6 September 2025).

6.

7.

8.

9.

10.

11. Pontificia Universidad Católica de Valparaíso.

Fondo Solidario de Crédtio Universitario. 2025 Available online: https:

//estudiantespucv.cl/fscu/ (accessed on 16 October 2025).

12. Department for Education (UK). Student Loans in England: Financial Year 2024–25; Department for Education: London, UK,
2025. Available online: https://www.gov.uk/government/statistics/student-loans-in-england-2024-to-2025/student-loans-in-
england-financial-year-2024-25 (accessed on 6 September 2025).

13. Australian Taxation Office. Study and Training Loan Repayment Thresholds and Rates; Australian Taxation Office: Canberra, Australia,
2025. Available online: https://www.ato.gov.au/tax-rates-and-codes/study-and-training-support-loans-rates-and-repayment-
thresholds (accessed on 6 September 2025).
Salmi, J.; Hauptman, A.M. Innovations in Tertiary Education Financing: A Comparative Evaluation of Allocation Mechanisms.
World Bank. 2006. Available online: https://documents1.worldbank.org/curated/en/383241468138743150/pdf/383240WP0
Box0317363B01PUBLIC1.pdf (accessed on 6 September 2025).

14.

15. OECD. OECD Policy GPS—Student Support (Comparative Policy Notes); OECD: Paris, France, 2024. Available online: https:

//gpseducation.oecd.org/revieweducationpolicies/ (accessed on 6 September 2025).

16. Thuy, N.T.H.; Ha, N.T.V.; Trung, N.N.; Binh, V.T.T.; Hang, N.T.; Binh, V.T. Comparing the Effectiveness of Machine Learning and

17.

Deep Learning Models in Student Credit Scoring: A Case Study in Vietnam. Risks 2025, 13, 99. [CrossRef]
Suleiman, R.; Anane, R. Institutional data analysis and machine learning prediction of student performance. In Proceedings of
the 2022 IEEE 25th International Conference on Computer Supported Cooperative Work in Design (CSCWD), Hangzhou, China,
4–6 May 2022; IEEE: New York, NY, USA, 2022; pp. 1480–1485. [CrossRef]

18. Yakubu, M.N.; Abubakar, A.M. Applying machine learning approach to predict students’ performance in higher educational

institutions. Kybernetes 2022, 51, 916–934. [CrossRef]

19. Lessmann, S.; Baesens, B.; Seow, H.V.; Thomas, L.C. Benchmarking state-of-the-art classification algorithms for credit scoring: An

update of research. Eur. J. Oper. Res. 2015, 247, 124–136. [CrossRef]

20. Aulck, L.; Velagapudi, N.; Blumenstock, J.; West, J. Predicting student dropout in higher education. arXiv 2016, arXiv:1606.06364.

[CrossRef]

21. Hastie, T.; Tibshirani, R.; Friedman, J. The Elements of Statistical Learning, 2nd ed.; Springer Series in Statistics; Springer: New York,

NY, USA, 2009. [CrossRef]

22. Alam, T.M.; Shaukat, K.; Hameed, I.A.; Luo, S.; Sarwar, M.U.; Shabbir, S.; Li, J.; Khushi, M. An Investigation of Credit Card

Default Prediction in the Imbalanced Datasets. IEEE Access 2020, 8, 201173–201198. [CrossRef]

23. Madaan, M.; Kumar, A.; Keshri, C.; Jain, R.; Nagrath, P. Loan default prediction using decision trees and random forest: A

comparative study. IOP Conf. Ser. Mater. Sci. Eng. 2021, 1022, 012042. [CrossRef]

24. Lemaître, G.; Nogueira, F.; Aridas, C.K. Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in

Machine Learning. J. Mach. Learn. Res. 2017, 18, 1–5.

https://doi.org/10.3390/math14030429

---

<!-- PAGE 44 -->

Mathematics 2026, 14, 429

44 of 44

25. Chicco, D.; Jurman, G. The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary

classification evaluation. BMC Genom. 2020, 21, 6. [CrossRef] [PubMed]

26. Breiman, L. Random Forests. Mach. Learn. 2001, 45, 5–32. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

https://doi.org/10.3390/math14030429

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Article
Interpretable Binary Classification Under Constraints for
Financial Compliance Modeling
ÁlexPaz1,2 ,BroderickCrawford3,* ,EricMonfroy2 ,EduardoRodriguez-Tello4 ,JoséBarrera-García5,* ,
FelipeCisternas-Caneo3 ,BenjamínLópezCortés3 ,YoslandyLazo3 ,AndrésYáñez1,2 ,ÁlvaroPeñaFritz1
andRicardoSoto3
1 EscueladeIngenieríaenConstrucciónyTransporte,PontificiaUniversidadCatólicadeValparaíso,
AvenidaBrasil2147,Valparaíso2362804,Chile;alex.paz@pucv.cl(Á.P.);andres.yanez@pucv.cl(A.Y.);
alvaro.pena@ucv.cl(Á.P.F.)
2 Laboratoired’ÉtudeetdeRechercheenInformatiqued’Angers(LERIA),Universitéd’Angers,UFRSciences,2
BddeLavoisier,49000Angers,France;eric.monfroy@univ-angers.fr
3 EscueladeIngenieríaInformática,PontificiaUniversidadCatólicadeValparaíso,AvenidaBrasil2241,
Valparaíso2362807,Chile;felipe.cisternas.c@mail.pucv.cl(F.C.-C.);benjamin.lopez.c@mail.pucv.cl(B.L.C.);
yoslandy.lazo@pucv.cl(Y.L.);ricardo.soto@pucv.cl(R.S.)
4 CinvestavUnidadTamaulipas,Km.5.5CarreteraVictoria-SotoLaMarina,
Victoria87130,Tamaulipas,Mexico;ertello@cinvestav.mx
5 EscueladeNegociosyEconomía,PontificiaUniversidadCatólicadeValparaíso,Amunátegui1838,
ViñadelMar2580129,Chile
* Correspondence:broderick.crawford@pucv.cl(B.C.);jose.barrera@pucv.cl(J.B.-G.)
Abstract
Thisstudyaddressesaninterpretablesupervisedbinaryclassificationproblemundercon-
strained feature availability and class imbalance. The objective is to evaluate whether
reliablepredictiveperformancecanbeachievedusingexclusivelypre-eventadministrative
variables while preserving transparency and analytical traceability of model decisions.
Acomparativeframeworkisdevelopedusinglinearandensemble-basedclassifiers,com-
binedwithresamplingstrategiesandexhaustivehyperparameteroptimizationembedded
withincross-validation. Modelperformanceisevaluatedusingstandardclassificationmet-
rics,withparticularemphasisontheMatthewscorrelationcoefficientasarobustmeasure
underimbalance. Inadditiontopredictiveaccuracy,theanalysisincorporatesglobal,struc-
tural,andlocalinterpretabilitymechanisms,includingpermutationfeatureimportance,
explicitdecisionpathsderivedfromtree-basedmodels,andadditivelocalexplanations.
Experimentalresultsshowthatoptimizedensemblemodelsachieveconsistentperformance
gains over linear baselines while maintaining a balanced error structure across classes.
Importantly, the most influential predictors exhibit stable rankings across models and
explanationmethods,indicatingaconcentratedandrobustdiscriminativesignalwithin
the constrained feature space. The interpretability analysis demonstrates that complex
classifierscanbedecomposedintoverifiabledecisionrulesandlocallycoherentfeature
contributions. Overall,thefindingsconfirmthatinterpretablesupervisedclassificationcan
AcademicEditor:ZengjingChen bereliablyconductedunderadministrativedataconstraints,providingareproduciblemod-
Received:31December2025 elingframeworkthatbalancespredictiveperformance,erroranalysis,andexplainabilityin
Revised:18January2026 appliedmathematicalsettings.
Accepted:23January2026
Published:26January2026 Keywords: binary classification; supervised learning; class imbalance; error analysis;
Copyright:©2026bytheauthors. Matthewscorrelationcoefficient;modelinterpretability;highereducationfinance
LicenseeMDPI,Basel,Switzerland.
Thisarticleisanopenaccessarticle
MSC:62H30;62P20;68T37
distributedunderthetermsand
conditionsoftheCreativeCommons
Attribution(CCBY)license.
Mathematics2026,14,429 https://doi.org/10.3390/math14030429

Mathematics2026,14,429 2of44
1. Introduction
1.1. BackgroundandMotivation
Income-contingentstudentloansystemsrelyonannualborrowercompliancetoensure
bothequityandfinancialsustainability. Fromacomputationalperspective,monitoring
such compliance can be formulated as a prediction problem under uncertainty, where
decisions must be made using limited and heterogeneous information available prior
to critical administrative deadlines. In this context, supervised learning models offer a
systematic framework for estimating the likelihood of borrower compliance based on
historicalacademicandadministrativerecords[1,2].
In Chile, the University Credit Solidarity Fund (Fondo Solidario de Crédito Universi-
tario,FSCU)constitutesalarge-scaleincome-contingentloansystemadministeredatthe
institutionallevel. Theprogramgeneratesextensivestructureddatadescribingacademic
trajectories,loancharacteristics,andadministrativeevents,whichcanberepresentedas
high-dimensionalfeaturespacessuitableforpredictivemodeling. However,theeffective
useofthisinformationischallengedbyclassimbalance,delayedoutcomes,andtheneed
fortransparentdecisionrules[3,4].
AtthePontificiaUniversidadCatólicadeValparaíso(PUCV),asignificantproportion
ofundergraduatestudentsarebeneficiariesoftheFSCU,makingearlyidentificationof
non-compliancepatternsarecurringoperationalproblem. Whiledetailedadministrative
recordsareroutinelycollected,theirpotentialforpredictiveanalysishasnotbeenfully
exploited.Thismotivatestheapplicationofmachinelearningtechniquesthatcantransform
institutionaldataintoquantitativeriskestimates,enablinganticipatorydecision-making.
Beyond this specific case, the problem addressed in this study reflects a broader
classofdata-drivenclassificationtasksinwhichoutcomesdependonsocioeconomicand
behavioralvariablesobservedpriortoaneventofinterest. Assuch,itprovidesarelevant
settingforevaluatingsupervisedlearningmodelsunderrealisticconstraintsofimbalance,
interpretability,andlimitedobservability.
1.2. ProblemStatementintheContextofFSCU
TheUniversityCreditSolidarityFund(FondoSolidariodeCréditoUniversitario,FSCU)
isastate-backedstudentloansystemappliedatChileanuniversitiesaffiliatedwiththe
CouncilofRectors(CRUCH)[5]. Itsoperationaldesignestablishesarepaymentmechanism
thatreliesontheborrower’sannualincomedeclarationtodeterminewhetherthedebt
installmentisadjustedtoincomeorfixedunderstatutoryrules.
Fromamodelingperspective,thismechanisminducesabinaryobservableoutcome
attheborrowerlevel. Lety ∈ {0,1}denotethedeclarationstatusofborroweri,where
i
y = 1representsthetimelysubmissionoftheincomedeclarationandy = 0otherwise.
i i
TheoutcomeisgovernedbythelegalframeworkestablishedbyLawNo. 19,287[6]and
itsamendment inLaw No. 20,572[7], whichmandate annualdeclarations andimpose
asymmetricconsequencesforcompliantandnon-compliantborrowers.
Officialinstitutionalreportsdocumentpersistentlevelsofnon-declarationandrepay-
mentdifficultiesamongFSCUbeneficiaries,particularlyamongborrowerswithincomplete
academictrajectoriesorgreatersocioeconomicvulnerability[8,9]. Inaddition,thestructure,
availability,andaccountingtreatmentoftheadministrativerecordsusedformonitoring
andcollectionareformallydefinedbyregulatoryguidelinesissuedbytheSuperintendence
ofHigherEducation[10]. Theseelementsestablishtheempiricalandoperationalcontext
inwhichdeclarationoutcomesareobservedandrecorded.
Crucially, thedeclarationdecisionmustbemadeusingonlyinformationavailable
beforethedeclarationdeadline. LetX
∈Rn×pdenotethematrixofpre-declarationfeatures
describing academic trajectories, loan characteristics, and administrative records for a
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 3of44
cohort of n borrowers. The problem addressed in this study consists of estimating the
conditional probability of declaration compliance under conditions of class imbalance,
heterogeneousfeatures,anddelayedoutcomerealization,definedas
P(y =1| X), (1)
wherey =1indicatestimelysubmissionoftheincomedeclaration.
TheFSCUcollectionprocessfurtherconstrainsthepredictiontask. Borrowerswho
submittheirincomedeclarationareassignedavariableinstallmentproportionaltotheir
reportedincome. Incontrast,non-compliantborrowersareautomaticallyassignedfixed
installmentswithlongerrepaymenthorizonsandthelossofassociatedbenefits[11]. These
asymmetricoutcomescreateastrongincentivestructure,makingearlyidentificationof
non-complianceparticularlyrelevantforinstitutionalplanning.
Accordingly,theproblemcanbeformalizedasasupervisedbinaryclassificationtask
withinterpretabilityrequirements,wherepredictionsareintendedtosupportanticipatory
decision-makingratherthanautomatedenforcement. Thisformulationenablesanalysisof
theFSCUcasewithinageneralmathematicalframeworkapplicabletoincome-contingent
mechanismsandcompliance-relatedpredictionproblems.
1.3. ResearchObjectivesandQuestions
Theobjectiveofthisstudyistoconstructandevaluatesupervisedclassificationmodels
thatestimatewhetherabeneficiaryoftheFSCUatthePontificiaUniversidadCatólicade
Valparaíso (PUCV) will submit their first annual income declaration. The prediction is
performedusingexclusivelypre-declarationacademic, socioeconomic, andadministra-
tivefeatures,framingthetaskasabinaryclassificationproblemunderinstitutionaland
informationalconstraints.
Morespecifically,thisstudyaimsto
• Identifythepre-declarationvariablesthatcontributemosttothepredictionofincome
declarationcompliance.
• Evaluatethepredictiveperformanceofmultiplesupervisedmachinelearningalgo-
rithmsunderclassimbalanceconditions.
• Assesstheinterpretabilityofmodeloutputsthroughfeatureimportanceandexplana-
tiontechniquesinaninstitutionaldatasetting.
Basedontheseobjectives,thefollowingresearchquestionsareformulated:
1. RQ1: Whichpre-declarationvariablesexhibitthestrongestpredictivecontributionto
incomedeclarationcompliance?
2. RQ2: Howaccuratelycansupervisedlearningmodelspredictdeclarationoutcomes
usingonlyinformationavailablebeforethedeclarationcycle?
3. RQ3: To what extent can interpretable classification models provide transparent
andreliablepredictionsunderinstitutionaldataconstraints,beyondpredictiveaccu-
racyalone?
This study does not aim to introduce new learning algorithms nor novel imbalance-
handlingtechniques. Instead,itadoptsadeliberatelyappliedandinstitutionallygrounded
perspective.Theoriginalityoftheworkliesintheformulationandvalidationofapredictive
frameworkdesignedunderrealisticadministrativeconstraints,whereonlypre-declaration
informationisavailableandsevereclassimbalanceisinherenttotheproblem. Byprioritiz-
ingoperationalfeasibility,methodologicalcoherence,andaudit-orientedinterpretability
overalgorithmicnovelty,thestudyaddressesagapinappliedmachinelearningresearch,
wherepredictivemodelsareoftenevaluatedunderconditionsmisalignedwithreal-world
institutionaldeployment.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 4of44
1.4. IntendedContributions
Thisstudymakesthefollowingcontributionstotheappliedmachinelearningliterature:
• A pre-event predictive problem formulation grounded in realistic administrative
constraints,explicitlyreflectingtheinformationavailabletoinstitutionsbeforethe
targetcompliancebehavioroccurs.
• Acontrolledandreproduciblemethodologicalpipelineforbenchmarkingestablished
supervisedlearningmodelsandimbalance-handlingstrategiesunderaunifiedvalida-
tionandpartitioningprotocol.
• Animbalance-appropriateevaluationstrategythatprioritizestheMatthewsCorrela-
tionCoefficient(MCC)astheprimaryperformancemetric,explicitlylinkingmodel
assessment to the balanced management of Type I and Type II errors in severely
imbalancedsettings.
• A triangulated interpretability design that combines global, structural, and local
explanation methods, positioned as an audit mechanism to support institutional
decision-makingratherthanasaclaimofdirectmodeltransparency.
• Atransferabilityanalysisthatdistinguishescontext-specificelementsfrompipeline-level
methodologicalinsightsapplicabletootherincome-contingentfinancingschemesand
administrativecompliancepredictionproblemsundersimilarpre-eventconstraints.
1.5. StructureofthePaper
The remainder of this paper is organized as follows: Section 2 reviews the most
relevantstudiesandoutlinesthemainresearchgapsidentifiedintheliterature. Section3
describesthedatabases,selectioncriteria,andmethodologicalframeworkadoptedforthe
empiricalanalysis. Section4detailstheexperimentaldesignandevaluationprocedures
applied to ensure replicability and transparency. Section 5 presents the main findings
obtained from the comparative analysis. Section 6 discusses these findings in light of
existing evidence and highlights the implications for future research. Finally, Section 7
summarizestheconclusionsandproposespotentialdirectionsforfurtherinvestigation.
2. RelatedWork
2.1. AbandonmentandDefaultRiskPrediction
Studentloanrepaymentandabandonmenthavebecomepersistentconcernsinhigher
educationfinancingsystems,particularlyincontextswhererepaymentdependsonlong-
term income trajectories rather than fixed installment schedules. In income-contingent
systemssuchasthoseimplementedinAustraliaandtheUnitedKingdom,legaldefault
isrelativelyuncommon;instead,thecentralchallengeliesinanticipatinglong-runnon-
repaymentandassociatedfiscalrisks[12,13]. Conversely,systemswithweakercollection
mechanisms or limited income linkage tend to exhibit higher levels of arrears and bor-
rowerdistress[14,15]. Thesecontrastingdesignshighlighttheimportanceofearlyrisk
identificationoverexpostrecovery.
Comparativepolicyanalysesconsistentlyidentifyacademicnon-completionandso-
cioeconomicvulnerabilityasprimarystructuraldriversofrepaymentdifficulties[8,15].
Borrowerswhofailtocompletetheirprogramsorwhoenterinformallabormarketsex-
hibitreducedrepaymentcapacityandhigherprobabilitiesoffallingintoarrears. From
amodelingperspective, thesefindingsmotivatetheuseofpredictiveapproachescapa-
bleofintegratingacademic,socioeconomic,andadministrativeinformationtoestimate
repaymentorcomplianceriskbeforeadverseoutcomesmaterialize.
Recentstudieshavedemonstratedtheeffectivenessofmachinelearningtechniquesfor
predictingrepayment-relatedoutcomes. Thuyetal.[16]showedthatmachinelearningand
deeplearningmodelsoutperformtraditionalstatisticalapproachesinstudentcreditscoring
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 5of44
tasks. Relatedworkineducationalanalyticsfurthersupportstheuseofinstitutionaladmin-
istrativedataforearlyriskdetection. Forinstance,SuleimanandAnane[17]andYakubu
andAbubakar[18]appliedsupervisedlearningmodelstoacademicandsocioeconomic
datatopredictstudentperformanceandprogression,demonstratingthatprofile-based
representationsimprovepredictiveaccuracy.
Takentogether,theliteratureindicatesthatrepaymentdistressandnon-compliance
behaviorscanbeframedaspredictiveproblemsdrivenbymultidimensionalriskfactors
observablebeforedefaultorabandonment. Thisperspectivesupportsthedevelopmentof
supervisedclassificationmodelsthatestimatethelikelihoodofadverseoutcomesusing
pre-eventinstitutionaldata,providingthemethodologicalfoundationfortheapproach
adoptedinthisstudy.
2.2. Profile-BasedRepresentationinPredictiveModeling
Therepresentationofindividualsthroughmultidimensionalprofilesplaysacentral
roleinpredictivemodelingforhighereducationandcredit-relatedapplications. Tradi-
tionaleconometricapproachestypicallyrelyonalimitedsetofexplanatoryvariables,such
asincome,loanamount,orrepaymenthistory,tomodeldefaultornon-complianceout-
comes[19]. Whilethesemodelsofferinterpretability,theyoftenfailtocapturethecomplex
interactionsthatarisewhenacademic,socioeconomic,andadministrativefactorsjointly
influence borrower behavior, a limitation that has motivated the adoption of machine
learningtechniquesinbotheducationalandcreditrisksettings[20].
Fromamachinelearningperspective,profile-basedmodelingrepresentseachindivid-
ualasafeaturevectorinamultidimensionalspace,allowingheterogeneousattributestobe
integratedwithinaunifiedpredictiveframework. Institutionaldatasetscommonlyinclude
variablesdescribingacademictrajectories,enrollmentcontinuity,completionstatus,and
financialcharacteristics,whichcanbetransformedintostructuredfeaturerepresentations
suitableforsupervisedlearning. Empiricalevidencesuggeststhatsuchrepresentations
oftencontributemoretopredictiveperformancethanthespecificchoiceofalgorithm. For
example,SuleimanandAnane[17]demonstratedthatregression-basedmachinelearning
appliedtoinstitutionaldatacansuccessfullyidentifyat-riskstudents,emphasizingthe
importanceoffeatureconstruction. Similarly,YakubuandAbubakar[18]showedthatcom-
biningsocioeconomic,demographic,andacademicvariablesimprovespredictiveaccuracy
ineducationalcontexts.
In credit management settings, the same representational logic applies. Borrower
profiles that integrate academic progression, socioeconomic background, and adminis-
trativeengagementcanreveallatentpatternsassociatedwithfuturenon-complianceor
repayment distress. By embedding these profiles in a high-dimensional feature space,
machinelearningmodelscancapturenonlinearrelationshipsamongvariablesthatarenot
readilycapturedbylinearmodelingassumptions[21].
Overall,theliteraturesupportstheviewthatprofile-basedrepresentationisacritical
determinantofmodeleffectivenessinpredictivetasksinvolvingheterogeneousinstitu-
tionaldata.Thisinsightmotivatestheadoptionofsupervisedlearningmodelsthatleverage
structuredfeaturespacestoestimatecompliance-relatedoutcomes,formingakeymethod-
ologicalpillaroftheapproachproposedinthisstudy.
Taken together, the reviewed literature highlights two converging insights. First,
repaymentdistressandcompliance-relatedoutcomesinstudentloansystemsaredrivenby
multidimensionalfactorsthatextendbeyondpurelyfinancialattributes. Second,integrat-
ingacademic,socioeconomic,andadministrativedataintoprofile-basedrepresentations
enablesmoreaccurateandrobustpredictivemodeling. Thesefindingsmotivatethedevel-
opmentofsupervisedlearningapproachesthattreatcompliancebehaviorasaclassification
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 6of44
probleminheterogeneousfeaturespacesunderclass-imbalanceconstraints. Buildingon
thismethodologicalfoundation,thefollowingsectiondescribesthedatasources,feature
construction,andmodelingproceduresadoptedinthisstudy.
3. MaterialsandMethods
3.1. DataSourcesandLegalContext
Eachyear,thePUCVFinanceDepartmentrequeststhatborrowerssubmittheirincome
declaration by 31 May. The declaration form includes personal identification, contact
information,pensionaffiliation,andtheborrower’smonthlygrossincome,aswellasthat
ofthespouse,whenapplicable. Supportingdocumentsarerequiredforverification. All
informationisintegratedintotheuniversitysystemandstoredinarelationaldatabase.
Inthisstudy,wesetacutoffdateof24April2024,andrestricttheanalysistoobligations
maturingfrom2012onward,followingthe2012legalreformthatstandardizedtheannual
income-declaration process. Focusing on the post-reform period ensures a consistent
operationalregimeandavoidsstructuralbreakscausedbylegacyrules.
3.2. DatabaseSchema
Thesourcedatabasecompriseseightrelationaltableswithhistoricalrecordsofthe
FSCU portfolio and enrollment information: Person, Promissory Note, Due Group, Debt,
Installment,PaymentSlip,IncomeDeclaration,andEnrollments. Fordatamanagementand
queryperformance,thecontentsweremigratedtoPostgreSQLpriortodatasetconstruction.
3.3. CohortDefinitionandTarget
Theworkingdatasetisconstructedattheborrowerlevelusingexclusivelyinformation
availablepriortothefirstincome-declarationdeadline. Lety ∈ {0,1}denotethedeclara-
i
tionoutcomeforborroweri,wherey =1indicatessubmissionofthefirstincomedeclara-
i
tionandy =0otherwise. Toensureconsistencywiththecurrentoperationalregime,only
i
recordscorrespondingtoobligationsmaturingfrom2012onwardwereincluded,following
thelegislativereformthatstandardizedtheannualincome-declarationprocess.
Thefeaturespacecomprisesnumerical,categorical,anddate-derivedvariablesdescrib-
ingborrowerdemographics,loancharacteristics,andacademictrajectory. Exactvariable
countsbytypearereportedinTable1. Intotal,theinitialdatasetconsistsofthebinary
targetvariableandaheterogeneouscollectionoffeaturesderivedfromadministrativeand
academicrecordsavailablebeforethedeclarationevent.
AsdiscussedinSection1,compliancewiththeincome-declarationrequirementplays
a central role in the functioning of income-contingent loan systems. From a modeling
perspective,understandingthefactorsassociatedwithfirst-timedeclarationbehavioris
essentialforcharacterizingcompliancepatternsunderinformationalconstraints.
Accordingly,thisstudyfocusesonpredictingwhetheraborrowerwillsubmitthefirst
incomedeclarationusingpre-declarationinformationonly, includingattributesrelated
to the borrower profile, loan characteristics, and academic history. By analyzing both
compliantandnon-compliantcases,theobjectiveistoidentifysystematicpatternsthatcan
informclassification-basedriskestimationwithinasupervisedlearningframework.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429
7of44
Table1.Initialfeaturepoolpriortopreprocessing.
| Name                    | DataType | FeatureType | Detail                     |
| ----------------------- | -------- | ----------- | -------------------------- |
| estado_civil            | Boolean  | Categorical | 1and2                      |
| nacionalidad            | Boolean  | Categorical | 1and2                      |
| sexo                    | Boolean  | Categorical | MandF                      |
| fecha_nacimiento        | Date     | Date        | 1January1900to26March1991  |
| edad                    | Integer  | Numerical   | 21to119                    |
| edad_dias               | Integer  | Numerical   | 7860to43,646               |
| deud_monto              | Float    | Numerical   | 0.571to1285.762            |
| deud_fecha_exigibilidad | Date     | Date        | 1January1994to1January2023 |
| deud_t_deuda            | Integer  | Categorical | 1value                     |
| tiene_declaracion       | Boolean  | Target      | 0and1                      |
| monto_total_pagare      | Float    | Numerical   | 1.32to922.22               |
| conteo_pagare           | Integer  | Numerical   | 1to29                      |
| anio_ult_matr           | Integer  | Categorical | 13values                   |
| e_ult_matr              | Integer  | Categorical | 1value                     |
| cod_carr_ult_matr       | Integer  | Categorical | 80values                   |
| carr_t_carrera          | Integer  | Categorical | 1value                     |
| cod_inst_ult_matr       | Integer  | Categorical | 1value                     |
| conteo_matr             | Integer  | Numerical   | 1to31                      |
| facultad                | String   | Categorical | 9values                    |
| escuela                 | String   | Categorical | 34values                   |
| stem                    | Boolean  | Categorical | 0and1                      |
3.4. FeatureConstruction
The feature construction process was guided by the need to balance predictive ex-
pressiveness,interpretability,andstricttemporalvalidity. Inparticular,allrepresentations
were deliberately constrained to borrower-level summaries observable before the first
income-declarationdeadline,reflectingtheinformationrealisticallyavailableforinstitu-
tionaldecision-makingatthatstage.
Thepredictivetaskrequiresaborrower-levelrepresentationinwhicheachobservation
correspondstotheinformationavailablebeforethefirstincome-declarationdeadline. Ac-
cordingly,aflatdatasetwasconstructed,whereeachrowrepresentsauniqueborrowerand
eachcolumncorrespondstoapre-declarationattributederivedfromacademic,financial,
oradministrativerecords.
LetD = {(X,y )}n denotetheresultingdataset,whereX ∈Rpisthefeaturevector
|     | i i | i=1 | i   |
| --- | --- | --- | --- |
associated with borrower i, and y ∈ {0,1} indicates whether the borrower submitted
i
thefirstincomedeclaration. Featureconstructionwasstrictlyconstrainedtoinformation
observablebeforethedeclarationdeadlinetopreventtemporalleakage.
Theoriginaldataarestoredinarelationalschemacomprisingmultipletableswithone-
to-manyrelationships,suchasenrollmentrecordsandpromissorynotes. Toobtainafixed-
dimensionalrepresentationsuitableforsupervisedlearning,borrower-levelaggregation
operatorswereappliedtorecurringrecords. Inparticular, count-basedandsum-based
aggregationswereusedtosummarizeenrollmenthistoryandloan-relatedinformation,
yieldingscalarfeaturesthatpreservecumulativeexposurewhileensuringdimensional
consistencyacrossobservations.
Two additional categorical attributes describing the undergraduate program were
appendedafterextraction. Thesevariablesarestaticwithrespecttothepredictionhorizon
anddonotdependonpost-declarationinformation,makingthemadmissibleforinclusion
inthepre-declarationfeaturespace.
Asmallsubsetofborrowersholdsmorethanoneloaninthesourcedatabase(166cases,
representing less than 0.01% of the sample). To preserve a consistent unit of analysis
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 8of44
and avoid duplicate borrower histories, only the first loan per borrower was retained.
Previously,forborrowerswithmultipleloans,thefeaturevectorX wasconstructedfrom
i
theearliestloanrecord,ensuringthateachobservationcorrespondstoasingle,well-defined
predictioninstance.
As a result, the final feature matrix X ∈ Rn×p provides a borrower-centric, fixed-
dimensionalrepresentationthatintegratesacademictrajectory,loancharacteristics,and
institutionalattributesavailablepriortothedeclarationevent. Thisconstructionenables
theapplicationofstandardsupervisedclassificationalgorithmswhilemaintainingaclear
correspondencebetweenmodelinputsandtheunderlyingadministrativeprocesses.
3.5. FeatureSetOverview
Themodelingprocessbeginswithaninitialpooloffeaturesextractedfromacademic
andadministrativerecordsavailablepriortothefirstincome-declarationdeadline. Thisini-
tialfeaturepoolissubsequentlyrefinedthroughthedatacleaning,consolidation,encoding,
andtransformationstepsdescribedinthefollowingsubsections,yieldingareducedand
consistentfeaturesetusedformodeltrainingandevaluation.
Fortransparencyandreproducibility,boththeinitialfeaturepoolandthefinalfeature
set are reported. Table 1 summarizes the variables initially extracted from the source
databases,whileTable2providessemanticdescriptionsoftheinitiallyextractedvariables
priortoanypreprocessing,consolidation,orfeatureselectionsteps. Variablenamesare
retainedintheiroriginalSpanishform,astheycorresponddirectlytofieldidentifiersused
intheofficialFSCUadministrativedatabases. InTable3reportsthevariablesexhibiting
missingobservations. Table4reportsthefeaturesretainedafterpreprocessingandfeature
engineering. Preservingthisnomenclatureensurestraceability,consistency,andalignment
with operational institutional data structures. For clarity, all variables are explicitly de-
scribedandinterpretedinEnglishwithinthetable,allowinginternationalreaderstofollow
theanalysiswithoutambiguity.
Table2.Featureset:detaileddescriptionsofeachvariable.
Feature Description
estado_civil Lastknownmaritalstatusofthedebtor.Itcantakethefollowingvalues:1notmarried,2married
nacionalidad WhetherthedebtorisChileanorforeign.1meansChilean,2meansforeign
sexo Genderofthedebtor.MmeansmaleandFmeansFemale
fecha_nacimiento Birthdateofthedebtor
edad Ageinyearsofthedebtoratthemomentthatthedebtisenforceable
edad_dias Ageindaysofthedebtoratthemomentthatthedebtisenforceable.
deud_monto Totalloanamount
deud_fecha_exigibilidad Dateofenforceabilityoftheloan
deud_t_deuda Typeofloancontracted
Whetherthedebtorhandedtheirfirstincomedeclarationornot.1Meanstheyhandeditand0means
tiene_declaración
theydidnot.TargetVariable
monto_total_pagare Totalvalueofpromissorynotessignedbythedebtor
conteo_pagare Amountofpromissorynotessignedbythedebtor
anio_ult_matr Yearofthelastcollegeenrollmentofthedebtor
e_ult_matr Statusofthelastcollegeenrollmentofthedebtor.1meanstheenrollmenthasavalidstatus
cod_carr_ult_matr Codeofthedegreeprogramcoveredbytheloan
carr_t_carrera Typeofdegreeprograminthelastcollegeenrollmentofthedebtor.1meansundergraduateprogram
cod_inst_ult_matr Institutioncodeinthelastcollegeenrollmentofthedebtor
conteo_matr Totalamountofenrollmentsofthedebtorwithinthedegreeprogramcoveredbytheloan
facultad Facultyofthedegreeprogram
escuela Schoolofthedegreeprogram
WhetherthedegreeprogramcoveredbytheloanisaSTEMoneornot.1meansthedegreeprogramis
stem
aSTEMprogram,0meansitisnot
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 9of44
Reportingboththeinitialandfinalfeaturesetsallowsthereadertotracehowmethod-
ologicaldecisionsprogressivelyreducedimensionalitywhilepreservinginstitutionalmean-
ing,therebysupportingtransparencyandreliabilityinanappliedadministrativecontext.
3.6. DataCleaningandPreprocessing
Datacleaningandpreprocessingdecisionsweredrivenbythedualobjectiveofpre-
serving as much administratively meaningful information as possible while ensuring
numerical stability and interpretability under severe class imbalance. Rather than ap-
plying aggressive filtering or imputation, the adopted strategy prioritizes conservative
transformationsalignedwithinstitutionaldataqualityanddeploymentconstraints.
3.6.1. MissingValues
Figure1summarizesthenumberofmissingvaluesobservedineachextractedfeature.
This exploratory analysis enables the identification of variables affected by incomplete
informationandguidessubsequentpreprocessingdecisions.
Figure1.Missingvaluesacrossdatasetfeaturescomparedtothedatasetsize(red-dottedline).
Five variables exhibit missing observations, as reported in Table 3. The variables
fecha_nacimiento,edad,andedad_diaspresentidenticalmissingnesspatterns,sincethelatter
two are deterministically derived from the birth date. Given the high proportion and
completeoverlapofmissingvaluesacrossthesethreeattributes,theywereexcludedfrom
thefeaturesettoavoidredundantlossofinformationandunstableimputations.
Formally,letX
∈Rn×p
denotetheoriginalfeaturematrix. Thefilteredfeaturematrix
X′wasobtainedbyremovingthecolumnscorrespondingtotheaffectedvariablessuchthat
X ′ = X\{fecha_nacimiento,edad,edad_dias}. (2)
In contrast, the variable escuela presents a small number of missing values corre-
spondingtodegreeprogramswithoutanassociatedschool. Ratherthandiscardingthese
observations,adedicatedcategoricallevelwasintroducedtoencodetheabsenceofanas-
signedschool,therebypreservingtheaffectedrecordsandretainingpotentiallyinformative
structureinthedata.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 10of44
Table3.Featureswithmissingvalues.
ColumnName MissingValues
sexo 9583
fecha_nacimiento 9614
edad 9614
edad_dias 9614
escuela 22
Thishandlingstrategyreflectsadeliberatetrade-offbetweeninformationretention
andmodelrobustness,favoringtheexclusionofhighlyincompleteandredundantvariables
whilepreservingpartiallymissingcategoricalinformationthroughexplicitencoding.
3.6.2. ClassConsolidationandRareCategories
Classconsolidationdecisionswereguidedbytheneedtoreducesparsityandunstable
parameterestimationwhilemaintainingasemanticallycoherentrepresentationaligned
withinstitutionalpractice.
Toassessthedistributionalpropertiesoftheconstructedfeaturespace,anexploratory
analysis was performed on both numerical and categorical variables. Figures 2–4 sum-
marizetheempiricaldistributionsobservedacrossthedatasetandprovideguidancefor
subsequentconsolidationdecisions.
(a)conteo_matrDistribution (b)conteo_pagareDistribution
(c)deud_montoDistribution (d)monto_total_pagareDistribution
Figure2.Distributionofselectednumericalfeatures.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 11of44
(a)estado_civilDistribution (b)deud_t_deudaDistribution
(c)tiene_declaracionDistribution (d)anio_ult_matrDistribution
(e)e_ult_matrDistribution
Figure3.Distributionofselectedcategoricalfeatures(PartI).
NumericalFeatureDistribution
Figure 2 present the distributions of selected numerical variables, including the
number of enrollments (conteo_matr), the number of promissory notes (conteo_pagare),
the outstanding debt amount (deud_monto), and the total value of promissory notes
(monto_total_pagare).
Althoughsomevariablesexhibitsimilardistributionalshapes(e.g.,Figure2c,d),none
of the numerical features display degenerate or constant behavior. Consequently, all
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 12of44
numericalvariableswereretainedatthisstageandfurtherexaminedthroughcorrelation
analysistoevaluatepotentialredundancy,asdiscussedinSection3.6.3.
(a)carr_t_carreraDistribution (b)cod_inst_ult_matrDistribution
(c)facultadDistribution (d)stemDistribution
Figure4.Distributionofselectedcategoricalfeatures(PartII).
CategoricalFeatureDistribution
Figures3–6illustratetheempiricaldistributionsofthecategoricalvariables. These
features describe marital status, loan attributes, declaration status, academic trajectory,
andinstitutionalaffiliation. Thevisualinspectionhighlightsdominantcategories,sparsity
patterns,andvariableswithlimitedvariability.
Categoricalvariablesexhibitinginvariantbehaviorwithintheanalyzedcohortwerere-
moved,astheyprovidenodiscriminativeinformationfortheclassificationtask.Specifically,
thefeaturescarr_t_carrera,cod_inst_ult_matr,deud_t_deuda,ande_ult_matrwereexcluded
fromthefeatureset.
Verylow-frequencycategorieswerealsoaddressedtoreducesparsityandprevent
unstableparameterestimation. The“foreign”categoryinnacionalidad,comprisingsixob-
servations,wasremovedduetoitsnegligiblerepresentation. Similarly,asingleobservation
correspondingtotheyear2008inanio_ult_matrwasexcluded.Tofurthercontrolcategorical
cardinality, thevariablescod_carr_ult_matrandescuelawereconsolidatedatthefacultad
level,yieldingamorecompactandsemanticallycoherentrepresentation.
Inaddition,asmallsubsetofborrowersholdsmorethanoneFSCUdebtassociated
withthesameinstitution(166cases,representinglessthan0.01%ofthefinalsampleafter
excluding non-PUCV loans). These records correspond to second or subsequent debts
acquired by the same borrower, rather than to independent or parallel loan events. To
preserveaconsistentandinstitutionallymeaningfulunitofanalysis,onlythefirstFSCU
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 13of44
debtperborrowerwasretained. Includingsecondarydebtsasseparateobservationswould
implicitlyintroducealongitudinaldimensionbasedonaverylimitednumberofcases,
increasingmodelcomplexitywhileriskingbiastowardatypicalborrowertrajectories.
Figure5.cod_carr_ult_matrDistribution.
Figure6.escuelaDistribution.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 14of44
ThisaggregationstrategywasfurthervalidatedinconsultationwiththeFSCUman-
agementunitatPUCV,whichconfirmedthatthefirstdebtconstitutestheprimaryadmin-
istrativereferenceforenforceabilityandearly-stagemonitoringprocesses. Accordingly,
theresultingdatasetadoptsaborrower-centricrepresentationalignedwithinstitutional
practicewhileavoidingunnecessarydimensionalexpansionorinstabilityinsubsequent
modelingstages.
Afterconsolidatingcategoricalvariablesandreducingsparsity,theresultingfeature
spacewasexaminedforredundancyamongnumericalattributes,asdetailedinthefollow-
ingsubsection.
3.6.3. CorrelationScreening
Correlationscreeningwasintroducedasapragmaticdimensionality-reductionstepto
mitigatemulticollinearityeffectsthatcoulddistortbothmodelestimationanddownstream
interpretabilityanalyses.
Toidentifypotentialredundancyamongnumericalvariables,pairwiselineardepen-
dence was assessed using Pearson’s correlation coefficient. Let x and x denote two
j k
numericalfeatures. TheirPearsoncorrelationisdefinedas
cov(x ,x )
j k
r = , (3)
jk
σ σ
xj xk
wherecov(·,·)denotescovarianceandσ thestandarddeviationofvariablex.
x
Figure7presentstheempiricalcorrelationmatrixcomputedoverthenumericalfeature
subset. Athresholdof|r | ≥ 0.70wasadoptedasapragmaticcriteriontoflagpairsof
jk
variablesexhibitingstronglinearassociationand,therefore,potentialcollinearity.
Figure7.Pearsoncorrelationheatmapamongnumericalfeatures.
Threevariablepairsexceededtheselectedthreshold: (deud_monto,monto_total_pagare),
(monto_total_pagare, conteo_pagare), and (deud_monto, conteo_pagare). To mitigate multi-
collinearityeffects,onlyonerepresentativevariablefromthiscorrelatedgroupwasretained.
Specifically,deud_montowaspreservedduetoitsdirectinterpretabilityandexplicitassocia-
tionwiththeloanmagnitude,whilemonto_total_pagareandconteo_pagarewereremoved
fromthefeatureset.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 15of44
Formally,letF denotethesetofnumericalfeaturespriortoscreeningandF′
num num
thereducedsetaftercorrelationfiltering. Theselectioncanbeexpressedas
F′ = F \{monto_total_pagare,conteo_pagare}. (4)
num num
This selection balances dimensional parsimony and interpretability, ensuring that
stronglycollinearmonetaryvariablesdonotdistortmodelestimation,numericalstability,
orfeatureimportanceanalysesinsubsequentclassificationstages.
3.6.4. EncodingandScaling
Toensurecompatibilitywithsupervisedlearningalgorithmsandtoavoidintroducing
artificialordinalrelationships,categoricalvariablesweretransformedusingone-hoten-
coding. Letx(c) ∈ C denoteacategoricalfeaturetakingvaluesinafinitesetofcategories.
Theencodingmapsx(c) toabinaryvectorin{0,1}|C|,whereeachcomponentindicatesthe
presenceofaspecificcategory. Thistransformationpreservescategorymembershipwhile
enablinglinearandnon-linearclassifierstooperateonanumericalfeaturespace.
Thischoiceensuresthatcategoricaldistinctionsarepreservedwithoutimposingartifi-
cialordinality,whilenumericalscalingsupportsstableoptimizationacrossheterogeneous
modelfamilies.
Numericalvariableswerestandardizedtoensurecomparablescalesandstablenu-
mericalbehaviorduringmodeltraining. Givenanumericalfeaturex,standardizationwas
performedusingthez-scoretransformation
x−µ
z = , (5)
σ
whereµandσdenotethesamplemeanandstandarddeviation,respectively. Thistransfor-
mationyieldsfeatureswithzeromeanandunitvariance,reducingscaledominanceeffects
indistance-basedandgradient-basedlearningalgorithms.
Thecombinedpreprocessingpipelinecanbeviewedasatransformation
Φ : X → X˜, (6)
whereXdenotestheoriginalfeaturematrixandX˜ theencodedandstandardizedrepresen-
tationusedformodelestimation.
Thispreprocessingstrategypreservesinterpretabilitywhileimprovingnumericalsta-
bilityandreducingnoiseduringtraining. Inparticular,byretainingasinglerepresentative
monetaryfeaturefollowingcorrelationscreening,thetransformationavoidsredundancy
amongvariablesexpressingsimilarfinancialmagnitudeandmaintainsaclearconceptual
linkbetweenfinancialexposureandtheprobabilityofnon-compliance.
Afterencodingcategoricalvariablesandscalingnumericalones,temporalfeatures
wereprocessedseparately,asdescribedinthefollowingsubsection.
3.6.5. DateHandling
Temporalvariableswerehandledwithparticularcautiontoretaininterpretabilitywhile
avoidingunnecessarydimensionalexpansioninasettingwithlimitedtemporalgranularity.
Afterpreprocessingcategoricalandnumericalvariables,temporalinformationwas
handled separately. Only one date-related attribute remains in the feature set, namely
deud_fecha_exigibilidad. Itsempiricaldistribution,asshowninFigure8,exhibitstwopro-
nounceddensityvalleysassociatedwithspecificenforceabilityperiods,whiletheremaining
datespresentrelativelyuniformfrequencies. Theaforementionedvalleysarespecifically
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 16of44
Januaryfirstof2013withsixvaluesandJanuarysecondof2022withonevalue. Forcontext,
Januarythirdof2013has1109values,whileJanuaryfirstof2022has1006values.
Figure8.Distributionofenforceabilitydates(deud_fecha_exigibilidad).
Toobtainanumericalrepresentationsuitableforsupervisedlearning,thedatevariable
wasdecomposedintoitsconstituentcomponents: day,month,andyear. Letd denotethe
i
enforceabilitydateassociatedwithborroweri. Thetransformationcanbeexpressedas
d (cid:55)−→ (day,month,year). (7)
i i i i
TheresultingmarginaldistributionsofthesecomponentsareshowninFigure9as
HistogramswithaKernelDensityEstimatetoprovideasmoothpictureofthedistribution.
Asallobservationscorrespondtothesamecalendarmonth(May),asevidencedinFigure9b,
themonthcomponentexhibitszerovarianceacrossthedatasetandthereforeprovidesno
discriminativeinformationfortheclassificationtask. Consequently,itwasexcludedfrom
thefeatureset.
(a)DayDistribution (b)MonthDistribution (c)YearDistribution
Figure9.Decompositionofenforceabilitydatesintoday,month,andyearcomponents.
Theretainedtemporalcomponentsthusdefineareducedrepresentation(day,year),
i i
operationalizedinthefinaldatasetasthevariablesdia_exigibilidadandanio_exigibilidad.
Thisdecompositionensuresthatthenumericalencodingofdatesremainsinformativeyet
parsimonious,facilitatingconsistentscalingandinterpretationwithinthemachinelearning
pipelineandallowingtemporalinformationtocontributemeaningfullytotheestimation
ofclassificationfunctionswithoutintroducingunnecessarydimensionalcomplexity.
Theresultingfeaturematrixandtargetvariable,presentedinTable4,weresubsequently
usedtotrainandevaluatesupervisedclassificationmodelsunderaconsistentvalidation
protocol. Thenextsectiondescribesthecomputationalsetup,trainingandtestingstrategy,
andevaluationmetrics.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429
17of44
Table4.Finalfeaturesetusedformodeltrainingafterpreprocessingandfeatureengineering.
| Name         | DataType | FeatureType | Detail |
| ------------ | -------- | ----------- | ------ |
| estado_civil | Boolean  | Categorical | 1and2  |
nacionalidad Boolean Categorical Filtered(foreigncategoryremoved)
| sexo              | Boolean | Categorical | MandF          |
| ----------------- | ------- | ----------- | -------------- |
| deud_monto        | Float   | Numerical   | standardized   |
| dia_exigibilidad  | Integer | Numerical   | 1to31          |
| anio_exigibilidad | Integer | Numerical   | multipleyears  |
| anio_ult_matr     | Integer | Categorical | filteredvalues |
| conteo_matr       | Integer | Numerical   | 1to31          |
| facultad          | String  | Categorical | 9values        |
| stem              | Boolean | Categorical | 0and1          |
| tiene_declaracion | Boolean | Target      | 0and1          |
4. ExperimentalSetup
Thissectiondescribesthecompleteexperimentalconfigurationusedtoevaluatethe
proposedsupervisedbinaryclassificationframework. Allstagesofdatapartitioning,pre-
processing,resampling,modeltraining,hyperparameteroptimization,andevaluationwere
designedtoensuremethodologicalrigorandtopreventinformationleakage,supporting
reliableandauditableempiricalassessment.
4.1. ComputationalEnvironment
AllexperimentswereexecutedonadedicatedserverequippedwithanIntelCore
i9-10900KCPUand64GBofDDR4RAM.Datamanipulationandnumericaloperations
wereconductedusingPandas(v2.1.4)andNumPy(v1.26.3). Machinelearningmodelswere
implementedusingscikit-learn(v1.7.1),whilegradientboostingmodelsweretrained
usingLightGBM(v4.6.0). Classimbalancetechniqueswereappliedviaimbalanced-learn
(v0.14.0). FeatureattributionanalysesweresupportedbytheSHAPlibrary(v0.48.0).
4.2. DataPartitioningandValidationProtocol
Thedatasetwasinitiallydividedintoatrainingset(70%)andanindependenttestset
(30%) asawidelyadoptedpracticeinthemachinelearningliterature(e.g.,[22,23]),and
becauseitprovidesasufficientlylargehold-outsettoobtainstableandreliableestimates
ofperformancemetricsunderclassimbalance. Fromanoperationalperspective,thissplit
enablesaclearseparationbetweenmodeldevelopmentandfinalevaluation,withthetest
setservingasaproxyforunseenfuturecohorts,whilepreservingenoughtrainingdatato
supportrobustmodelfittingandcross-validatedhyperparametertuning.
Withinthetrainingset,allmodelselectionandhyperparametertuningprocedures
wereconductedusingstratifiedK-foldcross-validation. Thisstrategyensuresthatclass
proportionsremainconsistentacrossfoldsandprovidesanunbiasedestimateofgener-
alizationperformance. Ateachfold,preprocessing,resampling,andmodelfittingwere
performedexclusivelyonthecorrespondingtrainingpartition, therebypreventingany
formofdataleakage.
4.3. PipelineStructure
Eachexperimentfollowedaunifiedpipelinearchitecturecomposedofthefollowing
sequentialstages:
1. Training–validationsplitaccordingtothecross-validationfold.
2. Featurescalingwhenrequiredbythelearningalgorithm.
3. Applicationofclassimbalancehandlingtechniques.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 18of44
4. Modeltrainingusingaspecifichyperparameterconfiguration.
5. Validationperformanceestimationusingpredefinedevaluationmetrics.
All transformations were fitted exclusively on training data within each fold and
subsequentlyappliedtothecorrespondingvalidationsubset. Thispipelinewasapplied
uniformlyacrossallexperiments.
4.4. PredictiveModels
Sevensupervisedlearningalgorithmswereevaluated: KNearestNeighbors,Naive
Bayes,LogisticRegression,LinearSupportVectorClassifier,DecisionTree,RandomForest,
and Light Gradient Boosting Machine. Non-linear kernel variants of Support Vector
Machineswereexcludedafterpreliminaryanalysisduetoconsistentlyinferiorperformance
onthestudiedfeaturespace.
4.5. ClassImbalanceHandling
Thetargetvariableexhibitsapronouncedclassimbalance,withthenon-declaration
class representing the minority group. To address this issue, three resampling strate-
gieswereevaluatedwithinthetrainingfolds, followingstandardapproachesforlearn-
ingfromimbalanceddata[3]. Theresamplingprocedureswereimplementedusingthe
imbalanced-learnlibrary[24]:
• SyntheticMinorityOver-SamplingTechnique(SMOTE),
• AdaptiveSyntheticSampling(ADASYN),
• RandomUnder-Samplingofthemajorityclass.
Thechoiceofresamplingmethodanditsassociatedparametersweretreatedashy-
perparametersandjointlyoptimizedwiththeclassifierconfiguration. Resamplingwas
appliedexclusivelytothetrainingportionofeachcross-validationfold.
4.6. HyperparameterOptimization
Model and sampling hyperparameters were optimized using an exhaustive grid
searchstrategyembeddedwithinthecross-validationprocedureappliedtothetrainingset.
LetΘdenotethediscretesearchspacedefinedbytheCartesianproductofallcandidate
hyperparametervaluesforagivenmodel–samplingconfiguration. Foreachθ ∈ Θ,model
performancewasestimatedusingstratifiedK-foldcross-validation.
Formally,letMCC (θ)denotetheMatthewsCorrelationCoefficientobtainedonthe
k
validation subset of the k-th fold when training the model with configuration θ. The
optimalhyperparameterconfigurationθˆwasselectedbymaximizingthemeanvalidation
performanceacrossfolds,definedas
θˆ =argmax 1 ∑ K MCC (θ). (8)
θ∈Θ K
k=1
k
Thisoptimizationprocesswasappliedconsistentlyacrossallclassifiersandresam-
plingstrategies. Thecompletehyperparametergridsexploredforpredictivemodelsand
samplingmethodsarereportedinTables5and6,respectively.
Although exhaustive grid search entails a higher computational cost compared to
heuristicorrandomizedalternatives,itensuresasystematicexplorationofthepredefined
parameterspaceandavoidsbiasesassociatedwithadhochyperparameterselection. This
designchoicesupportsafairandmethodologicallycontrolledcomparisonacrossmodels
andconfigurations.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429
19of44
Table5.Hyperparametergridusedformodelgridsearchstrategy.
| Model        | Hyperparameter    | Values                                 |     |     |
| ------------ | ----------------- | -------------------------------------- | --- | --- |
|              | n_neighbors       | 5,7,9,11,14,18,22,25,28,35,40,45,50,70 |     |     |
| KNN          | weights           | “uniform”,“distance”                   |     |     |
|              | p                 | 1,2                                    |     |     |
|              | n_estimators      | 20,50,100,200,500,800                  |     |     |
|              | max_depth         | None,5,10,20,50,70                     |     |     |
| RandomForest | min_samples_split | 2,10,20,50,70,100                      |     |     |
|              | min_samples_leaf  | 1,2,4,6,10,30                          |     |     |
|              | max_features      | “sqrt”,“log                            | ”   |     |
2
|     | n_estimators | 20,30,50,100,500,600,800,1000 |     |     |
| --- | ------------ | ----------------------------- | --- | --- |
|     | max_depth    | None,5,10,20,50,70            |     |     |
LightGBM
|     | learning_rate | 0.01,0.05,0.1,0.12,0.15,0.2        |     |     |
| --- | ------------- | ---------------------------------- | --- | --- |
|     | num_leaves    | 2,4,8,15,31,50,100                 |     |     |
|     | C             | 0.00001,0.0001,0.001,0.01,0.1,1,10 |     |     |
| SVM | loss          | “hinge”,“squared_hinge”            |     |     |
|     | penalty       | ‘l1’,‘l2’                          |     |     |
|     | C             | 0.01,0.1,1,5,10                    |     |     |
LogisticRegression
|     | solver | “lbfgs”,“sag”,“saga” |     |     |
| --- | ------ | -------------------- | --- | --- |
1×10−9,1×10−8,1×10−7,1×10−6,
| NaiveBayes | var_smoothing |     |     |     |
| ---------- | ------------- | --- | --- | --- |
1×10−4,1×10−2
|     | max_depth         | None,5,10,20,50,70 |     |     |
| --- | ----------------- | ------------------ | --- | --- |
|     | min_samples_split | 2,10,20,50,70,100  |     |     |
DecisionTree
|     | min_samples_leaf | 1,2,4,6,10,30 |     |     |
| --- | ---------------- | ------------- | --- | --- |
|     | max_features     | “sqrt”,“log   | ”   |     |
2
Table6.HyperparametergridusedforSamplinggridsearchstrategy.
| SamplingStrategy | Hyperparameter     |     | Values              |     |
| ---------------- | ------------------ | --- | ------------------- | --- |
| OverSampling     | Ratio              |     | 0.6,0.7,0.8,1       |     |
| UnderSampling    | TargetSampleValues |     | 4000,5000,5500,6000 |     |
4.7. EvaluationMetrics
Modelperformancewasassessedusingfivecomplementarymetricsderivedfrom
the confusion matrix: Accuracy, Precision, Recall, F -score, and Matthews Correlation
1
Coefficient(MCC).Thesemetricscapturedistinctaspectsofclassificationbehaviorandare
particularlyappropriateforbinaryclassificationproblemsunderclassimbalance.
Let TP, FP, TN, and FN denote the number of true positives, false positives, true
negatives,andfalsenegatives,respectively. Accuracymeasurestheproportionofcorrectly
classifiedinstancesoverthetotalnumberofobservations:
TP+TN
|     | Accuracy= |     | .   | (9) |
| --- | --------- | --- | --- | --- |
TP+TN+FP+FN
Althoughwidelyused,Accuracymayprovidemisleadingassessmentswhenclassdistribu-
tionsarehighlyunbalanced.
Precisionquantifiestheproportionofpositivepredictionsthatarecorrectlyclassified,
andisdefinedas:
TP
Precision=
|     |     |     | .   | (10) |
| --- | --- | --- | --- | ---- |
TP+FP
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 20of44
Recallmeasurestheproportionofactualpositiveinstancesthatarecorrectlyidentified:
TP
Recall= . (11)
TP+FN
PrecisionandRecallcharacterizecomplementaryaspectsofclassificationerror,particularly
inscenarioswherethecostsoffalsepositivesandfalsenegativesdiffer.
TheF -scorecorrespondstotheharmonicmeanofPrecisionandRecall,providinga
1
balancedsummaryofbothmeasures:
Precision·Recall
F =2· . (12)
1 Precision+Recall
Finally,theMatthewsCorrelationCoefficient(MCC)providesacomprehensiveevalu-
ationbyincorporatingallfourelementsoftheconfusionmatrix:
TP·TN−FP·FN
MCC= (cid:112) . (13)
(TP+FP)(TP+FN)(TN+FP)(TN+FN)
MCC ranges from −1 to 1, where values close to 1 indicate perfect classification, 0 cor-
responds to random prediction, and negative values indicate systematic disagreement
between predictions and true labels. This metric is particularly robust in imbalanced
classificationsettings,asitaccountsforallfourcomponentsoftheconfusionmatrixand
providesabalancedevaluationevenwhenclassdistributionsareskewed[25].
All reported results correspond to performance on the held-out test set using the
hyperparameterconfigurationselectedduringcross-validation.
4.8. FeatureImportanceAnalysis
Toanalyzethecontributionofindividualpredictors,bothmodel-specificandmodel-
agnosticfeatureimportancetechniqueswereemployed. Forclassifiersprovidingintrinsic
interpretability, native importance measures were extracted, including impurity-based
importancefortree-basedmodelsandcoefficientmagnitudesforlinearmodels.
Additionally, permutation feature importance was computed as a model-agnostic
approach [26]. This method quantifies the decrease in predictive performance induced
byrandomlypermutingasinglefeature,therebybreakingitsassociationwiththetarget
variable. Formally,theimportanceoffeature f isdefinedas:
j
1 ∑ R
i = s− s (14)
j
R
r,j
r=1
wheresdenotestheoriginalmodelscoreands representsthescoreobtainedafterthe
r,j
r-thpermutationoffeature f .
j
Thisanalysiswasconductedonvalidationdataandenablesconsistentcomparisonof
featurerelevanceacrossheterogeneousmodelfamilies,subjecttoknownlimitationsinthe
presenceofhighlycorrelatedpredictors.
4.9. Reproducibility
All experiments were conducted using fixed random seeds for data partitioning,
resampling,andmodelinitialization. Softwareversionsandexperimentalconfigurations
were explicitly controlled to ensure that results could be consistently replicated under
identicalconditions. Thisdesignsupportstransparentverificationofthereportedfindings
andfacilitatesmethodologicalscrutinyinappliedinstitutionalsettings.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 21of44
5. Results
This section presents the results obtained from the experiments described in the
previous sections. Section 5.1 summarizes the evaluation metrics achieved by each al-
gorithmintroducedinSection4.4,includingboththebaselineconfigurationsandthose
incorporatingdata-balancingtechniquesdiscussedinSection4.5. Inthebest-performing
configurationsreportedinthissection,thesyntheticoversamplingmethodsSMOTEand
ADASYNusedasampleratioof0.7,whileRandomUndersamplingreducedthemajority
classto5500instances. Eachconfigurationwasalsotestedwithandwithouthyperparame-
teroptimization,asdescribedinSection4.6,resultingineightexperimentalcombinations
peralgorithm.
Section 5.2 complements this analysis by presenting the confusion matrices of the
best-performingexperimentforeachmodel,providingadetailedviewoferrordistribution
andclass-levelperformance.
Finally,Section5.3exploresthefactorsthatdrivethemodels’predictions,combining
globalandlocalinterpretabilityanalyses. Itintegratespermutationimportanceandmodel-
wisefeatureanalyseswithvisualinspectionsofDecisionTreestructuresatmultipledepths
(Section5.3.3)andSHAPvaluevisualizations(Section5.3.4).Together,theseresultsprovide
bothaggregateandinstance-levelexplanations,offeringacomprehensiveunderstanding
ofhowmodeldecisionsalignwithobservableborrowerbehavior.
5.1. ModelPerformance
Tables 7–13 summarize the test-set performance of all algorithms under the eight
experimentalconfigurationsdescribedearlier. Astheprimaryselectioncriterion,MCC
differentiatesthemostcompetitiveconfigurationsunderclassimbalance,whileAccuracy,
Precision,Recall,andtheF -scoreprovidecomplementaryviewsofclassificationbehavior.
1
UnoptimizedDecisionTreesandNaiveBayespipelinesshowweakerperformance,whereas
theiroptimizedvariantsimprovesubstantially.
Table7.K-NearestNeighborsResults.
Pipeline Accuracy Precision Recall F1-Score MCC
KNN 0.746 0.795 0.872 0.832 0.323
SmoteKNN 0.701 0.814 0.758 0.785 0.298
AdasynKNN 0.701 0.817 0.753 0.784 0.303
RUSKNN 0.720 0.805 0.807 0.806 0.304
OPTKNN 0.765 0.785 0.928 0.850 0.344
OPTSmoteKNN 0.746 0.814 0.839 0.826 0.354
OPTAdasynKNN 0.740 0.823 0.814 0.819 0.361
OPTRUSKNN 0.763 0.804 0.887 0.843 0.366
Precision,recall,andtheF -scorefollowedaconsistenttrendacrossmodels,generally
1
remaining above 0.80, while MCC exhibited greater sensitivity to model and sampling
choices. Slightdeviationswereobservedinafewconfigurations,suchastheKNNwith
ADASYN,whereprecisionreached0.785,andtheunoptimizedNaiveBayes,whererecall
droppedto0.449andF1-scoresremainedbelow0.70. Onceoptimized,however,allNaive
Bayesvariantsimprovednotably,reachingF1-scoresofapproximately0.80. Thispattern
indicatesthatevensimplemodelsbenefitfromparameteradjustmentwhentrainedon
administrativedatawithmoderateclassimbalance.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429
22of44
Table8.GaussianNaiveBayesResults.
| Pipeline            | Accuracy | Precision | Recall | F1-Score | MCC   |
| ------------------- | -------- | --------- | ------ | -------- | ----- |
| NaiveBayes          | 0.615    | 0.874     | 0.543  | 0.670    | 0.309 |
| SmoteNaiveBayes     | 0.569    | 0.892     | 0.458  | 0.605    | 0.293 |
| AdasynNaiveBayes    | 0.562    | 0.888     | 0.449  | 0.596    | 0.282 |
| RUSNaiveBayes       | 0.599    | 0.875     | 0.518  | 0.651    | 0.296 |
| OPTNaiveBayes       | 0.715    | 0.847     | 0.738  | 0.789    | 0.366 |
| OPTSmoteNaiveBayes  | 0.754    | 0.810     | 0.860  | 0.835    | 0.361 |
| OPTAdasynNaiveBayes | 0.735    | 0.827     | 0.800  | 0.813    | 0.360 |
| OPTRUSNaiveBayes    | 0.725    | 0.835     | 0.770  | 0.801    | 0.360 |
Table9.LogisticRegressionResults.
| Pipeline                    | Accuracy | Precision | Recall | F1-Score | MCC   |
| --------------------------- | -------- | --------- | ------ | -------- | ----- |
| LogisticRegression          | 0.770    | 0.792     | 0.923  | 0.853    | 0.366 |
| SmoteLogisticRegression     | 0.729    | 0.847     | 0.760  | 0.802    | 0.383 |
| AdasynLogisticRegression    | 0.729    | 0.850     | 0.757  | 0.801    | 0.387 |
| RUSLogisticRegression       | 0.753    | 0.821     | 0.841  | 0.831    | 0.376 |
| OPTLogisticRegression       | 0.770    | 0.792     | 0.922  | 0.852    | 0.364 |
| OPTSmoteLogisticRegression  | 0.752    | 0.822     | 0.837  | 0.830    | 0.377 |
| OPTAdasynLogisticRegression | 0.738    | 0.840     | 0.785  | 0.812    | 0.384 |
| OPTRUSLogisticRegression    | 0.756    | 0.820     | 0.846  | 0.833    | 0.379 |
Table10.LinearSupportVectorMachineResults.
| Pipeline           | Accuracy | Precision | Recall | F1-Score | MCC   |
| ------------------ | -------- | --------- | ------ | -------- | ----- |
| LinearSVM          | 0.775    | 0.788     | 0.939  | 0.857    | 0.374 |
| SmoteLinearSVM     | 0.727    | 0.847     | 0.758  | 0.800    | 0.380 |
| AdasynLinearSVM    | 0.729    | 0.851     | 0.756  | 0.801    | 0.388 |
| RUSLinearSVM       | 0.754    | 0.818     | 0.846  | 0.832    | 0.373 |
| OPTLinearSVM       | 0.776    | 0.789     | 0.940  | 0.858    | 0.376 |
| OPTSmoteLinearSVM  | 0.729    | 0.840     | 0.770  | 0.804    | 0.373 |
| OPTAdasynLinearSVM | 0.750    | 0.828     | 0.824  | 0.826    | 0.382 |
| OPTRUSLinearSVM    | 0.726    | 0.846     | 0.758  | 0.800    | 0.377 |
Table11.DecisionTreeResults.
| Pipeline              | Accuracy | Precision | Recall | F1-Score | MCC   |
| --------------------- | -------- | --------- | ------ | -------- | ----- |
| DecisionTree          | 0.716    | 0.804     | 0.801  | 0.802    | 0.297 |
| SmoteDecisionTree     | 0.702    | 0.818     | 0.755  | 0.785    | 0.306 |
| AdasynDecisionTree    | 0.695    | 0.811     | 0.751  | 0.780    | 0.286 |
| RUSDecisionTree       | 0.688    | 0.808     | 0.743  | 0.774    | 0.273 |
| OPTDecisionTree       | 0.764    | 0.791     | 0.913  | 0.848    | 0.351 |
| OPTSmoteDecisionTree  | 0.704    | 0.868     | 0.696  | 0.772    | 0.384 |
| OPTAdasynDecisionTree | 0.735    | 0.841     | 0.780  | 0.809    | 0.381 |
| OPTRUSDecisionTree    | 0.742    | 0.844     | 0.787  | 0.814    | 0.394 |
TheMatthewsCorrelationCoefficient(MCC)displayedhighervariabilityacrossexper-
iments,asexpectedunderclassimbalance,rangingfromapproximately0.28to0.42.Models
suchasNaiveBayesandDecisionTreeshowedthegreatestsensitivitytohyperparame-
tertuning,whiletheRandomForestandLightGBMachievedconsistentimprovements
afteroptimization. Inparticular,LightGBMachievedthehighestMCCvaluesacrossall
experiments(upto0.419),suggestingthatboostingmethodscapturenonlinearinteractions
amongfinancialandacademicfeaturesmoreeffectivelythanotheralgorithms.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429
23of44
Table12.RandomForestResults.
| Pipeline              | Accuracy | Precision | Recall | F1-Score | MCC   |
| --------------------- | -------- | --------- | ------ | -------- | ----- |
| RandomForest          | 0.741    | 0.808     | 0.840  | 0.824    | 0.337 |
| SmoteRandomForest     | 0.733    | 0.818     | 0.808  | 0.813    | 0.343 |
| AdasynRandomForest    | 0.733    | 0.821     | 0.804  | 0.813    | 0.348 |
| RUSRandomForest       | 0.720    | 0.816     | 0.788  | 0.802    | 0.323 |
| OPTRandomForest       | 0.786    | 0.802     | 0.933  | 0.863    | 0.416 |
| OPTSmoteRandomForest  | 0.770    | 0.828     | 0.859  | 0.843    | 0.412 |
| OPTAdasynRandomForest | 0.762    | 0.834     | 0.835  | 0.835    | 0.407 |
| OPTRUSRandomForest    | 0.752    | 0.844     | 0.805  | 0.824    | 0.408 |
Table13.LightGradientBoostingMachineResults.
| Pipeline          | Accuracy | Precision | Recall | F1-Score | MCC   |
| ----------------- | -------- | --------- | ------ | -------- | ----- |
| LightGBM          | 0.786    | 0.807     | 0.922  | 0.861    | 0.418 |
| SmoteLightGBM     | 0.760    | 0.825     | 0.845  | 0.835    | 0.392 |
| AdasynLightGBM    | 0.765    | 0.832     | 0.843  | 0.838    | 0.409 |
| RUSLightGBM       | 0.765    | 0.825     | 0.855  | 0.840    | 0.400 |
| OPTLightGBM       | 0.786    | 0.803     | 0.931  | 0.862    | 0.415 |
| OPTSmoteLightGBM  | 0.756    | 0.836     | 0.823  | 0.829    | 0.403 |
| OPTAdasynLightGBM | 0.758    | 0.836     | 0.826  | 0.831    | 0.405 |
| OPTRUSLightGBM    | 0.750    | 0.838     | 0.809  | 0.823    | 0.397 |
Overall, theresultsindicatethatbothlinearandensembleclassifiersachievereliable
generalization on the held-out test set using exclusively pre-declaration features. Linear
models (Logistic Regression and Linear SVM) yield stable performance with transparent
decision functions, while ensemble methods (Random Forest and LightGBM) provide a
modestgaininpredictivepower,asreflectedbytheirhigherMCCvalues. Fromanerror-
analysisstandpoint,thejointinspectionofPrecision,Recall,andMCCshowsthatcompetitive
configurations maintain a favorable trade-off between false positives and false negatives
underclassimbalance,withoutcollapsingintodegeneratemajority-classpredictions.
From an operational perspective, differences in Matthews Correlation Coefficient
(MCC)translateintomeaningfultrade-offsbetweenTypeIandTypeIIerrors,whichare
directlyrelevantforinstitutionaldecision-making.Inthepresentcontext,TypeIerrors(false
positives)correspondtoborrowersincorrectlyclassifiedascompliant,potentiallydelaying
preventive outreach, whereas Type II errors (false negatives) correspond to borrowers
incorrectly classified as non-compliant, potentially triggering unnecessary monitoring
actions. BecauseMCCjointlyaccountsforallcellsoftheconfusionmatrix,improvements
inMCCreflectamorebalancedreductionofbotherrortypes,ratherthangainsdrivenby
majority-classdominanceorasymmetricerrorminimization.
Consequently,configurationsachievinghigherMCCvalues—suchasoptimizedRan-
dom Forest and LightGBM models—offer more robust discrimination capacity under
uncertainty,supportingearlierandmoreproportionateadministrativeresponses. Impor-
tantly,thesegainsshouldnotbeinterpretedasdeterministicdecisionthresholds,butas
improvementsinriskrankingqualitythatenhancetheefficiencyoftargetedcommunication
andfollow-upstrategieswhilepreservinginstitutionaldiscretion.
ThesefindingsaddressRQ2byshowingthatsupervisedmodelscanpredictdeclara-
tionoutcomeswithconsistentperformanceusingonlypre-eventinformation. Theyalso
supportRQ3bydemonstratingthatinterpretabilitycanbepreservedunderconstrained
administrative feature spaces: linear decision functions and tree-based structures pro-
videexplicit,verifiabledecisioncriteria,whilethecross-modelstabilityofthetop-ranked
predictorsmotivatestheinterpretabilityanalysesdevelopedinthesubsequentsubsections.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 24of44
Regardingcomputationalcost,thefullexperimentaltrainingpipelinewasexecutedon
astandardcommercialoff-the-shelfworkstation(asdescribedinSection4.1)andrequired
approximatelythreedaystocomplete,includinghyperparameteroptimizationandcross-
validationacrossallevaluatedconfigurations. Oncetrained,inferenceiscomputationally
lightweight: theaveragepredictiontimeisapproximately0.002secondsperinstanceon
theheld-outtestset.
Giventhattheinstitutionaldatasetcomprisesontheorderof103 recordsperyear,
batch inference over new cohorts can be performed in negligible time on conventional
hardware,withoutimposinganyoperationalburden. Fromaninstitutionaldeployment
perspective, thisclearseparationbetweenmoderateofflinetrainingcostandnegligible
online inference cost makes the proposed framework fully feasible for routine use in
administrativesettings.
5.2. ConfusionMatrices
Figures10and11displaytheconfusionmatricescorrespondingtothebest-performing
experimentforeachmodel. Thesevisualizationsprovideamoregranularviewofhoweach
classifierdistinguishesbetweenborrowerswhosubmittedtheirfirstincomedeclaration
andthosewhodidnot.
(a)OptimizedHPKNNwithRUS (b)OptimizedHPNaiveBayes
(c)LogisticRegressionwithADASYN (d)LinearSVMwithADASYN
Figure10.ConfusionMatrices(PartI).
Overall,allmodelsexhibitastrongabilitytodifferentiatebetweenthetwoclasses,
thoughthenatureofthemisclassificationsvaries. Somemodelsshowatendencytoward
TypeIerrors(falsepositives—predictingaborrowerwilldeclarewhentheywillnot),while
othersleantowardTypeIIerrors(falsenegatives—predictingaborrowerwillnotdeclare
whentheyactuallydo).
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 25of44
(a)OptimizedHPDTwithRUS (b)OptimizedHPRandomForest
(c)BaseLightGradientBoostingMachine
Figure11.ConfusionMatrices(PartII).
TheconfusionmatricesforNaiveBayes,LogisticRegression,LinearSVM,andDe-
cision Tree reveal a predominance of Type II errors, consistent with their lower recall
valuesreportedinSection5.1. Thesemodelstendtomissaportionofactualdeclarants,
prioritizingconservativeclassificationsthatfavorthemajorityclass.
Incontrast,KNN,RandomForest,andLightGBMdisplayastrongerinclinationtoward
Type I errors, predicting more declarants than those who actually filed. Although this
behaviorslightlyreducesprecision, itpreventsseveredropsinrecallandyieldshigher
overallF1-scores. Inpracticalterms,thistrade-offisfavorableforearly-warningsystems,
asitminimizestheriskoffailingtoidentifypotentialdefaultingborrowers.
From an error-analysis perspective, the observed asymmetry between Type I and
TypeIIerrorshasdirectimplicationsformodelselectionunderuncertainty. Configurations
exhibitingamildbiastowardTypeIerrorsprioritizehigherrecallatthecostofamoderate
increaseinfalsepositives, whereasmodelsdominatedbyTypeIIerrorsachievehigher
precisionbutrisksystematicallymissingtruepositivecases. Thistrade-offisconsistent
withthemetricprofilesreportedinSection5.1,particularlythejointbehaviorofRecall,
F -score,andMCC.
1
Underaconstrainedfeaturesettingandclassimbalance,ensemblemodelssuchas
RandomForestandLightGBMexhibitamorebalancederrorstructure,avoidingextreme
concentration on either error type. Their confusion matrices show that gains in recall
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 26of44
are not achieved at the expense of severe precision degradation, which explains their
consistentlyhigherMCCvalues. Fromacomputationalstandpoint,thisbalanceindicatesa
morerobustdiscriminationcapacityacrossbothclasses,ratherthanrelianceonmajority-
classdominance.
5.3. ModelInterpretability
This section analyzes which variables most strongly drive the predictive behavior
ofthemodelsandhowtheserelationshipscanbeinterpretedtoprovidetransparentand
verifiableexplanationsofmodelpredictions. Beyondsupportingtransparency,thisinter-
pretabilitylayeralsoplaysakeyroleinidentifyingandmonitoringpotentialsocioeconomic
biases present in the underlying administrative data. By making feature contributions,
splitthresholds,anddecisionrulesexplicit,theproposedapproachallowsinstitutional
analysts to detect patterns that may disproportionately affect specific groups, enabling
informedoversightandperiodicreview. Importantly,interpretabilityisnotpresentedas
abias-mitigationmechanismperse,butasadiagnostictooltosupportresponsibleuse,
humanjudgment,andthedesignofcomplementarygovernanceorcorrectivestrategies
whenneeded.
Section 5.3.1 reports the average permutation feature importance (PFI) across all
trainedmodels,providingaglobalviewofvariablerelevance. Section5.3.2presentsthetop
fifteenmodel-wiseimportancesforthebest-performingexperimentofeachinterpretable
model,highlightingdifferencesbetweenlinearandtree-basedalgorithms.
Tocomplementtheseaggregateanalyses,Section5.3.3illustratesdecisionpathsex-
tractedfromtheoptimizedDecisionTree(OPTRUSDecisionTree)atmultipledepths,show-
inghowmodelstructurecanbetranslatedintohuman-readablerules. Finally,Section5.3.4
introducesSHAPvaluevisualizations,whichquantifytheindividualcontributionofeach
featuretospecificpredictions,enhancingtransparencyandcase-levelexplainability.
5.3.1. PermutationFeatureImportanceResults
Figure12showstheaveragedPFIcomputedforeverymodel. Toreducetheeffectof
randomshuffling,theprocedurewasrepeatedthirty-onetimespermodelandtheresults
wereaveraged.
Two features stand out clearly: deud_monto (total loan amount) and conteo_matr
(total number of enrollments). They are followed by estado_civil (marital status) and
anio_exigibilidad(yearofenforceability). Theconsistentprominenceofthesefourvariables
acrossmodelsindicatesthatfinancialexposure,academictrajectory,andbasicdemograph-
icsjointlyexplainmostofthepredictivesignal.
Theremainingvariablescontributeprogressivelyless. Mostfacultydummieshave
limitedimpact,withthenotableexceptionoftheindicatorcorrespondingtotheFACULTY
OFLAW(seeTable14),whichranksamongthetopfeaturesandsuggestsprogram-specific
differences in declaration behavior. This result indicates that representing academic
affiliationatthefacultylevelprovidessufficientandstableinformationtocaptureprogram-
leveltrends,allowingnewlyintroducedacademicprogramstobeaccommodatedthrough
theirfacultyassignmentwithoutalteringthemodelstructure.
At the lower end of the chart, some features exhibit slightly negative average PFI
values. Giventheirverysmallmagnitudeandtheknownsensitivityofpermutationto
samplingnoiseandcollinearity,thesevaluesdonotbythemselvesjustifyfeatureremoval.
Whileaformalfeatureablationstudywasnotconducted,thepermutationfeature
importanceanalysisprovidesanindirectindicationofmodelsensitivitytoreducedfeature
availability.Acrossallevaluatedmodels,predictiveperformanceislargelydrivenbyasmall
subsetofhighlyinfluentialfeatures,whereasthepermutationofremainingvariablesresults
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 27of44
innegligiblechangesinperformance. Thissuggeststhatthelearneddecisionstructureis
notcriticallydependentonalargenumberofmarginalfeatures. However,itshouldbe
notedthatpermutationimportancereflectssensitivitytoinformationdegradationrather
thanactualfeatureremoval;asystematicretraining-basedablationanalysisisthereforeleft
asfuturework.
Figure12.AveragePermutationFeatureImportanceofallModels.
Table14.FacultyDummyFeatureValues.
DummyFeature RealValue
0 EcclesiasticalFacultyofTheology
1 FacultyofSciences
2 FacultyofPhilosophyandEducation
3 FacultyofEconomicandAdministrativeSciences
4 FacultyofEngineering
5 FacultyofMarineandGeographicalSciences
6 FacultyofAgronomicandFoodSciences
7 FacultyofLaw
8 FacultyofArchitectureandUrbanism
5.3.2. Model-WiseFeatureImportance
Figure13showsthefeatureimportancesforthebestexperimentsofthelinearmodels,
whileFigure14reportstheimportancesforthebesttree-basedmodels.
For the linear models, the coefficient-based importances in Figure 13 show that es-
tado_civil(maritalstatus)dominatesthedecisionboundariesinbothLogisticRegression
andLinearSVMs,reflectingitsstrongmarginaleffectunderthestandardizedfeaturespace.
IntheLogisticRegressionmodel,academicandinstitutionalvariablessuchasfacultad_7
(FacultyofLaw),theSTEMindicator,andseveralanio_ult_matrdummiesarealsoinflu-
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 28of44
ential, suggesting that the academic program and enrollment history contribute to the
likelihoodoftimelydeclaration.Incontrast,theLinearSVMassignshigherrelativeweights
torecentenrollmentyears(anio_ult_matr_2011,2015,and2020)andtothetotaldebtamount
(deud_monto),capturingtheimpactofbothtemporalandfinancialdimensions. Thesediffer-
encesareexpected,sincepermutationimportanceevaluatesoverallpredictivedependence,
whereaslinearcoefficientsreflectlocalmarginaleffectsconditionedonfeaturescaling.
(a)LogisticRegressionWithADASYNFeatureImportance
(b)LinearSVMwithADASYNFeatureImportance
Figure13.LinearModelsFeatureImportance.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 29of44
(a)OptimizedHPDTwithRandomUndersamplingofFeature
Importance
(b)OptimizedHPRandomForestFeatureImportance
(c)BaseLightGradientBoostingMachineFeatureImportance
Figure14.Tree-BasedModelsforFeatureImportance.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 30of44
For the tree-based models (Figure 14), the feature importance rankings are broadly
consistentacrosstheDecisionTree,RandomForest,andLightGBM.Inallthreecases,thesame
dominantpredictorsidentifiedbypermutationimportancedefinethecorepredictivestructure.
TheDecisionTreemodelassignsthegreatestweighttoconteo_matr,followedclosely
by estado_civil and deud_monto, indicating that a single borrower’s academic trajectory
and financial exposure are key splitting criteria. Random Forest and LightGBM rein-
force this pattern but invert the top two variables—deud_monto slightly surpasses con-
teo_matr—highlighting that ensemble averaging emphasizes financial magnitude over
enrollmentfrequency. Theconsistentpresenceofanio_exigibilidadamongthetopfeatures
acrossallthreemodelsunderscorestheimportanceoftherepaymenttimelineindistin-
guishingbetweendeclaringandnon-declaringborrowers.
Lower-rankedvariables,suchasfacultadindicatorsandSTEMaffiliation,contribute
marginallytomodelperformance,offeringlimitedincrementalinformationoncethemain
financialandacademicvariablesareincluded. Thisstabilityofrankingsacrossindepen-
denttree-basedarchitecturessuggeststhatthepredictivesignalisdominatedbyasmall,
interpretablesubsetoffeaturesdirectlylinkedtoborrowerbehaviorandloanstructure.
Fromapredictiveandinterpretabilitystandpoint,theseresultsalignwiththeperfor-
manceanalysis. Variablesrelatedtodebtmagnitudeandacademictrajectoryconsistently
carry the strongest explanatory weight across models, indicating that a small subset of
administrative features concentrates most of the discriminative signal. This concentra-
tionsupportsstableinterpretationunderuncertainty,asthesamevariablesgovernboth
predictiveaccuracyandexplanatorystructure.
5.3.3. DecisionTreeSnapshotsatDifferentDepths
Toillustratehowmodelstructuresupportsdecision-making,Figures15–17display
thesameDecisionTreetrainedunderoneofthebest-performingconfigurations,namely
theOptimizedRandomunder-samplingDecisionTree(OPTRUSDecisionTree)described
inSection5.1,andvisualizedatthreedifferentdepths(d = 4,d = 5,andd = 11). These
visualizationsareintendedasillustrativeartifactsratherthanasobjectsofexhaustivenode-
by-nodeinspection. Theshallowrepresentations(d =4andd =5)highlightasmallsetof
high-yieldsplitsthatcanbereadilyexamined,whereasthedeepertree(d =11)introduces
finer partitions that capture niche interactions at the cost of interpretability, exemplify-
inghowstructuralcomplexityrapidlylimitsdirecthumaninspectioninadministrative
predictionsettings.
Fromaninstitutionalperspective,thedecisiontreestructureenablestheextraction
ofexplicitandauditabledecisionrulesthatcanbeinterpretedasearly-warningsignals
ratherthandeterministicprescriptions. Splitthresholdsandbranchconditionsidentify
combinationsofadministrativeandacademicattributesthataresystematicallyassociated
withelevatedriskofnon-submission. Whenusedwithappropriatecaution,theserules
can inform high-level monitoring criteria or screening heuristics to prioritize outreach,
communication,orfollow-upactionswhileavoidingautomatedenforcementorexclusion.
Importantly, these rule-based patterns are intended to support human oversight and
contextualjudgment,nottoreplaceinstitutionaldecision-makingprocesses.
Atd =4,thetreetypicallyplacesestado_civil,anio_exigibilidadandfacultad_4among
thefirstsplits,followedbyconteo_matranddeud_monto. Thesenodesyieldcompactrules
withbroadcoverage. Forexample,aSingledebtor,alowloanamount,combinedwithlow
enrollments,mayincreasetheprobabilityofnotsubmittingthefirstincomedeclaration.
Suchrulesareeasytooperationalizeas“portfoliofilters”forearlyoutreach.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429
31of44
eslaF
012 = selpmas ]012 ,0[= eulav seralceD = ssalc
0.0 = inig
| 5.1 ≤ datlucaf  936 = selpmas ]536 ,4[= eulav seralceD = ssalc | seralceD = ssalc            |     |     |
| -------------------------------------------------------------- | --------------------------- | --- | --- |
| 210.0 = inig                                                   | 15 = selpmas ]84 ,3[= eulav |     |     |
111.0 = inig
| 5.8102 ≤ dadilibigxe_oina | eslaF |     |     |
| ------------------------- | ----- | --- | --- |
 924 = selpmas ]524 ,4[= eulav seralceD = ssalc
81.0 = inig
eslaF
eslaF
5.5102 ≤ dadilibigxe_oina
eurT
|     | 873 = selpmas ]773 ,1[= eulav seralceD = ssalc |  862 = selpmas ]862 ,0[= eulav seralceD = ssalc | 011 = selpmas ]901 ,1[= eulav seralceD = ssalc |
| --- | ---------------------------------------------- | ----------------------------------------------- | ---------------------------------------------- |
|     | eurT 500.0 = inig                              | 810.0 = inig                                    |                                                |
0.0 = inig
]0004 ,5292[= eulav
5.1≤ livic_odatse
4296 = selpmas seralceD = ssalc
| 884.0 = inig | eurT |     |     |
| ------------ | ---- | --- | --- |
eslaF
|     | ]0611 ,3311[= eulav                               | ]1701 ,4011[= eulav deralceD reveN = ssalc 406.0 ≤ otnom_dued |                    |
| --- | ------------------------------------------------- | ------------------------------------------------------------- | ------------------ |
|     | 5.0 ≤ 7_datlucaf  3922 = selpmas seralceD = ssalc |  5712 = selpmas                                               | seralceD = ssalc   |
|     |                                                   | 5.0 ≤ mets                                                    |  = selpmas         |
|     | 5.0 = inig                                        | 5.0 = inig                                                    |  = inig ],[= eulav |
eslaF
| 696.0− ≤ rtam_oetnoc deralceD reveN = ssalc |     |     |     |
| ------------------------------------------- | --- | --- | --- |
]0421 ,4641[= eulav
4072 = selpmas
794.0 = inig
eurT
eslaF
5.0202 ≤ dadilibigxe_oina
|       | 874.0− ≤ otnom_dued deralceD reveN = ssalc | deralceD reveN = ssalc 464.1− ≤ rtam_oetnoc | deralceD reeN = ssalc        |
| ----- | ------------------------------------------ | ------------------------------------------- | ---------------------------- |
| eurT  | ]08 ,133[= eulav                           | ]15 ,282[= eulav                            |                              |
| eslaF | 114 = selpmas                              | 333 = selpmas                               | 87 = selpmas ]92 ,94[= eulav |
|       | 413.0 = inig                               | 952.0 = inig                                | 764.0 = inig                 |
eurT
5.8102 ≤ dadilibigixe_oina
]5633 ,1292[= eulav
eurT
| 6825 = selpmas seralceD = ssalc |     | eslaF |     |
| ------------------------------- | --- | ----- | --- |
894.0 = inig
5.0 ≤ 1102_rtam_tlu_oina
|     | 137.0− ≤ otnom_adued            | 501.1− ≤ otnom_dued deralceD reveN = ssalc |                                 |
| --- | ------------------------------- | ------------------------------------------ | ------------------------------- |
|     | ]8491 ,448[= eulav              |                                            | ]4361 ,254[= eulav              |
|     | 2972 = selpmas seralceD = ssalc | ]413 ,293[= eulav                          | 6802 = selpmas seralceD = ssalc |
|     | 224.0 = inig                    | 494.0 = inig 607 = selpmas                 | 933.0 = inig                    |
eslaF
259.0− ≤ rtam_oetnoc
]5212 ,7541[= eulav
| eurT 2853 = selpmas seralceD = ssalc |     |     |     |
| ------------------------------------ | --- | --- | --- |
384.0 = inig
eurT
eslaF
|     | 5.2102 ≤ rtam_tlu_oina deralceD reveN = ssalc | 464.1 ≤ rtam_oetnoc deralceD reveN = ssalc | deralceD reveN = ssalc         |
| --- | --------------------------------------------- | ------------------------------------------ | ------------------------------ |
|     | ]771 ,316[= eulav                             | ]361 ,005[= eulav                          |                                |
|     | 097 = selpmas                                 | 366 = selpmas                              | 721 = selpmas ]41 ,311[= eulav |
|     | eurT 843.0 = inig                             | 173.0 = inig 691.0 = inig                  |                                |
eurT
Figure 15. Decision Tree Snapshot of Model OPTRUSDecisionTree at Depth = 4. Blue (orange)
nodesindicatehigherassociationwithdeclaration(non-declaration),withcolorintensityreflecting
nodepurity.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 32of44
Figure16.DecisionTreeSnapshotofModelOPTRUSDecisionTreeatDepth=5.Blue(orange)nodes
indicatehigherassociationwithdeclaration(non-declaration),withcolorintensityreflectingnode
purity;boxes(“...”)denotetruncatedbranchesbeyondtheselectedtreedepth.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 33of44
Figure17.DecisionTreeSnapshotofModelOPTRUSDecisionTreeatDepth=11.Blue(orange)nodes
indicatehigherassociationwithdeclaration(non-declaration),withcolorintensityreflectingnode
purity.boxes(“...”)denotetruncatedbranchesbeyondtheselectedtreedepth.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 34of44
At d = 5, the model refines these segments, introducing thresholds that separate
borderline cases (for instance, specific ranges in deud_monto, faculties (facultad_X), or
if the undergraduate program is a STEM program (stem)). This level balances fidelity
andinterpretability.
Atincreasingdepths,theDecisionTreeexposesprogressivelyfiner-grainedinterac-
tions among features. While deeper representations (d = 11) may improve local fit by
capturinghigher-ordercombinations,theyalsoreducetransparencyandincreasesensitiv-
itytosamplingvariability. Incontrast,shallowertrees(d =4andd =5)emphasizeasmall
setofhigh-yieldsplitsthatyieldcompactandstabledecisionrules. Fromaninterpretability
standpoint,theseshallowstructuresprovideafavorablebalancebetweenexpressivepower
andhumanverifiability, makingthemsuitableforanalyticalinspectionandrule-based
reasoningunderuncertainty.
Thesestructuralobservationsareconsistentwiththeglobalandmodel-wiseimpor-
tanceanalyses: thefirst-levelsplitssystematicallyinvolvethesamedominantvariables
(estado_civil,deud_monto,conteo_matr,andanio_exigibilidad)identifiedbypermutationim-
portanceandensemble-basedrankings. Thisalignmentindicatesthatthelearneddecision
pathsarenotartifactsofmodeldepth,butratherreflectstablepredictivesignalspresent
intherestrictedadministrativefeaturespace. Consequently,theextractedrulesprovide
explicit,auditableexplanationsofindividualpredictions,reinforcingtheinterpretability
claimsexaminedinrelationtoRQ3.
To illustrate the internal reasoning of the chosen model, Table 15 summarizes one
representativedecisionpathextractedfromthetreewithdepthd = 4. Thispathshows
howaborrower’scharacteristicssequentiallyleadthemodeltopredictahigherprobability
ofnotsubmittingthefirstincomedeclaration.
Table15.ExampledecisionpathfromtheoptimizedDecisionTree(depth=4).
ObservedValue SplitCondition FeatureMeaning BranchTaken
Borrowerissingleorwithout
1 estado_civil≤1.5 True(leftbranch)
dependents
2019 anio_exigibilidad≤2018.5 Loanenforceabilityyear(2019) False(rightbranch)
Totalnumberofenrollments
−0.5 conteo_matr≤ −0.696 True(leftbranch)
(standardized)
Totaldebtamount
−0.4 deud_monto≤ −0.478 True(leftbranch)
(standardized)
2019 anio_exigibilidad≤2020.5 Loanenforceabilityyear(2021) Endbranch
Predictedclass: NeverDeclared(estimatedprobability≈0.85,282casesofnodeclarationover333totalinthisnode)
Thispathillustratesaborrowerwhosemaritalstatuscorrespondstoasingleindividual
(estado_civil=1),withaloanenforceablein2019andbelow-averageacademicenrollments
(conteo_matrstandardizedvalue=−0.5). Themodelfirstfollowstheleftbranchforsingle
borrowers,thentherightbranchforrecentenforceabilityyears,andsubsequentlytheleft
branchesforbothlowenrollmentcountandbelow-averagedebt(deud_monto=−0.4).
The resulting classification, Never Declared, arises from the combination of limited
academic continuity (fewer than average enrollments) and less-than-average financial
exposure(atotalamountofdebtbelowtheaverage).Theprobabilityrelatedtotheoutcome
ofthemodel, inthiscase85%correspondstotheclassproportionattheterminalnode
reachedbythispath. Thisvaluecorrespondstotheempiricalclassfrequencyobservedat
theleafnodeanddoesnotrepresentacalibratedposteriorprobability.
Thisexampleshowshowthedecisiontreestructureenablesatransparent,rule-based
explanation of predictions: each split represents a human-interpretable condition that
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 35of44
linksadministrativeattributestobehavioraloutcomes. Suchexplicitreasoningenables
predictionstobetraced,verified,andanalyticallyjustifiedthroughasequenceofhuman-
interpretableconditionsdefinedonobservedfeatures.
5.3.4. ShapValuesforLightGradientBoostingMachine
Figure18showstheSHAPvaluedistributionforallfeaturesintheBaseLightGradient
BoostingMachine(LGBM)model. TheTreeExplainermethodfromtheSHAPlibrarywas
applied,asitprovidesaccuratelocalattributionsforensemble-basedalgorithms.Eachpoint
representsasingleobservation: itspositionalongthex-axisindicatesthemagnitudeand
directionofitscontributiontothemodeloutput,whilethecolorencodestheoriginalfeature
value(blueforlowandredforhigh). Pointsdistributedfartherfromzerocorrespondto
strongerimpactsonthefinalprediction.
Figure18.SHAPValuesforLGBM.
TheSHAPsummaryplotrevealspatternsconsistentwiththepermutationandtree-
basedfeatureimportanceanalyses(Figures12and14).Thedominantvariables—deud_monto
(loan amount), conteo_matr (number of enrollments), estado_civil (marital status), and
anio_exigibilidad(loanenforceabilityyear)—exhibitthelargestSHAPmagnitudes. These
featuresdrivethemodel’spredictionsininterpretabledirections: highdeud_monto,high
conteo_matr,andhigherestado_civilcodes(marriedborrowers)tendtopushpredictions
towardtheDeclaresclass,whileolderanio_exigibilidadvalues(earlierrepaymentyears)shift
thepredictiontowardNeverDeclared.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 36of44
Featuresrelatedtoacademicprograms(facultydummiesandtheSTEMindicator)
show minimal dispersion around zero, confirming their marginal influence on model
decisions. Notably,thedummyvariablecorrespondingtotheFacultyofLaw(facultad_7)
displays a slightly asymmetric distribution, suggesting a weak but consistent positive
contributiontodeclarationprobability.
Thesepatternsindicatethatmaritalstatusexertsamoderatebutconsistentinfluence
on declaration behavior, with married or partnered borrowers showing slightly higher
compliance. Financialexposurealsoplaysacentralrole: largerloanamountsareassoci-
atedwithhigherdeclarationprobability,whereassmallerdebtscorrespondtoincreased
non-declarationrisk. Academiccontinuityfurthercontributestothemodeloutput,asa
lower number of enrollments (conteo_matr) is systematically linked to reduced declara-
tionlikelihood. Temporaleffectsarepresentbutweaker,withearlierenforceabilityyears
(anio_exigibilidad)marginallyincreasingtheprobabilityofdeclaration. Finally,program-
relatedvariablessuchasfacultyaffiliationexhibitonlysecondaryeffects,withtheFaculty
ofLawshowingasmallbutconsistentpositivecontributionrelativetootherfaculties.
Overall,theSHAPanalysiscomplementstheglobalandmodel-wiseinterpretability
results by providing instance-level attributions that are consistent with the previously
identifiedfeaturerankings. Theagreementbetweenpermutationimportance,tree-based
importances,andSHAPvaluedistributionsindicatesthatthecontributionofthedominant
predictorsisstableacrossexplanationparadigmsandmodelfamilies.
Fromaformalinterpretabilityperspective,SHAPvaluesofferalocallyadditivede-
composition of the model output, enabling each prediction to be expressed as a sum
of feature-level contributions relative to a baseline expectation. This property ensures
traceabilityandinternalcoherenceofexplanations,eveninensemble-basedmodelswith
complexnonlineardecisionfunctions. Undertherestrictiontopre-declarationadminis-
trative features, such locally consistent explanations allow predictions to be examined,
compared,andvalidatedwithoutrelianceonlatentorpost-eventinformation.
Taken together, the stability of feature rankings, the availability of explicit decision
rulesintree-basedmodels,andthelocallyfaithfulexplanationsprovidedbySHAPjointly
addressRQ3.Theydemonstratethatreliableinterpretabilitycanbeachievedinsupervised
classificationtasksoperatingonconstrainedinstitutionaldatasets,supportingtransparent
reasoningaboutpredictionsunderuncertaintyratherthanopaquescore-basedclassification.
5.3.5. ConsistencyandComplementarityAcrossInterpretationLayers
Theinterpretabilityframeworkadoptedinthisstudyintegratesglobal(permutation
featureimportance),structural(decisionpaths),andlocal(SHAP)explanationmethods,
eachaddressingadistinctaspectofmodelbehavior. Theseapproachesarenotexpectedto
yieldidenticalexplanations,astheyoperateatdifferentanalyticallevelsandrespondto
differentinterpretativequestions.
Globalexplanationsidentifyvariablesthatexertconsistentinfluenceacrossthebor-
rowerpopulation,structuralexplanationsrevealhowsuchvariablesarecombinedwithin
the internal decision logic of the models, and local explanations provide instance-level
attributionsforindividualpredictions. Apparentdiscrepanciesbetweenexplanationlayers
arethereforenottreatedasmethodologicalinconsistencies,butratherascomplementary
perspectivesthatjointlycharacterizepredictivebehavior.
From an institutional perspective, this layered interpretability strategy supports
decision-making at multiple levels. Global explanations inform strategic prioritization
and policy-level resource allocation, structural explanations enhance transparency and
auditability of decision rules, and local explanations enable case-by-case review when
targetedmonitoringorpreventiveactionsareconsidered. Ratherthanresolvingdisagree-
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 37of44
mentsbyprivilegingasingleinterpretabilitymethod,theproposedframeworkemphasizes
triangulationacrossexplanationlayerstoensurerobust,interpretable,andcontext-aware
decisionsupport.
5.4. Rule-BasedThresholdBaselineComparison
Tocontextualizetheperformancegainsachievedbythemachinelearningmodels,a
simplerule-basedbaselinewasimplementedusingthresholdrulesondebtamountand
enrollment count, which were consistently identified as the most influential numerical
features across the interpretability analyses (Sections 5.3.2–5.3.4). High-risk cases were
definedasthoseexceedingthefourthquartileofeachrespectivedistribution.
As reported in Table 16, this baseline exhibits high precision but very low recall,
resulting in poor overall performance, as reflected by low F1-score and MCC values.
This behavior indicates that the rule-based approach captures only a small subset of
extreme-riskborrowerswhilefailingtoidentifyalargeproportionofnon-compliantcases.
Thecorrespondingconfusionmatrix(Figure19)confirmsthispattern,showingalimited
numberoftruepositivesalongsideasubstantialnumberoffalsenegatives.
Incontrast,theLightGradientBoostingMachineachievessubstantiallyhigherand
morebalancedperformance(e.g.,F1=0.861andMCC=0.418;seeTable13),demonstrating
itsabilitytoexploitmultivariateandnon-linearrelationshipsbeyondsimplethreshold
rules. These results highlight the limitations of practical rule-based heuristics and un-
derscoretheaddedvalueofmachinelearningmodelsforearlyriskidentificationinthis
institutionalcontext.
Table16.AppliedPracticalThresholdMetrics.
Pipeline Accuracy Precision Recall F1-Score MCC
PracticalThreshold 0.385 0.876 0.172 0.288 0.141
Figure19.Confusionmatrixfortherule-basedthresholdbaseline.
6. Discussion
Thefindingsofthisworkismethodologicalandinstitutionalratherthanalgorithmic.
Thefindingsshouldbereadasevidenceaboutwhatcanbeachievedwithestablishedmod-
elswhentheproblemisformulatedunderrealisticadministrativeconstraints,evaluated
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 38of44
with imbalance-appropriate metrics, and accompanied by interpretability mechanisms
designedforauditability. Accordingly,themanuscriptdoesnotclaimnewlearningtheory
ornewimbalance-handlingmethods,butprovidesadefensibleblueprintfordeploying
predictivedecisionsupportincomparableadministrativecompliancesettings.
Giventhebreadthofevaluatedconfigurations,theinterpretationinthissectionem-
phasizescross-modelpatternsandrelativeperformancetiersratherthanisolatednumerical
differences. Whilefullmetrictablesareretainedfortransparencyandcompleteness,the
discussionfocusesonaggregatedtrends—suchasthecomparativebehavioroflinearversus
ensemblemodels,theeffectofoptimizationandsamplingstrategies,andthestabilityof
MCCacrossconfigurations—whereadditionalnumericaldetaildoesnotyieldproportional
interpretivevalue.
Thisaggregationstrategyavoidsoveremphasisonmarginalmetricfluctuationsand
alignstheanalysiswiththestudy’sappliedobjective: assessingwhetheradministratively
deployablemodelsachievereliable,interpretable,andoperationallymeaningfulperfor-
manceunderrealisticdataconstraints.
6.1. ModelPerformanceandInterpretability
Althoughnon-submissionofthefirstincomedeclarationmay,ingeneral,reflecthet-
erogeneousbehavioralconditions, thepresentstudyconsidersthisoutcomewithinthe
specific institutional context of the FSCU system. The obligation to submit the declara-
tioniscontractuallyestablished, becomesenforceableafteradefinedgraceperiod, and
issupportedbysystematicinformationalandremindermechanisms. Accordingly,first-
timenon-submissionisinterpretedasanearlymanifestationofnon-compliancewithin
afullyinformedcontractualframework,ratherthanasaconsequenceoflackofaware-
ness. While individual circumstances may differ, such distinctions cannot be reliably
inferredfrompre-declarationadministrativedataalone. Consequently,theinterpretability
analyses presented in this study should be understood as identifying correlates of ele-
vatedearlynon-compliancerisk,ratherthanascausalexplanationsofdistinctunderlying
behavioralmechanisms.
Acrossallexperiments,mostalgorithmsachievedstrongandstablepredictiveper-
formance. Linearmodels,particularlyLogisticRegressionandtheLinearSupportVector
Machine, consistently achieved F1-scores above 0.85 and Matthews Correlation Coeffi-
cients(MCC)near0.37,indicatingbalancedperformancebetweenthetwoclassesdespite
a moderate imbalance in the dataset. Tree-based ensemble methods, such as Random
ForestandLightGBM,achievedslightlyhigherMCCvalues(around0.41–0.42),suggest-
ingthatnon-linearrelationshipsexistbetweenborrowercharacteristicsandrepayment
behavior. However, the gap in performance between ensemble and linear models was
narrow,reflectingthattheunderlyingpatternscanbecapturedeffectivelywithoutcomplex
architectures. Thisconsistencyacrossalgorithmsindicatesthatadministrativedatacontain
astrongandstablesignalthatcanbemodeledreliablythroughinterpretableapproaches
underconstrainedfeaturespaces andthatassessingclassificationqualitythroughMCC,
whichisparticularlyappropriateinimbalancedsettingsbecauseitaccountsforallcells
of the confusion matrix, supports more reliable identification and prioritization of bor-
rowersatelevatednon-compliancerisk. Inoperationalterms,thiscaninformearlierand
moretargetedoutreach(e.g.,remindersandguidance)andamoreefficientallocationof
administrativefollow-upresources,withouttreatingthemodeloutputasadeterministic
decisionrule.
The confusion matrix analysis confirmed these trends: linear models favored con-
servativeclassificationswithhigherprecisionbutlowerrecall(TypeIIerrors),whereas
ensemblemethodsofferedmorebalancedresults,slightlyincreasingfalsepositives(TypeI
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 39of44
errors)toimproverecallfornon-declarants. Hyperparametertuningproducedmarginal
yetconsistentimprovementsacrossallmodels,whileRandomUnderSamplingoftenen-
hancedminority-classrecallwithoutsubstantialaccuracyloss. Syntheticoversampling
methods(SMOTEandADASYN)achievedsimilareffects,marginallyimprovingprecision
insomeconfigurations.
Interpretability analyses further strengthened the robustness and transparency of
theseresults. Permutationfeatureimportanceandmodel-specificcoefficientsconsistently
highlighted financial and academic variables—particularly total debt (deud_monto), en-
rollment count (conteo_matr), marital status (estado_civil), and loan enforceability year
(anio_exigibilidad)—asthemaindeterminantsoffirst-declarationbehavior.Thedecision-tree
visualizationsprovidedconcreterule-basedexplanations,showinghowthesevariables
interacttoformdecisionpaths(e.g.,combinationsofhighdebtandlimitedenrollmentpre-
dictingnon-declaration). Complementarily,SHAPvalueanalysisquantifiedeachfeature’s
contributiontoindividualpredictions,confirmingthathigherdebtlevelsandcontinuous
enrollmentincreasetheprobabilityofcompliance,whereasmorerecentenforceabilityyears
andsinglemaritalstatusleantowardnon-declaration.
Itshouldbenotedthattheseinterpretabilitytechniquesdonotaddressidenticalex-
planatory questions and may therefore yield partially divergent insights. Permutation
FeatureImportance(PFI)capturesglobalsensitivitybymeasuringperformancedegrada-
tionunderfeatureperturbation,whereasSHAPvaluesprovideconditional,instance-level
attributions,anddecisiontreesoffersimplifiedstructuralapproximationsoflearnedre-
lationships. As a result, discrepancies between global rankings and local explanations
are expected and should be interpreted as complementary perspectives rather than as
methodologicalcontradictions.
Together,theseinterpretabilitylayers—global(PFI),structural(treepaths),andlocal
(SHAP)—provideacomprehensiveunderstandingofmodelbehavior. Theyensurethat
predictions can be traced, analytically justified, and examined across multiple levels of
abstraction, reinforcing the reliability of supervised learning models operating under
constrainedadministrativefeaturespaces.
Atthesametime,theinterpretabilityofensemblemodelsshouldbeunderstoodasme-
diatedratherthanintrinsic.Whilepost-hocexplanationtoolsenableanalyticalinspectionof
modelbehavior,ensemblemethodssuchasRandomForestsandgradientboostingdonot
yieldtransparentdecisionrulesinastrictsense. Accordingly,theexplanationspresented
inthisstudyshouldbeviewedasaudit-orientedapproximationsthatsupportdiagnostic
reasoningandinstitutionalscrutiny,ratherthanasfullytransparentrepresentationsofthe
underlyingdecisionlogic.
Atthecurrentstage,noinstitution-specificdecisionthresholdisdefinedfortranslating
predictedriskscoresintoautomaticactions. Thisreflectsthefactthat,withintheFSCU
system, formalized risk tolerance criteria and cost-sensitive decision policies have not
yet been established. Consequently, the proposed models are conceived as an initial
screeningandmonitoringtool,providingcontinuousriskindicatorsratherthanbinary
decision triggers. These outputs are intended to support early identification, targeted
communication,andpreventivefollow-upstrategies,leavingfinaldecisionstoinstitutional
judgment. Thedefinitionofoptimizedthresholdsalignedwithexplicitinstitutionalrisk
preferencesisthereforeidentifiedasanaturalextensionofthiswork,oncesuchpoliciesare
formallyspecified.
Fromanoperationalstandpoint,theinterpretabilityframeworkisintendedtosupport
institutionalprocessesratherthanindividual-leveladjudication. Forexample,aborrower
characterizedbyhighoutstandingdebt,limitedenrollmenthistory,andarecentenforce-
abilityyearmaybeflaggedaspresentingelevatedearlynon-compliancerisk. Insuchcases,
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 40of44
interpretabilityoutputscanguidetargetedcommunication,administrativefollow-up,or
preventiveguidance,withoutbeingusedasdeterministicorpunitivedecisionrules.
6.2. ImplicationsforPredictiveModelingUnderAdministrativeConstraints
Thisstudyillustrateshowsupervisedlearningmodelstrainedonroutinelycollected
administrativedatacananticipateborrowerdeclarationbehaviorunderinformationcon-
straints. Fromamodelingperspective,theresultsdemonstratethatpre-eventacademic
andfinancialvariablescontainsufficientsignaltosupportreliablebinaryclassification,
eveninthepresenceofmoderateclassimbalance.
Thecombinationofpredictiveperformanceandinterpretabilityindicatesthatcomplex
behavioral outcomes can be approximated using transparent decision structures. Rule-
basedpathsextractedfromdecisiontreesandlocallyadditiveSHAPexplanationsallow
predictionstobedecomposedintoverifiablefeaturecontributions,facilitatinganalytical
scrutinyratherthanopaquescoreassignment.
More broadly, the proposed framework exemplifies how predictive modeling can
beintegratedintoadministrativedataenvironmentswithoutrelianceonlatentvariables
or post-event information. This characteristic supports transferability to other income-
contingentloansystemsorinstitutionaldatasetswithsimilarstructurallimitations,where
explainabilityandtraceabilityareascriticalaspredictiveaccuracy.
Thegeneralizabilityofthesefindingsshouldbeinterpretedwithappropriatescope.
Severalelementsoftheresultsareinherentlycontext-specific,includingtheexactdistri-
bution of declaration outcomes, the magnitude of predictive performance metrics, the
relativeimportanceofindividualfeatures,andtheabsenceofinstitutionallydefineddeci-
sionthresholds. Theseaspectsreflecttheregulatoryframework,borrowerpopulation,and
administrativepracticesoftheFSCUsystematthePUCV,andshouldnotbeassumedto
transferdirectlytootherinstitutionsorfundingschemes.
Incontrast,themethodologicalstructureoftheproposedframeworkispotentially
transferableacrossadministrativecompliancecontexts. Specifically,thepre-eventformula-
tionofthepredictivetaskunderinformationalconstraints,theuseofaunifiedandleakage-
awarevalidationprotocol,theprioritizationofimbalance-appropriateevaluationmetrics
suchastheMatthewsCorrelationCoefficient,andthepositioningofinterpretabilitymech-
anismsasaudit-orienteddecisionsupporttoolsareapplicabletootherincome-contingent
loansystemsandregulatedadministrativedomainswhereoutcomesaredelayedandclass
imbalanceisstructural.
6.3. Limitations
Severallimitationsshouldbeacknowledged. First,thestudyisconstrainedbythe
scope and structure of the available administrative data, which, while comprehensive,
excludecertainsocioeconomicvariablesthatcouldfurtherexplainborrowerbehavior(e.g.,
employmenttypeorhouseholdcomposition). Second,theanalysisfocusesexclusivelyon
first-declarationoutcomes;subsequentdeclarationsandlong-termrepaymentbehavior
remainoutsidethescopeofthepresentstudy. Extendingtheframeworktoalongitudi-
nalsettingwouldallowtheidentificationofrecurrentnon-compliancepatternsandthe
assessmentofpersistenceincompliancebehaviorovertime.
Another limitation concerns generalizability. The data and administrative context
correspond to a single higher education institution. Although the proposed modeling
frameworkistransferable,predictiveperformanceandfeaturerelevancemayvaryacross
universitieswithdifferentborrowerprofiles,regulatoryenvironments,orcollectionprac-
tices. Futureresearchshouldvalidatetheapproachusingmulti-institutionaldata,particu-
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 41of44
larlywithintheCRUCHnetwork,toassessexternalvalidityandsupportthedevelopment
ofstandardizedpredictivetoolsforincome-contingentstudentloanmanagementinChile.
Finally, although models are trained on data pooled across multiple cohorts and
enforceabilityperiods,thepresentstudyadoptsacross-sectionalpredictiveperspective
ratherthanatime-awarelongitudinalone. Potentialtemporaldriftarisingfromregula-
tory changes, labour-market conditions, or evolving institutional practices is therefore
acknowledgedbutnotexplicitlymodelled. Thislimitationalsoconstrainsthefeasibility
of time-aware validation strategies, as implementing cohort-based training and testing
wouldrequirealongerandmorestablepost-reformobservationwindowtoavoidcon-
flatinggradualtemporaldriftwithstructuralbreaksinducedbylegislativechangesand
exogenousshocks. Assessingrobustnessacrosscohortsundersuchconditionsisidentified
asanimportantdirectionforfutureresearch.
7. ConclusionsandFutureWork
7.1. SummaryofMainFindings
This study developed a predictive framework for estimating whether borrowers of
theFondoSolidariodeCréditoUniversitario(FSCU)atthePontificiaUniversidadCatólicade
Valparaíso(PUCV)wouldsubmittheirfirstincomedeclarationusingonlypre-declaration
administrativeandacademicdata.Bycombiningstandardmachinelearningalgorithmswith
rigorouspreprocessing,themodelsachievedstrongandconsistentpredictiveperformance.
Linearclassifiers—LogisticRegressionandaSupportVectorMachine—demonstrated
highinterpretabilityandstability,whileensemblemodelssuchastheRandomForestand
LightGBMofferedslightlyhigherpredictiveaccuracy,reachingF1-scoresabove0.85and
MatthewsCorrelationCoefficientsaround0.41. Interpretabilityanalyses,includingpermu-
tationimportance,decision-treevisualization,andSHAPvalues,consistentlyidentifiedfi-
nancialandacademicfeatures—particularlytotaldebt(deud_monto),numberofenrollments
(conteo_matr),maritalstatus(estado_civil),andloanenforceabilityyear(anio_exigibilidad)—as
themostinfluentialdeterminantsofdeclarationbehavior. Together,theseresultsvalidate
thefeasibilityofleveragingadministrativedataforanticipatingdeclarationbehaviorand
demonstratethattransparent,interpretablemodelscanachievereliableperformancewithin
income-contingentloansettings.
7.2. MethodologicalImplications
Fromamethodologicalperspective,thestudyhighlightstheimportanceofcombining
predictiveperformancewithinterpretabilitywhenmodelingcompliance-relatedoutcomes
usingadministrativedata.Theresultsshowthatrelativelysimpleclassifiers,whenproperly
tunedandevaluated,canachievecompetitiveperformancewhilepreservingtransparency
andanalyticaltractability.
Theintegrationofinterpretablestructures—suchasexplicitdecisionpathsandad-
ditive explanation models—demonstrates that complex ensemble methods can remain
accessibletoinspectionandvalidation. Thisbalancebetweenaccuracyandexplainability
isparticularlyrelevantformodelingtasksinvolvingregulatedorhigh-stakesoutcomes,
whereunderstandingthecontributionofindividualfeaturesisasimportantaspredictive
accuracyitself.
7.3. DirectionsforFutureResearch
Whiletheresultsareencouraging,severalresearchopportunitiesremainopen. Fu-
tureworkshouldextendthepredictiveframeworktolongitudinalanalysis, examining
how borrower behavior evolves across successive income declarations and repayment
cycles. Incorporatingadditionalsocioeconomicvariables—suchasemploymentstability,
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 42of44
regionalcontext,orhouseholdcomposition—couldfurtherenhancepredictiveperformance
andinterpretability.
Fromamachinelearningpointofview, anaturalextensionistheincorporationof
cost-sensitiveorconstrainedlearningstrategies. Inthisdomain,theirmeaningfuladoption
requiresanexplicitinstitutionaldefinitionofmisclassificationcosts,sincetheoperational
consequencesoffalsepositivesandfalsenegativesareadministrative-policy-dependent.
Futureworkshouldformalizethesecoststructuresandevaluatecost-sensitivelearning
underthesamepre-eventconstraints.
Methodologically,integratingadvancedexplainableAItechniques(e.g.,SHAPinterac-
tionvalues,LIME,orcounterfactualexplanations)wouldallowforadeeperunderstanding
offeaturecontributionsatboththeindividualandsubgrouplevels. Expandingthedataset
toincludemultipleuniversitiesorlinkingitwithnationaladministrativerecordscould
testthemodel’sgeneralizabilityandscalability. Ultimately,theseextensionswouldcon-
tributetothedevelopmentofadaptiveandtransparentpredictiveframeworkssuitablefor
complex,regulatedadministrativedatasetsinChileandcomparablecontextsworldwide.
Anadditionalavenueforfutureresearchistoexaminetheextenttowhichthepro-
posedframeworkgeneralizesacrossadministrativecontextswithdifferentstructuralchar-
acteristics. Inparticular,controlledsensitivityanalysesunderalternativeclassimbalance
ratios or simulated administrative conditions would allow for a systematic assessment
of robustness beyond the specific distributional properties of the FSCU system. Such
extensionswouldhelpclarifywhichperformanceandinterpretabilitypatternsarestable
acrossinstitutionsandwhicharecontingentonlocalregulatoryorpopulationfeatures,
whilepreservingthepre-eventandaudit-orienteddesignprinciplesadoptedinthisstudy.
Overall,theresultsconfirmtheachievementofthisstudy’sobjectives: thepredictive
modelsidentifythekeyfactorsassociatedwithfirst-declarationbehaviorwhilemaintaining
reliable performance and interpretability under administrative constraints. This work
contributesareplicablemodelingframeworkthatbridgessupervisedlearning,explainable
AI, and real-world administrative data, reinforcing the role of transparent predictive
methodsinappliedcomputationalresearch.
AuthorContributions: Conceptualization,Á.P.,B.C.,E.M.,E.R.-T.,J.B.-G.,F.C.-C.,B.L.C.,A.Y.and
Á.P.F.;methodology,Á.P.,B.C.,E.M.,E.R.-T.andR.S.;software,Á.P.,J.B.-G.,F.C.-C.,B.L.C.andY.L.;
validation,Á.P.,B.C.,E.M.,E.R.-T.,J.B.-G.,F.C.-C.,B.L.C.,Y.L.,A.Y.,Á.P.F.andR.S.;formalanalysis,
Á.P.,J.B.-G.,F.C.-C.,B.L.C.,Y.L.andA.Y.;investigation,Á.P.,J.B.-G.,F.C.-C.,B.L.C.andY.L.;resources,
B.C.andÁ.P.F.; datacuration, Á.P., J.B.-G., F.C.-C., B.L.C.andY.L.; writing—originaldraft, Á.P.,
J.B.-G.,F.C.-C.,B.L.C.andY.L.;writing—review&editing,Á.P.,B.C.,J.B.-G.,F.C.-C.,B.L.C.,Y.L.,
Á.P.F.andR.S.;visualization,Á.P.,J.B.-G.,F.C.-C.,B.L.C.,Y.L.andA.Y.;supervision,B.C.,E.M.and
R.S.;projectadministration,Á.P.andB.C.Allauthorshavereadandagreedtothepublishedversion
ofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Therawdatasupportingtheconclusionsofthisarticlewillbemade
availablebytheauthorsonrequest.
Acknowledgments:JoséBarrera-GarcíaissupportedbytheNationalAgencyforResearchandDevel-
opment(ANID)/ScholarshipProgram/DOCTORADONACIONAL/2024-21242516.FelipeCisternas-
CaneoissupportedbytheNationalAgencyforResearchandDevelopment(ANID)/Scholarship
Program/DOCTORADONACIONAL/2023-21230203.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429 43of44
References
1. Romero,C.;Ventura,S. Educationaldatamining:Areviewofthestateoftheart. IEEETrans.Syst.ManCybern.PartC(Appl.
Rev.)2010,40,601–618.[CrossRef]
2. Paz,Á.;Crawford,B.;Monfroy,E.;Barrera-García,J.;PeñaFritz,Á.;Soto,R.;Cisternas-Caneo,F.;Yáñez,A. MachineLearning
andMetaheuristicsApproachforIndividualCreditRiskAssessment:ASystematicLiteratureReview. Biomimetics2025,10,326.
[CrossRef][PubMed]
3. He,H.;Garcia,E.A. Learningfromimbalanceddata. IEEETrans.Knowl.DataEng.2009,21,1263–1284.[CrossRef]
4. Doshi-Velez,F.;Kim,B. Towardsarigorousscienceofinterpretablemachinelearning. arXiv2017,arXiv:1702.08608.[CrossRef]
5. ConsejodeRectorasyRectoresdelasUniversidadesChilenas. UniversidadesCRUCHaloLargodeChile. 2025. Available
online:https://consejoderectores.cl/el-consejo/universidades-cruch/(accessedon16October2025).
6. BibliotecaNacionaldelCongresodeChile. LeyFondosSolidatirosdeCréditoUniversitario. 1994 Availableonline: https:
//www.bcn.cl/leychile/navegar?idNorma=30654(accessedon16October2025).
7. Biblioteca Nacional del Congreso de Chile. Modificación Ley Fondos Solidatiros de Crédito Universitario. 2012. Avail-
ableonline:https://www.bcn.cl/leychile/navegar?idNorma=1036996&idParte=9235355&idVersion=2012-02-04(accessedon
16October2025).
8. SubsecretaríadeEducaciónSuperior,MINEDUC. PrimerInformeCréditoconAvaldelEstado:Característicasdelapoblación
deudoraeimpactos,Julio2022. Availableonline:https://educacionsuperior.mineduc.cl/wp-content/uploads/sites/49/2022/
07/PrimerInformeCAE-1.pdf(accessedon30December2025).
9. ConsejodeRectorasyRectoresdelasUniversidadesChilenas(CRUCH). DeudoresMorososdeFondoSolidariodeCrédito
Universitario(publicacionesanuales). 2025. Availableonline: https://consejoderectores.cl/en/fondo-solidario-de-credito-
universitario/(accessedon6September2025).
10. SuperintendenciadeEducaciónSuperior. NormadeCarácterGeneralN°3:RegistrosycontabilidaddelFSCU.2024. Available
online:https://www.sesuperior.cl/wp-content/uploads/2024/04/NCG-3-FSCU.pdf(accessedon6September2025).
11. Pontificia Universidad Católica de Valparaíso. Fondo Solidario de Crédtio Universitario. 2025 Available online: https:
//estudiantespucv.cl/fscu/(accessedon16October2025).
12. DepartmentforEducation(UK). StudentLoansinEngland: FinancialYear2024–25; DepartmentforEducation: London,UK,
2025. Availableonline:https://www.gov.uk/government/statistics/student-loans-in-england-2024-to-2025/student-loans-in-
england-financial-year-2024-25(accessedon6September2025).
13. AustralianTaxationOffice. StudyandTrainingLoanRepaymentThresholdsandRates;AustralianTaxationOffice:Canberra,Australia,
2025. Availableonline:https://www.ato.gov.au/tax-rates-and-codes/study-and-training-support-loans-rates-and-repayment-
thresholds(accessedon6September2025).
14. Salmi,J.;Hauptman,A.M. InnovationsinTertiaryEducationFinancing:AComparativeEvaluationofAllocationMechanisms.
WorldBank.2006. Availableonline:https://documents1.worldbank.org/curated/en/383241468138743150/pdf/383240WP0
Box0317363B01PUBLIC1.pdf(accessedon6September2025).
15. OECD. OECDPolicyGPS—StudentSupport(ComparativePolicyNotes); OECD:Paris, France, 2024. Availableonline: https:
//gpseducation.oecd.org/revieweducationpolicies/(accessedon6September2025).
16. Thuy,N.T.H.;Ha,N.T.V.;Trung,N.N.;Binh,V.T.T.;Hang,N.T.;Binh,V.T. ComparingtheEffectivenessofMachineLearningand
DeepLearningModelsinStudentCreditScoring:ACaseStudyinVietnam. Risks2025,13,99.[CrossRef]
17. Suleiman,R.;Anane,R. Institutionaldataanalysisandmachinelearningpredictionofstudentperformance. InProceedingsof
the2022IEEE25thInternationalConferenceonComputerSupportedCooperativeWorkinDesign(CSCWD),Hangzhou,China,
4–6May2022;IEEE:NewYork,NY,USA,2022;pp.1480–1485.[CrossRef]
18. Yakubu,M.N.;Abubakar,A.M. Applyingmachinelearningapproachtopredictstudents’performanceinhighereducational
institutions. Kybernetes2022,51,916–934.[CrossRef]
19. Lessmann,S.;Baesens,B.;Seow,H.V.;Thomas,L.C. Benchmarkingstate-of-the-artclassificationalgorithmsforcreditscoring:An
updateofresearch. Eur.J.Oper.Res.2015,247,124–136.[CrossRef]
20. Aulck,L.;Velagapudi,N.;Blumenstock,J.;West,J. Predictingstudentdropoutinhighereducation. arXiv 2016,arXiv:1606.06364.
[CrossRef]
21. Hastie,T.;Tibshirani,R.;Friedman,J. TheElementsofStatisticalLearning,2nded.;SpringerSeriesinStatistics;Springer:NewYork,
NY,USA,2009.[CrossRef]
22. Alam,T.M.;Shaukat,K.;Hameed,I.A.;Luo,S.;Sarwar,M.U.;Shabbir,S.;Li,J.;Khushi,M. AnInvestigationofCreditCard
DefaultPredictionintheImbalancedDatasets. IEEEAccess2020,8,201173–201198.[CrossRef]
23. Madaan,M.;Kumar,A.;Keshri,C.;Jain,R.;Nagrath,P. Loandefaultpredictionusingdecisiontreesandrandomforest: A
comparativestudy.IOPConf.Ser.Mater.Sci.Eng.2021,1022,012042.[CrossRef]
24. Lemaître,G.;Nogueira,F.;Aridas,C.K. Imbalanced-learn: APythonToolboxtoTackletheCurseofImbalancedDatasetsin
MachineLearning. J.Mach.Learn.Res.2017,18,1–5.
https://doi.org/10.3390/math14030429

Mathematics2026,14,429
44of44
25. Chicco,D.;Jurman,G. TheadvantagesoftheMatthewscorrelationcoefficient(MCC)overF1scoreandaccuracyinbinary
| classificationevaluation. |                | BMCGenom.2020,21,6.[CrossRef][PubMed] |
| ------------------------- | -------------- | ------------------------------------- |
| 26. Breiman,L.            | RandomForests. | Mach.Learn.2001,45,5–32.[CrossRef]    |
Disclaimer/Publisher’sNote:
Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/math14030429