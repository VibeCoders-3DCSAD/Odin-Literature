---
conversion_metadata:
  converted_at: "2026-07-21T13:34:21Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Huang R. et al.pdf"
  source_pdf_sha256: "84dde4f9a91e373683836e5bb17e90e369f0216dde848991fcf6245fa8dd74c2"
  page_count: 10
  markdown_char_count: 105947
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Wealth-Voyager: Navigating IntelligentWealth Management with
a Multi-Agent Framework
Zimo Zhao
Blockchain and Intelligent
Technology Research Center
The Chinese University of Hong
Kong, Shenzhen
Shenzhen, Guangdong, China
zimozhao@link.cuhk.edu.cn

Rui Huang
Blockchain and Intelligent
Technology Research Center
The Chinese University of Hong
Kong, Shenzhen
Shenzhen, Guangdong, China
rayhuang@cuhk.edu.cn

Siwen Chen
Blockchain and Intelligent
Technology Research Center
The Chinese University of Hong
Kong, Shenzhen
Shenzhen, Guangdong, China
siwenchen@cuhk.edu.cn

Xiaoyu Wu
Independent Researcher
Shenzhen, Guangdong, China
xiaoyuwu5@gmail.com

J. Leon Zhao∗
School of Management and
Economics
The Chinese University of Hong
Kong, Shenzhen
Shenzhen, Guangdong, China
leonzhao@cuhk.edu.cn

Abstract
Rising demand for hyper-personalized wealth management is in-
creasingly unmet by traditional advisory models, which suffer from
limitations in scalability, cost-efficiency, and objectivity. While re-
cent AI-driven solutions show promise, they often remain frag-
mented, focusing on isolated tasks and lacking a unified architec-
ture that integrates long-term strategy with dynamic behavioral
adaptation. To bridge this gap, we introduce Wealth-Voyager,
a multi-agent framework that synergizes strategic asset alloca-
tion with adaptive tactical adjustments. Our system’s architecture
uniquely combines AlphaForge, a quantitative engine for estab-
lishing a long-term strategic portfolio, with DualAdvisor, a novel
Belief-Desire-Intention (BDI) grounded role-playing simulation that
interactively manages user-specific behavioral biases in response
to real-time events. Our proof-of-concept case study, conducted
under live market conditions, demonstrated the efficacy of this
integrated approach. The system’s adaptive tactical adjustments
outperformed a passive baseline, converting a marginal gain into
a more substantial return while reducing portfolio volatility. Our
work presents a blueprint for a new class of financial co-pilots
that integrate quantitative rigor with interactive, cognitively-aware
guidance, enhancing both decision quality and user trust.

CCS Concepts
• Social and professional topics → Economic impact.

∗Corresponding author.

This work is licensed under a Creative Commons Attribution 4.0 International License.
GAIB 2025, Hongkong, China
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1602-7/25/08
https://doi.org/10.1145/3766918.3766944

Keywords
Generative large language models (LLMs), Multi-agent systems,
Behavioral finance, Portfolio optimization, Personalized advisory

ACM Reference Format:
Rui Huang, Zimo Zhao, Siwen Chen, Xiaoyu Wu, and J. Leon Zhao. 2025.
Wealth-Voyager: Navigating IntelligentWealth Management with a Multi-
Agent Framework. In 2025 International Conference on Generative Artificial
Intelligence for Business (GAIB 2025), August 04–06, 2025, Hongkong, China.
ACM, New York, NY, USA, 10 pages. https://doi.org/10.1145/3766918.3766944

1 Introduction
Over the past decade, rising macroeconomic volatility and rapid
fintech innovation have fueled unprecedented demand for hyper-
personalized wealth management solutions. By 2023, global assets
under management (AUM) had reached USD 1.2 trillion [25], yet
an estimated 320 million potential investors remained underserved
by conventional advisory channels. This gap is especially acute
in China, where a burgeoning “new middle class” with rising in-
vestable assets is increasingly seeking technology-enabled financial
guidance. Empirical evidence from 290 Chinese cities shows that
fintech adoption significantly enhances financial access, depth, and
inclusion—particularly benefiting households with lower wealth
and limited access to traditional advisory services [14].

Traditional wealth management frameworks are under growing
pressure to meet the evolving expectations of an increasingly di-
verse and digitally sophisticated investor base. In markets such as
China, the dominance of bank-led fund distribution channels—typically
associated with high fees and limited personalization—further con-
strains access to tailored services, particularly for emerging in-
vestors and the expanding middle class. Beyond structural ineffi-
ciencies, behavioral challenges such as speculative trading, early
fund redemptions, and limited financial literacy remain widespread.
Trust in conventional advisory models is further eroded by inade-
quate transparency and a lack of timely, proactive engagement [13].

---

<!-- PAGE 2 -->

GAIB 2025, August 04–06, 2025, Hongkong, China

Huang et al.

Moreover, most incumbent platforms lack the real-time, behavior-
aware analytics required to support investors during volatile market
conditions, ultimately failing to address both performance-driven
goals and the psychological factors that shape retail investment
behavior [14].

To address these challenges, recent research has increasingly
focused on emerging technologies that enable more adaptive and
investor-centric solutions. Advances in large language models (LLMs)
and multi-agent frameworks offer promising alternatives to con-
ventional financial advisory systems. LLM-based advisors facilitate
personalized, context-aware interactions [21, 27], yet remain costly
to deploy and limited in adaptability [7]. Multi-agent systems im-
prove scalability by distributing financial tasks across specialized
roles [10, 20]. However, most implementations exhibit three key
limitations. First, the lack of behavioral modeling prevents these
systems from accounting for cognitive biases—such as overconfi-
dence or loss aversion—that frequently shape retail investor be-
havior. Second, in the absence of interactive explainability, users
receive opaque recommendations that undermine trust and reduce
engagement. Third, the static nature of their decision logic impedes
real-time responsiveness to market events—an essential capability
for maintaining portfolio relevance in volatile environments.

Given these limitations in existing systems, the choice of an
underlying investment philosophy is critical. We anchor our frame-
work in asset allocation, which financial literature widely recog-
nizes as the cornerstone of long-term portfolio returns, responsible
for over 90% of performance variance [4, 5, 12]. In contrast to more
speculative and volatile strategies like market timing or stock pick-
ing, asset allocation provides a more stable, risk-managed path to
wealth growth through diversification and systematic risk manage-
ment. This philosophy is implemented through two complementary
layers: Strategic Asset Allocation (SAA), which sets the founda-
tional, long-term policy portfolio, and Tactical Asset Allocation
(TAA), which enables dynamic, short-term adjustments to that
policy. The structured yet flexible nature of the SAA-TAA frame-
work makes it an ideal domain for an advisory system that must
also address the critical gaps in behavioral modeling and real-time
adaptiveness.

We present Wealth-Voyager, a behavior-aware, multi-agent
financial advisory framework coordinated by a central LLM-based
meta-controller. The system integrates structured financial signals,
unstructured market narratives, and investor-specific behavioral
traits to deliver adaptive, personalized, and interpretable portfolio
guidance. Through structured function calls and shared memory,
the LLM orchestrates a team of specialized agents responsible for
user profiling, news interpretation, portfolio optimization, and ad-
visory dialogue simulation. By embedding Monte Carlo–based risk
modeling, event-driven rebalancing, and cognitive bias adaptation,
Wealth-Voyager moves beyond static allocation tools. It functions
as an interactive co-pilot, enabling users to understand, trust, and
iteratively refine their financial decisions in dynamic market envi-
ronments.

Key Contributions:
• Modular multi-agent collaboration. WealthVoyager orches-
trates four specialised agents–AssistHub (behavioural profiling),

NewsCrawler (real-time intelligence extraction), AlphaForge
(scenario-aware portfolio optimization), and DualAdvisor (BDI-
based advisory simulation)–to emulate the workflow of elite
investment-research teams.

• Behaviour-aware personalization. Leveraging LLM-based se-
mantic reasoning, AssistHub infers latent client preferences and
cognitive biases, enabling personalised strategies aligned with
individual behavioural profiles that adapt and improve over time.
• Real-time adaptive decision-making. By continuously moni-
toring market dynamics through NewsCrawler and performing
on-the-fly re-optimization in AlphaForge, the system reduces
decision latency, supports timely portfolio rebalancing, and proac-
tively mitigates the impact of black-swan events.

• Bridging the education–decision gap. Through explainable
dialogue and interactive scenario testing, DualAdvisor aligns fi-
nancial education with actionable portfolio choices, empowering
users to develop long-term wealth-management competence.
• Transparency and trust by design. Through scenario-based
analysis, rationale tracing, and verifiable neutral recommenda-
tions, the system reveals its decision-making logic, promotes
financial literacy, and builds user trust in a transparent and ac-
countable manner.
Collectively, WealthVoyager introduces a promising frame-
work that transitions from static asset allocation strategies to an
interactive system capable of delivering personalized, adaptive, and
transparent wealth management at scale.

2 Related Work
2.1 Multi-Agent Frameworks
Multi-agent (MA) frameworks have gained increasing traction in
financial decision-making by distributing portfolio management
tasks among specialized agents, each responsible for subtasks such
as asset selection, market monitoring, or risk control. Recent sys-
tems such as FinCon [29] incorporate large language models (LLMs)
as high-level coordinators across agent teams, facilitating natural
language-based communication and reflective belief revision in
volatile environments. MASA [20] introduces a role-based struc-
ture comprising reward maximizers, risk solvers, and macro ob-
servers, with each agent adapting autonomously through deep rein-
forcement learning. Earlier frameworks, including MAPS [18] and
MSPM [11], emphasized modularity by decoupling strategy genera-
tion from asset evaluation, thereby enhancing diversity and scalabil-
ity. More recent efforts, such as MASS [10] and TradingAgents [28],
simulate collaborative trading desks where LLM-driven agents as-
sume specialized roles—such as sentiment analysis and trade execu-
tion—demonstrating strong performance in high-frequency trading
environments.

While existing systems demonstrate strong specialization, they
often focus on short-term trading or static planning, with lim-
ited support for continuous adaptation or investor-facing educa-
tion. Wealth-Voyager addresses these gaps by enabling persistent,
behavior-aware coordination that evolves with user preferences
and market dynamics. Leveraging real-time news analytics and a
Monte Carlo re-sampling loop, it can anticipate rare but disrup-
tive events such as market shocks. Meanwhile, the DualAdvisor

---

<!-- PAGE 3 -->

Wealth-Voyager: Navigating IntelligentWealth Management with a Multi-Agent Framework

GAIB 2025, August 04–06, 2025, Hongkong, China

module fosters financial literacy through interactive dialogues that
clarify trade-offs, surface biases, and enable scenario-based learn-
ing—shifting the system from execution to long-term investor em-
powerment.

2.2 Large Language Models for Investment

Decision Support

Large language models (LLMs) have become increasingly influential
in financial decision support by enabling contextual understanding,
generation, and interaction across a range of investment-related
tasks. FinLLM [21] applies instruction tuning to provide personal-
ized advice to retail investors, while BloombergGPT [27] demon-
strates the advantages of large-scale, domain-specific pretraining
for tasks such as entity recognition and financial question answer-
ing. LLM-Advisor [16] integrates real-time news summarization
and event interpretation into an interactive advisory workflow, and
LLM-Survey [7] offers a comprehensive overview of how LLMs
support the asset management lifecycle—from information extrac-
tion to portfolio construction. Despite this progress, many existing
systems under-address critical challenges related to probabilistic
uncertainty and behavioral biases in investor decision-making.

Despite recent advances, many LLM-based financial systems still
struggle with behavioral uncertainty, limited transparency, and
high deployment costs. While LLM-Advisor incorporates real-time
data and BloombergGPT scales well for domain coverage, such sys-
tems often operate as single-pass generators without introspection
or adaptive feedback. Wealth-Voyager introduces a cost-efficient,
dialogue-centric interface grounded in behavioral finance, where
a belief–desire–intention (BDI) framework supports explainable,
bias-aware recommendations. By simulating advisor–client interac-
tions, the system uncovers cognitive biases and promotes reflective
decisions through transparent strategy rationales.

2.3 Traditional and Behaviour-Aware

Approaches to Portfolio Optimization
Traditional portfolio optimization techniques, such as mean–variance
analysis and Conditional Value at Risk (CVaR), remain founda-
tional to financial planning [9]. Monte Carlo simulation (MCS)
has further enabled probabilistic outcome estimation, although
early implementations are generally offline and single-pass. MCS-
Interactive [3] introduces conversational simulation, while our sys-
tem (see AppendixA.3) advances this line by supporting custom
asset universes and user-defined risk thresholds, coupled with an
LLM-driven re-sampling loop for adaptive portfolio generation.

Beyond numerical optimization, behavior-aware systems in-
corporate cognitive biases—such as loss aversion and overcon-
fidence—that influence real-world investor decisions. Cognitive-
Aware Advisors [6, 8] demonstrate that embedding behavioral pro-
filing improves trust and engagement. Our approach adopts a nine-
dimensional bias vector (see Appendix A.2) to guide LLM-based
advisory dialogue, aligning with findings from Trust-Aware GAI
Advisors [26] on personalized, trust-sensitive interaction.

3 Framework
3.1 Overall Architecture
To provide personalized and real-time financial advisory services
for individual users, we propose an end-to-end framework named
Wealth-Voyager. As illustrated in Fig. 1, the system integrates
multiple collaborating agents that dynamically interact with core
tools, including an intelligent customer assistant, a news crawler,
and portfolio optimization models. In addition, a role-playing dia-
logue module that employs a dual-agent, role-playing simulation
to deliver adaptive guidance that is responsive to both real-time
market events and the user’s unique behavioral profile.

