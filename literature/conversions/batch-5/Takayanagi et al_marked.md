---
conversion_metadata:
  converted_at: "2026-07-21T08:55:20Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Takayanagi et al.pdf"
  source_pdf_sha256: "330030e7198ecd3e286766a221afcb05c60b85693a2944d8f3176e526323e927"
  page_count: 10
  markdown_char_count: 132874
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Are Generative AI Agents Effective Personalized Financial
Advisors?
Kiyoshi Izumi
izumi@sys.t.u-tokyo.ac.jp
The University of Tokyo
Tokyo, Japan

Takehiro Takayanagi
takayanagi-takehiro590@g.ecc.u-
tokyo.ac.jp
The University of Tokyo
Tokyo, Japan

Javier Sanz-Cruzado
javier.sanz-
cruzadopuig@glasgow.ac.uk
University of Glasgow
Glasgow, United Kingdom

Richard McCreadie
richard.mccreadie@glasgow.ac.uk
University of Glasgow
Glasgow, United Kingdom

Iadh Ounis
iadh.ounis@glasgow.ac.uk
University of Glasgow
Glasgow, United Kingdom

Abstract
Large language model-based agents are becoming increasingly pop-
ular as a low-cost mechanism to provide personalized, conversa-
tional advice, and have demonstrated impressive capabilities in
relatively simple scenarios, such as movie recommendations. But
how do these agents perform in complex high-stakes domains,
where domain expertise is essential and mistakes carry substantial
risk? This paper investigates the effectiveness of LLM-advisors in
the finance domain, focusing on three distinct challenges: (1) elic-
iting user preferences when users themselves may be unsure of
their needs, (2) providing personalized guidance for diverse invest-
ment preferences, and (3) leveraging advisor personality to build
relationships and foster trust. Via a lab-based user study with 64 par-
ticipants, we show that LLM-advisors often match human advisor
performance when eliciting preferences, although they can strug-
gle to resolve conflicting user needs. When providing personalized
advice, the LLM was able to positively influence user behavior, but
demonstrated clear failure modes. Our results show that accurate
preference elicitation is key, otherwise, the LLM-advisor has little
impact, or can even direct the investor toward unsuitable assets.
More worryingly, users appear insensitive to the quality of advice
being given, or worse these can have an inverse relationship. In-
deed, users reported a preference for and increased satisfaction as
well as emotional trust with LLMs adopting an extroverted persona,
even though those agents provided worse advice.

CCS Concepts
• Information systems → Decision support systems; Person-
alization.

Keywords
large language models, financial advisor, user study, generative AI

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 Interna-
tional License.
SIGIR ’25, Padua, Italy
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1592-1/2025/07
https://doi.org/10.1145/3726302.3729897

ACM Reference Format:
Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard Mc-
Creadie, and Iadh Ounis. 2025. Are Generative AI Agents Effective Personal-
ized Financial Advisors?. In Proceedings of the 48th International ACM SIGIR
Conference on Research and Development in Information Retrieval (SIGIR
’25), July 13–18, 2025, Padua, Italy. ACM, New York, NY, USA, 10 pages.
https://doi.org/10.1145/3726302.3729897

1 Introduction
Personalized advice plays a crucial role in our society, particularly
in complex and high-stakes domains like healthcare and finance.
Advisors and professionals in these fields use their expertise to offer
personalized guidance and emotional support to their clients, lever-
aging people’s specific preferences and/or circumstances. However,
advisory services are often provided at a high cost, effectively ex-
cluding a large portion of the population from this critical advice.
In the financial domain, to mitigate this issue, automated decision
support systems have been widely studied, with a special focus on
investment-related predictions, such as financial asset recommen-
dations [27, 32, 33].

Recent advances in natural language processing and large lan-
guage models (LLMs) have significantly accelerated the develop-
ment of conversational agents, presenting the potential to function
as personalized assistants for information-seeking and decision-
making [40]. These agents can now leverage multi-turn dialogues,
enabling dynamic, mixed-initiative interactions where both users
and systems can take the lead in conversations [1]. This progres-
sion has expanded the application of conversational agents to
various tasks, such as recommendation, question answering, and
search [10, 24, 31, 40].

The application of these conversational agents for financial
decision-making represents a much more complex scenario than
others like movie recommendations, because users are not nec-
essarily familiar with the basic terminology and concepts in this
space, and mistakes carry a substantial risk that can lead to large
monetary losses. While there is a growing interest in building
these conversational assistants to provide automated financial ad-
vice [18], previous work has mostly targeted agents capable of
handling simple inquiries [16, 35, 36]. Compared to these simple
systems, helping users navigate financial decisions and market
uncertainties poses a much greater challenge. Therefore, it is not

---

<!-- PAGE 2 -->

SIGIR ’25, July 13–18, 2025, Padua, Italy

Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard McCreadie, & Iadh Ounis

the second stage, given an individual asset, the advisor provides in-
formation about it to the investor, including how the asset matches
(or not) the investor’s preferences. To answer the different ques-
tions, we compare different configurations of the LLM-advisor: first,
we compare personalized vs. non-personalized advisors, and, then,
we compare two personalized advisors with distinct personalities.

2 Related Work
2.1 Personalization and Preference Elicitation
Information systems, especially those focused on search and rec-
ommendation benefit from personalization [14]. Specifically, per-
sonalization techniques play a crucial role in enhancing user ex-
perience [17, 22, 41]. Interactive approaches, such as conversa-
tional preference elicitation represent the frontier of personaliza-
tion. This problem has received growing attention, as advances
in generative AI now provide a functional mechanism to collect
user preferences dynamically in a free-form manner [40]. This in-
teractive approach can capture more diverse and targeted insights
than static approaches like questionnaires [6, 10, 23, 24, 31]. In-
deed, recent studies have proposed various methods for effective
conversational preference elicitation [31, 42], as well as user stud-
ies on the perceived quality of this process in domains such as
e-commerce, movies, fashion, books, travel, and restaurant recom-
mendations [2, 7, 15, 23, 31, 45].

However, we argue that for some important domains, trying to
directly collect preferences is insufficient. An implicit assumption
of these studies is that if directly asked, the user will be able to
accurately express their preferences. It is reasonable to expect that
this assumption would hold for scenarios like movie recommenda-
tion; we can ask a user “do you like horror movies?” and expect a
useful response. On the other hand, this will not hold for complex
tasks, where the user lacks the knowledge to form an accurate re-
sponse [10, 39]. For instance, in an investment context if we asked
“do you prefer ETFs or Bonds?”, it is not clear that an inexperienced
user would be able to produce a meaningful answer. In these cases,
an ideal agent needs to fill the gaps in the user knowledge through
conversation, as well as infer the user preferences across multiple
(often uncertain) user responses. But how effective are generative
AI agents at this complex task? This paper aims to answer that ques-
tion for the domain of financial advisory; a particularly challenging
domain given its technical nature and high risks if done poorly.

2.2 Financial advisory
In the financial domain, advisors help individuals manage their
personal finances by offering guidance on investments and assist-
ing with decision-making [34]. While financial advisors can be
beneficial, their services often come at a high cost, making them
unaffordable for many people. To mitigate this issue, automated
(non-conversational) financial decision support systems such as
financial recommender systems have been widely studied [44]. The
majority of research in this area has been focused on how to find
profitable assets (i.e. those that will make money if we invest in
them). These works assume a simplified user-model, where an in-
vestor is only concerned with maximizing return-on-investment
over a fixed period of time [27, 32, 33]. These studies frame financial
advisory as a ranking problem, where the goal is to rank financial

Figure 1: Conceptual illustration of an LLM-advisor with two
stages: (1) Preference Elicitation and (2) Advisory Discussion.

yet clear how to develop systems that effectively support complex
financial information-seeking and decision-making tasks.

This work aims to close this gap by exploring the effectiveness
of LLMs to act as personalized financial advisory agents. In partic-
ular, we focus on three problems: (a) eliciting investor preferences
through interactive conversations, (b) providing personalized guid-
ance to help users determine whether particular financial assets
align with their preferences, and (c) leveraging the personality of
the advisor to foster trust on the advisor.

First, the financial literature emphasizes that eliciting user pref-
erences is central to delivering suitable advice [30]. However, it
remains unclear whether current conversational technologies, par-
ticularly those powered by LLMs, can correctly elicit user prefer-
ences in specialized domains where users struggle to articulate
their needs. Our work addresses this challenge in the context of
financial services.

Second, although personalization is widely regarded as impor-
tant in the financial decision-support literature [27, 32, 33], its value
in a conversational setting remains uncertain. In particular, we ex-
plore whether tailoring dialogue around a user’s profile and context
improves financial decision-making. Additionally, we also explore
how personalization influences user perceptions of the advisor, in
terms of aspects like trust and satisfaction.

Finally, in personalized advisory settings within high-stakes
domains, the relationship and trust between the client and advisor
play a crucial role [18]. Research on conversational agents suggests
that agent personality significantly affects users’ perceptions of
the system [3, 29]. However, it remains unclear how an advisor’s
personality in the financial domain influences both the quality of
users’ financial decisions and their overall experience.

To summarize, in this paper, we explore the following questions:
• RQ1: Can LLM-advisors effectively elicit user preferences

through conversation?

• RQ2: Does personalization lead to better investment deci-

sions and a more positive advisor assessment?

• RQ3: Do different personality traits affect decision quality

and advisor assessment?

To address these questions, we conduct a lab-based user study
that explores the effectiveness of LLMs as interactive conversational
financial advisors, on which we simulate realistic investment sce-
narios using investor narratives and stock relevance scores curated
by financial experts. Figure 1 illustrates an example conversation
with the advisor, divided into two stages: first, the LLM-advisor at-
tempts to capture the investor preferences through conversation; in

---

<!-- PAGE 3 -->

Are Generative AI Agents Effective Personalized Financial Advisors?

SIGIR ’25, July 13–18, 2025, Padua, Italy

Figure 2: Example of an investor profile, investment preferences, and ground truth ranking. Dashed line components are used
for evaluation (and therefore, they are not shown to the user/LLM).

assets for a user over a specified time period. However, a recent
study suggests that a large part of the value offered by human fi-
nancial advisors stems from their ability to personalize investment
guidance to clients’ specific needs, build relationships, and foster
trust [13], rather than simply presenting suitable assets.

Reflecting on these findings, the development of conversational
financial advisors has drawn increasing attention, as it enables a
dynamic understanding of users’ needs, personalized guidance, and
the potential to build trustworthy relationships [9, 16, 34, 43]. In par-
ticular, the conversational agents’ personality has gained attention
as a factor that can help build relationships with clients and foster
trust [18], especially given the successes of conversational agents
using the Big Five personality model [20] to enhance the end-user
experience [4, 30]. Although conversational agents show potential
in finance, how to configure them to match the value of human
advisors remains unclear. Therefore, we conduct a user study to
examine how personalizing investment guidance and the advisor’s
personality shape users’ financial decision-making effectiveness
and overall user experience.

3 Methodology
In this paper we aim to determine to what extent current generative
language models can act as an effective financial advisor. Indeed,
given the need to personalize for the user, emotional implications,
the technical nature of the information-seeking task, and high
impact if failed, we argue that this is an excellent test case for
the limits of generative large language models. To structure our
evaluation, we divide our study into two phases, as illustrated in
Figure 1, where we evaluate the success of both:

(1) Preference Elicitation: During this stage, we have the LLM-
advisor hold a natural language conversation with a human,
where it is directed to collect information regarding the per-
son’s investment preferences. The human in this interaction
is pretending to have preferences from a given investor pro-
file.

(2) Advisory Discussion: During the advisory discussion, the
LLM-advisor again has a natural language conversation with
the human (acting on an investor profile), where the human
collects information about whether a company is a suitable
investment for them. This is repeated for multiple companies
per investor profile.

We provide preparatory information and discuss each stage in more
detail below:

3.1 Investor Profiles
To fairly evaluate the ability of any LLM-advisor, we need to have
them interact with human users with real needs. Given the open-
ended nature of free-form conversations, it is desirable to repeat
each experiment with different people such that we can observe
variances in conversation paths, as those variances may influence
task success. However, to enable repeatability, we need to hold the
investor needs constant across repetitions. Hence, we define three
archetypal investor profiles 𝑖 ∈ 𝐼 based on input from a financial
expert, where our human participants are given one to follow when
conversing with the LLM-advisor:

• Investor 1: Growth-Oriented Healthcare Enthusiast:
Prefers healthcare innovations, values high-growth opportu-
nities, and takes measured risks.

• Investor 2: Conservative Income Seeker: Seeks stable
returns, invests in well-established companies, values regular
dividend payouts.

• Investor 3: Risk-taking Value Investor: Targets under-
valued companies with strong long-term potential, tolerates
short-term volatility, and invests in cyclical sectors.

For each of these investor profiles, we select three key investment
preferences, chosen from well-known investment characteristics
such as industry sector, stock style, consistency in dividend pay-
ments, and sensitivity to global market changes [8]. We denote
the set of investor preferences as 𝑖𝑝𝑟𝑒 𝑓 . In our experiments, we
simulate a realistic elicitation scenario where the advisor collects
the preferences from the participants. Therefore, we do not straight-
forwardly provide the preferences to the participants. Instead, we
present them as text narratives of between 150 to 200 words. A
financial expert was consulted to confirm the quality and reliability
of these narratives. An example narrative representing Investor 2 is
illustrated in Figure 2, where we highlight the sentences referring
to specific investor preferences.

3.2 Stage 1: Preference Elicitation
The goal of stage 1 of our study is to determine to what extent an
LLM-advisor can effectively collect a user’s investment preferences
through conversation. Formally, given a participant of the user
study 𝑢 and an investor profile 𝑖, during the elicitation stage, the
LLM-advisor aims to obtain an approximated set of preferences,
, that matches the investor preferences (𝑖𝑝𝑟𝑒 𝑓 ). To
denoted 𝑖𝐿𝐿𝑀
achieve this, the generative model produces a series of questions
that participants answer by interpreting the investor narrative.

𝑢

---

<!-- PAGE 4 -->

SIGIR ’25, July 13–18, 2025, Padua, Italy

Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard McCreadie, & Iadh Ounis

Responses to those questions, denoted as 𝑅𝑢
advisor to generate the user profile 𝑖𝐿𝐿𝑀
by manually evaluating the overlap between 𝑖𝑝𝑟𝑒 𝑓 and 𝑖𝐿𝐿𝑀

𝑖 , are used by the LLM-
. Success is then measured

𝑢

.

𝑢

For user elicitation, we adopted a System-Ask-User-Respond
(SAUR) paradigm [42]. During the conversation, the advisor proac-
tively inquires about the user’s preferences given a set of target
preferences (e.g., industry type, acceptable risk). After the human
participant responds to a question, the LLM-advisor checks whether
the collected preferences cover all of the target preferences. If the ad-
visor is confident that they do, it ends the conversation and prompts
the user to proceed to the next stage; otherwise, it continues asking
follow-up questions in a loop.

3.3 Stage 2: Advisory Discussion
Stage 2 of our study investigates to what extent an LLM-advisor can
provide the same benefits as a real human advisor when exploring
investment options. Note that the goal here is not to have the LLM-
advisor promote any one asset, but rather to provide accurate and
meaningful information such that the human can find the best
investment opportunity for them. To this end, we structure our
experiment such that the human (acting on an investor profile) has
one conversation with the LLM-advisor for each of a set of assets
being considered.1 After all assets are presented to the participant,
a stock ranking is generated by sorting the stocks by the participant
rating in descending order.

Importantly, as we know the investor profile 𝑖𝑝𝑟𝑒 𝑓 for each con-
versation about an asset 𝑎, we can objectively determine whether 𝑎
is a good investment given 𝑖𝑝𝑟𝑒 𝑓 , forming a ground truth against
which we can compare to the rating provided by our human par-
ticipant after their conversation with the LLM-advisor. For each
asset 𝑎, a financial expert produced a score between 0 and 3 by
manually checking whether 𝑎 satisfied each of the three investment
criteria contained in 𝑖𝑝𝑟𝑒 𝑓 . A ground-truth ranking was produced
by sorting the assets by the expert scores. We show an example
of the ranking construction in Figure 2. During evaluation, the
closer the participant ranking is to the ranking produced by expert
judgments, the better the LLM-advisor performed.

Baseline Prompt: As we are working with an LLM-advisor and
the nature of financial information-seeking is time-sensitive, we
need to provide any information that might change over time to the
LLM within the prompt. As such, for each asset 𝑎, we pre-prepared
a standard asset descriptor block after consulting with a financial
expert, containing:

• Stock Prices: We collect monthly stock prices from 2023

using Yahoo! Finance.2

• Business Summary: We gather each company’s business

overview from Yahoo! Finance.

• Recent Performance and Key Financial Indicators (e.g.,
EPS): We obtain earnings conference call transcripts3 from
Seeking Alpha for the last quarter of 2023.

1These were manually selected, however in a production environment these might be
produced by an asset recommendation system.
2The scenario for the financial advising of our user study is set to December 30,
2023. By basing our experiment at the end of 2023, we avoid the problem of data
contamination [25].
3Earnings conference calls, hosted by publicly traded companies, discuss key aspects
of their earnings reports and future goals with financial analysts and investors, thus
covering critical financial indicators and recent performance insights [21]. These

