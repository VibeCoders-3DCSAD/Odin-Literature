---
conversion_metadata:
  converted_at: "2026-07-21T08:37:56Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Schwartz.pdf"
  source_pdf_sha256: "556eb428a28019a8ca17a241635ff0fdc1142649a91334ae8e928bc37db51054"
  page_count: 61
  markdown_char_count: 297595
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

THE RISE OF A NUDGE: FIELD EXPERIMENT AND
MACHINE LEARNING ON MINIMUM AND FULL CREDIT
CARD PAYMENTS

Daniel Schwartz ∗

The minimum payment warning, a notice that informs credit
cardholders of the downside of making the minimum payment, has
been described as a perverse nudge because it negatively aﬀects
those who would pay more than the minimum, presumably due
to the anchoring bias. This issue is tackled in a massive ﬁeld
experiment by introducing a novel “statement balance warning.”
The experiment used email payment reminders that randomly
added minimum payment or statement balance warnings. Results
indicate that the messages shifted actual payment distribution
depending on the warning and that payments increased when
the statement balance warning was added.
The analysis is
combined with causal random forests to examine heterogeneous
treatment eﬀects, underlying mechanisms, and the optimum
policy in diﬀerent scenarios, and with an online experiment to
further examine conditions in which the warnings aﬀect payment
behavior. The statement balance warning makes debtors give
priority to paying a higher amount, which signiﬁcantly increases
payments by cardholders who are more likely to make deliberate
decisions every billing cycle and improves the understanding of the
consequences of not paying the statement balance. Furthermore,
the optimal policy to decrease interest charges or debt delinquency
indicates that cardholders should receive a combination of warning
messages depending on their payment history. The results provide
evidence that the statement balance warning oﬀers a new element
for ﬁnancial market regulation to improve the decision-making of
indebted households.

JEL: C93,D14,D91,G40
Keywords: ﬁnancial decision-making, debt, anchoring, causal
random forests, nudges.

Version: 28 Jan 2022
PLEASE DO NOT CITE OR CIRCULATE

∗ University of Chile, Beauchef 851, Santiago, Chile. daschwar@dii.uchile.cl.
Acknowledgements:

1

---

<!-- PAGE 2 -->

I.

INTRODUCTION

2

There are 2.8 billion credit cards in use around the world (Shift Processing, 2021). In the
United States alone, the outstanding credit card debt totals USD $1 trillion, and more than
40% of that ﬁgure is revolving debt – i.e., it accrued interest every month (El Issa, 2019),
and credit card debt keeps growing (Resendiz, 2020). This widespread use of credit cards
that may oﬀer a convenient payment method to households has also brought on ﬁnancial
distress for those who cannot manage their debt payment, which has been associated with
increased life dissatisfaction and poorer mental health (Norvilitis et al., 2006; Fitch et al.,
2011; Nelson et al., 2008; Hodson et al., 2014).1

Reasons for the increasing credit card indebtedness of households are not just based on
liquidity constraints but also on people encountering many diﬃculties in understanding the
information related to credit card payment (Soll et al., 2013; Gin´e et al., 2019). Previous
work has shown that consumer characteristics, such as inattention and ﬁnancial literacy,
beyond local regulation, are key to understanding household ﬁnancial distress (Keys et al.,
2020). However, many ﬁnancial literacy interventions have been proven to have no eﬀect
on people’s behavior (Fernandes et al., 2014).

As a partial solution, policy regulations in several countries (e.g., United States, United
Kingdom, Australia, and New Zealand) have included a mandatory minimum payment
warning in credit card statements.2 Even though these regulations aimed to reduce addi-
tional payments based on unpaid amounts, avoid a delinquent state and a vicious cycle of
higher payments, several studies have shown, using administrative data or laboratory-based
experiments, that highlighting the minimum payment may actually cause lower overall and
full balance payments (Hershﬁeld and Roese, 2015; Salisbury, 2014; Stewart, 2009; Wang
and Keys, 2014; Navarro-Martinez et al., 2011; Adams et al., 2018). For this reason, the
minimum payment saliency policy has been described as a perverse nudge (Wang and Keys,
2014; The Economist, 2008).

The reduction of payments due to the salience of the minimum payment has been com-
monly explained by the anchoring bias (Tversky and Kahneman, 1974): people’s tendency
to use the minimum amount as an anchor and insuﬃciently adjust their payment (e.g.,
Thaler and Sunstein, 2008; Stewart, 2009; Navarro-Martinez et al., 2011). Other research
has argued that this eﬀect may be triggered by the minimum payment acting as a target
value (Bartels and Sussman, 2016); people exert eﬀort to get to a speciﬁc amount. Re-
gardless of the explanation — anchoring bias or target value — research shows that the
minimum credit card payment drives cardholders’ payment behavior even when account-
ing for liquidity constraints and ﬁnancial distress (Guttman-Kenney et al., 2018; Keys and
Wang, 2019).

1After conducting a systematic review, Fitch et al. (2011) recognized the challenges in ﬁnding a causal path
between debt and mental health. Nonetheless, they conclude that “it would seem implausible that indebtedness
makes no contribution towards poorer mental health over time” (p. 163).

2In the United Kingdom, for example, “Please make sure your minimum payment is credited to your account by
the payment due date to avoid incurring a late fee, allowing up to 7 workings days for payment to clear. If you only
make the minimum payment each month, it will take you longer and cost you more to clear your balance.”

---

<!-- PAGE 3 -->

3

This paper examines a randomized, massive preregistered ﬁeld experiment introducing a
novel statement balance warning that indicates to debtors that they will avoid paying more
interest by paying in full. Credit card debtors received an email reminder to pay their credit
card a few days before it was due. The message randomly varied in 4 groups, a minimum
payment warning, a statement balance warning, both warnings, and no warnings. While
the minimum payment warning may push high-payers (low-payers) to decrease (increase)
the fraction they pay of their credit card bill, based on the previous literature on lab
experiments, a statement balance warning may encourage people who are able to pay more
than the minimum to pay a higher fraction. However, the statement balance warning may
discourage people who could only pay the minimum (or not oﬀer the correct information).
On the other hand, presenting both warning messages on the minimum and the statement
balance may drive low and high payers into a self-selection process to beneﬁt from both
warnings.

The ﬁndings indicate that any warning message decreases the likelihood of not paying at
least the minimum compared to a simple payment reminder without any warning, which
reduces credit card delinquency. On average, the warnings decrease the less-than-the-
minimum payments by debtors by 6.9 to 8.8 percent more than debtors who received the
simple payment reminder (an absolute diﬀerence of 0.7-0.9 percentage points). However,
to avoid revolving interest accruing because payments are not in full, the experiment’s
results highlight a signiﬁcant change in payment distribution depending upon the speciﬁc
warning message. First, debtors who received the statement balance warning are 1.0 - 1.1
percent more likely to pay in full than debtors who received the simple payment reminder
(a diﬀerence of 0.6-0.7 percentage points). Second, despite the large sample size, there is
no sizable change in the likelihood of paying in full for debtors who received the minimum
payment warning, but they increased the likelihood of paying the minimum payment by
6.3 percent compared to the simple reminder (a diﬀerence of 0.5 percentage points).

The change in payment distribution has signiﬁcant consequences on the interest charged
in the following billing cycle, depending on the type of warnings they received. First,
debtors who received a message including both warnings or only the minimum-payment
warning reduced their delinquent interest (i.e., the interest charged for not paying at least
the minimum) by 3.8 percent and by 3.2 percent more than those who received the message
with only the statement balance warning, and by 8.0 and 7.4 percent more, respectively,
than debtors who received the simple reminder. Also, consistent with the changes in pay-
ment distribution, there is a diﬀerence in the revolving interest charged (i.e., the interest
charged for paying less than the statement balance). Debtors who received both warn-
ings or only the statement balance warning reduced the revolving interest charges by 6.0
and 3.8 percent more, respectively, than debtors who received only the minimum warning
message, and 9.0 and 6.8 percent more, respectively, than those who received the simple
reminder. Therefore, changes in payment distributions due to speciﬁc warning messages
impact people’s additional payments.

In order to explore heterogeneous treatment eﬀects and explain underlying mechanisms,
the ﬁeld experiment was combined with a recently developed machine-learning technique,

---

<!-- PAGE 4 -->

4

causal random forests (Wager and Athey, 2018). This method uses high-dimensional func-
tions to examine heterogeneous treatment eﬀects, an “honesty” approach of resampling
observations, and a bootstrap of covariates to avoid overﬁtting and thus avoid some of the
shortcomings of reduced-form heterogeneity analysis. There are signiﬁcant heterogeneous
eﬀects. A large fraction of cardholders increase their payments because of the statement
balance warnings, and a small fraction of debtors might slightly reduce their payments in
full due to the minimum payment warning, although there is no clear signiﬁcant perverse
eﬀect. Diﬀerent factors explain a positive and large treatment eﬀect on payments when
messages include the statement balance warning: a considerable variation in how much of
their bill debtors usually pay - indicative of deliberation -, and whether they partially pay
their balance. Also, for the messages with both warnings, debtors increase their payments
when they see a relatively small gap between the minimum and the statement balance
amounts, suggesting that debtors can prioritize one warning depending on which becomes
more relevant and attainable. Finally, the results from the ﬁeld experiment are replicated
through an online experiment reﬂecting digital credit card payments that incorporates the
warnings. This online experiment shows that the statement balance warning signiﬁcantly
increases the likelihood of paying in full, and results do not seem to be explained by ﬁnan-
cial skills, ﬁnancial vulnerability, or people trying to override an otherwise incorrect quick
response. Instead, the warnings follow a cognitive path by helping cardholders improve
their understanding of ﬁnancial information.

This study makes several contributions. First, it contributes to the literature on min-
imum payment salience and minimum payment warnings in ﬁnancial decisions using the
ﬁrst well-powered randomized ﬁeld experiment. The use of a randomized experiment over-
comes the potential identiﬁcation problems of secondary-data analysis studies (Besley and
In addition, a natural
Case, 2000; Heckman et al., 1999; Kahn-Lang and Lang, 2020).
ﬁeld experiment is not subject to potential social desirability or Hawthorne eﬀects that
may confound results in lab experiments compared to those conducted in the ﬁeld (Galizzi
and Navarro-Martinez, 2019; Schwartz et al., 2020, 2021). Furthermore, previous research
has found that the anchoring bias varies from lab experiments to ﬁeld experiments as lab
experiments magnify the inﬂuence of anchoring (Jung et al., 2016). For example, using a
before-after analysis for the US 2009 CARD Act, Agarwal et al. (2015) found no sizable
change in overall payment when examining the same nudge highlighting an amount some-
what higher than the minimum payment examined in previous lab experiments. As an
exemption to the previous lab and observational studies in the minimum payment domain,
Seira et al. (2017) conducted a ﬁeld experiment in Mexico using multiple treatments. One of
their treatment messages highlighted the number of months needed for customers to pay oﬀ
their debt if only the minimum was paid. They found no signiﬁcant diﬀerence compared to
customers who received no message whatsoever (their control condition), but, as discussed
by the authors, it may be diﬃcult to ﬁnd sizable eﬀects given the sample size (about 12,900
in each treatment arm), in addition to the lack of a control condition with no minimum
payment salience. Without such a control condition, it is not possible to tease apart the ef-
fect of a payment reminder (positive, as shown in previous research (Homonoﬀ et al., 2018;

---

<!-- PAGE 5 -->

5

Arenas and Schwartz, 2021)) from the eﬀect of the minimum-payment salience/warning
(potentially negative).
In contrast, in this paper, the ﬁeld experiment’s control condi-
tion includes a message with no warnings, and it has a large sample size that increases
the study’s statistical power and helps examine heterogeneous treatment eﬀects useful to
public policy and scientiﬁc inquiry.

Second, this research proposes a novel solution to tackle the potentially perverse eﬀect
of minimum-payment salience highlighted in the literature and to help decrease household
debt. Households that pay the minimum end up paying more interest and it is possible
that they may never pay their debt. Several scholars have examined and proposed the
solution of increasing the minimum payment (Jiang and Dunn, 2013; Navarro-Martinez
et al., 2011). However, even with a higher minimum payment, consumers could still be less
likely to pay in full because of the minimum payment’s inﬂuence. Moreover, constrained
borrowers who beneﬁt from the minimum payment may end up delinquent, which would
decrease wellbeing. Separate from the credit card statements, Guttman-Kenney et al.
(2018) oﬀer an interesting solution of removing the minimum payment on a Website and
simulating an online payment in which choices are oﬀered (hypothetical decisions).
If
a participant wanted to pay less than the minimum, a prompt appeared displaying the
minimum payment. However, ﬁnancial institutions may be discouraged from implementing
this information ﬂow, and in many countries, there is still a relevant percentage of people
who do not pay online. The authors note that the UK’s Financial Conduct Authority tried
to run this study with lenders, but no one wanted to do it. The statement balance warning
approach is a palatable solution because lenders acknowledge that consumers deserve to
know the consequences of their actions. Moreover, the ﬁeld experiment for this paper was
implemented by a private ﬁnancial institution, and served as the basis for a regulation
proposal for all statement balances in a country with high credit card market penetration,
which is discussed in Section VII.

Third, the experimental setting contributes to the literature examining goals and targets.
Research has shown how the diﬀerent tenets of prospect theory’s value function (Kahneman
and Tversky, 1979) can aﬀect people’s motivation and eﬀort when one target is set (Heath
et al., 1999). For example, people should exert greater eﬀort for targets that are perceived as
attainable and little eﬀort for harder ones. In addition, psychology research postulates that
when there is a hierarchy of goals or targets, one goal is prioritized and non-prioritized goals
are ignored (Unsworth et al., 2014). Both sets of research predict that credit card payment
may depend on which target values are prioritized: if cardholders care about paying the
statement balance to avoid revolving interest, they will pay attention to the statement
balance warning and ignore the minimum payment warning. This paper’s ﬁndings suggest
that cardholders who have usually paid more than the minimum are more likely to increase
their payment under the statement balance warning, and those who have usually failed to
pay at least the minimum are more likely to increase their payment when receiving the
minimum-payment warning message. Because there is no empirical research examining this
type of dual or multi-level targets in real-world behavior, this paper will be the ﬁrst one to
study how people prioritize two-level targets using a behavioral response that may be useful

---

<!-- PAGE 6 -->

6

to ﬁnancial decisions and other domains. For example, ﬁeld research oﬀers one interesting,
popularized case using social norms in energy consumption with dual-target information
(e.g., Allcott and Rogers, 2014). Utility companies inform two amounts to customers:
one indicates the neighbors’ average energy consumption and the other the usage of the
most energy-eﬃcient households, so they do not demotivate those consuming less than the
average household (Schultz et al., 2007). However, there is no current examination of how
household responses may prioritize these two targets.

Fourth, this paper contributes to the literature using causal machine learning in eco-
nomics (Athey and Imbens, 2019). One crucial diﬀerence to most previous studies using
causal random forests is that they use existing randomized control trials to ﬁnd new hetero-
geneous eﬀects (e.g., Davis and Heller, 2017). However, almost all behavioral interventions
are designed to positively aﬀect the average person.3 In contrast, based on the perverse
nudge eﬀect of the minimum salience payment found in previous research, the ﬁeld exper-
iment in this research was designed to examine heterogeneous eﬀects.

Finally, this paper contributes to the research on consumer ﬁnancial markets, their reg-
ulation, and the role of behavioral biases (Agarwal et al., 2017; Campbell, 2016; Bhamra
and Uppal, 2019). In particular, this research contributes to credit card disclosure reg-
ulation, as promoted in several countries (the Credit Card Accountability Responsibility
and Disclosure Act in the U.S., Truth-in-Lending-Act in Mexico, Credit Contracts and
Consumer Finance Act in New Zealand, and the United Kingdom Lending Code, among
others). Campbell 2016’s Richard Ely Lecture emphasizes the consequences on welfare
and the economy with the rise of complicated ﬁnancial information: consumers fail to per-
ceive the consequence of their ﬁnancial decisions, either because of complex information,
lack of attention, hyperbolic temporal decisions, heterogeneous capabilities or hidden costs.
Credit card issuers targeting less-educated consumers also present a systematic challenge
to ﬁnancial markets and regulation (Ru and Schoar, 2016). This paper’s ﬁndings indi-
cate that income and share of debt with other lenders are not the main drivers behind
an increase in payments when cardholders receive the statement balance warning, which
provides a palatable regulation for a broad base of consumers. Additionally, regulating
the information communicated in the credit card billing process can produce substantial
beneﬁts without forbidding people’s indebtedness or increasing costs. The statement bal-
ance and minimum payment warnings transparently explain the consequences of paying
less than a certain amount, which should alleviate concerns about their implementation.
This is aligned with policymakers’ role of encouraging lenders to disclose borrowing costs
so that consumers make more informed debt repayment decisions.

The rest of the paper proceeds as follows. Section II describes the background information
on credit card debt, minimum payment, and payment information. Section III explains the
methods, including the data and the experimental design. Section IV presents the results
using a parametric analysis, and Section V focuses on heterogeneous treatment eﬀects using
causal random forests. Section VI examines diﬀerent underlying mechanisms and presents

3This point has been raised by Susan Athey on several occasions (e.g., talk given in the AI & Big Data in Finance

Research Forum on August 25, 2021).

---

<!-- PAGE 7 -->

7

additional analyses and experiments. Finally, Section VII concludes.

II. BACKGROUND INFORMATION

Credit cards are ubiquitous – nearly 3 billion around the world. Global statistics indicate
that Canada is the country with the largest share of the population owning a credit card
(83%), while the US (66%) and the UK (65%) are within the top 10 (Statista, 2017). In
Latin America, Chile is one of the leading countries in credit card usage, with 20.1 million
credit cards in a population of nearly 19 million people (Retail Financiero, 2019).

One of the most important measures related to credit card debt is the credit card delin-
quency rate. Delinquency is caused by missing one or more minimum payments, and it has
consequences on individuals’ credit scores and rampant debt. In the US alone, the 30-day
delinquency has varied from 6.8% in 2009 to 1.8% at the beginning of 2021, probably due
to the government ﬁnancial aid in the midst of the Covid-19 Pandemic, and the 90-day
delinquency rate continued increasing to 10% in 2021 (Board of Governors of the Federal
Reserve System, 2021). In Chile, where this paper’s main study takes place, two-thirds of
the credit cards are managed by retail credit card issuers. The delinquency rate for retail
credit cardholders was 8.4% in 2018, rising to 9.1% during mass protests in the last quarter
of 2019. It varied from 7.9% to 12.1% during the Covid-19 pandemic, also inﬂuenced by
the ﬁnancial aid to Chilean families (Retail Financiero, 2021).4

Financial regulations in many countries have established payment information that must
be presented by the credit card issuer. One key piece is the required minimum payment,
which is generally an amount equal to at least the sum of interest and fees accrued at the
moment of billing. However, credit card issuers have ﬂexibility in calculating the minimum
payment when it is greater than a required threshold. For example, some credit card issuers
use a percentage of the statement balance (e.g., between 1% and 3%) or a minimum amount
(e.g., $25) if the statement balance is less than the amount corresponding to the sum of
1% of the statement balance, interest and fees.5 Like in many countries, in Chile, credit
card issuers must have a minimum payment of at least the sum of credit card interest,
except “when the [required minimum] is waived for a speciﬁed period under a promotion
or oﬀer” (MinEcon, 2012). Compared to the US and the UK, whose minimum payment
ranges from 1% to 3%, credit card issuers vary their minimum payment by much more in
Chile (between billing cycles and among consumers). The credit card issuer involved in the
study, one of the leaders in Latin America, has an average minimum payment of 29% of the
statement balance (SD = 20%; M edian = 24%; Mean SDwithin = 13%). This variation
depends on consumers’ purchases (e.g., if the purchase was made using the credit card in
retail stores), making the minimum vary from $0 to the statement balance, although this
is unknown to the consumer.

4For this reference, the delinquency rate is calculated using loans for which payment is 30 days or more past due,
divided by total loans (the numbers are very similar to the delinquency rate using the customer base of the retail
credit card issuer in the ﬁeld experiment of this paper, which is one of the major players in the country). Bank
issuers have historically lower levels of delinquency rates.

5For examples of several credit card issuers in the U.S, see: https://creditcards.usnews.com/articles/how-credit-

card-issuers-calculate-your-minimum-payment.

---

<!-- PAGE 8 -->

8

As introduced in the previous section, several countries have required credit card issuers
to include a minimum payment warning. However, in the case of Chile, the current regu-
lation does not require any warning of that sort, and there is no evidence that any credit
card issuer is using one. On the other hand, on their websites, the Consumer Protection
Bureau and the Financial Market Commission attempt to alert people that paying less or
only the minimum may keep families in debt for a long time or from even paying their
debt, even if they stop using their credit cards, although it would be venturesome to say
that consumers are paying attention to this information.6

III. DATA AND EXPERIMENTAL DESIGN

III.A. Data and Sample Selection

In collaboration with a major Latin American retail credit card issuer, customer selection
was based on operational requirements and on increasing statistical power.7 The sample
inclusion criteria considered customers who had no automatic payment at the time of the
study, those who paid less than the statement balance at least twice in the previous 12
months, and those who were sent at least six emails by the retailer with an email opening
rate of at least 20% in the previous six months.8 The retailer requested the exclusion
of a very small percentage of long-term delinquent accounts treated by other programs.
Other sample selection criteria were merely operational: the email was uniquely assigned
to one customer, and customers had to have a minimum payment of at least $2.40 and a
statement balance greater than or equal to $12.0, so customers would have something to
pay and could distinguish between the minimum payment and the statement balance.9

The company provided anonymized customer information using the above criteria to
conduct a block randomization procedure using the minimum payment and statement bal-
ance, the percentage paid of the previous bill, and the number of times the customer paid
less than the statement balance in the previous twelve months. Then for each block, in-
dividuals were randomly assigned to four experimental conditions. The sample consisted
of 179,706 debtors with a total of 2,853,939 observations.10 There are almost two years of
data on most customers, from March 2018 to November 2019.11

6E.g., ”The minimum payment can be a lifetime debt” from https://www.sernac.cl/portal/604/w3-article-

1094.html, and https://www.cmfchile.cl/mascerca/601/w3-article-27871.html.

7Companies’ concern about consumers’ indebtedness is not uncommon. Some banks and credit card issuers
provide tools to their customers (e.g., “inControl”) so that they can limit their expenditures and control their
shopping behavior (Lieber, 2010).

8A third-party ﬁrm measures email opening rates, mainly retail oﬀers and promotions. Even though this measure
is not exact because it depends on particular email providers and email settings, it may be used as a proxy for
consumers opening the emails sent by the company.

9In American dollars adjusted by the Power Purchase Parity (PPP), using the exchange rate at the time of the

experiment.

10Forty-seven people were excluded. Of those, 44 had a credit line exceeding $48,114 (99.98th percentile), which
may represent a business credit line, and 3 had a negative payment amount (they may have had some sort of credit).
The Online Appendix shows the main results including these accounts.

11The company provided data for January-February 2018, but there were substantial missing values at the begin-

ning of the year.

---

<!-- PAGE 9 -->

9

III.B. Procedure

Customers received two email payment reminders ﬁve and two days before their credit
card payment was due. Emails were sent for one billing cycle during August and September
2019. All email subjects indicated the name of the customer: “[Name], [Credit card name]
has important information for you.” Previous research has shown that email opening rates
improve when including people’s names in the subject (Sahni et al., 2018). Also, all email
bodies included a reminder sentence, “We remind you that your [card name] is due on
[date].” Individuals were randomly assigned to four experimental conditions through the
block randomization procedure explained above (25% to each experimental condition). The
ﬁrst experimental condition (the “Minimum Payment Warning” condition, or “MinW”) in-
cluded a sentence about the minimum payment: “If you at least pay the minimum
([$]) before the due date, you will pay additional interest charges but avoid late
fees.”, similar to the minimum payment warning sentence used in several countries. The
second experimental condition (the “Statement Balance Warning” condition, or “SBalW”)
included a sentence about the statement balance: “If you pay the statement balance
([$]) before the due date, you will avoid additional interest charges.” The third
experimental condition (“Both Warnings” condition, or “BothW”) combined the previ-
ous two experimental conditions, including the statement balance and minimum payment
warnings.12 Finally, the fourth experimental condition (“Control”) was a pure reminder
with no statement balance or minimum payment warnings.13 All customers received their
credit card statements in a separate communication that included the statement balance
and minimum payment amounts. Statistical power calculation and the sentences were ﬁrst
tested in a pilot study with multiple treatments that showed that people reacted to the
warnings rather than to the speciﬁc amounts (see the Pilot Study and Table A1 in the
Online Appendix).14 The experiment was preregistered at the Wharton Credibility Lab at
the University of Pennsylvania (https://aspredicted.org/blind.php?x=gz9gw3).

III.C. Sample Characteristics and Balance Checks

Table I shows descriptive statistics and checks the balance across experimental conditions.
All conditions present very similar values for pretreatment variables, with no sizable statis-
tical diﬀerences. Debtors (female: 51.6%, 44.4 years old) received a credit card statement
in the treatment period with a statement balance and a minimum payment of $1,949 (SD

12Original sentences in Spanish: “Te recordamos que el pago de tu [card name] vence el [date].” Minimum warning:
“Si pagas al menos el Monto M´ınimo [$] antes de la fecha de vencimiento, pagar´as intereses pero evitar´as pagar gastos
de cobranza.” Statement balance warning: “Si pagas el Monto Total Facturado [$] antes de la fecha de vencimiento,
evitar´as pagar intereses adicionales.”

13The company reviewed the messages before they were launched to ensure that they were understandable. It also
asked that the statement balance amount be included if the minimum payment was included, even if it was at the
end of the email (so, the minimum payment was also included when adding the statement balance at the end of the
email). Customers received both amounts in their monthly statements.

14The online experiment in Section VI also provides evidence that people react to the warning sentences and not

to the amounts.

---

<!-- PAGE 10 -->

10

= 3,050) and $416 (SD = 529), respectively.15 Before the experiment, using all 2019 billing
cycles before the treatment period, debtors paid an average of 75.8% of their statement
balance. In addition, on average, 63.7% paid in full, 7.9% paid the minimum payment,16
and 8.2% did not pay or paid less than the minimum payment, leading to credit card delin-
quency, additional interest, and late fees. This percentage is also similar to the average
national delinquency rate for credit cards issued by retailers at the time of the study, as
described in Section II.

IV. CHANGES IN PAYMENT BEHAVIOR

This section examines the eﬀect of the warning messages on payment behavior, including
how shifts in payment distribution aﬀected interest payments. Equation 1 estimates the
eﬀect of the warning messages using an ordinary least square analysis with robust standard
errors clustered by individual (Bertrand et al., 2004).

(1)

yit = α +

(cid:88)

j

βjDij × Pt + δPt + Xit + µm + µy + ai + εit

where Dij is a dummy indicator for each warning message assigned to individual i com-
pared to the control (treatment warnings j = {Minimum, Statement Balance, Both}). Pt
is a dummy variable for before and after the treatment period for billing cycle t. The speci-
ﬁcation includes controls for changes in customers’ characteristics over time and before the
treatment (Xit: company’s internal credit score, income, purchases, statement balance and
the ratio between the minimum payment and statement balance of individual i in billing
cycle t), monthly and yearly ﬁxed eﬀect (µm and µy), and individual ﬁxed eﬀects (ai). The
error term is εit. βj indicates the average intention-to-treatment eﬀect of each warning
message as compared to the control condition. Because of randomized assignment, these
diﬀerence-in-diﬀerence estimators are unbiased (Rubin, 1974). The outcome variable (yit)
changes for each analysis; for payment variation, the speciﬁcation uses the logarithmic
transformation of payments of individual i in billing cycle t.17 For the probability of not
paying at least the minimum, which drives credit card delinquency, the outcome variable
is a dummy indicator equal to 1 if individual i in billing cycle t does not pay or pays less
than the minimum (0, if not). Similarly, for the probability of paying in full, the outcome
is a dummy variable that indicates whether the cardholder i pays in full in billing cycle
t. In these latter two cases, changes in probability are examined using a linear probability
model. Another measure of interest is the percentage paid, which is the proportion of the

15Because of conﬁdentiality, the payment information was re-scaled using a typical statement balance of $1,949.28
in the United States (Salisbury and Zhao, 2020). Therefore, the statement balance and minimum payment were
.
re-scaled by this value using debtors’ actual statement balances multiplied by F, where F =

)
16These debtors paid exactly the minimum amount or up to the next nearest 10,000 Chilean pesos (approx. $24
adjusted by PPP). If this variable considers the next nearest 100,000 Chilean pesos, the percentage of debtors paying
the minimum would be 15.8%.
17For the amounts, ln(X+1).

1,949.28
(cid:80)(statementbalancei)
N

