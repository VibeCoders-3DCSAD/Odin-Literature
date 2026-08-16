---
conversion_metadata:
  converted_at: "2026-07-21T08:54:16Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Tabak et al.pdf"
  source_pdf_sha256: "21b532326b9d92dccf1b54952dfc669954fb18719d88104d49cdacd41b11de76"
  page_count: 33
  markdown_char_count: 209849
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Article
Assessing the Drivers of Financial Vulnerability and Fraud in
Brazil: The Critical Role of Financial Planning over Literacy

Benjamin Miranda Tabak *,†

, Débora H. Cardoso †

and Cristiano C. Silva †

School of Public Policy and Government, Getulio Vargas Foundation (FGV/EPPG), SGAN 602 Módulos A,B,C,
Asa Norte, Brasilia 70830-020, DF, Brazil; debora.cardoso@fgv.edu.br (D.H.C.); cristiano.silva@fgv.br (C.C.S.)
* Correspondence: benjamin.tabak@fgv.br
† These authors contributed equally to this work.

Abstract

This paper introduces and validates a comprehensive instrument designed to measure
financial literacy, its underlying determinants, and to assess how factors such as planning
affect financial vulnerability and fraud in Brazil. This work represents a crucial step toward
achieving several Sustainable Development Goals (SDGs). The study utilizes a two-fold
methodology. First, Confirmatory Factor Analysis (CFA) is used to validate a six-component
model consisting of Financial Literacy, Vulnerability, Fraud, Cognitive Reflection, Crypto
Literacy, and Planning. This analysis is followed by the development and interpretation
of a Random Forest model, which was identified as the best-performing predictor in a
comparison of seven machine learning algorithms. The CFA results showed that Financial
Planning has a stronger negative correlation with Financial Vulnerability (−0.642) and
Fraud (−0.375) than Financial Literacy does. This evidence was further supported by
the machine learning analysis; analyses using both SHAP and LIME identified Financial
Planning as the strongest predictor of financial vulnerability and fraud. The analysis
further showed significant social inequalities in the developed models and identified the
gender variable (female) as an important predictor of enhanced financial vulnerability.
Converging evidence from both CFA and machine learning confirms that sound planning
practices are more important than financial knowledge in reducing financial distress. Our
findings provide a solid foundation for the development of inclusive public policy that
promotes behavioral change, aiming to reduce systemic inequalities (SDG 10) and achieve
sustainable economic stability (SDG 8), thereby supporting social goals and the Sustainable
Development Goals.

Keywords: financial literacy; financial planning; vulnerability; financial behavior;
sustainable development

1. Introduction

Lack of financial knowledge directly affects individuals’ ability to make informed
economic decisions, thereby damaging their financial well-being in the short and long term.
This limitation is especially evident in retirement, when accumulated mistakes in financial
management become more difficult to correct. Studies highlight that low financial literacy
is associated with inadequate economic choices, such as excessive indebtedness, lack of
planning, and greater exposure to financial fraud, negatively impacting individual and
collective economic stability [1,2].

Academic Editor: Sajid Anwar

Received: 30 July 2025

Revised: 18 September 2025

Accepted: 24 September 2025

Published: 17 October 2025

Citation: Tabak, B.M.; Cardoso, D.H.;

Silva, C.C. Assessing the Drivers of

Financial Vulnerability and Fraud in

Brazil: The Critical Role of Financial

Planning over Literacy. Sustainability

2025, 17, 9219. https://doi.org/

10.3390/su17209219

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Sustainability 2025, 17, 9219

https://doi.org/10.3390/su17209219

---

<!-- PAGE 2 -->

Sustainability 2025, 17, 9219

2 of 33

Socioeconomic factors, especially low schooling, further exacerbate financial vulnera-
bility, which makes it increasingly important to develop intersectional interventions that
reach groups of women, black individuals, and people with low schooling, who have
greater difficulty in accessing good financial information and services, taking into account
the particularities of each one [3,4].

It is important to note that financial literacy refers to a set of skills, going beyond just
knowledge about finance. This is confirmed when we analyze traditional interventions that
focus only on educational methods, thereby neglecting behavioral factors. Interventions
such as these have low efficiency, which reveals the need to develop public policies that
consider the behavioral biases of individuals, as well as financial literacy.

Especially in the Brazilian context, research into financial literacy as a multifaceted
element is even more necessary. The Brazilian Central Bank and the Credit Guarantee
Fund point out that on a scale of 0 to 100, the average level of financial literacy in Brazil is
59.6, with about 75% of survey participants obtaining a maximum score of 70 points, being
those with higher levels of education. The same study shows that 44.8% of Brazilians in
the sample said they never or rarely had money left over at the end of the month, and 36%
were concerned about whether they would have enough money to cover their expenses.
Furthermore, the Central Bank points out that 64% of Brazilians face financial instability
and around 49.1% report that experiencing financial worries affects their mental health
on a personal and family level [5]. These data reveal Brazilians’ exposure to financial
vulnerability, which shows that there are still significant gaps to be filled in terms of
financial literacy in Brazil, especially for minority groups such as people with less access to
education and formal financial services.

In this context, investigating the elements related to financial literacy can help in the
development of interventions and public policies that contribute to individuals’ financial
autonomy and well-being. Financial education has a positive and significant influence on
financial inclusion and the attainment of sustainable livelihoods [6], and is considered a
path to sustainability. It is also key to ensuring the financial sustainability of individuals,
families, businesses, and national economies [7], since economic growth and sustainability
depend on the financial education of individuals.

Financial literacy is a pillar for the achievement of several Sustainable Development
Goals of the 2030 Agenda of the United Nations, related to poverty reduction (SDG 1),
increased well-being (SDG 3), higher-quality education (SDG 4), gender equality (SDG 5),
economic growth (SDG 8), reducing inequalities (SDG 10), and more responsible con-
sumption and production (SDG 12) [8]. This reinforces the indispensability of broad
and multifaceted research into financial literacy, as it is a driving force for individual
and collective economic development, in addition to contributing significantly to poverty
reduction [9].

Objective measures of financial literacy are important for reducing inequalities be-
tween people, as without financial literacy, they can face a series of problems, such as
difficulties in making informed investments or incurring losses on assets, which can harm
their financial well-being. Nevertheless, financial literacy as a concept should be further
developed in terms of also covering financial planning attitudes and using new digital
assets as investment products, such as cryptocurrencies. Of equal importance is measuring
knowledge and attitude impacts across desired outcome indicators, such as financial fraud
prevalence or financial vulnerabilities. The latter, defined as financial precariousness or
a lack of financial well-being, hinders the attainment of Sustainable Development Goal 1,
aimed at achieving a world without poverty, and at the same time hinders SDG 10, aimed
at reducing inequalities. Both impacts are significant and inhibit long-term sustainable
development of a country.

---

<!-- PAGE 3 -->

Sustainability 2025, 17, 9219

3 of 33

The primary objective of this work is to develop an instrument that comprehensively
measures financial literacy, encompassing aspects such as crypto literacy and financial
planning, and assess how these factors influence financial vulnerability and susceptibility
to financial fraud among individuals, ultimately impacting their financial well-being. The
scope of our instrument may help fill gaps in the literature, since it can be related to aspects
such as cognitive biases, financial fraud, and financial vulnerability. To the best of our
knowledge, these dimensions have not been analyzed in an integrated manner to date.

The structure of our paper is organized into interconnected sections. Initially, the
literature review presents the fundamental concepts of financial literacy, financial planning,
and susceptibility to fraud and financial vulnerability. Next, in Section 3 used to develop
and validate the proposed instrument are detailed, as well as the experimental application.
Finally, in Sections 4 and 5 provide insights into how financial literacy can be increased
and financial vulnerabilities reduced, with practical implications for public policies and
educational programs in Brazil.

2. Literature Review

There is a relatively large body of literature on how individuals deal with their finances.
Knowledge on this subject is essential because it provides conceptual inputs that help
people avoid putting themselves in a situation of financial vulnerability, especially in
scenarios of socioeconomic instability [1]. A better financial perception contributes to more
assertive decision-making based on information, thereby reducing the risk of indebtedness,
as well as promoting conditions for more sustainable economic growth, financial inclusion,
and positive financial behavior [7,10].

Financial literacy is understood as an individual’s ability to understand and apply
financial concepts to make well-informed and more rational decisions [11–13]. In the
literature, several factors are identified as variables that influence financial literacy. These
include demographic and socioeconomic variations, with an emphasis on educational
attainment, age, and gender [11,14]. Another factor highlighted in recent studies is the lack
of access or limited access to formal financial technologies and services [9].

Financial literacy has a strong economic and social impact, as it enables individuals to
improve their financial well-being and deal with situations of financial vulnerability [11].
The literature shows that people with greater financial literacy have greater autonomy
and ability to make prudent and beneficial decisions about their financial lives, such as
financial planning, increasing savings, and managing risks [15]. In addition to domestic
benefits, financial literacy is also associated with greater chances of business success, since
more literate entrepreneurs have higher incomes and savings [13]. Furthermore, in rural
contexts, financial literacy is also essential for encouraging entrepreneurial activities, which
contribute to the empowerment of rural communities and sustainable development [9].

Financial literacy contributes to people’s autonomy, enabling them to understand
economic scenarios and strategic resources and take more effective actions based on
planning, managing resources, calculating interest rates, diversifying investments, and
interacting with financial institutions. This contributes to making informed economic
decisions [1,16–24].

Understanding individuals’ attitudes towards the use of money, financial decisions,
risk management capacity, and financial uncertainties is the object of study of financial
literacy [25,26]. Greater financial literacy contributes to healthier financial behaviors, such
as greater savings, lower propensity to debt, greater financial planning capacity, and
better participation in the stock market [2,20,27–29]. The importance of this knowledge is
demonstrated by the number of people unable to answer simple questions on the subject,
as shown by an experiment carried out in the United States, in which only half of the

---

<!-- PAGE 4 -->

Sustainability 2025, 17, 9219

4 of 33

respondents over the age of 50 were able to get two simple questions about compound
interest and inflation right [30]. It is worth mentioning that low financial literacy is a global
issue that includes countries such as Germany, Sweden, Italy, Japan, and New Zealand [26].
Important aspects of economic life are impacted by financial knowledge, as is the case
with saving for retirement. A study carried out in the Netherlands found that getting more
questions right about financial literacy contributes to a 10 percentage point increase in the
ability to plan for retirement [26]. The number of social security programs, aimed at the most
diverse groups of individuals such as women, low-income families, and minorities [31],
reveals the gulf in the level of financial literacy, as can be seen among whites and Asians,
who are more knowledgeable in this area than African-Americans or Hispanics [26].

Financial literacy also helps to reduce financial vulnerability, a phenomenon charac-
terized by the inability to pay unforeseen bills, high levels of debt, and frequent exposure
to fraud. This issue is very worrying because it reveals a structural problem that exposes
economic inequalities, financial exclusion, and a lack of financial knowledge. This finan-
cial vulnerability can also affect the health of individuals, which can have an impact on
physical and mental health, interpersonal relationships, and work performance [32,33].
The training generated by financial literacy contributes to better management of savings
and investments; this capacity reduces financial vulnerability and thus provides economic
well-being [4,27–29].

Actions such as inadequate financial planning and impulsiveness, especially in the
short term, are factors present in the behavior of people exposed to financial vulnerabil-
ity, which makes them more susceptible to fraud, especially in a scenario of low digital
inclusion [34]. This is the case in Brazil, for example, where the low-income population has
no access to formal financial products such as credit and insurance [3,4]. And this financial
exclusion leads to dependence on informal and predatory financial services, which makes
the situation of vulnerability even worse [26].

The low level of knowledge about basic financial issues such as budgeting, savings,
and credit as a result of a lack of financial literacy exposes individuals to vulnerability,
as recent studies have shown. This lack of knowledge makes it difficult to deal with
unforeseen events, which contributes to excessive indebtedness. The consequence of this
behavior is the exclusion of low-income populations from the formal financial system,
increasing their exposure to fraud and unsustainable financial behavior [4].

Financial literacy is an important tool for promoting financial stability; understand-
ing the costs associated with credit and avoiding unsustainable financing decisions [35]
contributes to this result. This knowledge contributes to better financial planning, result-
ing in the establishment of emergency reserves, which reduces default and also helps to
strengthen individual and collective economic security.

Understanding cryptocurrencies is of paramount importance for assessing financial
knowledge. The 1st National Cryptocurrency Survey in Brazil indicates that crypto assets
have already surpassed stocks in investor preference, showing that investing in cryptocur-
rencies is now among the five most popular forms of investment among Brazilians. Despite
this, the survey shows that Brazilians’ knowledge of other aspects related to this market is
still limited and there is a long way to go in terms of financial education [36].

The effectiveness of financial literacy is clear in its role in contributing to good financial
behavior and reducing the risk of vulnerability. The literature shows that more financially
literate individuals develop more resilient behavior in times of crisis, reducing their ex-
posure to impulsive behavior and financial fraud. Financial literacy also contributes to
financial inclusion and sustainable economic development [7,37]. In scenarios characterized
by exclusion and economic instability, financial literacy highlights its importance as a tool

---

<!-- PAGE 5 -->

Sustainability 2025, 17, 9219

5 of 33

for change. This reinforces the importance of initiatives that support the expansion and
better dissemination of financial literacy at different levels of society.

Substantial amounts of literature confirm the importance of individual-level financial
literacy to personal as well as macroeconomic well-being. However, scholarly investiga-
tion has progressed mainly in a compartmentalized and unconnected manner. The past
literature can broadly be categorized into a few different camps: (1) studies focusing on
basic knowledge of finance where often interest compounding, inflation, or risk diversi-
fication (e.g., [26,30]) are tested, among other factors; (2) behavioral finance studies that
investigate how specific cognitive biases (e.g., overconfidence bias or loss aversion) impact
individual-level financial decision-making (e.g., [38,39]); (3) socioeconomic examinations
that assess drivers of financial insecurity often linking it to variables such as race, gender,
or income; or (4) recent scholarship where awareness regarding new financial instruments
such as cryptocurrencies is explored but often found to be unrelated to more traditional
literacy testing. While these represent worthwhile endeavors individually, they collectively
present an incomplete picture.

The key research gap, then, is the absence of a unifying, multidimensional frame-
work that simultaneously examines these components. Current scholarship falls short of
adequately examining interdependencies among financial literacy (both traditional and
novel), behavioral inclinations (e.g., planning), cognitive traits (e.g., biases and reflective
thinking), and real-world results (related to being vulnerable or being a fraud target) within
a single framework. Accordingly, an ambiguous understanding remains regarding how
these forces interact to impact one’s individual financial resilience. Additionally, a crucial
consideration missing from this fragmented landscape is an explicit connection to sus-
tainable development. While financial inclusion is often aligned with the United Nations
Sustainable Development Goals (SDGs), existing scholarship has failed to adequately ex-
plore how the quality of financial literacy—encompassing behaviors, cognitive resilience,
and vulnerability—facilitates social and economic sustainability. For instance, variations
in financial literacy and vulnerability by race and gender transcend economic issues and
embody the causes of social injustices that undermine social sustainability, especially with
respect to SDG 5: Gender Equality and SDG 10: Reduced Inequalities. Similarly, household
finance volatility has a direct impact on a nation’s economic resilience, delineating a core
component of SDG 8 (Decent Work and Economic Growth).

Our work aims to address these broad deficits through three key avenues. First,
we move beyond the individualistic methodology by positing and testing an integrated
framework that simultaneously considers basic financial literacy, knowledge about cryp-
tocurrency, financial planning, reflective thinking, and cognitive bias. Secondly, as a
necessary methodological innovation, we design and validate a new, omnibus instrument
specially developed for the Brazilian setting, which simultaneously measures these diverse
constructs. We establish the reliability and validity of such an instrument through Con-
firmatory Factor Analysis and thus provide a sturdy tool for future research applications.
Finally, by including socioeconomic and demographic variables (such as race and gender)
alongside coveted outcome measures (such as financial vulnerability and fraud experience),
our exploratory work establishes a direct empirical link between the multifaceted dimen-
sions of financial literacy and the overall goals of social and economic sustainability. In
doing so, we reconceptualize financial literacy as a critical component for building fairer,
more resilient, sustainable societies, beyond a mere concern for individual wealth.

---

<!-- PAGE 6 -->

Sustainability 2025, 17, 9219

6 of 33

3. Materials and Methods
3.1. Sampling

This research received approval from the Ethics Committee on Research Involving
Human Subjects of the Getulio Vargas Foundation—CEPH/FGV (P.214.2024). Data col-
lection commenced upon the acquisition of ethical permission. All study participants
provided informed consent. The given details encompassed the study’s aim, confidentiality,
participant autonomy, voluntary participation, the right to withdraw at any time, and the
guarantee that all acquired data would be anonymized to safeguard participant identity.

Although our analysis sheds light on the relevant determinants of vulnerability and im-
propriety in financial dealings in Brazil, it is important to consider the special characteristics
of our sample in interpreting the findings.

We conducted our data collection through direct contact at urban focal points, in-
cluding shopping centers, bus and subway terminal stations, and public spaces in the
Federal District. Specifically, our convenience sampling was employed to achieve a repre-
sentative coverage of the population by their socioeconomic levels, educational levels, and
occupation. The total size of the sample was 256 participants.

Despite this, however, we are aware of the following limitations associated with the
coverage of the sample. First, our focus on an urban population means that the sample does
not capture the views of populations in rural or other remote locations, and may face some
pecuniary issues, as well as disparate access to infrastructure for finances and information
technology. Secondly, the survey covered mostly the Federal District. This territory is
characterized by high internal mobility and demographic diversity, which increases the
diversity of the sample. However, given its unique economic features as the administrative
seat of the government, it may not be representative of other Brazilian states.

As such, it is critical to be cautious in extrapolating these findings to the broader
Brazilian population. The combination of planning, literacy, and vulnerability may be likely
influenced by local economic factors and cultural norms, which are addressed by this study
in limited ways. Although the population in the Federal District is very diverse, with most
residents coming from different parts of the country, large-scale migration may result in
some states in Brazil becoming more homogeneous, and these factors may work in different
ways. Nonetheless, this study adds to the creation of a sound framework in understanding
nuanced relations of finances within a heterogeneous urban environment in Brazil. We
show how it is important to expand financial education programs by incorporating key
elements, like planning finances, to inform intensive public policy actions.

Data were collected through the SurveyMonkey platform version 4.5.7, using electronic
devices. The data was kept in Survey Monkey’s cloud-based database, which keeps the
data encrypted according to the SOC 2 standard.

3.2. Instrument

In addition to socioeconomic questions, our instruments comprise items adapted
to Brazilian reality, ensuring good consistency and reliability (we used Confirmatory
Factor Analysis to evaluate the instruments and reduce the number of items to obtain
reliable and valid instruments, which we used for the econometric and machine learning
analysis). We developed a comprehensive financial literacy instrument, which comprises
core financial literacy items (FL). We also included financial planning (FP) and knowledge
on cryptocurrency (Crypto). This instrument has two knowledge dimensions (FL and
crypto) and an attitude dimension, which is financial planning.

We evaluated the impact of the Broad FL instrument on financial vulnerability (VF) or
financial fraud (FV). These two variables capture an outcome dimension, where respondents
have suffered from financial vulnerability (i.e., several bills past due) or financial fraud

---

<!-- PAGE 7 -->

Sustainability 2025, 17, 9219

7 of 33

(i.e., suffered losses from FF). We also measured the reflective and analytical thinking of
respondents using the Cognitive Reflection Test (CRT). In addition, we measured four
cognitive biases and control variables, including gender, race, age, and income.
It is
important to highlight that the final instrument follows the results from the Confirmatory
Factor Analysis, regarding the goodness of the model fit and the reliability and validity of
the latent factors.

3.3. Financial Literacy—Core Knowledge

Financial knowledge was measured using the main instrument (the Big Five) de-
veloped by Lusardi and Mitchell [26]. This is a widely used instrument for measuring
financial literacy, which provides a standardized and comparable measure of financial
knowledge between different countries and groups. The main objective of the “Big Five”,
which is an expanded version of the “Big Three” [25], is to provide a consistent measure
of financial knowledge. Consisting of questions on simple interest rates, inflation, bond
prices, mortgages, and risk diversification, the questionnaire provides an expanded view of
respondents’ financial knowledge [25]. To adapt it to the Brazilian context, we translated the
instrument by replacing “mortgage” with “financing”. We also included one question from
financial knowledge from the Financial Literacy Survey [40] which measures investment
knowledge focusing on return on investment.

Next, we selected two self-perception questions on financial knowledge from the
Financial Literacy Survey [40]. These questions allowed us to analyze whether people who
have had access to financial education manage their finances better and how confident they
are in their financial knowledge.

We covered different aspects of financial literacy, and to assess this aspect, we used
three questions from the Financial Literacy Quiz [40]. This is a tool based on the recommen-
dations of the Financial Literacy Map, a Japanese framework created by the Committee for
the Promotion of Financial Education. In order to cover different characteristics of financial
literacy, we included questions on family budget, financial knowledge, understanding of
financial/economic circumstances, appropriate selection/use of financial products, and
appropriate use of external expertise.

To ensure that the score of financial knowledge reflected the real result, we used the
method of Item Response Theory (IRT). IRT models analyze individual item performance in
relation to overall ability, allowing for more precise measurement of financial literacy and
providing insights into the difficulty and discriminating power of each question. Each item
in a test has constraints, such as difficulty, discrimination (ability to differentiate between
people with different skill levels), and the probability of getting it right by chance.

We utilized a multidimensional Item Response Theory named mirt. The mirt software
was developed to estimate multidimensional item response theory parameters for both
exploratory and confirmatory models with maximum-likelihood approaches [41]. We use
R Software version 4.5.1 whit Mirt package version 1.45.1.

After analyzing the eight questions in the instrument, the IRT method identified one
question (three) that participants had difficulty answering, even those with high literacy,
while some with low literacy also answered correctly. We have decided to disregard this
question in the scoring (Figure 1).

We also employed Confirmatory Factor Analysis, retained only four items that had
high loadings, and improved the psychometric properties of these instruments. The final
instruments are provided in Appendix C.

---

<!-- PAGE 8 -->

Sustainability 2025, 17, 9219

8 of 33

Figure 1. Item Characteristic Curve (ICC) graphs for each question in the Item Response Theory (IRT)
model, in this case a 2PL model (two-parameter logistic model). For each item, the graph shows a
curve that represents the chance of a correct response to the question, as a function of the person’s
latent ability (θ). X-axis: latent ability (θ) from −6 to +6. This is the level of proficiency or financial
literacy. θ = 0 is the average ability in the sample. θ > 0 indicates more “skilled” individuals. θ < 0
indicates individuals with below-average ability. Y-axis: probability of a correct response from 0 to 1.
Shows the chance of an individual with ability θ getting the item right. The steeper and higher the
curve, the better the item discriminates between ability levels.

3.4. Financial Planning

Financial planning was based on research by Anderloni et al. [42]. Six questions
were selected, focusing on personal behavior and attitudes, such as critical thinking before
buying something, setting financial goals, personal vigilance in financial matters, paying
bills on time, and people with divergent thinking, such as living for today and letting
tomorrow take care of itself. We opted to adopt a scale of only two response options for the
instrument’s items, attributing one if the respondent agreed to some extent with the text. It
should be noted that there are no correct or incorrect answers, and the score obtained is a
direct measure of the respondents’ level of financial planning. Hence, a lower score reflects
a lower level of financial planning.

3.5. Cryptocurrency Literacy

For knowledge of cryptocurrencies, four items were selected from an instrument
initially developed by Al-Omoush et al. [43], based on an empirical study and items
taken from relevant studies in the literature on financial literacy. The original instrument
contains 24 items, divided into six scales with 4 items each. In addition, three experts
in cryptocurrencies, financial technology, and investments in financial assets reviewed
this instrument to evaluate the measures and refine the items, ensuring the instrument’s
accuracy and robustness. As far as the answers are concerned, respondents must score each
item according to a Likert scale, ranging from 1 (strongly disagree) to 5 (strongly agree).

The original instrument consists of six scales, developed and validated based on
the relevant literature, namely (i) financial literacy, which assesses the knowledge and
ability to deal with fundamental concepts of cryptocurrencies [44,45]; (ii) perceived value,
which emphasizes the perceived benefits of using cryptocurrencies, such as security and
efficiency [46]; (iii) optimism, which measures users’ positive outlook on the future of
cryptocurrencies [47,48]; (iv) cryptocurrency dependence, based on the scales proposed
by Sonkurt and Altınöz [49] and Kiatsakared and Chen [50], which evaluates compulsive
behaviors and negative impacts related to excessive use; (v) trust, addressing the perceived
security and reliability of cryptocurrency transactions [51,52]; and, finally, (vi) intention

---

<!-- PAGE 9 -->

Sustainability 2025, 17, 9219

9 of 33

to continue using, which examines the long-term behavioral intention to continue using
cryptocurrencies [53,54].

To develop the instrument used in this study, only the items related to the financial
literacy scale were selected to gauge the participants’ self-perception of their knowledge
about the cryptocurrency market and risk assessment. Unlike the original study, we opted
to adopt a scale of only four response options for the instrument’s items, 1 (“strongly
disagree”), 2 (“disagree”), 3 (“agree”), and 4 (“strongly agree”). It should be noted that
there are no correct or incorrect answers, and the score obtained is a direct measure of the
respondents’ level of knowledge and perception. Hence, a lower score reflects a lower level
of knowledge about cryptocurrencies.

3.6. Financial Vulnerability

The questionnaire developed in this study was based on research by Anderloni et al. [42],
whose main objective is to propose a financial vulnerability indicator (Financial Vulnerabil-
ity Index) that summarizes different aspects of the financial stress faced by families, such
as excessive indebtedness, inability to cover monthly expenses, late payments and other
conditions of financial instability, as well as analyzing how the characteristics of families
are related to the level of financial vulnerability.

The study questionnaire covers five main areas to measure the degree of financial
vulnerability of families: (i) sociodemographic characteristics; (ii) economic and financial
profile, which investigates the level of income, financial wealth and assets, types of debt
(secured or unsecured), employment status, and use of risk management instruments,
such as insurance; (iii) financial literacy; and (iv) economic and financial situation, which
explores difficulties in balancing monthly expenses and dealing with unexpected expenses.
The items included in our questionnaire essentially concern secure access to credit lines,
financial well-being, household expenses, and access to health services.

3.7. Financial Fraud

To compose this dimension, we used questions on financial fraud (FF) from the Assess-
ment of Financial Consumer Survey Report (2018) and two questions on secure financial
behavior from the Financial Literacy Survey [40]. The items were selected to investigate
the vulnerability of individuals to economic crime and financial fraud. These questions are
based on studies examining exposure to economic crime and the role of financial literacy in
preventing it [55], as well as reports such as the Assessment of Financial Consumer Survey
Report (2018), which analyzes the impact of financial fraud in various contexts.

3.8. Cognitive Reflection Test

We used the 7-item Cognitive Reflection Test [56]. The Cognitive Reflection Test
is a psychological tool widely used to measure an individual’s propensity to resort to
reflective and analytical thinking rather than relying on intuitive and rapid responses.
Developed by Shane Frederick, the CRT was initially developed with just three questions,
but has evolved to include more comprehensive versions, such as the seven-item version.
This expansion aimed to increase the test’s accuracy and ability to capture nuances in
participants’ cognitive style.

