---
conversion_metadata:
  converted_at: "2026-07-21T13:35:07Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Imani et al.pdf"
  source_pdf_sha256: "d589704ce61f2c3c6d92954fa606b0136a57f557d3cc99b5363b1d1ae423777e"
  page_count: 38
  markdown_char_count: 268229
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Systematic Review
Customer Churn Prediction: A Systematic Review of Recent
Advances, Trends, and Challenges in Machine Learning and
Deep Learning

Mehdi Imani 1,*

, Majid Joudaki 2

, Ali Beikmohammadi 1,*

and Hamid Reza Arabnia 3

1 Department of Computer and System Sciences, Stockholm University, SE-16455 Stockholm, Sweden
2 Department of Computer Engineering, Faculty of Engineering, Ayatollah Boroujerdi University,

Boroujerd 69199-69737, Iran; m.joudaki@abru.ac.ir
School of Computing, University of Georgia, Athens, GA 30602, USA; hra@uga.edu

3

* Correspondence: m.imani@gmail.com (M.I.); beikmohammadi@dsv.su.se (A.B.)

Abstract

Background: Customer churn significantly impacts business revenues. Machine Learning
(ML) and Deep Learning (DL) methods are increasingly adopted to predict churn, yet a
systematic synthesis of recent advancements is lacking. Objectives: This systematic review
evaluates ML and DL approaches for churn prediction, identifying trends, challenges, and
research gaps from 2020 to 2024. Data Sources: Six databases (Springer, IEEE, Elsevier,
MDPI, ACM, Wiley) were searched via Lens.org for studies published between January
2020 and December 2024. Study Eligibility Criteria: Peer-reviewed original studies ap-
plying ML/DL techniques for churn prediction were included. Reviews, preprints, and
non-peer-reviewed works were excluded. Methods: Screening followed PRISMA 2020
guidelines. A two-phase strategy identified 240 studies for bibliometric analysis and 61
for detailed qualitative synthesis. Results: Ensemble methods (e.g., XGBoost, LightGBM)
remain dominant in ML, while DL approaches (e.g., LSTM, CNN) are increasingly applied
to complex data. Challenges include class imbalance, interpretability, concept drift, and lim-
ited use of profit-oriented metrics. Explainable AI and adaptive learning show potential but
limited real-world adoption. Limitations: No formal risk of bias or certainty assessments
were conducted. Study heterogeneity prevented meta-analysis. Conclusions: ML and DL
methods have matured as key tools for churn prediction, yet gaps remain in interpretability,
real-world deployment, and business-aligned evaluation. Systematic Review Registration:
Registered retrospectively in OSF.

Keywords: customer churn prediction; customer retention; deep learning; literature review;
machine learning

1. Introduction

Customer retention has become a critical challenge for businesses across various indus-
tries, including telecommunications, retail, banking, insurance, healthcare, education, and
subscription-based services. Customer churn—customers discontinuing their relationship
with a company—can significantly impact revenues, with annual churn rates ranging from
20% to 40% in some sectors [1]. Research indicates that acquiring a new customer is five to
twenty-five times more expensive than retaining an existing one, making churn prevention
a strategic priority for companies [2].

Academic Editors: Oliver Hinz and

Andreas Holzinger

Received: 9 July 2025

Revised: 10 September 2025

Accepted: 19 September 2025

Published: 21 September 2025

Citation:

Imani, M.; Joudaki, M.;

Beikmohammadi, A.; Arabnia, H.R.

Customer Churn Prediction: A

Systematic Review of Recent

Advances, Trends, and Challenges in

Machine Learning and Deep Learning.

Mach. Learn. Knowl. Extr. 2025, 7, 105.

https://doi.org/10.3390/

make7030105

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Mach. Learn. Knowl. Extr. 2025, 7, 105

https://doi.org/10.3390/make7030105

---

<!-- PAGE 2 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

2 of 38

Machine Learning and Deep Learning have emerged as powerful tools for churn
prediction due to their ability to analyze large, high-dimensional, and dynamic customer
datasets effectively. Traditional churn prediction methods, such as rule-based systems and
statistical modeling, often fail to capture customer behaviour’s complexities adequately.
Conversely, ML approaches like Decision Trees (DTs), Random Forests (RFs), Support Vector
Machines (SVMs), and boosting algorithms (e.g., XGBoost, LightGBM, CatBoost) have
demonstrated strong predictive capabilities with structured datasets [3–5]. Furthermore,
advanced DL architectures—including Artificial Neural Networks (ANNs), Convolutional
Neural Networks (CNNs), Long Short-Term Memory networks (LSTMs), and Transformer-
based models—provide significant advantages for modeling sequential and unstructured
data, such as customer interaction histories and textual feedback.

Despite these technological advancements, several critical challenges remain in churn
prediction. Model interpretability remains a significant concern, especially with complex
DL-based approaches often functioning as “black-box” models [6]. Data imbalance is
another prevalent issue, as churn datasets typically feature significantly fewer churners
than non-churners, potentially biasing model predictions [5]. Additionally, concept drift—
the evolving nature of customer behaviour over time—complicates the sustained accuracy
of predictive models.

This literature review systematically explores advancements in customer churn pre-
diction by analyzing peer-reviewed research published between 2020 and 2024 across
diverse domains such as telecommunications, retail, banking, healthcare, education, and
insurance. It aims to map the current landscape of ML and DL approaches, evaluating
their strengths, limitations, and applicability to real-world scenarios. Given the broad
adoption of predictive analytics across industries, this review seeks to clarify the evolution
of these methodologies, the specific challenges they address, and the gaps that require
further research.

A key objective of this study is to identify and categorize the most frequently employed
ML and DL techniques used in churn prediction. Understanding the evolution of these
methods over recent years provides insights into how businesses and researchers have re-
fined approaches to enhance accuracy and adaptability. Additionally, this review evaluates
the performance and interpretability of various predictive models, focusing specifically on
their capacity to manage imbalanced datasets, dynamic customer behaviours, and practical
deployment constraints. Considering that customer churn results from multiple factors—
such as transaction histories, engagement patterns, and external market conditions—it is
crucial to assess the effectiveness of models in capturing these complexities.

Another central goal is highlighting persistent challenges and limitations within churn
prediction research. Despite substantial progress, issues such as the black-box nature of DL
models, class imbalance, and difficulty adapting models to evolving customer behaviours
impede real-world implementations. This review emphasizes these research gaps and
suggests potential areas for future investigation, including improving model transparency,
advancing feature engineering techniques, and developing adaptive learning methods to
address shifting customer preferences.

While this review synthesizes a broad body of recent literature on customer churn
prediction, we intentionally refrain from presenting a direct comparison of their reported
performance metrics (e.g., accuracy, F1-score, AUC). This decision is based on the substan-
tial heterogeneity observed across the studies regarding dataset characteristics, imbalance
ratios, feature sets, modeling objectives, and evaluation protocols.

Specifically, models were trained and validated on various public and proprietary
datasets drawn from diverse industries (e.g., telecommunications, banking, e-commerce),
often with distinct definitions of churn, time windows, and input modalities. Evaluation

---

<!-- PAGE 3 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

3 of 38

metrics also varied widely, with some studies prioritising business-oriented outcomes and
others focusing on statistical measures. As such, any attempt to aggregate or compare these
results directly would risk introducing misleading interpretations and overgeneralizations.
Instead, this review focuses on identifying methodological trends, the taxonomy of
modeling strategies, and common challenges and innovations. Where appropriate, we
highlight representative studies that exemplify key methodological advances without
asserting quantitative superiority. We encourage future benchmark studies using standard-
ized datasets and experimental protocols to conduct rigorous performance comparisons,
ideally incorporating statistical significance testing under controlled conditions.

To address these objectives, this study is guided by three fundamental research ques-

tions:

RQ1: What are the predominant ML and DL approaches used in customer churn

prediction, and how have these methodologies evolved over time?

RQ2: How do different predictive models compare accuracy, adaptability, and inter-

pretability when applied to churn prediction across various industries?

RQ3: What are the significant challenges and limitations in existing churn predic-
tion research, and what future directions can be explored to enhance the effectiveness of
predictive models?

This review synthesizes current research to inform both academic and industry prac-
tices. This work’s specific contributions and novel aspects are outlined in the following
subsection.

Contributions and Novelty

This study offers several distinct contributions that differentiate it from prior reviews

on customer churn prediction:

1. Most Recent and Comprehensive Scope: We systematically review peer-reviewed
research published between January 2020 and December 2024, encompassing recent
advances such as CNN-based architectures, hybrid deep learning frameworks, and
profit-driven modelling approaches. Earlier reviews predominantly focus on pre-2020
literature and therefore do not capture these emerging trends.
PRISMA-Guided and Reproducible Methodology: Our search and selection strategy
adheres to the PRISMA 2020 guidelines, ensuring methodological transparency and
reproducibility. We employ a two-phase review process, an initial bibliometric analysis
of 240 studies followed by an in-depth synthesis of 61 key papers. Whereas existing
reviews often lack such a structured and replicable approach.

2.

4.

3. Novel Hierarchical Taxonomy: We introduce a new hierarchical taxonomy that catego-
rizes ML and DL approaches into fine-grained subgroups (e.g., profit-centric models,
optimization/metaheuristics, adaptive learning, explainable AI). This taxonomy pro-
vides a systematic framework for mapping the methodological landscape, a feature
absent in earlier works.
Integration of Bibliometric and Methodological Insights: In addition to methodolog-
ical synthesis, we conduct a comprehensive bibliometric analysis, including pub-
lisher trends, citation dynamics, and open-access effects, to contextualize the research
landscape. Previous reviews focus exclusively on models and do not incorporate
dissemination-oriented analyses.
Identification of Emerging Challenges Supported by Evidence-Based Trends: We
identify challenges such as class imbalance, concept drift, and the limited adoption of
business-oriented evaluation metrics, linking them to representative studies published
between 2020 and 2024. This evidence-driven mapping of trends provides a more

5.

---

<!-- PAGE 4 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

4 of 38

precise and up-to-date perspective than the generic limitations discussed in earlier
surveys.

By clearly delineating these contributions, this review makes its novelty and value
explicit, offering actionable insights for academic researchers and industry practitioners
engaged in customer retention analytics.

2. Purpose of the Study

Customer churn prediction is vital in modern Customer Relationship Management
(CRM), helping businesses proactively retain at-risk customers and maximize customer
lifetime value. With high churn rates leading to substantial revenue losses, businesses
in subscription-based services, telecommunications [1,7], retail [8], banking [9], educa-
tion [10], healthcare [11], Insurance [12], and other sectors increasingly rely on data-driven
approaches to enhance customer retention strategies.

While businesses collect vast amounts of customer data, extracting actionable insights
from these datasets is challenging. Data mining, a key discipline in ML and artificial intelli-
gence, enables organizations to uncover hidden patterns and trends in churn behaviours.
However, the effectiveness of churn prediction models varies significantly based on the
choice of methodology, dataset characteristics, and industry-specific factors.

This study systematically reviews 240 research articles published between 2020 and
2024, focusing on churn prediction using ML and DL methodologies across various sectors.
The review:

Examines different churn prediction approaches across multiple industries.

•
• Assesses the comparative performance of ML and DL techniques in churn prediction.
•
Investigates common challenges, such as data imbalance, feature selection, inter-
pretability, and concept drift.

• Highlights emerging trends in churn prediction, including profit-driven modeling,

explainable AI (XAI), and adaptive learning approaches.

Churn prediction research is crucial for developing effective retention strategies,
allowing businesses to anticipate customer attrition, personalize marketing efforts, and
allocate retention budgets more efficiently. Studies suggest that businesses implementing
advanced churn prediction techniques can improve retention rates by 5–10%, leading to
profit increases of 25–95% [13].

By synthesizing insights from recent research, this paper serves as a valuable resource
for researchers, data scientists, and industry practitioners, helping them understand best
practices, methodological advancements, and future directions in churn prediction.

For more information, readers can refer to several comprehensive review papers that
explore various aspects of customer churn prediction. Imani and Arabnia [3] provide a com-
parative analysis of hyperparameter optimization techniques and data sampling strategies
in ML models for churn prediction, highlighting their impact on predictive performance.
The authors in [5] extend this analysis by evaluating the effectiveness of SMOTE, ADASYN,
and GNUS upsampling techniques in conjunction with RF and XGBoost under different
class imbalance levels. Geiler et al. [14] offer a broad survey of ML approaches for churn
prediction, discussing their strengths, limitations, and practical applications. Domingos
et al. [15] focus on hyperparameter tuning for DL-based churn prediction models, particu-
larly within the banking sector, providing insights into optimizing deep neural networks
for improved accuracy. These studies offer valuable perspectives on churn prediction
research’s methodological advancements and challenges.

---

<!-- PAGE 5 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

5 of 38

3. Search Strategies

A systematic literature search was conducted across six major academic publishers,
including Springer, IEEE, Elsevier, MDPI, ACM, and Wiley, ensuring comprehensive cover-
age of recent advancements in customer churn prediction using ML and DL techniques.
The search was executed via Lens.org, a scholarly research platform offering advanced
filtering and indexing capabilities superior to generic search engines like Google Scholar.
To refine the search, the query “(churn prediction AND machine learning) OR (churn
prediction AND deep learning) NOT (“survey” OR “review”)” was applied, focusing on
original research contributions rather than survey or review articles. Additionally, results
were restricted to journal and conference proceedings articles published between 2020 and
2024, ensuring relevance to recent developments. The KStem-based stemming approach
was utilized to normalize variations of the term “churn,” such as “churned” and “churning,”
to capture a broader range of relevant studies. The final search was conducted on 15 January
2025. Visualizations and plots were produced using Python 3.13, employing the matplotlib
and seaborn libraries to ensure clarity and reproducibility of graphical results.

As illustrated in Figure 1, the initial search retrieved 837 articles. To ensure relevance
and quality, a series of refinement steps was applied. First, filtering by document type to in-
clude only journal and conference articles while excluding pre-prints, technical reports, and
other non-peer-reviewed documents reduced the count to 679 articles. Next, restricting the
selection to high-quality publishers—as previously outlined—further refined the dataset to
368 articles. Finally, a domain-specific review was conducted to eliminate papers unrelated
to customer churn prediction or those not utilizing ML and DL techniques. This resulted in
a final selection of 240 articles for the first phase (shallow review phase). This exploratory
phase analyzed broad research trends, methodological patterns, and key developments in
customer churn prediction using ML and DL approaches. This phase focused on high-level
bibliometric analysis, including publication trends across research domains, the distribu-
tion of ML and DL techniques, the average citation trends of publishers (Crossref citation),
citation patterns, and the publications shared among different publishers over the past five
years (2020–2024). By analyzing these broader trends, this phase provided a foundation for
identifying the most influential studies, emerging research directions, and methodological
advancements.

A second phase (deep review phase) was conducted to ensure a more focused and
rigorous examination, in which 61 papers were selected based on relevance, citation impact,
methodological novelty, and contribution to the field. This phase delved into the technical
depth of the selected studies, focusing on critical aspects such as dataset characteristics,
applied ML and DL techniques, evaluation metrics, and the key outcomes reported in the
studies. By conducting this two-phase review strategy, the study captured broad research
trends and provided a granular understanding of methodological advancements, dataset
challenges, and performance benchmarks. This structured approach enhanced the literature
review’s comprehensiveness, objectivity, and depth, ensuring both breadth and depth in
assessing the state-of-the-art customer churn prediction research.

The inclusion criteria are outlined below:

• Articles must focus on churn prediction using ML or DL techniques.
• Articles published between 2020 and 2024 in peer-reviewed, high-quality journals.
• Articles must be original research papers.
• Articles published in English.

The exclusion criteria are outlined below:

• Articles unrelated to churn prediction.
• Articles unrelated to ML or DL.

---

<!-- PAGE 6 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

6 of 38

• Non-peer-reviewed works (e.g., lecture notes, newsletters, dissertations).
•
•
• Non-English publications.

Low-quality publishers.
Review papers, preprints, books, etc.

Figure 1. PRISMA Flowchart.

This systematic approach, grounded in a well-documented filtering process and
adherence to PRISMA guidelines, ensures the reproducibility of this literature review. All
inclusion criteria, search strings, and filtering steps have been explicitly outlined to facilitate
replication by future researchers.

Two reviewers (MI and MJ) collaboratively screened titles and abstracts for relevance,
resolving disagreements through discussion. One reviewer (MI) extracted study charac-
teristics and methodological details for data collection, while the second reviewer (MJ)
cross-checked for accuracy. No automation tools or contact with study authors were used
during these processes.

For each included study, data were extracted on the primary outcomes of interest:
ML/DL techniques employed, evaluation metrics (e.g., accuracy, F1-score, ROC-AUC,
PR-AUC), and key findings related to methodological challenges such as class imbalance,
concept drift, and model interpretability. Additional variables collected included publi-
cation year, application domain (e.g., telecommunications, banking, healthcare), dataset
characteristics (public, private, or synthetic), and study citation metrics. All data were
extracted as reported in the original publications; no imputation or conversions were
applied.

Studies were grouped for synthesis using a two-phase approach: a shallow review
phase (240 studies) to identify broad methodological trends and a deep review phase
(61 studies) for detailed analysis. Results were tabulated and visually displayed using
summary tables and figures to illustrate trends in ML/DL techniques, performance metrics,

---

<!-- PAGE 7 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

7 of 38

and application domains. Narrative synthesis was performed to summarize methodological
patterns and challenges, as a meta-analysis was not feasible due to heterogeneity in study
designs, datasets, and evaluation metrics. No subgroup analyses or sensitivity analyses
were conducted, given the qualitative focus of this review.

We did not perform a formal risk of bias assessment or reporting bias assessment, as
the review aimed to synthesize methodological trends rather than evaluate the quality of
individual studies. Similarly, a formal certainty assessment (e.g., using GRADE) was not
applied. Future systematic reviews conducting quantitative synthesis or meta-analyses
should consider incorporating these assessments using standardized tools such as ROBIS,
AMSTAR 2, or GRADE. This systematic review was retrospectively registered in the Open
Science Framework (OSF) under DOI: https://doi.org/10.17605/OSF.IO/PZ2H7.

4. Trends in Churn Prediction Research

To comprehensively investigate the state of churn prediction research, we systemati-
cally reviewed 240 publications spanning the years 2020 to 2024. This five-year window
was chosen to capture current trends and reflect the rapid advancements in ML and DL
applications. The broad scope of this initial pool enabled us to analyze significant trends
in publisher distribution, citation dynamics, average citation variations, research domain
focus, and the adoption of various ML and DL techniques. All studies excluded during
the screening process failed to meet the predefined inclusion criteria (e.g., they did not
employ ML/DL techniques, did not address churn prediction, or were non-peer-reviewed).
No studies that initially appeared to meet inclusion criteria were excluded during full-text
review.

From this more extensive set, we selected 61 studies for deeper qualitative examination.
This subset was identified based on multiple criteria, including methodological rigor,
novelty of approach, domain diversity, and overall contribution to the field. By combining
a wide-ranging quantitative overview with a focused, in-depth analysis of key studies, our
methodology ensures an expansive mapping of churn prediction research and a thorough
investigation of the most influential and innovative work. This dual-level strategy thus
provides readers with a robust understanding of current practices, emerging challenges,
and future directions in churn prediction using ML and DL techniques.

Figure 2 presents the overall distribution of publications by publishers. The pie chart
illustrates that IEEE accounts for the largest share, with 60.4% of the total publications.
Springer and Elsevier follow, at 12.9% and 11.2%, respectively, while MDPI comprises 7.1%
of the dataset. ACM and Wiley comprise the remaining 5.8% and 2.5%, respectively. These
percentages highlight the dominant position of IEEE among the publishers represented in
this study.

Figure 3 further explores the temporal dimension of these publications from 2020
through 2024. IEEE exhibits a marked increase in published papers, peaking in 2023. In
contrast, the other publishers remain relatively steady, though minor fluctuations can
be observed from year to year. Notably, the apparent decline in publications for 2024 is
likely attributable to incomplete indexing during data extraction (January 2025). Given
that not all 2024 publications may have been processed and included in our study by that
point, the downward trend for 2024 should be interpreted with caution. These figures
suggest that IEEE consistently leads in publication output, while other publishers maintain
comparatively smaller yet stable shares over the examined period.

---

<!-- PAGE 8 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

8 of 38

Figure 2. Share of Publications by Publishers.

Figure 3. Publication Trends of Publishers.

Figures 4 and 5 illustrate the number of citations and normalized impact factor trends
for the selected publishers (Elsevier, IEEE, MDPI, Springer, Wiley, and ACM) from 2020 to
2024. Figure 4 shows that Elsevier exhibited the highest total citations in 2020, followed
by a noticeable decline in subsequent years. Other publishers, including IEEE and MDPI,
display smaller but still discernible peaks in earlier years, with a tendency toward reduced
citation counts in 2023 and 2024. These observations align with the typical pattern in
bibliometric analyses, whereby earlier publications have a longer window to accumulate
citations.

Figure 4. Citations Received by Each Publisher.

---

<!-- PAGE 9 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

9 of 38

Figure 5. Normalized IF Trends of Publishers.

Figure 5 illustrates the normalized impact factor trends of the publishers from 2020
to 2024. To ensure a fair comparison of citation performance across publication years,
we computed a normalized impact factor (IF) by dividing the total number of citations
received by the number of published papers and the number of years since publication.
This approach accounts for the varying time windows available for papers to accumulate
citations, thus mitigating the bias that favors earlier publications. The formula used is as
follows:

Normalized IF =

Total Citations
Number o f Papers × Years Since Publications

As shown in Figure 5, Elsevier and MDPI consistently outperform other publishers in
terms of normalized impact across most years. Elsevier exhibits strong performance in 2020
(above 10 citations per paper per year), dips in 2022, and then peaks again in 2023, suggest-
ing a combination of high-impact publications and efficient visibility. MDPI demonstrates
a steep rise in 2021—reaching nearly 10 citations per paper per year—and a gradual decline
in the following years yet maintaining a relatively strong citation performance through 2023.
Springer shows a downward trend from 2020 to 2022 but stabilizes around three citations
per paper per year by 2023. Wiley peaks in 2021, like MDPI, followed by a moderate but
steady decline. IEEE and ACM display lower and more stable citation patterns across the
years, with values remaining primarily below 2, indicating more consistent but modest
average citation rates.

While the normalized impact factor accounts for the time since publication, a general
decline is still observed in 2024 across most publishers. This may reflect several factors,
including recent shifts in publication strategies, article topics, quality changes, or early-
stage visibility. Moreover, papers published in 2024 may not yet be fully indexed or
cited at the time of data extraction (January 2025), especially for journals with delayed
indexing pipelines. As such, citation-based metrics from the most recent year should be
interpreted with caution, as they may underestimate the eventual long-term impact of these
publications.

Overall, the trends reveal significant year-to-year variation in normalized citation
performance among publishers, underscoring the roles of editorial policy, topical focus,
and dissemination strategies. By adjusting for publication age, the normalized impact
factor offers a fairer and more time-independent comparison, particularly when analyzing
performance across both recent and earlier publication years.

Figure 6 illustrates the overall distribution of citation counts for the collected publica-
tions, revealing a highly skewed pattern. Most papers receive only a few citations (fewer
than five), while a relatively small number of publications accumulate notably higher
citation counts. This right-skewed distribution is typical in bibliometric analyses, wherein

---

<!-- PAGE 10 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

10 of 38

most publications garner modest attention, whereas a limited subset gains substantial
visibility and, consequently, higher citation impact.

Figure 6. Citation Count Distribution.

Figure 7 presents the normalized impact factor trends—the average number of citations
per paper per year—for Open Access (OA) and Non-Open Access (non-OA) publications
from 2020 to 2024. Across all years, OA papers consistently outperform non-OA articles in
terms of citation impact, with robust performance in 2020 and 2021. This trend supports
the notion that OA publishing may enhance the visibility and discoverability of research,
thereby increasing its citation potential. While the normalized metric accounts for the time
since publication, a noticeable decline is observed for both OA and non-OA papers in
2024. This may reflect limited early-stage visibility, indexing delays, or publication lags that
hinder citation accumulation, particularly for articles published close to the data extraction
date (January 2025), which may not yet be fully indexed or cited, especially in journals with
slower indexing pipelines. As such, the lower values observed for the most recent year
should be interpreted cautiously, as they may not accurately reflect the long-term influence
of those publications.

Figure 7. Normalized IF Trends: OA vs. non-OA Papers.

Figure 8 presents the annual distribution of publications across six research domains—
Telecom, Retail, Banking, Education, Healthcare, and Insurance—from 2020 to 2024. Across
most domains, the overall trend is gradual growth from 2020 through 2023, followed by a
slight decline in 2024. Telecom shows a pronounced increase in publications up to 2023,
indicating a sustained research focus on churn prediction within that sector. Healthcare and
Education also exhibit steady upward trajectories, reflecting broader interest in applying
churn-related methodologies to patient retention and student engagement. Retail and
Banking maintain moderate but consistent growth, while Insurance remains comparatively

---

<!-- PAGE 11 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

11 of 38

lower throughout the observed period. The apparent drop in 2024 publications for all
domains is likely influenced by the shorter window for indexing at the time of data
extraction (January 2025), and it does not necessarily indicate a waning research interest.

Figure 8. Publication trends by research domains.

Figure 9 presents the time series trends of ML and DL techniques in churn prediction
from 2020 to 2024. ML methods exhibit a steady upward trend, indicating their widespread
adoption. In contrast, DL publications remain relatively low but show gradual growth. The
apparent decline in 2024 should be interpreted cautiously, as many papers from this year
may not yet be fully indexed or have had sufficient time to gain citations and visibility.

Figure 9. The usage of different categories of techniques in churn prediction research.

Figure 10 depicts the annual usage of seven ML algorithms—Boosting Techniques
(including XGBoost, LightGBM, and CatBoost), K-Nearest Neighbors, RF, DT, SVM, Naïve
Bayes, and Logistic Regression—between 2020 and 2024. Boosting Techniques, RF, and
Logistic Regression show notable growth through 2022–2023, suggesting increased research
interest in ensemble-based methods and widely used baseline models. While most tech-
niques experienced a slight dip in 2024, it is likely due to incomplete indexing and the
relatively short time since publication at the time of data extraction (January 2025).

Figure 11 focuses on DL approaches—ANNs, LSTMs, CNNs, Recurrent Neural Net-
works (RNNs), Transformers, and Reinforcement Learning—over the same period. ANNs
exhibit a pronounced surge in 2022, reflecting their broad applicability in diverse domains.
LSTMs and CNNs also show moderate yet consistent usage, while Transformers and Re-
inforcement Learning remain less frequent but appear to have gained modest traction in
recent years. Like the ML trends, the lower counts for 2024 likely do not capture the full
extent of ongoing research activity, underscoring the need to interpret these recent-year
values cautiously. Overall, the data reveal a continued shift toward advanced ML and DL

---

<!-- PAGE 12 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

12 of 38

techniques, albeit tempered by the time-dependent nature of publication and indexing
cycles.

Figure 10. The usage of different conventional ML techniques in churn prediction research.

Figure 11. The usage of different DL techniques in churn prediction research.

While the primary focus of this review is on methodological advancements in churn
prediction, analyzing where and how research is published offers complementary insights
into the dissemination and visibility of the field. The distribution of publications across
major academic publishers and the temporal trends in citation activity help illustrate
the growing attention to churn prediction across domains such as telecommunications,
banking, and healthcare. For example, the predominance of IEEE publications may reflect
historical engagement with machine learning applications in telecommunications and a
concentration of conference-style contributions. While citation trends at the publisher level
cannot be directly linked to specific methods or studies, they may suggest broader patterns
in research visibility, accessibility (e.g., open access availability), and perceived relevance.
As such, these bibliometric observations contextualize, not evaluate, the methodological
developments reviewed in this study.

5. Paper’s Categorizations

In our review, we propose a comprehensive taxonomy that systematically organizes
the literature on churn prediction into two primary methodological categories: Machine
Learning Approaches and Deep Learning Approaches. Each category is further subdivided
into specific subcategories, as illustrated in Figure 12.

---

<!-- PAGE 13 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

13 of 38

Figure 12. Taxonomy of Churn Prediction Approaches.

The ML Approaches encompass a range of techniques, including profit-centric mod-
els, which optimize retention strategies based on business impact, and ensemble and
hybrid approaches, which combine multiple classifiers to improve predictive performance.
Optimization and metaheuristic methods also focus on refining feature selection and hyper-
parameter tuning, while adaptive and resampling techniques address data imbalance and
concept drift. The review also covers explainable and interpretable models, which enhance
transparency in churn prediction, data-centric and augmentation strategies that leverage
novel data sources and synthetic data generation, and traditional ML techniques, which
continue to play a foundational role in churn modeling.

On the other hand, DL approaches leverage advanced architectures to capture com-
plex patterns in customer behaviour. These include deep reinforcement learning, which
enables adaptive decision-making, and temporal and sequential models, such as LSTMs,
which capture evolving churn patterns over time. The taxonomy also highlights hybrid
and ensemble DL approaches, which integrate multiple DL frameworks for improved
generalization, and CNN-based models, which excel in feature extraction. Furthermore,
feedforward deep neural networks, NLP-based models for text-based churn analysis, and
representation and feature interaction techniques, which enhance predictive performance
by capturing high-order dependencies, are explored.

As noted in the Introduction, direct comparison of reported performance metrics was
avoided due to substantial heterogeneity in datasets, evaluation protocols, and modeling
objectives across studies. Instead, a descriptive synthesis of individual study results is
presented.

By structuring the existing research into this hierarchical framework, our taxonomy
provides a clear perspective on the evolution of churn prediction methodologies. It under-
scores how different approaches have been tailored to address the multifaceted challenges
of churn modeling, from enhancing predictive accuracy and scalability to improving inter-
pretability and data efficiency.

---

<!-- PAGE 14 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

14 of 38

6. Machine Learning Approaches

Machine learning methodologies have significantly enhanced churn prediction
through diverse approaches to address complex customer retention challenges across
various sectors. Recent research encompasses profit-driven models, ensemble learning
techniques, optimization-based methods, adaptive resampling strategies, explainable artifi-
cial intelligence (XAI), and traditional algorithms. Each methodology contributes distinct
advantages such as improved predictive accuracy, enhanced interpretability, computational
efficiency, and alignment with business objectives. This section reviews these innovative
approaches, outlining their methodologies, data characteristics, and performance evalua-
tions, thereby providing valuable guidance for selecting suitable ML techniques for specific
churn prediction applications.

Table 1 briefly summarizes each study by indicating the dataset types used (public,

private, or synthetic), ML techniques employed, and performance metrics evaluated.

Table 1. The summary of studies in the domain of conventional ML.

Category

Ref.

Year

Dataset

Techniques Used

[16]

2020

Public

DT, Evolutionary Algorithm

Profit-centric

Ensemble and
Hybrid ML

[17]

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

[29]

[30]
[31]
[32]

[33]

2020

Public

Minimax Probability Machines (MPM), LASSO,
Tikhonov Regularization

2024

Private

Gradient Boosting

2020

Public

Ensemble Learning

2020

Private

Logistic Regression, Logit Boost

2021

Private

2021

Private

Boosted Tree Algorithms (XGBoost, LightGBM,
CatBoost)
Stacking Model (XGBoost, Logistic Regression, DT,
Naïve Bayes)

2021

2022
2022
2022
2022

2022

2022

2023
2023
2023

2024

SVMs, Bayesian Classifier, RF

Public

Private
Public
Private
Private

Public

Public

Artificial Neural Networks, RF
Decision Forest, Weighted Soft Voting
Multilayer Neural Networks, AdaBoost, RF
CatBoost, Recursive Feature Elimination (RFE)
Clustering (k-means, k-medoids), Gradient
Boosting Trees, DT, RF, Deep Learning,
Naïve Bayes
Hybrid Ensemble Learning, Two-Layer
Flexible Voting
Ensemble Learning, Nelder-Mead Optimization
Weighted Ensemble Model (XGBoost, RF)

Private
Public
Private Weighted Ensemble Model, Powell’s Optimization

Public

Quantum Support Vector Machine, Quantum
k-Nearest Neighbors, and Quantum Decision Tree

Metrics Used

AUC, Expected
Maximum Profit for
Customer Churn
(EMPC)

Profit Maximization

Expected Maximum
Profit for B2B (EMPB)

Accuracy
Accuracy, ROC AUC, PR
AUC, Precision, Recall,
MCC
Accuracy, AUC,
Precision, Recall

Accuracy

Accuracy, Precision,
Recall, F1-score
Accuracy
Accuracy
Accuracy, ROC AUC
Accuracy, F1-score

Accuracy

Accuracy, F1-score

Accuracy
F1-score, Execution Time
Accuracy, F1-score
Accuracy, Precision,
Recall

---

<!-- PAGE 15 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

15 of 38

Table 1. Cont.

Category

Ref.

Year

Dataset

Techniques Used

