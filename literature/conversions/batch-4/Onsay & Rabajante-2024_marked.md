---
conversion_metadata:
  converted_at: "2026-07-21T07:58:02Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Onsay & Rabajante-2024.pdf"
  source_pdf_sha256: "2d6ff8c50c14e7f0f51867d6d6a4f207684caf4e6087f03e1235435ba2827a43"
  page_count: 14
  markdown_char_count: 46649
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Science Talks 11 (2024) 100387

Contents lists available at ScienceDirect

Science Talks

j o u r n a l h o m e p a g e : w w w . e l s e v i e r . e s / s c t a l k

When machine learning meets econometrics: Can it build a better measure
to predict multidimensional poverty and examine unmeasurable economic
conditions?
Emmanuel A. Onsay a,b,⁎

, Jomar F. Rabajante a
a Graduate School, University of the Philippines Los Baños, Laguna 4030, Philippines
b Partido Institute of Economics, Partido State University, Camarines Sur 4422, Philippines

A R T I C L E

I N F O

A B S T R A C T

Keywords:
Machine learning
Econometrics
Multidimensional poverty
Indigenous people
Economic development
Poverty alleviation

Poverty is as old as human civilization, hard to eradicate, multidimensional, and difﬁcult to measure. The methods
used to measure poverty today are costly, labor-intensive, and time-consuming. Therefore, policymakers ﬁnd it difﬁ-
cult to target policies when putting poverty reduction initiatives into action. Indigenous communities are among the
most disadvantaged and vulnerable populations in society. Their socioeconomic situations are complex and multifac-
eted. While research on poverty is usually generic, prone to large sampling errors, and intended to guide national pol-
icy, research on indigenous people is qualitative. Thus, to measure multidimensional poverty with disaggregated
techniques, this work blends machine learning and econometrics. Researchers who have been studying poverty world-
wide can replicate all of the approaches, strategies, and resources used in this study. With the best R-square and accu-
racy, random forest models perform better than all regressors and classiﬁers combined. It also conﬁrms the causal
relationship and current econometric association between multidimensional characteristics and poverty conse-
quences. This study demonstrates the viability of using machine learning to predict poverty in a way that can save
costs, cut labor, and maximize time to empower indigenous communities and alleviate the poverty of impoverished
societies in the poorest region of Luzon, Philippines.

Video and Presentations to this article can be found online at https://

doi.org/10.1016/j.sctalk.2024.100387.

⁎

Corresponding author at: Graduate School, University of the Philippines Los Baños, Laguna 4030, Philippines.
E-mail address: eaonsay@up.edu.ph (E.A. Onsay).

http://dx.doi.org/10.1016/j.sctalk.2024.100387
Received 4 March 2024; Received in revised form 12 July 2024; Accepted 18 July 2024
2772-5693/© 2024 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

---

<!-- PAGE 2 -->

E.A. Onsay, J.F. Rabajante

Figures and tables

Science Talks 11 (2024) 100387

Fig. 1. Comprehensive poverty analytics at disaggregated approaches.

2

---

<!-- PAGE 3 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

Abucayan is the most impoverished locality. San Jose, San Benito, and
Panday have the fewest impoverished households. While poverty is wide-
spread in the Isarog Sector, it is not as severe in the Poblacion community.
Watt's Index claims that Isarog communities have a greater prevalence of
poverty. Poor households and people are reﬂected through poverty inci-
dence, which represents the headcount ratio of those living below the pov-
erty line and food thresholds in the Philippines, relative to the total number
of households and population [1,2,11,18,21].

Fig. 2. Results of multidimensional poverty evaluation at disaggregation and combination through the multiple constructs and indicators.

About 63.70% of people live in poverty and 51.10% of individuals do
not have access to food. The dynamics of education, income, and health
all clearly demonstrate poverty. In the Philippines, households with a
monthly income of PhP10,481 (about 186.18 USD) and below for a family
of ﬁve are considered poor. It is important to consider that different regions
may have different poverty lines, so it is pre-requisite to identify the poverty
line in your area before applying our suggested ML models. Multidimen-
sional Poverty deprivation refers to the 15 economic variables that we
have employed, which serve as predictors or independent variables in our
econometric and machine learning models. It offers a more comprehensive
approach. Instead of using an index, we employ binary and dummy data to
capture non-linear relationships [1,2,21,23].

3

---

<!-- PAGE 4 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

Fig. 3. Classiﬁcation results and predictive margins of multidimensional variables.

As a factor impacting health dynamics, the results indicate that house-
hold size is a strong predictor of poverty. Poverty is more likely to be expe-
rienced by informal settlers than by formal settlers. Furthermore, the
chance of falling into poverty increases with the number of household
members [1,2,6,20,24].

Fig. 4. Average root means square error of machine learning regressors for impoverished societies.

4

---

<!-- PAGE 5 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

With an RMSE of 0.3298, the random forest method performs better
than the others, LightGBM at 0.3642 and XGBoost at 0.4001. These results
are derived from ML models (regressors) displayed on video slides 15 and
17. The reason why random forest performed the best is that it can identify
explanatory factors, ﬁnd nonlinear correlations between explanatory and
dependent variables, and estimate feature importance, which provides in-
sight into the features that have the greatest inﬂuence on the categorization
process. Although the outcome of machine learning (ML) is dependent on
the context of the data, results from ML applied to similar datasets and
models in other locations would be comparable. Maybe the only things
that would change are the predictors. The ML model is sustainable in this
way since it requires a large amount of data, and the data we utilized is
available in the Philippines every two years after the census. Furthermore,
even with cross-sectional data, different regions can apply machine
learning once the data is accessible for them, because a medium-term social
outcome can be predicted by an ML model [1,2,19,10,15].

Fig. 5. Average mean square error of machine learning regressors for impoverished societies.

5

---

<!-- PAGE 6 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

For the entire municipality, the random forest regression algorithm has
the lowest mean square error, at 0.0792. XGBoost (0.4722) and LightGBM
(0.1242) are in its wake. The ML models we used are speciﬁc to the areas
we studied. Therefore, we initially employed econometrics to identify
proper predictors for ML models that are speciﬁc to our local context. How-
ever, the poverty models (logistic) and the ML models (regressors and clas-
siﬁers) are generic and can be applied to other regions or countries.
Consequently, repeatability is highly feasible in this regard. Other regions
of the world would need to identify their own predictors, but the models
we used could also work for them [1,2,15,22].

