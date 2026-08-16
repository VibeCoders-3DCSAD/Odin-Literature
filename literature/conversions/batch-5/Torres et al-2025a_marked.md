---
conversion_metadata:
  converted_at: "2026-07-21T09:04:47Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Torres et al-2025a.pdf"
  source_pdf_sha256: "be1fc353bdb50f1ae2977d4cb666263342746ae0387bdc7868e73ad46ef764ae"
  page_count: 4
  markdown_char_count: 47162
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Consumer’s Financial Habits on Server-Based Electronic Money
as It Affects Their Financial Behavior: Moderated By Monthly
Transactions
Globien Maitre Olaivar
Mapua Malayan Colleges Laguna
Cabuyao City, Philippines
2022gmolaivar@live.mcl.edu.ph

Ramachandra Castro Torres∗
Mapua Malayan Colleges Laguna
Cabuyao City, Philippines
rctorres@mcl.edu.ph

Steven Ian Britanico
Mapua Malayan Colleges Laguna
Cabuyao City, Philippines
sicbritanico@live.mcl.edu.ph

Abstract
This study investigates the impact of various financial habits—
specifically saving, spending, donating, investing, and credit/loan
behaviors—on consumer financial behavior, with transaction fre-
quency serving as a moderating factor. Grounded in the Theory
of Planned Behavior, the research utilized a quantitative approach,
collecting data from a targeted group of electronic money users
(GCash) through purposive sampling. The multiple regression anal-
yses revealed that all financial habits, except for credit/loan be-
haviors, significantly influence financial behavior. Additionally,
moderation analysis demonstrated that higher transaction volumes
enhance the relationship between spending habits and financial
behavior, emphasizing the role of mobile wallet usage in reinforcing
these spending patterns. These findings provide valuable insights
for fintech companies, enabling them to improve platform usability
and financial management tools, ultimately promoting responsible
financial habits among users. Consumers can gain a clearer un-
derstanding of how mobile wallets affect their financial decisions,
encouraging more informed spending and saving practices. Fu-
ture research should delve deeper into long-term behavioral trends,
qualitative insights, and the psychological factors driving digital
financial behavior, offering a broader perspective on how technol-
ogy shapes financial habits over time. By exploring these areas, the
evolving landscape of consumer finance in the digital age can be
understood further.

CCS Concepts
• Applied computing → Law, social and behavioral sciences;
Economics.

Keywords
Server-Based Electronic Money, GCash, style, Financial Behavior,
insert

ACM Reference Format:
Ramachandra Castro Torres, Globien Maitre Olaivar, and Steven Ian Britan-
ico. 2025. Consumer’s Financial Habits on Server-Based Electronic Money
as It Affects Their Financial Behavior: Moderated By Monthly Transactions.
In The 9th International Conference on Business and Information Management

∗Corresponding Author

This work is licensed under a Creative Commons Attribution 4.0 International License.
ICBIM 2025, Bangkok, Thailand
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2217-2/2025/09
https://doi.org/10.1145/3785171.3785192

(ICBIM 2025), September 19–21, 2025, Bangkok, Thailand. ACM, New York,
NY, USA, 4 pages. https://doi.org/10.1145/3785171.3785192

1 INTRODUCTION
In recent years, rapid technological innovations have significantly
transformed consumer behavior, particularly through the rising
popularity of e-commerce and the use of electronic wallets (e-
wallets) for online transactions. As consumers seek more con-
venient and efficient ways to shop, traditional payment methods—
such as cash and credit cards—are increasingly being replaced by
more practical and secure alternatives [1].

Advancements in digital wallet technology have played a cru-
cial role in this transition. E-wallets allow users to store payment
information and make transactions quickly and securely from their
mobile devices or computers. Features such as biometric security,
real-time transaction notifications, and digital receipt tracking en-
hance the user experience and build trust among consumers. The
shift toward e-commerce and e-wallets has been accelerated by the
global pandemic, which forced many businesses to adapt to online
selling and consumers to seek contactless payment options. This
trend highlights the importance of digital wallets as not only a safer
alternative but also a convenient choice for everyday transactions
[2].

Given these changes, it is essential to explore the implications
of digital wallets on consumer behavior. Understanding how these
technologies affect purchasing decisions, trust in online platforms,
and overall satisfaction can provide valuable insights for businesses
aiming to meet the evolving needs of their customers in this dy-
namic landscape.

Server-based electronic money systems offer enhanced security
features designed to mitigate the risks associated with electronic
transactions. An e-wallet, as defined by the Bank for International
Settlements, is a non-cash payment device that incorporates stored
value or prepaid products on an electronic device utilized by the
consumer. Supporting this concept, a study conducted by Lai [3]
indicated that increased security measures are positively correlated
with a heightened intention to utilize digital payment technologies.
Concerns surrounding the risks of theft and loss associated with
carrying cash and cards render security a critical factor influencing
consumer decision-making in relation to electronic payments.

This trend is particularly pronounced in developing countries
such as the Philippines, where the demand for cashless transac-
tions has accelerated following the endorsement of e-banking and
e-wallets by the Bangko Sentral ng Pilipinas, the country’s banking
regulatory authority [4]. As of 2023, the Philippines has witnessed
a considerable surge in the adoption of e-wallets, exemplified by

---

<!-- PAGE 2 -->

ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Ramachandra Torres et al.

GCash, which has attained a notable milestone of over 60 million
registered users nationwide [5]. This widespread acceptance under-
scores GCash’s significance as a virtual wallet that facilitates secure,
rapid, and convenient money transfers, thereby transforming the
digital payments landscape in the Philippines.

Initially launched in 2004, GCash gained substantial traction
during the COVID-19 pandemic, buoyed by regulatory support
and strategic innovations from telecommunications leaders Smart
Communications and Globe Telecom. Presently, GCash serves a
crucial role in promoting financial inclusion, offering a versatile
platform for various transactions, including bill payments, money
transfers, and mobile commerce [5].

