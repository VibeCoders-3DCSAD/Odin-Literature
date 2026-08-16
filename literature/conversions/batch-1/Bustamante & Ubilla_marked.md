---
conversion_metadata:
  converted_at: "2026-07-22T12:29:05Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Bustamante & Ubilla.pdf"
  source_pdf_sha256: "7ec2413f3a50e32114f4d1e8ad255de1c20194182cde3dc2a4a1d4a7fd011326"
  page_count: 18
  markdown_char_count: 135274
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Retail investor behavior and social 
media signals: exploring 
attention dynamics
Diana Bustamante
Faculty of Business and Economics, Universidad Andres Bello, Santiago, Chile, and
Alejandra Ubilla
Facultad de Econom�ıa y Negocios, Universidad Santo Tomas, Santiago, Chile

Journal of 
Economics, 
Finance and 
Administrative 
Science

Received 19 October 2025 
Revised 16 December 2025 
10 February 2026 
17 March 2026 
Accepted 18 March 2026

Abstract
Purpose – This study aims to investigate how social media recommendations influence investor attention and 
retail investor activity in stock investing.
Design/methodology/approach – Using data from the Organisation for Economic Co-operation and 
Development (OECD)’s 2023 Adult Financial Literacy Survey across a sample of countries, the analysis 
employs a logistic regression model. To address potential endogeneity, both instrumental variable and 
propensity score matching techniques are applied.
Findings – Investor attention to social media influencers shows a positive and significant effect on stock 
investment. After adjusting for endogeneity, the main results remain robust. However, the moderating role of 
digital financial literacy is not consistent across all countries in the sample.
Research limitations/implications – The influencer recommendation question was newly introduced in this 
survey, limiting longitudinal comparisons. Additionally, the results are based on self-reported data from four 
countries.
Originality/value – This research contributes to the emerging field of digital behavioral finance and offers 
insights for the design of financial inclusion and education policies in increasingly digital environments.
Keywords Investor attention, Social media, Stock investment, Digital financial literacy,
Investment decision-making, Digital financial behavior
Paper type Research article

1. Introduction
The growing influence of social media on the financial behavior of retail investors has 
attracted significant academic attention in recent years. These platforms have profoundly 
reshaped how investors access, interpret and process financial information, partially 
displacing traditional media outlets (M€unster et al., 2024). Their capacity for virality, 
immediacy and social validation has positioned social media as a key channel for 
disseminating market signals, raising concerns among regulators and market participants 
about its potential to trigger suboptimal investment decisions (Barber et al., 2022).

From a behavioral perspective, a wide body of literature has examined the role of cognitive 
resources, overconfidence as a behavioral bias and limited attention as a scarce resource 
(Kahneman, 1973), noting that these factors may amplify market noise and undermine the 
efficiency of price formation processes (Alfieri et al., 2025). These effects are further 
exacerbated in digital environments, where decision-making rationality is increasingly 
challenged (Warkulat and Pelster, 2024). Despite advances in this field, the literature has yet to 
thoroughly explore the mechanisms through which social media recommendations capture the

JEL Classification — G11, G40, G41, G53

© Diana Bustamante and Alejandra Ubilla. Published in Journal of Economics, Finance and 
Administrative Science. Published by Emerald Publishing Limited. This article is published under the 
Creative Commons Attribution (CC BY 4.0) licence. Anyone may reproduce, distribute, translate and 
create derivative works of this article (for both commercial and non-commercial purposes), subject to full 
attribution to the original publication and authors. The full terms of this licence maybe seen at Link to the 
terms of the CC BY 4.0 licence.

Journal of Economics, Finance and 
Administrative Science 
Emerald Publishing Limited 
e-ISSN: 2218-0648 
p-ISSN: 2077-1886 
DOI 10.1108/JEFAS-10-2025-0378

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 2 -->

JEFAS

attention of individual investors and shape their willingness to participate in equity markets. 
Recent studies have mostly focused on specific phenomena or asset classes, including short-
termism in investment behavior (Kim, 2025), disposition effect (Chen and Ren, 2025) or 
cryptocurrency investment (Kim and Fan, 2025), without addressing how these platforms 
interact with critical individual competencies such as digital financial literacy (DFL).

DFL has emerged as a key competency to navigate the challenges of the digital financial 
ecosystem by enabling individuals to efficiently access, understand and use financial 
information (Mazzoli and Baiocco, 2025). Recent evidence shows that developing DFL is 
essential for the effective use of digital financial services and for managing associated risks; 
however, despite widespread digitalization, its effects on individuals’ financial behavior and 
overall financial awareness remain insufficiently understood (Bhat et al., 2024). Moreover, 
little is known about the moderating role of DFL in shaping the influence of social media 
recommendations.

In parallel, a growing body of international literature has emphasized the importance of 
DFL across diverse settings. For instance, Pak et al. (2026), drawing on evidence from South 
Korea, suggest that DFL is a key determinant of both the adoption of and the benefits derived 
from digital financial services, thereby contributing to financial inclusion in the digital era. In 
northern India, Showkat et al. (2025) demonstrated that financial literacy enhances the use of 
digital financial services and serves as a critical mechanism for women’s economic 
empowerment, promoting gender equality. In the same country, Maheshwari and Samantaray 
(2025) find that financial literacy, together with artificial intelligence (AI)-based digital 
advisory services, encourages more rational investment decisions. Moreover, cross-country 
comparative studies highlight the role of financial capability in fostering digital monetary 
innovation, suggesting that strengthening financial literacy should be a strategic component in 
the design and implementation of central bank digital currencies across different national 
contexts (Mertzanis et al., 2025).

In this respect, the present study aims to analyze the relationship between attention to social 
media influencer recommendations and the decision to invest in the stock market, considering 
the moderating role of DFL. For this purpose, a logistic regression model is employed using 
individual-level  data  from  the  2023  Organisation  for  Economic  Co-operation  and 
Development (OECD)/International Network on Financial Education Survey (INFE) of 
Adult Financial Literacy, covering four countries with diverse socioeconomic environments: 
Brazil, Finland, the Philippines and Saudi Arabia. The study is guided by the following 
research questions: To what extent do influencer recommendations on social media influence 
individuals’ decisions to invest in the stock market? What role does DFL play in moderating 
this relationship?

This research offers a novel contribution by examining an understudied phenomenon from 
an international comparative perspective, integrating both behavioral and digital variables. 
Moreover, it provides empirical evidence from a heterogeneous group of countries, allowing 
for the analysis of contextual differences in investor behavior. By combining social media 
attention and DFL levels, the study aligns with an emerging body of literature, aiming to 
understand the cognitive and technological determinants of financial decision-making in 
contemporary digital environments (Anwar, 2025).

The structure of the paper is as follows: Section 2 reviews the literature and presents the 
theoretical framework, Section 3 describes the study methodology, Section 4 reports the 
results, Section 5 discusses the findings and Section 6 concludes.

2. Literature review
In recent years, social media platforms have emerged as a key channel for shaping financial 
expectations and investment behavior among retail investors (Reichenbach and Walther, 2025). 
This influence stems not only from their ability to capture attention but also from their role as 
providers of qualitative information about companies, which significantly affects investment

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 3 -->

Journal of 
Economics, 
Finance and 
Administrative 
Science

decisions (Bayar and Kesici, 2024). These platforms have been identified as behavioral drivers 
that shape short-term investment decisions, particularly among younger individuals who tend to 
exhibit overconfidence in their financial knowledge (Kim, 2025). Despite these advances, much 
of the existing literature relies on single-country case studies or nationally limited samples, 
which restrict the generalizability of the findings (Ly�ocsa et al., 2023). This national focus limits 
the understanding of the underlying mechanisms from a global perspective. Meanwhile, social 
media increasingly shapes markets: cases such as GameStop (Pedersen, 2022) and Twitter 
effects (Carosia et al., 2020) illustrate how social media operates as a behavioral determinant of 
investment decisions across highly diverse environments. Even in countries with high levels of 
digital literacy, such as Finland, young adults report spending between 35 and 42 h per week 
online, with nearly 20 of those hours dedicated exclusively to social media use (Hylkil€a et al., 
2023). Studies often rely on aggregated data, rarely examining individual influencer attention as 
an investment “attention shock” or comparing across countries. This limits micro-level evidence 
on how digital attention affects behavior. Since attention narrows choices and influencers can 
redirect it toward specific stocks, followers are more likely to invest.

The concept of digital finance has emerged as a response to rapid technological 
advancements in the financial sector (Al-Smadi, 2023), prompting individuals to acquire new 
competencies to navigate digital environments. Within this context, DFL has become essential 
for fostering informed, autonomous and responsible financial behavior (OECD, 2023). This 
competency enables individuals to analyze financial products, critically assess digital 
information and make rational investment decisions (Abdallah et al., 2024). Empirical studies 
have demonstrated that higher levels of DFL are associated with improved investment 
outcomes and more effective retirement planning (Mazzoli and Baiocco, 2025). However, 
concerns remain about the reliability of social media as an information source. Wang et al. 
(2024) suggest that content disseminated by financial influencers is often low in analytical 
quality and high in emotional appeal, increasing the behavioral risks for retail investors. While 
prior literature has explored how digital competencies influence financial behavior in single-
country contexts, such as Sweden (Hermansson et al., 2022) or China (Wang et al., 2024), few 
studies have systematically examined how the moderating role of DFL varies across countries 
with distinct institutional and technological landscapes. This gap is especially important, given 
the increasing globalization of digital financial content.

Given that influencers generate attention-grabbing events that particularly affect less 
sophisticated investors, it would be reasonable to expect that individuals with higher digital 
competencies would be less susceptible to such influence. DFL would provide analytical skills 
and critical thinking that would help individuals assess the quality of information and avoid 
impulsive choices, thereby attenuating the impact of attention to social media influencers on 
investment decisions.

2.1 Theoretical framework
The attention theory proposed by Barber and Odean (2008) offers a framework for 
understanding how stimuli originating from social media could influence individual financial 
behavior. This theory posits that attention functions as a selection mechanism prior to decision-
making, determining which alternatives are considered before preferences shape the final 
choice. Because individual investors face a large universe of potential stocks, they tend to 
simplify their search process by focusing on those that have recently captured their attention. 
Although not all attention-grabbing stocks are ultimately purchased, the authors show that 
investors only buy stocks that have succeeded in attracting their attention. In this sense, 
influencers operate as agents who generate “attention-grabbing events,” capable of directing 
attention toward specific assets, similar to what occurs in traditional media such as Consumer 
News and Business Channel (CNBC), where a single mention can multiply trading volume 
within minutes. Thus, when an influencer highlights a stock, they produce an attention event 
that increases the likelihood that an individual investor will consider purchasing it.

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 4 -->

JEFAS

Barber and Odean (2008) argue that individual investors face limited attention and rely on 
salient cues, while professionals reduce such constraints through systematic search, analytical 
tools and deeper fundamental analysis, recognizing that highlighted information is often 
already priced in. Higher DFL should make individuals behave more like professionals by 
improving  risk  understanding,  critical  evaluation  and  structured  decision-making. 
Consequently, reliance on salient cues declines, which could reduce susceptibility to social 
media influencer recommendations. As an alternative to Barber and Odean (2008), the limited 
attention theory developed by Hirshleifer and Teoh (2003) emphasizes that investors face 
cognitive constraints that affect not only which assets they consider but also how they process 
available information. Investors tend to assimilate salient, low-cognitive-cost information 
more easily, while economically relevant information may be ignored if it fails to attract 
attention. These limitations contribute to distortions in asset valuation and to the persistence of 
market inefficiencies, as neither arbitrage nor professional analysis fully corrects price 
misalignments. Taken together, this theory complements Barber and Odean (2008) by 
explaining the underlying cognitive mechanisms that allow attention-driven effects on 
investment decisions to persist in financial markets.

Taken together, this theoretical framework suggests that signals emitted by social media 
influencers would operate as attention-grabbing events that would increase the likelihood that 
individuals consider investing in stocks, while higher levels of DFL would attenuate this effect 
by reducing reliance on salient cues in the decision-making process. Therefore, consistent with 
the theoretical framework, the following hypotheses are proposed:

H1. Social media signals from influencers increase individuals’ propensity to invest in

H2.

stocks.
Individuals with higher digital financial literacy reduce the likelihood of social media 
influence on their investment decisions.

3. Method
3.1 Research design/model
This study uses microdata from the OECD/INFE 2023 International Survey of Adult Financial 
Literacy and focuses on Brazil, Finland, the Philippines and Saudi Arabia – countries where at 
least 8% of respondents reported both stock investing and paying attention to social media. The 
target population of this study consists of adult individuals from the general population who 
are potential retail investors, regardless of whether they currently participate in the stock 
market. The data are drawn from an OECD survey administered to adult individuals at the 
household  level,  which  focuses  on  financial  behaviors  and  decision-making  within 
households. The unit of analysis is the individual respondent. Accordingly, the analysis 
captures both current investors and non-investors, allowing the study to examine factors 
associated with stock market participation and the influence of information signals. The results 
are therefore representative of potential individual or retail investors rather than professional 
or institutional investors. The unit of analysis is the individual respondent. Stock investment 
(SI) is modeled using a logistic specification with country fixed effects:

PrðSI i ¼ 1 j XÞ ¼ Λ

0 þ β 
β

1 ·Atten i þ β

3 ·Gen i þ β

4 ·Age

i þ β

5 ·Edu i þ β

6 ·ES i

2 ·DFL i þ β 
!

X 3

þ β

7 ·Inc i þ

Country 
h

h¼1

(1)

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 5 -->

Journal of 
Economics, 
Finance and 
Administrative 
Science

3.2 Data and variables
This section describes the measurement of the dependent variable (SI) and the independent 
variables of interest (Atten and DFL). The survey items used in this study are presented in 
Appendix 1. In addition, the control variables were Gen, the respondent’s gender; Age, the 
individual’s age in years; Edu, educational attainment; ES, employment status, and Inc, the 
household’s average income bracket (Table A1). Moreover, fixed effects are included to 
incorporate country-specific characteristics into the model.

Against this background, SI is defined as stock market participation, referring to “the 
fraction of individuals who directly own stocks” (Guiso et al., 2008, p. 28). It is a binary 
variable equal to 1 if individuals report direct investment in shares or securities through recent 
savings, current holding or active selection and 0 otherwise.

Next, investor attention (Atten) reflects limited cognitive resources (Kahneman, 1973), 
leading to reliance on low-cognitive-cost signals in information-rich settings (Hirshleifer and 
Teoh, 2003). In empirical finance, attention is measured through observable information-
seeking behavior and interpreted as revealed attention (Da et al., 2011) and amplified by 
algorithmic exposure on social media (Jang and Jun, 2025). It is coded 1 if decisions were 
influenced by recommendations from unknown individuals (e.g. influencers) and 0 otherwise.
Along similar lines, DFL is defined as the “combination of knowledge, skills, attitudes and 
behaviors necessary for individuals to be aware of and safely use digital financial services and 
digital technologies with a view to contributing to their financial well-being” (OECD, 2023, 
p. 7). It is measured through a principal component analysis (PCA)-based index, capturing 
three standardized dimensions: digital financial behavior (DFB), reflecting secure and 
responsible online practices; digital financial knowledge (DFK), based on correct responses to 
questions on digital finance and regulation, and digital financial attitude (DFA), assessing 
prudent and safety-oriented attitudes toward digital financial services.