Figure 3: User study structure.

The advisor using this prompt acts as our baseline for the advisory
discussion study. We augment this baseline with additional context
and instructions to form two additional experimental scenarios,
discussed below:

+Personalization: As discussed earlier, one of the core roles of the
financial advisor is to personalize to the individual customer, based
on their financial situation, needs, and preferences. To enable the
LLM-advisor to personalize for the user, we integrate the gener-
ated profile from the preference elicitation (Stage 1) 𝑖𝐿𝐿𝑀
into the
prompt. We represent each preference as a series of short sentences.

𝑢

+Personality: In Section 2.2 we discussed how human financial
advisors provide emotional support as well as financial advice.
While it is unlikely that an LLM-advisor could do this as well as a
human (it lacks both emotional intelligence and non-conversational
clues to the customer’s mental state [38]), it might be possible to
provide a better end-user experience by directing the LLM-advisor
to adopt a personality. As noted in Section 2 it is possible to do this
via prompt engineering, such as instructing the LLM to take on the
traits of one or more of the Big-Five personality types [20].

As we are performing a user study with humans, it would be
impractical to exhaustively test every combination of personality
types, hence as an initial investigation we experiment with two
distinct personality profiles [29]:

• Extroverted: High in extroversion, agreeableness, and open-

ness; low in conscientiousness and neuroticism.

• Conscientious: Low in extroversion, agreeableness, and

openness; high in conscientiousness and neuroticism.

We adopted the prompting method from Jiang et al. (2024) to
assign a Big Five personality trait to the LLM agent [12], choos-
ing it for its simplicity and effectiveness among various proposed
approaches for embedding personality in LLMs (including both
prompting and fine-tuning) [11, 12, 28]. To ensure a high standard
of professionalism and accurate representation of the intended per-
sonality, we consulted financial professionals to review the texts
generated by LLMs adopting both personas.

transcripts cover significant financial indicators and provide explanations of recent
performance.

---

<!-- PAGE 5 -->

Are Generative AI Agents Effective Personalized Financial Advisors?

SIGIR ’25, July 13–18, 2025, Padua, Italy

3.4 Experimental Design
In our experiment, we conducted two studies: a personalization
study (for RQ2) and an advisor persona study (for RQ3). In the
personalization study, participants compared a non-personalized
(Baseline) advisor with a personalized (+Personalized) version. In
the advisor persona study, they compared different LLM-advisor
personality types (+Extroverted vs. +Conscientious). Participants
are randomly assigned to one of these two studies.

Figure 3 shows the structure of our user study for a single par-

ticipant, comprising seven steps:

(1) Participant Training: Participants are given a general overview
of the user study and given instructions on their expected
roles during preference elicitation, advisory discussions, as-
set ranking, and advisor assessment.

(2) Investor Profile Allocation: The user 𝑢 is randomly allo-
cated one of the investor profiles (See Section 3.1) that they
will follow. Each profile is assigned to 42 participants.
(3) Preference Elicitation (Stage 1): The participant interacts
with the LLM-advisor as if they were a new investor. The
conversation ends once the LLM-advisor determines that
they know enough about the investor to personalize for
them. The median time spent on preference elicitation was
5 minutes and 11 seconds.

𝑢

𝑢

. Otherwise, 𝑖𝐿𝐿𝑀

(4) Response Summarization: Given the aggregator of user
responses 𝑅𝑢
𝑖 , we instruct an LLM to generate an investor
. For each investor preference in 𝑖𝑝𝑟𝑒 𝑓 , if there is
profile 𝑖𝐿𝐿𝑀
𝑢
any relevant information in the responses 𝑅𝑢
𝑖 , that informa-
tion is included in 𝑖𝐿𝐿𝑀
indicates that no
relevant information is available for that specific preference.
(5) Advisory Discussion (Stage 2): To simplify the conversa-
tion flow we have the participant hold separate conversations
with the LLM-advisor for each asset they might invest in.
The LLM-advisor is provided with context about the current
asset (see Section 3.3), and depending on the experimen-
tal scenario, optionally personalization information (step 4
output) and/or a target personality context statement. Each
conversation continues until the user is satisfied that they
have enough information to rate the asset. The order in
which the assets are discussed is randomly assigned to avoid
position bias.

(6) Asset Ranking and Feedback: Participants rank all the
stocks (four in total) discussed in the advisory session ac-
cording to their desire to invest in each. They also assess the
advisor they interacted with using a 7-point Likert scale for
the items listed in Table 1 (see Section 4).

To enable more effective pair-wise comparison of LLM-advisor vari-
ants, we have each participant test two variants per study. If the
user has only tested one variant at this point, then they repeat the
user study (starting at step 2) with the second variant. The order in
which participants experience each variant is randomly assigned.

Table 1: Operational definitions used in the advisor assess-
ment questionnaire for all response dimensions.

Response Dimension

Operational Definition

Perceived Personalization [14]

The advisor understands my needs.

Emotional Trust [14]

I feel content about relying on this advisor for my decisions.

Trust in Competence [14]

The advisor has good knowledge of the stock.

Intention to Use [14]

I am willing to use this advisor as an aid to help with my
decision about which stock to purchase.

Perceived Usefulness [22]

The advisor gave me good suggestions.

Overall Satisfaction [22]

Overall, I am satisfied with the advisor.

Information Provision [37]

The advisor provides the financial knowledge needed.

In our experiments, we use Llama-3.1 8B as the background

model for all our LLM-advisor variants.4

3.5 Participants
We recruited 64 participants from the authors’ affiliated university
for our study: 32 participants for the personalization study and 32
participants for the advisor persona study, utilizing the university’s
online platform and blackboard for recruitment. Participants were
required to be fluent in English, over 18 years old, and have an in-
terest in finance and investment, mirroring the target demographic
of our system’s users. After excluding invalid data, 29 participants
remained in the personalization study and 31 in the advisor persona
study. We conducted a power analysis using the Wilcoxon signed-
rank test for matched pairs, with the experimental conditions as
the independent variable and users’ response to the advisor assess-
ment questionnaire as the dependent variable [26]. The analysis
determined that 29 participants are needed to observe a statistically
significant effect on user-perceived quality. Our recruitment cri-
teria and compensation (£10/hour) for approximately one hour of
participation were approved by our organization’s ethical board.

4 Evaluation Metrics and Statistics
In this section we discuss how we quantify effectiveness for the
preference elicitation and advisory discussion stages, respectively,
in addition to summarizing dataset statistics for each.

4.1 Preference Elicitation Metrics (Stage 1)
To evaluate the quality of the first preference elicitation stage,
we want to measure how well the LLM-advisor has captured the
investor preferences as defined in the investor profile 𝑖 (see Sec-
tion 3.1). Each investor profile 𝑖 ∈ 𝐼 defines key features of the
investor, such as preferring high-growth stocks, or favoring regu-
lar payouts, denoted 𝑖𝑝𝑟𝑒 𝑓 . We have three investor profiles (|𝐼 |=3),
with 10 (𝑛) participants performing elicitation on 𝑖𝐿𝐿𝑀
for each
profile and each LLM variant, i.e. there are 120 elicitation attempts
in total, with 30 attempts per LLM-advisor variant. Following the
notation in Section 3, 𝑖𝐿𝐿𝑀
in this case denotes a similar list of fea-
tures to 𝑖𝑝𝑟𝑒 𝑓 that LLM-advisor learned about the investor during
conversation with a participant 𝑢, which we derive from a manual
analysis of the elicitation output (i.e. what is produced by response
summarization). Intuitively, the closer the features produced from

𝑢

𝑢

(7) Exit Questionnaire: Once a pair of LLM-advisor variants
have been tested, the user fills in an exit questionnaire that
is designed to ask the overall experience in the user study.

4Further details about the LLM configuration, investor narratives, relevant scores,
prompts and scripts for data analysis can be accessed at the following repository:
https://github.com/TTsamurai/LLMAdvisor_supplementary

---

<!-- PAGE 6 -->

SIGIR ’25, July 13–18, 2025, Padua, Italy

Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard McCreadie, & Iadh Ounis

Table 2: General statistics of the collected conversation data.

Participants
Time Period
Total Turns

60
2024/10/24 ~ 2024/11/7
10,008

Stage 1: Preference Elicitation

Total Turns
Number of Sessions
Avg. Turns/Session
Avg. User Words/Turn

Stage 2: Advisory Discussion

1,788
120
15.8
9.8

Total Turns
Number of Sessions
Avg. Turns/Session
Avg. User Words/Turn
is to 𝑖𝑝𝑟𝑒 𝑓 , the better the LLM-advisor
any elicitation attempt 𝑖𝐿𝐿𝑀
is performing. To this end, we report elicitation accuracy for each
investor profile, calculated as:

8,220
480
18.2
13.0

𝑢

ElicitationAccuracy(𝑖) =

1
𝑛

𝑛
∑︁

𝑗=1

(cid:12)
𝑖𝐿𝐿𝑀
(cid:12)
𝑗
(cid:12)

∩ 𝑖𝑝𝑟𝑒 𝑓 (cid:12)
(cid:12)
(cid:12)

(cid:12)𝑖𝑝𝑟𝑒 𝑓 (cid:12)
(cid:12)
(cid:12)

(1)

Human Advisor: To provide a point of comparison, we also con-
duct a preference elicitation with a financial expert using the same
prompt and instructions as the LLM. This allows us to evaluate
how close LLMs are to a paid human advisor undertaking the same
task. More specifically, for each investor profile, three participants
engaged with this expert, who then produced a set of preferences
𝑖𝐸𝑥𝑝𝑒𝑟𝑡
𝑢

, which can be used instead of 𝑖𝐿𝐿𝑀

in Equation 1.

𝑢

4.2 Advisory Effectiveness Metrics (Stage 2)
Ranking correlation (Spearman’s Rho): In the second stage,
we evaluate how well the LLM-advisor can support an investor to
select financial assets that are suitable for them to invest in. Recall
from Figure 3 that after a participant finishes discussing all assets
with the LLM-advisor, they rank those assets 𝑎 ∈ 𝐴𝑖 based on the
likelihood they will invest in each, i.e. each participant 𝑢 acting
on a profile 𝑖 we have an asset ranking 𝑅(𝐴𝑖, 𝑖𝑢 ). As illustrated in
Figure 2, each investor profile 𝑖 was derived from a ground truth
set of investor preferences 𝑖𝑝𝑟𝑒 𝑓 , which an expert used to create
a ground truth ranking 𝑅(𝐴𝑖, 𝑖𝑝𝑟𝑒 𝑓 ), i.e. the “correct” ranking of
assets. Intuitively the closer the 𝑅(𝐴𝑖, 𝑖𝑢 ) is to 𝑅(𝐴𝑖, 𝑖𝑝𝑟𝑒 𝑓 ), the bet-
ter the advisor is performing, as the participant was better able to
distinguish suitable assets vs. unsuitable ones. Hence, to evaluate
the effectiveness of the advisory task, we report the mean ranking
correlation (Spearman’s Rho) between 𝑅(𝐴𝑖, 𝑖𝑢 ) and 𝑅(𝐴𝑖, 𝑖𝑝𝑟𝑒 𝑓 )
across participants 𝑢 for each LLM-advisor.

Advisor Assessment Questionnaire: Lastly, we also gather qual-
itative data from each participant via a questionnaire. In particular,
after ranking assets each participant, reports how they feel the
LLM-advisor performed in terms of 7 dimensions, listed in Table 1,
such as perceived usefulness, trust, and user satisfaction. We use
this data later to evaluate how sensitive the user is to differences in
the LLM-advisor.

4.3 Dataset Statistics
Table 2 summarizes the statistics of the data collected during the
two stages of our user study. Each conversation that a participant
had with an LLM-advisor in either stage 1 or 2 is referred to as

Table 3: Stage 1 - Comparison of Elicitation Accuracy of an
expert vs. different LLM-advisors for each investor profile.
The best advisor is highlighted in bold. Arrows denote per-
centage increases (↑) or decreases (↓) compared to the expert.

Investor Profile

Expert

LLM-Advisors

LLM +Extr.

+Cons.

Growth-Oriented
Conservative-Income
Risk-Taking

Average

0.78
0.89
0.89

0.85

0.76
0.82
0.48

0.69

0.80
0.75
0.60

0.70

0.79
0.87
0.55

0.73

Average
0.78→0.0%
0.82↓7.8%
0.53↓40.5%
0.70↓17.6%

a session, e.g. during Stage 1, there were 3 investor profiles * 10
participants * 4 LLM-advisors, resulting in 120 sessions. Stage 2 has
4x the number of sessions, as there are four assets associated with
each profile (𝐴𝑖 ) to discuss with the LLM-advisor.

From Table 2 we observe that in contrast to other conversational
tasks [35, 36], financial information-seeking appears to require
more extended interactions. On average, preference elicitation in-
volves 15 turns per session with 9.8 words per turn, whereas advi-
sory discussions involve 18 turns per session with 13.0 words per
turn, highlighting the overall complexity of the task.

5 Results
In this work, we explore how to design conversational financial advi-
sors that enhance both decision-making and positive experience. To
achieve this, our user study is guided by 3 core research questions.
• RQ1: Can LLM-advisors effectively elicit user preferences

through conversation?

• RQ2: Does personalization lead to better decisions and more

positive advisor assessment?

• RQ3: Do different personality traits affect decision quality

and advisor assessment?

5.1 RQ1: Elicitation accuracy
We begin by examining how effective the LLM-advisors are at iden-
tifying investment preferences during conversations in Stage 1.
Elicitation Accuracy is the primary metric, where we contrast the
mean accuracy across 10 sessions in comparison to a human expert
tackling the same task (see Section 4.1). Table 3 reports elicitation
accuracy for each LLM-advisor and the Human Expert across invest-
ment profiles. Arrows denote percentage increases (↑) or decreases
(↓) of the LLM-advisor compared to the expert.

To set expectations, we first consider the performance of the
expert in the first column in Table 3, as we might expect, the ex-
pert maintains consistently high performance across all profiles,
averaging 85% accuracy (random accuracy is 50%). This forms an
expectation of the performance ceiling for the task.

Next, we compare the expert performance to each LLM-advisor.
From the perspective of preference elicitation, there are three LLM-
advisor configurations, those that use only the Baseline Prompt (de-
noted LLM) from the personalization study, and those that include
a defined personality (either extroverted, +Extr., or conscientious,
+Cons.) from the advisor persona study.5 From Table 3, we observe

5Note we cannot have a personalized variant here, as the personalization evidence is
derived from this stage.

---

<!-- PAGE 7 -->

Are Generative AI Agents Effective Personalized Financial Advisors?

SIGIR ’25, July 13–18, 2025, Padua, Italy

that the LLM-advisor’s performance is generally strong for growth-
oriented, and conservative-income investors (with accuracy around
80%) on average, which is similar to the human advisor. However,
for the risk-taking investor profile, the LLM-advisor’s elicitation
accuracy was substantially lower (-40.5%).

From a manual failure analysis, we observed the following trends
that contribute to the performance gap with the human advisor,
particularly for the risk-taking profile. First, it is notable that elici-
tation failures can originate from the investor (participant) rather
than the LLM. Recall that one of the aspects that makes finance
more challenging than domains like movie recommendation is that
the “user” is inexpert, and so may give incorrect information during
the conversation. Indeed, we observed cases where the participant
confused concepts such as the difference between a growth and a
value stock, as well as cyclical/non-cyclical assets. On the other side,
preference hallucination is a core issue for the LLM-advisor. The
LLM is a probabilistic token generator conditioned on the baseline
prompt and prior conversation, and as a result, in some scenarios,
the contextual content can override a statement by the investor.
This type of error is more likely when the investor is unsure in
their responses or when they provide contradictory statements.
For instance, an investor expressing an interest in the consumer
discretionary sector while simultaneously opting for non-cyclical
stocks, despite consumer discretionary being inherently cyclical.

To answer RQ1, our results demonstrate that LLM-advisor’s are
able to elicit preferences from a user via conversation and that for
2/3’s of the user profiles tested, elicitation accuracy was consistently
equivalent or close to that of an expert human advisor. However,
we observed a clear failure mode when testing the risk-taking pro-
file, where misunderstandings by the investors and hallucinations
within the LLM compound to result in accuracy that is close to ran-
dom. Overall, we consider this a promising result, as the majority
of the time it is effective, and the failure mode observed might be
rectified by better context crafting and the addition of contradiction
detection; both directions for future research.

5.2 RQ2: Effectiveness of personalization
Having shown that automatic preference elicitation is possible, we
now examine stage 2 of our study, namely the advisory discussions.
Given the inherently personalized nature of financial advice, we
expect that the customer preferences obtained during stage 1 will
be key to enabling LLM-advisors to provide effective investment
advice. Hence, in this section, we compare the performance of an
LLM-advisor using only the Baseline Prompt to one that includes
the preferences obtained during stage 1 (+Personalized). However,
as we observed that preference elicitation is not always successful,
we also examine what effect elicitation performance has on the
LLM-advisor.

5.2.1 Non-personalized Decision-making Effectiveness: We initially
establish how effective the LLM-advisor is without any informa-
tion regarding the investor. LLM-advisor effectiveness is measured
based on how well the investor was able to rank the assets discussed
by suitability to them. The primary metric is average Spearman’s
Rho correlation between the investor ranking and the ground truth
ranking (see Section 4.2), reported in Table 4 row 1. As we expect,