This study aimed to investigate the effects of server-based elec-
tronic money, specifically focusing on GCash, on consumers’ finan-
cial behaviors. It explored various aspects such as saving, spending,
donating, investing, and credit or loan habits to understand how fac-
tors like specific financial practices and the accessibility of GCash
influenced consumer use of the platform. This research sought
to illuminate how these factors shaped financial decision-making
processes. Additionally, the study examined the relationship be-
tween financial habits and the average frequency of transactions
per month, analyzing how this usage frequency affected consumers’
overall financial behavior. By establishing this connection, the re-
search aimed to provide insights into the impact of GCash on the
financial choices and practices of its users.

2 LITERATURE REVIEW
2.1 Server-Based Electronic Money and

Financial Behavior

The emergence of server-based electronic money (SBEM), includ-
ing digital wallets and mobile payment platforms, has transformed
consumer financial behavior by enhancing convenience, accessibil-
ity, and transaction speed. Operating through centralized servers,
SBEM enables secure, real-time transactions without the need for
physical cash or traditional banking. Studies show that FinTech
innovations have led to more frequent small-value transactions,
increased reliance on mobile devices, and a shift toward cashless
economies, reflecting both technological and psychological changes.
SBEM also promotes financial inclusion and literacy, especially
among underserved populations, by simplifying saving, borrowing,
and risk management. However, without proper financial educa-
tion, these tools may also encourage impulsive spending, highlight-
ing the need for a balanced understanding of their benefits and
risks. [6] [7]

2.2 Financial Habits and Their Impact on

Overall Financial Behavior

Understanding consumers’ financial habits, such as donating, in-
vesting, saving, and borrowing, provides crucial insights into their
overall financial behavior, as these actions are interconnected
within a broader financial planning framework.
Influenced by
factors like financial satisfaction, social norms, and financial liter-
acy, these habits reflect varying levels of financial resilience and
planning. For instance, consistent saving and investing often signal
proactive financial management, while responsible borrowing and

Figure 1: Conceptual Framework

charitable giving may indicate confidence and discipline. However,
many consumers lack sufficient financial knowledge, which can
lead to poor decisions and financial instability. Studies emphasize
that financial education and behavioral insights are essential for
promoting informed, responsible financial behavior and long-term
well-being. [8] [9]

2.3 Monthly Transactions as they affect
Financial Habits and Behavior

The frequency of monthly transactions on server-based electronic
money (SBEM) platforms significantly shapes users’ financial habits
by promoting convenience and streamlining decision-making. As
consumers increasingly rely on digital wallets and mobile pay-
ments, they adopt new spending behaviors characterized by fre-
quent, smaller transactions. This shift, driven by ease of access and
speed, can lead to improved budgeting through transaction tracking
but also raises concerns about impulsive spending. Regular use of
SBEM fosters deeper engagement with digital finance, encourag-
ing users to explore advanced features like automated savings and
embedded credit tools. Aligned with the Technology Acceptance
Model, this trend highlights how perceived usefulness and ease of
use drive adoption, ultimately transforming traditional financial
practices into more dynamic, data-driven approaches. [10]

3 METHODOLOGY
3.1 Research Design
This study used a quantitative approach to explore how financial
habits—such as saving, spending, donating, investing, and man-
aging credit or loans—affect consumer financial behavior in the
context of server-based electronic money (SBEM). It also examined
whether the average number of monthly transactions moderates
these relationships, revealing how transaction frequency can influ-
ence the strength of financial habit effects. Guided by the Theory
of Planned Behavior (TPB), the research identified key psycholog-
ical and behavioral factors shaping financial actions in a digital
environment. Figure 1 shows how TPB concepts were integrated
to provide a comprehensive analysis of how individual financial
habits collectively influence broader financial behaviors, offering

---

<!-- PAGE 3 -->

Consumer’s Financial Habits on Server-Based Electronic Money as It Affects Their Financial Behavior: Moderated
By Monthly Transactions

ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

insights into the evolving nature of consumer engagement with
digital financial platforms. [11]

3.2 Sampling
The researchers employed a purposive sampling technique to select
300 participants for their study, ensuring demographic represen-
tation across age, gender, income/allowance, and occupation. Par-
ticipants were comprehensively briefed on the study’s objectives
and guaranteed confidentiality in accordance with ethical stan-
dards. This sampling method was deemed suitable as it targeted
individuals capable of providing valuable insights into how various
financial behaviors, namely saving, spending, donating, investing,
and managing credit or loans, impact engagement with server-
based electronic money platforms. Furthermore, the study aims
to investigate how the average number of monthly transactions
influences these relationships. The selection criteria encompassed
being a Filipino user of GCash, aged between 18 and 60, and actively
participating in at least one of the specified financial behaviors.

3.3 Research Instrument
The study utilized online questionnaires distributed through Google
Forms and social media to collect primary data on respondents’
financial behaviors related to various features of GCash. A 5-point
Likert Scale was used in the questionnaire to evaluate attitudes
and perceptions across several sections, including demographic
profiling, saving behaviors influenced by GCash’s GSave, spending
habits shaped by cashless transactions, and the impact of GCash’s
donation platform. Additional sections examined the effects of GIn-
vest on investment behavior, GCash’s credit features, and average
monthly transaction patterns among users. Ultimately, the research
aimed to quantify how digital payment tools like GCash influence
consumer financial decision-making and encourage responsible
financial behavior.

3.4 Statistical Treatment
In this study, multiple regression analysis was employed to inves-
tigate the extent to which specific financial habits—namely sav-
ing, spending, donating, investing, and managing credit or loans—
predict consumer financial behavior in the context of server-based
electronic money. This statistical method allowed for the simulta-
neous examination of multiple independent variables to determine
their individual and collective influence on the dependent vari-
able, financial behavior [12]. To further explore the dynamics of
this relationship, a moderation analysis was conducted to assess
whether the frequency of monthly transactions moderated the ef-
fect of financial habits on financial behavior [13]. By incorporating
this interaction term, the analysis aimed to reveal whether the
strength or direction of the relationship between financial habits
and behavior varied depending on the level of monthly engagement
with server-based electronic money platforms. This dual approach
provided a more nuanced understanding of how digital financial
activity shapes consumer behavior patterns.