Fig. 6. Average R-square of machine learning regressors for impoverished societies.

With an R-square of 0.4221, the linear regression has the lowest value.
The random forest regressor produced the highest R-square, 0.92075. It
suggests that the regression that best matches the regression line and has
the lowest error score is the random forest regression. Since the data exam-
ined in this paper is based on a comprehensive census of all populations in-
cluding indigenous people, there are no known limits. As a result, it remains
exempt to sampling error and upholds the sample assumptions of internal
and external validity. The writers thoroughly examine and ﬁlter the data's
multidimensional variables. The dataset is well-sized and devoid of well-
known biases. But time is of the essence. It takes time to create trustworthy
and veriﬁable datasets and models [1,2,12,13,14].

6

---

<!-- PAGE 7 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

Fig. 7. Performance evaluation of machine learning regressors for impoverished societies.

With an accuracy of 0.9108, the random forest regression classiﬁer has
the highest performance. The algorithms with the lowest accuracy are Bag-
ging (0.8437) and Decision Tree (0.8418). The R-squares for the SVM,
AdaBoost, Gaussian NB, and Perceptron are 0.86–0.87. The random forest
classiﬁcation has the greatest accuracy rate of 95.94% in pipeline algo-
rithms. Concerning the future improvements, the utilization of econometric
models and predictive analytics datasets has the potential to generate em-
pirical data that strengthens poverty theories that apply to entire popula-
tions, including indigenous populations. This would contribute to the
existing body of knowledge about the dearth of multidimensional poverty
metrics in developing nations like the Philippines, especially for indigenous
populations. Applying the models to all other tribes in the nation and utiliz-
ing artiﬁcial neural networks could both enhance forecast accuracy and
yield improvements [1,2,8,16,17].

7

---

<!-- PAGE 8 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

Fig. 8. Indigenous communities' population analytics.

Indigenous people make up about 11.84% of all households in Goa,
Camarines Sur. San Pedro Aroro, Payatan, and Balaynan are the most pop-
ulous indigenous tribes, with respective total population distributions of
92.50%, 68.66%, and 46.30% [3,4,7,11].

8

---

<!-- PAGE 9 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

Fig. 9. Multidimensional socioeconomic evaluation and poverty examination of indigenous people tribes.

There are 1660 houses of indigenous people and 8022 persons in total.
Eighty-two percent of people live in poverty, and 71% do not have access to
food. Evaluation results for schooling are largely constant throughout
barangays, suggesting that most children in the neighborhood are not en-
rolled in school or have stopped enrolling as educational levels rise
[3,4,7,11,18].

9

---

<!-- PAGE 10 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

Fig. 10. Indigenous people poverty analytics.

The Poorest tribe is the Abucayan Tribe while the Least Poor tribe is the

Salog Tribe [1,3,4,21,23].

Fig. 11. IP Classiﬁcation Prediction Margins.

Living below the poverty level is more common among IP informal set-
tlers. Moreover, the probability of poverty increases with the number of
household members. The results of the Estat categorization are positive.
Overall, 86.14% of cases were appropriately classiﬁed [3,4,5,9,25].

10

---

<!-- PAGE 11 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

Fig. 12. Average mean square error (MSE) of machine learning regressors in IP modeling.

After LightGBM and XGBoost, the random forest regression method has
the lowest mean square error (0.5497). Causality tests using econometrics
(logit and probit regression) were initially performed to identify predictors
for the ML models. All the multidimensional indicators used in the model
(Fig. 9) and reﬂected in the video have a causal relationship with poverty
for IP groups. The following variables have been found to have causality:
Health and Nutrition, Housing, Water and Sanitation, Basic Education, In-
come and Livelihood, and Peace and Order. Since these variables are caus-
ally linked to poverty, they serve as predictors in the ML models. Given that
these variables have a causal relationship and are predictors of poverty in
the models, our policy mapping and targeting analysis focuses on these var-
iables. We concentrate on addressing these variables in order to improve
policies, as doing so would alleviate poverty and promote development
[3,4,15,22].

11

---

<!-- PAGE 12 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

Fig. 13. Average R-square of machine learning regressors for Indigenous Communities.

Of all the techniques, linear regression has the lowest R-square, at
0.4222. Next are a polynomial algorithm and an SVR. With an R-square
of 0.9208, the random forest regressor produced the highest results, al-
though CatBoost, XGBoost, and LightGBM all performed similarly. It im-
plies that the random forest regression is the one that most closely
resembles the regression line and has the lowest error score [3,4,12,13,14].

12

---

<!-- PAGE 13 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

Fig. 14. Performance evaluation of ML classiﬁers at random and pipeline for IP.

For all tribes at random (α), the random forest regression classiﬁer has
the highest accuracy (90.69%); K-Nearest Neighbour, Gradient Boost, and
Logistic follow. At pipeline (Ω), the random forest classiﬁcation has the
greatest accuracy rate at 94.89%. The next two classiﬁcation strategies are
gradient boost and logistic. The results afﬁrm that all 15 indicators serve
as predictors of poverty, and the random forest algorithm emerges as the
most effective model for poverty prediction. Therefore, it is crucial to ad-
dress all these indicators adequately since they are the root causes of poverty.
By formulating policies that target each predictor, poverty can be alleviated,
leading to advancements in economic development [3,4,8,16,17].

CRediT authorship contribution statement

Emmanuel A. Onsay: Writing – original draft, Visualization, Valida-
tion, Project administration, Methodology, Investigation, Funding acquisi-
tion, Formal analysis, Data curation, Conceptualization. Jomar F.
Rabajante: Writing – review & editing, Validation, Supervision, Software,
Resources, Project administration, Methodology, Funding acquisition,
Formal analysis, Conceptualization.

Data availability

We have shared our data publicly. The links to our datasets were pro-

vided through the references section (Ref. 1, 2, 3, 4)

Acknowledgments

