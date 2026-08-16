---
conversion_metadata:
  converted_at: "2026-07-22T13:03:10Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "D'Acunto & Rossi.pdf"
  source_pdf_sha256: "85029ab7cb1dc5665eb5e7a6b44d565e838add572f1a76f63bce6d242344c4f5"
  page_count: 21
  markdown_char_count: 157734
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Annual Review of Financial Economics
Robo-Advice: Transforming
Households into Rational
Economic Agents

Francesco D’Acunto and Alberto G. Rossi

Department of Finance, McDonough School of Business, Georgetown University, Washington,
DC, USA; email: francesco.dacunto@georgetown.edu, agr60@georgetown.edu

Annu. Rev. Financ. Econ. 2023. 15:543–63

Keywords

First published as a Review in Advance on
August 24, 2023

The Annual Review of Financial Economics is online at
financial.annualreviews.org

https://doi.org/10.1146/annurev-financial-110921-
013217

Copyright © 2023 by the author(s). This work is
licensed under a Creative Commons Attribution 4.0
International License, which permits unrestricted
use, distribution, and reproduction in any medium,
provided the original author and source are credited.
See credit lines of images or other third-party
material in this article for license information.

JEL codes: D14, D91, G51, G53, O31

FinTech, household finance, behavioral finance, consumption, debt,
investments

Abstract

Robo-advice uses big and open data to provide consumers with fully in-
formed and rational-expectation benchmarks in all realms of household
finance, including consumption, saving, investment, and debt management
choices. It also minimizes the monetary, cognitive, and psychological costs
that households face in economic transactions. We review recent research on
the features and effects of robo-advice on individual and aggregate economic
outcomes through the lens of its differences from traditional human advice.
We discuss the distributional implications of robo-advice, its potential role
in increasing the effectiveness of economic policies, the role of providers’
incentives, and several questions that are still wide open for researchers in
finance, economics, social psychology, and related fields.

543

---

<!-- PAGE 2 -->

1. HOUSEHOLD FINANCE PUZZLES AND ISSUES
WITH TRADITIONAL SOLUTIONS

Every household around the world, irrespective of its level of income, wealth, or sophistication,
needs to make complex financial decisions on a daily basis. First and foremost, households need to
decide how much they want to spend for consumption or save to increase future consumption—
they need to solve an intertemporal consumption problem. Once the consumption–saving choice
is made, they need to allocate resources to durable and nondurable goods and choose how to fi-
nance their durable consumption (e.g., income flows, credit card debt, mortgages, personal loans,
student loans). Financing options differ based on multiple dimensions that need to be compared—
horizons, maturities, interest rates, and amortization plans. Households also need to manage their
assets by deciding how to invest savings to accumulate wealth and maximize future consumption
and/or bequests. On top of allocating resources across investment assets in their financial port-
folios, for instance, they must choose whether and how much to contribute to retirement saving
plans—a decision that has become prominent around the world given the global move away from
defined benefit pension systems and toward defined contribution individual plans. And, once they
reach retirement age, they need to make decisions about the decumulation phase of their accumu-
lated retirement savings, which is a complex problem that is still barely understood by researchers
and policymakers.

Ultimately, households, like corporate managers, need to make multiple financial decisions at
high frequency and cannot avoid choosing, in the sense that avoiding to decide is a choice in itself
that has relevant financial implications for the household (Madrian & Shea 2001). Contrary to
corporate managers, though, households cannot specialize in only one type of the multitude of
financial choices they need to make. Moreover, households need to make all these choices, even
though the vast majority have never been exposed to the most basic principles of finance, such as
diversification and compounding of interest rates, or obtained any financial education (Lusardi &
Mitchell 2014), because finance is absent from standard primary and secondary school curricula
in virtually every country around the world.

Given these premises, the fact that most households make decisions that depart from those
predicted by standard economic models should not be surprising. Standard models assume
the existence of utility-maximizing agents who have access to all the information needed to
make financial decisions, use it to form rational expectations, and have standard economic pref-
erences. A large and growing literature in finance and economics labels departures from standard
models in households’ financial choices as household finance puzzles (Zinman 2015).

Why do we care to understand and solve household finance puzzles? On top of negatively
affecting households’ utility, these puzzles have four important and undesirable aggregate effects.
First, they tend to produce and widen wealth inequalities because the poorer and most vulnerable
households tend to be less sophisticated in terms of economic and financial literacy and hence
make choices that depart most from optimality (Calvet, Campbell & Sodini 2007, 2009). Second,
they dampen the effects of economic policies that central banks and governments implement,
assuming that households understand and react to them in line with the predictions of standard
economic models (D’Acunto et al. 2021a). Third, household finance puzzles are likely to have
become even more severe over time due to the swift diffusion of FinTech applications that have
eased ordinary consumers’ access to high-risk financial choices, such as the trading of complex
financial products like derivatives and cryptocurrencies using apps on their personal devices or
the accumulation of high-interest debt through unsecured financing of consumption expenses
and buy now, pay later spending opportunities. Fourth, a detailed understanding of the nature and
consequences of the biases households face when making financial choices is crucial to inform

544

D’Acunto (cid:129) Rossi

---

<!-- PAGE 3 -->

regulators’ attempts to design effective policies that can protect households from being exploited
by better-informed financial institutions and other counterparts in financial contracts.

Two traditional solutions have been proposed for household finance puzzles. The first solu-
tion is the provision of financial advice. Financial advisors are agents who suggest how households
should make their multiple financial choices by interpreting their preferences and beliefs and eval-
uating options. Unfortunately, though, financial advisors have limitations. Their services are too
expensive for many households and cannot be scaled at a low cost, which reduces their viability, es-
pecially for middle- and low-income households. If anything, the availability of financial advisors
might increase rather than reduce wealth inequalities, given that more affluent households can ac-
cess them but poorer households cannot. Moreover, financial advisors, similar to other experts such
as CEOs and institutional investors, often engage in the same departures from rational decision-
making that households display and end up providing unsound suggestions (Mullainathan, Noeth
& Schoar 2012; Linnainmaa, Melzer & Previtero 2021). At the same time, the literature has doc-
umented the unintended consequences of limiting the presence of financial advisors on access to
financial investments by unsophisticated households. For instance, Linnainmaa et al. (2022) find
that once financial advisors’ regulatory oversight was introduced in Canada, the number of finan-
cial advisors reduced drastically and so did households’ stock market participation, especially by
middle-class households. The second solution is the design of nudges—default choices for pro-
gram participation or design mechanisms that lure households into making choices consistent
with those that a representative economic agent would make under the same conditions (Thaler
& Sunstein 2009). Although helpful, by construction, nudges can barely be tailored to the individ-
ual characteristics of each household, and their effectiveness often depends on the details of their
design (Sunstein 2017).

Next to human financial advice and nudges, robo-advice represents a third and more recent
solution to household finance puzzles (D’Acunto & Rossi 2021). At first, robo-advice might appear
as nothing more than traditional human financial advice produced and delivered automatically to
decision-makers with FinTech applications through personal devices. Even if this were the only
relevant feature of robo-advice, it would make it more scalable than human advice by reducing
its cost and allowing access to advice to a substantially higher share of households. This property
would thus improve the distributional consequences of advice by aligning the choices of vulnerable
households with those of sophisticated households (Philippon 2019).

Robo-advice, though, is not just traditional advice produced and delivered automatically
through personal devices. The crucial feature of robo-advice is that it reduces households’ dif-
ferences from the characteristics of standard neoclassical rational decision-makers and hence
allows households, including the least sophisticated, to make choices closer to those a standard
utility-maximizing agent would make.

Robo-advising transforms biased decision-makers into standard neoclassical decision-makers
through three unique features that differentiate it from traditional forms of advice. First, robo-
advising uses big and open data to make households fully informed about their own characteristics
and past behavior as well as the characteristics and past behavior of other agents, to which house-
holds (and often their human advisors) would otherwise have no access due to their limited ability
to recall past actions and collect and elaborate big datasets (D’Acunto & Rossi 2022a). The big
data that robo-advisors access are the universe of transactions households produce when making
economic decisions, such as purchases of durable and nondurable goods, investment choices, and
financing choices. Robo-advisors can access this wealth of information because, since the Digital
Revolution, electronic transactions can be stored, and these data are open; that is, households can
share them by linking transaction accounts to robo-advising applications.

www.annualreviews.org (cid:129) Robo-Advice

545

---

<!-- PAGE 4 -->

Second, robo-advising manages households’ beliefs and pushes them closer to the rational
expectations assumed in standard models. The economic literature has documented several sys-
tematic departures of households’ beliefs from those of a standard economic agent. The size of
these departures is correlated with demographic characteristics and varies over the business cycle.
As we discuss in Section 3.1, robo-advisors provide households with beliefs about both their own
future financial conditions and aggregate macroeconomic conditions that are closer to those of a
standard agent.

Third, robo-advising reduces the transaction costs of executing economic choices, which in-
clude not only monetary costs but also the cognitive and psychological costs that households face
when trying to make economic decisions.

In the rest of this review, we describe the findings of existing academic research on these three
defining features of robo-advice. We also emphasize the large set of open questions and areas of
investigation for future research.

2. REDUCING INFORMATION FRICTIONS

Standard neoclassical economic agents are assumed to be fully informed about their character-
istics, the characteristics of other agents, and macroeconomic conditions. This assumption of
standard models of intertemporal consumption optimization is heavily violated in the data, ex-
cept for a few special cases, such as highly sophisticated institutional investors in financial markets
who actively engage in costly information acquisition (Gargano, Rossi & Wermers 2017).

Most households are barely informed about macroeconomic conditions and often even ignore
the definition of basic economic aggregates, such as inflation rates or interest rates (Binder 2017).
Households have also been shown, on average, to have a wrong assessment of the economic con-
ditions of other economic agents, which is due mainly to a lack of full information about other
people’s income flows, spending, and debt positions and the observation of conspicuous and salient
transactions that households interpret as representative of the average transactions others execute
(Charles, Hurst & Roussanov 2009). Ultimately, and perhaps most surprisingly, households often
cannot recall or process information about their own income flows, consumption, and debt trans-
actions, even though all this information is produced by them and hence available to them without
the need to collect public or private signals from other sources. For example, households do not
keep information about all their transactions but often pay attention to them only temporarily and
for short periods (D’Acunto, Rossi & Weber 2019). Households also tend to have a biased recall of
their consumption over time, which is driven by their tendency to recall having paid lower prices
than the actual prices they faced (D’Acunto & Weber 2022).

The first unique feature of robo-advice is pushing households closer to being fully informed
about their own, others’, and aggregate economic outcomes. Robo-advice can achieve this goal
by collecting and elaborating big and open transaction-level data at various levels of observation:
households’ own characteristics and past choices, the characteristics and past choices of other
decision-makers in the economy, and information about macroeconomic conditions and other
aggregate variables that might be relevant to economic decision-making. In the rest of this section,
we discuss recent research that has studied the mechanics and effects of this function of robo-
advising.

2.1. Information About One’s Own Characteristics: Income Aggregators

The fact that providing information about one’s own characteristics and past choices influences
decision-making might appear surprising at first. After all, this information is produced by house-
holds and should therefore be readily available to them at any time. And yet research finds

546

D’Acunto (cid:129) Rossi

---

<!-- PAGE 5 -->

that households largely neglect essential information about their own behavior due to cognitive
constraints in the ability to collect and process information (D’Acunto, Ghosh & Rossi 2022).

Robo-advice allows households to overcome these constraints and obtain full information
about their past transactions and finances through income aggregators. Income aggregators are
robo-advisors that collect and elaborate households’ transaction-level data. These data are open
in that households can share them by linking their spending and other financial accounts to the
aggregator (Gelman et al. 2014).

Upon obtaining household-level transactions, income aggregators construct household-level
balance sheets similar to those that corporations use for financial reporting (D’Acunto & Rossi
2022b). Aggregators elaborate both static balance sheets, which include the current overall value
of households’ assets and liabilities at each point in time, and dynamic assessments of the past
evolution, liquidity, and horizons of households’ debts, spending, and investment decisions for
each entry of the balance sheet (Baker 2018).

Because not linking all financial accounts would render the aggregator’s information elabora-
tion incomplete, households that want to access this feature of robo-advising have an incentive
to link all their financial accounts to the aggregator. Consistently, Baker (2018) shows that 95%
of the users of a large US income aggregator linked all their checking accounts, over 93% linked
all their savings accounts, and 91% linked all their credit card accounts. At the same time, house-
holds might be wary of providing so much detailed information to an income aggregator. Income
aggregators have a short history of operations and hence lack reputation in terms of data protec-
tion and management, which might increase households’ expected probability that the data might
be appropriated by third parties and be subject to cybersecurity concerns. Consistent with these
potential concerns, Rossi & Utkus (2020a) find that a robo-advisor’s reputation is one of the main
drivers of robo-advice adoption, partly because of users’ data privacy concerns (Tang 2019).

Income aggregation can be a form of robo-advice if providing households with information
about their own characteristics and past choices influences their decision-making. Consistent with
this possibility, Olafsson & Pagel (2018) show that displaying aggregate information about one’s
own balance sheets to Icelandic households leads to financial choices that are closer to those of a
standard economic agent. For instance, households reduce their debt balances to avoid overdraft
fees, which is direct evidence that, before the information was provided to them, households were
unaware of the existence or size of overdraft fees. Information from income aggregators also makes
households realize that the benefits of running higher-than-limit debt balances are lower than the
monetary costs of the overdraft fees they are charged. Carlin, Olafsson & Pagel (2023) further
document that, after observing their own aggregate balance sheets, households reduce their non-
durable spending, especially in frivolous categories such as eating outside the home and traveling.
This reaction suggests that, absent the information income aggregators provide, households might
underestimate the share of total spending and income flows they allocate across consumption cat-
egories. Further evidence of the effects of giving consumers aggregated information about their
own finances through income aggregating robo-advisors is provided by Levi & Benartzi (2020)
and Olafsson & Pagel (2022). The latter paper also provides a direct empirical test of the os-
trich effect, whereby decision-makers select the information to which they want to attend in their
daily lives based on their beliefs about the positivity or negativity of such information (Karlsson,
Loewenstein & Seppi 2009).

In addition to the mere informational value of income aggregation, robo-advisors use the elab-
orated information to focus households’ attention on specific features of their balance sheets,
especially when such features indicate red flags, such as significant increases in spending pat-
terns over time despite constant or declining income flows. Lee (2019) studies a Canadian
robo-advisor that, on top of income aggregation features, sends users overspending messages when

www.annualreviews.org (cid:129) Robo-Advice

547

---

<!-- PAGE 6 -->

their spending in one category is substantially higher than the user’s recent spending within the
same category. Note that increasing spending in times of constant or declining income flows is not
necessarily inconsistent with intertemporal consumption optimization if, for example, households
correctly expect higher income growth—a feature that existing robo-advisors cannot observe or
include in their assessment of red flags in households’ balance sheets. Recent research, though,
documents substantial extrapolation in households’ expectations of future income after small in-
come increases, which leads to a systematic overestimation of future income levels and growth
relative to ex post realized levels and growth (D’Acunto, Weber & Yin 2022).

Lee (2019) compares users who are just above the robo-advisor’s threshold to send over-
spending messages with users who are just below and hence spend similarly more than in their
recent past but receive no messages. He finds that message receivers cut their daily spending by
approximately 5% more, and this effect, despite reverting in terms of spending flows, is permanent
in terms of cumulative spending over time; that is, the temporary shock does not fully revert over
time. Lee (2019) also finds that older, wealthier, and more financially savvy households react more
to obtaining information about their own transactions. Although this heterogeneity might at least
in part capture higher income growth expected by younger households going forward, it also
opens the possibility that this form of robo-advising might increase wealth inequalities over time.
Finally, Lee (2019) finds that, despite reacting to overspending messages by reducing spending,
several households also reduce the frequency with which they log in and check information about
their finances on the income aggregator. This form of the ostrich effect, whereby households tend
to avoid facing negative news about their finances, is a feature of robo-advising income aggregators
documented first by Olafsson & Pagel (2022).

The detection of an ostrich effect associated with using informative robo-advisors opens a set
of research questions. First, we do not know whether providing households with complete and ag-
gregated information about their finances has effects in the long term or whether the ostrich effect
(or fatigue from using an application regularly and for long periods) makes the effects only tem-
porary. By construction, because income aggregators have been implemented and commercialized
over only the last few years, researchers lack data for repeated interventions over prolonged pe-
riods, which would be crucial to answering this question. We also need to understand whether
the emergence of an ostrich effect makes robo-advisors that provide information such as in-
come aggregators increase inequalities. This unintended and undesirable consequence could be
plausible if detachment from robo-advisors were more common among vulnerable households.
Extensive literature in behavioral economics has also documented the prevalence of present bias
in choices and new toy effects, which are more substantial for demographic groups who tend
to understand their own finances less and make suboptimal consumption and saving choices in-
tertemporally (see, for example, Gargano & Rossi 2020). Understanding whether these common
behavioral features reduce the reliance on income aggregators over time for households that would
need them most and increase rather than reduce wealth inequalities is an open area for future
research.

2.2. Information About Other Economic Agents

Even if households were fully informed about their balance sheets, solving their intertemporal
consumption problem and hence determining their optimal consumption and saving rates would
be a daunting task for most households and depend largely on their preferences and subjective
beliefs, which can hardly even be expressed fully and entirely to a financial advisor by nonex-
pert economic agents (Bruine de Bruin et al. 2012). To facilitate this task, a strand of research in
economics, social psychology, and social finance shows that households make inferences about

548

D’Acunto (cid:129) Rossi

---

<!-- PAGE 7 -->

their own optimal consumption and saving rates based on the consumption and saving rates of
their peers, that is, individuals who have similar demographic characteristics and hence presum-
ably similar preferences, income flows, and expected income growth (for recent reviews of this
area of research, see Hirshleifer 2020 and Kuchler & Stroebel 2021).

Intuitively, making inferences based on signals about the behavior of a large mass of peers
could be meaningful based on the wisdom of the crowds, whereby a large number of independent
forecasts made by different individuals can provide an accurate consensus forecast, with which the
household can align their behavior (Da & Huang 2020). At the same time, households cannot ac-
cess the full set of transactions and full information about the choices their peers make in terms of
consumption, saving, investment, and financing: They cannot access or observe transaction-level
data about peers in the same way they access their own data. Instead, households are limited to
observing the information their peers disclose, and this information tends to not be representative
of peers’ finances, especially in times of pervasive use of social media (Han, Hirshleifer & Walden
2019). Peers tend to disclose their most conspicuous consumption instances in which they engage
(Charles, Hurst & Roussanov 2009) while not disclosing information about parsimonious con-
sumption choices, their income flows, or access to debt financing. In this way, the signals about
peers’ consumption that households observe lead them to overestimate the overall consumption
rates of peers unless households are sophisticated enough to account for peers’ partial disclosure
(Han, Hirshleifer & Walden 2019).