4. Results
As shown in Table 1, 21.4% of individuals report SI, a relatively low but adequate level for 
analyzing its determinants, while 17.7% report Atten, suggesting this channel already 
influences decisions. The descriptive statistics by country are presented in the Supplementary 
file, Supplementary Table No. S1. Finland has the highest investment rate, whereas attention is 
greatest in the Philippines and Saudi Arabia, revealing opposite cross-country patterns. 
Potential multicollinearity was assessed using the variance inflation factor (VIF). Results in 
Supplementary Table No. S2 report an average VIF of 1.12, well below the 4–5 threshold, 
indicating no multicollinearity concerns (Li and Huang, 2025).

Table 1.  Descriptive statistics

Variable

Stock investment
Investor attention
Digital financial literacy 
Digital financial behavior 
Digital financial knowledge 
Digital financial attitude 
Gender
Age
Education
Employment status
Income
Source(s): Authors’ own work

Obs

6,865
6,865
6,865
6,865
6,865
6,865
6,865
6,865
6,865
6,865
6,865

Mean

0.214
0.177
0.000
2.363
1.581
1.701
0.496
41.968
3.254
0.661
1.882

Std. Dev

0.410
0.381
0.699
0.921
0.924
0.993
0.500
15.171
1.039
0.473
0.905

Min

0
0
�2.119
0
0
0
0
16
0
0
0

Max

1
1
1.886
4
3
3
1
80
5
1
3

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 6 -->

JEFAS

The empirical analysis begins by examining the underlying structure of DFL through PCA, 
indicating that the first component captures a general DFL factor across countries, but that its 
composition varies: behavior and attitude dominate in Saudi Arabia and Finland, while Brazil 
and the Philippines  display more balanced contributions. The second component is 
consistently driven by DFK, suggesting a distinct, specialized dimension. The country-
specific PCA result tables are reported in Supplementary Table No. S3.

Table 2 reports the marginal effects from the baseline logit specifications for SI. Focusing 
first on the pooled sample (Models 1–3), Atten influencers exhibit a positive, economically 
meaningful and highly statistically significant effect on stock market participation. In Model 
(1), Atten raises the probability of investing in stocks by 17.2% (Std. Err. 5 0.011, p < 0.01). 
This effect remains stable and statistically significant across alternative specifications that 
incorporate DFL, decreasing only modestly to 15.8% in Model (2) and 12.2% in Model (3). 
DFL also shows a positive and statistically significant association with SI. In the pooled 
sample, DFL increased the probability of investing in stocks by 5.8% (Std. Err. 5 0.0066, 
p < 0.01). When disaggregating DFL into its components, DFK emerges as the main driver, 
with a marginal effect of 6.1% (p < 0.01), while DFB and DFA dimensions play a 
comparatively smaller or statistically weaker role.

In Brazil (Models 4–6), Atten exerts a positive and statistically significant effect on SI. 
Specifically, the marginal effect ranges from 8.28% in Model (4) (Std. Err. 5 0.0139, p < 0.01) 
to 5.33% in Model (6) (Std. Err. 5 0.0132, p < 0.01). DFL also contributes positively, 
increasing the probability of SI by 4.22% (p < 0.01), with the effect largely driven by DFK 
(marginal effect 5 2.68%, p < 0.01). In Finland (Models 7–9), Atten raises the probability of SI 
by 28.1% in Model (7) (Std. Err. 5 0.0423, p < 0.01), remaining highly significant at 27.9% in 
Model (8) and 23.5% in Model (9). DFL is likewise economically meaningful, with a marginal 
effect of 10.4% (p < 0.01), again predominantly explained by DFK, which alone increases SI 
by 9.54% (p < 0.01). In the Philippines (Models 10–12), Atten increases the probability of SI 
by 18.3% in Model (10) (Std. Err. 5 0.0247, p < 0.01), 18.4% in Model (11) and 12.5% in 
Model (12), remaining statistically significant throughout. DFL contributes positively as well, 
raising SI likelihood by 6.81% (p < 0.01), with both DFK (5.5%, p < 0.01) and behavioral 
components playing a secondary but supportive role. Finally, in Saudi Arabia (Models 13–15), 
Atten continues to exhibit a positive and statistically significant association with SI, with 
marginal effects ranging from 14.3% in Model (13) (Std. Err. 5 0.0161, p < 0.01) to 4.79% in 
Model (15) (Std. Err. 5 0.0159, p < 0.01). DFL remains significant across specifications, 
increasing SI by 3.46% (p < 0.01), once again driven mainly by DFK (6.5% in Model 
13, p < 0.01).

Turning to the control variables reported in Table 2, gender is positively and statistically 
significant across most specifications: in the pooled sample (Model 2), being male increases 
the probability of investing in stocks by 4.7% (p < 0.01), with similar effects in Brazil (7.6%), 
Finland (8.1%) and the Philippines (5.0%). Education is strongly associated with SI, raising 
investment probabilities by 7% in the pooled model and up to 10.4% in the Philippines 
(p < 0.01). Employment status also increases SI likelihood (4.8%, pooled; p < 0.01), while 
income emerges as one of the strongest predictors, with positive and significant effects across 
all countries. Socioeconomic factors persistently shape investment behavior, consistent with 
prior evidence (Van Rooij et al., 2011). Taken together, these findings provide strong empirical 
support for Hypothesis 1, confirming that investor attention to digital financial content 
significantly increases SI, even after controlling for DFL and standard socioeconomic factors.
The interaction results reported in Table 3 provide direct evidence on Hypothesis 2, 
revealing substantial cross-country heterogeneity in the moderating role of DFL on the 
relationship between Atten and SI. In Brazil, the interaction between Atten and DFL is 
statistically insignificant, with or without controls, indicating that DFL raises overall SI but 
does not alter the effect of attention on investment decisions, consistent with Brazil’s still-
developing financial knowledge (Ramalho, 2019). A similar result holds for Finland, where 
the interaction remains insignificant across specifications, despite strong direct effects of

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 7 -->

Table  2.  Marginal effects  main  model

Atten

DFL

Digital financial 
behavior 
Digital financial 
knowledge 
Digital financial 
attitude
Gender

Age

Education

Employment 
status 
Income

All countries
(1)

(2)

(3)

0.158***
(0.0110)

0.122***
(0.0109)

0.172***
(0.0110)
0.0584***
(0.0066)

Brazil
(4)

0.0828***
(0.0139)
0.0422***
(0.0100)

(5)

(6)

0.0798***
(0.0139)

0.0533***
(0.0132)

Finland
(7)

0.281***
(0.0423)
0.104***
(0.0166)

(8)

(9)

0.279***
(0.0419)

0.235***
(0.0409)

Philippines
(10)

0.183***
(0.0247)
0.0681***
(0.0180)

(11)

(12)

0.184***
(0.0247)

0.125***
(0.0257)

Saudi Arabia
(13)

(14)

(15)

0.0997***
(0.0164)

0.0479***
(0.0159)

0.143***
(0.0161)
0.0346***
(0.0111)

�0.00875  �0.0113**
(0.00529)
(0.00551)
0.0388***
0.0607***
(0.00498)
(0.00504)
0.000228
0.00423
(0.00499)
(0.00517)
0.0472***
(0.00879)
�0.000664**
(0.000326)
0.0699***
(0.00539)
0.0484***
(0.0105)
0.0484***
(0.00489)
Yes
1,573.89
0.0000
6,865

0.0247***
(0.0087)
0.0268***
(0.0069)
�0.0044 
(0.0073)

0.0137
(0.0086)
0.0098
(0.0067)
�0.0057
(0.0071)
0.0755***
(0.0126)
�0.0027***
(0.0005)
0.0193***
(0.0068)
0.0370**
(0.0150)
0.0262***
(0.0078)
No
195.98
0.0000
2,000

�0.0370**  �0.0356**
(0.0146)
0.0954***
(0.0117)
0.0270**
(0.0125)

(0.0140)
0.0490***
(0.0118)
0.0254**
(0.0120)
0.0805***
(0.0218)
0.0013*
(0.0007)
0.0876***
(0.0118)
0.0983***
(0.0233)
0.0804***
(0.0108)
No
307.08
0.0000
1,806

�0.0018  �0.0054
(0.0124)
(0.0130)
0.0388***
0.055***
(0.0142)
(0.0145)
�0.0003
0.0122
(0.0130)
(0.0131)
0.0496**
(0.0251)
�0.00175*
(0.0010)
0.104***
(0.0169)
0.0813***
(0.0270)
0.0149
(0.0123)
No
148.16
0.0000
1,000

�0.0152 
(0.0093)
0.0650***
(0.0094)
�0.0148
(0.0100)

0.000805
(0.00904)
0.0539***
(0.00888)
�0.0128
(0.00953)
�0.0163
(0.0150)
0.000305
(0.000690)
0.139***
(0.0143)
�0.0189
(0.0279)
0.0777***
(0.0115)
No
313.23
0.0000
2,059

Yes
1,133.43
0.0000
6,865

Yes
1,064.48
0.0000
6,865

Fixed  effect 
2
LR  χ 
2 
Prob  >  χ 
Observations
Note(s): Models (1), (2), and  (3) correspond  to  the  full sample  of countries. Models (4), (5), and  (6) correspond  to  Brazil; models (7), (8), and  (9) to  Finland; models (10), (11), and 
(12) to  the  Philippines; and  models  (13), (14), and  (15) to  Saudi Arabia. Standard  errors are  in  parentheses. ***, **  and  *  indicate  statistical significance  at the  1%, 5%
and  10%
levels, respectively
Source(s): Authors’ own  work

No
109.43
0.0000
1,806

No
73.82
0.0000
1,806

No
69.47
0.0000
1,000

No
65.86
0.0000
1,000

No
120.50
0.0000
2,059

No
77.7
0.0000
2,059

No
68.64
0.0000
2,000

No
59.54
0.0000
2,000

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

A
d
m
i
n
i
s
t
r
a
t
i
v
e

S
c
i
e
n
c
e

F
i
n
a
n
c
e
 a
n
d

E
c
o
n
o
m
i
c
s
,

J
o
u
r
n
a
l
 o

f

---

<!-- PAGE 8 -->

J
E
F
A
S

Saudi
Arabia
(10)

0.0800***
(0.0151)
0.0134
(0.0126)
0.0787***
(0.0225)
�0.0280*
(0.0149)
0.000411
(0.000696)
0.147***
(0.0146)
�0.0167
(0.0278)
0.0782***
(0.0115)
No
300.07
0.0000
2,059

Table  3.  Marginal effects  and  the  interactive  role  of digital financial literacy

All
countries
(1)

0.171***
(0.0110)
0.0612***
(0.00758)
�0.0118 
(0.0161)

Brazil
(2)

Finland
(3)

Philippines
(4)

0.0878***
(0.0154)
0.0465***
(0.0117)
�0.0168 
(0.0226)

0.285***
(0.0457)
0.103***
(0.0175)
0.0148
(0.0594)

0.207***
(0.0244)
0.130***
(0.0217)
�0.192*** 
(0.0374)

Saudi
Arabia
(5)

0.150***
(0.0152)
0.00475
(0.0130)
0.0929***
(0.0236)

Atten

DFL

Attention  *  DFL

Gender

Age

Education

Employment status

Income

Fixed  effect
2
LR  χ 
2 
Prob  >  χ 
Observations
Note(s): Standard  errors  are  in  parentheses. ***, **  and  *  indicate  statistical significance  at the  1%, 5%
Source(s): Authors’ own  work

Yes
1,065.02
0.0000
6,865

No
90.95
0.0000
1,000

No
73.88
0.0000
1,806

No
60.09
0.0000
2,000

No
93.29
0.0000
2,059

and  10%

All countries
(6)

Brazil
(7)

Finland
(8)

Philippines
(9)

0.131***
(0.0108)
0.0285***
(0.00742)
0.00463
(0.0153)
0.0485***
(0.00885)
�0.000730** 
(0.000327)
0.0726***
(0.00543)
0.0489***
(0.0106)
0.0501***
(0.00490)
Yes
1,531.92
0.0000
6,865

0.0528***
(0.0147)
0.0128
(0.0113)
0.00376
(0.0224)
0.0763***
(0.0126)
�0.00273*** 
(0.000473)
0.0209***
(0.00678)
0.0384**
(0.0150)
0.0264***
(0.00784)
No
192.52
0.0000
2,000
levels, respectively

0.239***
(0.0442)
0.0461***
(0.0173)
0.0292
(0.0569)
0.0911***
(0.0216)
0.00107
(0.000767)
0.0924***
(0.0118)
0.0961***
(0.0234)
0.0833***
(0.0108)
No
289.14
0.0000
1,806

0.144***
(0.0256)
0.0850***
(0.0213)
�0.148*** 
(0.0364)
0.0455*
(0.0249)
�0.00189** 
(0.000953)
0.0974***
(0.0168)
0.0810***
(0.0268)
0.00995
(0.0122)
No
160.9
0.0000
1,000

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 9 -->

Journal of 
Economics, 
Finance and 
Administrative 
Science

attention and DFL, suggesting that digital competencies are already embedded in information 
processing in a high-literacy context (Kalmi and Ruuskanen, 2017). The Philippines exhibits a 
negative and statistically significant interaction effect (Model 9: �0.148, p < 0.01), implying 
that higher levels of DFL weaken the positive impact of Atten on SI. This finding aligns with 
national evidence documenting low overall financial literacy and less sophisticated financial 
behavior (Bangko Sentral ng Pilipinas, 2024). Conversely, Saudi Arabia shows a positive, 
significant interaction (Model 10: 0.0787, p < 0.01), consistent with evidence linking higher 
financial literacy to better investment decisions (Albarrak et al., 2024).

Overall, these findings indicate that DFL does not operate as a universal buffer against 
digital persuasion. Instead, its moderating role is highly context-dependent and is shaped by 
the level and distribution of financial knowledge across countries. Consequently, Hypothesis 2 
receives partial empirical support, as the direction and strength of the interaction between 
attention and DFL vary systematically across national settings.

4.1 Endogeneity
4.1.1 Two-stage instrumental variable regression. To address potential reverse causality,
endogeneity is mitigated using an instrumental variable (IV) based on online purchasing 
behavior, measured on a 1–4 scale that indicates how often respondents bought goods and 
services online in the past 12 months. More frequent online shopping increases exposure to 
digital platforms where influencers are prominent, plausibly raising attention to their 
recommendations. Consistent with this channel, social media interactions shape purchase 
decisions (Ismael et al., 2025), and influencers’ live-commerce demonstrations affect 
consumer choices (Li et al., 2025). The instrument is assessed in terms of exogeneity, 
relevance and strength; it should be valid, relevant and strong (Cameron and Trivedi, 2005). 
Table 4 reports Spearman correlations between the instrument and baseline residuals (Panel A) 
and between the instrument and the endogenous variable (Panel B), with p-value testing for 
independence. The instrument appears valid in Finland, the Philippines and Saudi Arabia, as 
independence from model errors cannot be rejected. It is relevant in Brazil, Finland and the 
Philippines, where independence from the endogenous variable is rejected, with the strongest 
associations in Brazil and the Philippines. In the pooled sample, the instrument correlated 
15.68% with the endogenous variable, rejecting independence.

To address potential endogeneity concerns with a nonlinear dependent variable, the 
methodology proposed by Wooldridge (2014), known as the control function method or two-
stage residual inclusion (2SRI), was applied. A central feature of this approach is that, in the 
second stage, the generalized residuals estimated in the first stage are included in the 
specification. As shown in Table 5, the IV is significantly positive for the pooled sample, 
indicating that individuals who purchase goods and services online are 3.8% (p < 0.01) more 
likely to pay attention to investment recommendations issued by social media influencers;

Table 4.  Spearman correlations between the instrumental variable, model errors and the endogenous variable

Brazil

Finland

Philippines

Saudi Arabia

Panel A: Spearman correlations – Instrument and baseline model errors
Rho
p-value

