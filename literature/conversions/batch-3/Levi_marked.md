---
conversion_metadata:
  converted_at: "2026-07-21T13:56:57Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Levi.pdf"
  source_pdf_sha256: "87b5fe208f21faf447dec36d8e749761625e7e72622d2eed636c6bed6f88c93c"
  page_count: 74
  markdown_char_count: 220840
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Personal Financial Information Presentation and
Consumer Spending

Yaron Levi*

October 26, 2025

Abstract

We study whether information design influences consumer behavior in a randomized field

experiment with users of an online account aggregation app. Participants received a

personalized index representing their net worth as a lifetime monthly cash flow. The

presentation of this index varied across treatments in its framing and the salience of its

display. Consumers exposed to a consumption-oriented frame and a salient comparison of the

index with their past spending reduced discretionary spending. These findings show that

minor variations in information presentation can significantly affect financial behavior,

highlighting the power of design in promoting saving and informing policy and regulation.

JEL classification: D12, D14, D15, D91, G41, G51.

Keywords: Framing, Salience, Consumer Spending, Savings, Field Experiment.

*Yaron Levi, Yaron.Levi-1@ou.edu, University of Oklahoma Price College of Business. I am especially grateful to the editor, Ran Duchin,
for guidance and support throughout the review process. I would also like to thank Ivo Welch, Mark Garmaise, Shlomo Benartzi, Richard Thaler,

Stephen Spiller, David Hirshleifer, Tom Chang, Keith Chen, Mikhail Chernov, Cary Friedman, Noah Goldstein, Jinyong Hahn, Francis Longstaff,
Hanno Lustig, Richard Roll, Suzanne Shu, David Solomon, and seminar participants at UCLA Anderson, UCLA Behavioral Decision Making,
Vanderbilt, Boston College, Emory, Wharton, UT-Austin, Kellogg, USC, LSE, Columbia, Claremont, IDC, SFS Cavalcade, Boulder Summer Con-
ference on Consumer Financial Decision Making, CEPR European Summer Symposium in Financial Markets, and AFA for their comments and
discussions. Special thanks to Personal Capital for allowing me to conduct this study, and to the Hueler Companies for providing access to their
annuity quoting platform, Income Solutions®. I have no financial interest in any of the data providers, and I appreciate their commitment to science,
allowing me to publish the research regardless of the findings. This study does not use any personally identifiable information. The study was
exempt from IRB review by the Office of the Human Research Protection Program at USC (Study ID: UP-20-00254). The experiment described in
this paper was not pre-registered; it was conducted in 2014, before pre-registration became common practice in economics and finance.

---

<!-- PAGE 2 -->

I.

Introduction

Recent advancements in technology and the widespread use of online financial tools have

transformed the way individuals interact with their finances. Today, almost all financial services

are accessible through digital platforms, leading to a significant shift in how people manage their

money.1

When individuals access their online financial accounts, they can keep track of their

account balances and review recent transactions, which allows them to assess their financial

standing and plan their future spending. In this paper, we test if consumers are influenced by the

way in which their personal finances are presented. Changes in the presentation of information

can affect consumers’ sentiments, beliefs, or interpretation of the information and potentially lead

to a change in behavior.

We conducted a field experiment on the users of an online account aggregation software.

Account aggregation apps enable users to link various financial accounts such as checking,

savings, retirement, investment, mortgage, loans, and more, through a single application. This

aggregation provides users with a comprehensive and real-time overview of their finances,

including details such as net worth, total expenditures, expenditure breakdown by categories, and

income.2

1For instance, a considerable 71% of consumers in the U.S. with bank accounts utilize online banking services

(Federal Reserve Board (2016)).