[34]

[35]

2020

2021

Public

Public

[36]

2021

Public

[37]

2022

Public

Optimization
and
Metaheuristic
ML

Adaptive and
Resampling

Explainable
and
Interpretable

Data-centric
and
Augmentation

Traditional ML

[38]

[39]

[40]

[41]

[42]

[43]

[44]

[45]

[46]

[47]

[48]

[49]

[50]

[51]

[52]

[53]

[54]

[55]

[56]

[57]

[58]
[59]

2022

2023

2023

2023

2023

2022

2023

2023

2024

2021

2022

2024

2021

2023

2023

2024

2020

2022

2023

2023

2024
2024

Optimal Genetic Algorithm (OGA) with SVM
(OGA-SVM), Quantum-Genetic Algorithm
SVMs, Multi-Layer Perceptron, RF, Naïve Bayes,
Feature Selection (Information Gain)
Improved SMOTE (ISMOTE) with an Optimal
Weighted Extreme Learning Machine (OWELM),
Multi-objective Rain Optimization Algorithm
(MOROA)
Principal Component Analysis (PCA),
Autoencoders, Linear Discriminant Analysis
(LDA), t-SNE, XGBoost, LightGBM
Ant Colony Optimization with the Reptile Search
Algorithm (ACO-RSA)
SVMs, Particle Swarm Optimization (PSO),
Artificial Ecosystem Optimization (AEO)
Principal Component Analysis (PCA), Grey Wolf
Optimization (GWO), SVMs
Particle Swarm Optimization, SVMs
Extreme Learning Machine, Grid Search
Optimization

Adaptive Churn Prediction (OTCCD), SMOTE

Naive Bayes, Evolutionary Computation

Hybrid Statistical Modelling

XGBoost, SMOTE-ENN Resampling

Spline-Rule Ensemble, Sparse Group Lasso (SGL)
Shapley Additive Explanations (SHAP)
Explainable AI, Collaborative Filtering

Public

Public

Public

Public

Public

Public

Public

Public

Public

Public

Public

Other

Explainable AI, Social Interaction Analysis

Private

Public

Public

Public

Natural Language Processing, Interpretable ML
Entropy-based Min-Max Similarity (E-MMSIM),
Topic Classification
Synthetic Data Generation, Data-Centric AI
Network-Based Feature Engineering, Gradient
Boosting

Public

CRISP-DM, Logistic Regression, RF

Public

Fisher Discriminant Analysis, Logistic Regression

Private

Logistic Regression with Mixed Penalty

Public

Private
Private

KNN, DTs, Logistic Regression, RF, SVM,
AdaBoost, GBM
RF
DTs, SVMs

Metrics Used

Accuracy, F-score,
Sensitivity

Accuracy

Accuracy, F-measure

AUC, MCC, F1-score,
Kappa

Accuracy

Accuracy

Accuracy, Recall,
F1-score
Accuracy
Accuracy, F1-score,
Modified Accuracy

Accuracy
Precision, Recall,
F1-score
Recall
Accuracy, Precision,
Recall, F1-score

AUC

Accuracy

Interpretability,
Decision-Making

Accuracy
F1-score, AUC,
Accuracy
Accuracy

Accuracy

Accuracy,
Misclassification Rate
Accuracy
Accuracy, Precision,
Recall

Accuracy

F1-score, Recall
Accuracy

6.1. Profit-Centric Approaches

Recent developments in churn prediction research reflect a growing emphasis on
aligning predictive models with business objectives, particularly profitability. Traditionally,
churn models have been optimized for accuracy-based metrics like AUC. Still, a shift
toward integrating financial considerations directly into model training has emerged as
critical for more impactful customer retention strategies.

Höppner et al. [16] exemplify this shift by introducing ProfTree, a profit-driven DT tai-
lored explicitly for churn prediction. Rather than solely optimizing classification accuracy,

---

<!-- PAGE 16 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

16 of 38

ProfTree employs the Expected Maximum Profit for Customer Churn (EMPC) metric to
construct DTs prioritising profitability. The model systematically accounts for misclassi-
fication costs and customer-specific economic value through an evolutionary algorithm.
Experiments on telecommunication datasets demonstrate that ProfTree significantly en-
hances profit compared to conventional accuracy-centric approaches, underscoring the
importance of profit-centric predictive analytics.

Building on similar principles, Maldonado et al. [17] propose a profit-oriented churn
prediction model utilizing Minimax Probability Machines (MPM). Unlike traditional meth-
ods that often use profitability metrics only during post-model selection or threshold
adjustments, this approach directly integrates profit maximization into the classifier’s
training objective. Their framework includes a baseline model and two regularized vari-
ants incorporating LASSO and Tikhonov regularization to ensure robust generalization.
Benchmark evaluations confirm that these profit-driven MPM extensions yield superior
profitability outcomes relative to standard binary classifiers, emphasizing the necessity of
embedding business objectives directly into predictive modeling.

Extending this perspective into the business-to-business (B2B) domain, Janssens
et al. [18] introduce B2Boost, an instance-dependent gradient boosting model explicitly
designed for B2B churn scenarios. Recognizing customer heterogeneity in profitability, they
propose the Expected Maximum Profit for B2B churn (EMPB) metric to guide model train-
ing. B2Boost directly optimizes customer-specific profit rather than traditional classification
accuracy, yielding notable profit improvements over standard approaches. The successful
application in B2B contexts highlights the broader potential of profit-centric methodologies
beyond consumer markets.

These studies underscore the necessity of shifting predictive modeling practices to-
ward profit-centric frameworks. By directly incorporating financial objectives, churn
prediction models become more aligned with strategic business goals, facilitating more
effective and economically beneficial customer retention efforts.

6.2. Ensemble and Hybrid ML Approaches

Ensemble and hybrid approaches have emerged as robust methodologies for enhanc-
ing customer churn prediction across various industries. By integrating multiple classifiers,
clustering techniques, and advanced feature engineering methods, these approaches har-
ness the strengths of individual models to mitigate the limitations of single-algorithm
solutions. This section provides a comprehensive review of key studies that have demon-
strated the effectiveness of ensemble and hybrid learning in churn prediction, highlighting
their contributions to predictive accuracy, model robustness, and real-world applicability.
While both hybrid and ensemble approaches combine multiple models, their integra-
tion strategies differ. Ensemble methods, such as bagging, boosting, and stacking, aim to
improve generalization by aggregating the predictions of several base learners, typically of
the same or different types, without altering the original algorithms. In contrast, hybrid
methods integrate distinct algorithms sequentially or in parallel, where one model’s output
or feature transformation becomes the input for another. For example, a hybrid model
might use clustering for customer segmentation, followed by classification within each
segment, or combine feature engineering via CNNs with temporal modeling via LSTMs.
Hybrid systems are generally more customized and often domain-specific, whereas en-
semble methods follow standardized combining rules like majority voting or weighted
averaging.

One notable study by Liu et al. [28] introduces a hybrid approach that integrates
clustering and classification algorithms to improve predictive accuracy in the telecom
sector. Their model employs k-means, k-medoids, and random clustering techniques

---

<!-- PAGE 17 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

17 of 38

alongside classifiers such as Gradient Boosting Trees (GBT), DTs, RFs, DL, and Naïve Bayes
(NB). The study reports significant performance improvements by leveraging stacking-
based hybridization, with 96% and 93.6% accuracy on the Orange and Cell2Cell datasets.
These results emphasize the benefits of ensemble learning and clustering-based feature
enhancement in churn prediction. Similarly, Ramesh et al. [24] propose a hybrid model
combining ANNs and RFs to enhance churn prediction in telecommunications. Their ANN
architecture, consisting of four hidden layers, achieved 90.34% accuracy, outperforming
standalone RF and simpler ANN models. Integrating ANN’s predictive power with RF’s
robustness effectively identifies churn factors, aiding telecom companies in proactive
customer retention strategies.

Using hybrid approaches, Usman-Hamza et al. [25] introduce Intelligent Decision
Forest (DF) models to address scalability issues and class imbalance in telecom churn
prediction. Their approach significantly enhances classification accuracy by incorporating
Logistic Model Tree (LMT), RF, and Functional Trees (FT) within a weighted soft voting and
stacking framework. The study underscores the potential of decision forest-based models in
handling imbalanced datasets and improving churn detection across telecommunications.
Saias et al. [26] focus on churn prediction within cloud service providers, emphasizing
the importance of early detection in mitigating customer loss and optimizing resource
allocation. Their ML framework evaluates multilayer neural networks, AdaBoost, and RF
models, with RF emerging as the most effective, achieving an accuracy of 98.8% and an
AUC score of 0.997. These findings reinforce the relevance of ensemble learning in dynamic
service industries.

In the context of the webcasting industry, Fu et al. [30] employ an ensemble learning-
based churn prediction model optimized by the Nelder-Mead algorithm. Their approach
extracts high-dimensional behavioural features from time-series data, introducing a novel
churn indicator to enhance label accuracy. The study demonstrates superior operational
efficiency and outperformance of traditional ensemble models, offering actionable insights
for customer retention strategies.

Optimization techniques have also been explored to refine ensemble methods. Khoh
et al. [32] introduce an optimized weighted ensemble model tailored for the telecommuni-
cations industry, integrating Powell’s optimization algorithm to assign differential weights
to base learners based on their predictive strength. This model achieves an accuracy of
84% and an F1-score of 83.42%, surpassing conventional ML approaches. Yogesh et al. [29]
further contribute to this domain by proposing a two-layer flexible voting ensemble, demon-
strating the impact of data balancing on improving classification performance.

Boosted tree models have gained traction in various industries for their efficiency in
churn prediction. Maretta et al. [21] explore the use of XGBoost, LightGBM, and CatBoost in
banking churn prediction, finding LightGBM to be the most effective with 91.4% accuracy,
94.8% AUC, and 87.7% recall. Similarly, Tianpei et al. [22] implement a stacking-based
ensemble framework combining XGBoost, Logistic Regression, DTs, and Naïve Bayes,
achieving 98.09% accuracy by incorporating feature grouping techniques.

A novel direction in ensemble learning is explored by Arshad et al. [33], who in-
troduce Q-Ensemble Learning, a quantum-enhanced ensemble approach incorporating
Quantum Support Vector Machine (Q-SVM), Quantum k-Nearest Neighbors (Q-kNN), and
Quantum Decision Tree (QDT). By integrating blockchain technology for data security and
transparency, their model outperforms classical ensemble models, achieving 15% higher
accuracy and 12% higher precision, demonstrating the transformative potential of quantum
computing in churn prediction.

Ensemble methods have also been applied to e-commerce churn prediction. Ishrat
et al. [27] present an AI-driven framework that combines model tuning, feature selection,

---

<!-- PAGE 18 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

18 of 38

and comparative analysis, achieving 100% accuracy and F1-score using CatBoost. Manohar
et al. [23] investigate a collective data mining approach integrating SVMs, Bayesian Clas-
sifiers, and RF, highlighting the benefits of combining multiple classifiers for improved
accuracy and recall.

Other studies have focused on refining traditional ensemble techniques. Mahayasa
et al. [31] propose a weighted average ensemble combining XGBoost and RF, demonstrating
superior predictive performance in the telecom and insurance sectors, with an F1-score
of 0.850 and 0.947, respectively. Hemlata et al. [20] explore Logistic Regression and Logit
Boost for telecom churn prediction, confirming the efficacy of boosting techniques in
outperforming conventional regression models.

Finally, Wang et al. [19] provide a comparative analysis of widely used classification
algorithms for churn prediction, reinforcing the importance of ensemble learning in enhanc-
ing model performance. Their benchmarking study offers valuable guidance for businesses
seeking data-driven retention strategies.

These studies illustrate ensemble and hybrid approaches’ diverse and practical appli-
cations in customer churn prediction. By integrating multiple ML models and leveraging
sophisticated feature engineering techniques, these methodologies provide robust, scal-
able, and high-performing solutions to the complex challenge of customer retention across
various industries.

6.3. Optimization and Metaheuristic Approaches

Optimization and metaheuristic approaches have gained prominence in churn pre-
diction research as effective strategies for enhancing model performance and reducing
computational complexity. These studies offer robust frameworks that improve predictive
accuracy and provide greater interpretability and actionable insights by integrating ad-
vanced feature selection techniques, hyperparameter tuning, and metaheuristic algorithms.
This section reviews key contributions that employ these techniques to optimize churn
prediction models across various domains.

Feature selection plays a critical role in improving model efficiency and accuracy.
Saheed et al. [35] introduce an ML-based churn prediction framework for the telecom-
munications sector, leveraging Information Gain and Ranker-based feature selection to
enhance model interpretability. Their approach, which incorporates SVM, Multi-Layer Per-
ceptron (MLP), RF, and Naïve Bayes, achieves a 95.02% accuracy rate, surpassing the 92.92%
obtained without feature selection. These results highlight the importance of selecting
relevant churn-related attributes for improved classification performance.

Building on feature selection techniques, Al-Shourbaji et al. [38] propose a novel
hybrid method, ACO-RSA, which integrates Ant Colony Optimization (ACO) with the
Reptile Search Algorithm (RSA) to enhance predictive performance. Evaluated across
multiple open-source churn datasets, ACO-RSA outperforms Particle Swarm Optimization
(PSO), Multi-Verse Optimizer (MVO), and Grey Wolf Optimizer (GWO), demonstrating
its effectiveness in handling high-dimensional telecom data. This study underscores the
potential of metaheuristic approaches in refining feature selection for improved churn
detection.

Pustokhina et al. [36] introduce the ISMOTE-OWELM model, which integrates Im-
proved SMOTE (ISMOTE) for data balancing with an Optimal Weighted Extreme Learning
Machine (OWELM) for classification. A Multi-objective Rain Optimization Algorithm
(MOROA) optimizes sampling rates and model parameters, yielding 94%, 92%, and 90.9%
accuracy across three telecom datasets, significantly surpassing traditional approaches. The
study emphasizes the effectiveness of ISMOTE-OWELM in improving churn detection

---

<!-- PAGE 19 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

19 of 38

while maintaining computational efficiency, making it a valuable tool for telecom providers
aiming to enhance customer retention efforts.

Incorporating hyperparameter tuning into feature selection, Mirabdolbaghi et al. [37]
present a comprehensive model optimization framework integrating Principal Component
Analysis (PCA), Autoencoders, Linear Discriminant Analysis (LDA), t-SNE, and XGBoost
for feature reduction. Their approach employs Bayesian and genetic optimization to fine-
tune LightGBM models, significantly outperforming AdaBoost, SVM, and DT classifiers.
The study also utilizes SHAP for feature importance interpretation and introduces a Cus-
tomer Lifetime Value (CLV) ranking system, offering actionable insights for prioritising
high-value customers at risk of churn.

Koço ˘glu et al. [42] present an Extreme Learning Machine approach for customer churn
prediction, optimized using grid search for hyperparameter tuning. The study utilizes a
churn dataset from the UCI Machine Learning Repository and compares ELM’s perfor-
mance against Naïve Bayes, k-Nearest Neighbor, and SVM models. The results demonstrate
that ELM achieves the highest accuracy of 93.1%, highlighting its efficiency in churn pre-
diction due to minimal parameter tuning requirements and competitive performance. The
study underscores ELM’s potential as a robust and effective technique for churn analysis.
Metaheuristic optimization has also been explored to enhance gradient boosting tech-
niques. AlShourbaji et al. [39] propose the Enhanced Gradient Boosting Model (EGBM),
which integrates an SVM RBF base learner with PSO and Artificial Ecosystem Optimization
(AEO) for hyperparameter tuning. Evaluated on seven telecom datasets, EGBM demon-
strates superior predictive capabilities compared to traditional GBM and SVM models,
effectively addressing premature convergence and enhancing customer retention strategies.
Hybrid optimization approaches further improve churn prediction efficiency. Kurtcan
et al. [40] introduce PCA-GWO-SVM, a model combining Principal Component Analysis
(PCA) for feature selection, Grey Wolf Optimization for hyperparameter tuning, and SVM
for classification. Compared to logistic regression, k-nearest neighbors, naïve Bayes, and
DTs, PCA-GWO-SVM achieves higher accuracy, recall, and F1-score, reinforcing the value
of combining optimization techniques with classification frameworks.

Ponnusamy et al. [41] employ a PSO-SVM-based algorithm to enhance churn predic-
tion performance in the banking sector. By optimizing hyperparameters using Particle
Swarm Optimization, their approach significantly outperforms traditional SVM models,
demonstrating the effectiveness of hybrid optimization strategies for financial institutions
seeking to minimize customer attrition. Similarly, Venkatesh et al. [34] propose an Optimal
Genetic Algorithm (OGA) with SVM for cloud-based churn prediction. Their approach
utilizes a double-chain quantum genetic algorithm to fine-tune SVM hyperparameters,
achieving high sensitivity (94.50), accuracy (90.27), and an F-score of 94.30. These findings
underscore the effectiveness of genetic optimization in enhancing predictive performance,
making it a promising technique for large-scale cloud-based analytics.

These studies illustrate how optimization and metaheuristic approaches significantly
improve churn prediction models’ accuracy, efficiency, and interpretability. By integrat-
ing advanced feature selection, hyperparameter tuning, and metaheuristic optimization,
these methodologies provide scalable and high-performing solutions for industries grap-
pling with complex customer data, ultimately enhancing retention strategies and business
decision-making.

6.4. Adaptive and Resampling Approaches

In dynamic environments where customer behaviour and data distributions con-
tinuously evolve, addressing class imbalance and adapting to concept drift are critical
challenges in churn prediction. Researchers have increasingly turned to resampling and

---

<!-- PAGE 20 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

20 of 38

adaptive learning strategies to enhance model performance in real-time applications. This
section reviews key studies that employ these techniques to mitigate imbalances and adapt
predictive models to changing data patterns, ensuring more accurate and reliable churn
detection.

Ahmad et al. [43] introduce the Optimized Two-Sided Cumulative Sum Churn Detec-
tor (OTCCD), a novel adaptive churn prediction framework for telecom data streams. By
integrating the Synthetic Minority Over-sampling Technique (SMOTE) for data balancing
and a cumulative sum control chart for drift detection, OTCCD efficiently identifies shifts
in customer behaviour within a sliding window framework. Experimental evaluations
on real-world telecom datasets, such as Call Detail Records, demonstrate that OTCCD
outperforms traditional methods by providing higher accuracy and faster drift detection.
This study highlights the importance of real-time adaptability in churn prediction models,
offering telecom companies a robust tool for proactive customer retention strategies.

Adnan et al. [44] propose an adaptive learning approach that integrates evolutionary
computation with a Naïve Bayes classifier to address class imbalance in telecommunications
churn prediction. By dynamically adjusting model parameters based on incoming data
patterns, the hybrid method significantly improves precision, recall, and F1 scores compared
to traditional approaches. Evaluations on real-world telecom datasets confirm the model’s
effectiveness in proactively identifying at-risk customers, underscoring the potential of
adaptive learning in minimizing revenue loss due to customer churn.

Complementing adaptive methodologies, Shimaa et al. [46] develop a hybrid churn
prediction framework that combines XGBoost with SMOTE-ENN resampling to balance
datasets and improve classification accuracy. This integration enhances precision, recall,
and F1 scores, outperforming conventional ML techniques across three telecom datasets.
By effectively addressing class imbalance and leveraging ensemble learning, the model
facilitates proactive retention strategies, reinforcing the role of resampling techniques in
churn prediction.

Incorporating a more customer-centric approach, Lee et al. [45] propose a hybrid
churn prediction framework that dynamically models churn probability based on customer
lifetime value rather than fixed periods. By segmenting customers into groups such as
new, short-term, high-value, and churn-prone users, their methodology applies tailored
ML models to enhance predictive accuracy. Evaluations of datasets from a U.K. gift seller
and Pakistan’s most significant e-commerce platform show recall scores ranging from 0.56
to 0.72 in one case and 0.91 to 0.95 in another. The study highlights the advantages of
integrating statistical modeling with ML techniques to refine customer retention strategies
while reducing data requirements.

These studies illustrate how adaptive and resampling approaches effectively address
class imbalance and concept drift, enabling more scalable and robust churn prediction
solutions. By integrating real-time learning, resampling techniques, and evolutionary opti-
mization, these methodologies provide powerful tools for businesses seeking to enhance
customer retention strategies in evolving market conditions.

6.5. Explainable and Interpretable Approaches

Understanding the underlying decision processes in complex predictive tasks such as
churn prediction is crucial for gaining stakeholder trust and facilitating actionable insights.
Recent research has increasingly focused on integrating interpretability and explainable
AI techniques into churn prediction models. This section reviews key contributions that
enhance model transparency through rule-based formulations, SHAP analyses, and other
XAI methodologies.

---

<!-- PAGE 21 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

21 of 38

De Bock et al. [47] introduce Spline-Rule Ensemble classifiers with Structured Spar-
sity Regularization (SRE-SGL) as an interpretable approach to customer churn prediction.
While traditional ML models often prioritise predictive accuracy, this study emphasizes the
need for explainable models that provide actionable insights into customer behaviour. The
proposed spline-rule ensembles integrate tree-based ensemble methods with regression
analysis, balancing model flexibility and simplicity. However, conventional rule-based
ensembles can become excessively complex due to conflicting components. To address this,
the authors incorporate Sparse Group Lasso regularization, which enhances interpretability
by enforcing structured sparsity. Evaluations across fourteen real-world datasets demon-
strate that SRE-SGL outperforms standard rule ensembles in AUC and top decile lift while
maintaining competitive predictive performance. A case study in the telecommunications
sector further illustrates the model’s interpretability, reinforcing the value of structured
regularization in making churn prediction both effective and explainable.

Extending interpretability techniques to workforce analytics, Mitravinda et al. [48]
investigate employee attrition prediction using ML models and XAI methodologies. Their
study applies SHAP to identify key factors driving attrition and visualize their impact.
Additionally, the research introduces a recommendation system leveraging user-based
collaborative filtering to propose personalized retention strategies. By combining predictive
modeling with actionable insights, this study demonstrates how XAI techniques can inform
more effective employee retention policies.

In digital entertainment, Wang et al. [49] address the challenge of player churn pre-
diction in online video games, where understanding social interaction dynamics is critical.
While ML models are widely used for player behaviour analysis, their black-box nature
limits adoption by product managers and game designers. The study restructures model
inputs into explicit and implicit features to bridge this gap, enhancing expert interpretabil-
ity. Furthermore, the research highlights the necessity of XAI techniques that explain
feature contributions and provide actionable recommendations for reducing churn. The
proposed approach is validated through two case studies involving expert feedback and a
within-subject user study, demonstrating its effectiveness in improving decision-making
for player retention strategies.

Together, these studies illustrate the crucial role of interpretability in churn prediction
models. By integrating advanced XAI techniques, researchers bridge the gap between high
predictive performance and the need for transparent, actionable insights. This integra-
tion supports more informed and effective retention strategies across diverse industries,
reinforcing the value of explainable AI in real-world predictive analytics.

6.6. Data-Centric and Augmentation Approaches

Beyond refining predictive models, recent research in churn prediction has increasingly
emphasized enhancing the quality and diversity of training data. Data-centric and augmen-
tation approaches seek to enrich traditional datasets by incorporating novel data sources,
generating synthetic data, and leveraging advanced feature engineering techniques. These
strategies are crucial for improving model robustness, addressing data imbalances, and
achieving higher predictive accuracy. This section reviews key contributions that exemplify
these efforts.

Vo et al. [50] explore a novel churn prediction approach that integrates unstructured
call log data with traditional structured data. While existing ML models primarily rely
on demographic and account history data, this study highlights the untapped potential of
analyzing spoken content from customer interactions. Using natural language processing
techniques, the authors process a large-scale call center dataset containing two million calls
from over 200,000 customers. Their findings demonstrate that incorporating unstructured

---

<!-- PAGE 22 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

22 of 38

call data significantly enhances prediction accuracy while providing deeper insights into
customer behaviour. Additionally, interpretable ML techniques extract personality traits
and customer segmentation patterns, facilitating personalized retention strategies. This
study underscores the importance of combining structured and unstructured data sources
to develop more comprehensive churn prediction frameworks in the financial services
industry.

Soumi et al. [51] address the challenge of optimizing training data quality through a
representation-based query strategy for churn prediction. Given manual data annotation’s
high cost and inefficiency, the authors propose Entropy-based Min-Max Similarity (E-
MMSIM), an active learning algorithm inspired by protein sequencing techniques. This
method selects the most informative and representative data points for annotation, reducing
redundancy and improving model efficiency. The approach enhances topic classification
accuracy in customer service messages, yielding significant improvements in F1-score, AUC,
and overall model performance. Moreover, when these qualitative features are integrated
with structured customer data, churn prediction models achieve a 5% performance gain.
The study highlights the critical role of data selection strategies in optimizing ML workflows
for customer retention management.

In the realm of synthetic data generation, Wang et al. [52] explore the impact of data-
centric AI on churn prediction. Unlike traditional model-centric AI, which focuses on
hyperparameter tuning and algorithm modifications, data-centric AI enhances predictive
performance by improving training data quality and distribution. This research evaluates
various data synthesis algorithms, examining their effects on data balancing, augmenta-
tion, and substitution. The findings underscore the potential of resampling methods in
mitigating class imbalance and improving model robustness, providing valuable insights
for AI-driven churn prediction frameworks across industries.

Babak et al. [53] introduce a social network-based churn prediction model, recognizing
that social interactions and peer behaviour often influence customer churn. The study devel-
ops a feature engineering approach incorporating influence and conformity indices derived
from call network data. By integrating social connectivity metrics, the model significantly
enhances the predictive power of standard ML classifiers, particularly gradient boosting
models. This research demonstrates that churn is not solely an individual decision but is
shaped by broader social dynamics. This perspective extends beyond telecommunications
to various industries where peer influence affects customer behaviour.

Collectively, these studies illustrate the transformative impact of data augmentation
and quality improvement in churn prediction. Researchers are developing more compre-
hensive and robust predictive frameworks by incorporating novel data sources, employing
active learning for data selection, generating synthetic data, and leveraging social network
information. These advancements enhance model accuracy and provide deeper insights
into customer behaviour, enabling more effective and proactive retention strategies.

6.7. Traditional ML Approaches

Traditional machine learning approaches significantly influence churn prediction
by leveraging established statistical and algorithmic techniques. These methods rely on
classical models and feature engineering to derive actionable insights and achieve high
predictive accuracy. This section highlights key studies that exemplify the application of
conventional ML methodologies across diverse domains.

Tianyuan et al. [55] present a data-driven approach to customer churn prediction in
telecommunications, incorporating customer segmentation to enhance predictive accuracy.
Using Fisher discriminant analysis and logistic regression, their model achieves a 93.94%
accuracy rate on telecom datasets, effectively identifying potential churners. Tailoring

---

<!-- PAGE 23 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

23 of 38

predictions to specific customer groups enhances the precision of retention campaigns,
providing telecom operators with a powerful tool to proactively reduce churn and improve
profitability. The study underscores the significance of segmentation in refining churn
prediction models.

Expanding on customer relationship management (CRM) applications, Šimovi´c
et al. [56] explore churn prediction using big data analytics to analyze heterogeneous
customer behaviours, such as self-care service usage, service duration, and responsive-
ness to marketing efforts. Their study introduces an enhanced logistic regression model
with a mixed penalty term to mitigate overfitting and balance feature selection. Empirical
evaluation on a large CRM dataset demonstrates high classification performance across
standard metrics, reinforcing the potential of penalized logistic regression as a scalable and
computationally efficient approach to churn modeling in big data environments.

Jakob et al. [58] extend traditional ML techniques to the digital health sector, investigat-
ing early user churn in a weight loss app. By analyzing engagement data from 1283 users
and 310,845 event logs, the study employs an RF model to predict user dropout based on
daily login counts. Achieving an F1 score of 0.87 on day 7 and identifying 93% of churned
users, the study highlights how churn prediction can enable personalized retention strate-
gies in digital health interventions, ultimately improving long-term user engagement and
health outcomes.

Returning to the telecommunications industry, Sikri et al. [59] developed an ML-based
approach for improving customer retention. By analyzing customer demographics, usage
patterns, and service details, the study applies DTs and SVM to identify customers at
risk of churning. The results demonstrate high predictive accuracy, empowering telecom
companies to implement targeted retention strategies effectively. This study reaffirms the
value of conventional ML techniques in customer retention efforts.

Expanding on real-time prediction applications, Nyashadzashe et al. [54] developed a
churn prediction model tailored for the telecommunications industry, specifically focusing
on prepaid customers who frequently switch providers. Using Watson Studio, their study
employs big data analytics within the CRISP-DM framework and evaluates three ML
algorithms—Logistic Regression, RF, and DT. While Logistic Regression exhibited the
lowest misclassification rate (2.2%), RF and DT achieved relatively high accuracy rates
(78.3% and 79.2%, respectively) but suffered from misclassification rates above 20%. This
research underscores the limitations of relying solely on accuracy metrics and advocates
for more comprehensive evaluation techniques to enhance real-time churn prediction
performance.

Beyond customer churn, AbdElminaam et al. [57] introduce EmpTurnoverML, an
AI-driven approach for predicting employee turnover and customer churn using ML algo-
rithms. The study evaluates various classification techniques, including K-Nearest Neigh-
bors, DTs, Logistic Regression, RF, SVM, AdaBoost, Naïve Bayes, and Gradient Boosted
Machines (GBM), using an 80-20 train-test split. By identifying key patterns associated with
employee departures, the study highlights how AI-powered prediction models can help
organizations implement proactive retention strategies, reducing hiring and training costs
while enhancing workforce stability. The findings demonstrate the broader applicability of
churn prediction methodologies in workforce analytics and business efficiency.

These studies illustrate the continued relevance of conventional ML approaches in
churn prediction. Through rigorous model development and strategic feature engineering,
these methodologies provide potent tools for organizations seeking to mitigate churn,
improve customer and employee retention, and drive sustainable business growth. Overall,
traditional ML methods such as decision trees, logistic regression, and support vector
machines remain valued for their interpretability, computational efficiency, and ease of

---

<!-- PAGE 24 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

24 of 38

deployment. However, they may struggle with high-dimensional or sequential data, and
their performance is often limited compared to more advanced ensemble approaches.

7. Deep Learning Approaches

Deep learning techniques have significantly advanced churn prediction by offering di-
verse methodologies that address complex user behaviour patterns and industry retention
challenges. Recent advancements include deep reinforcement learning, sequential mod-
eling with architectures like LSTMs, hybrid and ensemble methods integrating multiple
DL paradigms, CNNs tailored for structured data, efficient feedforward neural networks,
and innovative representation learning and feature interaction models. Each category
provides unique strengths, such as improved accuracy, enhanced interpretability, or com-
putational efficiency, collectively supporting proactive and effective churn management
strategies. This section explores these distinct approaches, highlighting their applications,
advantages, and contributions to predictive analytics. Table 2 highlights the datasets used
(public, private, simulation-based), DL techniques implemented, and performance metrics
evaluated.

Table 2. The summary of the studies in the domain of DL.

Category

Ref.

Year

Dataset

Techniques Used

Metrics Used

Deep Reinforcement
Learning

[60]

[61]

[62]

2020

Simulation

Deep Reinforcement Learning

Accuracy

2020

2020

Public

Public

Trajectory-based LSTM (TR-LSTM)

LSTM-based Dynamic Churn Model

Temporal and
Sequential DL

[63]

2024

Private

LSTM and Gated Recurrent Unit (GRU)
networks, LightGBM, SHAP, Explainable
Boosting Machines (EBM)

[64]

2024

Public

LSTM

[65]

2022

Private

Ensemble and
Hybrid DL

[66]

2023

Private

Attentional DL model (AttnBLSTM-CNN)
integrated with Bidirectional LSTMs
(BiLSTM) and CNNs
Stacked Bidirectional LSTMs (SBLSTM)
and RNNs with an arithmetic optimization
algorithm (AOA), Improved Gravitational
Search Optimization Algorithm (IGSA)
K-Means Clustering, Self-Attention LSTM

[67]

[68]

2023

2024

Public

Private

Stacked DNNs, Logistic Regression

[69]

2021

Public

Comparative CNNs, LSTMs

CNN–based

Feedforward Deep
Neural Network

NLP-based DL

Representation and
Feature Interaction

[70]

[71]

[72]

[73]

[74]

[75]
[76]

2022

2024

2020

2024

2021

2020
2021

Private

Public

Public

Public

Private

Public
Public

CNNs, Extended Convolutional Decision
Trees (ECDT) integrated with Grid Search
Optimization
1D CNN, Residual Blocks, Attention

DNN, RF, XGBoost
Multi-Layer Perceptron, Radial Basis
Function (RBF) Networks

NLP, RNNs

Feature Interaction Network (FIN)
Vector Embeddings for Churn

ROC AUC
AUC, F1-Score,
Log Loss, Lift,
EMPC

AUC, F1-score

Accuracy,
Precision, Recall,
F1-score