�0.0280
0.2347

�0.2689
0.000

�0.0286
0.3665

Panel B: Spearman correlations – Instrument and endogenous variable
Rho
p-value
Source(s): Authors’ own work

0.0950
0.0001

0.2543
0.000

0.3089
0.000

0.0250
0.2568

0.0112
0.6115

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 10 -->

J
E
F
A
S

Finland

First step

Attention

0.0113
(0.00717)

Philippines

Saudi Arabia

Second
step
Stock
investment Attention

First step

Second
step
Stock
investment Attention

First step

Second
step
Stock
investment

0.0704***
(0.0109)

0.00336
(0.0104)

0.00949 
(0.0188)

0.118 
(0.269)
0.0449** 
(0.0184)
0.0908***  �0.0660*** 
(0.0217)
0.000686
(0.00123)
0.0910***
(0.0124)
0.0954***
(0.0238)
0.0867***
(0.0134)
0.0593
(0.138)
No
244.24
0.000
1,806

(0.0255) 
�0.00524*** 
(0.000958)
0.0803***
(0.0152)
0.00605
(0.0275)
0.00739
(0.0125)

No
165.61
0.000
1,000

�0.429** 
0.568*** 
(0.178)
(0.121) 
�0.119***  �0.0347 
0.0212
(0.0173)
(0.0266)
(0.0119) 
0.0969***  �0.178***  �0.144***
(0.0165)
(0.0278)
0.00183** 
0.000722
(0.000890)
(0.00116)
0.183***
0.0442**
(0.0223)
(0.0149)
0.0671*** �0.0655* 
(0.0336)
(0.0258)
�0.00335 
0.00345
(0.0128)
(0.0122)
�0.271***
(0.0743)
No
120.45
0.000
1,000

(0.0409)
0.00162*
(0.000826)
0.253***
(0.0406)
�0.0560*
(0.0319)
0.0742***
(0.0111)
0.500***
(0.178)
No
188.65
0.000
2,059

No
438.26
0.000
2,059

and  10%

levels, respectively

Table  5.  Marginal effects  from

the  two-stage  residual model

All countries

Brazil

I.V.

Atten

DFL

Gender

Age

Education

Employment
status
Income

Resid

First step

Attention

0.0380***
(0.00444)

Second
step
Stock
investment Attention

First step

Second  step
Stock
investment

0.0431***
(0.00708)

0.329*** 
(0.0611)
0.0381*** 
(0.00726)
0.0644*** 
(0.0101)

0.0153
(0.0117)
0.00771
(0.0139)

�0.0265*** 
(0.00908) 
�0.00713 
(0.0127)

�0.0543*** 
(0.00622) 
�0.0655*** 
(0.00866) 
�0.00350***  �0.000177  �0.00355***  �0.00159***  �0.00317*** 
(0.000334)
0.0590***
(0.00535)
�0.00544 
(0.0108)
0.0198***
(0.00513)

(0.000441)
0.00489
(0.00668)
�0.00432 
(0.0133)
0.0256***
(0.00668)

(0.000518)
(0.000391)
0.0113
0.0562***
(0.00702)
(0.00801)
0.0504***  �0.0127 
(0.0154)
(0.0106)
0.00403
0.0458***
(0.00941)
(0.00512)
�0.116*** 
(0.0353)
Yes
1,164.47
0.000
6,865

No
179.45
0.000
2,000

0.244***
(0.0822)
0.00448
(0.0105)
0.0724***
(0.0121)

(0.000595)
0.0143**
(0.00709)
0.0355*** 
(0.0137)
0.0245***
(0.00748)
�0.109** 
(0.0477)
No
156.16
0.000
2,000

Yes
923.35
0.000
6,865

Fixed  effect 
2
LR  χ 
2 
Prob  >  χ 
Observations
Note(s): Standard  errors  are  in  parentheses. ***, **  and  *  indicate  statistical significance  at the  1%, 5%
Source(s): Authors’ own  work

No
112.60
0.000
1,806

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 11 -->

Journal of 
Economics, 
Finance and 
Administrative 
Science

however, this effect is not statistically significant for Finland or Saudi Arabia. In the second-
stage regression, the residual is significant, and Atten remains significant at the 1% level for 
the pooled sample, again with Finland as the exception. After 2SRI correction, social media 
attention still significantly affects investment decisions.

4.1.2 Propensity score matching (PSM). The propensity score matching (PSM) is used to 
correct  selection  bias  that  arises  when  individuals  who  receive  a  treatment  differ 
systematically from those who do not (Ali and Behera, 2015). This technique allows 
estimating the average treatment effect by matching treated and untreated individuals with 
similar observable characteristics (Rosenbaum and Rubin, 1983). PSM is necessary in this 
study because attention to investment recommendations from influencers is not randomly 
assigned and may be associated with individual attributes such as gender, age, DFL or income. 
Propensity scores were obtained using a logit model, after which two matching methods were 
applied:  single  nearest-neighbor  matching  and  nearest-neighbor  matching  with  the 
Mahalanobis distance. As reported in Table 6 (Panels A and B), substantial differences 
existed between individuals who paid attention to influencer recommendations and those who 
did not, but these differences were considerably reduced after applying PSM, indicating that 
both groups became adequately balanced across observed covariates. Regarding the results, 
the probability of participating in the stock market reaches 32.1% (Panel A.1) among 
individuals who paid attention to influencers, compared with only 21.8% among those who did 
not: an absolute difference of 10%, significant at the 1% level. These results match baseline 
estimates, supporting robustness: influencer attention increases the likelihood of SI. The 
country-level average treatment effect on the treated estimates are presented in the 
Supplementary file, Supplementary Table No. S4 and Supplementary Table No. S5.

5. Discussion
5.1 Theoretical implications
The results reinforce and broaden its theoretical implications in the context of social media and 
DFL on SI. The evidence indicates that attention would act as a prior selection mechanism, in 
which signals from influencers operate as attention-grabbing events that delimit the set of 
investment alternatives. The findings strengthen attention-based explanations by showing that 
salient digital signals may function as “attention triggers” that stimulate investment activity, 
even when informational content is limited (Arnold et al., 2022) and that attention to social 
media content catalyzes investment decisions (Kim and Fan, 2025).

Likewise, the results nuance the view of DFL as a universal buffer against digital 
persuasion,  as  its  moderating  effect  is  heterogeneous  and  context-dependent.  The 
heterogeneity  observed  in  the  moderating role  of  DFL  can  be  understood  through 
Hofstede’s  cultural  dimensions  (The  Culture  Factor  Group,  2025)  –  particularly 
individualism or collectivism, uncertainty avoidance and long-term orientation, which 
influence how individuals process financial information and respond to attention stimuli 
across different national settings. In more collectivist societies, such as Brazil, the Philippines 
and Saudi Arabia, economic decisions tend to be more influenced by social signals, amplifying 
the impact of recommendations disseminated on social media. Uncertainty avoidance 
introduces a second mechanism: in societies with a high need for certainty, such as Brazil and 
Saudi Arabia, digital signals may function as cognitive shortcuts. However, while in Brazil 
DFL has not yet reached sufficient levels to modify this pattern, in Saudi Arabia, greater digital 
competencies allow attention to translate into more effective investment decisions. In the 
Philippines, where uncertainty avoidance is lower, increased DFL fosters a more critical 
evaluation of social signals, weakening the relationship between attention and investment. 
Finally, long-term orientation explains why DFL is integrated into the general decision-
making process in Finland, whereas in countries with a short-term orientation, DFL may act 
both as a protective filter and as a facilitator of investment action.

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 12 -->

JEFAS

Table 6.  Average treatment effect on the treated

Panel A.1: Average treatment effect on the treated (ATT) using nearest-neighbor
Variable

Difference

Treatment

Controls

SI

0.321

0.218

0.103

S.E.

0.021

Panel A.2: Comparison of variable averages under PSM 
Variable 
Treated

Matched

Control

t

DFL

Gender

Age

Education

Employment status

Income

Unmatched
Matched
Unmatched
Matched
Unmatched
Matched
Unmatched
Matched
Unmatched
Matched
Unmatched
Matched

�0.114 
�0.114 
0.394
0.394
35.333
35.333
3.691
3.691
0.771
0.771
2.105
2.105

0.025
�0.145 
0.518
0.389
43.391
35.859
3.160
3.708
0.638
0.762
1.834
2.092

�6.300
1.090 
�7.920 
0.250
�17.130 
�1.080 
16.440
�0.520 
8.970
0.530
9.520
0.350

T-stat

4.870

p > t

0.000
0.276
0.000
0.803
0.000
0.281
0.000
0.602
0.000
0.597
0.000
0.724

Panel B.1: Average treatment effect on the treated (ATT) using nearest-neighbor matching with Mahalanobis 
distance
Variable

Difference

Controls

Treated

S.E.

T-stat

SI

0.321

0.221

0.100

0.019

5.140

Panel B.2: Comparison of variable averages under PSM 
Variable 
Treated

Matched

Control

t

DFL

Gender

Age

Education

Employment status

Income

Unmatched
Matched
Unmatched
Matched
Unmatched
Matched
Unmatched
Matched
Unmatched
Matched
Unmatched
Matched

�0.114 
�0.114 
0.394
0.394
35.333
35.333
3.691
3.691
0.771
0.771
2.105
2.105

0.025
�0.104 
0.518
0.394
43.391
35.466
3.160
3.687
0.638
0.771
1.834
2.104

�6.300 
�0.370 
�7.920 
0.000
�17.130 
�0.280 
16.440
0.130
8.970
0.000
9.520
0.020

Source(s): Authors’ own work

p > t

0.000
0.712
0.000
1.000
0.000
0.780
0.000
0.901
0.000
1.000
0.000
0.981

5.2 Managerial/policy implications
The results have direct implications for market participants and policymakers, particularly 
when considering the interaction between attention and social media, DFL and the cultural 
context. First, the positive association between attention to influencers and equity market 
participation suggests that influencers and platform-mediated recommendations have become 
established as influential channels for disseminating market signals, with potential relevance 
for financial inclusion and economic empowerment strategies (M€olders et al., 2025). For firms 
operating in financial markets and digital investment platforms, these findings highlight the

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 13 -->

Journal of 
Economics, 
Finance and 
Administrative 
Science

need to design more responsible social media communication strategies, incorporating clear 
information on risks, investment horizons and potential conflicts of interest. Nevertheless, 
evidence showing that attention-driven dynamics can increase risk-taking and impair returns 
in other settings reinforces the need to complement inclusion initiatives with financial 
education and effective consumer protection mechanisms (Arnold et al., 2022).

In this regard, recent regulatory guidance and enforcement actions emphasize that financial 
promotions on social media must be clear, fair and not misleading, and that influencer 
participation and compensation schemes should be appropriately disclosed (FCA, 2024). For 
individual investors, these guidelines underscore the importance of critically assessing the 
source, incentives and quality of information received through social media before making 
investment decisions. This regulatory emphasis is particularly relevant, given that the 
abundance of stock-related information available in financial markets makes investment 
decision-making especially demanding, as processing such information imposes a high 
cognitive load and may lead to irrational choices (Isidore and Christy, 2019).

Taken together, these findings indicate that public policies and regulatory frameworks 
should be context-sensitive, recognizing that DFL does not operate as a universal buffer but 
rather as a culturally contingent mechanism that can either amplify or attenuate the 
behavioral impact of social media attention on SI. Consequently, strengthening DFL, 
alongside more transparent digital communication practices by firms and platform design 
tools aimed at reducing impulsive decision-making, may contribute to a more informed, 
prudent and sustainable financial environment (Shunmugasundaram and Sinha, 2025).

5.3 Limitations and future research agenda
This study has limitations that also point to promising directions for future research. First, 
the analysis relies on cross-sectional and self-reported measures, which may introduce 
reporting and inference biases; longitudinal or panel designs would enable researchers to 
assess  whether  attention  to  social  media  predicts  SI  and  longer-term  investment 
performance. Second, the question capturing attention to influencer recommendations 
was only recently introduced in the OECD/INFE survey, which restricts intertemporal 
comparisons and the analysis of dynamic effects. Future studies could incorporate 
measures of attention intensity, platform specificity and content characteristics, such as 
sentiment, emotional tone, credibility cues or informational complexity, to identify the 
underlying behavioral mechanisms more precisely. In this regard, the use of machine 
learning and natural language processing techniques applied to large-scale social media 
data could substantially enrich the measurement of digital attention and allow a finer 
classification of informational versus persuasive content.

6. Conclusion
Consistent with its objectives, this study contributes to the behavioral finance literature by 
showing that individual attention to social media influencers significantly increases the 
likelihood of SI, reinforcing attention-based explanations of investment behavior. The 
heterogeneous moderating role of DFL across countries, based on differences in financial 
literacy levels and cultural characteristics, underscores the need to interpret digital influence 
within this broader context. Theoretically, the findings advance the understanding of how 
digital signals function as behavioral triggers and how individual competencies shape their 
effects, bridging digital finance and investor psychology. Practically, the results support 
policies that strengthen DFL and improve the oversight of financial content on social media. 
As these platforms become integral to retail investment decisions, effective regulation and 
targeted education are essential to foster informed participation and reduce behavioral risks in 
increasingly digital financial markets.

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 14 -->

JEFAS

Acknowledgments
We thank the OECD Secretariat for granting the INFE survey data, which made this research possible. 
Their support and commitment to advancing financial literacy research were essential for the 
development of this study. We would also like to thank the anonymous reviewer, whose valuable 
comments significantly enriched the quality and clarity of the manuscript, helping us strengthen both the 
theoretical foundation and the empirical analysis.

Appendix
Variables used in the 2023 OECD international survey of adult financial literacy

A1.1. Stock investment (SI) variable
It was defined as a binary variable identifying individuals who met at least one of the three conditions, 
coded as 1 when at least one of the specified actions was performed.

(1)  QF3_7: In the past 12 months, have you been [personally] saving money in any of the following 
ways, whether or not you still have the money? Please don’t take into account any money paid 
into a pension, but think about all kinds of savings, such as building up a rainy-day fund or 
putting money aside for a special occasion. Response: Investing in shares and securities.
(2)  QP2_12: Can you tell me whether you [personally or jointly] currently hold any of these types of

products? Response: Shares and securities.

(3)  QP3_12: In the last two years, which of the following types of financial products have you 
chosen [Personally or jointly], whether or not you still hold them? Please do not include products 
that were renewed automatically. Response: Shares and securities.

A1.2. Investor attention (Atten) variable
Question QP7_6 is used: “Which of these sources of information do you feel significantly influenced your 
decision {about which one to take out}?” The variable takes the value of 1 if the respondent selects the 
option “A recommendation from people you do not know (such as social media or ‘influencers’)”, and
0 otherwise.

A1.3. Digital financial literacy (DFL) variables and their dimensions
The DFK dimension includes three true-or-false items. Each item scores 1 for a correct answer and
0 otherwise:

(1)  QK7_4, “True or False: A digital financial contract requires the signature on a paper contract to

be considered valid.”

(2)  QK7_5, “True or False: The personal data that I share publicly online may be used to target me

with personalized commercial or financial offers.”

(3)  QK7_6, “True or False: Cryptocurrencies have the same legal tender status as banknotes

and coins.”

The DFB dimension includes four items. Responses are coded as 1 for the appropriate behavior and

0 otherwise:

(1)  QS2_6, “I share the passwords and PINs of my bank account with close friends.”
(2)  QS2_7, “Before buying a financial product online I check if the provider is regulated in my

country.”

(3)  QS2_8, “I share information about my personal finances publicly online (e.g. on social media).”
(4)  QS3_13, “I regularly change the passwords on websites that I use for online shopping and