The CRT is based on the dual thought process model, which distinguishes between
two cognitive systems: System 1, which is intuitive, fast, and automatic, being responsible
for impulsive responses that often lead to error due to high susceptibility to optical illusions,
and System 2, which is reflective, slow, and deliberate, requiring greater cognitive effort to
suppress intuitive responses and reach more reasoned solutions [39,57–60]. CRT questions
are designed to exploit this dynamic, presenting problems that appear simple at first glance
but contain cognitive traps designed to induce incorrect answers.

---

<!-- PAGE 10 -->

Sustainability 2025, 17, 9219

10 of 33

The expanded version of the CRT, with seven items, maintains the logic of the original
version, but incorporates a greater number of questions to diversify the challenges pre-
sented and improve the reliability of the results. These questions are carefully formulated
to provoke intuitive errors and challenge the participant to resort to analytical thinking.
For example, one of the classic questions in the three-item version asks: “A bat and a
ball together cost $1.10. The bat costs $1 more than the ball. How much does the ball
cost?” The intuitive and wrong answer would be USD 0.10, while the correct answer, USD
0.05, requires more in-depth reasoning. In the seven-item version, similar problems are
presented, covering a wider spectrum of mathematical and logical reasoning.

Scoring on the CRT is simple and straightforward, with each correct answer worth
one point, resulting in a total score ranging from 0 to 7. Interpreting the results provides
insight into the participant’s cognitive style: lower scores indicate a strong reliance on
intuitive thinking, while higher scores reflect a greater capacity for analytical reasoning. In
addition, it is possible to analyze intuitive wrong answers, which offer insights into how
often automatic thinking dominates deliberative thinking.

We employed Confirmatory Factor Analysis for the Cognitive Reflection Test, retained
only five items that had high loadings, and improved the psychometric properties of these
instruments. The final instruments are provided in Appendix C.

3.9. Cognitive Biases

We also included four cognitive biases to test if they are related to financial literacy
(core competencies), financial vulnerability, and financial fraud. Our hypothesis is that if
respondents are prone to cognitive biases then they may have lower financial literacy or be
more likely to have financial vulnerability or financial fraud problems [40]. Taking cognitive
biases into consideration may help us to understand why so many people may have
difficulties in avoiding financial troubles or financial fraud. Cognitive biases are related to
behaviors that deviate from rationality and therefore may explain these financial outcomes.
The items were developed based on the premises of behavioral economics and explore
the general characteristics of behavior in addition to specific biases that are fundamen-
tal to financial decisions, such as loss aversion, herd behavior, myopic behavior, and
hyperbolic discounting.

• Aversion to loss:

Loss aversion is the cognitive bias that explains why individuals feel the pain of loss
twice as intensely as the satisfaction generated by a gain of equal value [38]. This
bias directly affects individuals’ financial decisions, from their investment choices to
the choice of which groceries to buy at the supermarket [61]. This is because people
affected by this bias will focus more on potential costs and failures than on potential
gains and benefits [62,63].

• Herd behavior:

Herd behavior refers to the tendency of individuals to follow the actions or decisions
of a group, even though these choices may be irrational or inconsistent with their own
preferences. This behavior is influenced by the belief that the actions of the majority
reflect superior information or decisions, leading individuals to ignore their own
judgments, something reinforced by factors such as social pressure and the search for
validation [64,65]. In the financial context, its implications are significant: collective
decisions, such as mass asset sales or purchases, can create economic bubbles or
crises [66]. Thus, herd behavior not only reduces the diversity of decisions but also
contributes to volatility and systemic risks in financial markets.
Short-sighted behavior:

•

---

<!-- PAGE 11 -->

Sustainability 2025, 17, 9219

11 of 33

Short-sighted behavior is marked by an exaggerated focus on immediate rewards,
which can lead to impulsive decisions, such as impulse purchases and procrastination,
prioritizing momentary satisfactions that can cause future regrets [67]. People affected
by this bias tend to see only isolated parts of a situation, which makes them ignore
the situation as a whole, leading them to decisions that lead to reduced gains at the
expense of greater opportunities [68].

• Hyperbolic discount:

Hyperbolic discounting refers to the tendency to undervalue future rewards to the
detriment of immediate ones [69]. Behavior like this has a significant impact on
financial decisions, causing people to opt for immediate benefits, such as impulse
purchases, rather than long-term beneficial choices, such as saving for retirement or
investments [70,71]. This type of behavior can lead to financial problems, such as debt
and lack of planning [72]. Understanding hyperbolic discounting and looking for
ways to overcome it is key to improving personal and social financial stability.

3.10. Multiple Linear Regression

We used Ordinary Least Squares (OLS) to investigate the relationship between vari-
ables. This is a widely used statistical method to estimate the coefficients of a linear regres-
sion model [73]. The multiple linear regression model was applied to explain the following
dependent variables: financial literacy (FL), financial vulnerability (FV), and financial fraud
(FF). All regressions were estimated with robust standard errors for heteroskedasticity, and
the results are displayed in Appendix A.

In our modeling strategy, we first assessed the predictors of financial literacy (FL),
which includes the Cognitive Reflection Test (CRT). Subsequently, we used the resulting FL
score, alongside other variables, to predict both financial vulnerability (FV) and financial
fraud (FF).

One of our key objectives here is to assess whether knowledge-based or behavior-based
dimensions of financial literacy have a more substantial impact. As such, we deliberately
looked at these factors individually. We frame our methodology with the following reasoning:

Hypothesis 1: We hoped to determine if the behavioral dimension (financial planning) would be a
better predictor than the knowledge dimension for financial results (fraud and vulnerability).

To distinguish this effect, we examined the dimensions individually.
Our general multiple linear regression model can be represented mathematically as:

FLi = βFL

FVi = βFV

FFi = βFF

2 Femalei + βFL
7 Oldi + βFL
12 Discounti + βFL
2 FPi + βFV
7 Other Racei + βFV

0 + βFL
+ βFL
+ βFL
0 + βFV
+ βFV
+ βFV
+ βFV
0 + βFF
+ βFF
+ βFF
+ βFF

1 CRTi + βFL
6 Youngi + βFL
11 Myopici + βFL
1 FLi + βFV
6 Blacki + βFV
11 HighIncomei + βFV
15 Herdingi + εi,FV,
1 FLi + βFF
6 Blacki + βFF
11 HighIncomei + βFF
15 Herdingi + εi,FF,

3 NonBinaryi + βFL

4 Blacki + βFL
9 HighIncomei + βFL

5 Other Racei

10 LossAversioni

8 LowIncomei + βFL

13 Herdingi + εi,FL,

3 Cryptoi + βFV

4 Femalei + βFV

5 NonBinaryi

12 LossAversioni + βFV

8 Youngi + βFV

9 Oldi + βFV
13 Myopici + βFV

10 LowIncomei
14 Discounti

3 Cryptoi + βFF

2 FPi + βFF
7 Other Racei + βFF

8 Youngi + βFF

4 Femalei + βFF

5 NonBinaryi

9 Oldi + βFF
13 Myopici + βFF

10 LowIncomei
14 Discounti

12 LossAversioni + βFF

The independent variables used in the models are defined as follows:

(1)

(2)

(3)

---

<!-- PAGE 12 -->

Sustainability 2025, 17, 9219

12 of 33

FL—Latent variable for financial literacy measured by four observed indicators;
FP—Latent variable for financial planning measured by six observed indicators;
Crypto—Latent variable for cryptocurrency knowledge measured by four observed

indicators;

CRT—Refers to the Cognitive Reflection Test, which measures the respondent’s ability

to override intuitive but incorrect answers with reflective and accurate reasoning;

Female—Represents the gender of the respondent, is a dummy variable equal to 1 if

the respondent identifies as female;

NonBinary—Represents the gender of the respondent, is a dummy variable equal to 1

if the respondent identifies as nonbinary;

Black—Is a dummy variable equal to 1 if the respondent identifies as Black. For
our analysis, we combined black and mixed-race groups, consistent with previous stud-
ies [74–76];

Other Race—Is a dummy variable equal to 1 if the respondent identifies as being of

Asian descent or Indigenous;

Young—Is a dummy variable equal to 1 if the respondent is between 18 and 30 years old;
Old—Is a dummy variable equal to 1 if the respondent is 56 years old or older;
LowIncome—Is a dummy variable that represents individuals earning up to three times

the minimum wage;

HighIncome—Is a dummy variable representing individuals earning more than

ten times the minimum wage;

LossAversion—Indicates the respondent’s tendency to avoid financial losses;
Myopic—Captures the preference for immediate rewards over long-term benefits,

indicating short-term financial behavior;

Discount—Reflects a preference for consumption rather than saving, indicating a

present-biased preference;

Herding—Measures the tendency to follow the behavior of the majority in financial

decision-making.

3.11. Machine Learning

Machine learning is a subset of artificial intelligence that enables computers to acquire
knowledge and enhance their performance through data. Machine learning models are
algorithms trained on data to identify specific patterns or generate changes in previously
unobserved datasets. A multitude of classification methods have been presented in the
machine learning literature and data science [73].

In this section, we utilize supervised learning techniques [77] to forecast the key
attributes that are important for assessing FL, FV, and FF indices. Initially, we evaluate many
classic machine learning approaches to identify the most appropriate one for our dataset.
This is significant as machine learning models are often employed to make judgments
with tangible real-world implications, particularly in sectors such as healthcare, banking,
criminal justice, and energy [78].

3.11.1. Horse Race

We conducted a competitive evaluation of supervised regressors to identify the optimal
machine learning technique that enhances model performance to explain the average
financial literacy (FL), financial vulnerability (FV), and financial fraud (FF). For modeling we
used the tidymodels framework for R Version 1.4.1, the results are presented in (Figure 2).
K-Nearest Neighbors—The fundamental concept of nearest neighbor methods is to
identify a certain number of training samples that are closest in proximity to a new point
and to predict its label based on those samples. The quantity of samples may be a user-

---

<!-- PAGE 13 -->

Sustainability 2025, 17, 9219

13 of 33

defined constant (k-nearest neighbor learning) or fluctuate according to the local density
of the points (radius-based neighbor learning). The distance can often be any metric
measurement, with the conventional Euclidean distance being the most prevalent option.
Neighbor-based approaches are classified as non-generalizing machine learning techniques,
as they utilize all available training data, potentially organized into an efficient indexing
structure, such as a ball tree or a KD tree [79].

SVMs—These are learning machines for classifying two groups. They map input
vectors nonlinearly to a high-dimensional feature space, where a linear decision surface
is constructed with properties that ensure high generalization capacity. Only the support
vectors, which define the maximum margin of separation between classes, are used to
construct this surface. SVMs use the “kernel trick” to efficiently create nonlinear decision
surfaces in high-dimensional spaces. For non-separable data, they apply soft margins to
allow for controlled errors, increasing robustness [80].

Random Forests—They consist of collections of classifiers that are tree-based, in which
each tree is grown independently by using a random vector. The forests vote by output,
and the generalization error converges without overfitting. Random Forests are also robust
against noise and yield high accuracy with numerous weak and correlated inputs [81].

XGBoost is a type of ensemble learning that uses the Gradient Boosting algorithm. It is
a common choice for many machine learning tasks, especially when it comes to classifying
and regressing structured data. It also lets you use more than one processor to speed up the
training of the model. It boasts considerable speed, precision, and room for growth [80].

A multilayer perceptron (MLP) is a type of neural network that has three layers: input
units, hidden (or internal) units, and output units. The hidden units’ principal job is to
make internal representations of the input patterns. This enables the network to solve
issues that are more complex than those that two-layer networks can handle. The MLP’s
purpose is to learn how to match the input patterns to the output patterns that are wanted,
which will help it make good generalizations [82].

Elastic Net is a penalized regression that outperforms Lasso when more predictors
exist than observations (p > n) or in situations of correlation of predictors. The model
involves both L1 (Lasso) and L2 (Ridge) penalties. For stability and model precision, Elastic
Net chooses more variables and ranks those that exhibit interrelationships among them [83].
Linear regression, being one of the fundamental methods under supervised machine
learning, makes use of one or multiple independent variables to predict a continuously
valued response (the dependent variable). A common method to estimate this model is the
Ordinary Lest Squares (OLS) regression [84].

Figure 2. Horse racing outcomes: On the left, we present the results for financial literacy, financial
vulnerability and financial fraud. The points represent the average RMSE achieved in the fold not
utilized for training throughout 5 separate iterations of our cross-validation. The horizontal bars
represent the 95% confidence interval.

---

<!-- PAGE 14 -->

Sustainability 2025, 17, 9219

14 of 33

The executed model selection approach sought to accurately optimize the distinct
hyperparameter for each utilized machine learning algorithm. The primary criterion for
identifying the optimal hyperparameter configuration was reduction in the Root Mean
Squared Error (RMSE). To achieve this, cross-validation using 5 different folds was used.
The resultant objects encompass the requisite information to iterate over these folds, utiliz-
ing 4 for model training and the remaining 1 for performance assessment, repeating this
process 5 times to ensure each fold serves as an evaluation set once. In general, tree-based
ensemble models exhibit improved performance on the dataset. Given our selection of
RMSE as the performance indicator, we deemed Random Forest the victor of the competi-
tion, due to it achieving the best or similar RMSE to the best-performing methods, but with
a lower standard deviation.

3.11.2. Interpretability Methods

Machine learning interpretability refers to methodologies for elucidating and com-
prehending the mechanisms by which machine learning models generate predictions. As
models increase in complexity, elucidating their internal logic and acquiring insights into
their behavior become paramount [85]. In the absence of interpretability, it becomes chal-
lenging to determine whether a machine learning model is making sound decisions or
exhibiting bias. Explainable Artificial Intelligence (XAI) has been revealed as a viable
solution to the difficulty of interpretability by clarifying the rationale behind the model
predictions [86].

Among the diverse XAI methodologies, Shapley Additive Explanation (SHAP) and
Local Interpretable Model-Agnostic Explanation (LIME) have attained recognition for
providing global and local interpretability. SHAP provides consistent and precise im-
portance values for the characteristics. In contrast, LIME builds local substitute models
that emulate complex classifier behavior, thereby improving the understanding of specific
predictions [87,88]. To elucidate the model’s judgments, we employed two prevalent XAI
methodologies: LIME, which generates local substitute explanations, and SHAP, which
assigns feature attributions based on game theory principles. These elements ensure a
clearer understanding and important predictive potential, essential for transparent results.

4. Results
4.1. Characteristics of the Respondents

Of the 256 respondents, 123 were women (48%), 128 men (50%), and 5 nonbinary
(1.95%). With regard to race/color, based on the principle of self-declaration, the sample is
made up of 100 white people (39.1%), 149 black people (58.2%), 5 yellow people (1.95%)
and 2 indigenous people (0.78%). In terms of income distribution, 100 respondents (39.1%)
earned up to 1 minimum wage (BRL 1320), 79 (30.9%) had an income between 1 and 3
minimum wages (BRL 1320 to 3960), 40 (15.6%) between 3 and 6 minimum wages (R$ 3960
to R$ 7920), 22 (8.59%) between 6 and 9 minimum wages (BRL 7920 to 11,880), 8 (3.12%)
between 10 and 20 minimum wages (BRL 13,200 to R$ 26,400) and 7 (2.73%) earned more
than 20 minimum wages (above BRL 26,400) (Tables 1 and 2).

Table 1. Averages of performance and behavioral variables by gender, race, and income.

Statistic

FL

Crypto

FP

FV

FF

CRT

Discount

Loss
Aversion

Herding

Myopic

Gender
Female
Male
Nonbinary

−0.135
0.0815
−0.103

−0.198
0.330
0.767

−0.132
0.00519
−0.513

0.161
0.00455
0.200

0.0710
0.162
0.661

0.0155
0.170
1.020

30
28
0

63
44
1

31
41
3

40
31
2

---

<!-- PAGE 15 -->

Sustainability 2025, 17, 9219

15 of 33

Table 1. Cont.

Statistic

FL

Crypto

FP

FV

FF

CRT

Discount

Loss
Aversion

Herding

Myopic

Race
Black
White
Other Race

Income
High income
Low income
Middle income

−0.0357
0.00124
−0.214

0.486
−0.0957
0.0509

0.0427
0.131
0.318

0.520
0.0486
0.0837

−0.0371
−0.114
−0.177

0.566
−0.121
−0.0805

0.124
0.0215
0.115

−0.590
0.161
0.0219

0.152
0.0805
0.288

0.0446
0.124
0.161

0.0588
0.180
0.288

0.571
0.0575
0.160

31
26
1

0
49
9

68
38
2

3
77
28

51
22
2

4
54
17

44
27
2

4
53
16

Table 2. Descriptive statistics of the variables.

Statistic

FL

Crypto

FP

FV

FF

CRT

Discount

Mean
Median
Std. Dev.
Variance
Skewness
Kurtosis
Min
Max
Jarque–Bera

−0.0261
−0.0102
0.7142
0.5101
−0.1985
−0.7806
−1.6742
1.5075
7.9143

0.0847
0.0250
0.8164
0.6665
0.6553
−0.4872
−0.8187
2.2870
20.8680

−0.0710
0.0631
0.7724
0.5966
−0.4124
−0.5072
−2.2995
1.3631
9.8786

0.2723
0.2143
0.2320
0.0538
1.1209
0.3486
0.0000
1.0000
55.7425

0.1281
−0.0398
0.6604
0.4362
0.7891
0.0065
−0.8469
2.2812
26.8942

0.1124
−0.0103
0.7091
0.5028
0.7039
−0.3156
−1.0397
2.0727
22.3174

0.2266
0.0000
0.4194
0.1759
1.2988
−0.3144
0.0000
1.0000
73.7376

Loss
Aversion

0.4219
0.0000
0.4948
0.2449
0.3145
−1.9085
0.0000
1.0000
42.7735

Herding

Myopic

0.2930
0.0000
0.4560
0.2080
0.9045
−1.1866
0.0000
1.0000
49.9742

0.2852
0.0000
0.4524
0.2046
0.9461
−1.1091
0.0000
1.0000
51.4175

4.2. Multiple Linear Regression

We used the following as dependent variables: financial literacy (FL), financial vulner-

ability (FV), and financial fraud (FF). The results are displayed in Appendix A.

In the financial literacy analysis, the Cognitive Reflection Test showed a strong positive
relationship (coef. 0.502; p < 0.01), with higher scores reflecting greater knowledge in
financial literacy, demonstrating that more thoughtful people tend to have more knowledge
in this field. Women had lower levels of financial literacy (coef. −0.140; p < 0.1), which
reflects social barriers in access to financial literacy. Individuals with a high income had
higher levels of financial literacy (coef. 0.348; p < 0.1) which can be explained by several
structural, social, and behavioral factors. In the analysis of race, individuals who self-
declared themselves as black or as an other race did not show significant results. Behavioral
characteristics such as loss aversion, myopic behavior, hyperbolic discounting, and herding,
although some showed a positive or negative coefficient, were not statistically significant.
In the analysis of financial vulnerability, individuals with better financial planning
exhibited a strong inverse relationship (coef. −0.797; p < 0.01), indicating that those with
effective financial planning, such as controlling and projecting their finances, are less
financially vulnerable. Individuals who self-identified as black were more financially
vulnerable (coef. 0.156; p < 0.05), showing that race is an important characteristic and that
black people are more financially vulnerable.

For financial fraud outcomes, financial literacy showed a significant negative relation-
ship (coefficient −0.139; p < 0.1), demonstrating that higher levels of financial knowledge
are correlated with a lower susceptibility to financial fraud. Financial planning is shown to
be important for financial vulnerability (coefficient −0.366; p < 0.01), showing that financial
planning is an effective tool in reducing fraud.

The results show that financial literacy and financial planning play a crucial role in

shaping better financial habits, reducing financial vulnerabilities, and preventing fraud.

---

<!-- PAGE 16 -->

Sustainability 2025, 17, 9219

16 of 33

4.3. Results of the Machine Learning Approach

The importance of SHAP measures the influence of each variable on the individual
model prediction. The absolute mean value shows the strength of this influence, regardless
of the sign (positive or negative). The higher the importance value, the more relevant
the variable is to the model’s decisions. The beeswarm plot presents the results for the
dependent variables FL (Figure 3), FV (Figure 4), and FF (Figure 5). The horizontal axis
denotes the SHAP value, while the vertical axis comprises the predictive features. Positive
(negative) SHAP values signify that the feature enhances (diminishes) the target variable.
Each represents a dot for every attribute, which signifies the SHAP value for a particular
instance, indicating the contribution of that attribute to the overall prediction for that
instance. The color of the dot corresponds to the value of the feature, with lighter hues
signifying greater values.

Figure 3. Results of SHAP computed for every attribute over the entire dataset for prediction of
financial literacy (FL).

Figure 4. Results of SHAP computed for every attribute over the entire dataset for prediction of
financial vulnerability (FV).

---

<!-- PAGE 17 -->

Sustainability 2025, 17, 9219

17 of 33

Figure 5. Results of SHAP computed for every attribute over the entire dataset for prediction of
financial fraud (FF).

The importance of LIME measures the influence of each variable on the individual
model prediction. The absolute mean strength shows the influence of each feature. The
higher the importance value, the more relevant the variable is to the model’s decisions. The
LIME plot presents the results for the dependent variables FL (Figure 6), FV (Figure 7),
and FF (Figure 8). Local Interpretable Model-Agnostic Explanation (LIME) represents the
average importance of the variables in the local explanation of the predictions made by the
best model (Random Forest). The X-axis (horizontal): names of the variables (or features),
ordered from most important to least important, and the Y-axis (vertical): average of the
absolute values of the weights attributed to the variables (mean_weight) by LIME in the
explanations. This represents the average contribution of that variable to the predictions.

Figure 6. Results of LIME computed for every attribute over the entire dataset for prediction of
financial literacy (FL).

Financial planning (FP) is the variable that most influences the model, presenting
a strong prediction for financial education, financial vulnerability, and financial fraud.
The significance is very high for both the SHAP and LIME methods. In an analysis of
financial literacy the Cognitive Reflection Test (CRT) is the feature that most influences
both the SHAP and LIME models, confirming the results of the regressions. Being a woman
significantly impacts the predicted result, showing a positive prediction for financial
vulnerability and financial fraud, especially for the prediction of financial literacy, mainly

---

<!-- PAGE 18 -->

Sustainability 2025, 17, 9219

18 of 33

when we look at the LIME results compared to the SHAP results; these values are a
consequence of the different methodologies behind SHAP and LIME. The LIME method
provides information on specific local specifications, while the SHAP method aims at a more
comprehensive and global understanding of resource contributions. Both are valuable, but
we answer different proposed questions about the importance of features. We can highlight
the variables FL, Crypto and Black, which, despite not having great predictive power,
always rank among the top for financial vulnerability and financial fraud modeling. The
other characteristics did not show great significance in our models. It is important to note
that the values for the Nonbinary and Other Race variables are not shown in the results,
due to the small number of samples. When cross-validation is performed on training and
test sets, these groups may end up in only one of these sets, or even in none of the test sets
in certain folds, which is what occurred for the values in question.

Figure 7. Results of LIME computed for every attribute over the entire dataset for the prediction of
financial vulnerability (FV).

Figure 8. Results of LIME computed for every attribute over the entire dataset for prediction of
financial fraud (FF).

These results confirm the regression results, especially when we look at the results of
the SHAP methodology, since this methodology aims at a more comprehensive and global
understanding of the contributions of resources. Both are valuable, but we answer different
proposed questions about the importance of features.

---

<!-- PAGE 19 -->

Sustainability 2025, 17, 9219

19 of 33

5. Discussion

In recent years, Brazil has seen a rise in indebtedness, with 32% of Brazilians having
been in arrears for more than three months, as well as the recurrence of financial scams,
which affect more than 40 million Brazilians [89]. At the same time, research points to the
growing popularity of online sports betting, called “bets”, which is predominantly aimed
at people earning up to two minimum salaries [89]. From this context, and based on the
results of this article, we infer that financial literacy is something that deserves the full
attention of public policymakers.

The recent literature on financial literacy mainly investigates financial literacy and
retirement planning; the intersection of financial risk management; and the impact of behav-
ioral finance and psychological factors [90]. In line with the discussion in the international
literature, our results showed that people with greater financial literacy have better financial
habits, which lead them to practices that reduce their level of debt, motivating an increase
in financial reserves and, consequently, the ability to deal with unexpected expenses and
even economic instability. Financial literacy combined with appropriate financial behavior
contributes to individual and family financial security and favors economic growth and
stability [91].

Emerging economies like Brazil are more vulnerable to economic instability and shocks.
The Getulio Vargas Foundation’s Economic Uncertainty Indicator (IIE-Br) rose by 4.6 points
in April 2025, totaling 115.5 points [92], which reinforces the need for a population capable
of dealing with economic instability, something that is only feasible through a good degree
of literacy and positive financial habits. The literature shows that people with greater
financial literacy have greater access to formal financial systems and use them sparingly,
reducing the likelihood of being exposed to any degree of financial vulnerability [93].

The development of new, innovative instruments that assess financial literacy, financial
planning, and cryptocurrency literacy is intended to address substantive gaps in the
prevailing literature. Policymakers will now be able to measure financial literacy and
related concepts in a more efficient and comprehensive manner, while being in a position
to design and deliver interventions that are empirically grounded. The imperative of
developing this tool arises due to the complicated nature of the construct and financial
literacy’s central role in personal as well as communal economic stability, whereby there
must be intermixing of basic financial competency with attitudes, behaviors, and contextual
factors, such as exposure to socioeconomic vulnerability, that have a direct influence
upon individuals’ health, well-being, and financial stability [91]. In hypothesizing and
crafting our approach, not only has there been a step up in scholarly work in academia,
but financial literacy’s status as a complicated construct has also been acknowledged. This
facilitates the evidence-based promotion of effective interventions, as well as a decrease in
vulnerability [1,23].

In line with the international literature, our results show that in the Federal District,
financial literacy plays an important role in developing better financial habits among the
population. However, for the sample analyzed, the data show that theoretical knowledge
alone does not guarantee the mitigation of financial vulnerabilities, nor even the prevention
of fraud. This type of finding converges with other studies that highlight the importance
of an integrated approach that considers not only knowledge, but also the practices and
social context of individuals [18,19,35]. Accordingly, financial behavior emerged as the
most consistent dimension in explaining the positive outcomes of the sample. This di-
mension, therefore, shows that skills such as spending control, financial planning, and
behavioral resilience are essential for reducing vulnerability and strengthening financial
security [20,68].

---

<!-- PAGE 20 -->

Sustainability 2025, 17, 9219

20 of 33

The analysis also revealed significant inequalities in the levels of financial literacy
between the different groups in the sample. Individuals with high income, for example,
had higher levels of financial literacy, reflecting structural and cultural barriers to accessing
financial literacy and other formal economic resources. This type of inequality, which has
already been demonstrated in other studies [25,29], is even more critical in Brazil, a country
characterized by high income inequality and financial exclusion, especially among the
low-income population [3,4]. These results highlight the need for intersectional public
policies, that is, policies that take into account the socioeconomic and cultural particularities
of the most vulnerable groups.

Our findings confirm our hypothesis: planning has much stronger predictive ability.
As a matter of theoretical interest but also because such a composite aggregated index
would suppress an important difference, we performed such an exercise as a robustness
check. The results, which we document in Appendix B, confirm our major results and
support our initial hypothesis. We carried out an assessment with a composite index to
confirm our methodology. The results procured were consistent with our main findings
and available in Appendix B.

5.1. Implications for Sustainable Development

