---
conversion_metadata:
  converted_at: "2026-07-21T08:15:12Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Rad et al.pdf"
  source_pdf_sha256: "37b05525f687800a5c1d4a4e0bbe32937bb5b40263edf604c662b4375b94afb5"
  page_count: 17
  markdown_char_count: 131061
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Article
Modeling Investment Decisions Through Decision Tree
Regression—A Behavioral Finance Theory Approach

Dana Rad 1,*
Raluca Simina Bilt,i 2, Sergiu Rusu 2

, Lavinia Denisia Cuc 2,*

, Gabriel Croitoru 3

, Bogdan Cosmin Gomoi 2

, Luminit,a Mazuru 2,

, Maria Sinaci 2

and Florentina Simona Barbu 2

1 Centre of Research Development and Innovation in Psychology, Faculty of Educational Sciences,

Aurel Vlaicu University of Arad, 310130 Arad, Romania

2 Centre for Economic Research and Consultancy, Faculty of Economics, Aurel Vlaicu University of Arad,

310130 Arad, Romania; bogdan.gomoi@uav.ro (B.C.G.); luminita.mazuru@uav.ro (L.M.);
raluca.bilti@uav.ro (R.S.B.); sergiu.rusu@uav.ro (S.R.); maria.sinaci@uav.ro (M.S.);
florentina.barbu@uav.ro (F.S.B.)
Faculty of Economics, Valahia University of Targoviste, 130004 Targoviste, Romania;
gabriel.croitoru@valahia.ro

3

* Correspondence: dana@xhouse.ro (D.R.); lavinia.cuc@uav.ro (L.D.C.)

Abstract: This study examines the key factors influencing investment decisions through
decision tree regression, grounded in behavioral finance theory. By analyzing a comprehen-
sive dataset incorporating behavioral, demographic, and financial variables—including
investment attitudes, decision-making behaviors, financial education, age, income, and
education—this study identifies significant predictors of investment outcomes. While the
model shows moderate predictive performance (R2 = 0.185; MAPE = 172.96%), it identi-
fies hierarchical relationships among behavioral, cognitive, and demographic predictors.
These results highlight the complexity of investment decisions and the need for integra-
tive, behavioral-driven approaches in predictive modeling. Investment attitudes (25.88%),
decision-making behaviors (19.53%), and financial education (16.68%) emerge as the most
influential variables, while traditional demographic factors such as income and age have
a lower impact. The hierarchical structure of the decision tree highlights critical decision-
making patterns, particularly regarding speculative behaviors and investment attitudes.
These findings challenge classical models of rationality by emphasizing the dominant role
of behavioral factors in investment decision making. This study contributes to bridging
computational modeling with financial economics, demonstrating the utility of decision
tree regression in uncovering complex investor behavior. Practical implications include
enhancing personalized financial advisory services and designing targeted financial literacy
programs to improve decision-making efficiency. These insights, while exploratory, can
guide future research and decision-support systems in behavioral finance.

Keywords: decision tree regression; investment decisions; behavioral finance; financial
predictors; computational modeling

1. Introduction

Understanding the factors that influence investment interest is a critical area of inquiry
in both financial research and practice. Investment interest, or the degree to which individ-
uals engage with and are motivated to participate in investment activities, is influenced
by a range of behavioral, attitudinal, educational, and contextual factors. Grounded in the
frameworks of behavioral finance theory [1,2] and prospect theory [3,4], this study exam-
ines the role of multiple predictors, including investment attitudes, financial education,

Academic Editors: Agnieszka Konys

and Agnieszka Nowak-Brzezi ´nska

Received: 5 February 2025

Revised: 5 April 2025

Accepted: 7 April 2025

Published: 9 April 2025

Citation: Rad, D.; Cuc, L.D.;

Croitoru, G.; Gomoi, B.C.; Mazuru, L.;

Bilt,i, R.S.; Rusu, S.; Sinaci, M.; Barbu,

F.S. Modeling Investment Decisions

Through Decision Tree Regression—A

Behavioral Finance Theory Approach.

Electronics 2025, 14, 1505. https://

doi.org/10.3390/electronics14081505

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Electronics 2025, 14, 1505

https://doi.org/10.3390/electronics14081505

---

<!-- PAGE 2 -->

Electronics 2025, 14, 1505

2 of 17

speculative investment attitudes, resilience after financial losses, decision adaptability after
losses, decision-making behaviors in investments, and trust in AI-based financial systems,
in shaping investment interest.

Behavioral finance theory provides a foundation for understanding how psycho-
logical factors, including cognitive biases and emotional responses, influence financial
decisions. It challenges the traditional “homo economicus” assumption of rational decision
making, emphasizing the systematic deviations from rationality observed in real-world
investor behavior [5,6]. Prospect theory complements this by explaining how individuals
perceive gains and losses asymmetrically, often exhibiting risk aversion for gains and risk-
seeking behavior for losses [7]. These theoretical frameworks are particularly relevant for
analyzing the complex relationships among behavioral and attitudinal factors in investment
decision making.

Investment attitudes—individuals’ perceptions of the benefits, risks, and im-portance
of investing—are pivotal in shaping investment interest. Research has shown that positive
attitudes towards investing correlate with higher engagement and better decision-making
outcomes [8,9]. Similarly, financial education plays a crucial role in equipping individuals
with the knowledge and skills needed to make informed investment decisions. Studies
highlight the positive impact of financial literacy on both investment attitudes and perfor-
mance [10,11]. Financially educated individuals are more likely to understand risks, assess
opportunities, and optimize returns.

Speculative investment attitudes reflect a willingness to engage in high-risk, high-
reward financial activities. These tendencies influence the degree of investment interest
shown by individuals. Research suggests that attitudes towards speculative investments,
such as cryptocurrencies or other volatile assets, are shaped by financial risk tolerance and
personal values [12,13]. Additionally, resilience in the face of financial losses is essential
for maintaining long-term investment engagement. Studies on resilience after financial
losses demonstrate that individuals who view losses as opportunities for learning are better
equipped to recover and adapt [14,15].

Adaptability in decision making following financial setbacks is another crucial fac-
tor. Decision adaptability after losses reflects an investor’s ability to revise strategies
based on past experiences, which is essential for navigating volatile markets [16,17]. This
adaptability is closely linked to overall decision-making behaviors in investments, which
include systematic practices such as portfolio diversification and reliance on expert advice.
Prior research underscores the importance of deliberate and informed decision making in
achieving favorable investment outcomes [18,19].

In recent years, the integration of artificial intelligence (AI) into financial systems has
introduced a new dimension to investment decision making. Trust in AI-based financial
systems has become a significant determinant of investment interest, as individuals in-
creasingly rely on AI-driven tools for financial analysis and recommendations. Studies
indicate that trust in AI systems is influenced by perceptions of reliability, transparency,
and performance [20,21]. As AI-enabled platforms become more prevalent, understanding
the role of trust in shaping user engagement is critical [22].

This study builds on the existing literature by integrating these diverse factors into a
comprehensive model of investment interest. By employing decision tree regression, we
aim to identify the hierarchical relationships among these predictors and provide actionable
insights for financial educators, advisors, and policymakers. The findings contribute to the
broader understanding of how behavioral, educational, and technological factors interact to
shape investment behavior, offering practical implications for improving financial literacy
and decision making in diverse populations.

---

<!-- PAGE 3 -->

Electronics 2025, 14, 1505

3 of 17

The primary aim of this study is to investigate the behavioral, cognitive, demographic,
and technological predictors of investment interest using a data-driven modeling approach.
Specifically, this research applies decision tree regression to identify the most influential
factors shaping individual investment behaviors. While grounded in behavioral finance
theory and prospect theory, this is not a literature review but an empirical study based on a
structured questionnaire administered to a sample of financial professionals. The research
seeks to (1) model the hierarchy of influences affecting investment interest, (2) assess the
predictive strength of these variables, and (3) offer practical implications for financial
education, advisory services, and digital investment tools.

Unlike previous studies which primarily used linear models such as logistic or multi-
ple regression, this research employs decision tree regression (DTR) to model non-linear
relationships between behavioral predictors and investment interest. DTR offers a transpar-
ent and interpretable structure, which is critical in behavioral finance, where interactions
among psychological and contextual variables can be complex. The novelty of this study
lies in its integration of DTR within the behavioral finance framework, offering a hierar-
chical view of how attitudinal, educational, and technological factors collectively shape
investment behavior.

Literature Review

Investment decisions have long been a central focus of financial research, with a variety
of factors influencing both individual and corporate investment behaviors. The extant
literature highlights the interplay of financial, demographic, behavioral, and contextual
variables in shaping investment decisions, often framed within theoretical perspectives
such as behavioral finance theory [1,6] and prospect theory [3]. This section synthesizes
findings across multiple domains to elucidate the determinants of investment interest
and behavior.

Financial constraints, market conditions, and economic variables have consistently
been found to influence corporate and individual investment decisions. Ref. [23] compared
investment behaviors across Belgium, France, Germany, and the United Kingdom, finding
that financial constraints significantly limit corporate investment. Similarly, Ref. [24] ex-
plored investment decisions in transitional China, revealing that financial factors, including
liquidity and cost of capital, are critical determinants. This aligns with earlier findings
by [25], who demonstrated that financial constraints significantly impede firm-level in-
vestment. In individual contexts, Ref. [26] identified liquidity as a key determinant of
investment choices, while Ref. [27] highlighted the relevance of macroeconomic conditions.
The role of financial literacy and education in facilitating better investment decisions
is also widely recognized. Ref. [28] emphasized the critical need for financial education
to enhance retirement preparedness and informed decision making. This is supported
by [10], who demonstrated the positive impact of financial literacy programs on high school
students’ investment attitudes. Ref. [29] further corroborated these findings, noting that
financially literate investors in the UAE make more rational and informed decisions. Such
insights are echoed by [11], stressing the broader implications of financial education for
economic stability and individual financial well-being.

Behavioral finance has shed a light on how cognitive biases and emotional factors
influence investment decisions. Ref. [30] identified key behavioral factors such as overcon-
fidence, loss aversion, and herd behavior among institutional investors at the Nairobi Stock
Exchange. These findings align with those of [31], who examined the psychological under-
pinnings of individual investment decisions. Ref. [32] employed the analytical hierarchy
process (AHP) to quantify the impact of behavioral factors, noting that risk perception and
emotional stability significantly shape investment behaviors.

---

<!-- PAGE 4 -->

Electronics 2025, 14, 1505

4 of 17

Prospect theory has been particularly influential in understanding the asymmetrical
attitudes toward gains and losses. Ref. [7] highlighted how individuals exhibit risk aversion
in the face of gains but are willing to take greater risks to recover losses. This dynamic was
further supported by studies such as those by [33,34], which illustrated how past losses
could trigger heightened risk-taking behaviors among investors.

Demographic variables such as age, income, education, and employment status also
play a critical role in investment decisions. Ref. [27] demonstrated that younger investors
are more likely to engage in high-risk investments, whereas older individuals tend to
prioritize safety and stability. Similarly, Ref. [35] found that financial literacy levels and
demographic characteristics jointly influence investment preferences, with higher-income
individuals demonstrating a greater propensity for diversified portfolios. Studies by [36,37]
further confirmed the importance of demographic factors in shaping financial behaviors,
noting significant variations based on gender, income, and educational attainment.

Strategic decision-making processes in investment are often influenced by external
and contextual factors. Ref. [38] argued that aligning investments with broader strategic
goals enhances their perceived value, particularly in energy efficiency initiatives. Ref. [39]
emphasized the role of contextual factors such as market competition and regulatory
frameworks in shaping strategic investment decisions. Ref. [40] extended this analysis
to cross-border investments, highlighting the impact of finance-specific factors such as
currency stability and financial integration.

Recent advancements in technology, particularly in artificial intelligence (AI), have
transformed the landscape of investment decision making. Trust in AI-enabled financial
systems is emerging as a critical factor in shaping investor behavior. Studies by [20,41]
revealed that perceptions of reliability and transparency significantly influence the adoption
of AI-based tools.

Financial literacy and behavioral biases remain pivotal in both individual and insti-
tutional contexts, while strategic and technological considerations increasingly influence
modern investment landscapes.

Thus, the reviewed literature supports the relevance of integrating behavioral, demo-
graphic, and educational variables in understanding investment decisions. This literature
review informed the construction of the survey instruments used in this study. Each behav-
ioral dimension analyzed—such as investment attitudes, speculative behaviors, resilience
after losses, and trust in AI—was derived from constructs identified as influential in prior
studies. This connection between theoretical background and empirical instrumentation
ensures the study’s conceptual coherence. Empirical studies have shown that financial edu-
cation significantly shapes investment attitudes and long-term financial decision-making
behavior. For example, Becchetti et al. [10] demonstrated through a randomized controlled
trial how educational interventions can positively influence students’ financial choices
and attitudes toward investing. These findings reinforce the behavioral underpinnings of
investment interest, supporting the integration of cognitive and attitudinal variables in
predictive modeling.

Recent studies have demonstrated the utility of decision tree-based models in finan-
cial behavior prediction. For example, Sun and collaborators developed a decision tree
ensemble method combining SMOTE and bagging to address class imbalance in enterprise
credit evaluation, demonstrating improved predictive accuracy and robustness in complex
financial contexts [22]. This approach underscores the relevance and adaptability of tree-
based algorithms in modeling investor behaviors where data imbalance and non-linear
interactions are prevalent.

---

<!-- PAGE 5 -->

Electronics 2025, 14, 1505

5 of 17

2. Materials and Methods
2.1. Participants

This study utilized a convenience sampling method, targeting networks of economists
and financial professionals. Recruitment was conducted primarily through online plat-
forms, with a Google Forms questionnaire distributed via email and professional social
media channels. Participation was voluntary, and all respondents provided informed
consent prior to completing the survey. Data collection was anonymous, ensuring confi-
dentiality throughout the process.

Participants were recruited from professional networks and academic associations
related to economics and finance. Eligibility required a basic level of investment experience
and understanding, ensuring respondents could meaningfully answer questions about
financial behaviors. Prior to survey distribution, an expert panel of three specialists in
behavioral finance and psychometrics reviewed the item pool to ensure clarity, relevance,
and content validity. Items were adapted from validated instruments and revised through
cognitive interviews with five pilot participants. These steps enhanced the credibility and
replicability of the research process.

A total of 548 participants completed the survey. Regarding gender distribution,
38% of respondents identified as male (n = 208), while 62% identified as female (n = 340).
In terms of education level, 21.4% (n = 117) reported having completed high school or
equivalent, 40.9% (n = 224) held a bachelor’s degree, 31.9% (n = 175) had a master’s degree,
and 5.8% (n = 32) reported holding a doctoral degree.

Participants’ employment status was categorized into four groups: 11.7% (n = 64)
reported being unemployed, 4% (n = 22) were employed part-time, 75% (n = 411) were
employed full-time, and 9.3% (n = 51) identified as freelancers or self-employed. Income
levels varied, with 19.3% (n = 106) reporting a monthly income below 3000 RON, 35.6%
(n = 195) earning between 3000–5000 RON, 20.1% (n = 110) earning between 5000 and
7000 RON, 8.9% (n = 49) earning between 7000 and 9000 RON, and 16.1% (n = 88) earning
above 9000 RON per month.

Participants’ professional experience was distributed as follows: 31.4% (n = 172)
reported less than five years of experience, 33.4% (n = 183) had between five and ten
years, 11.5% (n = 63) had ten to fifteen years, and 23.7% (n = 130) had over fifteen years of
professional experience.

This diverse sample provided a robust foundation for exploring financial behaviors
and attitudes across various demographic and professional contexts. While convenience
sampling allowed rapid access to a specific professional population, it introduced potential
selection bias and limited the generalizability of the findings. Future research should aim
for stratified or random sampling to improve representativeness.

The recruitment process involved distributing the survey to over 1000 individuals
via professional mailing lists, university alumni databases, and finance-related online
communities. From these, 548 responses were received and retained for analysis. The
exclusion criteria included incomplete responses.

2.2. Instruments

To analyze the factors influencing financial decision making, a set of rigorously devel-
oped scales was utilized, each comprising 7 to 14 items. These instruments were designed
to measure behavioral, attitudinal, and cognitive dimensions critical to investment-related
choices. The scales demonstrated strong reliability, with Cronbach’s alpha values ranging
from 0.84 to 0.93.

The questionnaire consisted of 8 distinct scales covering behavioral, attitudinal, cogni-
tive, technological, and demographic dimensions. Each scale used a 5-point Likert-type

---

<!-- PAGE 6 -->

Electronics 2025, 14, 1505

6 of 17

