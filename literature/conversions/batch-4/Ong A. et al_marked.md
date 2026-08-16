---
conversion_metadata:
  converted_at: "2026-07-21T07:57:02Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ong A. et al.pdf"
  source_pdf_sha256: "f0facfef7a6511d9cf3f330e3b3094663f931093da78d71c5f32d28e6d342875"
  page_count: 26
  markdown_char_count: 199990
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Article
Purchasing Intentions Analysis of Hybrid Cars Using Random
Forest Classiﬁer and Deep Learning

Ardvin Kester S. Ong 1,2,*
Rocksel Andry V. Javier 3, Riañina D. Borres 1,4 and Josephine D. German 1

, Lara Nicole Z. Cordova 3, Franscine Althea B. Longanilla 3, Neallo L. Caprecho 3,

1

2

School of Industrial Engineering and Engineering Management, Mapúa University, 658 Muralla St.,
Intramuros, Manila 1002, Philippines
E.T. Yuchengco School of Business, Mapua University, 1191 Pablo Ocampo Sr. Ext, Makati 1205, Philippines
3 Young Innovators Research Center, Mapúa University, 658 Muralla St., Intramuros, Manila 1002, Philippines
4

School of Graduate Studies, Mapúa University, 658 Muralla St., Intramuros, Manila 1002, Philippines

* Correspondence: aksong@mapua.edu.ph; Tel.: +63-(2)8247-5000 (ext. 6202)

Abstract: In developed or ﬁrst-world countries, hybrid cars are widely utilized and essential in
technological development and reducing carbon emissions. Despite that, developing or third-world
countries such as the Philippines have not yet fully adopted hybrid cars as a means of transportation.
Hence, the Sustainability Theory of Planned Behavior (STPB) was developed and integrated with
the UTAUT2 framework to predict the factors affecting the purchasing intentions of Filipino drivers
toward hybrid cars. The study gathered 1048 valid responses using convenience and snowball
sampling to holistically measure user acceptance through twelve latent variables. Machine Learning
Algorithm (MLA) tools such as the Decision Tree (DT), Random Forest Classiﬁer (RFC), and Deep
Learning Neural Network (DLNN) were utilized to anticipate consumer behavior. The ﬁnal results
from RFC showed an accuracy of 94% and DLNN with an accuracy of 96.60%, which were able
to prove the prediction of signiﬁcant latent factors. Perceived Environmental Concerns (PENCs),
Attitude (AT), Perceived Behavioral Control (PBC), and Performance Expectancy (PE) were observed
to be the highest factors. This study is one of the ﬁrst extensive studies utilizing the MLA approach
to predict Filipino drivers’ tendency to acquire hybrid vehicles. The study’s results can be adapted
by automakers or car companies for devising initiatives, tactics, and advertisements to promote the
viability and utility of hybrid vehicles in the Philippines. Since all the factors were proven signiﬁcant,
future investigations can assess not only the behavioral component but also the sustainability aspect
of an individual using the STPB framework.

Keywords: hybrid cars; machine learning algorithm; purchasing intentions; sustainability theory of
planned behavior; UTAUT2

1. Introduction

Greenhouse gases emitted by oil-powered and fossil-fueled vehicles have increased
over the years. According to Tiseo [1], the global transportation sector is a signiﬁcant
polluter, producing approximately 7.3 billion tons of carbon dioxide emissions in 2020. In
the same year, passenger cars were the most abundant source of emissions, accounting
for 41% of global transportation emissions. In Wasiak’s [2] study, internal combustion
engines have two prominent drawbacks. The ﬁrst is the relatively low efﬁciency of turning
the energy contained in the fuel into valuable mechanical energy for propulsion, and the
second is that the production of carbon dioxide and other components of the exhaust gas
can contribute to global warming.

Hybrid cars are essential in technological development and in addressing carbon
emission reduction. Furthermore, hybrid car production covers three of the United Nations’
global Sustainable Development Goals (SDGs): the 7th SDG for affordable and clean energy,

Citation: Ong, A.K.S.; Cordova,

L.N.Z.; Longanilla, F.A.B.; Caprecho,

N.L.; Javier, R.A.V.; Borres, R.D.;

German, J.D. Purchasing Intentions

Analysis of Hybrid Cars Using

Random Forest Classiﬁer and Deep

Learning. World Electr. Veh. J. 2023,

14, 227. https://doi.org/10.3390/

wevj14080227

Academic Editor: Genevieve Cullen

Received: 20 July 2023

Revised: 12 August 2023

Accepted: 16 August 2023

Published: 18 August 2023

Copyright: © 2023 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

World Electr. Veh. J. 2023, 14, 227. https://doi.org/10.3390/wevj14080227

https://www.mdpi.com/journal/wevj

---

<!-- PAGE 2 -->

World Electr. Veh. J. 2023, 14, 227

2 of 26

the 8th SDG for decent work and economic growth, and the 13th SDG for climate action.
Since the introduction of the various SDGs, the usage of hybrid cars has been promoted [3].
The present generation is seeing an increase in the marketability of hybrid vehicles,
but their utility is not widely acknowledged. Irawan et al. [4] estimated that roughly 18.20%
of automobile owners have begun to consider switching from a conventional vehicle and
becoming potential hybrid car users, while 81.22% of car buyers continue to reject getting a
hybrid vehicle completely. Thus, consumer behavior should be investigated to understand
purchasing behavior for sustainable transportation to be widely accepted.

One theory widely used to comprehensively assess consumers’ behavior in the aspect
of purchasing and marketing is the Theory of Planned Behavior (TPB) [5]. It is also proven
to extensively measure the intention to purchase. It is applied to examine customers’
behavioral aspects of buying while simultaneously proving some of the determinants of
purchase intentions [6]. In line with the TPB framework, several studies have supported
that TPB is commonly used in the ﬁeld of purchasing cars due to its explanatory capacity to
predict the adoption or purchasing intention of cars, speciﬁcally in Hybrid Electric Vehicles
(HEVs) [7,8]. Similarly, a study by Javid et al. [9] stated that the determinants of TPB
could also be applied to consumers’ purchasing intention, even in Electric Vehicles (EVs).
However, in the study of German et al. [10], TPB has limited variables that restrain the
model for holistic measurements.

Another theory that can be used in assessing people’s acceptance and behavioral inten-
tions is the Uniﬁed Theory of Acceptance and Use of Technology 2 (UTAUT2). Venkatesh
et al. [11] explained how UTAUT2 comprehensively measures the behavioral aspect of
technology usage. Studies such as that of Nordhoff et al. [12] employed the UTAUT2 model
to explain the public acceptance of conditionally automated cars in European countries.
According to their study’s analysis, the UTAUT2 model can be applied to conditional
automation, with hedonic motivation, social inﬂuence, and performance expectancy in-
ﬂuencing the behavioral intention to purchase and utilize a conditionally automated car.
Similarly, Prasetyo and Vallespin [13] used the UTAUT2 model to identify the factors inﬂu-
encing users’ utility of mobile technology applications and services. In Malaysia, Khazaei
and Tareq [14] examined consumers’ usage of battery electric vehicles using the UTAUT2
since this model incorporated a broader scope of factors to measure consumers’ usage
intention. However, a limited number of studies have analyzed the purchasing intentions
of hybrid cars, especially in the Philippines. Only that of Ong et al. [15] was seen to consider
the purchasing intentions of hybrid cars in the Philippines.

In the Philippines, hybrid cars are available in the market. With only leading car brands
such as Cherry, Geely, Hyundai, Mitsubishi, Nissan, and Toyota selling the product, limited
access and popularity are observed. There were 11,851,192 registered motor vehicles and
fossil-fueled cars in the Philippines as of December 2020 [16]. Unlike other countries, the
hybrid car vehicle market in the Philippines only caters to the extreme upper class, which
accounts for only less than 0.1% of the market—with about 7000 hybrid cars registered in
2018 [17]. A recent report by Canivel [18] presented how Kia Philippines showed a steady
increase in the purchase of hybrid cars due to increase in fuel costs. The once affordable
diesel fuel is now relatively not that cheap in the market. It was reported that Kia was able
to increase its sales by 14.6% in 5 months’ time of the same year. Kampi also expected a
rise in sales of 17% in 2021. A report by Statista research department [19] summarized the
hybrid/electric cars sold from 2020–2022. From 378 in 2020 to 843 in 2021, a signiﬁcant
increase was seen in 2022 with 1013 units being sold. One reason why hybrid cars are not
highly popularized in the country is their maturity in the Philippine car market, leading to
low adoption rates of hybrid cars [20]. As reported by the news [21], only recently (2023)
has there been any plans to put up charging stations. It was reported that 200 charging
stations are planned to be established and 500 more by 2025. Therefore, the need to explore
the purchasing intentions of consumers with this relatively new technology for the country
is needed. The slow progression of movement in purchase may be capitalized by the
governing units since the establishment of charging stations and business are still on the

---

<!-- PAGE 3 -->

World Electr. Veh. J. 2023, 14, 227

3 of 26

rise. The determination of purchasing intention surrounding these hybrid cars would be
beneﬁcial for the literature and business owners alike.

This paper aimed to determine what factors inﬂuence drivers’ preferences for future
use and purchase intentions of hybrid vehicles (HVs) in the Philippines. Through the
integration of the extended pro-environmental theory of planned behavior (PEPB) of
German et al. [22] and the extended uniﬁed theory of acceptance and use of technology
(UTAUT2) on hybrid car purchase and usage intention, this study is one of the ﬁrst few
that examined the MLA approach to behavioral intention. Since the current study extended
the established purchasing intention of hybrid cars in the Philippines [15], this study
wanted to add to the literature on closing the gap between the use of machine learning
and analyzing human behavior. Structural equation modeling was considered by the
previous study [15], which suggested the use of machine learning to better analyze the
nonlinear relationship among latent variables. In accordance, the literature, such as that
of Fan et al. [23], explained that some latent variables when mediating factors are present
may cause little to no signiﬁcance. In accordance, the study of Woody [24] also presented
similar ﬁndings and explained that large nonlinear relationship models may be unreliable
when SEM is used as Heywood cases might be present which may cause wrong parameter
estimates [23,25]. Therefore, this study contributes to a more thorough evaluation of the
Philippines’ capability to sustain smart technology—eventually developing into a smart
and sustainable city.

2. Conceptual Framework
2.1. Theories and Related Studies

Venkatesh et al. [11] extended the existing UTAUT by incorporating three latent
variables, namely hedonic motivation, price value, and habit, thus developing the UTAUT2
model. The extensions proposed in the UTAUT2 produced a signiﬁcant improvement in the
variance explained in behavioral intention and technology use compared to its predecessor,
the UTAUT. Although the UTAUT2 model comprehensively analyzes the constructs for
the adoption of new technology, the scope of the model only evaluates the intention to
use new technologies, making it insufﬁcient in terms of holistically measuring the human
behavior attributes and aspects [26]. LaRose et al. [27] suggested that the UTAUT2 model
employs generic measures of the latent variables so that the same operational standards
can be used across different studies. This approach improved the model’s generalizability
but compromised the actionable information gathered. In addition, Ong et al. [26] stated
that the UTAUT2 model was not able to analyze the actual behavior of adopting technology.
Their study recommended incorporating other factors in order to obtain a more accurate
depiction of the viewpoint of the general population in light of these minor informational
gaps in the research. Subsequently, their study also showed that demographic factors as
mediating effects might not be considered in an analysis.

Several studies have integrated the UTAUT2 model with other theories to evaluate
innovative solutions and technology. Yuduang et al. [28] considered the integration of
Protection Motivation Theory (PMT) and UTAUT2 to assess the actual usage and intention
to use new technologies, speciﬁcally mobile applications. Their study stated that this
integration could be interpreted as a model that can comprehensively assess the intention
and actual usage of a mobile application. Hassan et al. [29] integrated the Privacy Calculus
Model (PMC) and UTAUT2 by adding four constructs: privacy concern, perceived risk,
trust, and perceived credibility. Their study validated that the addition of these constructs
thoroughly measured the consumers’ perspectives in relation to the adoption of new
technologies. Chang et al. [30] extended the UTAUT2 model, which assimilates the existing
constructs from the UTAUT2 along with age, gender, and experience as moderators. Their
study highlighted three ﬁndings: (1) age and experience reduce the impact of habit on
usage behavior, (2) age affects the inﬂuence of facilitating conditions on usage behavior, and
(3) the moderating effect of experience reduced the direct impact of behavioral intention on
usage behavior, making it irrelevant.

---

<!-- PAGE 4 -->

World Electr. Veh. J. 2023, 14, 227

4 of 26

The Theory of Planned Behavior (TPB) was established to anticipate human behavior.
According to the TPB, behavioral intention is inﬂuenced by three factors: attitude (AT),
subjective norm (SN), and perceived behavioral control (PEC) [31]. In the study of Chau
and Shiau [32], six well-known theoretical models were used to have a better understanding
of terms of behavioral intention, including the TPB and ﬁve other models, namely Service
Quality (SQ), Self-Efﬁcacy (SE), Motivational Model (MM), Technology Acceptance Model
(TAM), and Innovation Diffusion Theory (IDT); thus, the united model gave a thorough
grasp of the aspects that have a signiﬁcant impact on behavioral intention. With that,
the TPB is to be proven effective when combined with other models. It provides a more
comprehensive review of a person’s behavioral intention concerning hybrid cars with
reference to the said study. In the paper of Sentosa [33], the TPB, along with Technology
Acceptance Modeling (TAM), was integrated. In fulﬁllment of the paper, it was implied that
a person’s conduct is inﬂuenced by the desire to execute the activity, which is determined
by one’s attitude toward the behavior and subjective norm.

Kim and Hwang [34] used a research model that combined the TPB and Norm Activa-
tion Model (NAM) into a single theoretical framework to analyze eco-friendly behavioral
intentions to employ drone food delivery services. Furthermore, the moderating inﬂuence
of product knowledge was investigated in this study, as the amount of product knowledge
has a major impact on customer behaviors. PEPB and SERVQUAL models were integrated
to further determine Filipino consumers’ behavioral intention in the paper of German
et al. [22], particularly during the COVID-19 pandemic. In reliance on the said study, since
it was mentioned that the PEPB places emphasis on environmental concerns and authority,
variables from the TPB play a role in determining an individual’s behavioral intention
towards a particular situation or activity. Additionally, the two models also indicated a
higher level of investigation. They can be used in developing countries like the Philip-
pines because the said country strongly encourages the emergence of more sustainable
smart technology.

The PEPB model was developed as an extension of the theory of planned behavior
(TPB) since it could not address all factors relevant to this study [22]. Perceived author-
ity support (PAS), perceived environmental concern (PEC), perceived behavioral control
(PBC), subjective norm (SN), attitude (AT), and behavior intention (BI) were important in
determining the consumer’s intention to purchase products. Furthermore, other variables
under the three sustainability domains, namely economic, environmental, and social, are
covered in this study [35].

From the PEPB model [22], no economic aspects were covered.

In line with the
objective of this study, natural resources such as oil cannot be replenished rapidly enough,
which impacts the economy [36]. Fossil-fueled cars are known for producing large amounts
of toxic air pollutants in the atmosphere [37]. This increase in CO2 in the atmosphere will
raise the average temperature of the earth’s surface [38]. In order to reduce air pollution,
an alternative must be used. Asim et al. [39] found that hybrid cars are less harmful to
the environment because they use less gasoline. This shows that hybrid cars are much
cleaner and better for the environment; nevertheless, a consumer’s interest does not include
economic or environmental concerns [40]. An individual’s choice of hybrid cars may vary
depending on their social environment perspective. For instance, a consumer’s decision to
buy a hybrid car may possibly be inﬂuenced by their family, relatives, or friends [41].

The researchers utilized the Uniﬁed Theory of Technology Acceptance and Use of
Technology 2 (UTAUT2), the Pro-environmental Theory of Planned Behavior (PEPB), and
sustainability domains while incorporating an additional factor which is perceived eco-
nomic concerns (PECCs) to measure human behavior and technology acceptance. Turo ´n
and Kubik [42] studied the economic considerations of adopting autonomous vehicles com-
pared to the traditional automobile ﬂeet acquired by individual consumers in car-sharing
systems. In a different scope, Nisa et al. [43] revealed that perceived economic risk con-
sistently predicted mitigation behavior and policy support, and economic considerations
positively predicted all outcomes. Hence, the added factor, perceived economic concerns

---

<!-- PAGE 5 -->

World Electr. Veh. J. 2023, 14, 227

5 of 26

(PECCs), relates to a sense of social responsibility, extensive societal and commercial con-
sideration, and voluntary company involvement.

2.2. Conceptual Framework

The Sustainability Theory of Planned Behavior (STPB) framework used in this study
(Figure 1) encompasses the combination of the TPB and the PEPB with the UTAUT2 and
the extension of the economic factor. Several variables, including habit (HB), price value
(PV), hedonic motivation (HM), performance expectancy (PE), effort expectancy (EE),
facilitating conditions (FCs), perceived authority support (PAS), perceived environmental
concern (PENC), perceived behavioral control (PBC), perceived economic concern (PECC),
subjective norm (SN), attitude (AT), and behavioral intention (BI) were taken into account to
comprehensively analyze the intention to use and actual purchase intention of consumers’
toward hybrid cars. This framework was adopted from the study of Ong et al. [15].

Figure 1. Sustainability theory of planned behavior framework with UTAUT2.

The UTAUT2 model can measure the individual’s intention to use hybrid cars. In this
study, a new framework was established in which the social inﬂuence (SI) was transferred
to the PEPB model as subjective norm (SN). This is due to the PEPB having a subjective
norm (SN) variable, where they offered the same behavioral aspect based on the inﬂuence
of other people.

---

<!-- PAGE 6 -->

World Electr. Veh. J. 2023, 14, 227

6 of 26

Habit is repeatedly described as a result of earlier experiences with numerous factors,
which becomes a beneﬁcial choice [11]. It is also considered a potential factor in decision
making [44]. Positive feelings associated with the habitual product experience of driving
a car strengthens the habit and discourages consumers from embracing a new means of
transportation, such as hybrid cars [45,46]. Additionally, the adoption of a new car may be
inﬂuenced by previous experience with similar cars [47]. Thus, it was hypothesized that:

H1. Habit has a signiﬁcant direct effect on behavioral intention.

The term price value (PV) refers to consumers’ cognitive trade-off between the per-
ceived advantages of the applications and the ﬁnancial expense of utilizing them [11].
Moreover, the advantages and associated expenses of purchasing hybrid cars were assessed
and contrasted [48]. Irawan et al. [4] observed that gas price and supply affected the utility
of hybrid cars signiﬁcantly; this suggests that consumers are more likely to acquire a hybrid
car depending on the fuel cost and supply. Thus, it was hypothesized that:

H2. Price value has a signiﬁcant direct effect on behavioral intention.

Venkatesh et al. [11] deﬁned hedonic motivation as the fun or pleasure derived from
using technology. It also makes an individual feel better since it is a crucial factor in
consumer choice to purchase hybrid cars [49–51]. Thus, it was hypothesized that:

H3. Hedonic motivation has a signiﬁcant direct effect on behavioral intention.

According to Venkatesh et al. [11], performance expectancy (PE) is the degree of
personal belief that employing collaborative technology would increase work efﬁciency
and result in operational success. Additionally, if customers ﬁnd a simple system to be used,
it will be more accepted [52]. This could be a factor in encouraging people to purchase [53].
Thus, it was hypothesized that:

H4. Performance expectancy has a signiﬁcant direct effect on behavioral intention.

Effort Expectancy (EE) relates to the level of ease connected with the use of the
system. The deﬁnition of EE discusses the effort required to become skillful when utilizing
technology. This method is comparable to the idea of Davis [54] of perceived ease of use,
which addresses the extent to which people think utilizing technology does not involve
much effort [55]. Ombach [56] concluded that developed technologies are efﬁciently
integrated with several vehicles. Thus, it was hypothesized that:

H5. Effort expectancy has a signiﬁcant direct effect on behavioral intention.

Facilitating Conditions (FCs) are said to be the degree to which a person feels that a
technological and organizational infrastructure exists to enable the usage of the system [57].
FC affects people’s perception of infrastructures, technical support, and other facilities
when they utilize technology, products, and services. In the previous UTAUT models, FC
was theorized as an operator of user behavior. This means that users are more likely to
use new technology if there are available resources, expertise, and support [58]. Due to
this, national policy actions are required to promote the commercialization of low-carbon
technology (i.e., hybrid cars) in both advanced and especially developing nations like
the Philippines [53]. In addition, FC is presumed to be an essential variable inﬂuencing
behavioral intention in the UTAUT2 framework [11,59]. Thus, it was hypothesized that:

H6. Facilitating conditions has a signiﬁcant direct effect on behavioral intention.

A study by Wang et al. [8] revealed that the theory of planned behavior (TPB), together
with its primary constructs, was found to predict behavioral intentions accurately. Attitude
is characterized as the positive or negative evaluation of the adoption behavior. Social
inﬂuence or subjective norm refers to the perceived social pressure an individual feels from
others. Perceived behavioral control was deﬁned as the level of perceived ease or difﬁculty
with regard to engaging in the behavior. Hybrid electric vehicles have been regarded as
a potential solution to the pressure of lowering carbon emissions in the transportation

---

<!-- PAGE 7 -->

World Electr. Veh. J. 2023, 14, 227

7 of 26

industry—affecting consumers’ behavioral intentions on adopting hybrid cars. Tanwir and
Hamzah [7] integrated the theory of planned behavior with environmental knowledge
as the foundation of their research model to examine the factors inﬂuencing people’s
intention to buy a hybrid car. They found that people’s perceptions of their ability to
manage resources are the most signiﬁcant predictors of their intention to purchase hybrid
vehicles. Thus, it was hypothesized that:

H7. Subjective norm has a signiﬁcant direct effect on behavioral intentions.

H8. Attitude has a signiﬁcant direct effect on behavioral intentions.

H9. Perceived behavioral control has a signiﬁcant direct effect on behavioral intentions.

According to Lin et al. [60], the perceived environmental concerns (PENCs) latent vari-
able functions as the antecedent of the subjective norm (SN), attitude (AT), and perceived
behavioral control (PBC) variables in the PEPB model of German et al. [22]. Car emissions
raise quantities of carbon dioxide and other greenhouse gases while trapping the sun’s heat
in the Earth’s atmosphere, which causes global warming. In the year 2020, transportation
passenger cars contribute to around 41% of worldwide carbon emissions [1]. There is an
apparent need for alternatives or modiﬁcations that would better sustain the means of
transportation and automotive industry productions nationwide, such as developing an
electric car, but more open and accessible to the general public and more ethically priced,
particularly hybrid cars [61]. Racz et al. [62] conducted a study on the ecological perspective
of hybrid cars. Their results revealed that the modern concept of an eco-friendly car is a
strong start for a healthier environment, but at the same time, battery recycling requires
greater focus because the advantages of electric batteries are generally acknowledged,
while the drawbacks of recycling are frequently ignored. Thus, it was hypothesized that:

H10. Perceived environmental concerns have a signiﬁcant direct effect on subjective norm.

H11. Perceived environmental concern has a signiﬁcant direct effect on attitude.

H12. Perceived environmental concerns have a significant direct effect on perceived behavioral control.

To thoroughly examine the adoption potential of hybrid cars, the researchers estab-
lished the STPB model in accordance with the sustainability domains. The latent variable
perceived economic concerns (PECCs) was added. Barbosa Junior et al. [63] presented
the economic dimension of the ﬁnancial viability of providing production continuity with
economic resources obtained through sustainable practices. Their research identiﬁed three
barriers: low ﬁnancial return, ﬁnancial incentive, and ﬁnancial viability. Social factors
are strongly related to survey respondents’ adoption of sustainable practices. Similarly,
economic concerns or perceived economic concerns directly impact subjective norm and
attitude. Economic efﬁciency was used as an independent variable in a study by Saif
et al. [64] to predict the intention to adopt digital-only technology. It was deﬁned as cus-
tomers’ perceptions of being able to save time, effort, and ﬁnancial resources by using
the services. According to their ﬁndings, perceived convenience and perceived economic
efﬁciency have a signiﬁcant positive effect on the usage intention, which would sufﬁce the
signiﬁcant direct effect PECC has on perceived behavioral control. Thus, the following
were hypothesized:

H13. Perceived economic concerns have a signiﬁcant direct effect on subjective norm.

H14. Perceived economic concerns have a signiﬁcant direct effect on attitude.

H15. Perceived economic concerns have a signiﬁcant direct effect on perceived behavioral control.

In a study by German et al. [22] utilizing the pro-environmental theory of planned
behavior (PEPB) model, perceived authority support (PAS) refers to an individual’s per-
ception of any resources, regulations, processes, or actions delivered by a government
or authority organization that can assist people in carrying out a particular activity. The
Philippines’ policies and programs are aimed at preventing the depletion of environmental

---

<!-- PAGE 8 -->

World Electr. Veh. J. 2023, 14, 227

8 of 26

resources, which involves reducing energy use, chloroﬂuorocarbons, and carbon dioxide
emissions [65]. The government’s initiative to supervise the transition from fossil-fueled
cars to hybrid cars is expected to have an impact on consumers’ purchase intention toward
hybrid cars [66]. According to Lin et al. [60], support from the government has a posi-
tive and substantial effect on subjective norm, attitude, and perceived behavioral control,
demonstrating that the government has a signiﬁcant impact on its population. Thus, it was
hypothesized that:

H16. Perceived authority support has a signiﬁcant direct effect on subjective norm.

H17. Perceived authority support has a signiﬁcant direct effect on attitude.

H18. Perceived authority support has a signiﬁcant direct effect on perceived behavioral control.

3. Methodology
3.1. Participants

The researchers conducted an online survey to predict Filipinos’ purchasing intentions
for hybrid cars. Non-probability sampling methods were utilized to gather the respondents
for the study. According to Galloway [67], convenience sampling can help gather a variety
of attitudes and opinions as well as identify tentative ideas. That being so, the convenience
sampling method was used. Meanwhile, snowball sampling was also employed to reach
the targeted number of participants with the help of each one’s social network [68]. The
researchers obtained more than 500 respondents, generalizing the study’s results [69]. Since
the self-administered survey was open to the general public, the respondents answered
at their discretion. A total of 1149 responses were accumulated (Table 1), but 1048 was
the number of responses considered since 101 participants did not possess a driver’s
license—the instrument’s primary qualiﬁcation. This resulted in a 91.21% valid response
rate with no missing data—similar to the adopted data from Ong et al. [15].

Table 1. Respondents’ descriptive characteristics (n = 1048).

Characteristics

Gender