3.2 Core Modules
AssistHub is an intelligent customer service module, implemented
as an agentic workflow on the Dify [17] platform and powered
by ChatGPT-4 [1]. Through a guided conversational process of
context-aware, adaptive testing and interactive calibrationdynamic,
it dynamically handles general inquiries and assists users in articu-
lating their wealth management goals (e.g., retirement savings, edu-
cational funds), detailing their current financial status, and complet-
ing a personalized risk assessment. AssistHub replaces the "static
questionnaire" with a guided multi-round dialogue mechanism to
comprehensive user profile. This profile, which encapsulates the
user’s financial status, long-term goals, and risk tolerance, serves
as a foundational input required by the other specialized modules
within the Wealth-Voyager framework to deliver personalized
analysis and advice.

NewsCrawler operates as a dedicated Model Context Proto-
col(MCP) [22] server responsible for the real-time aggregation
and processing of market information from a wide array of on-
line sources. This module serves two critical functions within the
Wealth-Voyager framework. Firstly, it periodically extracts ex-
pected return forecasts for major asset classes from research reports
published by professional financial institutions. This data provides
the AlphaForge module with realistic and timely inputs, signif-
icantly enhancing the practical applicability and accuracy of the
portfolio optimization algorithms. Secondly, NewsCrawler curates
and retrieves daily market news tailored to each user’s specific
profile, including their stated investment interests, risk tolerance,
and existing portfolio composition. This personalized news feed
serves as the foundational context for the role-playing dialogues
within the DualAdvisor module.

AlphaForge is the quantitative core of Wealth-Voyager which
is based on morden portfolio theory. Drawing on market expec-
tations (returns, volatilities, and cross-asset correlations) continu-
ously harvested by NewsCrawler and the investor-specific con-
straints produced by AssistHub, it constructs a long-term strategic
asset-allocation that balances growth, risk, and liquidity. Internally,
AlphaForge employs a constrained mean–variance engine aug-
mented with liquidity caps, draw-down limits, and leverage con-
trols. The solver outputs target weights alongside forward-looking
metrics—projected return, volatility, Value-at-Risk, and liquidity
coverage—that feed downstream advisory logic. The full math-
ematical specification and optimization routine are provided in
Appendix A.3

---

<!-- PAGE 4 -->

GAIB 2025, August 04–06, 2025, Hongkong, China

Huang et al.

Figure 1: The architecture of the proposed Wealth-Voyager framework.

DualAdvisor module utilizes a novel role-playing framework
powered by two distinct large language model (LLM) agents, which
simulate consultations between a professional investment advisor
and the user. The primary purpose of this module is to generate
real-time, tactical investment advice. By dynamically modeling
advisor-client interactions in response to market events, DualAd-
visor provides actionable recommendations that help users make
timely portfolio adjustments to navigate market volatility effec-
tively.

3.3 Role-Playing-Based Advisory Simulation
Traditional financial advisory systems typically rely on static user
profiles, which fail to capture the dynamic interplay between evolv-
ing market conditions and an investor’s real-time cognitive and
emotional responses [24]. To address this limitation, we propose
DualAdvisor, a role-playing module within Wealth-Voyager, de-
signed to simulate multi-turn, psychologically informed dialogue
between a professional advisor and a digitally modeled client. The
objective is to move beyond static recommendations by generat-
ing advisory responses that are both responsive to market signals
and adaptive to user-specific behavioral biases. This is achieved
through an agent-based interaction between two large language
model (LLM) agents, grounded in a behaviorally rich user profile.

3.3.1 Agent Roles and Dialogue Objectives. To effectively simulate
complex financial decision-making, we decompose the advisory
interaction into two specialized agent roles, inspired by recent
developments in social-agent simulation [19].

• Advisor Agent: Acts as the rational anchor. It interprets
market developments with professional neutrality and proac-
tively detects behavioral biases reflected in the user’s re-
sponses. For example, it may caution against overreaction to
news due to high policy sensitivity or discourage impulsive
“gain-chasing” behavior. The Advisor continuously steers
the dialogue toward strategies consistent with the user’s
stated long-term financial goals.

• User Agent: Serves as a high-fidelity "digital twin" of the
user, designed to inject psychologically plausible, and often
biased, human behavior into the simulation. Its purpose is
not to be perfectly rational but to realistically model how a
specific individual would react to market changes based on
their unique financial circumstances, goals, and behavioral
tendencies.

Each agent is instantiated using role-specific system prompts. The
User Agent prompt dynamically incorporates the complete user
profile, including financial goals, risk tolerance, and quantified
behavioral attributes, thereby ensuring psychologically coherent
and context-aware responses.

This dual-agent design fulfills two complementary objectives.
Firstly, it generates personalized, bias-aware investment guidance
by anticipatorily modeling the user’s likely emotional reactions.
Secondly, the recorded conversation acts as a “behavioral mirror”
for investor education, enabling users to observe how professional
reasoning can mitigate their own cognitive distortions, thereby
enhancing their financial self-awareness over time.

---

<!-- PAGE 5 -->

Wealth-Voyager: Navigating IntelligentWealth Management with a Multi-Agent Framework

GAIB 2025, August 04–06, 2025, Hongkong, China

3.3.2 BDI-Grounded Behavioral Profile. To enable realistic simu-
lation, we construct a comprehensive user profile that serves as a
behavioral fingerprint. Drawing from behavioral economics, this
profile extends beyond conventional data by quantifying a range of
user-specific biases. These are broadly categorized into emotional
indicators (e.g., loss aversion, overconfidence), which model the
user’s core feelings about risk and security, capturing the affective
responses under market stress that often drive intuitive decisions,
and cognitive indicators (e.g., herding tendency, policy sensitiv-
ity), which simulate how the user processes market information and
forms judgments, reflecting their systematic patterns of reasoning.
To operationalize this behavioral profile within the User Agent,
we model its internal deliberation using the Belief–Desire–Intention
(BDI) framework, a well-established paradigm for rational agency
that mirrors human practical reasoning. This structure sequentially
models the agent’s:

• Beliefs (B): Its subjective understanding of the current mar-

ket.

• Desires (D): Long-term investment goals and emotional

inclinations derived from the user profile.

• Intentions (I): Actionable steps proposed for portfolio ad-

justment.

We operationalize BDI reasoning via a step-wise prompting mech-
anism: the LLM is sequentially queried for its beliefs, desires, and
intentions in response to new market information. This chain-of-
thought design improves both the logical consistency and inter-
pretability of the simulated decision process.

3.3.3 Dialogue Flow and Consensus Mechanism. The agent inter-
action unfolds as a structured, multi-turn consultation designed to
transform a user’s potential biased reactions into a reasoned action
plan. The dialogue progresses through four distinct phases:

• Rational Initialization: The Advisor Agent synthesizes
daily market news through the lens of the user’s profile to
formulate a scenario-specific interpretation. This interpreta-
tion serves as the initial prompt, triggering the User Agent’s
BDI reasoning process.

• Behavioral Response: The User Agent then generates its
initial BDI response, surfacing the user’s likely first reaction,
complete with any possible biases.