Contrary to households or human advisors, robo-advisors can access and elaborate information
about peers’ consumption and saving rates. If households misestimate these variables systemati-
cally, they should change their consumption choices when robo-advisors provide them with full
information about peers’ finances. D’Acunto, Rossi & Weber (2019) study a US robo-advisor
that, on top of the standard income aggregation features discussed in Section 2.1, provides users
with elaborated information about peers’ consumption, saving, and investment transactions. In
this context, peers are not users’ social acquaintances: The information is based on transaction
accounts of households that have similar demographics as users, including income levels, age,
residence types, and locations. D’Acunto, Rossi & Weber (2019) find that users’ spending levels
converge with those of peers for both users who spent more than and those who spent less than
their peers. The effects are asymmetric: Overspenders cut their spending substantially more than
underspenders over the following 12 months. This observational evidence raises the concern that
only the users who are especially interested in information about peers might select into adopting
robo-advice. To tackle this concern, D’Acunto, Rossi & Weber (2019) run a randomized control
trial with a representative US population that did not select into any robo-advice applications and
find the same reactions to the provision of information about peers.

Understanding the channels through which providing detailed information about others with
robo-advising changes households’ preferences, beliefs, and choices is an open research area. Re-
search has shown that information about debt financing options and investment decisions does
transmit across peers (Maturana & Nickerson 2019, Kalda 2020, Ouimet & Tate 2020), but
whether such information affects behavior because of its content or due to social pressure or social
conditioning (Bursztyn, Ederer & Yuchtman 2014; Bailey et al. 2019)—and hence has the same
effects when delivered through robo-advising after being gathered from the crowds rather than
one’s personal acquaintances—is an open question.

Moreover, we have no conclusive evidence about whether adapting one’s behavior to the av-
erage behavior of those with similar demographic characteristics is optimal. The principle of the
wisdom of the crowd requires that the assessments and hence choices of a large group of agents
are independent from each other to provide accurate average assessments. Still, in times of social
media where households observe the same signals from focal network members or influencers and

www.annualreviews.org (cid:129) Robo-Advice

549

---

<!-- PAGE 8 -->

might read the same comments and interpretations about business cycle shocks circulating in their
social network, average signals might not be unbiased.

To the extent that a social planner would care more about avoiding overconsumption by some
households (and the potential excessive use of debt financing) than about underconsumption by
other households, the asymmetric effects documented by D’Acunto, Rossi & Weber (2021) sug-
gest that robo-advising for spending using information about others could align with the aims
of policymakers. However, the distributional consequences of this form of robo-advising are still
unknown and should be investigated further.

2.3. Information About Macroeconomic Variables

In standard intertemporal consumption optimization models, beliefs about future macroeconomic
conditions, especially inflation, drive perceptions of real interest rates and hence the decision about
how much to consume versus save for the scope of future consumption (Bernanke 2009). Research
in macroeconomics, applied microeconomics, and social psychology has shown that many house-
holds are uninformed about the most basic macroeconomic aggregates (Coibion et al. 2020) and
form biased beliefs about them (Armantier et al. 2015; D’Acunto, Malmendier & Weber 2021;
Weber et al. 2022). Furthermore, households’ beliefs are not based on representative informa-
tion but rather on the few signals about prices and wages households observe in their daily lives
(D’Acunto, Ghosh & Rossi 2022). Cognitive abilities also determine households’ understand-
ing of the relationships across economic variables and their ability to elaborate macroeconomic
information (D’Acunto et al. 2021a, Andre et al. 2022).

Robo-advice to provide households with unbiased processed information should thus natu-
rally extend to macroeconomic variables, especially inflation and unemployment, whose expected
values determine households’ perceived real rates and expected income flows in standard mod-
els. Because systematic biases and mistakes in economic expectations are more frequent among
the most vulnerable households, they can contribute to the widening of inequalities (D’Acunto
et al. 2020). And yet research on the provision and effects of macroeconomic information through
robo-advisors is extremely scarce (D’Acunto & Rossi 2022b).

Robo-advice that provides unbiased macroeconomic information could also help solve the re-
cent debate on the effectiveness of policies that aim to manage households’ expectations through
communication (Coibion, Gorodnichenko & Kamdar 2018). Communication as an expectations-
management tool is more effective when households trust the policymaking body (D’Acunto,
Fuster & Weber 2021) and policies are simple and intuitive (D’Acunto et al. 2021b), but it is less
effective when delivered through traditional media such as newspapers, which households barely
trust (Coibion, Gorodnichenko & Weber 2022). Robo-advising to deliver unbiased information
about current macroeconomic variables and consensus forecasts about future realizations of the
same variables could be an effective way to increase policymakers’ success in managing expecta-
tions and choices. This is not only a widely open area of inquiry but also one that could deliver
important practical suggestions that can be implemented for policy design.

3. REDUCING DISTORTED BELIEFS

Standard neoclassical decision-makers are also assumed to form expectations rationally; their be-
liefs about future own and aggregate outcomes are, on average, consistent with ex post realizations.
Contrary to this benchmark, households tend to display multiple biases regarding beliefs about
their own, others’, and macroeconomic outcomes.

550

D’Acunto (cid:129) Rossi

---

<!-- PAGE 9 -->

In terms of their own outcomes, for instance, households tend to misestimate their sur-
vival probabilities, which leads them to make suboptimal choices about retirement savings and
insurance policies (Heimer, Myrseth & Schoenle 2019). Moreover, many households have system-
atically distorted beliefs about their future income flows and income growth: They extrapolate
from recent income increases but not decreases and overestimate future income systematically
(see, e.g., Cutler, Poterba & Summers 1990; De Long et al. 1990; Greenwood & Shleifer 2014;
Barberis et al. 2015; Gennaioli, Ma & Shleifer 2016; Barberis et al. 2018; Carroll et al. 2020;
D’Acunto, Weber & Yin 2022). At the same time, more than one-third of a representative popu-
lation overestimates the likelihood of negative shocks and the need for precautionary savings and
underspending relative to their capacity—a perceived precautionary savings motive that drops
when households receive insurance in the form of a credit line (D’Acunto et al. 2020).

Households display biased beliefs also when forming expectations about others—they tend
to overestimate others’ consumption and underestimate their saving rates, as discussed above
(D’Acunto, Rossi & Weber 2019)—and future macroeconomic variables. These systematic distor-
tions are correlated with demographic characteristics such as socioeconomic status (Das, Kuhnen
& Nagel 2020), cognitive abilities (D’Acunto et al. 2019), age, and cohorts (Malmendier & Nagel
2016). Stango & Zinman (2023) provide a taxonomy of multiple biases in households’ expectations
and beliefs and document commonalities and correlation patterns across them, which suggests that
many biases in beliefs might have common sources. Ultimately, beliefs appear to be more biased
for vulnerable households, which might help perpetuate economic inequalities.

3.1. Beliefs About One’s Own Characteristics

Research in economics and social psychology, based primarily on laboratory experiments, has tack-
led the issue of reducing distortions in households’ beliefs about their own future characteristics
by using goal setting—the process of letting households think about future potential states of the
world, the likelihood of such states absent any interventions, and the commitment to increase the
likelihood of the desired state of the world by establishing it as a goal. In the field, Ashraf, Karlan
& Yin (2006) show that individuals with preferences that display a higher degree of hyperbolic
discounting have a higher probability of opening savings accounts that restrict access to saving
goals until the amount saved achieves a certain threshold. The authors show that adopting hard
goals of this type increases the households’ saving rate.

Goal setting is a primary tool robo-advisors use to reduce the impact of households’ biased
beliefs about their future income flows and debt repayment ability. Gargano & Rossi (2020) study
an Italian robo-advisor and find that the practice of goal setting to manage spending and saving
is adopted widely when offered: Forty-one percent of the users who have access to goal setting
use it on a continuous basis. In a difference-in-differences analysis based on a natural experiment,
Gargano & Rossi (2020) estimate an intention-to-treat effect of goal setting on savings of €20
per month and a local average treatment effect of €60 per month, for an average income of the
robo-advisor’s users of €1,200 per month. The authors also show that goal setting is particularly
effective for individuals who the literature has identified to be at risk of not saving enough for
retirement, who display high impatience (Laibson 1997), low levels of education (Cole, Paulson
& Shastry 2014), low income and socioeconomic status (Banerjee & Duflo 2011, Kuhnen & Miu
2017), and inattention (Karlan et al. 2016).

Gargano & Rossi (2020) also show that goal setting through robo-advising tools motivates
users to save more because once users set a certain state of the world as the one they want
to reach (goal), they monitor the robo-advisor often to increase the probability that the state
is reached. Goal setting thus increases the likelihood of reaching a valuable future state of the

www.annualreviews.org (cid:129) Robo-Advice

551

---

<!-- PAGE 10 -->

world by reminding users of their stated beliefs regularly while they make consumption and saving
choices.

Whether households are aware or naive about their biases is central to assessing the effec-
tiveness of a solution like robo-advising, which requires active adoption by users, relative to
a nudge or default option, which exploits households’ inattention and/or inertia in economic
decision-making. Researchers have used robo-advising to assess bias awareness and, consequently,
households’ assessment of the value of robo-advisors. To this aim, Chak et al. (2022) implement
a randomized control trial in the realm of robo-advice for household debt management. House-
holds are first left to their own means to solve three debt management problem scenarios whereby
they allocate a given disposable income to the repayment of several debt accounts whose features
(e.g., interest rates, minimum fees, late-fee payments) vary. Some users are then randomly offered
the help of a robo-advisor for allocation suggestions, and, within this group, some are provided
robo-advice for free, and others have to indicate their willingness to pay (WTP) for the tool. Note
that robo-advice for debt management is a primary application of automated advice because, con-
trary to choices under risk and uncertainty such as investment decisions, debt repayment choices
have a unique optimal solution that does not depend on households’ preferences, beliefs, or other
characteristics.

Chak et al. (2022) find that the average subject who is offered the robo-advising tool for a cost
expresses a WTP above and beyond the actual monetary benefits the subject obtains:1 The average
WTP is higher than the average amount subjects left on the table when making choices unassisted
relative to the optimal solutions. This result suggests that households are likely sophisticated about
their inability to assess optimal debt repayment strategies.

3.2. Beliefs About Others and the Macroeconomy

As discussed in the previous section, providing households with unbiased and representative in-
formation about others’ spending affects choices. This effect acts through a beliefs channel:
Households must have misestimated the spending of others if observing unbiased information
changes their behavior in the direction of their peers’ choices (D’Acunto, Rossi & Weber 2019).
Robo-advisors reduce biased beliefs about others’ outcomes not only in the realm of
consumption–saving choices but also in investment. D’Acunto, Ghosh & Rossi (2022) study a
robo-advisor for debt investment by households in the form of providing loans to borrowers on a
peer-to-peer platform. This form of investment requires that lenders form beliefs about potential
borrowers’ probability of default and expected cash flows to assess the expected returns from al-
ternative loan requests. D’Acunto, Ghosh & Rossi (2022) first document that investors use rules
of thumb based on cultural norms when assessing the viability of borrowers that belong to alter-
native social groups but are otherwise observationally similar. They find evidence for an in-group
versus out-group bias, whereby lenders who belong to a social group underestimate the probabil-
ity of default by borrowers from the same social group, and an implicit bias, whereby all lenders
overestimate the probability of default by borrowers from a heavily discriminated social group,
including the members of such group.

If these distorted beliefs were driven by lenders’ conscious willingness to discriminate against
the social groups they disliked, even if at a cost, lenders would not choose the borrowers sug-
gested by a robo-advising tool that did not engage in discrimination. By contrast, if lenders used
stereotypical rules of thumb to form beliefs but were aware that their beliefs might be inac-
curate (inaccurate statistical discrimination), they would follow the suggestions of an unbiased

1The authors implement a Becker–DeGroot–Marschak mechanism to elicit truthful WTP by agents.

552

D’Acunto (cid:129) Rossi

---

<!-- PAGE 11 -->

robo-advisor. D’Acunto, Ghosh & Rossi (2022) find that the same investors/lenders start provid-
ing funding to borrowers from groups they were less likely to choose before adopting robo-advice
and stop providing lending to borrowers belonging to their own social group, whose probability
of default they underestimated before adopting robo-advice.

As far as beliefs about aggregate outcomes are concerned, Capponi, Olafsson & Zariphopoulou
(2022) study the effects of a robo-advisor that provides unbiased expectations to users with respect
to stock market return and the risk–return trade-off of equity investments. The authors find that
robo-advising improves the Sharpe ratio and return of households’ risky portfolios, especially in
times of economic downturns, when households have excessively negative expectations about fu-
ture market returns and tend to reduce market exposure, whereas maintaining market exposure
would be especially profitable given the more favorable risk–return trade-off. D’Acunto, Prabhala
& Rossi (2019) further document that robo-advice virtually eliminates a set of biases in individ-
ual investors’ decision-making that have been attributed to nonstandard beliefs about aggregate
and individual stock returns, such as trend chasing, the disposition effect, and the rank effect in
trading.

4. REDUCING TRANSACTION COSTS

To optimize future consumption through wealth accumulation, standard portfolio optimization
models predict that virtually every household should participate in equity markets by investing a
fraction of their savings as long as participation costs are minimal. Conversely, an extensive liter-
ature in economics and finance has proposed participation costs as a potential explanation for one
of the most common findings in household finance around the world—the stock market partici-
pation puzzle, whereby a significant fraction of households do not participate in the stock market
and many invest smaller fractions of their wealth than predicted by standard models (Moskowitz &
Vissing-Jørgensen 2002).2 Costs can also be relevant for consumption/saving transactions (Abel,
Eberly & Panageas 2007) and, importantly, do not only take the form of monetary costs. Indeed,
the cognitive and psychological costs households face to conceptualize the household finance puz-
zles they face, to determine the potential choices they can make, to assess their expected value, and
to take the responsibility to act are substantial and completely dismissed in settings that assume
standard economic decision-makers (Sweet et al. 2013, Chak et al. 2022).

4.1. Monetary Costs

Monetary transaction costs, such as the price of a spending transaction or stock trade, have been
declining over the last few decades but might still represent a barrier to participation, especially for
the most vulnerable households (Reher & Sokolinski 2021). In line with this argument, Philippon
(2019) proposes a model in which a crucial feature of robo-advising and other FinTech platforms is
that they cut monetary financial transaction costs. Philippon (2019) argues that FinTech platforms,
which include robo-advisors, should increase participation in equity markets and reduce wealth
inequalities within and across countries. Reher & Sokolinski (2021) provide empirical evidence
supporting this argument. They study a US robo-advisor for financial investments that, during the
sample period they observe, cut the minimum amount required for access, which is tantamount to a

2Several other explanations not based on participation costs have also been studied in the literature. For
instance, households’ lack of financial literacy and understanding of the concept of diversification (Lusardi
& Mitchell 2014) and households’ lack of trust in the stock market and its participants (Guiso, Sapienza &
Zingales 2009; Giannetti & Wang 2016; Gurun, Stoffman & Yonkers 2018; D’Acunto, Prokopczuk & Weber
2019; D’Acunto 2021).

www.annualreviews.org (cid:129) Robo-Advice

553

---

<!-- PAGE 12 -->

drop in the costs of participation because households are required to maintain the minimum value
on their account rather than using such resources otherwise. Reher & Sokolinski (2021) show that
the share of households owning equities increases after this intervention and that the performance
of their portfolios, which are robo-advised, improves. Because this type of intervention does not
affect wealthier households that invested more than the minimum before the change, the benefits
are fully concentrated among middle-class and poorer households.

Research shows that whether robo-advisors provide benefits in terms of execution costs de-
pends on their design. US-based robo-advisors for financial investments, which should be more
appropriately labeled robo-managers, require an investor to commit cash to an account that is
managed automatically, including decisions to trade and rebalance the portfolio, which typically
happens at prespecified times (Reher & Sun 2019, Rossi & Utkus 2020b).

Other forms of robo-advice provide suggestions but require households to make active deci-
sions. These robo-advisors are closer to the role of a traditional financial advisor than to that of
a robo-manager. D’Acunto, Prabhala & Rossi (2019) study such a robo-advisor in India, which
was introduced by a large brokerage house, alongside traditional human advisors. They show
that robo-advice, on average, improves the performance of households’ portfolios, and the im-
provement is driven almost entirely by inducing higher portfolio diversification, which reduces
portfolio volatility. For this reason, the average performance improvement is entirely captured by
households whose portfolios were undiversified before adoption (even though human financial
advisors already helped these households). D’Acunto, Prabhala & Rossi (2019) find that diversi-
fied households not only face no performance improvement but perform worse after adoption
because they use the robo-advisor often, which increases their trading fees relative to before
adoption.

Even in the case of robo-managers, the benefits of accessing robo-advice vary across demo-
graphics. Rossi & Utkus (2020b) use machine-learning techniques to understand which investors’
demographic and portfolio characteristics predict higher performance improvement under robo-
advice. The cash share and trading volume at adoption are positively related to the improvement
in performance after access to robo-advice, indicating that investors who traded often and/or
held a large portion of their wealth in cash benefited most from robo-advice. The authors also
find that tenure, the percentage of wealth invested in mutual funds, and the percentage of mutual
fund holdings in indexed funds are negatively related to the benefits from robo-advice. Finally,
they find a positive monotonic relation between the share of equities held and the benefits of
robo-advice, because the portfolio of funds in which a robo-manager invests has higher risk–return
trade-offs than does the portfolio managed by the average investor.

Reducing execution costs not only is a feature of robo-advisors for investment but also is
common among robo-advisors for consumption. Researchers have studied the effects of mobile
wallets—applications that provide households with the ability to engage in low-cost electronic
spending transactions, and provide robo-advising features. Agarwal et al. (2020) find that adopt-
ing low-cost transaction mobile wallets increases the spending capacity of Indian households by
3% for each 10-percentage-point dependence on cash for transactions before adoption. Agarwal
et al. (2020) also detect a potential undesirable feature of robo-advising for consumption: House-
holds’ higher spending capacity after adoption is due at least in part to the increased salience and
lower search costs for conspicuous purchase opportunities.

Lower transaction costs when using robo-advisors for consumption not only aligns house-
holds’ behavior with the predictions of standard economic models but also has business cycle
effects. Agarwal et al. (2019) and Agarwal et al. (2022) show that the diffusion of a mobile wal-
let in Singapore, which reduced spending transaction costs substantially, increased sales growth
disproportionately for new and small businesses, which are responsible for most employment

554

D’Acunto (cid:129) Rossi

---

<!-- PAGE 13 -->

growth in the United States and abroad (Haltiwanger, Jarmin & Miranda 2013). These aggre-
gate effects of FinTech and robo-advising adoption are likely to be especially high in emerging
countries, as Agarwal et al. (2022) and Crouzet, Gupta & Mezzanotti (2022) document, exploiting
the sudden 2016 Indian demonetization event as a shock to technology adoption.

4.2. Cognitive and Psychological Costs

The costs households face to execute economic transactions can also be cognitive and psycholog-
ical. Even if households fully understood the economic problems they faced and were capable of
obtaining close-to-optimal solutions, conceptualizing such problems and determining their solu-
tions require the use of cognitive skills and time, both of which are scarce resources (Abel, Eberly
& Panageas 2013). Households often lack the cognitive skills and economic or numerical literacy
needed to understand and solve economic problems, which increases the cognitive costs of making
decisions (Lusardi & Mitchell 2014). Cognitive abilities also predict the wedge between house-
holds’ choices and standard neoclassical optimal solutions for forecasting economic variables and
making economic decisions (D’Acunto et al. 2022). Moreover, a large line of work in behavioral
economics has documented that the complexity of choices whose subtleties consumers cannot
fully grasp can lead to choice avoidance (Iyengar & Lepper 2000) and inertia in decision-making
(O’Donoghue & Rabin 1999, Madrian & Shea 2001), hence suboptimal choices relative to the
ones of a standard neoclassical agent.