Age

Monthly Income/Salary

Occupation

Marital Status

Category

Female
Male

17–22
23–29
30–36
37–43
44–50
51–60

Less than 20,000
20,000–30,000
30,000–40,000
40,000–50,000
50,000–60,000
Greater than 60,000
Others

Employed
Self-employed
Unemployed
Retired
Student

Married
Single
Widowed
Separated

N

146
902

5
341
365
192
97
48

42
310
495
113
52
34
2

1035
8
1
0
4

553
487
4
4

%

13.9
86.1

0.48
32.54
34.83
18.32
9.26
4.58

4.01
29.58
47.23
10.78
4.96
3.24
0.19

98.76
0.76
0.1
0.0
0.38

52.77
46.47
0.38
0.38

---

<!-- PAGE 9 -->

World Electr. Veh. J. 2023, 14, 227

9 of 26

Table 1. Cont.

Characteristics

Category

Elementary graduate
Junior high school graduate
Senior high school graduate
Technical–Vocational Graduate
College Graduate
Master Graduate
PhD Graduate

Urban
Rural

Owned house and lot
Owned an apartment
Owned a condominium
Rental
Others

Yes
No

Educational Attainment

Residence

Type of Residential Home

Do you have car insurance?

3.2. Questionnaire

N

2
1
4
2
992
45
2

866
182

566
25
10
395
52

636
412

%

0.19
0.1
0.38
0.19
94.66
4.29
0.19

82.63
17.37

54.01
2.39
0.95
37.69
4.96

60.69
39.31

A questionnaire with 13 distinct portions and four items each was adapted from the
related literature [15]. Participants were asked to rate how much they agreed or disagreed
with the given statement on a 5-point Likert scale to gather information for this study.

Data preprocessing was performed prior to integrate the Machine Learning Algorithm
(MLA). SPSS 25 was utilized to examine the missing data. For the data cleaning process,
nonsigniﬁcant indicators with a p-value more signiﬁcant than 0.05 were removed from the
data using correlation analysis. Similarly, for the MLA optimization, only the indicators
with a value higher than 0.20 correlation coefﬁcient were considered. Since none of the
indications were removed, all proposed indicators were deemed signiﬁcant.

To represent the input for the MLA, the various indicators were averaged through data
aggregation. The implications in the questionnaire portray the latent factors that were un-
observed variables and were taken into account in this study for the MLA utilizing Python
3.8, speciﬁcally Spyder 3—an integrated development environment. Other algorithms,
such as the decision tree (DT), the random forest classiﬁer (RFC), and the deep learning
neural network (DLNN) were used after data normalization to predict the factors affecting
the acceptance of hybrid cars among Filipino drivers.

3.3. Decision Tree

A decision tree is a structure and classiﬁcation approach with regression capacity
applied as a prediction factor in a cluster of independent variables [70]. This structure is
labeled as a primary classiﬁer of decision nodes organized in a tree pattern [71]. They are
easily interpretable and visually portrayed as hierarchical structures [72]. Additionally,
decision trees are often employed in model classiﬁcation in data mining [73]. Milani
et al. [74] also stated that DT is widely recognized as one of the most effective methods
for dealing with nonlinear datasets. Since decision trees study a nonlinear dataset for
understanding human features and behavior [75], this approach can be applied to the
current study.

Based on the study of Topîrceanu and Grosseck [76], MLA recognizes decision trees as
one of its classiﬁcation tools. It categorizes relevant latent variables that impact a dependent
factor by evaluating the relationship between factors represented by tree branches. Their
study also stated that DTs are a predictive model for human behavior regardless of the
target variable’s quantity. Furthermore, DTs are utilized to develop a prediction model
for multiple class (dependent factor) labels in domains such as healthcare, human factors,
manufacturing, and other ﬁelds [77].

---

<!-- PAGE 10 -->

World Electr. Veh. J. 2023, 14, 227

10 of 26

In conjunction with establishing the Entropy and Gini index values alongside best and
random splitters, various testing and training ratios were applied to the DT classiﬁcation
process, such as the 40:60, 50:50, 60:40, 70:30, 80:20, and 90:10 training-to-testing ratios.
Following the study of Chen et al. [78] the tree depth was evaluated, spanning from four to
seven. The ideal decision tree was determined by running each combination 100 times for a
total of 9600 runs. The splitter (Random or Best), training and testing ratios, tree depth, and
the criterion (Gini or Entropy) were all determined using the analysis of variance (ANOVA)
to evaluate the ideal decision tree.

3.4. Random Forest Classiﬁer

The random forest classiﬁer is a supervised classiﬁcation algorithm that categorizes
data by creating several classiﬁers to attain greater prediction accuracy [79]. The basic
decision tree generates a large number of branches; therefore, RFC classiﬁes the most
satisfactory decision tree using several characteristics and creates the best branch split
among the decision trees [80]. The primary goal of employing the RFC as MLA is to locate
the best tree with a high accuracy rate. The random forest classiﬁer evaluates the best
tree for each iteration, whereas the standard DT generates a random tree for each run.
Chen et al. [81] supported the claim that the random forest classiﬁer is the best among
other decision trees. According to the study of Rodriguez-Galano et al. [82], RFCs are
far more accurate and resistant to noise than single classiﬁers (i.e., basic decision trees);
hence, ensemble learning algorithms like random forest, bagging, and boosting are gaining
popularity. In the paper of Elhenawy et al. [83] and Ermagun et al. [84], the RFC was used
to predict human behavior, speciﬁcally driving behavior. Thus, the same classiﬁcation tool
was applied in the current investigation. Similar optimization parameters were utilized in
the study, as presented in the DT sections.

3.5. Deep Learning Neural Network

Compared to other machine learning and artiﬁcial intelligence applications, the deep
learning neural network (DLNN) is recognized as the best model for predicting parameters
or identifying patterns because of its capacity to assess and calculate many perceptions [26].
Cassini [85] stated that this algorithm has signiﬁcant advantages over conventional machine
learning algorithms (MLAs) in extracting features at various levels of abstraction and
thereby learning more complex patterns. Furthermore, deep learning neural networks are
artiﬁcial neural networks with additional hidden layers between the input and output
layers, wherein Ong et al. [26] explained how these can assess nonlinear relationships
among frameworks developed. According to Sturman et al. [86], the variation between and
among human annotators is eliminated by the deep neural network, which outperforms
commercial systems at a lower cost and contributes to the enhancement of behavioral data
quality and accuracy. Luceri et al. [87] afﬁrmed that the deep learning neural network
effectively evaluates the psychological behavior, behavioral intention, and psychology of
consumers. In this study, the results obtained from the random forest classiﬁer would be
supported by use of the deep learning neural network since this method can predict and
categorize the most inﬂuential factors affecting the behavioral intention of consumers in
purchasing hybrid cars.

Similar to the set conditions with a random forest classiﬁer, the deep learning neural
network preprocessing incorporated correlation analysis for data cleaning. Following
data normalization, various activation functions for the hidden layer (sigmoid, tanh, and
swish), output layer (sigmoid), and optimizer (Adam, SGD, RMSProp) were taken into
consideration [80]. Additionally, the number of nodes for the 80:20 training and testing
ratio was also included using a feed-forward neural network process. A total of 6480 runs
were conducted, set with 150 epochs per iteration [88].

---

<!-- PAGE 11 -->

World Electr. Veh. J. 2023, 14, 227

11 of 26

4. Results
4.1. Decision Tree

Iterations of the different combinations of parameters in the basic decision tree were
accomplished to generate the best output. Presented in Table 2 are the summarized results.
It could be posited that at depth 5, the most consistent tree output based on standard
deviation was produced with Gini and best as splitter and criterion. Though entropy and
best had higher accuracy rates, a signiﬁcant difference was not evident. In addition, the
accuracy rates under Gini and best had higher accuracy rates.

Table 2. Decision Tree Summarized Results.

Category

60:40

70:30

80:20

90:10

Gini
Standard Deviation

Entropy
Standard Deviation

Gini
Standard Deviation

Entropy
Standard Deviation

Random

Best

65.54
2.051

65.42
1.962

70.18
0.389

67.00
0.000

67.16
2.214

67.00
2.168

68.15
0.642

69.49
0.503

65.16
2.344

65.29
2.384

67.06
0.639

68.00
0.000

67.20
3.117

67.61
3.512

72.00
0.000

72.32
0.471

The study of German et al. [22] presented that these low accuracy rates from the basic
decision tree were due to the fact that it generates random trees every iteration. It was
proposed that a random forest classiﬁer be used. In this case, the random forest classiﬁer
ﬁnds the best tree output every iteration, which in turn considers a higher accuracy rate.
Studies such as that of Ong [80] and Chen et al. [81] presented the same discussion and
justiﬁed how the random forest classiﬁer can present the optimum tree output.

4.2. Random Forest Classiﬁer

Presented in Table 3 are the summarized results of the random forest classiﬁer. Fol-
lowing related studies [22,80,81], higher accuracy rates were evident in the random forest
classiﬁer output compared to the basic decision tree. Similar to the basic decision tree,
depth 5 presented the most consistent output with Gini and best as the parameters.

Table 3. Random Forest Classiﬁer Summarized Results.

Category

60:40

70:30

80:20

90:10

Gini
Standard Deviation

Entropy
Standard Deviation

Gini
Standard Deviation

Entropy
Standard Deviation

Random

81.82
4.896

82.85
3.300

88.74
0.7115

83.63
1.120

Best

80.69
3.668

80.36
3.976

84.06
1.003

84.98
0.642

83.22
5.904

84.43
5.028

92.55
0.500

89.37
1.077

85.38
4.582

83.69
6.238

94.00
0.000

92.00
0.000

---

<!-- PAGE 12 -->

World Electr. Veh. J. 2023, 14, 227

12 of 26

It could be seen from the results that the 90:10 training testing ratio produced the most
consistent tree with 94% accuracy and a standard deviation value of 0.000. Thus, this tree
output was considered the optimum classiﬁcation model. Figure 2 represents the optimum
tree with a random forest classiﬁer.

Figure 2. Optimum Tree with Random Forest Classiﬁer.

From the output, PENC (X1) dictated the behavioral intentions for acceptance of
hybrid cars. The tree will consider AT (X0) for the ﬁrst node. Then, it will consider X0,
X1 (≤−0.412), and PBC (X2) with a value less than or equal to −0.909. Satisfying this
condition, people will have very high behavioral intentions. If the X1 (≤−0.412) condition
is not satisﬁed, only a high behavioral intention is seen. This indicates that PENC should
be highlighted for people to have a very high or positive behavioral intention. A similar
output is evident if the ﬁrst child node conditions are not satisﬁed.

If the parent node with a value less than or equal to 0.386 is not satisﬁed,
a 0.123 condition for X0 ﬁrst child node is considered. Satisfying this will consider X1
and then PE (X4) with a value less than or equal to −0.043, which will lead to a high
behavioral intention. This posits that as PENC is inﬂuential to the control of an individual
to accept hybrid cars, its performance should also be highlighted as utilization for trans-
portation. Lastly, if the child node conditions are not satisﬁed, it will consider X2, then X1,
and X0, which will lead to very high behavioral intentions.

From the ﬁndings, it could be deduced that PENC and AT are the top signiﬁcant factors
that affected people’s PBC and PE to have very high behavioral intentions for hybrid cars.
This dictates that PBC and PE are signiﬁcant factors as well that would inﬂuence users’
acceptance of hybrid cars. However, with varied factors still present, the random forest
classiﬁer needs further assistance from other MLAs to provide a distinct classiﬁcation of
latent variables affecting behavioral intentions. Chen et al. [81] considered other tools in
support of the ﬁndings of the random forest classiﬁer to deduce signiﬁcant latent variables.

4.3. Deep Learning Neural Network

Following the study of Ong et al. [75], deep learning neural network parameter
optimization was conducted to provide the optimum classiﬁcation model. From the
different parameters tested, tanh, as the activation function for the different hidden layers,
presented the best output. Using sigmoid as the activation function in the output layer and
adam as the optimizer, the summarized training and testing average results are presented
in Table 4.

---

<!-- PAGE 13 -->

World Electr. Veh. J. 2023, 14, 227

13 of 26

Factor

PENC
AT
PBC
SN
PE
PAS
FC
HM
EE
PECC
PV
HB

Table 4. Summarized results for deep learning neural network.

Average Training

Standard Deviation

Average Testing

Standard Deviation

91.41
90.71
80.95
80.70
81.12
80.01
77.21
74.72
67.80
68.67
65.78
60.50

1.630
0.928
1.663
0.143
1.071
7.850
1.473
0.800
2.769
3.343
7.093
2.211

93.14
93.06
89.84
87.29
83.14
80.62
79.14
77.29
75.76
70.35
70.43
68.52

1.681
1.807
2.631
2.997
2.285
1.943
2.491
2.860
1.993
1.226
3.210
3.761

Tanh is an activation function that is considered to be an extension of the sigmoid
function. Gudivada [89] explained that a stretched and shifted sigmoid calculation is seen in
the tanh activation function. This is usually considered for nonlinear relationship models,
which can present high accuracy rates when used in the hidden layers. As explained
by Walrave et al. [90], tanh is an activation function with stronger complexity to update
weights in neural network models, which results in faster optimization and higher accuracy
rates. The equation of tanh is presented in Equation (1) adopted from de Ryck et al. [91].

tanh(x) =

2
1 + e−2x

− 1

(1)

For sigmoid, Costarelli [92] explained that this activation function is mostly utilized
in the output layer as it calculates nonlinear relationships with smaller ranges. Since
tanh was considered with several hidden layers in this study, bounded values would be
evident after the process, which can be computed using sigmoid [93]. It is also argued to
be efﬁcient despite its simple calculation, which is commonly utilized when probabilities
are considered. Equation (2) represents the sigmoid activation function adopted from
Narayan [94].

sigmoid(x) =

1
1 + e−x

(2)

The ﬁnal deep learning neural network classiﬁcation model is presented in Figure 3. A
total of three hidden layers with 50, 50, and 20 nodes, respectively, provided the optimum
model. With a 96.60% accuracy, the score of importance using SPSS 25 was used to verify the
output of consecutive ranking of factors affecting the acceptance of hybrid cars. Presented
in Table 5 is the normalized score of the importance of the resulting parameters.

Table 5. Normalized scores of importance.

Factor

PENC
AT
PBC
SN
PE
PAS
FC
HM
EE
PECC
PV
HB

Importance

Normalized Importance

0.107
0.103
0.101
0.099
0.097
0.090
0.087
0.084
0.083
0.082
0.081
0.076

100%
96.32%
94.50%
92.12%
90.20%
84.50%
81.20%
79.00%
77.60%
76.70%
76.20%
70.90%

---

<!-- PAGE 14 -->

World Electr. Veh. J. 2023, 14, 227

14 of 26

Figure 3. Deep learning neural network model.

4.4. Validation

To validate the different MLA accuracy outputs, a Taylor Diagram was generated.
Following the study of German et al. [22] and Ong [23], the root mean square error should
be within 20% and the accepted correlation value at 90% for signiﬁcant factors. Setting the
threshold of 1.00 for the standard deviation, Figure 4 represents the Taylor Diagram for this
study. It could be seen that the output of different MLAs used in this study is acceptable.
Moreover, the basic decision tree cannot be utilized due to the low output at 0. In addition,
the least signiﬁcant factors, such as HM, EE, PECC, PV, and HB, can still be considered but
are less inﬂuential latent variables.

Figure 4. Taylor Diagram.

---

<!-- PAGE 15 -->

World Electr. Veh. J. 2023, 14, 227

15 of 26

5. Discussion

Hybrid cars promote sustainable transportation, which is essential for both techno-
logical advancement and reducing carbon emissions; therefore, it is crucial to study the
role of behavioral intention in determining how Filipino drivers adapt and transition to
eco-friendly vehicles. The study aimed to examine the factors inﬂuencing Filipinos’ accep-
tance or purchasing intentions toward hybrid cars using the Pro-environmental Theory
of Planned Behavior (PEPB) and Sustainability Domains. These were combined into the
Sustainability Theory of Planned Behavior, along with the integrated the Uniﬁed Theory
of Acceptance and the Use of Technology 2 (UTAUT2). From the results, both the random
forest classiﬁer (RFC) and the deep learning neural network (DLNN) were utilized to
evaluate the different signiﬁcant factors affecting purchasing intentions of hybrid cars.

This study was able to justify the limitations of SEM as discussed by related
studies [23–25]. As seen, PENC was deemed to be the most important latent variable,
followed by AT, PBC, SN, and PE. Compared to the SEM result [15], it was seen that these
were ranked ﬁfth, third, seventh, second, and fourth, respectively. Clear distinctions were
seen within the indirect effects among sustainability domains, which were mediated by the
TPB domains. From the current study, PENC was deemed highly signiﬁcant, while PAS
ranked sixth, and PECC ranked tenth–compared to its SEM counterpart results being ﬁfth,
third, and ﬁrst, respectively. Since the presence of mediating factors are seen among the
STPB model, the justiﬁcation of hindrance among mediating factors played a role [23–25].
In addition, the MLA results proved that the FC, EE, and HB were signiﬁcant while
the SEM results deemed them insigniﬁcant. As explained by Li et al. [95] who compared
the SEM with the MLA, it was presented that the MLA has more predictive capabilities,
generated higher accuracy rates, and could better present the model output rather than
the ﬁnal model SEM considers. It was added that the MLA can provide better explanation
of the model based on the mutual understanding of machines and humans. Hadiyat [96]
also provided the same justiﬁcation. However, not all output may be different like that
of Ong et al. [75] when analyzing telemedicine acceptance in the Philippines where both
the SEM and the ANN provided the same output. Their explanation in the paper was that
their study only utilized a direct relationship from the UTAUT2. Thus, this small model
compared to the current study has distinct differences. Summarized in Table 6 are the
different ranked scores of the latent variables. The discussion of the succeeding section is
based on the highest signiﬁcant effect from MLA.

Table 6. MLA versus SEM Results.

Latent Variable

PENC

AT

PBC

SN

PE

PAS

FC

HM

EE

PECC

PV

HB

MLA

1st

2nd

3rd

4th

5th

6th

7th

8th

9th

10th

11th

12th

SEM

5th

3rd

7th

2nd

4th

3rd

Insigniﬁcant

6th

Insigniﬁcant

1st

8th

insigniﬁcant

---

<!-- PAGE 16 -->

World Electr. Veh. J. 2023, 14, 227

16 of 26

From the ﬁndings, the highest contributing factor to consumer acceptance was the
perceived environmental concern (PENC) (100%) latent, having a signiﬁcant direct effect on
subjective norm (SN), attitude (AT), and perceived behavioral control (PBC). Based on the
indicators, Filipino drivers or general respondents recognized that humankind is severely
abusing and polluting the environment, causing them to be worried about its future status
and avoiding more disastrous consequences. They felt compelled to adopt more ecologi-
cally friendly products, such as hybrid cars, which are both handy and beneﬁcial to the
existing environmental conditions. Rossi and Rivetti [97] mentioned that younger people,
notably millennials and post-millennials (ages 23–29 and 30–36), are more concerned with
sustainability, have a collective purchasing power, and are becoming an increasingly crucial
consumer demographic. Because they are more inclined to environmental activism and en-
gaging through platforms where these eco-labeled items and ideologies are promoted—in
this study, obtaining hybrid cars—millennials are more likely to utilize eco-friendly man-
ufactured products [98]. Thus, it could be deduced that hybrid cars could be viable as a
highly efﬁcient form of transportation due to their positive environmental effects.

Attitude (AT) (96.32%) was also deemed to have a highly signiﬁcant direct effect
on behavioral intention (BI). This shows that the positive or negative evaluation of the
adoption behavior of hybrid cars will particularly inﬂuence a person’s intention to purchase
them. Respondents were more likely to believe that purchasing a hybrid car is a wise and
pleasant decision, and they trusted the notion of purchasing a hybrid car since learning
to utilize it may be a fulﬁlling experience. In addition, this ﬁnding is substantiated by
the study of Chen et al. [78], which proves how products that may make customers feel
joyful, thrilled, or cheerful can lead to more acceptance and a higher loyalty attitude. In
addition, the study of Nadlifatin et al. [99] validated the correlation between AT and BI
as the greatest value among all correlation results regarding the use of eco-label products.
Therefore, these can be obtained through the associated emotional and known sustainable
beneﬁts that green products actively elicit. In accordance, PBC and PE were proved to have
a highly signiﬁcant and direct effect on BI.

PBC (94.50%) and PE (90.20%) were shown to have a highly signiﬁcant and direct
effect on BI. Although lower than that of the AT latent, it suggests that drivers can still sense
the ease of operation of a hybrid car compared to a conventional vehicle and that it comes
with more excellent resources and opportunities or anticipation that it is less vulnerable to
impediments [100]. This ﬁnding was supported by Cahigas et al. [101], which found that
PBC signiﬁcantly and positively affected the intention to use in the transportation setting.
Based on the two sets of indicators, it is up to the consumer’s discretion to conﬁdently
select a hybrid car for his/her future purchase by determining that driving a hybrid car
would be safer, more comfortable, and more productive. Furthermore, PE has been proven
by Chong et al. [102] to have a strong, positive association with behavioral intention in
adopting new technology, similar to the study conducted by Foroughi et al. [103] in the area
of autonomous transportation. These are vital aspects, especially when a high percentage of
respondents were working individuals who require efﬁciency in transportation and fewer
hindrances in using a different type of vehicle.

Concerning the signiﬁcant factors, SN (92.12%) latent had a signiﬁcant direct effect
on BI. Filipinos believed that the people they trusted who inﬂuenced and had a good
impression on them would also recommend that they purchase or use a hybrid car. Similarly,
it was indicated that hybrid cars would come off as more prestigious than traditional fossil-
fueled vehicles. This result aligned with a study by Yang [104], wherein consumers’ buying
intentions were impacted by peer trust and reciprocity. They were eager to take advice and
suggestions from trustworthy peers. Consequently, the moderate inﬂuence SI has on BI may
be because only the experience of social interactions that have created close relationships
among peers would impact customers’ buying intentions more signiﬁcantly [10,101].

Along with SN, perceived authority support (PAS) (84.50%) had a signiﬁcant direct
effect on SN, AT, and PBC. The indicators reveal that the government is active in setting up
facilities for hybrid cars, enacts regulations that allow Filipinos to use these vehicles, and

---

<!-- PAGE 17 -->

World Electr. Veh. J. 2023, 14, 227

17 of 26

encourages or endorses the usage of them through these same regulations. Although the
Philippine Statistics Authority [65] has acknowledged that there are policies and programs
in place to enable the acquisition and handling of hybrid vehicles, they still need to be
promoted on par with conventional vehicles in the market. A study by Yazdanpanah and
Hadji Hosseinlou [105] suggested that policymakers seek to modify habits by providing
relevant information to enhance the intention-behavior relationship. With that, there is
a need for eco-labeled cars in the country, which is gradually being addressed by the
authorities. Especially in the Philippines, the government is taking small steps, such as
setting up some places for charging electric cars. However, the promotion of the usage is
still underrepresented in the country.

Facilitating conditions (FCs) (81.20%) also proved to be a signiﬁcant factor affecting BI.
The indicators delineated that Filipino drivers have the necessary resources to operate a
hybrid car, are knowledgeable in driving, and can ask questions and ﬁnd solutions if any
problems are identiﬁed. This ﬁnding is similar to the study of Lallmahomed et al. [106],
wherein they presented how FC signiﬁcantly affects usage intention. Yuduang et al. [28]
also mentioned how consumers prefer using applications that are beneﬁcial and easily
accessible. The resources that are accessible for continuous usage of new technologies, such
as hybrid cars, are considered by the current generation. Hedonic motivation (HM) (79%)
was also seen to be a signiﬁcant factor affecting BI. Based on the indicators, using a hybrid
car is more fun, entertaining, enjoyable, and satisfying than driving a fossil-fueled car. It
has been demonstrated that hedonic motivation, deﬁned as the enjoyment or pleasure
consumers derive from adopting new technology, is crucial in inﬂuencing technology
acceptance and use [107]. The results of the analysis of the hedonic motivation construct
were in line with the results of previous studies by Venkatesh et al. [11] and Palau-Saumell
et al. [108], as both their results substantiated the fact that hedonic motivation is a signiﬁcant
predictor of intention to use.

Effort expectancy (EE) (77.60%) also proved to be a signiﬁcant factor affecting BI. The
indicators that led to the importance were that hybrid cars provide clear and understandable
interactions that are easy to operate, adapt, and adept. This result is quite similar to the
ﬁndings of Nordhoff et al. [12]: since EE is a substantial positive predictor of behavioral
intention, individuals who imply that using conditionally autonomous cars is simple
are more likely to want to utilize them. Aligned with this, perceived economic concern
(PECC) (76.70%) was also proved to be a signiﬁcant factor affecting BI, SN, AT, and PBC.
The study found that hybrid cars have good warranties and economic incentives, can
generate more savings which improve an individual’s economic standing in the long run,
drive more efﬁciently, and are easily acquirable in the market. This added latent, which
completes the sustainability theory of planned behavior (STPB), is related to an individual’s
voluntary involvement, comprehensive societal and commercial consideration, and sense
of social responsibility.

This is supported by the study of Saif et al. [64], which proved that consumers’ inten-
tion to adopt has a positive relationship with perceived economic efﬁciency. According to
their ﬁndings, practitioners should provide clients with ﬁnancial beneﬁts, such as charge-
free, new, or unique services, and competitive prices, to further promote user acceptance.
It has been established by Lane and Potter [109] that economic instruments point to a
strategy of promoting the use of cleaner fuels and vehicles through the use of ﬁnancial
incentives, an approach based on the concept of ecological taxation reform. This indicates
substantial evidence that economic factors can effectively encourage cleaner options such
as hybrid cars.

Interestingly, despite the positive remarks of the latent price value (PV) (76.20%)
indicators that hybrid cars are reasonably priced, good value for money, and a valuable
purchase, it was still considered the second least signiﬁcant factor affecting BI. Chaveesuk
et al. [110] explained that price value, which is deﬁned as consumers’ cognitive trade-offs
between the perceived costs and beneﬁts of adopting a speciﬁc system, has a signiﬁcant
direct effect on behavioral intention. Concerning the demographic factors, most of the

---

<!-- PAGE 18 -->

World Electr. Veh. J. 2023, 14, 227

18 of 26

respondents have a monthly salary of 20,000 pesos to 50,000 pesos which means that they
belong to the lower middle class to the middle class as stated on the indicative range
of monthly family income in the study of Albert et al. [111]. However, consumers may
purchase or are willing to invest in hybrid cars instead of fossil-fueled cars, regardless of the
added amount, since they are considered cost-effective. This study ﬁgured that consumers
are willing to pay the extra amount for the efﬁciency, environmental, and economic beneﬁts
that hybrid cars offer.