2Examples of research using account aggregation data include studies conducted in the US (Gelman, Kariv,

Shapiro, Silverman, and Tadelis (2014), Baker (2018), D’Acunto, Rossi, and Weber (2023), Levi and Benartzi

(2020)), Brazil (Medina (2021)), Germany (Becker (2017), Br¨auer, Hackethal, and Hanspal (2022), UK

(Chronopoulos, Lukas, and Wilson (2020), Hacıo˘glu-Hoke, K¨anzig, and Surico (2021)) and Iceland

2

---

<!-- PAGE 3 -->

Users of the app were provided with a personalized index that represents their net worth as

a monthly cash flow. That is, instead of presenting net worth as a lump sum (e.g., $650,000), it

was presented as the equivalent inflation-protected lifetime monthly cash flow, which depends on

the user’s age and current market prices of life annuities (e.g., $2,000 per month for life). The

index provides a relatively convenient reference for spending in comparison to the lump sum

presentation, since consumers typically use monthly cash flows as a unit of measure for spending

(e.g., rent, mortgage, utilities are typically billed monthly). We discuss the index in Section II.

Users of the app were randomly assigned into treatment groups that varied in the

presentation of the index. The first variation in treatments was in the framing of the index. A

significant body of research shows that consumers’ perceived value and attractiveness of life

annuities depends on the frame used to describe them (Agnew, Anderson, Gerlach, and Szykman

(2008), Benartzi, Previtero, and Thaler (2011), Beshears, Choi, Laibson, Madrian, and Zeldes

(2014), Brown, Kling, Mullainathan, and Wrobel (2008,0), Brown, Kapteyn, and Mitchell (2016),

Goda, Manchester, and Sojourner (2014), Goedde-Menke, Lehmensiek-Starke, and Nolte (2014)).

Consumers place a higher value on annuities when the cash flow stream is described using

a consumption frame (using words such as “spend” and “payment”) than when described using an

investment frame (using words such as “invest” and “earnings”). The consumption frame prompts

individuals to reflect on a negative scenario in which they have to cut their spending due to a lack

of resources, leading them to place a higher value on lifetime monthly income. Fear appeal

messages have been widely studied and shown to influence attitude, intentions, and behaviors

(Carlin, Olafsson, and Pagel (2017), Carvalho, Olafsson, and Silverman (2019), Gathergood and Olafsson (2024),

Olafsson and Pagel (2018)). For a recent review of research utilizing transaction-level data, see Baker and Kueng

(2022).

3

---

<!-- PAGE 4 -->

effectively (Peters, Ruiter, and Kok (2013), Tannenbaum, Hepler, Zimmerman, Saul, Jacobs,

Wilson, and Albarrac´ın (2015), Witte (1996)).

We test if using the consumption frame to describe the index can also drive consumers to

adjust their spending levels. Accordingly, we use two different labels as the name of the index:

Financial Sustainability Index (FSI): This label prompts users to think of the index as a

reference to their spending activities. This name induces users to reflect on a scenario in which

their financial condition is no longer “sustainable” and are therefore forced to cut their spending.

Life Annuity Index (LAI): This label maintains a neutral tone and does not elicit any

specific emotions from users. It simply describes the index for what it is - a life annuity quote.

The second variation in the treatments is the salience of the comparison between the index

and the user’s historical spending levels. Some of the treatment groups were presented with a time

series plot that directly compares the index level with the user’s historical monthly spending

(hereafter “context plot”; see Figure 1). Users in treatments that did not receive the context plot

had access to the same information content. A time series plot of the index was presented on the

dashboard page, and a separate time series plot of historical spending was available on the app’s

Cash Flow page. However, without an explicit contrast between the index and spending, users are

less likely to reflect on the difference between the two and adjust their spending.3

We find that users who were presented with the consumption frame (i.e., FSI) and a

3The experiment included a third variation in the treatments in which the personalized index represented a cash

flow stream that starts at retirement rather than immediately. This variation did not have an impact on consumer

behavior even though it is similar to reporting standards of fund performance required by the SECURE Act (2019)

and common practices in the financial industry. This variation in treatments, the related treatment groups, and the

tests are presented in Appendix B.

4

---

<!-- PAGE 5 -->

context plot decreased their discretionary spending by about 15% relative to users who received

only the consumption frame with no plot or a context plot but with a neutral frame (i.e., LAI). The

decrease in discretionary spending started immediately after the launch of the experiment and

persisted throughout the eight months in which the experiment materials were presented on the

app. These consumers increased their spending levels only gradually after the removal of the

experiment content and converged to the spending levels of consumers in unaffected groups after

an additional eight months.

The decrease in spending is most pronounced in relatively “tempting” spontaneous

categories such as entertainment, restaurants, and clothing. This evidence is consistent with an

improved ability to apply self-control due to an increased feeling of guilt and regret if they were

to make the purchase (e.g., Hoch and Loewenstein (1991)). In contrast, we do not find a change in

non-discretionary spending such as gas, groceries, and utilities, which are difficult to adjust,

especially over a short time period.

Furthermore, we find a decrease in infrequent large-ticket transactions. This evidence is

consistent with Karlan, McConnell, Mullainathan, and Zinman (2016) and Sussman and Alter

(2012), showing that people tend to omit such “exceptional” transactions from their budget plan,

and that salient reminders promote consumers to stay within their means.

Additionally, users in the affected treatments also decreased their cash withdrawals,

representing an additional decrease in spending (i.e., not included in the discretionary spending

variable). This decline in cash withdrawals is consistent with the notion that individuals assign a

higher subjective value to cash transactions compared to non-cash transactions, leading them to

prioritize cutting back on cash transactions first (Raghubir and Srivastava (2008)).

Existing research on consumer spending has predominantly relied on either aggregate

5

---

<!-- PAGE 6 -->

consumption data or low-frequency consumer-level data. However, recent studies have begun to

leverage high-frequency transaction-level data, providing a more granular understanding of

consumer behavior. This body of literature demonstrates that consumers exhibit strong spending

habits, typically making gradual adjustments over an extended period in response to changes in

economic factors like interest rates, income, or credit availability (Baker and Kueng (2022),

Havranek, Rusnak, and Sokolova (2017), Ravina (2019)). This paper shows that even in the

presence of strong behavioral inertia, simple information design manipulations can prompt

consumers to rapidly adjust their spending levels. Importantly, the response is caused by a change

in consumers’ sentiment or a perceived change in financial well-being and not by a change in any

economic variable.

Consumers in the affected groups decreased their spending immediately after receiving

the experimental treatments. However, their spending increased only gradually after the

experiment content was removed. This pattern aligns with findings from prior studies

documenting a non-linear adjustment in spending habits (Chen and Ludvigson (2009), Ferson and

Constantinides (1991)1, Ganong and Noel (2019)). Specifically, these results are consistent with

the predictions of the model proposed by Yogo (2008), which incorporates habit formation into a

reference-dependent utility function with loss aversion. According to the model, a negative shock

elicits a larger response than a positive economic shock.

Framing effects have been extensively explored in the social sciences, demonstrating their

influence across various domains.4 However, framing information to specifically influence

4Previous studies, such as those by Andreoni (1995), De Martino, Kumaran, Seymour, and Dolan (2006),

Johnson, Hershey, Meszaros, and Kunreuther (1993), Payne, Sagara, Shu, Appelt, and Johnson (2013), Seibold

(2021), and Shafir, Diamond, and Tversky (1997), have documented the impact of framing on decision-making.

6

---

<!-- PAGE 7 -->

consumer spending poses unique challenges. First, it requires consumers to deviate from their

established spending habits, which are typically resistant to change. Second, there is a temporal

gap between the exposure to the experimental treatments and actual spending activity. Lastly, the

treatments employed in our study do not prescribe a specific course of action, leaving consumers

to decide if and how to adjust their spending. Nonetheless, this study demonstrates that through

online financial apps, where consumers are frequently exposed to the treatments, certain

information designs can indeed influence consumer spending.

Studies that examine framing effects on decision-making have often produced mixed

results. Maheswaran and Meyers-Levy (1990) showed that issue involvement, which refers to the

personal relevance and salience of an issue to an individual, is a key determinant of framing

effects. They further demonstrated that negatively framed messages are more influential when

they contain a high level of involvement. K¨uhberger (1998) conducted a meta-analysis of framing

experiments and concluded that salience manipulations are critical determinants of framing

effects. Consistent with this existing evidence, our study demonstrates that the fear appeal

message incorporated in the consumption frame has an impact on spending behavior, but only

when accompanied by a salient context. In other words, information must include both a relevant

framing and salient context for consumers to act upon it.

The paper contributes to the extensive body of research on tools aimed at increasing

consumers’ saving rates. Financial education programs have thus far proven to be costly and to

have negligible effects on saving behavior (Campbell (2006), Fernandes, Lynch Jr, and

Netemeyer (2014), Willis (2011)). Tax subsidies for retirement accounts tend to benefit wealthier

individuals, who are already better prepared for retirement (Chetty, Friedman, Leth-Petersen,

Nielsen, and Olsen (2014)). Employers’ matching contributions to retirement accounts have had

7

---

<!-- PAGE 8 -->

limited success in increasing saving rates (Choi, Laibson, Madrian, and Metrick (2002), Choi,

Laibson, and Madrian (2011), Duflo, Gale, Liebman, Orszag, and Saez (2006)). Behavioral tools

such as choice architecture, reminders, and information design have repeatedly been proven to be

powerful in influencing savings and retirement account contributions. (Bai, Chi, Liu, Tang, and

Xu (2021), Chetty et al. (2014), Choi et al. (2002), Choi, Laibson, Madrian, and Metrick (2004),

Karlan et al. (2016), Madrian and Shea (2001), Thaler and Benartzi (2004)). However, these

behavioral tools may not be applicable to a significant portion of nonretired households that have

no access to retirement accounts.5 In addition, the effect of an increase in retirement contributions

on the overall saving rate is mitigated by early withdrawal from these accounts (Argento, Bryant,

and Sabelhaus (2015), Beshears, Choi, Clayton, Harris, Laibson, and Madrian (2020a), Beshears,

Choi, Iwry, John, Laibson, and Madrian (2020b)) and an increase in borrowing activity (Beshears,

Choi, Laibson, Madrian, and Goda (2012)). This paper shows that information design can

influence spending, which is the flip side of savings. Given the wide use of online financial

services, information design tools can be easily implemented and distributed to a large mass of

consumers at a low cost, including lower-income individuals who have no retirement accounts.6

526% of nonretired households in the U.S. have no retirement savings (Board of Governors of the Federal

Reserve System (2021)).

6There is no formal data on the number of users of account aggregation apps globally. However, these apps are

available in most countries, with an increasing number of third-party providers and banks offering them as a free

service. The Open Banking regulation in Europe, particularly the Revised Payment Services Directive (PSD2), has

significantly boosted their development and usage by requiring banks to provide standardized access to customer

account information. Similar regulations are being adopted in many other countries, likely increasing the supply and

usage of personal financial management tools with account aggregation technology.

8

---

<!-- PAGE 9 -->

II. Personalized Index

Account aggregation apps typically present the users’ net worth as the first item on the

first page users visit after logging in. In this study, all treatment groups received a personalized

index that presented their net worth but with a change in the unit of measure. Instead of

presenting net worth as a lump sum, it was presented as the equivalent inflation-protected lifetime

monthly cash flow, which depends on the user’s age, state of residence, and current market prices.

This index reflects the market quote of a monthly cash flow from an immediate,

inflation-protected life annuity. Life annuities are sold by large financial institutions (typically

insurance companies) and provide a hedge for market, longevity, and inflation risks. By using the

market prices and current net worth of the user (instead of a projected future next worth), the

index does not require any assumptions.

Figure 2 illustrates the index dynamics in comparison to net worth as a lump sum in a

simplified life cycle model with no uncertainty. An individual with a known end-of-life date

receives a constant income flow every period until a known retirement age. Under any standard

preferences, the individual will perfectly smooth their consumption over their lifetime. Net worth

as a lump sum increases during the consumer’s working years, peaks at retirement age, decreases

over the retirement years, and depletes at the end of life. Net worth as a personalized index

describes the constant cash flow level that the consumer can generate for the rest of their life,

given their current net worth and time till the end of life. During the consumer’s working years,

like the lump sum, the index gradually increases. Two factors contribute to the rate of increase:

wealth accumulation and the shortening of remaining life. The index peaks at retirement age,

where it converges to the consumption level and remains constant until the end of life.

9

---

<!-- PAGE 10 -->

This index can potentially provide useful financial guidance for the individual. For a

person in retirement, the index accurately shows the optimal level of consumption in the

simplified framework described above. A person approaching retirement age can check whether

the consumption level is close to the index level. If the difference between spending and the index

levels is large, they can consider adjusting the consumption level, the income, or even the

retirement age. For a younger person, the index is significantly lower than the optimal

consumption level. That person can monitor whether the index level and the consumption level

converge quickly enough.

The presentation of the personalized index can impact consumers’ behavior through

several non-exclusive channels. First, the index might reduce consumers’ “illusion of wealth.”

Goldstein, Hershfield, and Benartzi (2016) show that, when net worth is sufficiently high, people

tend to perceive it as having a higher value than the equivalent monthly cash flow. The

presentation of net worth as a monthly cash flow instead of a lump sum might encourage users to

feel less wealthy and change their spending behavior.

Second, monthly cash flow is the commonly used unit of measure for spending, such as

monthly bills for rent, mortgage, and utilities. The presentation of net worth as a monthly cash

flow provides a reference point for spending activity that encourages consumers to mentally

simulate their lives under a different monthly budget. Reference-dependent utility consumers are

predicted to be especially sensitive to potential changes in their standard of living and might

therefore adjust their spending levels.

Third, the index might serve as an anchor for spending activity. Anchor effects occur

when an initial salient value influences individuals’ subsequent estimations or decisions. These

effects are especially pronounced when there are no other competing reference points or

10

---

<!-- PAGE 11 -->

information available (Kahneman (1992)). Given that consumers typically do not know their

optimal level of spending nor does the app provide any other benchmark for spending, the index

might have a strong impact as an anchor.

Note that none of these channels requires consumers to fully understand the economic

interpretation of the index. In fact, it is highly plausible that many users do not fully grasp its

meaning, since doing so would require relatively advanced financial and economic knowledge.

There are several reasons for using the index as the subject for information design

manipulations. First, it is a new information content that is not already available on the app. This

requirement ensures that all users have the same level of familiarity with the experimental content

and are not biased toward the old information design. Second, the selection of the index is

motivated by previous studies in behavioral economics, policy discussions, and practices in the

financial industry. The academic research discussed in Section I examines the effects of

information design manipulation on consumers’ demand for life annuities, providing a foundation

for exploring the impact of the personalized index on consumer spending in this study.

Additionally, the recent SECUREwhite Act (2019) requiring retirement account providers to

display the account’s worth as a projected lifetime monthly income and the offering of similar

personalized indices by the financial industry, such as “CoRI” by BlackRock, demonstrate the

applicability of the index to consumers’ spending and savings decisions.

III. Experimental Design

The experiment was embedded in a financial management app that is offered to the

general public at no cost. The first web page users view after logging into the app is the

11

---

<!-- PAGE 12 -->

“dashboard” page, which provides a brief summary of the user’s finances. The pre-experiment

dashboard page is presented in Figure C1. Users were randomly assigned to seven groups.7 Apart

from the control group, all treated groups received a personalized index. The treatments differed

in the name of the index and in the availability of a context plot. The treatments are summarized

in Table 1 and illustrated in Figure 1. The treatment groups are defined as follows:

Control Group (Figure C1): The dashboard page was not changed for users in this group.

The page includes time-series plots of net worth, total income, and total spending. This group

serves as a baseline to detect any changes in financial activity that are not related to the

experiment.

FSI-Plot Group (Figures C2, C3): Users received the Financial Sustainability Index,

which contains a fear appeal message. They also received a context plot providing a salient

comparison between the index level and historical monthly spending.

FSI-Plot-inf Group: Several studies have suggested that high annuities prices might

explain the low demand for life annuities.8 If annuities are overpriced, the consumers might

respond to the index because it quotes an overly pessimistic cash flow. To address this concern,

this group received the same treatment as the FSI-Plot group, except the quoted index was inflated

by 20%. A differential response between these two groups would indicate that the change in

behavior is sensitive to the exact quote used.

FSI-NoPlot Group (Figure C4): Users received the FSI and no context plot. By

comparing the behavior of this group to that of users in the FSI-Plot group we can identify the

impact of providing a salient comparison between the index and spending.

7Two of the seven groups are omitted from the main text and are described in Appendix ??.

8See the discussion in Benartzi et al. (2011), Brown and Orszag (2006), and Brown (2007).

12

---

<!-- PAGE 13 -->

LAI-Plot Group (Figure C5): Users received the Life Annuity Index and no context plot.

By comparing the behavior of this group to that of users in the FSI-Plot group, we can identify the

impact of the framing effect embedded in the index names.

The experiment did not include a treatment that presents the index using neutral framing

(LAI) with a context plot due to the limited number of users available for the experiment. As a

result, we only test the impact of the context plot in the presence of consumption framing.

Goldstein et al. (2016) and Goda et al. (2014) showed that individuals respond to

information about changes in their cash flow stream. Following their findings, users received

information about the sensitivity of the index level to changes in their net worth (“At current

market prices, an increase of $10,000 in your net worth will increase your [FSI/LAI] by $[X]”).

The dashboard page of all the treated groups included a link to a FAQ page. The FAQ for

each group was adjusted to reflect the corresponding index name. The FAQ page for the FSI-Plot

group is presented in Figures C8 and C9.

Historical monthly income was removed from the dashboard page in all treatments but

was available to all users on the Cash Flow page of the app. Kahneman (1992) shows that anchor

effects are especially pronounced when no other competing reference points or information is

available. The removal of monthly income from the landing page decreases the salience of this

information and potentially increases the likelihood of using the index as the new benchmark for

spending. In addition, historical monthly spending was not presented on the dashboard page for

treatments that did not receive a context plot. All users could view their historical spending on the

Cash Flow page of the app. The removal of monthly spending from the landing page reduces the

salience of this information and the ability of users to directly compare it to the index level.

13

---

<!-- PAGE 14 -->

IV. Data

A. Annuity Price Quotes

We obtain life annuity prices from Hueler’s Income Solutions® annuity quoting platform.

This platform allows individuals to receive customized quotes of identical annuity contracts from

large insurance companies in real time. All insurance companies that provide quotes are rated “A”

or above by Moody’s, S&P, and A.M. Best. The costs of investment management, distribution,

administration, and other costs associated with annuity products are reflected in the annuity

quotes. We use annuity quotes of inflation-protected life annuities for single, male buyers

(reflecting the majority of the app users) with a nonqualified income of $100,000. We obtain the

full annuities quotes grid for all ages between 35 and 85, all commencement dates between

immediate and the age of 85, and all states.9 Annuity quotes were updated once a week during the

experiment. The personal index for each user was calculated as the average quote from all

companies given the user’s age, state of residence, and net worth.

B. Consumer Data

The sample consists of users of the financial management app who are not clients or

prospective clients of the app provider’s wealth management services. We restrict the sample to

users above the age of 35, which is the minimum age of life annuity quotes. Additionally, retired

users are excluded from the sample to accommodate the two treatment groups where the index

9Two of the treatment groups in this study received a personalized index representing a cash flow stream starting

at retirement rather than immediately. Deferred annuities quotes were used for these two treatment groups. See details

in Appendix ??.

14

---

<!-- PAGE 15 -->

represents a deferred annuity quote with a commencement date at retirement. We keep users who

had been using the app for at least five months before the experiment.

The sample includes only users who logged into the app at least once in the three months

before the experiment, linked at least one credit or debit account, and had an average monthly

income and spending above $1,000 in the five months before the experiment launch. These

restrictions ensure that the sample includes only users who are actively using the app. We also

exclude users with a net worth below $5,000 so that the level of the personal index is sufficiently

positive.

Users of mobile financial apps log in to view their accounts more frequently than users

who log in only from personal computers (Carlin, Olafsson, and Pagel (2023)). To ensure

consistency in the level of exposure to the app and the experiment material, we include only users

who have installed the mobile app prior to the start of the experiment and had logged in using a

mobile device at least once in the three months before the experiment launch.

The final sample consists of 3,138 users. Data on users’ transactions and login activity are

collected for a period of 25 months, starting five months before the experiment launch and

continuing for twenty months after.

Table 3 presents summary statistics of the sample as documented on March 17, 2014, the

launch day of the experiment. The average age in the sample is 45. The average net worth is $1.1

million (median $0.6 million), and the average monthly income from all sources is $16.7K

(median $12.6K). The personalized index in this table was calculated for all users, including the

control group, as the average quote on an immediate inflation-protected life annuity. The average

index level is $3,175, and the median is $1,561. The average number of monthly logins during the

five months before the experiment’s launch is 15.4 (median of 7.6), indicating that users in the

15

---

<!-- PAGE 16 -->

sample are actively using the app. The average monthly spending is about $12K, and the median

is $9.2K. The spending levels of users in this sample are well above their personalized index

levels, as predicted for consumers relatively far from retirement age (see discussion in Section II

and Figure 2).

The main variable of interest is discretionary spending, which refers to spending on items

over which consumers have relatively more control and can adjust over a short period, such as

entertainment and restaurants. We define discretionary spending as the sum of spending in

categories that correspond to industries in the Consumer Discretionary sector according to the

Global Industry Classification Standard (GIC code 25). The complete list of categories with

example vendors for each category is presented in Table 2. The average level of discretionary

spending in this sample is $3,689 (median $2,789), constituting about 30% of overall spending.

We analyze expenditures on clothing, entertainment, restaurants, and travel, which are relatively

large components of discretionary spending. We also analyze cash withdrawals, which reflect

additional spending not included in the discretionary spending variable. The average monthly

cash withdrawal in this sample is $925, and the median is $355.

Overall, the consumers in this sample are relatively wealthy and are similar to consumers

in the 80th percentile of the income distribution based on their income level, overall spending,

and spending on the categories studied in this paper.10

10Based on the Consumer Expenditures Survey of the BLS.

16

---

<!-- PAGE 17 -->

V. Empirical Specification

Experiment materials were available on the app for a period of eight months. The data

cover the period from t=-5 to t=19, where the experiment launch month is t=0. We define two

indicator variables:

Intra: equals 1 for event months in which experiment material was presented on the app,

from t=0 to t=7.

P ost: equals 1 for event months after the removal of experimental material from the app,

from t=8 to t=19.

The main empirical specification is:

(1)

yi,t =

j=5
(cid:88)

j=2

βjT Gj,iIntrat +

j=5
(cid:88)

j=2

γjT Gj,iP ostt + δi + θj + ϵi,t

where y(i, t) is an outcome variable such as logins or log spending for consumer i in event month

t. T Gj are treatment group indicator variables for each of the groups, where the omitted group

serves as the reference level. δi is an individual fixed effect, and θj is an event-month fixed effect.

Standard errors are clustered at the consumer level.11

βj captures the average change in the outcome variable between the pre-experiment

months (t=-5 to t=-1) and the experiment months (t=0 to t=7) of consumers in treatment group j,

relative to the same change in the omitted treatment group. Similarly, γj captures the average

change in the outcome variable between the pre-experiment months (t=-5 to t=-1) and the

11All tests are robust to double clustering of the standard errors by consumer and year-month.

17

---

<!-- PAGE 18 -->

post-experiment months (t=8 to t=19) of consumers in treatment group j, relative to the same

change in the omitted treatment group.

In addition, we estimate the following specification for each of the treatment groups

separately:

(2)

yi,t =

t=19
(cid:88)

t=−4

βtI(t) + δi + ϵi,t

where I(t) is an event-month indicator for month t. βt captures the change in the outcome

variable in event month t relative to event month t=-5. This within-group time-series analysis

allows us to test the speed and duration of consumers’ response to the treatments.

VI. Results

A. Attention

The experiment content was presented at the top of the dashboard page, which is the first

page users see after logging into the app. Given this placement of the experiment content, login

activity measures users’ exposure to the experiment materials and level of attention to their

personal finances.

Table 4 reports the effect of the treatments on the users’ number of logins per month. The

reference treatment group in the first column is the control group. The coefficients of all the

interaction variables between the treatment indicators and Intra reveal that the change in

monthly logins between the the pre-experiment months and the experiment months is

18

---

<!-- PAGE 19 -->

significantly larger for all the treatment groups relative to the same change in the control group.

Users in each of the treatment groups increased their login frequency during the experiment

months by about 1.3 logins per month relative to the control group. The coefficients of the

interaction variables between the treatment indicators and P ost show that after the removal of the

experiment material, the change in login frequency of users in all treatment groups relative to the

pre-experiment months is still greater than the same change in the control group (about 0.6 more

monthly logins), but the difference is not statistically significant. Columns 2 and 3 repeat the

same regression with the FSI-Plot and FSI-Plot-inf groups as the baseline treatments. Although

all groups increased their attention level during the experiment months relative to the control

group, there are no notable differences in the login frequency across any of the other treatment

groups during or after the experiment.

The results for the time series analysis for each of the treatment groups are presented in

Figure 3 (formal results are in Table A1). Panel (a) displays the estimated coefficients in Equation

2, and panel (b) shows the average predicted values in each event month. The monthly login

frequency of the treatment groups is similar and highly correlated between all the groups before

the start of the experiment. At t=0 all the treated groups immediately diverge from the control

group, and the predicted login frequency remains higher throughout the experiment months. The

change in the login frequency of all the treated groups is still higher than that of the control group

for about three months after the experiment, after which all the groups converge to the same login

frequency.

Overall, the login analysis shows that users in all treated groups increased the level of

attention to their finances throughout the experiment months. The change in login frequency is

significant but small in magnitude, with only slightly more than one login per month relative to

19

---

<!-- PAGE 20 -->

the control group. The change in login frequency started immediately after the launch of the

experiment and can be attributed to interest in the new content on the app. The lack of difference

in login frequency across the treated groups reveals that the increased attention cannot be

attributed to any specific treatment feature, such as the index name or the presentation of a context

plot. Therefore, any differences in spending behavior across the different treatments can not be

attributed to a difference in consumers’ login frequency.

B. Discretionary Spending

Table 5 presents the analysis of the treatment effects on the log of discretionary spending.

The first column shows that both the FSI-Plot and the FSI-Plot-inf reduced their discretionary

spending during the experiment period by about 15% relative to the change in the control group

over the same period. None of the other groups had a significant change in their spending

behavior. Columns 2 and 3 formally show that there were no significant differences between the

FSI-Plot and the FSI-Plot-inf groups, and that the change in discretionary spending of these

groups is significantly lower than that of the FSI-NoPlot and the LAI-Plot groups. Using the

sample mean of monthly discretionary spending ($3,689), a 15% decline in discretionary

spending corresponds to a drop of $553 per month, which is about 4.5% of overall monthly

spending. The coefficients of the interaction variable between the treatment indicators and P ost

show that after the removal of the experiment material from the app, there were no significant

differences in discretionary spending between any of the groups.

This analysis confirms that information design can have a substantial impact on

consumers’ discretionary spending. However, the effect is sensitive to specific features in

20

---

<!-- PAGE 21 -->

information presentation. Consumers only respond when the index is presented both under the

consumption frame and contains a salient context. Presentation of either the consumption frame

or a salient context by itself does not yield a partial response. The lack of difference in effect size

between the FSI-Plot and FSI-Plot-inf groups indicates that the effect is robust to the exact quote

used in the index.

Treatments that did not receive a context plot with a consumption framing of the index

name did not show any differences in spending relative to the control group, suggesting that the

omission of monthly income and spending from the dashboard page did not impact users’

spending behavior. However, the decrease in spending in the FSI-Plot and the PSI-Plot-inf groups

might have been smaller in magnitude if income was still presented on the dashboard page,

providing a salient alternative benchmark for spending instead of the index.

Figure 4 shows the dynamics of the change in discretionary spending for each of the

experiment groups relative to their spending at t=-5 (formal results are in Table A2). The changes

in discretionary spending of all the groups are positively correlated and similar in magnitude

before the experiment launch. The peak in discretionary spending at t=-3 and the sharp decline at

t=-2 are driven by seasonal effects, with a high spending month in December followed by a low

spending month in January. The change in discretionary spending of the FSI-Plot and FSI-Plot-inf

groups diverge from all the other groups immediately at the launch of the experiment and remain

lower throughout the experiment. The gap between these two groups and all the other groups

remained large for three additional months after the experiment and gradually decreased

afterwards. The changes in discretionary spending of all the groups converge only at t=16, nine

months after the removal of the experimental content from the app.

The analysis in Figure 4 shows the within-group evolution of discretionary spending. To

21

---

<!-- PAGE 22 -->

test the persistence of the effect after the experiment duration across groups, we conduct an

additional analysis of discretionary spending over shorter periods than used in Equation 1. The

results of this analysis are presented in Table 6. The dependent variable is the log of discretionary

spending. The explanatory variables are the interactions of group indicators and a time period

indicator where the time period in each regression is listed at the top of the column. The control

group is the baseline group in all columns, and the reference time period is the five months before

the experiment launch.12 The first two columns show that the average change in discretionary

spending is about 15% lower than the change in the control group during the experiment months.

Column 3 shows that the decline in discretionary spending of the affected treatments during the

following four months remained about 15% lower than the change in the control group. However,

this effect is only significant at the 10% level. The magnitude of the change in these groups

decays over time, and the point estimates of all the groups are similar to each other between t=16

and t=19.

Overall, the analysis in Figure 4 and Table 6 shows that the treatments had lasting effects

beyond the period in which the experiment content was presented on the app. The FSI-Plot and

FSI-Plot-inf treatments groups reduced their discretionary spending immediately at the start of

the experiment but resumed their non-treatment levels of spending only after several months.

C. Spending Categories

In Table 7, we test the average spending response in different spending categories.

Column 1 shows that both the FSI-Plot and FSI-Plot-inf reduced their restaurant expenditures by

12The sample in each regression includes the pre-experiment months (t=-5 to t=-1) and the four months listed at

the top of each column.

22

---

<!-- PAGE 23 -->

about 14% relative to all the other groups during the experiment months. Restaurant spending is

relatively easy to adjust by visiting less expensive restaurants or dining at home. Users in these

groups also reduced their clothing expenditures by a significant 20% relative to the other groups

(Column 2). Clothing expenses can be relatively easily adjusted as well by reducing purchase

frequency or clothing price. Column 3 shows that users in the FSI-Plot and FSI-Plot-inf

treatments decreased their expenditures on entertainment by about 14% percent relative to the

change in other groups. Column 4 shows a decrease of about 24% in travel expenses for users in

these two groups. Travel is likely to be a luxury item for many consumers that can be adjusted by

choosing a more modest vacation or skipping it altogether.

Column 5 shows that consumers in the FSI-Plot and FSI-Plot-inf groups reduced their

cash withdrawals by about 25% compared to other groups. Unlike the previous spending

categories, cash withdrawals are not included in the discretionary spending variable. Therefore,

this decrease in cash withdrawals reflects an additional decrease in spending. This evidence is

consistent with consumers placing a higher subjective value on cash transactions and therefore

being more likely to reduce these transactions first (Raghubir and Srivastava (2008)).

Sussman and Alter (2012) classified transactions into ordinary (i.e., common and

frequent) transactions and exceptional (i.e., unusual or infrequent) transactions, with many of the

largest expenses being the most exceptional.13 They show that although consumers are fairly

skillful at planning their ordinary spending, they systematically underestimate their future

expenditures on exceptional items. Consumers tend to categorize each exceptional expense as a

unique occurrence and consequently overspend after a series of exceptional expenses. Moreover,

13See additional discussion in Karlan et al. (2016).

23

---

<!-- PAGE 24 -->

changes in large and infrequent expenditures might be easier to implement, as the consumer will

have to make a single (large) mental effort to apply self-control rather than exercise discipline and

sacrifice every day.

We test if the decrease in spending is a result of a reduction in spending on exceptional

expenses. We use the sum of the five largest transactions of each user in a given month as a proxy

for large and infrequent transactions.14 Note that the consumers’ largest transactions are typically

rent, mortgage, and loan payments. However, these expenses are typically constant over time and

are therefore absorbed by the consumer fixed effects. Column 6 shows that both the FSI-Plot and

FSI-Plot-inf groups significantly reduced their large transactions during the experiment months,

suggesting that these users avoided or reduced spending on infrequent large-ticket transactions.

Overall, the reduction in spending is driven by a decrease in both common and exceptional

transactions.

D. Additional Tests

In the first column of Table 8, we test the effect of the different treatments on the users’

overall spending level. We find a decline of about 6% in overall spending in the FSI-Plot and

FSI-Plot-inf groups relative to the change in any of the other treatment groups. However, this

decline is only significant at the 10% level. Given the average monthly mean of overall spending

of $12,364, a decrease of 6% in overall spending translates to a reduction of approximately $742

per month. This decrease roughly corresponds to the combined decrease in monthly discretionary

14Results are robust to the selected number of extreme transactions.

24

---

<!-- PAGE 25 -->

spending and cash withdrawals.15 In addition, we test the effect of the different treatments on

overall monthly spending minus discretionary spending and cash withdrawals and find no

significant differences between any of the groups. This evidence confirms that consumers did in

fact decrease their spending levels and did not shift their expenses from discretionary spending

and cash transactions to other spending categories.

As a falsification test, we check if there is a change in spending categories that are

relatively difficult to adjust, especially in the short run. We find no significant differences in

spending on gas, groceries, telephone, or utilities between any of the treatment groups (columns 2

to 5).

VII. Conclusion

This paper documents the critical impact of information design on consumers’ spending

behavior. The frame in which the information is presented and the salience of the context can

have a significant impact on consumers’ spending, despite strong behavioral inertia in spending

and the temporal distance between exposure to treatment and the spending activity. Furthermore,

the effects on spending behavior start immediately after the exposure to the treatment and last for

several months beyond the experiment duration, showing that the impact of the information

design lasts beyond the exposure to the treatment and supports an asymmetrical adjustment of

spending habits.

Information tools that influence spending behavior offer several advantages over the

15The decrease in monthly discretionary spending = 15% * $3,689 = $553. The decrease in monthly cash

withdrawals = 25% * $925 = $231.

25

---

<!-- PAGE 26 -->

existing tools aimed at influencing saving behavior. First, information design tools are easy to

implement at low cost relative to financial education, tax subsidies, and employer matching

contribution. Second, unlike choice architecture interventions, information design tools can be

applied to all consumers rather than only to individuals with retirement plans. Third, a decrease in

spending reflects an equal size increase in consumer savings. An increase in retirement plan

contributions might not reflect an increase in savings due to early withdrawals and an increase in

borrowing.

The sensitivity of individuals’ responses to subtle details in information presentation can

be leveraged by firms. For instance, wealth management companies can utilize information design

tools that enhance their clients’ saving rates. On the other hand, loan providers can strategically

design information to encourage consumers to increase their spending and borrowing levels.

Given the potential impact of information design on consumer behavior, policymakers

may need to consider regulations to protect consumers in this context. Current regulations on

information presentation already exist in various industries such as food, tobacco, alcohol, and

cosmetics, where warning labels are regulated in terms of content, size, location, and color.

However, in the realm of consumer finance, information design regulations are primarily limited

to areas such as interest rate quotes, credit card statements, and fee disclosure. By specifying

guidelines and standards for the presentation of personal financial information, policymakers can

mitigate deceptive practices by firms.

A common limitation of all research using transaction level data is the potential

incompleteness of the data. Data obtained from account aggregation apps, banks, or credit card

companies might not include all the consumers’ accounts. It is possible that the change in

spending behavior in the observed accounts is offset by an increase in spending in unobserved

26

---

<!-- PAGE 27 -->

accounts. Similar concerns existed in the retirement contribution literature for more than two

decades until Chetty et al. (2014) showed that an increase in retirement contributions does not

crowd out savings in other accounts. We mitigate this concern by selecting relatively active users

who are more likely to have linked all their accounts to the app.16

Another limitation caused by potential data incompleteness is the inaccurate estimation of

users’ net worth and personalized index. The omission of retirement or debt accounts will bias the

net worth presented on the app. Additionally, real assets such as real estate are not included in the

app. It is possible that consumers respond to the index they observe on the app even if it does not

reflect their real net worth. Alternatively, they might ignore the index if they feel that it does not

represent their current financial situation accurately.

This paper demonstrates the significant impact of information design on the spending

behavior of consumers who are relatively far from retirement and whose spending levels are

significantly above their index levels. Future research should explore the effects of providing

annuitized values to consumers at or near retirement. These consumers may have spending levels

below their annuitized net worth, and examining whether they increase their spending after being

exposed to the index could offer valuable insights into the retirement decumulation puzzle.17

Future research can explore the exact mechanisms through which the index influences

consumer behavior. One possibility is that the index provides new information that was not

previously available to consumers, expanding their information set and leading to improved

spending decisions. Another potential channel is that the index establishes a new reference point

16See Baker and Kueng (2022) for a full discussion on the limitations of research using transaction-level data.

17See Battistin, Brugiavini, Rettore, and Weber (2009) for a comprehensive review of the retirement decumulation

puzzle.

27

---

<!-- PAGE 28 -->

for spending, distinct from the reference point consumers previously used, such as monthly

income. Finally, it is possible that the index serves as an anchor for spending behavior, meaning

consumers might adjust their spending levels based on any random salient reference point

provided.

This study shows that the presentation of the index has a critical role in influencing

consumer behavior. The consumption frame used to describe the index potentially induces a

feeling of guilt and regret, leading to an improvement in consumers’ self-control through a

decrease in the temptation value of unnecessary spending (e.g., Baumeister (2002), Fudenberg

and Levine (2012), Hoch and Loewenstein (1991)). The context plot comparing the index to the

consumer spending primes users to take a specific action of cutting their spending and increasing

their savings (e.g., Gollwitzer and Sheeran (2006)). Future research can explore if similar

information designs can influence other consumers’ decisions, such as stock market participation,

debt repayment, and the claiming age of social security benefits.

Consumers use a variety of benchmarks for their spending behavior, such as their monthly

income or spending in the previous month. Recent studies have shown that providing consumers

with information about their peers’ income, debt, or spending levels can influence their own

spending behavior (D’Acunto et al. (2023), van Rooij, Coibion, Georgarakos, Candia, and

Gorodnichenko (2024)). This study demonstrates that consumers adjust their spending when

presented with the annuitized value of their net worth. Future research should explore which of

these benchmarks consumers perceive as most important and whether the presentation of single or

multiple benchmarks has a stronger impact on consumer spending.

28

---

<!-- PAGE 29 -->

References

Agnew, J. R.; L. R. Anderson; J. R. Gerlach; and L. R. Szykman. “Who chooses annuities? An

experimental investigation of the role of gender, framing, and defaults.” American Economic

Review, 98 (2008), 418–22.

Andreoni, J. “Warm-glow versus cold-prickle: the effects of positive and negative framing on

cooperation in experiments.” The Quarterly Journal of Economics, 110 (1995), 1–21.

Argento, R.; V. L. Bryant; and J. Sabelhaus. “Early withdrawals from retirement accounts during

the great recession.” Contemporary Economic Policy, 33 (2015), 1–16.

Bai, C.-E.; W. Chi; T. X. Liu; C. Tang; and J. Xu. “Boosting pension enrollment and household

consumption by example: A field experiment on information provision.” Journal of

Development Economics, 150 (2021), 102622.

Baker, S. R. “Debt and the response to household income shocks: Validation and application of

linked financial account data.” Journal of Political Economy, 126 (2018), 1504–1557.

Baker, S. R., and L. Kueng. “Household financial transaction data.” Annual Review of Economics,

14 (2022), 47–67.

Battistin, E.; A. Brugiavini; E. Rettore; and G. Weber. “The retirement consumption puzzle:

evidence from a regression discontinuity approach.” American Economic Review, 99 (2009),

2209–26.

Baumeister, R. F. “Yielding to temptation: Self-control failure, impulsive purchasing, and

consumer behavior.” Journal of consumer Research, 28 (2002), 670–676.

29

---

<!-- PAGE 30 -->

Becker, G. “Does FinTech affect household saving behavior.” Findings from a natural field

experiment, 2009 (2017), 1–47.

Benartzi, S.; A. Previtero; and R. H. Thaler. “Annuitization puzzles.” Journal of Economic

Perspectives, 25 (2011), 143–64.

Beshears, J.; J. J. Choi; C. Clayton; C. Harris; D. Laibson; and B. C. Madrian. “Optimal

illiquidity.” National Bureau of Economic Research (2020a).

Beshears, J.; J. J. Choi; J. M. Iwry; D. C. John; D. Laibson; and B. C. Madrian. “Building

Emergency Savings Through Employer-Sponsored Rainy-Day Savings Accounts.” Tax Policy

and the Economy, 34 (2020b), 43–90.

Beshears, J.; J. J. Choi; D. Laibson; B. C. Madrian; and G. S. Goda. 4. The Availability and

Utilization of 401 (k) Loans. University of Chicago Press (2012).

Beshears, J.; J. J. Choi; D. Laibson; B. C. Madrian; and S. P. Zeldes. “What makes annuitization

more appealing?” Journal of public economics, 116 (2014), 2–16.

Board of Governors of the Federal Reserve System. “Report on the Economic Well-Being of U.S.

Households in 2020.” Available at: https://www.federalreserve.gov/publications/2021-

economic-well-being-of-us-households-in-2020-executive-summary.htm.

Br¨auer, K.; A. Hackethal; and T. Hanspal. “Consuming dividends.” The Review of Financial

Studies, 35 (2022), 4802–4857.

Brown, J. R. “Rational and behavioral perspectives on the role of annuities in retirement

planning.” National Bureau of Economic Research (2007).

30

---

<!-- PAGE 31 -->

Brown, J. R.; A. Kapteyn; and O. S. Mitchell. “Framing and Claiming: How Information-F

Raming Affects Expected Social Security Claiming Behavior.” Journal of Risk and Insurance,

83 (2016), 139–162.

Brown, J. R.; J. R. Kling; S. Mullainathan; and M. V. Wrobel. “Why don’t people insure late-life

consumption? A framing explanation of the under-annuitization puzzle.” American Economic

Review, 98 (2008), 304–09.

Brown, J. R.; J. R. Kling; S. Mullainathan; and M. V. Wrobel. “Framing lifetime income.” The

Journal of Retirement, 1 (2013), 27–37.

Brown, J. R., and P. R. Orszag. “The Political Economy of Government-Issued Longevity

Bonds.” Journal of Risk and Insurance, 73 (2006), 611–631.

Campbell, J. Y. “Household finance.” The journal of finance, 61 (2006), 1553–1604.

Carlin, B.; A. Olafsson; and M. Pagel. “Fintech adoption across generations: Financial fitness in

the information age.” National Bureau of Economic Research (2017).

Carlin, B.; A. Olafsson; and M. Pagel. “Mobile apps and financial decision making.” Review of

Finance, 27 (2023), 977–996.

Carvalho, L.; A. Olafsson; and D. Silverman. “Misfortune and mistake: The financial conditions

and decision-making ability of high-cost loan borrowers.”

Chen, X., and S. C. Ludvigson. “Land of addicts? an empirical investigation of habit-based asset

pricing models.” Journal of Applied Econometrics, 24 (2009), 1057–1093.

31

---

<!-- PAGE 32 -->

Chetty, R.; J. N. Friedman; S. Leth-Petersen; T. H. Nielsen; and T. Olsen. “Active vs. passive

decisions and crowd-out in retirement savings accounts: Evidence from Denmark.” The

Quarterly Journal of Economics, 129 (2014), 1141–1219.

Choi, J. J.; D. Laibson; and B. C. Madrian. “$100 bills on the sidewalk: Suboptimal investment in

401(k) plans.” Review of Economics and Statistics, 93 (2011), 748–763.

Choi, J. J.; D. Laibson; B. C. Madrian; and A. Metrick. “Defined contribution pensions: Plan

rules, participant choices, and the path of least resistance.” Tax policy and the economy, 16

(2002), 67–113.

Choi, J. J.; D. Laibson; B. C. Madrian; and A. Metrick. In Perspectives on the Economics of

Aging. “For better or for worse: Default effects and 401 (k) savings behavior.” University of

Chicago Press (2004), 81–126.

Choi, J. J.; D. Laibson; B. C. Madrian; A. Metrick; et al. “Saving for retirement on the path of

least resistance.” Rodney White Center for Financial Research Working Papers, 9.

Chronopoulos, D. K.; M. Lukas; and J. O. Wilson. “Consumer spending responses to the

COVID-19 pandemic: An assessment of Great Britain.” Available at SSRN 3586723.

D’Acunto, F.; A. G. Rossi; and M. Weber. “Crowdsourcing peer information to change spending

behavior.” Chicago Booth Research Paper.

De Martino, B.; D. Kumaran; B. Seymour; and R. J. Dolan. “Frames, biases, and rational

decision-making in the human brain.” Science, 313 (2006), 684–687.

Duflo, E.; W. Gale; J. Liebman; P. Orszag; and E. Saez. “Saving incentives for low-and

32

---

<!-- PAGE 33 -->

middle-income families: Evidence from a field experiment with H&R Block.” The Quarterly

Journal of Economics, 121 (2006), 1311–1346.

Federal Reserve Board. “Consumers and Mobile Financial Services.” Available at:

www.federalreserve.gov/econresdata/consumers-and-mobile-financial-services-report-

201603.pdf.

Fernandes, D.; J. G. Lynch Jr; and R. G. Netemeyer. “Financial literacy, financial education, and

downstream financial behaviors.” Management Science, 60 (2014), 1861–1883.

Ferson, W. E., and G. M. Constantinides. “Habit persistence and durability in aggregate

consumption: Empirical tests.” Journal of Financial Economics, 29 (1991), 199–240.

Fudenberg, D., and D. K. Levine. “Timing and self-control.” Econometrica, 80 (2012), 1–42.

Ganong, P., and P. Noel. “Consumer spending during unemployment: Positive and normative

implications.” American economic review, 109 (2019), 2383–2424.

Gathergood, J., and A. Olafsson. “The Coholding Puzzle: New Evidence from Transaction-Level

Data.” The Review of Financial Studies, hhae016.

Gelman, M.; S. Kariv; M. D. Shapiro; D. Silverman; and S. Tadelis. “Harnessing naturally

occurring data to measure the response of spending to income.” Science, 345 (2014), 212–215.

Goda, G. S.; C. F. Manchester; and A. J. Sojourner. “What will my account really be worth?

Experimental evidence on how retirement income projections affect saving.” Journal of Public

Economics, 119 (2014), 80–92.

33

---

<!-- PAGE 34 -->

Goedde-Menke, M.; M. Lehmensiek-Starke; and S. Nolte. “An empirical test of competing

hypotheses for the annuity puzzle.” Journal of Economic Psychology, 43 (2014), 75–91.

Goldstein, D. G.; H. E. Hershfield; and S. Benartzi. “The illusion of wealth and its reversal.”

Journal of Marketing Research, 53 (2016), 804–813.

Gollwitzer, P. M., and P. Sheeran. “Implementation intentions and goal achievement: A

meta-analysis of effects and processes.” Advances in experimental social psychology, 38

(2006), 69–119.

Hacıo˘glu-Hoke, S.; D. R. K¨anzig; and P. Surico. “The distributional impact of the pandemic.”

European Economic Review, 134 (2021), 103680.

Havranek, T.; M. Rusnak; and A. Sokolova. “Habit formation in consumption: A meta-analysis.”

European Economic Review, 95 (2017), 142–167.

Hershfield, H. E.; D. G. Goldstein; W. F. Sharpe; J. Fox; L. Yeykelis; L. L. Carstensen; and J. N.

Bailenson. “Increasing saving behavior through age-progressed renderings of the future self.”

Journal of Marketing Research, 48 (2011), S23–S37.

Hoch, S. J., and G. F. Loewenstein. “Time-inconsistent preferences and consumer self-control.”

Journal of consumer research, 17 (1991), 492–507.

Johnson, E. J.; J. Hershey; J. Meszaros; and H. Kunreuther. “Framing, probability distortions, and

insurance decisions.” Journal of risk and uncertainty, 7 (1993), 35–51.

Kahneman, D. “Reference points, anchors, norms, and mixed feelings.” Organizational behavior

and human decision processes, 51 (1992), 296–312.

34

---

<!-- PAGE 35 -->

Karlan, D.; M. McConnell; S. Mullainathan; and J. Zinman. “Getting to the top of mind: How

reminders increase saving.” Management Science, 62 (2016), 3393–3411.

K¨uhberger, A. “The influence of framing on risky decisions: A meta-analysis.” Organizational

behavior and human decision processes, 75 (1998), 23–55.

Levi, Y., and S. Benartzi. “Mind the app: Mobile access to financial information and consumer

behavior.” Available at SSRN 3557689.

Madrian, B. C., and D. F. Shea. “The power of suggestion: Inertia in 401 (k) participation and

savings behavior.” The Quarterly journal of economics, 116 (2001), 1149–1187.

Maheswaran, D., and J. Meyers-Levy. “The influence of message framing and issue

involvement.” Journal of Marketing research, 27 (1990), 361–367.

Medina, P. C. “Side effects of nudging: Evidence from a randomized intervention in the credit

card market.” The Review of Financial Studies, 34 (2021), 2580–2607.

Olafsson, A., and M. Pagel. “The liquid hand-to-mouth: Evidence from personal finance

management software.” The Review of Financial Studies, 31 (2018), 4398–4446.

Payne, J. W.; N. Sagara; S. B. Shu; K. C. Appelt; and E. J. Johnson. “Life expectancy as a

constructed belief: Evidence of a live-to or die-by framing effect.” Journal of Risk and

Uncertainty, 46 (2013), 27–50.

Peters, G.-J. Y.; R. A. Ruiter; and G. Kok. “Threatening communication: a critical re-analysis and

a revised meta-analytic test of fear appeal theory.” Health psychology review, 7 (2013), S8–S31.

35

---

<!-- PAGE 36 -->

Pronin, E.; C. Y. Olivola; and K. A. Kennedy. “Doing unto future selves as you would do unto

others: Psychological distance and decision making.” Personality and social psychology

bulletin, 34 (2008), 224–236.

Pronin, E., and L. Ross. “Temporal differences in trait self-ascription: when the self is seen as an

other.” Journal of personality and social psychology, 90 (2006), 197.

Raghubir, P., and J. Srivastava. “Monopoly money: The effect of payment coupling and form on

spending behavior.” Journal of experimental psychology: Applied, 14 (2008), 213.

Ravina, E. “Habit persistence and keeping up with the Joneses: evidence from micro data.”

SECUREwhite Act. “Setting Every Community Up for Retirement Enhancement Act.” Available

at: https://www.congress.gov/bill/116th-congress/house-bill/1994/text.

Seibold, A. “Reference points for retirement behavior: Evidence from german pension

discontinuities.” American Economic Review, 111 (2021), 1126–65.

Shafir, E.; P. Diamond; and A. Tversky. “Money illusion.” The Quarterly Journal of Economics,

112 (1997), 341–374.

Strotz, R. H. “Myopia and inconsistency in dynamic utility maximization.” The review of

economic studies, 23 (1955), 165–180.

Sussman, A. B., and A. L. Alter. “The exception is the rule: Underestimating and overspending

on exceptional expenses.” Journal of Consumer Research, 39 (2012), 800–814.

Tannenbaum, M. B.; J. Hepler; R. S. Zimmerman; L. Saul; S. Jacobs; K. Wilson; and

36

---

<!-- PAGE 37 -->

D. Albarrac´ın. “Appealing to fear: A meta-analysis of fear appeal effectiveness and theories.”

Psychological bulletin, 141 (2015), 1178.

Thaler, R. H., and S. Benartzi. “Save more tomorrow™: Using behavioral economics to increase

employee saving.” Journal of political Economy, 112 (2004), S164–S187.

Thaler, R. H., and H. M. Shefrin. “An economic theory of self-control.” Journal of political

Economy, 89 (1981), 392–406.

van Rooij, M.; O. Coibion; D. Georgarakos; B. Candia; and Y. Gorodnichenko. “Keeping up with

the Jansens: Causal peer effects on household spending, beliefs and happiness.” National

Bureau of Economic Research (2024).

Wakslak, C. J.; S. Nussbaum; N. Liberman; and Y. Trope. “Representations of the self in the near

and distant future.” Journal of personality and social psychology, 95 (2008), 757.

Willis, L. E. “The financial education fallacy.” American Economic Review, 101 (2011), 429–34.

Witte, K. In Handbook of communication and emotion. “Fear as motivator, fear as inhibitor:

Using the extended parallel process model to explain fear appeal successes and failures.”

Elsevier (1996), 423–450.

Yogo, M. “Asset prices under habit formation and reference-dependent preferences.” Journal of

Business & Economic Statistics, 26 (2008), 131–143.

37

---

<!-- PAGE 38 -->

FIGURE 1

Top of Dashboard Page for the FSI-Plot Treatment

38

---

<!-- PAGE 39 -->

FIGURE 2

Net Worth and Index Levels Over the Consumer’s Life Cycle

The figure illustrates the index and net worth level of a life cycle of a consumer with a constant

income level during their working years and no income after retirement. Given no uncertainty, the

consumer can smooth their consumption perfectly. Net worth as a lump sum is the accumulated

wealth from income savings. Net worth as an index is the constant consumption level that the

person can afford until the end of their life given their level of accumulated wealth and time till

the end of life. For simplicity, the real return on savings is set to zero. The plot of Net Worth as a

lump sum is scaled down by a factor of 6.

39

---

<!-- PAGE 40 -->

FIGURE 3

Monthly Logins by Treatment Group

Panel (a) shows the estimated coefficients in a regression of monthly login count on event month

indicator variables with consumer fixed effects for each treatment group. Panel (b) shows the

average predicted values for that regression. Detailed regression results are in Table A1.

(a) Coefficients

(b) Predicted Values

40

---

<!-- PAGE 41 -->

FIGURE 4

Monthly Discretionary Spending by Treatment Group

The figure shows the estimated coefficients in a regression of log monthly discretionary spending

on event month indicator variables with consumer fixed effects for each treatment group. Detailed

regression results are in Table A2.

41

---

<!-- PAGE 42 -->

TABLE 1

Treatment Groups

#

group name

index name

index and
spending plot

comments

1 Control
-
Financial Sustainability Index
2 FSI-Plot
3 FSI-Plot-inf Financial Sustainability Index
Financial Sustainability Index
4 FSI-NoPlot
Life Annuity Index
5 LAI-Plot

-
yes
yes
no
yes

index inflated by 20%

42

---

<!-- PAGE 43 -->

TABLE 2

Discretionary Spending Categories

Spending Categories

Vendor Examples

Automotive Expenses
Cable/Satellite Services
Charitable Giving
Child/Dependent Expenses
Clothing/Shoes
Dues and Subscriptions
Electronics
Entertainment
Gifts
Hobbies
Home Improvement
Home Maintenance
Online Services
Personal Care
Pets/Pet Care
Restaurants/Dining
Travel

Autozone, Honda, Pep Boys
Comcast, DirecTV, Time Warner Cable
Compassion International, Feed The Children, Greenpeace
Children’s Place, Gymboree, Toys “R” Us
Kohl’s Corporation, Macy’s, Nordstrom
Consumer Reports, The New York Times, The Wall Street Journal
Apple Inc., Best Buy Co., Fry’s Electronics
Redbox, Regal Cinemas, StubHub
Godiva Chocolatier Inc, Hallmark, ProFlowers
Camping World, Inc., Guitar Center, Hobby Lobby
Bed Bath & Beyond, Home Depot, Williams And Sonoma
Merry Maids, Stanley Steemer Intl. Inc., Terminix Intl. Company
Google Play, Skype, TransUnion
Bath & Body Works, Great Clips, Ulta Salon, Cosmetics & Fragrance
Petco’s, PetSmart, Wag.com
McDonald’s Corporation, Starbucks, Subway
Delta Air Lines, Hilton Hotels, Southwest Airlines

43

---

<!-- PAGE 44 -->

TABLE 3

Summary Statistics

Age, Net Worth, and Personalized Index were documented on the experiment launch day.

Personalized Index was calculated for all users, including the control group, as the average

monthly cash flow quote on an immediate life annuity. The remaining variables describe monthly

averages over the five months preceding the experiment launch.

Variable

N

Mean

Std. Dev.

10% Median

Age
3,138
Net Worth
3,138
Personalized Index
3,138
Logins
3,138
Income
3,138
Spending
3,138
Discretionary Spending 3,138
Clothing
3,138
Entertainment
3,138
Restaurants
3,138
Travel
3,138
Cash Withdrawal
3,138

44.6
1,128,106
3,178
15.4
16,784
12,364
3,689
374
168
504
693
925

90%

56.0

7.9

36.0
1,493,896 72,558

43.0

637,308 2,623,589

5,211
20.5
13,162
9,887
3,449
495
217
480
1,034
1,326

168
1.2
4,564
3,341
553
12
1
40
0
0

1,561
7.6
12,570
9,200
2,789
205
97
386
304
355

7,462
41.0
35,137
25,913
7,930
929
421
1,076
1,891
2,638

44

---

<!-- PAGE 45 -->

TABLE 4

Treatment Effects on Login Behavior

The dependent variable in all columns is the count of monthly logins. Control, FSI-Plot,

FSI-Plot-inf, FSI-NoPlot, and LAI-Plot are treatment group indicator variables (see Table 1 for

details). The baseline period in all regressions is the five months before the experiment launch

(t=-5 to t=-1). Intra is an indicator variable for the eight months during which experiment

materials were presented in the app (t=0 to t=7), and Post is an indicator for the following twelve

months (t=8 to t=19). Reported t-statistics in parentheses are heteroskedasticity-robust and

clustered at the consumer level. The symbols ***, **, and * indicate statistical significance at the

1%, 5%, and 10% levels, respectively.

Variables

(1)

(2)

(3)

Control * Intra

FSI-Plot * Intra

1.417**
(2.03)
FSI-Plot-inf * Intra 1.288**
(2.11)
1.293**
(2.05)
1.229**
(2.05)

FSI-NoPlot * Intra

LAI-Plot * Intra

Control * Post

FSI-Plot * Post

FSI-Plot-inf * Post

FSI-NoPlot * Post

LAI-Plot * Post

reference group
consumer FE
event month FE
N
adj. R2

0.691
(0.75)
0.700
(0.80)
0.522
(0.57)
0.556
(0.61)
Control
Y
Y
54,750
0.74

45

-1.417**
(-2.03)

-1.288**
(-2.11)
0.129
(0.17)

-0.129
(-0.17)
-0.123
(-0.16)
-0.187
(-0.25)
-0.691
(-0.75)

0.005
(0.01)
-0.058
(-0.09)
-0.700
(-0.80)
-0.009
(-0.01)

0.009
(0.01)
-0.169
(-0.16)
-0.135
(-0.13)
FSI-Plot FSI-Plot-inf

-0.177
(-0.17)
-0.144
(-0.14)

Y
Y
54,750
0.74

Y
Y
54,750
0.74

---

<!-- PAGE 46 -->

TABLE 5

Treatment Effects on Discretionary Spending

The dependent variable in all columns is the log of monthly discretionary spending. Control,

FSI-Plot, FSI-Plot-inf, FSI-NoPlot, and LAI-Plot are treatment group indicator variables (see

Table 1 for details). The baseline period in all regressions is the five months before the experiment

launch (t=-5 to t=-1). Intra is an indicator variable for the eight months during which experiment

materials were presented in the app (t=0 to t=7), and Post is an indicator for the following twelve

months (t=8 to t=19). Reported t-statistics in parentheses are heteroskedasticity-robust and

clustered at the consumer level. The symbols ***, **, and * indicate statistical significance at the

1%, 5%, and 10% levels, respectively.

Variables

(1)

(2)

(3)

Control * Intra

FSI-Plot * Intra

-0.156**
(-2.22)
FSI-Plot-inf * Intra -0.147**
(-2.25)
-0.012
(-0.18)
0.009
(0.13)

FSI-NoPlot * Intra

LAI-Plot * Intra

Control * Post

FSI-Plot * Post

FSI-Plot-inf * Post

FSI-NoPlot * Post

LAI-Plot * Post

reference group
consumer FE
event month FE
N
adj. R2

-0.092
(-0.98)
-0.073
(-0.77)
-0.022
(-0.25)
-0.035
(-0.37)
Control
Y
Y
54,750
0.64

46

0.156**
(2.22)

0.009
(0.13)
0.144**
(2.00)
0.165**
(2.24)
0.092
(0.98)

0.147**
(2.25)
-0.009
(-0.13)

0.135**
(2.01)
0.156**
(2.26)
0.073
(0.77)
-0.019
(-0.19)

0.019
(0.19)
0.070
(0.73)
0.057
(0.57)
FSI-Plot FSI-Plot-inf

0.050
(0.52)
0.038
(0.37)

Y
Y
54,750
0.64

Y
Y
54,750
0.64

---

<!-- PAGE 47 -->

Treatment Effects on Discretionary Spending Over Four Months Intervals

TABLE 6

The dependent variable in all columns is the log of monthly discretionary spending. FSI-Plot,

FSI-Plot-inf, FSI-NoPlot, and LAI-Plot are treatment group indicator variables (see Table 1 for details).

The baseline period in all regressions is the five months before the experiment launch (t=-5 to t=-1) and

the reference group is the Control group. Treatment group indicators are interacted with a time period

indicator for the four months listed at the top of each column. Experiment materials were presented on

the app from t = 0 to t = 7. Reported t-statistics in parentheses are heteroskedasticity-robust and

clustered at the consumer level. The symbols ***, **, and * indicate statistical significance at the 1%,

5%, and 10% levels, respectively.

Variables

(1)

(2)

(3)

(4)

(5)

Interaction:
FSI-Plot * I(a ≤ t ≤ b)

FSI-Plot-inf * I(a ≤ t ≤ b)

FSI-NoPlot * I(a ≤ t ≤ b)

LAI-Plot * I(a ≤ t ≤ b)

consumer FE
event month FE
N
adj. R2

I(0 ≤ t ≤ 3)
-0.140**
(-2.02)
-0.128**
(-2.03)
-0.004
(-0.06)
0.007
(0.10)
Y
Y
19,710
0.72

I(4 ≤ t ≤ 7)
-0.172**
(-1.97)
-0.166**
(-2.00)
-0.020
(-0.23)
0.011
(0.13)
Y
Y
19,710
0.69

I(8 ≤ t ≤ 11)
-0.153*
(-1.69)
-0.157*
(-1.70)
-0.049
(-0.55)
-0.057
(-0.63)
Y
Y
19,710
0.67

I(12 ≤ t ≤ 15)
-0.141
(-1.31)
-0.136
(-1.28)
-0.028
(-0.28)
-0.012
(-0.12)
Y
Y
19,710
0.63

I(16 ≤ t ≤ 19)
0.018
(0.16)
0.074
(0.63)
0.010
(0.09)
-0.036
(-0.30)
Y
Y
19,710
0.59

47

---

<!-- PAGE 48 -->

TABLE 7

Treatment Effects on Spending Categories

The dependent variables in columns (1)-(4) are the log of monthly spending in the corresponding

category, and the log of monthly cash withdrawal is in column (5). The dependent variable in

column (6) is the log sum of the five largest spending transactions for a given consumer-month.

FSI-Plot, FSI-Plot-inf, FSI-NoPlot, and LAI-Plot are treatment group indicator variables (see Table

1 for details). The baseline period in all regressions is the five months before the experiment launch

(t=-5 to t=-1) and the reference group is the Control group. Intra is an indicator variable for the

eight months during which experiment materials were presented in the app (t=0 to t=7), and Post is

an indicator for the following twelve months (t=8 to t=19). Reported t-statistics in parentheses are

heteroskedasticity-robust and clustered at the consumer level. The symbols ***, **, and * indicate

statistical significance at the 1%, 5%, and 10% levels, respectively.

Variables

(1)

(2)

(3)

(4)

(5)

Cash

(6)

5 Largest

Dependent:

Restaurants Clothing Entertainment

Travel Withdrawal Transactions

FSI-Plot * Intra

FSI-Plot-inf * Intra

FSI-NoPlot * Intra

LAI-Plot * Intra

FSI-Plot * Post

FSI-Plot-inf * Post

FSI-NoPlot * Post

LAI-Plot * Post

consumer FE
event month FE
N
adj. R2

-0.140**
(-1.96)
-0.137**
(-1.99)
0.052
(0.75)
0.020
(0.29)
0.004
(0.05)
0.008
(0.09)
-0.021
(-0.23)
-0.037
(-0.40)
Y
Y
54,750
0.70

-0.219**
(-2.37)
-0.184**
(-2.07)
0.010
(0.10)
-0.004
(-0.05)
0.089
(0.81)
0.030
(0.29)
-0.010
(-0.09)
-0.041
(-0.39)
Y
Y
54,750
0.48

-0.155**
(-2.23)
-0.132**
(-2.03)
0.014
(0.21)
0.002
(0.03)
-0.018
(-0.20)
0.023
(0.28)
0.016
(0.18)
-0.048
(-0.56)
Y
Y
54,750
0.56

48

-0.222**
(-2.12)
-0.257**
(-2.45)
0.015
(0.14)
0.082
(0.74)
0.035
(0.27)
-0.017
(-0.13)
0.027
(0.21)
0.011
(0.08)
Y
Y
54,750
0.48

-0.265**
(-2.23)
-0.237**
(-2.19)
-0.009
(-0.07)
0.007
(0.06)
0.006
(0.04)
0.021
(0.15)
-0.030
(-0.21)
0.025
(0.17)
Y
Y
54,750
0.49

-0.127***
(-2.94)
-0.141***
(-3.92)
-0.037
(-0.98)
-0.038
(-1.03)
-0.042
(-0.88)
0.000
(0.00)
-0.011
(-0.25)
0.033
(0.71)
Y
Y
54,750
0.49

---

<!-- PAGE 49 -->

TABLE 8

Treatment Effects on Additional Spending Categories

The dependent variables are the log of monthly total spending in column (1) and log monthly

spending in the corresponding category in columns (2)-(5). FSI-Plot, FSI-Plot-inf, FSI-NoPlot,

and LAI-Plot are treatment group indicator variables (see Table 1 for details). The baseline period

in all regressions is the five months before the experiment launch (t=-5 to t=-1) and the reference

group is the Control group. Intra is an indicator variable for the eight months during which

experiment materials were presented in the app (t=0 to t=7), and Post is an indicator for the

following twelve months (t=8 to t=19). Reported t-statistics in parentheses are

heteroskedasticity-robust and clustered at the consumer level. The symbols ***, **, and *

indicate statistical significance at the 1%, 5%, and 10% levels, respectively.

Variables

Dependent:

FSI-Plot * Intra

FSI-Plot-inf * Intra

FSI-NoPlot * Intra

LAI-Plot * Intra

FSI-Plot * Post

FSI-Plot-inf * Post

FSI-NoPlot * Post

LAI-Plot * Post

consumer FE
event month FE
N
adj. R2

(1)

Spending

-0.065*
(-1.95)
-0.053*
(-1.74)
0.007
(0.22)
0.006
(0.19)
-0.003
(-0.06)
-0.012
(-0.30)
0.021
(0.52)
0.017
(0.40)
Y
Y
54,750
0.60

(2)

Gas

0.026
(0.39)
0.090
(1.24)
0.008
(0.14)
0.093
(1.43)
-0.024
(-0.31)
0.010
(0.11)
0.023
(0.34)
-0.098
(-1.25)
Y
Y
35,450
0.37

49

(3)

(4)

(5)

Groceries Telephone Utilities

0.010
(0.15)
0.069
(1.00)
0.024
(0.35)
0.025
(0.37)
-0.041
(-0.42)
0.063
(0.65)
-0.005
(-0.06)
0.013
(0.14)
Y
Y
43,625
0.42

-0.046
(-0.65)
-0.001
(-0.01)
0.007
(0.09)
-0.030
(-0.41)
-0.012
(-0.14)
0.051
(0.58)
0.071
(0.82)
-0.082
(-0.95)
Y
Y
34,650
0.28

-0.086
(-0.95)
-0.080
(-0.91)
-0.107
(-1.22)
-0.021
(-0.22)
-0.126
(-1.06)
-0.073
(-0.66)
-0.162
(-1.46)
-0.167
(-1.44)
Y
Y
33,550
0.24

---

<!-- PAGE 50 -->

Internet Appendix

A. Detailed Analysis

50

---

<!-- PAGE 51 -->

TABLE A1

Monthly Logins by Treatment Group (7 Groups)

The dependent variable in all columns is the count of monthly logins. I(t = x) are event month

indicator variables. Event month t = −5 is the baseline level in all columns. Each column

presents the regression results for a given treatment group. The treatment groups in columns (6)

and (7) are described in Appendix B. Reported t-statistics in parentheses are

heteroskedasticity-robust and clustered at the consumer level. The symbols ***, **, and *

indicate statistical significance at the 1%, 5%, and 10% levels, respectively.

Variables

(1)

(2)

(3)

(4)

(5)

(6)

(7)

Treatment:

Control

FSI-Plot

FSI-Plot-inf

FSI-NoPlot

LAI-Plot

FSI-NoPlot-retire

LAI-NoPlot-retire

I(t=-4)

I(t=-3)

I(t=-2)

I(t=-1)

I(t=0)

I(t=1)

I(t=2)

I(t=3)

I(t=4)

I(t=5)

I(t=6)

I(t=7)

I(t=8)

I(t=9)

I(t=10)

I(t=11)

I(t=12)

I(t=13)

I(t=14)

I(t=15)

I(t=16)

I(t=17)

I(t=18)

I(t=19)

consumer FE
N
adj. R2

-1.893***
(-3.65)
1.371**
(2.05)
-1.633**
(-2.40)
-1.144*
(-1.71)
-2.679***
(-3.95)
-3.869***
(-5.94)
-1.845***
(-2.83)
-2.039***
(-2.99)
-3.906***
(-5.68)
-3.443***
(-5.08)
-4.493***
(-6.15)
-1.517**
(-2.05)
-3.199***
(-4.42)
-3.009***
(-4.03)
-1.144
(-1.50)
-2.201***
(-2.85)
-0.299
(-0.37)
-1.459*
(-1.82)
-0.592
(-0.75)
-0.428
(-0.57)
-1.797**
(-2.27)
-1.797**
(-2.11)
-3.469***
(-4.19)
-2.199***
(-2.68)
Y
11,450
0.77

-2.867***
(-4.11)
-0.047
(-0.06)
-3.365***
(-3.92)
-2.391***
(-2.72)
-1.161
(-1.28)
-2.258**
(-2.21)
-1.789*
(-1.80)
-2.085**
(-2.04)
-4.773***
(-4.65)
-3.557***
(-3.36)
-3.974***
(-3.51)
-1.457
(-1.28)
-3.180***
(-2.84)
-2.908***
(-2.74)
-0.872
(-0.80)
-1.813*
(-1.67)
-0.704
(-0.63)
-0.995
(-0.89)
-1.583
(-1.45)
-1.607
(-1.44)
-3.443***
(-3.04)
-2.758**
(-2.34)
-3.652***
(-3.23)
-2.675**
(-2.48)
Y
10,550
0.75

-1.998***
(-2.80)
-0.473
(-0.59)
-3.664***
(-4.07)
-2.231**
(-2.31)
-1.807**
(-1.97)
-3.271***
(-3.51)
-1.344
(-1.44)
-1.436
(-1.47)
-3.938***
(-4.03)
-3.133***
(-3.14)
-3.900***
(-3.52)
-2.769**
(-2.55)
-3.133***
(-2.87)
-2.573**
(-2.44)
0.038
(0.03)
-1.438
(-1.29)
0.009
(0.01)
-1.473
(-1.34)
-1.271
(-1.17)
-1.682
(-1.48)
-2.756**
(-2.39)
-3.829***
(-3.33)
-4.438***
(-4.10)
-2.811**
(-2.47)
Y
11,250
0.73

-2.505***
(-3.67)
1.334
(1.55)
-1.869**
(-2.37)
-0.724
(-0.88)
-0.887
(-1.04)
-2.323***
(-2.71)
-1.500*
(-1.69)
-0.710
(-0.81)
-3.454***
(-4.10)
-1.601*
(-1.86)
-3.523***
(-3.67)
-0.191
(-0.20)
-2.288***
(-2.59)
-1.350
(-1.40)
0.329
(0.32)
-1.793*
(-1.76)
0.214
(0.19)
-1.293
(-1.18)
-0.606
(-0.58)
-0.906
(-0.86)
-2.108**
(-2.01)
-1.903*
(-1.68)
-3.249***
(-3.01)
-1.484
(-1.32)
Y
10,850
0.74

51

-1.958***
(-3.12)
-0.059
(-0.07)
-2.437***
(-2.86)
-1.070
(-1.22)
-0.535
(-0.59)
-2.927***
(-3.20)
-1.934**
(-2.08)
-1.683*
(-1.80)
-3.223***
(-3.55)
-1.988**
(-2.14)
-4.192***
(-4.62)
-1.033
(-1.05)
-2.237**
(-2.15)
-1.446
(-1.38)
-0.230
(-0.22)
-1.448
(-1.44)
-0.444
(-0.42)
-0.587
(-0.52)
-1.026
(-0.93)
-1.995*
(-1.79)
-3.005***
(-2.89)
-2.223**
(-2.02)
-3.399***
(-3.16)
-2.221**
(-2.00)
Y
10,650
0.72

-1.906***
(-3.07)
1.294*
(1.71)
-2.046***
(-2.60)
-1.078
(-1.34)
-0.809
(-0.95)
-1.753**
(-2.21)
-1.226
(-1.52)
-1.136
(-1.36)
-3.646***
(-4.55)
-2.174**
(-2.51)
-3.178***
(-3.87)
-0.350
(-0.38)
-2.166**
(-2.46)
-1.413
(-1.51)
0.589
(0.59)
-0.509
(-0.52)
0.713
(0.70)
-0.379
(-0.38)
-0.312
(-0.34)
-0.656
(-0.72)
-2.080**
(-2.34)
-1.591
(-1.60)
-3.042***
(-3.23)
-1.413
(-1.48)
Y
11,925
0.76

-3.304***
(-5.36)
-0.036
(-0.04)
-3.246***
(-4.21)
-2.261***
(-2.72)
-1.834**
(-2.30)
-3.837***
(-5.08)
-2.537***
(-2.82)
-2.788***
(-3.06)
-2.911***
(-3.18)
-2.028**
(-2.24)
-3.537***
(-3.92)
-2.272**
(-2.38)
-3.628***
(-3.58)
-2.985***
(-3.01)
-1.720*
(-1.76)
-2.637***
(-2.63)
-0.367
(-0.31)
-2.263**
(-2.07)
-1.845*
(-1.77)
-2.546**
(-2.39)
-3.178***
(-3.20)
-1.414
(-1.36)
-2.752***
(-2.63)
-1.643
(-1.56)
Y
11,775
0.74

---

<!-- PAGE 52 -->

TABLE A2

Monthly Discretionary Spending by Treatment Group (7 Groups)

The dependent variable in all columns is the log of monthly discretionary spending. I(t = x) are

event month indicator variables. Event month t = −5 is the baseline level in all columns. Each

column presents the regression results for a given treatment group. The treatment groups in

columns (6) and (7) are described in Appendix B. Reported t-statistics in parentheses are

heteroskedasticity-robust and clustered at the consumer level. The symbols ***, **, and *

indicate statistical significance at the 1%, 5%, and 10% levels, respectively.

Variables

(1)

(2)

(3)

(4)

(5)

(6)

(7)

Treatment:

Control

FSI-Plot

FSI-Plot-inf

FSI-NoPlot

LAI-Plot

FSI-NoPlot-retire

LAI-NoPlot-retire

I(t=-4)

I(t=-3)

I(t=-2)

I(t=-1)

I(t=0)

I(t=1)

I(t=2)

I(t=3)

I(t=4)

I(t=5)

I(t=6)

I(t=7)

I(t=8)

I(t=9)

I(t=10)

I(t=11)

I(t=12)

I(t=13)

I(t=14)

I(t=15)

I(t=16)

I(t=17)

I(t=18)

I(t=19)

consumer FE
N
adj. R2

0.189***
(3.15)
0.226***
(3.26)
-0.128*
(-1.77)
-0.132*
(-1.82)
-0.010
(-0.14)
-0.040
(-0.52)
0.042
(0.56)
-0.054
(-0.68)
0.030
(0.37)
-0.040
(-0.46)
-0.022
(-0.26)
-0.010
(-0.11)
0.083
(0.90)
0.049
(0.51)
-0.026
(-0.29)
-0.114
(-1.32)
0.049
(0.55)
0.060
(0.60)
0.086
(0.90)
-0.047
(-0.49)
0.049
(0.47)
-0.097
(-0.96)
-0.098
(-0.94)
-0.008
(-0.08)
Y
11,450
0.64

0.141***
(2.96)
0.122*
(1.94)
-0.101
(-1.38)
-0.065
(-0.88)
-0.143*
(-1.73)
-0.185**
(-2.06)
-0.151*
(-1.84)
-0.188**
(-2.06)
-0.172**
(-1.98)
-0.183**
(-2.06)
-0.181**
(-2.02)
-0.238***
(-2.63)
-0.137
(-1.47)
-0.148
(-1.46)
-0.235**
(-2.41)
-0.147
(-1.63)
-0.127
(-1.20)
-0.124
(-1.16)
-0.037
(-0.34)
-0.172
(-1.53)
-0.057
(-0.53)
-0.033
(-0.30)
-0.012
(-0.10)
-0.026
(-0.23)
Y
10,550
0.68

0.073
(1.21)
0.143*
(1.83)
-0.089
(-1.10)
-0.037
(-0.47)
-0.119
(-1.32)
-0.226**
(-2.52)
-0.133*
(-1.71)
-0.149*
(-1.74)
-0.162**
(-2.00)
-0.169**
(-1.98)
-0.244***
(-2.66)
-0.181*
(-1.91)
-0.160
(-1.62)
-0.138
(-1.40)
-0.219**
(-2.33)
-0.171*
(-1.66)
-0.087
(-0.87)
-0.199*
(-1.91)
-0.035
(-0.35)
-0.127
(-1.21)
0.013
(0.12)
0.080
(0.78)
0.060
(0.54)
-0.063
(-0.56)
Y
11,250
0.61

0.143**
(2.29)
0.161**
(2.53)
-0.051
(-0.65)
-0.045
(-0.55)
0.130*
(1.70)
-0.007
(-0.08)
-0.065
(-0.70)
-0.092
(-1.04)
0.011
(0.12)
0.024
(0.27)
-0.101
(-1.05)
-0.012
(-0.14)
0.035
(0.39)
-0.007
(-0.07)
-0.067
(-0.70)
-0.124
(-1.28)
0.055
(0.54)
0.048
(0.48)
0.014
(0.13)
-0.040
(-0.37)
0.000
(0.00)
-0.085
(-0.76)
-0.002
(-0.02)
0.018
(0.15)
Y
10,850
0.61

52

0.194***
(3.34)
0.289***
(4.03)
0.051
(0.66)
-0.093
(-1.12)
0.127*
(1.69)
0.068
(0.85)
0.029
(0.36)
-0.030
(-0.35)
0.036
(0.40)
0.071
(0.81)
0.082
(0.93)
0.040
(0.44)
0.129
(1.45)
0.028
(0.29)
-0.133
(-1.30)
-0.035
(-0.39)
0.081
(0.77)
0.083
(0.81)
0.146
(1.48)
0.017
(0.17)
-0.054
(-0.49)
-0.037
(-0.33)
-0.033
(-0.29)
0.055
(0.47)
Y
10,650
0.65

0.089**
(2.57)
0.061
(1.61)
-0.118***
(-2.68)
-0.140***
(-3.19)
-0.058
(-1.28)
-0.138***
(-2.88)
-0.125**
(-2.46)
-0.143***
(-2.72)
-0.074
(-1.52)
-0.065
(-1.34)
-0.118**
(-2.44)
-0.089*
(-1.75)
-0.014
(-0.27)
-0.095*
(-1.80)
-0.175***
(-3.33)
-0.203***
(-3.72)
-0.069
(-1.25)
-0.061
(-1.08)
-0.068
(-1.18)
-0.020
(-0.35)
-0.044
(-0.74)
0.010
(0.15)
-0.192***
(-3.03)
-0.024
(-0.40)
Y
11,925
0.64

0.144**
(2.46)
0.099
(1.53)
-0.132*
(-1.71)
-0.151*
(-1.96)
0.104
(1.29)
0.018
(0.21)
0.018
(0.22)
-0.089
(-1.00)
-0.095
(-1.00)
-0.099
(-1.13)
-0.132
(-1.41)
-0.087
(-0.91)
-0.024
(-0.27)
-0.035
(-0.39)
-0.157*
(-1.76)
-0.127
(-1.48)
0.043
(0.45)
-0.009
(-0.10)
0.007
(0.07)
-0.032
(-0.32)
-0.093
(-0.86)
-0.130
(-1.18)
-0.201*
(-1.77)
-0.136
(-1.18)
Y
11,775
0.67

---

<!-- PAGE 53 -->

B. Additional Treatment Groups

A third variation in information design (in addition to framing and salience of context)

was a current- versus future-self framing. An individual can be viewed as two conflicted agents: a

current self and a future self (Strotz (1955), Thaler and Shefrin (1981)). Previous studies confirm

that individuals tend to make decisions that favor their current selves and often treat their future

selves as they would treat a stranger.18 In this study, we examine the effect of presenting the

intertemporal choice dilemma in either a current-self frame or a future-self frame.

In the current-self framing, users received the annuitized value of their net worth

represented by a cash flow stream that starts immediately (using immediate annuities quote). In

this frame, users are primed to reflect on questions that place the current self in the center, such as

“Can I retire today?” or “How far away am I from sustainably retiring, based on my current net

worth?” In the future-self framing, users received the annuitized values of their net worth as a

cash flow stream starting at retirement (calculated using the deferred annuities quote). Under this

frame, users are primed to reflect on questions that place their future self in the center such as

“Will I have enough money to spend when I retire?” To the extent that people identify with their

current selves more than their future selves, we can expect that users receiving current-self

framing would alter their saving behavior more than users receiving the future-self framing.

Unlike the other variations in treatments, the current-self/future-self variation is not a pure

information design test, as the users are exposed to somewhat different information content.

Nevertheless, it is important to test because most financial planners, retirement account providers,

and the Social Security Administration offer some projection of wealth or income at a future date.

18Examples include Pronin and Ross (2006), Pronin, Olivola, and Kennedy (2008), and Wakslak, Nussbaum,

Liberman, and Trope (2008). Researchers have been exploring tools to mitigate this conflict by creating commitments

to the future self (e.g., Choi, Laibson, Madrian, Metrick et al. (2005), Thaler and Benartzi (2004)) or by improving

the vividness or connectedness with the future self (Hershfield, Goldstein, Sharpe, Fox, Yeykelis, Carstensen, and

Bailenson (2011)).

53

---

<!-- PAGE 54 -->

Yet it is difficult to argue that the exposure to the new information content might drive a

differential response between the treatments, as immediate and deferred annuity quotes are

equally available to the public.19

In addition to the five experiment groups described in the main text, two additional

experiment groups were included to test the current-/future-self framing effect. The groups are

described below and in Table B1.

FSI-NoPlot-retire Group (Figure C6): Users in this treatment group received a

personalized index named FSI, which represents a potential cash flow that will start at retirement

and no context plot. By comparing the behavior of this group to that of the FSI-NoPlot group, we

can identify the effect of the current-self or future-self framing under the consumption frame, but

without the salience of the spending context.

LAI-NoPlot-retire Group (Figure C7): Users in this treatment group received a

personalized index named LAI, which represents a potential cash flow that will start at retirement,

and no context plot. By comparing the consumption behavior of this group with that of the

LAI-Plot group, we can identify the effect of the current-self or future-self framing combined

with the context effect.

As noted in the main text, framing effects are sensitive to the salience of the context in

which they are presented. In this study, it was not possible to design a treatment group with high

salience of context and future-self framing. Presentation of current spending levels with future

potential monthly income in the same plot was likely to confuse users and therefore was not

included in the experiment.

Table B2 presents the effect of all the treatments on login behavior. Both the

FSI-NoPlot-retire and the LAI-NoPlot-retire groups show a similar increase in login activity as

the other treatment groups. This confirms the previous conclusion that the increase in login

activity can be attributed to an interest in the new features of the app. Also, as the increase in

19Numerous websites provide free quotes for both immediate and deferred annuities. Inflation-protected life

annuities used in this study are relatively difficult to obtain for both immediate and deferred annuities.

54

---

<!-- PAGE 55 -->

login activity is similar across all treated groups, we reconfirm that none of the experiment

features were more engaging than the rest (e.g., differed annuity quotes did not draw more

attention than the immediate annuity quotes).

The remaining tables and figures in this appendix present the full set of tests for all seven

treatment groups in the experiment. Neither the FSI-NoPlot-retire nor the LAI-NoPlot-retire

treatments had an impact on user spending behavior relative to the control, FSI-NoPlot, or

LAI-Plot groups. The lack of impact of retirement treatments reconfirms the previous conclusion

that framing effects are sensitive to the presence of a salient context. Current or future framing

had no differential impact on financial behavior in the absence of a salient context. The lack of

response to future-self framing is concerning and merits additional research, as it is a common

method of presenting retirement income used by retirement account providers.

55

---

<!-- PAGE 56 -->

TABLE B1

Treatment Groups (7 Groups)

#

group name

index name

1
control
2 FSI-Plot
3 FSI-Plot-inf
4 FSI-NoPlot
5 LAI-Plot
6 FSI-NoPlot-retire
7 LAI-NoPlot-retire Life Annuity Index

-
Financial Sustainability Index
Financial Sustainability Index
Financial Sustainability Index
Life Annuity Index
Financial Sustainability Index

index and
spending plot

comments

-
yes
yes
no
yes
no
no

index inflated by 20%

cash flow starts at retirement
cash flow starts at retirement

56

---

<!-- PAGE 57 -->

TABLE B2

Treatment Effects on Login Behavior (7 Groups)

The dependent variable in all columns is the count of monthly logins. Control, FSI-Plot,

FSI-Plot-inf, FSI-NoPlot, FSI-NoPlot-retire, LAI-Plot, and LAI-NoPlot-retire are treatment group

indicator variables (see Table B1 for details). The baseline period in all regressions is the five

months before the experiment launch (t=-5 to t=-1). Intra is an indicator variable for the eight

months during which experiment materials were presented in the app (t=0 to t=7), and Post is an

indicator for the following twelve months (t=8 to t=19). Reported t-statistics in parentheses are

heteroskedasticity-robust and clustered at the consumer level. The symbols ***, **, and *

indicate statistical significance at the 1%, 5%, and 10% levels, respectively.

Variables

Control * Intra

(1)

(2)

(3)

FSI-Plot * Intra

FSI-NoPlot * Intra

FSI-Plot-inf * Intra

1.417**
(2.03)
1.288**
(2.11)
1.293**
(2.05)
1.229**
(2.05)
1.277**
(2.13)
LAI-NoPlot-retire * Intra 1.366**
(2.12)

FSI-NoPlot-retire * Intra

LAI-Plot * Intra

Control * Post

FSI-Plot * Post

FSI-Plot-inf * Post

FSI-NoPlot * Post

LAI-Plot * Post

FSI-NoPlot-retire * Post

LAI-NoPlot-retire * Post

reference group
consumer FE
event month FE
N
adj. R2

0.691
(0.75)
0.700
(0.80)
0.522
(0.57)
0.556
(0.61)
0.865
(0.95)
0.661
(0.76)
Control
Y
Y
57
78,450
0.74

-1.417**
(-2.03)

-1.288**
(-2.11)
0.129
(0.17)

-0.129
(-0.17)
-0.123
(-0.16)
-0.187
(-0.25)
-0.139
(-0.18)
-0.051
(-0.06)
-0.691
(-0.75)

0.005
(0.01)
-0.058
(-0.09)
-0.011
(-0.02)
0.078
(0.11)
-0.700
(-0.80)
-0.009
(-0.01)

0.009
(0.01)
-0.169
(-0.16)
-0.135
(-0.13)
0.174
(0.16)
-0.030
(-0.03)
FSI-Plot FSI-Plot-inf

-0.177
(-0.17)
-0.144
(-0.14)
0.165
(0.16)
-0.039
(-0.04)

Y
Y
78,450
0.74

Y
Y
78,450
0.74

---

<!-- PAGE 58 -->

FIGURE B1

Monthly Logins by Treatment Group (7 Groups)

Panel (a) shows the estimated coefficients in a regression of monthly login count on event month

indicator variables with consumer fixed effects for each treatment group. Panel (b) shows the

average predicted values for that regression. Detailed regression results are in Table A1.

(a) Coefficients

(b) Predicted Values

58

---

<!-- PAGE 59 -->

TABLE B3

Treatment Effects on Discretionary Spending (7 Groups)

The dependent variable in all columns is the log of monthly discretionary spending. Control,

FSI-Plot, FSI-Plot-inf, FSI-NoPlot, FSI-NoPlot-retire, LAI-Plot, and LAI-NoPlot-retire are

treatment group indicator variables (see Table B1 for details). The baseline period in all

regressions is the five months before the experiment launch (t=-5 to t=-1). Intra is an indicator

variable for the eight months during which experiment materials were presented in the app (t=0 to

t=7), and Post is an indicator for the following twelve months (t=8 to t=19). Reported t-statistics

in parentheses are heteroskedasticity-robust and clustered at the consumer level. The symbols

***, **, and * indicate statistical significance at the 1%, 5%, and 10% levels, respectively.

Variables

Control * Intra

FSI-Plot * Intra

FSI-Plot-inf * Intra

FSI-NoPlot * Intra

LAI-Plot * Intra

FSI-NoPlot-retire * Intra

LAI-NoPlot-retire * Intra

Control * Post

FSI-Plot * Post

FSI-Plot-inf * Post

FSI-NoPlot * Post

LAI-Plot * Post

FSI-NoPlot-retire * Post

LAI-NoPlot-retire * Post

reference group
consumer FE
event month FE
N
adj. R2

(1)

(2)

(3)

0.156**
(2.22)

0.009
(0.13)
0.144**
(2.00)
0.165**
(2.24)
0.120**
(1.99)
0.162**
(2.11)
0.092
(0.98)

0.147**
(2.25)
-0.009
(-0.13)

0.135**
(2.01)
0.156**
(2.26)
0.111**
(2.04)
0.154**
(2.12)
0.073
(0.77)
-0.019
(-0.19)

0.019
(0.19)
0.070
(0.73)
0.057
(0.57)
0.066
(0.82)
0.057
(0.59)
FSI-Plot FSI-Plot-inf

0.050
(0.52)
0.038
(0.37)
0.047
(0.58)
0.038
(0.39)

Y
Y
78,450
0.65

Y
Y
78,450
0.65

-0.156**
(-2.22)
-0.147**
(-2.25)
-0.012
(-0.18)
0.009
(0.13)
-0.036
(-0.66)
0.006
(0.09)

-0.092
(-0.98)
-0.073
(-0.77)
-0.022
(-0.25)
-0.035
(-0.37)
-0.026
(-0.34)
-0.034
(-0.38)
Control
Y
Y
59
78,450
0.65

---

<!-- PAGE 60 -->

FIGURE B2

Monthly Discretionary Spending by Treatment Group (7 Groups)

The figure shows the estimated coefficients in a regression of log monthly discretionary spending

on event month indicator variables with consumer fixed effects for each treatment group. Detailed

regression results are in Table A2.

60

---

<!-- PAGE 61 -->

Treatment Effects on Discretionary Spending Over Four Months Intervals (7 Groups)

TABLE B4

The dependent variable in all columns is the log of monthly discretionary spending. FSI-Plot,

FSI-Plot-inf, FSI-NoPlot, FSI-NoPlot-retire, LAI-Plot, and LAI-NoPlot-retire are treatment group

indicator variables (see Table B1 for details). The baseline period in all regressions is the five months

before the experiment launch (t=-5 to t=-1) and the reference group is the Control group. Treatment

group indicators are interacted with a time period indicator for the four months listed at the top of each

column. Experiment materials were presented on the app from t = 0 to t = 7. Reported t-statistics in

parentheses are heteroskedasticity-robust and clustered at the consumer level. The symbols ***, **, and

* indicate statistical significance at the 1%, 5%, and 10% levels, respectively.

Variables

Interaction:

FSI-Plot * I(a ≤ t ≤ b)

FSI-Plot-inf * I(a ≤ t ≤ b)

FSI-NoPlot * I(a ≤ t ≤ b)

LAI-Plot * I(a ≤ t ≤ b)

FSI-NoPlot-retire * I(a ≤ t ≤ b)

LAI-NoPlot-retire * I(a ≤ t ≤ b)

consumer FE
event month FE
N
adj. R2

(1)

(2)

(3)

(4)

(5)

I(0 ≤ t ≤ 3)

I(4 ≤ t ≤ 7)

I(8 ≤ t ≤ 11)

I(12 ≤ t ≤ 15)

I(16 ≤ t ≤ 19)

-0.140**
(-2.02)
-0.128**
(-2.03)
-0.004
(-0.06)
0.007
(0.10)
-0.048
(-0.88)
0.067
(0.98)
Y
Y
28,242
0.73

-0.172**
(-1.97)
-0.166**
(-2.00)
-0.020
(-0.23)
0.011
(0.13)
-0.024
(-0.35)
-0.054
(-0.61)
Y
Y
28,242
0.70

61

-0.153*
(-1.69)
-0.157*
(-1.70)
-0.049
(-0.55)
-0.057
(-0.63)
-0.067
(-0.91)
-0.045
(-0.52)
Y
Y
28,242
0.68

-0.141
(-1.31)
-0.136
(-1.28)
-0.028
(-0.28)
-0.012
(-0.12)
-0.039
(-0.47)
0.004
(0.04)
Y
Y
28,242
0.64

0.018
(0.16)
0.074
(0.63)
0.010
(0.09)
-0.036
(-0.30)
0.029
(0.31)
-0.063
(-0.53)
Y
Y
28,242
0.60

---

<!-- PAGE 62 -->

TABLE B5

Treatment Effects on Spending Categories (7 Groups)

The dependent variables in columns (1)-(4) are the log of monthly spending in the corresponding

category, and the log of monthly cash withdrawal is in column (5). The dependent variable in

column (6) is the log sum of the five largest spending transactions for a given consumer-month.

FSI-Plot, FSI-Plot-inf, FSI-NoPlot, FSI-NoPlot-retire, LAI-Plot, and LAI-NoPlot-retire are

treatment group indicator variables (see Table B1 for details). The baseline period in all

regressions is the five months before the experiment launch (t=-5 to t=-1) and the reference group

is the Control group. Intra is an indicator variable for the eight months during which experiment

materials were presented in the app (t=0 to t=7), and Post is an indicator for the following twelve

months (t=8 to t=19). Reported t-statistics in parentheses are heteroskedasticity-robust and

clustered at the consumer level. The symbols ***, **, and * indicate statistical significance at the

1%, 5%, and 10% levels, respectively.

Variables

(1)

(2)

(3)

(4)

(5)

Cash

(6)

5 Largest

Dependent:

Restaurants Clothing Entertainment

Travel Withdrawal Transactions

FSI-Plot * Intra

FSI-Plot-inf * Intra

FSI-NoPlot * Intra

LAI-Plot * Intra

FSI-NoPlot-retire * Intra

LAI-NoPlot-retire * Intra

FSI-Plot * Post

FSI-Plot-inf * Post

FSI-NoPlot * Post

LAI-Plot * Post

FSI-NoPlot-retire * Post

LAI-NoPlot-retire * Post

consumer FE
event month FE
N
adj. R2

-0.140**
(-1.96)
-0.137**
(-1.99)
0.052
(0.75)
0.020
(0.29)
-0.005
(-0.09)
0.023
(0.33)
0.004
(0.05)
0.008
(0.09)
-0.021
(-0.23)
-0.037
(-0.40)
0.021
(0.29)
-0.017
(-0.19)
Y
Y
78,450
0.71

-0.219**
(-2.37)
-0.184**
(-2.07)
0.010
(0.10)
-0.004
(-0.05)
-0.005
(-0.08)
-0.041
(-0.47)
0.089
(0.81)
0.030
(0.29)
-0.010
(-0.09)
-0.041
(-0.39)
0.066
(0.79)
0.011
(0.11)
Y
Y
78,450
0.50

62

-0.155**
(-2.23)
-0.132**
(-2.03)
0.014
(0.21)
0.002
(0.03)
0.006
(0.09)
-0.007
(-0.10)
-0.018
(-0.20)
0.023
(0.28)
0.016
(0.18)
-0.048
(-0.56)
0.002
(0.02)
-0.009
(-0.11)
Y
Y
78,450
0.57

-0.222**
(-2.12)
-0.257**
(-2.45)
0.015
(0.14)
0.082
(0.74)
-0.005
(-0.05)
0.021
(0.20)
0.035
(0.27)
-0.017
(-0.13)
0.027
(0.21)
0.011
(0.08)
0.018
(0.14)
-0.014
(-0.11)
Y
Y
78,450
0.48

-0.265**
(-2.23)
-0.237**
(-2.19)
-0.009
(-0.07)
0.007
(0.06)
-0.023
(-0.20)
-0.025
(-0.27)
0.006
(0.04)
0.021
(0.15)
-0.030
(-0.21)
0.025
(0.17)
0.003
(0.02)
0.013
(0.11)
Y
Y
78,450
0.49

-0.127***
(-2.94)
-0.141***
(-3.92)
-0.037
(-0.98)
-0.038
(-1.03)
-0.002
(-0.08)
-0.000
(-0.01)
-0.042
(-0.88)
0.000
(0.00)
-0.011
(-0.25)
0.033
(0.71)
0.021
(0.52)
0.017
(0.40)
Y
Y
78,450
0.49

---

<!-- PAGE 63 -->

TABLE B6

Treatment Effects on Additional Spending Categories (7 Groups)

The dependent variables are the log of monthly total spending in column (1) and log monthly

spending in the corresponding category in columns (2)-(5). FSI-Plot, FSI-Plot-inf, FSI-NoPlot,

and LAI-Plot are treatment group indicator variables (see Table B1 for details). The baseline

period in all regressions is the five months before the experiment launch (t=-5 to t=-1) and the

reference group is the Control group. Intra is an indicator variable for the eight months during

which experiment materials were presented in the app (t=0 to t=7), and Post is an indicator for the

following twelve months (t=8 to t=19). Reported t-statistics in parentheses are

heteroskedasticity-robust and clustered at the consumer level. The symbols ***, **, and *

indicate statistical significance at the 1%, 5%, and 10% levels, respectively.

Variables

Dependent:

FSI-Plot * Intra

FSI-Plot-inf * Intra

FSI-NoPlot * Intra

LAI-Plot * Intra

FSI-NoPlot-retire * Intra

LAI-NoPlot-retire * Intra

FSI-Plot * Post

FSI-Plot-inf * Post

FSI-NoPlot * Post

LAI-Plot * Post

FSI-NoPlot-retire * Post

LAI-NoPlot-retire * Post

consumer FE
event month FE
N
adj. R2

(1)

Spending

-0.065*
(-1.95)
-0.053*
(-1.74)
0.007
(0.22)
0.006
(0.19)
-0.001
(-0.02)
0.001
(0.04)
-0.003
(-0.06)
-0.012
(-0.30)
0.021
(0.52)
0.017
(0.40)
-0.018
(-0.45)
-0.005
(-0.12)
Y
Y
78,450
0.61

(2)

Gas

0.026
(0.39)
0.090
(1.24)
0.008
(0.14)
0.093
(1.43)
0.033
(0.64)
0.100
(1.53)
-0.024
(-0.31)
0.010
(0.11)
0.023
(0.34)
-0.098
(-1.25)
-0.001
(-0.02)
-0.027
(-0.33)
Y
Y
63
51,375
0.37

(3)

(4)

(5)

Groceries Telephone Utilities

0.010
(0.15)
0.069
(1.00)
0.024
(0.35)
0.025
(0.37)
0.024
(0.37)
0.076
(1.11)
-0.041
(-0.42)
0.063
(0.65)
-0.005
(-0.06)
0.013
(0.14)
0.057
(0.63)
0.044
(0.48)
Y
Y
62,350
0.42

-0.046
(-0.65)
-0.001
(-0.01)
0.007
(0.09)
-0.030
(-0.41)
-0.047
(-0.65)
-0.000
(-0.00)
-0.012
(-0.14)
0.051
(0.58)
0.071
(0.82)
-0.082
(-0.95)
0.024
(0.31)
0.034
(0.39)
Y
Y
49,675
0.27

-0.086
(-0.95)
-0.080
(-0.91)
-0.107
(-1.22)
-0.021
(-0.22)
0.002
(0.03)
0.015
(0.17)
-0.126
(-1.06)
-0.073
(-0.66)
-0.162
(-1.46)
-0.167
(-1.44)
0.042
(0.36)
0.012
(0.10)
Y
Y
48,150
0.24

---

<!-- PAGE 64 -->

TABLE B7

Balance Tests

Variables are defined in Table 3.

Panel A.

Treatment

Age

Net Worth

Personalized Index

Logins

N

458
422
450
434
426
477
471

N

458
422
450
434
426
477
471

Control
FSI-Plot
FSI-Plot-inf
FSI-NoPlot
LAI-Plot
FSI-NoPlot-retire
LAI-NoPlot-retire

Panel B.

Treatment

Control
FSI-Plot
FSI-Plot-inf
FSI-NoPlot
LAI-Plot
FSI-NoPlot-retire
LAI-NoPlot-retire

Panel C.

mean

44.48
44.4
44.23
44.67
44.78
44.48
44.84

sd

7.78
7.93
7.96
7.77
7.9
7.91
8.08

mean

sd

1,146,247
1,184,688
1,086,211
1,114,032
1,126,652
1,097,916
1,144,653

1,583,688
1,645,099
1,357,686
1,391,693
1,600,438
1,302,980
1,563,826

mean

3,274
3,310
2,953
2,990
3,367
3,037
3,328

sd

5,562
4,854
4,791
4,603
6,766
4,713
4,940

mean

15.25
15.29
14.98
14.97
15.69
15.98
15.78

sd

17.52
22.21
21.03
20.20
19.15
21.60
21.27

Income

mean

sd

16,863
16,721
16,446
16,692
17,284
16,972
16,531

12,683
13,405
12,753
13,110
13,525
13,370
13,355

Spending

Discretionary Spending

Clothing

mean

12,323
12,748
12,459
12,047
12,678
12,022
12,323

sd

9,826
10,396
10,062
9,841
10,434
8,656
9,971

mean

3,610
3,694
3,836
3,669
3,621
3,690
3,701

sd

3,290
3,547
3,709
3,549
3,206
3,168
3,654

mean

371
406
384
370
369
362
359

sd

492
577
552
484
467
396
485

Treatment

Entertainment

Restaurants

Travel

Cash Withdrawal

Control
FSI-Plot
FSI-Plot-inf
FSI-NoPlot
LAI-Plot
FSI-NoPlot-retire
LAI-NoPlot-retire

N

458
422
450
434
426
477
471

mean

170
172
177
163
168
163
161

sd

224
238
213
201
225
197
224

mean

508
531
495
499
509
490
499

64

sd

494
547
450
434
460
445
525

mean

667
677
742
686
749
682
656

sd

1,050
1,038
1,123
1,014
1,156
830
1,018

mean

sd

913
946
969
934
942
903
871

1,281
1,458
1,292
1,331
1,320
1,344
1,264

---

<!-- PAGE 65 -->

C. Experiment Material

65

---

<!-- PAGE 66 -->

FIGURE C1

Full Dashboard Page for the Control Group

This dashboard page was presented to all treatment groups before the experiment launch (t < 0)

and after the removal of the experiment material from the app (t > 7).

66

---

<!-- PAGE 67 -->

FIGURE C2

Full Dashboard Page for the FSI-Plot Treatment

67

---

<!-- PAGE 68 -->

FIGURE C3

Top of the Dashboard Page for the FSI-Plot Treatment

68

---

<!-- PAGE 69 -->

FIGURE C4

Top of the Dashboard Page for the FSI-NoPlot Treatment

69

---

<!-- PAGE 70 -->

FIGURE C5

Top of the Dashboard Page for the LAI-Plot Treatment

70

---

<!-- PAGE 71 -->

FIGURE C6

Top of the Dashboard Page for the FSI-NoPlot-retire Treatment

71

---

<!-- PAGE 72 -->

FIGURE C7

Top of the Dashboard Page for the LAI-NoPlot-retire Treatment

72

---

<!-- PAGE 73 -->

FIGURE C8

FAQ page for the FSI-Plot Treatment (part 1)

73

---

<!-- PAGE 74 -->

FIGURE C9

FAQ page for the FSI-Plot Treatment (part 2)

74

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Personal Financial Information Presentation and
Consumer Spending
Yaron Levi*
October 26, 2025
Abstract
Westudywhetherinformationdesigninfluencesconsumerbehaviorinarandomizedfield
experimentwithusersofanonlineaccountaggregationapp.Participantsreceiveda
personalizedindexrepresentingtheirnetworthasalifetimemonthlycashflow.The
presentationofthisindexvariedacrosstreatmentsinitsframingandthesalienceofits
display.Consumersexposedtoaconsumption-orientedframeandasalientcomparisonofthe
indexwiththeirpastspendingreduceddiscretionaryspending.Thesefindingsshowthat
minorvariationsininformationpresentationcansignificantlyaffectfinancialbehavior,
highlightingthepowerofdesigninpromotingsavingandinformingpolicyandregulation.
JELclassification:D12,D14,D15,D91,G41,G51.
Keywords:Framing,Salience,ConsumerSpending,Savings,FieldExperiment.
*YaronLevi,Yaron.Levi-1@ou.edu,UniversityofOklahomaPriceCollegeofBusiness.Iamespeciallygratefultotheeditor,RanDuchin,
forguidanceandsupportthroughoutthereviewprocess.IwouldalsoliketothankIvoWelch,MarkGarmaise,ShlomoBenartzi,RichardThaler,
StephenSpiller,DavidHirshleifer,TomChang,KeithChen,MikhailChernov,CaryFriedman,NoahGoldstein,JinyongHahn,FrancisLongstaff,
HannoLustig,RichardRoll,SuzanneShu,DavidSolomon,andseminarparticipantsatUCLAAnderson,UCLABehavioralDecisionMaking,
Vanderbilt,BostonCollege,Emory,Wharton,UT-Austin,Kellogg,USC,LSE,Columbia,Claremont,IDC,SFSCavalcade,BoulderSummerCon-
ferenceonConsumerFinancialDecisionMaking,CEPREuropeanSummerSymposiuminFinancialMarkets,andAFAfortheircommentsand
discussions.SpecialthankstoPersonalCapitalforallowingmetoconductthisstudy,andtotheHuelerCompaniesforprovidingaccesstotheir
annuityquotingplatform,IncomeSolutions®.Ihavenofinancialinterestinanyofthedataproviders,andIappreciatetheircommitmenttoscience,
allowingmetopublishtheresearchregardlessofthefindings.Thisstudydoesnotuseanypersonallyidentifiableinformation.Thestudywas
exemptfromIRBreviewbytheOfficeoftheHumanResearchProtectionProgramatUSC(StudyID:UP-20-00254).Theexperimentdescribedin
thispaperwasnotpre-registered;itwasconductedin2014,beforepre-registrationbecamecommonpracticeineconomicsandfinance.

I. Introduction
Recentadvancementsintechnologyandthewidespreaduseofonlinefinancialtoolshave
transformedthewayindividualsinteractwiththeirfinances.Today,almostallfinancialservices
areaccessiblethroughdigitalplatforms,leadingtoasignificantshiftinhowpeoplemanagetheir
money.1
Whenindividualsaccesstheironlinefinancialaccounts,theycankeeptrackoftheir
accountbalancesandreviewrecenttransactions,whichallowsthemtoassesstheirfinancial
standingandplantheirfuturespending.Inthispaper,wetestifconsumersareinfluencedbythe
wayinwhichtheirpersonalfinancesarepresented.Changesinthepresentationofinformation
canaffectconsumers’sentiments,beliefs,orinterpretationoftheinformationandpotentiallylead
toachangeinbehavior.
Weconductedafieldexperimentontheusersofanonlineaccountaggregationsoftware.
Accountaggregationappsenableuserstolinkvariousfinancialaccountssuchaschecking,
savings,retirement,investment,mortgage,loans,andmore,throughasingleapplication.This
aggregationprovidesuserswithacomprehensiveandreal-timeoverviewoftheirfinances,
includingdetailssuchasnetworth,totalexpenditures,expenditurebreakdownbycategories,and
income.2
1Forinstance,aconsiderable71%ofconsumersintheU.S.withbankaccountsutilizeonlinebankingservices
(FederalReserveBoard(2016)).
2ExamplesofresearchusingaccountaggregationdataincludestudiesconductedintheUS(Gelman,Kariv,
Shapiro,Silverman,andTadelis(2014),Baker(2018),D’Acunto,Rossi,andWeber(2023),LeviandBenartzi
(2020)),Brazil(Medina(2021)),Germany(Becker(2017),Bra¨uer,Hackethal,andHanspal(2022),UK
(Chronopoulos,Lukas,andWilson(2020),Hacıog˘lu-Hoke,Ka¨nzig,andSurico(2021))andIceland
2

Usersoftheappwereprovidedwithapersonalizedindexthatrepresentstheirnetworthas
amonthlycashflow.Thatis,insteadofpresentingnetworthasalumpsum(e.g.,$650,000),it
waspresentedastheequivalentinflation-protectedlifetimemonthlycashflow,whichdependson
theuser’sageandcurrentmarketpricesoflifeannuities(e.g.,$2,000permonthforlife).The
indexprovidesarelativelyconvenientreferenceforspendingincomparisontothelumpsum
presentation,sinceconsumerstypicallyusemonthlycashflowsasaunitofmeasureforspending
(e.g.,rent,mortgage,utilitiesaretypicallybilledmonthly).WediscusstheindexinSectionII.
Usersoftheappwererandomlyassignedintotreatmentgroupsthatvariedinthe
presentationoftheindex.Thefirstvariationintreatmentswasintheframingoftheindex.A
significantbodyofresearchshowsthatconsumers’perceivedvalueandattractivenessoflife
annuitiesdependsontheframeusedtodescribethem(Agnew,Anderson,Gerlach,andSzykman
(2008),Benartzi,Previtero,andThaler(2011),Beshears,Choi,Laibson,Madrian,andZeldes
(2014),Brown,Kling,Mullainathan,andWrobel(2008,0),Brown,Kapteyn,andMitchell(2016),
Goda,Manchester,andSojourner(2014),Goedde-Menke,Lehmensiek-Starke,andNolte(2014)).
Consumersplaceahighervalueonannuitieswhenthecashflowstreamisdescribedusing
aconsumptionframe(usingwordssuchas“spend”and“payment”)thanwhendescribedusingan
investmentframe(usingwordssuchas“invest”and“earnings”).Theconsumptionframeprompts
individualstoreflectonanegativescenarioinwhichtheyhavetocuttheirspendingduetoalack
ofresources,leadingthemtoplaceahighervalueonlifetimemonthlyincome.Fearappeal
messageshavebeenwidelystudiedandshowntoinfluenceattitude,intentions,andbehaviors
(Carlin,Olafsson,andPagel(2017),Carvalho,Olafsson,andSilverman(2019),GathergoodandOlafsson(2024),
OlafssonandPagel(2018)).Forarecentreviewofresearchutilizingtransaction-leveldata,seeBakerandKueng
(2022).
3

effectively(Peters,Ruiter,andKok(2013),Tannenbaum,Hepler,Zimmerman,Saul,Jacobs,
Wilson,andAlbarrac´ın(2015),Witte(1996)).
Wetestifusingtheconsumptionframetodescribetheindexcanalsodriveconsumersto
adjusttheirspendinglevels.Accordingly,weusetwodifferentlabelsasthenameoftheindex:
FinancialSustainabilityIndex(FSI):Thislabelpromptsuserstothinkoftheindexasa
referencetotheirspendingactivities.Thisnameinducesuserstoreflectonascenarioinwhich
theirfinancialconditionisnolonger“sustainable”andarethereforeforcedtocuttheirspending.
LifeAnnuityIndex(LAI):Thislabelmaintainsaneutraltoneanddoesnotelicitany
specificemotionsfromusers.Itsimplydescribestheindexforwhatitis-alifeannuityquote.
Thesecondvariationinthetreatmentsisthesalienceofthecomparisonbetweentheindex
andtheuser’shistoricalspendinglevels.Someofthetreatmentgroupswerepresentedwithatime
seriesplotthatdirectlycomparestheindexlevelwiththeuser’shistoricalmonthlyspending
(hereafter“contextplot”;seeFigure1).Usersintreatmentsthatdidnotreceivethecontextplot
hadaccesstothesameinformationcontent.Atimeseriesplotoftheindexwaspresentedonthe
dashboardpage,andaseparatetimeseriesplotofhistoricalspendingwasavailableontheapp’s
CashFlowpage.However,withoutanexplicitcontrastbetweentheindexandspending,usersare
lesslikelytoreflectonthedifferencebetweenthetwoandadjusttheirspending.3
Wefindthatuserswhowerepresentedwiththeconsumptionframe(i.e.,FSI)anda
3Theexperimentincludedathirdvariationinthetreatmentsinwhichthepersonalizedindexrepresentedacash
flowstreamthatstartsatretirementratherthanimmediately.Thisvariationdidnothaveanimpactonconsumer
behavioreventhoughitissimilartoreportingstandardsoffundperformancerequiredbytheSECUREAct(2019)
andcommonpracticesinthefinancialindustry.Thisvariationintreatments,therelatedtreatmentgroups,andthe
testsarepresentedinAppendixB.
4

contextplotdecreasedtheirdiscretionaryspendingbyabout15%relativetouserswhoreceived
onlytheconsumptionframewithnoplotoracontextplotbutwithaneutralframe(i.e.,LAI).The
decreaseindiscretionaryspendingstartedimmediatelyafterthelaunchoftheexperimentand
persistedthroughouttheeightmonthsinwhichtheexperimentmaterialswerepresentedonthe
app.Theseconsumersincreasedtheirspendinglevelsonlygraduallyaftertheremovalofthe
experimentcontentandconvergedtothespendinglevelsofconsumersinunaffectedgroupsafter
anadditionaleightmonths.
Thedecreaseinspendingismostpronouncedinrelatively“tempting”spontaneous
categoriessuchasentertainment,restaurants,andclothing.Thisevidenceisconsistentwithan
improvedabilitytoapplyself-controlduetoanincreasedfeelingofguiltandregretiftheywere
tomakethepurchase(e.g.,HochandLoewenstein(1991)).Incontrast,wedonotfindachangein
non-discretionaryspendingsuchasgas,groceries,andutilities,whicharedifficulttoadjust,
especiallyoverashorttimeperiod.
Furthermore,wefindadecreaseininfrequentlarge-tickettransactions.Thisevidenceis
consistentwithKarlan,McConnell,Mullainathan,andZinman(2016)andSussmanandAlter
(2012),showingthatpeopletendtoomitsuch“exceptional”transactionsfromtheirbudgetplan,
andthatsalientreminderspromoteconsumerstostaywithintheirmeans.
Additionally,usersintheaffectedtreatmentsalsodecreasedtheircashwithdrawals,
representinganadditionaldecreaseinspending(i.e.,notincludedinthediscretionaryspending
variable).Thisdeclineincashwithdrawalsisconsistentwiththenotionthatindividualsassigna
highersubjectivevaluetocashtransactionscomparedtonon-cashtransactions,leadingthemto
prioritizecuttingbackoncashtransactionsfirst(RaghubirandSrivastava(2008)).
Existingresearchonconsumerspendinghaspredominantlyreliedoneitheraggregate
5

consumptiondataorlow-frequencyconsumer-leveldata.However,recentstudieshavebegunto
leveragehigh-frequencytransaction-leveldata,providingamoregranularunderstandingof
consumerbehavior.Thisbodyofliteraturedemonstratesthatconsumersexhibitstrongspending
habits,typicallymakinggradualadjustmentsoveranextendedperiodinresponsetochangesin
economicfactorslikeinterestrates,income,orcreditavailability(BakerandKueng(2022),
Havranek,Rusnak,andSokolova(2017),Ravina(2019)).Thispapershowsthateveninthe
presenceofstrongbehavioralinertia,simpleinformationdesignmanipulationscanprompt
consumerstorapidlyadjusttheirspendinglevels.Importantly,theresponseiscausedbyachange
inconsumers’sentimentoraperceivedchangeinfinancialwell-beingandnotbyachangeinany
economicvariable.
Consumersintheaffectedgroupsdecreasedtheirspendingimmediatelyafterreceiving
theexperimentaltreatments.However,theirspendingincreasedonlygraduallyafterthe
experimentcontentwasremoved.Thispatternalignswithfindingsfrompriorstudies
documentinganon-linearadjustmentinspendinghabits(ChenandLudvigson(2009),Fersonand
Constantinides(1991)1,GanongandNoel(2019)).Specifically,theseresultsareconsistentwith
thepredictionsofthemodelproposedbyYogo(2008),whichincorporateshabitformationintoa
reference-dependentutilityfunctionwithlossaversion.Accordingtothemodel,anegativeshock
elicitsalargerresponsethanapositiveeconomicshock.
Framingeffectshavebeenextensivelyexploredinthesocialsciences,demonstratingtheir
influenceacrossvariousdomains.4 However,framinginformationtospecificallyinfluence
4Previousstudies,suchasthosebyAndreoni(1995),DeMartino,Kumaran,Seymour,andDolan(2006),
Johnson,Hershey,Meszaros,andKunreuther(1993),Payne,Sagara,Shu,Appelt,andJohnson(2013),Seibold
(2021),andShafir,Diamond,andTversky(1997),havedocumentedtheimpactofframingondecision-making.
6

consumerspendingposesuniquechallenges.First,itrequiresconsumerstodeviatefromtheir
establishedspendinghabits,whicharetypicallyresistanttochange.Second,thereisatemporal
gapbetweentheexposuretotheexperimentaltreatmentsandactualspendingactivity.Lastly,the
treatmentsemployedinourstudydonotprescribeaspecificcourseofaction,leavingconsumers
todecideifandhowtoadjusttheirspending.Nonetheless,thisstudydemonstratesthatthrough
onlinefinancialapps,whereconsumersarefrequentlyexposedtothetreatments,certain
informationdesignscanindeedinfluenceconsumerspending.
Studiesthatexamineframingeffectsondecision-makinghaveoftenproducedmixed
results.MaheswaranandMeyers-Levy(1990)showedthatissueinvolvement,whichreferstothe
personalrelevanceandsalienceofanissuetoanindividual,isakeydeterminantofframing
effects.Theyfurtherdemonstratedthatnegativelyframedmessagesaremoreinfluentialwhen
theycontainahighlevelofinvolvement.Ku¨hberger(1998)conductedameta-analysisofframing
experimentsandconcludedthatsaliencemanipulationsarecriticaldeterminantsofframing
effects.Consistentwiththisexistingevidence,ourstudydemonstratesthatthefearappeal
messageincorporatedintheconsumptionframehasanimpactonspendingbehavior,butonly
whenaccompaniedbyasalientcontext.Inotherwords,informationmustincludebotharelevant
framingandsalientcontextforconsumerstoactuponit.
Thepapercontributestotheextensivebodyofresearchontoolsaimedatincreasing
consumers’savingrates.Financialeducationprogramshavethusfarproventobecostlyandto
havenegligibleeffectsonsavingbehavior(Campbell(2006),Fernandes,LynchJr,and
Netemeyer(2014),Willis(2011)).Taxsubsidiesforretirementaccountstendtobenefitwealthier
individuals,whoarealreadybetterpreparedforretirement(Chetty,Friedman,Leth-Petersen,
Nielsen,andOlsen(2014)).Employers’matchingcontributionstoretirementaccountshavehad
7

limitedsuccessinincreasingsavingrates(Choi,Laibson,Madrian,andMetrick(2002),Choi,
Laibson,andMadrian(2011),Duflo,Gale,Liebman,Orszag,andSaez(2006)).Behavioraltools
suchaschoicearchitecture,reminders,andinformationdesignhaverepeatedlybeenproventobe
powerfulininfluencingsavingsandretirementaccountcontributions.(Bai,Chi,Liu,Tang,and
Xu(2021),Chettyetal.(2014),Choietal.(2002),Choi,Laibson,Madrian,andMetrick(2004),
Karlanetal.(2016),MadrianandShea(2001),ThalerandBenartzi(2004)).However,these
behavioraltoolsmaynotbeapplicabletoasignificantportionofnonretiredhouseholdsthathave
noaccesstoretirementaccounts.5 Inaddition,theeffectofanincreaseinretirementcontributions
ontheoverallsavingrateismitigatedbyearlywithdrawalfromtheseaccounts(Argento,Bryant,
andSabelhaus(2015),Beshears,Choi,Clayton,Harris,Laibson,andMadrian(2020a),Beshears,
Choi,Iwry,John,Laibson,andMadrian(2020b))andanincreaseinborrowingactivity(Beshears,
Choi,Laibson,Madrian,andGoda(2012)).Thispapershowsthatinformationdesigncan
influencespending,whichistheflipsideofsavings.Giventhewideuseofonlinefinancial
services,informationdesigntoolscanbeeasilyimplementedanddistributedtoalargemassof
consumersatalowcost,includinglower-incomeindividualswhohavenoretirementaccounts.6
526%ofnonretiredhouseholdsintheU.S.havenoretirementsavings(BoardofGovernorsoftheFederal
ReserveSystem(2021)).
6Thereisnoformaldataonthenumberofusersofaccountaggregationappsglobally.However,theseappsare
availableinmostcountries,withanincreasingnumberofthird-partyprovidersandbanksofferingthemasafree
service.TheOpenBankingregulationinEurope,particularlytheRevisedPaymentServicesDirective(PSD2),has
significantlyboostedtheirdevelopmentandusagebyrequiringbankstoprovidestandardizedaccesstocustomer
accountinformation.Similarregulationsarebeingadoptedinmanyothercountries,likelyincreasingthesupplyand
usageofpersonalfinancialmanagementtoolswithaccountaggregationtechnology.
8

II. Personalized Index
Accountaggregationappstypicallypresenttheusers’networthasthefirstitemonthe
firstpageusersvisitafterloggingin.Inthisstudy,alltreatmentgroupsreceivedapersonalized
indexthatpresentedtheirnetworthbutwithachangeintheunitofmeasure.Insteadof
presentingnetworthasalumpsum,itwaspresentedastheequivalentinflation-protectedlifetime
monthlycashflow,whichdependsontheuser’sage,stateofresidence,andcurrentmarketprices.
Thisindexreflectsthemarketquoteofamonthlycashflowfromanimmediate,
inflation-protectedlifeannuity.Lifeannuitiesaresoldbylargefinancialinstitutions(typically
insurancecompanies)andprovideahedgeformarket,longevity,andinflationrisks.Byusingthe
marketpricesandcurrentnetworthoftheuser(insteadofaprojectedfuturenextworth),the
indexdoesnotrequireanyassumptions.
Figure2illustratestheindexdynamicsincomparisontonetworthasalumpsumina
simplifiedlifecyclemodelwithnouncertainty.Anindividualwithaknownend-of-lifedate
receivesaconstantincomefloweveryperioduntilaknownretirementage.Underanystandard
preferences,theindividualwillperfectlysmooththeirconsumptionovertheirlifetime.Networth
asalumpsumincreasesduringtheconsumer’sworkingyears,peaksatretirementage,decreases
overtheretirementyears,anddepletesattheendoflife.Networthasapersonalizedindex
describestheconstantcashflowlevelthattheconsumercangeneratefortherestoftheirlife,
giventheircurrentnetworthandtimetilltheendoflife.Duringtheconsumer’sworkingyears,
likethelumpsum,theindexgraduallyincreases.Twofactorscontributetotherateofincrease:
wealthaccumulationandtheshorteningofremaininglife.Theindexpeaksatretirementage,
whereitconvergestotheconsumptionlevelandremainsconstantuntiltheendoflife.
9

Thisindexcanpotentiallyprovideusefulfinancialguidancefortheindividual.Fora
personinretirement,theindexaccuratelyshowstheoptimallevelofconsumptioninthe
simplifiedframeworkdescribedabove.Apersonapproachingretirementagecancheckwhether
theconsumptionlevelisclosetotheindexlevel.Ifthedifferencebetweenspendingandtheindex
levelsislarge,theycanconsideradjustingtheconsumptionlevel,theincome,oreventhe
retirementage.Forayoungerperson,theindexissignificantlylowerthantheoptimal
consumptionlevel.Thatpersoncanmonitorwhethertheindexlevelandtheconsumptionlevel
convergequicklyenough.
Thepresentationofthepersonalizedindexcanimpactconsumers’behaviorthrough
severalnon-exclusivechannels.First,theindexmightreduceconsumers’“illusionofwealth.”
Goldstein,Hershfield,andBenartzi(2016)showthat,whennetworthissufficientlyhigh,people
tendtoperceiveitashavingahighervaluethantheequivalentmonthlycashflow.The
presentationofnetworthasamonthlycashflowinsteadofalumpsummightencourageusersto
feellesswealthyandchangetheirspendingbehavior.
Second,monthlycashflowisthecommonlyusedunitofmeasureforspending,suchas
monthlybillsforrent,mortgage,andutilities.Thepresentationofnetworthasamonthlycash
flowprovidesareferencepointforspendingactivitythatencouragesconsumerstomentally
simulatetheirlivesunderadifferentmonthlybudget.Reference-dependentutilityconsumersare
predictedtobeespeciallysensitivetopotentialchangesintheirstandardoflivingandmight
thereforeadjusttheirspendinglevels.
Third,theindexmightserveasananchorforspendingactivity.Anchoreffectsoccur
whenaninitialsalientvalueinfluencesindividuals’subsequentestimationsordecisions.These
effectsareespeciallypronouncedwhentherearenoothercompetingreferencepointsor
10

informationavailable(Kahneman(1992)).Giventhatconsumerstypicallydonotknowtheir
optimallevelofspendingnordoestheappprovideanyotherbenchmarkforspending,theindex
mighthaveastrongimpactasananchor.
Notethatnoneofthesechannelsrequiresconsumerstofullyunderstandtheeconomic
interpretationoftheindex.Infact,itishighlyplausiblethatmanyusersdonotfullygraspits
meaning,sincedoingsowouldrequirerelativelyadvancedfinancialandeconomicknowledge.
Thereareseveralreasonsforusingtheindexasthesubjectforinformationdesign
manipulations.First,itisanewinformationcontentthatisnotalreadyavailableontheapp.This
requirementensuresthatallusershavethesameleveloffamiliaritywiththeexperimentalcontent
andarenotbiasedtowardtheoldinformationdesign.Second,theselectionoftheindexis
motivatedbypreviousstudiesinbehavioraleconomics,policydiscussions,andpracticesinthe
financialindustry.TheacademicresearchdiscussedinSectionIexaminestheeffectsof
informationdesignmanipulationonconsumers’demandforlifeannuities,providingafoundation
forexploringtheimpactofthepersonalizedindexonconsumerspendinginthisstudy.
Additionally,therecentSECUREwhite Act(2019)requiringretirementaccountprovidersto
displaytheaccount’sworthasaprojectedlifetimemonthlyincomeandtheofferingofsimilar
personalizedindicesbythefinancialindustry,suchas“CoRI”byBlackRock,demonstratethe
applicabilityoftheindextoconsumers’spendingandsavingsdecisions.
III. Experimental Design
Theexperimentwasembeddedinafinancialmanagementappthatisofferedtothe
generalpublicatnocost.Thefirstwebpageusersviewafterloggingintotheappisthe
11

“dashboard”page,whichprovidesabriefsummaryoftheuser’sfinances.Thepre-experiment
dashboardpageispresentedinFigureC1.Userswererandomlyassignedtosevengroups.7 Apart
fromthecontrolgroup,alltreatedgroupsreceivedapersonalizedindex.Thetreatmentsdiffered
inthenameoftheindexandintheavailabilityofacontextplot.Thetreatmentsaresummarized
inTable1andillustratedinFigure1.Thetreatmentgroupsaredefinedasfollows:
ControlGroup(FigureC1):Thedashboardpagewasnotchangedforusersinthisgroup.
Thepageincludestime-seriesplotsofnetworth,totalincome,andtotalspending.Thisgroup
servesasabaselinetodetectanychangesinfinancialactivitythatarenotrelatedtothe
experiment.
FSI-PlotGroup(FiguresC2,C3):UsersreceivedtheFinancialSustainabilityIndex,
whichcontainsafearappealmessage.Theyalsoreceivedacontextplotprovidingasalient
comparisonbetweentheindexlevelandhistoricalmonthlyspending.
FSI-Plot-infGroup:Severalstudieshavesuggestedthathighannuitiespricesmight
explainthelowdemandforlifeannuities.8 Ifannuitiesareoverpriced,theconsumersmight
respondtotheindexbecauseitquotesanoverlypessimisticcashflow.Toaddressthisconcern,
thisgroupreceivedthesametreatmentastheFSI-Plotgroup,exceptthequotedindexwasinflated
by20%.Adifferentialresponsebetweenthesetwogroupswouldindicatethatthechangein
behaviorissensitivetotheexactquoteused.
FSI-NoPlotGroup(FigureC4):UsersreceivedtheFSIandnocontextplot.By
comparingthebehaviorofthisgrouptothatofusersintheFSI-Plotgroupwecanidentifythe
impactofprovidingasalientcomparisonbetweentheindexandspending.
7TwoofthesevengroupsareomittedfromthemaintextandaredescribedinAppendix??.
8SeethediscussioninBenartzietal.(2011),BrownandOrszag(2006),andBrown(2007).
12

LAI-PlotGroup(FigureC5):UsersreceivedtheLifeAnnuityIndexandnocontextplot.
BycomparingthebehaviorofthisgrouptothatofusersintheFSI-Plotgroup,wecanidentifythe
impactoftheframingeffectembeddedintheindexnames.
Theexperimentdidnotincludeatreatmentthatpresentstheindexusingneutralframing
(LAI)withacontextplotduetothelimitednumberofusersavailablefortheexperiment.Asa
result,weonlytesttheimpactofthecontextplotinthepresenceofconsumptionframing.
Goldsteinetal.(2016)andGodaetal.(2014)showedthatindividualsrespondto
informationaboutchangesintheircashflowstream.Followingtheirfindings,usersreceived
informationaboutthesensitivityoftheindexleveltochangesintheirnetworth(“Atcurrent
marketprices,anincreaseof$10,000inyournetworthwillincreaseyour[FSI/LAI]by$[X]”).
ThedashboardpageofallthetreatedgroupsincludedalinktoaFAQpage.TheFAQfor
eachgroupwasadjustedtoreflectthecorrespondingindexname.TheFAQpagefortheFSI-Plot
groupispresentedinFiguresC8andC9.
Historicalmonthlyincomewasremovedfromthedashboardpageinalltreatmentsbut
wasavailabletoallusersontheCashFlowpageoftheapp.Kahneman(1992)showsthatanchor
effectsareespeciallypronouncedwhennoothercompetingreferencepointsorinformationis
available.Theremovalofmonthlyincomefromthelandingpagedecreasesthesalienceofthis
informationandpotentiallyincreasesthelikelihoodofusingtheindexasthenewbenchmarkfor
spending.Inaddition,historicalmonthlyspendingwasnotpresentedonthedashboardpagefor
treatmentsthatdidnotreceiveacontextplot.Alluserscouldviewtheirhistoricalspendingonthe
CashFlowpageoftheapp.Theremovalofmonthlyspendingfromthelandingpagereducesthe
salienceofthisinformationandtheabilityofuserstodirectlycompareittotheindexlevel.
13

IV. Data
A. Annuity Price Quotes
WeobtainlifeannuitypricesfromHueler’sIncomeSolutions® annuityquotingplatform.
Thisplatformallowsindividualstoreceivecustomizedquotesofidenticalannuitycontractsfrom
largeinsurancecompaniesinrealtime.Allinsurancecompaniesthatprovidequotesarerated“A”
orabovebyMoody’s,S&P,andA.M.Best.Thecostsofinvestmentmanagement,distribution,
administration,andothercostsassociatedwithannuityproductsarereflectedintheannuity
quotes.Weuseannuityquotesofinflation-protectedlifeannuitiesforsingle,malebuyers
(reflectingthemajorityoftheappusers)withanonqualifiedincomeof$100,000.Weobtainthe
fullannuitiesquotesgridforallagesbetween35and85,allcommencementdatesbetween
immediateandtheageof85,andallstates.9 Annuityquoteswereupdatedonceaweekduringthe
experiment.Thepersonalindexforeachuserwascalculatedastheaveragequotefromall
companiesgiventheuser’sage,stateofresidence,andnetworth.
B. Consumer Data
Thesampleconsistsofusersofthefinancialmanagementappwhoarenotclientsor
prospectiveclientsoftheappprovider’swealthmanagementservices.Werestrictthesampleto
usersabovetheageof35,whichistheminimumageoflifeannuityquotes.Additionally,retired
usersareexcludedfromthesampletoaccommodatethetwotreatmentgroupswheretheindex
9Twoofthetreatmentgroupsinthisstudyreceivedapersonalizedindexrepresentingacashflowstreamstarting
atretirementratherthanimmediately.Deferredannuitiesquoteswereusedforthesetwotreatmentgroups.Seedetails
inAppendix??.
14

representsadeferredannuityquotewithacommencementdateatretirement.Wekeepuserswho
hadbeenusingtheappforatleastfivemonthsbeforetheexperiment.
Thesampleincludesonlyuserswhologgedintotheappatleastonceinthethreemonths
beforetheexperiment,linkedatleastonecreditordebitaccount,andhadanaveragemonthly
incomeandspendingabove$1,000inthefivemonthsbeforetheexperimentlaunch.These
restrictionsensurethatthesampleincludesonlyuserswhoareactivelyusingtheapp.Wealso
excludeuserswithanetworthbelow$5,000sothatthelevelofthepersonalindexissufficiently
positive.
Usersofmobilefinancialappslogintoviewtheiraccountsmorefrequentlythanusers
whologinonlyfrompersonalcomputers(Carlin,Olafsson,andPagel(2023)).Toensure
consistencyinthelevelofexposuretotheappandtheexperimentmaterial,weincludeonlyusers
whohaveinstalledthemobileapppriortothestartoftheexperimentandhadloggedinusinga
mobiledeviceatleastonceinthethreemonthsbeforetheexperimentlaunch.
Thefinalsampleconsistsof3,138users.Dataonusers’transactionsandloginactivityare
collectedforaperiodof25months,startingfivemonthsbeforetheexperimentlaunchand
continuingfortwentymonthsafter.
Table3presentssummarystatisticsofthesampleasdocumentedonMarch17,2014,the
launchdayoftheexperiment.Theaverageageinthesampleis45.Theaveragenetworthis$1.1
million(median$0.6million),andtheaveragemonthlyincomefromallsourcesis$16.7K
(median$12.6K).Thepersonalizedindexinthistablewascalculatedforallusers,includingthe
controlgroup,astheaveragequoteonanimmediateinflation-protectedlifeannuity.Theaverage
indexlevelis$3,175,andthemedianis$1,561.Theaveragenumberofmonthlyloginsduringthe
fivemonthsbeforetheexperiment’slaunchis15.4(medianof7.6),indicatingthatusersinthe
15

sampleareactivelyusingtheapp.Theaveragemonthlyspendingisabout$12K,andthemedian
is$9.2K.Thespendinglevelsofusersinthissamplearewellabovetheirpersonalizedindex
levels,aspredictedforconsumersrelativelyfarfromretirementage(seediscussioninSectionII
andFigure2).
Themainvariableofinterestisdiscretionaryspending,whichreferstospendingonitems
overwhichconsumershaverelativelymorecontrolandcanadjustoverashortperiod,suchas
entertainmentandrestaurants.Wedefinediscretionaryspendingasthesumofspendingin
categoriesthatcorrespondtoindustriesintheConsumerDiscretionarysectoraccordingtothe
GlobalIndustryClassificationStandard(GICcode25).Thecompletelistofcategorieswith
examplevendorsforeachcategoryispresentedinTable2.Theaveragelevelofdiscretionary
spendinginthissampleis$3,689(median$2,789),constitutingabout30%ofoverallspending.
Weanalyzeexpendituresonclothing,entertainment,restaurants,andtravel,whicharerelatively
largecomponentsofdiscretionaryspending.Wealsoanalyzecashwithdrawals,whichreflect
additionalspendingnotincludedinthediscretionaryspendingvariable.Theaveragemonthly
cashwithdrawalinthissampleis$925,andthemedianis$355.
Overall,theconsumersinthissamplearerelativelywealthyandaresimilartoconsumers
inthe80thpercentileoftheincomedistributionbasedontheirincomelevel,overallspending,
andspendingonthecategoriesstudiedinthispaper.10
10BasedontheConsumerExpendituresSurveyoftheBLS.
16

| V. Empirical | Specification |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- |
Experimentmaterialswereavailableontheappforaperiodofeightmonths.Thedata
covertheperiodfromt=-5tot=19,wheretheexperimentlaunchmonthist=0.Wedefinetwo
indicatorvariables:
Intra:equals1foreventmonthsinwhichexperimentmaterialwaspresentedontheapp,
fromt=0tot=7.
Post:equals1foreventmonthsaftertheremovalofexperimentalmaterialfromtheapp,
fromt=8tot=19.
Themainempiricalspecificationis:
|     | j=5      |            | j=5      |         |          |
| --- | -------- | ---------- | -------- | ------- | -------- |
|     | (cid:88) |            | (cid:88) |         |          |
| (1) | y =      | β TG Intra | + γ      | TG Post | +δ +θ +ϵ |
|     | i,t      | j j,i      | t j      | j,i t   | i j i,t  |
|     | j=2      |            | j=2      |         |          |
wherey i,t)isanoutcomevariablesuchasloginsorlogspendingforconsumeriineventmonth
(
t.TG aretreatmentgroupindicatorvariablesforeachofthegroups,wheretheomittedgroup
j
servesasthereferencelevel.δ isanindividualfixedeffect,andθ isanevent-monthfixedeffect.
|     |     | i   |     |     | j   |
| --- | --- | --- | --- | --- | --- |
Standarderrorsareclusteredattheconsumerlevel.11
β capturestheaveragechangeintheoutcomevariablebetweenthepre-experiment
j
months(t=-5tot=-1)andtheexperimentmonths(t=0tot=7)ofconsumersintreatmentgroupj,
relativetothesamechangeintheomittedtreatmentgroup.Similarly,γ capturestheaverage
j
changeintheoutcomevariablebetweenthepre-experimentmonths(t=-5tot=-1)andthe
11Alltestsarerobusttodoubleclusteringofthestandarderrorsbyconsumerandyear-month.
17

post-experimentmonths(t=8tot=19)ofconsumersintreatmentgroupj,relativetothesame
changeintheomittedtreatmentgroup.
Inaddition,weestimatethefollowingspecificationforeachofthetreatmentgroups
separately:
t=19
(cid:88)
(2) y = β I(t)+δ +ϵ
i,t t i i,t
t=−4
whereI(t)isanevent-monthindicatorformontht.β capturesthechangeintheoutcome
t
variableineventmonthtrelativetoeventmontht=-5.Thiswithin-grouptime-seriesanalysis
allowsustotestthespeedanddurationofconsumers’responsetothetreatments.
VI. Results
A. Attention
Theexperimentcontentwaspresentedatthetopofthedashboardpage,whichisthefirst
pageusersseeafterloggingintotheapp.Giventhisplacementoftheexperimentcontent,login
activitymeasuresusers’exposuretotheexperimentmaterialsandlevelofattentiontotheir
personalfinances.
Table4reportstheeffectofthetreatmentsontheusers’numberofloginspermonth.The
referencetreatmentgroupinthefirstcolumnisthecontrolgroup.Thecoefficientsofallthe
interactionvariablesbetweenthetreatmentindicatorsandIntrarevealthatthechangein
monthlyloginsbetweenthethepre-experimentmonthsandtheexperimentmonthsis
18

significantlylargerforallthetreatmentgroupsrelativetothesamechangeinthecontrolgroup.
Usersineachofthetreatmentgroupsincreasedtheirloginfrequencyduringtheexperiment
monthsbyabout1.3loginspermonthrelativetothecontrolgroup.Thecoefficientsofthe
interactionvariablesbetweenthetreatmentindicatorsandPostshowthataftertheremovalofthe
experimentmaterial,thechangeinloginfrequencyofusersinalltreatmentgroupsrelativetothe
pre-experimentmonthsisstillgreaterthanthesamechangeinthecontrolgroup(about0.6more
monthlylogins),butthedifferenceisnotstatisticallysignificant.Columns2and3repeatthe
sameregressionwiththeFSI-PlotandFSI-Plot-infgroupsasthebaselinetreatments.Although
allgroupsincreasedtheirattentionlevelduringtheexperimentmonthsrelativetothecontrol
group,therearenonotabledifferencesintheloginfrequencyacrossanyoftheothertreatment
groupsduringoraftertheexperiment.
Theresultsforthetimeseriesanalysisforeachofthetreatmentgroupsarepresentedin
Figure3(formalresultsareinTableA1).Panel(a)displaystheestimatedcoefficientsinEquation
2,andpanel(b)showstheaveragepredictedvaluesineacheventmonth.Themonthlylogin
frequencyofthetreatmentgroupsissimilarandhighlycorrelatedbetweenallthegroupsbefore
thestartoftheexperiment.Att=0allthetreatedgroupsimmediatelydivergefromthecontrol
group,andthepredictedloginfrequencyremainshigherthroughouttheexperimentmonths.The
changeintheloginfrequencyofallthetreatedgroupsisstillhigherthanthatofthecontrolgroup
foraboutthreemonthsaftertheexperiment,afterwhichallthegroupsconvergetothesamelogin
frequency.
Overall,theloginanalysisshowsthatusersinalltreatedgroupsincreasedthelevelof
attentiontotheirfinancesthroughouttheexperimentmonths.Thechangeinloginfrequencyis
significantbutsmallinmagnitude,withonlyslightlymorethanoneloginpermonthrelativeto
19

thecontrolgroup.Thechangeinloginfrequencystartedimmediatelyafterthelaunchofthe
experimentandcanbeattributedtointerestinthenewcontentontheapp.Thelackofdifference
inloginfrequencyacrossthetreatedgroupsrevealsthattheincreasedattentioncannotbe
attributedtoanyspecifictreatmentfeature,suchastheindexnameorthepresentationofacontext
plot.Therefore,anydifferencesinspendingbehavioracrossthedifferenttreatmentscannotbe
attributedtoadifferenceinconsumers’loginfrequency.
B. Discretionary Spending
Table5presentstheanalysisofthetreatmenteffectsonthelogofdiscretionaryspending.
ThefirstcolumnshowsthatboththeFSI-PlotandtheFSI-Plot-infreducedtheirdiscretionary
spendingduringtheexperimentperiodbyabout15%relativetothechangeinthecontrolgroup
overthesameperiod.Noneoftheothergroupshadasignificantchangeintheirspending
behavior.Columns2and3formallyshowthattherewerenosignificantdifferencesbetweenthe
FSI-PlotandtheFSI-Plot-infgroups,andthatthechangeindiscretionaryspendingofthese
groupsissignificantlylowerthanthatoftheFSI-NoPlotandtheLAI-Plotgroups.Usingthe
samplemeanofmonthlydiscretionaryspending($3,689),a15%declineindiscretionary
spendingcorrespondstoadropof$553permonth,whichisabout4.5%ofoverallmonthly
spending.ThecoefficientsoftheinteractionvariablebetweenthetreatmentindicatorsandPost
showthataftertheremovaloftheexperimentmaterialfromtheapp,therewerenosignificant
differencesindiscretionaryspendingbetweenanyofthegroups.
Thisanalysisconfirmsthatinformationdesigncanhaveasubstantialimpacton
consumers’discretionaryspending.However,theeffectissensitivetospecificfeaturesin
20

informationpresentation.Consumersonlyrespondwhentheindexispresentedbothunderthe
consumptionframeandcontainsasalientcontext.Presentationofeithertheconsumptionframe
orasalientcontextbyitselfdoesnotyieldapartialresponse.Thelackofdifferenceineffectsize
betweentheFSI-PlotandFSI-Plot-infgroupsindicatesthattheeffectisrobusttotheexactquote
usedintheindex.
Treatmentsthatdidnotreceiveacontextplotwithaconsumptionframingoftheindex
namedidnotshowanydifferencesinspendingrelativetothecontrolgroup,suggestingthatthe
omissionofmonthlyincomeandspendingfromthedashboardpagedidnotimpactusers’
spendingbehavior.However,thedecreaseinspendingintheFSI-PlotandthePSI-Plot-infgroups
mighthavebeensmallerinmagnitudeifincomewasstillpresentedonthedashboardpage,
providingasalientalternativebenchmarkforspendinginsteadoftheindex.
Figure4showsthedynamicsofthechangeindiscretionaryspendingforeachofthe
experimentgroupsrelativetotheirspendingatt=-5(formalresultsareinTableA2).Thechanges
indiscretionaryspendingofallthegroupsarepositivelycorrelatedandsimilarinmagnitude
beforetheexperimentlaunch.Thepeakindiscretionaryspendingatt=-3andthesharpdeclineat
t=-2aredrivenbyseasonaleffects,withahighspendingmonthinDecemberfollowedbyalow
spendingmonthinJanuary.ThechangeindiscretionaryspendingoftheFSI-PlotandFSI-Plot-inf
groupsdivergefromalltheothergroupsimmediatelyatthelaunchoftheexperimentandremain
lowerthroughouttheexperiment.Thegapbetweenthesetwogroupsandalltheothergroups
remainedlargeforthreeadditionalmonthsaftertheexperimentandgraduallydecreased
afterwards.Thechangesindiscretionaryspendingofallthegroupsconvergeonlyatt=16,nine
monthsaftertheremovaloftheexperimentalcontentfromtheapp.
TheanalysisinFigure4showsthewithin-groupevolutionofdiscretionaryspending.To
21

testthepersistenceoftheeffectaftertheexperimentdurationacrossgroups,weconductan
additionalanalysisofdiscretionaryspendingovershorterperiodsthanusedinEquation1.The
resultsofthisanalysisarepresentedinTable6.Thedependentvariableisthelogofdiscretionary
spending.Theexplanatoryvariablesaretheinteractionsofgroupindicatorsandatimeperiod
indicatorwherethetimeperiodineachregressionislistedatthetopofthecolumn.Thecontrol
groupisthebaselinegroupinallcolumns,andthereferencetimeperiodisthefivemonthsbefore
theexperimentlaunch.12 Thefirsttwocolumnsshowthattheaveragechangeindiscretionary
spendingisabout15%lowerthanthechangeinthecontrolgroupduringtheexperimentmonths.
Column3showsthatthedeclineindiscretionaryspendingoftheaffectedtreatmentsduringthe
followingfourmonthsremainedabout15%lowerthanthechangeinthecontrolgroup.However,
thiseffectisonlysignificantatthe10%level.Themagnitudeofthechangeinthesegroups
decaysovertime,andthepointestimatesofallthegroupsaresimilartoeachotherbetweent=16
andt=19.
Overall,theanalysisinFigure4andTable6showsthatthetreatmentshadlastingeffects
beyondtheperiodinwhichtheexperimentcontentwaspresentedontheapp.TheFSI-Plotand
FSI-Plot-inftreatmentsgroupsreducedtheirdiscretionaryspendingimmediatelyatthestartof
theexperimentbutresumedtheirnon-treatmentlevelsofspendingonlyafterseveralmonths.
C. Spending Categories
InTable7,wetesttheaveragespendingresponseindifferentspendingcategories.
Column1showsthatboththeFSI-PlotandFSI-Plot-infreducedtheirrestaurantexpendituresby
12Thesampleineachregressionincludesthepre-experimentmonths(t=-5tot=-1)andthefourmonthslistedat
thetopofeachcolumn.
22

about14%relativetoalltheothergroupsduringtheexperimentmonths.Restaurantspendingis
relativelyeasytoadjustbyvisitinglessexpensiverestaurantsordiningathome.Usersinthese
groupsalsoreducedtheirclothingexpendituresbyasignificant20%relativetotheothergroups
(Column2).Clothingexpensescanberelativelyeasilyadjustedaswellbyreducingpurchase
frequencyorclothingprice.Column3showsthatusersintheFSI-PlotandFSI-Plot-inf
treatmentsdecreasedtheirexpendituresonentertainmentbyabout14%percentrelativetothe
changeinothergroups.Column4showsadecreaseofabout24%intravelexpensesforusersin
thesetwogroups.Travelislikelytobealuxuryitemformanyconsumersthatcanbeadjustedby
choosingamoremodestvacationorskippingitaltogether.
Column5showsthatconsumersintheFSI-PlotandFSI-Plot-infgroupsreducedtheir
cashwithdrawalsbyabout25%comparedtoothergroups.Unlikethepreviousspending
categories,cashwithdrawalsarenotincludedinthediscretionaryspendingvariable.Therefore,
thisdecreaseincashwithdrawalsreflectsanadditionaldecreaseinspending.Thisevidenceis
consistentwithconsumersplacingahighersubjectivevalueoncashtransactionsandtherefore
beingmorelikelytoreducethesetransactionsfirst(RaghubirandSrivastava(2008)).
SussmanandAlter(2012)classifiedtransactionsintoordinary(i.e.,commonand
frequent)transactionsandexceptional(i.e.,unusualorinfrequent)transactions,withmanyofthe
largestexpensesbeingthemostexceptional.13 Theyshowthatalthoughconsumersarefairly
skillfulatplanningtheirordinaryspending,theysystematicallyunderestimatetheirfuture
expendituresonexceptionalitems.Consumerstendtocategorizeeachexceptionalexpenseasa
uniqueoccurrenceandconsequentlyoverspendafteraseriesofexceptionalexpenses.Moreover,
13SeeadditionaldiscussioninKarlanetal.(2016).
23

changesinlargeandinfrequentexpendituresmightbeeasiertoimplement,astheconsumerwill
havetomakeasingle(large)mentalefforttoapplyself-controlratherthanexercisedisciplineand
sacrificeeveryday.
Wetestifthedecreaseinspendingisaresultofareductioninspendingonexceptional
expenses.Weusethesumofthefivelargesttransactionsofeachuserinagivenmonthasaproxy
forlargeandinfrequenttransactions.14 Notethattheconsumers’largesttransactionsaretypically
rent,mortgage,andloanpayments.However,theseexpensesaretypicallyconstantovertimeand
arethereforeabsorbedbytheconsumerfixedeffects.Column6showsthatboththeFSI-Plotand
FSI-Plot-infgroupssignificantlyreducedtheirlargetransactionsduringtheexperimentmonths,
suggestingthattheseusersavoidedorreducedspendingoninfrequentlarge-tickettransactions.
Overall,thereductioninspendingisdrivenbyadecreaseinbothcommonandexceptional
transactions.
D. Additional Tests
InthefirstcolumnofTable8,wetesttheeffectofthedifferenttreatmentsontheusers’
overallspendinglevel.Wefindadeclineofabout6%inoverallspendingintheFSI-Plotand
FSI-Plot-infgroupsrelativetothechangeinanyoftheothertreatmentgroups.However,this
declineisonlysignificantatthe10%level.Giventheaveragemonthlymeanofoverallspending
of$12,364,adecreaseof6%inoverallspendingtranslatestoareductionofapproximately$742
permonth.Thisdecreaseroughlycorrespondstothecombineddecreaseinmonthlydiscretionary
14Resultsarerobusttotheselectednumberofextremetransactions.
24

spendingandcashwithdrawals.15 Inaddition,wetesttheeffectofthedifferenttreatmentson
overallmonthlyspendingminusdiscretionaryspendingandcashwithdrawalsandfindno
significantdifferencesbetweenanyofthegroups.Thisevidenceconfirmsthatconsumersdidin
factdecreasetheirspendinglevelsanddidnotshifttheirexpensesfromdiscretionaryspending
andcashtransactionstootherspendingcategories.
Asafalsificationtest,wecheckifthereisachangeinspendingcategoriesthatare
relativelydifficulttoadjust,especiallyintheshortrun.Wefindnosignificantdifferencesin
spendingongas,groceries,telephone,orutilitiesbetweenanyofthetreatmentgroups(columns2
to5).
VII. Conclusion
Thispaperdocumentsthecriticalimpactofinformationdesignonconsumers’spending
behavior.Theframeinwhichtheinformationispresentedandthesalienceofthecontextcan
haveasignificantimpactonconsumers’spending,despitestrongbehavioralinertiainspending
andthetemporaldistancebetweenexposuretotreatmentandthespendingactivity.Furthermore,
theeffectsonspendingbehaviorstartimmediatelyaftertheexposuretothetreatmentandlastfor
severalmonthsbeyondtheexperimentduration,showingthattheimpactoftheinformation
designlastsbeyondtheexposuretothetreatmentandsupportsanasymmetricaladjustmentof
spendinghabits.
Informationtoolsthatinfluencespendingbehaviorofferseveraladvantagesoverthe
15Thedecreaseinmonthlydiscretionaryspending=15%*$3,689=$553.Thedecreaseinmonthlycash
withdrawals=25%*$925=$231.
25

existingtoolsaimedatinfluencingsavingbehavior.First,informationdesigntoolsareeasyto
implementatlowcostrelativetofinancialeducation,taxsubsidies,andemployermatching
contribution.Second,unlikechoicearchitectureinterventions,informationdesigntoolscanbe
appliedtoallconsumersratherthanonlytoindividualswithretirementplans.Third,adecreasein
spendingreflectsanequalsizeincreaseinconsumersavings.Anincreaseinretirementplan
contributionsmightnotreflectanincreaseinsavingsduetoearlywithdrawalsandanincreasein
borrowing.
Thesensitivityofindividuals’responsestosubtledetailsininformationpresentationcan
beleveragedbyfirms.Forinstance,wealthmanagementcompaniescanutilizeinformationdesign
toolsthatenhancetheirclients’savingrates.Ontheotherhand,loanproviderscanstrategically
designinformationtoencourageconsumerstoincreasetheirspendingandborrowinglevels.
Giventhepotentialimpactofinformationdesignonconsumerbehavior,policymakers
mayneedtoconsiderregulationstoprotectconsumersinthiscontext.Currentregulationson
informationpresentationalreadyexistinvariousindustriessuchasfood,tobacco,alcohol,and
cosmetics,wherewarninglabelsareregulatedintermsofcontent,size,location,andcolor.
However,intherealmofconsumerfinance,informationdesignregulationsareprimarilylimited
toareassuchasinterestratequotes,creditcardstatements,andfeedisclosure.Byspecifying
guidelinesandstandardsforthepresentationofpersonalfinancialinformation,policymakerscan
mitigatedeceptivepracticesbyfirms.
Acommonlimitationofallresearchusingtransactionleveldataisthepotential
incompletenessofthedata.Dataobtainedfromaccountaggregationapps,banks,orcreditcard
companiesmightnotincludealltheconsumers’accounts.Itispossiblethatthechangein
spendingbehaviorintheobservedaccountsisoffsetbyanincreaseinspendinginunobserved
26

accounts.Similarconcernsexistedintheretirementcontributionliteratureformorethantwo
decadesuntilChettyetal.(2014)showedthatanincreaseinretirementcontributionsdoesnot
crowdoutsavingsinotheraccounts.Wemitigatethisconcernbyselectingrelativelyactiveusers
whoaremorelikelytohavelinkedalltheiraccountstotheapp.16
Anotherlimitationcausedbypotentialdataincompletenessistheinaccurateestimationof
users’networthandpersonalizedindex.Theomissionofretirementordebtaccountswillbiasthe
networthpresentedontheapp.Additionally,realassetssuchasrealestatearenotincludedinthe
app.Itispossiblethatconsumersrespondtotheindextheyobserveontheappevenifitdoesnot
reflecttheirrealnetworth.Alternatively,theymightignoretheindexiftheyfeelthatitdoesnot
representtheircurrentfinancialsituationaccurately.
Thispaperdemonstratesthesignificantimpactofinformationdesignonthespending
behaviorofconsumerswhoarerelativelyfarfromretirementandwhosespendinglevelsare
significantlyabovetheirindexlevels.Futureresearchshouldexploretheeffectsofproviding
annuitizedvaluestoconsumersatornearretirement.Theseconsumersmayhavespendinglevels
belowtheirannuitizednetworth,andexaminingwhethertheyincreasetheirspendingafterbeing
exposedtotheindexcouldoffervaluableinsightsintotheretirementdecumulationpuzzle.17
Futureresearchcanexploretheexactmechanismsthroughwhichtheindexinfluences
consumerbehavior.Onepossibilityisthattheindexprovidesnewinformationthatwasnot
previouslyavailabletoconsumers,expandingtheirinformationsetandleadingtoimproved
spendingdecisions.Anotherpotentialchannelisthattheindexestablishesanewreferencepoint
16SeeBakerandKueng(2022)forafulldiscussiononthelimitationsofresearchusingtransaction-leveldata.
17SeeBattistin,Brugiavini,Rettore,andWeber(2009)foracomprehensivereviewoftheretirementdecumulation
puzzle.
27

forspending,distinctfromthereferencepointconsumerspreviouslyused,suchasmonthly
income.Finally,itispossiblethattheindexservesasananchorforspendingbehavior,meaning
consumersmightadjusttheirspendinglevelsbasedonanyrandomsalientreferencepoint
provided.
Thisstudyshowsthatthepresentationoftheindexhasacriticalroleininfluencing
consumerbehavior.Theconsumptionframeusedtodescribetheindexpotentiallyinducesa
feelingofguiltandregret,leadingtoanimprovementinconsumers’self-controlthrougha
decreaseinthetemptationvalueofunnecessaryspending(e.g.,Baumeister(2002),Fudenberg
andLevine(2012),HochandLoewenstein(1991)).Thecontextplotcomparingtheindextothe
consumerspendingprimesuserstotakeaspecificactionofcuttingtheirspendingandincreasing
theirsavings(e.g.,GollwitzerandSheeran(2006)).Futureresearchcanexploreifsimilar
informationdesignscaninfluenceotherconsumers’decisions,suchasstockmarketparticipation,
debtrepayment,andtheclaimingageofsocialsecuritybenefits.
Consumersuseavarietyofbenchmarksfortheirspendingbehavior,suchastheirmonthly
incomeorspendinginthepreviousmonth.Recentstudieshaveshownthatprovidingconsumers
withinformationabouttheirpeers’income,debt,orspendinglevelscaninfluencetheirown
spendingbehavior(D’Acuntoetal.(2023),vanRooij,Coibion,Georgarakos,Candia,and
Gorodnichenko(2024)).Thisstudydemonstratesthatconsumersadjusttheirspendingwhen
presentedwiththeannuitizedvalueoftheirnetworth.Futureresearchshouldexplorewhichof
thesebenchmarksconsumersperceiveasmostimportantandwhetherthepresentationofsingleor
multiplebenchmarkshasastrongerimpactonconsumerspending.
28

References
Agnew,J.R.;L.R.Anderson;J.R.Gerlach;andL.R.Szykman. “Whochoosesannuities?An
experimentalinvestigationoftheroleofgender,framing,anddefaults.” AmericanEconomic
Review,98(2008),418–22.
Andreoni,J. “Warm-glowversuscold-prickle:theeffectsofpositiveandnegativeframingon
cooperationinexperiments.” TheQuarterlyJournalofEconomics,110(1995),1–21.
Argento,R.;V.L.Bryant;andJ.Sabelhaus. “Earlywithdrawalsfromretirementaccountsduring
thegreatrecession.” ContemporaryEconomicPolicy,33(2015),1–16.
Bai,C.-E.;W.Chi;T.X.Liu;C.Tang;andJ.Xu. “Boostingpensionenrollmentandhousehold
consumptionbyexample:Afieldexperimentoninformationprovision.” Journalof
DevelopmentEconomics,150(2021),102622.
Baker,S.R. “Debtandtheresponsetohouseholdincomeshocks:Validationandapplicationof
linkedfinancialaccountdata.” JournalofPoliticalEconomy,126(2018),1504–1557.
Baker,S.R.,andL.Kueng. “Householdfinancialtransactiondata.” AnnualReviewofEconomics,
14(2022),47–67.
Battistin,E.;A.Brugiavini;E.Rettore;andG.Weber. “Theretirementconsumptionpuzzle:
evidencefromaregressiondiscontinuityapproach.” AmericanEconomicReview,99(2009),
2209–26.
Baumeister,R.F. “Yieldingtotemptation:Self-controlfailure,impulsivepurchasing,and
consumerbehavior.” JournalofconsumerResearch,28(2002),670–676.
29

Becker,G. “DoesFinTechaffecthouseholdsavingbehavior.” Findingsfromanaturalfield
experiment,2009(2017),1–47.
Benartzi,S.;A.Previtero;andR.H.Thaler. “Annuitizationpuzzles.” JournalofEconomic
Perspectives,25(2011),143–64.
Beshears,J.;J.J.Choi;C.Clayton;C.Harris;D.Laibson;andB.C.Madrian. “Optimal
illiquidity.” NationalBureauofEconomicResearch(2020a).
Beshears,J.;J.J.Choi;J.M.Iwry;D.C.John;D.Laibson;andB.C.Madrian. “Building
EmergencySavingsThroughEmployer-SponsoredRainy-DaySavingsAccounts.” TaxPolicy
andtheEconomy,34(2020b),43–90.
Beshears,J.;J.J.Choi;D.Laibson;B.C.Madrian;andG.S.Goda. 4.TheAvailabilityand
Utilizationof401(k)Loans. UniversityofChicagoPress(2012).
Beshears,J.;J.J.Choi;D.Laibson;B.C.Madrian;andS.P.Zeldes. “Whatmakesannuitization
moreappealing?” Journalofpubliceconomics,116(2014),2–16.
BoardofGovernorsoftheFederalReserveSystem. “ReportontheEconomicWell-BeingofU.S.
Householdsin2020.” Availableat:https://www.federalreserve.gov/publications/2021-
economic-well-being-of-us-households-in-2020-executive-summary.htm.
Bra¨uer,K.;A.Hackethal;andT.Hanspal. “Consumingdividends.” TheReviewofFinancial
Studies,35(2022),4802–4857.
Brown,J.R. “Rationalandbehavioralperspectivesontheroleofannuitiesinretirement
planning.” NationalBureauofEconomicResearch(2007).
30

Brown,J.R.;A.Kapteyn;andO.S.Mitchell. “FramingandClaiming:HowInformation-F
RamingAffectsExpectedSocialSecurityClaimingBehavior.” JournalofRiskandInsurance,
83(2016),139–162.
Brown,J.R.;J.R.Kling;S.Mullainathan;andM.V.Wrobel. “Whydon’tpeopleinsurelate-life
consumption?Aframingexplanationoftheunder-annuitizationpuzzle.” AmericanEconomic
Review,98(2008),304–09.
Brown,J.R.;J.R.Kling;S.Mullainathan;andM.V.Wrobel. “Framinglifetimeincome.” The
JournalofRetirement,1(2013),27–37.
Brown,J.R.,andP.R.Orszag. “ThePoliticalEconomyofGovernment-IssuedLongevity
Bonds.” JournalofRiskandInsurance,73(2006),611–631.
Campbell,J.Y. “Householdfinance.” Thejournaloffinance,61(2006),1553–1604.
Carlin,B.;A.Olafsson;andM.Pagel. “Fintechadoptionacrossgenerations:Financialfitnessin
theinformationage.” NationalBureauofEconomicResearch(2017).
Carlin,B.;A.Olafsson;andM.Pagel. “Mobileappsandfinancialdecisionmaking.” Reviewof
Finance,27(2023),977–996.
Carvalho,L.;A.Olafsson;andD.Silverman. “Misfortuneandmistake:Thefinancialconditions
anddecision-makingabilityofhigh-costloanborrowers.”
Chen,X.,andS.C.Ludvigson. “Landofaddicts?anempiricalinvestigationofhabit-basedasset
pricingmodels.” JournalofAppliedEconometrics,24(2009),1057–1093.
31

Chetty,R.;J.N.Friedman;S.Leth-Petersen;T.H.Nielsen;andT.Olsen. “Activevs.passive
decisionsandcrowd-outinretirementsavingsaccounts:EvidencefromDenmark.” The
QuarterlyJournalofEconomics,129(2014),1141–1219.
Choi,J.J.;D.Laibson;andB.C.Madrian. “$100billsonthesidewalk:Suboptimalinvestmentin
401(k)plans.” ReviewofEconomicsandStatistics,93(2011),748–763.
Choi,J.J.;D.Laibson;B.C.Madrian;andA.Metrick. “Definedcontributionpensions:Plan
rules,participantchoices,andthepathofleastresistance.” Taxpolicyandtheeconomy,16
(2002),67–113.
Choi,J.J.;D.Laibson;B.C.Madrian;andA.Metrick. InPerspectivesontheEconomicsof
Aging. “Forbetterorforworse:Defaulteffectsand401(k)savingsbehavior.”Universityof
ChicagoPress(2004),81–126.
Choi,J.J.;D.Laibson;B.C.Madrian;A.Metrick;etal. “Savingforretirementonthepathof
leastresistance.” RodneyWhiteCenterforFinancialResearchWorkingPapers,9.
Chronopoulos,D.K.;M.Lukas;andJ.O.Wilson. “Consumerspendingresponsestothe
COVID-19pandemic:AnassessmentofGreatBritain.” AvailableatSSRN3586723.
D’Acunto,F.;A.G.Rossi;andM.Weber. “Crowdsourcingpeerinformationtochangespending
behavior.” ChicagoBoothResearchPaper.
DeMartino,B.;D.Kumaran;B.Seymour;andR.J.Dolan. “Frames,biases,andrational
decision-makinginthehumanbrain.” Science,313(2006),684–687.
Duflo,E.;W.Gale;J.Liebman;P.Orszag;andE.Saez. “Savingincentivesforlow-and
32

middle-incomefamilies:EvidencefromafieldexperimentwithH&RBlock.” TheQuarterly
JournalofEconomics,121(2006),1311–1346.
FederalReserveBoard. “ConsumersandMobileFinancialServices.” Availableat:
www.federalreserve.gov/econresdata/consumers-and-mobile-financial-services-report-
201603.pdf.
Fernandes,D.;J.G.LynchJr;andR.G.Netemeyer. “Financialliteracy,financialeducation,and
downstreamfinancialbehaviors.” ManagementScience,60(2014),1861–1883.
Ferson,W.E.,andG.M.Constantinides. “Habitpersistenceanddurabilityinaggregate
consumption:Empiricaltests.” JournalofFinancialEconomics,29(1991),199–240.
Fudenberg,D.,andD.K.Levine. “Timingandself-control.” Econometrica,80(2012),1–42.
Ganong,P.,andP.Noel. “Consumerspendingduringunemployment:Positiveandnormative
implications.” Americaneconomicreview,109(2019),2383–2424.
Gathergood,J.,andA.Olafsson. “TheCoholdingPuzzle:NewEvidencefromTransaction-Level
Data.” TheReviewofFinancialStudies,hhae016.
Gelman,M.;S.Kariv;M.D.Shapiro;D.Silverman;andS.Tadelis. “Harnessingnaturally
occurringdatatomeasuretheresponseofspendingtoincome.” Science,345(2014),212–215.
Goda,G.S.;C.F.Manchester;andA.J.Sojourner. “Whatwillmyaccountreallybeworth?
Experimentalevidenceonhowretirementincomeprojectionsaffectsaving.” JournalofPublic
Economics,119(2014),80–92.
33

Goedde-Menke,M.;M.Lehmensiek-Starke;andS.Nolte. “Anempiricaltestofcompeting
hypothesesfortheannuitypuzzle.” JournalofEconomicPsychology,43(2014),75–91.
Goldstein,D.G.;H.E.Hershfield;andS.Benartzi. “Theillusionofwealthanditsreversal.”
JournalofMarketingResearch,53(2016),804–813.
Gollwitzer,P.M.,andP.Sheeran. “Implementationintentionsandgoalachievement:A
meta-analysisofeffectsandprocesses.” Advancesinexperimentalsocialpsychology,38
(2006),69–119.
Hacıog˘lu-Hoke,S.;D.R.Ka¨nzig;andP.Surico. “Thedistributionalimpactofthepandemic.”
EuropeanEconomicReview,134(2021),103680.
Havranek,T.;M.Rusnak;andA.Sokolova. “Habitformationinconsumption:Ameta-analysis.”
EuropeanEconomicReview,95(2017),142–167.
Hershfield,H.E.;D.G.Goldstein;W.F.Sharpe;J.Fox;L.Yeykelis;L.L.Carstensen;andJ.N.
Bailenson. “Increasingsavingbehaviorthroughage-progressedrenderingsofthefutureself.”
JournalofMarketingResearch,48(2011),S23–S37.
Hoch,S.J.,andG.F.Loewenstein. “Time-inconsistentpreferencesandconsumerself-control.”
Journalofconsumerresearch,17(1991),492–507.
Johnson,E.J.;J.Hershey;J.Meszaros;andH.Kunreuther. “Framing,probabilitydistortions,and
insurancedecisions.” Journalofriskanduncertainty,7(1993),35–51.
Kahneman,D. “Referencepoints,anchors,norms,andmixedfeelings.” Organizationalbehavior
andhumandecisionprocesses,51(1992),296–312.
34

Karlan,D.;M.McConnell;S.Mullainathan;andJ.Zinman. “Gettingtothetopofmind:How
remindersincreasesaving.” ManagementScience,62(2016),3393–3411.
Ku¨hberger,A. “Theinfluenceofframingonriskydecisions:Ameta-analysis.” Organizational
behaviorandhumandecisionprocesses,75(1998),23–55.
Levi,Y.,andS.Benartzi. “Mindtheapp:Mobileaccesstofinancialinformationandconsumer
behavior.” AvailableatSSRN3557689.
Madrian,B.C.,andD.F.Shea. “Thepowerofsuggestion:Inertiain401(k)participationand
savingsbehavior.” TheQuarterlyjournalofeconomics,116(2001),1149–1187.
Maheswaran,D.,andJ.Meyers-Levy. “Theinfluenceofmessageframingandissue
involvement.” JournalofMarketingresearch,27(1990),361–367.
Medina,P.C. “Sideeffectsofnudging:Evidencefromarandomizedinterventioninthecredit
cardmarket.” TheReviewofFinancialStudies,34(2021),2580–2607.
Olafsson,A.,andM.Pagel. “Theliquidhand-to-mouth:Evidencefrompersonalfinance
managementsoftware.” TheReviewofFinancialStudies,31(2018),4398–4446.
Payne,J.W.;N.Sagara;S.B.Shu;K.C.Appelt;andE.J.Johnson. “Lifeexpectancyasa
constructedbelief:Evidenceofalive-toordie-byframingeffect.” JournalofRiskand
Uncertainty,46(2013),27–50.
Peters,G.-J.Y.;R.A.Ruiter;andG.Kok. “Threateningcommunication:acriticalre-analysisand
arevisedmeta-analytictestoffearappealtheory.” Healthpsychologyreview,7(2013),S8–S31.
35

Pronin,E.;C.Y.Olivola;andK.A.Kennedy. “Doinguntofutureselvesasyouwoulddounto
others:Psychologicaldistanceanddecisionmaking.” Personalityandsocialpsychology
bulletin,34(2008),224–236.
Pronin,E.,andL.Ross. “Temporaldifferencesintraitself-ascription:whentheselfisseenasan
other.” Journalofpersonalityandsocialpsychology,90(2006),197.
Raghubir,P.,andJ.Srivastava. “Monopolymoney:Theeffectofpaymentcouplingandformon
spendingbehavior.” Journalofexperimentalpsychology:Applied,14(2008),213.
Ravina,E. “HabitpersistenceandkeepingupwiththeJoneses:evidencefrommicrodata.”
SECUREwhite Act. “SettingEveryCommunityUpforRetirementEnhancementAct.” Available
at:https://www.congress.gov/bill/116th-congress/house-bill/1994/text.
Seibold,A. “Referencepointsforretirementbehavior:Evidencefromgermanpension
discontinuities.” AmericanEconomicReview,111(2021),1126–65.
Shafir,E.;P.Diamond;andA.Tversky. “Moneyillusion.” TheQuarterlyJournalofEconomics,
112(1997),341–374.
Strotz,R.H. “Myopiaandinconsistencyindynamicutilitymaximization.” Thereviewof
economicstudies,23(1955),165–180.
Sussman,A.B.,andA.L.Alter. “Theexceptionistherule:Underestimatingandoverspending
onexceptionalexpenses.” JournalofConsumerResearch,39(2012),800–814.
Tannenbaum,M.B.;J.Hepler;R.S.Zimmerman;L.Saul;S.Jacobs;K.Wilson;and
36

D.Albarrac´ın. “Appealingtofear:Ameta-analysisoffearappealeffectivenessandtheories.”
Psychologicalbulletin,141(2015),1178.
Thaler,R.H.,andS.Benartzi. “Savemoretomorrow™:Usingbehavioraleconomicstoincrease
employeesaving.” JournalofpoliticalEconomy,112(2004),S164–S187.
Thaler,R.H.,andH.M.Shefrin. “Aneconomictheoryofself-control.” Journalofpolitical
Economy,89(1981),392–406.
vanRooij,M.;O.Coibion;D.Georgarakos;B.Candia;andY.Gorodnichenko. “Keepingupwith
theJansens:Causalpeereffectsonhouseholdspending,beliefsandhappiness.” National
BureauofEconomicResearch(2024).
Wakslak,C.J.;S.Nussbaum;N.Liberman;andY.Trope. “Representationsoftheselfinthenear
anddistantfuture.” Journalofpersonalityandsocialpsychology,95(2008),757.
Willis,L.E. “Thefinancialeducationfallacy.” AmericanEconomicReview,101(2011),429–34.
Witte,K. InHandbookofcommunicationandemotion. “Fearasmotivator,fearasinhibitor:
Usingtheextendedparallelprocessmodeltoexplainfearappealsuccessesandfailures.”
Elsevier(1996),423–450.
Yogo,M. “Assetpricesunderhabitformationandreference-dependentpreferences.” Journalof
Business&EconomicStatistics,26(2008),131–143.
37

FIGURE1
TopofDashboardPagefortheFSI-PlotTreatment
38

FIGURE2
NetWorthandIndexLevelsOvertheConsumer’sLifeCycle
Thefigureillustratestheindexandnetworthlevelofalifecycleofaconsumerwithaconstant
incomelevelduringtheirworkingyearsandnoincomeafterretirement.Givennouncertainty,the
consumercansmooththeirconsumptionperfectly.Networthasalumpsumistheaccumulated
wealthfromincomesavings.Networthasanindexistheconstantconsumptionlevelthatthe
personcanafforduntiltheendoftheirlifegiventheirlevelofaccumulatedwealthandtimetill
theendoflife.Forsimplicity,therealreturnonsavingsissettozero.TheplotofNetWorthasa
lumpsumisscaleddownbyafactorof6.
39

FIGURE3
MonthlyLoginsbyTreatmentGroup
Panel(a)showstheestimatedcoefficientsinaregressionofmonthlylogincountoneventmonth
indicatorvariableswithconsumerfixedeffectsforeachtreatmentgroup.Panel(b)showsthe
averagepredictedvaluesforthatregression.DetailedregressionresultsareinTableA1.
(a) Coefficients
2
1
0
-1
-2
-3
-4
-5
tneiciffeoC
Start End
control
FSI-Plot
FSI-Plotinf
FSI-NoPlot
LAI-Plot
-5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Event month
(b) PredictedValues
18
17
16
15
14
13
12
11
snigoL
ylhtnoM
detciderP
Start End
control
FSI-Plot
FSI-Plotinf
FSI-NoPlot
LAI-Plot
-5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Event month
40

FIGURE4
MonthlyDiscretionarySpendingbyTreatmentGroup
Thefigureshowstheestimatedcoefficientsinaregressionoflogmonthlydiscretionaryspending
oneventmonthindicatorvariableswithconsumerfixedeffectsforeachtreatmentgroup.Detailed
regressionresultsareinTableA2.
.3 .2
.1 0
-.1
-.2
-.3
tneiciffeoC
Start End
control
FSI-Plot
FSI-Plotinf
FSI-NoPlot
LAI-Plot
-5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Event month
41

TABLE1
TreatmentGroups
indexand
| # groupname | indexname                    |     | spendingplot | comments |
| ----------- | ---------------------------- | --- | ------------ | -------- |
| 1 Control   |                              | -   | -            |          |
| 2 FSI-Plot  | FinancialSustainabilityIndex |     | yes          |          |
3 FSI-Plot-inf FinancialSustainabilityIndex yes indexinflatedby20%
| 4 FSI-NoPlot | FinancialSustainabilityIndex |     | no  |     |
| ------------ | ---------------------------- | --- | --- | --- |
| 5 LAI-Plot   | LifeAnnuityIndex             |     | yes |     |
42

TABLE2
DiscretionarySpendingCategories
SpendingCategories VendorExamples
AutomotiveExpenses Autozone,Honda,PepBoys
Cable/SatelliteServices Comcast,DirecTV,TimeWarnerCable
CharitableGiving CompassionInternational,FeedTheChildren,Greenpeace
Child/DependentExpenses Children’sPlace,Gymboree,Toys“R”Us
Clothing/Shoes Kohl’sCorporation,Macy’s,Nordstrom
DuesandSubscriptions ConsumerReports,TheNewYorkTimes,TheWallStreetJournal
Electronics AppleInc.,BestBuyCo.,Fry’sElectronics
Entertainment Redbox,RegalCinemas,StubHub
Gifts GodivaChocolatierInc,Hallmark,ProFlowers
Hobbies CampingWorld,Inc.,GuitarCenter,HobbyLobby
HomeImprovement BedBath&Beyond,HomeDepot,WilliamsAndSonoma
HomeMaintenance MerryMaids,StanleySteemerIntl.Inc.,TerminixIntl.Company
OnlineServices GooglePlay,Skype,TransUnion
PersonalCare Bath&BodyWorks,GreatClips,UltaSalon,Cosmetics&Fragrance
Pets/PetCare Petco’s,PetSmart,Wag.com
Restaurants/Dining McDonald’sCorporation,Starbucks,Subway
Travel DeltaAirLines,HiltonHotels,SouthwestAirlines
43

TABLE3
SummaryStatistics
Age,NetWorth,andPersonalizedIndex weredocumentedontheexperimentlaunchday.
PersonalizedIndex wascalculatedforallusers,includingthecontrolgroup,astheaverage
monthlycashflowquoteonanimmediatelifeannuity.Theremainingvariablesdescribemonthly
averagesoverthefivemonthsprecedingtheexperimentlaunch.
| Variable          | N     | Mean      | Std.Dev.  | 10%    | Median  | 90%       |
| ----------------- | ----- | --------- | --------- | ------ | ------- | --------- |
| Age               | 3,138 | 44.6      | 7.9       | 36.0   | 43.0    | 56.0      |
| NetWorth          | 3,138 | 1,128,106 | 1,493,896 | 72,558 | 637,308 | 2,623,589 |
| PersonalizedIndex | 3,138 | 3,178     | 5,211     | 168    | 1,561   | 7,462     |
Logins
|                       | 3,138 | 15.4   | 20.5   | 1.2   | 7.6    | 41.0   |
| --------------------- | ----- | ------ | ------ | ----- | ------ | ------ |
| Income                | 3,138 | 16,784 | 13,162 | 4,564 | 12,570 | 35,137 |
| Spending              | 3,138 | 12,364 | 9,887  | 3,341 | 9,200  | 25,913 |
| DiscretionarySpending | 3,138 | 3,689  | 3,449  | 553   | 2,789  | 7,930  |
| Clothing              | 3,138 | 374    | 495    | 12    | 205    | 929    |
| Entertainment         | 3,138 | 168    | 217    | 1     | 97     | 421    |
| Restaurants           | 3,138 | 504    | 480    | 40    | 386    | 1,076  |
| Travel                | 3,138 | 693    | 1,034  | 0     | 304    | 1,891  |
| CashWithdrawal        | 3,138 | 925    | 1,326  | 0     | 355    | 2,638  |
44

TABLE4
TreatmentEffectsonLoginBehavior
Thedependentvariableinallcolumnsisthecountofmonthlylogins.Control,FSI-Plot,
FSI-Plot-inf,FSI-NoPlot,andLAI-Plot aretreatmentgroupindicatorvariables(seeTable1for
details).Thebaselineperiodinallregressionsisthefivemonthsbeforetheexperimentlaunch
(t=-5tot=-1).Intraisanindicatorvariablefortheeightmonthsduringwhichexperiment
materialswerepresentedintheapp(t=0tot=7),andPost
isanindicatorforthefollowingtwelve
months(t=8tot=19).Reportedt-statisticsinparenthesesareheteroskedasticity-robustand
clusteredattheconsumerlevel.Thesymbols***,**,and*indicatestatisticalsignificanceatthe
1%,5%,and10%levels,respectively.
| Variables          | (1)     | (2)      | (3)          |
| ------------------ | ------- | -------- | ------------ |
| Control*Intra      |         | -1.417** | -1.288**     |
|                    |         | (-2.03)  | (-2.11)      |
| FSI-Plot*Intra     | 1.417** |          | 0.129        |
|                    | (2.03)  |          | (0.17)       |
| FSI-Plot-inf*Intra | 1.288** | -0.129   |              |
|                    | (2.11)  | (-0.17)  |              |
| FSI-NoPlot*Intra   | 1.293** | -0.123   | 0.005        |
|                    | (2.05)  | (-0.16)  | (0.01)       |
| LAI-Plot*Intra     | 1.229** | -0.187   | -0.058       |
|                    | (2.05)  | (-0.25)  | (-0.09)      |
| Control*Post       |         | -0.691   | -0.700       |
|                    |         | (-0.75)  | (-0.80)      |
| FSI-Plot*Post      | 0.691   |          | -0.009       |
|                    | (0.75)  |          | (-0.01)      |
| FSI-Plot-inf*Post  | 0.700   | 0.009    |              |
|                    | (0.80)  | (0.01)   |              |
| FSI-NoPlot*Post    | 0.522   | -0.169   | -0.177       |
|                    | (0.57)  | (-0.16)  | (-0.17)      |
| LAI-Plot*Post      | 0.556   | -0.135   | -0.144       |
|                    | (0.61)  | (-0.13)  | (-0.14)      |
| referencegroup     | Control | FSI-Plot | FSI-Plot-inf |
| consumerFE         | Y       | Y        | Y            |
| eventmonthFE       | Y       | Y        | Y            |
| N                  | 54,750  | 54,750   | 54,750       |
| adj.R2             | 0.74    | 0.74     | 0.74         |
45

TABLE5
TreatmentEffectsonDiscretionarySpending
Thedependentvariableinallcolumnsisthelogofmonthlydiscretionaryspending.Control,
FSI-Plot,FSI-Plot-inf,FSI-NoPlot,andLAI-Plot aretreatmentgroupindicatorvariables(see
Table1fordetails).Thebaselineperiodinallregressionsisthefivemonthsbeforetheexperiment
launch(t=-5tot=-1).Intraisanindicatorvariablefortheeightmonthsduringwhichexperiment
materialswerepresentedintheapp(t=0tot=7),andPost
isanindicatorforthefollowingtwelve
months(t=8tot=19).Reportedt-statisticsinparenthesesareheteroskedasticity-robustand
clusteredattheconsumerlevel.Thesymbols***,**,and*indicatestatisticalsignificanceatthe
1%,5%,and10%levels,respectively.
| Variables          | (1)      | (2)      | (3)          |
| ------------------ | -------- | -------- | ------------ |
| Control*Intra      |          | 0.156**  | 0.147**      |
|                    |          | (2.22)   | (2.25)       |
| FSI-Plot*Intra     | -0.156** |          | -0.009       |
|                    | (-2.22)  |          | (-0.13)      |
| FSI-Plot-inf*Intra | -0.147** | 0.009    |              |
|                    | (-2.25)  | (0.13)   |              |
| FSI-NoPlot*Intra   | -0.012   | 0.144**  | 0.135**      |
|                    | (-0.18)  | (2.00)   | (2.01)       |
| LAI-Plot*Intra     | 0.009    | 0.165**  | 0.156**      |
|                    | (0.13)   | (2.24)   | (2.26)       |
| Control*Post       |          | 0.092    | 0.073        |
|                    |          | (0.98)   | (0.77)       |
| FSI-Plot*Post      | -0.092   |          | -0.019       |
|                    | (-0.98)  |          | (-0.19)      |
| FSI-Plot-inf*Post  | -0.073   | 0.019    |              |
|                    | (-0.77)  | (0.19)   |              |
| FSI-NoPlot*Post    | -0.022   | 0.070    | 0.050        |
|                    | (-0.25)  | (0.73)   | (0.52)       |
| LAI-Plot*Post      | -0.035   | 0.057    | 0.038        |
|                    | (-0.37)  | (0.57)   | (0.37)       |
| referencegroup     | Control  | FSI-Plot | FSI-Plot-inf |
| consumerFE         | Y        | Y        | Y            |
| eventmonthFE       | Y        | Y        | Y            |
| N                  | 54,750   | 54,750   | 54,750       |
| adj.R2             | 0.64     | 0.64     | 0.64         |
46

TABLE6
TreatmentEffectsonDiscretionarySpendingOverFourMonthsIntervals
Thedependentvariableinallcolumnsisthelogofmonthlydiscretionaryspending.FSI-Plot,
FSI-Plot-inf,FSI-NoPlot,andLAI-Plot aretreatmentgroupindicatorvariables(seeTable1fordetails).
Thebaselineperiodinallregressionsisthefivemonthsbeforetheexperimentlaunch(t=-5tot=-1)and
thereferencegroupistheControl group.Treatmentgroupindicatorsareinteractedwithatimeperiod
indicatorforthefourmonthslistedatthetopofeachcolumn.Experimentmaterialswerepresentedon
theappfromt = 0tot = 7.Reportedt-statisticsinparenthesesareheteroskedasticity-robustand
clusteredattheconsumerlevel.Thesymbols***,**,and*indicatestatisticalsignificanceatthe1%,
5%,and10%levels,respectively.
| Variables |     | (1) | (2) | (3) | (4) | (5) |
| --------- | --- | --- | --- | --- | --- | --- |
Interaction: I(0 ≤ t ≤ 3) I(4 ≤ t ≤ 7) I(8 ≤ t ≤ 11) I(12 ≤ t ≤ 15) I(16 ≤ t ≤ 19)
| FSI-Plot*I(a | ≤ t ≤ b) | -0.140** | -0.172** | -0.153* | -0.141  | 0.018  |
| ------------ | -------- | -------- | -------- | ------- | ------- | ------ |
|              |          | (-2.02)  | (-1.97)  | (-1.69) | (-1.31) | (0.16) |
FSI-Plot-inf*I(a ≤ t ≤ b) -0.128** -0.166** -0.157* -0.136 0.074
|                |          | (-2.03) | (-2.00) | (-1.70) | (-1.28) | (0.63)  |
| -------------- | -------- | ------- | ------- | ------- | ------- | ------- |
| FSI-NoPlot*I(a | ≤ t ≤ b) | -0.004  | -0.020  | -0.049  | -0.028  | 0.010   |
|                |          | (-0.06) | (-0.23) | (-0.55) | (-0.28) | (0.09)  |
| LAI-Plot*I(a   | ≤ t ≤ b) | 0.007   | 0.011   | -0.057  | -0.012  | -0.036  |
|                |          | (0.10)  | (0.13)  | (-0.63) | (-0.12) | (-0.30) |
| consumerFE     |          | Y       | Y       | Y       | Y       | Y       |
| eventmonthFE   |          | Y       | Y       | Y       | Y       | Y       |
| N              |          | 19,710  | 19,710  | 19,710  | 19,710  | 19,710  |
| adj.R2         |          | 0.72    | 0.69    | 0.67    | 0.63    | 0.59    |
47

TABLE7
TreatmentEffectsonSpendingCategories
Thedependentvariablesincolumns(1)-(4)arethelogofmonthlyspendinginthecorresponding
category,andthelogofmonthlycashwithdrawalisincolumn(5).Thedependentvariablein
column(6)isthelogsumofthefivelargestspendingtransactionsforagivenconsumer-month.
FSI-Plot,FSI-Plot-inf,FSI-NoPlot,andLAI-Plot aretreatmentgroupindicatorvariables(seeTable
1fordetails).Thebaselineperiodinallregressionsisthefivemonthsbeforetheexperimentlaunch
(t=-5tot=-1)andthereferencegroupistheControl group.Intraisanindicatorvariableforthe
eightmonthsduringwhichexperimentmaterialswerepresentedintheapp(t=0tot=7),andPost is
anindicatorforthefollowingtwelvemonths(t=8tot=19).Reportedt-statisticsinparenthesesare
heteroskedasticity-robustandclusteredattheconsumerlevel.Thesymbols***,**,and*indicate
statisticalsignificanceatthe1%,5%,and10%levels,respectively.
| Variables | (1) | (2) | (3) | (4) | (5)  | (6)      |
| --------- | --- | --- | --- | --- | ---- | -------- |
|           |     |     |     |     | Cash | 5Largest |
Dependent: Restaurants Clothing Entertainment Travel Withdrawal Transactions
FSI-Plot*Intra -0.140** -0.219** -0.155** -0.222** -0.265** -0.127***
|     | (-1.96) | (-2.37) | (-2.23) | (-2.12) | (-2.23) | (-2.94) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- |
FSI-Plot-inf*Intra -0.137** -0.184** -0.132** -0.257** -0.237** -0.141***
|     | (-1.99) | (-2.07) | (-2.03) | (-2.45) | (-2.19) | (-3.92) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- |
FSI-NoPlot*Intra
|                   | 0.052   | 0.010   | 0.014   | 0.015   | -0.009  | -0.037  |
| ----------------- | ------- | ------- | ------- | ------- | ------- | ------- |
|                   | (0.75)  | (0.10)  | (0.21)  | (0.14)  | (-0.07) | (-0.98) |
| LAI-Plot*Intra    | 0.020   | -0.004  | 0.002   | 0.082   | 0.007   | -0.038  |
|                   | (0.29)  | (-0.05) | (0.03)  | (0.74)  | (0.06)  | (-1.03) |
| FSI-Plot*Post     | 0.004   | 0.089   | -0.018  | 0.035   | 0.006   | -0.042  |
|                   | (0.05)  | (0.81)  | (-0.20) | (0.27)  | (0.04)  | (-0.88) |
| FSI-Plot-inf*Post | 0.008   | 0.030   | 0.023   | -0.017  | 0.021   | 0.000   |
|                   | (0.09)  | (0.29)  | (0.28)  | (-0.13) | (0.15)  | (0.00)  |
| FSI-NoPlot*Post   | -0.021  | -0.010  | 0.016   | 0.027   | -0.030  | -0.011  |
|                   | (-0.23) | (-0.09) | (0.18)  | (0.21)  | (-0.21) | (-0.25) |
| LAI-Plot*Post     | -0.037  | -0.041  | -0.048  | 0.011   | 0.025   | 0.033   |
48
|              | (-0.40) | (-0.39) | (-0.56) | (0.08) | (0.17) | (0.71) |
| ------------ | ------- | ------- | ------- | ------ | ------ | ------ |
| consumerFE   | Y       | Y       | Y       | Y      | Y      | Y      |
| eventmonthFE | Y       | Y       | Y       | Y      | Y      | Y      |
| N            | 54,750  | 54,750  | 54,750  | 54,750 | 54,750 | 54,750 |
| adj.R2       | 0.70    | 0.48    | 0.56    | 0.48   | 0.49   | 0.49   |

TABLE8
TreatmentEffectsonAdditionalSpendingCategories
Thedependentvariablesarethelogofmonthlytotalspendingincolumn(1)andlogmonthly
spendinginthecorrespondingcategoryincolumns(2)-(5).FSI-Plot,FSI-Plot-inf,FSI-NoPlot,
andLAI-Plot aretreatmentgroupindicatorvariables(seeTable1fordetails).Thebaselineperiod
inallregressionsisthefivemonthsbeforetheexperimentlaunch(t=-5tot=-1)andthereference
groupistheControlgroup.Intraisanindicatorvariablefortheeightmonthsduringwhich
experimentmaterialswerepresentedintheapp(t=0tot=7),andPost
isanindicatorforthe
followingtwelvemonths(t=8tot=19).Reportedt-statisticsinparenthesesare
heteroskedasticity-robustandclusteredattheconsumerlevel.Thesymbols***,**,and*
indicatestatisticalsignificanceatthe1%,5%,and10%levels,respectively.
| Variables          | (1)      | (2)    | (3)       | (4)       | (5)       |
| ------------------ | -------- | ------ | --------- | --------- | --------- |
| Dependent:         | Spending | Gas    | Groceries | Telephone | Utilities |
| FSI-Plot*Intra     | -0.065*  | 0.026  | 0.010     | -0.046    | -0.086    |
|                    | (-1.95)  | (0.39) | (0.15)    | (-0.65)   | (-0.95)   |
| FSI-Plot-inf*Intra | -0.053*  | 0.090  | 0.069     | -0.001    | -0.080    |
|                    | (-1.74)  | (1.24) | (1.00)    | (-0.01)   | (-0.91)   |
FSI-NoPlot*Intra
|                   | 0.007   | 0.008   | 0.024   | 0.007   | -0.107  |
| ----------------- | ------- | ------- | ------- | ------- | ------- |
|                   | (0.22)  | (0.14)  | (0.35)  | (0.09)  | (-1.22) |
| LAI-Plot*Intra    | 0.006   | 0.093   | 0.025   | -0.030  | -0.021  |
|                   | (0.19)  | (1.43)  | (0.37)  | (-0.41) | (-0.22) |
| FSI-Plot*Post     | -0.003  | -0.024  | -0.041  | -0.012  | -0.126  |
|                   | (-0.06) | (-0.31) | (-0.42) | (-0.14) | (-1.06) |
| FSI-Plot-inf*Post | -0.012  | 0.010   | 0.063   | 0.051   | -0.073  |
|                   | (-0.30) | (0.11)  | (0.65)  | (0.58)  | (-0.66) |
| FSI-NoPlot*Post   | 0.021   | 0.023   | -0.005  | 0.071   | -0.162  |
|                   | (0.52)  | (0.34)  | (-0.06) | (0.82)  | (-1.46) |
| LAI-Plot*Post     | 0.017   | -0.098  | 0.013   | -0.082  | -0.167  |
|                   | (0.40)  | (-1.25) | (0.14)  | (-0.95) | (-1.44) |
| consumerFE        | Y       | Y       | Y       | Y       | Y       |
| eventmonthFE      | Y       | Y       | Y       | Y       | Y       |
| N                 | 54,750  | 35,450  | 43,625  | 34,650  | 33,550  |
| adj.R2            | 0.60    | 0.37    | 0.42    | 0.28    | 0.24    |
49

InternetAppendix
A. Detailed Analysis
50

TABLEA1
MonthlyLoginsbyTreatmentGroup(7Groups)
Thedependentvariableinallcolumnsisthecountofmonthlylogins.I(t = x)areeventmonth
indicatorvariables.Eventmontht = −5isthebaselinelevelinallcolumns.Eachcolumn
presentstheregressionresultsforagiventreatmentgroup.Thetreatmentgroupsincolumns(6)
and(7)aredescribedinAppendixB.Reportedt-statisticsinparenthesesare
heteroskedasticity-robustandclusteredattheconsumerlevel.Thesymbols***,**,and*
indicatestatisticalsignificanceatthe1%,5%,and10%levels,respectively.
| Variables | (1) | (2) | (3) | (4) | (5) | (6) | (7) |
| --------- | --- | --- | --- | --- | --- | --- | --- |
Treatment: Control FSI-Plot FSI-Plot-inf FSI-NoPlot LAI-Plot FSI-NoPlot-retire LAI-NoPlot-retire
I(t=-4) -1.893*** -2.867*** -1.998*** -2.505*** -1.958*** -1.906*** -3.304***
|         | (-3.65) | (-4.11) | (-2.80) | (-3.67) | (-3.12) | (-3.07) | (-5.36) |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| I(t=-3) | 1.371** | -0.047  | -0.473  | 1.334   | -0.059  | 1.294*  | -0.036  |
|         | (2.05)  | (-0.06) | (-0.59) | (1.55)  | (-0.07) | (1.71)  | (-0.04) |
I(t=-2) -1.633** -3.365*** -3.664*** -1.869** -2.437*** -2.046*** -3.246***
|     | (-2.40) | (-3.92) | (-4.07) | (-2.37) | (-2.86) | (-2.60) | (-4.21) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=-1) -1.144* -2.391*** -2.231** -0.724 -1.070 -1.078 -2.261***
|     | (-1.71) | (-2.72) | (-2.31) | (-0.88) | (-1.22) | (-1.34) | (-2.72) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=0) -2.679*** -1.161 -1.807** -0.887 -0.535 -0.809 -1.834**
|     | (-3.95) | (-1.28) | (-1.97) | (-1.04) | (-0.59) | (-0.95) | (-2.30) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=1) -3.869*** -2.258** -3.271*** -2.323*** -2.927*** -1.753** -3.837***
|     | (-5.94) | (-2.21) | (-3.51) | (-2.71) | (-3.20) | (-2.21) | (-5.08) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=2) -1.845*** -1.789* -1.344 -1.500* -1.934** -1.226 -2.537***
|     | (-2.83) | (-1.80) | (-1.44) | (-1.69) | (-2.08) | (-1.52) | (-2.82) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=3) -2.039*** -2.085** -1.436 -0.710 -1.683* -1.136 -2.788***
|     | (-2.99) | (-2.04) | (-1.47) | (-0.81) | (-1.80) | (-1.36) | (-3.06) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=4) -3.906*** -4.773*** -3.938*** -3.454*** -3.223*** -3.646*** -2.911***
|     | (-5.68) | (-4.65) | (-4.03) | (-4.10) | (-3.55) | (-4.55) | (-3.18) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=5) -3.443*** -3.557*** -3.133*** -1.601* -1.988** -2.174** -2.028**
|     | (-5.08) | (-3.36) | (-3.14) | (-1.86) | (-2.14) | (-2.51) | (-2.24) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=6) -4.493*** -3.974*** -3.900*** -3.523*** -4.192*** -3.178*** -3.537***
|     | (-6.15) | (-3.51) | (-3.52) | (-3.67) | (-4.62) | (-3.87) | (-3.92) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=7) -1.517** -1.457 -2.769** -0.191 -1.033 -0.350 -2.272**
|     | (-2.05) | (-1.28) | (-2.55) | (-0.20) | (-1.05) | (-0.38) | (-2.38) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=8) -3.199*** -3.180*** -3.133*** -2.288*** -2.237** -2.166** -3.628***
|     | (-4.42) | (-2.84) | (-2.87) | (-2.59) | (-2.15) | (-2.46) | (-3.58) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=9) -3.009*** -2.908*** -2.573** -1.350 -1.446 -1.413 -2.985***
|         | (-4.03) | (-2.74) | (-2.44) | (-1.40) | (-1.38) | (-1.51) | (-3.01) |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| I(t=10) | -1.144  | -0.872  | 0.038   | 0.329   | -0.230  | 0.589   | -1.720* |
|         | (-1.50) | (-0.80) | (0.03)  | (0.32)  | (-0.22) | (0.59)  | (-1.76) |
I(t=11) -2.201*** -1.813* -1.438 -1.793* -1.448 -0.509 -2.637***
|         | (-2.85) | (-1.67) | (-1.29) | (-1.76) | (-1.44) | (-0.52) | (-2.63)  |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- |
| I(t=12) | -0.299  | -0.704  | 0.009   | 0.214   | -0.444  | 0.713   | -0.367   |
|         | (-0.37) | (-0.63) | (0.01)  | (0.19)  | (-0.42) | (0.70)  | (-0.31)  |
| I(t=13) | -1.459* | -0.995  | -1.473  | -1.293  | -0.587  | -0.379  | -2.263** |
|         | (-1.82) | (-0.89) | (-1.34) | (-1.18) | (-0.52) | (-0.38) | (-2.07)  |
| I(t=14) | -0.592  | -1.583  | -1.271  | -0.606  | -1.026  | -0.312  | -1.845*  |
|         | (-0.75) | (-1.45) | (-1.17) | (-0.58) | (-0.93) | (-0.34) | (-1.77)  |
| I(t=15) | -0.428  | -1.607  | -1.682  | -0.906  | -1.995* | -0.656  | -2.546** |
|         | (-0.57) | (-1.44) | (-1.48) | (-0.86) | (-1.79) | (-0.72) | (-2.39)  |
I(t=16) -1.797** -3.443*** -2.756** -2.108** -3.005*** -2.080** -3.178***
|     | (-2.27) | (-3.04) | (-2.39) | (-2.01) | (-2.89) | (-2.34) | (-3.20) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=17) -1.797** -2.758** -3.829*** -1.903* -2.223** -1.591 -1.414
|     | (-2.11) | (-2.34) | (-3.33) | (-1.68) | (-2.02) | (-1.60) | (-1.36) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=18) -3.469*** -3.652*** -4.438*** -3.249*** -3.399*** -3.042*** -2.752***
|     | (-4.19) | (-3.23) | (-4.10) | (-3.01) | (-3.16) | (-3.23) | (-2.63) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
I(t=19) -2.199*** -2.675** -2.811** -1.484 -2.221** -1.413 -1.643
|            | (-2.68) | (-2.48) | (-2.47) | 51(-1.32) | (-2.00) | (-1.48) | (-1.56) |
| ---------- | ------- | ------- | ------- | --------- | ------- | ------- | ------- |
| consumerFE | Y       | Y       | Y       | Y         | Y       | Y       | Y       |
| N          | 11,450  | 10,550  | 11,250  | 10,850    | 10,650  | 11,925  | 11,775  |
| adj.R2     | 0.77    | 0.75    | 0.73    | 0.74      | 0.72    | 0.76    | 0.74    |