4 Results and Discussions
4.1 Assumption Check
Before conducting multiple regression analyses, the dataset under-
went diagnostic tests to ensure model reliability, including checks
for autocorrelation, multicollinearity, and residual normality. The
regression model, grounded in the study’s conceptual framework,
examined how five independent variables—Saving Habit, Spend-
ing Habit, Donating Habit, Investment Habit, and Credit/Loan
Habit—affect Consumer Financial Behavior. Collinearity statis-
tics showed acceptable VIF values (1.26–1.80), indicating no serious
multicollinearity. The Durbin-Watson statistic of 1.73 suggested no
significant autocorrelation, and the Shapiro-Wilk test confirmed
that residuals were approximately normally distributed. These re-
sults validate the model’s assumptions, supporting the reliability
and validity of its findings. [14] [15]

4.2 Model Fit Measures
The comprehensive evaluation of model fit indicators show that
the regression model is both statistically significant and reliable.
The correlation coefficient (R = 0.633) reveals a strong positive
relationship between the independent variables and Consumer
Financial Behavior, while the coefficient of determination (R2 =
0.400) indicates that 40% of the variance in the dependent variable is
explained by the model. The RMSE of 0.502 suggests that prediction
errors are minimal, reinforcing the model’s accuracy. Additionally,
the F-test result (F(5, 927) = 39.6, p < 0.001) confirms the overall
significance of the model, meaning at least one independent variable
has a meaningful impact. Together, these metrics demonstrate that
the model provides a solid and dependable fit for the data. [16]

4.3 The Financial Habits of Consumers and
Their Impact on Financial Behavior

This study aimed to investigate how specific financial habits, such
as budgeting, saving, spending, donating, and managing credit,
affect consumer behavior on GCash, a widely used mobile wallet
in the Philippines. Using multiple regression analysis, the research
examined how these habits influence users’ interactions with the
platform, including transaction frequency, fund management, and
usage for bill payments and online shopping. The study also ex-
plored the moderating role of monthly transaction frequency, of-
fering insights into how consistent engagement with GCash can
shape financial decision-making and promote better financial man-
agement strategies.

The results in Table 1 revealed that four out of five financial
habits, investment, saving, donating, and spending, significantly in-
fluence consumer financial behavior on GCash. Investment habits
had the strongest impact, followed by spending and saving habits,
all of which were positively associated with effective financial man-
agement and platform engagement. Donating habits also showed
a meaningful influence, suggesting that users value GCash’s con-
venience for charitable contributions. The low standard errors in
the regression estimates indicate high precision and reliability of
the findings. Overall, the study highlights the critical role of digi-
tal platforms like GCash in fostering positive financial habits and

---

<!-- PAGE 4 -->

ICBIM 2025, September 19–21, 2025, Bangkok, Thailand

Ramachandra Torres et al.

Hypothesis

Predictor

𝛽

SE

t

p

Interpretation

Table 1: Coefficients for the Regression Model

H1
H2
H3
H4
H5
Dependent Variable: Consumer Financial Behavior; 𝛽 – Coefficients; *Highly significant at 0.01

0.178*
0.115*
0.144*
0.243*
-0.003

3.820
3.047
3.014
4.896
-0.056

0.047
0.038
0.048
0.050
0.047

SH
SPH
DH
IH
CLH

< .001
0.003
0.003
< .001
0.955

Significant
Significant
Significant
Significant
Not Significant

suggests that enhancing user experience could further improve
financial engagement and behavior. [17]

behavior, ultimately supporting responsible financial practices and
contributing to a more sustainable digital economy.

4.4 Moderation Analysis
This study investigated how average monthly transactions on
GCash moderate the relationship between users’ financial habits
and their overall financial behavior. Using multiple regression
analysis with an interaction term, the research found that only
one moderation effect, between spending habit and transaction fre-
quency, was statistically significant (t = -4.6, 𝛽 = -0.1629, p < 0.001).
This result indicates that frequent GCash transactions significantly
influence how spending habits affect financial behavior, suggest-
ing that users who transact more often may experience different
behavioral outcomes compared to less frequent users. The findings
highlight the importance of usage patterns in shaping financial
behaviors on digital platforms. [18]

The simple slope analysis indicates that at low and average levels
of monthly transactions, the effect of spending habits on financial
behavior is positive but relatively modest. These results suggest that
as monthly transactions increase, the positive impact of spending
habits on financial behavior becomes more pronounced. Therefore,
users with low to average monthly transactions in GCash may
utilize the platform to manage and control their financial transac-
tions effectively, while also spending more when making purchases
through GCash.

5 CONCLUSION AND RECOMMENDATIONS
This study offers a detailed analysis of how consumer financial
habits—specifically saving, spending, donating, and investing—
affect financial behavior on the GCash platform, with a focus on
the moderating role of monthly transaction frequency. The findings
reveal that each habit significantly influences user engagement and
financial outcomes, with investment and spending habits showing
particularly strong effects. Notably, the frequency of monthly trans-
actions intensifies the impact of spending habits, suggesting that
users who transact more often experience greater behavioral shifts.
These insights emphasize the importance of fostering positive fi-
nancial habits and optimizing digital platform features to enhance
financial management. The study also recommends improving user
interfaces and developing targeted strategies to guide spending

References
[1] Hidayati, Istiqlaliah & Polytechnique, Telkom. (2012). Evaluating the role of L1
in teaching receptive skills and grammar in EFL classes. Indonesian Journal of
Applied Linguistics. 1. 10.17509/ijal.v1i2.82.

[2] Jílková, P., & Králová, P. (2021). Digital consumer behaviour and eCommerce
trends during the COVID-19 crisis. International Advances in Economic Research,
27(1), 83–85. https://doi.org/10.1007/s11294-021-09817-4.