F1-score, ROC
AUC

Accuracy

AUC, F1-score
Accuracy,
Precision, Recall,
F1-score

Accuracy, ROC
AUC, G-Mean

Accuracy

Accuracy

Accuracy

Accuracy

F1-score

Accuracy
F1-score

---

<!-- PAGE 25 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

25 of 38

7.1. Deep Reinforcement Learning Approaches

Deep reinforcement learning approaches represent an emerging paradigm in churn
prediction, particularly within dynamic environments such as digital entertainment. These
methods go beyond traditional supervised learning by leveraging simulation-based tech-
niques to model complex user behaviours and engagement dynamics. This section high-
lights a pioneering study that exemplifies the potential of deep reinforcement learning in
addressing churn challenges in mobile gaming.

Roohi et al. [60] introduce a novel simulation-based model for predicting churn in
mobile gaming. Unlike traditional supervised ML models that rely on historical player
data, this work integrates Deep Reinforcement Learning to simulate AI-driven gameplay
behaviour, capturing in-game difficulty and player skill evolution. A key strength of
this approach is its ability to model player persistence and engagement dynamics without
requiring extensive real-world behavioural data. The study demonstrates that incorporating
a population-level simulation of player heterogeneity improves churn prediction accuracy,
thereby reducing the dependency on expensive retraining of DRL agents. This framework
offers a promising direction for churn analysis in digital entertainment, where player
retention strategies are critical for revenue sustainability.

7.2. Temporal and Sequential DL Approaches

Temporal and sequential DL approaches have emerged as essential tools for capturing
the dynamic nature of customer behaviour in churn prediction. By leveraging temporal
dependencies inherent in user engagement data, these models enable a more nuanced
understanding of churn patterns, ultimately leading to more effective retention strategies.
This section reviews recent studies that utilize deep sequential architectures, such as LSTM
networks, to enhance churn prediction performance.

Joy et al. [63] present a hybrid DL approach that integrates sequential modeling with
explainable AI to improve churn prediction in streaming services. The proposed framework
combines LSTM and Gated Recurrent Unit (GRU) networks to capture temporal trends in
user engagement, complemented by LightGBM to refine predictive performance. A key
contribution of this study is its emphasis on interpretability, employing Shapley Additive
Explanations and Explainable Boosting Machines (EBM) to provide transparency in feature
importance rankings. By ensuring that decision-makers understand the reasoning behind
churn predictions, the model enhances actionable insights for business applications. The
study reports state-of-the-art performance, achieving a 95.60% AUC and a 90.09% F1 score,
reinforcing the effectiveness of hybrid architectures in churn analysis.

Expanding on sequential DL techniques, Zhu et al. [61] introduce a trajectory-based
LSTM framework (TR-LSTM) for churn prediction, which extracts three trajectory-based
features from customer movement data. The model significantly outperforms traditional
methods, demonstrating the utility of spatiotemporal behaviour analysis in predicting
churn. Similarly, Alboukaey et al. [62] emphasize the importance of daily behavioural
patterns by developing an LSTM-based dynamic churn prediction model for mobile telecom
customers. Unlike conventional monthly-based models, this approach captures short-
term fluctuations in customer activity, enhancing prediction accuracy and allowing for
more timely interventions. These findings underscore the superiority of LSTM-based
architectures in modeling evolving user engagement patterns, particularly in dynamic
service industries.

Further validating the effectiveness of LSTMs, Beltozar-Clemente et al. [64] demon-
strate that deep sequential networks can overcome vanishing gradient issues and effectively
model long-term dependencies in customer behaviour sequences. Their study achieves 95%

---

<!-- PAGE 26 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

26 of 38

performance across multiple evaluation metrics, highlighting the potential of LSTM-based
models to refine churn prediction by capturing complex behavioural trends.

Collectively, these studies establish sequential and temporal DL approaches as robust
tools for churn prediction. By leveraging LSTM-based architectures, these models offer
enhanced predictive accuracy, more profound insights into user behaviour, and timely
interventions, making them invaluable for developing proactive retention strategies across
various industries.

7.3. Ensemble and Hybrid DL Approaches

Ensemble and Hybrid DL approaches have gained significant traction in churn predic-
tion due to their ability to combine multiple models’ strengths and overcome individual
architectures’ limitations. These approaches achieve enhanced predictive accuracy and
improved generalization across diverse application domains by integrating DL techniques,
such as RNNs, CNNs, and attention mechanisms, with ensemble methods and optimization
algorithms. This section highlights key studies that exemplify the effectiveness of hybrid
and ensemble strategies in churn prediction.

Jajam et al. [66] introduce an ensemble model that integrates Stacked Bidirectional
LSTMs (SBLSTM) and RNNs with an arithmetic optimization algorithm (AOA). The frame-
work is fine-tuned using an improved Gravitational Search Optimization Algorithm (IGSA),
achieving a state-of-the-art accuracy of 97.89% in the insurance domain. These results high-
light the potential of ensemble architectures to effectively merge multiple DL techniques,
improving generalization and performance in churn prediction tasks.

Similarly, Liu et al. [65] present a fused attentional DL model (AttnBLSTM-CNN) that
integrates Bidirectional LSTMs (BiLSTM) and CNNs to address the limitations of standalone
RNNs and CNNs. By incorporating an attention mechanism, the model enhances prediction
accuracy by prioritising critical customer behaviour patterns. The study demonstrates
that integrating attention layers into DL pipelines improves churn detection accuracy and
enhances interpretability, providing valuable insights for financial institutions.

Expanding on hybrid architectures in the financial sector, Van-Hieu et al. [68] propose
a DL ensemble model for customer churn prediction in banking. The approach employs
a stacked DL architecture where Level 0 integrates three distinct deep neural networks,
and Level 1 utilizes a logistic regression model for final prediction. Tested on the Bank
Customer Churn Prediction dataset, the framework achieves 96.60% accuracy, 90.26%
precision, 91.91% recall, and an F1-score of 91.07%. These results highlight the robustness
of combining DL models with logistic regression to improve churn prediction accuracy,
reinforcing the value of ensemble methodologies in financial customer retention strategies.
Zhao et al. [67] further enhance churn prediction by integrating unsupervised and
supervised learning techniques. Their hybrid model incorporates K-means clustering,
entropy-based methods, and customer portrait analysis for segmenting telecom customers.
A multi-head self-attention-based nested LSTM classifier is then applied to evaluate cus-
tomer behaviour. Tested on China’s telecom market data, the model outperforms traditional
classification methods by improving the accuracy of customer behaviour recognition. Ad-
ditionally, it effectively differentiates between medium-value and high-value customers,
providing critical insights for precision marketing strategies and enabling telecom compa-
nies to tailor service offerings more effectively.

Collectively, these studies illustrate that hybrid and ensemble DL approaches enhance
predictive accuracy and improve model interpretability and generalization across sectors.
Their innovative integration of diverse methodologies offers promising avenues for devel-
oping robust, scalable churn prediction systems that effectively support targeted retention
strategies.

---

<!-- PAGE 27 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

27 of 38

7.4. CNN–Based Approaches

Convolutional Neural Networks have emerged as a powerful tool in churn prediction,
particularly for tasks requiring complex feature extraction and hierarchical data represen-
tation. While traditionally applied to image and text processing, CNN-based approaches
have proven effective in structured data scenarios, offering improved predictive accuracy
and addressing challenges such as class imbalance and information loss. This section
reviews key studies that leverage CNNs—often in combination with other techniques—to
enhance churn prediction models.

Muhammad et al. [69] compare DL architectures on benchmark datasets such as
Cell2Cell and KDD Cup for churn prediction. Their findings identify CNNs as the most
effective model based on multiple evaluation criteria, outperforming traditional ML algo-
rithms and DL models. These results underscore the ability of convolutional architectures
to capture hierarchical relationships within customer data, particularly in scenarios where
feature extraction poses significant challenges.

Extending CNN applications to workforce analytics, Ebru et al. [70] introduce a
hybrid model (ECDT-GRID) for employee churn prediction. This approach integrates
Extended Convolutional Decision Trees (ECDT) with grid search optimization to enhance
classification accuracy. Unlike conventional CNN applications in image and text processing,
this study adapts CNNs for structured numerical data, addressing information loss through
DT-based learning. The ECDT-GRID model outperforms CNN, ECDT, and traditional ML
models, demonstrating the importance of hyperparameter tuning in improving predictive
performance. The study highlights the potential of DL in workforce analytics, particularly
in retail, where employee churn impacts operational stability. By combining CNNs with
DT structures, this approach provides a robust predictive framework, showcasing the role
of DL in optimizing employee retention strategies.

Saha et al. [71] introduce ChurnNet, a novel DL-based churn prediction model tai-
lored for the telecommunications industry (TCI). Recognizing the importance of customer
retention in a competitive market, the study aims to enhance predictive accuracy beyond
existing methods. ChurnNet integrates a 1D convolutional layer with residual blocks,
squeeze-and-excitation blocks, and a spatial attention module, allowing the model to cap-
ture complex feature dependencies while mitigating the vanishing gradient problem. The
model is evaluated using three public datasets, each exhibiting significant class imbal-
ance, which is addressed through SMOTE, SMOTEEN, and SMOTETomek resampling
techniques. Rigorous experimentation, including 10-fold cross-validation, demonstrates
that ChurnNet outperforms state-of-the-art models, achieving accuracy scores of 95.59%,
96.94%, and 97.52% across the three datasets. These findings emphasize the potential of DL
architectures with attention mechanisms in advancing churn prediction models, making
them more effective and interpretable for telecom service providers.

These studies highlight the versatility and strength of CNN-based approaches in
churn prediction. By addressing challenges such as feature extraction, information loss,
and class imbalance, CNNs and their hybrid variants provide robust frameworks that can
be adapted to various applications—from customer retention in telecom to employee churn
in retail—underscoring their critical role in modern predictive analytics.

7.5. Feedforward Deep Neural Network Approaches

Feedforward deep neural network approaches remain widely used in churn prediction
because they can learn complex nonlinear relationships directly from data while maintain-
ing relatively straightforward architectures. These methods, including Extreme Learning
Machines, Multi-Layer Perceptrons, and Deep Neural Networks, balance predictive perfor-

---

<!-- PAGE 28 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

28 of 38

mance and computational efficiency. This section reviews key studies that have leveraged
these architectures to achieve robust churn prediction outcomes.

Małgorzata et al. [73] evaluate Multi-Layer Perceptron and Radial Basis Function (RBF)
networks for churn prediction in mobile telecommunications. Their findings suggest that
MLPs achieve near-perfect accuracy (0.999), significantly outperforming traditional fuzzy
rule-based and rough-set systems. However, the study also acknowledges the black-box
nature of neural networks, emphasizing the need for explainability in DL models to support
real-world adoption. These insights highlight the trade-off between model performance
and interpretability, an ongoing challenge in deploying DL solutions for churn prediction.
Setyo [72] investigates churn prediction in the telecommunications sector using Deep
Neural Networks, comparing their performance against RF and XGBoost. Recognizing the
critical impact of customer attrition on business retention, the study incorporates feature
selection techniques and evaluates model efficiency using Google Colaboratory with a
TensorFlow backend. The results indicate that DNN achieves 80.62% accuracy in just 68 s,
outperforming XGBoost (76.45% accuracy, 175 s) and RF (77.87% accuracy, 529 s). These
findings highlight DNN’s ability to balance accuracy and computational efficiency, making
it a promising alternative for real-time churn prediction in telecommunications.

These studies underscore the potential of feedforward and standard deep neural
network approaches to provide robust and efficient churn prediction solutions. At the
same time, they highlight the ongoing need to improve model interpretability to enhance
adoption and usability in practical business applications.

7.6. NLP–Based DL Approaches

NLP-based deep learning approaches represent an innovative frontier in churn predic-
tion by leveraging unstructured textual data to complement traditional numerical inputs.
These methods harness advanced language models and RNNs to extract meaningful
insights from customer communications, enriching predictive analytics and enhancing
retention strategies. This section highlights a key study that exemplifies the potential of
NLP-driven churn prediction.

Ozan [74] offers a unique perspective by applying NLP techniques to CRM data for
churn prediction. Utilizing word embeddings alongside RNNs, the study demonstrates that
text data—such as customer feedback and service interactions—can be effectively harnessed
to predict churn. This approach complements traditional structured data methods and
provides deeper insights into customer sentiment and behaviour. The findings suggest that
NLP-driven churn prediction models could be particularly beneficial in industries where
customer communication is critical in shaping retention strategies.

7.7. Representation and Feature Interaction Approaches

Representation and feature interaction approaches have emerged as promising strate-
gies to enhance churn prediction by capturing complex relationships within customer data.
These methods address limitations in traditional deep neural networks, particularly in
handling high-order feature interactions and categorical variables. This section reviews
key studies that leverage advanced embedding techniques to improve predictive accuracy
and interpretability in churn modeling.

Tang et al. [75] introduce a Feature Interaction Network (FIN) designed to overcome
challenges standard deep neural network-based churn models face. Traditional models
often struggle to capture high-order feature interactions and effectively handle one-hot
encoded categorical features. FIN integrates two key components to address this: an entity
embedding network to capture meaningful feature representations and a factorization
machine network with sliding windows to enhance feature interactions. Experimental

---

<!-- PAGE 29 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

29 of 38

evaluations on four public datasets demonstrate that FIN outperforms state-of-the-art
models by effectively capturing complex dependencies in customer data. This study
underscores the importance of feature interaction modeling in churn prediction, offering a
robust framework for leveraging structured customer data in predictive analytics.

In a complementary approach, Cenggoro et al. [76] develop a DL-based vector embed-
ding model tailored for churn prediction in the telecommunications industry. This model
not only emphasizes predictive accuracy but also enhances interpretability. The model
enables precise differentiation between loyal and churn-prone customers by leveraging
vector embeddings to represent customer behaviour in a discriminative feature space.
Experimental results indicate that the model achieves an F1 score of 81.16%, demonstrat-
ing strong predictive performance. Additionally, cluster similarity analysis and t-SNE
visualizations confirm that the learned representations are highly separable, reinforcing
the model’s effectiveness. This study highlights the potential of vector embeddings as a
powerful tool for churn modeling, equipping telecom providers with actionable insights
for customer re-engagement and retention.

These studies illustrate how embedding and feature interaction techniques can signifi-
cantly improve churn prediction by capturing nuanced relationships within customer data.
By enhancing both predictive performance and interpretability, these approaches offer
valuable tools for developing proactive and targeted retention strategies in competitive
industries. Deep learning architectures such as CNNs, RNNs, and attention-based models
excel at capturing temporal dynamics and complex feature interactions, often achieving
superior predictive accuracy. Their main drawbacks are higher computational cost, re-
liance on large datasets, and reduced interpretability, which can limit adoption in business
contexts requiring transparency.

In summary, machine learning and deep learning offer complementary strengths
for churn prediction. ML techniques are generally easier to interpret, faster to train, and
less resource-intensive, making them suitable for business settings where transparency
and efficiency are critical. In contrast, DL models are well-suited to high-dimensional,
sequential, and unstructured data, where their ability to learn complex patterns can lead to
superior predictive accuracy. Therefore, the choice between ML and DL depends not only
on data characteristics but also on practical requirements such as interpretability, scalability,
and computational resources.

The included studies (n = 61) were synthesized narratively to highlight methodological
trends, dataset usage, and reported performance metrics (see Tables 1 and 2). No formal
risk of bias assessment, reporting bias assessment, or certainty of evidence assessment (e.g.,
using GRADE) was conducted, as the review focused on methodological analysis rather
than quantitative synthesis. Due to substantial heterogeneity in study designs, datasets,
and evaluation protocols, meta-analysis was not feasible. Consequently, no investigations
of heterogeneity, subgroup analyses, sensitivity analyses, or certainty assessments were
performed, and no results were presented for these items.

8. Discussion
8.1. Linking Findings to Research Questions

To provide a direct response to the research questions outlined in the Introduction, we

summarise our findings below about each question:

RQ1: What are the predominant ML and DL approaches used in customer churn
prediction, and how have these methodologies evolved over time? Our synthesis
(Sections 6 and 7, Tables 1 and 2) shows that ensemble-based ML techniques—particularly
boosting methods such as XGBoost, LightGBM, and CatBoost—remain the most widely
adopted across industries, with decision trees and random forests also frequently used as

---

<!-- PAGE 30 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

30 of 38

interpretable baselines. LSTMs, CNNs, and attention-based architectures have been widely
adopted in the DL domain, particularly for sequential and unstructured datasets. While
hybrid approaches exist, most combine algorithms within the same paradigm (ML–ML or
DL–DL) rather than integrating ML with DL. From 2020 to 2024, there has been an apparent
increase in the adoption of explainable AI techniques, adaptive learning strategies, and
profit-driven evaluation metrics, reflecting a gradual shift toward models that balance
predictive performance with interpretability and business relevance.

RQ2: How do different predictive models compare in terms of accuracy, adaptability,
and interpretability across industries? Due to the heterogeneity of datasets, churn defini-
tions, feature sets, and evaluation protocols, direct cross-study performance ranking is not
feasible. Nonetheless, specific trends are evident. Boosting-based ML models consistently
achieve strong predictive performance on structured datasets but may be less effective at
modelling temporal dependencies than sequential DL architectures. LSTMs and CNNs ex-
cel at capturing behavioural and temporal patterns but often require greater computational
resources and exhibit reduced interpretability. Efforts to improve adaptability include
applying online learning, reinforcement learning, and transfer learning, although these
remain limited in real-world deployments. Regarding interpretability, traditional ML meth-
ods offer inherent transparency, while DL methods benefit from post-hoc explainability
tools such as SHAP, LIME, and attention mechanisms.

RQ3: What are the significant challenges and limitations in existing churn prediction
research, and what future directions could address them? Our review identifies key chal-
lenges, including class imbalance, reliance on static datasets, limited interpretability in
complex models, underutilisation of profit-oriented metrics, and a lack of cross-domain
generalisability. These challenges are compounded by deployment barriers such as scala-
bility and integration with existing CRM systems. As discussed in Section 8.4, potential
solutions include advanced resampling and cost-sensitive learning to mitigate imbalance,
hybrid models that combine accuracy with transparency, adaptive drift-aware learning
methods, and embedding business-centric evaluation metrics directly into optimisation
processes. Future research should focus on developing scalable, adaptive, and interpretable
churn prediction frameworks validated on standardised benchmark datasets to ensure both
scientific rigour and real-world impact.

8.2. Challenges and Limitations

Despite significant advancements in ML and DL for churn prediction, several chal-
lenges hinder real-world implementation. One of the most persistent issues is class im-
balance, where the number of churners in datasets is significantly smaller than that of
non-churners. This imbalance often biases models toward the majority class, reducing
their effectiveness in identifying at-risk customers. While resampling techniques and cost-
sensitive learning have been proposed as solutions, they can lead to overfitting or increased
computational costs.

Another major challenge lies in feature engineering and data representation. Many
models rely on structured transactional data, yet customer interactions involve diverse
data sources such as call logs, social media activity, and customer support interactions.
Integrating and extracting meaningful features from such heterogeneous data remains a
complex task. DL models can automate feature extraction, but often require extensive data
preprocessing and significant computational resources.

Model interpretability is another critical concern, especially with DL models. While
traditional ML techniques such as DTs and logistic regression provide human-readable
decision rules, neural networks and ensemble models function as black boxes, making it
difficult for businesses to trust their predictions. Explainable AI techniques, such as SHAP

---

<!-- PAGE 31 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

31 of 38

and attention mechanisms, have been introduced to address this issue, but they are not yet
widely adopted in real-world churn prediction systems.

Furthermore, customer behaviour is dynamic, and many churn prediction models
struggle to adapt to evolving patterns over time. Concept drift—where customer prefer-
ences, engagement levels, and churn risks change—challenges models trained on historical
data. Adaptive learning techniques, such as online learning and reinforcement learning,
offer potential solutions but require continuous retraining, making them resource intensive.
Finally, there is a disconnect between academic evaluation metrics and business impact.
Many studies assess model performance using accuracy, F1-score, and AUC-ROC, but
these do not necessarily translate to actionable business decisions. Profit-driven evaluation
metrics, which factor in the cost of retention efforts versus lost revenue from churners, are
still underexplored in research. Bridging this gap is essential for developing models that
provide tangible business value.

Addressing these challenges will require further advancements in adaptive modeling,
explainability techniques, and profit-aware churn prediction. As businesses continue to in-
vest in data-driven retention strategies, future research should focus on developing scalable,
interpretable, and business-aligned solutions to improve churn prediction outcomes.

Beyond the methodological challenges discussed above, this review and the body
of evidence synthesized have additional limitations worth noting. The body of evidence
synthesized in this review may be subject to several limitations. First, the included stud-
ies exhibited substantial heterogeneity in datasets, modeling objectives, and evaluation
metrics, complicating direct comparisons across studies. Second, many studies relied on
proprietary datasets with limited transparency, potentially restricting the generalizability
of their findings. Third, publication and reporting biases may be present, as studies with
positive results are more likely to be published in peer-reviewed outlets. Finally, the lack of
standardized evaluation protocols across studies hinders the establishment of consistent
benchmarks for churn prediction performance.

Moreover, this review also has inherent limitations in its processes. The search strategy
was limited to English-language peer-reviewed studies, which may have excluded relevant
research published in other languages or grey literature. Although the review adhered to
PRISMA guidelines and involved two reviewers collaboratively screening and extracting
data, no formal risk of bias or certainty assessments (e.g., ROBIS, GRADE) were performed,
as the primary focus was on methodological trends rather than quantitative effect estimates.
Additionally, using a narrative synthesis, while appropriate given the heterogeneity of
studies, may be less robust than meta-analytic approaches for aggregating evidence.

8.3. Identified Gaps in Reviewed Research

Despite the extensive advancements in ML and DL for customer churn prediction,
several gaps persist in the reviewed research, highlighting areas that require further explo-
ration. One of the most notable gaps is the limited emphasis on real-world deployment
challenges. While many studies focus on improving model accuracy and robustness, fewer
address the practical aspects of implementing these models in business environments.
Issues such as scalability, computational efficiency, and integration with existing CRM sys-
tems remain underexplored. Research into lightweight, efficient, and real-time deployable
solutions is essential since many organizations lack the computational infrastructure to
support complex DL models.

Another significant gap is the lack of focus on model interpretability and explainability.
While DL approaches, particularly RNNs, CNNs, and transformers, have shown improved
predictive performance, their black-box nature limits their adoption in business settings
where transparency is crucial. Although techniques like SHAP and Local Interpretable

---

<!-- PAGE 32 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

32 of 38

Model-Agnostic Explanations (LIME) have been introduced, they are not widely integrated
into churn prediction models. Future research should prioritise the development of inher-
ently interpretable models or hybrid approaches that balance accuracy with transparency
to facilitate better decision-making in customer retention strategies.

Additionally, most existing studies rely on static datasets, which fail to account for
the dynamic nature of customer behaviour. Concept drift—where customer engagement
patterns and churn drivers change over time—poses a significant challenge for model
generalization. While some studies explore adaptive, reinforcement, or online learning
techniques, their practical adoption remains limited. Future research should focus on
developing adaptive and self-learning models that continuously update based on evolving
customer data, ensuring sustained predictive performance over time.

Another gap is the lack of cross-domain generalization in churn prediction models.
Many studies develop models tailored to specific industries, such as telecommunications
or banking, but do not test their applicability across different sectors. Given that customer
behaviour varies significantly across domains, future research should explore domain
adaptation techniques and transfer learning to improve model generalizability. This would
enable businesses in different sectors to leverage churn prediction methodologies without
extensive retraining.

A further gap in the reviewed literature concerns fairness, ethics, and bias mitigation,
which remain largely absent from churn prediction research. Although fairness-aware
algorithms, bias auditing, and responsible AI frameworks are increasingly discussed in the
broader machine learning field, very few studies apply these considerations to customer
churn. This omission is significant because biased models may unintentionally disadvan-
tage certain customer groups, leading to unequal treatment in retention strategies and
exposing businesses to reputational or regulatory risks. Future research should therefore
emphasize fairness-aware model design, transparent reporting of potential biases, and
the integration of bias mitigation strategies. Addressing these issues would ensure that
churn prediction models are accurate, profitable, equitable, trustworthy, and aligned with
emerging standards for responsible AI.

Finally, profit-driven evaluation metrics remain underutilized in the reviewed liter-
ature. While traditional metrics such as accuracy, F1-score, and AUC-ROC are widely
reported, they do not fully capture the business implications of churn prediction. Few stud-
ies incorporate profit-based metrics like Expected Maximum Profit for Customer Churn,
which consider the financial impact of retention strategies. Further research is needed
to develop models that align more closely with business goals, optimizing for predictive
performance, cost-effectiveness, and revenue maximization.

Addressing these gaps will require a multi-faceted research approach, integrating
interpretability, adaptive learning, cross-domain validation, and business-centric evaluation
into future churn prediction models. By bridging these gaps, the field can advance toward
more practical, transparent, and financially viable solutions for churn management in
real-world applications.

8.4. Trend Directions

Analyzing publication trends in churn prediction research over 2020–2024 reveals a
clear shift toward more advanced ML and DL techniques. IEEE has consistently led in pub-
lication volume, indicating a strong research focus within engineering and computational
disciplines. While traditional ML techniques such as DTs and logistic regression remain
widely used, boosting methods and ensemble learning have steadily grown, reflecting an
industry preference for robust and interpretable models.

---

<!-- PAGE 33 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

33 of 38

In recent years, DL approaches, particularly RNNs, CNNs, and transformers, have
gained traction, especially in domains dealing with complex sequential and unstructured
data, such as telecommunications and banking. Adopting hybrid ML-DL models also
suggests an increasing interest in combining the strengths of multiple paradigms to improve
predictive accuracy.

Another notable trend is the growing importance of explainability and business-
aligned evaluation metrics. While early studies prioritised accuracy-based benchmarks,
more recent research integrates profit-driven evaluation methods, addressing the gap
between academic performance metrics and real-world applicability.

The field will likely see further advancements in adaptive learning techniques, rein-
forcement learning for churn management, and integration of multi-modal data sources.
The continued evolution of ML and DL for churn prediction indicates a shift toward models
that are more accurate, transparent, cost-effective, and dynamically adaptable to changing
consumer behaviours.

8.5. Potential Solution to the Current Challenges

Our review identifies several persistent challenges in customer churn prediction,
each of which has been addressed in the literature through various technical approaches.
One of the most prevalent is class imbalance, where the proportion of churners is far
smaller than that of non-churners. Beyond conventional oversampling and undersampling
techniques, more advanced strategies such as Synthetic Minority Oversampling with
Edited Nearest Neighbors (SMOTE-ENN) and Adaptive Synthetic Sampling (ADASYN)
have demonstrated improved representation of the minority class. Some studies have
combined these resampling methods with ensemble learning, while others have adopted
cost-sensitive learning frameworks that incorporate misclassification costs directly into the
model’s optimisation process. These cost-sensitive approaches ensure that model training
reflects the real financial implications of prediction errors, which is particularly important
in retention-focused applications.

Model interpretability is another major challenge, especially as deep learning architec-
tures become increasingly complex. Several studies have applied post hoc explainability
techniques such as Shapley Additive Explanations (SHAP), Local Interpretable Model-
agnostic Explanations (LIME), and counterfactual explanation methods to provide a clearer
understanding of model behaviour. Others have explored inherently interpretable alter-
natives, including sparse linear models and rule-based ensemble methods, which may
better suit domains where transparency is critical for regulatory compliance or building
stakeholder trust. A recurring trade-off in churn prediction research is the choice between
interpretable ML models and more complex DL architectures. Interpretable methods such
as decision trees, logistic regression, and rule-based ensembles remain highly suitable in
business contexts where transparency, regulatory compliance, and ease of communication
with non-technical stakeholders are critical. These models allow decision-makers to trace
predictions back to customer attributes and design targeted retention strategies. By contrast,
DL models—including LSTMs, CNNs, and Transformer-based architectures—are more
effective for high-dimensional, unstructured, or sequential data, where predictive accuracy
and capturing complex behavioural patterns outweigh the need for interpretability. Guid-
ance for practitioners therefore depends on context: interpretable ML is preferable when
accountability and actionable insights are paramount, whereas DL approaches—including
LSTMs, CNNs, and Transformer-based architectures—are more appropriate when the rich-
ness and complexity of the data demand advanced representation learning and predictive
accuracy.

---

<!-- PAGE 34 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

34 of 38

The problem of concept drift, where customer behaviours and market conditions
evolve over time, has also received growing attention. The Optimised Two-Sided Cumu-
lative Sum Churn Detector (OTCCD) integrates drift detection with adaptive learning to
update models as data distributions change. Transfer learning and domain adaptation
techniques have likewise been proposed to enable models to reuse knowledge from earlier
data while adapting to new patterns with minimal retraining. These strategies are particu-
larly relevant in industries where churn determinants shift rapidly due to technological or
competitive changes.

Finally, the limited adoption of profit-oriented evaluation metrics remains a missed
opportunity for aligning model performance with business objectives. Metrics such as the
Expected Maximum Profit for Customer Churn (EMPC) and other cost–benefit frameworks
allow for a direct assessment of the economic impact of retention strategies. Several studies
have shown that embedding these metrics into the optimisation process can produce
predictive and financially effective models rather than using them solely for post hoc
evaluation.

These solutions show that the challenges in churn prediction are not insurmountable.
Many methodological tools exist to address imbalance, improve interpretability, adapt to
shifting data distributions, and incorporate business value into evaluation. By drawing
attention to these approaches, our review aims to encourage future work that advances the
technical state of the art and ensures that churn prediction models deliver actionable and
economically meaningful outcomes.

9. Conclusions and Future Research Directions

Customer churn prediction has undergone rapid methodological evolution in recent
years, with machine learning and deep learning techniques now central to identifying
at-risk customers and guiding retention strategies. In this systematic review, we examined
240 peer-reviewed studies published between January 2020 and December 2024, applying a
PRISMA-guided, two-phase methodology. The first phase provided a bibliometric mapping
of the field, while the second delivered a detailed synthesis of 61 studies meeting strict
novelty and contribution criteria. This dual approach enabled us to capture both the
breadth and depth of recent advances in churn prediction research.

Our findings reveal a strong preference for ensemble learning and advanced ML
techniques such as gradient boosting (XGBoost, LightGBM, CatBoost), decision trees, and
random forests, alongside a growing adoption of DL architectures, particularly LSTMs,
CNNs, and attention-based models. These methods are increasingly applied to capture cus-
tomer data’s temporal dynamics and behavioural patterns. Hybrid modelling approaches
are also explored, though most combine different algorithms within the same paradigm
(ML–ML or DL–DL) rather than integrating ML with DL. While DL models often achieve
superior predictive power, this comes at the expense of higher computational demands and
reduced interpretability; conversely, traditional ML models tend to be more interpretable
and computationally efficient but may underperform with high-dimensional or complex
datasets. Efforts to bridge this gap through explainable AI tools such as SHAP, LIME,
and attention mechanisms are promising but remain underrepresented in operational
deployments.

Several persistent challenges emerged from our analysis. Class imbalance continues
to bias model performance toward majority classes, and many models are trained on static
datasets that do not reflect evolving customer behaviours, making them susceptible to
concept drift. Adaptive learning strategies and real-time model updating are still rare
in practice. Moreover, accuracy-oriented metrics dominate evaluation, with relatively
few studies integrating profit-driven metrics such as the EMPC, despite their closer align-

---

<!-- PAGE 35 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

35 of 38

ment with business objectives. In addition, fairness, ethics, and bias mitigation represent
important but underexplored priorities in churn prediction research. Incorporating fairness-
aware modelling and transparent reporting practices will be essential to ensure that future
solutions are not only technically robust and business-aligned but also socially responsible.
Addressing these gaps presents clear directions for future research. There is a need
for adaptive churn prediction frameworks that can dynamically update to account for
behavioural and market changes, ideally incorporating automated drift detection and
incremental learning. Integrating inherently interpretable models and robust post hoc
explainability techniques should be prioritised to improve transparency and user trust,
especially in regulated industries. Researchers should also explore multi-modal approaches
that combine structured, unstructured, and network-based data to capture richer repre-
sentations of customer behaviour. Finally, adopting standardised benchmark datasets and
incorporating business-aligned performance metrics during training and evaluation would
enable fairer comparisons across studies and ensure that predictive models deliver tangible
value in real-world retention strategies.

By combining bibliometric insights with a structured methodological synthesis, this
review provides a comprehensive, up-to-date map of churn prediction research. It offers
concrete guidance for developing the next generation of adaptive, interpretable, and
business-aligned models that can be deployed effectively in real-world contexts.

Author Contributions: M.I.: Conceptualization; Investigation; Methodology; Project administration;
Resources; Software; Validation; Visualization; Writing—original draft. M.J.: Conceptualization;
Investigation; Methodology; Resources; Validation. A.B.: Methodology; Supervision; Validation;
Writing—review & editing. H.R.A.: Supervision; Writing—review & editing. All authors have read
and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Data Availability Statement: Not applicable.