(

---

<!-- PAGE 11 -->

statement balance paid by individual i in billing cycle t (yit ∈ [0,1]). Finally, using the
next couple of billing cycles after the treated billing cycle, two types of interest charged are
also used as outcome variables; revolving interest, which accrues when debtors pay at least
the minimum but less than the statement balance, and delinquent interest, which accrues
when debtors do not pay or pay less than the minimum.

11

IV.A. Main payment variation and its consequences

Table II shows the average treatment eﬀects of each condition using the control as the
baseline. The ﬁrst column shows that all warning messages increase payment amounts from
6.2% to 7.8% compared to the control condition, with no sizable statistical diﬀerences across
warnings. The second column indicates that the warnings reduce the probability of not
paying at least the minimum by 6.9% - 8.8% from a baseline of 9.7% (0.7-0.9 percentage
points), with the statement balance warning only condition oﬀering the smallest reduction,
but with no sizable statistical diﬀerence from the other warnings. This result translates
into a lower credit card delinquency rate because of the warnings. As a reference for these
magnitudes, the delinquency rate in Chile at the time of the experiment was 8.4% for
retail credit cards (Retail Financiero, 2019) and increased 3.7 percentage points in the
worst moment of the COVID-19 pandemic, which was an extreme situation.

For the probability of paying in full (third column), debtors who received a message
with the statement balance warning increased the likelihood of paying in full by 0.6-0.7
percentage points, which is an increase of 0.9% to 1.1% from a baseline of 62.5% (i.e., most
people paid in full under the control condition), which decreased the revolving interest
accrued by paying less than the statement balance. In contrast, there was no statistically
signiﬁcant change in the likelihood of debtors who received the minimum payment warning
paying in full as compared to the simple reminder (CI95% [-0.3 pp., 0.7 pp.]), i.e., not
clearly supporting previous lab evidence, although this result masks some heterogeneity
that will be examined in the next section. Moreover, debtors who received the minimum
payment warning only were 0.4 percentage points less likely to pay in full than those who
received the statement balance warning or both warnings.

The previous results have several consequences. First, the proportion paid of bills in
conditions that included the statement balance warning increased by 0.7 percentage points
compared to the plain remainder and by 0.4 percentage points compared to the minimum
payment warning condition (fourth column). Debtors who received the only minimum
payment warning did not pay a statistically sizable diﬀerent proportion of their bill com-
pared to the control condition. A more important consequence for household ﬁnance is the
interest that households ended up accruing in the billing cycle following the intervention,
depending on their payment behavior because of the warnings. Table II (ﬁfth column)
shows that debtors who received a message with the statement balance warning reduced
their revolving interest, which accrues on unpaid amounts above the minimum, by 6.8%
and 9.0% for the statement balance and both warnings conditions, respectively, compared
to debtors who received the simple reminder. Moreover, receiving the statement balance

---

<!-- PAGE 12 -->

12

warnings reduced the revolving interest more than for debtors who received the minimum
payment warnings only, by 3.8% and 6.0% for the statement balance and both warnings
conditions, respectively. Furthermore, consistent with column 3 of Table II, there is no
statistically signiﬁcant diﬀerence between debtors who received the minimum payment
warning and those who received the simple reminder on revolving interest.

Finally, Table II (last column) shows that all warning messages decreased delinquent
interest, i.e., interest accruing because of non-payment or payments below the minimum
in the billing cycle after the intervention. Speciﬁcally, debtors who received a message
including the minimum payment warning decreased revolving interest by 7.4% for the
minimum payment warning only condition and 8.0% for the both warnings condition,
compared to the control condition. Under these two conditions, debtors also paid less
revolving interest than debtors who received the statement balance warning only, by 3.2%
and 3.8%, respectively. These results indicate that the diﬀerent warnings aﬀect payment
distribution, with signiﬁcant consequences on how much and what type of interest debtors
end up accruing. Using both warnings simultaneously decreased the interest of people who
would not have paid at least the minimum and those who do not pay in full. Using one of
the warnings greatly aﬀected the speciﬁc interest charged, depending on the focus of the
warning.

IV.B. Payment distribution

To examine whether the previous result was in response to changes in payment distribu-
tion, Table III shows analyses using Equation 1, with diﬀerent payment values or ranges as
outcome variables. The ﬁrst column shows that all warning messages reduced the probabil-
ity of not paying at all compared to the control condition. Furthermore, it can be seen that
changes in payment distributions as a result of the warning messages came mainly from
a reduction in debtors who did not pay or who did pay but paid less than the minimum
(ﬁrst two columns). The question is where this reduction went and whether it depends on
the speciﬁc warning message.

For debtors who received the minimum payment warning only, Table III indicates that
they shifted their payment mostly toward the minimum amount (each row has to add up to
0). In particular, the third column shows that debtors who received this warning increased
the likelihood of paying the minimum by 6.3% compared to the control (or 0.5 percentage
points, with a baseline of 7.3%), i.e., 65.8% of the overall reduction in non-payment or in
paying less than the minimum went toward paying the minimum for debtors who received
the minimum warning only (0.52 pp. out of 0.79 pp.). In addition, Table III shows no
signiﬁcant changes in payments above the minimum for this group. This shift in payment
change due to the minimum warning can also be appreciated in Panel A of Figure 1 that
shows the average treatment eﬀects of Table III.

While payment changes shifted toward the minimum for the minimum payment warning
condition, payment changes in the conditions that included the statement balance warn-
ings shifted almost entirely toward full payment. For example, for the statement balance
warning condition, if the reduction in the likelihood of not paying at least the minimum is

---

<!-- PAGE 13 -->

13

aggregated with the change in the likelihood of not paying the minimum, the reduction is
0.79 percentage points. Eighty-one percent of that reduction went toward payment in full
(i.e., 0.64 pp. out of the 0.79 pp.), and the rest toward a revolving amount between the
minimum payment and the statement balance (Panel B in Figure 1).

Table III and Figure 1 (Panel C) show that debtors who received both warnings behave
very similarly to those in the statement balance warning condition, shifting 80% of the
reduction of not paying even the minimum or paying a revolving amount towards paying in
full. However, the remaining 20% went toward the minimum amount. In the both warnings
condition, debtors consistently increased their likelihood of paying the minimum compared
to debtors who received only the statement balance warning (statistical signiﬁcance at the
10% level in this case for the linear model and at 5% for the logit model in the Online
Appendix Table A2). Overall, these results show that the warning messages increased
payments by shifting their distribution consistent with the speciﬁc warning content.

The last two columns in Table III show whether cardholders paid the statement bal-
ance (rounded up to the nearest CLP 10,000) or paid more than that, even though there
is no economic beneﬁt of paying more than the statement balance (in the baseline, 6.8%
of debtors paid more than the statement balance).18 There is no statistically signiﬁcant
diﬀerence in the likelihood of paying more than the statement balance, although, direc-
tionally, there is a small reduction for debtors who received the statement balance warning
only compared to the control condition. Finally, Table A2, Table A3 and Table A4 in
the Online Appendix show that the main results are robust using a logit model, diﬀerent
speciﬁcations, or including accounts with large credit lines.

V. CAUSAL FORESTS AND HETEROGENEOUS TREATMENT EFFECTS

Machine learning methods have recently focused on causal inference, which oﬀers an op-
portunity for many economic problems (Athey and Imbens, 2017, 2019). The causal forests
method in particular is a machine-learning technique recently developed to examine het-
erogeneous causal eﬀects with high-dimensional functions of covariates, which allows be-
havioral mechanisms and optimal policies to be analyzed for multi-treatment cases (Athey
and Wager, 2021). This section shows the heterogeneous treatment eﬀect for each warning
message, which is especially relevant considering previous evidence on the perverse eﬀect
of the minimum payment salience. Then it characterizes the sub-samples with the largest
treatment eﬀects for each warning message and, ﬁnally, presents an optimal policy analysis.

V.A. Heterogeneous eﬀect

This part presents the heterogeneous eﬀect analysis using causal random forest models,
based on the Generalized Random Forests algorithm (Athey et al., 2019) to estimate the
conditional average treatment eﬀect (CATE). In regression or classiﬁcation trees, covariates
are used to split observations into branches to ﬁnd leaves that can predict treatment eﬀects
(Breiman and Stone, 1984), random forests solve individual tree inaccuracy and overﬁtting

18This behavior may be due to the convenience of paying subsequent installments in advance.

---

<!-- PAGE 14 -->

by ﬁrst aggregating trees using a bootstrap procedure with a sub-sample m of covariates
for each tree.19 Second, the algorithm selects a random subset of the sample for training
to determine the model parameters and another for testing to make the estimation (Athey
et al., 2019; Athey and Wager, 2019). Finally, individual tree treatment eﬀects are weighted
across the forest.

The CATE, τ D(x), conditional on debtors’ characteristics (x), is deﬁned for each warning

message, D = {Minimum, Statement Balance, Both}, as:

14

(2)

τ D(x) = E [Yi(1) − Yi(0)|Xi = x]

where Yi(1) is the potential outcome if debtor i would have been assigned to the warning
message D, and Yi(0) is the potential outcome if debtor i would have been assigned to the
control group. The causal forest algorithm averages individual predictions of each tree b
to produce out-of-bag CATE estimates (see details in Athey et al. (2019)).20 Wager and
Athey (2019) show that these CATE estimates are consistent and asymptotically normally
distributed. For further examination, observations can be ranked by their out-of-bag CATE
and grouped in subgroups (e.g., quintiles) to obtain valid conﬁdence intervals (Athey and
Imbens, 2016). The conditional average treatment eﬀect estimates within each subgroup
can then be obtained using Equation 3 for each warning condition:

(3)

yi = α +

(cid:88)

k=1

τkDwDi × nki +

(cid:88)

k=1

ϑknki + ui

where yi is the outcome variable, wDi is 1 if cardholder i was in the warning condition D
and 0 if i was in the control group. nki is a dummy variable equal to 1 if cardholder i
belongs to subgroup k (0 if not). τkD is the estimated conditional average treatment eﬀect
(CATE) for the kth subgroup in warning condition D compared to the control condition.
This process is repeated for each warning message and for each outcome variable. This
approach to characterize heterogeneous eﬀects has been used in other domains, such as the
evaluation of educational, parenting, and employment programs (Athey and Imbens, 2019;
Davis and Heller, 2017; Sylvia et al., 2021).

Table IV shows the results for the causal random forests sorted by the estimated CATE
using Equation 3 with diﬀerent dependent variables: whether cardholders paid in full
(“full payment”), whether they did not pay at least the minimum (“payment less than
the minimum”), and their payment as a percentage of the statement balance (“percentage
of full”), for each warning compared to the control condition. In most cases, all warning
treatments show signiﬁcant heterogeneity. For example, for cardholders who were in the
statement balance warning only condition, the top quintile indicates a conditional average
treatment eﬀect of 2.4 percentage points compared to the control group, i.e., one-ﬁfth of

19By default, in the Causal Forest algorithm, m =
20For each random forest, the algormithm uses 30,000 trees with 10 minimum observations per node, honesty with

p + 20, where p is the number of covariates.

√

0.5 splittings with the GRF 2.0.2 package in R.

---

<!-- PAGE 15 -->

15

the sample who received this warning increased their likelihood of paying in full by 2.4
percentage points more than debtors who received a reminder with no warning message (in
relative terms, this is an increase of 4.0% in the likelihood of paying in full, as indicated
in Table A5). This is almost four times the average treatment eﬀect found in the previous
section. For clarity of what follows, Table IV is discussed for each dependent variable. For
additional results, Figure A1 in the Online Appendix shows the complete distribution of
estimated CATE for each causal random forest, and Table A6 and Figure A2 show the
results for the causal random forests using combinations of warning message conditions.

Payment in full. Table IV shows that for the conditions that included the statement
balance warning, at least the top two quintiles signiﬁcantly increased their likelihood of
paying in full (the CATE coeﬃcients are at least more than 1.64 times their standard er-
rors). On the other hand, there is an enormous heterogeneity for cardholders who received
the minimum payment warning only; while only the top quintile increased the likelihood of
paying in full, most of the quintiles show conditional average treatment eﬀects not sizably
diﬀerent from the control group, and the ﬁrst quintile shows a reduction in the likelihood of
paying in full (a reduction of 0.8 percentage points, or 1.1%), although this is not statisti-
cally signiﬁcant even at the 10% signiﬁcance level. Its magnitude is similar to the ﬁndings
by Wang and Keys (2014), and it may suggest a small perverse eﬀect of the minimum
warning.21 Table IV also includes the estimates of the best linear predictors of the CATE
(Chernozhukov et al. 2018a, Chernozhukov et al. 2018b) using the out-of-bag predictions
for each causal random forest. The β1 coeﬃcient corresponds to the conditional average
treatment eﬀect. It also indicates how well the model is calibrated (a coeﬃcient equal to
1 represents a correct causal random forest prediction). β2 works as an omnibus test for
treatment eﬀect heterogeneity (the null hypothesis, β2 = 0, fails to ﬁnd underlying hetero-
geneity). The results of this analysis reaﬃrm that average treatment eﬀect predictions are
well-calibrated and heterogeneity is present for the warnings that include only one mes-
sage, in particular, for the minimum warning condition. The heterogeneity is weaker for
the both warnings condition, given the positive result for most quintiles.22

Payment less than the minimum. Table IV shows that for the likelihood of not paying
at least the minimum, which is associated with delinquency, the top quintiles for each
warning message indicate a reduction of 1.2 to 1.5 percentage points compared to the
control condition (a relative reduction of 5.8% to 15.5%). The warnings that include the
minimum payment warning message signiﬁcantly reduce the likelihood of not paying or
of paying less than the minimum for the top three quintiles. In contrast, the statement
balance warning does not show a sizable diﬀerence for the third quintile, and therefore fewer
debtors may have reduced their delinquent interest in the next bill. Importantly, results
suggest no indication that a relevant portion of cardholders would fail to pay at least the

21Wang and Keys (2014) also examined diﬀerent types of disclosures available for some US cardholders, including
the minimum payment warning and the payment calculation required to repay any debt in 3 years. They also found
that the minimum payment warning decreased delinquency and increased the likelihood of paying the minimum.

22The best linear predictor of the CATE uses the out-of-bag predictions, ˆτ −i(Xi), to estimate Yi = β1Di ¯τ +
(cid:0)ˆτ −i(Xi) − ¯τ (cid:1) + εi, where D is the warning treatment (vs. control) and ¯τ is the sample average of out-of-bag

β2Di
estimates.

---

<!-- PAGE 16 -->

16

minimum when receiving the statement balance warning – there are not even negative
magnitudes in the CATE coeﬃcients. Finally, the best linear projection analysis shows a
statistically signiﬁcant heterogeneity only for the minimum payment warning condition. In
the Online Appendix, Table A6, which shows the causal random forests between warning
conditions, the quintile with the largest treatment eﬀect shows that some people would have
signiﬁcantly reduced their likelihood of not paying at least the minimum if they received the
minimum payment warning only instead of a message with the statement balance warning.
Percentage of full. On average, cardholders in the top quintile who received the message
with the statement balance warning increased the fraction paid by 1.9 to 2.2 percentage
points (a relative increase between 2.9% and 3.2%). Comparing all quintiles, the average
magnitudes of the CATEs for cardholders who received the minimum payment warning
message are smaller than the other warning messages. All warning treatment eﬀects show
heterogeneity based on the best linear projection analysis.

V.B. Policy optimization

The previous analysis showed that the warnings did not aﬀect all cardholders in the same
way. One interesting feature of the causal random forest method is that individuals can
be classiﬁed based on their characteristics to predict an optimal policy (Athey and Wager,
2021).
In this case, using the results from the causal random forests for each outcome
variable, the maximum out-of-bag predictions are calculated to classify cardholder i for
one message (Mi). A random forest (Breiman, 2001) is then computed as a classiﬁer using
a training subset and then to predict on a test subset which predicted message ( ˆMi) card-
holder i would receive based on their characteristics. This result yields the “best” predicted
message each cardholder should receive for each outcome variable. However, because card-
holders actually belong to a randomized experimental condition, it is possible to calculate
the optimum CATE as if cardholders were assigned to message ˆMi.23 For example, using
a target policy to decrease any interest charges by increasing the fraction paid, the policy
optimization analysis indicates that most cardholders should receive a message with the
statement balance warning: 45.3% with the statement-balance warning and 44.7% with
both warnings. A small percentage (6.9%) of people should receive the minimum warning
only, and the rest is predicted by the model to receive only the reminder with no warnings.
Analogously, let us suppose that the optimal policy aims to reduce delinquent interest (i.e.,
cardholders paying at least the minimum). In this case, the analysis shows that almost
every cardholder should receive a message with the minimum payment warning (42.5%
the minimum payment warning and 36.4% both warnings), which is consistent with the
previous heterogeneous analysis. Then, 21.0% of debtors would receive a message with the
statement balance warning and 0.1% with the reminder with no warnings.

As an exercise to comprehend the role of each warning, a perverse policy that optimizes
cardholders paying less than the statement balance and, therefore, accruing more interest,

23Across models, accuracy is over 70% on the test subset. For each condition, the accuracy of classiﬁcation was

over 68%, except for the control group, in which the accuracy was 55% for one of the models.

---

<!-- PAGE 17 -->

17

would not include any warning in the message to most of the people (54.1%), and would,
interestingly, use the minimum payment warning in 32.7% of messages.24 Finally, this
policy would put the statement balance warning only in 10.6% of the messages while 2.6%
would receive both warnings. This latter result indicates that some cardholders would
decrease their payments if they received one warning message instead of a reminder with
no warnings.

VI. UNDERLYING MECHANISMS AND ADDITIONAL RESULTS

This section examines several explanations to disentangle why the warnings aﬀect pay-
ment behavior. In particular, the following analyses use the reduced-form analysis from
Section IV, the causal random forest results from the previous section, and a new random-
ized online experiment.

VI.A. Advance payments

One concern about the results is that debtors may have increased their payments during
the experiment by reducing their ability to pay in the following billing cycles, i.e., they
advanced their payments. The ﬁrm shared data on the two billing cycles after the ﬁeld ex-
periment, and Table V shows the results for these periods using Equation 1, the dependent
variables being the likelihood of paying at least the minimum, of paying in full, and the
amount paid. The ﬁrst post-treatment period shows that cardholders who received a mes-
sage including the minimum payment warning increased their likelihood of at least paying
the minimum compared to the control group that received a simple remainder; those in
the minimum-payment warning condition reduced their chance of not paying or of paying
less than the minimum by 2.8% (-0.4 percentage points), and those in the both warnings
condition by 3.6% (-0.5 percentage points). There was no sizable change in the statement
balance warning only in the post-treatment period, even at the 10% signiﬁcance level, and
the magnitude of its estimate is tiny (0.4%, 0.1 percentage point). In contrast, the likeli-
hood of paying in full one billing cycle after the treatment was not sizably diﬀerent from
zero for any warning. Consistent with the increase in the likelihood of at least paying the
minimum, the amount paid increased by 5.2% and 5.6% only for the minimum payment
warning and both warnings conditions, respectively (0.1%, and not sizably diﬀerent from
zero for the statement balance warning condition). Two billing cycles after the experiment,
there were no sizable diﬀerences for any warning in any of the outcome variables.

In summary, there are no signs that cardholders paid in advance (all the estimates
either indicate a positive payment or are very close to zero). On the other hand, this
evidence indicates that the eﬀect of the warnings lasted for one period in the absence
of the intervention, at least when it included the minimum payment warning message,
and then it dissipated, similar to other short-lived behavioral eﬀects (e.g., Schwartz et al.
(2013)). This attenuated eﬀect may also be due to the fact that in October 2019, Chile

24An organization adopting such a policy would probably not send any payment reminder.

---

<!-- PAGE 18 -->

experienced nationwide protests that may have somehow disrupted any purchase pattern
as several retailers closed or changed hours of operation.25

18

VI.B. Anchoring and targets

The minimum payment warning has become one of the most prominent examples of an-
choring bias (e.g., Thaler and Sunstein, 2008). However, the literature on target values
would also predict that people may lean towards paying the minimum amount if the mini-
mum payment is made salient, but through a diﬀerent process. This is examined by Bartels
and Sussman (2016) using a lab study and observational data, ﬁnding that people see the
minimum payment salience as a target value. One of the beneﬁts of the study in this paper
is that it is possible, through a randomized ﬁeld experiment, to examine whether people
are following the minimum payment and statement balance warnings as two anchors or
targets in a natural setting. Speciﬁcally, it can be examined whether debtors change their
behavior to pay the minimum or the statement balance, or a little more, depending on
the warning, as if they were targets, or whether they adjust around those amounts as if
they were anchors. In this latter case, we should see an increase in payments below the
minimum and the statement balance.

Table VI shows the average treatment eﬀect of the warnings on paying close to the
minimum and the statement balance using bins of 20 percent between payments. Based
on Equation 1, the dependent variables are calculated using each payment range (=1 if
payment is in that range, 0 if not). For example, the ﬁrst column indicates that cardholders
decreased their chance of not paying anything for all warnings (vs. the control), and the
second column indicates that the likelihood of paying between any positive amount and
20% of the minimum practically did not change as a result of the warnings. Notably, almost
every estimate of the top part of Table VI shows a negative magnitude for any range smaller
than paying the minimum. If the minimum payment warning had acted as an anchor, we
should have seen positive values around the minimum. The bottom part of the table shows
the eﬀect of all warning messages on payments around the statement balance. For example,
column (10) shows the likelihood of paying an amount midway between the minimum and
the statement balance, indicating no sizable change in payments.
In general, there are
positive estimates after the amount associated with each warning message, indicating that
cardholders were more likely to pay the minimum or a little more, or the statement balance
or a little more depending on the speciﬁc warning. Therefore, this analysis suggests that
it is more likely that debtors saw the warnings and associated amounts as target values
instead of anchors.

25From the New York Times: “‘Chile Woke Up’: Dictatorship’s Legacy of Inequality Triggers Mass Protests.”
“Crisis in
(https://www.nytimes.com/2019/11/03/world/americas/chile-protests.html) and from InStoreView:
Chile: Losses and opportunities for retail (in Spanish)” (https://www.instoreview.com/crisis-en-chile-perdidas-y-
oportunidades-para-el-retail).

---

<!-- PAGE 19 -->

19

VI.C. Previous payment behavior, the minimum payment and the statement balance

One of the key components of the experimental design of the ﬁeld experiment is its dual-
target setting of the minimum payment and statement balance warnings. Table VII shows
diﬀerences in the average treatment eﬀects of the warnings depending on debtors’ previous
payment behavior and the speciﬁc amounts in the credit card statement they received
during the experiment, using the percentage of full payment as the dependent variable.
This outcome variable can capture any increase in payments and showed a heterogeneous
eﬀect in all warnings based on the best linear predictor analysis.

Column 1 of Table VII shows a sub-sample of debtors who failed to pay at least the
minimum in one-half or more of the months prior to the intervention, i.e., they are debtors
who are more likely to become delinquent. For this sub-sample, receiving the minimum
payment warning or both warnings instead of the simple reminder increased the fraction
paid by 3.5 and 3.8 percentage points, respectively. On the other hand, there was no sizable
diﬀerence from zero for those who received the statement balance warning.

Table VII (column 2) shows a sub-sample of debtors who most of the time paid between
the minimum and the statement balance prior to the experiment (i.e., they are more likely
to pay a revolving amount). They increased the fraction paid during the experiment if
they received the statement balance warning or both warnings by 1.5 and 0.9 percentage
points, respectively. However, there was no sizable diﬀerence from zero in this sub-sample
for debtors who were in the minimum payment warning condition, consistent with the
ﬁnding that this warning did not signiﬁcantly reduce revolving interest. Overall, despite the
relatively small sample sizes in this analysis, the results suggest that debtors follow a self-
selection process by responding to speciﬁc warning messages (increasing their payments).26
Columns 3 and 4 of Table VII examine whether previous payment variation is aﬀected
by the warnings, using the mean absolute deviation (MAD) from the mean fraction paid.
For example, a debtor who pays the same fraction of the statement balance every time will
have a MAD equal to 0 and is less likely to be aﬀected by any warning as she is following
some sort of status quo.
In contrast, a debtor who varies her payment fraction every
month prior to the experiment probably deliberated on how much to pay, and therefore,
the warnings are more likely to aﬀect her payment decision (the maximum MAD can be
0.5 for someone who varies from paying in full to not paying at all). Using a median split of
this covariate, columns 3 and 4 show that debtors who have usually changed the percentage
of the statement balance they pay every month increased their payments much more due
to the warnings than debtors who generally paid the same fraction, mainly when messages
include the statement balance warning.

Columns 5 to 10 use the minimum payment and statement balance amounts charged
in the credit card statements for the experiment as the warnings are associated with the
consequences of paying these amounts. Using the median split of these amounts, the results

26Table A7 in the Online Appendix shows the payment distribution of these two sub-samples. It suggests that
debtors who are more likely not to pay at least the minimum shift their payments toward the minimum when receiving
a message with the minimum payment warning, as compared to those who received the statement balance warning
only.

---

<!-- PAGE 20 -->

20

indicate that the eﬀects of the minimum payment warning and the statement balance
warning do not signiﬁcantly vary depending on the amounts, except that the minimum
payment warning seems only to increase payments of debtors who had a low minimum
payment. On the other hand, the eﬀect of the both warnings condition seems to depend not
only on the speciﬁc statement balance and the minimum payment amounts but especially
on their absolute diﬀerence. In particular, debtors who received both warnings increased
the fraction paid relatively more when the diﬀerence between the statement balance and
minimum payment was relatively small. To illustrate, columns 5 and 6 indicate that debtors
who received both warnings increased the fraction paid by 1.0 percentage points (1.2%)
compared to the control group, when the diﬀerence between the minimum payment and
the statement balance amounts was small (M edian = $259), and that fraction increased by
0.4 percentage points (0.6%), although not signiﬁcantly sizably diﬀerent from zero, when
the diﬀerence between the amounts was great (M edian = $1,598).

The previous reduced-form analyses may be susceptible to the speciﬁc median splits
of the sub-samples, and any form of interaction may miss other functional relationships
between variables (for completeness, Table A8 in the Online Appendix shows the results
using linear and quadratic interactions). The causal random forest approach can examine
whether the estimated treatment eﬀects depend on the characteristics of debtors and bills
with more ﬂexible functions (e.g., Athey and Imbens, 2019; Davis and Heller, 2017). Using
the outputs from Section V, the panels of Figure 2 show the estimated conditional average
treatment eﬀects on the y-axis, and each panel uses a diﬀerent covariable in the x-axis.
The dashed lines are the benchmark for the estimated conditional average treatment eﬀect
for each warning compared to the control condition. The results are mostly in line with
the reduced-form analysis. For example, panel A shows that the largest treatment eﬀects
of the fraction paid are for debtors who usually partially pay their credit cards under the
conditions that include a statement balance warning. Panel B shows that all warnings
increase the estimated treatment eﬀect as people varied more (M AD) how much of their
statement balance they usually pay, although to a lesser degree for the minimum payment
warning condition; and panel C shows that debtors with the largest (smallest) estimated
treatment eﬀects due to the both warnings condition are characterized by a small (large)
gap between the minimum payment and the statement balance. Finally, Tables A9, A10
and A11 in the Online Appendix show the covariates across quintiles from Section V, sorted
It shows, for example, for the both warnings
by conditional average treatment eﬀects.
condition (Table A11), that a debtor from the top (bottom) quintile — the one with the
largest (smallest) conditional average treatment eﬀect — has a mean absolute deviation
from the fraction paid of 24.4% (8.8%) and had a gap between the minimum payment and
statement balance of $1,217 ($1,953).

In summary, these analyses suggest that, ﬁrst of all, debtors are more likely to be aﬀected
by the warnings if they usually vary how much they pay. Even if all debtors included in
the experiment do not have automatic payment, they still may be used to paying the
same amount every month. Varying payments may be the result of deliberate decisions
and, therefore, how much to pay may change depending on the warning message. This

---

<!-- PAGE 21 -->

21

eﬀect is separate from reminding people to pay like the message without warnings does
(control condition). Secondly, debtors who were in the both warnings condition seem to pay
attention to a speciﬁc warning depending on whether or not they can pay more, based on
how much they used to pay and the gap between the minimum payment and the statement
balance, i.e., debtors choose to prioritize a speciﬁc warning when both warnings are salient.
This result oﬀers new insights into individual decision-making in dual-target settings.

VI.D. Liquidity constraints

Similar to the previous analysis, Table VIII and Figure 3 examine whether the eﬀects
of the warnings may be associated with liquidity constraints. Consistent with prior ev-
idence (Keys and Wang, 2019), the results show no relevant heterogeneous eﬀects using
debtors’ income (columns 1 and 2 in Table VIII and Panel A of Figure 3) or the degree
of indebtedness with other lenders (columns 3 and 4 in Table VIII and Panel B of Figure
3).27 Therefore, cardholders may be increasing their payments because of the statement
balance warning, mainly by reducing consumption or by using savings. Tables A9, A10
and A11 in the Online Appendix also show no clear income pattern across the quintiles
sorted by the conditional average treatment eﬀect, but they do show that debtors owing
little debt to the credit card issuer in the experiment may be more aﬀected by the both
warnings message, i.e., part of the eﬀect is coming from people who may be prioritizing
repayment with one institution because of the warning.28

VI.E. Understanding, ﬁnancial knowledge, ﬁnancial vulnerability, and cognitive reﬂection

Previous literature has shown that other factors not captured by the ﬁeld experiment
may be associated with payment decisions. These factors may also be aﬀecting the impact
of the statement balance and minimum payment warnings. In particular, prior research
has found a positive relationship between indebtedness caused by the eﬀect of the mini-
mum payment and poor ﬁnancial literacy (e.g., Artavanis and Karra, 2020; Hamid and
Loke, 2021), and ﬁnancial vulnerability (Salisbury and Zhao, 2020). Although there is
no prior research on the statement balance warning, one hypothesis is that debtors with
poor ﬁnancial literacy or ﬁnancial vulnerability may beneﬁt from the minimum payment
warning more than a statement balance warning. On the other hand, ﬁnancial literacy
has been described as a long-term achievement, and messages, such as warnings, should
address in-the-moment decisions (Fernandes et al., 2014). It would also be important to
know whether the warnings can aﬀect people’s speciﬁc understanding of the consequences
of paying less than the minimum and of paying in full.

27The ﬁrm uses a score of how much money is lent as a percentage share of debt in the banking system (any type
of debt). This score, which goes from 0 to 2.14 (for conﬁdentiality purposes, the score was normalized with a mean
of 1.0), indicates that people owe most of their debt to other lenders when the number is almost zero and only to
the ﬁrm when it is 2.14.

28A speciﬁc analysis of this group and their payment behavior in the subsequent billing cycle does not diﬀer
signiﬁcantly from the control group. This means that debtors who have more debt with other institutions are not
advancing debt payment because of the warnings.

---

<!-- PAGE 22 -->

22

In order to examine the relationship between the warnings and cognitive factors, an online
experiment was conducted in Proliﬁc Academic (Peer et al., 2017) with debtors from the
US and the UK who had used a credit card in the previous three months. Participants (N =
400; female: 48.6%, 37.9 years old) saw a monthly credit card statement using the average
monthly amount in each country and the corresponding minimum payment (currency and
amounts were adjusted depending on where participants lived).29 Then they were asked
“how much would you repay?” with the following options: minimum payment, statement
balance, or another amount, in which case they had to type in a number. The information
and payment choices closely reﬂected how people worldwide see their credit card informa-
tion when paying online every month. Importantly, participants were randomly assigned
to four experimental conditions: minimum payment warning, statement balance warning,
both warnings, and no warning (control). After people input their payment decision, they
were asked how well they understood what the minimum payment and statement balance
mean (from 1: ”Not at all” to 7: ”Very well”), how much they generally pay on the credit
card (Salisbury, 2014), their average monthly credit card payment, a ﬁnancial vulnerability
scale (Salisbury and Zhao, 2020), ﬁnancial knowledge questions (Navarro-Martinez et al.,
2011), and the Cognitive Reﬂection Test (Frederick, 2005), which has been associated with
the anchoring bias and present bias (Bergman et al., 2010; Welsh et al., 2013). Finally,
participants answered demographic questions. All materials are in the Online Appendix
A12.

Table IX shows the average treatment eﬀect of each warning message on payment deci-
sions and the understanding of the minimum payment and the statement balance. First,
despite the hypothetical nature of the experiment, 16.8% of cardholders in the control
group chose to pay the minimum, 33.7% between the minimum and the statement balance,
and 49.5% chose to pay in full. Second, the results indicate that the warnings shifted
the payment distribution. The warning that included only the statement balance warning
increased the likelihood of deciding to pay in full by 18 percentage points compared to the
baseline no-warning condition, and the both warnings conditions increased this likelihood
by 25 percentage points. Messages including the statement balance warning also increased
the fraction paid of the statement balance, replicating the result from the ﬁeld experiment,
although by much larger magnitudes due to the hypothetical nature of the online experi-
ment and also because more people likely paid attention to the message at the moment of
the decision. On the other hand, the minimum warning condition had no sizable eﬀect on
payment decisions compared to the no-warning condition, although it is the only condition
with a positive estimate for the likelihood of paying the minimum.

The last two columns of Table IX show the changes in the understanding of the minimum
payment and statement balance. First, there was a high average reported understanding
of the meaning of both amounts in the baseline (above six on a 7-point scale). Second,
cardholders, regardless of the type of warning, directionally increased their understand-
ing of the minimum payment compared to control, from 0.21 to 0.24 points (signiﬁcance
levels at 9 to 15 percent). This suggests that any warning, even the statement balance

29One person was excluded because they did not complete the study.

---

<!-- PAGE 23 -->

23

warning, could increase people’s perception of their understanding of the minimum pay-
ment. Somewhat diﬀerent is the reaction of participants to their reported understanding
of what the statement balance means. In this case, people who saw the statement bal-
ance warning reported an increased understanding of this concept by 0.31 (both warnings)
and 0.23 (statement balance warning) points compared to the no-warning condition, with
signiﬁcance levels at the 4 and 12 percent, respectively.
In contrast, for the statement
balance understanding, the estimate of the minimum payment warning condition is much
smaller (with p = 0.41). Despite all the limitations of this outcome variable (self-reported,
ceiling eﬀect, and statistical power), people may have improved their understanding of the
statement balance warning due to the warning messages. This ﬁnding is very consistent
with a study conducted with governmental institutions in Chile, which asked these ques-
tions diﬀerently: credit card owners were asked how much they would have to pay to avoid
additional revolving interest. Most of them (58 percent) answered correctly (i.e., they en-
tered the statement balance) when the credit card statement contained a statement balance
warning, but only 26 percent correctly answered when they saw a credit card statement
with no warnings (SERNAC, 2021).

Table A13 (A and B) in the Online Appendix examines the role of ﬁnancial knowledge,
ﬁnancial vulnerability, and the cognitive reﬂection test (CRT) score. Based on the main
eﬀects of these covariates, more ﬁnancially literate cardholders with higher cognitive re-
ﬂection test scores would pay a larger fraction of their statement balance. Nevertheless,
more importantly, there is no strong indication of a moderation of the warning treatment
eﬀects using these variables, merely suggestive evidence that messages with the minimum
payment warning may be more eﬀective for people with better ﬁnancial knowledge and low
cognitive reﬂection test scores, indicating that this warning would aﬀect people who make
a rapid decision after seeing these messages.

VII. CONCLUSION

This paper documents a new statement balance warning for credit card payments in
contrast to the so-called “perverse nudge” based on the minimum payment salience. There
are several results that trigger diﬀerent conclusions. First, the warnings shift debtors’
payment distribution depending on the speciﬁc message. The statement balance warn-
ing increases payments and reduces interest by shifting payments towards the statement
balance. Compared to previous lab studies, the ﬁeld experiment results on the minimum
payment warning show no clear perverse eﬀect from highlighting the minimum payment
through a warning. In addition, the online study discussed in Section VI, structured in a
way similar to previous lab studies, does not suggest a backﬁring eﬀect either. One expla-
nation is that most previous lab studies focused on the time it takes to pay down the debt,
and a warning may be perceived as a softer manipulation. Nevertheless, this paper ﬁnds
that some cardholders are inﬂuenced to pay the minimum by the minimum warning.

Second, the quintiles based on the causal random forest show that 20 to 40 percent of the
sample signiﬁcantly increased their payments because of the statement balance warning.
The rest already paid a large fraction of the statement balance, so little noticeable gain

---

<!-- PAGE 24 -->

24

was possible, they were more likely to pay the same percentage of the statement balance
every billing cycle or might not even pay attention to the email.30 Warnings also seemed
to be aﬀected by the diﬀerence between the statement balance and minimum payment: it
is easier to pay more if the diﬀerence between these amounts is small, while when it is
great, the both warnings message may oﬀer an option of making the minimum payment
that the statement balance only warning does not. This result sheds light on how people
may deal with dual-target settings, in which one of them is disregarded when it is hard to
achieve. In other words, people can choose one target message if they are able to pay a
higher amount. Ex-ante, it could have been predicted that the statement balance warning
may even discourage low-payers from making payment, but the results suggest that people
are just following the warnings as much as they can without reducing their payment. Also,
the warnings seem to be treated as targets or goals that cardholders try to achieve.

Third, the cardholder behavior was very similar for the statement balance warning only
and the both warnings messages. This is the case except for a diﬀerence in the likelihood of
making the minimum payment when receiving the both warnings message, which is mainly
driven by debtors who historically were more likely to fail to pay at least the minimum
– a relatively small sub-sample in this population. The results were similar for these two
conditions in the quintile analysis with the causal random forest and the online experiment.
Nevertheless, the policy optimization analysis indicates a gain from using diﬀerent messages
to change repayment behavior, although using both warnings can be a good starting point.
Fourth, debtors who increase their payments and reduce their interest as a consequence
of the statement balance warning seem not to experience liquidity constraints. So, why
did they not pay more before? Recent research has explained this behavior by the credit
card puzzle or co-holding puzzle (Gathergood and Weber, 2014), where debtors do not use
liquid assets to repay their credit cards and reduce the costs of high interest. Consistently,
Vihri¨al¨a (2020) ﬁnds that households that are more likely to co-hold are more likely to
be “anchored” to paying the minimum payment, despite having the means to pay in full.
As the online experiment suggests, some debtors may need a salient explanation of the
consequences of not paying in full to pay more, just like the minimum payment salience
did for paying the minimum.

The results also have relevant policy implications. Compared to other solutions such as
increasing the minimum payment, the statement balance warning helps consumers decrease
their debt without imposing a cost on the more constrained borrowers (D’Astous and
Shore, 2017). In addition, while some behavioral interventions have been controversial (e.g.,
default options) because they depend on people not paying enough attention (Sunstein,
2019), warnings depend on the opposite, i.e., people paying attention to the information.
However, one limitation is that the intervention was conducted during one billing cycle, and
it may be relevant to know whether cardholders would still pay attention to the warnings
if they were included every period. This may motivate future research to examine whether
it is possible to have additive eﬀects over a long period.

30There were tiny diﬀerences in the historic email opening rates, but in the opposite direction that one would

expect; the quintile with the largest treatment eﬀect had a slightly lower historic email opening rate.

---

<!-- PAGE 25 -->

25

Finally, the success of any behavioral intervention depends on its degree of scalability (Al-
Ubaydli et al., 2017). The statement balance warning is highly scalable. For example, as the
online experiment suggests, it is possible to use the statement balance warning in online
payment settings, which are becoming more common in both developed and developing
countries. Furthermore, in the aftermath of the current study, the Chilean Consumer
Protection Bureau and the Ministry of Economy decided to regulate a new simpliﬁed
credit card statement for all credit cards. Based on this study, one of the main features of
these redesigned credit card statements is the statement balance warning. The ﬁrst step
in changing the regulation was to conduct an online experiment testing diﬀerent versions
of the redesigned credit card statement among a national sample of credit cardholders.
Results showed not only that the statement balance warning increased the intention to
increase payments, replicating the results of this paper, but also that it helped credit
cardholders learn how much to pay to reduce revolving interest (SERNAC, 2021).

---

<!-- PAGE 26 -->

REFERENCES

26

Adams, P., B. Guttman-Kenney, L. Hayes, S. Hunt, and N. Stewart (2018). Increasing
credit card payments using choice architecture: The case of anchors and prompts. FCA
Occasional Papers in Financial Regulation (Occasional Paper No. 42).

Agarwal, S., S. Chomsisengphet, and C. Lim (2017). What Shapes Consumer Choice and
Financial Products? A Review. Annual Review of Financial Economics 9 (1), 127–146.

Agarwal, S., S. Chomsisengphet, N. Mahoney, and J. Stroebel (2015). Regulating con-
sumer ﬁnancial products: Evidence from credit cards. The Quarterly Journal of Eco-
nomics 130 (1), 111–164.

Al-Ubaydli, O., J. A. List, and D. L. Suskind (2017). What can we learn from experiments?
understanding the threats to the scalability of experimental results. American Economic
Review 107 (5), 282–86.

Allcott, H. and T. Rogers (2014). The short-run and long-run eﬀects of behavioral in-
terventions: Experimental evidence from energy conservation. American Economic Re-
view 104 (10), 3003–3037.

Arenas, J. and D. Schwartz (2021). Using Causal Random Forest to Examine Spillover

Eﬀects of Credit Card Payment Reminders. Technical report.

Artavanis, N. and S. Karra (2020). Financial literacy and student debt. The European

Journal of Finance 26 (4-5), 382–401.

Athey, S. and G. Imbens (2016). Recursive partitioning for heterogeneous causal eﬀects.

Proceedings of the National Academy of Sciences 113 (27), 7353–7360.

Athey, S. and G. W. Imbens (2017). The state of applied econometrics: Causality and
policy evaluation. In Journal of Economic Perspectives, Volume 31, pp. 3–32. American
Economic Association.

Athey, S. and G. W. Imbens (2019). Machine Learning Methods That Economists Should

Know about. Annual Review of Economics 11, 685–725.

Athey, S., J. Tibshirani, and S. Wager (2019). Generalized random forests. Annals of

Statistics 47 (2), 1179–1203.

Athey, S. and S. Wager (2019). Estimating Treatment Eﬀects with Causal Forests: An

Application.

Athey, S. and S. Wager (2021). Policy Learning With Observational Data. Economet-

rica 89 (1), 133–161.

Bartels, D. and A. Sussman (2016). Anchors, Target Values, and Credit Card Payments.

---

<!-- PAGE 27 -->

27

Bergman, O., T. Ellingsen, M. Johannesson, and C. Svensson (2010). Anchoring and

cognitive ability. Economics Letters 107 (1), 66–68.

Bertrand, M., E. Duﬂo, and S. Mullainathan (2004). How much should we trust diﬀerences-

in-diﬀerences estimates? The Quarterly Journal of Economics 119 (1), 249–275.

Besley, T. and A. Case (2000). Unnatural Experiments? Estimating the Incidence of

Endogenous Policies. The Economic Journal 110 (467), 672–694.

Bhamra, H. S. and R. Uppal (2019). Does household ﬁnance matter? Small ﬁnancial errors

with large social costs.

Board of Governors of the Federal Reserve System (2021). Delinquency Rate on Credit
Card Loans, All Commercial Banks [DRCCLACBS], August 2021. Technical report,
Board of Governors of the Federal Reserve System.

Breiman, L. (2001). Random forests. Machine learning 45 (1), 5–32.

Breiman, Friedman, O. and Stone (1984). Classication And Regression Trees. Monterey:

WadsworthandBrooks/Cole..

Campbell, J. Y. (2016). Restoring rational choice: The challenge of consumer ﬁnancial
regulation. In American Economic Review, Volume 106, pp. 1–30. American Economic
Association.

Chernozhukov, V., D. Chetverikov, M. Demirer, E. Duﬂo, C. Hansen, W. Newey, and
J. Robins (2018). Double/debiased machine learning for treatment and structural pa-
rameters. The Econometrics Journal 21 (1).

Chernozhukov, V., M. Demirer, E. Duﬂo, and I. Fern´andez-Val (2018). Generic machine
learning inference on heterogeneous treatment eﬀects in randomized experiments, with
an application to immunization in india. (24678).

D’Astous, P. and S. H. Shore (2017). Liquidity Constraints and Credit Card Delinquency:
Evidence from Raising Minimum Payments. Journal of Financial and Quantitative Anal-
ysis 52 (4), 1705–1730.

Davis, J. M. V. and S. B. Heller (2017). Using causal forests to predict treatment hetero-
geneity: An application to summer jobs. In American Economic Review, Volume 107,
pp. 546–550. American Economic Association.

El Issa, E. (2019). 2019 American Household Credit Card Debt Study.

Fernandes, D., J. G. Lynch, and R. G. Netemeyer (2014). Financial Literacy, Financial
Education, and Downstream Financial Behaviors. Management Science 60 (8), 1861–
1883.

---

<!-- PAGE 28 -->

28

Fitch, C., S. Hamilton, P. Bassett, and R. Davey (2011). The relationship between personal
debt and mental health: A systematic review. Mental Health Review Journal 16 (4), 153–
166.

Frederick, S. (2005). Cognitive Reﬂection and Decision Making. Journal of Economic

Perspectives 19 (4), 25–42.

Galizzi, M. M. and D. Navarro-Martinez (2019). On the External Validity of Social Pref-
erence Games: A Systematic Lab-Field Study. Management Science 65 (3), 976–1002.

Gathergood, J. and J. Weber (2014). Self-control, ﬁnancial literacy & the co-holding puzzle.

Journal of Economic Behavior & Organization 107, 455–469.

Gin´e, Le´on, Negrin, Cort´es, and D. l. Cruz (2019). Simpliﬁcation and Standardization of
Credit Card Statements: Evidence from a Lab Experiment in Mexico. Technical report.

Guttman-Kenney, B., J. Leary, and N. Stewart (2018). Weighing anchor on credit card

debt. Financial Conduct Authority Occasional Paper Series 43 .

Hamid, F. S. and Y. J. Loke (2021). Financial literacy, money management skill and credit

card repayments. International Journal of Consumer Studies 45 (2), 235–247.

Heath, C., R. P. Larrick, and G. Wu (1999). Goals as Reference Points. Cognitive Psy-

chology 38 (1), 79–109.

Heckman, J. J., R. J. Lalonde, and J. A. Smith (1999). Chapter 31 The economics and
econometrics of active labor market programs. In Handbook of Labor Economics, Volume
3 PART, pp. 1865–2097. Elsevier B.V.

Hershﬁeld, H. E. and N. J. Roese (2015). Dual payoﬀ scenario warnings on credit card
statements elicit suboptimal payoﬀ decisions. Journal of Consumer Psychology 25 (1),
15–27.

Hodson, R., R. E. Dwyer, and L. A. Neilson (2014). Credit Card Blues: The Middle Class

and the Hidden Costs of Easy Credit. Sociological Quarterly 55 (2), 315–340.

Homonoﬀ, T., R. L. OBrien, and A. B. Sussman (2018). Does Knowing Your FICO Score
Change Financial Behavior? Evidence from a Field Experiment with Student Loan
Borrowers. SSRN Electronic Journal .

Jiang, S. S. and L. F. Dunn (2013). New evidence on credit card borrowing and repayment

patterns. Economic Inquiry 51 (1), 394–407.

Jung, M. H., H. Perfecto, and L. D. Nelson (2016). Anchoring in Payment: Evaluat-
ing a Judgmental Heuristic in Field Experimental Settings. Journal of Marketing Re-
search 53 (3), 354–368.

---

<!-- PAGE 29 -->

29

Kahn-Lang, A. and K. Lang (2020, jul). The Promise and Pitfalls of Diﬀerences-in-
Diﬀerences: Reﬂections on 16 and Pregnant and Other Applications. Journal of Business
& Economic Statistics 38 (3), 613–620.

Kahneman, D. and A. Tversky (1979). Prospect theory. Econommetrica 47 (2), 263–292.

Keys, B. J., N. Mahoney, and H. Yang (2020). What Determines Consumer Financial

Distress? Place- and Person-Based Factors. SSRN Electronic Journal .

Keys, B. J. and J. Wang (2019). Minimum payments and debt paydown in consumer credit

cards. Journal of Financial Economics 131 (3), 528–548.

Lieber, R. (2010). Your Card Has Been Declined, Just as You Wanted.

MinEcon (2012).

Decreto 44 - APRUEBA REGLAMENTO SOBRE INFOR-
MACI ´ON AL CONSUMIDOR DE TARJETAS DE CR´EDITO BANCARIAS Y
NO BANCARIAS. Technical report, Biblioteca del Congreso Nacional de Chile.
https://www.bcn.cl/leychile/navegar?idNorma=1041745.

Navarro-Martinez, D., L. C. Salisbury, K. N. Lemon, N. Stewart, W. J. Matthews, and
A. J. Harris (2011). Minimum required payment and supplemental information disclosure
eﬀects on consumer debt repayment decisions. Journal of Marketing Research 48 (SPEC.
ISSUE), S60–S77.

Nelson, M. C., K. Lust, M. Story, and E. Ehlinger (2008). Credit card debt, stress and
key health risk behaviors among college students. American Journal of Health Promo-
tion 22 (6), 400–407.

Norvilitis, J. M., M. M. Merwin, T. M. Osberg, P. V. Roehling, P. Young, and M. M. Kamas
(2006). Personality Factors, Money Attitudes, Financial Knowledge, and Credit-Card
Debt in College Students1. Journal of Applied Social Psychology 36 (6), 1395–1413.

Peer, E., L. Brandimarte, S. Samat, and A. Acquisti (2017). Beyond the Turk: Alter-
native platforms for crowdsourcing behavioral research. Journal of Experimental Social
Psychology 70, 153–163.

Resendiz, J. (2020). Average Credit Card Debt in America.

Retail Financiero (2019). Compendio Estad´ısco Mensual de la Industria del Cr´edito (Oc-
tubre 2019). Technical report, Retail Financiero. https://www.retailﬁnanciero.org/wp-
content/uploads/2020/01/Reporte-SBIF-Oct-2019.pdf.

Retail Financiero (2021). Compendio Estad´ısco Mensual de la Industria del Cr´edito (Marzo

2021). Technical report, Retail Financiero.

Ru, H. and A. Schoar (2016). Do Credit Card Companies Screen for Behavioral Biases?

Technical report, National Bureau of Economic Research, Cambridge, MA.

---

<!-- PAGE 30 -->

30

Rubin, D. B. (1974). Estimating causal eﬀects of treatments in randomized and nonran-

domized studies. Journal of educational Psychology 66 (5), 688–701.

Sahni, N. S., S. C. Wheeler, and P. Chintagunta (2018). Personalization in Email
Marketing: The Role of Noninformative Advertising Content. Marketing Science,
mksc.2017.1066.

Salisbury, L. C. (2014). Minimum payment warnings and information disclosure eﬀects
on consumer debt repayment decisions. Journal of Public Policy and Marketing 33 (1),
49–64.

Salisbury, L. C. and M. Zhao (2020). Active Choice Format and Minimum Payment Warn-
ings in Credit Card Repayment Decisions. Journal of Public Policy & Marketing 39 (3),
284–304.

Schultz, P. W., J. M. Nolan, R. B. Cialdini, N. J. Goldstein, and V. Griskevicius (2007).
The constructive, destructive, and reconstructive power of social norms. Psychological
science 18 (5), 429–34.

Schwartz, D., B. Fischhoﬀ, T. Krishnamurti, and F. Sowell (2013). The Hawthorne eﬀect
and energy awareness. Proceedings of the National Academy of Sciences of the United
States of America 110 (38), 15242–15246.

Schwartz, D., E. A. Keenan, A. Imas, and A. Gneezy (2021). Opting-in to prosocial

incentives. Organizational Behavior and Human Decision Processes 163, 132–141.

Schwartz, D., G. Loewenstein, and L. Ag¨uero-Gaete (2020).

Encouraging pro-
environmental behaviour through green identity labelling. Nature Sustainability 3 (9),
746–752. https://www.nature.com/articles/s41893-020-0543-4.

Seira, E., A. Elizondo, and E. Laguna-M¨uggenburg (2017). Are Information Disclosures Ef-
fective? Evidence from the Credit Card Market. American Economic Journal: Economic
Policy 9 (1), 277–307.

SERNAC (2021). Evaluating the impact of communicating the credit card statement on
ﬁnancial decisions: experimental evidence. https://www.sernac.cl/portal/619/articles-
62180 archivo 03.pdf.

Shift Processing (2021). Credit Card Statistics [Updated February 2021].

Soll, J. B., R. L. Keeney, and R. P. Larrick (2013). Consumer misunderstanding of credit
card use, payments, and debt: Causes and solutions. Journal of Public Policy & Mar-
keting 32 (1), 1–49.

Statista (2017). Credit card usage by country. https://www.statista.com/statistics/675371/

ownership-of-credit-cards-globally-by-country/.

---

<!-- PAGE 31 -->

31

Stewart, N. (2009). The Cost of Anchoring on Credit-Card Minimum Repayments. Psy-

chological Science 20 (1), 39–41.

Sunstein, C. R. (2019). Which nudges do people like? a national survey. In Handbook of

Behavioural Change and Public Policy. Edward Elgar Publishing.

Sylvia, S., N. Warrinnier, R. Luo, A. Yue, O. Attanasio, A. Medina, and S. Rozelle (2021).
From Quantity to Quality: Delivering a Home-Based Parenting Intervention Through
China’s Family Planning Cadres. The Economic Journal 131 (635), 1365–1400.

Thaler, R. H. and C. R. Sunstein (2008). Nudge: improving decisions about health. Wealth,

and Happiness 6, 14–38.

The Economist (2008).

The
Economist. https://www.economist.com/ﬁnance-and-economics/2008/12/11/a-nudge-
in-the-wrong-direction.

Credit cards - A nudge in the wrong direction.

Tversky, A. and D. Kahneman (1974). Judgment under Uncertainty: Heuristics and Biases.

Science 185 (4157), 1124–1131.

Unsworth, K., G. Yeo, and J. Beck (2014). Multiple goals: A review and derivation of

general principles. Journal of Organizational Behavior 35 (8), 1064–1078.

Vihri¨al¨a, E. (2020). Untangling the credit card debt puzzle. Available at SSRN 3710505 .

Wager, S. and S. Athey (2018). Estimation and Inference of Heterogeneous Treatment
Eﬀects using Random Forests. Journal of the American Statistical Association 113 (523),
1228–1242.

Wang, J. and B. Keys (2014). Perverse nudges: Minimum payments and debt paydown in

consumer credit cards. Technical Report 4.

Welsh, M., N. Burns,

How much more

and P. Delfabbro

reﬂec-
In Proceed-
tion test:
ings of
society, Volume 35.
https://escholarship.org/content/qt68n012fh/qt68n012fh noSplash 1e55cbb955ecbe352
3374393180ab1a7.pdf.

than numerical
the Cognitive Science

the Annual Meeting of

cognitive

ability?

(2013).

The

---

<!-- PAGE 32 -->

VIII. TABLES

32

TABLE I
DESCRIPTIVE STATISTICS AND RANDOMIZATION BALANCE

All

(1)

Control

MinW

SBalW

BothW

(2)

(3)

(4)

(5)

Diﬀerence
p-value
(6)

Cardholder information

Age (years)
Male
Monthly income ($)
Company’s internal credit score (0-100)
Credit card statment for the treatment period

44.4
48.4%
3,645.3
64.2

44.3
48.4%
3,647.4
64.2

44.4
48.6%
3,651.1
64.3

44.4
48.4%
3,632.8
64.2

44.4
48.3%
3,649.9
64.3

Statement balance ($)
Minimum ($)

1,949.3
415.7

1,956.2
414.6

1,940.1
414.2

1,947
417.8

1,953.8
416.3

Payment behavior before the treatment period

Previous payment ($)
Mean previous fraction of full
Previously paid in full
Previously paid the minimum
Previously did not pay at least the min

N cardholders

1208.2
75.8%
63.7%
7.9%
8.2%
179,706

1207.3
75.7%
63.6%
7.9%
8.3%
44,922

1202.2
75.9%
63.8%
7.9%
8.3%
44,935

1202.5
75.8%
63.8%
7.8%
8.3%
44,921

1220.8
75.8%
63.7%
8.0%
8.2%
44,928

0.8072
0.8278
0.7814
0.9160

0.8585
0.7224

0.5065
0.8919
0.6400
0.4469
0.7485

Notes: Cardholder and payment statistics for the whole sample are in column 1 and each experimental
condition in columns 2-5. Column 6 shows the p-value for the diﬀerence across conditions. Monetary
values were re-scaled for reasons of conﬁdentiality using a U.S. statement balance of $1,949.28 as reference.
The credit score computed by the ﬁrm was also re-scaled to a range of 0 to 100, where a higher number
is a better credit score. MinW is the Minimum warning, SBalW is the Statement Balance Warning, and
BothW is the Both Warnings condition.

---

<!-- PAGE 33 -->

TABLE II
WARNINGS EFFECT ON PAYMENT BEHAVIOR

33

ln(payment)

Dep. Var.

MinW

SBalW

BothW

(1)
0.0615***
(0.0206)
0.0661***
(0.0207)
0.0778***
(0.0206)
p-values from pairwise comparison
0.4244
0.5681
0.8226
11.080
0.023
2,853,939
179,706

Baseline (Control)
R2
N observations
N carholders

BothW vs. MinW
BothW vs. SBalW
SBalW vs. MinW

Less than
min
(2)
-0.0079***
(0.0018)
-0.0067***
(0.0019)
-0.0085***
(0.0019)

0.7835
0.3317
0.4846
0.097
0.003
2,853,939
179,706

Full

(3)
0.0020
(0.0025)
0.0064***
(0.0025)
0.0069**
(0.0025)

0.0443
0.8281
0.0729
0.625
0.036
2,853,939
179,706

Percent of
Full
(4)
0.0030
(0.0019)
0.0068***
(0.0019)
0.0070***
(0.0019)

0.0362
0.9076
0.0483
0.741
0.040
2,853939
179,706

ln(revolving
interest)
(5)
-0.0303
(0.0200)
-0.0681***
(0.0200)
-0.0898***
(0.0201)

ln(delinquent
interest)
(6)
-0.0739***
(0.0155)
-0.0422***
(0.0155)
-0.0797***
(0.0155)

0.0031
0.2792
0.0595
4.424
0.174
2,853939
179,706

0.7085
0.0156
0.0401
1.552
0.083
2,853,939
179,706

Notes: OLS estimates of Equation 1 using diﬀerent dependent variables. Columns 1 to 4 use the payments
associated with the billing cycle of the treatment period (t). Columns 5 and 6 use the credit card statement
information one billing cycle after the experiment (t+1). SEs between parenthesis. MinW is the Minimum
warning, SBalW is the Statement Balance Warning, and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 34 -->

TABLE III
WARNINGS EFFECT ON PAYMENT DISTRIBUTION

MinW

Dep. Var.

No
Payment
(1)
-0.0053***
(0.0017)
-0.0048***
(0.0017)
-0.0063***
(0.0017)
p-values from pairwise comparison

BothW

SBalW

BothW vs. MinW
BothW vs. SBalW
SBalW vs. MinW

Baseline (Control)
R2
N observations
N carholders

0.5521
0.3689
0.7593
0.082
0.006
2,853,939
179,706

Between 0
and Min
(2)
-0.0026***
(0.0008)
-0.0019**
(0.0008)
-0.0021***
(0.0008)

0.5177
0.7502
0.3324
0.015
0.010
2,853,939
179,706

Min

(3)
0.0052***
(0.0016)
-0.0012
(0.0016)
0.0017
(0.0016)

0.0338
0.0781
0.0001
0.083
0.012
2,853,939
179,706

Between Min
and Full
(4)
0.0008
(0.0023)
0.0015
(0.0023)
-0.0002
(0.0023)

Full no Extra
Payment
(5)
0.0021
(0.0026)
0.0084***
(0.0026)
0.0069***
(0.0026)

0.6637
0.4700
0.7734
0.195
0.026
2,853939
179,706

0.0600
0.5798
0.0147
0.557
0.025
2,853939
179,706

34

More than
Full
(6)
-0.0001
(0.0017)
-0.0020
(0.0017)
0.0000
(0.0017)

0.9534
0.2311
0.2529
0.068
0.009
2,853,939
179,706

Notes: OLS estimates of Equation 1 using diﬀerent payment values or ranges as dependent variables. SEs
between parenthesis. MinW is the Minimum warning, SBalW is the Statement Balance Warning, and
BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 35 -->

TABLE IV
SORTED CONDITIONAL AVERAGE TREATMENT EFFECTS
PER QUINTILE

35

Q1

Q2

Q3

Q4

Q5

Full Payment

-0.1
(0.7)
-0.2
(0.7)
0.4
(0.7)

MinW -0.8
0.1
(0.7)
(0.7)
SBalW -0.3
0.2
(0.7)
(0.7)
BothW 0.0
1.0
(0.7)
(0.7)
Payment less than the minimum
-0.7
(0.4)
-0.4
(0.4)
-0.8
(0.4)

-0.3
(0.4)
-0.4
(0.4)
-0.5
(0.4)

MinW -0.3
(0.4)
SBalW -0.2
(0.4)
BothW -0.2
(0.4)
Percentage of full
MinW -0.3
(0.6)
SBalW -0.3
(0.6)
BothW -0.2
(0.6)

-0.2
(0.6)
0.1
(0.6)
0.2
(0.6)

0.0
(0.6)
0.3
(0.6)
0.2
(0.6)

0.4
(0.7)
1.3
(0.7)
1.2
(0.7)

-0.9
(0.4)
-0.7
(0.4)
-0.9
(0.4)

0.8
(0.6)
1.0
(0.6)
0.9
(0.6)

1.4
(0.7)
2.4
(0.7)
1.6
(0.7)

-1.5
(0.4)
-1.2
(0.4)
-1.4
(0.4)

1.0
(0.6)
1.9
(0.6)
2.2
(0.6)

Best Linear
Predictor

β0

β1

1.01
(1.37)
1.00***
(0.41)
0.99**
(0.33)

1.00***
(0.27)
1.00***
(0.32)
1.01***
(0.26)

1.00
(0.90)
1.01***
(0.29)
1.00***
(0.28)

0.76***
(0.26)
0.54***
(0.26)
0.18
(0.27)

0.60*
(0.34)
0.16
(0.37)
0.16
(0.36)

0.65**
(0.27)
0.46*
(0.24)
0.50*
(0.29)

Notes: Conditional average treatment eﬀects for each quintile using
the control condition as baseline. SEs between parenthesis. MinW is
the Minimum warning, SBalW is the Statement Balance Warning, and
BothW is the Both Warnings condition. For the last two columns, β0
corresponds to the conditional average treatment eﬀect according to the
best linear predictor analysis. β1 works as an omnibus test of treatment
eﬀect heterogeneity. One-sided heteroskedasticity-robust (HC3) SEs are
between parentheses.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 36 -->

TABLE V
WARNINGS POST-TREATMENT EFFECT ON PAYMENT BEHAVIOR

Period

One Billing Cycle after Treatment

Two Billing Cycles after Treatment

36

MinW

Dep. Var.

Less than
Min
(1)
-0.0038*
(0.0021)
0.0005
(0.0022)
-0.0049**
(0.0021)
p-values from pairwise comparison

BothW

TotW

BothW vs. MinW
BothW vs. SBalW
SBalW vs. MinW

Baseline (Control)
R2
N observations
N cardholders

0.6101
0.0117
0.0440
0.138
0.012
2,853,949
179,706

Full

ln(payment)

(2)
-0.0007
(0.0027)
-0.0010
(0.0019)
0.0019
(0.0027)

0.4823
0.5001
0.9790
0.110
0.016
2,853,949
179,706

(3)
0.0557**
(0.0269)
0.0007
(0.0027)
0.0524*
(0.0270)

0.3327
0.2740
0.9002
0.559
0.149
2,853,949

179,706

Less than
Min
(4)
-0.0014
(0.0019)
-0.0015
(0.0026)
-0.0028
(0.0019)

0.5347
0.0963
0.2973
0.565
0.232
2,853,949
179,706

Full

ln(payment)

(5)
−0.00004
(0.0026)
0.0027
(0.0272)
-0.0017
(0.0026)

0.9016
0.0563
0.0418
10.238
0.396
2,853,949
179,706

(6)
-0.0121
(0.0267)
0.0245
(0.0267)
-0.0055
(0.0267)

0.8042
0.2626
0.1710
10.315
0.540
2,853,949
179,706

Notes: OLS estimates of Equation 1 using diﬀerent dependent variables for payment behavior one
billing cycle after the experiment (t+1) in columns 1 to 3, and two billing cycle after the experiment
(t+2) in columns 4 to 6. SEs between parenthesis. MinW is the Minimum warning, SBalW is the
Statement Balance Warning, and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 37 -->

Dep Var

MinW

SBalW

BothW

p-values from pairwise comparison

BothW vs MinW
BothW vs SBalW
SBalW vs MinW
Baseline (Control)
R2
N observations
N cardholders

Dep Var

MinW

SBalW

BothW

p-values from pairwise comparison

BothW vs MinW
BothW vs SBalW
SBalW vs MinW
Baseline (Control)
R2
N observations
N cardholders

No
Payment
(1)
-0.0053***
(0.0017)
-0.0048***
(0.0017)
-0.0063***
(0.0017)

0.5521
0.3689
0.7593
0.082
0.006
2,853,939
179,706

Payment
]40,60%]
(10)
0.0002
(0.0012)
0.0005
(0.0012)
0.0009
(0.0012)