response format, ranging from 1 (strongly disagree) to 5 (strongly agree). Higher scores
reflected stronger agreement with the construct being measured.

Investment interest captured the level of engagement individuals displayed toward fi-
nancial investments, encompassing activities like seeking information and staying updated
on market trends. For instance, participants responded to items such as the following:
“How often do you seek information about financial investments?”, adapted from [42]. The
scale displayed a Cronbach’s alpha of 0.86, reflecting high internal consistency.

Investment attitudes measured beliefs about the benefits, risks, and overall signifi-
cance of investing. This construct was vital for understanding how perceptions influence
financial behavior. An example item read, “Investing is essential for long-term financial
security.”, adapted from [43]. This scale achieved a Cronbach’s alpha of 0.91, underscoring
its reliability.

Financial education evaluated participants’ understanding of foundational financial
principles, such as saving, budgeting, and investment strategies, and their ability to apply
this knowledge effectively. A representative item was the following: “I understand the
concept of compound interest and its impact on savings.” (adapted from [28]). The scale
recorded a Cronbach’s alpha of 0.89, indicating robust reliability.

Speculative investment attitudes examined individuals’ perceptions of and engage-
ment with speculative investment options, including high-risk assets like crypto-currencies.
This construct shed light on risk tolerance and preferences. An example item included
the following: “Speculative investments are a viable way to achieve financial growth.”
(adapted from [4]). The scale demonstrated a Cronbach’s alpha of 0.87.

Resilience after financial losses assessed an individual’s emotional and behavioral
recovery following financial setbacks, reflecting their ability to regain confidence in future
investments. One item stated, “I view financial losses as an opportunity to learn and
improve my strategies.” (adapted from [3]). This scale had a Cronbach’s alpha of 0.84.

Decision adaptability after losses measured the flexibility in decision-making strategies
post loss, capturing how individuals recalibrated their approach to investing. A sample
item was the following: “After a financial loss, I reconsider my investment strategy to avoid
repeating mistakes.” The scale yielded a Cronbach’s alpha of 0.88.

Decision-making behaviors in investments evaluated the systematic and deliberate
approaches individuals used when making investment decisions, such as portfolio diversi-
fication and reliance on expert advice. An illustrative item was the following: “I diversify
my in-vestment portfolio to manage risk effectively.”, adapted from [44]. This scale had the
highest Cronbach’s alpha at 0.93.

Trust in AI-based financial systems explored confidence in automated tools and sys-
tems using artificial intelligence for financial management. This construct focused on
perceptions of technology’s reliability and utility. A representative item was the follow-
ing: “I trust AI-based systems to provide accurate financial recommendations.”, adapted
from [45]. The scale achieved a Cronbach’s alpha of 0.92, confirming its reliability.

2.3. Procedure

The analysis aimed to investigate the factors influencing investment interest, which
was designated as the dependent variable. The predictors included behavioral, attitudinal,
and demographic factors: investment attitudes, financial education, speculative investment
attitudes, resilience after financial losses, decision adaptability after losses, decision-making
behaviors in investments, trust in AI-based financial systems, and demographic variables
such as age, gender, education, income, and employment status.

The full list of factors included in the model is the following:

---

<!-- PAGE 7 -->

Electronics 2025, 14, 1505

7 of 17

•

•
•
•

Behavioral/Attitudinal: Investment attitudes, speculative investment attitudes, re-
silience after financial losses, decision-making behaviors in investments, and decision
adaptability after losses;
Cognitive: Financial education;
Technological: Trust in AI-based financial systems;
Demographic: Age, gender, education, income, employment status, and professional
experience.

The data were collected via an online questionnaire and processed in JASP (version
0.19.3), an open-source statistical software. JASP was chosen for its ease of use, accessibility,
and visual interpretability of tree structures, which aligns with the study’s applied focus.
However, future studies could replicate the analysis in Python (scikit-learn version 1.4.1) or
R (rpart, version 4.1.23) to allow greater control over model tuning and ensemble methods.
Preliminary analyses included descriptive statistics and frequency tables to summarize
participant characteristics. To model the relationships between the dependent variable
and predictors, decision tree regression was employed. This method was selected for its
ability to handle complex, non-linear relationships and provide interpretable hierarchical
structures in the form of decision trees.

Decision tree regression was trained and tested on the dataset, using a default
80/20 split for training and validation purposes. Model evaluation metrics, including
mean absolute error (MAE), mean absolute percentage error (MAPE), and R2, were cal-
culated to assess predictive performance. Given the 5-point Likert scale used for the
dependent variable, MAPE and R2 were prioritized as the most interpretable performance
metrics. Feature importance values were computed to determine the relative contribution
of each predictor to the model. Hyperparameters such as the tree’s maximum depth and
minimum samples per split were set to default in JASP. While this was a simplified inter-
pretation, it might have increased the risk of overfitting or underfitting. A grid search or
cross-validation approach could further optimize performance in future studies.

3. Results

Decision tree regression is a non-parametric supervised learning method that splits
data based on input variable values to predict continuous outcomes. The algorithm re-
cursively partitions the dataset by selecting splits that minimize the mean squared error
at each node. This structure reveals the hierarchical importance and interactions among
predictors, offering interpretable insights into complex behavioral patterns.

The results of the decision tree regression model provide insights into the predictors of
investment interest. The model was trained on 439 cases and tested on 109 cases, achieving
a test mean squared error (MSE) of 1.065, a root mean squared error (RMSE) of 1.032,
a mean absolute error (MAE) of 0.8, and a mean absolute percentage error (MAPE) of
172.96%. The R2 value of 0.185 indicated a modest proportion of variance in the investment
interest explained by the predictors. The dependent variable (investment interest) was
measured on a 5-point Likert scale. Given this limited scale range, the relatively low R2
(0.185) and high MAPE reflected the complex, subjective nature of investment interest and
the influence of unmeasured latent variables. The goal of this model was, therefore, not
precision forecasting but exploratory pattern recognition and predictor ranking. Thus, the
relatively low R2 value suggested that, while the model captured meaningful predictors,
other latent or contextual factors likely contributed to investment interest. This reflects
the inherent complexity of financial behavior, which is often influenced by non-observable
psychological or situational variables.

The relative importance of predictors (Table 1) revealed that investment attitudes were
the most influential factor, contributing 25.88% to the model. This was followed by decision-

---

<!-- PAGE 8 -->

Electronics 2025, 14, 1505

8 of 17

making behaviors in investments (19.53%) and financial education (16.69%), highlighting
the significant role of behavioral and educational dimensions in shaping investment interest.
Other important predictors included speculative investment attitudes (11.20%), decision
adaptability after losses (8.27%), and trust in AI-based financial systems (6.78%).

Demographic variables such as age (1.94%), experience (1.50%), income (1.09%), edu-
cation (0.39%), and employment status (0.28%) exhibited comparatively lower im-portance,
suggesting a lesser direct impact on investment interest compared to behavioral and attitu-
dinal factors.

Table 1. Feature importance.

Relative Importance

Investment attitudes
Decision-making behaviors in investments
Financial education
Speculative investment attitudes
Decision adaptability after losses
Trust in AI-based financial systems
Resilience after financial losses
Age
Experience
Income
Education
Status

25.883
19.534
16.686
11.195
8.273
6.775
6.439
1.940
1.503
1.094
0.394
0.283

The prominence of investment attitudes as the top predictor suggests a strong psy-
chological basis for financial engagement. Individuals with positive attitudes are more
proactive in seeking financial opportunities and show greater openness to using AI-based
investment tools, especially when trust in technology is present.

Decision tree regression revealed a hierarchical structure of predictors, with the most

significant splits occurring at various levels of the tree (Table 2).

Table 2. Splits in tree.

Obs. in Split

Split Point

Improvement

Investment attitudes
Investment attitudes
Speculative investment attitudes
Experience
Decision-making behaviors in investments
Decision-making behaviors in investments
Financial education
Decision-making behaviors in investments
Resilience after financial losses
Speculative investment attitudes
Financial education
Resilience after financial losses
Trust in AI-based financial systems
Trust in AI-based financial systems

439
142
132
73
48
25
297
282
75
22
207
100
89
27

−0.411
−2.020
−0.249
1.072
−0.240
−0.392
1.858
−0.392
0.267
−0.249
0.373
−0.811
−0.215
−0.568

0.160
0.191
0.165
0.122
0.231
0.314
0.136
0.113
0.102
0.286
0.062
0.112
0.124
0.337

Note. For each level of the tree, only the split with the highest improvement in deviance is shown.

Table 2 presents the most relevant decision tree splits, where “Obs. in Split” indicates
the number of observations at the node being split, “Split Point” represents the value
of the predictor at which the split occurs, and “Improvement” reflects the reduction in

---

<!-- PAGE 9 -->

Electronics 2025, 14, 1505

9 of 17

model deviance (a proxy for prediction error); higher improvement values indicate stronger
predictive contribution at that specific level of the tree.

The first split was based on investment attitudes, which emerged as the most influential
variable. At a split point of −0.411, this factor provided an improvement of 0.160 in the
model, emphasizing its foundational role in predicting investment interest. A subsequent
split within the same variable, at −2.020, yielded an even greater improvement of 0.191,
further highlighting its central importance.

The next critical split involved speculative investment attitudes, occurring at −0.249
and contributing an improvement of 0.165. This indicates that individuals’ perceptions and
engagement with speculative investments are also key drivers of their interest in financial
investments. Another significant split was observed with experience, at a point of 1.072,
which provided an improvement of 0.122, suggesting that professional experience plays a
supportive but secondary role in shaping investment behavior.

Decision-making behaviors in investments also appeared prominently in the tree
structure, with splits at −0.240 and −0.392, providing improvements of 0.231 and 0.314,
respectively. These findings underscore the importance of systematic and deliberate invest-
ment practices. Similarly, financial education splits at points such as 1.858 and 0.373 con-
tributed improvements of 0.136 and 0.062, indicating that financial knowledge significantly
complements other behavioral factors.

Other predictors, such as resilience after financial losses and trust in AI-based financial
systems, showed influence in lower-level splits, with respective improvements of 0.112 and
0.124. Their roles, though less prominent, suggested nuanced contributions to the overall
model. Notably, a split in trust in AI-based financial systems at −0.568 led to the highest
improvement at this level, with a value of 0.337, highlighting the emerging significance of
technological trust in financial contexts.

Overall, the tree structure highlights the dominant role of behavioral and attitudinal
factors, with demographic variables contributing more subtly to the prediction of invest-
ment interest. These results offer a comprehensive view of how different predictors interact
and contribute hierarchically to financial decision making (Figure 1).

Figure 1. Predictive performance plot.

Figure 1 illustrates the predictive performance of the decision tree regression model,
visualizing the relationship between observed and predicted values of the dependent
variable, investment interest. The plot provides an assessment of the model’s ability to
accurately predict the levels of investment interest based on the identified predictors.

---

<!-- PAGE 10 -->

Electronics 2025, 14, 1505

10 of 17

The scatterplot reveals a clustering of points around the diagonal line, which represents
perfect prediction. While there is some dispersion, particularly at extreme values, the
general alignment of data points with the diagonal indicates that the model captures the
overall trend effectively. This is consistent with the model’s performance metrics, including
a test mean squared error (MSE) of 1.065 and a root mean squared error (RMSE) of 1.032,
which reflect a reasonable level of predictive accuracy. However, the modest R2 value
of 0.185 suggests that, while the model identifies key predictors, additional unmeasured
factors may contribute to unexplained variance.

The decision tree plot (Figure 2) illustrates the hierarchical structure of the regression
model used to predict investment interest, highlighting the sequential importance of the
predictors. The root node identifies investment attitudes as the most significant variable,
splitting the dataset at a value of −0.411. This confirms that investment attitudes are the
strongest driver of investment interest, as indicated in the feature importance analysis.
For individuals with lower investment attitudes (<−0.411), further splits occur at −2.02
within the same variable, underscoring its critical role. Subsequent splits in this branch are
determined by speculative investment attitudes (<−0.249), followed by experience (<1.07)
and decision-making behaviors in investments, which refine the prediction for individuals
with negative or low attitudes toward investments.

Figure 2. Decision tree plot.

For individuals with higher investment attitudes (≥−0.411), the next significant split
is based on financial education (<1.86), demonstrating the role of financial knowledge in
distinguishing levels of investment interest among this group. The tree further branches
on variables such as decision-making behaviors in investments (<−0.392), resilience after
financial losses (<0.267), and speculative investment attitudes (<−0.249). Deeper splits in
the right subtree also include trust in AI-based financial systems, reflecting the emerging
relevance of technological trust in financial decision-making contexts.

The terminal nodes represent predicted levels of investment interest, with each node
displaying the predicted score and the number of observations (n) in that subset. These

---

<!-- PAGE 11 -->

Electronics 2025, 14, 1505

11 of 17

terminal nodes provide insights into the segmentation of participants based on their
characteristics and predictors. The tree demonstrates that investment attitudes play a foun-
dational role, with variables such as financial education, speculative investment attitudes,
and decision-making behaviors acting as critical secondary influences. Other factors, like
resilience after financial losses and trust in AI-based financial systems, contribute more
nuanced effects at deeper levels of the tree.

Although the full decision tree includes multiple levels of splits, this depth reflects
the complexity of interactions among behavioral and demographic predictors. The deeper
branches capture complex decision pathways that may apply to specific investor profiles,
while the upper levels highlight the most influential variables overall. This structure allows
for both general and detailed interpretation of investment interest segmentation.

4. Discussion

The findings of this study highlight the complex nature of investment decisions,
underscoring the interplay between behavioral, financial, demographic, and technological
factors. These results align with and expand upon the existing literature, offering significant
implications for investors, policymakers, and financial institutions.

The dominance of behavioral factors, such as investment attitudes, decision-making
behaviors, and speculative investment attitudes, reflects the critical role of psychology in
financial decision making. Behavioral biases, such as overconfidence and loss aversion,
influence how individuals perceive and respond to investment opportunities, as supported
by [46]. These findings are consistent with behavioral finance theory [1,6], which posits
that psychological influences often override rational financial analysis. The results also
highlight generational differences, as younger investors, particularly from Generation
Y, exhibit higher engagement in speculative investments [46]. This has implications for
financial education programs tailored to specific demographic groups, as emphasized
by [35,47].

The observed influence of demographic factors, such as income, education, and em-
ployment status, corroborates earlier studies that emphasize their importance in shaping
investment preferences. For instance, Refs. [48,49] highlight how macroeconomic and
socio-economic factors influence individual investment behavior in developing economies.
Furthermore, the interplay between financial literacy and demographic variables, as demon-
strated by [10,11], underscores the need for targeted financial literacy initiatives to bridge
gaps in investment knowledge and participation.

The findings demonstrate the importance of financial education in fostering informed
investment decisions, aligning with studies by [28,50]. Financially educated individu-
als are better equipped to evaluate risks and returns, enhancing their decision-making
processes. These results hold strategic implications for policymakers and educational
institutions, particularly in designing programs to enhance financial literacy. Ref. [47]
emphasizes that financial literacy in developing economies is critical to improving invest-
ment outcomes, which is especially pertinent for emerging markets like Pakistan and other
developing regions.

The role of strategic investment decision making, as highlighted in this study, aligns
with findings from [51,52], underscoring the importance of non-financial drivers in strategic
contexts, such as renewable energy and nuclear sectors. These insights extend to individual
investors, where alignment with long-term strategic goals can improve decision outcomes.
Additionally, this study confirms the relevance of contextual factors in shaping investment
behavior, consistent with findings by [53] on real estate investments and [54] on foreign
direct investment. Advanced analytical methods, such as fuzzy clustering and decision tree
modeling, have been shown to provide valuable insights into complex decision-making pro-

---

<!-- PAGE 12 -->

Electronics 2025, 14, 1505

12 of 17

cesses, highlighting their potential application in understanding financial behaviors [55,56].
Recent advancements in machine learning and decision tree methodologies, such as split
difference weighting and self-aware prediction models, offer promising solutions for ad-
dressing imbalances and improving investment recommendations [57,58]. Also, techniques
such as fuzzy-payoff methods and multi-period decision trees have demonstrated signifi-
cant utility in evaluating sustainable investment opportunities, bridging behavioral and
strategic considerations [56,59].

The growing significance of trust in AI-based financial systems observed in this study
reflects the increasing reliance on technology for investment decision making. These
findings are consistent with the recent literature, such as [20], highlighting the role of
transparency and reliability in fostering trust in AI systems. As financial technologies
continue to evolve, financial institutions must prioritize user trust through transparent
and user-friendly AI solutions. This is particularly important in the post-pandemic era,
where digital solutions are reshaping traditional investment processes [53]. The adoption
of advanced clustering analyses in management and accounting practices further illustrates
the potential for enhancing investor profiling and service customization [60].