Conflicts of Interest: The authors declare no competing interests.

References

1.

2.
3.

4.

5.

6.
7.

8.

9.

Ahn, J.; Hana, S.-P.; Lee, Y.-S. Customer churn analysis: Churn determinants and mediation effects of partial defection in the
Korean mobile telecommunications service industry. Telecommun. Policy 2006, 30, 552–568. [CrossRef]
Xiaoling, S.; Ye, Y. Knowledge Discovery: Methods from data mining and machine learning. Soc. Sci. Res. 2023, 110, 102817.
Imani, M.; Arabnia, H.R. Hyperparameter optimization and combined data sampling techniques in machine learning for customer
churn prediction: A comparative analysis. Technologies 2023, 11, 167. [CrossRef]
Imani, M.; Ghaderpour, Z.; Joudaki, M.; Beikmohammadi, A. The Impact of SMOTE and ADASYN on Random Forest and
Advanced Gradient Boosting Techniques in Telecom Customer Churn Prediction. In Proceedings of the 2024 10th International
Conference on Web Research (ICWR), Tehran, Iran, 24–25 April 2024.
Imani, M.; Beikmohammadi, A.; Arabnia, H.R. Comprehensive Analysis of Random Forest and XGBoost Performance with
SMOTE, ADASYN, and GNUS Under Varying Imbalance Levels. Technologies 2025, 13, 88. [CrossRef]
Lemmens, A.; Gupta, S. Managing churn to maximize profits. Mark. Sci. 2020, 39, 956–973. [CrossRef]
Joudaki, M.; Imani, M.; Esmaeili, M.; Mahmoodi, M.; Mazhari, N. Presenting a New Approach for Predicting and Preventing
Active/Deliberate Customer Churn in Telecommunication Industry. In Proceedings of the International Conference on Security
and Management (SAM). The Steering Committee of the World Congress in Computer Science, Computer Engineering and
Applied Computing (WorldComp), Las Vegas, NV, USA, 18–21 July 2011.
Kamil, M.; Kopczewska, K. Customer churn in retail e-commerce business: Spatial and machine learning approach. J. Theor. Appl.
Electron. Commer. Res. 2022, 17, 165–198. [CrossRef]
Al-Najjar, D.; Al-Rousan, N.; Al-Najjar, H. Machine learning to develop credit card customer churn prediction. J. Theor. Appl.
Electron. Commer. Res. 2022, 17, 1529–1542. [CrossRef]

10. Christou, V.; Tsoulos, I.; Loupas, V.; Tzallas, A.T.; Gogos, C.; Karvelis, P.S.; Antoniadis, N.; Glavas, E.; Giannakeas, N. Performance
and early drop prediction for higher education students using machine learning. Expert Syst. Appl. 2023, 225, 120079. [CrossRef]

---

<!-- PAGE 36 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

36 of 38

11. Ajegbile, M.D.; Olaboye, J.A.; Maha, C.C.; Igwama, G.T.; Abdul, S. The role of data-driven initiatives in enhancing healthcare

delivery and patient retention. World J. Biol. Pharm. Health Sci. 2024, 19, 234–242. [CrossRef]

12. Ahn, J.; Hwang, J.; Kim, D.; Choi, H.; Kang, S. A survey on churn analysis in various business domains. IEEE Access 2020, 8,

220816–220839. [CrossRef]

13. Reichheld, F.F.; Teal, T. Loyalty Effect: The Hidden Force Behind Growth, Profits, and Lasting; Harvard Business School Publications:

Brighton, MA, USA, 1996; pp. 352–354.

14. Geiler, L.; Affeldt, S.; Nadif, M. A survey on machine learning methods for churn prediction. Int. J. Data Sci. Anal. 2022, 14,

217–242. [CrossRef]

15. Edvaldo, D.; Ojeme, B.; Daramola, O. Experimental analysis of hyperparameters for deep learning-based churn prediction in the

banking sector. Computation 2021, 9, 34. [CrossRef]

16. Höppner, S.; Stripling, E.; Baesens, B.; vanden Broucke, S.; Verdonck, T. Profit driven decision trees for churn prediction. Eur. J.

Oper. Res. 2020, 284, 920–933. [CrossRef]

17. Maldonado, S.; López, J.; Vairetti, C. Profit-based churn prediction based on minimax probability machines. Eur. J. Oper. Res.

18.

2020, 284, 273–284. [CrossRef]
Janssens, B.; Bogaert, M.; Bagué, A.; Van den Poel, D. B2Boost: Instance-dependent profit-driven modelling of B2B churn. Ann.
Oper. Res. 2024, 341, 267–293. [CrossRef]

19. Wang, X.; Nguyen, K.; Nguyen, B.P. Churn prediction using ensemble learning. In Proceedings of the 4th International Conference
on Machine Learning and Soft Computing, Haiphong City, Vietnam, 17–19 January 2020; Association for Computing Machinery:
New York, NY, USA, 2020.

20. Hemlata, J.; Khunteta, A.; Srivastava, S. Churn prediction in telecommunication using logistic regression and logit boost. Procedia

Comput. Sci. 2020, 167, 101–112. [CrossRef]

21. Maretta, S.N.T.; Permai, S.D. Enhanced churn prediction model with boosted trees algorithms in the banking sector. In Proceedings

of the 2021 International Conference on Data Science and Its Applications (ICoDSA), Online, 6–7 October 2021.

22. Tianpei, X.; Ma, Y.; Kim, K. Telecom churn prediction system based on ensemble learning using feature grouping. Appl. Sci. 2021,

11, 4742. [CrossRef]

23. Manohar, E.; Jenifer, P.; Nisha, M.S.; Benita, B. A collective data mining approach to predict customer behaviour. In Proceedings
of the 2021 Third International Conference on Intelligent Communication Technologies and Virtual Mobile Networks (ICICV),
Tirunelveli, India, 4–6 February 2021.

24. Ramesh, P.; Emilyn, J.J.; Vijayakumar, V. Hybrid artificial neural networks using customer churn prediction. Wirel. Pers. Commun.

2022, 142, 1695–1709. [CrossRef]

25. Usman-Hamza, F.E.; Balogun, A.O.; Capretz, L.F.; Mojeed, H.A.; Mahamad, S.; Salihu, S.A.; Akintola, A.G.; Basri, S.; Amosa, R.T.;

26.

27.

Salahdeen, N.K. Intelligent decision forest models for customer churn prediction. Appl. Sci. 2022, 12, 8270. [CrossRef]
Saias, J.; Rato, L.; Gonçalves, T. An approach to churn prediction for cloud services recommendation and user retention.
Information 2022, 13, 227. [CrossRef]
Ishrat, J.; Sanam, T.F. An Improved Machine Learning Based Customer Churn Prediction for Insight and Recommendation in
E-commerce. In Proceedings of the 2022 25th International Conference on Computer and Information Technology (ICCIT), Cox’s
Bazar, Bangladesh, 17–19 December 2022.

28. Liu, R.; Ali, S.; Bilal, S.F.; Sakhawat, Z.; Imran, A.; Almuhaimeed, A.; Alzahrani, A.; Sun, G. An intelligent hybrid scheme for

customer churn prediction integrating clustering and classification algorithms. Appl. Sci. 2022, 12, 9355. [CrossRef]

29. Yogesh, B.; Fokone, R.T. Hybrid approach using machine learning algorithms for customers’ churn prediction in the telecommu-

30.

nications industry. Concurr. Comput. Pract. Exp. 2022, 34, e6627.
Fu, K.; Zheng, G.; Xie, W. Customer churn prediction for a webcast platform via a voting-based ensemble learning model with
Nelder-Mead optimizer. J. Intell. Inf. Syst. 2023, 61, 859–879. [CrossRef]

31. Mahayasa, A.I.N.; Wanchai, P. Customer Churn Prediction Using Weight Average Ensemble Machine Learning Model. In
Proceedings of the 2023 20th International Joint Conference on Computer Science and Software Engineering (JCSSE), Phitsanulok,
Thailand, 28 June–1 July 2023.

32. Khoh, W.H.; Pang, Y.H.; Ooi, S.Y.; Wang, L.Y.K.; Poh, Q.W. Predictive churn modeling for sustainable business in the telecommu-

nication industry: Optimized weighted ensemble machine learning. Sustainability 2023, 15, 8631. [CrossRef]

33. Arshad, U.; Khan, G.; Khaled Alarfaj, F.; Halim, Z.; Anwar, S. Q-ensemble learning for customer churn prediction with blockchain-

enabled data transparency. Ann. Oper. Res. 2024. [CrossRef]

34. Venkatesh, S.; Jeyakarthic, M. An optimal genetic algorithm with support vector machine for cloud based customer churn
prediction. In Proceedings of the 2020 International Conference on System, Computation, Automation and Networking (ICSCAN),
Pondicherry, India, 3–4 July 2020.

---

<!-- PAGE 37 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

37 of 38

35.

Saheed, Y.K.; Hambali, M.A. Customer churn prediction in telecom sector with machine learning and information gain filter
feature selection algorithms. In Proceedings of the 2021 International Conference on Data Analytics for Business and Industry
(ICDABI), Online, 25–26 October 2021.

36. Pustokhina, I.V.; Pustokhin, D.A.; Nguyen, P.T.; Elhoseny, M.; Shankar, K. Multi-objective rain optimization algorithm with

WELM model for customer churn prediction in telecommunication sector. Complex Intell. Syst. 2023, 9, 3473–3485. [CrossRef]

37. Mirabdolbaghi, S.; Mohammad, S.; Amiri, B. Model optimization analysis of customer churn prediction using machine learning

algorithms with focus on feature reductions. Discret. Dyn. Nat. Soc. 2022, 2022, 5134356. [CrossRef]

38. Al-Shourbaji, I.; Helian, N.; Sun, Y.; Alshathri, S.; Abd Elaziz, M. Boosting ant colony optimization with reptile search algorithm

for churn prediction. Mathematics 2022, 10, 1031. [CrossRef]

39. AlShourbaji, I.; Helian, N.; Sun, Y.; Hussien, A.G.; Abualigah, L.; Elnaim, B. An efficient churn prediction model using gradient

boosting machine and metaheuristic optimization. Sci. Rep. 2023, 13, 14441. [CrossRef]

40. Kurtcan, D.B.; Ozcan, T. Predicting customer churn using grey wolf optimization-based support vector machine with principal

component analysis. J. Forecast. 2023, 42, 1329–1340. [CrossRef]

41. Ponnusamy, R.R.A.; Rana, M.E.; Manickavasagam, S.A.; Hameed, V.A. PSO-SVM based algorithm for customer churn prediction
in the banking industry. In Proceedings of the 2023 IEEE 6th International Conference on Big Data and Artificial Intelligence
(BDAI), Jiaxing, China, 8–9 July 2023.

42. Koço ˘glu, F.Ö.; Özcan, T. A grid search optimized extreme learning machine approach for customer churn prediction. J. Eng. Res.

2023, 11, 103–112. [CrossRef]

43. Ahmad, T.A.; Usman, M. Adaptive telecom churn prediction for concept-sensitive imbalance data streams. J. Supercomput. 2022,

78, 3746–3774.

44. Adnan, A.; Adnan, A.; Anwar, S. An adaptive learning approach for customer churn prediction in the telecommunication industry

using evolutionary computation and Naïve Bayes. Appl. Soft Comput. 2023, 137, 110103. [CrossRef]

45. Lee, N.T.; Lee, H.C.; Hsin, J.; Fang, S.H. Prediction of customer behavior changing via a hybrid approach. IEEE Open J. Comput.

46.

Soc. 2023, 5, 27–38. [CrossRef]
Shimaa, O.; Mahmoud, K.T.; Abdel-Fattah, M.A. A proposed hybrid framework to improve the accuracy of customer churn
prediction in telecom industry. J. Big Data 2024, 11, 70. [CrossRef]

47. De Bock, K.W.; De Caigny, A. Spline-rule ensemble classifiers with structured sparsity regularization for interpretable customer

churn modeling. Decis. Support. Syst. 2021, 150, 113523. [CrossRef]

48. Mitravinda, K.M.; Shetty, S. Employee attrition: Prediction analysis of contributory factors and recommendations for employee
retention. In Proceedings of the 2022 IEEE International Conference for Women in Innovation, Technology & Entrepreneurship
(ICWITE), Bangalore, India, 1–3 December 2022.

49. Wang, X.; Xie, L.; Wang, H.; Xing, X.; Wan, W.; Wu, Z.; Ma, X.; Li, Q. Deciphering Explicit and Implicit Features for Reliable,
Interpretable; Actionable User Churn Prediction in Online Video Games. IEEE Trans. Vis. Comput. Graph. 2024, 31, 5990–6007.
[CrossRef]

50. Vo, N.N.; Liu, S.; Li, X.; Xu, G. Leveraging unstructured call log data for customer churn prediction. Knowl.-Based Syst. 2021, 212,

51.

106586. [CrossRef]
Soumi, D.; Prabu, P. A Representation-Based Query Strategy to Derive Qualitative Features for Improved Churn Prediction. IEEE
Access 2023, 11, 1213–1223. [CrossRef]

52. Wang, A.X.; Chukova, S.S.; Nguyen, B.P. Data-centric ai to improve churn prediction with synthetic data. In Proceedings of the

2023 3rd International Conference on Computer, Control and Robotics (ICCCR), Shanghai, China, 24–26 March 2023.

53. Babak, A.; Hosseini, S.H. Unveiling the Power of Social Influence: A Machine Learning Framework for Churn Prediction with

Network Analysis. IEEE Access 2024, 12, 71271–71285. [CrossRef]

54. Nyashadzashe, T.; Sibanda, K. Real time customer churn scoring model for the telecommunications industry. In Proceedings of
the 2020 2nd International Multidisciplinary Information Technology and Engineering Conference (IMITEC), Kimberley, South
Africa, 25–27 November 2020.

55. Tianyuan, Z.; Moro, S.; Ramos, R.F. A data-driven approach to improve customer churn prediction based on telecom customer

56.

segmentation. Future Internet 2022, 14, 94. [CrossRef]
Šimovi´c, P.P.; Chen, C.Y.T.; Sun, E.W. Classifying the variety of customers’ online engagement for churn prediction with a
mixed-penalty logistic regression. Comput. Econ. 2023, 61, 451–485. [CrossRef]

57. AbdElminaam, D.S.; Maged, M.; Mousa, M.K.; Younis, A.O.; Abdelsalam, M.S.; Hisham, Y.; Talaat, T. EmpTurnoverML: An
Efficient Model for Employee Turnover and Customer Churn Prediction Using Machine Learning Algorithms. In Proceedings of
the 2023 International Mobile, Intelligent; Ubiquitous Computing Conference (MIUCC), Cairo, Egypt, 27–28 September 2023.
Jakob, R.; Lepper, N.; Fleisch, E.; Kowatsch, T. Predicting early user churn in a public digital weight loss intervention. In
Proceedings of the CHI ’24: Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems, Honolulu, HI,
USA, 11–16 May 2024.

58.

---

<!-- PAGE 38 -->

Mach. Learn. Knowl. Extr. 2025, 7, 105

38 of 38

59.

Sikri, A.; Jameel, R.; Idrees, S.M.; Kaur, H. Enhancing customer retention in telecom industry with machine learning driven churn
prediction. Sci. Rep. 2024, 14, 13097. [CrossRef] [PubMed]

60. Roohi, S.; Relas, A.; Takatalo, J.; Heiskanen, H.; Hämäläinen, P. Predicting game difficulty and churn without players. In
Proceedings of the CHI PLAY ‘20: Proceedings of the Annual Symposium on Computer-Human Interaction in Play, Online, 2–4
November 2020.

61. Zhu, B.; Qian, C.; Pan, X.; Chen, H. A trajectory-based deep sequential method for customer churn prediction. In Proceedings of

the 2020 5th International Conference on Machine Learning Technologies, Beijing, China, 19–21 June 2020.

62. Alboukaey, N.; Joukhadar, A.; Ghneim, N. Dynamic behavior based churn prediction in mobile telecom. Expert Syst. Appl. 2020,

63.

162, 113779. [CrossRef]
Joy, U.G.; Hoque, K.E.; Uddin, M.N.; Chowdhury, L.; Park, S.B. A big data-driven hybrid model for enhancing streaming service
customer retention through churn prediction integrated with explainable AI. IEEE Access 2024, 12, 69130–69150. [CrossRef]
64. Beltozar-Clemente, S.; Iparraguirre-Villanueva, O.; Pucuhuayla-Revatta, F.; Zapata-Paulini, J.; Cabanillas-Carbonell, M. Predicting
customer abandonment in recurrent neural networks using short-term memory. J. Open Innov. Technol. Mark. Complex. 2024, 10,
100237. [CrossRef]

65. Liu, Y.; Shengdong, M.; Jijian, G.; Nedjah, N. Intelligent prediction of customer churn with a fused attentional deep learning

66.

model. Mathematics 2022, 10, 4733. [CrossRef]
Jajam, N.; Challa, N.P.; Prasanna, K.S.; Deepthi, C.V.S. Arithmetic optimization with ensemble deep learning SBLSTM-RNN-IGSA
model for customer churn prediction. IEEE Access 2023, 11, 93111–93128. [CrossRef]

67. Zhao, Y.; Shao, Z.; Zhao, W.; Han, J.; Zheng, Q.; Jing, R. Combining unsupervised and supervised classification for customer

value discovery in the telecom industry: A deep learning approach. Computing 2023, 105, 1395–1417. [CrossRef]

68. Van-Hieu, V. Predict customer churn using combination deep learning networks model. Neural Comput. Appl. 2024, 36, 4867–4883.
69. Muhammad, U.; Ahmad, W.; Fong, A. Design and implementation of a system for comparative analysis of learning architectures

for Churn prediction. IEEE Commun. Mag. 2021, 59, 86–90. [CrossRef]

70. Ebru, P.O.; Ozcan, T. A novel deep learning model based on convolutional neural networks for employee churn prediction. J.

71.

72.

Forecast. 2022, 41, 539–550.
Saha, S.; Saha, C.; Haque, M.M.; Alam, M.G.R.; Talukder, A. Churnnet: Deep learning enhanced customer churn prediction in
telecommunication industry. IEEE Access 2024, 12, 4471–4484. [CrossRef]
Setyo, A.A. Telecommunication service subscriber churn likelihood prediction analysis using diverse machine learning model. In
Proceedings of the 2020 3rd International Conference on Mechanical, Electronics, Computer; Industrial Technology (MECnIT),
Medan, Indonesia, 25–27 June 2020.

73. Małgorzata, P.-K.; Marfo, K.F.; Sulikowski, P. Multi-Layer Perceptron and Radial Basis Function Networks in Predictive Modeling

of Churn for Mobile Telecommunications Based on Usage Patterns. Appl. Sci. 2024, 14, 9226. [CrossRef]

74. Ozan, ¸S. Case studies on using natural language processing techniques in customer relationship management software. J. Intell.

Inf. Syst. 2021, 56, 233–253. [CrossRef]

75. Tang, Q.; Xia, G.; Zhang, X.; Li, Y. A feature interaction network for customer churn prediction. In Proceedings of the 2020 12th

International Conference on Machine Learning and Computing, Shenzhen, China, 15–17 February 2020.

76. Cenggoro, T.W.; Wirastari, R.A.; Rudianto, E.; Mohadi, M.I.; Ratj, D.; Pardamean, B. Deep learning as a vector embedding model

for customer churn. Procedia Comput. Sci. 2021, 179, 624–631. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

SystematicReview
Customer Churn Prediction: A Systematic Review of Recent
Advances, Trends, and Challenges in Machine Learning and
Deep Learning
MehdiImani1,* ,MajidJoudaki2 ,AliBeikmohammadi1,* andHamidRezaArabnia3
1 DepartmentofComputerandSystemSciences,StockholmUniversity,SE-16455Stockholm,Sweden
2 DepartmentofComputerEngineering,FacultyofEngineering,AyatollahBoroujerdiUniversity,
Boroujerd69199-69737,Iran;m.joudaki@abru.ac.ir
3 SchoolofComputing,UniversityofGeorgia,Athens,GA30602,USA;hra@uga.edu
* Correspondence:m.imani@gmail.com(M.I.);beikmohammadi@dsv.su.se(A.B.)
Abstract
Background: Customerchurnsignificantlyimpactsbusinessrevenues. MachineLearning
(ML)andDeepLearning(DL)methodsareincreasinglyadoptedtopredictchurn,yeta
systematicsynthesisofrecentadvancementsislacking. Objectives: Thissystematicreview
evaluatesMLandDLapproachesforchurnprediction,identifyingtrends,challenges,and
research gaps from 2020 to 2024. Data Sources: Six databases (Springer, IEEE, Elsevier,
MDPI,ACM,Wiley)weresearchedviaLens.orgforstudiespublishedbetweenJanuary
2020 and December 2024. Study Eligibility Criteria: Peer-reviewed original studies ap-
plyingML/DLtechniquesforchurnpredictionwereincluded. Reviews,preprints,and
non-peer-reviewed works were excluded. Methods: Screening followed PRISMA 2020
guidelines. Atwo-phasestrategyidentified240studiesforbibliometricanalysisand61
fordetailedqualitativesynthesis. Results: Ensemblemethods(e.g.,XGBoost,LightGBM)
remaindominantinML,whileDLapproaches(e.g.,LSTM,CNN)areincreasinglyapplied
tocomplexdata. Challengesincludeclassimbalance,interpretability,conceptdrift,andlim-
AcademicEditors:OliverHinzand iteduseofprofit-orientedmetrics.ExplainableAIandadaptivelearningshowpotentialbut
AndreasHolzinger limitedreal-worldadoption. Limitations: Noformalriskofbiasorcertaintyassessments
Received:9July2025 wereconducted. Studyheterogeneitypreventedmeta-analysis. Conclusions: MLandDL
Revised:10September2025 methodshavematuredaskeytoolsforchurnprediction,yetgapsremainininterpretability,
Accepted:19September2025 real-worlddeployment,andbusiness-alignedevaluation. SystematicReviewRegistration:
Published:21September2025
RegisteredretrospectivelyinOSF.
Citation: Imani,M.;Joudaki,M.;
Beikmohammadi,A.;Arabnia,H.R. Keywords:customerchurnprediction;customerretention;deeplearning;literaturereview;
CustomerChurnPrediction:A
machinelearning
SystematicReviewofRecent
Advances,Trends,andChallengesin
MachineLearningandDeepLearning.
Mach.Learn.Knowl.Extr.2025,7,105.
1. Introduction
https://doi.org/10.3390/
make7030105 Customerretentionhasbecomeacriticalchallengeforbusinessesacrossvariousindus-
Copyright:©2025bytheauthors. tries,includingtelecommunications,retail,banking,insurance,healthcare,education,and
LicenseeMDPI,Basel,Switzerland. subscription-basedservices. Customerchurn—customersdiscontinuingtheirrelationship
Thisarticleisanopenaccessarticle withacompany—cansignificantlyimpactrevenues,withannualchurnratesrangingfrom
distributedunderthetermsand
20%to40%insomesectors[1]. Researchindicatesthatacquiringanewcustomerisfiveto
conditionsoftheCreativeCommons
twenty-fivetimesmoreexpensivethanretaininganexistingone,makingchurnprevention
Attribution(CCBY)license
astrategicpriorityforcompanies[2].
(https://creativecommons.org/
licenses/by/4.0/).
Mach.Learn.Knowl.Extr.2025,7,105 https://doi.org/10.3390/make7030105

Mach.Learn.Knowl.Extr.2025,7,105 2of38
Machine Learning and Deep Learning have emerged as powerful tools for churn
predictionduetotheirabilitytoanalyzelarge,high-dimensional,anddynamiccustomer
datasetseffectively. Traditionalchurnpredictionmethods,suchasrule-basedsystemsand
statisticalmodeling,oftenfailtocapturecustomerbehaviour’scomplexitiesadequately.
Conversely,MLapproacheslikeDecisionTrees(DTs),RandomForests(RFs),SupportVector
Machines (SVMs), and boosting algorithms (e.g., XGBoost, LightGBM, CatBoost) have
demonstratedstrongpredictivecapabilitieswithstructureddatasets[3–5]. Furthermore,
advancedDLarchitectures—includingArtificialNeuralNetworks(ANNs),Convolutional
NeuralNetworks(CNNs),LongShort-TermMemorynetworks(LSTMs),andTransformer-
basedmodels—providesignificantadvantagesformodelingsequentialandunstructured
data,suchascustomerinteractionhistoriesandtextualfeedback.
Despitethesetechnologicaladvancements,severalcriticalchallengesremaininchurn
prediction. Modelinterpretabilityremainsasignificantconcern,especiallywithcomplex
DL-based approaches often functioning as “black-box” models [6]. Data imbalance is
anotherprevalentissue,aschurndatasetstypicallyfeaturesignificantlyfewerchurners
thannon-churners,potentiallybiasingmodelpredictions[5]. Additionally,conceptdrift—
theevolvingnatureofcustomerbehaviourovertime—complicatesthesustainedaccuracy
ofpredictivemodels.
Thisliteraturereviewsystematicallyexploresadvancementsincustomerchurnpre-
diction by analyzing peer-reviewed research published between 2020 and 2024 across
diversedomainssuchastelecommunications,retail,banking,healthcare,education,and
insurance. ItaimstomapthecurrentlandscapeofMLandDLapproaches, evaluating
their strengths, limitations, and applicability to real-world scenarios. Given the broad
adoptionofpredictiveanalyticsacrossindustries,thisreviewseekstoclarifytheevolution
of these methodologies, the specific challenges they address, and the gaps that require
furtherresearch.
Akeyobjectiveofthisstudyistoidentifyandcategorizethemostfrequentlyemployed
MLandDLtechniquesusedinchurnprediction. Understandingtheevolutionofthese
methodsoverrecentyearsprovidesinsightsintohowbusinessesandresearchershavere-
finedapproachestoenhanceaccuracyandadaptability. Additionally,thisreviewevaluates
theperformanceandinterpretabilityofvariouspredictivemodels,focusingspecificallyon
theircapacitytomanageimbalanceddatasets,dynamiccustomerbehaviours,andpractical
deploymentconstraints. Consideringthatcustomerchurnresultsfrommultiplefactors—
suchastransactionhistories,engagementpatterns,andexternalmarketconditions—itis
crucialtoassesstheeffectivenessofmodelsincapturingthesecomplexities.
Anothercentralgoalishighlightingpersistentchallengesandlimitationswithinchurn
predictionresearch. Despitesubstantialprogress,issuessuchastheblack-boxnatureofDL
models,classimbalance,anddifficultyadaptingmodelstoevolvingcustomerbehaviours
impede real-world implementations. This review emphasizes these research gaps and
suggestspotentialareasforfutureinvestigation,includingimprovingmodeltransparency,
advancingfeatureengineeringtechniques,anddevelopingadaptivelearningmethodsto
addressshiftingcustomerpreferences.
Whilethisreviewsynthesizesabroadbodyofrecentliteratureoncustomerchurn
prediction,weintentionallyrefrainfrompresentingadirectcomparisonoftheirreported
performancemetrics(e.g.,accuracy,F1-score,AUC).Thisdecisionisbasedonthesubstan-
tialheterogeneityobservedacrossthestudiesregardingdatasetcharacteristics,imbalance
ratios,featuresets,modelingobjectives,andevaluationprotocols.
Specifically, models were trained and validated on various public and proprietary
datasetsdrawnfromdiverseindustries(e.g.,telecommunications,banking,e-commerce),
oftenwithdistinctdefinitionsofchurn,timewindows,andinputmodalities. Evaluation

Mach.Learn.Knowl.Extr.2025,7,105 3of38
metricsalsovariedwidely,withsomestudiesprioritisingbusiness-orientedoutcomesand
othersfocusingonstatisticalmeasures. Assuch,anyattempttoaggregateorcomparethese
resultsdirectlywouldriskintroducingmisleadinginterpretationsandovergeneralizations.
Instead,thisreviewfocusesonidentifyingmethodologicaltrends,thetaxonomyof
modeling strategies, and common challenges and innovations. Where appropriate, we
highlight representative studies that exemplify key methodological advances without
assertingquantitativesuperiority. Weencouragefuturebenchmarkstudiesusingstandard-
izeddatasetsandexperimentalprotocolstoconductrigorousperformancecomparisons,
ideallyincorporatingstatisticalsignificancetestingundercontrolledconditions.
Toaddresstheseobjectives,thisstudyisguidedbythreefundamentalresearchques-
tions:
RQ1: What are the predominant ML and DL approaches used in customer churn
prediction,andhowhavethesemethodologiesevolvedovertime?
RQ2: Howdodifferentpredictivemodelscompareaccuracy,adaptability,andinter-
pretabilitywhenappliedtochurnpredictionacrossvariousindustries?
RQ3: What are the significant challenges and limitations in existing churn predic-
tionresearch,andwhatfuturedirectionscanbeexploredtoenhancetheeffectivenessof
predictivemodels?
Thisreviewsynthesizescurrentresearchtoinformbothacademicandindustryprac-
tices. Thiswork’sspecificcontributionsandnovelaspectsareoutlinedinthefollowing
subsection.
ContributionsandNovelty
Thisstudyoffersseveraldistinctcontributionsthatdifferentiateitfrompriorreviews
oncustomerchurnprediction:
1. Most Recent and Comprehensive Scope: We systematically review peer-reviewed
researchpublishedbetweenJanuary2020andDecember2024,encompassingrecent
advancessuchasCNN-basedarchitectures,hybriddeeplearningframeworks,and
profit-drivenmodellingapproaches. Earlierreviewspredominantlyfocusonpre-2020
literatureandthereforedonotcapturetheseemergingtrends.
2. PRISMA-GuidedandReproducibleMethodology: Oursearchandselectionstrategy
adherestothePRISMA2020guidelines,ensuringmethodologicaltransparencyand
reproducibility.Weemployatwo-phasereviewprocess,aninitialbibliometricanalysis
of240studiesfollowedbyanin-depthsynthesisof61keypapers. Whereasexisting
reviewsoftenlacksuchastructuredandreplicableapproach.
3. NovelHierarchicalTaxonomy:Weintroduceanewhierarchicaltaxonomythatcatego-
rizesMLandDLapproachesintofine-grainedsubgroups(e.g.,profit-centricmodels,
optimization/metaheuristics,adaptivelearning,explainableAI).Thistaxonomypro-
videsasystematicframeworkformappingthemethodologicallandscape,afeature
absentinearlierworks.
4. IntegrationofBibliometricandMethodologicalInsights: Inadditiontomethodolog-
ical synthesis, we conduct a comprehensive bibliometric analysis, including pub-
lishertrends,citationdynamics,andopen-accesseffects,tocontextualizetheresearch
landscape. Previous reviews focus exclusively on models and do not incorporate
dissemination-orientedanalyses.
5. Identification of Emerging Challenges Supported by Evidence-Based Trends: We
identifychallengessuchasclassimbalance,conceptdrift,andthelimitedadoptionof
business-orientedevaluationmetrics,linkingthemtorepresentativestudiespublished
between2020and2024. Thisevidence-drivenmappingoftrendsprovidesamore