0.5616
0.7219
0.8225
0.033
0.002
2,853,939
179,706

TABLE VI
WARNINGS EFFECT ON SMALL PAYMENT RANGES

Payment
]0,20%min]
(2)
0.0001
(0.0002)
−0.00003
(0.0002)
-0.0003
(0.0002)

0.0941
0.2055
0.6613
0.001
0.000
2,853,939
179,706

Payment
]20,40%]
(3)
0.0001
(0.0003)
0.0002
(0.0003)
0.0001
(0.0003)

0.9689
0.7387
0.7067
0.001
0.001
2,853,939
179,706

Payment
]40,60%]
(4)
-0.0011***
(0.0004)
-0.0003
(0.0004)
-0.0003
(0.0004)

0.0424
0.9166
0.0530
0.004
0.005
2,853,939
179,706

Payment
]60,80%]
(5)
-0.0009**
(0.0004)
-0.0007*
(0.0004)
-0.0007
(0.0004)

0.5806
0.9174
0.6521
0.004
0.002
2,853,939
179,706

Payment
]80,99%]
(6)
-0.0009*
(0.0005)
-0.0011**
(0.0005)
-0.0010**
(0.0004)

0.7104
0.9276
0.6459
0.005
0.002
2,853,939
179,706

Exact
Min
(7)
0.0052***
(0.0016)
-0.0012
(0.0016)
0.0017
(0.0016)

0.0338
0.0781
0.0001
0.083
0.012
2,853,939
179,706

Payment
]min,20%full]
(8)
0.0010
(0.0016)
0.0002
(0.0016)
0.0014
(0.0016)

0.7892
0.4241
0.5959
0.075
0.015
2,853,939
179,706

Payment
]20,40%]
(9)
0.0011
(0.0014)
-0.0009
(0.0014)
-0.0030**
(0.0014)

0.0023
0.1118
0.1498
0.046
0.003
2,853,939
179,706

Payment
]60,80%]
(11)
-0.0002
(0.0010)
0.0021**
(0.0010)
0.0007
(0.0010)

0.4175
0.1826
0.0316
0.024
0.001
2,853,939
179,706

Payment
]80,99%]
(12)
-0.0013
(0.0009)
-0.0004
(0.0009)
-0.0001
(0.0009)

0.1720
0.8031
0.2697
0.017
0.001
2,853,939
179,706

Exact
Full
(13)
0.0037
(0.0026)
0.0077***
(0.0026)
0.0057*
(0.0026)

0.4438
0.4431
0.1245
0.534
0.022
2,853,939
179,706

Payment
]full,120%]
(14)
-0.0002
(0.0006)
0.0003
(0.0007)
0.0011
(0.0007)

0.0487
0.2247
0.4469
0.009
0.000
2,853,939
179,706

Payment
]120,140%]
(15)
-0.00004
(0.0005)
-0.0002
(0.0005)
0.0001
(0.0005)

0.8444
0.5283
0.6643
0.005
0.000
2,853,939
179,706

Payment
]140,160%]
(16)
0.0001
(0.0004)
-0.0006
(0.0004)
-0.0006
(0.0004)

0.0595
0.9864
0.0596
0.003
0.000
2,853,939
179,706

Payment
]160%+ full]
(17)
-0.0010
(0.0012)
0.0007
(0.0012)
0.0000
(0.0012)

0.4039
0.5878
0.1686
0.030
0.010
2,853,939
179,706

3
7

Notes: OLS estimates of Equation 1 using diﬀerent payment ranges as dependent variables. SEs between parenthesis. MinW is the
Minimum warning, SBalW is the Statement Balance Warning, and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 38 -->

TABLE VII
WARNINGS EFFECT BASED ON PREVIOUS PAYMENT BEHAVIOR, THE MINIMUM PAYMENT AND THE STATEMENT BALANCE

Subsample

Dep. Var.

Likely
Paid Less
than Min
Percentage
of Full
(1)
0.0354**
(0.0172)
0.0184
(0.0174)
0.0377**
(0.0175)

Between
Min and
Full
Percentage
of Full
(2)
0.0019
(0.0050)
0.0148***
(0.0051)
0.0090*
(0.0051)

Low MAD
Percentage of
Full
Percentage
of Full
(3)
0.0011
(0.0018)
0.0022
(0.0018)
0.0040**
(0.0018)

High MAD
Percentage of
Full
Percentage
of Full
(4)
0.0048
(0.0033)
0.0113***
(0.0033)
0.0097***
(0.0033)

Small Diﬀ
between Min
and Stat. Bal.
Percentage
of Full
(5)
0.0034
(0.0028)
0.0081***
(0.0028)
0.0104***
(0.0028)

Large Diﬀ
between Min
and Stat. Bal.
Percentage
of Full
(6)
0.0029
(0.0026)
0.0053*
(0.0026)
0.0037
(0.0026)

MinW

SBalW

BothW

p-values from pairwise comparison

BothW vs MinW
BothW vs SBalW
SBalW vs MinW
Baseline (Control)
R2
N observations
N cardholders

0.8917
0.2669
0.3200
0.506
0.078
65,213
5,026

0.1661
0.2548
0.0107
0.489
0.136
429,016
25,793

0.0989
0.3156
0.5241
0.846
0.044
1,449,756
89,435

0.1459
0.6330
0.0536
0.638
0.051
1,404,183
90,271

0.0113
0.4062
0.0890
0.846
0.027
1,332,393
89,851

0.7600
0.5355
0.3539
0.637
0.065
1,521,546
89,855

Low
Statement
Balance
Percentage
of Full
(7)
0.0031
(0.0028)
0.0075***
(0.0028)
0.0085***
(0.0028)

0.0545
0.7242
0.1173
0.829
0.024
1,317,171
89,838

High
Statement
Balance
Percentage
of Full
(8)
0.0032
(0.0025)
0.0061**
(0.0025)
0.0057**
(0.0025)

0.3351
0.8518
0.2495
0.653
0.067
1,536,768
89,868

Low
Min

High
Min

Percentage
of Full
(9)
0.0050*
(0.0029)
0.0087***
(0.0029)
0.0101***
(0.0029)

0.0752
0.6154
0.2043
0.771
0.023
1,312,390
89,766

Percentage
of Full
(10)
0.0011
(0.0025)
0.0050**
(0.0025)
0.0041
(0.0025)

0.2388
0.7046
0.1182
0.711
0.064
1,541,549
89,940

Notes: OLS estimates of Equation 1 using the percentage of the statement balance paid (“Percentage of Full”) as dependent variable. Each column is a diﬀerent subsample:
column 1 shows debtors who usually failed to pay at least the minimum before the experiment, column 2 those who usually paid between the minimum and the statement
balance (i.e., a revolving amount) before the experiment, column 3 (column 4) the debtors with a relatively low (high) mean absolute deviation from the fraction paid,
column 5 (column 6) the debtors who saw a relatively small (large) diﬀerence between the minimum payment and the statement balance, column 7 (column 8) the debtors
who saw a relatively high (low) statement balance, and column 9 (column 10) the debtors who saw a relatively high (low) minimum payment amount. SEs are between
parenthesis. MinW is the Minimum warning, SBalW is the Statement Balance Warning, and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

3
8

---

<!-- PAGE 39 -->

39

TABLE VIII
WARNINGS EFFECT BASED ON
INCOME AND SHARE OF DEBT LEVELS

Subsample

Dep. Var.

Low
income
Percentage
of Full
(1)
0.0013
(0.0027)
0.0085***
(0.0026)
0.0054**
(0.0027)

MinW

SBalW

BothW

p-values from pairwise comparison

BothW vs MinW
BothW vs SBalW
SBalW vs MinW
Baseline (Control)
R2
N observations
N cardholders

0.1201
0.2437
0.0065
0.760
0.042
1,389,575
89,654

High
income
Percentage
of Full
(2)
0.0048*
(0.0027)
0.0051*
(0.0027)
0.0088***
(0.0027)

0.1463
0.1795
0.9238
0.722
0.043
1,464,364
90,052

Low score
share of debt
Percentage
of Full
(3)
0.0045
(0.0029)
0.0076***
(0.0029)
0.0090***
(0.0029)

High score
share of debt
Percentage
of Full
(4)
0.0016
(0.0025)
0.0061**
(0.0025)
0.0051**
(0.0025)

0.1217
0.6332
0.2846
0.710
0.038
1,391,292
89,833

0.1557
0.6767
0.0666
0.772
0.044
1,462,647
89,873

Notes: OLS estimates of Equation 1 using the percentage of the statement bal-
ance paid (“Percentage of Full”) as dependent variable. Each column is a diﬀer-
ent subsample: column 1 (column 2) shows debtors with a relatively low (high)
income, and column 3 (column 4) debtors with a relatively low (high) share of
their debt with the lender. SEs are between parenthesis. MinW is the Minimum
warning, SBalW is the Statement Balance Warning, and BothW is the Both
Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 40 -->

40

TABLE IX
WARNINGS EFFECT ON PAYMENT DECISIONS AND UNDERSTANDING
THROUGH AN ONLINE EXPERIMENT

Dep. Var.

MinW

SBalW

BothW

Min

(1)
0.028
(0.051)
-0.008
(0.051)
-0.080
(0.050)

Between
Min and Full
(2)
-0.027
(0.056)
-0.177***
(0.059)
-0.180***
(0.059)

Full

(3)
-0.000
(0.068)
0.185***
(0.067)
0.260***
(0.067)

Percentage
of Full
(4)
0.004
(0.060)
0.154***
(0.059)
0.222***
(0.059)

Understanding
Minimum
(5)
0.207
(0.146)
0.243*
(0.145)
0.233
(0.144)

Understanding
Statement Balance
(6)
0.124
(0.149)
0.233
(0.148)
0.311**
(0.147)

p-values from pairwise comparison

BothW vs MinW
BothW vs SBalW
SBalW vs MinW
Baseline (Control)
R2
N observations

0.035
0.156
0.484
0.170
0.012
400

0.011
0.958
0.013
0.337
0.038
400

0.000
0.265
0.007
0.495
0.055
400

0.000
0.247
0.012
0.570
0.051
400

0.862
0.944
0.809
6.277
0.009
400

0.211
0.596
0.470
6.267
0.013
400

Notes: OLS estimates of Equation 1 using diﬀerent dependent variables in the online experiment. Columns 1 to 4
use the payments decisions. Columns 5 and 6 use self-reported measures of understanding the minimum payment
and the statement balance. SEs are between parenthesis. MinW is the Minimum warning, SBalW is the Statement
Balance Warning, and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 41 -->

IX. FIGURES

41

Figure 1. CHANGES IN PAYMENT DISTRIBUTION (WITH THE CONTROL CONDITION AS THE BASE-

LINE)

(a) Panel A

(b) Panel B

Notes: Each panel contains the average treatment eﬀects for each warning, where the baseline is the control
condition, on the likelihood of each of the possible payments (from Table III). Error bars indicate 95% conﬁdence
intervals.

(c) Panel C

---

<!-- PAGE 42 -->

Figure 2. WARNINGS ESTIMATED CATE BASED ON PREVIOUS PAYMENT BEHAVIOR, THE MINIMUM

AND THE STATEMENT BALANCE AMOUNTS

42

(a) Previous Percentage of Full (%)

(b) MAD Percentage of Full

(c) Diﬀerence between the minimum and the statement balance amounts ($)

(d) Statement Balance ($)

Notes: This Figure shows the estimated conditional average treatment eﬀects on the fraction paid on the y-axis,
and each panel uses a diﬀerent covariable in the x-axis. The dashed lines are the benchmark for the estimated
conditional average treatment eﬀect for each warning compared to the control condition. Error bars indicate 95%
conﬁdence intervals.

---

<!-- PAGE 43 -->

Figure 3. WARNINGS ESTIMATED CATE BASED ON INCOME AND SHARE OF DEBT

43

(a) Income

(b) Share of Debt Score

Notes: This Figure shows the estimated conditional average treatment eﬀects on the fraction paid on the y-axis,
and each panel uses a diﬀerent covariable in the x-axis. Panel (a) uses debtors’ income (in US dollars) re-scaled
using a statement balance of $1,949.28. Panel (b) uses a re-scaled share of debt (0: people who have all their debt
with other lenders, and 2.14: they have all their debt with the ﬁrm). The dashed lines are the benchmark for the
estimated conditional average treatment eﬀect for each warning compared to the control condition. Error bars
indicate 95% conﬁdence intervals.

---

<!-- PAGE 44 -->

APPENDIX (FOR ONLINE PUBLICATION)

1

A1. Pilot Study

The following study was part of a diﬀerent study examining the role of payment re-
minders with the same Latin American credit card issuer as in the ﬁeld experiment in this
paper but conducted more than two years before. There were seven treatment conditions
sent by email and a control condition.31 The sample size varied from 20 to 30 thousand
for each treatment condition, and it was 251 thousand for the control.

• Simple reminder: “We remind you that your [card name] is due on [date].”

• Full amount only: [Simple reminder] + statement balance ($) amount in bold.

• Statement balance warning (beneﬁt framing):

[simple remainder] + statement bal-
ance ($) amount in bold + the warning: “If you pay the statement balance before the
due date, you will avoid additional interest charges.” [same as in the ﬁeld experiment]

• Statement balance warning (cost framing):

[simple reminder] + statement balance
($) amount in bold + the warning: “If you pay less than the statement balance, your
outstanding balance will accrue interest charges in your next billing cycle.”

• Statement balance warning (cost framing) and adding minimum: [simple reminder] +
statement balance ($) amount in bold + minimum ($) amount in bold + the warning:
“If you pay less than the statement balance, your outstanding balance will accrue
interest charges in your next billing cycle.”

• Placebo: “Remember these tips and protect your password.” [and a list of standard

tips]

• Control condition: People did not receive any email.

Table A1 shows the average treatment eﬀects from linear regression models using each
experimental condition as an independent variable where the baseline was the control con-
dition. The dependent variables were the likelihood of paying in full, not paying at least
the minimum, and the fraction of the statement balance.

The results indicate that all warning messages increase the likelihood of paying in full,
reduce the likelihood of not paying at least the minimum, and increase the percentage of the
fraction paid compared to the control group. In particular, the most successful statement
balance warning message is the one framed as a beneﬁt, and therefore that one was used for
this paper, increasing the likelihood of paying in full by 2 percent (1.3 percentage points)

31In addition, reminders were sent at diﬀerent times before the payment due date, but this factor is not analyzed

here.

---

<!-- PAGE 45 -->

more than the control group. Secondly, the condition using only the statement balance
amount and no warning (“Full amount only”) is not statistically signiﬁcantly diﬀerent from
the control group. Third, a simple reminder by itself increases the likelihood of paying in
full by 1.1 percent (0.7 percentage points) and, given the null result from the placebo,
indicates that the eﬀect is coming from reminding people and not from the contact from
the ﬁrm.

2

TABLE A1
AVERAGE TREATMENT EFFECTS OF THE PILOT STUDY

Dep. Var.

Full

Placebo

Simple reminder

SBalW (beneﬁt framing)