We would like to express our profound gratitude to the following orga-
nizations and individuals for their vital support of our research: Elsevier's
Science Talks for providing us a platform to disseminate our study's re-
views through video presentation, which support economic development
and poverty alleviation; University of the Philippines Los Baños
Graduate School for research development and analysis; Partido State
University for ﬁnancial and logistic support; De La Salle University
School of Economics for insightful feedback and review; and LGU Goa
Camarines Sur for providing the necessary data. In terms of authorization
and logistical support, we would like to express our sincere appreciation to
Hon. Pan, Marcel S., Engr. Moriel Prado, Ms. Prese Bradecina, Mr. Rafael
Belleza, Mr. Jude Zair C. Paladan, Ms. Keschei Joana Villar Cañaveras,
Mr. Herman B. Jungco II, Mr. Chris Ocampo, and Mr. Jobert Ronabio.
We also admire Prof. Jerrold Tubay and Prof. Neil Jerome Egarquin for
in mathematical analysis, and we owe Prof. Jason
their support
Alinsunurin and Prof. Jefferson Arapoc for their help with econometrics.
We are deeply grateful to Prof. Eva Marie Aragones and Prof. Alellie
Sobreviñas for their invaluable contributions to the poverty models. We
very much appreciate the invaluable assistance with editing, curation,
and logistics provided by Prof. Rolan Jon G. Bulao, Sir Kevin C. Baltar,
Mr. Mark Rey Pardiñas, Ms. Spotty Kankan, Mr. Jack Noy, Mr. King Ukay,
and Ms. Sakura Kok. Furthermore, we are incredibly grateful to the policy-
representatives, and stakeholders who have
makers, government

13

---

<!-- PAGE 14 -->

E.A. Onsay, J.F. Rabajante

Science Talks 11 (2024) 100387

contributed signiﬁcant insights and feedback to develop and implement
policy solutions. Ultimately, we give the Almighty God the highest praise
for knowledge, power, and wisdom.

Funding

This work was supported by the Partido State University (Poverty Alle-
viation and Economic Development Project 2022–2025) and University of
the Philippines Los Baños (Graduate School 2023–2025).

Ethics statement

All graphs and ﬁgures presented in this work were produced and visual-
ized by the authors. The utilization of all photos in the video presentation
has obtained formal consent from the subject, university, government,
and stakeholders. The conduct of this study was approved by Partido State
University and the University of the Philippines Los Baños. The Goa,
Camarines Sur Local Government Unit gave permission for the results of
the processed data to be used, manipulated, analyzed, and communicated.
Researchers voluntarily conduct the data analysis and procedures; they are
not a component of any experiment. Our human data are secondary, indi-
rect, and socioeconomic in nature; they don't entail any laboratory work.
Thus, ethical clearances are not required. Furthermore, this study does
not involve any animal testing, direct human volunteers, or data acquired
from social media platforms.

Declaration of interests

The authors declare that they have no known competing ﬁnancial inter-
ests or personal relationships that could have appeared to inﬂuence the
work reported in this paper.

References

[1] E.A. Onsay, J. Rabajante, Measuring the unmeasurable multidimensional poverty for
economic development: datasets, algorithms, and models from the poorest region of
Luzon, Philippines, Data Brief J. (2024), https://doi.org/10.1016/j.dib.2024.110150.
[2] Emmanuel Onsay, Jomar Rabajante, Dataset on measuring the unmeasurable multidi-
mensional rural poverty for economic development: analysis from the poorest district
of the poorest province in the poorest region of Luzon, Philippines, Mendeley Data V1
(2023), https://doi.org/10.17632/s76nh7dm4v.1.

[3] Emmanuel A. Onsay, “Poverty proﬁle and health dynamics of indigenous people.” Int

rev, Soc. Sci. Res. 2 (2022) 1–27.

[4] Emmanuel Onsay, Jomar Rabajante, Measuring the Unmeasurable Socio-Economic
Conditions and Multidimensional Poverty of Indigenous People: Datasets from the
Poorest Region of Luzon, Philippines, vol. V1, Harvard Dataverse, 2023, https://doi.
org/10.7910/DVN/QSZKUP.

[5] John H. Aldrich, Forrest D. Nelson, Linear Probability, Logit, and Probit Models, vol. 45,

Sage, 1984.

[6] Sabina Alkire, Valuing Freedoms: Sen’s Capability Approach and Poverty Reduction,

Oxford University Press, USA, 2005.

[7] Sami Bibi, Measuring Poverty in a Multidimensional Perspective: A Review of Litera-

ture, 2005.

[8] Chris Browne, David S. Matteson, Linden McBride, Hu Leiqiu, Yanyan Liu, Ying Sun,
Jiaming Wen, Christopher B. Barrett, Multivariate random forest prediction of poverty
and malnutrition prevalence, PLoS One 16 (2021), e0255519.

[9] James Foster, Joel Greer, Erik Thorbecke, A class of decomposable poverty measures,

Econometrica (1984) 761–766.

[10] Trevor Hastie, Robert Tibshirani, Jerome H. Friedman, Jerome H. Friedman, The Ele-
ments of Statistical Learning: Data Mining, Inference, and Prediction, vol. 2, springer,
New York, 2009.

[11] Jonathan Haughton, Shahidur R. Khandker, Handbook on Poverty+ Inequality, World

Bank Publications, 2009.

[12] Shan Hu, Yong Ge, Mengxiao Liu, Zhoupeng Ren, Xining Zhang, Village-level poverty
identiﬁcation using machine learning, high-resolution images, and geospatial data,
Int. J. Appl. Earth Obs. Geoinf. 107 (2022), 102694.

[13] Qing Li, Yu Shuai, Damien Échevin, Min Fan, Is poverty predictable with machine learn-
ing? A study of DHS data from Kyrgyzstan, Socio Econ. Plan. Sci. 81 (2022), 101195.

[14] Mengxiao Liu, Hu Shan, Yong Ge, Gerard B.M. Heuvelink, Zhoupeng Ren, Xiaoran
Huang, “Using multiple linear regression and random forests to identify spatial poverty
determinants in rural China.” spatial, Statistics 42 (2021), 100461.

[15] Pa Pa Min, Yen Wen Gan, Siti Nursyuhada Binti Hamzah, Thian Song Ong, Md Shohel
Sayeed, Poverty prediction using machine learning approach, J. Southwest Jiaotong
Univ. 57, no. 1 (2022).

[16] Aishwarya Mujumdar, V. Vaidehi, Diabetes prediction using machine learning algo-