The least signiﬁcant out of all the latent affecting behavioral intention was Habit
(HB) (70.90%). Based on the indicators, using a hybrid car became a habit, an addiction
for which consumers are willing to pay more, and serves as a daily utility. The utility of
hybrid cars remains unrecognized and unfamiliar to many since the Philippine market
for hybrid cars is currently sparse, which is why HB has not been established and is the
least signiﬁcant factor. Similarly, Nordfjaern et al. [112] discovered that the car habit factor
negatively predicts intention and is not as signiﬁcant as other behavioral factors. It was
found that to predict better user intention, user personality traits must be assessed in
line with TPB domains. As a result, consumers still need to develop the habit of using
this mode of transportation. Eventually, it is expected that habit will soon develop if the
hybrid car market in the Philippines becomes saturated, building strong familiarity with
Filipino drivers.

To better provide insights among readers, Table 7 lists all the abbreviations used

throughout the study.

Table 7. List of abbreviations used throughout the paper.

Abbreviations

ANN

AT

BI

DLNN

DT

HB

HM

HV

IDT

MLA

MM

NAM

PE

PECC

PEPB

PENC

PV

RFC

SE

SI

SN

SQ

EE

Meaning

Artiﬁcial Neural Network

Attitude

Behavioral Intentions

Deep Learning Neural Network

Decision Tree

Habit

Hedonic Motivation

Hybrid Vehicle

Innovation Diffusion Theory

Machine Learning Algorithm

Motivational Model

Norm Activation Model

Performance Expectancy

Perceived Economic Concern

Pro-Environmental Theory of Planned Behavior

Perceived Environmental Concern

Price Value

Random Forest Classiﬁer

Self-Efﬁcacy

Social Inﬂuence

Subjective Norm

Service Quality

Effort Expectancy

---

<!-- PAGE 19 -->

World Electr. Veh. J. 2023, 14, 227

19 of 26

Table 7. Cont.

Abbreviations

Meaning

FC

PAS

STPB

TAM

TPB

Facilitating Conditions

Perceived Authority Support

Sustainability Theory of Planned Behavior

Technology Acceptance Model

Theory of Planned Behavior

UTAUT2

Uniﬁed Theory of Acceptance and Use of Technology

5.1. Theoretical Contributions

According to the study by Agaton et al. [113], air pollution and greenhouse gas emis-
sions from the combustion of fossil fuels are one of the main drivers of why governments
and regions seek more sustainable means of transportation. With that, PEPB was used to
analyze the environmental impact on consumers’ behavioral intention and supports the
other latent variables of the sustainability domains [22]. Alongside the PEPB framework,
the sustainability domains, such as social, environmental, and economic, were considered,
while the UTAUT2 addressed the technological aspect. In the study of Yuriev et al. [114],
the TPB, or the theory of planned behavior, is the most extensively used model in studying
individuals’ behavior and is stated to encompass all environmental behavior variables.
However, it lacks the necessary sustainability latent construct [102,115].

In measuring the acceptance entirely or holistically, the frameworks mentioned above
were combined with integrating the economic aspect into the proposed sustainability theory
of planned behavior (STPB). It can be applied when evaluating the current generation’s
behavioral intention and acceptance of newly emerging or current smart technologies such
as the hybrid car. According to the study of Zadjafar and Gholamian [116], consumers
nowadays are more conscious of obtaining and purchasing sustainable products. In this
case, it was suggested that manufacturers and industries focus more on developing and
selling products that attest to the demand of green consumers. Since all the factors in
the study were proven signiﬁcant, the developed framework could be used by future
researchers to measure not only the behavioral aspect but also the sustainability aspect of
an individual utilizing the STPB.

5.2. Practical and Managerial Implications

The ﬁndings of this study have demonstrated the importance of predicting consumers’
acceptance of hybrid cars in the Philippines. Filipino drivers tend to consider hybrid cars
when aware of the environmental and economic beneﬁts. The result of the study proved
that it is essential for the younger generation to adapt to a more sustainable lifestyle, with
the high demand for greener transportation. Given that there is currently a limited market
for hybrid cars in the Philippines, consumers are still unaware of the utility of these vehicles.
Fortunately, this condition might improve with increased government reinforcement by
adopting incentives to promote their utility. Hybrid cars cost more than fossil-fueled
cars, which makes the marketing aspect challenging. In line with this, car companies
and manufacturers can also use the result of this study as a framework for designing and
implementing programs, strategies, and advertisements to propagate the marketability and
utility of hybrid cars. It is suggested that car companies should consider millennials as the
primary target for eco-friendly manufactured products such as hybrid cars, as projected in
the study’s demographic results. The advertisement and strategies may revolve around
sustainability, target generation, and the development and usage of hybrid cars to engage
purchasing intentions. Lastly, considering the technological aspect, companies can also
disseminate information about the ecological and economic advantages of hybrid cars
through social media platforms and in-app advertisements such as Facebook and YouTube
ads that can be capitalized by marketing ﬁrms.

---

<!-- PAGE 20 -->

World Electr. Veh. J. 2023, 14, 227

20 of 26

5.3. Limitations

Although there are positive ﬁndings in this study, there are also several limitations
to be noted. First, due to the adapted questionnaire, there were limited constructs. The
instrument was a self-administered online survey, which presents a constraint in terms
of the modality of the dissemination and follows the second point, the consideration of
the respondents. Having more constructs and items of measure may develop response
efﬁciency. In addition, considering interviewers may identify drivers for purchasing hybrid
cars among residents in the Philippines that other studies may consider.

Second, the primary criteria of a driver’s license and the modality narrowed the
respondents to those drivers who were active on social media. It is recommended that
the data collection be more diversiﬁed and not be inclined to only a particular generation,
speciﬁcally the millennials. A balance of each variation would emerge if the study could
expound on other generations, such as Generation Z or baby boomers, and would also
make studying the acceptance of each generation toward hybrid cars possible. It would
be more profound to gather more respondents outside the current study’s sample, such as
public utility vehicles or public utility jeepney drivers, separately to reassess the different
perspectives, behavior, and experiences of drivers toward hybrid cars.

Third, it is suggested that the study conduct interviews with these individuals to
provide a qualitative and quantitative analysis of those who intend to purchase hybrid
cars. Allowing the study to have a qualitative aspect would provide more ﬂexibility. The
insights from the interview results may be considered for additional latent variables and
items of measure, even presenting a qualitative-quantitative study.

Fourth, this study only considered two machine learning algorithms: the random forest
classiﬁer and the deep learning neural network. To maximize the utility of related analysis
techniques, other machine learning algorithm tools such as the Naïve Bayes classiﬁer,
K-Nearest neighbor, vector machine, or even C-Means clustering may be incorporated to
capture different areas of the result and identify factors based on probability and similarities
aside from the individual ﬁndings found in this study. Lastly, other tools such as K-Means
clustering could be utilized after gathering respondents from different generations to assess
the demographic characteristics of drivers who intend to purchase hybrid cars from the
lowest to the highest valued customers, which would allow the researchers to formulate
strategies with the market to support the economic aspect further. Simultaneous analysis
of the various factors may be reanalyzed using multivariate analysis tools to justify the
study’s ﬁndings since the indirect effect found on each latent may provide a signiﬁcant
relationship among the factors considered when it comes to the behavioral, sustainable,
and technological aspects of consumers’ purchasing intentions toward hybrid cars.

6. Conclusions

There are not enough studies on the purchasing intentions regarding hybrid cars
in developing countries like the Philippines. This necessitated the formulation of the
Sustainability Theory of Planned Behavior (STPB). The framework was constructed using
the Pro-environmental Theory of Planned Behavior (PEPB) and sustainability domains, as
well as integration of the Uniﬁed Theory of Acceptance and Use of Technology 2 (UTAUT2)
to predict the adoption of hybrid cars in the country. It was utilized to fully assess the
acceptance of smart and green technology, emphasizing sustainability—a vital aspect when
addressing climate change. A total of 1048 participants completed the self-administered
survey, disseminated using non-probability sampling methods, including convenience and
snowball sampling.

This study utilized a Machine Learning Algorithm (MLA) ensemble comprising a
Decision Tree (DT), Random Forest Classiﬁer (RFC), and Deep Learning Neural Network
(DLNN), which proved that PENC, AT, PBC, and PE were the most inﬂuential factors that
signiﬁcantly affect user acceptance of hybrid cars in the Philippines. This implies that MLA
is advantageous in analyzing the antecedents of human behavior, particularly sustainability
behavior. Comparing the results of both SEM and MLA, this study identiﬁed that MLA

---

<!-- PAGE 21 -->

World Electr. Veh. J. 2023, 14, 227

21 of 26

provided better and more accurate results since this study was able to consider an expanded
and large framework for analysis. However, based on other studies, a smaller model may
provide similar output. Therefore, this study concludes that using MLA may be applicable
and better suited for analyzing nonlinear relationships among large and extended models.
Moreover, it should be noted that this study was not able to guarantee that it represents an
unbiased cross section of the target audience since a convenience sampling approach was
used due to the limitations discussed. In addition, this study only focused on those who
are capable and have drivers’ licenses. This means that the output may be biased in the
aspect of capable purchasers.

From this study output, perceived environmental concerns have the highest signiﬁcant
direct effect on behavioral intention, suggesting that the environmental beneﬁts that come
with utilizing green technology increase Filipino drivers’ tendency to purchase hybrid
cars. It is recommended that car companies consider the study’s results and demographics
in propagating the marketability of hybrid cars. Other researchers could use the STPB
framework established by the study’s constructs and model to contextualize and emphasize
technological sustainability, which further validates the objectives of the United Nations’
Sustainable Development Goals (SDGs) to expedite the decarbonization of the overall
market and the entire economy.

Author Contributions: Conceptualization, R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C., R.A.V.J. and
J.D.G.; methodology, R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C. and R.A.V.J.; software, R.D.B.,
A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C. and R.A.V.J.; validation, R.D.B., A.K.S.O. and J.D.G.; formal
analysis, R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C., R.A.V.J. and J.D.G.; investigation, R.D.B.,
A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C. and R.A.V.J.; resources, R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C.
and R.A.V.J.; data curation, A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C. and R.A.V.J.; writing—original draft
preparation, R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C. and R.A.V.J.; writing—review and editing,
R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C., R.A.V.J. and J.D.G.; visualization, R.D.B., A.K.S.O. and
J.D.G.; supervision, R.D.B., A.K.S.O. and J.D.G.; project administration, R.D.B., A.K.S.O. and J.D.G.;
funding acquisition, R.D.B., A.K.S.O. and J.D.G. All authors have read and agreed to the published
version of the manuscript.

Funding: This research was funded by Mapua University Directed Research for Innovation and
Value Enhancement (DRIVE).

Institutional Review Board Statement: This study was approved by Mapua University Research
Ethics Committees (FM-RC-23-01-13).

Informed Consent Statement: Informed consent was obtained from all subjects involved in this
study (FM-RC-23-02-13).

Data Availability Statement: The data presented in this study are available on request from the
corresponding author.

Acknowledgments: The authors would like to thank all the respondents who answered our online
questionnaire. We would also like to thank our friends for their contributions to the distribution of
the questionnaire.

Conﬂicts of Interest: The authors declare no conﬂict of interest.

References

1.

Tiseo, I. Global Transport CO2 Emissions Breakdown; Statista: Singapore, 2021; Available online: https://www.statista.com/
statistics/1185535/transport-carbon-dioxide-emissions-breakdown/ (accessed on 31 May 2023).

4.

2. Wasiak, A.L. Modeling the Effects of Implementation of Alternative Ways of Vehicle Powering. Fuels 2021, 2, 487–500. [CrossRef]
United Nations. The 17 Goals|Sustainable Development. 2015. Available online: https://sdgs.un.org/goals (accessed on
3.
2 January 2023).
Irawan, M.Z.; Belgiawan, P.F.; Widyaparaga, A.; Deendarlianto; Budiman, A.; Muthohar, I.; Sopha, B.M. A market share analysis
for hybrid cars in Indonesia. Case Stud. Transp. Policy 2018, 6, 336–341. [CrossRef]
Ong, A.K.S.; Cleofas, M.A.; Prasetyo, Y.T.; Chuenyindee, T.; Young, M.N.; Diaz, J.F.T.; Nadlifatin, R.; Redi, A.A.N.P. Consumer
behavior in clothing industry and its relationship with open innovation dynamics during the COVID-19 pandemic. J. Open Innov.
Technol. Mark. Complex. 2021, 7, 211. [CrossRef]

5.

---

<!-- PAGE 22 -->

World Electr. Veh. J. 2023, 14, 227

22 of 26

6.

7.

Vabø, M.; Hansen, H. Purchase intentions for Domestic Food: A moderated tpb-explanation. Br. Food J. 2016, 118, 2372–2387.
[CrossRef]
Tanwir, N.S.; Hamzah, M.I. Predicting purchase intention of hybrid electric vehicles: Evidence from an emerging economy. World
Electr. Veh. J. 2020, 11, 35. [CrossRef]

8. Wang, S.; Fan, J.; Zhao, D.; Yang, S.; Fu, Y. Predicting consumers’ intention to adopt hybrid electric vehicles: Using an extended

9.

version of the theory of planned behavior model. Transportation 2016, 43, 123–143. [CrossRef]
Javid, M.A.; Abdullah, M.; Ali, N.; Shah, S.A.H.; Joyklad, P.; Hussain, Q.; Chaiyasarn, K. Extracting travelers’ preferences toward
electric vehicles using the theory of planned behavior in Lahore, Pakistan. Sustainability 2022, 14, 1909. [CrossRef]

10. German, J.D.; Ong, A.K.S.; Perwira Redi, A.A.N.; Robas, K.P.E. Predicting factors affecting the intention to use a 3PL during the

COVID-19 pandemic: A machine learning ensemble approach. Heliyon 2022, 8, e11382. [CrossRef]

11. Venkatesh, V.; Thong, J.Y.L.; Xu, X. Consumer acceptance and use of information technology: Extending the uniﬁed theory of

acceptance and use of Technology. MIS Q. 2012, 36, 157. [CrossRef]

12. Nordhoff, S.; Louw, T.; Innamaa, S.; Lehtonen, E.; Beuster, A.; Torrao, G.; Bjorvatn, A.; Kessel, T.; Malin, F.; Happee, R.; et al. Using
the UTAUT2 model to explain public acceptance of conditionally automated (L3) cars: A questionnaire study among 9118 car
drivers from eight European countries. Transp. Res. Part F Trafﬁc Psychol. Behav. 2020, 74, 280–297. [CrossRef]

13. Prasetyo, Y.T.; Vallespin, B.E.P. Determining factors affecting the acceptance of grab application in the Philippines using UTAUT2
approach. In Proceedings of the 2021 IEEE 8th International Conference on Industrial Engineering and Applications (ICIEA),
Chengdu, China, 23–26 April 2021. [CrossRef]

14. Khazaei, H.; Tareq, M.A. Moderating effects of personal innovativeness and driving experience on factors inﬂuencing adoption of

BEVs in Malaysia: An integrated sem–BSEM approach. Heliyon 2021, 7, e08072. [CrossRef]

15. Ong, A.K.S.; German, J.D.; Redi, A.A.N.P.; Cordova, L.N.Z.; Longanilla, F.A.B.; Caprecho, N.L.; Javier, R.A.V. Antecedents of
behavioral intentions for purchasing hybrid cars using sustainability theory of planned behavior integrated with UTAUT2.
Sustainability 2023, 15, 7657. [CrossRef]

16. Land Transportation Ofﬁce. Annual Report 2020; Land Transportation Ofﬁce—Department of Transportation: Philippines, 2021;
Available online: https://eb-production-media.s3.amazonaws.com/clients/research_paper_reports/EB-Report-BE-Manila-
Electric-Vehicles-2021-2.pdf (accessed on 27 January 2023).
International Trade Administration. Philippines Electric Vehicles Market. 2020. Available online: https://www.trade.gov/
market-intelligence/philippines-electric-vehicles-market (accessed on 27 January 2023).

17.

18. Canivel, R.S.C. Filipino Buyers Shift to Smaller Cars, Hevs as Fuel Prices Soar. Available online: https://business.inquirer.net/35

19.

1026/ﬁlipino-buyers-shift-to-smaller-cars-hevs-as-fuel-prices-soar (accessed on 29 April 2023).
Statista Research Department Philippines. Electric Vehicles Sold. 2022. Available online: https://www.statista.com/statistics/12
50975/philippines-electric-vehicles-sold/ (accessed on 29 June 2023).

20. Visconti, K. Hybrid Cars Not Catching on in Philippines. Available online: https://www.rappler.com/business/10854-hybrids-
not-catching-on-in-the-philippines/#:~:text=Hybrids%20haven\T1\textquoterightt%20caught%20on,in%20terms%20of%20
hybrid%20technology%E2%80%A6 (accessed on 26 February 2023).

21. Manila Bulletin Think about Driving an Electric or Hybrid Vehicle. Available online: https://mb.com.ph/2023/01/29/think-

about-driving-an-electric-or-hybrid-vehicle/ (accessed on 29 April 2023).

22. German, J.D.; Redi, A.A.N.P.; Prasetyo, Y.T.; Persada, S.F.; Ong, A.K.S.; Young, M.N.; Nadlifatin, R. Choosing a package
carrier during COVID-19 pandemic: An integration of pro-environmental planned behavior (PEPB) theory and Service Quality
(SERVQUAL). J. Clean. Prod. 2022, 346, 131123. [CrossRef] [PubMed]
Fan, Y.; Chen, J.; Shirkey, G.; John, R.; Wu, S.R.; Park, H.; Shao, C. Applications of structural equation modeling (SEM) in
Ecological Studies: An updated review. Ecol. Process. 2016, 5, 19. [CrossRef]

23.

24. Woody, E. An SEM perspective on evaluating mediation: What every clinical researcher needs to know. J. Exp. Psychopathol. 2011,

2, 210–251. [CrossRef]

25. Al-Emran, M.; Arpaci, I.; Salloum, S.A. An empirical examination of continuous intention to use M-learning: An integrated

model. Educ. Inf. Technol. 2020, 25, 2899–2918. [CrossRef]

26. Ong, A.K.S.; Chuenyindee, T.; Prasetyo, Y.T.; Nadlifatin, R.; Persada, S.F.; Gumasing, M.J.J.; German, J.D.; Robas, K.P.E.; Young,
M.N.; Sittiwatethanasiri, T. Utilization of random forest and deep learning neural network for predicting factors affecting
perceived usability of a COVID-19 contact tracing mobile application in Thailand “Thaichana”. Int. J. Environ. Res. Public Health
2022, 19, 6111. [CrossRef] [PubMed]

27. Larose, R.; De Maagd, K.; Chew, H.E.; Tsai, H.-Y.S.; Steinﬁeld, C.; Wildman, S.S.; Bauer, J.M. Broadband adoption|measuring
sustainable broadband adoption: An innovative approach to understanding broadband adoption and use. Int. J. Commun. 2012,
6, 25. [CrossRef]

28. Yuduang, N.; Ong, A.K.S.; Prasetyo, Y.T.; Chuenyindee, T.; Kusonwattana, P.; Limpasart, W.; Sittiwatethanasiri, T.; Gumasing,
M.J.J.; German, J.D.; Nadlifatin, R. Factors inﬂuencing the perceived effectiveness of covid-19 risk assessment mobile application
“Morchana” in Thailand: Utaut2 approach. Int. J. Environ. Res. Public Health 2022, 19, 5643. [CrossRef]

29. Hassan, I.B.; Murad, M.A.A.; El-Shekeil, I.; Liu, J. Extending the UTAUT2 model with a privacy calculus model to enhance the

adoption of a health information application in Malaysia. Informatics 2022, 9, 31. [CrossRef]

---

<!-- PAGE 23 -->

World Electr. Veh. J. 2023, 14, 227

23 of 26

30. Chang, C.-M.; Liu, L.-W.; Huang, H.-C.; Hsieh, H.-H. Factors inﬂuencing online hotel booking: Extending UTAUT2 with age,

gender, and experience as moderators. Information 2019, 10, 281. [CrossRef]

31. Ajzen, I. The theory of planned behavior. Organ. Behav. Hum. Decis. Process. 1991, 50, 179–211. [CrossRef]
32.

Shiau, W.-L.; Chau, P.Y.K. Understanding behavioral intention to use a cloud computing classroom: A multiple model comparison
approach. Inf. Manag. 2016, 53, 355–365. [CrossRef]
Sentosa, I. The integration of theory of planned behavior (TPB) and technology acceptance model in internet purchasing: A
structural equation modeling (SEM) approach. In Proceedings of the Applied International Business Conference, Kuala Lumpur,
Malaysia, 30 June–2 July 2008.

33.

34. Kim, J.J.; Hwang, J. Merging the norm activation model and the theory of planned behavior in the context of drone food delivery

services: Does the level of product knowledge really matter? J. Hosp. Tour. Manag. 2020, 42, 1–11. [CrossRef]

35. Elkington, J.; Rowland, I.H. Cannibals with forks: The triple bottom line of 21st-century business. Altern. J. 1999, 25, 42–43.
36.
37.

Friedman, L.; Cobb, E.C. Impact of Hybrid Cars; Worcester Polytechnic Institute: Worcester, MA, USA, 2010.
Su, C.-W.; Yuan, X.; Tao, R.; Umar, M. Can new energy vehicles help to achieve carbon neutrality targets? J. Environ. Manag. 2021,
297, 113348. [CrossRef] [PubMed]

38. Korchinski, W. Fueling America: How hydrogen cars affect the environment. Reason Found. Policy Study 2004, 322. Available

online: https://www.policyarchive.org/handle/10207/5741 (accessed on 18 July 2023).

39. Asim, N.; Bimani, A.A.; Saqri, A.A.; Matriano, M. The social and environmental impact of hybrid cars. Int. J. Res. Entrep. Bus.

40.

Stud. 2020, 1, 36–47. [CrossRef]
James, P.; Magee, L. Domains of sustainability. Glob. Encycl. Public Adm. Public Policy Gov. 2016, 1–17. Available online:
https://link.springer.com/referenceworkentry/10.1007/978-3-319-31816-5_2760-1 (accessed on 18 July 2023).

41. He, L.; Wang, M.; Chen, W.; Conzelmann, G. Incorporating social impact on new product adoption in Choice modeling: A case

study in green vehicles. Transp. Res. Part D Transp. Environ. 2014, 32, 421–434. [CrossRef]

42. Turo ´n, K.; Kubik, A. Economic aspects of driving various types of vehicles in intelligent urban transport systems, including

CAR-sharing services and Autonomous Vehicles. Appl. Sci. 2020, 10, 5580. [CrossRef]

43. Nisa, C.F.; Bélanger, J.J.; Faller, D.G.; Buttrick, N.R.; Mierau, J.O.; Austin, M.M.K.; Schumpe, B.M.; Sasin, E.M.; Agostini, M.;
Gützkow, B.; et al. Lives versus livelihoods? perceived economic risk has a stronger association with support for COVID-19
preventive measures than perceived health risk. Sci. Rep. 2021, 11, 9669. [CrossRef] [PubMed]

44. Klöckner, C.A.; Matthies, E. How habits interfere with norm-directed behaviour: A normative decision-making model for travel

45.

mode choice. J. Environ. Psychol. 2004, 24, 319–327. [CrossRef]
Sandqvist, K. The Appeal of Automobiles: Human Desires and the Proliferation of Cars. Available online: https://trid.trb.org/
view/567975 (accessed on 8 May 2023).

46. Tengstrom, R. The Use of the Automobile: Its Implications for Man, Society, and the Environment. Available online: https:

//trid.trb.org/view/386217 (accessed on 8 May 2023).

47. Crabbe, M.; Standing, C.; Standing, S.; Karjaluoto, H. An adoption model for mobile banking in Ghana. Int. J. Mob. Commun.

2009, 7, 515. [CrossRef]

48. Zeithaml, V.A. Consumer perceptions of price, quality, and value: A means-end model and synthesis of evidence. J. Mark. 1988,

52, 2. [CrossRef]

49. Onwezen, M.C.; Antonides, G.; Bartels, J. The norm activation model: An exploration of the functions of anticipated pride and

guilt in pro-environmental behaviour. J. Econ. Psychol. 2013, 39, 141–153. [CrossRef]

50. Rezvani, Z.; Jansson, J.; Bodin, J. Advances in consumer electric vehicle adoption research: A review and research agenda. Transp.

51.

Res. Part D Transp. Environ. 2015, 34, 122–136. [CrossRef]
Schuitema, G.; Anable, J.; Skippon, S.; Kinnear, N. The role of instrumental, hedonic and symbolic attributes in the intention to
adopt electric vehicles. Transp. Res. Part A Policy Pract. 2013, 48, 39–49. [CrossRef]

52. Pikkarainen, T.; Pikkarainen, K.; Karjaluoto, H.; Pahnila, S. Consumer acceptance of online banking: An extension of the

Technology Acceptance Model. Internet Res. 2004, 14, 224–235. [CrossRef]

53. Manutworakit, P.; Choocharukul, K. Factors inﬂuencing battery electric vehicle adoption in Thailand—Expanding the uniﬁed

theory of acceptance and use of technology’s variables. Sustainability 2022, 14, 8482. [CrossRef]

54. Davis, F.D.; Bagozzi, R.P.; Warshaw, P.R. User acceptance of computer technology: A comparison of two theoretical models.

Manag. Sci. 1989, 35, 982–1003. [CrossRef]

55. Gunawan, I.; Redi, A.A.N.P.; Santosa, A.A.; Maghﬁroh, M.F.N.; Pandyaswargo, A.H.; Kurniawan, A.C. Determinants of customer

intentions to use electric vehicle in Indonesia: An integrated model analysis. Sustainability 2022, 14, 1972. [CrossRef]

56. Ombach, G. Design considerations for Wireless Charging System for electric and plug-in hybrid vehicles. In Proceedings of the

Hybrid and Electric Vehicles Conference 2013 (HEVC 2013), London, UK, 6–7 November 2013.

57. Alalwan, A.A.; Dwivedi, Y.K.; Rana, N.P.; Algharabat, R. Examining factors inﬂuencing Jordanian customers’ intentions and

adoption of internet banking: Extending UTAUT2 with risk. J. Retail. Consum. Serv. 2018, 40, 125–138. [CrossRef]