TABLEA2
MonthlyDiscretionarySpendingbyTreatmentGroup(7Groups)
Thedependentvariableinallcolumnsisthelogofmonthlydiscretionaryspending.I(t = x)are
eventmonthindicatorvariables.Eventmontht = −5isthebaselinelevelinallcolumns.Each
columnpresentstheregressionresultsforagiventreatmentgroup.Thetreatmentgroupsin
columns(6)and(7)aredescribedinAppendixB.Reportedt-statisticsinparenthesesare
heteroskedasticity-robustandclusteredattheconsumerlevel.Thesymbols***,**,and*
indicatestatisticalsignificanceatthe1%,5%,and10%levels,respectively.
| Variables | (1) | (2) | (3) | (4) | (5) | (6) | (7) |
| --------- | --- | --- | --- | --- | --- | --- | --- |
Treatment: Control FSI-Plot FSI-Plot-inf FSI-NoPlot LAI-Plot FSI-NoPlot-retire LAI-NoPlot-retire
I(t=-4) 0.189*** 0.141*** 0.073 0.143** 0.194*** 0.089** 0.144**
|         | (3.15)   | (2.96)  | (1.21)  | (2.29)  | (3.34)   | (2.57)    | (2.46)  |
| ------- | -------- | ------- | ------- | ------- | -------- | --------- | ------- |
| I(t=-3) | 0.226*** | 0.122*  | 0.143*  | 0.161** | 0.289*** | 0.061     | 0.099   |
|         | (3.26)   | (1.94)  | (1.83)  | (2.53)  | (4.03)   | (1.61)    | (1.53)  |
| I(t=-2) | -0.128*  | -0.101  | -0.089  | -0.051  | 0.051    | -0.118*** | -0.132* |
|         | (-1.77)  | (-1.38) | (-1.10) | (-0.65) | (0.66)   | (-2.68)   | (-1.71) |
I(t=-1) -0.132* -0.065 -0.037 -0.045 -0.093 -0.140*** -0.151*
|        | (-1.82) | (-0.88)  | (-0.47)  | (-0.55) | (-1.12) | (-3.19)   | (-1.96) |
| ------ | ------- | -------- | -------- | ------- | ------- | --------- | ------- |
| I(t=0) | -0.010  | -0.143*  | -0.119   | 0.130*  | 0.127*  | -0.058    | 0.104   |
|        | (-0.14) | (-1.73)  | (-1.32)  | (1.70)  | (1.69)  | (-1.28)   | (1.29)  |
| I(t=1) | -0.040  | -0.185** | -0.226** | -0.007  | 0.068   | -0.138*** | 0.018   |
|        | (-0.52) | (-2.06)  | (-2.52)  | (-0.08) | (0.85)  | (-2.88)   | (0.21)  |
| I(t=2) | 0.042   | -0.151*  | -0.133*  | -0.065  | 0.029   | -0.125**  | 0.018   |
|        | (0.56)  | (-1.84)  | (-1.71)  | (-0.70) | (0.36)  | (-2.46)   | (0.22)  |
I(t=3) -0.054 -0.188** -0.149* -0.092 -0.030 -0.143*** -0.089
|        | (-0.68) | (-2.06)  | (-1.74)  | (-1.04) | (-0.35) | (-2.72) | (-1.00) |
| ------ | ------- | -------- | -------- | ------- | ------- | ------- | ------- |
| I(t=4) | 0.030   | -0.172** | -0.162** | 0.011   | 0.036   | -0.074  | -0.095  |
|        | (0.37)  | (-1.98)  | (-2.00)  | (0.12)  | (0.40)  | (-1.52) | (-1.00) |
| I(t=5) | -0.040  | -0.183** | -0.169** | 0.024   | 0.071   | -0.065  | -0.099  |
|        | (-0.46) | (-2.06)  | (-1.98)  | (0.27)  | (0.81)  | (-1.34) | (-1.13) |
I(t=6) -0.022 -0.181** -0.244*** -0.101 0.082 -0.118** -0.132
|        | (-0.26) | (-2.02)   | (-2.66) | (-1.05) | (0.93) | (-2.44) | (-1.41) |
| ------ | ------- | --------- | ------- | ------- | ------ | ------- | ------- |
| I(t=7) | -0.010  | -0.238*** | -0.181* | -0.012  | 0.040  | -0.089* | -0.087  |
|        | (-0.11) | (-2.63)   | (-1.91) | (-0.14) | (0.44) | (-1.75) | (-0.91) |
| I(t=8) | 0.083   | -0.137    | -0.160  | 0.035   | 0.129  | -0.014  | -0.024  |
|        | (0.90)  | (-1.47)   | (-1.62) | (0.39)  | (1.45) | (-0.27) | (-0.27) |
| I(t=9) | 0.049   | -0.148    | -0.138  | -0.007  | 0.028  | -0.095* | -0.035  |
|        | (0.51)  | (-1.46)   | (-1.40) | (-0.07) | (0.29) | (-1.80) | (-0.39) |
I(t=10) -0.026 -0.235** -0.219** -0.067 -0.133 -0.175*** -0.157*
|            | (-0.29) | (-2.41) | (-2.33) | (-0.70)  | (-1.30) | (-3.33)   | (-1.76) |
| ---------- | ------- | ------- | ------- | -------- | ------- | --------- | ------- |
| I(t=11)    | -0.114  | -0.147  | -0.171* | -0.124   | -0.035  | -0.203*** | -0.127  |
|            | (-1.32) | (-1.63) | (-1.66) | (-1.28)  | (-0.39) | (-3.72)   | (-1.48) |
| I(t=12)    | 0.049   | -0.127  | -0.087  | 0.055    | 0.081   | -0.069    | 0.043   |
|            | (0.55)  | (-1.20) | (-0.87) | (0.54)   | (0.77)  | (-1.25)   | (0.45)  |
| I(t=13)    | 0.060   | -0.124  | -0.199* | 0.048    | 0.083   | -0.061    | -0.009  |
|            | (0.60)  | (-1.16) | (-1.91) | (0.48)   | (0.81)  | (-1.08)   | (-0.10) |
| I(t=14)    | 0.086   | -0.037  | -0.035  | 0.014    | 0.146   | -0.068    | 0.007   |
|            | (0.90)  | (-0.34) | (-0.35) | (0.13)   | (1.48)  | (-1.18)   | (0.07)  |
| I(t=15)    | -0.047  | -0.172  | -0.127  | -0.040   | 0.017   | -0.020    | -0.032  |
|            | (-0.49) | (-1.53) | (-1.21) | (-0.37)  | (0.17)  | (-0.35)   | (-0.32) |
| I(t=16)    | 0.049   | -0.057  | 0.013   | 0.000    | -0.054  | -0.044    | -0.093  |
|            | (0.47)  | (-0.53) | (0.12)  | (0.00)   | (-0.49) | (-0.74)   | (-0.86) |
| I(t=17)    | -0.097  | -0.033  | 0.080   | -0.085   | -0.037  | 0.010     | -0.130  |
|            | (-0.96) | (-0.30) | (0.78)  | (-0.76)  | (-0.33) | (0.15)    | (-1.18) |
| I(t=18)    | -0.098  | -0.012  | 0.060   | -0.002   | -0.033  | -0.192*** | -0.201* |
|            | (-0.94) | (-0.10) | (0.54)  | (-0.02)  | (-0.29) | (-3.03)   | (-1.77) |
| I(t=19)    | -0.008  | -0.026  | -0.063  | 0.018    | 0.055   | -0.024    | -0.136  |
|            | (-0.08) | (-0.23) | (-0.56) | 52(0.15) | (0.47)  | (-0.40)   | (-1.18) |
| consumerFE | Y       | Y       | Y       | Y        | Y       | Y         | Y       |
| N          | 11,450  | 10,550  | 11,250  | 10,850   | 10,650  | 11,925    | 11,775  |
| adj.R2     | 0.64    | 0.68    | 0.61    | 0.61     | 0.65    | 0.64      | 0.67    |