[3] Lai, P. C. (2016). Design and security impact on consumers’ intention to use
single platform e-payment. Interdisciplinary Information Sciences, 22(1), 111–122.
https://doi.org/10.4036/iis.2016.R.05.

[4] Bangko Sentral ng Pilipinas.

(2020). Digital payments transformation
roadmap2020–2023. https://www.bsp.gov.ph/Media_And_Research/Primers%
20Faqs/Digital%20Payments%20Transformation%20Roadmap%20Report.pdf
[5] Globe Telecom. (2022, May 24). GCash achieves new milestone with over 60M reg-
istered users. https://www.globe.com.ph/about-us/newsroom/consumer/gcash-
new-milestone-over-60m-registered-users.

[6] Gomber, P., Koch, J.-A., & Siering, M. (2017). Digital Finance and FinTech: current

research and future research directions. Journal of Business Economics.

[7] Tiony, O. K., & Yin, Y. K. (2023). The Impact of Digital Financial Services on Finan-
cial Inclusion in Kenya. American Journal of Industrial and Business Management,
13, 593-628. doi: 10.4236/ajibm.2023.136035.

[8] Yeo, K. H. K., Lim, W. M., & Yii, K. J. (2024). Financial planning behaviour: a
systematic literature review and new theory development. Journal of Financial
Services Marketing.

[9] Raaij, W. F. (2016). Understanding Consumer Financial Behavior: Money Man-

agement in an Age of Financial Illiteracy. Springer.

[10] Ma, Q., & Liu, L. (2004). The Technology Acceptance Model: A Meta-Analysis of
Empirical Findings. Journal of Organizational and End User Computing, 16(1),
59–72. Retrieved from ResearchGate

[11] Bosnjak, M., Ajzen, I., & Schmidt, P. (2020). The Theory of Planned Behavior:
Selected Recent Advances and Applications. Europe’s Journal of Psychology,
16(3), 352–356. https://doi.org/10.5964/ejop.v16i3.3107

[12] Nayebi, H. (2020). Multiple Regression Analysis. In Advanced Statistics for Testing
Assumed Causal Relationships (pp. 1–46). Springer. https://doi.org/10.1007/978-
3-030-54754-7_1

[13] Memon, M. A., Cheah, J.-H., Ramayah, T., Ting, H., Chuah, F., & Cham, T. H.
(2019). Moderation Analysis: Issues and Guidelines. Journal of Applied Structural
Equation Modeling, 3(1), i–xi.

[14] Sevier, F. A. C. (1957). Testing the assumptions underlying multiple regression.
Journal of Experimental Education, 25, 323–330. https://doi.org/10.1080/00220973.
1957.11010578

[15] O’Brien, R. M. (2007). A caution regarding rules of thumb for variance inflation
factors. Quality & Quantity, 41(5), 673-690. https://doi.org/10.1007/s11135-006-
9018-6

[16] Miles, J., & Shevlin, M. (2001). Applying regression and correlation: A
guide for students and researchers. SAGE Publications. https://doi.org/10.4135/
9781849208963

[17] Kutner, M. H., Nachtsheim, C. J., & Neter, J. (2004). Applied Linear Regression

Models (4th ed.). McGraw-Hill/Irwin.

