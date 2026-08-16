---
conversion_metadata:
  converted_at: "2026-07-22T12:20:55Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Bernardo & Seva.pdf"
  source_pdf_sha256: "ebb41a7e1f04580c9e7fd283ebead19c805c40b617804d3dba60424a40330ec2"
  page_count: 24
  markdown_char_count: 192170
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Article
Affective Design Analysis of Explainable Artiﬁcial Intelligence
(XAI): A User-Centric Perspective

Ezekiel Bernardo *

and Rosemary Seva

Industrial and Systems Engineering Department, De La Salle University—Manila, 2401 Taft Ave, Malate,
Manila 1004, Philippines
* Correspondence: ezekiel.bernardo@dlsu.edu.ph

Abstract: Explainable Artiﬁcial Intelligence (XAI) has successfully solved the black box paradox of
Artiﬁcial Intelligence (AI). By providing human-level insights on AI, it allowed users to understand
its inner workings even with limited knowledge of the machine learning algorithms it uses. As a
result, the ﬁeld grew, and development ﬂourished. However, concerns have been expressed that
the techniques are limited in terms of to whom they are applicable and how their effect can be
leveraged. Currently, most XAI techniques have been designed by developers. Though needed
and valuable, XAI is more critical for an end-user, considering transparency cleaves on trust and
adoption. This study aims to understand and conceptualize an end-user-centric XAI to ﬁll in the
lack of end-user understanding. Considering recent ﬁndings of related studies, this study focuses on
design conceptualization and affective analysis. Data from 202 participants were collected from an
online survey to identify the vital XAI design components and testbed experimentation to explore the
affective and trust change per design conﬁguration. The results show that affective is a viable trust
calibration route for XAI. In terms of design, explanation form, communication style, and presence of
supplementary information are the components users look for in an effective XAI. Lastly, anxiety
about AI, incidental emotion, perceived AI reliability, and experience using the system are signiﬁcant
moderators of the trust calibration process for an end-user.

Keywords: explainable AI; XAI; artiﬁcial intelligence; AI; interpretable deep learning; machine
learning; computer vision; affective design; emotions; end-user design

1. Introduction

Recent breakthroughs in algorithmic techniques and the complementary development
of more capable computing tools have exponentially progressed the artiﬁcial intelligence
(AI) ﬁeld. These advancements have boosted AI’s analytical power, enabling convolution to
take on more cognitively demanding tasks [1,2]. As an effect, AI can now be seen powering
different systems, for multitudes of uses, and at varying levels of human augmentation.

While the added utility that AI can potentially bring is undeniably beneﬁcial, un-
fortunately, it also detriments the possible adoption of users to it. Why? Because these
advancements were realized by sacriﬁcing AI’s interpretability or the ability to understand
how and why the AI came up with its recommendations. This stems from using complex
algorithms (i.e., machine learning—ML and deep learning—DL) that are inherently incom-
prehensible [3]. In return, it restricts how trust [4–8] and subsequent reliance [9] can be
calibrated accurately, given that users are unaware of AI’s actual inner workings. This often
leads to over-trusting an incapable AI or, at worst, abandoning a reliable AI, which is a
pressing issue considering how society frames AI’s role in the future [10,11].

So, why do the experts that developed the algorithms not just provide the explanations?
As simple as it seems, this will not work as AI functions similarly to human brains [12].
Evolution will happen as it learns, creates rules, contextualizes, and eventually adapts to
gain performance. Because of this, new parameters (“hidden layers” in the context of ML)

Citation: Bernardo, E.; Seva, R.

Affective Design Analysis of

Explainable Artiﬁcial Intelligence

(XAI): A User-Centric Perspective.

Informatics 2023, 10, 32.

https://doi.org/10.3390/

informatics10010032

Academic Editor: Long Jin

Received: 17 January 2023

Revised: 9 March 2023

Accepted: 14 March 2023

Published: 16 March 2023

Copyright: © 2023 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under

the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

Informatics 2023, 10, 32. https://doi.org/10.3390/informatics10010032

https://www.mdpi.com/journal/informatics

---

<!-- PAGE 2 -->

Informatics 2023, 10, 32

2 of 24

that are not originally part of the understandable design are added to the system, making it
inexplainable to all users, including the developers [13]. For this reason, the issue is often
tagged as the black box paradox of AI [14].

As a workaround solution, the innovative ﬁeld of explainable AI (XAI) has been intro-
duced. Rather than entirely unpacking the algorithms that the AI uses, which is difﬁcult, it
focuses on providing human-level explanations conceptualized from the comprehensible
facets of the AI [15]. It centers on the AI’s purpose, process, and performance to grant
cognitive resources [16,17] to help developers [18] (e.g., troubleshooting, understanding
limitations, and improving performance) and to answer critical questions raised by an
end-user [19]. Often, this is in the form of visualization tools embedded in the AI interface
for interaction [20].

Take image recognition, for instance, which is one of the ﬁrst, most prominent, and
well-researched AI domains. XAI is being used as an alternative in explaining the thinking
process of the AI (e.g., heat maps, feature examples, rule explanations, etc.). This makes the
complex analysis per bitmap (i.e., geometric coding and pattern analysis) [21] comprehen-
sible and deducible for trust and reliance assessment for adoption [22,23]. As a result, more
demanding tasks (e.g., self-driving cars with visualization, facial recognition with saliency
maps, etc.) are being unlocked and adopted across different functions [20]. This goes the
same with other domains, which saw positive changes upon using XAI [15].

The beneﬁts from XAI have encouraged many scholars to expand the ﬁeld by develop-
ing newer techniques, with the majority taking on the challenge of providing a deeper and
more accurate representation of AI’s complex inner workings (e.g., Deterministic Local In-
terpretable Model-Agnostic Explanations, Shapley Additive Explanation, and Quantitative
Testing with Concept Activation Vectors) [8,15]. As a result, most of the research has cen-
tered on what information XAI should carry, or focused on its role as a cognitive repository
of explanation [24,25]. Although this is theoretically useful given the ﬁeld’s infancy and
rapidly expanding AI use cases, the spotlight from current research has underrepresented
the end-users and centered more on the developers [26–28].

Three foundational aspects can be synthesized from the current research stream that
supports the claim. First, expertise with ML and DL is needed to understand current XAI
techniques, which a typical end-user does not have [18,19]. Next, the goal is often directed
at improving AI’s algorithm [29,30] and not on an end-user’s fundamental goal of triggering
adoption and its prerequisite of trust. Lastly, current techniques were mainly viewed as a
cognitive resource rather than a bridge in human–computer interaction (HCI) [25,31]. This
means that little to nothing is known about how XAIs are perceived by an end-user when
embedded in an AI, considering its inherent characteristics. With the limited understanding
of the end-user context, this can cause a signiﬁcant threat to the trajectory of AI’s role in
society, viz., possibly halting the advantages AI can bring to the day-to-day life of humans.
Considering the gap in the context of end-user XAI, this study is proposed to an-
swer the question: “How to create an end-user-centric XAI?”. As pointed out by re-
cent works, people are approaching XAI with the same attitude of expectation they are
employing towards another human [32–34]. This entails that, in using XAI, interaction
process (how the stimuli were used), structure (how it is presented), and variability (pos-
sible external inﬂuences) can play essential roles in making a judgment (i.e., trust and
reliance) [29,31,33,35–37]—aspects that have been limited in existing XAI research. With
that, the problem will be examined following the objectives:
•
Determine how an end-user calibrates trust from XAI.
•
Identify the factors that can signiﬁcantly change how trust can be calibrated.
•
Examine possible moderating factors that can affect the calibration process.
• How do external factors moderate the effect of XAI in the calibration process?

The remainder of this paper is divided into six sections. The next section presents the
background of the study. Sections 3–5 confer the experiment design, give the data-gathering
results, and discuss the ﬁndings with respective recommendations based on the study’s
objectives. Finally, the last section closes the paper with the conclusion.

---

<!-- PAGE 3 -->

Informatics 2023, 10, 32

3 of 24

2. Review of Related Literature

Using this idea and the different theories in other spaces that similarly examined
cognitive-based stimuli, this study aims to address the problem through the interaction
lens in terms of the trust calibration process, design for the structure, and external limits
for inﬂuences.

2.1. Trust Calibration

Trust calibration is a dynamic process as it encompasses different dimensions (e.g.,
performance, reliability, predictability, etc.), and can be processed on various routes. In
the study conducted by Lee and See [38], they identiﬁed three possible ways to tune trust
based on rationality, societal belief or norms, and engagement of emotions. They devised
these routes as cognitive and affective routes. Cognitive can be further broken down as
analytic and analogic. The applicability of the routes mainly depends on the available
information, the relationship between the trustee and trustor, and how the information can
be elaborated in that situation.

2.1.1. Cognitive Trust Calibration

If trust is formed from a rational evaluation of a trustee’s salient behavior, this is
considered analytic processing [39]. This method overstates cognitive capacities as a
limitation for rationality, and understates the inﬂuence of emotions and strategies for
trust formation. This functions as knowledge-based processing, relying on a function-
based mental model of the system such as with motivation, interests, performance, and
capabilities [38]. Further, knowledge can be sourced through direct observation, possible
intermediaries, and presumptions available to the trustor.

On the other hand, if trustworthiness is determined based on societal norms, reputable
opinions, or any enabling information without direct contact, analogic processing is con-
sidered. This method heavily assumes that trust can be developed as an offset of belief
from signiﬁcant intermediaries and not on the direct experience from the system being
considered. This is less cognitively taxing than analytic processing and mainly uses rules
and presumptions [39].

2.1.2. Affective Trust Calibration

Aside from cognitive, another way to calibrate trust is via emotions or how people
feel. As the name implies, affective processing is strictly based on the emotions generated
by and toward the entity [39]. Compared to the analytical and analogical of cognitive
processing, this method minimizes the need for rational cues and prioritizes how people
feel about the system—the core inﬂuence of trust on behavior [40]. In addition, this route
mainly focuses on moment-to-moment trust—subjected to intrinsic and environmental
factors—since emotion tends to ﬂuctuate over time (e.g., expectation does not conform to
the ongoing experience). In the simplest terms, the core belief on this route is that people
think and feel trust.

Lee & See [38], in their well-cited HCI study, propose the idea of the affective route sug-
gesting that trust might also be induced by irrational factors, such as emotions and moods
(additional discussion is presented in the Affect section). Operationally, this leverages the
user’s emotional responses to the stimuli rather than its intellectual or cognitive resources.
The idea is deeply rooted in the social science paradigm, which argues that in an interaction,
aside from the cognitive gain, people can also develop affective states (e.g., positive or
negative mood, happy, sad, confused, and scared emotions), which can be infused in the
evaluation of the trustee’s abilities, competence, and trustworthiness [41–44]. These can run
as short-term emotions or long-term moods, allowing them to act as continuously shifting
inﬂuences that continually alter perception and trigger the mental processes that lead to
particular behaviors [45,46].

Madsen & Gregor [47] also pointed out that affective processing can calibrate trust
more rapidly and unconsciously; needs little to no cognitive resources; and can also be

---

<!-- PAGE 4 -->

Informatics 2023, 10, 32

4 of 24

developed outside the interaction from the stimuli (e.g., disposition or personality), which
makes the argument of it being dominant over cognitive processing. For example, Myers &
Tingley’s [48] money trust game identiﬁed that negative emotions (i.e., anxiety and fear)
could decrease trust, but only if those negative emotions make people feel less sure about
their current situation. Conversely, people tend to trust more if they experience positive
emotions even though the game presents a certainty of losing. In hospitality research, Jin
& Merkebu [49] found that in an upscale restaurant, positive emotion signiﬁcantly led to
higher customer trust and gratitude even in varying conditions of service (i.e., fast and slow
serving time). Fundamentally, people navigating through the affective route can decide not
to trust simply because of uneasy feelings that cannot be explained rationally, or by trusting
a system due to a particular emotion that developed during the moment of interaction.

2.1.3. Synthesis for Trust Calibration

Relating this processing to XAI, current research has focused on cognitive processing.
As presented previously, the running hypothesis in the research stream is that interpretabil-
ity has a direct relationship with the depth of cognitive information it provides. More so,
all the identiﬁed goals for XAI are regressed against its cognitive aspect. For example, by
allowing people to think, they will understand that AI is trustworthy.

On the contrary, affective processing is still an area to be explored for XAI trust
calibration. As of the writing of this paper, there are no studies that tried to evaluate the
affective ability of XAI to calibrate trust. At the very least, there are pieces of evidence
showing the ability of XAI to engender emotions. For instance, Jensen et al. [50] successfully
classiﬁed four primary affective states out of the nineteen pre-identiﬁed emotions, which
include hostility, positivity, anxiety, and loneliness, by showing additional explanations
of the process and performance of a drone AI system. Albayram et al.’s [51] work on
safety-critical AI systems factored negative individualistic emotion, positive emotion, and
negative prosocial emotions as the three main states out of 44 pre-identiﬁed emotions upon
subjects’ exposure to the explanation of role and criticality of the situation. By examining
human facial reactions and signals (i.e., brow, cheek, and lips movement), Guerdan et al. [52]
successfully identiﬁed that emotions such as happiness and anger are manifested when
people interact with XAI interfaces.

There are also pieces of evidence showing the emotion–trust relationship for XAI. For
example, eight pictures depicting positive or negative moods were used by Phillips and
Madhavan [53] to manipulate the participants’ initial emotional state. Their experiment
determined that users with positive moods are more susceptible to trust AI recommenda-
tions than negative moods. Merritt (2011) and Du et al. (2020) used affectively laden video
clips (i.e., happy, sad, scary) to prime the emotional status of the participants. The former
suggests that the decision-making process is driven emotionally rather than rationally,
while the latter proved that positive valence led to better takeover quality. Gompei &
Umemuro [54] discovered that trust towards utility information (e.g., instructions for a
task, explanations from an event) from social robots is developed via the affective route.
Speciﬁcally, the degree of feelings is directly correlated to the trust towards the information
and the robots (i.e., positive emotion leads to higher trust). For automated computer warn-
ings, Buck et al. [55] found that the quality of cognitive information presented by the alerts
was not the primary determinant of trust. Affective state fundamentally calibrated the trust
stance of users with positive affect building more trust than other developed emotions
such as anxiety, hostility, and loneliness. Bernardo & Tangsoc [56] identiﬁed that trust seals
(i.e., certiﬁcation showing payment assurance) serve as affective cues rather than cognitive
stimuli. As veriﬁed from the post hoc interview, exposed people developed a sense of
happiness and conﬁdence which triggered trust formation. For intelligent personal assis-
tants, Chen & Park [57] determined that even if it is intended to deliver factual responses,
trust is primarily calibrated based on the feeling of positive social attraction rather than the
correctness of the information it provides.

---

<!-- PAGE 5 -->

Informatics 2023, 10, 32

5 of 24

2.2. Emotional or Affective Design

With the consideration of the affective path approach, emotional design, also known
as affective design, is considered. This is a research ﬁeld concerned with creating designs
that elicit emotions from users to trigger speciﬁc behavior [58,59]. This attempts to deﬁne
the subjective emotional relationships between users and stimuli and explore the affective
properties that intend to communicate through their design attributes [46,60]. In other
words, the idea is to identify a speciﬁc design element that can potentially engender a
particular emotion that will lead to a speciﬁc change in the target behavior. This concept has
been used in a variety of domains such as in the user interface of children’s e-learn to create
positive attachment [61]; computer game design to enhance enjoyment and happiness [62];
eco-labels to promote positive affect which triggers purchase intention [63]; social robots
to enhance positive perception and preference [35]; and trash bin signages to encourage
waste segregation [64] to name a few.

In the timeline of affective design, the three most inﬂuential works were proposed by
Norman [65], Jordan [66], and Khalid & Helander [67]. Conceptually, the ideas differ in
how they approach design and scale its potential effect.

2.2.1. Three Levels of Processing

The Three Levels of Processing by Norman [65] views affective design in conjunction
with how the human brain processes design during an interaction. It is divided into
three categories which ﬂex from a surface-level view of the design features, an experiential
of its overall package, to an analytical approach that uses experience. Respectively, these
are categorized as visceral, behavioral, and reﬂective designs.

Of the three, the lowest level is visceral. This encapsulates the distinctive visual
aspects of the design, such as color, size, texture, shape, or any ﬁgurative element of the
design critical to its aesthetic value. Considering XAI as an example, visceral design is
concerned with how the attributes are presented, the theme of the images, the font size of
the explanations, or the thickness of the elements in a graph. Because of this scope, it uses
automatic or pre-wired processing that makes rapid and straightforward decisions on the
stimuli through pattern matching—appealing to the immediate emotional response to how
the user intuitively perceives the design.

The next level is behavioral design, which values an experiential view of the design. It
operates on the performance and functionality of the design over its superﬁcial appearance.
Conceptually, this functions in parallel with traditional usability engineering, meaning
designs are invested in how users carry out their activities, how accurately they achieve
their objectives, how many times and errors can be committed, or how well the design
accommodates different types of users. Relating again to XAI, this level of design is
concerned mainly with whether the user absorbed the explanations to perceive a certain
level of trust or its subsequent reliance behavior.

Lastly, the highest level is reﬂective design. Compared to the ﬁrst two, this leverages
more past experiences and knowledge rather than real-time design evaluation, using
developed interest or learned preferences for design. Traditionally, this is related to the
message the design sends to the user, which is evaluated on its parity with the self-image
the user wants to project. With that, reﬂective design is approached more consciously,
weighing its pros and cons according to a more rational side. In the context of XAI, this
can be a design based on the user’s personal preference grown over the interaction with
other explanations. For example, a user might prefer a heatmap due to their visual skills
and personal belief that it is better than other forms of explanation.

2.2.2. Four Pleasures

Another way that affective design has been categorized is with the Four Pleasures by
Jordan [66]. In this categorization, the main premise is that it emphasizes pleasure above
all else. Meaning, functionality, an aspect that is heavily considered in the proposal of
Norman [65], is not explicitly reﬂected. This is developed based on the known types of

---

<!-- PAGE 6 -->

Informatics 2023, 10, 32

6 of 24

pleasures from an anthropological perspective, divided into four types: physio-, socio-,
psycho-, and ideo-pleasure.

Physio-pleasure is an affect developed from the appreciation of the senses. For XAI,
since it is presented as an explanation in the interface of the AI system, it highly leverages
the sense of sight—how visually appealing the design is to deliver pleasure. On the other
hand, socio-pleasure stems from the interaction with others—whether it follows a certain
norm or is socially accepted. Operationally, this can be how XAI design resonates with the
well-accepted or favored way of giving explanations. For instance, for visual search tasks,
a visual feature-based explanation is better than a verbal one, which is socially acceptable.
If the focus is on the cognitive caveat of the stimuli, psycho-pleasure is considered. In
the context of XAI, this relates to the cognitive ability (i.e., memory, stress, workload) of
the user on how it should be designed to limit its negative effect. This can be performed
by simplifying the load presented or selecting a different form of explanation. Lastly,
idea-pleasure involves the user’s values and beliefs in appreciating the design. For XAI,
this mostly resonates with the aesthetic taste, which is relatively the same as the reﬂective
design of Norman [65].

2.2.3. Framework for Affective Customer Needs

Lastly, another foundational idea used in affective design for categorization is Khalid
& Helander’s [67] Framework for Affective Customer Needs. Relative to the ﬁrst two, it
was developed based on empirical results from an extensive survey rather than a parallel
view from an anthropological phenomenon (i.e., brain functions for the three levels of
processing and pleasure class for the four pleasures). They used a survey to rate product
features and then categorized them using factor analysis. Their results factored three
generic categories of user preference: holistic attributes, styling, and functional design.
Their study highlighted that familiarity differs from users’ stance on design appreciation.
Holistic attributes can be thought of as the gestalt of the product. This means that
designs are viewed as packages rather than speciﬁc components. Designs in this catego-
rization are from products unknown to the user. In the context of XAI, these are users
not familiar with the basic functionality of the system and the explanation itself. On the
other hand, if the design prioritization is on speciﬁc details, this often falls on styling. This
focuses on speciﬁc attributes such as colors, shapes, and sizes. The speciﬁcity is highly
attributable to the user’s familiarity with the product in consideration. If the familiar users
are way past the aesthetic quality of the design, they can dive into the functional level,
which relates to the types of tasks the product works for the user. For XAI, this can be
whether the explanation is appropriate in the given context.

2.2.4. Synthesis of Emotional or Affective Design

The different levels of design discussed, with some overlapping, showed what aspect
of design speciﬁc users consider given their varying characteristics. Considering this, the
study will mainly focus on the design attribute types rather than speciﬁc design components
of it (i.e., color, size, and shape). This decision is driven primarily by two points. First,
since there had been no study on affective design for XAI, a higher-level approach will be
beneﬁcial as an output to be used for future studies. Identifying which among XAI form
types of work is more encompassing than a speciﬁc design component that can observe
certain reservations. The second point follows the familiarity aspect raised by Khalid &
Helander [67], wherein novice users—the focus of this study—value holistic attributes
rather than speciﬁc styling.

2.3. Proposed Model and Hypothesis

Overall, the synthesis from the review of the related literature highlights the study’s
setup. As for the interaction, this study will deviate from the running hypothesis of the
cognitive route. Mainly, this study will center on the experience beyond the rational view
through affective calibration. The XAI emotion set (XES) of Bernardo & Seva [68] will be

---

<!-- PAGE 7 -->

Informatics 2023, 10, 32

7 of 24

used to measure changes. Coinciding with this, for the design, the study will value the
principle of emotional design. This leverages design saliency to trigger emotions or how
stimuli present their different design attributes. Following the end-user-centric approach, a
pre-study will be performed to identify these design attributes. Lastly, for limitations, the
study will consider both AI and user properties following the role of XAI in the interaction
and qualitative claims from other HCI studies [55,69,70]. This will include AI anxiety,
incidental emotions, trust disposition, and XAI experience for human factors, while also
AI reliability, learning capability, brand, and experience for AI factors. To encapsulate the
synthesis from the review of the related literature and the overall plan of this study, an XAI
Trust Calibration Model (XAITC) model is proposed (see Figure 1). This builds upon the
synthesized framework for XAI research from a user model perspective of Haque et al. [25].
Each path will be tested as a separate hypothesis to conﬁrm the model.

Figure 1. XAI Trust Calibration Model.

By answering the objectives, the end goal is to provide the following contributions to

the ﬁeld of XAI:
•

Being the ﬁrst study to verify how trust calibration from XAI happens through the
lens of an end-user.
Valuing the importance of the user-centered approach, this study shed light on the
user’s view of XAI design composition and its perceived importance in explaining
and possibly building the theories for XAI trust research.
Based on the results of this study, different insights on how XAI can be designed are
generated, which can potentially be used to leverage the effects of emotions.
By understanding the dynamics of external factors, better situational use of XAI can
be created.

•

•

•

3. Materials and Methods

To test the proposed hypothesis, viz., to analyze the objectives of the study, an asyn-
chronous experiment was designed and carried out. The goal was to simulate an interaction
with XAI by using an existing AI-powered system. This was performed using an exper-
imental testbed where different design combinations were prompted to the user in a
between-subject design. Data that were recorded were based on the independent variables
from the XAITC model.

To guide the development, a pre-study was conducted with four primary goals: (1) to
identify the most familiar AI to avoid alienation, (2) to decide the design setup to minimize
the undesirable effect of negative user experience, (3) to determine the design attributes
of XAI considered to be necessary by users, and (4) to identify the conﬁgurations of the

---

<!-- PAGE 8 -->

Informatics 2023, 10, 32

8 of 24

moderators. Data were collected from an online survey answered by 312 current AI users.
For idea validation and feasibility assessment, results were run through a focus group
discussion comprised of six AI developers and six user experience designers.

The conclusion was to use image classiﬁcation AI as a use-context, with the Google
Lens application as the template for the overall composition and logic ﬂow. For the XAI,
three design attributes were selected. Notably, (1) the explanation form or how XAI
is presented, (2) the communication style for the explanation, and (3) the presence of
supplementary information. Two levels per design attribute were considered based on the
enumeration of Jian et al. [71].

For the AI features, reliability was set to differ from 70% for low and 90% for high.
Learning capability defaulted to pure conditions. As for the brand, Google was selected to
be the name to represent high-reputation AI. Lastly, for the time experience, two days was
deemed optimal. All in all, 64 designs (26) were tested. Take note that time experience was
not considered as part of the factorial computation given that it is not a design input but a
moment of recording. Table 1 summarizes all design conﬁgurations for the experiment.

Table 1. Experimental design conﬁgurations.

Component

Variable

# of Levels

Conﬁgurations

XAI Design

AI Features

Explanation Form
Communication Style
Supplementary Information

AI Reliability
Learning Capability
Brand
Time Experience

2
2
2

2
2
2
2

Feature, Example
Humanized, Robotic
With, Without

Low (70%), High (90%)
Yes, No
Google, Generic
Day 1, Day 2

3.1. Participants