Mach.Learn.Knowl.Extr.2025,7,105 4of38
preciseandup-to-dateperspectivethanthegenericlimitationsdiscussedinearlier
surveys.
Byclearlydelineatingthesecontributions,thisreviewmakesitsnoveltyandvalue
explicit,offeringactionableinsightsforacademicresearchersandindustrypractitioners
engagedincustomerretentionanalytics.
2. PurposeoftheStudy
CustomerchurnpredictionisvitalinmodernCustomerRelationshipManagement
(CRM),helpingbusinessesproactivelyretainat-riskcustomersandmaximizecustomer
lifetime value. With high churn rates leading to substantial revenue losses, businesses
in subscription-based services, telecommunications [1,7], retail [8], banking [9], educa-
tion[10],healthcare[11],Insurance[12],andothersectorsincreasinglyrelyondata-driven
approachestoenhancecustomerretentionstrategies.
Whilebusinessescollectvastamountsofcustomerdata,extractingactionableinsights
fromthesedatasetsischallenging. Datamining,akeydisciplineinMLandartificialintelli-
gence,enablesorganizationstouncoverhiddenpatternsandtrendsinchurnbehaviours.
However,theeffectivenessofchurnpredictionmodelsvariessignificantlybasedonthe
choiceofmethodology,datasetcharacteristics,andindustry-specificfactors.
Thisstudysystematicallyreviews240researcharticlespublishedbetween2020and
2024,focusingonchurnpredictionusingMLandDLmethodologiesacrossvarioussectors.
Thereview:
• Examinesdifferentchurnpredictionapproachesacrossmultipleindustries.
• AssessesthecomparativeperformanceofMLandDLtechniquesinchurnprediction.
• Investigates common challenges, such as data imbalance, feature selection, inter-
pretability,andconceptdrift.
• Highlightsemergingtrendsinchurnprediction,includingprofit-drivenmodeling,
explainableAI(XAI),andadaptivelearningapproaches.
Churn prediction research is crucial for developing effective retention strategies,
allowingbusinessestoanticipatecustomerattrition,personalizemarketingefforts,and
allocateretentionbudgetsmoreefficiently. Studiessuggestthatbusinessesimplementing
advancedchurnpredictiontechniquescanimproveretentionratesby5–10%,leadingto
profitincreasesof25–95%[13].
Bysynthesizinginsightsfromrecentresearch,thispaperservesasavaluableresource
forresearchers,datascientists,andindustrypractitioners,helpingthemunderstandbest
practices,methodologicaladvancements,andfuturedirectionsinchurnprediction.
Formoreinformation,readerscanrefertoseveralcomprehensivereviewpapersthat
explorevariousaspectsofcustomerchurnprediction.ImaniandArabnia[3]provideacom-
parativeanalysisofhyperparameteroptimizationtechniquesanddatasamplingstrategies
inMLmodelsforchurnprediction,highlightingtheirimpactonpredictiveperformance.
Theauthorsin[5]extendthisanalysisbyevaluatingtheeffectivenessofSMOTE,ADASYN,
andGNUSupsamplingtechniquesinconjunctionwithRFandXGBoostunderdifferent
classimbalancelevels. Geileretal.[14]offerabroadsurveyofMLapproachesforchurn
prediction,discussingtheirstrengths,limitations,andpracticalapplications. Domingos
etal.[15]focusonhyperparametertuningforDL-basedchurnpredictionmodels,particu-
larlywithinthebankingsector,providinginsightsintooptimizingdeepneuralnetworks
for improved accuracy. These studies offer valuable perspectives on churn prediction
research’smethodologicaladvancementsandchallenges.

Mach.Learn.Knowl.Extr.2025,7,105 5of38
3. SearchStrategies
Asystematicliteraturesearchwasconductedacrosssixmajoracademicpublishers,
includingSpringer,IEEE,Elsevier,MDPI,ACM,andWiley,ensuringcomprehensivecover-
ageofrecentadvancementsincustomerchurnpredictionusingMLandDLtechniques.
ThesearchwasexecutedviaLens.org, ascholarlyresearchplatformofferingadvanced
filteringandindexingcapabilitiessuperiortogenericsearchengineslikeGoogleScholar.
Torefinethesearch,thequery“(churnpredictionANDmachinelearning)OR(churn
predictionANDdeeplearning)NOT(“survey”OR“review”)”wasapplied,focusingon
originalresearchcontributionsratherthansurveyorreviewarticles. Additionally,results
wererestrictedtojournalandconferenceproceedingsarticlespublishedbetween2020and
2024,ensuringrelevancetorecentdevelopments. TheKStem-basedstemmingapproach
wasutilizedtonormalizevariationsoftheterm“churn,”suchas“churned”and“churning,”
tocaptureabroaderrangeofrelevantstudies.Thefinalsearchwasconductedon15January
2025. VisualizationsandplotswereproducedusingPython3.13,employingthematplotlib
andseabornlibrariestoensureclarityandreproducibilityofgraphicalresults.
AsillustratedinFigure1,theinitialsearchretrieved837articles. Toensurerelevance
andquality,aseriesofrefinementstepswasapplied. First,filteringbydocumenttypetoin-
cludeonlyjournalandconferencearticleswhileexcludingpre-prints,technicalreports,and
othernon-peer-revieweddocumentsreducedthecountto679articles. Next,restrictingthe
selectiontohigh-qualitypublishers—aspreviouslyoutlined—furtherrefinedthedatasetto
368articles. Finally,adomain-specificreviewwasconductedtoeliminatepapersunrelated
tocustomerchurnpredictionorthosenotutilizingMLandDLtechniques. Thisresultedin
afinalselectionof240articlesforthefirstphase(shallowreviewphase). Thisexploratory
phaseanalyzedbroadresearchtrends,methodologicalpatterns,andkeydevelopmentsin
customerchurnpredictionusingMLandDLapproaches. Thisphasefocusedonhigh-level
bibliometricanalysis,includingpublicationtrendsacrossresearchdomains,thedistribu-
tionofMLandDLtechniques,theaveragecitationtrendsofpublishers(Crossrefcitation),
citationpatterns,andthepublicationssharedamongdifferentpublishersoverthepastfive
years(2020–2024). Byanalyzingthesebroadertrends,thisphaseprovidedafoundationfor
identifyingthemostinfluentialstudies,emergingresearchdirections,andmethodological
advancements.
Asecondphase(deepreviewphase)wasconductedtoensureamorefocusedand
rigorousexamination,inwhich61paperswereselectedbasedonrelevance,citationimpact,
methodologicalnovelty,andcontributiontothefield. Thisphasedelvedintothetechnical
depthoftheselectedstudies,focusingoncriticalaspectssuchasdatasetcharacteristics,
appliedMLandDLtechniques,evaluationmetrics,andthekeyoutcomesreportedinthe
studies. Byconductingthistwo-phasereviewstrategy,thestudycapturedbroadresearch
trendsandprovidedagranularunderstandingofmethodologicaladvancements,dataset
challenges,andperformancebenchmarks.Thisstructuredapproachenhancedtheliterature
review’scomprehensiveness,objectivity,anddepth,ensuringbothbreadthanddepthin
assessingthestate-of-the-artcustomerchurnpredictionresearch.
Theinclusioncriteriaareoutlinedbelow:
• ArticlesmustfocusonchurnpredictionusingMLorDLtechniques.
• Articlespublishedbetween2020and2024inpeer-reviewed,high-qualityjournals.
• Articlesmustbeoriginalresearchpapers.
• ArticlespublishedinEnglish.
Theexclusioncriteriaareoutlinedbelow:
• Articlesunrelatedtochurnprediction.
• ArticlesunrelatedtoMLorDL.

Mach.Learn.Knowl.Extr.2025,7,105 6of38
• Non-peer-reviewedworks(e.g.,lecturenotes,newsletters,dissertations).
• Low-qualitypublishers.
• Reviewpapers,preprints,books,etc.
• Non-Englishpublications.
Figure1.PRISMAFlowchart.
This systematic approach, grounded in a well-documented filtering process and
adherencetoPRISMAguidelines,ensuresthereproducibilityofthisliteraturereview. All
inclusioncriteria,searchstrings,andfilteringstepshavebeenexplicitlyoutlinedtofacilitate
replicationbyfutureresearchers.
Tworeviewers(MIandMJ)collaborativelyscreenedtitlesandabstractsforrelevance,
resolvingdisagreementsthroughdiscussion. Onereviewer(MI)extractedstudycharac-
teristics and methodological details for data collection, while the second reviewer (MJ)
cross-checkedforaccuracy. Noautomationtoolsorcontactwithstudyauthorswereused
duringtheseprocesses.
For each included study, data were extracted on the primary outcomes of interest:
ML/DL techniques employed, evaluation metrics (e.g., accuracy, F1-score, ROC-AUC,
PR-AUC),andkeyfindingsrelatedtomethodologicalchallengessuchasclassimbalance,
conceptdrift,andmodelinterpretability. Additionalvariablescollectedincludedpubli-
cationyear,applicationdomain(e.g.,telecommunications,banking,healthcare),dataset
characteristics (public, private, or synthetic), and study citation metrics. All data were
extracted as reported in the original publications; no imputation or conversions were
applied.
Studiesweregroupedforsynthesisusingatwo-phaseapproach: ashallowreview
phase (240 studies) to identify broad methodological trends and a deep review phase
(61 studies) for detailed analysis. Results were tabulated and visually displayed using
summarytablesandfigurestoillustratetrendsinML/DLtechniques,performancemetrics,

Mach.Learn.Knowl.Extr.2025,7,105 7of38
andapplicationdomains.Narrativesynthesiswasperformedtosummarizemethodological
patternsandchallenges,asameta-analysiswasnotfeasibleduetoheterogeneityinstudy
designs,datasets,andevaluationmetrics. Nosubgroupanalysesorsensitivityanalyses
wereconducted,giventhequalitativefocusofthisreview.
Wedidnotperformaformalriskofbiasassessmentorreportingbiasassessment,as
thereviewaimedtosynthesizemethodologicaltrendsratherthanevaluatethequalityof
individualstudies. Similarly,aformalcertaintyassessment(e.g.,usingGRADE)wasnot
applied. Futuresystematicreviewsconductingquantitativesynthesisormeta-analyses
shouldconsiderincorporatingtheseassessmentsusingstandardizedtoolssuchasROBIS,
AMSTAR2,orGRADE.ThissystematicreviewwasretrospectivelyregisteredintheOpen
ScienceFramework(OSF)underDOI:https://doi.org/10.17605/OSF.IO/PZ2H7.
4. TrendsinChurnPredictionResearch
Tocomprehensivelyinvestigatethestateofchurnpredictionresearch,wesystemati-
callyreviewed240publicationsspanningtheyears2020to2024. Thisfive-yearwindow
waschosentocapturecurrenttrendsandreflecttherapidadvancementsinMLandDL
applications. Thebroadscopeofthisinitialpoolenabledustoanalyzesignificanttrends
inpublisherdistribution,citationdynamics,averagecitationvariations,researchdomain
focus,andtheadoptionofvariousMLandDLtechniques. Allstudiesexcludedduring
thescreeningprocessfailedtomeetthepredefinedinclusioncriteria(e.g., theydidnot
employML/DLtechniques,didnotaddresschurnprediction,orwerenon-peer-reviewed).
Nostudiesthatinitiallyappearedtomeetinclusioncriteriawereexcludedduringfull-text
review.
Fromthismoreextensiveset,weselected61studiesfordeeperqualitativeexamination.
This subset was identified based on multiple criteria, including methodological rigor,
noveltyofapproach,domaindiversity,andoverallcontributiontothefield. Bycombining
awide-rangingquantitativeoverviewwithafocused,in-depthanalysisofkeystudies,our
methodologyensuresanexpansivemappingofchurnpredictionresearchandathorough
investigationofthemostinfluentialandinnovativework. Thisdual-levelstrategythus
providesreaderswitharobustunderstandingofcurrentpractices,emergingchallenges,
andfuturedirectionsinchurnpredictionusingMLandDLtechniques.
Figure2presentstheoveralldistributionofpublicationsbypublishers. Thepiechart
illustrates that IEEE accounts for the largest share, with 60.4% of the total publications.
SpringerandElsevierfollow,at12.9%and11.2%,respectively,whileMDPIcomprises7.1%
ofthedataset. ACMandWileycomprisetheremaining5.8%and2.5%,respectively. These
percentageshighlightthedominantpositionofIEEEamongthepublishersrepresentedin
thisstudy.
Figure 3 further explores the temporal dimension of these publications from 2020
through2024. IEEEexhibitsamarkedincreaseinpublishedpapers,peakingin2023. In
contrast, the other publishers remain relatively steady, though minor fluctuations can
beobservedfromyeartoyear. Notably,theapparentdeclineinpublicationsfor2024is
likelyattributabletoincompleteindexingduringdataextraction(January2025). Given
thatnotall2024publicationsmayhavebeenprocessedandincludedinourstudybythat
point, the downward trend for 2024 should be interpreted with caution. These figures
suggestthatIEEEconsistentlyleadsinpublicationoutput,whileotherpublishersmaintain
comparativelysmalleryetstablesharesovertheexaminedperiod.

Mach.Learn.Knowl.Extr.2025,7,105 8of38
Figure2.ShareofPublicationsbyPublishers.
Figure3.PublicationTrendsofPublishers.
Figures4and5illustratethenumberofcitationsandnormalizedimpactfactortrends
fortheselectedpublishers(Elsevier,IEEE,MDPI,Springer,Wiley,andACM)from2020to
2024. Figure4showsthatElsevierexhibitedthehighesttotalcitationsin2020,followed
byanoticeabledeclineinsubsequentyears. Otherpublishers,includingIEEEandMDPI,
displaysmallerbutstilldiscerniblepeaksinearlieryears,withatendencytowardreduced
citation counts in 2023 and 2024. These observations align with the typical pattern in
bibliometricanalyses,wherebyearlierpublicationshavealongerwindowtoaccumulate
citations.
Figure4.CitationsReceivedbyEachPublisher.

Mach.Learn.Knowl.Extr.2025,7,105 9of38
Figure5.NormalizedIFTrendsofPublishers.
Figure5illustratesthenormalizedimpactfactortrendsofthepublishersfrom2020
to 2024. To ensure a fair comparison of citation performance across publication years,
wecomputedanormalizedimpactfactor(IF)bydividingthetotalnumberofcitations
receivedbythenumberofpublishedpapersandthenumberofyearssincepublication.
Thisapproachaccountsforthevaryingtimewindowsavailableforpaperstoaccumulate
citations,thusmitigatingthebiasthatfavorsearlierpublications. Theformulausedisas
follows:
TotalCitations
Normalized IF =
Numberof Papers×YearsSincePublications
AsshowninFigure5,ElsevierandMDPIconsistentlyoutperformotherpublishersin
termsofnormalizedimpactacrossmostyears. Elsevierexhibitsstrongperformancein2020
(above10citationsperpaperperyear),dipsin2022,andthenpeaksagainin2023,suggest-
ingacombinationofhigh-impactpublicationsandefficientvisibility. MDPIdemonstrates
asteeprisein2021—reachingnearly10citationsperpaperperyear—andagradualdecline
inthefollowingyearsyetmaintainingarelativelystrongcitationperformancethrough2023.
Springershowsadownwardtrendfrom2020to2022butstabilizesaroundthreecitations
perpaperperyearby2023. Wileypeaksin2021,likeMDPI,followedbyamoderatebut
steadydecline. IEEEandACMdisplaylowerandmorestablecitationpatternsacrossthe
years,withvaluesremainingprimarilybelow2,indicatingmoreconsistentbutmodest
averagecitationrates.
Whilethenormalizedimpactfactoraccountsforthetimesincepublication,ageneral
declineisstillobservedin2024acrossmostpublishers. Thismayreflectseveralfactors,
includingrecentshiftsinpublicationstrategies,articletopics,qualitychanges,orearly-
stage visibility. Moreover, papers published in 2024 may not yet be fully indexed or
cited at the time of data extraction (January 2025), especially for journals with delayed
indexingpipelines. Assuch,citation-basedmetricsfromthemostrecentyearshouldbe
interpretedwithcaution,astheymayunderestimatetheeventuallong-termimpactofthese
publications.
Overall, the trends reveal significant year-to-year variation in normalized citation
performanceamongpublishers,underscoringtherolesofeditorialpolicy,topicalfocus,
and dissemination strategies. By adjusting for publication age, the normalized impact
factoroffersafairerandmoretime-independentcomparison,particularlywhenanalyzing
performanceacrossbothrecentandearlierpublicationyears.
Figure6illustratestheoveralldistributionofcitationcountsforthecollectedpublica-
tions,revealingahighlyskewedpattern. Mostpapersreceiveonlyafewcitations(fewer
than five), while a relatively small number of publications accumulate notably higher
citationcounts. Thisright-skeweddistributionistypicalinbibliometricanalyses,wherein

Mach.Learn.Knowl.Extr.2025,7,105 10of38
most publications garner modest attention, whereas a limited subset gains substantial
visibilityand,consequently,highercitationimpact.
Figure6.CitationCountDistribution.
Figure7presentsthenormalizedimpactfactortrends—theaveragenumberofcitations
perpaperperyear—forOpenAccess(OA)andNon-OpenAccess(non-OA)publications
from2020to2024. Acrossallyears,OApapersconsistentlyoutperformnon-OAarticlesin
termsofcitationimpact,withrobustperformancein2020and2021. Thistrendsupports
thenotionthatOApublishingmayenhancethevisibilityanddiscoverabilityofresearch,
therebyincreasingitscitationpotential. Whilethenormalizedmetricaccountsforthetime
since publication, a noticeable decline is observed for both OA and non-OA papers in
2024. Thismayreflectlimitedearly-stagevisibility,indexingdelays,orpublicationlagsthat
hindercitationaccumulation,particularlyforarticlespublishedclosetothedataextraction
date(January2025),whichmaynotyetbefullyindexedorcited,especiallyinjournalswith
slowerindexingpipelines. Assuch,thelowervaluesobservedforthemostrecentyear
shouldbeinterpretedcautiously,astheymaynotaccuratelyreflectthelong-terminfluence
ofthosepublications.
Figure7.NormalizedIFTrends:OAvs.non-OAPapers.
Figure8presentstheannualdistributionofpublicationsacrosssixresearchdomains—
Telecom,Retail,Banking,Education,Healthcare,andInsurance—from2020to2024. Across
mostdomains,theoveralltrendisgradualgrowthfrom2020through2023,followedbya
slightdeclinein2024. Telecomshowsapronouncedincreaseinpublicationsupto2023,
indicatingasustainedresearchfocusonchurnpredictionwithinthatsector.Healthcareand
Educationalsoexhibitsteadyupwardtrajectories,reflectingbroaderinterestinapplying
churn-related methodologies to patient retention and student engagement. Retail and
Bankingmaintainmoderatebutconsistentgrowth,whileInsuranceremainscomparatively

Mach.Learn.Knowl.Extr.2025,7,105 11of38
lower throughout the observed period. The apparent drop in 2024 publications for all
domains is likely influenced by the shorter window for indexing at the time of data
extraction(January2025),anditdoesnotnecessarilyindicateawaningresearchinterest.
Figure8.Publicationtrendsbyresearchdomains.
Figure9presentsthetimeseriestrendsofMLandDLtechniquesinchurnprediction
from2020to2024. MLmethodsexhibitasteadyupwardtrend,indicatingtheirwidespread
adoption. Incontrast,DLpublicationsremainrelativelylowbutshowgradualgrowth. The
apparentdeclinein2024shouldbeinterpretedcautiously,asmanypapersfromthisyear
maynotyetbefullyindexedorhavehadsufficienttimetogaincitationsandvisibility.
Figure9.Theusageofdifferentcategoriesoftechniquesinchurnpredictionresearch.
Figure10depictstheannualusageofsevenMLalgorithms—BoostingTechniques
(includingXGBoost,LightGBM,andCatBoost),K-NearestNeighbors,RF,DT,SVM,Naïve
Bayes,andLogisticRegression—between2020and2024. BoostingTechniques,RF,and
LogisticRegressionshownotablegrowththrough2022–2023,suggestingincreasedresearch
interestinensemble-basedmethodsandwidelyusedbaselinemodels. Whilemosttech-
niques experienced a slight dip in 2024, it is likely due to incomplete indexing and the
relativelyshorttimesincepublicationatthetimeofdataextraction(January2025).
Figure11focusesonDLapproaches—ANNs,LSTMs,CNNs,RecurrentNeuralNet-
works(RNNs),Transformers,andReinforcementLearning—overthesameperiod. ANNs
exhibitapronouncedsurgein2022,reflectingtheirbroadapplicabilityindiversedomains.
LSTMsandCNNsalsoshowmoderateyetconsistentusage,whileTransformersandRe-
inforcementLearningremainlessfrequentbutappeartohavegainedmodesttractionin
recentyears. LiketheMLtrends,thelowercountsfor2024likelydonotcapturethefull
extentofongoingresearchactivity,underscoringtheneedtointerprettheserecent-year
valuescautiously. Overall,thedatarevealacontinuedshifttowardadvancedMLandDL

Mach.Learn.Knowl.Extr.2025,7,105 12of38
techniques, albeit tempered by the time-dependent nature of publication and indexing
cycles.
Figure10.TheusageofdifferentconventionalMLtechniquesinchurnpredictionresearch.
Figure11.TheusageofdifferentDLtechniquesinchurnpredictionresearch.
Whiletheprimaryfocusofthisreviewisonmethodologicaladvancementsinchurn
prediction,analyzingwhereandhowresearchispublishedofferscomplementaryinsights
intothedisseminationandvisibilityofthefield. Thedistributionofpublicationsacross
major academic publishers and the temporal trends in citation activity help illustrate
the growing attention to churn prediction across domains such as telecommunications,
banking,andhealthcare. Forexample,thepredominanceofIEEEpublicationsmayreflect
historicalengagementwithmachinelearningapplicationsintelecommunicationsanda
concentrationofconference-stylecontributions. Whilecitationtrendsatthepublisherlevel
cannotbedirectlylinkedtospecificmethodsorstudies,theymaysuggestbroaderpatterns
inresearchvisibility,accessibility(e.g.,openaccessavailability),andperceivedrelevance.
Assuch,thesebibliometricobservationscontextualize,notevaluate,themethodological
developmentsreviewedinthisstudy.
5. Paper’sCategorizations
Inourreview,weproposeacomprehensivetaxonomythatsystematicallyorganizes
theliteratureonchurnpredictionintotwoprimarymethodologicalcategories: Machine
LearningApproachesandDeepLearningApproaches. Eachcategoryisfurthersubdivided
intospecificsubcategories,asillustratedinFigure12.

Mach.Learn.Knowl.Extr.2025,7,105 13of38
Figure12.TaxonomyofChurnPredictionApproaches.
TheMLApproachesencompassarangeoftechniques,includingprofit-centricmod-
els, which optimize retention strategies based on business impact, and ensemble and
hybridapproaches,whichcombinemultipleclassifierstoimprovepredictiveperformance.
Optimizationandmetaheuristicmethodsalsofocusonrefiningfeatureselectionandhyper-
parametertuning,whileadaptiveandresamplingtechniquesaddressdataimbalanceand
conceptdrift. Thereviewalsocoversexplainableandinterpretablemodels,whichenhance
transparencyinchurnprediction,data-centricandaugmentationstrategiesthatleverage
noveldatasourcesandsyntheticdatageneration,andtraditionalMLtechniques,which
continuetoplayafoundationalroleinchurnmodeling.
Ontheotherhand,DLapproachesleverageadvancedarchitecturestocapturecom-
plexpatternsincustomerbehaviour. Theseincludedeepreinforcementlearning,which
enablesadaptivedecision-making,andtemporalandsequentialmodels,suchasLSTMs,
whichcaptureevolvingchurnpatternsovertime. Thetaxonomyalsohighlightshybrid
and ensemble DL approaches, which integrate multiple DL frameworks for improved
generalization,andCNN-basedmodels,whichexcelinfeatureextraction. Furthermore,
feedforwarddeepneuralnetworks,NLP-basedmodelsfortext-basedchurnanalysis,and
representationandfeatureinteractiontechniques,whichenhancepredictiveperformance
bycapturinghigh-orderdependencies,areexplored.
AsnotedintheIntroduction,directcomparisonofreportedperformancemetricswas
avoidedduetosubstantialheterogeneityindatasets,evaluationprotocols,andmodeling
objectives across studies. Instead, a descriptive synthesis of individual study results is
presented.
Bystructuringtheexistingresearchintothishierarchicalframework,ourtaxonomy
providesaclearperspectiveontheevolutionofchurnpredictionmethodologies. Itunder-
scoreshowdifferentapproacheshavebeentailoredtoaddressthemultifacetedchallenges
ofchurnmodeling,fromenhancingpredictiveaccuracyandscalabilitytoimprovinginter-
pretabilityanddataefficiency.

Mach.Learn.Knowl.Extr.2025,7,105
14of38
6. MachineLearningApproaches
Machine learning methodologies have significantly enhanced churn prediction
through diverse approaches to address complex customer retention challenges across
various sectors. Recent research encompasses profit-driven models, ensemble learning
techniques,optimization-basedmethods,adaptiveresamplingstrategies,explainableartifi-
cialintelligence(XAI),andtraditionalalgorithms. Eachmethodologycontributesdistinct
advantagessuchasimprovedpredictiveaccuracy,enhancedinterpretability,computational
efficiency,andalignmentwithbusinessobjectives. Thissectionreviewstheseinnovative
approaches,outliningtheirmethodologies,datacharacteristics,andperformanceevalua-
tions,therebyprovidingvaluableguidanceforselectingsuitableMLtechniquesforspecific
churnpredictionapplications.
Table1brieflysummarizeseachstudybyindicatingthedatasettypesused(public,
private,orsynthetic),MLtechniquesemployed,andperformancemetricsevaluated.
Table1.ThesummaryofstudiesinthedomainofconventionalML.
| Category | Ref. Year | Dataset | TechniquesUsed | MetricsUsed |
| -------- | --------- | ------- | -------------- | ----------- |
AUC,Expected
MaximumProfitfor
|     | [16] 2020 | Public | DT,EvolutionaryAlgorithm |     |
| --- | --------- | ------ | ------------------------ | --- |
CustomerChurn
(EMPC)
Profit-centric
MinimaxProbabilityMachines(MPM),LASSO,
|     | [17] 2020 | Public |     | ProfitMaximization |
| --- | --------- | ------ | --- | ------------------ |
TikhonovRegularization
ExpectedMaximum
|     | [18] 2024 | Private | GradientBoosting |     |
| --- | --------- | ------- | ---------------- | --- |
ProfitforB2B(EMPB)
|     | [19] 2020 | Public | EnsembleLearning | Accuracy |
| --- | --------- | ------ | ---------------- | -------- |
Accuracy,ROCAUC,PR
[20] 2020 Private LogisticRegression,LogitBoost AUC,Precision,Recall,
MCC
|     |           |         | BoostedTreeAlgorithms(XGBoost,LightGBM, | Accuracy,AUC, |
| --- | --------- | ------- | --------------------------------------- | ------------- |
|     | [21] 2021 | Private |                                         |               |
CatBoost) Precision,Recall
StackingModel(XGBoost,LogisticRegression,DT,
|     | [22] 2021 | Private |     | Accuracy |
| --- | --------- | ------- | --- | -------- |
NaïveBayes)
Accuracy,Precision,
|     | [23] 2021 | Public | SVMs,BayesianClassifier,RF |     |
| --- | --------- | ------ | -------------------------- | --- |
Recall,F1-score
|     | [24] 2022 | Private | ArtificialNeuralNetworks,RF | Accuracy |
| --- | --------- | ------- | --------------------------- | -------- |
Ensembleand
|     | [25] 2022 | Public | DecisionForest,WeightedSoftVoting | Accuracy |
| --- | --------- | ------ | --------------------------------- | -------- |
HybridML
[26] 2022 Private MultilayerNeuralNetworks,AdaBoost,RF Accuracy,ROCAUC
[27] 2022 Private CatBoost,RecursiveFeatureElimination(RFE) Accuracy,F1-score
Clustering(k-means,k-medoids),Gradient
|     | [28] 2022 | Public | BoostingTrees,DT,RF,DeepLearning, | Accuracy |
| --- | --------- | ------ | --------------------------------- | -------- |
NaïveBayes
HybridEnsembleLearning,Two-Layer
|     | [29] 2022 | Public |     | Accuracy,F1-score |
| --- | --------- | ------ | --- | ----------------- |
FlexibleVoting
[30] 2023 Private EnsembleLearning,Nelder-MeadOptimization Accuracy
[31] 2023 Public WeightedEnsembleModel(XGBoost,RF) F1-score,ExecutionTime
[32] 2023 Private WeightedEnsembleModel,Powell’sOptimization Accuracy,F1-score
|     |           |                                           | QuantumSupportVectorMachine,Quantum | Accuracy,Precision, |
| --- | --------- | ----------------------------------------- | ----------------------------------- | ------------------- |
|     | [33] 2024 | Public                                    |                                     |                     |
|     |           | k-NearestNeighbors,andQuantumDecisionTree |                                     | Recall              |

Mach.Learn.Knowl.Extr.2025,7,105
15of38
Table1.Cont.
| Category | Ref. Year | Dataset |                                     | TechniquesUsed | MetricsUsed       |
| -------- | --------- | ------- | ----------------------------------- | -------------- | ----------------- |
|          |           |         | OptimalGeneticAlgorithm(OGA)withSVM |                | Accuracy,F-score, |
|          | [34] 2020 | Public  |                                     |                |                   |
|          |           |         | (OGA-SVM),Quantum-GeneticAlgorithm  |                | Sensitivity       |
SVMs,Multi-LayerPerceptron,RF,NaïveBayes,
|     | [35] 2021 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
FeatureSelection(InformationGain)
ImprovedSMOTE(ISMOTE)withanOptimal
WeightedExtremeLearningMachine(OWELM),
|     | [36] 2021 | Public |     |     | Accuracy,F-measure |
| --- | --------- | ------ | --- | --- | ------------------ |
Multi-objectiveRainOptimizationAlgorithm
(MOROA)
| Optimization |     |     | PrincipalComponentAnalysis(PCA), |     |     |
| ------------ | --- | --- | -------------------------------- | --- | --- |
AUC,MCC,F1-score,
| and | [37] 2022 | Public | Autoencoders,LinearDiscriminantAnalysis |     |     |
| --- | --------- | ------ | --------------------------------------- | --- | --- |
Kappa
Metaheuristic
(LDA),t-SNE,XGBoost,LightGBM
ML
AntColonyOptimizationwiththeReptileSearch
|     | [38] 2022 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
Algorithm(ACO-RSA)
SVMs,ParticleSwarmOptimization(PSO),
|     | [39] 2023 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
ArtificialEcosystemOptimization(AEO)
|     |           |        | PrincipalComponentAnalysis(PCA),GreyWolf |              | Accuracy,Recall,   |
| --- | --------- | ------ | ---------------------------------------- | ------------ | ------------------ |
|     | [40] 2023 | Public |                                          |              |                    |
|     |           |        | Optimization(GWO),SVMs                   |              | F1-score           |
|     | [41] 2023 | Public | ParticleSwarmOptimization,SVMs           |              | Accuracy           |
|     |           |        | ExtremeLearningMachine,GridSearch        |              | Accuracy,F1-score, |
|     | [42] 2023 | Public |                                          |              |                    |
|     |           |        |                                          | Optimization | ModifiedAccuracy   |
[43] 2022 Public AdaptiveChurnPrediction(OTCCD),SMOTE Accuracy
Precision,Recall,
|             | [44] 2023 | Public | NaiveBayes,EvolutionaryComputation |     |          |
| ----------- | --------- | ------ | ---------------------------------- | --- | -------- |
| Adaptiveand |           |        |                                    |     | F1-score |
Resampling [45] 2023 Public HybridStatisticalModelling Recall
Accuracy,Precision,
|     | [46] 2024 | Public | XGBoost,SMOTE-ENNResampling |     |     |
| --- | --------- | ------ | --------------------------- | --- | --- |
Recall,F1-score
[47] 2021 Public Spline-RuleEnsemble,SparseGroupLasso(SGL) AUC
| Explainable   |           |        | ShapleyAdditiveExplanations(SHAP)       |     |                   |
| ------------- | --------- | ------ | --------------------------------------- | --- | ----------------- |
|               | [48] 2022 | Public |                                         |     | Accuracy          |
| and           |           |        | ExplainableAI,CollaborativeFiltering    |     |                   |
| Interpretable |           |        |                                         |     | Interpretability, |
|               | [49] 2024 | Other  | ExplainableAI,SocialInteractionAnalysis |     |                   |
Decision-Making
[50] 2021 Private NaturalLanguageProcessing,InterpretableML Accuracy
|              |           |        | Entropy-basedMin-MaxSimilarity(E-MMSIM), |                     | F1-score,AUC, |
| ------------ | --------- | ------ | ---------------------------------------- | ------------------- | ------------- |
| Data-centric | [51] 2023 | Public |                                          |                     |               |
|              |           |        |                                          | TopicClassification | Accuracy      |
and
[52] 2023 Public SyntheticDataGeneration,Data-CentricAI Accuracy
Augmentation
Network-BasedFeatureEngineering,Gradient
|     | [53] 2024 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
Boosting
Accuracy,
|     | [54] 2020 | Public | CRISP-DM,LogisticRegression,RF |     |     |
| --- | --------- | ------ | ------------------------------ | --- | --- |
MisclassificationRate
[55] 2022 Public FisherDiscriminantAnalysis,LogisticRegression Accuracy
Accuracy,Precision,
|               | [56] 2023 | Private | LogisticRegressionwithMixedPenalty |     |        |
| ------------- | --------- | ------- | ---------------------------------- | --- | ------ |
| TraditionalML |           |         |                                    |     | Recall |
KNN,DTs,LogisticRegression,RF,SVM,
|     | [57] 2023 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
AdaBoost,GBM
|     | [58] 2024 | Private |     | RF       | F1-score,Recall |
| --- | --------- | ------- | --- | -------- | --------------- |
|     | [59] 2024 | Private |     | DTs,SVMs | Accuracy        |
6.1. Profit-CentricApproaches
Recent developments in churn prediction research reflect a growing emphasis on
aligningpredictivemodelswithbusinessobjectives,particularlyprofitability. Traditionally,
churn models have been optimized for accuracy-based metrics like AUC. Still, a shift
towardintegratingfinancialconsiderationsdirectlyintomodeltraininghasemergedas
criticalformoreimpactfulcustomerretentionstrategies.
Höppneretal.[16]exemplifythisshiftbyintroducingProfTree,aprofit-drivenDTtai-
loredexplicitlyforchurnprediction. Ratherthansolelyoptimizingclassificationaccuracy,