58. Venkatesh, V.; Morris, M.G.; Davis, G.B.; Davis, F.D. User acceptance of information technology: Toward a uniﬁed view. MIS Q.

2003, 27, 425. [CrossRef]

59. Morosan, C.; DeFranco, A. It’s About time: Revisiting utaut2 to examine consumers’ intentions to use NFC mobile payments in

hotels. Int. J. Hosp. Manag. 2016, 53, 17–29. [CrossRef]

---

<!-- PAGE 24 -->

World Electr. Veh. J. 2023, 14, 227

24 of 26

60. Lin, S.-C.; Nadlifatin, R.; Amna, A.R.; Persada, S.F.; Razif, M. Investigating citizen behavior intention on mandatory and voluntary
Pro-Environmental programs through a pro-environmental planned behavior model. Sustainability 2017, 9, 1289. [CrossRef]
61. Pearson. DOE Pushes for Faster electric Vehicle Rollout in the Philippines. Available online: https://www.philstar.com/nation/

2023/06/05/2271616/doe-pushes-faster-electric-vehicle-rollout-philippines (accessed on 8 May 2023).

62. Racz, A.A.; Muntean, I.; Stan, S.-D. A look into electric/hybrid cars from an ecological perspective. Procedia Technol. 2015, 19,

438–443. [CrossRef]

63. Barbosa Junior, M.; Pinheiro, E.; Sokulski, C.C.; Ramos Huarachi, D.A.; de Francisco, A.C. How to identify barriers to the adoption

64.

of sustainable agriculture? a study based on a multi-criteria model. Sustainability 2022, 14, 13277. [CrossRef]
Saif, M.A.M.; Hussin, N.; Husin, M.M.; Alwadain, A.; Chakraborty, A. Determinants of the intention to adopt digital-only banks
in Malaysia: The extension of environmental concern. Sustainability 2022, 14, 11043. [CrossRef]

65. Philippine Statistics Authority. Goal 7. Ensure Environmental Sustainability. 2021. Available online: https://psa.gov.ph/sdg/
about#:~:text=The%20Sustainable%20Development%20Goals%20(SDGs,targets%20and%20232%20unique%20indicators (ac-
cessed on 12 February 2023).

66. Muﬁdah, I.; Jiang, B.C.; Lin, S.-C.; Chin, J.; Rachmaniati, Y.P.; Persada, S.F. Understanding the consumers’ behavior intention in
using green ecolabel product through Pro-Environmental planned behavior model in developing and developed regions: Lessons
learned from Taiwan and Indonesia. Sustainability 2018, 10, 1423. [CrossRef]

67. Galloway, A. Non-probability sampling. In Encyclopedia of Social Measurement; Elsevier: Amsterdam, The Netherlands, 2005;

pp. 859–864.

68. Kirchherr, J.; Charles, K. Enhancing the sample diversity of Snowball Samples: Recommendations from a research project on

anti-dam movements in Southeast Asia. PLoS ONE 2018, 13, e0201710. [CrossRef]

69. Hair, J.F. Multivariate Data Analysis: A Global Perspective; Pearson Prentice Hall: Upper Saddle River, NJ, USA, 2010.
70. Yang, W.; Zhou, S. Using decision tree analysis to identify the determinants of residents’ CO2 emissions from different types of

trips: A case study of Guangzhou, China. J. Clean. Prod. 2020, 277, 124071. [CrossRef]

71. Wu, D.J.; Feng, T.; Naehrig, M.; Lauter, K. Privately evaluating decision trees and random forests. Cryptol. ePrint Arch. 2015.

Available online: https://math.berkeley.edu/~fengt/decision_tree.pdf (accessed on 18 July 2023). [CrossRef]

72. Bordarie, J. Predicting intentions to comply with speed limits using a ‘decision tree’ applied to an extended version of the theory

of planned behaviour. Transp. Res. Part F Trafﬁc Psychol. Behav. 2019, 63, 174–185. [CrossRef]

73. Charbuty, B.; Abdulazeez, A. Classiﬁcation Based on Decision Tree Algorithm for Machine Learning. J. Appl. Sci. Technol. Trends

2021, 2, 20–28. [CrossRef]

74. Milani, L.; Grumi, S.; Camisasca, E.; Miragoli, S.; Traﬁcante, D.; Di Blasio, P. Familial risk and protective factors affecting CPS
Professionals’ Child Removal Decision: A decision tree analysis study. Child. Youth Serv. Rev. 2020, 109, 104687. [CrossRef]
75. Ong, A.K.S.; Kurata, Y.B.; Castro, S.A.D.G.; De Leon, J.P.B.; Dela Rosa, H.V.; Tomines, A.P.J. Factors inﬂuencing the acceptance of

telemedicine in the Philippines. Technol. Soc. 2022, 70, 102040. [CrossRef]

76. Topîrceanu, A.; Grosseck, G. Decision tree learning used for the classiﬁcation of student archetypes in online courses. Procedia

Comput. Sci. 2017, 112, 51–60. [CrossRef]

77. Harwati; Sudiya, A. Application of decision tree approach to student selection model—A case study. IOP Conf. Series: Mater. Sci.

Eng. 2016, 105, 012014. [CrossRef]

78. Chen, J.; Li, Q.; Wang, H.; Deng, M. A machine learning ensemble approach based on Random Forest and radial basis function
neural network for risk evaluation of Regional Flood Disaster: A case study of the yangtze river delta, China. Int. J. Environ. Res.
Public Health 2019, 17, 49. [CrossRef] [PubMed]
Schnebly, J.; Sengupta, S. Random forest twitter bot classiﬁer. In Proceedings of the 2019 IEEE 9th Annual Computing and
Communication Workshop and Conference (CCWC), Las Vegas, NV, USA, 7–9 January 2019.

79.

80. Ong, A.K.S.; Prasetyo, Y.T.; Velasco, K.E.C.; Abad, E.D.R.; Buencille, A.L.B.; Estorninos, E.M.; Cahigas, M.M.L.; Chuenyindee, T.;
Persada, S.F.; Nadlifatin, R.; et al. Utilization of random forest classiﬁer and artiﬁcial neural network for predicting the acceptance
of reopening decommissioned nuclear power plant. Ann. Nucl. Energy 2022, 175, 109188. [CrossRef]

81. Chen, Y.-S.; Chang, T.-W.; Li, H.-X.; Chen, Y.-R. The inﬂuence of Green brand affect on Green Purchase Intentions: The mediation
effects of green brand associations and Green brand attitude. Int. J. Environ. Res. Public Health 2020, 17, 4089. [CrossRef]
82. Rodriguez-Galiano, V.F.; Ghimire, B.; Rogan, J.; Chica-Olmo, M.; Rigol-Sanchez, J.P. An assessment of the effectiveness of a

random forest classiﬁer for land-cover classiﬁcation. ISPRS J. Photogramm. Remote Sens. 2012, 67, 93–104. [CrossRef]

83. Elhenawy, M.; Rakha, H.A.; El-Shawarby, I. Enhanced modeling of driver stop-or-run actions at a yellow indication. Transp. Res.

Rec. J. Transp. Res. Board 2014, 2423, 24–34. [CrossRef]

84. Ermagun, A.; Rashidi, T.H.; Lari, Z.A. Mode choice for school trips. Transp. Res. Rec. J. Transp. Res. Board 2015, 2513, 97–105.

[CrossRef]

85. Casini, M. Building Automation Systems. Constr. 4.0 2022, 525–581. [CrossRef]
86.

Sturman, O.; von Ziegler, L.; Schläppi, C.; Akyol, F.; Privitera, M.; Slominski, D.; Grimm, C.; Thieren, L.; Zerbi, V.; Grewe, B.; et al.
Deep learning-based behavioral analysis reaches human accuracy and is capable of outperforming commercial solutions.
Neuropsychopharmacology 2020, 45, 1942–1952. [CrossRef]

87. Luceri, L.; Braun, T.; Giordano, S. Analyzing and inferring human real-life behavior through online social networks with social

inﬂuence Deep Learning. Appl. Netw. Sci. 2019, 4, 34. [CrossRef]

---

<!-- PAGE 25 -->

World Electr. Veh. J. 2023, 14, 227

25 of 26

88. Pradhan, B.; Lee, S. Landslide susceptibility assessment and Factor Effect Analysis: Backpropagation artiﬁcial neural networks
and their comparison with Frequency Ratio and bivariate logistic regression modelling. Environ. Model. Softw. 2010, 25, 747–759.
[CrossRef]

89. Gudivada, V.N. Natural language core tasks and applications. In Handbook of Statistics; Elsevier: Amsterdam, The Netherlands,

2018; pp. 403–428. [CrossRef]

90. Walrave, M.; Waeterloos, C.; Ponnet, K. Ready or not for contact tracing? investigating the adoption intention of COVID-19
contact-tracing technology using an extended uniﬁed theory of acceptance and use of Technology Model. Cyberpsychol. Behav. Soc.
Netw. 2021, 24, 377–383. [CrossRef]

91. De Ryck, T.; Lanthaler, S.; Mishra, S. On the approximation of functions by Tanh neural networks. Neural Netw. 2021, 143, 732–750.

[CrossRef] [PubMed]

92. Costarelli, D. Neural Network Operators: Constructive interpolation of multivariate functions. Neural Netw. 2015, 67, 28–36.

[CrossRef]

93. Liébana-Cabanillas, F.; Marinkovi´c, V.; Kalini´c, Z. A SEM-neural network approach for predicting antecedents of M-Commerce

Acceptance. Int. J. Inf. Manag. 2017, 37, 14–24. [CrossRef]

94. Narayan, S. The generalized sigmoid activation function: Competitive supervised learning. Inf. Sci. 1997, 99, 69–82. [CrossRef]
95. Li, J.; Sawaragi, T.; Horiguchi, Y. Introduce structural equation modelling to machine learning problems for building an explainable

and persuasive model. SICE J. Control. Meas. Syst. Integr. 2021, 14, 67–79. [CrossRef]

96. Hadiyat, M.A. Combined structural equation modelling—Artiﬁcial neural networks model for predicting customer loyalty. IOP

Conf. Ser. Mater. Sci. Eng. 2019, 703, 012024. [CrossRef]

97. Rossi, C.; Rivetti, F. Assessing young consumers’ responses to sustainable labels: Insights from a factorial experiment in Italy.

Sustainability 2020, 12, 10115. [CrossRef]

98. Bedard, S.A.N.; Tolmie, C.R. Millennials’ green consumption behaviour: Exploring the role of Social Media. Corp. Soc. Responsib.

Environ. Manag. 2018, 25, 1388–1396. [CrossRef]

99. Nadlifatin, R.; Lin, S.-C.; Rachmaniati, Y.P.; Persada, S.F.; Razif, M. A pro-environmental reasoned action model for measuring

citizens’ intentions regarding ecolabel product usage. Sustainability 2016, 8, 1165. [CrossRef]

100. Ajzen, I. Perceived behavioral control, self-efﬁcacy, locus of control, and the theory of planned behavior1. J. Appl. Soc. Psychol.

2002, 32, 665–683. [CrossRef]

101. Cahigas, M.M.; Prasetyo, Y.T.; Persada, S.F.; Ong, A.K.S.; Nadlifatin, R. Understanding the perceived behavior of public utility
bus passengers during the era of COVID-19 pandemic in the Philippines: Application of social exchange theory and theory of
planned behavior. Res. Transp. Bus. Manag. 2022, 45, 100840. [CrossRef]

102. Chong, Y.T.; Teo, K.M.; Tang, L.C. A lifecycle-based sustainability indicator framework for waste-to-energy systems and a

proposed metric of sustainability. Renew. Sustain. Energy Rev. 2016, 56, 797–809. [CrossRef]

103. Foroughi, B.; Nhan, P.V.; Iranmanesh, M.; Ghobakhloo, M.; Nilashi, M.; Yadegaridehkordi, E. Determinants of intention to use

Autonomous Vehicles: Findings from PLS-sem and ANFIS. J. Retail. Consum. Serv. 2023, 70, 103158. [CrossRef]

104. Yang, X. Understanding consumers’ purchase intentions in social commerce through social capital: Evidence from sem and

fsQCA. J. Theor. Appl. Electron. Commer. Res. 2021, 16, 1557–1570. [CrossRef]

105. Yazdanpanah, M.; Hadji Hosseinlou, M. The role of personality traits through habit and intention on determining future

preferences of public transport use. Behav. Sci. 2017, 7, 8. [CrossRef]

106. Lallmahomed, M.Z.; Lallmahomed, N.; Lallmahomed, G.M. Factors inﬂuencing the adoption of e-government services in

Mauritius. Telemat. Inform. 2017, 34, 57–72. [CrossRef]

107. Brown, S.A.; Venkatesh, V. Model of adoption of technology in households: A baseline model test and extension incorporating

household life cycle. MIS Q. 2005, 29, 399. [CrossRef]

108. Palau-Saumell, R.; Forgas-Coll, S.; Sánchez-García, J.; Robres, E. User acceptance of mobile apps for restaurants: An expanded

and extended utaut-2. Sustainability 2019, 11, 1210. [CrossRef]

109. Lane, B.; Potter, S. The adoption of cleaner vehicles in the UK: Exploring the consumer attitude–action gap. J. Clean. Prod. 2007,

15, 1085–1092. [CrossRef]

110. Chaveesuk, S.; Khalid, B.; Bsoul-Kopowska, M.; Rosta ´nska, E.; Chaiyasoonthorn, W. Comparative analysis of variables that

inﬂuence behavioral intention to use moocs. PLoS ONE 2022, 17, e0262037. [CrossRef] [PubMed]

111. Albert, J.R.G.; Santos, A.G.F.; Vizmanos, J.F.V. Proﬁle and Determinants of the Middle-Income Class in the Philippines; Philippine

Institute for Development Studies: Legaspi Village, Philippines, 2018.

112. Nordfjærn, T.; ¸Sim¸seko ˘glu, Ö.; Rundmo, T. The role of deliberate planning, car habit and resistance to change in public

transportation mode use. Transp. Res. Part F Trafﬁc Psychol. Behav. 2014, 27, 90–98. [CrossRef]

113. Agaton, C.B.; Collera, A.A.; Guno, C.S. Socio-economic and environmental analyses of sustainable public transport in the

Philippines. Sustainability 2020, 12, 4720. [CrossRef]

114. Yuriev, A.; Dahmen, M.; Paillé, P.; Boiral, O.; Guillaumie, L. Pro-environmental behaviors through the lens of the theory of

planned behavior: A scoping review. Resour. Conserv. Recycl. 2020, 155, 104660. [CrossRef]

---

<!-- PAGE 26 -->

World Electr. Veh. J. 2023, 14, 227

26 of 26

115. Wang, Z.; Dong, X.; Yin, J. Antecedents of urban residents’ separate collection intentions for household solid waste and their

willingness to pay: Evidence from China. J. Clean. Prod. 2018, 173, 256–264. [CrossRef]

116. Zadjafar, M.A.; Gholamian, M.R. A sustainable inventory model by considering Environmental Ergonomics and environmental

pollution, case study: Pulp and Paper mills. J. Clean. Prod. 2018, 199, 444–458. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Article
Purchasing Intentions Analysis of Hybrid Cars Using Random
Forest Classifier and Deep Learning
ArdvinKesterS.Ong1,2,* ,LaraNicoleZ.Cordova3,FranscineAltheaB.Longanilla3,NealloL.Caprecho3,
RockselAndryV.Javier3,RiañinaD.Borres1,4andJosephineD.German1
1 SchoolofIndustrialEngineeringandEngineeringManagement,MapúaUniversity,658MurallaSt.,
Intramuros,Manila1002,Philippines
2 E.T.YuchengcoSchoolofBusiness,MapuaUniversity,1191PabloOcampoSr.Ext,Makati1205,Philippines
3 YoungInnovatorsResearchCenter,MapúaUniversity,658MurallaSt.,Intramuros,Manila1002,Philippines
4 SchoolofGraduateStudies,MapúaUniversity,658MurallaSt.,Intramuros,Manila1002,Philippines
* Correspondence:aksong@mapua.edu.ph;Tel.:+63-(2)8247-5000(ext.6202)
Abstract: In developed or first-world countries, hybrid cars are widely utilized and essential in
technologicaldevelopmentandreducingcarbonemissions.Despitethat,developingorthird-world
countriessuchasthePhilippineshavenotyetfullyadoptedhybridcarsasameansoftransportation.
Hence,theSustainabilityTheoryofPlannedBehavior(STPB)wasdevelopedandintegratedwith
theUTAUT2frameworktopredictthefactorsaffectingthepurchasingintentionsofFilipinodrivers
toward hybrid cars. The study gathered 1048 valid responses using convenience and snowball
samplingtoholisticallymeasureuseracceptancethroughtwelvelatentvariables.MachineLearning
Algorithm(MLA)toolssuchastheDecisionTree(DT),RandomForestClassifier(RFC),andDeep
LearningNeuralNetwork(DLNN)wereutilizedtoanticipateconsumerbehavior.Thefinalresults
fromRFCshowedanaccuracyof94%andDLNNwithanaccuracyof96.60%, whichwereable
toprovethepredictionofsignificantlatentfactors. PerceivedEnvironmentalConcerns(PENCs),
Attitude(AT),PerceivedBehavioralControl(PBC),andPerformanceExpectancy(PE)wereobserved
tobethehighestfactors.ThisstudyisoneofthefirstextensivestudiesutilizingtheMLAapproach
topredictFilipinodrivers’tendencytoacquirehybridvehicles.Thestudy’sresultscanbeadapted
Citation:Ong,A.K.S.;Cordova,
byautomakersorcarcompaniesfordevisinginitiatives,tactics,andadvertisementstopromotethe
L.N.Z.;Longanilla,F.A.B.;Caprecho,
N.L.;Javier,R.A.V.;Borres,R.D.; viabilityandutilityofhybridvehiclesinthePhilippines.Sinceallthefactorswereprovensignificant,
German,J.D.PurchasingIntentions futureinvestigationscanassessnotonlythebehavioralcomponentbutalsothesustainabilityaspect
AnalysisofHybridCarsUsing ofanindividualusingtheSTPBframework.
RandomForestClassifierandDeep
Learning.WorldElectr.Veh.J.2023, Keywords:hybridcars;machinelearningalgorithm;purchasingintentions;sustainabilitytheoryof
14,227. https://doi.org/10.3390/ plannedbehavior;UTAUT2
wevj14080227
AcademicEditor:GenevieveCullen
Received:20July2023 1. Introduction
Revised:12August2023
Greenhousegasesemittedbyoil-poweredandfossil-fueledvehicleshaveincreased
Accepted:16August2023
over the years. According to Tiseo [1], the global transportation sector is a significant
Published:18August2023
polluter,producingapproximately7.3billiontonsofcarbondioxideemissionsin2020. In
thesameyear, passengercarswerethemostabundantsourceofemissions, accounting
for 41% of global transportation emissions. In Wasiak’s [2] study, internal combustion
Copyright: © 2023 by the authors. engineshavetwoprominentdrawbacks. Thefirstistherelativelylowefficiencyofturning
Licensee MDPI, Basel, Switzerland. theenergycontainedinthefuelintovaluablemechanicalenergyforpropulsion,andthe
This article is an open access article secondisthattheproductionofcarbondioxideandothercomponentsoftheexhaustgas
distributed under the terms and cancontributetoglobalwarming.
conditionsoftheCreativeCommons Hybrid cars are essential in technological development and in addressing carbon
Attribution(CCBY)license(https:// emissionreduction. Furthermore,hybridcarproductioncoversthreeoftheUnitedNations’
creativecommons.org/licenses/by/ globalSustainableDevelopmentGoals(SDGs):the7thSDGforaffordableandcleanenergy,
4.0/).
WorldElectr.Veh.J.2023,14,227.https://doi.org/10.3390/wevj14080227 https://www.mdpi.com/journal/wevj

WorldElectr.Veh.J.2023,14,227 2of26
the8thSDGfordecentworkandeconomicgrowth,andthe13thSDGforclimateaction.
SincetheintroductionofthevariousSDGs,theusageofhybridcarshasbeenpromoted[3].
Thepresentgenerationisseeinganincreaseinthemarketabilityofhybridvehicles,
buttheirutilityisnotwidelyacknowledged. Irawanetal.[4]estimatedthatroughly18.20%
ofautomobileownershavebeguntoconsiderswitchingfromaconventionalvehicleand
becomingpotentialhybridcarusers,while81.22%ofcarbuyerscontinuetorejectgettinga
hybridvehiclecompletely. Thus,consumerbehaviorshouldbeinvestigatedtounderstand
purchasingbehaviorforsustainabletransportationtobewidelyaccepted.
Onetheorywidelyusedtocomprehensivelyassessconsumers’behaviorintheaspect
ofpurchasingandmarketingistheTheoryofPlannedBehavior(TPB)[5]. Itisalsoproven
to extensively measure the intention to purchase. It is applied to examine customers’
behavioralaspectsofbuyingwhilesimultaneouslyprovingsomeofthedeterminantsof
purchaseintentions[6]. InlinewiththeTPBframework,severalstudieshavesupported
thatTPBiscommonlyusedinthefieldofpurchasingcarsduetoitsexplanatorycapacityto
predicttheadoptionorpurchasingintentionofcars,specificallyinHybridElectricVehicles
(HEVs) [7,8]. Similarly, a study by Javid et al. [9] stated that the determinants of TPB
couldalsobeappliedtoconsumers’purchasingintention,eveninElectricVehicles(EVs).
However, inthestudyofGermanetal.[10], TPBhaslimitedvariablesthatrestrainthe
modelforholisticmeasurements.
Anothertheorythatcanbeusedinassessingpeople’sacceptanceandbehavioralinten-
tionsistheUnifiedTheoryofAcceptanceandUseofTechnology2(UTAUT2). Venkatesh
et al. [11] explained how UTAUT2 comprehensively measures the behavioral aspect of
technologyusage. StudiessuchasthatofNordhoffetal.[12]employedtheUTAUT2model
toexplainthepublicacceptanceofconditionallyautomatedcarsinEuropeancountries.
According to their study’s analysis, the UTAUT2 model can be applied to conditional
automation,withhedonicmotivation,socialinfluence,andperformanceexpectancyin-
fluencingthebehavioralintentiontopurchaseandutilizeaconditionallyautomatedcar.
Similarly,PrasetyoandVallespin[13]usedtheUTAUT2modeltoidentifythefactorsinflu-
encingusers’utilityofmobiletechnologyapplicationsandservices. InMalaysia,Khazaei
andTareq[14]examinedconsumers’usageofbatteryelectricvehiclesusingtheUTAUT2
since this model incorporated a broader scope of factors to measure consumers’ usage
intention. However,alimitednumberofstudieshaveanalyzedthepurchasingintentions
ofhybridcars,especiallyinthePhilippines.OnlythatofOngetal.[15]wasseentoconsider
thepurchasingintentionsofhybridcarsinthePhilippines.
InthePhilippines,hybridcarsareavailableinthemarket.Withonlyleadingcarbrands
suchasCherry,Geely,Hyundai,Mitsubishi,Nissan,andToyotasellingtheproduct,limited
accessandpopularityareobserved. Therewere11,851,192registeredmotorvehiclesand
fossil-fueledcarsinthePhilippinesasofDecember2020[16]. Unlikeothercountries,the
hybridcarvehiclemarketinthePhilippinesonlycaterstotheextremeupperclass,which
accountsforonlylessthan0.1%ofthemarket—withabout7000hybridcarsregisteredin
2018[17]. ArecentreportbyCanivel[18]presentedhowKiaPhilippinesshowedasteady
increaseinthepurchaseofhybridcarsduetoincreaseinfuelcosts. Theonceaffordable
dieselfuelisnowrelativelynotthatcheapinthemarket. ItwasreportedthatKiawasable
toincreaseitssalesby14.6%in5months’timeofthesameyear. Kampialsoexpecteda
riseinsalesof17%in2021. AreportbyStatistaresearchdepartment[19]summarizedthe
hybrid/electriccarssoldfrom2020–2022. From378in2020to843in2021,asignificant
increasewasseenin2022with1013unitsbeingsold. Onereasonwhyhybridcarsarenot
highlypopularizedinthecountryistheirmaturityinthePhilippinecarmarket,leadingto
lowadoptionratesofhybridcars[20]. Asreportedbythenews[21],onlyrecently(2023)
hastherebeenanyplanstoputupchargingstations. Itwasreportedthat200charging
stationsareplannedtobeestablishedand500moreby2025. Therefore,theneedtoexplore
thepurchasingintentionsofconsumerswiththisrelativelynewtechnologyforthecountry
is needed. The slow progression of movement in purchase may be capitalized by the
governingunitssincetheestablishmentofchargingstationsandbusinessarestillonthe

