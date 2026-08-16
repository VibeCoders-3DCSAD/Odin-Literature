---
conversion_metadata:
  converted_at: "2026-07-21T09:26:54Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Xu et al.pdf"
  source_pdf_sha256: "cb95375b890d363a14648b3924167029ebc96295205a8e5a41317630b0570dda"
  page_count: 35
  markdown_char_count: 338641
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

6
2
0
2

r
a

M
6
1

]
I

A
.
s
c
[

2
v
0
8
6
2
2
.
2
0
6
2
:
v
i
X
r
a

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and
Future Directions
YUE XU, ShanghaiTech University, China
QI’AN CHEN, Tongji University, China
ZIZHAN MA, The Chinese University of Hong Kong, China
DONGRUI LIU, Shanghai Artificial Intelligence Laboratory, China
WENXUAN WANG, Renmin University of China, China
XITING WANG, Renmin University of China, China
LI XIONG, Emory University, United States
WENJIE WANG†, ShanghaiTech University, China

Large language models have enabled agentic systems that reason, plan, and interact with tools and environments to accomplish
complex tasks. As these agents operate over extended interaction horizons, their effectiveness increasingly depends on adapting
behavior to individual users and maintaining continuity across interactions, giving rise to personalized LLM-powered agents (PLAs).
In such long-term, user-dependent settings, personalization permeates the entire decision pipeline rather than remaining confined to
surface-level response generation. This survey provides a capability-oriented review of personalized LLM-powered agents. Existing
work is organized around four interdependent capabilities: profile modeling, memory, planning, and action execution. Using this
taxonomy, representative methods are synthesized and analyzed to illustrate how user signals are represented, propagated, and
utilized across the agent pipeline, highlighting cross-component interactions and recurring design challenges. Evaluation metrics
and benchmarking paradigms tailored to personalized agents are further examined, along with application scenarios ranging from
conversational assistants to domain-specific expert systems. By clarifying the design space of personalization in agent systems,
this survey provides a structured foundation for developing more user-aligned, adaptive, and deployable LLM-powered agents.

CCS Concepts: • General and reference → Surveys and overviews; • Human-centered computing; • Computing method-
ologies → Intelligent agents;

Additional Key Words and Phrases: Personalization, Personalized LLM-powered Agent

ACM Reference Format:
Yue Xu, Qi’an Chen, Zizhan Ma, Dongrui Liu, Wenxuan Wang, Xiting Wang, Li Xiong, and Wenjie Wang†. 2026. Toward
Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions. ACM Comput. Surv. 1, 1 (March 2026), 35 pages.
https://doi.org/XXXXXXX.XXXXXXX

Introduction

1
Large language models (LLMs) have evolved from passive text generators into general-purpose reasoning systems
capable of understanding diverse data, planning actions, and using external tools. Building on these capabilities,
LLM-powered agents extend LLMs into integrated systems that decompose complex objectives, invoke tools, interact
with dynamic environments, and coordinate with humans or other agents to achieve high-level goals over extended

† Corresponding Author.
Authors’ Contact information: Yue Xu, ShanghaiTech University, China; email: xuyue2022@shanghaitech.edu.cn; Qi’an Chen, Tongji University,
China; email: 2250951@tongji.edu.cn; Zizhan Ma, The Chinese University of Hong Kong, China; email: zzma2@cse.cuhk.edu.hk; Dongrui Liu,
Shanghai Artificial Intelligence Laboratory, China; email: liudongrui@pjlab.org.cn; Wenxuan Wang, Renmin University of China, China; email:
wangwenxuan@ruc.edu.cn; Xiting Wang, Renmin University of China, China; email: xitingwang@ruc.edu.cn; Li Xiong, Emory University, United
States; email: lxiong@emory.edu; Wenjie Wang, ShanghaiTech University, China; email: wangwj1@shanghaitech.edu.cn.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are
not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for
components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM 1557-7341/2026/3-ART
https://doi.org/XXXXXXX.XXXXXXX

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 2 -->

2

• Y. Xu et al.

horizons [1, 110, 192, 204]. This shift marks not only a technical expansion of LLM capabilities but also a broader
shift toward autonomous, adaptive, and socially grounded intelligent assistants.

As agent systems increasingly support long-term interaction and autonomous decision-making, personalization
emerges as a central requirement for maintaining contextual continuity and aligning agent behavior with individual
user preferences across domains such as education, healthcare, and recommendation [24, 139, 208]. For personalized
LLM-powered agents (PLAs), personalization extends beyond response style and operates across the full decision
pipeline, influencing how agents infer user intent, preserve user-relevant information over time, generate personalized
plans, and carry out actions in external environments [194, 261]. However, this broadened scope also introduces
substantial challenges, including integrating dynamic and multimodal feedback, preserving consistency across
interacting components, reconciling user-specific adaptation with general competence, and safeguarding privacy and
security. As a result, the evaluation of PLAs must move beyond static correctness and instead account for long-term
effectiveness, adaptability, and user satisfaction.

Despite the growing interest, reviews on PLAs remain fragmented. Prior surveys often focus on isolated capabilities
of general LLM-powered agents or isolated components of personalization, such as user modeling and memory
construction [227, 260], planning and reasoning strategies [217], or adaptive interaction mechanisms [38, 94]. Such
capability-specific perspectives have provided valuable insights, but a unified view of how personalization objectives
propagate across the full agent lifecycle is still lacking. In particular, the interactions among different personalization
mechanisms and their implications for evaluation and deployment remain insufficiently understood.

To address this gap, this survey presents a capability-oriented and system-level perspective on PLAs. We examine
personalization as a distributed property instantiated across four interdependent components: profile modeling,
memory, planning, and action execution. This decomposition enables a systematic analysis of how user-specific
signals are represented, propagated, and operationalized throughout the agent lifecycle, from intent understanding to
real-world outcomes. As illustrated in Figure 1, when an individual user submits a request, a PLA coordinates these
four capabilities to produce a tailored response. Profile representations and role definitions shape the agent’s internal
model of the user, the memory module organizes and retrieves relevant contextual information, planning determines
personalized decision strategies, and action execution grounds these decisions in the external environment. The
resulting outcomes, together with subsequent user feedback, in turn refine the agent’s internal representation of user
preferences, forming a closed loop that enables iterative and sustained personalization over time.

Building on this taxonomy, we review representative methods, benchmarks, and evaluation protocols, summarize
major application domains, and identify open challenges and future research directions. The survey aims to clarify the
design space of personalized agents, connect benchmark-driven research with real-world deployment requirements,
and provide a structured foundation for developing trustworthy, effective, and scalable personalized agent systems.

Our contributions are as follows:

(1) We introduce a unified taxonomy that organizes personalized LLM-powered agents around four core capabilities
(profile modeling, memory management, planning, and action execution), providing a system-level view of
how personalization is realized across the agent pipeline (§2).

(2) We present an extensive review of recent techniques, benchmarks, and evaluation protocols (§3–§7), highlighting
how personalization mechanisms operate within and across agent components and how personalization is
assessed in practice.

(3) We survey representative application domains of personalized agents and discuss open challenges and promising

research directions (§8-§9).

2 Foundations of Personalized LLM-powered Agents
2.1 LLM-powered Agents
An LLM-powered agent is an autonomous system that integrates a large language model with external tools and
utilities to support step-by-step interaction with open-ended environments for task completion [35]. The environment
includes both the user and the execution context, and is characterized by an external state space S that governs
environment dynamics and feedback.

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 3 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

3

Fig. 1. Overview of personalized LLM-powered agents. Upon receiving a user request, the agent coordinates profile modeling,
memory, planning, and action execution to generate a tailored response. Interaction outcomes provide feedback that refines user
preference representations, enabling iterative and long-term personalization.

At each time step 𝑡, the environment is in a state 𝑠𝑡 that captures the externally available information relevant to
the task, including user inputs, tool outputs, or other external signals. The agent maintains an internal state ℎ𝑡 , which
captures accumulated context such as retrieved memory, intermediate reasoning results, and internal representations
used for decision making. The agent’s behavior can be abstracted as a policy that selects an action 𝑎𝑡 conditioned on
both the current environment state and its internal state:

𝜋 (𝑎𝑡 |𝑠𝑡, ℎ𝑡 ).
Actions may correspond to natural language responses, planning steps, tool invocations, or other environment
interactions. The environment then evolves according to a controlled transition process, producing a subsequent
external state 𝑠𝑡 +1, and the agent updates its internal state accordingly as

ℎ𝑡 +1 = 𝑓 (ℎ𝑡, 𝑎𝑡, 𝑠𝑡 +1).
Starting from an initial state 𝑠0, such as a user query or task specification, execution proceeds iteratively until a
termination condition is met, yielding a trajectory

𝜏 = (𝑠0, ℎ0, 𝑎0, 𝑠1, . . . , 𝑎𝑇 −1, 𝑠𝑇 ).
This trajectory reflects the agent’s evolving interpretation of the task and its interaction history. For analysis or
evaluation purposes, execution outcomes can be assessed using a feedback or reward function defined over the
trajectory, denoted as 𝑟 = R (𝜏).

At the system level, LLM-powered agents rely on a set of tightly coupled cognitive capabilities that enable adaptive
and goal-directed behavior [110, 204]. Profiling shapes how the agent interprets its role and operating context. Memory
supports continuity by retaining and organizing information across interactions. Planning governs the transformation
of high-level objectives into structured decision processes. Action execution realizes these decisions through tool use
or direct interaction with the environment. Together, these capabilities elevate large language models into interactive
decision-making systems capable of sustained autonomy.

2.2 Personalized LLM-powered Agents
A personalized LLM-powered agent is an LLM-based agent whose internal pipeline is adapted to individual users
through user-specific preferences. For each user 𝑢 ∈ U, the agent maintains a representation of the user’s preferences
𝑝𝑢 inferred from interaction history, feedback, or explicit input.

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 4 -->

4

• Y. Xu et al.

At each time step 𝑡, the environment is in a state 𝑠𝑡 , and the agent maintains an internal state ℎ (𝑢 )

specific to the
user. The agent interprets and acts upon user preferences by conditioning its decision policy on 𝑝𝑢. This yields a
user-conditioned policy

𝑡

𝜋 (𝑎𝑡 |𝑠𝑡, ℎ𝑡, 𝑝𝑢),
which selects an action 𝑎𝑡 given the current environment state, internal state, and user preferences. The environment
transitions to a new state 𝑠𝑡 +1, and the agent updates its internal state as

ℎ𝑡 +1 = 𝑓 (ℎ𝑡, 𝑎𝑡, 𝑠𝑡 +1, 𝑝𝑢),
where user preferences may be explicitly stored within the internal state or provided as an external conditioning
signal. Executing this policy from an initial state produces a user-conditioned interaction trajectory
𝜏 (𝑢 ) = (𝑠0, ℎ (𝑢 )
0

, 𝑠1, . . . , 𝑠𝑇 ),

, 𝑎 (𝑢 )
0

where the superscript (𝑢) indicates that the trajectory is induced by decision-making conditioned on user preferences.
Personalization refers to the process through which user preferences are accumulated, represented, and integrated
into an agent’s decision pipeline, allowing the same task specification Q to give rise to different outcomes for different
users. Through repeated interaction, the agent collects user-centric data D𝑢 and refines an internal preference
representation ˆ𝑝𝑢 = 𝑝 (D𝑢), which conditions subsequent action selection. At an abstract level, personalization can
be viewed as favoring decisions that yield higher user-aligned utility over interaction trajectories:

𝜋 ∗
𝑢 ∝ arg max

𝜋

E𝜏 (𝑢) ∼𝜋 (· | Q, ˆ𝑝𝑢 ) R𝑢 (𝜏 (𝑢 ) ),

where ˆ𝑝𝑢 denotes an internal representation of user preferences maintained by the agent, and R𝑢 (𝜏 (𝑢 ) ) denotes
feedback reflecting user-specific satisfaction or alignment.

From a system perspective, personalization forms a closed interaction loop. User-specific preference representations
condition the agent’s perception, reasoning, and action selection; executed actions shape subsequent interactions;
and the resulting outcomes provide new signals that refine ˆ𝑝𝑢. Through repeated execution of this loop, personalized
LLM-powered agents progressively align their behavior with individual users, enabling long-term adaptivity and
consistent user-specific behavior.

2.3 User-Centric Data
The internal representation of user preferences in LLM-powered agents is grounded in user-centric data, which
captures contextual information, feedback, and interaction traces associated with a specific user. From a temporal and
functional perspective, user-centric data can be broadly divided into historical data and interaction data.

Historical Data refers to information available before task execution, including user identifiers, demographic
attributes, and records of prior interactions and feedback. This context provides a front-loaded prior over the user for
the current episode, capturing relatively stable user characteristics together with accumulated evidence from past
interactions, which supports consistent behavior and cross-task generalization.

Interaction Data is generated during task execution and captures real-time user inputs, feedback, and contextual
cues. It includes both explicit signals, such as corrections or ratings, and implicit signals, such as behavioral patterns
or response timing. Interaction data reflects the user’s momentary intent and is critical for guiding immediate
decision-making, including reasoning adjustments and dynamic action selection.

These two data types enable dual-timescale personalization: historical data defines who the user is, while interaction
data determines how the agent should act now. As illustrated in Figure 2, historical data guides the agent’s behavior
during interaction, while interaction data refines and expands the historical record, together forming a continuous
cycle of user-aware adaptation.

2.4 User Preferences
User preferences constitute the core signals that enable personalization in LLM-powered agents by conditioning their
internal state, decision-making processes, and user-specific feedback. Prior work commonly categorizes preferences
according to their mode of expression [87, 261]. Explicit preferences are directly specified by users and can be

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 5 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

5

Fig. 2. User-specific data in personalization process.

incorporated into the agent without additional inference. Implicit preferences are inferred indirectly from behavioral
patterns or contextual cues, reflecting user judgments in a latent or under-specified form.

Beyond expression form, preferences can be characterized by their semantic function, capturing which aspect
of the user they encode. We distinguish behavioral preferences, which govern how users communicate and reason,
and topical preferences, which specify what users prioritize in a given context. Behavioral preferences encompass
tone, reasoning style, general interaction tendencies, and personality-related traits, and are often stable across tasks.
Topical preferences cover domain interests, factual stances, and likes or dislikes toward specific entities or events,
and vary more with context. Both types can be stated explicitly or inferred implicitly, yielding the two-dimensional
taxonomy in Figure 3.

Fig. 3. Example of a two-dimensional taxonomy of user preferences. Preferences are categorized by their expression form (explicit
vs. implicit) and semantic function (behavioral vs. topical), illustrated through a multi-turn recommendation scenario.

In practical systems, explicit preferences can be represented in various forms, including reward vectors [10],
preference embeddings [141], or natural-language prompts [76]. Although explicit signals are often highly informative,
they are typically sparse, which limits their direct applicability for optimization. As a result, implicit preferences are
frequently leveraged through in-context prompting [75], retrieval-augmented generation (RAG; [144]), or preference
modeling techniques [45] that extract structured representations from user behavioral feedback. When performing
such an extraction, accounting for the semantic function of preferences enables more targeted modeling strategies
and improves interpretability.

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 6 -->

6

• Y. Xu et al.

2.5 Capability-oriented Taxonomy
Personalization in LLM-powered agents emerges from the coordinated operation of multiple internal capabilities
rather than from a single adaptation module. Given the diversity of user data, task settings, and preference types,
user-specific signals must be represented, retained, reasoned over, and operationalized throughout the whole pipeline.
We therefore adopt a capability-oriented taxonomy (illustrated in Figure 4) that organizes personalization into four
interdependent components:

Personalization in LLM-powered agents does not arise from a single adaptation module, but from the coordinated
operation of multiple capabilities distributed across the agent pipeline. Given the diversity of user data, task settings,
and preference types, user-specific signals must be represented, retained, reasoned over, and ultimately realized in
external actions and outcomes. We therefore adopt a capability-oriented taxonomy that organizes personalization
into four interdependent components. These components are not isolated modules, but complementary functional
stages that together support end-to-end personalization in agent systems.

(1) Profile Modeling structures user-specific information into internal representations, defining both user charac-

teristics and the agent’s role.

(2) Memory maintains and retrieves user-relevant information across interactions, supporting temporal continuity

and consistent preference grounding.

(3) Planning integrates user-specific information into reasoning processes, shaping decision paths, strategy

selection, and prioritization under contextual constraints.

(4) Action Execution operationalizes personalized decisions through tool invocation and environment interaction,

enabling the final personalized outcome.

To further clarify the distinctions among these four capabilities, Table 1 compares them along several shared
dimensions, including their typical inputs, temporal scope, and primary objectives, providing a unified analytical lens
for the remainder of the survey. In the following sections, we review each capability in detail, while noting that most
existing methods focus on only one or a subset of these capabilities rather than the full pipeline.

Table 1. Comparison of the four core capabilities in personalized LLM-powered agents.

Capability

Typical Inputs

Temporal Scope

Primary Objective

Profile Modeling

Memory

Planning

Action Execution

User attributes, behavioral his-
tory, and user instructions
Interaction history, user events,
contextual records
Profile information, memory, task
context, in-task feedback
Plans, tool states, execution feed-
back

Lifelong

Turn to lifelong

Turn to task

Step to task

Establish user understanding and sup-
port agent-user alignment
Maintain temporal continuity and con-
sistent personalization
Enable personalized reasoning and de-
cision making
Realize personalized actions and out-
comes

3 Profile Modeling
In general-purpose agent systems, profiles are primarily used to define the agent itself, including its intrinsic attributes,
behavioral tendencies, and operational boundaries [110]. Such identities are often static or externally specified through
fixed role instructions, domain expertise, or pre-defined functional assignments [224, 251]. In PLAs, however, profile
modeling becomes explicitly user-centered, modeling the user and dynamically shaping how the agent positions itself
when carrying out tasks for that user. In this sense, profile modeling serves as the foundational layer of PLAs, linking
user understanding with agent role configuration. Accordingly, we discuss profile modeling from two complementary
perspectives: user profile modeling and agent role definition.

3.1 User Profile Modeling
User profile modeling extracts and organizes user-specific signals into representations that can guide how an agent
should respond or act [221]. In this survey, we distinguish two major paradigms according to how user preferences

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 7 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

7

Profile Modeling
§3

User Profile
Modeling

AlignXpert [87], FSPO [175], [201], RLPF [223], RLPA [263],
CURIO [197], PFM [10], PReF [168], LoRe [12],
Janus [82],
PLUS [125],

Agent Role
Definition

ASFM [39], LD-Agent [86], RecAgent [205], PAA [85], Per-
sonaAgent [254], PersonaX [172], RPP [115],

Memory
§4

Planning
§5

t
n
e
g
A
d
e
r
e
w
o
p
-
M
L
L
d
e
z
i
l
a
n
o
s
r
e
P

Action Execution
§6

Evaluation
§7

Memory
Schemes

Personalized
Retrieval

One-shot
Planning

Feedback-
Driven
Planning

Pre-Action

LD-Agent [86], MemoryBank [269], SeCom [136], RMM
[187], Nemori [126], CAIM [219], PREMem [77], Mem-
oBase [119], MemInsight [154], MIRIX [209], Mem-𝛼
[213], MemWeaver [246], M3-Agent [109], RAPTOR [160],
MemTree [152], SGMem [230], LicoMemory [57], Mem0 [22],
Memory-R1 [241], A-Mem [237], TRAIL [264]

RAPTOR [160], [247], HippoRAG [65], AriGraph [5], Zep
[150], MemGAS [233], AssoMem [252], PBR [257], Person-
aRAG [248], UniMS-RAG [200], Persona-DB [180], OCG-
Agent [171], MemInsight [154]

ALIGNXPLORE [88], ReaRec [189], PbP [234], PRIME [256],
PSG-Agent [226], TravelPlanner++ [176], PTS [165], PREFINE
[195], IoTGPT [245]

SAGE-Agent [183], ECLAIR [124], Ask-before-Plan [255],
AIPOM [74], Dango [18], PlanFitting [173], VAIAGE [101],
Collab-Rec [9], SceneWeaver [244]

PEToolLLaMA [235], PUMA [14], ToolSpectrum [20], Color-
Agent [90], AWARE-US [80], [55], ValuePilot [111]

Post-Action

PEAR [96], MIR [232], WARPP [117], ETAPP [50]

Goals and
Metrics

Benchmarks

Effectiveness, Adaptivity, Generalization, Robustness, Risk

Interactive
Alignment

User-
Substitution

IndieValueCatalog [63], ALOE [225],
AgentRecBench [164], LongMemEval
[222], PTBench [55], ETAPP [50], Per-
sonaMem [61], PENGUIN [229]...

LongLaMP [79], PGraphRAG [7], Per-
sonaConvBench [89], LaMP-QA [157],
PRISM [78], PEToolBench [235], Trip-
Tailor [203], PersONAL [270]...

Fig. 4. Taxonomy of personalized LLM-powered agents.

are represented: persona-based approaches, which model the user through relatively holistic traits and preference
descriptions, and response-based approaches, which model the user through preferences over candidate responses or
model behaviors.

Persona-based Modeling. Persona-based methods model the user through relatively stable traits, characteristics,
and long-term preference descriptions that remain informative across contexts. Such profiles may be constructed
from explicit self-descriptions, behavioral history, or historical interactions, and are often represented as structured
attribute vectors or free-form natural-language persona summaries. In downstream use, persona-based profiles are
often incorporated as prompts or constraints to guide personalized generation and decision making. For instance,
AlignXpert [87] constructs a high-dimensional preference space grounded in psychological and alignment-related
dimensions, while FSPO [175] produces more fine-grained persona descriptions through a user-description chain-
of-thought mechanism. Beyond such one-shot profiling, several methods iteratively refine user representations
through interaction: RLPA [263] and Wang and Yang [201] update user representations across rounds, RGMem
[191] hierarchically aggregates user insights from episodic memory. Relatedly, RLPF [223] optimizes concise, human-
readable user summaries using a feedback loop tied to downstream performance, and CURIO [197] introduces an
intrinsic motivation objective that encourages active inference of latent user types during multi-turn interaction.

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 8 -->

8

• Y. Xu et al.

Response-based Modeling. Response-based modeling represents user preferences through how users evaluate
candidate outputs, thereby capturing more fine-grained and context-sensitive notions of what constitutes a preferred
response. Compared with persona-based approaches, which emphasize holistic user descriptions, response-based
approaches focus more directly on user satisfaction with model behavior. In downstream use, these representations
are naturally suited to feedback-driven correction and refinement of personalized outputs. A common strategy
is to factorize individual preference into a shared reward feature basis with user-specific weights, enabling rapid
adaptation under sparse user data. RFM [10], PReF [168], and LoRe [12] follow this paradigm by inferring user-specific
coefficients from limited feedback. Complementarily, some methods represent preferences in natural language to
improve interpretability and controllability. Janus [82] organizes preference dimensions hierarchically from coarse
categories to fine-grained value descriptions, while PLUS [125] learns text-based preference summaries that condition
downstream reward modeling for personalized scoring and generation.

3.2 Agent Role Definition
While user profile modeling focuses on representing the user, agent role definition determines how the agent should
position itself with respect to that user. We distinguish between user-substituting agent definition, where the agent is
configured to act on behalf of the user, and user-adaptive agent definition, where the agent dynamically adjusts its role
to better serve a real user during interaction.

User-substituting Agent Definition. User-substituting role definition is common in delegation-oriented and simulation
scenarios, where agents are expected either to perform tasks from the user’s perspective or to generate user-like
behaviors and dialogue data. In these cases, the agent is configured to act on behalf of the user by instantiating the
user’s profile as its role configuration. The resulting role prior then guides planning and execution toward personalized
objectives [128]. This form of role definition does not primarily rely on online adaptation to a real user, but remains
important for user proxy execution, realistic human-agent simulation, and scalable generation of diverse synthetic
users [39, 85, 205].

User-adaptive Agent Definition. In interactive personalized systems, PLAs adapt themselves to better support the
user during collaboration. Here, the agent role becomes conditional on the user profile, allowing the agent to adjust its
persona, tone, level of autonomy, or interaction strategy according to the user’s profile. This forms a two-way adaptive
process in which user understanding informs role configuration, and the adapted role in turn affects subsequent
interaction. Representative methods realize user-adaptive role definition through either joint persona modeling
or profile-conditioned prompt adaptation. LD-Agent [86] adopts a bidirectional user-agent modeling framework
[238] with a tunable persona extractor and a long-term persona bank for both users and agents. PersonaAgent
[254], PersonaX [172], and RPP [115] instead adapt the agent role through user-conditioned prompts or profiles:
PersonaAgent optimizes user-specific system prompts via textual loss feedback, PersonaX combines offline multi-
persona profiling with online profile retrieval, and RPP generates personalized discrete prompts from historical user
information and task guidance.

3.3 Discussion

Role and Challenges. Profile modeling provides the foundational layer of personalization by determining both
how the user is represented and how the agent is configured in response to that representation. They bridge raw
user-related evidence with downstream personalized memory, planning, and action. At the same time, they face
several tightly coupled challenges. User profiling must first cope with sparse, noisy, and inconsistent preference
signals. Beyond signal quality, a separate challenge is determining which user-related features are genuinely relevant
for downstream personalization. In parallel, agent role definition must balance adaptability with stability across tasks,
avoiding both rigid role assignments and undesirable role drift. Finally, a broader challenge lies in the requirement of
effective coupling and bidirectional alignment between user profiling and agent role adaptation.

Future Directions. Existing user profiling methods often produce representations that are either overly static or
narrowly task-specific, while agent roles often lack controllability or principled adaptation dynamics. Moreover,
user profiling and agent role definition are typically developed in isolation, with limited mechanisms for mutual

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 9 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

9

adjustment. Promising directions therefore include lightweight and interpretable profiling methods that remain robust
under sparse or noisy signals, as well as unified frameworks that jointly model evolving user profiles and stable yet
adaptive agent roles.

4 Memory
While profile modeling captures relatively stable and high-level user characteristics, personalized agents also require
mechanisms for retaining user-related information across interactions. Memory provides this capability by enabling
the system to store, recall, and leverage past experience to improve future behavior [218]. Memory is commonly
divided into personal memory, which stores user inputs and interaction histories, and system memory, which records
intermediate reasoning states or task-execution artifacts [227]. This survey focuses on personal memory, as it
directly shapes how agents adapt to individual users.

Personal memory can be implemented either as internal memory, which embeds user-related information within the
LLM, or as external memory, which stores such information in an auxiliary system. Internal memory may be realized
through model parameters, key–value caches, or hidden states [129, 144, 207, 211, 231, 259]. Although compact
and parameter-efficient [212], internal memory is limited by constrained capacity, difficulties in updating stored
information, and frequent reliance on retraining, making it less suitable for dynamic and long-horizon personalization.
By contrast, external memory is more flexible and typically operates through retrieval-augmented generation (RAG;
83) to incorporate stored user information into the current context.

External personal memory can further be viewed at different temporal scales, including short-term memory, which
retains recent conversational context, and long-term memory, which accumulates enduring user information across
sessions. Short-term memory supports immediate responses but is constrained by context windows, whereas long-
term memory enables the accumulation of long-tail personal information and continual adaptation [64], yet is more
vulnerable to information overload and stale content. As a result, many personalized agents adopt hybrid designs
that combine both. In the remainder of this section, however, we focus on long-term external personal memory,
where the structured design of personalized memory has been most extensively studied. We discuss it from two
perspectives: personal memory schemes, which determine how user-related information is stored and updated, and
personalized retrieval, which determines how stored information is accessed to support personalized behavior.

4.1 Memory Schemes
Memory schemes determine how user-related information is organized, stored, and updated over time. In long-term
external personal memory systems, this mainly involves the design of memory structure and update mechanism.

4.1.1 Memory Structure. Memory structure determines what information is stored and how it is represented, thereby
shaping the scalability and usefulness of personal memory. Early agent systems often stored full dialogue histories or
execution trajectories directly [104], but such raw storage introduced redundancy and made it difficult to surface
user-relevant information. Recent methods therefore transform interaction histories into more compact and task-
adaptive representations [103, 269]. Based on representation format, these structures can be broadly grouped into
textual memory and structured memory.

Textual Memory. Textual memory stores user-related information in natural language form, typically by summariz-
ing multi-turn interactions into concise and interpretable units. Because such representations preserve rich semantics
and align naturally with the input–output format of LLMs, textual memory has become a common choice for person-
alized agents across diverse tasks [260]. Its design mainly involves two key challenges: determining the granularity
of memory units through appropriate segmentation, and preserving user-relevant information accurately within
those units. Early approaches often relied on rigid turn-level or session-level segmentation, which could fragment
semantically coherent interactions and hinder retrieval. Recent work therefore explores more flexible, topic-consistent
segmentation strategies. For example, SeCom [136] and RMM [187] partition conversations into semantically coherent
segments, while Nemori [126] further improves segmentation by detecting episode boundaries and preserving the
integrity of user intent. Once appropriate memory units are formed, a second challenge is to preserve user-relevant
information faithfully and compactly. Many systems augment textual memory with auxiliary attributes such as

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 10 -->

10

• Y. Xu et al.

timestamps, topic labels, and user personality [103, 119, 237]. For instance, CAIM [219] augments memory entries
with tags, inductive thoughts, and timestamps, while MemInsight [154] extracts structured semantic attributes from
dialogue for richer memory augmentation. More recently, some works draw inspiration from human memory systems
by introducing multi-level organizations that distinguish semantic and episodic memory [107, 109, 140]. For example,
MIRIX [209] adopts a hierarchically organized multi-component memory architecture, and Mem-𝛼 [213] combines
core, semantic, and episodic memory with reinforcement learning for memory management. Overall, these efforts
move textual memory toward more coherent segmentation, more faithful preservation of user-relevant content, and
better support for long-term personalization.

Structured Memory. Structured memory represents interaction histories in predefined formats with explicit orga-
nizational relationships, making stored information easier to manipulate computationally. Compared with textual
summaries, it introduces stronger inductive biases for scalable retrieval, multi-granularity reasoning, and fine-grained
personalization. Current approaches can be broadly grouped into vector-based memory, hierarchical tree structures,
and graph-based memory architectures.

Vector-based memory encodes each memory unit as an embedding stored in a vector database, enabling efficient
similarity search and fast retrieval of user-relevant information. Owing to its efficiency and flexibility, this design
has become a common practice in memory modules [22, 133, 230]. However, vector memory alone provides limited
interpretability and does not explicitly capture relations among memory items, motivating more structured alternatives
or hybrid systems that combine vectors with explicit organizational formats. Hierarchical tree structures organize
memory at multiple abstraction levels, where parent–child relations encode increasingly coarse summaries. For
example, RAPTOR [160] and MemTree [152] recursively cluster and summarize text into trees, supporting retrieval at
both fine- and coarse-grained levels. Graph-based architectures capture richer relationships by linking memory
units through typed edges that encode temporal, semantic, or relational dependencies [22, 65, 97]. Some methods
emphasize behavioral coherence. For example, MemWeaver [246] constructs an event-level behavior graph in which
interaction events are connected by temporal and semantic edges, together with a context-aware random walk
mechanism. Other designs instead integrate multi-dimensional subgraphs to model more nuanced relations among
memory units. AriGraph [5] combines semantic knowledge with episodic observation nodes to support both long-
term accumulation and temporally grounded recall, while Zep [150] organizes memory into a temporally aware
multi-tier knowledge graph spanning episodic, semantic, and conceptual levels. While expressive, graph-based
memory often depends on costly LLM-based extraction and may lose fine-grained context during graph construction.
Lightweight variants therefore simplify graph design while preserving contextual information. SGMem [230] uses
sentence-level graph organization, whereas LiCoMemory [57] adopts a lightweight hierarchical indexing graph with
full content stored externally. Overall, structured memory aims to provide richer organization by explicitly modeling
how user-related information is organized, connected, and abstracted across interactions.

4.1.2 Update mechanism. The update mechanism determines how memory evolves as new interactions arrive,
ensuring that stored information remains useful over time. When a new memory unit is observed, the system must
decide whether to add it as a new entry, merge it with existing memory, revise outdated content, or discard irrelevant
information [34]. In external personal memory systems, updates differ between textual memory, where summary-level
content is rewritten or reorganized, and structured memory, where nodes, edges, and their relations are modified. We
discuss these two cases separately.

Textual memory stores interaction histories as natural-language segments or summaries. Updating therefore
concerns how these units are merged, rewritten, or reorganized as new dialogue arrives. Existing approaches can be
broadly grouped into similarity-driven updates and inference-guided updates.

Similarity-driven updates. These methods update memory by comparing new content with existing entries and
applying merge, revision, or replacement operations based on semantic similarity and auxiliary metadata. Earlier
approaches, such as RMM [187] and CAIM [219], perform summary-level merging and refinement. Mem0 [22]
makes this process more explicit through ADD, UPDATE, DELETE, and NOOP operations over candidate memories, while
Memory-R1 [241] further learns the update policy with reinforcement learning across multi-session interactions.

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 11 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

11

Inference-guided updates. Other systems treat memory updating as a reasoning or decision-making process, allowing
the agent to incorporate implicit preference shifts or contextual dynamics not captured by similarity alone. Nemori
[126] exemplifies this through its Predict–Calibrate mechanism, achieving proactively evolving memory based on gaps
between predicted and actual user responses. PREMem [77] similarly performs pre-storage reasoning across sessions
to analyze thematic evolution before inserting new content, enabling more consistent long-term topic tracking.
These methods provide more adaptive and self-correcting memory dynamics, capturing both short-term changes and
long-term shifts in user preferences.

Structured memory organizes information into interconnected architectures where inserting a new unit often
requires reorganizing its related counterparts. Update mechanisms can likewise be grouped into similarity-driven and
reasoning- or agentic-driven strategies.

Similarity-driven updates. These methods update structured memory by matching new information to existing units
through semantic similarity and then applying local structural modifications to preserve coherence. In hierarchical
tree structures, MemTree [152] traverses the tree by semantic similarity, inserts new nodes through sibling attachment
or leaf expansion, and incrementally updates ancestor summaries to maintain hierarchical consistency. In graph-based
memory, updates are more complex because each node may connect to multiple others [57]. Mem0𝑔 [22] matches new
triples to existing nodes, adds metadata-rich edges, and uses an LLM-based conflict resolver to deactivate outdated
relations. Similarly, Zep [150] updates episodic facts through timestamp-aware alignment while adjusting inconsistent
edges and higher-level clusters, and MemGAS [233] selectively reinforces contextually relevant cross-granularity
associations to maintain long-horizon personalization.

Reasoning-guided updates. An emerging line of work uses explicit reasoning or decision-making to guide memory
updates, moving beyond similarity matching toward more adaptive update dynamics. A-mem [237] exemplifies this
direction by treating each new memory as a structured note that triggers semantic linking and retroactive refinement
of historical notes, enabling a self-evolving memory graph. Although not designed specifically for personalization,
systems such as TRAIL [264] and AriGraph [5] further suggest that reasoning-guided graph evolution can support
more coherent memory updates.

4.2 Personalized Retrieval
Memory retrieval determines which stored information becomes available to an agent at inference time and therefore
directly influences the quality and consistency of personalized behaviors. Unlike conventional RAG systems, retrieval
for personalized LLM-powered agents must simultaneously satisfy three requirements: (1) content relevance to the
current query, (2) structural consistency with the underlying memory organization, and (3) personal alignment with
the user’s preferences. Existing retrieval methods address these challenges through three dominant mechanisms:
content-based retrieval, structure-aware retrieval, and policy-guided retrieval.

Content-based retrieval. Content-based retrieval selects relevant memory primarily through semantic or lexical
similarity between the current query and stored information, typically using dense or sparse retrievers [59, 68, 153].
Retrieved content is then incorporated into the agent’s prompt to improve contextual grounding [77, 209, 237]. This
mechanism can also operate at multiple levels of granularity. For example, RAPTOR [160] and MemTree [152] retrieve
memory across different abstraction levels based primarily on query similarity, even when the stored memory is
hierarchically organized. Some methods further refine retrieval after the initial search. For instance, Yuan et al. [247]
uses self-reflection to assess whether the retrieved content is sufficient for response generation and revise the query
when necessary. While effective for semantic matching, content-based retrieval does not explicitly model structural
dependencies among memory items and may therefore overlook long-range contextual relations.

Structure-aware retrieval. Structure-aware retrieval accesses memory by explicitly exploiting graph, hierarchy, or
episodic relations, rather than relying on content similarity alone. These methods often operate hierarchically, where
the retrieval of entities, topics, or relations guides subsequent access to detailed memory units [47, 65], sometimes
with graph-based techniques such as Personalized PageRank (PPR; 8). For example, AriGraph [5] retrieves relational
triplets before retrieving relevant episodic memories, while Zep [150] combines semantic search with graph-structured

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 12 -->

12

• Y. Xu et al.

signals such as episode frequency and node distance. More adaptive variants include MemGAS [233], which combines
entropy-based routing with PPR over an association graph, and AssoMem [252], which performs multi-signal ranking
over clue nodes and linked utterances. By modeling dependencies among memory units explicitly, structure-aware
retrieval better captures long-range and implicit user preferences.

Policy-guided retrieval. Policy-guided retrieval refers to retrieval strategies in which memory access is controlled by
user- or task-conditioned decision policies rather than by static similarity matching alone. Such a policy determines
how retrieval should proceed, including how queries are formed, which retrieval tools are invoked, and whether
additional information should be acquired. One line of work focuses on pre-retrieval query transformation,
where personalized retrieval intent is constructed before search. For example, PBR [257] generates user-style pseudo
feedback and corpus-anchored expansions to form a personalized query representation, while PersonaRAG [248]
adapts document selection and ranking using real-time behavioral signals. A second line of work adopts policy-driven
strategy selection, learning to invoke or combine heterogeneous retrieval tools according to task needs. UniMS-RAG
[200] formulates retrieval as a policy-learning problem over keyword search, dense retrieval, and knowledge-graph
lookup, while Persona-DB [180] employs a persona-aware policy to combine retrievals from target and collaborator
users for improved personalization under sparse data. A third direction incorporates schema-guided information
completion, framing retrieval as a structured inference process. OCG-Agent [171] decomposes narrative queries into
schema fields, retrieves relevant information through multiple routes, and iteratively supplements missing attributes
until the schema is completed. Overall, policy-guided retrieval shifts retrieval from passive matching toward active
decision making, enabling more flexible and personalized information acquisition.

4.3 Discussion

Role and Challenges. Personal memory bridges short-term interaction context with long-term preference modeling,
fulfilling three closely related roles. It provides personalized contextual grounding by preserving fine-grained user
details that cannot be fully encoded in static profiles, supports preference evolution by allowing the agent to track how
user preferences change across sessions, and enables preference-conditioned generation by supplying user-relevant
signals at inference time. At the same time, these roles make personal memory difficult to design effectively. User
preferences evolve at different rates, requiring memory systems to balance rapid adaptation with the preservation
of long-term traits. Memory stores may also accumulate redundancy or hallucinations, especially when updates
rely on LLM-based summarization or relation extraction, leading to degraded personalization over long horizons.
Moreover, retrieving content that is not only semantically relevant but also truly aligned with user preferences
remains a persistent challenge. Finally, personal memory raises privacy and transparency concerns, highlighting the
need for user-controllable and privacy-preserving memory mechanisms.

Future Directions. These limitations point to several promising directions across the memory pipeline. One is
hybrid memory architectures that combine the semantic richness of textual representations with the organizational
clarity of structured formats. Another is more principled and user-controllable update mechanisms that improve
reliability, transparency, and long-term consistency. A third is retrieval strategies that better integrate personal
alignment with semantic relevance, so that retrieved information is not only related to the query but also truly useful
for personalization.

5 Planning
In PLAs, planning is the stage at which user-specific information is translated into actionable decisions. While profile
modeling captures what is known about the user and memory preserves user-related information over time, planning
determines how these signals shape subgoal decomposition, strategy selection, and trade-off resolution during task
execution [110, 181]. Thus, it goes beyond generic task completion and instead seeks to optimize user utility by
aligning decisions with individual preferences, constraints, and latent intents [37, 48, 261]. We organize existing
methods into two broad paradigms according to how user signals enter the planning process: One-shot Planning, in
which personalization is incorporated as a prior during plan generation, and Feedback-driven Planning, in which
personalization is progressively refined through interaction [183, 255].

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 13 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

13

5.1 One-Shot Planning
One-shot personalized planning generates a complete plan within a single inference pass, where the plan is represented
as a structured decomposition of subgoals and decisions conditioned on user-specific constraints and latent intent.
We analyze this paradigm along two complementary axes: user signal grounding, which concerns how user signals
are incorporated into the planning process, and internal refinement, which concerns how an initial plan is internally
improved within the same inference pass.

5.1.1 User Signal Grounding. One-shot planning can ground user-specific information in two main ways. One directly
conditions planning on existing user representations, such as explicit profiles, retrieved memory, or compressed
interaction history. The other infers planning-ready constraints or objectives from heterogeneous user signals before
plan generation.

Profile and Memory Conditioning. These methods condition one-shot planning on existing user representations,
such as explicit profiles, retrieved memory, or compressed interaction history, thereby helping maintain consistency
with both long-term preferences and recent context [187, 219]. PRIME [256] integrates a dual-memory architecture
with a Personalized Thought Process that explicitly traces how past experiences and stable beliefs influence current
decisions. Before plan generation, PRIME synthesizes a personalized thought trace via self-distillation, effectively
grounding planning in the user-specific cognitive context. PersonaAgent [254] adopts a retrieval-augmented persona
mechanism, dynamically constructing system prompts from a unified memory bank to maintain cross-session planning
consistency. Related work in recommendation and dialogue systems similarly shows that structured user memory
retrieval significantly improves alignment and coherence in one-shot decision-making [17, 54].

Preference Induction. Complementary to direct conditioning, this line of work constructs a planning-ready user
state by inferring latent intent and translating heterogeneous user signals into explicit constraints or soft objectives
that guide plan generation [48]. For instance, ALIGNXPLORE [88] utilizes a User-description Chain-of-Thought
framework to synthesize a compact, semantically grounded preference description from sparse interaction traces.
Instead of retrieving raw logs, the model performs extended inductive reasoning to form global preference constraints
that condition downstream planning. Similarly, in sequential recommendation, ReaRec [189] proposes a Think-Before-
Recommend paradigm, using reasoning position embeddings to infer the user’s latent intent trajectory prior to plan
generation. In embodied and decision-making contexts, PbP [234] demonstrates that treating learned user preferences
as intermediate abstractions substantially improves few-shot personalized planning performance.

Internal Refinement. Internal refinement improves one-shot planning by first generating an initial plan and
5.1.2
then internally critiquing and revising it against a user-conditioned objective. General self-refinement frameworks,
such as Reflexion and structured critique-and-revise methods, provide reusable mechanisms for reflective feedback
and plan editing [44, 174], while recent test-time-compute reasoning models make deeper within-pass self-correction
increasingly practical [46, 121]. Representative systems instantiate this paradigm in several domains. In personalized
travel planning, TravelPlanner++ [176] and PTS [165] iteratively refine intermediate itineraries under implicit long-
horizon user preferences. PREFINE [195] constructs a pseudo-user critic and user-specific rubrics from interaction
history to critique and revise candidate plans. In embodied command execution, IoTGPT [245] performs self-correction
by testing intermediate command sequences in a simulated environment before deployment.

5.2 Feedback-Driven Planning
Feedback-driven planning treats an initial plan as a provisional hypothesis to be refined through interaction. It is
motivated by the fact that user intent is often underspecified, evolving, or only partially observable [108, 255]. Rather
than committing to a fixed plan in a single pass, these systems iteratively update plans to converge toward a more
personalized solution [183, 202]. We organize this paradigm according to the source of feedback and how it updates
the plan, including clarification seeking, user revision, and non-user feedback.

Clarification Seeking. A central challenge in feedback-driven personalized planning lies in deciding when to
ask for additional information: excessive clarification increases user burden, while premature commitment risks
misinterpreting user-specific constraints or latent intent. Prior studies indicate that user requests in planning tasks are

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 14 -->

14

• Y. Xu et al.

frequently underspecified or ambiguous [108], motivating approaches that treat clarification as decision-making under
uncertainty. For instance, SAGE-Agent [183] formulates selective questioning as a POMDP and issues clarification
queries only when the expected value of information outweighs interaction cost. Similarly, ECLAIR [124] focuses on
detecting missing arguments or ambiguous entities in user instructions and triggers targeted follow-up questions
before committing to a plan. Additionally, Ask-before-Plan style frameworks [255] explicitly decouple clarification
from plan synthesis, showing that resolving key uncertainties upfront improves robustness and downstream plan
quality.

User Revision. User edits provide a high-fidelity personalization signal that can update user-conditioned objectives,
constraints, and preferences for subsequent planning and generation. Gao et al. [37] shows that learning latent
preferences from historical edits can reduce future edit effort and improve user-specific alignment in subjective
settings. Building on this mixed-initiative view, AIPOM [74] represents plans as editable structures, enabling users
to revise intermediate plans while the agent updates constraints and priorities accordingly. Similar revision loops
appear in domain systems such as Dango [18], which supports iterative correction of agent-produced data-processing
workflows, and PlanFitting [173], which refines personalized exercise plans through conversational revisions. Similar
revision patterns are also increasingly visible in deployed coding assistants [6, 41].

Non-user Feedback. Beyond direct user input, plans can also be refined through non-user signals that improve
feasibility and preference satisfaction without repeatedly increasing interaction burden. One source is agent-mediated
feedback. For example, VAIAGE [101] employs specialized agents to negotiate route feasibility and recommendations
under user preferences, while Collab-Rec [9] supports multi-stakeholder planning through explicit user-advocacy
mechanisms. Another source is environment-mediated feedback, where intermediate outcomes are simulated and
used to trigger re-planning. For instance, SceneWeaver [244] follows a Reason–Act–Reflect loop and revises plans
when intermediate rendering results reveal violations.

5.3 Discussion

Role and Challenges. Planning serves two complementary roles in PLAs. First, it operationalizes personalization by
translating user intent inference and preference modeling into downstream decisions, instantiating user-contingent
objectives, constraints, and trade-offs that govern plan generation [17]. Second, especially in feedback-driven set-
tings [74], planning functions as a closed-loop optimization process that alternates between eliciting informative
feedback and revising the plan, enabling the agent to progressively uncover user intent and move toward stronger
personalization. However, these roles introduce several challenges at the same time. User intent and preferences
are often only partially observed and may evolve over time [108, 183], making it difficult to decide when to infer,
elicit, and commit. Moreover, personalized utility is inherently multi-objective [165], requiring arbitration among
competing constraints and idiosyncratic trade-offs. In interactive settings, refinement must also remain controllable
and convergent, limiting user burden while avoiding unstable revisions. These difficulties are reflected in the trade-off
between existing paradigms: one-shot planning offers low-latency and coherent decisions by internalizing user signals
as priors, but can be brittle under sparse or shifting signals, whereas feedback-driven planning improves alignment
through iterative elicitation and revision at the cost of additional latency and user effort [101].

Future Directions. Promising directions include uncertainty-aware planning workflows that adaptively allocate
internal computation and revision effort according to confidence in inferred preferences and task stakes [121], thereby
combining the efficiency of one-shot planning with the alignment benefits of feedback-driven refinement. Another
direction is to learn user-conditioned planning patterns at both inter- and intra-user levels [146], capturing systematic
differences in decomposition style and trade-off resolution while modeling their stability and drift over time. More
broadly, important but still under-explored directions include robustness to variation in user specification [183] and
privacy-preserving planning [229] that supports long-horizon user conditioning without exposing raw personal data.

6 Action Execution
Action execution is the stage at which a PLA realizes decisions through concrete operations in external environments
and receives feedback from execution outcomes [73, 167]. Unlike purely task-centric execution, personalized execution

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 15 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

15

must ground actions in user-specific constraints and preferences, while remaining adaptive when tools or environments
produce unexpected outcomes. We organize personalized action execution into two stages: a pre-action stage that
selects and parameterizes actions under user-conditioned constraints, and a post-action stage that leverages execution
signals for recovery and preference-consistent outcome realization.

6.1 Pre-action Stage
The pre-action stage focuses on user-conditioned action decision and grounding. It translates a selected intent or
plan step into executable tool calls or environment operations under user-specific constraints. We further decompose
this stage into action policy, which selects among functionally valid execution options for a given step, and action
grounding, which instantiates the selected action with user-specific arguments and realizations.

6.1.1 Action Policy. At this level, personalization manifests as a bias over functionally valid execution choices,
spanning both tool utilization and higher-level action selection. PEToolLLaMA [235] formalizes personalized tool
learning from interaction history and trains models to improve preference-aware tool selection. In web-agent settings,
PUMA [14] adopts a similar preference-aware learning strategy, while ToolSpectrum [20] further conditions tool
use on both user profiles and environmental context. Beyond tool invocation, ValuePilot [111] studies action-level
decision making under user values, showing that execution choices can be guided by individualized value preferences.
In cases of ambiguity, action policy may also involve proactive clarification. For example, ColorAgent [90] learns to
engage the user when intentions or instructions are incomplete before committing to an execution choice.

6.1.2 Action Grounding. Action grounding operationalizes a selected action by instantiating it into executable tool
calls with user-conditioned constraints and parameters [14, 20]. While many requests can be grounded by directly
applying user-specific settings, personalization becomes more challenging in corner cases. A frequent grounding-time
failure mode is infeasibility, where the instantiated query becomes unsatisfiable under the imposed constraints.
AWARE-US [80] frames this as a preference-aware query repair problem, arguing that agents should restore feasibility
by relaxing the least preferred constraints to the user rather than applying default heuristics. Another recurring issue
is the omission of essential tool arguments. Huang et al. [55] study how agents infer unspecified arguments from user
profiles, reducing execution friction while maintaining alignment with user intent.

6.2 Post-action Stage
The post-action stage closes the loop after an action is executed. Given execution result, the agent evaluates whether the
outcome satisfies user-conditioned objectives, applies corrective adjustments when mismatches arise (execution-time
correction), and produces final outputs that conform to user preferences and quality criteria (outcome realization).

6.2.1 Execution-Time Correction. A failed execution commonly produces feedback signals, which can be leveraged
for adjusting behavior without re-planning from scratch. Explicit studies on preference-aware recovery in PLAs
remain limited. Nevertheless, adjacent work suggests useful mechanisms for this stage. For example, research on
mitigating tool overuse under diminishing returns [143] and structured reflection over tool-interaction failures [179]
provides building blocks for future personalized recovery strategies.

6.2.2 Outcome Realization. Even when multiple execution outcomes are functionally valid, user satisfaction depends
on how final results are presented in accordance with individual preferences. One common mechanism is personalized
re-ranking, which transforms candidate results into outputs that better reflect user-specific utility [138]. Methods such
as PEAR and MIR explicitly model user preference features together with cross-item dependencies, producing more
faithful final rankings [96, 232]. Personalization may also govern which outcomes are retained or discarded: WARPP
[117] adjusts workflow branches at runtime based on user attributes, reducing irrelevant or erroneous outcomes
without re-planning the full process. Finally, outcome realization can extend beyond selecting among existing results
to proactively augmenting them. ETAPP [50] treats proactivity as a personalization signal, evaluating whether agents
can propose additional actions or suggestions to better satisfy user needs.

Role and Challenges. Action execution is the stage at which personalized decisions are translated into concrete
operations and external outcomes in PLAs [23, 148]. As such, it bridges high-level reasoning with observable behavior,

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 16 -->

16

• Y. Xu et al.

determining whether personalization is actually realized rather than remaining at the level of internal reasoning. This
stage is especially important because user experience depends not only on what the agent decides, but also on how
those decisions are instantiated and delivered. At the same time, personalized action execution remains challenging
for several reasons. Execution contexts are highly heterogeneous across tools, environments, and domains, making it
difficult to design general mechanisms that consistently respect individual preferences. Moreover, execution-time
personalization signals are often subtle, requiring abstract preferences to be translated into concrete parameters rather
than explicit instructions. Finally, execution feedback may reveal ambiguity or brittleness in how user preferences
were interpreted upstream, requiring careful handling and, in some cases, coordination with planning or preference-
modeling components to avoid cascading errors.

Future Directions. Research on personalized action execution remains relatively limited, leaving several promising
directions open. One is the development of personalization-aware execution primitives and tools that account not
only for task correctness but also for non-functional user preferences. Another is learning preference-conditioned
execution policies that generalize across tools and environments, enabling agents to reuse personalization signals
more effectively. It is also important to improve how agents handle vague or missing arguments, localize execution
failures, and aggregate outcomes in ways that reflect user priorities rather than default heuristics. More broadly, this
stage would benefit from execution-level evaluation protocols that move beyond task success to assess preference
adherence, consistency, and user satisfaction.

7 Evaluation
Evaluating personalized agents requires going beyond conventional task-centric assessment, because the objective
is not only task correctness but also long-horizon, user-specific utility. This challenge stems from the fact that
human preferences are often implicit, context-dependent, and evolving through interaction, making personalization
difficult to measure with a single objective criterion. As a result, evaluation should capture not only whether an
agent completes a task, but also whether it aligns with an individual user’s preferences, expectations, and experience
over time. In this section, we provide a systematic overview of evaluation for personalized LLM-powered agents.
As summarized in Figure 5, we organize the discussion into three layers: evaluation goals and metric dimensions,
assessment paradigms, and representative benchmark families.

Fig. 5. Overview of evaluation for personalized LLM-powered agents. Evaluation is organized along three layers: (1) evaluation
goals and metric dimensions, including effectiveness, adaptivity, generalization, robustness, and risk; (2) assessment paradigms,
such as automatic scoring, rule-based checking, learned evaluators, and LLM-as-a-judge; and (3) representative benchmark
families, including interactive alignment and user-substitution settings.

7.1 Evaluation Goals and Metrics
A rigorous evaluation framework for personalized agents must reflect the multi-faceted nature of personalization
quality. Beyond objective task success, an agent should align with individual preferences, remain coherent across

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 17 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

17

contexts and over time, adapt when preferences are revealed or revised, and operate within safety and privacy
constraints. Motivated by these requirements, we organize evaluation metrics for personalized agents into five
complementary dimensions: Effectiveness, Adaptivity, Generalization, Robustness, and Risk, as illustrated in
Table 2. These metric dimensions do not apply uniformly across all capabilities, but provide a structured basis for
comparing personalized agents across tasks, preference sources, and assessment paradigms.

Table 2. Evaluation metrics for personalized LLM-powered agents.

Goal

Metric

Discovery Accuracy [63, 92]

Knowledge Integration Score [7, 199]

Preference Alignment [229, 262]

Effectiveness

Preference-Aware Planning Accuracy [234, 235]

Preference Lift [50, 92, 225]

Consistency Score [123]

Emotional Empathy [229]

Adaptation Success Rate [62, 164]

Selective Forgetting [52]

Adaptivity

Interaction Efficiency [92]

Proactivity [50]

Generalization Out-of-Domain Performance [62]

Robustness

Accuracy under Ambiguity [55, 135]

Misinformed Condition Performance [53]

Safety Rate [226]

Risk

Risk Sensitivity [229]

Privacy Leakage Rate [123, 266]

Over-Secrecy Rate [123]

Description
Measures whether the agent can correctly discover user preferences
or intents from the interaction.
Measures the ability of the model to incorporate user-specific knowl-
edge or persona information into generated outputs.
Measures the alignment between the agent’s output and user pref-
erences or stated constraints.
Measures whether multi-step plans or tool-use sequences conform
to individual user preferences.
Compares personalized outputs against a non-personalized baseline
on the same prompt, reporting the lift in preference score.
Measures the consistency of the agent’s textual style and expressed
personality across the whole conversation.
Measures the degree to which the response shows understanding
and compassion for the user’s emotional state.

Assesses the ratio of successful personalization after receiving new
preference signals.
Measures the ability to revise, overwrite, or remove previously
stored information of users when faced with contradictory evidence.
Measures the efficiency of adapting, such as number of turns, clari-
fication questions, or edits needed to satisfy user expectations.
Measures the ability of the agent to proactively identify user needs
and offering extra suggestions or actions to enhance user satisfac-
tion.

Measures the ability of the agent to generalize user preferences to
other scenarios or tasks without explicit instruction.

Measures the accuracy of the agent’s action when some information
is missing or ambiguous.
Evaluates the model’s ability to identify and reject incorrect infor-
mation when the user is misinformed.

Measures whether the agent can make safe decisions based on dif-
ferent user profiles.
Measures whether the agent can recognize and respond appropri-
ately to potential risks in the user’s context.
Measures the percentage of conversations in which the agent dis-
closes private information inappropriately in tasks related to users’
privacy information.
Measures the failures of utility that arise from excessive caution.

Effectiveness. Effectiveness captures whether a personalized agent can produce user-contingent utility rather than
merely generic helpfulness. It covers at least three aspects: whether the agent can infer what the user wants from
partial interaction traces or contextual signals; whether it can correctly incorporate user-specific information into
planning and generation; and whether the final response or action actually satisfies explicit constraints and implicit
preferences. Metrics such as Discovery Accuracy [63], Knowledge Integration Score [7, 199], Preference Alignment
[229, 262], and Preference-Aware Planning Accuracy [234, 235] target these aspects from different angles. Beyond
absolute alignment, Preference Lift [50, 92, 225] measures gains over a non-personalized baseline under the same

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 18 -->

18

• Y. Xu et al.

prompt. In multi-turn settings, Consistency Score [123] evaluates stability of persona and values over time, while
Emotional Empathy [229] captures whether responses remain affect-appropriate and supportive.

Adaptivity. Adaptivity evaluates whether a personalized agent can update its behavior as new evidence about
user preferences becomes available, while preserving continuity and minimizing user burden. Adaptation Success
Rate [62, 164] measures whether the agent improves personalization after receiving explicit feedback, additional
constraints, or new user context. Because preferences may evolve or even contradict earlier evidence, Selective
Forgetting [52] is equally important for assessing whether outdated memory can be revised, overwritten, or removed
appropriately. Interaction Efficiency [92] captures the cost of adaptation, such as the number of turns, clarifications,
or edits required before the user accepts the result. Proactivity [50] complements these metrics by measuring whether
the agent can anticipate needs and offer helpful next steps at the right time without creating unnecessary interruption
or irrelevant suggestions.

Generalization. Generalization captures whether personalization transfers beyond the contexts in which it was
originally learned. In practice, a useful personalized agent should not require the user to restate preferences for every
new domain, task, or situation. Out-of-Domain Performance [62] therefore measures whether preferences acquired
in one setting can be applied appropriately in others. This dimension is especially important for general-purpose
agents that are expected to support diverse daily activities, where personalization must remain reusable rather than
narrowly tied to a single task context.

Robustness. Personalized agents operate under noisy, incomplete, and sometimes misleading preference evidence, so
evaluation must measure reliability under stress rather than only average-case alignment. Two robustness pressures
are especially important. First, user preferences are often underspecified, partially observed, or expressed indirectly.
Accuracy under Ambiguity [55, 135] therefore evaluates whether the agent can make reasonable inferences, ask
targeted clarification questions, and avoid overconfident assumptions when key signals are missing. Second, user
inputs may be incorrect or based on misconceptions. Misinformed Condition Performance [53] measures whether the
agent can identify flawed premises, provide corrective guidance, and still preserve a personalized interaction style.

Risk. Risk metrics quantify safety, privacy, and other downside constraints that are inseparable from personalization.
Safety Rate [226] measures whether the agent remains safe across heterogeneous user profiles, including cases where
user preferences may conflict with policies or where requests involve risky actions. Risk Sensitivity [229] evaluates
whether the agent can recognize contextual hazards and calibrate its advice appropriately, for example, by providing
warnings, suggesting safer alternatives, or encouraging professional help when needed. Because personalization
relies on user-specific information, Privacy Leakage Rate [123, 266] measures whether the agent discloses private data
in disallowed ways, especially under adversarial or indirect prompts. Conversely, Over-Secrecy Rate [123] captures
utility loss from excessive caution, where the agent withholds benign but helpful information despite a legitimate
request. These metrics reflect the central challenge of maximizing user utility while respecting risk constraints.

7.2 Assessment Paradigms
The metric dimensions above can be operationalized through different assessment paradigms, depending on whether
the target criterion is objectively verifiable or inherently user-contingent. We group mainstream paradigms into
four families. (1) Automatic scoring applies when ground-truth labels or reference answers are available. Typical
examples include accuracy and precision/recall/F1 for classification, as well as overlap-based metrics such as BLEU
[137] and ROUGE [100] for generation. (2) Rule-based constraint checking evaluates whether outputs satisfy
explicit and verifiable requirements, such as including required attributes, avoiding forbidden ones, or respecting
structured preference constraints. This paradigm is especially useful for delegation-style tasks in which compliance
can be deterministically validated. (3) Learned LLM-based evaluators (LLM-E) train dedicated evaluation models
to assess specific preference dimensions, often providing more stable and fine-grained diagnostic feedback at the
cost of reduced generality [198]. (4) LLM-as-a-judge (LLM-J) uses a general-purpose LLM as the evaluator for
user-contingent criteria such as preference alignment, tone, and satisfaction. In this setting, the judge is typically

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 19 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

19

conditioned on a user profile or preference description and asked to score or rank candidate outputs [267]. To improve
reliability, LLM-J protocols often adopt pairwise comparison, calibrated rubrics, and multi-judge aggregation.

7.3 Benchmark
Building on the above metric taxonomy, we summarize representative benchmarks for personalized agents and
organize them into two broad families. Interactive Alignment Benchmarks evaluate an agent’s ability to elicit, negotiate,
and refine user preferences through multi-turn interaction, where the user remains an indispensable part of the loop.
In contrast, User-Substitution Benchmarks evaluate whether an agent can stand in for the user by simulating their
preferences or persona to produce user-consistent responses or decisions without further user input. Mainstream
benchmarks are summarized in Table 31.

7.3.1

Interactive Alignment Benchmarks.

Preference Discovery Benchmarks. A core challenge in interactive alignment is preference discovery, where the
agent must recognize, infer, and iteratively refine user intents and preferences from heterogeneous signals, ranging
from explicit instructions to implicit feedback and contextual cues [193]. In this category, IndieValueCatalog [63]
curates value-expressing statements from diverse individuals and evaluates whether models can infer individualized
value judgments, highlighting limitations in capturing fine-grained personal values. PersonaBench [186] constructs
synthetic yet realistic personal profiles and associated artifacts to test whether agents can extract and reason over
user-specific information. PrefDisco [92] proposes a meta-evaluation framework that emphasizes interactive elicitation
efficiency, measuring whether an agent can proactively ask informative questions for a user-aligned solution with
minimal interaction turns.

Output-level Alignment Benchmarks. This category evaluates personalization in an end-to-end manner, focusing on
whether the agent’s final outputs satisfy a target user’s preferences and constraints in realistic interactive settings.
For conversation-centered personalization, benchmarks such as ALOE [225] and PrefEval [262] test whether agents
can infer, retain, and consistently follow user preferences across multi-turn dialogues. Beyond conversational tasks,
PDR-Bench [99] evaluates whether agents can incorporate user profiles into research workflows and produce outputs
that are practically useful for the end user. For recommendation, AgentRecBench [164] and RecBench+ [53] assess
whether agents can generate preference-conditioned recommendations and adapt to user feedback. More generally,
PersonaLens [265] targets multi-scenario, task-oriented assistants and evaluates whether personalization remains
coherent across diverse domains and user intents.

Component-probing Benchmarks. Complementary to the above, component-probing benchmarks provide controlled
testbeds that isolate specific personalization capabilities, enabling diagnostic analysis of when and how an agent
leverages user information. PersonaFeedback [190] pairs predefined personas with queries and asks the model to
select persona-consistent responses, offering a direct probe of preference-conditioned alignment. A major sub-line
focuses on personalized memory, including LongMemEval [222], LoCoMo [114], PerLTQA [30], MemoryAgentBench
[52], ConvoMem [135], and PAL-Bench [56], which test whether agents can organize, retrieve, and apply user-specific
memories under long conversations or incremental preference revelation. For personalized tool use, ETAPP [50]
and PTBench [55] evaluate whether agents tailor tool-invocation strategies to user needs, including proactivity and
handling missing or ambiguous information. Some benchmarks explicitly target adaptivity over time; for example,
PersonaMem [61, 62] assess whether an agent can track evolving traits and preferences, revise outdated beliefs, and
generalize them to new scenarios. Finally, several benchmarks diagnose user-specific risk, such as PSG-Agent [226]
and PENGUIN [229] that evaluate profile-contingent safety considerations for LLM-based agents, while PrivacyBench
[123] and AgentDam [266] test privacy compliance for agents when handling sensitive user information.

7.3.2 User-Substitution Benchmarks.

Textual and Dialogue Benchmarks. Textual and dialogue personalization benchmarks focus on evaluating how
models generate content that aligns with individual user preferences, styles, and contextual knowledge. For instance,

1Some benchmarks can partially span both families, and we place them in the major category to avoid duplication.

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 20 -->

20

• Y. Xu et al.

long-form generation tasks, as in LaMP [156] and LongLaMP [79], test whether models can adapt outputs to evolving
user interests over time, while PEFT-U [26] reformulates classification problems into annotator-specific instances to
measure user-conditioned generation capabilities. Benchmarks that leverage retrieval or knowledge graphs, such
as PGraphRAG [7], further examine performance in sparse or cold-start scenarios. Beyond single-turn generation,
multi-turn conversational benchmarks, including PersonaConvBench [89], PER-CHAT [228], LaMP-QA [157],
DPL [147], REGEN [161], and KBP [199]—assess whether models maintain coherence, adapt to a user’s conversational
style, and integrate personalized knowledge consistently across dialogue. PRISM [78] targets more complex scenarios
where user values vary culturally or contextually, evaluating the reproduction of individualized subjective choices.

Planning and Tool-Use Benchmarks. Benchmarks in planning and tool-use examine whether personalized agents
can learn and apply user preferences to perform sequential or multi-step tasks. Preference-based Planning (PBP) [234]
simulates everyday activities across diverse environments to evaluate preference-driven planning, while PETool-
Bench [235] specifically measures the agent’s ability to select and use tools according to individual user preferences.
FamilyTool [210] extends this focus to complex tool-based workflows, emphasizing the integration of user-specific
needs. Broader multi-domain planning benchmarks, including TravelPlanner++ [176], TripTailor [203], TripCraft [16],
COMPASS [145], TripTide [71], and Personal Travel Solver (PTS) [165], assess tasks ranging from adaptive itinerary
generation to disruption handling, testing whether agents can interpret explicit or inferred preferences and construct
coherent, user-aligned plans.

Embodied and Spatial Benchmarks. Embodied and spatial benchmarks investigate whether agents can navigate,
manipulate objects, and ground actions in physical or simulated spaces according to user preferences. Memory-guided
interaction tasks, such as MEMENTO [81], assess the agent’s ability to recall user-specific cues, while PersONAL [270]
focuses on personalized navigation and object grounding in photorealistic home environments. Personalized Instance-
based Navigation (PIN) benchmark [11] adds further complexity by requiring agents to locate user-specific target
objects among distractors in 3D scenes, emphasizing individualized navigation strategies.

Table 3. Summary of Personalized Benchmark.

Benchmark

Scale

Task

Pref.

Goal

Eval.

Metrics

Interactive Alignment Benchmarks

IndieValueCatalog [63]

800

PersonaBench [186]
PrefDisco [92]

582
10,000

PersonalLLM [225]

ALOE [225]
PrefEval [262]

1000

100
3,000

Human
Value
General
General

General

General
General

AgentRecBench [164]

1,500

Recomm.

Inferred

RecBench+ [53]

34,494

Recomm.

PDR-Bench[99]

250

PersonaLens [265]

122,133

PersonaFeedback [190]
PerLTQA [30]

LoCoMo [114]

LongMemEval [222]

8,298
8,593

7,512

500

Deep
Research
Multi-
domain
General
Memory

Memory

Memory

Inferred

Inferred

Effectiveness

Auto.

Accuracy

Inferred
Interactive

Given,
Inferred
Inferred
Given,
Inferred

Given,
Inferred
Given

Given
Given,
Inferred
Inferred

Effectiveness
Effectiveness,
Adaptivity

Effectiveness

Effectiveness
Effectiveness

Effectiveness,
Adaptivity
Effectiveness,
Robustness
Effectiveness

Effectiveness
Effectiveness

Effectiveness,
Robustness
Effectiveness

Inferred

Effectiveness

Auto.
Auto.,
Rule-
based
LLM-J,
LLM-E
LLM-J
Auto.,
Rule-
based,
LLM-J
Auto.

Auto.

LLM-J

LLM-J

Auto.
Auto.,
LLM-J
Auto.

Auto.,
LLM-J

Recall, F1
Discovery Accuracy, Preference Alignment,
Interaction Efficiency, Correctness

Personalized Reward

Alignment Level, Improvement Rate
Accuracy, Personalized Rate

Hit Rate@N

Precision, Recall, Condition Match Rate, Fail
to Recommend
Personalization Alignment, Content Quality,
Factual Reliability
Task Completion Rate, Personalization,
Naturalness, Coherence
Accuracy
Accuracy, Precision, Recall, F1, Recall@K,
MAP, Coherence
Precision, F1, Recall@K, ROUGE

Accuracy, Precision, Recall, F1, Recall@K,
MAP, Coherence

Continued on next page...

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 21 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

21

Table 3 – Continued from previous page

Benchmark

Scale

Task

MemoryAgentBench [52]

146

Memory

Pref.

Inferred

ConvoMem [135]

75,336

Memory

Inferred

PAL-Bench [56]

100

Memory

Inferred

PTBench [55]

1,083

Tool Usage

ETAPP [50]

800

Tool Usage

Given,
Inferred
Inferred

PersonaMem [61]

5,990

General

Inferred

PersonaMem-v2 [62]

10,000

General

Inferred

PSG-Agent [226]

PENGUIN [229]

2,900

14,000

PrivacyBench [123]

478

Multi-
domain
Multi-
domain
General

User-Substitution Benchmarks

LaMP [156]
LongLaMP [79]
PEFT-U [26]
PERSONA [15]

PGraphRAG [7]
PersonaConvBench
[89]
PER-CHAT [228]
LaMP-QA [157]
DPL [147]
REGEN [161]

KBP [199]

PRISM [78]
PBP [234]
PEToolBench [235]

25,095
9,658
15,300
3,868

General
General
General
Dialogue

10,000
111,634

Text Gen.
Multi-
domain
1,500,000 General
29,666
9,472
1,258,224 Multi-

Q&A
Text Gen

9,821

1,500
50,000
3,000

TravelPlanner++ [176]

1,000

TripTailor [203]

3,800

TripCraft [16]

TripTide [71]

PTS [165]

PersonalWAB [14]
PersONAL [270]

PIN [11]

MEMENTO [81]

FamilyTool [210]

AgentDam [266]

1,000

1,000

1,000

38,000
1,800

1,193

1,900

1,152

246

Inferred

Given

Given

Inferred
Inferred
Inferred
Inferred

Inferred
Inferred

Inferred
Given
Inferred
Inferred

Given

Given
Inferred
Inferred

Inferred

Inferred

Inferred

Inferred

Inferred

Inferred
Inferred

Inferred

Inferred

Inferred

domain
Q&A

Decision
Planning
Tool Usage

Travel
Planning
Travel
Planning

Travel
Planning
Travel
Planning
Travel
Planning
Web Search
Embodied
Nav
Embodied
Nav
Embodied
Tasks
Tool Usage

Web Search

Given

Goal

Effectiveness,
Adaptivity

Effectiveness,
Adaptivity
Effectiveness

Effectiveness,
Robustness
Effectiveness,
Adaptivity

Effectiveness,
Adaptivity
Effectiveness,
Adaptivity
Risk

Risk

Risk

Effectiveness
Effectiveness
Effectiveness
Effectiveness

Effectiveness
Effectiveness

Effectiveness
Effectiveness
Effectiveness
Effectiveness,
Generalization
Effectiveness

Effectiveness
Effectiveness
Effectiveness,
Adaptivity
Effectiveness

Effectiveness,
Adaptivity

Effectiveness,
Adaptivity
Effectiveness,
Adaptivity
Effectiveness,
Adaptivity
Effectiveness
Effectiveness,
Adaptivity
Effectiveness,
Adaptivity
Effectiveness,
Adaptivity
Effectiveness,
Adaptivity
Risk

Eval.

Auto.

Auto.

Auto.,
LLM-J
Auto.

Rule-
based,
LLM-J
Auto.

Auto.

Auto.

LLM-J

LLM-J

Auto.
Auto.
Auto.
Auto.,
LLM-J
Auto.
Auto.,
LLM-J
Auto.
Auto.
Auto.
Auto.

Auto.,
LLM-J
LLM-J
Auto.
Auto.

Metrics

Accuracy, Recall@5, F1 in Accurate Retrieval,
Test-Time Learning, Long-range
Understanding and Selective Forgetting
settings
Accuracy, Cost, Latency

BLEU, Win Rate

Accuracy

Personalization Score, Proactivity Score

Accuracy

Accuracy

Accuracy, Precision, Recall, F1-score

Risk Sensitivity, Emotional Empathy,
User-specific Alignment
Leakage Rate, Over-Secrecy Rate,
Inappropriate Retrieval Rate, Consistency
Score

Accuracy, F1, MAE, RMSE, ROUGE
ROUGE, METEOR
BLEU, ROUGE-L, Distinct-1/2
Perplexity, BLEU, BERTScore, Persona
consistency
MAE, RMSE, ROUGE, METEOR
Accuracy, ROUGE, METEOR, BLEU, SBERT
similarity
Perplexity, BLEU
ROUGE-1, ROUGE-L, METEOR
ROUGE-1, ROUGE-L, BLEU, METEOR
Recall@K, NDCG@K, MRR, BLEU,
ROUGE-L, Semantic similarity
BLEU, ROUGE, Persona grounding,
Knowledge grounding
Preference agreement(LLM-J)
Levenshtein distance
Tool Accuracy

Auto.

Feasibility, Constraint satisfaction

Rule-
based,
Auto.,
LLM-J
Auto.,
LLM-J
Auto.,
LLM-J
Auto.

Auto.
Auto.,
LLM-J
Auto.,
LLM-J
Auto.,
LLM-J
Auto.

Feasibility, Rationality, Personalization

Temporal, Spatial, Ordering, Persona

Intent preservation, Adaptability

Constraint satisfaction, Preference alignment

Search accuracy, Rec. accuracy
Success, SPL, Grounding

Success, Path efficiency

Memory recall, Task success

Tool accuracy

LLM-J

Privacy Leakage Rate

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 22 -->

22

• Y. Xu et al.

8 Applications
Personalized LLM-powered agents have been applied across a wide range of settings, from conversational support and
content creation to delegated assistance and expert-domain workflows. These applications differ in autonomy level,
risk profile, and the primary target of personalization, but all require agents to translate user-specific information
into sustained, context-sensitive behavior. We organize representative applications into four groups: conversational
assistants, content creation, delegation assistants, and expert support in specific domains.

8.1 Conversational Assistant
Conversational assistants are personalized agents whose primary objective is to support users through ongoing
interaction. In this setting, personalization is realized through long-term dialogue continuity, context-sensitive
response generation, and adaptation to user-specific preferences, tone, and support needs. We organize representative
applications in this category into daily dialogue assistants, emotional support companions, and educational agents.

8.1.1 Daily Dialogue Assistants. Personalized dialogue assistants focus on maintaining long-term conversational
continuity, where agents must preserve user-specific context and produce preference-consistent responses across
interactions [53, 258]. Recent work increasingly treats long-horizon interaction itself as a benchmarked personal-
ization problem [135, 164], while studies of deployed assistants highlight how memory behavior shapes user trust
and expectations [69]. In recommendation and search settings, personalization further depends on sustained user
understanding, interaction history, and preference-aware decision making [214, 248, 250]. These trends are also
reflected in deployed assistants such as ChatGPT, Gemini, and DeepSeek, which support persistent user memories
and controllable personalization [28, 43, 134].

8.1.2 Emotional Support Companions. Emotional support companions provide sustained and empathetic assistance
for users’ well-being, where personalization depends strongly on preferred tone, boundaries, and proactivity [58].
In this setting, personalization can arise both from user-side customization of the agent’s persona and from agent-
side adaptation of supportive strategies during interaction [4, 268]. Representative systems include ComPeer [106],
which delivers proactive peer support based on dialogue history, MultiAgentESC [239], which uses a strategy-aware
multi-agent pipeline for emotionally complex interactions, and ARIEL [178], which further incorporates physiological
signals for affect-aware adaptation. Similar priorities are reflected in companion-style products such as Replika and
Pi, where long-term personalization and relationship-building are central design features [3, 151].

8.1.3 Educational Agents. Educational agents personalize instruction and support by adapting guidance, feedback,
and learning materials to individual users [98, 166]. A common distinction is between personalized pedagogical
agents, which support general teaching and learning workflows, and domain-specific agents, which tailor assistance
to specialized subjects [24]. Representative pedagogical systems such as EduAgent [236] and TeachTune [66] adapt
course support based on learner profiles and contextual signals, while domain-specific agents such as MathAgent
[242] and EduMAS [91] combine personalization with specialized knowledge to improve learning effectiveness. These
directions are also reflected in deployed educational systems such as Duolingo [31].

8.2 Content Creation
Personalized content creation concerns the generation of standalone textual artifacts, where agents adapt style,
structure, and framing to personalization targets rather than sustaining interactive dialogue [240]. In this setting,
personalization is evaluated at the artifact level, giving rise to two complementary paradigms: author-centric alignment
with individual writing style and audience-centric adaptation to reader knowledge, interests, or expectations [132].

8.2.1 Author-Centric. Author-centric content creation treats personalization as a requirement of authorship, where
users expect generated documents to reflect their writing style, habitual phrasing, and long-term preferences across
independent outputs [95, 240, 261]. This setting is particularly important in creative writing, professional documenta-
tion, and brand communication, where quality is judged at the artifact level rather than through dialogue. Deployed
systems such as Adobe Firefly reflect this paradigm by adapting generation to persistent user assets, prior documents,

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 23 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

23

or stylistic conventions [2, 60, 131]. Correspondingly, recent research highlights stable preference representations
and document-level alignment as central ingredients for effective authorial personalization [13, 29, 155, 195].

8.2.2 Audience-Centric. Audience-centric content creation personalizes text for target readers rather than for the
author, adapting content to audience knowledge, expertise, interests, or usage contexts while preserving the intended
information [32, 130, 253]. This paradigm appears in settings such as differentiated educational materials, culturally
adapted documentation, and audience-aware communication, where personalization operates at the level of reader
groups or segments. In practice, it is reflected in systems such as Predis.ai and SalesForge AI, which tailor generated
content to intended audience groups [142, 158]. Recent research similarly emphasizes audience alignment, relevance,
and comprehension as key criteria for quality in audience-conditioned generation [36, 113, 159, 169, 177, 188].

8.3 Delegation Assistants
Delegation assistants act on behalf of users by internalizing preferences, managing information, planning actions,
and adapting behavior over extended horizons. Compared with conversational assistants, they assume a stronger
degree of delegated responsibility and therefore require more persistent, user-aligned representations.

Information Handling. Information handling concerns the long-term acquisition, organization, retention,
8.3.1
and retrieval of user-specific knowledge as a delegated cognitive function. In this setting, personalization lies in
maintaining a coherent informational context that can support downstream planning and action without repeated
user input. Representative systems include ARAG [116] and SPARK [21], which treat retrieval as a personalized,
agent-driven process, as well as memory-centric assistants such as Mr.Rec [54] and log-contextualized RAG [27],
which use persistent interaction history to support continuity across tasks. Similar ideas appear in deployed systems
such as Glean and Mem [42, 118].

8.3.2 Task Planning. Task-planning delegation assistants translate high-level user goals into executable action
sequences while respecting user-specific preferences and contextual constraints. Personalization in this setting
is crucial for resolving trade-offs and prioritizing subtasks in a user-aligned way. Representative work includes
VAIAGE, which frames personalized travel planning as a collaborative multi-agent process under user requirements
[101], as well as learning-based approaches showing that explicitly modeling user preferences improves planning
quality and alignment [234]. Related work also extends personalized planning to collaborative, embodied, and social
decision-making settings [48, 149, 249].

8.3.3 Behavior Adaptation. Behavior adaptation concerns how delegation assistants align interaction style, initiative,
and decision tendencies with a user’s habitual patterns over time. It supports reliable delegation by internalizing stable
routines while remaining responsive to evolving goals, thereby reducing supervision and cognitive burden. MEAgent
models persistent user habits in mobile assistant settings [206], while memory-centric frameworks enable agents
to accumulate and reuse user-specific knowledge beyond single interactions [213, 220]. Test-time personalization
methods such as PersonaAgent further show that adaptive delegation can be realized dynamically through inferred
user personas without retraining [254]. At the same time, recent work highlights that more autonomous behavior
adaptation also increases the need for controllable personalization and safeguards against misalignment [40, 182].

8.4 Expert Support in Specific Domains
Personalized agents are increasingly deployed as expert assistants in specialized domains such as healthcare, finance,
legal services, and research workflows, where user-centric tailoring can improve relevance and usability but must be
reconciled with stringent domain constraints and risk-sensitive requirements [196].

8.4.1 Healthcare. In healthcare, personalization is shifting from single-turn question answering to longitudinal, state-
ful interaction, where agents must support a patient trajectory rather than only isolated diagnoses. Frameworks such
as MedChain and MedPlan organize multi-stage clinical pipelines spanning history elicitation, symptom clarification,
and treatment planning [51, 102]. To reduce the risks of over-accommodation and unsafe agreement, recent systems
increasingly adopt modular architectures that separate patient-facing communication from clinical verification, as
illustrated by Polaris and ColaCare [122, 215]. For data-intensive settings, EHRAgent further grounds personalized

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 24 -->

24

• Y. Xu et al.

EHR analysis in deterministic code execution rather than purely generative reasoning [67, 170]. Evaluation envi-
ronments such as AgentClinic highlight the need to stress-test personalized clinical agents under diverse simulated
patient behaviors [112, 163].

Finance. In finance, personalization must balance alignment with individual goals and behaviors against
8.4.2
cognitive bias, trust calibration, and hard compliance requirements. FinPersona-based studies reveal a trust–quality
paradox, showing that persona-driven personalization can increase user trust even when the underlying advice is
poorer or riskier [184, 185]. This motivates safety-aware personalization frameworks such as PSG-Agent, which
introduce personality-conditioned guardrails to calibrate recommendations [226]. At the architectural level, systems
such as FinRobot decompose workflows into specialized roles for data aggregation, quantitative analysis, and thesis
generation, while GraphCompliance constrains personalization with structured regulatory reasoning paths [25, 243].

8.4.3 Legal services. In legal services, personalization conditions reasoning on user-specific facts, jurisdictions, and
drafting intents, turning assistance into a context-sensitive inference problem. A central challenge is statutory drift,
where agents must apply evolving laws to individual cases rather than relying on static knowledge. Benchmarks such
as LawShift show that this adaptability must often be achieved at inference time rather than through retraining [49].
Personalization also amplifies hallucination risks in legal drafting, motivating post-hoc verification loops such as
Citation-Enhanced Generation and watchdog frameworks like HalMit, which validate outputs against authoritative
legal sources before delivery [93, 105]. This is especially important for multilingual and jurisdiction-aware legal
assistants such as Mina [216].

8.4.4 Research Assistance. Research assistance supports expert users across the research lifecycle by performing
project- and goal-conditioned scholarly work. Early systems position LLM agents as general research collaborators
for exploration and orchestration, as in Agent Laboratory [162], while later work moves toward user- and context-
conditioned pipelines for project scoping, retrieval, and dialogue [33, 120]. Multi-agent settings further extend this
into sustained, stateful workflows through virtual research groups and iterative investigation [84, 127]. Recent studies
emphasize human-centered deployment, trust, and verifiability in real research settings, while complementary work
explores personalized scaffolding and customized writing support for productivity [19, 70, 72].

9 Open Problems and Future Directions
Despite rapid progress, building robust, scalable, and deployable personalized agents remains an open challenge.
Many of the remaining difficulties are cross-cutting rather than module-specific: they arise from how user models
are constructed, updated, generalized, evaluated, and deployed under real-world constraints. Below, we summarize
several directions that we view as especially important for future research.

9.1 Decision-Critical User Modeling
A central open problem in personalized agents is how to represent user information in a form that is both expressive
and decision-relevant. User preferences vary not only across individuals but also across tasks, aspects of a task,
and even situations within the same user, and they are often revealed only indirectly through behavior, interaction
patterns, or tool usage. As a result, effective personalization requires more than rich user modeling: it also requires
identifying which user attributes actually matter for the decision at hand. This challenge is especially pronounced
across application settings, where general-purpose assistants may rely on broad stylistic or value alignment, while
domain-specific or high-stakes agents depend on fine-grained attributes that directly affect outcomes. Future work
should therefore focus on structured and adaptive user representations that can distinguish decision-critical signals
from peripheral ones, rather than assuming a fixed or universally relevant user model.

9.2 Temporal Dynamics and Continual Personalization
Personalization is inherently dynamic: user preferences are progressively revealed through interaction, and different
aspects of user information evolve at different temporal scales. Short-term interests may shift rapidly across contexts,
whereas long-term values, goals, or reasoning styles are often more stable. This temporal heterogeneity makes
static personalization mechanisms fundamentally inadequate. Future research should therefore develop continual

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 25 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

25

personalization methods that can update user representations over time without catastrophic forgetting, while
distinguishing transient preferences from durable ones. More broadly, personalized agents should close the loop
between observation and action, so that newly acquired signals can be incorporated in ways that maintain alignment
rather than gradually degrading it.

9.3 Generalization
Personalized agents must often operate under sparse, uneven, or missing user data, making generalization a core
challenge for real-world deployment. This problem arises along at least two dimensions. First, agents must generalize
to unseen or low-interaction users, where limited evidence makes direct preference inference unreliable. Second,
they must generalize across domains and tasks, where preferences learned in one context may only partially transfer
to another because task structures, action spaces, or decision criteria differ. Promising directions include few-shot
and meta-learning approaches for rapid adaptation, uncertainty-aware personalization that avoids overconfident
alignment under weak evidence, and transferable preference abstractions that capture reusable decision principles
rather than narrow task-specific behaviors.

9.4 Evaluation and Benchmarking
Evaluating personalization poses a unique challenge because success is defined relative to individual users rather than
objective task completion. Existing benchmarks often rely on synthetic user data generated by language models, which
may fail to capture real human diversity and can suffer from homogenization effects. Additionally, common evaluation
protocols such as LLM-as-a-judge raise concerns about reliability and alignment with human satisfaction. Future
evaluation frameworks should emphasize fine-grained, component-level analysis and distinguish between intra-user
consistency and inter-user differentiation. Incorporating human-in-the-loop evaluation, longitudinal interaction
studies, and user-centric satisfaction metrics may provide more faithful assessments of personalization quality.

9.5 Privacy and User Control
Personalization inherently depends on collecting, storing, and reusing user data, making privacy a central challenge
for deployment. Even when user data is stored separately, risks remain in the form of unauthorized access, unintended
leakage, or secondary misuse. Moreover, self-evolving agents may erode trust if users feel they no longer understand
or control how their information is being retained and applied. Future systems must therefore balance data utility
with privacy preservation through privacy-aware memory architectures, selective retention policies, on-device or
federated personalization, and transparent interfaces for inspecting, editing, and managing stored information. In
this sense, privacy should be treated not only as a technical safeguard but also as a core part of the user experience.

9.6 Efficiency and Deployment
A practical open problem is how to deliver meaningful personalization under real-world resource constraints. In
current systems, personalization is often implemented through post-training adaptation, inference-time augmentation,
memory retrieval, or repeated planning and tool use, all of which introduce additional storage, latency, and computation
costs. Future work should therefore explore workflow designs that explicitly trade off personalization depth against
deployment cost. Lightweight personalization mechanisms, adaptive memory usage, and budget-aware inference
strategies may allow agents to provide sustained user alignment without incurring prohibitive overhead.

10 Conclusion
Personalization is becoming a defining capability of LLM-powered agents, enabling them to move beyond generic task
execution toward sustained, user-aligned collaboration. This survey presented a system-level view of personalized
LLM-powered agents through four core capabilities: profile modeling, memory, planning, and action execution.
Overall, personalization should be understood not as an isolated module, but as a system-wide property of agent
design. Despite substantial progress, major challenges remain in user modeling, generalization, evaluation, privacy,
and efficiency. Future progress will require integrated architectures that support personalization together with
robustness, safety, and deployability.

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 26 -->

26

• Y. Xu et al.

References

[1] Deepak Bhaskar Acharya, Karthigeyan Kuppan, and B Divya. 2025. Agentic ai: Autonomous intelligence for complex goals–a comprehensive

survey. IEEe Access (2025).

[2] Adobe. 2023. Adobe Firefly — firefly.adobe.com. https://firefly.adobe.com/.
[3] Inflection AI. [n. d.]. Pi, your personal AI — pi.ai. https://pi.ai/onboarding/pi-intro.
[4] Jaber O Alotaibi and Amer S Alshahre. 2024. The role of conversational AI agents in providing support and social care for isolated individuals.

Alexandria Engineering Journal 108 (2024), 273–284.

[5] Petr Anokhin, Nikita Semenov, Artyom Sorokin, Dmitry Evseev, Andrey Kravchenko, Mikhail Burtsev, and Evgeny Burnaev. 2024. Arigraph:

Learning knowledge graph world models with episodic memory for llm agents. arXiv preprint arXiv:2407.04363 (2024).

[6] Anthropic. 2025. Common workflows - Claude Code Docs — code.claude.com. https://code.claude.com/docs/en/common-workflows.
[7] Steven Au, Cameron J Dimacali, Ojasmitha Pedirappagari, Namyong Park, Franck Dernoncourt, Yu Wang, Nikos Kanakaris, Hanieh
Deilamsalehy, Ryan A Rossi, and Nesreen K Ahmed. 2025. Personalized graph-based retrieval for large language models. arXiv preprint
arXiv:2501.02157 (2025).

[8] Bahman Bahmani, Abdur Chowdhury, and Ashish Goel. 2010. Fast incremental and personalized pagerank. arXiv preprint arXiv:1006.2880

(2010).

[9] Ashmi Banerjee, Adithi Satish, Fitri Nur Aisyah, Wolfgang Wörndl, and Yashar Deldjoo. 2025. Collab-REC: An LLM-based Agentic Framework

for Balancing Recommendations in Tourism. arXiv preprint arXiv:2508.15030 (2025).

[10] André Barreto, Vincent Dumoulin, Yiran Mao, Nicolas Perez-Nieves, Bobak Shahriari, Yann Dauphin, Doina Precup, and Hugo Larochelle.

2025. Capturing individual human preferences with reward features. arXiv preprint arXiv:2503.17338 (2025).

[11] Luca Barsellotti, Roberto Bigazzi, Marcella Cornia, Lorenzo Baraldi, and Rita Cucchiara. 2024. Personalized instance-based navigation toward

user-specific objects in realistic environments. Advances in Neural Information Processing Systems 37 (2024), 11228–11250.

[12] Avinandan Bose, Zhihan Xiong, Yuejie Chi, Simon Shaolei Du, Lin Xiao, and Maryam Fazel. 2025. LoRe: Personalizing LLMs via Low-Rank

Reward Modeling. arXiv preprint arXiv:2504.14439 (2025).

[13] Hyungjune Bu, Chanjoo Jung, Minjae Kang, and Jaehyung Kim. 2025. Personalized llm decoding via contrasting personal preference. In

Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing. 33946–33966.

[14] Hongru Cai, Yongqi Li, Wenjie Wang, Fengbin Zhu, Xiaoyu Shen, Wenjie Li, and Tat-Seng Chua. 2025. Large language models empowered

personalized web agents. In Proceedings of the ACM on Web Conference 2025. 198–215.

[15] Louis Castricato, Nathan Lile, Rafael Rafailov, Jan-Philipp Fränken, and Chelsea Finn. 2025. Persona: A reproducible testbed for pluralistic

alignment. In Proceedings of the 31st International Conference on Computational Linguistics. 11348–11368.

[16] Soumyabrata Chaudhuri, Pranav Purkar, Ritwik Raghav, Shubhojit Mallick, Manish Gupta, Abhik Jana, and Shreya Ghosh. 2025. Tripcraft:
A benchmark for spatio-temporally fine grained travel planning. In Proceedings of the 63rd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers). 17035–17064.

[17] Jiarui Chen. 2025. Memory Assisted LLM for Personalized Recommendation System. arXiv preprint arXiv:2505.03824 (2025).
[18] Wei-Hao Chen, Weixi Tong, Amanda Case, and Tianyi Zhang. 2025. Dango: a mixed-initiative data wrangling system using large language

model. In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems. 1–28.

[19] Zan Chen, Jingjing Chen, Yu Guang Wang, and Yiqing Shen. 2025. A Human-Centered AI Agent Framework with Large Language Models for
Academic Research Tasks. In CCF International Conference on Natural Language Processing and Chinese Computing. Springer, 363–374.
[20] Zihao Cheng, Hongru Wang, Zeming Liu, Yuhang Guo, Yuanfang Guo, Yunhong Wang, and Haifeng Wang. 2025. ToolSpectrum: Towards
personalized tool utilization for large language models. In Findings of the Association for Computational Linguistics: ACL 2025. 20679–20699.
[21] Gaurab Chhetri, Subasish Das, and Tausif Islam Chowdhury. 2025. SPARK: Search Personalization via Agent-Driven Retrieval and Knowledge-

sharing. arXiv preprint arXiv:2512.24008 (2025).

[22] Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. 2025. Mem0: Building production-ready ai agents with

scalable long-term memory. arXiv preprint arXiv:2504.19413 (2025).

[23] Sadia Sultana Chowa, Riasad Alvi, Subhey Sadi Rahman, Md Abdur Rahman, Mohaimenul Azam Khan Raiaan, Md Rafiqul Islam, Mukhtar
Hussain, and Sami Azam. 2026. From language to action: a review of large language models as autonomous agents and tool users. Artificial
Intelligence Review (2026).

[24] Zhendong Chu, Shen Wang, Jian Xie, Tinghui Zhu, Yibo Yan, Jinheng Ye, Aoxiao Zhong, Xuming Hu, Jing Liang, Philip S Yu, et al. 2025. Llm

agents for education: Advances and applications. arXiv preprint arXiv:2503.11733 (2025).

[25] Jiseong Chung, Ronny Ko, Wonchul Yoo, Makoto Onizuka, Sungmok Kim, Tae-Wan Kim, and Won-Yong Shin. 2025. GraphCompliance:

Aligning Policy and Context Graphs for LLM-Based Regulatory Compliance. arXiv preprint arXiv:2510.26309 (2025).

[26] Christopher Clarke, Yuzhao Heng, Lingjia Tang, and Jason Mars. 2024. Peft-u: Parameter-efficient fine-tuning for user personalization. arXiv

preprint arXiv:2407.18078 (2024).

[27] Clayton Cohn, Surya Rayala, Caitlin Snyder, Joyce Fonteles, Shruti Jain, Naveeduddin Mohammed, Umesh Timalsina, Sarah K Burriss,
Namrata Srivastava, Menton Deweese, et al. 2025. Personalizing Student-Agent Interactions Using Log-Contextualized Retrieval Augmented
Generation (RAG). arXiv preprint arXiv:2505.17238 (2025).

[28] DeepSeek. 2024. DeepSeek|deepseek.com. https://www.deepseek.com/.
[29] Priyanka Dey, Daniele Rosa, Wenqing Zheng, Daniel Barcklow, Jieyu Zhao, and Emilio Ferrara. 2025. GRAVITY: A Framework for Personalized

Text Generation via Profile-Grounded Synthetic Preferences. arXiv preprint arXiv:2510.11952 (2025).

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 27 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

27

[30] Yiming Du, Hongru Wang, Zhengyi Zhao, Bin Liang, Baojun Wang, Wanjun Zhong, Zezhong Wang, and Kam-Fai Wong. 2024. Perltqa: A
personal long-term memory dataset for memory classification, retrieval, and synthesis in question answering. arXiv preprint arXiv:2402.16288
(2024).

[31] Duolingo. 2025. Learn a language for free — duolingo.com. https://www.duolingo.com/.
[32] Mehmet Samet Duran and Tevfik Aytekin. 2025. Beyond one-size-fits-all summarization: Customizing summaries for diverse users. arXiv

preprint arXiv:2503.10675 (2025).

[33] Jacob Emmerson, Rayid Ghani, and Zheyuan Ryan Shi. 2025. Towards Automated Scoping of AI for Social Good Projects. arXiv preprint

arXiv:2504.20010 (2025).

[34] Jizhan Fang, Xinle Deng, Haoming Xu, Ziyan Jiang, Yuqi Tang, Ziwen Xu, Shumin Deng, Yunzhi Yao, Mengru Wang, Shuofei Qiao, et al.

2025. LightMem: Lightweight and Efficient Memory-Augmented Generation. arXiv preprint arXiv:2510.18866 (2025).

[35] Mohamed Amine Ferrag, Norbert Tihanyi, and Merouane Debbah. 2025. From llm reasoning to autonomous ai agents: A comprehensive

review. arXiv preprint arXiv:2504.19678 (2025).

[36] Xiao Fu, Hossein A Rahmani, Bin Wu, Jerome Ramos, Emine Yilmaz, and Aldo Lipani. 2025. PREF: Reference-Free Evaluation of Personalised

Text Generation in LLMs. arXiv preprint arXiv:2508.10028 (2025).

[37] Ge Gao, Alexey Taymanov, Eduardo Salinas, Paul Mineiro, and Dipendra Misra. 2024. Aligning llm agents by learning latent preference from

user edits. Advances in Neural Information Processing Systems 37 (2024), 136873–136896.

[38] Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, Xinzhe Juan, Hongzhang Liu, Shilong Liu, Jiahao Qiu, Xuan Qi, Yiran Wu, et al.

2025. A survey of self-evolving agents: On path to artificial super intelligence. arXiv preprint arXiv:2507.21046 (2025).

[39] Shen Gao, Yuntao Wen, Minghang Zhu, Jianing Wei, Yuhan Cheng, Qunzi Zhang, and Shuo Shang. 2024. Simulating financial market via

large language model based agents. arXiv preprint arXiv:2406.19966 (2024).

[40] Simret Araya Gebreegziabher, Yukun Yang, Charles Chiang, Hojun Yoo, Chaoran Chen, Hyo Jin Do, Zahra Ashktorab, Werner Geyer, Diego
Gómez-Zará, and Toby Jia-Jun Li. 2026. The Behavioral Fabric of LLM-Powered GUI Agents: Human Values and Interaction Outcomes.
arXiv preprint arXiv:2601.16356 (2026).

[41] Github. 2025. GitHub Copilot features - GitHub Docs — docs.github.com. https://docs.github.com/en/copilot/get-started/features.
[42] Inc. Glean Technologies. 2023. Glean — glean.com. https://www.glean.com/.
[43] Google. 2023. Google Gemini — gemini.google.com. https://gemini.google.com/.
[44] Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Nan Duan, and Weizhu Chen. 2023. Critic: Large language models can

self-correct with tool-interactive critiquing. arXiv preprint arXiv:2305.11738 (2023).

[45] Jian Guan, Junfei Wu, Jia-Nan Li, Chuanqi Cheng, and Wei Wu. 2025. A Survey on Personalized Alignment—The Missing Piece for Large
Language Models in Real-World Applications. In Findings of the Association for Computational Linguistics: ACL 2025. 5313–5333.

[46] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. 2025.

Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948 (2025).

[47] Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou, and Yu Su. 2025. From rag to memory: Non-parametric continual learning for

large language models. arXiv preprint arXiv:2502.14802 (2025).

[48] Dongge Han, Trevor McInroe, Adam Jelley, Stefano V Albrecht, Peter Bell, and Amos Storkey. 2025. Llm-personalize: Aligning llm planners
with human preferences via reinforced self-training for housekeeping robots. In Proceedings of the 31st International Conference on
Computational Linguistics. 1465–1474.

[49] Zhuo Han, Yi Yang, Yi Feng, Wanhong Huang, Xuxing Ding, Chuanyi Li, Jidong Ge, and Vincent Ng. 2025. LawShift: Benchmarking Legal
Judgment Prediction Under Statute Shifts. In The Thirty-ninth Annual Conference on Neural Information Processing Systems Datasets and
Benchmarks Track.

[50] Yupu Hao, Pengfei Cao, Zhuoran Jin, Huanxuan Liao, Yubo Chen, Kang Liu, and Jun Zhao. 2025. Evaluating personalized tool-augmented llms
from the perspectives of personalization and proactivity. In Proceedings of the 63rd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers). 21897–21935.

[51] Hsin-Ling Hsu, Cong-Tinh Dao, Luning Wang, Zitao Shuai, Thao Nguyen Minh Phan, Jun-En Ding, Chun-Chieh Liao, Pengfei Hu, Xiaoxue
Han, Chih-Ho Hsu, et al. 2025. Medplan: a two-stage rag-based system for personalized medical plan generation. In Proceedings of the 63rd
Annual Meeting of the Association for Computational Linguistics (Volume 6: Industry Track). 1072–1082.

[52] Yuanzhe Hu, Yu Wang, and Julian McAuley. 2025. Evaluating memory in llm agents via incremental multi-turn interactions. arXiv preprint

arXiv:2507.05257 (2025).

[53] Chengkai Huang, Junda Wu, Yu Xia, Zixu Yu, Ruhan Wang, Tong Yu, Ruiyi Zhang, Ryan A Rossi, Branislav Kveton, Dongruo Zhou, et al.
2025. Towards agentic recommender systems in the era of multimodal large language models. arXiv preprint arXiv:2503.16734 (2025).
[54] Jiani Huang, Xingchen Zou, Lianghao Xia, and Qing Li. 2025. Mr. rec: Synergizing memory and reasoning for personalized recommendation

assistant with llms. arXiv preprint arXiv:2510.14629 (2025).

[55] Xu Huang, Yuefeng Huang, Weiwen Liu, Xingshan Zeng, Yasheng Wang, Ruiming Tang, Hong Xie, and Defu Lian. 2025. Advancing and

Benchmarking Personalized Tool Invocation for LLMs. arXiv preprint arXiv:2505.04072 (2025).

[56] Zhaopei Huang, Qifeng Dai, Guozheng Wu, Xiaopeng Wu, Kehan Chen, Chuan Yu, Xubin Li, Tiezheng Ge, Wenxuan Wang, and Qin
Jin. 2025. Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction. arXiv preprint
arXiv:2511.13410 (2025).

[57] Zhengjun Huang, Zhoujin Tian, Qintian Guo, Fangyuan Zhang, Yingli Zhou, Di Jiang, and Xiaofang Zhou. 2025. LiCoMemory: Lightweight

and Cognitive Agentic Memory for Efficient Long-Term Reasoning. arXiv preprint arXiv:2511.01448 (2025).

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 28 -->

28

• Y. Xu et al.

[58] Bahar Irfan, Sanna Kuoppamäki, and Gabriel Skantze. 2024. Recommendations for designing conversational companion robots with older

adults through foundation models. Frontiers in Robotics and AI 11 (2024), 1363713.

[59] Gautier Izacard, Mathilde Caron, Lucas Hosseini, Sebastian Riedel, Piotr Bojanowski, Armand Joulin, and Edouard Grave. 2021. Unsupervised

dense information retrieval with contrastive learning. arXiv preprint arXiv:2112.09118 (2021).

[60] Jasper. 2023. Jasper Brand Voice — jasper.ai/brand-voice. https://www.jasper.ai/brand-voice.
[61] Bowen Jiang, Zhuoqun Hao, Young-Min Cho, Bryan Li, Yuan Yuan, Sihao Chen, Lyle Ungar, Camillo J Taylor, and Dan Roth. 2025. Know me,
respond to me: Benchmarking llms for dynamic user profiling and personalized responses at scale. arXiv preprint arXiv:2504.14225 (2025).
[62] Bowen Jiang, Yuan Yuan, Maohao Shen, Zhuoqun Hao, Zhangchen Xu, Zichen Chen, Ziyi Liu, Anvesh Rao Vijjini, Jiashu He, Hanchao Yu,
et al. 2025. PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory. arXiv preprint
arXiv:2512.06688 (2025).

[63] Liwei Jiang, Taylor Sorensen, Sydney Levine, and Yejin Choi. 2024. Can language models reason about individualistic human values and

preferences? arXiv preprint arXiv:2410.03868 (2024).

[64] Xun Jiang, Feng Li, Han Zhao, Jiahao Qiu, Jiaying Wang, Jun Shao, Shihao Xu, Shu Zhang, Weiling Chen, Xavier Tang, et al. 2024. Long term

memory: The foundation of ai self-evolution. arXiv preprint arXiv:2410.15665 (2024).

[65] Bernal Jimenez Gutierrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, and Yu Su. 2024. Hipporag: Neurobiologically inspired long-term memory

for large language models. Advances in Neural Information Processing Systems 37 (2024), 59532–59569.

[66] Hyoungwook Jin, Minju Yoo, Jeongeon Park, Yokyung Lee, Xu Wang, and Juho Kim. 2025. Teachtune: Reviewing pedagogical agents against
diverse student profiles with simulated students. In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems.
1–28.

[67] Mingyu Jin, Qinkai Yu, Dong Shu, Chong Zhang, Lizhou Fan, Wenyue Hua, Suiyuan Zhu, Yanda Meng, Zhenting Wang, Mengnan Du, et al.

2024. Health-llm: Personalized retrieval-augmented disease prediction system. arXiv preprint arXiv:2402.00746 (2024).

[68] Jeff Johnson, Matthijs Douze, and Hervé Jégou. 2019. Billion-scale similarity search with GPUs. IEEE Transactions on Big Data 7, 3 (2019),

535–547.

[69] Brennan Jones, Kelsey Stemmler, Emily Su, Young-Ho Kim, and Anastasia Kuzminykh. 2025. Users’ Expectations and Practices with Agent

Memory. In Proceedings of the Extended Abstracts of the CHI Conference on Human Factors in Computing Systems. 1–8.

[70] Aymen Kabir, Suraj Shah, Alexander Haddad, and Daniel MS Raper. 2025. Introducing our custom GPT: An example of the potential impact

of personalized GPT builders on scientific writing. World Neurosurgery 193 (2025), 461–468.

[71] Priyanshu Karmakar, Soumyabrata Chaudhuri, Shubhojit Mallick, Manish Gupta, Abhik Jana, and Shreya Ghosh. 2025. TripTide: A Benchmark

for Adaptive Travel Planning under Disruptions. arXiv preprint arXiv:2510.21329 (2025).

[72] Sean Kelley, David De Cremer, and Christoph Riedl. 2025. Personalized AI Scaffolds Synergistic Multi-Turn Collaboration in Creative Work.

arXiv preprint arXiv:2510.27681 (2025).

[73] Callie Y Kim, Christine P Lee, and Bilge Mutlu. 2024. Understanding large-language model (llm)-powered human-robot interaction. In

Proceedings of the 2024 ACM/IEEE international conference on human-robot interaction. 371–380.

[74] Hannah Kim, Kushan Mitra, Chen Shen, Dan Zhang, and Estevam Hruschka. 2025. AIPOM: Agent-aware Interactive Planning for Multi-Agent

Systems. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations. 85–96.

[75] Jaehyung Kim and Yiming Yang. 2024. Few-shot personalization of llms with mis-aligned responses. arXiv preprint arXiv:2406.18678 (2024).
[76] Minbeom Kim, Kang-il Lee, Seongho Joo, Hwaran Lee, Thibaut Thonet, and Kyomin Jung. 2025. Drift: Decoding-time personalized alignments

with implicit user preferences. arXiv preprint arXiv:2502.14289 (2025).

[77] Sangyeop Kim, Yohan Lee, Sanghwa Kim, Hyunjong Kim, and Sungzoon Cho. 2025. Pre-Storage Reasoning for Episodic Memory: Shifting

Inference Burden to Memory for Personalized Dialogue. arXiv preprint arXiv:2509.10852 (2025).

[78] Hannah Rose Kirk, Alexander Whitefield, Paul Rottger, Andrew M Bean, Katerina Margatina, Rafael Mosquera-Gomez, Juan Ciro, Max
Bartolo, Adina Williams, He He, et al. 2024. The prism alignment dataset: What participatory, representative and individualised human
feedback reveals about the subjective and multicultural alignment of large language models. Advances in Neural Information Processing
Systems 37 (2024), 105236–105344.

[79] Ishita Kumar, Snigdha Viswanathan, Sushrita Yerra, Alireza Salemi, Ryan A Rossi, Franck Dernoncourt, Hanieh Deilamsalehy, Xiang
Chen, Ruiyi Zhang, Shubham Agarwal, et al. 2024. Longlamp: A benchmark for personalized long-form text generation. arXiv preprint
arXiv:2407.11016 (2024).

[80] Mehmet Kurmaz. 2026. AWARE-US: Benchmark for Preference-Aware Resolution in Tool-Calling Agents. arXiv preprint arXiv:2601.02643

(2026).

[81] Taeyoon Kwon, Dongwook Choi, Sunghwan Kim, Hyojun Kim, Seungjun Moon, Beong-woo Kwak, Kuan-Hao Huang, and Jinyoung Yeo.
2025. Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance. arXiv preprint arXiv:2505.16348
(2025).

[82] Seongyun Lee, Sue Hyun Park, Seungone Kim, and Minjoon Seo. 2024. Aligning to thousands of preferences via system message generalization.

Advances in Neural Information Processing Systems 37 (2024), 73783–73829.

[83] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau
Yih, Tim Rocktäschel, et al. 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in neural information
processing systems 33 (2020), 9459–9474.

[84] Ed Li, Junyu Ren, Xintian Pan, Cat Yan, Chuanhao Li, Dirk Bergemann, and Zhuoran Yang. 2025. Build Your Personalized Research Group: A

Multiagent Framework for Continual and Interactive Science Automation. arXiv preprint arXiv:2510.15624 (2025).

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 29 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

29

[85] Hao Li, Ruoyuan Gong, and Hao Jiang. 2025. Political actor agent: Simulating legislative system for roll call votes prediction with large

language models. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 39. 388–396.

[86] Hao Li, Chenghao Yang, An Zhang, Yang Deng, Xiang Wang, and Tat-Seng Chua. 2025. Hello again! llm-powered personalized agent for
long-term dialogue. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational
Linguistics: Human Language Technologies (Volume 1: Long Papers). 5259–5276.

[87] Jia-Nan Li, Jian Guan, Songhao Wu, Wei Wu, and Rui Yan. 2025. From 1,000,000 users to every user: Scaling up personalized preference for

user-level alignment. arXiv preprint arXiv:2503.15463 (2025).

[88] Jia-Nan Li, Jian Guan, Wei Wu, and Rui Yan. 2025. Extended inductive reasoning for personalized preference inference from behavioral

signals. arXiv preprint arXiv:2505.18071 (2025).

[89] Li Li, Peilin Cai, Ryan A Rossi, Franck Dernoncourt, Branislav Kveton, Junda Wu, Tong Yu, Linxin Song, Tiankai Yang, Yuehan Qin, et al.
2025. A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations. arXiv preprint arXiv:2505.14106 (2025).
[90] Ning Li, Qiqiang Lin, Zheng Wu, Xiaoyun Mo, Weiming Zhang, Yin Zhao, Xiangmou Qu, Jiamu Zhou, Jun Wang, Congmin Zheng, et al.

2025. ColorAgent: Building A Robust, Personalized, and Interactive OS Agent. arXiv preprint arXiv:2510.19386 (2025).

[91] Qiaomu Li, Ying Xie, Sumit Chakravarty, and Dabae Lee. 2024. EduMAS: A novel LLM-powered multi-agent framework for educational

support. In 2024 IEEE International Conference on Big Data (BigData). IEEE, 8309–8316.

[92] Shuyue Stella Li, Avinandan Bose, Faeze Brahman, Simon Shaolei Du, Pang Wei Koh, Maryam Fazel, and Yulia Tsvetkov. 2025. PrefDisco:
Evaluating Proactive Personalization through Interactive Preference Discovery. In First Workshop on Multi-Turn Interactions in Large
Language Models.

[93] Weitao Li, Junkai Li, Weizhi Ma, and Yang Liu. 2024. Citation-enhanced generation for LLM-based chatbots. In Proceedings of the 62nd

Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 1451–1466.

[94] Xinzhe Li. 2025. A review of prominent paradigms for llm-based agents: Tool use, planning (including rag), and feedback learning. In

Proceedings of the 31st international conference on computational linguistics. 9760–9779.

[95] Xiaopeng Li, Pengyue Jia, Derong Xu, Yi Wen, Yingyi Zhang, Wenlin Zhang, Wanyu Wang, Yichao Wang, Zhaocheng Du, Xiangyang Li,

et al. 2025. A survey of personalization: From rag to agent. arXiv preprint arXiv:2504.10147 (2025).

[96] Yi Li, Jieming Zhu, Weiwen Liu, Liangcai Su, Guohao Cai, Qi Zhang, Ruiming Tang, Xi Xiao, and Xiuqiang He. 2022. Pear: Personalized

re-ranking with contextualized transformer for recommendation. In Companion Proceedings of the Web Conference 2022. 62–66.

[97] Zhiyu Li, Shichao Song, Chenyang Xi, Hanyu Wang, Chen Tang, Simin Niu, Ding Chen, Jiawei Yang, Chunyu Li, Qingchen Yu, et al. 2025.

Memos: A memory os for ai system. arXiv preprint arXiv:2507.03724 (2025).

[98] Guannan Liang and Qianqian Tong. 2025. LLM-powered AI agent systems and their applications in industry. In 2025 IEEE World AI IoT

Congress (AIIoT). IEEE, 0463–0471.

[99] Yuan Liang, Jiaxian Li, Yuqing Wang, Piaohong Wang, Motong Tian, Pai Liu, Shuofei Qiao, Runnan Fang, He Zhu, Ge Zhang, et al. 2025.

Towards Personalized Deep Research: Benchmarks and Evaluations. arXiv preprint arXiv:2509.25106 (2025).

[100] Chin-Yew Lin. 2004. Rouge: A package for automatic evaluation of summaries. In Text summarization branches out. 74–81.
[101] Binwen Liu, Jiexi Ge, and Jiamin Wang. 2025. Vaiage: A Multi-Agent Solution to Personalized Travel Planning. arXiv preprint arXiv:2505.10922

(2025).

[102] Jie Liu, Wenxuan Wang, Zizhan Ma, Guolin Huang, Yihang SU, Kao-Jung Chang, Wenting Chen, Haoliang Li, Linlin Shen, and Michael Lyu.
2024. Medchain: Bridging the gap between llm agents and clinical practice through interactive sequential benchmarking. arXiv preprint
arXiv:2412.01605 (2024).

[103] Lei Liu, Xiaoyan Yang, Yue Shen, Binbin Hu, Zhiqiang Zhang, Jinjie Gu, and Guannan Zhang. 2023. Think-in-memory: Recalling and

post-thinking enable llms with long-term memory. arXiv preprint arXiv:2311.08719 (2023).

[104] Na Liu, Liangyu Chen, Xiaoyu Tian, Wei Zou, Kaijiang Chen, and Ming Cui. 2024. From llm to conversational agent: A memory enhanced

architecture with fine-tuning of large language models. arXiv preprint arXiv:2401.02777 (2024).

[105] Siyuan Liu, Wenjing Liu, Zhiwei Xu, Xin Wang, Bo Chen, and Tao Li. 2025. Towards Mitigation of Hallucination for LLM-empowered

Agents: Progressive Generalization Bound Exploration and Watchdog Monitor. arXiv preprint arXiv:2507.15903 (2025).

[106] Tianjian Liu, Hongzheng Zhao, Yuheng Liu, Xingbo Wang, and Zhenhui Peng. 2024. Compeer: A generative conversational agent for

proactive peer support. In Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology. 1–22.

[107] WenTao Liu, Ruohua Zhang, Aimin Zhou, Feng Gao, and JiaLi Liu. 2025. Echo: A large language model with temporal episodic memory.

arXiv preprint arXiv:2502.16090 (2025).

[108] Yuhan Liu, Michael JQ Zhang, and Eunsol Choi. 2025. User Feedback in Human-LLM Dialogues: A Lens to Understand Users But Noisy as a

Learning Signal. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing. 2666–2681.

[109] Lin Long, Yichen He, Wentao Ye, Yiyuan Pan, Yuan Lin, Hang Li, Junbo Zhao, and Wei Li. 2025. Seeing, listening, remembering, and

reasoning: A multimodal agent with long-term memory. arXiv preprint arXiv:2508.09736 (2025).

[110] Junyu Luo, Weizhi Zhang, Ye Yuan, Yusheng Zhao, Junwei Yang, Yiyang Gu, Bohan Wu, Binqi Chen, Ziyue Qiao, Qingqing Long, et al. 2025.

Large language model agent: A survey on methodology, applications and challenges. arXiv preprint arXiv:2503.21460 (2025).

[111] Yitong Luo, Hou Hei Lam, Ziang Chen, Zhenliang Zhang, and Xue Feng. 2025. ValuePilot: A Two-Phase Framework for Value-Driven

Decision-Making. arXiv preprint arXiv:2503.04569 (2025).

[112] Chenhan Lyu, Yutong Song, Pengfei Zhang, and Amir M Rahmani. 2025. Domain-Specific Constitutional AI: Enhancing Safety in LLM-

Powered Mental Health Chatbots. arXiv preprint arXiv:2509.16444 (2025).

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 30 -->

30

• Y. Xu et al.

[113] Yibo Lyu, Gongwei Chen, Rui Shao, Weili Guan, and Liqiang Nie. 2026. PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized

GUI Agent with Long-Term User-Centric Records. arXiv preprint arXiv:2601.09636 (2026).

[114] Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, and Yuwei Fang. 2024. Evaluating very long-term
conversational memory of llm agents. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers). 13851–13870.

[115] Wenyu Mao, Jiancan Wu, Weijian Chen, Chongming Gao, Xiang Wang, and Xiangnan He. 2025. Reinforced prompt personalization for

recommendation with large language models. ACM Transactions on Information Systems 43, 3 (2025), 1–27.

[116] Reza Yousefi Maragheh, Pratheek Vadla, Priyank Gupta, Kai Zhao, Aysenur Inan, Kehui Yao, Jianpeng Xu, Praveen Kanumala, Jason Cho, and
Sushant Kumar. 2025. ARAG: Agentic Retrieval Augmented Generation for Personalized Recommendation. arXiv preprint arXiv:2506.21931
(2025).

[117] Maria Emilia Mazzolenis and Ruirui Zhang. 2025. Agent warpp: Workflow adherence via runtime parallel personalization. arXiv preprint

arXiv:2507.19543 (2025).

[118] Inc. Mem. 2023. Mem — mem.ai. https://mem.ai/.
[119] memodb. 2025. GitHub - memodb-io/memobase: Profile-Based Long-Term Memory for AI Applications. Memobase handles user profiles,
memory events, and evolving context — perfect for chatbots, companions, tutors, customer service bots, and all chat-based agents. —
github.com. https://github.com/memodb-io/memobase.

[120] Fengran Mo, Yuchen Hui, Yuxing Tian, Zhaoxuan Tan, Chuan Meng, Zhan Su, Kaiyu Huang, and Jian-Yun Nie. 2025. Towards adaptive
personalized conversational information retrieval. In Proceedings of the 34th ACM International Conference on Information and Knowledge
Management. 2137–2147.

[121] Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel
Candès, and Tatsunori B Hashimoto. 2025. s1: Simple test-time scaling. In Proceedings of the 2025 Conference on Empirical Methods in
Natural Language Processing. 20286–20332.

[122] Subhabrata Mukherjee, Paul Gamble, Markel Sanz Ausin, Neel Kant, Kriti Aggarwal, Neha Manjunath, Debajyoti Datta, Zhengliang
Liu, Jiayuan Ding, Sophia Busacca, et al. 2024. Polaris: A safety-focused llm constellation architecture for healthcare. arXiv preprint
arXiv:2403.13313 (2024).

[123] Srija Mukhopadhyay, Sathwik Reddy, Shruthi Muthukumar, Jisun An, and Ponnurangam Kumaraguru. 2025. PrivacyBench: A Conversational

Benchmark for Evaluating Privacy in Personalized AI. arXiv preprint arXiv:2512.24848 (2025).

[124] John Murzaku, Zifan Liu, Md Mehrab Tanjim, Vaishnavi Muppala, Xiang Chen, and Yunyao Li. 2025. ECLAIR: Enhanced Clarification for

Interactive Responses. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 39. 28864–28870.

[125] Hyunji Nam, Yanming Wan, Mickel Liu, Jianxun Lian, Peter Ahnn, and Natasha Jaques. 2025. Learning to summarize user information for

personalized reinforcement learning from human feedback. arXiv preprint arXiv:2507.13579 (2025).

[126] Jiayan Nan, Wenquan Ma, Wenlong Wu, and Yize Chen. 2025. Nemori: Self-organizing agent memory inspired by cognitive science. arXiv

preprint arXiv:2508.03341 (2025).

[127] Vladimir Naumov, Diana Zagirova, Sha Lin, Yupeng Xie, Wenhao Gou, Anatoly Urban, Nina Tikhonova, Khadija Alawi, Mike Durymanov,
Fedor Galkin, et al. 2025. Dora ai scientist: Multi-agent virtual research team for scientific exploration discovery and automated report
generation. bioRxiv (2025).

[128] Lewis Newsham and Daniel Prince. 2025. Personality-Driven Decision Making in LLM-Based Autonomous Agents. In Proceedings of the

24th International Conference on Autonomous Agents and Multiagent Systems. 1538–1547.

[129] Lin Ning, Luyang Liu, Jiaxing Wu, Neo Wu, Devora Berlowitz, Sushant Prakash, Bradley Green, Shawn O’Banion, and Jun Xie. 2025. User-llm:
Efficient llm contextualization with user embeddings. In Companion Proceedings of the ACM on Web Conference 2025. 1219–1223.
[130] Wenyu Ning, Shaotao Shi, Yuchen Yin, Zixuan Guo, and Jinrong Xie. 2025. Intent-aware personalized summarization for educational texts

with large language models. Journal of King Saud University Computer and Information Sciences 37, 9 (2025), 308.

[131] Inc. Notion Labs. 2023. Notion AI — notion.com/product/ai. https://www.notion.com/product/ai.
[132] Rodrigo Novelo, Rodrigo Rocha Silva, and Jorge Bernardino. 2025. A Literature Review of Personalized Large Language Models for Email

Generation and Automation. Future Internet 17, 12 (2025), 536.

[133] Felix Ocker, Jörg Deigmöller, Pavel Smirnov, and Julian Eggert. 2025. A grounded memory system for smart personal assistants. arXiv

preprint arXiv:2505.06328 (2025).

[134] OpenAI. 2022. ChatGPT — chatgpt.com. https://chatgpt.com/.
[135] Egor Pakhomov, Erik Nijkamp, and Caiming Xiong. 2025. Convomem Benchmark: Why Your First 150 Conversations Don’t Need RAG.

arXiv preprint arXiv:2511.10523 (2025).

[136] Zhuoshi Pan, Qianhui Wu, Huiqiang Jiang, Xufang Luo, Hao Cheng, Dongsheng Li, Yuqing Yang, Chin-Yew Lin, H Vicky Zhao, Lili Qiu,
et al. 2025. On memory construction and retrieval for personalized conversational agents. arXiv preprint arXiv:2502.05589 (2025).
[137] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002. Bleu: a method for automatic evaluation of machine translation. In

Proceedings of the 40th annual meeting of the Association for Computational Linguistics. 311–318.

[138] Changhua Pei, Yi Zhang, Yongfeng Zhang, Fei Sun, Xiao Lin, Hanxiao Sun, Jian Wu, Peng Jiang, Junfeng Ge, Wenwu Ou, et al. 2019.

Personalized re-ranking for recommendation. In Proceedings of the 13th ACM conference on recommender systems. 3–11.

[139] Qiyao Peng, Hongtao Liu, Hua Huang, Qing Yang, and Minglai Shao. 2025. A survey on llm-powered agents for recommender systems.

arXiv preprint arXiv:2502.10050 (2025).

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 31 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

31

[140] Mathis Pink, Qinyuan Wu, Vy Ai Vo, Javier Turek, Jianing Mu, Alexander Huth, and Mariya Toneva. 2025. Position: Episodic Memory is the

Missing Piece for Long-Term LLM Agents. arXiv preprint arXiv:2502.06975 (2025).

[141] Sriyash Poddar, Yanming Wan, Hamish Ivison, Abhishek Gupta, and Natasha Jaques. 2024. Personalizing reinforcement learning from
human feedback with variational preference learning. Advances in Neural Information Processing Systems 37 (2024), 52516–52544.

[142] Predis.ai. 2023. Predis.ai — predis.ai. https://predis.ai/.
[143] Cheng Qian, Emre Can Acikgoz, Hongru Wang, Xiusi Chen, Avirup Sil, Dilek Hakkani-Tur, Gokhan Tur, and Heng Ji. 2025. SMART:

Self-aware agent for tool overuse mitigation. In Findings of the Association for Computational Linguistics: ACL 2025. 4604–4621.
[144] Hongjin Qian, Zheng Liu, Peitian Zhang, Kelong Mao, Defu Lian, Zhicheng Dou, and Tiejun Huang. 2025. Memorag: Boosting long context
processing with global memory-enhanced retrieval augmentation. In Proceedings of the ACM on Web Conference 2025. 2366–2377.
[145] Tian Qin, Felix Bai, Ting-Yao Hu, Raviteja Vemulapalli, Hema Swetha Koppula, Zhiyang Xu, Bowen Jin, Mert Cemri, Jiarui Lu, Zirui Wang,
et al. 2025. COMPASS: A Multi-Turn Benchmark for Tool-Mediated Planning & Preference Optimization. arXiv preprint arXiv:2510.07043
(2025).

[146] Yilun Qiu, Tianhao Shi, Xiaoyan Zhao, Fengbin Zhu, Yang Zhang, and Fuli Feng. 2025. Latent inter-user difference modeling for llm

personalization. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing. 10610–10628.

[147] Yilun Qiu, Xiaoyan Zhao, Yang Zhang, Yimeng Bai, Wenjie Wang, Hong Cheng, Fuli Feng, and Tat-Seng Chua. 2025. Measuring what
makes you unique: Difference-aware user modeling for enhancing llm personalization. In Findings of the Association for Computational
Linguistics: ACL 2025. 21258–21277.

[148] Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, and Ji-Rong Wen. 2025. Tool learning with large

language models: A survey. Frontiers of Computer Science 19, 8 (2025), 198343.

[149] Steven Jige Quan and Seojung Lee. 2025. Enhancing participatory planning with ChatGPT-assisted planning support systems: a hypothetical

case study in Seoul. International Journal of Urban Sciences 29, 1 (2025), 89–122.

[150] Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais, Jack Ryan, and Daniel Chalef. 2025. Zep: a temporal knowledge graph architecture

for agent memory. arXiv preprint arXiv:2501.13956 (2025).

[151] Replika. [n. d.]. Replika — replika.com. https://replika.com/.
[152] Alireza Rezazadeh, Zichao Li, Wei Wei, and Yujia Bao. 2024. From isolated conversations to hierarchical schemas: Dynamic tree memory

representation for llms. arXiv preprint arXiv:2410.14052 (2024).

[153] Stephen Robertson, Hugo Zaragoza, et al. 2009. The probabilistic relevance framework: BM25 and beyond. Foundations and Trends® in

Information Retrieval 3, 4 (2009), 333–389.

[154] Rana Salama, Jason Cai, Michelle Yuan, Anna Currey, Monica Sunkara, Yi Zhang, and Yassine Benajiba. 2025. Meminsight: Autonomous

memory augmentation for llm agents. arXiv preprint arXiv:2503.21760 (2025).

[155] Alireza Salemi, Cheng Li, Mingyang Zhang, Qiaozhu Mei, Weize Kong, Tao Chen, Zhuowan Li, Michael Bendersky, and Hamed Zamani.

2025. Reasoning-Enhanced Self-Training for Long-Form Personalized Text Generation. arXiv preprint arXiv:2501.04167 (2025).

[156] Alireza Salemi, Sheshera Mysore, Michael Bendersky, and Hamed Zamani. 2024. Lamp: When large language models meet personalization.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 7370–7392.
[157] Alireza Salemi and Hamed Zamani. 2025. Lamp-qa: A benchmark for personalized long-form question answering. In Proceedings of the

2025 Conference on Empirical Methods in Natural Language Processing. 1139–1159.

[158] Salesforge. 2023. Salesforge AI — salesforge.ai. https://www.salesforge.ai/.
[159] Rohan Charudatt Salvi, Chirag Chawla, Dhruv Jain, Swapnil Panigrahi, Md Shad Akhtar, and Shweta Yadav. 2025. PERCS: Persona-Guided

Controllable Biomedical Summarization Dataset. arXiv preprint arXiv:2512.03340 (2025).

[160] Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh Khanna, Anna Goldie, and Christopher D Manning. 2024. Raptor: Recursive abstractive

processing for tree-organized retrieval. In The Twelfth International Conference on Learning Representations.

[161] Krishna Sayana, Raghavendra Vasudeva, Yuri Vasilevski, Kun Su, Liam Hebert, James Pine, Hubert Pham, Ambarish Jash, and Sukhdeep
Sodhi. 2025. Beyond Retrieval: Generating Narratives in Conversational Recommender Systems. In Companion Proceedings of the ACM on
Web Conference 2025. 2411–2420.

[162] Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, and Emad Barsoum.
2025. Agent laboratory: Using llm agents as research assistants. Findings of the Association for Computational Linguistics: EMNLP 2025
(2025), 5977–6043.

[163] Samuel Schmidgall, Rojin Ziaei, Carl Harris, Eduardo Reis, Jeffrey Jopling, and Michael Moor. 2024. AgentClinic: a multimodal agent

benchmark to evaluate AI in simulated clinical environments. arXiv preprint arXiv:2405.07960 (2024).

[164] Yu Shang, Peijie Liu, Yuwei Yan, Zijing Wu, Leheng Sheng, Yuanqing Yu, Chumeng Jiang, An Zhang, Fengli Xu, Yu Wang, et al. 2025.

Agentrecbench: Benchmarking llm agent-based personalized recommender systems. arXiv preprint arXiv:2505.19623 (2025).

[165] Zijian Shao, Jiancan Wu, Weijian Chen, and Xiang Wang. 2025. Personal Travel Solver: A Preference-Driven LLM-Solver System for
Travel Planning. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).
27622–27642.

[166] Sahil Sharma, Puneet Mittal, Mukesh Kumar, and Vivek Bhardwaj. 2025. The role of large language models in personalized learning: a

systematic review of educational impact. Discover Sustainability 6, 1 (2025), 1–24.
[167] Zhuocheng Shen. 2024. Llm with tools: A survey. arXiv preprint arXiv:2409.18807 (2024).
[168] Idan Shenfeld, Felix Faltings, Pulkit Agrawal, and Aldo Pacchiano. 2025. Language model personalization via reward factorization. arXiv

preprint arXiv:2503.06358 (2025).

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 32 -->

32

• Y. Xu et al.

[169] Teng Shi, Jun Xu, Xiao Zhang, Xiaoxue Zang, Kai Zheng, Yang Song, and Han Li. 2025. Retrieval augmented generation with collaborative
filtering for personalized text generation. In Proceedings of the 48th International ACM SIGIR Conference on Research and Development
in Information Retrieval. 1294–1304.

[170] Wenqi Shi, Ran Xu, Yuchen Zhuang, Yue Yu, Jieyu Zhang, Hang Wu, Yuanda Zhu, Joyce C Ho, Carl Yang, and May Dongmei Wang. 2024.
Ehragent: Code empowers large language models for few-shot complex tabular reasoning on electronic health records. In Proceedings of
the 2024 Conference on Empirical Methods in Natural Language Processing. 22315–22339.

[171] Yunxiao Shi, Haoning Shang, Xing Zi, Wujiang Xu, Yue Feng, and Min Xu. 2025. Answering Narrative-Driven Recommendation Queries
via a Retrieve–Rank Paradigm and the OCG-Agent. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language
Processing. 13192–13213.

[172] Yunxiao Shi, Wujiang Xu, Zhang Zeqi, Xing Zi, Qiang Wu, and Min Xu. 2025. PersonaX: A recommendation agent-oriented user modeling

framework for long behavior sequence. In Findings of the Association for Computational Linguistics: ACL 2025. 5764–5787.

[173] Donghoon Shin, Gary Hsieh, and Young-Ho Kim. 2025. PlanFitting: Personalized Exercise Planning with Large Language Model-driven

Conversational Agent. In Proceedings of the 7th ACM Conference on Conversational User Interfaces. 1–19.

[174] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. 2023. Reflexion: Language agents with verbal

reinforcement learning. Advances in Neural Information Processing Systems 36 (2023), 8634–8652.

[175] Anikait Singh, Sheryl Hsu, Kyle Hsu, Eric Mitchell, Stefano Ermon, Tatsunori Hashimoto, Archit Sharma, and Chelsea Finn. 2025. Fspo: Few-
shot preference optimization of synthetic preference data in llms elicits effective personalization to real users. arXiv preprint arXiv:2502.19312
(2025).

[176] Harmanpreet Singh, Nikhil Verma, Yixiao Wang, Manasa Bharadwaj, Homa Fashandi, Kevin Ferreira, and Chul Lee. 2024. Personal large
language model agents: A case study on tailored travel planning. In Proceedings of the 2024 Conference on Empirical Methods in Natural
Language Processing: Industry Track. 486–514.

[177] Yutong Song, Jiang Wu, Weijia Zhang, Chengze Shen, Shaofan Yuan, Weitao Lu, Jian Wang, Amir Rahmani, Nikil Dutt, and Yu Wang. 2026.
CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized Text Generation. arXiv preprint arXiv:2601.06352 (2026).
[178] Paolo Sorino, Giovanni Maria Biancofiore, Domenico Lofù, Tommaso Colafiglio, Angela Lombardi, Fedelucio Narducci, and Tommaso
Di Noia. 2024. Ariel: Brain-computer interfaces meet large language models for emotional support conversation. In Adjunct Proceedings of
the 32nd ACM Conference on User Modeling, Adaptation and Personalization. 601–609.

[179] Junhao Su, Yuanliang Wan, Junwei Yang, Hengyu Shi, Tianyang Han, Junfeng Luo, and Yurui Qiu. 2025. Failure makes the agent stronger:

Enhancing accuracy through structured reflection for reliable tool interactions. arXiv preprint arXiv:2509.18847 (2025).

[180] Chenkai Sun, Ke Yang, Revanth Gangi Reddy, Yi Fung, Hou Pong Chan, Kevin Small, ChengXiang Zhai, and Heng Ji. 2025. Persona-db:
Efficient large language model personalization for response prediction with collaborative data refinement. In Proceedings of the 31st
International Conference on Computational Linguistics. 281–296.

[181] Haotian Sun, Yuchen Zhuang, Lingkai Kong, Bo Dai, and Chao Zhang. 2023. Adaplanner: Adaptive planning from feedback with language

models. Advances in neural information processing systems 36 (2023), 58202–58245.

[182] Weiwei Sun, Xuhui Zhou, Weihua Du, Xingyao Wang, Sean Welleck, Graham Neubig, Maarten Sap, and Yiming Yang. 2025. Training

proactive and personalized llm agents. arXiv preprint arXiv:2511.02208 (2025).

[183] Manan Suri, Puneet Mathur, Nedim Lipka, Franck Dernoncourt, Ryan A Rossi, and Dinesh Manocha. 2025. Structured Uncertainty guided

Clarification for LLM Agents. arXiv preprint arXiv:2511.08798 (2025).

[184] Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard McCreadie, and Iadh Ounis. 2025. Are generative AI agents effec-
tive personalized financial advisors?. In Proceedings of the 48th International ACM SIGIR Conference on Research and Development in
Information Retrieval. 286–295.

[185] Takehiro Takayanagi, Masahiro Suzuki, Kiyoshi Izumi, Javier Sanz-Cruzado, Richard McCreadie, and Iadh Ounis. 2025. FinPersona: An
LLM-Driven Conversational Agent for Personalized Financial Advising. In European Conference on Information Retrieval. Springer, 13–18.
[186] Juntao Tan, Liangwei Yang, Zuxin Liu, Zhiwei Liu, Rithesh RN, Tulika Manoj Awalgaonkar, Jianguo Zhang, Weiran Yao, Ming Zhu, Shirley
Kokane, et al. 2025. Personabench: Evaluating ai models on understanding personal information through accessing (synthetic) private user
data. In Findings of the Association for Computational Linguistics: ACL 2025. 878–893.

[187] Zhen Tan, Jun Yan, I Hsu, Rujun Han, Zifeng Wang, Long T Le, Yiwen Song, Yanfei Chen, Hamid Palangi, George Lee, et al. 2025. In prospect
and retrospect: Reflective memory management for long-term personalized dialogue agents. arXiv preprint arXiv:2503.08026 (2025).
[188] Zhaoxuan Tan, Zixuan Zhang, Haoyang Wen, Zheng Li, Rongzhi Zhang, Pei Chen, Fengran Mo, Zheyuan Liu, Qingkai Zeng, Qingyu Yin,

et al. 2025. Instant Personalized Large Language Model Adaptation via Hypernetwork. arXiv preprint arXiv:2510.16282 (2025).

[189] Jiakai Tang, Sunhao Dai, Teng Shi, Jun Xu, Xu Chen, Wen Chen, Jian Wu, and Yuning Jiang. 2025. Think before recommend: Unleashing the

latent reasoning power for sequential recommendation. arXiv preprint arXiv:2503.22675 (2025).

[190] Meiling Tao, Chenghao Zhu, Dongyi Ding, Tiannan Wang, Yuchen Eleanor Jiang, and Wangchunshu Zhou. 2025. PersonaFeedback: A

Large-scale Human-annotated Benchmark For Personalization. arXiv preprint arXiv:2506.12915 (2025).

[191] Ao Tian, Yunfeng Lu, Xinxin Fan, Changhao Wang, Lanzhi Zhou, Yeyao Zhang, and Yanfang Liu. 2025. Rgmem: Renormalization group-based

memory evolution for language agent user profile. arXiv preprint arXiv:2510.16392 (2025).

[192] Khanh-Tung Tran, Dung Dao, Minh-Duong Nguyen, Quoc-Viet Pham, Barry O’Sullivan, and Hoang D Nguyen. 2025. Multi-agent collaboration

mechanisms: A survey of llms. arXiv preprint arXiv:2501.06322 (2025).

[193] Ioannis Tsaknakis, Bingqing Song, Shuyu Gan, Dongyeop Kang, Alfredo Garcia, Gaowen Liu, Charles Fleming, and Mingyi Hong. 2025.
Do LLMs Recognize Your Latent Preferences? A Benchmark for Latent Information Discovery in Personalized Interaction. arXiv preprint

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 33 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

33

arXiv:2510.17132 (2025).

[194] Yu-Min Tseng, Yu-Chao Huang, Teng-Yun Hsiao, Wei-Lin Chen, Chao-Wei Huang, Yu Meng, and Yun-Nung Chen. 2024. Two tales of

persona in llms: A survey of role-playing and personalization. arXiv preprint arXiv:2406.01171 (2024).

[195] Kentaro Ueda and Takehiro Takayanagi. 2025. PREFINE: Personalized Story Generation via Simulated User Critics and User-Specific Rubric

Generation. arXiv preprint arXiv:2510.21721 (2025).

[196] Harsh Vishwakarma, Ankush Agarwal, Ojas Patil, Chaitanya Devaguptapu, and Mahesh Chandran. 2025. Can LLMs Help You at Work? A
Sandbox for Evaluating LLM Agents in Enterprise Environments. In Proceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing. 9178–9212.

[197] Yanming Wan, Jiaxing Wu, Marwa Abdulhai, Lior Shani, and Natasha Jaques. 2025. Enhancing Personalized Multi-Turn Dialogue with

Curiosity Reward. arXiv preprint arXiv:2504.03206 (2025).

[198] Danqing Wang, Kevin Yang, Hanlin Zhu, Xiaomeng Yang, Andrew Cohen, Lei Li, and Yuandong Tian. 2024. Learning personalized alignment
for evaluating open-ended text generation. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing.
13274–13292.

[199] Hongru Wang, Minda Hu, Yang Deng, Rui Wang, Fei Mi, Weichao Wang, Yasheng Wang, Wai-Chung Kwan, Irwin King, and Kam-Fai
Wong. 2023. Large language models as source planner for personalized knowledge-grounded dialogues. In Findings of the Association for
Computational Linguistics: EMNLP 2023. 9556–9569.

[200] Hongru Wang, Wenyu Huang, Yang Deng, Rui Wang, Zezhong Wang, Yufei Wang, Fei Mi, Jeff Z Pan, and Kam-Fai Wong. 2024. Unims-rag:
A unified multi-source retrieval-augmented generation for personalized dialogue systems. arXiv preprint arXiv:2401.13256 (2024).
[201] Hanpeng Wang and Zijiang Yang. 2025. A Multi-Agent Approach to Investor Profiling Using Large Language Models. In 2025 International

Conference on Control, Automation and Diagnosis (ICCAD). IEEE, 1–6.

[202] Kuan Wang, Yadong Lu, Michael Santacroce, Yeyun Gong, Chao Zhang, and Yelong Shen. 2023. Adapting llm agents with universal feedback

in communication. arXiv preprint arXiv:2310.01444 (2023).

[203] Kaimin Wang, Yuanzhe Shen, Changze Lv, Xiaoqing Zheng, and Xuanjing Huang. 2025. TripTailor: A Real-World Benchmark for Personalized
Travel Planning. In Findings of the Association for Computational Linguistics: ACL 2025. Association for Computational Linguistics, Vienna,
Austria, 9705–9723. doi:10.18653/v1/2025.findings-acl.503

[204] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al. 2024. A

survey on large language model based autonomous agents. Frontiers of Computer Science 18, 6 (2024), 186345.

[205] Lei Wang, Jingsen Zhang, Hao Yang, Zhi-Yuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Hao Sun, Ruihua Song, et al. 2025. User

behavior simulation with large language model-based agents. ACM Transactions on Information Systems 43, 2 (2025), 1–37.

[206] Shuoxin Wang, Chang Liu, Gowen Loo, Lifan Zheng, Kaiwen Wei, Xinyi Zeng, Jingyuan Zhang, and Yu Tian. 2026. Me-Agent: A Personalized

Mobile Agent with Two-Level User Habit Learning for Enhanced Interaction. arXiv preprint arXiv:2601.20162 (2026).

[207] Tianze Wang, Dongnan Gui, Yifan Hu, Shuhang Lin, and Linjun Zhang. 2025. Mpo: An efficient post-processing framework for mixing

diverse preference alignment. arXiv preprint arXiv:2502.18699 (2025).

[208] Wenxuan Wang, Zizhan Ma, Zheng Wang, Chenghan Wu, Jiaming Ji, Wenting Chen, Xiang Li, and Yixuan Yuan. 2025. A survey of llm-based

agents in medicine: How far are we from baymax? arXiv preprint arXiv:2502.11211 (2025).

[209] Yu Wang and Xi Chen. 2025. Mirix: Multi-agent memory system for llm-based agents. arXiv preprint arXiv:2507.07957 (2025).
[210] Yuxin Wang, Yiran Guo, Yining Zheng, Zhangyue Yin, Shuo Chen, Jie Yang, Jiajun Chen, Yuan Li, Xuanjing Huang, and Xipeng Qiu. 2025.

FamilyTool: A Multi-hop Personalized Tool Use Benchmark. arXiv preprint arXiv:2504.06766 (2025).

[211] Yu Wang, Dmitry Krotov, Yuanzhe Hu, Yifan Gao, Wangchunshu Zhou, Julian McAuley, Dan Gutfreund, Rogerio Feris, and Zexue He. 2025.

M+: Extending MemoryLLM with Scalable Long-Term Memory. arXiv preprint arXiv:2502.00592 (2025).

[212] Yu Wang, Xinshuang Liu, Xiusi Chen, Sean O’Brien, Junda Wu, and Julian McAuley. 2024. Self-updatable large language models by integrating

context into model parameters. arXiv preprint arXiv:2410.00487 (2024).

[213] Yu Wang, Ryuichi Takanobu, Zhiqi Liang, Yuzhen Mao, Yuanzhe Hu, Julian McAuley, and Xiaojian Wu. 2025. Mem-{\alpha}: Learning

Memory Construction via Reinforcement Learning. arXiv preprint arXiv:2509.25911 (2025).

[214] Zhefan Wang, Yuanqing Yu, Wendi Zheng, Weizhi Ma, and Min Zhang. 2024. Macrec: A multi-agent collaboration framework for
recommendation. In Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval.
2760–2764.

[215] Zixiang Wang, Yinghao Zhu, Huiya Zhao, Xiaochen Zheng, Dehao Sui, Tianlong Wang, Wen Tang, Yasha Wang, Ewen Harrison, Chengwei
Pan, et al. 2025. Colacare: Enhancing electronic health record modeling through large language model-driven multi-agent collaboration. In
Proceedings of the ACM on Web Conference 2025. 2250–2261.

[216] Azmine Toushik Wasi, Wahid Faisal, and Mst Rafia Islam. 2025. Mina: A Multilingual LLM-Powered Legal Assistant Agent for Bangladesh

for Empowering Access to Justice. arXiv preprint arXiv:2511.08605 (2025).

[217] Hui Wei, Zihao Zhang, Shenghua He, Tian Xia, Shijia Pan, and Fei Liu. 2025. Plangenllms: A modern survey of llm planning capabilities. In
Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 19497–19521.
[218] Lilian Weng. 2023. LLM-powered Autonomous Agents. lilianweng.github.io (Jun 2023). https://lilianweng.github.io/posts/2023-06-23-agent/
[219] Rebecca Westhäußer, Frederik Berenz, Wolfgang Minker, and Sebastian Zepf. 2025. CAIM: Development and Evaluation of a Cognitive AI

Memory Framework for Long-Term Interaction with Intelligent Agents. arXiv preprint arXiv:2505.13044 (2025).

[220] Rebecca Westhäußer, Wolfgang Minker, and Sebatian Zepf. 2025. Enabling Personalized Long-term Interactions in LLM-based Agents

through Persistent Memory and User Profiles. arXiv preprint arXiv:2510.07925 (2025).

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 34 -->

34

• Y. Xu et al.

[221] Bin Wu, Zhengyan Shi, Hossein A Rahmani, Varsha Ramineni, and Emine Yilmaz. 2024. Understanding the role of user profile in the

personalization of large language models. arXiv preprint arXiv:2406.17803 (2024).

[222] Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, and Dong Yu. 2025. LongMemEval: Benchmarking Chat Assistants on

Long-Term Interactive Memory. In The Thirteenth International Conference on Learning Representations.

[223] Jiaxing Wu, Lin Ning, Luyang Liu, Harrison Lee, Neo Wu, Chao Wang, Sushant Prakash, Shawn O’Banion, Bradley Green, and Jun Xie.
2025. Rlpf: Reinforcement learning from prediction feedback for user summarization with llms. In Proceedings of the AAAI Conference on
Artificial Intelligence, Vol. 39. 25488–25496.

[224] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, et al. 2024.

Autogen: Enabling next-gen LLM applications via multi-agent conversations. In First Conference on Language Modeling.

[225] Shujin Wu, May Fung, Cheng Qian, Jeonghwan Kim, Dilek Hakkani-Tur, and Heng Ji. 2024. Aligning llms with individual preferences via

interaction. arXiv preprint arXiv:2410.03642 (2024).

[226] Yaozu Wu, Jizhou Guo, Dongyuan Li, Henry Peng Zou, Wei-Chieh Huang, Yankai Chen, Zhen Wang, Weizhi Zhang, Yangning Li, Meng

Zhang, et al. 2025. Psg-agent: Personality-aware safety guardrail for llm-based agents. arXiv preprint arXiv:2509.23614 (2025).

[227] Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang, Huifeng Guo, Ruiming Tang, and Yong Liu. 2025. From human

memory to ai memory: A survey on memory mechanisms in the era of llms. arXiv preprint arXiv:2504.15965 (2025).

[228] Yuwei Wu, Xuezhe Ma, and Diyi Yang. 2021. Personalized response generation via generative split memory network. In Proceedings
of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.
1956–1970.

[229] Yuchen Wu, Edward Sun, Kaijie Zhu, Jianxun Lian, Jose Hernandez-Orallo, Aylin Caliskan, and Jindong Wang. 2025. Personalized Safety in

LLMs: A Benchmark and A Planning-Based Agent Approach. arXiv preprint arXiv:2505.18882 (2025).

[230] Yaxiong Wu, Yongyue Zhang, Sheng Liang, and Yong Liu. 2025. Sgmem: Sentence graph memory for long-term conversational agents. arXiv

preprint arXiv:2509.21212 (2025).

[231] Yunjia Xi, Weiwen Liu, Jianghao Lin, Bo Chen, Ruiming Tang, Weinan Zhang, and Yong Yu. 2024. Memocrs: Memory-enhanced sequential
conversational recommender systems with large language models. In Proceedings of the 33rd ACM International Conference on Information
and Knowledge Management. 2585–2595.

[232] Yunjia Xi, Weiwen Liu, Jieming Zhu, Xilong Zhao, Xinyi Dai, Ruiming Tang, Weinan Zhang, Rui Zhang, and Yong Yu. 2022. Multi-
level interaction reranking with user behavior history. In Proceedings of the 45th International ACM SIGIR Conference on Research and
Development in Information Retrieval. 1336–1346.

[233] Derong Xu, Yi Wen, Pengyue Jia, Yingyi Zhang, Yichao Wang, Huifeng Guo, Ruiming Tang, Xiangyu Zhao, Enhong Chen, Tong Xu, et al.
2025. Towards multi-granularity memory association and selection for long-term conversational agents. arXiv preprint arXiv:2505.19549
(2025).

[234] Manjie Xu, Xinyi Yang, Wei Liang, Chi Zhang, and Yixin Zhu. 2025. Learning to Plan with Personalized Preferences. arXiv preprint

arXiv:2502.00858 (2025).

[235] Qiancheng Xu, Yongqi Li, Heming Xia, Fan Liu, Min Yang, and Wenjie Li. 2025. Petoolllm: Towards personalized tool learning in large

language models. In Findings of the Association for Computational Linguistics: ACL 2025. 21488–21503.

[236] Songlin Xu, Xinyu Zhang, and Lianhui Qin. 2024. Eduagent: Generative student agents in learning. arXiv preprint arXiv:2404.07963 (2024).
[237] Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Yongfeng Zhang. 2025. A-mem: Agentic memory for llm agents. arXiv

preprint arXiv:2502.12110 (2025).

[238] Xinchao Xu, Zhibin Gou, Wenquan Wu, Zheng-Yu Niu, Hua Wu, Haifeng Wang, and Shihang Wang. 2022. Long time no see! open-domain
conversation with long-term persona memory. In Findings of the Association for Computational Linguistics: ACL 2022. 2639–2650.
[239] Yangyang Xu, Jinpeng Hu, Zhuoer Zhao, Zhangling Duan, Xiao Sun, and Xun Yang. 2025. MultiAgentESC: A LLM-based Multi-Agent
Collaboration Framework for Emotional Support Conversation. In Proceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing. 4665–4681.

[240] Yiyan Xu, Jinghao Zhang, Alireza Salemi, Xinting Hu, Wenjie Wang, Fuli Feng, Hamed Zamani, Xiangnan He, and Tat-Seng Chua. 2025.

Personalized generation in large model era: A survey. arXiv preprint arXiv:2503.02614 (2025).

[241] Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Kristian Kersting, Jeff Z Pan, Hinrich Schütze,
et al. 2025. Memory-r1: Enhancing large language model agents to manage and utilize memories via reinforcement learning. arXiv preprint
arXiv:2508.19828 (2025).

[242] Yibo Yan, Shen Wang, Jiahao Huo, Philip S Yu, Xuming Hu, and Qingsong Wen. 2025. Mathagent: Leveraging a mixture-of-math-agent
framework for real-world multimodal mathematical error detection. In Proceedings of the 63rd Annual Meeting of the Association for
Computational Linguistics (Volume 6: Industry Track). 69–82.

[243] Hongyang Yang, Boyu Zhang, Neng Wang, Cheng Guo, Xiaoli Zhang, Likun Lin, Junlin Wang, Tianyu Zhou, Mao Guan, Runjia Zhang, et al.
2024. Finrobot: An open-source ai agent platform for financial applications using large language models. arXiv preprint arXiv:2405.14767
(2024).

[244] Yandan Yang, Baoxiong Jia, Shujie Zhang, and Siyuan Huang. 2025. Sceneweaver: All-in-one 3d scene synthesis with an extensible and

self-reflective agent. arXiv preprint arXiv:2509.20414 (2025).

[245] Chaerin Yu, Chihun Choi, Sunjae Lee, Hyosu Kim, Steven Y Ko, Young-Bae Ko, and Sangeun Oh. 2026. Leveraging LLMs for Efficient and

Personalized Smart Home Automation. arXiv preprint arXiv:2601.04680 (2026).

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

---

<!-- PAGE 35 -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions

•

35

[246] Shuo Yu, Mingyue Cheng, Daoyu Wang, Qi Liu, Zirui Liu, Ze Guo, and Xiaoyu Tao. 2025. MemWeaver: A Hierarchical Memory from Textual

Interactive Behaviors for Personalized Generation. arXiv preprint arXiv:2510.07713 (2025).

[247] Ruifeng Yuan, Shichao Sun, Yongqi Li, Zili Wang, Ziqiang Cao, and Wenjie Li. 2025. Personalized Large Language Model Assistant with

Evolving Conditional Memory. In Proceedings of the 31st International Conference on Computational Linguistics.

[248] Saber Zerhoudi and Michael Granitzer. 2024. Personarag: Enhancing retrieval-augmented generation systems with user-centric agents.

arXiv preprint arXiv:2407.09394 (2024).

[249] Cong Zhang, Xin Deik Goh, Dexun Li, Hao Zhang, and Yong Liu. 2025. Planning with multi-constraints via collaborative language agents.

In Proceedings of the 31st International Conference on Computational Linguistics. 10054–10082.

[250] Junjie Zhang, Yupeng Hou, Ruobing Xie, Wenqi Sun, Julian McAuley, Wayne Xin Zhao, Leyu Lin, and Ji-Rong Wen. 2024. Agentcf:
Collaborative learning with autonomous language agents for recommender systems. In Proceedings of the ACM Web Conference 2024.
3679–3689.

[251] Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xionghui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang,

et al. 2024. Aflow: Automating agentic workflow generation. arXiv preprint arXiv:2410.10762 (2024).

[252] Kai Zhang, Xinyuan Zhang, Ejaz Ahmed, Hongda Jiang, Caleb Kumar, Kai Sun, Zhaojiang Lin, Sanat Sharma, Shereen Oraby, Aaron Colak,

et al. 2025. AssoMem: Scalable Memory QA with Multi-Signal Associative Retrieval. arXiv preprint arXiv:2510.10397 (2025).

[253] Lemei Zhang, Peng Liu, Marcus Henriksboe, Even Lauvrak, Jon Atle Gulla, and Heri Ramampiaro. 2024. Personalsum: A user-subjective
guided personalized summarization dataset for large language models. Advances in Neural Information Processing Systems 37 (2024),
99333–99346.

[254] Weizhi Zhang, Xinyang Zhang, Chenwei Zhang, Liangwei Yang, Jingbo Shang, Zhepei Wei, Henry Peng Zou, Zijie Huang, Zhengyang Wang,
Yifan Gao, et al. 2025. Personaagent: When large language model agents meet personalization at test time. arXiv preprint arXiv:2506.06254
(2025).

[255] Xuan Zhang, Yang Deng, Zifeng Ren, See Kiong Ng, and Tat-Seng Chua. 2024. Ask-before-plan: Proactive language agents for real-world

planning. In Findings of the Association for Computational Linguistics: EMNLP 2024. 10836–10863.

[256] Xinliang Frederick Zhang, Nick Beauchamp, and Lu Wang. 2025. PRIME: Large Language Model Personalization with Cognitive Dual-
Memory and Personalized Thought Process. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing.
33695–33724.

[257] Yingyi Zhang, Pengyue Jia, Derong Xu, Yi Wen, Xianneng Li, Yichao Wang, Wenlin Zhang, Xiaopeng Li, Weinan Gan, Huifeng Guo, et al.
2025. Personalize Before Retrieve: LLM-based Personalized Query Expansion for User-Centric Retrieval. arXiv preprint arXiv:2510.08935
(2025).

[258] Yu Zhang, Shutong Qiao, Jiaqi Zhang, Tzu-Heng Lin, Chen Gao, and Yong Li. 2025. A survey of large language model empowered agents for

recommendation and search: Towards next-generation information retrieval. arXiv preprint arXiv:2503.05659 (2025).

[259] Zhaowei Zhang, Fengshuo Bai, Qizhi Chen, Chengdong Ma, Mingzhi Wang, Haoran Sun, Zilong Zheng, and Yaodong Yang. 2025. Amulet:

Realignment during test time for personalized preference adaptation of LLMs. arXiv preprint arXiv:2502.19148 (2025).

[260] Zeyu Zhang, Quanyu Dai, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Jieming Zhu, Zhenhua Dong, and Ji-Rong Wen. 2025. A survey on the

memory mechanism of large language model-based agents. ACM Transactions on Information Systems 43, 6 (2025), 1–47.

[261] Zhehao Zhang, Ryan A Rossi, Branislav Kveton, Yijia Shao, Diyi Yang, Hamed Zamani, Franck Dernoncourt, Joe Barrow, Tong Yu, Sungchul

Kim, et al. 2024. Personalization of large language models: A survey. arXiv preprint arXiv:2411.00027 (2024).

[262] Siyan Zhao, Mingyi Hong, Yang Liu, Devamanyu Hazarika, and Kaixiang Lin. 2025. Do llms recognize your preferences? evaluating

personalized preference following in llms. arXiv preprint arXiv:2502.09597 (2025).

[263] Weixiang Zhao, Xingyu Sui, Yulin Hu, Jiahe Guo, Haixiao Liu, Biye Li, Yanyan Zhao, Bing Qin, and Ting Liu. 2025. Teaching Language

Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment. arXiv preprint arXiv:2505.15456 (2025).

[264] Xinkui Zhao, Haode Li, Yifan Zhang, Guanjie Cheng, and Yueshen Xu. 2025. TRAIL: Joint Inference and Refinement of Knowledge Graphs

with Large Language Models. arXiv preprint arXiv:2508.04474 (2025).

[265] Zheng Zhao, Clara Vania, Subhradeep Kayal, Naila Khan, Shay B Cohen, and Emine Yilmaz. 2025. Personalens: A benchmark for personal-

ization evaluation in conversational ai assistants. In Findings of the Association for Computational Linguistics: ACL 2025. 18023–18055.

[266] Arman Zharmagambetov, Chuan Guo, Ivan Evtimov, Maya Pavlova, Ruslan Salakhutdinov, and Kamalika Chaudhuri. 2025. Agentdam:

Privacy leakage evaluation for autonomous web agents. arXiv preprint arXiv:2503.09780 (2025).

[267] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric
Xing, et al. 2023. Judging llm-as-a-judge with mt-bench and chatbot arena. Advances in neural information processing systems 36 (2023),
46595–46623.

[268] Xi Zheng, Zhuoyang Li, Xinning Gui, and Yuhan Luo. 2025. Customizing Emotional Support: How Do Individuals Construct and Interact
With LLM-Powered Chatbots. In Proceedings of the Extended Abstracts of the CHI Conference on Human Factors in Computing Systems.
[269] Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. 2024. Memorybank: Enhancing large language models with long-term

memory. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38. 19724–19731.

[270] Filippo Ziliotto, Jelin Raphael Akkara, Alessandro Daniele, Lamberto Ballan, Luciano Serafini, and Tommaso Campari. 2025. Personal:

Towards a comprehensive benchmark for personalized embodied agents. arXiv preprint arXiv:2509.19843 (2025).

ACM Comput. Surv., Vol. 1, No. 1, Article . Publication date: March 2026.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and
Future Directions
YUEXU,ShanghaiTechUniversity,China
QI’ANCHEN,TongjiUniversity,China
ZIZHANMA,TheChineseUniversityofHongKong,China
DONGRUILIU,ShanghaiArtificialIntelligenceLaboratory,China
WENXUANWANG,RenminUniversityofChina,China
XITINGWANG,RenminUniversityofChina,China
LIXIONG,EmoryUniversity,UnitedStates
WENJIEWANG†,ShanghaiTechUniversity,China
Largelanguagemodelshaveenabledagenticsystemsthatreason,plan,andinteractwithtoolsandenvironmentstoaccomplish
complextasks.Astheseagentsoperateoverextendedinteractionhorizons,theireffectivenessincreasinglydependsonadapting
behaviortoindividualusersandmaintainingcontinuityacrossinteractions,givingrisetopersonalizedLLM-poweredagents(PLAs).
Insuchlong-term,user-dependentsettings,personalizationpermeatestheentiredecisionpipelineratherthanremainingconfinedto
surface-levelresponsegeneration.Thissurveyprovidesacapability-orientedreviewofpersonalizedLLM-poweredagents.Existing
workisorganizedaroundfourinterdependentcapabilities:profilemodeling,memory,planning,andactionexecution.Usingthis
taxonomy,representativemethodsaresynthesizedandanalyzedtoillustratehowusersignalsarerepresented,propagated,and
utilizedacrosstheagentpipeline,highlightingcross-componentinteractionsandrecurringdesignchallenges.Evaluationmetrics
andbenchmarkingparadigmstailoredtopersonalizedagentsarefurtherexamined,alongwithapplicationscenariosrangingfrom
conversationalassistantstodomain-specificexpertsystems.Byclarifyingthedesignspaceofpersonalizationinagentsystems,
thissurveyprovidesastructuredfoundationfordevelopingmoreuser-aligned,adaptive,anddeployableLLM-poweredagents.
CCSConcepts:•Generalandreference→Surveysandoverviews;•Human-centeredcomputing;•Computingmethod-
ologies→Intelligentagents;
AdditionalKeyWordsandPhrases:Personalization,PersonalizedLLM-poweredAgent
ACMReferenceFormat:
Yue Xu, Qi’an Chen, Zizhan Ma, Dongrui Liu, Wenxuan Wang, Xiting Wang, Li Xiong, and Wenjie Wang†. 2026. Toward
PersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections.ACMComput.Surv.1,1(March2026),35pages.
https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
Largelanguagemodels(LLMs)haveevolvedfrompassivetextgeneratorsintogeneral-purposereasoningsystems
capableofunderstandingdiversedata,planningactions,andusingexternaltools.Buildingonthesecapabilities,
LLM-poweredagentsextendLLMsintointegratedsystemsthatdecomposecomplexobjectives,invoketools,interact
withdynamicenvironments,andcoordinatewithhumansorotheragentstoachievehigh-levelgoalsoverextended
†CorrespondingAuthor.
Authors’Contactinformation:YueXu,ShanghaiTechUniversity,China;email:xuyue2022@shanghaitech.edu.cn;Qi’anChen,TongjiUniversity,
China;email:2250951@tongji.edu.cn;ZizhanMa,TheChineseUniversityofHongKong,China;email:zzma2@cse.cuhk.edu.hk;DongruiLiu,
ShanghaiArtificialIntelligenceLaboratory,China;email:liudongrui@pjlab.org.cn;WenxuanWang,RenminUniversityofChina,China;email:
wangwenxuan@ruc.edu.cn;XitingWang,RenminUniversityofChina,China;email:xitingwang@ruc.edu.cn;LiXiong,EmoryUniversity,United
States;email:lxiong@emory.edu;WenjieWang,ShanghaiTechUniversity,China;email:wangwj1@shanghaitech.edu.cn.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfeeprovidedthatcopiesare
notmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitationonthefirstpage.Copyrightsfor
componentsofthisworkownedbyothersthantheauthor(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,
topostonserversortoredistributetolists,requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2026Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ACM1557-7341/2026/3-ART
https://doi.org/XXXXXXX.XXXXXXX
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.
6202
raM
61
]IA.sc[
2v08622.2062:viXra

2 • Y.Xuetal.
horizons[1,110,192,204].ThisshiftmarksnotonlyatechnicalexpansionofLLMcapabilitiesbutalsoabroader
shifttowardautonomous,adaptive,andsociallygroundedintelligentassistants.
Asagentsystemsincreasinglysupportlong-terminteractionandautonomousdecision-making,personalization
emergesasacentralrequirementformaintainingcontextualcontinuityandaligningagentbehaviorwithindividual
userpreferencesacrossdomainssuchaseducation,healthcare,andrecommendation[24,139,208].Forpersonalized
LLM-poweredagents(PLAs),personalizationextendsbeyondresponsestyleandoperatesacrossthefulldecision
pipeline,influencinghowagentsinferuserintent,preserveuser-relevantinformationovertime,generatepersonalized
plans,andcarryoutactionsinexternalenvironments[194,261].However,thisbroadenedscopealsointroduces
substantial challenges, including integrating dynamic and multimodal feedback, preserving consistency across
interactingcomponents,reconcilinguser-specificadaptationwithgeneralcompetence,andsafeguardingprivacyand
security.Asaresult,theevaluationofPLAsmustmovebeyondstaticcorrectnessandinsteadaccountforlong-term
effectiveness,adaptability,andusersatisfaction.
Despitethegrowinginterest,reviewsonPLAsremainfragmented.Priorsurveysoftenfocusonisolatedcapabilities
of general LLM-powered agents or isolated components of personalization, such as user modeling and memory
construction[227,260],planningandreasoningstrategies[217],oradaptiveinteractionmechanisms[38,94].Such
capability-specificperspectiveshaveprovidedvaluableinsights,butaunifiedviewofhowpersonalizationobjectives
propagateacrossthefullagentlifecycleisstilllacking.Inparticular,theinteractionsamongdifferentpersonalization
mechanismsandtheirimplicationsforevaluationanddeploymentremaininsufficientlyunderstood.
Toaddressthisgap,thissurveypresentsacapability-orientedandsystem-levelperspectiveonPLAs.Weexamine
personalization as a distributed property instantiated across four interdependent components: profile modeling,
memory,planning,andactionexecution.Thisdecompositionenablesasystematicanalysisofhowuser-specific
signalsarerepresented,propagated,andoperationalizedthroughouttheagentlifecycle,fromintentunderstandingto
real-worldoutcomes.AsillustratedinFigure1,whenanindividualusersubmitsarequest,aPLAcoordinatesthese
fourcapabilitiestoproduceatailoredresponse.Profilerepresentationsandroledefinitionsshapetheagent’sinternal
modeloftheuser,thememorymoduleorganizesandretrievesrelevantcontextualinformation,planningdetermines
personalizeddecisionstrategies,andactionexecutiongroundsthesedecisionsintheexternalenvironment.The
resultingoutcomes,togetherwithsubsequentuserfeedback,inturnrefinetheagent’sinternalrepresentationofuser
preferences,formingaclosedloopthatenablesiterativeandsustainedpersonalizationovertime.
Buildingonthistaxonomy,wereviewrepresentativemethods,benchmarks,andevaluationprotocols,summarize
majorapplicationdomains,andidentifyopenchallengesandfutureresearchdirections.Thesurveyaimstoclarifythe
designspaceofpersonalizedagents,connectbenchmark-drivenresearchwithreal-worlddeploymentrequirements,
andprovideastructuredfoundationfordevelopingtrustworthy,effective,andscalablepersonalizedagentsystems.
Ourcontributionsareasfollows:
(1) WeintroduceaunifiedtaxonomythatorganizespersonalizedLLM-poweredagentsaroundfourcorecapabilities
(profilemodeling,memorymanagement,planning,andactionexecution),providingasystem-levelviewof
howpersonalizationisrealizedacrosstheagentpipeline(§2).
(2) Wepresentanextensivereviewofrecenttechniques,benchmarks,andevaluationprotocols(§3–§7),highlighting
howpersonalizationmechanismsoperatewithinandacrossagentcomponentsandhowpersonalizationis
assessedinpractice.
(3) Wesurveyrepresentativeapplicationdomainsofpersonalizedagentsanddiscussopenchallengesandpromising
researchdirections(§8-§9).
2 FoundationsofPersonalizedLLM-poweredAgents
2.1 LLM-poweredAgents
AnLLM-poweredagentisanautonomoussystemthatintegratesalargelanguagemodelwithexternaltoolsand
utilitiestosupportstep-by-stepinteractionwithopen-endedenvironmentsfortaskcompletion[35].Theenvironment
includesboththeuserandtheexecutioncontext,andischaracterizedbyanexternalstatespaceS thatgoverns
environmentdynamicsandfeedback.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 3
User Profile Modeling
|     |     |     |     |     | Profiles | Memory Schemes | Personalized Retrieval |
| --- | --- | --- | --- | --- | -------- | -------------- | ---------------------- |
(structure+update)
|             |     |               | response-based /      |     |                  |            | content-based /  |
| ----------- | --- | ------------- | --------------------- | --- | ---------------- | ---------- | ---------------- |
|             |     |               | persona-based         |     | +                | textual/   | structure-aware/ |
|             |     |               |                       |     |                  | structured | policy-guided    |
| Individual  |     | Personalized  | Agent Role Definition |     |                  |            |                  |
|             |     |               |                       |     | § 3.  P r o f il | e          |                  |
| User        |     | Agent         | user-substituting /   |     |                  | §4. Memory | Relevant         |
|             |     |               |                       |     | M o d e li n g   |            |                  |
|             |     |               | user-adaptive         |     |                  |            | Memory           |
Request
One-Shot
Execution
|     | Response |     | Outcome |     | §6. Action  |              |                        |
| --- | -------- | --- | ------- | --- | ----------- | ------------ | ---------------------- |
|     |          |     |         |     | Execution   | §5. Planning | user signal grounding/ |
internal refinement
|     |     |     | Post-action |     | Pre-action |     |     |
| --- | --- | --- | ----------- | --- | ---------- | --- | --- |
Feedback-Driven
| User Request ing |     |     | execution-time  |     |                 |               |                        |
| ---------------- | --- | --- | --------------- | --- | --------------- | ------------- | ---------------------- |
|                  |     |     |                 |     | action policy + | Personalized  | clarification seeking/ |
Personalized Response Generation correction +  action grounding Plan user revision/
outcome realization
| Iterative Personalization |     |     |     |     |     |     | non-user feedback |
| ------------------------- | --- | --- | --- | --- | --- | --- | ----------------- |
Fig.1. OverviewofpersonalizedLLM-poweredagents.Uponreceivingauserrequest,theagentcoordinatesprofilemodeling,
memory,planning,andactionexecutiontogenerateatailoredresponse.Interactionoutcomesprovidefeedbackthatrefinesuser
preferencerepresentations,enablingiterativeandlong-termpersonalization.
Ateachtimestep𝑡,theenvironmentisinastate𝑠 thatcapturestheexternallyavailableinformationrelevantto
𝑡
thetask,includinguserinputs,tooloutputs,orotherexternalsignals.Theagentmaintainsaninternalstateℎ ,which
𝑡
capturesaccumulatedcontextsuchasretrievedmemory,intermediatereasoningresults,andinternalrepresentations
usedfordecisionmaking.Theagent’sbehaviorcanbeabstractedasapolicythatselectsanaction𝑎 conditionedon
𝑡
boththecurrentenvironmentstateanditsinternalstate:
|     |     |     |     | 𝜋(𝑎 𝑡|𝑠 | ,ℎ 𝑡). |     |     |
| --- | --- | --- | --- | ------- | ------ | --- | --- |
𝑡
Actions may correspond to natural language responses, planning steps, tool invocations, or other environment
interactions.Theenvironmentthenevolvesaccordingtoacontrolledtransitionprocess,producingasubsequent
externalstate𝑠 ,andtheagentupdatesitsinternalstateaccordinglyas
𝑡+1
|     |     |     | ℎ   | =𝑓(ℎ | ,𝑎 ,𝑠 𝑡+1). |     |     |
| --- | --- | --- | --- | ---- | ----------- | --- | --- |
|     |     |     | 𝑡+1 | 𝑡    | 𝑡           |     |     |
Startingfromaninitialstate𝑠 0 ,suchasauserqueryortaskspecification,executionproceedsiterativelyuntila
terminationconditionismet,yieldingatrajectory
|     |     |     | 𝜏 =(𝑠 ,ℎ | ,𝑎 ,𝑠 | ,...,𝑎 ,𝑠 | 𝑇). |     |
| --- | --- | --- | -------- | ----- | --------- | --- | --- |
|     |     |     | 0        | 0 0 1 | 𝑇−1       |     |     |
Thistrajectoryreflectstheagent’sevolvinginterpretationofthetaskanditsinteractionhistory.Foranalysisor
evaluation purposes, execution outcomes can be assessed using a feedback or reward function defined over the
| trajectory,denotedas𝑟 |     | =R(𝜏). |     |     |     |     |     |
| --------------------- | --- | ------ | --- | --- | --- | --- | --- |
Atthesystemlevel,LLM-poweredagentsrelyonasetoftightlycoupledcognitivecapabilitiesthatenableadaptive
andgoal-directedbehavior[110,204].Profilingshapeshowtheagentinterpretsitsroleandoperatingcontext.Memory
supportscontinuitybyretainingandorganizinginformationacrossinteractions.Planninggovernsthetransformation
ofhigh-levelobjectivesintostructureddecisionprocesses.Actionexecutionrealizesthesedecisionsthroughtooluse
ordirectinteractionwiththeenvironment.Together,thesecapabilitieselevatelargelanguagemodelsintointeractive
decision-makingsystemscapableofsustainedautonomy.
2.2 PersonalizedLLM-poweredAgents
ApersonalizedLLM-poweredagentisanLLM-basedagentwhoseinternalpipelineisadaptedtoindividualusers
throughuser-specificpreferences.Foreachuser𝑢 ∈U,theagentmaintainsarepresentationoftheuser’spreferences
𝑝 inferredfrominteractionhistory,feedback,orexplicitinput.
𝑢
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

4 • Y.Xuetal.
Ateachtimestep𝑡,theenvironmentisinastate𝑠 ,andtheagentmaintainsaninternalstateℎ(𝑢) specifictothe
𝑡 𝑡
user.Theagentinterpretsandactsuponuserpreferencesbyconditioningitsdecisionpolicyon𝑝 .Thisyieldsa
𝑢
user-conditionedpolicy
𝜋(𝑎 𝑡|𝑠
𝑡
,ℎ
𝑡
,𝑝 𝑢),
whichselectsanaction𝑎 giventhecurrentenvironmentstate,internalstate,anduserpreferences.Theenvironment
𝑡
transitionstoanewstate𝑠 ,andtheagentupdatesitsinternalstateas
𝑡+1
ℎ
𝑡+1
=𝑓(ℎ
𝑡
,𝑎
𝑡
,𝑠
𝑡+1
,𝑝 𝑢),
whereuserpreferencesmaybeexplicitlystoredwithintheinternalstateorprovidedasanexternalconditioning
signal.Executingthispolicyfromaninitialstateproducesauser-conditionedinteractiontrajectory
𝜏(𝑢) =(𝑠
0
,ℎ
0
(𝑢),𝑎
0
(𝑢),𝑠
1
,...,𝑠 𝑇),
wherethesuperscript(𝑢)indicatesthatthetrajectoryisinducedbydecision-makingconditionedonuserpreferences.
Personalizationreferstotheprocessthroughwhichuserpreferencesareaccumulated,represented,andintegrated
intoanagent’sdecisionpipeline,allowingthesametaskspecificationQtogiverisetodifferentoutcomesfordifferent
users. Through repeated interaction, the agent collects user-centric data D𝑢 and refines an internal preference
representation𝑝ˆ
𝑢
=𝑝(D𝑢),whichconditionssubsequentactionselection.Atanabstractlevel,personalizationcan
beviewedasfavoringdecisionsthatyieldhigheruser-alignedutilityoverinteractiontrajectories:
𝜋
𝑢
∗ ∝ argm
𝜋
axE
𝜏(𝑢)∼𝜋(·|Q,𝑝ˆ 𝑢)
R𝑢(𝜏(𝑢)),
where𝑝ˆ
𝑢
denotes an internal representation of user preferences maintained by the agent, and R𝑢(𝜏(𝑢)) denotes
feedbackreflectinguser-specificsatisfactionoralignment.
Fromasystemperspective,personalizationformsaclosedinteractionloop.User-specificpreferencerepresentations
conditiontheagent’sperception,reasoning,andactionselection;executedactionsshapesubsequentinteractions;
andtheresultingoutcomesprovidenewsignalsthatrefine𝑝ˆ .Throughrepeatedexecutionofthisloop,personalized
𝑢
LLM-poweredagentsprogressivelyaligntheirbehaviorwithindividualusers,enablinglong-termadaptivityand
consistentuser-specificbehavior.
2.3 User-CentricData
TheinternalrepresentationofuserpreferencesinLLM-powered agentsisgroundedinuser-centric data,which
capturescontextualinformation,feedback,andinteractiontracesassociatedwithaspecificuser.Fromatemporaland
functionalperspective,user-centricdatacanbebroadlydividedintohistoricaldataandinteractiondata.
Historical Data refers to information available before task execution, including user identifiers, demographic
attributes,andrecordsofpriorinteractionsandfeedback.Thiscontextprovidesafront-loadedpriorovertheuserfor
thecurrentepisode,capturingrelativelystableusercharacteristicstogetherwithaccumulatedevidencefrompast
interactions,whichsupportsconsistentbehaviorandcross-taskgeneralization.
InteractionDataisgeneratedduringtaskexecutionandcapturesreal-timeuserinputs,feedback,andcontextual
cues.Itincludesbothexplicitsignals,suchascorrectionsorratings,andimplicitsignals,suchasbehavioralpatterns
or response timing. Interaction data reflects the user’s momentary intent and is critical for guiding immediate
decision-making,includingreasoningadjustmentsanddynamicactionselection.
Thesetwodatatypesenabledual-timescalepersonalization:historicaldatadefineswhotheuseris,whileinteraction
datadetermineshowtheagentshouldactnow.AsillustratedinFigure2,historicaldataguidestheagent’sbehavior
duringinteraction,whileinteractiondatarefinesandexpandsthehistoricalrecord,togetherformingacontinuous
cycleofuser-awareadaptation.
2.4 UserPreferences
UserpreferencesconstitutethecoresignalsthatenablepersonalizationinLLM-poweredagentsbyconditioningtheir
internalstate,decision-makingprocesses,anduser-specificfeedback.Priorworkcommonlycategorizespreferences
according to their mode of expression [87, 261]. Explicit preferences are directly specified by users and can be
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 5
Historical Data Guide Interaction Data
User Demographic Explicit Feedback
Identifiers Attributes
(confirmations, corrections, ratings......)
Historical User Implicit Feedback
Interactions Feedback Refine (response latency, tone, emotions.....)
Fig.2. User-specificdatainpersonalizationprocess.
incorporatedintotheagentwithoutadditionalinference.Implicitpreferencesareinferredindirectlyfrombehavioral
patternsorcontextualcues,reflectinguserjudgmentsinalatentorunder-specifiedform.
Beyondexpressionform,preferencescanbecharacterizedbytheirsemanticfunction,capturingwhichaspect
oftheusertheyencode.Wedistinguishbehavioralpreferences,whichgovernhowuserscommunicateandreason,
andtopicalpreferences,whichspecifywhatusersprioritizeinagivencontext.Behavioralpreferencesencompass
tone,reasoningstyle,generalinteractiontendencies,andpersonality-relatedtraits,andareoftenstableacrosstasks.
Topicalpreferencescoverdomaininterests,factualstances,andlikesordislikestowardspecificentitiesorevents,
andvarymorewithcontext.Bothtypescanbestatedexplicitlyorinferredimplicitly,yieldingthetwo-dimensional
taxonomyinFigure3.
User: Heyyy! Can you help me pick a place for dinner tonight?
User Preference
I?m hungry and excited but totally indecisive.
Assistant: Sure! There are many factors we can consider, such
as cuisine type, price range, location, dietary restrictions, Behavioral
ambiance, popularity, customer reviews, and whether the
restaurant offers unique or innovative dishes. For example, if
you like Asian food, there are Korean, Thai, and Chinese
options, each with different flavor profiles and dining ...... -Avoid long explanations -Extroverted and lively
User: Whoa whoa pause. That?s way too much already. Long - Concise communication -Prefers minimal options
explanations make my head spin and make choosing harder.
Assistant: Got it! Any dietary restrictions or strong dislikes? Explicit Implicit
User: Yep! Important one. I?m allergic to peanuts.
Assistant: Okay. I?ll avoid peanut-containing restaurants.
User: Oh and two more things! I really don?t like spicy food. -Peanut-free food -Dislikes fusion restaurants
Mild only, please. Last time we went to a super trendy fusion
-Non-spicy cuisine -Prefers quiet dining
spot, the food was awful. And it was loud, chaotic, and
stressful. Totally not my vibe... environments
Assistant: Thanks for letting me know. Based on this, I
recommend a traditional Japanese udon restaurant nearby. It?s
peanut-free, mild in flavor, and known for a calm atmosphere.
If you want one alternative, I can suggest a similar option. Topical
User: Perfect!! That sounds exactly right. Thanks a ton!
Fig.3. Exampleofatwo-dimensionaltaxonomyofuserpreferences.Preferencesarecategorizedbytheirexpressionform(explicit
vs.implicit)andsemanticfunction(behavioralvs.topical),illustratedthroughamulti-turnrecommendationscenario.
In practical systems, explicit preferences can be represented in various forms, including reward vectors [10],
preferenceembeddings[141],ornatural-languageprompts[76].Althoughexplicitsignalsareoftenhighlyinformative,
theyaretypicallysparse,whichlimitstheirdirectapplicabilityforoptimization.Asaresult,implicitpreferencesare
frequentlyleveragedthroughin-contextprompting[75],retrieval-augmentedgeneration(RAG;[144]),orpreference
modelingtechniques[45]thatextractstructuredrepresentationsfromuserbehavioralfeedback.Whenperforming
suchanextraction,accountingforthesemanticfunctionofpreferencesenablesmoretargetedmodelingstrategies
andimprovesinterpretability.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

6 • Y.Xuetal.
2.5 Capability-orientedTaxonomy
PersonalizationinLLM-poweredagentsemergesfromthecoordinatedoperationofmultipleinternalcapabilities
ratherthanfromasingleadaptationmodule.Giventhediversityofuserdata,tasksettings,andpreferencetypes,
user-specificsignalsmustberepresented,retained,reasonedover,andoperationalizedthroughoutthewholepipeline.
Wethereforeadoptacapability-orientedtaxonomy(illustratedinFigure4)thatorganizespersonalizationintofour
interdependentcomponents:
PersonalizationinLLM-poweredagentsdoesnotarisefromasingleadaptationmodule,butfromthecoordinated
operationofmultiplecapabilitiesdistributedacrosstheagentpipeline.Giventhediversityofuserdata,tasksettings,
andpreferencetypes,user-specificsignalsmustberepresented,retained,reasonedover,andultimatelyrealizedin
externalactionsandoutcomes.Wethereforeadoptacapability-orientedtaxonomythatorganizespersonalization
intofourinterdependentcomponents.Thesecomponentsarenotisolatedmodules,butcomplementaryfunctional
stagesthattogethersupportend-to-endpersonalizationinagentsystems.
(1) ProfileModelingstructuresuser-specificinformationintointernalrepresentations,definingbothusercharac-
teristicsandtheagent’srole.
(2) Memorymaintainsandretrievesuser-relevantinformationacrossinteractions,supportingtemporalcontinuity
andconsistentpreferencegrounding.
(3) Planning integrates user-specific information into reasoning processes, shaping decision paths, strategy
selection,andprioritizationundercontextualconstraints.
(4) ActionExecutionoperationalizespersonalizeddecisionsthroughtoolinvocationandenvironmentinteraction,
enablingthefinalpersonalizedoutcome.
To further clarify the distinctions among these four capabilities, Table 1 compares them along several shared
dimensions,includingtheirtypicalinputs,temporalscope,andprimaryobjectives,providingaunifiedanalyticallens
fortheremainderofthesurvey.Inthefollowingsections,werevieweachcapabilityindetail,whilenotingthatmost
existingmethodsfocusononlyoneorasubsetofthesecapabilitiesratherthanthefullpipeline.
Table1. ComparisonofthefourcorecapabilitiesinpersonalizedLLM-poweredagents.
Capability TypicalInputs TemporalScope PrimaryObjective
ProfileModeling User attributes, behavioral his- Lifelong Establishuserunderstandingandsup-
tory,anduserinstructions portagent-useralignment
Memory Interactionhistory,userevents, Turntolifelong Maintaintemporalcontinuityandcon-
contextualrecords sistentpersonalization
Planning Profileinformation,memory,task Turntotask Enablepersonalizedreasoningandde-
context,in-taskfeedback cisionmaking
ActionExecution Plans,toolstates,executionfeed- Steptotask Realize personalized actions and out-
back comes
3 ProfileModeling
Ingeneral-purposeagentsystems,profilesareprimarilyusedtodefinetheagentitself,includingitsintrinsicattributes,
behavioraltendencies,andoperationalboundaries[110].Suchidentitiesareoftenstaticorexternallyspecifiedthrough
fixedroleinstructions,domainexpertise,orpre-definedfunctionalassignments[224,251].InPLAs,however,profile
modelingbecomesexplicitlyuser-centered,modelingtheuseranddynamicallyshapinghowtheagentpositionsitself
whencarryingouttasksforthatuser.Inthissense,profilemodelingservesasthefoundationallayerofPLAs,linking
userunderstandingwithagentroleconfiguration.Accordingly,wediscussprofilemodelingfromtwocomplementary
perspectives:userprofilemodelingandagentroledefinition.
3.1 UserProfileModeling
Userprofilemodelingextractsandorganizesuser-specificsignalsintorepresentationsthatcanguidehowanagent
shouldrespondoract[221].Inthissurvey,wedistinguishtwomajorparadigmsaccordingtohowuserpreferences
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 7
AlignXpert[87],FSPO[175],[201],RLPF[223],RLPA[263],
UserProfile
|     | Modeling | CURIO[197],PFM[10],PReF[168],LoRe[12], |     | Janus[82], |
| --- | -------- | -------------------------------------- | --- | ---------- |
PLUS[125],
ProfileModeling
§3
|     | AgentRole  | ASFM[39],LD-Agent[86],RecAgent[205],PAA[85],Per- |     |     |
| --- | ---------- | ------------------------------------------------ | --- | --- |
|     | Definition | sonaAgent[254],PersonaX[172],RPP[115],           |     |     |
LD-Agent[86],MemoryBank[269],SeCom[136],RMM
[187],Nemori[126],CAIM[219],PREMem[77],Mem-
|     | Memory  | oBase[119],MemInsight[154],MIRIX[209], |                            | Mem-𝛼 |
| --- | ------- | -------------------------------------- | -------------------------- | ----- |
|     | Schemes | [213], MemWeaver[246],                 | M3-Agent[109],RAPTOR[160], |       |
MemTree[152],SGMem[230],LicoMemory[57],Mem0[22],
| Memory |     | Memory-R1[241],A-Mem[237],TRAIL[264] |     |     |
| ------ | --- | ------------------------------------ | --- | --- |
§4
tnegAderewop-MLLdezilanosreP RAPTOR[160],[247],HippoRAG[65],AriGraph[5],Zep
|     | Personalized | [150],MemGAS[233],AssoMem[252],PBR[257],Person- |     |     |
| --- | ------------ | ----------------------------------------------- | --- | --- |
|     | Retrieval    | aRAG[248],UniMS-RAG[200],Persona-DB[180],OCG-   |     |     |
Agent[171],MemInsight[154]
ALIGNXPLORE[88],ReaRec[189],PbP[234],PRIME[256],
|     | One-shot | PSG-Agent[226],TravelPlanner++[176],PTS[165],PREFINE |     |     |
| --- | -------- | ---------------------------------------------------- | --- | --- |
Planning
[195],IoTGPT[245]
Planning
| §5  | Feedback- |     |     |     |
| --- | --------- | --- | --- | --- |
SAGE-Agent[183],ECLAIR[124],Ask-before-Plan[255],
|     | Driven   | AIPOM[74],Dango[18],PlanFitting[173],VAIAGE[101], |     |     |
| --- | -------- | ------------------------------------------------- | --- | --- |
|     | Planning | Collab-Rec[9],SceneWeaver[244]                    |     |     |
PEToolLLaMA[235],PUMA[14],ToolSpectrum[20],Color-
Pre-Action
| ActionExecution |     | Agent[90],AWARE-US[80],[55],ValuePilot[111] |     |     |
| --------------- | --- | ------------------------------------------- | --- | --- |
§6
PEAR[96],MIR[232],WARPP[117],ETAPP[50]
Post-Action
|     | Goalsand | Effectiveness,Adaptivity,Generalization,Robustness,Risk |     |     |
| --- | -------- | ------------------------------------------------------- | --- | --- |
Metrics
IndieValueCatalog[63],ALOE[225],
Evaluation
| §7  |     | Interactive | AgentRecBench[164],LongMemEval   |     |
| --- | --- | ----------- | -------------------------------- | --- |
|     |     | Alignment   | [222],PTBench[55],ETAPP[50],Per- |     |
sonaMem[61],PENGUIN[229]...
Benchmarks
LongLaMP[79],PGraphRAG[7],Per-
|     |     | User- | sonaConvBench[89],LaMP-QA[157], |     |
| --- | --- | ----- | ------------------------------- | --- |
PRISM[78],PEToolBench[235],Trip-
Substitution
Tailor[203],PersONAL[270]...
| Fig.4. | TaxonomyofpersonalizedLLM-poweredagents. |     |     |     |
| ------ | ---------------------------------------- | --- | --- | --- |
arerepresented:persona-based approaches,whichmodeltheuserthroughrelativelyholistictraitsandpreference
descriptions,andresponse-based approaches,whichmodeltheuserthroughpreferencesovercandidateresponsesor
modelbehaviors.
Persona-basedmethodsmodeltheuserthroughrelativelystabletraits,characteristics,
Persona-basedModeling.
andlong-termpreferencedescriptionsthatremaininformativeacrosscontexts.Suchprofilesmaybeconstructed
fromexplicitself-descriptions,behavioralhistory,orhistoricalinteractions,andareoftenrepresentedasstructured
attributevectorsorfree-formnatural-languagepersonasummaries.Indownstreamuse,persona-basedprofilesare
oftenincorporatedaspromptsorconstraintstoguidepersonalizedgenerationanddecisionmaking.Forinstance,
AlignXpert[87]constructsahigh-dimensionalpreferencespacegroundedinpsychologicalandalignment-related
dimensions,whileFSPO[175]producesmorefine-grainedpersonadescriptionsthroughauser-descriptionchain-
of-thought mechanism. Beyond such one-shot profiling, several methods iteratively refine user representations
through interaction: RLPA [263] and Wang and Yang [201] update user representations across rounds, RGMem
[191]hierarchicallyaggregatesuserinsightsfromepisodicmemory.Relatedly,RLPF[223]optimizesconcise,human-
readableusersummariesusingafeedbacklooptiedtodownstreamperformance,andCURIO[197]introducesan
intrinsicmotivationobjectivethatencouragesactiveinferenceoflatentusertypesduringmulti-turninteraction.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

8 • Y.Xuetal.
Response-based Modeling. Response-based modeling represents user preferences through how users evaluate
candidateoutputs,therebycapturingmorefine-grainedandcontext-sensitivenotionsofwhatconstitutesapreferred
response.Comparedwithpersona-basedapproaches,whichemphasizeholisticuserdescriptions,response-based
approachesfocusmoredirectlyonusersatisfactionwithmodelbehavior.Indownstreamuse,theserepresentations
are naturally suited to feedback-driven correction and refinement of personalized outputs. A common strategy
istofactorizeindividualpreferenceintoasharedrewardfeaturebasiswithuser-specificweights,enablingrapid
adaptationundersparseuserdata.RFM[10],PReF[168],andLoRe[12]followthisparadigmbyinferringuser-specific
coefficientsfromlimitedfeedback.Complementarily,somemethodsrepresentpreferencesinnaturallanguageto
improveinterpretabilityandcontrollability.Janus[82]organizespreferencedimensionshierarchicallyfromcoarse
categoriestofine-grainedvaluedescriptions,whilePLUS[125]learnstext-basedpreferencesummariesthatcondition
downstreamrewardmodelingforpersonalizedscoringandgeneration.
3.2 AgentRoleDefinition
Whileuserprofilemodelingfocusesonrepresentingtheuser,agentroledefinitiondetermineshowtheagentshould
positionitselfwithrespecttothatuser.Wedistinguishbetweenuser-substitutingagentdefinition,wheretheagentis
configuredtoactonbehalfoftheuser,anduser-adaptiveagentdefinition,wheretheagentdynamicallyadjustsitsrole
tobetterservearealuserduringinteraction.
User-substitutingAgentDefinition. User-substitutingroledefinitioniscommonindelegation-orientedandsimulation
scenarios,whereagentsareexpectedeithertoperformtasksfromtheuser’sperspectiveortogenerateuser-like
behaviorsanddialoguedata.Inthesecases,theagentisconfiguredtoactonbehalfoftheuserbyinstantiatingthe
user’sprofileasitsroleconfiguration.Theresultingrolepriorthenguidesplanningandexecutiontowardpersonalized
objectives[128].Thisformofroledefinitiondoesnotprimarilyrelyononlineadaptationtoarealuser,butremains
importantforuserproxyexecution,realistichuman-agentsimulation,andscalablegenerationofdiversesynthetic
users[39,85,205].
User-adaptiveAgentDefinition. Ininteractivepersonalizedsystems,PLAsadaptthemselvestobettersupportthe
userduringcollaboration.Here,theagentrolebecomesconditionalontheuserprofile,allowingtheagenttoadjustits
persona,tone,levelofautonomy,orinteractionstrategyaccordingtotheuser’sprofile.Thisformsatwo-wayadaptive
processinwhichuserunderstandinginformsroleconfiguration,andtheadaptedroleinturnaffectssubsequent
interaction. Representative methods realize user-adaptive role definition through either joint persona modeling
orprofile-conditionedpromptadaptation.LD-Agent[86]adoptsabidirectionaluser-agentmodelingframework
[238] with a tunable persona extractor and a long-term persona bank for both users and agents. PersonaAgent
[254],PersonaX[172],andRPP[115]insteadadapttheagentrolethroughuser-conditionedpromptsorprofiles:
PersonaAgentoptimizesuser-specificsystempromptsviatextuallossfeedback,PersonaXcombinesofflinemulti-
personaprofilingwithonlineprofileretrieval,andRPPgeneratespersonalizeddiscretepromptsfromhistoricaluser
informationandtaskguidance.
3.3 Discussion
RoleandChallenges. Profilemodelingprovidesthefoundationallayerofpersonalizationbydeterminingboth
howtheuserisrepresentedandhowtheagentisconfiguredinresponsetothatrepresentation.Theybridgeraw
user-relatedevidencewithdownstreampersonalizedmemory,planning,andaction.Atthesametime,theyface
severaltightlycoupledchallenges.Userprofilingmustfirstcopewithsparse,noisy,andinconsistentpreference
signals.Beyondsignalquality,aseparatechallengeisdeterminingwhichuser-relatedfeaturesaregenuinelyrelevant
fordownstreampersonalization.Inparallel,agentroledefinitionmustbalanceadaptabilitywithstabilityacrosstasks,
avoidingbothrigidroleassignmentsandundesirableroledrift.Finally,abroaderchallengeliesintherequirementof
effectivecouplingandbidirectionalalignmentbetweenuserprofilingandagentroleadaptation.
FutureDirections. Existinguserprofilingmethodsoftenproducerepresentationsthatareeitheroverlystaticor
narrowlytask-specific,whileagentrolesoftenlackcontrollabilityorprincipledadaptationdynamics.Moreover,
userprofilingandagentroledefinitionaretypicallydevelopedinisolation,withlimitedmechanismsformutual
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 9
adjustment.Promisingdirectionsthereforeincludelightweightandinterpretableprofilingmethodsthatremainrobust
undersparseornoisysignals,aswellasunifiedframeworksthatjointlymodelevolvinguserprofilesandstableyet
adaptiveagentroles.
4 Memory
Whileprofilemodelingcapturesrelativelystableandhigh-levelusercharacteristics,personalizedagentsalsorequire
mechanismsforretaininguser-relatedinformationacrossinteractions.Memoryprovidesthiscapabilitybyenabling
thesystemtostore,recall,andleveragepastexperiencetoimprovefuturebehavior[218].Memoryiscommonly
dividedintopersonalmemory,whichstoresuserinputsandinteractionhistories,andsystemmemory,whichrecords
intermediatereasoningstatesortask-executionartifacts[227].Thissurveyfocusesonpersonalmemory,asit
directlyshapeshowagentsadapttoindividualusers.
Personalmemorycanbeimplementedeitherasinternalmemory,whichembedsuser-relatedinformationwithinthe
LLM,orasexternalmemory,whichstoressuchinformationinanauxiliarysystem.Internalmemorymayberealized
through model parameters, key–value caches, or hidden states [129, 144, 207, 211, 231, 259]. Although compact
andparameter-efficient[212],internalmemoryislimitedbyconstrainedcapacity,difficultiesinupdatingstored
information,andfrequentrelianceonretraining,makingitlesssuitablefordynamicandlong-horizonpersonalization.
Bycontrast,externalmemoryismoreflexibleandtypicallyoperatesthroughretrieval-augmentedgeneration(RAG;
83)toincorporatestoreduserinformationintothecurrentcontext.
Externalpersonalmemorycanfurtherbeviewedatdifferenttemporalscales,includingshort-termmemory,which
retainsrecentconversationalcontext,andlong-termmemory,whichaccumulatesenduringuserinformationacross
sessions.Short-termmemorysupportsimmediateresponsesbutisconstrainedbycontextwindows,whereaslong-
termmemoryenablestheaccumulationoflong-tailpersonalinformationandcontinualadaptation[64],yetismore
vulnerabletoinformationoverloadandstalecontent.Asaresult,manypersonalizedagentsadopthybriddesigns
thatcombineboth.Intheremainderofthissection,however,wefocusonlong-termexternalpersonalmemory,
wherethestructureddesignofpersonalizedmemoryhasbeenmostextensivelystudied.Wediscussitfromtwo
perspectives:personalmemoryschemes,whichdeterminehowuser-relatedinformationisstoredandupdated,and
personalizedretrieval,whichdetermineshowstoredinformationisaccessedtosupportpersonalizedbehavior.
4.1 MemorySchemes
Memoryschemesdeterminehowuser-relatedinformationisorganized,stored,andupdatedovertime.Inlong-term
externalpersonalmemorysystems,thismainlyinvolvesthedesignofmemorystructureandupdatemechanism.
4.1.1 MemoryStructure. Memorystructuredetermineswhatinformationisstoredandhowitisrepresented,thereby
shapingthescalabilityandusefulnessofpersonalmemory.Earlyagentsystemsoftenstoredfulldialoguehistoriesor
executiontrajectoriesdirectly[104],butsuchrawstorageintroducedredundancyandmadeitdifficulttosurface
user-relevantinformation.Recentmethodsthereforetransforminteractionhistoriesintomorecompactandtask-
adaptiverepresentations[103,269].Basedonrepresentationformat,thesestructurescanbebroadlygroupedinto
textualmemoryandstructuredmemory.
TextualMemory. Textualmemorystoresuser-relatedinformationinnaturallanguageform,typicallybysummariz-
ingmulti-turninteractionsintoconciseandinterpretableunits.Becausesuchrepresentationspreserverichsemantics
andalignnaturallywiththeinput–outputformatofLLMs,textualmemoryhasbecomeacommonchoiceforperson-
alizedagentsacrossdiversetasks[260].Itsdesignmainlyinvolvestwokeychallenges:determiningthegranularity
ofmemoryunitsthroughappropriatesegmentation,andpreservinguser-relevantinformationaccuratelywithin
thoseunits.Earlyapproachesoftenreliedonrigidturn-levelorsession-levelsegmentation,whichcouldfragment
semanticallycoherentinteractionsandhinderretrieval.Recentworkthereforeexploresmoreflexible,topic-consistent
segmentationstrategies.Forexample,SeCom[136]andRMM[187]partitionconversationsintosemanticallycoherent
segments,whileNemori[126]furtherimprovessegmentationbydetectingepisodeboundariesandpreservingthe
integrityofuserintent.Onceappropriatememoryunitsareformed,asecondchallengeistopreserveuser-relevant
information faithfully and compactly. Many systems augment textual memory with auxiliary attributes such as
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

10 • Y.Xuetal.
timestamps,topiclabels,anduserpersonality[103,119,237].Forinstance,CAIM[219]augmentsmemoryentries
withtags,inductivethoughts,andtimestamps,whileMemInsight[154]extractsstructuredsemanticattributesfrom
dialogueforrichermemoryaugmentation.Morerecently,someworksdrawinspirationfromhumanmemorysystems
byintroducingmulti-levelorganizationsthatdistinguishsemanticandepisodicmemory[107,109,140].Forexample,
MIRIX[209]adoptsahierarchicallyorganizedmulti-componentmemoryarchitecture,andMem-𝛼 [213]combines
core,semantic,andepisodicmemorywithreinforcementlearningformemorymanagement.Overall,theseefforts
movetextualmemorytowardmorecoherentsegmentation,morefaithfulpreservationofuser-relevantcontent,and
bettersupportforlong-termpersonalization.
StructuredMemory. Structuredmemoryrepresentsinteractionhistoriesinpredefinedformatswithexplicitorga-
nizationalrelationships,makingstoredinformationeasiertomanipulatecomputationally.Comparedwithtextual
summaries,itintroducesstrongerinductivebiasesforscalableretrieval,multi-granularityreasoning,andfine-grained
personalization.Currentapproachescanbebroadlygroupedintovector-basedmemory,hierarchicaltreestructures,
andgraph-basedmemoryarchitectures.
Vector-basedmemoryencodeseachmemoryunitasanembeddingstoredinavectordatabase,enablingefficient
similaritysearchandfastretrievalofuser-relevantinformation.Owingtoitsefficiencyandflexibility,thisdesign
hasbecomeacommonpracticeinmemorymodules[22,133,230].However,vectormemoryaloneprovideslimited
interpretabilityanddoesnotexplicitlycapturerelationsamongmemoryitems,motivatingmorestructuredalternatives
orhybridsystemsthatcombinevectorswithexplicitorganizationalformats.Hierarchicaltreestructuresorganize
memory at multiple abstraction levels, where parent–child relations encode increasingly coarse summaries. For
example,RAPTOR[160]andMemTree[152]recursivelyclusterandsummarizetextintotrees,supportingretrievalat
bothfine-andcoarse-grainedlevels.Graph-basedarchitecturescapturericherrelationshipsbylinkingmemory
unitsthroughtypededgesthatencodetemporal,semantic,orrelationaldependencies[22,65,97].Somemethods
emphasizebehavioralcoherence.Forexample,MemWeaver[246]constructsanevent-levelbehaviorgraphinwhich
interaction events are connected by temporal and semantic edges, together with a context-aware random walk
mechanism.Otherdesignsinsteadintegratemulti-dimensionalsubgraphstomodelmorenuancedrelationsamong
memoryunits.AriGraph[5]combinessemanticknowledgewithepisodicobservationnodestosupportbothlong-
termaccumulationandtemporallygroundedrecall,whileZep[150]organizesmemoryintoatemporallyaware
multi-tier knowledge graph spanning episodic, semantic, and conceptual levels. While expressive, graph-based
memoryoftendependsoncostlyLLM-basedextractionandmaylosefine-grainedcontextduringgraphconstruction.
Lightweightvariantsthereforesimplifygraphdesignwhilepreservingcontextualinformation.SGMem[230]uses
sentence-levelgraphorganization,whereasLiCoMemory[57]adoptsalightweighthierarchicalindexinggraphwith
fullcontentstoredexternally.Overall,structuredmemoryaimstoprovidericherorganizationbyexplicitlymodeling
howuser-relatedinformationisorganized,connected,andabstractedacrossinteractions.
4.1.2 Update mechanism. The update mechanism determines how memory evolves as new interactions arrive,
ensuringthatstoredinformationremainsusefulovertime.Whenanewmemoryunitisobserved,thesystemmust
decidewhethertoadditasanewentry,mergeitwithexistingmemory,reviseoutdatedcontent,ordiscardirrelevant
information[34].Inexternalpersonalmemorysystems,updatesdifferbetweentextualmemory,wheresummary-level
contentisrewrittenorreorganized,andstructuredmemory,wherenodes,edges,andtheirrelationsaremodified.We
discussthesetwocasesseparately.
Textual memory stores interaction histories as natural-language segments or summaries. Updating therefore
concernshowtheseunitsaremerged,rewritten,orreorganizedasnewdialoguearrives.Existingapproachescanbe
broadlygroupedintosimilarity-drivenupdatesandinference-guidedupdates.
Similarity-drivenupdates. Thesemethodsupdatememorybycomparingnewcontentwithexistingentriesand
applyingmerge,revision,orreplacementoperationsbasedonsemanticsimilarityandauxiliarymetadata.Earlier
approaches, such as RMM [187] and CAIM [219], perform summary-level merging and refinement. Mem0 [22]
makesthisprocessmoreexplicitthroughADD,UPDATE,DELETE,andNOOPoperationsovercandidatememories,while
Memory-R1[241]furtherlearnstheupdatepolicywithreinforcementlearningacrossmulti-sessioninteractions.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 11
Inference-guidedupdates. Othersystemstreatmemoryupdatingasareasoningordecision-makingprocess,allowing
theagenttoincorporateimplicitpreferenceshiftsorcontextualdynamicsnotcapturedbysimilarityalone.Nemori
[126]exemplifiesthisthroughitsPredict–Calibratemechanism,achievingproactivelyevolvingmemorybasedongaps
betweenpredictedandactualuserresponses.PREMem[77]similarlyperformspre-storagereasoningacrosssessions
to analyze thematic evolution before inserting new content, enabling more consistent long-term topic tracking.
Thesemethodsprovidemoreadaptiveandself-correctingmemorydynamics,capturingbothshort-termchangesand
long-termshiftsinuserpreferences.
Structuredmemoryorganizesinformationintointerconnectedarchitectureswhereinsertinganewunitoften
requiresreorganizingitsrelatedcounterparts.Updatemechanismscanlikewisebegroupedintosimilarity-drivenand
reasoning-oragentic-drivenstrategies.
Similarity-drivenupdates. Thesemethodsupdatestructuredmemorybymatchingnewinformationtoexistingunits
throughsemanticsimilarityandthenapplyinglocalstructuralmodificationstopreservecoherence.Inhierarchical
treestructures,MemTree[152]traversesthetreebysemanticsimilarity,insertsnewnodesthroughsiblingattachment
orleafexpansion,andincrementallyupdatesancestorsummariestomaintainhierarchicalconsistency.Ingraph-based
memory,updatesaremorecomplexbecauseeachnodemayconnecttomultipleothers[57].Mem0𝑔[22]matchesnew
triplestoexistingnodes,addsmetadata-richedges,andusesanLLM-basedconflictresolvertodeactivateoutdated
relations.Similarly,Zep[150]updatesepisodicfactsthroughtimestamp-awarealignmentwhileadjustinginconsistent
edgesandhigher-levelclusters,andMemGAS[233]selectivelyreinforcescontextuallyrelevantcross-granularity
associationstomaintainlong-horizonpersonalization.
Reasoning-guidedupdates. Anemerginglineofworkusesexplicitreasoningordecision-makingtoguidememory
updates,movingbeyondsimilaritymatchingtowardmoreadaptiveupdatedynamics.A-mem[237]exemplifiesthis
directionbytreatingeachnewmemoryasastructurednotethattriggerssemanticlinkingandretroactiverefinement
ofhistoricalnotes,enablingaself-evolvingmemorygraph.Althoughnotdesignedspecificallyforpersonalization,
systemssuchasTRAIL[264]andAriGraph[5]furthersuggestthatreasoning-guidedgraphevolutioncansupport
morecoherentmemoryupdates.
4.2 PersonalizedRetrieval
Memoryretrievaldetermineswhichstoredinformationbecomesavailabletoanagentatinferencetimeandtherefore
directlyinfluencesthequalityandconsistencyofpersonalizedbehaviors.UnlikeconventionalRAGsystems,retrieval
forpersonalizedLLM-poweredagentsmustsimultaneouslysatisfythreerequirements:(1)contentrelevancetothe
currentquery,(2)structuralconsistencywiththeunderlyingmemoryorganization,and(3)personalalignmentwith
theuser’spreferences.Existingretrievalmethodsaddressthesechallengesthroughthreedominantmechanisms:
content-basedretrieval,structure-awareretrieval,andpolicy-guidedretrieval.
Content-basedretrieval. Content-basedretrievalselectsrelevantmemoryprimarilythroughsemanticorlexical
similaritybetweenthecurrentqueryandstoredinformation,typicallyusingdenseorsparseretrievers[59,68,153].
Retrievedcontentisthenincorporatedintotheagent’sprompttoimprovecontextualgrounding[77,209,237].This
mechanismcanalsooperateatmultiplelevelsofgranularity.Forexample,RAPTOR[160]andMemTree[152]retrieve
memoryacrossdifferentabstractionlevelsbasedprimarilyonquerysimilarity,evenwhenthestoredmemoryis
hierarchicallyorganized.Somemethodsfurtherrefineretrievalaftertheinitialsearch.Forinstance,Yuanetal.[247]
usesself-reflectiontoassesswhethertheretrievedcontentissufficientforresponsegenerationandrevisethequery
whennecessary.Whileeffectiveforsemanticmatching,content-basedretrievaldoesnotexplicitlymodelstructural
dependenciesamongmemoryitemsandmaythereforeoverlooklong-rangecontextualrelations.
Structure-awareretrieval. Structure-awareretrievalaccessesmemorybyexplicitlyexploitinggraph,hierarchy,or
episodicrelations,ratherthanrelyingoncontentsimilarityalone.Thesemethodsoftenoperatehierarchically,where
theretrievalofentities,topics,orrelationsguidessubsequentaccesstodetailedmemoryunits[47,65],sometimes
withgraph-basedtechniquessuchasPersonalizedPageRank(PPR;8).Forexample,AriGraph[5]retrievesrelational
tripletsbeforeretrievingrelevantepisodicmemories,whileZep[150]combinessemanticsearchwithgraph-structured
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

12 • Y.Xuetal.
signalssuchasepisodefrequencyandnodedistance.MoreadaptivevariantsincludeMemGAS[233],whichcombines
entropy-basedroutingwithPPRoveranassociationgraph,andAssoMem[252],whichperformsmulti-signalranking
overcluenodesandlinkedutterances.Bymodelingdependenciesamongmemoryunitsexplicitly,structure-aware
retrievalbettercaptureslong-rangeandimplicituserpreferences.
Policy-guidedretrieval. Policy-guidedretrievalreferstoretrievalstrategiesinwhichmemoryaccessiscontrolledby
user-ortask-conditioneddecisionpoliciesratherthanbystaticsimilaritymatchingalone.Suchapolicydetermines
howretrievalshouldproceed,includinghowqueriesareformed,whichretrievaltoolsareinvoked,andwhether
additional information should be acquired. One line of work focuses on pre-retrieval query transformation,
wherepersonalizedretrievalintentisconstructedbeforesearch.Forexample,PBR[257]generatesuser-stylepseudo
feedbackandcorpus-anchoredexpansionstoformapersonalizedqueryrepresentation,whilePersonaRAG[248]
adaptsdocumentselectionandrankingusingreal-timebehavioralsignals.Asecondlineofworkadoptspolicy-driven
strategyselection,learningtoinvokeorcombineheterogeneousretrievaltoolsaccordingtotaskneeds.UniMS-RAG
[200]formulatesretrievalasapolicy-learningproblemoverkeywordsearch,denseretrieval,andknowledge-graph
lookup,whilePersona-DB[180]employsapersona-awarepolicytocombineretrievalsfromtargetandcollaborator
usersforimprovedpersonalizationundersparsedata.Athirddirectionincorporatesschema-guidedinformation
completion,framingretrievalasastructuredinferenceprocess.OCG-Agent[171]decomposesnarrativequeriesinto
schemafields,retrievesrelevantinformationthroughmultipleroutes,anditerativelysupplementsmissingattributes
untiltheschemaiscompleted.Overall,policy-guidedretrievalshiftsretrievalfrompassivematchingtowardactive
decisionmaking,enablingmoreflexibleandpersonalizedinformationacquisition.
4.3 Discussion
RoleandChallenges. Personalmemorybridgesshort-terminteractioncontextwithlong-termpreferencemodeling,
fulfillingthreecloselyrelatedroles.Itprovidespersonalizedcontextualgroundingbypreservingfine-graineduser
detailsthatcannotbefullyencodedinstaticprofiles,supportspreferenceevolutionbyallowingtheagenttotrackhow
userpreferenceschangeacrosssessions,andenablespreference-conditionedgenerationbysupplyinguser-relevant
signalsatinferencetime.Atthesametime,theserolesmakepersonalmemorydifficulttodesigneffectively.User
preferencesevolveatdifferentrates,requiringmemorysystemstobalancerapidadaptationwiththepreservation
oflong-termtraits.Memorystoresmayalsoaccumulateredundancyorhallucinations,especiallywhenupdates
relyonLLM-basedsummarizationorrelationextraction,leadingtodegradedpersonalizationoverlonghorizons.
Moreover, retrieving content that is not only semantically relevant but also truly aligned with user preferences
remainsapersistentchallenge.Finally,personalmemoryraisesprivacyandtransparencyconcerns,highlightingthe
needforuser-controllableandprivacy-preservingmemorymechanisms.
Future Directions. These limitations point to several promising directions across the memory pipeline. One is
hybridmemoryarchitecturesthatcombinethesemanticrichnessoftextualrepresentationswiththeorganizational
clarityofstructuredformats.Anotherismoreprincipledanduser-controllableupdatemechanismsthatimprove
reliability, transparency, and long-term consistency. A third is retrieval strategies that better integrate personal
alignmentwithsemanticrelevance,sothatretrievedinformationisnotonlyrelatedtothequerybutalsotrulyuseful
forpersonalization.
5 Planning
InPLAs,planningisthestageatwhichuser-specificinformationistranslatedintoactionabledecisions.Whileprofile
modelingcaptureswhatisknownabouttheuserandmemorypreservesuser-relatedinformationovertime,planning
determineshowthesesignalsshapesubgoaldecomposition,strategyselection,andtrade-offresolutionduringtask
execution[110,181].Thus,itgoesbeyondgenerictask completionandinsteadseeksto optimizeuserutilityby
aligningdecisionswithindividualpreferences,constraints,andlatentintents[37,48,261].Weorganizeexisting
methodsintotwobroadparadigmsaccordingtohowusersignalsentertheplanningprocess:One-shotPlanning,in
whichpersonalizationisincorporatedasapriorduringplangeneration,andFeedback-drivenPlanning,inwhich
personalizationisprogressivelyrefinedthroughinteraction[183,255].
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 13
5.1 One-ShotPlanning
One-shotpersonalizedplanninggeneratesacompleteplanwithinasingleinferencepass,wheretheplanisrepresented
asastructureddecompositionofsubgoalsanddecisionsconditionedonuser-specificconstraintsandlatentintent.
Weanalyzethisparadigmalongtwocomplementaryaxes:usersignalgrounding,whichconcernshowusersignals
areincorporatedintotheplanningprocess,andinternalrefinement,whichconcernshowaninitialplanisinternally
improvedwithinthesameinferencepass.
5.1.1 UserSignalGrounding. One-shotplanningcangrounduser-specificinformationintwomainways.Onedirectly
conditionsplanningonexistinguserrepresentations,suchasexplicitprofiles,retrievedmemory,orcompressed
interactionhistory.Theotherinfersplanning-readyconstraintsorobjectivesfromheterogeneoususersignalsbefore
plangeneration.
ProfileandMemoryConditioning. Thesemethodsconditionone-shotplanningonexistinguserrepresentations,
suchasexplicitprofiles,retrievedmemory,orcompressedinteractionhistory,therebyhelpingmaintainconsistency
withbothlong-termpreferencesandrecentcontext[187,219].PRIME[256]integratesadual-memoryarchitecture
withaPersonalizedThoughtProcessthatexplicitlytraceshowpastexperiencesandstablebeliefsinfluencecurrent
decisions.Beforeplangeneration,PRIMEsynthesizesapersonalizedthoughttraceviaself-distillation,effectively
groundingplanningintheuser-specificcognitivecontext.PersonaAgent[254]adoptsaretrieval-augmentedpersona
mechanism,dynamicallyconstructingsystempromptsfromaunifiedmemorybanktomaintaincross-sessionplanning
consistency.Relatedworkinrecommendationanddialoguesystemssimilarlyshowsthatstructuredusermemory
retrievalsignificantlyimprovesalignmentandcoherenceinone-shotdecision-making[17,54].
PreferenceInduction. Complementarytodirectconditioning,thislineofworkconstructsaplanning-readyuser
statebyinferringlatentintentandtranslatingheterogeneoususersignalsintoexplicitconstraintsorsoftobjectives
thatguideplangeneration[48].Forinstance,ALIGNXPLORE[88]utilizesaUser-descriptionChain-of-Thought
frameworktosynthesizeacompact,semanticallygroundedpreferencedescriptionfromsparseinteractiontraces.
Insteadofretrievingrawlogs,themodelperformsextendedinductivereasoningtoformglobalpreferenceconstraints
thatconditiondownstreamplanning.Similarly,insequentialrecommendation,ReaRec[189]proposesaThink-Before-
Recommendparadigm,usingreasoningpositionembeddingstoinfertheuser’slatentintenttrajectorypriortoplan
generation.Inembodiedanddecision-makingcontexts,PbP[234]demonstratesthattreatinglearneduserpreferences
asintermediateabstractionssubstantiallyimprovesfew-shotpersonalizedplanningperformance.
5.1.2 InternalRefinement. Internalrefinementimprovesone-shotplanningbyfirstgeneratinganinitialplanand
theninternallycritiquingandrevisingitagainstauser-conditionedobjective.Generalself-refinementframeworks,
suchasReflexionandstructuredcritique-and-revisemethods,providereusablemechanismsforreflectivefeedback
andplanediting[44,174],whilerecenttest-time-computereasoningmodelsmakedeeperwithin-passself-correction
increasinglypractical[46,121].Representativesystemsinstantiatethisparadigminseveraldomains.Inpersonalized
travelplanning,TravelPlanner++[176]andPTS[165]iterativelyrefineintermediateitinerariesunderimplicitlong-
horizonuserpreferences.PREFINE[195]constructsapseudo-usercriticanduser-specificrubricsfrominteraction
historytocritiqueandrevisecandidateplans.Inembodiedcommandexecution,IoTGPT[245]performsself-correction
bytestingintermediatecommandsequencesinasimulatedenvironmentbeforedeployment.
5.2 Feedback-DrivenPlanning
Feedback-drivenplanningtreatsaninitialplanasaprovisionalhypothesistoberefinedthroughinteraction.Itis
motivatedbythefactthatuserintentisoftenunderspecified,evolving,oronlypartiallyobservable[108,255].Rather
thancommittingtoafixedplaninasinglepass,thesesystemsiterativelyupdateplanstoconvergetowardamore
personalizedsolution[183,202].Weorganizethisparadigmaccordingtothesourceoffeedbackandhowitupdates
theplan,includingclarificationseeking,userrevision,andnon-userfeedback.
Clarification Seeking. A central challenge in feedback-driven personalized planning lies in deciding when to
askforadditionalinformation:excessiveclarificationincreasesuserburden,whileprematurecommitmentrisks
misinterpretinguser-specificconstraintsorlatentintent.Priorstudiesindicatethatuserrequestsinplanningtasksare
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

14 • Y.Xuetal.
frequentlyunderspecifiedorambiguous[108],motivatingapproachesthattreatclarificationasdecision-makingunder
uncertainty.Forinstance,SAGE-Agent[183]formulatesselectivequestioningasaPOMDPandissuesclarification
queriesonlywhentheexpectedvalueofinformationoutweighsinteractioncost.Similarly,ECLAIR[124]focuseson
detectingmissingargumentsorambiguousentitiesinuserinstructionsandtriggerstargetedfollow-upquestions
beforecommittingtoaplan.Additionally,Ask-before-Planstyleframeworks[255]explicitlydecoupleclarification
fromplansynthesis,showingthatresolvingkeyuncertaintiesupfrontimprovesrobustnessanddownstreamplan
quality.
UserRevision. Usereditsprovideahigh-fidelitypersonalizationsignalthatcanupdateuser-conditionedobjectives,
constraints, and preferences for subsequent planning and generation. Gao et al. [37] shows that learning latent
preferences from historical edits can reduce future edit effort and improve user-specific alignment in subjective
settings.Buildingonthismixed-initiativeview,AIPOM[74]representsplansaseditablestructures,enablingusers
toreviseintermediateplanswhiletheagentupdatesconstraintsandprioritiesaccordingly.Similarrevisionloops
appearindomainsystemssuchasDango[18],whichsupportsiterativecorrectionofagent-produceddata-processing
workflows,andPlanFitting[173],whichrefinespersonalizedexerciseplansthroughconversationalrevisions.Similar
revisionpatternsarealsoincreasinglyvisibleindeployedcodingassistants[6,41].
Non-userFeedback. Beyonddirectuserinput,planscanalsoberefinedthroughnon-usersignalsthatimprove
feasibilityandpreferencesatisfactionwithoutrepeatedlyincreasinginteractionburden.Onesourceisagent-mediated
feedback.Forexample,VAIAGE[101]employsspecializedagentstonegotiateroutefeasibilityandrecommendations
underuserpreferences,whileCollab-Rec[9]supportsmulti-stakeholderplanningthroughexplicituser-advocacy
mechanisms.Anothersourceisenvironment-mediatedfeedback,whereintermediateoutcomesaresimulatedand
usedtotriggerre-planning.Forinstance,SceneWeaver[244]followsaReason–Act–Reflectloopandrevisesplans
whenintermediaterenderingresultsrevealviolations.
5.3 Discussion
RoleandChallenges. PlanningservestwocomplementaryrolesinPLAs.First,itoperationalizespersonalizationby
translatinguserintentinferenceandpreferencemodelingintodownstreamdecisions,instantiatinguser-contingent
objectives,constraints,andtrade-offsthatgovernplangeneration[17].Second,especiallyinfeedback-drivenset-
tings[74],planningfunctionsasaclosed-loopoptimizationprocessthatalternatesbetweenelicitinginformative
feedbackandrevisingtheplan,enablingtheagenttoprogressivelyuncoveruserintentandmovetowardstronger
personalization.However,theserolesintroduceseveralchallengesatthesametime.Userintentandpreferences
areoftenonlypartiallyobservedandmayevolveovertime[108,183],makingitdifficulttodecidewhentoinfer,
elicit,andcommit.Moreover,personalizedutilityisinherentlymulti-objective[165],requiringarbitrationamong
competingconstraintsandidiosyncratictrade-offs.Ininteractivesettings,refinementmustalsoremaincontrollable
andconvergent,limitinguserburdenwhileavoidingunstablerevisions.Thesedifficultiesarereflectedinthetrade-off
betweenexistingparadigms:one-shotplanningofferslow-latencyandcoherentdecisionsbyinternalizingusersignals
aspriors,butcanbebrittleundersparseorshiftingsignals,whereasfeedback-drivenplanningimprovesalignment
throughiterativeelicitationandrevisionatthecostofadditionallatencyandusereffort[101].
FutureDirections. Promisingdirectionsincludeuncertainty-awareplanningworkflowsthatadaptivelyallocate
internalcomputationandrevisioneffortaccordingtoconfidenceininferredpreferencesandtaskstakes[121],thereby
combiningtheefficiencyofone-shotplanningwiththealignmentbenefitsoffeedback-drivenrefinement.Another
directionistolearnuser-conditionedplanningpatternsatbothinter-andintra-userlevels[146],capturingsystematic
differencesindecompositionstyleandtrade-offresolutionwhilemodelingtheirstabilityanddriftovertime.More
broadly,importantbutstillunder-exploreddirectionsincluderobustnesstovariationinuserspecification[183]and
privacy-preservingplanning[229]thatsupportslong-horizonuserconditioningwithoutexposingrawpersonaldata.
6 ActionExecution
ActionexecutionisthestageatwhichaPLArealizesdecisionsthroughconcreteoperationsinexternalenvironments
andreceivesfeedbackfromexecutionoutcomes[73,167].Unlikepurelytask-centricexecution,personalizedexecution
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 15
mustgroundactionsinuser-specificconstraintsandpreferences,whileremainingadaptivewhentoolsorenvironments
produceunexpectedoutcomes.Weorganizepersonalizedactionexecutionintotwostages:apre-actionstagethat
selectsandparameterizesactionsunderuser-conditionedconstraints,andapost-actionstagethatleveragesexecution
signalsforrecoveryandpreference-consistentoutcomerealization.
6.1 Pre-actionStage
Thepre-actionstagefocusesonuser-conditionedactiondecisionandgrounding.Ittranslatesaselectedintentor
planstepintoexecutabletoolcallsorenvironmentoperationsunderuser-specificconstraints.Wefurtherdecompose
thisstageintoactionpolicy,whichselectsamongfunctionallyvalidexecutionoptionsforagivenstep,andaction
grounding,whichinstantiatestheselectedactionwithuser-specificargumentsandrealizations.
6.1.1 Action Policy. At this level, personalization manifests as a bias over functionally valid execution choices,
spanningbothtoolutilizationandhigher-levelactionselection.PEToolLLaMA[235]formalizespersonalizedtool
learningfrominteractionhistoryandtrainsmodelstoimprovepreference-awaretoolselection.Inweb-agentsettings,
PUMA[14]adoptsasimilarpreference-awarelearningstrategy,whileToolSpectrum[20]furtherconditionstool
useonbothuserprofilesandenvironmentalcontext.Beyondtoolinvocation,ValuePilot[111]studiesaction-level
decisionmakingunderuservalues,showingthatexecutionchoicescanbeguidedbyindividualizedvaluepreferences.
Incasesofambiguity,actionpolicymayalsoinvolveproactiveclarification.Forexample,ColorAgent[90]learnsto
engagetheuserwhenintentionsorinstructionsareincompletebeforecommittingtoanexecutionchoice.
6.1.2 ActionGrounding. Actiongroundingoperationalizesaselectedactionbyinstantiatingitintoexecutabletool
callswithuser-conditionedconstraintsandparameters[14,20].Whilemanyrequestscanbegroundedbydirectly
applyinguser-specificsettings,personalizationbecomesmorechallengingincornercases.Afrequentgrounding-time
failure mode is infeasibility, where the instantiated query becomes unsatisfiable under the imposed constraints.
AWARE-US[80]framesthisasapreference-awarequeryrepairproblem,arguingthatagentsshouldrestorefeasibility
byrelaxingtheleastpreferredconstraintstotheuserratherthanapplyingdefaultheuristics.Anotherrecurringissue
istheomissionofessentialtoolarguments.Huangetal.[55]studyhowagentsinferunspecifiedargumentsfromuser
profiles,reducingexecutionfrictionwhilemaintainingalignmentwithuserintent.
6.2 Post-actionStage
Thepost-actionstageclosestheloopafteranactionisexecuted.Givenexecutionresult,theagentevaluateswhetherthe
outcomesatisfiesuser-conditionedobjectives,appliescorrectiveadjustmentswhenmismatchesarise(execution-time
correction),andproducesfinaloutputsthatconformtouserpreferencesandqualitycriteria(outcomerealization).
6.2.1 Execution-TimeCorrection. Afailedexecutioncommonlyproducesfeedbacksignals,whichcanbeleveraged
foradjustingbehaviorwithoutre-planningfromscratch.Explicitstudiesonpreference-awarerecoveryinPLAs
remainlimited.Nevertheless,adjacentworksuggestsusefulmechanismsforthisstage.Forexample,researchon
mitigatingtooloveruseunderdiminishingreturns[143]andstructuredreflectionovertool-interactionfailures[179]
providesbuildingblocksforfuturepersonalizedrecoverystrategies.
6.2.2 OutcomeRealization. Evenwhenmultipleexecutionoutcomesarefunctionallyvalid,usersatisfactiondepends
onhowfinalresultsarepresentedinaccordancewithindividualpreferences.Onecommonmechanismispersonalized
re-ranking,whichtransformscandidateresultsintooutputsthatbetterreflectuser-specificutility[138].Methodssuch
asPEARandMIRexplicitlymodeluserpreferencefeaturestogetherwithcross-itemdependencies,producingmore
faithfulfinalrankings[96,232].Personalizationmayalsogovernwhichoutcomesareretainedordiscarded:WARPP
[117]adjustsworkflowbranchesatruntimebasedonuserattributes,reducingirrelevantorerroneousoutcomes
withoutre-planningthefullprocess.Finally,outcomerealizationcanextendbeyondselectingamongexistingresults
toproactivelyaugmentingthem.ETAPP[50]treatsproactivityasapersonalizationsignal,evaluatingwhetheragents
canproposeadditionalactionsorsuggestionstobettersatisfyuserneeds.
RoleandChallenges. Actionexecutionisthestageatwhichpersonalizeddecisionsaretranslatedintoconcrete
operationsandexternaloutcomesinPLAs[23,148].Assuch,itbridgeshigh-levelreasoningwithobservablebehavior,
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

16 • Y.Xuetal.
determiningwhetherpersonalizationisactuallyrealizedratherthanremainingatthelevelofinternalreasoning.This
stageisespeciallyimportantbecauseuserexperiencedependsnotonlyonwhattheagentdecides,butalsoonhow
thosedecisionsareinstantiatedanddelivered.Atthesametime,personalizedactionexecutionremainschallenging
forseveralreasons.Executioncontextsarehighlyheterogeneousacrosstools,environments,anddomains,makingit
difficulttodesigngeneralmechanismsthatconsistentlyrespectindividualpreferences.Moreover,execution-time
personalizationsignalsareoftensubtle,requiringabstractpreferencestobetranslatedintoconcreteparametersrather
thanexplicitinstructions.Finally,executionfeedbackmayrevealambiguityorbrittlenessinhowuserpreferences
wereinterpretedupstream,requiringcarefulhandlingand,insomecases,coordinationwithplanningorpreference-
modelingcomponentstoavoidcascadingerrors.
FutureDirections. Researchonpersonalizedactionexecutionremainsrelativelylimited,leavingseveralpromising
directionsopen.Oneisthedevelopmentofpersonalization-awareexecutionprimitivesandtoolsthataccountnot
onlyfortaskcorrectnessbutalsofornon-functionaluserpreferences.Anotherislearningpreference-conditioned
executionpoliciesthatgeneralizeacrosstoolsandenvironments,enablingagentstoreusepersonalizationsignals
moreeffectively.Itisalsoimportanttoimprovehowagentshandlevagueormissingarguments,localizeexecution
failures,andaggregateoutcomesinwaysthatreflectuserprioritiesratherthandefaultheuristics.Morebroadly,this
stagewouldbenefitfromexecution-levelevaluationprotocolsthatmovebeyondtasksuccesstoassesspreference
adherence,consistency,andusersatisfaction.
7 Evaluation
Evaluatingpersonalizedagentsrequiresgoingbeyondconventionaltask-centricassessment,becausetheobjective
is not only task correctness but also long-horizon, user-specific utility. This challenge stems from the fact that
humanpreferencesareoftenimplicit,context-dependent,andevolvingthroughinteraction,makingpersonalization
difficulttomeasurewithasingleobjectivecriterion.Asaresult,evaluationshouldcapturenotonlywhetheran
agentcompletesatask,butalsowhetheritalignswithanindividualuser’spreferences,expectations,andexperience
overtime.Inthissection,weprovideasystematicoverviewofevaluationforpersonalizedLLM-poweredagents.
AssummarizedinFigure5,weorganizethediscussionintothreelayers:evaluationgoalsandmetricdimensions,
assessmentparadigms,andrepresentativebenchmarkfamilies.
Evaluation Goals Assessment Paradigms Benchmarks
Effectiveness Restrictive Interactive Alignment Benchmarks
Automatic Scoring -Preference Discover
-Output-level Alignment
Risk Adaptivity Rule-based Constraint -Component-probing
Personalized Checking
Agent
LLM-as-a-judge User-Substitution Benchmarks
-Textual and Dialogue
Robustness Generalization
LLM-based Evaluator -Planning and Tool-use
-Embodied and Spatial
Flexible
Fig.5. OverviewofevaluationforpersonalizedLLM-poweredagents.Evaluationisorganizedalongthreelayers:(1)evaluation
goalsandmetricdimensions,includingeffectiveness,adaptivity,generalization,robustness,andrisk;(2)assessmentparadigms,
suchasautomaticscoring,rule-basedchecking,learnedevaluators,andLLM-as-a-judge;and(3)representativebenchmark
families,includinginteractivealignmentanduser-substitutionsettings.
7.1 EvaluationGoalsandMetrics
Arigorousevaluationframeworkforpersonalizedagentsmustreflectthemulti-facetednatureofpersonalization
quality.Beyondobjectivetasksuccess,anagentshouldalignwithindividualpreferences,remaincoherentacross
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 17
contexts and over time, adapt when preferences are revealed or revised, and operate within safety and privacy
constraints. Motivated by these requirements, we organize evaluation metrics for personalized agents into five
complementarydimensions:Effectiveness,Adaptivity,Generalization,Robustness,andRisk,asillustratedin
Table2.Thesemetricdimensionsdonotapplyuniformlyacrossallcapabilities,butprovideastructuredbasisfor
comparingpersonalizedagentsacrosstasks,preferencesources,andassessmentparadigms.
Table2. EvaluationmetricsforpersonalizedLLM-poweredagents.
Goal Metric Description
Measureswhethertheagentcancorrectlydiscoveruserpreferences
DiscoveryAccuracy[63,92]
orintentsfromtheinteraction.
Measurestheabilityofthemodeltoincorporateuser-specificknowl-
KnowledgeIntegrationScore[7,199]
edgeorpersonainformationintogeneratedoutputs.
Measuresthealignmentbetweentheagent’soutputanduserpref-
PreferenceAlignment[229,262]
erencesorstatedconstraints.
Measureswhethermulti-stepplansortool-usesequencesconform
Effectiveness Preference-AwarePlanningAccuracy[234,235]
toindividualuserpreferences.
Comparespersonalizedoutputsagainstanon-personalizedbaseline
PreferenceLift[50,92,225]
onthesameprompt,reportingtheliftinpreferencescore.
Measurestheconsistencyoftheagent’stextualstyleandexpressed
ConsistencyScore[123]
personalityacrossthewholeconversation.
Measuresthedegreetowhichtheresponseshowsunderstanding
EmotionalEmpathy[229]
andcompassionfortheuser’semotionalstate.
Assessestheratioofsuccessfulpersonalizationafterreceivingnew
AdaptationSuccessRate[62,164]
preferencesignals.
Measures the ability to revise, overwrite, or remove previously
SelectiveForgetting[52]
storedinformationofuserswhenfacedwithcontradictoryevidence.
Measurestheefficiencyofadapting,suchasnumberofturns,clari-
Adaptivity InteractionEfficiency[92]
ficationquestions,oreditsneededtosatisfyuserexpectations.
Measurestheabilityoftheagenttoproactivelyidentifyuserneeds
Proactivity[50] andofferingextrasuggestionsoractionstoenhanceusersatisfac-
tion.
Measurestheabilityoftheagenttogeneralizeuserpreferencesto
Generalization Out-of-DomainPerformance[62]
otherscenariosortaskswithoutexplicitinstruction.
Measurestheaccuracyoftheagent’sactionwhensomeinformation
AccuracyunderAmbiguity[55,135]
Robustness ismissingorambiguous.
Evaluatesthemodel’sabilitytoidentifyandrejectincorrectinfor-
MisinformedConditionPerformance[53]
mationwhentheuserismisinformed.
Measureswhethertheagentcanmakesafedecisionsbasedondif-
SafetyRate[226]
ferentuserprofiles.
Measureswhethertheagentcanrecognizeandrespondappropri-
Risk RiskSensitivity[229]
atelytopotentialrisksintheuser’scontext.
Measuresthepercentageofconversationsinwhichtheagentdis-
PrivacyLeakageRate[123,266] closesprivateinformationinappropriatelyintasksrelatedtousers’
privacyinformation.
Over-SecrecyRate[123] Measuresthefailuresofutilitythatarisefromexcessivecaution.
Effectiveness. Effectivenesscaptureswhetherapersonalizedagentcanproduceuser-contingentutilityratherthan
merelygenerichelpfulness.Itcoversatleastthreeaspects:whethertheagentcaninferwhattheuserwantsfrom
partialinteractiontracesorcontextualsignals;whetheritcancorrectlyincorporateuser-specificinformationinto
planningandgeneration;andwhetherthefinalresponseoractionactuallysatisfiesexplicitconstraintsandimplicit
preferences.MetricssuchasDiscoveryAccuracy[63],KnowledgeIntegrationScore[7,199],PreferenceAlignment
[229,262],andPreference-AwarePlanningAccuracy[234,235]targettheseaspectsfromdifferentangles.Beyond
absolutealignment,PreferenceLift[50,92,225]measuresgainsoveranon-personalizedbaselineunderthesame
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

18 • Y.Xuetal.
prompt.Inmulti-turnsettings,ConsistencyScore[123]evaluatesstabilityofpersonaandvaluesovertime,while
EmotionalEmpathy[229]captureswhetherresponsesremainaffect-appropriateandsupportive.
Adaptivity. Adaptivityevaluateswhetherapersonalizedagentcanupdateitsbehaviorasnewevidenceabout
userpreferencesbecomesavailable,whilepreservingcontinuityandminimizinguserburden.AdaptationSuccess
Rate[62,164]measureswhethertheagentimprovespersonalizationafterreceivingexplicitfeedback,additional
constraints, or new user context. Because preferences may evolve or even contradict earlier evidence, Selective
Forgetting[52]isequallyimportantforassessingwhetheroutdatedmemorycanberevised,overwritten,orremoved
appropriately.InteractionEfficiency[92]capturesthecostofadaptation,suchasthenumberofturns,clarifications,
oreditsrequiredbeforetheuseracceptstheresult.Proactivity[50]complementsthesemetricsbymeasuringwhether
theagentcananticipateneedsandofferhelpfulnextstepsattherighttimewithoutcreatingunnecessaryinterruption
orirrelevantsuggestions.
Generalization. Generalizationcaptureswhetherpersonalizationtransfersbeyondthecontextsinwhichitwas
originallylearned.Inpractice,ausefulpersonalizedagentshouldnotrequiretheusertorestatepreferencesforevery
newdomain,task,orsituation.Out-of-DomainPerformance[62]thereforemeasureswhetherpreferencesacquired
inonesettingcanbeappliedappropriatelyinothers.Thisdimensionisespeciallyimportantforgeneral-purpose
agentsthatareexpectedtosupportdiversedailyactivities,wherepersonalizationmustremainreusableratherthan
narrowlytiedtoasingletaskcontext.
Robustness. Personalizedagentsoperateundernoisy,incomplete,andsometimesmisleadingpreferenceevidence,so
evaluationmustmeasurereliabilityunderstressratherthanonlyaverage-casealignment.Tworobustnesspressures
areespeciallyimportant.First,userpreferencesareoftenunderspecified,partiallyobserved,orexpressedindirectly.
AccuracyunderAmbiguity[55,135]thereforeevaluateswhethertheagentcanmakereasonableinferences,ask
targetedclarificationquestions,andavoidoverconfidentassumptionswhenkeysignalsaremissing.Second,user
inputsmaybeincorrectorbasedonmisconceptions.MisinformedConditionPerformance[53]measureswhetherthe
agentcanidentifyflawedpremises,providecorrectiveguidance,andstillpreserveapersonalizedinteractionstyle.
Risk. Riskmetricsquantifysafety,privacy,andotherdownsideconstraintsthatareinseparablefrompersonalization.
SafetyRate[226]measureswhethertheagentremainssafeacrossheterogeneoususerprofiles,includingcaseswhere
userpreferencesmayconflictwithpoliciesorwhererequestsinvolveriskyactions.RiskSensitivity[229]evaluates
whethertheagentcanrecognizecontextualhazardsandcalibrateitsadviceappropriately,forexample,byproviding
warnings,suggestingsaferalternatives,orencouragingprofessionalhelpwhenneeded.Becausepersonalization
reliesonuser-specificinformation,PrivacyLeakageRate[123,266]measureswhethertheagentdisclosesprivatedata
indisallowedways,especiallyunderadversarialorindirectprompts.Conversely,Over-SecrecyRate[123]captures
utilitylossfromexcessivecaution,wheretheagentwithholdsbenignbuthelpfulinformationdespitealegitimate
request.Thesemetricsreflectthecentralchallengeofmaximizinguserutilitywhilerespectingriskconstraints.
7.2 AssessmentParadigms
Themetricdimensionsabovecanbeoperationalizedthroughdifferentassessmentparadigms,dependingonwhether
thetargetcriterionisobjectivelyverifiableorinherentlyuser-contingent.Wegroupmainstreamparadigmsinto
fourfamilies.(1)Automaticscoringapplieswhenground-truthlabelsorreferenceanswersareavailable.Typical
examplesincludeaccuracyandprecision/recall/F1forclassification,aswellasoverlap-basedmetricssuchasBLEU
[137]andROUGE[100]forgeneration.(2)Rule-basedconstraintcheckingevaluateswhetheroutputssatisfy
explicitandverifiablerequirements,suchasincludingrequiredattributes,avoidingforbiddenones,orrespecting
structuredpreferenceconstraints.Thisparadigmisespeciallyusefulfordelegation-styletasksinwhichcompliance
canbedeterministicallyvalidated.(3)LearnedLLM-basedevaluators(LLM-E)traindedicatedevaluationmodels
toassessspecificpreferencedimensions,oftenprovidingmorestableandfine-graineddiagnosticfeedbackatthe
costofreducedgenerality[198].(4)LLM-as-a-judge(LLM-J)usesageneral-purposeLLMastheevaluatorfor
user-contingentcriteriasuchaspreferencealignment,tone,andsatisfaction.Inthissetting,thejudgeistypically
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 19
conditionedonauserprofileorpreferencedescriptionandaskedtoscoreorrankcandidateoutputs[267].Toimprove
reliability,LLM-Jprotocolsoftenadoptpairwisecomparison,calibratedrubrics,andmulti-judgeaggregation.
7.3 Benchmark
Building on the above metric taxonomy, we summarize representative benchmarks for personalized agents and
organizethemintotwobroadfamilies.InteractiveAlignmentBenchmarksevaluateanagent’sabilitytoelicit,negotiate,
andrefineuserpreferencesthroughmulti-turninteraction,wheretheuserremainsanindispensablepartoftheloop.
Incontrast,User-SubstitutionBenchmarksevaluatewhetheranagentcanstandinfortheuserbysimulatingtheir
preferencesorpersonatoproduceuser-consistentresponsesordecisionswithoutfurtheruserinput.Mainstream
benchmarksaresummarizedinTable31.
7.3.1 InteractiveAlignmentBenchmarks.
PreferenceDiscoveryBenchmarks. Acorechallengeininteractivealignmentispreferencediscovery,wherethe
agentmustrecognize,infer,anditerativelyrefineuserintentsandpreferencesfromheterogeneoussignals,ranging
fromexplicitinstructionstoimplicitfeedbackandcontextualcues[193].Inthiscategory,IndieValueCatalog[63]
curatesvalue-expressingstatementsfromdiverseindividualsandevaluateswhethermodelscaninferindividualized
valuejudgments,highlightinglimitationsincapturingfine-grainedpersonalvalues.PersonaBench[186]constructs
syntheticyetrealisticpersonalprofilesandassociatedartifactstotestwhetheragentscanextractandreasonover
user-specificinformation.PrefDisco[92]proposesameta-evaluationframeworkthatemphasizesinteractiveelicitation
efficiency,measuringwhetheranagentcanproactivelyaskinformativequestionsforauser-alignedsolutionwith
minimalinteractionturns.
Output-levelAlignmentBenchmarks. Thiscategoryevaluatespersonalizationinanend-to-endmanner,focusingon
whethertheagent’sfinaloutputssatisfyatargetuser’spreferencesandconstraintsinrealisticinteractivesettings.
Forconversation-centeredpersonalization,benchmarkssuchasALOE[225]andPrefEval[262]testwhetheragents
caninfer,retain,andconsistentlyfollowuserpreferencesacrossmulti-turndialogues.Beyondconversationaltasks,
PDR-Bench[99]evaluateswhetheragentscanincorporateuserprofilesintoresearchworkflowsandproduceoutputs
thatarepracticallyusefulfortheenduser.Forrecommendation,AgentRecBench[164]andRecBench+[53]assess
whetheragentscangeneratepreference-conditionedrecommendationsandadapttouserfeedback.Moregenerally,
PersonaLens[265]targetsmulti-scenario,task-orientedassistantsandevaluateswhetherpersonalizationremains
coherentacrossdiversedomainsanduserintents.
Component-probingBenchmarks. Complementarytotheabove,component-probingbenchmarksprovidecontrolled
testbedsthatisolatespecificpersonalizationcapabilities,enablingdiagnosticanalysisofwhenandhowanagent
leveragesuserinformation.PersonaFeedback[190]pairspredefinedpersonaswithqueriesandasksthemodelto
selectpersona-consistentresponses,offeringadirectprobeofpreference-conditionedalignment.Amajorsub-line
focusesonpersonalizedmemory,includingLongMemEval[222],LoCoMo[114],PerLTQA[30],MemoryAgentBench
[52],ConvoMem[135],andPAL-Bench[56],whichtestwhetheragentscanorganize,retrieve,andapplyuser-specific
memoriesunderlongconversationsorincrementalpreferencerevelation.Forpersonalizedtooluse,ETAPP[50]
andPTBench[55]evaluatewhetheragentstailortool-invocationstrategiestouserneeds,includingproactivityand
handlingmissingorambiguousinformation.Somebenchmarksexplicitlytargetadaptivityovertime;forexample,
PersonaMem[61,62]assesswhetheranagentcantrackevolvingtraitsandpreferences,reviseoutdatedbeliefs,and
generalizethemtonewscenarios.Finally,severalbenchmarksdiagnoseuser-specificrisk,suchasPSG-Agent[226]
andPENGUIN[229]thatevaluateprofile-contingentsafetyconsiderationsforLLM-basedagents,whilePrivacyBench
[123]andAgentDam[266]testprivacycomplianceforagentswhenhandlingsensitiveuserinformation.
7.3.2 User-SubstitutionBenchmarks.
TextualandDialogueBenchmarks. Textualanddialoguepersonalizationbenchmarksfocusonevaluatinghow
modelsgeneratecontentthatalignswithindividualuserpreferences,styles,andcontextualknowledge.Forinstance,
1Somebenchmarkscanpartiallyspanbothfamilies,andweplacetheminthemajorcategorytoavoidduplication.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

20 • Y.Xuetal.
long-formgenerationtasks,asinLaMP[156]andLongLaMP[79],testwhethermodelscanadaptoutputstoevolving
userinterestsovertime,whilePEFT-U[26]reformulatesclassificationproblemsintoannotator-specificinstancesto
measureuser-conditionedgenerationcapabilities.Benchmarksthatleverageretrievalorknowledgegraphs,such
asPGraphRAG[7],furtherexamineperformanceinsparseorcold-startscenarios.Beyondsingle-turngeneration,
multi-turn conversational benchmarks, including PersonaConvBench [89], PER-CHAT [228], LaMP-QA [157],
DPL[147],REGEN[161],andKBP[199]—assesswhethermodelsmaintaincoherence,adapttoauser’sconversational
style,andintegratepersonalizedknowledgeconsistentlyacrossdialogue.PRISM[78]targetsmorecomplexscenarios
whereuservaluesvaryculturallyorcontextually,evaluatingthereproductionofindividualizedsubjectivechoices.
PlanningandTool-UseBenchmarks. Benchmarksinplanningandtool-useexaminewhetherpersonalizedagents
canlearnandapplyuserpreferencestoperformsequentialormulti-steptasks.Preference-basedPlanning(PBP)[234]
simulateseverydayactivitiesacrossdiverseenvironmentstoevaluatepreference-drivenplanning,whilePETool-
Bench[235]specificallymeasurestheagent’sabilitytoselectandusetoolsaccordingtoindividualuserpreferences.
FamilyTool[210]extendsthisfocustocomplextool-basedworkflows,emphasizingtheintegrationofuser-specific
needs.Broadermulti-domainplanningbenchmarks,includingTravelPlanner++[176],TripTailor[203],TripCraft[16],
COMPASS[145],TripTide[71],andPersonalTravelSolver(PTS)[165],assesstasksrangingfromadaptiveitinerary
generationtodisruptionhandling,testingwhetheragentscaninterpretexplicitorinferredpreferencesandconstruct
coherent,user-alignedplans.
EmbodiedandSpatialBenchmarks. Embodiedandspatialbenchmarksinvestigatewhetheragentscannavigate,
manipulateobjects,andgroundactionsinphysicalorsimulatedspacesaccordingtouserpreferences.Memory-guided
interactiontasks,suchasMEMENTO[81],assesstheagent’sabilitytorecalluser-specificcues,whilePersONAL[270]
focusesonpersonalizednavigationandobjectgroundinginphotorealistichomeenvironments.PersonalizedInstance-
basedNavigation(PIN)benchmark[11]addsfurthercomplexitybyrequiringagentstolocateuser-specifictarget
objectsamongdistractorsin3Dscenes,emphasizingindividualizednavigationstrategies.
Table3. SummaryofPersonalizedBenchmark.
Benchmark Scale Task Pref. Goal Eval. Metrics
InteractiveAlignmentBenchmarks
IndieValueCatalog[63] 800 Human Inferred Effectiveness Auto. Accuracy
Value
PersonaBench[186] 582 General Inferred Effectiveness Auto. Recall,F1
PrefDisco[92] 10,000 General Interactive Effectiveness, Auto., DiscoveryAccuracy,PreferenceAlignment,
Adaptivity Rule- InteractionEfficiency,Correctness
based
PersonalLLM[225] 1000 General Given, Effectiveness LLM-J, PersonalizedReward
Inferred LLM-E
ALOE[225] 100 General Inferred Effectiveness LLM-J AlignmentLevel,ImprovementRate
PrefEval[262] 3,000 General Given, Effectiveness Auto., Accuracy,PersonalizedRate
Inferred Rule-
based,
LLM-J
AgentRecBench[164] 1,500 Recomm. Inferred Effectiveness, Auto. HitRate@N
Adaptivity
RecBench+[53] 34,494 Recomm. Given, Effectiveness, Auto. Precision,Recall,ConditionMatchRate,Fail
Inferred Robustness toRecommend
PDR-Bench[99] 250 Deep Given Effectiveness LLM-J PersonalizationAlignment,ContentQuality,
Research FactualReliability
PersonaLens[265] 122,133 Multi- Inferred Effectiveness LLM-J TaskCompletionRate,Personalization,
domain Naturalness,Coherence
PersonaFeedback[190] 8,298 General Given Effectiveness Auto. Accuracy
PerLTQA[30] 8,593 Memory Given, Effectiveness Auto., Accuracy,Precision,Recall,F1,Recall@K,
Inferred LLM-J MAP,Coherence
LoCoMo[114] 7,512 Memory Inferred Effectiveness, Auto. Precision,F1,Recall@K,ROUGE
Robustness
LongMemEval[222] 500 Memory Inferred Effectiveness Auto., Accuracy,Precision,Recall,F1,Recall@K,
LLM-J MAP,Coherence
Continuedonnextpage...
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 21
Table3–Continuedfrompreviouspage
Benchmark Scale Task Pref. Goal Eval. Metrics
MemoryAgentBench[52] 146 Memory Inferred Effectiveness, Auto. Accuracy,Recall@5,F1inAccurateRetrieval,
Adaptivity Test-TimeLearning,Long-range
UnderstandingandSelectiveForgetting
settings
ConvoMem[135] 75,336 Memory Inferred Effectiveness, Auto. Accuracy,Cost,Latency
Adaptivity
PAL-Bench[56] 100 Memory Inferred Effectiveness Auto., BLEU,WinRate
LLM-J
PTBench[55] 1,083 ToolUsage Given, Effectiveness, Auto. Accuracy
Inferred Robustness
ETAPP[50] 800 ToolUsage Inferred Effectiveness, Rule- PersonalizationScore,ProactivityScore
Adaptivity based,
LLM-J
PersonaMem[61] 5,990 General Inferred Effectiveness, Auto. Accuracy
Adaptivity
PersonaMem-v2[62] 10,000 General Inferred Effectiveness, Auto. Accuracy
Adaptivity
PSG-Agent[226] 2,900 Multi- Inferred Risk Auto. Accuracy,Precision,Recall,F1-score
domain
PENGUIN[229] 14,000 Multi- Given Risk LLM-J RiskSensitivity,EmotionalEmpathy,
domain User-specificAlignment
PrivacyBench[123] 478 General Given Risk LLM-J LeakageRate,Over-SecrecyRate,
InappropriateRetrievalRate,Consistency
Score
User-SubstitutionBenchmarks
LaMP[156] 25,095 General Inferred Effectiveness Auto. Accuracy,F1,MAE,RMSE,ROUGE
LongLaMP[79] 9,658 General Inferred Effectiveness Auto. ROUGE,METEOR
PEFT-U[26] 15,300 General Inferred Effectiveness Auto. BLEU,ROUGE-L,Distinct-1/2
PERSONA[15] 3,868 Dialogue Inferred Effectiveness Auto., Perplexity,BLEU,BERTScore,Persona
LLM-J consistency
PGraphRAG[7] 10,000 TextGen. Inferred Effectiveness Auto. MAE,RMSE,ROUGE,METEOR
PersonaConvBench 111,634 Multi- Inferred Effectiveness Auto., Accuracy,ROUGE,METEOR,BLEU,SBERT
[89] domain LLM-J similarity
PER-CHAT[228] 1,500,000 General Inferred Effectiveness Auto. Perplexity,BLEU
LaMP-QA[157] 29,666 Q&A Given Effectiveness Auto. ROUGE-1,ROUGE-L,METEOR
DPL[147] 9,472 TextGen Inferred Effectiveness Auto. ROUGE-1,ROUGE-L,BLEU,METEOR
REGEN[161] 1,258,224 Multi- Inferred Effectiveness, Auto. Recall@K,NDCG@K,MRR,BLEU,
domain Generalization ROUGE-L,Semanticsimilarity
KBP[199] 9,821 Q&A Given Effectiveness Auto., BLEU,ROUGE,Personagrounding,
LLM-J Knowledgegrounding
PRISM[78] 1,500 Decision Given Effectiveness LLM-J Preferenceagreement(LLM-J)
PBP[234] 50,000 Planning Inferred Effectiveness Auto. Levenshteindistance
PEToolBench[235] 3,000 ToolUsage Inferred Effectiveness, Auto. ToolAccuracy
Adaptivity
TravelPlanner++[176] 1,000 Travel Inferred Effectiveness Auto. Feasibility,Constraintsatisfaction
Planning
TripTailor[203] 3,800 Travel Inferred Effectiveness, Rule- Feasibility,Rationality,Personalization
Planning Adaptivity based,
Auto.,
LLM-J
TripCraft[16] 1,000 Travel Inferred Effectiveness, Auto., Temporal,Spatial,Ordering,Persona
Planning Adaptivity LLM-J
TripTide[71] 1,000 Travel Inferred Effectiveness, Auto., Intentpreservation,Adaptability
Planning Adaptivity LLM-J
PTS[165] 1,000 Travel Inferred Effectiveness, Auto. Constraintsatisfaction,Preferencealignment
Planning Adaptivity
PersonalWAB[14] 38,000 WebSearch Inferred Effectiveness Auto. Searchaccuracy,Rec.accuracy
PersONAL[270] 1,800 Embodied Inferred Effectiveness, Auto., Success,SPL,Grounding
Nav Adaptivity LLM-J
PIN[11] 1,193 Embodied Inferred Effectiveness, Auto., Success,Pathefficiency
Nav Adaptivity LLM-J
MEMENTO[81] 1,900 Embodied Inferred Effectiveness, Auto., Memoryrecall,Tasksuccess
Tasks Adaptivity LLM-J
FamilyTool[210] 1,152 ToolUsage Inferred Effectiveness, Auto. Toolaccuracy
Adaptivity
AgentDam[266] 246 WebSearch Given Risk LLM-J PrivacyLeakageRate
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

22 • Y.Xuetal.
8 Applications
PersonalizedLLM-poweredagentshavebeenappliedacrossawiderangeofsettings,fromconversationalsupportand
contentcreationtodelegatedassistanceandexpert-domainworkflows.Theseapplicationsdifferinautonomylevel,
riskprofile,andtheprimarytargetofpersonalization,butallrequireagentstotranslateuser-specificinformation
intosustained,context-sensitivebehavior.Weorganizerepresentativeapplicationsintofourgroups:conversational
assistants,contentcreation,delegationassistants,andexpertsupportinspecificdomains.
8.1 ConversationalAssistant
Conversationalassistantsarepersonalizedagentswhoseprimaryobjectiveistosupportusersthroughongoing
interaction. In this setting, personalization is realized through long-term dialogue continuity, context-sensitive
responsegeneration,andadaptationtouser-specificpreferences,tone,andsupportneeds.Weorganizerepresentative
applicationsinthiscategoryintodailydialogueassistants,emotionalsupportcompanions,andeducationalagents.
8.1.1 DailyDialogueAssistants. Personalizeddialogueassistantsfocusonmaintaininglong-termconversational
continuity,whereagentsmustpreserveuser-specificcontextandproducepreference-consistentresponsesacross
interactions[53,258].Recentworkincreasinglytreatslong-horizoninteractionitselfasabenchmarkedpersonal-
izationproblem[135,164],whilestudiesofdeployedassistantshighlighthowmemorybehaviorshapesusertrust
andexpectations[69].Inrecommendationandsearchsettings,personalizationfurtherdependsonsustaineduser
understanding, interaction history, and preference-aware decision making [214, 248, 250]. These trends are also
reflectedindeployedassistantssuchasChatGPT,Gemini,andDeepSeek,whichsupportpersistentusermemories
andcontrollablepersonalization[28,43,134].
8.1.2 EmotionalSupportCompanions. Emotionalsupportcompanionsprovidesustainedandempatheticassistance
forusers’well-being,wherepersonalizationdependsstronglyonpreferredtone,boundaries,andproactivity[58].
Inthissetting,personalizationcanarisebothfromuser-sidecustomizationoftheagent’spersonaandfromagent-
sideadaptationofsupportivestrategiesduringinteraction[4,268].RepresentativesystemsincludeComPeer[106],
whichdeliversproactivepeersupportbasedondialoguehistory,MultiAgentESC[239],whichusesastrategy-aware
multi-agentpipelineforemotionallycomplexinteractions,andARIEL[178],whichfurtherincorporatesphysiological
signalsforaffect-awareadaptation.Similarprioritiesarereflectedincompanion-styleproductssuchasReplikaand
Pi,wherelong-termpersonalizationandrelationship-buildingarecentraldesignfeatures[3,151].
8.1.3 EducationalAgents. Educationalagentspersonalizeinstructionandsupportbyadaptingguidance,feedback,
and learning materials to individual users [98, 166]. A common distinction is between personalized pedagogical
agents,whichsupportgeneralteachingandlearningworkflows,anddomain-specificagents,whichtailorassistance
tospecializedsubjects[24].RepresentativepedagogicalsystemssuchasEduAgent[236]andTeachTune[66]adapt
coursesupportbasedonlearnerprofilesandcontextualsignals,whiledomain-specificagentssuchasMathAgent
[242]andEduMAS[91]combinepersonalizationwithspecializedknowledgetoimprovelearningeffectiveness.These
directionsarealsoreflectedindeployededucationalsystemssuchasDuolingo[31].
8.2 ContentCreation
Personalized content creation concerns the generation of standalone textual artifacts, where agents adapt style,
structure,andframingtopersonalizationtargetsratherthansustaininginteractivedialogue[240].Inthissetting,
personalizationisevaluatedattheartifactlevel,givingrisetotwocomplementaryparadigms:author-centricalignment
withindividualwritingstyleandaudience-centricadaptationtoreaderknowledge,interests,orexpectations[132].
8.2.1 Author-Centric. Author-centriccontentcreationtreatspersonalizationasarequirementofauthorship,where
usersexpectgenerateddocumentstoreflecttheirwritingstyle,habitualphrasing,andlong-termpreferencesacross
independentoutputs[95,240,261].Thissettingisparticularlyimportantincreativewriting,professionaldocumenta-
tion,andbrandcommunication,wherequalityisjudgedattheartifactlevelratherthanthroughdialogue.Deployed
systemssuchasAdobeFireflyreflectthisparadigmbyadaptinggenerationtopersistentuserassets,priordocuments,
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 23
orstylisticconventions[2,60,131].Correspondingly,recentresearchhighlightsstablepreferencerepresentations
anddocument-levelalignmentascentralingredientsforeffectiveauthorialpersonalization[13,29,155,195].
8.2.2 Audience-Centric. Audience-centriccontentcreationpersonalizestextfortargetreadersratherthanforthe
author,adaptingcontenttoaudienceknowledge,expertise,interests,orusagecontextswhilepreservingtheintended
information[32,130,253].Thisparadigmappearsinsettingssuchasdifferentiatededucationalmaterials,culturally
adapteddocumentation,andaudience-awarecommunication,wherepersonalizationoperatesatthelevelofreader
groupsorsegments.Inpractice,itisreflectedinsystemssuchasPredis.aiandSalesForgeAI,whichtailorgenerated
contenttointendedaudiencegroups[142,158].Recentresearchsimilarlyemphasizesaudiencealignment,relevance,
andcomprehensionaskeycriteriaforqualityinaudience-conditionedgeneration[36,113,159,169,177,188].
8.3 DelegationAssistants
Delegationassistantsactonbehalfofusersbyinternalizingpreferences,managinginformation,planningactions,
andadaptingbehavioroverextendedhorizons.Comparedwithconversationalassistants,theyassumeastronger
degreeofdelegatedresponsibilityandthereforerequiremorepersistent,user-alignedrepresentations.
8.3.1 Information Handling. Information handling concerns the long-term acquisition, organization, retention,
andretrievalofuser-specificknowledgeasadelegatedcognitivefunction.Inthissetting,personalizationliesin
maintainingacoherentinformationalcontextthatcansupportdownstreamplanningandactionwithoutrepeated
userinput.RepresentativesystemsincludeARAG[116]andSPARK[21],whichtreatretrievalasapersonalized,
agent-drivenprocess,aswellasmemory-centricassistantssuchasMr.Rec[54]andlog-contextualizedRAG[27],
whichusepersistentinteractionhistorytosupportcontinuityacrosstasks.Similarideasappearindeployedsystems
suchasGleanandMem[42,118].
8.3.2 Task Planning. Task-planning delegation assistants translate high-level user goals into executable action
sequences while respecting user-specific preferences and contextual constraints. Personalization in this setting
is crucial for resolving trade-offs and prioritizing subtasks in a user-aligned way. Representative work includes
VAIAGE,whichframespersonalizedtravelplanningasacollaborativemulti-agentprocessunderuserrequirements
[101],aswellaslearning-basedapproachesshowingthatexplicitlymodelinguserpreferencesimprovesplanning
qualityandalignment[234].Relatedworkalsoextendspersonalizedplanningtocollaborative,embodied,andsocial
decision-makingsettings[48,149,249].
8.3.3 BehaviorAdaptation. Behavioradaptationconcernshowdelegationassistantsaligninteractionstyle,initiative,
anddecisiontendencieswithauser’shabitualpatternsovertime.Itsupportsreliabledelegationbyinternalizingstable
routineswhileremainingresponsivetoevolvinggoals,therebyreducingsupervisionandcognitiveburden.MEAgent
modelspersistentuserhabitsinmobileassistantsettings[206],whilememory-centricframeworksenableagents
toaccumulateandreuseuser-specificknowledgebeyondsingleinteractions[213,220].Test-timepersonalization
methodssuchasPersonaAgentfurthershowthatadaptivedelegationcanberealizeddynamicallythroughinferred
userpersonaswithoutretraining[254].Atthesametime,recentworkhighlightsthatmoreautonomousbehavior
adaptationalsoincreasestheneedforcontrollablepersonalizationandsafeguardsagainstmisalignment[40,182].
8.4 ExpertSupportinSpecificDomains
Personalizedagentsareincreasinglydeployedasexpertassistantsinspecializeddomainssuchashealthcare,finance,
legalservices,andresearchworkflows,whereuser-centrictailoringcanimproverelevanceandusabilitybutmustbe
reconciledwithstringentdomainconstraintsandrisk-sensitiverequirements[196].
8.4.1 Healthcare. Inhealthcare,personalizationisshiftingfromsingle-turnquestionansweringtolongitudinal,state-
fulinteraction,whereagentsmustsupportapatienttrajectoryratherthanonlyisolateddiagnoses.Frameworkssuch
asMedChainandMedPlanorganizemulti-stageclinicalpipelinesspanninghistoryelicitation,symptomclarification,
andtreatmentplanning[51,102].Toreducetherisksofover-accommodationandunsafeagreement,recentsystems
increasinglyadoptmodulararchitecturesthatseparatepatient-facingcommunicationfromclinicalverification,as
illustratedbyPolarisandColaCare[122,215].Fordata-intensivesettings,EHRAgentfurthergroundspersonalized
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

24 • Y.Xuetal.
EHRanalysisindeterministiccodeexecutionratherthanpurelygenerativereasoning[67,170].Evaluationenvi-
ronmentssuchasAgentClinichighlighttheneedtostress-testpersonalizedclinicalagentsunderdiversesimulated
patientbehaviors[112,163].
8.4.2 Finance. In finance, personalization must balance alignment with individual goals and behaviors against
cognitivebias,trustcalibration,andhardcompliancerequirements.FinPersona-basedstudiesrevealatrust–quality
paradox,showingthatpersona-drivenpersonalizationcanincreaseusertrustevenwhentheunderlyingadviceis
poorerorriskier[184,185].Thismotivatessafety-awarepersonalizationframeworkssuchasPSG-Agent,which
introducepersonality-conditionedguardrailstocalibraterecommendations[226].Atthearchitecturallevel,systems
suchasFinRobotdecomposeworkflowsintospecializedrolesfordataaggregation,quantitativeanalysis,andthesis
generation,whileGraphComplianceconstrainspersonalizationwithstructuredregulatoryreasoningpaths[25,243].
8.4.3 Legalservices. Inlegalservices,personalizationconditionsreasoningonuser-specificfacts,jurisdictions,and
draftingintents,turningassistanceintoacontext-sensitiveinferenceproblem.Acentralchallengeisstatutorydrift,
whereagentsmustapplyevolvinglawstoindividualcasesratherthanrelyingonstaticknowledge.Benchmarkssuch
asLawShiftshowthatthisadaptabilitymustoftenbeachievedatinferencetimeratherthanthroughretraining[49].
Personalizationalsoamplifieshallucinationrisksinlegaldrafting,motivatingpost-hocverificationloopssuchas
Citation-EnhancedGenerationandwatchdogframeworkslikeHalMit,whichvalidateoutputsagainstauthoritative
legalsourcesbeforedelivery[93,105].Thisisespeciallyimportantformultilingualandjurisdiction-awarelegal
assistantssuchasMina[216].
8.4.4 ResearchAssistance. Researchassistancesupportsexpertusersacrosstheresearchlifecyclebyperforming
project-andgoal-conditionedscholarlywork.EarlysystemspositionLLMagentsasgeneralresearchcollaborators
forexplorationandorchestration,asinAgentLaboratory[162],whilelaterworkmovestowarduser-andcontext-
conditionedpipelinesforprojectscoping,retrieval,anddialogue[33,120].Multi-agentsettingsfurtherextendthis
intosustained,statefulworkflowsthroughvirtualresearchgroupsanditerativeinvestigation[84,127].Recentstudies
emphasizehuman-centereddeployment,trust,andverifiabilityinrealresearchsettings,whilecomplementarywork
explorespersonalizedscaffoldingandcustomizedwritingsupportforproductivity[19,70,72].
9 OpenProblemsandFutureDirections
Despiterapidprogress,buildingrobust,scalable,anddeployablepersonalizedagentsremainsanopenchallenge.
Manyoftheremainingdifficultiesarecross-cuttingratherthanmodule-specific:theyarisefromhowusermodels
areconstructed,updated,generalized,evaluated,anddeployedunderreal-worldconstraints.Below,wesummarize
severaldirectionsthatweviewasespeciallyimportantforfutureresearch.
9.1 Decision-CriticalUserModeling
Acentralopenprobleminpersonalizedagentsishowtorepresentuserinformationinaformthatisbothexpressive
and decision-relevant. User preferences vary not only across individuals but also across tasks, aspects of a task,
andevensituationswithinthesameuser,andtheyareoftenrevealedonlyindirectlythroughbehavior,interaction
patterns,ortoolusage.Asaresult,effectivepersonalizationrequiresmorethanrichusermodeling:italsorequires
identifyingwhichuserattributesactuallymatterforthedecisionathand.Thischallengeisespeciallypronounced
acrossapplicationsettings,wheregeneral-purposeassistantsmayrelyonbroadstylisticorvaluealignment,while
domain-specificorhigh-stakesagentsdependonfine-grainedattributesthatdirectlyaffectoutcomes.Futurework
shouldthereforefocusonstructuredandadaptiveuserrepresentationsthatcandistinguishdecision-criticalsignals
fromperipheralones,ratherthanassumingafixedoruniversallyrelevantusermodel.
9.2 TemporalDynamicsandContinualPersonalization
Personalizationisinherentlydynamic:userpreferencesareprogressivelyrevealedthroughinteraction,anddifferent
aspectsofuserinformationevolveatdifferenttemporalscales.Short-terminterestsmayshiftrapidlyacrosscontexts,
whereas long-term values, goals, or reasoning styles are often more stable. This temporal heterogeneity makes
staticpersonalizationmechanismsfundamentallyinadequate.Futureresearchshouldthereforedevelopcontinual
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 25
personalization methods that can update user representations over time without catastrophic forgetting, while
distinguishingtransientpreferencesfromdurableones.Morebroadly,personalizedagentsshouldclosetheloop
betweenobservationandaction,sothatnewlyacquiredsignalscanbeincorporatedinwaysthatmaintainalignment
ratherthangraduallydegradingit.
9.3 Generalization
Personalizedagentsmustoftenoperateundersparse,uneven,ormissinguserdata,makinggeneralizationacore
challengeforreal-worlddeployment.Thisproblemarisesalongatleasttwodimensions.First,agentsmustgeneralize
tounseenorlow-interactionusers,wherelimitedevidencemakesdirectpreferenceinferenceunreliable.Second,
theymustgeneralizeacrossdomainsandtasks,wherepreferenceslearnedinonecontextmayonlypartiallytransfer
toanotherbecausetaskstructures,actionspaces,ordecisioncriteriadiffer.Promisingdirectionsincludefew-shot
andmeta-learningapproachesforrapidadaptation,uncertainty-awarepersonalizationthatavoidsoverconfident
alignmentunderweakevidence,andtransferablepreferenceabstractionsthatcapturereusabledecisionprinciples
ratherthannarrowtask-specificbehaviors.
9.4 EvaluationandBenchmarking
Evaluatingpersonalizationposesauniquechallengebecausesuccessisdefinedrelativetoindividualusersratherthan
objectivetaskcompletion.Existingbenchmarksoftenrelyonsyntheticuserdatageneratedbylanguagemodels,which
mayfailtocapturerealhumandiversityandcansufferfromhomogenizationeffects.Additionally,commonevaluation
protocolssuchasLLM-as-a-judgeraiseconcernsaboutreliabilityandalignmentwithhumansatisfaction.Future
evaluationframeworksshouldemphasizefine-grained,component-levelanalysisanddistinguishbetweenintra-user
consistencyandinter-userdifferentiation.Incorporatinghuman-in-the-loopevaluation,longitudinalinteraction
studies,anduser-centricsatisfactionmetricsmayprovidemorefaithfulassessmentsofpersonalizationquality.
9.5 PrivacyandUserControl
Personalizationinherentlydependsoncollecting,storing,andreusinguserdata,makingprivacyacentralchallenge
fordeployment.Evenwhenuserdataisstoredseparately,risksremainintheformofunauthorizedaccess,unintended
leakage,orsecondarymisuse.Moreover,self-evolvingagentsmayerodetrustifusersfeeltheynolongerunderstand
orcontrolhowtheirinformationisbeingretainedandapplied.Futuresystemsmustthereforebalancedatautility
withprivacypreservationthroughprivacy-awarememoryarchitectures,selectiveretentionpolicies,on-deviceor
federatedpersonalization,andtransparentinterfacesforinspecting,editing,andmanagingstoredinformation.In
thissense,privacyshouldbetreatednotonlyasatechnicalsafeguardbutalsoasacorepartoftheuserexperience.
9.6 EfficiencyandDeployment
Apracticalopenproblemishowtodelivermeaningfulpersonalizationunderreal-worldresourceconstraints.In
currentsystems,personalizationisoftenimplementedthroughpost-trainingadaptation,inference-timeaugmentation,
memoryretrieval,orrepeatedplanningandtooluse,allofwhichintroduceadditionalstorage,latency,andcomputation
costs.Futureworkshouldthereforeexploreworkflowdesignsthatexplicitlytradeoffpersonalizationdepthagainst
deploymentcost.Lightweightpersonalizationmechanisms,adaptivememoryusage,andbudget-awareinference
strategiesmayallowagentstoprovidesustaineduseralignmentwithoutincurringprohibitiveoverhead.
10 Conclusion
PersonalizationisbecomingadefiningcapabilityofLLM-poweredagents,enablingthemtomovebeyondgenerictask
executiontowardsustained,user-alignedcollaboration.Thissurveypresentedasystem-levelviewofpersonalized
LLM-powered agents through four core capabilities: profile modeling, memory, planning, and action execution.
Overall,personalizationshouldbeunderstoodnotasanisolatedmodule,butasasystem-widepropertyofagent
design.Despitesubstantialprogress,majorchallengesremaininusermodeling,generalization,evaluation,privacy,
and efficiency. Future progress will require integrated architectures that support personalization together with
robustness,safety,anddeployability.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

26 • Y.Xuetal.
References
[1] DeepakBhaskarAcharya,KarthigeyanKuppan,andBDivya.2025.Agenticai:Autonomousintelligenceforcomplexgoals–acomprehensive
survey.IEEeAccess(2025).
[2] Adobe.2023.AdobeFirefly—firefly.adobe.com.https://firefly.adobe.com/.
[3] InflectionAI.[n.d.].Pi,yourpersonalAI—pi.ai.https://pi.ai/onboarding/pi-intro.
[4] JaberOAlotaibiandAmerSAlshahre.2024.TheroleofconversationalAIagentsinprovidingsupportandsocialcareforisolatedindividuals.
AlexandriaEngineeringJournal108(2024),273–284.
[5] PetrAnokhin,NikitaSemenov,ArtyomSorokin,DmitryEvseev,AndreyKravchenko,MikhailBurtsev,andEvgenyBurnaev.2024.Arigraph:
Learningknowledgegraphworldmodelswithepisodicmemoryforllmagents.arXivpreprintarXiv:2407.04363(2024).
[6] Anthropic.2025.Commonworkflows-ClaudeCodeDocs—code.claude.com.https://code.claude.com/docs/en/common-workflows.
[7] StevenAu,CameronJDimacali,OjasmithaPedirappagari,NamyongPark,FranckDernoncourt,YuWang,NikosKanakaris,Hanieh
Deilamsalehy,RyanARossi,andNesreenKAhmed.2025.Personalizedgraph-basedretrievalforlargelanguagemodels.arXivpreprint
arXiv:2501.02157(2025).
[8] BahmanBahmani,AbdurChowdhury,andAshishGoel.2010.Fastincrementalandpersonalizedpagerank.arXivpreprintarXiv:1006.2880
(2010).
[9] AshmiBanerjee,AdithiSatish,FitriNurAisyah,WolfgangWörndl,andYasharDeldjoo.2025.Collab-REC:AnLLM-basedAgenticFramework
forBalancingRecommendationsinTourism.arXivpreprintarXiv:2508.15030(2025).
[10] AndréBarreto,VincentDumoulin,YiranMao,NicolasPerez-Nieves,BobakShahriari,YannDauphin,DoinaPrecup,andHugoLarochelle.
2025.Capturingindividualhumanpreferenceswithrewardfeatures.arXivpreprintarXiv:2503.17338(2025).
[11] LucaBarsellotti,RobertoBigazzi,MarcellaCornia,LorenzoBaraldi,andRitaCucchiara.2024.Personalizedinstance-basednavigationtoward
user-specificobjectsinrealisticenvironments.AdvancesinNeuralInformationProcessingSystems37(2024),11228–11250.
[12] AvinandanBose,ZhihanXiong,YuejieChi,SimonShaoleiDu,LinXiao,andMaryamFazel.2025.LoRe:PersonalizingLLMsviaLow-Rank
RewardModeling.arXivpreprintarXiv:2504.14439(2025).
[13] HyungjuneBu,ChanjooJung,MinjaeKang,andJaehyungKim.2025.Personalizedllmdecodingviacontrastingpersonalpreference.In
Proceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.33946–33966.
[14] HongruCai,YongqiLi,WenjieWang,FengbinZhu,XiaoyuShen,WenjieLi,andTat-SengChua.2025.Largelanguagemodelsempowered
personalizedwebagents.InProceedingsoftheACMonWebConference2025.198–215.
[15] LouisCastricato,NathanLile,RafaelRafailov,Jan-PhilippFränken,andChelseaFinn.2025.Persona:Areproducibletestbedforpluralistic
alignment.InProceedingsofthe31stInternationalConferenceonComputationalLinguistics.11348–11368.
[16] SoumyabrataChaudhuri,PranavPurkar,RitwikRaghav,ShubhojitMallick,ManishGupta,AbhikJana,andShreyaGhosh.2025.Tripcraft:
A benchmark for spatio-temporally fine grained travel planning. In Proceedings of the 63rd Annual Meeting of the Association for
ComputationalLinguistics(Volume1:LongPapers).17035–17064.
[17] JiaruiChen.2025.MemoryAssistedLLMforPersonalizedRecommendationSystem.arXivpreprintarXiv:2505.03824(2025).
[18] Wei-HaoChen,WeixiTong,AmandaCase,andTianyiZhang.2025.Dango:amixed-initiativedatawranglingsystemusinglargelanguage
model.InProceedingsofthe2025CHIConferenceonHumanFactorsinComputingSystems.1–28.
[19] ZanChen,JingjingChen,YuGuangWang,andYiqingShen.2025.AHuman-CenteredAIAgentFrameworkwithLargeLanguageModelsfor
AcademicResearchTasks.InCCFInternationalConferenceonNaturalLanguageProcessingandChineseComputing.Springer,363–374.
[20] ZihaoCheng,HongruWang,ZemingLiu,YuhangGuo,YuanfangGuo,YunhongWang,andHaifengWang.2025.ToolSpectrum:Towards
personalizedtoolutilizationforlargelanguagemodels.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.20679–20699.
[21] GaurabChhetri,SubasishDas,andTausifIslamChowdhury.2025.SPARK:SearchPersonalizationviaAgent-DrivenRetrievalandKnowledge-
sharing.arXivpreprintarXiv:2512.24008(2025).
[22] PrateekChhikara,DevKhant,SaketAryan,TaranjeetSingh,andDeshrajYadav.2025.Mem0:Buildingproduction-readyaiagentswith
scalablelong-termmemory.arXivpreprintarXiv:2504.19413(2025).
[23] SadiaSultanaChowa,RiasadAlvi,SubheySadiRahman,MdAbdurRahman,MohaimenulAzamKhanRaiaan,MdRafiqulIslam,Mukhtar
Hussain,andSamiAzam.2026.Fromlanguagetoaction:areviewoflargelanguagemodelsasautonomousagentsandtoolusers.Artificial
IntelligenceReview(2026).
[24] ZhendongChu,ShenWang,JianXie,TinghuiZhu,YiboYan,JinhengYe,AoxiaoZhong,XumingHu,JingLiang,PhilipSYu,etal.2025.Llm
agentsforeducation:Advancesandapplications.arXivpreprintarXiv:2503.11733(2025).
[25] JiseongChung,RonnyKo,WonchulYoo,MakotoOnizuka,SungmokKim,Tae-WanKim,andWon-YongShin.2025.GraphCompliance:
AligningPolicyandContextGraphsforLLM-BasedRegulatoryCompliance.arXivpreprintarXiv:2510.26309(2025).
[26] ChristopherClarke,YuzhaoHeng,LingjiaTang,andJasonMars.2024.Peft-u:Parameter-efficientfine-tuningforuserpersonalization.arXiv
preprintarXiv:2407.18078(2024).
[27] ClaytonCohn,SuryaRayala,CaitlinSnyder,JoyceFonteles,ShrutiJain,NaveeduddinMohammed,UmeshTimalsina,SarahKBurriss,
NamrataSrivastava,MentonDeweese,etal.2025.PersonalizingStudent-AgentInteractionsUsingLog-ContextualizedRetrievalAugmented
Generation(RAG).arXivpreprintarXiv:2505.17238(2025).
[28] DeepSeek.2024.DeepSeek|deepseek.com.https://www.deepseek.com/.
[29] PriyankaDey,DanieleRosa,WenqingZheng,DanielBarcklow,JieyuZhao,andEmilioFerrara.2025.GRAVITY:AFrameworkforPersonalized
TextGenerationviaProfile-GroundedSyntheticPreferences.arXivpreprintarXiv:2510.11952(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 27
[30] YimingDu,HongruWang,ZhengyiZhao,BinLiang,BaojunWang,WanjunZhong,ZezhongWang,andKam-FaiWong.2024.Perltqa:A
personallong-termmemorydatasetformemoryclassification,retrieval,andsynthesisinquestionanswering.arXivpreprintarXiv:2402.16288
(2024).
[31] Duolingo.2025.Learnalanguageforfree—duolingo.com.https://www.duolingo.com/.
[32] MehmetSametDuranandTevfikAytekin.2025.Beyondone-size-fits-allsummarization:Customizingsummariesfordiverseusers.arXiv
preprintarXiv:2503.10675(2025).
[33] JacobEmmerson,RayidGhani,andZheyuanRyanShi.2025.TowardsAutomatedScopingofAIforSocialGoodProjects.arXivpreprint
arXiv:2504.20010(2025).
[34] JizhanFang,XinleDeng,HaomingXu,ZiyanJiang,YuqiTang,ZiwenXu,ShuminDeng,YunzhiYao,MengruWang,ShuofeiQiao,etal.
2025.LightMem:LightweightandEfficientMemory-AugmentedGeneration.arXivpreprintarXiv:2510.18866(2025).
[35] MohamedAmineFerrag,NorbertTihanyi,andMerouaneDebbah.2025.Fromllmreasoningtoautonomousaiagents:Acomprehensive
review.arXivpreprintarXiv:2504.19678(2025).
[36] XiaoFu,HosseinARahmani,BinWu,JeromeRamos,EmineYilmaz,andAldoLipani.2025.PREF:Reference-FreeEvaluationofPersonalised
TextGenerationinLLMs.arXivpreprintarXiv:2508.10028(2025).
[37] GeGao,AlexeyTaymanov,EduardoSalinas,PaulMineiro,andDipendraMisra.2024.Aligningllmagentsbylearninglatentpreferencefrom
useredits.AdvancesinNeuralInformationProcessingSystems37(2024),136873–136896.
[38] Huan-angGao,JiayiGeng,WenyueHua,MengkangHu,XinzheJuan,HongzhangLiu,ShilongLiu,JiahaoQiu,XuanQi,YiranWu,etal.
2025.Asurveyofself-evolvingagents:Onpathtoartificialsuperintelligence.arXivpreprintarXiv:2507.21046(2025).
[39] ShenGao,YuntaoWen,MinghangZhu,JianingWei,YuhanCheng,QunziZhang,andShuoShang.2024.Simulatingfinancialmarketvia
largelanguagemodelbasedagents.arXivpreprintarXiv:2406.19966(2024).
[40] SimretArayaGebreegziabher,YukunYang,CharlesChiang,HojunYoo,ChaoranChen,HyoJinDo,ZahraAshktorab,WernerGeyer,Diego
Gómez-Zará,andTobyJia-JunLi.2026. TheBehavioralFabricofLLM-PoweredGUIAgents:HumanValuesandInteractionOutcomes.
arXivpreprintarXiv:2601.16356(2026).
[41] Github.2025.GitHubCopilotfeatures-GitHubDocs—docs.github.com.https://docs.github.com/en/copilot/get-started/features.
[42] Inc.GleanTechnologies.2023.Glean—glean.com.https://www.glean.com/.
[43] Google.2023.GoogleGemini—gemini.google.com.https://gemini.google.com/.
[44] ZhibinGou,ZhihongShao,YeyunGong,YelongShen,YujiuYang,NanDuan,andWeizhuChen.2023.Critic:Largelanguagemodelscan
self-correctwithtool-interactivecritiquing.arXivpreprintarXiv:2305.11738(2023).
[45] JianGuan,JunfeiWu,Jia-NanLi,ChuanqiCheng,andWeiWu.2025.ASurveyonPersonalizedAlignment—TheMissingPieceforLarge
LanguageModelsinReal-WorldApplications.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.5313–5333.
[46] DayaGuo,DejianYang,HaoweiZhang,JunxiaoSong,RuoyuZhang,RunxinXu,QihaoZhu,ShirongMa,PeiyiWang,XiaoBi,etal.2025.
Deepseek-r1:Incentivizingreasoningcapabilityinllmsviareinforcementlearning.arXivpreprintarXiv:2501.12948(2025).
[47] BernalJiménezGutiérrez,YihengShu,WeijianQi,SizheZhou,andYuSu.2025.Fromragtomemory:Non-parametriccontinuallearningfor
largelanguagemodels.arXivpreprintarXiv:2502.14802(2025).
[48] DonggeHan,TrevorMcInroe,AdamJelley,StefanoVAlbrecht,PeterBell,andAmosStorkey.2025.Llm-personalize:Aligningllmplanners
withhumanpreferencesviareinforcedself-trainingforhousekeepingrobots.InProceedingsofthe31stInternationalConferenceon
ComputationalLinguistics.1465–1474.
[49] ZhuoHan,YiYang,YiFeng,WanhongHuang,XuxingDing,ChuanyiLi,JidongGe,andVincentNg.2025.LawShift:BenchmarkingLegal
JudgmentPredictionUnderStatuteShifts.InTheThirty-ninthAnnualConferenceonNeuralInformationProcessingSystemsDatasetsand
BenchmarksTrack.
[50] YupuHao,PengfeiCao,ZhuoranJin,HuanxuanLiao,YuboChen,KangLiu,andJunZhao.2025.Evaluatingpersonalizedtool-augmentedllms
fromtheperspectivesofpersonalizationandproactivity.InProceedingsofthe63rdAnnualMeetingoftheAssociationforComputational
Linguistics(Volume1:LongPapers).21897–21935.
[51] Hsin-LingHsu,Cong-TinhDao,LuningWang,ZitaoShuai,ThaoNguyenMinhPhan,Jun-EnDing,Chun-ChiehLiao,PengfeiHu,Xiaoxue
Han,Chih-HoHsu,etal.2025.Medplan:atwo-stagerag-basedsystemforpersonalizedmedicalplangeneration.InProceedingsofthe63rd
AnnualMeetingoftheAssociationforComputationalLinguistics(Volume6:IndustryTrack).1072–1082.
[52] YuanzheHu,YuWang,andJulianMcAuley.2025.Evaluatingmemoryinllmagentsviaincrementalmulti-turninteractions.arXivpreprint
arXiv:2507.05257(2025).
[53] ChengkaiHuang,JundaWu,YuXia,ZixuYu,RuhanWang,TongYu,RuiyiZhang,RyanARossi,BranislavKveton,DongruoZhou,etal.
2025.Towardsagenticrecommendersystemsintheeraofmultimodallargelanguagemodels.arXivpreprintarXiv:2503.16734(2025).
[54] JianiHuang,XingchenZou,LianghaoXia,andQingLi.2025.Mr.rec:Synergizingmemoryandreasoningforpersonalizedrecommendation
assistantwithllms.arXivpreprintarXiv:2510.14629(2025).
[55] XuHuang,YuefengHuang,WeiwenLiu,XingshanZeng,YashengWang,RuimingTang,HongXie,andDefuLian.2025.Advancingand
BenchmarkingPersonalizedToolInvocationforLLMs.arXivpreprintarXiv:2505.04072(2025).
[56] ZhaopeiHuang,QifengDai,GuozhengWu,XiaopengWu,KehanChen,ChuanYu,XubinLi,TiezhengGe,WenxuanWang,andQin
Jin.2025. Mem-PAL:TowardsMemory-basedPersonalizedDialogueAssistantsforLong-termUser-AgentInteraction. arXivpreprint
arXiv:2511.13410(2025).
[57] ZhengjunHuang,ZhoujinTian,QintianGuo,FangyuanZhang,YingliZhou,DiJiang,andXiaofangZhou.2025.LiCoMemory:Lightweight
andCognitiveAgenticMemoryforEfficientLong-TermReasoning.arXivpreprintarXiv:2511.01448(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

28 • Y.Xuetal.
[58] BaharIrfan,SannaKuoppamäki,andGabrielSkantze.2024.Recommendationsfordesigningconversationalcompanionrobotswitholder
adultsthroughfoundationmodels.FrontiersinRoboticsandAI11(2024),1363713.
[59] GautierIzacard,MathildeCaron,LucasHosseini,SebastianRiedel,PiotrBojanowski,ArmandJoulin,andEdouardGrave.2021.Unsupervised
denseinformationretrievalwithcontrastivelearning.arXivpreprintarXiv:2112.09118(2021).
[60] Jasper.2023.JasperBrandVoice—jasper.ai/brand-voice.https://www.jasper.ai/brand-voice.
[61] BowenJiang,ZhuoqunHao,Young-MinCho,BryanLi,YuanYuan,SihaoChen,LyleUngar,CamilloJTaylor,andDanRoth.2025.Knowme,
respondtome:Benchmarkingllmsfordynamicuserprofilingandpersonalizedresponsesatscale.arXivpreprintarXiv:2504.14225(2025).
[62] BowenJiang,YuanYuan,MaohaoShen,ZhuoqunHao,ZhangchenXu,ZichenChen,ZiyiLiu,AnveshRaoVijjini,JiashuHe,HanchaoYu,
etal.2025.PersonaMem-v2:TowardsPersonalizedIntelligenceviaLearningImplicitUserPersonasandAgenticMemory.arXivpreprint
arXiv:2512.06688(2025).
[63] LiweiJiang,TaylorSorensen,SydneyLevine,andYejinChoi.2024.Canlanguagemodelsreasonaboutindividualistichumanvaluesand
preferences?arXivpreprintarXiv:2410.03868(2024).
[64] XunJiang,FengLi,HanZhao,JiahaoQiu,JiayingWang,JunShao,ShihaoXu,ShuZhang,WeilingChen,XavierTang,etal.2024.Longterm
memory:Thefoundationofaiself-evolution.arXivpreprintarXiv:2410.15665(2024).
[65] BernalJimenezGutierrez,YihengShu,YuGu,MichihiroYasunaga,andYuSu.2024.Hipporag:Neurobiologicallyinspiredlong-termmemory
forlargelanguagemodels.AdvancesinNeuralInformationProcessingSystems37(2024),59532–59569.
[66] HyoungwookJin,MinjuYoo,JeongeonPark,YokyungLee,XuWang,andJuhoKim.2025.Teachtune:Reviewingpedagogicalagentsagainst
diversestudentprofileswithsimulatedstudents.InProceedingsofthe2025CHIConferenceonHumanFactorsinComputingSystems.
1–28.
[67] MingyuJin,QinkaiYu,DongShu,ChongZhang,LizhouFan,WenyueHua,SuiyuanZhu,YandaMeng,ZhentingWang,MengnanDu,etal.
2024.Health-llm:Personalizedretrieval-augmenteddiseasepredictionsystem.arXivpreprintarXiv:2402.00746(2024).
[68] JeffJohnson,MatthijsDouze,andHervéJégou.2019.Billion-scalesimilaritysearchwithGPUs.IEEETransactionsonBigData7,3(2019),
535–547.
[69] BrennanJones,KelseyStemmler,EmilySu,Young-HoKim,andAnastasiaKuzminykh.2025.Users’ExpectationsandPracticeswithAgent
Memory.InProceedingsoftheExtendedAbstractsoftheCHIConferenceonHumanFactorsinComputingSystems.1–8.
[70] AymenKabir,SurajShah,AlexanderHaddad,andDanielMSRaper.2025.IntroducingourcustomGPT:Anexampleofthepotentialimpact
ofpersonalizedGPTbuildersonscientificwriting.WorldNeurosurgery193(2025),461–468.
[71] PriyanshuKarmakar,SoumyabrataChaudhuri,ShubhojitMallick,ManishGupta,AbhikJana,andShreyaGhosh.2025.TripTide:ABenchmark
forAdaptiveTravelPlanningunderDisruptions.arXivpreprintarXiv:2510.21329(2025).
[72] SeanKelley,DavidDeCremer,andChristophRiedl.2025.PersonalizedAIScaffoldsSynergisticMulti-TurnCollaborationinCreativeWork.
arXivpreprintarXiv:2510.27681(2025).
[73] CallieYKim,ChristinePLee,andBilgeMutlu.2024. Understandinglarge-languagemodel(llm)-poweredhuman-robotinteraction.In
Proceedingsofthe2024ACM/IEEEinternationalconferenceonhuman-robotinteraction.371–380.
[74] HannahKim,KushanMitra,ChenShen,DanZhang,andEstevamHruschka.2025.AIPOM:Agent-awareInteractivePlanningforMulti-Agent
Systems.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing:SystemDemonstrations.85–96.
[75] JaehyungKimandYimingYang.2024.Few-shotpersonalizationofllmswithmis-alignedresponses.arXivpreprintarXiv:2406.18678(2024).
[76] MinbeomKim,Kang-ilLee,SeonghoJoo,HwaranLee,ThibautThonet,andKyominJung.2025.Drift:Decoding-timepersonalizedalignments
withimplicituserpreferences.arXivpreprintarXiv:2502.14289(2025).
[77] SangyeopKim,YohanLee,SanghwaKim,HyunjongKim,andSungzoonCho.2025.Pre-StorageReasoningforEpisodicMemory:Shifting
InferenceBurdentoMemoryforPersonalizedDialogue.arXivpreprintarXiv:2509.10852(2025).
[78] HannahRoseKirk,AlexanderWhitefield,PaulRottger,AndrewMBean,KaterinaMargatina,RafaelMosquera-Gomez,JuanCiro,Max
Bartolo,AdinaWilliams,HeHe,etal.2024.Theprismalignmentdataset:Whatparticipatory,representativeandindividualisedhuman
feedbackrevealsaboutthesubjectiveandmulticulturalalignmentoflargelanguagemodels.AdvancesinNeuralInformationProcessing
Systems37(2024),105236–105344.
[79] IshitaKumar,SnigdhaViswanathan,SushritaYerra,AlirezaSalemi,RyanARossi,FranckDernoncourt,HaniehDeilamsalehy,Xiang
Chen,RuiyiZhang,ShubhamAgarwal,etal.2024. Longlamp:Abenchmarkforpersonalizedlong-formtextgeneration. arXivpreprint
arXiv:2407.11016(2024).
[80] MehmetKurmaz.2026.AWARE-US:BenchmarkforPreference-AwareResolutioninTool-CallingAgents.arXivpreprintarXiv:2601.02643
(2026).
[81] TaeyoonKwon,DongwookChoi,SunghwanKim,HyojunKim,SeungjunMoon,Beong-wooKwak,Kuan-HaoHuang,andJinyoungYeo.
2025.EmbodiedAgentsMeetPersonalization:ExploringMemoryUtilizationforPersonalizedAssistance.arXivpreprintarXiv:2505.16348
(2025).
[82] SeongyunLee,SueHyunPark,SeungoneKim,andMinjoonSeo.2024.Aligningtothousandsofpreferencesviasystemmessagegeneralization.
AdvancesinNeuralInformationProcessingSystems37(2024),73783–73829.
[83] PatrickLewis,EthanPerez,AleksandraPiktus,FabioPetroni,VladimirKarpukhin,NamanGoyal,HeinrichKüttler,MikeLewis,Wen-tau
Yih,TimRocktäschel,etal.2020. Retrieval-augmentedgenerationforknowledge-intensivenlptasks. Advancesinneuralinformation
processingsystems33(2020),9459–9474.
[84] EdLi,JunyuRen,XintianPan,CatYan,ChuanhaoLi,DirkBergemann,andZhuoranYang.2025.BuildYourPersonalizedResearchGroup:A
MultiagentFrameworkforContinualandInteractiveScienceAutomation.arXivpreprintarXiv:2510.15624(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 29
[85] HaoLi,RuoyuanGong,andHaoJiang.2025.Politicalactoragent:Simulatinglegislativesystemforrollcallvotespredictionwithlarge
languagemodels.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.39.388–396.
[86] HaoLi,ChenghaoYang,AnZhang,YangDeng,XiangWang,andTat-SengChua.2025.Helloagain!llm-poweredpersonalizedagentfor
long-termdialogue.InProceedingsofthe2025ConferenceoftheNationsoftheAmericasChapteroftheAssociationforComputational
Linguistics:HumanLanguageTechnologies(Volume1:LongPapers).5259–5276.
[87] Jia-NanLi,JianGuan,SonghaoWu,WeiWu,andRuiYan.2025.From1,000,000userstoeveryuser:Scalinguppersonalizedpreferencefor
user-levelalignment.arXivpreprintarXiv:2503.15463(2025).
[88] Jia-NanLi,JianGuan,WeiWu,andRuiYan.2025.Extendedinductivereasoningforpersonalizedpreferenceinferencefrombehavioral
signals.arXivpreprintarXiv:2505.18071(2025).
[89] LiLi,PeilinCai,RyanARossi,FranckDernoncourt,BranislavKveton,JundaWu,TongYu,LinxinSong,TiankaiYang,YuehanQin,etal.
2025.APersonalizedConversationalBenchmark:TowardsSimulatingPersonalizedConversations.arXivpreprintarXiv:2505.14106(2025).
[90] NingLi,QiqiangLin,ZhengWu,XiaoyunMo,WeimingZhang,YinZhao,XiangmouQu,JiamuZhou,JunWang,CongminZheng,etal.
2025.ColorAgent:BuildingARobust,Personalized,andInteractiveOSAgent.arXivpreprintarXiv:2510.19386(2025).
[91] QiaomuLi,YingXie,SumitChakravarty,andDabaeLee.2024.EduMAS:AnovelLLM-poweredmulti-agentframeworkforeducational
support.In2024IEEEInternationalConferenceonBigData(BigData).IEEE,8309–8316.
[92] ShuyueStellaLi,AvinandanBose,FaezeBrahman,SimonShaoleiDu,PangWeiKoh,MaryamFazel,andYuliaTsvetkov.2025.PrefDisco:
EvaluatingProactivePersonalizationthroughInteractivePreferenceDiscovery.InFirstWorkshoponMulti-TurnInteractionsinLarge
LanguageModels.
[93] WeitaoLi,JunkaiLi,WeizhiMa,andYangLiu.2024. Citation-enhancedgenerationforLLM-basedchatbots.InProceedingsofthe62nd
AnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).1451–1466.
[94] XinzheLi.2025. Areviewofprominentparadigmsforllm-basedagents:Tooluse,planning(includingrag),andfeedbacklearning.In
Proceedingsofthe31stinternationalconferenceoncomputationallinguistics.9760–9779.
[95] XiaopengLi,PengyueJia,DerongXu,YiWen,YingyiZhang,WenlinZhang,WanyuWang,YichaoWang,ZhaochengDu,XiangyangLi,
etal.2025.Asurveyofpersonalization:Fromragtoagent.arXivpreprintarXiv:2504.10147(2025).
[96] YiLi,JiemingZhu,WeiwenLiu,LiangcaiSu,GuohaoCai,QiZhang,RuimingTang,XiXiao,andXiuqiangHe.2022.Pear:Personalized
re-rankingwithcontextualizedtransformerforrecommendation.InCompanionProceedingsoftheWebConference2022.62–66.
[97] ZhiyuLi,ShichaoSong,ChenyangXi,HanyuWang,ChenTang,SiminNiu,DingChen,JiaweiYang,ChunyuLi,QingchenYu,etal.2025.
Memos:Amemoryosforaisystem.arXivpreprintarXiv:2507.03724(2025).
[98] GuannanLiangandQianqianTong.2025.LLM-poweredAIagentsystemsandtheirapplicationsinindustry.In2025IEEEWorldAIIoT
Congress(AIIoT).IEEE,0463–0471.
[99] YuanLiang,JiaxianLi,YuqingWang,PiaohongWang,MotongTian,PaiLiu,ShuofeiQiao,RunnanFang,HeZhu,GeZhang,etal.2025.
TowardsPersonalizedDeepResearch:BenchmarksandEvaluations.arXivpreprintarXiv:2509.25106(2025).
[100] Chin-YewLin.2004.Rouge:Apackageforautomaticevaluationofsummaries.InTextsummarizationbranchesout.74–81.
[101] BinwenLiu,JiexiGe,andJiaminWang.2025.Vaiage:AMulti-AgentSolutiontoPersonalizedTravelPlanning.arXivpreprintarXiv:2505.10922
(2025).
[102] JieLiu,WenxuanWang,ZizhanMa,GuolinHuang,YihangSU,Kao-JungChang,WentingChen,HaoliangLi,LinlinShen,andMichaelLyu.
2024.Medchain:Bridgingthegapbetweenllmagentsandclinicalpracticethroughinteractivesequentialbenchmarking.arXivpreprint
arXiv:2412.01605(2024).
[103] LeiLiu,XiaoyanYang,YueShen,BinbinHu,ZhiqiangZhang,JinjieGu,andGuannanZhang.2023. Think-in-memory:Recallingand
post-thinkingenablellmswithlong-termmemory.arXivpreprintarXiv:2311.08719(2023).
[104] NaLiu,LiangyuChen,XiaoyuTian,WeiZou,KaijiangChen,andMingCui.2024.Fromllmtoconversationalagent:Amemoryenhanced
architecturewithfine-tuningoflargelanguagemodels.arXivpreprintarXiv:2401.02777(2024).
[105] SiyuanLiu,WenjingLiu,ZhiweiXu,XinWang,BoChen,andTaoLi.2025. TowardsMitigationofHallucinationforLLM-empowered
Agents:ProgressiveGeneralizationBoundExplorationandWatchdogMonitor.arXivpreprintarXiv:2507.15903(2025).
[106] TianjianLiu,HongzhengZhao,YuhengLiu,XingboWang,andZhenhuiPeng.2024. Compeer:Agenerativeconversationalagentfor
proactivepeersupport.InProceedingsofthe37thAnnualACMSymposiumonUserInterfaceSoftwareandTechnology.1–22.
[107] WenTaoLiu,RuohuaZhang,AiminZhou,FengGao,andJiaLiLiu.2025.Echo:Alargelanguagemodelwithtemporalepisodicmemory.
arXivpreprintarXiv:2502.16090(2025).
[108] YuhanLiu,MichaelJQZhang,andEunsolChoi.2025.UserFeedbackinHuman-LLMDialogues:ALenstoUnderstandUsersButNoisyasa
LearningSignal.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.2666–2681.
[109] LinLong,YichenHe,WentaoYe,YiyuanPan,YuanLin,HangLi,JunboZhao,andWeiLi.2025. Seeing,listening,remembering,and
reasoning:Amultimodalagentwithlong-termmemory.arXivpreprintarXiv:2508.09736(2025).
[110] JunyuLuo,WeizhiZhang,YeYuan,YushengZhao,JunweiYang,YiyangGu,BohanWu,BinqiChen,ZiyueQiao,QingqingLong,etal.2025.
Largelanguagemodelagent:Asurveyonmethodology,applicationsandchallenges.arXivpreprintarXiv:2503.21460(2025).
[111] YitongLuo,HouHeiLam,ZiangChen,ZhenliangZhang,andXueFeng.2025. ValuePilot:ATwo-PhaseFrameworkforValue-Driven
Decision-Making.arXivpreprintarXiv:2503.04569(2025).
[112] ChenhanLyu,YutongSong,PengfeiZhang,andAmirMRahmani.2025.Domain-SpecificConstitutionalAI:EnhancingSafetyinLLM-
PoweredMentalHealthChatbots.arXivpreprintarXiv:2509.16444(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

30 • Y.Xuetal.
[113] YiboLyu,GongweiChen,RuiShao,WeiliGuan,andLiqiangNie.2026.PersonalAlign:HierarchicalImplicitIntentAlignmentforPersonalized
GUIAgentwithLong-TermUser-CentricRecords.arXivpreprintarXiv:2601.09636(2026).
[114] AdyashaMaharana,Dong-HoLee,SergeyTulyakov,MohitBansal,FrancescoBarbieri,andYuweiFang.2024.Evaluatingverylong-term
conversationalmemoryofllmagents.InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume
1:LongPapers).13851–13870.
[115] WenyuMao,JiancanWu,WeijianChen,ChongmingGao,XiangWang,andXiangnanHe.2025.Reinforcedpromptpersonalizationfor
recommendationwithlargelanguagemodels.ACMTransactionsonInformationSystems43,3(2025),1–27.
[116] RezaYousefiMaragheh,PratheekVadla,PriyankGupta,KaiZhao,AysenurInan,KehuiYao,JianpengXu,PraveenKanumala,JasonCho,and
SushantKumar.2025.ARAG:AgenticRetrievalAugmentedGenerationforPersonalizedRecommendation.arXivpreprintarXiv:2506.21931
(2025).
[117] MariaEmiliaMazzolenisandRuiruiZhang.2025.Agentwarpp:Workflowadherenceviaruntimeparallelpersonalization.arXivpreprint
arXiv:2507.19543(2025).
[118] Inc.Mem.2023.Mem—mem.ai.https://mem.ai/.
[119] memodb.2025.GitHub-memodb-io/memobase:Profile-BasedLong-TermMemoryforAIApplications.Memobasehandlesuserprofiles,
memoryevents,andevolvingcontext—perfectforchatbots,companions,tutors,customerservicebots,andallchat-basedagents.—
github.com.https://github.com/memodb-io/memobase.
[120] FengranMo,YuchenHui,YuxingTian,ZhaoxuanTan,ChuanMeng,ZhanSu,KaiyuHuang,andJian-YunNie.2025.Towardsadaptive
personalizedconversationalinformationretrieval.InProceedingsofthe34thACMInternationalConferenceonInformationandKnowledge
Management.2137–2147.
[121] NiklasMuennighoff,ZitongYang,WeijiaShi,XiangLisaLi,LiFei-Fei,HannanehHajishirzi,LukeZettlemoyer,PercyLiang,Emmanuel
Candès,andTatsunoriBHashimoto.2025. s1:Simpletest-timescaling.InProceedingsofthe2025ConferenceonEmpiricalMethodsin
NaturalLanguageProcessing.20286–20332.
[122] SubhabrataMukherjee,PaulGamble,MarkelSanzAusin,NeelKant,KritiAggarwal,NehaManjunath,DebajyotiDatta,Zhengliang
Liu,JiayuanDing,SophiaBusacca,etal.2024. Polaris:Asafety-focusedllmconstellationarchitectureforhealthcare. arXivpreprint
arXiv:2403.13313(2024).
[123] SrijaMukhopadhyay,SathwikReddy,ShruthiMuthukumar,JisunAn,andPonnurangamKumaraguru.2025.PrivacyBench:AConversational
BenchmarkforEvaluatingPrivacyinPersonalizedAI.arXivpreprintarXiv:2512.24848(2025).
[124] JohnMurzaku,ZifanLiu,MdMehrabTanjim,VaishnaviMuppala,XiangChen,andYunyaoLi.2025.ECLAIR:EnhancedClarificationfor
InteractiveResponses.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.39.28864–28870.
[125] HyunjiNam,YanmingWan,MickelLiu,JianxunLian,PeterAhnn,andNatashaJaques.2025.Learningtosummarizeuserinformationfor
personalizedreinforcementlearningfromhumanfeedback.arXivpreprintarXiv:2507.13579(2025).
[126] JiayanNan,WenquanMa,WenlongWu,andYizeChen.2025.Nemori:Self-organizingagentmemoryinspiredbycognitivescience.arXiv
preprintarXiv:2508.03341(2025).
[127] VladimirNaumov,DianaZagirova,ShaLin,YupengXie,WenhaoGou,AnatolyUrban,NinaTikhonova,KhadijaAlawi,MikeDurymanov,
FedorGalkin,etal.2025. Doraaiscientist:Multi-agentvirtualresearchteamforscientificexplorationdiscoveryandautomatedreport
generation.bioRxiv(2025).
[128] LewisNewshamandDanielPrince.2025.Personality-DrivenDecisionMakinginLLM-BasedAutonomousAgents.InProceedingsofthe
24thInternationalConferenceonAutonomousAgentsandMultiagentSystems.1538–1547.
[129] LinNing,LuyangLiu,JiaxingWu,NeoWu,DevoraBerlowitz,SushantPrakash,BradleyGreen,ShawnO’Banion,andJunXie.2025.User-llm:
Efficientllmcontextualizationwithuserembeddings.InCompanionProceedingsoftheACMonWebConference2025.1219–1223.
[130] WenyuNing,ShaotaoShi,YuchenYin,ZixuanGuo,andJinrongXie.2025.Intent-awarepersonalizedsummarizationforeducationaltexts
withlargelanguagemodels.JournalofKingSaudUniversityComputerandInformationSciences37,9(2025),308.
[131] Inc.NotionLabs.2023.NotionAI—notion.com/product/ai.https://www.notion.com/product/ai.
[132] RodrigoNovelo,RodrigoRochaSilva,andJorgeBernardino.2025.ALiteratureReviewofPersonalizedLargeLanguageModelsforEmail
GenerationandAutomation.FutureInternet17,12(2025),536.
[133] FelixOcker,JörgDeigmöller,PavelSmirnov,andJulianEggert.2025. Agroundedmemorysystemforsmartpersonalassistants. arXiv
preprintarXiv:2505.06328(2025).
[134] OpenAI.2022.ChatGPT—chatgpt.com.https://chatgpt.com/.
[135] EgorPakhomov,ErikNijkamp,andCaimingXiong.2025.ConvomemBenchmark:WhyYourFirst150ConversationsDon’tNeedRAG.
arXivpreprintarXiv:2511.10523(2025).
[136] ZhuoshiPan,QianhuiWu,HuiqiangJiang,XufangLuo,HaoCheng,DongshengLi,YuqingYang,Chin-YewLin,HVickyZhao,LiliQiu,
etal.2025.Onmemoryconstructionandretrievalforpersonalizedconversationalagents.arXivpreprintarXiv:2502.05589(2025).
[137] KishorePapineni,SalimRoukos,ToddWard,andWei-JingZhu.2002.Bleu:amethodforautomaticevaluationofmachinetranslation.In
Proceedingsofthe40thannualmeetingoftheAssociationforComputationalLinguistics.311–318.
[138] ChanghuaPei,YiZhang,YongfengZhang,FeiSun,XiaoLin,HanxiaoSun,JianWu,PengJiang,JunfengGe,WenwuOu,etal.2019.
Personalizedre-rankingforrecommendation.InProceedingsofthe13thACMconferenceonrecommendersystems.3–11.
[139] QiyaoPeng,HongtaoLiu,HuaHuang,QingYang,andMinglaiShao.2025. Asurveyonllm-poweredagentsforrecommendersystems.
arXivpreprintarXiv:2502.10050(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 31
[140] MathisPink,QinyuanWu,VyAiVo,JavierTurek,JianingMu,AlexanderHuth,andMariyaToneva.2025.Position:EpisodicMemoryisthe
MissingPieceforLong-TermLLMAgents.arXivpreprintarXiv:2502.06975(2025).
[141] SriyashPoddar,YanmingWan,HamishIvison,AbhishekGupta,andNatashaJaques.2024. Personalizingreinforcementlearningfrom
humanfeedbackwithvariationalpreferencelearning.AdvancesinNeuralInformationProcessingSystems37(2024),52516–52544.
[142] Predis.ai.2023.Predis.ai—predis.ai.https://predis.ai/.
[143] ChengQian,EmreCanAcikgoz,HongruWang,XiusiChen,AvirupSil,DilekHakkani-Tur,GokhanTur,andHengJi.2025. SMART:
Self-awareagentfortooloverusemitigation.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.4604–4621.
[144] HongjinQian,ZhengLiu,PeitianZhang,KelongMao,DefuLian,ZhichengDou,andTiejunHuang.2025.Memorag:Boostinglongcontext
processingwithglobalmemory-enhancedretrievalaugmentation.InProceedingsoftheACMonWebConference2025.2366–2377.
[145] TianQin,FelixBai,Ting-YaoHu,RavitejaVemulapalli,HemaSwethaKoppula,ZhiyangXu,BowenJin,MertCemri,JiaruiLu,ZiruiWang,
etal.2025.COMPASS:AMulti-TurnBenchmarkforTool-MediatedPlanning&PreferenceOptimization.arXivpreprintarXiv:2510.07043
(2025).
[146] YilunQiu,TianhaoShi,XiaoyanZhao,FengbinZhu,YangZhang,andFuliFeng.2025. Latentinter-userdifferencemodelingforllm
personalization.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.10610–10628.
[147] YilunQiu,XiaoyanZhao,YangZhang,YimengBai,WenjieWang,HongCheng,FuliFeng,andTat-SengChua.2025. Measuringwhat
makesyouunique:Difference-awareusermodelingforenhancingllmpersonalization.InFindingsoftheAssociationforComputational
Linguistics:ACL2025.21258–21277.
[148] ChangleQu,SunhaoDai,XiaochiWei,HengyiCai,ShuaiqiangWang,DaweiYin,JunXu,andJi-RongWen.2025.Toollearningwithlarge
languagemodels:Asurvey.FrontiersofComputerScience19,8(2025),198343.
[149] StevenJigeQuanandSeojungLee.2025.EnhancingparticipatoryplanningwithChatGPT-assistedplanningsupportsystems:ahypothetical
casestudyinSeoul.InternationalJournalofUrbanSciences29,1(2025),89–122.
[150] PrestonRasmussen,PavloPaliychuk,TravisBeauvais,JackRyan,andDanielChalef.2025.Zep:atemporalknowledgegrapharchitecture
foragentmemory.arXivpreprintarXiv:2501.13956(2025).
[151] Replika.[n.d.].Replika—replika.com.https://replika.com/.
[152] AlirezaRezazadeh,ZichaoLi,WeiWei,andYujiaBao.2024.Fromisolatedconversationstohierarchicalschemas:Dynamictreememory
representationforllms.arXivpreprintarXiv:2410.14052(2024).
[153] StephenRobertson,HugoZaragoza,etal.2009.Theprobabilisticrelevanceframework:BM25andbeyond.FoundationsandTrends®in
InformationRetrieval3,4(2009),333–389.
[154] RanaSalama,JasonCai,MichelleYuan,AnnaCurrey,MonicaSunkara,YiZhang,andYassineBenajiba.2025.Meminsight:Autonomous
memoryaugmentationforllmagents.arXivpreprintarXiv:2503.21760(2025).
[155] AlirezaSalemi,ChengLi,MingyangZhang,QiaozhuMei,WeizeKong,TaoChen,ZhuowanLi,MichaelBendersky,andHamedZamani.
2025.Reasoning-EnhancedSelf-TrainingforLong-FormPersonalizedTextGeneration.arXivpreprintarXiv:2501.04167(2025).
[156] AlirezaSalemi,ShesheraMysore,MichaelBendersky,andHamedZamani.2024.Lamp:Whenlargelanguagemodelsmeetpersonalization.
InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).7370–7392.
[157] AlirezaSalemiandHamedZamani.2025.Lamp-qa:Abenchmarkforpersonalizedlong-formquestionanswering.InProceedingsofthe
2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.1139–1159.
[158] Salesforge.2023.SalesforgeAI—salesforge.ai.https://www.salesforge.ai/.
[159] RohanCharudattSalvi,ChiragChawla,DhruvJain,SwapnilPanigrahi,MdShadAkhtar,andShwetaYadav.2025.PERCS:Persona-Guided
ControllableBiomedicalSummarizationDataset.arXivpreprintarXiv:2512.03340(2025).
[160] ParthSarthi,SalmanAbdullah,AditiTuli,ShubhKhanna,AnnaGoldie,andChristopherDManning.2024.Raptor:Recursiveabstractive
processingfortree-organizedretrieval.InTheTwelfthInternationalConferenceonLearningRepresentations.
[161] KrishnaSayana,RaghavendraVasudeva,YuriVasilevski,KunSu,LiamHebert,JamesPine,HubertPham,AmbarishJash,andSukhdeep
Sodhi.2025.BeyondRetrieval:GeneratingNarrativesinConversationalRecommenderSystems.InCompanionProceedingsoftheACMon
WebConference2025.2411–2420.
[162] SamuelSchmidgall,YushengSu,ZeWang,XimengSun,JialianWu,XiaodongYu,JiangLiu,MichaelMoor,ZichengLiu,andEmadBarsoum.
2025.Agentlaboratory:Usingllmagentsasresearchassistants.FindingsoftheAssociationforComputationalLinguistics:EMNLP2025
(2025),5977–6043.
[163] SamuelSchmidgall,RojinZiaei,CarlHarris,EduardoReis,JeffreyJopling,andMichaelMoor.2024. AgentClinic:amultimodalagent
benchmarktoevaluateAIinsimulatedclinicalenvironments.arXivpreprintarXiv:2405.07960(2024).
[164] YuShang,PeijieLiu,YuweiYan,ZijingWu,LehengSheng,YuanqingYu,ChumengJiang,AnZhang,FengliXu,YuWang,etal.2025.
Agentrecbench:Benchmarkingllmagent-basedpersonalizedrecommendersystems.arXivpreprintarXiv:2505.19623(2025).
[165] ZijianShao,JiancanWu,WeijianChen,andXiangWang.2025. PersonalTravelSolver:APreference-DrivenLLM-SolverSystemfor
TravelPlanning.InProceedingsofthe63rdAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).
27622–27642.
[166] SahilSharma,PuneetMittal,MukeshKumar,andVivekBhardwaj.2025. Theroleoflargelanguagemodelsinpersonalizedlearning:a
systematicreviewofeducationalimpact.DiscoverSustainability6,1(2025),1–24.
[167] ZhuochengShen.2024.Llmwithtools:Asurvey.arXivpreprintarXiv:2409.18807(2024).
[168] IdanShenfeld,FelixFaltings,PulkitAgrawal,andAldoPacchiano.2025.Languagemodelpersonalizationviarewardfactorization.arXiv
preprintarXiv:2503.06358(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

32 • Y.Xuetal.
[169] TengShi,JunXu,XiaoZhang,XiaoxueZang,KaiZheng,YangSong,andHanLi.2025.Retrievalaugmentedgenerationwithcollaborative
filteringforpersonalizedtextgeneration.InProceedingsofthe48thInternationalACMSIGIRConferenceonResearchandDevelopment
inInformationRetrieval.1294–1304.
[170] WenqiShi,RanXu,YuchenZhuang,YueYu,JieyuZhang,HangWu,YuandaZhu,JoyceCHo,CarlYang,andMayDongmeiWang.2024.
Ehragent:Codeempowerslargelanguagemodelsforfew-shotcomplextabularreasoningonelectronichealthrecords.InProceedingsof
the2024ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.22315–22339.
[171] YunxiaoShi,HaoningShang,XingZi,WujiangXu,YueFeng,andMinXu.2025.AnsweringNarrative-DrivenRecommendationQueries
viaaRetrieve–RankParadigmandtheOCG-Agent.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguage
Processing.13192–13213.
[172] YunxiaoShi,WujiangXu,ZhangZeqi,XingZi,QiangWu,andMinXu.2025.PersonaX:Arecommendationagent-orientedusermodeling
frameworkforlongbehaviorsequence.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.5764–5787.
[173] DonghoonShin,GaryHsieh,andYoung-HoKim.2025.PlanFitting:PersonalizedExercisePlanningwithLargeLanguageModel-driven
ConversationalAgent.InProceedingsofthe7thACMConferenceonConversationalUserInterfaces.1–19.
[174] NoahShinn,FedericoCassano,AshwinGopinath,KarthikNarasimhan,andShunyuYao.2023. Reflexion:Languageagentswithverbal
reinforcementlearning.AdvancesinNeuralInformationProcessingSystems36(2023),8634–8652.
[175] AnikaitSingh,SherylHsu,KyleHsu,EricMitchell,StefanoErmon,TatsunoriHashimoto,ArchitSharma,andChelseaFinn.2025.Fspo:Few-
shotpreferenceoptimizationofsyntheticpreferencedatainllmselicitseffectivepersonalizationtorealusers.arXivpreprintarXiv:2502.19312
(2025).
[176] HarmanpreetSingh,NikhilVerma,YixiaoWang,ManasaBharadwaj,HomaFashandi,KevinFerreira,andChulLee.2024.Personallarge
languagemodelagents:Acasestudyontailoredtravelplanning.InProceedingsofthe2024ConferenceonEmpiricalMethodsinNatural
LanguageProcessing:IndustryTrack.486–514.
[177] YutongSong,JiangWu,WeijiaZhang,ChengzeShen,ShaofanYuan,WeitaoLu,JianWang,AmirRahmani,NikilDutt,andYuWang.2026.
CARD:Cluster-levelAdaptationwithReward-guidedDecodingforPersonalizedTextGeneration.arXivpreprintarXiv:2601.06352(2026).
[178] PaoloSorino,GiovanniMariaBiancofiore,DomenicoLofù,TommasoColafiglio,AngelaLombardi,FedelucioNarducci,andTommaso
DiNoia.2024.Ariel:Brain-computerinterfacesmeetlargelanguagemodelsforemotionalsupportconversation.InAdjunctProceedingsof
the32ndACMConferenceonUserModeling,AdaptationandPersonalization.601–609.
[179] JunhaoSu,YuanliangWan,JunweiYang,HengyuShi,TianyangHan,JunfengLuo,andYuruiQiu.2025.Failuremakestheagentstronger:
Enhancingaccuracythroughstructuredreflectionforreliabletoolinteractions.arXivpreprintarXiv:2509.18847(2025).
[180] ChenkaiSun,KeYang,RevanthGangiReddy,YiFung,HouPongChan,KevinSmall,ChengXiangZhai,andHengJi.2025. Persona-db:
Efficientlargelanguagemodelpersonalizationforresponsepredictionwithcollaborativedatarefinement.InProceedingsofthe31st
InternationalConferenceonComputationalLinguistics.281–296.
[181] HaotianSun,YuchenZhuang,LingkaiKong,BoDai,andChaoZhang.2023.Adaplanner:Adaptiveplanningfromfeedbackwithlanguage
models.Advancesinneuralinformationprocessingsystems36(2023),58202–58245.
[182] WeiweiSun,XuhuiZhou,WeihuaDu,XingyaoWang,SeanWelleck,GrahamNeubig,MaartenSap,andYimingYang.2025. Training
proactiveandpersonalizedllmagents.arXivpreprintarXiv:2511.02208(2025).
[183] MananSuri,PuneetMathur,NedimLipka,FranckDernoncourt,RyanARossi,andDineshManocha.2025.StructuredUncertaintyguided
ClarificationforLLMAgents.arXivpreprintarXiv:2511.08798(2025).
[184] TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,andIadhOunis.2025. AregenerativeAIagentseffec-
tivepersonalizedfinancialadvisors?.InProceedingsofthe48thInternationalACMSIGIRConferenceonResearchandDevelopmentin
InformationRetrieval.286–295.
[185] TakehiroTakayanagi,MasahiroSuzuki,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,andIadhOunis.2025. FinPersona:An
LLM-DrivenConversationalAgentforPersonalizedFinancialAdvising.InEuropeanConferenceonInformationRetrieval.Springer,13–18.
[186] JuntaoTan,LiangweiYang,ZuxinLiu,ZhiweiLiu,RitheshRN,TulikaManojAwalgaonkar,JianguoZhang,WeiranYao,MingZhu,Shirley
Kokane,etal.2025.Personabench:Evaluatingaimodelsonunderstandingpersonalinformationthroughaccessing(synthetic)privateuser
data.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.878–893.
[187] ZhenTan,JunYan,IHsu,RujunHan,ZifengWang,LongTLe,YiwenSong,YanfeiChen,HamidPalangi,GeorgeLee,etal.2025.Inprospect
andretrospect:Reflectivememorymanagementforlong-termpersonalizeddialogueagents.arXivpreprintarXiv:2503.08026(2025).
[188] ZhaoxuanTan,ZixuanZhang,HaoyangWen,ZhengLi,RongzhiZhang,PeiChen,FengranMo,ZheyuanLiu,QingkaiZeng,QingyuYin,
etal.2025.InstantPersonalizedLargeLanguageModelAdaptationviaHypernetwork.arXivpreprintarXiv:2510.16282(2025).
[189] JiakaiTang,SunhaoDai,TengShi,JunXu,XuChen,WenChen,JianWu,andYuningJiang.2025.Thinkbeforerecommend:Unleashingthe
latentreasoningpowerforsequentialrecommendation.arXivpreprintarXiv:2503.22675(2025).
[190] MeilingTao,ChenghaoZhu,DongyiDing,TiannanWang,YuchenEleanorJiang,andWangchunshuZhou.2025. PersonaFeedback:A
Large-scaleHuman-annotatedBenchmarkForPersonalization.arXivpreprintarXiv:2506.12915(2025).
[191] AoTian,YunfengLu,XinxinFan,ChanghaoWang,LanzhiZhou,YeyaoZhang,andYanfangLiu.2025.Rgmem:Renormalizationgroup-based
memoryevolutionforlanguageagentuserprofile.arXivpreprintarXiv:2510.16392(2025).
[192] Khanh-TungTran,DungDao,Minh-DuongNguyen,Quoc-VietPham,BarryO’Sullivan,andHoangDNguyen.2025.Multi-agentcollaboration
mechanisms:Asurveyofllms.arXivpreprintarXiv:2501.06322(2025).
[193] IoannisTsaknakis,BingqingSong,ShuyuGan,DongyeopKang,AlfredoGarcia,GaowenLiu,CharlesFleming,andMingyiHong.2025.
DoLLMsRecognizeYourLatentPreferences?ABenchmarkforLatentInformationDiscoveryinPersonalizedInteraction.arXivpreprint
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 33
arXiv:2510.17132(2025).
[194] Yu-MinTseng,Yu-ChaoHuang,Teng-YunHsiao,Wei-LinChen,Chao-WeiHuang,YuMeng,andYun-NungChen.2024. Twotalesof
personainllms:Asurveyofrole-playingandpersonalization.arXivpreprintarXiv:2406.01171(2024).
[195] KentaroUedaandTakehiroTakayanagi.2025.PREFINE:PersonalizedStoryGenerationviaSimulatedUserCriticsandUser-SpecificRubric
Generation.arXivpreprintarXiv:2510.21721(2025).
[196] HarshVishwakarma,AnkushAgarwal,OjasPatil,ChaitanyaDevaguptapu,andMaheshChandran.2025.CanLLMsHelpYouatWork?A
SandboxforEvaluatingLLMAgentsinEnterpriseEnvironments.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNatural
LanguageProcessing.9178–9212.
[197] YanmingWan,JiaxingWu,MarwaAbdulhai,LiorShani,andNatashaJaques.2025. EnhancingPersonalizedMulti-TurnDialoguewith
CuriosityReward.arXivpreprintarXiv:2504.03206(2025).
[198] DanqingWang,KevinYang,HanlinZhu,XiaomengYang,AndrewCohen,LeiLi,andYuandongTian.2024.Learningpersonalizedalignment
forevaluatingopen-endedtextgeneration.InProceedingsofthe2024ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.
13274–13292.
[199] HongruWang,MindaHu,YangDeng,RuiWang,FeiMi,WeichaoWang,YashengWang,Wai-ChungKwan,IrwinKing,andKam-Fai
Wong.2023.Largelanguagemodelsassourceplannerforpersonalizedknowledge-groundeddialogues.InFindingsoftheAssociationfor
ComputationalLinguistics:EMNLP2023.9556–9569.
[200] HongruWang,WenyuHuang,YangDeng,RuiWang,ZezhongWang,YufeiWang,FeiMi,JeffZPan,andKam-FaiWong.2024.Unims-rag:
Aunifiedmulti-sourceretrieval-augmentedgenerationforpersonalizeddialoguesystems.arXivpreprintarXiv:2401.13256(2024).
[201] HanpengWangandZijiangYang.2025.AMulti-AgentApproachtoInvestorProfilingUsingLargeLanguageModels.In2025International
ConferenceonControl,AutomationandDiagnosis(ICCAD).IEEE,1–6.
[202] KuanWang,YadongLu,MichaelSantacroce,YeyunGong,ChaoZhang,andYelongShen.2023.Adaptingllmagentswithuniversalfeedback
incommunication.arXivpreprintarXiv:2310.01444(2023).
[203] KaiminWang,YuanzheShen,ChangzeLv,XiaoqingZheng,andXuanjingHuang.2025.TripTailor:AReal-WorldBenchmarkforPersonalized
TravelPlanning.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.AssociationforComputationalLinguistics,Vienna,
Austria,9705–9723.doi:10.18653/v1/2025.findings-acl.503
[204] LeiWang,ChenMa,XueyangFeng,ZeyuZhang,HaoYang,JingsenZhang,ZhiyuanChen,JiakaiTang,XuChen,YankaiLin,etal.2024.A
surveyonlargelanguagemodelbasedautonomousagents.FrontiersofComputerScience18,6(2024),186345.
[205] LeiWang,JingsenZhang,HaoYang,Zhi-YuanChen,JiakaiTang,ZeyuZhang,XuChen,YankaiLin,HaoSun,RuihuaSong,etal.2025.User
behaviorsimulationwithlargelanguagemodel-basedagents.ACMTransactionsonInformationSystems43,2(2025),1–37.
[206] ShuoxinWang,ChangLiu,GowenLoo,LifanZheng,KaiwenWei,XinyiZeng,JingyuanZhang,andYuTian.2026.Me-Agent:APersonalized
MobileAgentwithTwo-LevelUserHabitLearningforEnhancedInteraction.arXivpreprintarXiv:2601.20162(2026).
[207] TianzeWang,DongnanGui,YifanHu,ShuhangLin,andLinjunZhang.2025. Mpo:Anefficientpost-processingframeworkformixing
diversepreferencealignment.arXivpreprintarXiv:2502.18699(2025).
[208] WenxuanWang,ZizhanMa,ZhengWang,ChenghanWu,JiamingJi,WentingChen,XiangLi,andYixuanYuan.2025.Asurveyofllm-based
agentsinmedicine:Howfararewefrombaymax?arXivpreprintarXiv:2502.11211(2025).
[209] YuWangandXiChen.2025.Mirix:Multi-agentmemorysystemforllm-basedagents.arXivpreprintarXiv:2507.07957(2025).
[210] YuxinWang,YiranGuo,YiningZheng,ZhangyueYin,ShuoChen,JieYang,JiajunChen,YuanLi,XuanjingHuang,andXipengQiu.2025.
FamilyTool:AMulti-hopPersonalizedToolUseBenchmark.arXivpreprintarXiv:2504.06766(2025).
[211] YuWang,DmitryKrotov,YuanzheHu,YifanGao,WangchunshuZhou,JulianMcAuley,DanGutfreund,RogerioFeris,andZexueHe.2025.
M+:ExtendingMemoryLLMwithScalableLong-TermMemory.arXivpreprintarXiv:2502.00592(2025).
[212] YuWang,XinshuangLiu,XiusiChen,SeanO’Brien,JundaWu,andJulianMcAuley.2024.Self-updatablelargelanguagemodelsbyintegrating
contextintomodelparameters.arXivpreprintarXiv:2410.00487(2024).
[213] YuWang,RyuichiTakanobu,ZhiqiLiang,YuzhenMao,YuanzheHu,JulianMcAuley,andXiaojianWu.2025.Mem-{\alpha}:Learning
MemoryConstructionviaReinforcementLearning.arXivpreprintarXiv:2509.25911(2025).
[214] ZhefanWang,YuanqingYu,WendiZheng,WeizhiMa,andMinZhang.2024. Macrec:Amulti-agentcollaborationframeworkfor
recommendation.InProceedingsofthe47thInternationalACMSIGIRConferenceonResearchandDevelopmentinInformationRetrieval.
2760–2764.
[215] ZixiangWang,YinghaoZhu,HuiyaZhao,XiaochenZheng,DehaoSui,TianlongWang,WenTang,YashaWang,EwenHarrison,Chengwei
Pan,etal.2025.Colacare:Enhancingelectronichealthrecordmodelingthroughlargelanguagemodel-drivenmulti-agentcollaboration.In
ProceedingsoftheACMonWebConference2025.2250–2261.
[216] AzmineToushikWasi,WahidFaisal,andMstRafiaIslam.2025.Mina:AMultilingualLLM-PoweredLegalAssistantAgentforBangladesh
forEmpoweringAccesstoJustice.arXivpreprintarXiv:2511.08605(2025).
[217] HuiWei,ZihaoZhang,ShenghuaHe,TianXia,ShijiaPan,andFeiLiu.2025.Plangenllms:Amodernsurveyofllmplanningcapabilities.In
Proceedingsofthe63rdAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).19497–19521.
[218] LilianWeng.2023.LLM-poweredAutonomousAgents.lilianweng.github.io(Jun2023). https://lilianweng.github.io/posts/2023-06-23-agent/
[219] RebeccaWesthäußer,FrederikBerenz,WolfgangMinker,andSebastianZepf.2025.CAIM:DevelopmentandEvaluationofaCognitiveAI
MemoryFrameworkforLong-TermInteractionwithIntelligentAgents.arXivpreprintarXiv:2505.13044(2025).
[220] RebeccaWesthäußer,WolfgangMinker,andSebatianZepf.2025. EnablingPersonalizedLong-termInteractionsinLLM-basedAgents
throughPersistentMemoryandUserProfiles.arXivpreprintarXiv:2510.07925(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

34 • Y.Xuetal.
[221] BinWu,ZhengyanShi,HosseinARahmani,VarshaRamineni,andEmineYilmaz.2024. Understandingtheroleofuserprofileinthe
personalizationoflargelanguagemodels.arXivpreprintarXiv:2406.17803(2024).
[222] DiWu,HongweiWang,WenhaoYu,YuweiZhang,Kai-WeiChang,andDongYu.2025.LongMemEval:BenchmarkingChatAssistantson
Long-TermInteractiveMemory.InTheThirteenthInternationalConferenceonLearningRepresentations.
[223] JiaxingWu,LinNing,LuyangLiu,HarrisonLee,NeoWu,ChaoWang,SushantPrakash,ShawnO’Banion,BradleyGreen,andJunXie.
2025.Rlpf:Reinforcementlearningfrompredictionfeedbackforusersummarizationwithllms.InProceedingsoftheAAAIConferenceon
ArtificialIntelligence,Vol.39.25488–25496.
[224] QingyunWu,GaganBansal,JieyuZhang,YiranWu,BeibinLi,ErkangZhu,LiJiang,XiaoyunZhang,ShaokunZhang,JialeLiu,etal.2024.
Autogen:Enablingnext-genLLMapplicationsviamulti-agentconversations.InFirstConferenceonLanguageModeling.
[225] ShujinWu,MayFung,ChengQian,JeonghwanKim,DilekHakkani-Tur,andHengJi.2024.Aligningllmswithindividualpreferencesvia
interaction.arXivpreprintarXiv:2410.03642(2024).
[226] YaozuWu,JizhouGuo,DongyuanLi,HenryPengZou,Wei-ChiehHuang,YankaiChen,ZhenWang,WeizhiZhang,YangningLi,Meng
Zhang,etal.2025.Psg-agent:Personality-awaresafetyguardrailforllm-basedagents.arXivpreprintarXiv:2509.23614(2025).
[227] YaxiongWu,ShengLiang,ChenZhang,YichaoWang,YongyueZhang,HuifengGuo,RuimingTang,andYongLiu.2025. Fromhuman
memorytoaimemory:Asurveyonmemorymechanismsintheeraofllms.arXivpreprintarXiv:2504.15965(2025).
[228] YuweiWu,XuezheMa,andDiyiYang.2021. Personalizedresponsegenerationviagenerativesplitmemorynetwork.InProceedings
ofthe2021ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:HumanLanguageTechnologies.
1956–1970.
[229] YuchenWu,EdwardSun,KaijieZhu,JianxunLian,JoseHernandez-Orallo,AylinCaliskan,andJindongWang.2025.PersonalizedSafetyin
LLMs:ABenchmarkandAPlanning-BasedAgentApproach.arXivpreprintarXiv:2505.18882(2025).
[230] YaxiongWu,YongyueZhang,ShengLiang,andYongLiu.2025.Sgmem:Sentencegraphmemoryforlong-termconversationalagents.arXiv
preprintarXiv:2509.21212(2025).
[231] YunjiaXi,WeiwenLiu,JianghaoLin,BoChen,RuimingTang,WeinanZhang,andYongYu.2024.Memocrs:Memory-enhancedsequential
conversationalrecommendersystemswithlargelanguagemodels.InProceedingsofthe33rdACMInternationalConferenceonInformation
andKnowledgeManagement.2585–2595.
[232] YunjiaXi,WeiwenLiu,JiemingZhu,XilongZhao,XinyiDai,RuimingTang,WeinanZhang,RuiZhang,andYongYu.2022. Multi-
levelinteractionrerankingwithuserbehaviorhistory.InProceedingsofthe45thInternationalACMSIGIRConferenceonResearchand
DevelopmentinInformationRetrieval.1336–1346.
[233] DerongXu,YiWen,PengyueJia,YingyiZhang,YichaoWang,HuifengGuo,RuimingTang,XiangyuZhao,EnhongChen,TongXu,etal.
2025.Towardsmulti-granularitymemoryassociationandselectionforlong-termconversationalagents.arXivpreprintarXiv:2505.19549
(2025).
[234] ManjieXu,XinyiYang,WeiLiang,ChiZhang,andYixinZhu.2025. LearningtoPlanwithPersonalizedPreferences. arXivpreprint
arXiv:2502.00858(2025).
[235] QianchengXu,YongqiLi,HemingXia,FanLiu,MinYang,andWenjieLi.2025. Petoolllm:Towardspersonalizedtoollearninginlarge
languagemodels.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.21488–21503.
[236] SonglinXu,XinyuZhang,andLianhuiQin.2024.Eduagent:Generativestudentagentsinlearning.arXivpreprintarXiv:2404.07963(2024).
[237] WujiangXu,ZujieLiang,KaiMei,HangGao,JuntaoTan,andYongfengZhang.2025. A-mem:Agenticmemoryforllmagents. arXiv
preprintarXiv:2502.12110(2025).
[238] XinchaoXu,ZhibinGou,WenquanWu,Zheng-YuNiu,HuaWu,HaifengWang,andShihangWang.2022.Longtimenosee!open-domain
conversationwithlong-termpersonamemory.InFindingsoftheAssociationforComputationalLinguistics:ACL2022.2639–2650.
[239] YangyangXu,JinpengHu,ZhuoerZhao,ZhanglingDuan,XiaoSun,andXunYang.2025. MultiAgentESC:ALLM-basedMulti-Agent
CollaborationFrameworkforEmotionalSupportConversation.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNatural
LanguageProcessing.4665–4681.
[240] YiyanXu,JinghaoZhang,AlirezaSalemi,XintingHu,WenjieWang,FuliFeng,HamedZamani,XiangnanHe,andTat-SengChua.2025.
Personalizedgenerationinlargemodelera:Asurvey.arXivpreprintarXiv:2503.02614(2025).
[241] SikuanYan,XiufengYang,ZuchaoHuang,ErcongNie,ZifengDing,ZonggenLi,XiaowenMa,KristianKersting,JeffZPan,HinrichSchütze,
etal.2025.Memory-r1:Enhancinglargelanguagemodelagentstomanageandutilizememoriesviareinforcementlearning.arXivpreprint
arXiv:2508.19828(2025).
[242] YiboYan,ShenWang,JiahaoHuo,PhilipSYu,XumingHu,andQingsongWen.2025. Mathagent:Leveragingamixture-of-math-agent
frameworkforreal-worldmultimodalmathematicalerrordetection.InProceedingsofthe63rdAnnualMeetingoftheAssociationfor
ComputationalLinguistics(Volume6:IndustryTrack).69–82.
[243] HongyangYang,BoyuZhang,NengWang,ChengGuo,XiaoliZhang,LikunLin,JunlinWang,TianyuZhou,MaoGuan,RunjiaZhang,etal.
2024.Finrobot:Anopen-sourceaiagentplatformforfinancialapplicationsusinglargelanguagemodels.arXivpreprintarXiv:2405.14767
(2024).
[244] YandanYang,BaoxiongJia,ShujieZhang,andSiyuanHuang.2025. Sceneweaver:All-in-one3dscenesynthesiswithanextensibleand
self-reflectiveagent.arXivpreprintarXiv:2509.20414(2025).
[245] ChaerinYu,ChihunChoi,SunjaeLee,HyosuKim,StevenYKo,Young-BaeKo,andSangeunOh.2026.LeveragingLLMsforEfficientand
PersonalizedSmartHomeAutomation.arXivpreprintarXiv:2601.04680(2026).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 35
[246] ShuoYu,MingyueCheng,DaoyuWang,QiLiu,ZiruiLiu,ZeGuo,andXiaoyuTao.2025.MemWeaver:AHierarchicalMemoryfromTextual
InteractiveBehaviorsforPersonalizedGeneration.arXivpreprintarXiv:2510.07713(2025).
[247] RuifengYuan,ShichaoSun,YongqiLi,ZiliWang,ZiqiangCao,andWenjieLi.2025.PersonalizedLargeLanguageModelAssistantwith
EvolvingConditionalMemory.InProceedingsofthe31stInternationalConferenceonComputationalLinguistics.
[248] SaberZerhoudiandMichaelGranitzer.2024. Personarag:Enhancingretrieval-augmentedgenerationsystemswithuser-centricagents.
arXivpreprintarXiv:2407.09394(2024).
[249] CongZhang,XinDeikGoh,DexunLi,HaoZhang,andYongLiu.2025.Planningwithmulti-constraintsviacollaborativelanguageagents.
InProceedingsofthe31stInternationalConferenceonComputationalLinguistics.10054–10082.
[250] JunjieZhang,YupengHou,RuobingXie,WenqiSun,JulianMcAuley,WayneXinZhao,LeyuLin,andJi-RongWen.2024. Agentcf:
Collaborativelearningwithautonomouslanguageagentsforrecommendersystems.InProceedingsoftheACMWebConference2024.
3679–3689.
[251] JiayiZhang,JinyuXiang,ZhaoyangYu,FengweiTeng,XionghuiChen,JiaqiChen,MingchenZhuge,XinCheng,SiruiHong,JinlinWang,
etal.2024.Aflow:Automatingagenticworkflowgeneration.arXivpreprintarXiv:2410.10762(2024).
[252] KaiZhang,XinyuanZhang,EjazAhmed,HongdaJiang,CalebKumar,KaiSun,ZhaojiangLin,SanatSharma,ShereenOraby,AaronColak,
etal.2025.AssoMem:ScalableMemoryQAwithMulti-SignalAssociativeRetrieval.arXivpreprintarXiv:2510.10397(2025).
[253] LemeiZhang,PengLiu,MarcusHenriksboe,EvenLauvrak,JonAtleGulla,andHeriRamampiaro.2024.Personalsum:Auser-subjective
guidedpersonalizedsummarizationdatasetforlargelanguagemodels. AdvancesinNeuralInformationProcessingSystems37(2024),
99333–99346.
[254] WeizhiZhang,XinyangZhang,ChenweiZhang,LiangweiYang,JingboShang,ZhepeiWei,HenryPengZou,ZijieHuang,ZhengyangWang,
YifanGao,etal.2025.Personaagent:Whenlargelanguagemodelagentsmeetpersonalizationattesttime.arXivpreprintarXiv:2506.06254
(2025).
[255] XuanZhang,YangDeng,ZifengRen,SeeKiongNg,andTat-SengChua.2024.Ask-before-plan:Proactivelanguageagentsforreal-world
planning.InFindingsoftheAssociationforComputationalLinguistics:EMNLP2024.10836–10863.
[256] XinliangFrederickZhang,NickBeauchamp,andLuWang.2025. PRIME:LargeLanguageModelPersonalizationwithCognitiveDual-
MemoryandPersonalizedThoughtProcess.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.
33695–33724.
[257] YingyiZhang,PengyueJia,DerongXu,YiWen,XiannengLi,YichaoWang,WenlinZhang,XiaopengLi,WeinanGan,HuifengGuo,etal.
2025.PersonalizeBeforeRetrieve:LLM-basedPersonalizedQueryExpansionforUser-CentricRetrieval.arXivpreprintarXiv:2510.08935
(2025).
[258] YuZhang,ShutongQiao,JiaqiZhang,Tzu-HengLin,ChenGao,andYongLi.2025.Asurveyoflargelanguagemodelempoweredagentsfor
recommendationandsearch:Towardsnext-generationinformationretrieval.arXivpreprintarXiv:2503.05659(2025).
[259] ZhaoweiZhang,FengshuoBai,QizhiChen,ChengdongMa,MingzhiWang,HaoranSun,ZilongZheng,andYaodongYang.2025.Amulet:
RealignmentduringtesttimeforpersonalizedpreferenceadaptationofLLMs.arXivpreprintarXiv:2502.19148(2025).
[260] ZeyuZhang,QuanyuDai,XiaoheBo,ChenMa,RuiLi,XuChen,JiemingZhu,ZhenhuaDong,andJi-RongWen.2025.Asurveyonthe
memorymechanismoflargelanguagemodel-basedagents.ACMTransactionsonInformationSystems43,6(2025),1–47.
[261] ZhehaoZhang,RyanARossi,BranislavKveton,YijiaShao,DiyiYang,HamedZamani,FranckDernoncourt,JoeBarrow,TongYu,Sungchul
Kim,etal.2024.Personalizationoflargelanguagemodels:Asurvey.arXivpreprintarXiv:2411.00027(2024).
[262] SiyanZhao,MingyiHong,YangLiu,DevamanyuHazarika,andKaixiangLin.2025. Dollmsrecognizeyourpreferences?evaluating
personalizedpreferencefollowinginllms.arXivpreprintarXiv:2502.09597(2025).
[263] WeixiangZhao,XingyuSui,YulinHu,JiaheGuo,HaixiaoLiu,BiyeLi,YanyanZhao,BingQin,andTingLiu.2025. TeachingLanguage
ModelstoEvolvewithUsers:DynamicProfileModelingforPersonalizedAlignment.arXivpreprintarXiv:2505.15456(2025).
[264] XinkuiZhao,HaodeLi,YifanZhang,GuanjieCheng,andYueshenXu.2025.TRAIL:JointInferenceandRefinementofKnowledgeGraphs
withLargeLanguageModels.arXivpreprintarXiv:2508.04474(2025).
[265] ZhengZhao,ClaraVania,SubhradeepKayal,NailaKhan,ShayBCohen,andEmineYilmaz.2025.Personalens:Abenchmarkforpersonal-
izationevaluationinconversationalaiassistants.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.18023–18055.
[266] ArmanZharmagambetov,ChuanGuo,IvanEvtimov,MayaPavlova,RuslanSalakhutdinov,andKamalikaChaudhuri.2025. Agentdam:
Privacyleakageevaluationforautonomouswebagents.arXivpreprintarXiv:2503.09780(2025).
[267] LianminZheng,Wei-LinChiang,YingSheng,SiyuanZhuang,ZhanghaoWu,YonghaoZhuang,ZiLin,ZhuohanLi,DachengLi,Eric
Xing,etal.2023.Judgingllm-as-a-judgewithmt-benchandchatbotarena.Advancesinneuralinformationprocessingsystems36(2023),
46595–46623.
[268] XiZheng,ZhuoyangLi,XinningGui,andYuhanLuo.2025.CustomizingEmotionalSupport:HowDoIndividualsConstructandInteract
WithLLM-PoweredChatbots.InProceedingsoftheExtendedAbstractsoftheCHIConferenceonHumanFactorsinComputingSystems.
[269] WanjunZhong,LianghongGuo,QiqiGao,HeYe,andYanlinWang.2024.Memorybank:Enhancinglargelanguagemodelswithlong-term
memory.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.38.19724–19731.
[270] FilippoZiliotto,JelinRaphaelAkkara,AlessandroDaniele,LambertoBallan,LucianoSerafini,andTommasoCampari.2025. Personal:
Towardsacomprehensivebenchmarkforpersonalizedembodiedagents.arXivpreprintarXiv:2509.19843(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.