rithms, Proc. Comput. Sci. 165 (2019) 292–299.

[17] Guberney Muñetón-Santa, Luis Carlos Manrique-Ruiz, Predicting multidimensional
poverty with machine learning algorithms: an open data source approach using spatial
data, Sociol. Sci. 12 (5) (2023) 296.

[18] RA11315, Community-Based Monitoring Act of 2018, https://www.ofﬁcialgazette.gov.

ph/downloads/2019/04apr/20190417-RA-11315-RRD.pdf 2024.

[19] Jomar F. Rabajante, Jerrold M. Tubay, Hiromu Ito, Takashi Uehara, Satoshi Kakishima,
Satoru Morita, Jin Yoshimura, Dieter Ebert, Host-parasite red queen dynamics with
phase-locked rare genotypes, Sci. Adv. 2 (3) (2016), e1501548.

[20] Benjamin Seebohm Rowntree, Poverty: A study of town life, Macmillan, 1902.
[21] Alellie Borel Sobreviñas, Examining chronic and transient poverty using the
community-based monitoring system (CBMS) data: the case of the municipality of
Orion, DLSU Business Econ. Rev. 30 (1) (2020) 111–129.

[22] Thomas Pave Sohnesen, Niels Stender, Is random forest a superior methodology for
predicting poverty? An empirical assessment, Poverty Public Policy 9 (1) (2017)
118–133.

[23] Aubrey D. Tabuga, Christian D. Mina, Celia M. Reyes, Ronina D. Asis, Maria Blesila G.
Datu, Dynamics of Poverty in the Philippines: Distinguishing the Chronic from the Tran-
sient Poor. No. 2011-31, PIDS Discussion Paper Series, 2011.

[24] United Nations, Facing the challenge of measuring the unmeasurable, https://www.un.

org/en/development/desa/news/statistics/measuring-the-unmeasurable.html 2012.

[25] Jeffrey M. Wooldridge, Mokhtarul Wadud, Jenny Lye, Introductory Econometrics: Asia

Paciﬁc Edition with Online Study Tools 12 Months, Cengage AU, 2016.

Emmanuel A. Onsay is a Certiﬁed Public Accountant, econo-
mist, data analyst, econometrician, assistant professor,
extensionist, and researcher at Partido State University,
Camarines Sur, Philippines. He completed the Master in Applied
Economics at De La Salle University (DLSU) School of Econom-
ics. He graduated with 5 publications, and 4 research awards
and recognitions. He also successfully ﬁnished an international
exchange program, the Sakura Science Exchange Program of
Japan Science and Technology Agency and Kochi University
Japan. He was awarded 2 University Presidential Citations for
Research and Competitive Graduate Studies. He also received
2 Kilyab Awards for research, various publication awards, and
citation awards. At this point, he bagged 25 best paper awards
in different conferences across regions. In 2023, he became
the youngest recipient of the Outstanding Faculty Award of Partido State University. He is also
the youngest researcher from his institution to be included in the World's Scientists rankings by
the AD Scientiﬁc Index. Currently, he is a candidate for the degree of Doctor of Philosophy by
Research in Data Science(Analytics) and Informatics, specializing in Economics, Business, and
Quantitative Social Science Analytics at the University of the Philippines Los Baños Graduate
School. His dissertation focuses on Measuring the unmeasurable aspects of society. His re-
search interest and specialization lie in data analytics, poverty economics, public economics,
applied econometrics, impact evaluation, environmental economics, business analytics, and
accountancy.

Jomar F. Rabajante is a professor 5 and UP Scientist III of the
Institute of Mathematical Sciences and Physics (IMSP), and
Dean of the Graduate School University of the Philippines Los
Baños (UPLB), Laguna, Philippines. He holds an appointment
as a Junior Associate at the Quantitative Life Sciences Group
of the Abdus Salam International Centre for Theoretical Physics
in Trieste Italy from year 2019 to 2024. He served as a research
collaborator/consultant to the Asian Development Bank, United
Nations Population Fund, Zuellig Family Foundation, World Vi-
sion/START Network, PhilRice, Department of Finance, Task
Force T3, Supreme Court of the Philippines, and Province of Ba-
taan in modeling the dynamics of infectious diseases. He is one
of the proponents and the co-chair for program implementation
of the ﬁrst and only PhD Applied Mathematics degree program
in the Philippines and PhD by Research (Data Analytics and Informatics) programs in UPLB. He
is a holder of a Doctor of Science in Mathematical and Systems Engineering - Environment and
Energy Systems from Shizuoka University (National University), Hamamatsu City, Shizuoka,
Japan under the Japanese Government Monbukagakusho scholarship grant. His research inter-
ests lie in mathematical modeling, data analytics, and quantitative risk assessment of complex
biological and social systems.

14

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

