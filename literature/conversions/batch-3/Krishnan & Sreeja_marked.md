---
conversion_metadata:
  converted_at: "2026-07-21T13:51:01Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Krishnan & Sreeja.pdf"
  source_pdf_sha256: "b1444e353711bffa56e6a07e972d1c3bb9ea65d2fd701109819219f102606caa"
  page_count: 40
  markdown_char_count: 476866
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 24 April 2026, accepted 13 May 2026, date of publication 20 May 2026, date of current version 27 May 2026.

Digital Object Identifier 10.1109/ACCESS.2026.3695458

Provably Adaptive Trust Dynamics in
Context-Aware Zero-Trust Systems: A Formal
Framework for Continuous Verification

VIVIN KRISHNAN 1 AND C. S. SREEJA 2, (Senior Member, IEEE)
1Department of Computer Science, CHRIST (Deemed to be University), Bengaluru, Karnataka 560029, India
2Center for Quantum Technologies and Complex Systems (CQTCS), CHRIST (Deemed to be University), Bengaluru, Karnataka 560029, India

Corresponding author: Vivin Krishnan (vivin.krishnan@res.christuniversity.in)

ABSTRACT Zero-Trust (ZT) requires continuous, context-aware evaluation of authentication and
authorization decisions. This paper introduces Zero-Trust Hybrid Adaptive Authentication (ZeTHAA),
a continuous authentication and authorization framework integrating contextual attributes, authentication
strength, behavioral evidence, and retry dynamics. ZeTHAA utilizes a probabilistic risk model and
dual-policy thresholds to partition outcomes into allow, step-up, and block regions, enabling precise control
over security–usability trade-offs. The system introduces a global admissibility predicate to distinguish
hard violations from probabilistic soft violations. Attribute importance is dynamically derived from entropy
and Beta-posterior distribution, enabling robust cold-start initialization and online recalibration. ZeTHAA
presents a unified composite attack surface covering credential compromise, attribute forgery, and post-
grant hijacking, modeling retry behavior with exponential risk escalation and temporal decay. A large-
scale synthetic dataset capturing realistic authentication flows, adversarial and temporal patterns, was used
to evaluate ZeTHAA against heuristic, logistic regression, random forest, XGBoost, and isolation forest
baselines. ZeTHAA produced a more expressive risk distribution and significantly higher attack detection
and efficiency while minimizing user friction. ZeTHAA outperformed baseline models, with Recall and Area
Under the Curve (AUC) exceeding 79% and 15.1%, respectively. F1-Score showed increases of 48%-147%,
with efficiency boost of 20-65%, while reducing the cost per attack by up to 39.6%. Benchmarks against
frameworks from Dasu et al. and Matiushin et al. showed a 57.5% lead in F1-Score, more than double
increase in detection rate, while blocking 70.78% more attacks. Additional analysis shows that ZeTHAA
provides a mathematically grounded foundation for Zero-Trust systems, aligns with NIST standards, offering
improved security guarantees and adaptive enforcement.

INDEX TERMS Adaptive authentication, application integrity check, Bayesian online learning, continuous
authentication, device authentication, dynamic secret injection, risk-based access control.

I. INTRODUCTION
Single-factor authentication (SFA) schemes have been the
mainstay of authentication because of their usability and
ease of implementation [1]. However, as computing resources
and threat vectors become increasingly sophisticated, attacks
on SFA systems have become commonplace [2], [3]. With
SFA, the attacker must focus on breaking only a single
authentication method [4].

The associate editor coordinating the review of this manuscript and

approving it for publication was Sedat Akleylek

.

The need for secure authentication accelerated the devel-
opment of multifactor authentication (MFA) systems, which
are more secure [5], [6]; however, MFA remains a static
approach that relies on sequential chaining of authentication
challenges [7]. Blancaflor et al. [8] reported sophisticated
attack measures that specifically target MFA systems. The
layering of challenges also contributes to user friction
and reduces usability and adoption [9]. Traditional MFA
techniques, while effective in bolstering security, frequently
lead to ‘‘MFA fatigue’’ and user frustration due to repetitive
prompts, even in low-risk scenarios [10].

VOLUME 14, 2026

2026 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/

77839

---

<!-- PAGE 2 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

Consequently, Adaptive Authentication (AA) systems,
which utilize users’ behavioral and contextual patterns to
challenge users sparingly when behavior deviates from estab-
lished patterns, have gained popularity [11]. AA incorporates
contextual signals such as device posture, geolocation,
behavioral biometrics, and network attributes to compute
dynamic risk scores. When the behavioral context of a request
varies from the established profile, the system selects an
alternative authentication modality to challenge the user.
The complexity of the selected alternative authentication
modality is proportional to the risk of malicious agents
accessing resources. In contrast to MFA, AA employs a
dynamic strategy in which risk factors are considered when
selecting the subsequent action. This evolution in security
design is largely driven by the inherent tension between
achieving robust protection and maintaining enhanced user
experiences [12].

As authentication systems began to incorporate adaptive
and risk-based authentication (RBA), a new cybersecurity
design paradigm, i.e., zero-trust (ZT), evolved in parallel,
with many enterprises adopting it as the driving principle. ZT,
which revolves around the principle of ‘‘never trust, always
verify’’, ensures that no implicit trust is assigned to users or
resources regardless of location (physical or network) [13].

However, many risk-based systems rely on heuristic or
proprietary scoring mechanisms, and they typically lack
a formalized mathematical model governing trust accu-
mulation, decay, and re-evaluation over time. This gap
motivates a transition from authentication-centric security
to architectural paradigms that assume persistent adversarial
presence.

This paper presents ZeTHAA - a novel convergence
of Zero-Trust philosophy into Adaptive and Continuous
Authentication. This work is based on the hypothesis
incorporating policy-aware, multi-threshold decision
that
mechanisms into risk-based authentication systems leads
to improved operational outcomes compared to traditional
single-threshold approaches. The proposed Zero-Trust-based
hybrid Adaptive Authentication system operates on a com-
that covers all participating discrete
posite attribute set
entities. The system covers the actor,
the medium of
access, and the platform it runs, establishing a ‘‘who -
uses what - on which’’ relationship. This allows for the
collection of a wider range of attributes while employ-
ing a minimally invasive profile. The hybrid nature of
the proposed system enables the validation of contextual
attributes, grouped by their composition, in parallel, thereby
allowing faster outcomes. The key contributions of this paper
are:

• Formalization of trust as a continuous, time-evolving,
and bounded state variable rather than a binary policy-
based outcome.

• Assurance-aware Trust initialization, integrating authen-

posture, behavioral context, access medium, application
attributes, and threat indicators) and transforms them
into a normalized risk metric for trust evolution.

• Trust evolution with reinforcement and temporal decay

dynamics.

• Parameterization and recalibration of weighting and

penalty coefficients.

• Explicit mapping of trust state to policy decisions within

Zero Trust architecture.

• Standards-aligned architectural

integration, including

identity, application, and device trust considerations.
• Formulate and evaluate a hypothesis that policy-aware
multi-threshold authentication improves the trade-off
between security and usability.

The remainder of this paper is organized as follows.
Section II outlines the research questions and hypotheses
guiding the proposed framework. Section III presents the
foundational principles of Zero Trust Architecture and
relevant standards. Section IV presents a detailed analysis of
the existing literature in the field and identifies key research
gaps. Section V discusses the methodology of the proposed
ZeTHAA framework and formulates the trust evolution
model. Section VI formalizes the security guarantees of the
ZeTHAA framework, followed by experimental evaluation
and findings in section VII. Finally, Section VIII concludes
the paper.

II. RESEARCH QUESTIONS AND HYPOTHESES
We establish the theoretical foundation by presenting the
research questions and hypotheses that underpin the proposed
framework.

A. RESEARCH QUESTIONS
AA and RBA systems have traditionally focused on improv-
ing classification accuracy through enhanced risk estimation
using heuristic or machine-learning approaches. However,
real-world authentication systems must balance security
(attack detection) with usability (user friction and cost),
with decisions governed by policies rather than risk scores
alone.

In this context, this work is guided by the following

research questions:

• RQ1: Does incorporating policy-aware, multi-threshold
decision mechanisms improve the trade-off between
security and usability compared to traditional single-
threshold RBA approaches?

• RQ2: Can multi-stage decision regions (allow, step-up,
block) reduce false blocking rates without significantly
degrading attack detection performance?

• RQ3: Does the calibration of model outputs to oper-
ational thresholds improve the alignment between risk
estimation and authentication decisions?

tication and identity strengths.

• Contextual Risk aggregation framework that

inte-
grates multi-dimensional contextual signals (device

These questions aim to shift the focus from risk pre-
diction alone to decision effectiveness under operational
constraints.

77840

VOLUME 14, 2026

---

<!-- PAGE 3 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

B. RESEARCH HYPOTHESES
Based on the above research questions, we formulate the
following hypotheses:

• H1 (Trade-off Hypothesis): A policy-aware, dual-
threshold authentication framework achieves a bet-
ter balance between security and usability than
single-threshold AA or RBA approaches.

• H2 (Decision Structure Hypothesis): Multi-threshold
decision regions reduce false-blocking rates while
maintaining comparable or improved attack-detection
performance.

• H3 (Calibration Hypothesis): Calibration of model
outputs to policy thresholds improves the alignment
between risk scores and authentication decisions,
enabling more effective utilization of decision regions.

C. HYPOTHESIS EVALUATION STRATEGY
The hypotheses were evaluated through a comprehensive
experimental framework using a held-out test dataset. Each
hypothesis is tested using specific metrics:

• Operational Trade-off (H1): Assessed using cost-
based metrics, step-up rate, block rate, and false
block rate, capturing the balance between security
enforcement and user friction.

• Discrimination Performance (H2): Evaluated using
Receiver Operating Characteristic (ROC) curves, Area
Under the Curve (AUC), and Equal Error Rate (EER),
which measure the ability to distinguish between benign
and malicious events.

• Decision Alignment (H3): Analyzed through calibrated
risk score distributions, decision boundary analysis, and
region-wise behavior (allow, step-up, block), demon-
strating how well model outputs align with policy
thresholds.

A comparative evaluation was conducted against heuristic
and machine learning-based baselines to validate the pro-
posed hypotheses.

Together, these research questions and hypotheses estab-
lish a framework for evaluating authentication systems not
only in terms of predictive accuracy, but also in terms
of decision quality, operational efficiency, and real-world
applicability.

III. ZERO TRUST ARCHITECTURE AND STANDARDS
CONTEXT
A. ZERO TRUST ARCHITECTURE
The Zero Trust paradigm operates on the tenet of ‘‘no
implicit trust’’. ZT assumes that no entity is trustworthy,
regardless of user identity, network, or device posture. The
key principles and components of the Zero Trust Architecture
(ZTA) have been formalized by the National Institute of
Standards and Technology under NIST SP 800-207 [13].
ZTA mandates continuous authentication, and verification
of identity, device, and contextual attributes across all data
points at all
times before granting access to protected
resources.

The core principles of ZTA include:

• Elimination of implicit trust
• Least privilege access enforcement
• Strict authentication and authorization actions
• Continuous evaluation of

signals

for data-driven

decisions

• Dynamic Policy-driven decision mechanisms

Under the ZTA, trust is treated as dynamic and contextual
rather than static and rule-driven. Access decisions are
evaluated by policy engines that analyze continuous data
supplied across sources. However, while ZTA articulates
architectural components—policy enforcement points, policy
decision points, and trust signal collectors—it does not
formally define a quantitative trust function or a methodology
for continuous trust evolution.

B. IDENTITY ASSURANCE AND AUTHENTICATOR
STRENGTH
NIST SP 800-63, referred to as ‘‘Digital Identity Guidelines’’,
standardizes authentication and identity proofing for private
and public sector enterprises. It covers a Risk Management
Framework, along with Identity and authentication life cycle
management, assurances, and assertions [14].

This framework defines Identity Assurance Levels (IAL),
Authenticator Assurance Levels (AAL), and Federation
Assurance Levels (FAL) for identity proofing and authen-
tication strength. AAL defines metrics that characterize
the strength of an authentication process. AALs 1-3 offer
an indicator of confidence in an authentication method.
Higher assurance levels (e.g., AAL2 and AAL3) mandate
stronger authenticators, including cryptographic hardware-
bound credentials.

Although these standards help choose authentication
methods based on security needs, they remain largely focused
on the strength of the authentication event itself. Assurance
levels do not specify how trust should decay, accumulate,
or be recalibrated during an active session, nor do they
address the dynamic threat conditions that emerge after
session establishment.

C. PHISHING-RESISTANT AUTHENTICATION AND FIDO
The FIDO Alliance and W3C’s work on phishing-resistant
and largely passwordless authentication methods resulted in
the FIDO2 framework and the WebAuthn standard [15].

FIDO-based authentication aims to eliminate or replace
shared secrets such as passwords or OTPs with public-key
cryptography, where private keys are securely bound to user
devices and never transmitted over the network. By lever-
aging device-bound hardware credentials, this architecture
provides strong resistance to phishing attacks, credential
replays, etc., significantly strengthening authentication.

Nevertheless, similar to other authentication mechanisms,
FIDO aims to secure the authentication event rather than
defining continuous trust evaluation mechanisms throughout
the life of authenticated sessions. They do not provide formal

VOLUME 14, 2026

77841

---

<!-- PAGE 4 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

models for adaptive trust recalibration or continuous risk
aggregation.

D. ARCHITECTURAL GAPS IN STANDARDS-BASED ZERO
TRUST IMPLEMENTATIONS
Zero Trust architecture and identity assurance standards
provide a robust framework for secure access control.
However, they do not define a computational model for trust
evaluation and recalibration. This results in implementations
relying on arbitrary or heuristic scoring approaches.

• Trust is treated as a policy outcome rather than as
a continuously monitored, measurable, and evolving
variable.

• There is no formal definition of how contextual signals
from different sources are aggregated and transformed
into quantitative trust metrics.

• The parameterization of reinforcing weights or degrad-

ing penalties and their formulation is not defined.

• Trust decay, recalibration, and convergence during

ongoing sessions are not modeled formally.

These limitations highlight a critical research gap: the
lack of a formal mathematical
framework capable of
modeling continuous, adaptive trust computation within Zero
Trust architectures. The following section surveys existing
academic approaches that attempt to address aspects of this
problem and identifies the remaining challenges that motivate
the proposed model.

IV. RELATED WORK
Strong security systems have been a priority area of research
in both industry and academia, and previous studies on
implicit authentication using behavioral metrics set the path
towards AA.

A. RISK-BASED AND ADAPTIVE AUTHENTICATION
Risk-based authentication (RBA) and Adaptive Authenti-
cation (AA) for systems have been a growing focus of
study. RBA focuses on risk analysis using contextual and
behavioral signals, comparing them with the user’s historical
profile, and derives a risk score. The risk score determines
which authenticators will be employed to challenge the user.
Adaptive authentication focuses on choosing authenticators
to activate based on the risk score derived from behavioral
and contextual analysis. They represent an ‘‘at the point of
authentication’’ phase.

Dasu et al. [16] proposed an Adaptive Authentication
framework to defend against identity threats. However, the
authors adopt a heuristic approach to weight assignment,
in which risk signal weights are assigned statically and
are independent of the data distribution and attack history.
Furthermore, the variance computation is performed only
on the last 10 login records, limiting the scope of vari-
ance computation to strictly heuristic and not statistical.
Picard and Pierre [17] presented an RBA system that uses
deep reinforcement learning (DRL) to select authentication

modalities based on a user’s context. The work concentrated
on access to mobile device applications based on user context
and resource sensitivity. Although the DRL approach enables
rapid learning and inference, the system lacks cold-start
initialization when no prior data are available.

An RBA implementation for OpenStack was presented by
Unsel et al. in [18]. This study attempts to mitigate the low
adoption rates of RBA. However, the framework uses only the
IP address, round-trip-time(RTT), and User-Agent to evaluate
variance from baseline behavior. Matiushin et al. proposed
Machine Learning-Empowered Risk-Based Authentication
(MLE-RBA), a LightGBM-based RBA framework, in [19].
Although MLE-RBA operates on a dynamically computed
binary threshold, it focuses on the mathematical optimality
and does not account for user friction in the outcome.
In addition, the framework assumes that prior data is available
to compute the threshold. Further studies on risk-based and
AA have been proposed by [20], [21], [22], [23], [24],
and [25] that utilize various attributes such as usage patterns,
behavioral biometrics, and smartphone usage. However, these
studies propose binary decision-making systems based on
singular behavioral aspects, that are individually susceptible
to spoofing.

RBA and AA systems focus on the authentication phase,
and not beyond into post-login authorization requests, token
grants, and resource requests. This is handled by continuous
authentication systems.

B. CONTINUOUS AUTHENTICATION
Continuous authentication (CA) systems focus on validating
a user’s identity while a user session is in progress.

Acar et al.

[26] presented a wearables-assisted CA
framework that verifies user identity based on keystroke
dynamics detected by sensors. The work proposed by
Buriro et al. [27] used keystroke dynamics and touch-timing
differences to continuously authenticate users throughout
active sessions. The framework distinguishes itself from
others by not requiring users to memorize a fixed password.
Shen et al. presented a behavioral biometrics-based CA
system for smartphones [28]. Liang et al. [29] investigated the
use of wearable-device behavioral biometrics for continuous
in which ML was employed to derive
authentication,
behavioral patterns from biometric data. In [30], Mekni et al.
presented a study in which CA was achieved using gait
biometrics and was enhanced using machine learning. The
authors employed a deep-learning-based classifier to enhance
authentication accuracy. Shah et al. in their study on contin-
uous device-to-device authentication proposed a lightweight
CA framework that utilizes channel properties to dynamically
rotate session keys [31]. Similar studies in CA highlight the
growing interest in monitoring behavioral aspects for user
identity verification, with a focus mainly on wearables and
mobile devices [32], [33], [34], [35]. While promising, the
proposed CA systems effectively work on binary decision
controls, where the user request is either treated as benign or

77842

VOLUME 14, 2026

---

<!-- PAGE 5 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

asked to step up their authentication. Hard violations, such as
impossible travels, and cryptographic binding violat,ions, are
not considered. In addition, decisions are made by evaluating
data from limited behavioral attributes, which can be spoofed
individually, and by assuming that historical data will be
present as the system is online.

Furthermore, established products in the cybersecurity
domain, such as RSA Cybersecurity, CA Risk Authen-
tication, Okta, BIO-Key Portal Guard, Duo Risk-Based
Authentication, and IBM Security, employ risk-based AA
systems. However, the detailed working patterns of these
products, including the attributes they gather and the methods
employed to create the contextual profile, are proprietary.

C. ZERO-TRUST SYSTEMS
Zero-trust, as a design philosophy, is being rapidly evaluated
and adopted by researchers and industry.

Hasan et al. in their study [36] presented design and
assurance patterns for ZT components. With pattern libraries
enriched with their findings, the authors claim that system
architects can model ZT transformations of Cyber-Physical
systems. The authors in [37] proposed a process-driven
framework for migrating to a ZT architecture, aimed at
addressing the gaps and challenges identified in previous ZT
migrations. A similar study on the cost-effectiveness of ZT
transformation for organizational security was published by
Adahman et al. [38]. Similar studies on ZT transformation
of industry sectors have been published in [39], [40], [41],
and [42].

Hale et al. [43] presented a ZT-based mitigation approach
for ML components originating from data or model manip-
ulation. In addition, Krishnan and Sreeja [44] proposed a
zero-trust-based adaptive authentication system that uses
composite attribute sets. Ahmed et al. in their work [45]
presented a ZT-based access control system to guard sensitive
data stores. The authors utilized an access-control proxy to
analyze request parameters and arrive at the enforcement
decisions. A ZT-based implementation of security measures
for Oracle ERP cloud was studied by the authors in Qazi
and Arshad [46]. In contrast, a framework to protect power
grids from security attacks using a Zero-Trust strategy was
discussed by Faraj [47]. Similar zero-trust frameworks for
protecting resources have been featured in the literature [48],
[49].

D. RESEARCH GAP ANALYSIS
Based on the inference derived from the literature review, the
following research gaps have been identified, which need to
be addressed:

1) Vendor-locked, opaque implementation:

Existing Zero-Trust implementations are proprietary,
resulting in vendor lock-in, and do not offer a view of
internal working and calibrations [50], [51], [52], [53].

2) Static attribute weighting and penalty policies:

Attribute importance, spoofability, and temporal sta-
bility are set by fixed rules or expert heuristics. Sys-
tems lack cold-start strategies and online recalibration
methods [16], [54], [55].

3) Implicit Trust:

Risk evaluation and trust computations are performed
only until
the point of authentication. Post-login
requests are implicitly deemed valid and fall within the
realm of implicit trust [17], [18], [19].

4) Lack of an explicit admissibility/safety invariant.
Industry controls (e.g., impossible travel checks, attes-
tation failures) are often implemented as scattered
heuristics. There is little formal distinction between
failures and probabilistic
non-compensable (hard)
(soft) evidence, which complicates correctness argu-
ments and policy proofs.

5) Poor integration of retry/attack dynamics into

threat models.
Retry behavior (failed logins, repeated attempts) is
frequently handled by synthetic counters or lockout
rules; few approaches model retries as probabilistic
amplifiers of attack likelihood with time decay and
contextual consistency checks.

6) Insufficient adversary-aware threat surfaces.

Composite attack surfaces that combine authentication,
attribute forgery, token replay, and post-grant hijack are
rarely modeled together; as a result, policy thresholds
are hard to justify quantitatively.

Based on the literature review, the identified research gaps
highlight the need to develop an AA system that covers the
following factors.

1) Discards implicit trust.
2) Models trust as a continuous, evolving, and bounded

variable

3) Multi-dimensional contextual signals for risk aggrega-
tion and policy-driven thresholds-based evaluation.
4) Enables parameterization and online recalibration of
attribute and authentication weighting and penalty
coefficients.

5) Resists profile poisoning.
6) Distinguishes between hard violations and probabilistic

soft violations.

7) Incorporates retry attack dynamics into threat models.
8) Aligned to industry standards.

The proposed ZeTHAA system is an extension of the work
of Krishnan and Sreeja [44] to mitigate identified research
gaps with an implemented proof-of-concept.

V. METHODOLOGY
This section presents the methodology underlying the
proposed Zero-Trust Hybrid Adaptive Authentication
(ZeTHAA) framework. The methodology proceeds from
system definition and state modeling to threat analysis,
risk computation, adaptive enforcement, and security
guarantees.

VOLUME 14, 2026

77843

---

<!-- PAGE 6 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

A. NOTATION
Table 1 summarizes the symbols and notations used through-
out this study.

B. SYSTEM MODEL
The system consists of a set of protected resources R =
{R1, R2, . . . , Rn}. Each resource Ri
is associated with a
required trust threshold T (Ri), which must be achieved before
access is granted. A set of registered users U interacts with
the system by performing actions Act = {login, read, write}
on the resources in R.

Access decisions are determined under a Zero Trust model,
in which no user, device, or session is implicitly trusted. Each
access request is evaluated based on:

• A set of contextual and behavioral attributes At =

{a1(t), a2(t), . . . };

• A set of supported authentication methods M, each
associated with an intrinsic authentication strength;
• A dynamically evaluated session context C(t), com-
prising attributes, authentication state, and historical
evidence;

• A trust score Trust(C(t)) and an estimated attack success

probability Pr[Attack Success | C(t)].

Authorization decisions are issued per session and per
resource, and are continuously re-evaluated as the context
evolves.

The ZeTHAA framework defines the Zero-Trust Adaptive

Authentication system as the tuple:

Z = (U , A, M , C, R, T )

where:

• U denotes the set of users,
• A = {a1, a2, . . . , an} denotes the set of contextual and

behavioral attributes,

• M = {m1, m2, . . . , mk } denotes the set of supported

authentication methods,
• C denotes session context,
• R ∈ {0, 1} denotes the observed security outcome,
• T ∈ R denotes the trust score.
The tuple Z defines the system’s static structure. Dynamic
behavior is captured by explicitly modeling the session
context C(t), the trust score T (t), and the observed outcomes
R(t) as time-dependent variables.

The high-level architecture of the proposed system is

presented in Fig. 1:

C. ASSUMPTIONS AND DESIGN SCOPE
The proposed framework is built on a set of system,
threat, and modeling assumptions that enable the for-
malization of trust, risk, and attack probability. These
assumptions are aligned with Zero Trust principles and
standard identity frameworks such as NIST SP 800-207 and
SP 800-63B.

1) SYSTEM AND TRUST MODEL ASSUMPTIONS

• Continuous Evaluation. Trust is evaluated at every
request and is not persistent across sessions. Each
request is treated as a fresh evaluation under Zero Trust
semantics.

• Composite Trust Function. Trust is a unified function
of authentication strength, contextual attributes, and
behavioral history. No independent trust components
(e.g., authentication-only or behavior-only trust) exist in
isolation.

• Separation of Trust and Risk. Trust and risk are
complementary but distinct quantities. Trust represents
confidence in legitimacy, whereas risk represents the
likelihood of adversarial success. The decisions are
based on both quantities.

2) ATTRIBUTE AND CONTEXT ASSUMPTIONS

• Attribute Observability. Contextual attributes (device,
time, network, etc.) are observable with

location,
bounded noise and may exhibit natural variability.

• Spoofability and Stability. Each attribute is associated
with a spoofability likelihood and temporal stability,
which influences its weight and penalty in trust
computation.

3) BEHAVIORAL AND LEARNING ASSUMPTIONS

• Behavioral Profiles are Probabilistic. User behavior
is modeled as a probabilistic distribution derived from
historical observations rather than deterministic rules.
• Temporal Drift. Legitimate user behavior evolves over
time, and the system accommodates this evolution
through bounded learning rates and windowed updates.

4) ADVERSARY AND THREAT MODEL ASSUMPTIONS

• Polynomial-time, probabilistic Adversary Model.
The adversary’s success is modeled probabilistically
through authentication breakability, attribute forgery,
and post-authentication attack vectors.

• Retry Behavior as Attack Signal. Repeated authenti-
cation failures are treated as probabilistic indicators of
adversarial activity and contribute to risk through retry
amplification functions.

• Hard vs Soft Violations. Hard violations represent
non-compensable failures (e.g., cryptographic failure,
impossible travel), while soft violations represent prob-
abilistic deviations that reduce trust but do not terminate
the session.

5) OPERATIONAL ASSUMPTIONS

• Availability of Logging and Telemetry. Sufficient
logging and telemetry are available to estimate
attribute distributions, behavioral profiles, and attack
probabilities.

77844

VOLUME 14, 2026

---

<!-- PAGE 7 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 1. Summary of notations.

• Policy-Driven Thresholds. Thresholds for authentica-
tion, authorization, and escalation are defined by system
policy and may vary according to resource sensitivity.

6) DEVICE CAPABILITIES
Every request is assumed to originate from a client device
capable of:

• Contextual Signal Provisioning: The device can pro-
vide contextual attributes such as location (coarse or
fine-grained), device characteristics, and application
metadata. These attributes may be derived from system
application programming interfaces (APIs), network
observations, or trusted execution environments.

• Device Integrity and Attestation: The device sup-
ports mechanisms to assert platform integrity, such
as Trusted Execution Environments (TEE), secure

enclaves, or platform attestation services. These mech-
anisms provide evidence of the device state (e.g., non-
rooted, verified boot, emulator).

• Cryptographic Capability: The device can securely
generate and use cryptographic keys for authenti-
cation,
including signing challenges and participat-
ing in hardware-backed authentication protocols (e.g.,
FIDO2 and, Trusted Platform Module (TPM)-based
attestation).

• Secure Communication: All communication between
the device and verifier is assumed to occur over
secure channels (e.g., TLS), ensuring confidentiality and
integrity of transmitted data.

7) SCOPE OF APPLICABILITY
In environments where such device capabilities are unavail-
able (e.g., legacy systems without attestation support), the

VOLUME 14, 2026

77845

---

<!-- PAGE 8 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

FIGURE 1. ZeTHAA system architecture.

framework degrades gracefully by assigning lower weights
to untrusted attributes and relying more heavily on behavioral
and contextual risk signals.

D. TRUST AND RISK
The trust state T (t) ∈ [0, 1] represents an accumulated
confidence. The trust evolves over time as the user continues
to interact with the system. The trust T (t) is thus a function
of the current and historical context, modeled as:

E. SECURITY OBJECTIVE
The primary security objective of the proposed system is to
ensure that access to any protected resource is granted and
maintained only when the probability of adversarial success
in the current context remains below an acceptable threshold.
For any session context C(t) at any given time t, the system

enforces:

∀t, ∀k ∈ K, Pr(Rk (t) = 1 | C(t) ≤ δk

T (t) = f (C(t), T (t −),

Rk (t) ∈ {0, 1}∀k ∈ K

where T (t −) is the historical trust. Trust T (t) at any time is
a composite of contextual conformance, behavioral history,
device postures, and risk signals.

R(t) ∈ 0, 1 represents the security outcome at time t.
R(t) = Pr[Attack Success | C(t)] = 1 represents the risk
of adversarial access.

where Rk (t) = 1 indicates a successful attack of class k at
time t. Rk (t) = 0 otherwise. δ represents a configurable risk
tolerance.

The system adapts authentication strengths and authoriza-
tion decisions to evolving risk, thereby enforcing continuous
risk evaluation, consistent with Zero-Trust principles.

77846

VOLUME 14, 2026

---

<!-- PAGE 9 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

F. ATTRIBUTES
The system defines a set of attributes A. An attribute ai is a
measurable contextual or behavioral property derived from
the user, the device, or the application that facilitates the
construction of an overall risk profile and the computation
of the risk probability.

Each user request transmits a collection of attributes ai ∈
A to the system. The set of attributes A and its weight W (A)
can be defined as:

A = {ai ∈ A | w(ai) < Tr (Ri)},

where the weight assigned to any attribute is less than the trust
required to access any resource Ri.

The set of attributes A is extensible, and new attributes can

be added as discovered.

G. AUTHENTICATION MODALITIES
The system is configured with a set of authentication
modalities M with a corresponding set of weights W (M).
The set of authentication modalities M is defined as follows:
M = {m ∈ M | w(m) < Tr (i)}
where w(m) is the weight assigned to a selected authentication
modality m ∈ M. The weight obtained by successful
authentication with any participating modality will always be
less than the trust required to access the resource, Tr (Ri).

The set M is extensible and can accommodate newer

authentication modalities.

With this system model established, we define user identity

using authentication sessions.

H. AUTHENTICATION SESSION MODEL
The authentication Authi is represented as:

Authi(Ui, mi, C) → {True, False}
where Ui represents the user requesting verification of
identity, mi denotes the authentication method applied, and
context C = Ccontextual ∪ Cbehavioral denotes the context
originating from behavioral and contextual signals.

An authentication session is a construct established upon

successful authentication, defined as:

S = (Ui, m, t0, te, σ )

where:

• Ui ∈ U is the authenticated user,
• m ∈ M is the authentication method used,
• t0 is the authentication start time,
• te is the expiration time,
• σ ∈ {active, expired, revoked} denotes the authentica-

tion state.

An authentication session only establishes the identity
of a user at a given point in time. This does not imply
continued authorization. While authentication sessions verify
and establish user identity, authorization decisions depend on
additional environmental and situational factors, which are
modeled as a session context.

I. SESSION CONTEXT MODEL
The session context captures the environmental and situa-
tional conditions under which access requests are evaluated.
It is defined as a time-dependent tuple:

C(t) = (Rs, Dp, Ns, Tc(t), Lc),

where:

• Rs denotes resource sensitivity,
• Dp denotes device posture,
• Ns denotes network state,
• Tc(t) denotes temporal context,
• Lc denotes location context.
The session context evolves over time and directly influ-
ences risk estimation, trust computation, and authorization
decisions. Given the dynamic nature of the session context,
authorization must be continuously evaluated and not treated
as a one-time decision.

J. ATTRIBUTE TAXONOMY AND CLASSIFICATION
An attribute ai
is a behavioral or contextual property
associated with a user, device, session, or request. Attributes
provide contextual signals that are relevant to dynamic risk
and trust computation in Zero Trust systems. This section
introduces an attribute taxonomy and classification based on
their properties.

1) COMPOSITE ATTRIBUTE SET
The proposed ZeTHAA framework classifies attributes under
three categories,i.e., - ‘‘User,’’ ‘‘Application,’’ and ‘‘Device,’’
based on the participating entities. The attributes and entities
are discrete yet related. This establishes a ‘‘who uses what,
where’’ relationship among the three discrete entities (user,
device, browser/application), and this relationship model
allows attribute variances to be flagged across categories.
The application attributes provide a way to uniquely identify
‘‘the application, running on device’’ combination. Thus, the
attribute-driven context becomes a composite construct of
‘‘user, using the application, on device’’. The attributes used
in the Composite Attribute set are listed in Table 2.

For mobile devices, the device attribute set is obtained via
Application Programming Interfaces(APIs) provided by the
native mobile operating system.

2) ATTRIBUTE CLASSIFICATION
Attributes are classified based on their type, stability, and
applicability to context binding.
1) Contextual Vs Behavioral

Attributes that describe the execution environment are
classified as contextual, and those that describe user
interaction over time are considered behavioral. Table 3
classifies the attributes as contextual or behavioral.

2) Stability

Attributes can be classified as static or dynamic based
on their tendency to change over time, which affects
their contribution to the persistence or trust decay and

VOLUME 14, 2026

77847

---

<!-- PAGE 10 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 2. Composite attribute set.

TABLE 3. Contextual vs behavioral attribute classification.

from benign historical observations. A profile represents the
expected distribution or pattern of attribute values and may
include summary statistics, temporal patterns, or learned
probabilistic behavior.

For an attribute ai, the profile P i

u captures its expected

behavior, modeled as:

their suitability for continuous validation. For instance,
application and device attributes are predominantly
static and do not change during their interactions with
the system. Table 4 classifies attributes based on their
disposition to change.

Predominantly static attributes contribute to longer-lived
trust, while dynamic attributes are continuously evaluated and
utilized to detect anomalies.

K. DYNAMIC ATTRIBUTE ANALYSIS AND BEHAVIORAL
PROFILING
Contextual and behavioral attributes change owing to user
behavior, operational changes, and modifications to the
access device. For example, a login location or access time
may be benign for one user while anomalous for another.
As such, static interpretation of attributes is not sufficient
in Zero Trust environments. In ZT systems, trust must be
continuously evaluated, updated, or recalibrated.

This section introduces a dynamic analysis of observed
attributes, how they contribute to user-specific profiles, and
provides signals and evidence for trust, risk, and authorization
decisions.

P i
u = {E[ai], Var[ai], . . .},
where E[ai] represents the mean value and Var[ai] denotes the
observed variance of the attribute ai. Profiles are updated con-
servatively to accommodate benign drift while avoiding rapid
adaptation resulting from potentially adversarial behavior.

2) DEVIATION AND ANOMALY SCORING
Behavioral patterns can change, subject to human behavior
or associated changes. If a user with an established pattern
of logging in at 10 A.M. daily logs in at 9 A.M., the
system records this as a deviation from the established
pattern. However, this does not conclusively establish risk
or adversarial behavior. While the deviation indicates an
elevated risk, it could be an isolated incident of a user logging
in at a different time. The system records, flags, and validates
deviations against tolerance limits set per policy.

At time t, the observed attribute value ai(t) is compared
u to compute a deviation

against the corresponding profile P i
score:

(cid:49)ai(t) = dist(cid:0)ai(t), P i
u
where (cid:49)ai represents the deviation of the observed value of
the attribute from the established mean value.

(cid:1),

Observed deviations are evaluated relative to acceptable
attribute-specific variation thresholds. Let θi denote the
permissible deviation for attribute ai. Deviations within
this tolerance are treated as benign, while excess deviation
contributes to anomaly scoring and penalty assignment.

(cid:49)a+

i (t) = max(cid:0)0, (cid:49)ai(t) − θi

(cid:1)

1) BEHAVIORAL AND CONTEXTUAL PROFILES
For each user u (or device, where applicable), the system
maintains a behavioral and contextual profile Pu, constructed

The deviation score quantifies how unusual
the current
observation is relative to established behavior, but does not
directly result in a classification decision.

77848

VOLUME 14, 2026

---

<!-- PAGE 11 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 4. Temporal disposition of attributes.

3) MAPPING DEVIATIONS TO ATTRIBUTE PENALTIES
Deviation scores are mapped to attribute penalties that reflect
increased suspicion or reduced confidence in the observed
evidence. For attribute ai, the penalty at time t is a function
of the deviation observed:

πi(t) = g(cid:0)(cid:49)ai(t)(cid:1),

where g(·) is a policy-defined function that controls sen-
in higher
sitivity to deviations. Larger deviations result
penalties, which in turn reduce trust and increase estimated
risk in subsequent computations. The penalties represent
the system’s assessment of elevated risk based on observed
behavior; they do not imply that an attack has occurred.

The deviation-derived penalties introduced in this section
represent instantaneous evidence of anomalous behavior.
These signals are subsequently aggregated and recalibrated
time by the penalty assignment model described
over
later, which accounts for historical observations, resource
sensitivity, and policy constraints.

4) ROLE OF MACHINE LEARNING
Machine learning is employed in this layer exclusively for
evidence interpretation. Machine learning is strictly limited
to learning and updating behavioral profiles and computing
deviation scores. It does not directly determine authentication
or authorization outcomes, or modify authentication strength
or policy thresholds. Instead, ML-derived outputs serve as
inputs to trust, risk, and authorization decisions.

This separation enables the system to adapt to evolving

user behavior and environmental conditions.

5) INTEGRATION WITH DOWNSTREAM COMPONENTS
The penalties derived through dynamic attribute analysis
are incorporated into the composite trust and risk models

described in subsequent sections. Attribute penalties influ-
ence trust decay, contribute to attack success probability
estimation, and trigger adaptive enforcement actions during
continuous monitoring.

Thus, dynamic attribute analysis provides the foundation
for threat modeling, authorization decisions, and Zero Trust
guarantees.

L. BEHAVIORAL PROFILE CONSTRUCTION AND
EVOLUTION
This section formalizes the construction and evolution of
behavioral profiles introduced earlier. Behavioral profiles
capture long-term patterns of user behavior and serve as
the reference against which deviations are evaluated for
penalty assignment and trust computation. The framework
design balances adaptability to legitimate behavioral drift
with resistance to profile poisoning.

1) PROFILE INITIALIZATION
For each user u and behavioral attribute ai, an initial profile
P i
u(t0) is established at the first trusted observation. The
profile maintains summary statistics (mean and variance)
representing normal behavior.

This initialization phase provides a stable baseline from
which learning can proceed cautiously as observations
accumulate. Algorithm 1 details the initialization of the
behavioral profile.

2) HARD AND SOFT CONTEXTUAL VIOLATIONS
Observed deviations from behavioral profiles are classified
as either hard or soft violations.

Hard violations correspond to physically or logically
impossible states (e.g., infeasible geo-velocity, cryptographic
binding failures, token replay, hardware attestation failure,

VOLUME 14, 2026

77849

---

<!-- PAGE 12 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

Algorithm 1 Behavioral Profile Initialization
Require: Attribute ai, initial observation ai(t0)
0 , learning rate γ
Require: Default variance σ 2
Ensure: Initialized behavioral profile P i
u
1:

Initialize mean: µi ← ai(t0)
← σ 2
Initialize variance: σ 2
i
0
}

2:
3: Set profile P i
4:

u ← {µi, σ 2
i
Initialize penalty accumulator (cid:53)i ← 0

application signature mismatch). Such violations indicate
session compromise with high confidence and result in imme-
diate access denial or session termination. Hard violations
permanently disable learning for the affected session. Let
HV(t) ∈ {0, 1} denote the hard violation predicate at time t,
where HV(t) = 1 indicates that at least one hard violation has
occurred within the current authentication or access session.
Once a hard violation occurs, trust- and risk-based reasoning
is no longer valid, and the session must be terminated or re-
authenticated. The hard violation check is used by the system
as a primary defensive validation for each request, enabling it
to reject any request that violates the condition immediately.
Soft violations correspond to statistically unlikely but
plausible behavioral deviations (e.g., unusual login time, new
location). These violations incur penalties that reduce trust
but do not immediately invalidate the session. Soft violations
temporarily suspend learning until trust is re-established.

Table 5 classifies contextual signals into hard and soft
violations with the corresponding action executed by the
system.

Global Admissibility Predicate
The system defines a global admissibility predicate:

Admissible(t) ⇐⇒ (HV(t) = 0(cid:1)

The admissibility predicate represents a system-wide
safety invariant. All authentication, authorization,
token
issuance, and resource access events are defined only over
an admissible system state. If Admissible(t) = 0, all
subsequent requests are denied irrespective of accumulated
trust, authentication strength, or contextual evidence.

This separation ensures that trust computation operates
strictly within safe execution states, while hard violations
trigger immediate and deterministic security responses. This
distinction allows the system to react decisively to impossible
states while remaining tolerant of legitimate behavioral
variation.

as:

Learn(t) = Trust(t) ≥ τlearn
∧ (cid:53)i(t) ≤ ϵ ∧ S(m) ≥ Slearn
∧ ¬HardViolation(t)

(1)

where τlearn is a minimum trust threshold, (cid:53)i(t) represents
the cumulative penalties at time t, ϵ is a small penalty
tolerance, S(m) is the current authentication strength, Slearn
is a minimum authentication assurance required for learning,
and no hard violations have been observed. In addition,
a state variable LearningEnabled(t) governs whether profile
updates are allowed, transitioning to false upon anomalous
events, and returning to true only when sufficient trust has
been built, and soft violations remain within acceptable
bounds. The behavioral profile update proceeds only if:

UpdateAllowed(t) = Learn(t) ∧ LearningEnabled(t)

When Learn(t) = 1, the profile is updated using an

exponentially weighted moving average (EWMA):
u(t + 1) = (1 − γ ) P i
P i

u(t) + γ ai(t),

γ ∈ (0, 1), γ ≪ 1.
(2)

If Learn(t) = 0, then P i

u(t + 1) = P i
This separation ensures immediate reaction to suspicious
behavior while allowing learning to resume only after
sustained trust is re-established.

u(t).

4) LEARNING SUSPENSION AND RE-ENABLEMENT
To prevent adversarial manipulation, learning is suspended
whenever anomalous behavior is observed and the state
variable LearningEnabled(t) transitions to false.

However, suspending learning indefinitely would prevent
adaptation to legitimate behavioral shifts. Therefore, learning
is re-enabled only after sustained evidence of legitimacy is
observed over a temporal window W :

ReLearn(t) =

1
|W |
∧ X
s∈W

X

Trust(s) ≥ τlearn

s∈W
Indicator.((cid:53)i(s) > 0) ≤ k,

(3)

where s is a time index and k is the upper limit of the number
of soft violation events permitted within the relearning
window W , and Indicator(.) is an indicator function.

When ReLearn(t) = true, LearningEnabled transitions to

true.

3) BEHAVIORAL LEARNING POLICY
Behavioral profiles are updated in an event-driven and trust-
based manner. Profile updates occur only when no hard
violations are observed, the current trust level exceeds a
learning threshold, authentication strength is satisfactory, and
no significant penalties are present. This approach ensures
that anomalous behavior does not contribute to profile
learning and adaptation. The learning condition is modeled

5) BEHAVIORAL LEARNING STRATEGIES
Once initialized, behavioral profiles evolve through con-
trolled learning. Different attributes exhibit varying obser-
vation frequencies and noise characteristics;
therefore,
a single learning mechanism is insufficient. Accordingly,
is assigned a learning strategy χi ∈
each attribute ai
{online, windowed} based on its volatility, observation fre-
quency, and security sensitivity.

77850

VOLUME 14, 2026

---

<!-- PAGE 13 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 5. Hard violations vs soft contextual signals.

The system responds faster to behavioral attributes with
natural drift, to ensure faster adaptation and prevent step-up
authentication in every request. Stable and security-sensitive
attributes present a very slow rate of change. Sudden changes
to these attributes could signify an attempt at repeated attacks
or profile poisoning by adversarial elements. As such, stable
and security-sensitive attributes are assigned a slow learning
and adaptation rate.

The system defines a learning rate γi

that controls
the speed at which the behavioral profile adapts to new
observations. These values are policy-configurable and serve
as conservative defaults for evaluation. This hybrid strategy
ensures responsiveness to legitimate behavioral drift while
improving robustness against noise and profile poisoning.

γi ↓ for stable/contextual attributes,
γi ↑ for behavioral attributes with natural drift.
Furthermore, profile updates are calculated using EWMA
to ensure that profiles respond immediately to changes, adapt
gradually to legitimate behavioral drift, maintain historical
precedents, and give new observations more weightage in the
profile.

Behavioral profile updates are performed at two levels
of granularity. Trust-based online updates apply to low-
frequency, low-noise attributes, enabling immediate but con-
servative adaptation. For high-frequency or noisy attributes,
updates are performed over trusted observation windows,
allowing learning from aggregate behavior while improving
stability and resistance to profile poisoning.

a: TRUST-GATED ONLINE UPDATE
For stable, low-noise behavioral attributes (e.g., login time),
profile updates are performed using trust-gated online
learning. When learning is permitted, the profile mean is
updated using EWMA:

µi(t + 1) = (1 − γi)µi(t) + γiai(t),
where 0 < γi ≪ 1 is the attribute-specific learning rate.
Online updates enable gradual adaptation from individual
trusted observations while restricting the influence of any
single event.

Algorithm 2 demonstrates the trust-gated online behavioral

profile update.

b: WINDOWED BEHAVIORAL UPDATE
For high-frequency or noisy attributes (e.g., IP address,
access patterns), learning is performed over trusted observa-
tion windows. Let Wi = {t1, . . . , t|Wi|} denote a window of

u(t) = {µi(t), σ 2

Algorithm 2 Trust-Gated Online Behavioral Profile Update
Require: Current observation ai(t)
Require: Current profile P i
Require: Trust Trust(t), penalty (cid:53)i(t)
Require: Thresholds τlearn, ϵ
Require: Learning rate γ
Ensure: Updated profile P i
1: if Trust(t) < τlearnor(cid:53)i(t) > ϵ then
2:

u(t + 1)

i (t)}

P i
u(t + 1) ← P i
return

u(t)

3:
4: end if
5: Update mean (EWMA):
6:
7: Update variance:
8:
9: P i

i (t + 1) ← (1 − γ )σ 2
σ 2
u(t + 1) ← {µi(t + 1), σ 2

µi(t + 1) ← (1 − γ )µi(t) + γ ai(t)

i (t) + γ (ai(t) − µi(t))2
i (t + 1)}

observations. The aggregated behavior is computed as:

¯ai(Wi) =

1
|Wi|

X

t∈Wi

ai(t).

(4)

Profile updates are then applied using EWMA:

µi(t + 1) = (1 − γi)µi(t) + γi ¯ai(Wi).

Windowed updates reduce sensitivity to transient noise and
improve robustness against
in-session profile poisoning.
Algorithm 3 presents the windowed approach to behavioral
profile update for high-frequency attributes.

Algorithm 3 Windowed Behavioral Profile Update
Require: Observation window W = {ai(t1), . . . , ai(tk )}
Require: Window trust summary Trust(W )
Require: Window penalty indicator (cid:53)i(W )
Require: Profile P i
u(t)
Require: Learning parameters τlearn, γ
Ensure: Updated profile P i
1: if Trust(W ) < τlearnor(cid:53)i(W ) > 0 then
2:
3:
4: end if
5: Compute window aggregate:
¯ai ← 1
6:
|W |
7: Update mean:
8:
9: P i

µi(t + 1) ← (1 − γ )µi(t) + γ ¯ai

u(t + 1) ← P i
P i
return

u(t + 1) ← {µi(t + 1), σ 2

t∈W ai(t)

u(t + 1)

u(t)

i (t)}

P

VOLUME 14, 2026

77851

---

<!-- PAGE 14 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

Together, these strategies define how behavioral profiles

Trust is updated as:

are updated, as attributes are observed and evaluated.

M. AUTHENTICATION AND TRUST INITIALIZATION EVENT
An authentication session begins with an authentication and
trust initialization event, which establishes the initial trust
state of a user–device pair prior to any authorization decision.
This event marks the transition from an unauthenticated
request to an authenticated session and provides the baseline
trust from which subsequent authorization, continuous mon-
itoring, and adaptive enforcement operate. Authentication is
modeled as an iterative process that may include retries and
step-up challenges before a stable trust state is achieved.

Trust(t + 1) = Trust(t) + wm · (AuthSuccess(t))
−πm · (1 − AuthSuccess(t)),

(5)

where wm is the positive contribution of authentication
method m, and πm is the penalty applied upon failure.

4) STEP-UP AUTHENTICATION TRIGGER
Repeated failures or low resulting trust may trigger additional
authentication factors. Step-up authentication is required
when:

Trust(t) < τstep-up,

1) AUTHENTICATION EVENT
Let Eauth(t) denote an authentication event at time t, defined
as:

where τstep-up is a policy-defined threshold. Step-up mecha-
nisms may include OTP, hardware-backed challenge, or addi-
tional verification factors.

Eauth(t) = (cid:0)U , m, C(t), t(cid:1),

where U is the user identity, m is the authentication method
employed, and C(t) is the contextual state observed at
authentication time.

AuthSuccess(t) ∈ {0, 1} denotes the outcome of the
authentication attempt. Authentication succeeds if and only
if Admissible(t)=1 and the system validates method m
according to its defined assurance requirements.

2) INITIAL TRUST ASSIGNMENT
Upon successful authentication, an initial
assigned:

5) RETRY CONSISTENCY AND TRUST DELTA ANALYSIS
Let k denote the retry index within the current authentication
session. The trust value at retry k is defined as:

Trustk = f (cid:0)Ck , mk , Hk−1

(cid:1),

where Ck represents the contextual state at retry k, mk is the
authentication method employed, and Hk−1 denotes the prior
retry history.

The trust delta between successive retries is modeled as:

trust value is

(cid:49)Tk = Trustk − Trustk−1.

(6)

Trust(t0) = Tinit(S(m), C(t0), H(t0)),

where Tinit(·) is a policy-defined function of the authen-
tication strength S(m),
the observed authentication-time
context, and behavioral history. This initial trust reflects the
assurance obtained during the authentication phase, along
with contextual and historical behavioral evidence.

Authentication and trust initialization are complete when:

Admissible(t) = 1 ∧ Trust(t) ≥ τauth.

The resulting trust value Trust(t0) forms the baseline for
subsequent authorization decisions and continuous monitor-
ing.

3) AUTHENTICATION ATTEMPT AND RETRY SEMANTICS
Authentication attempts may succeed or fail due to benign
user error (e.g., mistyped credentials). Such failures are
treated as soft violations and result in a reduction in trust
rather than immediate termination. Authentication retries are
re-evaluated under ZT principles, in which each retry is
treated as an independent request with a fresh contextual and
behavioral assessment.

Let E (k)

auth(t) denote the k-th authentication attempt within a

session at time t.

In a Zero-Trust system, contextual drift, device change
(e.g., logging in from a different device), or network variation
(e.g., turning on VPN) may legitimately reduce trust even
when authentication succeeds. The system can verify trust
fluctuation between attempts, based on a policy-defined
threshold ϵT > 0, such that:

(cid:49)Tk < −ϵT

to determine and record the possibility of brute force
attacks, credential misuse, automation, or adversarial replay.
The authentication and trust initialization event defines the
starting state for continuous verification under the Zero Trust
model. Algorithm 4 defines the authentication and trust
initialization event.

6) HARD VIOLATION ESCALATION
Authentication failure alone does not constitute a hard
violation. However, excessive failures or detection of adver-
sarial patterns (e.g., brute force attacks, credential stuffing,
automation, or cryptographic proof failure) result in:

HV(t) ← 1.

Once HV(t) = 1, the system becomes non-admissible and
the session is terminated.

77852

VOLUME 14, 2026

---

<!-- PAGE 15 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

Algorithm 4 Authentication With Retry and Trust Initializa-
tion
1: procedure Authenticate(U , m, C(t))
2:

attempts ← 0
Trust(t) ← 0
while attempts < Nmax do

if Admissible(t) = 0 then

3:

4:

5:

6:

7:

8:

9:

10:

11:

12:

13:

14:

15:
16:

17:

18:

19:

20:

21:

22:

23:

24:

25:

26:

27:

28:

29:

30:

31:

return Reject

end if
result ← VerifyAuthMethod(U , m)
if result = success then

Trust(t) ← Trust(t) + wm

else

Trust(t) ← Trust(t) − πm
attempts ← attempts + 1

end if
if Trust(t) < τstep-up then
TriggerStepUp(U )
stepResult ← VerifyStepUp(U )
if stepResult = failure then

HV(t) ← DetectHardAttack(U )
if HV(t) = 1 then

return Terminate Session

end if

else

Trust(t) ← Trust(t) + wstep

end if

end if
if Trust(t) ≥ τauth then

return Authenticated

end if
end while
HV(t) ← 1
return Lock or Escalate

32:
33: end procedure

7) SEPARATION FROM AUTHORIZATION
initialized at authentication time serves as an
The trust
input to authorization decisions but does not itself imply
access to any protected resource. Authorization is evaluated
independently based on resource sensitivity, required assur-
ance levels, and contextual risk. This separation ensures that
authentication establishes identity and baseline confidence,
while authorization enforces ZT prescribed least-privilege
access under continuous evaluation. We now model
the
post-login authorization and subsequent flows in the next
section.

N. AUTHORIZATION DECISION AND EVENT
An authorization event is defined as:

Ea(t) = (Ui, Ri, A(t), t)

where Ui is the user, Ri is the requested resource, A(t) is the
authorization decision and t is the decision timestamp.

Algorithm 5 Authorization Decision Evaluation
Require: Resource Rs, context C(t), authentication state

S(t)

Ensure: Authorization decision
1: if ¬AuthValid(S(t)) then
return Deny
2:
3: end if
4: if ˆSeff(m, t) < ˆSreq(C(t), Rs) then
return Step-Up Authentication
5:
6: end if
7: if Trust(C(t)) < τgrant(Rs) then
8:
9: end if
10: if Pr[Attack Success | C(t)] > δgrant(Rs) then
11:
12: end if
13: return Authorize

return Deny

return Deny

Authorization is granted if and only if:

AuthValid(S(t)) ∧ ContextAcceptable(C(t)) ∧ (T (t) ≥ Tr (Ri))

where Tr (Ri) is the trust required to access Ri based on the
specified policy PolicyRi on the resource.

Authorization decisions are evaluated continuously over

time. The authorization decision at time t is modeled as:

A(t) = f(S(t), C(t), T (t), Rs),

where S(t) denotes the authentication state, C(t) the session
context, and T (t) the trust gained.

Let R(t) = Pr[Attack Success

| C(t)] denote the
composite risk evaluated under session context C(t). Each
protected resource Ri is associated with two risk thresholds
δ1(Ri) and δ2(Ri) such that:

0 < δ1(Ri) < δ2(Ri) < 1.

The authorization decision at time t

is defined as the

following threshold-based function:

A(t) =





allow,

if R(t) ≤ δ1(Ri),

step_up,

if δ1(Ri) < R(t) ≤ δ2(Ri),

(7)

deny,

if R(t) > δ2(Ri).

This ensures that increasing risk enforces stricter actions
to protect the system. Authorization decisions thus become
continuous verification consistent with Zero-Trust principles.
Algorithm 5 defines the evaluation of the authorization
decision.

The issuance and use of authorization tokens that mediate
access to protected resources following an authorization
decision are modeled in the following section.

VOLUME 14, 2026

77853

---

<!-- PAGE 16 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

Algorithm 6 Authorization Token Grant
Require: Authorization decision, context C(t), resource Rs
Ensure: Token T or denial

Algorithm 7 Resource Access Enforcement
Require: Access request (T , Rs), current context C(t)
Ensure: Access decision

return No Token Issued

1: if Authorization decision ̸= Authorize then
2:
3: end if
4: Bind token to context: T ← Bind(u, Rs, C(t), t)
5: Set token validity window and scope
6: Log authorization grant event Eg(t)
7: return Token T

O. AUTHORIZATION GRANT AND TOKEN-BASED
RESOURCE ACCESS
In Zero-Trust systems, authentication alone does not grant
access to protected resources. Instead, successful authen-
tication enables an explicit authorization grant, typically
realized through short-lived authorization tokens (e.g., OAuth
access tokens, Security Assertion Markup Language (SAML)
assertions, or JSON Web Tokens (JWT)).

1) AUTHORIZATION TOKEN MODEL
Authorization tokens are security artifacts distinct from
authentication sessions. An authorization token is modeled
as:

T = (Ui, s, ℓ, τe, κ)

where:

• Ui ∈ U denotes the user,
• s denotes the associated authentication session identifier,
• ℓ denotes the authorized scope or privileges,
• τe denotes the token expiration time,
• κ denotes cryptographic or contextual binding.

2) AUTHORIZATION GRANT EVENT
An authorization grant event is defined as:

Eg(t) = (S(t), C(t), T , t)

An authorization token is issued if and only if:

AuthValid(S(t)) ∧ S(m) ≥ Sreq(C(t)) ∧
Pr[Attack Success | C(t)] ≤ δgrant(Rs)
∧ (T (t) ≥ Tgrant (Rs))

return Deny Access

1: if ¬ValidateToken(T ) then
2:
3: end if
4: if ¬ContextMatch(T , C(t)) then
5:

Apply token-context mismatch penalty
return Deny Access

return Re-authentication Required

6:
7: end if
8: if Trust(C(t)) < τaccess(Rs) then
9:
10: end if
11: if Pr[Attack Success | C(t)] > δaccess(Rs) then
12:
13: end if
14: return Grant Access

return Deny Access

Token validity is defined as:

TokenValid(T , C(t))

(cid:16)
= 1

t < τe ∧ Bind(T , C(t)) ∧ ScopeAllowed(ℓ, r)

(cid:17)

(9)

Resource access is granted if and only if:

AuthValid(S(t)) ∧ TokenValid(T , C(t)) ∧
Pr[Attack Success | C(t)] ≤ δr (Rs)

(10)

This formulation enforces continuous authorization even

in the presence of valid tokens.

P. CONTINUOUS MONITORING AND RE-EVALUATION
As a Zero-Trust system, the context, risk, and trust states
must be continuously evaluated, and authorization decisions
should be revalidated throughout the lifetime of a session.
The system enters a continuous monitoring and re-evaluation
phase following the authorization grant and token issue. This
phase spans the lifetime of the session.

The continuous monitoring function at time t is modeled

as:

M(t) : (C(t), T (t −), R(t −), Tt ) → (T (t), R(t), E(t)),

(8)

where

where S(m) denotes authentication strength, Tgrant (Rs) is the
minimum trust threshold, and δgrant(Rs) is the maximum
acceptable attack success probability.

This ensures that possession of valid credentials alone
is insufficient to obtain authorization artifacts. Algorithm 6
describes the authorization token grant flow.

3) RESOURCE ACCESS USING AUTHORIZATION TOKENS
A resource access request at time t is defined as:

Er (t) = (Ui, Ri, T , C(t))

• C(t): current context
• T (t −), T (t): past and current trust states
• R(t −), R(t): past and current risk states
• Tt : current and active token
• E(t): enforcement decision
Algorithm 8 represents the continuous monitoring and re-

evaluation flow.

1) TRUST UPDATE
Trust evolves as a function of prior trust, current context, and
estimated risk.

77854

VOLUME 14, 2026

---

<!-- PAGE 17 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

Algorithm 8 Continuous Monitoring and Re-Evaluation
Require: Active session, context stream C(t)
Ensure: Updated trust, enforcement actions

2) TRUST DECAY
Trust is designed to decay even in the absence of user actions
or reinforcing evidence. Trust decay is modeled as:

1: while Session Active do
2:

Observe new attributes and events
Update context C(t)
Update attribute penalties for mismatch or absence
Update authentication penalties if applicable
Recompute Trust(C(t)), Pr[Attack Success | C(t)]
if Any authorization threshold violated then

Enforce step-up authentication, token revocation,

3:

4:

5:

6:

7:

8:

or termination
end if
9:
10: end while

The current context can be modeled as:

wi · Indicator(ai).[match(ai(t))]

C(t) = λ+ X
ai∈A
(cid:16)

− X
ai∈A
+ λmiss
i

λmm
i

(Rs) · πi · Indicator(ai).[mismatch(ai(t))]

(Rs) · π miss

i

· Indicator(ai).(cid:2)missing(ai(t))(cid:3) (cid:17)

(11)

Reeval(t) =

where:

• λ+ ∈ (0, 1) denotes the rate at which trust increases in

response to a matching contextual attribute ai.

• wi denotes the positive weight associated with an

attribute ai.

• λmm
∈ (0, 1] denotes a mismatch coefficient for
i
attribute ai. It controls how rapidly trust decreases
when the observed value of ai deviates from expected
behavior.

• λmiss
∈ (0, 1] denotes the missing-attribute coefficient
i
for attribute ai. It governs the rate of trust reduction when
evidence for ai is unavailable.

• πi > 0 denotes the penalty associated with a mismatch

of attribute ai.

• π miss
> 0 denotes the penalty associated with a missing
i
attribute ai. This value may differ from πi to reflect
scenarios where the absence of evidence is more or less
suspicious than an explicit mismatch.

•

Indicator(x) =

(cid:26) 1 : if x is present
0 : if x is absent

T (t) = T (t −) ∗ e−µ(cid:49)t ,

(13)

where (cid:49)t = t − t −, the time that elapsed between the past
trust state and current trust state, ensuring that stale sessions
do not retain implicit trust.

The risk R(t) is, however, always fully recomputed and

does not decay.

3) BINDING VALIDATION
For attributes bound to the authorization token, con-
tinuous monitoring verifies that bound attributes remain
within defined tolerance thresholds. Violations contribute to
increased risk and accelerated trust decay, mitigating replay
and session hijacking attacks.

4) RE-EVALUATION AND ENFORCEMENT
Authorization validity is re-evaluated at each monitoring step
according to:





Allow,

Step-Up,

Revoke,

T (t) ≥ τallow ∧ R(t) ≤ δrisk,
τdeny ≤ T (t) < τallow,
T (t) < τdeny ∨ R(t) > δrisk

(14)

This formulation ensures that authorization and access
privileges are continuously evaluated and adaptively enforced
in response to the evolving context and threat conditions.

Having defined the authentication and authorization mech-
anisms, the adversarial threats to the system are modeled in
the next section.

Q. THREAT MODEL
1) ADVERSARY DEFINITION
A polynomial-time adversary is modeled as:

A = (K, C, G)

where K denotes attacker knowledge, C attacker capabilities,
and G the objective of unauthorized access.

The knowledge and capability of the adversary can fall

under different attack classes, such as, but not limited to:

Using (11), the current trust can be modeled as:

K = {kauth, kgrant , kreplay, khijack , kpriv, . . .},

T (t) =

(1 − λ+) T (t −) + λ+ · C(t) − γ R(t)

(12)

Here, R(t) = Pr[Attack Success | C(t)] denotes the risk at
time t based on the current context and γ > 0 represents
the coefficient of risk, indicating how fast it suppresses
trust.

where:
kauth: Authentication compromise
kgrant : Illicit authorization grant
kreplay: Authorization token replay
khijack : Session hijack
kpriv: Privilege escalation

VOLUME 14, 2026

77855

---

<!-- PAGE 18 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

2) ATTRIBUTE-LEVEL THREATS
Each contextual attribute ai ∈ A is characterized by:

ai = (Ei, Si, Di, ρi)

where Ei denotes entropy, Si spoofability, Di
temporal
stability, and ρi = Pr(R = 1 | ai), represents the probability
of attack given ai.

Attribute-level risk is defined as:

Risk(ai) = λ1(1 − Ei) + λ2Si + λ3ρi

The probability of an adversary spoofing an attribute ai can

be defined as:

Pr[Forge(ai) | C] ∈ [0, 1]

The effective attribute compromise probability can be

defined as:

Pr[Forge(A) | C] =

n
Y

i=1

Pr[Forge(ai) | C]

3) AUTHENTICATION METHOD THREATS
Each authentication method m ∈ M is represented as:

m = (S(m), Rel(m), PR(m))

where S(m) denotes strength, Rel(m) reliability, and PR(m)
phishing resistance.

The probability of compromise of an authentication

method m is approximated as:

Pr[Break(m)] = e−S(m)(1 − PR(m))

The effective probability of an adversary breaking an
authentication method, given a surrounding context C, can
be modeled as:

5) PROFILE POISONING
Since the proposed framework incorporates adaptive behav-
ioral profiling, an adversary may attempt to manipulate
learned baselines by injecting malicious or atypical behavior
over time, aiming to redefine normal context and reduce
anomaly sensitivity.

6) COMPOSITE THREAT SURFACE
The composite threat surface is defined as the probability of
unauthorized access under session context C(t), accounting
for attacks during both authentication and authorization
phases.

a: AUTHENTICATION-PHASE ATTACK
The probability of a successful authentication-phase attack is
defined as:

Pr[Attackauth | C(t)]
= 1 − (1 − Pr(Break(m) | C(t))·
Y
(1 − Pr(Forge(ai) | C(t))),

ai∈C(t)

(15)

| C(t) denotes the probability of
where Pr[Break(m)
compromising the active authentication method m and
Pr[Forge(ai) | C(t)] captures the forgeability of contextual
attributes used during authentication.

If multiple authentication methods are used during the life

of a session, then (15) can be modified as:

Pr[Attackauth | C(t)]
= 1 − Y
m∈M (t)
(1 − Pr(Forge(ai) | C(t)))

Y

(1 − Pr(Break(m) | C(t))·

Pr[Break(m) | C] = Pr[Break(m)] · (1 + η · Risk(C)),

ai∈C(t)

where η defines the sensitivity of the method m to contextual
risk Risk(C).

4) SESSION HIJACKING AND TOKEN REPLAY
A session hijacking or token replay event is modeled as:

Er (t) = (U ′
i

, Ri, T ′, C(t))

where U ′
capturing session hijacking or token theft scenarios.

i may differ from the original authenticated user Ui,

Token replay attacks are modeled as:

∃T ′ ̸= T

s.t. TokenValid(T ′, C(t)) = 1

The probability of replay success is approximated as:

Pr[Replay Success] = Pr[Steal(T )] · Pr[Bind Fail(T , C(t))]

Session hijacking is defined as:

U ′
i

̸= Ui ∧ T ′ = T

b: AUTHORIZATION-PHASE ATTACK
In a Zero-Trust system, contextual attributes are validated
after authentication through authorization and continuous
access checks. Let Ab ⊆ A denote the subset of attributes
bound to the authorization token or session.

The authorization-phase attack probability is defined as:

Pr[Attackauthz | C(t)]
= Pr[Illicit Grant]

+ Pr[Replay] · Y
ai∈Ab
+ Pr[Hijack] · Y
ai∈Ab

Pr[Forge(ai) | C(t)]

Pr[Forge(ai) | C(t)].

(16)

c: UNIFIED ATTACK SUCCESS PROBABILITY
Combining (15) and (16), the overall probability of unautho-
rized access is defined as:

Both attacks are mitigated through contextual binding,

continuous authorization, and adaptive trust degradation.

Pr[Attack Success | C(t)]
= 1−(cid:0)1 − Pr[Attackauth | C(t)](cid:1)(cid:0)1 − Pr[Attackauthz | C(t)](cid:1)

77856

VOLUME 14, 2026

---

<!-- PAGE 19 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

R. ATTRIBUTE WEIGHT AND PENALTY ASSIGNMENT
MODEL
This section formalizes the computation, initialization, and
online adaptation of attribute weights and penalties used in
trust evaluation. Weights are derived from threat-related prop-
erties and are computed periodically, ensuring continuous
validation.

1) ATTRIBUTE UTILITY AND WEIGHT FORMULATION
a: ATTRIBUTE UTILITY
Let A = {a1, a2, . . . , an} denote the set of attributes. Each
attribute ai is characterized by the following properties:

• Ei ∈ [0, 1]: entropy (uniqueness),
• Si ∈ [0, 1]: spoofability,
• Di ∈ [0, 1]: temporal stability,
• ρi ∈ [0, 1]: risk correlation, where ρi = Pr(R = 1 | ai)

denotes the probability of an attack.

Here, ρi follows a Beta distribution, ρi ∼ Beta(αi, βi),
where αi and βi denote the count of attack and benign obser-
vations, respectively. The Beta distribution model allows
learning and refining the attack correlation
incremental
as data builds. Spoofability and stability properties of an
attribute are treated as structural properties that remain
constant over time. They are re-evaluated as attack vectors
evolve.

Each attribute is associated with a normalized attribute

utility score as a function of its properties:

θi = U (ai) = αE Ei + αDDi + αρ(1 − ρi) − αS Si

(17)

where αE , αD, αρ, αS ≥ 0 and:

αE + αD + αρ + αS = 1

b: COMPUTATION OF ATTRIBUTE WEIGHTS
Attribute weights are obtained using softmax normalization:

a phase-specific version wi(p). Phase-specific weights allow
factoring in resource sensitivity at each phase of action.

wi(phase) =

eβpθi
j=1 eβpθj

Pn

,

where phase ∈ {login, grant, access, continuous access}.

2) ATTRIBUTE PENALTY FORMULATION
While attribute weights determine how trust is accumulates
through positive evidence, attribute penalties model the loss
of trust when expected evidence is absent or contradicts
it. In a Zero Trust system, both missing and mismatched
attributes constitute negative evidence, with different security
implications.

a: PENALTY TYPES FOR MISSING AND MISMATCHED
ATTRIBUTES
For each attribute ai, two penalty parameters are maintained:
: penalty applied when the attribute ai is missing

• π miss
i

from the observed context.

• π mm
i

: penalty applied when the attribute ai is present but

mismatches its expected or bound value.

3) INTEGRATION OF ATTRIBUTE PENALTIES INTO TRUST
COMPUTATION
The overall
penalties:

trust score incorporates both weights and

Trust(C(t)) = X

w(t)
i Indicator.[match(ai)]

i
− X
i
− X
i

π miss,(t)
i

Indicator.[missing(ai)]

π mm,(t)
i

Indicator.[mismatch(ai)],

(19)

wi =

eβθi
j=1 eβθj

Pn

(18)

enabling the accumulation and degradation of trust in

accordance with Zero Trust principles.

where β > 0 determines how a difference in the attribute’s
utility affects the weight derivation of the attribute.

By construction:

n
X

i=1

wi = 1

The softmax normalization is utilized to ensure that strong
attributes (high entropy, low spoofability) contribute more to
trust gain than weak attributes. This ensures that even if the
adversary manages to spoof weak attributes, the contribution
to trust will be minimal.

Depending on the sensitivity of the resources, attribute
weights can be modified based on the phase in which they
are participating (authentication, authorization, token grant,
resource access). The parameter β can be modified to be
a phase-specific version βp such that the weight becomes

4) ATTRIBUTE WEIGHT INITIALIZATION STRATEGIES
In the proposed system, attribute weights are derived from
attribute properties such as entropy, spoofability, reliability,
and attack correlation. Attribute weight derivation operates
under
three regimes, depending on the availability of
empirical data.

a: INITIALIZATION USING HISTORICAL OBSERVATIONS
When sufficient historical data is available, attribute weights
are initialized using evidence derived from prior authen-
tication and access logs. This process combines entropy,
Bayesian estimation of attack correlation, and structural
attribute properties to derive an initial utility score for each
attribute.

Let ai denote an attribute and R ∈ {0, 1} denote the security
outcome, where R = 1 corresponds to an adversarial event.

VOLUME 14, 2026

77857

---

<!-- PAGE 20 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

Historical logs are analyzed to compute the entropy of R and
the conditional entropy of R given attribute ai.

Shannon entropy of the attack and conditional entropy are

computed as:

H (R) = − X

P(R)log2P(R)

H (R | ai) = X
v∈Vi

P(ai = v)H (R | ai = v),

(20)

(21)

where Vi represents the set of all possible values that the
attribute ai can take. Information gain IG(ai) of attribute ai

IGai

= H (R) − H (R | ai),

(22)

quantifies the reduction in uncertainty about the security
outcome after observing the attribute.

In parallel, the attack correlation of attribute ai is modeled

as a Bayesian random variable:

ρi = Pr(R = 1 | ai),

with a Beta prior initialized from historical attack and benign
observations. The posterior mean,
αi
αi + βi

E[ρi] =

(23)

,

provides the estimate of the likelihood that the presence of ai
is associated with adversarial behavior.

Using these quantities, the initial utility of attribute ai is

defined as:

θ (0)
i

= λ1 IGai

+ λ2 Di + λ3 E[ρi] − λ4 Si,

(24)

where Di denotes the temporal stability of the attribute, Si
denotes its spoofability, and λk > 0 are policy-defined
coefficients reflecting the relative importance of each factor.
The initial attribute weights are then computed using

softmax normalization:

w(0)
i

=

eβθ (0)

i

βθ (0)
j

P

j e

ensuring contributions across attributes.

Algorithm 9 represents attribute weight initialization using

historical evidence.

b: INITIALIZATION USING EXPERT KNOWLEDGE
When no attack history logs exist, and only expert knowledge
is available to set attribute values, the expert defines initial
utility scores for attributes θ 0
i

= θ expert
i

In the absence of historical observations linking attributes
i and embeds an
i as a prior belief. The initial attribute weights are

to security outcomes, the expert assigns θ 0
initial ρ0
computed based on the θ (0)

as:

.

i

w(0)
i

=

eβθ (0)

i

Pn

j=1 e

βθ (0)
j

Algorithm 10 denotes attribute utilities and weights
initialization using expert knowledge alone, in the absence

Algorithm 9 Attribute Weight Initialization With Historical
Data
Require: Attribute set A = {a1, a2, . . . , an}
Require: Historical log dataset L
Require: Structural attribute properties {Si, Di}
Require: Initial Beta prior parameters {(αi, βi)}
Require: Coefficients λ1, λ2, λ3, λ4 > 0
Require: Inverse temperature β > 0
Ensure: Initial and updated attribute weights {w(t)
i

▷ Offline Phase: Batch Initialization Using Historical
Data

}

1: for each attribute ai ∈ A do
2:

Compute: IG(ai) ← H (R) − H (R | ai)
Count attack and benign occurrences (αi, βi)
], utility θ (0)
Compute posterior mean E[ρ(0)

i

i

3:

4:
5: end for

▷ Compute Initial Weights

6: for each attribute ai ∈ A do
← softmax(β, θ (0)
w(0)
)
7:
i
8: end for

i

return {w(0)

}

i

of historical data. Structural properties such as spoofability
and temporal stability are encoded in baseline utilities, while
Bayesian priors are initialized to enable subsequent learning.

Algorithm 10 Offline Expert-Only Attribute Utility Initial-
ization
Require: Attribute set A = {a1, a2, . . . , an}
Require: Expert-defined baseline utilities {θ (0)
}n
i=1
i
Require: Initial Beta prior parameters {α(0)
, β(0)
}n
i=1
i
Require: Inverse temperature parameter β > 0
Ensure: Initial attribute weights {w(0)

}n
i=1
▷ Initialize attribute utilities and priors

i

i

1: for each attribute ai ∈ A do
2:

θi ← θ (0)
i
ρi ∼ Beta(α(0)

i

3:
4: end for

, β(0)
i

)

▷ Compute initial weights

5: for each attribute ai ∈ A do
w(0)
← softmax(β, θi)
6:
i
7: end for

return {w(0)

i

}n
i=1

c: INITIALIZATION UNDER MAXIMAL UNCERTAINTY
When reliable estimates of {Ei, Di, Si, ρi} are unavailable, the
system adopts a uniform fallback initialization:

wi =

,

1
n

∀ai ∈ A

This fallback represents a non-informative prior and total
uncertainty over the attributes, ensuring unbiased baseline
behavior. As empirical observations accumulate, the system

77858

VOLUME 14, 2026

---

<!-- PAGE 21 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

transitions from uniform to entropy-driven weights without
altering the underlying trust or authorization logic.

5) ATTRIBUTE PENALTY INITIALIZATION STRATEGIES
Similar to attribute weights, penalties are initialized under
three distinct regimes depending on information availability.

a: INITIALIZATION USING HISTORICAL OBSERVATIONS
When historical logs are available, penalties are initialized
using empirical attack correlation. Let:

ρmiss
= Pr(R = 1 | ai missing),
i
ρmm
i = Pr(R = 1 | ai mismatched),
be modeled using Beta distributions. The initial penalties are
then defined as:
π miss,(0)
i

], π mm,(0)
i

= ν1E[ρmiss

= ν2E[ρmm

],

i

i

with ν2 > ν1, ensuring stronger penalties for mismatches.

b: INITIALIZATION USING EXPERT KNOWLEDGE
When expert knowledge is available but historical data is
absent, penalties are initialized based on structural attribute
properties such as spoofability and temporal stability:

π miss,(0)
i
π mm,(0)
i

= µ1Si + µ2(1 − Di),
= π miss,(0)
i

+ (cid:49)i,

(25)

(26)

where Si denotes spoofability, Di denotes temporal stability,
and µk , (cid:49)i > 0 are policy-defined coefficients reflecting the
severity of negative evidence.

c: INITIALIZATION UNDER MAXIMAL UNCERTAINTY
In the absence of both expert guidance and historical data,
penalties are initialized uniformly:

π miss,(0)
i

= π miss
base

, π mm,(0)
i

= π mm
base

,

where π mm
base
constants.

> π miss

base are conservative, policy-defined

6) ONLINE LEARNING AND ADAPTATION OF WEIGHTS AND
PENALTIES
Once the baseline weights and penalties are defined, the
system continues to learn and recalibrate its values as data
accumulates. At this stage, the system transitions into an
entropy-based learning regime.

a: ONLINE RECALIBRATION OF ATTRIBUTE WEIGHT
As the system operates, new session outcomes are observed
and incorporated into the model. The Beta posterior param-
eters (αi, βi) are updated incrementally based on observed
attack and benign events, generating an updated posterior
mean E[ρ(t)
]. Initially, attribute weights are dominated by
i
expert priors or arbitrary assignments. As observations accu-
mulate, Bayesian posterior means and entropy-based infor-
mation gain gradually shift importance towards attributes that
correlate with attacks.

Every time the system observes attribute ai:
(αi + 1, βi), (Attack | ai) = 1
(αi, βi + 1), (Attack | ai) = 0

(αi, βi) ←

(

(27)

The system computes the updated risk correlation and the
posterior mean of ρi as:

ρ(t)
i

= E[ρi | αi, βi] =

αi
αi + βi

Information gain may be recomputed periodically or updated
incrementally. With information gain IG(ai) of attribute ai

IGai

= H (R) − H (R | ai),

θ (t)
i

, the overall attribute utility at time t relative to its initial value
is defined as:
= θ (0)
i

(cid:1),
(28)
where η1, η2 > 0 controls the sensitivity of utility updates to
newly observed evidence.

] − E[ρ(0)

(cid:0)E[ρ(t)
i

− IG(0)
ai

](cid:1) + η2

(cid:0)IG(t)
ai

+ η1

Updated attribute weights w(t)
i

are obtained via softmax
normalization and used in subsequent trust computation and
adaptive enforcement decisions.

i

wt
i =

eβθ t

i

Pn

j=1 e

βθ t
j

,

where β > 0 determines how a difference in the attribute’s
utility affects the weight derivation of the attribute.

Algorithm 11 incrementally refines attribute utilities
and weights using Bayesian updating and entropy-based
information gain. This enables adaptation from cold start
or arbitrary assignment to data-driven operation, based on
accumulating evidence.

b: ONLINE RECALIBRATION OF PENALTIES
The penalty recalibration process operates on penalty signals
obtained by dynamic attribute analysis, adjusting their impact
on trust and risk based on accumulated evidence and system
policy.

As new session outcomes are observed, penalties are
updated incrementally using Bayesian estimation. Separate
Beta posteriors are maintained for missing and mismatched
events and updated based on observed attack or benign
outcomes.

Penalties are recalibrated using a delta-based update:

π miss,(t)
i

= π miss,(t−1)

i

+ γmiss

(cid:0)E[ρmiss,(t)
i

] − E[ρmiss,(t−1)
i

π mm,(t)
i

= π mm,(t−1)

i

+ γmm

(cid:0)E[ρmm,(t)
i

] − E[ρmm,(t−1)
i

](cid:1),
(29)
](cid:1),
(30)

to predefined bounds π min

≤ π max
.
subject
This formulation ensures stable learning while preventing
unbounded trust loss.

≤ π (·)
i

i

i

Algorithm 12 records incremental recalibration of attribute

penalties based on accumulating evidence.

VOLUME 14, 2026

77859

---

<!-- PAGE 22 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

Algorithm 11 Online Attribute Weight Recalibration via
Bayesian Learning
Require: Attribute set A = {a1, a2, . . . , an}
Require: Initialized utilities {θ (0)
Require: Initialized Beta parameters {αi, βi}n
Require: Learning coefficients α1, α2 > 0
Require: Inverse temperature parameter β > 0
Ensure: Updated attribute weights {w(t)
i

}n
i=1

}n
i=1

i=1

i

1: while new session observation (C(t), R(t)) is available do
▷ Update attack correlation posteriors

for each attribute ai ∈ C(t) do

if R(t) = 1 then
αi ← αi + 1

else

βi ← βi + 1

end if

▷ Attack observed

▷ Benign observed

2:

3:

4:

5:

6:

7:
8:

9:

10:

11:

12:

13:

end for
for each attribute ai ∈ A do
Compute: E[ρi], IG(ai)
Update utility θ (t)

end for
for each attribute ai ∈ A do
← softmax(β, θ (t)
)

i

i

14:

w(t)
i
end for
15:
16: end while

return {w(t)
i

}n
i=1

Algorithm 12 Online Bayesian Attribute Penalty Recalibra-
tion
Require: Attribute set A
Require: Initialized penalties {π miss
, π mm
}
i
Require: Learning coefficients α1, α2 > 0
Require: Penalty learning rates γmiss, γmm > 0
Require: Penalty bounds π min
Ensure: Updated penalties

, π max
i

i

i

1: while new session (C(t), R(t)) observed do

▷ Penalty learning for missing and mismatched

attributes

for each attribute ai ∈ A do

if ai is missing in C(t) then

if R(t) = 1 then

π miss
i

← min(π miss

i

+ γmiss, π max

i

← max(π miss

i

− γmiss, π min

i

else

π miss
i
end if

else if ai mismatches baseline in C(t) then

if R(t) = 1 then

π mm
i

← min(π mm

i

+ γmm, π max

i

← max(π mm

i

− γmm, π min

i

)

)

)

)

2:

3:

4:

5:

6:
7:

8:

9:

10:

11:

12:

13:

14:

15:

else

π mm
i
end if

end if

end for
16:
17: end while

return {π miss

i

, π mm
i

}

7) BASELINE ATTRIBUTE WEIGHTING ASSUMPTION
Although NIST standards primarily define requirements
for authentication mechanisms, they explicitly permit and
encourage the use of contextual and behavioral attributes for
risk-based and continuous authorization decisions, provided
such attributes are not treated as standalone authenticators.
Table 6 showcases indicative baseline values of weights and
penalties for the composite attribute set defined in Table 2.

The expert priors defined in this work align with these
guidelines and serve solely as initial conditions that are
progressively refined through empirical learning.

S. AUTHENTICATION STRENGTH AND PENALTY
ASSIGNMENT MODEL
1) AUTHENTICATION STRENGTH FORMULATION
a: DEFINITION OF AUTHENTICATION STRENGTH

Definition 1: The authentication weight wm reflects the
relative exposure of an authentication method to an adversary
and its contribution to the overall attack surface. wm provides
the degree of likelihood that an adversary will target method
m.
Authentication weights do not represent security strength.
Instead, weights scale the impact of a successful break rather
than reducing its likelihood.

Let m denote an authentication method. The authentication

S(m) = f (Hm, Rm, Bm, Lm),

where

• Hm represents credential entropy or cryptographic

strength

• Rm represents resistance to attacks
• Bm represents how tightly m can bind to the user, device,

or session context

• Lm represents life cycle assurance

b: RELATIONSHIP TO AUTHENTICATION ASSURANCE
LEVELS
Authentication strength provides a quantitative mapping to
authentication assurance levels. A mapping function φ(·)
associates strength values with required assurance thresholds:
AAL(m) = φ(cid:0) ˆS(m)(cid:1),
where φ(·) is indicative and aligns with the assurance
requirements defined in NIST SP 800-63B.

(31)

c: DEFINITION OF AUTHENTICATION UTILITY
Let M = {m1, m2, . . . , mk } denote the set of authentication
methods. Each method m is characterized by:

strength of m, denoted as S(m), is defined as:

• S(m): authentication strength,

77860

VOLUME 14, 2026

---

<!-- PAGE 23 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 6. Indicative attribute weights and penalties from expert priors.

• Rel(m) ∈ [0, 1]: reliability,
• PR(m) ∈ {0, 1}: phishing resistance,
• Pr[Break(m)]: probability of compromise.
The authentication method utility score is defined as:

e: INTEGRATION OF AUTHENTICATION WEIGHTS INTO
THREAT MODELING
The weighted authentication-phase attack probability is
defined as:

Um = γS log S(m)+γRRel(m) + γPPR(m) − γB Pr[Break(m)]
(32)

where γS , γR, γP, γB ≥ 0 and:

γS + γR + γP + γB = 1

The value of S(m) is driven by its entropy score. The utility
function takes the logarithmic value of S(m) to ensure it does
not dominate over the other properties.

d: COMPUTATION OF AUTHENTICATION METHOD SCORES
Authentication method weights are computed as:

wm =

eλUm
m′∈M eλUm′

P

where λ > 0 controls sensitivity. By construction:

wm = 1

X

m∈M

Pr[Attackauth | C]

=

X

m∈M

wm Pr[Break(m)]

!

·

n
Y

i=1

Pr[Forge(ai) | C]wi

(33)

2) AUTHENTICATION PENALTY FORMULATION
a: DEFINITION OF AUTHENTICATION PENALTY

Definition 2 (Authentication Penalty): An authentication
penalty (cid:53)m(t)
represents a reactive measure the sys-
tem undertakes by reducing the effective authentication
assurance in response to observed failures, degrada-
tion, or fallback behavior associated with authentication
method m.
Let m denote an authentication method invoked at time
t. An authentication penalty quantifies the degradation
in trust caused by failed, weak, or downgraded authen-
tication during an authentication or
re-authentication
event.

The authentication penalty is defined as a function:

(cid:53)m(t) = f (Authfail, Authdeg, Authfallback )

VOLUME 14, 2026

77861

---

<!-- PAGE 24 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

b: PENALTY TYPES FOR AUTHENTICATION METHODS
The system defines the following authentication penalty
types:

1) Authentication failure penalty (cid:53)fail
authentication challenge using m fails.
( π fail
m
0, otherwise,

m (t) =

(cid:53)fail

, if AuthFail(m, t)

m (t), when an

where π fail

m > 0

2) Authentication degradation penalty, applied when the
method m does not meet the required assurance for the
current context C(t).
( π deg

m ∗ (cid:49)S, if S(m) < Sreq(C(t)
0, otherwise,

(cid:53)deg

m (t) =

where S(m)
is the authentication strength of m,
Sreq(C(t)) is the strength required by the context, and
(cid:49)S = Sreq(C(t)) − S(m)

3) Authentication fallback penalty, applied when a weaker
method is used after a stronger method was requested
or failed.

(cid:53)fallback

m

(t) =

, if fallback to m occurs

( π fb
m
0, otherwise,

where π fb
Typically, π fb

m > 0
m > π deg
m

≥ π fail
m
authentication penalty is modeled as:

and the cumulative

(cid:53)m(t) = (cid:53)fail

m (t) + (cid:53)deg

m (t) + (cid:53)fallback

m

(t)

(34)

The ordering π fb > π deg ≥ π fail reflects the increasing
severity of authentication control degradation, consistent with
risk management guidance in NIST SP 800-30 and NIST SP
800-37, and in the authentication literature [56], [57], [58],
[59].

c: INTEGRATION OF AUTHENTICATION PENALTIES INTO
TRUST COMPUTATION
Authentication penalties reduce the overall trust score of a
context C(t), modeled as:

Trust(t) = Trust(C(t)) − X
m∈M (t)

(cid:53)m(t)

3) AUTHENTICATION STRENGTH INITIALIZATION
STRATEGIES
Authentication strength initialization defines the baseline
assurance associated with each authentication method prior
to any runtime observations. The authentication method
strength initialization strategies depend on historical obser-
vations, the availability of standards guidance, and expert
knowledge. These strategies differ only in how the initial
strength value is instantiated; the subsequent enforcement and
adaptation logic remains unchanged.

a: INITIALIZATION USING STANDARDS AND HISTORICAL
OBSERVATIONS
When standards, guidance, and historical security data are
available, authentication strength is initialized based on the
intrinsic properties of the authentication method and its
alignment with established assurance requirements.
Let S(m) = f (Hm, Rm, Bm, Lm) denote the intrinsic strength
formulation defined in Section V-S1. Initial strength values
are computed as:

S(0)(m) = log

(cid:16)
1 + ω1Hm + ω2Rm + ω3Bm + ω4Lm

(cid:17)
,

(35)

where the constituent properties are instantiated using
method-specific characteristics derived from standards such
as NIST SP 800-63B and industry best practices. The
logarithmic conversion ensures stronger properties do not
dominate the result.

The normalized strength ˆS(0)(m) is then mapped to an NIST
authentication assurance level using a monotonic mapping
function:

AAL(m) = φ(cid:0) ˆS(0)(m)(cid:1),

This mapping is indicative.

b: INITIALIZATION USING EXPERT KNOWLEDGE
In the absence of authoritative standards mappings or
sufficient historical data, authentication strength may be
initialized using expert knowledge. This approach helps
in deriving authentication strengths in case of customized,
proprietary, enterprise-specific, or emerging authentication
mechanisms for which standardized assurance levels are not
yet established. Domain experts assign an initial utility score
θ expert
that reflects the expected cryptographic hardness,
m
attack resistance, binding properties, and life cycle guarantees
of the method:

S(0)(m) = U expert

m

.

c: INITIALIZATION UNDER MAXIMAL UNCERTAINTY
When neither standards guidance nor expert knowledge is
available, authentication strength is initialized conservatively
under maximal uncertainty. All authentication methods are
assigned a uniform baseline strength:

S(0)(m) = Sbase,

where Sbase is a policy-defined constant representing minimal
assurance. This strategy ensures safe default behavior while
avoiding overestimation of authentication assurance.

In the absence of prior data,

the system initializes
the authentication method utility coefficients from (32)
uniformly, as:

γS = γR = γP = γB =

1
4

77862

VOLUME 14, 2026

---

<!-- PAGE 25 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

Under this assumption, the authentication method utility

function modeled in (32) reduces to:

Um =

1
4

(log S(m) + Rel(m) + PR(m) − Pr[Break(m)])

This uniform initialization treats all security-relevant
properties of an authentication method as equally important.
The resulting utility Um is interpreted as a security score and
is normalized via softmax to obtain the authentication method
weight:

wm =

eλUm
m′∈M eλUm′

P

The uniform initialization is adopted solely for baseline
evaluation and reproducibility; the coefficients γi can be
re-estimated or adapted using security outcomes once the
system is operational.

Regardless of the initialization strategy, authentication
strength is treated as an intrinsic, static property of the
authentication method. Runtime behavior, authentication
outcomes, and contextual factors do not modify S(m) directly
and are instead captured through authentication penalties and
contextual trust signals. Authentication strengths are recal-
ibrated as standards evolve (e.g., NIST standards revision),
when exploitation of the method is reported, or cryptographic
breaks occur.

This separation ensures that differences between initializa-
tion strategies affect only baseline assurance and do not alter
threat modeling assumptions or enforcement decisions.

4) AUTHENTICATION PENALTY INITIALIZATION STRATEGIES
a: INITIALIZATION USING STANDARDS AND HISTORICAL
OBSERVATIONS
When historical data is available, penalties are initialized
using empirical attack correlations. We model
the Beta
distribution:

ρx
m = Pr(R = 1 | x),

x ∈ {fail, degrade, fallback},

as the probability distribution of an attack scenario. Initial
penalties are defined as:

π x,(0)
m = κxE[ρx

m],

with κfb > κdeg ≥ κfail.

b: INITIALIZATION USING EXPERT KNOWLEDGE
In the absence of historical data, penalties are initialized using
expert-defined priors reflecting the intrinsic weakness of the
authentication method:

π x,(0)
m = µx(1 − S(m)),

x ∈ {fail, degrade, fallback},

(36)

with µfb > µdeg ≥ µfail.

VOLUME 14, 2026

c: INITIALIZATION UNDER MAXIMAL UNCERTAINTY
When neither historical data nor expert knowledge is
available, conservative defaults are used:

π x,(0)
m = π x
> π deg
base

base

base

≥ π fail
base.

with π fb

,

x ∈ {fail, degrade, fallback},

5) ONLINE LEARNING AND ADAPTATION OF
AUTHENTICATION PENALTIES
The penalty recalibration process operates on instantaneous
penalty signals generated by dynamic attribute analysis,
adjusting their impact on trust and risk based on accumulated
evidence and system policy.

For each penalty type x, a Beta posterior ρx

m ∼
is maintained. Upon observing a session

Beta(αx
m
outcome R(t), the posterior parameters are updated as:

, βx
m)

m ← αx
αx

m + 1[R(t) = 1],

m ← βx
βx

m + 1[R(t) = 0]

(37)

Penalties are recalibrated using a delta-based update rule:
(cid:0)E[ρx,(t)

m ] − E[ρx,(t−1)

m = π x,(t−1)
π x,(t)

](cid:1),

(38)

m

m

subject to bounds π min

m ≤ π max
m .

+ γx
m ≤ π x,(t)

T. INTEGRATION OF AUTHENTICATION STRENGTH AND
PENALTIES INTO AUTHORIZATION THRESHOLDS
Authorization decisions in the proposed framework are
governed by both the intrinsic assurance provided by
authentication methods and the dynamic trust and risk
signals accumulated during system interaction. Authenti-
cation strength acts as a minimum assurance gate, while
authentication penalties dynamically adjust the effective trust
and attack success probability.

1) PENALTY-ADJUSTED EFFECTIVE AUTHENTICATION
STRENGTH
Authentication penalties degrade the effective assurance of
an authentication method without modifying its intrinsic
strength. We define the penalty-adjusted authentication
strength as:

ˆSeff(m, t) = ˆS(m) − λ(cid:53) · (cid:53)m(t),

(39)

where (cid:53)m(t) is the cumulative authentication penalty and
λ(cid:53) > 0 is a policy-defined scaling factor.

2) PENALTY-ADJUSTED TRUST THRESHOLD
Authentication penalties also influence authorization indi-
rectly through trust degradation:

Trust(C(t)) = Trustattr(C(t)) − X
m∈M(t)

(cid:53)m(t),

(40)

ensuring that repeated authentication failures or downgrade
attempts rapidly reduce trust below authorization thresholds
for sensitive resources.

77863

---

<!-- PAGE 26 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

3) AUTHORIZATION GRANT CONDITION
Let Rs denote a protected resource with sensitivity level
σ (Rs). An authorization grant event at time t is defined as
Eg(t) = (cid:0)S(t), C(t), T , t(cid:1),

where S(t) is the active authentication state, C(t) is the
session context, and T is the issued authorization token.

The authorization token grant event from (8) can be

rewritten as:
Eg(t) ⇐⇒ AuthValid(S(t)) ∧ ˆSeff(m, t) ≥ ˆSreq(C(t), Rs)
∧ Trust(C(t)) ≥ τgrant(Rs)
∧ Pr[Attack Success | C(t)] ≤ δgrant(Rs),

where ˆSeff (m) denotes effective authentication strength,
Sreq(t) = f (Pr[Attack Success | C(t)]), τgrant(Rs) is the
minimum trust threshold, and δgrant(Rs) is the maximum
thereby allowing
acceptable attack success probability,
authentication degradation and fallback behavior to directly
influence authorization outcomes.

4) PENALTY-AMPLIFIED ATTACK SUCCESS PROBABILITY
Authentication penalties represent runtime evidence of degra-
dation, failure, or fallback behavior of authentication meth-
ods, indicating increased adversarial activity. Authentication
penalties thus provide a baseline of the break probability of
the authentication method and reflect elevated risk. This is
in line with NIST SP 800-30, which recommends treating
indicators as a measure of the likelihood of a threat.

With this, the probability of breaking an authentication

method is remodeled as:

Pr[Break(m) | (cid:53)m(t)] = Pr[Break(m)](cid:0)1 + ηm(cid:53)m(t)(cid:1),
where (cid:53)m(t) represents the authentication penalty imposed
in case of authentication challenge failure, downgrade,
or fallback using m, and ηm > 0 is a method-specific
sensitivity parameter.

The authentication-phase attack probability defined in (15)

is redefined as:

(cid:17)
1 − Pr[Break(m)](1 + ηm(cid:53)m(t))

Pr[Attackauth | C(t)]
= 1 − Y
m∈M(t)
(cid:16)

(cid:16)

. Y
ai∈C(t)

(cid:17)
1 − Pr[Forge(ai) | C(t))

This modeling contributes directly to the composite attack

success probability used in authorization decisions.

5) ADAPTIVE AUTHORIZATION ENFORCEMENT
The required authentication strength at time t is defined as:

Sreq(t) = f (Pr[Attack Success | C(t)])

If any condition in (V-T3) is violated, the system enforces

one of the following actions based on policy:

77864

• Step-up authentication to a stronger method m′ such that

ˆSeff(m′, t) ≥ ˆSreq(C(t), Rs);

• Token revocation or scope reduction;
• Access denial or session termination.
This mechanism enables continuous authorization, ensur-
ing that authentication assurance, trust, and risk remain
aligned with resource sensitivity throughout the session.

U. BASELINE PARAMETERIZATION FOR EVALUATION AND
POLICY TUNING
Authentication strength values are indicative baselines used
for evaluation and policy tuning, derived from the assurance
properties defined in NIST SP 800-63B and FIDO specifica-
tions, and do not imply formal certification.

Table 7 maps common authentication methods to NIST
AAL and FIDO, along with indicative baseline authentication
strengths and penalties for evaluation and policy tuning.

V. DETECTING AND ENFORCING HARD VIOLATIONS
Hard violations represent non-compensable states that result
in request denial and suspension of learning and recalibration.
We model the computation and validation of hard violation
signals below.

1) GEO-VELOCITY COMPUTATION
Geo-velocity, calculated from the time between requests and
the geographic distance, is crucial for risk assessment and
analysis. The geo-velocity risk model is represented using the
risk Function:

G(v) =





0

v − vsafe
vmax − vsafe
∞

if v ≤ vsafe
if vsafe < v < vmax
if v ≥ vmax

where velocity v = (cid:49)d
(cid:49)t
distance between two consecutive logins.

km/h and (cid:49)d is the Haversine

The geo-velocity safe threshold vsafe is set between 800-
1000 km/h [60]. The threshold vmax is set to 1000 km/h as
the upper bound of plausible commercial air travel speed,
allowing margin for geolocation inaccuracy and clock skew
while excluding physically impossible transitions. Speeds
below this threshold but exceeding normal travel rates are
treated as probabilistic anomalies rather than deterministic
violations. Requests with geo-velocity exceeding the hard
limit are blocked and reported as risky, given typical user
displacement.

Given two points with latitudes φ1, φ2 and longitudes
λ1, λ2 (in radians), the Haversine distance (cid:49)d is calculated
as:

(cid:18) (cid:49)φ

(cid:19)

a = sin2

2
c = 2 · atan2
d = RE · c,

+ cos φ1 cos φ2 sin2
(cid:17)
1 − a

√

a,

,

(cid:16)√

(cid:18) (cid:49)λ

(cid:19)

2

,

(41)

VOLUME 14, 2026

---

<!-- PAGE 27 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 7. Indicative baseline authentication strengths and penalties mapped to NIST AAL and FIDO.

where:

• (cid:49)φ = φ2 − φ1 (difference in latitudes),
• (cid:49)λ = λ2 − λ1 (difference in longitudes),
• RE is the Earth’s radius (mean radius = 6,371 km),
• atan2(y, x) is the two-argument arctangent function.

attacker rebuilds the application, the value changes, and can
be detected by the server.

The algorithms for the application integrity check and
dynamic build secret injection are presented in Algorithms 13
respectively. The corresponding anti-tampering
and 14,
techniques are described in Algorithm 15.

2) APPLICATION INTEGRITY ENFORCEMENT
With the increased penetration of smartphones, mobile
applications form a major access medium. The application
attributes described in Table 2 provide a contextual attribute
subset that can be used to statically verify the origin of the
request. The application attributes provide a way to uniquely
identify ‘‘the application, running on device’’ combination.
In addition, the proposed framework introduces two new
approaches to mitigate the risk of application spoofing.

a: APPLICATION INTEGRITY CHECKS
During the first connection of the device to the system, the
Cyclic Redundancy Check (CRC) value of the constituent
files of the application package is computed and stored on
the server. Upon each application load in the user’s device,
the CRC is recomputed and compared with the CRC data
on the server to ensure that the binaries have not been
tampered with.

b: DYNAMIC BUILD SECRET INJECTION
Dynamic Build Secret Injection comprises injecting a random
value into the application properties at build time. This
value is stored in the server during the first contact. If an

W. DEVICE INTEGRITY ENFORCEMENT
In ZT architecture, device posture is a trust signal that
is given as much weight as user identity. Policy-driven
specifications can detect if the device posture does not meet
the policy-set requirements and deny access, even if the
user identity is valid. Just as trust signals related to users’
behavioral and contextual attributes are validated, device-
originated attributes are also continuously monitored. The
proposed ZeTHAA framework introduces an adaptive device
authentication protocol that aligns with NIST guidance on
device binding by combining contextual device attributes
with hardware-backed verification. Passive device attributes
provide evidence that adds to or degrades trust. Contex-
tual trust degradation and risk-based escalation result in
hardware challenges that require the participating device
to establish a hardware-backed cryptographic binding. This
adaptive device authentication protocol offers resistance
to replay and device impersonation, consistent with NIST
SP 800-63B and Zero Trust principles defined in NIST
SP 800-207. Algorithms 16 and 17 describe the proposed
Adaptive Device Authentication Protocol.

With the system definitions described, we move into the
security guarantees formalized by the ZeTHAA framework.

VOLUME 14, 2026

77865

---

<!-- PAGE 28 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

4:

5:

6:

7:

8:

9:

10:

15:

16:

17:

18:

19:

20:

21:

22:

3:

4:

8:

Algorithm 13 Application Integrity Verification
Require: serverKey ← HKDF(masterKey, ‘‘checksum′′ ▷

Key derivation

1: appCRC ← 0, fileHashes ← ∅
2: procedure

ComputeAndRegisterCheck-

sum(ApplicationPackage)

for each file ∈ ApplicationPackage in parallel do

hash ← xxHash64(file.content)
fileHashes.add(hash)
appCRC ← appCRC ⊕ hash

▷ XOR chaining

end for
sealedCRC ← HMAC-SHA256(serverKey, appCRC)
SecureStore(sealedCRC)

▷ Encrypted database

9:
10: end procedure
11: procedure VerifyChecksum(ApplicationPackage)
12:

localCRC ← 0
for each file ∈ ApplicationPackage do

←

localCRC

⊕

localCRC
xxHash64(file.content)

if file /∈ fileHashes then

▷ Detect new/deleted

files

Reject(‘‘Unauthorized file modification’’)

end if

end for
receivedSeal ← HMAC-SHA256(serverKey, localCRC)
if receivedSeal ̸= SecureFetch() then

RejectAndAudit(‘‘Integrity violation’’)
ReportToSIEM()

▷ Security monitoring

3:

4:

5:

6:

7:

8:

13:
14:

15:

16:

17:

18:

19:

20:

21:

22:

end if
23:
24: end procedure

VI. SECURITY GUARANTEES
This section formalizes the security guarantees provided by
the proposed ZeTHAA framework. The guarantees are stated
relative to baseline assumptions and follow directly from
the models and mechanisms introduced in the preceding
sections.

A. IMPOSSIBLE TRAVEL ELIMINATION GUARANTEE
Guarantee 1 (Impossible State Elimination). The system
guarantees that no authorization grant or session continuation
occurs under physically or logically impossible contextual
states. Formally, for any time t,

ImpossibleTravel(t) = 1 ⇒ Grant(t) = 0.

Grant(t) ⇐⇒ ¬ImpossibleTravel(t) ∧ AuthValid(S(t))

∧ S(m) ≥ Sreq(C(t))
∧ Pr[AttackSuccess | C(t)] ≤ δ(Rs). (42)

B. SECURITY GUARANTEE: POISONING RESISTANCE
Guarantee (Profile Poisoning Resistance). Under
the
learning policy defined in (1)–(2), an adversary cannot
significantly shift a behavioral profile through transient or

Algorithm 14 Secure Build Secret Embedding and Verifica-
tion Protocol
Require: κ ← 256
1: Kwrap ← HKDF-SHA512(kmaster, ’’secret-wrap’’)
2: procedure EmbedSecret(Ssrc, build_config)
3:

▷ Security parameter

▷ 256-bit secret

σ ← PRF(κ)
σenc ← AES-GCM-SIV(Kwrap, σ )
// Obfuscated Injection
for each fi ∈ MatchFiles(Ssrc, *.cpp,py,java) do
InjectAsConst(fi, base64(σenc[0 : 32]))
InjectAsComment(fi, base64(σenc[32 :]))

end for
CompileWithPIE(Ssrc, build_config)

▷

Position-Independent Executable

StoreSecret(HMAC-SHA256(Kwrap, σ ))

11:
12: end procedure
13: procedure VerifySecret(Bapp)
14:

σext ← ExtractFromBinary(Bapp)
σdec ← AES-GCM-SIV-Decrypt(Kwrap, σext)
sealserver ← FetchSeal()
seallocal ← HMAC-SHA256(Kwrap, σdec)
if ¬SecureEqual(seallocal, sealserver) then
Reject(‘‘Tampering detected’’)
FireCanaryToken()

▷ Trigger deception

measures
else

GrantAccess()

end if
23:
24: end procedure

Algorithm 15 Anti-Tampering Techniques

1: function InjectAsConst(file, data)
2:

varName ← RandomIdentifier()
InsertCode(file, ’’const auto varName = ’’ + data +

’’;’’)

InsertDeadCode(file, varName)

▷ Control-flow

obfuscation
5: end function
6: function ExtractFromBinary(binary)
7:

mem ← ReadELF/PE/MachO(binary)
FindXORedSegments(mem, Kwrap[0 : 16])
return ReconstructSecret(mem)

9:
10: end function

suspicious activity. Specifically, for any time window W
during which Learn(t) = 0 for all t ∈ W, the profile remains
invariant:

u(t).

∀t ∈ W, P i

u(t + 1) = P i
the maximum
Moreover, when learning is permitted,
cumulative influence of any sequence of observations of
length n is bounded by 1 − (1 − γ )n, ensuring that
no finite sequence of events can rapidly redefine normal
behavior.

77866

VOLUME 14, 2026

---

<!-- PAGE 29 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

3:

4:

5:

6:

7:

8:

9:

10:

11:

12:

13:

14:

15:

3:

4:

5:

6:

7:

8:

9:

Algorithm 16 Adaptive Device Authentication Protocol
1: procedure DeviceAuthentication(C(t), Pu, θdev)
2:

(cid:49)pen ← 0
DOS ← ExtractOSAttributes(C(t))
for all di ∈ DOS do

if Match(di, Pu(di)) = 1 then
Trust(t) ← Trust(t) + wi

else

(cid:49)pen ← (cid:49)pen + πi

end if

end for
if (cid:49)pen ≥ θdev then

DRS ← SelectHWChallengeSet(DHW \ DOS )
SendChallenge(DRS )
BindState(DRS , C(t))
LearningEnabled(t) ← 0

end if
16:
17: end procedure

Algorithm 17 Hardware Challenge Verification
1: procedure VerifyDeviceChallenge(Uid , C(t), Dresp
RS )
← RetrieveBoundState(Uid )
2:

RS ) = 1 then

Dstate
RS
if VerifyHWProof (Dresp
RS

, Dstate
Trust(t) ← Trust(t) + wHW
LearningEnabled(t) ← 1

else

Trust(t) ← Trust(t) − πHW
HardViolation(t) ← 1
LogSecurityEvent(Uid , t)

end if
10:
11: end procedure

1) AUTHENTICATION ASSURANCE GUARANTEE

Theorem 1 (Minimum Authentication Assurance): An
authorization grant is issued only if the effective authen-
tication strength meets or exceeds the required assurance
threshold for the current context and resource sensitivity.

Proof: By construction, authorization is granted only
when ˆSeff(m, t) ≥ ˆSreq(C(t), Rs), where ˆSeff(m, t) = ˆS(m) −
λ(cid:53)(cid:53)m(t). Since (cid:53)m(t) ≥ 0, penalties can only reduce
effective strength, ensuring that authentication assurance is
□
never overestimated.

2) MONOTONIC RISK AMPLIFICATION GUARANTEE

Theorem 2 (Penalty-Induced Risk Monotonicity): The
probability of a successful authentication attack is a
monotonic increasing function of accumulated authentication
penalties.

Proof: The authentication attack probability is defined

as:

increases monotonically, implying that additional penalties
□
strictly increase adversarial success probability.

3) TRUST DEGRADATION AND RAPID LOSS GUARANTEE

Theorem 3 (Asymmetric Trust Evolution): Trust accumu-
lates gradually through positive contextual evidence but
degrades rapidly in the presence of authentication penalties
or attribute violations.

Proof: Trust is computed as:
Trust(t) = Trustattr(C(t)) − X
m∈M(t)

(cid:53)m(t) − X

πi(t).

i

Positive evidence contributes additively through weighted
attributes, while penalties are unbounded in frequency and
additive in magnitude, ensuring faster trust decay than
□
accumulation.

4) ADAPTIVE ENFORCEMENT GUARANTEE

Theorem 4 (Adaptive Step-Up and Revocation): If authen-
tication strength, trust, or acceptable attack risk thresholds
are violated at any time,
the system enforces step-up
authentication, token revocation, or access termination.

Proof: Authorization is continuously evaluated against
thresholds ˆSreq, τgrant, and δgrant. Violation of any condition
triggers predefined enforcement actions, ensuring that access
is never maintained under insufficient assurance or excessive
□
risk.

5) END-TO-END ZERO TRUST GUARANTEE

Theorem 5 (End-to-End Zero Trust Enforcement): Under
the stated assumptions, the proposed framework ensures
that no access is granted or retained solely based on
prior authentication, and that all access decisions are
continuously re-evaluated against current authentication
assurance, contextual trust, and estimated attack risk.

Proof: Initial access requires satisfaction of authen-
tication strength,
trust, and risk constraints. Continuous
monitoring updates penalties, trust, and attack probability.
Any deviation from acceptable bounds triggers enforcement
per Theorem 4. Therefore, trust is never implicit, persistent,
□
or unconditional.
Having established the security guarantees, Table 8 maps
the 7 NIST Zero Trust tenets to the proposed framework’s
security guarantees.

6) SCOPE AND LIMITATIONS
The guarantees hold relative to the accuracy of attribute
measurements, the correct initialization of authentication
strengths, and the timely observation of security outcomes.
Compromise of these assumptions may reduce the effective-
ness of enforcement, but does not invalidate the structural
guarantees of monotonic risk amplification and adaptive
control.

Pr(Break(m) | (cid:53)m(t)) = Pr(Break(m))(cid:0)1 + ηm(cid:53)m(t)(cid:1),
with ηm > 0. Since (cid:53)m(t) is non-negative and increasing
the conditional break probability
under negative events,

VII. EXPERIMENTAL EVALUATION
A. TESTBED AND IMPLEMENTATION
The evaluation was conducted on a Lenovo IdeaPad run-
ning 12th Gen Intel(R) Core(TM) i5-12450H (2.00 GHz)

VOLUME 14, 2026

77867

---

<!-- PAGE 30 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 8. Mapping of security guarantees to NIST zero trust tenets.

TABLE 9. Dataset summary.

TABLE 10. Attack distribution.

[H]

and 16 GB of RAM, running Windows 11 Home Edition(64-
bit). To evaluate the effectiveness of the proposed ZeTHAA
framework, we conducted experiments using a synthetic
authentication dataset that incorporates realistic user behav-
ior and adversarial scenarios. To ensure reproducibility, the
source code, the baseline implementations, and the evaluation
scripts are available at [61].

1) DATASET DESCRIPTION
The dataset contains approximately 50,000 authentication
sessions across 500 users, generating close to 150,000
authentication events. Each session includes contextual
attributes such as device model, operating system version,
geographic location, and temporal login behavior. The dataset
models user travel patterns and device life cycle events,
such as new phone purchases, operating system upgrades,
and application version upgrades. Approximately 70% of the
sessions represent normal user behavior, while the remaining
30% model adversarial scenarios. Table 9 summarizes the
overall dataset characteristics.

2) DATASET PROPERTIES
The dataset models multiple adversarial scenarios, including
coordinated attack campaigns, credential theft, bot-driven
login attempts, device spoofing, session hijack, token theft
and replay, and application tampering. The attack classes
were balanced and evenly distributed to prevent bias towards

[H]

a single attack pattern. Table 10 shows the diversity and
distribution of the attack types in the dataset.

B. CONTEXTUAL RISK MODELING
The proposed framework evaluates authentication risk using
contextual signals derived from device characteristics, net-
work context, user mobility, and behavioral patterns. These
signals are calibrated using evidence–based weighting to
estimate their relative contribution to authentication risk.

1) CONTEXTUAL SIGNALS
Key contextual signals include:

• geographic anomaly detection
• travel status and timezone shifts
• device fingerprint consistency
• session token reuse patterns
• repeated attacker IP activity
These contextual signals capture identity, device, network,
temporal, and behavioral context. The relative importance of
each contextual feature was derived using Bayesian online
calibration via Beta posterior updating. The calibrated results
show the probability of an attack given the exposure of the
attribute signal.

77868

VOLUME 14, 2026

---

<!-- PAGE 31 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

FIGURE 2. Feature importance.

FIGURE 3. Risk score distribution by class.

TABLE 11. Decision rates.

2) FEATURE IMPORTANCE
The relative importance of contextual features, derived using
is shown in Fig. 2. Attack
Bayesian online calibration,
campaign-related features contribute the highest
to risk,
followed by geographic anomalies. Device and session
integrity-related signals, particularly fingerprint mismatch
and session context inconsistencies, contribute moderately to
the risk score, while temporal and travel anomalies serve as
weak indicators.

C. RISK SCORE BEHAVIOR
Fig. 3 compares the distribution of risk scores by class
- benign and attack sessions. The figure shows a clear
separation between benign and attack events, with attack
sessions showing consistently higher risk values than benign
sessions. The attack classes form two clusters, with the
majority of the sessions in the first cluster showing risk
scores ranging from 0 to 0.11, indicating stable contextual
behavior. A second group is identified with risk ranging from
0.12 to 0.4, indicating a natural separation of risk values. This
demonstrates the proposed framework’s ability to distinguish
anomalous behavior. The distribution shows that the decision
thresholds can be placed logically.

D. DECISION POLICY AND DETECTION PERFORMANCE
1) THRESHOLD SELECTION
Authentication events are classified into three regions based
on their computed risk score decision thresholds. Events with
risk scores below the lower threshold τ1 are allowed without
additional verification, while moderate-risk events trigger
step-up authentication until the upper threshold τ2. Events
exceeding the upper threshold are classified high risk and will
result in denial of access.

The decision thresholds τ1 and τ2 are derived from the
dataset. The upper threshold τ2 is computed as the maximum
Youden’s value youden = tpr − fpr, where tpr denotes the
true positive rate and fpr represents the false positive rate. The

lower threshold τ1 was set to the 75th percentile of benign
traffic to minimize user friction.

The thresholds were subsequently derived from the dataset

as:

τ1 = 0.1180, τ2 = 0.1809

2) POLICY DECISIONS
Table 11 captures the policy decisions that apply thresholds
to the events.

The data shows that approximately 75% of benign events
were allowed without additional verification, while 17.5%
required step-up authentication. Only 7.5% of benign ses-
sions were incorrectly blocked. In the case of attack sessions,
about 73% were immediately blocked, and approximately
9.7% were subjected to step-up verification. The results show
that the framework balances security and usability, minimizes
user friction, and maintains attack detection.

Fig. 4 shows the policy decisions based on the risk score

distribution.

The derived decision thresholds balance between security
and usability. The majority of the benign events were allowed
without friction, while a controlled percentage underwent
step-up verification. The framework blocked a significant
proportion of attack events, demonstrating the effectiveness
of a risk-based policy.

E. CLASSIFICATION PERFORMANCE
To quantify the effectiveness of the proposed ZeTHAA
framework, standard classification metrics were computed
using the calibrated risk thresholds.

1) CONFUSION MATRIX
Table 12 presents the global confusion matrix comparing
the input dataset to the ZeTHAA framework’s output, while

VOLUME 14, 2026

77869

---

<!-- PAGE 32 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

FIGURE 4. Policy decision with risk score distribution.

FIGURE 6. Risk-trust correlation.

TABLE 12. Global confusion matrix.

TABLE 14. Stealth attack metrics.

TABLE 13. Performance metrics.

FIGURE 5. ROC curve.

the corresponding performance metrics are summarized in
Table 13. Fig. 5 shows the derived Receiver Operating
Characteristic (ROC) curve.

2) RISK-TRUST CORRELATION AND ATTACK
CLASSIFICATION PERFORMANCE
Fig. 6 presents the correlation between risk and trust, and how
the framework uses the trust score, along with the computed
thresholds to classify events.

The low-risk phase is represented by the region with risk
scores less than the step-up threshold. While this region
shows a high density of benign events as expected, it also
shows the presence of attack events. The subset of attacks that
fall in the low-risk region can be considered stealth attacks,
where adversarial behavior does not manifest strongly across
the observed contextual signals. Table 14 records the number
of attack events that were found in the low-risk zone.

However, even in the low-risk area, malicious activities
were found to dominate the lower trust areas, while benign
activities clustered in the higher trust region. This trend
continues into the transition phase between the thresholds.
The higher risk zone (>0.18) represents a concentration of
attack events and is also characterized by a high density
of events with very low trust scores. The diagonal linear
trend represents the correlation between risk and trust in the
framework: as the risk score increases, the trust score declines
linearly. This suggests that risk alone is not sufficient to
distinguish events; trust scores are the primary differentiator.
Fig. 6 also closely corresponds to the findings noted in
Table 11.

F. DETECTION LATENCY
An important requirement of an adaptive authentication
system is its ability to rapidly detect malicious activity.
To evaluate this aspect, the delay between the onset of an
attack and the first event exceeding the block threshold τ2 was
measured. The detection latency is defined as the number
of events required before the risk score crosses the block
threshold τ2.

Table 15 records the detection performance of the proposed
framework. Strong contextual signals, such as Attack cam-
paign signatures, device fingerprint mismatches, and session

77870

VOLUME 14, 2026

---

<!-- PAGE 33 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 15. Detection delay by events.

TABLE 16. User friction analysis.

FIGURE 7. Detection delay distribution.

FIGURE 8. Cost vs attack detection recall.

context violations, elevate the aggregated risk score above
the block threshold. The framework showed an immediate
detection rate of 98.4%, with a 95th percentile delay of
0 events. The average delay, in terms of the number of events
was 0.0170. Fig. 7 represents the distribution of detection
delay by events during the attack campaigns.

G. USER FRICTION ANALYSIS
The usability of the proposed ZeTHAA framework was
evaluated through user friction analysis. User friction analysis
aims to identify the rate at which benign users are forced to
perform additional authentication. While step-up authentica-
tion introduces moderate friction, blocking a benign user can
significantly degrade the user experience, including potential
service denial.

The friction metrics were computed as:

Step-Up Rate =

Benign Step-Up Events
Total Benign Events

False Block Rate =

Attack Block Rate =

Benign Block Events
Total Benign Events

Attack Block Events
Total Attack Events

A non-linear cost model was adopted to reflect
the
disproportionate impact of user-facing decisions. Step-up
authentication demands on benign users were assigned a
moderate cost, while blocking a benign user was assigned
a significantly higher cost due to user disruption and denial.
Blocking legitimate users is penalized more heavily than step-
up authentication, as it directly impacts service availability

and user experience. The cost map used was:

ALLOW : 1, STEP UP : 5, BLOCK : 10

Table 16 captures the user friction metrics, including the

cost details.

The usability impact analysis of the data showed that
73% of genuine attacks were blocked by the framework.
Approximately 15% of the benign users were challenged to
perform additional authentication. About 5% of benign users
were blocked from accessing resources.

Fig. 8 illustrates the trade-off between authentication
cost and attack detection rate across varying threshold
configurations. The plotted curve depicts possible operating
points of the framework when thresholds are varied. Each
point represents a unique threshold configuration, illustrating
the relationship between authentication cost and detection
performance. As expected, increasing the strictness of deci-
sion thresholds leads to higher detection rates at the expense
of increased user friction. The selected operating point
(marked with x) achieves a favorable balance, delivering
strong detection performance while maintaining a moderate
authentication cost.

H. ROBUSTNESS ANALYSIS
Robustness analysis of the proposed framework aimed at
assessing how the system responded to parameter changes.

1) ABLATION STUDY
As the system validates contextual signals to arrive at
a decision, an ablation study was conducted to measure
how the performance changes when the contextual signals

VOLUME 14, 2026

77871

---

<!-- PAGE 34 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

are removed. The study also aimed to confirm that each
contextual signal contributes to the system.

Table 17 records how the system responded to the
removal of each contextual signal. F1-score and Area
Under Curve(AUC) were used as the primary comparison
metrics. The system was unaffected by the removal of travel,
timezone, and temporal anomalies. The removal of repeated
attacker IP resulted in the largest variation in the metrics,
followed by Geo anomaly. The session token mismatch
showed the next highest variation, followed by fingerprint
mismatch. The observations matched with the contextual
feature importance computed in Fig. 2.

A further study was conducted by removing group signals,
in which all contextual signals related to a specific contextual
group were removed. Table 18 presents the observations
from the removal of group signals. The observations align
with results from the removal of singular contextual signals,
with the attack campaign-related group showing the highest
impact on F1 and AUC, followed by mobility, which groups
geo-anomaly-related signals. The session group showed
the next highest impact, followed by temporal and device
integrity.

2) ATTACK INTENSITY ANALYSIS
The performance of the framework under increasing attack
intensities was studied to understand its response to coordi-
nated attacks. This study exposed the framework to attack
intensities varying from 10% to 40%, simulating coordinated
attack conditions. Table 19 presents the findings from the
study.

The proposed framework demonstrated robust perfor-
mance under varying attack intensities. The AUC value
remains stable, showing that the framework is robust under
attack and can distinguish between attack and benign events,
even as the proportion of attacks increases. The recall value
also remains stabile with increasing attack density, indicating
that the attack detection capability is consistent. The precision
improves, indicating the system becomes more efficient as
attacks increase. The accuracy shows slight degradation but
remains stable overall.

The results highlight that the proposed framework main-
tains stable detection performance, while adapting efficiently
to increasing complex attack scenarios.

I. COMPARISON WITH BASELINE MODELS
To compare the effectiveness of the proposed ZeTHAA
framework, its performance was compared with multiple rep-
resentative authentication and anomaly detection approaches
commonly used in risk-based authentication systems.

1) BASELINE MODELS
The selected baseline methods represent different categories
of authentication models. Table 20 lists the baseline models
against which the proposed framework is assessed for
performance.

FIGURE 9. ROC comparison across models.

2) DETECTION PERFORMANCE
The performance of the proposed framework and baseline
models was evaluated using several commonly used security
metrics. All model comparisons were performed on a test set
to ensure fair and unbiased evaluation.

Table 21 shows the performance metrics observed compar-
ing the ZeTHAA framework against baselines. The similarity
in performance between Random Forest and XGBoost is
attributed to the limited feature space and the dominance of
a few contextual signals, leading to both models learning
identical decision structures.

The ZeTHAA framework outperformed other classifica-
tion algorithms across most performance metrics. While
Random Forest and XGBoost showed a marginal increase
in precision, ZeTHAA showed better results recall and F1-
score respectively. The ZeTHAA Framework significantly
outperforms every other model in Recall, notably beating
the Isolation Forest by over 251%. As the Recall is higher,
the overall F1-Score (the balance of Precision and Recall)
shows a massive jump of 48% to 147% over the comparison.
The Logistic Regression and Heuristic approaches performed
better
than Isolation Forest, which offered the lowest
performance metrics among all the approaches.

Fig. 9 records the ROC curve of the ZeTHAA framework
compared to the baseline models. The proposed framework
records a high true positive rate compared to the other models.
The computed decision thresholds are highlighted on the
curve, indicating the policy’s operating region. At the step-
up decision threshold (τ1) indicated by the blue marker, the
framework detects 83.2% of attack events and challenges
with step-up verification, while incurring a false positive
rate of 24.7%. The True Positive Rate (TPR) and False
Positive Rate (FPR) represent aggressive detection, but use
step-up authentication and do not block users. The red marker
indicates the operating point corresponding to the blocking
threshold (τ2), achieving 73.2% attack detection with a
7.24% false positive rate, showcasing strict security while

77872

VOLUME 14, 2026

---

<!-- PAGE 35 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 17. Single signal ablation results.

TABLE 18. Group signal ablation results.

TABLE 19. Attack intensity analysis.

TABLE 20. Selected baselines for comparison.

TABLE 21. Performance comparison between baselines.

minimizing user disruption. The shaded portion between the
policy thresholds represents the adaptive decision region of
the framework. The sharp rise of the proposed framework’s
ROC curve near the origin indicates early-stage discrimina-
tion capability, which helps in minimizing user friction while
maintaining high detection rates.

Fig. 10 records the policy decisions taken by the models.
The ZeTHAA framework balances security and usability
compared to the baseline models. Although it showed a
lower ‘‘ALLOW’’ state for events, it had a higher proportion
of step-up challenges than the baselines. This shows that
events with higher risk scores were automatically asked
to perform additional verification. The baseline models

showed a lower range of step-up challenges and block
decisions, indicating a conservative approach to security.
Unlike traditional classifiers that operate at a single threshold,
the ZeTHAA framework defines a controllable decision
band, enabling responses based on risk levels and improving
detection performance. The ZeTHAA framework produces
a well-spread risk distribution, enabling effective utilization
of allow, step-up, and block regions. In contrast, baseline
models exhibit clustered score distributions. This supports
RQ3 and H3, demonstrating improved alignment between
risk scores and decision policies. With a more effective use
of the intermediate step-up region, the framework further
supports RQ2 and H2.

VOLUME 14, 2026

77873

---

<!-- PAGE 36 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

The proposed framework achieves the lowest cost per
detected attack among all models. This indicates that
although the framework incurs higher overall costs, it uses
authentication resources more efficiently to detect attacks.
Baseline models exhibit a lower average cost but a higher
cost per detected attack,
reflecting inefficient security
performance. The proposed ZeTHAA framework achieves
a higher detection efficiency, indicating a more effective
use of authentication resources. The controlled increase in
intervention, with significantly improved detection, further
demonstrates support of RQ1 and H1.

J. COMPARISON WITH EXISTING FRAMEWORKS
With the ZeTHAA framework exhibiting better performance
metrics, operational efficiency, and cost effectiveness against
baseline models, we further compare ZeTHAA with method-
ologies presented in the existing literature. Comparison
studies were performed with Dasu et al. [16] and Matiushin
and Korkhov [19]. Dasu et al. use a weighted heuristic
approach to derive risk scores and make decisions. On the
other hand, Matiushin et al. use an ML-based approach to
identify anomalies in user behavior and classify requests as
an attack or benign. As representatives of two widely used
approaches to risk classification - heuristic and ML-based,
these works were chosen for the comparison study.

1) DASU ET AL
Dasu et al. utilize five risk signals - travel risk(r1), location
risk(r2), browser risk(r3), device risk(r4), and password
risk(r5). The risk score for each signal is bounded as {x ∈
R|0 ≤ x ≤ 5}. Each risk signal is assigned a static weight
that represents its relative importance in heuristic scoring.

• Travel Risk (w1) - 80/33
• Location Risk (w2) - 40/33
• Browser Risk (w3) - 20/33
• Device Risk (w4) - 20/33
• Password Risk (w5) - 5/33
Travel risk is assigned the highest weight, followed by
location, browser, and device risk, with password risk being
assigned the least weight. The total risk is then computed as:

Total Risk = (w1r1 + w2r2 + w3r3 + w4r4 + w5r5)

The weights are assigned statically, and the framework does
not propose an approach to recalibrate them or the binary
decision threshold. Risk scores that exceed the threshold are
subjected to validation. However, the risk analysis considers
only the last 10 login attempts, thereby excluding historical
patterns.

To compare the ZeTHAA framework with Dasu et al.,
we first map the risks to the proposed risk signals. Table 23
presents the mapping of risks from Dasu et al. to ZeTHAA
framework’s risk signals.

In the absence of separate browser or device features,
fingerprint mismatch is used as a proxy for both. The browser
signal is approximated using a device fingerprint mismatch,

FIGURE 10. Proportion of decisions per policy region.

3) OPERATIONAL EFFICIENCY AND COST PER ATTACK
The operational efficiency of the proposed framework was
verified against the baseline models.
Table 22 reports the operational efficiency metrics for the
ZeTHAA framework compared with the baseline models.
The proposed ZeTHAA framework records the highest
step-up and block rates among the models, exceeding 47.9%
and 59.9% respectively. However, in the context of the
higher recall value, indicating higher attack detection, the
higher step-up and block rates can be correlated to increased
intervention. The baseline models incur lower costs because
they fail
to identify and act on a large proportion of
attack events. The proposed framework maintains a higher
Efficiency (+20% to +65%) but incurs a higher False Block
Rate than Random Forest and XGBoost, suggesting a more
aggressive yet highly effective detection posture.

The analysis used a non-linear cost model, as adopted
earlier in the user friction analysis. The cost map used was
{Allow : 1, Stepup : 5, Block : 10}, indicating the cost of
asking a benign user for a step-up challenge or blocking him
from using the service.

Detection efficiency is defined as the ratio of the Attack
detection rate (Recall) to the Average cost of authentication.

Efficiency =

Attack detection rate(Recall)
Average authentication cost

The models were further compared in terms of their
average cost, cost per attack detected, and higher efficiency.
We define the cost per detected attack as the ratio of the
average authentication cost to the attack detection rate.

Cost per attack detected =

Average authentication cost
Attack detection rate(Recall)

Although the average cost per transaction is higher, the ‘‘Cost
per attack detected’’ is significantly lower, indicating a 17.3%
to 39.6% reduction in cost compared with the other models.
However, this increased cost is offset by improved attack
detection performance. The cost vs. recall and detection
efficiency observations support RQ1 and H1, respectively.

77874

VOLUME 14, 2026

---

<!-- PAGE 37 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 22. Operational efficiency and cost/attack detected.

TABLE 23. Risk to signal mapping.

TABLE 24. Performance metrics comparison.

which captures deviations in client-device characteristics.
While the dataset does not explicitly distinguish between
browser and device features, fingerprint-based signals pro-
vide a reasonable approximation of both.

2) MATIUSHIN ET AL
The Machine Learning-Empowered Risk-Based Authentica-
tion (MLE-RBA) framework proposed by Matiushin et al.,
uses a multi-stage ML pipeline to identify irregularities and
make dynamic decisions. It combines two unsupervised ML
models: Local Outlier Factor (LOF) and Isolation Forest to
capture both local and global deviations in a user’s behavior,
generating an aggregate anomaly score. This anomaly score is
fed into a LightGBM classifier to generate a continuous risk
score for every login attempt. Instead of relying on a static,
predefined threshold, MLE-RBA dynamically calculates an
threshold by evaluating the Receiver Operating
optimal
Characteristic (ROC) curve. If a login’s risk score exceeds
this threshold, the system classifies it as an attack and triggers
secondary authentication.

3) RESULTS AND OBSERVATIONS
All three frameworks were subjected to the same dataset and
cost mapping. The comparisons were conducted under the
broad categories of:

a: PERFORMANCE ANALYSIS
Table 24 records the performance metrics recorded by the
three frameworks. The proposed ZeTHAA framework exhib-
ited demonstrably higher performance indicators compared
to Dasu et al. and MLE-RBA. While MLE-RBA presented a
slightly higher precision, indicating accuracy in true positive
prediction, ZeTHAA was close behind and fared much better
than Dasu et al. ZeTHAA presented a higher recall, indicating
an edge in correctly classifying requests.

Table 25 presents the operational efficiency figures for the
three frameworks. The ZeTHAA framework presents a higher
step-up rate due to an active engagement policy, followed

by MLE-RBA. Dasu et al. presented the lowest step-up rate,
indicating that a higher number of requests were classified
as benign. ZeTHAA had the highest block rate among
the frameworks, while MLE-RBA demonstrated the lowest
false block rates, followed by ZeTHAA.However, ZeTHAA
exhibited the highest efficiency figures while recording the
lowest cost per correctly detected attack. The proposed
framework achieves higher recall at comparable cost levels,
demonstrating a more favorable security–usability balance
and supporting RQ1 and H1.

b: SECURITY POSTURE AND ATTACK DETECTION
Table 26 lists the combined confusion matrix of the three
frameworks.

The Proposed ZeTHAA Framework blocks significantly
more attacks (7,963) than both the heuristic (Dasu et al.)
(3,630) and MLE-RBA (3,695). ZeTHAA is much more
aggressive with ‘‘Step-Up’’ challenges for benign users
(4,184) than Dasu et al. (240), which corresponds with the
higher recall noted in Table 24. ZeTHAA also allows the
fewest attacks (1,826) through the system, whereas the others
allow over 5,000. MLE-RBA has the lowest FPR (1.95%),
indicating it rarely interrupts legitimate users. However,
as observed from the Recall value, it misses 66% of attacks
to achieve this. ZeTHAA blocked 5% more benign users than
MLE-RBA, but in exchange, caught nearly 40% more attacks.

c: ERROR REDUCTION
We further compared the frameworks for their Equal Error
Rate (EER). EER represents the point on a ROC curve, where
the False Positive Rate (benign users incorrectly blocked) and
False Rejection Rate are equal. A lower EER represents a
better balance between false accepts and rejects, showcasing
the ability to detect attacks while making fewer mistakes on
identifying legitimate users.

Fig. 11 presents the ROC curves and corresponding
EER points for the ZeTHAA, heuristic-based Dasu et al.,
and ML-based MLE-RBA frameworks. The EER point
in the plot represents the balanced operating point at
which false positives equal the missed attacks. The pro-
posed framework consistently achieves a higher TPR at

VOLUME 14, 2026

77875

---

<!-- PAGE 38 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

TABLE 25. Operational efficiency comparison.

TABLE 26. Combined confusion matrix.

entropy and Bayesian-driven parameterization of attribute
weights and penalties provides a robust mechanism for
cold-start initialization and continuous recalibration, address-
ing one of the key limitations in existing systems. The
framework further establishes a clear separation between
intrinsic authentication strength and operational reliability,
enabling consistent mapping to NIST assurance levels. With
evidence-driven decision thresholds, the framework can cap-
ture adversarial behaviors, such as credential stuffing, while
tolerating benign user error. The paper highlights how the
proposed system extends security and risk assessment well
into the resource access phase, a functionality not covered
under conventional AA systems. The proposed multiphase
hybrid evaluation strategy ensures that
the system can
validate risk and trust even in the absence of historical context
or access patterns. The efficacy of the proposed system
was validated on a large-scale synthetic dataset simulating
real-world attack conditions. With novel security checks
extending to newer attributes,e.g., application integrity and
dynamic build secrets, and device posture evaluation, the
proposed system minimizes user friction and ensures the
user obtains only the minimum degree of trust required to
access the intended resources. The proposed ZeTHAA frame-
work provides a coherent, mathematically grounded, and
practically implementable approach to ZT-based continuous
authentication and authorization.

DECLARATIONS
CONFLICTS OF INTEREST
The authors declare no conflicts of interest.

REFERENCES
[1] C. Jacomme and S. Kremer, ‘‘An extensive formal analysis of multi-factor
authentication protocols,’’ ACM Trans. Privacy Secur., vol. 24, no. 2,
pp. 1–34, Jan. 2021, doi: 10.1145/3440712.

[2] S. S. U. Hasan, A. Ghani, A. Daud, H. Akbar, and M. F. Khan, ‘‘A review on
secure authentication mechanisms for mobile security,’’ Sensors, vol. 25,
no. 3, p. 700, Jan. 2025, doi: 10.3390/s25030700.

[3] A. Agarwal, S. B. Verma, and B. K. Gupta, ‘‘A review of cloud security
issues and challenges,’’ ADCAIJ, Adv. Distrib. Comput. Artif. Intell. J.,
vol. 12, Dec. 2023, Art. no. e31459, doi: 10.14201/adcaij.31459.

[4] Y. Chen, Y. Yu, and L. Zhai, ‘‘Infinitygauntlet: Brute-force attack on
smartphone fingerprint authentication,’’ in Proc. 32nd USENIX Conf.
Secur. Symp., 2023, pp. 2027–2041. [Online]. Available: https://dl.acm.
org/doi/10.5555/3620237.3620351

FIGURE 11. ROC curve with EER points.

a lower FPR, indicating superior discrimination capability.
The proposed model achieves the lowest EER (0.1981),
significantly outperforming both the heuristic (0.2992) and
ML-based approaches (0.2729), supporting RQ2 and H2,
which hypothesize improved detection performance and
reduced error trade-offs. ZeTHAA reported approximately
33% reduction in error compared to Dasu et al.

The observations show that

the proposed framework
provides a more favorable balance between false positives
and false negatives, improving both security and usability,
while achieving higher performance, greater efficiency, and
lower operating costs.

VIII. CONCLUSION
Adaptive authentication represents an evolution in security
while maintaining usability as a central design factor.
This paper presents ZeTHAA, a novel, unified, and for-
mally grounded Zero-Trust-based Adaptive Authentication
and continuous authorization framework. By integrating
authentication strength, contextual attributes, behavioral
evidence, and retry dynamics into a time-dependent trust–risk
model,
the proposed approach moves beyond heuristic
scoring systems. A central contribution is the introduction
of a global admissibility predicate, which distinguishes
non-compensable hard violations from probabilistic soft
signals, thereby enabling clear enforcement decisions. The

77876

VOLUME 14, 2026

---

<!-- PAGE 39 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

[5] Q. Wang and D. Wang, ‘‘Understanding failures in security proofs of
multi-factor authentication for mobile devices,’’ IEEE Trans. Inf. Forensics
Security, vol. 18, pp. 597–612, 2023, doi: 10.1109/TIFS.2022.3227753.
[6] D. Wang, X. Zhang, Z. Zhang, and P. Wang, ‘‘Understanding security
failures of multi-factor authentication schemes for multi-server envi-
ronments,’’ Comput. Secur., vol. 88, Jan. 2020, Art. no. 101619, doi:
10.1016/j.cose.2019.101619.

[7] M. Syahreen, N. Hafizah, N. Maarop, and M. Maslinan, ‘‘A sys-
Int. J.
tematic review on multi-factor authentication framework,’’
Adv. Comput. Sci. Appl., vol. 15, no. 5, pp. 1043–1050, 2024, doi:
10.14569/ijacsa.2024.01505105.

[8] E. B. Blancaflor, J. O. Duldulao, J. V. E. Espeño, G. S. M. Patag,
M. T. Menor, and G. L. Intal, ‘‘Advanced phishing techniques: Analyzing
adversary-in-the-middle and browser-in-the-browser attacks in modern
cybersecurity,’’ Cybern. Inf. Technol., vol. 25, no. 1, pp. 55–77, Mar. 2025,
doi: 10.2478/cait-2025-0004.

[9] A. F. Baig and S. Eskeland, ‘‘Security, privacy, and usability in continuous
authentication: A survey,’’ Sensors, vol. 21, no. 17, p. 5967, Sep. 2021, doi:
10.3390/s21175967.

[10] F. Al-Husari, O. Nakov, and P. Nakov, ‘‘Multi-factor authentication fatigue:
A growing concern in user experience and security,’’ in Proc. 60th Int. Sci.
Conf. Inf., Commun. Energy Syst. Technol. (ICEST), Jun. 2025, pp. 1–4,
doi: 10.1109/ICEST66328.2025.11098219.

[11] S. Wiefling, M. Dürmuth, and L. Lo Iacono, ‘‘More than just good
passwords? A study on usability and security perceptions of risk-based
authentication,’’ in Proc. Annu. Comput. Secur. Appl. Conf., Dec. 2020,
pp. 203–218, doi: 10.1145/3427228.3427243.

[12] A. Hassan, B. Nuseibeh, and L. Pasquale,

‘‘Engineering adaptive
authentication,’’ in Proc. IEEE Int. Conf. Autonomic Comput. Self-
Organizing Syst. Companion (ACSOS-C), Sep. 2021, pp. 275–280, doi:
10.1109/ACSOS-C52956.2021.00068.

[13] S. Rose, O. Borchert, S. Mitchell, and S. Connelly,

‘‘Zero trust
architecture,’’ National Institute of Standards and Technology, Tech. Rep.,
2020. [Online]. Available: https://doi.org/10.6028/NIST.SP.800-207
[14] D. Temoshok, D. Proud-Madruga, Y.-Y. Choong, R. Galluzzo, S. Gupta,
C. LaSalle, N. Lefkovitz, and A. Regenscheid, ‘‘Digital identity guide-
lines,’’ National Institute of Standards and Technology, Gaithersburg, MD,
USA, Tech. Rep. 800-63-4, 2025, doi: 10.6028/NIST.SP.800-63-4.
[15] (2021). Web Authentication: An Api for Accessing Public Key Credentials
Level 2. [Online]. Available: https://www.w3.org/TR/webauthn-2/
[16] L. S. Dasu, M. Dhamija, G. Dishitha, A. Vivekanandan, and V. Sarasvathi,
‘‘Defending against
identity threats using risk-based authentication,’’
Cybern. Inf. Technol., vol. 23, no. 2, pp. 105–123, Jun. 2023, doi:
10.2478/cait-2023-0016.
[17] C. Picard and S. Pierre,

‘‘RLAuth: A risk-based authentication
IEEE Access, vol. 11,

system using reinforcement
pp. 61129–61143, 2023, doi: 10.1109/ACCESS.2023.3286376.

learning,’’

[18] V. Unsel, S. Wiefling, N. Gruschka, and L. Lo Iacono, ‘‘Risk-based
authentication for OpenStack: A fully functional implementation and
guiding example,’’ in Proc. 13th ACM Conf. Data Appl. Secur. Privacy,
Apr. 2023, pp. 237–243, doi: 10.1145/3577923.3583634.

[19] I. Matiushin and V. Korkhov,

‘‘MLE-RBA: A machine learning-
empowered risk-based authentication algorithm,’’ in Proc. Comput. Sci.
Appl.-ICCSA Workshops, 2025, pp. 325–339, doi: 10.1007/978-3-031-
97648-3_22.

[20] Y. Zhang, F. Wang, J. Zeng, L. Chen, X. Huang, Z. Li, and K. Xue,
‘‘User behavior-based dynamic authentication design for enhanced identity
security,’’ in Proc. IEEE Int. Conf. Commun., Jun. 2025, pp. 1–6, doi:
10.1109/ICC52391.2025.11161955.

[21] M. Papaioannou, G. Zachos, G. Mantas, and J. Rodriguez, ‘‘Novelty
detection for risk-based user authentication on mobile devices,’’ in
Proc. IEEE Global Commun. Conf., Dec. 2022, pp. 837–842, doi:
10.1109/GLOBECOM48099.2022.10000843.

[22] Q. I. M. Hussain and V. Kale, ‘‘Risk-based adaptive authentication in
mobile network system using dynamic elliptic curve digital signature
algorithm,’’ Concurrency Comput., Pract. Exper., vol. 37, nos. 21–22,
p. 70208, Sep. 2025. [Online]. Available: https://onlinelibrary.wiley.com/
doi/abs/10.1002/cpe.70208

[23] M. Papaioannou, G. Mantas, and J. Rodriguez,

‘‘Risk-based user
authentication for mobile passenger ID devices for land and sea border
control,’’ in Proc. IEEE Int. Medit. Conf. Commun. Netw. (MeditCom),
Sep. 2021, pp. 180–185, doi: 10.1109/MEDITCOM49071.2021.9647603.

[24] A. A. Megahed, M. F. Arnous, Y. Elmoataz, A. Moussa, S. Haitham,
and M. Hany, ‘‘Enhanced security through intelligent risk-based authen-
tication: Leveraging big data and machine learning for real-time threat
mitigation,’’ in Proc. 6th Novel Intell. Lead. Emerg. Sci. Conf. (NILES),
Oct. 2024, pp. 246–249.

[25] M. Al-Zubaidie, Z. Zhang, and J. Zhang, ‘‘RAMHU: A new robust
lightweight scheme for mutual users authentication in healthcare applica-
tions,’’ Secur. Commun. Netw., vol. 2019, pp. 1–26, Mar. 2019. [Online].
Available: https://onlinelibrary.wiley.com/doi/abs/10.1155/2019/3263902
[26] A. Acar, H. Aksu, A. S. Uluagac, and K. Akkaya, ‘‘A usable and robust
continuous authentication framework using wearables,’’ IEEE Trans.
Mobile Comput., vol. 20, no. 6, pp. 2140–2153, Jun. 2021.

[27] A. Buriro, S. Gupta, A. Yautsiukhin, and B. Crispo, ‘‘Risk-driven
behavioral biometric-based one-shot-cum-continuous user authentication
scheme,’’ J. Signal Process. Syst., vol. 93, no. 9, pp. 989–1006, Sep. 2021,
doi: 10.1007/s11265-021-01654-2.

[28] Z. Shen, S. Li, X. Zhao, and J. Zou,

‘‘MMAuth: A continuous
authentication framework on smartphones using multiple modalities,’’
IEEE Trans. Inf. Forensics Security, vol. 17, pp. 1450–1465, 2022, doi:
10.1109/TIFS.2022.3160361.

[29] Y. Liang, S. Samtani, B. Guo, and Z. Yu, ‘‘Behavioral biometrics for
continuous authentication in the Internet-of-Things era: An artificial
IEEE Internet Things J., vol. 7, no. 9,
intelligence perspective,’’
pp. 9128–9143, Sep. 2020, doi: 10.1109/JIOT.2020.3004077.

[30] M. Mekni, E. O. Ogunwobi, and S. C. Russell, ‘‘Context-adaptive gait
biometrics for real-time continuous authentication,’’ in Proc. Int. Conf.
Adv. Mach. Learn. Data Sci. (AMLDS), Jul. 2025, pp. 799–807.

[31] S. W. Shah, N. F. Syed, A. Shaghaghi, A. Anwar, Z. Baig, and R. Doss,
‘‘LCDA: Lightweight continuous device-to-device authentication for a
zero trust architecture (ZTA),’’ Comput. Secur., vol. 108, Sep. 2021,
Art. no. 102351, doi: 10.1016/j.cose.2021.102351.

[32] G. Dahia, L. Jesus, and M. Pamplona Segundo, ‘‘Continuous authentica-
tion using biometrics: An advanced review,’’ WIREs Data Mining Knowl.
Discovery, vol. 10, no. 4, p. 1365, Jul. 2020, doi: 10.1002/widm.1365.
[33] A. F. Baig, S. Eskeland, and B. Yang, ‘‘Privacy-preserving continuous
authentication using behavioral biometrics,’’ Int. J. Inf. Secur., vol. 22,
no. 6, pp. 1833–1847, Dec. 2023, doi: 10.1007/s10207-023-00721-y.
J. Singh,

[34] S. Ayeswarya

and K.
review
user
biometric-based
IEEE Access, vol. 12, pp. 82996–83021, 2024, doi:

‘‘A comprehensive
authentication

secure
on
profiling,’’
10.1109/ACCESS.2024.3411783.

continuous

and

[35] S. Ambol and S. Rashad, ‘‘Continuous authentication of smartphone users
using machine learning,’’ in Proc. 11th IEEE Annu. Ubiquitous Comput.,
Electron. Mobile Commun. Conf. (UEMCON), Oct. 2020, pp. 0056–0062,
doi: 10.1109/UEMCON51285.2020.9298040.

and D. Hardin,
[36] S. Hasan,
and
cyber–physical
Archit., vol. 155, Oct. 2024, Art. no. 103261.
https://www.sciencedirect.com/science/article/pii/S138376212400198X

design
‘‘Zero-trust
Syst.
systems,’’
[Online]. Available:

I. Amundson,
patterns

assurance

for

J.

[37] P. Phiayura

and S. Teerakanok,

for migrating to zero trust architecture,’’
pp. 19487–19511, 2023.

‘‘A comprehensive

framework
IEEE Access, vol. 11,

[38] Z. Adahman, A. W. Malik, and Z. Anwar, ‘‘An analysis of zero-trust
architecture and its cost-effectiveness for organizational security,’’ Com-
put. Secur., vol. 122, Nov. 2022, Art. no. 102911. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0167404822003042

[39] C. Liu, R. Tan, Y. Wu, Y. Feng, Z. Jin, F. Zhang, Y. Liu, and Q. Liu,
‘‘Dissecting zero trust: Research landscape and its implementation in IoT,’’
Cybersecurity, vol. 7, no. 1, p. 20, May 2024, doi: 10.1186/s42400-024-
00212-0.

[40] W. Yeoh, M. Liu, M. Shore, and F. Jiang, ‘‘Zero trust cybersecurity: Critical
success factors and a maturity assessment framework,’’ Comput. Secur.,
vol. 133, Oct. 2023, Art. no. 103412, doi: 10.1016/j.cose.2023.103412.

[41] E. W. Tomlinson, W. D. Abrha, S. D. Kim, and S. A. Ortega, ‘‘Cyber-
security access control: Framework analysis in a healthcare institution,’’
J. Cybersecurity Privacy, vol. 4, no. 3, pp. 762–776, Sep. 2024, doi:
10.3390/jcp4030035.

[42] Y. Kim, S.-G. Sohn, K. T. Kim, H. S. Jeon, S.-M. Lee, Y. Lee, and J. Kim,
‘‘Exploring effective zero trust architecture for defense cybersecurity: A
study,’’ KSII Trans. Internet Inf. Syst., vol. 18, no. 9, pp. 2665–2691,
Sep. 2024, doi: 10.3837/tiis.2024.09.011.

VOLUME 14, 2026

77877

---

<!-- PAGE 40 -->

V. Krishnan, C. S. Sreeja: Provably Adaptive Trust Dynamics in Context-Aware Zero-Trust Systems

[43] B. Hale, D. L. Van Bossuyt, N. Papakonstantinou, and B. O’Halloran,
‘‘A zero-trust methodology for security of complex systems with machine
learning components,’’ in Proc. 41st Comput. Inf. Eng. Conf. (CIE),
Aug. 2021, p. 002, doi: 10.1115/detc2021-70442.

[44] V. Krishnan and C. S. Sreeja, ‘‘Zero trust-based adaptive authentication
using composite attribute set,’’ in Proc. IEEE 3rd PhD Colloq. Ethically
Driven Innov. Technol. Soc. (PhD EDITS), Nov. 2021, pp. 1–2, doi:
10.1109/PHDEDITS53295.2021.9649474.

[45] I. Ahmed, T. Nahar, S. S. Urmi, and K. A. Taher, ‘‘Protection of sensitive
data in zero trust model,’’ in Proc. Int. Conf. Comput. Advancements,
Jan. 2020, pp. 1–5, doi: 10.1145/3377049.3377114.

[46] A. Qazi and S. Arshad, ‘‘Implementation of enhanced security measures in
Oracle ERP cloud with zero trust architecture (ZTA),’’ in Proc. Int. Conf.
Commun. Technol. (ComTech), Apr. 2025, pp. 1–6.

[57] National Institute of Standards and Technology. (2012). Guide for
Conducting Risk Assessments. [Online]. Available: https://nvlpubs.nist.
gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf

[58] National Institute of Standards and Technology. (2018). Risk Manage-
ment Framework for Information Systems and Organizations. [Online].
Available: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.
800-37r2.pdf

[59] (2024). OWASP Authentication Cheat Sheet. [Online]. Available: https://

cheatsheetseries.owasp.org/cheatsheets/AuthenticationCheatSheet.html

[60] N. Harwood-Nash. (Jun. 2023). How Fast Do Planes Fly. [Online].

Available: https://airadvisor.com/en/blog/how-fast-do-planes-fly

[61] V. Krishnan. (2026). ZeTHAA. [Online]. Available: https://github.com/

vivinkrishnan/ZeTHAA

[47] A. Farraj, ‘‘On using zero trust to securing industrial control systems in
the power systems industry,’’ in Proc. IEEE Texas Power Energy Conf.
(TPEC), Feb. 2025, pp. 1–5, doi: 10.1109/TPEC63981.2025.10906998.
for
‘‘Blockchain-enabled zero trust
privacy-preserving cybersecurity in IoT environments,’’ IEEE Access,
vol. 13, pp. 18660–18676, 2025, doi: 10.1109/ACCESS.2025.3529309.

[48] M. A. Aleisa,

architecture

[49] M. Tsai, S. Lee, and S. W. Shieh, ‘‘Strategy for implementing of zero trust
architecture,’’ IEEE Trans. Rel., vol. 73, no. 1, pp. 93–100, Mar. 2024, doi:
10.1109/TR.2023.3345665.

[50] A. Hassan, A. Rauf, N. Shafqat, R. Latif, and H. Khan, ‘‘ZenGuard a
machine learning based zero trust framework for context aware threat
mitigation using SIEM SOAR and UEBA,’’ Sci. Rep., vol. 15, no. 1,
p. 35871, Oct. 2025, doi: 10.1038/s41598-025-20998-4.

[51] N. F. Syed, S. W. Shah, A. Shaghaghi, A. Anwar, Z. Baig, and R. Doss,
‘‘Zero trust architecture (ZTA): A comprehensive survey,’’ IEEE Access,
vol. 10, pp. 57143–57179, 2022.

[52] E. Hosney, I. Halim, and A. H. Yousef, ‘‘An artificial intelligence approach
for deploying zero trust architecture (ZTA),’’ in Proc. 5th Int. Conf.
Comput. Inform. (ICCI), Mar. 2022, pp. 343–350.

[53] E. Bertino, ‘‘Zero trust architecture: Does it help?’’ IEEE Secur. Privacy,
vol. 19, no. 5, pp. 95–96, Sep. 2021, doi: 10.1109/MSEC.2021.3091195.
[54] L. Bradatsch, O. Miroshkin, N. Trkulja, and F. Kargl, ‘‘Zero trust score-
based network-level access control in enterprise networks,’’ in Proc. IEEE
22nd Int. Conf. Trust, Secur. Privacy Comput. Commun. (TrustCom),
CA. Los Alamitos, CA, USA: IEEE Computer Society, Nov. 2023,
pp. 1422–1429. [Online]. Available: https://doi.ieeecomputersociety.org/
10.1109/TrustCom60117.2023.00194

[55] Q. Yao, Q. Wang, X. Zhang, and J. Fei, ‘‘Dynamic access control
and authorization system based on zero-trust architecture,’’ in Proc.
Int. Conf. Control, Robot. Intell. Syst., Oct. 2020, pp. 123–127, doi:
10.1145/3437802.3437824.

[56] Special Publication 800-63b: Digital Identity Guidelines: Authentication
and Authenticator Management, National Institute of Standards and
Technology, Gaithersburg, MD, USA, 2025, doi: 10.6028/NIST.SP.800-
63B-4.

VIVIN KRISHNAN received the master’s degree
in technology from Cochin University of Science
and Technology. He is currently a Software Archi-
tect with Numentica Technologies, Bengaluru.
He is a Research Scholar at CHRIST (Deemed
to be University), Bengaluru. He has more than
18 years of IT experience. His areas of interest
include information security, authentication, and
scalable software systems.

C. S. SREEJA (Senior Member, IEEE) received
the Ph.D. degree from CHRIST (Deemed to
be University), Bengaluru, which focused on
Information security aspects. She is an Assistant
Professor with the Quantum Technologies and
Complex Systems (CQTCS), CHRIST (Deemed
to be University), where she has been a Faculty
Member, since 2019. She has published her
research work in peer-reviewed journals, including
Elsevier and Inderscience, and in the proceedings
of renowned International conferences by IEEE, Springer, and ACM. Her
area of expertise in research includes, but is not limited to, information
security, authentication, public key cryptography, E-signature, bio-molecular
computing, DNA cryptography, and blockchain. She also received the
IEEE best thesis award (second) for her Ph.D. Thesis during the Graduate
Congress GraTE ’7’ 2019. She also served as a reviewer for prestigious IEEE
Conferences, the Session Chair, and the Publications Co-Chair for the IEEE
PhD Colloquium on Ethically Driven Innovation and Technology for Society
2019 and 2020. She is an active member of the IEEE ComSoc Bangalore
Chapter.

77878

VOLUME 14, 2026

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received24April2026,accepted13May2026,dateofpublication20May2026,dateofcurrentversion27May2026.
DigitalObjectIdentifier10.1109/ACCESS.2026.3695458
Provably Adaptive Trust Dynamics in
Context-Aware Zero-Trust Systems: A Formal
Framework for Continuous Verification
VIVINKRISHNAN 1 ANDC.S.SREEJA 2,(SeniorMember,IEEE)
1DepartmentofComputerScience,CHRIST(DeemedtobeUniversity),Bengaluru,Karnataka560029,India
2CenterforQuantumTechnologiesandComplexSystems(CQTCS),CHRIST(DeemedtobeUniversity),Bengaluru,Karnataka560029,India
Correspondingauthor:VivinKrishnan(vivin.krishnan@res.christuniversity.in)
ABSTRACT Zero-Trust (ZT) requires continuous, context-aware evaluation of authentication and
authorization decisions. This paper introduces Zero-Trust Hybrid Adaptive Authentication (ZeTHAA),
a continuous authentication and authorization framework integrating contextual attributes, authentication
strength, behavioral evidence, and retry dynamics. ZeTHAA utilizes a probabilistic risk model and
dual-policythresholdstopartitionoutcomesintoallow,step-up,andblockregions,enablingprecisecontrol
over security–usability trade-offs. The system introduces a global admissibility predicate to distinguish
hardviolationsfromprobabilisticsoftviolations.Attributeimportanceisdynamicallyderivedfromentropy
andBeta-posteriordistribution,enablingrobustcold-startinitializationandonlinerecalibration.ZeTHAA
presents a unified composite attack surface covering credential compromise, attribute forgery, and post-
grant hijacking, modeling retry behavior with exponential risk escalation and temporal decay. A large-
scalesyntheticdatasetcapturingrealisticauthenticationflows,adversarialandtemporalpatterns,wasused
to evaluate ZeTHAA against heuristic, logistic regression, random forest, XGBoost, and isolation forest
baselines.ZeTHAAproducedamoreexpressiveriskdistributionandsignificantlyhigherattackdetection
andefficiencywhileminimizinguserfriction.ZeTHAAoutperformedbaselinemodels,withRecallandArea
UndertheCurve(AUC)exceeding79%and15.1%,respectively.F1-Scoreshowedincreasesof48%-147%,
with efficiency boost of 20-65%, while reducing the cost per attack by up to 39.6%. Benchmarks against
frameworks from Dasu et al. and Matiushin et al. showed a 57.5% lead in F1-Score, more than double
increase in detection rate, while blocking 70.78% more attacks. Additional analysis shows that ZeTHAA
providesamathematicallygroundedfoundationforZero-Trustsystems,alignswithNISTstandards,offering
improvedsecurityguaranteesandadaptiveenforcement.
INDEXTERMS Adaptiveauthentication,applicationintegritycheck,Bayesianonlinelearning,continuous
authentication,deviceauthentication,dynamicsecretinjection,risk-basedaccesscontrol.
I. INTRODUCTION The need for secure authentication accelerated the devel-
Single-factor authentication (SFA) schemes have been the opmentofmultifactorauthentication(MFA)systems,which
mainstay of authentication because of their usability and are more secure [5], [6]; however, MFA remains a static
easeofimplementation[1].However,ascomputingresources approachthatreliesonsequentialchainingofauthentication
andthreatvectorsbecomeincreasinglysophisticated,attacks challenges [7]. Blancaflor et al. [8] reported sophisticated
on SFA systems have become commonplace [2], [3]. With attack measures that specifically target MFA systems. The
SFA, the attacker must focus on breaking only a single layering of challenges also contributes to user friction
authenticationmethod[4]. and reduces usability and adoption [9]. Traditional MFA
techniques,whileeffectiveinbolsteringsecurity,frequently
The associate editor coordinating the review of this manuscript and leadto‘‘MFAfatigue’’anduserfrustrationduetorepetitive
approvingitforpublicationwasSedatAkleylek . prompts,eveninlow-riskscenarios[10].
2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME14,2026 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 77839

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Consequently, Adaptive Authentication (AA) systems, posture,behavioralcontext,accessmedium,application
which utilize users’ behavioral and contextual patterns to attributes, and threat indicators) and transforms them
challengeuserssparinglywhenbehaviordeviatesfromestab- intoanormalizedriskmetricfortrustevolution.
lishedpatterns,havegainedpopularity[11].AAincorporates • Trustevolutionwithreinforcementandtemporaldecay
contextual signals such as device posture, geolocation, dynamics.
behavioral biometrics, and network attributes to compute • Parameterization and recalibration of weighting and
dynamicriskscores.Whenthebehavioralcontextofarequest penaltycoefficients.
varies from the established profile, the system selects an • Explicitmappingoftruststatetopolicydecisionswithin
alternative authentication modality to challenge the user. ZeroTrustarchitecture.
The complexity of the selected alternative authentication • Standards-aligned architectural integration, including
modality is proportional to the risk of malicious agents identity,application,anddevicetrustconsiderations.
accessing resources. In contrast to MFA, AA employs a Formulate and evaluate a hypothesis that policy-aware
•
dynamic strategy in which risk factors are considered when multi-threshold authentication improves the trade-off
selecting the subsequent action. This evolution in security betweensecurityandusability.
design is largely driven by the inherent tension between The remainder of this paper is organized as follows.
| achieving | robust | protection | and | maintaining | enhanced | user |         |             |     |          |           |     |                |     |
| --------- | ------ | ---------- | --- | ----------- | -------- | ---- | ------- | ----------- | --- | -------- | --------- | --- | -------------- | --- |
|           |        |            |     |             |          |      | Section | II outlines | the | research | questions |     | and hypotheses |     |
experiences[12].
|     |     |     |     |     |     |     | guiding | the proposed |     | framework. |     | Section | III presents | the |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ---------- | --- | ------- | ------------ | --- |
As authentication systems began to incorporate adaptive foundational principles of Zero Trust Architecture and
| and risk-based |     | authentication |     | (RBA), a | new cybersecurity |     |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | -------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
relevantstandards.SectionIVpresentsadetailedanalysisof
design paradigm, i.e., zero-trust (ZT), evolved in parallel, theexistingliteratureinthefieldandidentifieskeyresearch
withmanyenterprisesadoptingitasthedrivingprinciple.ZT, gaps. Section V discusses the methodology of the proposed
| which revolves |     | around | the principle | of  | ‘‘never | trust, always |        |           |     |                |     |     |                 |     |
| -------------- | --- | ------ | ------------- | --- | ------- | ------------- | ------ | --------- | --- | -------------- | --- | --- | --------------- | --- |
|                |     |        |               |     |         |               | ZeTHAA | framework |     | and formulates |     | the | trust evolution |     |
verify’’,ensuresthatnoimplicittrustisassignedtousersor model. Section VI formalizes the security guarantees of the
resourcesregardlessoflocation(physicalornetwork)[13].
|     |     |     |     |     |     |     | ZeTHAA | framework, |     | followed | by  | experimental | evaluation |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | -------- | --- | ------------ | ---------- | --- |
However, many risk-based systems rely on heuristic or and findings in section VII. Finally, Section VIII concludes
| proprietary  | scoring      | mechanisms, |               | and             | they typically | lack        | thepaper. |     |     |     |     |     |     |     |
| ------------ | ------------ | ----------- | ------------- | --------------- | -------------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| a formalized | mathematical |             |               | model governing |                | trust accu- |           |     |     |     |     |     |     |     |
| mulation,    | decay,       | and         | re-evaluation | over            | time.          | This gap    |           |     |     |     |     |     |     |     |
II. RESEARCHQUESTIONSANDHYPOTHESES
| motivates | a transition |     | from | authentication-centric |     | security |              |     |             |     |            |     |            |     |
| --------- | ------------ | --- | ---- | ---------------------- | --- | -------- | ------------ | --- | ----------- | --- | ---------- | --- | ---------- | --- |
|           |              |     |      |                        |     |          | We establish | the | theoretical |     | foundation | by  | presenting | the |
toarchitecturalparadigmsthatassumepersistentadversarial
researchquestionsandhypothesesthatunderpintheproposed
presence.
framework.
| This          | paper | presents   | ZeTHAA | - a      | novel | convergence |     |     |     |     |     |     |     |     |
| ------------- | ----- | ---------- | ------ | -------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| of Zero-Trust |       | philosophy | into   | Adaptive | and   | Continuous  |     |     |     |     |     |     |     |     |
A. RESEARCHQUESTIONS
| Authentication. |     | This | work | is based | on the | hypothesis |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ---- | -------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
AAandRBAsystemshavetraditionallyfocusedonimprov-
| that incorporating |     | policy-aware, |     | multi-threshold |     | decision |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------------- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ingclassificationaccuracythroughenhancedriskestimation
| mechanisms  | into        | risk-based |          | authentication | systems | leads          |                 |                |                     |         |     |              |          |          |
| ----------- | ----------- | ---------- | -------- | -------------- | ------- | -------------- | --------------- | -------------- | ------------------- | ------- | --- | ------------ | -------- | -------- |
|             |             |            |          |                |         |                | using heuristic |                | or machine-learning |         |     | approaches.  | However, |          |
| to improved | operational |            | outcomes | compared       |         | to traditional |                 |                |                     |         |     |              |          |          |
|             |             |            |          |                |         |                | real-world      | authentication |                     | systems |     | must balance |          | security |
single-thresholdapproaches.TheproposedZero-Trust-based
|                  |     |                |        |                   |          |           | (attack        | detection) | with     | usability   | (user | friction | and       | cost), |
| ---------------- | --- | -------------- | ------ | ----------------- | -------- | --------- | -------------- | ---------- | -------- | ----------- | ----- | -------- | --------- | ------ |
| hybrid Adaptive  |     | Authentication |        | system            | operates | on a com- |                |            |          |             |       |          |           |        |
|                  |     |                |        |                   |          |           | with decisions |            | governed | by policies |       | rather   | than risk | scores |
| posite attribute |     | set that       | covers | all participating |          | discrete  |                |            |          |             |       |          |           |        |
alone.
| entities. | The system |          | covers | the actor,         | the | medium of |         |          |      |      |           |     |               |     |
| --------- | ---------- | -------- | ------ | ------------------ | --- | --------- | ------- | -------- | ---- | ---- | --------- | --- | ------------- | --- |
|           |            |          |        |                    |     |           | In this | context, | this | work | is guided | by  | the following |     |
| access,   | and the    | platform | it     | runs, establishing |     | a ‘‘who - |         |          |      |      |           |     |               |     |
researchquestions:
| uses what | - on | which’’ | relationship. | This | allows | for the |     |     |     |     |     |     |     |     |
| --------- | ---- | ------- | ------------- | ---- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
• RQ1:Doesincorporatingpolicy-aware,multi-threshold
| collection | of a | wider | range | of attributes | while | employ- |     |     |     |     |     |     |     |     |
| ---------- | ---- | ----- | ----- | ------------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ing a minimally invasive profile. The hybrid nature of decision mechanisms improve the trade-off between
|              |        |     |         |                |     |            | security | and | usability | compared |     | to traditional |     | single- |
| ------------ | ------ | --- | ------- | -------------- | --- | ---------- | -------- | --- | --------- | -------- | --- | -------------- | --- | ------- |
| the proposed | system |     | enables | the validation | of  | contextual |          |     |           |          |     |                |     |         |
thresholdRBAapproaches?
attributes,groupedbytheircomposition,inparallel,thereby
• RQ2:Canmulti-stagedecisionregions(allow,step-up,
allowingfasteroutcomes.Thekeycontributionsofthispaper
block)reducefalseblockingrateswithoutsignificantly
are:
• Formalization of trust as a continuous, time-evolving, degradingattackdetectionperformance?
|     |         |       |          |             |          |         | • RQ3:  | Does       | the calibration |         | of  | model outputs |         | to oper- |
| --- | ------- | ----- | -------- | ----------- | -------- | ------- | ------- | ---------- | --------------- | ------- | --- | ------------- | ------- | -------- |
| and | bounded | state | variable | rather than | a binary | policy- |         |            |                 |         |     |               |         |          |
|     |         |       |          |             |          |         | ational | thresholds |                 | improve | the | alignment     | between | risk     |
basedoutcome.
Assurance-awareTrustinitialization,integratingauthen- estimationandauthenticationdecisions?
•
ticationandidentitystrengths. These questions aim to shift the focus from risk pre-
• Contextual Risk aggregation framework that inte- diction alone to decision effectiveness under operational
| grates | multi-dimensional |     |     | contextual | signals | (device | constraints. |     |     |     |     |     |               |     |
| ------ | ----------------- | --- | --- | ---------- | ------- | ------- | ------------ | --- | --- | --- | --- | --- | ------------- | --- |
| 77840  |                   |     |     |            |         |         |              |     |     |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| B. RESEARCHHYPOTHESES |     |     |     |     |     |     | ThecoreprinciplesofZTAinclude: |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Based on the above research questions, we formulate the • Eliminationofimplicittrust
followinghypotheses:
• Leastprivilegeaccessenforcement
• H1 (Trade-off Hypothesis): A policy-aware, dual- • Strictauthenticationandauthorizationactions
threshold authentication framework achieves a bet- • Continuous evaluation of signals for data-driven
| ter | balance | between | security |     | and usability | than |     |     |     |     |     |     |     |     |
| --- | ------- | ------- | -------- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
decisions
single-thresholdAAorRBAapproaches. • DynamicPolicy-drivendecisionmechanisms
| • H2 | (Decision | Structure | Hypothesis): |     | Multi-threshold |     |     |     |     |     |     |     |     |     |
| ---- | --------- | --------- | ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
UndertheZTA,trustistreatedasdynamicandcontextual
| decision    |     | regions reduce |     | false-blocking |                  | rates while |             |           |         |              |              |        |            |      |
| ----------- | --- | -------------- | --- | -------------- | ---------------- | ----------- | ----------- | --------- | ------- | ------------ | ------------ | ------ | ---------- | ---- |
|             |     |                |     |                |                  |             | rather than | static    | and     | rule-driven. |              | Access | decisions  | are  |
| maintaining |     | comparable     | or  | improved       | attack-detection |             |             |           |         |              |              |        |            |      |
|             |     |                |     |                |                  |             | evaluated   | by policy | engines |              | that analyze |        | continuous | data |
performance.
|      |              |              |     |             |     |          | supplied | across | sources. | However, |     | while | ZTA articulates |     |
| ---- | ------------ | ------------ | --- | ----------- | --- | -------- | -------- | ------ | -------- | -------- | --- | ----- | --------------- | --- |
| • H3 | (Calibration | Hypothesis): |     | Calibration |     | of model |          |        |          |          |     |       |                 |     |
architecturalcomponents—policyenforcementpoints,policy
| outputs | to  | policy thresholds |     | improves | the | alignment |          |         |           |        |     |               |      |     |
| ------- | --- | ----------------- | --- | -------- | --- | --------- | -------- | ------- | --------- | ------ | --- | ------------- | ---- | --- |
|         |     |                   |     |          |     |           | decision | points, | and trust | signal |     | collectors—it | does | not |
between risk scores and authentication decisions, formallydefineaquantitativetrustfunctionoramethodology
enablingmoreeffectiveutilizationofdecisionregions.
forcontinuoustrustevolution.
C. HYPOTHESISEVALUATIONSTRATEGY
B. IDENTITYASSURANCEANDAUTHENTICATOR
| The hypotheses |     | were evaluated |     | through | a comprehensive |     |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
STRENGTH
| experimental | framework |     | using a | held-out | test dataset. | Each |     |     |     |     |     |     |     |     |
| ------------ | --------- | --- | ------- | -------- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
NISTSP800-63,referredtoas‘‘DigitalIdentityGuidelines’’,
hypothesisistestedusingspecificmetrics:
standardizesauthenticationandidentityproofingforprivate
| • Operational |          | Trade-off | (H1): | Assessed |       | using cost- |            |        |              |     |           |        |            |     |
| ------------- | -------- | --------- | ----- | -------- | ----- | ----------- | ---------- | ------ | ------------ | --- | --------- | ------ | ---------- | --- |
|               |          |           |       |          |       |             | and public | sector | enterprises. |     | It covers | a Risk | Management |     |
| based         | metrics, | step-up   | rate, | block    | rate, | and false   |            |        |              |     |           |        |            |     |
Framework,alongwithIdentityandauthenticationlifecycle
| block | rate, | capturing | the | balance | between | security |     |     |     |     |     |     |     |     |
| ----- | ----- | --------- | --- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
management,assurances,andassertions[14].
enforcementanduserfriction.
ThisframeworkdefinesIdentityAssuranceLevels(IAL),
| • Discrimination |     | Performance  |                | (H2): | Evaluated | using        |               |           |           |         |          |          |                   |         |
| ---------------- | --- | ------------ | -------------- | ----- | --------- | ------------ | ------------- | --------- | --------- | ------- | -------- | -------- | ----------------- | ------- |
|                  |     |              |                |       |           |              | Authenticator |           | Assurance | Levels  | (AAL),   |          | and Federation    |         |
| Receiver         |     | Operating    | Characteristic |       | (ROC)     | curves, Area |               |           |           |         |          |          |                   |         |
|                  |     |              |                |       |           |              | Assurance     | Levels    | (FAL)     | for     | identity | proofing | and               | authen- |
| Under            | the | Curve (AUC), | and            | Equal | Error     | Rate (EER),  |               |           |           |         |          |          |                   |         |
|                  |     |              |                |       |           |              | tication      | strength. | AAL       | defines | metrics  |          | that characterize |         |
whichmeasuretheabilitytodistinguishbetweenbenign
|     |     |     |     |     |     |     | the strength | of  | an authentication |     | process. |     | AALs 1-3 | offer |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------------- | --- | -------- | --- | -------- | ----- |
andmaliciousevents.
|     |     |     |     |     |     |     | an indicator | of  | confidence |     | in an | authentication | method. |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | ----- | -------------- | ------- | --- |
• DecisionAlignment(H3):Analyzedthroughcalibrated
|     |     |     |     |     |     |     | Higher assurance |     | levels | (e.g., | AAL2 | and | AAL3) mandate |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------ | ---- | --- | ------------- | --- |
riskscoredistributions,decisionboundaryanalysis,and
|             |     |          |         |          |         |        | stronger | authenticators, |     | including | cryptographic |     | hardware- |     |
| ----------- | --- | -------- | ------- | -------- | ------- | ------ | -------- | --------------- | --- | --------- | ------------- | --- | --------- | --- |
| region-wise |     | behavior | (allow, | step-up, | block), | demon- |          |                 |     |           |               |     |           |     |
boundcredentials.
| strating | how | well | model | outputs | align | with policy |          |       |           |     |      |        |                |     |
| -------- | --- | ---- | ----- | ------- | ----- | ----------- | -------- | ----- | --------- | --- | ---- | ------ | -------------- | --- |
|          |     |      |       |         |       |             | Although | these | standards |     | help | choose | authentication |     |
thresholds.
methodsbasedonsecurityneeds,theyremainlargelyfocused
Acomparativeevaluationwasconductedagainstheuristic
|             |                |     |           |     |             |          | on the strength |             | of the authentication |       |        | event  | itself. Assurance |     |
| ----------- | -------------- | --- | --------- | --- | ----------- | -------- | --------------- | ----------- | --------------------- | ----- | ------ | ------ | ----------------- | --- |
| and machine | learning-based |     | baselines |     | to validate | the pro- |                 |             |                       |       |        |        |                   |     |
|             |                |     |           |     |             |          | levels do       | not specify | how                   | trust | should | decay, | accumulate,       |     |
posedhypotheses.
|                  |       |                |           |                |            |             | or be recalibrated |             | during | an     | active     | session, | nor    | do they |
| ---------------- | ----- | -------------- | --------- | -------------- | ---------- | ----------- | ------------------ | ----------- | ------ | ------ | ---------- | -------- | ------ | ------- |
| Together,        | these | research       | questions | and            | hypotheses | estab-      |                    |             |        |        |            |          |        |         |
|                  |       |                |           |                |            |             | address            | the dynamic |        | threat | conditions | that     | emerge | after   |
| lish a framework |       | for evaluating |           | authentication |            | systems not |                    |             |        |        |            |          |        |         |
sessionestablishment.
| only in     | terms    | of predictive | accuracy, |             | but also | in terms   |     |     |     |     |     |     |     |     |
| ----------- | -------- | ------------- | --------- | ----------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| of decision | quality, | operational   |           | efficiency, | and      | real-world |     |     |     |     |     |     |     |     |
C. PHISHING-RESISTANTAUTHENTICATIONANDFIDO
applicability.
|     |     |     |     |     |     |     | The FIDO | Alliance | and | W3C’s | work | on  | phishing-resistant |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ----- | ---- | --- | ------------------ | --- |
III. ZEROTRUSTARCHITECTUREANDSTANDARDS andlargelypasswordlessauthenticationmethodsresultedin
| CONTEXT |     |     |     |     |     |     | theFIDO2frameworkandtheWebAuthnstandard[15]. |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
A. ZEROTRUSTARCHITECTURE FIDO-based authentication aims to eliminate or replace
The Zero Trust paradigm operates on the tenet of ‘‘no shared secrets such as passwords or OTPs with public-key
implicit trust’’. ZT assumes that no entity is trustworthy, cryptography,whereprivatekeysaresecurelyboundtouser
regardless of user identity, network, or device posture. The devices and never transmitted over the network. By lever-
keyprinciplesandcomponentsoftheZeroTrustArchitecture aging device-bound hardware credentials, this architecture
(ZTA) have been formalized by the National Institute of provides strong resistance to phishing attacks, credential
Standards and Technology under NIST SP 800-207 [13]. replays,etc.,significantlystrengtheningauthentication.
ZTA mandates continuous authentication, and verification Nevertheless,similartootherauthenticationmechanisms,
of identity, device, and contextual attributes across all data FIDO aims to secure the authentication event rather than
points at all times before granting access to protected definingcontinuoustrustevaluationmechanismsthroughout
resources. thelifeofauthenticatedsessions.Theydonotprovideformal
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 77841 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
models for adaptive trust recalibration or continuous risk modalitiesbasedonauser’scontext.Theworkconcentrated
aggregation. onaccesstomobiledeviceapplicationsbasedonusercontext
andresourcesensitivity.AlthoughtheDRLapproachenables
|     |     |     |     |     |     | rapid learning | and | inference, | the system |     | lacks cold-start |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ---------- | --- | ---------------- | --- |
D. ARCHITECTURALGAPSINSTANDARDS-BASEDZERO
TRUSTIMPLEMENTATIONS initializationwhennopriordataareavailable.
Zero Trust architecture and identity assurance standards AnRBAimplementationforOpenStackwaspresentedby
|         |          |           |            |        |          | Unsel et al. | in [18]. | This study | attempts | to mitigate |     | the low |
| ------- | -------- | --------- | ---------- | ------ | -------- | ------------ | -------- | ---------- | -------- | ----------- | --- | ------- |
| provide | a robust | framework | for secure | access | control. |              |          |            |          |             |     |         |
However,theydonotdefineacomputationalmodelfortrust adoptionratesofRBA.However,theframeworkusesonlythe
IPaddress,round-trip-time(RTT),andUser-Agenttoevaluate
evaluationandrecalibration.Thisresultsinimplementations
relyingonarbitraryorheuristicscoringapproaches. variance from baseline behavior. Matiushin et al. proposed
|                |            |             |             |        |          | Machine    | Learning-Empowered |          | Risk-Based |             | Authentication |          |
| -------------- | ---------- | ----------- | ----------- | ------ | -------- | ---------- | ------------------ | -------- | ---------- | ----------- | -------------- | -------- |
| • Trust        | is treated | as a policy | outcome     | rather | than as  |            |                    |          |            |             |                |          |
|                |            |             |             |        |          | (MLE-RBA), | a LightGBM-based   |          | RBA        | framework,  |                | in [19]. |
| a continuously |            | monitored,  | measurable, | and    | evolving |            |                    |          |            |             |                |          |
|                |            |             |             |        |          | Although   | MLE-RBA            | operates | on a       | dynamically | computed       |          |
variable.
|     |     |     |     |     |     | binary threshold, |     | it focuses | on the mathematical |     | optimality |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | ------------------- | --- | ---------- | --- |
• Thereisnoformaldefinitionofhowcontextualsignals
|      |           |             |            |     |             | and does | not account | for | user friction | in  | the outcome. |     |
| ---- | --------- | ----------- | ---------- | --- | ----------- | -------- | ----------- | --- | ------------- | --- | ------------ | --- |
| from | different | sources are | aggregated | and | transformed |          |             |     |               |     |              |     |
Inaddition,theframeworkassumesthatpriordataisavailable
intoquantitativetrustmetrics.
|     |     |     |     |     |     | to compute | the threshold. |     | Further studies | on  | risk-based | and |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | --------------- | --- | ---------- | --- |
Theparameterizationofreinforcingweightsordegrad-
•
|     |     |     |     |     |     | AA have | been proposed |     | by [20], | [21], [22], | [23], | [24], |
| --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | -------- | ----------- | ----- | ----- |
ingpenaltiesandtheirformulationisnotdefined.
and[25]thatutilizevariousattributessuchasusagepatterns,
| • Trust | decay, | recalibration, | and | convergence | during |     |     |     |     |     |     |     |
| ------- | ------ | -------------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
behavioralbiometrics,andsmartphoneusage.However,these
ongoingsessionsarenotmodeledformally.
|     |     |     |     |     |     | studies propose | binary | decision-making |     | systems | based | on  |
| --- | --- | --- | --- | --- | --- | --------------- | ------ | --------------- | --- | ------- | ----- | --- |
These limitations highlight a critical research gap: the singularbehavioralaspects,thatareindividuallysusceptible
| lack of | a formal | mathematical | framework |     | capable of |     |     |     |     |     |     |     |
| ------- | -------- | ------------ | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
tospoofing.
modelingcontinuous,adaptivetrustcomputationwithinZero
|                      |     |               |         |         |          | RBA and | AA systems | focus | on the | authentication |     | phase, |
| -------------------- | --- | ------------- | ------- | ------- | -------- | ------- | ---------- | ----- | ------ | -------------- | --- | ------ |
| Trust architectures. |     | The following | section | surveys | existing |         |            |       |        |                |     |        |
andnotbeyondintopost-loginauthorizationrequests,token
| academic | approaches | that attempt | to address | aspects | of this |     |     |     |     |     |     |     |
| -------- | ---------- | ------------ | ---------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
grants,andresourcerequests.Thisishandledbycontinuous
problemandidentifiestheremainingchallengesthatmotivate
authenticationsystems.
theproposedmodel.
| IV. RELATEDWORK |     |     |     |     |     | B. CONTINUOUSAUTHENTICATION |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
Strongsecuritysystemshavebeenapriorityareaofresearch
Continuousauthentication(CA)systemsfocusonvalidating
in both industry and academia, and previous studies on auser’sidentitywhileausersessionisinprogress.
implicitauthenticationusingbehavioralmetricssetthepath Acar et al. [26] presented a wearables-assisted CA
towardsAA.
|     |     |     |     |     |     | framework | that verifies | user        | identity | based | on keystroke |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | ----------- | -------- | ----- | ------------ | --- |
|     |     |     |     |     |     | dynamics  | detected      | by sensors. | The      | work  | proposed     | by  |
A. RISK-BASEDANDADAPTIVEAUTHENTICATION Buriroetal.[27]usedkeystrokedynamicsandtouch-timing
Risk-based authentication (RBA) and Adaptive Authenti- differences to continuously authenticate users throughout
cation (AA) for systems have been a growing focus of active sessions. The framework distinguishes itself from
study. RBA focuses on risk analysis using contextual and othersbynotrequiringuserstomemorizeafixedpassword.
behavioralsignals,comparingthemwiththeuser’shistorical Shen et al. presented a behavioral biometrics-based CA
profile, and derives a risk score. The risk score determines systemforsmartphones[28].Liangetal.[29]investigatedthe
whichauthenticatorswillbeemployedtochallengetheuser. useofwearable-devicebehavioralbiometricsforcontinuous
Adaptive authentication focuses on choosing authenticators authentication, in which ML was employed to derive
to activate based on the risk score derived from behavioral behavioralpatternsfrombiometricdata.In[30],Meknietal.
and contextual analysis. They represent an ‘‘at the point of presented a study in which CA was achieved using gait
authentication’’phase. biometrics and was enhanced using machine learning. The
Dasu et al. [16] proposed an Adaptive Authentication authorsemployedadeep-learning-basedclassifiertoenhance
framework to defend against identity threats. However, the authenticationaccuracy.Shahetal.intheirstudyoncontin-
authors adopt a heuristic approach to weight assignment, uousdevice-to-deviceauthenticationproposedalightweight
in which risk signal weights are assigned statically and CAframeworkthatutilizeschannelpropertiestodynamically
are independent of the data distribution and attack history. rotatesessionkeys[31].SimilarstudiesinCAhighlightthe
Furthermore, the variance computation is performed only growing interest in monitoring behavioral aspects for user
on the last 10 login records, limiting the scope of vari- identity verification, with a focus mainly on wearables and
ance computation to strictly heuristic and not statistical. mobile devices [32], [33], [34], [35]. While promising, the
Picard and Pierre [17] presented an RBA system that uses proposed CA systems effectively work on binary decision
deep reinforcement learning (DRL) to select authentication controls,wheretheuserrequestiseithertreatedasbenignor
| 77842 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
askedtostepuptheirauthentication.Hardviolations,suchas Attribute importance, spoofability, and temporal sta-
impossibletravels,andcryptographicbindingviolat,ions,are bility are set by fixed rules or expert heuristics. Sys-
notconsidered.Inaddition,decisionsaremadebyevaluating temslackcold-startstrategiesandonlinerecalibration
datafromlimitedbehavioralattributes,whichcanbespoofed methods[16],[54],[55].
individually, and by assuming that historical data will be 3) ImplicitTrust:
presentasthesystemisonline. Risk evaluation and trust computations are performed
Furthermore, established products in the cybersecurity only until the point of authentication. Post-login
domain, such as RSA Cybersecurity, CA Risk Authen- requestsareimplicitlydeemedvalidandfallwithinthe
tication, Okta, BIO-Key Portal Guard, Duo Risk-Based realmofimplicittrust[17],[18],[19].
Authentication, and IBM Security, employ risk-based AA 4) Lack of an explicit admissibility/safety invariant.
systems. However, the detailed working patterns of these Industrycontrols(e.g.,impossibletravelchecks,attes-
products,includingtheattributestheygatherandthemethods tation failures) are often implemented as scattered
employedtocreatethecontextualprofile,areproprietary. heuristics. There is little formal distinction between
|     |     |     |     |     |     |     | non-compensable |           |       | (hard) failures |     | and         | probabilistic |       |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | ----- | --------------- | --- | ----------- | ------------- | ----- |
|     |     |     |     |     |     |     | (soft)          | evidence, | which | complicates     |     | correctness |               | argu- |
C. ZERO-TRUSTSYSTEMS
mentsandpolicyproofs.
Zero-trust,asadesignphilosophy,isbeingrapidlyevaluated
|     |     |     |     |     |     |     | 5) Poor | integration |     | of retry/attack |     | dynamics |     | into |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --------------- | --- | -------- | --- | ---- |
andadoptedbyresearchersandindustry.
threatmodels.
| Hasan | et al. | in their | study | [36] presented |     | design and |       |          |         |         |          |     |           |     |
| ----- | ------ | -------- | ----- | -------------- | --- | ---------- | ----- | -------- | ------- | ------- | -------- | --- | --------- | --- |
|       |        |          |       |                |     |            | Retry | behavior | (failed | logins, | repeated |     | attempts) | is  |
assurancepatternsforZTcomponents.Withpatternlibraries
|            |           |                 |                 |          |                   |             | frequently |     | handled    | by synthetic | counters |      | or lockout    |     |
| ---------- | --------- | --------------- | --------------- | -------- | ----------------- | ----------- | ---------- | --- | ---------- | ------------ | -------- | ---- | ------------- | --- |
| enriched   | with      | their findings, | the             | authors  | claim             | that system |            |     |            |              |          |      |               |     |
|            |           |                 |                 |          |                   |             | rules;     | few | approaches | model        | retries  | as   | probabilistic |     |
| architects | can model | ZT              | transformations |          | of Cyber-Physical |             |            |     |            |              |          |      |               |     |
|            |           |                 |                 |          |                   |             | amplifiers |     | of attack  | likelihood   | with     | time | decay         | and |
| systems.   | The       | authors         | in [37]         | proposed | a process-driven  |             |            |     |            |              |          |      |               |     |
contextualconsistencychecks.
| framework | for | migrating | to a | ZT architecture, |     | aimed at |     |     |     |     |     |     |     |     |
| --------- | --- | --------- | ---- | ---------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
6) Insufficientadversary-awarethreatsurfaces.
addressingthegapsandchallengesidentifiedinpreviousZT Compositeattacksurfacesthatcombineauthentication,
| migrations. | A similar | study | on  | the cost-effectiveness |     | of ZT |     |     |     |     |     |     |     |     |
| ----------- | --------- | ----- | --- | ---------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
attributeforgery,tokenreplay,andpost-granthijackare
| transformation |     | for organizational |     | security | was published | by  |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------------ | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rarelymodeledtogether;asaresult,policythresholds
| Adahman | et al. | [38]. Similar | studies | on  | ZT transformation |     |     |     |     |     |     |     |     |     |
| ------- | ------ | ------------- | ------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arehardtojustifyquantitatively.
| of industry | sectors | have | been published |     | in [39], | [40], [41], |          |                |         |     |            |          |     |      |
| ----------- | ------- | ---- | -------------- | --- | -------- | ----------- | -------- | -------------- | ------- | --- | ---------- | -------- | --- | ---- |
|             |         |      |                |     |          |             | Based on | the literature | review, | the | identified | research |     | gaps |
and[42].
|     |     |     |     |     |     |     | highlight | the need | to develop | an  | AA system | that | covers | the |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ---------- | --- | --------- | ---- | ------ | --- |
Haleetal.[43]presentedaZT-basedmitigationapproach
for ML components originating from data or model manip- followingfactors.
ulation. In addition, Krishnan and Sreeja [44] proposed a 1) Discardsimplicittrust.
zero-trust-based adaptive authentication system that uses 2) Models trust as a continuous, evolving, and bounded
variable
| composite | attribute | sets. | Ahmed | et al. | in their | work [45] |     |     |     |     |     |     |     |     |
| --------- | --------- | ----- | ----- | ------ | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
presentedaZT-basedaccesscontrolsystemtoguardsensitive 3) Multi-dimensionalcontextualsignalsforriskaggrega-
data stores. The authors utilized an access-control proxy to tionandpolicy-driventhresholds-basedevaluation.
analyze request parameters and arrive at the enforcement 4) Enables parameterization and online recalibration of
decisions.AZT-basedimplementationofsecuritymeasures attribute and authentication weighting and penalty
coefficients.
| for Oracle | ERP | cloud | was studied | by the | authors | in Qazi |     |     |     |     |     |     |     |     |
| ---------- | --- | ----- | ----------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
and Arshad [46]. In contrast, a framework to protect power 5) Resistsprofilepoisoning.
grids from security attacks using a Zero-Trust strategy was 6) Distinguishesbetweenhardviolationsandprobabilistic
softviolations.
| discussed | by Faraj | [47]. | Similar | zero-trust | frameworks | for |     |     |     |     |     |     |     |     |
| --------- | -------- | ----- | ------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
protectingresourceshavebeenfeaturedintheliterature[48], 7) Incorporatesretryattackdynamicsintothreatmodels.
8) Alignedtoindustrystandards.
[49].
TheproposedZeTHAAsystemisanextensionofthework
|     |     |     |     |     |     |     | of Krishnan | and | Sreeja [44] | to mitigate |     | identified | research |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ----------- | --- | ---------- | -------- | --- |
D. RESEARCHGAPANALYSIS
gapswithanimplementedproof-of-concept.
Basedontheinferencederivedfromtheliteraturereview,the
followingresearchgapshavebeenidentified,whichneedto
V. METHODOLOGY
beaddressed:
|     |     |     |     |     |     |     | This section | presents |     | the methodology |     | underlying |     | the |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | --------------- | --- | ---------- | --- | --- |
1) Vendor-locked,opaqueimplementation: proposed Zero-Trust Hybrid Adaptive Authentication
Existing Zero-Trust implementations are proprietary, (ZeTHAA) framework. The methodology proceeds from
resultinginvendorlock-in,anddonotofferaviewof system definition and state modeling to threat analysis,
internalworkingandcalibrations[50],[51],[52],[53]. risk computation, adaptive enforcement, and security
| 2) Staticattributeweightingandpenaltypolicies: |     |     |     |     |     |     | guarantees. |     |     |     |     |     |     |       |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ----- |
| VOLUME14,2026                                  |     |     |     |     |     |     |             |     |     |     |     |     |     | 77843 |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| A. NOTATION |     |     |     |     |     |     | 1) SYSTEMANDTRUSTMODELASSUMPTIONS |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
Table1summarizesthesymbolsandnotationsusedthrough- • Continuous Evaluation. Trust is evaluated at every
outthisstudy. request and is not persistent across sessions. Each
requestistreatedasafreshevaluationunderZeroTrust
| B. SYSTEMMODEL |          |          |              |     |           |     | semantics.                                       |     |     |     |     |     |     |
| -------------- | -------- | -------- | ------------ | --- | --------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|                |          |          |              |     |           | =   | • CompositeTrustFunction.Trustisaunifiedfunction |     |     |     |     |     |     |
| The system     | consists | of a set | of protected |     | resources | R   |                                                  |     |     |     |     |     |     |
{R ,R ,...,R }. Each resource R is associated with a of authentication strength, contextual attributes, and
| 1 2 | n   |     |     | i   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
requiredtrustthresholdT(R),whichmustbeachievedbefore behavioral history. No independent trust components
i
(e.g.,authentication-onlyorbehavior-onlytrust)existin
| access is | granted. A set | of registered |     | users | U interacts | with |     |     |     |     |     |     |     |
| --------- | -------------- | ------------- | --- | ----- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
thesystembyperformingactionsAct = {login,read,write} isolation.
ontheresourcesinR. • Separation of Trust and Risk. Trust and risk are
AccessdecisionsaredeterminedunderaZeroTrustmodel, complementary but distinct quantities. Trust represents
inwhichnouser,device,orsessionisimplicitlytrusted.Each confidence in legitimacy, whereas risk represents the
|     |     |     |     |     |     |     | likelihood | of  | adversarial | success. |     | The decisions | are |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | -------- | --- | ------------- | --- |
accessrequestisevaluatedbasedon:
|         |                 |                |            |            |     | =       | basedonbothquantities.            |     |     |     |     |     |     |
| ------- | --------------- | -------------- | ---------- | ---------- | --- | ------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
| • A set | of contextual   | and            | behavioral | attributes |     | A t     |                                   |     |     |     |     |     |     |
| {a      | (t),a (t),...}; |                |            |            |     |         |                                   |     |     |     |     |     |     |
| 1       | 2               |                |            |            |     |         |                                   |     |     |     |     |     |     |
| A set   | of supported    | authentication |            | methods    |     | M, each |                                   |     |     |     |     |     |     |
| •       |                 |                |            |            |     |         | 2) ATTRIBUTEANDCONTEXTASSUMPTIONS |     |     |     |     |     |     |
associatedwithanintrinsicauthenticationstrength; • AttributeObservability.Contextualattributes(device,
• A dynamically evaluated session context C(t), com- location, time, network, etc.) are observable with
prising attributes, authentication state, and historical boundednoiseandmayexhibitnaturalvariability.
evidence; • SpoofabilityandStability.Eachattributeisassociated
AtrustscoreTrust(C(t))andanestimatedattacksuccess
| •   |     |     |     |     |     |     | with | a spoofability | likelihood |     | and | temporal | stability, |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------------- | ---------- | --- | --- | -------- | ---------- |
probabilityPr[AttackSuccess|C(t)].
|     |     |     |     |     |     |     | which | influences | its | weight | and | penalty | in trust |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ------ | --- | ------- | -------- |
computation.
| Authorization | decisions            |     | are issued   | per | session | and per |     |     |     |     |     |     |     |
| ------------- | -------------------- | --- | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| resource,     | and are continuously |     | re-evaluated |     | as the  | context |     |     |     |     |     |     |     |
evolves.
|     |     |     |     |     |     |     | 3) BEHAVIORALANDLEARNINGASSUMPTIONS |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
TheZeTHAAframeworkdefinestheZero-TrustAdaptive
|     |     |     |     |     |     |     | • Behavioral | Profiles |     | are Probabilistic. |     | User | behavior |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------------ | --- | ---- | -------- |
Authenticationsystemasthetuple:
|     |     |     |     |     |     |     | is modeled | as  | a probabilistic |     | distribution | derived | from |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------------- | --- | ------------ | ------- | ---- |
historicalobservationsratherthandeterministicrules.
=(U,A,M,C,R,T)
Z
• TemporalDrift.Legitimateuserbehaviorevolvesover
|     |     |     |     |     |     |     | time, | and the | system | accommodates |     | this | evolution |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------ | ------------ | --- | ---- | --------- |
where:
throughboundedlearningratesandwindowedupdates.
• U denotesthesetofusers,
| • A = | {a ,a ,...,a | }denotesthesetofcontextualand |     |     |     |     |                                       |     |     |     |     |     |     |
| ----- | ------------ | ----------------------------- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
|       | 1 2          | n                             |     |     |     |     |                                       |     |     |     |     |     |     |
|       |              |                               |     |     |     |     | 4) ADVERSARYANDTHREATMODELASSUMPTIONS |     |     |     |     |     |     |
behavioralattributes,
• M = {m ,m ,...,m } denotes the set of supported • Polynomial-time, probabilistic Adversary Model.
|     | 1 2 |     | k   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
authenticationmethods, The adversary’s success is modeled probabilistically
• C denotessessioncontext, through authentication breakability, attribute forgery,
• R∈{0,1}denotestheobservedsecurityoutcome, andpost-authenticationattackvectors.
∈Rdenotesthetrustscore. Retry Behavior as Attack Signal. Repeated authenti-
| • T |     |     |     |     |     |     | •      |          |             |     |               |            |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ----------- | --- | ------------- | ---------- | --- |
|     |     |     |     |     |     |     | cation | failures | are treated | as  | probabilistic | indicators | of  |
ThetupleZdefinesthesystem’sstaticstructure.Dynamic
|          |             |               |     |          |     |         | adversarial | activity | and | contribute | to  | risk through | retry |
| -------- | ----------- | ------------- | --- | -------- | --- | ------- | ----------- | -------- | --- | ---------- | --- | ------------ | ----- |
| behavior | is captured | by explicitly |     | modeling | the | session |             |          |     |            |     |              |       |
contextC(t),thetrustscoreT(t),andtheobservedoutcomes amplificationfunctions.
|     |     |     |     |     |     |     | • Hard | vs Soft | Violations. |     | Hard violations |     | represent |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ----------- | --- | --------------- | --- | --------- |
R(t)astime-dependentvariables.
|                |              |     |        |          |        |     | non-compensable |     | failures | (e.g., | cryptographic |     | failure, |
| -------------- | ------------ | --- | ------ | -------- | ------ | --- | --------------- | --- | -------- | ------ | ------------- | --- | -------- |
| The high-level | architecture |     | of the | proposed | system | is  |                 |     |          |        |               |     |          |
impossibletravel),whilesoftviolationsrepresentprob-
presentedinFig.1:
abilisticdeviationsthatreducetrustbutdonotterminate
thesession.
C. ASSUMPTIONSANDDESIGNSCOPE
| The proposed | framework    |             | is built | on a | set of | system,  |                           |     |     |     |     |     |     |
| ------------ | ------------ | ----------- | -------- | ---- | ------ | -------- | ------------------------- | --- | --- | --- | --- | --- | --- |
| threat,      | and modeling | assumptions |          | that | enable | the for- |                           |     |     |     |     |     |     |
|              |              |             |          |      |        |          | 5) OPERATIONALASSUMPTIONS |     |     |     |     |     |     |
malization of trust, risk, and attack probability. These • Availability of Logging and Telemetry. Sufficient
assumptions are aligned with Zero Trust principles and logging and telemetry are available to estimate
standardidentityframeworkssuchasNISTSP800-207and attribute distributions, behavioral profiles, and attack
| SP800-63B. |     |     |     |     |     |     | probabilities. |     |     |     |     |               |     |
| ---------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | ------------- | --- |
| 77844      |     |     |     |     |     |     |                |     |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE1. Summaryofnotations.
• Policy-Driven Thresholds. Thresholds for authentica- enclaves,orplatform attestationservices.Thesemech-
tion,authorization,andescalationaredefinedbysystem anisms provide evidence of the device state (e.g., non-
policyandmayvaryaccordingtoresourcesensitivity. rooted,verifiedboot,emulator).
|     |     |     |     |     | • Cryptographic | Capability:           | The | device | can securely  |
| --- | --- | --- | --- | --- | --------------- | --------------------- | --- | ------ | ------------- |
|     |     |     |     |     | generate        | and use cryptographic |     | keys   | for authenti- |
6) DEVICECAPABILITIES
Every request is assumed to originate from a client device cation, including signing challenges and participat-
capableof: ing in hardware-backed authentication protocols (e.g.,
|            |                      |     |            |          | FIDO2 | and, Trusted | Platform | Module | (TPM)-based |
| ---------- | -------------------- | --- | ---------- | -------- | ----- | ------------ | -------- | ------ | ----------- |
| Contextual | Signal Provisioning: |     | The device | can pro- |       |              |          |        |             |
•
attestation).
| vide contextual | attributes | such             | as location | (coarse or  |            |                |                   |     |               |
| --------------- | ---------- | ---------------- | ----------- | ----------- | ---------- | -------------- | ----------------- | --- | ------------- |
|                 |            |                  |             |             | • Secure   | Communication: | All communication |     | between       |
| fine-grained),  | device     | characteristics, | and         | application |            |                |                   |     |               |
|                 |            |                  |             |             | the device | and verifier   | is assumed        |     | to occur over |
metadata.Theseattributesmaybederivedfromsystem
securechannels(e.g.,TLS),ensuringconfidentialityand
| application | programming | interfaces | (APIs), | network |     |     |     |     |     |
| ----------- | ----------- | ---------- | ------- | ------- | --- | --- | --- | --- | --- |
integrityoftransmitteddata.
observations,ortrustedexecutionenvironments.
• Device Integrity and Attestation: The device sup- 7) SCOPEOFAPPLICABILITY
ports mechanisms to assert platform integrity, such Inenvironmentswheresuchdevicecapabilitiesareunavail-
as Trusted Execution Environments (TEE), secure able (e.g., legacy systems without attestation support), the
| VOLUME14,2026 |     |     |     |     |     |     |     |     | 77845 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
FIGURE1. ZeTHAAsystemarchitecture.
framework degrades gracefully by assigning lower weights E. SECURITYOBJECTIVE
tountrustedattributesandrelyingmoreheavilyonbehavioral The primary security objective of the proposed system is to
andcontextualrisksignals. ensure that access to any protected resource is granted and
maintainedonlywhentheprobabilityofadversarialsuccess
D. TRUSTANDRISK inthecurrentcontextremainsbelowanacceptablethreshold.
The trust state T(t) ∈ [0,1] represents an accumulated ForanysessioncontextC(t)atanygiventimet,thesystem
confidence.Thetrustevolvesovertimeastheusercontinues enforces:
tointeractwiththesystem.ThetrustT(t)isthusafunction
ofthecurrentandhistoricalcontext,modeledas: ∀t,∀k ∈K, Pr(R k (t)=1|C(t)≤δ k
T(t)=f(C(t),T(t − ), R (t)∈{0,1}∀k ∈K
k
where T(t−) is the historical trust. Trust T(t) at any time is where R k (t) = 1 indicates a successful attack of class k at
a composite of contextual conformance, behavioral history, timet.R k (t) = 0otherwise.δ representsaconfigurablerisk
devicepostures,andrisksignals. tolerance.
R(t) ∈ 0,1 represents the security outcome at time t. Thesystemadaptsauthenticationstrengthsandauthoriza-
R(t) = Pr[AttackSuccess | C(t)] = 1 represents the risk tiondecisionstoevolvingrisk,therebyenforcingcontinuous
ofadversarialaccess. riskevaluation,consistentwithZero-Trustprinciples.
77846 VOLUME14,2026

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| F. ATTRIBUTES |     |     |     |     |     | I. SESSIONCONTEXTMODEL |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
ThesystemdefinesasetofattributesA.Anattributea i isa The session context captures the environmental and situa-
measurable contextual or behavioral property derived from tionalconditionsunderwhichaccessrequestsareevaluated.
the user, the device, or the application that facilitates the Itisdefinedasatime-dependenttuple:
| construction          | of an overall | risk profile |     | and the | computation |     |         |     |       |          |     |     |
| --------------------- | ------------- | ------------ | --- | ------- | ----------- | --- | ------- | --- | ----- | -------- | --- | --- |
|                       |               |              |     |         |             |     | C(t)=(R |     | ,D ,N | ,T (t),L | ),  |     |
| oftheriskprobability. |               |              |     |         |             |     |         |     | s p s | c        | c   |     |
∈
| Eachuserrequesttransmitsacollectionofattributesa |     |     |     |     | i   | where: |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
Atothesystem.ThesetofattributesAanditsweightW(A)
• R s denotesresourcesensitivity,
canbedefinedas:
• D denotesdeviceposture,
p
|     |      |        | )<T | )}, |     |       |                      |     |     |     |     |     |
| --- | ---- | ------ | --- | --- | --- | ----- | -------------------- | --- | --- | --- | --- | --- |
|     | A={a | ∈A|w(a |     | (R  |     | • N s | denotesnetworkstate, |     |     |     |     |     |
|     | i    |        | i   | r i |     |       |                      |     |     |     |     |     |
• T (t)denotestemporalcontext,
| wheretheweightassignedtoanyattributeislessthanthetrust |     |     |     |     |     | c   |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• L denoteslocationcontext.
c
| requiredtoaccessanyresourceR. |     |     | i   |     |     |             |         |         |      |      |              |        |
| ----------------------------- | --- | --- | --- | --- | --- | ----------- | ------- | ------- | ---- | ---- | ------------ | ------ |
|                               |     |     |     |     |     | The session | context | evolves | over | time | and directly | influ- |
ThesetofattributesAisextensible,andnewattributescan
|     |     |     |     |     |     | ences risk | estimation, | trust | computation, |     | and authorization |     |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----- | ------------ | --- | ----------------- | --- |
beaddedasdiscovered.
|     |     |     |     |     |     | decisions. | Given the | dynamic | nature | of the | session | context, |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | ------- | ------ | ------ | ------- | -------- |
authorizationmustbecontinuouslyevaluatedandnottreated
G. AUTHENTICATIONMODALITIES
asaone-timedecision.
| The system | is configured | with          | a set | of authentication |       |     |     |     |     |     |     |     |
| ---------- | ------------- | ------------- | ----- | ----------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| modalities | M with a      | corresponding | set   | of weights        | W(M). |     |     |     |     |     |     |     |
ThesetofauthenticationmodalitiesMisdefinedasfollows: J. ATTRIBUTETAXONOMYANDCLASSIFICATION
|     |     |     |     |     |     | An attribute | a is | a behavioral |     | or contextual |     | property |
| --- | --- | --- | --- | --- | --- | ------------ | ---- | ------------ | --- | ------------- | --- | -------- |
i
M={m∈M|w(m)<T ( )} associatedwithauser,device,session,orrequest.Attributes
r i
wherew(m)istheweightassignedtoaselectedauthentication provide contextual signals that are relevant to dynamic risk
|          |        |            |          |     |            | and trust | computation | in  | Zero Trust | systems. | This | section |
| -------- | ------ | ---------- | -------- | --- | ---------- | --------- | ----------- | --- | ---------- | -------- | ---- | ------- |
| modality | m ∈ M. | The weight | obtained | by  | successful |           |             |     |            |          |      |         |
authenticationwithanyparticipatingmodalitywillalwaysbe introducesanattributetaxonomyandclassificationbasedon
theirproperties.
| lessthanthetrustrequiredtoaccesstheresource,T |                 |     |     |             | r (R). i |                          |     |     |     |     |     |     |
| --------------------------------------------- | --------------- | --- | --- | ----------- | -------- | ------------------------ | --- | --- | --- | --- | --- | --- |
| The set                                       | M is extensible | and | can | accommodate | newer    |                          |     |     |     |     |     |     |
| authenticationmodalities.                     |                 |     |     |             |          | 1) COMPOSITEATTRIBUTESET |     |     |     |     |     |     |
TheproposedZeTHAAframeworkclassifiesattributesunder
Withthissystemmodelestablished,wedefineuseridentity
usingauthenticationsessions. threecategories,i.e.,-‘‘User,’’‘‘Application,’’and‘‘Device,’’
basedontheparticipatingentities.Theattributesandentities
H. AUTHENTICATIONSESSIONMODEL are discrete yet related. This establishes a ‘‘who uses what,
TheauthenticationAuth isrepresentedas: where’’ relationship among the three discrete entities (user,
i
|     |     |     |     |     |     | device, | browser/application), |     | and | this relationship |     | model |
| --- | --- | --- | --- | --- | --- | ------- | --------------------- | --- | --- | ----------------- | --- | ----- |
Auth(U,m,C)→{True,False}
i i i allows attribute variances to be flagged across categories.
where U represents the user requesting verification of Theapplicationattributesprovideawaytouniquelyidentify
i
identity, m i denotes the authentication method applied, and ‘‘theapplication,runningondevice’’combination.Thus,the
context C = C ∪ C denotes the context attribute-driven context becomes a composite construct of
|     | contextual | behavioral |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
‘‘user,usingtheapplication,ondevice’’.Theattributesused
originatingfrombehavioralandcontextualsignals.
An authentication session is a construct established upon intheCompositeAttributesetarelistedinTable2.
successfulauthentication,definedas: Formobiledevices,thedeviceattributesetisobtainedvia
|     |         |     |        |     |     | Application | Programming |     | Interfaces(APIs) |     | provided | by the |
| --- | ------- | --- | ------ | --- | --- | ----------- | ----------- | --- | ---------------- | --- | -------- | ------ |
|     | =(U,m,t |     | ,t ,σ) |     |     |             |             |     |                  |     |          |        |
S
|     |     | i   | 0 e |     |     | nativemobileoperatingsystem. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
where:
| • U ∈U | istheauthenticateduser, |     |     |     |     | 2) ATTRIBUTECLASSIFICATION |     |     |     |     |     |     |
| ------ | ----------------------- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
i
m∈M istheauthenticationmethodused, Attributes are classified based on their type, stability, and
•
• t 0 istheauthenticationstarttime, applicabilitytocontextbinding.
| • t istheexpirationtime, |     |     |     |     |     | 1) ContextualVsBehavioral |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
e
| σ ∈ | {active,expired,revoked} |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• denotes the authentica- Attributesthatdescribetheexecutionenvironmentare
tionstate. classified as contextual, and those that describe user
An authentication session only establishes the identity interactionovertimeareconsideredbehavioral.Table3
of a user at a given point in time. This does not imply classifiestheattributesascontextualorbehavioral.
continuedauthorization.Whileauthenticationsessionsverify 2) Stability
andestablishuseridentity,authorizationdecisionsdependon Attributescanbeclassifiedasstaticordynamicbased
additional environmental and situational factors, which are on their tendency to change over time, which affects
modeledasasessioncontext. theircontributiontothepersistenceortrustdecayand
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     | 77847 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE2. Compositeattributeset.
TABLE3. Contextualvsbehavioralattributeclassification. frombenignhistoricalobservations.Aprofilerepresentsthe
|     |     |     |     |     | expected distribution | or pattern  | of attribute | values    | and may    |
| --- | --- | --- | --- | --- | --------------------- | ----------- | ------------ | --------- | ---------- |
|     |     |     |     |     | include summary       | statistics, | temporal     | patterns, | or learned |
probabilisticbehavior.
|     |     |     |     |     | For an attribute | a, the profile | Pi  | captures | its expected |
| --- | --- | --- | --- | --- | ---------------- | -------------- | --- | -------- | ------------ |
|     |     |     |     |     |                  | i              |     | u        |              |
behavior,modeledas:
Pi ={E[a],Var[a],...},
|     |     |     |     |     |     | u i | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereE[a]representsthemeanvalueandVar[a]denotesthe
|     |     |     |     |     | i   |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observedvarianceoftheattributea.Profilesareupdatedcon-
i
servativelytoaccommodatebenigndriftwhileavoidingrapid
adaptationresultingfrompotentiallyadversarialbehavior.
theirsuitabilityforcontinuousvalidation.Forinstance, 2) DEVIATIONANDANOMALYSCORING
application and device attributes are predominantly Behavioral patterns can change, subject to human behavior
staticanddonotchangeduringtheirinteractionswith or associated changes. If a user with an established pattern
thesystem.Table4classifiesattributesbasedontheir of logging in at 10 A.M. daily logs in at 9 A.M., the
dispositiontochange. system records this as a deviation from the established
Predominantly static attributes contribute to longer-lived pattern. However, this does not conclusively establish risk
|     |     |     |     |     | or adversarial | behavior. While | the | deviation | indicates an |
| --- | --- | --- | --- | --- | -------------- | --------------- | --- | --------- | ------------ |
trust,whiledynamicattributesarecontinuouslyevaluatedand
utilizedtodetectanomalies. elevatedrisk,itcouldbeanisolatedincidentofauserlogging
inatadifferenttime.Thesystemrecords,flags,andvalidates
deviationsagainsttolerancelimitssetperpolicy.
K. DYNAMICATTRIBUTEANALYSISANDBEHAVIORAL
PROFILING At time t, the observed attribute value a(t) i is compared
|                       |                |            |               |         | againstthecorrespondingprofilePi |                   |                         | tocomputeadeviation |     |
| --------------------- | -------------- | ---------- | ------------- | ------- | -------------------------------- | ----------------- | ----------------------- | ------------------- | --- |
| Contextual            | and behavioral | attributes | change owing  | to user |                                  |                   | u                       |                     |     |
| behavior, operational | changes,       | and        | modifications | to the  | score:                           |                   |                         |                     |     |
|                       |                |            |               |         |                                  | (cid:49)a(t)=dist | (cid:0) a(t),Pi(cid:1), |                     |     |
access device. For example, a login location or access time i i u
may be benign for one user while anomalous for another. where(cid:49)a representsthedeviationoftheobservedvalueof
i
| As such, static | interpretation | of  | attributes is not | sufficient |     |     |     |     |     |
| --------------- | -------------- | --- | ----------------- | ---------- | --- | --- | --- | --- | --- |
theattributefromtheestablishedmeanvalue.
in Zero Trust environments. In ZT systems, trust must be Observed deviations are evaluated relative to acceptable
| continuouslyevaluated,updated,orrecalibrated. |     |     |     |     |                    |           |             | θ   |              |
| --------------------------------------------- | --- | --- | --- | --- | ------------------ | --------- | ----------- | --- | ------------ |
|                                               |     |     |     |     | attribute-specific | variation | thresholds. | Let | i denote the |
This section introduces a dynamic analysis of observed permissible deviation for attribute a. Deviations within
i
attributes, how they contribute to user-specific profiles, and this tolerance are treated as benign, while excess deviation
providessignalsandevidencefortrust,risk,andauthorization
contributestoanomalyscoringandpenaltyassignment.
| decisions. |     |     |     |     |     |                     | (cid:0) (cid:49)a(t)−θ(cid:1) |     |     |
| ---------- | --- | --- | --- | --- | --- | ------------------- | ----------------------------- | --- | --- |
|            |     |     |     |     |     | (cid:49)a + (t)=max | 0,                            |     |     |
|            |     |     |     |     |     | i                   |                               | i i |     |
1) BEHAVIORALANDCONTEXTUALPROFILES The deviation score quantifies how unusual the current
For each user u (or device, where applicable), the system observation is relative to established behavior, but does not
maintainsabehavioralandcontextualprofileP u ,constructed directlyresultinaclassificationdecision.
| 77848 |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE4. Temporaldispositionofattributes.
3) MAPPINGDEVIATIONSTOATTRIBUTEPENALTIES described in subsequent sections. Attribute penalties influ-
|     |     |     |     |     |     |     |     | ence trust | decay, | contribute | to  | attack | success | probability |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---------- | --- | ------ | ------- | ----------- | --- |
Deviationscoresaremappedtoattributepenaltiesthatreflect
increased suspicion or reduced confidence in the observed estimation, and trigger adaptive enforcement actions during
evidence.Forattributea,thepenaltyattimet isafunction continuousmonitoring.
i
ofthedeviationobserved: Thus, dynamic attribute analysis provides the foundation
forthreatmodeling,authorizationdecisions,andZeroTrust
|            |      | π              |         | (cid:0)(cid:49)a (cid:1), |      |          |      |             |     |     |     |     |     |     |     |
| ---------- | ---- | -------------- | ------- | ------------------------- | ---- | -------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|            |      |                | i (t)=g | i (t)                     |      |          |      | guarantees. |     |     |     |     |     |     |     |
| where g(·) | is a | policy-defined |         | function                  | that | controls | sen- |             |     |     |     |     |     |     |     |
sitivity to deviations. Larger deviations result in higher L. BEHAVIORALPROFILECONSTRUCTIONAND
EVOLUTION
| penalties,         | which | in turn       | reduce | trust and | increase  | estimated |     |              |            |     |                  |     |     |           |     |
| ------------------ | ----- | ------------- | ------ | --------- | --------- | --------- | --- | ------------ | ---------- | --- | ---------------- | --- | --- | --------- | --- |
|                    |       |               |        |           |           |           |     | This section | formalizes |     | the construction |     | and | evolution | of  |
| risk in subsequent |       | computations. |        | The       | penalties | represent |     |              |            |     |                  |     |     |           |     |
the system’s assessment of elevated risk based on observed behavioral profiles introduced earlier. Behavioral profiles
|     |     |     |     |     |     |     |     | capture long-term |     | patterns | of user | behavior |     | and serve | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | ------- | -------- | --- | --------- | --- |
behavior;theydonotimplythatanattackhasoccurred.
Thedeviation-derivedpenaltiesintroducedinthissection the reference against which deviations are evaluated for
|               |               |              |          |            |           |              |     | penalty assignment |     | and          | trust computation. |            | The        | framework |       |
| ------------- | ------------- | ------------ | -------- | ---------- | --------- | ------------ | --- | ------------------ | --- | ------------ | ------------------ | ---------- | ---------- | --------- | ----- |
| represent     | instantaneous |              | evidence | of         | anomalous | behavior.    |     |                    |     |              |                    |            |            |           |       |
|               |               |              |          |            |           |              |     | design balances    |     | adaptability | to                 | legitimate | behavioral |           | drift |
| These signals | are           | subsequently |          | aggregated | and       | recalibrated |     |                    |     |              |                    |            |            |           |       |
over time by the penalty assignment model described withresistancetoprofilepoisoning.
| later, which                      | accounts |     | for historical | observations, |     | resource |     |                                                      |     |     |     |     |     |     |     |
| --------------------------------- | -------- | --- | -------------- | ------------- | --- | -------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| sensitivity,andpolicyconstraints. |          |     |                |               |     |          |     | 1) PROFILEINITIALIZATION                             |     |     |     |     |     |     |     |
|                                   |          |     |                |               |     |          |     | Foreachuseruandbehavioralattributea,aninitialprofile |     |     |     |     | i   |     |     |
4) ROLEOFMACHINELEARNING P i(t ) is established at the first trusted observation. The
|         |          |             |     |         |                   |     |     | u 0               |     |         |            |       |     |           |     |
| ------- | -------- | ----------- | --- | ------- | ----------------- | --- | --- | ----------------- | --- | ------- | ---------- | ----- | --- | --------- | --- |
|         |          |             |     |         |                   |     |     | profile maintains |     | summary | statistics | (mean | and | variance) |     |
| Machine | learning | is employed |     | in this | layer exclusively |     | for |                   |     |         |            |       |     |           |     |
evidence interpretation. Machine learning is strictly limited representingnormalbehavior.
to learning and updating behavioral profiles and computing This initialization phase provides a stable baseline from
|     |     |     |     |     |     |     |     | which learning |     | can proceed |     | cautiously | as  | observations |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | ---------- | --- | ------------ | --- |
deviationscores.Itdoesnotdirectlydetermineauthentication
orauthorizationoutcomes,ormodifyauthenticationstrength accumulate. Algorithm 1 details the initialization of the
behavioralprofile.
| or policy | thresholds. | Instead, |     | ML-derived | outputs | serve | as  |     |     |     |     |     |     |     |     |
| --------- | ----------- | -------- | --- | ---------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inputstotrust,risk,andauthorizationdecisions.
| This separation |     | enables | the | system | to adapt | to evolving |     |                                    |     |     |     |     |     |     |     |
| --------------- | --- | ------- | --- | ------ | -------- | ----------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                 |     |         |     |        |          |             |     | 2) HARDANDSOFTCONTEXTUALVIOLATIONS |     |     |     |     |     |     |     |
userbehaviorandenvironmentalconditions. Observed deviations from behavioral profiles are classified
|     |     |     |     |     |     |     |     | aseitherhard | orsoft | violations. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------- | --- | --- | --- | --- | --- |
5) INTEGRATIONWITHDOWNSTREAMCOMPONENTS Hard violations correspond to physically or logically
The penalties derived through dynamic attribute analysis impossiblestates(e.g.,infeasiblegeo-velocity,cryptographic
are incorporated into the composite trust and risk models binding failures, token replay, hardware attestation failure,
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 77849 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm1BehavioralProfileInitialization as:
Require: Attributea,initialobservationa(t )
Require: Defaultvar
i
ianceσ2,learningrate
i
γ
0 Learn(t)=Trust(t)≥τ
learn
0
Ensure: InitializedbehavioralprofileP u i ∧ (cid:53) i (t)≤ϵ ∧ S(m)≥S learn
1: Initializemean:µ i ←a i (t 0 ) ∧ ¬HardViolation(t) (1)
2:
Initializevariance:σ2 ←σ2
3 4 : : S In e i t ti p a r l o iz fi e le pe P n u i al ← tya { c µ c i i u , m σ i u 2 l } at 0 or(cid:53) i ←0 w th h e er c e um τ le u a l r a n ti i v s e a p m en in a i l m tie u s m at tru ti s m t e thr t e , sh ϵ ol i d s , a (cid:53) i s ( m t) a r ll ep p re e s n e a n lt t y s
tolerance, S(m) is the current authentication strength, S
learn
isaminimumauthenticationassurancerequiredforlearning,
and no hard violations have been observed. In addition,
application signature mismatch). Such violations indicate
astatevariableLearningEnabled(t)governswhetherprofile
sessioncompromisewithhighconfidenceandresultinimme-
updates are allowed, transitioning to false upon anomalous
diate access denial or session termination. Hard violations
events, and returning to true only when sufficient trust has
permanently disable learning for the affected session. Let
been built, and soft violations remain within acceptable
HV(t) ∈ {0,1}denotethehardviolationpredicateattimet,
bounds.Thebehavioralprofileupdateproceedsonlyif:
whereHV(t)=1indicatesthatatleastonehardviolationhas
occurredwithinthecurrentauthenticationoraccesssession. UpdateAllowed(t)=Learn(t)∧LearningEnabled(t)
Onceahardviolationoccurs,trust-andrisk-basedreasoning
When Learn(t) = 1, the profile is updated using an
isnolongervalid,andthesessionmustbeterminatedorre-
exponentiallyweightedmovingaverage(EWMA):
authenticated.Thehardviolationcheckisusedbythesystem
asaprimarydefensivevalidationforeachrequest,enablingit Pi(t +1)=(1−γ)Pi(t)+γ a(t), γ ∈(0,1), γ ≪1.
u u i
torejectanyrequestthatviolatestheconditionimmediately.
(2)
Soft violations correspond to statistically unlikely but
plausiblebehavioraldeviations(e.g.,unusuallogintime,new IfLearn(t)=0,thenPi(t +1)=Pi(t).
u u
location). These violations incur penalties that reduce trust This separation ensures immediate reaction to suspicious
butdonotimmediatelyinvalidatethesession.Softviolations behavior while allowing learning to resume only after
temporarilysuspendlearninguntiltrustisre-established. sustainedtrustisre-established.
Table 5 classifies contextual signals into hard and soft
violations with the corresponding action executed by the 4) LEARNINGSUSPENSIONANDRE-ENABLEMENT
system. To prevent adversarial manipulation, learning is suspended
GlobalAdmissibilityPredicate whenever anomalous behavior is observed and the state
Thesystemdefinesaglobaladmissibilitypredicate: variableLearningEnabled(t)transitionstofalse.
However, suspending learning indefinitely would prevent
Admissible(t) ⇐⇒ (HV(t)=0 (cid:1)
adaptationtolegitimatebehavioralshifts.Therefore,learning
is re-enabled only after sustained evidence of legitimacy is
The admissibility predicate represents a system-wide
observedoveratemporalwindowW:
safety invariant. All authentication, authorization, token
issuance, and resource access events are defined only over 1 X
ReLearn(t)= Trust(s)≥τ
an admissible system state. If Admissible(t) = 0, all |W| learn
s∈W
subsequent requests are denied irrespective of accumulated X
∧ Indicator.((cid:53)(s)>0)≤k, (3)
trust,authenticationstrength,orcontextualevidence. i
This separation ensures that trust computation operates s∈W
strictly within safe execution states, while hard violations wheresisatimeindexandk istheupperlimitofthenumber
triggerimmediateanddeterministicsecurityresponses.This of soft violation events permitted within the relearning
distinctionallowsthesystemtoreactdecisivelytoimpossible windowW,andIndicator(.)isanindicatorfunction.
states while remaining tolerant of legitimate behavioral WhenReLearn(t) = true,LearningEnabled transitionsto
variation. true.
3) BEHAVIORALLEARNINGPOLICY 5) BEHAVIORALLEARNINGSTRATEGIES
Behavioralprofilesareupdatedinanevent-drivenandtrust- Once initialized, behavioral profiles evolve through con-
based manner. Profile updates occur only when no hard trolled learning. Different attributes exhibit varying obser-
violations are observed, the current trust level exceeds a vation frequencies and noise characteristics; therefore,
learningthreshold,authenticationstrengthissatisfactory,and a single learning mechanism is insufficient. Accordingly,
no significant penalties are present. This approach ensures each attribute a is assigned a learning strategy χ ∈
i i
that anomalous behavior does not contribute to profile {online,windowed} based on its volatility, observation fre-
learning and adaptation. The learning condition is modeled quency,andsecuritysensitivity.
77850 VOLUME14,2026

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE5. Hardviolationsvssoftcontextualsignals.
The system responds faster to behavioral attributes with Algorithm2Trust-GatedOnlineBehavioralProfileUpdate
naturaldrift,toensurefasteradaptationandpreventstep-up Require: Currentobservationa i (t)
authenticationineveryrequest.Stableandsecurity-sensitive Require: CurrentprofileP u i(t)={µ i (t),σ i 2(t)}
attributespresentaveryslowrateofchange.Suddenchanges Require: TrustTrust(t),penalty(cid:53) i (t)
totheseattributescouldsignifyanattemptatrepeatedattacks Require: Thresholdsτ learn ,ϵ
orprofilepoisoningbyadversarialelements.Assuch,stable Require: Learningrateγ
andsecurity-sensitiveattributesareassignedaslowlearning Ensure: UpdatedprofilePi(t +1)
u
andadaptationrate. 1: ifTrust(t)<τ learn or(cid:53) i (t)>ϵ then
The system defines a learning rate γ i that controls 2: P u i(t +1)←P u i(t)
the speed at which the behavioral profile adapts to new 3: return
observations.Thesevaluesarepolicy-configurableandserve 4: endif
as conservative defaults for evaluation. This hybrid strategy 5: Updatemean(EWMA):
ensures responsiveness to legitimate behavioral drift while 6: µ i (t +1)←(1−γ)µ i (t)+γa i (t)
improvingrobustnessagainstnoiseandprofilepoisoning. 7: Updatevariance:
8:
σ
i
2(t +1)←(1−γ)σ
i
2(t)+γ(a
i
(t)−µ
i
(t))2
γ ↓ forstable/contextualattributes, 9: P u i(t +1)←{µ i (t +1),σ i 2(t +1)}
i
γ ↑ forbehavioralattributeswithnaturaldrift.
i
Furthermore,profileupdatesarecalculatedusingEWMA observations.Theaggregatedbehavioriscomputedas:
toensurethatprofilesrespondimmediatelytochanges,adapt
gradually to legitimate behavioral drift, maintain historical 1 X
a¯ (W)= a(t). (4)
precedents,andgivenewobservationsmoreweightageinthe i i |W| i
profile.
i t∈Wi
Behavioral profile updates are performed at two levels ProfileupdatesarethenappliedusingEWMA:
of granularity. Trust-based online updates apply to low-
frequency,low-noiseattributes,enablingimmediatebutcon- µ(t +1)=(1−γ)µ(t)+γa¯ (W).
i i i i i i
servative adaptation. For high-frequency or noisy attributes,
updates are performed over trusted observation windows, Windowed updates reduce sensitivity to transient noise and
allowinglearningfromaggregatebehaviorwhileimproving improve robustness against in-session profile poisoning.
stabilityandresistancetoprofilepoisoning. Algorithm 3 presents the windowed approach to behavioral
profileupdateforhigh-frequencyattributes.
a: TRUST-GATEDONLINEUPDATE
Forstable,low-noisebehavioralattributes(e.g.,logintime), Algorithm3WindowedBehavioralProfileUpdate
profile updates are performed using trust-gated online Require: ObservationwindowW ={a(t ),...,a(t )}
i 1 i k
learning. When learning is permitted, the profile mean is
Require: WindowtrustsummaryTrust(W)
updatedusingEWMA: Require: Windowpenaltyindicator(cid:53)(W)
i
µ i (t +1)=(1−γ i )µ i (t)+γ i a i (t), Require: ProfileP u i(t)
Require: Learningparametersτ ,γ
where 0 < γ i ≪ 1 is the attribute-specific learning rate. Ensure: UpdatedprofilePi(t + le 1 a ) rn
Online updates enable gradual adaptation from individual
1:
ifTrust(W)<τ
learn
or(cid:53) u
i
(W)>0then
t s r i u n s g t l e e d ev o e b n s t e . rvations while restricting the influence of any 2: P u i(t +1)←P u i(t)
3: return
Algorithm2demonstratesthetrust-gatedonlinebehavioral
4: endif
profileupdate.
5: Computewindowaggregate:
b: WINDOWEDBEHAVIORALUPDATE
6: a¯ i ← |W 1 | P t∈W a i (t)
7: Updatemean:
For high-frequency or noisy attributes (e.g., IP address, 8: µ i (t +1)←(1−γ)µ i (t)+γa¯ i
a ti c o c n es w s i p n a d t o te w r s n . s) L , e l t ea W rn i in = gi { s t 1 p , e . r . f . o , rm t|W e i d | } o d v e e n r o t t r e us a te w d i o n b d s o e w rv o a f - 9: P u i(t +1)←{µ i (t +1),σ i 2(t)}
VOLUME14,2026 77851

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Together, these strategies define how behavioral profiles Trustisupdatedas:
areupdated,asattributesareobservedandevaluated.
|     |     |     |     |     |     |     |     | Trust(t | +1)=Trust(t)+w |     |     | ·(AuthSuccess(t)) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | --- | ----------------- | --- | --- | --- |
m
|                                              |     |     |     |     |     |     |     |     |     |     | −π  | ·(1−AuthSuccess(t)), |     |     | (5) |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
| M. AUTHENTICATIONANDTRUSTINITIALIZATIONEVENT |     |     |     |     |     |     |     |     |     |     | m   |                      |     |     |     |
Anauthenticationsessionbeginswithanauthenticationand
trust initialization event, which establishes the initial trust where w m is the positive contribution of authentication
methodm,andπ
isthepenaltyapplieduponfailure.
| stateofauser–devicepairpriortoanyauthorizationdecision. |       |                |     |         |                 |     |     |     | m   |     |     |     |     |     |     |
| ------------------------------------------------------- | ----- | -------------- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| This event                                              | marks | the transition |     | from an | unauthenticated |     |     |     |     |     |     |     |     |     |     |
requesttoanauthenticatedsessionandprovidesthebaseline 4) STEP-UPAUTHENTICATIONTRIGGER
Repeatedfailuresorlowresultingtrustmaytriggeradditional
trustfromwhichsubsequentauthorization,continuousmon-
itoring,andadaptiveenforcementoperate.Authenticationis authentication factors. Step-up authentication is required
when:
modeledasaniterativeprocessthatmayincluderetriesand
step-upchallengesbeforeastabletruststateisachieved.
|     |     |     |     |     |     |     |     |     |     | Trust(t)<τ |     |     | ,   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
step-up
| 1) AUTHENTICATIONEVENT |     |     |     |     |     |     | whereτ |         |                                          |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
|                        |     |     |     |     |     |     |        | step-up | isapolicy-definedthreshold.Step-upmecha- |     |     |     |     |     |     |
LetE auth (t)denoteanauthenticationeventattimet,defined nismsmayincludeOTP,hardware-backedchallenge,oraddi-
| as: |     |             |            |     |          |     | tionalverificationfactors. |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | ---------- | --- | -------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (t)=(cid:0) |            |     | (cid:1), |     |                            |     |     |     |     |     |     |     |     |
|     |     | E           | U,m,C(t),t |     |          |     |                            |     |     |     |     |     |     |     |     |
auth
5) RETRYCONSISTENCYANDTRUSTDELTAANALYSIS
whereU istheuseridentity,mistheauthenticationmethod Letk denotetheretryindexwithinthecurrentauthentication
|           |     |         |                |     |       |             | session.Thetrustvalueatretryk |     |     |     |     | isdefinedas: |     |     |     |
| --------- | --- | ------- | -------------- | --- | ----- | ----------- | ----------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| employed, | and | C(t) is | the contextual |     | state | observed at |                               |     |     |     |     |              |     |     |     |
authenticationtime.
|     |     |     |     |     |     |     |     |     |     |     | =f (cid:0) | ,m ,H | (cid:1), |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | -------- | --- | --- |
AuthSuccess(t) ∈ {0,1} denotes the outcome of the Trust k C k k k−1
| authentication     |     | attempt. Authentication |            | succeeds  |     | if and only |                                   |     |                                        |     |     |     |                 |     |       |
| ------------------ | --- | ----------------------- | ---------- | --------- | --- | ----------- | --------------------------------- | --- | -------------------------------------- | --- | --- | --- | --------------- | --- | ----- |
|                    |     |                         |            |           |     |             | whereC                            |     | representsthecontextualstateatretryk,m |     |     |     |                 |     | isthe |
| if Admissible(t)=1 |     | and                     | the system | validates |     | method m    |                                   | k   |                                        |     |     |     |                 |     | k     |
|                    |     |                         |            |           |     |             | authenticationmethodemployed,andH |     |                                        |     |     |     | denotestheprior |     |       |
k−1
accordingtoitsdefinedassurancerequirements.
retryhistory.
Thetrustdeltabetweensuccessiveretriesismodeledas:
2) INITIALTRUSTASSIGNMENT
Upon successful authentication, an initial trust value is (cid:49)T =Trust −Trust . (6)
|     |     |     |     |     |     |     |     |     |     | k   | k   |     | k−1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assigned:
|     |     |     |           |       |     |     | In  | a Zero-Trust |     | system, | contextual |     | drift, device |     | change |
| --- | --- | --- | --------- | ----- | --- | --- | --- | ------------ | --- | ------- | ---------- | --- | ------------- | --- | ------ |
|     |     | )=T | (S(m),C(t | ),H(t | )), |     |     |              |     |         |            |     |               |     |        |
Trust(t 0 init 0 0 (e.g.,logginginfromadifferentdevice),ornetworkvariation
|         |     |                     |     |          |     |             | (e.g., | turning | on  | VPN) | may legitimately |     | reduce | trust | even |
| ------- | --- | ------------------- | --- | -------- | --- | ----------- | ------ | ------- | --- | ---- | ---------------- | --- | ------ | ----- | ---- |
| where T | (·) | is a policy-defined |     | function | of  | the authen- |        |         |     |      |                  |     |        |       |      |
init when authentication succeeds. The system can verify trust
| tication | strength | S(m), | the observed | authentication-time |     |     |             |     |         |           |     |       |                     |     |     |
| -------- | -------- | ----- | ------------ | ------------------- | --- | --- | ----------- | --- | ------- | --------- | --- | ----- | ------------------- | --- | --- |
|          |          |       |              |                     |     |     | fluctuation |     | between | attempts, |     | based | on a policy-defined |     |     |
context,andbehavioralhistory.Thisinitialtrustreflectsthe thresholdϵ >0,suchthat:
T
| assurance                                      | obtained | during | the authentication |     | phase, | along |     |     |     |     |               |     |     |     |     |
| ---------------------------------------------- | -------- | ------ | ------------------ | --- | ------ | ----- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
| withcontextualandhistoricalbehavioralevidence. |          |        |                    |     |        |       |     |     |     |     | (cid:49)T <−ϵ |     |     |     |     |
|                                                |          |        |                    |     |        |       |     |     |     |     | k             | T   |     |     |     |
Authenticationandtrustinitializationarecompletewhen:
|     |     |     |     |     |     |     | to  | determine | and | record | the | possibility | of  | brute | force |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | --- | ----------- | --- | ----- | ----- |
Admissible(t)=1 ∧ Trust(t)≥τ . attacks,credentialmisuse,automation,oradversarialreplay.
auth
|               |     |             |         |         |     |              | The                                                     | authentication |     | and | trust initialization |     | event | defines | the |
| ------------- | --- | ----------- | ------- | ------- | --- | ------------ | ------------------------------------------------------- | -------------- | --- | --- | -------------------- | --- | ----- | ------- | --- |
| The resulting |     | trust value | Trust(t | ) forms | the | baseline for |                                                         |                |     |     |                      |     |       |         |     |
|               |     |             |         | 0       |     |              | startingstateforcontinuousverificationundertheZeroTrust |                |     |     |                      |     |       |         |     |
subsequentauthorizationdecisionsandcontinuousmonitor-
|     |     |     |     |     |     |     | model. | Algorithm |     | 4 defines |     | the authentication |     | and | trust |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | --------- | --- | ------------------ | --- | --- | ----- |
ing.
initializationevent.
3) AUTHENTICATIONATTEMPTANDRETRYSEMANTICS
6) HARDVIOLATIONESCALATION
| Authentication |        | attempts may | succeed       | or  | fail due | to benign    |                |     |         |     |       |          |            |     |        |
| -------------- | ------ | ------------ | ------------- | --- | -------- | ------------ | -------------- | --- | ------- | --- | ----- | -------- | ---------- | --- | ------ |
|                |        |              |               |     |          |              | Authentication |     | failure |     | alone | does not | constitute |     | a hard |
| user error     | (e.g., | mistyped     | credentials). |     | Such     | failures are |                |     |         |     |       |          |            |     |        |
violation.However,excessivefailuresordetectionofadver-
| treated as | soft | violations | and result | in a | reduction | in trust |        |          |        |       |       |          |            |           |     |
| ---------- | ---- | ---------- | ---------- | ---- | --------- | -------- | ------ | -------- | ------ | ----- | ----- | -------- | ---------- | --------- | --- |
|            |      |            |            |      |           |          | sarial | patterns | (e.g., | brute | force | attacks, | credential | stuffing, |     |
ratherthanimmediatetermination.Authenticationretriesare automation,orcryptographicprooffailure)resultin:
| re-evaluated | under | ZT principles, |     | in which | each | retry is |     |     |     |     |     |     |     |     |     |
| ------------ | ----- | -------------- | --- | -------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
treatedasanindependentrequestwithafreshcontextualand HV(t)←1.
behavioralassessment.
LetE (k) (t)denotethek-thauthenticationattemptwithina Once HV(t) = 1, the system becomes non-admissible and
auth
| sessionattimet. |     |     |     |     |     |     | thesessionisterminated. |     |     |     |     |     |     |               |     |
| --------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- |
| 77852           |     |     |     |     |     |     |                         |     |     |     |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm4AuthenticationWithRetryandTrustInitializa- Algorithm5AuthorizationDecisionEvaluation
tion Require: Resource R , context C(t), authentication state
s
procedureAuthenticate(U,m,C(t))
| 1:  |     |     |     |     |     |     | S(t) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
attempts←0
| 2:            |     |     |     |     |     | Ensure: |                        | Authorizationdecision |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ------- | ---------------------- | --------------------- | --- | --- | --- | --- | --- |
| 3: Trust(t)←0 |     |     |     |     |     |         | if¬AuthValid(S(t))then |                       |     |     |     |     |     |
1:
| whileattempts<N |                       |     | do  |     |     |     |            |     |     |     |     |     |     |
| --------------- | --------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| 4:              |                       |     | max |     |     | 2:  | returnDeny |     |     |     |     |     |     |
| 5:              | ifAdmissible(t)=0then |     |     |     |     |     | endif      |     |     |     |     |     |     |
3:
|     | returnReject |                        |     |     |     |     | ˆ                           | (m,t)<S | ˆ (C(t),R |         |     |     |     |
| --- | ------------ | ---------------------- | --- | --- | --- | --- | --------------------------- | ------- | --------- | ------- | --- | --- | --- |
| 6:  |              |                        |     |     |     | 4:  | ifS eff                     |         | req       | s )then |     |     |     |
| 7:  | endif        |                        |     |     |     | 5:  | returnStep-UpAuthentication |         |           |         |     |     |     |
| 8:  | result       | ←VerifyAuthMethod(U,m) |     |     |     |     | endif                       |         |           |         |     |     |     |
6:
|     | ifresult            | =successthen |     |     |     |     | ifTrust(C(t))<τ |     |          |         |     |     |     |
| --- | ------------------- | ------------ | --- | --- | --- | --- | --------------- | --- | -------- | ------- | --- | --- | --- |
| 9:  |                     |              |     |     |     | 7:  |                 |     | grant (R | s )then |     |     |     |
| 10: | Trust(t)←Trust(t)+w |              |     | m   |     | 8:  | returnDeny      |     |          |         |     |     |     |
| 11: | else                |              |     |     |     |     |                 |     |          |         |     |     |     |
9: endif
Trust(t)←Trust(t)−π
| 12: |                     |     |     | m   |     | 10: | ifPr[AttackSuccess|C(t)]>δ |     |     |     | (R    | )then |     |
| --- | ------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | ----- | ----- | --- |
|     |                     |     |     |     |     |     |                            |     |     |     | grant | s     |     |
| 13: | attempts←attempts+1 |     |     |     |     |     | returnDeny                 |     |     |     |       |       |     |
11:
endif
| 14: |     |     |     |     |     | 12: | endif |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
ifTrust(t)<τ
| 15: |                  |     | step-up then     |     |     | 13: | returnAuthorize |     |     |     |     |     |     |
| --- | ---------------- | --- | ---------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| 16: | TriggerStepUp(U) |     |                  |     |     |     |                 |     |     |     |     |     |     |
|     | stepResult       |     | ←VerifyStepUp(U) |     |     |     |                 |     |     |     |     |     |     |
17:
| 18: | ifstepResult |     | =failurethen |     |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Authorizationisgrantedifandonlyif:
HV(t)←DetectHardAttack(U)
19:
ifHV(t)=1then
20:
|     |     |                        |     |     |     | AuthValid(S(t))∧ContextAcceptable(C(t))∧(T(t)≥T |     |     |     |     |     |     | (R)) |
| --- | --- | ---------------------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
| 21: |     | returnTerminateSession |     |     |     |                                                 |     |     |     |     |     |     | r i  |
endif
22:
|     |                     |                     |      |      |     | where                                | T             | (R) is the              | trust required | to            | access       | R based | on the |
| --- | ------------------- | ------------------- | ---- | ---- | --- | ------------------------------------ | ------------- | ----------------------- | -------------- | ------------- | ------------ | ------- | ------ |
| 23: | else                |                     |      |      |     |                                      | r             | i                       |                |               |              | i       |        |
|     |                     |                     |      |      |     | specifiedpolicyPolicy                |               |                         | ontheresource. |               |              |         |        |
|     |                     | Trust(t)←Trust(t)+w |      |      |     |                                      |               |                         | Ri             |               |              |         |        |
| 24: |                     |                     |      | step |     |                                      |               |                         |                |               |              |         |        |
|     |                     |                     |      |      |     |                                      | Authorization |                         | decisions      | are evaluated | continuously |         | over   |
| 25: | endif               |                     |      |      |     |                                      |               |                         |                |               |              |         |        |
|     |                     |                     |      |      |     | time.Theauthorizationdecisionattimet |               |                         |                |               | ismodeledas: |         |        |
| 26: | endif               |                     |      |      |     |                                      |               |                         |                |               |              |         |        |
|     | ifTrust(t)≥τ        |                     | then |      |     |                                      |               |                         |                |               |              |         |        |
| 27: |                     |                     | auth |      |     |                                      |               |                         |                |               |              |         |        |
|     |                     |                     |      |      |     |                                      |               | A(t)=f(S(t),C(t),T(t),R |                |               |              | ),      |        |
| 28: | returnAuthenticated |                     |      |      |     |                                      |               |                         |                |               |              | s       |        |
endif
29:
whereS(t)denotestheauthenticationstate,C(t)thesession
30: endwhile
context,andT(t)thetrustgained.
31: HV(t)←1
|     |     |     |     |     |     |     |     | =   |     |     | |   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
returnLockorEscalate Let R(t) Pr[AttackSuccess C(t)] denote the
32:
|     |     |     |     |     |     | composite |     | risk evaluated | under | session | context |     | C(t). Each |
| --- | --- | --- | --- | --- | --- | --------- | --- | -------------- | ----- | ------- | ------- | --- | ---------- |
33: endprocedure
|     |     |     |     |     |     | protected |     | resource | R is associated |     | with two | risk | thresholds |
| --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --------------- | --- | -------- | ---- | ---------- |
i
δ (R)andδ
(R)suchthat:
|                                |             |           |                |                     |       | 1   | i                 | 2 i |           |         |      |         |        |
| ------------------------------ | ----------- | --------- | -------------- | ------------------- | ----- | --- | ----------------- | --- | --------- | ------- | ---- | ------- | ------ |
| 7) SEPARATIONFROMAUTHORIZATION |             |           |                |                     |       |     |                   |     | 0<δ (R)<δ | (R)<1.  |      |         |        |
|                                |             |           |                |                     |       |     |                   |     | 1         | i 2     | i    |         |        |
| The trust                      | initialized | at        | authentication | time serves         | as an |     |                   |     |           |         |      |         |        |
| input to authorization         |             | decisions |                | but does not itself | imply |     |                   |     |           |         |      |         |        |
|                                |             |           |                |                     |       |     | The authorization |     | decision  | at time | t is | defined | as the |
accesstoanyprotectedresource.Authorizationisevaluated
followingthreshold-basedfunction:
| independently                                          | based | on  | resource | sensitivity, required | assur- |     |     |        |          |     |      |     |     |
| ------------------------------------------------------ | ----- | --- | -------- | --------------------- | ------ | --- | --- | ------ | -------- | --- | ---- | --- | --- |
| ancelevels,andcontextualrisk.Thisseparationensuresthat |       |     |          |                       |        |     |     |       |          |     |      |     |     |
|                                                        |       |     |          |                       |        |     |     | allow, | ifR(t)≤δ |     | (R), |     |     |
authentication establishes identity and baseline confidence,  1 i
while authorization enforces ZT prescribed least-privilege A(t)= step_up, ifδ (R)<R(t)≤δ (R), (7)
|     |     |     |     |     |     |     |     |     |     | 1 i |     | 2 i |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a c c e s s u nd e r c o n ti n u o us e va l u at i o n . W e n ow mo d el t h e deny,
|     |     |     |     |     |     |     |     |     | ifR(t)>δ |     | (R ). |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- | --- | --- |
p o s t- l og in a u th o r iz a t io n an d s u b s e q u en t flo w s in th e n e x t 2 i
section.
|     |     |     |     |     |     |     | This ensures | that        | increasing    | risk | enforces  | stricter | actions |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------------- | ---- | --------- | -------- | ------- |
|     |     |     |     |     |     | to  | protect      | the system. | Authorization |      | decisions | thus     | become  |
N. AUTHORIZATIONDECISIONANDEVENT
continuousverificationconsistentwithZero-Trustprinciples.
Anauthorizationeventisdefinedas:
|     |     |                  |     |     |     | Algorithm |     | 5 defines | the | evaluation | of  | the authorization |     |
| --- | --- | ---------------- | --- | --- | --- | --------- | --- | --------- | --- | ---------- | --- | ----------------- | --- |
|     |     | (t)=(U,R,A(t),t) |     |     |     | decision. |     |           |     |            |     |                   |     |
|     |     | E a              | i i |     |     |           |     |           |     |            |     |                   |     |
Theissuanceanduseofauthorizationtokensthatmediate
whereU istheuser,R istherequestedresource,A(t)isthe access to protected resources following an authorization
| i   |     | i   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
authorizationdecisionandt isthedecisiontimestamp. decisionaremodeledinthefollowingsection.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     | 77853 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm6AuthorizationTokenGrant Algorithm7ResourceAccessEnforcement
Require: Authorizationdecision,contextC(t),resourceR Require: Accessrequest(T,R ),currentcontextC(t)
|         |        |          |     |     |     | s   |         |                |     | s   |     |     |
| ------- | ------ | -------- | --- | --- | --- | --- | ------- | -------------- | --- | --- | --- | --- |
| Ensure: | TokenT | ordenial |     |     |     |     | Ensure: | Accessdecision |     |     |     |     |
1: ifAuthorizationdecision̸=Authorizethen 1: if¬ValidateToken(T)then
|          | returnNoTokenIssued |     |     |     |     |     |     | returnDenyAccess |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
| 2:       |                     |     |     |     |     |     |     | 2:               |     |     |     |     |
| 3: endif |                     |     |     |     |     |     |     | 3: endif         |     |     |     |     |
Bindtokentocontext:T ←Bind(u,R ,C(t),t) if¬ContextMatch(T,C(t))then
| 4:  |     |     |     |     | s   |     |     | 4:  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5: Settokenvaliditywindowandscope 5: Applytoken-contextmismatchpenalty
| 6:  | LogauthorizationgranteventE |     |     |     | (t) |     |     | 6: returnDenyAccess |     |     |     |     |
| --- | --------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
g
| returnTokenT |     |     |     |     |     |     |     | endif |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
| 7:           |     |     |     |     |     |     |     | 7:    |     |     |     |     |
ifTrust(C(t))<τ
|     |     |     |     |     |     |     |     | 8:  | access | (R s )then |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | --- |
9: returnRe-authenticationRequired
| O. AUTHORIZATIONGRANTANDTOKEN-BASED |     |     |     |     |     |     | 10: | endif                      |     |     |          |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | -------- | --- |
|                                     |     |     |     |     |     |     | 11: | ifPr[AttackSuccess|C(t)]>δ |     |     | (R )then |     |
| RESOURCEACCESS                      |     |     |     |     |     |     |     |                            |     |     | access s |     |
returnDenyAccess
| In Zero-Trust |              | systems,   | authentication |          | alone does | not grant | 12: |       |     |     |     |     |
| ------------- | ------------ | ---------- | -------------- | -------- | ---------- | --------- | --- | ----- | --- | --- | --- | --- |
| access        | to protected | resources. |                | Instead, | successful | authen-   | 13: | endif |     |     |     |     |
14: returnGrantAccess
| tication | enables | an explicit |     | authorization | grant, | typically |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | ------------- | ------ | --------- | --- | --- | --- | --- | --- | --- |
realizedthroughshort-livedauthorizationtokens(e.g.,OAuth
accesstokens,SecurityAssertionMarkupLanguage(SAML)
Tokenvalidityisdefinedas:
assertions,orJSONWebTokens(JWT)).
TokenValid(T,C(t))
| 1) AUTHORIZATIONTOKENMODEL |     |     |     |     |     |     |     | (cid:16) |                |     |                   | (cid:17) |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ----------------- | -------- |
|                            |     |     |     |     |     |     |     | =1 <τ    | ∧ Bind(T,C(t)) | ∧   | ScopeAllowed(ℓ,r) |          |
Authorization tokens are security artifacts distinct from t e
authentication sessions. An authorization token is modeled (9)
as:
Resourceaccessisgrantedifandonlyif:
|     |     | T   | =(U,s,ℓ,τ |     | ,κ) |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i e
|     |     |     |     |     |     |     |     | AuthValid(S(t)) |     | ∧ TokenValid(T,C(t))∧ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------------- | --- | --- |
where:
|     |      |                 |     |     |     |     |     |     | Pr[AttackSuccess|C(t)]≤δ |     | r(Rs) | (10) |
| --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | ----- | ---- |
| •   | U ∈U | denotestheuser, |     |     |     |     |     |     |                          |     |       |      |
i
• sdenotestheassociatedauthenticationsessionidentifier, This formulation enforces continuous authorization even
• ℓdenotestheauthorizedscopeorprivileges, inthepresenceofvalidtokens.
τ denotesthetokenexpirationtime,
• e
κ
• denotescryptographicorcontextualbinding. P. CONTINUOUSMONITORINGANDRE-EVALUATION
|     |     |     |     |     |     |     | As  | a Zero-Trust | system, | the context, | risk, and trust | states |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------------ | --------------- | ------ |
2) AUTHORIZATIONGRANTEVENT mustbecontinuouslyevaluated,andauthorizationdecisions
Anauthorizationgranteventisdefinedas: should be revalidated throughout the lifetime of a session.
Thesystementersacontinuousmonitoringandre-evaluation
|     |     | E (t)=(S(t),C(t),T,t) |     |     |     |     |                                                       |     |     |     |     |     |
| --- | --- | --------------------- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | g                     |     |     |     |     | phasefollowingtheauthorizationgrantandtokenissue.This |     |     |     |     |     |
phasespansthelifetimeofthesession.
Anauthorizationtokenisissuedifandonlyif:
|     |     |     |     |     |     |     |     | The continuous | monitoring | function | at time t is modeled |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | -------- | -------------------- | --- |
as:
|     | AuthValid(S(t)) |     | ∧   | S(m)≥S | req (C(t))∧ |     |     |     |     |     |     |     |
| --- | --------------- | --- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
Pr[AttackSuccess|C(t)]≤δ M(t):(C(t),T(t − ),R(t − ),T )→(T(t),R(t),E(t)),
|     |     |         |          |      | grant (R s ) |     |       |     |     | t   |     |     |
| --- | --- | ------- | -------- | ---- | ------------ | --- | ----- | --- | --- | --- | --- | --- |
|     | ∧   | (T(t)≥T |          |      |              |     |       |     |     |     |     |     |
|     |     |         | grant (R | s )) |              | (8) | where |     |     |     |     |     |
• C(t):currentcontext
| whereS(m)denotesauthenticationstrength,T |       |            |     |       |               | (R )isthe |     |                                      |     |     |     |     |
| ---------------------------------------- | ----- | ---------- | --- | ----- | ------------- | --------- | --- | ------------------------------------ | --- | --- | --- | --- |
|                                          |       |            |     |       | g ra nt       | s         |     | T(t−),T(t):pastandcurrenttruststates |     |     |     |     |
| minimum                                  | trust | threshold, | and | δ     | (R ) is t h e | ma ximum  |     | •                                    |     |     |     |     |
|                                          |       |            |     | grant | s             |           |     | R(t−),R(t):pastandcurrentriskstates  |     |     |     |     |
•
acceptableattacksuccessprobability.
• T :currentandactivetoken
| This | ensures | that possession |     | of  | valid credentials | alone |     | t   |     |     |     |     |
| ---- | ------- | --------------- | --- | --- | ----------------- | ----- | --- | --- | --- | --- | --- | --- |
is insufficient to obtain authorization artifacts. Algorithm 6 • E(t):enforcementdecision
Algorithm8representsthecontinuousmonitoringandre-
describestheauthorizationtokengrantflow.
evaluationflow.
3) RESOURCEACCESSUSINGAUTHORIZATIONTOKENS
| Aresourceaccessrequestattimet |     |     |     | isdefinedas: |     |     | 1)  | TRUSTUPDATE |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------------ | --- | --- | --- | ----------- | --- | --- | --- | --- |
Trustevolvesasafunctionofpriortrust,currentcontext,and
(t)=(U,R,T,C(t))
|       |     | E r |     | i i |     |     | estimatedrisk. |     |     |     |               |     |
| ----- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | ------------- | --- |
| 77854 |     |     |     |     |     |     |                |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| Algorithm8ContinuousMonitoringandRe-Evaluation |     |     |     |     |     |     | 2) TRUSTDECAY |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Require: Activesession,contextstreamC(t)
Trustisdesignedtodecayevenintheabsenceofuseractions
Ensure: Updatedtrust,enforcementactions orreinforcingevidence.Trustdecayismodeledas:
1: whileSessionActivedo
|     | Observenewattributesandevents |     |     |     |     |     |     |     |          |     | −    | −µ(cid:49)t, |     |      |
| --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | ------------ | --- | ---- |
| 2:  |                               |     |     |     |     |     |     |     | T(t)=T(t |     | ) ∗e |              |     | (13) |
3: UpdatecontextC(t)
|     | Updateattributepenaltiesformismatchorabsence |     |     |     |     |     |       | (cid:49)t | = −t−, |          |              |     |         |          |
| --- | -------------------------------------------- | --- | --- | --- | --- | --- | ----- | --------- | ------ | -------- | ------------ | --- | ------- | -------- |
| 4:  |                                              |     |     |     |     |     | where |           | t      | the time | that elapsed |     | between | the past |
5: Updateauthenticationpenaltiesifapplicable truststateandcurrenttruststate,ensuringthatstalesessions
6: RecomputeTrust(C(t)),Pr[AttackSuccess|C(t)]
donotretainimplicittrust.
ifAnyauthorizationthresholdviolatedthen
| 7:  |                                               |     |     |     |     |     | The           | risk | R(t) is, however, |     | always | fully | recomputed | and |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | ------------- | ---- | ----------------- | --- | ------ | ----- | ---------- | --- |
| 8:  | Enforcestep-upauthentication,tokenrevocation, |     |     |     |     |     | doesnotdecay. |      |                   |     |        |       |            |     |
ortermination
9: endif
3) BINDINGVALIDATION
10: endwhile
|     |     |     |     |     |     |     | For     | attributes | bound | to       | the authorization |            | token, | con-   |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ----- | -------- | ----------------- | ---------- | ------ | ------ |
|     |     |     |     |     |     |     | tinuous | monitoring |       | verifies | that bound        | attributes |        | remain |
withindefinedtolerancethresholds.Violationscontributeto
Thecurrentcontextcanbemodeledas: increasedriskandacceleratedtrustdecay,mitigatingreplay
| C(t)=λ+X |     |     |     |     |     |     | andsessionhijackingattacks. |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
w ·Indicator(a).[match(a(t))]
|     |       | i   | i   | i   |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | ai ∈A |     |     |     |     |     |     |     |     |     |     |     |     |     |
4) RE-EVALUATIONANDENFORCEMENT
X(cid:16)
− λmm(R )· π ·Indicator(a).[mismatch(a(t))] Authorizationvalidityisre-evaluatedateachmonitoringstep
|     |     | i s i |     | i   |     | i   |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accordingto:
ai ∈A
|     |           |                        |     | ).(cid:2) |     | (t))(cid:3)(cid:17) |     |     |          |        |     |       |        |      |
| --- | --------- | ---------------------- | --- | --------- | --- | ------------------- | --- | --- | -------- | ------ | --- | ----- | ------ | ---- |
|     | +λm iss(R | )· π miss ·Indicator(a |     | missing(a |     |                     |     |     |          |        |     |       |        |      |
|     | i         | s i                    |     | i         |     | i                   |     |     |  Allow, | T(t)≥τ |     | ∧     | R(t)≤δ | ,    |
|     |           |                        |     |           |     |                     |     |     |       |        |     | allow |        | risk |
(11)
|        |     |     |     |     |     |     | Reeval(t)= |     | Step-Up,   | τ      | ≤T(t)<τ |        | ,      |      |
| ------ | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ------ | ------- | ------ | ------ | ---- |
|        |     |     |     |     |     |     |            |     |            |        | deny    |        | allow  |      |
| where: |     |     |     |     |     |     |            |     | Revoke, |        |         |        |        |      |
|        |     |     |     |     |     |     |            |     |            | T(t)<τ |         |        | R(t)>δ |      |
|        |     |     |     |     |     |     |            |     |            |        |         | deny ∨ |        | risk |
λ+ ∈ (0,1)denotestherateatwhichtrustincreasesin
| •   |                                          |              |        |            |     |         |      |             |     |         |                    |     |     | (14)   |
| --- | ---------------------------------------- | ------------ | ------ | ---------- | --- | ------- | ---- | ----------- | --- | ------- | ------------------ | --- | --- | ------ |
|     | responsetoamatchingcontextualattributea. |              |        |            | i   |         |      |             |     |         |                    |     |     |        |
| •   | w denotes                                | the positive | weight | associated |     | with an |      |             |     |         |                    |     |     |        |
|     | i                                        |              |        |            |     |         | This | formulation |     | ensures | that authorization |     | and | access |
attributea.
|     |           | i              |            |         |             |           | privilegesarecontinuouslyevaluatedandadaptivelyenforced |     |     |     |     |     |     |     |
| --- | --------- | -------------- | ---------- | ------- | ----------- | --------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | λm        | (0,1]          |            |         |             |           |                                                         |     |     |     |     |     |     |     |
| •   | m ∈       | denotes        | a mismatch |         | coefficient | for       |                                                         |     |     |     |     |     |     |     |
|     | i         |                |            |         |             |           | inresponsetotheevolvingcontextandthreatconditions.      |     |     |     |     |     |     |     |
|     | attribute | a. It controls | how        | rapidly | trust       | decreases |                                                         |     |     |     |     |     |     |     |
|     |           | i              |            |         |             |           | Havingdefinedtheauthenticationandauthorizationmech-     |     |     |     |     |     |     |     |
when the observed value of a i deviates from expected anisms,theadversarialthreatstothesystemaremodeledin
behavior.
thenextsection.
|     | λmiss ∈ | (0,1] denotes | the missing-attribute |     | coefficient |     |     |     |     |     |     |     |     |     |
| --- | ------- | ------------- | --------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• i
forattributea.Itgovernstherateoftrustreductionwhen
|     |              | i              |     |     |     |     | Q.  | THREATMODEL |     |     |     |     |     |     |
| --- | ------------ | -------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|     | evidencefora | isunavailable. |     |     |     |     |     |             |     |     |     |     |     |     |
i
|     | π > |     |     |     |     |     | 1) ADVERSARYDEFINITION |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
• i 0denotesthepenaltyassociatedwithamismatch
Apolynomial-timeadversaryismodeledas:
ofattributea.
i
πmiss >0denotesthepenaltyassociatedwithamissing
| •   | i   |     |     |     |     |     |     |     |     | A=(K,C,G) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
π
|     | at tribute | a. i This value | may differ | from | i   | to reflect |     |     |     |     |     |     |     |     |
| --- | ---------- | --------------- | ---------- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
scenarioswheretheabsenceofevidenceismoreorless
whereKdenotesattackerknowledge,Cattackercapabilities,
suspiciousthananexplicitmismatch.
andG theobjectiveofunauthorizedaccess.
•
(cid:26) : if x ispresent The knowledge and capability of the adversary can fall
|     |     | Indicator(x)= | 1   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
underdifferentattackclasses,suchas,butnotlimitedto:
0 : if x isabsent
|     |     |     |     |     |     |     |     | K={k | ,k  | ,k  | ,k  | ,k  | ,...}, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------ | --- |
Using(11),thecurrenttrustcanbemodeledas: auth grant replay hijack priv
|       |     | (1−λ+ | − λ+·C(t)−γ |     |      |      |        |     |     |     |     |     |     |     |
| ----- | --- | ----- | ----------- | --- | ---- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
| T(t)= |     | )T(t  | ) +         |     | R(t) | (12) | where: |     |     |     |     |     |     |     |
k :Authenticationcompromise
auth
Here,R(t) = Pr[AttackSuccess | C(t)]denotestheriskat k :Illicitauthorizationgrant
grant
|     |     |     |     | γ   | >   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
time t based on the current context and 0 represents k replay :Authorizationtokenreplay
the coefficient of risk, indicating how fast it suppresses k :Sessionhijack
hijack
| trust.        |     |     |     |     |     |     | k priv | :Privilegeescalation |     |     |     |     |     |       |
| ------------- | --- | --- | --- | --- | --- | --- | ------ | -------------------- | --- | --- | --- | --- | --- | ----- |
| VOLUME14,2026 |     |     |     |     |     |     |        |                      |     |     |     |     |     | 77855 |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| 2) ATTRIBUTE-LEVELTHREATS |     |     |     |     |     | 5) PROFILEPOISONING |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
∈Aischaracterizedby:
Eachcontextualattributea i Sincetheproposedframeworkincorporatesadaptivebehav-
|     |     |     |     |     |     | ioral | profiling, | an adversary | may | attempt to | manipulate |
| --- | --- | --- | --- | --- | --- | ----- | ---------- | ------------ | --- | ---------- | ---------- |
a =(E,S,D,ρ)
i i i i i learnedbaselinesbyinjectingmaliciousoratypicalbehavior
where E denotes entropy, S spoofability, D temporal over time, aiming to redefine normal context and reduce
|     | i   |     |     | i   | i   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stability,andρ = Pr(R = 1 | a),representstheprobability anomalysensitivity.
|     |     | i   |     | i   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofattackgivena.
i
| Attribute-levelriskisdefinedas: |     |     |     |     |     | 6) COMPOSITETHREATSURFACE |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
Thecompositethreatsurfaceisdefinedastheprobabilityof
|     |     | Risk(a)=λ | (1−E)+λ | S +λ | ρ   |     |     |     |     |     |     |
| --- | --- | --------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
i 1 i 2 i 3 i unauthorized access under session context C(t), accounting
|                                                 |     |     |     |     |       | for attacks | during | both | authentication | and authorization |     |
| ----------------------------------------------- | --- | --- | --- | --- | ----- | ----------- | ------ | ---- | -------------- | ----------------- | --- |
| Theprobabilityofanadversaryspoofinganattributea |     |     |     |     | i can |             |        |      |                |                   |     |
| bedefinedas:                                    |     |     |     |     |       | phases.     |        |      |                |                   |     |
Pr[Forge(a)|C]∈[0,1]
i
a: AUTHENTICATION-PHASEATTACK
The effective attribute compromise probability can be Theprobabilityofasuccessfulauthentication-phaseattackis
definedas:
definedas:
n
|C(t)]
|     | Pr[Forge(A)|C]= |     |     | Y Pr[Forge(a)|C] |     |     | Pr[Attack | auth |     |     |     |
| --- | --------------- | --- | --- | ---------------- | --- | --- | --------- | ---- | --- | --- | --- |
i
=1−(1−Pr(Break(m)|C(t))·
i=1
Y
|                                |     |     |     |     |     |     |          | (1−Pr(Forge(a)|C(t))), |     |     | (15) |
| ------------------------------ | --- | --- | --- | --- | --- | --- | -------- | ---------------------- | --- | --- | ---- |
| 3) AUTHENTICATIONMETHODTHREATS |     |     |     |     |     |     |          |                        | i   |     |      |
| Eachauthenticationmethodm∈M    |     |     |     |     |     |     | ai ∈C(t) |                        |     |     |      |
isrepresentedas:
|     |     |     |     |     |     | where | Pr[Break(m) | | C(t) | denotes | the probability | of  |
| --- | --- | --- | --- | --- | --- | ----- | ----------- | ------ | ------- | --------------- | --- |
m=(S(m),Rel(m),PR(m))
|     |     |     |     |     |     | compromising | the | active | authentication | method | m and |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | -------------- | ------ | ----- |
|
where S(m) denotes strength, Rel(m) reliability, and PR(m) Pr[Forge(a i ) C(t)] captures the forgeability of contextual
| phishingresistance. |     |     |     |     |     | attributesusedduringauthentication. |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
The probability of compromise of an authentication Ifmultipleauthenticationmethodsareusedduringthelife
| methodmisapproximatedas: |     |     |     |     |     | ofasession,then(15)canbemodifiedas: |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
−S(m)(1−PR(m))
|     |     | Pr[Break(m)]=e |     |     |     |     | Pr[Attack | |C(t)] |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --------- | ------ | --- | --- | --- |
auth
Y
|     |           |             |     |                 |             |     | =1− | (1−Pr(Break(m)|C(t))· |     |     |     |
| --- | --------- | ----------- | --- | --------------- | ----------- | --- | --- | --------------------- | --- | --- | --- |
| The | effective | probability |     | of an adversary | breaking an |     |     |                       |     |     |     |
authentication method, given a surrounding context C, can m∈M(t)
| bemodeledas: |     |     |     |     |     |     | Y   |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(1−Pr(Forge(a)|C(t)))
i
| Pr[Break(m)|C]=Pr[Break(m)]·(1+η·Risk(C)), |     |     |     |     |     |     | ai ∈C(t) |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
whereηdefinesthesensitivityofthemethodmtocontextual
b: AUTHORIZATION-PHASEATTACK
riskRisk(C). In a Zero-Trust system, contextual attributes are validated
|     |     |     |     |     |     | after authentication |     | through | authorization | and | continuous |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | ------- | ------------- | --- | ---------- |
4) SESSIONHIJACKINGANDTOKENREPLAY access checks. Let A ⊆ A denote the subset of attributes
b
boundtotheauthorizationtokenorsession.
Asessionhijackingortokenreplayeventismodeledas:
Theauthorization-phaseattackprobabilityisdefinedas:
|                                                    |     | E (t)=(U |     | ′,R,T′,C(t)) |     |     |           |        |     |     |     |
| -------------------------------------------------- | --- | -------- | --- | ------------ | --- | --- | --------- | ------ | --- | --- | --- |
|                                                    |     | r        | i   | i            |     |     |           |        |     |     |     |
|                                                    |     |          |     |              |     |     | Pr[Attack | |C(t)] |     |     |     |
| whereU′maydifferfromtheoriginalauthenticateduserU, |     |          |     |              |     |     |           | authz  |     |     |     |
|                                                    | i   |          |     |              | i   |     |           |        |     |     |     |
capturingsessionhijackingortokentheftscenarios. =Pr[IllicitGrant]
Y
Tokenreplayattacksaremodeledas: +Pr[Replay]· Pr[Forge(a)|C(t)]
i
|     | ∃T′ | ̸=T | TokenValid(T′,C(t))=1 |     |     |     |     |     | ai ∈Ab |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | ------ | --- | --- |
s.t.
|                                                |     |     |     |     |     |     |              |     | Y Pr[Forge(a)|C(t)]. |     |      |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------------------- | --- | ---- |
|                                                |     |     |     |     |     |     | +Pr[Hijack]· |     |                      |     | (16) |
| Theprobabilityofreplaysuccessisapproximatedas: |     |     |     |     |     |     |              |     |                      | i   |      |
ai ∈Ab
Pr[ReplaySuccess]=Pr[Steal(T)]·Pr[BindFail(T,C(t))]
c: UNIFIEDATTACKSUCCESSPROBABILITY
Sessionhijackingisdefinedas: Combining(15)and(16),theoverallprobabilityofunautho-
rizedaccessisdefinedas:
|     |     | U   | ′ ̸=U | ∧ T′ =T |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | i i   |         |     |     |     |     |     |     |     |
Pr[AttackSuccess|C(t)]
| Both | attacks | are | mitigated | through contextual | binding, |            |             |        |                            |     |                |
| ---- | ------- | --- | --------- | ------------------ | -------- | ---------- | ----------- | ------ | -------------------------- | --- | -------------- |
|      |         |     |           |                    |          | =1−(cid:0) | 1−Pr[Attack | |C(t)] | (cid:1)(cid:0) 1−Pr[Attack |     | |C(t)] (cid:1) |
continuousauthorization,andadaptivetrustdegradation. auth authz
| 77856 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
R. ATTRIBUTEWEIGHTANDPENALTYASSIGNMENT aphase-specificversionw i (p).Phase-specificweightsallow
MODEL factoringinresourcesensitivityateachphaseofaction.
This section formalizes the computation, initialization, and
β θ
e p i
online adaptation of attribute weights and penalties used in w(phase)= ,
trustevaluation.Weightsarederivedfromthreat-relatedprop-
i Pn
j=1 e
β
p
θ
j
erties and are computed periodically, ensuring continuous wherephase∈{login,grant,access,continuous access}.
validation.
2) ATTRIBUTEPENALTYFORMULATION
1) ATTRIBUTEUTILITYANDWEIGHTFORMULATION
While attribute weights determine how trust is accumulates
a: ATTRIBUTEUTILITY
throughpositiveevidence,attributepenaltiesmodeltheloss
Let A = {a ,a ,...,a } denote the set of attributes. Each
1 2 n of trust when expected evidence is absent or contradicts
attributea ischaracterizedbythefollowingproperties:
i it. In a Zero Trust system, both missing and mismatched
• E i ∈[0,1]:entropy(uniqueness), attributesconstitutenegativeevidence,withdifferentsecurity
• S i ∈[0,1]:spoofability, implications.
• D i ∈[0,1]:temporalstability,
• ρ i ∈ [0,1]:riskcorrelation,whereρ i = Pr(R = 1 | a i ) a: PENALTYTYPESFORMISSINGANDMISMATCHED
denotestheprobabilityofanattack.
ATTRIBUTES
Here, ρ i follows a Beta distribution, ρ i ∼ Beta(α i ,β i ), Foreachattributea i ,twopenaltyparametersaremaintained:
whereα i andβ i denotethecountofattackandbenignobser- • π i miss: penalty applied when the attribute a i is missing
vations, respectively. The Beta distribution model allows
fromtheobservedcontext.
incremental learning and refining the attack correlation • π i mm:penaltyappliedwhentheattributea i ispresentbut
as data builds. Spoofability and stability properties of an
mismatchesitsexpectedorboundvalue.
attribute are treated as structural properties that remain
constant over time. They are re-evaluated as attack vectors
3) INTEGRATIONOFATTRIBUTEPENALTIESINTOTRUST
evolve.
COMPUTATION
Each attribute is associated with a normalized attribute
The overall trust score incorporates both weights and
utilityscoreasafunctionofitsproperties:
penalties:
θ i =U(a i )=α E E i +α D D i +α ρ(1−ρ i )−α S S i (17) Trust(C(t))= X w (t) Indicator.[match(a)]
i i
whereα E ,α D ,α ρ ,α S ≥0and: i
− X πmiss,(t) Indicator.[missing(a)]
α E +α D +α ρ +α S =1 i i i
− X πmm,(t) Indicator.[mismatch(a)],
b: COMPUTATIONOFATTRIBUTEWEIGHTS i i
Attributeweightsareobtainedusingsoftmaxnormalization: i
(19)
βθ
w = e i (18) enabling the accumulation and degradation of trust in
i Pn
j=1 e
βθ
j accordancewithZeroTrustprinciples.
where β > 0 determines how a difference in the attribute’s
4) ATTRIBUTEWEIGHTINITIALIZATIONSTRATEGIES
utilityaffectstheweightderivationoftheattribute.
In the proposed system, attribute weights are derived from
Byconstruction:
attribute properties such as entropy, spoofability, reliability,
n and attack correlation. Attribute weight derivation operates
X
w =1
i under three regimes, depending on the availability of
i=1 empiricaldata.
Thesoftmaxnormalizationisutilizedtoensurethatstrong
attributes(highentropy,lowspoofability)contributemoreto a: INITIALIZATIONUSINGHISTORICALOBSERVATIONS
trustgainthanweakattributes.Thisensuresthatevenifthe Whensufficienthistoricaldataisavailable,attributeweights
adversarymanagestospoofweakattributes,thecontribution are initialized using evidence derived from prior authen-
totrustwillbeminimal. tication and access logs. This process combines entropy,
Depending on the sensitivity of the resources, attribute Bayesian estimation of attack correlation, and structural
weights can be modified based on the phase in which they attribute properties to derive an initial utility score for each
are participating (authentication, authorization, token grant, attribute.
resource access). The parameter β can be modified to be Leta denoteanattributeandR∈{0,1}denotethesecurity
i
a phase-specific version β such that the weight becomes outcome,whereR = 1correspondstoanadversarialevent.
p
VOLUME14,2026 77857

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
HistoricallogsareanalyzedtocomputetheentropyofRand Algorithm9AttributeWeightInitializationWithHistorical
theconditionalentropyofRgivenattributea. Data
i
Shannonentropyoftheattackandconditionalentropyare Require: AttributesetA={a 1 ,a 2 ,...,a n }
computedas: Require: HistoricallogdatasetL
Require: Structuralattributeproperties{S,D}
X i i
H(R)=− P(R)log 2 P(R) (20) Require: InitialBetapriorparameters{(α i ,β i )}
H(R|a)=
X
P(a =v)H(R|a =v), (21)
Require: Coefficientsλ
1
,λ
2
,λ
3
,λ
4
>0
i i i Require: Inversetemperatureβ >0
v∈Vi Ensure: Initialandupdatedattributeweights{w (t)}
i
where V i represents the set of all possible values that the ▷OfflinePhase:BatchInitializationUsingHistorical
attributea cantake.InformationgainIG(a)ofattributea
i i i Data
IG =H(R)−H(R|a), (22) 1: foreachattributea i ∈Ado
ai i
2: Compute:IG(a i )←H(R)−H(R|a i )
quantifies the reduction in uncertainty about the security 3: Countattackandbenignoccurrences(α i ,β i )
outcomeafterobservingtheattribute.
4:
ComputeposteriormeanE[ρ(0) ],utilityθ(0)
i i
Inparallel,theattackcorrelationofattributea i ismodeled 5: endfor
asaBayesianrandomvariable: ▷ComputeInitialWeights
ρ =Pr(R=1|a), 6: foreachattributea i ∈Ado
i i
7: w
(0) ←softmax(β,θ(0)
)
i i
withaBetapriorinitializedfromhistoricalattackandbenign 8: endfor
observations.Theposteriormean, return{w (0)}
i
α
E[ρ]= i , (23)
i α +β
i i
providestheestimateofthelikelihoodthatthepresenceofa i of historical data. Structural properties such as spoofability
isassociatedwithadversarialbehavior. andtemporalstabilityareencodedinbaselineutilities,while
Using these quantities, the initial utility of attribute a i is Bayesianpriorsareinitializedtoenablesubsequentlearning.
definedas:
θ(0) =λ IG +λ D +λ E[ρ]−λ S, (24) Algorithm 10 Offline Expert-Only Attribute Utility Initial-
i 1 ai 2 i 3 i 4 i
ization
where D i denotes the temporal stability of the attribute, S i Require: AttributesetA={a 1 ,a 2 ,...,a n }
denotes its spoofability, and λ k > 0 are policy-defined Require: Expert-definedbaselineutilities{θ(0)}n
i i=1
coefficientsreflectingtherelativeimportanceofeachfactor.
Require:
InitialBetapriorparameters{α(0),β(0)}n
The initial attribute weights are then computed using Require: Inversetemperatureparameterβ
i
>0
i i=1
softmaxnormalization: Ensure: Initialattributeweights{w (0)}n
i i=1
w ( i 0) = P e βθ β i (0 θ ) (0) 1: foreachattribu ▷ te In a i i ti ∈ al A ize do attributeutilitiesandpriors
j
e j
2:
θ
i
←θ
i
(0)
ensuringcontributionsacrossattributes. 3: ρ i ∼Beta(α i (0),β i (0) )
Algorithm9representsattributeweightinitializationusing 4: endfor
historicalevidence. ▷Computeinitialweights
5: foreachattributea i ∈Ado
b: INITIALIZATIONUSINGEXPERTKNOWLEDGE 6: w ( i 0) ←softmax(β,θ i )
Whennoattackhistorylogsexist,andonlyexpertknowledge 7: endfor
is available to set attribute values, the expert defines initial
return{w (
i
0)}n
i=1
utilityscoresforattributesθ0 =θexpert .
i i
Intheabsenceofhistoricalobservationslinkingattributes
to security outcomes, the expert assigns θ0 and embeds an c: INITIALIZATIONUNDERMAXIMALUNCERTAINTY
initial ρ0 as a prior belief. The initial attr i ibute weights are Whenreliableestimatesof{E i ,D i ,S i ,ρ i }areunavailable,the
compute
i
dbasedontheθ(0) as:
systemadoptsauniformfallbackinitialization:
i
w (0) = e βθ i (0) w i = n 1 , ∀a i ∈A
i Pn
e
βθ
j
(0)
j=1 Thisfallbackrepresentsanon-informativepriorandtotal
Algorithm 10 denotes attribute utilities and weights uncertainty over the attributes, ensuring unbiased baseline
initialization using expert knowledge alone, in the absence behavior.Asempiricalobservationsaccumulate,thesystem
77858 VOLUME14,2026

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
transitions from uniform to entropy-driven weights without Everytimethesystemobservesattributea:
i
alteringtheunderlyingtrustorauthorizationlogic. (
(α +1,β), (Attack |a)=1
(α,β)← i i i (27)
i i (α,β +1), (Attack |a)=0
5) ATTRIBUTEPENALTYINITIALIZATIONSTRATEGIES i i i
Similar to attribute weights, penalties are initialized under
The system computes the updated risk correlation and the
threedistinctregimesdependingoninformationavailability. posteriormeanofρ as:
i
α
a: INITIALIZATIONUSINGHISTORICALOBSERVATIONS ρ i (t) =E[ρ i |α i ,β i ]= α + i β
i i
When historical logs are available, penalties are initialized
usingempiricalattackcorrelation.Let: Informationgainmayberecomputedperiodicallyorupdated
incrementally.WithinformationgainIG(a)ofattributea
i i
ρmiss =Pr(R=1|a missing),
i i IG =H(R)−H(R|a),
ρmm =Pr(R=1|a mismatched), ai i
i i
,theoverallattributeutilityattimetrelativetoitsinitialvalue
bemodeledusingBetadistributions.Theinitialpenaltiesare
isdefinedas:
thendefinedas:
π i miss,(0) =ν 1 E[ρ i miss], π i mm,(0) =ν 2 E[ρ i mm], θ i (t) =θ i (0)+η 1 (cid:0)E[ρ i (t) ]−E[ρ i (0) ] (cid:1)+η 2 (cid:0) IG( a t i )−IG( a 0 i ) ( (cid:1) 2 , 8)
withν >ν ,ensuringstrongerpenaltiesformismatches.
2 1 whereη ,η >0controlsthesensitivityofutilityupdatesto
1 2
newlyobservedevidence.
b: INITIALIZATIONUSINGEXPERTKNOWLEDGE (t)
Updated attribute weights w are obtained via softmax
When expert knowledge is available but historical data is i
normalizationandusedinsubsequenttrustcomputationand
absent, penalties are initialized based on structural attribute
adaptiveenforcementdecisions.
propertiessuchasspoofabilityandtemporalstability:
βθt
π
π
i
m
m
i
m
ss
,
,
(
(
0
0
)
) =
=
µ
π
1
m
S
is
i
s,
+
(0)
µ
+
2
(
(cid:49)
1−
,
D
i
), (
(
2
2
5
6
)
)
wt
i
=
Pn
j
e
=1 e
i
βθ
j
t
,
i i i
where β > 0 determines how a difference in the attribute’s
whereS denotesspoofability,D denotestemporalstability,
i i
utilityaffectstheweightderivationoftheattribute.
andµ ,(cid:49) >0arepolicy-definedcoefficientsreflectingthe
k i
Algorithm 11 incrementally refines attribute utilities
severityofnegativeevidence.
and weights using Bayesian updating and entropy-based
information gain. This enables adaptation from cold start
c: INITIALIZATIONUNDERMAXIMALUNCERTAINTY
or arbitrary assignment to data-driven operation, based on
In the absence of both expert guidance and historical data,
accumulatingevidence.
penaltiesareinitializeduniformly:
πmiss,(0) =πmiss, πmm,(0) =πmm, b: ONLINERECALIBRATIONOFPENALTIES
i base i base
Thepenaltyrecalibrationprocessoperatesonpenaltysignals
where πmm > πmiss are conservative, policy-defined
base base obtainedbydynamicattributeanalysis,adjustingtheirimpact
constants.
ontrustandriskbasedonaccumulatedevidenceandsystem
policy.
6) ONLINELEARNINGANDADAPTATIONOFWEIGHTSAND
As new session outcomes are observed, penalties are
PENALTIES
updated incrementally using Bayesian estimation. Separate
Once the baseline weights and penalties are defined, the
Beta posteriors are maintained for missing and mismatched
system continues to learn and recalibrate its values as data
events and updated based on observed attack or benign
accumulates. At this stage, the system transitions into an
outcomes.
entropy-basedlearningregime.
Penaltiesarerecalibratedusingadelta-basedupdate:
a: ONLINERECALIBRATIONOFATTRIBUTEWEIGHT π i miss,(t) =π i miss,(t−1)+γ miss (cid:0)E[ρ i miss,(t) ]−E[ρ i miss,(t−1) ] (cid:1),
Asthesystemoperates,newsessionoutcomesareobserved (29)
andincorporated intothemodel.The Betaposteriorparam- πmm,(t) =πmm,(t−1)+γ (cid:0)E[ρmm,(t) ]−E[ρmm,(t−1)
]
(cid:1),
eters (α,β) are updated incrementally based on observed i i mm i i
i i (30)
attack and benign events, generating an updated posterior
mean E[ρ(t) ]. Initially, attribute weights are dominated by subject to predefined bounds πmin ≤ π(·) ≤ πmax.
i i i i
expertpriorsorarbitraryassignments.Asobservationsaccu- This formulation ensures stable learning while preventing
mulate, Bayesian posterior means and entropy-based infor- unboundedtrustloss.
mationgaingraduallyshiftimportancetowardsattributesthat Algorithm12recordsincrementalrecalibrationofattribute
correlatewithattacks. penaltiesbasedonaccumulatingevidence.
VOLUME14,2026 77859

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm 11 Online Attribute Weight Recalibration via Algorithm12OnlineBayesianAttributePenaltyRecalibra-
| BayesianLearning |     |                  |     |      |          |     | tion     |               |     |     |            |           |     |
| ---------------- | --- | ---------------- | --- | ---- | -------- | --- | -------- | ------------- | --- | --- | ---------- | --------- | --- |
|                  |     | AttributesetA={a |     | ,a   | ,...,a } |     | Require: | AttributesetA |     |     |            |           |     |
| Require:         |     |                  |     | 1    | 2 n      |     |          |               |     |     |            |           |     |
|                  |     |                  |     | (0 ) |          |     |          |               |     |     | { π m is s | , π m m } |     |
R e q u i r e : I n i t i a l i z e d u t i l i t i e s { θ } n R e q u i r e : I n i ti a l i z e d p e n a lt i e s
|     |     |     |     | i   | i= 1 |     |     |     |     |     | i   | i   |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
R e q u i r e : I n i t i a l i z e d B e t a p a r a m e t e r s {α , β }n R e q u i r e : L e a r n i n g c o e f fi c i e n t s α , α > 0
|     |     |     |     |     | i i i=1 |     |     |     |     |     | 1   | 2   |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
α , α > R e q u i r e : P e n a l t y le a rn in g r a te s γ , γ >0
R e q u i r e : L e a r n i n g co e f fi c i e n t s 0 m is s m m
|          |                           |                              |     |     | 1 2   |     |          | Penaltyboundsπ   |     | min,π | max |     |     |
| -------- | ------------------------- | ---------------------------- | --- | --- | ----- | --- | -------- | ---------------- | --- | ----- | --- | --- | --- |
| Require: |                           | Inversetemperatureparameterβ |     |     | >0    |     | Require: |                  |     |       |     |     |     |
|          |                           |                              |     |     |       |     |          |                  |     | i     | i   |     |     |
|          | Updatedattributeweights{w |                              |     |     | (t)}n |     | Ensure:  | Updatedpenalties |     |       |     |     |     |
Ensure:
i i=1
whilenewsessionobservation(C(t),R(t))isavailabledo 1: whilenewsession(C(t),R(t))observeddo
1:
▷Penaltylearningformissingandmismatched
▷Updateattackcorrelationposteriors
|     | foreachattributea |              |     | ∈C(t)do |                 |     | attributes |                   |                       |      |     |     |     |
| --- | ----------------- | ------------ | --- | ------- | --------------- | --- | ---------- | ----------------- | --------------------- | ---- | --- | --- | --- |
| 2:  |                   |              |     | i       |                 |     |            |                   |                       |      |     |     |     |
|     |                   | ifR(t)=1then |     |         |                 |     | 2:         | foreachattributea |                       | ∈Ado |     |     |     |
| 3:  |                   |              |     |         |                 |     |            |                   |                       | i    |     |     |     |
| 4:  |                   | α ←α         | +1  |         | ▷Attackobserved |     | 3:         | ifa               | i ismissinginC(t)then |      |     |     |     |
|     |                   | i            | i   |         |                 |     |            |                   |                       |      |     |     |     |
|     |                   | else         |     |         |                 |     | 4:         |                   | ifR(t)=1then          |      |     |     |     |
5:
|     |     | β ←β  |     |     |                 |     |     |     | π    | miss ←min(π | miss+γ |      | ,π max) |
| --- | --- | ----- | --- | --- | --------------- | --- | --- | --- | ---- | ----------- | ------ | ---- | ------- |
| 6:  |     |       | +1  |     | ▷Benignobserved |     | 5:  |     | i    |             | i      | miss | i       |
|     |     | i     | i   |     |                 |     |     |     |      |             |        |      |         |
|     |     | endif |     |     |                 |     | 6:  |     | else |             |        |      |         |
7:
|     |        |     |     |     |     |     | 7:  |     | π   | miss ←max(π | miss−γ |      | ,π min) |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ---- | ------- |
| 8:  | endfor |     |     |     |     |     |     |     | i   |             | i      | miss | i       |
endif
| 9:  | foreachattributea |     |     | ∈Ado |     |     | 8:  |     |     |     |     |     |     |
| --- | ----------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
|     |                   | Compute:E[ρ       |     | ],IG(a | )   |     | 9:  | elseifa |              | mismatchesbaselineinC(t)then |      |     |         |
| --- | ----------------- | ----------------- | --- | ------ | --- | --- | --- | ------- | ------------ | ---------------------------- | ---- | --- | ------- |
| 10: |                   |                   |     | i      | i   |     |     |         | i            |                              |      |     |         |
|     |                   | Updateutilityθ(t) |     |        |     |     |     |         | ifR(t)=1then |                              |      |     |         |
| 11: |                   |                   |     |        |     |     | 10: |         |              |                              |      |     |         |
|     |                   |                   |     | i      |     |     |     |         | π            | mm ←min(π                    | mm+γ |     | ,π max) |
|     | endfor            |                   |     |        |     |     | 11: |         |              |                              |      | mm  |         |
| 12: |                   |                   |     |        |     |     |     |         | i            |                              | i    |     | i       |
|     |                   |                   |     | ∈Ado   |     |     | 12: |         | else         |                              |      |     |         |
| 13: | foreachattributea |                   |     | i      |     |     |     |         |              |                              |      |     |         |
|     |                   | ( t)              |     | (t)    |     |     |     |         | π            | mm ←max(π                    | mm−γ |     | ,π min) |
| 14: |                   | w ←softmax(β,θ    |     |        | )   |     | 13: |         | i            |                              | i    | mm  | i       |
|     |                   | i                 |     | i      |     |     |     |         |              |                              |      |     |         |
|     | endfor            |                   |     |        |     |     | 14: |         | endif        |                              |      |     |         |
15:
endif
| 16: | endwhile |       |     |     |     |     | 15: |        |     |     |     |     |     |
| --- | -------- | ----- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     | return{w | (t)}n |     |     |     |     | 16: | endfor |     |     |     |     |     |
i i=1
17: endwhile
return{πmiss,πmm}
|     |     |     |     |     |     |     |     | i   | i   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7) BASELINEATTRIBUTEWEIGHTINGASSUMPTION
| Although |     | NIST standards |     | primarily | define | requirements |     |     |     |     |     |     |     |
| -------- | --- | -------------- | --- | --------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
for authentication mechanisms, they explicitly permit and S(m)=f(H ,R ,B ,L ),
|     |     |     |     |     |     |     |     |     |     | m   | m m | m   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
encouragetheuseofcontextualandbehavioralattributesfor
where
risk-basedandcontinuousauthorizationdecisions,provided
such attributes are not treated as standalone authenticators. • H represents credential entropy or cryptographic
m
| Table6showcasesindicativebaselinevaluesofweightsand |     |     |     |     |     |     | strength |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
penaltiesforthecompositeattributesetdefinedinTable2. • R m representsresistancetoattacks
The expert priors defined in this work align with these • B representshowtightlymcanbindtotheuser,device,
m
| guidelines |     | and serve | solely | as initial | conditions | that are |     |     |     |     |     |     |     |
| ---------- | --- | --------- | ------ | ---------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
orsessioncontext
progressivelyrefinedthroughempiricallearning. • L representslifecycleassurance
m
S. AUTHENTICATIONSTRENGTHANDPENALTY b: RELATIONSHIPTOAUTHENTICATIONASSURANCE
| ASSIGNMENTMODEL |     |     |     |     |     |     | LEVELS |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
1) AUTHENTICATIONSTRENGTHFORMULATION Authentication strength provides a quantitative mapping to
|     |     |     |     |     |     |     | authentication |     | assurance | levels. | A mapping |     | function φ(·) |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | ------- | --------- | --- | ------------- |
a: DEFINITIONOFAUTHENTICATIONSTRENGTH
associatesstrengthvalueswithrequiredassurancethresholds:
| Definition1: |     | The | authentication |     | weight w | reflects the |     |     |     |     |     |     |     |
| ------------ | --- | --- | -------------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
m
relativeexposureofanauthenticationmethodtoanadversary AAL(m)=φ(cid:0) ˆ (cid:1),
|                                               |     |     |     |     |     |            |     |     |     |     | S (m) |     | (31) |
| --------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ----- | --- | ---- |
| anditscontributiontotheoverallattacksurface.w |     |     |     |     |     | m provides |     |     |     |     |       |     |      |
φ(·)
thedegreeoflikelihoodthatanadversarywilltargetmethod where is indicative and aligns with the assurance
requirementsdefinedinNISTSP800-63B.
m.
| Authentication |     | weights | do  | not represent | security | strength. |     |     |     |     |     |     |     |
| -------------- | --- | ------- | --- | ------------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Instead,weightsscaletheimpactofasuccessfulbreakrather c: DEFINITIONOFAUTHENTICATIONUTILITY
|                            |     |     |     |     |     |     | Let M | = {m ,m | ,...,m | } denote | the | set of | authentication |
| -------------------------- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------ | -------- | --- | ------ | -------------- |
| thanreducingitslikelihood. |     |     |     |     |     |     |       | 1       | 2      | k        |     |        |                |
Letmdenoteanauthenticationmethod.Theauthentication methods.Eachmethodmischaracterizedby:
strengthofm,denotedasS(m),isdefinedas: • S(m):authenticationstrength,
| 77860 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE6. Indicativeattributeweightsandpenaltiesfromexpertpriors.
• Rel(m)∈[0,1]:reliability, e: INTEGRATIONOFAUTHENTICATIONWEIGHTSINTO
PR(m)∈{0,1}:phishingresistance,
| •   |     |     |     |     | THREATMODELING |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
• Pr[Break(m)]:probabilityofcompromise. The weighted authentication-phase attack probability is
definedas:
Theauthenticationmethodutilityscoreisdefinedas:
|        | =γ logS(m)+γ | Rel(m)+γ  | PR(m)−γ |                |     | Pr[Attack                        | |C]            |     |     |                  |     |      |
| ------ | ------------ | --------- | ------- | -------------- | --- | -------------------------------- | -------------- | --- | --- | ---------------- | --- | ---- |
| U m    | S            | R         | P       | B Pr[Break(m)] |     |                                  | auth           |     |     |                  |     |      |
|        |              |           |         |                |     |                                  |                |     | !   |                  |     |      |
|        |              |           |         | (32)           |     |                                  |                |     | n   |                  |     |      |
|        |              |           |         |                |     | X                                |                |     | Y   | Pr[Forge(a)|C]wi |     |      |
|        |              |           |         |                |     | =                                | w Pr[Break(m)] |     | ·   |                  |     | (33) |
|        |              |           |         |                |     |                                  | m              |     |     |                  | i   |      |
| whereγ | ,γ ,γ        | ,γ ≥0and: |         |                |     |                                  |                |     |     |                  |     |      |
|        | S R          | P B       |         |                |     | m∈M                              |                |     | i=1 |                  |     |      |
|        |              | γ +γ +γ   | +γ =1   |                | 2)  | AUTHENTICATIONPENALTYFORMULATION |                |     |     |                  |     |      |
|        |              | S R       | P B     |                |     |                                  |                |     |     |                  |     |      |
a: DEFINITIONOFAUTHENTICATIONPENALTY
ThevalueofS(m)isdrivenbyitsentropyscore.Theutility Definition2(AuthenticationPenalty): An authentication
functiontakesthelogarithmicvalueofS(m)toensureitdoes penalty (cid:53) (t) represents a reactive measure the sys-
m
|     |     |     |     |     | tem | undertakes | by  | reducing | the | effective | authentication |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | --- | --------- | -------------- | --- |
notdominateovertheotherproperties.
|     |     |     |     |     | assurance |             | in response |          | to observed |      | failures,      | degrada- |
| --- | --- | --- | --- | --- | --------- | ----------- | ----------- | -------- | ----------- | ---- | -------------- | -------- |
|     |     |     |     |     | tion,     | or fallback |             | behavior | associated  | with | authentication |          |
d: COMPUTATIONOFAUTHENTICATIONMETHODSCORES
| Authenticationmethodweightsarecomputedas: |     |     |     |     | methodm. |                   |     |                |            |        |         |             |
| ----------------------------------------- | --- | --- | --- | --- | -------- | ----------------- | --- | -------------- | ---------- | ------ | ------- | ----------- |
|                                           |     |     |     |     | Let      | m denote          | an  | authentication |            | method | invoked | at time     |
|                                           |     |     | λUm |     | t.       | An authentication |     | penalty        | quantifies |        | the     | degradation |
e
w =
m P λU m′ in trust caused by failed, weak, or downgraded authen-
m′∈M e
|     |     |     |     |     | tication | during | an  | authentication |     | or  | re-authentication |     |
| --- | --- | --- | --- | --- | -------- | ------ | --- | -------------- | --- | --- | ----------------- | --- |
whereλ>0controlssensitivity.Byconstruction:
event.
Theauthenticationpenaltyisdefinedasafunction:
|     |     | X   | =1  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w m
|               |     |     |     |     |     | (cid:53) | (t)=f(Auth |     | ,Auth | ,Auth |          |       |
| ------------- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ----- | ----- | -------- | ----- |
|               |     | m∈M |     |     |     |          | m          |     | fail  | deg   | fallback | )     |
| VOLUME14,2026 |     |     |     |     |     |          |            |     |       |       |          | 77861 |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
b: PENALTYTYPESFORAUTHENTICATIONMETHODS a: INITIALIZATIONUSINGSTANDARDSANDHISTORICAL
The system defines the following authentication penalty OBSERVATIONS
types: When standards, guidance, and historical security data are
(cid:53)fail available, authentication strength is initialized based on the
|     | 1) Authentication |     | failure | penalty |     | (t), | when an |     |     |     |     |     |     |     |     |
| --- | ----------------- | --- | ------- | ------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
m
authenticationchallengeusingmfails. intrinsic properties of the authentication method and its
alignmentwithestablishedassurancerequirements.
(
|     |     |     |     | πfail,ifAuthFail(m,t) |     |     |     |     | =   | ,R  | ,B ,L |     |     |     |     |
| --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
(cid:53)fail(t)= m LetS(m) f(H m m m m )denotetheintrinsicstrength
m 0,otherwise, formulation defined in Section V-S1. Initial strength values
arecomputedas:
|     | whereπfail |     | >0  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m
|     |                   |     |             |     |          |         |          |             |     | (cid:16) |      |     |      |      | (cid:17) |
| --- | ----------------- | --- | ----------- | --- | -------- | ------- | -------- | ----------- | --- | -------- | ---- | --- | ---- | ---- | -------- |
|     |                   |     |             |     |          |         |          | S(0)(m)=log |     | 1+ω      | H +ω | R   | +ω B | +ω L | ,        |
|     |                   |     |             |     |          |         |          |             |     |          | 1 m  | 2 m | 3 m  | 4    | m        |
|     | 2) Authentication |     | degradation |     | penalty, | applied | when the |             |     |          |      |     |      |      |          |
(35)
methodmdoesnotmeettherequiredassuranceforthe
currentcontextC(t). where the constituent properties are instantiated using
|     |     |     |     |     |     |     |     | method-specific |     | characteristics |     | derived | from | standards | such |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | --- | ------- | ---- | --------- | ---- |
(
|     |     |     | πdeg∗(cid:49)S,ifS(m)<S |     |     | (C(t) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:53)deg(t)= m req as NIST SP 800-63B and industry best practices. The
m
0,otherwise, logarithmic conversion ensures stronger properties do not
dominatetheresult.
where S(m) is the authentication strength of m, ˆ(0)(m)isthenmappedtoanNIST
ThenormalizedstrengthS
|     | S (C(t))     | is          | the strength | required |     | by the context, | and |                |     |           |       |         |           |         |     |
| --- | ------------ | ----------- | ------------ | -------- | --- | --------------- | --- | -------------- | --- | --------- | ----- | ------- | --------- | ------- | --- |
|     | req          |             |              |          |     |                 |     | authentication |     | assurance | level | using a | monotonic | mapping |     |
|     | (cid:49)S =S | (C(t))−S(m) |              |          |     |                 |     |                |     |           |       |         |           |         |     |
|     |              | req         |              |          |     |                 |     | function:      |     |           |       |         |           |         |     |
3) Authenticationfallbackpenalty,appliedwhenaweaker
methodisusedafterastrongermethodwasrequested AAL(m)=φ(cid:0) ˆ(0)(m) (cid:1),
S
orfailed.
|     |     |     | (   |     |     |     |     | Thismappingisindicative. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
πfb,iffallbacktomoccurs
|     | (cid:53)fallback(t)= |     |     | m            |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | m                    |     |     | 0,otherwise, |     |     |     |     |     |     |     |     |     |     |     |
b: INITIALIZATIONUSINGEXPERTKNOWLEDGE
whereπfb >0 In the absence of authoritative standards mappings or
m
|     |            |     |        |     |           |     |            | sufficient  | historical | data,        | authentication |     | strength      | may | be    |
| --- | ---------- | --- | ------ | --- | --------- | --- | ---------- | ----------- | ---------- | ------------ | -------------- | --- | ------------- | --- | ----- |
|     | Typically, | πfb | > πdeg | ≥   | πfail and | the | cumulative |             |            |              |                |     |               |     |       |
|     |            | m   |        | m   | m         |     |            |             |            |              |                |     |               |     |       |
|     |            |     |        |     |           |     |            | initialized |            | using expert | knowledge.     |     | This approach |     | helps |
authenticationpenaltyismodeledas:
|     |     |     |     |     |     |     |     | in deriving |     | authentication | strengths | in  | case | of customized, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --------- | --- | ---- | -------------- | --- |
(cid:53) (t)=(cid:53)fail(t)+(cid:53)deg(t)+(cid:53)fallback(t) proprietary, enterprise-specific, or emerging authentication
|     |     | m   |     |     |     |     | (34) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | m   | m   |     | m   |      |     |     |     |     |     |     |     |     |
mechanismsforwhichstandardizedassurancelevelsarenot
|     | The ordering | πfb | > πdeg | ≥ πfail | reflects | the | increasing |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------ | ------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
yetestablished.Domainexpertsassignaninitialutilityscore
| severityofauthenticationcontroldegradation,consistentwith |     |     |     |     |     |     |     | θexpert |      |              |          |               |     |           |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------------ | -------- | ------------- | --- | --------- | --- |
|                                                           |     |     |     |     |     |     |     | m       | that | reflects the | expected | cryptographic |     | hardness, |     |
riskmanagementguidanceinNISTSP800-30andNISTSP
attackresistance,bindingproperties,andlifecycleguarantees
800-37, and in the authentication literature [56], [57], [58], ofthemethod:
[59].
|     |     |     |     |     |     |     |     |     |     | S(0)(m)=U |     | expert. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --- | --- | --- |
m
c: INTEGRATIONOFAUTHENTICATIONPENALTIESINTO
TRUSTCOMPUTATION
c: INITIALIZATIONUNDERMAXIMALUNCERTAINTY
Authentication penalties reduce the overall trust score of a When neither standards guidance nor expert knowledge is
contextC(t),modeledas:
available,authenticationstrengthisinitializedconservatively
|     |                       |     |     |     | X   |              |     | under                             | maximal | uncertainty. | All | authentication |     | methods | are |
| --- | --------------------- | --- | --- | --- | --- | ------------ | --- | --------------------------------- | ------- | ------------ | --- | -------------- | --- | ------- | --- |
|     | Trust(t)=Trust(C(t))− |     |     |     |     | (cid:53) (t) |     |                                   |         |              |     |                |     |         |     |
|     |                       |     |     |     |     | m            |     | assignedauniformbaselinestrength: |         |              |     |                |     |         |     |
m∈M(t)
|     |     |     |     |     |     |     |     |     |     |     | S(0)(m)=S | ,   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
base
3) AUTHENTICATIONSTRENGTHINITIALIZATION
STRATEGIES
|     |     |     |     |     |     |     |     | whereS |     | isapolicy-definedconstantrepresentingminimal |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
base
Authentication strength initialization defines the baseline assurance.Thisstrategyensuressafedefaultbehaviorwhile
| assurance | associated |     | with | each authentication |     | method | prior |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ---- | ------------------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
avoidingoverestimationofauthenticationassurance.
to any runtime observations. The authentication method In the absence of prior data, the system initializes
| strength | initialization |              | strategies | depend       |           | on historical | obser-     |                    |     |        |         |              |     |      |      |
| -------- | -------------- | ------------ | ---------- | ------------ | --------- | ------------- | ---------- | ------------------ | --- | ------ | ------- | ------------ | --- | ---- | ---- |
|          |                |              |            |              |           |               |            | the authentication |     | method | utility | coefficients |     | from | (32) |
| vations, | the            | availability |            | of standards | guidance, |               | and expert |                    |     |        |         |              |     |      |      |
uniformly,as:
| knowledge.                                              |     | These | strategies | differ | only | in how | the initial |     |     |      |     |     |     |               |     |
| ------------------------------------------------------- | --- | ----- | ---------- | ------ | ---- | ------ | ----------- | --- | --- | ---- | --- | --- | --- | ------------- | --- |
| strengthvalueisinstantiated;thesubsequentenforcementand |     |       |            |        |      |        |             |     |     |      |     |     | 1   |               |     |
|                                                         |     |       |            |        |      |        |             |     |     | γ =γ | =γ  | =γ  | =   |               |     |
|                                                         |     |       |            |        |      |        |             |     |     | S    | R   | P B |     |               |     |
| adaptationlogicremainsunchanged.                        |     |       |            |        |      |        |             |     |     |      |     |     | 4   |               |     |
| 77862                                                   |     |       |            |        |      |        |             |     |     |      |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Under this assumption, the authentication method utility c: INITIALIZATIONUNDERMAXIMALUNCERTAINTY
functionmodeledin(32)reducesto: When neither historical data nor expert knowledge is
available,conservativedefaultsareused:
1
U = (logS(m)+Rel(m)+PR(m)−Pr[Break(m)])
m 4 πx,(0) =πx , x ∈{fail,degrade,fallback},
m base
This uniform initialization treats all security-relevant withπfb >πdeg ≥πfail.
propertiesofanauthenticationmethodasequallyimportant. base base base
TheresultingutilityU isinterpretedasasecurityscoreand
m 5) ONLINELEARNINGANDADAPTATIONOF
isnormalizedviasoftmaxtoobtaintheauthenticationmethod
AUTHENTICATIONPENALTIES
weight:
The penalty recalibration process operates on instantaneous
e
λUm penalty signals generated by dynamic attribute analysis,
w m = P
m′∈M
e λU m′ a
ev
d
i
j
d
u
e
st
n
i
c
n
e
g
a
th
n
e
d
ir
sy
im
st
p
em
act
p
o
o
n
lic
tr
y
u
.
standriskbasedonaccumulated
For each penalty type x, a Beta posterior ρx ∼
The uniform initialization is adopted solely for baseline m
evaluation and reproducibility; the coefficients γ i can be Beta(α m x,β m x) is maintained. Upon observing a session
outcomeR(t),theposteriorparametersareupdatedas:
re-estimated or adapted using security outcomes once the
systemisoperational. αx ←αx +1[R(t)=1], βx ←βx +1[R(t)=0] (37)
Regardless of the initialization strategy, authentication m m m m
strength is treated as an intrinsic, static property of the Penaltiesarerecalibratedusingadelta-basedupdaterule:
authentication method. Runtime behavior, authentication
outcomes,andcontextualfactorsdonotmodifyS(m)directly π m x,(t) =π m x,(t−1)+γ x (cid:0)E[ρ m x,(t)]−E[ρ m x,(t−1)] (cid:1), (38)
andareinsteadcapturedthroughauthenticationpenaltiesand
subjecttoboundsπmin ≤πx,(t) ≤πmax.
contextual trust signals. Authentication strengths are recal- m m m
ibrated as standards evolve (e.g., NIST standards revision),
whenexploitationofthemethodisreported,orcryptographic T. INTEGRATIONOFAUTHENTICATIONSTRENGTHAND
breaksoccur. PENALTIESINTOAUTHORIZATIONTHRESHOLDS
Thisseparationensuresthatdifferencesbetweeninitializa- Authorization decisions in the proposed framework are
tionstrategiesaffectonlybaselineassuranceanddonotalter governed by both the intrinsic assurance provided by
threatmodelingassumptionsorenforcementdecisions. authentication methods and the dynamic trust and risk
signals accumulated during system interaction. Authenti-
cation strength acts as a minimum assurance gate, while
4) AUTHENTICATIONPENALTYINITIALIZATIONSTRATEGIES
authenticationpenaltiesdynamicallyadjusttheeffectivetrust
a: INITIALIZATIONUSINGSTANDARDSANDHISTORICAL
andattacksuccessprobability.
OBSERVATIONS
When historical data is available, penalties are initialized
1) PENALTY-ADJUSTEDEFFECTIVEAUTHENTICATION
using empirical attack correlations. We model the Beta
distribution: STRENGTH
Authentication penalties degrade the effective assurance of
ρx =Pr(R=1|x), x ∈{fail,degrade,fallback}, an authentication method without modifying its intrinsic
m
strength. We define the penalty-adjusted authentication
as the probability distribution of an attack scenario. Initial strengthas:
penaltiesaredefinedas:
S ˆ
eff
(m,t)=S ˆ (m)−λ (cid:53)·(cid:53)
m
(t), (39)
π
m
x,(0) =κ
x
E[ρ
m
x],
where (cid:53) (t) is the cumulative authentication penalty and
m
withκ >κ ≥κ .
λ
(cid:53)
>0isapolicy-definedscalingfactor.
fb deg fail
2) PENALTY-ADJUSTEDTRUSTTHRESHOLD
b: INITIALIZATIONUSINGEXPERTKNOWLEDGE
Authentication penalties also influence authorization indi-
Intheabsenceofhistoricaldata,penaltiesareinitializedusing
rectlythroughtrustdegradation:
expert-definedpriorsreflectingtheintrinsicweaknessofthe
authenticationmethod: Trust(C(t))=Trust (C(t))− X (cid:53) (t), (40)
attr m
πx,(0) =µ (1−S(m)), x ∈{fail,degrade,fallback},
m∈M(t)
m x
(36) ensuring that repeated authentication failures or downgrade
attemptsrapidlyreducetrustbelowauthorizationthresholds
withµ >µ ≥µ . forsensitiveresources.
fb deg fail
VOLUME14,2026 77863

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
3) AUTHORIZATIONGRANTCONDITION • Step-upauthenticationtoastrongermethodm′suchthat
|     |     |     |     |     |     |     |     |     | S ˆ (m′,t)≥S | ˆ   | (C(t),R | );  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | --- | --- | --- | --- |
Let R s denote a protected resource with sensitivity level eff req s
σ(R ).Anauthorizationgranteventattimet isdefinedas • Tokenrevocationorscopereduction;
s
• Accessdenialorsessiontermination.
|     |     | (t)=(cid:0) | S(t),C(t),T,t |     | (cid:1), |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E
|            |     | g          |                |     |        |      |        |     | Thismechanismenablescontinuousauthorization,ensur- |     |            |     |        |          |        |
| ---------- | --- | ---------- | -------------- | --- | ------ | ---- | ------ | --- | -------------------------------------------------- | --- | ---------- | --- | ------ | -------- | ------ |
|            |     |            |                |     |        |      |        | ing | that authentication                                |     | assurance, |     | trust, | and risk | remain |
| where S(t) | is  | the active | authentication |     | state, | C(t) | is the |     |                                                    |     |            |     |        |          |        |
sessioncontext,andT istheissuedauthorizationtoken. alignedwithresourcesensitivitythroughoutthesession.
| The          | authorization |     | token grant | event | from | (8) | can be |     |                                          |     |     |     |     |     |     |
| ------------ | ------------- | --- | ----------- | ----- | ---- | --- | ------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| rewrittenas: |               |     |             |       |      |     |        | U.  | BASELINEPARAMETERIZATIONFOREVALUATIONAND |     |     |     |     |     |     |
POLICYTUNING
|     |     |     |     | ˆ (m,t)≥S |     | ˆ (C(t),R |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E (t) ⇐⇒ AuthValid(S(t)) ∧ S ) Authentication strength values are indicative baselines used
| g   |     |     |     | eff |     | req | s   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Trust(C(t))≥τ
| ∧   |     |       | (R ) |     |     |     |     | forevaluationandpolicytuning,derivedfromtheassurance |     |     |     |     |     |     |     |
| --- | --- | ----- | ---- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | grant | s    |     |     |     |     |                                                      |     |     |     |     |     |     |     |
Pr[AttackSuccess|C(t)]≤δ ), propertiesdefinedinNISTSP800-63BandFIDOspecifica-
| ∧   |     |     |     |       | (R  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | grant | s   |     |     |     |     |     |     |     |     |     |     |
tions,anddonotimplyformalcertification.
ˆ
where S (m) denotes effective authentication strength, Table 7 maps common authentication methods to NIST
eff
S (t) = f(Pr[AttackSuccess | C(t)]), τ (R ) is the AALandFIDO,alongwithindicativebaselineauthentication
| req |     |     |     |     |     | grant s |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
δ
minimum trust threshold, and grant (R s ) is the maximum strengthsandpenaltiesforevaluationandpolicytuning.
| acceptable | attack | success | probability, |     | thereby | allowing |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | ------------ | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
authentication degradation and fallback behavior to directly V. DETECTINGANDENFORCINGHARDVIOLATIONS
influenceauthorizationoutcomes. Hardviolationsrepresentnon-compensablestatesthatresult
inrequestdenialandsuspensionoflearningandrecalibration.
4) PENALTY-AMPLIFIEDATTACKSUCCESSPROBABILITY We model the computation and validation of hard violation
Authenticationpenaltiesrepresentruntimeevidenceofdegra- signalsbelow.
| dation, | failure, | or fallback | behavior | of  | authentication |     | meth- |     |     |     |     |     |     |     |     |
| ------- | -------- | ----------- | -------- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ods,indicatingincreasedadversarialactivity.Authentication 1) GEO-VELOCITYCOMPUTATION
penalties thus provide a baseline of the break probability of Geo-velocity,calculatedfromthetimebetweenrequestsand
the authentication method and reflect elevated risk. This is the geographic distance, is crucial for risk assessment and
in line with NIST SP 800-30, which recommends treating analysis.Thegeo-velocityriskmodelisrepresentedusingthe
| indicatorsasameasureofthelikelihoodofathreat. |           |             |     |          |     |                |     | riskFunction: |     |     |     |     |     |     |     |
| --------------------------------------------- | --------- | ----------- | --- | -------- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| With                                          | this, the | probability | of  | breaking | an  | authentication |     |               |     |     |     |     |     |     |     |
methodisremodeledas:
|     |     |     |     |     |     |     |     |     |     |      |     | ifv≤v |       |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | ----- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |  0 |     |       | saf e |     |     |
v−
Pr[Break(m)|(cid:53) (t)]=Pr[Break(m)] (cid:0) 1+η (cid:53) (t) (cid:1), v s afe
|     |     | m   |     |     |     | m m |     |     | G(v)= |          |     | ifv  | < v  | <v  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | ---- | ---- | --- | --- |
|     |     |     |     |     |     |     |     |     |       | v        | − v |      | safe | max |     |
|     |     |     |     |     |     |     |     |     |       | ∞ max |     | safe |      |     |     |
where (cid:53) (t) represents the authentication penalty imposed ifv≥v
|         | m                 |     |           |     |          |            |     |     |     |     |            |     | max       |     |     |
| ------- | ----------------- | --- | --------- | --- | -------- | ---------- | --- | --- | --- | --- | ---------- | --- | --------- | --- | --- |
| in case | of authentication |     | challenge |     | failure, | downgrade, |     |     |     |     |            |     |           |     |     |
|         |                   |     |           |     |          |            |     |     |     | =   | (cid:49) d |     | (cid:49)d |     |     |
or fallback using m, and η > 0 is a method-specific where velocity v (cid:49) km/h and is the Haversine
|     |     |     | m   |     |     |     |     |     |     |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distancebetweentwoconsecutivelogins.
sensitivityparameter.
|                                                       |     |     |     |     |     |     |     |     | The geo-velocity |     | safe threshold |     | v is | set between | 800- |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------- | --- | ---- | ----------- | ---- |
| Theauthentication-phaseattackprobabilitydefinedin(15) |     |     |     |     |     |     |     |     |                  |     |                |     | safe |             |      |
isredefinedas: 1000 km/h [60]. The threshold v is set to 1000 km/h as
max
|           |     |        |     |     |     |     |     | the | upper bound | of  | plausible | commercial |     | air travel | speed, |
| --------- | --- | ------ | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ---------- | --- | ---------- | ------ |
| Pr[Attack |     | |C(t)] |     |     |     |     |     |     |             |     |           |            |     |            |        |
auth allowing margin for geolocation inaccuracy and clock skew
|     |     | (cid:16) |     |     |     |     | (cid:17) |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Y 1−Pr[Break(m)](1+η (cid:53) while excluding physically impossible transitions. Speeds
| =1− |     |     |     |     |     | m m (t)) |     |       |                |     |               |     |        |        |           |
| --- | --- | --- | --- | --- | --- | -------- | --- | ----- | -------------- | --- | ------------- | --- | ------ | ------ | --------- |
|     |     |     |     |     |     |          |     | below | this threshold |     | but exceeding |     | normal | travel | rates are |
m∈M(t)
(cid:16) (cid:17) treated as probabilistic anomalies rather than deterministic
| .   | Y 1−Pr[Forge(a)|C(t)) |     |     |     |     |     |     |             |          |     |      |              |           |     |          |
| --- | --------------------- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ---- | ------------ | --------- | --- | -------- |
|     |                       |     | i   |     |     |     |     | violations. | Requests |     | with | geo-velocity | exceeding |     | the hard |
∈C(t)
ai limit are blocked and reported as risky, given typical user
displacement.
Thismodelingcontributesdirectlytothecompositeattack
φ ,φ
successprobabilityusedinauthorizationdecisions. Given two points with latitudes 1 2 and longitudes
|     |     |     |     |     |     |     |     | λ   | ,λ            |     |               |          |     | (cid:49)d     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | -------- | --- | ------------- | --- |
|     |     |     |     |     |     |     |     |     | (in radians), |     | the Haversine | distance |     | is calculated |     |
|     |     |     |     |     |     |     |     | 1   | 2             |     |               |          |     |               |     |
as:
5) ADAPTIVEAUTHORIZATIONENFORCEMENT
|                                          |     |                               |     |     |     |              |     |     |           | (cid:18)(cid:49)φ(cid:19) |           |          |      | (cid:18)(cid:49)λ(cid:19) |     |
| ---------------------------------------- | --- | ----------------------------- | --- | --- | --- | ------------ | --- | --- | --------- | ------------------------- | --------- | -------- | ---- | ------------------------- | --- |
| Therequiredauthenticationstrengthattimet |     |                               |     |     |     | isdefinedas: |     |     |           |                           |           |          |      |                           |     |
|                                          |     |                               |     |     |     |              |     |     | a=sin2    |                           | +cosφ     | cosφ     | sin2 |                           | ,   |
|                                          |     |                               |     |     |     |              |     |     |           |                           |           | 1        | 2    |                           |     |
|                                          |     |                               |     |     |     |              |     |     |           |                           | 2         |          |      | 2                         |     |
|                                          | S   | (t)=f(Pr[AttackSuccess|C(t)]) |     |     |     |              |     |     |           |                           | (cid:16)√ | √        |      |                           |     |
|                                          | req |                               |     |     |     |              |     |     |           |                           |           | (cid:17) |      |                           |     |
|                                          |     |                               |     |     |     |              |     |     | c=2·atan2 |                           | a,        | 1−a      | ,    |                           |     |
Ifanyconditionin(V-T3)isviolated,thesystemenforces
·c,
| oneofthefollowingactionsbasedonpolicy: |     |     |     |     |     |     |     |     | d =R | E   |     |     |     |               | (41) |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------------- | ---- |
| 77864                                  |     |     |     |     |     |     |     |     |      |     |     |     |     | VOLUME14,2026 |      |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE7. IndicativebaselineauthenticationstrengthsandpenaltiesmappedtoNISTAALandFIDO.
| where:        |       |                           |     |     |     |     | attackerrebuildstheapplication,thevaluechanges,andcan |     |         |             |           |     |           |
| ------------- | ----- | ------------------------- | --- | --- | --- | --- | ----------------------------------------------------- | --- | ------- | ----------- | --------- | --- | --------- |
| (cid:49)φ     | =φ −φ |                           |     |     |     |     | bedetectedbytheserver.                                |     |         |             |           |     |           |
| •             |       | (differenceinlatitudes),  |     |     |     |     |                                                       |     |         |             |           |     |           |
|               | 2     | 1                         |     |     |     |     | The algorithms                                        |     | for the | application | integrity |     | check and |
| • (cid:49)λ=λ | −λ    | (differenceinlongitudes), |     |     |     |     |                                                       |     |         |             |           |     |           |
|               | 2     | 1                         |     |     |     |     | dynamicbuildsecretinjectionarepresentedinAlgorithms13 |     |         |             |           |     |           |
• R E istheEarth’sradius(meanradius=6,371km),
|     |     |     |     |     |     |     | and 14, | respectively. |     | The corresponding |     | anti-tampering |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ----------------- | --- | -------------- | --- |
• atan2(y,x)isthetwo-argumentarctangentfunction.
techniquesaredescribedinAlgorithm15.
2) APPLICATIONINTEGRITYENFORCEMENT
With the increased penetration of smartphones, mobile W. DEVICEINTEGRITYENFORCEMENT
|              |      |         |        |         |     |             | In ZT architecture, |     | device | posture | is  | a trust | signal that |
| ------------ | ---- | ------- | ------ | ------- | --- | ----------- | ------------------- | --- | ------ | ------- | --- | ------- | ----------- |
| applications | form | a major | access | medium. | The | application |                     |     |        |         |     |         |             |
attributesdescribedinTable2provideacontextualattribute is given as much weight as user identity. Policy-driven
subset that can be used to statically verify the origin of the specificationscandetectifthedeviceposturedoesnotmeet
request.Theapplicationattributesprovideawaytouniquely the policy-set requirements and deny access, even if the
identify ‘‘the application, running on device’’ combination. user identity is valid. Just as trust signals related to users’
|              |     |          |           |     |            |         | behavioral | and contextual |     | attributes | are | validated, | device- |
| ------------ | --- | -------- | --------- | --- | ---------- | ------- | ---------- | -------------- | --- | ---------- | --- | ---------- | ------- |
| In addition, | the | proposed | framework |     | introduces | two new |            |                |     |            |     |            |         |
approachestomitigatetheriskofapplicationspoofing. originated attributes are also continuously monitored. The
proposedZeTHAAframeworkintroducesanadaptivedevice
|     |     |     |     |     |     |     | authentication | protocol |     | that aligns | with | NIST guidance | on  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ----------- | ---- | ------------- | --- |
a: APPLICATIONINTEGRITYCHECKS
|        |           |            |     |            |        |             | device binding | by  | combining |     | contextual | device | attributes |
| ------ | --------- | ---------- | --- | ---------- | ------ | ----------- | -------------- | --- | --------- | --- | ---------- | ------ | ---------- |
| During | the first | connection | of  | the device | to the | system, the |                |     |           |     |            |        |            |
withhardware-backedverification.Passivedeviceattributes
| Cyclic Redundancy |                 | Check  | (CRC)       | value        | of the   | constituent    |                  |                   |                |            |                   |          |            |
| ----------------- | --------------- | ------ | ----------- | ------------ | -------- | -------------- | ---------------- | ----------------- | -------------- | ---------- | ----------------- | -------- | ---------- |
|                   |                 |        |             |              |          |                | provide evidence |                   | that adds      | to         | or degrades       | trust.   | Contex-    |
| files of          | the application |        | package     | is computed  |          | and stored on  |                  |                   |                |            |                   |          |            |
|                   |                 |        |             |              |          |                | tual trust       | degradation       | and            | risk-based | escalation        |          | result in  |
| the server.       | Upon            | each   | application | load         | in the   | user’s device, |                  |                   |                |            |                   |          |            |
|                   |                 |        |             |              |          |                | hardware         | challenges        | that           | require    | the participating |          | device     |
| the CRC           | is recomputed   |        | and         | compared     | with the | CRC data       |                  |                   |                |            |                   |          |            |
|                   |                 |        |             |              |          |                | to establish     | a hardware-backed |                |            | cryptographic     | binding. | This       |
| on the            | server to       | ensure | that        | the binaries | have     | not been       |                  |                   |                |            |                   |          |            |
|                   |                 |        |             |              |          |                | adaptive         | device            | authentication |            | protocol          | offers   | resistance |
tamperedwith.
|     |     |     |     |     |     |     | to replay  | and device | impersonation, |       | consistent |         | with NIST |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | -------------- | ----- | ---------- | ------- | --------- |
|     |     |     |     |     |     |     | SP 800-63B | and        | Zero           | Trust | principles | defined | in NIST   |
b: DYNAMICBUILDSECRETINJECTION SP 800-207. Algorithms 16 and 17 describe the proposed
DynamicBuildSecretInjectioncomprisesinjectingarandom AdaptiveDeviceAuthenticationProtocol.
value into the application properties at build time. This With the system definitions described, we move into the
value is stored in the server during the first contact. If an securityguaranteesformalizedbytheZeTHAAframework.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     | 77865 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm13ApplicationIntegrityVerification Algorithm14SecureBuildSecretEmbeddingandVerifica-
| Require: |     | serverKey←HKDF(masterKey,‘‘checksum′′ |     |     |     |     | ▷   | tionProtocol |     |        |     |     |                    |     |     |
| -------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | ------ | --- | --- | ------------------ | --- | --- |
|          |     |                                       |     |     |     |     |     | Require:     |     | κ ←256 |     |     | ▷Securityparameter |     |     |
Keyderivation
|     |        |                 |     |     |     |     |     |     |        | ←HKDF-SHA512(k |     |        | ,’’secret-wrap’’) |     |     |
| --- | ------ | --------------- | --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | ------ | ----------------- | --- | --- |
|     | appCRC | ←0,fileHashes←∅ |     |     |     |     |     | 1:  | K wrap |                |     | master |                   |     |     |
1:
|     |                         |     |     |                          |     |     |     | 2:  | procedureEmbedSecret(S |         |     | ,build_config) |     |                |     |
| --- | ----------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | ---------------------- | ------- | --- | -------------- | --- | -------------- | --- |
| 2:  | procedure               |     |     | ComputeAndRegisterCheck- |     |     |     |     |                        |         |     | src            |     |                |     |
|     |                         |     |     |                          |     |     |     |     | σ                      | ←PRF(κ) |     |                |     | ▷256-bitsecret |     |
|     | sum(ApplicationPackage) |     |     |                          |     |     |     | 3:  |                        |         |     |                |     |                |     |
|     |                         |     |     |                          |     |     |     |     | σ                      |         |     |                | ,σ) |                |     |
foreachfile∈ApplicationPackageinparalleldo 4: enc ←AES-GCM-SIV(K wrap
3:
|     |     | hash←xxHash64(file.content) |     |     |     |     |     |     | //ObfuscatedInjection |               |     |     |                   |     |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --------------------- | ------------- | --- | --- | ----------------- | --- | --- |
| 4:  |     |                             |     |     |     |     |     | 5:  |                       |               |     |     |                   |     |     |
|     |     |                             |     |     |     |     |     |     |                       | ∈MatchFiles(S |     |     | ,*.cpp,py,java)do |     |     |
|     |     | fileHashes.add(hash)        |     |     |     |     |     | 6:  | foreachf              | i             |     | src |                   |     |     |
5:
←appCRC ⊕hash ▷XORchaining 7: InjectAsConst(f ,base64(σ [0:32]))
| 6:  |           | appCRC |                                |     |     |     |     |     |        |                   | i   |           | enc |         |     |
| --- | --------- | ------ | ------------------------------ | --- | --- | --- | --- | --- | ------ | ----------------- | --- | --------- | --- | ------- | --- |
|     |           |        |                                |     |     |     |     |     |        | InjectAsComment(f |     | ,base64(σ |     | [32:])) |     |
| 7:  | endfor    |        |                                |     |     |     |     | 8:  |        |                   |     | i         | enc |         |     |
|     | sealedCRC |        | ←HMAC-SHA256(serverKey,appCRC) |     |     |     |     | 9:  | endfor |                   |     |           |     |         |     |
8:
|     |                                             |     |     |     |                    |     |     | 10: | CompileWithPIE(S               |     |     | ,build_config) |      |      | ▷   |
| --- | ------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | ------------------------------ | --- | --- | -------------- | ---- | ---- | --- |
| 9:  | SecureStore(sealedCRC)                      |     |     |     | ▷Encrypteddatabase |     |     |     |                                |     | src |                |      |      |     |
| 10: | endprocedure                                |     |     |     |                    |     |     |     | Position-IndependentExecutable |     |     |                |      |      |     |
|     |                                             |     |     |     |                    |     |     | 11: | StoreSecret(HMAC-SHA256(K      |     |     |                |      | ,σ)) |     |
| 11: | procedureVerifyChecksum(ApplicationPackage) |     |     |     |                    |     |     |     |                                |     |     |                | wrap |      |     |
endprocedure
| 12: | localCRC |     | ←0  |     |     |     |     | 12: |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
foreachfile∈ApplicationPackagedo 13: procedureVerifySecret(B app )
13:
|     |                        |          |     | ←   |     |          | ⊕   | 14: | σ   | ←ExtractFromBinary(B   |     |     | )   |            |     |
| --- | ---------------------- | -------- | --- | --- | --- | -------- | --- | --- | --- | ---------------------- | --- | --- | --- | ---------- | --- |
| 14: |                        | localCRC |     |     |     | localCRC |     |     | ext |                        |     |     | app |            |     |
|     |                        |          |     |     |     |          |     |     | σ   | ←AES-GCM-SIV-Decrypt(K |     |     |     | ,σ         |     |
|     | xxHash64(file.content) |          |     |     |     |          |     | 15: | dec |                        |     |     |     | wrap ext ) |     |
iffile∈/ fileHashesthen ▷Detectnew/deleted 16: seal ←FetchSeal()
| 15: |       |     |     |     |     |     |     |     |                     | server         |     |       |      |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | ------------------- | -------------- | --- | ----- | ---- | --- | --- |
|     |       |     |     |     |     |     |     |     | seal                | ←HMAC-SHA256(K |     |       | ,σ   | )   |     |
|     | files |     |     |     |     |     |     | 17: |                     | local          |     |       | wrap | dec |     |
|     |       |     |     |     |     |     |     |     | if¬SecureEqual(seal |                |     | ,seal |      |     |     |
Reject(‘‘Unauthorizedfilemodification’’) 18: local server )then
16:
|     |              |       |                                  |     |     |     |     | 19: |          | Reject(‘‘Tamperingdetected’’) |     |     |                   |     |     |
| --- | ------------ | ----- | -------------------------------- | --- | --- | --- | --- | --- | -------- | ----------------------------- | --- | --- | ----------------- | --- | --- |
| 17: |              | endif |                                  |     |     |     |     |     |          |                               |     |     |                   |     |     |
|     |              |       |                                  |     |     |     |     |     |          | FireCanaryToken()             |     |     | ▷Triggerdeception |     |     |
| 18: | endfor       |       |                                  |     |     |     |     | 20: |          |                               |     |     |                   |     |     |
|     | receivedSeal |       | ←HMAC-SHA256(serverKey,localCRC) |     |     |     |     |     | measures |                               |     |     |                   |     |     |
19:
else
| 20: | ifreceivedSeal |                                        |     | ̸=SecureFetch()then |     |     |     | 21: |     |               |     |     |     |     |     |
| --- | -------------- | -------------------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
|     |                | RejectAndAudit(‘‘Integrityviolation’’) |     |                     |     |     |     | 22: |     | GrantAccess() |     |     |     |     |     |
21:
|     |     |                |     |     | ▷Securitymonitoring |     |     | 23: | endif |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | ------------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
| 22: |     | ReportToSIEM() |     |     |                     |     |     |     |       |     |     |     |     |     |     |
endprocedure
| 23: | endif |     |     |     |     |     |     | 24: |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
endprocedure
24:
Algorithm15Anti-TamperingTechniques
|     |                    |     |     |     |     |     |     | 1:  | functionInjectAsConst(file,data) |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
| VI. | SECURITYGUARANTEES |     |     |     |     |     |     | 2:  | varName←RandomIdentifier()       |     |     |     |     |     |     |
This section formalizes the security guarantees provided by InsertCode(file,’’constautovarName = ’’+data+
3:
| theproposedZeTHAAframework.Theguaranteesarestated |     |     |     |     |     |     |     |     | ’’;’’) |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
relative to baseline assumptions and follow directly from InsertDeadCode(file,varName) ▷Control-flow
4:
the models and mechanisms introduced in the preceding obfuscation
| sections. |     |     |     |     |     |     |     | 5:  | endfunction |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
functionExtractFromBinary(binary)
6:
A. IMPOSSIBLETRAVELELIMINATIONGUARANTEE
|           |     |               |     |                     |     |     |        | 7:  | mem←ReadELF/PE/MachO(binary) |     |     |     |         |     |     |
| --------- | --- | ------------- | --- | ------------------- | --- | --- | ------ | --- | ---------------------------- | --- | --- | --- | ------- | --- | --- |
| Guarantee |     | 1 (Impossible |     | State Elimination). |     | The | system |     |                              |     |     |     |         |     |     |
|           |     |               |     |                     |     |     |        |     | FindXORedSegments(mem,K      |     |     |     | [0:16]) |     |     |
|           |     |               |     |                     |     |     |        | 8:  |                              |     |     |     | wrap    |     |     |
guaranteesthatnoauthorizationgrantorsessioncontinuation
|        |       |            |     |              |            |            |     | 9:  | returnReconstructSecret(mem) |     |     |     |     |     |     |
| ------ | ----- | ---------- | --- | ------------ | ---------- | ---------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
| occurs | under | physically |     | or logically | impossible | contextual |     |     |                              |     |     |     |     |     |     |
|        |       |            |     |              |            |            |     | 10: | endfunction                  |     |     |     |     |     |     |
states.Formally,foranytimet,
|     | ImpossibleTravel(t)=1 |     |     |     | ⇒ Grant(t)=0. |     |     |            |     |                         |     |     |          |        |     |
| --- | --------------------- | --- | --- | --- | ------------- | --- | --- | ---------- | --- | ----------------------- | --- | --- | -------- | ------ | --- |
|     |                       |     |     |     |               |     |     | suspicious |     | activity. Specifically, |     | for | any time | window | W   |
Grant(t) ⇐⇒ ¬ImpossibleTravel(t) ∧ AuthValid(S(t)) duringwhichLearn(t)=0forallt ∈W,theprofileremains
invariant:
|     |     |     | ∧ S(m)≥S                     | (C(t)) |     |     |      |     |     |        |      |            |     |     |     |
| --- | --- | --- | ---------------------------- | ------ | --- | --- | ---- | --- | --- | ------ | ---- | ---------- | --- | --- | --- |
|     |     |     |                              | req    |     |     |      |     |     | ∀t ∈W, | Pi(t | +1)=Pi(t). |     |     |     |
|     |     |     | ∧ Pr[AttackSuccess|C(t)]≤δ(R |        |     | ).  | (42) |     |     |        | u    |            | u   |     |     |
s
|     |     |     |     |     |     |     |     | Moreover, |     | when learning |     | is permitted, |     | the maximum |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | ------------- | --- | ----------- | --- |
B. SECURITYGUARANTEE:POISONINGRESISTANCE cumulative influence of any sequence of observations of
Guarantee (Profile Poisoning Resistance). Under the length n is bounded by 1 − (1 − γ)n, ensuring that
learning policy defined in (1)–(2), an adversary cannot no finite sequence of events can rapidly redefine normal
| significantly |     | shift | a behavioral | profile | through | transient | or  | behavior. |     |     |     |     |     |               |     |
| ------------- | --- | ----- | ------------ | ------- | ------- | --------- | --- | --------- | --- | --- | --- | --- | --- | ------------- | --- |
| 77866         |     |       |              |         |         |           |     |           |     |     |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm16AdaptiveDeviceAuthenticationProtocol increases monotonically, implying that additional penalties
1: procedureDeviceAuthentication(C(t),P u ,θ dev ) strictlyincreaseadversarialsuccessprobability. □
2: (cid:49) pen ←0
3: D OS ←ExtractOSAttributes(C(t)) 3) TRUSTDEGRADATIONANDRAPIDLOSSGUARANTEE
4: foralld i ∈D OS do Theorem3(AsymmetricTrustEvolution): Trust accumu-
5: ifMatch(d i ,P u (d i ))=1then lates gradually through positive contextual evidence but
6: Trust(t)←Trust(t)+w i degrades rapidly in the presence of authentication penalties
orattributeviolations.
7: else
8:
(cid:49)
pen
←(cid:49)
pen
+π
i
Proof:Trustiscomputedas:
9: endif Trust(t)=Trust (C(t))− X (cid:53) (t)− X π(t).
attr m i
10: endfor m∈M(t) i
11: if(cid:49) pen ≥θ dev then
Positive evidence contributes additively through weighted
12: D RS ←SelectHWChallengeSet(D HW \D OS )
attributes, while penalties are unbounded in frequency and
13: SendChallenge(D RS )
additive in magnitude, ensuring faster trust decay than
14: BindState(D RS ,C(t)) accumulation. □
15: LearningEnabled(t)←0
16: endif 4) ADAPTIVEENFORCEMENTGUARANTEE
17: endprocedure Theorem4(AdaptiveStep-UpandRevocation): Ifauthen-
tication strength, trust, or acceptable attack risk thresholds
Algorithm17HardwareChallengeVerification are violated at any time, the system enforces step-up
1: procedureVerifyDeviceChallenge(U id ,C(t),D r R e S sp ) authe P n r ti o c o a f t : io A n u , t t h o o k r e i n za r t e i v o o n c i a s ti c o o n n , t o in r u a o cc u e s s ly st e e v r a m lu in a a te ti d on a . gainst
2 3 : : D if s R V t S a e t r e if ← yH R W e P tr r i o e o v f eB (D o r u e n sp d , S D ta s t ta e t ( e U ) i = d ) 1then thresholds S ˆ req , τ grant , and δ grant . Violation of any condition
RS RS triggerspredefinedenforcementactions,ensuringthataccess
4: Trust(t)←Trust(t)+w HW
isnevermaintainedunderinsufficientassuranceorexcessive
5: LearningEnabled(t)←1
risk. □
6: else
7:
Trust(t)←Trust(t)−π
HW 5) END-TO-ENDZEROTRUSTGUARANTEE
8: HardViolation(t)←1 Theorem5(End-to-EndZeroTrustEnforcement): Under
9: LogSecurityEvent(U id ,t) the stated assumptions, the proposed framework ensures
10: endif that no access is granted or retained solely based on
11: endprocedure prior authentication, and that all access decisions are
continuously re-evaluated against current authentication
assurance,contextualtrust,andestimatedattackrisk.
1) AUTHENTICATIONASSURANCEGUARANTEE Proof: Initial access requires satisfaction of authen-
Theorem1(MinimumAuthenticationAssurance): An tication strength, trust, and risk constraints. Continuous
authorization grant is issued only if the effective authen- monitoring updates penalties, trust, and attack probability.
tication strength meets or exceeds the required assurance Anydeviationfromacceptableboundstriggersenforcement
thresholdforthecurrentcontextandresourcesensitivity. perTheorem4.Therefore,trustisneverimplicit,persistent,
Proof: By construction, authorization is granted only orunconditional. □
whenS ˆ (m,t) ≥ S ˆ (C(t),R ),whereS ˆ (m,t) = S ˆ (m)− Havingestablishedthesecurityguarantees,Table8maps
eff req s eff
λ (cid:53) (cid:53) m (t). Since (cid:53) m (t) ≥ 0, penalties can only reduce the 7 NIST Zero Trust tenets to the proposed framework’s
effective strength, ensuring that authentication assurance is securityguarantees.
neveroverestimated. □
6) SCOPEANDLIMITATIONS
The guarantees hold relative to the accuracy of attribute
2) MONOTONICRISKAMPLIFICATIONGUARANTEE
measurements, the correct initialization of authentication
Theorem2(Penalty-InducedRiskMonotonicity): The
strengths, and the timely observation of security outcomes.
probability of a successful authentication attack is a
Compromiseoftheseassumptionsmayreducetheeffective-
monotonicincreasingfunctionofaccumulatedauthentication
ness of enforcement, but does not invalidate the structural
penalties.
guarantees of monotonic risk amplification and adaptive
Proof: The authentication attack probability is defined
control.
as:
Pr(Break(m)|(cid:53) (t))=Pr(Break(m)) (cid:0) 1+η (cid:53) (t) (cid:1), VII. EXPERIMENTALEVALUATION
m m m
A. TESTBEDANDIMPLEMENTATION
with η > 0. Since (cid:53) (t) is non-negative and increasing The evaluation was conducted on a Lenovo IdeaPad run-
m m
under negative events, the conditional break probability ning 12th Gen Intel(R) Core(TM) i5-12450H (2.00 GHz)
VOLUME14,2026 77867

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE8. MappingofsecurityguaranteestoNISTzerotrusttenets.
| TABLE9. | Datasetsummary. |     |     |     |     |     | TABLE10. Attackdistribution. |     |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
[H]
and16GBofRAM,runningWindows11HomeEdition(64-
| bit).ToevaluatetheeffectivenessoftheproposedZeTHAA |     |           |             |       |             |     |     |     |     |     | [H] |     |
| -------------------------------------------------- | --- | --------- | ----------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| framework,                                         | we  | conducted | experiments | using | a synthetic |     |     |     |     |     |     |     |
authenticationdatasetthatincorporatesrealisticuserbehav-
|         |             |            |     |                         |     |     | a single attack | pattern. | Table | 10 shows | the diversity | and |
| ------- | ----------- | ---------- | --- | ----------------------- | --- | --- | --------------- | -------- | ----- | -------- | ------------- | --- |
| ior and | adversarial | scenarios. | To  | ensure reproducibility, |     | the |                 |          |       |          |               |     |
distributionoftheattacktypesinthedataset.
sourcecode,thebaselineimplementations,andtheevaluation
scriptsareavailableat[61].
|     |     |     |     |     |     |     | B. CONTEXTUALRISKMODELING |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
Theproposedframeworkevaluatesauthenticationriskusing
1) DATASETDESCRIPTION
|                |          |               |              |          |                |     | contextual    | signals    | derived   | from device    | characteristics, | net-  |
| -------------- | -------- | ------------- | ------------ | -------- | -------------- | --- | ------------- | ---------- | --------- | -------------- | ---------------- | ----- |
| The dataset    | contains | approximately |              | 50,000   | authentication |     |               |            |           |                |                  |       |
|                |          |               |              |          |                |     | work context, | user       | mobility, | and behavioral | patterns.        | These |
| sessions       | across   | 500 users,    | generating   | close    | to 150,000     |     |               |            |           |                |                  |       |
|                |          |               |              |          |                |     | signals are   | calibrated | using     | evidence–based | weighting        | to    |
| authentication |          | events.       | Each session | includes | contextual     |     |               |            |           |                |                  |       |
estimatetheirrelativecontributiontoauthenticationrisk.
| attributes | such | as device | model, | operating | system | version, |     |     |     |     |     |     |
| ---------- | ---- | --------- | ------ | --------- | ------ | -------- | --- | --- | --- | --- | --- | --- |
geographiclocation,andtemporalloginbehavior.Thedataset
|        |             |          |     |             |       |         | 1) CONTEXTUALSIGNALS |     |     |     |     |     |
| ------ | ----------- | -------- | --- | ----------- | ----- | ------- | -------------------- | --- | --- | --- | --- | --- |
| models | user travel | patterns | and | device life | cycle | events, |                      |     |     |     |     |     |
Keycontextualsignalsinclude:
| such as | new phone | purchases, | operating | system | upgrades, |     |     |     |     |     |     |     |
| ------- | --------- | ---------- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
andapplicationversionupgrades.Approximately70%ofthe • geographicanomalydetection
sessionsrepresentnormaluserbehavior,whiletheremaining • travelstatusandtimezoneshifts
30% model adversarial scenarios. Table 9 summarizes the • devicefingerprintconsistency
• sessiontokenreusepatterns
overalldatasetcharacteristics.
• repeatedattackerIPactivity
2) DATASETPROPERTIES Thesecontextualsignalscaptureidentity,device,network,
Thedatasetmodelsmultipleadversarialscenarios,including temporal,andbehavioralcontext.Therelativeimportanceof
coordinated attack campaigns, credential theft, bot-driven each contextual feature was derived using Bayesian online
login attempts, device spoofing, session hijack, token theft calibrationviaBetaposteriorupdating.Thecalibratedresults
and replay, and application tampering. The attack classes show the probability of an attack given the exposure of the
werebalancedandevenlydistributedtopreventbiastowards attributesignal.
| 77868 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
FIGURE3. Riskscoredistributionbyclass.
| FIGURE2. Featureimportance. |     |     |     | TABLE11. | Decisionrates. |     |     |
| --------------------------- | --- | --- | --- | -------- | -------------- | --- | --- |
2) FEATUREIMPORTANCE
Therelativeimportanceofcontextualfeatures,derivedusing
| Bayesian online | calibration, | is shown | in Fig. 2. Attack |     |     |     |     |
| --------------- | ------------ | -------- | ----------------- | --- | --- | --- | --- |
τ
campaign-related features contribute the highest to risk, lower threshold was set to the 75th percentile of benign
1
followed by geographic anomalies. Device and session traffictominimizeuserfriction.
integrity-related signals, particularly fingerprint mismatch Thethresholdsweresubsequentlyderivedfromthedataset
| andsessioncontextinconsistencies,contributemoderatelyto |     |     |     | as: |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
theriskscore,whiletemporalandtravelanomaliesserveas τ =0.1180,τ =0.1809
|     |     |     |     |     | 1   | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
weakindicators.
2) POLICYDECISIONS
C. RISKSCOREBEHAVIOR Table 11 captures the policy decisions that apply thresholds
| Fig. 3 compares | the distribution | of risk | scores by class | totheevents. |     |     |     |
| --------------- | ---------------- | ------- | --------------- | ------------ | --- | --- | --- |
- benign and attack sessions. The figure shows a clear Thedatashowsthatapproximately75%ofbenignevents
separation between benign and attack events, with attack were allowed without additional verification, while 17.5%
sessionsshowingconsistentlyhigherriskvaluesthanbenign required step-up authentication. Only 7.5% of benign ses-
sessions. The attack classes form two clusters, with the sionswereincorrectlyblocked.Inthecaseofattacksessions,
majority of the sessions in the first cluster showing risk about 73% were immediately blocked, and approximately
scores ranging from 0 to 0.11, indicating stable contextual 9.7%weresubjectedtostep-upverification.Theresultsshow
behavior.Asecondgroupisidentifiedwithriskrangingfrom thattheframeworkbalancessecurityandusability,minimizes
0.12to0.4,indicatinganaturalseparationofriskvalues.This userfriction,andmaintainsattackdetection.
demonstratestheproposedframework’sabilitytodistinguish Fig. 4 shows the policy decisions based on the risk score
| anomalousbehavior.Thedistributionshowsthatthedecision |     |     |     | distribution. |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- |
thresholdscanbeplacedlogically. Thederiveddecisionthresholdsbalancebetweensecurity
andusability.Themajorityofthebenigneventswereallowed
|     |     |     |     | without | friction, while | a controlled percentage | underwent |
| --- | --- | --- | --- | ------- | --------------- | ----------------------- | --------- |
D. DECISIONPOLICYANDDETECTIONPERFORMANCE
1) THRESHOLDSELECTION step-up verification. The framework blocked a significant
|     |     |     |     | proportion | of attack events, | demonstrating | the effectiveness |
| --- | --- | --- | --- | ---------- | ----------------- | ------------- | ----------------- |
Authenticationeventsareclassifiedintothreeregionsbased
ontheircomputedriskscoredecisionthresholds.Eventswith ofarisk-basedpolicy.
| riskscoresbelowthelowerthresholdτ |     |     | areallowedwithout |     |     |     |     |
| --------------------------------- | --- | --- | ----------------- | --- | --- | --- | --- |
1
additional verification, while moderate-risk events trigger E. CLASSIFICATIONPERFORMANCE
step-up authentication until the upper threshold τ . Events To quantify the effectiveness of the proposed ZeTHAA
2
|     |     |     |     | framework, | standard classification | metrics | were computed |
| --- | --- | --- | --- | ---------- | ----------------------- | ------- | ------------- |
exceedingtheupperthresholdareclassifiedhighriskandwill
| resultindenialofaccess. |            |             |                  | usingthecalibratedriskthresholds. |     |     |     |
| ----------------------- | ---------- | ----------- | ---------------- | --------------------------------- | --- | --- | --- |
| The decision            | thresholds | τ and τ are | derived from the |                                   |     |     |     |
1 2
dataset.Theupperthresholdτ
|     |     | 2 iscomputedasthemaximum |     | 1) CONFUSIONMATRIX |     |     |     |
| --- | --- | ------------------------ | --- | ------------------ | --- | --- | --- |
Youden’s value youden = tpr −fpr, where tpr denotes the Table 12 presents the global confusion matrix comparing
truepositiverateandfprrepresentsthefalsepositiverate.The theinputdatasettotheZeTHAAframework’soutput,while
VOLUME14,2026 77869

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
FIGURE4. Policydecisionwithriskscoredistribution. FIGURE6. Risk-trustcorrelation.
TABLE14. Stealthattackmetrics.
TABLE12. Globalconfusionmatrix.
TABLE13. Performancemetrics.
|     |     |     |     | The low-risk | phase            | is represented   | by the region | with risk   |
| --- | --- | --- | --- | ------------ | ---------------- | ---------------- | ------------- | ----------- |
|     |     |     |     | scores less  | than the step-up | threshold.       | While         | this region |
|     |     |     |     | shows a      | high density     | of benign events | as expected,  | it also     |
showsthepresenceofattackevents.Thesubsetofattacksthat
|     |     |     |     | fall in the | low-risk region | can be considered | stealth | attacks, |
| --- | --- | --- | --- | ----------- | --------------- | ----------------- | ------- | -------- |
whereadversarialbehaviordoesnotmanifeststronglyacross
theobservedcontextualsignals.Table14recordsthenumber
ofattackeventsthatwerefoundinthelow-riskzone.
|     |     |     |     | However,      | even in the         | low-risk area,     | malicious       | activities  |
| --- | --- | --- | --- | ------------- | ------------------- | ------------------ | --------------- | ----------- |
|     |     |     |     | were found    | to dominate         | the lower trust    | areas, while    | benign      |
|     |     |     |     | activities    | clustered in        | the higher trust   | region.         | This trend  |
|     |     |     |     | continues     | into the transition | phase between      | the             | thresholds. |
|     |     |     |     | The higher    | risk zone           | (>0.18) represents | a concentration | of          |
|     |     |     |     | attack events | and is also         | characterized      | by a high       | density     |
|     |     |     |     | of events     | with very low       | trust scores.      | The diagonal    | linear      |
trendrepresentsthecorrelationbetweenriskandtrustinthe
framework:astheriskscoreincreases,thetrustscoredeclines
|     |     |     |     | linearly. | This suggests | that risk alone | is not | sufficient to |
| --- | --- | --- | --- | --------- | ------------- | --------------- | ------ | ------------- |
distinguishevents;trustscoresaretheprimarydifferentiator.
|     |     |     |     | Fig. 6 | also closely corresponds | to  | the findings | noted in |
| --- | --- | --- | --- | ------ | ------------------------ | --- | ------------ | -------- |
Table11.
FIGURE5. ROCcurve.
F. DETECTIONLATENCY
|     |     |     |     | An important | requirement | of an adaptive | authentication |     |
| --- | --- | --- | --- | ------------ | ----------- | -------------- | -------------- | --- |
the corresponding performance metrics are summarized in system is its ability to rapidly detect malicious activity.
| Table 13. Fig. | 5 shows | the derived Receiver | Operating |             |              |                   |     |             |
| -------------- | ------- | -------------------- | --------- | ----------- | ------------ | ----------------- | --- | ----------- |
|                |         |                      |           | To evaluate | this aspect, | the delay between | the | onset of an |
Characteristic(ROC)curve. attackandthefirsteventexceedingtheblockthresholdτ was
2
|     |     |     |     | measured. | The detection | latency is | defined as | the number |
| --- | --- | --- | --- | --------- | ------------- | ---------- | ---------- | ---------- |
2) RISK-TRUSTCORRELATIONANDATTACK of events required before the risk score crosses the block
| CLASSIFICATIONPERFORMANCE |     |     |     | thresholdτ | .   |     |     |     |
| ------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
2
Fig.6presentsthecorrelationbetweenriskandtrust,andhow Table15recordsthedetectionperformanceoftheproposed
theframeworkusesthetrustscore,alongwiththecomputed framework. Strong contextual signals, such as Attack cam-
thresholdstoclassifyevents. paignsignatures,devicefingerprintmismatches,andsession
| 77870 |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE15. Detectiondelaybyevents. TABLE16. Userfrictionanalysis.
|     |     |     |     |     |     | FIGURE8. | Costvsattackdetectionrecall. |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ---------------------------- | --- | --- | --- |
FIGURE7. Detectiondelaydistribution.
anduserexperience.Thecostmapusedwas:
| context violations, |            | elevate | the aggregated |        | risk score   | above |     |     |     |     |
| ------------------- | ---------- | ------- | -------------- | ------ | ------------ | ----- | --- | --- | --- | --- |
| the block           | threshold. | The     | framework      | showed | an immediate |       |     |     |     |     |
ALLOW:1,STEPUP:5,BLOCK:10
| detection | rate | of 98.4%, | with a | 95th percentile | delay | of  |     |     |     |     |
| --------- | ---- | --------- | ------ | --------------- | ----- | --- | --- | --- | --- | --- |
0events.Theaveragedelay,intermsofthenumberofevents Table 16 captures the user friction metrics, including the
| was 0.0170. | Fig. | 7 represents | the | distribution | of detection |     |     |     |     |     |
| ----------- | ---- | ------------ | --- | ------------ | ------------ | --- | --- | --- | --- | --- |
costdetails.
delaybyeventsduringtheattackcampaigns. The usability impact analysis of the data showed that
|     |     |     |     |     |     | 73% of genuine | attacks | were blocked | by  | the framework. |
| --- | --- | --- | --- | --- | --- | -------------- | ------- | ------------ | --- | -------------- |
G. USERFRICTIONANALYSIS Approximately 15% of the benign users were challenged to
The usability of the proposed ZeTHAA framework was performadditionalauthentication.About5%ofbenignusers
evaluatedthroughuserfrictionanalysis.Userfrictionanalysis wereblockedfromaccessingresources.
aimstoidentifytherateatwhichbenignusersareforcedto Fig. 8 illustrates the trade-off between authentication
performadditionalauthentication.Whilestep-upauthentica- cost and attack detection rate across varying threshold
tionintroducesmoderatefriction,blockingabenignusercan configurations.Theplottedcurvedepictspossibleoperating
significantlydegradetheuserexperience,includingpotential points of the framework when thresholds are varied. Each
servicedenial.
pointrepresentsauniquethresholdconfiguration,illustrating
Thefrictionmetricswerecomputedas: the relationship between authentication cost and detection
|     |     |     |     |     |     | performance. | As expected, | increasing | the strictness | of deci- |
| --- | --- | --- | --- | --- | --- | ------------ | ------------ | ---------- | -------------- | -------- |
BenignStep-UpEvents
Step-UpRate= sionthresholdsleadstohigherdetectionratesattheexpense
TotalBenignEvents
|     |     |     |     |     |     | of increased | user friction. | The selected |     | operating point |
| --- | --- | --- | --- | --- | --- | ------------ | -------------- | ------------ | --- | --------------- |
BenignBlockEvents (marked with x) achieves a favorable balance, delivering
FalseBlockRate=
|     |     |     |     |     |     | strong detection | performance | while maintaining |     | a moderate |
| --- | --- | --- | --- | --- | --- | ---------------- | ----------- | ----------------- | --- | ---------- |
TotalBenignEvents
authenticationcost.
AttackBlockEvents
AttackBlockRate=
TotalAttackEvents
H. ROBUSTNESSANALYSIS
A non-linear cost model was adopted to reflect the Robustness analysis of the proposed framework aimed at
assessinghowthesystemrespondedtoparameterchanges.
| disproportionate |     | impact  | of user-facing | decisions. | Step-up       |     |     |     |     |     |
| ---------------- | --- | ------- | -------------- | ---------- | ------------- | --- | --- | --- | --- | --- |
| authentication   |     | demands | on benign      | users      | were assigned | a   |     |     |     |     |
moderate cost, while blocking a benign user was assigned 1) ABLATIONSTUDY
asignificantlyhighercostduetouserdisruptionanddenial. As the system validates contextual signals to arrive at
Blockinglegitimateusersispenalizedmoreheavilythanstep- a decision, an ablation study was conducted to measure
up authentication, as it directly impacts service availability how the performance changes when the contextual signals
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     | 77871 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| are removed. |     | The study | also | aimed | to confirm |     | that each |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---- | ----- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
contextualsignalcontributestothesystem.
| Table            | 17 records |            | how       | the system | responded |            | to the |     |     |     |     |     |     |     |     |
| ---------------- | ---------- | ---------- | --------- | ---------- | --------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| removal          | of each    | contextual |           | signal.    | F1-score  | and        | Area   |     |     |     |     |     |     |     |     |
| Under Curve(AUC) |            |            | were used | as the     | primary   | comparison |        |     |     |     |     |     |     |     |     |
metrics.Thesystemwasunaffectedbytheremovaloftravel,
timezone,andtemporalanomalies.Theremovalofrepeated
| attacker  | IP resulted | in           | the        | largest variation |      | in the         | metrics, |     |     |     |     |     |     |     |     |
| --------- | ----------- | ------------ | ---------- | ----------------- | ---- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| followed  | by          | Geo anomaly. |            | The session       |      | token          | mismatch |     |     |     |     |     |     |     |     |
| showed    | the next    | highest      | variation, | followed          |      | by fingerprint |          |     |     |     |     |     |     |     |     |
| mismatch. | The         | observations |            | matched           | with | the contextual |          |     |     |     |     |     |     |     |     |
featureimportancecomputedinFig.2.
Afurtherstudywasconductedbyremovinggroupsignals,
inwhichallcontextualsignalsrelatedtoaspecificcontextual
| group were | removed. |     | Table | 18 presents |                  | the observations |       |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----- | ----------- | ---------------- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| from the   | removal  | of  | group | signals.    | The observations |                  | align |     |     |     |     |     |     |     |     |
withresultsfromtheremovalofsingularcontextualsignals, FIGURE9. ROCcomparisonacrossmodels.
withtheattackcampaign-relatedgroupshowingthehighest
impactonF1andAUC,followedbymobility,whichgroups
geo-anomaly-related signals. The session group showed 2) DETECTIONPERFORMANCE
the next highest impact, followed by temporal and device The performance of the proposed framework and baseline
integrity. modelswasevaluatedusingseveralcommonlyusedsecurity
metrics.Allmodelcomparisonswereperformedonatestset
toensurefairandunbiasedevaluation.
2) ATTACKINTENSITYANALYSIS
Table21showstheperformancemetricsobservedcompar-
| The performance |     | of  | the framework | under | increasing |     | attack |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | ------------- | ----- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ingtheZeTHAAframeworkagainstbaselines.Thesimilarity
| intensities    | was | studied    | to understand |     | its response |     | to coordi- |                |     |         |        |        |     |         |     |
| -------------- | --- | ---------- | ------------- | --- | ------------ | --- | ---------- | -------------- | --- | ------- | ------ | ------ | --- | ------- | --- |
|                |     |            |               |     |              |     |            | in performance |     | between | Random | Forest | and | XGBoost | is  |
| nated attacks. |     | This study | exposed       | the | framework    |     | to attack  |                |     |         |        |        |     |         |     |
intensitiesvaryingfrom10%to40%,simulatingcoordinated attributedtothelimitedfeaturespaceandthedominanceof
|                    |     |       |     |          |              |     |          | a few contextual |     | signals, | leading | to both | models | learning |     |
| ------------------ | --- | ----- | --- | -------- | ------------ | --- | -------- | ---------------- | --- | -------- | ------- | ------- | ------ | -------- | --- |
| attack conditions. |     | Table | 19  | presents | the findings |     | from the |                  |     |          |         |         |        |          |     |
identicaldecisionstructures.
study.
|       |          |           |        |              |     |        |         | The ZeTHAA      |     | framework | outperformed |             | other    | classifica- |       |
| ----- | -------- | --------- | ------ | ------------ | --- | ------ | ------- | --------------- | --- | --------- | ------------ | ----------- | -------- | ----------- | ----- |
| The   | proposed | framework |        | demonstrated |     | robust | perfor- |                 |     |           |              |             |          |             |       |
|       |          |           |        |              |     |        |         | tion algorithms |     | across    | most         | performance | metrics. |             | While |
| mance | under    | varying   | attack | intensities. | The | AUC    | value   |                 |     |           |              |             |          |             |       |
remains stable, showing that the framework is robust under Random Forest and XGBoost showed a marginal increase
|     |     |     |     |     |     |     |     | in precision, | ZeTHAA |     | showed | better results |     | recall and | F1- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | --- | ------ | -------------- | --- | ---------- | --- |
attackandcandistinguishbetweenattackandbenignevents,
|     |     |     |     |     |     |     |     | score respectively. |     | The | ZeTHAA | Framework |     | significantly |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------ | --------- | --- | ------------- | --- |
evenastheproportionofattacksincreases.Therecallvalue
|     |     |     |     |     |     |     |     | outperforms | every | other | model | in Recall, | notably | beating |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----- | ----- | ---------- | ------- | ------- | --- |
alsoremainsstabilewithincreasingattackdensity,indicating
|     |     |     |     |     |     |     |     | the Isolation | Forest | by  | over 251%. | As  | the Recall | is higher, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | --- | ---------- | --- | ---------- | ---------- | --- |
thattheattackdetectioncapabilityisconsistent.Theprecision
improves, indicating the system becomes more efficient as the overall F1-Score (the balance of Precision and Recall)
showsamassivejumpof48%to147%overthecomparison.
| attacks | increase. | The | accuracy | shows | slight | degradation | but |     |     |     |     |     |     |     |     |
| ------- | --------- | --- | -------- | ----- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TheLogisticRegressionandHeuristicapproachesperformed
remainsstableoverall.
The results highlight that the proposed framework main- better than Isolation Forest, which offered the lowest
performancemetricsamongalltheapproaches.
tainsstabledetectionperformance,whileadaptingefficiently
Fig.9recordstheROCcurveoftheZeTHAAframework
toincreasingcomplexattackscenarios.
|     |     |     |     |     |     |     |     | compared | to the | baseline | models. | The | proposed | framework |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | ------- | --- | -------- | --------- | --- |
recordsahightruepositiveratecomparedtotheothermodels.
I. COMPARISONWITHBASELINEMODELS
|            |     |               |     |        |          |     |        | The computed      |     | decision | thresholds         | are | highlighted | on     | the   |
| ---------- | --- | ------------- | --- | ------ | -------- | --- | ------ | ----------------- | --- | -------- | ------------------ | --- | ----------- | ------ | ----- |
| To compare | the | effectiveness |     | of the | proposed |     | ZeTHAA |                   |     |          |                    |     |             |        |       |
|            |     |               |     |        |          |     |        | curve, indicating |     | the      | policy’s operating |     | region.     | At the | step- |
framework,itsperformancewascomparedwithmultiplerep- up decision threshold (τ ) indicated by the blue marker, the
1
resentativeauthenticationandanomalydetectionapproaches
|     |     |     |     |     |     |     |     | framework | detects | 83.2% | of  | attack events | and | challenges |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ----- | --- | ------------- | --- | ---------- | --- |
commonlyusedinrisk-basedauthenticationsystems.
|     |     |     |     |     |     |     |     | with step-up | verification, |     | while         | incurring | a     | false positive |       |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | ------------- | --------- | ----- | -------------- | ----- |
|     |     |     |     |     |     |     |     | rate of      | 24.7%.        | The | True Positive | Rate      | (TPR) | and            | False |
1) BASELINEMODELS Positive Rate (FPR) represent aggressive detection, but use
Theselectedbaselinemethodsrepresentdifferentcategories step-upauthenticationanddonotblockusers.Theredmarker
ofauthenticationmodels.Table20liststhebaselinemodels indicates the operating point corresponding to the blocking
against which the proposed framework is assessed for threshold (τ ), achieving 73.2% attack detection with a
2
performance. 7.24% false positive rate, showcasing strict security while
| 77872 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE17. Singlesignalablationresults.
TABLE18. Groupsignalablationresults.
TABLE19. Attackintensityanalysis.
TABLE20. Selectedbaselinesforcomparison.
TABLE21. Performancecomparisonbetweenbaselines.
minimizinguserdisruption.Theshadedportionbetweenthe showed a lower range of step-up challenges and block
policy thresholds represents the adaptive decision region of decisions, indicating a conservative approach to security.
the framework. The sharp rise of the proposed framework’s Unliketraditionalclassifiersthatoperateatasinglethreshold,
ROC curve near the origin indicates early-stage discrimina- the ZeTHAA framework defines a controllable decision
tioncapability,whichhelpsinminimizinguserfrictionwhile band,enablingresponsesbasedonrisklevelsandimproving
maintaininghighdetectionrates. detection performance. The ZeTHAA framework produces
Fig. 10 records the policy decisions taken by the models. a well-spread risk distribution, enabling effective utilization
The ZeTHAA framework balances security and usability of allow, step-up, and block regions. In contrast, baseline
compared to the baseline models. Although it showed a models exhibit clustered score distributions. This supports
lower‘‘ALLOW’’stateforevents,ithadahigherproportion RQ3 and H3, demonstrating improved alignment between
of step-up challenges than the baselines. This shows that risk scores and decision policies. With a more effective use
events with higher risk scores were automatically asked of the intermediate step-up region, the framework further
to perform additional verification. The baseline models supportsRQ2andH2.
VOLUME14,2026 77873

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
|     |     |     |     |     |     |     | The proposed          |               | framework     | achieves         | the            | lowest     | cost per    |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | ------------- | ------------- | ---------------- | -------------- | ---------- | ----------- |
|     |     |     |     |     |     |     | detected              | attack        | among         | all models.      | This           | indicates  | that        |
|     |     |     |     |     |     |     | although              | the framework |               | incurs higher    | overall        | costs,     | it uses     |
|     |     |     |     |     |     |     | authentication        | resources     |               | more efficiently |                | to detect  | attacks.    |
|     |     |     |     |     |     |     | Baseline              | models        | exhibit       | a lower          | average        | cost but   | a higher    |
|     |     |     |     |     |     |     | cost per              | detected      | attack,       | reflecting       | inefficient    |            | security    |
|     |     |     |     |     |     |     | performance.          | The           | proposed      | ZeTHAA           | framework      |            | achieves    |
|     |     |     |     |     |     |     | a higher              | detection     | efficiency,   | indicating       |                | a more     | effective   |
|     |     |     |     |     |     |     | use of authentication |               | resources.    |                  | The controlled |            | increase in |
|     |     |     |     |     |     |     | intervention,         | with          | significantly | improved         |                | detection, | further     |
demonstratessupportofRQ1andH1.
J. COMPARISONWITHEXISTINGFRAMEWORKS
WiththeZeTHAAframeworkexhibitingbetterperformance
| FIGURE10. | Proportionofdecisionsperpolicyregion. |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
metrics,operationalefficiency,andcosteffectivenessagainst
baselinemodels,wefurthercompareZeTHAAwithmethod-
3) OPERATIONALEFFICIENCYANDCOSTPERATTACK ologies presented in the existing literature. Comparison
The operational efficiency of the proposed framework was studieswereperformedwithDasuetal.[16]andMatiushin
|     |     |     |     |     |     |     | and Korkhov | [19]. | Dasu | et al. | use a | weighted | heuristic |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ---- | ------ | ----- | -------- | --------- |
verifiedagainstthebaselinemodels.
Table 22 reports the operational efficiency metrics for the approach to derive risk scores and make decisions. On the
ZeTHAA framework compared with the baseline models. other hand, Matiushin et al. use an ML-based approach to
The proposed ZeTHAA framework records the highest identify anomalies in user behavior and classify requests as
step-upandblockratesamongthemodels,exceeding47.9% an attack or benign. As representatives of two widely used
|           |               |     |          |     |             |        | approaches | to risk | classification |     | - heuristic | and | ML-based, |
| --------- | ------------- | --- | -------- | --- | ----------- | ------ | ---------- | ------- | -------------- | --- | ----------- | --- | --------- |
| and 59.9% | respectively. |     | However, | in  | the context | of the |            |         |                |     |             |     |           |
higher recall value, indicating higher attack detection, the theseworkswerechosenforthecomparisonstudy.
higherstep-upandblockratescanbecorrelatedtoincreased
intervention.Thebaselinemodelsincurlowercostsbecause 1) DASUETAL
they fail to identify and act on a large proportion of Dasu et al. utilize five risk signals - travel risk(r ), location
1
attack events. The proposed framework maintains a higher risk(r 2 ), browser risk(r 3 ), device risk(r 4 ), and password
Efficiency(+20%to+65%)butincursahigherFalseBlock risk(r ). The risk score for each signal is bounded as {x ∈
5
Rate than Random Forest and XGBoost, suggesting a more R|0 ≤ x ≤ 5}. Each risk signal is assigned a static weight
aggressiveyethighlyeffectivedetectionposture. thatrepresentsitsrelativeimportanceinheuristicscoring.
| The analysis | used     | a non-linear |           | cost | model,   | as adopted |                  |     |           |     |     |     |     |
| ------------ | -------- | ------------ | --------- | ---- | -------- | ---------- | ---------------- | --- | --------- | --- | --- | --- | --- |
|              |          |              |           |      |          |            | • TravelRisk(w   |     | 1 )-80/33 |     |     |     |     |
| earlier in   | the user | friction     | analysis. | The  | cost map | used was   |                  |     |           |     |     |     |     |
|              |          |              |           |      |          |            | • LocationRisk(w |     | )-40/33   |     |     |     |     |
|              | 1,Stepup | 5,Block      |           |      |          |            |                  |     | 2         |     |     |     |     |
{Allow : : : 10}, indicating the cost of BrowserRisk(w )-20/33
|     |     |     |     |     |     |     | •   |     | 3   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
askingabenignuserforastep-upchallengeorblockinghim
|                      |     |     |     |     |     |     | • DeviceRisk(w   |     | 4 )-20/33 |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | --- | --- | --- | --- |
| fromusingtheservice. |     |     |     |     |     |     | • PasswordRisk(w |     | )-5/33    |     |     |     |     |
5
| Detection | efficiency | is  | defined | as the | ratio of | the Attack |        |         |          |             |         |          |     |
| --------- | ---------- | --- | ------- | ------ | -------- | ---------- | ------ | ------- | -------- | ----------- | ------- | -------- | --- |
|           |            |     |         |        |          |            | Travel | risk is | assigned | the highest | weight, | followed | by  |
detectionrate(Recall)totheAveragecostofauthentication.
location,browser,anddevicerisk,withpasswordriskbeing
assignedtheleastweight.Thetotalriskisthencomputedas:
Attackdetectionrate(Recall)
Efficiency=
Averageauthenticationcost TotalRisk=(w 1 r 1 +w 2 r 2 +w 3 r 3 +w 4 r 4 +w 5 r 5 )
| The models | were | further | compared |     | in terms | of their |     |     |     |     |     |     |     |
| ---------- | ---- | ------- | -------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Theweightsareassignedstatically,andtheframeworkdoes
averagecost,costperattackdetected,andhigherefficiency. not propose an approach to recalibrate them or the binary
| We define | the cost | per detected |     | attack | as the ratio | of the |     |     |     |     |     |     |     |
| --------- | -------- | ------------ | --- | ------ | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
decisionthreshold.Riskscoresthatexceedthethresholdare
averageauthenticationcosttotheattackdetectionrate.
subjectedtovalidation.However,theriskanalysisconsiders
|     |     |     |     |     |     |     | only the | last 10 | login attempts, | thereby | excluding |     | historical |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------------- | ------- | --------- | --- | ---------- |
Averageauthenticationcost
Costperattackdetected=
patterns.
Attackdetectionrate(Recall)
|     |     |     |     |     |     |     | To compare |     | the ZeTHAA | framework |     | with Dasu | et al., |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --------- | --- | --------- | ------- |
Althoughtheaveragecostpertransactionishigher,the‘‘Cost wefirstmaptheriskstotheproposedrisksignals.Table23
perattackdetected’’issignificantlylower,indicatinga17.3% presents the mapping of risks from Dasu et al. to ZeTHAA
to39.6%reductionincostcomparedwiththeothermodels. framework’srisksignals.
However, this increased cost is offset by improved attack In the absence of separate browser or device features,
detection performance. The cost vs. recall and detection fingerprintmismatchisusedasaproxyforboth.Thebrowser
efficiencyobservationssupportRQ1andH1,respectively. signalisapproximatedusingadevicefingerprintmismatch,
| 77874 |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE22. Operationalefficiencyandcost/attackdetected.
TABLE23. Risktosignalmapping. TABLE24. Performancemetricscomparison.
byMLE-RBA.Dasuetal.presentedtheloweststep-uprate,
|                |            |     |                  |     |                  |     | indicating      | that a | higher | number  | of requests  |       | were classified |
| -------------- | ---------- | --- | ---------------- | --- | ---------------- | --- | --------------- | ------ | ------ | ------- | ------------ | ----- | --------------- |
|                |            |     |                  |     |                  |     | as benign.      | ZeTHAA |        | had the | highest      | block | rate among      |
| which captures | deviations |     | in client-device |     | characteristics. |     |                 |        |        |         |              |       |                 |
|                |            |     |                  |     |                  |     | the frameworks, |        | while  | MLE-RBA | demonstrated |       | the lowest      |
While the dataset does not explicitly distinguish between falseblockrates,followedbyZeTHAA.However,ZeTHAA
browser and device features, fingerprint-based signals pro- exhibited the highest efficiency figures while recording the
videareasonableapproximationofboth. lowest cost per correctly detected attack. The proposed
|     |     |     |     |     |     |     | framework | achieves | higher | recall | at  | comparable | cost levels, |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | ------ | --- | ---------- | ------------ |
2) MATIUSHINETAL demonstrating a more favorable security–usability balance
TheMachineLearning-EmpoweredRisk-BasedAuthentica- andsupportingRQ1andH1.
| tion (MLE-RBA) |     | framework | proposed | by  | Matiushin | et al., |     |     |     |     |     |     |     |
| -------------- | --- | --------- | -------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
usesamulti-stageMLpipelinetoidentifyirregularitiesand b: SECURITYPOSTUREANDATTACKDETECTION
makedynamicdecisions.ItcombinestwounsupervisedML Table 26 lists the combined confusion matrix of the three
| models: Local | Outlier | Factor | (LOF) | and Isolation |     | Forest to | frameworks. |     |     |     |     |     |     |
| ------------- | ------- | ------ | ----- | ------------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
capturebothlocalandglobaldeviationsinauser’sbehavior, The Proposed ZeTHAA Framework blocks significantly
generatinganaggregateanomalyscore.Thisanomalyscoreis
|     |     |     |     |     |     |     | more attacks | (7,963) | than | both | the | heuristic | (Dasu et al.) |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ---- | ---- | --- | --------- | ------------- |
fedintoaLightGBMclassifiertogenerateacontinuousrisk (3,630) and MLE-RBA (3,695). ZeTHAA is much more
score for every login attempt. Instead of relying on a static, aggressive with ‘‘Step-Up’’ challenges for benign users
| predefined | threshold, | MLE-RBA | dynamically |     | calculates | an  |              |      |        |        |       |             |          |
| ---------- | ---------- | ------- | ----------- | --- | ---------- | --- | ------------ | ---- | ------ | ------ | ----- | ----------- | -------- |
|            |            |         |             |     |            |     | (4,184) than | Dasu | et al. | (240), | which | corresponds | with the |
optimal threshold by evaluating the Receiver Operating higher recall noted in Table 24. ZeTHAA also allows the
| Characteristic | (ROC) | curve. | If a login’s | risk | score | exceeds |     |     |     |     |     |     |     |
| -------------- | ----- | ------ | ------------ | ---- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
fewestattacks(1,826)throughthesystem,whereastheothers
thisthreshold,thesystemclassifiesitasanattackandtriggers allow over 5,000. MLE-RBA has the lowest FPR (1.95%),
secondaryauthentication. indicating it rarely interrupts legitimate users. However,
asobservedfromtheRecallvalue,itmisses66%ofattacks
3) RESULTSANDOBSERVATIONS toachievethis.ZeTHAAblocked5%morebenignusersthan
Allthreeframeworksweresubjectedtothesamedatasetand
MLE-RBA,butinexchange,caughtnearly40%moreattacks.
| cost mapping.      | The | comparisons | were | conducted |     | under the |                   |          |     |            |     |           |             |
| ------------------ | --- | ----------- | ---- | --------- | --- | --------- | ----------------- | -------- | --- | ---------- | --- | --------- | ----------- |
| broadcategoriesof: |     |             |      |           |     |           | c: ERRORREDUCTION |          |     |            |     |           |             |
|                    |     |             |      |           |     |           | We further        | compared | the | frameworks |     | for their | Equal Error |
a: PERFORMANCEANALYSIS Rate(EER).EERrepresentsthepointonaROCcurve,where
Table 24 records the performance metrics recorded by the theFalsePositiveRate(benignusersincorrectlyblocked)and
threeframeworks.TheproposedZeTHAAframeworkexhib- False Rejection Rate are equal. A lower EER represents a
ited demonstrably higher performance indicators compared betterbalancebetweenfalseacceptsandrejects,showcasing
toDasuetal.andMLE-RBA.WhileMLE-RBApresenteda theabilitytodetectattackswhilemakingfewermistakeson
slightlyhigherprecision,indicatingaccuracyintruepositive identifyinglegitimateusers.
prediction,ZeTHAAwasclosebehindandfaredmuchbetter Fig. 11 presents the ROC curves and corresponding
thanDasuetal.ZeTHAApresentedahigherrecall,indicating EER points for the ZeTHAA, heuristic-based Dasu et al.,
anedgeincorrectlyclassifyingrequests. and ML-based MLE-RBA frameworks. The EER point
Table25presentstheoperationalefficiencyfiguresforthe in the plot represents the balanced operating point at
threeframeworks.TheZeTHAAframeworkpresentsahigher which false positives equal the missed attacks. The pro-
step-up rate due to an active engagement policy, followed posed framework consistently achieves a higher TPR at
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     | 77875 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE25. Operationalefficiencycomparison.
TABLE26. Combinedconfusionmatrix.
|     |     |     |     |     |     |     | entropy | and Bayesian-driven |     | parameterization |          |           | of attribute |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------- | --- | ---------------- | -------- | --------- | ------------ |
|     |     |     |     |     |     |     | weights | and penalties       |     | provides         | a robust | mechanism | for          |
cold-startinitializationandcontinuousrecalibration,address-
|     |     |     |     |     |     |     | ing one   | of the         | key limitations |          | in existing     | systems.   | The          |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --------------- | -------- | --------------- | ---------- | ------------ |
|     |     |     |     |     |     |     | framework | further        | establishes     |          | a clear         | separation | between      |
|     |     |     |     |     |     |     | intrinsic | authentication |                 | strength | and operational |            | reliability, |
enablingconsistentmappingtoNISTassurancelevels.With
evidence-drivendecisionthresholds,theframeworkcancap-
tureadversarialbehaviors,suchascredentialstuffing,while
|           |                        |     |     |     |     |     | tolerating         | benign     | user error. | The      | paper           | highlights | how the     |
| --------- | ---------------------- | --- | --- | --- | --- | --- | ------------------ | ---------- | ----------- | -------- | --------------- | ---------- | ----------- |
|           |                        |     |     |     |     |     | proposed           | system     | extends     | security | and risk        | assessment | well        |
|           |                        |     |     |     |     |     | into the           | resource   | access      | phase,   | a functionality |            | not covered |
|           |                        |     |     |     |     |     | under conventional |            | AA          | systems. | The proposed    |            | multiphase  |
|           |                        |     |     |     |     |     | hybrid             | evaluation | strategy    | ensures  | that            | the        | system can  |
| FIGURE11. | ROCcurvewithEERpoints. |     |     |     |     |     |                    |            |             |          |                 |            |             |
validateriskandtrustevenintheabsenceofhistoricalcontext
|         |                 |          |     |                |     |             | or access     | patterns. | The           | efficacy | of the    | proposed | system     |
| ------- | --------------- | -------- | --- | -------------- | --- | ----------- | ------------- | --------- | ------------- | -------- | --------- | -------- | ---------- |
|         |                 |          |     |                |     |             | was validated | on        | a large-scale |          | synthetic | dataset  | simulating |
| a lower | FPR, indicating | superior |     | discrimination |     | capability. |               |           |               |          |           |          |            |
The proposed model achieves the lowest EER (0.1981), real-world attack conditions. With novel security checks
significantly outperforming both the heuristic (0.2992) and extending to newer attributes,e.g., application integrity and
|          |            |           |            |     |     |         | dynamic | build | secrets, | and device | posture | evaluation, | the |
| -------- | ---------- | --------- | ---------- | --- | --- | ------- | ------- | ----- | -------- | ---------- | ------- | ----------- | --- |
| ML-based | approaches | (0.2729), | supporting |     | RQ2 | and H2, |         |       |          |            |         |             |     |
which hypothesize improved detection performance and proposed system minimizes user friction and ensures the
|         |                   |        |     |          |               |     | user obtains | only | the minimum |     | degree | of trust | required to |
| ------- | ----------------- | ------ | --- | -------- | ------------- | --- | ------------ | ---- | ----------- | --- | ------ | -------- | ----------- |
| reduced | error trade-offs. | ZeTHAA |     | reported | approximately |     |              |      |             |     |        |          |             |
33%reductioninerrorcomparedtoDasuetal. accesstheintendedresources.TheproposedZeTHAAframe-
The observations show that the proposed framework work provides a coherent, mathematically grounded, and
practicallyimplementableapproachtoZT-basedcontinuous
| provides | a more | favorable | balance | between | false | positives |     |     |     |     |     |     |     |
| -------- | ------ | --------- | ------- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
and false negatives, improving both security and usability, authenticationandauthorization.
| while achieving      |     | higher performance, |     | greater | efficiency, | and |              |     |     |     |     |     |     |
| -------------------- | --- | ------------------- | --- | ------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| loweroperatingcosts. |     |                     |     |         |             |     | DECLARATIONS |     |     |     |     |     |     |
CONFLICTSOFINTEREST
| VIII. CONCLUSION  |                |            |     |              |        |             | Theauthorsdeclarenoconflictsofinterest. |     |     |     |     |     |     |
| ----------------- | -------------- | ---------- | --- | ------------ | ------ | ----------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
| Adaptive          | authentication | represents |     | an evolution |        | in security |                                         |     |     |     |     |     |     |
| while maintaining |                | usability  | as  | a central    | design | factor.     | REFERENCES                              |     |     |     |     |     |     |
This paper presents ZeTHAA, a novel, unified, and for- [1] C.JacommeandS.Kremer,‘‘Anextensiveformalanalysisofmulti-factor
mally grounded Zero-Trust-based Adaptive Authentication authentication protocols,’’ ACM Trans. Privacy Secur., vol. 24, no. 2,
pp.1–34,Jan.2021,doi:10.1145/3440712.
| and continuous |     | authorization | framework. |     | By  | integrating |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | ---------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
[2] S.S.U.Hasan,A.Ghani,A.Daud,H.Akbar,andM.F.Khan,‘‘Areviewon
authentication strength, contextual attributes, behavioral secureauthenticationmechanismsformobilesecurity,’’Sensors,vol.25,
no.3,p.700,Jan.2025,doi:10.3390/s25030700.
evidence,andretrydynamicsintoatime-dependenttrust–risk
[3] A.Agarwal,S.B.Verma,andB.K.Gupta,‘‘Areviewofcloudsecurity
| model, | the proposed | approach |     | moves | beyond | heuristic |     |     |     |     |     |     |     |
| ------ | ------------ | -------- | --- | ----- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
issuesandchallenges,’’ADCAIJ,Adv.Distrib.Comput.Artif.Intell.J.,
| scoring | systems. | A central | contribution |     | is the | introduction |     |     |     |     |     |     |     |
| ------- | -------- | --------- | ------------ | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
vol.12,Dec.2023,Art.no.e31459,doi:10.14201/adcaij.31459.
of a global admissibility predicate, which distinguishes [4] Y. Chen, Y. Yu, and L. Zhai, ‘‘Infinitygauntlet: Brute-force attack on
|                 |     |                 |     |      |               |      | smartphone | fingerprint | authentication,’’ |     | in Proc. | 32nd | USENIX Conf. |
| --------------- | --- | --------------- | --- | ---- | ------------- | ---- | ---------- | ----------- | ----------------- | --- | -------- | ---- | ------------ |
| non-compensable |     | hard violations |     | from | probabilistic | soft |            |             |                   |     |          |      |              |
Secur.Symp.,2023,pp.2027–2041.[Online].Available:https://dl.acm.
signals, thereby enabling clear enforcement decisions. The org/doi/10.5555/3620237.3620351
| 77876 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
[5] Q. Wang and D. Wang, ‘‘Understanding failures in security proofs of [24] A. A. Megahed, M. F. Arnous, Y. Elmoataz, A. Moussa, S. Haitham,
multi-factorauthenticationformobiledevices,’’IEEETrans.Inf.Forensics andM.Hany,‘‘Enhancedsecuritythroughintelligentrisk-basedauthen-
Security,vol.18,pp.597–612,2023,doi:10.1109/TIFS.2022.3227753. tication: Leveraging big data and machine learning for real-time threat
[6] D. Wang, X. Zhang, Z. Zhang, and P. Wang, ‘‘Understanding security mitigation,’’inProc.6thNovelIntell.Lead.Emerg.Sci.Conf.(NILES),
failures of multi-factor authentication schemes for multi-server envi- Oct.2024,pp.246–249.
ronments,’’ Comput. Secur., vol. 88, Jan. 2020, Art.no.101619, doi: [25] M. Al-Zubaidie, Z. Zhang, and J. Zhang, ‘‘RAMHU: A new robust
10.1016/j.cose.2019.101619.
lightweightschemeformutualusersauthenticationinhealthcareapplica-
[7] M. Syahreen, N. Hafizah, N. Maarop, and M. Maslinan, ‘‘A sys- tions,’’Secur.Commun.Netw.,vol.2019,pp.1–26,Mar.2019.[Online].
tematic review on multi-factor authentication framework,’’ Int. J. Available:https://onlinelibrary.wiley.com/doi/abs/10.1155/2019/3263902
Adv. Comput. Sci. Appl., vol. 15, no. 5, pp. 1043–1050, 2024, doi: [26] A.Acar,H.Aksu,A.S.Uluagac,andK.Akkaya,‘‘Ausableandrobust
10.14569/ijacsa.2024.01505105. continuous authentication framework using wearables,’’ IEEE Trans.
[8] E. B. Blancaflor, J. O. Duldulao, J. V. E. Espeño, G. S. M. Patag, MobileComput.,vol.20,no.6,pp.2140–2153,Jun.2021.
M.T.Menor,andG.L.Intal,‘‘Advancedphishingtechniques:Analyzing [27] A. Buriro, S. Gupta, A. Yautsiukhin, and B. Crispo, ‘‘Risk-driven
| adversary-in-the-middle |     |     | and browser-in-the-browser |     |     | attacks | in modern |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | -------------------------- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
behavioralbiometric-basedone-shot-cum-continuoususerauthentication
cybersecurity,’’Cybern.Inf.Technol.,vol.25,no.1,pp.55–77,Mar.2025,
scheme,’’J.SignalProcess.Syst.,vol.93,no.9,pp.989–1006,Sep.2021,
| doi:10.2478/cait-2025-0004. |     |     |     |     |     |     |     | doi:10.1007/s11265-021-01654-2. |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[9] A.F.BaigandS.Eskeland,‘‘Security,privacy,andusabilityincontinuous [28] Z. Shen, S. Li, X. Zhao, and J. Zou, ‘‘MMAuth: A continuous
authentication:Asurvey,’’Sensors,vol.21,no.17,p.5967,Sep.2021,doi: authentication framework on smartphones using multiple modalities,’’
10.3390/s21175967. IEEETrans.Inf.ForensicsSecurity,vol.17,pp.1450–1465,2022,doi:
[10] F.Al-Husari,O.Nakov,andP.Nakov,‘‘Multi-factorauthenticationfatigue: 10.1109/TIFS.2022.3160361.
Agrowingconcerninuserexperienceandsecurity,’’inProc.60thInt.Sci.
|     |     |     |     |     |     |     |     | [29] Y. Liang, | S.  | Samtani, B. | Guo, and | Z. Yu, | ‘‘Behavioral | biometrics | for |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | -------- | ------ | ------------ | ---------- | --- |
Conf.Inf.,Commun.EnergySyst.Technol.(ICEST),Jun.2025,pp.1–4,
|     |     |     |     |     |     |     |     | continuous | authentication |     | in the | Internet-of-Things |     | era: An artificial |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ------ | ------------------ | --- | ------------------ | --- |
doi:10.1109/ICEST66328.2025.11098219. intelligence perspective,’’ IEEE Internet Things J., vol. 7, no. 9,
[11] S. Wiefling, M. Dürmuth, and L. Lo Iacono, ‘‘More than just good pp.9128–9143,Sep.2020,doi:10.1109/JIOT.2020.3004077.
passwords?Astudyonusabilityandsecurityperceptionsofrisk-based [30] M.Mekni,E.O.Ogunwobi,andS.C.Russell,‘‘Context-adaptivegait
authentication,’’inProc.Annu.Comput.Secur.Appl.Conf.,Dec.2020, biometrics for real-time continuous authentication,’’ in Proc. Int. Conf.
pp.203–218,doi:10.1145/3427228.3427243.
Adv.Mach.Learn.DataSci.(AMLDS),Jul.2025,pp.799–807.
| [12] A. Hassan,   | B.  | Nuseibeh, | and L.    | Pasquale, | ‘‘Engineering |         | adaptive |                                                              |             |            |     |                  |                |     |       |
| ----------------- | --- | --------- | --------- | --------- | ------------- | ------- | -------- | ------------------------------------------------------------ | ----------- | ---------- | --- | ---------------- | -------------- | --- | ----- |
|                   |     |           |           |           |               |         |          | [31] S.W.Shah,N.F.Syed,A.Shaghaghi,A.Anwar,Z.Baig,andR.Doss, |             |            |     |                  |                |     |       |
| authentication,’’ |     | in Proc.  | IEEE Int. | Conf.     | Autonomic     | Comput. | Self-    |                                                              |             |            |     |                  |                |     |       |
|                   |     |           |           |           |               |         |          | ‘‘LCDA:                                                      | Lightweight | continuous |     | device-to-device | authentication |     | for a |
OrganizingSyst.Companion(ACSOS-C),Sep.2021,pp.275–280,doi:
|     |     |     |     |     |     |     |     | zero | trust architecture | (ZTA),’’ | Comput. | Secur., | vol. | 108, Sep. | 2021, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------ | -------- | ------- | ------- | ---- | --------- | ----- |
10.1109/ACSOS-C52956.2021.00068.
Art.no.102351,doi:10.1016/j.cose.2021.102351.
| [13] S. Rose, | O. Borchert, |     | S. Mitchell, | and | S. Connelly, | ‘‘Zero | trust |                                                                   |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | ------------ | --- | ------------ | ------ | ----- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|               |              |     |              |     |              |        |       | [32] G.Dahia,L.Jesus,andM.PamplonaSegundo,‘‘Continuousauthentica- |     |     |     |     |     |     |     |
architecture,’’NationalInstituteofStandardsandTechnology,Tech.Rep., tionusingbiometrics:Anadvancedreview,’’WIREsDataMiningKnowl.
2020.[Online].Available:https://doi.org/10.6028/NIST.SP.800-207
Discovery,vol.10,no.4,p.1365,Jul.2020,doi:10.1002/widm.1365.
[14] D.Temoshok,D.Proud-Madruga,Y.-Y.Choong,R.Galluzzo,S.Gupta,
|     |     |     |     |     |     |     |     | [33] A. F. | Baig, S. | Eskeland, | and B. Yang, | ‘‘Privacy-preserving |     | continuous |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --------- | ------------ | -------------------- | --- | ---------- | --- |
C.LaSalle,N.Lefkovitz,andA.Regenscheid,‘‘Digitalidentityguide-
|     |     |     |     |     |     |     |     | authentication |     | using behavioral | biometrics,’’ |     | Int. J. Inf. | Secur., vol. | 22, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | ------------- | --- | ------------ | ------------ | --- |
lines,’’NationalInstituteofStandardsandTechnology,Gaithersburg,MD,
no.6,pp.1833–1847,Dec.2023,doi:10.1007/s10207-023-00721-y.
USA,Tech.Rep.800-63-4,2025,doi:10.6028/NIST.SP.800-63-4.
|     |     |     |     |     |     |     |     | [34] S. | Ayeswarya | and | K. J. Singh, | ‘‘A | comprehensive |     | review |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ------------ | --- | ------------- | --- | ------ |
[15] (2021).WebAuthentication:AnApiforAccessingPublicKeyCredentials
|     |     |     |     |     |     |     |     | on  | secure | biometric-based | continuous |     | authentication | and | user |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------------- | ---------- | --- | -------------- | --- | ---- |
Level2.[Online].Available:https://www.w3.org/TR/webauthn-2/
|     |     |     |     |     |     |     |     | profiling,’’ | IEEE | Access, | vol. | 12, pp.82996–83021, |     | 2024, | doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ------- | ---- | ------------------- | --- | ----- | ---- |
[16] L.S.Dasu,M.Dhamija,G.Dishitha,A.Vivekanandan,andV.Sarasvathi,
10.1109/ACCESS.2024.3411783.
| ‘‘Defending | against | identity | threats | using | risk-based | authentication,’’ |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | -------- | ------- | ----- | ---------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Cybern. Inf. Technol., vol. 23, no. 2, pp.105–123, Jun. 2023, doi: [35] S.AmbolandS.Rashad,‘‘Continuousauthenticationofsmartphoneusers
usingmachinelearning,’’inProc.11thIEEEAnnu.UbiquitousComput.,
10.2478/cait-2023-0016.
Electron.MobileCommun.Conf.(UEMCON),Oct.2020,pp.0056–0062,
| [17] C. Picard | and | S. Pierre, | ‘‘RLAuth: |     | A risk-based | authentication |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | --------- | --- | ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
doi:10.1109/UEMCON51285.2020.9298040.
| system | using | reinforcement | learning,’’ |     | IEEE | Access, | vol. 11, |         |        |              |     |            |              |     |        |
| ------ | ----- | ------------- | ----------- | --- | ---- | ------- | -------- | ------- | ------ | ------------ | --- | ---------- | ------------ | --- | ------ |
|        |       |               |             |     |      |         |          | [36] S. | Hasan, | I. Amundson, | and | D. Hardin, | ‘‘Zero-trust |     | design |
pp.61129–61143,2023,doi:10.1109/ACCESS.2023.3286376.
|                |              |     |              |     |               |              |     | and      | assurance | patterns  | for cyber–physical   |     | systems,’’ | J.         | Syst. |
| -------------- | ------------ | --- | ------------ | --- | ------------- | ------------ | --- | -------- | --------- | --------- | -------------------- | --- | ---------- | ---------- | ----- |
| [18] V. Unsel, | S. Wiefling, |     | N. Gruschka, | and | L. Lo Iacono, | ‘‘Risk-based |     |          |           |           |                      |     |            |            |       |
|                |              |     |              |     |               |              |     | Archit., | vol.      | 155, Oct. | 2024, Art.no.103261. |     | [Online].  | Available: |       |
authentication for OpenStack: A fully functional implementation and https://www.sciencedirect.com/science/article/pii/S138376212400198X
guidingexample,’’inProc.13thACMConf.DataAppl.Secur.Privacy,
Apr.2023,pp.237–243,doi:10.1145/3577923.3583634. [37] P. Phiayura and S. Teerakanok, ‘‘A comprehensive framework
|                   |     |     |          |            |     |         |           | for | migrating | to zero | trust architecture,’’ |     | IEEE | Access, vol. | 11, |
| ----------------- | --- | --- | -------- | ---------- | --- | ------- | --------- | --- | --------- | ------- | --------------------- | --- | ---- | ------------ | --- |
| [19] I. Matiushin | and | V.  | Korkhov, | ‘‘MLE-RBA: | A   | machine | learning- |     |           |         |                       |     |      |              |     |
pp.19487–19511,2023.
empoweredrisk-basedauthenticationalgorithm,’’inProc.Comput.Sci.
|             |            |     |                   |     |      |                    |     | [38] Z. Adahman, |     | A. W. Malik, | and Z. | Anwar, | ‘‘An analysis | of zero-trust |     |
| ----------- | ---------- | --- | ----------------- | --- | ---- | ------------------ | --- | ---------------- | --- | ------------ | ------ | ------ | ------------- | ------------- | --- |
| Appl.-ICCSA | Workshops, |     | 2025, pp.325–339, |     | doi: | 10.1007/978-3-031- |     |                  |     |              |        |        |               |               |     |
architectureanditscost-effectivenessfororganizationalsecurity,’’Com-
97648-3_22.
|                |          |          |          |     |        |            |         | put. | Secur., vol. | 122, Nov. | 2022, | Art.no.102911. | [Online]. | Available: |     |
| -------------- | -------- | -------- | -------- | --- | ------ | ---------- | ------- | ---- | ------------ | --------- | ----- | -------------- | --------- | ---------- | --- |
| [20] Y. Zhang, | F. Wang, | J. Zeng, | L. Chen, | X.  | Huang, | Z. Li, and | K. Xue, |      |              |           |       |                |           |            |     |
‘‘Userbehavior-baseddynamicauthenticationdesignforenhancedidentity https://www.sciencedirect.com/science/article/pii/S0167404822003042
security,’’ in Proc. IEEE Int. Conf. Commun., Jun. 2025, pp.1–6, doi: [39] C. Liu, R. Tan, Y. Wu, Y. Feng, Z. Jin, F. Zhang, Y. Liu, and Q. Liu,
10.1109/ICC52391.2025.11161955. ‘‘Dissectingzerotrust:ResearchlandscapeanditsimplementationinIoT,’’
Cybersecurity,vol.7,no.1,p.20,May2024,doi:10.1186/s42400-024-
| [21] M. Papaioannou, |     | G. Zachos, | G.  | Mantas, | and J. Rodriguez, |     | ‘‘Novelty |     |     |     |     |     |     |     |     |
| -------------------- | --- | ---------- | --- | ------- | ----------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
00212-0.
| detection | for risk-based |         | user authentication |      | on mobile | devices,’’  | in   |                                                                        |     |     |     |     |     |     |     |
| --------- | -------------- | ------- | ------------------- | ---- | --------- | ----------- | ---- | ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |                |         |                     |      |           |             |      | [40] W.Yeoh,M.Liu,M.Shore,andF.Jiang,‘‘Zerotrustcybersecurity:Critical |     |     |     |     |     |     |     |
| Proc.     | IEEE Global    | Commun. | Conf.,              | Dec. | 2022,     | pp.837–842, | doi: |                                                                        |     |     |     |     |     |     |     |
10.1109/GLOBECOM48099.2022.10000843. successfactorsandamaturityassessmentframework,’’Comput.Secur.,
[22] Q. I. M. Hussain and V. Kale, ‘‘Risk-based adaptive authentication in vol.133,Oct.2023,Art.no.103412,doi:10.1016/j.cose.2023.103412.
mobile network system using dynamic elliptic curve digital signature [41] E.W.Tomlinson,W.D.Abrha,S.D.Kim,andS.A.Ortega,‘‘Cyber-
algorithm,’’ Concurrency Comput., Pract. Exper., vol. 37, nos. 21–22, securityaccesscontrol:Frameworkanalysisinahealthcareinstitution,’’
p.70208,Sep.2025.[Online].Available:https://onlinelibrary.wiley.com/ J. Cybersecurity Privacy, vol. 4, no. 3, pp.762–776, Sep. 2024, doi:
| doi/abs/10.1002/cpe.70208 |     |     |     |     |     |     |     | 10.3390/jcp4030035. |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
[23] M. Papaioannou, G. Mantas, and J. Rodriguez, ‘‘Risk-based user [42] Y.Kim,S.-G.Sohn,K.T.Kim,H.S.Jeon,S.-M.Lee,Y.Lee,andJ.Kim,
authenticationformobilepassengerIDdevicesforlandandseaborder ‘‘Exploringeffectivezerotrustarchitecturefordefensecybersecurity:A
control,’’inProc.IEEEInt.Medit.Conf.Commun.Netw.(MeditCom), study,’’ KSII Trans. Internet Inf. Syst., vol. 18, no. 9, pp.2665–2691,
Sep.2021,pp.180–185,doi:10.1109/MEDITCOM49071.2021.9647603. Sep.2024,doi:10.3837/tiis.2024.09.011.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 77877 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
[43] B. Hale, D. L. Van Bossuyt, N. Papakonstantinou, and B. O’Halloran, [57] National Institute of Standards and Technology. (2012). Guide for
‘‘Azero-trustmethodologyforsecurityofcomplexsystemswithmachine Conducting Risk Assessments. [Online]. Available: https://nvlpubs.nist.
learning components,’’ in Proc. 41st Comput. Inf. Eng. Conf. (CIE), gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf
Aug.2021,p.002,doi:10.1115/detc2021-70442. [58] National Institute of Standards and Technology. (2018). Risk Manage-
[44] V.KrishnanandC.S.Sreeja,‘‘Zerotrust-basedadaptiveauthentication ment Framework for Information Systems and Organizations. [Online].
usingcompositeattributeset,’’inProc.IEEE3rdPhDColloq.Ethically Available:https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.
Driven Innov. Technol. Soc. (PhD EDITS), Nov. 2021, pp.1–2, doi: 800-37r2.pdf
10.1109/PHDEDITS53295.2021.9649474. [59] (2024).OWASPAuthenticationCheatSheet.[Online].Available:https://
[45] I.Ahmed,T.Nahar,S.S.Urmi,andK.A.Taher,‘‘Protectionofsensitive cheatsheetseries.owasp.org/cheatsheets/AuthenticationCheatSheet.html
data in zero trust model,’’ in Proc. Int. Conf. Comput. Advancements, [60] N. Harwood-Nash. (Jun. 2023). How Fast Do Planes Fly. [Online].
Jan.2020,pp.1–5,doi:10.1145/3377049.3377114. Available:https://airadvisor.com/en/blog/how-fast-do-planes-fly
[46] A.QaziandS.Arshad,‘‘Implementationofenhancedsecuritymeasuresin [61] V. Krishnan. (2026). ZeTHAA. [Online]. Available: https://github.com/
OracleERPcloudwithzerotrustarchitecture(ZTA),’’inProc.Int.Conf. vivinkrishnan/ZeTHAA
Commun.Technol.(ComTech),Apr.2025,pp.1–6.
[47] A.Farraj,‘‘Onusingzerotrusttosecuringindustrialcontrolsystemsin
thepowersystemsindustry,’’inProc.IEEETexasPowerEnergyConf. VIVIN KRISHNAN receivedthemaster’sdegree
(TPEC),Feb.2025,pp.1–5,doi:10.1109/TPEC63981.2025.10906998. intechnologyfromCochinUniversityofScience
[48] M. A. Aleisa, ‘‘Blockchain-enabled zero trust architecture for andTechnology.HeiscurrentlyaSoftwareArchi-
privacy-preserving cybersecurity in IoT environments,’’ IEEE Access, tect with Numentica Technologies, Bengaluru.
vol.13,pp.18660–18676,2025,doi:10.1109/ACCESS.2025.3529309. He is a Research Scholar at CHRIST (Deemed
[49] M.Tsai,S.Lee,andS.W.Shieh,‘‘Strategyforimplementingofzerotrust to be University), Bengaluru. He has more than
architecture,’’IEEETrans.Rel.,vol.73,no.1,pp.93–100,Mar.2024,doi: 18 years of IT experience. His areas of interest
10.1109/TR.2023.3345665. include information security, authentication, and
[50] A. Hassan, A. Rauf, N. Shafqat, R. Latif, and H. Khan, ‘‘ZenGuard a scalablesoftwaresystems.
machine learning based zero trust framework for context aware threat
mitigation using SIEM SOAR and UEBA,’’ Sci. Rep., vol. 15, no. 1,
p.35871,Oct.2025,doi:10.1038/s41598-025-20998-4.
[51] N.F.Syed,S.W.Shah,A.Shaghaghi,A.Anwar,Z.Baig,andR.Doss, C. S. SREEJA (Senior Member, IEEE) received
‘‘Zerotrustarchitecture(ZTA):Acomprehensivesurvey,’’IEEEAccess, the Ph.D. degree from CHRIST (Deemed to
vol.10,pp.57143–57179,2022. be University), Bengaluru, which focused on
[52] E.Hosney,I.Halim,andA.H.Yousef,‘‘Anartificialintelligenceapproach Informationsecurityaspects.SheisanAssistant
for deploying zero trust architecture (ZTA),’’ in Proc. 5th Int. Conf. Professor with the Quantum Technologies and
Comput.Inform.(ICCI),Mar.2022,pp.343–350. Complex Systems (CQTCS), CHRIST (Deemed
[53] E.Bertino,‘‘Zerotrustarchitecture:Doesithelp?’’IEEESecur.Privacy, to be University), where she has been a Faculty
vol.19,no.5,pp.95–96,Sep.2021,doi:10.1109/MSEC.2021.3091195. Member, since 2019. She has published her
[54] L.Bradatsch,O.Miroshkin,N.Trkulja,andF.Kargl,‘‘Zerotrustscore- researchworkinpeer-reviewedjournals,including
basednetwork-levelaccesscontrolinenterprisenetworks,’’inProc.IEEE ElsevierandInderscience,andintheproceedings
22nd Int. Conf. Trust, Secur. Privacy Comput. Commun. (TrustCom),
ofrenownedInternationalconferencesbyIEEE,Springer,andACM.Her
CA. Los Alamitos, CA, USA: IEEE Computer Society, Nov. 2023,
area of expertise in research includes, but is not limited to, information
pp.1422–1429. [Online]. Available: https://doi.ieeecomputersociety.org/
security,authentication,publickeycryptography,E-signature,bio-molecular
10.1109/TrustCom60117.2023.00194
computing, DNA cryptography, and blockchain. She also received the
[55] Q. Yao, Q. Wang, X. Zhang, and J. Fei, ‘‘Dynamic access control
IEEEbestthesisaward(second)forherPh.D.ThesisduringtheGraduate
and authorization system based on zero-trust architecture,’’ in Proc.
Int. Conf. Control, Robot. Intell. Syst., Oct. 2020, pp.123–127, doi: CongressGraTE’7’2019.ShealsoservedasareviewerforprestigiousIEEE
10.1145/3437802.3437824. Conferences,theSessionChair,andthePublicationsCo-ChairfortheIEEE
[56] SpecialPublication800-63b:DigitalIdentityGuidelines:Authentication PhDColloquiumonEthicallyDrivenInnovationandTechnologyforSociety
and Authenticator Management, National Institute of Standards and 2019and2020.SheisanactivememberoftheIEEEComSocBangalore
Technology,Gaithersburg,MD,USA,2025,doi:10.6028/NIST.SP.800- Chapter.
63B-4.
77878 VOLUME14,2026