These insights are valuable for financial advisors seeking to personalize investment rec-
ommendations. Behavioral segmentation models can help financial service providers adapt
their approaches to risk-tolerant versus risk-averse clients. Moreover, education programs
should prioritize not only general financial literacy but also psychological preparedness
for speculative environments, helping individuals develop resilience and adaptability. For
researchers, the hierarchical modeling provided by decision trees offers an alternative to
linear approaches, capturing non-linear and interactive effects often missed in traditional
econometric analyses.

Compared to traditional linear models, decision tree regression offers interpretability
and non-linearity but may lack robustness in high-dimensional data. Future research should
explore ensemble models like random forests or XGBoost, which offer better generalization.
Additionally, Bayesian or deep learning methods could provide more nuanced modeling of
investor uncertainty.

The integration of AI and other digital tools in financial decision making presents
both opportunities and challenges. While AI-based systems can provide accurate and
data-driven insights, they must also address concerns about data security and ethical
decision making, as suggested by [41]. These findings underscore the need for regulatory
frameworks to govern the use of AI in finance, ensuring both trust and accountability.
Additionally, the integration of emotional and behavioral insights into AI-based systems,
such as those examining the role of trust and friendship in information-sharing behav-
iors [61], highlights the importance of user-centric approaches in fostering engagement
and trust in financial technologies. Trust in AI is not only about system performance but
also ethical and emotional considerations. As Pelau and collaborators note, perceptions of
“friendship” and emotional trust in AI systems significantly affect information-sharing and
engagement [61]. Financial AI tools must therefore address emotional UX design alongside
accuracy.

The role of technological advancements, including cloud computing services [62] and
risk management systems for sustainable development [63], further illustrates the transfor-
mative potential of AI in addressing investment complexities. Similarly, considerations of
cryptocurrency’s impact on accounting practices [64] and sustainability-focused business
models [65] underscore the need for aligning technological innovations with evolving
market demands.

The results of this study hold broader implications for policymakers and practitioners.
For developing economies, such as those discussed by [48,66], improving financial literacy

---

<!-- PAGE 13 -->

Electronics 2025, 14, 1505

13 of 17

and access to financial services can significantly enhance investment participation and
outcomes. Policymakers should consider implementing targeted interventions, such as tax
incentives for investment in financial education programs, to address gaps in literacy and
participation.

For financial institutions, understanding the behavioral and demographic nuances of
investors can inform the design of personalized investment products and advisory services.
By leveraging AI and big data analytics, institutions can tailor solutions to meet the needs of
diverse investor profiles, as highlighted by [20]. Furthermore, the integration of behavioral
insights into financial advisory services can improve engagement and decision making, as
emphasized by [52,67].

Policymakers can apply these findings by integrating behavioral segmentation into
public financial literacy campaigns, tailoring messages to match investor profiles (e.g.,
speculative vs. risk-averse). Financial institutions can use DTR-based profiles to customize
robo-advisory systems and align product offerings with behavioral predictors.

5. Conclusions

Future research should explore complementary modeling approaches to deepen the
insights obtained from behavioral predictors. In particular, the analytic hierarchy pro-
cess (AHP) and fuzzy logic represent valuable methods for multi-criteria decision mak-
ing under uncertainty. AHP facilitates pairwise comparisons and priority rankings of
investment-related criteria, enabling researchers to assess trade-offs between risk, return,
and psychological comfort [68]. Similarly, fuzzy logic models the imprecision inherent in
human judgment, capturing the degrees of investor preferences and beliefs in a flexible
manner [69]. These techniques would allow for a more systematic evaluation of investor
decision patterns and could be used in combination with machine learning models for
enhanced hybrid approaches. Exploring these methods may also provide a stronger foun-
dation for personalized financial advisory tools.

This study provides exploratory insights into the factors associated with investment
interest, emphasizing the potential of integrating behavioral, educational, and technolog-
ical variables into predictive modeling frameworks. The results tentatively suggest that
behavioral factors, particularly investment attitudes and decision-making behaviors, may
play a more pronounced role compared to traditional demographics, though further vali-
dation is needed. Additionally, this study highlights the growing significance of financial
literacy and AI-driven technologies in shaping investment strategies, reinforcing the need
for adaptive financial education and personalized advisory services.

Although this study contributed valuable insights, it had several limitations. First, the
reliance on self-reported data might have introduce response biases, namely social desirabil-
ity or recall bias, as individuals’ stated investment behaviors may not fully align with their
actual financial decisions. Future studies should consider integrating objective financial
data or experimental methodologies to mitigate this limitation. Second, the study’s sample
was non-random and, thus, limited in scope, potentially restricting the generalizability of
the findings to other regions or investor groups. The use of a single predictive algorithm
might have also constrained the study’s broader applicability. Expanding the dataset to
include a more diverse population across different economic backgrounds and investment
environments would enhance the robustness of the conclusions. Finally, while decision
tree regression provided valuable insights into predictive relationships, this study does
not account for potential interactions between variables. Future research could employ
ensemble models or deep learning techniques to capture more complex decision-making
patterns.

---

<!-- PAGE 14 -->

Electronics 2025, 14, 1505

14 of 17

The results have significant implications for policymakers, financial institutions, and
investors. For policymakers, the findings emphasize the need for targeted financial liter-
acy programs, particularly for younger investors and individuals with limited financial
education. Governments could implement incentive-driven initiatives to promote finan-
cial awareness and responsible investment behaviors. Financial institutions, on the other
hand, should leverage behavioral insights to design personalized investment products
and AI-driven advisory services that account for cognitive biases and risk perceptions.
The increasing role of technology in investment decisions suggests that institutions must
prioritize transparency, trust, and ethical considerations in AI-powered financial tools.
Additionally, this study reinforces the importance of integrating behavioral finance prin-
ciples into traditional investment strategies, offering a more comprehensive approach to
understanding market behavior.

Additional work could test ensemble learning methods or apply the current methodol-
ogy in cross-cultural settings to examine how investment predictors vary across economic
systems. A hybrid approach that integrates behavioral scoring with machine learning
could also enhance real-time financial advising systems. Future research should explore
the dynamic interplay between behavioral, technological, and financial factors in differ-
ent economic and cultural contexts. Specifically, longitudinal studies could provide a
deeper understanding of how investor behaviors evolve over time in response to market
fluctuations and financial education initiatives. Additionally, examining sector-specific
investment behaviors—such as in sustainable finance, cryptocurrency, or real estate—could
offer more tailored insights into decision-making processes. Further research should also
investigate the ethical and regulatory challenges associated with AI-driven investment
platforms, particularly in ensuring fairness, privacy, and data security. Lastly, interdisci-
plinary approaches combining behavioral finance, machine learning, and neuroscience
could provide groundbreaking perspectives on how emotions and cognitive biases shape
financial decision making.

Building on these exploratory results, future research should adopt longitudinal
designs to track changes in investment behavior over time and across economic cycles.
Applying more advanced algorithms—such as random forests, gradient boosting, and deep
learning networks—could improve prediction accuracy. Cross-national comparisons would
also be valuable in examining how cultural and institutional contexts shape investment
attitudes. Lastly, integrating behavioral data with real financial behavior (e.g., transaction
records) could enhance the ecological validity of predictive models.

In conclusion, this study advances the field of investment decision making by integrat-
ing multiple dimensions of financial behavior. The findings call for a more holistic approach
to investment strategies, combining behavioral insights with technological advancements
to enhance decision-making efficiency and financial well-being. Ongoing research and
innovation in financial literacy, AI-driven advisory systems, and regulatory frameworks
will be crucial in shaping the future of investment practices in an increasingly digital and
complex financial landscape.

Author Contributions: Conceptualization, D.R., L.D.C. and G.C.; methodology, L.D.C., B.C.G., L.M.
and D.R.; software, D.R., B.C.G., S.R. and R.S.B.; validation, G.C., S.R. and M.S.; formal analysis,
L.D.C., D.R. and F.S.B.; investigation, B.C.G., S.R. and M.S.; resources, L.D.C., L.M. and F.S.B.; data
curation, G.C., R.S.B. and B.C.G.; writing—original draft preparation, L.D.C., D.R. and L.M.; writing—
review and editing, D.R., G.C. and F.S.B.; visualization, G.C., S.R. and R.S.B.; supervision, D.R., L.D.C.
and G.C.; project administration, L.D.C., D.R. and F.S.B.; and funding acquisition, B.C.G., S.R. and
F.S.B. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

---

<!-- PAGE 15 -->

Electronics 2025, 14, 1505

15 of 17

Institutional Review Board Statement: This study was conducted in accordance with the Declaration
of Helsinki and approved by the Centre for Economic Research and Consultancy of Aurel Vlaicu
University of Arad (protocol code 15/5 April 2023).

Informed Consent Statement: Informed consent was obtained from all the subjects involved in
this study.

Data Availability Statement: The data supporting our findings can be provided by the corresponding
author upon reasonable request.

Conflicts of Interest: The authors declare no conflicts of interest.

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

Brooks, M.; Byrne, A. Behavioral Finance: Theories and Evidence; The Research Foundation of CFA Institute: Charlottesville, VA,
USA; University of Edinburgh: Edinburgh, UK, 2008.
Fromlet, H. Behavioral finance-theory and practical application: Systematic analysis of departures from the homo oeconomicus
paradigm are essential for realistic financial research and analysis. Bus. Econ. 2001, 36, 63–69.
Kahneman, D.; Tversky, A. Prospect theory: An analysis of decision under risk. In Handbook of the Fundamentals of Financial
Decision Making: Part I; World Scientific: Singapore, 2013; pp. 99–127.
Barberis, N. Thirty years of prospect theory in economics: A review and assessment. J. Econ. Perspect. 2013, 27, 173–196. [CrossRef]
Ritter, J.R. Behavioral finance. Pac. Basin Financ. J. 2003, 11, 429–437. [CrossRef]
Shiller, R.J. From efficient markets theory to behavioral finance. J. Econ. Perspect. 2003, 17, 83–104. [CrossRef]
Tversky, A.; Kahneman, D. Advances in prospect theory: Cumulative representation of uncertainty. J. Risk Uncertain. 1992, 5,
297–323. [CrossRef]
Lease, R.C.; Lewellen, W.G.; Schlarbaum, G.G. The individual investor: Attributes and attitudes. J. Financ. 1974, 29, 413–433.
[CrossRef]
Aram, J.D. Attitudes and behaviors of informal investors toward early-stage investments, technology-based ventures, and
coinvestors. J. Bus. Ventur. 1989, 4, 333–347. [CrossRef]

10. Becchetti, L.; Caiazza, S.; Coviello, D. Financial education and investment attitudes in high schools: Evidence from a randomized

experiment. Appl. Financ. Econ. 2013, 23, 817–836. [CrossRef]

11. Lusardi, A. Financial literacy and the need for financial education: Evidence and implications. Swiss J. Econ. Stat. 2019, 155, 1.

[CrossRef]

12. Arthur, J.N.; Williams, R.J.; Delfabbro, P.H. The conceptual and empirical relationship between gambling, investing, and

speculation. J. Behav. Addict. 2016, 5, 580–591. [CrossRef]

13. Keller, C.; Siegrist, M. Investing in stocks: The influence of financial risk attitude and values-related money and stock market

attitudes. J. Econ. Psychol. 2006, 27, 285–303. [CrossRef]

14. Tomasic, R.; Akinbami, F. The role of trust in maintaining the resilience of financial markets. J. Corp. Law. Stud. 2011, 11, 369–394.

[CrossRef]

15. Clarvis, M.H.; Bohensky, E.; Yarime, M. Can resilience thinking inform resilience investments? Learning from resilience principles

for disaster risk reduction. Sustainability 2015, 7, 9048–9066. [CrossRef]

16. Lee, K.M.C.; Kraussl, R.G.W.; Lucas, A.; Paas, L.J. A dynamic model of investor decision-making: How adaptation to losses affects
future selling decisions. SSRN Electron. J. 2008. Available online: https://www.econstor.eu/bitstream/10419/87082/1/08-112.pdf
(accessed on 22 January 2025).

17. Monin, P. On a dynamic adaptation of the distribution builder approach to investment decisions. Quant. Financ. 2014, 14, 749–760.

[CrossRef]

18. Lucey, B.M.; Dowling, M. The role of feelings in investor decision-making. J. Econ. Surv. 2005, 19, 211–237. [CrossRef]
19. Renneboog, L.; Ter Horst, J.; Zhang, C. Socially responsible investments: Institutional aspects, performance, and investor behavior.

J. Bank. Financ. 2008, 32, 1723–1742. [CrossRef]

20. Maier, T.; Menold, J.; McComb, C. The relationship between performance and trust in AI in e-finance. Front. Artif. Intell. 2022, 5,

21.

22.

891529. [CrossRef]
Schreibelmayr, S.; Moradbakhti, L.; Mara, M. First impressions of a financial AI assistant: Differences between high trust and low
trust users. Front. Artif. Intell. 2023, 6, 1241290. [CrossRef]
Sun, J.; Lang, J.; Fujita, H.; Li, H. Imbalanced enterprise credit evaluation with DTE-SBD: Decision tree ensemble based on SMOTE
and bagging with differentiated sampling rates. Inf. Sci. 2018, 425, 76–91. [CrossRef]

23. Bond, S.; Elston, J.A.; Mairesse, J.; Mulkay, B. Financial factors and investment in Belgium, France, Germany, and the United

Kingdom: A comparison using company panel data. Rev. Econ. Stat. 2003, 85, 153–165. [CrossRef]

---

<!-- PAGE 16 -->

Electronics 2025, 14, 1505

16 of 17

24. Liu, J.; Pang, D. Financial factors and company investment decisions in transitional China. Manag. Decis. Econ. 2009, 30, 91–108.

[CrossRef]

25. Bond, S.; Meghir, C. Financial constraints and company investment. Fisc. Stud. 1994, 15, 1–18. [CrossRef]
26. Mills, K.; Morling, S.; Tease, W. The influence of financial factors on corporate investment. Aust. Econ. Rev. 1995, 28, 50–64.

[CrossRef]

27. Geetha, N.; Ramesh, M. A study on relevance of demographic factors in investment decisions. Perspect. Innov. Econ. Bus. 2012, 10,

14–28. [CrossRef]

28. Lusardi, A.; Mitchelli, O.S. Financial literacy and retirement preparedness: Evidence and implications for financial education.

Bus. Econ. 2007, 42, 35–44. [CrossRef]

29. Hassan Al-Tamimi, H.A.; Bin Kalli, A.A. Financial literacy and investment decisions of UAE investors. J. Risk Financ. 2009, 10,

500–516. [CrossRef]

30. Waweru, N.M.; Munyoki, E.; Uliana, E. The effects of behavioural factors in investment decision-making: A survey of institutional

investors operating at the Nairobi Stock Exchange. Int. J. Bus. Emerg. Mark. 2008, 1, 24–41. [CrossRef]

31. Lubis, H.; Kumar, M.D.; Ikbar, P.; Muneer, S. Role of psychological factors in individuals’ investment decisions. Int. J. Econ.

Financ. Issues 2015, 5, 397–405.

32. Antony, A.; Joseph, A.I. Influence of behavioural factors affecting investment decision—An AHP analysis. Metamorphosis 2017, 16,

107–114. [CrossRef]

33. Das, S.; Jain, R. A study on the influence of demographical variables on the factors of investment—A perspective on the Guwahati

region. Int. J. Res. Humanit. Arts Lit. 2014, 2, 97–102.

34. Masomi, S.R.; Ghayekhloo, S. Consequences of human behaviors in economics: The effects of behavioral factors in investment
decision making at Tehran Stock Exchange. In Proceedings of the International Conference on Business and Economics Research,
Langkawi, Malaysia, 14–16 March 2011; Volume 1, pp. 234–237.
Senda, D.A.; Rahayu, C.W.E.; Rahmawati, C.H.T. The effect of financial literacy level and demographic factors on investment
decision. Media Ekon. Manag. 2020, 35, 100–111. [CrossRef]

35.

36. Lutfi, L. The relationship between demographic factors and investment decision in Surabaya. J. Econ. Bus. Account. Ventur. 2010,

13, 1–9. [CrossRef]

37. Gaikar, V. Demographic variables influencing financial investment of urban individuals: A case study of selected districts of
Maharashtra State. SSRN Electron. J. 2021. Available online: https://ssrn.com/abstract=3890224 (accessed on 22 January 2025).
[CrossRef]

38. Cooremans, C. Make it strategic! Financial investment logic is not enough. Energy Effic. 2011, 4, 473–492. [CrossRef]
39. Alkaraan, F.; Northcott, D. Strategic Investment Decision-Making Processes: The Influence of Contextual Factors. Meditari