By simplifying the decision process and making the future potential benefits of active choices
more clear and tangible, robo-advice can reduce cognitive costs, psychological costs, and iner-
tia in decision-making. For instance, Bianchi & Brière (2021) study a French robo-advisor for
employees’ savings accounts that provides a salient target for portfolio allocations that investors
can observe at any time. They find that robo-advice increases attention to one’s account. In turn,
higher attention leads to higher risk-adjusted returns and lower volatility (Gargano & Rossi 2018).
Moreover, the salient graphical target depiction, which the robo-advisor computes automatically,
reduces the cognitive costs of assessing whether and to what extent portfolio allocations devi-
ate from an optimal benchmark. This drop in the cognitive costs of elaborating the optimization
problem and mapping the solution into an investment action reduces investors’ inertia in financial
decision-making and leads to more frequent portfolio rebalancing, which induces higher risk-
adjusted returns relative to unassisted portfolios. Bianchi & Brière (2021) find that the benefits of
robo-advice are higher for investors holding smaller portfolios and displaying lower stock market
participation before adoption, which presumably represent less wealthy and lower-income em-
ployees. Reducing cognitive costs through robo-advice thus has the same potential distributional
consequences as reducing monetary transaction costs—it encourages participation and wealth
accumulation by more vulnerable households.

Psychological costs for households facing financial and economic decisions, including anxi-
ety and fear of disappointment in case of bad outcomes, are nonnegligible (Sweet et al. 2013).
Gennaioli, Shleifer & Vishny (2015) model the money doctor role of financial advisors, who re-
duce psychological costs and lead investors to take on more risk, and Linnainmaa et al. (2022)
provide empirical evidence in microdata consistent with this model. In Section 4.1, we interpreted
the fact that households have a high WTP for robo-advice for debt management relative to the
monetary benefits they obtain from switching to robo-advice as evidence of households’ awareness
of their own biases (Chak et al. 2022). A nonbeliefs-based interpretation is that households might
correctly assess their ability to find optimal debt repayment strategies, but the cognitive and psy-
chological costs to do so lead them to be willing to overpay to obtain an automated robo-advisor
and avoid facing the problem altogether.

www.annualreviews.org (cid:129) Robo-Advice

555

---

<!-- PAGE 14 -->

5. OPEN QUESTIONS

5.1. Learning From Robo-Advice

Whether households learn about their biases and how to correct them after being exposed to
robo-advice is a wide-open question and one that has important policy implications. With learn-
ing, access to robo-advice would not need to be repeated over time, and robo-advisors’ role of
transforming households into standard economic decision-makers would be quite effective. The
effectiveness of robo-advice would be enhanced if it produced spillover effects of learning about bi-
ases and how to correct them across areas of economic decision-making. In this sense, robo-advice
could be interpreted as a means of delivery of financial literacy, which, contrary to traditional
financial literacy programs, is cheap: It does not require recruiting and paying instructors, invest-
ing time by users, or facing cognitive costs when trying to apply abstract principles to real-world
choices. Instead, users learn by imitation during a time they would have anyway spent making
(often flawed) economic choices.

This question is still open because most empirical settings so far include short time series:
Robo-advisors, especially in areas different from portfolio management, have only recently started
to diffuse. Currently, the evidence for learning is mixed. For instance, Chak et al. (2022) and
D’Acunto, Ghosh & Rossi (2022) do not detect any learning from robo-advice by households in
either debt management or peer-to-peer lending choices, but Hao et al. (2022) do find evidence of
spillover effects of robo-advice-based corrections in investment strategies to nonadvised portfolios
by the same households. Bianchi & Brière (2021) find that robo-advice for retirement investments
increases households’ attention to their own accounts and to trading strategies, which in principle
could also improve performance in nonadvised investment accounts, which are unobserved to the
econometrician.

More research is warranted to understand whether the conflicting results in the literature arise
because of studying different economic problems, some of which might be easier to solve than
others in different institutional settings, or because of other reasons. Empirical research needs
observational data in which multiple financial accounts of the same household are observed, of
which only some are robo-advised, and ideally, the assignment to robo-advice is quasi-random
across accounts and within the household. Alternatively, research could use settings in which re-
searchers observe repeated choices by the same user of the same account, for which robo-advice
is intermittently available, so that one could assess whether exposure to robo-advice lets users
learn about biases and correct them. More experimental research would help isolate the potential
mechanisms through which households learn from the transactions from one part of their balance
sheet to other parts, if at all.

Economic preferences are another dimension that could be affected by learning from the infor-
mation gathered through robo-advice but that has been largely neglected by the existing literature.
As we discussed in Section 3, most existing work on the information provided to consumers via
robo-advice has focused on agents’ beliefs. In principle, though, robo-advice could shape users’
preferences, too. For instance, learning about the effects of diversification on a portfolio’s ex-
pected returns and volatility might change users’ risk appetite and hence their choices under risk.
Research that can disentangle effectively the roles of learning from robo-provided information in
consumers’ preferences and beliefs would provide a substantial contribution to our understanding
of the consequences of the diffusion of robo-advice around the world.

5.2. Algorithmic Aversion Versus Appreciation and Inequalities

The drivers of robo-advice adoption are not yet well understood. Whereas research designs on
the effects of robo-advising on choices aim to obtain quasi-exogenous variation in the provision of

556

D’Acunto (cid:129) Rossi

---

<!-- PAGE 15 -->

robo-advice across observationally similar households, the extensive margin of choosing whether
to adopt is important to assess the aggregate effects of robo-advice. Most existing research based on
randomized treatment with robo-advice finds that the less sophisticated households benefit most
because their unassisted choices typically depart more from standard neoclassical predictions. Less
sophisticated households, though, are less likely and slower to adopt new technologies due to a lack
of awareness, distrust in unknown applications, and other reasons (Foster & Rosenzweig 2010). If
true also for the adoption of robo-advice, the heterogeneous effects on performance conditional
on adoption would be counteracted.

Existing research provides mixed evidence for the existence and heterogeneity of distrust to-
ward algorithms (algorithmic aversion) (Dawes 1979). In principle, this form of distrust could have
several sources, including the lack of direct access and communication with a human and/or the
lack of skills needed to understand robo-advising processes (Rossi & Utkus 2020a). Rossi & Utkus
(2020b) survey a large representative sample of traditionally advised, robo-advised, and unadvised
households and find that algorithmic aversion is the main predictor of robo-advice adoption. They
also show that aversion varies dramatically across age groups and other demographic characteris-
tics. Ramadorai et al. (2022) estimate a structural model that captures interactions between human
clients and hybrid robo-advisors that offer different forms of human counseling to complement a
robo-manager. The model features three dimensions of algorithmic aversion: a per-period disu-
tility of dealing with the algorithm, pessimism about the algorithm’s ability to manage assets, and
uncertainty about the algorithm’s performance. The authors find evidence that algorithm aver-
sion is driven mainly by ongoing disutility and uncertainty and that human advice is important
especially to retain households invested in equities during market downturns.

At the same time, a strand of research in social psychology argues that some households in
fact display forms of algorithmic appreciation—they prefer to rely on algorithms more than hu-
mans when making decisions. Logg, Minson & Moore (2019) find that decision-makers are more
adherent to advice when they know it comes from an algorithm rather than a human, and this
is true also for forecasts of choices based on human taste. Algorithmic appreciation is higher for
decision-makers who are not used to making forecasts in their daily lives and lower for those whose
occupations involve making forecasts.

Understanding the conditions under which algorithmic aversion or appreciation arises allows
for assessing whether robo-advice could reduce rather than increase wealth inequalities. Algorith-
mic aversion reduces the adoption of robo-advice, which could exacerbate differences in outcomes
across the wealth and education distributions if more vulnerable households were more algo-
rithmic averse. Algorithmic aversion could produce new types of inequalities, such as across age
groups. Understanding the drivers of algorithmic aversion would also help inform the design of
next-generation robo-advisors.

5.3. Supply-Side Incentives: Financial Institutions Versus Third Parties

This article has focused on the effects of robo-advice on human decision-making from the users’
point of view, but the extent to which the incentives of the suppliers of robo-advice services might
affect the characteristics and consequences of robo-advice is also an important open question.

Applications studied in the literature as well as existing commercial applications in the field
are provided either by financial institutions, such as banks and credit card companies, or by third
parties whose main business aim is the provision of robo-advice. In several applications, financial
institutions face a trade-off that third-party providers do not face: On the one hand, catering to
users who display behavioral biases in decision-making increases their revenues and profits. For
instance, credit card companies benefit from the fact that users do not fully repay their balances at

www.annualreviews.org (cid:129) Robo-Advice

557

---

<!-- PAGE 16 -->

the end of each cycle and end up paying high interest and potential late fees. Consistently, credit
card companies screen for clients’ behavioral biases to exploit them (Ru & Schoar 2018) and might
design consumer contracts in ways that attract biased clients (DellaVigna & Malmendier 2004).
On the other hand, excessive accumulation of credit card debt (and hence of prospective interest
and fee payments) could drive households to default, which would be detrimental to providers in
terms of missed revenues and regulatory concerns. Contrary to financial institutions, third parties
do not face a direct benefit from maintaining households’ biases in decision-making, because they
do not earn the interest and fees households pay on their accounts. If anything, the business model
of third parties often relies on sharing the benefits from robo-advised choices with users based on
fees that are directly proportional to users’ outcomes, which aligns the incentives of the supply
and demand sides.

To date, despite the importance of these differences, research on whether and how the nature
and incentives of the providers of robo-advice shape its design and effectiveness is scant. Moreover,
the effects of the market for control of FinTech applications on the diffusion and effectiveness
of robo-advice, whereby the shareholders of third-party providers might have incentives to exit
their equity investment through sale to financial institutions rather than market-based diffused
ownership (Wang 2018), are an interesting and open topic for future research.

5.4. Broader Implications for Economics and Society

We conclude this article by discussing a set of broader implications of robo-advice that beget
further research in economics, finance, social psychology, sociology, law, and other fields.

In terms of broader implications for economics, this article has advanced the view that robo-
advice can be a disruptive feature for decision-making in that it can transform biased and inexpert
households into agents that form beliefs and act in line with standard neoclassical models. This
feature could have an important impact on the direction of future research in economics. After
developing standard neoclassical models in microeconomics and macroeconomics, the field of
behavioral economics has documented many ways in which decision-makers in the field and the
laboratory depart from the assumptions of such models. These results have fed back into the
original strands of neoclassical economics and have motivated new generations of microeconomic
and macroeconomic theories that incorporate features of decision-making documented in the
field into representative- and heterogeneous-agent models in order to make the predictions of
such models more realistic and to produce further testable implications that would not arise in
standard models. As robo-advice diffuses more and more widely, though, traditional standard
neoclassical models, based on which robo-advisors are designed, could increase their explanatory
power for empirical patterns given that agents behave more in line with standard assumptions.
Understanding whether and how endowing households with robo-advice could make standard
models more predictive of observed outcomes and hence revive their relevance in an open agenda.
Moreover, robo-advice could be used as a potential solution to the lack of effectiveness of eco-
nomic policies that require active choices by households to be fully transmitted to the economy.
Households’ biases often reduce the aggregate effects of policies simply because many house-
holds that could act in a way that increases transmission (and would benefit from doing so) are
unaware of or do not understand policies—they act as human frictions in the transmission of pol-
icy (D’Acunto, Hoang & Weber 2022). Research in macroeconomics and finance has studied a set
of potential solutions, such as policy communication (D’Acunto et al. 2020), the design of sim-
ple policies (D’Acunto et al. 2022), and an increase in trust and attention to policy institutions
(D’Acunto, Fuster & Weber 2021), to limit the effects of human frictions. Robo-advice could be
a cheap and effective means of transmission of policy: Most households around the globe can be
accessed directly via personal devices.

558

D’Acunto (cid:129) Rossi

---

<!-- PAGE 17 -->

Finally, an important trade-off that crosses several fields of research and begets further inquiry
is the tension between freedom in individual decision-making and designing instruments that al-
low for socially optimal economic choices. Although existing research is still limited, as we have
argued in this article, the evidence so far seems to suggest that robo-advice has the potential to
align households’ incentives with those of standard decision-makers, which might make policy
design and aggregate outcomes more efficient. At the same time, the nature of algorithmic ad-
vice, which often does not include explanations to households or provides explanations that many
households cannot understand, requires that households follow and accept its suggestions often
without a full understanding of them. Over time, robo-advice could create conformity and de-
pendence on algorithmic indications, which, when paired with a lack of understanding of such
indications, might reduce critical thinking, induce social conformity, and reduce heterogeneities
in preferences and beliefs across individuals, which could have far-reaching implications across
many aspects of social life. Understanding this potential trade-off and assessing its prevalence and
potential relevance are two of the most important open questions in this area.

6. CONCLUSIONS

Robo-advice has the potential to transform households that display a set of biases and suboptimal
decision-making processes across a wide range of economic problems into standard economic
agents by providing them with a fully informed and rational-expectation benchmark that can be
implemented cheaply and that can barely be provided by human advisors.

In this article, we have emphasized that research on robo-advice is still in its infancy and we have
proposed open questions to develop this agenda in the direction of better understanding whether,
how, and why robo-advice might achieve the goals indicated above. We have also argued that
robo-advice could decrease or widen wealth inequalities across a set of demographic dimensions.
Understanding this trade-off is an important area for future inquiry and one that speaks to the
policy implications of all the open questions we have indicated in this article.

Making researchers realize that robo-advice is not a mere FinTech application to the allocation
of households’ investment portfolios, as the media and normal parlance suggest, but rather a po-
tentially transformational force across most dimensions of individual economic decision-making
that has consequences for empirical and theoretical research across several fields of economics and
finance is the main message coming from this nascent literature.

DISCLOSURE STATEMENT

The authors are not aware of any affiliations, memberships, funding, or financial holdings that
might be perceived as affecting the objectivity of this review.

LITERATURE CITED

Abel AB, Eberly JC, Panageas S. 2007. Optimal inattention to the stock market. Am. Econ. Rev. 97:244–49
Abel AB, Eberly JC, Panageas S. 2013. Optimal inattention to the stock market with information costs and

transactions costs. Econometrica 81:1455–81

Agarwal S, Basu D, Ghosh P, Pareek B, Zhang J. 2022. Demonetization and digitization. SSRN Work. Pap.

3197990

Agarwal S, Qian W, Ren Y, Tsai H-T, Yeung BY. 2020. The real impact of fintech: evidence from mobile payment

technology. SSRN Work. Pap. 3556340

Agarwal S, Qian W, Yeung BY, Zou X. 2019. Mobile wallet and entrepreneurial growth. AEA Pap. Proc. 109:48–

53

www.annualreviews.org (cid:129) Robo-Advice

559

---

<!-- PAGE 18 -->

Andre P, Pizzinelli C, Roth C, Wohlfart J. 2022. Subjective models of the macroeconomy: evidence from

experts and representative samples. Rev. Econ. Stud. 89:2958–91

Armantier O, Bruine de Bruin W, Topa G, Van Der Klaauw W, Zafar B. 2015. Inflation expectations and

behavior: Do survey respondents act on their beliefs? Int. Econ. Rev. 56:505–36

Ashraf N, Karlan D, Yin W. 2006. Tying Odysseus to the mast: evidence from a commitment savings product

in the Philippines. Q. J. Econ. 121:635–72

Bailey M, Dávila E, Kuchler T, Stroebel J. 2019. House price beliefs and mortgage leverage choice. Rev. Econ.

Stud. 86:2403–52

Baker SR. 2018. Debt and the response to household income shocks: validation and application of linked

financial account data. J. Political Econ. 126:1504–57

Banerjee AV, Duflo E. 2011. Poor Economics: A Radical Rethinking of the Way to Fight Global Poverty. New York:

PublicAffairs

Barberis N, Greenwood R, Jin L, Shleifer A. 2015. X-CAPM: an extrapolative capital asset pricing model.

J. Financ. Econ. 115:1–24

Barberis N, Greenwood R, Jin L, Shleifer A. 2018. Extrapolation and bubbles. J. Financ. Econ. 129:203–27
Bernanke BS. 2009. Reflections on a year of crisis. Speech presented at the Federal Reserve Bank of Kansas City’s

Annual Economic Symposium, Jackson Hole, Wyoming, Aug. 21

Bianchi M, Brière M. 2021. Augmenting investment decisions with robo-advice. SSRN Work. Pap. 3751620
Binder CC. 2017. Measuring uncertainty based on rounding: new method and application to inflation

expectations. J. Monet. Econ. 90:1–12

Bruine de Bruin W, Van der Klaauw W, Topa G, Downs JS, Fischhoff B, Armantier O. 2012. The effect of

question wording on consumers’ reported inflation expectations. J. Econ. Psychol. 33:749–57

Bursztyn L, Ederer F, Ferman B, Yuchtman N. 2014. Understanding mechanisms underlying peer effects:

evidence from a field experiment on financial decisions. Econometrica 82:1273–301

Calvet LE, Campbell JY, Sodini P. 2007. Down or out: assessing the welfare costs of household investment

mistakes. J. Political Econ. 115:707–47

Calvet LE, Campbell JY, Sodini P. 2009. Measuring the financial sophistication of households. Am. Econ. Rev.

99:393–98

Capponi A, Olafsson S, Zariphopoulou T. 2022. Personalized robo-advising: enhancing investment through

client interaction. Manag. Sci. 68:2485–512

Carlin B, Olafsson A, Pagel M. 2023. Mobile apps and financial decision making. Rev. Finance 27(3):977–96
Carroll CD, Crawley E, Slacalek J, Tokuoka K, White MN. 2020. Sticky expectations and consumption

dynamics. Am. Econ. J. Macroecon. 12(3):40–76

Chak I, Croxson K, D’Acunto F, Reuter J, Rossi A, Shaw J. 2022. Robo-advice for borrower repayment

decisions. Occas. Pap. 61

Charles KK, Hurst E, Roussanov N. 2009. Conspicuous consumption and race. Q. J. Econ. 124:425–67
Coibion O, Gorodnichenko Y, Kamdar R. 2018. The formation of expectations, inflation, and the Phillips

curve. J. Econ. Lit. 56:1447–91

Coibion O, Gorodnichenko Y, Knotek ES II, Schoenle R. 2020. Average inflation targeting and household

expectations. NBER Work. Pap. 27836

Coibion O, Gorodnichenko Y, Weber M. 2022. Monetary policy communications and their effects on

household inflation expectations. J. Political Econ. 130:1537–84

Cole S, Paulson A, Shastry GK. 2014. Smart money? The effect of education on financial outcomes. Rev.

Financ. Stud. 27:2022–51

Crouzet N, Gupta A, Mezzanotti F. 2022. Shocks and technology adoption: Evidence from electronic payment systems.