We found lower financial literacy for women, compared to male respondents, and
greater vulnerability among black individuals. These results demonstrate not only impor-
tant economic issues, but also issues of social injustice that undermine social sustainability.
In Brazil, there are already racial quota policies for black people to access public universities.
Public policies that address racial injustices are important to tackle issues of vulnerability
and financial fraud. Future research could assess whether algorithms may be being used to
defraud people of specific races due to greater vulnerability.

Greater financial vulnerability leads to families experiencing greater instability in their
savings. It causes them to seek access to credit that can be predatory, with high interest rates.
It can also lead to difficulty in withstanding adverse economic shocks. These weaknesses
should be addressed at the macroeconomic level, which underscores the importance of
enhancing financial planning, as well as household resilience, in order to build a more
stable and sustainable national economy (this point is closely related to SDG 8: Decent
Work and Economic Growth).

Our main finding is that financial planning and behaviors are more critical than
knowledge (as measured by the financial literacy instrument, which encompasses only
basic knowledge). Similarly, environmental knowledge does not necessarily lead people
to behave in a pro-environmental way. Thus, financial knowledge does not guarantee the
financial well-being of families. Thus, a key finding of our study is that sustainable out-
comes depend on fostering or stimulating long-term thinking and behavioral changes. Our
results suggest important avenues for developing public policies that are more inclusive
and aim to foster behavioral change. Future research could investigate this relationship
by evaluating the impact of nudges on increasing people’s financial well-being, reducing
vulnerabilities, and promoting more sustainable behaviors.

5.2. Machine Learning Discussion

Machine learning systems help people and institutions better understand data and
identify important patterns within it. This information is crucial for decision-making and
planning. Therefore, it is important to understand the principles of machine learning
algorithms and their applicability in various real-world application areas, such as security
services, healthcare, economic data, context-aware systems, sustainable agriculture, and
many others [94]. Choosing the best machine learning model can be quite a daunting task.

---

<!-- PAGE 21 -->

Sustainability 2025, 17, 9219

21 of 33

Typically, when creating a model, we choose the algorithm that performs best for the data
in question. To support this, we use a methodology that is becoming widespread when
comparing machine learning models in a horse race to choose which model is best [95]. The
best model evaluated was Random Forest, a highly effective machine learning algorithm
that excels at modeling nonlinear relationships and providing the importance of each
variable [96].

Ease of interpreting results is paramount, as social researchers are primarily concerned
with understanding complex social specificity, testing theories, and drawing explanatory
conclusions from their data. Their expertise lies in their respective fields, not necessarily in
advanced computer programming or algorithm development, to have a better interpreta-
tion of the results using SHAP and LIME, which are two prominent techniques in the field
of Explainable AI (XAI), addressing the “black box” problem of complex machine learning
models, helping researchers understand why a certain discovery was made.

6. Final Considerations

The results highlight the need for comprehensive initiatives that address not only
the fundamentals of financial knowledge but also the understanding and development
of individuals’ behaviors and attitudes. Public policies aimed at promoting financial
inclusion, for example, should incorporate financial literacy programs adapted to different
audiences. This adaptation must also consider other social factors, such as sex, race, and
income. Another key point lies in the integration of technological tools and innovative
methodologies, such as the instrument developed in this study, which can significantly
contribute to enhancing the effectiveness and reach of these initiatives.

One possible limitation of the study is that we focus on respondents from the Federal
District of Brazil. Although a potential shortcoming involves the use of participants drawn
from the Federal District, sample heterogeneity regarding income, education, and racial
background allowed us to gain insight into the associations among these fundamental
demographic factors and financial literacy. Future studies may consider how inter-regional
variations affect financial literacy and its correlation with cognitive biases, among other
factors. One of the fundamental questions of research is whether there is generalizability
in such findings and whether there is a potential contribution of cultural variations in
this regard.

It is essential to highlight that our results do not necessarily imply a direct cause-and-
effect relationship. However, our results indicate that enhancing financial literacy and
mitigating financial vulnerabilities present relevant drivers that are consistent with the
broad goals of sustainable development.

Author Contributions: Conceptualization, B.M.T. and D.H.C.; Methodology, B.M.T., D.H.C. and
C.C.S.; Software, B.M.T. and C.C.S.; Formal analysis, B.M.T., D.H.C. and C.C.S.; Investigation, B.M.T.
and D.H.C.; Data curation, D.H.C. and C.C.S.; Writing—original draft, B.M.T., D.H.C. and C.C.S.;
Writing—review & editing, B.M.T., D.H.C. and C.C.S. All authors have read and agreed to the
published version of the manuscript.

Funding: This research was funded by Fundação de Apoio à Pesquisa do Distrito Federal—FAP-
DF—under the name ‘Alfabetização Financeira e Vieses Cognitivos: o caso do Distrito Federal
00193-00000273/2023-01’. BMT gratefully acknowledges financial support from FAP-DF, CAPES
(Experimental Laboratory in Public Policy—LAB-LEPP), and CNPq (grant). DCS and TCS gratefully
acknowledge financial support from FAP-DF.

Institutional Review Board Statement: The study was conducted according to the guidelines of
the Declaration of Helsinki, and approved by the Ethics Committee of Getulio Vargas Foundation
(protocol code P.421.2023 and date of approval is 24 October 2023).

---

<!-- PAGE 22 -->

Sustainability 2025, 17, 9219

22 of 33

Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.

Data Availability Statement: The data are available upon request from the authors.

Acknowledgments: The authors used GenAI, DeepL, and Grammarly to improve the readability and
clarity of the text. The entire text has been reviewed and approved by the authors, who assume full
responsibility. We thank the four anonymous reviewers and the editor, who have helped improve
the paper.

Conflicts of Interest: The authors declare no conflicts of interest. The funders had no role in the design
of the study; in the collection, analysis, or interpretation of data; in the writing of the manuscript; or
in the decision to publish the results.

Appendix A. Regression Results

Table A1. Dependent variables: FL Broad, FV, and FF.

FL Broad (HC3)
(1)

FV (HC3)
(2)

FF (HC3)
(3)

CRT

FL

FP

Crypto

Female

NonBinary

Black

Other Race

Young

Old

Low Income

High Income

Loss Aversion

Myopic

Discount

Herding

0.502 ***
(0.057)

−0.140 *
(0.083)
−0.709
(0.454)
0.010
(0.088)
−0.315
(0.395)
0.025
(0.100)
−0.063
(0.143)
−0.071
(0.106)
0.348 *
(0.195)

0.014
(0.084)
0.055
(0.088)
−0.111
(0.097)
−0.064
(0.086)

0.053
(0.071)
−0.797 ***
(0.055)
−0.046
(0.045)
0.053
(0.074)
−0.176
(0.286)
0.156 **
(0.073)
0.127
(0.143)
−0.017
(0.089)
−0.087
(0.114)
0.096
(0.096)
−0.113
(0.133)

−0.096
(0.073)
0.016
(0.082)
−0.028
(0.084)
0.064
(0.077)

−0.139 *
(0.078)
−0.366 ***
(0.071)
0.079
(0.054)
−0.117
(0.079)
0.243
(0.402)
0.091
(0.076)
0.0002
(0.285)
−0.104
(0.103)
−0.056
(0.154)
−0.027
(0.102)
0.127
(0.220)

−0.064
(0.074)
0.046
(0.082)
−0.006
(0.092)
−0.008
(0.083)

---

<!-- PAGE 23 -->

Sustainability 2025, 17, 9219

23 of 33

Table A1. Cont.

FL Broad (HC3)
(1)

Constant

Observations
R2
Adjusted R2
Residual Std. Error
F Statistic

0.046
(0.119)

256
0.320
0.284
0.604
8.771 ***

FV (HC3)
(2)

−0.100
(0.095)

256
0.594
0.569
0.527
23.430 ***

FF (HC3)
(3)

0.188 *
(0.108)

256
0.304
0.261
0.568
6.992 ***

Note: Robust standard errors in parentheses. * p < 0.1; ** p < 0.05; *** p < 0.01.

Appendix B. FL_Broad Factor Index

We constructed the FL_Broad factor index, which comprises an aggregate index that
encompasses financial literacy (basic knowledge of finance), knowledge about cryptocurren-
cies (Crypto), and financial attitudes regarding financial planning (Financial Planning—FP).

FL_Broad =

FL + FP + Crypto
3

Our general multiple linear regression model can be represented mathematically as:

FL_Broadi = βFL

CRTi + βFL_Broad
2

Blacki + βFL_Broad
5
LowIncomei + βFL_Broad
Myopici + βFL_Broad

9

Femalei + βFL_Broad
Other Racei + βFL_Broad

3

6

NonBinaryi
Youngi + βFL_Broad

7

Oldi

HighIncomei + βFL_Broad

LossAversioni
10
Herdingi + εi,FL_Broad,

FVi = βFV

12
2 Femalei + βFV
1 FL_Broadi + βFV

Discounti + βFL_Broad
13
3 NonBinaryi

5 Other Racei + βFV

6 Youngi + βFV

10 LossAversioni + βFV

7 Oldi + βFV
11 Myopici + βFV

8 LowIncomei
12 Discounti

FFi = βFF

1 FL_Broadi + βFF

2 Femalei + βFF

3 NonBinaryi

5 Other Racei + βFF

6 Youngi + βFF

10 LossAversioni + βFF

7 Oldi + βFF
11 Myopici + βFF

8 LowIncomei
12 Discounti

0 + βFL_Broad
1
+ βFL_Broad
4
+ βFL_Broad
8
+ βFL_Broad
11
0 + βFV
+ βFV
+ βFV
+ βFV
0 + βFF
+ βFF
+ βFF
+ βFF

4 Blacki + βFV
9 HighIncomei + βFV
13 Herdingi + εi,FV,

4 Blacki + βFF
9 HighIncomei + βFF
13 Herdingi + εi,FF,

(A1)

(A2)

(A3)

Table A2. Regression results: dependent variables: FL_Broad, FV, and FF.

FL_Broad (HC3)
(1)

FV (HC3)
(2)

FF (HC3)
(3)

C_R

FL_Broad

Female

NonBinary

0.363 ***
(0.046)

−0.220 ***
(0.061)
−0.631 *
(0.371)

−0.917 ***
(0.072)
−0.066
(0.085)
0.088
(0.372)

−0.516 ***
(0.075)
−0.209 ***
(0.080)
0.389
(0.382)

---

<!-- PAGE 24 -->

Sustainability 2025, 17, 9219

24 of 33

Table A2. Cont.

Black

Other Race

Young

Old

Low Income

High Income

Loss Aversion

Myopic

Discount

Herding

Constant

Observations
R2
Adjusted R2
Residual Std. Error
F Statistic

FL_Broad (HC3)
(1)

0.020
(0.066)
−0.104
(0.319)
0.187 **
(0.075)
−0.006
(0.107)
−0.069
(0.079)
0.369 **
(0.154)
−0.054
(0.061)
0.091
(0.066)
−0.147 **
(0.070)
−0.012
(0.069)
0.013
(0.087)

256
0.388
0.355
0.459
11.799 ***

FV (HC3)
(2)

0.090
(0.083)
0.088
(0.240)
0.040
(0.108)
−0.169
(0.137)
0.044
(0.106)
−0.215
(0.179)
−0.209 **
(0.081)
−0.008
(0.089)
−0.055
(0.095)
0.109
(0.092)
0.105
(0.111)

256
0.439
0.409
0.617
14.560 ***

FF (HC3)
(3)

0.057
(0.083)
0.034
(0.244)
−0.034
(0.108)
−0.094
(0.160)
−0.052
(0.104)
0.071
(0.230)
−0.148 *
(0.077)
0.047
(0.086)
−0.031
(0.099)
0.039
(0.090)
0.293 **
(0.115)

256
0.206
0.164
0.604
4.841 ***

Note: Robust standard errors in parentheses. * p < 0.1; ** p < 0.05; *** p < 0.01.

Appendix C. Measurement Model Equations for the Confirmatory Factor
Analysis (CFA)

Appendix C.1. Confirmatory Factor Analysis

We implemented a Confirmatory Factor Analysis to evaluate the reliability and validity
of our latent factors (Rosseel [97]). We modeled six latent factors: (i) the financial literacy
(FL) scale, which measures core knowledge; (ii) the financial vulnerability (FV) scale, which
measures if the respondent is not able to pay their bills (an outcome scale); (iii) the financial
fraud scale (FF), which has four items that evaluate if the respondent has been victimized
by financial fraud; (iv) the Cognitive Reflection Test (CR), which evaluates if the respondent
uses intuition or rationality to answer the questions; (v) the cryptocurrency literacy scale
(CRY); and (vi) the financial planning (FP) scale, which measures if the respondent is prone
to financial planning.

Appendix C.2. Notation

Let:

•

η (eta) represent a latent variable (factor).

---

<!-- PAGE 25 -->

Sustainability 2025, 17, 9219

25 of 33

•
•

•

x represent an observed variable (indicator).
λ (lambda) represent the factor loading, which measures the strength of the relation-
ship between the observed variable and its respective latent factor.
ϵ (epsilon) represent the measurement error associated with each observed variable.

Appendix C.3. Measurement Equations

Appendix C.3.1. Financial Literacy (FL)

The latent variable for financial literacy (ηFL) is measured by four observed indicators:

xFL1 = λFL1,FL · ηFL + ϵFL1
xFL2 = λFL2,FL · ηFL + ϵFL2
xFL4 = λFL4,FL · ηFL + ϵFL4
xFL6 = λFL6,FL · ηFL + ϵFL6

Appendix C.3.2. Financial Vulnerability (FV)

The latent variable for financial vulnerability (ηFV) is measured by fourteen observed

indicators:

xFV1 = λFV1,FV · ηFV + ϵFV1
xFV2 = λFV2,FV · ηFV + ϵFV2
xFV3 = λFV3,FV · ηFV + ϵFV3
xFV4 = λFV4,FV · ηFV + ϵFV4
xFV5 = λFV5,FV · ηFV + ϵFV5
xFV6 = λFV6,FV · ηFV + ϵFV6
xFV7 = λFV7,FV · ηFV + ϵFV7
xFV8 = λFV8,FV · ηFV + ϵFV8
xFV9 = λFV9,FV · ηFV + ϵFV9
xFV10 = λFV10,FV · ηFV + ϵFV10
xFV11 = λFV11,FV · ηFV + ϵFV11
xFV12 = λFV12,FV · ηFV + ϵFV12
xFV13 = λFV13,FV · ηFV + ϵFV13
xFV14 = λFV14,FV · ηFV + ϵFV14

Appendix C.3.3. Financial Fraud (FF)

The latent variable for financial fraud (ηFF) is measured by four observed indicators:

xFF1 = λFF1,FF · ηFF + ϵFF1
xFF2 = λFF2,FF · ηFF + ϵFF2
xFF3 = λFF3,FF · ηFF + ϵFF3
xFF4 = λFF4,FF · ηFF + ϵFF4

---

<!-- PAGE 26 -->

Sustainability 2025, 17, 9219

26 of 33

Appendix C.3.4. Cognitive Reflection Test (CR)

The latent variable for Cognitive Reflection (ηCR) is measured by five observed indicators:

xCR1 = λCR1,CR · ηCR + ϵCR1
xCR2 = λCR2,CR · ηCR + ϵCR2
xCR3 = λCR3,CR · ηCR + ϵCR3
xCR5 = λCR5,CR · ηCR + ϵCR5
xCR7 = λCR7,CR · ηCR + ϵCR7

Appendix C.3.5. Cryptocurrency Knowledge (CRY)

The latent variable for cryptocurrency knowledge (ηCRY) is measured by four observed

indicators:

xCrypto1 = λCrypto1,CRY · ηCRY + ϵCrypto1
xCrypto2 = λCrypto2,CRY · ηCRY + ϵCrypto2
xCrypto3 = λCrypto3,CRY · ηCRY + ϵCrypto3
xCrypto4 = λCrypto4,CRY · ηCRY + ϵCrypto4

Appendix C.3.6. Financial Planning (FP)

The latent variable for financial planning (ηFP) is measured by six observed indicators:

xFP1 = λFP1,FP · ηFP + ϵFP1
xFP2 = λFP2,FP · ηFP + ϵFP2
xFP3 = λFP3,FP · ηFP + ϵFP3
xFP4 = λFP4,FP · ηFP + ϵFP4
xFP5 = λFP5,FP · ηFP + ϵFP5
xFP6 = λFP6,FP · ηFP + ϵFP6

Given that the survey items were measured on an ordered categorical scale (dichoto-
mous or Likert-type), we performed the analysis using the polychoric correlation matrix
and the robust Diagonally Weighted Least Squares (DWLS) estimator. We based the eval-
uation of the model on the usual global fit indices, as well as reliability, convergent, and
discriminant validity assessments.

Appendix C.3.7. Overall Model Fit

Our CFA model shows an excelent fit to the data. The robust Comparative Fit Index
(CFI = 0.954) and Tucker–Lewis Index (TLI = 0.950) exceed the 0.95 threshold, which
indicates a strong correspondence between our model and the data. Also, the Root Mean
Square Error of Approximation (known as RMSEA = 0.039) was well below the 0.06 cutoff
for a close fit, with a 90% confidence interval of [0.032, 0.045] that further supports our
conclusion. While these indices suggest a perfect global model fit, the Standardized Root
Mean Square Residual (SRMR = 0.114) is elevated above the recommended maximum of
0.08. This result may suggest that while the overall model structure is sound, there may be
some localized areas of misfit.

Appendix C.3.8. Reliability and Convergent Validity

The internal consistency and convergent validity of the six factors were assessed.
Composite Reliability (CR) scores indicated good to excellent reliability for the majority

---

<!-- PAGE 27 -->

Sustainability 2025, 17, 9219

27 of 33

of the factors: financial vulnerability (CR = 0.950), financial fraud (CR = 0.803), Cognitive
Reflection Test (CR = 0.844), cryptocurrency literacy (CR = 0.955), and financial planning
(CR = 0.845), all of which were well above the > 0.70 threshold. The financial literacy factor
(CR = 0.695) demonstrated borderline but acceptable reliability.

Convergent validity, as estimated by the Average Variance Extracted (AVE), regis-
tered strong levels in four of six factors, all of which exceeded the >0.50 threshold: fi-
nancial vulnerability (AVE = 0.581), financial fraud (AVE = 0.511), Cognitive Reflection
Test (AVE = 0.531), and cryptocurrency literacy (AVE = 0.841). On the contrary, while the
financial planning factor (AVE = 0.481) and the financial literacy factor (AVE = 0.370) failed
to pass this test, this means that such constructs share less than 50% of the variance of their
respective indications in mean terms. However, upon consideration of parameter estimates,
it emerged that all of the individual factor loadings were significant statistically (p < 0.001)
with most of them showing substantively large magnitudes.

Appendix C.3.9. Discriminant Validity

We find strong evidence for discriminant validity, which helps confirm that the
six latent constructs can be seen as empirically distinct from one another. First, the Fornell–
Larcker criterion was met for all pairs of factors; the square root of the AVE (AVE) for each
construct was greater than its correlation with any other construct. Second, a more stringent
test using the Heterotrait–Monotrait Ratio of Correlations (HTMT) further supported these
findings. The highest observed HTMT value was 0.599 (between FV and FP), which is
well below the conservative threshold of <0.85, which provides robust evidence for the
discriminant validity of all of the factors in our model.

Appendix C.3.10. Conclusion on Measurement Model Quality

We conclude, using the Confirmatory Factor Analysis, that our proposed six-factor
structure of the measurement instrument fits the data well on a global level, and the
constructs demonstrate excellent discriminant validity and generally high reliability. These
results suggest the model has a firm foundation.

Figure A1. Path diagram of the final six-factor Confirmatory Factor Analysis (CFA) model.
Ovals represent latent factors and rectangles represent observed indicators. Path values are
standardized estimates.

---

<!-- PAGE 28 -->

Sustainability 2025, 17, 9219

28 of 33

Table A3. Model fit indices and latent factor correlations for the six-factor CFA model.

χ2 (df)

849.845 *** (614)

Part A: Goodness-of-Fit Indices

CFI

0.954

TLI

0.950

RMSEA [90% CI]

SRMR

0.039 [0.032, 0.045]

0.114

Part B: Latent Factor Standardized Correlations

Factor

1.

2.

3.

4.

5.

6.

1. Financial Literacy (FL)
2. Financial Vulnerability (FV)
3. Financial Fraud (FF)
4. Cognitive Reflection Test (CR)
5. Cryptocurrency Literacy (CRY)
–
6. Financial Planning (FP)
0.139
Note. N = 256. Fit indices are based on the robust DWLS estimator. * p < 0.05, ** p < 0.01, *** p < 0.001.

–
−0.380 ***
−0.292 *
0.415 ***
0.135
0.522 ***

–
0.469 ***
−0.222 **
−0.146
−0.642 ***

–
0.021
0.021
−0.375 ***

–
0.274 **
0.217 *

–

Table A4. Standardized Factor Loadings (λ), Composite Reliability (CR), and Average Variance
Extracted (AVE).

Construct

Financial Literacy (F L)
CR = 0.695, AVE = 0.370

Financial Vulnerability (FV )
CR = 0.950, AVE = 0.581

Financial Fraud (FF)
CR = 0.803, AVE = 0.511

Cognitive Reflection Test (CR)
CR = 0.844, AVE = 0.531

Cryptocurrency Literacy (CRY)
CR = 0.955, AVE = 0.841

Item

Standardized Loading (λ)

FL1
FL2
FL4
FL6

FV1
FV2
FV3
FV4
FV5
FV6
FV7
FV8
FV9
FV10
FV11
FV12
FV13
FV14

FF1
FF2
FF3
FF4

CR1
CR2
CR3
CR5
CR7

Crypto1
Crypto2
Crypto3
Crypto4

0.671
0.435
0.585
0.707

0.780
0.778
0.851
0.829
0.829
0.778
0.733
0.839
0.869
0.816
0.716
0.493
0.665
0.592

0.673
0.530
0.807
0.812

0.979
0.644
0.764
0.633
0.547

0.888
0.903
0.968
0.907

---

<!-- PAGE 29 -->

Sustainability 2025, 17, 9219

29 of 33

Table A4. Cont.

Construct

Financial Planning (FP)
CR = 0.845, AVE = 0.481

Item

Standardized Loading (λ)

FP1
FP2
FP3
FP4
FP5
FP6

0.791
0.614
0.591
0.608
0.711
0.811

Note. All factor loadings are statistically significant at p < 0.001.

Table A5. Construct reliability and convergent validity statistics.

Factor

Composite Reliability (CR)

Average Variance Extracted (AVE)

FL
FV
FF
CR
CRY
FP
Note. Thresholds for good psychometric properties are typically CR > 0.70 and AVE > 0.50.

0.370
0.581
0.511
0.531
0.841
0.481

0.695
0.950
0.803
0.844
0.955
0.845

The results from the Fornell–Larcker criterion analysis provide strong evidence for
the discriminant validity of the six-factor model. As shown in the table, the square root of
the AVE for each latent construct was greater than its correlation with any other construct,
indicating that each factor is statistically distinct.

Table A6. Discriminant validity assessment using the Fornell–Larcker criterion.

Factor

FL

FV

FF

CR

CRY

FP

0.609
−0.380
−0.292
0.415
0.135
0.522

FL
FV
FF
CR
CRY
FP
0.693
Note. Diagonal elements (in bold) are the square root of the Average Variance Extracted (AVE). For discrimi-
nant validity, diagonal elements must be greater than the off-diagonal correlations in the corresponding rows
and columns.

0.762
0.469
−0.222
−0.146
−0.642

0.715
0.021
0.021
−0.375

0.729
0.274
0.217

0.917
0.139

References

1.

2.

3.

4.

5.

6.

Lusardi, A.; Mitchell, O.S. Financial Literacy and Planning: Implications for Retirement Wellbeing. In The Routledge Handbook of
Financial Literacy; Oliver, B.; Young, C., Eds.; Routledge: New York, NY, USA, 2014.
Van Rooij, M.; Lusardi, A.; Alessie, R. Financial literacy and retirement planning in the Netherlands. J. Econ. Psychol. 2011,
32, 593–608. [CrossRef]
Batinga, G.L.; Castro, A.S.; Almeida, L.K.d.S.D. Educação Financeira, Condição Sociocultural e Vulnerabilidade: uma análise
da saúde e bem-estar financeiro de famílias monoparentais femininas. In Proceedings of the Anais do Encontro da Associação
Nacional de Pós-Graduação e Pesquisa em Administração, ANPAD, Fortaleza, Brazil, 16–18 May 2019.
Camargo, R.Z.; Junior, M.F.; Strehlau, S. Vulnerabilidade e Educação Financeira: A Visão de Gerentes de Banco; Revista Interdisciplinar
de Marketing: São Paulo, Brazil, 2020.
Banco Central do Brasil. Relatório de Letramento Financeiro. 2023. Available online: https://www.bcb.gov.br/content/
cidadaniafinanceira/documentos_cidadania/letramento/relatorio-de-letramento-financeiro.pdf (accessed on 23 June 2025).
Akande, J.; Hosu, Y.; Kabiti, H.; Ndhleve, S.; Garidzirai, R. Financial literacy and inclusion for rural agrarian change and
sustainable livelihood in the Eastern Cape, South Africa. Heliyon 2023, 9, e16330. [CrossRef]

---

<!-- PAGE 30 -->

Sustainability 2025, 17, 9219

30 of 33

7.

8.

9.

Zaimovic, A.; Torlakovic, A.; Arnaut-Berilo, A.; Zaimovic, T.; Dedovic, L.; Nuhic Meskovic, M. Mapping financial literacy:
A systematic literature review of determinants and recent trends. Sustainability 2023, 15, 9358. [CrossRef]
UN Capital Development Fund (UNCDF). Financial Inclusion and the SDGs. Available online: https://www.uncdf.org/financial-
inclusion-and-the-sdgs?ref=hackernoon.com (accessed on 20 April 2025).
Kyeyune, G.N.; Ntayi, J.M. Empowering rural communities: The role of financial literacy and management in sustainable
development. Front. Hum. Dyn. 2025, 6, 1424126. [CrossRef]
Swiecka, B.; Ye¸silda ˘g, E.; Özen, E.; Grima, S. Financial literacy: The case of Poland. Sustainability 2020, 12, 700. [CrossRef]

10.
11. Garg, N.; Singh, S. Financial literacy among youth. Int. J. Soc. Econ. 2016, 45, 173–186. [CrossRef]
12. Goyal, K.; Kumar, S. Financial literacy: A systematic review and bibliometric analysis. Int. J. Consum. Stud. 2020, 45, 173–186.

[CrossRef]

13. Anshika.; Singla, A. Financial literacy of entrepreneurs: A systematic review. Manag. Financ. 2021, 48, 1352–1371. [CrossRef]
14. Haag, L.; Brahm, T. The Gender Gap in Economic and Financial Literacy: A Review and Research Agenda. Int. J. Consum. Stud.

2025, 49, e70031. [CrossRef]

15. Negi, P.; Jaiswal, A. Impact of financial literacy on consumer financial behavior: A systematic review and research agenda using

TCCM framework. Int. J. Consum. Stud. 2024, 48, e13053. [CrossRef]

16. Atkinson, A.; Messy, F.A. Measuring Financial Literacy: Results of the OECD/International Network on Financial Education (INFE) Pilot
Study; Technical Report 15, OECD Working Papers on Finance, Insurance and Private Pensions; OECD Publishing: Paris, France,
2012. [CrossRef]

17. Campbell, J.Y. Restoring Rational Choice: The Challenge of Consumer Financial Regulation. Annu. Rev. Econ. 2016, 8, 1–23.