SBalW (cost framing)

SBalW (cost framing) & adding min.

Full amount only

R2
N observations

Notes: SEs between parenthesis.
* p < 0.10, ** p < 0.05, *** p < 0.01

(1)
0.0002
(0.0030)
0.0071**
(0.0029)
0.0131***
(0.0028)
0.0087***
(0.0028)
0.0030
(0.0028)
0.0035
(0.0035)
0.0001
411,309

Less than
Min
(2)
-0.0016
(0.0022)
-0.0052**
(0.0021)
-0.0070***
(0.0021)
-0.0073***
(0.0021)
-0.0051**
(0.0021)
-0.0034
(0.0025)
0.0001
411,309

Percentage
of Full
(3)
0.0001
(0.0025)
0.0079***
(0.0024)
0.0107***
(0.0023)
0.0082***
(0.0023)
0.0050**
(0.0023)
0.0030
(0.0028)
0.0001
411,309

---

<!-- PAGE 46 -->

3

TABLE A2
WARNINGS EFFECT ON MAIN PAYMENT
DISTRIBUTION USING A LOGIT MODEL

Dep. Var.

MinW

SBalW

BothW

ll
N observations

Less than
Min
(1)
-0.0860***
(0.0236)
-0.0706***
(0.0236)
-0.0980***
(0.0237)
-50,985.808
179,706

Min

Full

(2)
0.0825***
(0.0246)
-0.0141
(0.0251)
0.0441*
(0.0248)
-47,627.145
179,706

(3)
0.0150
(0.0154)
0.0369**
(0.0154)
0.0404***
(0.0154)
-99,445.711
179,706

Notes: Logit model estimates for the treatment period
using the main payment values or ranges as dependent
variables. SEs between parenthesis. MinW is the Mini-
mum warning, SBalW is the Statement Balance Warning,
and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 47 -->

TABLE A3
WARNINGS EFFECT ON MAIN PAYMENT DISTRIBUTION

Dep. Var.

MinW

SBalW

BothW

Time eﬀects
Xs

Less than
Min
(1)
-0.0079***
(0.0018)
-0.0066***
(0.0019)
-0.0083***
(0.0019)
No
No

Less than
Min
(2)
-0.0079***
(0.0018)
-0.0066***
(0.0019)
-0.0083***
(0.0019)
Yes
No

Less than
Min
(3)
-0.0079***
(0.0018)
-0.0067***
(0.0019)
-0.0085***
(0.0019)
Yes
Yes

Min

Min

Min

Full

Full

Full

(4)
0.0050***
(0.0017)
-0.0012
(0.0016)
0.0015
(0.0016)
No
No

(5)
0.0049***
(0.0017)
-0.0012
(0.0016)
0.0015
(0.0016)
Yes
No

(6)
0.0052***
(0.0016)
-0.0012
(0.0016)
0.0017
(0.0016)
Yes
Yes

(7)
0.0027
(0.0026)
0.0066***
(0.0026)
0.0075***
(0.0026)
No
No

(8)
0.0027
(0.0026)
0.0066**
(0.0026)
0.0075***
(0.0026)
Yes
No

(9)
0.0020
(0.0025)
0.0066***
(0.0025)
0.0069***
(0.0025)
Yes
Yes

R2
N observations
N cardholders

0.000
2,853,949
179,706

0.001
2,853,949
179,706

0.003
2,853,939
179,706

0.000
2,853,949
179,706

0.003
2,853,949
179,706

0.012
2,853,939
179,706

0.000
2,853,949
179,706

0.002
2,853,949
179,706

0.036
2,853,939
179,706

Notes: OLS estimates of Equation 1 using diﬀerent main payment values or ranges as dependent variables. SEs between parenthesis.
MinW is the Minimum warning, SBalW is the Statement Balance Warning, and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

4

---

<!-- PAGE 48 -->

5

TABLE A4
WARNINGS EFFECT ON MAIN PAYMENT
DISTRIBUTION INCLUDING ALL ACCOUNTS

Dep. Var.

MinW

SBalW

BothW

R2
N observations
N cardholders

Less than
Min
(1)
-0.0082***
(0.0019)
-0.0073***
(0.0019)
-0.0090***
(0.0019)
0.006
3,112,110
179,753

Min

Full

(2)
0.0052***
(0.0016)
-0.0013
(0.0016)
0.0019
(0.0016)
0.013
3,112,110
179,753

(3)
0.0025
(0.0025)
0.0063**
(0.0025)
0.0063**
(0.0025)
0.033
3,112,110
179,753

Notes: OLS estimates of Equation 1 using diﬀer-
ent main payment values or ranges as dependent
variables. SEs between parenthesis. MinW is the
Minimum warning, SBalW is the Statement Balance
Warning, and BothW is the Both Warnings condi-
tion.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 49 -->

6

TABLE A5
RELATIVE CHANGE IN
CONDITIONAL AVERAGE TREATMENT
EFFECTS PER QUINTILE

Q1

Q2

Q3

Q4

Q5

Full Payment

MinW

-0.1
59.0
-0.1
-0.3
57.4
-0.2
0.8
50.2
0.4

-1.1
69.0
-0.8
SBalW -0.5
68.8
-0.3
BothW 0.0
65.8
0.0

0.2
70.5
0.1
0.2
64.9
0.2
1.5
67.0
1.0
Payment less than the minimum
-11.3
5.8
-0.7
-8.3
4.7
-0.4
-18.7
4.4
-0.8

-4.0
21.1
-0.9
-3.2
21.6
-0.7
-8.5
10.9
-0.9

MinW -15.5

9.9
-1.5
SBalW -11.8
10.1
-1.2
BothW -5.8
24.0
-1.4
Percentage of full
-0.4
63.9
-0.3
SBalW -0.4
75.5
-0.3
BothW -0.2
80.4
-0.2

MinW

-0.2
77.9
-0.2
0.2
79.7
0.1
0.2
79.8
0.2

0.0
77.8
0.0
0.4
82.2
0.3
0.3
70.1
0.2

0.7
51.7
0.4
2.1
62.8
1.3
1.7
69.8
1.2

-7.9
4.1
-0.3
-4.4
8.3
-0.4
-15.0
3.3
-0.5

1.0
81.0
0.8
1.5
67.6
1.0
1.2
73.3
0.9

2.3
62.7
1.4
4.0
58.8
2.4
2.6
59.7
1.6

-3.3
7.6
-0.3
-5.9
3.6
-0.2
-3.8
5.6
-0.2

1.4
70.1
1.0
2.9
65.7
1.9
3.2
67.0
2.2

Notes: The ﬁrst row shows the relative change
in the conditional average treatment eﬀect
(CATE) for each quintile. The second row
(smaller font and italics) shows the the base-
line from the control group. The third row
(smaller font and italics) is the CATE in per-
centage points as shown in Table IV. MinW
is the Minimum warning, SBalW is the State-
ment Balance Warning, and BothW is the Both
Warnings condition.

---

<!-- PAGE 50 -->

7

TABLE A6
SORTED CONDITIONAL AVERAGE TREATMENT EFFECTS
PER QUINTILE BETWEEN WARNINGS

Q1

Q2

Q3

Q4

Q5

Full Payment

MinW (vs. BothW)

MinW (vs. SBalW)

BothW (vs. SBalW)

-2.0
(0.7)
-1.2
(0.7)
-1.1
(0.7)

Payment less than the minimum

MinW (vs. BothW)

MinW (vs. SBalW)

BothW (vs. SBalW)

Percentage of full

MinW (vs. BothW)

MinW (vs. SBalW)

BothW (vs. SBalW)

-0.9
(0.4)
-0.8
(0.4)
-0.2
(0.4)

-1.7
(0.6)
-0.7
(0.5)
-0.4
(0.6)

-1.2
(0.7)
-0.6
(0.7)
-0.6
(0.7)

-0.3
(0.4)
-0.5
(0.4)
0.1
(0.4)

-0.6
(0.6)
-0.6
(0.5)
-0.1
(0.6)

-0.7
(0.7)
-0.5
(0.7)
0.4
(0.7)

-0.2
(0.4)
-0.3
(0.4)
0.2
(0.4)

-0.2
(0.6)
-0.3
(0.5)
0.1
(0.6)

0.5
(0.7)
0.0
(0.7)
0.5
(0.7)

0.9
(0.4)
0.3
(0.4)
0.4
(0.4)

0.1
(0.6)
-0.2
(0.5)
0.2
(0.6)

1.2
(0.7)
0.3
(0.7)
0.6
(0.7)

1.1
(0.4)
0.7
(0.4)
0.6
(0.4)

0.4
(0.6)
-0.2
(0.5)
0.2
(0.6)

Best Linear
Predictor
β1
β0

1.01**
(0.42)
1.00*
(0.57)
1.05
(1.88)

1.21
(4.92)
1.00
(1.93)
1.02
(1.28)

1.01**
(0.38)
1.00**
(0.43)
1.00
(4.23)

-0.02
(0.31)
-0.34
(0.29)
-0.25
(0.29)

0.50*
(0.26)
0.09
(0.42)
-0.14
(0.42)

0.29
(0.29)
-0.23
(0.28)
0.31
(0.28)

Notes: Conditional average treatment eﬀects for each quintile between warning
conditions. The baseline is indicated as the second group after “vs.” SEs between
parenthesis. MinW is the Minimum warning, SBalW is the Statement Balance
Warning, and BothW is the Both Warnings condition. For the last two columns,
β0 corresponds to the conditional average treatment eﬀect from the best linear
predictor analysis. β1 works as an omnibus test for treatment eﬀect heterogeneity.
One-sided heteroskedasticity-robust (HC3) SEs are between parentheses .
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 51 -->

8

TABLE A7
WARNINGS EFFECTS ON PAYMENT DISTRIBUTION
BASED ON PREVIOUS PAYMENT BEHAVIOR

Panel A - Likely paid less than the Min

0.8991
0.1352
0.1699
0.364
0.107
65,213
5,026

MinW

SBalW

BothW

Dep Var

Less than
Min
(1)
-0.0479**
(0.0212)
-0.0193
(0.0212)
-0.0506**
(0.0213)

p-values for pairwise comparison

BothW vs MinW
BothW vs SBalW
SBalW vs MinW

Baseline(Control)
R2
N observation
N cardholders
Panel B - Likely paid between Min and Full
Less than
Min
(1)
-0.0084*
(0.0048)
-0.0085*
(0.0047)
-0.0095**
(0.0048)

Dep Var

BothW

SBalW

MinW

p-values for pairwise comparison

BothW vs MinW
BothW vs SBalW
SBalW vs MinW

Baseline(Control)
R2
N observations
N cardholders

0.8176
0.8332
0.9830
0.086
0.010
429,016
25,793

Min

(2)
0.0229*
(0.0132)
-0.0007
(0.0127)
0.0155
(0.0130)

0.5834
0.2141
0.0729
0.083
0.010
65,213
5,026

Min

(2)
0.0001
(0.0053)
-0.0100*
(0.0051)
-0.0108**
(0.0052)

0.0351
0.8694
0.0506
0.099
0.011
429,016
25,793

Between
Min and Full
(3)
0.0100
(0.0157)
-0.0070
(0.0153)
0.0137
(0.0157)

0.8131
0.1776
0.2681
0.152
0.033
65,213
5,026

Between
Min and Full
(3)
0.0139*
(0.0084)
0.0104
(0.0083)
0.0150*
(0.0084)

0.8975
0.5865
0.6776
0.607
0.117
429,016
25,793

Full

(4)
0.0157
(0.0188)
0.0253
(0.0189)
0.0212
(0.0191)

0.7691
0.8252
0.6034
0.401
0.051
65,213
5,026

Full

(4)
-0.0052
(0.0068)
0.0081
(0.0068)
0.0052
(0.0069)

0.1330
0.6813
0.0524
0.207
0.131
429,016
25,793

Notes: OLS estimates of Equation 1 using diﬀerent main payment values or ranges
as dependent variables. Columns in Panel A include a sub-sample of debtors who
usually failed to pay or paid less than the minimum before the experiment. Columns
in Panel B include a sub-sample of debtors who usually paid between the minimum
and the statement balance before the experiment. SEs between parenthesis. MinW
is the Minimum warning, SBalW is the Statement Balance Warning, and BothW is
the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 52 -->

WARNINGS EFFECT BASED ON PREVIOUS PAYMENT BEHAVIOR, THE MINIMUM AND
THE STATEMENT BALANCE AMOUNTS USING INTERACTIONS

TABLE A8

Percentage
of full
(1)
0.0013
(0.0020)
0.0026
(0.0020)
0.0041**
(0.0020)
MAD previous
% of full (%)
0.0129
(0.0159)
0.0312**
(0.0159)
0.0205
(0.0158)

0.040
2,851,884
178,870

Percentage
of full
(2)
0.0013
(0.0020)
0.0014
(0.0020)
0.0037*
(0.0019)
MAD previous
% of full (%)
0.0105
(0.0459)
0.0658
(0.0462)
0.0276
(0.0460)
0.0059
(0.1311)
-0.0905
(0.1317)
-0.0121
(0.1314)
0.040
2,851,884
178,870

Percentage
of full
(3)
0.0046**
(0.0023)
0.0075***
(0.0023)
0.0078***
(0.0023)
Diﬀ between
SB and min ($)
-0.0010
(0.0007)
-0.0004
(0.0007)
-0.0005
(0.0007)

0.040
2,853,939
179,706

Percentage
of full
(4)
0.0021
(0.0027)
0.0054**
(0.0028)
0.0060**
(0.0026)
Diﬀ between
SB and min ($)
0.0017
(0.0018)
0.0019
(0.0019)
0.0019
(0.0017)
-0.0002
(0.0001)
-0.0002
(0.0001)
-0.0002**
(0.0001)
0.040
2,853,939
179,706

Percentage
of full
(5)
0.0049**
(0.0024)
0.0077***
(0.0024)
0.0081***
(0.0024)
Statement
Balance ($)
-0.0009
(0.0007)
-0.0005
(0.0007)
-0.0005
(0.0007)

0.040
2,853,939
179,706

Percentage
of full
(6)
0.0022
(0.0029)
0.0055*
(0.0030)
0.0065**
(0.0029)
Statement
Balance ($)
0.0012
(0.0016)
0.0015
(0.0017)
0.0012
(0.0015)
-0.0001
(0.0001)
-0.0001
(0.0001)
-0.0001*
(0.0001)
0.040
2,853,939
179,706

Percentage
of full
(7)
0.0053**
(0.0025)
0.0080***
(0.0025)
0.0090***
(0.0026)

Percentage
of full
(8)
0.0061**
(0.0029)
0.0099***
(0.0030)
0.0130***
(0.0030)

Minimum ($) Minimum ($)

-0.0053
(0.0036)
-0.0029
(0.0036)
-0.0047
(0.0037)

0,04
2,853,939
179,706

-0.0094
(0.0066)
-0.0109
(0.0070)
-0.0210***
(0.0069)
0.0022
(0.0022)
0.0033
(0.0024)
0.0062***
(0.0024)
0,04
2,853,939
179,706

Dep Var

MinW

SBalW

BothW

X=

MinW × X

SBalW × X

BothW × X

MinW × X 2

SBalW × X 2

BothW × X 2

R2
N observation
N cardholders

Notes: OLS estimates of Equation 1 plus the main eﬀect of a covariate (X) and its linear and quadratic interaction with the warnings conditions. All models
using the percentage paid of the statement balance (“Percentage of Full”) as the dependent variable. SEs between parenthesis. MinW is the Minimum warning, SBalW
is the Statement Balance Warning, and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

9

---

<!-- PAGE 53 -->

TABLE A9
COVARIATES FOR EACH QUINTILE - MINIMUM PAYMENT WARNING

10

CATE Fraction Paid (%)

Age (years)

Male (%)

Mean previous % of full (%)

MAD previous % of full (%)

Statement balance ($)

Diﬀerence between SB and min ($)

Previous payment ($)

Monthly income ($)

Share of Debt Score (0 to 2.1)

Company’s credit score (0-100)

Mean email opening rate (%)

Q1
-0.3
(0.6)
42.0
(0.10)
48.7
(0.4)
65.8
(0.2)
17.0
(0.1)
2,420
(30)
1,953
(27)
1,409
(24)
3,809
(25)
0.9
(0.01)
56.0
(0.12)
50.0
(0.2)

Minimum Payment Warning
Q3
0.0
(0.6)
44.9
(0.10)
48.3
(0.4)
79.8
(0.2)
11.6
(0.1)
1,816
(21)
1,432
(18)
1,144
(11)
3,689
(22)
1.0
(0.01)
67.8
(0.12)
51.1
(0.2)

Q4
0.8
(0.6)
45.5
(0.10)
47.4
(0.4)
83.2
(0.2)
8.9
(0.1)
1,776
(18)
1,365
(16)
1,224
(12)
3,417
(20)
1.1
(0.01)
67.8
(0.12)
51.6
(0.2)

Q2
-0.2
(0.6)
44.4
(0.10)
48.9
(0.4)
80.0
(0.2)
9.5
(0.1)
2,028
(20)
1,547
(18)
1,328
(15)
3,389
(21)
1.1
(0.01)
64.5
(0.11)
51.4
(0.2)

Q5
1.0
(0.6)
45.0
(0.10)
49.1
(0.4)
70.2
(0.2)
22.0
(0.1)
1,701
(22)
1,371
(20)
919
(11)
3,942
(23)
0.9
(0.01)
65.2
(0.15)
50.0
(0.2)

Notes: For the minimum-payment warning (vs. control) analysis, quintiles are
sorted by the conditional average treatment eﬀects on the fraction paid. Each
row shows the mean value for each covariate and standard errors are between
parenthesis. For reasons of conﬁdentiality, monetary amounts ($) were re-scaled
using a statement balance of $1,949.28 (in US dollars). Share of debt score was
re-scaled (0: people who owe other lenders, and 2.14: they owe all their debt to
the ﬁrm). Credit score was re-scaled where 100 was the best score (lowest risk).

---

<!-- PAGE 54 -->

11

TABLE A10
COVARIATES FOR EACH QUINTILE - STATEMENT BALANCE WARNING

Statement Balance Warning

CATE Fraction Paid (%)

Age (years)

Male (%)

Mean previous % of full (%)

MAD previous % of full (%)

Statement balance ($)

Diﬀerence between SB and min ($)

Previous payment ($)

Monthly income ($)

Share of Debt Score (0 to 2.1)

Company’s credit score (0-100)

Mean email opening rate (%)

Q1
-0.3
(0.6)
44.2
(0.10)
50
(0.4)
78.6
(0.2)
9.9
(0.1)
2,026
(29)
1,646
(26)
1,242
(21)
3,775
(23)
0.9
(0.01)
61.4
(0.14)
50.7
(0.2)

Q2
0.1
(0.6)
44.6
(0.10)
47.7
(0.4)
82.7
(0.2)
8.5
(0.1)
1,903
(20)
1,457
(18)
1,280
(13)
3,487
(22)
1.1
(0.01)
66.6
(0.12)
51.4
(0.2)

Q3
0.3
(0.6)
45.5
(0.10)
50.3
(0.4)
84.9
(0.2)
6.7
(0.1)
2,064
(22)
1,575
(20)
1,518
(18)
3,642
(22)
1.1
(0.01)
67.3
(0.12)
51.9
(0.2)

Q4
1.0
(0.6)
43.5
(0.10)
47.8
(0.4)
70.3
(0.2)
16.6
(0.1)
2,205
(23)
1,755
(20)
1,190
(12)
3,742
(23)
1.0
(0.01)
63.2
(0.12)
50.3
(0.2)

Q5
1.9
(0.6)
44
(0.10)
46.2
(0.4)
62.4
(0.2)
27.2
(0.1)
1,560
(18)
1,244
(16)
794
(10)
3,553
(22)
0.9
(0.01)
62.6
(0.14)
49.1
(0.2)

Notes: For the statement balance warning (vs. control) analysis, quintiles are
sorted by the conditional average treatment eﬀects on the fraction paid. Each
row shows the mean value for each covariate and standard errors are between
parenthesis. For reasons of conﬁdentiality, monetary amounts ($) were re-scaled
using a statement balance of $1,949.28 (in US dollars). Share of debt score was
re-scaled (0: people who owe other lenders, and 2.14: they owe all their debt to
the ﬁrm). Credit score was re-scaled where 100 was the best score (lowest risk).

---

<!-- PAGE 55 -->

TABLE A11
COVARIATES FOR EACH QUINTILE - BOTH WARNINGS

CATE Fraction Paid (%)

Age (years)

Male (%)

Mean previous % of full (%)

MAD previous % of full (%)

Statement balance ($)

Diﬀerence between SB and min ($)

Previous payment ($)

Monthly income ($)

Share of Debt Score (0 to 2.1)

Company’s credit score (0-100)

Mean email opening rate (%)

Q1
-0.2
(0.6)
44.5
(0.10)
48.4
(0.4)
82.4
(0.2)
8.8
(0.1)
2,065
(22)
1,615
(20)
1,514
(18)
3,582
(22)
1.1
(0.01)
66.6
(0.12)
51.6
(0.2)

Both Warnings
Q3
0.2
(0.6)
42.8
(0.10)
50.7
(0.4)
73.1
(0.2)
10.6
(0.1)
2,722
(26)
2,133
(24)
1,774
(22)
4,053
(25)
1.0
(0.01)
60.8
(0.13)
51.7
(0.2)

Q2
0.2
(0.6)
44.6
(0.10)
47.9
(0.4)
81.4
(0.2)
10.4
(0.1)
1,743
(21)
1,364
(19)
1,153
(14)
3,456
(21)
1.1
(0.01)
66.3
(0.12)
50.9
(0.2)

Q4
0.9
(0.6)
44.5
(0.10)
47.8
(0.4)
75.3
(0.2)
14.8
(0.1)
1,732
(21)
1,369
(19)
944
(11)
3,511
(21)
1.0
(0.01)
64
(0.12)
50.0
(0.2)

12

Q5
2.2
(0.6)
45.5
(0.10)
46.8
(0.4)
66.5
(0.2)
24.4
(0.1)
1,514
(24)
1,217
(21)
686
(9)
3,641
(23)
0.8
(0.01)
63.6
(0.14)
49.6
(0.2)

Notes: For the both warning (vs. control) analysis, quintiles are sorted by the
conditional average treatment eﬀects on the fraction paid. Each row shows
the mean value for each covariate and standard errors are between parenthesis.
For reasons of conﬁdentiality, monetary amounts ($) were re-scaled using a
statement balance of $1,949.28 (in US dollars). Share of debt score was re-
scaled (0: people who owe other lenders, and 2.14: they owe all their debt to
the ﬁrm). Credit score was re-scaled where 100 was the best score (lowest risk).

---

<!-- PAGE 56 -->

13

A12. Material of online experiment

• Are you more familiar with U.S. dollars or British pounds?

◦ $ (US Dollar)
◦ £ (British Pound)
◦ I am not familiar with any of these currencies.

• Payment information
Imagine that you own a credit card and you are about to make your monthly repayment.

The next screen will show summary information from your credit card balance.

Please consider how much you can aﬀord to pay, and treat your payment decision as you

would in your everyday life.

Payment Due Date

Statement Balance

Minimum Payment

[date]
[$]
[$]

[Warnings, if any]

[Values depending on the currency selected:]
UK: minimum (£17.30), statement balance (£691.82).
US: minimum ($33.89), statement balance ($1,355.67).
[Random assignment to no warnings, minimum payment, statement balance, or both warn-
ings, using:]

Minimum payment warning: ”If you make at least the Minimum Payment ([$]), you will
pay additional interest, but you will avoid late fees.”

Statement balance warning: ”If you pay the Statement Balance [$]), you will not pay
any additional interest or fees.”

• How much will you repay?
◦ Minimum payment
◦ Statement balance
◦ Other amount: [participants could type in the amount]

• Please answer these two questions about the information you just saw [the following

two questions are randomly ordered]

◦ How well do you understand what the minimum payment means? (1=Not at

all/7=Very well)

---

<!-- PAGE 57 -->

14

◦ How well do you understand what the statement balance means?

(1=Not at

all/7=Very well)

• During the last 12 months, please answer to what extent you agree with the following
statements [1 “Strongly disagree”, 2 “Disagree”, 3 “Somewhat disagree”, 4 “Neither dis-
agree nor agree”, 5 “Somewhat agree”, 6 “Agree”, 7 “Strongly agree”]
◦ I always pay my credit card balance oﬀ in full each month
◦ I often make only the minimum payment on my credit card bills

• [Payments with credit card from Salisbury (2014)]

• Considering the last 12 months, please answer which range best reﬂects the amount

you usually repay for your credit card [using UK and US ranges]

• [Financial vulnerability from Salisbury and Zhao (2020)]

• [Financial literacy from Navarro-Martinez et al. (2011)]

• [Cognitive reﬂection test from Frederick (2005)]

• Demographics: age, gender, occupation, annual income [using UK and US ranges], and
educational level. Were the rules about the study clear? Do you have any comments about
the study?

• Open-ended question about any comment about the study.

---

<!-- PAGE 58 -->

15

TABLE A13 - A
WARNINGS EFFECT BASED ON COGNITIVE FACTORS
IN THE ONLINE EXPERIMENT (WITH INTERACTIONS)

Dep. Var.

MinW

SBalW

BothW

X =
X

MinW × X

SBalW × X

BothW × X

R2
N observations

Percentage
of Full
(1)
0.047
(0.065)
0.171***
(0.063)
0.246***
(0.062)

Financial Vulnerability
-0.027
(0.018)
-0.035
(0.027)
-0.025
(0.028)
-0.035
(0.026)
0.115
400

Percent
of Full
(2)
-0.067
(0.125)
0.110
(0.122)
0.209*
(0.125)

Percentage
of Full
(3)
-0.010
(0.100)
0.198*
(0.097)
0.346***
(0.097)

Financial Literacy CRT (Score)

0.097**
(0.039)
0.043
(0.057)
0.027
(0.055)
0.013
(0.057)
0.130
400

0.074**
(0.033)
0.018
(0.048)
-0.019
(0.049)
-0.067
(0.048)
0.085
400

Notes: OLS estimates of Equation 1 plus the main eﬀect of a covariate (X) and
its linear interaction with the warnings conditions. All models using the per-
centage of the statement balance paid (“Percentage of Full”) as the dependent
variable. SEs between parenthesis. MinW is the Minimum warning, SBalW is
the Statement Balance Warning, and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 59 -->

TABLE A13 - B
WARNINGS EFFECT BASED ON COGNITIVE FACTORS IN THE ONLINE EXPERIMENT

16

MinW

Dep. Var.

Subsample

High Financial
Vulnerability
Percentage
of Full
(1)
0.037
(0.067)
0.130**
(0.065)
0.183***
(0.063)
p-values from pairwise comparison

BothW

SBalW

Low Financial
Vulnerability
Percentage
of Full
(2)
0.003
(0.111)
0.207*
(0.117)
0.268**
(0.125)

Low Financial
Literacy
Percentage
of Full
(3)
-0.051
(0.081)
0.139*
(0.082)
0.195**
(0.079)

High Financial
Literacy
Percentage
of Full
(4)
0.134*
(0.075)
0.185**
(0.072)
0.319***
(0.075)

Low CRT
(Score)
Percentage
of Full
(5)
0.030
(0.094)
0.205**
(0.093)
0.331***
(0.090)

High CRT
(Score)
Percentage
of Full
(6)
0.003
(0.076)
0.135*
(0.076)
0.154*
(0.078)

BothW vs MinW
BothW vs SBalW
SBalW vs MinW

R2
N observations

0.027
0.401
0.166
0.036
286

0.030
0.628
0.072
0.068
114

0.002
0.479
0.018
0.051
245

0.021
0.081
0.500
0.110
155

0.001
0.143
0.055
0.094
183

0.064
0.814
0.095
0.030
217

Notes: OLS estimates of Equation 1 using the percentage of the statement balance paid (“Percentage of Full”) as the
dependent variable. Each column is a diﬀerent sub-sample. SEs between parenthesis. MinW is the Minimum warning,
SBalW is the Statement Balance Warning, and BothW is the Both Warnings condition.
* p < 0.10, ** p < 0.05, *** p < 0.01

---

<!-- PAGE 60 -->

Figure A1. Distributions of heterogeneous treatment effects for each warning using the control as

the baseline

17

(a) Full

(b) Less than Min

Notes: Histograms of the causal random forests. Panels (a), (b) and (c) indicate the dependent variable. The
baseline is the control group for all the graphs.

(c) Percent of Full

---

<!-- PAGE 61 -->

Figure A2. Distributions of heterogeneous treatment effects between warning conditions

18

(a) Full

(b) Less than Min

Notes: Histograms of the causal random forests. Panels (a), (b) and (c) indicate the dependent variable. The
baseline is the second group after “vs.” in each graph.

(c) Percent of Full

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

THE RISE OF A NUDGE: FIELD EXPERIMENT AND
MACHINE LEARNING ON MINIMUM AND FULL CREDIT
CARD PAYMENTS
Daniel Schwartz ∗
The minimum payment warning, a notice that informs credit
cardholders of the downside of making the minimum payment, has
been described as a perverse nudge because it negatively affects
those who would pay more than the minimum, presumably due
to the anchoring bias. This issue is tackled in a massive field
experiment by introducing a novel “statement balance warning.”
The experiment used email payment reminders that randomly
added minimum payment or statement balance warnings. Results
indicate that the messages shifted actual payment distribution
depending on the warning and that payments increased when
the statement balance warning was added. The analysis is
combined with causal random forests to examine heterogeneous
treatment effects, underlying mechanisms, and the optimum
policy in different scenarios, and with an online experiment to
further examine conditions in which the warnings affect payment
behavior. The statement balance warning makes debtors give
priority to paying a higher amount, which significantly increases
payments by cardholders who are more likely to make deliberate
decisions every billing cycle and improves the understanding of the
consequences of not paying the statement balance. Furthermore,
the optimal policy to decrease interest charges or debt delinquency
indicates that cardholders should receive a combination of warning
messages depending on their payment history. The results provide
evidence that the statement balance warning offers a new element
for financial market regulation to improve the decision-making of
indebted households.
JEL: C93,D14,D91,G40
Keywords: financial decision-making, debt, anchoring, causal
random forests, nudges.
Version: 28 Jan 2022
PLEASE DO NOT CITE OR CIRCULATE
∗ UniversityofChile,Beauchef851,Santiago,Chile. daschwar@dii.uchile.cl.
Acknowledgements:
1

2
I. INTRODUCTION
Thereare2.8billioncreditcardsinusearoundtheworld(ShiftProcessing,2021). Inthe
UnitedStatesalone,theoutstandingcreditcarddebttotalsUSD$1trillion,andmorethan
40% of that figure is revolving debt – i.e., it accrued interest every month (El Issa, 2019),
and credit card debt keeps growing (Resendiz, 2020). This widespread use of credit cards
that may offer a convenient payment method to households has also brought on financial
distress for those who cannot manage their debt payment, which has been associated with
increased life dissatisfaction and poorer mental health (Norvilitis et al., 2006; Fitch et al.,
2011; Nelson et al., 2008; Hodson et al., 2014).1
Reasons for the increasing credit card indebtedness of households are not just based on
liquidityconstraintsbutalsoonpeopleencounteringmanydifficultiesinunderstandingthe
information related to credit card payment (Soll et al., 2013; Gin´e et al., 2019). Previous
work has shown that consumer characteristics, such as inattention and financial literacy,
beyond local regulation, are key to understanding household financial distress (Keys et al.,
2020). However, many financial literacy interventions have been proven to have no effect
on people’s behavior (Fernandes et al., 2014).
As a partial solution, policy regulations in several countries (e.g., United States, United
Kingdom, Australia, and New Zealand) have included a mandatory minimum payment
warning in credit card statements.2 Even though these regulations aimed to reduce addi-
tional payments based on unpaid amounts, avoid a delinquent state and a vicious cycle of
higherpayments,severalstudieshaveshown,usingadministrativedataorlaboratory-based
experiments, that highlighting the minimum payment may actually cause lower overall and
full balance payments (Hershfield and Roese, 2015; Salisbury, 2014; Stewart, 2009; Wang
and Keys, 2014; Navarro-Martinez et al., 2011; Adams et al., 2018). For this reason, the
minimumpaymentsaliencypolicyhasbeendescribedasaperversenudge(WangandKeys,
2014; The Economist, 2008).
The reduction of payments due to the salience of the minimum payment has been com-
monly explained by the anchoring bias (Tversky and Kahneman, 1974): people’s tendency
to use the minimum amount as an anchor and insufficiently adjust their payment (e.g.,
Thaler and Sunstein, 2008; Stewart, 2009; Navarro-Martinez et al., 2011). Other research
has argued that this effect may be triggered by the minimum payment acting as a target
value (Bartels and Sussman, 2016); people exert effort to get to a specific amount. Re-
gardless of the explanation — anchoring bias or target value — research shows that the
minimum credit card payment drives cardholders’ payment behavior even when account-
ing for liquidity constraints and financial distress (Guttman-Kenney et al., 2018; Keys and
Wang, 2019).
1After conducting a systematic review, Fitch et al. (2011) recognized the challenges in finding a causal path
between debt and mental health. Nonetheless, they conclude that “it would seem implausible that indebtedness
makesnocontributiontowardspoorermentalhealthovertime”(p. 163).
2IntheUnitedKingdom,forexample,“Pleasemakesureyourminimumpaymentiscreditedtoyouraccountby
thepaymentduedatetoavoidincurringalatefee,allowingupto7workingsdaysforpaymenttoclear. Ifyouonly
maketheminimumpaymenteachmonth,itwilltakeyoulongerandcostyoumoretoclearyourbalance.”

3
This paper examines a randomized, massive preregistered field experiment introducing a
novel statement balance warning that indicates to debtors that they will avoid paying more
interestbypayinginfull. Creditcarddebtorsreceivedanemailremindertopaytheircredit
card a few days before it was due. The message randomly varied in 4 groups, a minimum
payment warning, a statement balance warning, both warnings, and no warnings. While
the minimum payment warning may push high-payers (low-payers) to decrease (increase)
the fraction they pay of their credit card bill, based on the previous literature on lab
experiments, a statement balance warning may encourage people who are able to pay more
than the minimum to pay a higher fraction. However, the statement balance warning may
discourage people who could only pay the minimum (or not offer the correct information).
On the other hand, presenting both warning messages on the minimum and the statement
balance may drive low and high payers into a self-selection process to benefit from both
warnings.
The findings indicate that any warning message decreases the likelihood of not paying at
least the minimum compared to a simple payment reminder without any warning, which
reduces credit card delinquency. On average, the warnings decrease the less-than-the-
minimum payments by debtors by 6.9 to 8.8 percent more than debtors who received the
simple payment reminder (an absolute difference of 0.7-0.9 percentage points). However,
to avoid revolving interest accruing because payments are not in full, the experiment’s
results highlight a significant change in payment distribution depending upon the specific
warning message. First, debtors who received the statement balance warning are 1.0 - 1.1
percent more likely to pay in full than debtors who received the simple payment reminder
(a difference of 0.6-0.7 percentage points). Second, despite the large sample size, there is
no sizable change in the likelihood of paying in full for debtors who received the minimum
payment warning, but they increased the likelihood of paying the minimum payment by
6.3 percent compared to the simple reminder (a difference of 0.5 percentage points).
The change in payment distribution has significant consequences on the interest charged
in the following billing cycle, depending on the type of warnings they received. First,
debtors who received a message including both warnings or only the minimum-payment
warning reduced their delinquent interest (i.e., the interest charged for not paying at least
theminimum)by3.8percentandby3.2percentmorethanthosewhoreceivedthemessage
with only the statement balance warning, and by 8.0 and 7.4 percent more, respectively,
than debtors who received the simple reminder. Also, consistent with the changes in pay-
ment distribution, there is a difference in the revolving interest charged (i.e., the interest
charged for paying less than the statement balance). Debtors who received both warn-
ings or only the statement balance warning reduced the revolving interest charges by 6.0
and 3.8 percent more, respectively, than debtors who received only the minimum warning
message, and 9.0 and 6.8 percent more, respectively, than those who received the simple
reminder. Therefore, changes in payment distributions due to specific warning messages
impact people’s additional payments.
In order to explore heterogeneous treatment effects and explain underlying mechanisms,
the field experiment was combined with a recently developed machine-learning technique,