[18] McLeod, S. (2025). Moderating Variable in Statistics. Simply Psychology.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Consumer’s Financial Habits on Server-Based Electronic Money
as It Affects Their Financial Behavior: Moderated By Monthly
Transactions
∗
RamachandraCastroTorres GlobienMaitreOlaivar StevenIanBritanico
MapuaMalayanCollegesLaguna MapuaMalayanCollegesLaguna MapuaMalayanCollegesLaguna
CabuyaoCity,Philippines CabuyaoCity,Philippines CabuyaoCity,Philippines
rctorres@mcl.edu.ph 2022gmolaivar@live.mcl.edu.ph sicbritanico@live.mcl.edu.ph
Abstract (ICBIM2025),September19–21,2025,Bangkok,Thailand.ACM,NewYork,
This study investigates the impact of various financial habits— NY,USA,4pages.https://doi.org/10.1145/3785171.3785192
specificallysaving,spending,donating,investing,andcredit/loan
1 INTRODUCTION
behaviors—onconsumerfinancialbehavior,withtransactionfre-
quencyservingasamoderatingfactor. GroundedintheTheory Inrecentyears,rapidtechnologicalinnovationshavesignificantly
ofPlannedBehavior,theresearchutilizedaquantitativeapproach, transformedconsumerbehavior,particularlythroughtherising
collectingdatafromatargetedgroupofelectronicmoneyusers popularity of e-commerce and the use of electronic wallets (e-
(GCash)throughpurposivesampling.Themultipleregressionanal- wallets) for online transactions. As consumers seek more con-
ysesrevealedthatallfinancialhabits, exceptforcredit/loanbe- venientandefficientwaystoshop,traditionalpaymentmethods—
haviors,significantlyinfluencefinancialbehavior. Additionally, suchascashandcreditcards—areincreasinglybeingreplacedby
moderationanalysisdemonstratedthathighertransactionvolumes morepracticalandsecurealternatives[1].
enhancetherelationshipbetweenspendinghabitsandfinancial Advancementsindigitalwallettechnologyhaveplayedacru-
behavior,emphasizingtheroleofmobilewalletusageinreinforcing cialroleinthistransition.E-walletsallowuserstostorepayment
thesespendingpatterns.Thesefindingsprovidevaluableinsights informationandmaketransactionsquicklyandsecurelyfromtheir
forfintechcompanies,enablingthemtoimproveplatformusability mobiledevicesorcomputers. Featuressuchasbiometricsecurity,
andfinancialmanagementtools,ultimatelypromotingresponsible real-timetransactionnotifications,anddigitalreceipttrackingen-
financialhabitsamongusers. Consumerscangainaclearerun- hancetheuserexperienceandbuildtrustamongconsumers. The
derstandingofhowmobilewalletsaffecttheirfinancialdecisions, shifttowarde-commerceande-walletshasbeenacceleratedbythe
encouragingmoreinformedspendingandsavingpractices. Fu- globalpandemic,whichforcedmanybusinessestoadapttoonline
tureresearchshoulddelvedeeperintolong-termbehavioraltrends, sellingandconsumerstoseekcontactlesspaymentoptions. This
qualitativeinsights,andthepsychologicalfactorsdrivingdigital trendhighlightstheimportanceofdigitalwalletsasnotonlyasafer
financialbehavior,offeringabroaderperspectiveonhowtechnol- alternativebutalsoaconvenientchoiceforeverydaytransactions
ogyshapesfinancialhabitsovertime.Byexploringtheseareas,the [2].
evolvinglandscapeofconsumerfinanceinthedigitalagecanbe Giventhesechanges,itisessentialtoexploretheimplications
understoodfurther. ofdigitalwalletsonconsumerbehavior. Understandinghowthese
technologiesaffectpurchasingdecisions,trustinonlineplatforms,
CCSConcepts andoverallsatisfactioncanprovidevaluableinsightsforbusinesses
• Applied computing → Law, social and behavioral sciences; aimingtomeettheevolvingneedsoftheircustomersinthisdy-
namiclandscape.
Economics.
Server-basedelectronicmoneysystemsofferenhancedsecurity
Keywords featuresdesignedtomitigatetherisksassociatedwithelectronic
transactions. Ane-wallet,asdefinedbytheBankforInternational
Server-BasedElectronicMoney,GCash,style,FinancialBehavior,
Settlements,isanon-cashpaymentdevicethatincorporatesstored
insert
valueorprepaidproductsonanelectronicdeviceutilizedbythe
ACMReferenceFormat: consumer.Supportingthisconcept,astudyconductedbyLai[3]
RamachandraCastroTorres,GlobienMaitreOlaivar,andStevenIanBritan- indicatedthatincreasedsecuritymeasuresarepositivelycorrelated
ico.2025.Consumer’sFinancialHabitsonServer-BasedElectronicMoney
withaheightenedintentiontoutilizedigitalpaymenttechnologies.
asItAffectsTheirFinancialBehavior:ModeratedByMonthlyTransactions.
Concernssurroundingtherisksoftheftandlossassociatedwith
InThe9thInternationalConferenceonBusinessandInformationManagement
carryingcashandcardsrendersecurityacriticalfactorinfluencing
∗CorrespondingAuthor consumerdecision-makinginrelationtoelectronicpayments.
Thistrendisparticularlypronouncedindevelopingcountries
suchasthePhilippines,wherethedemandforcashlesstransac-
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. tionshasacceleratedfollowingtheendorsementofe-bankingand
ICBIM2025,Bangkok,Thailand e-walletsbytheBangkoSentralngPilipinas,thecountry’sbanking
©2025Copyrightheldbytheowner/author(s).
regulatoryauthority[4].Asof2023,thePhilippineshaswitnessed
ACMISBN979-8-4007-2217-2/2025/09
https://doi.org/10.1145/3785171.3785192 aconsiderablesurgeintheadoptionofe-wallets,exemplifiedby
52