B. Additional Treatment Groups
Athirdvariationininformationdesign(inadditiontoframingandsalienceofcontext)
wasacurrent-versusfuture-selfframing.Anindividualcanbeviewedastwoconflictedagents:a
currentselfandafutureself(Strotz(1955),ThalerandShefrin(1981)).Previousstudiesconfirm
thatindividualstendtomakedecisionsthatfavortheircurrentselvesandoftentreattheirfuture
selvesastheywouldtreatastranger.18 Inthisstudy,weexaminetheeffectofpresentingthe
intertemporalchoicedilemmaineitheracurrent-selfframeorafuture-selfframe.
Inthecurrent-selfframing,usersreceivedtheannuitizedvalueoftheirnetworth
representedbyacashflowstreamthatstartsimmediately(usingimmediateannuitiesquote).In
thisframe,usersareprimedtoreflectonquestionsthatplacethecurrentselfinthecenter,suchas
“CanIretiretoday?”or“HowfarawayamIfromsustainablyretiring,basedonmycurrentnet
worth?”Inthefuture-selfframing,usersreceivedtheannuitizedvaluesoftheirnetworthasa
cashflowstreamstartingatretirement(calculatedusingthedeferredannuitiesquote).Underthis
frame,usersareprimedtoreflectonquestionsthatplacetheirfutureselfinthecentersuchas
“WillIhaveenoughmoneytospendwhenIretire?”Totheextentthatpeopleidentifywiththeir
currentselvesmorethantheirfutureselves,wecanexpectthatusersreceivingcurrent-self
framingwouldaltertheirsavingbehaviormorethanusersreceivingthefuture-selfframing.
Unliketheothervariationsintreatments,thecurrent-self/future-selfvariationisnotapure
informationdesigntest,astheusersareexposedtosomewhatdifferentinformationcontent.
Nevertheless,itisimportanttotestbecausemostfinancialplanners,retirementaccountproviders,
andtheSocialSecurityAdministrationoffersomeprojectionofwealthorincomeatafuturedate.
18ExamplesincludeProninandRoss(2006),Pronin,Olivola,andKennedy(2008),andWakslak,Nussbaum,
Liberman,andTrope(2008).Researchershavebeenexploringtoolstomitigatethisconflictbycreatingcommitments
tothefutureself(e.g.,Choi,Laibson,Madrian,Metricketal.(2005),ThalerandBenartzi(2004))orbyimproving
thevividnessorconnectednesswiththefutureself(Hershfield,Goldstein,Sharpe,Fox,Yeykelis,Carstensen,and
Bailenson(2011)).
53