Table 4: Investor decision-making effectiveness, expressed
as the Spearman’s Rho correlation between the investor’s
asset ranking and the expert asset ranking (higher is better).
† indicates statistical improvements (Welch’s t-test with 𝑝 <
0.05) over the not personalized baseline, while § indicates
significant differences between cases with successful and
unsuccessful preference elicitations.

Advisor Config

Investor vs. Expert (Spearman’s Rho)

Personalization

Personality

All

Preference Elicitation

Successful

Unsuccessful

Baseline
+Personalized
+Personalized
+Personalized

None
None
+Extroverted
+Conscientious

0.110
0.310
0.122
0.26

–
0.481†§
0.243§
0.365

–
-0.228
-0.286
-0.025

baseline advisory performance is low, with only a very weak pos-
itive correlation to the ground truth ranking of 0.11. This indicates
that without further evidence, the LLM is not able to meaningfully
guide the investor.

5.2.2 Personalized Decision-making Effectiveness: Having estab-
lished our baseline, we now examine the impact that adding the
investor preferences collected during stage 1 has, comparing Table 4
row 1 (baseline) to row 2 (personalized). As we anticipated, person-
alization is beneficial, with investor decision-making effectiveness
increasing from 0.11 to 0.31 (average Spearman’s Rho correlation
to the expert ranking). However, this correlation is still weak, illus-
trating that while discussing assets with the LLM-advisor is better
than no help at all, our participants are still struggling to evaluate
the suitability of financial assets.

This correlation is an average over all the participants in the user
study, regardless of how effective their preference elicitation was in
stage 1. Hence, we might ask whether the low correlation is due to
the LLM-advisor being confused by poor preference elicitation data.
To explore this, Table 4 also reports investor decision-making effec-
tiveness stratified based on whether stage 1 was successful (column
4) or not (column 5).6As expected, we see a statistically significant
increase in investor decision-making effectiveness when prefer-
ence elicitation was successful when compared to non-personalized
sessions (0.481 vs. 0.110). More concerningly, we also see the LLM-
advisor has a strong negative influence on the investors’ decision-
making capability if preference elicitation fails, as illustrated by
the negative correlations with the expert in column 5. This result
highlights both that effective preference elicitation is crucial, but
also that the LLM-advisor can easily influence the investor into
making poor decisions, as the human is heavily reliant on the agent
to navigate the relatively unfamiliar financial information space.

5.2.3 Participant Assessment of the Advisor: So far we have demon-
strated that there is a large difference between a non-personalized
LLM-advisor and a personalized one, in terms of how they can
alter the decision-making of the investor/participant. But can the
participant tell the differences between them?

Table 5 reports the aggregation of the qualitative data we col-
lected from each participant after they finished interacting with
each LLM-advisor in terms of 7 dimensions, where we start by

6We define that an elicitation session is successful if more than 50% of the investor’s
preferences were correctly captured

---

<!-- PAGE 8 -->

SIGIR ’25, July 13–18, 2025, Padua, Italy

Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard McCreadie, & Iadh Ounis

Table 5: Average participant users’ response to advisor assessment questionnaire under different advisor conditions. Columns
labeled with advisor condition (Baseline, +Pers., +Cons., +Extr.) contain a 7-point Likert scale (higher is better). “p” column
contains Wilcoxon signed-rank test p-values for (RQ2) Baseline vs. +Personalized (Pers.), and (RQ3) +Conscientious (Cons.) vs.
+Extroverted (Extr), for both the full data (All) and the subset where the elicitation accuracy is above 0.5. “Successful Elicitation”
refers to the subset where elicitation accuracy was ≥ 0.5. For RQ2, this subset consists of pairs for which +Pers elicitation is
successful, while for RQ3, it consists of pairs for which both +Extr and +Cons elicitation are successful. Boldface indicates
significant effects with † for 𝑝 < 0.1 and ‡ for 𝑝 < 0.05.

(RQ2) Baseline vs. +Personalized

(RQ3) +Conscientious vs. +Extroverted

All

Successful Elicitation

All

Successful Elicitation

Response Dimension

Baseline

+Pers.

p

Baseline

+Pers.

p

+Cons.

+Extr.

p

+Cons.

+Extr.

p

Perceived Personalization
Emotional Trust
Trust in Competence
Intention to Use
Perceived Usefulness
Overall Satisfaction
Information Provision

5.759
5.103
5.690
5.310
5.241
5.345
5.517

5.724
5.241
5.690
5.483
5.517
5.690
5.966

0.838
0.446
0.817
0.505
0.183
0.116
0.026‡

5.762
5.143
5.810
5.429
5.381
5.429
5.714

5.905
5.333
5.857
5.714
5.810
5.810
6.143

0.751
0.537
0.782
0.166
0.194
0.098†
0.053†

5.500
5.038
5.962
4.885
5.423
5.269
5.692

5.500
5.154
6.077
5.462
5.538
5.577
5.654

0.663
0.600
0.538
0.005‡
0.425
0.179
0.953

5.588
4.706
6.000
4.941
5.176
5.118
5.588

5.706
5.235
6.000
5.588
5.118
5.529
5.765

0.941
0.034‡
1.000
0.013‡
0.968
0.244
0.490

focusing on the RQ2-All columns, i.e. comparing the baseline and
personalized variants. The important observation to note here is
that the participant preference scores for both variants are statis-
tically indistinguishable, except under the quality of information
provision criteria. This means that our participants cannot tell if
the LLM-advisor is personalizing to them, and trust the worse agent
just as much as the better one. Furthermore, if we consider the best
case scenario where the preference elicitation was successful (RQ2
Successful Elicitation columns) we observe the same pattern, even
though the difference between the baseline and the personalized
variants in terms of the effect it has on the participant decision-
making is more pronounced. This underlines one of the core risks
of using LLM-advisors in the financial domain; since our users are
inherently inexpert they lack the fundamental skills to judge to
what extent the LLM is providing good advice, meaning that there
is no safety net if the LLM makes a mistake.

To answer RQ2, our results show that a personalized LLM-advisor
is able to provide useful financial advice when it has accurate in-
formation regarding the preferences of the investor. This is demon-
strated by better decision-making capability by participants using
the personalized advisor in comparison to the non-personalized one.
However, we also identified two important challenges to adoption.
First, the impact the LLM-advisor has is strongly tied to the quality
of the preference elicitation data provided, where poor preference
elicitation will cause the agent to actively direct the investor to the
wrong assets. Second, while the participants were positive regard-
ing the LLM-advisors across all questionnaire criteria, they were
not able to consistently tell the difference between good and bad ad-
visors; leading to an increased risk of humans acting on bad advice.

5.3 RQ3: Effectiveness of personalities
Once we have confirmed the utility of personalization for LLM-
advisors, we now study the effect that the personality of the advisor
has on users’ financial information-seeking. As previous studies
have shown [29], chatbot personality can affect the way humans
interact with the chatbot, and therefore affect the effectiveness and
perception of LLM-advisors. To understand whether personality
affects LLM financial advisors, we compare two personalized LLM-
advisors on which we have injected a pre-defined personality: an

extroverted personality and a conscientious personality. 7 While
we could consider the personalized LLM-advisor discussed in Sec-
tion 5.2 as a third distinct personality (the base LLM personality
of the LLM), we shall not compare it with our personality-injected
models, because different sets of participants were used in the per-
sonalization study and the advisor-persona study.

5.3.1 Decision-making Effectiveness: We first examine the impact
of adding personality to the advisors on the decision-making pro-
cess, by measuring the capacity of the participants to correctly rank
the assets (as previously done in Section 5.2). As a primary metric,
we again use the average Spearman’s Rho correlation between the
investor ranking and the ground truth ranking reported in Table 4
rows 3 (extroverted advisor) and row 4 (conscientious advisor).

We first observe the results for the full set of participants in
the user study. Interestingly, we observe a difference between the
two advisors, with the conscientious LLM-advisor providing better
guidance than the extroverted one (0.26 vs. 0.122). This observation
is consistent when we restrict our analysis to those cases where the
preference elicitation is successful. While, expectedly, the effective-
ness of both advisors improves when the elicitation is successful
(0.243 vs. 0.122 in the case of the extroverted advisor and 0.365 vs.
0.26 in the case of the conscientious one), the conscientious advisor
has an advantage over the extroverted one (0.365 vs. 0.26).

These results highlight that providing different personalities to
an LLM-advisor can notably impact the capacity of the advisor to
provide useful information to the investors.

5.3.2 Participant Assessment of the Advisor: We have observed so
far that the use of different personalities affects the user decision-
making process. But how do these personalities affect the perception
that users have of the LLM-advisor? We observe this in Table 5, in
terms of the seven dimensions captured during the advisor assess-
ment questionnaire.

We first look at the RQ3-All columns, comparing the two per-
sonalities. Notably, for the majority of the dimensions, users barely
distinguish between both systems. The only answer where we ob-
serve a statistically significant difference is the intention to use the

7Refer to Section 3.3 for a full description of each personality.

---

<!-- PAGE 9 -->

Are Generative AI Agents Effective Personalized Financial Advisors?

SIGIR ’25, July 13–18, 2025, Padua, Italy

system in the future. Surprisingly, despite providing worse guid-
ance to the investor, participants expressed a higher interest in
using the extroverted advisor than the conscientious one. When we
limit our study to those participants who experienced a successful
preference elicitation in both advisor variants, this issue is stressed,
as those users also develop a significantly greater emotional trust
with the extroverted advisor.

These observations are worrisome, as they reveal that the per-
sonality of a financial advisor cannot only affect the quality of the
advice but also lead the investors to trust more on those systems
providing worse advice.

5.3.3 Differences in language: To further understand how person-
alities affect financial advisory, we analyze the differences in the
linguistic patterns provided by extroverted and conscientious ad-
visors. Analyzing participants’ reported overall experience from
the exit questionnaires in the advisor persona study, over 20% (7
of 31) described the extroverted advisor as clear, assertive, and
cheerful while perceiving the conscientious advisor as straight-
forward, analytical, yet less confident.8 Therefore, to quantify the
linguistic differences in the advisors, we conduct a financial sen-
timent analysis of the utterances generated by each advisor. For
each utterance, we count the occurrences of positive, negative, and
uncertain words from the Loughran and McDonald Financial Senti-
ment Dictionary [19]. We normalize these counts by the length of
the sentences and average the results across all dialogues.

Figure 4 shows the results, showing the extroverted sentiment
scores in blue, and the conscientious scores in orange. For the three
sentiment dimensions, differences between advisors are statisti-
cally significant (Welch’s t-test with 𝑝 < 0.01). Figure 4 shows
that extroverted advisors tend to use more positive language in
their interactions, while conscientious advisors prefer negative
and uncertain tones. Through manual analysis of the conversation,
we observe that this results in the extroverted advisor focusing
on the positive aspects of investments while overlooking serious
drawbacks, whereas the conscientious advisor provides a more bal-
anced view of the assets. Because of this, participants guided by
conscientious advisors may make more well-informed financial de-
cisions. Meanwhile, the positivity of the extroverted advisor seems
more appreciated by the users, which is reflected in higher advisor
assessment scores from the post-discussion questionnaire.

To answer RQ3, our results show that different personalities of
a personalized LLM-advisor can affect the utility of the provided
advice. This is demonstrated by the better decisions of the study
participants when using an advisor with a conscientious person-
ality than when using an advisor with an extroverted personality.
Moreover, the personality of the advisor affects the perception of
humans towards the system, and it has the risk of leading investors
to further trust those systems that provide worse advice.

6 Conclusion
In this paper, we have conducted a lab-based user study to examine
how effective large language models are as financial advisors. We
focus on three core challenges: preference elicitation, investment
personalization, and advisor personality.

8Participants were unaware of the specific personas during the study.

Figure 4: Average sentiment scores by advisor personality.
Error bars indicate the standard deviation.

First, our analysis shows that LLMs are effective tools for prefer-
ence elicitation through conversation. In a majority of cases, they
are capable of obtaining investor’s preferences with an accuracy
close to or equivalent to that of an expert human advisor. How-
ever, there are some clear failure cases, as LLMs are vulnerable to
contradictory statements and hallucinations, which, in the case of
complex investor profiles, can decrease the accuracy of the elicita-
tion to random levels. Although LLMs are promising for elicitation,
in a complex domain like finance, investors do not always fully un-
derstand their own preferences (or they have difficulties expressing
them). Therefore, future work should explore the development of
LLM-advisors capable of resolving conflicting user needs.

Second, personalizing LLMs to provide investment advice can
improve the decisions made by the investors, but only when the
personalized LLM-advisor receives accurate information about the
investor’s preferences. If the preference elicitation is not successful,
the agent actively directs the investors to the wrong assets on which
to invest. This underscores how crucial a good preference elicitation
is for providing useful financial advice.

Finally, our results suggest that investors are not necessarily
aware of what constitutes good financial advice, and therefore,
are vulnerable to acting on bad advice provided by LLMs. In the
comparison between a non-personalized and a personalized LLM-
advisor, although the personalized system led to better decisions,
participants were unable to distinguish between the systems. More
worryingly, when comparing two personalized advisors with ex-
troverted and conscientious personalities, we observed that, even
though the extroverted advisor provided lower-quality advice, par-
ticipants trusted this advisor more than the conscientious one.

Our findings highlight that, while personalized LLM-advisors
represent a promising research direction, their use in high-stakes
domains like finance is not free of risks: due to the limitations of
LLMs at capturing complex investment preferences, and the diffi-
culty of investors to discern whether the advice they receive truly
serves their interests, LLMs have a notable risk to drive investors
to bad financial assets (leading not only to a low satisfaction but
also to potentially large monetary losses). However, these draw-
backs open interesting research directions not only from a system
perspective, but also from a human-centered approach: automated
advisory development where we do not just focus on improving the
quality of automated systems to guide investors, but also on how
the investors will adopt, trust and interact with these AI agents [5].

Acknowledgments
This work was supported by Daiwa Securities Group Inc.

---

<!-- PAGE 10 -->

SIGIR ’25, July 13–18, 2025, Padua, Italy

Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard McCreadie, & Iadh Ounis

References
[1] James E. Allen, Curry I. Guinn, and Eric Horvtz. 1999. Mixed-initiative interaction.

IEEE Intelligent Systems and their Applications 14, 5 (1999), 14–23.

[2] Ashay Argal, Siddharth Gupta, Ajay Modi, Pratik Pandey, Simon Shim, and Chang
Choo. 2018. Intelligent travel chatbot for predictive recommendation in echo
platform. In 2018 IEEE 8th Annual Computing and Communication Workshop and
Conference (CCWC 2018). IEEE, 176–183.

[3] Wanling Cai, Yucheng Jin, and Li Chen. 2022. Impacts of personal characteristics
on user trust in conversational recommender systems. In Proceedings of the 2022
CHI Conference on Human Factors in Computing Systems (CHI 2022). Article 489,
14 pages.

[4] Gary Charness, Uri Gneezy, and Alex Imas. 2013. Experimental methods: Eliciting
risk preferences. Journal of Economic Behavior & Organization 87 (2013), 43–51.
[5] Erin K. Chiou and John D. Lee. 2023. Trusting automation: Designing for respon-

sivity and resilience. Human factors 65, 1 (2023), 137–165.

[6] Konstantina Christakopoulou, Filip Radlinski, and Katja Hofmann. 2016. Towards
conversational recommender systems. In Proceedings of the 22nd ACM SIGKDD
international conference on knowledge discovery and data mining (KDD 2016).
815–824.

[7] Berardina De Carolis, Marco de Gemmis, Pasquale Lops, and Giuseppe Palestra.
2017. Recognizing users feedback from non-verbal communicative acts in con-
versational recommender systems. Pattern Recognition Letters 99 (2017), 87–95.
[8] Eugene F Fama and Kenneth R French. 1998. Value versus growth: The interna-

tional evidence. The journal of finance 53, 6 (1998), 1975–1999.

[9] Christian Hildebrand and Anouk Bergner. 2021. Conversational robo advisors
as surrogates of trust: onboarding experience, firm perception, and consumer
financial decision making. Journal of the Academy of Marketing Science 49, 4
(2021), 659–676.

[10] Dietmar Jannach, Ahtsham Manzoor, Wanling Cai, and Li Chen. 2021. A survey

on conversational recommender systems. Comput. Surveys 54, 5 (2021), 1–36.

[11] Guangyuan Jiang, Manjie Xu, Song-Chun Zhu, Wenjuan Han, Chi Zhang, and
Yixin Zhu. 2024. Evaluating and inducing personality in pre-trained language
models. In Proceedings of the 37th Conference on Neural Information Processing
Systems (NeurIPS 2023).

[12] Hang Jiang, Xiajie Zhang, Xubo Cao, Cynthia Breazeal, Deb Roy, and Jad Kabbara.
2024. PersonaLLM: Investigating the Ability of Large Language Models to Express
Personality Traits. In Findings of the Association for Computational Linguistics:
NAACL 2024. 3605–3627.

[13] Francis M. Kinniry Jr., Colleen M. Jaconetti., Michael A. DiJoseph., Yan Zilbering.,
Donald G. Bennyhoff., and Georgina Yarwood. 2020. Putting a value on your
value: Quantifying Vanguard Adviser’s Alpha in the UK. Technical Report. The
Vanguard Group, Valley Forge, Pennsylvania, USA.