18.

[CrossRef]
Fernandes, D.; Lynch, J.G., Jr.; Netemeyer, R.G. Financial literacy, financial education, and downstream financial behaviors.
Manag. Sci. 2014, 60, 1861–1883. [CrossRef]

19. Huston, S.J. Measuring financial literacy. J. Consum. Aff. 2010, 44, 296–316. [CrossRef]
20. Lusardi, A.; Tufano, P. Debt Literacy, Financial Experiences, and Overindebtedness. Brookings Pap. Econ. Act. 2015, 2015, 139–182.

[CrossRef]

21. Mandell, L. The Financial Literacy of Young American Adults: Results of the 2008 National Jumptart Coalition Survey of High School
Seniors and College Students; Technical Report; Jumptart Coalition for Personal Financial Literacy: Washington, DC, USA, 2008.

22. OECD. OECD/INFE International Survey of Adult Financial Literacy Competencies; Technical Report; OECD Publishing: Paris, France,

2016.

23. Remund, D.L. Financial Literacy Explicated: The Case for a Clearer Definition in an Increasingly Complex Economy. J. Financ.

24.

Couns. Plan. 2010, 21, 66–81. [CrossRef]
Sherraden, M.; Johnson, L.; Elliott, W.; Porterfield, S.; Rathbun, A. Financial Capability in Children: Effects of Participation in a
School-Based Financial Education and Savings Program. J. Sociol. Soc. Welf. 2011, 38, 69–91. [CrossRef]

25. Bucher-Koenen, T.; Lusardi, A. Financial Literacy and Retirement Planning in Germany. J. Pension Econ. Financ. 2011, 10, 565–584.

[CrossRef]

26. Lusardi, A.; Mitchell, O.S. Financial literacy and retirement planning: New evidence from the RAND American Life Panel.

J. Pension Econ. Financ. 2011, 10, 509–525. [CrossRef]

27. Hastings, J.S.; Madrian, B.C.; Skimmyhorn, W.L. Financial literacy, financial education, and economic outcomes. Annu. Rev. Econ.

2013, 5, 347–373. [CrossRef] [PubMed]

28. Hsu, J. Aging and strategic learning: The impact of spousal incentives on financial literacy. J. Hum. Resour. 2016, 51, 1036–1067.

[CrossRef]
Jappelli, T.; Padula, M. Investment in financial literacy and saving decisions. J. Bank. Financ. 2013, 37, 2779–2792. [CrossRef]
29.
30. Lusardi, A.; Mitchell, O.S. Financial literacy and retirement preparedness: Evidence and implications for financial education.

Bus. Econ. 2007, 42, 35–44. [CrossRef]

31. Vitt, L.; Anderson, C.; Kent, J.; Lyter, D.M.; Siegenthaler, J.K.; Ward, J. Personal Finance and the Rush to Competence: Financial Literacy

32.

Education in the US; Institute for Socio-Financial Studies: Middleburg, VA, USA, 2000.
Financial Industry Regulatory Authority (FINRA). Non-Traditional Costs of Financial Fraud; Technical Report; FINRA: Washington,
DC, USA, 2015.

33. Gilovich, T.; Kumar, A.; Jampol, L. A wonderful life: Experiential consumption and the pursuit of happiness. J. Consum. Psychol.

34.

2015, 25, 152–165. [CrossRef]
Isaia, E.; Oggero, N.; Sandretto, D. Is financial literacy a protection tool from online fraud in the digital era? J. Behav. Exp. Financ.
2024, 44, 100977. [CrossRef]

35. Tabak, B.M.; Silva, E.B.; Horta, R.; Christiano, T.; Tabak, G.C. Modeling Financial Literacy Using Multilevel Item Response Theory

and the COVID-19 Pandemic. 2023. Available online: https://ssrn.com/abstract=4368359 (accessed on 1 August 2025).

---

<!-- PAGE 31 -->

Sustainability 2025, 17, 9219

31 of 33

36. Paradgma; DataFolha. Primeira Pesquisa Nacional das Criptomoedas. 2025. Available online: https://criptopelobrasil.com.br/

(accessed on 10 August 2025).

37. Zhang, Y.; Chatterjee, S. Financial well-being in the United States: The roles of financial literacy and financial stress. Sustainability

2023, 15, 4505. [CrossRef]

38. Kahneman, D.; Tversky, A. Prospect Theory. An Analysis of Decision Making Under Risk; World Scientific: Singapore, 1977. [CrossRef]
39. Kahneman, D.; Frederick, S. Representativeness Revisited: Attribute Substitution in Intuitive Judgment. In Heuristics and Biases:
The Psychology of Intuitive Judgment; Gilovich, T., Griffin, D., Kahneman, D., Eds.; Cambridge University Press: New York, NY,
USA, 2002; pp. 49–81.
Financial Literacy Survey. Financial Literacy Survey 2022: Results; Technical Report; Public Relations Department, Bank of Japan:
Tokyo, Japan, 2022.

40.

41. Chalmers, R.P. mirt: A Multidimensional Item Response Theory Package for the R Environment. J. Stat. Softw. 2012, 48, 1–29.

[CrossRef]

42. Anderloni, L.; Bacchiocchi, E.; Vandone, D. Household financial vulnerability: An empirical analysis. Res. Econ. 2012, 66, 284–296.

[CrossRef]

43. Al-Omoush, K.S.; Gomez-Olmedo, A.M.; Funes, A.G. Why do people choose to continue using cryptocurrencies? Technol. Forecast.

Soc. Change 2024, 200, 123151. [CrossRef]

44. Eren, B.M.; Taspinar, N.; Gokmenoglu, K.K. The impact of financial development and economic growth on renewable energy

consumption: Empirical analysis of India. Sci. Total Environ. 2019, 663, 189–197. [CrossRef]

45. Ye, J.; Kulathunga, K.M.M.C.B. How does financial literacy promote sustainability in SMEs? A developing country perspective.

Sustainability 2019, 11, 2990. [CrossRef]

46. Waller, L.G.; Johnson, S. The possible contributive value of cryptocurrencies to Small Island Developing States. Int. J. Blockchains

Cryptocurrencies 2022, 3, 60–79. [CrossRef]

47. Alharbi, A.; Sohaib, O. Technology Readiness and Cryptocurrency Adoption: PLS-SEM and Deep Learning Neural Network

Analysis. IEEE Access 2021, 9, 21388–21394. [CrossRef]

48. Toufaily, E. An integrative model of trust toward crypto-tokens applications: A customer perspective approach. Digit. Bus. 2022,

49.

2, 100041. [CrossRef]
Sonkurt, H.; Altinöz, A. Cryptocurrency investment: A safe venture or a new type of gambling? J. Gambl. Issues 2021, 47.
[CrossRef]

50. KiatSakared, P.; Chen, K.Y. The effect of flow experience on online game addiction during the COVID-19 pandemic:

The moderating effect of activity passion. Sustainability 2022, 14, 12364. [CrossRef]

51. Mashatan, A.; Sangari, M.S.; Dehghani, M. How perceptions of information privacy and security impact consumer trust in

crypto-payment: An empirical study. IEEE Access 2022, 10, 69441–69454. [CrossRef]

52. Hariguna, T.; Ruangkanjanases, A.; Madon, B.B.; Alfawaz, K.M. Assessing determinants of continuance intention toward cryp-
tocurrency usage: Extending expectation confirmation model with technology readiness. SAGE Open 2023, 13, 21582440231160439.
[CrossRef]

53. Limayem, M.; Cheung, C.M. Predicting the continued use of Internet-based learning technologies: the role of habit. Behav. Inf.

Technol. 2011, 30, 91–99. [CrossRef]

54. Venkatesh, V.; Davis, F.D.; Morris, M.G.; Davis, G.B.; D., F. User acceptance of information technology: Toward a unified view.

55.

MIS Q. 2012, 27, 425–478. [CrossRef]
Sirohi, N.; Misra, G. Vulnerability of individuals to economic crime and the role of financial literacy in its prevention: Evidence
from India. In Crime, Law and Social Change; Springer: Berlin/Heidelberg, Germany, 2024; pp. 1–32. [CrossRef]
Frederick, S. Cognitive reflection and decision making. J. Econ. Perspect. 2005, 19, 25–42. [CrossRef]
Jensen, A.R. The g Factor: The Science of Mental Ability; Praeger: Westport, CT, USA, 1998.

56.
57.
58. Epstein, S. Integration of the Cognitive and Psychodynamic Unconscious. Am. Psychol. 1994, 49, 709–724. [CrossRef]
Sloman, S.A. The Empirical Case for Two Systems of Reasoning. Psychol. Bull. 1996, 119, 3–22. [CrossRef]
59.
60. Chaiken, S.; Trope, Y. Dual-Process Theories in Social Psychology; Guilford Press: New York, NY, USA, 1999.
61. Putler, D.S. Incorporating Reference Price Effects into a Theory of Consumer Choice. Mark. Sci. 1992, 11, 287–309. [CrossRef]
62. Tversky, A.; Kahneman, D. Advances in Prospect Theory: Cumulative Representation of Uncertainty. In Choices, Values, and

Frames; Springer Nature: Berlin/Heidelberg, Germany, 2000; pp. 44–66. [CrossRef]

63. Wang, M.; Rieger, M.O.; Hens, T. The Impact of Culture on Loss aversion. J. Behav. Decis. Mak. 2016, 30, 270–281. [CrossRef]
64. Banerjee, A.V. A simple model of herd behavior. Q. J. Econ. 1992, 107, 797–817. [CrossRef]
65. Raafat, R.M.; Chater, N.; Frith, C. Herding in humans. Trends Cogn. Sci. 2009, 13, 420–428. [CrossRef]
66. Da Gama Silva, P.V.J.; Klotzle, M.C.; Pinto, A.C.F.; Gomes, L.L. Herding behavior and contagion in the cryptocurrency market.

J. Behav. Exp. Financ. 2019, 22, 41–50. [CrossRef]

67. Kahneman, D. Thinking, Fast and Slow; Farrar, Straus and Giroux: New York, NY, USA, 2011.

---

<!-- PAGE 32 -->

Sustainability 2025, 17, 9219

32 of 33

68. Thaler, R.H.; Benartzi, S. Save More Tomorrow™: Using behavioral economics to increase employee saving. J. Political Econ. 2004,

112, S164–S187. [CrossRef]

69. Loewenstein, G.; Thaler, R. Anomalies: Intertemporal Choice. J. Econ. Perspect. 1989, 3, 181–193. [CrossRef]
70. Hershfield, H.E.; Goldstein, D.G.; Sharpe, W.F.; Fox, J.; Yeykelis, L.; Carstensen, L.L.; Bailenson, J.N. Increasing Saving Behavior

Through Age-Progressed Renderings of the Future Self. J. Mark. Res. 2011, 48, S23. [CrossRef]

71. Ye¸silkayalı, D. Procrastination and Future Discounting. J. Int. Soc. Res. 2025, 7, 275.
72.

Sheffer, C.E.; MacKillop, J.; Fernandez, A.; Christensen, D.; Bickel, W.K.; Johnson, M.W.; Mathew, M. Initial Examination of
Priming Tasks to Decrease Delay Discounting. Behav. Processes 2016, 128, 144–152. [CrossRef]

73. Witten, I.H.; Frank, E. Practical Machine Learning Tools and Techniques, 2nd ed.; Elsevier: Amsterdam, The Netherlands, 2005.
74. Oliveira, B.L.C.A.d.; Thomaz, E.B.A.F.; Silva, R.A.d. The association between skin color/race and health indicators in elderly
Brazilians: A study based on the Brazilian National Household Sample Survey (2008). Cad. Saúde Pública 2014, 30, 1438–1452.
[CrossRef] [PubMed]

75. Paixão, M.; Rossetto, I.; Montovanele, F.; Carvano, L.M. Relatório Anual das Desigualdades Raciais no Brasil: 2009–2010; Garamond:

Rio de Janeiro, Brazil, 2010.

76. da Silva Paiva, L.; Oliveira, F.R.; de Alcantara Sousa, L.V.; dos Santos Figueiredo, F.W.; de Sá, T.H.; Adami, F. Decline in Stroke
Mortality Between 1997 and 2012 by Sex: Ecological Study in Brazilians Aged 15 to 49 Years. Sci. Rep. 2019, 9, 2962. [CrossRef]
[PubMed]
Jiang, T.; Gradus, J.L.; Rosellini, A.J. Supervised Machine Learning: A Brief Primer. Behav. Ther. 2020, 51, 675–687. [CrossRef]
Silva, T.C.; Braz, T.; Tabak, B.M. Mapping the landscape of energy markets research: A bibliometric analysis and predictive
assessment using machine learning. Energy Econ. 2024, 136, 107698. [CrossRef]

77.
78.

79. Taunk, K.; De, S.; Verma, S.; Swetapadma, A. A Brief Review of Nearest Neighbor Algorithm for Learning and Classification.
In Proceedings of the 2019 International Conference on Intelligent Computing and Control Systems (ICCS), Madurai, India,
15–17 May 2019; pp. 1255–1260. [CrossRef]

80. Cortes, C.; Vapnik, V. Support-Vector Networks. Mach. Learn. 1995, 20, 273–297. [CrossRef]
81. Breiman, L. Random forests. Mach. Learn. 2001, 45, 5–32. [CrossRef]
82. Rumelhart, D.E.; McClelland, J.L., Learning Internal Representations by Error Propagation. In Parallel Distributed Processing:

Explorations in the Microstructure of Cognition: Foundations; MIT Press: Cambridge, MA, USA, 1987; pp. 318–362.

83. Zou, H.; Hastie, T. Regularization and Variable Selection Via the Elastic Net. J. R. Stat. Soc. Ser. B Stat. Methodol. 2005, 67, 301–320.

[CrossRef]

84. Kumar, S.; Bhatnagar, V. A Review of Regression Models in Machine Learning. J. Intell. Syst. Comput. 2021, 2, 40–47. [CrossRef]
85. Carvalho, D.V.; Pereira, E.M.; Cardoso, J.S. Machine Learning Interpretability: A Survey on Methods and Metrics. Electronics

2019, 8, 832. [CrossRef]

86. Hermosilla, P.; Berríos, S.; Allende-Cid, H. Explainable AI for Forensic Analysis: A Comparative Study of SHAP and LIME in

Intrusion Detection Models. Appl. Sci. 2025, 15, 7329. [CrossRef]

87. Lundberg, S.M.; Lee, S.I. A unified approach to interpreting model predictions. Adv. Neural Inf. Process. Syst. 2017, 30, 4768–4777.
88. Ribeiro, M.T.; Singh, S.; Guestrin, C. “ Why should i trust you?” Explaining the predictions of any classifier. In Proceedings of the
22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, CA, USA, 13–17 August
2016; pp. 1135–1144.

89. Pesquisa DataSenado. Panorama Político 2024: Apostas Esportivas, Golpes Digitais e Endividamento; Instituto de Pesquisa DataSenado:

90.

Brasilia, Brazil, 2024.
Sundarasen, S.; Rajagopalan, U.; Ibrahim, I. Financial Sustainability Through Literacy and Retirement Preparedness. Sustainability
2024, 16, 10692. [CrossRef]

91. Tulcanaza-Prieto, A.B.; Cortez-Ordoñez, A.; Rivera, J.; Lee, C.W. Is Digital Literacy a Moderator Variable in the Relationship
Between Financial Literacy, Financial Inclusion, and Financial Well-Being in the Ecuadorian Context? Sustainability 2025, 17, 2476.
[CrossRef]
Fundação Getulio Vargas. Indicador de Incerteza da Economia (IIE-Br)—Indicador Mensal de Abril de 2025. 2025. Available
online: https://portalibre.fgv.br/indicador-de-incerteza-da-economia (accessed on 21 May 2025).

92.

93. Katnic, I.; Katnic, M.; Orlandic, M.; Radunovic, M.; Mugosa, I. Understanding the Role of Financial Literacy in Enhancing

94.

Economic Stability and Resilience in Montenegro: A Data-Driven Approach. Sustainability 2024, 16, 11065. [CrossRef]
Sarker, I.H. Machine Learning: Algorithms, Real-World Applications and Research Directions. SN Comput. Sci. 2021, 2, 160.
[CrossRef]

95. de Lima Lemos, R.A.; Silva, T.C.; Tabak, B.M. Propension to customer churn in a financial institution: A machine learning

approach. Neural Comput. Appl. 2022, 34, 11751–11768. [CrossRef]

---

<!-- PAGE 33 -->

Sustainability 2025, 17, 9219

33 of 33

Schonlau, M.; Zou, R.Y. The random forest algorithm for statistical learning. Stata J. 2020, 20, 3–29. [CrossRef]

96.
97. Rosseel, Y. lavaan: An R Package for Structural Equation Modeling. J. Stat. Softw. 2011, 48, 1–36. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Article
Assessing the Drivers of Financial Vulnerability and Fraud in
Brazil: The Critical Role of Financial Planning over Literacy
BenjaminMirandaTabak*,† ,DéboraH.Cardoso† andCristianoC.Silva†
SchoolofPublicPolicyandGovernment,GetulioVargasFoundation(FGV/EPPG),SGAN602MódulosA,B,C,
AsaNorte,Brasilia70830-020,DF,Brazil;debora.cardoso@fgv.edu.br(D.H.C.);cristiano.silva@fgv.br(C.C.S.)
* Correspondence:benjamin.tabak@fgv.br
† Theseauthorscontributedequallytothiswork.
Abstract
This paper introduces and validates a comprehensive instrument designed to measure
financialliteracy,itsunderlyingdeterminants,andtoassesshowfactorssuchasplanning
affectfinancialvulnerabilityandfraudinBrazil. Thisworkrepresentsacrucialsteptoward
achievingseveralSustainableDevelopmentGoals(SDGs). Thestudyutilizesatwo-fold
methodology.First,ConfirmatoryFactorAnalysis(CFA)isusedtovalidateasix-component
modelconsistingofFinancialLiteracy,Vulnerability,Fraud,CognitiveReflection,Crypto
Literacy,andPlanning. Thisanalysisisfollowedbythedevelopmentandinterpretation
of a Random Forest model, which was identified as the best-performing predictor in a
comparisonofsevenmachinelearningalgorithms. TheCFAresultsshowedthatFinancial
Planning has a stronger negative correlation with Financial Vulnerability (−0.642) and
Fraud (−0.375) than Financial Literacy does. This evidence was further supported by
themachinelearninganalysis;analysesusingbothSHAPandLIMEidentifiedFinancial
Planning as the strongest predictor of financial vulnerability and fraud. The analysis
furthershowedsignificantsocialinequalitiesinthedevelopedmodelsandidentifiedthe
gender variable (female) as an important predictor of enhanced financial vulnerability.
ConvergingevidencefrombothCFAandmachinelearningconfirmsthatsoundplanning
practicesaremoreimportantthanfinancialknowledgeinreducingfinancialdistress. Our
findingsprovideasolidfoundationforthedevelopmentofinclusivepublicpolicythat
AcademicEditor:SajidAnwar promotesbehavioralchange,aimingtoreducesystemicinequalities(SDG10)andachieve
Received:30July2025 sustainableeconomicstability(SDG8),therebysupportingsocialgoalsandtheSustainable
Revised:18September2025 DevelopmentGoals.
Accepted:24September2025
Published:17October2025 Keywords: financial literacy; financial planning; vulnerability; financial behavior;
Citation: Tabak,B.M.;Cardoso,D.H.; sustainabledevelopment
Silva,C.C.AssessingtheDriversof
FinancialVulnerabilityandFraudin
Brazil:TheCriticalRoleofFinancial
PlanningoverLiteracy.Sustainability
1. Introduction
2025,17,9219. https://doi.org/
10.3390/su17209219 Lack of financial knowledge directly affects individuals’ ability to make informed
economicdecisions,therebydamagingtheirfinancialwell-beingintheshortandlongterm.
Copyright:©2025bytheauthors.
Thislimitationisespeciallyevidentinretirement,whenaccumulatedmistakesinfinancial
LicenseeMDPI,Basel,Switzerland.
Thisarticleisanopenaccessarticle managementbecomemoredifficulttocorrect. Studieshighlightthatlowfinancialliteracy
distributedunderthetermsand isassociatedwithinadequateeconomicchoices,suchasexcessiveindebtedness,lackof
conditionsoftheCreativeCommons planning,andgreaterexposuretofinancialfraud,negativelyimpactingindividualand
Attribution(CCBY)license
collectiveeconomicstability[1,2].
(https://creativecommons.org/
licenses/by/4.0/).
Sustainability2025,17,9219 https://doi.org/10.3390/su17209219

Sustainability2025,17,9219 2of33
Socioeconomicfactors,especiallylowschooling,furtherexacerbatefinancialvulnera-
bility,whichmakesitincreasinglyimportanttodevelopintersectionalinterventionsthat
reach groups of women, black individuals, and people with low schooling, who have
greaterdifficultyinaccessinggoodfinancialinformationandservices,takingintoaccount
theparticularitiesofeachone[3,4].
Itisimportanttonotethatfinancialliteracyreferstoasetofskills,goingbeyondjust
knowledgeaboutfinance. Thisisconfirmedwhenweanalyzetraditionalinterventionsthat
focusonlyoneducationalmethods,therebyneglectingbehavioralfactors. Interventions
suchasthesehavelowefficiency,whichrevealstheneedtodeveloppublicpoliciesthat
considerthebehavioralbiasesofindividuals,aswellasfinancialliteracy.
EspeciallyintheBraziliancontext,researchintofinancialliteracyasamultifaceted
element is even more necessary. The Brazilian Central Bank and the Credit Guarantee
Fundpointoutthatonascaleof0to100,theaverageleveloffinancialliteracyinBrazilis
59.6,withabout75%ofsurveyparticipantsobtainingamaximumscoreof70points,being
thosewithhigherlevelsofeducation. Thesamestudyshowsthat44.8%ofBraziliansin
thesamplesaidtheyneverorrarelyhadmoneyleftoverattheendofthemonth,and36%
wereconcernedaboutwhethertheywouldhaveenoughmoneytocovertheirexpenses.
Furthermore,theCentralBankpointsoutthat64%ofBraziliansfacefinancialinstability
andaround49.1%reportthatexperiencingfinancialworriesaffectstheirmentalhealth
on a personal and family level [5]. These data reveal Brazilians’ exposure to financial
vulnerability, which shows that there are still significant gaps to be filled in terms of
financialliteracyinBrazil,especiallyforminoritygroupssuchaspeoplewithlessaccessto
educationandformalfinancialservices.
Inthiscontext,investigatingtheelementsrelatedtofinancialliteracycanhelpinthe
developmentofinterventionsandpublicpoliciesthatcontributetoindividuals’financial
autonomyandwell-being. Financialeducationhasapositiveandsignificantinfluenceon
financialinclusionandtheattainmentofsustainablelivelihoods[6],andisconsidereda
pathtosustainability. Itisalsokeytoensuringthefinancialsustainabilityofindividuals,
families,businesses,andnationaleconomies[7],sinceeconomicgrowthandsustainability
dependonthefinancialeducationofindividuals.
FinancialliteracyisapillarfortheachievementofseveralSustainableDevelopment
Goals of the 2030 Agenda of the United Nations, related to poverty reduction (SDG 1),
increasedwell-being(SDG3),higher-qualityeducation(SDG4),genderequality(SDG5),
economic growth (SDG 8), reducing inequalities (SDG 10), and more responsible con-
sumption and production (SDG 12) [8]. This reinforces the indispensability of broad
and multifaceted research into financial literacy, as it is a driving force for individual
andcollectiveeconomicdevelopment,inadditiontocontributingsignificantlytopoverty
reduction[9].
Objectivemeasuresoffinancialliteracyareimportantforreducinginequalitiesbe-
tween people, as without financial literacy, they can face a series of problems, such as
difficultiesinmakinginformedinvestmentsorincurringlossesonassets,whichcanharm
theirfinancialwell-being. Nevertheless,financialliteracyasaconceptshouldbefurther
developedin terms ofalso coveringfinancial planningattitudes andusing newdigital
assetsasinvestmentproducts,suchascryptocurrencies. Ofequalimportanceismeasuring
knowledgeandattitudeimpactsacrossdesiredoutcomeindicators,suchasfinancialfraud
prevalenceorfinancialvulnerabilities. Thelatter,definedasfinancialprecariousnessor
alackoffinancialwell-being,hinderstheattainmentofSustainableDevelopmentGoal1,
aimedatachievingaworldwithoutpoverty,andatthesametimehindersSDG10,aimed
atreducinginequalities. Bothimpactsaresignificantandinhibitlong-termsustainable
developmentofacountry.

Sustainability2025,17,9219 3of33
Theprimaryobjectiveofthisworkistodevelopaninstrumentthatcomprehensively
measures financial literacy, encompassing aspects such as crypto literacy and financial
planning,andassesshowthesefactorsinfluencefinancialvulnerabilityandsusceptibility
tofinancialfraudamongindividuals,ultimatelyimpactingtheirfinancialwell-being. The
scopeofourinstrumentmayhelpfillgapsintheliterature,sinceitcanberelatedtoaspects
such as cognitive biases, financial fraud, and financial vulnerability. To the best of our
knowledge,thesedimensionshavenotbeenanalyzedinanintegratedmannertodate.
The structure of our paper is organized into interconnected sections. Initially, the
literaturereviewpresentsthefundamentalconceptsoffinancialliteracy,financialplanning,
andsusceptibilitytofraudandfinancialvulnerability. Next,inSection3usedtodevelop
andvalidatetheproposedinstrumentaredetailed,aswellastheexperimentalapplication.
Finally,inSections4and5provideinsightsintohowfinancialliteracycanbeincreased
andfinancialvulnerabilitiesreduced,withpracticalimplicationsforpublicpoliciesand
educationalprogramsinBrazil.
2. LiteratureReview
Thereisarelativelylargebodyofliteratureonhowindividualsdealwiththeirfinances.
Knowledge on this subject is essential because it provides conceptual inputs that help
people avoid putting themselves in a situation of financial vulnerability, especially in
scenariosofsocioeconomicinstability[1]. Abetterfinancialperceptioncontributestomore
assertivedecision-makingbasedoninformation,therebyreducingtheriskofindebtedness,
aswellaspromotingconditionsformoresustainableeconomicgrowth,financialinclusion,
andpositivefinancialbehavior[7,10].
Financialliteracyisunderstoodasanindividual’sabilitytounderstandandapply
financial concepts to make well-informed and more rational decisions [11–13]. In the
literature,severalfactorsareidentifiedasvariablesthatinfluencefinancialliteracy. These
include demographic and socioeconomic variations, with an emphasis on educational
attainment,age,andgender[11,14]. Anotherfactorhighlightedinrecentstudiesisthelack
ofaccessorlimitedaccesstoformalfinancialtechnologiesandservices[9].
Financialliteracyhasastrongeconomicandsocialimpact,asitenablesindividualsto
improvetheirfinancialwell-beinganddealwithsituationsoffinancialvulnerability[11].
The literature shows that people with greater financial literacy have greater autonomy
andabilitytomakeprudentandbeneficialdecisionsabouttheirfinanciallives,suchas
financialplanning,increasingsavings,andmanagingrisks[15]. Inadditiontodomestic
benefits,financialliteracyisalsoassociatedwithgreaterchancesofbusinesssuccess,since
moreliterateentrepreneurshavehigherincomesandsavings[13]. Furthermore,inrural
contexts,financialliteracyisalsoessentialforencouragingentrepreneurialactivities,which
contributetotheempowermentofruralcommunitiesandsustainabledevelopment[9].
Financial literacy contributes to people’s autonomy, enabling them to understand
economic scenarios and strategic resources and take more effective actions based on
planning, managing resources, calculating interest rates, diversifying investments, and
interacting with financial institutions. This contributes to making informed economic
decisions[1,16–24].
Understandingindividuals’attitudestowardstheuseofmoney,financialdecisions,
riskmanagementcapacity, andfinancialuncertaintiesistheobjectofstudyoffinancial
literacy[25,26]. Greaterfinancialliteracycontributestohealthierfinancialbehaviors,such
as greater savings, lower propensity to debt, greater financial planning capacity, and
betterparticipationinthestockmarket[2,20,27–29]. Theimportanceofthisknowledgeis
demonstratedbythenumberofpeopleunabletoanswersimplequestionsonthesubject,
as shown by an experiment carried out in the United States, in which only half of the