The snowball convenience sampling method was used for the data gathering. Initial
leads were generated from direct invitations of peers and promotional ads posted in various
social networking groups. Qualiﬁcations were set as being able to communicate in English,
being at least 18 years old, having a normal or corrected-to-normal vision without any
color blindness issues, and with experience using any AI-powered system. Considering
the nature of the study, being not emotionally depressed was also a requirement to limit
bias and skewness. This, however, was not posted as part of the advertisement material to
avoid discrimination. Further discussion on how these requirements were conﬁrmed will
be given in the next section.

Technical requirements were also speciﬁed to facilitate the experiment effectively
in remote conditions. Particularly, having a smartphone with at least 1080 × 1920 pixel
resolution without any screen issues, internet connectivity of at least 5 Mbps, an updated
web browser app, and availability of area conducive to the experiment. Additionally, they
were required to have at least 30 min of uninterrupted time to perform the test for two days.
A token worth 100 PHP (~2.00 USD) plus a performance bonus ranging from 25 PHP to
50 PHP was guaranteed in exchange for their complete involvement.

Considering the overarching goal of the paper of testing the relationships involved
in the trust calibration of an end-user from XAI through the proposed XAITC model,
as well as to attain a statistically capable data set, the minimum sample size was set to
152 participants. This was evaluated based on the principles set by Kline [72] for structural
assessment and the result of the priori-power sample computation established from the
guidelines of Westland [73] and Cohen [74]; the setup was at 0.3 anticipated effect size,
0.85 desired statistical power level, and 0.05 alpha level.

3.2. Measurements

Data were captured through an online questionnaire and an experimental testbed.
The former requested the control (i.e., demographics, disposition, and situational factors)

---

<!-- PAGE 9 -->

Informatics 2023, 10, 32

9 of 24

and independent variables (i.e., depressive state and incidental emotions), while the latter
enabled the manipulation of XAI design attributes to measure changes from the interaction.
Both tools were designed to be accessed through a web browser, with English being its
default language.

3.2.1. Online Questionnaire

A three-section online questionnaire was developed and hosted through Google Forms.
The ﬁrst section functioned as the preliminary, where the overview, general instruction, and
data consent clause were detailed. It also carried the yes-or-no screening test for English
language competence, age restriction, visual acuity, and AI experience. As for the depressive
state, the Mood and Feeling Questionnaire (MFQ) developed by Angold & Costello [75] was
used. Moving on, the second part requested demographic and dispositional information.
Age, gender, educational attainment, occupation, and income were the identiﬁed controls.
For the disposition, trust assessment by Frazier et al. [76] and AI anxiety measurement by
Wang & Wang [37] were contextually used. Finally, the last section inquired about AI plus
XAI experiences and incidental emotions. The years of experience were in a multiple-choice
form, while four new seven-point Likert questions were developed to measure incidental
emotions. The XAI emotion set (XES) of Bernardo & Seva [68] was used as the reference for
the different emotion groups.

3.2.2. Experiment Testbed

The three-sectioned testbed was built using Figma and was hosted through the Quant-
UX prototyping site. The ﬁrst section handled the instruction and examples, with three
practice trials available. This was followed by the second section, which carried the main
image classiﬁcation task. The general workﬂow is as follows: (1) the participants will ﬁrst
select the image from the gallery, (2) the AI will generate its recommendation and explain
its decision-making, and (3) the participants will decide on whether to agree or provide
their classiﬁcation as a measurement for their reliance. Take note that the correctness of
recognition was not disclosed as the testbed’s purpose was limited to recommendation and
machine learning. Finally, the third section features the rating scale sliders for the integral
emotions, measured like the incidental emotions mentioned earlier. Figure 2 presents
sample screenshots of the testbed.

Figure 2. Sample screenshot of experiment testbed: (a) AI classiﬁcation and XAI presentation of the
image being recognized; (b) dependent variable sliders to be answered after classiﬁcation.

---

<!-- PAGE 10 -->

Informatics 2023, 10, 32

10 of 24

The user experience, grammar, spelling, and interface of both tools were pre-tested
with nine current AI users, three English language experts, and four app developers. Rec-
ommendations were implemented before its use for the main experiment. In addition, factor
consistency and validity of the newly introduced questionnaire for incidental emotions
were checked.

3.3. Procedure

There are three phases in data-gathering: pre-experiment onboarding, main experi-

ment, and post-experiment analysis.

3.3.1. Pre-Experiment Onboarding

The experiment started with the participants attending a synchronous online onboard-
ing via Facebook Group Call. The focus was to relay the general instructions, check the
setup requirements, present the data conﬁdentiality, and explain the priming condition. In
particular, the scenario was that an NGO hired the participants to help recognize pictures of
different species in the Philippines saved in their database. To aid them, an image recogni-
tion AI system was developed that could give recommendations on what species the photos
contain. Participants were allowed to use it or provide their own. The onboarding ended
with the measurement tool links shared with the participants for asynchronous access.

3.3.2. Main Experiment

The main experiment started with the participants accessing the online questionnaire.
They were allowed to do it anytime as long as they ﬁnished it uninterruptedly. Upon
access, participants were prompted with the data agreement and screening questions.
Those who agreed and qualiﬁed were the only ones allowed to continue. Demographic
information was then requested from the participants, together with the rating for AI, XAI,
and incidental emotions-related questions. Once completed, participants were forwarded
randomly to any of the 24 designs of the XAI testbed.

The use of the XAI testbed started with the preliminaries: application information,
general instructions, and the recap of the priming scenario. Each participant was in-
structed to classify 50 random photos available in the application. This was performed
on two consecutive days (25 photos per day), with scores recorded to measure the per-
formance bonus for the compensation. After completing the required task, additional
instructions were given to the participants, plus the list of available schedules for the
voluntary post-experiment interview and mode of call.

3.3.3. Post-Experiment Analysis

After all the data were collected, the post-experiment analysis started. It centered
on analyzing experiment results, interviews, and token distribution. Initially, the data
were assessed for completeness and performance. Those who garnered at least 40 correct
classiﬁcations were tagged to receive an additional 25 PHP (~0.5 USD), while 50 PHP
(~1 USD) was intended for those who got all correct. Once ﬁnalized, the evaluation was sent
to the participants via their social media accounts and email. This contained information
on how the token will be distributed, the interview schedule for those who volunteered,
and the meeting access links. The interview focused on the reasoning for the answers on
the dependent variables.

3.4. Technique of Analysis

The analysis was principally driven by the two-stage methodology proposed by
Lowry & Gaskin [77] for Structural Equation Modeling (SEM) under a covariance-based
optimization. This technique was selected, primarily, because of its ability to deduce causal
relationships proposed in the objectives. In addition, it can estimate model parameters that
minimize residual variance [78], is insensitive to parametric conditions [79], and is suitable
for simultaneous analysis of the design constructs [80].

---

<!-- PAGE 11 -->

Informatics 2023, 10, 32

11 of 24

Analysis was segmented into two main phases. The ﬁrst part is for the conﬁrmation
of the rigidity of the tool and the data it gathered. This was performed via factor analysis
and measured against convergent, discriminant, and ﬁt measures. After conﬁrmation, SEM
was performed which was further divided into mediation analysis to conﬁrm the path of
calibration, direct analysis for the relationship between the design component and integral
emotions, and moderation analysis for the effect of incidental emotions and AI reliability.
All tests were assessed based on their statistical signiﬁcance and rigidity.

As for the data management, representative ﬁgures were computed based on the
aggregate measurement from the initial trial up to the time considered. This adheres to
the recommendations by Yang et al. [81] on the detectable moment of difference (i.e., the
area under the curve). Since the method of use was SEM, design elements were coded
dichotomously (e.g., +1, −1) to represent change. For moderators, the multigroup test was
the approach used to parallel the objectives of the study. Particularly, for factors that used
the Likert scale, conversion is based on the midpoint.

The main program used was IBM’s Analysis of Moment Structure (AMOS) graphics
version 24. In addition, Design Expert (DX) version 13 was used to generate the design of
the experiment, and IBM’s Statistical Package for the Social Science (SPSS) version 25.0 was
used for all statistical tests outside SEM. For consistency, testing was held constant under a
p < 0.05 signiﬁcance.

4. Results

The data gathering lasted for 15 days. Seven onboarding sessions were conducted,
with at most 40 participants per session. The cumulative time in the main experiment
lasted 40 min, with access happening between 11:00 a.m. and 10:00 p.m. There were
no recorded ethical concerns or testbed issues. As for the post-interview, 22.27% of the
participants joined, with an average call lasting 10 min. Lastly, those who scored 12 or
above on the MFQ were notiﬁed at most two days after the experiment and were referred
to a professional health organization.

4.1. Data Screening

All in all, 234 participated in the data gathering. After ﬁltering, only 202 were consid-
ered for analysis as the data from those who failed the requirements, tested positive for the
depression test, and did not ﬁnish the experiment were removed.

The summary of the demographics is presented in Table 2. Structurally, the gender
count for those who disclosed was relatively the same (male—40.59% and female—44.55%),
with the majority belonging to the millennial age group (58.42%), followed by generation
X (22.77%), and generation Z (16.34%). Most were degree holders (vocational—9.41%;
college—68.81%; postgraduate—15.84%) and part of the working class (67.33%). Look-
ing at AI-related factors, the majority have at least ﬁve years of experience (more than
5 years—71.78%; 3 to 5 years—25.25%; less than 2 years—2.97%), with almost all having
previous interaction experience with an XAI (90.10%). For the moderators, most of the
participants reported positive incidental emotions (71.78%), used the high AI reliability
version (62.87%), and were recorded at the later stage of use (56.44%).

Table 2. Summary of subjects’ demographics.

Type

Count

%

Type

Count

%

Age

Gen Z (18 to 23)
Younger Millennial (24 to 30)
Older Millennial (31 to 39)
Younger GenX (40 to 47)
Older GenX (48 to 55)
Younger Boomer (56-65)

33
54
64
36
10
5

16.34%
26.73%
31.68%
17.82%
4.95%
2.48%

Educational Attainment

Elementary
High School
College
Masters
PhD
Technical Vocational

0
12
139
25
7
19

0.00%
5.94%
68.81%
12.38%
3.47%
9.41%

---

<!-- PAGE 12 -->

Informatics 2023, 10, 32

12 of 24

Table 2. Cont.

Type

Count

%

Type

Count

%

Gender

Male
Female
Prefer not to say

AI Experience

Laggards (Less than 1 year)
Late Majority (1–2 years)
Early Majority (3–4 years)
Early Adopters (4–5 years)
Innovators (More than 5 years)

82
90
30

3
3
15
36
145

40.59%
44.55%
14.85%

1.49%
1.49%
7.43%
17.82%
71.78%

Occupation

Student
Employed (Full Time)
Employed (Part-Time)
Unemployed
Freelance/Contractor
Self-employed
Retired

56
81
13
9
20
22
1

27.72%
40.10%
6.44%
4.46%
9.90%
10.89%
0.50%

4.2. Exploratory Factor Analysis

Excellent results from the exploratory factor analysis (EFA) supported the use of the
designed questionnaire to capture the latent variables of AI anxiety, incidental emotion,
trust disposition, perceived usefulness, and perceived trust.

Primarily, the 0.919 Kaiser–Meyer–Olkin (KMO) measure and signiﬁcant Bartlett’s test
of sphericity (p < 0.001) highlighted the high proportion of variance among variables [82]
(see Table 3). This was further proven by the high communality extraction ranging between
0.947 and 0.958 and high cumulative variance for ﬁve component eigenvalue at 88.710%. As
for loadings, the proposed ﬁve dimensions were cleanly factored with high intercorrelation
scores (minimum of 0.731) and no signiﬁcant cross-loadings under a principal component
analysis extraction at a varimax normalization (see Table 4). This highlighted that the
structure of the questions does not overlap due to its validity securing a highly stable
analysis [83].

Table 3. Internal consistency measures.

Consistency Measure

Kaiser–Meyer–Olkin Measure
Bartlett’s Test of Sphericity
Approx. Chi-Square
df
Sig.

a Signiﬁcant at p < 0.05.

Table 4. Rotated component matrix.

Measurement

0.919

7055.358
253.000
<0.000 a

Dimension

AI Anxiety

Incidental
Emotion

Trust
Disposition

Perceived
Usefulness

Perceived
Trust

AIAnxietySocioTechnicalQ6
AIAnxietySocioTechnicalQ5
AIAnxietySocioTechnicalQ4
AIAnxietyLearningQ3
AIAnxietyConﬁgurationQ7
AIAnxietyLearningQ1
AIAnxietyConﬁgurationQ9
AIAnxietyLearningQ2
AIAnxietyConﬁgurationQ8
IncidentalEmotionQ1
IncidentalEmotionQ2
IncidentalEmotionQ4
IncidentalEmotionQ3

0.970
0.960
0.957
0.956
0.954
0.953
0.947
0.939
0.928

0.937
0.936
0.929
0.916

---

<!-- PAGE 13 -->

Informatics 2023, 10, 32

13 of 24

Table 4. Cont.

Dimension

AI Anxiety

Incidental
Emotion

Trust
Disposition

Perceived
Usefulness

Perceived
Trust

TrustDispositionQ4
TrustDispositionQ2
TrustDispositionQ3
TrustDispositionQ1
PercUsefulnessQ3
PercUsefulnessQ2
PercUsefulnessQ1
TrustQ1
TrustQ2
TrustQ3

0.987
0.979
0.978
0.978

0.868
0.849
0.759

0.806
0.761
0.731

Note: Extraction method via principal component analysis; Rotation method via varimax with kaiser normaliza-
tion; Rotation converged in 6 iterations.

4.3. Conﬁrmatory Factor Analysis

Same with the ﬁndings from the EFA, conﬁrmatory factor analysis (CFA) also attests to
the structure of the dimensions (see Table 5). From the model validity test, Cronbach’s alpha
and average variance explained (AVE) showed high reliability and convergent validity,
respectively, as all are above the threshold of 0.70 [84]. Moreover, divergent validity also
follows the same trend with minimum shared variance (MSV) being below AVE and
maximum reliability (MaxR(H)) being above 0.70 [83]. All of these were achieved at an
excellent ﬁtted conﬁrmatory model as highlighted in Table 6. Collectively, the measures
validated the questionnaire’s ability to explain incidental emotion and soundness to be
used for the hypothesis testing.

Table 5. Model validity measures.

Dimension

AI Anxiety
Incidental Emotion
Trust Disposition
Perceived Usefulness
Perceived Trust

CR

0.988
0.983
0.989
0.832
0.831

AVE

0.904
0.935
0.957
0.630
0.627

MSV

0.101
0.445
0.017
0.106
0.445

MaxR(H)

0.989
0.983
0.992
0.944
0.927

Note: CR—Cronbach’s alpha; AVE—average variance explained; MSV—minimum shared variance;
MaxR(H)—maximum reliability.

Table 6. Conﬁrmatory factor analysis ﬁt estimates.

Type

Absolute Fit

Incremental Fit

Parsimonious Fit

Indices

RMSEA
SRMR

CFI
NFI
χ2/df

Estimate

Threshold

0.039
0.045

0.991
0.961

1.301

<0.06 [73]
<0.08 [85]

>0.95 [86]
>0.95 [85]

1 to 3 [85]

Note: RMSEA—Root Mean Square Error of Approximation; SRMR—Standardized Root Mean Square Residua;
CFI—Comparative Fit Index; NFI—Normed Fit Index; χ2/df—Chi-squared per Degrees of Freedom

4.4. Structural Equation Modelling

A signiﬁcant and good-ﬁtting model was achieved from the 2000 bootstrapped SEM
run. As summarized in Table 7, all representative measures from the three types of ﬁt
belong to the threshold limit. This highlighted the consistency of the data and its ability
to reproduce the hypothesized relationship. Further, there were no suggested additional
structural links from the main variables symbolizing a rigid model structure.

---

<!-- PAGE 14 -->

Informatics 2023, 10, 32

14 of 24

Table 7. Structural equation model ﬁt estimates.

Type

Absolute Fit

Incremental Fit

Parsimonious Fit

Indices

RMSEA
SRMR

CFI
NFI
χ2/df

Estimate

Threshold

0.051
0.045

0.988
0.966

1.524

<0.06 [73]
<0.08 [87]

>0.95 [86]
>0.95 [85]

1 to 3 [85]

Note: RMSEA—Root Mean Square Error of Approximation; SRMR—Standardized Root Mean Square Residual;
CFI—Comparative Fit Index; NFI—Normed Fit Index; χ2/df—Chi-squared per Degrees of Freedom.

4.4.1. Mediation Effect Analysis

Results identiﬁed that both affective and cognitive elements function as mediators
in the trust and reliance calibration process from XAI (see Table 8). For affect, anxiously
suspicious was the only insigniﬁcant mediator. Interestingly surprised mediates the appre-
ciation of the explanation form, trusting mediates explanation form and supplementary
information, and communication style and supplementary information for fearfully dis-
mayed. Relating to reliance, the insigniﬁcance of anxiously suspicious was still seen with
the path coming from it when mediated by perceived trust. As for the cognitive paths,
all proposed mediation of perceived trust and usefulness from the design elements were
signiﬁcant. Overall, these ﬁndings highlight the initial proposed idea from the study that
affective path calibration exists in the use of XAI.

Table 8. Mediation effect analysis.

Group

From

Mediator

To

Std. Est.

p-Value

Mediated? a

Explanation Form

Affective Trust

Communication Style

Supplementary Information

Interestingly Surprised
Trusting
Fearfully Dismayed
Anxiously Suspicious

Explanation Form
Communication Style
Supplementary Information

Affective Reliance

Cognitive Trust

Interestingly Surprised
Trusting
Fearfully Dismayed
Anxiously Suspicious

Interestingly Surprised
Trusting
Fearfully Dismayed
Anxiously Suspicious

Interestingly Surprised
Trusting
Fearfully Dismayed
Anxiously Suspicious

Perceived Trust

Perceived Trust

Perceived Trust

Perceived Trust

Reliance

Perceived Usefulness

Perceived Trust

Cognitive Reliance

Perceived Usefulness

Perceived Trust

Reliance

Note: Std. Est.—Standard Estimate; a Evaluated at p-value < 0.05.

0.289
0.163
−0.020
0.001

−0.015
−0.037
−0.108
−0.017

0.064
0.078
0.068
0.005

0.239
0.171
−0.070
−0.010

0.023
0.211
0.010

−0.099

0.001
0.001
0.159
0.523

0.489
0.067
0.015
0.527

0.068
0.046
0.020
0.475

0.001
0.001
0.013
0.509

0.009
0.008
0.036

0.007

Yes
Yes
No
No

No
No
Yes
No

No
Yes
Yes
No

Yes
Yes
Yes
No

Yes
Yes
Yes

Yes

4.4.2. Direct Effect Analysis

Considering the results from the mediation analysis, relationships and design recom-
mendations were successfully drawn from the direct effect analysis. Of the 21 hypothesized
direct relationships, only 12 were identiﬁed to be statistically supported (see Table 9). As
for the design to emotions group, explanation form signiﬁcantly relates to interestingly
surprised and trusting emotions. Communication style was signiﬁcant to affect fearfully
dismayed and anxiously suspicious. Lastly, the presence of supplementary information
decreases fearfully dismayed.

---

<!-- PAGE 15 -->

Informatics 2023, 10, 32

15 of 24

Table 9. Direct effect analysis.

Group

From

To

Std. Est.

p-Value

Supported a

Explanation Form
(+Example, −Feature, Rule)

Design to Emotions

Communication Style
(+Logic, −Human)

Supplementary Information
(+With, −Without)

Interestingly Surprised
Trusting
Fearfully Dismayed
Anxiously Suspicious

Supplementary Information
Communication Style
Explanation Form

Emotions to Trust

Design to Usefulness

Interestingly Surprised
Trusting
Fearfully Dismayed
Anxiously Suspicious

Interestingly Surprised
Trusting
Fearfully Dismayed
Anxiously Suspicious

Interestingly Surprised
Trusting
Fearfully Dismayed
Anxiously Suspicious

Perceived Trust

Perceived Usefulness

Usefulness to Trust

Perceived Usefulness

Perceived Trust

Trust to Reliance

Perceived Trust

Reliance

0.530
0.419
0.126
−0.032

−0.070
−0.257
1.822
1.783

0.117
0.201
−0.432
−0.227

0.545
0.390
−0.158
−0.024

0.045
−0.940
0.100

0.225

0.439

0.001
0.002
0.339
0.806

0.488
0.081
0.001
0.001

0.068
0.053
0.006
0.059

0.001
0.001
0.017
0.539

0.224
0.002
0.006

0.007

0.001

Yes
Yes
No
No

No
No
Yes
Yes b

No
No
Yes
No

Yes
Yes
Yes
No
No c
Yes
Yes

Yes

Yes

Note: Std. Est.—Standard Estimate; a Evaluated at p-value < 0.05; b unsupported from the mediation analysis;
c supported from the mediation analysis.

For emotion to trust, all emotions aside from anxiously suspicious have a signiﬁcant
relationship to perceived trust. Particularly, users that felt interestingly surprised and
trusting reported higher perceived trust, while reporting the opposite when fearfully
dismayed was felt. As for the cognitive-based groups, perceived usefulness has a positive
relationship with perceived trust. This stemmed from explanation form and communication
style design elements being signiﬁcant. Supplementary information, although identiﬁed be
part of the mediated path, was insigniﬁcant for the direct test showing the possibility of
partial mediation [88]. Lastly, perceived trust has a signiﬁcant positive relationship with
reliance. Given that each design was dichotomously coded for the analysis, translating the
results to design means

•

•

•

Example-based explanation increases interestingly surprised, trusting emotions, and
perceived usefulness, while feature- and rule-based explanation decreases them.
Logic robotic increases fearfully dismayed plus anxiously suspicious emotions and de-
creases perceived usefulness, while humanized communication functions the opposite.
The presence of supplementary information decreases fearfully dismayed emotions,
while the absence of it increases the effect.

4.4.3. Moderation Effect Analysis

Only half of the moderators were identiﬁed to have a signiﬁcant effect. As shown
in Table 10, the nested comparisons for AI anxiety and incidental emotions for human
factors, while reliability and experience for the AI factors received a p-value less than
0.05, highlighted the substantial concurring difference from the full default model. With
these results, deeper analysis was performed to identify the source of moderation on a
per-path basis.

---

<!-- PAGE 16 -->

Informatics 2023, 10, 32

16 of 24

Table 10. Global multi-group moderation effect analysis.

Group

Moderation Model

Human Factors

AI Factors

AI Anxiety
Incidental Emotion
Trust Disposition
XAI Experience

AI Reliability
Learning Capability
Brand
Experience

DF

21.000
21.000
21.000
21.000

21.000
21.000
21.000
21.000

CMIN

41.212
63.314
21.940
22.810

73.497
16.260
13.083
34.021

p-Value

Moderated? a

0.005
0.000
0.403
0.354

0.000
0.755
0.906
0.036

Yes
Yes
No
No

Yes
No
No
Yes

Note: DF—Degrees of Freedom; CMIN—Chi-square statistics; p-value—Signiﬁcance;
p-value < 0.05.

a Evaluated at

The results from the individual ﬁt test for all moderation runs also favored the global
results. As shown in Table 11, the CFI, SRMR, and PClose all passed the thresholds assuring
capability for further exploration. Take note that these are the measures used considering
the data were truncated due to the stratiﬁcation. More so, these are insensitive with low
sample size and corresponding degrees of freedom [87,89].

Table 11. Local moderation test ﬁt scores.

Group

Moderation Model

Runs

Human Factors

AI Anxiety

Incidental Emotion

High AI Anxiety
Low AI Anxiety
Positive Incidental Emotion
Negative Incidental Emotion

AI Factors

AI Reliability

Experience

High AI Reliability
Low AI Reliability
Short Experience
Long Experience

CFI

0.986
1.000
1.000
0.994

1.000
0.952
1.000
0.994

SRMR

PClose

Fit? a

0.032
0.021
0.008
0.028

0.014
0.051
0.008
0.028

0.054
0.754
0.892
0.283

0.587
0.050
0.892
0.283

Yes
Yes
Yes
Yes

Yes
Yes
Yes
Yes

Note: CFI—Comparative Fit Index; SRMR—Standardized Root Mean Square Residual; PClose—p of close ﬁt;
a Considered ﬁt if all measures passed the threshold: CFI > 0.95, SRMR < 0.08, PClose > 0.05 [85].

The local effect surfaced varying degrees of moderation per relationship, as presented
in Table 12. For AI anxiety, the difference seen was mainly that values are higher with the
low group than with the high group in three key areas. First, when fearfully dismayed
emotions were felt, users with high AI anxiety experienced lower perceived trust than those
who have low AI anxiety (β = −0.059 vs. β = 0.021, z-score = 2.195 and p-value = 0.014).
Second, when exposed to a logic-robotic communication style, users in the high group have
lower perceived usefulness than the low group (β = 0.804 vs. β = 1.185, z-score = 1.762
and p-value = 0.039). Lastly, for the relationship between perceived trust and reliance,
users in the high group have lower reliance than the low group (β = 0.804 vs. β = 1.185,
z-score = 1.762 and p-value = 0.039).

Table 12. Local multi-group moderation difference effect analysis.

From

To

Est.

p-Value

Est.

p-Value

z-Score