• Cognitive Debiasing: The Advisor Agent critiques this
response, identifies irrational patterns based on the user’s
profile, and recommends alternative, goal-aligned plans.
• Iterative Consensus: The agents engage in an iterative dia-
logue. The User Agent either revises its intentions based on
the Advisor’s feedback or defends its position to prompt fur-
ther clarification. The dialogue terminates when a consensus
is reached, governed by a pragmatic mechanism: either the
Advisor generates a specific agreement phrase (e.g., "Agree,
no modification needed") or a predefined maximum of ten
rounds is reached.

suggestions derived from the consensus, and key areas of focus for
the near future.

4 User Study
To evaluate the practical effectiveness and decision-support capabil-
ities of the Wealth-Voyager system, we conducted a month-long
pilot study from April 2 to May 2, 2025. The study involved a
mid-career participant focused on retirement planning and aimed
to simulate realistic investment scenarios under live market con-
ditions. During this period the system was fully deployed in a
sandbox environment, enabling end-to-end validation of its core
modules—including behavioural profiling, adaptive rebalancing,
and agent-driven market response.

Importantly, the experiment coincided with a period of elevated
geopolitical and financial uncertainty, marked by a sharp escala-
tion in global trade tensions. This provided a natural stress-test
for evaluating how Wealth-Voyager responds to volatile market
events.

The study focus on the quantitative performance (e.g. returns
and volatility) of both Strategic Asset Allocation (SAA), which based
on long-term investment goals and Tactical Asset Allocation (TAA),
which based on SAA and dynamically adjusted according to short-
term market signals (such as policy changes, macroeconomic data),
and qualitative user experience offering an integrated view of the
robustness, adaptability, and usability of our system.

4.1 Participant Profile
The case involves a 45-year-old professional planning to retire
within eight years, with the objective of growing investable assets to
support a comfortable post-retirement lifestyle. During onboarding,
the user reported substantial wealth and moderate liquidity require-
ments but did not specify key parameters such as risk tolerance or
return objectives. The initial portfolio allocation (Table 1a) includes
a 20% concentration in real estate investment trusts (REITs)—an
unusually high exposure for a balanced portfolio—introducing liq-
uidity constraints and limiting diversification.

Onboarding interactions revealed three primary concerns: (i)
mitigating large drawdowns near retirement, (ii) maintaining ac-
cess to capital within six months for potential obligations, and
(iii) receiving clear, rationale-driven investment guidance. These
concerns informed the system’s evaluation criteria, emphasizing
drawdown control, risk-adjusted performance, and interpretability.
In contrast to conventional systems that provide static recom-
mendations or opaque optimizations, Wealth-Voyager inferred
latent preferences and applied a structured, investment-bank-style
workflow to revise the portfolio. The resulting allocation (Table 1b)
improved diversification and more closely aligned with the user’s
implicit risk profile—demonstrating Wealth-Voyager’s capacity to
translate vague financial goals into actionable, personalized invest-
ment strategies.

The entire interaction culminates in a final, user-facing deliver-
able: the Daily Investment Briefing. This structured report summa-
rizes the essence of the dialogue, providing the user with a clear
and actionable summary that includes a market overview, the Ad-
visor Agent’s tailored interpretation, concrete portfolio adjustment

4.2 System Operation
To ensure timely adaptation to market shifts, the system continu-
ously scraped macroeconomic news and monitored real-time asset
prices. The AlphaForge firstly implements Strategic Asset Alloca-
tion (SAA) by optimizing long-term weights under constraints such

---

<!-- PAGE 6 -->

GAIB 2025, August 04–06, 2025, Hongkong, China

Huang et al.

Table 1: Comparison between user-declared baseline profile and AI-optimised allocation.

Attribute

Initial capital
Target amount
Risk tolerance
Leverage allowed
Liquidity need
Strategic asset mix

Expected return
Expected volatility

User-declared (Apr 2, 2025)

AI-optimised (DualAdvisor)

RMB 3,000,000
RMB 4,500,000+
N/A
No
Medium
A-shares 30%, Bonds 35%,
Gold 15%, REITs 20%
N/A
N/A

RMB 3,000,000
RMB 4,500,000+
Medium (max loss 20%)
No
Medium
A-shares 35.3%, Bonds 41.1%,
Gold 17.6%, REITs 6.0%
6.53%
9.42%

Notes. “A-shares” are RMB-denominated equities on mainland Chinese exchanges; “Bonds” are fixed-income securities; “Gold” includes physical bullion or ETF exposure;
“REITs” are real-estate investment trusts. N/A = not provided at onboarding.

as maximum drawdown thresholds. Addtionally, the NewsCrawler
module generated personalised briefings and contextual interpre-
tations tailored to the participant’s portfolio exposures. Upon de-
tection of disruptive events—such as unexpected policy shifts or
volatility spikes—the DualAdvisor module assessed potential port-
folio impacts and issued preemptive rebalancing proposals to hedge
downside risk while preserving upside potential and also employs
Tactical Asset Allocation (TAA) to adjust positions in response to
real-time market events with the algorithm in the AlphaForge.

On April 2, 2025, a sudden tariff shock (a minor “black-swan”
event) was detected. Tactical adjustments were executed prior to
significant market drawdowns. These included a reduction in equity
holdings, increased exposure to gold and government bonds, and a
moderate uptick in REIT allocation. This repositioning enabled the
participant to limit losses and capitalise on short-term mispricings.

4.3 Performance Across Portfolio Strategies
Figure 2 compares segment-level returns of passive and tactical port-
folios from April 2 to May 9, 2025. Following a tariff-induced shock
(Apr 02–Apr 09), the tactical approach reduced losses (−2.56% vs.
−2.79%). In the rebound phase (Apr 09–Apr 23), it captured greater
upside (3.24% vs. 2.16%). Across subsequent intervals, tactical re-
turns remained consistently higher, notably during Apr 30–May 07
(1.15% vs. 0.68%). Even during mild pullbacks (May 07–May 09), the
tactical strategy limited downside more effectively.

These results underscore the advantage of layering Tactical Asset
Allocation (TAA) atop a Strategic Asset Allocation (SAA) frame-
work, enhancing responsiveness without sacrificing stability.

Table 2 compares the performance of three portfolio strategies:
the user-declared baseline (Original), a behaviorally Anchored port-
folio, and a dynamically rebalanced Tactical strategy. Anchoring
alone yields substantial gains, increasing the annual return from
3.72% to 6.53% while nearly halving annualised volatility (from
18.08% to 9.42%).

Building on this foundation, the Tactical strategy delivers fur-
ther improvements. Over the evaluation period, cumulative return
rises from 0.24% to 1.86%, with annual volatility reduced to 12.10%,
outperforming both baseline and Anchored strategies on a risk-
adjusted basis.

These results validate the effectiveness of WealthVoyager’s
layered decision architecture: the integration of strategic behavioral

anchoring with real-time tactical rebalancing achieves superior
returns without increasing risk exposure.

4.4 Comparative Analysis with Existing Market

Solutions

Recent industry analyses highlight the growing adoption of AI-
driven wealth-management systems in China, notably: Ant Group’s
Ant Fortune [2], JD Digits’ JD Xiaobei [15], and Ping An’s Intel-
ligent Wealth Butler [23]. These platforms provide foundational
investment guidance through rule-based allocation and basic user
profiling.

In contrast, Wealth-Voyager was co-developed with a group of
novice and intermediate investors who used it alongside existing
market solutions over a six-week period. Feedback from this real-
world deployment informed the design of key differentiators: real-
time adaptive recommendations, personalized behavioral modeling,
and conversational explanation mechanisms.

Wealth-Voyager not only supports standard investment advi-
sory functions but also introduces novel dimensions that enhance
the user experience. As shown in Table 3, our system outperforms
existing offerings in areas such as dynamic responsiveness, person-
alization depth, and educational engagement — features that users
highlighted as critical for building long-term financial literacy and
confidence.

The comparison reveals that while current mainstream plat-
forms fulfill baseline advisory requirements, they remain limited
in their responsiveness and personalization depth. Users reported
that Wealth-Voyager’s ability to explain investment logic in plain
language and adapt to their evolving preferences significantly im-
proved their engagement and understanding of portfolio manage-
ment.

Wealth-Voyager advances the paradigm by enabling adaptive
intraday asset rebalancing, integrating behavioral finance signals,
and providing interpretable recommendations via dialogue-based
interfaces. These enhancements collectively position it as a more
transparent and responsive co-advisor across diverse investor seg-
ments.

---

<!-- PAGE 7 -->

Wealth-Voyager: Navigating IntelligentWealth Management with a Multi-Agent Framework

GAIB 2025, August 04–06, 2025, Hongkong, China

Figure 2: Segment-level returns for passive and tactical portfolios (April 2–May 9, 2025).

Table 2: Performance comparison across user-declared, anchored, and tactical portfolio strategies.

(a) Original vs. Anchored

(b) Anchored vs. Tactical

Portfolio

Original

Anchored

Annual Return
(%)

Annual
Volatility (%)

3.72

6.53

18.08

9.42

Portfolio

Anchored

Tactical

Cumulative
Return (%)

Annual
Volatility (%)

0.24

1.86

13.70

12.10

Notes. Original: user-declared allocation; Anchored: allocation anchored by behavioral signals via DualAdvisor; Tactical: adaptively rebalanced based on live
market signals.
Annual return = projected yearly gain; cumulative return = total return over the observed period; annual volatility = yearly return dispersion.

Table 3: Capability comparison between Wealth-Voyager and representative market offerings. ✓ = supported; ✗ = absent.

Feature

Ant Fortune

JD Xiaobei

Ping An Butler Wealth-Voyager

Diverse asset-class support
Interactive interface
Real-time dynamic adjustment
Personalized customization
Financial education integration

✓
✓
✗
✗
✗

✓
✓
✗
✗
✗

✓
✓
✗
✗
✗

✓
✓
✓
✓
✓

5 Conclusion
In this paper, we introduced Wealth-Voyager, a novel multi-agent
framework that unifies behavioural profiling, real-time market in-
telligence, and quantitative optimization into a cohesive pipeline.
Through the coordination of four specialized modules—AssistHub,
NewsCrawler, AlphaForge, and DualAdvisor—our system deliv-
ers interactive decision support that moves beyond passive recom-
mendations. This was evidenced by our proof-of-concept deploy-
ment, where the system’s adaptive advice outperformed a passive
baseline by +1.62 pp during a period of elevated macro uncertainty,
and its strategic allocations improved the user’s risk-return trade-
off (+2.81 pp annualized return, −8.66 pp volatility). Qualitative
feedback also indicated that the dual-agent simulation enhances

user trust and self-awareness by exposing cognitive biases in an
explainable dialogue.

Our validation, while promising, has several limitations: the pro-
totype was evaluated on a single user and a limited asset universe,
and its performance is contingent on the underlying LLM. To ad-
dress these gaps and strengthen the robustness of our findings, our
future work will prioritize a multi-faceted evaluation. We plan to
conduct larger, longitudinal studies with a diverse cohort of users
to statistically validate the system’s adaptability across different
behavioral profiles. Furthermore, we will expand the asset uni-
verse, test the framework under varied market regimes to assess its
resilience, and perform systematic benchmarking against state-of-
the-art systems to highlight the advantages of our behavior-aware

---

<!-- PAGE 8 -->

GAIB 2025, August 04–06, 2025, Hongkong, China

Huang et al.

approach. Beyond these evaluations, we also aim to enhance the
core methodology by exploring reinforcement learning to refine
the negotiation dynamics within DualAdvisor and investigating
domain-specific models to improve performance and reduce infer-
ence costs.

By bridging the gap between behavioural finance, quantitative
analysis, and generative AI, Wealth-Voyager charts a viable path
toward the next generation of financial co-pilots. We believe this
work represents a significant step toward more effective, trans-
parent, and trustworthy human-AI collaboration in the complex
domain of wealth management.

Acknowledgments
We gratefully acknowledge the generous financial and computa-
tional support from Prof. Zhao and the Blockchain and Intelligent
Technology Research Center (CBIT). We also extend our sincere
thanks to our industry mentor, Dr. Xiaoyu Wu (formerly of Black-
Rock), for her invaluable insights that shaped this research, and
to Amos Chen and Warren Li of Google Cloud for their helpful
feedback on an early demonstration of our work.

References
[1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Floren-
cia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal
Anadkat, et al. 2023. Gpt-4 technical report. arXiv preprint arXiv:2303.08774
(2023).

[2] Ant Group. n.d.. Ant Fortune - Ant Group. https://www.antfortune.com/. Ac-

cessed: 2025-07-11.

[3] Kousik Barnwal. 2023. User Friendly Portfolio Optimisation Using Monte Carlo
https://medium.com/@indubarnwal752/user-friendly-portfolio-

Simulation.
optimization-using-mcs-5154ff52dc14
[4] Z. Bodie. 1995. Investments. (1995). Book.
[5] Gary P. Brinson, L. Randolph Hood, and Gilbert L. Beebower. 1986. Determinants
of Portfolio Performance. Financial Analysts Journal 42, 4 (1986), 39–44. http:
//www.jstor.org/stable/4478947

[6] Abhijeet Chandra, Arnav Kumar, and Sha Bala. 2025. Cognitive Biases and
Robo-Advisory Adoption: Experimental Evidence. Journal of Behavioral and
Experimental Finance 37 (2025), 100742. doi:10.1016/j.jbef.2024.100742

[7] Xu Dong, Thanos Stratopoulos, and Christina Wang. 2024. Large Language
Models for Financial and Investment Management. The Journal of Portfolio
Management 51, 2 (2024), 211–230. doi:10.3905/jpm.2024.1.350

[8] Kim Sandy Eichler and Elizabeth Schwab. 2024. Evaluating Robo-Advisors
through Behavioral Finance: A Critical Review of Technology Potential, Ra-
tionality, and Investor Expectations. Frontiers in Behavioral Economics 3 (2024),
1489159. doi:10.3389/frbhe.2024.1489159

[9] Financial Edge Training. 2024.

Portfolio Optimisation Explained: Mean–
Variance, CVaR and Beyond. https://www.fe.training/free-resources/portfolio-
optimisation-guide/

[10] Taian Guo, Haiyang Shen, Jinsheng Huang, Zhengyang Mao, Junyu Luo, Zhuoru
Chen, Xuhui Liu, Bingyu Xia, Luchen Liu, Yun Ma, et al. 2025. MASS: Multi-Agent
Simulation Scaling for Portfolio Construction. arXiv preprint arXiv:2505.10278
(2025).

[11] Zhenhan Huang and Fumihide Tanaka. 2022. MSPM: A modularized and scal-
able multi-agent reinforcement learning-based system for financial portfolio
management. Plos one 17, 2 (2022), e0263689.

[12] Roger G. Ibbotson and Paul D. Kaplan. 2000. Does Asset Allocation Policy Explain
40, 90, or 100 Percent of Performance? Financial Analysts Journal 56, 1 (2000),
26–33. http://www.jstor.org/stable/4480220

[13] CFA Institute. 2022. Enhancing Investors’ Trust: 2022 CFA Institute Investor
Trust Study. https://www.cfainstitute.org/sites/default/files/-/media/documents/
article/Enhancing-Investors-Trust-Report_2022_Online.pdf

[14] International Monetary Institute. 2024. China Wealth Management Compe-
https://www.imi.ruc.edu.cn/docs/2024-06/

tency Evaluation Report (2023).
cad95d7db7774df4a82a04bb5c212e8f.pdf.

[15] JD Digits. n.d.. JD Xiaobei - JD Digits. https://jr.jd.com/. Accessed: 2025-07-11.
[16] Kausik Lakkaraju, Sai K. R. Vuruma, Vishal Pallagani, Bharath Muppasani, and
Biplav Srivastava. 2023. Can LLMs Be Good Financial Advisors? An Initial Study
in Personal Finance Decision Making. In Proc. ICAPS FinPlan Workshop. 1–6.

[17] Alex Leatherwood and Vic Matta. 2025. Building AI Applications with Dify. ai:

A Hands-On Workshop. (2025).

[18] Jinho Lee, Raehyun Kim, Seok-Won Yi, and Jaewoo Kang. 2020. MAPS: Multi-
agent reinforcement learning-based portfolio management system. arXiv preprint
arXiv:2007.05402 (2020).

[19] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard
Ghanem. 2023. Camel: Communicative agents for" mind" exploration of large
language model society. Advances in Neural Information Processing Systems 36
(2023), 51991–52008.

[20] Zhenglong Li, Vincent Tam, and Kwan L Yeung. 2024. Developing a multi-agent
and self-adaptive framework with deep reinforcement learning for dynamic
portfolio risk management. arXiv preprint arXiv:2402.00515 (2024).

[21] Xiao-Yang Liu, Guoxuan Wang, Hongyang Yang, and Daochen Zha. 2023. FinGPT:
Democratizing Internet-Scale Data for Financial Large Language Models. arXiv
preprint arXiv:2307.10485 (2023).

[22] Model Context Protocol Initiative. 2024.

Introduction to the Model Context
Protocol. https://modelcontextprotocol.io/introduction. Accessed: 2025-07-11.

[23] Ping An Group. n.d.. Intelligent Wealth Butler - Ping An Group. https://group.

pingan.com/. Accessed: 2025-07-11.

[24] Michael Pompian. 2016. Risk profiling through a behavioral finance lens. CFA

Institute Research Foundation.

[25] Statista Research Department. 2023. Global wealth-management market
size, 2019–2023. https://www.statista.com/statistics/1266189/global-wealth-
management-market-size/. Accessed: 2025-07-07.

[26] Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard McCreadie,
and Iadh Ounis. 2025. Are Generative AI Agents Effective Personalized Financial
Advisors?. In Proc. SIGIR 2025. arXiv:2504.05862.

[27] Shijie Wu, Caolan Slack, Bryan Kelly, Ozan Irsoy, and et al. 2023. BloombergGPT:
A Large Language Model for Finance. arXiv preprint arXiv:2303.17564 (2023).
[28] Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. 2024. TradingAgents: Multi-
Agents LLM Financial Trading Framework. arXiv preprint arXiv:2412.20138 (2024).
[29] Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng, Yuechen Jiang, Yupeng
Cao, Zhi Chen, Jordan Suchow, Zhenyu Cui, Rong Liu, et al. 2024. Fincon: A
synthesized llm multi-agent system with conceptual verbal reinforcement for
enhanced financial decision making. Advances in Neural Information Processing
Systems 37 (2024), 137010–137045.

A Appendix
A.1 Monte-Carlo–Driven Meta-Agent

Algorithm 1 Investment Advisor Loop (simplified)

Require: User config 𝑐0, success threshold 𝜏, max rounds 𝑅

𝑏𝑒𝑠𝑡𝑝 ← 0

𝑏𝑒𝑠𝑡𝑐 ← 𝑐0;

1: 𝑐 ← 𝑐0;
2: for 𝑟 ← 1 to 𝑅 do
3:

𝑝 ← MonteCarloSim(𝑐)
if 𝑝 > 𝑏𝑒𝑠𝑡𝑝 then
𝑏𝑒𝑠𝑡𝑐 ← 𝑐;

𝑏𝑒𝑠𝑡𝑝 ← 𝑝

4:

5:

6:

7:

8:

9:

end if
if 𝑝 ≥ 𝜏 then
break

end if
𝑐 ← LLM_Adjust(cid:0)𝑐, allowed_params(cid:1)

10:
11: end for
12: return (𝑏𝑒𝑠𝑡𝑐, 𝑏𝑒𝑠𝑡𝑝 )

Function Descriptions for Algorithm 1 (Investment Advisor Loop):

• MonteCarloSim(𝑐): runs a Monte Carlo rollout under configu-

ration 𝑐 and returns the success probability estimate.

• LLM_Adjust(𝑐, allowed_params): interacts with an LLM-based
dialogue agent to propose adjustments to the current user con-
figuration 𝑐, subject to a whitelist of allowed parameters.

---

<!-- PAGE 9 -->

Wealth-Voyager: Navigating IntelligentWealth Management with a Multi-Agent Framework

GAIB 2025, August 04–06, 2025, Hongkong, China

Algorithm 2 Construction of Behaviour Vector

Require: Conversation ID 𝑖𝑑; default mapping M (Table 4)

𝐸 ← LLM_ProfileExtract(𝐻 )

1: 𝐻 ← LoadDialogueHistory(𝑖𝑑)
2: if ContainsStructuredBlock(𝐻 ) then
𝐸 ← ParseStructuredBlock(𝐻 )
3:
4: else
5:
6: end if
7: if 𝐸 incomplete then
8:
9: end if
10: 𝑝 ← 𝐸.investment_purpose ⊲ retirement / education / house /

𝐸 ← FillDefaults(𝐸)

growth
11: v ← M [𝑝]
12: v[4] ← 𝐸.real_time_emotion
13: return Dict(keys, v)

A.2 Large-Model–Assisted Behaviour Profiling

Function Descriptions for Algorithm 2 (Behaviour Vector Construc-

tion):
• LoadDialogueHistory(𝑖𝑑): retrieves the entire conversation

history for a given conversation ID.

• ContainsStructuredBlock(𝐻 ): checks if a well-formed, machine-

readable block is present in the dialogue.

• ParseStructuredBlock(𝐻 ): parses a structured block to di-

rectly extract user profile attributes.

• LLM_ProfileExtract(𝐻 ): uses a language model to infer user
attributes from free-form dialogue if no structured block is
found.

• FillDefaults(𝐸): fills missing entries in the extracted profile

vector 𝐸 using predefined default values.

Behavioral Metric Descriptions:
• Loss Aversion: This is an emotional bias where investors tend
to feel the pain of losses more than the pleasure of gains.
• News & Policy Sensitivity: This metric gauges how much
an investor’s decisions are irrationally swayed by immediate
media headlines and policy changes.

• Investment Experience: An investor’s behavior is uncon-
sciously influenced by past experiences, which can provide
more accurate insight into their risk profile.

• Real-Time Emotion: This refers to reasoning influenced by
feelings, which can overpower logical thinking during times of
stress and affect investment decisions.

• Herding Tendency: This is a behavior where investors do not
have their own ideas and instead follow the lead of their friends
and colleagues in making investment decisions.

• Regret Aversion: This is an emotional bias where investors
avoid taking decisive actions because they fear that their chosen
course will prove unwise in hindsight.

• Overconfidence: This is an emotional bias best described as

unwarranted faith in one’s own thoughts and abilities.

• Illusion of Control: This is a cognitive bias where people
believe they can control or influence investment outcomes when
they actually cannot.

• Decision Delay: This is a behavior where investors are slow to
make decisions due to discomfort with uncertainty or putting
off decisions until they receive professional advice.

Table 4: Default Personality Mapping M

Purpose

Vector slice (loss_aversion, . . . , decision_delay)

retirement
child_education
house_purchase
wealth_growth

[0.8, 0.5, 0.8, 0.5, 0.4, 0.8, 0.3, 0.2, 0.6]
[0.7, 0.6, 0.5, 0.5, 0.5, 0.7, 0.4, 0.4, 0.5]
[0.6, 0.7, 0.4, 0.5, 0.6, 0.6, 0.3, 0.3, 0.7]
[0.3, 0.8, 0.6, 0.5, 0.7, 0.3, 0.8, 0.7, 0.3]

A.3 Constraint-Aware Portfolio Optimiser

Algorithm 3 Multi-Stage Optimization Procedure

Require: Mean returns 𝜇, covariance Σ, user config 𝜅
1: Infer target return 𝑟★, vol limit 𝜎max, CVaR limit
2: Derive liquidity tiers, leverage flag and restricted set R
3: Build box bounds 𝑏𝑖 for all assets
4: 𝑤 (0) ← ERC_Init(Σ)
5: 𝑤MS ← closed-form max-Sharpe solution
6: if 𝑤MS feasible and meets all risk caps then
7:
8: end if

return 𝑤MS

⊲ — Stage 1: smooth local search —

9: L (𝑤) ← −Sharpe(𝑤) + 𝜆 IlliqPenalty(𝑤)
10: 𝑤★ ← SLSQP(cid:0)L, 𝑤 (0), 𝑏𝑖, constraints(cid:1)
11: if success then
12:
13: end if

return PostProcess(𝑤★)

⊲ — Stage 2: global repair —

return PostProcess(𝑤 ⋄)

14: 𝑤 ⋄ ← DifferentialEvolution(cid:0)L, 𝑏𝑖, constraints(cid:1)
15: if success then
16:
17: else
18:
19: end if

return FailReport()

Function Descriptions for Algorithm 3 (Multi-Stage Optimization):
• ERC_Init(Σ): returns an equal risk contribution portfolio ini-

tialization given the covariance matrix Σ.

• SLSQP(L, 𝑤 (0), 𝑏𝑖, constraints): applies Sequential Least Squares
Quadratic Programming to locally optimize the objective L
starting from 𝑤 (0) .

• DifferentialEvolution(L, 𝑏𝑖, constraints): applies a global
evolutionary search to optimize L in case the local method
fails.

• PostProcess(𝑤): normalizes and sanitizes a candidate weight

vector before returning it.

• FailReport(): generates a diagnostic message if no feasible

solution is found.

---

<!-- PAGE 10 -->

GAIB 2025, August 04–06, 2025, Hongkong, China

Huang et al.

A.4 Illustrative Case Study: A Tactical Response

Narrative

To illustrate the practical utility of the framework, this appendix
offers a narrative walkthrough of a five-stage tactical response to a
simulated market crisis. The box below summarizes the key events,
corresponding analyses, and portfolio adjustments made at each
stage.

Investment Strategy Review and Outlook

Phase 1: Crisis Response (Apr 2: Tariff Shock)
News: On April 2, the U.S. President announced a "Liberation Day" tariff policy,
triggering a global stock market sell-off.
Analysis: The market experienced a sudden downturn. For a client with a
"retirement" objective, the primary task is to strictly control portfolio drawdown
and protect hard-earned capital. We must adopt decisive defensive measures
to prevent panic from affecting the long-term plan.
Portfolio Adjustment:
A-Shares

Bonds

REITs

Gold

26.6% ↓

38.0% ↑

27.9% ↓
7.5% ↑
Phase 2: Market Observation & Final Hedging (Apr 8: Pre-Rebound
Signals)
News: On April 8, "pre-rebound signals" emerged as the stock market saw a
minor recovery and the CBOE Volatility Index (VIX) stabilized.
Analysis: The market decline has paused, but the true trend remains uncertain.
Such a fragile rebound is not worth the risk. Maintaining caution and complet-
ing the final defensive adjustments are crucial to ensure we are in the safest
position before the situation fully clears, allowing us to seize the initiative later.
Portfolio Adjustment:
A-Shares

Bonds

REITs

Gold

B Research Methods
B.1 Part One
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi
malesuada, quam in pulvinar varius, metus nunc fermentum urna,
id sollicitudin purus odio sit amet enim. Aliquam ullamcorper eu
ipsum vel mollis. Curabitur quis dictum nisl. Phasellus vel semper
risus, et lacinia dolor. Integer ultricies commodo sem nec semper.

B.2 Part Two
Etiam commodo feugiat nisl pulvinar pellentesque. Etiam auctor
sodales ligula, non varius nibh pulvinar semper. Suspendisse nec
lectus non ipsum convallis congue hendrerit vitae sapien. Donec
at laoreet eros. Vivamus non purus placerat, scelerisque diam eu,
cursus ante. Etiam aliquam tortor auctor efficitur mattis.

C Online Resources
Nam id fermentum dui. Suspendisse sagittis tortor a nulla mollis,
in pulvinar ex pretium. Sed interdum orci quis metus euismod, et
sagittis enim maximus. Vestibulum gravida massa ut felis suscipit
congue. Quisque mattis elit a risus ultrices commodo venenatis eget
dui. Etiam sagittis eleifend elementum.

Nam interdum magna at lectus dignissim, ac dignissim lorem
rhoncus. Maecenas eu arcu ac neque placerat aliquam. Nunc pulv-
inar massa et mattis lacinia.

5.5% ↓

34.3% ↑

41.3% ↑

18.9% ↓
Phase 3: Decisive Re-entry (Apr 9: Tariff Suspension)
News: On April 9, the suspension of some tariffs was announced, leading to a
rapid recovery in global risk assets.
Analysis: This definitive positive news has turned the market’s direction. While
our previous defensive posture was successful, we must now respond swiftly.
To avoid missing the core of this rally, we need to act immediately and reinvest
capital into the A-share market, a key offensive move in our "phased re-entry"
plan.
Portfolio Adjustment:
A-Shares

Bonds

REITs

Gold

31.4% ↓

24.9% ↓

36.0% ↑
7.3% ↑
Phase 4: Trend Confirmation & Steadiness (Apr 11: Consumer Confi-
dence Drop)
News: On April 11, the University of Michigan Consumer Sentiment Index fell
to a near-record low, creating mixed market signals.
Analysis: Negative macroeconomic news serves as a reminder that the market’s
foundation is not yet solid. This confirms the wisdom of our earlier decision
not to go all-in at once. During such periods of mixed signals, the best strategy
is to remain patient, maintain the current allocation, and observe further devel-
opments.
Portfolio Adjustment:
A-Shares

Bonds

REITs

Gold

7.3% (Hold)

24.9% (Hold)

36.0% (Hold)
31.4% (Hold)
Phase 5: Crisis Aversion & Normalization (May 2: U.S. Stocks Recover)
News: On May 2, U.S. stocks erased all "Liberation Day" losses.
Analysis: The market turmoil has subsided, and your portfolio has successfully
passed this stress test. Our "defense first, offense later" tactic proved effective.
The market’s focus now returns to fundamentals, and so our focus must shift
from short-term responses back to your eight-year retirement objective.
Portfolio Adjustment:
A-Shares

Bonds

REITs

Gold

36.0% (Hold)

24.9% (Hold)

31.4% (Hold)

7.3% (Hold)

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Wealth-Voyager: Navigating IntelligentWealth Management with
a Multi-Agent Framework
RuiHuang ZimoZhao SiwenChen
BlockchainandIntelligent BlockchainandIntelligent BlockchainandIntelligent
TechnologyResearchCenter TechnologyResearchCenter TechnologyResearchCenter
TheChineseUniversityofHong TheChineseUniversityofHong TheChineseUniversityofHong
Kong,Shenzhen Kong,Shenzhen Kong,Shenzhen
Shenzhen,Guangdong,China Shenzhen,Guangdong,China Shenzhen,Guangdong,China
rayhuang@cuhk.edu.cn zimozhao@link.cuhk.edu.cn siwenchen@cuhk.edu.cn
XiaoyuWu J.LeonZhao∗
IndependentResearcher SchoolofManagementand
Shenzhen,Guangdong,China Economics
xiaoyuwu5@gmail.com TheChineseUniversityofHong
Kong,Shenzhen
Shenzhen,Guangdong,China
leonzhao@cuhk.edu.cn
Abstract Keywords
Risingdemandforhyper-personalizedwealthmanagementisin- Generativelargelanguagemodels(LLMs),Multi-agentsystems,
creasinglyunmetbytraditionaladvisorymodels,whichsufferfrom Behavioralfinance,Portfoliooptimization,Personalizedadvisory
limitationsinscalability,cost-efficiency,andobjectivity.Whilere-
centAI-drivensolutionsshowpromise,theyoftenremainfrag- ACMReferenceFormat:
mented,focusingonisolatedtasksandlackingaunifiedarchitec- RuiHuang,ZimoZhao,SiwenChen,XiaoyuWu,andJ.LeonZhao.2025.
turethatintegrateslong-termstrategywithdynamicbehavioral Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-
adaptation. To bridge this gap, we introduce Wealth-Voyager,
AgentFramework.In2025InternationalConferenceonGenerativeArtificial
a multi-agent framework that synergizes strategic asset alloca- IntelligenceforBusiness(GAIB2025),August04–06,2025,Hongkong,China.
ACM,NewYork,NY,USA,10pages.https://doi.org/10.1145/3766918.3766944
tionwithadaptivetacticaladjustments.Oursystem’sarchitecture
uniquelycombinesAlphaForge,aquantitativeengineforestab-
lishingalong-termstrategicportfolio,withDualAdvisor,anovel 1 Introduction
Belief-Desire-Intention(BDI)groundedrole-playingsimulationthat
Overthepastdecade,risingmacroeconomicvolatilityandrapid
interactivelymanagesuser-specificbehavioralbiasesinresponse
fintechinnovationhavefueledunprecedenteddemandforhyper-
toreal-timeevents.Ourproof-of-conceptcasestudy,conducted
personalizedwealthmanagementsolutions.By2023,globalassets
under live market conditions, demonstrated the efficacy of this
undermanagement(AUM)hadreachedUSD1.2trillion[25],yet
integratedapproach.Thesystem’sadaptivetacticaladjustments
anestimated320millionpotentialinvestorsremainedunderserved
outperformedapassivebaseline,convertingamarginalgaininto
byconventionaladvisorychannels.Thisgapisespeciallyacute
amoresubstantialreturnwhilereducingportfoliovolatility.Our
inChina,whereaburgeoning“newmiddleclass”withrisingin-
work presents a blueprint for a new class of financial co-pilots
vestableassetsisincreasinglyseekingtechnology-enabledfinancial
thatintegratequantitativerigorwithinteractive,cognitively-aware
guidance.Empiricalevidencefrom290Chinesecitiesshowsthat
guidance,enhancingbothdecisionqualityandusertrust.
fintechadoptionsignificantlyenhancesfinancialaccess,depth,and
inclusion—particularlybenefitinghouseholdswithlowerwealth
CCSConcepts
andlimitedaccesstotraditionaladvisoryservices[14].
•Socialandprofessionaltopics→Economicimpact. Traditionalwealthmanagementframeworksareundergrowing
pressuretomeettheevolvingexpectationsofanincreasinglydi-
verseanddigitallysophisticatedinvestorbase.Inmarketssuchas
∗Correspondingauthor.
China,thedominanceofbank-ledfunddistributionchannels—typically
associatedwithhighfeesandlimitedpersonalization—furthercon-
strains access to tailored services, particularly for emerging in-
vestorsandtheexpandingmiddleclass.Beyondstructuralineffi-
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. ciencies,behavioralchallengessuchasspeculativetrading,early
GAIB2025,Hongkong,China fundredemptions,andlimitedfinancialliteracyremainwidespread.
©2025Copyrightheldbytheowner/author(s). Trustinconventionaladvisorymodelsisfurthererodedbyinade-
ACMISBN979-8-4007-1602-7/25/08
https://doi.org/10.1145/3766918.3766944 quatetransparencyandalackoftimely,proactiveengagement[13].
156

GAIB2025,August04–06,2025,Hongkong,China Huangetal.
Moreover,mostincumbentplatformslackthereal-time,behavior- NewsCrawler(real-timeintelligenceextraction),AlphaForge
awareanalyticsrequiredtosupportinvestorsduringvolatilemarket (scenario-awareportfoliooptimization),andDualAdvisor(BDI-
conditions,ultimatelyfailingtoaddressbothperformance-driven based advisory simulation)–to emulate the workflow of elite
goalsandthepsychologicalfactorsthatshaperetailinvestment investment-researchteams.
behavior[14]. • Behaviour-awarepersonalization.LeveragingLLM-basedse-
Toaddressthesechallenges,recentresearchhasincreasingly manticreasoning,AssistHubinferslatentclientpreferencesand
focusedonemergingtechnologiesthatenablemoreadaptiveand cognitivebiases,enablingpersonalisedstrategiesalignedwith
investor-centricsolutions.Advancesinlargelanguagemodels(LLMs) individualbehaviouralprofilesthatadaptandimproveovertime.
andmulti-agentframeworksofferpromisingalternativestocon- • Real-timeadaptivedecision-making.Bycontinuouslymoni-
ventionalfinancialadvisorysystems.LLM-basedadvisorsfacilitate toringmarketdynamicsthroughNewsCrawlerandperforming
personalized,context-awareinteractions[21,27],yetremaincostly on-the-flyre-optimizationinAlphaForge,thesystemreduces
todeployandlimitedinadaptability[7].Multi-agentsystemsim- decisionlatency,supportstimelyportfoliorebalancing,andproac-
provescalabilitybydistributingfinancialtasksacrossspecialized tivelymitigatestheimpactofblack-swanevents.
roles[10,20].However,mostimplementationsexhibitthreekey • Bridgingtheeducation–decisiongap.Throughexplainable
limitations.First,thelackofbehavioralmodelingpreventsthese dialogueandinteractivescenariotesting,DualAdvisoralignsfi-
systemsfromaccountingforcognitivebiases—suchasoverconfi- nancialeducationwithactionableportfoliochoices,empowering
denceorlossaversion—thatfrequentlyshaperetailinvestorbe- userstodeveloplong-termwealth-managementcompetence.
havior.Second,intheabsenceofinteractiveexplainability,users
• Transparencyandtrustbydesign.Throughscenario-based
receiveopaquerecommendationsthatunderminetrustandreduce
analysis,rationaletracing,andverifiableneutralrecommenda-
engagement.Third,thestaticnatureoftheirdecisionlogicimpedes
tions, the system reveals its decision-making logic, promotes
real-timeresponsivenesstomarketevents—anessentialcapability
financialliteracy,andbuildsusertrustinatransparentandac-
formaintainingportfoliorelevanceinvolatileenvironments.
countablemanner.
Given these limitations in existing systems, the choice of an
Collectively, WealthVoyager introduces a promising frame-
underlyinginvestmentphilosophyiscritical.Weanchorourframe-
workthattransitionsfromstaticassetallocationstrategiestoan
workinassetallocation,whichfinancialliteraturewidelyrecog-
interactivesystemcapableofdeliveringpersonalized,adaptive,and
nizesasthecornerstoneoflong-termportfolioreturns,responsible
transparentwealthmanagementatscale.
forover90%ofperformancevariance[4,5,12].Incontrasttomore
speculativeandvolatilestrategieslikemarkettimingorstockpick-
ing,assetallocationprovidesamorestable,risk-managedpathto 2 RelatedWork
wealthgrowththroughdiversificationandsystematicriskmanage-
2.1 Multi-AgentFrameworks
ment.Thisphilosophyisimplementedthroughtwocomplementary
layers:StrategicAssetAllocation(SAA),whichsetsthefounda- Multi-agent(MA)frameworkshavegainedincreasingtractionin
tional,long-termpolicyportfolio,andTacticalAssetAllocation financialdecision-makingbydistributingportfoliomanagement
(TAA),which enablesdynamic, short-termadjustmentsto that tasksamongspecializedagents,eachresponsibleforsubtaskssuch
policy.ThestructuredyetflexiblenatureoftheSAA-TAAframe- asassetselection,marketmonitoring,orriskcontrol.Recentsys-
workmakesitanidealdomainforanadvisorysystemthatmust temssuchasFinCon[29]incorporatelargelanguagemodels(LLMs)
alsoaddressthecriticalgapsinbehavioralmodelingandreal-time ashigh-levelcoordinatorsacrossagentteams,facilitatingnatural
adaptiveness. language-basedcommunicationandreflectivebeliefrevisionin
WepresentWealth-Voyager,abehavior-aware,multi-agent volatileenvironments.MASA[20]introducesarole-basedstruc-
financialadvisoryframeworkcoordinatedbyacentralLLM-based turecomprisingrewardmaximizers,risksolvers,andmacroob-
meta-controller.Thesystemintegratesstructuredfinancialsignals, servers,witheachagentadaptingautonomouslythroughdeeprein-
unstructuredmarketnarratives,andinvestor-specificbehavioral forcementlearning.Earlierframeworks,includingMAPS[18]and
traitstodeliveradaptive,personalized,andinterpretableportfolio MSPM[11],emphasizedmodularitybydecouplingstrategygenera-
guidance.Throughstructuredfunctioncallsandsharedmemory, tionfromassetevaluation,therebyenhancingdiversityandscalabil-
theLLMorchestratesateamofspecializedagentsresponsiblefor ity.Morerecentefforts,suchasMASS[10]andTradingAgents[28],
userprofiling,newsinterpretation,portfoliooptimization,andad- simulatecollaborativetradingdeskswhereLLM-drivenagentsas-
visorydialoguesimulation.ByembeddingMonteCarlo–basedrisk sumespecializedroles—suchassentimentanalysisandtradeexecu-
modeling,event-drivenrebalancing,andcognitivebiasadaptation, tion—demonstratingstrongperformanceinhigh-frequencytrading
Wealth-Voyagermovesbeyondstaticallocationtools.Itfunctions environments.
asaninteractiveco-pilot,enablinguserstounderstand,trust,and Whileexistingsystemsdemonstratestrongspecialization,they
iterativelyrefinetheirfinancialdecisionsindynamicmarketenvi- often focus on short-term trading or static planning, with lim-
ronments. itedsupportforcontinuousadaptationorinvestor-facingeduca-
tion.Wealth-Voyageraddressesthesegapsbyenablingpersistent,
behavior-awarecoordinationthatevolveswithuserpreferences
KeyContributions:
andmarketdynamics.Leveragingreal-timenewsanalyticsanda
• Modularmulti-agentcollaboration.WealthVoyagerorches- MonteCarlore-samplingloop,itcananticipaterarebutdisrup-
tratesfourspecialisedagents–AssistHub(behaviouralprofiling), tiveeventssuchasmarketshocks.Meanwhile,theDualAdvisor
157

Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-AgentFramework GAIB2025,August04–06,2025,Hongkong,China
modulefostersfinancialliteracythroughinteractivedialoguesthat 3 Framework
clarifytrade-offs,surfacebiases,andenablescenario-basedlearn- 3.1 OverallArchitecture
ing—shiftingthesystemfromexecutiontolong-terminvestorem-
Toprovidepersonalizedandreal-timefinancialadvisoryservices
powerment.
forindividualusers,weproposeanend-to-endframeworknamed
Wealth-Voyager.AsillustratedinFig.1,thesystemintegrates
multiplecollaboratingagentsthatdynamicallyinteractwithcore
2.2 LargeLanguageModelsforInvestment tools,includinganintelligentcustomerassistant,anewscrawler,
andportfoliooptimizationmodels.Inaddition,arole-playingdia-
DecisionSupport
loguemodulethatemploysadual-agent,role-playingsimulation
Largelanguagemodels(LLMs)havebecomeincreasinglyinfluential todeliveradaptiveguidancethatisresponsivetobothreal-time
infinancialdecisionsupportbyenablingcontextualunderstanding, marketeventsandtheuser’suniquebehavioralprofile.
generation,andinteractionacrossarangeofinvestment-related
tasks.FinLLM[21]appliesinstructiontuningtoprovidepersonal-
izedadvicetoretailinvestors,whileBloombergGPT [27]demon- 3.2 CoreModules
stratestheadvantagesoflarge-scale,domain-specificpretraining
AssistHubisanintelligentcustomerservicemodule,implemented
fortaskssuchasentityrecognitionandfinancialquestionanswer-
asanagenticworkflowontheDify[17]platformandpowered
ing.LLM-Advisor [16]integratesreal-timenewssummarization
by ChatGPT-4 [1]. Through a guided conversational process of
andeventinterpretationintoaninteractiveadvisoryworkflow,and
context-aware,adaptivetestingandinteractivecalibrationdynamic,
LLM-Survey [7]offersacomprehensiveoverviewofhowLLMs
itdynamicallyhandlesgeneralinquiriesandassistsusersinarticu-
supporttheassetmanagementlifecycle—frominformationextrac-
latingtheirwealthmanagementgoals(e.g.,retirementsavings,edu-
tiontoportfolioconstruction.Despitethisprogress,manyexisting
cationalfunds),detailingtheircurrentfinancialstatus,andcomplet-
systemsunder-addresscriticalchallengesrelatedtoprobabilistic
ingapersonalizedriskassessment.AssistHubreplacesthe"static
uncertaintyandbehavioralbiasesininvestordecision-making.
questionnaire"withaguidedmulti-rounddialoguemechanismto
Despiterecentadvances,manyLLM-basedfinancialsystemsstill
comprehensiveuserprofile.Thisprofile,whichencapsulatesthe
struggle with behavioral uncertainty, limited transparency, and
user’sfinancialstatus,long-termgoals,andrisktolerance,serves
highdeploymentcosts.WhileLLM-Advisorincorporatesreal-time
asafoundationalinputrequiredbytheotherspecializedmodules
dataandBloombergGPT scaleswellfordomaincoverage,suchsys-
withintheWealth-Voyagerframeworktodeliverpersonalized
temsoftenoperateassingle-passgeneratorswithoutintrospection
analysisandadvice.
oradaptivefeedback.Wealth-Voyagerintroducesacost-efficient,
NewsCrawleroperatesasadedicatedModelContextProto-
dialogue-centricinterfacegroundedinbehavioralfinance,where
col(MCP) [22] server responsible for the real-time aggregation
abelief–desire–intention(BDI)frameworksupportsexplainable,
andprocessingofmarketinformationfromawidearrayofon-
bias-awarerecommendations.Bysimulatingadvisor–clientinterac-
linesources.Thismoduleservestwocriticalfunctionswithinthe
tions,thesystemuncoverscognitivebiasesandpromotesreflective
Wealth-Voyagerframework.Firstly,itperiodicallyextractsex-
decisionsthroughtransparentstrategyrationales.
pectedreturnforecastsformajorassetclassesfromresearchreports
publishedbyprofessionalfinancialinstitutions.Thisdataprovides
theAlphaForgemodulewithrealisticandtimelyinputs,signif-
icantlyenhancingthepracticalapplicabilityandaccuracyofthe
2.3 TraditionalandBehaviour-Aware
portfoliooptimizationalgorithms.Secondly,NewsCrawlercurates
ApproachestoPortfolioOptimization
andretrievesdailymarketnewstailoredtoeachuser’sspecific
Traditionalportfoliooptimizationtechniques,suchasmean–variance profile,includingtheirstatedinvestmentinterests,risktolerance,
analysis and Conditional Value at Risk (CVaR), remain founda- andexistingportfoliocomposition.Thispersonalizednewsfeed
tional to financial planning [9]. Monte Carlo simulation (MCS) servesasthefoundationalcontextfortherole-playingdialogues
has further enabled probabilistic outcome estimation, although withintheDualAdvisormodule.
earlyimplementationsaregenerallyofflineandsingle-pass.MCS- AlphaForgeisthequantitativecoreofWealth-Voyagerwhich
Interactive[3]introducesconversationalsimulation,whileoursys- isbasedonmordenportfoliotheory.Drawingonmarketexpec-
tem(seeAppendixA.3)advancesthislinebysupportingcustom tations(returns,volatilities,andcross-assetcorrelations)continu-
assetuniversesanduser-definedriskthresholds,coupledwithan ouslyharvestedbyNewsCrawlerandtheinvestor-specificcon-
LLM-drivenre-samplingloopforadaptiveportfoliogeneration. straintsproducedbyAssistHub,itconstructsalong-termstrategic
Beyond numerical optimization, behavior-aware systems in- asset-allocationthatbalancesgrowth,risk,andliquidity.Internally,
corporate cognitive biases—such as loss aversion and overcon- AlphaForge employs a constrained mean–variance engine aug-
fidence—thatinfluence real-worldinvestordecisions. Cognitive- mentedwithliquiditycaps,draw-downlimits,andleveragecon-
AwareAdvisors[6,8]demonstratethatembeddingbehavioralpro- trols.Thesolveroutputstargetweightsalongsideforward-looking
filingimprovestrustandengagement.Ourapproachadoptsanine- metrics—projectedreturn,volatility,Value-at-Risk,andliquidity
dimensionalbiasvector(seeAppendixA.2)toguideLLM-based coverage—that feed downstream advisory logic. The full math-
advisorydialogue,aligningwithfindingsfromTrust-AwareGAI ematical specification and optimization routine are provided in
Advisors[26]onpersonalized,trust-sensitiveinteraction. AppendixA.3
158

GAIB2025,August04–06,2025,Hongkong,China Huangetal.
Figure1:ThearchitectureoftheproposedWealth-Voyagerframework.
DualAdvisormoduleutilizesanovelrole-playingframework • AdvisorAgent:Actsastherationalanchor.Itinterprets
poweredbytwodistinctlargelanguagemodel(LLM)agents,which marketdevelopmentswithprofessionalneutralityandproac-
simulateconsultationsbetweenaprofessionalinvestmentadvisor tively detects behavioral biases reflected in the user’s re-
andtheuser.Theprimarypurposeofthismoduleistogenerate sponses.Forexample,itmaycautionagainstoverreactionto
real-time, tactical investment advice. By dynamically modeling newsduetohighpolicysensitivityordiscourageimpulsive
advisor-clientinteractionsinresponsetomarketevents,DualAd- “gain-chasing”behavior.TheAdvisorcontinuouslysteers
visorprovidesactionablerecommendationsthathelpusersmake the dialogue toward strategies consistent with the user’s
timelyportfolioadjustmentstonavigatemarketvolatilityeffec- statedlong-termfinancialgoals.
tively. • UserAgent:Servesasahigh-fidelity"digitaltwin"ofthe
user,designedtoinjectpsychologicallyplausible,andoften
3.3 Role-Playing-BasedAdvisorySimulation biased,humanbehaviorintothesimulation.Itspurposeis
Traditionalfinancialadvisorysystemstypicallyrelyonstaticuser nottobeperfectlyrationalbuttorealisticallymodelhowa
profiles,whichfailtocapturethedynamicinterplaybetweenevolv- specificindividualwouldreacttomarketchangesbasedon
ingmarketconditionsandaninvestor’sreal-timecognitiveand theiruniquefinancialcircumstances,goals,andbehavioral
emotionalresponses[24].Toaddressthislimitation,wepropose tendencies.
DualAdvisor,arole-playingmodulewithinWealth-Voyager,de-
signedtosimulatemulti-turn,psychologicallyinformeddialogue
Eachagentisinstantiatedusingrole-specificsystemprompts.The
UserAgentpromptdynamicallyincorporatesthecompleteuser
betweenaprofessionaladvisorandadigitallymodeledclient.The
profile, including financial goals, risk tolerance, and quantified
objectiveistomovebeyondstaticrecommendationsbygenerat-
behavioralattributes,therebyensuringpsychologicallycoherent
ingadvisoryresponsesthatarebothresponsivetomarketsignals
andcontext-awareresponses.
andadaptivetouser-specificbehavioralbiases.Thisisachieved
Thisdual-agentdesignfulfillstwocomplementaryobjectives.
throughanagent-basedinteractionbetweentwolargelanguage
Firstly,itgeneratespersonalized,bias-awareinvestmentguidance
model(LLM)agents,groundedinabehaviorallyrichuserprofile.
byanticipatorilymodelingtheuser’slikelyemotionalreactions.
3.3.1 AgentRolesandDialogueObjectives. Toeffectivelysimulate Secondly,therecordedconversationactsasa“behavioralmirror”
complexfinancialdecision-making,wedecomposetheadvisory forinvestoreducation,enablinguserstoobservehowprofessional
interaction into two specialized agent roles, inspired by recent reasoningcanmitigatetheirowncognitivedistortions,thereby
developmentsinsocial-agentsimulation[19]. enhancingtheirfinancialself-awarenessovertime.
159

Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-AgentFramework GAIB2025,August04–06,2025,Hongkong,China
3.3.2 BDI-GroundedBehavioralProfile. Toenablerealisticsimu- suggestionsderivedfromtheconsensus,andkeyareasoffocusfor
lation,weconstructacomprehensiveuserprofilethatservesasa thenearfuture.
behavioralfingerprint.Drawingfrombehavioraleconomics,this
profileextendsbeyondconventionaldatabyquantifyingarangeof 4 UserStudy
user-specificbiases.Thesearebroadlycategorizedintoemotional
Toevaluatethepracticaleffectivenessanddecision-supportcapabil-
indicators(e.g.,lossaversion,overconfidence),whichmodelthe
itiesoftheWealth-Voyagersystem,weconductedamonth-long
user’scorefeelingsaboutriskandsecurity,capturingtheaffective
pilot study from April 2 to May 2, 2025. The study involved a
responsesundermarketstressthatoftendriveintuitivedecisions,
mid-careerparticipantfocusedonretirementplanningandaimed
andcognitiveindicators(e.g.,herdingtendency,policysensitiv-
tosimulaterealisticinvestmentscenariosunderlivemarketcon-
ity),whichsimulatehowtheuserprocessesmarketinformationand
ditions. During this period the system was fully deployed in a
formsjudgments,reflectingtheirsystematicpatternsofreasoning.
sandboxenvironment,enablingend-to-endvalidationofitscore
TooperationalizethisbehavioralprofilewithintheUserAgent,
modules—includingbehaviouralprofiling,adaptiverebalancing,
wemodelitsinternaldeliberationusingtheBelief–Desire–Intention
andagent-drivenmarketresponse.
(BDI)framework,awell-establishedparadigmforrationalagency
Importantly,theexperimentcoincidedwithaperiodofelevated
thatmirrorshumanpracticalreasoning.Thisstructuresequentially
geopoliticalandfinancialuncertainty,markedbyasharpescala-
modelstheagent’s:
tioninglobaltradetensions.Thisprovidedanaturalstress-test
• Beliefs(B):Itssubjectiveunderstandingofthecurrentmar- forevaluatinghowWealth-Voyagerrespondstovolatilemarket
ket. events.
• Desires (D): Long-term investment goals and emotional Thestudyfocusonthequantitativeperformance(e.g.returns
inclinationsderivedfromtheuserprofile. andvolatility)ofbothStrategicAssetAllocation(SAA),whichbased
• Intentions(I):Actionablestepsproposedforportfolioad- onlong-terminvestmentgoalsandTacticalAssetAllocation(TAA),
justment. whichbasedonSAAanddynamicallyadjustedaccordingtoshort-
termmarketsignals(suchaspolicychanges,macroeconomicdata),
WeoperationalizeBDIreasoningviaastep-wisepromptingmech-
andqualitativeuserexperienceofferinganintegratedviewofthe
anism:theLLMissequentiallyqueriedforitsbeliefs,desires,and
robustness,adaptability,andusabilityofoursystem.
intentionsinresponsetonewmarketinformation.Thischain-of-
thoughtdesignimprovesboththelogicalconsistencyandinter-
4.1 ParticipantProfile
pretabilityofthesimulateddecisionprocess.
The case involves a 45-year-old professional planning to retire
3.3.3 DialogueFlowandConsensusMechanism. Theagentinter- withineightyears,withtheobjectiveofgrowinginvestableassetsto
actionunfoldsasastructured,multi-turnconsultationdesignedto
supportacomfortablepost-retirementlifestyle.Duringonboarding,
transformauser’spotentialbiasedreactionsintoareasonedaction
theuserreportedsubstantialwealthandmoderateliquidityrequire-
plan.Thedialogueprogressesthroughfourdistinctphases:
mentsbutdidnotspecifykeyparameterssuchasrisktoleranceor
• RationalInitialization:TheAdvisorAgentsynthesizes returnobjectives.Theinitialportfolioallocation(Table1a)includes
dailymarketnewsthroughthelensoftheuser’sprofileto a20%concentrationinrealestateinvestmenttrusts(REITs)—an
formulateascenario-specificinterpretation.Thisinterpreta- unusuallyhighexposureforabalancedportfolio—introducingliq-
tionservesastheinitialprompt,triggeringtheUserAgent’s uidityconstraintsandlimitingdiversification.
BDIreasoningprocess. Onboardinginteractionsrevealedthreeprimaryconcerns:(i)
• BehavioralResponse:TheUserAgentthengeneratesits mitigatinglargedrawdownsnearretirement,(ii)maintainingac-
initialBDIresponse,surfacingtheuser’slikelyfirstreaction, cess to capital within six months for potential obligations, and
completewithanypossiblebiases. (iii)receivingclear,rationale-driveninvestmentguidance.These
• Cognitive Debiasing: The Advisor Agent critiques this concernsinformedthesystem’sevaluationcriteria,emphasizing
response,identifiesirrationalpatternsbasedontheuser’s drawdowncontrol,risk-adjustedperformance,andinterpretability.
profile,andrecommendsalternative,goal-alignedplans. Incontrasttoconventionalsystemsthatprovidestaticrecom-
• IterativeConsensus:Theagentsengageinaniterativedia- mendationsoropaqueoptimizations,Wealth-Voyagerinferred
logue.TheUserAgenteitherrevisesitsintentionsbasedon latentpreferencesandappliedastructured,investment-bank-style
theAdvisor’sfeedbackordefendsitspositiontopromptfur- workflowtorevisetheportfolio.Theresultingallocation(Table1b)
therclarification.Thedialogueterminateswhenaconsensus improveddiversificationandmorecloselyalignedwiththeuser’s
isreached,governedbyapragmaticmechanism:eitherthe implicitriskprofile—demonstratingWealth-Voyager’scapacityto
Advisorgeneratesaspecificagreementphrase(e.g.,"Agree, translatevaguefinancialgoalsintoactionable,personalizedinvest-
nomodificationneeded")orapredefinedmaximumoften mentstrategies.
roundsisreached.
4.2 SystemOperation
Theentireinteractionculminatesinafinal,user-facingdeliver-
able:theDailyInvestmentBriefing.Thisstructuredreportsumma- Toensuretimelyadaptationtomarketshifts,thesystemcontinu-
rizestheessenceofthedialogue,providingtheuserwithaclear ouslyscrapedmacroeconomicnewsandmonitoredreal-timeasset
andactionablesummarythatincludesamarketoverview,theAd- prices.TheAlphaForgefirstlyimplementsStrategicAssetAlloca-
visorAgent’stailoredinterpretation,concreteportfolioadjustment tion(SAA)byoptimizinglong-termweightsunderconstraintssuch
160

GAIB2025,August04–06,2025,Hongkong,China Huangetal.
Table1:Comparisonbetweenuser-declaredbaselineprofileandAI-optimisedallocation.
Attribute User-declared(Apr2,2025) AI-optimised(DualAdvisor)
Initialcapital RMB3,000,000 RMB3,000,000
Targetamount RMB4,500,000+ RMB4,500,000+
Risktolerance N/A Medium(maxloss20%)
Leverageallowed No No
Liquidityneed Medium Medium
Strategicassetmix A-shares30%,Bonds35%, A-shares35.3%,Bonds41.1%,
Gold15%,REITs20% Gold17.6%,REITs6.0%
Expectedreturn N/A 6.53%
Expectedvolatility N/A 9.42%
Notes.“A-shares”areRMB-denominatedequitiesonmainlandChineseexchanges;“Bonds”arefixed-incomesecurities;“Gold”includesphysicalbullionorETFexposure;
“REITs”arereal-estateinvestmenttrusts.N/A=notprovidedatonboarding.
asmaximumdrawdownthresholds.Addtionally,theNewsCrawler anchoring with real-time tactical rebalancing achieves superior
modulegeneratedpersonalisedbriefingsandcontextualinterpre- returnswithoutincreasingriskexposure.
tationstailoredtotheparticipant’sportfolioexposures.Uponde-
tectionofdisruptiveevents—suchasunexpectedpolicyshiftsor
volatilityspikes—theDualAdvisormoduleassessedpotentialport-
folioimpactsandissuedpreemptiverebalancingproposalstohedge
downsideriskwhilepreservingupsidepotentialandalsoemploys
TacticalAssetAllocation(TAA)toadjustpositionsinresponseto
4.4 ComparativeAnalysiswithExistingMarket
real-timemarketeventswiththealgorithmintheAlphaForge.
Solutions
OnApril2,2025,asuddentariffshock(aminor“black-swan”
event)wasdetected.Tacticaladjustmentswereexecutedpriorto RecentindustryanalyseshighlightthegrowingadoptionofAI-
significantmarketdrawdowns.Theseincludedareductioninequity drivenwealth-managementsystemsinChina,notably:AntGroup’s
holdings,increasedexposuretogoldandgovernmentbonds,anda AntFortune [2],JDDigits’JDXiaobei [15],andPingAn’sIntel-
moderateuptickinREITallocation.Thisrepositioningenabledthe ligentWealthButler [23].Theseplatformsprovidefoundational
participanttolimitlossesandcapitaliseonshort-termmispricings. investmentguidancethroughrule-basedallocationandbasicuser
profiling.
Incontrast,Wealth-Voyagerwasco-developedwithagroupof
4.3 PerformanceAcrossPortfolioStrategies
noviceandintermediateinvestorswhouseditalongsideexisting
Figure2comparessegment-levelreturnsofpassiveandtacticalport- marketsolutionsoverasix-weekperiod.Feedbackfromthisreal-
foliosfromApril2toMay9,2025.Followingatariff-inducedshock worlddeploymentinformedthedesignofkeydifferentiators:real-
(Apr02–Apr09),thetacticalapproachreducedlosses(−2.56%vs. timeadaptiverecommendations,personalizedbehavioralmodeling,
−2.79%).Inthereboundphase(Apr09–Apr23),itcapturedgreater andconversationalexplanationmechanisms.
upside(3.24%vs.2.16%).Acrosssubsequentintervals,tacticalre- Wealth-Voyagernotonlysupportsstandardinvestmentadvi-
turnsremainedconsistentlyhigher,notablyduringApr30–May07 soryfunctionsbutalsointroducesnoveldimensionsthatenhance
(1.15%vs.0.68%).Evenduringmildpullbacks(May07–May09),the theuserexperience.AsshowninTable3,oursystemoutperforms
tacticalstrategylimiteddownsidemoreeffectively. existingofferingsinareassuchasdynamicresponsiveness,person-
TheseresultsunderscoretheadvantageoflayeringTacticalAsset alizationdepth,andeducationalengagement—featuresthatusers
Allocation(TAA)atopaStrategicAssetAllocation(SAA)frame- highlightedascriticalforbuildinglong-termfinancialliteracyand
work,enhancingresponsivenesswithoutsacrificingstability. confidence.
Table2comparestheperformanceofthreeportfoliostrategies: The comparison reveals that while current mainstream plat-
theuser-declaredbaseline(Original),abehaviorallyAnchoredport- formsfulfillbaselineadvisoryrequirements,theyremainlimited
folio,andadynamicallyrebalancedTacticalstrategy.Anchoring intheirresponsivenessandpersonalizationdepth.Usersreported
aloneyieldssubstantialgains,increasingtheannualreturnfrom thatWealth-Voyager’sabilitytoexplaininvestmentlogicinplain
3.72% to 6.53% while nearly halving annualised volatility (from languageandadapttotheirevolvingpreferencessignificantlyim-
18.08%to9.42%). provedtheirengagementandunderstandingofportfoliomanage-
Buildingonthisfoundation,theTacticalstrategydeliversfur- ment.
therimprovements.Overtheevaluationperiod,cumulativereturn Wealth-Voyageradvancestheparadigmbyenablingadaptive
risesfrom0.24%to1.86%,withannualvolatilityreducedto12.10%, intradayassetrebalancing,integratingbehavioralfinancesignals,
outperformingbothbaselineandAnchoredstrategiesonarisk- andprovidinginterpretablerecommendationsviadialogue-based
adjustedbasis. interfaces.Theseenhancementscollectivelypositionitasamore
Theseresultsvalidatetheeffectivenessof WealthVoyager’s transparentandresponsiveco-advisoracrossdiverseinvestorseg-
layereddecisionarchitecture:theintegrationofstrategicbehavioral ments.
161

Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-AgentFramework GAIB2025,August04–06,2025,Hongkong,China
Figure2:Segment-levelreturnsforpassiveandtacticalportfolios(April2–May9,2025).
Table2:Performancecomparisonacrossuser-declared,anchored,andtacticalportfoliostrategies.
|           | (a)Originalvs.Anchored |              |               |           | (b)Anchoredvs.Tactical |            |               |
| --------- | ---------------------- | ------------ | ------------- | --------- | ---------------------- | ---------- | ------------- |
| Portfolio |                        | AnnualReturn | Annual        | Portfolio |                        | Cumulative | Annual        |
|           |                        | (%)          | Volatility(%) |           |                        | Return(%)  | Volatility(%) |
| Original  |                        | 3.72         | 18.08         | Anchored  |                        | 0.24       | 13.70         |
| Anchored  |                        | 6.53         | 9.42          | Tactical  |                        | 1.86       | 12.10         |
Notes.Original:user-declaredallocation;Anchored:allocationanchoredbybehavioralsignalsviaDualAdvisor;Tactical:adaptivelyrebalancedbasedonlive
marketsignals.
Annualreturn=projectedyearlygain;cumulativereturn=totalreturnovertheobservedperiod;annualvolatility=yearlyreturndispersion.
Table3:CapabilitycomparisonbetweenWealth-Voyagerandrepresentativemarketofferings.✓=supported;✗=absent.
|     | Feature                       |     | AntFortune | JDXiaobei PingAnButler |     | Wealth-Voyager |     |
| --- | ----------------------------- | --- | ---------- | ---------------------- | --- | -------------- | --- |
|     | Diverseasset-classsupport     |     | ✓          | ✓                      | ✓   | ✓              |     |
|     | Interactiveinterface          |     | ✓          | ✓                      | ✓   | ✓              |     |
|     | Real-timedynamicadjustment    |     | ✗          | ✗                      | ✗   | ✓              |     |
|     | Personalizedcustomization     |     | ✗          | ✗                      | ✗   | ✓              |     |
|     | Financialeducationintegration |     | ✗          | ✗                      | ✗   | ✓              |     |
5 Conclusion usertrustandself-awarenessbyexposingcognitivebiasesinan
explainabledialogue.
Inthispaper,weintroducedWealth-Voyager,anovelmulti-agent
frameworkthatunifiesbehaviouralprofiling,real-timemarketin- Ourvalidation,whilepromising,hasseverallimitations:thepro-
telligence,andquantitativeoptimizationintoacohesivepipeline. totypewasevaluatedonasingleuserandalimitedassetuniverse,
anditsperformanceiscontingentontheunderlyingLLM.Toad-
Throughthecoordinationoffourspecializedmodules—AssistHub,
dressthesegapsandstrengthentherobustnessofourfindings,our
NewsCrawler,AlphaForge,andDualAdvisor—oursystemdeliv-
futureworkwillprioritizeamulti-facetedevaluation.Weplanto
ersinteractivedecisionsupportthatmovesbeyondpassiverecom-
mendations.Thiswasevidencedbyourproof-of-conceptdeploy- conductlarger,longitudinalstudieswithadiversecohortofusers
ment,wherethesystem’sadaptiveadviceoutperformedapassive tostatisticallyvalidatethesystem’sadaptabilityacrossdifferent
|     |     |     |     | behavioral profiles. | Furthermore, | we will expand | the asset uni- |
| --- | --- | --- | --- | -------------------- | ------------ | -------------- | -------------- |
baselineby+1.62ppduringaperiodofelevatedmacrouncertainty,
verse,testtheframeworkundervariedmarketregimestoassessits
anditsstrategicallocationsimprovedtheuser’srisk-returntrade-
resilience,andperformsystematicbenchmarkingagainststate-of-
off(+2.81ppannualizedreturn,−8.66ppvolatility).Qualitative
feedbackalsoindicatedthatthedual-agentsimulationenhances the-artsystemstohighlighttheadvantagesofourbehavior-aware
162

| GAIB2025,August04–06,2025,Hongkong,China |     |     |     |     |     |     |     |     |     | Huangetal. |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |
approach.Beyondtheseevaluations,wealsoaimtoenhancethe [17] AlexLeatherwoodandVicMatta.2025.BuildingAIApplicationswithDify.ai:
coremethodologybyexploringreinforcementlearningtorefine AHands-OnWorkshop.(2025).
thenegotiationdynamicswithinDualAdvisorandinvestigating [18] JinhoLee,RaehyunKim,Seok-WonYi,andJaewooKang.2020.MAPS:Multi-
agentreinforcementlearning-basedportfoliomanagementsystem.arXivpreprint
domain-specificmodelstoimproveperformanceandreduceinfer- arXiv:2007.05402(2020).
|     |     |     |     |     | [19] Guohao | Li, Hasan | Hammoud, Hani | Itani, Dmitrii | Khizbullin, | and Bernard |
| --- | --- | --- | --- | --- | ----------- | --------- | ------------- | -------------- | ----------- | ----------- |
encecosts.
Ghanem.2023.Camel:Communicativeagentsfor"mind"explorationoflarge
Bybridgingthegapbetweenbehaviouralfinance,quantitative languagemodelsociety.AdvancesinNeuralInformationProcessingSystems36
analysis,andgenerativeAI,Wealth-Voyagerchartsaviablepath (2023),51991–52008.
towardthenextgenerationoffinancialco-pilots.Webelievethis [20] ZhenglongLi,VincentTam,andKwanLYeung.2024.Developingamulti-agent
andself-adaptiveframeworkwithdeepreinforcementlearningfordynamic
| work represents | a significant | step toward | more effective, | trans- |     |     |     |     |     |     |
| --------------- | ------------- | ----------- | --------------- | ------ | --- | --- | --- | --- | --- | --- |
portfolioriskmanagement.arXivpreprintarXiv:2402.00515(2024).
[21] Xiao-YangLiu,GuoxuanWang,HongyangYang,andDaochenZha.2023.FinGPT:
parent,andtrustworthyhuman-AIcollaborationinthecomplex
DemocratizingInternet-ScaleDataforFinancialLargeLanguageModels.arXiv
domainofwealthmanagement.
preprintarXiv:2307.10485(2023).
|     |     |     |     |     | [22] ModelContextProtocolInitiative.2024.              |     |     | IntroductiontotheModelContext |                      |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | ----------------------------- | -------------------- | --- |
|     |     |     |     |     | Protocol.https://modelcontextprotocol.io/introduction. |     |     |                               | Accessed:2025-07-11. |     |
Acknowledgments [23] PingAnGroup.n.d..IntelligentWealthButler-PingAnGroup.https://group.
|     |     |     |     |     | pingan.com/. | Accessed:2025-07-11. |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | -------------------- | --- | --- | --- | --- |
Wegratefullyacknowledgethegenerousfinancialandcomputa-
|     |     |     |     |     | [24] MichaelPompian.2016. |     | Riskprofilingthroughabehavioralfinancelens. |     |     | CFA |
| --- | --- | --- | --- | --- | ------------------------- | --- | ------------------------------------------- | --- | --- | --- |
tionalsupportfromProf.ZhaoandtheBlockchainandIntelligent InstituteResearchFoundation.
|     |     |     |     |     | [25] Statista | Research | Department. 2023. | Global | wealth-management | market |
| --- | --- | --- | --- | --- | ------------- | -------- | ----------------- | ------ | ----------------- | ------ |
TechnologyResearchCenter(CBIT).Wealsoextendoursincere size, 2019–2023. https://www.statista.com/statistics/1266189/global-wealth-
thankstoourindustrymentor,Dr.XiaoyuWu(formerlyofBlack- management-market-size/. Accessed:2025-07-07.
Rock),forherinvaluableinsightsthatshapedthisresearch,and [26] TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,
andIadhOunis.2025.AreGenerativeAIAgentsEffectivePersonalizedFinancial
toAmosChenandWarrenLiofGoogleCloudfortheirhelpful
|     |     |     |     |     | Advisors?.InProc.SIGIR2025. |     | arXiv:2504.05862. |     |     |     |
| --- | --- | --- | --- | --- | --------------------------- | --- | ----------------- | --- | --- | --- |
feedbackonanearlydemonstrationofourwork. [27] ShijieWu,CaolanSlack,BryanKelly,OzanIrsoy,andetal.2023.BloombergGPT:
ALargeLanguageModelforFinance.arXivpreprintarXiv:2303.17564(2023).
|     |     |     |     |     | [28] YijiaXiao,EdwardSun,DiLuo,andWeiWang.2024. |     |     |     | TradingAgents:Multi- |     |
| --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | -------------------- | --- |
References AgentsLLMFinancialTradingFramework.arXivpreprintarXiv:2412.20138(2024).
[29] YangyangYu,ZhiyuanYao,HaohangLi,ZhiyangDeng,YuechenJiang,Yupeng
[1] JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,IlgeAkkaya,Floren- Cao,ZhiChen,JordanSuchow,ZhenyuCui,RongLiu,etal.2024. Fincon:A
ciaLeoniAleman,DiogoAlmeida,JankoAltenschmidt,SamAltman,Shyamal synthesizedllmmulti-agentsystemwithconceptualverbalreinforcementfor
Anadkat,etal.2023. Gpt-4technicalreport. arXivpreprintarXiv:2303.08774 enhancedfinancialdecisionmaking.AdvancesinNeuralInformationProcessing
| (2023).                                                            |     |     |     |     | Systems37(2024),137010–137045. |     |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
| [2] AntGroup.n.d..AntFortune-AntGroup.https://www.antfortune.com/. |     |     |     | Ac- |                                |     |     |     |     |     |
cessed:2025-07-11.
| [3] KousikBarnwal.2023. | UserFriendlyPortfolioOptimisationUsingMonteCarlo            |     |     |     | A Appendix |     |     |     |     |     |
| ----------------------- | ----------------------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
| Simulation.             | https://medium.com/@indubarnwal752/user-friendly-portfolio- |     |     |     |            |     |     |     |     |     |
optimization-using-mcs-5154ff52dc14 A.1 Monte-Carlo–DrivenMeta-Agent
| [4] Z.Bodie.1995.Investments.(1995). |     | Book. |     |     |     |     |     |     |     |     |
| ------------------------------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
[5] GaryP.Brinson,L.RandolphHood,andGilbertL.Beebower.1986.Determinants
| ofPortfolioPerformance.FinancialAnalystsJournal42,4(1986),39–44. |     |     |     | http: |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
//www.jstor.org/stable/4478947
[6] AbhijeetChandra,ArnavKumar,andShaBala.2025. CognitiveBiasesand Algorithm1InvestmentAdvisorLoop(simplified)
| Robo-AdvisoryAdoption:ExperimentalEvidence. |     |     | JournalofBehavioraland |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
ExperimentalFinance37(2025),100742.doi:10.1016/j.jbef.2024.100742 Require: Userconfig𝑐0 ,successthreshold𝜏,maxrounds𝑅
[7] XuDong,ThanosStratopoulos,andChristinaWang.2024. LargeLanguage 1: 𝑐 ←𝑐0 ; 𝑏𝑒𝑠𝑡 ←𝑐0 ; 𝑏𝑒𝑠𝑡 ←0
M o d e ls fo r Fi n a n c i a l a n d I n v e s t m e n t M a n a g e m en t. 𝑐 𝑝
|               |                               |                            | T h e J o urnalofPortfolio |     | for𝑟 | ←1to𝑅do |     |     |     |     |
| ------------- | ----------------------------- | -------------------------- | -------------------------- | --- | ---- | ------- | --- | --- | --- | --- |
| Ma n a g em e | nt 5 1 , 2 ( 2 0 2 4 ), 2 1 1 | – 2 3 0 . d o i:1 0 .3 9 0 | 5 /j pm .2 02 4. 1 .3 5 0  |     | 2:   |         |     |     |     |     |
←MonteCarloSim(𝑐)
| [8] KimSandyEichlerandElizabethSchwab.2024. |                                 |                             | EvaluatingRobo-Advisors       |                        | 3: 𝑝   |       |        |     |     |     |
| ------------------------------------------- | ------------------------------- | --------------------------- | ----------------------------- | ---------------------- | ------ | ----- | ------ | --- | --- | --- |
| t h r o u g h B                             | e h a v i o r a l F i n an ce : | A C r i ti c a l R e v      | ie w o f T e c h n o lo g y P | o t e n ti a l, R a -  |        |       |        |     |     |     |
|                                             |                                 |                             |                               |                        | 4: if𝑝 | >𝑏𝑒𝑠𝑡 | 𝑝 then |     |     |     |
| ti o n a l it y, a                          | n d I n v e s t o r E x pe ct   | a tio n s . F r o n ti e rs | i nB e ha v i o r al E c o no | m i c s 3 ( 2 02 4 ) , |        |       |        |     |     |     |
1489159.doi:10.3389/frbhe.2024.1489159 5: 𝑏𝑒𝑠𝑡 𝑐 ←𝑐; 𝑏𝑒𝑠𝑡 𝑝 ←𝑝
| [9] Financial      | Edge Training. 2024. | Portfolio                                         | Optimisation Explained: | Mean– | 6: endif |         |     |     |     |     |
| ------------------ | -------------------- | ------------------------------------------------- | ----------------------- | ----- | -------- | ------- | --- | --- | --- | --- |
| V a r i an c e , C | V a R a n d Beyond.  | https://www.fe.training/free-resources/portfolio- |                         |       | if𝑝      | ≥𝜏 then |     |     |     |     |
| o p ti m i s a ti  | o n -g u id e /      |                                                   |                         |       | 7:       |         |     |     |     |     |
break
| [10] TaianGuo,HaiyangShen,JinshengHuang,ZhengyangMao,JunyuLuo,Zhuoru |     |     |     |     | 8:  |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Chen,XuhuiLiu,BingyuXia,LuchenLiu,YunMa,etal.2025.MASS:Multi-Agent
9: endif
S i m u l a tionScalingforPortfolioConstruction.arXivpreprintarXiv:2505.10278
10: 𝑐 ←LLM_Adjust(cid:0)𝑐,allowed_params(cid:1)
( 2 0 2 5 ) .
| [11] ZhenhanHuangandFumihideTanaka.2022.MSPM:Amodularizedandscal- |     |     |     |     | 11: endfor |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
a b le m u lti - a g e n t re i n fo r c e m e n t l e a r n i n g - b a sedsystemforfinancialportfolio return(𝑏𝑒𝑠𝑡 ,𝑏𝑒𝑠𝑡 𝑝)
| m a na ge m e | n t . 1 7 , 2 (2 | 0 2 2 ) , e 0 2 6 3 6 8 9 . |     |     | 12: | 𝑐   |     |     |     |     |
| ------------- | ---------------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
P l os o n e
[12] RogerG.IbbotsonandPaulD.Kaplan.2000.DoesAssetAllocationPolicyExplain
40,90,or100PercentofPerformance?FinancialAnalystsJournal56,1(2000),
26–33. http://www.jstor.org/stable/4480220
| [13] CFAInstitute.2022. | EnhancingInvestors’Trust:2022CFAInstituteInvestor                   |     |     |     |     |     |     |     |     |     |
| ----------------------- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TrustStudy.             | https://www.cfainstitute.org/sites/default/files/-/media/documents/ |     |     |     |     |     |     |     |     |     |
FunctionDescriptionsforAlgorithm1(InvestmentAdvisorLoop):
article/Enhancing-Investors-Trust-Report_2022_Online.pdf
[14] InternationalMonetaryInstitute.2024. ChinaWealthManagementCompe- • MonteCarloSim(𝑐):runsaMonteCarlorolloutunderconfigu-
| tency Evaluation | Report (2023). | https://www.imi.ruc.edu.cn/docs/2024-06/ |     |     |     |     |     |     |     |     |
| ---------------- | -------------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ration𝑐andreturnsthesuccessprobabilityestimate.
cad95d7db7774df4a82a04bb5c212e8f.pdf.
[15] JDDigits.n.d..JDXiaobei-JDDigits.https://jr.jd.com/. Accessed:2025-07-11. LLM_Adjust(𝑐,allowed_params):interactswithanLLM-based
•
[16] KausikLakkaraju,SaiK.R.Vuruma,VishalPallagani,BharathMuppasani,and dialogueagenttoproposeadjustmentstothecurrentusercon-
BiplavSrivastava.2023.CanLLMsBeGoodFinancialAdvisors?AnInitialStudy
inPersonalFinanceDecisionMaking.InProc.ICAPSFinPlanWorkshop.1–6. figuration𝑐,subjecttoawhitelistofallowedparameters.
163

Wealth-Voyager:NavigatingIntelligentWealthManagementwithaMulti-AgentFramework GAIB2025,August04–06,2025,Hongkong,China
Algorithm2ConstructionofBehaviourVector • DecisionDelay:Thisisabehaviorwhereinvestorsareslowto
Require: ConversationID𝑖𝑑;defaultmappingM(Table4) makedecisionsduetodiscomfortwithuncertaintyorputting
1: 𝐻 ←LoadDialogueHistory(𝑖𝑑) offdecisionsuntiltheyreceiveprofessionaladvice.
2: ifContainsStructuredBlock(𝐻)then
3: 𝐸←ParseStructuredBlock(𝐻) Table4:DefaultPersonalityMappingM
4: else
5: 𝐸←LLM_ProfileExtract(𝐻)
6: endif Purpose Vectorslice(loss_aversion,...,decision_delay)
7: if𝐸incompletethen retirement [0.8,0.5,0.8,0.5,0.4,0.8,0.3,0.2,0.6]
8: 𝐸←FillDefaults(𝐸) child_education [0.7,0.6,0.5,0.5,0.5,0.7,0.4,0.4,0.5]
9: endif house_purchase [0.6,0.7,0.4,0.5,0.6,0.6,0.3,0.3,0.7]
10: 𝑝 ←𝐸.investment_purpose⊲retirement/education/house/ wealth_growth [0.3,0.8,0.6,0.5,0.7,0.3,0.8,0.7,0.3]
growth
11: v←M[𝑝]
12: v[4] ←𝐸.real_time_emotion
13: returnDict(keys,v) A.3 Constraint-AwarePortfolioOptimiser
Algorithm3Multi-StageOptimizationProcedure
A.2 Large-Model–AssistedBehaviourProfiling
Require: Meanreturns𝜇,covarianceΣ,userconfig𝜅
FunctionDescriptionsforAlgorithm2(BehaviourVectorConstruc- 1: Infertargetreturn𝑟★,vollimit𝜎max ,CVaRlimit
tion):
2: Deriveliquiditytiers,leverageflagandrestrictedsetR
• LoadDialogueHistory(𝑖𝑑):retrievestheentireconversation 3: Buildboxbounds𝑏 𝑖 forallassets
historyforagivenconversationID. 4: 𝑤(0) ←ERC_Init(Σ)
• ContainsStructuredBlock(𝐻):checksifawell-formed,machine- 5: 𝑤 MS←closed-formmax-Sharpesolution
readableblockispresentinthedialogue. 6: if𝑤 MS feasibleandmeetsallriskcapsthen
• ParseStructuredBlock(𝐻):parsesastructuredblocktodi- 7: return𝑤 MS
rectlyextractuserprofileattributes. 8: endif
• LLM_ProfileExtract(𝐻):usesalanguagemodeltoinferuser ⊲—Stage1:smoothlocalsearch—
attributes from free-form dialogue if no structured block is 9: L(𝑤)←−Sharpe(𝑤)+𝜆IlliqPenalty(𝑤)
found.
10:
𝑤★←SLSQP(cid:0)L,𝑤(0),𝑏
𝑖
,constraints(cid:1)
• FillDefaults(𝐸):fillsmissingentriesintheextractedprofile 11: ifsuccessthen
vector𝐸usingpredefineddefaultvalues.
12:
returnPostProcess(𝑤★)
13: endif
BehavioralMetricDescriptions:
⊲—Stage2:globalrepair—
• LossAversion:Thisisanemotionalbiaswhereinvestorstend 14: 𝑤⋄ ←DifferentialEvolution(cid:0)L,𝑏 𝑖 ,constraints(cid:1)
tofeelthepainoflossesmorethanthepleasureofgains.
15: ifsuccessthen
• News&PolicySensitivity:Thismetricgaugeshowmuch 16: returnPostProcess(𝑤⋄)
aninvestor’sdecisionsareirrationallyswayedbyimmediate
17: else
mediaheadlinesandpolicychanges.
18: returnFailReport()
• Investment Experience: An investor’s behavior is uncon- 19: endif
sciously influenced by past experiences, which can provide
moreaccurateinsightintotheirriskprofile.
• Real-TimeEmotion:Thisreferstoreasoninginfluencedby
feelings,whichcanoverpowerlogicalthinkingduringtimesof FunctionDescriptionsforAlgorithm3(Multi-StageOptimization):
stressandaffectinvestmentdecisions. • ERC_Init(Σ):returnsanequalriskcontributionportfolioini-
• HerdingTendency:Thisisabehaviorwhereinvestorsdonot tializationgiventhecovariancematrixΣ.
havetheirownideasandinsteadfollowtheleadoftheirfriends • SLSQP(L,𝑤(0),𝑏 𝑖 ,constraints):appliesSequentialLeastSquares
andcolleaguesinmakinginvestmentdecisions. QuadraticProgrammingtolocallyoptimizetheobjective L
• RegretAversion:Thisisanemotionalbiaswhereinvestors startingfrom𝑤(0).
avoidtakingdecisiveactionsbecausetheyfearthattheirchosen • DifferentialEvolution(L,𝑏 𝑖 ,constraints):appliesaglobal
coursewillproveunwiseinhindsight. evolutionarysearchtooptimize L incasethelocalmethod
• Overconfidence:Thisisanemotionalbiasbestdescribedas fails.
unwarrantedfaithinone’sownthoughtsandabilities. • PostProcess(𝑤):normalizesandsanitizesacandidateweight
• Illusion of Control: This is a cognitive bias where people vectorbeforereturningit.
believetheycancontrolorinfluenceinvestmentoutcomeswhen • FailReport(): generates a diagnostic message if no feasible
theyactuallycannot. solutionisfound.
164

GAIB2025,August04–06,2025,Hongkong,China Huangetal.
A.4 IllustrativeCaseStudy:ATacticalResponse B ResearchMethods
Narrative B.1 PartOne
Toillustratethepracticalutilityoftheframework,thisappendix Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi
offersanarrativewalkthroughofafive-stagetacticalresponsetoa malesuada,quaminpulvinarvarius,metusnuncfermentumurna,
simulatedmarketcrisis.Theboxbelowsummarizesthekeyevents, idsollicitudinpurusodiositametenim.Aliquamullamcorpereu
correspondinganalyses,andportfolioadjustmentsmadeateach ipsumvelmollis.Curabiturquisdictumnisl.Phasellusvelsemper
stage. risus,etlaciniadolor.Integerultriciescommodosemnecsemper.
B.2 PartTwo
Etiamcommodofeugiatnislpulvinarpellentesque.Etiamauctor
sodalesligula,nonvariusnibhpulvinarsemper.Suspendissenec
lectusnonipsumconvallisconguehendreritvitaesapien.Donec
atlaoreeteros.Vivamusnonpurusplacerat,scelerisquediameu,
InvestmentStrategyReviewandOutlook
cursusante.Etiamaliquamtortorauctorefficiturmattis.
Phase1:CrisisResponse(Apr2:TariffShock)
News:OnApril2,theU.S.Presidentannounceda"LiberationDay"tariffpolicy, C OnlineResources
triggeringaglobalstockmarketsell-off.
Analysis:Themarketexperiencedasuddendownturn.Foraclientwitha Namidfermentumdui.Suspendissesagittistortoranullamollis,
"retirement"objective,theprimarytaskistostrictlycontrolportfoliodrawdown inpulvinarexpretium.Sedinterdumorciquismetuseuismod,et
andprotecthard-earnedcapital.Wemustadoptdecisivedefensivemeasures
sagittisenimmaximus.Vestibulumgravidamassautfelissuscipit
topreventpanicfromaffectingthelong-termplan.
PortfolioAdjustment: congue.Quisquemattiselitarisusultricescommodovenenatiseget
A-Shares Bonds Gold REITs dui.Etiamsagittiseleifendelementum.
27.9%↓ 26.6%↓ 38.0%↑ 7.5%↑ Naminterdummagnaatlectusdignissim,acdignissimlorem
Phase2:MarketObservation&FinalHedging(Apr8:Pre-Rebound rhoncus.Maecenaseuarcuacnequeplacerataliquam.Nuncpulv-
Signals)
News:OnApril8,"pre-reboundsignals"emergedasthestockmarketsawa inarmassaetmattislacinia.
minorrecoveryandtheCBOEVolatilityIndex(VIX)stabilized.
Analysis:Themarketdeclinehaspaused,butthetruetrendremainsuncertain.
Suchafragilereboundisnotworththerisk.Maintainingcautionandcomplet-
ingthefinaldefensiveadjustmentsarecrucialtoensureweareinthesafest
positionbeforethesituationfullyclears,allowingustoseizetheinitiativelater.
PortfolioAdjustment:
A-Shares Bonds Gold REITs
18.9%↓ 34.3%↑ 41.3%↑ 5.5%↓
Phase3:DecisiveRe-entry(Apr9:TariffSuspension)
News:OnApril9,thesuspensionofsometariffswasannounced,leadingtoa
rapidrecoveryinglobalriskassets.
Analysis:Thisdefinitivepositivenewshasturnedthemarket’sdirection.While
ourpreviousdefensiveposturewassuccessful,wemustnowrespondswiftly.
Toavoidmissingthecoreofthisrally,weneedtoactimmediatelyandreinvest
capitalintotheA-sharemarket,akeyoffensivemoveinour"phasedre-entry"
plan.
PortfolioAdjustment:
A-Shares Bonds Gold REITs
36.0%↑ 24.9%↓ 31.4%↓ 7.3%↑
Phase4:TrendConfirmation&Steadiness(Apr11:ConsumerConfi-
denceDrop)
News:OnApril11,theUniversityofMichiganConsumerSentimentIndexfell
toanear-recordlow,creatingmixedmarketsignals.
Analysis:Negativemacroeconomicnewsservesasareminderthatthemarket’s
foundationisnotyetsolid.Thisconfirmsthewisdomofourearlierdecision
nottogoall-inatonce.Duringsuchperiodsofmixedsignals,thebeststrategy
istoremainpatient,maintainthecurrentallocation,andobservefurtherdevel-
opments.
PortfolioAdjustment:
A-Shares Bonds Gold REITs
36.0%(Hold) 24.9%(Hold) 31.4%(Hold) 7.3%(Hold)
Phase5:CrisisAversion&Normalization(May2:U.S.StocksRecover)
News:OnMay2,U.S.stockserasedall"LiberationDay"losses.
Analysis:Themarketturmoilhassubsided,andyourportfoliohassuccessfully
passedthisstresstest.Our"defensefirst,offenselater"tacticprovedeffective.
Themarket’sfocusnowreturnstofundamentals,andsoourfocusmustshift
fromshort-termresponsesbacktoyoureight-yearretirementobjective.
PortfolioAdjustment:
A-Shares Bonds Gold REITs
36.0%(Hold) 24.9%(Hold) 31.4%(Hold) 7.3%(Hold)
165