Sustainability2025,17,9219 4of33
respondentsovertheageof50wereabletogettwosimplequestionsaboutcompound
interestandinflationright[30]. Itisworthmentioningthatlowfinancialliteracyisaglobal
issuethatincludescountriessuchasGermany,Sweden,Italy,Japan,andNewZealand[26].
Importantaspectsofeconomiclifeareimpactedbyfinancialknowledge,asisthecase
withsavingforretirement. AstudycarriedoutintheNetherlandsfoundthatgettingmore
questionsrightaboutfinancialliteracycontributestoa10percentagepointincreaseinthe
abilitytoplanforretirement[26].Thenumberofsocialsecurityprograms,aimedatthemost
diversegroupsofindividualssuchaswomen,low-incomefamilies,andminorities[31],
revealsthegulfintheleveloffinancialliteracy,ascanbeseenamongwhitesandAsians,
whoaremoreknowledgeableinthisareathanAfrican-AmericansorHispanics[26].
Financialliteracyalsohelpstoreducefinancialvulnerability,aphenomenoncharac-
terizedbytheinabilitytopayunforeseenbills,highlevelsofdebt,andfrequentexposure
tofraud. Thisissueisveryworryingbecauseitrevealsastructuralproblemthatexposes
economicinequalities,financialexclusion,andalackoffinancialknowledge. Thisfinan-
cialvulnerabilitycanalsoaffectthehealthofindividuals,whichcanhaveanimpacton
physical and mental health, interpersonal relationships, and work performance [32,33].
Thetraininggeneratedbyfinancialliteracycontributestobettermanagementofsavings
andinvestments;thiscapacityreducesfinancialvulnerabilityandthusprovideseconomic
well-being[4,27–29].
Actionssuchasinadequatefinancialplanningandimpulsiveness,especiallyinthe
shortterm,arefactorspresentinthebehaviorofpeopleexposedtofinancialvulnerabil-
ity,whichmakesthemmoresusceptibletofraud,especiallyinascenariooflowdigital
inclusion[34].ThisisthecaseinBrazil,forexample,wherethelow-incomepopulationhas
noaccesstoformalfinancialproductssuchascreditandinsurance[3,4]. Andthisfinancial
exclusionleadstodependenceoninformalandpredatoryfinancialservices,whichmakes
thesituationofvulnerabilityevenworse[26].
Thelowlevelofknowledgeaboutbasicfinancialissuessuchasbudgeting,savings,
and credit as a result of a lack of financial literacy exposes individuals to vulnerability,
as recent studies have shown. This lack of knowledge makes it difficult to deal with
unforeseenevents,whichcontributestoexcessiveindebtedness. Theconsequenceofthis
behavior is the exclusion of low-income populations from the formal financial system,
increasingtheirexposuretofraudandunsustainablefinancialbehavior[4].
Financialliteracyisanimportanttoolforpromotingfinancialstability;understand-
ingthecostsassociatedwithcreditandavoidingunsustainablefinancingdecisions[35]
contributestothisresult. Thisknowledgecontributestobetterfinancialplanning,result-
ingintheestablishmentofemergencyreserves,whichreducesdefaultandalsohelpsto
strengthenindividualandcollectiveeconomicsecurity.
Understandingcryptocurrenciesisofparamountimportanceforassessingfinancial
knowledge. The1stNationalCryptocurrencySurveyinBrazilindicatesthatcryptoassets
havealreadysurpassedstocksininvestorpreference,showingthatinvestingincryptocur-
renciesisnowamongthefivemostpopularformsofinvestmentamongBrazilians. Despite
this,thesurveyshowsthatBrazilians’knowledgeofotheraspectsrelatedtothismarketis
stilllimitedandthereisalongwaytogointermsoffinancialeducation[36].
Theeffectivenessoffinancialliteracyisclearinitsroleincontributingtogoodfinancial
behaviorandreducingtheriskofvulnerability. Theliteratureshowsthatmorefinancially
literateindividualsdevelopmoreresilientbehaviorintimesofcrisis,reducingtheirex-
posuretoimpulsivebehaviorandfinancialfraud. Financialliteracyalsocontributesto
financialinclusionandsustainableeconomicdevelopment[7,37].Inscenarioscharacterized
byexclusionandeconomicinstability,financialliteracyhighlightsitsimportanceasatool

Sustainability2025,17,9219 5of33
forchange. Thisreinforcestheimportanceofinitiativesthatsupporttheexpansionand
betterdisseminationoffinancialliteracyatdifferentlevelsofsociety.
Substantialamountsofliteratureconfirmtheimportanceofindividual-levelfinancial
literacytopersonalaswellasmacroeconomicwell-being. However,scholarlyinvestiga-
tionhasprogressedmainlyinacompartmentalizedandunconnectedmanner. Thepast
literaturecanbroadlybecategorizedintoafewdifferentcamps: (1)studiesfocusingon
basicknowledgeoffinancewhereofteninterestcompounding,inflation,orriskdiversi-
fication(e.g.,[26,30])aretested,amongotherfactors;(2)behavioralfinancestudiesthat
investigatehowspecificcognitivebiases(e.g.,overconfidencebiasorlossaversion)impact
individual-levelfinancialdecision-making(e.g.,[38,39]);(3)socioeconomicexaminations
thatassessdriversoffinancialinsecurityoftenlinkingittovariablessuchasrace,gender,
orincome;or(4)recentscholarshipwhereawarenessregardingnewfinancialinstruments
suchascryptocurrenciesisexploredbutoftenfoundtobeunrelatedtomoretraditional
literacytesting. Whiletheserepresentworthwhileendeavorsindividually,theycollectively
presentanincompletepicture.
The key research gap, then, is the absence of a unifying, multidimensional frame-
workthatsimultaneouslyexaminesthesecomponents. Currentscholarshipfallsshortof
adequatelyexamininginterdependenciesamongfinancialliteracy(bothtraditionaland
novel),behavioralinclinations(e.g.,planning),cognitivetraits(e.g.,biasesandreflective
thinking),andreal-worldresults(relatedtobeingvulnerableorbeingafraudtarget)within
asingleframework. Accordingly,anambiguousunderstandingremainsregardinghow
theseforcesinteracttoimpactone’sindividualfinancialresilience. Additionally,acrucial
consideration missing from this fragmented landscape is an explicit connection to sus-
tainabledevelopment. WhilefinancialinclusionisoftenalignedwiththeUnitedNations
SustainableDevelopmentGoals(SDGs),existingscholarshiphasfailedtoadequatelyex-
plorehowthequalityoffinancialliteracy—encompassingbehaviors,cognitiveresilience,
andvulnerability—facilitatessocialandeconomicsustainability. Forinstance,variations
infinancialliteracyandvulnerabilitybyraceandgendertranscendeconomicissuesand
embodythecausesofsocialinjusticesthatunderminesocialsustainability,especiallywith
respecttoSDG5: GenderEqualityandSDG10: ReducedInequalities. Similarly,household
financevolatilityhasadirectimpactonanation’seconomicresilience,delineatingacore
componentofSDG8(DecentWorkandEconomicGrowth).
Our work aims to address these broad deficits through three key avenues. First,
wemovebeyondtheindividualisticmethodologybypositingandtestinganintegrated
frameworkthatsimultaneouslyconsidersbasicfinancialliteracy,knowledgeaboutcryp-
tocurrency, financial planning, reflective thinking, and cognitive bias. Secondly, as a
necessarymethodologicalinnovation,wedesignandvalidateanew,omnibusinstrument
speciallydevelopedfortheBraziliansetting,whichsimultaneouslymeasuresthesediverse
constructs. WeestablishthereliabilityandvalidityofsuchaninstrumentthroughCon-
firmatoryFactorAnalysisandthusprovideasturdytoolforfutureresearchapplications.
Finally,byincludingsocioeconomicanddemographicvariables(suchasraceandgender)
alongsidecovetedoutcomemeasures(suchasfinancialvulnerabilityandfraudexperience),
ourexploratoryworkestablishesadirectempiricallinkbetweenthemultifaceteddimen-
sionsoffinancialliteracyandtheoverallgoalsofsocialandeconomicsustainability. In
doingso,wereconceptualizefinancialliteracyasacriticalcomponentforbuildingfairer,
moreresilient,sustainablesocieties,beyondamereconcernforindividualwealth.

Sustainability2025,17,9219 6of33
3. MaterialsandMethods
3.1. Sampling
ThisresearchreceivedapprovalfromtheEthicsCommitteeonResearchInvolving
HumanSubjectsoftheGetulioVargasFoundation—CEPH/FGV(P.214.2024). Datacol-
lection commenced upon the acquisition of ethical permission. All study participants
providedinformedconsent. Thegivendetailsencompassedthestudy’saim,confidentiality,
participantautonomy,voluntaryparticipation,therighttowithdrawatanytime,andthe
guaranteethatallacquireddatawouldbeanonymizedtosafeguardparticipantidentity.
Althoughouranalysisshedslightontherelevantdeterminantsofvulnerabilityandim-
proprietyinfinancialdealingsinBrazil,itisimportanttoconsiderthespecialcharacteristics
ofoursampleininterpretingthefindings.
We conducted our data collection through direct contact at urban focal points, in-
cluding shopping centers, bus and subway terminal stations, and public spaces in the
FederalDistrict. Specifically,ourconveniencesamplingwasemployedtoachievearepre-
sentativecoverageofthepopulationbytheirsocioeconomiclevels,educationallevels,and
occupation. Thetotalsizeofthesamplewas256participants.
Despitethis,however,weareawareofthefollowinglimitationsassociatedwiththe
coverageofthesample.First,ourfocusonanurbanpopulationmeansthatthesampledoes
notcapturetheviewsofpopulationsinruralorotherremotelocations,andmayfacesome
pecuniaryissues,aswellasdisparateaccesstoinfrastructureforfinancesandinformation
technology. Secondly, the survey covered mostly the Federal District. This territory is
characterizedbyhighinternalmobilityanddemographicdiversity,whichincreasesthe
diversityofthesample. However,givenitsuniqueeconomicfeaturesastheadministrative
seatofthegovernment,itmaynotberepresentativeofotherBrazilianstates.
As such, it is critical to be cautious in extrapolating these findings to the broader
Brazilianpopulation.Thecombinationofplanning,literacy,andvulnerabilitymaybelikely
influencedbylocaleconomicfactorsandculturalnorms,whichareaddressedbythisstudy
inlimitedways. AlthoughthepopulationintheFederalDistrictisverydiverse,withmost
residentscomingfromdifferentpartsofthecountry,large-scalemigrationmayresultin
somestatesinBrazilbecomingmorehomogeneous,andthesefactorsmayworkindifferent
ways. Nonetheless,thisstudyaddstothecreationofasoundframeworkinunderstanding
nuancedrelationsoffinanceswithinaheterogeneousurbanenvironmentinBrazil. We
showhowitisimportanttoexpandfinancialeducationprogramsbyincorporatingkey
elements,likeplanningfinances,toinformintensivepublicpolicyactions.
DatawerecollectedthroughtheSurveyMonkeyplatformversion4.5.7,usingelectronic
devices. ThedatawaskeptinSurveyMonkey’scloud-baseddatabase,whichkeepsthe
dataencryptedaccordingtotheSOC2standard.
3.2. Instrument
In addition to socioeconomic questions, our instruments comprise items adapted
to Brazilian reality, ensuring good consistency and reliability (we used Confirmatory
Factor Analysis to evaluate the instruments and reduce the number of items to obtain
reliableandvalidinstruments,whichweusedfortheeconometricandmachinelearning
analysis). Wedevelopedacomprehensivefinancialliteracyinstrument,whichcomprises
corefinancialliteracyitems(FL).Wealsoincludedfinancialplanning(FP)andknowledge
on cryptocurrency (Crypto). This instrument has two knowledge dimensions (FL and
crypto)andanattitudedimension,whichisfinancialplanning.
WeevaluatedtheimpactoftheBroadFLinstrumentonfinancialvulnerability(VF)or
financialfraud(FV).Thesetwovariablescaptureanoutcomedimension,whererespondents
havesufferedfromfinancialvulnerability(i.e.,severalbillspastdue)orfinancialfraud

Sustainability2025,17,9219 7of33
(i.e.,sufferedlossesfromFF).Wealsomeasuredthereflectiveandanalyticalthinkingof
respondents using the Cognitive Reflection Test (CRT). In addition, we measured four
cognitive biases and control variables, including gender, race, age, and income. It is
importanttohighlightthatthefinalinstrumentfollowstheresultsfromtheConfirmatory
FactorAnalysis,regardingthegoodnessofthemodelfitandthereliabilityandvalidityof
thelatentfactors.
3.3. FinancialLiteracy—CoreKnowledge
Financial knowledge was measured using the main instrument (the Big Five) de-
veloped by Lusardi and Mitchell [26]. This is a widely used instrument for measuring
financial literacy, which provides a standardized and comparable measure of financial
knowledgebetweendifferentcountriesandgroups. Themainobjectiveofthe“BigFive”,
whichisanexpandedversionofthe“BigThree”[25],istoprovideaconsistentmeasure
offinancialknowledge. Consistingofquestionsonsimpleinterestrates,inflation,bond
prices,mortgages,andriskdiversification,thequestionnaireprovidesanexpandedviewof
respondents’financialknowledge[25].ToadaptittotheBraziliancontext,wetranslatedthe
instrumentbyreplacing“mortgage”with“financing”. Wealsoincludedonequestionfrom
financialknowledgefromtheFinancialLiteracySurvey[40]whichmeasuresinvestment
knowledgefocusingonreturnoninvestment.
Next, we selected two self-perception questions on financial knowledge from the
FinancialLiteracySurvey[40]. Thesequestionsallowedustoanalyzewhetherpeoplewho
havehadaccesstofinancialeducationmanagetheirfinancesbetterandhowconfidentthey
areintheirfinancialknowledge.
Wecovereddifferentaspectsoffinancialliteracy,andtoassessthisaspect,weused
threequestionsfromtheFinancialLiteracyQuiz[40]. Thisisatoolbasedontherecommen-
dationsoftheFinancialLiteracyMap,aJapaneseframeworkcreatedbytheCommitteefor
thePromotionofFinancialEducation. Inordertocoverdifferentcharacteristicsoffinancial
literacy,weincludedquestionsonfamilybudget,financialknowledge,understandingof
financial/economiccircumstances,appropriateselection/useoffinancialproducts,and
appropriateuseofexternalexpertise.
Toensurethatthescoreoffinancialknowledgereflectedtherealresult,weusedthe
methodofItemResponseTheory(IRT).IRTmodelsanalyzeindividualitemperformancein
relationtooverallability,allowingformoreprecisemeasurementoffinancialliteracyand
providinginsightsintothedifficultyanddiscriminatingpowerofeachquestion. Eachitem
inatesthasconstraints,suchasdifficulty,discrimination(abilitytodifferentiatebetween
peoplewithdifferentskilllevels),andtheprobabilityofgettingitrightbychance.
WeutilizedamultidimensionalItemResponseTheorynamedmirt. Themirtsoftware
wasdevelopedtoestimatemultidimensionalitemresponsetheoryparametersforboth
exploratoryandconfirmatorymodelswithmaximum-likelihoodapproaches[41]. Weuse
RSoftwareversion4.5.1whitMirtpackageversion1.45.1.
Afteranalyzingtheeightquestionsintheinstrument,theIRTmethodidentifiedone
question(three)thatparticipantshaddifficultyanswering,eventhosewithhighliteracy,
whilesomewithlowliteracyalsoansweredcorrectly. Wehavedecidedtodisregardthis
questioninthescoring(Figure1).
WealsoemployedConfirmatoryFactorAnalysis,retainedonlyfouritemsthathad
highloadings,andimprovedthepsychometricpropertiesoftheseinstruments. Thefinal
instrumentsareprovidedinAppendixC.

Sustainability2025,17,9219 8of33
Figure1.ItemCharacteristicCurve(ICC)graphsforeachquestionintheItemResponseTheory(IRT)
model,inthiscasea2PLmodel(two-parameterlogisticmodel).Foreachitem,thegraphshowsa
curvethatrepresentsthechanceofacorrectresponsetothequestion,asafunctionoftheperson’s
latentability(θ).X-axis:latentability(θ)from−6to+6.Thisisthelevelofproficiencyorfinancial
literacy.θ=0istheaverageabilityinthesample.θ>0indicatesmore“skilled”individuals.θ<0
indicatesindividualswithbelow-averageability.Y-axis:probabilityofacorrectresponsefrom0to1.
Showsthechanceofanindividualwithabilityθgettingtheitemright.Thesteeperandhigherthe
curve,thebettertheitemdiscriminatesbetweenabilitylevels.
3.4. FinancialPlanning
Financial planning was based on research by Anderloni et al. [42]. Six questions
wereselected,focusingonpersonalbehaviorandattitudes,suchascriticalthinkingbefore
buyingsomething,settingfinancialgoals,personalvigilanceinfinancialmatters,paying
bills on time, and people with divergent thinking, such as living for today and letting
tomorrowtakecareofitself. Weoptedtoadoptascaleofonlytworesponseoptionsforthe
instrument’sitems,attributingoneiftherespondentagreedtosomeextentwiththetext. It
shouldbenotedthattherearenocorrectorincorrectanswers,andthescoreobtainedisa
directmeasureoftherespondents’leveloffinancialplanning. Hence,alowerscorereflects
alowerleveloffinancialplanning.
3.5. CryptocurrencyLiteracy
For knowledge of cryptocurrencies, four items were selected from an instrument
initially developed by Al-Omoush et al. [43], based on an empirical study and items
takenfromrelevantstudiesintheliteratureonfinancialliteracy. Theoriginalinstrument
contains 24 items, divided into six scales with 4 items each. In addition, three experts
in cryptocurrencies, financial technology, and investments in financial assets reviewed
thisinstrumenttoevaluatethemeasuresandrefinetheitems,ensuringtheinstrument’s
accuracyandrobustness. Asfarastheanswersareconcerned,respondentsmustscoreeach
itemaccordingtoaLikertscale,rangingfrom1(stronglydisagree)to5(stronglyagree).
The original instrument consists of six scales, developed and validated based on
the relevant literature, namely (i) financial literacy, which assesses the knowledge and
abilitytodealwithfundamentalconceptsofcryptocurrencies[44,45];(ii)perceivedvalue,
whichemphasizestheperceivedbenefitsofusingcryptocurrencies,suchassecurityand
efficiency [46]; (iii) optimism, which measures users’ positive outlook on the future of
cryptocurrencies[47,48];(iv)cryptocurrencydependence,basedonthescalesproposed
bySonkurtandAltınöz[49]andKiatsakaredandChen[50],whichevaluatescompulsive
behaviorsandnegativeimpactsrelatedtoexcessiveuse;(v)trust,addressingtheperceived
securityandreliabilityofcryptocurrencytransactions[51,52];and,finally,(vi)intention

Sustainability2025,17,9219 9of33
tocontinueusing,whichexaminesthelong-termbehavioralintentiontocontinueusing
cryptocurrencies[53,54].
Todeveloptheinstrumentusedinthisstudy,onlytheitemsrelatedtothefinancial
literacyscalewereselectedtogaugetheparticipants’self-perceptionoftheirknowledge
aboutthecryptocurrencymarketandriskassessment. Unliketheoriginalstudy,weopted
to adopt a scale of only four response options for the instrument’s items, 1 (“strongly
disagree”),2(“disagree”),3(“agree”),and4(“stronglyagree”). Itshouldbenotedthat
therearenocorrectorincorrectanswers,andthescoreobtainedisadirectmeasureofthe
respondents’levelofknowledgeandperception. Hence,alowerscorereflectsalowerlevel
ofknowledgeaboutcryptocurrencies.
3.6. FinancialVulnerability
ThequestionnairedevelopedinthisstudywasbasedonresearchbyAnderlonietal.[42],
whosemainobjectiveistoproposeafinancialvulnerabilityindicator(FinancialVulnerabil-
ityIndex)thatsummarizesdifferentaspectsofthefinancialstressfacedbyfamilies,such
asexcessiveindebtedness,inabilitytocovermonthlyexpenses,latepaymentsandother
conditionsoffinancialinstability,aswellasanalyzinghowthecharacteristicsoffamilies
arerelatedtotheleveloffinancialvulnerability.
The study questionnaire covers five main areas to measure the degree of financial
vulnerabilityoffamilies: (i)sociodemographiccharacteristics;(ii)economicandfinancial
profile,whichinvestigatesthelevelofincome,financialwealthandassets,typesofdebt
(secured or unsecured), employment status, and use of risk management instruments,
suchasinsurance;(iii)financialliteracy;and(iv)economicandfinancialsituation,which
exploresdifficultiesinbalancingmonthlyexpensesanddealingwithunexpectedexpenses.
Theitemsincludedinourquestionnaireessentiallyconcernsecureaccesstocreditlines,
financialwell-being,householdexpenses,andaccesstohealthservices.
3.7. FinancialFraud
Tocomposethisdimension,weusedquestionsonfinancialfraud(FF)fromtheAssess-
mentofFinancialConsumerSurveyReport(2018)andtwoquestionsonsecurefinancial
behaviorfromtheFinancialLiteracySurvey[40]. Theitemswereselectedtoinvestigate
thevulnerabilityofindividualstoeconomiccrimeandfinancialfraud. Thesequestionsare
basedonstudiesexaminingexposuretoeconomiccrimeandtheroleoffinancialliteracyin
preventingit[55],aswellasreportssuchastheAssessmentofFinancialConsumerSurvey
Report(2018),whichanalyzestheimpactoffinancialfraudinvariouscontexts.
3.8. CognitiveReflectionTest
We used the 7-item Cognitive Reflection Test [56]. The Cognitive Reflection Test
is a psychological tool widely used to measure an individual’s propensity to resort to
reflective and analytical thinking rather than relying on intuitive and rapid responses.
DevelopedbyShaneFrederick,theCRTwasinitiallydevelopedwithjustthreequestions,
buthasevolvedtoincludemorecomprehensiveversions,suchastheseven-itemversion.
This expansion aimed to increase the test’s accuracy and ability to capture nuances in
participants’cognitivestyle.
TheCRTisbasedonthedualthoughtprocessmodel,whichdistinguishesbetween
twocognitivesystems: System1,whichisintuitive,fast,andautomatic,beingresponsible
forimpulsiveresponsesthatoftenleadtoerrorduetohighsusceptibilitytoopticalillusions,
andSystem2,whichisreflective,slow,anddeliberate,requiringgreatercognitiveeffortto
suppressintuitiveresponsesandreachmorereasonedsolutions[39,57–60]. CRTquestions
aredesignedtoexploitthisdynamic,presentingproblemsthatappearsimpleatfirstglance
butcontaincognitivetrapsdesignedtoinduceincorrectanswers.

Sustainability2025,17,9219 10of33
TheexpandedversionoftheCRT,withsevenitems,maintainsthelogicoftheoriginal
version, butincorporatesagreaternumberofquestionstodiversifythechallengespre-
sentedandimprovethereliabilityoftheresults. Thesequestionsarecarefullyformulated
toprovokeintuitiveerrorsandchallengetheparticipanttoresorttoanalyticalthinking.
For example, one of the classic questions in the three-item version asks: “A bat and a
ball together cost $1.10. The bat costs $1 more than the ball. How much does the ball
cost?” TheintuitiveandwronganswerwouldbeUSD0.10,whilethecorrectanswer,USD
0.05,requiresmorein-depthreasoning. Intheseven-itemversion,similarproblemsare
presented,coveringawiderspectrumofmathematicalandlogicalreasoning.
ScoringontheCRTissimpleandstraightforward,witheachcorrectanswerworth
onepoint,resultinginatotalscorerangingfrom0to7. Interpretingtheresultsprovides
insight into the participant’s cognitive style: lower scores indicate a strong reliance on
intuitivethinking,whilehigherscoresreflectagreatercapacityforanalyticalreasoning. In
addition,itispossibletoanalyzeintuitivewronganswers,whichofferinsightsintohow
oftenautomaticthinkingdominatesdeliberativethinking.
WeemployedConfirmatoryFactorAnalysisfortheCognitiveReflectionTest,retained
onlyfiveitemsthathadhighloadings,andimprovedthepsychometricpropertiesofthese
instruments. ThefinalinstrumentsareprovidedinAppendixC.
3.9. CognitiveBiases
Wealsoincludedfourcognitivebiasestotestiftheyarerelatedtofinancialliteracy
(corecompetencies),financialvulnerability,andfinancialfraud. Ourhypothesisisthatif
respondentsarepronetocognitivebiasesthentheymayhavelowerfinancialliteracyorbe
morelikelytohavefinancialvulnerabilityorfinancialfraudproblems[40].Takingcognitive
biases into consideration may help us to understand why so many people may have
difficultiesinavoidingfinancialtroublesorfinancialfraud. Cognitivebiasesarerelatedto
behaviorsthatdeviatefromrationalityandthereforemayexplainthesefinancialoutcomes.
Theitemsweredevelopedbasedonthepremisesofbehavioraleconomicsandexplore
the general characteristics of behavior in addition to specific biases that are fundamen-
tal to financial decisions, such as loss aversion, herd behavior, myopic behavior, and
hyperbolicdiscounting.
• Aversiontoloss:
Lossaversionisthecognitivebiasthatexplainswhyindividualsfeelthepainofloss
twice as intensely as the satisfaction generated by a gain of equal value [38]. This
biasdirectlyaffectsindividuals’financialdecisions,fromtheirinvestmentchoicesto
thechoiceofwhichgroceriestobuyatthesupermarket[61]. Thisisbecausepeople
affectedbythisbiaswillfocusmoreonpotentialcostsandfailuresthanonpotential
gainsandbenefits[62,63].
• Herdbehavior:
Herdbehaviorreferstothetendencyofindividualstofollowtheactionsordecisions
ofagroup,eventhoughthesechoicesmaybeirrationalorinconsistentwiththeirown
preferences. Thisbehaviorisinfluencedbythebeliefthattheactionsofthemajority
reflect superior information or decisions, leading individuals to ignore their own
judgments,somethingreinforcedbyfactorssuchassocialpressureandthesearchfor
validation[64,65]. Inthefinancialcontext,itsimplicationsaresignificant: collective
decisions, such as mass asset sales or purchases, can create economic bubbles or
crises[66]. Thus,herdbehaviornotonlyreducesthediversityofdecisionsbutalso
contributestovolatilityandsystemicrisksinfinancialmarkets.
• Short-sightedbehavior:

Sustainability2025,17,9219
11of33
Short-sighted behavior is marked by an exaggerated focus on immediate rewards,
whichcanleadtoimpulsivedecisions,suchasimpulsepurchasesandprocrastination,
prioritizingmomentarysatisfactionsthatcancausefutureregrets[67]. Peopleaffected
bythisbiastendtoseeonlyisolatedpartsofasituation,whichmakesthemignore
thesituationasawhole,leadingthemtodecisionsthatleadtoreducedgainsatthe
expenseofgreateropportunities[68].
|     |     |     | • Hyperbolicdiscount: |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hyperbolicdiscountingreferstothetendencytoundervaluefuturerewardstothe
detriment of immediate ones [69]. Behavior like this has a significant impact on
financial decisions, causing people to opt for immediate benefits, such as impulse
purchases,ratherthanlong-termbeneficialchoices,suchassavingforretirementor
investments[70,71]. Thistypeofbehaviorcanleadtofinancialproblems,suchasdebt
and lack of planning [72]. Understanding hyperbolic discounting and looking for
waystoovercomeitiskeytoimprovingpersonalandsocialfinancialstability.
|     |     |     | 3.10. MultipleLinearRegression |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
WeusedOrdinaryLeastSquares(OLS)toinvestigatetherelationshipbetweenvari-
ables. Thisisawidelyusedstatisticalmethodtoestimatethecoefficientsofalinearregres-
sionmodel[73]. Themultiplelinearregressionmodelwasappliedtoexplainthefollowing
dependentvariables:financialliteracy(FL),financialvulnerability(FV),andfinancialfraud
(FF).Allregressionswereestimatedwithrobuststandarderrorsforheteroskedasticity,and
theresultsaredisplayedinAppendixA.
Inourmodelingstrategy, wefirstassessedthepredictorsoffinancialliteracy(FL),
whichincludestheCognitiveReflectionTest(CRT).Subsequently,weusedtheresultingFL
score,alongsideothervariables,topredictbothfinancialvulnerability(FV)andfinancial
fraud(FF).
Oneofourkeyobjectiveshereistoassesswhetherknowledge-basedorbehavior-based
dimensionsoffinancialliteracyhaveamoresubstantialimpact. Assuch,wedeliberately
lookedatthesefactorsindividually.Weframeourmethodologywiththefollowingreasoning:
Hypothesis1: Wehopedtodetermineifthebehavioraldimension(financialplanning)wouldbea
betterpredictorthantheknowledgedimensionforfinancialresults(fraudandvulnerability).
Todistinguishthiseffect,weexaminedthedimensionsindividually.
Ourgeneralmultiplelinearregressionmodelcanberepresentedmathematicallyas:
FL = βFL+βFLCRT +βFLFemale +βFLNonBinary +βFLBlack +βFLOtherRace
|     | i 0 | 1   | i   | 2   | i   | 3   |     | i   | 4   | i   | 5   | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+βFLYoung +βFLOld +βFLLowIncome +βFLHighIncome +βFLLossAversion
|     |                | 6   | i             | 7                | i 8        |             |            | i          | 9             | i             | 10  |     | i   |     |
| --- | -------------- | --- | ------------- | ---------------- | ---------- | ----------- | ---------- | ---------- | ------------- | ------------- | --- | --- | --- | --- |
|     | +βFLMyopic     |     |               | +βFLDiscount     |            | +βFLHerding |            | +ε         | ,             |               |     |     |     | (1) |
|     |                | 11  | i             | 12               |            | i           | 13         | i          | i,FL          |               |     |     |     |     |
|     | = βFV+βFVFL    |     | +βFVFP        |                  | +βFVCrypto |             | +βFVFemale |            | +βFVNonBinary |               |     |     |     |     |
| FV  | i              |     | i             |                  | i          |             |            |            | i             |               |     |     |     |     |
|     | 0              | 1   |               | 2                | 3          |             | i          | 4          |               | 5             |     | i   |     |     |
|     | +βFVBlack      |     | +βFVOtherRace |                  |            | +βFVYoung   |            | +βFVOld    |               | +βFVLowIncome |     |     |     |     |
|     |                | 6   | i             | 7                |            | i           | 8          | i          | 9             | i 10          |     | i   |     |     |
|     | +βFVHighIncome |     |               | +βFVLossAversion |            |             |            | +βFVMyopic |               | +βFVDiscount  |     |     |     |     |
|     |                | 11  |               | i                | 12         |             | i          | 13         | i             | 14            |     | i   |     |     |
+βFVHerding
|     |             |     |               | +ε i,FV | ,          |           |            |         |               |               |     |     |     | (2) |
| --- | ----------- | --- | ------------- | ------- | ---------- | --------- | ---------- | ------- | ------------- | ------------- | --- | --- | --- | --- |
|     |             | 15  |               | i       |            |           |            |         |               |               |     |     |     |     |
| FF  | = βFF+βFFFL |     | +βFFFP        |         | +βFFCrypto |           | +βFFFemale |         | +βFFNonBinary |               |     |     |     |     |
|     | i 0         | 1   | i             | 2 i     | 3          |           | i          | 4       | i             | 5             | i   |     |     |     |
|     | +βFFBlack   |     | +βFFOtherRace |         |            | +βFFYoung |            | +βFFOld |               | +βFFLowIncome |     |     |     |     |
|     |             | 6   | i             | 7       |            | i 8       |            |         | 9 i           | 10            |     | i   |     |     |
i
|     | +βFFHighIncome |     |     | +βFFLossAversion |     |     | +βFFMyopic |     |     | +βFFDiscount |     |     |     |     |
| --- | -------------- | --- | --- | ---------------- | --- | --- | ---------- | --- | --- | ------------ | --- | --- | --- | --- |
|     |                | 11  |     | i                | 12  |     | i          | 13  | i   | 14           | i   |     |     |     |
|     | +βFFHerding    |     |     | +ε ,             |     |     |            |     |     |              |     |     |     | (3) |
|     |                | 15  |     | i i,FF           |     |     |            |     |     |              |     |     |     |     |
Theindependentvariablesusedinthemodelsaredefinedasfollows:

Sustainability2025,17,9219 12of33
FL—Latentvariableforfinancialliteracymeasuredbyfourobservedindicators;
FP—Latentvariableforfinancialplanningmeasuredbysixobservedindicators;
Crypto—Latentvariableforcryptocurrencyknowledgemeasuredbyfourobserved
indicators;
CRT—ReferstotheCognitiveReflectionTest,whichmeasurestherespondent’sability
tooverrideintuitivebutincorrectanswerswithreflectiveandaccuratereasoning;
Female—Representsthegenderoftherespondent,isadummyvariableequalto1if
therespondentidentifiesasfemale;
NonBinary—Representsthegenderoftherespondent,isadummyvariableequalto1
iftherespondentidentifiesasnonbinary;
Black—Is a dummy variable equal to 1 if the respondent identifies as Black. For
ouranalysis,wecombinedblackandmixed-racegroups,consistentwithpreviousstud-
ies[74–76];
OtherRace—Isadummyvariableequalto1iftherespondentidentifiesasbeingof
AsiandescentorIndigenous;
Young—Isadummyvariableequalto1iftherespondentisbetween18and30yearsold;
Old—Isadummyvariableequalto1iftherespondentis56yearsoldorolder;
LowIncome—Isadummyvariablethatrepresentsindividualsearninguptothreetimes
theminimumwage;
HighIncome—Is a dummy variable representing individuals earning more than
tentimestheminimumwage;
LossAversion—Indicatestherespondent’stendencytoavoidfinanciallosses;
Myopic—Captures the preference for immediate rewards over long-term benefits,
indicatingshort-termfinancialbehavior;
Discount—Reflects a preference for consumption rather than saving, indicating a
present-biasedpreference;
Herding—Measuresthetendencytofollowthebehaviorofthemajorityinfinancial
decision-making.
3.11. MachineLearning
Machinelearningisasubsetofartificialintelligencethatenablescomputerstoacquire
knowledgeandenhancetheirperformancethroughdata. Machinelearningmodelsare
algorithmstrainedondatatoidentifyspecificpatternsorgeneratechangesinpreviously
unobserveddatasets. Amultitudeofclassificationmethodshavebeenpresentedinthe
machinelearningliteratureanddatascience[73].
In this section, we utilize supervised learning techniques [77] to forecast the key
attributesthatareimportantforassessingFL,FV,andFFindices.Initially,weevaluatemany
classicmachinelearningapproachestoidentifythemostappropriateoneforourdataset.
This is significant as machine learning models are often employed to make judgments
withtangiblereal-worldimplications,particularlyinsectorssuchashealthcare,banking,
criminaljustice,andenergy[78].
3.11.1. HorseRace
Weconductedacompetitiveevaluationofsupervisedregressorstoidentifytheoptimal
machine learning technique that enhances model performance to explain the average
financialliteracy(FL),financialvulnerability(FV),andfinancialfraud(FF).Formodelingwe
usedthetidymodelsframeworkforRVersion1.4.1,theresultsarepresentedin(Figure2).
K-NearestNeighbors—Thefundamentalconceptofnearestneighbormethodsisto
identifyacertainnumberoftrainingsamplesthatareclosestinproximitytoanewpoint
andtopredictitslabelbasedonthosesamples. Thequantityofsamplesmaybeauser-

Sustainability2025,17,9219 13of33
definedconstant(k-nearestneighborlearning)orfluctuateaccordingtothelocaldensity
of the points (radius-based neighbor learning). The distance can often be any metric
measurement,withtheconventionalEuclideandistancebeingthemostprevalentoption.
Neighbor-basedapproachesareclassifiedasnon-generalizingmachinelearningtechniques,
astheyutilizeallavailabletrainingdata,potentiallyorganizedintoanefficientindexing
structure,suchasaballtreeoraKDtree[79].
SVMs—These are learning machines for classifying two groups. They map input
vectorsnonlinearlytoahigh-dimensionalfeaturespace,wherealineardecisionsurface
isconstructedwithpropertiesthatensurehighgeneralizationcapacity. Onlythesupport
vectors, which define the maximum margin of separation between classes, are used to
constructthissurface. SVMsusethe“kerneltrick”toefficientlycreatenonlineardecision
surfacesinhigh-dimensionalspaces. Fornon-separabledata,theyapplysoftmarginsto
allowforcontrollederrors,increasingrobustness[80].
RandomForests—Theyconsistofcollectionsofclassifiersthataretree-based,inwhich
eachtreeisgrownindependentlybyusingarandomvector. Theforestsvotebyoutput,
andthegeneralizationerrorconvergeswithoutoverfitting. RandomForestsarealsorobust
againstnoiseandyieldhighaccuracywithnumerousweakandcorrelatedinputs[81].
XGBoostisatypeofensemblelearningthatusestheGradientBoostingalgorithm. Itis
acommonchoiceformanymachinelearningtasks,especiallywhenitcomestoclassifying
andregressingstructureddata. Italsoletsyouusemorethanoneprocessortospeedupthe
trainingofthemodel. Itboastsconsiderablespeed,precision,androomforgrowth[80].
Amultilayerperceptron(MLP)isatypeofneuralnetworkthathasthreelayers: input
units,hidden(orinternal)units,andoutputunits. Thehiddenunits’principaljobisto
make internal representations of the input patterns. This enables the network to solve
issuesthataremorecomplexthanthosethattwo-layernetworkscanhandle. TheMLP’s
purposeistolearnhowtomatchtheinputpatternstotheoutputpatternsthatarewanted,
whichwillhelpitmakegoodgeneralizations[82].
ElasticNetisapenalizedregressionthatoutperformsLassowhenmorepredictors
exist than observations (p > n) or in situations of correlation of predictors. The model
involvesbothL1(Lasso)andL2(Ridge)penalties. Forstabilityandmodelprecision,Elastic
Netchoosesmorevariablesandranksthosethatexhibitinterrelationshipsamongthem[83].
Linearregression,beingoneofthefundamentalmethodsundersupervisedmachine
learning,makesuseofoneormultipleindependentvariablestopredictacontinuously
valuedresponse(thedependentvariable). Acommonmethodtoestimatethismodelisthe
OrdinaryLestSquares(OLS)regression[84].
Figure2.Horseracingoutcomes:Ontheleft,wepresenttheresultsforfinancialliteracy,financial
vulnerabilityandfinancialfraud.ThepointsrepresenttheaverageRMSEachievedinthefoldnot
utilizedfortrainingthroughout5separateiterationsofourcross-validation. Thehorizontalbars
representthe95%confidenceinterval.

Sustainability2025,17,9219 14of33
The executed model selection approach sought to accurately optimize the distinct
hyperparameterforeachutilizedmachinelearningalgorithm. Theprimarycriterionfor
identifyingtheoptimalhyperparameterconfigurationwasreductionintheRootMean
SquaredError(RMSE).Toachievethis,cross-validationusing5differentfoldswasused.
Theresultantobjectsencompasstherequisiteinformationtoiterateoverthesefolds,utiliz-
ing4formodeltrainingandtheremaining1forperformanceassessment,repeatingthis
process5timestoensureeachfoldservesasanevaluationsetonce. Ingeneral,tree-based
ensemblemodelsexhibitimprovedperformanceonthedataset. Givenourselectionof
RMSEastheperformanceindicator,wedeemedRandomForestthevictorofthecompeti-
tion,duetoitachievingthebestorsimilarRMSEtothebest-performingmethods,butwith
alowerstandarddeviation.
3.11.2. InterpretabilityMethods
Machinelearninginterpretabilityreferstomethodologiesforelucidatingandcom-
prehendingthemechanismsbywhichmachinelearningmodelsgeneratepredictions. As
modelsincreaseincomplexity,elucidatingtheirinternallogicandacquiringinsightsinto
theirbehaviorbecomeparamount[85]. Intheabsenceofinterpretability,itbecomeschal-
lenging to determine whether a machine learning model is making sound decisions or
exhibiting bias. Explainable Artificial Intelligence (XAI) has been revealed as a viable
solutiontothedifficultyofinterpretabilitybyclarifyingtherationalebehindthemodel
predictions[86].
AmongthediverseXAImethodologies,ShapleyAdditiveExplanation(SHAP)and
Local Interpretable Model-Agnostic Explanation (LIME) have attained recognition for
providing global and local interpretability. SHAP provides consistent and precise im-
portancevaluesforthecharacteristics. Incontrast,LIMEbuildslocalsubstitutemodels
thatemulatecomplexclassifierbehavior,therebyimprovingtheunderstandingofspecific
predictions[87,88]. Toelucidatethemodel’sjudgments,weemployedtwoprevalentXAI
methodologies: LIME,whichgenerateslocalsubstituteexplanations,andSHAP,which
assigns feature attributions based on game theory principles. These elements ensure a
clearerunderstandingandimportantpredictivepotential,essentialfortransparentresults.
4. Results
4.1. CharacteristicsoftheRespondents
Of the 256 respondents, 123 were women (48%), 128 men (50%), and 5 nonbinary
(1.95%). Withregardtorace/color,basedontheprincipleofself-declaration,thesampleis
madeupof100whitepeople(39.1%),149blackpeople(58.2%),5yellowpeople(1.95%)
and2indigenouspeople(0.78%). Intermsofincomedistribution,100respondents(39.1%)
earned up to 1 minimum wage (BRL 1320), 79 (30.9%) had an income between 1 and 3
minimumwages(BRL1320to3960),40(15.6%)between3and6minimumwages(R$3960
toR$7920),22(8.59%)between6and9minimumwages(BRL7920to11,880),8(3.12%)
between10and20minimumwages(BRL13,200toR$26,400)and7(2.73%)earnedmore
than20minimumwages(aboveBRL26,400)(Tables1and2).
Table1.Averagesofperformanceandbehavioralvariablesbygender,race,andincome.
Loss
Statistic FL Crypto FP FV FF CRT Discount Herding Myopic
Aversion
Gender
Female −0.135 −0.198 −0.132 0.161 0.0710 0.0155 30 63 31 40
Male 0.0815 0.330 0.00519 0.00455 0.162 0.170 28 44 41 31
Nonbinary −0.103 0.767 −0.513 0.200 0.661 1.020 0 1 3 2

Sustainability2025,17,9219 15of33
Table1.Cont.
Loss
Statistic FL Crypto FP FV FF CRT Discount Herding Myopic
Aversion
Race
Black −0.0357 0.0427 −0.0371 0.124 0.152 0.0588 31 68 51 44
White 0.00124 0.131 −0.114 0.0215 0.0805 0.180 26 38 22 27
OtherRace −0.214 0.318 −0.177 0.115 0.288 0.288 1 2 2 2
Income
Highincome 0.486 0.520 0.566 −0.590 0.0446 0.571 0 3 4 4
Lowincome −0.0957 0.0486 −0.121 0.161 0.124 0.0575 49 77 54 53
Middleincome 0.0509 0.0837 −0.0805 0.0219 0.161 0.160 9 28 17 16
Table2.Descriptivestatisticsofthevariables.
Loss
Statistic FL Crypto FP FV FF CRT Discount Herding Myopic
Aversion
Mean −0.0261 0.0847 −0.0710 0.2723 0.1281 0.1124 0.2266 0.4219 0.2930 0.2852
Median −0.0102 0.0250 0.0631 0.2143 −0.0398 −0.0103 0.0000 0.0000 0.0000 0.0000
Std.Dev. 0.7142 0.8164 0.7724 0.2320 0.6604 0.7091 0.4194 0.4948 0.4560 0.4524
Variance 0.5101 0.6665 0.5966 0.0538 0.4362 0.5028 0.1759 0.2449 0.2080 0.2046
Skewness −0.1985 0.6553 −0.4124 1.1209 0.7891 0.7039 1.2988 0.3145 0.9045 0.9461
Kurtosis −0.7806 −0.4872 −0.5072 0.3486 0.0065 −0.3156 −0.3144 −1.9085 −1.1866 −1.1091
Min −1.6742 −0.8187 −2.2995 0.0000 −0.8469 −1.0397 0.0000 0.0000 0.0000 0.0000
Max 1.5075 2.2870 1.3631 1.0000 2.2812 2.0727 1.0000 1.0000 1.0000 1.0000
Jarque–Bera 7.9143 20.8680 9.8786 55.7425 26.8942 22.3174 73.7376 42.7735 49.9742 51.4175
4.2. MultipleLinearRegression
Weusedthefollowingasdependentvariables: financialliteracy(FL),financialvulner-
ability(FV),andfinancialfraud(FF).TheresultsaredisplayedinAppendixA.
Inthefinancialliteracyanalysis,theCognitiveReflectionTestshowedastrongpositive
relationship (coef. 0.502; p < 0.01), with higher scores reflecting greater knowledge in
financialliteracy,demonstratingthatmorethoughtfulpeopletendtohavemoreknowledge
inthisfield. Womenhadlowerlevelsoffinancialliteracy(coef. −0.140;p<0.1),which
reflectssocialbarriersinaccesstofinancialliteracy. Individualswithahighincomehad
higherlevelsoffinancialliteracy(coef. 0.348;p<0.1)whichcanbeexplainedbyseveral
structural, social, and behavioral factors. In the analysis of race, individuals who self-
declaredthemselvesasblackorasanotherracedidnotshowsignificantresults.Behavioral
characteristicssuchaslossaversion,myopicbehavior,hyperbolicdiscounting,andherding,
althoughsomeshowedapositiveornegativecoefficient,werenotstatisticallysignificant.
Intheanalysisoffinancialvulnerability,individualswithbetterfinancialplanning
exhibitedastronginverserelationship(coef. −0.797;p<0.01),indicatingthatthosewith
effective financial planning, such as controlling and projecting their finances, are less
financially vulnerable. Individuals who self-identified as black were more financially
vulnerable(coef. 0.156;p<0.05),showingthatraceisanimportantcharacteristicandthat
blackpeoplearemorefinanciallyvulnerable.
Forfinancialfraudoutcomes,financialliteracyshowedasignificantnegativerelation-
ship(coefficient−0.139;p<0.1),demonstratingthathigherlevelsoffinancialknowledge
arecorrelatedwithalowersusceptibilitytofinancialfraud. Financialplanningisshownto
beimportantforfinancialvulnerability(coefficient−0.366;p<0.01),showingthatfinancial
planningisaneffectivetoolinreducingfraud.
Theresultsshowthatfinancialliteracyandfinancialplanningplayacrucialrolein
shapingbetterfinancialhabits,reducingfinancialvulnerabilities,andpreventingfraud.

Sustainability2025,17,9219 16of33
4.3. ResultsoftheMachineLearningApproach
TheimportanceofSHAPmeasurestheinfluenceofeachvariableontheindividual
modelprediction. Theabsolutemeanvalueshowsthestrengthofthisinfluence,regardless
of the sign (positive or negative). The higher the importance value, the more relevant
thevariableistothemodel’sdecisions. Thebeeswarmplotpresentstheresultsforthe
dependentvariablesFL(Figure3),FV(Figure4),andFF(Figure5). Thehorizontalaxis
denotestheSHAPvalue,whiletheverticalaxiscomprisesthepredictivefeatures. Positive
(negative)SHAPvaluessignifythatthefeatureenhances(diminishes)thetargetvariable.
Eachrepresentsadotforeveryattribute,whichsignifiestheSHAPvalueforaparticular
instance, indicating the contribution of that attribute to the overall prediction for that
instance. Thecolorofthedotcorrespondstothevalueofthefeature,withlighterhues
signifyinggreatervalues.
Figure3. ResultsofSHAPcomputedforeveryattributeovertheentiredatasetforpredictionof
financialliteracy(FL).
Figure4. ResultsofSHAPcomputedforeveryattributeovertheentiredatasetforpredictionof
financialvulnerability(FV).

Sustainability2025,17,9219 17of33
Figure5. ResultsofSHAPcomputedforeveryattributeovertheentiredatasetforpredictionof
financialfraud(FF).
TheimportanceofLIMEmeasurestheinfluenceofeachvariableontheindividual
modelprediction. Theabsolutemeanstrengthshowstheinfluenceofeachfeature. The
highertheimportancevalue,themorerelevantthevariableistothemodel’sdecisions. The
LIMEplotpresentstheresultsforthedependentvariablesFL(Figure6), FV(Figure7),
andFF(Figure8). LocalInterpretableModel-AgnosticExplanation(LIME)representsthe
averageimportanceofthevariablesinthelocalexplanationofthepredictionsmadebythe
bestmodel(RandomForest). TheX-axis(horizontal): namesofthevariables(orfeatures),
orderedfrommostimportanttoleastimportant,andtheY-axis(vertical): averageofthe
absolutevaluesoftheweightsattributedtothevariables(mean_weight)byLIMEinthe
explanations. Thisrepresentstheaveragecontributionofthatvariabletothepredictions.
Figure6. ResultsofLIMEcomputedforeveryattributeovertheentiredatasetforpredictionof
financialliteracy(FL).
Financial planning (FP) is the variable that most influences the model, presenting
a strong prediction for financial education, financial vulnerability, and financial fraud.
The significance is very high for both the SHAP and LIME methods. In an analysis of
financialliteracytheCognitiveReflectionTest(CRT)isthefeaturethatmostinfluences
boththeSHAPandLIMEmodels,confirmingtheresultsoftheregressions. Beingawoman
significantly impacts the predicted result, showing a positive prediction for financial
vulnerabilityandfinancialfraud,especiallyforthepredictionoffinancialliteracy,mainly

Sustainability2025,17,9219 18of33
when we look at the LIME results compared to the SHAP results; these values are a
consequenceofthedifferentmethodologiesbehindSHAPandLIME.TheLIMEmethod
providesinformationonspecificlocalspecifications,whiletheSHAPmethodaimsatamore
comprehensiveandglobalunderstandingofresourcecontributions. Botharevaluable,but
weanswerdifferentproposedquestionsabouttheimportanceoffeatures. Wecanhighlight
the variables FL, Crypto and Black, which, despite not having great predictive power,
alwaysrankamongthetopforfinancialvulnerabilityandfinancialfraudmodeling. The
othercharacteristicsdidnotshowgreatsignificanceinourmodels. Itisimportanttonote
thatthevaluesfortheNonbinaryandOtherRacevariablesarenotshownintheresults,
duetothesmallnumberofsamples. Whencross-validationisperformedontrainingand
testsets,thesegroupsmayendupinonlyoneofthesesets,oreveninnoneofthetestsets
incertainfolds,whichiswhatoccurredforthevaluesinquestion.
Figure7.ResultsofLIMEcomputedforeveryattributeovertheentiredatasetforthepredictionof
financialvulnerability(FV).
Figure8. ResultsofLIMEcomputedforeveryattributeovertheentiredatasetforpredictionof
financialfraud(FF).
Theseresultsconfirmtheregressionresults,especiallywhenwelookattheresultsof
theSHAPmethodology,sincethismethodologyaimsatamorecomprehensiveandglobal
understandingofthecontributionsofresources. Botharevaluable,butweanswerdifferent
proposedquestionsabouttheimportanceoffeatures.

Sustainability2025,17,9219 19of33
5. Discussion
Inrecentyears,Brazilhasseenariseinindebtedness,with32%ofBrazilianshaving
beeninarrearsformorethanthreemonths,aswellastherecurrenceoffinancialscams,
whichaffectmorethan40millionBrazilians[89]. Atthesametime,researchpointstothe
growingpopularityofonlinesportsbetting,called“bets”,whichispredominantlyaimed
atpeopleearninguptotwominimumsalaries[89]. Fromthiscontext,andbasedonthe
results of this article, we infer that financial literacy is something that deserves the full
attentionofpublicpolicymakers.
Therecentliteratureonfinancialliteracymainlyinvestigatesfinancialliteracyand
retirementplanning;theintersectionoffinancialriskmanagement;andtheimpactofbehav-
ioralfinanceandpsychologicalfactors[90]. Inlinewiththediscussionintheinternational
literature,ourresultsshowedthatpeoplewithgreaterfinancialliteracyhavebetterfinancial
habits,whichleadthemtopracticesthatreducetheirlevelofdebt,motivatinganincrease
infinancialreservesand,consequently,theabilitytodealwithunexpectedexpensesand
eveneconomicinstability. Financialliteracycombinedwithappropriatefinancialbehavior
contributestoindividualandfamilyfinancialsecurityandfavorseconomicgrowthand
stability[91].
EmergingeconomieslikeBrazilaremorevulnerabletoeconomicinstabilityandshocks.
TheGetulioVargasFoundation’sEconomicUncertaintyIndicator(IIE-Br)roseby4.6points
inApril2025,totaling115.5points[92],whichreinforcestheneedforapopulationcapable
ofdealingwitheconomicinstability,somethingthatisonlyfeasiblethroughagooddegree
of literacy and positive financial habits. The literature shows that people with greater
financialliteracyhavegreateraccesstoformalfinancialsystemsandusethemsparingly,
reducingthelikelihoodofbeingexposedtoanydegreeoffinancialvulnerability[93].
Thedevelopmentofnew,innovativeinstrumentsthatassessfinancialliteracy,financial
planning, and cryptocurrency literacy is intended to address substantive gaps in the
prevailing literature. Policymakers will now be able to measure financial literacy and
relatedconceptsinamoreefficientandcomprehensivemanner,whilebeinginaposition
to design and deliver interventions that are empirically grounded. The imperative of
developingthistoolarisesduetothecomplicatednatureoftheconstructandfinancial
literacy’scentralroleinpersonalaswellascommunaleconomicstability,wherebythere
mustbeintermixingofbasicfinancialcompetencywithattitudes,behaviors,andcontextual
factors, such as exposure to socioeconomic vulnerability, that have a direct influence
upon individuals’ health, well-being, and financial stability [91]. In hypothesizing and
craftingourapproach,notonlyhastherebeenastepupinscholarlyworkinacademia,
butfinancialliteracy’sstatusasacomplicatedconstructhasalsobeenacknowledged. This
facilitatestheevidence-basedpromotionofeffectiveinterventions,aswellasadecreasein
vulnerability[1,23].
Inlinewiththeinternationalliterature,ourresultsshowthatintheFederalDistrict,
financialliteracyplaysanimportantroleindevelopingbetterfinancialhabitsamongthe
population. However,forthesampleanalyzed,thedatashowthattheoreticalknowledge
alonedoesnotguaranteethemitigationoffinancialvulnerabilities,noreventheprevention
offraud. Thistypeoffindingconvergeswithotherstudiesthathighlighttheimportance
ofanintegratedapproachthatconsidersnotonlyknowledge,butalsothepracticesand
social context of individuals [18,19,35]. Accordingly, financial behavior emerged as the
most consistent dimension in explaining the positive outcomes of the sample. This di-
mension, therefore, shows that skills such as spending control, financial planning, and
behavioralresilienceareessentialforreducingvulnerabilityandstrengtheningfinancial
security[20,68].