p-Value a

Fearfully Dismayed
Communication Style
Perceived Trust

Perceived Trust
Perceived Usefulness
Reliance

High AI Anxiety
−0.059
−0.970
0.804

0.044
0.000
0.000

Low AI Anxiety
0.331
0.021
−0.790
0.000
0.000
1.185

2.195
2.442
1.762

0.014
0.007
0.039

---

<!-- PAGE 17 -->

Informatics 2023, 10, 32

17 of 24

Table 12. Cont.

From

To

Est.

p-Value

Est.

p-Value

z-Score

p-Value a

Supplementary Information
Supplementary Information
Trusting
Fearfully Dismayed
Communication Style
Perceived Usefulness

Interestingly Surprised
Trusting
Perceived Trust
Perceived Trust
Perceived Usefulness
Perceived Trust

Trusting
Fearfully Dismayed

Perceived Trust
Perceived Trust

Trusting
Fearfully Dismayed

Perceived Trust
Perceived Trust

Pos. Inci. Emotion
−0.979
0.026
−1.001
0.032
−0.017
0.681
−0.045
0.148
−1.058
0.000
0.029
0.196

High AI Reliability
0.076
0.064
−0.073
0.026

Short Experience
0.184
0.018

0.000
0.177

Neg. Inci. Emotion
0.209
0.457
0.725
0.137
0.000
0.174
0.035
0.023
−0.875
0.000
0.331
0.028

Low AI Reliability
0.000
0.223
0.250
0.027

Long Experience
0.012
0.095
−0.046
0.117

2.513
1.868
4.081
2.071
2.096
1.780

3.416
2.479

1.859
1.987 b

0.006
0.031
0.000
0.019
0.018
0.038

0.000
0.007

0.032
0.023

Note: Pos.—Positive; Neg.—Negative; Inci.—Incidental; Est.—Unstandardized Estimate; a Evaluated at
p-value < 0.05; b Signiﬁcant z-score difference and p-value but with insigniﬁcant per moderated run estimates.

For incidental emotions, six paths were identiﬁed to be signiﬁcantly moderated. In
terms of dampening effect, when supplementary information was provided, users with pos-
itive incidental emotions experienced lower interestingly surprised and trusting emotions
than those with negative (β = −0.979 vs. β = 0.457, z-score = 2.513 and p-value = 0.006 and
β = −1.001 vs. β = 0.137, z-score = 1.868 and p-value = 0.031). Next, the effect of perceived
trust is lower for the positive group than the negative group when trusting and fearfully
dismayed emotions were felt (β = −0.017 vs. β = 0.174, z-score = 4.081 and p-value = 0.000
and β = −0.045 vs. β = 0.023, z-score = 2.071 and p-value = 0.019). Both conditions highlight
that positive incidental emotions resulted in a decrease in effect towards supplementary in-
formation and perceived trust. In contrary, there are also ampliﬁcation effects that surfaced
from the moderation. First when logic-robotic communication style was used, the nega-
tive group had a higher perception of usefulness than the positive group (β = −0.875 vs.
β = −1.058, z-score = 2.096 and p-value = 0.018). In addition, perceived trust was higher in
the positive group relative to perceived usefulness (β = 0.196 vs. β = 0.028, z-score = 1.780
and p-value = 0.038).

Aside from incidental emotion, the same moderated paths for reliability and experi-
ence were determined. Speciﬁcally, these are the affective paths from trusting and fearfully
dismayed emotion to perceived trust. For both instances, low AI reliability and short experi-
ence have higher perceived trust when trusting (β = 0.223 vs. β = 0.064, z-score = 3.416 and
p-value = 0.000; β = 0.184 vs. β = 0.095, z-score = 1.859 and p-value = 0.032) and fearfully
dismayed emotions (β = 0.027 vs. β = −0.073, z-score = 2.479 and p-value = 0.007; β = 0.018
vs. β = −0.046, z-score = 1.987 and p-value = 0.023) were experienced.

5. Discussion

Considering the quantitative results from the experiment and subsequent interviews,
the study was able to successfully analyze the postulated objectives for the end-user
XAI consideration.

5.1. Objective 1: Conﬁrmation of Affective Trust Calibration for XAI

Affect was determined to be a variable route for trust calibration. This was established
through the causal relationship test, anchored on the mediation analysis of the SEM. No-
tably, emotions belonging to the group of interestingly surprised (e.g., interested, excited,
surprised, pleased, and amazed), trusting (e.g., happy, conﬁdent, secure, proud, and trust-
ing), and fearfully dismayed (e.g., dismayed, afraid, fear, angry, and sad) were identiﬁed
to be signiﬁcant mediators for trust and reliance in a behavioral and use change view.
On the other hand, anxiously suspicious (e.g., suspicious, concerned, confused, nervous,

---

<!-- PAGE 18 -->

Informatics 2023, 10, 32

18 of 24

and anxious) emotions were unsupported. In terms of relationships, both interestingly
surprised and trusting emotions have a positive relation to trust, while fearfully dismayed
observe a negative stance. All of these were validated jointly with the signiﬁcant mediation
of the cognitive route showing that trust calibration can happen on the two routes.

Insights from the interview also second the conﬁrmation of the variability of the
affective route alongside the cognitive route. By synthesizing the claims, distinctively,
participants can be divided into two types: people who value emotions and people who
value information. The former works when intuition or perception were the mode of
assessment, while the latter when information quality deliberation happens. This obser-
vation resonates with the elaboration likelihood model (ELM) of persuasion of Petty and
Cacioppo [90], which is essentially a theory about the thinking process in the context of
persuasion variables. Contextually, this is called the central route when high elaboration
happens on the detail presented, while peripheral when low. Further, the interview also
uncovered the same consideration of motivation and ability from ELM which dictates what
route of trust calibration the user will follow. If they have high motivation (i.e., invested in
the task reward, high curiosity with the XAI, aiming for a high score in the experiment)
and high ability (i.e., understanding of the information on XAI, perceived expertise with
the task), they will follow a cognitive path or central route, and affective or peripheral for
the opposite.

Overall, these ﬁndings offset the running hypothesis on how XAI induces trust as
determined in previous review studies [8,24]. This shows that XAI works similarly to other
cues in the ﬁeld of HCI that transverse on both trust calibration routes. Considering this
study is a pioneer for testing the affective route, further studies can work on measuring
such elaboration to analyze the differences in various contexts to ultimately check the
variability of each route.

5.2. Objective 2: Effect of Different XAI Designs and Importance of End-User Centric Approach

For the design, two important observations were recognized. First, the pre-study was
able to identify that certain design elements are being considered in the utility assessment
of an XAI. From the survey, explanation form, communication style, and use of supplemen-
tary information rest on the top of the perceived important design element list. Notably,
reasoning from the interview showed that these are selected as they provide the ability
to see the rules AI rules, give an idea of the information used in such decision-making,
and learn the details of the process. This shows that perceived important XAI design
mainly echoes the original purpose of XAI among other things. For example, aesthetics
can be considered. Text size and color are design elements but only very few noted their
importance as they do not perform a critical role in explaining.

The next observation is that XAI design elements play a signiﬁcant role both for the
affective and cognitive trust calibration route, with changing each conﬁguration producing
different results. As deduced via SEM, design change will yield distinctive effects on
emotions and cognitive evaluation (see Table 13 for the summary of effects). The varying
effect theoretically implies that for XAI, design functions on a deeper level—a micro view
as conﬁguration rather than a macro view through categorical effect.

The key ﬁndings support and explain the signiﬁcant elaboration routes and ELM
parallelism reﬂected in the ﬁrst objective. The second objective unfolds that in the de-
velopment of XAI, aside from the information it carries, the design also matters. More
so, the common consensus highlights the subsistence of a general structure for possible
design prioritization when developing an XAI. This means that the identiﬁed effects can be
leveraged to create a targeted XAI for an optimized utility function for an XAI. For example,
to increase trust and reliance, an XAI featuring an example-based explanation form can be
tapped to have a positive change to interestingly surprised and trusting emotions, or can
use human-like communication to simply remove the feeling of fearfully dismayed and
anxiously suspicious emotions. Overall, the observations shed light on the importance of
design and its variability for an end-user-centric XAI.

---

<!-- PAGE 19 -->

Informatics 2023, 10, 32

19 of 24

Table 13. Summary of affect and cognitive change per design element.

Design Element

Type

Explanation Form

Example
Feature and Rule

Communication Style

Supplementary Information

Logic
Human

With
Without

Interestingly
Surprised

Trusting

Fearfully
Dismayed

Anxiously
Suspicious

Perceived
Usefulness

+
−

×
×

×
×

+
−

×
×

×
×

×
×

+
−

−
+

×
×

+
−

×
×

+
−

−
+

×
×

Note: “+” means increasing; “−” means decreasing; “×” unsupported relationship.

5.3. Objective 3: External Factors Delimiting XAI Effect

The results also identiﬁed that external factors are a point worth noting when devel-
oping an XAI, with both human (i.e., AI anxiety and incidental emotions) and AI factors
(i.e., reliability and experience) being viable. This implies that XAI utility effectiveness
works beyond the design and information as situational factors are also signiﬁcant. For
example, supplementary information will only cause a signiﬁcant negative affective change
on interestingly surprised if they have positive incidental emotions. Viewing the XAI
development in this light further denotes that to mitigate transparency, design should be
contextualized on the situational need of the implementation.

In addition, commentaries from the interview suggest that the moderation works on
a per AI-type experience basis. For example, a user with a bad experience with image
recognition carried this in the experiment with higher anxiety, negative incidental emotion,
and lower perception of the AI reliability, even though they have a good experience relative
to the other types. This infers that XAI, being a complementary element, was evaluated
after the AI system was assessed, opening the idea that the XAI effect might differ for other
AI use cases. A possible extension of the study can be performed to check this idea.

6. Conclusions

Explainable artiﬁcial intelligence (XAI) has successfully addressed the black box trust
problem of artiﬁcial intelligence (AI) by allowing users to gain a human-level understanding
of how AI works, even if they have limited knowledge on the complex machine learning
algorithms that power it. However, concerns that current XAI techniques have been
delimited in terms of their applicability and impact have been highlighted in the recent
years. Particularly, the exploration has determined that it focuses more on the needs of
developers and not end-users, putting AI adoption in a critical position. To provide the
necessary viewpoint, this study aimed to explore end-user-centric XAI.

For the ﬁrst objective, which aims to determine how an end-user calibrates trust from
XAI, it was identiﬁed that it not only serves as a cognitive resource but also as an affective
cue for trust and reliance change. Effectively, this study argues that XAI can be used as
an information resource and irrationally via emotions through its affective contributions.
Continuing that, another claim identiﬁed in the study is that information carried out by
the XAI is not the only determinant for both routes. The study tested and identiﬁed
that design—or manner by which XAI is presented—can also alter its effectiveness. This
answers the second objective regarding the factors that can viably change trust from an
XAI. Lastly, as for the third and fourth objective, which looked on the moderating factors
in the trust calibration process, evidence showed that human and AI factors were capable
to inﬂuence the effect. This includes anxiety and incidental emotion for the former, while
AI reliability and experience for the latter. Overall, the study successfully ﬁlled in the
theoretical gap acknowledged from the research stream. It opened a new understanding of
the routes by which XAI calibrates trust, the importance of its design, and external factors
that may alter its effectiveness.

---

<!-- PAGE 20 -->

Informatics 2023, 10, 32

20 of 24

6.1. Implications

Considering the ﬁndings from the study, several implications can be drawn both in
theoretical and managerial landscapes. For theoretical, as this study viably determined that
XAI also functions in the affective trust route, it opens a new path of research regarding
XAI effectiveness and subsequently poses important delimitation on previous research
that only approached calibration through cognitive route. Possibly, revisiting such studies
can be carried out to ﬁrm up the ﬁndings relative to the importance of integral emotions.
In terms of development, the study also creates a new paradigm on the course of XAI
improvement research.

For the managerial, the results create a better position for the implementors and users.
For the former, developers and designers can use the ﬁndings on how to better leverage
the effect of XAI towards trust. For instance, they can reorient the XAI to induce more
positive emotions or use XAI more on systems where the primary customers are those with
high anxiety (e.g., telehealth applications, banking, security, driving). Moving on, for the
users, if the results are operationalized, they can have a better interaction with AI systems,
possibly allowing effective adoption.

Aside from the positive implications, another side that can be drawn from the results
is the possibility of misusing XAI. From the ﬁndings, it highlights that not all users use
XAI as an information resource for mental model calibration; some only use it as a cue. In
addition, design can manipulate emotions that later affect trust and reliance. In this chain,
faulty and manipulative XAI can be simply shown in the system and be effective if the
design can produce a positive effect on the user.

6.2. Limitations and Direction for Future Research

Although the study has ﬁlled in an important research gap and has followed a well-
planned methodology, there have been limitations that should be addressed for future
research. First, the study can be extended and retested under different domains. This is
recommended to strengthen the claims from the study and to identify the limitations of
the relationship. Possibly, different purpose, level of sensitivity, and stakeholders can be
viewed. In line with that, secondly, the study can be expanded to check on other types
of XAI other than the tested type in the study. In the experiment, the focus has been on
visual imagery type since it complements the nature of the AI system selected (i.e., image
recognition). Other types such as tree diagrams or textual can be tested. Third, moderator
testing can be improved by expanding its limits. For instance, the experience can be viewed
for a longer time frame (e.g., 2 weeks) to have a broader and more realistic view of the
relationships. This is recommended as the post-interview surfaced it on multiple occasions.
Lastly, a cross demographical view can be conducted to check on differences between less
and highly adopted AI communities as this directly affects the use of XAI.

Author Contributions: Conceptualization, E.B. and R.S.; methodology, E.B. and R.S.; experiment
testbed, E.B.; validation, E.B. and R.S.; formal analysis, E.B.; investigation, E.B.; data curation, E.B.;
writing—original draft preparation, E.B.; writing—review and editing, E.B.; visualization, E.B.;
supervision, R.S.; project administration, E.B. and R.S.; funding acquisition, E.B. and R.S. All authors
have read and agreed to the published version of the manuscript.

Funding: This research and the APC were funded by De La Salle University—Manila.

Institutional Review Board Statement: The ethical aspects of this research have been approved by
the Social Science Ethics Review Board (SSERB) of the Philippine Social Science Council (Reference
Code: CB-22-20 on 27 June 2022).

Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.

Data Availability Statement: Data are not publicly available, though the data may be made available
on request from the corresponding author.

---

<!-- PAGE 21 -->

Informatics 2023, 10, 32

21 of 24

Acknowledgments: The research team would like to acknowledge 80/20 Design Labs for their help
in the development of the experiment testbed, Angelimarie Miguel and Wira Madria for their aid
in the data curation and processing, and Naomi Bernardo, Edgardo Bernardo, Noel Bernardo, and
Christiane Willits for their technical support and material donations used in the experiment.

Conﬂicts of Interest: The authors declare no conﬂict of interest. The funders had no role in the design
of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or
in the decision to publish the results.

References

1.

2.

3.
4.
5.
6.
7.

8.

Lu, Y. Artiﬁcial Intelligence: A Survey on Evolution, Models, Applications and Future Trends. J. Manag. Anal. 2019, 6, 1–29.
[CrossRef]
Jordan, M.I.; Mitchell, T.M. Machine Learning: Trends, Perspectives, and Prospects. Science 2015, 349, 255–260. [CrossRef]
[PubMed]
Rai, A. Explainable AI: From Black Box to Glass Box. J. Acad. Mark. Sci. 2020, 48, 137–141. [CrossRef]
Doshi-Velez, F.; Kim, B. Towards A Rigorous Science of Interpretable Machine Learning. arXiv 2017, arXiv:1702.08608.
Castelvecchi, D. Can We Open the Black Box of AI? Nat. News 2016, 538, 4. [CrossRef]
Schmidt, P.; Biessmann, F. Quantifying Interpretability and Trust in Machine Learning Systems. arXiv 2019, arXiv:1901.08558.
Kliegr, T.; Bahník, Š.; Fürnkranz, J. A Review of Possible Effects of Cognitive Biases on Interpretation of Rule-Based Machine
Learning Models. Artif. Intell. 2021, 295, 103458. [CrossRef]
Linardatos, P.; Papastefanopoulos, V.; Kotsiantis, S. Explainable AI: A Review of Machine Learning Interpretability Methods.
Entropy 2020, 23, 18. [CrossRef] [PubMed]

9. Weitz, K.; Hassan, T.; Schmid, U.; Garbas, J.-U. Deep-Learned Faces of Pain and Emotions: Elucidating the Differences of Facial

Expressions with the Help of Explainable AI Methods. TM Tech. Mess. 2019, 86, 404–412. [CrossRef]

10. Preece, A. Asking ‘Why’ in AI: Explainability of Intelligent Systems—Perspectives and Challenges. Intell. Sys. Acc. Fin. Manag.

2018, 25, 63–72. [CrossRef]

11. Venkatesh, V. Adoption and Use of AI Tools: A Research Agenda Grounded in UTAUT. Ann. Oper. Res. 2022, 308, 641–652.

[CrossRef]

12. Chowdhary, K.R. Fundamentals of Artiﬁcial Intelligence; Springer: New Delhi, India, 2020; ISBN 978-81-322-3970-3.
13. Lewis, M.; Li, H.; Sycara, K. Deep Learning, Transparency, and Trust in Human Robot Teamwork. In Trust in Human-Robot

Interaction; Elsevier: Amsterdam, The Netherlands, 2021; pp. 321–352. ISBN 978-0-12-819472-0.
Savage, N. Breaking into the Black Box of Artiﬁcial Intelligence. Nature 2022. [CrossRef]

14.
15. Mohseni, S.; Zarei, N.; Ragan, E.D. A Multidisciplinary Survey and Framework for Design and Evaluation of Explainable AI

Systems. ACM Trans. Interact. Intell. Syst. 2021, 11, 1–45. [CrossRef]

16. Barredo Arrieta, A.; Díaz-Rodríguez, N.; Del Ser, J.; Bennetot, A.; Tabik, S.; Barbado, A.; Garcia, S.; Gil-Lopez, S.; Molina, D.;
Benjamins, R.; et al. Explainable Artiﬁcial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward
Responsible AI. Inf. Fusion 2020, 58, 82–115. [CrossRef]
Singh, A.; Sengupta, S.; Lakshminarayanan, V. Explainable Deep Learning Models in Medical Image Analysis. J. Imaging 2020,
6, 52. [CrossRef]

17.

18. Miller, T.; Howe, P.; Sonenberg, L. Explainable AI: Beware of Inmates Running the Asylum Or: How I Learnt to Stop Worrying

and Love the Social and Behavioural Sciences. arXiv 2017, arXiv:1712.00547. [CrossRef]

19. Lopes, P.; Silva, E.; Braga, C.; Oliveira, T.; Rosado, L. XAI Systems Evaluation: A Review of Human and Computer-Centred

Methods. Appl. Sci. 2022, 12, 9423. [CrossRef]

20. Alicioglu, G.; Sun, B. A Survey of Visual Analytics for Explainable Artiﬁcial Intelligence Methods. Comput. Graph. 2022, 102,

502–520. [CrossRef]

21. Zhang, Z.; Zhao, L.; Yang, T. Research on the Application of Artiﬁcial Intelligence in Image Recognition Technology. J. Phys. Conf.

Ser. 2021, 1992, 032118. [CrossRef]

22. Arun, N.; Gaw, N.; Singh, P.; Chang, K.; Aggarwal, M.; Chen, B.; Hoebel, K.; Gupta, S.; Patel, J.; Gidwani, M.; et al. Assessing
the Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging. Radiol. Artif. Intell. 2021, 3, e200267.
[CrossRef]

23. Zhang, J.; Chao, H.; Dasegowda, G.; Wang, G.; Kalra, M.K.; Yan, P. Overlooked Trustworthiness of Saliency Maps. In Medical Image
Computing and Computer Assisted Intervention—MICCAI 2022; Wang, L., Dou, Q., Fletcher, P.T., Speidel, S., Li, S., Eds.; Lecture
Notes in Computer Science; Springer Nature: Cham, Switzerland, 2022; Volume 13433, pp. 451–461. ISBN 978-3-031-16436-1.

24. Adadi, A.; Berrada, M. Peeking Inside the Black-Box: A Survey on Explainable Artiﬁcial Intelligence (XAI). IEEE Access 2018, 6,

52138–52160. [CrossRef]

25. Haque, A.B.; Islam, A.K.M.N.; Mikalef, P. Explainable Artiﬁcial Intelligence (XAI) from a User Perspective: A Synthesis of Prior

26.

Literature and Problematizing Avenues for Future Research. Technol. Forecast. Soc. Chang. 2023, 186, 122120. [CrossRef]
Shin, D. The Effects of Explainability and Causability on Perception, Trust, and Acceptance: Implications for Explainable AI. Int.
J. Hum. Comput. Stud. 2021, 146, 102551. [CrossRef]

---

<!-- PAGE 22 -->

Informatics 2023, 10, 32

22 of 24

27. Rudin, C.; Radin, J. Why Are We Using Black Box Models in AI When We Don’t Need To? A Lesson From An Explainable AI

28.

29.

30.

Competition. Harv. Data Sci. Rev. 2019, 1. [CrossRef]
Förster, M.; Hühn, P.; Klier, M.; Kluge, K. User-Centric Explainable AI: Design and Evaluation of an Approach to Generate
Coherent Counterfactual Explanations for Structured Data. J. Decis. Syst. 2022, 1–32. [CrossRef]
Ferreira, J.J.; Monteiro, M. Designer-User Communication for XAI: An Epistemological Approach to Discuss XAI Design. arXiv
2021, arXiv:2105.07804. [CrossRef]
Silva, A.; Schrum, M.; Hedlund-Botti, E.; Gopalan, N.; Gombolay, M. Explainable Artiﬁcial Intelligence: Evaluating the Objective
and Subjective Impacts of XAI on Human-Agent Interaction. Int. J. Hum. Comput. Interact. 2022, 1–15. [CrossRef]

31. Cirqueira, D.; Helfert, M.; Bezbradica, M. Towards Design Principles for User-Centric Explainable AI in Fraud Detection. In
Artiﬁcial Intelligence in HCI; Degen, H., Ntoa, S., Eds.; Lecture Notes in Computer Science; Springer International Publishing:
Cham, Switzerland, 2021; Volume 12797, pp. 21–40. ISBN 978-3-030-77771-5.

32. Chari, S.; Seneviratne, O.; Gruen, D.M.; Foreman, M.A.; Das, A.K.; McGuinness, D.L. Explanation Ontology: A Model of
Explanations for User-Centered AI. In The Semantic Web—ISWC 2020; Pan, J.Z., Tamma, V., d’Amato, C., Janowicz, K., Fu, B.,
Polleres, A., Seneviratne, O., Kagal, L., Eds.; Lecture Notes in Computer Science; Springer International Publishing: Cham,
Switzerland, 2020; Volume 12507, pp. 228–243. ISBN 978-3-030-62465-1.

33. Chromik, M.; Butz, A. Human-XAI Interaction: A Review and Design Principles for Explanation User Interfaces. In Human-
Computer Interaction—INTERACT 2021; Ardito, C., Lanzilotti, R., Malizia, A., Petrie, H., Piccinno, A., Desolda, G., Inkpen, K., Eds.;
Lecture Notes in Computer Science; Springer International Publishing: Cham, Switzerland, 2021; Volume 12933, pp. 619–640.
ISBN 978-3-030-85615-1.

34. Liao, Q.V.; Varshney, K.R. Human-Centered Explainable AI (XAI): From Algorithms to User Experiences.

arXiv 2021,

arXiv:2110.10790.

35. Gan, Y.; Ji, Y.; Jiang, S.; Liu, X.; Feng, Z.; Li, Y.; Liu, Y. Integrating Aesthetic and Emotional Preferences in Social Robot Design: An
Affective Design Approach with Kansei Engineering and Deep Convolutional Generative Adversarial Network. Int. J. Ind. Ergon.
2021, 83, 103128. [CrossRef]

36. Nawaratne, R. Human-Centric Product Design with Kansei Engineering and Artiﬁcial Intelligence. Available online: https:
//towardsdatascience.com/human-centric-product-design-with-kansei-engineering-and-artiﬁcial-intelligence-f38cb3c0f26d
(accessed on 21 December 2021).

37. Wang, D.; Yang, Q.; Abdul, A.; Lim, B.Y. Designing Theory-Driven User-Centric Explainable AI. In Proceedings of the 2019 CHI
Conference on Human Factors in Computing Systems, Glasgow Scotland, UK, 2 May 2019; ACM: New York, NY, USA, 2019;
pp. 1–15.

38. Lee, J.D.; See, K.A. Trust in Automation: Designing for Appropriate Reliance. Hum. Factors 2004, 46, 50–80. [CrossRef]
39. Hoff, K.A.; Bashir, M. Trust in Automation: Integrating Empirical Evidence on Factors That Inﬂuence Trust. Hum. Factors 2015, 57,

407–434. [CrossRef] [PubMed]

40. Kramer, R.M. Trust and Distrust in Organizations: Emerging Perspectives, Enduring Questions. Annu. Rev. Psychol. 1999, 50,