ICBIM2025,September19–21,2025,Bangkok,Thailand RamachandraTorresetal.
GCash,whichhasattainedanotablemilestoneofover60million
registeredusersnationwide[5].Thiswidespreadacceptanceunder-
scoresGCash’ssignificanceasavirtualwalletthatfacilitatessecure,
rapid,andconvenientmoneytransfers,therebytransformingthe
digitalpaymentslandscapeinthePhilippines.
Initiallylaunchedin2004, GCashgainedsubstantialtraction
during the COVID-19pandemic, buoyed by regulatory support
andstrategicinnovationsfromtelecommunicationsleadersSmart
CommunicationsandGlobeTelecom. Presently,GCashservesa
crucialroleinpromotingfinancialinclusion,offeringaversatile
platformforvarioustransactions,includingbillpayments,money
transfers,andmobilecommerce[5].
Thisstudyaimedtoinvestigatetheeffectsofserver-basedelec-
tronicmoney,specificallyfocusingonGCash,onconsumers’finan-
cialbehaviors.Itexploredvariousaspectssuchassaving,spending,
Figure1:ConceptualFramework
donating,investing,andcreditorloanhabitstounderstandhowfac-
torslikespecificfinancialpracticesandtheaccessibilityofGCash
influencedconsumeruseoftheplatform. Thisresearchsought
charitablegivingmayindicateconfidenceanddiscipline. However,
toilluminatehowthesefactorsshapedfinancialdecision-making
manyconsumerslacksufficientfinancialknowledge,whichcan
processes. Additionally,thestudyexaminedtherelationshipbe-
leadtopoordecisionsandfinancialinstability.Studiesemphasize
tweenfinancialhabitsandtheaveragefrequencyoftransactions
thatfinancialeducationandbehavioralinsightsareessentialfor
permonth,analyzinghowthisusagefrequencyaffectedconsumers’
promotinginformed,responsiblefinancialbehaviorandlong-term
overallfinancialbehavior.Byestablishingthisconnection,there-
well-being.[8][9]
searchaimedtoprovideinsightsintotheimpactofGCashonthe
financialchoicesandpracticesofitsusers.
2.3 MonthlyTransactionsastheyaffect
FinancialHabitsandBehavior
2 LITERATUREREVIEW
Thefrequencyofmonthlytransactionsonserver-basedelectronic
2.1 Server-BasedElectronicMoneyand
money(SBEM)platformssignificantlyshapesusers’financialhabits
FinancialBehavior
bypromotingconvenienceandstreamliningdecision-making. As
Theemergenceofserver-basedelectronicmoney(SBEM),includ- consumers increasingly rely on digital wallets and mobile pay-
ingdigitalwalletsandmobilepaymentplatforms,hastransformed ments,theyadoptnewspendingbehaviorscharacterizedbyfre-
consumerfinancialbehaviorbyenhancingconvenience,accessibil- quent,smallertransactions.Thisshift,drivenbyeaseofaccessand
ity,andtransactionspeed. Operatingthroughcentralizedservers, speed,canleadtoimprovedbudgetingthroughtransactiontracking
SBEMenablessecure,real-timetransactionswithouttheneedfor butalsoraisesconcernsaboutimpulsivespending. Regularuseof
physicalcashortraditionalbanking. StudiesshowthatFinTech SBEMfostersdeeperengagementwithdigitalfinance,encourag-
innovationshaveledtomorefrequentsmall-valuetransactions, inguserstoexploreadvancedfeatureslikeautomatedsavingsand
increasedrelianceonmobiledevices,andashifttowardcashless embeddedcredittools.AlignedwiththeTechnologyAcceptance
economies,reflectingbothtechnologicalandpsychologicalchanges. Model,thistrendhighlightshowperceivedusefulnessandeaseof
SBEM also promotes financial inclusion and literacy, especially usedriveadoption,ultimatelytransformingtraditionalfinancial
amongunderservedpopulations,bysimplifyingsaving,borrowing, practicesintomoredynamic,data-drivenapproaches.[10]
andriskmanagement. However,withoutproperfinancialeduca-
tion,thesetoolsmayalsoencourageimpulsivespending,highlight- 3 METHODOLOGY
ingtheneedforabalancedunderstandingoftheirbenefitsand
3.1 ResearchDesign
risks.[6][7]
Thisstudyusedaquantitativeapproachtoexplorehowfinancial
habits—suchassaving,spending,donating,investing,andman-
2.2 FinancialHabitsandTheirImpacton
agingcreditorloans—affectconsumerfinancialbehaviorinthe
OverallFinancialBehavior
contextofserver-basedelectronicmoney(SBEM).Italsoexamined
Understandingconsumers’financialhabits,suchasdonating,in- whethertheaveragenumberofmonthlytransactionsmoderates
vesting,saving,andborrowing,providescrucialinsightsintotheir theserelationships,revealinghowtransactionfrequencycaninflu-
overall financial behavior, as these actions are interconnected encethestrengthoffinancialhabiteffects.GuidedbytheTheory
within a broader financial planning framework. Influenced by ofPlannedBehavior(TPB),theresearchidentifiedkeypsycholog-
factorslikefinancialsatisfaction,socialnorms,andfinancialliter- icalandbehavioralfactorsshapingfinancialactionsinadigital
acy,thesehabitsreflectvaryinglevelsoffinancialresilienceand environment.Figure1showshowTPBconceptswereintegrated
planning.Forinstance,consistentsavingandinvestingoftensignal toprovideacomprehensiveanalysisofhowindividualfinancial
proactivefinancialmanagement,whileresponsibleborrowingand habitscollectivelyinfluencebroaderfinancialbehaviors,offering
53