personal finance.”

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 15 -->

The DFA dimension consists of three statements. Answers are scored 1 for the appropriate attitude

and 0 otherwise.

(1)  QS4_1, “I think that it is safe to shop online using public Wi-Fi networks.”
(2)  QS4_2, “It is important to pay attention to the security of a website before making a transaction

online.”

Journal of 
Economics, 
Finance and 
Administrative 
Science

(3)  QS4_3, “I think it is not important to read the terms and conditions when buying something

online.”

A1.4. Gender (Gen)
Question QD1, which takes the value of 1 if the respondent identifies as male and 0 if female.

A1.5. Age
Question QD7: “How old are you?” Respondents report their age in years.

A1.6. Education (Edu) variable
Education is measured on a 0–5 scale. Level 0 indicates no formal education. Level 1 corresponds to 
primary education, Level 2 to lower or secondary education, and Level 3 to upper secondary or high 
school. Level 4 represents completed university studies (e.g. bachelor’s degree), while Level 5 includes 
postgraduate education such as a master’s or a doctorate. The variable is labeled QD9.

A1.7. Employment status (ES) variable
The variable takes values of 1 or 0, where a value of 1 is assigned to two categories: individuals who are 
self-employed and those who are employed for pay. Conversely, a value of 0 is assigned when the 
respondent is an apprentice, homemaker, seeking work (unemployed), retired, not working, not seeking 
work, or a student. The question label for this variable is QD10.

A1.8. Household income (Inc) variable
The variable QD13 classifies monthly household income into four categories: nonresponse, below 75% of 
the median, between 75 and 125% of the median, and above 125%, using country-specific thresholds. The 
three income ranges for each country are as follows:

Table A1.  Income ranges for each country

Salary
range

Low (1)

Medium 
(2) 
High (3)

Saudi Arabia

Brazil

Philippines

Finland

Up to 7,000 Saudi 
riyals
Between 7,000 and 
11,000 Saudi riyals
11,000 Saudi riyals or 
more

Up to 2,604 reais  Up to 20,800 Philippine 
pesos
Between 20,800 and 
42,000 Philippine pesos 
42,000 Philippine pesos 
or more

Between 2,604 
and 6,510 reais 
6,510 reais or 
more

Up to 30,000 euros

Between 30,000 
and 50,000 euros 
50,000 euros or 
more

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 16 -->

JEFAS

Supplementary material
The supplementary material for this article can be found online.

References
Abdallah, W., Tfaily, F. and Harraf, A. (2024), “The impact of digital financial literacy on financial 
behavior: customers’ perspective”, Competitiveness Review: An International Business Journal, 
Vol. 35 No. 2, pp. 347-370, doi: 10.1108/CR-11-2023-0297.

Al-Smadi, M. (2023), “Examining the relationship between digital finance and financial inclusion: 
evidence from MENA countries”, Borsa Istanbul Review, Vol. 23 No. 2, pp. 464-472, doi: 
10.1016/j.bir.2022.11.016.

Albarrak, M.S., Alokley, S.A. and Ansari, Y. (2024), “Financial literacy among working adults: the 
case of Saudi Arabia”, Quantitative Finance and Economics, Vol. 8 No. 4, pp. 841-866, doi: 
10.3934/QFE.2024032.

Alfieri, E., Burlacu, R. and Enjolras, G. (2025), “Cryptocurrency bubbles, information asymmetry and 
noise trading”, The Journal of Risk Finance, Vol. 26 No. 2, pp. 295-319, doi: 10.1108/JRF-07-
2024-0220.

Ali, A. and Behera, B. (2015), “Household participation and effects of community forest management 
on income and poverty levels: empirical evidence from Bhutan”, Forest Policy and Economics, 
Vol. 61, pp. 20-29, doi: 10.1016/j.forpol.2015.06.006.

Anwar, M. (2025), “How digital financial literacy and social media usage build saving behavior among 
Generation Z. Asia-Pacific”, Journal of Business Administration, Vol. 143 No. 2, pp. 1-26, doi: 
10.1108/APJBA-04-2025-0329.

Arnold, M., Pelster, M. and Subrahmanyam, M.G. (2022), “Attention triggers and investors’ risk-
taking”, Journal of Financial Economics, Vol. 143 No. 2, pp. 846-875, doi: 10.1016/ 
j.jfineco.2021.05.031.

Bangko Sentral ng Pilipinas (2024), “How does financial literacy affect financial behavior over the life 
cycle? Evidence from Filipino households”, (Discussion Paper No. 2024 13), available at: 
https://www.bsp.gov.ph/Sites/researchsite/Publications/BSP-Discussion-Papers/DP202413.pdf
Barber, B. and Odean, T. (2008), “All that glitters: the effect of attention and news on the buying 
behavior of individual and institutional investors”, The Review of Financial Studies, Vol. 21 
No. 2, pp. 785-818, doi: 10.1093/rfs/hhm079.

Barber, B., Huang, X., Odean, T. and Schwarz, C. (2022), “Attention-induced trading and returns:

evidence from Robinhood users”, The Journal of Finance, Vol. 77 No. 6, pp. 3141-3190, doi: 
10.1111/jofi.13183.

Bayar, O. and Kesici, E. (2024), “The impact of social media on venture capital financing: evidence

from Twitter interactions”, Review of Quantitative Finance and Accounting, Vol. 62 No. 1, 
pp. 195-224, doi: 10.1007/s11156-023-01199-4.

Bhat, S., Lone, U., SivaKumar, A. and Krishna, U. (2024), “Digital financial literacy and financial

well-being–evidence from India”, International Journal of Bank Marketing, Vol. 43 No. 3, 
pp. 522-548, doi: 10.1108/IJBM-05-2024-0320.

Cameron, A. and Trivedi, P. (2005), Microeconometrics: Methods and Applications, Cambridge

University Press, Cambridge.

Carosia, A.O., Coelho, G.P. and Silva, A.E.A.D. (2020), “Analyzing the Brazilian financial market

through Portuguese sentiment analysis in social media”, Applied Artificial Intelligence, Vol. 34 
No. 1, pp. 1-19, doi: 10.1080/08839514.2019.1673037.

Chen, S. and Ren, F. (2025), “Does social media information affect individual investor disposition 
effect? Evidence from Xueqiu”, PLoS One, Vol. 20 No. 7, e0328547, doi: 10.1371/ 
journal.pone.0328547.

Da, Z., Engelberg, J. and Gao, P. (2011), “In search of attention”, The Journal of Finance, Vol. 66

No. 5, pp. 1461-1499, doi: 10.1111/j.1540-6261.2011.01679.x.

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 17 -->

Journal of 
Economics, 
Finance and 
Administrative 
Science

Financial Conduct Authority (2024), “Finalised guidance on financial promotions on social media 
(FG24/1)”, available at: https://www.fca.org.uk/publication/finalised-guidance/fg24-1.pdf
Guiso, L., Sapienza, P. and Zingales, L. (2008), “Trusting the stock market”, The Journal of Finance,

Vol. 63 No. 6, pp. 2557-2600, doi: 10.1111/j.1540-6261.2008.01408.x.

Hermansson, C., Jonsson, S. and Liu, L. (2022), “The medium is the message: learning channels,

financial literacy, and stock market participation”, International Review of Financial Analysis, 
Vol. 79, 101996, doi: 10.1016/j.irfa.2021.101996.

Hirshleifer, D. and Teoh, S. (2003), “Limited attention, information disclosure, and financial

reporting”, Journal of Accounting and Economics, Vol. 36 Nos 1-3, pp. 337-386, doi: 10.1016/ 
j.jacceco.2003.10.002.

Hylkil€a, K., M€annikk€o, N., Castr�en, S., Mustonen, T., Peltonen, A., Konttila, J., M€annist€o, M.,

K€a€ari€ainen, M. and K€a€ari€ainen, M. (2023), “Association between psychosocial well-being and 
problematic social media use among Finnish young adults: a cross-sectional study”, Telematics 
and Informatics, Vol. 81, 101996, doi: 10.1016/j.tele.2023.101996.

Isidore, R. and Christy, P. (2019), “The relationship between the income and behavioral biases”,

Journal of Economics, Finance and Administrative Science, Vol. 24 No. 47, pp. 127-144, doi: 
10.1108/JEFAS-10-2018-0111.

Ismael, A., Amin, M., Ali, M., Hajd�u, Z. and P�eter, B. (2025), “Relationship between social media 
marketing and young customers’ purchase intention towards online shopping”, Cogent Social 
Sciences, Vol. 11 No. 1, 2459881, doi: 10.1080/23311886.2025.2459881.

Jang, J. and Jun, S. (2025), “YouTube view count, investor attention and stock returns”, International

Review of Financial Analysis, Vol. 97, 103782, doi: 10.1016/j.irfa.2024.103782.

Kahneman, D. (1973), Attention and Effort, Prentice-Hall, Englewood Cliffs: NJ.
Kalmi, P. and Ruuskanen, O. (2017), “Financial literacy and retirement planning in Finland”, Journal

of Pension Economics and Finance, Vol. 17 No. 3, pp. 335-355, doi: 10.1017/ 
S1474747217000154.

Kim, H. (2025), “Social media engagement and retail investors’ short-termism”, Finance Research

Letters, Vol. 85, 108249, doi: 10.1016/j.frl.2025.108249.

Kim, K. and Fan, L. (2025), “Beyond the hashtags: social media usage and cryptocurrency

investment”, International Journal of Bank Marketing, Vol. 43 No. 3, pp. 569-590, doi: 10.1108/ 
IJBM-12-2023-0665.

Li, Y. and Huang, Y. (2025), “Social security, digital literacy, and relative poverty in China”, Finance

Research Letters, Vol. 71, 106446, doi: 10.1016/j.frl.2024.106446.

Li, X., Wang, Q., Yao, X., Yan, X. and Li, R. (2025), “How do influencers’ impression management

tactics affect purchase intention in live commerce? –Trust transfer and gender differences”, 
Information and Management, Vol. 62 No. 2, 104094, doi: 10.1016/j.im.2024.104094.
Ly�ocsa, �S., Halouskov�a, M. and Haugom, E. (2023), “The US banking crisis in 2023: intraday attention
and price variation of banks at risk”, Finance Research Letters, Vol. 57, 104209, doi: 10.1016/ 
j.frl.2023.104209.

Maheshwari, H. and Samantaray, A.K. (2025), “Navigating investment challenges: financial literacy 
and digital advisory services in countering behavioural biases”, International Journal of 
Sociology and Social Policy, Vol. 46 Nos 3-4, pp. 1-17, doi: 10.1108/IJSSP-12-2024-0620.
Mazzoli, C. and Baiocco, S. (2025), “Unlocking sustainable investing through digital financial literacy: 
the impact of advanced digital skills”, International Journal of Bank Marketing, Vol. 43 No. 9, 
pp. 1-21, doi: 10.1108/IJBM-10-2024-0622.

Mertzanis, C., Ahmed, M.S., Faisal, R. and Al Suwaidi, R.A. (2025), “Does financial literacy drive 
digital currency innovation? Cross-country evidence on CBDC adoption”, Borsa Istanbul 
Review, Vol. 25, p. 109, doi: 10.1016/j.bir.2025.08.006.

M€olders, M., Bock, L., Barrantes, E. and Z€ulch, H. (2025), “Understanding finfluencers: roles and 
strategic partnerships in retail investor engagement”, Journal of Business Research, Vol. 198, 
115462, doi: 10.1016/j.jbusres.2025.115462.

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

---

<!-- PAGE 18 -->

JEFAS

M€unster, M., Reichenbach, F. and Walther, M. (2024), “Robinhood, Reddit, and the news: the impact of 
traditional and social media on retail investor trading”, Journal of Financial Markets, Vol. 71, 
100929, doi: 10.1016/j.finmar.2024.100929.

OECD (2023), OECD/INFE 2023 International Survey of Adult Financial Literacy, OECD Publishing,

Paris, OECD Business and Finance Policy Papers, No. 39, doi: 10.1787/56003a32-en.

Pak, T., Chatterjee, S. and Choung, Y. (2026), “Navigating digital finance: how digital financial literacy 
influences digital financial services use and benefits in Korea”, Financial Innovation, Vol. 12 
No. 1, p. 42, doi: 10.1186/s40854-025-00820-w.

Pedersen, L. (2022), “Game on: social networks and markets”, Journal of Financial Economics,

Vol. 146 No. 3, pp. 1097-1119, doi: 10.1016/j.jfineco.2022.05.002.

Ramalho, T.B. (2019), “Financial literacy in Brazil – do knowledge and self reported financial behavior 
relate to financial outcomes?”, Revista Brasileira de Gest~ao e Finanças. doi: 10.12660/ 
rbgn.v21n2.2019.80215.

Reichenbach, F. and Walther, M. (2025), “Attention allocation of investors on social media: the role of 
prospect theory”, The Journal of Behavioral Finance, Vol. 26 No. 3, pp. 317-334, doi: 10.1080/ 
15427560.2024.2309145.

Rosenbaum, P. and Rubin, D. (1983), “Constructing a control group using multivariate matched

sampling method that incorporate the propensity score”, The American Statistician, Vol. 39 
No. 1, pp. 3-38.

Showkat, M., Nagina, R., Baba, M.A. and Yahya, A.T. (2025), “The impact of financial literacy on 
women’s economic empowerment: exploring the mediating role of digital financial services”, 
Cogent Economics and Finance, Vol. 13 No. 1, 2440444, doi: 10.1080/23322039.2024.2440444.

Shunmugasundaram, V. and Sinha, A. (2025), “The impact of behavioral biases on investment

decisions: a serial mediation analysis”, Journal of Economics, Finance and Administrative 
Science, Vol. 30 No. 59, pp. 5-21, doi: 10.1108/JEFAS-08-2023-0243.
The Culture Factor Group (2025), “Country comparison tool”, available at: https://

www.theculturefactor.com/country-comparison-tool?countries5

Van Rooij, M., Lusardi, A. and Alessie, R. (2011), “Financial literacy and stock market participation”,

Journal of Financial Economics, Vol. 101 No. 2, pp. 449-472, doi: 10.1016/ 
j.jfineco.2011.03.006.

Wang, G., Wang, Y., Dong, Y. and Shen, X. (2024), “Media attention for carbon neutrality, investor

sentiment, and excess stock returns: evidence from mass media and social media”, 
Computational Economics, Vol. 66 No. 3, pp. 1-25, doi: 10.1007/s10614-024-10739-6.
Warkulat, S. and Pelster, M. (2024), “Social media attention and retail investor behavior: evidence from

r/wallstreetbets”, International Review of Financial Analysis, Vol. 96, 103721, doi: 10.1016/ 
j.irfa.2024.103721.

Wooldridge, J. (2014), “Quasi-maximum likelihood estimation and testing for nonlinear models with 
endogenous explanatory variables”, Journal of Econometrics, Vol. 182 No. 1, pp. 226-234, doi: 
10.1016/j.jeconom.2014.04.020.

Corresponding author
Diana Bustamante can be contacted at: di.bustamante@uandresbello.edu