569–598. [CrossRef] [PubMed]

41. Lewis, J.D.; Weigert, A. Trust as a Social Reality. Soc. Forces 1985, 63, 967. [CrossRef]
42. McAllister, D.J. Affect- and Cognition-Based Trust as Foundations for Interpersonal Cooperation in Organizations. Acad. Manag.

J. 1995, 38, 24–59. [CrossRef]

43. Panksepp, J. Affective Consciousness: Core Emotional Feelings in Animals and Humans. Conscious. Cogn. 2005, 14, 30–80.

44.

45.

[CrossRef]
Schwarz, N.; Bless, H.; Bohner, G. Mood and Persuasion: Affective States Inﬂuence the Processing of Persuasive Communications.
In Advances in Experimental Social Psychology; Elsevier: Amsterdam, The Netherlands, 1991; Volume 24, pp. 161–199. ISBN
978-0-12-015224-7.
Forlizzi, J.; Battarbee, K. Understanding Experience in Interactive Systems. In Proceedings of the 2004 Conference on Designing
Interactive Systems Processes, Practices, Methods, and Techniques—DIS ’04, Cambridge, MA, USA, 1–4 August 2004; ACM Press:
New York, NY, USA, 2004; p. 261.

46. Van Gorp, T.; Adams, E. Design for Emotion; Morgan Kaufmann: Waltham, MA, USA, 2012; ISBN 978-0-12-386531-1.
47. Madsen, M.; Gregor, S. Measuring Human-Computer Trust; Australasian Association for Information System: Wales, Australia,

2000; Volume 53, pp. 6–8.

50.

48. Myers, C.D.; Tingley, D. The Inﬂuence of Emotion on Trust. Polit. Anal. 2016, 24, 492–500. [CrossRef]
49.

Jin, N.; Merkebu, J. The Role of Employee Attractiveness and Positive Emotion in Upscale Restaurants. Anatolia 2015, 26, 284–297.
[CrossRef]
Jensen, T.; Khan, M.M.H.; Albayram, Y.; Fahim, M.A.A.; Buck, R.; Coman, E. Anticipated Emotions in Initial Trust Evaluations of
a Drone System Based on Performance and Process Information. Int. J. Hum. Comput. Interact. 2020, 36, 316–325. [CrossRef]
51. Albayram, Y.; Khan, M.M.H.; Jensen, T.; Buck, R.; Coman, E. The Effects of Risk and Role on Users’ Anticipated Emotions in
Safety-Critical Systems. In Engineering Psychology and Cognitive Ergonomics; Harris, D., Ed.; Lecture Notes in Computer Science;
Springer International Publishing: Cham, Switzerland, 2018; Volume 10906, pp. 369–388. ISBN 978-3-319-91121-2.

---

<!-- PAGE 23 -->

Informatics 2023, 10, 32

23 of 24

52. Guerdan, L.; Raymond, A.; Gunes, H. Toward Affective XAI: Facial Affect Analysis for Understanding Explainable Human-
AI Interactions. In Proceedings of the 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
(CVPRW), Nashville, TN, USA, 19–25 June 2021; Volume 10, pp. 3796–3805.

53. Phillips, R.; Madhavan, P. The Role of Affective Valence and Task Uncertainty in Human-Automation Interaction. Proc. Hum.

Factors Ergon. Soc. Annu. Meet. 2013, 57, 354–358. [CrossRef]

54. Gompei, T.; Umemuro, H. Factors and Development of Cognitive and Affective Trust on Social Robots. In Social Robotics; Ge, S.S.,
Cabibihan, J.-J., Salichs, M.A., Broadbent, E., He, H., Wagner, A.R., Castro-González, Á., Eds.; Lecture Notes in Computer Science;
Springer International Publishing: Cham, Switzerland, 2018; Volume 11357, pp. 45–54. ISBN 978-3-030-05203-4.

55. Buck, R.; Khan, M.; Fagan, M.; Coman, E. The User Affective Experience Scale: A Measure of Emotions Anticipated in Response

to Pop-Up Computer Warnings. Int. J. Hum. Comput. Interact. 2018, 34, 25–34. [CrossRef]

56. Bernardo, E.; Tangsoc, J. Explanatory Modelling of Factors Inﬂuencing Adoption of Smartphone Shopping Application. IEMS

2019, 18, 647–657. [CrossRef]

57. Chen, Q.Q.; Park, H.J. How Anthropomorphism Affects Trust in Intelligent Personal Assistants. Ind. Manag. Data Syst. 2021, 121,

2722–2737. [CrossRef]

58. Helander, M.G.; Khalid, H.M. Affective and Pleasurable Design. In Handbook of Human Factors and Ergonomics; Salvendy, G., Ed.;

John Wiley & Sons, Inc.: Hoboken, NJ, USA, 2006; pp. 543–572. ISBN 978-0-470-04820-7.

59. Khalid, H.M. Embracing Diversity in User Needs for Affective Design. Appl. Ergon. 2006, 37, 409–418. [CrossRef] [PubMed]
60. Lottridge, D.; Chignell, M.; Jovicic, A. Affective Interaction: Understanding, Evaluating, and Designing for Human Emotion. Rev.

Hum. Factors Ergon. 2011, 7, 197–217. [CrossRef]

61. Gasah, M.; Mat Zain, N.H.; Baharum, A. An Approach in Creating Positive Emotion for Children’s e-Learning Based on User

62.

Interface Design. IJEECS 2019, 13, 1267. [CrossRef]
Isbister, K. How Games Move Us: Emotion by Design; Playful Thinking; MIT Press: Cambridge, MA, USA, 2016; ISBN 978-0-262-
03426-5.

63. Gutierrez, A.M.J.; Chiu, A.S.F.; Seva, R. A Proposed Framework on the Affective Design of Eco-Product Labels. Sustainability

2020, 12, 3234. [CrossRef]

64. Dy, A.K.; Lazo, M.; Santos, A.G.; Seva, R. Affective Trash Bin Signage to Promote Waste Segregation. In Proceedings of the
21st Congress of the International Ergonomics Association (IEA 2021), Online, 13-18 June 2021; Black, N.L., Neumann, W.P.,
Noy, I., Eds.; Lecture Notes in Networks and Systems. Springer International Publishing: Cham, Switzerland, 2022; Volume 223,
pp. 20–30, ISBN 978-3-030-74613-1.

65. Norman, D.A. Emotional Design: Why We Love (or Hate) Everyday Things; Basic Books: New York, NY, USA, 2004; ISBN 978-0-465-

05135-9.
Jordan, P.W. Designing Pleasurable Products; CRC Press: Boca Raton, FL, USA, 2000; ISBN 978-1-135-73411-4.

66.
67. Khalid, H.M.; Helander, M.G. A Framework for Affective Customer Needs in Product Design. Theor. Issues Ergon. Sci. 2004, 5,

27–42. [CrossRef]

68. Bernardo, E.; Seva, R. Explainable Artiﬁcial Intelligence (XAI) Emotions Set. Appl. Sci. 2022, submitted.
69. Albayram, Y.; Jensen, T.; Khan, M.M.H.; Buck, R.; Coman, E. Investigating the Effect of System Reliability, Risk, and Role on
Users’ Emotions and Attitudes toward a Safety-Critical Drone System. Int. J. Hum. Comput. Interact. 2019, 35, 761–772. [CrossRef]
70. Du, N.; Zhou, F.; Pulver, E.M.; Tilbury, D.M.; Robert, L.P.; Pradhan, A.K.; Yang, X.J. Examining the Effects of Emotional Valence
and Arousal on Takeover Performance in Conditionally Automated Driving. Transp. Res. Part C Emerg. Technol. 2020, 112, 78–87.
[CrossRef]
Jian, J.-Y.; Bisantz, A.M.; Drury, C.G. Foundations for an Empirically Determined Scale of Trust in Automated Systems. Int.
J. Cogn. Ergon. 2000, 4, 53–71. [CrossRef]

71.

72. Kline, R.B. Principles and Practice of Structural Equation Modeling, 4th ed.; Methodology in the Social Sciences; The Guilford Press:

New York, NY, USA, 2016; ISBN 978-1-4625-2335-1.

73. Westland, C. Lower Bounds on Sample Size in Structural Equation Modeling. Electron. Commer. Res. Appl. 2010, 9, 476–487.

[CrossRef]

74. Cohen, J. Statistical Power Analysis for the Behavioral Sciences; Routledge: London, UK, 1988; ISBN 978-0-203-77158-7.
75. Angold, A.; Costello, E.J. Short Mood and Feelings Questionnaire; APA PsycNet: Washington, DC, USA, 1987. [CrossRef]
76.

Frazier, M.L.; Johnson, P.D.; Fainshmidt, S. Development and Validation of a Propensity to Trust Scale. J. Trust. Res. 2013, 3, 76–97.
[CrossRef]

77. Lowry, P.B.; Twyman, N.W.; Pickard, M.; Jenkins, J.L.; Bui, Q. “Neo” Proposing the Affect-Trust Infusion Model (ATIM) to Explain
and Predict the Inﬂuence of High and Low Affect Infusion on Web Vendor Trust. Inf. Manag. 2014, 51, 579–594. [CrossRef]
78. Hsu, S.-H.; Chen, W.; Hsieh, M. Robustness Testing of PLS, LISREL, EQS and ANN-Based SEM for Measuring Customer

Satisfaction. Total Qual. Manag. Bus. Excell. 2006, 17, 355–372. [CrossRef]

79. Henseler, J.; Ringle, C.M.; Sinkovics, R.R. The Use of Partial Least Squares Path Modeling in International Marketing. In Advances
in International Marketing; Sinkovics, R.R., Ghauri, P.N., Eds.; Emerald Group Publishing Limited: Bingley, UK, 2009; Volume 20,
pp. 277–319. ISBN 978-1-84855-468-9.

---

<!-- PAGE 24 -->

Informatics 2023, 10, 32

24 of 24

80. Chin, W.W. The Partial Least Squares Approach for Structural Equation Modeling. In Modern Methods for Business Research;
Methodology for Business and Management; Lawrence Erlbaum Associates Publishers: Mahwah, NJ, USA, 1998; pp. 295–336.
ISBN 0-8058-2677-7.

81. Yang, X.J.; Unhelkar, V.V.; Li, K.; Shah, J.A. Evaluating Effects of User Experience and System Transparency on Trust in Automation.
In Proceedings of the 2017 ACM/IEEE International Conference on Human-Robot Interaction, Vienna, Austria, 6 March 2017;
ACM: New York, NY, USA, 2017; pp. 408–416.

82. Vogt, W.P.; Johnson, R.B. The SAGE Dictionary of Statistics & Methodology: A Nontechnical Guide for the Social Sciences, 5th ed.; SAGE:

Los Angeles, CA, USA, 2016; ISBN 978-1-4833-8176-3.

83. Hair, J.F. (Ed.) Multivariate Data Analysis; Prentice Hall: Upper Saddle River, NJ, USA, 1998; ISBN 978-0-13-894858-0.
84. Taber, K.S. The Use of Cronbach’s Alpha When Developing and Reporting Research Instruments in Science Education. Res. Sci.

Educ. 2018, 48, 1273–1296. [CrossRef]

85. Hu, L.; Bentler, P.M. Cutoff Criteria for Fit Indexes in Covariance Structure Analysis: Conventional Criteria versus New

86.

Alternatives. Struct. Equ. Model. A Multidiscip. J. 1999, 6, 1–55. [CrossRef]
Schreiber, J.B.; Nora, A.; Stage, F.K.; Barlow, E.A.; King, J. Reporting Structural Equation Modeling and Conﬁrmatory Factor
Analysis Results: A Review. J. Educ. Res. 2006, 99, 323–338. [CrossRef]

87. Cangur, S.; Ercan, I. Comparison of Model Fit Indices Used in Structural Equation Modeling Under Multivariate Normality.

J. Mod. Appl. Stat. Meth. 2015, 14, 152–167. [CrossRef]

88. Baron, R.M.; Kenny, D.A. The Moderator–Mediator Variable Distinction in Social Psychological Research: Conceptual, Strategic,

89.

and Statistical Considerations. J. Personal. Soc. Psychol. 1986, 51, 1173–1182. [CrossRef]
Shi, D.; Lee, T.; Maydeu-Olivares, A. Understanding the Model Size Effect on SEM Fit Indices. Educ. Psychol. Meas. 2019, 79,
310–334. [CrossRef]

90. Petty, R.E.; Cacioppo, J.T. The Elaboration Likelihood Model of Persuasion. In Advances in Experimental Social Psychology; Elsevier:

Amsterdam, The Netherlands, 1986; Volume 19, pp. 123–205. ISBN 978-0-12-015219-3.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

informa t ics
Article
Affective Design Analysis of Explainable Artificial Intelligence
(XAI): A User-Centric Perspective
EzekielBernardo* andRosemarySeva
IndustrialandSystemsEngineeringDepartment,DeLaSalleUniversity—Manila,2401TaftAve,Malate,
Manila1004,Philippines
* Correspondence:ezekiel.bernardo@dlsu.edu.ph
Abstract:ExplainableArtificialIntelligence(XAI)hassuccessfullysolvedtheblackboxparadoxof
ArtificialIntelligence(AI).Byprovidinghuman-levelinsightsonAI,italloweduserstounderstand
itsinnerworkingsevenwithlimitedknowledgeofthemachinelearningalgorithmsituses. Asa
result,thefieldgrew,anddevelopmentflourished. However,concernshavebeenexpressedthat
the techniques are limited in terms of to whom they are applicable and how their effect can be
leveraged. Currently, mostXAItechniqueshavebeendesignedbydevelopers. Thoughneeded
andvaluable,XAIismorecriticalforanend-user,consideringtransparencycleavesontrustand
adoption. Thisstudyaimstounderstandandconceptualizeanend-user-centricXAItofillinthe
lackofend-userunderstanding.Consideringrecentfindingsofrelatedstudies,thisstudyfocuseson
designconceptualizationandaffectiveanalysis.Datafrom202participantswerecollectedfroman
onlinesurveytoidentifythevitalXAIdesigncomponentsandtestbedexperimentationtoexplorethe
affectiveandtrustchangeperdesignconfiguration.Theresultsshowthataffectiveisaviabletrust
calibrationrouteforXAI.Intermsofdesign,explanationform,communicationstyle,andpresenceof
supplementaryinformationarethecomponentsuserslookforinaneffectiveXAI.Lastly,anxiety
aboutAI,incidentalemotion,perceivedAIreliability,andexperienceusingthesystemaresignificant
moderatorsofthetrustcalibrationprocessforanend-user.
Keywords: explainable AI; XAI; artificial intelligence; AI; interpretable deep learning; machine
learning;computervision;affectivedesign;emotions;end-userdesign
Citation:Bernardo,E.;Seva,R.
AffectiveDesignAnalysisof
ExplainableArtificialIntelligence
(XAI):AUser-CentricPerspective. 1. Introduction
Informatics2023,10,32.
Recentbreakthroughsinalgorithmictechniquesandthecomplementarydevelopment
https://doi.org/10.3390/
ofmorecapablecomputingtoolshaveexponentiallyprogressedtheartificialintelligence
informatics10010032
(AI)field.TheseadvancementshaveboostedAI’sanalyticalpower,enablingconvolutionto
AcademicEditor:LongJin takeonmorecognitivelydemandingtasks[1,2]. Asaneffect,AIcannowbeseenpowering
differentsystems,formultitudesofuses,andatvaryinglevelsofhumanaugmentation.
Received:17January2023
While the added utility that AI can potentially bring is undeniably beneficial, un-
Revised:9March2023
fortunately, italsodetrimentsthepossibleadoptionofuserstoit. Why? Becausethese
Accepted:14March2023
Published:16March2023 advancementswererealizedbysacrificingAI’sinterpretabilityortheabilitytounderstand
howandwhytheAIcameupwithitsrecommendations. Thisstemsfromusingcomplex
algorithms(i.e.,machinelearning—MLanddeeplearning—DL)thatareinherentlyincom-
prehensible[3]. Inreturn,itrestrictshowtrust[4–8]andsubsequentreliance[9]canbe
Copyright: © 2023 by the authors. calibratedaccurately,giventhatusersareunawareofAI’sactualinnerworkings. Thisoften
Licensee MDPI, Basel, Switzerland.
leadstoover-trustinganincapableAIor,atworst,abandoningareliableAI,whichisa
This article is an open access article
pressingissueconsideringhowsocietyframesAI’sroleinthefuture[10,11].
distributed under the terms and
So,whydotheexpertsthatdevelopedthealgorithmsnotjustprovidetheexplanations?
conditionsoftheCreativeCommons
Assimpleasitseems,thiswillnotworkasAIfunctionssimilarlytohumanbrains[12].
Attribution(CCBY)license(https://
Evolutionwillhappenasitlearns,createsrules,contextualizes,andeventuallyadaptsto
creativecommons.org/licenses/by/
gainperformance. Becauseofthis,newparameters(“hiddenlayers”inthecontextofML)
4.0/).
Informatics2023,10,32.https://doi.org/10.3390/informatics10010032 https://www.mdpi.com/journal/informatics

Informatics2023,10,32 2of24
thatarenotoriginallypartoftheunderstandabledesignareaddedtothesystem,makingit
inexplainabletoallusers,includingthedevelopers[13]. Forthisreason,theissueisoften
taggedastheblackboxparadoxofAI[14].
Asaworkaroundsolution,theinnovativefieldofexplainableAI(XAI)hasbeenintro-
duced. RatherthanentirelyunpackingthealgorithmsthattheAIuses,whichisdifficult,it
focusesonprovidinghuman-levelexplanationsconceptualizedfromthecomprehensible
facets of the AI [15]. It centers on the AI’s purpose, process, and performance to grant
cognitiveresources[16,17]tohelpdevelopers[18](e.g.,troubleshooting,understanding
limitations, and improving performance) and to answer critical questions raised by an
end-user[19]. Often,thisisintheformofvisualizationtoolsembeddedintheAIinterface
forinteraction[20].
Takeimagerecognition,forinstance,whichisoneofthefirst,mostprominent,and
well-researchedAIdomains. XAIisbeingusedasanalternativeinexplainingthethinking
processoftheAI(e.g.,heatmaps,featureexamples,ruleexplanations,etc.). Thismakesthe
complexanalysisperbitmap(i.e.,geometriccodingandpatternanalysis)[21]comprehen-
sibleanddeduciblefortrustandrelianceassessmentforadoption[22,23]. Asaresult,more
demandingtasks(e.g.,self-drivingcarswithvisualization,facialrecognitionwithsaliency
maps,etc.) arebeingunlockedandadoptedacrossdifferentfunctions[20]. Thisgoesthe
samewithotherdomains,whichsawpositivechangesuponusingXAI[15].
ThebenefitsfromXAIhaveencouragedmanyscholarstoexpandthefieldbydevelop-
ingnewertechniques,withthemajoritytakingonthechallengeofprovidingadeeperand
moreaccuraterepresentationofAI’scomplexinnerworkings(e.g.,DeterministicLocalIn-
terpretableModel-AgnosticExplanations,ShapleyAdditiveExplanation,andQuantitative
TestingwithConceptActivationVectors)[8,15]. Asaresult,mostoftheresearchhascen-
teredonwhatinformationXAIshouldcarry,orfocusedonitsroleasacognitiverepository
ofexplanation[24,25]. Althoughthisistheoreticallyusefulgiventhefield’sinfancyand
rapidlyexpandingAIusecases,thespotlightfromcurrentresearchhasunderrepresented
theend-usersandcenteredmoreonthedevelopers[26–28].
Threefoundationalaspectscanbesynthesizedfromthecurrentresearchstreamthat
supportstheclaim. First,expertisewithMLandDLisneededtounderstandcurrentXAI
techniques,whichatypicalend-userdoesnothave[18,19]. Next,thegoalisoftendirected
atimprovingAI’salgorithm[29,30]andnotonanend-user’sfundamentalgoaloftriggering
adoptionanditsprerequisiteoftrust. Lastly,currenttechniquesweremainlyviewedasa
cognitiveresourceratherthanabridgeinhuman–computerinteraction(HCI)[25,31]. This
meansthatlittletonothingisknownabouthowXAIsareperceivedbyanend-userwhen
embeddedinanAI,consideringitsinherentcharacteristics.Withthelimitedunderstanding
oftheend-usercontext,thiscancauseasignificantthreattothetrajectoryofAI’srolein
society,viz.,possiblyhaltingtheadvantagesAIcanbringtotheday-to-daylifeofhumans.
Considering the gap in the context of end-user XAI, this study is proposed to an-
swer the question: “How to create an end-user-centric XAI?”. As pointed out by re-
centworks,peopleareapproachingXAIwiththesameattitudeofexpectationtheyare
employingtowardsanotherhuman[32–34]. Thisentailsthat, inusingXAI,interaction
process(howthestimuliwereused),structure(howitispresented),andvariability(pos-
sible external influences) can play essential roles in making a judgment (i.e., trust and
reliance)[29,31,33,35–37]—aspectsthathavebeenlimitedinexistingXAIresearch. With
that,theproblemwillbeexaminedfollowingtheobjectives:
• Determinehowanend-usercalibratestrustfromXAI.
• Identifythefactorsthatcansignificantlychangehowtrustcanbecalibrated.
• Examinepossiblemoderatingfactorsthatcanaffectthecalibrationprocess.
• HowdoexternalfactorsmoderatetheeffectofXAIinthecalibrationprocess?
Theremainderofthispaperisdividedintosixsections. Thenextsectionpresentsthe
backgroundofthestudy.Sections3–5confertheexperimentdesign,givethedata-gathering
results,anddiscussthefindingswithrespectiverecommendationsbasedonthestudy’s
objectives. Finally,thelastsectionclosesthepaperwiththeconclusion.

Informatics2023,10,32 3of24
2. ReviewofRelatedLiterature
Using this idea and the different theories in other spaces that similarly examined
cognitive-basedstimuli,thisstudyaimstoaddresstheproblemthroughtheinteraction
lensintermsofthetrustcalibrationprocess,designforthestructure,andexternallimits
forinfluences.
2.1. TrustCalibration
Trustcalibrationisadynamicprocessasitencompassesdifferentdimensions(e.g.,
performance,reliability,predictability,etc.),andcanbeprocessedonvariousroutes. In
thestudyconductedbyLeeandSee[38],theyidentifiedthreepossiblewaystotunetrust
basedonrationality,societalbeliefornorms,andengagementofemotions. Theydevised
theseroutesascognitiveandaffectiveroutes. Cognitivecanbefurtherbrokendownas
analytic and analogic. The applicability of the routes mainly depends on the available
information,therelationshipbetweenthetrusteeandtrustor,andhowtheinformationcan
beelaboratedinthatsituation.
2.1.1. CognitiveTrustCalibration
If trust is formed from a rational evaluation of a trustee’s salient behavior, this is
considered analytic processing [39]. This method overstates cognitive capacities as a
limitation for rationality, and understates the influence of emotions and strategies for
trust formation. This functions as knowledge-based processing, relying on a function-
basedmentalmodelofthesystemsuchaswithmotivation,interests,performance,and
capabilities[38]. Further,knowledgecanbesourcedthroughdirectobservation,possible
intermediaries,andpresumptionsavailabletothetrustor.
Ontheotherhand,iftrustworthinessisdeterminedbasedonsocietalnorms,reputable
opinions,oranyenablinginformationwithoutdirectcontact,analogicprocessingiscon-
sidered. Thismethodheavilyassumesthattrustcanbedevelopedasanoffsetofbelief
fromsignificantintermediariesandnotonthedirectexperiencefromthesystembeing
considered. Thisislesscognitivelytaxingthananalyticprocessingandmainlyusesrules
andpresumptions[39].
2.1.2. AffectiveTrustCalibration
Asidefromcognitive,anotherwaytocalibratetrustisviaemotionsorhowpeople
feel. Asthenameimplies,affectiveprocessingisstrictlybasedontheemotionsgenerated
by and toward the entity [39]. Compared to the analytical and analogical of cognitive
processing,thismethodminimizestheneedforrationalcuesandprioritizeshowpeople
feelaboutthesystem—thecoreinfluenceoftrustonbehavior[40]. Inaddition,thisroute
mainlyfocusesonmoment-to-momenttrust—subjectedtointrinsicandenvironmental
factors—sinceemotiontendstofluctuateovertime(e.g.,expectationdoesnotconformto
theongoingexperience). Inthesimplestterms,thecorebeliefonthisrouteisthatpeople
thinkandfeeltrust.
Lee&See[38],intheirwell-citedHCIstudy,proposetheideaoftheaffectiveroutesug-
gestingthattrustmightalsobeinducedbyirrationalfactors,suchasemotionsandmoods
(additionaldiscussionispresentedintheAffectsection). Operationally,thisleveragesthe
user’semotionalresponsestothestimuliratherthanitsintellectualorcognitiveresources.
Theideaisdeeplyrootedinthesocialscienceparadigm,whicharguesthatinaninteraction,
aside from the cognitive gain, people can also develop affective states (e.g., positive or
negativemood,happy,sad,confused,andscaredemotions),whichcanbeinfusedinthe
evaluationofthetrustee’sabilities,competence,andtrustworthiness[41–44].Thesecanrun
asshort-termemotionsorlong-termmoods,allowingthemtoactascontinuouslyshifting
influencesthatcontinuallyalterperceptionandtriggerthementalprocessesthatleadto
particularbehaviors[45,46].
Madsen&Gregor[47]alsopointedoutthataffectiveprocessingcancalibratetrust
morerapidlyandunconsciously; needslittletonocognitiveresources; andcanalsobe