Consumer’sFinancialHabitsonServer-BasedElectronicMoneyasItAffectsTheirFinancialBehavior:Moderated
ByMonthlyTransactions ICBIM2025,September19–21,2025,Bangkok,Thailand
insightsintotheevolvingnatureofconsumerengagementwith 4 ResultsandDiscussions
digitalfinancialplatforms.[11]
4.1 AssumptionCheck
Beforeconductingmultipleregressionanalyses,thedatasetunder-
wentdiagnosticteststoensuremodelreliability,includingchecks
3.2 Sampling
forautocorrelation,multicollinearity,andresidualnormality.The
Theresearchersemployedapurposivesamplingtechniquetoselect regressionmodel,groundedinthestudy’sconceptualframework,
300participantsfortheirstudy,ensuringdemographicrepresen- examinedhowfiveindependentvariables—SavingHabit,Spend-
tationacrossage,gender,income/allowance,andoccupation.Par- ing Habit, Donating Habit, Investment Habit, and Credit/Loan
ticipantswerecomprehensivelybriefedonthestudy’sobjectives Habit—affect Consumer Financial Behavior. Collinearity statis-
and guaranteed confidentiality in accordance with ethical stan- ticsshowedacceptableVIFvalues(1.26–1.80),indicatingnoserious
dards. Thissamplingmethodwasdeemedsuitableasittargeted multicollinearity. TheDurbin-Watsonstatisticof1.73suggestedno
individualscapableofprovidingvaluableinsightsintohowvarious significantautocorrelation,andtheShapiro-Wilktestconfirmed
financialbehaviors,namelysaving,spending,donating,investing, thatresidualswereapproximatelynormallydistributed.Thesere-
and managing credit or loans, impact engagement with server- sultsvalidatethemodel’sassumptions,supportingthereliability
basedelectronicmoneyplatforms. Furthermore,thestudyaims andvalidityofitsfindings.[14][15]
toinvestigatehowtheaveragenumberofmonthlytransactions
influencestheserelationships.Theselectioncriteriaencompassed
4.2 ModelFitMeasures
beingaFilipinouserofGCash,agedbetween18and60,andactively
participatinginatleastoneofthespecifiedfinancialbehaviors. Thecomprehensiveevaluationofmodelfitindicatorsshowthat
theregressionmodelisbothstatisticallysignificantandreliable.
The correlation coefficient (R = 0.633) reveals a strong positive
3.3 ResearchInstrument relationship between the independent variables and Consumer
FinancialBehavior,whilethecoefficientofdetermination(R2 =
ThestudyutilizedonlinequestionnairesdistributedthroughGoogle
0.400)indicatesthat40%ofthevarianceinthedependentvariableis
Formsandsocialmediatocollectprimarydataonrespondents’
explainedbythemodel.TheRMSEof0.502suggeststhatprediction
financialbehaviorsrelatedtovariousfeaturesofGCash.A5-point
errorsareminimal,reinforcingthemodel’saccuracy.Additionally,
LikertScalewasusedinthequestionnairetoevaluateattitudes
theF-testresult(F(5,927)=39.6,p<0.001)confirmstheoverall
andperceptionsacrossseveralsections, includingdemographic
significanceofthemodel,meaningatleastoneindependentvariable
profiling,savingbehaviorsinfluencedbyGCash’sGSave,spending
hasameaningfulimpact. Together,thesemetricsdemonstratethat
habitsshapedbycashlesstransactions,andtheimpactofGCash’s
themodelprovidesasolidanddependablefitforthedata.[16]
donationplatform.AdditionalsectionsexaminedtheeffectsofGIn-
vestoninvestmentbehavior,GCash’screditfeatures,andaverage
monthlytransactionpatternsamongusers.Ultimately,theresearch 4.3 TheFinancialHabitsofConsumersand
aimedtoquantifyhowdigitalpaymenttoolslikeGCashinfluence
TheirImpactonFinancialBehavior
consumerfinancialdecision-makingandencourageresponsible
Thisstudyaimedtoinvestigatehowspecificfinancialhabits,such
financialbehavior.
as budgeting, saving, spending, donating, and managing credit,
affectconsumerbehavioronGCash,awidelyusedmobilewallet
inthePhilippines.Usingmultipleregressionanalysis,theresearch
3.4 StatisticalTreatment
examinedhowthesehabitsinfluenceusers’interactionswiththe
Inthisstudy,multipleregressionanalysiswasemployedtoinves- platform,includingtransactionfrequency,fundmanagement,and
tigatetheextenttowhichspecificfinancialhabits—namelysav- usageforbillpaymentsandonlineshopping. Thestudyalsoex-
ing,spending,donating,investing,andmanagingcreditorloans— ploredthemoderatingroleofmonthlytransactionfrequency,of-
predictconsumerfinancialbehaviorinthecontextofserver-based feringinsightsintohowconsistentengagementwithGCashcan
electronicmoney.Thisstatisticalmethodallowedforthesimulta- shapefinancialdecision-makingandpromotebetterfinancialman-
neousexaminationofmultipleindependentvariablestodetermine agementstrategies.
their individual and collective influence on the dependent vari- TheresultsinTable1revealedthatfouroutoffivefinancial
able,financialbehavior[12]. Tofurtherexplorethedynamicsof habits,investment,saving,donating,andspending,significantlyin-
thisrelationship,amoderationanalysiswasconductedtoassess fluenceconsumerfinancialbehavioronGCash.Investmenthabits
whetherthefrequencyofmonthlytransactionsmoderatedtheef- hadthestrongestimpact,followedbyspendingandsavinghabits,
fectoffinancialhabitsonfinancialbehavior[13].Byincorporating allofwhichwerepositivelyassociatedwitheffectivefinancialman-
this interaction term, the analysis aimed to reveal whether the agementandplatformengagement. Donatinghabitsalsoshowed
strengthordirectionoftherelationshipbetweenfinancialhabits ameaningfulinfluence,suggestingthatusersvalueGCash’scon-
andbehaviorvarieddependingonthelevelofmonthlyengagement venienceforcharitablecontributions.Thelowstandarderrorsin
withserver-basedelectronicmoneyplatforms. Thisdualapproach theregressionestimatesindicatehighprecisionandreliabilityof
providedamorenuancedunderstandingofhowdigitalfinancial thefindings. Overall,thestudyhighlightsthecriticalroleofdigi-
activityshapesconsumerbehaviorpatterns. talplatformslikeGCashinfosteringpositivefinancialhabitsand
54