4
causal random forests (Wager and Athey, 2018). This method uses high-dimensional func-
tions to examine heterogeneous treatment effects, an “honesty” approach of resampling
observations, and a bootstrap of covariates to avoid overfitting and thus avoid some of the
shortcomings of reduced-form heterogeneity analysis. There are significant heterogeneous
effects. A large fraction of cardholders increase their payments because of the statement
balance warnings, and a small fraction of debtors might slightly reduce their payments in
full due to the minimum payment warning, although there is no clear significant perverse
effect. Different factors explain a positive and large treatment effect on payments when
messages include the statement balance warning: a considerable variation in how much of
their bill debtors usually pay - indicative of deliberation -, and whether they partially pay
their balance. Also, for the messages with both warnings, debtors increase their payments
when they see a relatively small gap between the minimum and the statement balance
amounts, suggesting that debtors can prioritize one warning depending on which becomes
more relevant and attainable. Finally, the results from the field experiment are replicated
through an online experiment reflecting digital credit card payments that incorporates the
warnings. This online experiment shows that the statement balance warning significantly
increases the likelihood of paying in full, and results do not seem to be explained by finan-
cial skills, financial vulnerability, or people trying to override an otherwise incorrect quick
response. Instead, the warnings follow a cognitive path by helping cardholders improve
their understanding of financial information.
This study makes several contributions. First, it contributes to the literature on min-
imum payment salience and minimum payment warnings in financial decisions using the
first well-powered randomized field experiment. The use of a randomized experiment over-
comes the potential identification problems of secondary-data analysis studies (Besley and
Case, 2000; Heckman et al., 1999; Kahn-Lang and Lang, 2020). In addition, a natural
field experiment is not subject to potential social desirability or Hawthorne effects that
may confound results in lab experiments compared to those conducted in the field (Galizzi
and Navarro-Martinez, 2019; Schwartz et al., 2020, 2021). Furthermore, previous research
has found that the anchoring bias varies from lab experiments to field experiments as lab
experiments magnify the influence of anchoring (Jung et al., 2016). For example, using a
before-after analysis for the US 2009 CARD Act, Agarwal et al. (2015) found no sizable
change in overall payment when examining the same nudge highlighting an amount some-
what higher than the minimum payment examined in previous lab experiments. As an
exemption to the previous lab and observational studies in the minimum payment domain,
Seiraetal.(2017)conductedafieldexperimentinMexicousingmultipletreatments. Oneof
theirtreatmentmessageshighlightedthenumberofmonthsneededforcustomerstopayoff
their debt if only the minimum was paid. They found no significant difference compared to
customers who received no message whatsoever (their control condition), but, as discussed
bytheauthors, itmaybedifficulttofindsizableeffectsgiventhesamplesize(about12,900
in each treatment arm), in addition to the lack of a control condition with no minimum
payment salience. Without such a control condition, it is not possible to tease apart the ef-
fect of a payment reminder (positive, as shown in previous research (Homonoff et al., 2018;

5
Arenas and Schwartz, 2021)) from the effect of the minimum-payment salience/warning
(potentially negative). In contrast, in this paper, the field experiment’s control condi-
tion includes a message with no warnings, and it has a large sample size that increases
the study’s statistical power and helps examine heterogeneous treatment effects useful to
public policy and scientific inquiry.
Second, this research proposes a novel solution to tackle the potentially perverse effect
of minimum-payment salience highlighted in the literature and to help decrease household
debt. Households that pay the minimum end up paying more interest and it is possible
that they may never pay their debt. Several scholars have examined and proposed the
solution of increasing the minimum payment (Jiang and Dunn, 2013; Navarro-Martinez
et al., 2011). However, even with a higher minimum payment, consumers could still be less
likely to pay in full because of the minimum payment’s influence. Moreover, constrained
borrowers who benefit from the minimum payment may end up delinquent, which would
decrease wellbeing. Separate from the credit card statements, Guttman-Kenney et al.
(2018) offer an interesting solution of removing the minimum payment on a Website and
simulating an online payment in which choices are offered (hypothetical decisions). If
a participant wanted to pay less than the minimum, a prompt appeared displaying the
minimumpayment. However, financialinstitutionsmaybediscouragedfromimplementing
this information flow, and in many countries, there is still a relevant percentage of people
who do not pay online. The authors note that the UK’s Financial Conduct Authority tried
to run this study with lenders, but no one wanted to do it. The statement balance warning
approach is a palatable solution because lenders acknowledge that consumers deserve to
know the consequences of their actions. Moreover, the field experiment for this paper was
implemented by a private financial institution, and served as the basis for a regulation
proposal for all statement balances in a country with high credit card market penetration,
which is discussed in Section VII.
Third,theexperimentalsettingcontributestotheliteratureexamininggoalsandtargets.
Researchhasshownhowthedifferenttenetsofprospecttheory’svaluefunction(Kahneman
and Tversky, 1979) can affect people’s motivation and effort when one target is set (Heath
etal.,1999). Forexample,peopleshouldexertgreatereffortfortargetsthatareperceivedas
attainableandlittleeffortforharderones. Inaddition, psychologyresearchpostulatesthat
whenthereisahierarchyofgoalsortargets,onegoalisprioritizedandnon-prioritizedgoals
are ignored (Unsworth et al., 2014). Both sets of research predict that credit card payment
may depend on which target values are prioritized: if cardholders care about paying the
statement balance to avoid revolving interest, they will pay attention to the statement
balance warning and ignore the minimum payment warning. This paper’s findings suggest
that cardholderswho have usually paid more than theminimumare more likely to increase
their payment under the statement balance warning, and those who have usually failed to
pay at least the minimum are more likely to increase their payment when receiving the
minimum-paymentwarningmessage. Becausethereisnoempiricalresearchexaminingthis
type of dual or multi-level targets in real-world behavior, this paper will be the first one to
studyhowpeopleprioritizetwo-leveltargetsusingabehavioralresponsethatmaybeuseful

6
to financial decisions and other domains. For example, field research offers one interesting,
popularized case using social norms in energy consumption with dual-target information
(e.g., Allcott and Rogers, 2014). Utility companies inform two amounts to customers:
one indicates the neighbors’ average energy consumption and the other the usage of the
most energy-efficient households, so they do not demotivate those consuming less than the
average household (Schultz et al., 2007). However, there is no current examination of how
household responses may prioritize these two targets.
Fourth, this paper contributes to the literature using causal machine learning in eco-
nomics (Athey and Imbens, 2019). One crucial difference to most previous studies using
causalrandomforestsisthattheyuseexistingrandomizedcontroltrialstofindnewhetero-
geneous effects (e.g., Davis and Heller, 2017). However, almost all behavioral interventions
are designed to positively affect the average person.3 In contrast, based on the perverse
nudge effect of the minimum salience payment found in previous research, the field exper-
iment in this research was designed to examine heterogeneous effects.
Finally, this paper contributes to the research on consumer financial markets, their reg-
ulation, and the role of behavioral biases (Agarwal et al., 2017; Campbell, 2016; Bhamra
and Uppal, 2019). In particular, this research contributes to credit card disclosure reg-
ulation, as promoted in several countries (the Credit Card Accountability Responsibility
and Disclosure Act in the U.S., Truth-in-Lending-Act in Mexico, Credit Contracts and
Consumer Finance Act in New Zealand, and the United Kingdom Lending Code, among
others). Campbell 2016’s Richard Ely Lecture emphasizes the consequences on welfare
and the economy with the rise of complicated financial information: consumers fail to per-
ceive the consequence of their financial decisions, either because of complex information,
lackofattention, hyperbolictemporaldecisions, heterogeneouscapabilitiesorhiddencosts.
Credit card issuers targeting less-educated consumers also present a systematic challenge
to financial markets and regulation (Ru and Schoar, 2016). This paper’s findings indi-
cate that income and share of debt with other lenders are not the main drivers behind
an increase in payments when cardholders receive the statement balance warning, which
provides a palatable regulation for a broad base of consumers. Additionally, regulating
the information communicated in the credit card billing process can produce substantial
benefits without forbidding people’s indebtedness or increasing costs. The statement bal-
ance and minimum payment warnings transparently explain the consequences of paying
less than a certain amount, which should alleviate concerns about their implementation.
This is aligned with policymakers’ role of encouraging lenders to disclose borrowing costs
so that consumers make more informed debt repayment decisions.
Therestofthepaperproceedsasfollows. SectionIIdescribesthebackgroundinformation
on credit card debt, minimum payment, and payment information. Section III explains the
methods, including the data and the experimental design. Section IV presents the results
usingaparametricanalysis,andSectionVfocusesonheterogeneoustreatmenteffectsusing
causal random forests. Section VI examines different underlying mechanisms and presents
3ThispointhasbeenraisedbySusanAtheyonseveraloccasions(e.g.,talkgivenintheAI&BigDatainFinance
ResearchForumonAugust25,2021).

7
additional analyses and experiments. Finally, Section VII concludes.
II. BACKGROUND INFORMATION
Creditcardsareubiquitous–nearly3billionaroundtheworld. Globalstatisticsindicate
that Canada is the country with the largest share of the population owning a credit card
(83%), while the US (66%) and the UK (65%) are within the top 10 (Statista, 2017). In
Latin America, Chile is one of the leading countries in credit card usage, with 20.1 million
credit cards in a population of nearly 19 million people (Retail Financiero, 2019).
One of the most important measures related to credit card debt is the credit card delin-
quency rate. Delinquency is caused by missing one or more minimum payments, and it has
consequences on individuals’ credit scores and rampant debt. In the US alone, the 30-day
delinquency has varied from 6.8% in 2009 to 1.8% at the beginning of 2021, probably due
to the government financial aid in the midst of the Covid-19 Pandemic, and the 90-day
delinquency rate continued increasing to 10% in 2021 (Board of Governors of the Federal
Reserve System, 2021). In Chile, where this paper’s main study takes place, two-thirds of
the credit cards are managed by retail credit card issuers. The delinquency rate for retail
credit cardholders was 8.4% in 2018, rising to 9.1% during mass protests in the last quarter
of 2019. It varied from 7.9% to 12.1% during the Covid-19 pandemic, also influenced by
the financial aid to Chilean families (Retail Financiero, 2021).4
Financial regulations in many countries have established payment information that must
be presented by the credit card issuer. One key piece is the required minimum payment,
which is generally an amount equal to at least the sum of interest and fees accrued at the
moment of billing. However, credit card issuers have flexibility in calculating the minimum
paymentwhenitisgreaterthanarequiredthreshold. Forexample,somecreditcardissuers
useapercentageofthestatementbalance(e.g.,between1%and3%)oraminimumamount
(e.g., $25) if the statement balance is less than the amount corresponding to the sum of
1% of the statement balance, interest and fees.5 Like in many countries, in Chile, credit
card issuers must have a minimum payment of at least the sum of credit card interest,
except “when the [required minimum] is waived for a specified period under a promotion
or offer” (MinEcon, 2012). Compared to the US and the UK, whose minimum payment
ranges from 1% to 3%, credit card issuers vary their minimum payment by much more in
Chile (between billing cycles and among consumers). The credit card issuer involved in the
study, oneoftheleadersinLatinAmerica, hasanaverageminimumpaymentof29%ofthe
statement balance (SD = 20%; Median = 24%; Mean SD = 13%). This variation
within
depends on consumers’ purchases (e.g., if the purchase was made using the credit card in
retail stores), making the minimum vary from $0 to the statement balance, although this
is unknown to the consumer.
4Forthisreference,thedelinquencyrateiscalculatedusingloansforwhichpaymentis30daysormorepastdue,
divided by total loans (the numbers are very similar to the delinquency rate using the customer base of the retail
credit card issuer in the field experiment of this paper, which is one of the major players in the country). Bank
issuershavehistoricallylowerlevelsofdelinquencyrates.
5ForexamplesofseveralcreditcardissuersintheU.S,see: https://creditcards.usnews.com/articles/how-credit-
card-issuers-calculate-your-minimum-payment.

8
As introduced in the previous section, several countries have required credit card issuers
to include a minimum payment warning. However, in the case of Chile, the current regu-
lation does not require any warning of that sort, and there is no evidence that any credit
card issuer is using one. On the other hand, on their websites, the Consumer Protection
Bureau and the Financial Market Commission attempt to alert people that paying less or
only the minimum may keep families in debt for a long time or from even paying their
debt, even if they stop using their credit cards, although it would be venturesome to say
that consumers are paying attention to this information.6
III. DATA AND EXPERIMENTAL DESIGN
III.A. Data and Sample Selection
IncollaborationwithamajorLatinAmericanretailcreditcardissuer,customerselection
was based on operational requirements and on increasing statistical power.7 The sample
inclusion criteria considered customers who had no automatic payment at the time of the
study, those who paid less than the statement balance at least twice in the previous 12
months, and those who were sent at least six emails by the retailer with an email opening
rate of at least 20% in the previous six months.8 The retailer requested the exclusion
of a very small percentage of long-term delinquent accounts treated by other programs.
Other sample selection criteria were merely operational: the email was uniquely assigned
to one customer, and customers had to have a minimum payment of at least $2.40 and a
statement balance greater than or equal to $12.0, so customers would have something to
pay and could distinguish between the minimum payment and the statement balance.9
The company provided anonymized customer information using the above criteria to
conduct a block randomization procedure using the minimum payment and statement bal-
ance, the percentage paid of the previous bill, and the number of times the customer paid
less than the statement balance in the previous twelve months. Then for each block, in-
dividuals were randomly assigned to four experimental conditions. The sample consisted
of 179,706 debtors with a total of 2,853,939 observations.10 There are almost two years of
data on most customers, from March 2018 to November 2019.11
6E.g., ”The minimum payment can be a lifetime debt” from https://www.sernac.cl/portal/604/w3-article-
1094.html,andhttps://www.cmfchile.cl/mascerca/601/w3-article-27871.html.
7Companies’ concern about consumers’ indebtedness is not uncommon. Some banks and credit card issuers
provide tools to their customers (e.g., “inControl”) so that they can limit their expenditures and control their
shoppingbehavior(Lieber,2010).
8Athird-partyfirmmeasuresemailopeningrates,mainlyretailoffersandpromotions. Eventhoughthismeasure
is not exact because it depends on particular email providers and email settings, it may be used as a proxy for
consumersopeningtheemailssentbythecompany.
9InAmericandollarsadjustedbythePowerPurchaseParity(PPP),usingtheexchangerateatthetimeofthe
experiment.
10Forty-sevenpeoplewereexcluded. Ofthose,44hadacreditlineexceeding$48,114(99.98thpercentile),which
mayrepresentabusinesscreditline,and3hadanegativepaymentamount(theymayhavehadsomesortofcredit).
TheOnlineAppendixshowsthemainresultsincludingtheseaccounts.
11ThecompanyprovideddataforJanuary-February2018,butthereweresubstantialmissingvaluesatthebegin-
ningoftheyear.