Informatics2023,10,32 4of24
developedoutsidetheinteractionfromthestimuli(e.g.,dispositionorpersonality),which
makestheargumentofitbeingdominantovercognitiveprocessing. Forexample,Myers&
Tingley’s[48]moneytrustgameidentifiedthatnegativeemotions(i.e.,anxietyandfear)
coulddecreasetrust,butonlyifthosenegativeemotionsmakepeoplefeellesssureabout
theircurrentsituation. Conversely,peopletendtotrustmoreiftheyexperiencepositive
emotionseventhoughthegamepresentsacertaintyoflosing. Inhospitalityresearch,Jin
&Merkebu[49]foundthatinanupscalerestaurant,positiveemotionsignificantlyledto
highercustomertrustandgratitudeeveninvaryingconditionsofservice(i.e.,fastandslow
servingtime). Fundamentally,peoplenavigatingthroughtheaffectiveroutecandecidenot
totrustsimplybecauseofuneasyfeelingsthatcannotbeexplainedrationally,orbytrusting
asystemduetoaparticularemotionthatdevelopedduringthemomentofinteraction.
2.1.3. SynthesisforTrustCalibration
RelatingthisprocessingtoXAI,currentresearchhasfocusedoncognitiveprocessing.
Aspresentedpreviously,therunninghypothesisintheresearchstreamisthatinterpretabil-
ityhasadirectrelationshipwiththedepthofcognitiveinformationitprovides. Moreso,
alltheidentifiedgoalsforXAIareregressedagainstitscognitiveaspect. Forexample,by
allowingpeopletothink,theywillunderstandthatAIistrustworthy.
On the contrary, affective processing is still an area to be explored for XAI trust
calibration. Asofthewritingofthispaper,therearenostudiesthattriedtoevaluatethe
affective ability of XAIto calibrate trust. At the veryleast, there are piecesof evidence
showingtheabilityofXAItoengenderemotions.Forinstance,Jensenetal.[50]successfully
classifiedfourprimaryaffectivestatesoutofthenineteenpre-identifiedemotions,which
includehostility,positivity,anxiety,andloneliness,byshowingadditionalexplanations
of the process and performance of a drone AI system. Albayram et al.’s [51] work on
safety-criticalAIsystemsfactorednegativeindividualisticemotion,positiveemotion,and
negativeprosocialemotionsasthethreemainstatesoutof44pre-identifiedemotionsupon
subjects’exposuretotheexplanationofroleandcriticalityofthesituation. Byexamining
humanfacialreactionsandsignals(i.e.,brow,cheek,andlipsmovement),Guerdanetal.[52]
successfullyidentifiedthatemotionssuchashappinessandangeraremanifestedwhen
peopleinteractwithXAIinterfaces.
Therearealsopiecesofevidenceshowingtheemotion–trustrelationshipforXAI.For
example,eightpicturesdepictingpositiveornegativemoodswereusedbyPhillipsand
Madhavan[53]tomanipulatetheparticipants’initialemotionalstate. Theirexperiment
determinedthatuserswithpositivemoodsaremoresusceptibletotrustAIrecommenda-
tionsthannegativemoods. Merritt(2011)andDuetal. (2020)usedaffectivelyladenvideo
clips(i.e.,happy,sad,scary)toprimetheemotionalstatusoftheparticipants. Theformer
suggests that the decision-making process is driven emotionally rather than rationally,
while the latter proved that positive valence led to better takeover quality. Gompei &
Umemuro[54]discoveredthattrusttowardsutilityinformation(e.g.,instructionsfora
task,explanationsfromanevent)fromsocialrobotsisdevelopedviatheaffectiveroute.
Specifically,thedegreeoffeelingsisdirectlycorrelatedtothetrusttowardstheinformation
andtherobots(i.e.,positiveemotionleadstohighertrust). Forautomatedcomputerwarn-
ings,Bucketal.[55]foundthatthequalityofcognitiveinformationpresentedbythealerts
wasnottheprimarydeterminantoftrust. Affectivestatefundamentallycalibratedthetrust
stance of users with positive affect building more trust than other developed emotions
suchasanxiety,hostility,andloneliness. Bernardo&Tangsoc[56]identifiedthattrustseals
(i.e.,certificationshowingpaymentassurance)serveasaffectivecuesratherthancognitive
stimuli. As verified from the post hoc interview, exposed people developed a sense of
happinessandconfidencewhichtriggeredtrustformation. Forintelligentpersonalassis-
tants,Chen&Park[57]determinedthatevenifitisintendedtodeliverfactualresponses,
trustisprimarilycalibratedbasedonthefeelingofpositivesocialattractionratherthanthe
correctnessoftheinformationitprovides.

Informatics2023,10,32 5of24
2.2. EmotionalorAffectiveDesign
Withtheconsiderationoftheaffectivepathapproach,emotionaldesign,alsoknown
asaffectivedesign,isconsidered. Thisisaresearchfieldconcernedwithcreatingdesigns
thatelicitemotionsfromuserstotriggerspecificbehavior[58,59]. Thisattemptstodefine
thesubjectiveemotionalrelationshipsbetweenusersandstimuliandexploretheaffective
properties that intend to communicate through their design attributes [46,60]. In other
words, the idea is to identify a specific design element that can potentially engender a
particularemotionthatwillleadtoaspecificchangeinthetargetbehavior.Thisconcepthas
beenusedinavarietyofdomainssuchasintheuserinterfaceofchildren’se-learntocreate
positiveattachment[61];computergamedesigntoenhanceenjoymentandhappiness[62];
eco-labelstopromotepositiveaffectwhichtriggerspurchaseintention[63];socialrobots
toenhancepositiveperceptionandpreference[35];andtrashbinsignagestoencourage
wastesegregation[64]tonameafew.
Inthetimelineofaffectivedesign,thethreemostinfluentialworkswereproposedby
Norman[65],Jordan[66],andKhalid&Helander[67]. Conceptually,theideasdifferin
howtheyapproachdesignandscaleitspotentialeffect.
2.2.1. ThreeLevelsofProcessing
TheThreeLevelsofProcessingbyNorman[65]viewsaffectivedesigninconjunction
with how the human brain processes design during an interaction. It is divided into
threecategorieswhichflexfromasurface-levelviewofthedesignfeatures,anexperiential
ofitsoverallpackage,toananalyticalapproachthatusesexperience. Respectively,these
arecategorizedasvisceral,behavioral,andreflectivedesigns.
Of the three, the lowest level is visceral. This encapsulates the distinctive visual
aspectsofthedesign,suchascolor,size,texture,shape,oranyfigurativeelementofthe
designcriticaltoitsaestheticvalue. ConsideringXAIasanexample, visceraldesignis
concernedwithhowtheattributesarepresented,thethemeoftheimages,thefontsizeof
theexplanations,orthethicknessoftheelementsinagraph. Becauseofthisscope,ituses
automaticorpre-wiredprocessingthatmakesrapidandstraightforwarddecisionsonthe
stimulithroughpatternmatching—appealingtotheimmediateemotionalresponsetohow
theuserintuitivelyperceivesthedesign.
Thenextlevelisbehavioraldesign,whichvaluesanexperientialviewofthedesign. It
operatesontheperformanceandfunctionalityofthedesignoveritssuperficialappearance.
Conceptually, this functions in parallel with traditional usability engineering, meaning
designsareinvestedinhowuserscarryouttheiractivities,howaccuratelytheyachieve
theirobjectives, howmanytimesanderrorscanbecommitted, orhowwellthedesign
accommodates different types of users. Relating again to XAI, this level of design is
concernedmainlywithwhethertheuserabsorbedtheexplanationstoperceiveacertain
leveloftrustoritssubsequentreliancebehavior.
Lastly,thehighestlevelisreflectivedesign. Comparedtothefirsttwo,thisleverages
more past experiences and knowledge rather than real-time design evaluation, using
developedinterestorlearnedpreferencesfordesign. Traditionally,thisisrelatedtothe
messagethedesignsendstotheuser,whichisevaluatedonitsparitywiththeself-image
the user wants to project. With that, reflective design is approached more consciously,
weighingitsprosandconsaccordingtoamorerationalside. InthecontextofXAI,this
canbeadesignbasedontheuser’spersonalpreferencegrownovertheinteractionwith
otherexplanations. Forexample,ausermightpreferaheatmapduetotheirvisualskills
andpersonalbeliefthatitisbetterthanotherformsofexplanation.
2.2.2. FourPleasures
AnotherwaythataffectivedesignhasbeencategorizediswiththeFourPleasuresby
Jordan[66]. Inthiscategorization,themainpremiseisthatitemphasizespleasureabove
all else. Meaning, functionality, an aspect that is heavily considered in the proposal of
Norman[65],isnotexplicitlyreflected. Thisisdevelopedbasedontheknowntypesof

Informatics2023,10,32 6of24
pleasuresfromananthropologicalperspective,dividedintofourtypes: physio-,socio-,
psycho-,andideo-pleasure.
Physio-pleasureisanaffectdevelopedfromtheappreciationofthesenses. ForXAI,
sinceitispresentedasanexplanationintheinterfaceoftheAIsystem,ithighlyleverages
thesenseofsight—howvisuallyappealingthedesignistodeliverpleasure. Ontheother
hand,socio-pleasurestemsfromtheinteractionwithothers—whetheritfollowsacertain
normorissociallyaccepted. Operationally,thiscanbehowXAIdesignresonateswiththe
well-acceptedorfavoredwayofgivingexplanations. Forinstance,forvisualsearchtasks,
avisualfeature-basedexplanationisbetterthanaverbalone,whichissociallyacceptable.
If the focus is on the cognitive caveat of the stimuli, psycho-pleasure is considered. In
thecontextofXAI,thisrelatestothecognitiveability(i.e.,memory,stress,workload)of
theuseronhowitshouldbedesignedtolimititsnegativeeffect. Thiscanbeperformed
by simplifying the load presented or selecting a different form of explanation. Lastly,
idea-pleasureinvolvestheuser’svaluesandbeliefsinappreciatingthedesign. ForXAI,
thismostlyresonateswiththeaesthetictaste,whichisrelativelythesameasthereflective
designofNorman[65].
2.2.3. FrameworkforAffectiveCustomerNeeds
Lastly,anotherfoundationalideausedinaffectivedesignforcategorizationisKhalid
&Helander’s[67]FrameworkforAffectiveCustomerNeeds. Relativetothefirsttwo,it
wasdevelopedbasedonempiricalresultsfromanextensivesurveyratherthanaparallel
view from an anthropological phenomenon (i.e., brain functions for the three levels of
processingandpleasureclassforthefourpleasures). Theyusedasurveytorateproduct
features and then categorized them using factor analysis. Their results factored three
generic categories of user preference: holistic attributes, styling, and functional design.
Theirstudyhighlightedthatfamiliaritydiffersfromusers’stanceondesignappreciation.
Holisticattributescanbethoughtofasthegestaltoftheproduct. Thismeansthat
designsareviewedaspackagesratherthanspecificcomponents. Designsinthiscatego-
rization are from products unknown to the user. In the context of XAI, these are users
notfamiliarwiththebasicfunctionalityofthesystemandtheexplanationitself. Onthe
otherhand,ifthedesignprioritizationisonspecificdetails,thisoftenfallsonstyling. This
focusesonspecificattributessuchascolors, shapes, andsizes. Thespecificityishighly
attributabletotheuser’sfamiliaritywiththeproductinconsideration. Ifthefamiliarusers
are way past the aesthetic quality of the design, they can dive into the functional level,
which relates to the types of tasks the product works for the user. For XAI, this can be
whethertheexplanationisappropriateinthegivencontext.
2.2.4. SynthesisofEmotionalorAffectiveDesign
Thedifferentlevelsofdesigndiscussed,withsomeoverlapping,showedwhataspect
ofdesignspecificusersconsidergiventheirvaryingcharacteristics. Consideringthis,the
studywillmainlyfocusonthedesignattributetypesratherthanspecificdesigncomponents
ofit(i.e., color, size, andshape). Thisdecisionisdrivenprimarilybytwopoints. First,
sincetherehadbeennostudyonaffectivedesignforXAI,ahigher-levelapproachwillbe
beneficialasanoutputtobeusedforfuturestudies. IdentifyingwhichamongXAIform
typesofworkismoreencompassingthanaspecificdesigncomponentthatcanobserve
certainreservations. ThesecondpointfollowsthefamiliarityaspectraisedbyKhalid&
Helander [67], wherein novice users—the focus of this study—value holistic attributes
ratherthanspecificstyling.
2.3. ProposedModelandHypothesis
Overall,thesynthesisfromthereviewoftherelatedliteraturehighlightsthestudy’s
setup. Asfortheinteraction,thisstudywilldeviatefromtherunninghypothesisofthe
cognitiveroute. Mainly,thisstudywillcenterontheexperiencebeyondtherationalview
throughaffectivecalibration. TheXAIemotionset(XES)ofBernardo&Seva[68]willbe

Informatics 2023, 10, x FOR PEER REVIEW 7 of 25
observe certain reservations. The second point follows the familiarity aspect raised by
Khalid & Helander [67], wherein novice users—the focus of this study—value holistic at-
tributes rather than specific styling.
2.3. Proposed Model and Hypothesis
Overall, the synthesis from the review of the related literature highlights the study’s
Informatics2023,10,32 setup. As for the interaction, this study will deviate from the running hypothesis o7f otfh2e4
cognitive route. Mainly, this study will center on the experience beyond the rational view
through affective calibration. The XAI emotion set (XES) of Bernardo & Seva [68] will be
uusseedd ttoo mmeeaassuurree cchhaannggeess.. CCooiinncciiddiinngg wwiitthh tthhiiss,, ffoorr tthhee ddeessiiggnn,, tthhee ssttuuddyy wwiillll vvaalluuee tthhee
pprriinncciippllee ooff eemmoottiioonnaall ddeessiiggnn.. TThhiiss lleevveerraaggeess ddeessiiggnn ssaalliieennccyy ttoo ttrriiggggeerr eemmoottiioonnss oorr hhooww
ssttiimmuullii pprreesseenntt tthheeiirr ddiiffffeerreennttd deessigignna atttrtribibuutetess..F Foolllolowwininggt htheee enndd-u-usesre-rc-ecnetnrtircica papprporaocahc,ha,
pa rper-set-ustduydwy iwlliblle bpee prfeorrfmoremdetdo tido eindteinfytitfhye tsheedsee sdigensigantt raibtturitbeus.teLsa. sLtlays,tfloyr, lfiomr iltiamtiiotantsi,otnhse,
tshtued sytuwdiyll wcoilnl sciodnesribdoetrh bAotIha nAdI aunsedr upsreorp perrotipeserftoilelso wfoilnlogwthinegr othlee orfoXleA oIf iXnAthI einin ttheer aicnttieorn-
aacntdioqnu aanldit aqtuivaelitcalatiivme sclfariomms ofrtohmer oHthCeIr sHtuCdI isetsu[d5i5e,s6 9[5,750,6].9,7T0h]i.s Twhiisl lwinilcl liundceluAdeI AanIx ainetxy-,
iientcyid, iennctiadleenmtaol teiomnost,itornuss,t tdruisspt odsiistpioons,itaionnd, XanAdI eXxApIe erixepnecreiefnocreh fuomr hanumfaacnto frasc,tworhsi,l ewahlisloe
AalIsore AliIa rbeilliitayb,illeitayr,n lienagrncianpga cbaiplitayb,iblirtayn, bdr,aanndd, aexnpde erxiepnecreiefnocreA foIrf aAcIt ofarcs.toTros.e Tnoc aepnscuaplastueltahtee
tshyen tshyenstihsefrsoism frtohmer tehveie rwevoifewth eofr etlhaete rdellaitteerda tluitreeraatnudreth aenodv tehrael lopvlearnalol fptlhains sotfu tdhyi,s asntuXdAyI,
Tanru XstACI aTlirbursatt iCoanliMbroadtieoln( XMAoIdTeCl) (mXAodITeCli)s mproodpeol siesd p(rsoepeoFsiegdu r(ese1e) .FTighuisreb u1)i.l dTshuisp obnuitlhdes
usypnotnh etshizee dsyfnrathmeeswizoedrk ffroarmXeAwIorerkse aforcrh XfrAoIm reasuesaerrchm ofrdoemlp ae ruspseecr timveoodfelH paqerusepeetctailv.e[2 5o]f.
HEaacqhupe aetth awl. i[l2l5b]e. Eteascthe dpaatsha wseilpl abrea tteeshteydp oatsh ae ssiesptaorcaoten fihrympotthheesmiso tdoe cl.onfirm the model.
FFiigguurree 11.. XXAAII TTrruusstt CCaalliibbrraattiioonn MMooddeell..
BByy aannsswweerriinngg tthhee oobbjjeeccttiivveess,, tthhee eenndd ggooaall iiss ttoo pprroovviiddee tthhee ffoolllloowwiinngg ccoonnttrriibbuuttiioonnss ttoo
tthhee ffiieelldd ooff XXAAII::
• • B Be e i i n n g g t th h e e fi fi r r s s t t s s t t u u d d y y t t o o v v e e r r i i f f y y h h o o w w t t r r u u s s t t c c a a l l i i b b r r a a t t i i o on n f f r r o o m m X X A A I I h h a a p p p p e en n s s t t h hr ro o u ug g h h t t h he e
lensofanend-user.
lens of an end-user.
• Valuingtheimportanceoftheuser-centeredapproach,thisstudyshedlightonthe
• Valuing the importance of the user-centered approach, this study shed light on the
user’sviewofXAIdesigncompositionanditsperceivedimportanceinexplaining
user’s view of XAI design composition and its perceived importance in explaining
andpossiblybuildingthetheoriesforXAItrustresearch.
and possibly building the theories for XAI trust research.
• Basedontheresultsofthisstudy,differentinsightsonhowXAIcanbedesignedare
• Based on the results of this study, different insights on how XAI can be designed are
generated,whichcanpotentiallybeusedtoleveragetheeffectsofemotions.
generated, which can potentially be used to leverage the effects of emotions.
• Byunderstandingthedynamicsofexternalfactors,bettersituationaluseofXAIcan
• By understanding the dynamics of external factors, better situational use of XAI can
becreated.
be created.
3. MaterialsandMethods
3. Materials and Methods
Totesttheproposedhypothesis,viz.,toanalyzetheobjectivesofthestudy,anasyn-
chronousexperimentwasdesignedandcarriedout.Thegoalwastosimulateaninteraction
withXAIbyusinganexistingAI-poweredsystem. Thiswasperformedusinganexper-
imental testbed where different design combinations were prompted to the user in a
between-subjectdesign. Datathatwererecordedwerebasedontheindependentvariables
fromtheXAITCmodel.
Toguidethedevelopment,apre-studywasconductedwithfourprimarygoals: (1)to
identifythemostfamiliarAItoavoidalienation,(2)todecidethedesignsetuptominimize
theundesirableeffectofnegativeuserexperience,(3)todeterminethedesignattributes
ofXAIconsideredtobenecessarybyusers,and(4)toidentifytheconfigurationsofthe

Informatics2023,10,32 8of24
moderators. Datawerecollectedfromanonlinesurveyansweredby312currentAIusers.
For idea validation and feasibility assessment, results were run through a focus group
discussioncomprisedofsixAIdevelopersandsixuserexperiencedesigners.
TheconclusionwastouseimageclassificationAIasause-context,withtheGoogle
Lensapplicationasthetemplatefortheoverallcompositionandlogicflow. FortheXAI,
three design attributes were selected. Notably, (1) the explanation form or how XAI
is presented, (2) the communication style for the explanation, and (3) the presence of
supplementaryinformation. Twolevelsperdesignattributewereconsideredbasedonthe
enumerationofJianetal.[71].
FortheAIfeatures,reliabilitywassettodifferfrom70%forlowand90%forhigh.
Learningcapabilitydefaultedtopureconditions. Asforthebrand,Googlewasselectedto
bethenametorepresenthigh-reputationAI.Lastly,forthetimeexperience,twodayswas
deemedoptimal. Allinall,64designs(26)weretested. Takenotethattimeexperiencewas
notconsideredaspartofthefactorialcomputationgiventhatitisnotadesigninputbuta
momentofrecording. Table1summarizesalldesignconfigurationsfortheexperiment.
Table1.Experimentaldesignconfigurations.
Component Variable #ofLevels Configurations
ExplanationForm 2 Feature,Example
XAIDesign CommunicationStyle 2 Humanized,Robotic
SupplementaryInformation 2 With,Without
AIReliability 2 Low(70%),High(90%)
LearningCapability 2 Yes,No
AIFeatures
Brand 2 Google,Generic
TimeExperience 2 Day1,Day2
3.1. Participants
Thesnowballconveniencesamplingmethodwasusedforthedatagathering. Initial
leadsweregeneratedfromdirectinvitationsofpeersandpromotionaladspostedinvarious
socialnetworkinggroups. QualificationsweresetasbeingabletocommunicateinEnglish,
being at least 18 years old, having a normal or corrected-to-normal vision without any
colorblindnessissues,andwithexperienceusinganyAI-poweredsystem. Considering
thenatureofthestudy,beingnotemotionallydepressedwasalsoarequirementtolimit
biasandskewness. This,however,wasnotpostedaspartoftheadvertisementmaterialto
avoiddiscrimination. Furtherdiscussiononhowtheserequirementswereconfirmedwill
begiveninthenextsection.
Technical requirements were also specified to facilitate the experiment effectively
inremoteconditions. Particularly,havingasmartphonewithatleast1080×1920pixel
resolutionwithoutanyscreenissues,internetconnectivityofatleast5Mbps,anupdated
webbrowserapp,andavailabilityofareaconducivetotheexperiment. Additionally,they
wererequiredtohaveatleast30minofuninterruptedtimetoperformthetestfortwodays.
Atokenworth100PHP(~2.00USD)plusaperformancebonusrangingfrom25PHPto
50PHPwasguaranteedinexchangefortheircompleteinvolvement.
Consideringtheoverarchinggoalofthepaperoftestingtherelationshipsinvolved
in the trust calibration of an end-user from XAI through the proposed XAITC model,
aswellastoattainastatisticallycapabledataset, theminimumsamplesizewassetto
152participants. ThiswasevaluatedbasedontheprinciplessetbyKline[72]forstructural
assessmentandtheresultofthepriori-powersamplecomputationestablishedfromthe
guidelinesofWestland[73]andCohen[74]; thesetupwasat0.3anticipatedeffectsize,
0.85desiredstatisticalpowerlevel,and0.05alphalevel.
3.2. Measurements
Data were captured through an online questionnaire and an experimental testbed.
Theformerrequestedthecontrol(i.e.,demographics,disposition,andsituationalfactors)