For instructions on how to order reprints of this article, please visit our website:
www.emeraldgrouppublishing.com/licensing/reprints.htm
Or contact us for further details: permissions@emeraldinsight.com

Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Retail investor behavior and social Journal of
Economics,
media signals: exploring Finance and
Administrative
attention dynamics Science
Diana Bustamante
Faculty of Business and Economics, Universidad Andres Bello, Santiago, Chile, and
Alejandra Ubilla Received 19 October 2025
Revised 16 December 2025
Facultad de Econom�ıa y Negocios, Universidad Santo Tomas, Santiago, Chile 10 February 2026
17 March 2026
Accepted 18 March 2026
Abstract
Purpose – This study aims to investigate how social media recommendations influence investor attention and
retail investor activity in stock investing.
Design/methodology/approach – Using data from the Organisation for Economic Co-operation and
Development (OECD)’s 2023 Adult Financial Literacy Survey across a sample of countries, the analysis
employs a logistic regression model. To address potential endogeneity, both instrumental variable and
propensity score matching techniques are applied.
Findings – Investor attention to social media influencers shows a positive and significant effect on stock
investment. After adjusting for endogeneity, the main results remain robust. However, the moderating role of
digital financial literacy is not consistent across all countries in the sample.
Research limitations/implications – The influencer recommendation question was newly introduced in this
survey, limiting longitudinal comparisons. Additionally, the results are based on self-reported data from four
countries.
Originality/value – This research contributes to the emerging field of digital behavioral finance and offers
insights for the design of financial inclusion and education policies in increasingly digital environments.
Keywords Investor attention, Social media, Stock investment, Digital financial literacy,
Investment decision-making, Digital financial behavior
Paper type Research article
1. Introduction
The growing influence of social media on the financial behavior of retail investors has
attracted significant academic attention in recent years. These platforms have profoundly
reshaped how investors access, interpret and process financial information, partially
displacing traditional media outlets (M€unster et al., 2024). Their capacity for virality,
immediacy and social validation has positioned social media as a key channel for
disseminating market signals, raising concerns among regulators and market participants
about its potential to trigger suboptimal investment decisions (Barber et al., 2022).
From a behavioral perspective, a wide body of literature has examined the role of cognitive
resources, overconfidence as a behavioral bias and limited attention as a scarce resource
(Kahneman, 1973), noting that these factors may amplify market noise and undermine the
efficiency of price formation processes (Alfieri et al., 2025). These effects are further
exacerbated in digital environments, where decision-making rationality is increasingly
challenged (Warkulat and Pelster, 2024). Despite advances in this field, the literature has yet to
thoroughly explore the mechanisms through which social media recommendations capture the
JEL Classification — G11, G40, G41, G53
© Diana Bustamante and Alejandra Ubilla. Published in Journal of Economics, Finance and
Administrative Science. Published by Emerald Publishing Limited. This article is published under the
Creative Commons Attribution (CC BY 4.0) licence. Anyone may reproduce, distribute, translate and
Journal of Economics, Finance and
create derivative works of this article (for both commercial and non-commercial purposes), subject to full Administrative Science
attribution to the original publication and authors. The full terms of this licence maybe seen at Link to the
Emerald
e
P
-
u
IS
b
S
li
N
sh
:
i n
2
g
2 1
L
8
i
-
m
0
i
6
t
4
ed
8
terms of the CC BY 4.0 licence.
DOI 10.1108/JE
p
F
-
A
IS
S
S
-1
N
0
:
- 2
2
0
0
2
7
5
7
-
-
0
1
3
8
7
8
8
6
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

JEFAS attention of individual investors and shape their willingness to participate in equity markets.
Recent studies have mostly focused on specific phenomena or asset classes, including short-
termism in investment behavior (Kim, 2025), disposition effect (Chen and Ren, 2025) or
cryptocurrency investment (Kim and Fan, 2025), without addressing how these platforms
interact with critical individual competencies such as digital financial literacy (DFL).
DFL has emerged as a key competency to navigate the challenges of the digital financial
ecosystem by enabling individuals to efficiently access, understand and use financial
information (Mazzoli and Baiocco, 2025). Recent evidence shows that developing DFL is
essential for the effective use of digital financial services and for managing associated risks;
however, despite widespread digitalization, its effects on individuals’ financial behavior and
overall financial awareness remain insufficiently understood (Bhat et al., 2024). Moreover,
little is known about the moderating role of DFL in shaping the influence of social media
recommendations.
In parallel, a growing body of international literature has emphasized the importance of
DFL across diverse settings. For instance, Pak et al. (2026), drawing on evidence from South
Korea, suggest that DFL is a key determinant of both the adoption of and the benefits derived
from digital financial services, thereby contributing to financial inclusion in the digital era. In
northern India, Showkat et al. (2025) demonstrated that financial literacy enhances the use of
digital financial services and serves as a critical mechanism for women’s economic
empowerment, promoting gender equality. In the same country, Maheshwari and Samantaray
(2025) find that financial literacy, together with artificial intelligence (AI)-based digital
advisory services, encourages more rational investment decisions. Moreover, cross-country
comparative studies highlight the role of financial capability in fostering digital monetary
innovation, suggesting that strengthening financial literacy should be a strategic component in
the design and implementation of central bank digital currencies across different national
contexts (Mertzanis et al., 2025).
In this respect, the present study aims to analyze the relationship between attention to social
media influencer recommendations and the decision to invest in the stock market, considering
the moderating role of DFL. For this purpose, a logistic regression model is employed using
individual-level data from the 2023 Organisation for Economic Co-operation and
Development (OECD)/International Network on Financial Education Survey (INFE) of
Adult Financial Literacy, covering four countries with diverse socioeconomic environments:
Brazil, Finland, the Philippines and Saudi Arabia. The study is guided by the following
research questions: To what extent do influencer recommendations on social media influence
individuals’ decisions to invest in the stock market? What role does DFL play in moderating
this relationship?
This research offers a novel contribution by examining an understudied phenomenon from
an international comparative perspective, integrating both behavioral and digital variables.
Moreover, it provides empirical evidence from a heterogeneous group of countries, allowing
for the analysis of contextual differences in investor behavior. By combining social media
attention and DFL levels, the study aligns with an emerging body of literature, aiming to
understand the cognitive and technological determinants of financial decision-making in
contemporary digital environments (Anwar, 2025).
The structure of the paper is as follows: Section 2 reviews the literature and presents the
theoretical framework, Section 3 describes the study methodology, Section 4 reports the
results, Section 5 discusses the findings and Section 6 concludes.
2. Literature review
In recent years, social media platforms have emerged as a key channel for shaping financial
expectations and investment behavior among retail investors (Reichenbach and Walther, 2025).
This influence stems not only from their ability to capture attention but also from their role as
providers of qualitative information about companies, which significantly affects investment
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

decisions (Bayar and Kesici, 2024). These platforms have been identified as behavioral drivers Journal of
that shape short-term investment decisions, particularly among younger individuals who tend to Economics,
exhibit overconfidence in their financial knowledge (Kim, 2025). Despite these advances, much Finance and
of the existing literature relies on single-country case studies or nationally limited samples, Administrative
which restrict the generalizability of the findings (Ly�ocsa et al., 2023). This national focus limits Science
the understanding of the underlying mechanisms from a global perspective. Meanwhile, social
media increasingly shapes markets: cases such as GameStop (Pedersen, 2022) and Twitter
effects (Carosia et al., 2020) illustrate how social media operates as a behavioral determinant of
investment decisions across highly diverse environments. Even in countries with high levels of
digital literacy, such as Finland, young adults report spending between 35 and 42 h per week
online, with nearly 20 of those hours dedicated exclusively to social media use (Hylkil€a et al.,
2023). Studies often rely on aggregated data, rarely examining individual influencer attention as
an investment “attention shock” or comparing across countries. This limits micro-level evidence
on how digital attention affects behavior. Since attention narrows choices and influencers can
redirect it toward specific stocks, followers are more likely to invest.
The concept of digital finance has emerged as a response to rapid technological
advancements in the financial sector (Al-Smadi, 2023), prompting individuals to acquire new
competencies to navigate digital environments. Within this context, DFL has become essential
for fostering informed, autonomous and responsible financial behavior (OECD, 2023). This
competency enables individuals to analyze financial products, critically assess digital
information and make rational investment decisions (Abdallah et al., 2024). Empirical studies
have demonstrated that higher levels of DFL are associated with improved investment
outcomes and more effective retirement planning (Mazzoli and Baiocco, 2025). However,
concerns remain about the reliability of social media as an information source. Wang et al.
(2024) suggest that content disseminated by financial influencers is often low in analytical
quality and high in emotional appeal, increasing the behavioral risks for retail investors. While
prior literature has explored how digital competencies influence financial behavior in single-
country contexts, such as Sweden (Hermansson et al., 2022) or China (Wang et al., 2024), few
studies have systematically examined how the moderating role of DFL varies across countries
with distinct institutional and technological landscapes. This gap is especially important, given
the increasing globalization of digital financial content.
Given that influencers generate attention-grabbing events that particularly affect less
sophisticated investors, it would be reasonable to expect that individuals with higher digital
competencies would be less susceptible to such influence. DFL would provide analytical skills
and critical thinking that would help individuals assess the quality of information and avoid
impulsive choices, thereby attenuating the impact of attention to social media influencers on
investment decisions.
2.1 Theoretical framework
The attention theory proposed by Barber and Odean (2008) offers a framework for
understanding how stimuli originating from social media could influence individual financial
behavior. This theory posits that attention functions as a selection mechanism prior to decision-
making, determining which alternatives are considered before preferences shape the final
choice. Because individual investors face a large universe of potential stocks, they tend to
simplify their search process by focusing on those that have recently captured their attention.
Although not all attention-grabbing stocks are ultimately purchased, the authors show that
investors only buy stocks that have succeeded in attracting their attention. In this sense,
influencers operate as agents who generate “attention-grabbing events,” capable of directing
attention toward specific assets, similar to what occurs in traditional media such as Consumer
News and Business Channel (CNBC), where a single mention can multiply trading volume
within minutes. Thus, when an influencer highlights a stock, they produce an attention event
that increases the likelihood that an individual investor will consider purchasing it.
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

JEFAS Barber and Odean (2008) argue that individual investors face limited attention and rely on
salient cues, while professionals reduce such constraints through systematic search, analytical
tools and deeper fundamental analysis, recognizing that highlighted information is often
already priced in. Higher DFL should make individuals behave more like professionals by
improving risk understanding, critical evaluation and structured decision-making.
Consequently, reliance on salient cues declines, which could reduce susceptibility to social
media influencer recommendations. As an alternative to Barber and Odean (2008), the limited
attention theory developed by Hirshleifer and Teoh (2003) emphasizes that investors face
cognitive constraints that affect not only which assets they consider but also how they process
available information. Investors tend to assimilate salient, low-cognitive-cost information
more easily, while economically relevant information may be ignored if it fails to attract
attention. These limitations contribute to distortions in asset valuation and to the persistence of
market inefficiencies, as neither arbitrage nor professional analysis fully corrects price
misalignments. Taken together, this theory complements Barber and Odean (2008) by
explaining the underlying cognitive mechanisms that allow attention-driven effects on
investment decisions to persist in financial markets.
Taken together, this theoretical framework suggests that signals emitted by social media
influencers would operate as attention-grabbing events that would increase the likelihood that
individuals consider investing in stocks, while higher levels of DFL would attenuate this effect
by reducing reliance on salient cues in the decision-making process. Therefore, consistent with
the theoretical framework, the following hypotheses are proposed:
H1. Social media signals from influencers increase individuals’ propensity to invest in
stocks.
H2. Individuals with higher digital financial literacy reduce the likelihood of social media
influence on their investment decisions.
3. Method
3.1 Research design/model
This study uses microdata from the OECD/INFE 2023 International Survey of Adult Financial
Literacy and focuses on Brazil, Finland, the Philippines and Saudi Arabia – countries where at
least 8% of respondents reported both stock investing and paying attention to social media. The
target population of this study consists of adult individuals from the general population who
are potential retail investors, regardless of whether they currently participate in the stock
market. The data are drawn from an OECD survey administered to adult individuals at the
household level, which focuses on financial behaviors and decision-making within
households. The unit of analysis is the individual respondent. Accordingly, the analysis
captures both current investors and non-investors, allowing the study to examine factors
associated with stock market participation and the influence of information signals. The results
are therefore representative of potential individual or retail investors rather than professional
or institutional investors. The unit of analysis is the individual respondent. Stock investment
(SI) is modeled using a logistic specification with country fixed effects:
PrðSI
i
¼ 1 j XÞ¼ Λ β
0
þ β
1
·Atten
i
þ β
2
·DFL
i
þ β
3
·Gen
i
þ β
4
·Age
i
þ β
5
·Edu
i
þ β
6
·ES
i
!
X3
þ β
7
·Inc
i
þ Country
h
h¼1
(1)
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

3.2 Data and variables Journal of
This section describes the measurement of the dependent variable (SI) and the independent  Economics,
variables of interest (Atten and DFL). The survey items used in this study are presented in  Finance and
Appendix 1. In addition, the control variables were Gen, the respondent’s gender; Age, the  Administrative
individual’s age in years; Edu, educational attainment; ES, employment status, and Inc, the  Science
household’s average income bracket (Table A1). Moreover, fixed effects are included to
incorporate country-specific characteristics into the model.
Against this background, SI is defined as stock market participation, referring to “the
fraction of individuals who directly own stocks” (Guiso et al., 2008, p. 28). It is a binary
variable equal to 1 if individuals report direct investment in shares or securities through recent
savings, current holding or active selection and 0 otherwise.
Next, investor attention (Atten) reflects limited cognitive resources (Kahneman, 1973),
leading to reliance on low-cognitive-cost signals in information-rich settings (Hirshleifer and
Teoh, 2003). In empirical finance, attention is measured through observable information-
seeking behavior and interpreted as revealed attention (Da et al., 2011) and amplified by
algorithmic exposure on social media (Jang and Jun, 2025). It is coded 1 if decisions were
influenced by recommendations from unknown individuals (e.g. influencers) and 0 otherwise.
Along similar lines, DFL is defined as the “combination of knowledge, skills, attitudes and
behaviors necessary for individuals to be aware of and safely use digital financial services and
digital technologies with a view to contributing to their financial well-being” (OECD, 2023,
p. 7). It is measured through a principal component analysis (PCA)-based index, capturing
three standardized dimensions: digital financial behavior (DFB), reflecting secure and
responsible online practices; digital financial knowledge (DFK), based on correct responses to
questions on digital finance and regulation, and digital financial attitude (DFA), assessing
prudent and safety-oriented attitudes toward digital financial services.
4. Results
As shown in Table 1, 21.4% of individuals report SI, a relatively low but adequate level for
analyzing its determinants, while 17.7% report Atten, suggesting this channel already
influences decisions. The descriptive statistics by country are presented in the Supplementary
file, Supplementary Table No. S1. Finland has the highest investment rate, whereas attention is
greatest in the Philippines and Saudi Arabia, revealing opposite cross-country patterns.
Potential multicollinearity was assessed using the variance inflation factor (VIF). Results in
Supplementary Table No. S2 report an average VIF of 1.12, well below the 4–5 threshold,
indicating no multicollinearity concerns (Li and Huang, 2025).
Table 1. Descriptive statistics
| Variable | Obs Mean | Std. Dev | Min | Max |
| -------- | -------- | -------- | --- | --- |
Stock investment
|                             | 6,865 0.214 | 0.410 | 0      | 1     |
| --------------------------- | ----------- | ----- | ------ | ----- |
| Investor attention          | 6,865 0.177 | 0.381 | 0      | 1     |
| Digital financial literacy  | 6,865 0.000 | 0.699 | �2.119 | 1.886 |
| Digital financial behavior  | 6,865 2.363 | 0.921 | 0      | 4     |
Digital financial knowledge
|                             | 6,865 1.581  | 0.924  | 0   | 3   |
| --------------------------- | ------------ | ------ | --- | --- |
| Digital financial attitude  | 6,865 1.701  | 0.993  | 0   | 3   |
| Gender                      | 6,865 0.496  | 0.500  | 0   | 1   |
| Age                         | 6,865 41.968 | 15.171 | 16  | 80  |
| Education                   | 6,865 3.254  | 1.039  | 0   | 5   |
Employment status
|        | 6,865 0.661 | 0.473 | 0   | 1   |
| ------ | ----------- | ----- | --- | --- |
| Income | 6,865 1.882 | 0.905 | 0   | 3   |
Source(s): Authors’ own work
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