WorldElectr.Veh.J.2023,14,227 3of26
rise. Thedeterminationofpurchasingintentionsurroundingthesehybridcarswouldbe
beneficialfortheliteratureandbusinessownersalike.
Thispaperaimedtodeterminewhatfactorsinfluencedrivers’preferencesforfuture
use and purchase intentions of hybrid vehicles (HVs) in the Philippines. Through the
integration of the extended pro-environmental theory of planned behavior (PEPB) of
Germanetal.[22]andtheextendedunifiedtheoryofacceptanceanduseoftechnology
(UTAUT2)onhybridcarpurchaseandusageintention,thisstudyisoneofthefirstfew
thatexaminedtheMLAapproachtobehavioralintention. Sincethecurrentstudyextended
the established purchasing intention of hybrid cars in the Philippines [15], this study
wantedtoaddtotheliteratureonclosingthegapbetweentheuseofmachinelearning
and analyzing human behavior. Structural equation modeling was considered by the
previousstudy[15], whichsuggestedtheuseofmachinelearningtobetteranalyzethe
nonlinearrelationshipamonglatentvariables. Inaccordance,theliterature,suchasthat
ofFanetal.[23],explainedthatsomelatentvariableswhenmediatingfactorsarepresent
maycauselittletonosignificance. Inaccordance,thestudyofWoody[24]alsopresented
similarfindingsandexplainedthatlargenonlinearrelationshipmodelsmaybeunreliable
whenSEMisusedasHeywoodcasesmightbepresentwhichmaycausewrongparameter
estimates[23,25]. Therefore,thisstudycontributestoamorethoroughevaluationofthe
Philippines’capabilitytosustainsmarttechnology—eventuallydevelopingintoasmart
andsustainablecity.
2. ConceptualFramework
2.1. TheoriesandRelatedStudies
Venkatesh et al. [11] extended the existing UTAUT by incorporating three latent
variables,namelyhedonicmotivation,pricevalue,andhabit,thusdevelopingtheUTAUT2
model.TheextensionsproposedintheUTAUT2producedasignificantimprovementinthe
varianceexplainedinbehavioralintentionandtechnologyusecomparedtoitspredecessor,
theUTAUT.AlthoughtheUTAUT2modelcomprehensivelyanalyzestheconstructsfor
theadoptionofnewtechnology, thescopeofthemodelonlyevaluatestheintentionto
usenewtechnologies,makingitinsufficientintermsofholisticallymeasuringthehuman
behaviorattributesandaspects[26]. LaRoseetal.[27]suggestedthattheUTAUT2model
employsgenericmeasuresofthelatentvariablessothatthesameoperationalstandards
canbeusedacrossdifferentstudies. Thisapproachimprovedthemodel’sgeneralizability
butcompromisedtheactionableinformationgathered. Inaddition,Ongetal.[26]stated
thattheUTAUT2modelwasnotabletoanalyzetheactualbehaviorofadoptingtechnology.
Theirstudyrecommendedincorporatingotherfactorsinordertoobtainamoreaccurate
depictionoftheviewpointofthegeneralpopulationinlightoftheseminorinformational
gapsintheresearch. Subsequently,theirstudyalsoshowedthatdemographicfactorsas
mediatingeffectsmightnotbeconsideredinananalysis.
SeveralstudieshaveintegratedtheUTAUT2modelwithothertheoriestoevaluate
innovative solutions and technology. Yuduang et al. [28] considered the integration of
ProtectionMotivationTheory(PMT)andUTAUT2toassesstheactualusageandintention
to use new technologies, specifically mobile applications. Their study stated that this
integrationcouldbeinterpretedasamodelthatcancomprehensivelyassesstheintention
andactualusageofamobileapplication. Hassanetal.[29]integratedthePrivacyCalculus
Model(PMC)andUTAUT2byaddingfourconstructs: privacyconcern,perceivedrisk,
trust,andperceivedcredibility. Theirstudyvalidatedthattheadditionoftheseconstructs
thoroughly measured the consumers’ perspectives in relation to the adoption of new
technologies. Changetal.[30]extendedtheUTAUT2model,whichassimilatestheexisting
constructsfromtheUTAUT2alongwithage,gender,andexperienceasmoderators. Their
study highlighted three findings: (1) age and experience reduce the impact of habit on
usagebehavior,(2)ageaffectstheinfluenceoffacilitatingconditionsonusagebehavior,and
(3)themoderatingeffectofexperiencereducedthedirectimpactofbehavioralintentionon
usagebehavior,makingitirrelevant.

WorldElectr.Veh.J.2023,14,227 4of26
TheTheoryofPlannedBehavior(TPB)wasestablishedtoanticipatehumanbehavior.
AccordingtotheTPB,behavioralintentionisinfluencedbythreefactors: attitude(AT),
subjectivenorm(SN),andperceivedbehavioralcontrol(PEC)[31]. InthestudyofChau
andShiau[32],sixwell-knowntheoreticalmodelswereusedtohaveabetterunderstanding
oftermsofbehavioralintention,includingtheTPBandfiveothermodels,namelyService
Quality(SQ),Self-Efficacy(SE),MotivationalModel(MM),TechnologyAcceptanceModel
(TAM),andInnovationDiffusionTheory(IDT);thus,theunitedmodelgaveathorough
grasp of the aspects that have a significant impact on behavioral intention. With that,
theTPBistobeproveneffectivewhencombinedwithothermodels. Itprovidesamore
comprehensive review of a person’s behavioral intention concerning hybrid cars with
referencetothesaidstudy. InthepaperofSentosa[33],theTPB,alongwithTechnology
AcceptanceModeling(TAM),wasintegrated.Infulfillmentofthepaper,itwasimpliedthat
aperson’sconductisinfluencedbythedesiretoexecutetheactivity,whichisdetermined
byone’sattitudetowardthebehaviorandsubjectivenorm.
KimandHwang[34]usedaresearchmodelthatcombinedtheTPBandNormActiva-
tionModel(NAM)intoasingletheoreticalframeworktoanalyzeeco-friendlybehavioral
intentionstoemploydronefooddeliveryservices. Furthermore,themoderatinginfluence
ofproductknowledgewasinvestigatedinthisstudy,astheamountofproductknowledge
hasamajorimpactoncustomerbehaviors. PEPBandSERVQUALmodelswereintegrated
to further determine Filipino consumers’ behavioral intention in the paper of German
etal.[22],particularlyduringtheCOVID-19pandemic. Inrelianceonthesaidstudy,since
itwasmentionedthatthePEPBplacesemphasisonenvironmentalconcernsandauthority,
variables from the TPB play a role in determining an individual’s behavioral intention
towardsaparticularsituationoractivity. Additionally,thetwomodelsalsoindicateda
higher level of investigation. They can be used in developing countries like the Philip-
pinesbecausethesaidcountrystronglyencouragestheemergenceofmoresustainable
smarttechnology.
ThePEPBmodelwasdevelopedasanextensionofthetheoryofplannedbehavior
(TPB)sinceitcouldnotaddressallfactorsrelevanttothisstudy[22]. Perceivedauthor-
itysupport(PAS),perceivedenvironmentalconcern(PEC),perceivedbehavioralcontrol
(PBC),subjectivenorm(SN),attitude(AT),andbehaviorintention(BI)wereimportantin
determiningtheconsumer’sintentiontopurchaseproducts. Furthermore,othervariables
underthethreesustainabilitydomains,namelyeconomic,environmental,andsocial,are
coveredinthisstudy[35].
From the PEPB model [22], no economic aspects were covered. In line with the
objectiveofthisstudy,naturalresourcessuchasoilcannotbereplenishedrapidlyenough,
whichimpactstheeconomy[36]. Fossil-fueledcarsareknownforproducinglargeamounts
oftoxicairpollutantsintheatmosphere[37]. ThisincreaseinCO2intheatmospherewill
raisetheaveragetemperatureoftheearth’ssurface[38]. Inordertoreduceairpollution,
analternativemustbeused. Asimetal.[39]foundthathybridcarsarelessharmfulto
the environment because they use less gasoline. This shows that hybrid cars are much
cleanerandbetterfortheenvironment;nevertheless,aconsumer’sinterestdoesnotinclude
economicorenvironmentalconcerns[40]. Anindividual’schoiceofhybridcarsmayvary
dependingontheirsocialenvironmentperspective. Forinstance,aconsumer’sdecisionto
buyahybridcarmaypossiblybeinfluencedbytheirfamily,relatives,orfriends[41].
The researchers utilized the Unified Theory of Technology Acceptance and Use of
Technology2(UTAUT2),thePro-environmentalTheoryofPlannedBehavior(PEPB),and
sustainabilitydomainswhileincorporatinganadditionalfactorwhichisperceivedeco-
nomicconcerns(PECCs)tomeasurehumanbehaviorandtechnologyacceptance. Turon´
andKubik[42]studiedtheeconomicconsiderationsofadoptingautonomousvehiclescom-
paredtothetraditionalautomobilefleetacquiredbyindividualconsumersincar-sharing
systems. Inadifferentscope,Nisaetal.[43]revealedthatperceivedeconomicriskcon-
sistentlypredictedmitigationbehaviorandpolicysupport,andeconomicconsiderations
positivelypredictedalloutcomes. Hence,theaddedfactor,perceivedeconomicconcerns

World Electr. Veh. J. 2023, 14, x FOR PEER REVIEW 5 of 27
The researchers utilized the Unified Theory of Technology Acceptance and Use of
Technology 2 (UTAUT2), the Pro-environmental Theory of Planned Behavior (PEPB), and
sustainability domains while incorporating an additional factor which is perceived eco-
nomic concerns (PECCs) to measure human behavior and technology acceptance. Turoń
and Kubik [42] studied the economic considerations of adopting autonomous vehicles
compared to the traditional automobile fleet acquired by individual consumers in car-
sharing systems. In a different scope, Nisa et al. [43] revealed that perceived economic risk
consistently predicted mitigation behavior and policy support, and economic considera-
tions positively predicted all outcomes. Hence, the added factor, perceived economic con-
WorldElectr.Veh.J.2023,14,227 5of26
cerns (PECCs), relates to a sense of social responsibility, extensive societal and commercial
consideration, and voluntary company involvement.
(PECCs),relatestoasenseofsocialresponsibility,extensivesocietalandcommercialcon-
2.2. Conceptual Framework
sideration,andvoluntarycompanyinvolvement.
The Sustainability Theory of Planned Behavior (STPB) framework used in this study
(2F.2ig. Cuorne c1ep) teunalcoFrmampeawssoreks the combination of the TPB and the PEPB with the UTAUT2 and
the eTxhteenSsuiostna inoaf btihliet yeTcohneoormyiocf fPalcatnonre. dSeBveehraavli ovra(rSiTaPbBle)sf,r ainmceluwdoirnkgu hseadbiint (tHhiBs)s,t updryice value
((PFiVgu),r hee1d)oenncioc mmpoatsisveastitohen c(oHmMbi)n, apteiornfoorfmthaencTeP BexapnedctthanecPyE P(PBEw),i tehfftohret UexTpAeUcTta2nacnyd (EE), fa-
theextensionoftheeconomicfactor. Severalvariables,includinghabit(HB),pricevalue
cilitating conditions (FCs), perceived authority support (PAS), perceived environmental
(PV), hedonic motivation (HM), performance expectancy (PE), effort expectancy (EE),
concern (PENC), perceived behavioral control (PBC), perceived economic concern
facilitatingconditions(FCs),perceivedauthoritysupport(PAS),perceivedenvironmental
(PECC), subjective norm (SN), attitude (AT), and behavioral intention (BI) were taken into
concern(PENC),perceivedbehavioralcontrol(PBC),perceivedeconomicconcern(PECC),
account to comprehensively analyze the intention to use and actual purchase intention of
subjectivenorm(SN),attitude(AT),andbehavioralintention(BI)weretakenintoaccountto
ccoomnspurmeheernss’i vtoelwyaanrdal yhzyebtrhied incaternst. ioTnhitso fursaemanedwaocrtku awlpaus rachdaospetiendte fnrtoiomn othfceo sntsuudmye rosf’ Ong et
atol.w [a1r5d].h ybridcars. ThisframeworkwasadoptedfromthestudyofOngetal.[15].
FFiigguurree 11..S Suusstataininabaibliitlyittyh ethoreyoroyf polfa npnlaendnbeedh abveihoravfriaomr efwraomrkewwiotrhkU wTAithU TU2T.AUT2.
TheUTAUT2modelcanmeasuretheindividual’sintentiontousehybridcars. Inthis
study,anewframeworkwasestablishedinwhichthesocialinfluence(SI)wastransferred
tothePEPBmodelassubjectivenorm(SN).ThisisduetothePEPBhavingasubjective
norm(SN)variable,wheretheyofferedthesamebehavioralaspectbasedontheinfluence
ofotherpeople.

WorldElectr.Veh.J.2023,14,227 6of26
Habitisrepeatedlydescribedasaresultofearlierexperienceswithnumerousfactors,
whichbecomesabeneficialchoice[11]. Itisalsoconsideredapotentialfactorindecision
making[44]. Positivefeelingsassociatedwiththehabitualproductexperienceofdriving
acarstrengthensthehabitanddiscouragesconsumersfromembracinganewmeansof
transportation,suchashybridcars[45,46]. Additionally,theadoptionofanewcarmaybe
influencedbypreviousexperiencewithsimilarcars[47]. Thus,itwashypothesizedthat:
H1. Habithasasignificantdirecteffectonbehavioralintention.
Thetermpricevalue(PV)referstoconsumers’cognitivetrade-offbetweentheper-
ceived advantages of the applications and the financial expense of utilizing them [11].
Moreover,theadvantagesandassociatedexpensesofpurchasinghybridcarswereassessed
andcontrasted[48]. Irawanetal.[4]observedthatgaspriceandsupplyaffectedtheutility
ofhybridcarssignificantly;thissuggeststhatconsumersaremorelikelytoacquireahybrid
cardependingonthefuelcostandsupply. Thus,itwashypothesizedthat:
H2. Pricevaluehasasignificantdirecteffectonbehavioralintention.
Venkateshetal.[11]definedhedonicmotivationasthefunorpleasurederivedfrom
using technology. It also makes an individual feel better since it is a crucial factor in
consumerchoicetopurchasehybridcars[49–51]. Thus,itwashypothesizedthat:
H3. Hedonicmotivationhasasignificantdirecteffectonbehavioralintention.
According to Venkatesh et al. [11], performance expectancy (PE) is the degree of
personalbeliefthatemployingcollaborativetechnologywouldincreaseworkefficiency
andresultinoperationalsuccess.Additionally,ifcustomersfindasimplesystemtobeused,
itwillbemoreaccepted[52]. Thiscouldbeafactorinencouragingpeopletopurchase[53].
Thus,itwashypothesizedthat:
H4. Performanceexpectancyhasasignificantdirecteffectonbehavioralintention.
Effort Expectancy (EE) relates to the level of ease connected with the use of the
system. ThedefinitionofEEdiscussestheeffortrequiredtobecomeskillfulwhenutilizing
technology. ThismethodiscomparabletotheideaofDavis[54]ofperceivedeaseofuse,
whichaddressestheextenttowhichpeoplethinkutilizingtechnologydoesnotinvolve
much effort [55]. Ombach [56] concluded that developed technologies are efficiently
integratedwithseveralvehicles. Thus,itwashypothesizedthat:
H5. Effortexpectancyhasasignificantdirecteffectonbehavioralintention.
FacilitatingConditions(FCs)aresaidtobethedegreetowhichapersonfeelsthata
technologicalandorganizationalinfrastructureexiststoenabletheusageofthesystem[57].
FC affects people’s perception of infrastructures, technical support, and other facilities
whentheyutilizetechnology,products,andservices. InthepreviousUTAUTmodels,FC
wastheorizedasanoperatorofuserbehavior. Thismeansthatusersaremorelikelyto
usenewtechnologyifthereareavailableresources,expertise,andsupport[58]. Dueto
this,nationalpolicyactionsarerequiredtopromotethecommercializationoflow-carbon
technology (i.e., hybrid cars) in both advanced and especially developing nations like
thePhilippines[53]. Inaddition,FCispresumedtobeanessentialvariableinfluencing
behavioralintentionintheUTAUT2framework[11,59]. Thus,itwashypothesizedthat:
H6. Facilitatingconditionshasasignificantdirecteffectonbehavioralintention.
AstudybyWangetal.[8]revealedthatthetheoryofplannedbehavior(TPB),together
withitsprimaryconstructs,wasfoundtopredictbehavioralintentionsaccurately. Attitude
is characterized as the positive or negative evaluation of the adoption behavior. Social
influenceorsubjectivenormreferstotheperceivedsocialpressureanindividualfeelsfrom
others. Perceivedbehavioralcontrolwasdefinedasthelevelofperceivedeaseordifficulty
withregardtoengaginginthebehavior. Hybridelectricvehicleshavebeenregardedas
a potential solution to the pressure of lowering carbon emissions in the transportation

WorldElectr.Veh.J.2023,14,227 7of26
industry—affectingconsumers’behavioralintentionsonadoptinghybridcars. Tanwirand
Hamzah [7] integrated the theory of planned behavior with environmental knowledge
as the foundation of their research model to examine the factors influencing people’s
intention to buy a hybrid car. They found that people’s perceptions of their ability to
manageresourcesarethemostsignificantpredictorsoftheirintentiontopurchasehybrid
vehicles. Thus,itwashypothesizedthat:
H7. Subjectivenormhasasignificantdirecteffectonbehavioralintentions.
H8. Attitudehasasignificantdirecteffectonbehavioralintentions.
H9. Perceivedbehavioralcontrolhasasignificantdirecteffectonbehavioralintentions.
AccordingtoLinetal.[60],theperceivedenvironmentalconcerns(PENCs)latentvari-
ablefunctionsastheantecedentofthesubjectivenorm(SN),attitude(AT),andperceived
behavioralcontrol(PBC)variablesinthePEPBmodelofGermanetal.[22]. Caremissions
raisequantitiesofcarbondioxideandothergreenhousegaseswhiletrappingthesun’sheat
intheEarth’satmosphere,whichcausesglobalwarming. Intheyear2020,transportation
passengercarscontributetoaround41%ofworldwidecarbonemissions[1]. Thereisan
apparent need for alternatives or modifications that would better sustain the means of
transportationandautomotiveindustryproductionsnationwide,suchasdevelopingan
electriccar,butmoreopenandaccessibletothegeneralpublicandmoreethicallypriced,
particularlyhybridcars[61].Raczetal.[62]conductedastudyontheecologicalperspective
ofhybridcars. Theirresultsrevealedthatthemodernconceptofaneco-friendlycarisa
strongstartforahealthierenvironment,butatthesametime,batteryrecyclingrequires
greater focus because the advantages of electric batteries are generally acknowledged,
whilethedrawbacksofrecyclingarefrequentlyignored. Thus,itwashypothesizedthat:
H10. Perceivedenvironmentalconcernshaveasignificantdirecteffectonsubjectivenorm.
H11. Perceivedenvironmentalconcernhasasignificantdirecteffectonattitude.
H12.Perceivedenvironmentalconcernshaveasignificantdirecteffectonperceivedbehavioralcontrol.
Tothoroughlyexaminetheadoptionpotentialofhybridcars,theresearchersestab-
lishedtheSTPBmodelinaccordancewiththesustainabilitydomains. Thelatentvariable
perceived economic concerns (PECCs) was added. Barbosa Junior et al. [63] presented
theeconomicdimensionofthefinancialviabilityofprovidingproductioncontinuitywith
economicresourcesobtainedthroughsustainablepractices. Theirresearchidentifiedthree
barriers: low financial return, financial incentive, and financial viability. Social factors
arestronglyrelatedtosurveyrespondents’adoptionofsustainablepractices. Similarly,
economicconcernsorperceivedeconomicconcernsdirectlyimpactsubjectivenormand
attitude. Economic efficiency was used as an independent variable in a study by Saif
etal.[64]topredicttheintentiontoadoptdigital-onlytechnology. Itwasdefinedascus-
tomers’ perceptions of being able to save time, effort, and financial resources by using
theservices. Accordingtotheirfindings,perceivedconvenienceandperceivedeconomic
efficiencyhaveasignificantpositiveeffectontheusageintention,whichwouldsufficethe
significantdirecteffectPECChasonperceivedbehavioralcontrol. Thus, thefollowing
werehypothesized:
H13. Perceivedeconomicconcernshaveasignificantdirecteffectonsubjectivenorm.
H14. Perceivedeconomicconcernshaveasignificantdirecteffectonattitude.
H15. Perceivedeconomicconcernshaveasignificantdirecteffectonperceivedbehavioralcontrol.
InastudybyGermanetal.[22]utilizingthepro-environmentaltheoryofplanned
behavior(PEPB)model,perceivedauthoritysupport(PAS)referstoanindividual’sper-
ception of any resources, regulations, processes, or actions delivered by a government
orauthorityorganizationthatcanassistpeopleincarryingoutaparticularactivity. The
Philippines’policiesandprogramsareaimedatpreventingthedepletionofenvironmental

WorldElectr.Veh.J.2023,14,227 8of26
resources,whichinvolvesreducingenergyuse,chlorofluorocarbons,andcarbondioxide
emissions[65]. Thegovernment’sinitiativetosupervisethetransitionfromfossil-fueled
carstohybridcarsisexpectedtohaveanimpactonconsumers’purchaseintentiontoward
hybrid cars [66]. According to Lin et al. [60], support from the government has a posi-
tiveandsubstantialeffectonsubjectivenorm,attitude,andperceivedbehavioralcontrol,
demonstratingthatthegovernmenthasasignificantimpactonitspopulation. Thus,itwas
hypothesizedthat:
H16. Perceivedauthoritysupporthasasignificantdirecteffectonsubjectivenorm.
H17. Perceivedauthoritysupporthasasignificantdirecteffectonattitude.
H18. Perceivedauthoritysupporthasasignificantdirecteffectonperceivedbehavioralcontrol.
3. Methodology
3.1. Participants
TheresearchersconductedanonlinesurveytopredictFilipinos’purchasingintentions
forhybridcars. Non-probabilitysamplingmethodswereutilizedtogathertherespondents
forthestudy. AccordingtoGalloway[67],conveniencesamplingcanhelpgatheravariety
ofattitudesandopinionsaswellasidentifytentativeideas. Thatbeingso,theconvenience
samplingmethodwasused. Meanwhile,snowballsamplingwasalsoemployedtoreach
thetargetednumberofparticipantswiththehelpofeachone’ssocialnetwork[68]. The
researchersobtainedmorethan500respondents,generalizingthestudy’sresults[69]. Since
theself-administeredsurveywasopentothegeneralpublic,therespondentsanswered
attheirdiscretion. Atotalof 1149responseswereaccumulated(Table1), but1048was
the number of responses considered since 101 participants did not possess a driver’s
license—theinstrument’sprimaryqualification. Thisresultedina91.21%validresponse
ratewithnomissingdata—similartotheadopteddatafromOngetal.[15].
Table1.Respondents’descriptivecharacteristics(n=1048).
| Characteristics | Category | N   | %    |
| --------------- | -------- | --- | ---- |
|                 | Female   | 146 | 13.9 |
Gender
|     | Male  | 902 | 86.1  |
| --- | ----- | --- | ----- |
|     | 17–22 | 5   | 0.48  |
|     | 23–29 | 341 | 32.54 |
|     | 30–36 | 365 | 34.83 |
Age
|                      | 37–43             | 192  | 18.32 |
| -------------------- | ----------------- | ---- | ----- |
|                      | 44–50             | 97   | 9.26  |
|                      | 51–60             | 48   | 4.58  |
|                      | Lessthan20,000    | 42   | 4.01  |
|                      | 20,000–30,000     | 310  | 29.58 |
|                      | 30,000–40,000     | 495  | 47.23 |
| MonthlyIncome/Salary | 40,000–50,000     | 113  | 10.78 |
|                      | 50,000–60,000     | 52   | 4.96  |
|                      | Greaterthan60,000 | 34   | 3.24  |
|                      | Others            | 2    | 0.19  |
|                      | Employed          | 1035 | 98.76 |
|                      | Self-employed     | 8    | 0.76  |
| Occupation           | Unemployed        | 1    | 0.1   |
|                      | Retired           | 0    | 0.0   |
|                      | Student           | 4    | 0.38  |
|                      | Married           | 553  | 52.77 |
|                      | Single            | 487  | 46.47 |
MaritalStatus
|     | Widowed   | 4   | 0.38 |
| --- | --------- | --- | ---- |
|     | Separated | 4   | 0.38 |

WorldElectr.Veh.J.2023,14,227 9of26
Table1.Cont.
| Characteristics       |                              | Category    | N   | %     |
| --------------------- | ---------------------------- | ----------- | --- | ----- |
|                       | Elementarygraduate           |             | 2   | 0.19  |
|                       | Juniorhighschoolgraduate     |             | 1   | 0.1   |
|                       | Seniorhighschoolgraduate     |             | 4   | 0.38  |
| EducationalAttainment | Technical–VocationalGraduate |             | 2   | 0.19  |
|                       | CollegeGraduate              |             | 992 | 94.66 |
|                       | MasterGraduate               |             | 45  | 4.29  |
|                       |                              | PhDGraduate | 2   | 0.19  |
|                       |                              | Urban       | 866 | 82.63 |
Residence
|                       |                   | Rural  | 182 | 17.37 |
| --------------------- | ----------------- | ------ | --- | ----- |
|                       | Ownedhouseandlot  |        | 566 | 54.01 |
|                       | Ownedanapartment  |        | 25  | 2.39  |
| TypeofResidentialHome | Ownedacondominium |        | 10  | 0.95  |
|                       |                   | Rental | 395 | 37.69 |
|                       |                   | Others | 52  | 4.96  |
|                       |                   | Yes    | 636 | 60.69 |
Doyouhavecarinsurance?
|     |     | No  | 412 | 39.31 |
| --- | --- | --- | --- | ----- |
3.2. Questionnaire
Aquestionnairewith13distinctportionsandfouritemseachwasadaptedfromthe
relatedliterature[15]. Participantswereaskedtoratehowmuchtheyagreedordisagreed
withthegivenstatementona5-pointLikertscaletogatherinformationforthisstudy.
DatapreprocessingwasperformedpriortointegratetheMachineLearningAlgorithm
(MLA).SPSS25wasutilizedtoexaminethemissingdata. Forthedatacleaningprocess,
nonsignificantindicatorswithap-valuemoresignificantthan0.05wereremovedfromthe
datausingcorrelationanalysis. Similarly,fortheMLAoptimization,onlytheindicators
withavaluehigherthan0.20correlationcoefficientwereconsidered. Sincenoneofthe
indicationswereremoved,allproposedindicatorsweredeemedsignificant.
TorepresenttheinputfortheMLA,thevariousindicatorswereaveragedthroughdata
aggregation. Theimplicationsinthequestionnaireportraythelatentfactorsthatwereun-
observedvariablesandweretakenintoaccountinthisstudyfortheMLAutilizingPython
3.8, specifically Spyder 3—an integrated development environment. Other algorithms,
suchasthedecisiontree(DT),therandomforestclassifier(RFC),andthedeeplearning
neuralnetwork(DLNN)wereusedafterdatanormalizationtopredictthefactorsaffecting
theacceptanceofhybridcarsamongFilipinodrivers.
3.3. DecisionTree
A decision tree is a structure and classification approach with regression capacity
appliedasapredictionfactorinaclusterofindependentvariables[70]. Thisstructureis
labeledasaprimaryclassifierofdecisionnodesorganizedinatreepattern[71]. Theyare
easilyinterpretableandvisuallyportrayedashierarchicalstructures[72]. Additionally,
decision trees are often employed in model classification in data mining [73]. Milani
etal.[74]alsostatedthatDTiswidelyrecognizedasoneofthemosteffectivemethods
for dealing with nonlinear datasets. Since decision trees study a nonlinear dataset for
understanding human features and behavior [75], this approach can be applied to the
currentstudy.
BasedonthestudyofTopîrceanuandGrosseck[76],MLArecognizesdecisiontreesas
oneofitsclassificationtools.Itcategorizesrelevantlatentvariablesthatimpactadependent
factorbyevaluatingtherelationshipbetweenfactorsrepresentedbytreebranches. Their
studyalsostatedthatDTsareapredictivemodelforhumanbehaviorregardlessofthe
targetvariable’squantity. Furthermore,DTsareutilizedtodevelopapredictionmodel
formultipleclass(dependentfactor)labelsindomainssuchashealthcare,humanfactors,
manufacturing,andotherfields[77].