Informatics2023,10,32 9of24
andindependentvariables(i.e.,depressivestateandincidentalemotions),whilethelatter
enabledthemanipulationofXAIdesignattributestomeasurechangesfromtheinteraction.
Bothtoolsweredesignedtobeaccessedthroughawebbrowser,withEnglishbeingits
defaultlanguage.
3.2.1. OnlineQuestionnaire
Athree-sectiononlinequestionnairewasdevelopedandhostedthroughGoogleForms.
Thefirstsectionfunctionedasthepreliminary,wheretheoverview,generalinstruction,and
dataconsentclauseweredetailed. Italsocarriedtheyes-or-noscreeningtestforEnglish
languagecompetence,agerestriction,visualacuity,andAIexperience.Asforthedepressive
state,theMoodandFeelingQuestionnaire(MFQ)developedbyAngold&Costello[75]was
used. Movingon,thesecondpartrequesteddemographicanddispositionalinformation.
Age,gender,educationalattainment,occupation,andincomeweretheidentifiedcontrols.
Forthedisposition,trustassessmentbyFrazieretal.[76]andAIanxietymeasurementby
Wang&Wang[37]werecontextuallyused. Finally,thelastsectioninquiredaboutAIplus
XAIexperiencesandincidentalemotions.Theyearsofexperiencewereinamultiple-choice
form,whilefournewseven-pointLikertquestionsweredevelopedtomeasureincidental
emotions. TheXAIemotionset(XES)ofBernardo&Seva[68]wasusedasthereferencefor
thedifferentemotiongroups.
3.2.2. ExperimentTestbed
Thethree-sectionedtestbedwasbuiltusingFigmaandwashostedthroughtheQuant-
UXprototypingsite. Thefirstsectionhandledtheinstructionandexamples,withthree
practicetrialsavailable. Thiswasfollowedbythesecondsection,whichcarriedthemain
imageclassificationtask. Thegeneralworkflowisasfollows: (1)theparticipantswillfirst
selecttheimagefromthegallery,(2)theAIwillgenerateitsrecommendationandexplain
itsdecision-making,and(3)theparticipantswilldecideonwhethertoagreeorprovide
theirclassificationasameasurementfortheirreliance. Takenotethatthecorrectnessof
recognitionwasnotdisclosedasthetestbed’spurposewaslimitedtorecommendationand
machinelearning. Finally,thethirdsectionfeaturestheratingscaleslidersfortheintegral
Informatics 2023, 10, x FOR ePmEEoRt RioEnVsIE,Wm easured like the incidental emotions mentioned earlier. Figure 2 presents 10 of 25
samplescreenshotsofthetestbed.
(a) (b)
Figure2.FSiagmurpel e2.s Scraemenpslhe ostcroefeenxspheorti mofe enxtpteersitmbeedn:t( tae)sAtbIecdl:a (sas)i fiAcIa tciloanssaifnicdaXtiAonI panreds eXnAtaIt piornesoefntthaetion of
the image being recognized; (b) dependent variable sliders to be answered after classification.
imagebeingrecognized;(b)dependentvariablesliderstobeansweredafterclassification.
The user experience, grammar, spelling, and interface of both tools were pre-tested
with nine current AI users, three English language experts, and four app developers. Rec-
ommendations were implemented before its use for the main experiment. In addition,
factor consistency and validity of the newly introduced questionnaire for incidental emo-
tions were checked.
3.3. Procedure
There are three phases in data-gathering: pre-experiment onboarding, main experi-
ment, and post-experiment analysis.
3.3.1. Pre-Experiment Onboarding
The experiment started with the participants attending a synchronous online
onboarding via Facebook Group Call. The focus was to relay the general instructions,
check the setup requirements, present the data confidentiality, and explain the priming
condition. In particular, the scenario was that an NGO hired the participants to help rec-
ognize pictures of different species in the Philippines saved in their database. To aid them,
an image recognition AI system was developed that could give recommendations on what
species the photos contain. Participants were allowed to use it or provide their own. The
onboarding ended with the measurement tool links shared with the participants for asyn-
chronous access.
3.3.2. Main Experiment
The main experiment started with the participants accessing the online question-
naire. They were allowed to do it anytime as long as they finished it uninterruptedly.
Upon access, participants were prompted with the data agreement and screening ques-
tions. Those who agreed and qualified were the only ones allowed to continue. Demo-
graphic information was then requested from the participants, together with the rating
for AI, XAI, and incidental emotions-related questions. Once completed, participants were
forwarded randomly to any of the 24 designs of the XAI testbed.
The use of the XAI testbed started with the preliminaries: application information,
general instructions, and the recap of the priming scenario. Each participant was in-
structed to classify 50 random photos available in the application. This was performed on
two consecutive days (25 photos per day), with scores recorded to measure the

Informatics2023,10,32 10of24
Theuserexperience,grammar,spelling,andinterfaceofbothtoolswerepre-tested
withninecurrentAIusers,threeEnglishlanguageexperts,andfourappdevelopers. Rec-
ommendationswereimplementedbeforeitsuseforthemainexperiment.Inaddition,factor
consistencyandvalidityofthenewlyintroducedquestionnaireforincidentalemotions
werechecked.
3.3. Procedure
Therearethreephasesindata-gathering: pre-experimentonboarding,mainexperi-
ment,andpost-experimentanalysis.
3.3.1. Pre-ExperimentOnboarding
Theexperimentstartedwiththeparticipantsattendingasynchronousonlineonboard-
ingviaFacebookGroupCall. Thefocuswastorelaythegeneralinstructions,checkthe
setuprequirements,presentthedataconfidentiality,andexplaintheprimingcondition. In
particular,thescenariowasthatanNGOhiredtheparticipantstohelprecognizepicturesof
differentspeciesinthePhilippinessavedintheirdatabase. Toaidthem,animagerecogni-
tionAIsystemwasdevelopedthatcouldgiverecommendationsonwhatspeciesthephotos
contain. Participantswereallowedtouseitorprovidetheirown. Theonboardingended
withthemeasurementtoollinkssharedwiththeparticipantsforasynchronousaccess.
3.3.2. MainExperiment
Themainexperimentstartedwiththeparticipantsaccessingtheonlinequestionnaire.
They were allowed to do it anytime as long as they finished it uninterruptedly. Upon
access, participants were prompted with the data agreement and screening questions.
Thosewhoagreedandqualifiedweretheonlyonesallowedtocontinue. Demographic
informationwasthenrequestedfromtheparticipants,togetherwiththeratingforAI,XAI,
andincidentalemotions-relatedquestions. Oncecompleted,participantswereforwarded
randomlytoanyofthe24designsoftheXAItestbed.
TheuseoftheXAItestbedstartedwiththepreliminaries: applicationinformation,
general instructions, and the recap of the priming scenario. Each participant was in-
structedtoclassify50randomphotosavailableintheapplication. Thiswasperformed
on twoconsecutive days (25 photos per day), with scores recorded to measure the per-
formance bonus for the compensation. After completing the required task, additional
instructions were given to the participants, plus the list of available schedules for the
voluntarypost-experimentinterviewandmodeofcall.
3.3.3. Post-ExperimentAnalysis
After all the data were collected, the post-experiment analysis started. It centered
on analyzing experiment results, interviews, and token distribution. Initially, the data
wereassessedforcompletenessandperformance. Thosewhogarneredatleast40correct
classifications were tagged to receive an additional 25 PHP (~0.5 USD), while 50 PHP
(~1USD)wasintendedforthosewhogotallcorrect.Oncefinalized,theevaluationwassent
totheparticipantsviatheirsocialmediaaccountsandemail. Thiscontainedinformation
onhowthetokenwillbedistributed,theinterviewscheduleforthosewhovolunteered,
andthemeetingaccesslinks. Theinterviewfocusedonthereasoningfortheanswerson
thedependentvariables.
3.4. TechniqueofAnalysis
The analysis was principally driven by the two-stage methodology proposed by
Lowry&Gaskin[77]forStructuralEquationModeling(SEM)underacovariance-based
optimization. Thistechniquewasselected,primarily,becauseofitsabilitytodeducecausal
relationshipsproposedintheobjectives. Inaddition,itcanestimatemodelparametersthat
minimizeresidualvariance[78],isinsensitivetoparametricconditions[79],andissuitable
forsimultaneousanalysisofthedesignconstructs[80].

Informatics2023,10,32 11of24
Analysiswassegmentedintotwomainphases. Thefirstpartisfortheconfirmation
oftherigidityofthetoolandthedataitgathered. Thiswasperformedviafactoranalysis
andmeasuredagainstconvergent,discriminant,andfitmeasures. Afterconfirmation,SEM
wasperformedwhichwasfurtherdividedintomediationanalysistoconfirmthepathof
calibration,directanalysisfortherelationshipbetweenthedesigncomponentandintegral
emotions,andmoderationanalysisfortheeffectofincidentalemotionsandAIreliability.
Alltestswereassessedbasedontheirstatisticalsignificanceandrigidity.
As for the data management, representative figures were computed based on the
aggregatemeasurementfromtheinitialtrialuptothetimeconsidered. Thisadheresto
therecommendationsbyYangetal.[81]onthedetectablemomentofdifference(i.e.,the
area under the curve). Since the method of use was SEM, design elements were coded
dichotomously(e.g.,+1,−1)torepresentchange. Formoderators,themultigrouptestwas
theapproachusedtoparalleltheobjectivesofthestudy. Particularly,forfactorsthatused
theLikertscale,conversionisbasedonthemidpoint.
ThemainprogramusedwasIBM’sAnalysisofMomentStructure(AMOS)graphics
version24. Inaddition,DesignExpert(DX)version13wasusedtogeneratethedesignof
theexperiment,andIBM’sStatisticalPackagefortheSocialScience(SPSS)version25.0was
usedforallstatisticaltestsoutsideSEM.Forconsistency,testingwasheldconstantundera
p<0.05significance.
4. Results
Thedatagatheringlastedfor15days. Sevenonboardingsessionswereconducted,
with at most 40 participants per session. The cumulative time in the main experiment
lasted 40 min, with access happening between 11:00 a.m. and 10:00 p.m. There were
norecordedethicalconcernsortestbedissues. Asforthepost-interview, 22.27%ofthe
participants joined, with an average call lasting 10 min. Lastly, those who scored 12 or
aboveontheMFQwerenotifiedatmosttwodaysaftertheexperimentandwerereferred
toaprofessionalhealthorganization.
4.1. DataScreening
Allinall,234participatedinthedatagathering. Afterfiltering,only202wereconsid-
eredforanalysisasthedatafromthosewhofailedtherequirements,testedpositiveforthe
depressiontest,anddidnotfinishtheexperimentwereremoved.
ThesummaryofthedemographicsispresentedinTable2. Structurally,thegender
countforthosewhodisclosedwasrelativelythesame(male—40.59%andfemale—44.55%),
withthemajoritybelongingtothemillennialagegroup(58.42%),followedbygeneration
X (22.77%), and generation Z (16.34%). Most were degree holders (vocational—9.41%;
college—68.81%; postgraduate—15.84%) and part of the working class (67.33%). Look-
ing at AI-related factors, the majority have at least five years of experience (more than
5years—71.78%;3to5years—25.25%;lessthan2years—2.97%),withalmostallhaving
previousinteractionexperiencewithanXAI(90.10%). Forthemoderators, mostofthe
participantsreportedpositiveincidentalemotions(71.78%),usedthehighAIreliability
version(62.87%),andwererecordedatthelaterstageofuse(56.44%).
Table2.Summaryofsubjects’demographics.
Type Count % Type Count %
Age EducationalAttainment
GenZ(18to23) 33 16.34% Elementary 0 0.00%
YoungerMillennial(24to30) 54 26.73% HighSchool 12 5.94%
OlderMillennial(31to39) 64 31.68% College 139 68.81%
YoungerGenX(40to47) 36 17.82% Masters 25 12.38%
OlderGenX(48to55) 10 4.95% PhD 7 3.47%
YoungerBoomer(56-65) 5 2.48% TechnicalVocational 19 9.41%

| Informatics2023,10,32 |     |     |     |     |     |     |     | 12of24 |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | ------ |
Table2.Cont.
|                            | Type           | Count | %      |            | Type                 |     | Count | %      |
| -------------------------- | -------------- | ----- | ------ | ---------- | -------------------- | --- | ----- | ------ |
| Gender                     |                |       |        | Occupation |                      |     |       |        |
|                            | Male           | 82    | 40.59% |            | Student              |     | 56    | 27.72% |
|                            | Female         | 90    | 44.55% |            | Employed(FullTime)   |     | 81    | 40.10% |
|                            | Prefernottosay | 30    | 14.85% |            | Employed(Part-Time)  |     | 13    | 6.44%  |
|                            |                |       |        |            | Unemployed           |     | 9     | 4.46%  |
| AIExperience               |                |       |        |            | Freelance/Contractor |     | 20    | 9.90%  |
| Laggards(Lessthan1year)    |                | 3     | 1.49%  |            | Self-employed        |     | 22    | 10.89% |
| LateMajority(1–2years)     |                | 3     | 1.49%  |            | Retired              |     | 1     | 0.50%  |
| EarlyMajority(3–4years)    |                | 15    | 7.43%  |            |                      |     |       |        |
| EarlyAdopters(4–5years)    |                | 36    | 17.82% |            |                      |     |       |        |
| Innovators(Morethan5years) |                | 145   | 71.78% |            |                      |     |       |        |
4.2. ExploratoryFactorAnalysis
Excellentresultsfromtheexploratoryfactoranalysis(EFA)supportedtheuseofthe
designedquestionnairetocapturethelatentvariablesofAIanxiety,incidentalemotion,
trustdisposition,perceivedusefulness,andperceivedtrust.
Primarily,the0.919Kaiser–Meyer–Olkin(KMO)measureandsignificantBartlett’stest
ofsphericity(p<0.001)highlightedthehighproportionofvarianceamongvariables[82]
(seeTable3). Thiswasfurtherprovenbythehighcommunalityextractionrangingbetween
0.947and0.958andhighcumulativevarianceforfivecomponenteigenvalueat88.710%.As
forloadings,theproposedfivedimensionswerecleanlyfactoredwithhighintercorrelation
scores(minimumof0.731)andnosignificantcross-loadingsunderaprincipalcomponent
analysis extraction at a varimax normalization (see Table 4). This highlighted that the
structure of the questions does not overlap due to its validity securing a highly stable
analysis[83].
Table3.Internalconsistencymeasures.
|     |     |     | ConsistencyMeasure        |     |     |     | Measurement |     |
| --- | --- | --- | ------------------------- | --- | --- | --- | ----------- | --- |
|     |     |     | Kaiser–Meyer–OlkinMeasure |     |     |     | 0.919       |     |
Bartlett’sTestofSphericity
|     |     |     | Approx.Chi-Square |      |     |     | 7055.358 |     |
| --- | --- | --- | ----------------- | ---- | --- | --- | -------- | --- |
|     |     |     |                   | df   |     |     | 253.000  |     |
|     |     |     |                   | Sig. |     |     | <0.000a  |     |
aSignificantatp<0.05.
Table4.Rotatedcomponentmatrix.
|                           |           |           |     | Incidental | Trust       | Perceived  | Perceived |     |
| ------------------------- | --------- | --------- | --- | ---------- | ----------- | ---------- | --------- | --- |
|                           | Dimension | AIAnxiety |     |            |             |            |           |     |
|                           |           |           |     | Emotion    | Disposition | Usefulness | Trust     |     |
| AIAnxietySocioTechnicalQ6 |           | 0.970     |     |            |             |            |           |     |
| AIAnxietySocioTechnicalQ5 |           | 0.960     |     |            |             |            |           |     |
| AIAnxietySocioTechnicalQ4 |           | 0.957     |     |            |             |            |           |     |
| AIAnxietyLearningQ3       |           | 0.956     |     |            |             |            |           |     |
| AIAnxietyConfigurationQ7  |           | 0.954     |     |            |             |            |           |     |
| AIAnxietyLearningQ1       |           | 0.953     |     |            |             |            |           |     |
| AIAnxietyConfigurationQ9  |           | 0.947     |     |            |             |            |           |     |
| AIAnxietyLearningQ2       |           | 0.939     |     |            |             |            |           |     |
| AIAnxietyConfigurationQ8  |           | 0.928     |     |            |             |            |           |     |
| IncidentalEmotionQ1       |           |           |     | 0.937      |             |            |           |     |
| IncidentalEmotionQ2       |           |           |     | 0.936      |             |            |           |     |
| IncidentalEmotionQ4       |           |           |     | 0.929      |             |            |           |     |
| IncidentalEmotionQ3       |           |           |     | 0.916      |             |            |           |     |

Informatics2023,10,32 13of24
Table4.Cont.
|     |     | Incidental |     | Trust |     | Perceived |     |     | Perceived |
| --- | --- | ---------- | --- | ----- | --- | --------- | --- | --- | --------- |
Dimension AIAnxiety
|     |     | Emotion |     | Disposition |     | Usefulness |     |     | Trust |
| --- | --- | ------- | --- | ----------- | --- | ---------- | --- | --- | ----- |
TrustDispositionQ4 0.987
TrustDispositionQ2 0.979
TrustDispositionQ3 0.978
TrustDispositionQ1 0.978
PercUsefulnessQ3 0.868
PercUsefulnessQ2 0.849
PercUsefulnessQ1 0.759
TrustQ1 0.806
TrustQ2 0.761
TrustQ3 0.731
Note:Extractionmethodviaprincipalcomponentanalysis;Rotationmethodviavarimaxwithkaisernormaliza-
tion;Rotationconvergedin6iterations.
4.3. ConfirmatoryFactorAnalysis
SamewiththefindingsfromtheEFA,confirmatoryfactoranalysis(CFA)alsoatteststo
thestructureofthedimensions(seeTable5).Fromthemodelvaliditytest,Cronbach’salpha
andaveragevarianceexplained(AVE)showedhighreliabilityandconvergentvalidity,
respectively,asallareabovethethresholdof0.70[84]. Moreover,divergentvalidityalso
follows the same trend with minimum shared variance (MSV) being below AVE and
maximumreliability(MaxR(H))beingabove0.70[83]. Allofthesewereachievedatan
excellentfittedconfirmatorymodelashighlightedinTable6. Collectively,themeasures
validatedthequestionnaire’sabilitytoexplainincidentalemotionandsoundnesstobe
usedforthehypothesistesting.
Table5.Modelvaliditymeasures.
|     | Dimension           |     | CR    |     | AVE   |     | MSV   |     | MaxR(H) |
| --- | ------------------- | --- | ----- | --- | ----- | --- | ----- | --- | ------- |
|     | AIAnxiety           |     | 0.988 |     | 0.904 |     | 0.101 |     | 0.989   |
|     | IncidentalEmotion   |     | 0.983 |     | 0.935 |     | 0.445 |     | 0.983   |
|     | TrustDisposition    |     | 0.989 |     | 0.957 |     | 0.017 |     | 0.992   |
|     | PerceivedUsefulness |     | 0.832 |     | 0.630 |     | 0.106 |     | 0.944   |
|     | PerceivedTrust      |     | 0.831 |     | 0.627 |     | 0.445 |     | 0.927   |
Note: CR—Cronbach’s alpha; AVE—average variance explained; MSV—minimum shared variance;
MaxR(H)—maximumreliability.
Table6.Confirmatoryfactoranalysisfitestimates.
|                | Type | Indices |     |     | Estimate |     |     | Threshold |     |
| -------------- | ---- | ------- | --- | --- | -------- | --- | --- | --------- | --- |
| AbsoluteFit    |      | RMSEA   |     |     | 0.039    |     |     | <0.06[73] |     |
|                |      | SRMR    |     |     | 0.045    |     |     | <0.08[85] |     |
| IncrementalFit |      |         | CFI |     | 0.991    |     |     | >0.95[86] |     |
|                |      |         | NFI |     | 0.961    |     |     | >0.95[85] |     |
χ2/df
| ParsimoniousFit |     |     |     |     | 1.301 |     |     | 1to3[85] |     |
| --------------- | --- | --- | --- | --- | ----- | --- | --- | -------- | --- |
Note:RMSEA—RootMeanSquareErrorofApproximation;SRMR—StandardizedRootMeanSquareResidua;
CFI—ComparativeFitIndex;NFI—NormedFitIndex;χ2/df—Chi-squaredperDegreesofFreedom
4.4. StructuralEquationModelling
Asignificantandgood-fittingmodelwasachievedfromthe2000bootstrappedSEM
run. As summarized in Table 7, all representative measures from the three types of fit
belongtothethresholdlimit. Thishighlightedtheconsistencyofthedataanditsability
toreproducethehypothesizedrelationship. Further,therewerenosuggestedadditional
structurallinksfromthemainvariablessymbolizingarigidmodelstructure.

| Informatics2023,10,32 |     |     |     |     |     |     |     |     | 14of24 |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
Table7.Structuralequationmodelfitestimates.
|     |     |     | Type           |     | Indices |     | Estimate | Threshold |     |
| --- | --- | --- | -------------- | --- | ------- | --- | -------- | --------- | --- |
|     |     |     | AbsoluteFit    |     | RMSEA   |     | 0.051    | <0.06[73] |     |
|     |     |     |                |     | SRMR    |     | 0.045    | <0.08[87] |     |
|     |     |     | IncrementalFit |     | CFI     |     | 0.988    | >0.95[86] |     |
|     |     |     |                |     | NFI     |     | 0.966    | >0.95[85] |     |
χ2/df
|     |     |     | ParsimoniousFit |     |     |     | 1.524 | 1to3[85] |     |
| --- | --- | --- | --------------- | --- | --- | --- | ----- | -------- | --- |
Note:RMSEA—RootMeanSquareErrorofApproximation;SRMR—StandardizedRootMeanSquareResidual;
CFI—ComparativeFitIndex;NFI—NormedFitIndex;χ2/df—Chi-squaredperDegreesofFreedom.
4.4.1. MediationEffectAnalysis
Resultsidentifiedthatbothaffectiveandcognitiveelementsfunctionasmediators
inthetrustandreliancecalibrationprocessfromXAI(seeTable8). Foraffect,anxiously
suspiciouswastheonlyinsignificantmediator. Interestinglysurprisedmediatestheappre-
ciationoftheexplanationform,trustingmediatesexplanationformandsupplementary
information,andcommunicationstyleandsupplementaryinformationforfearfullydis-
mayed. Relatingtoreliance,theinsignificanceofanxiouslysuspiciouswasstillseenwith
thepath comingfromit whenmediated byperceived trust. As forthe cognitive paths,
allproposedmediationofperceivedtrustandusefulnessfromthedesignelementswere
significant. Overall,thesefindingshighlighttheinitialproposedideafromthestudythat
affectivepathcalibrationexistsintheuseofXAI.
Table8.Mediationeffectanalysis.
| Group |     | From            |     | Mediator               |     | To             | Std.Est. | p-Value | Mediated?a |
| ----- | --- | --------------- | --- | ---------------------- | --- | -------------- | -------- | ------- | ---------- |
|       |     |                 |     | InterestinglySurprised |     |                | 0.289    | 0.001   | Yes        |
|       |     |                 |     | Trusting               |     |                | 0.163    | 0.001   | Yes        |
|       |     | ExplanationForm |     |                        |     | PerceivedTrust |          |         |            |
|       |     |                 |     | FearfullyDismayed      |     |                | −0.020   | 0.159   | No         |
|       |     |                 |     | AnxiouslySuspicious    |     |                | 0.001    | 0.523   | No         |
−0.015
|                |                          |          |     | InterestinglySurprised |     |                |        | 0.489 | No  |
| -------------- | ------------------------ | -------- | --- | ---------------------- | --- | -------------- | ------ | ----- | --- |
|                |                          |          |     | Trusting               |     |                | −0.037 | 0.067 | No  |
| AffectiveTrust | CommunicationStyle       |          |     |                        |     |                |        |       |     |
|                |                          |          |     | FearfullyDismayed      |     | PerceivedTrust | −0.108 | 0.015 | Yes |
|                |                          |          |     | AnxiouslySuspicious    |     |                | −0.017 | 0.527 | No  |
|                |                          |          |     | InterestinglySurprised |     |                | 0.064  | 0.068 | No  |
|                |                          |          |     | Trusting               |     |                | 0.078  | 0.046 | Yes |
|                | SupplementaryInformation |          |     |                        |     | PerceivedTrust |        |       |     |
|                |                          |          |     | FearfullyDismayed      |     |                | 0.068  | 0.020 | Yes |
|                |                          |          |     | AnxiouslySuspicious    |     |                | 0.005  | 0.475 | No  |
|                | InterestinglySurprised   |          |     |                        |     |                | 0.239  | 0.001 | Yes |
|                |                          | Trusting |     |                        |     |                | 0.171  | 0.001 | Yes |
AffectiveReliance FearfullyDismayed PerceivedTrust Reliance −0.070 0.013 Yes
|     | AnxiouslySuspicious |                 |     |     |     |     | −0.010 | 0.509 | No  |
| --- | ------------------- | --------------- | --- | --- | --- | --- | ------ | ----- | --- |
|     |                     | ExplanationForm |     |     |     |     | 0.023  | 0.009 | Yes |
CognitiveTrust CommunicationStyle PerceivedUsefulness PerceivedTrust 0.211 0.008 Yes
|     | SupplementaryInformation |     |     |     |     |     | 0.010 | 0.036 | Yes |
| --- | ------------------------ | --- | --- | --- | --- | --- | ----- | ----- | --- |
CognitiveReliance PerceivedUsefulness PerceivedTrust Reliance −0.099 0.007 Yes
Note:Std.Est.—StandardEstimate;aEvaluatedatp-value<0.05.
4.4.2. DirectEffectAnalysis
Consideringtheresultsfromthemediationanalysis,relationshipsanddesignrecom-
mendationsweresuccessfullydrawnfromthedirecteffectanalysis. Ofthe21hypothesized
directrelationships,only12wereidentifiedtobestatisticallysupported(seeTable9). As
forthedesigntoemotionsgroup,explanationformsignificantlyrelatestointerestingly
surprisedandtrustingemotions. Communicationstylewassignificanttoaffectfearfully
dismayedandanxiouslysuspicious. Lastly,thepresenceofsupplementaryinformation
decreasesfearfullydismayed.