40.

Account. Res. 2013, 21, 117–143. [CrossRef]
Forssbæck, J.; Oxelheim, L. Finance-specific factors as drivers of cross-border investment—An empirical investigation. Int. Bus.
Rev. 2008, 17, 630–641. [CrossRef]

41. Zarifis, A.; Cheng, X. A model of trust in Fintech and trust in Insurtech: How artificial intelligence and the context influence it. J.

Behav. Exp. Financ. 2022, 36, 100739. [CrossRef]

42. Huston, S.J. Measuring financial literacy. J. Consum. Aff. 2010, 44, 296–316. [CrossRef]
43. Mandell, L.; Klein, L.S. The impact of financial literacy education on subsequent financial behavior. J. Financ. Couns. Plan. 2009,

20, 15–24.

44. Markowitz, H.M. Foundations of portfolio theory. J. Financ. 1991, 46, 469–477. [CrossRef]
45. Davis, F.D. Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Q. 1989, 13, 319–340.

[CrossRef]

46. Rahman, M.; Gan, S.S. Generation Y investment decision: An analysis using behavioural factors. Manag. Financ. 2020, 46,

1023–1041. [CrossRef]

47. Arif, K. Financial literacy and other factors influencing individuals’ investment decision: Evidence from a developing economy

48.

(Pakistan). J. Poverty Investig. Dev. 2015, 12, 74–84.
Salahuddin, M.; Islam, M.R. Factors affecting investment in developing countries: A panel data study. J. Dev. Areas 2008, 42,
21–37. [CrossRef]

49. Mlambo, K.; Oshikoya, T.W. Macroeconomic factors and investment in Africa. J. Afr. Econ. 2001, 10, 12–47. [CrossRef]
50. Love, I.; Zicchino, L. Financial development and dynamic investment behavior: Evidence from panel VAR. Q. Rev. Econ. Financ.

2006, 46, 190–210. [CrossRef]

51. Locatelli, G.; Mancini, M. The role of the reactor size for an investment in the nuclear sector: An evaluation of non-financial

parameters. Prog. Nucl. Energy 2011, 53, 212–222. [CrossRef]

52. Masini, A.; Menichetti, E. The impact of behavioral factors in the renewable energy investment decision-making process:

Conceptual framework and empirical findings. Energy Policy 2012, 40, 28–38. [CrossRef]

---

<!-- PAGE 17 -->

Electronics 2025, 14, 1505

17 of 17

53. Ngoc, N.M.; Tien, N.H.; Hieu, V.M. The relevance of factors affecting real estate investment decisions for post-pandemic time. Int.

J. Bus. Glob. 2023, 1, 1–15. [CrossRef]

54. Dutta, N.; Roy, S. Foreign direct investment, financial development and political risks. J. Dev. Areas 2011, 45, 303–327. [CrossRef]
55. Vesselenyi, T.; Dzi¸tac, I.; Dzi¸tac, S.; Vaida, V. Surface roughness image analysis using quasi-fractal characteristics and fuzzy

clustering methods. Int. J. Comput. Commun. Control 2008, 3, 304–316. [CrossRef]

56. Csorba, L.M.; Crăciun, M. An application of the multi-period decision trees in sustainable medical waste investments. In Soft
Computing Applications. SOFA 2016. Advances in Intelligent Systems and Computing; Balas, V., Jain, L., Balas, M., Eds.; Springer:
Cham, Switzerland, 2018; Volume 634, pp. 540–556.

57. Zhou, T.; Gao, X.; Sun, X.; Han, L. Split difference weighting: An enhanced decision tree approach for imbalanced classification.

Int. J. Comput. Commun. Control 2024, 19, 6702. [CrossRef]

58. Daranda, A.; Dzemyda, G. Novel machine learning approach for self-aware prediction based on contextual reasoning. Int. J.

Comput. Commun. Control 2021, 16, 4345. [CrossRef]

59. Crăciun, M.; Csorba, L.M. Application of the fuzzy-pay-off method in the valuation of a financial instrument. In Soft Computing
Applications. SOFA 2016. Advances in Intelligent Systems and Computing; Balas, V., Jain, L., Balas, M., Eds.; Springer: Cham,
Switzerland, 2018; Volume 634, pp. 235–252.

60. Cuc, L.D.; Rad, D.; Săplăcan, S.; Sendroiu, C.; Bâtcă-Dumitru, G.C.; Wysocki, D.; Dut,u, A.; Manolescu, A.-A. A hierarchical
clustering analysis of the management accounting practices perceptions in Romania. Int. J. Comput. Commun. Control 2024, 19,
6864. [CrossRef]

61. Pelau, C.; Dabija, D.C.; Stanescu, M. Can I trust my AI friend? The role of emotions, feelings of friendship and trust for consumers’

information-sharing behavior toward AI. Oeconomia Copernic. 2024, 15, 407–433. [CrossRef]

62. Toader, L.; Paraschiv, D.; Dinu, V.; Manea, D.; Mihai, M. The effects of private sector companies’ research and development
investments on the adoption of cloud computing services in the European Union. E+M Èkon. A Manag. 2023, 26, 189–202.
[CrossRef]

63. Ciocoiu, C.N.; Prioteasa, A.L.; Colesca, S.E. Risk management implementation for sustainable development of Romanian SMEs:

A fuzzy approach. Amfiteatru Econ. 2020, 22, 726–741. [CrossRef]

64. Lazea, G.I.; Bunget, O.C.; Lungu, C. Cryptocurrencies’ impact on accounting: Bibliometric review. Risks 2024, 12, 94. [CrossRef]
65. Ogrean, C.; Herciu, M. Business models addressing sustainability challenges—Towards a new research agenda. Sustainability

2020, 12, 3534. [CrossRef]

66. Anwar, K. Factors affecting stock exchange investment in Kurdistan. Int. J. Account. Bus. Soc. 2017, 25, 32–37. [CrossRef]
67. Carcello, J.V.; Hermanson, D.R.; Raghunandan, K. Factors associated with US public companies’ investment in internal auditing.

68.

Account. Horiz. 2005, 19, 69–84. [CrossRef]
Simone, F.; Ansaldi, S.M.; Agnello, P.; Di Gravio, G.; Patriarca, R. Knowledge in graphs: Investigating the completeness of
industrial near miss reports. Saf. Sci. 2023, 168, 106305. [CrossRef]

69. Patriarca, R.; De Carlo, F.; Leoni, L. A system-theoretic fuzzy analysis (STheFA) for systemic safety assessment. Process Saf.

Environ. Prot. 2023, 177, 1181–1196. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Article
Modeling Investment Decisions Through Decision Tree
Regression—A Behavioral Finance Theory Approach
DanaRad1,* ,LaviniaDenisiaCuc2,* ,GabrielCroitoru3 ,BogdanCosminGomoi2 ,LuminitaMazuru2,
,
RalucaSiminaBilti2,SergiuRusu2 ,MariaSinaci2 andFlorentinaSimonaBarbu2
,
1 CentreofResearchDevelopmentandInnovationinPsychology,FacultyofEducationalSciences,
AurelVlaicuUniversityofArad,310130Arad,Romania
2 CentreforEconomicResearchandConsultancy,FacultyofEconomics,AurelVlaicuUniversityofArad,
310130Arad,Romania;bogdan.gomoi@uav.ro(B.C.G.);luminita.mazuru@uav.ro(L.M.);
raluca.bilti@uav.ro(R.S.B.);sergiu.rusu@uav.ro(S.R.);maria.sinaci@uav.ro(M.S.);
florentina.barbu@uav.ro(F.S.B.)
3 FacultyofEconomics,ValahiaUniversityofTargoviste,130004Targoviste,Romania;
gabriel.croitoru@valahia.ro
* Correspondence:dana@xhouse.ro(D.R.);lavinia.cuc@uav.ro(L.D.C.)
Abstract: Thisstudyexaminesthekeyfactorsinfluencinginvestmentdecisionsthrough
decisiontreeregression,groundedinbehavioralfinancetheory. Byanalyzingacomprehen-
sivedatasetincorporatingbehavioral,demographic,andfinancialvariables—including
investmentattitudes,decision-makingbehaviors,financialeducation,age,income,and
education—thisstudyidentifiessignificantpredictorsofinvestmentoutcomes. Whilethe
modelshowsmoderatepredictiveperformance(R2 =0.185;MAPE=172.96%),itidenti-
fieshierarchicalrelationshipsamongbehavioral,cognitive,anddemographicpredictors.
Theseresultshighlightthecomplexityofinvestmentdecisionsandtheneedforintegra-
tive,behavioral-drivenapproachesinpredictivemodeling. Investmentattitudes(25.88%),
decision-makingbehaviors(19.53%),andfinancialeducation(16.68%)emergeasthemost
influentialvariables,whiletraditionaldemographicfactorssuchasincomeandagehave
alowerimpact. Thehierarchicalstructureofthedecisiontreehighlightscriticaldecision-
makingpatterns,particularlyregardingspeculativebehaviorsandinvestmentattitudes.
AcademicEditors:AgnieszkaKonys Thesefindingschallengeclassicalmodelsofrationalitybyemphasizingthedominantrole
andAgnieszkaNowak-Brzezin´ska ofbehavioralfactorsininvestmentdecisionmaking. Thisstudycontributestobridging
Received:5February2025 computationalmodelingwithfinancialeconomics,demonstratingtheutilityofdecision
Revised:5April2025 treeregressioninuncoveringcomplexinvestorbehavior. Practicalimplicationsinclude
Accepted:7April2025
enhancingpersonalizedfinancialadvisoryservicesanddesigningtargetedfinancialliteracy
Published:9April2025
programstoimprovedecision-makingefficiency. Theseinsights,whileexploratory,can
Citation: Rad,D.;Cuc,L.D.;
guidefutureresearchanddecision-supportsystemsinbehavioralfinance.
Croitoru,G.;Gomoi,B.C.;Mazuru,L.;
Bilt,i,R.S.;Rusu,S.;Sinaci,M.;Barbu,
Keywords: decisiontreeregression; investmentdecisions; behavioralfinance; financial
F.S.ModelingInvestmentDecisions
predictors;computationalmodeling
ThroughDecisionTreeRegression—A
BehavioralFinanceTheoryApproach.
Electronics2025,14,1505. https://
doi.org/10.3390/electronics14081505
1. Introduction
Copyright:©2025bytheauthors.
LicenseeMDPI,Basel,Switzerland. Understandingthefactorsthatinfluenceinvestmentinterestisacriticalareaofinquiry
Thisarticleisanopenaccessarticle inbothfinancialresearchandpractice. Investmentinterest,orthedegreetowhichindivid-
distributedunderthetermsand
ualsengagewithandaremotivatedtoparticipateininvestmentactivities,isinfluenced
conditionsoftheCreativeCommons
byarangeofbehavioral,attitudinal,educational,andcontextualfactors. Groundedinthe
Attribution(CCBY)license
frameworksofbehavioralfinancetheory[1,2]andprospecttheory[3,4],thisstudyexam-
(https://creativecommons.org/
licenses/by/4.0/). inestheroleofmultiplepredictors,includinginvestmentattitudes,financialeducation,
Electronics2025,14,1505 https://doi.org/10.3390/electronics14081505

Electronics2025,14,1505 2of17
speculativeinvestmentattitudes,resilienceafterfinanciallosses,decisionadaptabilityafter
losses,decision-makingbehaviorsininvestments,andtrustinAI-basedfinancialsystems,
inshapinginvestmentinterest.
Behavioral finance theory provides a foundation for understanding how psycho-
logical factors, including cognitive biases and emotional responses, influence financial
decisions. Itchallengesthetraditional“homoeconomicus”assumptionofrationaldecision
making,emphasizingthesystematicdeviationsfromrationalityobservedinreal-world
investorbehavior[5,6]. Prospecttheorycomplementsthisbyexplaininghowindividuals
perceivegainsandlossesasymmetrically,oftenexhibitingriskaversionforgainsandrisk-
seekingbehaviorforlosses[7]. Thesetheoreticalframeworksareparticularlyrelevantfor
analyzingthecomplexrelationshipsamongbehavioralandattitudinalfactorsininvestment
decisionmaking.
Investmentattitudes—individuals’perceptionsofthebenefits,risks,andim-portance
ofinvesting—arepivotalinshapinginvestmentinterest. Researchhasshownthatpositive
attitudestowardsinvestingcorrelatewithhigherengagementandbetterdecision-making
outcomes[8,9]. Similarly,financialeducationplaysacrucialroleinequippingindividuals
withtheknowledgeandskillsneededtomakeinformedinvestmentdecisions. Studies
highlightthepositiveimpactoffinancialliteracyonbothinvestmentattitudesandperfor-
mance[10,11]. Financiallyeducatedindividualsaremorelikelytounderstandrisks,assess
opportunities,andoptimizereturns.
Speculative investment attitudes reflect a willingness to engage in high-risk, high-
rewardfinancialactivities. Thesetendenciesinfluencethedegreeofinvestmentinterest
shownbyindividuals. Researchsuggeststhatattitudestowardsspeculativeinvestments,
suchascryptocurrenciesorothervolatileassets,areshapedbyfinancialrisktoleranceand
personalvalues[12,13]. Additionally,resilienceinthefaceoffinanciallossesisessential
formaintaininglong-terminvestmentengagement. Studiesonresilienceafterfinancial
lossesdemonstratethatindividualswhoviewlossesasopportunitiesforlearningarebetter
equippedtorecoverandadapt[14,15].
Adaptabilityindecisionmakingfollowingfinancialsetbacksisanothercrucialfac-
tor. Decision adaptability after losses reflects an investor’s ability to revise strategies
basedonpastexperiences,whichisessentialfornavigatingvolatilemarkets[16,17]. This
adaptabilityiscloselylinkedtooveralldecision-makingbehaviorsininvestments,which
includesystematicpracticessuchasportfoliodiversificationandrelianceonexpertadvice.
Priorresearchunderscorestheimportanceofdeliberateandinformeddecisionmakingin
achievingfavorableinvestmentoutcomes[18,19].
Inrecentyears,theintegrationofartificialintelligence(AI)intofinancialsystemshas
introducedanewdimensiontoinvestmentdecisionmaking. TrustinAI-basedfinancial
systems has become a significant determinant of investment interest, as individuals in-
creasinglyrelyonAI-driventoolsforfinancialanalysisandrecommendations. Studies
indicatethattrustinAIsystemsisinfluencedbyperceptionsofreliability,transparency,
andperformance[20,21]. AsAI-enabledplatformsbecomemoreprevalent,understanding
theroleoftrustinshapinguserengagementiscritical[22].
Thisstudybuildsontheexistingliteraturebyintegratingthesediversefactorsintoa
comprehensivemodelofinvestmentinterest. Byemployingdecisiontreeregression,we
aimtoidentifythehierarchicalrelationshipsamongthesepredictorsandprovideactionable
insightsforfinancialeducators,advisors,andpolicymakers. Thefindingscontributetothe
broaderunderstandingofhowbehavioral,educational,andtechnologicalfactorsinteractto
shapeinvestmentbehavior,offeringpracticalimplicationsforimprovingfinancialliteracy
anddecisionmakingindiversepopulations.