Yetitisdifficulttoarguethattheexposuretothenewinformationcontentmightdrivea
differentialresponsebetweenthetreatments,asimmediateanddeferredannuityquotesare
equallyavailabletothepublic.19
Inadditiontothefiveexperimentgroupsdescribedinthemaintext,twoadditional
experimentgroupswereincludedtotestthecurrent-/future-selfframingeffect.Thegroupsare
describedbelowandinTableB1.
FSI-NoPlot-retireGroup(FigureC6):Usersinthistreatmentgroupreceiveda
personalizedindexnamedFSI,whichrepresentsapotentialcashflowthatwillstartatretirement
andnocontextplot.BycomparingthebehaviorofthisgrouptothatoftheFSI-NoPlotgroup,we
canidentifytheeffectofthecurrent-selforfuture-selfframingundertheconsumptionframe,but
withoutthesalienceofthespendingcontext.
LAI-NoPlot-retireGroup(FigureC7):Usersinthistreatmentgroupreceiveda
personalizedindexnamedLAI,whichrepresentsapotentialcashflowthatwillstartatretirement,
andnocontextplot.Bycomparingtheconsumptionbehaviorofthisgroupwiththatofthe
LAI-Plotgroup,wecanidentifytheeffectofthecurrent-selforfuture-selfframingcombined
withthecontexteffect.
Asnotedinthemaintext,framingeffectsaresensitivetothesalienceofthecontextin
whichtheyarepresented.Inthisstudy,itwasnotpossibletodesignatreatmentgroupwithhigh
salienceofcontextandfuture-selfframing.Presentationofcurrentspendinglevelswithfuture
potentialmonthlyincomeinthesameplotwaslikelytoconfuseusersandthereforewasnot
includedintheexperiment.
TableB2presentstheeffectofallthetreatmentsonloginbehavior.Boththe
FSI-NoPlot-retireandtheLAI-NoPlot-retiregroupsshowasimilarincreaseinloginactivityas
theothertreatmentgroups.Thisconfirmsthepreviousconclusionthattheincreaseinlogin
activitycanbeattributedtoaninterestinthenewfeaturesoftheapp.Also,astheincreasein
19Numerouswebsitesprovidefreequotesforbothimmediateanddeferredannuities.Inflation-protectedlife
annuitiesusedinthisstudyarerelativelydifficulttoobtainforbothimmediateanddeferredannuities.
54