Mach.Learn.Knowl.Extr.2025,7,105 16of38
ProfTreeemploystheExpectedMaximumProfitforCustomerChurn(EMPC)metricto
constructDTsprioritisingprofitability. Themodelsystematicallyaccountsformisclassi-
ficationcostsandcustomer-specificeconomicvaluethroughanevolutionaryalgorithm.
ExperimentsontelecommunicationdatasetsdemonstratethatProfTreesignificantlyen-
hancesprofitcomparedtoconventionalaccuracy-centricapproaches, underscoringthe
importanceofprofit-centricpredictiveanalytics.
Buildingonsimilarprinciples,Maldonadoetal.[17]proposeaprofit-orientedchurn
predictionmodelutilizingMinimaxProbabilityMachines(MPM).Unliketraditionalmeth-
ods that often use profitability metrics only during post-model selection or threshold
adjustments, this approach directly integrates profit maximization into the classifier’s
trainingobjective. Theirframeworkincludesabaselinemodelandtworegularizedvari-
antsincorporatingLASSOandTikhonovregularizationtoensurerobustgeneralization.
Benchmarkevaluationsconfirmthattheseprofit-drivenMPMextensionsyieldsuperior
profitabilityoutcomesrelativetostandardbinaryclassifiers,emphasizingthenecessityof
embeddingbusinessobjectivesdirectlyintopredictivemodeling.
Extending this perspective into the business-to-business (B2B) domain, Janssens
etal.[18]introduceB2Boost, aninstance-dependentgradientboostingmodelexplicitly
designedforB2Bchurnscenarios. Recognizingcustomerheterogeneityinprofitability,they
proposetheExpectedMaximumProfitforB2Bchurn(EMPB)metrictoguidemodeltrain-
ing.B2Boostdirectlyoptimizescustomer-specificprofitratherthantraditionalclassification
accuracy,yieldingnotableprofitimprovementsoverstandardapproaches. Thesuccessful
applicationinB2Bcontextshighlightsthebroaderpotentialofprofit-centricmethodologies
beyondconsumermarkets.
Thesestudiesunderscorethenecessityofshiftingpredictivemodelingpracticesto-
ward profit-centric frameworks. By directly incorporating financial objectives, churn
predictionmodelsbecomemorealignedwithstrategicbusinessgoals,facilitatingmore
effectiveandeconomicallybeneficialcustomerretentionefforts.
6.2. EnsembleandHybridMLApproaches
Ensembleandhybridapproacheshaveemergedasrobustmethodologiesforenhanc-
ingcustomerchurnpredictionacrossvariousindustries. Byintegratingmultipleclassifiers,
clusteringtechniques,andadvancedfeatureengineeringmethods,theseapproacheshar-
ness the strengths of individual models to mitigate the limitations of single-algorithm
solutions. Thissectionprovidesacomprehensivereviewofkeystudiesthathavedemon-
stratedtheeffectivenessofensembleandhybridlearninginchurnprediction,highlighting
theircontributionstopredictiveaccuracy,modelrobustness,andreal-worldapplicability.
Whilebothhybridandensembleapproachescombinemultiplemodels,theirintegra-
tionstrategiesdiffer. Ensemblemethods,suchasbagging,boosting,andstacking,aimto
improvegeneralizationbyaggregatingthepredictionsofseveralbaselearners,typicallyof
thesameordifferenttypes,withoutalteringtheoriginalalgorithms. Incontrast,hybrid
methodsintegratedistinctalgorithmssequentiallyorinparallel,whereonemodel’soutput
or feature transformation becomes the input for another. For example, a hybrid model
mightuseclusteringforcustomersegmentation, followedbyclassificationwithineach
segment,orcombinefeatureengineeringviaCNNswithtemporalmodelingviaLSTMs.
Hybridsystemsaregenerallymorecustomizedandoftendomain-specific, whereasen-
semblemethodsfollowstandardizedcombiningruleslikemajorityvotingorweighted
averaging.
One notable study by Liu et al. [28] introduces a hybrid approach that integrates
clustering and classification algorithms to improve predictive accuracy in the telecom
sector. Their model employs k-means, k-medoids, and random clustering techniques

Mach.Learn.Knowl.Extr.2025,7,105 17of38
alongsideclassifierssuchasGradientBoostingTrees(GBT),DTs,RFs,DL,andNaïveBayes
(NB). The study reports significant performance improvements by leveraging stacking-
basedhybridization,with96%and93.6%accuracyontheOrangeandCell2Celldatasets.
Theseresultsemphasizethebenefitsofensemblelearningandclustering-basedfeature
enhancementinchurnprediction. Similarly,Rameshetal.[24]proposeahybridmodel
combiningANNsandRFstoenhancechurnpredictionintelecommunications. TheirANN
architecture,consistingoffourhiddenlayers,achieved90.34%accuracy,outperforming
standaloneRFandsimplerANNmodels. IntegratingANN’spredictivepowerwithRF’s
robustness effectively identifies churn factors, aiding telecom companies in proactive
customerretentionstrategies.
Using hybrid approaches, Usman-Hamza et al. [25] introduce Intelligent Decision
Forest (DF) models to address scalability issues and class imbalance in telecom churn
prediction. Theirapproachsignificantlyenhancesclassificationaccuracybyincorporating
LogisticModelTree(LMT),RF,andFunctionalTrees(FT)withinaweightedsoftvotingand
stackingframework.Thestudyunderscoresthepotentialofdecisionforest-basedmodelsin
handlingimbalanceddatasetsandimprovingchurndetectionacrosstelecommunications.
Saiasetal.[26]focusonchurnpredictionwithincloudserviceproviders,emphasizing
the importance of early detection in mitigating customer loss and optimizing resource
allocation. TheirMLframeworkevaluatesmultilayerneuralnetworks,AdaBoost,andRF
models,withRFemergingasthemosteffective,achievinganaccuracyof98.8%andan
AUCscoreof0.997. Thesefindingsreinforcetherelevanceofensemblelearningindynamic
serviceindustries.
Inthecontextofthewebcastingindustry,Fuetal.[30]employanensemblelearning-
basedchurnpredictionmodeloptimizedbytheNelder-Meadalgorithm. Theirapproach
extractshigh-dimensionalbehaviouralfeaturesfromtime-seriesdata,introducinganovel
churnindicatortoenhancelabelaccuracy. Thestudydemonstratessuperioroperational
efficiencyandoutperformanceoftraditionalensemblemodels,offeringactionableinsights
forcustomerretentionstrategies.
Optimizationtechniqueshavealsobeenexploredtorefineensemblemethods. Khoh
etal.[32]introduceanoptimizedweightedensemblemodeltailoredforthetelecommuni-
cationsindustry,integratingPowell’soptimizationalgorithmtoassigndifferentialweights
tobaselearnersbasedontheirpredictivestrength. Thismodelachievesanaccuracyof
84%andanF1-scoreof83.42%,surpassingconventionalMLapproaches. Yogeshetal.[29]
furthercontributetothisdomainbyproposingatwo-layerflexiblevotingensemble,demon-
stratingtheimpactofdatabalancingonimprovingclassificationperformance.
Boostedtreemodelshavegainedtractioninvariousindustriesfortheirefficiencyin
churnprediction.Marettaetal.[21]exploretheuseofXGBoost,LightGBM,andCatBoostin
bankingchurnprediction,findingLightGBMtobethemosteffectivewith91.4%accuracy,
94.8% AUC, and 87.7% recall. Similarly, Tianpei et al. [22] implement a stacking-based
ensemble framework combining XGBoost, Logistic Regression, DTs, and Naïve Bayes,
achieving98.09%accuracybyincorporatingfeaturegroupingtechniques.
A novel direction in ensemble learning is explored by Arshad et al. [33], who in-
troduce Q-Ensemble Learning, a quantum-enhanced ensemble approachincorporating
QuantumSupportVectorMachine(Q-SVM),Quantumk-NearestNeighbors(Q-kNN),and
QuantumDecisionTree(QDT).Byintegratingblockchaintechnologyfordatasecurityand
transparency,theirmodeloutperformsclassicalensemblemodels,achieving15%higher
accuracyand12%higherprecision,demonstratingthetransformativepotentialofquantum
computinginchurnprediction.
Ensemblemethodshavealsobeenappliedtoe-commercechurnprediction. Ishrat
etal.[27]presentanAI-drivenframeworkthatcombinesmodeltuning,featureselection,

Mach.Learn.Knowl.Extr.2025,7,105 18of38
andcomparativeanalysis,achieving100%accuracyandF1-scoreusingCatBoost. Manohar
etal.[23]investigateacollectivedataminingapproachintegratingSVMs,BayesianClas-
sifiers,andRF,highlightingthebenefitsofcombiningmultipleclassifiersforimproved
accuracyandrecall.
Otherstudieshavefocusedonrefiningtraditionalensembletechniques. Mahayasa
etal.[31]proposeaweightedaverageensemblecombiningXGBoostandRF,demonstrating
superiorpredictiveperformanceinthetelecomandinsurancesectors,withanF1-score
of0.850and0.947,respectively. Hemlataetal.[20]exploreLogisticRegressionandLogit
Boost for telecom churn prediction, confirming the efficacy of boosting techniques in
outperformingconventionalregressionmodels.
Finally,Wangetal.[19]provideacomparativeanalysisofwidelyusedclassification
algorithmsforchurnprediction,reinforcingtheimportanceofensemblelearninginenhanc-
ingmodelperformance. Theirbenchmarkingstudyoffersvaluableguidanceforbusinesses
seekingdata-drivenretentionstrategies.
Thesestudiesillustrateensembleandhybridapproaches’diverseandpracticalappli-
cationsincustomerchurnprediction. ByintegratingmultipleMLmodelsandleveraging
sophisticatedfeatureengineeringtechniques,thesemethodologiesproviderobust,scal-
able,andhigh-performingsolutionstothecomplexchallengeofcustomerretentionacross
variousindustries.
6.3. OptimizationandMetaheuristicApproaches
Optimizationandmetaheuristicapproacheshavegainedprominenceinchurnpre-
diction research as effective strategies for enhancing model performance and reducing
computationalcomplexity. Thesestudiesofferrobustframeworksthatimprovepredictive
accuracyandprovidegreaterinterpretabilityandactionableinsightsbyintegratingad-
vancedfeatureselectiontechniques,hyperparametertuning,andmetaheuristicalgorithms.
Thissectionreviewskeycontributionsthatemploythesetechniquestooptimizechurn
predictionmodelsacrossvariousdomains.
Feature selection plays a critical role in improving model efficiency and accuracy.
Saheed et al. [35] introduce an ML-based churn prediction framework for the telecom-
municationssector, leveragingInformationGainandRanker-basedfeatureselectionto
enhancemodelinterpretability. Theirapproach,whichincorporatesSVM,Multi-LayerPer-
ceptron(MLP),RF,andNaïveBayes,achievesa95.02%accuracyrate,surpassingthe92.92%
obtained without feature selection. These results highlight the importance of selecting
relevantchurn-relatedattributesforimprovedclassificationperformance.
Building on feature selection techniques, Al-Shourbaji et al. [38] propose a novel
hybridmethod, ACO-RSA,whichintegratesAntColonyOptimization(ACO)withthe
Reptile Search Algorithm (RSA) to enhance predictive performance. Evaluated across
multipleopen-sourcechurndatasets,ACO-RSAoutperformsParticleSwarmOptimization
(PSO),Multi-VerseOptimizer(MVO),andGreyWolfOptimizer(GWO),demonstrating
itseffectivenessinhandlinghigh-dimensionaltelecomdata. Thisstudyunderscoresthe
potential of metaheuristic approaches in refining feature selection for improved churn
detection.
Pustokhinaetal.[36]introducetheISMOTE-OWELMmodel,whichintegratesIm-
provedSMOTE(ISMOTE)fordatabalancingwithanOptimalWeightedExtremeLearning
Machine (OWELM) for classification. A Multi-objective Rain Optimization Algorithm
(MOROA)optimizessamplingratesandmodelparameters,yielding94%,92%,and90.9%
accuracyacrossthreetelecomdatasets,significantlysurpassingtraditionalapproaches. The
study emphasizes the effectiveness of ISMOTE-OWELM in improving churn detection

Mach.Learn.Knowl.Extr.2025,7,105 19of38
whilemaintainingcomputationalefficiency,makingitavaluabletoolfortelecomproviders
aimingtoenhancecustomerretentionefforts.
Incorporatinghyperparametertuningintofeatureselection,Mirabdolbaghietal.[37]
presentacomprehensivemodeloptimizationframeworkintegratingPrincipalComponent
Analysis(PCA),Autoencoders,LinearDiscriminantAnalysis(LDA),t-SNE,andXGBoost
forfeaturereduction. TheirapproachemploysBayesianandgeneticoptimizationtofine-
tuneLightGBMmodels,significantlyoutperformingAdaBoost,SVM,andDTclassifiers.
ThestudyalsoutilizesSHAPforfeatureimportanceinterpretationandintroducesaCus-
tomerLifetimeValue(CLV)rankingsystem,offeringactionableinsightsforprioritising
high-valuecustomersatriskofchurn.
Koçog˘luetal.[42]presentanExtremeLearningMachineapproachforcustomerchurn
prediction,optimizedusinggridsearchforhyperparametertuning. Thestudyutilizesa
churndatasetfromtheUCIMachineLearningRepositoryandcomparesELM’sperfor-
manceagainstNaïveBayes,k-NearestNeighbor,andSVMmodels.Theresultsdemonstrate
thatELMachievesthehighestaccuracyof93.1%,highlightingitsefficiencyinchurnpre-
dictionduetominimalparametertuningrequirementsandcompetitiveperformance. The
studyunderscoresELM’spotentialasarobustandeffectivetechniqueforchurnanalysis.
Metaheuristicoptimizationhasalsobeenexploredtoenhancegradientboostingtech-
niques. AlShourbajietal.[39]proposetheEnhancedGradientBoostingModel(EGBM),
whichintegratesanSVMRBFbaselearnerwithPSOandArtificialEcosystemOptimization
(AEO)forhyperparametertuning. Evaluatedonseventelecomdatasets,EGBMdemon-
strates superior predictive capabilities compared to traditional GBM and SVM models,
effectivelyaddressingprematureconvergenceandenhancingcustomerretentionstrategies.
Hybridoptimizationapproachesfurtherimprovechurnpredictionefficiency. Kurtcan
etal.[40]introducePCA-GWO-SVM,amodelcombiningPrincipalComponentAnalysis
(PCA)forfeatureselection,GreyWolfOptimizationforhyperparametertuning,andSVM
forclassification. Comparedtologisticregression,k-nearestneighbors,naïveBayes,and
DTs,PCA-GWO-SVMachieveshigheraccuracy,recall,andF1-score,reinforcingthevalue
ofcombiningoptimizationtechniqueswithclassificationframeworks.
Ponnusamyetal.[41]employaPSO-SVM-basedalgorithmtoenhancechurnpredic-
tion performance in the banking sector. By optimizing hyperparameters using Particle
SwarmOptimization,theirapproachsignificantlyoutperformstraditionalSVMmodels,
demonstratingtheeffectivenessofhybridoptimizationstrategiesforfinancialinstitutions
seekingtominimizecustomerattrition. Similarly,Venkateshetal.[34]proposeanOptimal
GeneticAlgorithm(OGA)withSVMforcloud-basedchurnprediction. Theirapproach
utilizes a double-chain quantum genetic algorithm to fine-tune SVM hyperparameters,
achievinghighsensitivity(94.50),accuracy(90.27),andanF-scoreof94.30. Thesefindings
underscoretheeffectivenessofgeneticoptimizationinenhancingpredictiveperformance,
makingitapromisingtechniqueforlarge-scalecloud-basedanalytics.
Thesestudiesillustratehowoptimizationandmetaheuristicapproachessignificantly
improvechurnpredictionmodels’accuracy,efficiency,andinterpretability. Byintegrat-
ingadvancedfeatureselection,hyperparametertuning,andmetaheuristicoptimization,
thesemethodologiesprovidescalableandhigh-performingsolutionsforindustriesgrap-
plingwithcomplexcustomerdata,ultimatelyenhancingretentionstrategiesandbusiness
decision-making.
6.4. AdaptiveandResamplingApproaches
In dynamic environments where customer behaviour and data distributions con-
tinuously evolve, addressing class imbalance and adapting to concept drift are critical
challengesinchurnprediction. Researchershaveincreasinglyturnedtoresamplingand

Mach.Learn.Knowl.Extr.2025,7,105 20of38
adaptivelearningstrategiestoenhancemodelperformanceinreal-timeapplications. This
sectionreviewskeystudiesthatemploythesetechniquestomitigateimbalancesandadapt
predictivemodelstochangingdatapatterns,ensuringmoreaccurateandreliablechurn
detection.
Ahmadetal.[43]introducetheOptimizedTwo-SidedCumulativeSumChurnDetec-
tor(OTCCD),anoveladaptivechurnpredictionframeworkfortelecomdatastreams. By
integratingtheSyntheticMinorityOver-samplingTechnique(SMOTE)fordatabalancing
andacumulativesumcontrolchartfordriftdetection,OTCCDefficientlyidentifiesshifts
incustomerbehaviourwithinaslidingwindowframework. Experimentalevaluations
on real-world telecom datasets, such as Call Detail Records, demonstrate that OTCCD
outperformstraditionalmethodsbyprovidinghigheraccuracyandfasterdriftdetection.
Thisstudyhighlightstheimportanceofreal-timeadaptabilityinchurnpredictionmodels,
offeringtelecomcompaniesarobusttoolforproactivecustomerretentionstrategies.
Adnanetal.[44]proposeanadaptivelearningapproachthatintegratesevolutionary
computationwithaNaïveBayesclassifiertoaddressclassimbalanceintelecommunications
churnprediction. Bydynamicallyadjustingmodelparametersbasedonincomingdata
patterns,thehybridmethodsignificantlyimprovesprecision,recall,andF1scorescompared
totraditionalapproaches. Evaluationsonreal-worldtelecomdatasetsconfirmthemodel’s
effectivenessinproactivelyidentifyingat-riskcustomers, underscoringthepotentialof
adaptivelearninginminimizingrevenuelossduetocustomerchurn.
Complementingadaptivemethodologies,Shimaaetal.[46]developahybridchurn
predictionframeworkthatcombinesXGBoostwithSMOTE-ENNresamplingtobalance
datasetsandimproveclassificationaccuracy. Thisintegrationenhancesprecision,recall,
andF1scores,outperformingconventionalMLtechniquesacrossthreetelecomdatasets.
Byeffectivelyaddressingclassimbalanceandleveragingensemblelearning,themodel
facilitatesproactiveretentionstrategies,reinforcingtheroleofresamplingtechniquesin
churnprediction.
Incorporating a more customer-centric approach, Lee et al. [45] propose a hybrid
churnpredictionframeworkthatdynamicallymodelschurnprobabilitybasedoncustomer
lifetimevalueratherthanfixedperiods. Bysegmentingcustomersintogroupssuchas
new,short-term,high-value,andchurn-proneusers,theirmethodologyappliestailored
MLmodelstoenhancepredictiveaccuracy. EvaluationsofdatasetsfromaU.K.giftseller
andPakistan’smostsignificante-commerceplatformshowrecallscoresrangingfrom0.56
to 0.72 in one case and 0.91 to 0.95 in another. The study highlights the advantages of
integratingstatisticalmodelingwithMLtechniquestorefinecustomerretentionstrategies
whilereducingdatarequirements.
Thesestudiesillustratehowadaptiveandresamplingapproacheseffectivelyaddress
class imbalance and concept drift, enabling more scalable and robust churn prediction
solutions. Byintegratingreal-timelearning,resamplingtechniques,andevolutionaryopti-
mization,thesemethodologiesprovidepowerfultoolsforbusinessesseekingtoenhance
customerretentionstrategiesinevolvingmarketconditions.
6.5. ExplainableandInterpretableApproaches
Understandingtheunderlyingdecisionprocessesincomplexpredictivetaskssuchas
churnpredictioniscrucialforgainingstakeholdertrustandfacilitatingactionableinsights.
Recentresearchhasincreasinglyfocusedonintegratinginterpretabilityandexplainable
AItechniquesintochurnpredictionmodels. Thissectionreviewskeycontributionsthat
enhancemodeltransparencythroughrule-basedformulations,SHAPanalyses,andother
XAImethodologies.

Mach.Learn.Knowl.Extr.2025,7,105 21of38
DeBocketal.[47]introduceSpline-RuleEnsembleclassifierswithStructuredSpar-
sityRegularization(SRE-SGL)asaninterpretableapproachtocustomerchurnprediction.
WhiletraditionalMLmodelsoftenprioritisepredictiveaccuracy,thisstudyemphasizesthe
needforexplainablemodelsthatprovideactionableinsightsintocustomerbehaviour. The
proposedspline-ruleensemblesintegratetree-basedensemblemethodswithregression
analysis, balancing model flexibility and simplicity. However, conventional rule-based
ensemblescanbecomeexcessivelycomplexduetoconflictingcomponents. Toaddressthis,
theauthorsincorporateSparseGroupLassoregularization,whichenhancesinterpretability
byenforcingstructuredsparsity. Evaluationsacrossfourteenreal-worlddatasetsdemon-
stratethatSRE-SGLoutperformsstandardruleensemblesinAUCandtopdecileliftwhile
maintainingcompetitivepredictiveperformance. Acasestudyinthetelecommunications
sectorfurtherillustratesthemodel’sinterpretability,reinforcingthevalueofstructured
regularizationinmakingchurnpredictionbotheffectiveandexplainable.
Extendinginterpretabilitytechniquestoworkforceanalytics,Mitravindaetal.[48]
investigateemployeeattritionpredictionusingMLmodelsandXAImethodologies. Their
study applies SHAP to identify key factors driving attrition and visualize their impact.
Additionally, the research introduces a recommendation system leveraging user-based
collaborativefilteringtoproposepersonalizedretentionstrategies.Bycombiningpredictive
modelingwithactionableinsights,thisstudydemonstrateshowXAItechniquescaninform
moreeffectiveemployeeretentionpolicies.
Indigitalentertainment,Wangetal.[49]addressthechallengeofplayerchurnpre-
dictioninonlinevideogames,whereunderstandingsocialinteractiondynamicsiscritical.
WhileMLmodelsarewidelyusedforplayerbehaviouranalysis,theirblack-boxnature
limitsadoptionbyproductmanagersandgamedesigners. Thestudyrestructuresmodel
inputsintoexplicitandimplicitfeaturestobridgethisgap,enhancingexpertinterpretabil-
ity. Furthermore, the research highlights the necessity of XAI techniques that explain
featurecontributionsandprovideactionablerecommendationsforreducingchurn. The
proposedapproachisvalidatedthroughtwocasestudiesinvolvingexpertfeedbackanda
within-subjectuserstudy,demonstratingitseffectivenessinimprovingdecision-making
forplayerretentionstrategies.
Together,thesestudiesillustratethecrucialroleofinterpretabilityinchurnprediction
models. ByintegratingadvancedXAItechniques,researchersbridgethegapbetweenhigh
predictive performance and the need for transparent, actionable insights. This integra-
tionsupportsmoreinformedandeffectiveretentionstrategiesacrossdiverseindustries,
reinforcingthevalueofexplainableAIinreal-worldpredictiveanalytics.
6.6. Data-CentricandAugmentationApproaches
Beyondrefiningpredictivemodels,recentresearchinchurnpredictionhasincreasingly
emphasizedenhancingthequalityanddiversityoftrainingdata. Data-centricandaugmen-
tationapproachesseektoenrichtraditionaldatasetsbyincorporatingnoveldatasources,
generatingsyntheticdata,andleveragingadvancedfeatureengineeringtechniques. These
strategiesarecrucialforimprovingmodelrobustness,addressingdataimbalances,and
achievinghigherpredictiveaccuracy. Thissectionreviewskeycontributionsthatexemplify
theseefforts.
Voetal.[50]exploreanovelchurnpredictionapproachthatintegratesunstructured
calllogdatawithtraditionalstructureddata. WhileexistingMLmodelsprimarilyrely
ondemographicandaccounthistorydata,thisstudyhighlightstheuntappedpotentialof
analyzingspokencontentfromcustomerinteractions. Usingnaturallanguageprocessing
techniques,theauthorsprocessalarge-scalecallcenterdatasetcontainingtwomillioncalls
fromover200,000customers. Theirfindingsdemonstratethatincorporatingunstructured

Mach.Learn.Knowl.Extr.2025,7,105 22of38
calldatasignificantlyenhancespredictionaccuracywhileprovidingdeeperinsightsinto
customerbehaviour. Additionally,interpretableMLtechniquesextractpersonalitytraits
andcustomersegmentationpatterns,facilitatingpersonalizedretentionstrategies. This
studyunderscorestheimportanceofcombiningstructuredandunstructureddatasources
to develop more comprehensive churn prediction frameworks in the financial services
industry.
Soumietal.[51]addressthechallengeofoptimizingtrainingdataqualitythrougha
representation-basedquerystrategyforchurnprediction. Givenmanualdataannotation’s
high cost and inefficiency, the authors propose Entropy-based Min-Max Similarity (E-
MMSIM),anactivelearningalgorithminspiredbyproteinsequencingtechniques. This
methodselectsthemostinformativeandrepresentativedatapointsforannotation,reducing
redundancyandimprovingmodelefficiency. Theapproachenhancestopicclassification
accuracyincustomerservicemessages,yieldingsignificantimprovementsinF1-score,AUC,
andoverallmodelperformance. Moreover,whenthesequalitativefeaturesareintegrated
withstructuredcustomerdata,churnpredictionmodelsachievea5%performancegain.
ThestudyhighlightsthecriticalroleofdataselectionstrategiesinoptimizingMLworkflows
forcustomerretentionmanagement.
Intherealmofsyntheticdatageneration,Wangetal.[52]exploretheimpactofdata-
centric AI on churn prediction. Unlike traditional model-centric AI, which focuses on
hyperparametertuningandalgorithmmodifications,data-centricAIenhancespredictive
performancebyimprovingtrainingdataqualityanddistribution. Thisresearchevaluates
variousdatasynthesisalgorithms,examiningtheireffectsondatabalancing,augmenta-
tion,andsubstitution. Thefindingsunderscorethepotentialofresamplingmethodsin
mitigatingclassimbalanceandimprovingmodelrobustness,providingvaluableinsights
forAI-drivenchurnpredictionframeworksacrossindustries.
Babaketal.[53]introduceasocialnetwork-basedchurnpredictionmodel,recognizing
thatsocialinteractionsandpeerbehaviourofteninfluencecustomerchurn.Thestudydevel-
opsafeatureengineeringapproachincorporatinginfluenceandconformityindicesderived
fromcallnetworkdata. Byintegratingsocialconnectivitymetrics,themodelsignificantly
enhancesthepredictivepowerofstandardMLclassifiers,particularlygradientboosting
models. Thisresearchdemonstratesthatchurnisnotsolelyanindividualdecisionbutis
shapedbybroadersocialdynamics. Thisperspectiveextendsbeyondtelecommunications
tovariousindustrieswherepeerinfluenceaffectscustomerbehaviour.
Collectively,thesestudiesillustratethetransformativeimpactofdataaugmentation
andqualityimprovementinchurnprediction. Researchersaredevelopingmorecompre-
hensiveandrobustpredictiveframeworksbyincorporatingnoveldatasources,employing
activelearningfordataselection,generatingsyntheticdata,andleveragingsocialnetwork
information. Theseadvancementsenhancemodelaccuracyandprovidedeeperinsights
intocustomerbehaviour,enablingmoreeffectiveandproactiveretentionstrategies.
6.7. TraditionalMLApproaches
Traditional machine learning approaches significantly influence churn prediction
byleveragingestablishedstatisticalandalgorithmictechniques. Thesemethodsrelyon
classicalmodelsandfeatureengineeringtoderiveactionableinsightsandachievehigh
predictiveaccuracy. Thissectionhighlightskeystudiesthatexemplifytheapplicationof
conventionalMLmethodologiesacrossdiversedomains.
Tianyuanetal.[55]presentadata-drivenapproachtocustomerchurnpredictionin
telecommunications,incorporatingcustomersegmentationtoenhancepredictiveaccuracy.
UsingFisherdiscriminantanalysisandlogisticregression,theirmodelachievesa93.94%
accuracy rate on telecom datasets, effectively identifying potential churners. Tailoring

Mach.Learn.Knowl.Extr.2025,7,105 23of38
predictions to specific customer groups enhances the precision of retention campaigns,
providingtelecomoperatorswithapowerfultooltoproactivelyreducechurnandimprove
profitability. The study underscores the significance of segmentation in refining churn
predictionmodels.
Expanding on customer relationship management (CRM) applications, Šimovic´
et al. [56] explore churn prediction using big data analytics to analyze heterogeneous
customer behaviours, such as self-care service usage, service duration, and responsive-
nesstomarketingefforts. Theirstudyintroducesanenhancedlogisticregressionmodel
withamixedpenaltytermtomitigateoverfittingandbalancefeatureselection. Empirical
evaluationonalargeCRMdatasetdemonstrateshighclassificationperformanceacross
standardmetrics,reinforcingthepotentialofpenalizedlogisticregressionasascalableand
computationallyefficientapproachtochurnmodelinginbigdataenvironments.
Jakobetal.[58]extendtraditionalMLtechniquestothedigitalhealthsector,investigat-
ingearlyuserchurninaweightlossapp. Byanalyzingengagementdatafrom1283users
and310,845eventlogs,thestudyemploysanRFmodeltopredictuserdropoutbasedon
dailylogincounts. AchievinganF1scoreof0.87onday7andidentifying93%ofchurned
users,thestudyhighlightshowchurnpredictioncanenablepersonalizedretentionstrate-
giesindigitalhealthinterventions,ultimatelyimprovinglong-termuserengagementand
healthoutcomes.
Returningtothetelecommunicationsindustry,Sikrietal.[59]developedanML-based
approachforimprovingcustomerretention. Byanalyzingcustomerdemographics,usage
patterns, and service details, the study applies DTs and SVM to identify customers at
riskofchurning. Theresultsdemonstratehighpredictiveaccuracy,empoweringtelecom
companiestoimplementtargetedretentionstrategieseffectively. Thisstudyreaffirmsthe
valueofconventionalMLtechniquesincustomerretentionefforts.
Expandingonreal-timepredictionapplications,Nyashadzasheetal.[54]developeda
churnpredictionmodeltailoredforthetelecommunicationsindustry,specificallyfocusing
onprepaidcustomerswhofrequentlyswitchproviders. UsingWatsonStudio,theirstudy
employs big data analytics within the CRISP-DM framework and evaluates three ML
algorithms—Logistic Regression, RF, and DT. While Logistic Regression exhibited the
lowest misclassification rate (2.2%), RF and DT achieved relatively high accuracy rates
(78.3%and79.2%,respectively)butsufferedfrommisclassificationratesabove20%. This
researchunderscoresthelimitationsofrelyingsolelyonaccuracymetricsandadvocates
for more comprehensive evaluation techniques to enhance real-time churn prediction
performance.
Beyond customer churn, AbdElminaam et al. [57] introduce EmpTurnoverML, an
AI-drivenapproachforpredictingemployeeturnoverandcustomerchurnusingMLalgo-
rithms. Thestudyevaluatesvariousclassificationtechniques,includingK-NearestNeigh-
bors,DTs,LogisticRegression,RF,SVM,AdaBoost,NaïveBayes,andGradientBoosted
Machines(GBM),usingan80-20train-testsplit. Byidentifyingkeypatternsassociatedwith
employeedepartures,thestudyhighlightshowAI-poweredpredictionmodelscanhelp
organizationsimplementproactiveretentionstrategies,reducinghiringandtrainingcosts
whileenhancingworkforcestability. Thefindingsdemonstratethebroaderapplicabilityof
churnpredictionmethodologiesinworkforceanalyticsandbusinessefficiency.
ThesestudiesillustratethecontinuedrelevanceofconventionalMLapproachesin
churnprediction. Throughrigorousmodeldevelopmentandstrategicfeatureengineering,
these methodologies provide potent tools for organizations seeking to mitigate churn,
improvecustomerandemployeeretention,anddrivesustainablebusinessgrowth. Overall,
traditional ML methods such as decision trees, logistic regression, and support vector
machinesremainvaluedfortheirinterpretability, computationalefficiency, andeaseof