Electronics2025,14,1505 3of17
Theprimaryaimofthisstudyistoinvestigatethebehavioral,cognitive,demographic,
andtechnologicalpredictorsofinvestmentinterestusingadata-drivenmodelingapproach.
Specifically,thisresearchappliesdecisiontreeregressiontoidentifythemostinfluential
factorsshapingindividualinvestmentbehaviors. Whilegroundedinbehavioralfinance
theoryandprospecttheory,thisisnotaliteraturereviewbutanempiricalstudybasedona
structuredquestionnaireadministeredtoasampleoffinancialprofessionals. Theresearch
seeksto(1)modelthehierarchyofinfluencesaffectinginvestmentinterest,(2)assessthe
predictive strength of these variables, and (3) offer practical implications for financial
education,advisoryservices,anddigitalinvestmenttools.
Unlikepreviousstudieswhichprimarilyusedlinearmodelssuchaslogisticormulti-
pleregression,thisresearchemploysdecisiontreeregression(DTR)tomodelnon-linear
relationshipsbetweenbehavioralpredictorsandinvestmentinterest. DTRoffersatranspar-
entandinterpretablestructure,whichiscriticalinbehavioralfinance,whereinteractions
amongpsychologicalandcontextualvariablescanbecomplex. Thenoveltyofthisstudy
liesinitsintegrationofDTRwithinthebehavioralfinanceframework,offeringahierar-
chicalviewofhowattitudinal,educational,andtechnologicalfactorscollectivelyshape
investmentbehavior.
LiteratureReview
Investmentdecisionshavelongbeenacentralfocusoffinancialresearch,withavariety
of factors influencing both individual and corporate investment behaviors. The extant
literaturehighlightstheinterplayoffinancial,demographic,behavioral,andcontextual
variablesinshapinginvestmentdecisions,oftenframedwithintheoreticalperspectives
suchasbehavioralfinancetheory[1,6]andprospecttheory[3]. Thissectionsynthesizes
findings across multiple domains to elucidate the determinants of investment interest
andbehavior.
Financialconstraints,marketconditions,andeconomicvariableshaveconsistently
beenfoundtoinfluencecorporateandindividualinvestmentdecisions. Ref.[23]compared
investmentbehaviorsacrossBelgium,France,Germany,andtheUnitedKingdom,finding
thatfinancialconstraintssignificantlylimitcorporateinvestment. Similarly,Ref.[24]ex-
ploredinvestmentdecisionsintransitionalChina,revealingthatfinancialfactors,including
liquidity and cost of capital, are critical determinants. This aligns with earlier findings
by [25], who demonstrated that financial constraints significantly impede firm-level in-
vestment. In individual contexts, Ref. [26] identified liquidity as a key determinant of
investmentchoices,whileRef.[27]highlightedtherelevanceofmacroeconomicconditions.
Theroleoffinancialliteracyandeducationinfacilitatingbetterinvestmentdecisions
isalsowidelyrecognized. Ref.[28]emphasizedthecriticalneedforfinancialeducation
to enhance retirement preparedness and informed decision making. This is supported
by[10],whodemonstratedthepositiveimpactoffinancialliteracyprogramsonhighschool
students’investmentattitudes. Ref.[29]furthercorroboratedthesefindings,notingthat
financiallyliterateinvestorsintheUAEmakemorerationalandinformeddecisions. Such
insightsareechoedby[11],stressingthebroaderimplicationsoffinancialeducationfor
economicstabilityandindividualfinancialwell-being.
Behavioralfinancehasshedalightonhowcognitivebiasesandemotionalfactors
influenceinvestmentdecisions. Ref.[30]identifiedkeybehavioralfactorssuchasovercon-
fidence,lossaversion,andherdbehavioramonginstitutionalinvestorsattheNairobiStock
Exchange. Thesefindingsalignwiththoseof[31],whoexaminedthepsychologicalunder-
pinningsofindividualinvestmentdecisions. Ref.[32]employedtheanalyticalhierarchy
process(AHP)toquantifytheimpactofbehavioralfactors,notingthatriskperceptionand
emotionalstabilitysignificantlyshapeinvestmentbehaviors.

Electronics2025,14,1505 4of17
Prospecttheoryhasbeenparticularlyinfluentialinunderstandingtheasymmetrical
attitudestowardgainsandlosses.Ref.[7]highlightedhowindividualsexhibitriskaversion
inthefaceofgainsbutarewillingtotakegreaterriskstorecoverlosses. Thisdynamicwas
furthersupportedbystudiessuchasthoseby[33,34],whichillustratedhowpastlosses
couldtriggerheightenedrisk-takingbehaviorsamonginvestors.
Demographicvariablessuchasage,income,education,andemploymentstatusalso
playacriticalroleininvestmentdecisions. Ref.[27]demonstratedthatyoungerinvestors
are more likely to engage in high-risk investments, whereas older individuals tend to
prioritizesafetyandstability. Similarly,Ref.[35]foundthatfinancialliteracylevelsand
demographiccharacteristicsjointlyinfluenceinvestmentpreferences,withhigher-income
individualsdemonstratingagreaterpropensityfordiversifiedportfolios. Studiesby[36,37]
furtherconfirmedtheimportanceofdemographicfactorsinshapingfinancialbehaviors,
notingsignificantvariationsbasedongender,income,andeducationalattainment.
Strategicdecision-makingprocessesininvestmentareofteninfluencedbyexternal
andcontextualfactors. Ref.[38]arguedthataligninginvestmentswithbroaderstrategic
goalsenhancestheirperceivedvalue,particularlyinenergyefficiencyinitiatives. Ref.[39]
emphasized the role of contextual factors such as market competition and regulatory
frameworks in shaping strategic investment decisions. Ref. [40] extended this analysis
to cross-border investments, highlighting the impact of finance-specific factors such as
currencystabilityandfinancialintegration.
Recentadvancementsintechnology,particularlyinartificialintelligence(AI),have
transformedthelandscapeofinvestmentdecisionmaking. TrustinAI-enabledfinancial
systemsisemergingasacriticalfactorinshapinginvestorbehavior. Studiesby[20,41]
revealedthatperceptionsofreliabilityandtransparencysignificantlyinfluencetheadoption
ofAI-basedtools.
Financialliteracyandbehavioralbiasesremainpivotalinbothindividualandinsti-
tutionalcontexts,whilestrategicandtechnologicalconsiderationsincreasinglyinfluence
moderninvestmentlandscapes.
Thus,thereviewedliteraturesupportstherelevanceofintegratingbehavioral,demo-
graphic,andeducationalvariablesinunderstandinginvestmentdecisions. Thisliterature
reviewinformedtheconstructionofthesurveyinstrumentsusedinthisstudy. Eachbehav-
ioraldimensionanalyzed—suchasinvestmentattitudes,speculativebehaviors,resilience
afterlosses,andtrustinAI—wasderivedfromconstructsidentifiedasinfluentialinprior
studies. Thisconnectionbetweentheoreticalbackgroundandempiricalinstrumentation
ensuresthestudy’sconceptualcoherence. Empiricalstudieshaveshownthatfinancialedu-
cationsignificantlyshapesinvestmentattitudesandlong-termfinancialdecision-making
behavior. Forexample,Becchettietal.[10]demonstratedthrougharandomizedcontrolled
trial how educational interventions can positively influence students’ financial choices
andattitudestowardinvesting. Thesefindingsreinforcethebehavioralunderpinningsof
investmentinterest,supportingtheintegrationofcognitiveandattitudinalvariablesin
predictivemodeling.
Recentstudieshavedemonstratedtheutilityofdecisiontree-basedmodelsinfinan-
cialbehaviorprediction. Forexample,Sunandcollaboratorsdevelopedadecisiontree
ensemblemethodcombiningSMOTEandbaggingtoaddressclassimbalanceinenterprise
creditevaluation,demonstratingimprovedpredictiveaccuracyandrobustnessincomplex
financialcontexts[22]. Thisapproachunderscorestherelevanceandadaptabilityoftree-
basedalgorithmsinmodelinginvestorbehaviorswheredataimbalanceandnon-linear
interactionsareprevalent.

Electronics2025,14,1505 5of17
2. MaterialsandMethods
2.1. Participants
Thisstudyutilizedaconveniencesamplingmethod,targetingnetworksofeconomists
andfinancialprofessionals. Recruitmentwasconductedprimarilythroughonlineplat-
forms,withaGoogleFormsquestionnairedistributedviaemailandprofessionalsocial
media channels. Participation was voluntary, and all respondents provided informed
consentpriortocompletingthesurvey. Datacollectionwasanonymous,ensuringconfi-
dentialitythroughouttheprocess.
Participantswererecruitedfromprofessionalnetworksandacademicassociations
relatedtoeconomicsandfinance. Eligibilityrequiredabasiclevelofinvestmentexperience
and understanding, ensuring respondents could meaningfully answer questions about
financial behaviors. Prior to survey distribution, an expert panel of three specialists in
behavioralfinanceandpsychometricsreviewedtheitempooltoensureclarity,relevance,
andcontentvalidity. Itemswereadaptedfromvalidatedinstrumentsandrevisedthrough
cognitiveinterviewswithfivepilotparticipants. Thesestepsenhancedthecredibilityand
replicabilityoftheresearchprocess.
A total of 548 participants completed the survey. Regarding gender distribution,
38%ofrespondentsidentifiedasmale(n=208),while62%identifiedasfemale(n=340).
In terms of education level, 21.4% (n = 117) reported having completed high school or
equivalent,40.9%(n=224)heldabachelor’sdegree,31.9%(n=175)hadamaster’sdegree,
and5.8%(n=32)reportedholdingadoctoraldegree.
Participants’ employment status was categorized into four groups: 11.7% (n = 64)
reportedbeingunemployed,4%(n=22)wereemployedpart-time,75%(n=411)were
employedfull-time,and9.3%(n=51)identifiedasfreelancersorself-employed. Income
levelsvaried,with19.3%(n=106)reportingamonthlyincomebelow3000RON,35.6%
(n=195) earning between 3000–5000 RON, 20.1% (n = 110) earning between 5000 and
7000RON,8.9%(n=49)earningbetween7000and9000RON,and16.1%(n=88)earning
above9000RONpermonth.
Participants’ professional experience was distributed as follows: 31.4% (n = 172)
reported less than five years of experience, 33.4% (n = 183) had between five and ten
years,11.5%(n=63)hadtentofifteenyears,and23.7%(n=130)hadoverfifteenyearsof
professionalexperience.
Thisdiversesampleprovidedarobustfoundationforexploringfinancialbehaviors
andattitudesacrossvariousdemographicandprofessionalcontexts. Whileconvenience
samplingallowedrapidaccesstoaspecificprofessionalpopulation,itintroducedpotential
selectionbiasandlimitedthegeneralizabilityofthefindings. Futureresearchshouldaim
forstratifiedorrandomsamplingtoimproverepresentativeness.
Therecruitmentprocessinvolveddistributingthesurveytoover1000individuals
via professional mailing lists, university alumni databases, and finance-related online
communities. From these, 548 responses were received and retained for analysis. The
exclusioncriteriaincludedincompleteresponses.
2.2. Instruments
Toanalyzethefactorsinfluencingfinancialdecisionmaking,asetofrigorouslydevel-
opedscaleswasutilized,eachcomprising7to14items. Theseinstrumentsweredesigned
tomeasurebehavioral,attitudinal,andcognitivedimensionscriticaltoinvestment-related
choices. Thescalesdemonstratedstrongreliability,withCronbach’salphavaluesranging
from0.84to0.93.
Thequestionnaireconsistedof8distinctscalescoveringbehavioral,attitudinal,cogni-
tive,technological,anddemographicdimensions. Eachscaleuseda5-pointLikert-type

Electronics2025,14,1505 6of17
responseformat,rangingfrom1(stronglydisagree)to5(stronglyagree). Higherscores
reflectedstrongeragreementwiththeconstructbeingmeasured.
Investmentinterestcapturedthelevelofengagementindividualsdisplayedtowardfi-
nancialinvestments,encompassingactivitieslikeseekinginformationandstayingupdated
on market trends. For instance, participants responded to items such as the following:
“Howoftendoyouseekinformationaboutfinancialinvestments?”,adaptedfrom[42]. The
scaledisplayedaCronbach’salphaof0.86,reflectinghighinternalconsistency.
Investmentattitudesmeasuredbeliefsaboutthebenefits,risks,andoverallsignifi-
canceofinvesting. Thisconstructwasvitalforunderstandinghowperceptionsinfluence
financialbehavior. Anexampleitemread,“Investingisessentialforlong-termfinancial
security.”,adaptedfrom[43]. ThisscaleachievedaCronbach’salphaof0.91,underscoring
itsreliability.
Financialeducationevaluatedparticipants’understandingoffoundationalfinancial
principles,suchassaving,budgeting,andinvestmentstrategies,andtheirabilitytoapply
thisknowledgeeffectively. Arepresentativeitemwasthefollowing: “Iunderstandthe
conceptofcompoundinterestanditsimpactonsavings.”(adaptedfrom[28]). Thescale
recordedaCronbach’salphaof0.89,indicatingrobustreliability.
Speculativeinvestmentattitudesexaminedindividuals’perceptionsofandengage-
mentwithspeculativeinvestmentoptions,includinghigh-riskassetslikecrypto-currencies.
This construct shed light on risk tolerance and preferences. An example item included
the following: “Speculative investments are a viable way to achieve financial growth.”
(adaptedfrom[4]). ThescaledemonstratedaCronbach’salphaof0.87.
Resilience after financial losses assessed an individual’s emotional and behavioral
recoveryfollowingfinancialsetbacks,reflectingtheirabilitytoregainconfidenceinfuture
investments. One item stated, “I view financial losses as an opportunity to learn and
improvemystrategies.”(adaptedfrom[3]). ThisscalehadaCronbach’salphaof0.84.
Decisionadaptabilityafterlossesmeasuredtheflexibilityindecision-makingstrategies
postloss,capturinghowindividualsrecalibratedtheirapproachtoinvesting. Asample
itemwasthefollowing:“Afterafinancialloss,Ireconsidermyinvestmentstrategytoavoid
repeatingmistakes.”ThescaleyieldedaCronbach’salphaof0.88.
Decision-makingbehaviorsininvestmentsevaluatedthesystematicanddeliberate
approachesindividualsusedwhenmakinginvestmentdecisions,suchasportfoliodiversi-
ficationandrelianceonexpertadvice. Anillustrativeitemwasthefollowing: “Idiversify
myin-vestmentportfoliotomanageriskeffectively.”,adaptedfrom[44]. Thisscalehadthe
highestCronbach’salphaat0.93.
TrustinAI-basedfinancialsystemsexploredconfidenceinautomatedtoolsandsys-
tems using artificial intelligence for financial management. This construct focused on
perceptionsoftechnology’sreliabilityandutility. Arepresentativeitemwasthefollow-
ing: “ItrustAI-basedsystemstoprovideaccuratefinancialrecommendations.”,adapted
from[45]. ThescaleachievedaCronbach’salphaof0.92,confirmingitsreliability.
2.3. Procedure
Theanalysisaimedtoinvestigatethefactorsinfluencinginvestmentinterest,which
wasdesignatedasthedependentvariable. Thepredictorsincludedbehavioral,attitudinal,
anddemographicfactors: investmentattitudes,financialeducation,speculativeinvestment
attitudes,resilienceafterfinanciallosses,decisionadaptabilityafterlosses,decision-making
behaviorsininvestments,trustinAI-basedfinancialsystems,anddemographicvariables
suchasage,gender,education,income,andemploymentstatus.
Thefulllistoffactorsincludedinthemodelisthefollowing:

Electronics2025,14,1505 7of17
• Behavioral/Attitudinal: Investmentattitudes, speculativeinvestmentattitudes,re-
silienceafterfinanciallosses,decision-makingbehaviorsininvestments,anddecision
adaptabilityafterlosses;
• Cognitive: Financialeducation;
• Technological: TrustinAI-basedfinancialsystems;
• Demographic: Age,gender,education,income,employmentstatus,andprofessional
experience.
ThedatawerecollectedviaanonlinequestionnaireandprocessedinJASP(version
0.19.3),anopen-sourcestatisticalsoftware. JASPwaschosenforitseaseofuse,accessibility,
andvisualinterpretabilityoftreestructures,whichalignswiththestudy’sappliedfocus.
However,futurestudiescouldreplicatetheanalysisinPython(scikit-learnversion1.4.1)or
R(rpart,version4.1.23)toallowgreatercontrolovermodeltuningandensemblemethods.
Preliminaryanalysesincludeddescriptivestatisticsandfrequencytablestosummarize
participant characteristics. To model the relationships between the dependent variable
andpredictors,decisiontreeregressionwasemployed. Thismethodwasselectedforits
abilitytohandlecomplex,non-linearrelationshipsandprovideinterpretablehierarchical
structuresintheformofdecisiontrees.
Decision tree regression was trained and tested on the dataset, using a default
80/20split for training and validation purposes. Model evaluation metrics, including
meanabsoluteerror(MAE),meanabsolutepercentageerror(MAPE),andR2,werecal-
culated to assess predictive performance. Given the 5-point Likert scale used for the
dependentvariable,MAPEandR2wereprioritizedasthemostinterpretableperformance
metrics. Featureimportancevalueswerecomputedtodeterminetherelativecontribution
ofeachpredictortothemodel. Hyperparameterssuchasthetree’smaximumdepthand
minimumsamplespersplitweresettodefaultinJASP.Whilethiswasasimplifiedinter-
pretation,itmighthaveincreasedtheriskofoverfittingorunderfitting. Agridsearchor
cross-validationapproachcouldfurtheroptimizeperformanceinfuturestudies.
3. Results
Decisiontreeregressionisanon-parametricsupervisedlearningmethodthatsplits
databasedoninputvariablevaluestopredictcontinuousoutcomes. Thealgorithmre-
cursivelypartitionsthedatasetbyselectingsplitsthatminimizethemeansquarederror
ateachnode. Thisstructurerevealsthehierarchicalimportanceandinteractionsamong
predictors,offeringinterpretableinsightsintocomplexbehavioralpatterns.
Theresultsofthedecisiontreeregressionmodelprovideinsightsintothepredictorsof
investmentinterest. Themodelwastrainedon439casesandtestedon109cases,achieving
a test mean squared error (MSE) of 1.065, a root mean squared error (RMSE) of 1.032,
a mean absolute error (MAE) of 0.8, and a mean absolute percentage error (MAPE) of
172.96%. TheR2valueof0.185indicatedamodestproportionofvarianceintheinvestment
interest explained by the predictors. The dependent variable (investment interest) was
measuredona5-pointLikertscale. Giventhislimitedscalerange,therelativelylowR2
(0.185)andhighMAPEreflectedthecomplex,subjectivenatureofinvestmentinterestand
theinfluenceofunmeasuredlatentvariables. Thegoalofthismodelwas,therefore,not
precisionforecastingbutexploratorypatternrecognitionandpredictorranking. Thus,the
relativelylowR2valuesuggestedthat,whilethemodelcapturedmeaningfulpredictors,
otherlatentorcontextualfactorslikelycontributedtoinvestmentinterest. Thisreflects
theinherentcomplexityoffinancialbehavior,whichisofteninfluencedbynon-observable
psychologicalorsituationalvariables.
Therelativeimportanceofpredictors(Table1)revealedthatinvestmentattitudeswere
themostinfluentialfactor,contributing25.88%tothemodel.Thiswasfollowedbydecision-