loginactivityissimilaracrossalltreatedgroups,wereconfirmthatnoneoftheexperiment
featuresweremoreengagingthantherest(e.g.,differedannuityquotesdidnotdrawmore
attentionthantheimmediateannuityquotes).
Theremainingtablesandfiguresinthisappendixpresentthefullsetoftestsforallseven
treatmentgroupsintheexperiment.NeithertheFSI-NoPlot-retirenortheLAI-NoPlot-retire
treatmentshadanimpactonuserspendingbehaviorrelativetothecontrol,FSI-NoPlot,or
LAI-Plotgroups.Thelackofimpactofretirementtreatmentsreconfirmsthepreviousconclusion
thatframingeffectsaresensitivetothepresenceofasalientcontext.Currentorfutureframing
hadnodifferentialimpactonfinancialbehaviorintheabsenceofasalientcontext.Thelackof
responsetofuture-selfframingisconcerningandmeritsadditionalresearch,asitisacommon
methodofpresentingretirementincomeusedbyretirementaccountproviders.
55

TABLEB1
TreatmentGroups(7Groups)
indexand
| # groupname | indexname                    |     | spendingplot | comments |
| ----------- | ---------------------------- | --- | ------------ | -------- |
| 1 control   |                              | -   | -            |          |
| 2 FSI-Plot  | FinancialSustainabilityIndex |     | yes          |          |
3 FSI-Plot-inf FinancialSustainabilityIndex yes indexinflatedby20%
| 4 FSI-NoPlot | FinancialSustainabilityIndex |     | no  |     |
| ------------ | ---------------------------- | --- | --- | --- |
| 5 LAI-Plot   | LifeAnnuityIndex             |     | yes |     |
6 FSI-NoPlot-retire FinancialSustainabilityIndex no cashflowstartsatretirement
7 LAI-NoPlot-retire LifeAnnuityIndex no cashflowstartsatretirement
56