JEFAS The empirical analysis begins by examining the underlying structure of DFL through PCA,
indicating that the first component captures a general DFL factor across countries, but that its
composition varies: behavior and attitude dominate in Saudi Arabia and Finland, while Brazil
and the Philippines display more balanced contributions. The second component is
consistently driven by DFK, suggesting a distinct, specialized dimension. The country-
specific PCA result tables are reported in Supplementary Table No. S3.
Table 2 reports the marginal effects from the baseline logit specifications for SI. Focusing
first on the pooled sample (Models 1–3), Atten influencers exhibit a positive, economically
meaningful and highly statistically significant effect on stock market participation. In Model
(1), Atten raises the probability of investing in stocks by 17.2% (Std. Err. 5 0.011, p < 0.01).
This effect remains stable and statistically significant across alternative specifications that
incorporate DFL, decreasing only modestly to 15.8% in Model (2) and 12.2% in Model (3).
DFL also shows a positive and statistically significant association with SI. In the pooled
sample, DFL increased the probability of investing in stocks by 5.8% (Std. Err. 5 0.0066,
p < 0.01). When disaggregating DFL into its components, DFK emerges as the main driver,
with a marginal effect of 6.1% (p < 0.01), while DFB and DFA dimensions play a
comparatively smaller or statistically weaker role.
In Brazil (Models 4–6), Atten exerts a positive and statistically significant effect on SI.
Specifically, the marginal effect ranges from 8.28% in Model (4) (Std. Err. 5 0.0139, p < 0.01)
to 5.33% in Model (6) (Std. Err. 5 0.0132, p < 0.01). DFL also contributes positively,
increasing the probability of SI by 4.22% (p < 0.01), with the effect largely driven by DFK
(marginal effect 5 2.68%, p < 0.01). In Finland (Models 7–9), Atten raises the probability of SI
by 28.1% in Model (7) (Std. Err. 5 0.0423, p < 0.01), remaining highly significant at 27.9% in
Model (8) and 23.5% in Model (9). DFL is likewise economically meaningful, with a marginal
effect of 10.4% (p < 0.01), again predominantly explained by DFK, which alone increases SI
by 9.54% (p < 0.01). In the Philippines (Models 10–12), Atten increases the probability of SI
by 18.3% in Model (10) (Std. Err. 5 0.0247, p < 0.01), 18.4% in Model (11) and 12.5% in
Model (12), remaining statistically significant throughout. DFL contributes positively as well,
raising SI likelihood by 6.81% (p < 0.01), with both DFK (5.5%, p < 0.01) and behavioral
components playing a secondary but supportive role. Finally, in Saudi Arabia (Models 13–15),
Atten continues to exhibit a positive and statistically significant association with SI, with
marginal effects ranging from 14.3% in Model (13) (Std. Err. 5 0.0161, p < 0.01) to 4.79% in
Model (15) (Std. Err. 5 0.0159, p < 0.01). DFL remains significant across specifications,
increasing SI by 3.46% (p < 0.01), once again driven mainly by DFK (6.5% in Model
13, p < 0.01).
Turning to the control variables reported in Table 2, gender is positively and statistically
significant across most specifications: in the pooled sample (Model 2), being male increases
the probability of investing in stocks by 4.7% (p < 0.01), with similar effects in Brazil (7.6%),
Finland (8.1%) and the Philippines (5.0%). Education is strongly associated with SI, raising
investment probabilities by 7% in the pooled model and up to 10.4% in the Philippines
(p < 0.01). Employment status also increases SI likelihood (4.8%, pooled; p < 0.01), while
income emerges as one of the strongest predictors, with positive and significant effects across
all countries. Socioeconomic factors persistently shape investment behavior, consistent with
prior evidence (Van Rooij et al., 2011). Taken together, these findings provide strong empirical
support for Hypothesis 1, confirming that investor attention to digital financial content
significantly increases SI, even after controlling for DFL and standard socioeconomic factors.
The interaction results reported in Table 3 provide direct evidence on Hypothesis 2,
revealing substantial cross-country heterogeneity in the moderating role of DFL on the
relationship between Atten and SI. In Brazil, the interaction between Atten and DFL is
statistically insignificant, with or without controls, indicating that DFL raises overall SI but
does not alter the effect of attention on investment decisions, consistent with Brazil’s still-
developing financial knowledge (Ramalho, 2019). A similar result holds for Finland, where
the interaction remains insignificant across specifications, despite strong direct effects of
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

Tabl e2 . Marginal effects main model
|     | Al lcountries | Brazil | Finland | Philippines | Saudi Arabia |     |
| --- | ------------- | ------ | ------- | ----------- | ------------ | --- |
(1) (2) (3) (4) (5) (6) (7) (8) (9) (10) (11) (12) (13) (14) (15)
Atten 0.172*** 0.158*** 0.122*** 0.0828*** 0.0798*** 0.0533*** 0.281*** 0.279*** 0.235*** 0.183*** 0.184*** 0.125*** 0.143*** 0.0997*** 0.0479***
(0.0110) (0.0110) (0.0109) (0.0139) (0.0139) (0.0132) (0.0423) (0.0419) (0.0409) (0.0247) (0.0247) (0.0257) (0.0161) (0.0164) (0.0159)
| DF L | 0.0584*** | 0.0422*** | 0.104*** | 0.0681*** | 0.0346*** |     |
| ---- | --------- | --------- | -------- | --------- | --------- | --- |
|      | (0.0066)  | (0.0100)  | (0.0166) | (0.0180)  | (0.0111)  |     |
Digital financia l �0.0087 5 �0.0113** 0.0247*** 0.0137 �0.0370* * �0.0356** �0.0018  �0.0054 �0.0152  0.000805
behavior  (0.00551) (0.00529) (0.0087) (0.0086) (0.0146) (0.0140) (0.0130) (0.0124) (0.0093) (0.00904)
Digital financia l 0.0607*** 0.0388*** 0.0268*** 0.0098 0.0954*** 0.0490*** 0.055*** 0.0388*** 0.0650*** 0.0539***
knowledge  (0.00504) (0.00498) (0.0069) (0.0067) (0.0117) (0.0118) (0.0145) (0.0142) (0.0094) (0.00888)
Digital financia l 0.00423 0.000228 �0.0044  �0.0057 0.0270** 0.0254** 0.0122 �0.0003 �0.0148 �0.0128
attitude (0.00517) (0.00499) (0.0073) (0.0071) (0.0125) (0.0120) (0.0131) (0.0130) (0.0100) (0.00953)
| Gender      |     | 0.0472***   | 0.0755***  | 0.0805*** | 0.0496**  | �0.0163    |
| ----------- | --- | ----------- | ---------- | --------- | --------- | ---------- |
|             |     | (0.00879)   | (0.0126)   | (0.0218)  | (0.0251)  | (0.0150)   |
| Age         |     | �0.000664** | �0.0027*** | 0.0013*   | �0.00175* | 0.000305   |
|             |     | (0.000326)  | (0.0005)   | (0.0007)  | (0.0010)  | (0.000690) |
| Educatio n  |     | 0.0699***   | 0.0193***  | 0.0876*** | 0.104***  | 0.139***   |
|             |     | (0.00539)   | (0.0068)   | (0.0118)  | (0.0169)  | (0.0143)   |
| Employment  |     | 0.0484***   | 0.0370**   | 0.0983*** | 0.0813*** | �0.0189    |
| status      |     | (0.0105)    | (0.0150)   | (0.0233)  | (0.0270)  | (0.0279)   |
| Incom e     |     | 0.0484***   | 0.0262***  | 0.0804*** | 0.0149    | 0.0777***  |
|             |     | (0.00489)   | (0.0078)   | (0.0108)  | (0.0123)  | (0.0115)   |
Fixe deffec t Yes Yes Yes No No No No No No No No No No No No
L Rχ 2 1,064.48 1,133.43 1,573.89 59.54 68.64 195.98 73.82 109.43 307.08 65.86 69.47 148.16 77.7 120.50 313.23
Pro b> χ 2  0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
Observations 6,865 6,865 6,865 2,000 2,000 2,000 1,806 1,806 1,806 1,000 1,000 1,000 2,059 2,059 2,059
Note(s): Models (1) ,(2) ,and (3 )correspon dto th efull sample of countries .Model s(4) ,(5) ,an d(6 )correspond t oBrazil ;models (7) ,(8) ,an d(9 )t oFinland; model s(10) ,(11), an d
(12) t oth ePhilippines ;and models (13), (14), and (15) to Saud iArabia. Standar derror sare i nparentheses. *** ,** an d* indicate statistical significance a tthe 1%, 5% an d10%
| levels, respectively |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- |
Source(s): Authors ’own work
Administrative
Finance and  Economics,
Journal of
Science
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

JEFAS
Tabl e3 . Marginal effects and th einteractive role of digita lfinancia lliteracy
|     | All |     | Saudi |     |     | Saudi |
| --- | --- | --- | ----- | --- | --- | ----- |
countries Brazil Finland Philippines Arabia All countries Brazil Finland Philippines Arabia
|     | (1) (2) | (3) (4) | (5) (6) | (7) | (8) (9) | (10) |
| --- | ------- | ------- | ------- | --- | ------- | ---- |
Atten 0.171*** 0.0878*** 0.285*** 0.207*** 0.150*** 0.131*** 0.0528*** 0.239*** 0.144*** 0.0800***
(0.0110) (0.0154) (0.0457) (0.0244) (0.0152) (0.0108) (0.0147) (0.0442) (0.0256) (0.0151)
DFL 0.0612*** 0.0465*** 0.103*** 0.130*** 0.00475 0.0285*** 0.0128 0.0461*** 0.0850*** 0.0134
(0.00758) (0.0117) (0.0175) (0.0217) (0.0130) (0.00742) (0.0113) (0.0173) (0.0213) (0.0126)
Attention * DFL �0.0118  �0.0168  0.0148 �0.192***  0.0929*** 0.00463 0.00376 0.0292 �0.148***  0.0787***

(0.0161) (0.0226) (0.0594) (0.0374) (0.0236) (0.0153) (0.0224) (0.0569) (0.0364) (0.0225)
| Gender     |     |     | 0.0485***    | 0.0763***    | 0.0911*** 0.0455*     | �0.0280*   |
| ---------- | --- | --- | ------------ | ------------ | --------------------- | ---------- |
|            |     |     | (0.00885)    | (0.0126)     | (0.0216) (0.0249)     | (0.0149)   |
| Age        |     |     | �0.000730**  | �0.00273***  | 0.00107 �0.00189**    | 0.000411   |
|            |     |     | (0.000327)   | (0.000473)   | (0.000767) (0.000953) | (0.000696) |
| Education  |     |     | 0.0726***    | 0.0209***    | 0.0924*** 0.0974***   | 0.147***   |
|            |     |     | (0.00543)    | (0.00678)    | (0.0118) (0.0168)     | (0.0146)   |
Employment statu s 0.0489*** 0.0384** 0.0961*** 0.0810*** �0.0167
|              |        |       | (0.0106)  | (0.0150)  | (0.0234) (0.0268) | (0.0278)  |
| ------------ | ------ | ----- | --------- | --------- | ----------------- | --------- |
| Income       |        |       | 0.0501*** | 0.0264*** | 0.0833*** 0.00995 | 0.0782*** |
|              |        |       | (0.00490) | (0.00784) | (0.0108) (0.0122) | (0.0115)  |
| Fixed effect | Yes No | No No | No Yes    | No        | No No             | No        |
2
LR   χ  1,065.02 60.09 73.88 90.95 93.29 1,531.92 192.52 289.14 160.9 300.07
Pro b> χ  2  0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
Observations 6,865 2,000 1,806 1,000 2,059 6,865 2,000 1,806 1,000 2,059
Note(s): Standard errors are in parentheses. ***, ** and * indicate statistical significance at th e1% ,5% an d10% levels ,respectively

Source(s): Authors’ own work
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

attention and DFL, suggesting that digital competencies are already embedded in information Journal of
processing in a high-literacy context (Kalmi and Ruuskanen, 2017). The Philippines exhibits a Economics,
negative and statistically significant interaction effect (Model 9: �0.148, p < 0.01), implying Finance and
that higher levels of DFL weaken the positive impact of Atten on SI. This finding aligns with Administrative
national evidence documenting low overall financial literacy and less sophisticated financial Science
behavior (Bangko Sentral ng Pilipinas, 2024). Conversely, Saudi Arabia shows a positive,
significant interaction (Model 10: 0.0787, p < 0.01), consistent with evidence linking higher
financial literacy to better investment decisions (Albarrak et al., 2024).
Overall, these findings indicate that DFL does not operate as a universal buffer against
digital persuasion. Instead, its moderating role is highly context-dependent and is shaped by
the level and distribution of financial knowledge across countries. Consequently, Hypothesis 2
receives partial empirical support, as the direction and strength of the interaction between
attention and DFL vary systematically across national settings.
4.1 Endogeneity
4.1.1 Two-stage instrumental variable regression. To address potential reverse causality,
endogeneity is mitigated using an instrumental variable (IV) based on online purchasing
behavior, measured on a 1–4 scale that indicates how often respondents bought goods and
services online in the past 12 months. More frequent online shopping increases exposure to
digital platforms where influencers are prominent, plausibly raising attention to their
recommendations. Consistent with this channel, social media interactions shape purchase
decisions (Ismael et al., 2025), and influencers’ live-commerce demonstrations affect
consumer choices (Li et al., 2025). The instrument is assessed in terms of exogeneity,
relevance and strength; it should be valid, relevant and strong (Cameron and Trivedi, 2005).
Table 4 reports Spearman correlations between the instrument and baseline residuals (Panel A)
and between the instrument and the endogenous variable (Panel B), with p-value testing for
independence. The instrument appears valid in Finland, the Philippines and Saudi Arabia, as
independence from model errors cannot be rejected. It is relevant in Brazil, Finland and the
Philippines, where independence from the endogenous variable is rejected, with the strongest
associations in Brazil and the Philippines. In the pooled sample, the instrument correlated
15.68% with the endogenous variable, rejecting independence.
To address potential endogeneity concerns with a nonlinear dependent variable, the
methodology proposed by Wooldridge (2014), known as the control function method or two-
stage residual inclusion (2SRI), was applied. A central feature of this approach is that, in the
second stage, the generalized residuals estimated in the first stage are included in the
specification. As shown in Table 5, the IV is significantly positive for the pooled sample,
indicating that individuals who purchase goods and services online are 3.8% (p < 0.01) more
likely to pay attention to investment recommendations issued by social media influencers;
Table 4. Spearman correlations between the instrumental variable, model errors and the endogenous variable
Brazil Finland Philippines Saudi Arabia
Panel A: Spearman correlations – Instrument and baseline model errors
Rho �0.2689 �0.0280 �0.0286 0.0250
p-value 0.000 0.2347 0.3665 0.2568
Panel B: Spearman correlations – Instrument and endogenous variable
Rho 0.2543 0.0950 0.3089 0.0112
p-value 0.000 0.0001 0.000 0.6115
Source(s): Authors’ own work
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