Electronics2025,14,1505
8of17
makingbehaviorsininvestments(19.53%)andfinancialeducation(16.69%),highlighting
thesignificantroleofbehavioralandeducationaldimensionsinshapinginvestmentinterest.
Otherimportantpredictorsincludedspeculativeinvestmentattitudes(11.20%),decision
adaptabilityafterlosses(8.27%),andtrustinAI-basedfinancialsystems(6.78%).
Demographicvariablessuchasage(1.94%),experience(1.50%),income(1.09%),edu-
cation(0.39%),andemploymentstatus(0.28%)exhibitedcomparativelylowerim-portance,
suggestingalesserdirectimpactoninvestmentinterestcomparedtobehavioralandattitu-
dinalfactors.
Table1.Featureimportance.
RelativeImportance
Investmentattitudes 25.883
Decision-makingbehaviorsininvestments 19.534
Financialeducation 16.686
Speculativeinvestmentattitudes 11.195
Decisionadaptabilityafterlosses 8.273
TrustinAI-basedfinancialsystems 6.775
Resilienceafterfinanciallosses 6.439
Age 1.940
Experience 1.503
Income 1.094
Education 0.394
Status 0.283
Theprominenceofinvestmentattitudesasthetoppredictorsuggestsastrongpsy-
chologicalbasisforfinancialengagement. Individualswithpositiveattitudesaremore
proactiveinseekingfinancialopportunitiesandshowgreateropennesstousingAI-based
investmenttools,especiallywhentrustintechnologyispresent.
Decisiontreeregressionrevealedahierarchicalstructureofpredictors,withthemost
significantsplitsoccurringatvariouslevelsofthetree(Table2).
Table2.Splitsintree.
|                     | Obs. inSplit | SplitPoint | Improvement |
| ------------------- | ------------ | ---------- | ----------- |
| Investmentattitudes | 439          | −0.411     | 0.160       |
−2.020
| Investmentattitudes                   | 142 |        | 0.191 |
| ------------------------------------- | --- | ------ | ----- |
| Speculativeinvestmentattitudes        | 132 | −0.249 | 0.165 |
| Experience                            | 73  | 1.072  | 0.122 |
| Decision-makingbehaviorsininvestments | 48  | −0.240 | 0.231 |
| Decision-makingbehaviorsininvestments | 25  | −0.392 | 0.314 |
| Financialeducation                    | 297 | 1.858  | 0.136 |
| Decision-makingbehaviorsininvestments | 282 | −0.392 | 0.113 |
| Resilienceafterfinanciallosses        | 75  | 0.267  | 0.102 |
| Speculativeinvestmentattitudes        | 22  | −0.249 | 0.286 |
| Financialeducation                    | 207 | 0.373  | 0.062 |
−0.811
| Resilienceafterfinanciallosses  | 100 |        | 0.112 |
| ------------------------------- | --- | ------ | ----- |
| TrustinAI-basedfinancialsystems | 89  | −0.215 | 0.124 |
| TrustinAI-basedfinancialsystems | 27  | −0.568 | 0.337 |
Note.Foreachlevelofthetree,onlythesplitwiththehighestimprovementindevianceisshown.
Table2presentsthemostrelevantdecisiontreesplits,where“Obs. inSplit”indicates
the number of observations at the node being split, “Split Point” represents the value
of the predictor at which the split occurs, and “Improvement” reflects the reduction in

Electronics 2025, 14, x FOR PEER REVIEW 9 of 17
Electronics2025,14,1505 Table 2 presents the most relevant decision tree splits, where “Obs. in Split” indi 9 c o a f t 1 e 7 s
the number of observations at the node being split, “Split Point” represents the value of
the predictor at which the split occurs, and “Improvement” reflects the reduction in model
mdeovdiealndceev (iaa npcreox(ay pforor xpyrefodricptiroend iecrtiroonr)e; rhriogrh);ehr iigmhperroimvepmroevnetm vaenlutevsa ilnudesiciantde isctartoensgtreorn pgreer-
pdriecdtiivceti vcoenctornibturitbiounti oant tahtatth saptescpifiecci filecvleelv oefl tohfet htreeter.e e.
TThhee fifirrsstts pspliltitw wasasb absaesdedon oinn vinesvtemstemnteanttt iatuttditeusd,ewsh, iwchhiecmh eermgeedrgaesdth aesm thoes tminoflsut einnfltiual-
veanrtiiaabl lvea.rAiatbales. pAlitt ap sopinlitt pofoi−n0t .o4f1 −10,.t4h1i1s, ftahcitso frapctroorv pidreodviadnedim anp riomvpermoevnemtoefn0t .o16f 00.i1n60th ien
mthoed melo,demel,p ehmaspizhiansgiziitnsgfo iutsn fdoautniodnaatlioronlael irnolper eind ipcrtiendgicitninvges itnmveensttminetnert eisntt.eAressut. bAse squubesnet-
sqpuleitnwt sitphliint wthiethsianm theev saarmiabe lve,aarita−bl2e.,0 a2t0 −,2y.i0e2ld0,e dyiaelndeevde anng erveaetne rgrimeapterro vimempreonvteomfe0n.1t9 o1f,
f0u.1rt9h1e, rfuhrigthhelrig hhitginhgligithsticnegn tirtas lciemnptroarl tiamncpeo.rtance.
TThhee nneexxtt ccrriittiiccaall sspplliitt iinnvvoollvveedds sppeeccuulalattiviveei ninvveesstmtmeenntta attttitiutuddeess,,o occccuurrrirningga att− −00..224499
aanndd ccoonntrtribibuutitningga nanim imprporvoevmemenetnotf o0f. 106.51.6T5.h iTshiinsd iincadtiecsattehsa tthinadt iivniddiuvaildsu’palesr’c eppetricoenpstiaonnds
eanngda genemgaegnetmweintht wspiethcu slpaeticvuelaintivvees timnveensttsmaernetasl saorek aeylsod rkiveyer dsroifvtehrse iorfi nthteeriers itnitnerfiensat ninc iafil-
innavnecsitaml iennvtes.stAmneontthse. rAsnigonthifierc asnigtnsipfilciatnwt asspolibt swearvs eodbsweritvhedex wpietrhi eenxcpee,raietnacpe,o aint tao pfo1i.n0t7 o2f,
w1.h0i7c2h, wprhoivcihd epdroavnidimedp aronv iemmpernotvoefm0e.1n2t2 o,fs u0.g1g2e2s, tsinugggthesattinpgro tfheasst ipornoafleesxsipoenraiel necxepperlaieynscae
spulpaypso art isvuepbpuotrtsievceo bnudta sreycroonledainrys hroalpei ning sihnavpesintmg einnvtebsethmaevniot rb.ehavior.
DDeecciissiioonn--mmaakkiinngg bbeehhaavviioorrss iinn iinnvveessttmmeennttss aallssoo aappppeeaarreedd pprroommiinneennttllyy iinn tthhee ttrreeee
ssttrruuccttuurree,, wwiitthh sspplliittss aatt− −00..224400 aanndd −−00..339922,, pprroovviiddiinngg iimmpprroovveemmeennttss ooff 00..223311 aanndd 00..331144,,
rreessppeeccttiivveellyy..T Thheesesefi finnddinignsgsu nudnedresrcsocroerteh tehiem ipmoprtoarntacencoef soyf sstyemsteamticaatincd adnedl idbeelriabteeriantve eisnt--
mveesntmtpernatc tpircaecst.iSceims. iSlaimrlyil,afirnlya,n ficniaalnecdiaulc eadtiuocnatsipolnit sspaltitpso aitn tpsosiunctsh sausc1h. 8a5s8 1a.8n5d8 0a.n37d3 0c.3o7n3-
tcroibnutrteibduitmedp riomvpermoevnetmseonft0s. 1o3f6 0a.1n3d6 0a.n06d2 0,.i0n6d2i,c aintidnigcathtiantgfi tnhaant cfiianlaknncoiawl lkendogwelseigdngiefi sciagnntilfy-
cicoamnptllye mcoemntpsleomtheenrtbse ohtahveiro braelhfaavcitoorrasl. factors.
OOtthheerr pprreeddicictotorrss,,s suucchha assr erseisliileinecnecea fateftrefir nfiannacniaclialol slosessseasn adntdru tsrtuisnt AinI -AbIa-sbeadsefidn afinncaianl-
scyiastl esmyss,tesmhosw, eshdoiwnfleude nincfleuinenlocwe einr- lleovwelesrp-lleitvse,lw sipthlitrse,s pweictthiv reeismpepcrtoivveem imenptsroovfe0m.1e1n2tasn odf
00..112142. aTnhde i0r.r1o2l4e.s T,thheoiru grohleless, sthporuomghi nleesnst ,psruogmgeinsetendt, nsuuagngceesdtecdo nnutraibnucetido ncsontotrtihbuetoiovnersa tlol
mthoed oevl.eNraollt ambolyd,eal.s Nploittainbltyr,u as tsipnliAt iIn-b tarsuesdt fiinn AanIc-biaalsseyds tfienmanscaita − l s0y.5st6e8mlesd att o−0th.5e6h8 ilgehde stot
itmhep rhoivgehmesetn itmaptrthoviselmeveenlt, wati tthhias vleavlueel, owfi0t.h3 3a7 ,vhailguhel iogfh 0ti.3n3g7t,h heigemhleigrghitninggs itghnei fiemcaenrcgeinogf
tseicghnnifiocloagniccea lotfr tuescthinnofilongainccaila tlrcuosnt tienx fitsn.ancial contexts.
OOvveerraallll,, tthhee ttrreeee ssttrruuccttuurree hhiigghhlliigghhttss tthhee ddoommiinnaanntt rroollee ooff bbeehhaavviioorraall aanndd aattttiittuuddiinnaall
ffaaccttoorrss,, wwiitthh ddeemmooggrraapphhiicc vvaarriiaabblleess ccoonnttrriibbuuttiinngg mmoorree ssuubbttllyy ttoo tthhee pprreeddiiccttiioonn ooff iinnvveesstt--
mmeenntt iinntteerreesstt.. TThheesseer reessuultlstso offffeerra ac ocommpprerhehenesnisvievev iveiwewo fohf ohwowd idffieffreernetnptr pedreicdtiocrtsorins tienrtaecrt-
aancdt acnodn tcroibnutrtiebhuiteer hariecrhaicrcahlliycatollyfi ntoa nficniaanlcdieacl idsieocnismioank minagk(iFnigg u(Frieg1u)r.e 1).
Figure1.Predictiveperformanceplot.
Figure 1. Predictive performance plot.
Figure1illustratesthepredictiveperformanceofthedecisiontreeregressionmodel,
visualizing the relationship between observed and predicted values of the dependent
variable, investmentinterest. Theplotprovidesanassessmentofthemodel’sabilityto
accuratelypredictthelevelsofinvestmentinterestbasedontheidentifiedpredictors.

Electronics 2025, 14, x FOR PEER REVIEW 10 of 17
Figure 1 illustrates the predictive performance of the decision tree regression model,
visualizing the relationship between observed and predicted values of the dependent var-
iable, investment interest. The plot provides an assessment of the model’s ability to accu-
rately predict the levels of investment interest based on the identified predictors.
Electronics2025,14,1505 10of17
The scatterplot reveals a clustering of points around the diagonal line, which repre-
sents perfect prediction. While there is some dispersion, particularly at extreme values,
Thescatterplotrevealsaclusteringofpointsaroundthediagonalline,whichrepresents
the general alignment of data points with the diagonal indicates that the model captures
perfect prediction. While there is some dispersion, particularly at extreme values, the
the overall trend effectively. This is consistent with the model’s performance metrics, in-
generalalignmentofdatapointswiththediagonalindicatesthatthemodelcapturesthe
cluding a test mean squared error (MSE) of 1.065 and a root mean squared error (RMSE)
overalltrendeffectively. Thisisconsistentwiththemodel’sperformancemetrics,including
of 1.032, which reflect a reasonable level of predictive accuracy. However, the modest R2
atestmeansquarederror(MSE)of1.065andarootmeansquarederror(RMSE)of1.032,
va
w
lu
h
e
i c
o
h
f 0
re
.1 fl
8
e
5
c t
su
a
g
re
g
a
e
s
s
o
ts
n a
th
bl
a
e
t,
l e
w
v
h
el
il
o
e
f
th
p
e
re
m
di
o
ct
d
iv
e
e
l i
a
d
c
e
c
n
u
t
r
i
a
fi
c
e
y
s
.
k
H
e
o
y
w
p
e
r
v
e
e
d
r,
ic
t
t
h
o
e
rs
m
, a
o
d
de
d
s
i
t
ti
R
o2na
v
l
a
u
lu
n
e
meas-
ured factors may contribute to unexplained variance.
of0.185suggeststhat,whilethemodelidentifieskeypredictors,additionalunmeasured
facTtohres mdeacyiscioonnt rtirbeuet eptlootu (nFeixgpulraein 2e)d ilvlaursitarnactee.s the hierarchical structure of the regression
model Tuhseedd etcoi spiornedtriecet pinlovte(sFtimguernet2 i)niltleursetsrat,t ehsigthhelihgihertainrcgh itchael ssteruqcuteunretioafl tihmepreogrrteasnsicoen of the
premdoicdteolruss. eTdhteo rporoedt incotidnev eidstemnetinfiteins tienrvesets,thmigehnltig ahtttiintugdthees saesq tuheen tmiaolsimt spiogrntaifinccaenotf vthaeriable,
splpirtteidnigct othrse. dThaetarsoeott anto ad eviadleunet iofife s−0in.4v1e1st.m Tehnits actotintufidremssa sththaet minovsetsstimgneinfitc aantttivtuardiaebs lae,re the
splittingthedatasetatavalueof−0.411. Thisconfirmsthatinvestmentattitudesarethe
strongest driver of investment interest, as indicated in the feature importance analysis.
strongest driver of investment interest, as indicated in the feature importance analysis.
For individuals with lower investment attitudes (<−0.411), further splits occur at −2.02
Forindividualswithlowerinvestmentattitudes(<−0.411),furthersplitsoccurat−2.02
within the same variable, underscoring its critical role. Subsequent splits in this branch
withinthesamevariable,underscoringitscriticalrole. Subsequentsplitsinthisbranchare
are determined by speculative investment attitudes (<−0.249), followed by experience
determinedbyspeculativeinvestmentattitudes(<−0.249),followedbyexperience(<1.07)
(<1.07) and decision-making behaviors in investments, which refine the prediction for in-
anddecision-makingbehaviorsininvestments,whichrefinethepredictionforindividuals
divwidithuanlesg watiitvhe noregloawtivaett iotur dloeswto awttaitruddinevs etsotwmeanrdts .investments.
FigFuigreu r2e. 2D.eDceicsiisoinon trtereee pplloott..
Forindividualswithhigherinvestmentattitudes(≥−0.411),thenextsignificantsplit
For individuals with higher investment attitudes (≥−0.411), the next significant split
isbasedonfinancialeducation(<1.86),demonstratingtheroleoffinancialknowledgein
is based on financial education (<1.86), demonstrating the role of financial knowledge in
distinguishinglevelsofinvestmentinterestamongthisgroup. Thetreefurtherbranches
distinguishing levels of investment interest among this group. The tree further branches
onvariablessuchasdecision-makingbehaviorsininvestments(<−0.392),resilienceafter
on
fi
v
n
a
a
r
n
i
c
a
i
b
a
l
l
e
l
s
o s
s
s
u
es
ch
(<
a
0
s
.2 d
67
e
)
c
,
i
a
s
n
io
d
n
s
-
p
m
ec
a
u
k
l
i
a
n
t
g
iv e
be
in
h
v
a
e
v
s
i
t
o
m
r
e
s
n
i
t
n
a t
in
tit
v
u
e
d
s
e
tm
s(
e
<
n−t
0
s
.2 (<
4
−
9)
0
.
.3 D
9
e
2
e
)
p
,
e
r
r
e
s
s
p
il
l
i
i
e
ts
n
i
c
n
e after
fintahnecriiaglh ltossusbetsr e(e<0a.l2so67in),c laundde strpuesctuinlaAtiIv-bea isnevdefisntmanecniat lasttysittuemdes,s r(e<fl−e0c.t2in4g9)t.h Deeemepeergr inspglits in
ther erliegvhatn cseuboftrteeech anlosloo giniccallutdrues ttriunsfit ninan AciIa-lbdaesceidsi ofinn-manackiianlg scyosntetemxtss,. reflecting the emerging
relevanTchee otfe rtmecihnnalonloodgeicsarle tprruesset nint pfirnedainccteiadl ldeveeclissioofnin-mveasktminegn tcionnteterexstts,.w itheachnode
displayingthepredictedscoreandthenumberofobservations(n)inthatsubset. These