[14] Sherrie Y.X. Komiak and Izak Benbasat. 2006. The effects of personalization
and familiarity on trust and adoption of recommendation agents. MIS quarterly
(2006), 941–960.

[15] Ivica Kostric, Krisztian Balog, and Filip Radlinski. 2021. Soliciting user prefer-
ences in conversational recommender systems via usage-related questions. In
Proceedings of the 15th ACM Conference on Recommender Systems. 724–729.
[16] Kausik Lakkaraju, Sara E. Jones, Sai Krishna Revanth Vuruma, Vishal Pallagani,
Bharath C. Muppasani, and Biplav Srivastava. 2023. LLMs for Financial Advise-
ment: A Fairness and Efficacy Study in Personal Decision Making. In Proceedings
of the 4th ACM Conference on AI in Finance (ICAIF 2023). 100–107.

[17] Cong Li. 2016. When does web-based personalization really work? The distinction
between actual personalization and perceived personalization. Computers in
human behavior 54 (2016), 25–33.

[18] Andrew W. Lo and Jillian Ross. 2024. Can ChatGPT Plan Your Retirement?:
Generative AI and Financial Advice. Harvard Data Science Review (2024). Issue
Special Issue 5.

[19] Tim Loughran and Bill McDonald. 2011. When is a liability not a liability? Textual
analysis, dictionaries, and 10-Ks. The Journal of finance 66, 1 (2011), 35–65.
[20] Robert R. McCrae and Oliver P. John. 1992. An introduction to the five-factor

model and its applications. Journal of personality 60 2 (1992), 175–215.

[21] Sourav Medya, Mohammad Rasoolinejad, Yang Yang, and Brian Uzzi. 2022. An
Exploratory Study of Stock Price Movements from Earnings Calls. In Companion
Proceedings of the Web Conference 2022 (WWW 2022). Association for Computing
Machinery, 20–31.

[22] Pearl Pu, Li Chen, and Rong Hu. 2011. A user-centric evaluation framework for
recommender systems. In Proceedings of the 5th ACM conference on Recommender
Systems (RecSys 2011). 157–164.

[23] Filip Radlinski, Krisztian Balog, Bill Byrne, and Karthik Krishnamoorthi. 2019.
Coached conversational preference elicitation: A case study in understanding
movie preferences. In Proceedings of the 20th Annual SIGdial Meeting on Discourse
and Dialogue (SIGDIAL 2019). 353–360.

[24] Filip Radlinski and Nick Craswell. 2017. A theoretical framework for conver-
sational search. In Proceedings of the 2nd Conference on Human Information
Interaction and Retrieval (CHIIR 2017). 117–126.

[25] Oscar Sainz, Jon Campos, Iker García-Ferrero, Julen Etxaniz, Oier Lopez de Lacalle,
and Eneko Agirre. 2023. NLP Evaluation in trouble: On the Need to Measure
LLM Data Contamination for each Benchmark. In Findings of the Association for
Computational Linguistics: EMNLP 2023, Houda Bouamor, Juan Pino, and Kalika
Bali (Eds.). Association for Computational Linguistics, 10776–10787.

[26] Tetsuya Sakai. 2018. Laboratory experiments in information retrieval. The

information retrieval series 40 (2018), 4.

[27] Javier Sanz-Cruzado, Edward Richards, and Richard McCreadie. 2024. FAR-AI: A
Modular Platform for Investment Recommendation in the Financial Domain. In
Proceedings of the 46th European Conference on Information Retrieval (ECIR 2024),
Part V. Springer-Verlag, 267–271.

[28] Yunfan Shao, Linyang Li, Junqi Dai, and Xipeng Qiu. 2023. Character-LLM:
A Trainable Agent for Role-Playing. In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing (EMNLP 2023). Association for
Computational Linguistics, 13153–13187.

[29] Tuva Lunde Smestad and Frode Volden. 2019. Chatbot personalities matters: im-
proving the user experience of chatbot interfaces. In 5th International Conference
Internet Science: (INSCI 2018). Springer, 170–181.

[30] David J Streich. 2023. Risk preference elicitation and financial advice taking.

Journal of Behavioral Finance 24, 3 (2023), 259–275.

[31] Yueming Sun and Yi Zhang. 2018. Conversational recommender system. In
Proceedings of the 41st International ACM SIGIR Conference on Research and De-
velopment in Information Retrieval (SIGIR 2018). 235–244.

[32] Takehiro Takayanagi, Chung-Chi Chen, and Kiyoshi Izumi. 2023. Personalized
Dynamic Recommender System for Investors. In Proceedings of the 46th Inter-
national ACM SIGIR Conference on Research and Development in Information
Retrieval (SIGIR 2023). Association for Computing Machinery, 2246–2250.
[33] Takehiro Takayanagi, Kiyoshi Izumi, Atsuo Kato, Naoyuki Tsunedomi, and Yuk-
ina Abe. 2023. Personalized Stock Recommendation with Investors’ Attention
and Contextual Information. In Proceedings of the 46th International ACM SIGIR
Conference on Research and Development in Information Retrieval (SIGIR 2023).
Association for Computing Machinery, 3339–3343.

[34] Takehiro Takayanagi, Masahiro Suzuki, Kiyoshi Izumi, Javier Sanz-Cruzado,
Richard McCreadie, and Iadh Ounis. 2025. FinPersona: An LLM-Driven Conver-
sational Agent for Personalized Financial Advising. In Proceedings of the 47th
European Conference on Information Retrieval (ECIR 2025), Part V. Springer-Verlag,
13–18.

[35] Johanne R. Trippas, Sara Fahad Dawood Al Lawati, Joel Mackenzie, and Luke
Gallagher. 2024. What do Users Really Ask Large Language Models? An Initial
Log Analysis of Google Bard Interactions in the Wild. In Proceedings of the 47th
International ACM SIGIR Conference on Research and Development in Information
Retrieval (SIGIR 2024). 2703–2707.

[36] Johanne R. Trippas, Luke Gallagher, and Joel Mackenzie. 2024. Re-evaluating
the Command-and-Control Paradigm in Conversational Search Interactions.
In Proceedings of the 33rd ACM International Conference on Information and
Knowledge Management (CIKM 2024). Association for Computing Machinery,
2260–2270.

[37] Patchara Vanichvasin. 2021. Chatbot Development as a Digital Learning Tool
to Increase Students’ Research Knowledge. International Education Studies 14, 2
(2021), 44–53.

[38] Xuena Wang, Xueting Li, Zi Yin, Yue Wu, and Jia Liu. 2023. Emotional intel-
ligence of large language models. Journal of Pacific Rim Psychology 17 (2023),
18344909231213958.

[39] Pontus Wärnestål. 2005. User evaluation of a conversational recommender system.
In Proceedings of the 4th Workshop on Knowledge and Reasoning in Practical
Dialogue Systems.

[40] Hamed Zamani, Johanne R Trippas, Jeff Dalton, Filip Radlinski, et al. 2023. Con-
versational information seeking. Foundations and Trends® in Information Retrieval
17, 3-4 (2023), 244–456.

[41] Markus Zanker, Laurens Rook, and Dietmar Jannach. 2019. Measuring the impact
International Journal of

of online personalisation: Past, present and future.
Human-Computer Studies 131 (2019), 160–168.

[42] Yongfeng Zhang, Xu Chen, Qingyao Ai, Liu Yang, and W Bruce Croft. 2018.
Towards conversational search and recommendation: System ask, user respond.
In Proceedings of the 27th ACM International Conference on Information and
Knowledge Management (CIKM 2018). 177–186.

[43] Huaqin Zhao, Zhengliang Liu, Zihao Wu, Yiwei Li, Tianze Yang, Peng Shu,
Shaochen Xu, Haixing Dai, Lin Zhao, Gengchen Mai, et al. 2024. Revolutionizing
Finance with LLMs: An Overview of Applications and Insights. arXiv preprint
arXiv:2401.11641 (2024).

[44] Dávid Zibriczky. 2016. Recommender systems meet finance: a literature review. In
Proceedings of the 2nd International Workshop on Personalization & Recommender
Systems in Financial Services (FinRec 2016). 1–10.

[45] Liv Ziegfeld, Daan Di Scala, and Anita HM Cremers. 2025. The effect of prefer-
ence elicitation methods on the user experience in conversational recommender
systems. Computer Speech & Language 89 (2025), 101696.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Are Generative AI Agents Effective Personalized Financial
Advisors?
TakehiroTakayanagi KiyoshiIzumi JavierSanz-Cruzado
takayanagi-takehiro590@g.ecc.u- izumi@sys.t.u-tokyo.ac.jp javier.sanz-
tokyo.ac.jp TheUniversityofTokyo cruzadopuig@glasgow.ac.uk
TheUniversityofTokyo Tokyo,Japan UniversityofGlasgow
Tokyo,Japan Glasgow,UnitedKingdom
RichardMcCreadie IadhOunis
richard.mccreadie@glasgow.ac.uk iadh.ounis@glasgow.ac.uk
UniversityofGlasgow UniversityofGlasgow
Glasgow,UnitedKingdom Glasgow,UnitedKingdom
Abstract ACMReferenceFormat:
Largelanguagemodel-basedagentsarebecomingincreasinglypop- TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMc-
Creadie,andIadhOunis.2025.AreGenerativeAIAgentsEffectivePersonal-
ularasalow-costmechanismtoprovidepersonalized,conversa-
izedFinancialAdvisors?.InProceedingsofthe48thInternationalACMSIGIR
tionaladvice,andhavedemonstratedimpressivecapabilitiesin
ConferenceonResearchandDevelopmentinInformationRetrieval(SIGIR
relativelysimplescenarios,suchasmovierecommendations.But ’25),July13–18,2025,Padua,Italy.ACM,NewYork,NY,USA,10pages.
how do these agents perform in complex high-stakes domains,
https://doi.org/10.1145/3726302.3729897
wheredomainexpertiseisessentialandmistakescarrysubstantial
risk?ThispaperinvestigatestheeffectivenessofLLM-advisorsin
thefinancedomain,focusingonthreedistinctchallenges:(1)elic- 1 Introduction
itinguserpreferenceswhenusersthemselvesmaybeunsureof
Personalizedadviceplaysacrucialroleinoursociety,particularly
theirneeds,(2)providingpersonalizedguidancefordiverseinvest-
incomplexandhigh-stakesdomainslikehealthcareandfinance.
mentpreferences,and(3)leveragingadvisorpersonalitytobuild
Advisorsandprofessionalsinthesefieldsusetheirexpertisetooffer
relationshipsandfostertrust.Viaalab-baseduserstudywith64par-
personalizedguidanceandemotionalsupporttotheirclients,lever-
ticipants,weshowthatLLM-advisorsoftenmatchhumanadvisor
agingpeople’sspecificpreferencesand/orcircumstances.However,
performancewhenelicitingpreferences,althoughtheycanstrug-
advisoryservicesareoftenprovidedatahighcost,effectivelyex-
gletoresolveconflictinguserneeds.Whenprovidingpersonalized
cludingalargeportionofthepopulationfromthiscriticaladvice.
advice,theLLMwasabletopositivelyinfluenceuserbehavior,but
Inthefinancialdomain,tomitigatethisissue,automateddecision
demonstratedclearfailuremodes.Ourresultsshowthataccurate
supportsystemshavebeenwidelystudied,withaspecialfocuson
preferenceelicitationiskey,otherwise,theLLM-advisorhaslittle
investment-relatedpredictions,suchasfinancialassetrecommen-
impact,orcanevendirecttheinvestortowardunsuitableassets.
dations[27,32,33].
Moreworryingly,usersappearinsensitivetothequalityofadvice
Recentadvancesinnaturallanguageprocessingandlargelan-
beinggiven,orworsethesecanhaveaninverserelationship.In-
guagemodels(LLMs)havesignificantlyacceleratedthedevelop-
deed,usersreportedapreferenceforandincreasedsatisfactionas
mentofconversationalagents,presentingthepotentialtofunction
wellasemotionaltrustwithLLMsadoptinganextrovertedpersona,
aspersonalizedassistantsforinformation-seekinganddecision-
eventhoughthoseagentsprovidedworseadvice.
making[40].Theseagentscannowleveragemulti-turndialogues,
enablingdynamic,mixed-initiativeinteractionswherebothusers
CCSConcepts
andsystemscantaketheleadinconversations[1].Thisprogres-
•Informationsystems→Decisionsupportsystems;Person- sion has expanded the application of conversational agents to
alization. varioustasks,suchasrecommendation,questionanswering,and
search[10,24,31,40].
Keywords The application of these conversational agents for financial
decision-makingrepresentsamuchmorecomplexscenariothan
largelanguagemodels,financialadvisor,userstudy,generativeAI
otherslikemovierecommendations,becauseusersarenotnec-
essarilyfamiliarwiththebasicterminologyandconceptsinthis
space,andmistakescarryasubstantialriskthatcanleadtolarge
monetary losses. While there is a growing interest in building
theseconversationalassistantstoprovideautomatedfinancialad-
ThisworkislicensedunderaCreativeCommonsAttribution-ShareAlike4.0Interna-
tionalLicense. vice [18], previous work has mostly targeted agents capable of
SIGIR’25,Padua,Italy handlingsimpleinquiries[16,35,36].Comparedtothesesimple
©2025Copyrightheldbytheowner/author(s).
systems, helping users navigate financial decisions and market
ACMISBN979-8-4007-1592-1/2025/07
https://doi.org/10.1145/3726302.3729897 uncertaintiesposesamuchgreaterchallenge.Therefore,itisnot
286

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
Hi Now, let's talk about the current thesecondstage,givenanindividualasset,theadvisorprovidesin-
user We y lc o o u m m e o ! W st h in at t e in re d s u t s e t d ri e in s ? are s W to h c a k t c f a a i b r n s o d t u i c d t a a t u t h g e e h , A c t o m y m o a u p z r o a n n at y .c t ? o e m nt , i I o n n c . advisor ( f o o r rm n a o t t i ) o t n h a e b i o n u v t e i s t to to r’ t s h p e r i e n f v e e r s e t n o c r e , s in . c T l o ud a i n n s g w h e o r w th th e e d a iff ss e e r t e m nt a q tc u h e e s s -
advisor
I tend to prefer non-cyclical
r A e s r g t e a o y r c d o k l u s e c s m o o s r n o o s d r f t e i t e t i i h a o n e d n to y s e ? c v s o o to n la c o t k m i s le ic advisor user stock e it s c s , o c I e ’ o n m e m o m u m m s n i c s e a u r s b c r w i e e t i n a p se b g la n o s t s u f a i o t s t i r A a v m m n e . t e a o z - on— w w tio e e n c c s o o , m m w p p e a a c r r o e e m p t p w e a r o r s e o p n d e a i r ff s li o e z r n e e d a n li v t z s c e . o d n n o a fi d n g v - u p i r s e a o r t r s i s o o n n w s a i l t o i h z f e t d d h i e s a t L d in v L c i M s t o - p r a e s d r , v s a i o n s n o d a r , : l t i fi h ti r e e s n s t . , ,
I s fe t e o e c c l o k m n s o o t r m h e a i c c t o f c m l a u n f c o t w r u t i a a t t h b i l s o e t n a w s n . i d th im s A i o p g m f a n f a c if e z t i r e c o i a d n n n ’ g s b t y A c r l e W e o v c u S e o d s n n e u s o g e e m m r a v i e n c ic n d s e t w g s d r i r l o n e i w v g s e s s t s h … , … . advisor 2 RelatedWork
user
Stage 1:Preference Elicitation Stage 2:Advisory Discussion 2.1 PersonalizationandPreferenceElicitation
Informationsystems,especiallythosefocusedonsearchandrec-
Figure1:ConceptualillustrationofanLLM-advisorwithtwo
ommendationbenefitfrompersonalization[14].Specifically,per-
stages:(1)PreferenceElicitationand(2)AdvisoryDiscussion.
sonalizationtechniquesplayacrucialroleinenhancinguserex-
yetclearhowtodevelopsystemsthateffectivelysupportcomplex perience [17, 22, 41]. Interactive approaches, such as conversa-
financialinformation-seekinganddecision-makingtasks. tionalpreferenceelicitationrepresentthefrontierofpersonaliza-
Thisworkaimstoclosethisgapbyexploringtheeffectiveness tion.Thisproblemhasreceivedgrowingattention,asadvances
ofLLMstoactaspersonalizedfinancialadvisoryagents.Inpartic- ingenerativeAInowprovideafunctionalmechanismtocollect
ular,wefocusonthreeproblems:(a)elicitinginvestorpreferences userpreferencesdynamicallyinafree-formmanner[40].Thisin-
throughinteractiveconversations,(b)providingpersonalizedguid- teractiveapproachcancapturemorediverseandtargetedinsights
ancetohelpusersdeterminewhetherparticularfinancialassets thanstaticapproacheslikequestionnaires[6,10,23,24,31].In-
alignwiththeirpreferences,and(c)leveragingthepersonalityof deed,recentstudieshaveproposedvariousmethodsforeffective
theadvisortofostertrustontheadvisor. conversationalpreferenceelicitation[31,42],aswellasuserstud-
First,thefinancialliteratureemphasizesthatelicitinguserpref- ies on the perceived quality of this process in domains such as
erencesiscentraltodeliveringsuitableadvice[30].However,it e-commerce,movies,fashion,books,travel,andrestaurantrecom-
remainsunclearwhethercurrentconversationaltechnologies,par- mendations[2,7,15,23,31,45].
ticularlythosepoweredbyLLMs,cancorrectlyelicituserprefer- However,wearguethatforsomeimportantdomains,tryingto
encesinspecializeddomainswhereusers struggletoarticulate directlycollectpreferencesisinsufficient.Animplicitassumption
theirneeds.Ourworkaddressesthischallengeinthecontextof ofthesestudiesisthatifdirectlyasked,theuserwillbeableto
financialservices. accuratelyexpresstheirpreferences.Itisreasonabletoexpectthat
Second,althoughpersonalizationiswidelyregardedasimpor- thisassumptionwouldholdforscenarioslikemovierecommenda-
tantinthefinancialdecision-supportliterature[27,32,33],itsvalue tion;wecanaskauser“doyoulikehorrormovies?”andexpecta
inaconversationalsettingremainsuncertain.Inparticular,weex- usefulresponse.Ontheotherhand,thiswillnotholdforcomplex
plorewhethertailoringdialoguearoundauser’sprofileandcontext tasks,wheretheuserlackstheknowledgetoformanaccuratere-
improvesfinancialdecision-making.Additionally,wealsoexplore sponse[10,39].Forinstance,inaninvestmentcontextifweasked
howpersonalizationinfluencesuserperceptionsoftheadvisor,in “doyoupreferETFsorBonds?”,itisnotclearthataninexperienced
termsofaspectsliketrustandsatisfaction. userwouldbeabletoproduceameaningfulanswer.Inthesecases,
Finally, in personalized advisory settings within high-stakes anidealagentneedstofillthegapsintheuserknowledgethrough
domains,therelationshipandtrustbetweentheclientandadvisor conversation,aswellasinfertheuserpreferencesacrossmultiple
playacrucialrole[18].Researchonconversationalagentssuggests (oftenuncertain)userresponses.Buthoweffectivearegenerative
thatagentpersonalitysignificantlyaffectsusers’perceptionsof AIagentsatthiscomplextask?Thispaperaimstoanswerthatques-
thesystem[3,29].However,itremainsunclearhowanadvisor’s tionforthedomainoffinancialadvisory;aparticularlychallenging
personalityinthefinancialdomaininfluencesboththequalityof domaingivenitstechnicalnatureandhighrisksifdonepoorly.
users’financialdecisionsandtheiroverallexperience.
Tosummarize,inthispaper,weexplorethefollowingquestions: 2.2 Financialadvisory
• RQ1:CanLLM-advisorseffectivelyelicituserpreferences Inthefinancialdomain,advisorshelpindividualsmanagetheir
throughconversation? personalfinancesbyofferingguidanceoninvestmentsandassist-
• RQ2:Doespersonalizationleadtobetterinvestmentdeci- ing with decision-making [34]. While financial advisors can be
sionsandamorepositiveadvisorassessment? beneficial,theirservicesoftencomeatahighcost,makingthem
• RQ3:Dodifferentpersonalitytraitsaffectdecisionquality unaffordableformanypeople.Tomitigatethisissue,automated
andadvisorassessment? (non-conversational)financialdecisionsupportsystemssuchas
Toaddressthesequestions,weconductalab-baseduserstudy financialrecommendersystemshavebeenwidelystudied[44].The
thatexplorestheeffectivenessofLLMsasinteractiveconversational majorityofresearchinthisareahasbeenfocusedonhowtofind
financialadvisors,onwhichwesimulaterealisticinvestmentsce- profitableassets(i.e.thosethatwillmakemoneyifweinvestin
nariosusinginvestornarrativesandstockrelevancescorescurated them).Theseworksassumeasimplifieduser-model,whereanin-
byfinancialexperts.Figure1illustratesanexampleconversation vestorisonlyconcernedwithmaximizingreturn-on-investment
withtheadvisor,dividedintotwostages:first,theLLM-advisorat- overafixedperiodoftime[27,32,33].Thesestudiesframefinancial
temptstocapturetheinvestorpreferencesthroughconversation;in advisoryasarankingproblem,wherethegoalistorankfinancial
287