9
III.B. Procedure
Customers received two email payment reminders five and two days before their credit
cardpaymentwasdue. EmailsweresentforonebillingcycleduringAugustandSeptember
2019. All email subjects indicated the name of the customer: “[Name], [Credit card name]
has important information for you.” Previous research has shown that email opening rates
improve when including people’s names in the subject (Sahni et al., 2018). Also, all email
bodies included a reminder sentence, “We remind you that your [card name] is due on
[date].” Individuals were randomly assigned to four experimental conditions through the
blockrandomizationprocedureexplainedabove(25%toeachexperimentalcondition). The
firstexperimentalcondition(the“MinimumPaymentWarning”condition, or“MinW”)in-
cluded a sentence about the minimum payment: “If you at least pay the minimum
([$]) before the due date, you will pay additional interest charges but avoid late
fees.”, similar to the minimum payment warning sentence used in several countries. The
second experimental condition (the “Statement Balance Warning” condition, or “SBalW”)
included a sentence about the statement balance: “If you pay the statement balance
([$]) before the due date, you will avoid additional interest charges.” The third
experimental condition (“Both Warnings” condition, or “BothW”) combined the previ-
ous two experimental conditions, including the statement balance and minimum payment
warnings.12 Finally, the fourth experimental condition (“Control”) was a pure reminder
with no statement balance or minimum payment warnings.13 All customers received their
credit card statements in a separate communication that included the statement balance
and minimum payment amounts. Statistical power calculation and the sentences were first
tested in a pilot study with multiple treatments that showed that people reacted to the
warnings rather than to the specific amounts (see the Pilot Study and Table A1 in the
Online Appendix).14 The experiment was preregistered at the Wharton Credibility Lab at
the University of Pennsylvania (https://aspredicted.org/blind.php?x=gz9gw3).
III.C. Sample Characteristics and Balance Checks
TableIshowsdescriptivestatisticsandchecksthebalanceacrossexperimentalconditions.
All conditions present very similar values for pretreatment variables, with no sizable statis-
tical differences. Debtors (female: 51.6%, 44.4 years old) received a credit card statement
in the treatment period with a statement balance and a minimum payment of $1,949 (SD
12OriginalsentencesinSpanish: “Terecordamosqueelpagodetu[cardname]venceel[date].”Minimumwarning:
“SipagasalmenoselMontoM´ınimo[$]antesdelafechadevencimiento,pagar´asinteresesperoevitara´spagargastos
decobranza.”Statementbalancewarning: “SipagaselMontoTotalFacturado[$]antesdelafechadevencimiento,
evitar´aspagarinteresesadicionales.”
13Thecompanyreviewedthemessagesbeforetheywerelaunchedtoensurethattheywereunderstandable. Italso
asked that the statement balance amount be included if the minimum payment was included, even if it was at the
endoftheemail(so,theminimumpaymentwasalsoincludedwhenaddingthestatementbalanceattheendofthe
email). Customersreceivedbothamountsintheirmonthlystatements.
14TheonlineexperimentinSectionVIalsoprovidesevidencethatpeoplereacttothewarningsentencesandnot
totheamounts.

10
= 3,050) and $416 (SD = 529), respectively.15 Before the experiment, using all 2019 billing
cycles before the treatment period, debtors paid an average of 75.8% of their statement
balance. In addition, on average, 63.7% paid in full, 7.9% paid the minimum payment,16
and 8.2% did not pay or paid less than the minimum payment, leading to credit card delin-
quency, additional interest, and late fees. This percentage is also similar to the average
national delinquency rate for credit cards issued by retailers at the time of the study, as
described in Section II.
IV. CHANGES IN PAYMENT BEHAVIOR
This section examines the effect of the warning messages on payment behavior, including
how shifts in payment distribution affected interest payments. Equation 1 estimates the
effectofthewarningmessagesusinganordinaryleastsquareanalysiswithrobuststandard
errors clustered by individual (Bertrand et al., 2004).
(cid:88)
(1) y = α+ β D ×P +δP +X +µ +µ +a +ε
it j ij t t it m y i it
j
where D is a dummy indicator for each warning message assigned to individual i com-
ij
pared to the control (treatment warnings j = {Minimum, Statement Balance, Both}). P
t
isadummyvariableforbeforeandafterthetreatmentperiodforbillingcyclet. Thespeci-
fication includes controls for changes in customers’ characteristics over time and before the
treatment (X : company’s internal credit score, income, purchases, statement balance and
it
the ratio between the minimum payment and statement balance of individual i in billing
cycle t), monthly and yearly fixed effect (µ and µ ), and individual fixed effects (a ). The
m y i
error term is ε . β indicates the average intention-to-treatment effect of each warning
it j
message as compared to the control condition. Because of randomized assignment, these
difference-in-difference estimators are unbiased (Rubin, 1974). The outcome variable (y )
it
changes for each analysis; for payment variation, the specification uses the logarithmic
transformation of payments of individual i in billing cycle t.17 For the probability of not
paying at least the minimum, which drives credit card delinquency, the outcome variable
is a dummy indicator equal to 1 if individual i in billing cycle t does not pay or pays less
than the minimum (0, if not). Similarly, for the probability of paying in full, the outcome
is a dummy variable that indicates whether the cardholder i pays in full in billing cycle
t. In these latter two cases, changes in probability are examined using a linear probability
model. Another measure of interest is the percentage paid, which is the proportion of the
15Becauseofconfidentiality,thepaymentinformationwasre-scaledusingatypicalstatementbalanceof$1,949.28
in the United States (Salisbury and Zhao, 2020). Therefore, the statement balance and minimum payment were
re-scaledbythisvalueusingdebtors’actualstatementbalancesmultipliedbyF,whereF= ( (cid:80)(state 1 m ,9 e 4 n 9 t . b 2 a 8 lancei)) .
16Thesedebtorspaidexactlytheminimumamountoruptothenextnearest10,000Chileanpesos( N approx. $24
adjustedbyPPP).Ifthisvariableconsidersthenextnearest100,000Chileanpesos,thepercentageofdebtorspaying
theminimumwouldbe15.8%.
17Fortheamounts,ln(X+1).

11
statement balance paid by individual i in billing cycle t (y ∈ [0,1]). Finally, using the
it
next couple of billing cycles after the treated billing cycle, two types of interest charged are
also used as outcome variables; revolving interest, which accrues when debtors pay at least
the minimum but less than the statement balance, and delinquent interest, which accrues
when debtors do not pay or pay less than the minimum.
IV.A. Main payment variation and its consequences
Table II shows the average treatment effects of each condition using the control as the
baseline. Thefirstcolumnshowsthatallwarningmessagesincreasepaymentamountsfrom
6.2%to7.8%comparedtothecontrolcondition,withnosizablestatisticaldifferencesacross
warnings. The second column indicates that the warnings reduce the probability of not
paying at least the minimum by 6.9% - 8.8% from a baseline of 9.7% (0.7-0.9 percentage
points), with the statement balance warning only condition offering the smallest reduction,
but with no sizable statistical difference from the other warnings. This result translates
into a lower credit card delinquency rate because of the warnings. As a reference for these
magnitudes, the delinquency rate in Chile at the time of the experiment was 8.4% for
retail credit cards (Retail Financiero, 2019) and increased 3.7 percentage points in the
worst moment of the COVID-19 pandemic, which was an extreme situation.
For the probability of paying in full (third column), debtors who received a message
with the statement balance warning increased the likelihood of paying in full by 0.6-0.7
percentage points, which is an increase of 0.9% to 1.1% from a baseline of 62.5% (i.e., most
people paid in full under the control condition), which decreased the revolving interest
accrued by paying less than the statement balance. In contrast, there was no statistically
significant change in the likelihood of debtors who received the minimum payment warning
paying in full as compared to the simple reminder (CI95% [-0.3 pp., 0.7 pp.]), i.e., not
clearly supporting previous lab evidence, although this result masks some heterogeneity
that will be examined in the next section. Moreover, debtors who received the minimum
payment warning only were 0.4 percentage points less likely to pay in full than those who
received the statement balance warning or both warnings.
The previous results have several consequences. First, the proportion paid of bills in
conditions that included the statement balance warning increased by 0.7 percentage points
compared to the plain remainder and by 0.4 percentage points compared to the minimum
payment warning condition (fourth column). Debtors who received the only minimum
payment warning did not pay a statistically sizable different proportion of their bill com-
pared to the control condition. A more important consequence for household finance is the
interest that households ended up accruing in the billing cycle following the intervention,
depending on their payment behavior because of the warnings. Table II (fifth column)
shows that debtors who received a message with the statement balance warning reduced
their revolving interest, which accrues on unpaid amounts above the minimum, by 6.8%
and 9.0% for the statement balance and both warnings conditions, respectively, compared
to debtors who received the simple reminder. Moreover, receiving the statement balance

12
warnings reduced the revolving interest more than for debtors who received the minimum
payment warnings only, by 3.8% and 6.0% for the statement balance and both warnings
conditions, respectively. Furthermore, consistent with column 3 of Table II, there is no
statistically significant difference between debtors who received the minimum payment
warning and those who received the simple reminder on revolving interest.
Finally, Table II (last column) shows that all warning messages decreased delinquent
interest, i.e., interest accruing because of non-payment or payments below the minimum
in the billing cycle after the intervention. Specifically, debtors who received a message
including the minimum payment warning decreased revolving interest by 7.4% for the
minimum payment warning only condition and 8.0% for the both warnings condition,
compared to the control condition. Under these two conditions, debtors also paid less
revolving interest than debtors who received the statement balance warning only, by 3.2%
and 3.8%, respectively. These results indicate that the different warnings affect payment
distribution, with significant consequences on how much and what type of interest debtors
end up accruing. Using both warnings simultaneously decreased the interest of people who
would not have paid at least the minimum and those who do not pay in full. Using one of
the warnings greatly affected the specific interest charged, depending on the focus of the
warning.
IV.B. Payment distribution
To examine whether the previous result was in response to changes in payment distribu-
tion, Table III shows analyses using Equation 1, with different payment values or ranges as
outcomevariables. Thefirstcolumnshowsthatallwarningmessagesreducedtheprobabil-
ityofnotpayingatallcomparedtothecontrolcondition. Furthermore, itcanbeseenthat
changes in payment distributions as a result of the warning messages came mainly from
a reduction in debtors who did not pay or who did pay but paid less than the minimum
(first two columns). The question is where this reduction went and whether it depends on
the specific warning message.
For debtors who received the minimum payment warning only, Table III indicates that
theyshiftedtheirpaymentmostlytowardtheminimumamount(eachrowhastoaddupto
0). In particular, the third column shows that debtors who received this warning increased
the likelihood of paying the minimum by 6.3% compared to the control (or 0.5 percentage
points, with a baseline of 7.3%), i.e., 65.8% of the overall reduction in non-payment or in
paying less than the minimum went toward paying the minimum for debtors who received
the minimum warning only (0.52 pp. out of 0.79 pp.). In addition, Table III shows no
significant changes in payments above the minimum for this group. This shift in payment
change due to the minimum warning can also be appreciated in Panel A of Figure 1 that
shows the average treatment effects of Table III.
While payment changes shifted toward the minimum for the minimum payment warning
condition, payment changes in the conditions that included the statement balance warn-
ings shifted almost entirely toward full payment. For example, for the statement balance
warning condition, if the reduction in the likelihood of not paying at least the minimum is

13
aggregated with the change in the likelihood of not paying the minimum, the reduction is
0.79 percentage points. Eighty-one percent of that reduction went toward payment in full
(i.e., 0.64 pp. out of the 0.79 pp.), and the rest toward a revolving amount between the
minimum payment and the statement balance (Panel B in Figure 1).
Table III and Figure 1 (Panel C) show that debtors who received both warnings behave
very similarly to those in the statement balance warning condition, shifting 80% of the
reduction of not paying even the minimum or paying a revolving amount towards paying in
full. However,theremaining20%wenttowardtheminimumamount. Inthebothwarnings
condition, debtors consistently increased their likelihood of paying the minimum compared
to debtors who received only the statement balance warning (statistical significance at the
10% level in this case for the linear model and at 5% for the logit model in the Online
Appendix Table A2). Overall, these results show that the warning messages increased
payments by shifting their distribution consistent with the specific warning content.
The last two columns in Table III show whether cardholders paid the statement bal-
ance (rounded up to the nearest CLP 10,000) or paid more than that, even though there
is no economic benefit of paying more than the statement balance (in the baseline, 6.8%
of debtors paid more than the statement balance).18 There is no statistically significant
difference in the likelihood of paying more than the statement balance, although, direc-
tionally, there is a small reduction for debtors who received the statement balance warning
only compared to the control condition. Finally, Table A2, Table A3 and Table A4 in
the Online Appendix show that the main results are robust using a logit model, different
specifications, or including accounts with large credit lines.
V. CAUSAL FORESTS AND HETEROGENEOUS TREATMENT EFFECTS
Machine learning methods have recently focused on causal inference, which offers an op-
portunityformanyeconomicproblems(AtheyandImbens,2017,2019). Thecausalforests
method in particular is a machine-learning technique recently developed to examine het-
erogeneous causal effects with high-dimensional functions of covariates, which allows be-
havioral mechanisms and optimal policies to be analyzed for multi-treatment cases (Athey
and Wager, 2021). This section shows the heterogeneous treatment effect for each warning
message, which is especially relevant considering previous evidence on the perverse effect
of the minimum payment salience. Then it characterizes the sub-samples with the largest
treatmenteffectsforeachwarningmessageand,finally,presentsanoptimalpolicyanalysis.
V.A. Heterogeneous effect
This part presents the heterogeneous effect analysis using causal random forest models,
based on the Generalized Random Forests algorithm (Athey et al., 2019) to estimate the
conditionalaveragetreatmenteffect(CATE).Inregressionorclassificationtrees,covariates
areusedtosplitobservationsintobranchestofindleavesthatcanpredicttreatmenteffects
(Breiman and Stone, 1984), random forests solve individual tree inaccuracy and overfitting
18Thisbehaviormaybeduetotheconvenienceofpayingsubsequentinstallmentsinadvance.

14
by first aggregating trees using a bootstrap procedure with a sub-sample m of covariates
for each tree.19 Second, the algorithm selects a random subset of the sample for training
to determine the model parameters and another for testing to make the estimation (Athey
etal.,2019;AtheyandWager,2019). Finally,individualtreetreatmenteffectsareweighted
| across | the forest. |     |     |     |     |
| ------ | ----------- | --- | --- | --- | --- |
TheCATE,τD(x),conditionalondebtors’characteristics(x),isdefinedforeachwarning
| message, | D = {Minimum, | Statement | Balance, | Both}, | as: |
| -------- | ------------- | --------- | -------- | ------ | --- |
τD(x)
| (2) |     |     | = E[Y i (1)−Y | i (0)|X | i = x] |
| --- | --- | --- | ------------- | ------- | ------ |
where Y (1) is the potential outcome if debtor i would have been assigned to the warning
i
message D, and Y (0) is the potential outcome if debtor i would have been assigned to the
i
control group. The causal forest algorithm averages individual predictions of each tree b
to produce out-of-bag CATE estimates (see details in Athey et al. (2019)).20 Wager and
Athey (2019) show that these CATE estimates are consistent and asymptotically normally
distributed. Forfurtherexamination,observationscanberankedbytheirout-of-bagCATE
and grouped in subgroups (e.g., quintiles) to obtain valid confidence intervals (Athey and
Imbens, 2016). The conditional average treatment effect estimates within each subgroup
| can then | be obtained | using Equation | 3 for each | warning  | condition: |
| -------- | ----------- | -------------- | ---------- | -------- | ---------- |
|          |             |                | (cid:88)   | (cid:88) |            |
| (3)      |             | y = α+         | τ w        | ×n +     | ϑ n +u     |
|          |             | i              | kD Di      | ki       | k ki i     |
|          |             |                | k=1        | k=1      |            |
where y is the outcome variable, w is 1 if cardholder i was in the warning condition D
|     | i   |     | Di  |     |     |
| --- | --- | --- | --- | --- | --- |
and 0 if i was in the control group. n is a dummy variable equal to 1 if cardholder i
ki
belongs to subgroup k (0 if not). τ is the estimated conditional average treatment effect
kD
(CATE) for the kth subgroup in warning condition D compared to the control condition.
This process is repeated for each warning message and for each outcome variable. This
approach to characterize heterogeneous effects has been used in other domains, such as the
evaluation of educational, parenting, and employment programs (Athey and Imbens, 2019;
| Davis and | Heller, 2017; | Sylvia | et al., 2021). |     |     |
| --------- | ------------- | ------ | -------------- | --- | --- |
Table IV shows the results for the causal random forests sorted by the estimated CATE
using Equation 3 with different dependent variables: whether cardholders paid in full
(“full payment”), whether they did not pay at least the minimum (“payment less than
the minimum”), and their payment as a percentage of the statement balance (“percentage
of full”), for each warning compared to the control condition. In most cases, all warning
treatments show significant heterogeneity. For example, for cardholders who were in the
statement balance warning only condition, the top quintile indicates a conditional average
treatment effect of 2.4 percentage points compared to the control group, i.e., one-fifth of
√
19Bydefault,intheCausalForestalgorithm,m= p+20,wherepisthenumberofcovariates.
20Foreachrandomforest,thealgormithmuses30,000treeswith10minimumobservationspernode,honestywith
0.5splittingswiththeGRF2.0.2packageinR.

15
the sample who received this warning increased their likelihood of paying in full by 2.4
percentage points more than debtors who received a reminder with no warning message (in
relative terms, this is an increase of 4.0% in the likelihood of paying in full, as indicated
in Table A5). This is almost four times the average treatment effect found in the previous
section. For clarity of what follows, Table IV is discussed for each dependent variable. For
additional results, Figure A1 in the Online Appendix shows the complete distribution of
estimated CATE for each causal random forest, and Table A6 and Figure A2 show the
results for the causal random forests using combinations of warning message conditions.
Payment in full. Table IV shows that for the conditions that included the statement
balance warning, at least the top two quintiles significantly increased their likelihood of
paying in full (the CATE coefficients are at least more than 1.64 times their standard er-
rors). On the other hand, there is an enormous heterogeneity for cardholders who received
the minimum payment warning only; while only the top quintile increased the likelihood of
paying in full, most of the quintiles show conditional average treatment effects not sizably
differentfromthecontrolgroup, andthefirstquintileshowsareductioninthelikelihoodof
paying in full (a reduction of 0.8 percentage points, or 1.1%), although this is not statisti-
cally significant even at the 10% significance level. Its magnitude is similar to the findings
by Wang and Keys (2014), and it may suggest a small perverse effect of the minimum
warning.21 Table IV also includes the estimates of the best linear predictors of the CATE
(Chernozhukov et al. 2018a, Chernozhukov et al. 2018b) using the out-of-bag predictions
for each causal random forest. The β coefficient corresponds to the conditional average
1
treatment effect. It also indicates how well the model is calibrated (a coefficient equal to
1 represents a correct causal random forest prediction). β works as an omnibus test for
2
treatment effect heterogeneity (the null hypothesis, β = 0, fails to find underlying hetero-
2
geneity). The results of this analysis reaffirm that average treatment effect predictions are
well-calibrated and heterogeneity is present for the warnings that include only one mes-
sage, in particular, for the minimum warning condition. The heterogeneity is weaker for
the both warnings condition, given the positive result for most quintiles.22
Payment less than the minimum. Table IV shows that for the likelihood of not paying
at least the minimum, which is associated with delinquency, the top quintiles for each
warning message indicate a reduction of 1.2 to 1.5 percentage points compared to the
control condition (a relative reduction of 5.8% to 15.5%). The warnings that include the
minimum payment warning message significantly reduce the likelihood of not paying or
of paying less than the minimum for the top three quintiles. In contrast, the statement
balancewarningdoesnotshowasizabledifferenceforthethirdquintile,andthereforefewer
debtors may have reduced their delinquent interest in the next bill. Importantly, results
suggest no indication that a relevant portion of cardholders would fail to pay at least the
21WangandKeys(2014)alsoexamineddifferenttypesofdisclosuresavailableforsomeUScardholders,including
theminimumpaymentwarningandthepaymentcalculationrequiredtorepayanydebtin3years. Theyalsofound
thattheminimumpaymentwarningdecreaseddelinquencyandincreasedthelikelihoodofpayingtheminimum.
β2D 22 i T (cid:0) h τˆ e −i b ( e X st i) l − ine τ¯ a (cid:1) r + pr ε e i d , i w ct h o e r re of D th is e t C he AT w E arn u i s n e g s t t r h e e at o m u e t n -o t f- ( b v a s g . c p o r n e t d r i o c l t ) io a n n s d , τ τ ˆ ¯ − is i( t X h i e ), sa t m o p e l s e ti a m v a er t a e g Y e i of = ou β t 1 - D of i - τ¯ ba + g
estimates.

16
minimum when receiving the statement balance warning – there are not even negative
magnitudes in the CATE coefficients. Finally, the best linear projection analysis shows a
statistically significant heterogeneity only for the minimum payment warning condition. In
the Online Appendix, Table A6, which shows the causal random forests between warning
conditions,thequintilewiththelargesttreatmenteffectshowsthatsomepeoplewouldhave
significantlyreducedtheirlikelihoodofnotpayingatleasttheminimumiftheyreceivedthe
minimum payment warning only instead of a message with the statement balance warning.
Percentage of full. On average, cardholders in the top quintile who received the message
with the statement balance warning increased the fraction paid by 1.9 to 2.2 percentage
points (a relative increase between 2.9% and 3.2%). Comparing all quintiles, the average
magnitudes of the CATEs for cardholders who received the minimum payment warning
message are smaller than the other warning messages. All warning treatment effects show
heterogeneity based on the best linear projection analysis.
V.B. Policy optimization
Thepreviousanalysisshowedthatthewarningsdidnotaffectallcardholdersinthesame
way. One interesting feature of the causal random forest method is that individuals can
be classified based on their characteristics to predict an optimal policy (Athey and Wager,
2021). In this case, using the results from the causal random forests for each outcome
variable, the maximum out-of-bag predictions are calculated to classify cardholder i for
one message (M ). A random forest (Breiman, 2001) is then computed as a classifier using
i
a training subset and then to predict on a test subset which predicted message (Mˆ ) card-
i
holderiwouldreceivebasedontheircharacteristics. Thisresultyieldsthe“best”predicted
message each cardholder should receive for each outcome variable. However, because card-
holders actually belong to a randomized experimental condition, it is possible to calculate
the optimum CATE as if cardholders were assigned to message Mˆ .23 For example, using
i
a target policy to decrease any interest charges by increasing the fraction paid, the policy
optimization analysis indicates that most cardholders should receive a message with the
statement balance warning: 45.3% with the statement-balance warning and 44.7% with
both warnings. A small percentage (6.9%) of people should receive the minimum warning
only, and the rest is predicted by the model to receive only the reminder with no warnings.
Analogously, let us suppose that the optimal policy aims to reduce delinquent interest (i.e.,
cardholders paying at least the minimum). In this case, the analysis shows that almost
every cardholder should receive a message with the minimum payment warning (42.5%
the minimum payment warning and 36.4% both warnings), which is consistent with the
previous heterogeneous analysis. Then, 21.0% of debtors would receive a message with the
statement balance warning and 0.1% with the reminder with no warnings.
As an exercise to comprehend the role of each warning, a perverse policy that optimizes
cardholders paying less than the statement balance and, therefore, accruing more interest,
23Across models, accuracy is over 70% on the test subset. For each condition, the accuracy of classification was
over68%,exceptforthecontrolgroup,inwhichtheaccuracywas55%foroneofthemodels.

17
would not include any warning in the message to most of the people (54.1%), and would,
interestingly, use the minimum payment warning in 32.7% of messages.24 Finally, this
policy would put the statement balance warning only in 10.6% of the messages while 2.6%
would receive both warnings. This latter result indicates that some cardholders would
decrease their payments if they received one warning message instead of a reminder with
no warnings.
VI. UNDERLYING MECHANISMS AND ADDITIONAL RESULTS
This section examines several explanations to disentangle why the warnings affect pay-
ment behavior. In particular, the following analyses use the reduced-form analysis from
Section IV, the causal random forest results from the previous section, and a new random-
ized online experiment.
VI.A. Advance payments
One concern about the results is that debtors may have increased their payments during
the experiment by reducing their ability to pay in the following billing cycles, i.e., they
advanced their payments. The firm shared data on the two billing cycles after the field ex-
periment, and Table V shows the results for these periods using Equation 1, the dependent
variables being the likelihood of paying at least the minimum, of paying in full, and the
amount paid. The first post-treatment period shows that cardholders who received a mes-
sage including the minimum payment warning increased their likelihood of at least paying
the minimum compared to the control group that received a simple remainder; those in
the minimum-payment warning condition reduced their chance of not paying or of paying
less than the minimum by 2.8% (-0.4 percentage points), and those in the both warnings
condition by 3.6% (-0.5 percentage points). There was no sizable change in the statement
balance warning only in the post-treatment period, even at the 10% significance level, and
the magnitude of its estimate is tiny (0.4%, 0.1 percentage point). In contrast, the likeli-
hood of paying in full one billing cycle after the treatment was not sizably different from
zero for any warning. Consistent with the increase in the likelihood of at least paying the
minimum, the amount paid increased by 5.2% and 5.6% only for the minimum payment
warning and both warnings conditions, respectively (0.1%, and not sizably different from
zeroforthestatementbalancewarningcondition). Twobillingcyclesaftertheexperiment,
there were no sizable differences for any warning in any of the outcome variables.
In summary, there are no signs that cardholders paid in advance (all the estimates
either indicate a positive payment or are very close to zero). On the other hand, this
evidence indicates that the effect of the warnings lasted for one period in the absence
of the intervention, at least when it included the minimum payment warning message,
and then it dissipated, similar to other short-lived behavioral effects (e.g., Schwartz et al.
(2013)). This attenuated effect may also be due to the fact that in October 2019, Chile
24Anorganizationadoptingsuchapolicywouldprobablynotsendanypaymentreminder.

18
experienced nationwide protests that may have somehow disrupted any purchase pattern
as several retailers closed or changed hours of operation.25
VI.B. Anchoring and targets
The minimum payment warning has become one of the most prominent examples of an-
choring bias (e.g., Thaler and Sunstein, 2008). However, the literature on target values
would also predict that people may lean towards paying the minimum amount if the mini-
mumpaymentismadesalient,butthroughadifferentprocess. ThisisexaminedbyBartels
and Sussman (2016) using a lab study and observational data, finding that people see the
minimum payment salience as a target value. One of the benefits of the study in this paper
is that it is possible, through a randomized field experiment, to examine whether people
are following the minimum payment and statement balance warnings as two anchors or
targets in a natural setting. Specifically, it can be examined whether debtors change their
behavior to pay the minimum or the statement balance, or a little more, depending on
the warning, as if they were targets, or whether they adjust around those amounts as if
they were anchors. In this latter case, we should see an increase in payments below the
minimum and the statement balance.
Table VI shows the average treatment effect of the warnings on paying close to the
minimum and the statement balance using bins of 20 percent between payments. Based
on Equation 1, the dependent variables are calculated using each payment range (=1 if
paymentisinthatrange,0ifnot). Forexample,thefirstcolumnindicatesthatcardholders
decreased their chance of not paying anything for all warnings (vs. the control), and the
second column indicates that the likelihood of paying between any positive amount and
20%oftheminimumpracticallydidnotchangeasaresultofthewarnings. Notably,almost
everyestimateofthetoppartofTableVIshowsanegativemagnitudeforanyrangesmaller
than paying the minimum. If the minimum payment warning had acted as an anchor, we
should have seen positive values around the minimum. The bottom part of the table shows
theeffectofallwarningmessagesonpaymentsaroundthestatementbalance. Forexample,
column (10) shows the likelihood of paying an amount midway between the minimum and
the statement balance, indicating no sizable change in payments. In general, there are
positive estimates after the amount associated with each warning message, indicating that
cardholdersweremorelikelytopaytheminimumoralittlemore, orthestatementbalance
or a little more depending on the specific warning. Therefore, this analysis suggests that
it is more likely that debtors saw the warnings and associated amounts as target values
instead of anchors.
25From the New York Times: “‘Chile Woke Up’: Dictatorship’s Legacy of Inequality Triggers Mass Protests.”
(https://www.nytimes.com/2019/11/03/world/americas/chile-protests.html) and from InStoreView: “Crisis in
Chile: Losses and opportunities for retail (in Spanish)” (https://www.instoreview.com/crisis-en-chile-perdidas-y-
oportunidades-para-el-retail).

19
VI.C. Previous payment behavior, the minimum payment and the statement balance
One of the key components of the experimental design of the field experiment is its dual-
target setting of the minimum payment and statement balance warnings. Table VII shows
differences in the average treatment effects of the warnings depending on debtors’ previous
payment behavior and the specific amounts in the credit card statement they received
during the experiment, using the percentage of full payment as the dependent variable.
This outcome variable can capture any increase in payments and showed a heterogeneous
effect in all warnings based on the best linear predictor analysis.
Column 1 of Table VII shows a sub-sample of debtors who failed to pay at least the
minimum in one-half or more of the months prior to the intervention, i.e., they are debtors
who are more likely to become delinquent. For this sub-sample, receiving the minimum
payment warning or both warnings instead of the simple reminder increased the fraction
paidby3.5and3.8percentagepoints,respectively. Ontheotherhand,therewasnosizable
difference from zero for those who received the statement balance warning.
Table VII (column 2) shows a sub-sample of debtors who most of the time paid between
the minimum and the statement balance prior to the experiment (i.e., they are more likely
to pay a revolving amount). They increased the fraction paid during the experiment if
they received the statement balance warning or both warnings by 1.5 and 0.9 percentage
points, respectively. However, there was no sizable difference from zero in this sub-sample
for debtors who were in the minimum payment warning condition, consistent with the
findingthatthiswarningdidnotsignificantlyreducerevolvinginterest. Overall,despitethe
relatively small sample sizes in this analysis, the results suggest that debtors follow a self-
selectionprocessbyrespondingtospecificwarningmessages(increasingtheirpayments).26
Columns 3 and 4 of Table VII examine whether previous payment variation is affected
by the warnings, using the mean absolute deviation (MAD) from the mean fraction paid.
For example, a debtor who pays the same fraction of the statement balance every time will
have a MAD equal to 0 and is less likely to be affected by any warning as she is following
some sort of status quo. In contrast, a debtor who varies her payment fraction every
month prior to the experiment probably deliberated on how much to pay, and therefore,
the warnings are more likely to affect her payment decision (the maximum MAD can be
0.5forsomeonewhovariesfrompayinginfulltonotpayingatall). Usingamediansplitof
thiscovariate, columns3and4showthatdebtorswhohaveusuallychangedthepercentage
of the statement balance they pay every month increased their payments much more due
to the warnings than debtors who generally paid the same fraction, mainly when messages
include the statement balance warning.
Columns 5 to 10 use the minimum payment and statement balance amounts charged
in the credit card statements for the experiment as the warnings are associated with the
consequencesofpayingtheseamounts. Usingthemediansplitoftheseamounts,theresults
26Table A7 in the Online Appendix shows the payment distribution of these two sub-samples. It suggests that
debtorswhoaremorelikelynottopayatleasttheminimumshifttheirpaymentstowardtheminimumwhenreceiving
amessagewiththeminimumpaymentwarning,ascomparedtothosewhoreceivedthestatementbalancewarning
only.

20
indicate that the effects of the minimum payment warning and the statement balance
warning do not significantly vary depending on the amounts, except that the minimum
payment warning seems only to increase payments of debtors who had a low minimum
payment. Ontheotherhand,theeffectofthebothwarningsconditionseemstodependnot
only on the specific statement balance and the minimum payment amounts but especially
on their absolute difference. In particular, debtors who received both warnings increased
the fraction paid relatively more when the difference between the statement balance and
minimumpaymentwasrelativelysmall. Toillustrate,columns5and6indicatethatdebtors
who received both warnings increased the fraction paid by 1.0 percentage points (1.2%)
compared to the control group, when the difference between the minimum payment and
thestatementbalanceamountswassmall(Median=$259), andthatfractionincreasedby
0.4 percentage points (0.6%), although not significantly sizably different from zero, when
the difference between the amounts was great (Median = $1,598).
The previous reduced-form analyses may be susceptible to the specific median splits
of the sub-samples, and any form of interaction may miss other functional relationships
between variables (for completeness, Table A8 in the Online Appendix shows the results
using linear and quadratic interactions). The causal random forest approach can examine
whether the estimated treatment effects depend on the characteristics of debtors and bills
withmoreflexiblefunctions(e.g., AtheyandImbens,2019;DavisandHeller,2017). Using
the outputs from Section V, the panels of Figure 2 show the estimated conditional average
treatment effects on the y-axis, and each panel uses a different covariable in the x-axis.
The dashed lines are the benchmark for the estimated conditional average treatment effect
for each warning compared to the control condition. The results are mostly in line with
the reduced-form analysis. For example, panel A shows that the largest treatment effects
of the fraction paid are for debtors who usually partially pay their credit cards under the
conditions that include a statement balance warning. Panel B shows that all warnings
increase the estimated treatment effect as people varied more (MAD) how much of their
statement balance they usually pay, although to a lesser degree for the minimum payment
warning condition; and panel C shows that debtors with the largest (smallest) estimated
treatment effects due to the both warnings condition are characterized by a small (large)
gap between the minimum payment and the statement balance. Finally, Tables A9, A10
andA11intheOnlineAppendixshowthecovariatesacrossquintilesfromSectionV,sorted
by conditional average treatment effects. It shows, for example, for the both warnings
condition (Table A11), that a debtor from the top (bottom) quintile — the one with the
largest (smallest) conditional average treatment effect — has a mean absolute deviation
from the fraction paid of 24.4% (8.8%) and had a gap between the minimum payment and
statement balance of $1,217 ($1,953).
Insummary,theseanalysessuggestthat,firstofall,debtorsaremorelikelytobeaffected
by the warnings if they usually vary how much they pay. Even if all debtors included in
the experiment do not have automatic payment, they still may be used to paying the
same amount every month. Varying payments may be the result of deliberate decisions
and, therefore, how much to pay may change depending on the warning message. This

21
effect is separate from reminding people to pay like the message without warnings does
(controlcondition). Secondly,debtorswhowereinthebothwarningsconditionseemtopay
attention to a specific warning depending on whether or not they can pay more, based on
how much they used to pay and the gap between the minimum payment and the statement
balance, i.e., debtorschoosetoprioritizeaspecificwarningwhenbothwarningsaresalient.
This result offers new insights into individual decision-making in dual-target settings.
VI.D. Liquidity constraints
Similar to the previous analysis, Table VIII and Figure 3 examine whether the effects
of the warnings may be associated with liquidity constraints. Consistent with prior ev-
idence (Keys and Wang, 2019), the results show no relevant heterogeneous effects using
debtors’ income (columns 1 and 2 in Table VIII and Panel A of Figure 3) or the degree
of indebtedness with other lenders (columns 3 and 4 in Table VIII and Panel B of Figure
3).27 Therefore, cardholders may be increasing their payments because of the statement
balance warning, mainly by reducing consumption or by using savings. Tables A9, A10
and A11 in the Online Appendix also show no clear income pattern across the quintiles
sorted by the conditional average treatment effect, but they do show that debtors owing
little debt to the credit card issuer in the experiment may be more affected by the both
warnings message, i.e., part of the effect is coming from people who may be prioritizing
repayment with one institution because of the warning.28
VI.E. Understanding, financial knowledge, financial vulnerability, and cognitive reflection
Previous literature has shown that other factors not captured by the field experiment
may be associated with payment decisions. These factors may also be affecting the impact
of the statement balance and minimum payment warnings. In particular, prior research
has found a positive relationship between indebtedness caused by the effect of the mini-
mum payment and poor financial literacy (e.g., Artavanis and Karra, 2020; Hamid and
Loke, 2021), and financial vulnerability (Salisbury and Zhao, 2020). Although there is
no prior research on the statement balance warning, one hypothesis is that debtors with
poor financial literacy or financial vulnerability may benefit from the minimum payment
warning more than a statement balance warning. On the other hand, financial literacy
has been described as a long-term achievement, and messages, such as warnings, should
address in-the-moment decisions (Fernandes et al., 2014). It would also be important to
know whether the warnings can affect people’s specific understanding of the consequences
of paying less than the minimum and of paying in full.
27Thefirmusesascoreofhowmuchmoneyislentasapercentageshareofdebtinthebankingsystem(anytype
ofdebt). Thisscore,whichgoesfrom0to2.14(forconfidentialitypurposes,thescorewasnormalizedwithamean
of 1.0), indicates that people owe most of their debt to other lenders when the number is almost zero and only to
thefirmwhenitis2.14.
28A specific analysis of this group and their payment behavior in the subsequent billing cycle does not differ
significantly from the control group. This means that debtors who have more debt with other institutions are not
advancingdebtpaymentbecauseofthewarnings.

22
Inordertoexaminetherelationshipbetweenthewarningsandcognitivefactors,anonline
experiment was conducted in Prolific Academic (Peer et al., 2017) with debtors from the
USandtheUKwhohadusedacreditcardinthepreviousthreemonths. Participants(N=
400; female: 48.6%, 37.9 years old) saw a monthly credit card statement using the average
monthly amount in each country and the corresponding minimum payment (currency and
amounts were adjusted depending on where participants lived).29 Then they were asked
“how much would you repay?” with the following options: minimum payment, statement
balance, or another amount, in which case they had to type in a number. The information
and payment choices closely reflected how people worldwide see their credit card informa-
tion when paying online every month. Importantly, participants were randomly assigned
to four experimental conditions: minimum payment warning, statement balance warning,
both warnings, and no warning (control). After people input their payment decision, they
were asked how well they understood what the minimum payment and statement balance
mean (from 1: ”Not at all” to 7: ”Very well”), how much they generally pay on the credit
card(Salisbury,2014), theiraveragemonthlycreditcardpayment, afinancialvulnerability
scale (Salisbury and Zhao, 2020), financial knowledge questions (Navarro-Martinez et al.,
2011), and the Cognitive Reflection Test (Frederick, 2005), which has been associated with
the anchoring bias and present bias (Bergman et al., 2010; Welsh et al., 2013). Finally,
participants answered demographic questions. All materials are in the Online Appendix
A12.
Table IX shows the average treatment effect of each warning message on payment deci-
sions and the understanding of the minimum payment and the statement balance. First,
despite the hypothetical nature of the experiment, 16.8% of cardholders in the control
group chose to pay the minimum, 33.7% between the minimum and the statement balance,
and 49.5% chose to pay in full. Second, the results indicate that the warnings shifted
the payment distribution. The warning that included only the statement balance warning
increased the likelihood of deciding to pay in full by 18 percentage points compared to the
baseline no-warning condition, and the both warnings conditions increased this likelihood
by 25 percentage points. Messages including the statement balance warning also increased
the fraction paid of the statement balance, replicating the result from the field experiment,
although by much larger magnitudes due to the hypothetical nature of the online experi-
ment and also because more people likely paid attention to the message at the moment of
the decision. On the other hand, the minimum warning condition had no sizable effect on
payment decisions compared to the no-warning condition, although it is the only condition
with a positive estimate for the likelihood of paying the minimum.
ThelasttwocolumnsofTableIXshowthechangesintheunderstandingoftheminimum
payment and statement balance. First, there was a high average reported understanding
of the meaning of both amounts in the baseline (above six on a 7-point scale). Second,
cardholders, regardless of the type of warning, directionally increased their understand-
ing of the minimum payment compared to control, from 0.21 to 0.24 points (significance
levels at 9 to 15 percent). This suggests that any warning, even the statement balance
29Onepersonwasexcludedbecausetheydidnotcompletethestudy.

23
warning, could increase people’s perception of their understanding of the minimum pay-
ment. Somewhat different is the reaction of participants to their reported understanding
of what the statement balance means. In this case, people who saw the statement bal-
ance warning reported an increased understanding of this concept by 0.31 (both warnings)
and 0.23 (statement balance warning) points compared to the no-warning condition, with
significance levels at the 4 and 12 percent, respectively. In contrast, for the statement
balance understanding, the estimate of the minimum payment warning condition is much
smaller (with p = 0.41). Despite all the limitations of this outcome variable (self-reported,
ceiling effect, and statistical power), people may have improved their understanding of the
statement balance warning due to the warning messages. This finding is very consistent
with a study conducted with governmental institutions in Chile, which asked these ques-
tions differently: credit card owners were asked how much they would have to pay to avoid
additional revolving interest. Most of them (58 percent) answered correctly (i.e., they en-
teredthestatementbalance)whenthecreditcardstatementcontainedastatementbalance
warning, but only 26 percent correctly answered when they saw a credit card statement
with no warnings (SERNAC, 2021).
Table A13 (A and B) in the Online Appendix examines the role of financial knowledge,
financial vulnerability, and the cognitive reflection test (CRT) score. Based on the main
effects of these covariates, more financially literate cardholders with higher cognitive re-
flection test scores would pay a larger fraction of their statement balance. Nevertheless,
more importantly, there is no strong indication of a moderation of the warning treatment
effects using these variables, merely suggestive evidence that messages with the minimum
payment warning may be more effective for people with better financial knowledge and low
cognitive reflection test scores, indicating that this warning would affect people who make
a rapid decision after seeing these messages.
VII. CONCLUSION
This paper documents a new statement balance warning for credit card payments in
contrast to the so-called “perverse nudge” based on the minimum payment salience. There
are several results that trigger different conclusions. First, the warnings shift debtors’
payment distribution depending on the specific message. The statement balance warn-
ing increases payments and reduces interest by shifting payments towards the statement
balance. Compared to previous lab studies, the field experiment results on the minimum
payment warning show no clear perverse effect from highlighting the minimum payment
through a warning. In addition, the online study discussed in Section VI, structured in a
way similar to previous lab studies, does not suggest a backfiring effect either. One expla-
nation is that most previous lab studies focused on the time it takes to pay down the debt,
and a warning may be perceived as a softer manipulation. Nevertheless, this paper finds
that some cardholders are influenced to pay the minimum by the minimum warning.
Second, thequintilesbasedonthecausalrandomforestshowthat20to40percentofthe
sample significantly increased their payments because of the statement balance warning.
The rest already paid a large fraction of the statement balance, so little noticeable gain

24
was possible, they were more likely to pay the same percentage of the statement balance
every billing cycle or might not even pay attention to the email.30 Warnings also seemed
to be affected by the difference between the statement balance and minimum payment: it
is easier to pay more if the difference between these amounts is small, while when it is
great, the both warnings message may offer an option of making the minimum payment
that the statement balance only warning does not. This result sheds light on how people
may deal with dual-target settings, in which one of them is disregarded when it is hard to
achieve. In other words, people can choose one target message if they are able to pay a
higher amount. Ex-ante, it could have been predicted that the statement balance warning
may even discourage low-payers from making payment, but the results suggest that people
are just following the warnings as much as they can without reducing their payment. Also,
the warnings seem to be treated as targets or goals that cardholders try to achieve.
Third, the cardholder behavior was very similar for the statement balance warning only
andthebothwarningsmessages. Thisisthecaseexceptforadifferenceinthelikelihoodof
making the minimum payment when receiving the both warnings message, which is mainly
driven by debtors who historically were more likely to fail to pay at least the minimum
– a relatively small sub-sample in this population. The results were similar for these two
conditionsinthequintileanalysiswiththecausalrandomforestandtheonlineexperiment.
Nevertheless,thepolicyoptimizationanalysisindicatesagainfromusingdifferentmessages
to change repayment behavior, although using both warnings can be a good starting point.
Fourth, debtors who increase their payments and reduce their interest as a consequence
of the statement balance warning seem not to experience liquidity constraints. So, why
did they not pay more before? Recent research has explained this behavior by the credit
card puzzle or co-holding puzzle (Gathergood and Weber, 2014), where debtors do not use
liquid assets to repay their credit cards and reduce the costs of high interest. Consistently,
Vihri¨al¨a (2020) finds that households that are more likely to co-hold are more likely to
be “anchored” to paying the minimum payment, despite having the means to pay in full.
As the online experiment suggests, some debtors may need a salient explanation of the
consequences of not paying in full to pay more, just like the minimum payment salience
did for paying the minimum.
The results also have relevant policy implications. Compared to other solutions such as
increasingtheminimumpayment,thestatementbalancewarninghelpsconsumersdecrease
their debt without imposing a cost on the more constrained borrowers (D’Astous and
Shore,2017). Inaddition,whilesomebehavioralinterventionshavebeencontroversial(e.g.,
default options) because they depend on people not paying enough attention (Sunstein,
2019), warnings depend on the opposite, i.e., people paying attention to the information.
However,onelimitationisthattheinterventionwasconductedduringonebillingcycle,and
it may be relevant to know whether cardholders would still pay attention to the warnings
if they were included every period. This may motivate future research to examine whether
it is possible to have additive effects over a long period.
30There were tiny differences in the historic email opening rates, but in the opposite direction that one would
expect;thequintilewiththelargesttreatmenteffecthadaslightlylowerhistoricemailopeningrate.

25
Finally,thesuccessofanybehavioralinterventiondependsonitsdegreeofscalability(Al-
Ubaydlietal.,2017). Thestatementbalancewarningishighlyscalable. Forexample,asthe
online experiment suggests, it is possible to use the statement balance warning in online
payment settings, which are becoming more common in both developed and developing
countries. Furthermore, in the aftermath of the current study, the Chilean Consumer
Protection Bureau and the Ministry of Economy decided to regulate a new simplified
credit card statement for all credit cards. Based on this study, one of the main features of
these redesigned credit card statements is the statement balance warning. The first step
in changing the regulation was to conduct an online experiment testing different versions
of the redesigned credit card statement among a national sample of credit cardholders.
Results showed not only that the statement balance warning increased the intention to
increase payments, replicating the results of this paper, but also that it helped credit
cardholders learn how much to pay to reduce revolving interest (SERNAC, 2021).

26
REFERENCES
Adams, P., B. Guttman-Kenney, L. Hayes, S. Hunt, and N. Stewart (2018). Increasing
credit card payments using choice architecture: The case of anchors and prompts. FCA
| Occasional | Papers in Financial | Regulation | (Occasional | Paper No. | 42). |
| ---------- | ------------------- | ---------- | ----------- | --------- | ---- |
Agarwal, S., S. Chomsisengphet, and C. Lim (2017). What Shapes Consumer Choice and
Financial Products? A Review. Annual Review of Financial Economics 9(1), 127–146.
Agarwal, S., S. Chomsisengphet, N. Mahoney, and J. Stroebel (2015). Regulating con-
sumer financial products: Evidence from credit cards. The Quarterly Journal of Eco-
| nomics | 130(1), 111–164. |     |     |     |     |
| ------ | ---------------- | --- | --- | --- | --- |
Al-Ubaydli, O., J.A.List, andD.L.Suskind(2017). Whatcanwelearnfromexperiments?
understanding the threats to the scalability of experimental results. American Economic
| Review | 107(5), 282–86. |     |     |     |     |
| ------ | --------------- | --- | --- | --- | --- |
Allcott, H. and T. Rogers (2014). The short-run and long-run effects of behavioral in-
terventions: Experimental evidence from energy conservation. American Economic Re-
| view 104(10), | 3003–3037. |     |     |     |     |
| ------------- | ---------- | --- | --- | --- | --- |
Arenas, J. and D. Schwartz (2021). Using Causal Random Forest to Examine Spillover
| Effects | of Credit Card Payment | Reminders. | Technical | report. |     |
| ------- | ---------------------- | ---------- | --------- | ------- | --- |
Artavanis, N. and S. Karra (2020). Financial literacy and student debt. The European
| Journal | of Finance 26(4-5), | 382–401. |     |     |     |
| ------- | ------------------- | -------- | --- | --- | --- |
Athey, S. and G. Imbens (2016). Recursive partitioning for heterogeneous causal effects.
| Proceedings | of the National | Academy | of Sciences 113(27), | 7353–7360. |     |
| ----------- | --------------- | ------- | -------------------- | ---------- | --- |
Athey, S. and G. W. Imbens (2017). The state of applied econometrics: Causality and
policy evaluation. In Journal of Economic Perspectives, Volume 31, pp. 3–32. American
| Economic | Association. |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- |
Athey, S. and G. W. Imbens (2019). Machine Learning Methods That Economists Should
| Know about. | Annual Review | of Economics | 11, 685–725. |     |     |
| ----------- | ------------- | ------------ | ------------ | --- | --- |
Athey, S., J. Tibshirani, and S. Wager (2019). Generalized random forests. Annals of
| Statistics | 47(2), 1179–1203. |     |     |     |     |
| ---------- | ----------------- | --- | --- | --- | --- |
Athey, S. and S. Wager (2019). Estimating Treatment Effects with Causal Forests: An
Application.
Athey, S. and S. Wager (2021). Policy Learning With Observational Data. Economet-
| rica 89(1), | 133–161. |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
Bartels, D. and A. Sussman (2016). Anchors, Target Values, and Credit Card Payments.

27
Bergman, O., T. Ellingsen, M. Johannesson, and C. Svensson (2010). Anchoring and
| cognitive | ability. | Economics |     | Letters 107(1), | 66–68. |     |
| --------- | -------- | --------- | --- | --------------- | ------ | --- |
Bertrand,M.,E.Duflo,andS.Mullainathan(2004). Howmuchshouldwetrustdifferences-
in-differences estimates? The Quarterly Journal of Economics 119(1), 249–275.
Besley, T. and A. Case (2000). Unnatural Experiments? Estimating the Incidence of
| Endogenous | Policies. | The | Economic | Journal | 110(467), | 672–694. |
| ---------- | --------- | --- | -------- | ------- | --------- | -------- |
Bhamra, H.S.andR.Uppal(2019). Doeshouseholdfinancematter? Smallfinancialerrors
| with large | social | costs. |     |     |     |     |
| ---------- | ------ | ------ | --- | --- | --- | --- |
Board of Governors of the Federal Reserve System (2021). Delinquency Rate on Credit
Card Loans, All Commercial Banks [DRCCLACBS], August 2021. Technical report,
| Board    | of Governors | of     | the Federal | Reserve | System.  |              |
| -------- | ------------ | ------ | ----------- | ------- | -------- | ------------ |
| Breiman, | L. (2001).   | Random | forests.    | Machine | learning | 45(1), 5–32. |
Breiman, Friedman, O. and Stone (1984). Classication And Regression Trees. Monterey:
WadsworthandBrooks/Cole..
Campbell, J. Y. (2016). Restoring rational choice: The challenge of consumer financial
regulation. In American Economic Review, Volume 106, pp. 1–30. American Economic
Association.
Chernozhukov, V., D. Chetverikov, M. Demirer, E. Duflo, C. Hansen, W. Newey, and
J. Robins (2018). Double/debiased machine learning for treatment and structural pa-
| rameters. | The | Econometrics |     | Journal 21(1). |     |     |
| --------- | --- | ------------ | --- | -------------- | --- | --- |
Chernozhukov, V., M. Demirer, E. Duflo, and I. Fern´andez-Val (2018). Generic machine
learning inference on heterogeneous treatment effects in randomized experiments, with
| an application |     | to immunization |     | in india. | (24678). |     |
| -------------- | --- | --------------- | --- | --------- | -------- | --- |
D’Astous, P. and S. H. Shore (2017). Liquidity Constraints and Credit Card Delinquency:
EvidencefromRaisingMinimumPayments. Journal of Financial and Quantitative Anal-
| ysis 52(4), | 1705–1730. |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- | --- |
Davis, J. M. V. and S. B. Heller (2017). Using causal forests to predict treatment hetero-
geneity: An application to summer jobs. In American Economic Review, Volume 107,
| pp. 546–550. | American |     | Economic | Association. |     |     |
| ------------ | -------- | --- | -------- | ------------ | --- | --- |
El Issa, E. (2019). 2019 American Household Credit Card Debt Study.
Fernandes, D., J. G. Lynch, and R. G. Netemeyer (2014). Financial Literacy, Financial
Education, and Downstream Financial Behaviors. Management Science 60(8), 1861–
1883.

28
Fitch,C.,S.Hamilton,P.Bassett,andR.Davey(2011). Therelationshipbetweenpersonal
debtandmentalhealth: Asystematicreview. Mental Health Review Journal 16(4),153–
166.
Frederick, S. (2005). Cognitive Reflection and Decision Making. Journal of Economic
| Perspectives |     | 19(4), | 25–42. |     |     |     |     |
| ------------ | --- | ------ | ------ | --- | --- | --- | --- |
Galizzi, M. M. and D. Navarro-Martinez (2019). On the External Validity of Social Pref-
erence Games: A Systematic Lab-Field Study. Management Science 65(3), 976–1002.
Gathergood,J.andJ.Weber(2014). Self-control,financialliteracy&theco-holdingpuzzle.
| Journal | of Economic |     | Behavior | &   | Organization | 107, 455–469. |     |
| ------- | ----------- | --- | -------- | --- | ------------ | ------------- | --- |
Gin´e, Le´on, Negrin, Cort´es, and D. l. Cruz (2019). Simplification and Standardization of
Credit Card Statements: Evidence from a Lab Experiment in Mexico. Technical report.
Guttman-Kenney, B., J. Leary, and N. Stewart (2018). Weighing anchor on credit card
| debt. Financial |     | Conduct |     | Authority | Occasional | Paper Series | 43. |
| --------------- | --- | ------- | --- | --------- | ---------- | ------------ | --- |
Hamid, F. S. and Y. J. Loke (2021). Financial literacy, money management skill and credit
card repayments. International Journal of Consumer Studies 45(2), 235–247.
Heath, C., R. P. Larrick, and G. Wu (1999). Goals as Reference Points. Cognitive Psy-
| chology | 38(1), | 79–109. |     |     |     |     |     |
| ------- | ------ | ------- | --- | --- | --- | --- | --- |
Heckman, J. J., R. J. Lalonde, and J. A. Smith (1999). Chapter 31 The economics and
econometricsofactivelabormarketprograms. InHandbook of Labor Economics, Volume
| 3 PART, | pp. | 1865–2097. |     | Elsevier | B.V. |     |     |
| ------- | --- | ---------- | --- | -------- | ---- | --- | --- |
Hershfield, H. E. and N. J. Roese (2015). Dual payoff scenario warnings on credit card
statements elicit suboptimal payoff decisions. Journal of Consumer Psychology 25(1),
15–27.
Hodson, R., R. E. Dwyer, and L. A. Neilson (2014). Credit Card Blues: The Middle Class
and the Hidden Costs of Easy Credit. Sociological Quarterly 55(2), 315–340.
Homonoff, T., R. L. OBrien, and A. B. Sussman (2018). Does Knowing Your FICO Score
Change Financial Behavior? Evidence from a Field Experiment with Student Loan
| Borrowers. | SSRN |     | Electronic | Journal. |     |     |     |
| ---------- | ---- | --- | ---------- | -------- | --- | --- | --- |
Jiang, S. S. and L. F. Dunn (2013). New evidence on credit card borrowing and repayment
| patterns. | Economic |     | Inquiry | 51(1), | 394–407. |     |     |
| --------- | -------- | --- | ------- | ------ | -------- | --- | --- |
Jung, M. H., H. Perfecto, and L. D. Nelson (2016). Anchoring in Payment: Evaluat-
ing a Judgmental Heuristic in Field Experimental Settings. Journal of Marketing Re-
| search | 53(3), | 354–368. |     |     |     |     |     |
| ------ | ------ | -------- | --- | --- | --- | --- | --- |

29
Kahn-Lang, A. and K. Lang (2020, jul). The Promise and Pitfalls of Differences-in-
Differences: Reflectionson16andPregnantandOtherApplications. Journal of Business
| & Economic |     | Statistics 38(3), | 613–620. |     |     |     |     |     |
| ---------- | --- | ----------------- | -------- | --- | --- | --- | --- | --- |
Kahneman, D. and A. Tversky (1979). Prospect theory. Econommetrica 47(2), 263–292.
Keys, B. J., N. Mahoney, and H. Yang (2020). What Determines Consumer Financial
| Distress? | Place- | and Person-Based |     | Factors. SSRN | Electronic | Journal. |     |     |
| --------- | ------ | ---------------- | --- | ------------- | ---------- | -------- | --- | --- |
Keys, B.J.andJ.Wang(2019). Minimumpaymentsanddebtpaydowninconsumercredit
| cards. | Journal | of Financial | Economics | 131(3), | 528–548. |     |     |     |
| ------ | ------- | ------------ | --------- | ------- | -------- | --- | --- | --- |
Lieber, R. (2010). Your Card Has Been Declined, Just as You Wanted.
| MinEcon | (2012). | Decreto    | 44  | - APRUEBA   | REGLAMENTO  |     | SOBRE INFOR- |     |
| ------- | ------- | ---------- | --- | ----------- | ----------- | --- | ------------ | --- |
| MACIO´N | AL      | CONSUMIDOR |     | DE TARJETAS | DE CRE´DITO |     | BANCARIAS    | Y   |
NO BANCARIAS. Technical report, Biblioteca del Congreso Nacional de Chile.
https://www.bcn.cl/leychile/navegar?idNorma=1041745.
Navarro-Martinez, D., L. C. Salisbury, K. N. Lemon, N. Stewart, W. J. Matthews, and
A.J.Harris(2011). Minimumrequiredpaymentandsupplementalinformationdisclosure
effectsonconsumerdebtrepaymentdecisions. Journal of Marketing Research 48(SPEC.
| ISSUE), | S60–S77. |     |     |     |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Nelson, M. C., K. Lust, M. Story, and E. Ehlinger (2008). Credit card debt, stress and
key health risk behaviors among college students. American Journal of Health Promo-
| tion | 22(6), 400–407. |     |     |     |     |     |     |     |
| ---- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Norvilitis,J.M.,M.M.Merwin,T.M.Osberg,P.V.Roehling,P.Young,andM.M.Kamas
(2006). Personality Factors, Money Attitudes, Financial Knowledge, and Credit-Card
Debt in College Students1. Journal of Applied Social Psychology 36(6), 1395–1413.
Peer, E., L. Brandimarte, S. Samat, and A. Acquisti (2017). Beyond the Turk: Alter-
native platforms for crowdsourcing behavioral research. Journal of Experimental Social
| Psychology | 70,        | 153–163. |        |              |          |     |     |     |
| ---------- | ---------- | -------- | ------ | ------------ | -------- | --- | --- | --- |
| Resendiz,  | J. (2020). | Average  | Credit | Card Debt in | America. |     |     |     |
Retail Financiero (2019). Compendio Estad´ısco Mensual de la Industria del Cr´edito (Oc-
tubre 2019). Technical report, Retail Financiero. https://www.retailfinanciero.org/wp-
content/uploads/2020/01/Reporte-SBIF-Oct-2019.pdf.
RetailFinanciero(2021). CompendioEstad´ıscoMensualdelaIndustriadelCr´edito(Marzo
| 2021). | Technical | report, | Retail | Financiero. |     |     |     |     |
| ------ | --------- | ------- | ------ | ----------- | --- | --- | --- | --- |
Ru, H. and A. Schoar (2016). Do Credit Card Companies Screen for Behavioral Biases?
Technical report, National Bureau of Economic Research, Cambridge, MA.

30
Rubin, D. B. (1974). Estimating causal effects of treatments in randomized and nonran-
| domized studies. | Journal | of educational | Psychology | 66(5), 688–701. |
| ---------------- | ------- | -------------- | ---------- | --------------- |
Sahni, N. S., S. C. Wheeler, and P. Chintagunta (2018). Personalization in Email
Marketing: The Role of Noninformative Advertising Content. Marketing Science,
mksc.2017.1066.
Salisbury, L. C. (2014). Minimum payment warnings and information disclosure effects
on consumer debt repayment decisions. Journal of Public Policy and Marketing 33(1),
49–64.
Salisbury, L. C. and M. Zhao (2020). Active Choice Format and Minimum Payment Warn-
ings in Credit Card Repayment Decisions. Journal of Public Policy & Marketing 39(3),
284–304.
Schultz, P. W., J. M. Nolan, R. B. Cialdini, N. J. Goldstein, and V. Griskevicius (2007).
The constructive, destructive, and reconstructive power of social norms. Psychological
| science 18(5), | 429–34. |     |     |     |
| -------------- | ------- | --- | --- | --- |
Schwartz, D., B. Fischhoff, T. Krishnamurti, and F. Sowell (2013). The Hawthorne effect
and energy awareness. Proceedings of the National Academy of Sciences of the United
| States of America | 110(38), | 15242–15246. |     |     |
| ----------------- | -------- | ------------ | --- | --- |
Schwartz, D., E. A. Keenan, A. Imas, and A. Gneezy (2021). Opting-in to prosocial
incentives. Organizational Behavior and Human Decision Processes 163, 132–141.
Schwartz, D., G. Loewenstein, and L. Agu¨ero-Gaete (2020). Encouraging pro-
environmental behaviour through green identity labelling. Nature Sustainability 3(9),
| 746–752. https://www.nature.com/articles/s41893-020-0543-4. |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- |
Seira,E.,A.Elizondo,andE.Laguna-Mu¨ggenburg(2017). AreInformationDisclosuresEf-
fective? EvidencefromtheCreditCardMarket. American Economic Journal: Economic
| Policy 9(1), 277–307. |     |     |     |     |
| --------------------- | --- | --- | --- | --- |
SERNAC (2021). Evaluating the impact of communicating the credit card statement on
financial decisions: experimental evidence. https://www.sernac.cl/portal/619/articles-
| 62180 archivo | 03.pdf. |     |     |     |
| ------------- | ------- | --- | --- | --- |
Shift Processing (2021). Credit Card Statistics [Updated February 2021].
Soll, J. B., R. L. Keeney, and R. P. Larrick (2013). Consumer misunderstanding of credit
card use, payments, and debt: Causes and solutions. Journal of Public Policy & Mar-
| keting 32(1), | 1–49. |     |     |     |
| ------------- | ----- | --- | --- | --- |
Statista(2017).Creditcardusagebycountry.https://www.statista.com/statistics/675371/
ownership-of-credit-cards-globally-by-country/.

31
Stewart, N. (2009). The Cost of Anchoring on Credit-Card Minimum Repayments. Psy-
| chological | Science 20(1), | 39–41. |     |     |     |
| ---------- | -------------- | ------ | --- | --- | --- |
Sunstein, C. R. (2019). Which nudges do people like? a national survey. In Handbook of
| Behavioural | Change and | Public Policy. | Edward Elgar | Publishing. |     |
| ----------- | ---------- | -------------- | ------------ | ----------- | --- |
Sylvia, S., N. Warrinnier, R. Luo, A. Yue, O. Attanasio, A. Medina, and S. Rozelle (2021).
From Quantity to Quality: Delivering a Home-Based Parenting Intervention Through
China’s Family Planning Cadres. The Economic Journal 131(635), 1365–1400.
Thaler,R.H.andC.R.Sunstein(2008). Nudge: improvingdecisionsabouthealth. Wealth,
| and Happiness | 6, 14–38. |     |     |     |     |
| ------------- | --------- | --- | --- | --- | --- |
The Economist (2008). Credit cards - A nudge in the wrong direction. The
Economist. https://www.economist.com/finance-and-economics/2008/12/11/a-nudge-
in-the-wrong-direction.
Tversky,A.andD.Kahneman(1974). JudgmentunderUncertainty: HeuristicsandBiases.
| Science 185(4157), | 1124–1131. |     |     |     |     |
| ------------------ | ---------- | --- | --- | --- | --- |
Unsworth, K., G. Yeo, and J. Beck (2014). Multiple goals: A review and derivation of
general principles. Journal of Organizational Behavior 35(8), 1064–1078.
Vihri¨al¨a, E. (2020). Untangling the credit card debt puzzle. Available at SSRN 3710505.
Wager, S. and S. Athey (2018). Estimation and Inference of Heterogeneous Treatment
EffectsusingRandomForests. Journal of the American Statistical Association 113(523),
1228–1242.
Wang, J. and B. Keys (2014). Perverse nudges: Minimum payments and debt paydown in
| consumer | credit cards. | Technical Report | 4.  |     |     |
| -------- | ------------- | ---------------- | --- | --- | --- |
Welsh, M., N. Burns, and P. Delfabbro (2013). The cognitive reflec-
| tion test: | How | much more | than numerical | ability? | In Proceed- |
| ---------- | --- | --------- | -------------- | -------- | ----------- |
ings of the Annual Meeting of the Cognitive Science society, Volume 35.
https://escholarship.org/content/qt68n012fh/qt68n012fh noSplash 1e55cbb955ecbe352
3374393180ab1a7.pdf.

32
|     |             |            | VIII. TABLES      |      |         |                  |
| --- | ----------- | ---------- | ----------------- | ---- | ------- | ---------------- |
|     |             |            | TABLE I           |      |         |                  |
|     | DESCRIPTIVE | STATISTICS | AND RANDOMIZATION |      | BALANCE |                  |
|     |             |            | All Control       | MinW | SBalW   | BothW Difference |
p-value
|             |             |     | (1) (2)     | (3)   | (4)   | (5) (6)      |
| ----------- | ----------- | --- | ----------- | ----- | ----- | ------------ |
| Cardholder  | information |     |             |       |       |              |
| Age (years) |             |     | 44.4 44.3   | 44.4  | 44.4  | 44.4 0.8072  |
| Male        |             |     | 48.4% 48.4% | 48.6% | 48.4% | 48.3% 0.8278 |
Monthly income ($) 3,645.3 3,647.4 3,651.1 3,632.8 3,649.9 0.7814
Company’s internal credit score (0-100) 64.2 64.2 64.3 64.2 64.3 0.9160
| Credit card | statment for the | treatment period |     |     |     |     |
| ----------- | ---------------- | ---------------- | --- | --- | --- | --- |
Statement balance ($) 1,949.3 1,956.2 1,940.1 1,947 1,953.8 0.8585
| Minimum          | ($)        |                  | 415.7 414.6 | 414.2 | 417.8 | 416.3 0.7224 |
| ---------------- | ---------- | ---------------- | ----------- | ----- | ----- | ------------ |
| Payment behavior | before the | treatment period |             |       |       |              |
($)
| Previous | payment |     | 1208.2 1207.3 | 1202.2 | 1202.5 | 1220.8 0.5065 |
| -------- | ------- | --- | ------------- | ------ | ------ | ------------- |
Mean previous fraction of full 75.8% 75.7% 75.9% 75.8% 75.8% 0.8919
| Previously | paid in full     |     | 63.7% 63.6% | 63.8% | 63.8% | 63.7% 0.6400 |
| ---------- | ---------------- | --- | ----------- | ----- | ----- | ------------ |
| Previously | paid the minimum |     | 7.9% 7.9%   | 7.9%  | 7.8%  | 8.0% 0.4469  |
Previously did not pay at least the min 8.2% 8.3% 8.3% 8.3% 8.2% 0.7485
| N cardholders |     |     | 179,706 44,922 | 44,935 | 44,921 | 44,928 |
| ------------- | --- | --- | -------------- | ------ | ------ | ------ |
Notes: Cardholder and payment statistics for the whole sample are in column 1 and each experimental
condition in columns 2-5. Column 6 shows the p-value for the difference across conditions. Monetary
valueswerere-scaledforreasonsofconfidentialityusingaU.S.statementbalanceof$1,949.28asreference.
The credit score computed by the firm was also re-scaled to a range of 0 to 100, where a higher number
is a better credit score. MinW is the Minimum warning, SBalW is the Statement Balance Warning, and
| BothW is | the Both Warnings | condition. |     |     |     |     |
| -------- | ----------------- | ---------- | --- | --- | --- | --- |

33
|      |           |             | TABLE      | II         |            |              |               |
| ---- | --------- | ----------- | ---------- | ---------- | ---------- | ------------ | ------------- |
|      |           | WARNINGS    | EFFECT     | ON PAYMENT | BEHAVIOR   |              |               |
|      |           | ln(payment) | Less than  | Full       | Percent of | ln(revolving | ln(delinquent |
|      | Dep. Var. |             | min        |            | Full       | interest)    | interest)     |
|      |           | (1)         | (2)        | (3)        | (4)        | (5)          | (6)           |
| MinW |           | 0.0615***   | -0.0079*** | 0.0020     | 0.0030     | -0.0303      | -0.0739***    |
|      |           | (0.0206)    | (0.0018)   | (0.0025)   | (0.0019)   | (0.0200)     | (0.0155)      |
SBalW 0.0661*** -0.0067*** 0.0064*** 0.0068*** -0.0681*** -0.0422***
|     |     | (0.0207) | (0.0019) | (0.0025) | (0.0019) | (0.0200) | (0.0155) |
| --- | --- | -------- | -------- | -------- | -------- | -------- | -------- |
BothW 0.0778*** -0.0085*** 0.0069** 0.0070*** -0.0898*** -0.0797***
|          |               | (0.0206)   | (0.0019) | (0.0025) | (0.0019) | (0.0201) | (0.0155) |
| -------- | ------------- | ---------- | -------- | -------- | -------- | -------- | -------- |
| p-values | from pairwise | comparison |          |          |          |          |          |
| BothW    | vs. MinW      | 0.4244     | 0.7835   | 0.0443   | 0.0362   | 0.0031   | 0.7085   |
| BothW    | vs. SBalW     | 0.5681     | 0.3317   | 0.8281   | 0.9076   | 0.2792   | 0.0156   |
| SBalW    | vs. MinW      | 0.8226     | 0.4846   | 0.0729   | 0.0483   | 0.0595   | 0.0401   |
| Baseline | (Control)     | 11.080     | 0.097    | 0.625    | 0.741    | 4.424    | 1.552    |
| R2       |               | 0.023      | 0.003    | 0.036    | 0.040    | 0.174    | 0.083    |
N observations 2,853,939 2,853,939 2,853,939 2,853939 2,853939 2,853,939
| N carholders |     | 179,706 | 179,706 | 179,706 | 179,706 | 179,706 | 179,706 |
| ------------ | --- | ------- | ------- | ------- | ------- | ------- | ------- |
Notes: OLS estimates of Equation 1 using different dependent variables. Columns 1 to 4 use the payments
associatedwiththebillingcycleofthetreatmentperiod(t). Columns5and6usethecreditcardstatement
information one billing cycle after the experiment (t+1). SEs between parenthesis. MinW is the Minimum
warning, SBalW is the Statement Balance Warning, and BothW is the Both Warnings condition.
| * p<0.10, | ** p<0.05, | *** p<0.01 |     |     |     |     |     |
| --------- | ---------- | ---------- | --- | --- | --- | --- | --- |

34
|          |               |            |            | TABLE III  |              |               |           |
| -------- | ------------- | ---------- | ---------- | ---------- | ------------ | ------------- | --------- |
|          |               | WARNINGS   | EFFECT     | ON PAYMENT | DISTRIBUTION |               |           |
|          |               | No         | Between    | 0 Min      | Between Min  | Full no Extra | More than |
|          | Dep. Var.     | Payment    | and        | Min        | and Full     | Payment       | Full      |
|          |               | (1)        | (2)        | (3)        | (4)          | (5)           | (6)       |
| MinW     |               | -0.0053*** | -0.0026*** | 0.0052***  | 0.0008       | 0.0021        | -0.0001   |
|          |               | (0.0017)   | (0.0008)   | (0.0016)   | (0.0023)     | (0.0026)      | (0.0017)  |
| SBalW    |               | -0.0048*** | -0.0019**  | -0.0012    | 0.0015       | 0.0084***     | -0.0020   |
|          |               | (0.0017)   | (0.0008)   | (0.0016)   | (0.0023)     | (0.0026)      | (0.0017)  |
| BothW    |               | -0.0063*** | -0.0021*** | 0.0017     | -0.0002      | 0.0069***     | 0.0000    |
|          |               | (0.0017)   | (0.0008)   | (0.0016)   | (0.0023)     | (0.0026)      | (0.0017)  |
| p-values | from pairwise | comparison |            |            |              |               |           |
| BothW    | vs. MinW      | 0.5521     | 0.5177     | 0.0338     | 0.6637       | 0.0600        | 0.9534    |
| BothW    | vs. SBalW     | 0.3689     | 0.7502     | 0.0781     | 0.4700       | 0.5798        | 0.2311    |
| SBalW    | vs. MinW      | 0.7593     | 0.3324     | 0.0001     | 0.7734       | 0.0147        | 0.2529    |
| Baseline | (Control)     | 0.082      | 0.015      | 0.083      | 0.195        | 0.557         | 0.068     |
| R2       |               | 0.006      | 0.010      | 0.012      | 0.026        | 0.025         | 0.009     |
N observations 2,853,939 2,853,939 2,853,939 2,853939 2,853939 2,853,939
| N carholders |     | 179,706 | 179,706 | 179,706 | 179,706 | 179,706 | 179,706 |
| ------------ | --- | ------- | ------- | ------- | ------- | ------- | ------- |
Notes: OLS estimates of Equation 1 using different payment values or ranges as dependent variables. SEs
between parenthesis. MinW is the Minimum warning, SBalW is the Statement Balance Warning, and
| BothW     | is the Both | Warnings condition. |     |     |     |     |     |
| --------- | ----------- | ------------------- | --- | --- | --- | --- | --- |
| * p<0.10, | ** p<0.05,  | *** p<0.01          |     |     |     |     |     |

35
TABLE IV
SORTED CONDITIONAL AVERAGE TREATMENT EFFECTS
PER QUINTILE
Best Linear
Q1 Q2 Q3 Q4 Q5 Predictor
β β
0 1
Full Payment
MinW -0.8 -0.1 0.1 0.4 1.4 1.01 0.76***
(0.7) (0.7) (0.7) (0.7) (0.7) (1.37) (0.26)
SBalW -0.3 -0.2 0.2 1.3 2.4 1.00*** 0.54***
(0.7) (0.7) (0.7) (0.7) (0.7) (0.41) (0.26)
BothW 0.0 0.4 1.0 1.2 1.6 0.99** 0.18
(0.7) (0.7) (0.7) (0.7) (0.7) (0.33) (0.27)
Payment less than the minimum
MinW -0.3 -0.3 -0.7 -0.9 -1.5 1.00*** 0.60*
(0.4) (0.4) (0.4) (0.4) (0.4) (0.27) (0.34)
SBalW -0.2 -0.4 -0.4 -0.7 -1.2 1.00*** 0.16
(0.4) (0.4) (0.4) (0.4) (0.4) (0.32) (0.37)
BothW -0.2 -0.5 -0.8 -0.9 -1.4 1.01*** 0.16
(0.4) (0.4) (0.4) (0.4) (0.4) (0.26) (0.36)
Percentage of full
MinW -0.3 -0.2 0.0 0.8 1.0 1.00 0.65**
(0.6) (0.6) (0.6) (0.6) (0.6) (0.90) (0.27)
SBalW -0.3 0.1 0.3 1.0 1.9 1.01*** 0.46*
(0.6) (0.6) (0.6) (0.6) (0.6) (0.29) (0.24)
BothW -0.2 0.2 0.2 0.9 2.2 1.00*** 0.50*
(0.6) (0.6) (0.6) (0.6) (0.6) (0.28) (0.29)
Notes: Conditional average treatment effects for each quintile using
the control condition as baseline. SEs between parenthesis. MinW is
the Minimum warning, SBalW is the Statement Balance Warning, and
BothW is the Both Warnings condition. For the last two columns, β
0
correspondstotheconditionalaveragetreatmenteffectaccordingtothe
bestlinearpredictoranalysis. β worksasanomnibustestoftreatment
1
effect heterogeneity. One-sided heteroskedasticity-robust (HC3) SEs are
between parentheses.
* p<0.10, ** p<0.05, *** p<0.01

36
|     |          |                |     | TABLE V |            |          |     |
| --- | -------- | -------------- | --- | ------- | ---------- | -------- | --- |
|     | WARNINGS | POST-TREATMENT |     | EFFECT  | ON PAYMENT | BEHAVIOR |     |
Period One Billing Cycle after Treatment Two Billing Cycles after Treatment
|          |               | Less than  | Full     | ln(payment) | Less than | Full     | ln(payment) |
| -------- | ------------- | ---------- | -------- | ----------- | --------- | -------- | ----------- |
|          | Dep.          | Var. Min   |          |             | Min       |          |             |
|          |               | (1)        | (2)      | (3)         | (4)       | (5)      | (6)         |
| MinW     |               | -0.0038*   | -0.0007  | 0.0557**    | -0.0014   | −0.00004 | -0.0121     |
|          |               | (0.0021)   | (0.0027) | (0.0269)    | (0.0019)  | (0.0026) | (0.0267)    |
| TotW     |               | 0.0005     | -0.0010  | 0.0007      | -0.0015   | 0.0027   | 0.0245      |
|          |               | (0.0022)   | (0.0019) | (0.0027)    | (0.0026)  | (0.0272) | (0.0267)    |
| BothW    |               | -0.0049**  | 0.0019   | 0.0524*     | -0.0028   | -0.0017  | -0.0055     |
|          |               | (0.0021)   | (0.0027) | (0.0270)    | (0.0019)  | (0.0026) | (0.0267)    |
| p-values | from pairwise | comparison |          |             |           |          |             |
| BothW    | vs. MinW      | 0.6101     | 0.4823   | 0.3327      | 0.5347    | 0.9016   | 0.8042      |
| BothW    | vs. SBalW     | 0.0117     | 0.5001   | 0.2740      | 0.0963    | 0.0563   | 0.2626      |
| SBalW    | vs. MinW      | 0.0440     | 0.9790   | 0.9002      | 0.2973    | 0.0418   | 0.1710      |
| Baseline | (Control)     | 0.138      | 0.110    | 0.559       | 0.565     | 10.238   | 10.315      |
R2
|     |     | 0.012 | 0.016 | 0.149 | 0.232 | 0.396 | 0.540 |
| --- | --- | ----- | ----- | ----- | ----- | ----- | ----- |
N observations 2,853,949 2,853,949 2,853,949 2,853,949 2,853,949 2,853,949
N cardholders 179,706 179,706 179,706 179,706 179,706 179,706
Notes: OLS estimates of Equation 1 using different dependent variables for payment behavior one
billing cycle after the experiment (t+1) in columns 1 to 3, and two billing cycle after the experiment
(t+2) in columns 4 to 6. SEs between parenthesis. MinW is the Minimum warning, SBalW is the
| Statement | Balance    | Warning,   | and BothW is | the Both Warnings | condition. |     |     |
| --------- | ---------- | ---------- | ------------ | ----------------- | ---------- | --- | --- |
| * p<0.10, | ** p<0.05, | *** p<0.01 |              |                   |            |     |     |

|     |     |     |     |          |     |        | TABLE | VI    |         |     |        |     |     |     |
| --- | --- | --- | --- | -------- | --- | ------ | ----- | ----- | ------- | --- | ------ | --- | --- | --- |
|     |     |     |     | WARNINGS |     | EFFECT | ON    | SMALL | PAYMENT |     | RANGES |     |     |     |
No Payment Payment Payment Payment Payment Exact Payment Payment
Dep Var Payment ]0,20%min] ]20,40%] ]40,60%] ]60,80%] ]80,99%] Min ]min,20%full] ]20,40%]
|     |     |     | (1) |     | (2) |     | (3) | (4) |     | (5) | (6) | (7) | (8) | (9) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MinW -0.0053*** 0.0001 0.0001 -0.0011*** -0.0009** -0.0009* 0.0052*** 0.0010 0.0011
(0.0017) (0.0002) (0.0003) (0.0004) (0.0004) (0.0005) (0.0016) (0.0016) (0.0014)
SBalW -0.0048*** −0.00003 0.0002 -0.0003 -0.0007* -0.0011** -0.0012 0.0002 -0.0009
(0.0017) (0.0002) (0.0003) (0.0004) (0.0004) (0.0005) (0.0016) (0.0016) (0.0014)
BothW -0.0063*** -0.0003 0.0001 -0.0003 -0.0007 -0.0010** 0.0017 0.0014 -0.0030**
(0.0017) (0.0002) (0.0003) (0.0004) (0.0004) (0.0004) (0.0016) (0.0016) (0.0014)
| p-values from | pairwise comparison |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
BothW vs MinW 0.5521 0.0941 0.9689 0.0424 0.5806 0.7104 0.0338 0.7892 0.0023
BothW vs SBalW 0.3689 0.2055 0.7387 0.9166 0.9174 0.9276 0.0781 0.4241 0.1118
SBalW vs MinW 0.7593 0.6613 0.7067 0.0530 0.6521 0.6459 0.0001 0.5959 0.1498
Baseline (Control) 0.082 0.001 0.001 0.004 0.004 0.005 0.083 0.075 0.046
| R2  |     |     | 0.006 |     | 0.000 | 0.001 |     | 0.005 |     | 0.002 | 0.002 | 0.012 | 0.015 | 0.003 |
| --- | --- | --- | ----- | --- | ----- | ----- | --- | ----- | --- | ----- | ----- | ----- | ----- | ----- |
N observations 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939
N cardholders 179,706 179,706 179,706 179,706 179,706 179,706 179,706 179,706 179,706
|     |     |     | Payment | Payment |     | Payment |     | Exact | Payment |     | Payment | Payment | Payment |     |
| --- | --- | --- | ------- | ------- | --- | ------- | --- | ----- | ------- | --- | ------- | ------- | ------- | --- |
Dep Var ]40,60%] ]60,80%] ]80,99%] Full ]full,120%] ]120,140%] ]140,160%] ]160%+ full]
|     |     |     | (10) | (11) |     | (12) |     | (13) |     | (14) | (15) | (16) | (17) |     |
| --- | --- | --- | ---- | ---- | --- | ---- | --- | ---- | --- | ---- | ---- | ---- | ---- | --- |
MinW 0.0002 -0.0002 -0.0013 0.0037 -0.0002 -0.00004 0.0001 -0.0010
|     |     |     | (0.0012) | (0.0010) |     | (0.0009) |     | (0.0026) | (0.0006) |     | (0.0005) | (0.0004) | (0.0012) |     |
| --- | --- | --- | -------- | -------- | --- | -------- | --- | -------- | -------- | --- | -------- | -------- | -------- | --- |
SBalW 0.0005 0.0021** -0.0004 0.0077*** 0.0003 -0.0002 -0.0006 0.0007
|     |     |     | (0.0012) | (0.0010) |     | (0.0009) |     | (0.0026) | (0.0007) |     | (0.0005) | (0.0004) | (0.0012) |     |
| --- | --- | --- | -------- | -------- | --- | -------- | --- | -------- | -------- | --- | -------- | -------- | -------- | --- |
BothW 0.0009 0.0007 -0.0001 0.0057* 0.0011 0.0001 -0.0006 0.0000
|               |                     |     | (0.0012) | (0.0010) |     | (0.0009) |     | (0.0026) | (0.0007) |     | (0.0005) | (0.0004) | (0.0012) |     |
| ------------- | ------------------- | --- | -------- | -------- | --- | -------- | --- | -------- | -------- | --- | -------- | -------- | -------- | --- |
| p-values from | pairwise comparison |     |          |          |     |          |     |          |          |     |          |          |          |     |
BothW vs MinW 0.5616 0.4175 0.1720 0.4438 0.0487 0.8444 0.0595 0.4039
BothW vs SBalW 0.7219 0.1826 0.8031 0.4431 0.2247 0.5283 0.9864 0.5878
SBalW vs MinW 0.8225 0.0316 0.2697 0.1245 0.4469 0.6643 0.0596 0.1686
Baseline (Control) 0.033 0.024 0.017 0.534 0.009 0.005 0.003 0.030
| R2  |     |     | 0.002 | 0.001 |     | 0.001 |     | 0.022 |     | 0.000 | 0.000 | 0.000 | 0.010 |     |
| --- | --- | --- | ----- | ----- | --- | ----- | --- | ----- | --- | ----- | ----- | ----- | ----- | --- |
N observations 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939
37
N cardholders 179,706 179,706 179,706 179,706 179,706 179,706 179,706 179,706
Notes: OLS estimates of Equation 1 using different payment ranges as dependent variables. SEs between parenthesis. MinW is the
| Minimum   | warning, SBalW | is         | the Statement | Balance | Warning, |     | and BothW | is  | the Both | Warnings | condition. |     |     |     |
| --------- | -------------- | ---------- | ------------- | ------- | -------- | --- | --------- | --- | -------- | -------- | ---------- | --- | --- | --- |
| * p<0.10, | ** p<0.05,     | *** p<0.01 |               |         |          |     |           |     |          |          |            |     |     |     |