Electronics2025,14,1505 11of17
terminal nodes provide insights into the segmentation of participants based on their
characteristicsandpredictors. Thetreedemonstratesthatinvestmentattitudesplayafoun-
dationalrole,withvariablessuchasfinancialeducation,speculativeinvestmentattitudes,
anddecision-makingbehaviorsactingascriticalsecondaryinfluences. Otherfactors,like
resilienceafterfinanciallossesandtrustinAI-basedfinancialsystems,contributemore
nuancedeffectsatdeeperlevelsofthetree.
Althoughthefulldecisiontreeincludesmultiplelevelsofsplits,thisdepthreflects
thecomplexityofinteractionsamongbehavioralanddemographicpredictors. Thedeeper
branchescapturecomplexdecisionpathwaysthatmayapplytospecificinvestorprofiles,
whiletheupperlevelshighlightthemostinfluentialvariablesoverall. Thisstructureallows
forbothgeneralanddetailedinterpretationofinvestmentinterestsegmentation.
4. Discussion
The findings of this study highlight the complex nature of investment decisions,
underscoringtheinterplaybetweenbehavioral,financial,demographic,andtechnological
factors.Theseresultsalignwithandexpandupontheexistingliterature,offeringsignificant
implicationsforinvestors,policymakers,andfinancialinstitutions.
Thedominanceofbehavioralfactors,suchasinvestmentattitudes,decision-making
behaviors,andspeculativeinvestmentattitudes,reflectsthecriticalroleofpsychologyin
financialdecisionmaking. Behavioralbiases,suchasoverconfidenceandlossaversion,
influencehowindividualsperceiveandrespondtoinvestmentopportunities,assupported
by[46]. Thesefindingsareconsistentwithbehavioralfinancetheory[1,6],whichposits
thatpsychologicalinfluencesoftenoverriderationalfinancialanalysis. Theresultsalso
highlight generational differences, as younger investors, particularly from Generation
Y,exhibithigherengagementinspeculativeinvestments[46]. Thishasimplicationsfor
financial education programs tailored to specific demographic groups, as emphasized
by[35,47].
Theobservedinfluenceofdemographicfactors,suchasincome,education,andem-
ploymentstatus,corroboratesearlierstudiesthatemphasizetheirimportanceinshaping
investment preferences. For instance, Refs. [48,49] highlight how macroeconomic and
socio-economicfactorsinfluenceindividualinvestmentbehaviorindevelopingeconomies.
Furthermore,theinterplaybetweenfinancialliteracyanddemographicvariables,asdemon-
stratedby[10,11],underscorestheneedfortargetedfinancialliteracyinitiativestobridge
gapsininvestmentknowledgeandparticipation.
Thefindingsdemonstratetheimportanceoffinancialeducationinfosteringinformed
investment decisions, aligning with studies by [28,50]. Financially educated individu-
als are better equipped to evaluate risks and returns, enhancing their decision-making
processes. These results hold strategic implications for policymakers and educational
institutions, particularly in designing programs to enhance financial literacy. Ref. [47]
emphasizesthatfinancialliteracyindevelopingeconomiesiscriticaltoimprovinginvest-
mentoutcomes,whichisespeciallypertinentforemergingmarketslikePakistanandother
developingregions.
Theroleofstrategicinvestmentdecisionmaking,ashighlightedinthisstudy,aligns
withfindingsfrom[51,52],underscoringtheimportanceofnon-financialdriversinstrategic
contexts,suchasrenewableenergyandnuclearsectors. Theseinsightsextendtoindividual
investors,wherealignmentwithlong-termstrategicgoalscanimprovedecisionoutcomes.
Additionally,thisstudyconfirmstherelevanceofcontextualfactorsinshapinginvestment
behavior,consistentwithfindingsby[53]onrealestateinvestmentsand[54]onforeign
directinvestment. Advancedanalyticalmethods,suchasfuzzyclusteringanddecisiontree
modeling,havebeenshowntoprovidevaluableinsightsintocomplexdecision-makingpro-

Electronics2025,14,1505 12of17
cesses,highlightingtheirpotentialapplicationinunderstandingfinancialbehaviors[55,56].
Recentadvancementsinmachinelearninganddecisiontreemethodologies,suchassplit
differenceweightingandself-awarepredictionmodels,offerpromisingsolutionsforad-
dressingimbalancesandimprovinginvestmentrecommendations[57,58]. Also,techniques
suchasfuzzy-payoffmethodsandmulti-perioddecisiontreeshavedemonstratedsignifi-
cantutilityinevaluatingsustainableinvestmentopportunities,bridgingbehavioraland
strategicconsiderations[56,59].
ThegrowingsignificanceoftrustinAI-basedfinancialsystemsobservedinthisstudy
reflects the increasing reliance on technology for investment decision making. These
findings are consistent with the recent literature, such as [20], highlighting the role of
transparency and reliability in fostering trust in AI systems. As financial technologies
continue to evolve, financial institutions must prioritize user trust through transparent
anduser-friendlyAIsolutions. Thisisparticularlyimportantinthepost-pandemicera,
wheredigitalsolutionsarereshapingtraditionalinvestmentprocesses[53]. Theadoption
ofadvancedclusteringanalysesinmanagementandaccountingpracticesfurtherillustrates
thepotentialforenhancinginvestorprofilingandservicecustomization[60].
Theseinsightsarevaluableforfinancialadvisorsseekingtopersonalizeinvestmentrec-
ommendations. Behavioralsegmentationmodelscanhelpfinancialserviceprovidersadapt
theirapproachestorisk-tolerantversusrisk-averseclients. Moreover,educationprograms
shouldprioritizenotonlygeneralfinancialliteracybutalsopsychologicalpreparedness
forspeculativeenvironments,helpingindividualsdevelopresilienceandadaptability. For
researchers,thehierarchicalmodelingprovidedbydecisiontreesoffersanalternativeto
linearapproaches,capturingnon-linearandinteractiveeffectsoftenmissedintraditional
econometricanalyses.
Comparedtotraditionallinearmodels,decisiontreeregressionoffersinterpretability
andnon-linearitybutmaylackrobustnessinhigh-dimensionaldata.Futureresearchshould
exploreensemblemodelslikerandomforestsorXGBoost,whichofferbettergeneralization.
Additionally,Bayesianordeeplearningmethodscouldprovidemorenuancedmodelingof
investoruncertainty.
The integration of AI and other digital tools in financial decision making presents
both opportunities and challenges. While AI-based systems can provide accurate and
data-driven insights, they must also address concerns about data security and ethical
decisionmaking,assuggestedby[41]. Thesefindingsunderscoretheneedforregulatory
frameworks to govern the use of AI in finance, ensuring both trust and accountability.
Additionally,theintegrationofemotionalandbehavioralinsightsintoAI-basedsystems,
such as those examining the role of trust and friendship in information-sharing behav-
iors[61],highlightstheimportanceofuser-centricapproachesinfosteringengagement
andtrustinfinancialtechnologies. TrustinAIisnotonlyaboutsystemperformancebut
alsoethicalandemotionalconsiderations. AsPelauandcollaboratorsnote,perceptionsof
“friendship”andemotionaltrustinAIsystemssignificantlyaffectinformation-sharingand
engagement[61]. FinancialAItoolsmustthereforeaddressemotionalUXdesignalongside
accuracy.
Theroleoftechnologicaladvancements,includingcloudcomputingservices[62]and
riskmanagementsystemsforsustainabledevelopment[63],furtherillustratesthetransfor-
mativepotentialofAIinaddressinginvestmentcomplexities. Similarly,considerationsof
cryptocurrency’simpactonaccountingpractices[64]andsustainability-focusedbusiness
models [65] underscore the need for aligning technological innovations with evolving
marketdemands.
Theresultsofthisstudyholdbroaderimplicationsforpolicymakersandpractitioners.
Fordevelopingeconomies,suchasthosediscussedby[48,66],improvingfinancialliteracy

Electronics2025,14,1505 13of17
and access to financial services can significantly enhance investment participation and
outcomes. Policymakersshouldconsiderimplementingtargetedinterventions,suchastax
incentivesforinvestmentinfinancialeducationprograms,toaddressgapsinliteracyand
participation.
Forfinancialinstitutions,understandingthebehavioralanddemographicnuancesof
investorscaninformthedesignofpersonalizedinvestmentproductsandadvisoryservices.
ByleveragingAIandbigdataanalytics,institutionscantailorsolutionstomeettheneedsof
diverseinvestorprofiles,ashighlightedby[20]. Furthermore,theintegrationofbehavioral
insightsintofinancialadvisoryservicescanimproveengagementanddecisionmaking,as
emphasizedby[52,67].
Policymakerscanapplythesefindingsbyintegratingbehavioralsegmentationinto
public financial literacy campaigns, tailoring messages to match investor profiles (e.g.,
speculativevs. risk-averse). FinancialinstitutionscanuseDTR-basedprofilestocustomize
robo-advisorysystemsandalignproductofferingswithbehavioralpredictors.
5. Conclusions
Futureresearchshouldexplorecomplementarymodelingapproachestodeepenthe
insights obtained from behavioral predictors. In particular, the analytic hierarchy pro-
cess(AHP)andfuzzylogicrepresentvaluablemethodsformulti-criteriadecisionmak-
ing under uncertainty. AHP facilitates pairwise comparisons and priority rankings of
investment-relatedcriteria,enablingresearcherstoassesstrade-offsbetweenrisk,return,
andpsychologicalcomfort[68]. Similarly,fuzzylogicmodelstheimprecisioninherentin
humanjudgment,capturingthedegreesofinvestorpreferencesandbeliefsinaflexible
manner[69]. Thesetechniqueswouldallowforamoresystematicevaluationofinvestor
decision patterns and could be used in combination with machine learning models for
enhancedhybridapproaches. Exploringthesemethodsmayalsoprovideastrongerfoun-
dationforpersonalizedfinancialadvisorytools.
Thisstudyprovidesexploratoryinsightsintothefactorsassociatedwithinvestment
interest,emphasizingthepotentialofintegratingbehavioral,educational,andtechnolog-
icalvariablesintopredictivemodelingframeworks. Theresultstentativelysuggestthat
behavioralfactors,particularlyinvestmentattitudesanddecision-makingbehaviors,may
playamorepronouncedrolecomparedtotraditionaldemographics,thoughfurthervali-
dationisneeded. Additionally,thisstudyhighlightsthegrowingsignificanceoffinancial
literacyandAI-driventechnologiesinshapinginvestmentstrategies,reinforcingtheneed
foradaptivefinancialeducationandpersonalizedadvisoryservices.
Althoughthisstudycontributedvaluableinsights,ithadseverallimitations. First,the
relianceonself-reporteddatamighthaveintroduceresponsebiases,namelysocialdesirabil-
ityorrecallbias,asindividuals’statedinvestmentbehaviorsmaynotfullyalignwiththeir
actualfinancialdecisions. Futurestudiesshouldconsiderintegratingobjectivefinancial
dataorexperimentalmethodologiestomitigatethislimitation. Second,thestudy’ssample
wasnon-randomand,thus,limitedinscope,potentiallyrestrictingthegeneralizabilityof
thefindingstootherregionsorinvestorgroups. Theuseofasinglepredictivealgorithm
mighthavealsoconstrainedthestudy’sbroaderapplicability. Expandingthedatasetto
includeamorediversepopulationacrossdifferenteconomicbackgroundsandinvestment
environmentswouldenhancetherobustnessoftheconclusions. Finally,whiledecision
treeregressionprovidedvaluableinsightsintopredictiverelationships,thisstudydoes
notaccountforpotentialinteractionsbetweenvariables. Futureresearchcouldemploy
ensemblemodelsordeeplearningtechniquestocapturemorecomplexdecision-making
patterns.

Electronics2025,14,1505 14of17
Theresultshavesignificantimplicationsforpolicymakers,financialinstitutions,and
investors. Forpolicymakers,thefindingsemphasizetheneedfortargetedfinancialliter-
acyprograms,particularlyforyoungerinvestorsandindividualswithlimitedfinancial
education. Governmentscouldimplementincentive-driveninitiativestopromotefinan-
cialawarenessandresponsibleinvestmentbehaviors. Financialinstitutions,ontheother
hand, should leverage behavioral insights to design personalized investment products
and AI-driven advisory services that account for cognitive biases and risk perceptions.
Theincreasingroleoftechnologyininvestmentdecisionssuggeststhatinstitutionsmust
prioritize transparency, trust, and ethical considerations in AI-powered financial tools.
Additionally,thisstudyreinforcestheimportanceofintegratingbehavioralfinanceprin-
ciplesintotraditionalinvestmentstrategies,offeringamorecomprehensiveapproachto
understandingmarketbehavior.
Additionalworkcouldtestensemblelearningmethodsorapplythecurrentmethodol-
ogyincross-culturalsettingstoexaminehowinvestmentpredictorsvaryacrosseconomic
systems. A hybrid approach that integrates behavioral scoring with machine learning
couldalsoenhancereal-timefinancialadvisingsystems. Futureresearchshouldexplore
thedynamicinterplaybetweenbehavioral,technological,andfinancialfactorsindiffer-
ent economic and cultural contexts. Specifically, longitudinal studies could provide a
deeperunderstandingofhowinvestorbehaviorsevolveovertimeinresponsetomarket
fluctuationsandfinancialeducationinitiatives. Additionally, examiningsector-specific
investmentbehaviors—suchasinsustainablefinance,cryptocurrency,orrealestate—could
offermoretailoredinsightsintodecision-makingprocesses. Furtherresearchshouldalso
investigate the ethical and regulatory challenges associated with AI-driven investment
platforms,particularlyinensuringfairness,privacy,anddatasecurity. Lastly,interdisci-
plinary approaches combining behavioral finance, machine learning, and neuroscience
couldprovidegroundbreakingperspectivesonhowemotionsandcognitivebiasesshape
financialdecisionmaking.
Building on these exploratory results, future research should adopt longitudinal
designs to track changes in investment behavior over time and across economic cycles.
Applyingmoreadvancedalgorithms—suchasrandomforests,gradientboosting,anddeep
learningnetworks—couldimprovepredictionaccuracy.Cross-nationalcomparisonswould
alsobevaluableinexamininghowculturalandinstitutionalcontextsshapeinvestment
attitudes. Lastly,integratingbehavioraldatawithrealfinancialbehavior(e.g.,transaction
records)couldenhancetheecologicalvalidityofpredictivemodels.
Inconclusion,thisstudyadvancesthefieldofinvestmentdecisionmakingbyintegrat-
ingmultipledimensionsoffinancialbehavior.Thefindingscallforamoreholisticapproach
toinvestmentstrategies,combiningbehavioralinsightswithtechnologicaladvancements
to enhance decision-making efficiency and financial well-being. Ongoing research and
innovationinfinancialliteracy,AI-drivenadvisorysystems,andregulatoryframeworks
willbecrucialinshapingthefutureofinvestmentpracticesinanincreasinglydigitaland
complexfinanciallandscape.
AuthorContributions:Conceptualization,D.R.,L.D.C.andG.C.;methodology,L.D.C.,B.C.G.,L.M.
andD.R.;software,D.R.,B.C.G.,S.R.andR.S.B.;validation,G.C.,S.R.andM.S.;formalanalysis,
L.D.C.,D.R.andF.S.B.;investigation,B.C.G.,S.R.andM.S.;resources,L.D.C.,L.M.andF.S.B.;data
curation,G.C.,R.S.B.andB.C.G.;writing—originaldraftpreparation,L.D.C.,D.R.andL.M.;writing—
reviewandediting,D.R.,G.C.andF.S.B.;visualization,G.C.,S.R.andR.S.B.;supervision,D.R.,L.D.C.
andG.C.;projectadministration,L.D.C.,D.R.andF.S.B.;andfundingacquisition,B.C.G.,S.R.and
F.S.B.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.