TABLEB2
TreatmentEffectsonLoginBehavior(7Groups)
Thedependentvariableinallcolumnsisthecountofmonthlylogins.Control,FSI-Plot,
FSI-Plot-inf,FSI-NoPlot,FSI-NoPlot-retire,LAI-Plot,andLAI-NoPlot-retirearetreatmentgroup
indicatorvariables(seeTableB1fordetails).Thebaselineperiodinallregressionsisthefive
monthsbeforetheexperimentlaunch(t=-5tot=-1).Intraisanindicatorvariablefortheeight
monthsduringwhichexperimentmaterialswerepresentedintheapp(t=0tot=7),andPost isan
indicatorforthefollowingtwelvemonths(t=8tot=19).Reportedt-statisticsinparenthesesare
heteroskedasticity-robustandclusteredattheconsumerlevel.Thesymbols***,**,and*
indicatestatisticalsignificanceatthe1%,5%,and10%levels,respectively.
| Variables               | (1)     | (2)      | (3)          |
| ----------------------- | ------- | -------- | ------------ |
| Control*Intra           |         | -1.417** | -1.288**     |
|                         |         | (-2.03)  | (-2.11)      |
| FSI-Plot*Intra          | 1.417** |          | 0.129        |
|                         | (2.03)  |          | (0.17)       |
| FSI-Plot-inf*Intra      | 1.288** | -0.129   |              |
|                         | (2.11)  | (-0.17)  |              |
| FSI-NoPlot*Intra        | 1.293** | -0.123   | 0.005        |
|                         | (2.05)  | (-0.16)  | (0.01)       |
| LAI-Plot*Intra          | 1.229** | -0.187   | -0.058       |
|                         | (2.05)  | (-0.25)  | (-0.09)      |
| FSI-NoPlot-retire*Intra | 1.277** | -0.139   | -0.011       |
|                         | (2.13)  | (-0.18)  | (-0.02)      |
| LAI-NoPlot-retire*Intra | 1.366** | -0.051   | 0.078        |
|                         | (2.12)  | (-0.06)  | (0.11)       |
| Control*Post            |         | -0.691   | -0.700       |
|                         |         | (-0.75)  | (-0.80)      |
| FSI-Plot*Post           | 0.691   |          | -0.009       |
|                         | (0.75)  |          | (-0.01)      |
| FSI-Plot-inf*Post       | 0.700   | 0.009    |              |
|                         | (0.80)  | (0.01)   |              |
| FSI-NoPlot*Post         | 0.522   | -0.169   | -0.177       |
|                         | (0.57)  | (-0.16)  | (-0.17)      |
| LAI-Plot*Post           | 0.556   | -0.135   | -0.144       |
|                         | (0.61)  | (-0.13)  | (-0.14)      |
| FSI-NoPlot-retire*Post  | 0.865   | 0.174    | 0.165        |
|                         | (0.95)  | (0.16)   | (0.16)       |
| LAI-NoPlot-retire*Post  | 0.661   | -0.030   | -0.039       |
|                         | (0.76)  | (-0.03)  | (-0.04)      |
| referencegroup          | Control | FSI-Plot | FSI-Plot-inf |
| consumerFE              | Y       | Y        | Y            |
| eventmonthFE            | Y       | Y        | Y            |
57
| N      | 78,450 | 78,450 | 78,450 |
| ------ | ------ | ------ | ------ |
| adj.R2 | 0.74   | 0.74   | 0.74   |