38
TABLE VII
WARNINGS EFFECT BASED ON PREVIOUS PAYMENT BEHAVIOR, THE MINIMUM PAYMENT AND THE STATEMENT BALANCE
Likely Between Low MAD High MAD Small Diff Large Diff Low High Low High
Subsample Paid Less Min and Percentage of Percentage of between Min between Min Statement Statement Min Min
than Min Full Full Full and Stat. Bal. and Stat. Bal. Balance Balance
Percentage Percentage Percentage Percentage Percentage Percentage Percentage Percentage Percentage Percentage
Dep. Var. of Full of Full of Full of Full of Full of Full of Full of Full of Full of Full
(1) (2) (3) (4) (5) (6) (7) (8) (9) (10)
MinW 0.0354** 0.0019 0.0011 0.0048 0.0034 0.0029 0.0031 0.0032 0.0050* 0.0011
(0.0172) (0.0050) (0.0018) (0.0033) (0.0028) (0.0026) (0.0028) (0.0025) (0.0029) (0.0025)
SBalW 0.0184 0.0148*** 0.0022 0.0113*** 0.0081*** 0.0053* 0.0075*** 0.0061** 0.0087*** 0.0050**
(0.0174) (0.0051) (0.0018) (0.0033) (0.0028) (0.0026) (0.0028) (0.0025) (0.0029) (0.0025)
BothW 0.0377** 0.0090* 0.0040** 0.0097*** 0.0104*** 0.0037 0.0085*** 0.0057** 0.0101*** 0.0041
(0.0175) (0.0051) (0.0018) (0.0033) (0.0028) (0.0026) (0.0028) (0.0025) (0.0029) (0.0025)
p-values from pairwise comparison
BothW vs MinW 0.8917 0.1661 0.0989 0.1459 0.0113 0.7600 0.0545 0.3351 0.0752 0.2388
BothW vs SBalW 0.2669 0.2548 0.3156 0.6330 0.4062 0.5355 0.7242 0.8518 0.6154 0.7046
SBalW vs MinW 0.3200 0.0107 0.5241 0.0536 0.0890 0.3539 0.1173 0.2495 0.2043 0.1182
Baseline (Control) 0.506 0.489 0.846 0.638 0.846 0.637 0.829 0.653 0.771 0.711
R2 0.078 0.136 0.044 0.051 0.027 0.065 0.024 0.067 0.023 0.064
N observations 65,213 429,016 1,449,756 1,404,183 1,332,393 1,521,546 1,317,171 1,536,768 1,312,390 1,541,549
N cardholders 5,026 25,793 89,435 90,271 89,851 89,855 89,838 89,868 89,766 89,940
Notes: OLSestimatesofEquation1usingthepercentageofthestatementbalancepaid(“PercentageofFull”)asdependentvariable. Eachcolumnisadifferentsubsample:
column1showsdebtorswhousuallyfailedtopayatleasttheminimumbeforetheexperiment, column2thosewhousuallypaidbetweentheminimumandthestatement
balance (i.e., a revolving amount) before the experiment, column 3 (column 4) the debtors with a relatively low (high) mean absolute deviation from the fraction paid,
column5(column6)thedebtorswhosawarelativelysmall(large)differencebetweentheminimumpaymentandthestatementbalance,column7(column8)thedebtors
who saw a relatively high (low) statement balance, and column 9 (column 10) the debtors who saw a relatively high (low) minimum payment amount. SEs are between
parenthesis. MinW is the Minimum warning, SBalW is the Statement Balance Warning, and BothW is the Both Warnings condition.
* p<0.10, ** p<0.05, *** p<0.01

39
TABLE VIII
WARNINGS EFFECT BASED ON
INCOME AND SHARE OF DEBT LEVELS
Low High Low score High score
Subsample
income income share of debt share of debt
Percentage Percentage Percentage Percentage
Dep. Var. of Full of Full of Full of Full
(1) (2) (3) (4)
MinW 0.0013 0.0048* 0.0045 0.0016
(0.0027) (0.0027) (0.0029) (0.0025)
SBalW 0.0085*** 0.0051* 0.0076*** 0.0061**
(0.0026) (0.0027) (0.0029) (0.0025)
BothW 0.0054** 0.0088*** 0.0090*** 0.0051**
(0.0027) (0.0027) (0.0029) (0.0025)
p-values from pairwise comparison
BothW vs MinW 0.1201 0.1463 0.1217 0.1557
BothW vs SBalW 0.2437 0.1795 0.6332 0.6767
SBalW vs MinW 0.0065 0.9238 0.2846 0.0666
Baseline (Control) 0.760 0.722 0.710 0.772
R2 0.042 0.043 0.038 0.044
N observations 1,389,575 1,464,364 1,391,292 1,462,647
N cardholders 89,654 90,052 89,833 89,873
Notes: OLS estimates of Equation 1 using the percentage of the statement bal-
ancepaid(“PercentageofFull”)asdependentvariable. Eachcolumnisadiffer-
ent subsample: column 1 (column 2) shows debtors with a relatively low (high)
income, and column 3 (column 4) debtors with a relatively low (high) share of
theirdebtwiththelender. SEsarebetweenparenthesis. MinWistheMinimum
warning, SBalW is the Statement Balance Warning, and BothW is the Both
Warnings condition.
* p<0.10, ** p<0.05, *** p<0.01

40
|          |           |          |            |        |           |         | TABLE     | IX         |         |               |           |               |
| -------- | --------- | -------- | ---------- | ------ | --------- | ------- | --------- | ---------- | ------- | ------------- | --------- | ------------- |
|          |           | WARNINGS |            | EFFECT | ON        | PAYMENT | DECISIONS |            | AND     | UNDERSTANDING |           |               |
|          |           |          |            |        | THROUGH   | AN      | ONLINE    | EXPERIMENT |         |               |           |               |
|          |           |          | Min        |        | Between   |         | Full      | Percentage |         | Understanding |           | Understanding |
|          | Dep.      | Var.     |            |        | Min and   | Full    |           |            | of Full | Minimum       | Statement | Balance       |
|          |           |          | (1)        |        | (2)       |         | (3)       |            | (4)     | (5)           |           | (6)           |
| MinW     |           |          | 0.028      |        | -0.027    |         | -0.000    |            | 0.004   | 0.207         |           | 0.124         |
|          |           |          | (0.051)    |        | (0.056)   |         | (0.068)   |            | (0.060) | (0.146)       |           | (0.149)       |
| SBalW    |           |          | -0.008     |        | -0.177*** |         | 0.185***  | 0.154***   |         | 0.243*        |           | 0.233         |
|          |           |          | (0.051)    |        | (0.059)   |         | (0.067)   |            | (0.059) | (0.145)       |           | (0.148)       |
| BothW    |           |          | -0.080     |        | -0.180*** |         | 0.260***  | 0.222***   |         | 0.233         |           | 0.311**       |
|          |           |          | (0.050)    |        | (0.059)   |         | (0.067)   |            | (0.059) | (0.144)       |           | (0.147)       |
| p-values | from      | pairwise | comparison |        |           |         |           |            |         |               |           |               |
| BothW    | vs        | MinW     | 0.035      |        | 0.011     |         | 0.000     |            | 0.000   | 0.862         |           | 0.211         |
| BothW    | vs        | SBalW    | 0.156      |        | 0.958     |         | 0.265     |            | 0.247   | 0.944         |           | 0.596         |
| SBalW    | vs        | MinW     | 0.484      |        | 0.013     |         | 0.007     |            | 0.012   | 0.809         |           | 0.470         |
| Baseline | (Control) |          | 0.170      |        | 0.337     |         | 0.495     |            | 0.570   | 6.277         |           | 6.267         |
R2
|                |     |     | 0.012 |     | 0.038 |     | 0.055 |     | 0.051 | 0.009 |     | 0.013 |
| -------------- | --- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | ----- | --- | ----- |
| N observations |     |     | 400   |     | 400   |     | 400   |     | 400   | 400   |     | 400   |
Notes: OLS estimates of Equation 1 using different dependent variables in the online experiment. Columns 1 to 4
use the payments decisions. Columns 5 and 6 use self-reported measures of understanding the minimum payment
andthestatementbalance. SEsarebetweenparenthesis. MinWistheMinimumwarning,SBalWistheStatement
| Balance   | Warning, |            | and BothW | is     | the Both | Warnings | condition. |     |     |     |     |     |
| --------- | -------- | ---------- | --------- | ------ | -------- | -------- | ---------- | --- | --- | --- | --- | --- |
| * p<0.10, |          | ** p<0.05, | ***       | p<0.01 |          |          |            |     |     |     |     |     |

41
IX. FIGURES
Figure1.CHANGESINPAYMENTDISTRIBUTION(WITHTHECONTROLCONDITIONASTHEBASE-
LINE)
(a) PanelA (b) PanelB
(c) PanelC
Notes: Eachpanelcontainstheaveragetreatmenteffectsforeachwarning,wherethebaselineisthecontrol
condition,onthelikelihoodofeachofthepossiblepayments(fromTableIII). Errorbarsindicate95%confidence
intervals.

42
Figure2.WARNINGSESTIMATEDCATEBASEDONPREVIOUSPAYMENTBEHAVIOR,THEMINIMUM
AND THE STATEMENT BALANCE AMOUNTS
(a) PreviousPercentageofFull(%)
(b) MADPercentageofFull
(c) Differencebetweentheminimumandthestatementbalanceamounts($)
(d) StatementBalance($)
Notes: ThisFigureshowstheestimatedconditionalaveragetreatmenteffectsonthefractionpaidonthey-axis,
andeachpanelusesadifferentcovariableinthex-axis. Thedashedlinesarethebenchmarkfortheestimated
conditionalaveragetreatmenteffectforeachwarningcomparedtothecontrolcondition. Errorbarsindicate95%
confidenceintervals.