AreGenerativeAIAgentsEffectivePersonalizedFinancialAdvisors? SIGIR’25,July13–18,2025,Padua,Italy
Investor profile 𝑖 Investmen 𝑖𝑝 t 𝑟 p 𝑒 r 𝑓 eferences Ground truth ranking
N A a g m e e J 3 a 0 son Matthews M St a a r t it u a s l Married c E u x r p a e t r e t d - Stock style c E u x r p a e t r e t d - Ra 1 nk C T o h m e p C a o n ca y -Cola Score (3/3)
Occupation IT Systems Children No Value stock Company
Jason works at a mid-siz D ed e s in c s r u ip ra t n io ce n company and values job Dividend payments 2 Walmart Inc. (2/3)
stability alongside predictable daily responsibilities... He is a Regular dividends
cautious planner favoring steady, reliable returns over 3 JPMorgan Chase & (1/3)
higher-risk investments… He invests in resilient, well- Sensitivity to macro market Co
e d s o t w a n b t li u s r h n e s d — e c s o p m ec p i a al n ly ie t s h os th e a o t f fe c r a in n g r w e e g a u t la h r e d r iv e id c e o n n d o … m ic Defensive stock 4 Amazon.com, Inc. (0/3)
Figure2:Exampleofaninvestorprofile,investmentpreferences,andgroundtruthranking.Dashedlinecomponentsareused
forevaluation(andtherefore,theyarenotshowntotheuser/LLM).
assetsforauseroveraspecifiedtimeperiod.However,arecent 3.1 InvestorProfiles
studysuggeststhatalargepartofthevalueofferedbyhumanfi- TofairlyevaluatetheabilityofanyLLM-advisor,weneedtohave
nancialadvisorsstemsfromtheirabilitytopersonalizeinvestment theminteractwithhumanuserswithrealneeds.Giventheopen-
guidancetoclients’specificneeds,buildrelationships,andfoster endednatureoffree-formconversations,itisdesirabletorepeat
trust[13],ratherthansimplypresentingsuitableassets. eachexperimentwithdifferentpeoplesuchthatwecanobserve
Reflectingonthesefindings,thedevelopmentofconversational variancesinconversationpaths,asthosevariancesmayinfluence
financialadvisorshasdrawnincreasingattention,asitenablesa tasksuccess.However,toenablerepeatability,weneedtoholdthe
dynamicunderstandingofusers’needs,personalizedguidance,and investorneedsconstantacrossrepetitions.Hence,wedefinethree
thepotentialtobuildtrustworthyrelationships[9,16,34,43].Inpar- archetypalinvestorprofiles𝑖 ∈𝐼 basedoninputfromafinancial
ticular,theconversationalagents’personalityhasgainedattention expert,whereourhumanparticipantsaregivenonetofollowwhen
asafactorthatcanhelpbuildrelationshipswithclientsandfoster conversingwiththeLLM-advisor:
trust[18],especiallygiventhesuccessesofconversationalagents
• Investor1:Growth-OrientedHealthcareEnthusiast:
usingtheBigFivepersonalitymodel[20]toenhancetheend-user
Prefershealthcareinnovations,valueshigh-growthopportu-
experience[4,30].Althoughconversationalagentsshowpotential
nities,andtakesmeasuredrisks.
infinance,howtoconfigurethemtomatchthevalueofhuman
• Investor2:ConservativeIncomeSeeker:Seeksstable
advisorsremainsunclear.Therefore,weconductauserstudyto
returns,investsinwell-establishedcompanies,valuesregular
examinehowpersonalizinginvestmentguidanceandtheadvisor’s
dividendpayouts.
personalityshapeusers’financialdecision-makingeffectiveness
• Investor3:Risk-takingValueInvestor:Targetsunder-
andoveralluserexperience.
valuedcompanieswithstronglong-termpotential,tolerates
short-termvolatility,andinvestsincyclicalsectors.
3 Methodology
Foreachoftheseinvestorprofiles,weselectthreekeyinvestment
Inthispaperweaimtodeterminetowhatextentcurrentgenerative
preferences,chosenfromwell-knowninvestmentcharacteristics
languagemodelscanactasaneffectivefinancialadvisor.Indeed,
suchasindustrysector,stockstyle,consistencyindividendpay-
giventheneedtopersonalizefortheuser,emotionalimplications,
ments,andsensitivitytoglobalmarketchanges[8].Wedenote
the technical nature of the information-seeking task, and high thesetofinvestorpreferencesas𝑖𝑝𝑟𝑒𝑓
.Inourexperiments,we
impact if failed, we argue that this is an excellent test case for
simulatearealisticelicitationscenariowheretheadvisorcollects
thelimitsofgenerativelargelanguagemodels.Tostructureour
thepreferencesfromtheparticipants.Therefore,wedonotstraight-
evaluation,wedivideourstudyintotwophases,asillustratedin
forwardlyprovidethepreferencestotheparticipants.Instead,we
Figure1,whereweevaluatethesuccessofboth:
presentthemastextnarrativesofbetween150to200words.A
(1) PreferenceElicitation:Duringthisstage,wehavetheLLM- financialexpertwasconsultedtoconfirmthequalityandreliability
advisorholdanaturallanguageconversationwithahuman, ofthesenarratives.AnexamplenarrativerepresentingInvestor2is
whereitisdirectedtocollectinformationregardingtheper- illustratedinFigure2,wherewehighlightthesentencesreferring
son’sinvestmentpreferences.Thehumaninthisinteraction tospecificinvestorpreferences.
ispretendingtohavepreferencesfromagiveninvestorpro-
file. 3.2 Stage1:PreferenceElicitation
(2) AdvisoryDiscussion:Duringtheadvisorydiscussion,the
Thegoalofstage1ofourstudyistodeterminetowhatextentan
LLM-advisoragainhasanaturallanguageconversationwith
LLM-advisorcaneffectivelycollectauser’sinvestmentpreferences
thehuman(actingonaninvestorprofile),wherethehuman
through conversation. Formally, given a participant of the user
collectsinformationaboutwhetheracompanyisasuitable
study𝑢andaninvestorprofile𝑖,duringtheelicitationstage,the
investmentforthem.Thisisrepeatedformultiplecompanies
LLM-advisoraimstoobtainanapproximatedsetofpreferences,
perinvestorprofile. denoted𝑖 𝑢 𝐿𝐿𝑀 ,thatmatchestheinvestorpreferences(𝑖𝑝𝑟𝑒𝑓 ).To
Weprovidepreparatoryinformationanddiscusseachstageinmore achievethis,thegenerativemodelproducesaseriesofquestions
detailbelow: that participants answer by interpreting the investor narrative.
288

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
| R e sp o n s e | s t o t h o s e q    | u e st i o n s, d en o | t e d a s𝑅 𝑢 , | a r e u se d b y th e L L M - |     |                      |                         |                           |
| -------------- | -------------------- | ---------------------- | -------------- | ----------------------------- | --- | -------------------- | ----------------------- | ------------------------- |
|                |                      |                        | 𝑖              |                               |     | Participant Training |                         |                           |
|                |                      | 𝑖                      | 𝐿 𝐿 𝑀          |                               |     |                      | Stag e  2 :   A d v i s | o r y  D is c u s s i o n |
| ad v is o r t  | o g e n e r a te t h | e u s e r p ro fi le   | 𝑢 . Su c c     | e s s is th e n m e as u r ed |     |                      |                         |                           |
bymanuallyevaluatingtheoverlapbetween𝑖𝑝𝑟𝑒𝑓 𝐿𝐿𝑀 Y o u   m i g h t  w a n t  to  i nv e s t  i n
|     |     |     |     | and𝑖 . |     | Investor Profile Allocation | tessa hcae roftaepeR Amazon Inc, it is a large…. |     |
| --- | --- | --- | --- | ------ | --- | --------------------------- | ------------------------------------------------ | --- |
𝑢
For user elicitation, we adopted a System-Ask-User-Respond Why this company?
|     |     |     |     |     |     | Stage 1: Preference Elicitation | Amazon has a dominant  |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | ---------------------- | --- |
(SAUR)paradigm[42].Duringtheconversation,theadvisorproac- Before we start investing, I  market share in online shop…
|     |     |     |     |     |     | need to get to know about you | How profitable has it been in  |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | ------------------------------ | --- |
tivelyinquiresabouttheuser’spreferencesgivenasetoftarget the last 3 years?
Have you invested before?
preferences(e.g.,industrytype,acceptablerisk).Afterthehuman gnisilanosrep fI The stock price has increased
|     |     |     |     |     |     | No, I am a new investor | by 67% and has a Sharpe Ra.. |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | ---------------------------- | --- |
participantrespondstoaquestion,theLLM-advisorcheckswhether Explain Sharpe Ratio?
How long are you looking to
thecollectedpreferencescoverallofthetargetpreferences.Ifthead- invest for? Sharp Ratio is a combined
|                                                            |     |     |     |     |     | I am saving for a house, so    | profitability and risk metric.. |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------ | ------------------------------- | --- |
| visorisconfidentthattheydo,itendstheconversationandprompts |     |     |     |     |     | maybe 5 years?                 |                                 |     |
|                                                            |     |     |     |     |     | How adverse are you to taking  | Asset Ranking and Feedback      |     |
theusertoproceedtothenextstage;otherwise,itcontinuesasking risks with your money?
|                            |     |     |     |     |     | Is investment risky? What are  |                                | If all assets rated… |
| -------------------------- | --- | --- | --- | --- | --- | ------------------------------ | ------------------------------ | -------------------- |
| follow-upquestionsinaloop. |     |     |     |     |     |                                | Repeat for second LLM-Advisor  |                      |
|                            |     |     |     |     |     | the risks I should consider?   | variant  (go-to       )        |                      |
Different investment
|     |     |     |     |     |     | strategies come with…. |     | If both conditions tested… |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | -------------------------- |
3.3 Stage2:AdvisoryDiscussion
Exit Questionnaire
Response Summarization
Stage2ofourstudyinvestigatestowhatextentanLLM-advisorcan
providethesamebenefitsasarealhumanadvisorwhenexploring
investmentoptions.NotethatthegoalhereisnottohavetheLLM-
Figure3:Userstudystructure.
advisorpromoteanyoneasset,butrathertoprovideaccurateand
Theadvisorusingthispromptactsasourbaselinefortheadvisory
| meaningful | information | such that | the human | can find the best |     |     |     |     |
| ---------- | ----------- | --------- | --------- | ----------------- | --- | --- | --- | --- |
discussionstudy.Weaugmentthisbaselinewithadditionalcontext
investmentopportunityforthem.Tothisend,westructureour
andinstructionstoformtwoadditionalexperimentalscenarios,
experimentsuchthatthehuman(actingonaninvestorprofile)has
discussedbelow:
oneconversationwiththeLLM-advisorforeachofasetofassets
beingconsidered.1Afterallassetsarepresentedtotheparticipant,
+Personalization:Asdiscussedearlier,oneofthecorerolesofthe
astockrankingisgeneratedbysortingthestocksbytheparticipant financialadvisoristopersonalizetotheindividualcustomer,based
ratingindescendingorder. ontheirfinancialsituation,needs,andpreferences.Toenablethe
Importantly,asweknowtheinvestorprofile𝑖𝑝𝑟𝑒𝑓
|     |     |     |     | foreachcon- | LLM-advisortopersonalizefortheuser,weintegratethegener- |     |     |     |
| --- | --- | --- | --- | ----------- | ------------------------------------------------------- | --- | --- | --- |
versationaboutanasset𝑎,wecanobjectivelydeterminewhether𝑎 atedprofilefromthepreferenceelicitation(Stage1)𝑖 𝐿𝐿𝑀
𝑢 intothe
isagoodinvestmentgiven𝑖𝑝𝑟𝑒𝑓
,formingagroundtruthagainst prompt.Werepresenteachpreferenceasaseriesofshortsentences.
whichwecancomparetotheratingprovidedbyourhumanpar-
+Personality:InSection2.2wediscussedhowhumanfinancial
ticipantaftertheirconversationwiththeLLM-advisor.Foreach
|                                                   |     |     |     |     | advisors | provide emotional support | as well as | financial advice. |
| ------------------------------------------------- | --- | --- | --- | --- | -------- | ------------------------- | ---------- | ----------------- |
| asset𝑎,afinancialexpertproducedascorebetween0and3 |     |     |     | by  |          |                           |            |                   |
manuallycheckingwhether𝑎satisfiedeachofthethreeinvestment WhileitisunlikelythatanLLM-advisorcoulddothisaswellasa
criteriacontainedin𝑖𝑝𝑟𝑒𝑓 human(itlacksbothemotionalintelligenceandnon-conversational
.Aground-truthrankingwasproduced
cluestothecustomer’smentalstate[38]),itmightbepossibleto
bysortingtheassetsbytheexpertscores.Weshowanexample
provideabetterend-userexperiencebydirectingtheLLM-advisor
| of the ranking | construction | in Figure | 2. During | evaluation, the |     |     |     |     |
| -------------- | ------------ | --------- | --------- | --------------- | --- | --- | --- | --- |
toadoptapersonality.AsnotedinSection2itispossibletodothis
closertheparticipantrankingistotherankingproducedbyexpert
viapromptengineering,suchasinstructingtheLLMtotakeonthe
judgments,thebettertheLLM-advisorperformed.
traitsofoneormoreoftheBig-Fivepersonalitytypes[20].
BaselinePrompt:AsweareworkingwithanLLM-advisorand Asweareperformingauserstudywithhumans,itwouldbe
thenatureoffinancialinformation-seekingistime-sensitive,we impracticaltoexhaustivelytesteverycombinationofpersonality
needtoprovideanyinformationthatmightchangeovertimetothe types,henceasaninitialinvestigationweexperimentwithtwo
LLMwithintheprompt.Assuch,foreachasset𝑎,wepre-prepared distinctpersonalityprofiles[29]:
astandardassetdescriptorblockafterconsultingwithafinancial • Extroverted:Highinextroversion,agreeableness,andopen-
expert,containing: ness;lowinconscientiousnessandneuroticism.
| • StockPrices:Wecollectmonthlystockpricesfrom2023 |     |     |     |     | •   |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Conscientious:Lowinextroversion,agreeableness,and
usingYahoo!Finance.2
openness;highinconscientiousnessandneuroticism.
• BusinessSummary:Wegathereachcompany’sbusiness WeadoptedthepromptingmethodfromJiangetal.(2024)to
overviewfromYahoo!Finance.
assignaBigFivepersonalitytraittotheLLMagent[12],choos-
• RecentPerformanceandKeyFinancialIndicators(e.g.,
ingitforitssimplicityandeffectivenessamongvariousproposed
EPS):Weobtainearningsconferencecalltranscripts3from
approachesforembeddingpersonalityinLLMs(includingboth
SeekingAlphaforthelastquarterof2023. promptingandfine-tuning)[11,12,28].Toensureahighstandard
ofprofessionalismandaccuraterepresentationoftheintendedper-
1Theseweremanuallyselected,howeverinaproductionenvironmentthesemightbe
producedbyanassetrecommendationsystem. sonality,weconsultedfinancialprofessionalstoreviewthetexts
2ThescenarioforthefinancialadvisingofouruserstudyissettoDecember30,
generatedbyLLMsadoptingbothpersonas.
2023.Bybasingourexperimentattheendof2023,weavoidtheproblemofdata
contamination[25].
3Earningsconferencecalls,hostedbypubliclytradedcompanies,discusskeyaspects transcriptscoversignificantfinancialindicatorsandprovideexplanationsofrecent
performance.
oftheirearningsreportsandfuturegoalswithfinancialanalystsandinvestors,thus
coveringcriticalfinancialindicatorsandrecentperformanceinsights[21].These
289