Work. Pap., Northwestern Univ., Evanston, IL

Cutler DM, Poterba JM, Summers LH. 1990. Speculative dynamics and the role of feedback traders. NBER Work.

Pap. 3243

Da Z, Huang X. 2020. Harnessing the wisdom of crowds. Manag. Sci. 66:1847–67
D’Acunto F. 2021. Tear down this Wall Street: Anti-finance rhetoric and investment decisions. SSRN Work. Pap.

3213904

D’Acunto F, Fuster A, Weber M. 2021. Diverse policy committees can reach underrepresented groups. Work. Pap.

2021-95, Univ. Chicago

560

D’Acunto (cid:129) Rossi

---

<!-- PAGE 19 -->

D’Acunto F, Ghosh P, Rossi AG. 2022. How costly are cultural biases? Evidence from fintech. SSRN Work. Pap.

3736117

D’Acunto F, Hoang D, Paloviita M, Weber M. 2019. Cognitive abilities and inflation expectations. AEA Pap.

Proc. 109:562–66

D’Acunto F, Hoang D, Paloviita M, Weber M. 2020. Effective policy communication: targets versus instruments.

Work. Pap., Univ. Chicago

D’Acunto F, Hoang D, Paloviita M, Weber M. 2021a. Human frictions in the transmission of economic policies.

NBER Work. Pap. 29279

D’Acunto F, Hoang D, Paloviita M, Weber M. 2022. IQ, expectations, and choice. Rev. Econ. Stud.

https://doi.org/10.1093/restud/rdac075

D’Acunto F, Hoang D, Weber M. 2022. Managing households’ expectations with unconventional policies.

Rev. Financ. Stud. 35:1597–642

D’Acunto F, Malmendier U, Ospina J, Weber M. 2021b. Exposure to grocery prices and inflation expectations.

J. Political Econ. 129:1615–39

D’Acunto F, Malmendier U, Weber M. 2021. Gender roles produce divergent economic expectations. PNAS

118(21):e2008534118

D’Acunto F, Prabhala N, Rossi AG. 2019. The promises and pitfalls of robo-advising. Rev. Financ. Stud.

32:1983–2020

D’Acunto F, Prokopczuk M, Weber M. 2019. Historical antisemitism, ethnic specialization, and financial

development. Rev. Econ. Stud. 86(3):1170–206

D’Acunto F, Rossi AG. 2021. Robo-advising. In The Palgrave Handbook of Technological Finance, ed. R Rau,

R Wardrop, L Zingales, pp. 725–49. Cham, Switz.: Palgrave Macmillan

D’Acunto F, Rossi AG. 2022a. IT meets finance: financial decision making in the digital era. SSRN Work. Pap.

4100784

D’Acunto F, Rossi AG. 2022b. New frontiers of robo-advising: consumption, saving, debt management, and
taxes. In Machine Learning in Financial Markets: A Guide to Contemporary Practice, ed. A Capponi, C-A
Lehalle, pp. 9–28. Cambridge, UK: Cambridge Univ. Press

D’Acunto F, Rossi AG, Weber M. 2019. Crowdsourcing financial information to change spending behavior. CESifo

Work. Pap. 7533

D’Acunto F, Weber M. 2022. Memory and beliefs: evidence from the field. Work. Pap., Univ. Chicago
D’Acunto F, Weber M, Yin X. 2022. Microfounding household debt cycles with extrapolative expectations. Work.

Pap., Univ. Chicago Booth Sch. Bus.

Das S, Kuhnen CM, Nagel S. 2020. Socioeconomic status and macroeconomic expectations. Rev. Financ. Stud.

33:395–432

Dawes RM. 1979. The robust beauty of improper linear models in decision making. Am. Psychol. 34:571–82
De Long JB, Shleifer A, Summers LH, Waldmann RJ. 1990. Positive feedback investment strategies and

destabilizing rational speculation. J. Finance 45:379–95

DellaVigna S, Malmendier U. 2004. Contract design and self-control: theory and evidence. Q. J. Econ. 119:353–

402

Foster AD, Rosenzweig MR. 2010. Microeconomics of technology adoption. Annu. Rev. Econ. 2:395–424
Gargano A, Rossi AG. 2018. Does it pay to pay attention? Rev. Financ. Stud. 31:4595–649
Gargano A, Rossi AG. 2020. Goal setting and saving in the fintech era. SSRN Work. Pap. 3579275
Gargano A, Rossi AG, Wermers R. 2017. The Freedom of Information Act and the race toward information

acquisition. Rev. Financ. Stud. 30:2179–228

Gelman M, Kariv S, Shapiro MD, Silverman D, Tadelis S. 2014. Harnessing naturally occurring data to

measure the response of spending to income. Science 345:212–15

Gennaioli N, Ma Y, Shleifer A. 2016. Expectations and investment. NBER Macroecon. Annu. 30:379–431
Gennaioli N, Shleifer A, Vishny R. 2015. Money doctors. J. Finance 70:91–114
Giannetti M, Wang TY. 2016. Corporate scandals and household stock market participation. J. Finance

71:2591–636

Greenwood R, Shleifer A. 2014. Expectations of returns and expected returns. Rev. Financ. Stud. 27:714–46
Guiso L, Sapienza P, Zingales L. 2009. Cultural biases in economic exchange? Q. J. Econ. 124:1095–131

www.annualreviews.org (cid:129) Robo-Advice

561

---

<!-- PAGE 20 -->

Gurun UG, Stoffman N, Yonker SE. 2018. Trust busting: the effect of fraud on investor behavior. Rev. Financ.

Stud. 31:1341–76

Haltiwanger J, Jarmin RS, Miranda J. 2013. Who creates jobs? Small versus large versus young. Rev. Econ. Stat.

95:347–61

Han B, Hirshleifer D, Walden J. 2019. Visibility bias in the transmission of consumption beliefs and undersaving.

NBER Work. Pap. 25566

Hao R, Hu C, Xu X, Zhang Y. 2022. Beyond performance: the financial education role of robo-advising. SSRN Work.

Pap. 4230191

Heimer RZ, Myrseth KOR, Schoenle RS. 2019. Yolo: mortality beliefs and household finance puzzles.

J. Finance 74:2957–96

Hirshleifer D. 2020. Presidential address: social transmission bias in economics and finance. J. Finance 75:1779–

831

Iyengar SS, Lepper MR. 2000. When choice is demotivating: Can one desire too much of a good thing?

J. Personal. Soc. Psychol. 79(6):995–1006

Kalda A. 2020. Peer financial distress and individual leverage. Rev. Financ. Stud. 33:3348–90
Karlan D, McConnell M, Mullainathan S, Zinman J. 2016. Getting to the top of mind: how reminders increase

saving. Manag. Sci. 62:3393–411

Karlsson N, Loewenstein G, Seppi D. 2009. The ostrich effect: selective attention to information. J. Risk

Uncertain. 38(2):95–115

Kuchler T, Stroebel J. 2021. Social finance. Annu. Rev. Financ. Econ. 13:37–55
Kuhnen CM, Miu AC. 2017. Socioeconomic status and learning from financial information. J. Financ. Econ.

124:349–72

Laibson D. 1997. Golden eggs and hyperbolic discounting. Q. J. Econ. 112:443–78
Lee SK. 2019. Fintech nudges: overspending messages and personal finance management. SSRN Work. Pap. 3390777
Levi Y, Benartzi S. 2020. Mind the app: access to financial information and consumer behavior. SSRN Work. Pap.

3557689

Linnainmaa JT, Melzer BT, Previtero A. 2021. The misguided beliefs of financial advisors. J. Finance 76:587–

621

Linnainmaa JT, Melzer BT, Previtero A, Foerster S. 2022. Investor protections and stock market participation: an

evaluation of financial advisor oversight. Work. Pap., Indiana Univ., Bloomington

Logg J, Minson J, Moore D. 2019. Algorithm appreciation: People prefer algorithmic to human judgement.

Organ. Behav. Hum. Decis. Proc. 151:90–103

Lusardi A, Mitchell OS. 2014. The economic importance of financial literacy: theory and evidence. J. Econ.

Lit. 52:5–44

Madrian BC, Shea DF. 2001. The power of suggestion: inertia in 401(k) participation and saving behavior.

Q. J. Econ. 116(4):1149–87

Malmendier U, Nagel S. 2016. Learning from inflation experiences. Q. J. Econ. 131:53–87
Maturana G, Nickerson J. 2019. Teachers teaching teachers: the role of workplace peer effects in financial

decisions. Rev. Financ. Stud. 32:3920–57

Moskowitz TJ, Vissing-Jørgensen A. 2002. The returns to entrepreneurial investment: a private equity

premium puzzle? Am. Econ. Rev. 92:745–78

Mullainathan S, Noeth M, Schoar A. 2012. The market for financial advice: an audit study. NBER Work. Pap.

17929

O’Donoghue T, Rabin M. 1999. Doing it now or later. Am. Econ. Rev. 89(1):103–24
Olafsson A, Pagel M. 2018. The liquid hand-to-mouth: evidence from personal finance management software.

Rev. Financ. Stud. 31:4398–446

Olafsson A, Pagel M. 2022. The ostrich in us: selective attention to financial accounts, income, spending, and liquidity.

NBER Work. Pap. 23945

Ouimet P, Tate G. 2020. Learning from coworkers: peer effects on individual investment decisions. J. Finance

75:133–72

Philippon T. 2019. The fintech opportunity. NBER Work. Pap. 22476
Ramadorai T, Rossi AG, Utkus S, Walther A. 2022. Algorithm aversion: theory and evidence from robo-advice.

SSRN Work. Pap. 4301514

562

D’Acunto (cid:129) Rossi

---

<!-- PAGE 21 -->

Reher M, Sokolinski S. 2021. Automation and inequality in wealth management. Work. Pap., Univ. North

Carolina, Chapel Hill

Reher M, Sun C. 2019. Automated financial management: diversification and account-size flexibility. J. Invest.

Manag. 17(2):63–75

Rossi AG, Utkus SP. 2020a. The needs and wants in financial advice: human versus robo-advising. SSRN Work.

Pap. 3759041

Rossi AG, Utkus SP. 2020b. Who benefits from robo-advising? Evidence from machine learning. SSRN Work. Pap.

3552671

Ru H, Schoar A. 2018. Do credit card companies screen for behavioral biases? NBER Work. Pap. 22360
Stango V, Zinman J. 2023. We are all behavioral, more or less: a taxonomy of consumer decision-making. Rev.

Econ. Studies 90:1470–98

Sunstein CR. 2017. Nudges that fail. Behav. Public Policy 1:4–25
Sweet E, Nandi A, Adam EK, McDade TW. 2013. The high price of debt: household financial debt and its

impact on mental and physical health. Soc. Sci. Med. 91:94–100

Tang H. 2019. The value of privacy: evidence from online borrowers. Work. Pap., HEC, Paris
Thaler RH, Sunstein CR. 2009. Nudge: Improving Decisions About Health, Wealth, and Happiness. New York:

Penguin

Wang X. 2018. Catering innovation: entrepreneurship and the acquisition market. SSRN Work. Pap. 3247274
Weber M, D’Acunto F, Gorodnichenko Y, Coibion O. 2022. The subjective inflation expectations of
households and firms: measurement, determinants, and implications. J. Econ. Perspect. 36:157–84

Zinman J. 2015. Household debt: facts, puzzles, theories, and policies. Annu. Rev. Econ. 7:251–76

www.annualreviews.org (cid:129) Robo-Advice