JEFAS
| Tabl e5 . Marginal effects fro |   mth etwo-stage residual model |         |     |          |             |              |        |
| ------------------------------ | ------------------------------- | ------- | --- | -------- | ----------- | ------------ | ------ |
|                                | All countries                   | Brazi l |     | Finland  | Philippines | Saudi Arabia |        |
|                                |                                 | Second  |     |          | Second      | Second       | Second |
Firs tstep step Firs tstep Second step Firs tstep step Firs tste p step Firs tste p step
|     |     | Stock | Stock |     | Stock | Stock | Stock |
| --- | --- | ----- | ----- | --- | ----- | ----- | ----- |
Attention investment Attention investment Attention investment Attention investment Attention investment
| I.V.  | 0.0380*** | 0.0431*** |          | 0.0113    | 0.0704*** | 0.00336   |           |
| ----- | --------- | --------- | -------- | --------- | --------- | --------- | --------- |
|       | (0.00444) | (0.00708) |          | (0.00717) | (0.0109)  | (0.0104)  |           |
| Atten |           | 0.329***  | 0.244*** |           | 0.118     | 0.568***  | �0.429**  |
|       |           | (0.0611)  | (0.0822) |           | (0.269)   | (0.121 )  | (0.178)   |
DFL �0.0543***  0.0381***  0.0153 0.00448 �0.0265** * 0.0449**  0.00949  0.0212 �0.119***  �0.0347

(0.00622)  (0.00726) (0.0117) (0.0105) (0.00908)  (0.0184) (0.0188) (0.0173) (0.0119)  (0.0266)
Gender �0.0655***  0.0644***  0.00771 0.0724*** �0.00713  0.0908** * �0.0660** * 0.0969** * �0.178***  �0.144***
(0.00866 ) (0.0101) (0.0139) (0.0121) (0.0127)  (0.0217) (0.0255)  (0.0278) (0.0165) (0.0409)
Ag e �0.00350***  �0.000177  �0.00355***  �0.00159***  �0.00317***  0.000686 �0.00524***  0.000722 0.00183**  0.00162*
(0.000334) (0.000391) (0.000518) (0.000595) (0.000441) (0.00123) (0.000958) (0.00116) (0.000890) (0.000826)
Education  0.0590*** 0.0562*** 0.0113 0.0143** 0.00489 0.0910*** 0.0803*** 0.0442** 0.183*** 0.253***
(0.00535) (0.00702) (0.00801) (0.00709) (0.00668) (0.0124) (0.0152) (0.0223) (0.0149) (0.0406)
Employment �0.0054 4 0.0504***  �0.0127  0.0355** * �0.00432  0.0954*** 0.00605 0.0671*** �0.0655*  �0.0560*
status (0.0108) (0.0106) (0.0154) (0.0137) (0.0133) (0.0238) (0.0275) (0.0258) (0.0336) (0.0319)
Income  0.0198*** 0.0458*** 0.00403 0.0245*** 0.0256*** 0.0867*** 0.00739 0.00345 �0.00335  0.0742***
(0.00513) (0.00512) (0.00941) (0.00748) (0.00668) (0.0134) (0.0125) (0.0122) (0.0128) (0.0111)
| Resid         |     | �0.116** * | �0.109**  |     | 0.0593  | �0.271*** | 0.500*** |
| ------------- | --- | ---------- | --------- | --- | ------- | --------- | -------- |
|               |     | (0.0353)   | (0.0477)  |     | (0.138) | (0.0743)  | (0.178)  |
| Fixed effect  | Yes | Yes No     | No        | No  | No No   | No No     | No       |
LR χ  2 923.35 1,164.47 179.45 156.16 112.60 244.24 165.61 120.45 438.26 188.65

Pro b> χ  2  0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
Observations 6,865 6,865 2,000 2,000 1,806 1,806 1,000 1,000 2,059 2,059
Note(s): Standard errors are in parentheses. ***, ** and * indicat estatistical significance at th e1% ,5% an d10% levels ,respectively

Source(s) :Authors’ ow nwork
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

however, this effect is not statistically significant for Finland or Saudi Arabia. In the second- Journal of
stage regression, the residual is significant, and Atten remains significant at the 1% level for Economics,
the pooled sample, again with Finland as the exception. After 2SRI correction, social media Finance and
attention still significantly affects investment decisions. Administrative
4.1.2 Propensity score matching (PSM). The propensity score matching (PSM) is used to Science
correct selection bias that arises when individuals who receive a treatment differ
systematically from those who do not (Ali and Behera, 2015). This technique allows
estimating the average treatment effect by matching treated and untreated individuals with
similar observable characteristics (Rosenbaum and Rubin, 1983). PSM is necessary in this
study because attention to investment recommendations from influencers is not randomly
assigned and may be associated with individual attributes such as gender, age, DFL or income.
Propensity scores were obtained using a logit model, after which two matching methods were
applied: single nearest-neighbor matching and nearest-neighbor matching with the
Mahalanobis distance. As reported in Table 6 (Panels A and B), substantial differences
existed between individuals who paid attention to influencer recommendations and those who
did not, but these differences were considerably reduced after applying PSM, indicating that
both groups became adequately balanced across observed covariates. Regarding the results,
the probability of participating in the stock market reaches 32.1% (Panel A.1) among
individuals who paid attention to influencers, compared with only 21.8% among those who did
not: an absolute difference of 10%, significant at the 1% level. These results match baseline
estimates, supporting robustness: influencer attention increases the likelihood of SI. The
country-level average treatment effect on the treated estimates are presented in the
Supplementary file, Supplementary Table No. S4 and Supplementary Table No. S5.
5. Discussion
5.1 Theoretical implications
The results reinforce and broaden its theoretical implications in the context of social media and
DFL on SI. The evidence indicates that attention would act as a prior selection mechanism, in
which signals from influencers operate as attention-grabbing events that delimit the set of
investment alternatives. The findings strengthen attention-based explanations by showing that
salient digital signals may function as “attention triggers” that stimulate investment activity,
even when informational content is limited (Arnold et al., 2022) and that attention to social
media content catalyzes investment decisions (Kim and Fan, 2025).
Likewise, the results nuance the view of DFL as a universal buffer against digital
persuasion, as its moderating effect is heterogeneous and context-dependent. The
heterogeneity observed in the moderating role of DFL can be understood through
Hofstede’s cultural dimensions (The Culture Factor Group, 2025) – particularly
individualism or collectivism, uncertainty avoidance and long-term orientation, which
influence how individuals process financial information and respond to attention stimuli
across different national settings. In more collectivist societies, such as Brazil, the Philippines
and Saudi Arabia, economic decisions tend to be more influenced by social signals, amplifying
the impact of recommendations disseminated on social media. Uncertainty avoidance
introduces a second mechanism: in societies with a high need for certainty, such as Brazil and
Saudi Arabia, digital signals may function as cognitive shortcuts. However, while in Brazil
DFL has not yet reached sufficient levels to modify this pattern, in Saudi Arabia, greater digital
competencies allow attention to translate into more effective investment decisions. In the
Philippines, where uncertainty avoidance is lower, increased DFL fosters a more critical
evaluation of social signals, weakening the relationship between attention and investment.
Finally, long-term orientation explains why DFL is integrated into the general decision-
making process in Finland, whereas in countries with a short-term orientation, DFL may act
both as a protective filter and as a facilitator of investment action.
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

JEFAS Table 6. Average treatment effect on the treated
Panel A.1: Average treatment effect on the treated (ATT) using nearest-neighbor
| Variable  | Treatment  | Controls  | Difference  | S.E.   | T-stat |
| --------- | ---------- | --------- | ----------- | ------ | ------ |
| SI        | 0.321      | 0.218     | 0.103       | 0.021  | 4.870  |
Panel A.2: Comparison of variable averages under PSM
| Variable  | Matched   |         |         |          | p > t |
| --------- | --------- | ------- | ------- | -------- | ----- |
|           |           | Treated | Control | t        |       |
| DFL       | Unmatched | �0.114  | 0.025   | �6.300   | 0.000 |
|           |           | �0.114  | �0.145  | 1.090    |       |
|           | Matched   |         |         |          | 0.276 |
| Gender    | Unmatched | 0.394   | 0.518   | �7.920   | 0.000 |
|           | Matched   | 0.394   | 0.389   | 0.250    | 0.803 |
| Age       | Unmatched | 35.333  | 43.391  | �17.130  | 0.000 |
|           | Matched   | 35.333  | 35.859  | �1.080   | 0.281 |
Education
|                    | Unmatched | 3.691 | 3.160 | 16.440  | 0.000 |
| ------------------ | --------- | ----- | ----- | ------- | ----- |
|                    | Matched   | 3.691 | 3.708 | �0.520  | 0.602 |
| Employment status  | Unmatched | 0.771 | 0.638 | 8.970   | 0.000 |
|                    | Matched   | 0.771 | 0.762 | 0.530   | 0.597 |
| Income             | Unmatched | 2.105 | 1.834 | 9.520   | 0.000 |
|                    | Matched   | 2.105 | 2.092 | 0.350   | 0.724 |
Panel B.1: Average treatment effect on the treated (ATT) using nearest-neighbor matching with Mahalanobis
distance
| Variable  | Treated  | Controls  | Difference  | S.E.  |     |
| --------- | -------- | --------- | ----------- | ----- | --- |
T-stat
| SI  | 0.321  | 0.221  | 0.100  | 0.019  | 5.140 |
| --- | ------ | ------ | ------ | ------ | ----- |
Panel B.2: Comparison of variable averages under PSM
| Variable  | Matched   | Treated | Control | t       | p > t |
| --------- | --------- | ------- | ------- | ------- | ----- |
|           |           | �0.114  |         | �6.300  |       |
| DFL       | Unmatched |         | 0.025   |         | 0.000 |
|           | Matched   | �0.114  | �0.104  | �0.370  | 0.712 |
| Gender    | Unmatched | 0.394   | 0.518   | �7.920  | 0.000 |
|           | Matched   | 0.394   | 0.394   | 0.000   | 1.000 |
�17.130
| Age | Unmatched | 35.333 | 43.391 |     | 0.000 |
| --- | --------- | ------ | ------ | --- | ----- |
�0.280
|                   | Matched   | 35.333 | 35.466 |        | 0.780 |
| ----------------- | --------- | ------ | ------ | ------ | ----- |
| Education         | Unmatched | 3.691  | 3.160  | 16.440 | 0.000 |
|                   | Matched   | 3.691  | 3.687  | 0.130  | 0.901 |
| Employment status | Unmatched | 0.771  | 0.638  | 8.970  | 0.000 |
|                   | Matched   | 0.771  | 0.771  | 0.000  | 1.000 |
| Income            | Unmatched | 2.105  | 1.834  | 9.520  | 0.000 |
|                   | Matched   | 2.105  | 2.104  | 0.020  | 0.981 |
Source(s): Authors’ own work
5.2 Managerial/policy implications
The results have direct implications for market participants and policymakers, particularly
when considering the interaction between attention and social media, DFL and the cultural
context. First, the positive association between attention to influencers and equity market
participation suggests that influencers and platform-mediated recommendations have become
established as influential channels for disseminating market signals, with potential relevance
for financial inclusion and economic empowerment strategies (M€olders et al., 2025). For firms
operating in financial markets and digital investment platforms, these findings highlight the
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

need to design more responsible social media communication strategies, incorporating clear Journal of
information on risks, investment horizons and potential conflicts of interest. Nevertheless, Economics,
evidence showing that attention-driven dynamics can increase risk-taking and impair returns Finance and
in other settings reinforces the need to complement inclusion initiatives with financial Administrative
education and effective consumer protection mechanisms (Arnold et al., 2022). Science
In this regard, recent regulatory guidance and enforcement actions emphasize that financial
promotions on social media must be clear, fair and not misleading, and that influencer
participation and compensation schemes should be appropriately disclosed (FCA, 2024). For
individual investors, these guidelines underscore the importance of critically assessing the
source, incentives and quality of information received through social media before making
investment decisions. This regulatory emphasis is particularly relevant, given that the
abundance of stock-related information available in financial markets makes investment
decision-making especially demanding, as processing such information imposes a high
cognitive load and may lead to irrational choices (Isidore and Christy, 2019).
Taken together, these findings indicate that public policies and regulatory frameworks
should be context-sensitive, recognizing that DFL does not operate as a universal buffer but
rather as a culturally contingent mechanism that can either amplify or attenuate the
behavioral impact of social media attention on SI. Consequently, strengthening DFL,
alongside more transparent digital communication practices by firms and platform design
tools aimed at reducing impulsive decision-making, may contribute to a more informed,
prudent and sustainable financial environment (Shunmugasundaram and Sinha, 2025).
5.3 Limitations and future research agenda
This study has limitations that also point to promising directions for future research. First,
the analysis relies on cross-sectional and self-reported measures, which may introduce
reporting and inference biases; longitudinal or panel designs would enable researchers to
assess whether attention to social media predicts SI and longer-term investment
performance. Second, the question capturing attention to influencer recommendations
was only recently introduced in the OECD/INFE survey, which restricts intertemporal
comparisons and the analysis of dynamic effects. Future studies could incorporate
measures of attention intensity, platform specificity and content characteristics, such as
sentiment, emotional tone, credibility cues or informational complexity, to identify the
underlying behavioral mechanisms more precisely. In this regard, the use of machine
learning and natural language processing techniques applied to large-scale social media
data could substantially enrich the measurement of digital attention and allow a finer
classification of informational versus persuasive content.
6. Conclusion
Consistent with its objectives, this study contributes to the behavioral finance literature by
showing that individual attention to social media influencers significantly increases the
likelihood of SI, reinforcing attention-based explanations of investment behavior. The
heterogeneous moderating role of DFL across countries, based on differences in financial
literacy levels and cultural characteristics, underscores the need to interpret digital influence
within this broader context. Theoretically, the findings advance the understanding of how
digital signals function as behavioral triggers and how individual competencies shape their
effects, bridging digital finance and investor psychology. Practically, the results support
policies that strengthen DFL and improve the oversight of financial content on social media.
As these platforms become integral to retail investment decisions, effective regulation and
targeted education are essential to foster informed participation and reduce behavioral risks in
increasingly digital financial markets.
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

JEFAS Acknowledgments
We thank the OECD Secretariat for granting the INFE survey data, which made this research possible.
Their support and commitment to advancing financial literacy research were essential for the
development of this study. We would also like to thank the anonymous reviewer, whose valuable
comments significantly enriched the quality and clarity of the manuscript, helping us strengthen both the
theoretical foundation and the empirical analysis.
Appendix
Variables used in the 2023 OECD international survey of adult financial literacy
A1.1. Stock investment (SI) variable
It was defined as a binary variable identifying individuals who met at least one of the three conditions,
coded as 1 when at least one of the specified actions was performed.
(1) QF3_7: In the past 12 months, have you been [personally] saving money in any of the following
ways, whether or not you still have the money? Please don’t take into account any money paid
into a pension, but think about all kinds of savings, such as building up a rainy-day fund or
putting money aside for a special occasion. Response: Investing in shares and securities.
(2) QP2_12: Can you tell me whether you [personally or jointly] currently hold any of these types of
products? Response: Shares and securities.
(3) QP3_12: In the last two years, which of the following types of financial products have you
chosen [Personally or jointly], whether or not you still hold them? Please do not include products
that were renewed automatically. Response: Shares and securities.
A1.2. Investor attention (Atten) variable
Question QP7_6 is used: “Which of these sources of information do you feel significantly influenced your
decision {about which one to take out}?” The variable takes the value of 1 if the respondent selects the
option “A recommendation from people you do not know (such as social media or ‘influencers’)”, and
0 otherwise.
A1.3. Digital financial literacy (DFL) variables and their dimensions
The DFK dimension includes three true-or-false items. Each item scores 1 for a correct answer and
0 otherwise:
(1) QK7_4, “True or False: A digital financial contract requires the signature on a paper contract to
be considered valid.”
(2) QK7_5, “True or False: The personal data that I share publicly online may be used to target me
with personalized commercial or financial offers.”
(3) QK7_6, “True or False: Cryptocurrencies have the same legal tender status as banknotes
and coins.”
The DFB dimension includes four items. Responses are coded as 1 for the appropriate behavior and
0 otherwise:
(1) QS2_6, “I share the passwords and PINs of my bank account with close friends.”
(2) QS2_7, “Before buying a financial product online I check if the provider is regulated in my
country.”
(3) QS2_8, “I share information about my personal finances publicly online (e.g. on social media).”
(4) QS3_13, “I regularly change the passwords on websites that I use for online shopping and
personal finance.”
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