Mach.Learn.Knowl.Extr.2025,7,105
24of38
deployment. However,theymaystrugglewithhigh-dimensionalorsequentialdata,and
theirperformanceisoftenlimitedcomparedtomoreadvancedensembleapproaches.
7. DeepLearningApproaches
Deeplearningtechniqueshavesignificantlyadvancedchurnpredictionbyofferingdi-
versemethodologiesthataddresscomplexuserbehaviourpatternsandindustryretention
challenges. Recentadvancementsincludedeepreinforcementlearning,sequentialmod-
elingwitharchitectureslikeLSTMs,hybridandensemblemethodsintegratingmultiple
DLparadigms,CNNstailoredforstructureddata,efficientfeedforwardneuralnetworks,
and innovative representation learning and feature interaction models. Each category
providesuniquestrengths,suchasimprovedaccuracy,enhancedinterpretability,orcom-
putationalefficiency,collectivelysupportingproactiveandeffectivechurnmanagement
strategies. Thissectionexploresthesedistinctapproaches,highlightingtheirapplications,
advantages,andcontributionstopredictiveanalytics. Table2highlightsthedatasetsused
(public,private,simulation-based),DLtechniquesimplemented,andperformancemetrics
evaluated.
Table2.ThesummaryofthestudiesinthedomainofDL.
| Category | Ref. Year | Dataset | TechniquesUsed |     | MetricsUsed |
| -------- | --------- | ------- | -------------- | --- | ----------- |
DeepReinforcement
|     | [60] 2020 | Simulation | DeepReinforcementLearning |     | Accuracy |
| --- | --------- | ---------- | ------------------------- | --- | -------- |
Learning
|     | [61] 2020 | Public | Trajectory-basedLSTM(TR-LSTM) |     | ROCAUC |
| --- | --------- | ------ | ----------------------------- | --- | ------ |
AUC,F1-Score,
|     | [62] 2020 | Public | LSTM-basedDynamicChurnModel |     | LogLoss,Lift, |
| --- | --------- | ------ | --------------------------- | --- | ------------- |
EMPC
| Temporaland |     |     | LSTMandGatedRecurrentUnit(GRU) |     |     |
| ----------- | --- | --- | ------------------------------ | --- | --- |
SequentialDL
[63] 2024 Private networks,LightGBM,SHAP,Explainable AUC,F1-score
BoostingMachines(EBM)
Accuracy,
|     | [64] 2024 | Public |     | LSTM | Precision,Recall, |
| --- | --------- | ------ | --- | ---- | ----------------- |
F1-score
AttentionalDLmodel(AttnBLSTM-CNN)
F1-score,ROC
|     | [65] 2022 | Private | integratedwithBidirectionalLSTMs |     |     |
| --- | --------- | ------- | -------------------------------- | --- | --- |
AUC
(BiLSTM)andCNNs
StackedBidirectionalLSTMs(SBLSTM)
andRNNswithanarithmeticoptimization
| Ensembleand | [66] 2023 | Private |     |     | Accuracy |
| ----------- | --------- | ------- | --- | --- | -------- |
algorithm(AOA),ImprovedGravitational
HybridDL
SearchOptimizationAlgorithm(IGSA)
[67] 2023 Public K-MeansClustering,Self-AttentionLSTM AUC,F1-score
Accuracy,
[68] 2024 Private StackedDNNs,LogisticRegression Precision,Recall,
F1-score
Accuracy,ROC
|     | [69] 2021 | Public | ComparativeCNNs,LSTMs |     |     |
| --- | --------- | ------ | --------------------- | --- | --- |
AUC,G-Mean
CNNs,ExtendedConvolutionalDecision
CNN–based
[70] 2022 Private Trees(ECDT)integratedwithGridSearch Accuracy
Optimization
|     | [71] 2024 | Public | 1DCNN,ResidualBlocks,Attention |     | Accuracy |
| --- | --------- | ------ | ------------------------------ | --- | -------- |
|     | [72] 2020 | Public | DNN,RF,XGBoost                 |     | Accuracy |
FeedforwardDeep
Multi-LayerPerceptron,RadialBasis
| NeuralNetwork | [73] 2024 | Public |     |     | Accuracy |
| ------------- | --------- | ------ | --- | --- | -------- |
Function(RBF)Networks
| NLP-basedDL | [74] 2021 | Private |                                | NLP,RNNs | F1-score |
| ----------- | --------- | ------- | ------------------------------ | -------- | -------- |
|             | [75] 2020 | Public  | FeatureInteractionNetwork(FIN) |          | Accuracy |
Representationand
FeatureInteraction [76] 2021 Public VectorEmbeddingsforChurn F1-score

Mach.Learn.Knowl.Extr.2025,7,105 25of38
7.1. DeepReinforcementLearningApproaches
Deepreinforcementlearningapproachesrepresentanemergingparadigminchurn
prediction,particularlywithindynamicenvironmentssuchasdigitalentertainment. These
methodsgobeyondtraditionalsupervisedlearningbyleveragingsimulation-basedtech-
niquestomodelcomplexuserbehavioursandengagementdynamics. Thissectionhigh-
lightsapioneeringstudythatexemplifiesthepotentialofdeepreinforcementlearningin
addressingchurnchallengesinmobilegaming.
Roohietal.[60]introduceanovelsimulation-basedmodelforpredictingchurnin
mobilegaming. UnliketraditionalsupervisedMLmodelsthatrelyonhistoricalplayer
data,thisworkintegratesDeepReinforcementLearningtosimulateAI-drivengameplay
behaviour, capturing in-game difficulty and player skill evolution. A key strength of
thisapproachisitsabilitytomodelplayerpersistenceandengagementdynamicswithout
requiringextensivereal-worldbehaviouraldata.Thestudydemonstratesthatincorporating
apopulation-levelsimulationofplayerheterogeneityimproveschurnpredictionaccuracy,
therebyreducingthedependencyonexpensiveretrainingofDRLagents. Thisframework
offers a promising direction for churn analysis in digital entertainment, where player
retentionstrategiesarecriticalforrevenuesustainability.
7.2. TemporalandSequentialDLApproaches
TemporalandsequentialDLapproacheshaveemergedasessentialtoolsforcapturing
thedynamicnatureofcustomerbehaviourinchurnprediction. Byleveragingtemporal
dependencies inherent in user engagement data, these models enable a more nuanced
understandingofchurnpatterns,ultimatelyleadingtomoreeffectiveretentionstrategies.
Thissectionreviewsrecentstudiesthatutilizedeepsequentialarchitectures,suchasLSTM
networks,toenhancechurnpredictionperformance.
Joyetal.[63]presentahybridDLapproachthatintegratessequentialmodelingwith
explainableAItoimprovechurnpredictioninstreamingservices.Theproposedframework
combinesLSTMandGatedRecurrentUnit(GRU)networkstocapturetemporaltrendsin
userengagement,complementedbyLightGBMtorefinepredictiveperformance. Akey
contributionofthisstudyisitsemphasisoninterpretability,employingShapleyAdditive
ExplanationsandExplainableBoostingMachines(EBM)toprovidetransparencyinfeature
importancerankings. Byensuringthatdecision-makersunderstandthereasoningbehind
churnpredictions,themodelenhancesactionableinsightsforbusinessapplications. The
studyreportsstate-of-the-artperformance,achievinga95.60%AUCanda90.09%F1score,
reinforcingtheeffectivenessofhybridarchitecturesinchurnanalysis.
ExpandingonsequentialDLtechniques,Zhuetal.[61]introduceatrajectory-based
LSTMframework(TR-LSTM)forchurnprediction,whichextractsthreetrajectory-based
featuresfromcustomermovementdata. Themodelsignificantlyoutperformstraditional
methods, demonstrating the utility of spatiotemporal behaviour analysis in predicting
churn. Similarly, Alboukaey et al. [62] emphasize the importance of daily behavioural
patternsbydevelopinganLSTM-baseddynamicchurnpredictionmodelformobiletelecom
customers. Unlike conventional monthly-based models, this approach captures short-
term fluctuations in customer activity, enhancing prediction accuracy and allowing for
more timely interventions. These findings underscore the superiority of LSTM-based
architectures in modeling evolving user engagement patterns, particularly in dynamic
serviceindustries.
FurthervalidatingtheeffectivenessofLSTMs,Beltozar-Clementeetal.[64]demon-
stratethatdeepsequentialnetworkscanovercomevanishinggradientissuesandeffectively
modellong-termdependenciesincustomerbehavioursequences.Theirstudyachieves95%

Mach.Learn.Knowl.Extr.2025,7,105 26of38
performanceacrossmultipleevaluationmetrics,highlightingthepotentialofLSTM-based
modelstorefinechurnpredictionbycapturingcomplexbehaviouraltrends.
Collectively,thesestudiesestablishsequentialandtemporalDLapproachesasrobust
toolsforchurnprediction. ByleveragingLSTM-basedarchitectures,thesemodelsoffer
enhanced predictive accuracy, more profound insights into user behaviour, and timely
interventions,makingtheminvaluablefordevelopingproactiveretentionstrategiesacross
variousindustries.
7.3. EnsembleandHybridDLApproaches
EnsembleandHybridDLapproacheshavegainedsignificanttractioninchurnpredic-
tionduetotheirabilitytocombinemultiplemodels’strengthsandovercomeindividual
architectures’limitations. Theseapproachesachieveenhancedpredictiveaccuracyand
improvedgeneralizationacrossdiverseapplicationdomainsbyintegratingDLtechniques,
suchasRNNs,CNNs,andattentionmechanisms,withensemblemethodsandoptimization
algorithms. Thissectionhighlightskeystudiesthatexemplifytheeffectivenessofhybrid
andensemblestrategiesinchurnprediction.
Jajametal.[66]introduceanensemblemodelthatintegratesStackedBidirectional
LSTMs(SBLSTM)andRNNswithanarithmeticoptimizationalgorithm(AOA).Theframe-
workisfine-tunedusinganimprovedGravitationalSearchOptimizationAlgorithm(IGSA),
achievingastate-of-the-artaccuracyof97.89%intheinsurancedomain. Theseresultshigh-
lightthepotentialofensemblearchitecturestoeffectivelymergemultipleDLtechniques,
improvinggeneralizationandperformanceinchurnpredictiontasks.
Similarly,Liuetal.[65]presentafusedattentionalDLmodel(AttnBLSTM-CNN)that
integratesBidirectionalLSTMs(BiLSTM)andCNNstoaddressthelimitationsofstandalone
RNNsandCNNs.Byincorporatinganattentionmechanism,themodelenhancesprediction
accuracy by prioritising critical customer behaviour patterns. The study demonstrates
thatintegratingattentionlayersintoDLpipelinesimproveschurndetectionaccuracyand
enhancesinterpretability,providingvaluableinsightsforfinancialinstitutions.
Expandingonhybridarchitecturesinthefinancialsector,Van-Hieuetal.[68]propose
aDLensemblemodelforcustomerchurnpredictioninbanking. Theapproachemploys
astackedDLarchitecturewhereLevel0integratesthreedistinctdeepneuralnetworks,
andLevel1utilizesalogisticregressionmodelforfinalprediction. TestedontheBank
Customer Churn Prediction dataset, the framework achieves 96.60% accuracy, 90.26%
precision,91.91%recall,andanF1-scoreof91.07%. Theseresultshighlighttherobustness
ofcombiningDLmodelswithlogisticregressiontoimprovechurnpredictionaccuracy,
reinforcingthevalueofensemblemethodologiesinfinancialcustomerretentionstrategies.
Zhaoetal.[67]furtherenhancechurnpredictionbyintegratingunsupervisedand
supervised learning techniques. Their hybrid model incorporates K-means clustering,
entropy-basedmethods,andcustomerportraitanalysisforsegmentingtelecomcustomers.
Amulti-headself-attention-basednestedLSTMclassifieristhenappliedtoevaluatecus-
tomerbehaviour.TestedonChina’stelecommarketdata,themodeloutperformstraditional
classificationmethodsbyimprovingtheaccuracyofcustomerbehaviourrecognition. Ad-
ditionally,iteffectivelydifferentiatesbetweenmedium-valueandhigh-valuecustomers,
providingcriticalinsightsforprecisionmarketingstrategiesandenablingtelecomcompa-
niestotailorserviceofferingsmoreeffectively.
Collectively,thesestudiesillustratethathybridandensembleDLapproachesenhance
predictiveaccuracyandimprovemodelinterpretabilityandgeneralizationacrosssectors.
Theirinnovativeintegrationofdiversemethodologiesofferspromisingavenuesfordevel-
opingrobust,scalablechurnpredictionsystemsthateffectivelysupporttargetedretention
strategies.

Mach.Learn.Knowl.Extr.2025,7,105 27of38
7.4. CNN–BasedApproaches
ConvolutionalNeuralNetworkshaveemergedasapowerfultoolinchurnprediction,
particularlyfortasksrequiringcomplexfeatureextractionandhierarchicaldatarepresen-
tation. Whiletraditionallyappliedtoimageandtextprocessing,CNN-basedapproaches
haveproveneffectiveinstructureddatascenarios,offeringimprovedpredictiveaccuracy
and addressing challenges such as class imbalance and information loss. This section
reviewskeystudiesthatleverageCNNs—oftenincombinationwithothertechniques—to
enhancechurnpredictionmodels.
Muhammad et al. [69] compare DL architectures on benchmark datasets such as
Cell2CellandKDDCupforchurnprediction. TheirfindingsidentifyCNNsasthemost
effectivemodelbasedonmultipleevaluationcriteria,outperformingtraditionalMLalgo-
rithmsandDLmodels. Theseresultsunderscoretheabilityofconvolutionalarchitectures
tocapturehierarchicalrelationshipswithincustomerdata,particularlyinscenarioswhere
featureextractionposessignificantchallenges.
Extending CNN applications to workforce analytics, Ebru et al. [70] introduce a
hybrid model (ECDT-GRID) for employee churn prediction. This approach integrates
ExtendedConvolutionalDecisionTrees(ECDT)withgridsearchoptimizationtoenhance
classificationaccuracy.UnlikeconventionalCNNapplicationsinimageandtextprocessing,
thisstudyadaptsCNNsforstructurednumericaldata,addressinginformationlossthrough
DT-basedlearning. TheECDT-GRIDmodeloutperformsCNN,ECDT,andtraditionalML
models,demonstratingtheimportanceofhyperparametertuninginimprovingpredictive
performance. ThestudyhighlightsthepotentialofDLinworkforceanalytics,particularly
inretail,whereemployeechurnimpactsoperationalstability. BycombiningCNNswith
DTstructures,thisapproachprovidesarobustpredictiveframework,showcasingtherole
ofDLinoptimizingemployeeretentionstrategies.
Sahaetal.[71]introduceChurnNet, anovelDL-basedchurnpredictionmodeltai-
loredforthetelecommunicationsindustry(TCI).Recognizingtheimportanceofcustomer
retentioninacompetitivemarket,thestudyaimstoenhancepredictiveaccuracybeyond
existing methods. ChurnNet integrates a 1D convolutional layer with residual blocks,
squeeze-and-excitationblocks,andaspatialattentionmodule,allowingthemodeltocap-
turecomplexfeaturedependencieswhilemitigatingthevanishinggradientproblem. The
model is evaluated using three public datasets, each exhibiting significant class imbal-
ance, which is addressed through SMOTE, SMOTEEN, and SMOTETomek resampling
techniques. Rigorousexperimentation,including10-foldcross-validation,demonstrates
thatChurnNetoutperformsstate-of-the-artmodels,achievingaccuracyscoresof95.59%,
96.94%,and97.52%acrossthethreedatasets. ThesefindingsemphasizethepotentialofDL
architectureswithattentionmechanismsinadvancingchurnpredictionmodels,making
themmoreeffectiveandinterpretablefortelecomserviceproviders.
These studies highlight the versatility and strength of CNN-based approaches in
churnprediction. Byaddressingchallengessuchasfeatureextraction,informationloss,
andclassimbalance,CNNsandtheirhybridvariantsproviderobustframeworksthatcan
beadaptedtovariousapplications—fromcustomerretentionintelecomtoemployeechurn
inretail—underscoringtheircriticalroleinmodernpredictiveanalytics.
7.5. FeedforwardDeepNeuralNetworkApproaches
Feedforwarddeepneuralnetworkapproachesremainwidelyusedinchurnprediction
becausetheycanlearncomplexnonlinearrelationshipsdirectlyfromdatawhilemaintain-
ingrelativelystraightforwardarchitectures. Thesemethods,includingExtremeLearning
Machines,Multi-LayerPerceptrons,andDeepNeuralNetworks,balancepredictiveperfor-

Mach.Learn.Knowl.Extr.2025,7,105 28of38
manceandcomputationalefficiency. Thissectionreviewskeystudiesthathaveleveraged
thesearchitecturestoachieverobustchurnpredictionoutcomes.
Małgorzataetal.[73]evaluateMulti-LayerPerceptronandRadialBasisFunction(RBF)
networksforchurnpredictioninmobiletelecommunications. Theirfindingssuggestthat
MLPsachievenear-perfectaccuracy(0.999),significantlyoutperformingtraditionalfuzzy
rule-basedandrough-setsystems. However,thestudyalsoacknowledgestheblack-box
natureofneuralnetworks,emphasizingtheneedforexplainabilityinDLmodelstosupport
real-worldadoption. Theseinsightshighlightthetrade-offbetweenmodelperformance
andinterpretability,anongoingchallengeindeployingDLsolutionsforchurnprediction.
Setyo[72]investigateschurnpredictioninthetelecommunicationssectorusingDeep
NeuralNetworks,comparingtheirperformanceagainstRFandXGBoost. Recognizingthe
criticalimpactofcustomerattritiononbusinessretention,thestudyincorporatesfeature
selection techniques and evaluates model efficiency using Google Colaboratory with a
TensorFlowbackend. TheresultsindicatethatDNNachieves80.62%accuracyinjust68s,
outperformingXGBoost(76.45%accuracy,175s)andRF(77.87%accuracy,529s). These
findingshighlightDNN’sabilitytobalanceaccuracyandcomputationalefficiency,making
itapromisingalternativeforreal-timechurnpredictionintelecommunications.
These studies underscore the potential of feedforward and standard deep neural
network approaches to provide robust and efficient churn prediction solutions. At the
sametime,theyhighlighttheongoingneedtoimprovemodelinterpretabilitytoenhance
adoptionandusabilityinpracticalbusinessapplications.
7.6. NLP–BasedDLApproaches
NLP-baseddeeplearningapproachesrepresentaninnovativefrontierinchurnpredic-
tionbyleveragingunstructuredtextualdatatocomplementtraditionalnumericalinputs.
These methods harness advanced language models and RNNs to extract meaningful
insights from customer communications, enriching predictive analytics and enhancing
retentionstrategies. Thissectionhighlightsakeystudythatexemplifiesthepotentialof
NLP-drivenchurnprediction.
Ozan[74]offersauniqueperspectivebyapplyingNLPtechniquestoCRMdatafor
churnprediction.UtilizingwordembeddingsalongsideRNNs,thestudydemonstratesthat
textdata—suchascustomerfeedbackandserviceinteractions—canbeeffectivelyharnessed
topredictchurn. Thisapproachcomplementstraditionalstructureddatamethodsand
providesdeeperinsightsintocustomersentimentandbehaviour. Thefindingssuggestthat
NLP-drivenchurnpredictionmodelscouldbeparticularlybeneficialinindustrieswhere
customercommunicationiscriticalinshapingretentionstrategies.
7.7. RepresentationandFeatureInteractionApproaches
Representationandfeatureinteractionapproacheshaveemergedaspromisingstrate-
giestoenhancechurnpredictionbycapturingcomplexrelationshipswithincustomerdata.
These methods address limitations in traditional deep neural networks, particularly in
handlinghigh-orderfeatureinteractionsandcategoricalvariables. Thissectionreviews
keystudiesthatleverageadvancedembeddingtechniquestoimprovepredictiveaccuracy
andinterpretabilityinchurnmodeling.
Tangetal.[75]introduceaFeatureInteractionNetwork(FIN)designedtoovercome
challengesstandarddeepneuralnetwork-basedchurnmodelsface. Traditionalmodels
oftenstruggletocapturehigh-orderfeatureinteractionsandeffectivelyhandleone-hot
encodedcategoricalfeatures. FINintegratestwokeycomponentstoaddressthis: anentity
embedding network to capture meaningful feature representations and a factorization
machine network with sliding windows to enhance feature interactions. Experimental

Mach.Learn.Knowl.Extr.2025,7,105 29of38
evaluations on four public datasets demonstrate that FIN outperforms state-of-the-art
models by effectively capturing complex dependencies in customer data. This study
underscorestheimportanceoffeatureinteractionmodelinginchurnprediction,offeringa
robustframeworkforleveragingstructuredcustomerdatainpredictiveanalytics.
Inacomplementaryapproach,Cenggoroetal.[76]developaDL-basedvectorembed-
dingmodeltailoredforchurnpredictioninthetelecommunicationsindustry. Thismodel
not onlyemphasizes predictive accuracybut alsoenhances interpretability. Themodel
enablesprecisedifferentiationbetweenloyalandchurn-pronecustomersbyleveraging
vector embeddings to represent customer behaviour in a discriminative feature space.
ExperimentalresultsindicatethatthemodelachievesanF1scoreof81.16%,demonstrat-
ing strong predictive performance. Additionally, cluster similarity analysis and t-SNE
visualizationsconfirmthatthelearnedrepresentationsarehighlyseparable,reinforcing
themodel’seffectiveness. Thisstudyhighlightsthepotentialofvectorembeddingsasa
powerfultoolforchurnmodeling,equippingtelecomproviderswithactionableinsights
forcustomerre-engagementandretention.
Thesestudiesillustratehowembeddingandfeatureinteractiontechniquescansignifi-
cantlyimprovechurnpredictionbycapturingnuancedrelationshipswithincustomerdata.
By enhancing both predictive performance and interpretability, these approaches offer
valuabletoolsfordevelopingproactiveandtargetedretentionstrategiesincompetitive
industries. DeeplearningarchitecturessuchasCNNs,RNNs,andattention-basedmodels
excelatcapturingtemporaldynamicsandcomplexfeatureinteractions,oftenachieving
superior predictive accuracy. Their main drawbacks are higher computational cost, re-
lianceonlargedatasets,andreducedinterpretability,whichcanlimitadoptioninbusiness
contextsrequiringtransparency.
In summary, machine learning and deep learning offer complementary strengths
forchurnprediction. MLtechniquesaregenerallyeasiertointerpret,fastertotrain,and
lessresource-intensive, makingthemsuitableforbusinesssettingswheretransparency
and efficiency are critical. In contrast, DL models are well-suited to high-dimensional,
sequential,andunstructureddata,wheretheirabilitytolearncomplexpatternscanleadto
superiorpredictiveaccuracy. Therefore,thechoicebetweenMLandDLdependsnotonly
ondatacharacteristicsbutalsoonpracticalrequirementssuchasinterpretability,scalability,
andcomputationalresources.
Theincludedstudies(n=61)weresynthesizednarrativelytohighlightmethodological
trends,datasetusage,andreportedperformancemetrics(seeTables1and2). Noformal
riskofbiasassessment,reportingbiasassessment,orcertaintyofevidenceassessment(e.g.,
usingGRADE)wasconducted,asthereviewfocusedonmethodologicalanalysisrather
thanquantitativesynthesis. Duetosubstantialheterogeneityinstudydesigns,datasets,
andevaluationprotocols,meta-analysiswasnotfeasible. Consequently,noinvestigations
ofheterogeneity,subgroupanalyses,sensitivityanalyses,orcertaintyassessmentswere
performed,andnoresultswerepresentedfortheseitems.
8. Discussion
8.1. LinkingFindingstoResearchQuestions
ToprovideadirectresponsetotheresearchquestionsoutlinedintheIntroduction,we
summariseourfindingsbelowabouteachquestion:
RQ1: What are the predominant ML and DL approaches used in customer churn
prediction, and how have these methodologies evolved over time? Our synthesis
(Sections6and7,Tables1and2)showsthatensemble-basedMLtechniques—particularly
boostingmethodssuchasXGBoost,LightGBM,andCatBoost—remainthemostwidely
adoptedacrossindustries,withdecisiontreesandrandomforestsalsofrequentlyusedas

Mach.Learn.Knowl.Extr.2025,7,105 30of38
interpretablebaselines. LSTMs,CNNs,andattention-basedarchitectureshavebeenwidely
adoptedintheDLdomain,particularlyforsequentialandunstructureddatasets. While
hybridapproachesexist,mostcombinealgorithmswithinthesameparadigm(ML–MLor
DL–DL)ratherthanintegratingMLwithDL.From2020to2024,therehasbeenanapparent
increaseintheadoptionofexplainableAItechniques,adaptivelearningstrategies,and
profit-driven evaluation metrics, reflecting a gradual shift toward models that balance
predictiveperformancewithinterpretabilityandbusinessrelevance.
RQ2: Howdodifferentpredictivemodelscompareintermsofaccuracy,adaptability,
andinterpretabilityacrossindustries? Duetotheheterogeneityofdatasets,churndefini-
tions,featuresets,andevaluationprotocols,directcross-studyperformancerankingisnot
feasible. Nonetheless,specifictrendsareevident. Boosting-basedMLmodelsconsistently
achievestrongpredictiveperformanceonstructureddatasetsbutmaybelesseffectiveat
modellingtemporaldependenciesthansequentialDLarchitectures. LSTMsandCNNsex-
celatcapturingbehaviouralandtemporalpatternsbutoftenrequiregreatercomputational
resources and exhibit reduced interpretability. Efforts to improve adaptability include
applyingonlinelearning,reinforcementlearning,andtransferlearning,althoughthese
remainlimitedinreal-worlddeployments. Regardinginterpretability,traditionalMLmeth-
odsofferinherenttransparency,whileDLmethodsbenefitfrompost-hocexplainability
toolssuchasSHAP,LIME,andattentionmechanisms.
RQ3: Whatarethesignificantchallengesandlimitationsinexistingchurnprediction
research,andwhatfuturedirectionscouldaddressthem? Ourreviewidentifieskeychal-
lenges, including class imbalance, reliance on static datasets, limited interpretability in
complexmodels,underutilisationofprofit-orientedmetrics,andalackofcross-domain
generalisability. Thesechallengesarecompoundedbydeploymentbarrierssuchasscala-
bilityandintegrationwithexistingCRMsystems. AsdiscussedinSection8.4,potential
solutionsincludeadvancedresamplingandcost-sensitivelearningtomitigateimbalance,
hybridmodelsthatcombineaccuracywithtransparency,adaptivedrift-awarelearning
methods,andembeddingbusiness-centricevaluationmetricsdirectlyintooptimisation
processes. Futureresearchshouldfocusondevelopingscalable,adaptive,andinterpretable
churnpredictionframeworksvalidatedonstandardisedbenchmarkdatasetstoensureboth
scientificrigourandreal-worldimpact.
8.2. ChallengesandLimitations
DespitesignificantadvancementsinMLandDLforchurnprediction,severalchal-
lengeshinderreal-worldimplementation. Oneofthemostpersistentissuesisclassim-
balance, where the number of churners in datasets is significantly smaller than that of
non-churners. This imbalance often biases models toward the majority class, reducing
theireffectivenessinidentifyingat-riskcustomers. Whileresamplingtechniquesandcost-
sensitivelearninghavebeenproposedassolutions,theycanleadtooverfittingorincreased
computationalcosts.
Anothermajorchallengeliesinfeatureengineeringanddatarepresentation. Many
modelsrelyonstructuredtransactionaldata, yetcustomerinteractionsinvolvediverse
data sources such as call logs, social media activity, and customer support interactions.
Integratingandextractingmeaningfulfeaturesfromsuchheterogeneousdataremainsa
complextask. DLmodelscanautomatefeatureextraction,butoftenrequireextensivedata
preprocessingandsignificantcomputationalresources.
Modelinterpretabilityisanothercriticalconcern,especiallywithDLmodels. While
traditionalMLtechniquessuchasDTsandlogisticregressionprovidehuman-readable
decisionrules,neuralnetworksandensemblemodelsfunctionasblackboxes,makingit
difficultforbusinessestotrusttheirpredictions. ExplainableAItechniques,suchasSHAP

Mach.Learn.Knowl.Extr.2025,7,105 31of38
andattentionmechanisms,havebeenintroducedtoaddressthisissue,buttheyarenotyet
widelyadoptedinreal-worldchurnpredictionsystems.
Furthermore, customerbehaviourisdynamic, andmanychurnpredictionmodels
struggletoadapttoevolvingpatternsovertime. Conceptdrift—wherecustomerprefer-
ences,engagementlevels,andchurnriskschange—challengesmodelstrainedonhistorical
data. Adaptivelearningtechniques,suchasonlinelearningandreinforcementlearning,
offerpotentialsolutionsbutrequirecontinuousretraining,makingthemresourceintensive.
Finally,thereisadisconnectbetweenacademicevaluationmetricsandbusinessimpact.
Many studies assess model performance using accuracy, F1-score, and AUC-ROC, but
thesedonotnecessarilytranslatetoactionablebusinessdecisions. Profit-drivenevaluation
metrics,whichfactorinthecostofretentioneffortsversuslostrevenuefromchurners,are
stillunderexploredinresearch. Bridgingthisgapisessentialfordevelopingmodelsthat
providetangiblebusinessvalue.
Addressingthesechallengeswillrequirefurtheradvancementsinadaptivemodeling,
explainabilitytechniques,andprofit-awarechurnprediction. Asbusinessescontinuetoin-
vestindata-drivenretentionstrategies,futureresearchshouldfocusondevelopingscalable,
interpretable,andbusiness-alignedsolutionstoimprovechurnpredictionoutcomes.
Beyond the methodological challenges discussed above, this review and the body
ofevidencesynthesizedhaveadditionallimitationsworthnoting. Thebodyofevidence
synthesizedinthisreviewmaybesubjecttoseverallimitations. First,theincludedstud-
iesexhibitedsubstantialheterogeneityindatasets,modelingobjectives,andevaluation
metrics,complicatingdirectcomparisonsacrossstudies. Second,manystudiesreliedon
proprietarydatasetswithlimitedtransparency,potentiallyrestrictingthegeneralizability
oftheirfindings. Third,publicationandreportingbiasesmaybepresent,asstudieswith
positiveresultsaremorelikelytobepublishedinpeer-reviewedoutlets. Finally,thelackof
standardizedevaluationprotocolsacrossstudieshinderstheestablishmentofconsistent
benchmarksforchurnpredictionperformance.
Moreover,thisreviewalsohasinherentlimitationsinitsprocesses. Thesearchstrategy
waslimitedtoEnglish-languagepeer-reviewedstudies,whichmayhaveexcludedrelevant
researchpublishedinotherlanguagesorgreyliterature. Althoughthereviewadheredto
PRISMAguidelinesandinvolvedtworeviewerscollaborativelyscreeningandextracting
data,noformalriskofbiasorcertaintyassessments(e.g.,ROBIS,GRADE)wereperformed,
astheprimaryfocuswasonmethodologicaltrendsratherthanquantitativeeffectestimates.
Additionally, using a narrative synthesis, while appropriate given the heterogeneity of
studies,maybelessrobustthanmeta-analyticapproachesforaggregatingevidence.
8.3. IdentifiedGapsinReviewedResearch
DespitetheextensiveadvancementsinMLandDLforcustomerchurnprediction,
severalgapspersistinthereviewedresearch,highlightingareasthatrequirefurtherexplo-
ration. Oneofthemostnotablegapsisthelimitedemphasisonreal-worlddeployment
challenges. Whilemanystudiesfocusonimprovingmodelaccuracyandrobustness,fewer
address the practical aspects of implementing these models in business environments.
Issuessuchasscalability,computationalefficiency,andintegrationwithexistingCRMsys-
temsremainunderexplored. Researchintolightweight,efficient,andreal-timedeployable
solutionsisessentialsincemanyorganizationslackthecomputationalinfrastructureto
supportcomplexDLmodels.
Anothersignificantgapisthelackoffocusonmodelinterpretabilityandexplainability.
WhileDLapproaches,particularlyRNNs,CNNs,andtransformers,haveshownimproved
predictiveperformance,theirblack-boxnaturelimitstheiradoptioninbusinesssettings
wheretransparencyiscrucial. AlthoughtechniqueslikeSHAPandLocalInterpretable