43
Figure 3. WARNINGS ESTIMATED CATE BASED ON INCOME AND SHARE OF DEBT
(a) Income
(b) ShareofDebtScore
Notes: ThisFigureshowstheestimatedconditionalaveragetreatmenteffectsonthefractionpaidonthey-axis,
andeachpanelusesadifferentcovariableinthex-axis. Panel(a)usesdebtors’income(inUSdollars)re-scaled
usingastatementbalanceof$1,949.28. Panel(b)usesare-scaledshareofdebt(0: peoplewhohavealltheirdebt
withotherlenders,and2.14: theyhavealltheirdebtwiththefirm). Thedashedlinesarethebenchmarkforthe
estimatedconditionalaveragetreatmenteffectforeachwarningcomparedtothecontrolcondition. Errorbars
indicate95%confidenceintervals.

1
APPENDIX (FOR ONLINE PUBLICATION)
A1. Pilot Study
The following study was part of a different study examining the role of payment re-
minders with the same Latin American credit card issuer as in the field experiment in this
paper but conducted more than two years before. There were seven treatment conditions
sent by email and a control condition.31 The sample size varied from 20 to 30 thousand
for each treatment condition, and it was 251 thousand for the control.
• Simple reminder: “We remind you that your [card name] is due on [date].”
• Full amount only: [Simple reminder] + statement balance ($) amount in bold.
• Statement balance warning (benefit framing): [simple remainder] + statement bal-
ance ($) amount inbold +the warning: “If you pay the statement balancebefore the
duedate, youwillavoidadditionalinterestcharges.”[sameasinthefieldexperiment]
• Statement balance warning (cost framing): [simple reminder] + statement balance
($) amount in bold + the warning: “If you pay less than the statement balance, your
outstanding balance will accrue interest charges in your next billing cycle.”
• Statementbalancewarning(costframing)andaddingminimum: [simplereminder]+
statementbalance($)amountinbold+minimum($)amountinbold+thewarning:
“If you pay less than the statement balance, your outstanding balance will accrue
interest charges in your next billing cycle.”
• Placebo: “Remember these tips and protect your password.” [and a list of standard
tips]
• Control condition: People did not receive any email.
Table A1 shows the average treatment effects from linear regression models using each
experimental condition as an independent variable where the baseline was the control con-
dition. The dependent variables were the likelihood of paying in full, not paying at least
the minimum, and the fraction of the statement balance.
The results indicate that all warning messages increase the likelihood of paying in full,
reducethelikelihoodofnotpayingatleasttheminimum,andincreasethepercentageofthe
fraction paid compared to the control group. In particular, the most successful statement
balancewarningmessageistheoneframedasabenefit, andthereforethatonewasusedfor
this paper, increasing the likelihood of paying in full by 2 percent (1.3 percentage points)
31Inaddition,remindersweresentatdifferenttimesbeforethepaymentduedate,butthisfactorisnotanalyzed
here.

2
more than the control group. Secondly, the condition using only the statement balance
amountandnowarning(“Fullamountonly”)isnotstatisticallysignificantlydifferentfrom
the control group. Third, a simple reminder by itself increases the likelihood of paying in
full by 1.1 percent (0.7 percentage points) and, given the null result from the placebo,
indicates that the effect is coming from reminding people and not from the contact from
the firm.
|         |           | TABLE   | A1   |        |       |       |            |
| ------- | --------- | ------- | ---- | ------ | ----- | ----- | ---------- |
| AVERAGE | TREATMENT | EFFECTS |      | OF THE | PILOT | STUDY |            |
|         |           |         | Full |        | Less  | than  | Percentage |
Dep. Var.
|                 |                          |         |           |     | Min        |     | of Full   |
| --------------- | ------------------------ | ------- | --------- | --- | ---------- | --- | --------- |
|                 |                          |         | (1)       |     | (2)        |     | (3)       |
| Placebo         |                          |         | 0.0002    |     | -0.0016    |     | 0.0001    |
|                 |                          |         | (0.0030)  |     | (0.0022)   |     | (0.0025)  |
| Simple reminder |                          |         | 0.0071**  |     | -0.0052**  |     | 0.0079*** |
|                 |                          |         | (0.0029)  |     | (0.0021)   |     | (0.0024)  |
| SBalW (benefit  | framing)                 |         | 0.0131*** |     | -0.0070*** |     | 0.0107*** |
|                 |                          |         | (0.0028)  |     | (0.0021)   |     | (0.0023)  |
| SBalW (cost     | framing)                 |         | 0.0087*** |     | -0.0073*** |     | 0.0082*** |
|                 |                          |         | (0.0028)  |     | (0.0021)   |     | (0.0023)  |
| SBalW (cost     | framing) & adding        | min.    | 0.0030    |     | -0.0051**  |     | 0.0050**  |
|                 |                          |         | (0.0028)  |     | (0.0021)   |     | (0.0023)  |
| Full amount     | only                     |         | 0.0035    |     | -0.0034    |     | 0.0030    |
|                 |                          |         | (0.0035)  |     | (0.0025)   |     | (0.0028)  |
| R2              |                          |         | 0.0001    |     | 0.0001     |     | 0.0001    |
| N observations  |                          |         | 411,309   |     | 411,309    |     | 411,309   |
| Notes:          | SEs between parenthesis. |         |           |     |            |     |           |
| * p <           | 0.10, ** p < 0.05,       | *** p < | 0.01      |     |            |     |           |

3
|                |             | TABLE       | A2           |           |             |           |
| -------------- | ----------- | ----------- | ------------ | --------- | ----------- | --------- |
| WARNINGS       |             | EFFECT      | ON MAIN      | PAYMENT   |             |           |
| DISTRIBUTION   |             | USING       | A LOGIT      |           | MODEL       |           |
|                |             | Less than   |              | Min       |             | Full      |
| Dep.           | Var.        | Min         |              |           |             |           |
|                |             | (1)         |              | (2)       |             | (3)       |
| MinW           |             | -0.0860***  | 0.0825***    |           |             | 0.0150    |
|                |             | (0.0236)    | (0.0246)     |           |             | (0.0154)  |
| SBalW          |             | -0.0706***  | -0.0141      |           | 0.0369**    |           |
|                |             | (0.0236)    | (0.0251)     |           |             | (0.0154)  |
| BothW          |             | -0.0980***  | 0.0441*      |           | 0.0404***   |           |
|                |             | (0.0237)    | (0.0248)     |           |             | (0.0154)  |
| ll             |             | -50,985.808 | -47,627.145  |           | -99,445.711 |           |
| N observations |             | 179,706     | 179,706      |           |             | 179,706   |
| Notes:         | Logit model | estimates   | for          | the       | treatment   | period    |
| using the      | main        | payment     | values       | or ranges | as          | dependent |
| variables.     | SEs         | between     | parenthesis. | MinW      | is          | the Mini- |
mumwarning,SBalWistheStatementBalanceWarning,
| and BothW | is the     | Both | Warnings   | condition. |     |     |
| --------- | ---------- | ---- | ---------- | ---------- | --- | --- |
| * p<0.10, | ** p<0.05, |      | *** p<0.01 |            |     |     |

TABLE A3
|           |           | WARNINGS  | EFFECT    | ON MAIN | PAYMENT DISTRIBUTION |     |      |      |      |
| --------- | --------- | --------- | --------- | ------- | -------------------- | --- | ---- | ---- | ---- |
|           | Less than | Less than | Less than | Min     | Min                  | Min | Full | Full | Full |
| Dep. Var. | Min       | Min       | Min       |         |                      |     |      |      |      |
|           | (1)       | (2)       | (3)       | (4)     | (5)                  | (6) | (7)  | (8)  | (9)  |
MinW -0.0079*** -0.0079*** -0.0079*** 0.0050*** 0.0049*** 0.0052*** 0.0027 0.0027 0.0020
(0.0018) (0.0018) (0.0018) (0.0017) (0.0017) (0.0016) (0.0026) (0.0026) (0.0025)
SBalW -0.0066*** -0.0066*** -0.0067*** -0.0012 -0.0012 -0.0012 0.0066*** 0.0066** 0.0066***
(0.0019) (0.0019) (0.0019) (0.0016) (0.0016) (0.0016) (0.0026) (0.0026) (0.0025)
BothW -0.0083*** -0.0083*** -0.0085*** 0.0015 0.0015 0.0017 0.0075*** 0.0075*** 0.0069***
(0.0019) (0.0019) (0.0019) (0.0016) (0.0016) (0.0016) (0.0026) (0.0026) (0.0025)
| Time effects | No    | Yes   | Yes   | No    | Yes   | Yes   | No    | Yes   | Yes   |
| ------------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| X s          | No    | No    | Yes   | No    | No    | Yes   | No    | No    | Yes   |
| R2           | 0.000 | 0.001 | 0.003 | 0.000 | 0.003 | 0.012 | 0.000 | 0.002 | 0.036 |
N observations 2,853,949 2,853,949 2,853,939 2,853,949 2,853,949 2,853,939 2,853,949 2,853,949 2,853,939
N cardholders 179,706 179,706 179,706 179,706 179,706 179,706 179,706 179,706 179,706
Notes: OLSestimatesofEquation1usingdifferentmainpaymentvaluesorrangesasdependentvariables. SEsbetweenparenthesis.
MinW is the Minimum warning, SBalW is the Statement Balance Warning, and BothW is the Both Warnings condition.
| * p<0.10, | ** p<0.05, | *** p<0.01 |     |     |     |     |     |     |     |
| --------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
4

5
TABLE A4
WARNINGS EFFECT ON MAIN PAYMENT
DISTRIBUTION INCLUDING ALL ACCOUNTS
Less than Min Full
Dep. Var. Min
(1) (2) (3)
MinW -0.0082*** 0.0052*** 0.0025
(0.0019) (0.0016) (0.0025)
SBalW -0.0073*** -0.0013 0.0063**
(0.0019) (0.0016) (0.0025)
BothW -0.0090*** 0.0019 0.0063**
(0.0019) (0.0016) (0.0025)
R2 0.006 0.013 0.033
N observations 3,112,110 3,112,110 3,112,110
N cardholders 179,753 179,753 179,753
Notes: OLS estimates of Equation 1 using differ-
ent main payment values or ranges as dependent
variables. SEs between parenthesis. MinW is the
Minimum warning, SBalW is the Statement Balance
Warning, and BothW is the Both Warnings condi-
tion.
* p<0.10, ** p<0.05, *** p<0.01

6
TABLE A5
RELATIVE CHANGE IN
CONDITIONAL AVERAGE TREATMENT
EFFECTS PER QUINTILE
Q1 Q2 Q3 Q4 Q5
Full Payment
MinW -1.1 -0.1 0.2 0.7 2.3
69.0 59.0 70.5 51.7 62.7
-0.8 -0.1 0.1 0.4 1.4
SBalW -0.5 -0.3 0.2 2.1 4.0
68.8 57.4 64.9 62.8 58.8
-0.3 -0.2 0.2 1.3 2.4
BothW 0.0 0.8 1.5 1.7 2.6
65.8 50.2 67.0 69.8 59.7
0.0 0.4 1.0 1.2 1.6
Payment less than the minimum
MinW -15.5 -4.0 -11.3 -7.9 -3.3
9.9 21.1 5.8 4.1 7.6
-1.5 -0.9 -0.7 -0.3 -0.3
SBalW -11.8 -3.2 -8.3 -4.4 -5.9
10.1 21.6 4.7 8.3 3.6
-1.2 -0.7 -0.4 -0.4 -0.2
BothW -5.8 -8.5 -18.7 -15.0 -3.8
24.0 10.9 4.4 3.3 5.6
-1.4 -0.9 -0.8 -0.5 -0.2
Percentage of full
MinW -0.4 -0.2 0.0 1.0 1.4
63.9 77.9 77.8 81.0 70.1
-0.3 -0.2 0.0 0.8 1.0
SBalW -0.4 0.2 0.4 1.5 2.9
75.5 79.7 82.2 67.6 65.7
-0.3 0.1 0.3 1.0 1.9
BothW -0.2 0.2 0.3 1.2 3.2
80.4 79.8 70.1 73.3 67.0
-0.2 0.2 0.2 0.9 2.2
Notes: The first row shows the relative change
in the conditional average treatment effect
(CATE) for each quintile. The second row
(smaller font and italics) shows the the base-
line from the control group. The third row
(smaller font and italics) is the CATE in per-
centage points as shown in Table IV. MinW
is the Minimum warning, SBalW is the State-
mentBalanceWarning,andBothWistheBoth
Warnings condition.

7
TABLE A6
SORTED CONDITIONAL AVERAGE TREATMENT EFFECTS
PER QUINTILE BETWEEN WARNINGS
Best Linear
Q1 Q2 Q3 Q4 Q5 Predictor
β β
0 1
Full Payment
MinW (vs. BothW) -2.0 -1.2 -0.7 0.5 1.2 1.01** -0.02
(0.7) (0.7) (0.7) (0.7) (0.7) (0.42) (0.31)
MinW (vs. SBalW) -1.2 -0.6 -0.5 0.0 0.3 1.00* -0.34
(0.7) (0.7) (0.7) (0.7) (0.7) (0.57) (0.29)
BothW (vs. SBalW) -1.1 -0.6 0.4 0.5 0.6 1.05 -0.25
(0.7) (0.7) (0.7) (0.7) (0.7) (1.88) (0.29)
Payment less than the minimum
MinW (vs. BothW) -0.9 -0.3 -0.2 0.9 1.1 1.21 0.50*
(0.4) (0.4) (0.4) (0.4) (0.4) (4.92) (0.26)
MinW (vs. SBalW) -0.8 -0.5 -0.3 0.3 0.7 1.00 0.09
(0.4) (0.4) (0.4) (0.4) (0.4) (1.93) (0.42)
BothW (vs. SBalW) -0.2 0.1 0.2 0.4 0.6 1.02 -0.14
(0.4) (0.4) (0.4) (0.4) (0.4) (1.28) (0.42)
Percentage of full
MinW (vs. BothW) -1.7 -0.6 -0.2 0.1 0.4 1.01** 0.29
(0.6) (0.6) (0.6) (0.6) (0.6) (0.38) (0.29)
MinW (vs. SBalW) -0.7 -0.6 -0.3 -0.2 -0.2 1.00** -0.23
(0.5) (0.5) (0.5) (0.5) (0.5) (0.43) (0.28)
BothW (vs. SBalW) -0.4 -0.1 0.1 0.2 0.2 1.00 0.31
(0.6) (0.6) (0.6) (0.6) (0.6) (4.23) (0.28)
Notes: Conditional average treatment effects for each quintile between warning
conditions. The baseline is indicated as the second group after “vs.” SEs between
parenthesis. MinW is the Minimum warning, SBalW is the Statement Balance
Warning, and BothW is the Both Warnings condition. For the last two columns,
β corresponds to the conditional average treatment effect from the best linear
0
predictoranalysis. β worksasanomnibustestfortreatmenteffectheterogeneity.
1
One-sided heteroskedasticity-robust (HC3) SEs are between parentheses .
* p<0.10, ** p<0.05, *** p<0.01

8
TABLE A7
WARNINGS EFFECTS ON PAYMENT DISTRIBUTION
BASED ON PREVIOUS PAYMENT BEHAVIOR
Panel A - Likely paid less than the Min
Less than Min Between Full
Dep Var Min Min and Full
(1) (2) (3) (4)
MinW -0.0479** 0.0229* 0.0100 0.0157
(0.0212) (0.0132) (0.0157) (0.0188)
SBalW -0.0193 -0.0007 -0.0070 0.0253
(0.0212) (0.0127) (0.0153) (0.0189)
BothW -0.0506** 0.0155 0.0137 0.0212
(0.0213) (0.0130) (0.0157) (0.0191)
p-values for pairwise comparison
BothW vs MinW 0.8991 0.5834 0.8131 0.7691
BothW vs SBalW 0.1352 0.2141 0.1776 0.8252
SBalW vs MinW 0.1699 0.0729 0.2681 0.6034
Baseline(Control) 0.364 0.083 0.152 0.401
R2 0.107 0.010 0.033 0.051
N observation 65,213 65,213 65,213 65,213
N cardholders 5,026 5,026 5,026 5,026
Panel B - Likely paid between Min and Full
Less than Min Between Full
Dep Var Min Min and Full
(1) (2) (3) (4)
MinW -0.0084* 0.0001 0.0139* -0.0052
(0.0048) (0.0053) (0.0084) (0.0068)
SBalW -0.0085* -0.0100* 0.0104 0.0081
(0.0047) (0.0051) (0.0083) (0.0068)
BothW -0.0095** -0.0108** 0.0150* 0.0052
(0.0048) (0.0052) (0.0084) (0.0069)
p-values for pairwise comparison
BothW vs MinW 0.8176 0.0351 0.8975 0.1330
BothW vs SBalW 0.8332 0.8694 0.5865 0.6813
SBalW vs MinW 0.9830 0.0506 0.6776 0.0524
Baseline(Control) 0.086 0.099 0.607 0.207
R2 0.010 0.011 0.117 0.131
N observations 429,016 429,016 429,016 429,016
N cardholders 25,793 25,793 25,793 25,793
Notes: OLS estimates of Equation 1 using different main payment values or ranges
as dependent variables. Columns in Panel A include a sub-sample of debtors who
usuallyfailedtopayorpaidlessthantheminimumbeforetheexperiment. Columns
inPanelBincludeasub-sampleofdebtorswhousuallypaidbetweentheminimum
and the statement balance before the experiment. SEs between parenthesis. MinW
istheMinimumwarning,SBalWistheStatementBalanceWarning,andBothWis
the Both Warnings condition.
* p<0.10, ** p<0.05, *** p<0.01

|     |     |     | TABLE A8 |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- |
WARNINGSEFFECTBASEDONPREVIOUSPAYMENTBEHAVIOR,THEMINIMUMAND
THESTATEMENTBALANCEAMOUNTSUSINGINTERACTIONS
Percentage Percentage Percentage Percentage Percentage Percentage Percentage Percentage
DepVar offull offull offull offull offull offull offull offull
|     | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
MinW 0.0013 0.0013 0.0046** 0.0021 0.0049** 0.0022 0.0053** 0.0061**
(0.0020) (0.0020) (0.0023) (0.0027) (0.0024) (0.0029) (0.0025) (0.0029)
SBalW 0.0026 0.0014 0.0075*** 0.0054** 0.0077*** 0.0055* 0.0080*** 0.0099***
(0.0020) (0.0020) (0.0023) (0.0028) (0.0024) (0.0030) (0.0025) (0.0030)
BothW 0.0041** 0.0037* 0.0078*** 0.0060** 0.0081*** 0.0065** 0.0090*** 0.0130***
(0.0020) (0.0019) (0.0023) (0.0026) (0.0024) (0.0029) (0.0026) (0.0030)
MADprevious MADprevious Diffbetween Diffbetween Statement Statement Minimum($) Minimum($)
X=
|     | %offull(%) | %offull(%) | SBandmin($) | SBandmin($) | Balance($) | Balance($) |     |     |
| --- | ---------- | ---------- | ----------- | ----------- | ---------- | ---------- | --- | --- |
MinW×X 0.0129 0.0105 -0.0010 0.0017 -0.0009 0.0012 -0.0053 -0.0094
(0.0159) (0.0459) (0.0007) (0.0018) (0.0007) (0.0016) (0.0036) (0.0066)
SBalW×X 0.0312** 0.0658 -0.0004 0.0019 -0.0005 0.0015 -0.0029 -0.0109
(0.0159) (0.0462) (0.0007) (0.0019) (0.0007) (0.0017) (0.0036) (0.0070)
BothW×X 0.0205 0.0276 -0.0005 0.0019 -0.0005 0.0012 -0.0047 -0.0210***
(0.0158) (0.0460) (0.0007) (0.0017) (0.0007) (0.0015) (0.0037) (0.0069)
| MinW×X2  |       | 0.0059   |       | -0.0002   |       | -0.0001  |      | 0.0022    |
| -------- | ----- | -------- | ----- | --------- | ----- | -------- | ---- | --------- |
|          |       | (0.1311) |       | (0.0001)  |       | (0.0001) |      | (0.0022)  |
| SBalW×X2 |       | -0.0905  |       | -0.0002   |       | -0.0001  |      | 0.0033    |
|          |       | (0.1317) |       | (0.0001)  |       | (0.0001) |      | (0.0024)  |
| BothW×X2 |       | -0.0121  |       | -0.0002** |       | -0.0001* |      | 0.0062*** |
|          |       | (0.1314) |       | (0.0001)  |       | (0.0001) |      | (0.0024)  |
| R2       | 0.040 | 0.040    | 0.040 | 0.040     | 0.040 | 0.040    | 0,04 | 0,04      |
Nobservation 2,851,884 2,851,884 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939 2,853,939
Ncardholders 178,870 178,870 179,706 179,706 179,706 179,706 179,706 179,706
Notes: OLSestimatesofEquation1plusthemaineffectofacovariate(X)anditslinearandquadraticinteractionwiththewarningsconditions. Allmodels
usingthepercentagepaidofthestatementbalance(“PercentageofFull”)asthedependentvariable. SEsbetweenparenthesis. MinWistheMinimumwarning,SBalW
istheStatementBalanceWarning,andBothWistheBothWarningscondition.
*p<0.10,**p<0.05,***p<0.01
9

10
TABLE A9
COVARIATES FOR EACH QUINTILE - MINIMUM PAYMENT WARNING
Minimum Payment Warning
Q1 Q2 Q3 Q4 Q5
CATE Fraction Paid (%) -0.3 -0.2 0.0 0.8 1.0
(0.6) (0.6) (0.6) (0.6) (0.6)
Age (years) 42.0 44.4 44.9 45.5 45.0
(0.10) (0.10) (0.10) (0.10) (0.10)
Male (%) 48.7 48.9 48.3 47.4 49.1
(0.4) (0.4) (0.4) (0.4) (0.4)
Mean previous % of full (%) 65.8 80.0 79.8 83.2 70.2
(0.2) (0.2) (0.2) (0.2) (0.2)
MAD previous % of full (%) 17.0 9.5 11.6 8.9 22.0
(0.1) (0.1) (0.1) (0.1) (0.1)
Statement balance ($) 2,420 2,028 1,816 1,776 1,701
(30) (20) (21) (18) (22)
Difference between SB and min ($) 1,953 1,547 1,432 1,365 1,371
(27) (18) (18) (16) (20)
Previous payment ($) 1,409 1,328 1,144 1,224 919
(24) (15) (11) (12) (11)
Monthly income ($) 3,809 3,389 3,689 3,417 3,942
(25) (21) (22) (20) (23)
Share of Debt Score (0 to 2.1) 0.9 1.1 1.0 1.1 0.9
(0.01) (0.01) (0.01) (0.01) (0.01)
Company’s credit score (0-100) 56.0 64.5 67.8 67.8 65.2
(0.12) (0.11) (0.12) (0.12) (0.15)
Mean email opening rate (%) 50.0 51.4 51.1 51.6 50.0
(0.2) (0.2) (0.2) (0.2) (0.2)
Notes: For the minimum-payment warning (vs. control) analysis, quintiles are
sorted by the conditional average treatment effects on the fraction paid. Each
row shows the mean value for each covariate and standard errors are between
parenthesis. Forreasonsofconfidentiality,monetaryamounts($)werere-scaled
usingastatementbalanceof$1,949.28(inUSdollars). Shareofdebtscorewas
re-scaled(0: peoplewhooweotherlenders,and2.14: theyowealltheirdebtto
thefirm). Creditscorewasre-scaledwhere100wasthebestscore(lowestrisk).

11
|               |     |          |          | TABLE  | A10         |       |         |         |        |
| ------------- | --- | -------- | -------- | ------ | ----------- | ----- | ------- | ------- | ------ |
| COVARIATES    | FOR | EACH     | QUINTILE |        | - STATEMENT |       | BALANCE | WARNING |        |
|               |     |          |          |        | Statement   |       | Balance | Warning |        |
|               |     |          |          | Q1     |             | Q2    | Q3      | Q4      | Q5     |
| CATE Fraction |     | Paid (%) |          | -0.3   |             | 0.1   | 0.3     | 1.0     | 1.9    |
|               |     |          |          | (0.6)  |             | (0.6) | (0.6)   | (0.6)   | (0.6)  |
| Age (years)   |     |          |          | 44.2   |             | 44.6  | 45.5    | 43.5    | 44     |
|               |     |          |          | (0.10) | (0.10)      |       | (0.10)  | (0.10)  | (0.10) |
| Male (%)      |     |          |          | 50     |             | 47.7  | 50.3    | 47.8    | 46.2   |
|               |     |          |          | (0.4)  |             | (0.4) | (0.4)   | (0.4)   | (0.4)  |
| Mean previous | %   | of full  | (%)      | 78.6   |             | 82.7  | 84.9    | 70.3    | 62.4   |
|               |     |          |          | (0.2)  |             | (0.2) | (0.2)   | (0.2)   | (0.2)  |
| MAD previous  | %   | of full  | (%)      | 9.9    |             | 8.5   | 6.7     | 16.6    | 27.2   |
|               |     |          |          | (0.1)  |             | (0.1) | (0.1)   | (0.1)   | (0.1)  |
($)
| Statement        | balance |        |     | 2,026     |     | 1,903 | 2,064 | 2,205 | 1,560 |
| ---------------- | ------- | ------ | --- | --------- | --- | ----- | ----- | ----- | ----- |
|                  |         |        |     | (29)      |     | (20)  | (22)  | (23)  | (18)  |
| Difference       | between | SB and | min | ($) 1,646 |     | 1,457 | 1,575 | 1,755 | 1,244 |
|                  |         |        |     | (26)      |     | (18)  | (20)  | (20)  | (16)  |
| Previous payment |         | ($)    |     | 1,242     |     | 1,280 | 1,518 | 1,190 | 794   |
|                  |         |        |     | (21)      |     | (13)  | (18)  | (12)  | (10)  |
($)
| Monthly income |            |             |                     | 3,775          |          | 3,487     | 3,642           | 3,742     | 3,553         |
| -------------- | ---------- | ----------- | ------------------- | -------------- | -------- | --------- | --------------- | --------- | ------------- |
|                |            |             |                     | (23)           |          | (22)      | (22)            | (23)      | (22)          |
| Share of Debt  | Score      | (0 to       | 2.1)                | 0.9            |          | 1.1       | 1.1             | 1.0       | 0.9           |
|                |            |             |                     | (0.01)         | (0.01)   |           | (0.01)          | (0.01)    | (0.01)        |
| Company’s      | credit     | score       | (0-100)             | 61.4           |          | 66.6      | 67.3            | 63.2      | 62.6          |
|                |            |             |                     | (0.14)         | (0.12)   |           | (0.12)          | (0.12)    | (0.14)        |
| Mean email     | opening    | rate        | (%)                 | 50.7           |          | 51.4      | 51.9            | 50.3      | 49.1          |
|                |            |             |                     | (0.2)          |          | (0.2)     | (0.2)           | (0.2)     | (0.2)         |
| Notes:         | For the    | statement   | balance             | warning        | (vs.     | control)  | analysis,       |           | quintiles are |
| sorted by      | the        | conditional | average             | treatment      |          | effects   | on the fraction |           | paid. Each    |
| row shows      | the        | mean        | value for           | each covariate |          | and       | standard        | errors    | are between   |
| parenthesis.   | For        | reasons     | of confidentiality, |                | monetary |           | amounts         | ($) were  | re-scaled     |
| using a        | statement  | balance     | of $1,949.28        |                | (in US   | dollars). | Share           | of debt   | score was     |
| re-scaled      | (0: people | who         | owe other           | lenders,       | and      | 2.14:     | they owe        | all their | debt to       |
| the firm).     | Credit     | score       | was re-scaled       | where          | 100      | was       | the best score  | (lowest   | risk).        |

12
TABLE A11
COVARIATES FOR EACH QUINTILE - BOTH WARNINGS
Both Warnings
Q1 Q2 Q3 Q4 Q5
CATE Fraction Paid (%) -0.2 0.2 0.2 0.9 2.2
(0.6) (0.6) (0.6) (0.6) (0.6)
Age (years) 44.5 44.6 42.8 44.5 45.5
(0.10) (0.10) (0.10) (0.10) (0.10)
Male (%) 48.4 47.9 50.7 47.8 46.8
(0.4) (0.4) (0.4) (0.4) (0.4)
Mean previous % of full (%) 82.4 81.4 73.1 75.3 66.5
(0.2) (0.2) (0.2) (0.2) (0.2)
MAD previous % of full (%) 8.8 10.4 10.6 14.8 24.4
(0.1) (0.1) (0.1) (0.1) (0.1)
Statement balance ($) 2,065 1,743 2,722 1,732 1,514
(22) (21) (26) (21) (24)
Difference between SB and min ($) 1,615 1,364 2,133 1,369 1,217
(20) (19) (24) (19) (21)
Previous payment ($) 1,514 1,153 1,774 944 686
(18) (14) (22) (11) (9)
Monthly income ($) 3,582 3,456 4,053 3,511 3,641
(22) (21) (25) (21) (23)
Share of Debt Score (0 to 2.1) 1.1 1.1 1.0 1.0 0.8
(0.01) (0.01) (0.01) (0.01) (0.01)
Company’s credit score (0-100) 66.6 66.3 60.8 64 63.6
(0.12) (0.12) (0.13) (0.12) (0.14)
Mean email opening rate (%) 51.6 50.9 51.7 50.0 49.6
(0.2) (0.2) (0.2) (0.2) (0.2)
Notes: For the both warning (vs. control) analysis, quintiles are sorted by the
conditional average treatment effects on the fraction paid. Each row shows
themeanvalueforeachcovariateandstandarderrorsarebetweenparenthesis.
For reasons of confidentiality, monetary amounts ($) were re-scaled using a
statement balance of $1,949.28 (in US dollars). Share of debt score was re-
scaled (0: people who owe other lenders, and 2.14: they owe all their debt to
thefirm). Creditscorewasre-scaledwhere100wasthebestscore(lowestrisk).

13
A12. Material of online experiment
• Are you more familiar with U.S. dollars or British pounds?
◦ $ (US Dollar)
◦ £ (British Pound)
◦ I am not familiar with any of these currencies.
• Payment information
Imagine that you own a credit card and you are about to make your monthly repayment.
The next screen will show summary information from your credit card balance.
Please consider how much you can afford to pay, and treat your payment decision as you
would in your everyday life.
Payment Due Date [date]
Statement Balance [$]
Minimum Payment [$]
[Warnings,ifany]
[Values depending on the currency selected:]
UK: minimum (£17.30), statement balance (£691.82).
US: minimum ($33.89), statement balance ($1,355.67).
[Randomassignmenttonowarnings, minimumpayment, statementbalance, orbothwarn-
ings, using:]
Minimum payment warning: ”If you make at least the Minimum Payment ([$]), you will
pay additional interest, but you will avoid late fees.”
Statement balance warning: ”If you pay the Statement Balance [$]), you will not pay
any additional interest or fees.”
• How much will you repay?
◦ Minimum payment
◦ Statement balance
◦ Other amount: [participants could type in the amount]
• Please answer these two questions about the information you just saw [the following
two questions are randomly ordered]
◦ How well do you understand what the minimum payment means? (1=Not at
all/7=Very well)

14
◦ How well do you understand what the statement balance means? (1=Not at
all/7=Very well)
• During the last 12 months, please answer to what extent you agree with the following
statements [1 “Strongly disagree”, 2 “Disagree”, 3 “Somewhat disagree”, 4 “Neither dis-
agree nor agree”, 5 “Somewhat agree”, 6 “Agree”, 7 “Strongly agree”]
◦ I always pay my credit card balance off in full each month
◦ I often make only the minimum payment on my credit card bills
• [Payments with credit card from Salisbury (2014)]
• Considering the last 12 months, please answer which range best reflects the amount
you usually repay for your credit card [using UK and US ranges]
• [Financial vulnerability from Salisbury and Zhao (2020)]
• [Financial literacy from Navarro-Martinez et al. (2011)]
• [Cognitive reflection test from Frederick (2005)]
• Demographics: age, gender, occupation, annual income [using UK and US ranges], and
educational level. Were the rules about the study clear? Do you have any comments about
the study?
• Open-ended question about any comment about the study.

15
TABLE A13 - A
WARNINGS EFFECT BASED ON COGNITIVE FACTORS
IN THE ONLINE EXPERIMENT (WITH INTERACTIONS)
Percentage Percent Percentage
Dep. Var. of Full of Full of Full
(1) (2) (3)
MinW 0.047 -0.067 -0.010
(0.065) (0.125) (0.100)
SBalW 0.171*** 0.110 0.198*
(0.063) (0.122) (0.097)
BothW 0.246*** 0.209* 0.346***
(0.062) (0.125) (0.097)
X = Financial Vulnerability Financial Literacy CRT (Score)
X -0.027 0.097** 0.074**
(0.018) (0.039) (0.033)
MinW × X -0.035 0.043 0.018
(0.027) (0.057) (0.048)
SBalW × X -0.025 0.027 -0.019
(0.028) (0.055) (0.049)
BothW × X -0.035 0.013 -0.067
(0.026) (0.057) (0.048)
R2 0.115 0.130 0.085
N observations 400 400 400
Notes: OLSestimatesofEquation1plusthemaineffectofacovariate(X)and
its linear interaction with the warnings conditions. All models using the per-
centageofthestatementbalancepaid(“PercentageofFull”)asthedependent
variable. SEsbetweenparenthesis. MinWistheMinimumwarning,SBalWis
theStatementBalanceWarning,andBothWistheBothWarningscondition.
* p<0.10, ** p<0.05, *** p<0.01

16
|     |     |     | TABLE | A13 - B |     |     |     |
| --- | --- | --- | ----- | ------- | --- | --- | --- |
WARNINGS EFFECT BASED ON COGNITIVE FACTORS IN THE ONLINE EXPERIMENT
High Financial Low Financial Low Financial High Financial Low CRT High CRT
Subsample
Vulnerability Vulnerability Literacy Literacy (Score) (Score)
Percentage Percentage Percentage Percentage Percentage Percentage
| Dep.          | Var.                | of Full  | of Full | of Full | of Full  | of Full  | of Full |
| ------------- | ------------------- | -------- | ------- | ------- | -------- | -------- | ------- |
|               |                     | (1)      | (2)     | (3)     | (4)      | (5)      | (6)     |
| MinW          |                     | 0.037    | 0.003   | -0.051  | 0.134*   | 0.030    | 0.003   |
|               |                     | (0.067)  | (0.111) | (0.081) | (0.075)  | (0.094)  | (0.076) |
| SBalW         |                     | 0.130**  | 0.207*  | 0.139*  | 0.185**  | 0.205**  | 0.135*  |
|               |                     | (0.065)  | (0.117) | (0.082) | (0.072)  | (0.093)  | (0.076) |
| BothW         |                     | 0.183*** | 0.268** | 0.195** | 0.319*** | 0.331*** | 0.154*  |
|               |                     | (0.063)  | (0.125) | (0.079) | (0.075)  | (0.090)  | (0.078) |
| p-values from | pairwise comparison |          |         |         |          |          |         |
| BothW vs      | MinW                | 0.027    | 0.030   | 0.002   | 0.021    | 0.001    | 0.064   |
| BothW vs      | SBalW               | 0.401    | 0.628   | 0.479   | 0.081    | 0.143    | 0.814   |
| SBalW vs      | MinW                | 0.166    | 0.072   | 0.018   | 0.500    | 0.055    | 0.095   |
R2
|                |     | 0.036 | 0.068 | 0.051 | 0.110 | 0.094 | 0.030 |
| -------------- | --- | ----- | ----- | ----- | ----- | ----- | ----- |
| N observations |     | 286   | 114   | 245   | 155   | 183   | 217   |
Notes: OLS estimates of Equation 1 using the percentage of the statement balance paid (“Percentage of Full”) as the
dependentvariable. Eachcolumnisadifferentsub-sample. SEsbetweenparenthesis. MinWistheMinimumwarning,
SBalW is the Statement Balance Warning, and BothW is the Both Warnings condition.
| * p<0.10, | ** p<0.05, | *** p<0.01 |     |     |     |     |     |
| --------- | ---------- | ---------- | --- | --- | --- | --- | --- |

17
Figure A1. Distributions of heterogeneous treatment effects for each warning using the control as
the baseline
(a) Full
(b) LessthanMin
(c) PercentofFull
Notes: Histogramsofthecausalrandomforests. Panels(a),(b)and(c)indicatethedependentvariable. The
baselineisthecontrolgroupforallthegraphs.

18
Figure A2. Distributions of heterogeneous treatment effects between warning conditions
(a) Full
(b) LessthanMin
(c) PercentofFull
Notes: Histogramsofthecausalrandomforests. Panels(a),(b)and(c)indicatethedependentvariable. The
baselineisthesecondgroupafter“vs.”ineachgraph.