The DFA dimension consists of three statements. Answers are scored 1 for the appropriate attitude Journal of
and 0 otherwise. Economics,
(1) QS4_1, “I think that it is safe to shop online using public Wi-Fi networks.”
Finance and
Administrative
(2) QS4_2, “It is important to pay attention to the security of a website before making a transaction Science
online.”
(3) QS4_3, “I think it is not important to read the terms and conditions when buying something
online.”
A1.4. Gender (Gen)
Question QD1, which takes the value of 1 if the respondent identifies as male and 0 if female.
A1.5. Age
Question QD7: “How old are you?” Respondents report their age in years.
A1.6. Education (Edu) variable
Education is measured on a 0–5 scale. Level 0 indicates no formal education. Level 1 corresponds to
primary education, Level 2 to lower or secondary education, and Level 3 to upper secondary or high
school. Level 4 represents completed university studies (e.g. bachelor’s degree), while Level 5 includes
postgraduate education such as a master’s or a doctorate. The variable is labeled QD9.
A1.7. Employment status (ES) variable
The variable takes values of 1 or 0, where a value of 1 is assigned to two categories: individuals who are
self-employed and those who are employed for pay. Conversely, a value of 0 is assigned when the
respondent is an apprentice, homemaker, seeking work (unemployed), retired, not working, not seeking
work, or a student. The question label for this variable is QD10.
A1.8. Household income (Inc) variable
The variable QD13 classifies monthly household income into four categories: nonresponse, below 75% of
the median, between 75 and 125% of the median, and above 125%, using country-specific thresholds. The
three income ranges for each country are as follows:
Table A1. Income ranges for each country
Salary
range Saudi Arabia Brazil Philippines Finland
Low (1) Up to 7,000 Saudi Up to 2,604 reais Up to 20,800 Philippine Up to 30,000 euros
riyals pesos
Medium Between 7,000 and Between 2,604 Between 20,800 and Between 30,000
(2) 11,000 Saudi riyals and 6,510 reais 42,000 Philippine pesos and 50,000 euros
High (3) 11,000 Saudi riyals or 6,510 reais or 42,000 Philippine pesos 50,000 euros or
more more or more more
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

JEFAS Supplementary material
The supplementary material for this article can be found online.
References
Abdallah, W., Tfaily, F. and Harraf, A. (2024), “The impact of digital financial literacy on financial
behavior: customers’ perspective”, Competitiveness Review: An International Business Journal,
Vol. 35 No. 2, pp. 347-370, doi: 10.1108/CR-11-2023-0297.
Al-Smadi, M. (2023), “Examining the relationship between digital finance and financial inclusion:
evidence from MENA countries”, Borsa Istanbul Review, Vol. 23 No. 2, pp. 464-472, doi:
10.1016/j.bir.2022.11.016.
Albarrak, M.S., Alokley, S.A. and Ansari, Y. (2024), “Financial literacy among working adults: the
case of Saudi Arabia”, Quantitative Finance and Economics, Vol. 8 No. 4, pp. 841-866, doi:
10.3934/QFE.2024032.
Alfieri, E., Burlacu, R. and Enjolras, G. (2025), “Cryptocurrency bubbles, information asymmetry and
noise trading”, The Journal of Risk Finance, Vol. 26 No. 2, pp. 295-319, doi: 10.1108/JRF-07-
2024-0220.
Ali, A. and Behera, B. (2015), “Household participation and effects of community forest management
on income and poverty levels: empirical evidence from Bhutan”, Forest Policy and Economics,
Vol. 61, pp. 20-29, doi: 10.1016/j.forpol.2015.06.006.
Anwar, M. (2025), “How digital financial literacy and social media usage build saving behavior among
Generation Z. Asia-Pacific”, Journal of Business Administration, Vol. 143 No. 2, pp. 1-26, doi:
10.1108/APJBA-04-2025-0329.
Arnold, M., Pelster, M. and Subrahmanyam, M.G. (2022), “Attention triggers and investors’ risk-
taking”, Journal of Financial Economics, Vol. 143 No. 2, pp. 846-875, doi: 10.1016/
j.jfineco.2021.05.031.
Bangko Sentral ng Pilipinas (2024), “How does financial literacy affect financial behavior over the life
cycle? Evidence from Filipino households”, (Discussion Paper No. 2024 13), available at:
https://www.bsp.gov.ph/Sites/researchsite/Publications/BSP-Discussion-Papers/DP202413.pdf
Barber, B. and Odean, T. (2008), “All that glitters: the effect of attention and news on the buying
behavior of individual and institutional investors”, The Review of Financial Studies, Vol. 21
No. 2, pp. 785-818, doi: 10.1093/rfs/hhm079.
Barber, B., Huang, X., Odean, T. and Schwarz, C. (2022), “Attention-induced trading and returns:
evidence from Robinhood users”, The Journal of Finance, Vol. 77 No. 6, pp. 3141-3190, doi:
10.1111/jofi.13183.
Bayar, O. and Kesici, E. (2024), “The impact of social media on venture capital financing: evidence
from Twitter interactions”, Review of Quantitative Finance and Accounting, Vol. 62 No. 1,
pp. 195-224, doi: 10.1007/s11156-023-01199-4.
Bhat, S., Lone, U., SivaKumar, A. and Krishna, U. (2024), “Digital financial literacy and financial
well-being–evidence from India”, International Journal of Bank Marketing, Vol. 43 No. 3,
pp. 522-548, doi: 10.1108/IJBM-05-2024-0320.
Cameron, A. and Trivedi, P. (2005), Microeconometrics: Methods and Applications, Cambridge
University Press, Cambridge.
Carosia, A.O., Coelho, G.P. and Silva, A.E.A.D. (2020), “Analyzing the Brazilian financial market
through Portuguese sentiment analysis in social media”, Applied Artificial Intelligence, Vol. 34
No. 1, pp. 1-19, doi: 10.1080/08839514.2019.1673037.
Chen, S. and Ren, F. (2025), “Does social media information affect individual investor disposition
effect? Evidence from Xueqiu”, PLoS One, Vol. 20 No. 7, e0328547, doi: 10.1371/
journal.pone.0328547.
Da, Z., Engelberg, J. and Gao, P. (2011), “In search of attention”, The Journal of Finance, Vol. 66
No. 5, pp. 1461-1499, doi: 10.1111/j.1540-6261.2011.01679.x.
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

Financial Conduct Authority (2024), “Finalised guidance on financial promotions on social media Journal of
(FG24/1)”, available at: https://www.fca.org.uk/publication/finalised-guidance/fg24-1.pdf Economics,
Guiso, L., Sapienza, P. and Zingales, L. (2008), “Trusting the stock market”, The Journal of Finance, Finance and
Vol. 63 No. 6, pp. 2557-2600, doi: 10.1111/j.1540-6261.2008.01408.x. Administrative
Science
Hermansson, C., Jonsson, S. and Liu, L. (2022), “The medium is the message: learning channels,
financial literacy, and stock market participation”, International Review of Financial Analysis,
Vol. 79, 101996, doi: 10.1016/j.irfa.2021.101996.
Hirshleifer, D. and Teoh, S. (2003), “Limited attention, information disclosure, and financial
reporting”, Journal of Accounting and Economics, Vol. 36 Nos 1-3, pp. 337-386, doi: 10.1016/
j.jacceco.2003.10.002.
Hylkil€a, K., M€annikk€o, N., Castr�en, S., Mustonen, T., Peltonen, A., Konttila, J., M€annist€o, M.,
K€a€ari€ainen, M. and K€a€ari€ainen, M. (2023), “Association between psychosocial well-being and
problematic social media use among Finnish young adults: a cross-sectional study”, Telematics
and Informatics, Vol. 81, 101996, doi: 10.1016/j.tele.2023.101996.
Isidore, R. and Christy, P. (2019), “The relationship between the income and behavioral biases”,
Journal of Economics, Finance and Administrative Science, Vol. 24 No. 47, pp. 127-144, doi:
10.1108/JEFAS-10-2018-0111.
Ismael, A., Amin, M., Ali, M., Hajd�u, Z. and P�eter, B. (2025), “Relationship between social media
marketing and young customers’ purchase intention towards online shopping”, Cogent Social
Sciences, Vol. 11 No. 1, 2459881, doi: 10.1080/23311886.2025.2459881.
Jang, J. and Jun, S. (2025), “YouTube view count, investor attention and stock returns”, International
Review of Financial Analysis, Vol. 97, 103782, doi: 10.1016/j.irfa.2024.103782.
Kahneman, D. (1973), Attention and Effort, Prentice-Hall, Englewood Cliffs: NJ.
Kalmi, P. and Ruuskanen, O. (2017), “Financial literacy and retirement planning in Finland”, Journal
of Pension Economics and Finance, Vol. 17 No. 3, pp. 335-355, doi: 10.1017/
S1474747217000154.
Kim, H. (2025), “Social media engagement and retail investors’ short-termism”, Finance Research
Letters, Vol. 85, 108249, doi: 10.1016/j.frl.2025.108249.
Kim, K. and Fan, L. (2025), “Beyond the hashtags: social media usage and cryptocurrency
investment”, International Journal of Bank Marketing, Vol. 43 No. 3, pp. 569-590, doi: 10.1108/
IJBM-12-2023-0665.
Li, Y. and Huang, Y. (2025), “Social security, digital literacy, and relative poverty in China”, Finance
Research Letters, Vol. 71, 106446, doi: 10.1016/j.frl.2024.106446.
Li, X., Wang, Q., Yao, X., Yan, X. and Li, R. (2025), “How do influencers’ impression management
tactics affect purchase intention in live commerce? –Trust transfer and gender differences”,
Information and Management, Vol. 62 No. 2, 104094, doi: 10.1016/j.im.2024.104094.
Ly�ocsa,S�., Halouskov�a, M. and Haugom, E. (2023), “The US banking crisis in 2023: intraday attention
and price variation of banks at risk”, Finance Research Letters, Vol. 57, 104209, doi: 10.1016/
j.frl.2023.104209.
Maheshwari, H. and Samantaray, A.K. (2025), “Navigating investment challenges: financial literacy
and digital advisory services in countering behavioural biases”, International Journal of
Sociology and Social Policy, Vol. 46 Nos 3-4, pp. 1-17, doi: 10.1108/IJSSP-12-2024-0620.
Mazzoli, C. and Baiocco, S. (2025), “Unlocking sustainable investing through digital financial literacy:
the impact of advanced digital skills”, International Journal of Bank Marketing, Vol. 43 No. 9,
pp. 1-21, doi: 10.1108/IJBM-10-2024-0622.
Mertzanis, C., Ahmed, M.S., Faisal, R. and Al Suwaidi, R.A. (2025), “Does financial literacy drive
digital currency innovation? Cross-country evidence on CBDC adoption”, Borsa Istanbul
Review, Vol. 25, p. 109, doi: 10.1016/j.bir.2025.08.006.
M€olders, M., Bock, L., Barrantes, E. and Z€ulch, H. (2025), “Understanding finfluencers: roles and
strategic partnerships in retail investor engagement”, Journal of Business Research, Vol. 198,
115462, doi: 10.1016/j.jbusres.2025.115462.
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026

JEFAS M€unster, M., Reichenbach, F. and Walther, M. (2024), “Robinhood, Reddit, and the news: the impact of
traditional and social media on retail investor trading”, Journal of Financial Markets, Vol. 71,
100929, doi: 10.1016/j.finmar.2024.100929.
OECD (2023), OECD/INFE 2023 International Survey of Adult Financial Literacy, OECD Publishing,
Paris, OECD Business and Finance Policy Papers, No. 39, doi: 10.1787/56003a32-en.
Pak, T., Chatterjee, S. and Choung, Y. (2026), “Navigating digital finance: how digital financial literacy
influences digital financial services use and benefits in Korea”, Financial Innovation, Vol. 12
No. 1, p. 42, doi: 10.1186/s40854-025-00820-w.
Pedersen, L. (2022), “Game on: social networks and markets”, Journal of Financial Economics,
Vol. 146 No. 3, pp. 1097-1119, doi: 10.1016/j.jfineco.2022.05.002.
Ramalho, T.B. (2019), “Financial literacy in Brazil – do knowledge and self reported financial behavior
relate to financial outcomes?”, Revista Brasileira de Gest~ao e Finanças. doi: 10.12660/
rbgn.v21n2.2019.80215.
Reichenbach, F. and Walther, M. (2025), “Attention allocation of investors on social media: the role of
prospect theory”, The Journal of Behavioral Finance, Vol. 26 No. 3, pp. 317-334, doi: 10.1080/
15427560.2024.2309145.
Rosenbaum, P. and Rubin, D. (1983), “Constructing a control group using multivariate matched
sampling method that incorporate the propensity score”, The American Statistician, Vol. 39
No. 1, pp. 3-38.
Showkat, M., Nagina, R., Baba, M.A. and Yahya, A.T. (2025), “The impact of financial literacy on
women’s economic empowerment: exploring the mediating role of digital financial services”,
Cogent Economics and Finance, Vol. 13 No. 1, 2440444, doi: 10.1080/23322039.2024.2440444.
Shunmugasundaram, V. and Sinha, A. (2025), “The impact of behavioral biases on investment
decisions: a serial mediation analysis”, Journal of Economics, Finance and Administrative
Science, Vol. 30 No. 59, pp. 5-21, doi: 10.1108/JEFAS-08-2023-0243.
The Culture Factor Group (2025), “Country comparison tool”, available at: https://
www.theculturefactor.com/country-comparison-tool?countries5
Van Rooij, M., Lusardi, A. and Alessie, R. (2011), “Financial literacy and stock market participation”,
Journal of Financial Economics, Vol. 101 No. 2, pp. 449-472, doi: 10.1016/
j.jfineco.2011.03.006.
Wang, G., Wang, Y., Dong, Y. and Shen, X. (2024), “Media attention for carbon neutrality, investor
sentiment, and excess stock returns: evidence from mass media and social media”,
Computational Economics, Vol. 66 No. 3, pp. 1-25, doi: 10.1007/s10614-024-10739-6.
Warkulat, S. and Pelster, M. (2024), “Social media attention and retail investor behavior: evidence from
r/wallstreetbets”, International Review of Financial Analysis, Vol. 96, 103721, doi: 10.1016/
j.irfa.2024.103721.
Wooldridge, J. (2014), “Quasi-maximum likelihood estimation and testing for nonlinear models with
endogenous explanatory variables”, Journal of Econometrics, Vol. 182 No. 1, pp. 226-234, doi:
10.1016/j.jeconom.2014.04.020.
Corresponding author
Diana Bustamante can be contacted at: di.bustamante@uandresbello.edu
For instructions on how to order reprints of this article, please visit our website:
www.emeraldgrouppublishing.com/licensing/reprints.htm
Or contact us for further details: permissions@emeraldinsight.com
Downloaded from http://www.emerald.com/jefas/article-pdf/doi/10.1108/JEFAS-10-2025-0378/11493280/jefas-10-2025-0378en.pdf by guest on 24 June 2026