FIGUREB1
MonthlyLoginsbyTreatmentGroup(7Groups)
Panel(a)showstheestimatedcoefficientsinaregressionofmonthlylogincountoneventmonth
indicatorvariableswithconsumerfixedeffectsforeachtreatmentgroup.Panel(b)showsthe
averagepredictedvaluesforthatregression.DetailedregressionresultsareinTableA1.
(a) Coefficients
2
1
0
-1
-2
-3
-4
-5
tneiciffeoC
Start End
control
FSI-Plot
FSI-Plotinf
FSI-NoPlot
LAI-Plot
FSI-NoPlot-retire
LAI-NoPlot-retire
-5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Event month
(b) PredictedValues
18
17
16
15
14
13
12
11
snigoL
ylhtnoM
detciderP
Start End
control
FSI-Plot
FSI-Plotinf
FSI-NoPlot
LAI-Plot
FSI-NoPlot-retire
LAI-NoPlot-retire
-5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Event month
58

TABLEB3
TreatmentEffectsonDiscretionarySpending(7Groups)
Thedependentvariableinallcolumnsisthelogofmonthlydiscretionaryspending.Control,
FSI-Plot,FSI-Plot-inf,FSI-NoPlot,FSI-NoPlot-retire,LAI-Plot,andLAI-NoPlot-retireare
treatmentgroupindicatorvariables(seeTableB1fordetails).Thebaselineperiodinall
regressionsisthefivemonthsbeforetheexperimentlaunch(t=-5tot=-1).Intraisanindicator
variablefortheeightmonthsduringwhichexperimentmaterialswerepresentedintheapp(t=0to
t=7),andPost isanindicatorforthefollowingtwelvemonths(t=8tot=19).Reportedt-statistics
inparenthesesareheteroskedasticity-robustandclusteredattheconsumerlevel.Thesymbols
***,**,and*indicatestatisticalsignificanceatthe1%,5%,and10%levels,respectively.
| Variables               | (1)      | (2)      | (3)          |
| ----------------------- | -------- | -------- | ------------ |
| Control*Intra           |          | 0.156**  | 0.147**      |
|                         |          | (2.22)   | (2.25)       |
| FSI-Plot*Intra          | -0.156** |          | -0.009       |
|                         | (-2.22)  |          | (-0.13)      |
| FSI-Plot-inf*Intra      | -0.147** | 0.009    |              |
|                         | (-2.25)  | (0.13)   |              |
| FSI-NoPlot*Intra        | -0.012   | 0.144**  | 0.135**      |
|                         | (-0.18)  | (2.00)   | (2.01)       |
| LAI-Plot*Intra          | 0.009    | 0.165**  | 0.156**      |
|                         | (0.13)   | (2.24)   | (2.26)       |
| FSI-NoPlot-retire*Intra | -0.036   | 0.120**  | 0.111**      |
|                         | (-0.66)  | (1.99)   | (2.04)       |
| LAI-NoPlot-retire*Intra | 0.006    | 0.162**  | 0.154**      |
|                         | (0.09)   | (2.11)   | (2.12)       |
| Control*Post            |          | 0.092    | 0.073        |
|                         |          | (0.98)   | (0.77)       |
| FSI-Plot*Post           | -0.092   |          | -0.019       |
|                         | (-0.98)  |          | (-0.19)      |
| FSI-Plot-inf*Post       | -0.073   | 0.019    |              |
|                         | (-0.77)  | (0.19)   |              |
| FSI-NoPlot*Post         | -0.022   | 0.070    | 0.050        |
|                         | (-0.25)  | (0.73)   | (0.52)       |
| LAI-Plot*Post           | -0.035   | 0.057    | 0.038        |
|                         | (-0.37)  | (0.57)   | (0.37)       |
| FSI-NoPlot-retire*Post  | -0.026   | 0.066    | 0.047        |
|                         | (-0.34)  | (0.82)   | (0.58)       |
| LAI-NoPlot-retire*Post  | -0.034   | 0.057    | 0.038        |
|                         | (-0.38)  | (0.59)   | (0.39)       |
| referencegroup          | Control  | FSI-Plot | FSI-Plot-inf |
| consumerFE              | Y        | Y        | Y            |
| eventmonthFE            | Y        | Y        | Y            |
59
| N      | 78,450 | 78,450 | 78,450 |
| ------ | ------ | ------ | ------ |
| adj.R2 | 0.65   | 0.65   | 0.65   |

FIGUREB2
MonthlyDiscretionarySpendingbyTreatmentGroup(7Groups)
Thefigureshowstheestimatedcoefficientsinaregressionoflogmonthlydiscretionaryspending
oneventmonthindicatorvariableswithconsumerfixedeffectsforeachtreatmentgroup.Detailed
regressionresultsareinTableA2.
.3 .2
.1 0
-.1
-.2
-.3
tneiciffeoC
Start End
control
FSI-Plot
FSI-Plotinf
FSI-NoPlot
LAI-Plot
FSI-NoPlot-retire
LAI-NoPlot-retire
-5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Event month
60

TABLEB4
TreatmentEffectsonDiscretionarySpendingOverFourMonthsIntervals(7Groups)
Thedependentvariableinallcolumnsisthelogofmonthlydiscretionaryspending.FSI-Plot,
FSI-Plot-inf,FSI-NoPlot,FSI-NoPlot-retire,LAI-Plot,andLAI-NoPlot-retirearetreatmentgroup
indicatorvariables(seeTableB1fordetails).Thebaselineperiodinallregressionsisthefivemonths
beforetheexperimentlaunch(t=-5tot=-1)andthereferencegroupistheControl group.Treatment
groupindicatorsareinteractedwithatimeperiodindicatorforthefourmonthslistedatthetopofeach
column.Experimentmaterialswerepresentedontheappfromt = 0tot = 7.Reportedt-statisticsin
parenthesesareheteroskedasticity-robustandclusteredattheconsumerlevel.Thesymbols***,**,and
*indicatestatisticalsignificanceatthe1%,5%,and10%levels,respectively.
| Variables |     | (1) | (2) | (3) | (4) | (5) |
| --------- | --- | --- | --- | --- | --- | --- |
Interaction: I(0 ≤ t ≤ 3) I(4 ≤ t ≤ 7) I(8 ≤ t ≤ 11) I(12 ≤ t ≤ 15) I(16 ≤ t ≤ 19)
| FSI-Plot*I(a     | ≤ t ≤ b) | -0.140** | -0.172** | -0.153* | -0.141  | 0.018   |
| ---------------- | -------- | -------- | -------- | ------- | ------- | ------- |
|                  |          | (-2.02)  | (-1.97)  | (-1.69) | (-1.31) | (0.16)  |
| FSI-Plot-inf*I(a | ≤ t ≤ b) |          |          |         |         |         |
|                  |          | -0.128** | -0.166** | -0.157* | -0.136  | 0.074   |
|                  |          | (-2.03)  | (-2.00)  | (-1.70) | (-1.28) | (0.63)  |
| FSI-NoPlot*I(a   | ≤ t ≤ b) | -0.004   | -0.020   | -0.049  | -0.028  | 0.010   |
|                  |          | (-0.06)  | (-0.23)  | (-0.55) | (-0.28) | (0.09)  |
| LAI-Plot*I(a     | ≤ t ≤ b) | 0.007    | 0.011    | -0.057  | -0.012  | -0.036  |
|                  |          | (0.10)   | (0.13)   | (-0.63) | (-0.12) | (-0.30) |
FSI-NoPlot-retire*I(a ≤ t ≤ b) -0.048 -0.024 -0.067 -0.039 0.029
|     |     | (-0.88) | (-0.35) | (-0.91) | (-0.47) | (0.31) |
| --- | --- | ------- | ------- | ------- | ------- | ------ |
LAI-NoPlot-retire*I(a ≤ t ≤ b) 0.067 -0.054 -0.045 0.004 -0.063
|              |     | (0.98) | (-0.61) | (-0.52) | (0.04) | (-0.53) |
| ------------ | --- | ------ | ------- | ------- | ------ | ------- |
| consumerFE   |     | Y      | Y       | Y       | Y      | Y       |
| eventmonthFE |     | Y      | Y       | Y       | Y      | Y       |
| N            |     | 28,242 | 28,242  | 28,242  | 28,242 | 28,242  |
| adj.R2       |     | 0.73   | 0.70    | 0.68    | 0.64   | 0.60    |
61

TABLEB5
TreatmentEffectsonSpendingCategories(7Groups)
Thedependentvariablesincolumns(1)-(4)arethelogofmonthlyspendinginthecorresponding
category,andthelogofmonthlycashwithdrawalisincolumn(5).Thedependentvariablein
column(6)isthelogsumofthefivelargestspendingtransactionsforagivenconsumer-month.
FSI-Plot,FSI-Plot-inf,FSI-NoPlot,FSI-NoPlot-retire,LAI-Plot,andLAI-NoPlot-retireare
treatmentgroupindicatorvariables(seeTableB1fordetails).Thebaselineperiodinall
regressionsisthefivemonthsbeforetheexperimentlaunch(t=-5tot=-1)andthereferencegroup
istheControl group.Intraisanindicatorvariablefortheeightmonthsduringwhichexperiment
materialswerepresentedintheapp(t=0tot=7),andPost isanindicatorforthefollowingtwelve
months(t=8tot=19).Reportedt-statisticsinparenthesesareheteroskedasticity-robustand
clusteredattheconsumerlevel.Thesymbols***,**,and*indicatestatisticalsignificanceatthe
1%,5%,and10%levels,respectively.
| Variables | (1) | (2) | (3) | (4) | (5)  | (6)      |
| --------- | --- | --- | --- | --- | ---- | -------- |
|           |     |     |     |     | Cash | 5Largest |
Dependent: Restaurants Clothing Entertainment Travel Withdrawal Transactions
FSI-Plot*Intra -0.140** -0.219** -0.155** -0.222** -0.265** -0.127***
|     | (-1.96) | (-2.37) | (-2.23) | (-2.12) | (-2.23) | (-2.94) |
| --- | ------- | ------- | ------- | ------- | ------- | ------- |
FSI-Plot-inf*Intra -0.137** -0.184** -0.132** -0.257** -0.237** -0.141***
|                  | (-1.99) | (-2.07) | (-2.03) | (-2.45) | (-2.19) | (-3.92) |
| ---------------- | ------- | ------- | ------- | ------- | ------- | ------- |
| FSI-NoPlot*Intra | 0.052   | 0.010   | 0.014   | 0.015   | -0.009  | -0.037  |
|                  | (0.75)  | (0.10)  | (0.21)  | (0.14)  | (-0.07) | (-0.98) |
| LAI-Plot*Intra   | 0.020   | -0.004  | 0.002   | 0.082   | 0.007   | -0.038  |
|                  | (0.29)  | (-0.05) | (0.03)  | (0.74)  | (0.06)  | (-1.03) |
FSI-NoPlot-retire*Intra -0.005 -0.005 0.006 -0.005 -0.023 -0.002
|     | (-0.09) | (-0.08) | (0.09) | (-0.05) | (-0.20) | (-0.08) |
| --- | ------- | ------- | ------ | ------- | ------- | ------- |
LAI-NoPlot-retire*Intra 0.023 -0.041 -0.007 0.021 -0.025 -0.000
|                        | (0.33)  | (-0.47) | (-0.10) | (0.20)  | (-0.27) | (-0.01) |
| ---------------------- | ------- | ------- | ------- | ------- | ------- | ------- |
| FSI-Plot*Post          | 0.004   | 0.089   | -0.018  | 0.035   | 0.006   | -0.042  |
|                        | (0.05)  | (0.81)  | (-0.20) | (0.27)  | (0.04)  | (-0.88) |
| FSI-Plot-inf*Post      | 0.008   | 0.030   | 0.023   | -0.017  | 0.021   | 0.000   |
|                        | (0.09)  | (0.29)  | (0.28)  | (-0.13) | (0.15)  | (0.00)  |
| FSI-NoPlot*Post        | -0.021  | -0.010  | 0.016   | 0.027   | -0.030  | -0.011  |
|                        | (-0.23) | (-0.09) | (0.18)  | (0.21)  | (-0.21) | (-0.25) |
| LAI-Plot*Post          | -0.037  | -0.041  | -0.048  | 0.011   | 0.025   | 0.033   |
|                        | (-0.40) | (-0.39) | (-0.56) | (0.08)  | (0.17)  | (0.71)  |
| FSI-NoPlot-retire*Post | 0.021   | 0.066   | 0.002   | 0.018   | 0.003   | 0.021   |
|                        | (0.29)  | (0.79)  | (0.02)  | (0.14)  | (0.02)  | (0.52)  |
LAI-NoPlot-retire*Post -0.017 0.011 -0.009 -0.014 0.013 0.017
|              | (-0.19) | (0.11) | (-0.11) | (-0.11) | (0.11) | (0.40) |
| ------------ | ------- | ------ | ------- | ------- | ------ | ------ |
| consumerFE   | Y       | Y      | Y       | Y       | Y      | Y      |
| eventmonthFE | Y       | Y      | Y       | Y       | Y      | Y      |
62
| N      | 78,450 | 78,450 | 78,450 | 78,450 | 78,450 | 78,450 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| adj.R2 | 0.71   | 0.50   | 0.57   | 0.48   | 0.49   | 0.49   |

TABLEB6
TreatmentEffectsonAdditionalSpendingCategories(7Groups)
Thedependentvariablesarethelogofmonthlytotalspendingincolumn(1)andlogmonthly
spendinginthecorrespondingcategoryincolumns(2)-(5).FSI-Plot,FSI-Plot-inf,FSI-NoPlot,
andLAI-Plot aretreatmentgroupindicatorvariables(seeTableB1fordetails).Thebaseline
periodinallregressionsisthefivemonthsbeforetheexperimentlaunch(t=-5tot=-1)andthe
referencegroupistheControl group.Intraisanindicatorvariablefortheeightmonthsduring
whichexperimentmaterialswerepresentedintheapp(t=0tot=7),andPost isanindicatorforthe
followingtwelvemonths(t=8tot=19).Reportedt-statisticsinparenthesesare
heteroskedasticity-robustandclusteredattheconsumerlevel.Thesymbols***,**,and*
indicatestatisticalsignificanceatthe1%,5%,and10%levels,respectively.
| Variables               | (1)      | (2)    | (3)       | (4)       | (5)       |
| ----------------------- | -------- | ------ | --------- | --------- | --------- |
| Dependent:              | Spending | Gas    | Groceries | Telephone | Utilities |
| FSI-Plot*Intra          | -0.065*  | 0.026  | 0.010     | -0.046    | -0.086    |
|                         | (-1.95)  | (0.39) | (0.15)    | (-0.65)   | (-0.95)   |
| FSI-Plot-inf*Intra      | -0.053*  | 0.090  | 0.069     | -0.001    | -0.080    |
|                         | (-1.74)  | (1.24) | (1.00)    | (-0.01)   | (-0.91)   |
| FSI-NoPlot*Intra        | 0.007    | 0.008  | 0.024     | 0.007     | -0.107    |
|                         | (0.22)   | (0.14) | (0.35)    | (0.09)    | (-1.22)   |
| LAI-Plot*Intra          | 0.006    | 0.093  | 0.025     | -0.030    | -0.021    |
|                         | (0.19)   | (1.43) | (0.37)    | (-0.41)   | (-0.22)   |
| FSI-NoPlot-retire*Intra | -0.001   | 0.033  | 0.024     | -0.047    | 0.002     |
|                         | (-0.02)  | (0.64) | (0.37)    | (-0.65)   | (0.03)    |
| LAI-NoPlot-retire*Intra | 0.001    | 0.100  | 0.076     | -0.000    | 0.015     |
|                         | (0.04)   | (1.53) | (1.11)    | (-0.00)   | (0.17)    |
FSI-Plot*Post
|                        | -0.003  | -0.024   | -0.041  | -0.012  | -0.126  |
| ---------------------- | ------- | -------- | ------- | ------- | ------- |
|                        | (-0.06) | (-0.31)  | (-0.42) | (-0.14) | (-1.06) |
| FSI-Plot-inf*Post      | -0.012  | 0.010    | 0.063   | 0.051   | -0.073  |
|                        | (-0.30) | (0.11)   | (0.65)  | (0.58)  | (-0.66) |
| FSI-NoPlot*Post        | 0.021   | 0.023    | -0.005  | 0.071   | -0.162  |
|                        | (0.52)  | (0.34)   | (-0.06) | (0.82)  | (-1.46) |
| LAI-Plot*Post          | 0.017   | -0.098   | 0.013   | -0.082  | -0.167  |
|                        | (0.40)  | (-1.25)  | (0.14)  | (-0.95) | (-1.44) |
| FSI-NoPlot-retire*Post | -0.018  | -0.001   | 0.057   | 0.024   | 0.042   |
|                        | (-0.45) | (-0.02)  | (0.63)  | (0.31)  | (0.36)  |
| LAI-NoPlot-retire*Post | -0.005  | -0.027   | 0.044   | 0.034   | 0.012   |
|                        | (-0.12) | (-0.33)  | (0.48)  | (0.39)  | (0.10)  |
| consumerFE             | Y       | Y        | Y       | Y       | Y       |
| eventmonthFE           | Y       | Y        | Y       | Y       | Y       |
| N                      | 78,450  | 5613,375 | 62,350  | 49,675  | 48,150  |
| adj.R2                 | 0.61    | 0.37     | 0.42    | 0.27    | 0.24    |

TABLEB7
BalanceTests
| VariablesaredefinedinTable |     | 3.  |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PanelA.
| Treatment |     |      | Age | NetWorth |     | PersonalizedIndex |     | Logins |     |
| --------- | --- | ---- | --- | -------- | --- | ----------------- | --- | ------ | --- |
|           | N   | mean | sd  | mean     | sd  | mean              | sd  | mean   | sd  |
Control 458 44.48 7.78 1,146,247 1,583,688 3,274 5,562 15.25 17.52
FSI-Plot 422 44.4 7.93 1,184,688 1,645,099 3,310 4,854 15.29 22.21
FSI-Plot-inf 450 44.23 7.96 1,086,211 1,357,686 2,953 4,791 14.98 21.03
FSI-NoPlot 434 44.67 7.77 1,114,032 1,391,693 2,990 4,603 14.97 20.20
LAI-Plot 426 44.78 7.9 1,126,652 1,600,438 3,367 6,766 15.69 19.15
FSI-NoPlot-retire 477 44.48 7.91 1,097,916 1,302,980 3,037 4,713 15.98 21.60
LAI-NoPlot-retire 471 44.84 8.08 1,144,653 1,563,826 3,328 4,940 15.78 21.27
PanelB.
| Treatment |     | Income |        | Spending |        | DiscretionarySpending |       | Clothing |     |
| --------- | --- | ------ | ------ | -------- | ------ | --------------------- | ----- | -------- | --- |
|           | N   | mean   | sd     | mean     | sd     | mean                  | sd    | mean     | sd  |
| Control   | 458 | 16,863 | 12,683 | 12,323   | 9,826  | 3,610                 | 3,290 | 371      | 492 |
| FSI-Plot  | 422 | 16,721 | 13,405 | 12,748   | 10,396 | 3,694                 | 3,547 | 406      | 577 |
FSI-Plot-inf 450 16,446 12,753 12,459 10,062 3,836 3,709 384 552
FSI-NoPlot 434 16,692 13,110 12,047 9,841 3,669 3,549 370 484
| LAI-Plot | 426 | 17,284 | 13,525 | 12,678 | 10,434 | 3,621 | 3,206 | 369 | 467 |
| -------- | --- | ------ | ------ | ------ | ------ | ----- | ----- | --- | --- |
FSI-NoPlot-retire 477 16,972 13,370 12,022 8,656 3,690 3,168 362 396
LAI-NoPlot-retire 471 16,531 13,355 12,323 9,971 3,701 3,654 359 485
PanelC.
| Treatment         |     | Entertainment |     | Restaurants |     |      | Travel | CashWithdrawal |       |
| ----------------- | --- | ------------- | --- | ----------- | --- | ---- | ------ | -------------- | ----- |
|                   | N   | mean          | sd  | mean        | sd  | mean | sd     | mean           | sd    |
| Control           | 458 | 170           | 224 | 508         | 494 | 667  | 1,050  | 913            | 1,281 |
| FSI-Plot          | 422 | 172           | 238 | 531         | 547 | 677  | 1,038  | 946            | 1,458 |
| FSI-Plot-inf      | 450 | 177           | 213 | 495         | 450 | 742  | 1,123  | 969            | 1,292 |
| FSI-NoPlot        | 434 | 163           | 201 | 499         | 434 | 686  | 1,014  | 934            | 1,331 |
| LAI-Plot          | 426 | 168           | 225 | 509         | 460 | 749  | 1,156  | 942            | 1,320 |
| FSI-NoPlot-retire | 477 | 163           | 197 | 490         | 445 | 682  | 830    | 903            | 1,344 |
| LAI-NoPlot-retire | 471 | 161           | 224 | 499         | 525 | 656  | 1,018  | 871            | 1,264 |
64

C. Experiment Material
65

FIGUREC1
FullDashboardPagefortheControlGroup
Thisdashboardpagewaspresentedtoalltreatmentgroupsbeforetheexperimentlaunch(t < 0)
andaftertheremovaloftheexperimentmaterialfromtheapp(t > 7).
66

FIGUREC2
FullDashboardPagefortheFSI-PlotTreatment
67

FIGUREC3
TopoftheDashboardPagefortheFSI-PlotTreatment
68

FIGUREC4
TopoftheDashboardPagefortheFSI-NoPlotTreatment
69

FIGUREC5
TopoftheDashboardPagefortheLAI-PlotTreatment
70

FIGUREC6
TopoftheDashboardPagefortheFSI-NoPlot-retireTreatment
71

FIGUREC7
TopoftheDashboardPagefortheLAI-NoPlot-retireTreatment
72

FIGUREC8
FAQpagefortheFSI-PlotTreatment(part1)
73

FIGUREC9
FAQpagefortheFSI-PlotTreatment(part2)
74