Mach.Learn.Knowl.Extr.2025,7,105 32of38
Model-AgnosticExplanations(LIME)havebeenintroduced,theyarenotwidelyintegrated
intochurnpredictionmodels. Futureresearchshouldprioritisethedevelopmentofinher-
entlyinterpretablemodelsorhybridapproachesthatbalanceaccuracywithtransparency
tofacilitatebetterdecision-makingincustomerretentionstrategies.
Additionally,mostexistingstudiesrelyonstaticdatasets,whichfailtoaccountfor
thedynamicnatureofcustomerbehaviour. Conceptdrift—wherecustomerengagement
patterns and churn drivers change over time—poses a significant challenge for model
generalization. Whilesomestudiesexploreadaptive, reinforcement, oronlinelearning
techniques, their practical adoption remains limited. Future research should focus on
developingadaptiveandself-learningmodelsthatcontinuouslyupdatebasedonevolving
customerdata,ensuringsustainedpredictiveperformanceovertime.
Anothergapisthelackofcross-domaingeneralizationinchurnpredictionmodels.
Manystudiesdevelopmodelstailoredtospecificindustries,suchastelecommunications
orbanking,butdonottesttheirapplicabilityacrossdifferentsectors. Giventhatcustomer
behaviour varies significantly across domains, future research should explore domain
adaptationtechniquesandtransferlearningtoimprovemodelgeneralizability. Thiswould
enablebusinessesindifferentsectorstoleveragechurnpredictionmethodologieswithout
extensiveretraining.
Afurthergapinthereviewedliteratureconcernsfairness,ethics,andbiasmitigation,
which remain largely absent from churn prediction research. Although fairness-aware
algorithms,biasauditing,andresponsibleAIframeworksareincreasinglydiscussedinthe
broadermachinelearningfield,veryfewstudiesapplytheseconsiderationstocustomer
churn. Thisomissionissignificantbecausebiasedmodelsmayunintentionallydisadvan-
tage certain customer groups, leading to unequal treatment in retention strategies and
exposingbusinessestoreputationalorregulatoryrisks. Futureresearchshouldtherefore
emphasize fairness-aware model design, transparent reporting of potential biases, and
theintegrationofbiasmitigationstrategies. Addressingtheseissueswouldensurethat
churnpredictionmodelsareaccurate,profitable,equitable,trustworthy,andalignedwith
emergingstandardsforresponsibleAI.
Finally,profit-drivenevaluationmetricsremainunderutilizedinthereviewedliter-
ature. While traditional metrics such as accuracy, F1-score, and AUC-ROC are widely
reported,theydonotfullycapturethebusinessimplicationsofchurnprediction. Fewstud-
iesincorporateprofit-basedmetricslikeExpectedMaximumProfitforCustomerChurn,
which consider the financial impact of retention strategies. Further research is needed
todevelopmodelsthatalignmorecloselywithbusinessgoals,optimizingforpredictive
performance,cost-effectiveness,andrevenuemaximization.
Addressing these gaps will require a multi-faceted research approach, integrating
interpretability,adaptivelearning,cross-domainvalidation,andbusiness-centricevaluation
intofuturechurnpredictionmodels. Bybridgingthesegaps,thefieldcanadvancetoward
more practical, transparent, and financially viable solutions for churn management in
real-worldapplications.
8.4. TrendDirections
Analyzingpublicationtrendsinchurnpredictionresearchover2020–2024revealsa
clearshifttowardmoreadvancedMLandDLtechniques. IEEEhasconsistentlyledinpub-
licationvolume,indicatingastrongresearchfocuswithinengineeringandcomputational
disciplines. WhiletraditionalMLtechniquessuchasDTsandlogisticregressionremain
widelyused,boostingmethodsandensemblelearninghavesteadilygrown,reflectingan
industrypreferenceforrobustandinterpretablemodels.

Mach.Learn.Knowl.Extr.2025,7,105 33of38
Inrecentyears,DLapproaches,particularlyRNNs,CNNs,andtransformers,have
gainedtraction,especiallyindomainsdealingwithcomplexsequentialandunstructured
data, such as telecommunications and banking. Adopting hybrid ML-DL models also
suggestsanincreasinginterestincombiningthestrengthsofmultipleparadigmstoimprove
predictiveaccuracy.
Another notable trend is the growing importance of explainability and business-
alignedevaluationmetrics. Whileearlystudiesprioritisedaccuracy-basedbenchmarks,
more recent research integrates profit-driven evaluation methods, addressing the gap
betweenacademicperformancemetricsandreal-worldapplicability.
Thefieldwilllikelyseefurtheradvancementsinadaptivelearningtechniques,rein-
forcementlearningforchurnmanagement,andintegrationofmulti-modaldatasources.
ThecontinuedevolutionofMLandDLforchurnpredictionindicatesashifttowardmodels
thataremoreaccurate,transparent,cost-effective,anddynamicallyadaptabletochanging
consumerbehaviours.
8.5. PotentialSolutiontotheCurrentChallenges
Our review identifies several persistent challenges in customer churn prediction,
eachofwhichhasbeenaddressedintheliteraturethroughvarioustechnicalapproaches.
One of the most prevalent is class imbalance, where the proportion of churners is far
smallerthanthatofnon-churners. Beyondconventionaloversamplingandundersampling
techniques, more advanced strategies such as Synthetic Minority Oversampling with
EditedNearestNeighbors(SMOTE-ENN)andAdaptiveSyntheticSampling(ADASYN)
have demonstrated improved representation of the minority class. Some studies have
combinedtheseresamplingmethodswithensemblelearning,whileothershaveadopted
cost-sensitivelearningframeworksthatincorporatemisclassificationcostsdirectlyintothe
model’soptimisationprocess. Thesecost-sensitiveapproachesensurethatmodeltraining
reflectstherealfinancialimplicationsofpredictionerrors,whichisparticularlyimportant
inretention-focusedapplications.
Modelinterpretabilityisanothermajorchallenge,especiallyasdeeplearningarchitec-
turesbecomeincreasinglycomplex. Severalstudieshaveappliedposthocexplainability
techniques such as Shapley Additive Explanations (SHAP), Local Interpretable Model-
agnosticExplanations(LIME),andcounterfactualexplanationmethodstoprovideaclearer
understandingofmodelbehaviour. Othershaveexploredinherentlyinterpretablealter-
natives, including sparse linear models and rule-based ensemble methods, which may
bettersuitdomainswheretransparencyiscriticalforregulatorycomplianceorbuilding
stakeholdertrust. Arecurringtrade-offinchurnpredictionresearchisthechoicebetween
interpretableMLmodelsandmorecomplexDLarchitectures. Interpretablemethodssuch
asdecisiontrees,logisticregression,andrule-basedensemblesremainhighlysuitablein
businesscontextswheretransparency,regulatorycompliance,andeaseofcommunication
withnon-technicalstakeholdersarecritical. Thesemodelsallowdecision-makerstotrace
predictionsbacktocustomerattributesanddesigntargetedretentionstrategies.Bycontrast,
DLmodels—includingLSTMs, CNNs, andTransformer-basedarchitectures—aremore
effectiveforhigh-dimensional,unstructured,orsequentialdata,wherepredictiveaccuracy
andcapturingcomplexbehaviouralpatternsoutweightheneedforinterpretability. Guid-
anceforpractitionersthereforedependsoncontext: interpretableMLispreferablewhen
accountabilityandactionableinsightsareparamount,whereasDLapproaches—including
LSTMs,CNNs,andTransformer-basedarchitectures—aremoreappropriatewhentherich-
nessandcomplexityofthedatademandadvancedrepresentationlearningandpredictive
accuracy.

Mach.Learn.Knowl.Extr.2025,7,105 34of38
The problem of concept drift, where customer behaviours and market conditions
evolveovertime,hasalsoreceivedgrowingattention. TheOptimisedTwo-SidedCumu-
lativeSumChurnDetector(OTCCD)integratesdriftdetectionwithadaptivelearningto
update models as data distributions change. Transfer learning and domain adaptation
techniqueshavelikewisebeenproposedtoenablemodelstoreuseknowledgefromearlier
datawhileadaptingtonewpatternswithminimalretraining. Thesestrategiesareparticu-
larlyrelevantinindustrieswherechurndeterminantsshiftrapidlyduetotechnologicalor
competitivechanges.
Finally,thelimitedadoptionofprofit-orientedevaluationmetricsremainsamissed
opportunityforaligningmodelperformancewithbusinessobjectives. Metricssuchasthe
ExpectedMaximumProfitforCustomerChurn(EMPC)andothercost–benefitframeworks
allowforadirectassessmentoftheeconomicimpactofretentionstrategies. Severalstudies
have shown that embedding these metrics into the optimisation process can produce
predictive and financially effective models rather than using them solely for post hoc
evaluation.
Thesesolutionsshowthatthechallengesinchurnpredictionarenotinsurmountable.
Manymethodologicaltoolsexisttoaddressimbalance,improveinterpretability,adaptto
shiftingdatadistributions,andincorporatebusinessvalueintoevaluation. Bydrawing
attentiontotheseapproaches,ourreviewaimstoencouragefutureworkthatadvancesthe
technicalstateoftheartandensuresthatchurnpredictionmodelsdeliveractionableand
economicallymeaningfuloutcomes.
9. ConclusionsandFutureResearchDirections
Customerchurnpredictionhasundergonerapidmethodologicalevolutioninrecent
years, with machine learning and deep learning techniques now central to identifying
at-riskcustomersandguidingretentionstrategies. Inthissystematicreview,weexamined
240peer-reviewedstudiespublishedbetweenJanuary2020andDecember2024,applyinga
PRISMA-guided,two-phasemethodology.Thefirstphaseprovidedabibliometricmapping
ofthefield, whiletheseconddeliveredadetailedsynthesisof61studiesmeetingstrict
novelty and contribution criteria. This dual approach enabled us to capture both the
breadthanddepthofrecentadvancesinchurnpredictionresearch.
Our findings reveal a strong preference for ensemble learning and advanced ML
techniquessuchasgradientboosting(XGBoost,LightGBM,CatBoost),decisiontrees,and
randomforests,alongsideagrowingadoptionofDLarchitectures,particularlyLSTMs,
CNNs,andattention-basedmodels. Thesemethodsareincreasinglyappliedtocapturecus-
tomerdata’stemporaldynamicsandbehaviouralpatterns. Hybridmodellingapproaches
arealsoexplored,thoughmostcombinedifferentalgorithmswithinthesameparadigm
(ML–MLorDL–DL)ratherthanintegratingMLwithDL.WhileDLmodelsoftenachieve
superiorpredictivepower,thiscomesattheexpenseofhighercomputationaldemandsand
reducedinterpretability;conversely,traditionalMLmodelstendtobemoreinterpretable
andcomputationallyefficientbutmayunderperformwithhigh-dimensionalorcomplex
datasets. Efforts to bridge this gap through explainable AI tools such as SHAP, LIME,
and attention mechanisms are promising but remain underrepresented in operational
deployments.
Severalpersistentchallengesemergedfromouranalysis. Classimbalancecontinues
tobiasmodelperformancetowardmajorityclasses,andmanymodelsaretrainedonstatic
datasets that do not reflect evolving customer behaviours, making them susceptible to
concept drift. Adaptive learning strategies and real-time model updating are still rare
in practice. Moreover, accuracy-oriented metrics dominate evaluation, with relatively
fewstudiesintegratingprofit-drivenmetricssuchastheEMPC,despitetheircloseralign-

Mach.Learn.Knowl.Extr.2025,7,105 35of38
mentwithbusinessobjectives. Inaddition,fairness,ethics,andbiasmitigationrepresent
importantbutunderexploredprioritiesinchurnpredictionresearch.Incorporatingfairness-
awaremodellingandtransparentreportingpracticeswillbeessentialtoensurethatfuture
solutionsarenotonlytechnicallyrobustandbusiness-alignedbutalsosociallyresponsible.
Addressingthesegapspresentscleardirectionsforfutureresearch. Thereisaneed
for adaptive churn prediction frameworks that can dynamically update to account for
behavioural and market changes, ideally incorporating automated drift detection and
incremental learning. Integrating inherently interpretable models and robust post hoc
explainabilitytechniquesshouldbeprioritisedtoimprovetransparencyandusertrust,
especiallyinregulatedindustries. Researchersshouldalsoexploremulti-modalapproaches
thatcombinestructured,unstructured,andnetwork-baseddatatocapturericherrepre-
sentationsofcustomerbehaviour. Finally,adoptingstandardisedbenchmarkdatasetsand
incorporatingbusiness-alignedperformancemetricsduringtrainingandevaluationwould
enablefairercomparisonsacrossstudiesandensurethatpredictivemodelsdelivertangible
valueinreal-worldretentionstrategies.
Bycombiningbibliometricinsightswithastructuredmethodologicalsynthesis,this
reviewprovidesacomprehensive,up-to-datemapofchurnpredictionresearch. Itoffers
concrete guidance for developing the next generation of adaptive, interpretable, and
business-alignedmodelsthatcanbedeployedeffectivelyinreal-worldcontexts.
AuthorContributions:M.I.:Conceptualization;Investigation;Methodology;Projectadministration;
Resources; Software; Validation; Visualization; Writing—originaldraft. M.J.: Conceptualization;
Investigation; Methodology;Resources; Validation. A.B.: Methodology; Supervision; Validation;
Writing—review&editing.H.R.A.:Supervision;Writing—review&editing.Allauthorshaveread
andagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenocompetinginterests.
References
1. Ahn,J.;Hana,S.-P.;Lee,Y.-S.Customerchurnanalysis:Churndeterminantsandmediationeffectsofpartialdefectioninthe
Koreanmobiletelecommunicationsserviceindustry.Telecommun.Policy2006,30,552–568.[CrossRef]
2. Xiaoling,S.;Ye,Y.KnowledgeDiscovery:Methodsfromdataminingandmachinelearning.Soc.Sci.Res.2023,110,102817.
3. Imani,M.;Arabnia,H.R.Hyperparameteroptimizationandcombineddatasamplingtechniquesinmachinelearningforcustomer
churnprediction:Acomparativeanalysis.Technologies2023,11,167.[CrossRef]
4. Imani,M.; Ghaderpour,Z.; Joudaki,M.; Beikmohammadi,A.TheImpactofSMOTEandADASYNonRandomForestand
AdvancedGradientBoostingTechniquesinTelecomCustomerChurnPrediction.InProceedingsofthe202410thInternational
ConferenceonWebResearch(ICWR),Tehran,Iran,24–25April2024.
5. Imani,M.;Beikmohammadi,A.;Arabnia,H.R.ComprehensiveAnalysisofRandomForestandXGBoostPerformancewith
SMOTE,ADASYN,andGNUSUnderVaryingImbalanceLevels.Technologies2025,13,88.[CrossRef]
6. Lemmens,A.;Gupta,S.Managingchurntomaximizeprofits.Mark.Sci.2020,39,956–973.[CrossRef]
7. Joudaki,M.;Imani,M.;Esmaeili,M.;Mahmoodi,M.;Mazhari,N.PresentingaNewApproachforPredictingandPreventing
Active/DeliberateCustomerChurninTelecommunicationIndustry.InProceedingsoftheInternationalConferenceonSecurity
andManagement(SAM).TheSteeringCommitteeoftheWorldCongressinComputerScience,ComputerEngineeringand
AppliedComputing(WorldComp),LasVegas,NV,USA,18–21July2011.
8. Kamil,M.;Kopczewska,K.Customerchurninretaile-commercebusiness:Spatialandmachinelearningapproach.J.Theor.Appl.
Electron.Commer.Res.2022,17,165–198.[CrossRef]
9. Al-Najjar,D.;Al-Rousan,N.;Al-Najjar,H.Machinelearningtodevelopcreditcardcustomerchurnprediction. J.Theor. Appl.
Electron.Commer.Res.2022,17,1529–1542.[CrossRef]
10. Christou,V.;Tsoulos,I.;Loupas,V.;Tzallas,A.T.;Gogos,C.;Karvelis,P.S.;Antoniadis,N.;Glavas,E.;Giannakeas,N.Performance
andearlydroppredictionforhighereducationstudentsusingmachinelearning.ExpertSyst.Appl.2023,225,120079.[CrossRef]

Mach.Learn.Knowl.Extr.2025,7,105 36of38
11. Ajegbile,M.D.;Olaboye,J.A.;Maha,C.C.;Igwama,G.T.;Abdul,S.Theroleofdata-driveninitiativesinenhancinghealthcare
deliveryandpatientretention.WorldJ.Biol.Pharm.HealthSci.2024,19,234–242.[CrossRef]
12. Ahn,J.;Hwang,J.;Kim,D.;Choi,H.;Kang,S.Asurveyonchurnanalysisinvariousbusinessdomains. IEEEAccess2020,8,
220816–220839.[CrossRef]
13. Reichheld,F.F.;Teal,T.LoyaltyEffect:TheHiddenForceBehindGrowth,Profits,andLasting;HarvardBusinessSchoolPublications:
Brighton,MA,USA,1996;pp.352–354.
14. Geiler,L.;Affeldt,S.;Nadif,M.Asurveyonmachinelearningmethodsforchurnprediction. Int. J.DataSci. Anal. 2022,14,
217–242.[CrossRef]
15. Edvaldo,D.;Ojeme,B.;Daramola,O.Experimentalanalysisofhyperparametersfordeeplearning-basedchurnpredictioninthe
bankingsector.Computation2021,9,34.[CrossRef]
16. Höppner,S.;Stripling,E.;Baesens,B.;vandenBroucke,S.;Verdonck,T.Profitdrivendecisiontreesforchurnprediction.Eur.J.
Oper.Res.2020,284,920–933.[CrossRef]
17. Maldonado,S.;López,J.;Vairetti,C.Profit-basedchurnpredictionbasedonminimaxprobabilitymachines. Eur. J.Oper. Res.
2020,284,273–284.[CrossRef]
18. Janssens,B.;Bogaert,M.;Bagué,A.;VandenPoel,D.B2Boost:Instance-dependentprofit-drivenmodellingofB2Bchurn.Ann.
Oper.Res.2024,341,267–293.[CrossRef]
19. Wang,X.;Nguyen,K.;Nguyen,B.P.Churnpredictionusingensemblelearning.InProceedingsofthe4thInternationalConference
onMachineLearningandSoftComputing,HaiphongCity,Vietnam,17–19January2020;AssociationforComputingMachinery:
NewYork,NY,USA,2020.
20. Hemlata,J.;Khunteta,A.;Srivastava,S.Churnpredictionintelecommunicationusinglogisticregressionandlogitboost.Procedia
Comput.Sci.2020,167,101–112.[CrossRef]
21. Maretta,S.N.T.;Permai,S.D.Enhancedchurnpredictionmodelwithboostedtreesalgorithmsinthebankingsector.InProceedings
ofthe2021InternationalConferenceonDataScienceandItsApplications(ICoDSA),Online,6–7October2021.
22. Tianpei,X.;Ma,Y.;Kim,K.Telecomchurnpredictionsystembasedonensemblelearningusingfeaturegrouping.Appl.Sci.2021,
11,4742.[CrossRef]
23. Manohar,E.;Jenifer,P.;Nisha,M.S.;Benita,B.Acollectivedataminingapproachtopredictcustomerbehaviour.InProceedings
ofthe2021ThirdInternationalConferenceonIntelligentCommunicationTechnologiesandVirtualMobileNetworks(ICICV),
Tirunelveli,India,4–6February2021.
24. Ramesh,P.;Emilyn,J.J.;Vijayakumar,V.Hybridartificialneuralnetworksusingcustomerchurnprediction.Wirel.Pers.Commun.
2022,142,1695–1709.[CrossRef]
25. Usman-Hamza,F.E.;Balogun,A.O.;Capretz,L.F.;Mojeed,H.A.;Mahamad,S.;Salihu,S.A.;Akintola,A.G.;Basri,S.;Amosa,R.T.;
Salahdeen,N.K.Intelligentdecisionforestmodelsforcustomerchurnprediction.Appl.Sci.2022,12,8270.[CrossRef]
26. Saias, J.; Rato, L.; Gonçalves, T. An approach to churn prediction for cloud services recommendation and user retention.
Information2022,13,227.[CrossRef]
27. Ishrat,J.;Sanam,T.F.AnImprovedMachineLearningBasedCustomerChurnPredictionforInsightandRecommendationin
E-commerce.InProceedingsofthe202225thInternationalConferenceonComputerandInformationTechnology(ICCIT),Cox’s
Bazar,Bangladesh,17–19December2022.
28. Liu,R.;Ali,S.;Bilal,S.F.;Sakhawat,Z.;Imran,A.;Almuhaimeed,A.;Alzahrani,A.;Sun,G.Anintelligenthybridschemefor
customerchurnpredictionintegratingclusteringandclassificationalgorithms.Appl.Sci.2022,12,9355.[CrossRef]
29. Yogesh,B.;Fokone,R.T.Hybridapproachusingmachinelearningalgorithmsforcustomers’churnpredictioninthetelecommu-
nicationsindustry.Concurr.Comput.Pract.Exp.2022,34,e6627.
30. Fu,K.;Zheng,G.;Xie,W.Customerchurnpredictionforawebcastplatformviaavoting-basedensemblelearningmodelwith
Nelder-Meadoptimizer.J.Intell.Inf.Syst.2023,61,859–879.[CrossRef]
31. Mahayasa, A.I.N.; Wanchai, P. Customer Churn Prediction Using Weight Average Ensemble Machine Learning Model. In
Proceedingsofthe202320thInternationalJointConferenceonComputerScienceandSoftwareEngineering(JCSSE),Phitsanulok,
Thailand,28June–1July2023.
32. Khoh,W.H.;Pang,Y.H.;Ooi,S.Y.;Wang,L.Y.K.;Poh,Q.W.Predictivechurnmodelingforsustainablebusinessinthetelecommu-
nicationindustry:Optimizedweightedensemblemachinelearning.Sustainability2023,15,8631.[CrossRef]
33. Arshad,U.;Khan,G.;KhaledAlarfaj,F.;Halim,Z.;Anwar,S.Q-ensemblelearningforcustomerchurnpredictionwithblockchain-
enableddatatransparency.Ann.Oper.Res.2024.[CrossRef]
34. Venkatesh, S.; Jeyakarthic, M.Anoptimalgeneticalgorithmwithsupportvectormachineforcloudbasedcustomerchurn
prediction.InProceedingsofthe2020InternationalConferenceonSystem,Computation,AutomationandNetworking(ICSCAN),
Pondicherry,India,3–4July2020.

Mach.Learn.Knowl.Extr.2025,7,105 37of38
35. Saheed,Y.K.;Hambali,M.A.Customerchurnpredictionintelecomsectorwithmachinelearningandinformationgainfilter
featureselectionalgorithms.InProceedingsofthe2021InternationalConferenceonDataAnalyticsforBusinessandIndustry
(ICDABI),Online,25–26October2021.
36. Pustokhina,I.V.;Pustokhin,D.A.;Nguyen,P.T.;Elhoseny,M.;Shankar,K.Multi-objectiverainoptimizationalgorithmwith
WELMmodelforcustomerchurnpredictionintelecommunicationsector.ComplexIntell.Syst.2023,9,3473–3485.[CrossRef]
37. Mirabdolbaghi,S.;Mohammad,S.;Amiri,B.Modeloptimizationanalysisofcustomerchurnpredictionusingmachinelearning
algorithmswithfocusonfeaturereductions.Discret.Dyn.Nat.Soc.2022,2022,5134356.[CrossRef]
38. Al-Shourbaji,I.;Helian,N.;Sun,Y.;Alshathri,S.;AbdElaziz,M.Boostingantcolonyoptimizationwithreptilesearchalgorithm
forchurnprediction.Mathematics2022,10,1031.[CrossRef]
39. AlShourbaji,I.;Helian,N.;Sun,Y.;Hussien,A.G.;Abualigah,L.;Elnaim,B.Anefficientchurnpredictionmodelusinggradient
boostingmachineandmetaheuristicoptimization.Sci.Rep.2023,13,14441.[CrossRef]
40. Kurtcan,D.B.;Ozcan,T.Predictingcustomerchurnusinggreywolfoptimization-basedsupportvectormachinewithprincipal
componentanalysis.J.Forecast.2023,42,1329–1340.[CrossRef]
41. Ponnusamy,R.R.A.;Rana,M.E.;Manickavasagam,S.A.;Hameed,V.A.PSO-SVMbasedalgorithmforcustomerchurnprediction
inthebankingindustry. InProceedingsofthe2023IEEE6thInternationalConferenceonBigDataandArtificialIntelligence
(BDAI),Jiaxing,China,8–9July2023.
42. Koçog˘lu,F.Ö.;Özcan,T.Agridsearchoptimizedextremelearningmachineapproachforcustomerchurnprediction.J.Eng.Res.
2023,11,103–112.[CrossRef]
43. Ahmad,T.A.;Usman,M.Adaptivetelecomchurnpredictionforconcept-sensitiveimbalancedatastreams.J.Supercomput.2022,
78,3746–3774.
44. Adnan,A.;Adnan,A.;Anwar,S.Anadaptivelearningapproachforcustomerchurnpredictioninthetelecommunicationindustry
usingevolutionarycomputationandNaïveBayes.Appl.SoftComput.2023,137,110103.[CrossRef]
45. Lee,N.T.;Lee,H.C.;Hsin,J.;Fang,S.H.Predictionofcustomerbehaviorchangingviaahybridapproach.IEEEOpenJ.Comput.
Soc.2023,5,27–38.[CrossRef]
46. Shimaa,O.;Mahmoud,K.T.;Abdel-Fattah,M.A.Aproposedhybridframeworktoimprovetheaccuracyofcustomerchurn
predictionintelecomindustry.J.BigData2024,11,70.[CrossRef]
47. DeBock,K.W.;DeCaigny,A.Spline-ruleensembleclassifierswithstructuredsparsityregularizationforinterpretablecustomer
churnmodeling.Decis.Support.Syst.2021,150,113523.[CrossRef]
48. Mitravinda,K.M.;Shetty,S.Employeeattrition:Predictionanalysisofcontributoryfactorsandrecommendationsforemployee
retention.InProceedingsofthe2022IEEEInternationalConferenceforWomeninInnovation,Technology&Entrepreneurship
(ICWITE),Bangalore,India,1–3December2022.
49. Wang,X.;Xie,L.;Wang,H.;Xing,X.;Wan,W.;Wu,Z.;Ma,X.;Li,Q.DecipheringExplicitandImplicitFeaturesforReliable,
Interpretable;ActionableUserChurnPredictioninOnlineVideoGames.IEEETrans.Vis.Comput.Graph.2024,31,5990–6007.
[CrossRef]
50. Vo,N.N.;Liu,S.;Li,X.;Xu,G.Leveragingunstructuredcalllogdataforcustomerchurnprediction.Knowl.-BasedSyst.2021,212,
106586.[CrossRef]
51. Soumi,D.;Prabu,P.ARepresentation-BasedQueryStrategytoDeriveQualitativeFeaturesforImprovedChurnPrediction.IEEE
Access2023,11,1213–1223.[CrossRef]
52. Wang,A.X.;Chukova,S.S.;Nguyen,B.P.Data-centricaitoimprovechurnpredictionwithsyntheticdata.InProceedingsofthe
20233rdInternationalConferenceonComputer,ControlandRobotics(ICCCR),Shanghai,China,24–26March2023.
53. Babak,A.;Hosseini,S.H.UnveilingthePowerofSocialInfluence:AMachineLearningFrameworkforChurnPredictionwith
NetworkAnalysis.IEEEAccess2024,12,71271–71285.[CrossRef]
54. Nyashadzashe,T.;Sibanda,K.Realtimecustomerchurnscoringmodelforthetelecommunicationsindustry.InProceedingsof
the20202ndInternationalMultidisciplinaryInformationTechnologyandEngineeringConference(IMITEC),Kimberley,South
Africa,25–27November2020.
55. Tianyuan,Z.;Moro,S.;Ramos,R.F.Adata-drivenapproachtoimprovecustomerchurnpredictionbasedontelecomcustomer
segmentation.FutureInternet2022,14,94.[CrossRef]
56. Šimovic´, P.P.; Chen, C.Y.T.; Sun, E.W.Classifyingthevarietyofcustomers’onlineengagementforchurnpredictionwitha
mixed-penaltylogisticregression.Comput.Econ.2023,61,451–485.[CrossRef]
57. AbdElminaam,D.S.;Maged,M.;Mousa,M.K.;Younis,A.O.;Abdelsalam,M.S.;Hisham,Y.;Talaat,T.EmpTurnoverML:An
EfficientModelforEmployeeTurnoverandCustomerChurnPredictionUsingMachineLearningAlgorithms.InProceedingsof
the2023InternationalMobile,Intelligent;UbiquitousComputingConference(MIUCC),Cairo,Egypt,27–28September2023.
58. Jakob, R.; Lepper, N.; Fleisch, E.; Kowatsch, T. Predicting early user churn in a public digital weight loss intervention. In
ProceedingsoftheCHI’24:Proceedingsofthe2024CHIConferenceonHumanFactorsinComputingSystems,Honolulu,HI,
USA,11–16May2024.

Mach.Learn.Knowl.Extr.2025,7,105 38of38
59. Sikri,A.;Jameel,R.;Idrees,S.M.;Kaur,H.Enhancingcustomerretentionintelecomindustrywithmachinelearningdrivenchurn
prediction.Sci.Rep.2024,14,13097.[CrossRef][PubMed]
60. Roohi, S.; Relas, A.; Takatalo, J.; Heiskanen, H.; Hämäläinen, P. Predicting game difficulty and churn without players. In
ProceedingsoftheCHIPLAY‘20:ProceedingsoftheAnnualSymposiumonComputer-HumanInteractioninPlay,Online,2–4
November2020.
61. Zhu,B.;Qian,C.;Pan,X.;Chen,H.Atrajectory-baseddeepsequentialmethodforcustomerchurnprediction.InProceedingsof
the20205thInternationalConferenceonMachineLearningTechnologies,Beijing,China,19–21June2020.
62. Alboukaey,N.;Joukhadar,A.;Ghneim,N.Dynamicbehaviorbasedchurnpredictioninmobiletelecom.ExpertSyst.Appl.2020,
162,113779.[CrossRef]
63. Joy,U.G.;Hoque,K.E.;Uddin,M.N.;Chowdhury,L.;Park,S.B.Abigdata-drivenhybridmodelforenhancingstreamingservice
customerretentionthroughchurnpredictionintegratedwithexplainableAI.IEEEAccess2024,12,69130–69150.[CrossRef]
64. Beltozar-Clemente,S.;Iparraguirre-Villanueva,O.;Pucuhuayla-Revatta,F.;Zapata-Paulini,J.;Cabanillas-Carbonell,M.Predicting
customerabandonmentinrecurrentneuralnetworksusingshort-termmemory.J.OpenInnov.Technol.Mark.Complex.2024,10,
100237.[CrossRef]
65. Liu,Y.;Shengdong,M.;Jijian,G.;Nedjah,N.Intelligentpredictionofcustomerchurnwithafusedattentionaldeeplearning
model.Mathematics2022,10,4733.[CrossRef]
66. Jajam,N.;Challa,N.P.;Prasanna,K.S.;Deepthi,C.V.S.ArithmeticoptimizationwithensembledeeplearningSBLSTM-RNN-IGSA
modelforcustomerchurnprediction.IEEEAccess2023,11,93111–93128.[CrossRef]
67. Zhao,Y.;Shao,Z.;Zhao,W.;Han,J.;Zheng,Q.;Jing,R.Combiningunsupervisedandsupervisedclassificationforcustomer
valuediscoveryinthetelecomindustry:Adeeplearningapproach.Computing2023,105,1395–1417.[CrossRef]
68. Van-Hieu,V.Predictcustomerchurnusingcombinationdeeplearningnetworksmodel.NeuralComput.Appl.2024,36,4867–4883.
69. Muhammad,U.;Ahmad,W.;Fong,A.Designandimplementationofasystemforcomparativeanalysisoflearningarchitectures
forChurnprediction.IEEECommun.Mag.2021,59,86–90.[CrossRef]
70. Ebru,P.O.;Ozcan,T.Anoveldeeplearningmodelbasedonconvolutionalneuralnetworksforemployeechurnprediction.J.
Forecast.2022,41,539–550.
71. Saha,S.;Saha,C.;Haque,M.M.;Alam,M.G.R.;Talukder,A.Churnnet:Deeplearningenhancedcustomerchurnpredictionin
telecommunicationindustry.IEEEAccess2024,12,4471–4484.[CrossRef]
72. Setyo,A.A.Telecommunicationservicesubscriberchurnlikelihoodpredictionanalysisusingdiversemachinelearningmodel.In
Proceedingsofthe20203rdInternationalConferenceonMechanical,Electronics,Computer;IndustrialTechnology(MECnIT),
Medan,Indonesia,25–27June2020.
73. Małgorzata,P.-K.;Marfo,K.F.;Sulikowski,P.Multi-LayerPerceptronandRadialBasisFunctionNetworksinPredictiveModeling
ofChurnforMobileTelecommunicationsBasedonUsagePatterns.Appl.Sci.2024,14,9226.[CrossRef]
74. Ozan,S¸.Casestudiesonusingnaturallanguageprocessingtechniquesincustomerrelationshipmanagementsoftware.J.Intell.
Inf.Syst.2021,56,233–253.[CrossRef]
75. Tang,Q.;Xia,G.;Zhang,X.;Li,Y.Afeatureinteractionnetworkforcustomerchurnprediction.InProceedingsofthe202012th
InternationalConferenceonMachineLearningandComputing,Shenzhen,China,15–17February2020.
76. Cenggoro,T.W.;Wirastari,R.A.;Rudianto,E.;Mohadi,M.I.;Ratj,D.;Pardamean,B.Deeplearningasavectorembeddingmodel
forcustomerchurn.ProcediaComput.Sci.2021,179,624–631.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.