Sustainability2025,17,9219 20of33
The analysis also revealed significant inequalities in the levels of financial literacy
betweenthedifferentgroupsinthesample. Individualswithhighincome,forexample,
hadhigherlevelsoffinancialliteracy,reflectingstructuralandculturalbarrierstoaccessing
financialliteracyandotherformaleconomicresources. Thistypeofinequality,whichhas
alreadybeendemonstratedinotherstudies[25,29],isevenmorecriticalinBrazil,acountry
characterized by high income inequality and financial exclusion, especially among the
low-income population [3,4]. These results highlight the need for intersectional public
policies,thatis,policiesthattakeintoaccountthesocioeconomicandculturalparticularities
ofthemostvulnerablegroups.
Ourfindingsconfirmourhypothesis: planninghasmuchstrongerpredictiveability.
As a matter of theoretical interest but also because such a composite aggregated index
wouldsuppressanimportantdifference,weperformedsuchanexerciseasarobustness
check. The results, which we document in Appendix B, confirm our major results and
supportourinitialhypothesis. Wecarriedoutanassessmentwithacompositeindexto
confirmourmethodology. Theresultsprocuredwereconsistentwithourmainfindings
andavailableinAppendixB.
5.1. ImplicationsforSustainableDevelopment
Wefoundlowerfinancialliteracyforwomen, comparedtomalerespondents, and
greatervulnerabilityamongblackindividuals. Theseresultsdemonstratenotonlyimpor-
tanteconomicissues,butalsoissuesofsocialinjusticethatunderminesocialsustainability.
InBrazil,therearealreadyracialquotapoliciesforblackpeopletoaccesspublicuniversities.
Publicpoliciesthataddressracialinjusticesareimportanttotackleissuesofvulnerability
andfinancialfraud. Futureresearchcouldassesswhetheralgorithmsmaybebeingusedto
defraudpeopleofspecificracesduetogreatervulnerability.
Greaterfinancialvulnerabilityleadstofamiliesexperiencinggreaterinstabilityintheir
savings.Itcausesthemtoseekaccesstocreditthatcanbepredatory,withhighinterestrates.
Itcanalsoleadtodifficultyinwithstandingadverseeconomicshocks. Theseweaknesses
shouldbeaddressedatthemacroeconomiclevel,whichunderscorestheimportanceof
enhancing financial planning, as well as household resilience, in order to build a more
stableandsustainablenationaleconomy(thispointiscloselyrelatedtoSDG8: Decent
WorkandEconomicGrowth).
Our main finding is that financial planning and behaviors are more critical than
knowledge(asmeasuredbythefinancialliteracyinstrument, whichencompassesonly
basicknowledge). Similarly,environmentalknowledgedoesnotnecessarilyleadpeople
tobehaveinapro-environmentalway. Thus,financialknowledgedoesnotguaranteethe
financialwell-beingoffamilies. Thus,akeyfindingofourstudyisthatsustainableout-
comesdependonfosteringorstimulatinglong-termthinkingandbehavioralchanges. Our
resultssuggestimportantavenuesfordevelopingpublicpoliciesthataremoreinclusive
andaimtofosterbehavioralchange. Futureresearchcouldinvestigatethisrelationship
byevaluatingtheimpactofnudgesonincreasingpeople’sfinancialwell-being,reducing
vulnerabilities,andpromotingmoresustainablebehaviors.
5.2. MachineLearningDiscussion
Machinelearningsystemshelppeopleandinstitutionsbetterunderstanddataand
identifyimportantpatternswithinit. Thisinformationiscrucialfordecision-makingand
planning. Therefore, it is important to understand the principles of machine learning
algorithmsandtheirapplicabilityinvariousreal-worldapplicationareas,suchassecurity
services,healthcare,economicdata,context-awaresystems,sustainableagriculture,and
manyothers[94]. Choosingthebestmachinelearningmodelcanbequiteadauntingtask.

Sustainability2025,17,9219 21of33
Typically,whencreatingamodel,wechoosethealgorithmthatperformsbestforthedata
inquestion. Tosupportthis,weuseamethodologythatisbecomingwidespreadwhen
comparingmachinelearningmodelsinahorseracetochoosewhichmodelisbest[95]. The
bestmodelevaluatedwasRandomForest,ahighlyeffectivemachinelearningalgorithm
that excels at modeling nonlinear relationships and providing the importance of each
variable[96].
Easeofinterpretingresultsisparamount,associalresearchersareprimarilyconcerned
withunderstandingcomplexsocialspecificity,testingtheories,anddrawingexplanatory
conclusionsfromtheirdata. Theirexpertiseliesintheirrespectivefields,notnecessarilyin
advancedcomputerprogrammingoralgorithmdevelopment,tohaveabetterinterpreta-
tionoftheresultsusingSHAPandLIME,whicharetwoprominenttechniquesinthefield
ofExplainableAI(XAI),addressingthe“blackbox”problemofcomplexmachinelearning
models,helpingresearchersunderstandwhyacertaindiscoverywasmade.
6. FinalConsiderations
The results highlight the need for comprehensive initiatives that address not only
thefundamentalsoffinancialknowledgebutalsotheunderstandinganddevelopment
of individuals’ behaviors and attitudes. Public policies aimed at promoting financial
inclusion,forexample,shouldincorporatefinancialliteracyprogramsadaptedtodifferent
audiences. Thisadaptationmustalsoconsiderothersocialfactors,suchassex,race,and
income. Anotherkeypointliesintheintegrationoftechnologicaltoolsandinnovative
methodologies,suchastheinstrumentdevelopedinthisstudy,whichcansignificantly
contributetoenhancingtheeffectivenessandreachoftheseinitiatives.
OnepossiblelimitationofthestudyisthatwefocusonrespondentsfromtheFederal
DistrictofBrazil. Althoughapotentialshortcominginvolvestheuseofparticipantsdrawn
fromtheFederalDistrict,sampleheterogeneityregardingincome,education,andracial
background allowed us to gain insight into the associations among these fundamental
demographicfactorsandfinancialliteracy. Futurestudiesmayconsiderhowinter-regional
variationsaffectfinancialliteracyanditscorrelationwithcognitivebiases,amongother
factors. Oneofthefundamentalquestionsofresearchiswhetherthereisgeneralizability
in such findings and whether there is a potential contribution of cultural variations in
thisregard.
Itisessentialtohighlightthatourresultsdonotnecessarilyimplyadirectcause-and-
effect relationship. However, our results indicate that enhancing financial literacy and
mitigatingfinancialvulnerabilitiespresentrelevantdriversthatareconsistentwiththe
broadgoalsofsustainabledevelopment.
AuthorContributions: Conceptualization,B.M.T.andD.H.C.;Methodology,B.M.T.,D.H.C.and
C.C.S.;Software,B.M.T.andC.C.S.;Formalanalysis,B.M.T.,D.H.C.andC.C.S.;Investigation,B.M.T.
andD.H.C.;Datacuration,D.H.C.andC.C.S.;Writing—originaldraft,B.M.T.,D.H.C.andC.C.S.;
Writing—review & editing, B.M.T., D.H.C. and C.C.S. All authors have read and agreed to the
publishedversionofthemanuscript.
Funding: ThisresearchwasfundedbyFundaçãodeApoioàPesquisadoDistritoFederal—FAP-
DF—under the name ‘Alfabetização Financeira e Vieses Cognitivos: o caso do Distrito Federal
00193-00000273/2023-01’. BMTgratefullyacknowledgesfinancialsupportfromFAP-DF,CAPES
(ExperimentalLaboratoryinPublicPolicy—LAB-LEPP),andCNPq(grant).DCSandTCSgratefully
acknowledgefinancialsupportfromFAP-DF.
InstitutionalReviewBoardStatement: Thestudywasconductedaccordingtotheguidelinesof
theDeclarationofHelsinki,andapprovedbytheEthicsCommitteeofGetulioVargasFoundation
(protocolcodeP.421.2023anddateofapprovalis24October2023).

Sustainability2025,17,9219
22of33
InformedConsentStatement:Informedconsentwasobtainedfromallsubjectsinvolvedinthestudy.
DataAvailabilityStatement:Thedataareavailableuponrequestfromtheauthors.
Acknowledgments:TheauthorsusedGenAI,DeepL,andGrammarlytoimprovethereadabilityand
clarityofthetext.Theentiretexthasbeenreviewedandapprovedbytheauthors,whoassumefull
responsibility.Wethankthefouranonymousreviewersandtheeditor,whohavehelpedimprove
thepaper.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.Thefundershadnoroleinthedesign
ofthestudy;inthecollection,analysis,orinterpretationofdata;inthewritingofthemanuscript;or
inthedecisiontopublishtheresults.
AppendixA.RegressionResults
TableA1.Dependentvariables:FLBroad,FV,andFF.
|     | FLBroad(HC3) | FV(HC3) | FF(HC3) |
| --- | ------------ | ------- | ------- |
|     | (1)          | (2)     | (3)     |
| CRT | 0.502***     |         |         |
(0.057)
| FL  |     | 0.053     | −0.139*   |
| --- | --- | --------- | --------- |
|     |     | (0.071)   | (0.078)   |
| FP  |     | −0.797*** | −0.366*** |
|     |     | (0.055)   | (0.071)   |
−0.046
| Crypto    |         |         | 0.079   |
| --------- | ------- | ------- | ------- |
|           |         | (0.045) | (0.054) |
| Female    | −0.140* | 0.053   | −0.117  |
|           | (0.083) | (0.074) | (0.079) |
| NonBinary | −0.709  | −0.176  | 0.243   |
|           | (0.454) | (0.286) | (0.402) |
| Black     | 0.010   | 0.156** | 0.091   |
|           | (0.088) | (0.073) | (0.076) |
−0.315
| OtherRace    |         | 0.127   | 0.0002  |
| ------------ | ------- | ------- | ------- |
|              | (0.395) | (0.143) | (0.285) |
| Young        | 0.025   | −0.017  | −0.104  |
|              | (0.100) | (0.089) | (0.103) |
| Old          | −0.063  | −0.087  | −0.056  |
|              | (0.143) | (0.114) | (0.154) |
|              | −0.071  |         | −0.027  |
| LowIncome    |         | 0.096   |         |
|              | (0.106) | (0.096) | (0.102) |
| HighIncome   | 0.348*  | −0.113  | 0.127   |
|              | (0.195) | (0.133) | (0.220) |
| LossAversion | 0.014   | −0.096  | −0.064  |
|              | (0.084) | (0.073) | (0.074) |
| Myopic       | 0.055   | 0.016   | 0.046   |
|              | (0.088) | (0.082) | (0.082) |
|              | −0.111  | −0.028  | −0.006  |
Discount
|         | (0.097) | (0.084) | (0.092) |
| ------- | ------- | ------- | ------- |
| Herding | −0.064  | 0.064   | −0.008  |
|         | (0.086) | (0.077) | (0.083) |

Sustainability2025,17,9219 23of33
TableA1.Cont.
FLBroad(HC3) FV(HC3) FF(HC3)
(1) (2) (3)
Constant 0.046 −0.100 0.188*
(0.119) (0.095) (0.108)
Observations 256 256 256
R2 0.320 0.594 0.304
AdjustedR2 0.284 0.569 0.261
ResidualStd. Error 0.604 0.527 0.568
FStatistic 8.771*** 23.430*** 6.992***
Note: Robuststandarderrorsinparentheses.*p<0.1;**p<0.05;***p<0.01.
AppendixB.FL_BroadFactorIndex
WeconstructedtheFL_Broadfactorindex,whichcomprisesanaggregateindexthat
encompassesfinancialliteracy(basicknowledgeoffinance),knowledgeaboutcryptocurren-
cies(Crypto),andfinancialattitudesregardingfinancialplanning(FinancialPlanning—FP).
FL+FP+Crypto
FL_Broad =
3
Ourgeneralmultiplelinearregressionmodelcanberepresentedmathematicallyas:
FL_Broad = βFL+βFL_BroadCRT +βFL_BroadFemale +βFL_BroadNonBinary
i 0 1 i 2 i 3 i
+βFL_BroadBlack +βFL_BroadOtherRace +βFL_BroadYoung +βFL_BroadOld
4 i 5 i 6 i 7 i
+βFL_BroadLowIncome +βFL_BroadHighIncome +βFL_BroadLossAversion
8 i 9 i 10 i
+βFL_BroadMyopic +βFL_BroadDiscount +βFL_BroadHerding +ε , (A1)
11 i 12 i 13 i i,FL_Broad
FV = βFV+βFVFL_Broad +βFVFemale +βFVNonBinary
i 0 1 i 2 i 3 i
+βFVBlack +βFVOtherRace +βFVYoung +βFVOld +βFVLowIncome
4 i 5 i 6 i 7 i 8 i
+βFVHighIncome +βFVLossAversion +βFVMyopic +βFVDiscount
9 i 10 i 11 i 12 i
+βFVHerding +ε , (A2)
13 i i,FV
FF = βFF+βFFFL_Broad +βFFFemale +βFFNonBinary
i 0 1 i 2 i 3 i
+βFFBlack +βFFOtherRace +βFFYoung +βFFOld +βFFLowIncome
4 i 5 i 6 i 7 i 8 i
+βFFHighIncome +βFFLossAversion +βFFMyopic +βFFDiscount
9 i 10 i 11 i 12 i
+βFFHerding +ε , (A3)
13 i i,FF
TableA2.Regressionresults:dependentvariables:FL_Broad,FV,andFF.
FL_Broad(HC3) FV(HC3) FF(HC3)
(1) (2) (3)
C_R 0.363***
(0.046)
FL_Broad −0.917*** −0.516***
(0.072) (0.075)
Female −0.220*** −0.066 −0.209***
(0.061) (0.085) (0.080)
NonBinary −0.631* 0.088 0.389
(0.371) (0.372) (0.382)

Sustainability2025,17,9219
24of33
TableA2.Cont.
|           |     | FL_Broad(HC3) | FV(HC3) | FF(HC3) |
| --------- | --- | ------------- | ------- | ------- |
|           |     | (1)           | (2)     | (3)     |
| Black     |     | 0.020         | 0.090   | 0.057   |
|           |     | (0.066)       | (0.083) | (0.083) |
| OtherRace |     | −0.104        | 0.088   | 0.034   |
|           |     | (0.319)       | (0.240) | (0.244) |
−0.034
| Young      |     | 0.187** | 0.040    |         |
| ---------- | --- | ------- | -------- | ------- |
|            |     | (0.075) | (0.108)  | (0.108) |
| Old        |     | −0.006  | −0.169   | −0.094  |
|            |     | (0.107) | (0.137)  | (0.160) |
| LowIncome  |     | −0.069  | 0.044    | −0.052  |
|            |     | (0.079) | (0.106)  | (0.104) |
| HighIncome |     | 0.369** | −0.215   | 0.071   |
|            |     | (0.154) | (0.179)  | (0.230) |
|            |     | −0.054  | −0.209** | −0.148* |
LossAversion
|              |       | (0.061)   | (0.081)   | (0.077)  |
| ------------ | ----- | --------- | --------- | -------- |
| Myopic       |       | 0.091     | −0.008    | 0.047    |
|              |       | (0.066)   | (0.089)   | (0.086)  |
| Discount     |       | −0.147**  | −0.055    | −0.031   |
|              |       | (0.070)   | (0.095)   | (0.099)  |
| Herding      |       | −0.012    | 0.109     | 0.039    |
|              |       | (0.069)   | (0.092)   | (0.090)  |
| Constant     |       | 0.013     | 0.105     | 0.293**  |
|              |       | (0.087)   | (0.111)   | (0.115)  |
| Observations |       | 256       | 256       | 256      |
| R2           |       | 0.388     | 0.439     | 0.206    |
| AdjustedR2   |       | 0.355     | 0.409     | 0.164    |
| ResidualStd. | Error | 0.459     | 0.617     | 0.604    |
| FStatistic   |       | 11.799*** | 14.560*** | 4.841*** |
Note:Robuststandarderrorsinparentheses.*p<0.1;**p<0.05;***p<0.01.
AppendixC.MeasurementModelEquationsfortheConfirmatoryFactor
Analysis(CFA)
| AppendixC.1. | ConfirmatoryFactorAnalysis |     |     |     |
| ------------ | -------------------------- | --- | --- | --- |
WeimplementedaConfirmatoryFactorAnalysistoevaluatethereliabilityandvalidity
ofourlatentfactors(Rosseel[97]). Wemodeledsixlatentfactors: (i)thefinancialliteracy
(F )scale,whichmeasurescoreknowledge;(ii)thefinancialvulnerability(FV)scale,which
L
measuresiftherespondentisnotabletopaytheirbills(anoutcomescale);(iii)thefinancial
fraudscale(FF),whichhasfouritemsthatevaluateiftherespondenthasbeenvictimized
byfinancialfraud;(iv)theCognitiveReflectionTest(CR),whichevaluatesiftherespondent
usesintuitionorrationalitytoanswerthequestions;(v)thecryptocurrencyliteracyscale
(CRY);and(vi)thefinancialplanning(FP)scale,whichmeasuresiftherespondentisprone
tofinancialplanning.
| AppendixC.2. | Notation |     |     |     |
| ------------ | -------- | --- | --- | --- |
Let:
• η(eta)representalatentvariable(factor).

Sustainability2025,17,9219 25of33
• xrepresentanobservedvariable(indicator).
• λ(lambda)representthefactorloading,whichmeasuresthestrengthoftherelation-
shipbetweentheobservedvariableanditsrespectivelatentfactor.
• ϵ(epsilon)representthemeasurementerrorassociatedwitheachobservedvariable.
AppendixC.3. MeasurementEquations
AppendixC.3.1. FinancialLiteracy(FL)
Thelatentvariableforfinancialliteracy(η )ismeasuredbyfourobservedindicators:
FL
x = λ ·η +ϵ
FL1 FL1,FL FL FL1
x = λ ·η +ϵ
FL2 FL2,FL FL FL2
x = λ ·η +ϵ
FL4 FL4,FL FL FL4
x = λ ·η +ϵ
FL6 FL6,FL FL FL6
AppendixC.3.2. FinancialVulnerability(FV)
Thelatentvariableforfinancialvulnerability(η )ismeasuredbyfourteenobserved
FV
indicators:
x = λ ·η +ϵ
FV1 FV1,FV FV FV1
x = λ ·η +ϵ
FV2 FV2,FV FV FV2
x = λ ·η +ϵ
FV3 FV3,FV FV FV3
x = λ ·η +ϵ
FV4 FV4,FV FV FV4
x = λ ·η +ϵ
FV5 FV5,FV FV FV5
x = λ ·η +ϵ
FV6 FV6,FV FV FV6
x = λ ·η +ϵ
FV7 FV7,FV FV FV7
x = λ ·η +ϵ
FV8 FV8,FV FV FV8
x = λ ·η +ϵ
FV9 FV9,FV FV FV9
x = λ ·η +ϵ
FV10 FV10,FV FV FV10
x = λ ·η +ϵ
FV11 FV11,FV FV FV11
x = λ ·η +ϵ
FV12 FV12,FV FV FV12
x = λ ·η +ϵ
FV13 FV13,FV FV FV13
x = λ ·η +ϵ
FV14 FV14,FV FV FV14
AppendixC.3.3. FinancialFraud(FF)
Thelatentvariableforfinancialfraud(η )ismeasuredbyfourobservedindicators:
FF
x = λ ·η +ϵ
FF1 FF1,FF FF FF1
x = λ ·η +ϵ
FF2 FF2,FF FF FF2
x = λ ·η +ϵ
FF3 FF3,FF FF FF3
x = λ ·η +ϵ
FF4 FF4,FF FF FF4

Sustainability2025,17,9219
26of33
AppendixC.3.4. CognitiveReflectionTest(CR)
ThelatentvariableforCognitiveReflection(η )ismeasuredbyfiveobservedindicators:
CR
| x     | = λ      | ·η +ϵ  |
| ----- | -------- | ------ |
| CR1   | CR1,CR   | CR CR1 |
| x     | = λ      | ·η +ϵ  |
| CR2   | CR2,CR   | CR CR2 |
| x     | = λ      | ·η +ϵ  |
| CR3   | CR3,CR   | CR CR3 |
|       | =        | ·η +ϵ  |
| x CR5 | λ CR5,CR | CR CR5 |
| x     | = λ      | ·η +ϵ  |
| CR7   | CR7,CR   | CR CR7 |
AppendixC.3.5. CryptocurrencyKnowledge(CRY)
Thelatentvariableforcryptocurrencyknowledge(η CRY )ismeasuredbyfourobserved
indicators:
| x         | = λ           | ·η +ϵ       |
| --------- | ------------- | ----------- |
| Crypto1   | Crypto1,CRY   | CRY Crypto1 |
| x         | = λ           | ·η +ϵ       |
| Crypto2   | Crypto2,CRY   | CRY Crypto2 |
|           | =             | ·η +ϵ       |
| x Crypto3 | λ Crypto3,CRY | CRY Crypto3 |
| x         | = λ           | ·η +ϵ       |
| Crypto4   | Crypto4,CRY   | CRY Crypto4 |
AppendixC.3.6. FinancialPlanning(FP)
Thelatentvariableforfinancialplanning(η FP )ismeasuredbysixobservedindicators:
|       | =          | ·η +ϵ        |
| ----- | ---------- | ------------ |
| x FP1 | λ FP1,FP   | FP FP1       |
| x     | = λ        | ·η +ϵ        |
| FP2   | FP2,FP     | FP FP2       |
| x     | = λ        | ·η +ϵ        |
| FP3   | FP3,FP     | FP FP3       |
| x FP4 | = λ FP4,FP | ·η FP +ϵ FP4 |
| x     | = λ        | ·η +ϵ        |
| FP5   | FP5,FP     | FP FP5       |
|       | =          | ·η +ϵ        |
| x FP6 | λ FP6,FP   | FP FP6       |
Giventhatthesurveyitemsweremeasuredonanorderedcategoricalscale(dichoto-
mousorLikert-type),weperformedtheanalysisusingthepolychoriccorrelationmatrix
andtherobustDiagonallyWeightedLeastSquares(DWLS)estimator. Webasedtheeval-
uationofthemodelontheusualglobalfitindices,aswellasreliability,convergent,and
discriminantvalidityassessments.
AppendixC.3.7. OverallModelFit
OurCFAmodelshowsanexcelentfittothedata. TherobustComparativeFitIndex
(CFI = 0.954) and Tucker–Lewis Index (TLI = 0.950) exceed the 0.95 threshold, which
indicatesastrongcorrespondencebetweenourmodelandthedata. Also,theRootMean
SquareErrorofApproximation(knownasRMSEA=0.039)waswellbelowthe0.06cutoff
foraclosefit, witha90%confidenceintervalof[0.032, 0.045]thatfurthersupportsour
conclusion. Whiletheseindicessuggestaperfectglobalmodelfit,theStandardizedRoot
MeanSquareResidual(SRMR=0.114)iselevatedabovetherecommendedmaximumof
0.08. Thisresultmaysuggestthatwhiletheoverallmodelstructureissound,theremaybe
somelocalizedareasofmisfit.
AppendixC.3.8. ReliabilityandConvergentValidity
The internal consistency and convergent validity of the six factors were assessed.
CompositeReliability(CR)scoresindicatedgoodtoexcellentreliabilityforthemajority

Sustainability2025,17,9219 27of33
ofthefactors: financialvulnerability(CR=0.950),financialfraud(CR=0.803),Cognitive
ReflectionTest(CR=0.844),cryptocurrencyliteracy(CR=0.955),andfinancialplanning
(CR=0.845),allofwhichwerewellabovethe>0.70threshold. Thefinancialliteracyfactor
(CR=0.695)demonstratedborderlinebutacceptablereliability.
Convergent validity, as estimated by the Average Variance Extracted (AVE), regis-
tered strong levels in four of six factors, all of which exceeded the >0.50 threshold: fi-
nancialvulnerability(AVE=0.581), financialfraud(AVE=0.511), CognitiveReflection
Test(AVE=0.531),andcryptocurrencyliteracy(AVE=0.841). Onthecontrary,whilethe
financialplanningfactor(AVE=0.481)andthefinancialliteracyfactor(AVE=0.370)failed
topassthistest,thismeansthatsuchconstructssharelessthan50%ofthevarianceoftheir
respectiveindicationsinmeanterms. However,uponconsiderationofparameterestimates,
itemergedthatalloftheindividualfactorloadingsweresignificantstatistically(p<0.001)
withmostofthemshowingsubstantivelylargemagnitudes.
AppendixC.3.9. DiscriminantValidity
We find strong evidence for discriminant validity, which helps confirm that the
sixlatentconstructscanbeseenasempiricallydistinctfromoneanother. First,theFornell–
Larckercriterionwasmetforallpairsoffactors;thesquarerootoftheAVE(AVE)foreach
constructwasgreaterthanitscorrelationwithanyotherconstruct.Second,amorestringent
testusingtheHeterotrait–MonotraitRatioofCorrelations(HTMT)furthersupportedthese
findings. The highest observed HTMT value was 0.599 (between FV and FP), which is
wellbelowtheconservativethresholdof<0.85,whichprovidesrobustevidenceforthe
discriminantvalidityofallofthefactorsinourmodel.
AppendixC.3.10. ConclusiononMeasurementModelQuality
Weconclude,usingtheConfirmatoryFactorAnalysis,thatourproposedsix-factor
structure of the measurement instrument fits the data well on a global level, and the
constructsdemonstrateexcellentdiscriminantvalidityandgenerallyhighreliability. These
resultssuggestthemodelhasafirmfoundation.
Figure A1. Path diagram of the final six-factor Confirmatory Factor Analysis (CFA) model.
Ovals represent latent factors and rectangles represent observed indicators. Path values are
standardizedestimates.