WorldElectr.Veh.J.2023,14,227 10of26
InconjunctionwithestablishingtheEntropyandGiniindexvaluesalongsidebestand
randomsplitters,varioustestingandtrainingratioswereappliedtotheDTclassification
process, such as the 40:60, 50:50, 60:40, 70:30, 80:20, and 90:10 training-to-testing ratios.
FollowingthestudyofChenetal.[78]thetreedepthwasevaluated,spanningfromfourto
seven. Theidealdecisiontreewasdeterminedbyrunningeachcombination100timesfora
totalof9600runs. Thesplitter(RandomorBest),trainingandtestingratios,treedepth,and
thecriterion(GiniorEntropy)werealldeterminedusingtheanalysisofvariance(ANOVA)
toevaluatetheidealdecisiontree.
3.4. RandomForestClassifier
Therandomforestclassifierisasupervisedclassificationalgorithmthatcategorizes
data by creating several classifiers to attain greater prediction accuracy [79]. The basic
decision tree generates a large number of branches; therefore, RFC classifies the most
satisfactory decision tree using several characteristics and creates the best branch split
amongthedecisiontrees[80]. TheprimarygoalofemployingtheRFCasMLAistolocate
the best tree with a high accuracy rate. The random forest classifier evaluates the best
tree for each iteration, whereas the standard DT generates a random tree for each run.
Chen et al. [81] supported the claim that the random forest classifier is the best among
other decision trees. According to the study of Rodriguez-Galano et al. [82], RFCs are
farmoreaccurateandresistanttonoisethansingleclassifiers(i.e.,basicdecisiontrees);
hence,ensemblelearningalgorithmslikerandomforest,bagging,andboostingaregaining
popularity. InthepaperofElhenawyetal.[83]andErmagunetal.[84],theRFCwasused
topredicthumanbehavior,specificallydrivingbehavior. Thus,thesameclassificationtool
wasappliedinthecurrentinvestigation. Similaroptimizationparameterswereutilizedin
thestudy,aspresentedintheDTsections.
3.5. DeepLearningNeuralNetwork
Comparedtoothermachinelearningandartificialintelligenceapplications,thedeep
learningneuralnetwork(DLNN)isrecognizedasthebestmodelforpredictingparameters
oridentifyingpatternsbecauseofitscapacitytoassessandcalculatemanyperceptions[26].
Cassini[85]statedthatthisalgorithmhassignificantadvantagesoverconventionalmachine
learning algorithms (MLAs) in extracting features at various levels of abstraction and
therebylearningmorecomplexpatterns. Furthermore,deeplearningneuralnetworksare
artificial neural networks with additional hidden layers between the input and output
layers, wherein Ong et al. [26] explained how these can assess nonlinear relationships
amongframeworksdeveloped. AccordingtoSturmanetal.[86],thevariationbetweenand
amonghumanannotatorsiseliminatedbythedeepneuralnetwork,whichoutperforms
commercialsystemsatalowercostandcontributestotheenhancementofbehavioraldata
quality and accuracy. Luceri et al. [87] affirmed that the deep learning neural network
effectivelyevaluatesthepsychologicalbehavior,behavioralintention,andpsychologyof
consumers. Inthisstudy,theresultsobtainedfromtherandomforestclassifierwouldbe
supportedbyuseofthedeeplearningneuralnetworksincethismethodcanpredictand
categorizethemostinfluentialfactorsaffectingthebehavioralintentionofconsumersin
purchasinghybridcars.
Similartothesetconditionswitharandomforestclassifier,thedeeplearningneural
network preprocessing incorporated correlation analysis for data cleaning. Following
datanormalization,variousactivationfunctionsforthehiddenlayer(sigmoid,tanh,and
swish),outputlayer(sigmoid),andoptimizer(Adam,SGD,RMSProp)weretakeninto
consideration[80]. Additionally,thenumberofnodesforthe80:20trainingandtesting
ratiowasalsoincludedusingafeed-forwardneuralnetworkprocess. Atotalof6480runs
wereconducted,setwith150epochsperiteration[88].

WorldElectr.Veh.J.2023,14,227 11of26
4. Results
4.1. DecisionTree
Iterationsofthedifferentcombinationsofparametersinthebasicdecisiontreewere
accomplishedtogeneratethebestoutput. PresentedinTable2arethesummarizedresults.
It could be posited that at depth 5, the most consistent tree output based on standard
deviationwasproducedwithGiniandbestassplitterandcriterion. Thoughentropyand
besthadhigheraccuracyrates,asignificantdifferencewasnotevident. Inaddition,the
accuracyratesunderGiniandbesthadhigheraccuracyrates.
Table2.DecisionTreeSummarizedResults.
| Category | 60:40 | 70:30 | 80:20 | 90:10 |
| -------- | ----- | ----- | ----- | ----- |
Random
| Gini              | 65.54 | 67.16 | 65.16 | 67.20 |
| ----------------- | ----- | ----- | ----- | ----- |
| StandardDeviation | 2.051 | 2.214 | 2.344 | 3.117 |
| Entropy           | 65.42 | 67.00 | 65.29 | 67.61 |
| StandardDeviation | 1.962 | 2.168 | 2.384 | 3.512 |
Best
| Gini              | 70.18 | 68.15 | 67.06 | 72.00 |
| ----------------- | ----- | ----- | ----- | ----- |
| StandardDeviation | 0.389 | 0.642 | 0.639 | 0.000 |
| Entropy           | 67.00 | 69.49 | 68.00 | 72.32 |
| StandardDeviation | 0.000 | 0.503 | 0.000 | 0.471 |
ThestudyofGermanetal.[22]presentedthattheselowaccuracyratesfromthebasic
decisiontreewereduetothefactthatitgeneratesrandomtreeseveryiteration. Itwas
proposedthatarandomforestclassifierbeused. Inthiscase,therandomforestclassifier
findsthebesttreeoutputeveryiteration,whichinturnconsidersahigheraccuracyrate.
StudiessuchasthatofOng[80]andChenetal.[81]presentedthesamediscussionand
justifiedhowtherandomforestclassifiercanpresenttheoptimumtreeoutput.
4.2. RandomForestClassifier
PresentedinTable3arethesummarizedresultsoftherandomforestclassifier. Fol-
lowingrelatedstudies[22,80,81],higheraccuracyrateswereevidentintherandomforest
classifier output compared to the basic decision tree. Similar to the basic decision tree,
depth5presentedthemostconsistentoutputwithGiniandbestastheparameters.
Table3.RandomForestClassifierSummarizedResults.
| Category | 60:40 | 70:30 | 80:20 | 90:10 |
| -------- | ----- | ----- | ----- | ----- |
Random
| Gini              | 81.82 | 80.69 | 83.22 | 85.38 |
| ----------------- | ----- | ----- | ----- | ----- |
| StandardDeviation | 4.896 | 3.668 | 5.904 | 4.582 |
| Entropy           | 82.85 | 80.36 | 84.43 | 83.69 |
| StandardDeviation | 3.300 | 3.976 | 5.028 | 6.238 |
Best
| Gini              | 88.74  | 84.06 | 92.55 | 94.00 |
| ----------------- | ------ | ----- | ----- | ----- |
| StandardDeviation | 0.7115 | 1.003 | 0.500 | 0.000 |
| Entropy           | 83.63  | 84.98 | 89.37 | 92.00 |
| StandardDeviation | 1.120  | 0.642 | 1.077 | 0.000 |

| World Electr. Veh. J. 2023, 14, x FOR PEER REVIEW  |     |     |     | 12 of 27  |
| -------------------------------------------------- | --- | --- | --- | --------- |

| Standard Deviation  | 0.389  | 0.642  | 0.639  | 0.000  |
| ------------------- | ------ | ------ | ------ | ------ |
| Entropy             | 67.00  | 69.49  | 68.00  | 72.32  |
| Standard Deviation  | 0.000  | 0.503  | 0.000  | 0.471  |
The study of German et al. [22] presented that these low accuracy rates from the basic
decision tree were due to the fact that it generates random trees every iteration. It was
proposed that a random forest classifier be used. In this case, the random forest classifier
finds the best tree output every iteration, which in turn considers a higher accuracy rate.
Studies such as that of Ong [80] and Chen et al. [81] presented the same discussion and
justified how the random forest classifier can present the optimum tree output.
4.2. Random Forest Classifier
Presented in Table 3 are the summarized results of the random forest classifier. Fol-
lowing related studies [22,80,81], higher accuracy rates were evident in the random forest
classifier output compared to the basic decision tree. Similar to the basic decision tree,
depth 5 presented the most consistent output with Gini and best as the parameters.
Table 3. Random Forest Classifier Summarized Results.
| Category  | 60:40  | 70:30  | 80:20  | 90:10  |
| --------- | ------ | ------ | ------ | ------ |
Random
| Gini                | 81.82  | 80.69  | 83.22  | 85.38  |
| ------------------- | ------ | ------ | ------ | ------ |
| Standard Deviation  | 4.896  | 3.668  | 5.904  | 4.582  |
| Entropy             | 82.85  | 80.36  | 84.43  | 83.69  |
| Standard Deviation  | 3.300  | 3.976  | 5.028  | 6.238  |
Best
| Gini                | 88.74   | 84.06  | 92.55  | 94.00  |
| ------------------- | ------- | ------ | ------ | ------ |
| Standard Deviation  | 0.7115  | 1.003  | 0.500  | 0.000  |
WorldElectr.Veh.EJ.n20t2r3o,p1y4, 227 83.63  84.98  89.37  92.00  12of26
| Standard Deviation  | 1.120  | 0.642  | 1.077  | 0.000  |
| ------------------- | ------ | ------ | ------ | ------ |
IItt ccoouuldldb bees eseenenf rformomth tehree sruesltuslttsh athtatht eth9e0 :1900:t1r0a itnrianingitnegs ttiensgtirnagti oraptiroo dpurocedducthede mthoes t
cmonossits ctoenntsitsrteeenwt tirtehe 9w4i%tha 9c4c%ur aacccyuarancdy aanstda na dstaarndddaervdi dateivoinatvioanlu veaolufe0 .o0f0 00..0T00h.u Tsh,uthsi, sthtries e
oturetep uotuwtpaust cwoanss icdoenrseiddethreedo tphteim oupmtimculamss icfilacsastiifoincamtioond eml.oFdieglu. rFeig2urreep 2re rseepnrtesstehnetso tphteim opu-m
ttriemeuwmit htreaer wanidtho am rafonrdeostmc lfaosrseisfite crl.assifier.

Figure2.OptimumTreewithRandomForestClassifier.
From the output, PENC (X ) dictated the behavioral intentions for acceptance of
1
hybrid cars. The tree will consider AT (X 0 ) for the first node. Then, it will consider X 0 ,
X (≤−0.412), and PBC (X ) with a value less than or equal to −0.909. Satisfying this
| 1   |     | 2   |     |     |
| --- | --- | --- | --- | --- |
(≤−0.412)condition
| condition,peoplewillhaveveryhighbehavioralintentions. |     |     | IftheX 1 |     |
| ----------------------------------------------------- | --- | --- | -------- | --- |
isnotsatisfied,onlyahighbehavioralintentionisseen. ThisindicatesthatPENCshould
behighlightedforpeopletohaveaveryhighorpositivebehavioralintention. Asimilar
outputisevidentifthefirstchildnodeconditionsarenotsatisfied.
If the parent node with a value less than or equal to 0.386 is not satisfied,
a 0.123condition for X first child node is considered. Satisfying this will consider X
0 1
and then PE (X 4 ) with a value less than or equal to −0.043, which will lead to a high
behavioralintention. ThispositsthatasPENCisinfluentialtothecontrolofanindividual
toaccepthybridcars,itsperformanceshouldalsobehighlightedasutilizationfortrans-
portation. Lastly,ifthechildnodeconditionsarenotsatisfied,itwillconsiderX ,thenX ,
2 1
andX ,whichwillleadtoveryhighbehavioralintentions.
0
Fromthefindings,itcouldbededucedthatPENCandATarethetopsignificantfactors
thataffectedpeople’sPBCandPEtohaveveryhighbehavioralintentionsforhybridcars.
ThisdictatesthatPBCandPEaresignificantfactorsaswellthatwouldinfluenceusers’
acceptanceofhybridcars. However,withvariedfactorsstillpresent,therandomforest
classifierneedsfurtherassistancefromotherMLAstoprovideadistinctclassificationof
latentvariablesaffectingbehavioralintentions. Chenetal.[81]consideredothertoolsin
supportofthefindingsoftherandomforestclassifiertodeducesignificantlatentvariables.
4.3. DeepLearningNeuralNetwork
Following the study of Ong et al. [75], deep learning neural network parameter
optimization was conducted to provide the optimum classification model. From the
differentparameterstested,tanh,astheactivationfunctionforthedifferenthiddenlayers,
presentedthebestoutput. Usingsigmoidastheactivationfunctionintheoutputlayerand
adamastheoptimizer,thesummarizedtrainingandtestingaverageresultsarepresented
inTable4.

WorldElectr.Veh.J.2023,14,227 13of26
Table4.Summarizedresultsfordeeplearningneuralnetwork.
Factor AverageTraining StandardDeviation AverageTesting StandardDeviation
| PENC | 91.41 | 1.630 |     | 93.14 |     | 1.681 |     |
| ---- | ----- | ----- | --- | ----- | --- | ----- | --- |
| AT   | 90.71 | 0.928 |     | 93.06 |     | 1.807 |     |
| PBC  | 80.95 | 1.663 |     | 89.84 |     | 2.631 |     |
| SN   | 80.70 | 0.143 |     | 87.29 |     | 2.997 |     |
| PE   | 81.12 | 1.071 |     | 83.14 |     | 2.285 |     |
| PAS  | 80.01 | 7.850 |     | 80.62 |     | 1.943 |     |
| FC   | 77.21 | 1.473 |     | 79.14 |     | 2.491 |     |
| HM   | 74.72 | 0.800 |     | 77.29 |     | 2.860 |     |
| EE   | 67.80 | 2.769 |     | 75.76 |     | 1.993 |     |
| PECC | 68.67 | 3.343 |     | 70.35 |     | 1.226 |     |
| PV   | 65.78 | 7.093 |     | 70.43 |     | 3.210 |     |
| HB   | 60.50 | 2.211 |     | 68.52 |     | 3.761 |     |
Tanhis anactivation functionthatis considered tobe anextensionof thesigmoid
function.Gudivada[89]explainedthatastretchedandshiftedsigmoidcalculationisseenin
thetanhactivationfunction. Thisisusuallyconsideredfornonlinearrelationshipmodels,
which can present high accuracy rates when used in the hidden layers. As explained
byWalraveetal.[90],tanhisanactivationfunctionwithstrongercomplexitytoupdate
weightsinneuralnetworkmodels,whichresultsinfasteroptimizationandhigheraccuracy
rates. TheequationoftanhispresentedinEquation(1)adoptedfromdeRycketal.[91].
2
|     |     | tanh(x) | =   | −1  |     |     | (1) |
| --- | --- | ------- | --- | --- | --- | --- | --- |
1+e−2x
Forsigmoid,Costarelli[92]explainedthatthisactivationfunctionismostlyutilized
in the output layer as it calculates nonlinear relationships with smaller ranges. Since
tanhwasconsideredwithseveralhiddenlayersinthisstudy,boundedvalueswouldbe
evidentaftertheprocess,whichcanbecomputedusingsigmoid[93]. Itisalsoarguedto
beefficientdespiteitssimplecalculation,whichiscommonlyutilizedwhenprobabilities
are considered. Equation (2) represents the sigmoid activation function adopted from
Narayan[94].
1
|     |     | sigmoid(x) | =   |     |     |     | (2) |
| --- | --- | ---------- | --- | --- | --- | --- | --- |
1+e−x
ThefinaldeeplearningneuralnetworkclassificationmodelispresentedinFigure3. A
totalofthreehiddenlayerswith50,50,and20nodes,respectively,providedtheoptimum
model.Witha96.60%accuracy,thescoreofimportanceusingSPSS25wasusedtoverifythe
outputofconsecutiverankingoffactorsaffectingtheacceptanceofhybridcars. Presented
inTable5isthenormalizedscoreoftheimportanceoftheresultingparameters.
Table5.Normalizedscoresofimportance.
|     | Factor |     | Importance |     | NormalizedImportance |        |     |
| --- | ------ | --- | ---------- | --- | -------------------- | ------ | --- |
|     | PENC   |     | 0.107      |     |                      | 100%   |     |
|     | AT     |     | 0.103      |     |                      | 96.32% |     |
|     | PBC    |     | 0.101      |     |                      | 94.50% |     |
|     | SN     |     | 0.099      |     |                      | 92.12% |     |
|     | PE     |     | 0.097      |     |                      | 90.20% |     |
|     | PAS    |     | 0.090      |     |                      | 84.50% |     |
|     | FC     |     | 0.087      |     |                      | 81.20% |     |
|     | HM     |     | 0.084      |     |                      | 79.00% |     |
|     | EE     |     | 0.083      |     |                      | 77.60% |     |
|     | PECC   |     | 0.082      |     |                      | 76.70% |     |
|     | PV     |     | 0.081      |     |                      | 76.20% |     |
|     | HB     |     | 0.076      |     |                      | 70.90% |     |

World Electr. Veh. J. 2023, 14, x FOR PEER REVIEW 14 of 27
to update weights in neural network models, which results in faster optimization and
higher accuracy rates. The equation of tanh is presented in Equation (1) adopted from de
Ryck et al. [91].
tanh(𝑥)= 2 −1 (1)
1+𝑒−2𝑥
For sigmoid, Costarelli [92] explained that this activation function is mostly utilized
in the output layer as it calculates nonlinear relationships with smaller ranges. Since tanh
was considered with several hidden layers in this study, bounded values would be
evident after the process, which can be computed using sigmoid [93]. It is also argued to
be efficient despite its simple calculation, which is commonly utilized when probabilities
are considered. Equation (2) represents the sigmoid activation function adopted from
Narayan [94].
𝑠𝑖𝑔𝑚𝑜𝑖𝑑 (𝑥)= 1 (2)
1+𝑒−𝑥
The final deep learning neural network classification model is presented in Figure 3.
A total of three hidden layers with 50, 50, and 20 nodes, respectively, provided the
optimum model. With a 96.60% accuracy, the score of importance using SPSS 25 was used
to verify the output of consecutive ranking of factors affecting the acceptance of hybrid
WorldElectr.Veh.J.2023,14,227 14of26
cars. Presented in Table 5 is the normalized score of the importance of the resulting
parameters.
FiFgiugruer 3e. 3D.eDepe eleparlneainrgn innegurnael unreatwlnoerktw moordkelm. odel.
4.4 . Validation
To validate the different MLA accuracy outputs, a Taylor Diagram was generated.
FollowingthestudyofGermanetal.[22]andOng[23],therootmeansquareerrorshould
bewithin20%andtheacceptedcorrelationvalueat90%forsignificantfactors. Settingthe
thresholdof1.00forthestandarddeviation,Figure4representstheTaylorDiagramforthis
study. ItcouldbeseenthattheoutputofdifferentMLAsusedinthisstudyisacceptable.
Moreover,thebasicdecisiontreecannotbeutilizedduetothelowoutputat0. Inaddition,
World Electr. Veh. J. 2023, 14, x FOR PEtEhR eREleVaIEsWt significantfactors,suchasHM,EE,PECC,PV,andHB,canst1il6l obf e27c onsideredbut
arelessinfluentiallatentvariables.
FFigiugruer 4e. T4.ayTlaoyr lDoiragDraiamg. ram.
5. Discussion
Hybrid cars promote sustainable transportation, which is essential for both techno-
logical advancement and reducing carbon emissions; therefore, it is crucial to study the
role of behavioral intention in determining how Filipino drivers adapt and transition to
eco-friendly vehicles. The study aimed to examine the factors influencing Filipinos’ ac-
ceptance or purchasing intentions toward hybrid cars using the Pro-environmental The-
ory of Planned Behavior (PEPB) and Sustainability Domains. These were combined into
the Sustainability Theory of Planned Behavior, along with the integrated the Unified The-
ory of Acceptance and the Use of Technology 2 (UTAUT2). From the results, both the
random forest classifier (RFC) and the deep learning neural network (DLNN) were uti-
lized to evaluate the different significant factors affecting purchasing intentions of hybrid
cars.
This study was able to justify the limitations of SEM as discussed by related studies
[23–25]. As seen, PENC was deemed to be the most important latent variable, followed by
AT, PBC, SN, and PE. Compared to the SEM result [15], it was seen that these were ranked
fifth, third, seventh, second, and fourth, respectively. Clear distinctions were seen within
the indirect effects among sustainability domains, which were mediated by the TPB do-
mains. From the current study, PENC was deemed highly significant, while PAS ranked
sixth, and PECC ranked tenth–compared to its SEM counterpart results being fifth, third,
and first, respectively. Since the presence of mediating factors are seen among the STPB
model, the justification of hindrance among mediating factors played a role [23–25].
In addition, the MLA results proved that the FC, EE, and HB were significant while
the SEM results deemed them insignificant. As explained by Li et al. [95] who compared
the SEM with the MLA, it was presented that the MLA has more predictive capabilities,
generated higher accuracy rates, and could better present the model output rather than
the final model SEM considers. It was added that the MLA can provide better explanation
of the model based on the mutual understanding of machines and humans. Hadiyat [96]
also provided the same justification. However, not all output may be different like that of
Ong et al. [75] when analyzing telemedicine acceptance in the Philippines where both the
SEM and the ANN provided the same output. Their explanation in the paper was that

WorldElectr.Veh.J.2023,14,227 15of26
5. Discussion
Hybridcarspromotesustainabletransportation,whichisessentialforbothtechno-
logicaladvancementandreducingcarbonemissions;therefore,itiscrucialtostudythe
roleofbehavioralintentionindetermininghowFilipinodriversadaptandtransitionto
eco-friendlyvehicles. ThestudyaimedtoexaminethefactorsinfluencingFilipinos’accep-
tanceorpurchasingintentionstowardhybridcarsusingthePro-environmentalTheory
ofPlannedBehavior(PEPB)andSustainabilityDomains. Thesewerecombinedintothe
SustainabilityTheoryofPlannedBehavior,alongwiththeintegratedtheUnifiedTheory
ofAcceptanceandtheUseofTechnology2(UTAUT2). Fromtheresults,boththerandom
forest classifier (RFC) and the deep learning neural network (DLNN) were utilized to
evaluatethedifferentsignificantfactorsaffectingpurchasingintentionsofhybridcars.
This study was able to justify the limitations of SEM as discussed by related
studies[23–25]. As seen, PENC was deemed to be the most important latent variable,
followedbyAT,PBC,SN,andPE.ComparedtotheSEMresult[15],itwasseenthatthese
wererankedfifth,third,seventh,second,andfourth,respectively. Cleardistinctionswere
seenwithintheindirecteffectsamongsustainabilitydomains,whichweremediatedbythe
TPBdomains. Fromthecurrentstudy,PENCwasdeemedhighlysignificant,whilePAS
rankedsixth,andPECCrankedtenth–comparedtoitsSEMcounterpartresultsbeingfifth,
third,andfirst,respectively. Sincethepresenceofmediatingfactorsareseenamongthe
STPBmodel,thejustificationofhindranceamongmediatingfactorsplayedarole[23–25].
Inaddition,theMLAresultsprovedthattheFC,EE,andHBweresignificantwhile
theSEMresultsdeemedtheminsignificant. AsexplainedbyLietal.[95]whocompared
theSEMwiththeMLA,itwaspresentedthattheMLAhasmorepredictivecapabilities,
generatedhigheraccuracyrates,andcouldbetterpresentthemodeloutputratherthan
thefinalmodelSEMconsiders. ItwasaddedthattheMLAcanprovidebetterexplanation
ofthemodelbasedonthemutualunderstandingofmachinesandhumans. Hadiyat[96]
alsoprovidedthesamejustification. However,notalloutputmaybedifferentlikethat
ofOngetal.[75]whenanalyzingtelemedicineacceptanceinthePhilippineswhereboth
theSEMandtheANNprovidedthesameoutput. Theirexplanationinthepaperwasthat
theirstudyonlyutilizedadirectrelationshipfromtheUTAUT2. Thus,thissmallmodel
compared to the current study has distinct differences. Summarized in Table 6 are the
differentrankedscoresofthelatentvariables. Thediscussionofthesucceedingsectionis
basedonthehighestsignificanteffectfromMLA.
Table6.MLAversusSEMResults.
| LatentVariable | MLA  | SEM           |
| -------------- | ---- | ------------- |
| PENC           | 1st  | 5th           |
| AT             | 2nd  | 3rd           |
| PBC            | 3rd  | 7th           |
| SN             | 4th  | 2nd           |
| PE             | 5th  | 4th           |
| PAS            | 6th  | 3rd           |
| FC             | 7th  | Insignificant |
| HM             | 8th  | 6th           |
| EE             | 9th  | Insignificant |
| PECC           | 10th | 1st           |
| PV             | 11th | 8th           |
| HB             | 12th | insignificant |