AreGenerativeAIAgentsEffectivePersonalizedFinancialAdvisors? SIGIR’25,July13–18,2025,Padua,Italy
3.4 ExperimentalDesign Table1:Operationaldefinitionsusedintheadvisorassess-
mentquestionnaireforallresponsedimensions.
Inourexperiment,weconductedtwostudies:apersonalization
study(forRQ2)andanadvisorpersonastudy(forRQ3).Inthe
personalizationstudy,participantscomparedanon-personalized ResponseDimension OperationalDefinition
(Baseline)advisorwithapersonalized(+Personalized)version.In PerceivedPersonalization[14] Theadvisorunderstandsmyneeds.
EmotionalTrust[14] Ifeelcontentaboutrelyingonthisadvisorformydecisions.
theadvisorpersonastudy,theycompareddifferentLLM-advisor
TrustinCompetence[14] Theadvisorhasgoodknowledgeofthestock.
personalitytypes(+Extrovertedvs.+Conscientious).Participants
Iamwillingtousethisadvisorasanaidtohelpwithmy
arerandomlyassignedtooneofthesetwostudies. IntentiontoUse[14] decisionaboutwhichstocktopurchase.
Figure3showsthestructureofouruserstudyforasinglepar- PerceivedUsefulness[22] Theadvisorgavemegoodsuggestions.
ticipant,comprisingsevensteps: OverallSatisfaction[22] Overall,Iamsatisfiedwiththeadvisor.
InformationProvision[37] Theadvisorprovidesthefinancialknowledgeneeded.
(1) ParticipantTraining:Participantsaregivenageneraloverview
In our experiments, we use Llama-3.1 8B as the background
oftheuserstudyandgiveninstructionsontheirexpected
modelforallourLLM-advisorvariants.4
rolesduringpreferenceelicitation,advisorydiscussions,as-
setranking,andadvisorassessment.
3.5 Participants
(2) InvestorProfileAllocation:Theuser𝑢israndomlyallo-
catedoneoftheinvestorprofiles(SeeSection3.1)thatthey Werecruited64participantsfromtheauthors’affiliateduniversity
willfollow.Eachprofileisassignedto42participants. forourstudy:32participantsforthepersonalizationstudyand32
(3) PreferenceElicitation(Stage1):Theparticipantinteracts participantsfortheadvisorpersonastudy,utilizingtheuniversity’s
withtheLLM-advisorasiftheywereanewinvestor.The onlineplatformandblackboardforrecruitment.Participantswere
conversationendsoncetheLLM-advisordeterminesthat requiredtobefluentinEnglish,over18yearsold,andhaveanin-
they know enough about the investor to personalize for terestinfinanceandinvestment,mirroringthetargetdemographic
them.Themediantimespentonpreferenceelicitationwas ofoursystem’susers.Afterexcludinginvaliddata,29participants
5minutesand11seconds. remainedinthepersonalizationstudyand31intheadvisorpersona
(4) ResponseSummarization:Giventheaggregatorofuser study.WeconductedapoweranalysisusingtheWilcoxonsigned-
responses𝑅 𝑖 𝑢 ,weinstructanLLMtogenerateaninvestor ranktestformatchedpairs,withtheexperimentalconditionsas
profile𝑖 𝑢 𝐿𝐿𝑀 .Foreachinvestorpreferencein𝑖𝑝𝑟𝑒𝑓 ,ifthereis theindependentvariableandusers’responsetotheadvisorassess-
anyrelevantinformationintheresponses𝑅 𝑖 𝑢 ,thatinforma- mentquestionnaireasthedependentvariable[26].Theanalysis
tionisincludedin𝑖 𝑢 𝐿𝐿𝑀 .Otherwise,𝑖 𝑢 𝐿𝐿𝑀 indicatesthatno determinedthat29participantsareneededtoobserveastatistically
significanteffectonuser-perceivedquality.Ourrecruitmentcri-
relevantinformationisavailableforthatspecificpreference.
teriaandcompensation(£10/hour)forapproximatelyonehourof
(5) AdvisoryDiscussion(Stage2):Tosimplifytheconversa-
participationwereapprovedbyourorganization’sethicalboard.
tionflowwehavetheparticipantholdseparateconversations
withtheLLM-advisorforeachassettheymightinvestin.
4 EvaluationMetricsandStatistics
TheLLM-advisorisprovidedwithcontextaboutthecurrent
asset (see Section 3.3), and depending on the experimen- Inthissectionwediscusshowwequantifyeffectivenessforthe
talscenario,optionallypersonalizationinformation(step4 preferenceelicitationandadvisorydiscussionstages,respectively,
output)and/oratargetpersonalitycontextstatement.Each inadditiontosummarizingdatasetstatisticsforeach.
conversationcontinuesuntiltheuserissatisfiedthatthey
4.1 PreferenceElicitationMetrics(Stage1)
have enough information to rate the asset. The order in
whichtheassetsarediscussedisrandomlyassignedtoavoid To evaluate the quality of the first preference elicitation stage,
positionbias. wewanttomeasurehowwelltheLLM-advisorhascapturedthe
(6) AssetRankingandFeedback:Participantsrankallthe investorpreferencesasdefinedintheinvestorprofile𝑖 (seeSec-
stocks(fourintotal)discussedintheadvisorysessionac- tion3.1).Eachinvestorprofile𝑖 ∈ 𝐼 defineskeyfeaturesofthe
cordingtotheirdesiretoinvestineach.Theyalsoassessthe investor,suchaspreferringhigh-growthstocks,orfavoringregu-
advisortheyinteractedwithusinga7-pointLikertscalefor larpayouts,denoted𝑖𝑝𝑟𝑒𝑓 .Wehavethreeinvestorprofiles(|𝐼|=3),
theitemslistedinTable1(seeSection4). with10(𝑛)participantsperformingelicitationon𝑖 𝑢 𝐿𝐿𝑀 foreach
profileandeachLLMvariant,i.e.thereare120elicitationattempts
Toenablemoreeffectivepair-wisecomparisonofLLM-advisorvari- intotal,with30attemptsperLLM-advisorvariant.Followingthe
ants,wehaveeachparticipanttesttwovariantsperstudy.Ifthe notationinSection3,𝑖 𝑢 𝐿𝐿𝑀 inthiscasedenotesasimilarlistoffea-
userhasonlytestedonevariantatthispoint,thentheyrepeatthe turesto𝑖𝑝𝑟𝑒𝑓 thatLLM-advisorlearnedabouttheinvestorduring
userstudy(startingatstep2)withthesecondvariant.Theorderin conversationwithaparticipant𝑢,whichwederivefromamanual
whichparticipantsexperienceeachvariantisrandomlyassigned. analysisoftheelicitationoutput(i.e.whatisproducedbyresponse
summarization).Intuitively,thecloserthefeaturesproducedfrom
(7) ExitQuestionnaire:OnceapairofLLM-advisorvariants
4FurtherdetailsabouttheLLMconfiguration,investornarratives,relevantscores,
havebeentested,theuserfillsinanexitquestionnairethat
promptsandscriptsfordataanalysiscanbeaccessedatthefollowingrepository:
isdesignedtoasktheoverallexperienceintheuserstudy. https://github.com/TTsamurai/LLMAdvisor_supplementary
290

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
Table2:Generalstatisticsofthecollectedconversationdata. Table3:Stage1-ComparisonofElicitationAccuracyofan
expertvs.differentLLM-advisorsforeachinvestorprofile.
Participants 60 Thebestadvisorishighlightedinbold.Arrowsdenoteper-
| TimePeriod | 2024/10/24~2024/11/7 |     |     |     |     |     |
| ---------- | -------------------- | --- | --- | --- | --- | --- |
centageincreases(↑)ordecreases(↓)comparedtotheexpert.
| TotalTurns                   |     | 10,008 |                 |        |               |         |
| ---------------------------- | --- | ------ | --------------- | ------ | ------------- | ------- |
| Stage1:PreferenceElicitation |     |        |                 |        | LLM-Advisors  |         |
| TotalTurns                   |     | 1,788  | InvestorProfile | Expert |               |         |
| NumberofSessions             |     | 120    |                 | LLM    | +Extr. +Cons. | Average |
Avg.Turns/Session 15.8
|                    |     |     | Growth-Oriented     |           | 0.80      | 0.78→0.0% |
| ------------------ | --- | --- | ------------------- | --------- | --------- | --------- |
| Avg.UserWords/Turn |     | 9.8 |                     | 0.78 0.76 | 0.79      |           |
|                    |     |     | Conservative-Income | 0.89 0.82 | 0.75 0.87 | 0.82↓7.8% |
Stage2:AdvisoryDiscussion
|     |     |     | Risk-Taking | 0.89 0.48 | 0.60 0.55 | 0.53↓40.5% |
| --- | --- | --- | ----------- | --------- | --------- | ---------- |
TotalTurns 8,220
0.70↓17.6%
| NumberofSessions |     | 480 | Average | 0.85 0.69 | 0.70 0.73 |     |
| ---------------- | --- | --- | ------- | --------- | --------- | --- |
Avg.Turns/Session 18.2
Avg.UserWords/Turn 13.0 asession,e.g.duringStage1,therewere3investorprofiles*10
anyelicitationattempt𝑖 𝐿𝐿𝑀 isto𝑖𝑝𝑟𝑒𝑓 participants*4LLM-advisors,resultingin120sessions.Stage2has
𝑢 ,thebettertheLLM-advisor
isperforming.Tothisend,wereportelicitationaccuracyforeach 4xthenumberofsessions,astherearefourassetsassociatedwith
eachprofile(𝐴
| investorprofile,calculatedas: |     |     | 𝑖)todiscusswiththeLLM-advisor. |     |     |     |
| ----------------------------- | --- | --- | ------------------------------ | --- | --- | --- |
(cid:12) (cid:12) FromTable2weobservethatincontrasttootherconversational
|     | 𝑛 (cid:12)𝑖𝐿𝐿𝑀 | ∩𝑖𝑝𝑟𝑒𝑓(cid:12) |     |     |     |     |
| --- | -------------- | -------------- | --- | --- | --- | --- |
1∑︁(cid:12) 𝑗 (cid:12) tasks [35, 36], financial information-seeking appears to require
ElicitationAccuracy(𝑖)= (1)
𝑛 (cid:12)𝑖𝑝𝑟𝑒𝑓(cid:12) moreextendedinteractions.Onaverage,preferenceelicitationin-
|     | 𝑗=1 | (cid:12) (cid:12) |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- |
HumanAdvisor:Toprovideapointofcomparison,wealsocon- volves15turnspersessionwith9.8wordsperturn,whereasadvi-
sorydiscussionsinvolve18turnspersessionwith13.0wordsper
ductapreferenceelicitationwithafinancialexpertusingthesame
turn,highlightingtheoverallcomplexityofthetask.
promptandinstructionsastheLLM.Thisallowsustoevaluate
howcloseLLMsaretoapaidhumanadvisorundertakingthesame
5 Results
task.Morespecifically,foreachinvestorprofile,threeparticipants
engagedwiththisexpert,whothenproducedasetofpreferences Inthiswork,weexplorehowtodesignconversationalfinancialadvi-
𝐸𝑥𝑝𝑒𝑟𝑡 𝐿𝐿𝑀 sorsthatenhancebothdecision-makingandpositiveexperience.To
| 𝑖 𝑢 ,whichcanbeusedinsteadof𝑖 | 𝑢 inEquation1. |     |     |     |     |     |
| ----------------------------- | -------------- | --- | --- | --- | --- | --- |
achievethis,ouruserstudyisguidedby3coreresearchquestions.
4.2 AdvisoryEffectivenessMetrics(Stage2) • RQ1:CanLLM-advisorseffectivelyelicituserpreferences
throughconversation?
Rankingcorrelation(Spearman’sRho):Inthesecondstage,
weevaluatehowwelltheLLM-advisorcansupportaninvestorto • RQ2:Doespersonalizationleadtobetterdecisionsandmore
selectfinancialassetsthataresuitableforthemtoinvestin.Recall positiveadvisorassessment?
• RQ3:Dodifferentpersonalitytraitsaffectdecisionquality
fromFigure3thatafteraparticipantfinishesdiscussingallassets
withtheLLM-advisor,theyrankthoseassets𝑎∈𝐴 andadvisorassessment?
𝑖 basedonthe
| likelihoodtheywillinvestineach,i.e.eachparticipant𝑢 |     | acting |     |     |     |     |
| --------------------------------------------------- | --- | ------ | --- | --- | --- | --- |
onaprofile𝑖wehaveanassetranking𝑅(𝐴 𝑖 ,𝑖 𝑢).Asillustratedin 5.1 RQ1:Elicitationaccuracy
Figure2,eachinvestorprofile𝑖wasderivedfromagroundtruth
WebeginbyexamininghoweffectivetheLLM-advisorsareatiden-
setofinvestorpreferences𝑖𝑝𝑟𝑒𝑓
,whichanexpertusedtocreate tifying investment preferences during conversations in Stage 1.
| agroundtruthranking𝑅(𝐴 ,𝑖𝑝𝑟𝑒𝑓),i.e.the“correct”rankingof |     |     |                                                          |     |     |     |
| -------------------------------------------------------- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
| 𝑖                                                        |     |     | ElicitationAccuracyistheprimarymetric,wherewecontrastthe |     |     |     |
,𝑖𝑝𝑟𝑒𝑓),thebet-
| assets.Intuitivelythecloserthe𝑅(𝐴 | 𝑖 ,𝑖 𝑢)isto𝑅(𝐴 | 𝑖   |     |     |     |     |
| --------------------------------- | -------------- | --- | --- | --- | --- | --- |
meanaccuracyacross10sessionsincomparisontoahumanexpert
tertheadvisorisperforming,astheparticipantwasbetterableto
tacklingthesametask(seeSection4.1).Table3reportselicitation
distinguishsuitableassetsvs.unsuitableones.Hence,toevaluate accuracyforeachLLM-advisorandtheHumanExpertacrossinvest-
theeffectivenessoftheadvisorytask,wereportthemeanranking mentprofiles.Arrowsdenotepercentageincreases(↑)ordecreases
,𝑖𝑝𝑟𝑒𝑓)
correlation(Spearman’sRho)between𝑅(𝐴 𝑖 ,𝑖 𝑢) and𝑅(𝐴 𝑖 (↓)oftheLLM-advisorcomparedtotheexpert.
acrossparticipants𝑢foreachLLM-advisor. Tosetexpectations,wefirstconsidertheperformanceofthe
expertinthefirstcolumninTable3,aswemightexpect,theex-
AdvisorAssessmentQuestionnaire:Lastly,wealsogatherqual-
pertmaintainsconsistentlyhighperformanceacrossallprofiles,
itativedatafromeachparticipantviaaquestionnaire.Inparticular,
averaging85%accuracy(randomaccuracyis50%).Thisformsan
afterrankingassetseachparticipant,reportshowtheyfeelthe
expectationoftheperformanceceilingforthetask.
LLM-advisorperformedintermsof7dimensions,listedinTable1,
Next,wecomparetheexpertperformancetoeachLLM-advisor.
suchasperceivedusefulness,trust,andusersatisfaction.Weuse
Fromtheperspectiveofpreferenceelicitation,therearethreeLLM-
thisdatalatertoevaluatehowsensitivetheuseristodifferencesin
advisorconfigurations,thosethatuseonlytheBaselinePrompt(de-
theLLM-advisor.
notedLLM)fromthepersonalizationstudy,andthosethatinclude
adefinedpersonality(eitherextroverted,+Extr.,orconscientious,
4.3 DatasetStatistics
+Cons.)fromtheadvisorpersonastudy.5FromTable3,weobserve
Table2summarizesthestatisticsofthedatacollectedduringthe
twostagesofouruserstudy.Eachconversationthataparticipant 5Notewecannothaveapersonalizedvarianthere,asthepersonalizationevidenceis
| hadwithanLLM-advisorineitherstage1or2isreferredtoas |     |     | derivedfromthisstage. |     |     |     |
| --------------------------------------------------- | --- | --- | --------------------- | --- | --- | --- |
291

AreGenerativeAIAgentsEffectivePersonalizedFinancialAdvisors? SIGIR’25,July13–18,2025,Padua,Italy
thattheLLM-advisor’sperformanceisgenerallystrongforgrowth- Table4:Investordecision-makingeffectiveness,expressed
oriented,andconservative-incomeinvestors(withaccuracyaround astheSpearman’sRhocorrelationbetweentheinvestor’s
80%)onaverage,whichissimilartothehumanadvisor.However, assetrankingandtheexpertassetranking(higherisbetter).
fortherisk-takinginvestorprofile,theLLM-advisor’selicitation
†indicatesstatisticalimprovements(Welch’st-testwith𝑝 <
accuracywassubstantiallylower(-40.5%). 0.05)overthenotpersonalizedbaseline,while§ indicates
Fromamanualfailureanalysis,weobservedthefollowingtrends significant differences between cases with successful and
thatcontributetotheperformancegapwiththehumanadvisor, unsuccessfulpreferenceelicitations.
particularlyfortherisk-takingprofile.First,itisnotablethatelici-
AdvisorConfig Investorvs.Expert(Spearman’sRho)
tationfailurescanoriginatefromtheinvestor(participant)rather
thantheLLM.Recallthatoneoftheaspectsthatmakesfinance Personalization Personality All PreferenceElicitation
Successful Unsuccessful
morechallengingthandomainslikemovierecommendationisthat
Baseline None 0.110 – –
the“user”isinexpert,andsomaygiveincorrectinformationduring
+Personalized None 0.310 0.481†§ -0.228
theconversation.Indeed,weobservedcaseswheretheparticipant +Personalized +Extroverted 0.122 0.243§ -0.286
confusedconceptssuchasthedifferencebetweenagrowthanda +Personalized +Conscientious 0.26 0.365 -0.025
valuestock,aswellascyclical/non-cyclicalassets.Ontheotherside,
baselineadvisoryperformanceislow,withonlyaveryweakpos-
preferencehallucinationisacoreissuefortheLLM-advisor.The
itivecorrelationtothegroundtruthrankingof0.11.Thisindicates
LLMisaprobabilistictokengeneratorconditionedonthebaseline
thatwithoutfurtherevidence,theLLMisnotabletomeaningfully
promptandpriorconversation,andasaresult,insomescenarios,
guidetheinvestor.
thecontextualcontentcanoverrideastatementbytheinvestor.
Thistypeoferrorismorelikelywhentheinvestorisunsurein 5.2.2 PersonalizedDecision-makingEffectiveness: Havingestab-
theirresponsesorwhentheyprovidecontradictorystatements. lishedourbaseline,wenowexaminetheimpactthataddingthe
Forinstance,aninvestorexpressinganinterestintheconsumer investorpreferencescollectedduringstage1has,comparingTable4
discretionarysectorwhilesimultaneouslyoptingfornon-cyclical row1(baseline)torow2(personalized).Asweanticipated,person-
stocks,despiteconsumerdiscretionarybeinginherentlycyclical. alizationisbeneficial,withinvestordecision-makingeffectiveness
increasingfrom0.11to0.31(averageSpearman’sRhocorrelation
ToanswerRQ1,ourresultsdemonstratethatLLM-advisor’sare
totheexpertranking).However,thiscorrelationisstillweak,illus-
abletoelicitpreferencesfromauserviaconversationandthatfor
tratingthatwhilediscussingassetswiththeLLM-advisorisbetter
2/3’softheuserprofilestested,elicitationaccuracywasconsistently
thannohelpatall,ourparticipantsarestillstrugglingtoevaluate
equivalentorclosetothatofanexperthumanadvisor.However,
thesuitabilityoffinancialassets.
weobservedaclearfailuremodewhentestingtherisk-takingpro-
Thiscorrelationisanaverageoveralltheparticipantsintheuser
file,wheremisunderstandingsbytheinvestorsandhallucinations
study,regardlessofhoweffectivetheirpreferenceelicitationwasin
withintheLLMcompoundtoresultinaccuracythatisclosetoran-
stage1.Hence,wemightaskwhetherthelowcorrelationisdueto
dom.Overall,weconsiderthisapromisingresult,asthemajority
theLLM-advisorbeingconfusedbypoorpreferenceelicitationdata.
ofthetimeitiseffective,andthefailuremodeobservedmightbe
Toexplorethis,Table4alsoreportsinvestordecision-makingeffec-
rectifiedbybettercontextcraftingandtheadditionofcontradiction
tivenessstratifiedbasedonwhetherstage1wassuccessful(column
detection;bothdirectionsforfutureresearch.
4)ornot(column5).6Asexpected,weseeastatisticallysignificant
increaseininvestordecision-makingeffectivenesswhenprefer-
5.2 RQ2:Effectivenessofpersonalization
enceelicitationwassuccessfulwhencomparedtonon-personalized
Havingshownthatautomaticpreferenceelicitationispossible,we sessions(0.481vs.0.110).Moreconcerningly,wealsoseetheLLM-
nowexaminestage2ofourstudy,namelytheadvisorydiscussions. advisorhasastrongnegativeinfluenceontheinvestors’decision-
Giventheinherentlypersonalizednatureoffinancialadvice,we makingcapabilityifpreferenceelicitationfails,asillustratedby
expectthatthecustomerpreferencesobtainedduringstage1will thenegativecorrelationswiththeexpertincolumn5.Thisresult
bekeytoenablingLLM-advisorstoprovideeffectiveinvestment highlightsboththateffectivepreferenceelicitationiscrucial,but
advice.Hence,inthissection,wecomparetheperformanceofan alsothattheLLM-advisorcaneasilyinfluencetheinvestorinto
LLM-advisorusingonlytheBaselinePrompttoonethatincludes makingpoordecisions,asthehumanisheavilyreliantontheagent
thepreferencesobtainedduringstage1(+Personalized).However, tonavigatetherelativelyunfamiliarfinancialinformationspace.
asweobservedthatpreferenceelicitationisnotalwayssuccessful,
5.2.3 ParticipantAssessmentoftheAdvisor: Sofarwehavedemon-
wealsoexaminewhateffectelicitationperformancehasonthe
stratedthatthereisalargedifferencebetweenanon-personalized
LLM-advisor.
LLM-advisorandapersonalizedone,intermsofhowtheycan
alterthedecision-makingoftheinvestor/participant.Butcanthe
5.2.1 Non-personalizedDecision-makingEffectiveness: Weinitially
participanttellthedifferencesbetweenthem?
establishhoweffectivetheLLM-advisoriswithoutanyinforma-
Table5reportstheaggregationofthequalitativedatawecol-
tionregardingtheinvestor.LLM-advisoreffectivenessismeasured
lectedfromeachparticipantaftertheyfinishedinteractingwith
basedonhowwelltheinvestorwasabletoranktheassetsdiscussed
each LLM-advisor in terms of 7 dimensions, where we start by
bysuitabilitytothem.TheprimarymetricisaverageSpearman’s
Rhocorrelationbetweentheinvestorrankingandthegroundtruth
6Wedefinethatanelicitationsessionissuccessfulifmorethan50%oftheinvestor’s
ranking(seeSection4.2),reportedinTable4row1.Asweexpect, preferenceswerecorrectlycaptured
292

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
Table5:Averageparticipantusers’responsetoadvisorassessmentquestionnaireunderdifferentadvisorconditions.Columns
labeledwithadvisorcondition(Baseline,+Pers.,+Cons.,+Extr.)containa7-pointLikertscale(higherisbetter).“p”column
containsWilcoxonsigned-ranktestp-valuesfor(RQ2)Baselinevs.+Personalized(Pers.),and(RQ3)+Conscientious(Cons.)vs.
+Extroverted(Extr),forboththefulldata(All)andthesubsetwheretheelicitationaccuracyisabove0.5.“SuccessfulElicitation”
referstothesubsetwhereelicitationaccuracywas≥0.5.ForRQ2,thissubsetconsistsofpairsforwhich+Perselicitationis
successful,whileforRQ3,itconsistsofpairsforwhichboth+Extrand+Conselicitationaresuccessful.Boldfaceindicates
significanteffectswith†for𝑝 <0.1and‡for𝑝 <0.05.
(RQ2)Baselinevs.+Personalized (RQ3)+Conscientiousvs.+Extroverted
All SuccessfulElicitation All SuccessfulElicitation
ResponseDimension Baseline +Pers. p Baseline +Pers. p +Cons. +Extr. p +Cons. +Extr. p
PerceivedPersonalization 5.759 5.724 0.838 5.762 5.905 0.751 5.500 5.500 0.663 5.588 5.706 0.941
EmotionalTrust 5.103 5.241 0.446 5.143 5.333 0.537 5.038 5.154 0.600 4.706 5.235 0.034‡
TrustinCompetence 5.690 5.690 0.817 5.810 5.857 0.782 5.962 6.077 0.538 6.000 6.000 1.000
IntentiontoUse 5.310 5.483 0.505 5.429 5.714 0.166 4.885 5.462 0.005‡ 4.941 5.588 0.013‡
PerceivedUsefulness 5.241 5.517 0.183 5.381 5.810 0.194 5.423 5.538 0.425 5.176 5.118 0.968
OverallSatisfaction 5.345 5.690 0.116 5.429 5.810 0.098† 5.269 5.577 0.179 5.118 5.529 0.244
InformationProvision 5.517 5.966 0.026‡ 5.714 6.143 0.053† 5.692 5.654 0.953 5.588 5.765 0.490
focusingontheRQ2-Allcolumns,i.e.comparingthebaselineand extrovertedpersonalityandaconscientiouspersonality.7While
personalizedvariants.Theimportantobservationtonotehereis wecouldconsiderthepersonalizedLLM-advisordiscussedinSec-
thattheparticipantpreferencescoresforbothvariantsarestatis- tion5.2asathirddistinctpersonality(thebaseLLMpersonality
ticallyindistinguishable,exceptunderthequalityofinformation oftheLLM),weshallnotcompareitwithourpersonality-injected
provisioncriteria.Thismeansthatourparticipantscannottellif models,becausedifferentsetsofparticipantswereusedintheper-
theLLM-advisorispersonalizingtothem,andtrusttheworseagent sonalizationstudyandtheadvisor-personastudy.
justasmuchasthebetterone.Furthermore,ifweconsiderthebest
casescenariowherethepreferenceelicitationwassuccessful(RQ2 5.3.1 Decision-makingEffectiveness: Wefirstexaminetheimpact
SuccessfulElicitationcolumns)weobservethesamepattern,even ofaddingpersonalitytotheadvisorsonthedecision-makingpro-
thoughthedifferencebetweenthebaselineandthepersonalized cess,bymeasuringthecapacityoftheparticipantstocorrectlyrank
variantsintermsoftheeffectithasontheparticipantdecision- theassets(aspreviouslydoneinSection5.2).Asaprimarymetric,
makingismorepronounced.Thisunderlinesoneofthecorerisks weagainusetheaverageSpearman’sRhocorrelationbetweenthe
ofusingLLM-advisorsinthefinancialdomain;sinceourusersare investorrankingandthegroundtruthrankingreportedinTable4
inherentlyinexperttheylackthefundamentalskillstojudgeto rows3(extrovertedadvisor)androw4(conscientiousadvisor).
whatextenttheLLMisprovidinggoodadvice,meaningthatthere Wefirstobservetheresultsforthefullsetofparticipantsin
isnosafetynetiftheLLMmakesamistake. theuserstudy.Interestingly,weobserveadifferencebetweenthe
twoadvisors,withtheconscientiousLLM-advisorprovidingbetter
ToanswerRQ2,ourresultsshowthatapersonalizedLLM-advisor guidancethantheextrovertedone(0.26vs.0.122).Thisobservation
isabletoprovideusefulfinancialadvicewhenithasaccuratein- isconsistentwhenwerestrictouranalysistothosecaseswherethe
formationregardingthepreferencesoftheinvestor.Thisisdemon- preferenceelicitationissuccessful.While,expectedly,theeffective-
stratedbybetterdecision-makingcapabilitybyparticipantsusing nessofbothadvisorsimproveswhentheelicitationissuccessful
thepersonalizedadvisorincomparisontothenon-personalizedone. (0.243vs.0.122inthecaseoftheextrovertedadvisorand0.365vs.
However,wealsoidentifiedtwoimportantchallengestoadoption. 0.26inthecaseoftheconscientiousone),theconscientiousadvisor
First,theimpacttheLLM-advisorhasisstronglytiedtothequality hasanadvantageovertheextrovertedone(0.365vs.0.26).
ofthepreferenceelicitationdataprovided,wherepoorpreference Theseresultshighlightthatprovidingdifferentpersonalitiesto
elicitationwillcausetheagenttoactivelydirecttheinvestortothe anLLM-advisorcannotablyimpactthecapacityoftheadvisorto
wrongassets.Second,whiletheparticipantswerepositiveregard- provideusefulinformationtotheinvestors.
ingtheLLM-advisorsacrossallquestionnairecriteria,theywere
notabletoconsistentlytellthedifferencebetweengoodandbadad- 5.3.2 ParticipantAssessmentoftheAdvisor: Wehaveobservedso
visors;leadingtoanincreasedriskofhumansactingonbadadvice. farthattheuseofdifferentpersonalitiesaffectstheuserdecision-
makingprocess.Buthowdothesepersonalitiesaffecttheperception
5.3 RQ3:Effectivenessofpersonalities thatusershaveoftheLLM-advisor?WeobservethisinTable5,in
termsofthesevendimensionscapturedduringtheadvisorassess-
OncewehaveconfirmedtheutilityofpersonalizationforLLM-
mentquestionnaire.
advisors,wenowstudytheeffectthatthepersonalityoftheadvisor
WefirstlookattheRQ3-Allcolumns,comparingthetwoper-
hasonusers’financialinformation-seeking.Aspreviousstudies
sonalities.Notably,forthemajorityofthedimensions,usersbarely
haveshown[29],chatbotpersonalitycanaffectthewayhumans
distinguishbetweenbothsystems.Theonlyanswerwhereweob-
interactwiththechatbot,andthereforeaffecttheeffectivenessand
serveastatisticallysignificantdifferenceistheintentiontousethe
perceptionofLLM-advisors.Tounderstandwhetherpersonality
affectsLLMfinancialadvisors,wecomparetwopersonalizedLLM-
advisorsonwhichwehaveinjectedapre-definedpersonality:an 7RefertoSection3.3forafulldescriptionofeachpersonality.
293

AreGenerativeAIAgentsEffectivePersonalizedFinancialAdvisors? SIGIR’25,July13–18,2025,Padua,Italy
systeminthefuture.Surprisingly,despiteprovidingworseguid- 0.035
ancetotheinvestor,participantsexpressedahigherinterestin 0.030
usingtheextrovertedadvisorthantheconscientiousone.Whenwe 0.025
limitourstudytothoseparticipantswhoexperiencedasuccessful 0.020
preferenceelicitationinbothadvisorvariants,thisissueisstressed, 0.015
asthoseusersalsodevelopasignificantlygreateremotionaltrust 0.010
withtheextrovertedadvisor.
0.005
Theseobservationsareworrisome,astheyrevealthattheper-
0.000 Positive Negative Uncertainty
sonalityofafinancialadvisorcannotonlyaffectthequalityofthe
advicebutalsoleadtheinvestorstotrustmoreonthosesystems
providingworseadvice.
5.3.3 Differencesinlanguage: Tofurtherunderstandhowperson-
alitiesaffectfinancialadvisory,weanalyzethedifferencesinthe
linguisticpatternsprovidedbyextrovertedandconscientiousad-
visors. Analyzingparticipants’reportedoverallexperiencefrom
theexitquestionnairesintheadvisorpersonastudy,over20%(7
of 31) described the extroverted advisor as clear, assertive, and
cheerful while perceiving the conscientious advisor as straight-
forward,analytical,yetlessconfident.8Therefore,toquantifythe
linguisticdifferencesintheadvisors,weconductafinancialsen-
timentanalysisoftheutterancesgeneratedbyeachadvisor.For
eachutterance,wecounttheoccurrencesofpositive,negative,and
uncertainwordsfromtheLoughranandMcDonaldFinancialSenti-
mentDictionary[19].Wenormalizethesecountsbythelengthof
thesentencesandaveragetheresultsacrossalldialogues.
Figure4showstheresults,showingtheextrovertedsentiment
scoresinblue,andtheconscientiousscoresinorange.Forthethree
sentimentdimensions,differencesbetweenadvisorsarestatisti-
cally significant (Welch’s t-test with𝑝 < 0.01). Figure 4 shows
thatextrovertedadvisorstendtousemorepositivelanguagein
their interactions, while conscientious advisors prefer negative
anduncertaintones.Throughmanualanalysisoftheconversation,
weobservethatthisresultsintheextrovertedadvisorfocusing
onthepositiveaspectsofinvestmentswhileoverlookingserious
drawbacks,whereastheconscientiousadvisorprovidesamorebal-
ancedviewoftheassets.Becauseofthis,participantsguidedby
conscientiousadvisorsmaymakemorewell-informedfinancialde-
cisions.Meanwhile,thepositivityoftheextrovertedadvisorseems
moreappreciatedbytheusers,whichisreflectedinhigheradvisor
assessmentscoresfromthepost-discussionquestionnaire.
ToanswerRQ3, ourresultsshowthatdifferentpersonalitiesof
apersonalizedLLM-advisorcanaffecttheutilityoftheprovided
advice.Thisisdemonstratedbythebetterdecisionsofthestudy
participantswhenusinganadvisorwithaconscientiousperson-
alitythanwhenusinganadvisorwithanextrovertedpersonality.
Moreover,thepersonalityoftheadvisoraffectstheperceptionof
humanstowardsthesystem,andithastheriskofleadinginvestors
tofurthertrustthosesystemsthatprovideworseadvice.
6 Conclusion
Inthispaper,wehaveconductedalab-baseduserstudytoexamine
howeffectivelargelanguagemodelsareasfinancialadvisors.We
focusonthreecorechallenges:preferenceelicitation,investment
personalization,andadvisorpersonality.
8Participantswereunawareofthespecificpersonasduringthestudy.
serocS
tnemitneS
egarevA
Extroverted
Conscientious
Figure4:Averagesentimentscoresbyadvisorpersonality.
Errorbarsindicatethestandarddeviation.
First,ouranalysisshowsthatLLMsareeffectivetoolsforprefer-
enceelicitationthroughconversation.Inamajorityofcases,they
arecapableofobtaininginvestor’spreferenceswithanaccuracy
closetoorequivalenttothatofanexperthumanadvisor.How-
ever,therearesomeclearfailurecases,asLLMsarevulnerableto
contradictorystatementsandhallucinations,which,inthecaseof
complexinvestorprofiles,candecreasetheaccuracyoftheelicita-
tiontorandomlevels.AlthoughLLMsarepromisingforelicitation,
inacomplexdomainlikefinance,investorsdonotalwaysfullyun-
derstandtheirownpreferences(ortheyhavedifficultiesexpressing
them).Therefore,futureworkshouldexplorethedevelopmentof
LLM-advisorscapableofresolvingconflictinguserneeds.
Second,personalizingLLMstoprovideinvestmentadvicecan
improvethedecisionsmadebytheinvestors,butonlywhenthe
personalizedLLM-advisorreceivesaccurateinformationaboutthe
investor’spreferences.Ifthepreferenceelicitationisnotsuccessful,
theagentactivelydirectstheinvestorstothewrongassetsonwhich
toinvest.Thisunderscoreshowcrucialagoodpreferenceelicitation
isforprovidingusefulfinancialadvice.
Finally,ourresultssuggestthatinvestorsarenotnecessarily
aware of what constitutes good financial advice, and therefore,
arevulnerabletoactingonbadadviceprovidedbyLLMs.Inthe
comparisonbetweenanon-personalizedandapersonalizedLLM-
advisor,althoughthepersonalizedsystemledtobetterdecisions,
participantswereunabletodistinguishbetweenthesystems.More
worryingly,whencomparingtwopersonalizedadvisorswithex-
trovertedandconscientiouspersonalities,weobservedthat,even
thoughtheextrovertedadvisorprovidedlower-qualityadvice,par-
ticipantstrustedthisadvisormorethantheconscientiousone.
Ourfindingshighlightthat,whilepersonalizedLLM-advisors
representapromisingresearchdirection,theiruseinhigh-stakes
domainslikefinanceisnotfreeofrisks:duetothelimitationsof
LLMsatcapturingcomplexinvestmentpreferences,andthediffi-
cultyofinvestorstodiscernwhethertheadvicetheyreceivetruly
servestheirinterests,LLMshaveanotablerisktodriveinvestors
tobadfinancialassets(leadingnotonlytoalowsatisfactionbut
alsotopotentiallylargemonetarylosses).However,thesedraw-
backsopeninterestingresearchdirectionsnotonlyfromasystem
perspective,butalsofromahuman-centeredapproach:automated
advisorydevelopmentwherewedonotjustfocusonimprovingthe
qualityofautomatedsystemstoguideinvestors,butalsoonhow
theinvestorswilladopt,trustandinteractwiththeseAIagents[5].
Acknowledgments
ThisworkwassupportedbyDaiwaSecuritiesGroupInc.
294

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
References
[25] OscarSainz,JonCampos,IkerGarcía-Ferrero,JulenEtxaniz,OierLopezdeLacalle,
[1] JamesE.Allen,CurryI.Guinn,andEricHorvtz.1999.Mixed-initiativeinteraction. andEnekoAgirre.2023. NLPEvaluationintrouble:OntheNeedtoMeasure
IEEEIntelligentSystemsandtheirApplications14,5(1999),14–23. LLMDataContaminationforeachBenchmark.InFindingsoftheAssociationfor
[2] AshayArgal,SiddharthGupta,AjayModi,PratikPandey,SimonShim,andChang
ComputationalLinguistics:EMNLP2023,HoudaBouamor,JuanPino,andKalika
Choo.2018. Intelligenttravelchatbotforpredictiverecommendationinecho Bali(Eds.).AssociationforComputationalLinguistics,10776–10787.
platform.In2018IEEE8thAnnualComputingandCommunicationWorkshopand [26] TetsuyaSakai.2018. Laboratoryexperimentsininformationretrieval. The
Conference(CCWC2018).IEEE,176–183. informationretrievalseries40(2018),4.
[3] WanlingCai,YuchengJin,andLiChen.2022.Impactsofpersonalcharacteristics [27] JavierSanz-Cruzado,EdwardRichards,andRichardMcCreadie.2024.FAR-AI:A
onusertrustinconversationalrecommendersystems.InProceedingsofthe2022 ModularPlatformforInvestmentRecommendationintheFinancialDomain.In
CHIConferenceonHumanFactorsinComputingSystems(CHI2022).Article489, Proceedingsofthe46thEuropeanConferenceonInformationRetrieval(ECIR2024),
14pages.
PartV.Springer-Verlag,267–271.
[4] GaryCharness,UriGneezy,andAlexImas.2013.Experimentalmethods:Eliciting [28] YunfanShao,LinyangLi,JunqiDai,andXipengQiu.2023. Character-LLM:
riskpreferences.JournalofEconomicBehavior&Organization87(2013),43–51. ATrainableAgentforRole-Playing.InProceedingsofthe2023Conferenceon
[5] ErinK.ChiouandJohnD.Lee.2023.Trustingautomation:Designingforrespon-
EmpiricalMethodsinNaturalLanguageProcessing(EMNLP2023).Associationfor
sivityandresilience.Humanfactors65,1(2023),137–165. ComputationalLinguistics,13153–13187.
[6] KonstantinaChristakopoulou,FilipRadlinski,andKatjaHofmann.2016.Towards [29] TuvaLundeSmestadandFrodeVolden.2019.Chatbotpersonalitiesmatters:im-
conversationalrecommendersystems.InProceedingsofthe22ndACMSIGKDD provingtheuserexperienceofchatbotinterfaces.In5thInternationalConference
internationalconferenceonknowledgediscoveryanddatamining(KDD2016). InternetScience:(INSCI2018).Springer,170–181.
815–824. [30] DavidJStreich.2023. Riskpreferenceelicitationandfinancialadvicetaking.
[7] BerardinaDeCarolis,MarcodeGemmis,PasqualeLops,andGiuseppePalestra.
JournalofBehavioralFinance24,3(2023),259–275.
2017.Recognizingusersfeedbackfromnon-verbalcommunicativeactsincon- [31] YuemingSunandYiZhang.2018. Conversationalrecommendersystem.In
versationalrecommendersystems.PatternRecognitionLetters99(2017),87–95. Proceedingsofthe41stInternationalACMSIGIRConferenceonResearchandDe-
[8] EugeneFFamaandKennethRFrench.1998.Valueversusgrowth:Theinterna-
velopmentinInformationRetrieval(SIGIR2018).235–244.
tionalevidence.Thejournaloffinance53,6(1998),1975–1999. [32] TakehiroTakayanagi,Chung-ChiChen,andKiyoshiIzumi.2023.Personalized
[9] ChristianHildebrandandAnoukBergner.2021.Conversationalroboadvisors
DynamicRecommenderSystemforInvestors.InProceedingsofthe46thInter-
nationalACMSIGIRConferenceonResearchandDevelopmentinInformation
assurrogatesoftrust:onboardingexperience,firmperception,andconsumer
financialdecisionmaking. JournaloftheAcademyofMarketingScience49,4 Retrieval(SIGIR2023).AssociationforComputingMachinery,2246–2250.
(2021),659–676. [33] TakehiroTakayanagi,KiyoshiIzumi,AtsuoKato,NaoyukiTsunedomi,andYuk-
[10] DietmarJannach,AhtshamManzoor,WanlingCai,andLiChen.2021.Asurvey inaAbe.2023.PersonalizedStockRecommendationwithInvestors’Attention
onconversationalrecommendersystems.Comput.Surveys54,5(2021),1–36. andContextualInformation.InProceedingsofthe46thInternationalACMSIGIR
[11] GuangyuanJiang,ManjieXu,Song-ChunZhu,WenjuanHan,ChiZhang,and
ConferenceonResearchandDevelopmentinInformationRetrieval(SIGIR2023).
YixinZhu.2024.Evaluatingandinducingpersonalityinpre-trainedlanguage AssociationforComputingMachinery,3339–3343.
models.InProceedingsofthe37thConferenceonNeuralInformationProcessing [34] TakehiroTakayanagi,MasahiroSuzuki,KiyoshiIzumi,JavierSanz-Cruzado,
Systems(NeurIPS2023). RichardMcCreadie,andIadhOunis.2025.FinPersona:AnLLM-DrivenConver-
[12] HangJiang,XiajieZhang,XuboCao,CynthiaBreazeal,DebRoy,andJadKabbara.
sationalAgentforPersonalizedFinancialAdvising.InProceedingsofthe47th
2024.PersonaLLM:InvestigatingtheAbilityofLargeLanguageModelstoExpress
EuropeanConferenceonInformationRetrieval(ECIR2025),PartV.Springer-Verlag,
PersonalityTraits.InFindingsoftheAssociationforComputationalLinguistics: 13–18.
NAACL2024.3605–3627. [35] JohanneR.Trippas,SaraFahadDawoodAlLawati,JoelMackenzie,andLuke
[13] FrancisM.KinniryJr.,ColleenM.Jaconetti.,MichaelA.DiJoseph.,YanZilbering., Gallagher.2024.WhatdoUsersReallyAskLargeLanguageModels?AnInitial
DonaldG.Bennyhoff.,andGeorginaYarwood.2020. Puttingavalueonyour LogAnalysisofGoogleBardInteractionsintheWild.InProceedingsofthe47th
value:QuantifyingVanguardAdviser’sAlphaintheUK.TechnicalReport.The InternationalACMSIGIRConferenceonResearchandDevelopmentinInformation
VanguardGroup,ValleyForge,Pennsylvania,USA.
Retrieval(SIGIR2024).2703–2707.
[14] SherrieY.X.KomiakandIzakBenbasat.2006. Theeffectsofpersonalization [36] JohanneR.Trippas,LukeGallagher,andJoelMackenzie.2024. Re-evaluating
andfamiliarityontrustandadoptionofrecommendationagents.MISquarterly theCommand-and-ControlParadigminConversationalSearchInteractions.
(2006),941–960.
InProceedingsofthe33rdACMInternationalConferenceonInformationand
[15] IvicaKostric,KrisztianBalog,andFilipRadlinski.2021.Solicitinguserprefer-
KnowledgeManagement(CIKM2024).AssociationforComputingMachinery,
encesinconversationalrecommendersystemsviausage-relatedquestions.In 2260–2270.
Proceedingsofthe15thACMConferenceonRecommenderSystems.724–729. [37] PatcharaVanichvasin.2021.ChatbotDevelopmentasaDigitalLearningTool
[16] KausikLakkaraju,SaraE.Jones,SaiKrishnaRevanthVuruma,VishalPallagani,
toIncreaseStudents’ResearchKnowledge.InternationalEducationStudies14,2
BharathC.Muppasani,andBiplavSrivastava.2023.LLMsforFinancialAdvise- (2021),44–53.
ment:AFairnessandEfficacyStudyinPersonalDecisionMaking.InProceedings [38] XuenaWang,XuetingLi,ZiYin,YueWu,andJiaLiu.2023. Emotionalintel-
ofthe4thACMConferenceonAIinFinance(ICAIF2023).100–107. ligenceoflargelanguagemodels. JournalofPacificRimPsychology17(2023),
[17] CongLi.2016.Whendoesweb-basedpersonalizationreallywork?Thedistinction 18344909231213958.
betweenactualpersonalizationandperceivedpersonalization. Computersin [39] PontusWärnestål.2005.Userevaluationofaconversationalrecommendersystem.
humanbehavior54(2016),25–33. InProceedingsofthe4thWorkshoponKnowledgeandReasoninginPractical
[18] AndrewW.LoandJillianRoss.2024. CanChatGPTPlanYourRetirement?:
DialogueSystems.
GenerativeAIandFinancialAdvice.HarvardDataScienceReview(2024).Issue [40] HamedZamani,JohanneRTrippas,JeffDalton,FilipRadlinski,etal.2023.Con-
SpecialIssue5.
versationalinformationseeking.FoundationsandTrends®inInformationRetrieval
[19] TimLoughranandBillMcDonald.2011.Whenisaliabilitynotaliability?Textual 17,3-4(2023),244–456.
analysis,dictionaries,and10-Ks.TheJournaloffinance66,1(2011),35–65. [41] MarkusZanker,LaurensRook,andDietmarJannach.2019.Measuringtheimpact
[20] RobertR.McCraeandOliverP.John.1992.Anintroductiontothefive-factor ofonlinepersonalisation:Past,presentandfuture. InternationalJournalof
modelanditsapplications.Journalofpersonality602(1992),175–215. Human-ComputerStudies131(2019),160–168.
[21] SouravMedya,MohammadRasoolinejad,YangYang,andBrianUzzi.2022.An [42] YongfengZhang,XuChen,QingyaoAi,LiuYang,andWBruceCroft.2018.
ExploratoryStudyofStockPriceMovementsfromEarningsCalls.InCompanion Towardsconversationalsearchandrecommendation:Systemask,userrespond.
ProceedingsoftheWebConference2022(WWW2022).AssociationforComputing InProceedingsofthe27thACMInternationalConferenceonInformationand
Machinery,20–31.
KnowledgeManagement(CIKM2018).177–186.
[22] PearlPu,LiChen,andRongHu.2011.Auser-centricevaluationframeworkfor [43] HuaqinZhao,ZhengliangLiu,ZihaoWu,YiweiLi,TianzeYang,PengShu,
recommendersystems.InProceedingsofthe5thACMconferenceonRecommender ShaochenXu,HaixingDai,LinZhao,GengchenMai,etal.2024.Revolutionizing
Systems(RecSys2011).157–164. FinancewithLLMs:AnOverviewofApplicationsandInsights.arXivpreprint
[23] FilipRadlinski,KrisztianBalog,BillByrne,andKarthikKrishnamoorthi.2019.
arXiv:2401.11641(2024).
Coachedconversationalpreferenceelicitation:Acasestudyinunderstanding [44] DávidZibriczky.2016.Recommendersystemsmeetfinance:aliteraturereview.In
moviepreferences.InProceedingsofthe20thAnnualSIGdialMeetingonDiscourse Proceedingsofthe2ndInternationalWorkshoponPersonalization&Recommender
andDialogue(SIGDIAL2019).353–360. SystemsinFinancialServices(FinRec2016).1–10.
[24] FilipRadlinskiandNickCraswell.2017. Atheoreticalframeworkforconver- [45] LivZiegfeld,DaanDiScala,andAnitaHMCremers.2025.Theeffectofprefer-
sationalsearch.InProceedingsofthe2ndConferenceonHumanInformation enceelicitationmethodsontheuserexperienceinconversationalrecommender
InteractionandRetrieval(CHIIR2017).117–126. systems.ComputerSpeech&Language89(2025),101696.
295