ScienceTalks11(2024)100387
ContentslistsavailableatScienceDirect
Science Talks
journal homepage: www.elsevier.es/sctalk
When machine learning meets econometrics: Can it build a better measure
to predict multidimensional poverty and examine unmeasurable economic
conditions?
⁎
EmmanuelA.Onsaya,b, ,JomarF.Rabajantea
aGraduateSchool,UniversityofthePhilippinesLosBaños,Laguna4030,Philippines
bPartidoInstituteofEconomics,PartidoStateUniversity,CamarinesSur4422,Philippines
A R T I C L E I N F O A B S T R A C T
Keywords: Povertyisasoldashumancivilization,hardtoeradicate,multidimensional,anddifficulttomeasure.Themethods
Machinelearning usedtomeasurepovertytodayarecostly,labor-intensive,andtime-consuming.Therefore,policymakersfinditdiffi-
Econometrics culttotargetpolicieswhenputtingpovertyreductioninitiativesintoaction.Indigenouscommunitiesareamongthe
Multidimensionalpoverty
mostdisadvantagedandvulnerablepopulationsinsociety.Theirsocioeconomicsituationsarecomplexandmultifac-
Indigenouspeople
eted.Whileresearchonpovertyisusuallygeneric,pronetolargesamplingerrors,andintendedtoguidenationalpol-
Economicdevelopment
icy,researchonindigenouspeopleisqualitative.Thus,tomeasuremultidimensionalpovertywithdisaggregated
Povertyalleviation
techniques,thisworkblendsmachinelearningandeconometrics.Researcherswhohavebeenstudyingpovertyworld-
widecanreplicatealloftheapproaches,strategies,andresourcesusedinthisstudy.WiththebestR-squareandaccu-
racy,randomforestmodelsperformbetterthanallregressorsandclassifierscombined.Italsoconfirmsthecausal
relationshipandcurrenteconometricassociationbetweenmultidimensionalcharacteristicsandpovertyconse-
quences.Thisstudydemonstratestheviabilityofusingmachinelearningtopredictpovertyinawaythatcansave
costs,cutlabor,andmaximizetimetoempowerindigenouscommunitiesandalleviatethepovertyofimpoverished
societiesinthepoorestregionofLuzon,Philippines.
VideoandPresentationstothisarticlecanbefoundonlineathttps://
doi.org/10.1016/j.sctalk.2024.100387.
⁎
Correspondingauthorat:GraduateSchool,UniversityofthePhilippinesLosBaños,Laguna4030,Philippines.
E-mailaddress:eaonsay@up.edu.ph(E.A.Onsay).
http://dx.doi.org/10.1016/j.sctalk.2024.100387
Received4March2024;Receivedinrevisedform12July2024;Accepted18July2024
2772-5693/©2024TheAuthors.PublishedbyElsevierLtd.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Figuresandtables
Fig.1.Comprehensivepovertyanalyticsatdisaggregatedapproaches.
2

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Abucayanisthemostimpoverishedlocality.SanJose,SanBenito,and
Pandayhavethefewestimpoverishedhouseholds.Whilepovertyiswide-
spreadintheIsarogSector,itisnotassevereinthePoblacioncommunity.
Watt'sIndexclaimsthatIsarogcommunitieshaveagreaterprevalenceof
poverty.Poorhouseholdsandpeoplearereflectedthroughpovertyinci-
dence,whichrepresentstheheadcountratioofthoselivingbelowthepov-
ertylineandfoodthresholdsinthePhilippines,relativetothetotalnumber
ofhouseholdsandpopulation[1,2,11,18,21].
Fig.2.Resultsofmultidimensionalpovertyevaluationatdisaggregationandcombinationthroughthemultipleconstructsandindicators.
About63.70%ofpeopleliveinpovertyand51.10%ofindividualsdo
nothaveaccesstofood.Thedynamicsofeducation,income,andhealth
allclearly demonstratepoverty. InthePhilippines,householdswitha
monthlyincomeofPhP10,481(about186.18USD)andbelowforafamily
offiveareconsideredpoor.Itisimportanttoconsiderthatdifferentregions
mayhavedifferentpovertylines,soitispre-requisitetoidentifythepoverty
lineinyourareabeforeapplyingoursuggestedMLmodels.Multidimen-
sionalPovertydeprivationreferstothe15economicvariablesthatwe
haveemployed,whichserveaspredictorsorindependentvariablesinour
econometricandmachinelearningmodels.Itoffersamorecomprehensive
approach.Insteadofusinganindex,weemploybinaryanddummydatato
capturenon-linearrelationships[1,2,21,23].
3

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Fig.3.Classificationresultsandpredictivemarginsofmultidimensionalvariables.
Asafactorimpactinghealthdynamics,theresultsindicatethathouse-
holdsizeisastrongpredictorofpoverty.Povertyismorelikelytobeexpe-
rienced by informal settlers than by formal settlers. Furthermore, the
chanceoffallingintopovertyincreaseswiththenumberofhousehold
members[1,2,6,20,24].
Fig.4.Averagerootmeanssquareerrorofmachinelearningregressorsforimpoverishedsocieties.
4

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
WithanRMSEof0.3298,therandomforestmethodperformsbetter
thantheothers,LightGBMat0.3642andXGBoostat0.4001.Theseresults
arederivedfromMLmodels(regressors)displayedonvideoslides15and
17.Thereasonwhyrandomforestperformedthebestisthatitcanidentify
explanatoryfactors,findnonlinearcorrelationsbetweenexplanatoryand
dependentvariables,andestimatefeatureimportance,whichprovidesin-
sightintothefeaturesthathavethegreatestinfluenceonthecategorization
process.Althoughtheoutcomeofmachinelearning(ML)isdependenton
thecontextofthedata,resultsfromMLappliedtosimilardatasetsand
modelsinotherlocationswouldbecomparable.Maybetheonlythings
thatwouldchangearethepredictors.TheMLmodelissustainableinthis
waysinceitrequiresalargeamountofdata,andthedataweutilizedis
availableinthePhilippineseverytwoyearsafterthecensus.Furthermore,
even with cross-sectional data, different regions can apply machine
learningoncethedataisaccessibleforthem,becauseamedium-termsocial
outcomecanbepredictedbyanMLmodel[1,2,19,10,15].
Fig.5.Averagemeansquareerrorofmachinelearningregressorsforimpoverishedsocieties.
5

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Fortheentiremunicipality,therandomforestregressionalgorithmhas
thelowestmeansquareerror,at0.0792.XGBoost(0.4722)andLightGBM
(0.1242)areinitswake.TheMLmodelsweusedarespecifictotheareas
westudied.Therefore,weinitiallyemployed econometricstoidentify
properpredictorsforMLmodelsthatarespecifictoourlocalcontext.How-
ever,thepovertymodels(logistic)andtheMLmodels(regressorsandclas-
sifiers) are generic and can be applied to other regions or countries.
Consequently,repeatabilityishighlyfeasibleinthisregard.Otherregions
oftheworldwouldneedtoidentifytheirownpredictors,butthemodels
weusedcouldalsoworkforthem[1,2,15,22].
Fig.6.AverageR-squareofmachinelearningregressorsforimpoverishedsocieties.
WithanR-squareof0.4221,thelinearregressionhasthelowestvalue.
TherandomforestregressorproducedthehighestR-square,0.92075.It
suggeststhattheregressionthatbestmatchestheregressionlineandhas
thelowesterrorscoreistherandomforestregression.Sincethedataexam-
inedinthispaperisbasedonacomprehensivecensusofallpopulationsin-
cludingindigenouspeople,therearenoknownlimits.Asaresult,itremains
exempttosamplingerrorandupholdsthesampleassumptionsofinternal
andexternalvalidity.Thewritersthoroughlyexamineandfilterthedata's
multidimensionalvariables.Thedatasetiswell-sizedanddevoidofwell-
knownbiases.Buttimeisoftheessence.Ittakestimetocreatetrustworthy
andverifiabledatasetsandmodels[1,2,12,13,14].
6

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Fig.7.Performanceevaluationofmachinelearningregressorsforimpoverishedsocieties.
Withanaccuracyof0.9108,therandomforestregressionclassifierhas
thehighestperformance.ThealgorithmswiththelowestaccuracyareBag-
ging(0.8437)andDecisionTree(0.8418).TheR-squaresfortheSVM,
AdaBoost,GaussianNB,andPerceptronare0.86–0.87.Therandomforest
classificationhasthegreatestaccuracyrateof95.94%inpipelinealgo-
rithms.Concerningthefutureimprovements,theutilizationofeconometric
modelsandpredictiveanalyticsdatasetshasthepotentialtogenerateem-
piricaldatathatstrengthenspovertytheoriesthatapplytoentirepopula-
tions, including indigenous populations. This would contribute to the
existingbodyofknowledgeaboutthedearthofmultidimensionalpoverty
metricsindevelopingnationslikethePhilippines,especiallyforindigenous
populations.Applyingthemodelstoallothertribesinthenationandutiliz-
ingartificialneuralnetworkscouldbothenhanceforecastaccuracyand
yieldimprovements[1,2,8,16,17].
7

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Fig.8.Indigenouscommunities'populationanalytics.
Indigenouspeoplemakeupabout11.84%ofallhouseholdsinGoa,
CamarinesSur.SanPedroAroro,Payatan,andBalaynanarethemostpop-
ulousindigenoustribes,withrespectivetotalpopulationdistributionsof
92.50%,68.66%,and46.30%[3,4,7,11].
8

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Fig.9.Multidimensionalsocioeconomicevaluationandpovertyexaminationofindigenouspeopletribes.
Thereare1660housesofindigenouspeopleand8022personsintotal.
Eighty-twopercentofpeopleliveinpoverty,and71%donothaveaccessto
| food. Evaluation | resultsfor schooling | are largely constant | throughout |
| ---------------- | -------------------- | -------------------- | ---------- |
barangays,suggestingthatmostchildrenintheneighborhoodarenoten-
| rolled in school | or have stopped | enrolling as educational | levels rise |
| ---------------- | --------------- | ------------------------ | ----------- |
[3,4,7,11,18].
9

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Fig.10.Indigenouspeoplepovertyanalytics.
ThePooresttribeistheAbucayanTribewhiletheLeastPoortribeisthe
SalogTribe[1,3,4,21,23].
Fig.11.IPClassificationPredictionMargins.
LivingbelowthepovertylevelismorecommonamongIPinformalset-
tlers.Moreover,theprobabilityofpovertyincreaseswiththenumberof
householdmembers.TheresultsoftheEstatcategorizationarepositive.
Overall,86.14%ofcaseswereappropriatelyclassified[3,4,5,9,25].
10

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Fig.12.Averagemeansquareerror(MSE)ofmachinelearningregressorsinIPmodeling.
AfterLightGBMandXGBoost,therandomforestregressionmethodhas
thelowestmeansquareerror(0.5497).Causalitytestsusingeconometrics
(logitandprobitregression)wereinitiallyperformedtoidentifypredictors
fortheMLmodels.Allthemultidimensionalindicatorsusedinthemodel
(Fig.9)andreflectedinthevideohaveacausalrelationshipwithpoverty
forIPgroups.Thefollowingvariableshavebeenfoundtohavecausality:
HealthandNutrition,Housing,WaterandSanitation,BasicEducation,In-
comeandLivelihood,andPeaceandOrder.Sincethesevariablesarecaus-
allylinkedtopoverty,theyserveaspredictorsintheMLmodels.Giventhat
thesevariableshaveacausalrelationshipandarepredictorsofpovertyin
themodels,ourpolicymappingandtargetinganalysisfocusesonthesevar-
iables.Weconcentrateonaddressingthesevariablesinordertoimprove
policies,asdoingsowouldalleviatepovertyandpromotedevelopment
[3,4,15,22].
11

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Fig.13.AverageR-squareofmachinelearningregressorsforIndigenousCommunities.
Ofallthetechniques,linearregressionhasthelowestR-square,at
0.4222.NextareapolynomialalgorithmandanSVR.WithanR-square
of0.9208,therandomforestregressorproducedthehighestresults,al-
thoughCatBoost,XGBoost,andLightGBMallperformedsimilarly.Itim-
plies that the random forest regression is the one that most closely
resemblestheregressionlineandhasthelowesterrorscore[3,4,12,13,14].
12

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
Fig.14.PerformanceevaluationofMLclassifiersatrandomandpipelineforIP.
Foralltribesatrandom(α),therandomforestregressionclassifierhas Acknowledgments
thehighestaccuracy(90.69%);K-NearestNeighbour,GradientBoost,and
Logisticfollow.Atpipeline(Ω),therandomforestclassificationhasthe Wewouldliketoexpressourprofoundgratitudetothefollowingorga-
greatestaccuracyrateat94.89%.Thenexttwoclassificationstrategiesare nizationsandindividualsfortheirvitalsupportofourresearch:Elsevier's
gradientboostandlogistic.Theresultsaffirmthatall15indicatorsserve ScienceTalksforprovidingusaplatformtodisseminateourstudy'sre-
aspredictorsofpoverty,andtherandomforestalgorithmemergesasthe viewsthroughvideopresentation,whichsupporteconomicdevelopment
mosteffectivemodelforpovertyprediction.Therefore,itiscrucialtoad- and poverty alleviation; University of the Philippines Los Baños
dressalltheseindicatorsadequatelysincetheyaretherootcausesofpoverty. GraduateSchoolforresearchdevelopmentandanalysis;PartidoState
Byformulatingpoliciesthattargeteachpredictor,povertycanbealleviated, University for financial and logistic support; De La Salle University
leadingtoadvancementsineconomicdevelopment[3,4,8,16,17]. SchoolofEconomicsforinsightfulfeedbackandreview;andLGUGoa
CamarinesSurforprovidingthenecessarydata.Intermsofauthorization
andlogisticalsupport,wewouldliketoexpressoursincereappreciationto
CRediTauthorshipcontributionstatement
Hon.Pan,MarcelS.,Engr.MorielPrado,Ms.PreseBradecina,Mr.Rafael
EmmanuelA.Onsay:Writing–originaldraft,Visualization,Valida- Belleza,Mr.JudeZairC.Paladan,Ms.KescheiJoanaVillarCañaveras,
Mr.HermanB.JungcoII,Mr.ChrisOcampo,andMr.JobertRonabio.
tion,Projectadministration,Methodology,Investigation,Fundingacquisi-
WealsoadmireProf.JerroldTubayandProf.NeilJeromeEgarquinfor
tion, Formal analysis, Data curation, Conceptualization. Jomar F.
Rabajante:Writing–review&editing,Validation,Supervision,Software, their support in mathematical analysis, and we owe Prof. Jason
AlinsunurinandProf.JeffersonArapocfortheirhelpwitheconometrics.
Resources, Project administration, Methodology, Funding acquisition,
We are deeply grateful to Prof. Eva Marie Aragones and Prof. Alellie
Formalanalysis,Conceptualization.
Sobreviñasfortheirinvaluablecontributionstothepovertymodels.We
verymuchappreciatetheinvaluableassistancewithediting,curation,
Dataavailability andlogisticsprovidedbyProf.RolanJonG.Bulao,SirKevinC.Baltar,
Mr.MarkReyPardiñas,Ms.SpottyKankan,Mr.JackNoy,Mr.KingUkay,
Wehavesharedourdatapublicly.Thelinkstoourdatasetswerepro- andMs.SakuraKok.Furthermore,weareincrediblygratefultothepolicy-
videdthroughthereferencessection(Ref.1,2,3,4) makers, government representatives, and stakeholders who have
13