Electronics2025,14,1505 15of17
InstitutionalReviewBoardStatement:ThisstudywasconductedinaccordancewiththeDeclaration
ofHelsinkiandapprovedbytheCentreforEconomicResearchandConsultancyofAurelVlaicu
UniversityofArad(protocolcode15/5April2023).
InformedConsentStatement: Informedconsentwasobtainedfromallthesubjectsinvolvedin
thisstudy.
DataAvailabilityStatement:Thedatasupportingourfindingscanbeprovidedbythecorresponding
authoruponreasonablerequest.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Brooks,M.;Byrne,A.BehavioralFinance:TheoriesandEvidence;TheResearchFoundationofCFAInstitute:Charlottesville,VA,
USA;UniversityofEdinburgh:Edinburgh,UK,2008.
2. Fromlet,H.Behavioralfinance-theoryandpracticalapplication:Systematicanalysisofdeparturesfromthehomooeconomicus
paradigmareessentialforrealisticfinancialresearchandanalysis.Bus.Econ.2001,36,63–69.
3. Kahneman,D.;Tversky,A.Prospecttheory: Ananalysisofdecisionunderrisk. InHandbookoftheFundamentalsofFinancial
DecisionMaking:PartI;WorldScientific:Singapore,2013;pp.99–127.
4. Barberis,N.Thirtyyearsofprospecttheoryineconomics:Areviewandassessment.J.Econ.Perspect.2013,27,173–196.[CrossRef]
5. Ritter,J.R.Behavioralfinance.Pac.BasinFinanc.J.2003,11,429–437.[CrossRef]
6. Shiller,R.J.Fromefficientmarketstheorytobehavioralfinance.J.Econ.Perspect.2003,17,83–104.[CrossRef]
7. Tversky,A.;Kahneman,D.Advancesinprospecttheory:Cumulativerepresentationofuncertainty.J.RiskUncertain.1992,5,
297–323.[CrossRef]
8. Lease,R.C.;Lewellen,W.G.;Schlarbaum,G.G.Theindividualinvestor: Attributesandattitudes. J.Financ. 1974,29,413–433.
[CrossRef]
9. Aram, J.D.Attitudesandbehaviorsofinformalinvestorstowardearly-stageinvestments, technology-basedventures, and
coinvestors.J.Bus.Ventur.1989,4,333–347.[CrossRef]
10. Becchetti,L.;Caiazza,S.;Coviello,D.Financialeducationandinvestmentattitudesinhighschools:Evidencefromarandomized
experiment.Appl.Financ.Econ.2013,23,817–836.[CrossRef]
11. Lusardi,A.Financialliteracyandtheneedforfinancialeducation:Evidenceandimplications.SwissJ.Econ.Stat.2019,155,1.
[CrossRef]
12. Arthur, J.N.; Williams, R.J.; Delfabbro, P.H. The conceptual and empirical relationship between gambling, investing, and
speculation.J.Behav.Addict.2016,5,580–591.[CrossRef]
13. Keller,C.;Siegrist,M.Investinginstocks:Theinfluenceoffinancialriskattitudeandvalues-relatedmoneyandstockmarket
attitudes.J.Econ.Psychol.2006,27,285–303.[CrossRef]
14. Tomasic,R.;Akinbami,F.Theroleoftrustinmaintainingtheresilienceoffinancialmarkets.J.Corp.Law.Stud.2011,11,369–394.
[CrossRef]
15. Clarvis,M.H.;Bohensky,E.;Yarime,M.Canresiliencethinkinginformresilienceinvestments?Learningfromresilienceprinciples
fordisasterriskreduction.Sustainability2015,7,9048–9066.[CrossRef]
16. Lee,K.M.C.;Kraussl,R.G.W.;Lucas,A.;Paas,L.J.Adynamicmodelofinvestordecision-making:Howadaptationtolossesaffects
futuresellingdecisions.SSRNElectron.J.2008.Availableonline:https://www.econstor.eu/bitstream/10419/87082/1/08-112.pdf
(accessedon22January2025).
17. Monin,P.Onadynamicadaptationofthedistributionbuilderapproachtoinvestmentdecisions.Quant.Financ.2014,14,749–760.
[CrossRef]
18. Lucey,B.M.;Dowling,M.Theroleoffeelingsininvestordecision-making.J.Econ.Surv.2005,19,211–237.[CrossRef]
19. Renneboog,L.;TerHorst,J.;Zhang,C.Sociallyresponsibleinvestments:Institutionalaspects,performance,andinvestorbehavior.
J.Bank.Financ.2008,32,1723–1742.[CrossRef]
20. Maier,T.;Menold,J.;McComb,C.TherelationshipbetweenperformanceandtrustinAIine-finance.Front.Artif.Intell.2022,5,
891529.[CrossRef]
21. Schreibelmayr,S.;Moradbakhti,L.;Mara,M.FirstimpressionsofafinancialAIassistant:Differencesbetweenhightrustandlow
trustusers.Front.Artif.Intell.2023,6,1241290.[CrossRef]
22. Sun,J.;Lang,J.;Fujita,H.;Li,H.ImbalancedenterprisecreditevaluationwithDTE-SBD:DecisiontreeensemblebasedonSMOTE
andbaggingwithdifferentiatedsamplingrates.Inf.Sci.2018,425,76–91.[CrossRef]
23. Bond,S.;Elston,J.A.;Mairesse,J.;Mulkay,B.FinancialfactorsandinvestmentinBelgium,France,Germany,andtheUnited
Kingdom:Acomparisonusingcompanypaneldata.Rev.Econ.Stat.2003,85,153–165.[CrossRef]

Electronics2025,14,1505 16of17
24. Liu,J.;Pang,D.FinancialfactorsandcompanyinvestmentdecisionsintransitionalChina.Manag.Decis.Econ.2009,30,91–108.
[CrossRef]
25. Bond,S.;Meghir,C.Financialconstraintsandcompanyinvestment.Fisc.Stud.1994,15,1–18.[CrossRef]
26. Mills,K.;Morling,S.;Tease,W.Theinfluenceoffinancialfactorsoncorporateinvestment. Aust. Econ. Rev. 1995,28,50–64.
[CrossRef]
27. Geetha,N.;Ramesh,M.Astudyonrelevanceofdemographicfactorsininvestmentdecisions.Perspect.Innov.Econ.Bus.2012,10,
14–28.[CrossRef]
28. Lusardi,A.;Mitchelli,O.S.Financialliteracyandretirementpreparedness:Evidenceandimplicationsforfinancialeducation.
Bus.Econ.2007,42,35–44.[CrossRef]
29. HassanAl-Tamimi,H.A.;BinKalli,A.A.FinancialliteracyandinvestmentdecisionsofUAEinvestors.J.RiskFinanc.2009,10,
500–516.[CrossRef]
30. Waweru,N.M.;Munyoki,E.;Uliana,E.Theeffectsofbehaviouralfactorsininvestmentdecision-making:Asurveyofinstitutional
investorsoperatingattheNairobiStockExchange.Int.J.Bus.Emerg.Mark.2008,1,24–41.[CrossRef]
31. Lubis,H.;Kumar,M.D.;Ikbar,P.;Muneer,S.Roleofpsychologicalfactorsinindividuals’investmentdecisions. Int. J.Econ.
Financ.Issues2015,5,397–405.
32. Antony,A.;Joseph,A.I.Influenceofbehaviouralfactorsaffectinginvestmentdecision—AnAHPanalysis.Metamorphosis2017,16,
107–114.[CrossRef]
33. Das,S.;Jain,R.Astudyontheinfluenceofdemographicalvariablesonthefactorsofinvestment—AperspectiveontheGuwahati
region.Int.J.Res.Humanit.ArtsLit.2014,2,97–102.
34. Masomi,S.R.;Ghayekhloo,S.Consequencesofhumanbehaviorsineconomics:Theeffectsofbehavioralfactorsininvestment
decisionmakingatTehranStockExchange.InProceedingsoftheInternationalConferenceonBusinessandEconomicsResearch,
Langkawi,Malaysia,14–16March2011;Volume1,pp.234–237.
35. Senda,D.A.;Rahayu,C.W.E.;Rahmawati,C.H.T.Theeffectoffinancialliteracylevelanddemographicfactorsoninvestment
decision.MediaEkon.Manag.2020,35,100–111.[CrossRef]
36. Lutfi,L.TherelationshipbetweendemographicfactorsandinvestmentdecisioninSurabaya.J.Econ.Bus.Account.Ventur.2010,
13,1–9.[CrossRef]
37. Gaikar,V.Demographicvariablesinfluencingfinancialinvestmentofurbanindividuals: Acasestudyofselecteddistrictsof
MaharashtraState.SSRNElectron.J.2021.Availableonline:https://ssrn.com/abstract=3890224(accessedon22January2025).
[CrossRef]
38. Cooremans,C.Makeitstrategic!Financialinvestmentlogicisnotenough.EnergyEffic.2011,4,473–492.[CrossRef]
39. Alkaraan, F.; Northcott, D.StrategicInvestmentDecision-MakingProcesses: TheInfluenceofContextualFactors. Meditari
Account.Res.2013,21,117–143.[CrossRef]
40. Forssbæck,J.;Oxelheim,L.Finance-specificfactorsasdriversofcross-borderinvestment—Anempiricalinvestigation.Int.Bus.
Rev.2008,17,630–641.[CrossRef]
41. Zarifis,A.;Cheng,X.AmodeloftrustinFintechandtrustinInsurtech:Howartificialintelligenceandthecontextinfluenceit.J.
Behav.Exp.Financ.2022,36,100739.[CrossRef]
42. Huston,S.J.Measuringfinancialliteracy.J.Consum.Aff.2010,44,296–316.[CrossRef]
43. Mandell,L.;Klein,L.S.Theimpactoffinancialliteracyeducationonsubsequentfinancialbehavior.J.Financ.Couns.Plan.2009,
20,15–24.
44. Markowitz,H.M.Foundationsofportfoliotheory.J.Financ.1991,46,469–477.[CrossRef]
45. Davis,F.D.Perceivedusefulness,perceivedeaseofuse,anduseracceptanceofinformationtechnology.MISQ.1989,13,319–340.
[CrossRef]
46. Rahman, M.; Gan, S.S.GenerationYinvestmentdecision: Ananalysisusingbehaviouralfactors. Manag. Financ. 2020, 46,
1023–1041.[CrossRef]
47. Arif,K.Financialliteracyandotherfactorsinfluencingindividuals’investmentdecision:Evidencefromadevelopingeconomy
(Pakistan).J.PovertyInvestig.Dev.2015,12,74–84.
48. Salahuddin,M.;Islam,M.R.Factorsaffectinginvestmentindevelopingcountries: Apaneldatastudy. J.Dev. Areas2008,42,
21–37.[CrossRef]
49. Mlambo,K.;Oshikoya,T.W.MacroeconomicfactorsandinvestmentinAfrica.J.Afr.Econ.2001,10,12–47.[CrossRef]
50. Love,I.;Zicchino,L.Financialdevelopmentanddynamicinvestmentbehavior:EvidencefrompanelVAR.Q.Rev.Econ.Financ.
2006,46,190–210.[CrossRef]
51. Locatelli,G.;Mancini,M.Theroleofthereactorsizeforaninvestmentinthenuclearsector: Anevaluationofnon-financial
parameters.Prog.Nucl.Energy2011,53,212–222.[CrossRef]
52. Masini, A.; Menichetti, E. The impact of behavioral factors in the renewable energy investment decision-making process:
Conceptualframeworkandempiricalfindings.EnergyPolicy2012,40,28–38.[CrossRef]

Electronics2025,14,1505 17of17
53. Ngoc,N.M.;Tien,N.H.;Hieu,V.M.Therelevanceoffactorsaffectingrealestateinvestmentdecisionsforpost-pandemictime.Int.
J.Bus.Glob.2023,1,1–15.[CrossRef]
54. Dutta,N.;Roy,S.Foreigndirectinvestment,financialdevelopmentandpoliticalrisks.J.Dev.Areas2011,45,303–327.[CrossRef]
55. Vesselenyi,T.;Dzi¸tac,I.;Dzi¸tac,S.;Vaida,V.Surfaceroughnessimageanalysisusingquasi-fractalcharacteristicsandfuzzy
clusteringmethods.Int.J.Comput.Commun.Control2008,3,304–316.[CrossRef]
56. Csorba,L.M.;Crăciun,M.Anapplicationofthemulti-perioddecisiontreesinsustainablemedicalwasteinvestments.InSoft
ComputingApplications. SOFA2016. AdvancesinIntelligentSystemsandComputing;Balas,V.,Jain,L.,Balas,M.,Eds.;Springer:
Cham,Switzerland,2018;Volume634,pp.540–556.
57. Zhou,T.;Gao,X.;Sun,X.;Han,L.Splitdifferenceweighting:Anenhanceddecisiontreeapproachforimbalancedclassification.
Int.J.Comput.Commun.Control2024,19,6702.[CrossRef]
58. Daranda,A.;Dzemyda,G.Novelmachinelearningapproachforself-awarepredictionbasedoncontextualreasoning. Int. J.
Comput.Commun.Control2021,16,4345.[CrossRef]
59. Crăciun,M.;Csorba,L.M.Applicationofthefuzzy-pay-offmethodinthevaluationofafinancialinstrument.InSoftComputing
Applications. SOFA2016. AdvancesinIntelligentSystemsandComputing; Balas, V., Jain, L., Balas, M., Eds.; Springer: Cham,
Switzerland,2018;Volume634,pp.235–252.
60. Cuc,L.D.;Rad,D.;Săplăcan,S.;Sendroiu,C.;Bâtcă-Dumitru,G.C.;Wysocki,D.;Dutu,A.;Manolescu,A.-A.Ahierarchical
,
clusteringanalysisofthemanagementaccountingpracticesperceptionsinRomania.Int.J.Comput.Commun.Control2024,19,
6864.[CrossRef]
61. Pelau,C.;Dabija,D.C.;Stanescu,M.CanItrustmyAIfriend?Theroleofemotions,feelingsoffriendshipandtrustforconsumers’
information-sharingbehaviortowardAI.OeconomiaCopernic.2024,15,407–433.[CrossRef]
62. Toader,L.;Paraschiv,D.;Dinu,V.;Manea,D.;Mihai,M.Theeffectsofprivatesectorcompanies’researchanddevelopment
investmentsontheadoptionofcloudcomputingservicesintheEuropeanUnion. E+MÈkon. AManag. 2023, 26, 189–202.
[CrossRef]
63. Ciocoiu,C.N.;Prioteasa,A.L.;Colesca,S.E.RiskmanagementimplementationforsustainabledevelopmentofRomanianSMEs:
Afuzzyapproach.AmfiteatruEcon.2020,22,726–741.[CrossRef]
64. Lazea,G.I.;Bunget,O.C.;Lungu,C.Cryptocurrencies’impactonaccounting:Bibliometricreview.Risks2024,12,94.[CrossRef]
65. Ogrean,C.;Herciu,M.Businessmodelsaddressingsustainabilitychallenges—Towardsanewresearchagenda.Sustainability
2020,12,3534.[CrossRef]
66. Anwar,K.FactorsaffectingstockexchangeinvestmentinKurdistan.Int.J.Account.Bus.Soc.2017,25,32–37.[CrossRef]
67. Carcello,J.V.;Hermanson,D.R.;Raghunandan,K.FactorsassociatedwithUSpubliccompanies’investmentininternalauditing.
Account.Horiz.2005,19,69–84.[CrossRef]
68. Simone,F.; Ansaldi,S.M.; Agnello,P.; DiGravio,G.; Patriarca,R.Knowledgeingraphs: Investigatingthecompletenessof
industrialnearmissreports.Saf.Sci.2023,168,106305.[CrossRef]
69. Patriarca,R.; DeCarlo,F.; Leoni,L.Asystem-theoreticfuzzyanalysis(STheFA)forsystemicsafetyassessment. ProcessSaf.
Environ.Prot.2023,177,1181–1196.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.