Sustainability2025,17,9219
28of33
TableA3.Modelfitindicesandlatentfactorcorrelationsforthesix-factorCFAmodel.
PartA:Goodness-of-FitIndices
| χ2(df)          | CFI   | TLI   | RMSEA[90%CI]       | SRMR  |     |
| --------------- | ----- | ----- | ------------------ | ----- | --- |
| 849.845***(614) | 0.954 | 0.950 | 0.039[0.032,0.045] | 0.114 |     |
PartB:LatentFactorStandardizedCorrelations
| Factor                        | 1.        | 2.       | 3.    | 4. 5.     | 6.  |
| ----------------------------- | --------- | -------- | ----- | --------- | --- |
| 1.FinancialLiteracy(FL)       | –         |          |       |           |     |
| 2.FinancialVulnerability(FV)  | −0.380*** | –        |       |           |     |
| 3.FinancialFraud(FF)          | −0.292*   | 0.469*** | –     |           |     |
| 4.CognitiveReflectionTest(CR) | 0.415***  | −0.222** | 0.021 | –         |     |
| 5.CryptocurrencyLiteracy(CRY) | 0.135     | −0.146   | 0.021 | 0.274** – |     |
6.FinancialPlanning(FP) 0.522*** −0.642*** −0.375*** 0.217* 0.139 –
Note. N=256.FitindicesarebasedontherobustDWLSestimator.*p<0.05,**p<0.01,***p<0.001.
TableA4. StandardizedFactorLoadings(λ), CompositeReliability(CR),andAverageVariance
Extracted(AVE).
| Construct |     | Item | StandardizedLoading(λ) |     |     |
| --------- | --- | ---- | ---------------------- | --- | --- |
FinancialLiteracy(FL)
CR=0.695,AVE=0.370
|     |     | FL1 |     | 0.671 |     |
| --- | --- | --- | --- | ----- | --- |
|     |     | FL2 |     | 0.435 |     |
|     |     | FL4 |     | 0.585 |     |
|     |     | FL6 |     | 0.707 |     |
FinancialVulnerability(FV)
CR=0.950,AVE=0.581
|     |     | FV1  |     | 0.780 |     |
| --- | --- | ---- | --- | ----- | --- |
|     |     | FV2  |     | 0.778 |     |
|     |     | FV3  |     | 0.851 |     |
|     |     | FV4  |     | 0.829 |     |
|     |     | FV5  |     | 0.829 |     |
|     |     | FV6  |     | 0.778 |     |
|     |     | FV7  |     | 0.733 |     |
|     |     | FV8  |     | 0.839 |     |
|     |     | FV9  |     | 0.869 |     |
|     |     | FV10 |     | 0.816 |     |
|     |     | FV11 |     | 0.716 |     |
|     |     | FV12 |     | 0.493 |     |
|     |     | FV13 |     | 0.665 |     |
|     |     | FV14 |     | 0.592 |     |
FinancialFraud(FF)
CR=0.803,AVE=0.511
|     |     | FF1 |     | 0.673 |     |
| --- | --- | --- | --- | ----- | --- |
|     |     | FF2 |     | 0.530 |     |
|     |     | FF3 |     | 0.807 |     |
|     |     | FF4 |     | 0.812 |     |
CognitiveReflectionTest(CR)
CR=0.844,AVE=0.531
|     |     | CR1 |     | 0.979 |     |
| --- | --- | --- | --- | ----- | --- |
|     |     | CR2 |     | 0.644 |     |
|     |     | CR3 |     | 0.764 |     |
|     |     | CR5 |     | 0.633 |     |
|     |     | CR7 |     | 0.547 |     |
CryptocurrencyLiteracy(CRY)
CR=0.955,AVE=0.841
|     |     | Crypto1 |     | 0.888 |     |
| --- | --- | ------- | --- | ----- | --- |
|     |     | Crypto2 |     | 0.903 |     |
|     |     | Crypto3 |     | 0.968 |     |
|     |     | Crypto4 |     | 0.907 |     |

Sustainability2025,17,9219
29of33
TableA4.Cont.
| Construct |     |     | Item | StandardizedLoading(λ) |     |     |
| --------- | --- | --- | ---- | ---------------------- | --- | --- |
FinancialPlanning(FP)
CR=0.845,AVE=0.481
|     |     |     | FP1 | 0.791 |     |     |
| --- | --- | --- | --- | ----- | --- | --- |
|     |     |     | FP2 | 0.614 |     |     |
|     |     |     | FP3 | 0.591 |     |     |
|     |     |     | FP4 | 0.608 |     |     |
|     |     |     | FP5 | 0.711 |     |     |
|     |     |     | FP6 | 0.811 |     |     |
Note.Allfactorloadingsarestatisticallysignificantatp<0.001.
TableA5.Constructreliabilityandconvergentvaliditystatistics.
Factor CompositeReliability(CR) AverageVarianceExtracted(AVE)
| F   |     | 0.695 |     | 0.370 |     |     |
| --- | --- | ----- | --- | ----- | --- | --- |
L
| F V |     | 0.950 |     | 0.581 |     |     |
| --- | --- | ----- | --- | ----- | --- | --- |
| F F |     | 0.803 |     | 0.511 |     |     |
| C   |     | 0.844 |     | 0.531 |     |     |
R
| CRY |     | 0.955 |     | 0.841 |     |     |
| --- | --- | ----- | --- | ----- | --- | --- |
| F   |     | 0.845 |     | 0.481 |     |     |
P
Note. ThresholdsforgoodpsychometricpropertiesaretypicallyCR>0.70andAVE>0.50.
TheresultsfromtheFornell–Larckercriterionanalysisprovidestrongevidencefor
thediscriminantvalidityofthesix-factormodel. Asshowninthetable,thesquarerootof
theAVEforeachlatentconstructwasgreaterthanitscorrelationwithanyotherconstruct,
indicatingthateachfactorisstatisticallydistinct.
TableA6.DiscriminantvalidityassessmentusingtheFornell–Larckercriterion.
| Factor | F     | F   | F   | C   | CRY | F   |
| ------ | ----- | --- | --- | --- | --- | --- |
|        | L     | V   | F   | R   |     | P   |
| F      | 0.609 |     |     |     |     |     |
L
| F V | −0.380 | 0.762 |       |     |     |     |
| --- | ------ | ----- | ----- | --- | --- | --- |
| F   | −0.292 | 0.469 | 0.715 |     |     |     |
F
−0.222
| C R | 0.415 |        | 0.021  | 0.729 |       |       |
| --- | ----- | ------ | ------ | ----- | ----- | ----- |
| CRY | 0.135 | −0.146 | 0.021  | 0.274 | 0.917 |       |
| F   | 0.522 | −0.642 | −0.375 | 0.217 | 0.139 | 0.693 |
P
Note. Diagonalelements(inbold)arethesquarerootoftheAverageVarianceExtracted(AVE).Fordiscrimi-
nantvalidity,diagonalelementsmustbegreaterthantheoff-diagonalcorrelationsinthecorrespondingrows
andcolumns.
References
1. Lusardi,A.;Mitchell,O.S. FinancialLiteracyandPlanning:ImplicationsforRetirementWellbeing.InTheRoutledgeHandbookof
FinancialLiteracy;Oliver,B.;Young,C.,Eds.;Routledge:NewYork,NY,USA,2014.
2. VanRooij,M.;Lusardi,A.;Alessie,R. FinancialliteracyandretirementplanningintheNetherlands. J.Econ. Psychol. 2011,
32,593–608.[CrossRef]
3. Batinga,G.L.;Castro,A.S.;Almeida,L.K.d.S.D. EducaçãoFinanceira,CondiçãoSocioculturaleVulnerabilidade:umaanálise
dasaúdeebem-estarfinanceirodefamíliasmonoparentaisfemininas. InProceedingsoftheAnaisdoEncontrodaAssociação
NacionaldePós-GraduaçãoePesquisaemAdministração,ANPAD,Fortaleza,Brazil,16–18May2019.
4. Camargo,R.Z.;Junior,M.F.;Strehlau,S. VulnerabilidadeeEducaçãoFinanceira:AVisãodeGerentesdeBanco;RevistaInterdisciplinar
deMarketing:SãoPaulo,Brazil,2020.
5. Banco Central do Brasil. Relatório de Letramento Financeiro. 2023. Available online: https://www.bcb.gov.br/content/
cidadaniafinanceira/documentos_cidadania/letramento/relatorio-de-letramento-financeiro.pdf(accessedon23June2025).
6. Akande, J.; Hosu, Y.; Kabiti, H.; Ndhleve, S.; Garidzirai, R. Financialliteracyandinclusionforruralagrarianchangeand
sustainablelivelihoodintheEasternCape,SouthAfrica. Heliyon2023,9,e16330.[CrossRef]

Sustainability2025,17,9219 30of33
7. Zaimovic,A.; Torlakovic,A.; Arnaut-Berilo,A.; Zaimovic,T.; Dedovic,L.; NuhicMeskovic,M. Mappingfinancialliteracy:
Asystematicliteraturereviewofdeterminantsandrecenttrends. Sustainability2023,15,9358.[CrossRef]
8. UNCapitalDevelopmentFund(UNCDF).FinancialInclusionandtheSDGs. Availableonline:https://www.uncdf.org/financial-
inclusion-and-the-sdgs?ref=hackernoon.com(accessedon20April2025).
9. Kyeyune, G.N.; Ntayi, J.M. Empoweringruralcommunities: Theroleoffinancialliteracyandmanagementinsustainable
development. Front.Hum.Dyn.2025,6,1424126.[CrossRef]
10. Swiecka,B.;Yes¸ildag˘,E.;Özen,E.;Grima,S. Financialliteracy:ThecaseofPoland. Sustainability2020,12,700.[CrossRef]
11. Garg,N.;Singh,S. Financialliteracyamongyouth. Int.J.Soc.Econ.2016,45,173–186.[CrossRef]
12. Goyal,K.;Kumar,S. Financialliteracy:Asystematicreviewandbibliometricanalysis. Int.J.Consum.Stud.2020,45,173–186.
[CrossRef]
13. Anshika.;Singla,A. Financialliteracyofentrepreneurs:Asystematicreview. Manag.Financ.2021,48,1352–1371.[CrossRef]
14. Haag,L.;Brahm,T. TheGenderGapinEconomicandFinancialLiteracy:AReviewandResearchAgenda. Int.J.Consum.Stud.
2025,49,e70031.[CrossRef]
15. Negi,P.;Jaiswal,A. Impactoffinancialliteracyonconsumerfinancialbehavior:Asystematicreviewandresearchagendausing
TCCMframework. Int.J.Consum.Stud.2024,48,e13053.[CrossRef]
16. Atkinson,A.;Messy,F.A. MeasuringFinancialLiteracy:ResultsoftheOECD/InternationalNetworkonFinancialEducation(INFE)Pilot
Study; TechnicalReport15,OECDWorkingPapersonFinance,InsuranceandPrivatePensions;OECDPublishing:Paris,France,
2012.[CrossRef]
17. Campbell,J.Y. RestoringRationalChoice: TheChallengeofConsumerFinancialRegulation. Annu. Rev. Econ. 2016,8,1–23.
[CrossRef]
18. Fernandes,D.;Lynch,J.G.,Jr.;Netemeyer,R.G. Financialliteracy,financialeducation,anddownstreamfinancialbehaviors.
Manag.Sci.2014,60,1861–1883.[CrossRef]
19. Huston,S.J. Measuringfinancialliteracy. J.Consum.Aff.2010,44,296–316.[CrossRef]
20. Lusardi,A.;Tufano,P. DebtLiteracy,FinancialExperiences,andOverindebtedness. BrookingsPap.Econ.Act.2015,2015,139–182.
[CrossRef]
21. Mandell,L. TheFinancialLiteracyofYoungAmericanAdults:Resultsofthe2008NationalJumptartCoalitionSurveyofHighSchool
SeniorsandCollegeStudents; TechnicalReport;JumptartCoalitionforPersonalFinancialLiteracy:Washington,DC,USA,2008.
22. OECD.OECD/INFEInternationalSurveyofAdultFinancialLiteracyCompetencies;TechnicalReport;OECDPublishing:Paris,France,
2016.
23. Remund,D.L. FinancialLiteracyExplicated:TheCaseforaClearerDefinitioninanIncreasinglyComplexEconomy. J.Financ.
Couns.Plan.2010,21,66–81.[CrossRef]
24. Sherraden,M.;Johnson,L.;Elliott,W.;Porterfield,S.;Rathbun,A. FinancialCapabilityinChildren:EffectsofParticipationina
School-BasedFinancialEducationandSavingsProgram. J.Sociol.Soc.Welf.2011,38,69–91.[CrossRef]
25. Bucher-Koenen,T.;Lusardi,A. FinancialLiteracyandRetirementPlanninginGermany. J.PensionEcon.Financ.2011,10,565–584.
[CrossRef]
26. Lusardi,A.;Mitchell,O.S. Financialliteracyandretirementplanning: NewevidencefromtheRANDAmericanLifePanel.
J.PensionEcon.Financ.2011,10,509–525.[CrossRef]
27. Hastings,J.S.;Madrian,B.C.;Skimmyhorn,W.L. Financialliteracy,financialeducation,andeconomicoutcomes. Annu.Rev.Econ.
2013,5,347–373.[CrossRef][PubMed]
28. Hsu,J. Agingandstrategiclearning:Theimpactofspousalincentivesonfinancialliteracy. J.Hum.Resour.2016,51,1036–1067.
[CrossRef]
29. Jappelli,T.;Padula,M. Investmentinfinancialliteracyandsavingdecisions. J.Bank.Financ.2013,37,2779–2792.[CrossRef]
30. Lusardi,A.;Mitchell,O.S. Financialliteracyandretirementpreparedness:Evidenceandimplicationsforfinancialeducation.
Bus.Econ.2007,42,35–44.[CrossRef]
31. Vitt,L.;Anderson,C.;Kent,J.;Lyter,D.M.;Siegenthaler,J.K.;Ward,J.PersonalFinanceandtheRushtoCompetence:FinancialLiteracy
EducationintheUS;InstituteforSocio-FinancialStudies:Middleburg,VA,USA,2000.
32. FinancialIndustryRegulatoryAuthority(FINRA). Non-TraditionalCostsofFinancialFraud; TechnicalReport;FINRA:Washington,
DC,USA,2015.
33. Gilovich,T.;Kumar,A.;Jampol,L. Awonderfullife:Experientialconsumptionandthepursuitofhappiness. J.Consum.Psychol.
2015,25,152–165.[CrossRef]
34. Isaia,E.;Oggero,N.;Sandretto,D. Isfinancialliteracyaprotectiontoolfromonlinefraudinthedigitalera? J.Behav.Exp.Financ.
2024,44,100977.[CrossRef]
35. Tabak,B.M.;Silva,E.B.;Horta,R.;Christiano,T.;Tabak,G.C. ModelingFinancialLiteracyUsingMultilevelItemResponseTheory
andtheCOVID-19Pandemic.2023. Availableonline:https://ssrn.com/abstract=4368359(accessedon1August2025).

Sustainability2025,17,9219 31of33
36. Paradgma;DataFolha. PrimeiraPesquisaNacionaldasCriptomoedas.2025. Availableonline:https://criptopelobrasil.com.br/
(accessedon10August2025).
37. Zhang,Y.;Chatterjee,S. Financialwell-beingintheUnitedStates:Therolesoffinancialliteracyandfinancialstress. Sustainability
2023,15,4505.[CrossRef]
38. Kahneman,D.;Tversky,A.ProspectTheory.AnAnalysisofDecisionMakingUnderRisk;WorldScientific:Singapore,1977.[CrossRef]
39. Kahneman,D.;Frederick,S. RepresentativenessRevisited:AttributeSubstitutioninIntuitiveJudgment.InHeuristicsandBiases:
ThePsychologyofIntuitiveJudgment;Gilovich,T.,Griffin,D.,Kahneman,D.,Eds.;CambridgeUniversityPress:NewYork,NY,
USA,2002;pp.49–81.
40. FinancialLiteracySurvey. FinancialLiteracySurvey2022:Results; TechnicalReport;PublicRelationsDepartment,BankofJapan:
Tokyo,Japan,2022.
41. Chalmers,R.P. mirt:AMultidimensionalItemResponseTheoryPackagefortheREnvironment. J.Stat.Softw.2012,48,1–29.
[CrossRef]
42. Anderloni,L.;Bacchiocchi,E.;Vandone,D. Householdfinancialvulnerability:Anempiricalanalysis. Res.Econ.2012,66,284–296.
[CrossRef]
43. Al-Omoush,K.S.;Gomez-Olmedo,A.M.;Funes,A.G.Whydopeoplechoosetocontinueusingcryptocurrencies? Technol.Forecast.
Soc.Change2024,200,123151.[CrossRef]
44. Eren,B.M.;Taspinar,N.;Gokmenoglu,K.K. Theimpactoffinancialdevelopmentandeconomicgrowthonrenewableenergy
consumption:EmpiricalanalysisofIndia. Sci.TotalEnviron.2019,663,189–197.[CrossRef]
45. Ye,J.;Kulathunga,K.M.M.C.B. HowdoesfinancialliteracypromotesustainabilityinSMEs?Adevelopingcountryperspective.
Sustainability2019,11,2990.[CrossRef]
46. Waller,L.G.;Johnson,S. ThepossiblecontributivevalueofcryptocurrenciestoSmallIslandDevelopingStates. Int.J.Blockchains
Cryptocurrencies2022,3,60–79.[CrossRef]
47. Alharbi,A.;Sohaib,O. TechnologyReadinessandCryptocurrencyAdoption:PLS-SEMandDeepLearningNeuralNetwork
Analysis. IEEEAccess2021,9,21388–21394.[CrossRef]
48. Toufaily,E. Anintegrativemodeloftrusttowardcrypto-tokensapplications:Acustomerperspectiveapproach. Digit.Bus.2022,
2,100041.[CrossRef]
49. Sonkurt,H.; Altinöz,A. Cryptocurrencyinvestment: Asafeventureoranewtypeofgambling? J.Gambl. Issues2021,47.
[CrossRef]
50. KiatSakared, P.; Chen, K.Y. The effect of flow experience on online game addiction during the COVID-19 pandemic:
Themoderatingeffectofactivitypassion. Sustainability2022,14,12364.[CrossRef]
51. Mashatan,A.;Sangari,M.S.;Dehghani,M. Howperceptionsofinformationprivacyandsecurityimpactconsumertrustin
crypto-payment:Anempiricalstudy. IEEEAccess2022,10,69441–69454.[CrossRef]
52. Hariguna,T.;Ruangkanjanases,A.;Madon,B.B.;Alfawaz,K.M. Assessingdeterminantsofcontinuanceintentiontowardcryp-
tocurrencyusage:Extendingexpectationconfirmationmodelwithtechnologyreadiness. SAGEOpen2023,13,21582440231160439.
[CrossRef]
53. Limayem,M.;Cheung,C.M. PredictingthecontinueduseofInternet-basedlearningtechnologies:theroleofhabit. Behav.Inf.
Technol.2011,30,91–99.[CrossRef]
54. Venkatesh,V.;Davis,F.D.;Morris,M.G.;Davis,G.B.;D.,F. Useracceptanceofinformationtechnology:Towardaunifiedview.
MISQ.2012,27,425–478.[CrossRef]
55. Sirohi,N.;Misra,G. Vulnerabilityofindividualstoeconomiccrimeandtheroleoffinancialliteracyinitsprevention:Evidence
fromIndia. InCrime,LawandSocialChange;Springer:Berlin/Heidelberg,Germany,2024;pp.1–32.[CrossRef]
56. Frederick,S. Cognitivereflectionanddecisionmaking. J.Econ.Perspect.2005,19,25–42.[CrossRef]
57. Jensen,A.R. ThegFactor:TheScienceofMentalAbility;Praeger:Westport,CT,USA,1998.
58. Epstein,S. IntegrationoftheCognitiveandPsychodynamicUnconscious. Am.Psychol.1994,49,709–724.[CrossRef]
59. Sloman,S.A. TheEmpiricalCaseforTwoSystemsofReasoning. Psychol.Bull.1996,119,3–22.[CrossRef]
60. Chaiken,S.;Trope,Y. Dual-ProcessTheoriesinSocialPsychology;GuilfordPress:NewYork,NY,USA,1999.
61. Putler,D.S. IncorporatingReferencePriceEffectsintoaTheoryofConsumerChoice. Mark.Sci.1992,11,287–309.[CrossRef]
62. Tversky,A.;Kahneman,D. AdvancesinProspectTheory: CumulativeRepresentationofUncertainty. InChoices,Values,and
Frames;SpringerNature:Berlin/Heidelberg,Germany, 2000;pp.44–66.[CrossRef]
63. Wang,M.;Rieger,M.O.;Hens,T. TheImpactofCultureonLossaversion. J.Behav.Decis.Mak.2016,30,270–281.[CrossRef]
64. Banerjee,A.V. Asimplemodelofherdbehavior. Q.J.Econ.1992,107,797–817.[CrossRef]
65. Raafat,R.M.;Chater,N.;Frith,C. Herdinginhumans. TrendsCogn.Sci.2009,13,420–428.[CrossRef]
66. DaGamaSilva,P.V.J.;Klotzle,M.C.;Pinto,A.C.F.;Gomes,L.L. Herdingbehaviorandcontagioninthecryptocurrencymarket.
J.Behav.Exp.Financ.2019,22,41–50.[CrossRef]
67. Kahneman,D. Thinking,FastandSlow;Farrar,StrausandGiroux:NewYork,NY,USA,2011.

Sustainability2025,17,9219 32of33
68. Thaler,R.H.;Benartzi,S. SaveMoreTomorrow™:Usingbehavioraleconomicstoincreaseemployeesaving. J.PoliticalEcon.2004,
112,S164–S187.[CrossRef]
69. Loewenstein,G.;Thaler,R. Anomalies:IntertemporalChoice. J.Econ.Perspect.1989,3,181–193.[CrossRef]
70. Hershfield,H.E.;Goldstein,D.G.;Sharpe,W.F.;Fox,J.;Yeykelis,L.;Carstensen,L.L.;Bailenson,J.N. IncreasingSavingBehavior
ThroughAge-ProgressedRenderingsoftheFutureSelf. J.Mark.Res.2011,48,S23.[CrossRef]
71. Yes¸ilkayalı,D. ProcrastinationandFutureDiscounting. J.Int.Soc.Res.2025,7,275.
72. Sheffer,C.E.;MacKillop,J.;Fernandez,A.;Christensen,D.;Bickel,W.K.;Johnson,M.W.;Mathew,M. InitialExaminationof
PrimingTaskstoDecreaseDelayDiscounting. Behav.Processes2016,128,144–152.[CrossRef]
73. Witten,I.H.;Frank,E. PracticalMachineLearningToolsandTechniques,2nded.;Elsevier:Amsterdam,TheNetherlands,2005.
74. Oliveira,B.L.C.A.d.;Thomaz,E.B.A.F.;Silva,R.A.d. Theassociationbetweenskincolor/raceandhealthindicatorsinelderly
Brazilians:AstudybasedontheBrazilianNationalHouseholdSampleSurvey(2008). Cad.SaúdePública2014,30,1438–1452.
[CrossRef][PubMed]
75. Paixão,M.;Rossetto,I.;Montovanele,F.;Carvano,L.M. RelatórioAnualdasDesigualdadesRaciaisnoBrasil:2009–2010;Garamond:
RiodeJaneiro,Brazil,2010.
76. daSilvaPaiva,L.;Oliveira,F.R.;deAlcantaraSousa,L.V.;dosSantosFigueiredo,F.W.;deSá,T.H.;Adami,F. DeclineinStroke
MortalityBetween1997and2012bySex:EcologicalStudyinBraziliansAged15to49Years. Sci.Rep.2019,9,2962.[CrossRef]
[PubMed]
77. Jiang,T.;Gradus,J.L.;Rosellini,A.J. SupervisedMachineLearning:ABriefPrimer. Behav.Ther.2020,51,675–687.[CrossRef]
78. Silva,T.C.;Braz,T.;Tabak,B.M. Mappingthelandscapeofenergymarketsresearch: Abibliometricanalysisandpredictive
assessmentusingmachinelearning. EnergyEcon.2024,136,107698.[CrossRef]
79. Taunk,K.;De,S.;Verma,S.;Swetapadma,A. ABriefReviewofNearestNeighborAlgorithmforLearningandClassification.
InProceedingsofthe2019InternationalConferenceonIntelligentComputingandControlSystems(ICCS),Madurai,India,
15–17May2019;pp.1255–1260.[CrossRef]
80. Cortes,C.;Vapnik,V. Support-VectorNetworks. Mach.Learn.1995,20,273–297.[CrossRef]
81. Breiman,L. Randomforests. Mach.Learn.2001,45,5–32.[CrossRef]
82. Rumelhart,D.E.;McClelland,J.L.,LearningInternalRepresentationsbyErrorPropagation. InParallelDistributedProcessing:
ExplorationsintheMicrostructureofCognition:Foundations;MITPress:Cambridge,MA,USA,1987;pp.318–362.
83. Zou,H.;Hastie,T. RegularizationandVariableSelectionViatheElasticNet. J.R.Stat.Soc.Ser.BStat.Methodol.2005,67,301–320.
[CrossRef]
84. Kumar,S.;Bhatnagar,V. AReviewofRegressionModelsinMachineLearning. J.Intell.Syst.Comput.2021,2,40–47.[CrossRef]
85. Carvalho,D.V.;Pereira,E.M.;Cardoso,J.S. MachineLearningInterpretability:ASurveyonMethodsandMetrics. Electronics
2019,8,832.[CrossRef]
86. Hermosilla,P.;Berríos,S.;Allende-Cid,H. ExplainableAIforForensicAnalysis:AComparativeStudyofSHAPandLIMEin
IntrusionDetectionModels. Appl.Sci.2025,15,7329.[CrossRef]
87. Lundberg,S.M.;Lee,S.I. Aunifiedapproachtointerpretingmodelpredictions. Adv.NeuralInf.Process.Syst.2017,30,4768–4777.
88. Ribeiro,M.T.;Singh,S.;Guestrin,C. “Whyshoulditrustyou?”Explainingthepredictionsofanyclassifier. InProceedingsofthe
22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,SanFrancisco,CA,USA,13–17August
2016;pp.1135–1144.
89. PesquisaDataSenado. PanoramaPolítico2024:ApostasEsportivas,GolpesDigitaiseEndividamento;InstitutodePesquisaDataSenado:
Brasilia,Brazil,2024.
90. Sundarasen,S.;Rajagopalan,U.;Ibrahim,I.FinancialSustainabilityThroughLiteracyandRetirementPreparedness. Sustainability
2024,16,10692.[CrossRef]
91. Tulcanaza-Prieto,A.B.;Cortez-Ordoñez,A.;Rivera,J.;Lee,C.W. IsDigitalLiteracyaModeratorVariableintheRelationship
BetweenFinancialLiteracy,FinancialInclusion,andFinancialWell-BeingintheEcuadorianContext? Sustainability2025,17,2476.
[CrossRef]
92. FundaçãoGetulioVargas. IndicadordeIncertezadaEconomia(IIE-Br)—IndicadorMensaldeAbrilde2025.2025.Available
online:https://portalibre.fgv.br/indicador-de-incerteza-da-economia(accessedon21May2025).
93. Katnic,I.; Katnic,M.; Orlandic,M.; Radunovic,M.; Mugosa,I. UnderstandingtheRoleofFinancialLiteracyinEnhancing
EconomicStabilityandResilienceinMontenegro:AData-DrivenApproach. Sustainability2024,16,11065.[CrossRef]
94. Sarker,I.H. MachineLearning: Algorithms,Real-WorldApplicationsandResearchDirections. SNComput. Sci. 2021,2,160.
[CrossRef]
95. deLimaLemos,R.A.; Silva,T.C.; Tabak,B.M. Propensiontocustomerchurninafinancialinstitution: Amachinelearning
approach. NeuralComput.Appl.2022,34,11751–11768.[CrossRef]

Sustainability2025,17,9219 33of33
96. Schonlau,M.;Zou,R.Y. Therandomforestalgorithmforstatisticallearning. StataJ.2020,20,3–29.[CrossRef]
97. Rosseel,Y. lavaan:AnRPackageforStructuralEquationModeling. J.Stat.Softw.2011,48,1–36.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.