ICBIM2025,September19–21,2025,Bangkok,Thailand RamachandraTorresetal.
Table1:CoefficientsfortheRegressionModel
| Hypothesis | Predictor | 𝛽      | SE    | t      | p     | Interpretation |     |
| ---------- | --------- | ------ | ----- | ------ | ----- | -------------- | --- |
| H1         | SH        | 0.178* | 0.047 | 3.820  | <.001 | Significant    |     |
| H2         | SPH       | 0.115* | 0.038 | 3.047  | 0.003 | Significant    |     |
| H3         | DH        | 0.144* | 0.048 | 3.014  | 0.003 | Significant    |     |
| H4         | IH        | 0.243* | 0.050 | 4.896  | <.001 | Significant    |     |
| H5         | CLH       | -0.003 | 0.047 | -0.056 | 0.955 | NotSignificant |     |
DependentVariable:ConsumerFinancialBehavior;𝛽–Coefficients;*Highlysignificantat0.01
suggeststhatenhancinguserexperiencecouldfurtherimprove behavior,ultimatelysupportingresponsiblefinancialpracticesand
financialengagementandbehavior.[17] contributingtoamoresustainabledigitaleconomy.
References
4.4 ModerationAnalysis
|                         |             |                      |     | [1] Hidayati,Istiqlaliah&Polytechnique,Telkom.(2012).EvaluatingtheroleofL1 |     |     |     |
| ----------------------- | ----------- | -------------------- | --- | -------------------------------------------------------------------------- | --- | --- | --- |
| This study investigated | how average | monthly transactions | on  |                                                                            |     |     |     |
inteachingreceptiveskillsandgrammarinEFLclasses.IndonesianJournalof
GCashmoderatetherelationshipbetweenusers’financialhabits AppliedLinguistics.1.10.17509/ijal.v1i2.82.
and their overall financial behavior. Using multiple regression [2] Jílková,P.,&Králová,P.(2021).DigitalconsumerbehaviourandeCommerce
analysiswithaninteractionterm, theresearchfoundthatonly trendsduringtheCOVID-19crisis.InternationalAdvancesinEconomicResearch,
27(1),83–85.https://doi.org/10.1007/s11294-021-09817-4.
onemoderationeffect,betweenspendinghabitandtransactionfre- [3] Lai,P.C.(2016).Designandsecurityimpactonconsumers’intentiontouse
quency,wasstatisticallysignificant(t=-4.6,𝛽 singleplatforme-payment.InterdisciplinaryInformationSciences,22(1),111–122.
=-0.1629,p<0.001).
https://doi.org/10.4036/iis.2016.R.05.
ThisresultindicatesthatfrequentGCashtransactionssignificantly
|     |     |     |     | [4] Bangko Sentral | ng Pilipinas. (2020). | Digital payments | transformation |
| --- | --- | --- | --- | ------------------ | --------------------- | ---------------- | -------------- |
influencehowspendinghabitsaffectfinancialbehavior,suggest- roadmap2020–2023.https://www.bsp.gov.ph/Media_And_Research/Primers%
ingthatuserswhotransactmoreoftenmayexperiencedifferent 20Faqs/Digital%20Payments%20Transformation%20Roadmap%20Report.pdf
|     |     |     |     | [5] GlobeTelecom.(2022,May24).GCashachievesnewmilestonewithover60Mreg- |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------------------------- | --- | --- | --- |
behavioraloutcomescomparedtolessfrequentusers.Thefindings isteredusers.https://www.globe.com.ph/about-us/newsroom/consumer/gcash-
highlighttheimportanceofusagepatternsinshapingfinancial new-milestone-over-60m-registered-users.
|     |     |     |     | [6] Gomber,P.,Koch,J.-A.,&Siering,M.(2017).DigitalFinanceandFinTech:current |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------------------------------- | --- | --- | --- |
behaviorsondigitalplatforms.[18]
researchandfutureresearchdirections.JournalofBusinessEconomics.
Thesimpleslopeanalysisindicatesthatatlowandaveragelevels [7] Tiony,O.K.,&Yin,Y.K.(2023).TheImpactofDigitalFinancialServicesonFinan-
ofmonthlytransactions,theeffectofspendinghabitsonfinancial cialInclusioninKenya.AmericanJournalofIndustrialandBusinessManagement,
13,593-628.doi:10.4236/ajibm.2023.136035.
behaviorispositivebutrelativelymodest.Theseresultssuggestthat [8] Yeo,K.H.K.,Lim,W.M.,&Yii,K.J.(2024).Financialplanningbehaviour: a
asmonthlytransactionsincrease,thepositiveimpactofspending systematicliteraturereviewandnewtheorydevelopment.JournalofFinancial
ServicesMarketing.
| habitsonfinancialbehaviorbecomesmorepronounced. |     | Therefore, |     |                                                                       |     |     |     |
| ----------------------------------------------- | --- | ---------- | --- | --------------------------------------------------------------------- | --- | --- | --- |
|                                                 |     |            |     | [9] Raaij,W.F.(2016).UnderstandingConsumerFinancialBehavior:MoneyMan- |     |     |     |
users with low to average monthly transactions in GCash may agementinanAgeofFinancialIlliteracy.Springer.
utilizetheplatformtomanageandcontroltheirfinancialtransac- [10] Ma,Q.,&Liu,L.(2004).TheTechnologyAcceptanceModel:AMeta-Analysisof
EmpiricalFindings.JournalofOrganizationalandEndUserComputing,16(1),
tionseffectively,whilealsospendingmorewhenmakingpurchases 59–72.RetrievedfromResearchGate
throughGCash. [11] Bosnjak,M.,Ajzen,I.,&Schmidt,P.(2020).TheTheoryofPlannedBehavior:
SelectedRecentAdvancesandApplications.Europe’sJournalofPsychology,
16(3),352–356.https://doi.org/10.5964/ejop.v16i3.3107
5 CONCLUSIONANDRECOMMENDATIONS
|     |     |     |     | [12] Nayebi,H.(2020).MultipleRegressionAnalysis.InAdvancedStatisticsforTesting |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------------------------------ | --- | --- | --- |
AssumedCausalRelationships(pp.1–46).Springer.https://doi.org/10.1007/978-
Thisstudyoffersadetailedanalysisofhowconsumerfinancial
3-030-54754-7_1
habits—specifically saving, spending, donating, and investing— [13] Memon,M.A.,Cheah,J.-H.,Ramayah,T.,Ting,H.,Chuah,F.,&Cham,T.H.
affectfinancialbehaviorontheGCashplatform,withafocuson (2019).ModerationAnalysis:IssuesandGuidelines.JournalofAppliedStructural
themoderatingroleofmonthlytransactionfrequency.Thefindings EquationModeling,3(1),i–xi.
|     |     |     |     | [14] Sevier,F.A.C.(1957).Testingtheassumptionsunderlyingmultipleregression. |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------------------------------- | --- | --- | --- |
revealthateachhabitsignificantlyinfluencesuserengagementand
JournalofExperimentalEducation,25,323–330.https://doi.org/10.1080/00220973.
1957.11010578
financialoutcomes,withinvestmentandspendinghabitsshowing
|     |     |     |     | [15] O’Brien,R.M.(2007).Acautionregardingrulesofthumbforvarianceinflation |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------------------------- | --- | --- | --- |
particularlystrongeffects.Notably,thefrequencyofmonthlytrans-
factors.Quality&Quantity,41(5),673-690.https://doi.org/10.1007/s11135-006-
| actionsintensifiestheimpactofspendinghabits,suggestingthat |     |     |     | 9018-6 |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | ------ | --- | --- | --- |
userswhotransactmoreoftenexperiencegreaterbehavioralshifts. [16] Miles, J., & Shevlin, M. (2001). Applying regression and correlation: A
guideforstudentsandresearchers.SAGEPublications.https://doi.org/10.4135/
Theseinsightsemphasizetheimportanceoffosteringpositivefi-
9781849208963
nancialhabitsandoptimizingdigitalplatformfeaturestoenhance [17] Kutner,M.H.,Nachtsheim,C.J.,&Neter,J.(2004).AppliedLinearRegression
Models(4thed.).McGraw-Hill/Irwin.
financialmanagement.Thestudyalsorecommendsimprovinguser
|     |     |     |     | [18] McLeod,S.(2025).ModeratingVariableinStatistics.SimplyPsychology. |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- |
interfacesanddevelopingtargetedstrategiestoguidespending
55