563

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| Annual       | Review | of Financial |              | Economics |     |
| ------------ | ------ | ------------ | ------------ | --------- | --- |
| Robo-Advice: |        |              | Transforming |           |     |
13:93:60 6202 yaM 40 ,noM :nO 05.91.94.72  :PI )tseug( tseuG  .gro.sweiverlaunna.www morf dedaolnwoD Households into Rational
| Economic  |          | Agents |         |         |     |
| --------- | -------- | ------ | ------- | ------- | --- |
| Francesco | D’Acunto | and    | Alberto | G.Rossi |     |
DepartmentofFinance,McDonoughSchoolofBusiness,GeorgetownUniversity,Washington,
DC,USA;email:francesco.dacunto@georgetown.edu,agr60@georgetown.edu
Annu.Rev.Financ.Econ.2023.15:543–63
Keywords
FirstpublishedasaReviewinAdvanceon
FinTech,householdfinance,behavioralfinance,consumption,debt,
August24,2023
investments
TheAnnualReviewofFinancialEconomicsisonlineat
financial.annualreviews.org Abstract
https://doi.org/10.1146/annurev-financial-110921-
| Robo-advice | uses | big and open | data to | provide consumers | with fully in- |
| ----------- | ---- | ------------ | ------- | ----------------- | -------------- |
013217
| formed | and rational-expectation |     | benchmarks | in all realms | of household |
| ------ | ------------------------ | --- | ---------- | ------------- | ------------ |
Copyright©2023bytheauthor(s). Thisworkis finance,includingconsumption,saving,investment,anddebtmanagement
licensedunderaCreativeCommonsAttribution4.0
InternationalLicense,whichpermitsunrestricted choices.Italsominimizesthemonetary,cognitive,andpsychologicalcosts
use,distribution,andreproductioninanymedium, thathouseholdsfaceineconomictransactions.Wereviewrecentresearchon
providedtheoriginalauthorandsourcearecredited. thefeaturesandeffectsofrobo-adviceonindividualandaggregateeconomic
Seecreditlinesofimagesorotherthird-party
outcomesthroughthelensofitsdifferencesfromtraditionalhumanadvice.
materialinthisarticleforlicenseinformation.
Wediscussthedistributionalimplicationsofrobo-advice,itspotentialrole
JELcodes:D14,D91,G51,G53,O31
| in increasing | the effectiveness |     | of economic | policies,the | role of providers’ |
| ------------- | ----------------- | --- | ----------- | ------------ | ------------------ |
incentives,andseveralquestionsthatarestillwideopenforresearchersin
finance,economics,socialpsychology,andrelatedfields.
543

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
1.HOUSEHOLDFINANCEPUZZLESANDISSUES
WITHTRADITIONALSOLUTIONS
Everyhouseholdaroundtheworld,irrespectiveofitslevelofincome,wealth,orsophistication,
needstomakecomplexfinancialdecisionsonadailybasis.Firstandforemost,householdsneedto
decidehowmuchtheywanttospendforconsumptionorsavetoincreasefutureconsumption—
theyneedtosolveanintertemporalconsumptionproblem.Oncetheconsumption–savingchoice
ismade,theyneedtoallocateresourcestodurableandnondurablegoodsandchoosehowtofi-
nancetheirdurableconsumption(e.g.,incomeflows,creditcarddebt,mortgages,personalloans,
studentloans).Financingoptionsdifferbasedonmultipledimensionsthatneedtobecompared—
horizons,maturities,interestrates,andamortizationplans.Householdsalsoneedtomanagetheir
assetsbydecidinghowtoinvestsavingstoaccumulatewealthandmaximizefutureconsumption
and/orbequests.Ontopofallocatingresourcesacrossinvestmentassetsintheirfinancialport-
folios,forinstance,theymustchoosewhetherandhowmuchtocontributetoretirementsaving
plans—adecisionthathasbecomeprominentaroundtheworldgiventheglobalmoveawayfrom
definedbenefitpensionsystemsandtowarddefinedcontributionindividualplans.And,oncethey
reachretirementage,theyneedtomakedecisionsaboutthedecumulationphaseoftheiraccumu-
latedretirementsavings,whichisacomplexproblemthatisstillbarelyunderstoodbyresearchers
andpolicymakers.
Ultimately,households,likecorporatemanagers,needtomakemultiplefinancialdecisionsat
highfrequencyandcannotavoidchoosing,inthesensethatavoidingtodecideisachoiceinitself
that has relevant financial implications for the household (Madrian & Shea 2001).Contrary to
corporatemanagers,though,householdscannotspecializeinonlyonetypeofthemultitudeof
financialchoicestheyneedtomake.Moreover,householdsneedtomakeallthesechoices,even
thoughthevastmajorityhaveneverbeenexposedtothemostbasicprinciplesoffinance,suchas
diversificationandcompoundingofinterestrates,orobtainedanyfinancialeducation(Lusardi&
Mitchell2014),becausefinanceisabsentfromstandardprimaryandsecondaryschoolcurricula
invirtuallyeverycountryaroundtheworld.
Given these premises,the fact that most households make decisions that depart from those
predicted by standard economic models should not be surprising. Standard models assume
the existence of utility-maximizing agents who have access to all the information needed to
makefinancialdecisions,useittoformrationalexpectations,andhavestandardeconomicpref-
erences.Alargeandgrowingliteratureinfinanceandeconomicslabelsdeparturesfromstandard
modelsinhouseholds’financialchoicesashouseholdfinancepuzzles(Zinman2015).
Why do we care to understand and solve household finance puzzles? On top of negatively
affectinghouseholds’utility,thesepuzzleshavefourimportantandundesirableaggregateeffects.
First,theytendtoproduceandwidenwealthinequalitiesbecausethepoorerandmostvulnerable
households tend to be less sophisticated in terms of economic and financial literacy and hence
makechoicesthatdepartmostfromoptimality(Calvet,Campbell&Sodini2007,2009).Second,
they dampen the effects of economic policies that central banks and governments implement,
assumingthathouseholdsunderstandandreacttotheminlinewiththepredictionsofstandard
economic models (D’Acunto et al.2021a).Third,household finance puzzles are likely to have
becomeevenmoresevereovertimeduetotheswiftdiffusionofFinTechapplicationsthathave
eased ordinary consumers’ access to high-risk financial choices,such as the trading of complex
financial products like derivatives and cryptocurrencies using apps on their personal devices or
the accumulation of high-interest debt through unsecured financing of consumption expenses
andbuynow,paylaterspendingopportunities.Fourth,adetailedunderstandingofthenatureand
consequences of the biases households face when making financial choices is crucial to inform
544 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
regulators’attemptstodesigneffectivepoliciesthatcanprotecthouseholdsfrombeingexploited
bybetter-informedfinancialinstitutionsandothercounterpartsinfinancialcontracts.
Twotraditionalsolutionshavebeenproposedforhouseholdfinancepuzzles.Thefirstsolu-
tionistheprovisionoffinancialadvice.Financialadvisorsareagentswhosuggesthowhouseholds
shouldmaketheirmultiplefinancialchoicesbyinterpretingtheirpreferencesandbeliefsandeval-
uatingoptions.Unfortunately,though,financialadvisorshavelimitations.Theirservicesaretoo
expensiveformanyhouseholdsandcannotbescaledatalowcost,whichreducestheirviability,es-
peciallyformiddle-andlow-incomehouseholds.Ifanything,theavailabilityoffinancialadvisors
mightincreaseratherthanreducewealthinequalities,giventhatmoreaffluenthouseholdscanac-
cessthembutpoorerhouseholdscannot.Moreover,financialadvisors,similartootherexpertssuch
asCEOsandinstitutionalinvestors,oftenengageinthesamedeparturesfromrationaldecision-
makingthathouseholdsdisplayandendupprovidingunsoundsuggestions(Mullainathan,Noeth
&Schoar2012;Linnainmaa,Melzer&Previtero2021).Atthesametime,theliteraturehasdoc-
umentedtheunintendedconsequencesoflimitingthepresenceoffinancialadvisorsonaccessto
financialinvestmentsbyunsophisticatedhouseholds.Forinstance,Linnainmaaetal.(2022)find
thatoncefinancialadvisors’regulatoryoversightwasintroducedinCanada,thenumberoffinan-
cialadvisorsreduceddrasticallyandsodidhouseholds’stockmarketparticipation,especiallyby
middle-classhouseholds.Thesecondsolutionisthedesignofnudges—defaultchoicesforpro-
gram participation or design mechanisms that lure households into making choices consistent
withthosethatarepresentativeeconomicagentwouldmakeunderthesameconditions(Thaler
&Sunstein2009).Althoughhelpful,byconstruction,nudgescanbarelybetailoredtotheindivid-
ualcharacteristicsofeachhousehold,andtheireffectivenessoftendependsonthedetailsoftheir
design(Sunstein2017).
Nexttohumanfinancialadviceandnudges,robo-advicerepresentsathirdandmorerecent
solutiontohouseholdfinancepuzzles(D’Acunto&Rossi2021).Atfirst,robo-advicemightappear
asnothingmorethantraditionalhumanfinancialadviceproducedanddeliveredautomaticallyto
decision-makerswithFinTechapplicationsthroughpersonaldevices.Evenifthisweretheonly
relevantfeatureofrobo-advice,itwouldmakeitmorescalablethanhumanadvicebyreducing
itscostandallowingaccesstoadvicetoasubstantiallyhighershareofhouseholds.Thisproperty
wouldthusimprovethedistributionalconsequencesofadvicebyaligningthechoicesofvulnerable
householdswiththoseofsophisticatedhouseholds(Philippon2019).
Robo-advice, though, is not just traditional advice produced and delivered automatically
throughpersonal devices.Thecrucial featureof robo-adviceis thatitreduces households’dif-
ferences from the characteristics of standard neoclassical rational decision-makers and hence
allowshouseholds,includingtheleastsophisticated,tomakechoicesclosertothoseastandard
utility-maximizingagentwouldmake.
Robo-advisingtransformsbiaseddecision-makersintostandardneoclassicaldecision-makers
throughthreeuniquefeaturesthatdifferentiateitfromtraditionalformsofadvice.First,robo-
advisingusesbigandopendatatomakehouseholdsfullyinformedabouttheirowncharacteristics
andpastbehavioraswellasthecharacteristicsandpastbehaviorofotheragents,towhichhouse-
holds(andoftentheirhumanadvisors)wouldotherwisehavenoaccessduetotheirlimitedability
torecallpastactionsandcollectandelaboratebigdatasets(D’Acunto&Rossi2022a).Thebig
datathatrobo-advisorsaccessaretheuniverseoftransactionshouseholdsproducewhenmaking
economicdecisions,suchaspurchasesofdurableandnondurablegoods,investmentchoices,and
financingchoices.Robo-advisorscanaccessthiswealthofinformationbecause,sincetheDigital
Revolution,electronictransactionscanbestored,andthesedataareopen;thatis,householdscan
sharethembylinkingtransactionaccountstorobo-advisingapplications.
www.annualreviews.org (cid:129) Robo-Advice 545

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
Second, robo-advising manages households’ beliefs and pushes them closer to the rational
expectationsassumedinstandardmodels.Theeconomicliteraturehasdocumentedseveralsys-
tematicdeparturesofhouseholds’beliefsfromthoseofastandardeconomicagent.Thesizeof
thesedeparturesiscorrelatedwithdemographiccharacteristicsandvariesoverthebusinesscycle.
AswediscussinSection3.1,robo-advisorsprovidehouseholdswithbeliefsaboutboththeirown
futurefinancialconditionsandaggregatemacroeconomicconditionsthatareclosertothoseofa
standardagent.
Third,robo-advisingreducesthetransactioncostsofexecutingeconomicchoices,whichin-
cludenotonlymonetarycostsbutalsothecognitiveandpsychologicalcoststhathouseholdsface
whentryingtomakeeconomicdecisions.
Intherestofthisreview,wedescribethefindingsofexistingacademicresearchonthesethree
definingfeaturesofrobo-advice.Wealsoemphasizethelargesetofopenquestionsandareasof
investigationforfutureresearch.
2.REDUCINGINFORMATIONFRICTIONS
Standardneoclassicaleconomicagents areassumedtobefullyinformedabouttheircharacter-
istics, the characteristics of other agents, and macroeconomic conditions. This assumption of
standard models of intertemporal consumption optimization is heavily violated in the data,ex-
ceptforafewspecialcases,suchashighlysophisticatedinstitutionalinvestorsinfinancialmarkets
whoactivelyengageincostlyinformationacquisition(Gargano,Rossi&Wermers2017).
Mosthouseholdsarebarelyinformedaboutmacroeconomicconditionsandoftenevenignore
thedefinitionofbasiceconomicaggregates,suchasinflationratesorinterestrates(Binder2017).
Householdshavealsobeenshown,onaverage,tohaveawrongassessmentoftheeconomiccon-
ditionsofothereconomicagents,whichisduemainlytoalackoffullinformationaboutother
people’sincomeflows,spending,anddebtpositionsandtheobservationofconspicuousandsalient
transactionsthathouseholdsinterpretasrepresentativeoftheaveragetransactionsothersexecute
(Charles,Hurst&Roussanov2009).Ultimately,andperhapsmostsurprisingly,householdsoften
cannotrecallorprocessinformationabouttheirownincomeflows,consumption,anddebttrans-
actions,eventhoughallthisinformationisproducedbythemandhenceavailabletothemwithout
theneedtocollectpublicorprivatesignalsfromothersources.Forexample,householdsdonot
keepinformationaboutalltheirtransactionsbutoftenpayattentiontothemonlytemporarilyand
forshortperiods(D’Acunto,Rossi&Weber2019).Householdsalsotendtohaveabiasedrecallof
theirconsumptionovertime,whichisdrivenbytheirtendencytorecallhavingpaidlowerprices
thantheactualpricestheyfaced(D’Acunto&Weber2022).
Thefirstuniquefeatureofrobo-adviceispushinghouseholdsclosertobeingfullyinformed
abouttheirown,others’,andaggregateeconomicoutcomes.Robo-advicecanachievethisgoal
bycollectingandelaboratingbigandopentransaction-leveldataatvariouslevelsofobservation:
households’ own characteristics and past choices, the characteristics and past choices of other
decision-makers in the economy,and information about macroeconomic conditions and other
aggregatevariablesthatmightberelevanttoeconomicdecision-making.Intherestofthissection,
we discuss recent research that has studied the mechanics and effects of this function of robo-
advising.
2.1.InformationAboutOne’sOwnCharacteristics:IncomeAggregators
Thefactthatprovidinginformationaboutone’sowncharacteristicsandpastchoicesinfluences
decision-makingmightappearsurprisingatfirst.Afterall,thisinformationisproducedbyhouse-
holds and should therefore be readily available to them at any time. And yet research finds
546 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
thathouseholdslargelyneglectessentialinformationabouttheirownbehaviorduetocognitive
constraintsintheabilitytocollectandprocessinformation(D’Acunto,Ghosh&Rossi2022).
Robo-advice allows households to overcome these constraints and obtain full information
abouttheirpasttransactionsandfinancesthroughincomeaggregators.Incomeaggregatorsare
robo-advisorsthatcollectandelaboratehouseholds’transaction-leveldata.Thesedataareopen
inthathouseholdscansharethembylinkingtheirspendingandotherfinancialaccountstothe
aggregator(Gelmanetal.2014).
Uponobtaininghousehold-leveltransactions,incomeaggregatorsconstructhousehold-level
balancesheetssimilartothosethatcorporationsuseforfinancialreporting(D’Acunto&Rossi
2022b).Aggregatorselaboratebothstaticbalancesheets,whichincludethecurrentoverallvalue
of households’ assets and liabilities at each point in time,and dynamic assessments of the past
evolution,liquidity,and horizons of households’ debts,spending,and investment decisions for
eachentryofthebalancesheet(Baker2018).
Becausenotlinkingallfinancialaccountswouldrendertheaggregator’sinformationelabora-
tionincomplete,householdsthatwanttoaccessthisfeatureofrobo-advisinghaveanincentive
tolinkalltheirfinancialaccountstotheaggregator.Consistently,Baker(2018)showsthat95%
oftheusersofalargeUSincomeaggregatorlinkedalltheircheckingaccounts,over93%linked
alltheirsavingsaccounts,and91%linkedalltheircreditcardaccounts.Atthesametime,house-
holdsmightbewaryofprovidingsomuchdetailedinformationtoanincomeaggregator.Income
aggregatorshaveashorthistoryofoperationsandhencelackreputationintermsofdataprotec-
tionandmanagement,whichmightincreasehouseholds’expectedprobabilitythatthedatamight
beappropriatedbythirdpartiesandbesubjecttocybersecurityconcerns.Consistentwiththese
potentialconcerns,Rossi&Utkus(2020a)findthatarobo-advisor’sreputationisoneofthemain
driversofrobo-adviceadoption,partlybecauseofusers’dataprivacyconcerns(Tang2019).
Incomeaggregationcanbeaformofrobo-adviceifprovidinghouseholdswithinformation
abouttheirowncharacteristicsandpastchoicesinfluencestheirdecision-making.Consistentwith
thispossibility,Olafsson&Pagel(2018)showthatdisplayingaggregateinformationaboutone’s
ownbalancesheetstoIcelandichouseholdsleadstofinancialchoicesthatareclosertothoseofa
standardeconomicagent.Forinstance,householdsreducetheirdebtbalancestoavoidoverdraft
fees,whichisdirectevidencethat,beforetheinformationwasprovidedtothem,householdswere
unawareoftheexistenceorsizeofoverdraftfees.Informationfromincomeaggregatorsalsomakes
householdsrealizethatthebenefitsofrunninghigher-than-limitdebtbalancesarelowerthanthe
monetary costs of the overdraft fees they are charged.Carlin,Olafsson & Pagel (2023) further
documentthat,afterobservingtheirownaggregatebalancesheets,householdsreducetheirnon-
durablespending,especiallyinfrivolouscategoriessuchaseatingoutsidethehomeandtraveling.
Thisreactionsuggeststhat,absenttheinformationincomeaggregatorsprovide,householdsmight
underestimatetheshareoftotalspendingandincomeflowstheyallocateacrossconsumptioncat-
egories.Furtherevidenceoftheeffectsofgivingconsumersaggregatedinformationabouttheir
ownfinancesthroughincomeaggregatingrobo-advisorsisprovidedbyLevi&Benartzi(2020)
and Olafsson & Pagel (2022).The latter paper also provides a direct empirical test of the os-
tricheffect,wherebydecision-makersselecttheinformationtowhichtheywanttoattendintheir
dailylivesbasedontheirbeliefsaboutthepositivityornegativityofsuchinformation(Karlsson,
Loewenstein&Seppi2009).
Inadditiontothemereinformationalvalueofincomeaggregation,robo-advisorsusetheelab-
orated information to focus households’ attention on specific features of their balance sheets,
especially when such features indicate red flags, such as significant increases in spending pat-
terns over time despite constant or declining income flows. Lee (2019) studies a Canadian
robo-advisorthat,ontopofincomeaggregationfeatures,sendsusersoverspendingmessageswhen
www.annualreviews.org (cid:129) Robo-Advice 547

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
theirspendinginonecategoryissubstantiallyhigherthantheuser’srecentspendingwithinthe
samecategory.Notethatincreasingspendingintimesofconstantordecliningincomeflowsisnot
necessarilyinconsistentwithintertemporalconsumptionoptimizationif,forexample,households
correctlyexpecthigherincomegrowth—afeaturethatexistingrobo-advisorscannotobserveor
includeintheirassessmentofredflagsinhouseholds’balancesheets.Recentresearch,though,
documentssubstantialextrapolationinhouseholds’expectationsoffutureincomeaftersmallin-
come increases,which leads to a systematic overestimation of future income levels and growth
relativetoexpostrealizedlevelsandgrowth(D’Acunto,Weber&Yin2022).
Lee (2019) compares users who are just above the robo-advisor’s threshold to send over-
spendingmessageswithuserswhoarejustbelowandhencespendsimilarlymorethanintheir
recentpastbutreceivenomessages.Hefindsthatmessagereceiverscuttheirdailyspendingby
approximately5%more,andthiseffect,despiterevertingintermsofspendingflows,ispermanent
intermsofcumulativespendingovertime;thatis,thetemporaryshockdoesnotfullyrevertover
time.Lee(2019)alsofindsthatolder,wealthier,andmorefinanciallysavvyhouseholdsreactmore
toobtaininginformationabouttheirowntransactions.Althoughthisheterogeneitymightatleast
in part capture higher income growth expected by younger households going forward, it also
opensthepossibilitythatthisformofrobo-advisingmightincreasewealthinequalitiesovertime.
Finally,Lee(2019)findsthat,despitereactingtooverspendingmessagesbyreducingspending,
severalhouseholdsalsoreducethefrequencywithwhichtheyloginandcheckinformationabout
theirfinancesontheincomeaggregator.Thisformoftheostricheffect,wherebyhouseholdstend
toavoidfacingnegativenewsabouttheirfinances,isafeatureofrobo-advisingincomeaggregators
documentedfirstbyOlafsson&Pagel(2022).
Thedetectionofanostricheffectassociatedwithusinginformativerobo-advisorsopensaset
ofresearchquestions.First,wedonotknowwhetherprovidinghouseholdswithcompleteandag-
gregatedinformationabouttheirfinanceshaseffectsinthelongtermorwhethertheostricheffect
(orfatiguefromusinganapplicationregularlyandforlongperiods)makestheeffectsonlytem-
porary.Byconstruction,becauseincomeaggregatorshavebeenimplementedandcommercialized
overonlythelastfewyears,researcherslackdataforrepeatedinterventionsoverprolongedpe-
riods,which would be crucial to answering this question.We also need to understandwhether
the emergence of an ostrich effect makes robo-advisors that provide information such as in-
comeaggregatorsincreaseinequalities.Thisunintendedandundesirableconsequencecouldbe
plausibleifdetachmentfromrobo-advisorsweremorecommonamongvulnerablehouseholds.
Extensiveliteratureinbehavioraleconomicshasalsodocumentedtheprevalenceofpresentbias
in choices and new toy effects, which are more substantial for demographic groups who tend
tounderstandtheirownfinanceslessandmakesuboptimalconsumptionandsavingchoicesin-
tertemporally(see,forexample,Gargano&Rossi2020).Understandingwhetherthesecommon
behavioralfeaturesreducetherelianceonincomeaggregatorsovertimeforhouseholdsthatwould
need them most and increase rather than reduce wealth inequalities is an open area for future
research.
2.2.InformationAboutOtherEconomicAgents
Even if households were fully informed about their balance sheets,solving their intertemporal
consumptionproblemandhencedeterminingtheiroptimalconsumptionandsavingrateswould
beadauntingtaskformosthouseholdsanddependlargelyontheirpreferencesandsubjective
beliefs,which can hardly even be expressed fully and entirely to a financial advisor by nonex-
perteconomicagents(BruinedeBruinetal.2012).Tofacilitatethistask,astrandofresearchin
economics,social psychology,and social finance shows that households make inferences about
548 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
theirownoptimalconsumptionandsavingratesbasedontheconsumptionandsavingratesof
theirpeers,thatis,individualswhohavesimilardemographiccharacteristicsandhencepresum-
ably similar preferences,income flows,and expected income growth (for recent reviews of this
areaofresearch,seeHirshleifer2020andKuchler&Stroebel2021).
Intuitively, making inferences based on signals about the behavior of a large mass of peers
couldbemeaningfulbasedonthewisdomofthecrowds,wherebyalargenumberofindependent
forecastsmadebydifferentindividualscanprovideanaccurateconsensusforecast,withwhichthe
householdcanaligntheirbehavior(Da&Huang2020).Atthesametime,householdscannotac-
cessthefullsetoftransactionsandfullinformationaboutthechoicestheirpeersmakeintermsof
consumption,saving,investment,andfinancing:Theycannotaccessorobservetransaction-level
dataaboutpeersinthesamewaytheyaccesstheirowndata.Instead,householdsarelimitedto
observingtheinformationtheirpeersdisclose,andthisinformationtendstonotberepresentative
ofpeers’finances,especiallyintimesofpervasiveuseofsocialmedia(Han,Hirshleifer&Walden
2019).Peerstendtodisclosetheirmostconspicuousconsumptioninstancesinwhichtheyengage
(Charles,Hurst & Roussanov 2009) while not disclosing information about parsimonious con-
sumptionchoices,theirincomeflows,oraccesstodebtfinancing.Inthisway,thesignalsabout
peers’consumptionthathouseholdsobserveleadthemtooverestimatetheoverallconsumption
ratesofpeersunlesshouseholdsaresophisticatedenoughtoaccountforpeers’partialdisclosure
(Han,Hirshleifer&Walden2019).
Contrarytohouseholdsorhumanadvisors,robo-advisorscanaccessandelaborateinformation
aboutpeers’consumptionandsavingrates.Ifhouseholdsmisestimatethesevariablessystemati-
cally,theyshouldchangetheirconsumptionchoiceswhenrobo-advisorsprovidethemwithfull
information about peers’ finances. D’Acunto, Rossi & Weber (2019) study a US robo-advisor
that,ontopofthestandardincomeaggregationfeaturesdiscussedinSection2.1,providesusers
with elaborated information about peers’ consumption,saving,and investment transactions.In
this context,peers are not users’ social acquaintances: The information is based on transaction
accounts of households that have similar demographics as users, including income levels, age,
residencetypes,andlocations.D’Acunto,Rossi&Weber(2019)findthatusers’spendinglevels
convergewiththoseofpeersforbothuserswhospentmorethanandthosewhospentlessthan
theirpeers.Theeffectsareasymmetric:Overspenderscuttheirspendingsubstantiallymorethan
underspendersoverthefollowing12months.Thisobservationalevidenceraisestheconcernthat
onlytheuserswhoareespeciallyinterestedininformationaboutpeersmightselectintoadopting
robo-advice.Totacklethisconcern,D’Acunto,Rossi&Weber(2019)runarandomizedcontrol
trialwitharepresentativeUSpopulationthatdidnotselectintoanyrobo-adviceapplicationsand
findthesamereactionstotheprovisionofinformationaboutpeers.
Understandingthechannelsthroughwhichprovidingdetailedinformationaboutotherswith
robo-advisingchangeshouseholds’preferences,beliefs,andchoicesisanopenresearcharea.Re-
searchhasshownthatinformationaboutdebtfinancingoptionsandinvestmentdecisionsdoes
transmit across peers (Maturana & Nickerson 2019, Kalda 2020, Ouimet & Tate 2020), but
whethersuchinformationaffectsbehaviorbecauseofitscontentorduetosocialpressureorsocial
conditioning(Bursztyn,Ederer&Yuchtman2014;Baileyetal.2019)—andhencehasthesame
effectswhendeliveredthroughrobo-advisingafterbeinggatheredfromthecrowdsratherthan
one’spersonalacquaintances—isanopenquestion.
Moreover,wehavenoconclusiveevidenceaboutwhetheradaptingone’sbehaviortotheav-
eragebehaviorofthosewithsimilardemographiccharacteristicsisoptimal.Theprincipleofthe
wisdomofthecrowdrequiresthattheassessmentsandhencechoicesofalargegroupofagents
areindependentfromeachothertoprovideaccurateaverageassessments.Still,intimesofsocial
mediawherehouseholdsobservethesamesignalsfromfocalnetworkmembersorinfluencersand
www.annualreviews.org (cid:129) Robo-Advice 549

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
mightreadthesamecommentsandinterpretationsaboutbusinesscycleshockscirculatingintheir
socialnetwork,averagesignalsmightnotbeunbiased.
Totheextentthatasocialplannerwouldcaremoreaboutavoidingoverconsumptionbysome
households(andthepotentialexcessiveuseofdebtfinancing)thanaboutunderconsumptionby
otherhouseholds,theasymmetriceffectsdocumentedbyD’Acunto,Rossi&Weber(2021)sug-
gest that robo-advising for spending using information about others could align with the aims
ofpolicymakers.However,thedistributionalconsequencesofthisformofrobo-advisingarestill
unknownandshouldbeinvestigatedfurther.
2.3.InformationAboutMacroeconomicVariables
Instandardintertemporalconsumptionoptimizationmodels,beliefsaboutfuturemacroeconomic
conditions,especiallyinflation,driveperceptionsofrealinterestratesandhencethedecisionabout
howmuchtoconsumeversussaveforthescopeoffutureconsumption(Bernanke2009).Research
inmacroeconomics,appliedmicroeconomics,andsocialpsychologyhasshownthatmanyhouse-
holdsareuninformedaboutthemostbasicmacroeconomicaggregates(Coibionetal.2020)and
formbiasedbeliefsaboutthem(Armantieretal.2015;D’Acunto,Malmendier &Weber2021;
Weber et al.2022).Furthermore,households’ beliefs are not based on representative informa-
tionbutratheronthefewsignalsaboutpricesandwageshouseholdsobserveintheirdailylives
(D’Acunto, Ghosh & Rossi 2022). Cognitive abilities also determine households’ understand-
ingoftherelationshipsacrosseconomicvariablesandtheirabilitytoelaboratemacroeconomic
information(D’Acuntoetal.2021a,Andreetal.2022).
Robo-advice to provide households with unbiased processed information should thus natu-
rallyextendtomacroeconomicvariables,especiallyinflationandunemployment,whoseexpected
valuesdeterminehouseholds’perceivedrealratesandexpectedincomeflowsinstandardmod-
els.Becausesystematicbiasesandmistakesineconomicexpectationsaremorefrequentamong
themostvulnerablehouseholds,theycancontributetothewideningofinequalities(D’Acunto
etal.2020).Andyetresearchontheprovisionandeffectsofmacroeconomicinformationthrough
robo-advisorsisextremelyscarce(D’Acunto&Rossi2022b).
Robo-advicethatprovidesunbiasedmacroeconomicinformationcouldalsohelpsolvethere-
centdebateontheeffectivenessofpoliciesthataimtomanagehouseholds’expectationsthrough
communication(Coibion,Gorodnichenko&Kamdar2018).Communicationasanexpectations-
management tool is more effective when households trust the policymaking body (D’Acunto,
Fuster&Weber2021)andpoliciesaresimpleandintuitive(D’Acuntoetal.2021b),butitisless
effectivewhendeliveredthroughtraditionalmediasuchasnewspapers,whichhouseholdsbarely
trust(Coibion,Gorodnichenko&Weber2022).Robo-advisingtodeliverunbiasedinformation
aboutcurrentmacroeconomicvariablesandconsensusforecastsaboutfuturerealizationsofthe
samevariablescouldbeaneffectivewaytoincreasepolicymakers’successinmanagingexpecta-
tionsandchoices.Thisisnotonlyawidelyopenareaofinquirybutalsoonethatcoulddeliver
importantpracticalsuggestionsthatcanbeimplementedforpolicydesign.
3.REDUCINGDISTORTEDBELIEFS
Standardneoclassicaldecision-makersarealsoassumedtoformexpectationsrationally;theirbe-
liefsaboutfutureownandaggregateoutcomesare,onaverage,consistentwithexpostrealizations.
Contrarytothisbenchmark,householdstendtodisplaymultiplebiasesregardingbeliefsabout
theirown,others’,andmacroeconomicoutcomes.
550 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
In terms of their own outcomes, for instance, households tend to misestimate their sur-
vival probabilities,which leads them to make suboptimal choices about retirement savings and
insurancepolicies(Heimer,Myrseth&Schoenle2019).Moreover,manyhouseholdshavesystem-
atically distorted beliefs about their future income flows and income growth: They extrapolate
from recent income increases but not decreases and overestimate future income systematically
(see,e.g.,Cutler,Poterba&Summers1990;DeLongetal.1990;Greenwood&Shleifer2014;
Barberis et al. 2015; Gennaioli, Ma & Shleifer 2016; Barberis et al. 2018; Carroll et al. 2020;
D’Acunto,Weber&Yin2022).Atthesametime,morethanone-thirdofarepresentativepopu-
lationoverestimatesthelikelihoodofnegativeshocksandtheneedforprecautionarysavingsand
underspending relative to their capacity—a perceived precautionary savings motive that drops
whenhouseholdsreceiveinsuranceintheformofacreditline(D’Acuntoetal.2020).
Households display biased beliefs also when forming expectations about others—they tend
to overestimate others’ consumption and underestimate their saving rates, as discussed above
(D’Acunto,Rossi&Weber2019)—andfuturemacroeconomicvariables.Thesesystematicdistor-
tionsarecorrelatedwithdemographiccharacteristicssuchassocioeconomicstatus(Das,Kuhnen
&Nagel2020),cognitiveabilities(D’Acuntoetal.2019),age,andcohorts(Malmendier&Nagel
2016).Stango&Zinman(2023)provideataxonomyofmultiplebiasesinhouseholds’expectations
andbeliefsanddocumentcommonalitiesandcorrelationpatternsacrossthem,whichsuggeststhat
manybiasesinbeliefsmighthavecommonsources.Ultimately,beliefsappeartobemorebiased
forvulnerablehouseholds,whichmighthelpperpetuateeconomicinequalities.
3.1.BeliefsAboutOne’sOwnCharacteristics
Researchineconomicsandsocialpsychology,basedprimarilyonlaboratoryexperiments,hastack-
ledtheissueofreducingdistortionsinhouseholds’beliefsabouttheirownfuturecharacteristics
byusinggoalsetting—theprocessoflettinghouseholdsthinkaboutfuturepotentialstatesofthe
world,thelikelihoodofsuchstatesabsentanyinterventions,andthecommitmenttoincreasethe
likelihoodofthedesiredstateoftheworldbyestablishingitasagoal.Inthefield,Ashraf,Karlan
&Yin(2006)showthatindividualswithpreferencesthatdisplayahigherdegreeofhyperbolic
discountinghaveahigherprobabilityofopeningsavingsaccountsthatrestrictaccesstosaving
goalsuntiltheamountsavedachievesacertainthreshold.Theauthorsshowthatadoptinghard
goalsofthistypeincreasesthehouseholds’savingrate.
Goal setting is a primary tool robo-advisors use to reduce the impact of households’ biased
beliefsabouttheirfutureincomeflowsanddebtrepaymentability.Gargano&Rossi(2020)study
anItalianrobo-advisorandfindthatthepracticeofgoalsettingtomanagespendingandsaving
isadoptedwidelywhenoffered:Forty-onepercentoftheuserswhohaveaccesstogoalsetting
useitonacontinuousbasis.Inadifference-in-differencesanalysisbasedonanaturalexperiment,
Gargano & Rossi (2020) estimate an intention-to-treat effect of goal setting on savings of €20
permonthandalocalaveragetreatmenteffectof€60permonth,foranaverageincomeofthe
robo-advisor’susersof€1,200permonth.Theauthorsalsoshowthatgoalsettingisparticularly
effective for individuals who the literature has identified to be at risk of not saving enough for
retirement,whodisplayhighimpatience(Laibson1997),lowlevelsofeducation(Cole,Paulson
&Shastry2014),lowincomeandsocioeconomicstatus(Banerjee&Duflo2011,Kuhnen&Miu
2017),andinattention(Karlanetal.2016).
Gargano & Rossi (2020) also show that goal setting through robo-advising tools motivates
users to save more because once users set a certain state of the world as the one they want
to reach (goal), they monitor the robo-advisor often to increase the probability that the state
is reached.Goal setting thus increases the likelihood of reaching a valuable future state of the
www.annualreviews.org (cid:129) Robo-Advice 551

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
worldbyremindingusersoftheirstatedbeliefsregularlywhiletheymakeconsumptionandsaving
choices.
Whether households are aware or naive about their biases is central to assessing the effec-
tiveness of a solution like robo-advising, which requires active adoption by users, relative to
a nudge or default option, which exploits households’ inattention and/or inertia in economic
decision-making.Researchershaveusedrobo-advisingtoassessbiasawarenessand,consequently,
households’assessmentofthevalueofrobo-advisors.Tothisaim,Chaketal.(2022)implement
arandomizedcontroltrialintherealmofrobo-adviceforhouseholddebtmanagement.House-
holdsarefirstlefttotheirownmeanstosolvethreedebtmanagementproblemscenarioswhereby
theyallocateagivendisposableincometotherepaymentofseveraldebtaccountswhosefeatures
(e.g.,interestrates,minimumfees,late-feepayments)vary.Someusersarethenrandomlyoffered
thehelpofarobo-advisorforallocationsuggestions,and,withinthisgroup,someareprovided
robo-adviceforfree,andothershavetoindicatetheirwillingnesstopay(WTP)forthetool.Note
thatrobo-advicefordebtmanagementisaprimaryapplicationofautomatedadvicebecause,con-
trarytochoicesunderriskanduncertaintysuchasinvestmentdecisions,debtrepaymentchoices
haveauniqueoptimalsolutionthatdoesnotdependonhouseholds’preferences,beliefs,orother
characteristics.
Chaketal.(2022)findthattheaveragesubjectwhoisofferedtherobo-advisingtoolforacost
expressesaWTPaboveandbeyondtheactualmonetarybenefitsthesubjectobtains:1Theaverage
WTPishigherthantheaverageamountsubjectsleftonthetablewhenmakingchoicesunassisted
relativetotheoptimalsolutions.Thisresultsuggeststhathouseholdsarelikelysophisticatedabout
theirinabilitytoassessoptimaldebtrepaymentstrategies.
3.2.BeliefsAboutOthersandtheMacroeconomy
Asdiscussedintheprevioussection,providinghouseholdswithunbiasedandrepresentativein-
formation about others’ spending affects choices. This effect acts through a beliefs channel:
Households must have misestimated the spending of others if observing unbiased information
changestheirbehaviorinthedirectionoftheirpeers’choices(D’Acunto,Rossi&Weber2019).
Robo-advisors reduce biased beliefs about others’ outcomes not only in the realm of
consumption–saving choices but also in investment. D’Acunto,Ghosh & Rossi (2022) study a
robo-advisorfordebtinvestmentbyhouseholdsintheformofprovidingloanstoborrowersona
peer-to-peerplatform.Thisformofinvestmentrequiresthatlendersformbeliefsaboutpotential
borrowers’probabilityofdefaultandexpectedcashflowstoassesstheexpectedreturnsfromal-
ternativeloanrequests.D’Acunto,Ghosh&Rossi(2022)firstdocumentthatinvestorsuserules
ofthumbbasedonculturalnormswhenassessingtheviabilityofborrowersthatbelongtoalter-
nativesocialgroupsbutareotherwiseobservationallysimilar.Theyfindevidenceforanin-group
versusout-groupbias,wherebylenderswhobelongtoasocialgroupunderestimatetheprobabil-
ityofdefaultbyborrowersfromthesamesocialgroup,andanimplicitbias,wherebyalllenders
overestimatetheprobabilityofdefaultbyborrowersfromaheavilydiscriminatedsocialgroup,
includingthemembersofsuchgroup.
Ifthesedistortedbeliefsweredrivenbylenders’consciouswillingnesstodiscriminateagainst
the social groups they disliked,even if at a cost,lenders would not choose the borrowers sug-
gestedbyarobo-advisingtoolthatdidnotengageindiscrimination.Bycontrast,iflendersused
stereotypical rules of thumb to form beliefs but were aware that their beliefs might be inac-
curate (inaccurate statistical discrimination),they would follow the suggestions of an unbiased
1TheauthorsimplementaBecker–DeGroot–MarschakmechanismtoelicittruthfulWTPbyagents.
552 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
robo-advisor.D’Acunto,Ghosh&Rossi(2022)findthatthesameinvestors/lendersstartprovid-
ingfundingtoborrowersfromgroupstheywerelesslikelytochoosebeforeadoptingrobo-advice
andstopprovidinglendingtoborrowersbelongingtotheirownsocialgroup,whoseprobability
ofdefaulttheyunderestimatedbeforeadoptingrobo-advice.
Asfarasbeliefsaboutaggregateoutcomesareconcerned,Capponi,Olafsson&Zariphopoulou
(2022)studytheeffectsofarobo-advisorthatprovidesunbiasedexpectationstouserswithrespect
tostockmarketreturnandtherisk–returntrade-offofequityinvestments.Theauthorsfindthat
robo-advisingimprovestheSharperatioandreturnofhouseholds’riskyportfolios,especiallyin
timesofeconomicdownturns,whenhouseholdshaveexcessivelynegativeexpectationsaboutfu-
turemarketreturnsandtendtoreducemarketexposure,whereasmaintainingmarketexposure
wouldbeespeciallyprofitablegiventhemorefavorablerisk–returntrade-off.D’Acunto,Prabhala
&Rossi(2019)furtherdocumentthatrobo-advicevirtuallyeliminatesasetofbiasesinindivid-
ualinvestors’decision-makingthathavebeenattributedtononstandardbeliefsaboutaggregate
andindividualstockreturns,suchastrendchasing,thedispositioneffect,andtherankeffectin
trading.
4.REDUCINGTRANSACTIONCOSTS
Tooptimizefutureconsumptionthroughwealthaccumulation,standardportfoliooptimization
modelspredictthatvirtuallyeveryhouseholdshouldparticipateinequitymarketsbyinvestinga
fractionoftheirsavingsaslongasparticipationcostsareminimal.Conversely,anextensiveliter-
atureineconomicsandfinancehasproposedparticipationcostsasapotentialexplanationforone
ofthemostcommonfindingsinhouseholdfinancearoundtheworld—thestockmarketpartici-
pationpuzzle,wherebyasignificantfractionofhouseholdsdonotparticipateinthestockmarket
andmanyinvestsmallerfractionsoftheirwealththanpredictedbystandardmodels(Moskowitz&
Vissing-Jørgensen2002).2 Costscanalsoberelevantforconsumption/savingtransactions(Abel,
Eberly&Panageas2007)and,importantly,donotonlytaketheformofmonetarycosts.Indeed,
thecognitiveandpsychologicalcostshouseholdsfacetoconceptualizethehouseholdfinancepuz-
zlestheyface,todeterminethepotentialchoicestheycanmake,toassesstheirexpectedvalue,and
totaketheresponsibilitytoactaresubstantialandcompletelydismissedinsettingsthatassume
standardeconomicdecision-makers(Sweetetal.2013,Chaketal.2022).
4.1.MonetaryCosts
Monetarytransactioncosts,suchasthepriceofaspendingtransactionorstocktrade,havebeen
decliningoverthelastfewdecadesbutmightstillrepresentabarriertoparticipation,especiallyfor
themostvulnerablehouseholds(Reher&Sokolinski2021).Inlinewiththisargument,Philippon
(2019)proposesamodelinwhichacrucialfeatureofrobo-advisingandotherFinTechplatformsis
thattheycutmonetaryfinancialtransactioncosts.Philippon(2019)arguesthatFinTechplatforms,
whichincluderobo-advisors,shouldincreaseparticipationinequitymarketsandreducewealth
inequalitieswithinandacrosscountries.Reher&Sokolinski(2021)provideempiricalevidence
supportingthisargument.TheystudyaUSrobo-advisorforfinancialinvestmentsthat,duringthe
sampleperiodtheyobserve,cuttheminimumamountrequiredforaccess,whichistantamounttoa
2Several other explanations not based on participation costs have also been studied in the literature.For
instance,households’lackoffinancialliteracyandunderstandingoftheconceptofdiversification(Lusardi
&Mitchell2014)andhouseholds’lackoftrustinthestockmarketanditsparticipants(Guiso,Sapienza&
Zingales2009;Giannetti&Wang2016;Gurun,Stoffman&Yonkers2018;D’Acunto,Prokopczuk&Weber
2019;D’Acunto2021).
www.annualreviews.org (cid:129) Robo-Advice 553

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
dropinthecostsofparticipationbecausehouseholdsarerequiredtomaintaintheminimumvalue
ontheiraccountratherthanusingsuchresourcesotherwise.Reher&Sokolinski(2021)showthat
theshareofhouseholdsowningequitiesincreasesafterthisinterventionandthattheperformance
oftheirportfolios,whicharerobo-advised,improves.Becausethistypeofinterventiondoesnot
affectwealthierhouseholdsthatinvestedmorethantheminimumbeforethechange,thebenefits
arefullyconcentratedamongmiddle-classandpoorerhouseholds.
Researchshowsthatwhetherrobo-advisorsprovidebenefitsintermsofexecutioncostsde-
pendsontheirdesign.US-basedrobo-advisorsforfinancialinvestments,whichshouldbemore
appropriately labeled robo-managers,require an investor to commit cash to an account that is
managedautomatically,includingdecisionstotradeandrebalancetheportfolio,whichtypically
happensatprespecifiedtimes(Reher&Sun2019,Rossi&Utkus2020b).
Otherformsofrobo-adviceprovidesuggestionsbutrequirehouseholdstomakeactivedeci-
sions.Theserobo-advisorsareclosertotheroleofatraditionalfinancialadvisorthantothatof
arobo-manager.D’Acunto,Prabhala&Rossi(2019)studysucharobo-advisorinIndia,which
was introduced by a large brokerage house, alongside traditional human advisors. They show
that robo-advice,on average,improves the performance of households’ portfolios,and the im-
provementisdrivenalmostentirelybyinducinghigherportfoliodiversification,whichreduces
portfoliovolatility.Forthisreason,theaverageperformanceimprovementisentirelycapturedby
households whose portfolios were undiversified before adoption (even though human financial
advisorsalreadyhelpedthesehouseholds).D’Acunto,Prabhala&Rossi(2019)findthatdiversi-
fied households not only face no performance improvement but perform worse after adoption
because they use the robo-advisor often, which increases their trading fees relative to before
adoption.
Eveninthecaseofrobo-managers,thebenefitsofaccessingrobo-advicevaryacrossdemo-
graphics.Rossi&Utkus(2020b)usemachine-learningtechniquestounderstandwhichinvestors’
demographicandportfoliocharacteristicspredicthigherperformanceimprovementunderrobo-
advice.Thecashshareandtradingvolumeatadoptionarepositivelyrelatedtotheimprovement
in performance after access to robo-advice, indicating that investors who traded often and/or
heldalargeportionoftheirwealthincashbenefitedmostfromrobo-advice.Theauthorsalso
findthattenure,thepercentageofwealthinvestedinmutualfunds,andthepercentageofmutual
fundholdingsinindexedfundsarenegativelyrelatedtothebenefitsfromrobo-advice.Finally,
they find a positive monotonic relation between the share of equities held and the benefits of
robo-advice,becausetheportfoliooffundsinwhicharobo-managerinvestshashigherrisk–return
trade-offsthandoestheportfoliomanagedbytheaverageinvestor.
Reducing execution costs not only is a feature of robo-advisors for investment but also is
commonamongrobo-advisorsforconsumption.Researchershavestudiedtheeffectsofmobile
wallets—applications that provide households with the ability to engage in low-cost electronic
spendingtransactions,andproviderobo-advisingfeatures.Agarwaletal.(2020)findthatadopt-
inglow-costtransactionmobilewalletsincreasesthespendingcapacityofIndianhouseholdsby
3%foreach10-percentage-pointdependenceoncashfortransactionsbeforeadoption.Agarwal
etal.(2020)alsodetectapotentialundesirablefeatureofrobo-advisingforconsumption:House-
holds’higherspendingcapacityafteradoptionisdueatleastinparttotheincreasedsalienceand
lowersearchcostsforconspicuouspurchaseopportunities.
Lower transaction costs when using robo-advisors for consumption not only aligns house-
holds’ behavior with the predictions of standard economic models but also has business cycle
effects.Agarwaletal.(2019)andAgarwaletal.(2022)showthatthediffusionofamobilewal-
letinSingapore,whichreducedspendingtransactioncostssubstantially,increasedsalesgrowth
disproportionately for new and small businesses, which are responsible for most employment
554 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
growth in the United States and abroad (Haltiwanger,Jarmin & Miranda 2013).These aggre-
gateeffectsofFinTechandrobo-advisingadoptionarelikelytobeespeciallyhighinemerging
countries,asAgarwaletal.(2022)andCrouzet,Gupta&Mezzanotti(2022)document,exploiting
thesudden2016Indiandemonetizationeventasashocktotechnologyadoption.
4.2.CognitiveandPsychologicalCosts
Thecostshouseholdsfacetoexecuteeconomictransactionscanalsobecognitiveandpsycholog-
ical.Evenifhouseholdsfullyunderstoodtheeconomicproblemstheyfacedandwerecapableof
obtainingclose-to-optimalsolutions,conceptualizingsuchproblemsanddeterminingtheirsolu-
tionsrequiretheuseofcognitiveskillsandtime,bothofwhicharescarceresources(Abel,Eberly
&Panageas2013).Householdsoftenlackthecognitiveskillsandeconomicornumericalliteracy
neededtounderstandandsolveeconomicproblems,whichincreasesthecognitivecostsofmaking
decisions(Lusardi&Mitchell2014).Cognitiveabilitiesalsopredictthewedgebetweenhouse-
holds’choicesandstandardneoclassicaloptimalsolutionsforforecastingeconomicvariablesand
makingeconomicdecisions(D’Acuntoetal.2022).Moreover,alargelineofworkinbehavioral
economics has documented that the complexity of choices whose subtleties consumers cannot
fullygraspcanleadtochoiceavoidance(Iyengar&Lepper2000)andinertiaindecision-making
(O’Donoghue & Rabin 1999,Madrian & Shea 2001),hence suboptimal choices relative to the
onesofastandardneoclassicalagent.
Bysimplifyingthedecisionprocessandmakingthefuturepotentialbenefitsofactivechoices
more clear and tangible,robo-advice can reduce cognitive costs,psychological costs,and iner-
tia in decision-making.For instance,Bianchi & Brière (2021) study a French robo-advisor for
employees’savingsaccountsthatprovidesasalienttargetforportfolioallocationsthatinvestors
canobserveatanytime.Theyfindthatrobo-adviceincreasesattentiontoone’saccount.Inturn,
higherattentionleadstohigherrisk-adjustedreturnsandlowervolatility(Gargano&Rossi2018).
Moreover,thesalientgraphicaltargetdepiction,whichtherobo-advisorcomputesautomatically,
reduces the cognitive costs of assessing whether and to what extent portfolio allocations devi-
atefromanoptimalbenchmark.Thisdropinthecognitivecostsofelaboratingtheoptimization
problemandmappingthesolutionintoaninvestmentactionreducesinvestors’inertiainfinancial
decision-making and leads to more frequent portfolio rebalancing, which induces higher risk-
adjustedreturnsrelativetounassistedportfolios.Bianchi&Brière(2021)findthatthebenefitsof
robo-advicearehigherforinvestorsholdingsmallerportfoliosanddisplayinglowerstockmarket
participation before adoption,which presumably represent less wealthy and lower-income em-
ployees.Reducingcognitivecoststhroughrobo-advicethushasthesamepotentialdistributional
consequences as reducing monetary transaction costs—it encourages participation and wealth
accumulationbymorevulnerablehouseholds.
Psychological costs for households facing financial and economic decisions,including anxi-
ety and fear of disappointment in case of bad outcomes,are nonnegligible (Sweet et al.2013).
Gennaioli,Shleifer&Vishny(2015)modelthemoneydoctorroleoffinancialadvisors,whore-
duce psychological costs and lead investors to take on more risk,and Linnainmaa et al.(2022)
provideempiricalevidenceinmicrodataconsistentwiththismodel.InSection4.1,weinterpreted
thefactthathouseholdshaveahighWTPforrobo-advicefordebtmanagementrelativetothe
monetarybenefitstheyobtainfromswitchingtorobo-adviceasevidenceofhouseholds’awareness
oftheirownbiases(Chaketal.2022).Anonbeliefs-basedinterpretationisthathouseholdsmight
correctlyassesstheirabilitytofindoptimaldebtrepaymentstrategies,butthecognitiveandpsy-
chologicalcoststodosoleadthemtobewillingtooverpaytoobtainanautomatedrobo-advisor
andavoidfacingtheproblemaltogether.
www.annualreviews.org (cid:129) Robo-Advice 555

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
5.OPENQUESTIONS
5.1.LearningFromRobo-Advice
Whether households learn about their biases and how to correct them after being exposed to
robo-adviceisawide-openquestionandonethathasimportantpolicyimplications.Withlearn-
ing,access to robo-advice would not need to be repeated over time,and robo-advisors’ role of
transforminghouseholdsintostandardeconomicdecision-makerswouldbequiteeffective.The
effectivenessofrobo-advicewouldbeenhancedifitproducedspillovereffectsoflearningaboutbi-
asesandhowtocorrectthemacrossareasofeconomicdecision-making.Inthissense,robo-advice
could be interpreted as a means of delivery of financial literacy,which,contrary to traditional
financialliteracyprograms,ischeap:Itdoesnotrequirerecruitingandpayinginstructors,invest-
ingtimebyusers,orfacingcognitivecostswhentryingtoapplyabstractprinciplestoreal-world
choices.Instead,users learn by imitation during a time they would have anyway spent making
(oftenflawed)economicchoices.
This question is still open because most empirical settings so far include short time series:
Robo-advisors,especiallyinareasdifferentfromportfoliomanagement,haveonlyrecentlystarted
to diffuse. Currently, the evidence for learning is mixed. For instance, Chak et al. (2022) and
D’Acunto,Ghosh&Rossi(2022)donotdetectanylearningfromrobo-advicebyhouseholdsin
eitherdebtmanagementorpeer-to-peerlendingchoices,butHaoetal.(2022)dofindevidenceof
spillovereffectsofrobo-advice-basedcorrectionsininvestmentstrategiestononadvisedportfolios
bythesamehouseholds.Bianchi&Brière(2021)findthatrobo-adviceforretirementinvestments
increaseshouseholds’attentiontotheirownaccountsandtotradingstrategies,whichinprinciple
couldalsoimproveperformanceinnonadvisedinvestmentaccounts,whichareunobservedtothe
econometrician.
Moreresearchiswarrantedtounderstandwhethertheconflictingresultsintheliteraturearise
becauseofstudyingdifferenteconomicproblems,someofwhichmightbeeasiertosolvethan
others in different institutional settings,or because of other reasons.Empirical research needs
observationaldatainwhichmultiplefinancialaccountsofthesamehouseholdareobserved,of
which only some are robo-advised,and ideally,the assignment to robo-advice is quasi-random
acrossaccountsandwithinthehousehold.Alternatively,researchcouldusesettingsinwhichre-
searchersobserverepeatedchoicesbythesameuserofthesameaccount,forwhichrobo-advice
is intermittently available,so that one could assess whether exposure to robo-advice lets users
learnaboutbiasesandcorrectthem.Moreexperimentalresearchwouldhelpisolatethepotential
mechanismsthroughwhichhouseholdslearnfromthetransactionsfromonepartoftheirbalance
sheettootherparts,ifatall.
Economicpreferencesareanotherdimensionthatcouldbeaffectedbylearningfromtheinfor-
mationgatheredthroughrobo-advicebutthathasbeenlargelyneglectedbytheexistingliterature.
AswediscussedinSection3,mostexistingworkontheinformationprovidedtoconsumersvia
robo-advicehasfocusedonagents’beliefs.Inprinciple,though,robo-advicecouldshapeusers’
preferences, too. For instance, learning about the effects of diversification on a portfolio’s ex-
pectedreturnsandvolatilitymightchangeusers’riskappetiteandhencetheirchoicesunderrisk.
Researchthatcandisentangleeffectivelytherolesoflearningfromrobo-providedinformationin
consumers’preferencesandbeliefswouldprovideasubstantialcontributiontoourunderstanding
oftheconsequencesofthediffusionofrobo-advicearoundtheworld.
5.2.AlgorithmicAversionVersusAppreciationandInequalities
Thedriversofrobo-adviceadoptionarenotyetwellunderstood.Whereasresearchdesignson
theeffectsofrobo-advisingonchoicesaimtoobtainquasi-exogenousvariationintheprovisionof
556 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
robo-adviceacrossobservationallysimilarhouseholds,theextensivemarginofchoosingwhether
toadoptisimportanttoassesstheaggregateeffectsofrobo-advice.Mostexistingresearchbasedon
randomizedtreatmentwithrobo-advicefindsthatthelesssophisticatedhouseholdsbenefitmost
becausetheirunassistedchoicestypicallydepartmorefromstandardneoclassicalpredictions.Less
sophisticatedhouseholds,though,arelesslikelyandslowertoadoptnewtechnologiesduetoalack
ofawareness,distrustinunknownapplications,andotherreasons(Foster&Rosenzweig2010).If
truealsofortheadoptionofrobo-advice,theheterogeneouseffectsonperformanceconditional
onadoptionwouldbecounteracted.
Existingresearchprovidesmixedevidencefortheexistenceandheterogeneityofdistrustto-
wardalgorithms(algorithmicaversion)(Dawes1979).Inprinciple,thisformofdistrustcouldhave
severalsources,includingthelackofdirectaccessandcommunicationwithahumanand/orthe
lackofskillsneededtounderstandrobo-advisingprocesses(Rossi&Utkus2020a).Rossi&Utkus
(2020b)surveyalargerepresentativesampleoftraditionallyadvised,robo-advised,andunadvised
householdsandfindthatalgorithmicaversionisthemainpredictorofrobo-adviceadoption.They
alsoshowthataversionvariesdramaticallyacrossagegroupsandotherdemographiccharacteris-
tics.Ramadoraietal.(2022)estimateastructuralmodelthatcapturesinteractionsbetweenhuman
clientsandhybridrobo-advisorsthatofferdifferentformsofhumancounselingtocomplementa
robo-manager.Themodelfeaturesthreedimensionsofalgorithmicaversion:aper-perioddisu-
tilityofdealingwiththealgorithm,pessimismaboutthealgorithm’sabilitytomanageassets,and
uncertaintyaboutthealgorithm’sperformance.Theauthorsfindevidencethatalgorithmaver-
sionisdrivenmainlybyongoingdisutilityanduncertaintyandthathumanadviceisimportant
especiallytoretainhouseholdsinvestedinequitiesduringmarketdownturns.
At the same time,a strand of research in social psychology argues that some households in
factdisplayformsofalgorithmicappreciation—theyprefertorelyonalgorithmsmorethanhu-
manswhenmakingdecisions.Logg,Minson&Moore(2019)findthatdecision-makersaremore
adherent to advice when they know it comes from an algorithm rather than a human,and this
istruealsoforforecastsofchoicesbasedonhumantaste.Algorithmicappreciationishigherfor
decision-makerswhoarenotusedtomakingforecastsintheirdailylivesandlowerforthosewhose
occupationsinvolvemakingforecasts.
Understandingtheconditionsunderwhichalgorithmicaversionorappreciationarisesallows
forassessingwhetherrobo-advicecouldreduceratherthanincreasewealthinequalities.Algorith-
micaversionreducestheadoptionofrobo-advice,whichcouldexacerbatedifferencesinoutcomes
across the wealth and education distributions if more vulnerable households were more algo-
rithmicaverse.Algorithmicaversioncouldproducenewtypesofinequalities,suchasacrossage
groups.Understandingthedriversofalgorithmicaversionwouldalsohelpinformthedesignof
next-generationrobo-advisors.
5.3.Supply-SideIncentives:FinancialInstitutionsVersusThirdParties
Thisarticlehasfocusedontheeffectsofrobo-adviceonhumandecision-makingfromtheusers’
pointofview,buttheextenttowhichtheincentivesofthesuppliersofrobo-adviceservicesmight
affectthecharacteristicsandconsequencesofrobo-adviceisalsoanimportantopenquestion.
Applicationsstudiedintheliteratureaswellasexistingcommercialapplicationsinthefield
areprovidedeitherbyfinancialinstitutions,suchasbanksandcreditcardcompanies,orbythird
partieswhosemainbusinessaimistheprovisionofrobo-advice.Inseveralapplications,financial
institutionsfaceatrade-offthatthird-partyprovidersdonotface:Ontheonehand,cateringto
userswhodisplaybehavioralbiasesindecision-makingincreasestheirrevenuesandprofits.For
instance,creditcardcompaniesbenefitfromthefactthatusersdonotfullyrepaytheirbalancesat
www.annualreviews.org (cid:129) Robo-Advice 557

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
theendofeachcycleandenduppayinghighinterestandpotentiallatefees.Consistently,credit
cardcompaniesscreenforclients’behavioralbiasestoexploitthem(Ru&Schoar2018)andmight
designconsumercontractsinwaysthatattractbiasedclients(DellaVigna&Malmendier2004).
Ontheotherhand,excessiveaccumulationofcreditcarddebt(andhenceofprospectiveinterest
andfeepayments)coulddrivehouseholdstodefault,whichwouldbedetrimentaltoprovidersin
termsofmissedrevenuesandregulatoryconcerns.Contrarytofinancialinstitutions,thirdparties
donotfaceadirectbenefitfrommaintaininghouseholds’biasesindecision-making,becausethey
donotearntheinterestandfeeshouseholdspayontheiraccounts.Ifanything,thebusinessmodel
ofthirdpartiesoftenreliesonsharingthebenefitsfromrobo-advisedchoiceswithusersbasedon
feesthataredirectlyproportionaltousers’outcomes,whichalignstheincentivesofthesupply
anddemandsides.
Todate,despitetheimportanceofthesedifferences,researchonwhetherandhowthenature
andincentivesoftheprovidersofrobo-adviceshapeitsdesignandeffectivenessisscant.Moreover,
the effects of the market for control of FinTech applications on the diffusion and effectiveness
ofrobo-advice,wherebytheshareholdersofthird-partyprovidersmighthaveincentivestoexit
theirequityinvestmentthroughsaletofinancialinstitutionsratherthanmarket-baseddiffused
ownership(Wang2018),areaninterestingandopentopicforfutureresearch.
5.4.BroaderImplicationsforEconomicsandSociety
We conclude this article by discussing a set of broader implications of robo-advice that beget
furtherresearchineconomics,finance,socialpsychology,sociology,law,andotherfields.
Intermsofbroaderimplicationsforeconomics,thisarticlehasadvancedtheviewthatrobo-
advicecanbeadisruptivefeaturefordecision-makinginthatitcantransformbiasedandinexpert
householdsintoagentsthatformbeliefsandactinlinewithstandardneoclassicalmodels.This
featurecouldhaveanimportantimpactonthedirectionoffutureresearchineconomics.After
developing standard neoclassical models in microeconomics and macroeconomics, the field of
behavioraleconomicshasdocumentedmanywaysinwhichdecision-makersinthefieldandthe
laboratory depart from the assumptions of such models. These results have fed back into the
originalstrandsofneoclassicaleconomicsandhavemotivatednewgenerationsofmicroeconomic
and macroeconomic theories that incorporate features of decision-making documented in the
field into representative- and heterogeneous-agent models in order to make the predictions of
suchmodelsmorerealisticandtoproducefurthertestableimplicationsthatwouldnotarisein
standard models. As robo-advice diffuses more and more widely, though, traditional standard
neoclassicalmodels,basedonwhichrobo-advisorsaredesigned,couldincreasetheirexplanatory
power for empirical patterns given that agents behave more in line with standard assumptions.
Understanding whether and how endowing households with robo-advice could make standard
modelsmorepredictiveofobservedoutcomesandhencerevivetheirrelevanceinanopenagenda.
Moreover,robo-advicecouldbeusedasapotentialsolutiontothelackofeffectivenessofeco-
nomicpoliciesthatrequireactivechoicesbyhouseholdstobefullytransmittedtotheeconomy.
Households’ biases often reduce the aggregate effects of policies simply because many house-
holdsthatcouldactinawaythatincreasestransmission(andwouldbenefitfromdoingso)are
unawareofordonotunderstandpolicies—theyactashumanfrictionsinthetransmissionofpol-
icy(D’Acunto,Hoang&Weber2022).Researchinmacroeconomicsandfinancehasstudiedaset
ofpotentialsolutions,suchaspolicycommunication(D’Acuntoetal.2020),thedesignofsim-
ple policies (D’Acunto et al.2022),and an increase in trust and attention to policy institutions
(D’Acunto,Fuster&Weber2021),tolimittheeffectsofhumanfrictions.Robo-advicecouldbe
acheapandeffectivemeansoftransmissionofpolicy:Mosthouseholdsaroundtheglobecanbe
accesseddirectlyviapersonaldevices.
558 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
Finally,animportanttrade-offthatcrossesseveralfieldsofresearchandbegetsfurtherinquiry
isthetensionbetweenfreedominindividualdecision-makinganddesigninginstrumentsthatal-
lowforsociallyoptimaleconomicchoices.Althoughexistingresearchisstilllimited,aswehave
arguedinthisarticle,theevidencesofarseemstosuggestthatrobo-advicehasthepotentialto
align households’ incentives with those of standard decision-makers,which might make policy
designandaggregateoutcomesmoreefficient.Atthesametime,thenatureofalgorithmicad-
vice,whichoftendoesnotincludeexplanationstohouseholdsorprovidesexplanationsthatmany
householdscannotunderstand,requiresthathouseholdsfollowandacceptitssuggestionsoften
without a full understanding of them.Over time,robo-advice could create conformity and de-
pendence on algorithmic indications,which,when paired with a lack of understanding of such
indications,mightreducecriticalthinking,inducesocialconformity,andreduceheterogeneities
in preferences and beliefs across individuals,which could have far-reaching implications across
manyaspectsofsociallife.Understandingthispotentialtrade-offandassessingitsprevalenceand
potentialrelevancearetwoofthemostimportantopenquestionsinthisarea.
6.CONCLUSIONS
Robo-advicehasthepotentialtotransformhouseholdsthatdisplayasetofbiasesandsuboptimal
decision-making processes across a wide range of economic problems into standard economic
agentsbyprovidingthemwithafullyinformedandrational-expectationbenchmarkthatcanbe
implementedcheaplyandthatcanbarelybeprovidedbyhumanadvisors.
Inthisarticle,wehaveemphasizedthatresearchonrobo-adviceisstillinitsinfancyandwehave
proposedopenquestionstodevelopthisagendainthedirectionofbetterunderstandingwhether,
how,and why robo-advice might achieve the goals indicated above. We have also argued that
robo-advicecoulddecreaseorwidenwealthinequalitiesacrossasetofdemographicdimensions.
Understandingthistrade-offisanimportantareaforfutureinquiryandonethatspeakstothe
policyimplicationsofalltheopenquestionswehaveindicatedinthisarticle.
Makingresearchersrealizethatrobo-adviceisnotamereFinTechapplicationtotheallocation
ofhouseholds’investmentportfolios,asthemediaandnormalparlancesuggest,butratherapo-
tentiallytransformationalforceacrossmostdimensionsofindividualeconomicdecision-making
thathasconsequencesforempiricalandtheoreticalresearchacrossseveralfieldsofeconomicsand
financeisthemainmessagecomingfromthisnascentliterature.
DISCLOSURESTATEMENT
The authors are not aware of any affiliations,memberships,funding,or financial holdings that
mightbeperceivedasaffectingtheobjectivityofthisreview.
LITERATURECITED
AbelAB,EberlyJC,PanageasS.2007.Optimalinattentiontothestockmarket.Am.Econ.Rev.97:244–49
AbelAB,EberlyJC,PanageasS.2013.Optimalinattentiontothestockmarketwithinformationcostsand
transactionscosts.Econometrica81:1455–81
AgarwalS,BasuD,GhoshP,PareekB,ZhangJ.2022.Demonetizationanddigitization.SSRNWork.Pap.
3197990
AgarwalS,QianW,RenY,TsaiH-T,YeungBY.2020.Therealimpactoffintech:evidencefrommobilepayment
technology.SSRNWork.Pap.3556340
AgarwalS,QianW,YeungBY,ZouX.2019.Mobilewalletandentrepreneurialgrowth.AEAPap.Proc.109:48–
53
www.annualreviews.org (cid:129) Robo-Advice 559

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
AndreP,PizzinelliC,RothC,WohlfartJ.2022.Subjectivemodelsofthemacroeconomy:evidencefrom
expertsandrepresentativesamples.Rev.Econ.Stud.89:2958–91
ArmantierO,BruinedeBruinW,TopaG,VanDerKlaauwW,ZafarB.2015.Inflationexpectationsand
behavior:Dosurveyrespondentsactontheirbeliefs?Int.Econ.Rev.56:505–36
AshrafN,KarlanD,YinW.2006.TyingOdysseustothemast:evidencefromacommitmentsavingsproduct
inthePhilippines.Q.J.Econ.121:635–72
BaileyM,DávilaE,KuchlerT,StroebelJ.2019.Housepricebeliefsandmortgageleveragechoice.Rev.Econ.
Stud.86:2403–52
BakerSR.2018.Debtandtheresponsetohouseholdincomeshocks:validationandapplicationoflinked
financialaccountdata.J.PoliticalEcon.126:1504–57
BanerjeeAV,DufloE.2011.PoorEconomics:ARadicalRethinkingoftheWaytoFightGlobalPoverty.NewYork:
PublicAffairs
BarberisN,GreenwoodR,JinL,ShleiferA.2015.X-CAPM:anextrapolativecapitalassetpricingmodel.
J.Financ.Econ.115:1–24
BarberisN,GreenwoodR,JinL,ShleiferA.2018.Extrapolationandbubbles.J.Financ.Econ.129:203–27
BernankeBS.2009.Reflectionsonayearofcrisis.SpeechpresentedattheFederalReserveBankofKansasCity’s
AnnualEconomicSymposium,JacksonHole,Wyoming,Aug.21
BianchiM,BrièreM.2021.Augmentinginvestmentdecisionswithrobo-advice.SSRNWork.Pap.3751620
Binder CC. 2017. Measuring uncertainty based on rounding: new method and application to inflation
expectations.J.Monet.Econ.90:1–12
BruinedeBruinW,VanderKlaauwW,TopaG,DownsJS,FischhoffB,ArmantierO.2012.Theeffectof
questionwordingonconsumers’reportedinflationexpectations.J.Econ.Psychol.33:749–57
BursztynL,EdererF,FermanB,YuchtmanN.2014.Understandingmechanismsunderlyingpeereffects:
evidencefromafieldexperimentonfinancialdecisions.Econometrica82:1273–301
CalvetLE,CampbellJY,SodiniP.2007.Downorout:assessingthewelfarecostsofhouseholdinvestment
mistakes.J.PoliticalEcon.115:707–47
CalvetLE,CampbellJY,SodiniP.2009.Measuringthefinancialsophisticationofhouseholds.Am.Econ.Rev.
99:393–98
CapponiA,OlafssonS,ZariphopoulouT.2022.Personalizedrobo-advising:enhancinginvestmentthrough
clientinteraction.Manag.Sci.68:2485–512
CarlinB,OlafssonA,PagelM.2023.Mobileappsandfinancialdecisionmaking.Rev.Finance27(3):977–96
Carroll CD, Crawley E, Slacalek J, Tokuoka K, White MN. 2020. Sticky expectations and consumption
dynamics.Am.Econ.J.Macroecon.12(3):40–76
Chak I,Croxson K,D’Acunto F,Reuter J,Rossi A,Shaw J.2022.Robo-advice for borrower repayment
decisions.Occas.Pap.61
CharlesKK,HurstE,RoussanovN.2009.Conspicuousconsumptionandrace.Q.J.Econ.124:425–67
CoibionO,GorodnichenkoY,KamdarR.2018.Theformationofexpectations,inflation,andthePhillips
curve.J.Econ.Lit.56:1447–91
Coibion O, Gorodnichenko Y, Knotek ES II, Schoenle R. 2020. Average inflation targeting and household
expectations.NBERWork.Pap.27836
Coibion O, Gorodnichenko Y, Weber M. 2022. Monetary policy communications and their effects on
householdinflationexpectations.J.PoliticalEcon.130:1537–84
ColeS,PaulsonA,ShastryGK.2014.Smartmoney?Theeffectofeducationonfinancialoutcomes.Rev.
Financ.Stud.27:2022–51
CrouzetN,GuptaA,MezzanottiF.2022.Shocksandtechnologyadoption:Evidencefromelectronicpaymentsystems.
Work.Pap.,NorthwesternUniv.,Evanston,IL
CutlerDM,PoterbaJM,SummersLH.1990.Speculativedynamicsandtheroleoffeedbacktraders.NBERWork.
Pap.3243
DaZ,HuangX.2020.Harnessingthewisdomofcrowds.Manag.Sci.66:1847–67
D’AcuntoF.2021.TeardownthisWallStreet:Anti-financerhetoricandinvestmentdecisions.SSRNWork.Pap.
3213904
D’AcuntoF,FusterA,WeberM.2021.Diversepolicycommitteescanreachunderrepresentedgroups.Work.Pap.
2021-95,Univ.Chicago
560 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
D’AcuntoF,GhoshP,RossiAG.2022.Howcostlyareculturalbiases?Evidencefromfintech.SSRNWork.Pap.
3736117
D’AcuntoF,HoangD,PaloviitaM,WeberM.2019.Cognitiveabilitiesandinflationexpectations.AEAPap.
Proc.109:562–66
D’AcuntoF,HoangD,PaloviitaM,WeberM.2020.Effectivepolicycommunication:targetsversusinstruments.
Work.Pap.,Univ.Chicago
D’AcuntoF,HoangD,PaloviitaM,WeberM.2021a.Humanfrictionsinthetransmissionofeconomicpolicies.
NBERWork.Pap.29279
D’Acunto F, Hoang D, Paloviita M, Weber M. 2022. IQ, expectations, and choice. Rev. Econ. Stud.
https://doi.org/10.1093/restud/rdac075
D’AcuntoF,HoangD,WeberM.2022.Managinghouseholds’expectationswithunconventionalpolicies.
Rev.Financ.Stud.35:1597–642
D’AcuntoF,MalmendierU,OspinaJ,WeberM.2021b.Exposuretogrocerypricesandinflationexpectations.
J.PoliticalEcon.129:1615–39
D’AcuntoF,MalmendierU,WeberM.2021.Genderrolesproducedivergenteconomicexpectations.PNAS
118(21):e2008534118
D’Acunto F, Prabhala N, Rossi AG. 2019. The promises and pitfalls of robo-advising. Rev. Financ. Stud.
32:1983–2020
D’Acunto F,Prokopczuk M,Weber M.2019.Historical antisemitism,ethnic specialization,and financial
development.Rev.Econ.Stud.86(3):1170–206
D’AcuntoF,RossiAG.2021.Robo-advising.InThePalgraveHandbookofTechnologicalFinance,ed.RRau,
RWardrop,LZingales,pp.725–49.Cham,Switz.:PalgraveMacmillan
D’AcuntoF,RossiAG.2022a.ITmeetsfinance:financialdecisionmakinginthedigitalera.SSRNWork.Pap.
4100784
D’AcuntoF,RossiAG.2022b.Newfrontiersofrobo-advising:consumption,saving,debtmanagement,and
taxes.InMachineLearninginFinancialMarkets:AGuidetoContemporaryPractice,ed.ACapponi,C-A
Lehalle,pp.9–28.Cambridge,UK:CambridgeUniv.Press
D’AcuntoF,RossiAG,WeberM.2019.Crowdsourcingfinancialinformationtochangespendingbehavior.CESifo
Work.Pap.7533
D’AcuntoF,WeberM.2022.Memoryandbeliefs:evidencefromthefield.Work.Pap.,Univ.Chicago
D’AcuntoF,WeberM,YinX.2022.Microfoundinghouseholddebtcycleswithextrapolativeexpectations.Work.
Pap.,Univ.ChicagoBoothSch.Bus.
DasS,KuhnenCM,NagelS.2020.Socioeconomicstatusandmacroeconomicexpectations.Rev.Financ.Stud.
33:395–432
DawesRM.1979.Therobustbeautyofimproperlinearmodelsindecisionmaking.Am.Psychol.34:571–82
De Long JB,Shleifer A,Summers LH,Waldmann RJ.1990.Positive feedback investment strategies and
destabilizingrationalspeculation.J.Finance45:379–95
DellaVignaS,MalmendierU.2004.Contractdesignandself-control:theoryandevidence.Q.J.Econ.119:353–
402
FosterAD,RosenzweigMR.2010.Microeconomicsoftechnologyadoption.Annu.Rev.Econ.2:395–424
GarganoA,RossiAG.2018.Doesitpaytopayattention?Rev.Financ.Stud.31:4595–649
GarganoA,RossiAG.2020.Goalsettingandsavinginthefintechera.SSRNWork.Pap.3579275
GarganoA,RossiAG,WermersR.2017.TheFreedomofInformationActandtheracetowardinformation
acquisition.Rev.Financ.Stud.30:2179–228
Gelman M,Kariv S,Shapiro MD,Silverman D,Tadelis S.2014.Harnessing naturally occurring data to
measuretheresponseofspendingtoincome.Science345:212–15
GennaioliN,MaY,ShleiferA.2016.Expectationsandinvestment.NBERMacroecon.Annu.30:379–431
GennaioliN,ShleiferA,VishnyR.2015.Moneydoctors.J.Finance70:91–114
Giannetti M, Wang TY. 2016. Corporate scandals and household stock market participation. J. Finance
71:2591–636
GreenwoodR,ShleiferA.2014.Expectationsofreturnsandexpectedreturns.Rev.Financ.Stud.27:714–46
GuisoL,SapienzaP,ZingalesL.2009.Culturalbiasesineconomicexchange?Q.J.Econ.124:1095–131
www.annualreviews.org (cid:129) Robo-Advice 561

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
GurunUG,StoffmanN,YonkerSE.2018.Trustbusting:theeffectoffraudoninvestorbehavior.Rev.Financ.
Stud.31:1341–76
HaltiwangerJ,JarminRS,MirandaJ.2013.Whocreatesjobs?Smallversuslargeversusyoung.Rev.Econ.Stat.
95:347–61
HanB,HirshleiferD,WaldenJ.2019.Visibilitybiasinthetransmissionofconsumptionbeliefsandundersaving.
NBERWork.Pap.25566
HaoR,HuC,XuX,ZhangY.2022.Beyondperformance:thefinancialeducationroleofrobo-advising.SSRNWork.
Pap.4230191
Heimer RZ, Myrseth KOR, Schoenle RS. 2019. Yolo: mortality beliefs and household finance puzzles.
J.Finance74:2957–96
HirshleiferD.2020.Presidentialaddress:socialtransmissionbiasineconomicsandfinance.J.Finance75:1779–
831
IyengarSS,LepperMR.2000.Whenchoiceisdemotivating:Canonedesiretoomuchofagoodthing?
J.Personal.Soc.Psychol.79(6):995–1006
KaldaA.2020.Peerfinancialdistressandindividualleverage.Rev.Financ.Stud.33:3348–90
KarlanD,McConnellM,MullainathanS,ZinmanJ.2016.Gettingtothetopofmind:howremindersincrease
saving.Manag.Sci.62:3393–411
KarlssonN,LoewensteinG,SeppiD.2009.Theostricheffect:selectiveattentiontoinformation.J.Risk
Uncertain.38(2):95–115
KuchlerT,StroebelJ.2021.Socialfinance.Annu.Rev.Financ.Econ.13:37–55
KuhnenCM,MiuAC.2017.Socioeconomicstatusandlearningfromfinancialinformation.J.Financ.Econ.
124:349–72
LaibsonD.1997.Goldeneggsandhyperbolicdiscounting.Q.J.Econ.112:443–78
LeeSK.2019.Fintechnudges:overspendingmessagesandpersonalfinancemanagement.SSRNWork.Pap.3390777
LeviY,BenartziS.2020.Mindtheapp:accesstofinancialinformationandconsumerbehavior.SSRNWork.Pap.
3557689
LinnainmaaJT,MelzerBT,PreviteroA.2021.Themisguidedbeliefsoffinancialadvisors.J.Finance76:587–
621
LinnainmaaJT,MelzerBT,PreviteroA,FoersterS.2022.Investorprotectionsandstockmarketparticipation:an
evaluationoffinancialadvisoroversight.Work.Pap.,IndianaUniv.,Bloomington
LoggJ,MinsonJ,MooreD.2019.Algorithmappreciation:Peoplepreferalgorithmictohumanjudgement.
Organ.Behav.Hum.Decis.Proc.151:90–103
LusardiA,MitchellOS.2014.Theeconomicimportanceoffinancialliteracy:theoryandevidence.J.Econ.
Lit.52:5–44
MadrianBC,SheaDF.2001.Thepowerofsuggestion:inertiain401(k)participationandsavingbehavior.
Q.J.Econ.116(4):1149–87
MalmendierU,NagelS.2016.Learningfrominflationexperiences.Q.J.Econ.131:53–87
MaturanaG,NickersonJ.2019.Teachersteachingteachers:theroleofworkplacepeereffectsinfinancial
decisions.Rev.Financ.Stud.32:3920–57
Moskowitz TJ, Vissing-Jørgensen A. 2002. The returns to entrepreneurial investment: a private equity
premiumpuzzle?Am.Econ.Rev.92:745–78
MullainathanS,NoethM,SchoarA.2012.Themarketforfinancialadvice:anauditstudy.NBERWork.Pap.
17929
O’DonoghueT,RabinM.1999.Doingitnoworlater.Am.Econ.Rev.89(1):103–24
OlafssonA,PagelM.2018.Theliquidhand-to-mouth:evidencefrompersonalfinancemanagementsoftware.
Rev.Financ.Stud.31:4398–446
OlafssonA,PagelM.2022.Theostrichinus:selectiveattentiontofinancialaccounts,income,spending,andliquidity.
NBERWork.Pap.23945
OuimetP,TateG.2020.Learningfromcoworkers:peereffectsonindividualinvestmentdecisions.J.Finance
75:133–72
PhilipponT.2019.Thefintechopportunity.NBERWork.Pap.22476
RamadoraiT,RossiAG,UtkusS,WaltherA.2022.Algorithmaversion:theoryandevidencefromrobo-advice.
SSRNWork.Pap.4301514
562 D’Acunto (cid:129)Rossi

13:93:60
6202
yaM
40
,noM
:nO
05.91.94.72
:PI
)tseug(
tseuG
.gro.sweiverlaunna.www
morf
dedaolnwoD
Reher M, Sokolinski S. 2021. Automation and inequality in wealth management. Work. Pap., Univ. North
Carolina,ChapelHill
ReherM,SunC.2019.Automatedfinancialmanagement:diversificationandaccount-sizeflexibility.J.Invest.
Manag.17(2):63–75
RossiAG,UtkusSP.2020a.Theneedsandwantsinfinancialadvice:humanversusrobo-advising.SSRNWork.
Pap.3759041
RossiAG,UtkusSP.2020b.Whobenefitsfromrobo-advising?Evidencefrommachinelearning.SSRNWork.Pap.
3552671
RuH,SchoarA.2018.Docreditcardcompaniesscreenforbehavioralbiases?NBERWork.Pap.22360
StangoV,ZinmanJ.2023.Weareallbehavioral,moreorless:ataxonomyofconsumerdecision-making.Rev.
Econ.Studies90:1470–98
SunsteinCR.2017.Nudgesthatfail.Behav.PublicPolicy1:4–25
SweetE,NandiA,AdamEK,McDadeTW.2013.Thehighpriceofdebt:householdfinancialdebtandits
impactonmentalandphysicalhealth.Soc.Sci.Med.91:94–100
TangH.2019.Thevalueofprivacy:evidencefromonlineborrowers.Work.Pap.,HEC,Paris
ThalerRH,SunsteinCR.2009.Nudge:ImprovingDecisionsAboutHealth,Wealth,andHappiness.NewYork:
Penguin
WangX.2018.Cateringinnovation:entrepreneurshipandtheacquisitionmarket.SSRNWork.Pap.3247274
Weber M, D’Acunto F, Gorodnichenko Y, Coibion O. 2022. The subjective inflation expectations of
householdsandfirms:measurement,determinants,andimplications.J.Econ.Perspect.36:157–84
ZinmanJ.2015.Householddebt:facts,puzzles,theories,andpolicies.Annu.Rev.Econ.7:251–76
www.annualreviews.org (cid:129) Robo-Advice 563