E.A.Onsay,J.F.Rabajante ScienceTalks11(2024)100387
contributedsignificantinsightsandfeedbacktodevelopandimplement [14] MengxiaoLiu,HuShan,YongGe,GerardB.M.Heuvelink,ZhoupengRen,Xiaoran
Huang,“Usingmultiplelinearregressionandrandomforeststoidentifyspatialpoverty
policysolutions.Ultimately,wegivetheAlmightyGodthehighestpraise determinantsinruralChina.”spatial,Statistics42(2021), 100461.
forknowledge,power,andwisdom. [15] PaPaMin,YenWenGan,SitiNursyuhadaBintiHamzah,ThianSongOng,MdShohel
Sayeed,Povertypredictionusingmachinelearningapproach,J.SouthwestJiaotong
Univ.57,no.1(2022).
Funding
[16] AishwaryaMujumdar,V.Vaidehi,Diabetespredictionusingmachinelearningalgo-
rithms,Proc.Comput.Sci.165(2019)292–299.
ThisworkwassupportedbythePartidoStateUniversity(PovertyAlle- [17] GuberneyMuñetón-Santa,LuisCarlosManrique-Ruiz,Predictingmultidimensional
viationandEconomicDevelopmentProject2022–2025)andUniversityof povertywithmachinelearningalgorithms:anopendatasourceapproachusingspatial
data,Sociol.Sci.12(5)(2023)296.
thePhilippinesLosBaños(GraduateSchool2023–2025).
[18] RA11315,Community-BasedMonitoringActof2018,https://www.officialgazette.gov.
ph/downloads/2019/04apr/20190417-RA-11315-RRD.pdf2024.
Ethicsstatement [19] JomarF.Rabajante,JerroldM.Tubay,HiromuIto,TakashiUehara,SatoshiKakishima,
SatoruMorita,JinYoshimura,DieterEbert,Host-parasiteredqueendynamicswith
phase-lockedraregenotypes,Sci.Adv.2(3)(2016), e1501548.
Allgraphsandfigurespresentedinthisworkwereproducedandvisual- [20] BenjaminSeebohmRowntree,Poverty:Astudyoftownlife,Macmillan,1902.
izedbytheauthors.Theutilizationofallphotosinthevideopresentation [21] Alellie Borel Sobreviñas, Examining chronic and transient poverty using the
community-basedmonitoringsystem(CBMS)data:thecaseofthemunicipalityof
hasobtainedformalconsentfromthesubject,university,government, Orion,DLSUBusinessEcon.Rev.30(1)(2020)111–129.
andstakeholders.TheconductofthisstudywasapprovedbyPartidoState [22] ThomasPaveSohnesen,NielsStender,Israndomforestasuperiormethodologyfor
University and the University of the Philippines Los Baños. The Goa, predictingpoverty?Anempiricalassessment,PovertyPublicPolicy9(1)(2017)
118–133.
CamarinesSurLocalGovernmentUnitgavepermissionfortheresultsof
[23] AubreyD.Tabuga,ChristianD.Mina,CeliaM.Reyes,RoninaD.Asis,MariaBlesilaG.
theprocesseddatatobeused,manipulated,analyzed,andcommunicated. Datu,DynamicsofPovertyinthePhilippines:DistinguishingtheChronicfromtheTran-
Researchersvoluntarilyconductthedataanalysisandprocedures;theyare sientPoor.No.2011-31,PIDSDiscussionPaperSeries,2011.
[24] UnitedNations,Facingthechallengeofmeasuringtheunmeasurable,https://www.un.
notacomponentofanyexperiment.Ourhumandataaresecondary,indi-
org/en/development/desa/news/statistics/measuring-the-unmeasurable.html2012.
rect,andsocioeconomicinnature;theydon'tentailanylaboratorywork. [25] JeffreyM.Wooldridge,MokhtarulWadud,JennyLye,IntroductoryEconometrics:Asia
Thus,ethicalclearancesarenotrequired.Furthermore,thisstudydoes PacificEditionwithOnlineStudyTools12Months,CengageAU,2016.
notinvolveanyanimaltesting,directhumanvolunteers,ordataacquired
fromsocialmediaplatforms.
EmmanuelA.OnsayisaCertifiedPublicAccountant,econo-
mist, data analyst, econometrician, assistant professor,
extensionist, and researcher at Partido State University,
Declarationofinterests CamarinesSur,Philippines.HecompletedtheMasterinApplied
EconomicsatDeLaSalleUniversity(DLSU)SchoolofEconom-
Theauthorsdeclarethattheyhavenoknowncompetingfinancialinter- i
a
c
n
s
d
.H
re
e
co
g
g
ra
n
d
it
u
io
a
n
te
s
d
.H
w
e
it
a
h
ls
5
os
p
u
u
c
b
c
l
e
ic
ss
a
f
t
u
io
ll
n
y
s
fi
,
n
an
is
d
he
4
d
r
a
e
n
se
i
a
n
r
t
c
e
h
rn
a
a
w
tio
ar
n
d
a
s
l
estsorpersonalrelationshipsthatcouldhaveappearedtoinfluencethe
exchangeprogram,theSakuraScienceExchangeProgramof
workreportedinthispaper. JapanScienceandTechnologyAgencyandKochiUniversity
Japan.Hewasawarded2UniversityPresidentialCitationsfor
ResearchandCompetitiveGraduateStudies.Healsoreceived
References 2KilyabAwardsforresearch,variouspublicationawards,and
citationawards.Atthispoint,hebagged25bestpaperawards
indifferentconferencesacrossregions.In2023,hebecame
[1] E.A.Onsay,J.Rabajante,Measuringtheunmeasurablemultidimensionalpovertyfor
theyoungestrecipientoftheOutstandingFacultyAwardofPartidoStateUniversity.Heisalso
economicdevelopment:datasets,algorithms,andmodelsfromthepoorestregionof
theyoungestresearcherfromhisinstitutiontobeincludedintheWorld'sScientistsrankingsby
Luzon,Philippines,DataBriefJ.(2024),https://doi.org/10.1016/j.dib.2024.110150. theADScientificIndex.Currently,heisacandidateforthedegreeofDoctorofPhilosophyby
[2] EmmanuelOnsay,JomarRabajante,Datasetonmeasuringtheunmeasurablemultidi-
ResearchinDataScience(Analytics)andInformatics,specializinginEconomics,Business,and
mensionalruralpovertyforeconomicdevelopment:analysisfromthepoorestdistrict
QuantitativeSocialScienceAnalyticsattheUniversityofthePhilippinesLosBañosGraduate
ofthepoorestprovinceinthepoorestregionofLuzon,Philippines,MendeleyDataV1
School.HisdissertationfocusesonMeasuringtheunmeasurableaspectsofsociety.Hisre-
(2023),https://doi.org/10.17632/s76nh7dm4v.1.
[3] EmmanuelA.Onsay,“Povertyprofileandhealthdynamicsofindigenouspeople.”Int searchinterestandspecializationlieindataanalytics,povertyeconomics,publiceconomics,
rev,Soc.Sci.Res.2(2022)1–27. appliedeconometrics,impactevaluation,environmentaleconomics,businessanalytics,and
accountancy.
[4] EmmanuelOnsay,JomarRabajante,MeasuringtheUnmeasurableSocio-Economic
ConditionsandMultidimensionalPovertyofIndigenousPeople:Datasetsfromthe
PoorestRegionofLuzon,Philippines,vol.V1,HarvardDataverse,2023,https://doi.
org/10.7910/DVN/QSZKUP. JomarF.Rabajanteisaprofessor5andUPScientistIIIofthe
[5] JohnH.Aldrich,ForrestD.Nelson,LinearProbability,Logit,andProbitModels,vol.45, InstituteofMathematicalSciencesandPhysics(IMSP),and
Sage,1984. DeanoftheGraduateSchoolUniversityofthePhilippinesLos
[6] SabinaAlkire,ValuingFreedoms:Sen’sCapabilityApproachandPovertyReduction, Baños(UPLB),Laguna,Philippines.Heholdsanappointment
OxfordUniversityPress,USA,2005. asaJuniorAssociateattheQuantitativeLifeSciencesGroup
[7] SamiBibi,MeasuringPovertyinaMultidimensionalPerspective:AReviewofLitera- oftheAbdusSalamInternationalCentreforTheoreticalPhysics
ture,2005. inTriesteItalyfromyear2019to2024.Heservedasaresearch
[8] ChrisBrowne,DavidS.Matteson,LindenMcBride,HuLeiqiu,YanyanLiu,YingSun, collaborator/consultanttotheAsianDevelopmentBank,United
JiamingWen,ChristopherB.Barrett,Multivariaterandomforestpredictionofpoverty NationsPopulationFund,ZuelligFamilyFoundation,WorldVi-
andmalnutritionprevalence,PLoSOne16(2021), e0255519. sion/STARTNetwork,PhilRice,DepartmentofFinance,Task
[9] JamesFoster,JoelGreer,ErikThorbecke,Aclassofdecomposablepovertymeasures, ForceT3,SupremeCourtofthePhilippines,andProvinceofBa-
Econometrica(1984)761–766. taaninmodelingthedynamicsofinfectiousdiseases.Heisone
[10] TrevorHastie,RobertTibshirani,JeromeH.Friedman,JeromeH.Friedman,TheEle- oftheproponentsandtheco-chairforprogramimplementation
mentsofStatisticalLearning:DataMining,Inference,andPrediction,vol.2,springer, ofthefirstandonlyPhDAppliedMathematicsdegreeprogram
NewYork,2009. inthePhilippinesandPhDbyResearch(DataAnalyticsandInformatics)programsinUPLB.He
[11] JonathanHaughton,ShahidurR.Khandker,HandbookonPoverty+Inequality,World isaholderofaDoctorofScienceinMathematicalandSystemsEngineering-Environmentand
BankPublications,2009. EnergySystemsfromShizuokaUniversity(NationalUniversity),HamamatsuCity,Shizuoka,
[12] ShanHu,YongGe,MengxiaoLiu,ZhoupengRen,XiningZhang,Village-levelpoverty JapanundertheJapaneseGovernmentMonbukagakushoscholarshipgrant.Hisresearchinter-
identificationusingmachinelearning,high-resolutionimages,andgeospatialdata, estslieinmathematicalmodeling,dataanalytics,andquantitativeriskassessmentofcomplex
Int.J.Appl.EarthObs.Geoinf.107(2022), 102694. biologicalandsocialsystems.
[13] QingLi,YuShuai,DamienÉchevin,MinFan,Ispovertypredictablewithmachinelearn-
ing?AstudyofDHSdatafromKyrgyzstan,SocioEcon.Plan.Sci.81(2022), 101195.
14