WorldElectr.Veh.J.2023,14,227 16of26
Fromthefindings,thehighestcontributingfactortoconsumeracceptancewasthe
perceivedenvironmentalconcern(PENC)(100%)latent,havingasignificantdirecteffecton
subjectivenorm(SN),attitude(AT),andperceivedbehavioralcontrol(PBC).Basedonthe
indicators,Filipinodriversorgeneralrespondentsrecognizedthathumankindisseverely
abusingandpollutingtheenvironment,causingthemtobeworriedaboutitsfuturestatus
andavoidingmoredisastrousconsequences. Theyfeltcompelledtoadoptmoreecologi-
callyfriendlyproducts,suchashybridcars,whicharebothhandyandbeneficialtothe
existingenvironmentalconditions. RossiandRivetti[97]mentionedthatyoungerpeople,
notablymillennialsandpost-millennials(ages23–29and30–36),aremoreconcernedwith
sustainability,haveacollectivepurchasingpower,andarebecominganincreasinglycrucial
consumerdemographic. Becausetheyaremoreinclinedtoenvironmentalactivismanden-
gagingthroughplatformswheretheseeco-labeleditemsandideologiesarepromoted—in
thisstudy,obtaininghybridcars—millennialsaremorelikelytoutilizeeco-friendlyman-
ufacturedproducts[98]. Thus,itcouldbededucedthathybridcarscouldbeviableasa
highlyefficientformoftransportationduetotheirpositiveenvironmentaleffects.
Attitude (AT) (96.32%) was also deemed to have a highly significant direct effect
on behavioral intention (BI). This shows that the positive or negative evaluation of the
adoptionbehaviorofhybridcarswillparticularlyinfluenceaperson’sintentiontopurchase
them. Respondentsweremorelikelytobelievethatpurchasingahybridcarisawiseand
pleasantdecision,andtheytrustedthenotionofpurchasingahybridcarsincelearning
to utilize it may be a fulfilling experience. In addition, this finding is substantiated by
thestudyofChenetal.[78],whichproveshowproductsthatmaymakecustomersfeel
joyful,thrilled,orcheerfulcanleadtomoreacceptanceandahigherloyaltyattitude. In
addition,thestudyofNadlifatinetal.[99]validatedthecorrelationbetweenATandBI
asthegreatestvalueamongallcorrelationresultsregardingtheuseofeco-labelproducts.
Therefore,thesecanbeobtainedthroughtheassociatedemotionalandknownsustainable
benefitsthatgreenproductsactivelyelicit. Inaccordance,PBCandPEwereprovedtohave
ahighlysignificantanddirecteffectonBI.
PBC (94.50%) and PE (90.20%) were shown to have a highly significant and direct
effectonBI.AlthoughlowerthanthatoftheATlatent,itsuggeststhatdriverscanstillsense
theeaseofoperationofahybridcarcomparedtoaconventionalvehicleandthatitcomes
withmoreexcellentresourcesandopportunitiesoranticipationthatitislessvulnerableto
impediments[100]. ThisfindingwassupportedbyCahigasetal.[101],whichfoundthat
PBCsignificantlyandpositivelyaffectedtheintentiontouseinthetransportationsetting.
Based on the two sets of indicators, it is up to the consumer’s discretion to confidently
selectahybridcarforhis/herfuturepurchasebydeterminingthatdrivingahybridcar
wouldbesafer,morecomfortable,andmoreproductive. Furthermore,PEhasbeenproven
byChongetal.[102]tohaveastrong, positiveassociationwithbehavioralintentionin
adoptingnewtechnology,similartothestudyconductedbyForoughietal.[103]inthearea
ofautonomoustransportation.Thesearevitalaspects,especiallywhenahighpercentageof
respondentswereworkingindividualswhorequireefficiencyintransportationandfewer
hindrancesinusingadifferenttypeofvehicle.
Concerningthesignificantfactors,SN(92.12%)latenthadasignificantdirecteffect
on BI. Filipinos believed that the people they trusted who influenced and had a good
impressiononthemwouldalsorecommendthattheypurchaseoruseahybridcar.Similarly,
itwasindicatedthathybridcarswouldcomeoffasmoreprestigiousthantraditionalfossil-
fueledvehicles. ThisresultalignedwithastudybyYang[104],whereinconsumers’buying
intentionswereimpactedbypeertrustandreciprocity. Theywereeagertotakeadviceand
suggestionsfromtrustworthypeers.Consequently,themoderateinfluenceSIhasonBImay
bebecauseonlytheexperienceofsocialinteractionsthathavecreatedcloserelationships
amongpeerswouldimpactcustomers’buyingintentionsmoresignificantly[10,101].
AlongwithSN,perceivedauthoritysupport(PAS)(84.50%)hadasignificantdirect
effectonSN,AT,andPBC.Theindicatorsrevealthatthegovernmentisactiveinsettingup
facilitiesforhybridcars,enactsregulationsthatallowFilipinostousethesevehicles,and

WorldElectr.Veh.J.2023,14,227 17of26
encouragesorendorsestheusageofthemthroughthesesameregulations. Althoughthe
PhilippineStatisticsAuthority[65]hasacknowledgedthattherearepoliciesandprograms
in place to enable the acquisition and handling of hybrid vehicles, they still need to be
promotedonparwithconventionalvehiclesinthemarket. AstudybyYazdanpanahand
HadjiHosseinlou[105]suggestedthatpolicymakersseektomodifyhabitsbyproviding
relevantinformationtoenhancetheintention-behaviorrelationship. Withthat, thereis
a need for eco-labeled cars in the country, which is gradually being addressed by the
authorities. EspeciallyinthePhilippines,thegovernmentistakingsmallsteps,suchas
settingupsomeplacesforchargingelectriccars. However,thepromotionoftheusageis
stillunderrepresentedinthecountry.
Facilitatingconditions(FCs)(81.20%)alsoprovedtobeasignificantfactoraffectingBI.
TheindicatorsdelineatedthatFilipinodrivershavethenecessaryresourcestooperatea
hybridcar,areknowledgeableindriving,andcanaskquestionsandfindsolutionsifany
problemsareidentified. ThisfindingissimilartothestudyofLallmahomedetal.[106],
whereintheypresentedhowFCsignificantlyaffectsusageintention. Yuduangetal.[28]
also mentioned how consumers prefer using applications that are beneficial and easily
accessible. Theresourcesthatareaccessibleforcontinuoususageofnewtechnologies,such
ashybridcars,areconsideredbythecurrentgeneration. Hedonicmotivation(HM)(79%)
wasalsoseentobeasignificantfactoraffectingBI.Basedontheindicators,usingahybrid
carismorefun,entertaining,enjoyable,andsatisfyingthandrivingafossil-fueledcar. It
has been demonstrated that hedonic motivation, defined as the enjoyment or pleasure
consumers derive from adopting new technology, is crucial in influencing technology
acceptanceanduse[107]. Theresultsoftheanalysisofthehedonicmotivationconstruct
wereinlinewiththeresultsofpreviousstudiesbyVenkateshetal.[11]andPalau-Saumell
etal.[108],asboththeirresultssubstantiatedthefactthathedonicmotivationisasignificant
predictorofintentiontouse.
Effortexpectancy(EE)(77.60%)alsoprovedtobeasignificantfactoraffectingBI.The
indicatorsthatledtotheimportancewerethathybridcarsprovideclearandunderstandable
interactionsthatareeasytooperate,adapt,andadept. Thisresultisquitesimilartothe
findingsofNordhoffetal.[12]: sinceEEisasubstantialpositivepredictorofbehavioral
intention, individuals who imply that using conditionally autonomous cars is simple
aremorelikelytowanttoutilizethem. Alignedwiththis,perceivedeconomicconcern
(PECC)(76.70%)wasalsoprovedtobeasignificantfactoraffectingBI,SN,AT,andPBC.
The study found that hybrid cars have good warranties and economic incentives, can
generatemoresavingswhichimproveanindividual’seconomicstandinginthelongrun,
drivemoreefficiently,andareeasilyacquirableinthemarket. Thisaddedlatent,which
completesthesustainabilitytheoryofplannedbehavior(STPB),isrelatedtoanindividual’s
voluntaryinvolvement,comprehensivesocietalandcommercialconsideration,andsense
ofsocialresponsibility.
ThisissupportedbythestudyofSaifetal.[64],whichprovedthatconsumers’inten-
tiontoadopthasapositiverelationshipwithperceivedeconomicefficiency. Accordingto
theirfindings,practitionersshouldprovideclientswithfinancialbenefits,suchascharge-
free,new,oruniqueservices,andcompetitiveprices,tofurtherpromoteuseracceptance.
It has been established by Lane and Potter [109] that economic instruments point to a
strategyofpromotingtheuseofcleanerfuelsandvehiclesthroughtheuseoffinancial
incentives,anapproachbasedontheconceptofecologicaltaxationreform. Thisindicates
substantialevidencethateconomicfactorscaneffectivelyencouragecleaneroptionssuch
ashybridcars.
Interestingly, despite the positive remarks of the latent price value (PV) (76.20%)
indicatorsthathybridcarsarereasonablypriced,goodvalueformoney,andavaluable
purchase,itwasstillconsideredthesecondleastsignificantfactoraffectingBI.Chaveesuk
etal.[110]explainedthatpricevalue,whichisdefinedasconsumers’cognitivetrade-offs
betweentheperceivedcostsandbenefitsofadoptingaspecificsystem,hasasignificant
direct effect on behavioral intention. Concerning the demographic factors, most of the

WorldElectr.Veh.J.2023,14,227 18of26
respondentshaveamonthlysalaryof20,000pesosto50,000pesoswhichmeansthatthey
belong to the lower middle class to the middle class as stated on the indicative range
ofmonthlyfamilyincomeinthestudyofAlbertetal.[111]. However, consumersmay
purchaseorarewillingtoinvestinhybridcarsinsteadoffossil-fueledcars,regardlessofthe
addedamount,sincetheyareconsideredcost-effective. Thisstudyfiguredthatconsumers
arewillingtopaytheextraamountfortheefficiency,environmental,andeconomicbenefits
thathybridcarsoffer.
The least significant out of all the latent affecting behavioral intention was Habit
(HB)(70.90%). Basedontheindicators,usingahybridcarbecameahabit,anaddiction
forwhichconsumersarewillingtopaymore,andservesasadailyutility. Theutilityof
hybridcarsremainsunrecognizedandunfamiliartomanysincethePhilippinemarket
forhybridcarsiscurrentlysparse,whichiswhyHBhasnotbeenestablishedandisthe
leastsignificantfactor. Similarly,Nordfjaernetal.[112]discoveredthatthecarhabitfactor
negativelypredictsintentionandisnotassignificantasotherbehavioralfactors. Itwas
found that to predict better user intention, user personality traits must be assessed in
line with TPB domains. As a result, consumers still need to develop the habit of using
thismodeoftransportation. Eventually,itisexpectedthathabitwillsoondevelopifthe
hybridcarmarketinthePhilippinesbecomessaturated,buildingstrongfamiliaritywith
Filipinodrivers.
To better provide insights among readers, Table 7 lists all the abbreviations used
throughoutthestudy.
Table7.Listofabbreviationsusedthroughoutthepaper.
Abbreviations Meaning
ANN ArtificialNeuralNetwork
AT Attitude
BI BehavioralIntentions
DLNN DeepLearningNeuralNetwork
DT DecisionTree
HB Habit
HM HedonicMotivation
HV HybridVehicle
IDT InnovationDiffusionTheory
MLA MachineLearningAlgorithm
MM MotivationalModel
NAM NormActivationModel
PE PerformanceExpectancy
PECC PerceivedEconomicConcern
PEPB Pro-EnvironmentalTheoryofPlannedBehavior
PENC PerceivedEnvironmentalConcern
PV PriceValue
RFC RandomForestClassifier
SE Self-Efficacy
SI SocialInfluence
SN SubjectiveNorm
SQ ServiceQuality
EE EffortExpectancy

WorldElectr.Veh.J.2023,14,227 19of26
Table7.Cont.
Abbreviations Meaning
FC FacilitatingConditions
PAS PerceivedAuthoritySupport
STPB SustainabilityTheoryofPlannedBehavior
TAM TechnologyAcceptanceModel
TPB TheoryofPlannedBehavior
UTAUT2 UnifiedTheoryofAcceptanceandUseofTechnology
5.1. TheoreticalContributions
AccordingtothestudybyAgatonetal.[113],airpollutionandgreenhousegasemis-
sionsfromthecombustionoffossilfuelsareoneofthemaindriversofwhygovernments
andregionsseekmoresustainablemeansoftransportation. Withthat,PEPBwasusedto
analyzetheenvironmentalimpactonconsumers’behavioralintentionandsupportsthe
otherlatentvariablesofthesustainabilitydomains[22]. AlongsidethePEPBframework,
thesustainabilitydomains,suchassocial,environmental,andeconomic,wereconsidered,
whiletheUTAUT2addressedthetechnologicalaspect. InthestudyofYurievetal.[114],
theTPB,orthetheoryofplannedbehavior,isthemostextensivelyusedmodelinstudying
individuals’ behavior and is stated to encompass all environmental behavior variables.
However,itlacksthenecessarysustainabilitylatentconstruct[102,115].
Inmeasuringtheacceptanceentirelyorholistically,theframeworksmentionedabove
werecombinedwithintegratingtheeconomicaspectintotheproposedsustainabilitytheory
ofplannedbehavior(STPB).Itcanbeappliedwhenevaluatingthecurrentgeneration’s
behavioralintentionandacceptanceofnewlyemergingorcurrentsmarttechnologiessuch
as the hybrid car. According to the study of Zadjafar and Gholamian [116], consumers
nowadaysaremoreconsciousofobtainingandpurchasingsustainableproducts. Inthis
case,itwassuggestedthatmanufacturersandindustriesfocusmoreondevelopingand
selling products that attest to the demand of green consumers. Since all the factors in
the study were proven significant, the developed framework could be used by future
researcherstomeasurenotonlythebehavioralaspectbutalsothesustainabilityaspectof
anindividualutilizingtheSTPB.
5.2. PracticalandManagerialImplications
Thefindingsofthisstudyhavedemonstratedtheimportanceofpredictingconsumers’
acceptanceofhybridcarsinthePhilippines. Filipinodriverstendtoconsiderhybridcars
whenawareoftheenvironmentalandeconomicbenefits. Theresultofthestudyproved
thatitisessentialfortheyoungergenerationtoadapttoamoresustainablelifestyle,with
thehighdemandforgreenertransportation. Giventhatthereiscurrentlyalimitedmarket
forhybridcarsinthePhilippines,consumersarestillunawareoftheutilityofthesevehicles.
Fortunately,thisconditionmightimprovewithincreasedgovernmentreinforcementby
adopting incentives to promote their utility. Hybrid cars cost more than fossil-fueled
cars, which makes the marketing aspect challenging. In line with this, car companies
andmanufacturerscanalsousetheresultofthisstudyasaframeworkfordesigningand
implementingprograms,strategies,andadvertisementstopropagatethemarketabilityand
utilityofhybridcars. Itissuggestedthatcarcompaniesshouldconsidermillennialsasthe
primarytargetforeco-friendlymanufacturedproductssuchashybridcars,asprojectedin
thestudy’sdemographicresults. Theadvertisementandstrategiesmayrevolvearound
sustainability,targetgeneration,andthedevelopmentandusageofhybridcarstoengage
purchasingintentions. Lastly,consideringthetechnologicalaspect,companiescanalso
disseminate information about the ecological and economic advantages of hybrid cars
throughsocialmediaplatformsandin-appadvertisementssuchasFacebookandYouTube
adsthatcanbecapitalizedbymarketingfirms.

WorldElectr.Veh.J.2023,14,227 20of26
5.3. Limitations
Althoughtherearepositivefindingsinthisstudy,therearealsoseverallimitations
tobenoted. First,duetotheadaptedquestionnaire,therewerelimitedconstructs. The
instrumentwasaself-administeredonlinesurvey, whichpresentsaconstraintinterms
ofthemodalityofthedisseminationandfollowsthesecondpoint,theconsiderationof
therespondents. Havingmoreconstructsanditemsofmeasuremaydevelopresponse
efficiency. Inaddition,consideringinterviewersmayidentifydriversforpurchasinghybrid
carsamongresidentsinthePhilippinesthatotherstudiesmayconsider.
Second, the primary criteria of a driver’s license and the modality narrowed the
respondentstothosedriverswhowereactiveonsocialmedia. Itisrecommendedthat
thedatacollectionbemorediversifiedandnotbeinclinedtoonlyaparticulargeneration,
specificallythemillennials. Abalanceofeachvariationwouldemergeifthestudycould
expoundonothergenerations, suchasGenerationZorbabyboomers, andwouldalso
makestudyingtheacceptanceofeachgenerationtowardhybridcarspossible. Itwould
bemoreprofoundtogathermorerespondentsoutsidethecurrentstudy’ssample,suchas
publicutilityvehiclesorpublicutilityjeepneydrivers,separatelytoreassessthedifferent
perspectives,behavior,andexperiencesofdriverstowardhybridcars.
Third, it is suggested that the study conduct interviews with these individuals to
provideaqualitativeandquantitativeanalysisofthosewhointendtopurchasehybrid
cars. Allowingthestudytohaveaqualitativeaspectwouldprovidemoreflexibility. The
insightsfromtheinterviewresultsmaybeconsideredforadditionallatentvariablesand
itemsofmeasure,evenpresentingaqualitative-quantitativestudy.
Fourth,thisstudyonlyconsideredtwomachinelearningalgorithms:therandomforest
classifierandthedeeplearningneuralnetwork. Tomaximizetheutilityofrelatedanalysis
techniques, other machine learning algorithm tools such as the Naïve Bayes classifier,
K-Nearestneighbor,vectormachine,orevenC-Meansclusteringmaybeincorporatedto
capturedifferentareasoftheresultandidentifyfactorsbasedonprobabilityandsimilarities
asidefromtheindividualfindingsfoundinthisstudy. Lastly,othertoolssuchasK-Means
clusteringcouldbeutilizedaftergatheringrespondentsfromdifferentgenerationstoassess
thedemographiccharacteristicsofdriverswhointendtopurchasehybridcarsfromthe
lowesttothehighestvaluedcustomers,whichwouldallowtheresearcherstoformulate
strategieswiththemarkettosupporttheeconomicaspectfurther. Simultaneousanalysis
ofthevariousfactorsmaybereanalyzedusingmultivariateanalysistoolstojustifythe
study’sfindingssincetheindirecteffectfoundoneachlatentmayprovideasignificant
relationshipamongthefactorsconsideredwhenitcomestothebehavioral,sustainable,
andtechnologicalaspectsofconsumers’purchasingintentionstowardhybridcars.
6. Conclusions
There are not enough studies on the purchasing intentions regarding hybrid cars
in developing countries like the Philippines. This necessitated the formulation of the
SustainabilityTheoryofPlannedBehavior(STPB).Theframeworkwasconstructedusing
thePro-environmentalTheoryofPlannedBehavior(PEPB)andsustainabilitydomains,as
wellasintegrationoftheUnifiedTheoryofAcceptanceandUseofTechnology2(UTAUT2)
to predict the adoption of hybrid cars in the country. It was utilized to fully assess the
acceptanceofsmartandgreentechnology,emphasizingsustainability—avitalaspectwhen
addressingclimatechange. Atotalof1048participantscompletedtheself-administered
survey,disseminatedusingnon-probabilitysamplingmethods,includingconvenienceand
snowballsampling.
This study utilized a Machine Learning Algorithm (MLA) ensemble comprising a
DecisionTree(DT),RandomForestClassifier(RFC),andDeepLearningNeuralNetwork
(DLNN),whichprovedthatPENC,AT,PBC,andPEwerethemostinfluentialfactorsthat
significantlyaffectuseracceptanceofhybridcarsinthePhilippines. ThisimpliesthatMLA
isadvantageousinanalyzingtheantecedentsofhumanbehavior,particularlysustainability
behavior. ComparingtheresultsofbothSEMandMLA,thisstudyidentifiedthatMLA

WorldElectr.Veh.J.2023,14,227 21of26
providedbetterandmoreaccurateresultssincethisstudywasabletoconsideranexpanded
andlargeframeworkforanalysis. However,basedonotherstudies,asmallermodelmay
providesimilaroutput. Therefore,thisstudyconcludesthatusingMLAmaybeapplicable
andbettersuitedforanalyzingnonlinearrelationshipsamonglargeandextendedmodels.
Moreover,itshouldbenotedthatthisstudywasnotabletoguaranteethatitrepresentsan
unbiasedcrosssectionofthetargetaudiencesinceaconveniencesamplingapproachwas
usedduetothelimitationsdiscussed. Inaddition,thisstudyonlyfocusedonthosewho
arecapableandhavedrivers’licenses. Thismeansthattheoutputmaybebiasedinthe
aspectofcapablepurchasers.
Fromthisstudyoutput,perceivedenvironmentalconcernshavethehighestsignificant
directeffectonbehavioralintention,suggestingthattheenvironmentalbenefitsthatcome
with utilizing green technology increase Filipino drivers’ tendency to purchase hybrid
cars. Itisrecommendedthatcarcompaniesconsiderthestudy’sresultsanddemographics
in propagating the marketability of hybrid cars. Other researchers could use the STPB
frameworkestablishedbythestudy’sconstructsandmodeltocontextualizeandemphasize
technologicalsustainability,whichfurthervalidatestheobjectivesoftheUnitedNations’
Sustainable Development Goals (SDGs) to expedite the decarbonization of the overall
marketandtheentireeconomy.
AuthorContributions:Conceptualization,R.D.B.,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.,R.A.V.J.and
J.D.G.; methodology, R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C. and R.A.V.J.; software, R.D.B.,
A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C.andR.A.V.J.; validation, R.D.B., A.K.S.O.and J.D.G.; formal
analysis, R.D.B., A.K.S.O., L.N.Z.C., F.A.B.L., N.L.C., R.A.V.J. and J.D.G.; investigation, R.D.B.,
A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.andR.A.V.J.;resources,R.D.B.,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.
andR.A.V.J.;datacuration,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.andR.A.V.J.;writing—originaldraft
preparation,R.D.B.,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.andR.A.V.J.;writing—reviewandediting,
R.D.B.,A.K.S.O.,L.N.Z.C.,F.A.B.L.,N.L.C.,R.A.V.J.andJ.D.G.;visualization,R.D.B.,A.K.S.O.and
J.D.G.;supervision,R.D.B.,A.K.S.O.andJ.D.G.;projectadministration,R.D.B.,A.K.S.O.andJ.D.G.;
fundingacquisition,R.D.B.,A.K.S.O.andJ.D.G.Allauthorshavereadandagreedtothepublished
versionofthemanuscript.
Funding: ThisresearchwasfundedbyMapuaUniversityDirectedResearchforInnovationand
ValueEnhancement(DRIVE).
InstitutionalReviewBoardStatement: ThisstudywasapprovedbyMapuaUniversityResearch
EthicsCommittees(FM-RC-23-01-13).
InformedConsentStatement: Informedconsentwasobtainedfromallsubjectsinvolvedinthis
study(FM-RC-23-02-13).
DataAvailabilityStatement: Thedatapresentedinthisstudyareavailableonrequestfromthe
correspondingauthor.
Acknowledgments:Theauthorswouldliketothankalltherespondentswhoansweredouronline
questionnaire.Wewouldalsoliketothankourfriendsfortheircontributionstothedistributionof
thequestionnaire.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Tiseo, I. Global Transport CO Emissions Breakdown; Statista: Singapore, 2021; Available online: https://www.statista.com/
2
statistics/1185535/transport-carbon-dioxide-emissions-breakdown/(accessedon31May2023).
2. Wasiak,A.L.ModelingtheEffectsofImplementationofAlternativeWaysofVehiclePowering.Fuels2021,2,487–500.[CrossRef]
3. UnitedNations. The17Goals|SustainableDevelopment. 2015. Availableonline: https://sdgs.un.org/goals(accessedon
2January2023).
4. Irawan,M.Z.;Belgiawan,P.F.;Widyaparaga,A.;Deendarlianto;Budiman,A.;Muthohar,I.;Sopha,B.M.Amarketshareanalysis
forhybridcarsinIndonesia.CaseStud.Transp.Policy2018,6,336–341.[CrossRef]
5. Ong,A.K.S.;Cleofas,M.A.;Prasetyo,Y.T.;Chuenyindee,T.;Young,M.N.;Diaz,J.F.T.;Nadlifatin,R.;Redi,A.A.N.P.Consumer
behaviorinclothingindustryanditsrelationshipwithopeninnovationdynamicsduringtheCOVID-19pandemic.J.OpenInnov.
Technol.Mark.Complex.2021,7,211.[CrossRef]