| Informatics2023,10,32 |     |     |     |     | 15of24 |
| --------------------- | --- | --- | --- | --- | ------ |
Table9.Directeffectanalysis.
| Group | From            | To                     | Std.Est. | p-Value | Supporteda |
| ----- | --------------- | ---------------------- | -------- | ------- | ---------- |
|       |                 | InterestinglySurprised | 0.530    | 0.001   | Yes        |
|       | ExplanationForm | Trusting               | 0.419    | 0.002   | Yes        |
(+Example,−Feature,Rule)
|     |                    | FearfullyDismayed      | 0.126  | 0.339 | No  |
| --- | ------------------ | ---------------------- | ------ | ----- | --- |
|     |                    | AnxiouslySuspicious    | −0.032 | 0.806 | No  |
|     |                    | InterestinglySurprised | −0.070 | 0.488 | No  |
|     | CommunicationStyle | Trusting               | −0.257 | 0.081 | No  |
DesigntoEmotions
|     | (+Logic,−Human) | FearfullyDismayed | 1.822 | 0.001 | Yes |
| --- | --------------- | ----------------- | ----- | ----- | --- |
Yesb
|                    |                          | AnxiouslySuspicious    | 1.783  | 0.001 |     |
| ------------------ | ------------------------ | ---------------------- | ------ | ----- | --- |
|                    |                          | InterestinglySurprised | 0.117  | 0.068 | No  |
|                    | SupplementaryInformation | Trusting               | 0.201  | 0.053 | No  |
|                    | (+With,−Without)         | FearfullyDismayed      | −0.432 | 0.006 | Yes |
|                    |                          | AnxiouslySuspicious    | −0.227 | 0.059 | No  |
|                    | InterestinglySurprised   |                        | 0.545  | 0.001 | Yes |
|                    | Trusting                 |                        | 0.390  | 0.001 | Yes |
| EmotionstoTrust    |                          | PerceivedTrust         |        |       |     |
|                    | FearfullyDismayed        |                        | −0.158 | 0.017 | Yes |
|                    | AnxiouslySuspicious      |                        | −0.024 | 0.539 | No  |
|                    | SupplementaryInformation |                        | 0.045  | 0.224 | Noc |
| DesigntoUsefulness | CommunicationStyle       |                        | −0.940 | 0.002 | Yes |
PerceivedUsefulness
|     | ExplanationForm |     | 0.100 | 0.006 | Yes |
| --- | --------------- | --- | ----- | ----- | --- |
UsefulnesstoTrust PerceivedUsefulness PerceivedTrust 0.225 0.007 Yes
| TrusttoReliance | PerceivedTrust | Reliance | 0.439 | 0.001 | Yes |
| --------------- | -------------- | -------- | ----- | ----- | --- |
Note:Std.Est.—StandardEstimate;aEvaluatedatp-value<0.05;bunsupportedfromthemediationanalysis;
csupportedfromthemediationanalysis.
Foremotiontotrust,allemotionsasidefromanxiouslysuspicioushaveasignificant
relationship to perceived trust. Particularly, users that felt interestingly surprised and
trusting reported higher perceived trust, while reporting the opposite when fearfully
dismayedwasfelt. Asforthecognitive-basedgroups,perceivedusefulnesshasapositive
relationshipwithperceivedtrust.Thisstemmedfromexplanationformandcommunication
styledesignelementsbeingsignificant. Supplementaryinformation,althoughidentifiedbe
partofthemediatedpath,wasinsignificantforthedirecttestshowingthepossibilityof
partialmediation[88]. Lastly,perceivedtrusthasasignificantpositiverelationshipwith
reliance. Giventhateachdesignwasdichotomouslycodedfortheanalysis,translatingthe
resultstodesignmeans
• Example-basedexplanationincreasesinterestinglysurprised,trustingemotions,and
perceivedusefulness,whilefeature-andrule-basedexplanationdecreasesthem.
• Logicroboticincreasesfearfullydismayedplusanxiouslysuspiciousemotionsandde-
creasesperceivedusefulness,whilehumanizedcommunicationfunctionstheopposite.
• Thepresenceofsupplementaryinformationdecreasesfearfullydismayedemotions,
whiletheabsenceofitincreasestheeffect.
4.4.3. ModerationEffectAnalysis
Onlyhalfofthemoderatorswereidentifiedtohaveasignificanteffect. Asshown
in Table 10, the nested comparisons for AI anxiety and incidental emotions for human
p-value
factors, while reliability and experience for the AI factors received a less than
0.05,highlightedthesubstantialconcurringdifferencefromthefulldefaultmodel. With
theseresults, deeperanalysiswasperformedtoidentifythesourceofmoderationona
per-pathbasis.

| Informatics2023,10,32 |     |     |     |     |     |     |     |     |     |     |     |     |     | 16of24 |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
Table10.Globalmulti-groupmoderationeffectanalysis.
| Group |     |     | ModerationModel   |           |     |     |     | DF     | CMIN   |     | p-Value |     | Moderated?a |     |
| ----- | --- | --- | ----------------- | --------- | --- | --- | --- | ------ | ------ | --- | ------- | --- | ----------- | --- |
|       |     |     |                   | AIAnxiety |     |     |     | 21.000 | 41.212 |     | 0.005   |     |             | Yes |
|       |     |     | IncidentalEmotion |           |     |     |     | 21.000 | 63.314 |     | 0.000   |     |             | Yes |
HumanFactors
|     |     |     | TrustDisposition   |               |     |     |     | 21.000 | 21.940 |     | 0.403 |     |     | No  |
| --- | --- | --- | ------------------ | ------------- | --- | --- | --- | ------ | ------ | --- | ----- | --- | --- | --- |
|     |     |     |                    | XAIExperience |     |     |     | 21.000 | 22.810 |     | 0.354 |     |     | No  |
|     |     |     |                    | AIReliability |     |     |     | 21.000 | 73.497 |     | 0.000 |     |     | Yes |
|     |     |     | LearningCapability |               |     |     |     | 21.000 | 16.260 |     | 0.755 |     |     | No  |
AIFactors
|     |     |     |     | Brand      |     |     |     | 21.000 | 13.083 |     | 0.906 |     |     | No  |
| --- | --- | --- | --- | ---------- | --- | --- | --- | ------ | ------ | --- | ----- | --- | --- | --- |
|     |     |     |     | Experience |     |     |     | 21.000 | 34.021 |     | 0.036 |     |     | Yes |
a
Note: DF—Degrees of Freedom; CMIN—Chi-square statistics; p-value—Significance; Evaluated at
p-value<0.05.
Theresultsfromtheindividualfittestforallmoderationrunsalsofavoredtheglobal
results.AsshowninTable11,theCFI,SRMR,andPCloseallpassedthethresholdsassuring
capabilityforfurtherexploration. Takenotethatthesearethemeasuresusedconsidering
thedataweretruncatedduetothestratification. Moreso,theseareinsensitivewithlow
samplesizeandcorrespondingdegreesoffreedom[87,89].
Table11.Localmoderationtestfitscores.
| Group |     | ModerationModel |     |     |     |               | Runs |     | CFI   |     | SRMR  | PClose |     | Fit?a |
| ----- | --- | --------------- | --- | --- | --- | ------------- | ---- | --- | ----- | --- | ----- | ------ | --- | ----- |
|       |     |                 |     |     |     | HighAIAnxiety |      |     | 0.986 |     | 0.032 | 0.054  |     | Yes   |
AIAnxiety
|     |     |     |     |     |     | LowAIAnxiety |     |     | 1.000 |     | 0.021 | 0.754 |     | Yes |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ----- | --- | ----- | ----- | --- | --- |
HumanFactors
|     |     |     |     |     |     | PositiveIncidentalEmotion |     |     | 1.000 |     | 0.008 | 0.892 |     | Yes |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ----- | --- | ----- | ----- | --- | --- |
IncidentalEmotion
|     |     |     |     |     |     | NegativeIncidentalEmotion |     |     | 0.994 |     | 0.028 | 0.283 |     | Yes |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ----- | --- | ----- | ----- | --- | --- |
|     |     |     |     |     |     | HighAIReliability         |     |     | 1.000 |     | 0.014 | 0.587 |     | Yes |
AIReliability
|     |     |     |     |     |     | LowAIReliability |     |     | 0.952 |     | 0.051 | 0.050 |     | Yes |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ----- | --- | ----- | ----- | --- | --- |
AIFactors
|     |     |     |     |     |     | ShortExperience |     |     | 1.000 |     | 0.008 | 0.892 |     | Yes |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ----- | --- | ----- | ----- | --- | --- |
Experience
|     |     |     |     |     |     | LongExperience |     |     | 0.994 |     | 0.028 | 0.283 |     | Yes |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ----- | --- | ----- | ----- | --- | --- |
Note:CFI—ComparativeFitIndex;SRMR—StandardizedRootMeanSquareResidual;PClose—pofclosefit;
aConsideredfitifallmeasurespassedthethreshold:CFI>0.95,SRMR<0.08,PClose>0.05[85].
Thelocaleffectsurfacedvaryingdegreesofmoderationperrelationship,aspresented
inTable12. ForAIanxiety,thedifferenceseenwasmainlythatvaluesarehigherwiththe
lowgroupthanwiththehighgroupinthreekeyareas. First,whenfearfullydismayed
emotionswerefelt,userswithhighAIanxietyexperiencedlowerperceivedtrustthanthose
whohavelowAIanxiety(β=−0.059vs. β=0.021,z-score=2.195andp-value=0.014).
Second,whenexposedtoalogic-roboticcommunicationstyle,usersinthehighgrouphave
lowerperceivedusefulnessthanthelowgroup(β=0.804vs. β=1.185, z-score=1.762
and p-value = 0.039). Lastly, for the relationship between perceived trust and reliance,
usersinthehighgrouphavelowerreliancethanthelowgroup(β=0.804vs. β=1.185,
z-score=1.762andp-value=0.039).
Table12.Localmulti-groupmoderationdifferenceeffectanalysis.
|     | From |     |     |     | To  |     |     | Est. p-Value  |     | Est.         | p-Value | z-Score |     | p-Valuea |
| --- | ---- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | ------- | ------- | --- | -------- |
|     |      |     |     |     |     |     |     | HighAIAnxiety |     | LowAIAnxiety |         |         |     |          |
FearfullyDismayed PerceivedTrust −0.059 0.044 0.021 0.331 2.195 0.014
|     |     |     |     |     |     |     |     | −0.970 |     | −0.790 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- |
CommunicationStyle PerceivedUsefulness 0.000 0.000 2.442 0.007
|     | PerceivedTrust |     |     |     | Reliance |     |     | 0.804 | 0.000 | 1.185 | 0.000 |     | 1.762 | 0.039 |
| --- | -------------- | --- | --- | --- | -------- | --- | --- | ----- | ----- | ----- | ----- | --- | ----- | ----- |

Informatics2023,10,32 17of24
Table12.Cont.
From To Est. p-Value Est. p-Value z-Score p-Valuea
Pos.Inci.Emotion Neg.Inci.Emotion
SupplementaryInformation InterestinglySurprised −0.979 0.026 0.457 0.209 2.513 0.006
SupplementaryInformation Trusting −1.001 0.032 0.137 0.725 1.868 0.031
Trusting PerceivedTrust −0.017 0.681 0.174 0.000 4.081 0.000
FearfullyDismayed PerceivedTrust −0.045 0.148 0.023 0.035 2.071 0.019
CommunicationStyle PerceivedUsefulness −1.058 0.000 −0.875 0.000 2.096 0.018
PerceivedUsefulness PerceivedTrust 0.196 0.029 0.028 0.331 1.780 0.038
HighAIReliability LowAIReliability
Trusting PerceivedTrust 0.064 0.076 0.223 0.000 3.416 0.000
FearfullyDismayed PerceivedTrust −0.073 0.026 0.027 0.250 2.479 0.007
ShortExperience LongExperience
Trusting PerceivedTrust 0.184 0.000 0.095 0.012 1.859 0.032
FearfullyDismayed PerceivedTrust 0.018 0.177 −0.046 0.117 1.987b 0.023
Note: Pos.—Positive; Neg.—Negative; Inci.—Incidental; Est.—Unstandardized Estimate; a Evaluated at
p-value<0.05;bSignificantz-scoredifferenceandp-valuebutwithinsignificantpermoderatedrunestimates.
Forincidentalemotions,sixpathswereidentifiedtobesignificantlymoderated. In
termsofdampeningeffect,whensupplementaryinformationwasprovided,userswithpos-
itiveincidentalemotionsexperiencedlowerinterestinglysurprisedandtrustingemotions
thanthosewithnegative(β=−0.979vs. β=0.457,z-score=2.513andp-value=0.006and
β=−1.001vs. β=0.137,z-score=1.868andp-value=0.031). Next,theeffectofperceived
trustislowerforthepositivegroupthanthenegativegroupwhentrustingandfearfully
dismayedemotionswerefelt(β=−0.017vs. β=0.174,z-score=4.081andp-value=0.000
andβ=−0.045vs.β=0.023,z-score=2.071andp-value=0.019).Bothconditionshighlight
thatpositiveincidentalemotionsresultedinadecreaseineffecttowardssupplementaryin-
formationandperceivedtrust. Incontrary,therearealsoamplificationeffectsthatsurfaced
fromthemoderation. Firstwhenlogic-roboticcommunicationstylewasused,thenega-
tivegrouphadahigherperceptionofusefulnessthanthepositivegroup(β=−0.875vs.
β=−1.058,z-score=2.096andp-value=0.018). Inaddition,perceivedtrustwashigherin
thepositivegrouprelativetoperceivedusefulness(β=0.196vs. β=0.028,z-score=1.780
andp-value=0.038).
Asidefromincidentalemotion,thesamemoderatedpathsforreliabilityandexperi-
enceweredetermined. Specifically,thesearetheaffectivepathsfromtrustingandfearfully
dismayedemotiontoperceivedtrust.Forbothinstances,lowAIreliabilityandshortexperi-
encehavehigherperceivedtrustwhentrusting(β=0.223vs. β=0.064,z-score=3.416and
p-value=0.000;β=0.184vs. β=0.095,z-score=1.859andp-value=0.032)andfearfully
dismayedemotions(β=0.027vs. β=−0.073,z-score=2.479andp-value=0.007;β=0.018
vs. β=−0.046,z-score=1.987andp-value=0.023)wereexperienced.
5. Discussion
Consideringthequantitativeresultsfromtheexperimentandsubsequentinterviews,
the study was able to successfully analyze the postulated objectives for the end-user
XAIconsideration.
5.1. Objective1: ConfirmationofAffectiveTrustCalibrationforXAI
Affectwasdeterminedtobeavariableroutefortrustcalibration. Thiswasestablished
throughthecausalrelationshiptest,anchoredonthemediationanalysisoftheSEM.No-
tably,emotionsbelongingtothegroupofinterestinglysurprised(e.g.,interested,excited,
surprised,pleased,andamazed),trusting(e.g.,happy,confident,secure,proud,andtrust-
ing),andfearfullydismayed(e.g.,dismayed,afraid,fear,angry,andsad)wereidentified
to be significant mediators for trust and reliance in a behavioral and use change view.
Ontheotherhand,anxiouslysuspicious(e.g.,suspicious,concerned,confused,nervous,

Informatics2023,10,32 18of24
andanxious)emotionswereunsupported. Intermsofrelationships, bothinterestingly
surprisedandtrustingemotionshaveapositiverelationtotrust,whilefearfullydismayed
observeanegativestance. Allofthesewerevalidatedjointlywiththesignificantmediation
ofthecognitiverouteshowingthattrustcalibrationcanhappenonthetworoutes.
Insights from the interview also second the confirmation of the variability of the
affective route alongside the cognitive route. By synthesizing the claims, distinctively,
participantscanbedividedintotwotypes: peoplewhovalueemotionsandpeoplewho
value information. The former works when intuition or perception were the mode of
assessment,whilethelatterwheninformationqualitydeliberationhappens. Thisobser-
vationresonateswiththeelaborationlikelihoodmodel(ELM)ofpersuasionofPettyand
Cacioppo[90],whichisessentiallyatheoryaboutthethinkingprocessinthecontextof
persuasionvariables. Contextually,thisiscalledthecentralroutewhenhighelaboration
happensonthedetailpresented,whileperipheralwhenlow. Further,theinterviewalso
uncoveredthesameconsiderationofmotivationandabilityfromELMwhichdictateswhat
routeoftrustcalibrationtheuserwillfollow. Iftheyhavehighmotivation(i.e.,investedin
thetaskreward,highcuriositywiththeXAI,aimingforahighscoreintheexperiment)
andhighability(i.e.,understandingoftheinformationonXAI,perceivedexpertisewith
thetask),theywillfollowacognitivepathorcentralroute,andaffectiveorperipheralfor
theopposite.
Overall, these findings offset the running hypothesis on how XAI induces trust as
determinedinpreviousreviewstudies[8,24]. ThisshowsthatXAIworkssimilarlytoother
cuesinthefieldofHCIthattransverseonbothtrustcalibrationroutes. Consideringthis
studyisapioneerfortestingtheaffectiveroute,furtherstudiescanworkonmeasuring
such elaboration to analyze the differences in various contexts to ultimately check the
variabilityofeachroute.
5.2. Objective2: EffectofDifferentXAIDesignsandImportanceofEnd-UserCentricApproach
Forthedesign,twoimportantobservationswererecognized. First,thepre-studywas
abletoidentifythatcertaindesignelementsarebeingconsideredintheutilityassessment
ofanXAI.Fromthesurvey,explanationform,communicationstyle,anduseofsupplemen-
taryinformationrestonthetopoftheperceivedimportantdesignelementlist. Notably,
reasoningfromtheinterviewshowedthattheseareselectedastheyprovidetheability
toseetherulesAIrules, giveanideaoftheinformationusedinsuchdecision-making,
and learn the details of the process. This shows that perceived important XAI design
mainlyechoestheoriginalpurposeofXAIamongotherthings. Forexample,aesthetics
canbeconsidered. Textsizeandcoloraredesignelementsbutonlyveryfewnotedtheir
importanceastheydonotperformacriticalroleinexplaining.
ThenextobservationisthatXAIdesignelementsplayasignificantrolebothforthe
affectiveandcognitivetrustcalibrationroute,withchangingeachconfigurationproducing
different results. As deduced via SEM, design change will yield distinctive effects on
emotionsandcognitiveevaluation(seeTable13forthesummaryofeffects). Thevarying
effecttheoreticallyimpliesthatforXAI,designfunctionsonadeeperlevel—amicroview
asconfigurationratherthanamacroviewthroughcategoricaleffect.
The key findings support and explain the significant elaboration routes and ELM
parallelism reflected in the first objective. The second objective unfolds that in the de-
velopment of XAI, aside from the information it carries, the design also matters. More
so,thecommonconsensushighlightsthesubsistenceofageneralstructureforpossible
designprioritizationwhendevelopinganXAI.Thismeansthattheidentifiedeffectscanbe
leveragedtocreateatargetedXAIforanoptimizedutilityfunctionforanXAI.Forexample,
toincreasetrustandreliance,anXAIfeaturinganexample-basedexplanationformcanbe
tappedtohaveapositivechangetointerestinglysurprisedandtrustingemotions,orcan
usehuman-likecommunicationtosimplyremovethefeelingoffearfullydismayedand
anxiouslysuspiciousemotions. Overall,theobservationsshedlightontheimportanceof
designanditsvariabilityforanend-user-centricXAI.

Informatics2023,10,32 19of24
Table13.Summaryofaffectandcognitivechangeperdesignelement.
Interestingly Fearfully Anxiously Perceived
DesignElement Type Trusting
Surprised Dismayed Suspicious Usefulness
Example + + × × +
ExplanationForm
FeatureandRule − − × × −
Logic × × + + −
CommunicationStyle
Human × × − − +
With × × − × ×
SupplementaryInformation
Without × × + × ×
Note:“+”meansincreasing;“−”meansdecreasing;“×”unsupportedrelationship.
5.3. Objective3: ExternalFactorsDelimitingXAIEffect
Theresultsalsoidentifiedthatexternalfactorsareapointworthnotingwhendevel-
opinganXAI,withbothhuman(i.e.,AIanxietyandincidentalemotions)andAIfactors
(i.e., reliability and experience) being viable. This implies that XAI utility effectiveness
worksbeyondthedesignandinformationassituationalfactorsarealsosignificant. For
example,supplementaryinformationwillonlycauseasignificantnegativeaffectivechange
on interestingly surprised if they have positive incidental emotions. Viewing the XAI
developmentinthislightfurtherdenotesthattomitigatetransparency,designshouldbe
contextualizedonthesituationalneedoftheimplementation.
Inaddition,commentariesfromtheinterviewsuggestthatthemoderationworkson
a per AI-type experience basis. For example, a user with a bad experience with image
recognitioncarriedthisintheexperimentwithhigheranxiety,negativeincidentalemotion,
andlowerperceptionoftheAIreliability,eventhoughtheyhaveagoodexperiencerelative
totheothertypes. ThisinfersthatXAI,beingacomplementaryelement,wasevaluated
aftertheAIsystemwasassessed,openingtheideathattheXAIeffectmightdifferforother
AIusecases. Apossibleextensionofthestudycanbeperformedtocheckthisidea.
6. Conclusions
Explainableartificialintelligence(XAI)hassuccessfullyaddressedtheblackboxtrust
problemofartificialintelligence(AI)byallowinguserstogainahuman-levelunderstanding
ofhowAIworks,eveniftheyhavelimitedknowledgeonthecomplexmachinelearning
algorithms that power it. However, concerns that current XAI techniques have been
delimitedintermsoftheirapplicabilityandimpacthavebeenhighlightedintherecent
years. Particularly,theexplorationhasdeterminedthatitfocusesmoreontheneedsof
developersandnotend-users,puttingAIadoptioninacriticalposition. Toprovidethe
necessaryviewpoint,thisstudyaimedtoexploreend-user-centricXAI.
Forthefirstobjective,whichaimstodeterminehowanend-usercalibratestrustfrom
XAI,itwasidentifiedthatitnotonlyservesasacognitiveresourcebutalsoasanaffective
cuefortrustandreliancechange. Effectively,thisstudyarguesthatXAIcanbeusedas
aninformationresourceandirrationallyviaemotionsthroughitsaffectivecontributions.
Continuingthat,anotherclaimidentifiedinthestudyisthatinformationcarriedoutby
the XAI is not the only determinant for both routes. The study tested and identified
thatdesign—ormannerbywhichXAIispresented—canalsoalteritseffectiveness. This
answersthesecondobjectiveregardingthefactorsthatcanviablychangetrustfroman
XAI.Lastly,asforthethirdandfourthobjective,whichlookedonthemoderatingfactors
inthetrustcalibrationprocess,evidenceshowedthathumanandAIfactorswerecapable
toinfluencetheeffect. Thisincludesanxietyandincidentalemotionfortheformer,while
AI reliability and experience for the latter. Overall, the study successfully filled in the
theoreticalgapacknowledgedfromtheresearchstream. Itopenedanewunderstandingof
theroutesbywhichXAIcalibratestrust,theimportanceofitsdesign,andexternalfactors
thatmayalteritseffectiveness.

Informatics2023,10,32 20of24
6.1. Implications
Consideringthefindingsfromthestudy,severalimplicationscanbedrawnbothin
theoreticalandmanageriallandscapes. Fortheoretical,asthisstudyviablydeterminedthat
XAIalsofunctionsintheaffectivetrustroute,itopensanewpathofresearchregarding
XAI effectiveness and subsequently poses important delimitation on previous research
thatonlyapproachedcalibrationthroughcognitiveroute. Possibly,revisitingsuchstudies
canbecarriedouttofirmupthefindingsrelativetotheimportanceofintegralemotions.
In terms of development, the study also creates a new paradigm on the course of XAI
improvementresearch.
Forthemanagerial,theresultscreateabetterpositionfortheimplementorsandusers.
Fortheformer,developersanddesignerscanusethefindingsonhowtobetterleverage
the effect of XAI towards trust. For instance, they can reorient the XAI to induce more
positiveemotionsoruseXAImoreonsystemswheretheprimarycustomersarethosewith
highanxiety(e.g.,telehealthapplications,banking,security,driving). Movingon,forthe
users,iftheresultsareoperationalized,theycanhaveabetterinteractionwithAIsystems,
possiblyallowingeffectiveadoption.
Asidefromthepositiveimplications,anothersidethatcanbedrawnfromtheresults
isthepossibilityofmisusingXAI.Fromthefindings,ithighlightsthatnotallusersuse
XAIasaninformationresourceformentalmodelcalibration;someonlyuseitasacue. In
addition,designcanmanipulateemotionsthatlateraffecttrustandreliance. Inthischain,
faultyandmanipulativeXAIcanbesimplyshowninthesystemandbeeffectiveifthe
designcanproduceapositiveeffectontheuser.
6.2. LimitationsandDirectionforFutureResearch
Althoughthestudyhasfilledinanimportantresearchgapandhasfollowedawell-
planned methodology, there have been limitations that should be addressed for future
research. First,thestudycanbeextendedandretestedunderdifferentdomains. Thisis
recommendedtostrengthentheclaimsfromthestudyandtoidentifythelimitationsof
therelationship. Possibly,differentpurpose,levelofsensitivity,andstakeholderscanbe
viewed. Inlinewiththat, secondly, thestudycanbeexpandedtocheckonothertypes
ofXAIotherthanthetestedtypeinthestudy. Intheexperiment,thefocushasbeenon
visualimagerytypesinceitcomplementsthenatureoftheAIsystemselected(i.e.,image
recognition). Othertypessuchastreediagramsortextualcanbetested. Third,moderator
testingcanbeimprovedbyexpandingitslimits. Forinstance,theexperiencecanbeviewed
foralongertimeframe(e.g., 2weeks)tohaveabroaderandmorerealisticviewofthe
relationships. Thisisrecommendedasthepost-interviewsurfaceditonmultipleoccasions.
Lastly,acrossdemographicalviewcanbeconductedtocheckondifferencesbetweenless
andhighlyadoptedAIcommunitiesasthisdirectlyaffectstheuseofXAI.
AuthorContributions: Conceptualization,E.B.andR.S.;methodology,E.B.andR.S.;experiment
testbed,E.B.;validation,E.B.andR.S.;formalanalysis,E.B.;investigation,E.B.;datacuration,E.B.;
writing—original draft preparation, E.B.; writing—review and editing, E.B.; visualization, E.B.;
supervision,R.S.;projectadministration,E.B.andR.S.;fundingacquisition,E.B.andR.S.Allauthors
havereadandagreedtothepublishedversionofthemanuscript.
Funding:ThisresearchandtheAPCwerefundedbyDeLaSalleUniversity—Manila.
InstitutionalReviewBoardStatement:Theethicalaspectsofthisresearchhavebeenapprovedby
theSocialScienceEthicsReviewBoard(SSERB)ofthePhilippineSocialScienceCouncil(Reference
Code:CB-22-20on27June2022).
InformedConsentStatement:Informedconsentwasobtainedfromallsubjectsinvolvedinthestudy.
DataAvailabilityStatement:Dataarenotpubliclyavailable,thoughthedatamaybemadeavailable
onrequestfromthecorrespondingauthor.

Informatics2023,10,32 21of24
Acknowledgments:Theresearchteamwouldliketoacknowledge80/20DesignLabsfortheirhelp
inthedevelopmentoftheexperimenttestbed,AngelimarieMiguelandWiraMadriafortheiraid
inthedatacurationandprocessing,andNaomiBernardo,EdgardoBernardo,NoelBernardo,and
ChristianeWillitsfortheirtechnicalsupportandmaterialdonationsusedintheexperiment.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.Thefundershadnoroleinthedesign
ofthestudy;inthecollection,analyses,orinterpretationofdata;inthewritingofthemanuscript;or
inthedecisiontopublishtheresults.
References
1. Lu,Y.ArtificialIntelligence: ASurveyonEvolution,Models,ApplicationsandFutureTrends. J.Manag. Anal. 2019,6,1–29.
[CrossRef]
2. Jordan, M.I.; Mitchell, T.M.MachineLearning: Trends, Perspectives, andProspects. Science2015, 349, 255–260. [CrossRef]
[PubMed]
3. Rai,A.ExplainableAI:FromBlackBoxtoGlassBox.J.Acad.Mark.Sci.2020,48,137–141.[CrossRef]
4. Doshi-Velez,F.;Kim,B.TowardsARigorousScienceofInterpretableMachineLearning.arXiv2017,arXiv:1702.08608.
5. Castelvecchi,D.CanWeOpentheBlackBoxofAI?Nat.News2016,538,4.[CrossRef]
6. Schmidt,P.;Biessmann,F.QuantifyingInterpretabilityandTrustinMachineLearningSystems.arXiv2019,arXiv:1901.08558.
7. Kliegr,T.;Bahník,Š.;Fürnkranz,J.AReviewofPossibleEffectsofCognitiveBiasesonInterpretationofRule-BasedMachine
LearningModels.Artif.Intell.2021,295,103458.[CrossRef]
8. Linardatos,P.;Papastefanopoulos,V.;Kotsiantis,S.ExplainableAI:AReviewofMachineLearningInterpretabilityMethods.
Entropy2020,23,18.[CrossRef][PubMed]
9. Weitz,K.;Hassan,T.;Schmid,U.;Garbas,J.-U.Deep-LearnedFacesofPainandEmotions:ElucidatingtheDifferencesofFacial
ExpressionswiththeHelpofExplainableAIMethods.TMTech.Mess.2019,86,404–412.[CrossRef]
10. Preece,A.Asking‘Why’inAI:ExplainabilityofIntelligentSystems—PerspectivesandChallenges.Intell.Sys.Acc.Fin.Manag.
2018,25,63–72.[CrossRef]
11. Venkatesh,V.AdoptionandUseofAITools: AResearchAgendaGroundedinUTAUT.Ann. Oper. Res. 2022,308,641–652.
[CrossRef]
12. Chowdhary,K.R.FundamentalsofArtificialIntelligence;Springer:NewDelhi,India,2020;ISBN978-81-322-3970-3.
13. Lewis,M.;Li,H.;Sycara,K.DeepLearning,Transparency,andTrustinHumanRobotTeamwork. InTrustinHuman-Robot
Interaction;Elsevier:Amsterdam,TheNetherlands,2021;pp.321–352.ISBN978-0-12-819472-0.
14. Savage,N.BreakingintotheBlackBoxofArtificialIntelligence.Nature2022.[CrossRef]
15. Mohseni,S.;Zarei,N.;Ragan,E.D.AMultidisciplinarySurveyandFrameworkforDesignandEvaluationofExplainableAI
Systems.ACMTrans.Interact.Intell.Syst.2021,11,1–45.[CrossRef]
16. BarredoArrieta,A.;Díaz-Rodríguez,N.;DelSer,J.;Bennetot,A.;Tabik,S.;Barbado,A.;Garcia,S.;Gil-Lopez,S.;Molina,D.;
Benjamins,R.;etal. ExplainableArtificialIntelligence(XAI):Concepts,Taxonomies,OpportunitiesandChallengestoward
ResponsibleAI.Inf.Fusion2020,58,82–115.[CrossRef]
17. Singh,A.;Sengupta,S.;Lakshminarayanan,V.ExplainableDeepLearningModelsinMedicalImageAnalysis.J.Imaging2020,
6,52.[CrossRef]
18. Miller,T.;Howe,P.;Sonenberg,L.ExplainableAI:BewareofInmatesRunningtheAsylumOr:HowILearnttoStopWorrying
andLovetheSocialandBehaviouralSciences.arXiv2017,arXiv:1712.00547.[CrossRef]
19. Lopes,P.;Silva,E.;Braga,C.;Oliveira,T.;Rosado,L.XAISystemsEvaluation: AReviewofHumanandComputer-Centred
Methods.Appl.Sci.2022,12,9423.[CrossRef]
20. Alicioglu,G.;Sun,B.ASurveyofVisualAnalyticsforExplainableArtificialIntelligenceMethods. Comput. Graph. 2022,102,
502–520.[CrossRef]
21. Zhang,Z.;Zhao,L.;Yang,T.ResearchontheApplicationofArtificialIntelligenceinImageRecognitionTechnology.J.Phys.Conf.
Ser.2021,1992,032118.[CrossRef]
22. Arun,N.;Gaw,N.;Singh,P.;Chang,K.;Aggarwal,M.;Chen,B.;Hoebel,K.;Gupta,S.;Patel,J.;Gidwani,M.;etal.Assessing
theTrustworthinessofSaliencyMapsforLocalizingAbnormalitiesinMedicalImaging. Radiol. Artif. Intell. 2021,3,e200267.
[CrossRef]
23. Zhang,J.;Chao,H.;Dasegowda,G.;Wang,G.;Kalra,M.K.;Yan,P.OverlookedTrustworthinessofSaliencyMaps.InMedicalImage
ComputingandComputerAssistedIntervention—MICCAI2022;Wang,L.,Dou,Q.,Fletcher,P.T.,Speidel,S.,Li,S.,Eds.;Lecture
NotesinComputerScience;SpringerNature:Cham,Switzerland,2022;Volume13433,pp.451–461.ISBN978-3-031-16436-1.
24. Adadi,A.;Berrada,M.PeekingInsidetheBlack-Box:ASurveyonExplainableArtificialIntelligence(XAI).IEEEAccess2018,6,
52138–52160.[CrossRef]
25. Haque,A.B.;Islam,A.K.M.N.;Mikalef,P.ExplainableArtificialIntelligence(XAI)fromaUserPerspective:ASynthesisofPrior
LiteratureandProblematizingAvenuesforFutureResearch.Technol.Forecast.Soc.Chang.2023,186,122120.[CrossRef]
26. Shin,D.TheEffectsofExplainabilityandCausabilityonPerception,Trust,andAcceptance:ImplicationsforExplainableAI.Int.
J.Hum.Comput.Stud.2021,146,102551.[CrossRef]

Informatics2023,10,32 22of24
27. Rudin,C.;Radin,J.WhyAreWeUsingBlackBoxModelsinAIWhenWeDon’tNeedTo?ALessonFromAnExplainableAI
Competition.Harv.DataSci.Rev.2019,1.[CrossRef]
28. Förster,M.; Hühn,P.; Klier,M.; Kluge,K.User-CentricExplainableAI:DesignandEvaluationofanApproachtoGenerate
CoherentCounterfactualExplanationsforStructuredData.J.Decis.Syst.2022,1–32.[CrossRef]
29. Ferreira,J.J.;Monteiro,M.Designer-UserCommunicationforXAI:AnEpistemologicalApproachtoDiscussXAIDesign.arXiv
2021,arXiv:2105.07804.[CrossRef]
30. Silva,A.;Schrum,M.;Hedlund-Botti,E.;Gopalan,N.;Gombolay,M.ExplainableArtificialIntelligence:EvaluatingtheObjective
andSubjectiveImpactsofXAIonHuman-AgentInteraction.Int.J.Hum.Comput.Interact.2022,1–15.[CrossRef]
31. Cirqueira,D.;Helfert,M.;Bezbradica,M.TowardsDesignPrinciplesforUser-CentricExplainableAIinFraudDetection. In
ArtificialIntelligenceinHCI;Degen,H.,Ntoa,S.,Eds.;LectureNotesinComputerScience;SpringerInternationalPublishing:
Cham,Switzerland,2021;Volume12797,pp.21–40.ISBN978-3-030-77771-5.
32. Chari, S.; Seneviratne, O.; Gruen, D.M.; Foreman, M.A.; Das, A.K.; McGuinness, D.L. Explanation Ontology: A Model of
ExplanationsforUser-CenteredAI.InTheSemanticWeb—ISWC2020;Pan,J.Z.,Tamma,V.,d’Amato,C.,Janowicz,K.,Fu,B.,
Polleres,A.,Seneviratne,O.,Kagal,L.,Eds.; LectureNotesinComputerScience; SpringerInternationalPublishing: Cham,
Switzerland,2020;Volume12507,pp.228–243.ISBN978-3-030-62465-1.
33. Chromik,M.;Butz,A.Human-XAIInteraction: AReviewandDesignPrinciplesforExplanationUserInterfaces. InHuman-
ComputerInteraction—INTERACT2021;Ardito,C.,Lanzilotti,R.,Malizia,A.,Petrie,H.,Piccinno,A.,Desolda,G.,Inkpen,K.,Eds.;
LectureNotesinComputerScience;SpringerInternationalPublishing:Cham,Switzerland,2021;Volume12933,pp.619–640.
ISBN978-3-030-85615-1.
34. Liao, Q.V.; Varshney, K.R. Human-Centered Explainable AI (XAI): From Algorithms to User Experiences. arXiv 2021,
arXiv:2110.10790.
35. Gan,Y.;Ji,Y.;Jiang,S.;Liu,X.;Feng,Z.;Li,Y.;Liu,Y.IntegratingAestheticandEmotionalPreferencesinSocialRobotDesign:An
AffectiveDesignApproachwithKanseiEngineeringandDeepConvolutionalGenerativeAdversarialNetwork.Int.J.Ind.Ergon.
2021,83,103128.[CrossRef]
36. Nawaratne,R.Human-CentricProductDesignwithKanseiEngineeringandArtificialIntelligence. Availableonline: https:
//towardsdatascience.com/human-centric-product-design-with-kansei-engineering-and-artificial-intelligence-f38cb3c0f26d
(accessedon21December2021).
37. Wang,D.;Yang,Q.;Abdul,A.;Lim,B.Y.DesigningTheory-DrivenUser-CentricExplainableAI.InProceedingsofthe2019CHI
ConferenceonHumanFactorsinComputingSystems,GlasgowScotland,UK,2May2019;ACM:NewYork,NY,USA,2019;
pp.1–15.
38. Lee,J.D.;See,K.A.TrustinAutomation:DesigningforAppropriateReliance.Hum.Factors2004,46,50–80.[CrossRef]
39. Hoff,K.A.;Bashir,M.TrustinAutomation:IntegratingEmpiricalEvidenceonFactorsThatInfluenceTrust.Hum.Factors2015,57,
407–434.[CrossRef][PubMed]
40. Kramer,R.M.TrustandDistrustinOrganizations:EmergingPerspectives,EnduringQuestions. Annu. Rev. Psychol. 1999,50,
569–598.[CrossRef][PubMed]
41. Lewis,J.D.;Weigert,A.TrustasaSocialReality.Soc.Forces1985,63,967.[CrossRef]
42. McAllister,D.J.Affect-andCognition-BasedTrustasFoundationsforInterpersonalCooperationinOrganizations.Acad.Manag.
J.1995,38,24–59.[CrossRef]
43. Panksepp,J.AffectiveConsciousness: CoreEmotionalFeelingsinAnimalsandHumans. Conscious. Cogn. 2005,14,30–80.
[CrossRef]
44. Schwarz,N.;Bless,H.;Bohner,G.MoodandPersuasion:AffectiveStatesInfluencetheProcessingofPersuasiveCommunications.
InAdvancesinExperimentalSocialPsychology; Elsevier: Amsterdam, TheNetherlands, 1991; Volume24, pp. 161–199. ISBN
978-0-12-015224-7.
45. Forlizzi,J.;Battarbee,K.UnderstandingExperienceinInteractiveSystems.InProceedingsofthe2004ConferenceonDesigning
InteractiveSystemsProcesses,Practices,Methods,andTechniques—DIS’04,Cambridge,MA,USA,1–4August2004;ACMPress:
NewYork,NY,USA,2004;p.261.
46. VanGorp,T.;Adams,E.DesignforEmotion;MorganKaufmann:Waltham,MA,USA,2012;ISBN978-0-12-386531-1.
47. Madsen,M.;Gregor,S.MeasuringHuman-ComputerTrust;AustralasianAssociationforInformationSystem:Wales,Australia,
2000;Volume53,pp.6–8.
48. Myers,C.D.;Tingley,D.TheInfluenceofEmotiononTrust.Polit.Anal.2016,24,492–500.[CrossRef]
49. Jin,N.;Merkebu,J.TheRoleofEmployeeAttractivenessandPositiveEmotioninUpscaleRestaurants.Anatolia2015,26,284–297.
[CrossRef]
50. Jensen,T.;Khan,M.M.H.;Albayram,Y.;Fahim,M.A.A.;Buck,R.;Coman,E.AnticipatedEmotionsinInitialTrustEvaluationsof
aDroneSystemBasedonPerformanceandProcessInformation.Int.J.Hum.Comput.Interact.2020,36,316–325.[CrossRef]
51. Albayram,Y.;Khan,M.M.H.;Jensen,T.;Buck,R.;Coman,E.TheEffectsofRiskandRoleonUsers’AnticipatedEmotionsin
Safety-CriticalSystems.InEngineeringPsychologyandCognitiveErgonomics;Harris,D.,Ed.;LectureNotesinComputerScience;
SpringerInternationalPublishing:Cham,Switzerland,2018;Volume10906,pp.369–388.ISBN978-3-319-91121-2.

Informatics2023,10,32 23of24
52. Guerdan,L.;Raymond,A.;Gunes,H.TowardAffectiveXAI:FacialAffectAnalysisforUnderstandingExplainableHuman-
AIInteractions. InProceedingsofthe2021IEEE/CVFConferenceonComputerVisionandPatternRecognitionWorkshops
(CVPRW),Nashville,TN,USA,19–25June2021;Volume10,pp.3796–3805.
53. Phillips,R.;Madhavan,P.TheRoleofAffectiveValenceandTaskUncertaintyinHuman-AutomationInteraction.Proc.Hum.
FactorsErgon.Soc.Annu.Meet.2013,57,354–358.[CrossRef]
54. Gompei,T.;Umemuro,H.FactorsandDevelopmentofCognitiveandAffectiveTrustonSocialRobots.InSocialRobotics;Ge,S.S.,
Cabibihan,J.-J.,Salichs,M.A.,Broadbent,E.,He,H.,Wagner,A.R.,Castro-González,Á.,Eds.;LectureNotesinComputerScience;
SpringerInternationalPublishing:Cham,Switzerland,2018;Volume11357,pp.45–54.ISBN978-3-030-05203-4.
55. Buck,R.;Khan,M.;Fagan,M.;Coman,E.TheUserAffectiveExperienceScale:AMeasureofEmotionsAnticipatedinResponse
toPop-UpComputerWarnings.Int.J.Hum.Comput.Interact.2018,34,25–34.[CrossRef]
56. Bernardo,E.;Tangsoc,J.ExplanatoryModellingofFactorsInfluencingAdoptionofSmartphoneShoppingApplication.IEMS
2019,18,647–657.[CrossRef]
57. Chen,Q.Q.;Park,H.J.HowAnthropomorphismAffectsTrustinIntelligentPersonalAssistants.Ind.Manag.DataSyst.2021,121,
2722–2737.[CrossRef]
58. Helander,M.G.;Khalid,H.M.AffectiveandPleasurableDesign.InHandbookofHumanFactorsandErgonomics;Salvendy,G.,Ed.;
JohnWiley&Sons,Inc.:Hoboken,NJ,USA,2006;pp.543–572.ISBN978-0-470-04820-7.
59. Khalid,H.M.EmbracingDiversityinUserNeedsforAffectiveDesign.Appl.Ergon.2006,37,409–418.[CrossRef][PubMed]
60. Lottridge,D.;Chignell,M.;Jovicic,A.AffectiveInteraction:Understanding,Evaluating,andDesigningforHumanEmotion.Rev.
Hum.FactorsErgon.2011,7,197–217.[CrossRef]
61. Gasah,M.;MatZain,N.H.;Baharum,A.AnApproachinCreatingPositiveEmotionforChildren’se-LearningBasedonUser
InterfaceDesign.IJEECS2019,13,1267.[CrossRef]
62. Isbister,K.HowGamesMoveUs:EmotionbyDesign;PlayfulThinking;MITPress:Cambridge,MA,USA,2016;ISBN978-0-262-
03426-5.
63. Gutierrez,A.M.J.;Chiu,A.S.F.;Seva,R.AProposedFrameworkontheAffectiveDesignofEco-ProductLabels.Sustainability
2020,12,3234.[CrossRef]
64. Dy,A.K.;Lazo,M.;Santos,A.G.;Seva,R.AffectiveTrashBinSignagetoPromoteWasteSegregation. InProceedingsofthe
21stCongressoftheInternationalErgonomicsAssociation(IEA2021),Online,13-18June2021;Black,N.L.,Neumann,W.P.,
Noy,I.,Eds.;LectureNotesinNetworksandSystems.SpringerInternationalPublishing:Cham,Switzerland,2022;Volume223,
pp.20–30,ISBN978-3-030-74613-1.
65. Norman,D.A.EmotionalDesign:WhyWeLove(orHate)EverydayThings;BasicBooks:NewYork,NY,USA,2004;ISBN978-0-465-
05135-9.
66. Jordan,P.W.DesigningPleasurableProducts;CRCPress:BocaRaton,FL,USA,2000;ISBN978-1-135-73411-4.
67. Khalid,H.M.;Helander,M.G.AFrameworkforAffectiveCustomerNeedsinProductDesign.Theor.IssuesErgon.Sci.2004,5,
27–42.[CrossRef]
68. Bernardo,E.;Seva,R.ExplainableArtificialIntelligence(XAI)EmotionsSet.Appl.Sci.2022,submitted.
69. Albayram,Y.;Jensen,T.;Khan,M.M.H.;Buck,R.;Coman,E.InvestigatingtheEffectofSystemReliability,Risk,andRoleon
Users’EmotionsandAttitudestowardaSafety-CriticalDroneSystem.Int.J.Hum.Comput.Interact.2019,35,761–772.[CrossRef]
70. Du,N.;Zhou,F.;Pulver,E.M.;Tilbury,D.M.;Robert,L.P.;Pradhan,A.K.;Yang,X.J.ExaminingtheEffectsofEmotionalValence
andArousalonTakeoverPerformanceinConditionallyAutomatedDriving.Transp.Res.PartCEmerg.Technol.2020,112,78–87.
[CrossRef]
71. Jian,J.-Y.;Bisantz,A.M.;Drury,C.G.FoundationsforanEmpiricallyDeterminedScaleofTrustinAutomatedSystems. Int.
J.Cogn.Ergon.2000,4,53–71.[CrossRef]
72. Kline,R.B.PrinciplesandPracticeofStructuralEquationModeling,4thed.;MethodologyintheSocialSciences;TheGuilfordPress:
NewYork,NY,USA,2016;ISBN978-1-4625-2335-1.
73. Westland,C.LowerBoundsonSampleSizeinStructuralEquationModeling. Electron. Commer. Res. Appl. 2010,9,476–487.
[CrossRef]
74. Cohen,J.StatisticalPowerAnalysisfortheBehavioralSciences;Routledge:London,UK,1988;ISBN978-0-203-77158-7.
75. Angold,A.;Costello,E.J.ShortMoodandFeelingsQuestionnaire;APAPsycNet:Washington,DC,USA,1987.[CrossRef]
76. Frazier,M.L.;Johnson,P.D.;Fainshmidt,S.DevelopmentandValidationofaPropensitytoTrustScale.J.Trust.Res.2013,3,76–97.
[CrossRef]
77. Lowry,P.B.;Twyman,N.W.;Pickard,M.;Jenkins,J.L.;Bui,Q.“Neo”ProposingtheAffect-TrustInfusionModel(ATIM)toExplain
andPredicttheInfluenceofHighandLowAffectInfusiononWebVendorTrust.Inf.Manag.2014,51,579–594.[CrossRef]
78. Hsu, S.-H.; Chen, W.; Hsieh, M. Robustness Testing of PLS, LISREL, EQS and ANN-Based SEM for Measuring Customer
Satisfaction.TotalQual.Manag.Bus.Excell.2006,17,355–372.[CrossRef]
79. Henseler,J.;Ringle,C.M.;Sinkovics,R.R.TheUseofPartialLeastSquaresPathModelinginInternationalMarketing.InAdvances
inInternationalMarketing;Sinkovics,R.R.,Ghauri,P.N.,Eds.;EmeraldGroupPublishingLimited:Bingley,UK,2009;Volume20,
pp.277–319.ISBN978-1-84855-468-9.

Informatics2023,10,32 24of24
80. Chin,W.W.ThePartialLeastSquaresApproachforStructuralEquationModeling. InModernMethodsforBusinessResearch;
MethodologyforBusinessandManagement;LawrenceErlbaumAssociatesPublishers:Mahwah,NJ,USA,1998;pp.295–336.
ISBN0-8058-2677-7.
81. Yang,X.J.;Unhelkar,V.V.;Li,K.;Shah,J.A.EvaluatingEffectsofUserExperienceandSystemTransparencyonTrustinAutomation.
InProceedingsofthe2017ACM/IEEEInternationalConferenceonHuman-RobotInteraction,Vienna,Austria,6March2017;
ACM:NewYork,NY,USA,2017;pp.408–416.
82. Vogt,W.P.;Johnson,R.B.TheSAGEDictionaryofStatistics&Methodology:ANontechnicalGuidefortheSocialSciences,5thed.;SAGE:
LosAngeles,CA,USA,2016;ISBN978-1-4833-8176-3.
83. Hair,J.F.(Ed.)MultivariateDataAnalysis;PrenticeHall:UpperSaddleRiver,NJ,USA,1998;ISBN978-0-13-894858-0.
84. Taber,K.S.TheUseofCronbach’sAlphaWhenDevelopingandReportingResearchInstrumentsinScienceEducation.Res.Sci.
Educ.2018,48,1273–1296.[CrossRef]
85. Hu, L.; Bentler, P.M. Cutoff Criteria for Fit Indexes in Covariance Structure Analysis: Conventional Criteria versus New
Alternatives.Struct.Equ.Model.AMultidiscip.J.1999,6,1–55.[CrossRef]
86. Schreiber,J.B.;Nora,A.;Stage,F.K.;Barlow,E.A.;King,J.ReportingStructuralEquationModelingandConfirmatoryFactor
AnalysisResults:AReview.J.Educ.Res.2006,99,323–338.[CrossRef]
87. Cangur,S.;Ercan,I.ComparisonofModelFitIndicesUsedinStructuralEquationModelingUnderMultivariateNormality.
J.Mod.Appl.Stat.Meth.2015,14,152–167.[CrossRef]
88. Baron,R.M.;Kenny,D.A.TheModerator–MediatorVariableDistinctioninSocialPsychologicalResearch:Conceptual,Strategic,
andStatisticalConsiderations.J.Personal.Soc.Psychol.1986,51,1173–1182.[CrossRef]
89. Shi,D.;Lee,T.;Maydeu-Olivares,A.UnderstandingtheModelSizeEffectonSEMFitIndices. Educ. Psychol. Meas. 2019,79,
310–334.[CrossRef]
90. Petty,R.E.;Cacioppo,J.T.TheElaborationLikelihoodModelofPersuasion.InAdvancesinExperimentalSocialPsychology;Elsevier:
Amsterdam,TheNetherlands,1986;Volume19,pp.123–205.ISBN978-0-12-015219-3.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.