WorldElectr.Veh.J.2023,14,227 22of26
6. Vabø,M.;Hansen,H.PurchaseintentionsforDomesticFood: Amoderatedtpb-explanation. Br. FoodJ.2016,118,2372–2387.
[CrossRef]
7. Tanwir,N.S.;Hamzah,M.I.Predictingpurchaseintentionofhybridelectricvehicles:Evidencefromanemergingeconomy.World
Electr.Veh.J.2020,11,35.[CrossRef]
8. Wang,S.;Fan,J.;Zhao,D.;Yang,S.;Fu,Y.Predictingconsumers’intentiontoadopthybridelectricvehicles:Usinganextended
versionofthetheoryofplannedbehaviormodel.Transportation2016,43,123–143.[CrossRef]
9. Javid,M.A.;Abdullah,M.;Ali,N.;Shah,S.A.H.;Joyklad,P.;Hussain,Q.;Chaiyasarn,K.Extractingtravelers’preferencestoward
electricvehiclesusingthetheoryofplannedbehaviorinLahore,Pakistan.Sustainability2022,14,1909.[CrossRef]
10. German,J.D.;Ong,A.K.S.;PerwiraRedi,A.A.N.;Robas,K.P.E.Predictingfactorsaffectingtheintentiontousea3PLduringthe
COVID-19pandemic:Amachinelearningensembleapproach.Heliyon2022,8,e11382.[CrossRef]
11. Venkatesh,V.;Thong,J.Y.L.;Xu,X.Consumeracceptanceanduseofinformationtechnology:Extendingtheunifiedtheoryof
acceptanceanduseofTechnology.MISQ.2012,36,157.[CrossRef]
12. Nordhoff,S.;Louw,T.;Innamaa,S.;Lehtonen,E.;Beuster,A.;Torrao,G.;Bjorvatn,A.;Kessel,T.;Malin,F.;Happee,R.;etal.Using
theUTAUT2modeltoexplainpublicacceptanceofconditionallyautomated(L3)cars:Aquestionnairestudyamong9118car
driversfromeightEuropeancountries.Transp.Res.PartFTrafficPsychol.Behav.2020,74,280–297.[CrossRef]
13. Prasetyo,Y.T.;Vallespin,B.E.P.DeterminingfactorsaffectingtheacceptanceofgrabapplicationinthePhilippinesusingUTAUT2
approach.InProceedingsofthe2021IEEE8thInternationalConferenceonIndustrialEngineeringandApplications(ICIEA),
Chengdu,China,23–26April2021.[CrossRef]
14. Khazaei,H.;Tareq,M.A.Moderatingeffectsofpersonalinnovativenessanddrivingexperienceonfactorsinfluencingadoptionof
BEVsinMalaysia:Anintegratedsem–BSEMapproach.Heliyon2021,7,e08072.[CrossRef]
15. Ong,A.K.S.;German,J.D.;Redi,A.A.N.P.;Cordova,L.N.Z.;Longanilla,F.A.B.;Caprecho,N.L.;Javier,R.A.V.Antecedentsof
behavioralintentionsforpurchasinghybridcarsusingsustainabilitytheoryofplannedbehaviorintegratedwithUTAUT2.
Sustainability2023,15,7657.[CrossRef]
16. LandTransportationOffice.AnnualReport2020;LandTransportationOffice—DepartmentofTransportation:Philippines,2021;
Availableonline: https://eb-production-media.s3.amazonaws.com/clients/research_paper_reports/EB-Report-BE-Manila-
Electric-Vehicles-2021-2.pdf(accessedon27January2023).
17. InternationalTradeAdministration. PhilippinesElectricVehiclesMarket. 2020. Availableonline: https://www.trade.gov/
market-intelligence/philippines-electric-vehicles-market(accessedon27January2023).
18. Canivel,R.S.C.FilipinoBuyersShifttoSmallerCars,HevsasFuelPricesSoar.Availableonline:https://business.inquirer.net/35
1026/filipino-buyers-shift-to-smaller-cars-hevs-as-fuel-prices-soar(accessedon29April2023).
19. StatistaResearchDepartmentPhilippines.ElectricVehiclesSold.2022.Availableonline:https://www.statista.com/statistics/12
50975/philippines-electric-vehicles-sold/(accessedon29June2023).
20. Visconti,K.HybridCarsNotCatchingoninPhilippines.Availableonline:https://www.rappler.com/business/10854-hybrids-
not-catching-on-in-the-philippines/#:~:text=Hybrids%20haven\T1\textquoterightt%20caught%20on,in%20terms%20of%20
hybrid%20technology%E2%80%A6(accessedon26February2023).
21. ManilaBulletinThinkaboutDrivinganElectricorHybridVehicle.Availableonline:https://mb.com.ph/2023/01/29/think-
about-driving-an-electric-or-hybrid-vehicle/(accessedon29April2023).
22. German, J.D.; Redi, A.A.N.P.; Prasetyo, Y.T.; Persada, S.F.; Ong, A.K.S.; Young, M.N.; Nadlifatin, R. Choosing a package
carrierduringCOVID-19pandemic:Anintegrationofpro-environmentalplannedbehavior(PEPB)theoryandServiceQuality
(SERVQUAL).J.Clean.Prod.2022,346,131123.[CrossRef][PubMed]
23. Fan, Y.; Chen, J.; Shirkey, G.; John, R.; Wu, S.R.; Park, H.; Shao, C.Applicationsofstructuralequationmodeling(SEM)in
EcologicalStudies:Anupdatedreview.Ecol.Process.2016,5,19.[CrossRef]
24. Woody,E.AnSEMperspectiveonevaluatingmediation:Whateveryclinicalresearcherneedstoknow.J.Exp.Psychopathol.2011,
2,210–251.[CrossRef]
25. Al-Emran,M.;Arpaci,I.;Salloum,S.A.AnempiricalexaminationofcontinuousintentiontouseM-learning: Anintegrated
model.Educ.Inf.Technol.2020,25,2899–2918.[CrossRef]
26. Ong,A.K.S.;Chuenyindee,T.;Prasetyo,Y.T.;Nadlifatin,R.;Persada,S.F.;Gumasing,M.J.J.;German,J.D.;Robas,K.P.E.;Young,
M.N.; Sittiwatethanasiri, T. Utilization of random forest and deep learning neural network for predicting factors affecting
perceivedusabilityofaCOVID-19contacttracingmobileapplicationinThailand“Thaichana”.Int.J.Environ.Res.PublicHealth
2022,19,6111.[CrossRef][PubMed]
27. Larose,R.;DeMaagd,K.;Chew,H.E.;Tsai,H.-Y.S.;Steinfield,C.;Wildman,S.S.;Bauer,J.M.Broadbandadoption|measuring
sustainablebroadbandadoption:Aninnovativeapproachtounderstandingbroadbandadoptionanduse.Int.J.Commun.2012,
6,25.[CrossRef]
28. Yuduang,N.;Ong,A.K.S.;Prasetyo,Y.T.;Chuenyindee,T.;Kusonwattana,P.;Limpasart,W.;Sittiwatethanasiri,T.;Gumasing,
M.J.J.;German,J.D.;Nadlifatin,R.Factorsinfluencingtheperceivedeffectivenessofcovid-19riskassessmentmobileapplication
“Morchana”inThailand:Utaut2approach.Int.J.Environ.Res.PublicHealth2022,19,5643.[CrossRef]
29. Hassan,I.B.;Murad,M.A.A.;El-Shekeil,I.;Liu,J.ExtendingtheUTAUT2modelwithaprivacycalculusmodeltoenhancethe
adoptionofahealthinformationapplicationinMalaysia.Informatics2022,9,31.[CrossRef]

WorldElectr.Veh.J.2023,14,227 23of26
30. Chang,C.-M.;Liu,L.-W.;Huang,H.-C.;Hsieh,H.-H.Factorsinfluencingonlinehotelbooking:ExtendingUTAUT2withage,
gender,andexperienceasmoderators.Information2019,10,281.[CrossRef]
31. Ajzen,I.Thetheoryofplannedbehavior.Organ.Behav.Hum.Decis.Process.1991,50,179–211.[CrossRef]
32. Shiau,W.-L.;Chau,P.Y.K.Understandingbehavioralintentiontouseacloudcomputingclassroom:Amultiplemodelcomparison
approach.Inf.Manag.2016,53,355–365.[CrossRef]
33. Sentosa,I.Theintegrationoftheoryofplannedbehavior(TPB)andtechnologyacceptancemodelininternetpurchasing: A
structuralequationmodeling(SEM)approach.InProceedingsoftheAppliedInternationalBusinessConference,KualaLumpur,
Malaysia,30June–2July2008.
34. Kim,J.J.;Hwang,J.Mergingthenormactivationmodelandthetheoryofplannedbehaviorinthecontextofdronefooddelivery
services:Doesthelevelofproductknowledgereallymatter?J.Hosp.Tour.Manag.2020,42,1–11.[CrossRef]
35. Elkington,J.;Rowland,I.H.Cannibalswithforks:Thetriplebottomlineof21st-centurybusiness.Altern.J.1999,25,42–43.
36. Friedman,L.;Cobb,E.C.ImpactofHybridCars;WorcesterPolytechnicInstitute:Worcester,MA,USA,2010.
37. Su,C.-W.;Yuan,X.;Tao,R.;Umar,M.Cannewenergyvehicleshelptoachievecarbonneutralitytargets?J.Environ.Manag.2021,
297,113348.[CrossRef][PubMed]
38. Korchinski,W.FuelingAmerica: Howhydrogencarsaffecttheenvironment. ReasonFound. PolicyStudy2004,322. Available
online:https://www.policyarchive.org/handle/10207/5741(accessedon18July2023).
39. Asim,N.;Bimani,A.A.;Saqri,A.A.;Matriano,M.Thesocialandenvironmentalimpactofhybridcars.Int.J.Res.Entrep.Bus.
Stud.2020,1,36–47.[CrossRef]
40. James, P.; Magee, L. Domains of sustainability. Glob. Encycl. Public Adm. Public Policy Gov. 2016, 1–17. Available online:
https://link.springer.com/referenceworkentry/10.1007/978-3-319-31816-5_2760-1(accessedon18July2023).
41. He,L.;Wang,M.;Chen,W.;Conzelmann,G.IncorporatingsocialimpactonnewproductadoptioninChoicemodeling:Acase
studyingreenvehicles.Transp.Res.PartDTransp.Environ.2014,32,421–434.[CrossRef]
42. Turon´,K.;Kubik,A.Economicaspectsofdrivingvarioustypesofvehiclesinintelligenturbantransportsystems,including
CAR-sharingservicesandAutonomousVehicles.Appl.Sci.2020,10,5580.[CrossRef]
43. Nisa,C.F.;Bélanger,J.J.;Faller,D.G.;Buttrick,N.R.;Mierau,J.O.;Austin,M.M.K.;Schumpe,B.M.;Sasin,E.M.;Agostini,M.;
Gützkow,B.;etal. Livesversuslivelihoods? perceivedeconomicriskhasastrongerassociationwithsupportforCOVID-19
preventivemeasuresthanperceivedhealthrisk.Sci.Rep.2021,11,9669.[CrossRef][PubMed]
44. Klöckner,C.A.;Matthies,E.Howhabitsinterferewithnorm-directedbehaviour:Anormativedecision-makingmodelfortravel
modechoice.J.Environ.Psychol.2004,24,319–327.[CrossRef]
45. Sandqvist,K.TheAppealofAutomobiles:HumanDesiresandtheProliferationofCars.Availableonline:https://trid.trb.org/
view/567975(accessedon8May2023).
46. Tengstrom,R.TheUseoftheAutomobile: ItsImplicationsforMan,Society,andtheEnvironment. Availableonline: https:
//trid.trb.org/view/386217(accessedon8May2023).
47. Crabbe,M.;Standing,C.;Standing,S.;Karjaluoto,H.AnadoptionmodelformobilebankinginGhana. Int. J.Mob. Commun.
2009,7,515.[CrossRef]
48. Zeithaml,V.A.Consumerperceptionsofprice,quality,andvalue:Ameans-endmodelandsynthesisofevidence.J.Mark.1988,
52,2.[CrossRef]
49. Onwezen,M.C.;Antonides,G.;Bartels,J.Thenormactivationmodel:Anexplorationofthefunctionsofanticipatedprideand
guiltinpro-environmentalbehaviour.J.Econ.Psychol.2013,39,141–153.[CrossRef]
50. Rezvani,Z.;Jansson,J.;Bodin,J.Advancesinconsumerelectricvehicleadoptionresearch:Areviewandresearchagenda.Transp.
Res.PartDTransp.Environ.2015,34,122–136.[CrossRef]
51. Schuitema,G.;Anable,J.;Skippon,S.;Kinnear,N.Theroleofinstrumental,hedonicandsymbolicattributesintheintentionto
adoptelectricvehicles.Transp.Res.PartAPolicyPract.2013,48,39–49.[CrossRef]
52. Pikkarainen, T.; Pikkarainen, K.; Karjaluoto, H.; Pahnila, S. Consumer acceptance of online banking: An extension of the
TechnologyAcceptanceModel.InternetRes.2004,14,224–235.[CrossRef]
53. Manutworakit,P.;Choocharukul,K.FactorsinfluencingbatteryelectricvehicleadoptioninThailand—Expandingtheunified
theoryofacceptanceanduseoftechnology’svariables.Sustainability2022,14,8482.[CrossRef]
54. Davis,F.D.;Bagozzi,R.P.;Warshaw,P.R.Useracceptanceofcomputertechnology: Acomparisonoftwotheoreticalmodels.
Manag.Sci.1989,35,982–1003.[CrossRef]
55. Gunawan,I.;Redi,A.A.N.P.;Santosa,A.A.;Maghfiroh,M.F.N.;Pandyaswargo,A.H.;Kurniawan,A.C.Determinantsofcustomer
intentionstouseelectricvehicleinIndonesia:Anintegratedmodelanalysis.Sustainability2022,14,1972.[CrossRef]
56. Ombach,G.DesignconsiderationsforWirelessChargingSystemforelectricandplug-inhybridvehicles.InProceedingsofthe
HybridandElectricVehiclesConference2013(HEVC2013),London,UK,6–7November2013.
57. Alalwan,A.A.;Dwivedi,Y.K.;Rana,N.P.;Algharabat,R.ExaminingfactorsinfluencingJordaniancustomers’intentionsand
adoptionofinternetbanking:ExtendingUTAUT2withrisk.J.Retail.Consum.Serv.2018,40,125–138.[CrossRef]
58. Venkatesh,V.;Morris,M.G.;Davis,G.B.;Davis,F.D.Useracceptanceofinformationtechnology:Towardaunifiedview.MISQ.
2003,27,425.[CrossRef]
59. Morosan,C.;DeFranco,A.It’sAbouttime:Revisitingutaut2toexamineconsumers’intentionstouseNFCmobilepaymentsin
hotels.Int.J.Hosp.Manag.2016,53,17–29.[CrossRef]

WorldElectr.Veh.J.2023,14,227 24of26
60. Lin,S.-C.;Nadlifatin,R.;Amna,A.R.;Persada,S.F.;Razif,M.Investigatingcitizenbehaviorintentiononmandatoryandvoluntary
Pro-Environmentalprogramsthroughapro-environmentalplannedbehaviormodel.Sustainability2017,9,1289.[CrossRef]
61. Pearson.DOEPushesforFasterelectricVehicleRolloutinthePhilippines.Availableonline:https://www.philstar.com/nation/
2023/06/05/2271616/doe-pushes-faster-electric-vehicle-rollout-philippines(accessedon8May2023).
62. Racz,A.A.;Muntean,I.;Stan,S.-D.Alookintoelectric/hybridcarsfromanecologicalperspective. ProcediaTechnol. 2015,19,
438–443.[CrossRef]
63. BarbosaJunior,M.;Pinheiro,E.;Sokulski,C.C.;RamosHuarachi,D.A.;deFrancisco,A.C.Howtoidentifybarrierstotheadoption
ofsustainableagriculture?astudybasedonamulti-criteriamodel.Sustainability2022,14,13277.[CrossRef]
64. Saif,M.A.M.;Hussin,N.;Husin,M.M.;Alwadain,A.;Chakraborty,A.Determinantsoftheintentiontoadoptdigital-onlybanks
inMalaysia:Theextensionofenvironmentalconcern.Sustainability2022,14,11043.[CrossRef]
65. PhilippineStatisticsAuthority.Goal7.EnsureEnvironmentalSustainability.2021.Availableonline:https://psa.gov.ph/sdg/
about#:~:text=The%20Sustainable%20Development%20Goals%20(SDGs,targets%20and%20232%20unique%20indicators(ac-
cessedon12February2023).
66. Mufidah,I.;Jiang,B.C.;Lin,S.-C.;Chin,J.;Rachmaniati,Y.P.;Persada,S.F.Understandingtheconsumers’behaviorintentionin
usinggreenecolabelproductthroughPro-Environmentalplannedbehaviormodelindevelopinganddevelopedregions:Lessons
learnedfromTaiwanandIndonesia.Sustainability2018,10,1423.[CrossRef]
67. Galloway,A.Non-probabilitysampling. InEncyclopediaofSocialMeasurement;Elsevier: Amsterdam,TheNetherlands,2005;
pp.859–864.
68. Kirchherr,J.;Charles,K.EnhancingthesamplediversityofSnowballSamples:Recommendationsfromaresearchprojecton
anti-dammovementsinSoutheastAsia.PLoSONE2018,13,e0201710.[CrossRef]
69. Hair,J.F.MultivariateDataAnalysis:AGlobalPerspective;PearsonPrenticeHall:UpperSaddleRiver,NJ,USA,2010.
70. Yang,W.;Zhou,S.Usingdecisiontreeanalysistoidentifythedeterminantsofresidents’CO2emissionsfromdifferenttypesof
trips:AcasestudyofGuangzhou,China.J.Clean.Prod.2020,277,124071.[CrossRef]
71. Wu,D.J.;Feng,T.;Naehrig,M.;Lauter,K.Privatelyevaluatingdecisiontreesandrandomforests. Cryptol. ePrintArch. 2015.
Availableonline:https://math.berkeley.edu/~fengt/decision_tree.pdf(accessedon18July2023).[CrossRef]
72. Bordarie,J.Predictingintentionstocomplywithspeedlimitsusinga‘decisiontree’appliedtoanextendedversionofthetheory
ofplannedbehaviour.Transp.Res.PartFTrafficPsychol.Behav.2019,63,174–185.[CrossRef]
73. Charbuty,B.;Abdulazeez,A.ClassificationBasedonDecisionTreeAlgorithmforMachineLearning.J.Appl.Sci.Technol.Trends
2021,2,20–28.[CrossRef]
74. Milani,L.;Grumi,S.;Camisasca,E.;Miragoli,S.;Traficante,D.;DiBlasio,P.FamilialriskandprotectivefactorsaffectingCPS
Professionals’ChildRemovalDecision:Adecisiontreeanalysisstudy.Child.YouthServ.Rev.2020,109,104687.[CrossRef]
75. Ong,A.K.S.;Kurata,Y.B.;Castro,S.A.D.G.;DeLeon,J.P.B.;DelaRosa,H.V.;Tomines,A.P.J.Factorsinfluencingtheacceptanceof
telemedicineinthePhilippines.Technol.Soc.2022,70,102040.[CrossRef]
76. Topîrceanu,A.;Grosseck,G.Decisiontreelearningusedfortheclassificationofstudentarchetypesinonlinecourses.Procedia
Comput.Sci.2017,112,51–60.[CrossRef]
77. Harwati;Sudiya,A.Applicationofdecisiontreeapproachtostudentselectionmodel—Acasestudy.IOPConf.Series:Mater.Sci.
Eng.2016,105,012014.[CrossRef]
78. Chen,J.;Li,Q.;Wang,H.;Deng,M.AmachinelearningensembleapproachbasedonRandomForestandradialbasisfunction
neuralnetworkforriskevaluationofRegionalFloodDisaster:Acasestudyoftheyangtzeriverdelta,China.Int.J.Environ.Res.
PublicHealth2019,17,49.[CrossRef][PubMed]
79. Schnebly,J.; Sengupta,S.Randomforesttwitterbotclassifier. InProceedingsofthe2019IEEE9thAnnualComputingand
CommunicationWorkshopandConference(CCWC),LasVegas,NV,USA,7–9January2019.
80. Ong,A.K.S.;Prasetyo,Y.T.;Velasco,K.E.C.;Abad,E.D.R.;Buencille,A.L.B.;Estorninos,E.M.;Cahigas,M.M.L.;Chuenyindee,T.;
Persada,S.F.;Nadlifatin,R.;etal.Utilizationofrandomforestclassifierandartificialneuralnetworkforpredictingtheacceptance
ofreopeningdecommissionednuclearpowerplant.Ann.Nucl.Energy2022,175,109188.[CrossRef]
81. Chen,Y.-S.;Chang,T.-W.;Li,H.-X.;Chen,Y.-R.TheinfluenceofGreenbrandaffectonGreenPurchaseIntentions:Themediation
effectsofgreenbrandassociationsandGreenbrandattitude.Int.J.Environ.Res.PublicHealth2020,17,4089.[CrossRef]
82. Rodriguez-Galiano,V.F.;Ghimire,B.;Rogan,J.;Chica-Olmo,M.;Rigol-Sanchez,J.P.Anassessmentoftheeffectivenessofa
randomforestclassifierforland-coverclassification.ISPRSJ.Photogramm.RemoteSens.2012,67,93–104.[CrossRef]
83. Elhenawy,M.;Rakha,H.A.;El-Shawarby,I.Enhancedmodelingofdriverstop-or-runactionsatayellowindication.Transp.Res.
Rec.J.Transp.Res.Board2014,2423,24–34.[CrossRef]
84. Ermagun,A.;Rashidi,T.H.;Lari,Z.A.Modechoiceforschooltrips. Transp. Res. Rec. J.Transp. Res. Board2015,2513,97–105.
[CrossRef]
85. Casini,M.BuildingAutomationSystems.Constr.4.02022,525–581.[CrossRef]
86. Sturman,O.;vonZiegler,L.;Schläppi,C.;Akyol,F.;Privitera,M.;Slominski,D.;Grimm,C.;Thieren,L.;Zerbi,V.;Grewe,B.;etal.
Deep learning-based behavioral analysis reaches human accuracy and is capable of outperforming commercial solutions.
Neuropsychopharmacology2020,45,1942–1952.[CrossRef]
87. Luceri,L.;Braun,T.;Giordano,S.Analyzingandinferringhumanreal-lifebehaviorthroughonlinesocialnetworkswithsocial
influenceDeepLearning.Appl.Netw.Sci.2019,4,34.[CrossRef]

WorldElectr.Veh.J.2023,14,227 25of26
88. Pradhan,B.;Lee,S.LandslidesusceptibilityassessmentandFactorEffectAnalysis:Backpropagationartificialneuralnetworks
andtheircomparisonwithFrequencyRatioandbivariatelogisticregressionmodelling.Environ.Model.Softw.2010,25,747–759.
[CrossRef]
89. Gudivada,V.N.Naturallanguagecoretasksandapplications.InHandbookofStatistics;Elsevier:Amsterdam,TheNetherlands,
2018;pp.403–428.[CrossRef]
90. Walrave,M.;Waeterloos,C.;Ponnet,K.Readyornotforcontacttracing? investigatingtheadoptionintentionofCOVID-19
contact-tracingtechnologyusinganextendedunifiedtheoryofacceptanceanduseofTechnologyModel.Cyberpsychol.Behav.Soc.
Netw.2021,24,377–383.[CrossRef]
91. DeRyck,T.;Lanthaler,S.;Mishra,S.OntheapproximationoffunctionsbyTanhneuralnetworks.NeuralNetw.2021,143,732–750.
[CrossRef][PubMed]
92. Costarelli,D.NeuralNetworkOperators: Constructiveinterpolationofmultivariatefunctions. NeuralNetw. 2015,67,28–36.
[CrossRef]
93. Liébana-Cabanillas,F.;Marinkovic´,V.;Kalinic´,Z.ASEM-neuralnetworkapproachforpredictingantecedentsofM-Commerce
Acceptance.Int.J.Inf.Manag.2017,37,14–24.[CrossRef]
94. Narayan,S.Thegeneralizedsigmoidactivationfunction:Competitivesupervisedlearning.Inf.Sci.1997,99,69–82.[CrossRef]
95. Li,J.;Sawaragi,T.;Horiguchi,Y.Introducestructuralequationmodellingtomachinelearningproblemsforbuildinganexplainable
andpersuasivemodel.SICEJ.Control.Meas.Syst.Integr.2021,14,67–79.[CrossRef]
96. Hadiyat,M.A.Combinedstructuralequationmodelling—Artificialneuralnetworksmodelforpredictingcustomerloyalty.IOP
Conf.Ser.Mater.Sci.Eng.2019,703,012024.[CrossRef]
97. Rossi,C.;Rivetti,F.Assessingyoungconsumers’responsestosustainablelabels:InsightsfromafactorialexperimentinItaly.
Sustainability2020,12,10115.[CrossRef]
98. Bedard,S.A.N.;Tolmie,C.R.Millennials’greenconsumptionbehaviour:ExploringtheroleofSocialMedia.Corp.Soc.Responsib.
Environ.Manag.2018,25,1388–1396.[CrossRef]
99. Nadlifatin,R.;Lin,S.-C.;Rachmaniati,Y.P.;Persada,S.F.;Razif,M.Apro-environmentalreasonedactionmodelformeasuring
citizens’intentionsregardingecolabelproductusage.Sustainability2016,8,1165.[CrossRef]
100. Ajzen,I.Perceivedbehavioralcontrol,self-efficacy,locusofcontrol,andthetheoryofplannedbehavior1.J.Appl.Soc.Psychol.
2002,32,665–683.[CrossRef]
101. Cahigas,M.M.;Prasetyo,Y.T.;Persada,S.F.;Ong,A.K.S.;Nadlifatin,R.Understandingtheperceivedbehaviorofpublicutility
buspassengersduringtheeraofCOVID-19pandemicinthePhilippines:Applicationofsocialexchangetheoryandtheoryof
plannedbehavior.Res.Transp.Bus.Manag.2022,45,100840.[CrossRef]
102. Chong, Y.T.; Teo, K.M.; Tang, L.C. A lifecycle-based sustainability indicator framework for waste-to-energy systems and a
proposedmetricofsustainability.Renew.Sustain.EnergyRev.2016,56,797–809.[CrossRef]
103. Foroughi,B.;Nhan,P.V.;Iranmanesh,M.;Ghobakhloo,M.;Nilashi,M.;Yadegaridehkordi,E.Determinantsofintentiontouse
AutonomousVehicles:FindingsfromPLS-semandANFIS.J.Retail.Consum.Serv.2023,70,103158.[CrossRef]
104. Yang,X.Understandingconsumers’purchaseintentionsinsocialcommercethroughsocialcapital: Evidencefromsemand
fsQCA.J.Theor.Appl.Electron.Commer.Res.2021,16,1557–1570.[CrossRef]
105. Yazdanpanah, M.; Hadji Hosseinlou, M. The role of personality traits through habit and intention on determining future
preferencesofpublictransportuse.Behav.Sci.2017,7,8.[CrossRef]
106. Lallmahomed, M.Z.; Lallmahomed, N.; Lallmahomed, G.M. Factors influencing the adoption of e-government services in
Mauritius.Telemat.Inform.2017,34,57–72.[CrossRef]
107. Brown,S.A.;Venkatesh,V.Modelofadoptionoftechnologyinhouseholds:Abaselinemodeltestandextensionincorporating
householdlifecycle.MISQ.2005,29,399.[CrossRef]
108. Palau-Saumell,R.;Forgas-Coll,S.;Sánchez-García,J.;Robres,E.Useracceptanceofmobileappsforrestaurants:Anexpanded
andextendedutaut-2.Sustainability2019,11,1210.[CrossRef]
109. Lane,B.;Potter,S.TheadoptionofcleanervehiclesintheUK:Exploringtheconsumerattitude–actiongap.J.Clean.Prod.2007,
15,1085–1092.[CrossRef]
110. Chaveesuk,S.;Khalid,B.;Bsoul-Kopowska,M.;Rostan´ska,E.;Chaiyasoonthorn,W.Comparativeanalysisofvariablesthat
influencebehavioralintentiontousemoocs.PLoSONE2022,17,e0262037.[CrossRef][PubMed]
111. Albert,J.R.G.;Santos,A.G.F.;Vizmanos,J.F.V.ProfileandDeterminantsoftheMiddle-IncomeClassinthePhilippines;Philippine
InstituteforDevelopmentStudies:LegaspiVillage,Philippines,2018.
112. Nordfjærn, T.; S¸ims¸ekog˘lu, Ö.; Rundmo, T. The role of deliberate planning, car habit and resistance to change in public
transportationmodeuse.Transp.Res.PartFTrafficPsychol.Behav.2014,27,90–98.[CrossRef]
113. Agaton, C.B.; Collera, A.A.; Guno, C.S. Socio-economic and environmental analyses of sustainable public transport in the
Philippines.Sustainability2020,12,4720.[CrossRef]
114. Yuriev,A.; Dahmen,M.; Paillé,P.; Boiral,O.; Guillaumie,L.Pro-environmentalbehaviorsthroughthelensofthetheoryof
plannedbehavior:Ascopingreview.Resour.Conserv.Recycl.2020,155,104660.[CrossRef]

WorldElectr.Veh.J.2023,14,227 26of26
115. Wang,Z.;Dong,X.;Yin,J.Antecedentsofurbanresidents’separatecollectionintentionsforhouseholdsolidwasteandtheir
willingnesstopay:EvidencefromChina.J.Clean.Prod.2018,173,256–264.[CrossRef]
116. Zadjafar,M.A.;Gholamian,M.R.AsustainableinventorymodelbyconsideringEnvironmentalErgonomicsandenvironmental
pollution,casestudy:PulpandPapermills.J.Clean.Prod.2018,199,444–458.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.