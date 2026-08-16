---
conversion_metadata:
  converted_at: "2026-07-21T08:04:17Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Pakarinen.pdf"
  source_pdf_sha256: "0a2ef7b20050546bb6724200d0647719ac8dfcceec21b050b00152fb8b8fb003"
  page_count: 57
  markdown_char_count: 199847
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Optimizing Banking Application 
Interfaces

A User-Centric Perspective on Consent Management in 
Digital Banking Environments

Olga Pakarinen

Master’s thesis 
December 2025 
Master’s Degree Programme in Information Technology, Full Stack 
Software Development

---

<!-- PAGE 2 -->

Description

Olga Pakarinen

Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management

Jyväskylä University of Applied Sciences, December 2025, 55 pages.

Degree Programme in Information Technology, Full Stack Software Development. Master’s Thesis

Permission for open access publication: Yes

Language of publication: English

Abstract

This study examined the implementation of a consent management tool for digital banking users that is 
more transparent, accessible, and controllable than existing solutions. This goal was achieved by designing 
and testing a consent management tool and by examining the effects of different consent flows on users’ 
understanding and trust in decision-making. The study used a mixed-methods approach, including an initial 
quick exploratory survey, two rounds of usability testing, and semi-structured interviews.

The prototype is structured into two levels. A category-based overview will allow users to view all the 
categories of their data usage at a higher level. Users can also view and adjust individual permissions via a 
detailed consent view.

During the usability studies, participants interacted with the prototype, provided feedback on the wording 
and formatting of the text, and assessed their confidence in making consent-related decisions. The research 
results showed that lengthy, complex consent language impairs users' understanding. Conversely, concise, 
clear steps and explicit labels, along with the visibility of the consent state, improve users' perception of 
control and confidence when consenting.

Research findings can inform practical recommendations for designing consent interfaces. 
Recommendations include gradual disclosure of content, consistent structures, and the implications of 
reversible consent decisions. Additionally, the study guides further development, including an AI-supported 
summarization tool. The summary feature will explain why users need consent for specific options and how 
their choices affect the security of their data. Ultimately, the main goal of this project is to establish and 
promote best practices for creating a Consent Management Solution that supports users' needs above 
those of regulatory compliance.

Keywords/tags (subjects)

Consent management, Digital Banking, User-Centered Design, Data Privacy, GDPR, Usability Testing

Miscellaneous (Confidential information)

None

---

<!-- PAGE 3 -->

1

Contents

1

2

Introduction ................................................................................................................. 3

Background and Context of the Study ........................................................................... 4

2.1	 Research Motivation ........................................................................................................ 5

2.2	 Research Objectives ......................................................................................................... 6

2.3	 Research problem and research questions ...................................................................... 6

2.4	 Scope and Limitations ...................................................................................................... 7

2.5	 Thesis Structure ............................................................................................................... 8

3

Ethical Considerations .................................................................................................. 9

3.1	 Research Integrity and Authorship .................................................................................. 9

3.2	 Transparency and Responsible Use of AI ....................................................................... 10

3.3	 Data Protection and Privacy .......................................................................................... 11

3.4	 Usability Testing and User Feedback ............................................................................. 11

3.5	 Balancing Legal Compliance and User Agency ............................................................... 12

4	 Methodology ............................................................................................................... 12

4.1	 Research Design ............................................................................................................. 12

4.2	 Data Collection Methods ............................................................................................... 13

4.3	 Data Analysis Approach ................................................................................................. 13

4.4	 Reliability of the Study ................................................................................................... 14

4.5	 Reflection on the Research Process ............................................................................... 14

5	 User Engagement and Consent Management ............................................................... 14

5.1	 Understanding User Behavior in Banking Applications ................................................. 14

5.2

Importance of User Engagement in Consent Management .......................................... 15

5.3	 Challenges in Consent Interface Design ......................................................................... 16

6	 User-Centric Design Principles ..................................................................................... 17

6.1	 Principles of User-Centric Design ................................................................................... 18

6.2	 Usability and Accessibility Considerations ..................................................................... 19

6.3	 Usability and Accessibility Considerations ..................................................................... 20

7

Case Studies and Comparative Analysis ....................................................................... 21

7.1	 Analysis of Existing Banking Application Interfaces ....................................................... 22

7.2	 Case Studies of Successful Consent Management Implementations ............................ 24

7.3	 Comparative Analysis of Different Consent Management Approaches ........................ 27

8

Implementation of Consent Management Tool ............................................................ 31

8.1	 User Experience Design of the Consent Management Tool .......................................... 31

---

<!-- PAGE 4 -->

2

8.2	 Designing an AI-Driven Consent Explanation Tool ......................................................... 33

8.3	 Full-Stack Development Approach ................................................................................ 34

8.4	 Back-End Functionality for Consent Management ........................................................ 35

8.5

Integration with Existing Banking Systems .................................................................... 36

9	 Usability Testing and User Feedback ............................................................................ 37

9.1	 Usability Testing Plan ..................................................................................................... 37

9.2	 Category-Based Consent Overview (First Layer) ............................................................ 38

9.3	 Detailed Consent View (Second Layer) .......................................................................... 38

9.4	 “Smart Summary” AI feature ......................................................................................... 39

10	 Results ......................................................................................................................... 39

10.1	 User Feedback Analysis (First round of User Studies) ................................................... 39

10.2	 Iterative Improvements based on User Input ................................................................ 40

10.3	 Observed Improvements and Remaining Gaps (Second round of User Studies) ........... 40

10.4	 Final Improvements Suggestion ..................................................................................... 40

11	 Discussion and Conclusion ........................................................................................... 41

11.1	 Linking Results to Research Questions .......................................................................... 41

11.2	 Interpretation of Findings .............................................................................................. 42

11.3	 Sustainability Considerations ......................................................................................... 42

11.4	 Development Proposals ................................................................................................. 43

11.5	 Conclusion ..................................................................................................................... 43

References .......................................................................................................................... 45

Appendices ......................................................................................................................... 47

Appendix 1. Category-Based Consent Overview (Figma) ....................................................... 47

Appendix 2. Granular Consent Settings Within a Category .................................................... 48

Appendix 3. Consent Summary and Confirmation View ......................................................... 49

Appendix 4. User Questionnaire (Exploratory, n=6) ............................................................... 50

Appendix 5. Semi-Structured Interview Topics ...................................................................... 55

---

<!-- PAGE 5 -->

3

1

Introduction

Digital banking has grown over the last decade. Mobile banking applications and online systems

now handle tasks that previously required a visit to a bank branch. As a result, customers expect

these services to be fast, simple, and continuously available. Since banking services have moved

online, the volume of personal data processed has increased, along with concerns for personal

information privacy.

Consent management defines how users accept or decline the processing of personal information

and how that consent is subsequently managed. Often, this relates to decisions about which

personal information can be collected, how it will be processed, and when it can be shared.

Regulations such as the GDPR and the CCPA set minimum requirements for the collection and

management of consent. According to Yusuff (2023), consent management in information systems

adds a level of trust and accountability in digital systems. In banking environments, consent

management affects how individuals' private data is handled. It shows that consent is more of a

practical mechanism than a legal concept.

In banking applications, consent is often presented in ways that are difficult for users to

understand. To present consent information and support users’ decision-making, designing an

efficient interface structure was selected as a key objective of this project. User behavior in

consent flows, information needs, and common points of misunderstanding are analyzed using

qualitative and quantitative methods. Based on these findings, a user-centered prototype is

developed. The design integrates consent into everyday interactions rather than presenting it as

an isolated legal item.

The research explores how interface design can align user expectations with legal requirements.

Banking systems must meet legal requirements, but they also need to function in ways that feel

reasonable to their customers. Still, clear communication and consistent data handling remain the

foundation for trust. This project blends regulatory analysis, user-centered design principles, and

observational usability testing to identify improvements in consent management for digital

banking interfaces.

---

<!-- PAGE 6 -->

4

2  Background and Context of the Study

The future of online banking depends on how user consent is defined and managed within data

privacy policies. Banks store large volumes of sensitive information about their clients. They need

to handle this information with caution while complying with confidentiality requirements. Several

laws regulate the processing of personal data, which increases the importance of consent.

Regulations such as the GDPR and the CCPA require organizations to manage personal data

transparently before processing it (GDPR, 2016).

Collecting and managing consents creates the foundation of data privacy governance in banking.

Legal regulations raise expectations for information security, particularly when personal data is

collected via explicit customer consent. As stated by Husain, financial institutions are obligated to

be transparent and accountable in handling all personal information in their operations (GDPR,

2016).

The General Data Protection Regulation and California Consumer Privacy Act both require express

consent before processing personal information (General Data Protection Regulation, 2016;

California Consumer Privacy Act, Cal. Civ. Code § 1798.100 et seq.). According to the European

Data Protection Board, users should be able to grant and revoke their consents (European Data

Protection Board, 2020). European data protection law states that “consent of the data subject”

refers to a voluntary, informed, and obvious indication of a person’s wishes (GDPR, Art. 4(11)).

This definition guides how banking interfaces must request and record user decisions.

Consent is closely related to risk management in banking systems. Given the frequent occurrence

of data breaches and cyberattacks, banks need to be especially careful with sensitive information.

Banks can develop secure systems and minimize the risk of unauthorized access by understanding

how users interact with consent systems. Additionally, banks aim to increase customer satisfaction

through personalized services. These services depend on users’ willingness to grant consent.

According to Gartner (2024), effective consent management supports risk control and responsible

data use.

Banks use data to create individual services, but only when users feel comfortable granting

permission. As indicated by the World Economic Forum, consent will always be heavily dependent

---

<!-- PAGE 7 -->

on customer expectations regarding personalization (WEF, 2018). When used wisely, consent

supports customer-centered services. When handled poorly, it compromises customer trust and

loyalty.

5

A bank’s reputation is shaped by how responsibly it handles consent and personal data. Neglecting

to obtain consent or failing to protect data may compromise customers’ confidence. McKinsey &

Company believes that strong data protection practices and consent handling are critical in

achieving sustained success in organizations (McKinsey, 2020). Digital banking systems must

balance legal requirements, user expectations, and technical limitations.

The materials used in this study reflect this balance. GDPR guidelines form the basis for the

consent analysis. Industry literature gives an insight into the banking industry, but sometimes

these texts are published with a commercial focus and must be interpreted with caution. Research

on consent management in digital banking remains limited, but the available sources support the

analysis conducted in this study.

2.1  Research Motivation

The new era of online environment has changed the entire meaning and perception of data

privacy. GDPR and the CCPA remind banks that consent should be obtained before processing

personal data. These requirements have pushed banks to revise their systems and ensure that

consent is properly collected and recorded. Banks can improve their management of regulatory

requirements and reduce legal and financial risks by examining how consent operates in real-

world banking interactions (Financial Conduct Authority, 2018).

Working with financial information adds an extra level of complexity due to its sensitive nature.

According to the Ponemon Institute (2012), banks must prioritize effective risk management

policies. This includes precautions against data leaks and the maintenance of incident response

plans in the event of security breaches. Addressing these risks requires an understanding of how

customers approach consent. Improving consent practices helps protect customers and supports

trust in financial institutions.

---

<!-- PAGE 8 -->

Cyber incidents remain a long-term issue. The increase in data theft and fraud highlights the need

for clear permission settings and reliable safety measures (Ponemon Institute, 2012). When

consent tools are predictable and easy to understand, users can manage their preferences with

confidence. Predictability promotes loyal relationships, and banks can meet expectations

regarding privacy and security (Financial Conduct Authority, 2018).

6

2.2  Research Objectives

Customers frequently manage personal information in digital banking applications. Therefore,

consent management has become a standard part of the user experience. Although consent

management flows are widely used across banking systems, their design and structure vary quite

extensively. The research will explore how these consent systems function and how customers

respond when they encounter them.

Legal requirements, particularly the General Data Protection Regulation (GDPR), affect the design

and implementation of consent mechanisms in banking applications. The study aims to improve

banking interfaces to make consent easier to understand and manage. User testing sessions and

participant feedback from individuals who interacted with the prototype will assist in this goal.

One additional goal is to investigate consent with double considerations: first, how well the user

understands it, and second, how well consent is documented and applied in the system. The

integration of these perspectives will help in understanding both where the design is already

effective and where it can be improved (Følstad & Hornbæk, 2017).

2.3  Research problem and research questions

User consent is a key area of study in data protection and customer experience in digital banking.

With growing online banking experience, there is a clear need for a consent management system

that is simple and easy to understand. While consent functionality is present in most online

banking systems, a significant gap exists between standard technical implementation and legal

requirements for consent, especially under the GDPR and the CCPA.

---

<!-- PAGE 9 -->

7

The most common problem with digital banks is inadequate regulation and poorly optimized

consent management systems. A consent management system with an unclear or intrusive

consent flow can easily affect customer satisfaction and compromise their trust. A modern digital

bank with limited knowledge of how to properly implement consent management systems must

therefore learn from existing practices, customer expectations, and real constraints of digital

banking.

This research addresses several questions. First, it reviews existing consent solutions in online

banking to determine how well they respond to industry standards and regulatory requirements.

Then, it investigates how users behave during consent management and how they understand

consent-related information. The study looks at users’ needs, challenges, and decision-making

through usability testing, questionnaires, and interviews. A further question is whether these

practices meet the expectations set by regulatory organizations such as the GDPR and the CCPA.

Additionally, this project aims to make recommendations on consent management in banking

apps more actionable. The design process will be supported by end-user testing and validation.

These inputs helped refine the prototype and assess whether the proposed model improved

understanding, supported user choice, and remained compliant with legal standards.

2.4  Scope and Limitations

Consent management in digital banking is the primary focus of this study. Likewise, regulatory

requirements, user experience, consent management design and architecture are three essential

components addressed through the user-centric perspective. The research investigates how users

understand consent, how they manage it, and how design choices influence these behaviors.

The research does not cover financial risks, back-end banking operations, or other organizational

policies beyond consent management. A combination of usability testing, interviews, and a

research questionnaire is used to identify existing commonalities in the requirements and

expectations of banking customers. The objective of this research is to find out how individuals

perceive consent management and banks’ expectations, and how effective design can support

these decisions in digital banking.

---

<!-- PAGE 10 -->

8

Some flaws have been noted. A limited research time resulted in a smaller user group, therefore

limiting the opportunity to generalize the findings. Conducting this research in a controlled

environment and not in a real-life banking system is another shortcoming. Several technical issues

have influenced the prototype design, which can be addressed as a simplified model of a banking

system. Despite these limitations, the findings provide a practical foundation for improving

consent design and guiding future research.

2.5  Thesis Structure

The findings of this research are presented in an eleven-chapter structure from background and

motivation through design, evaluation, and conclusions.

1.  Chapter 1 introduces the research topic and explains its relevance to consent management

in modern digital banking. The background is outlined, and consent is considered an

essential part of user interactions in a banking environment.

2.  Chapter 2 presents the research context. It reviews the regulatory framework, key

concepts, and definitions of data protection and consent. The chapter also reviews the

relevant sources on digital banking, consent management, and usability. In addition, it

presents the research motivation, objectives, research questions, scope, and limitations,

explaining what the study focuses on and what it does not.

3.  Chapter 3 presents ethical considerations related to the research. It explains how research

integrity, data protection, and responsible use of AI were addressed throughout the study.

The chapter also analyzes the balance between legal compliance and user agency, and how

ethical responsibilities were managed during the research and design phases.

4.  Chapter 4 describes the research methodology used in the study. It explains how the

research was planned, how data were collected and analyzed, and why these methods

were selected. The chapter also supports the credibility of the findings by addressing issues

of reliability.

5.  Chapter 5 focuses on user engagement in digital banking applications, with precise

attention to consent-related interactions. It examines how users encounter consent

management in everyday contexts, how they respond to it, and the challenges they face in

these interactions. The chapter compares observed user behavior to issues in consent

interface design.

---

<!-- PAGE 11 -->

9

6.  Chapter 6 introduces user-centered design principles and discusses usability and

accessibility in consent management. It explains how these principles support clear

communication, reduce users’ cognitive load, and help them make informed decisions in

banking digital environments.

7.  Chapter 7 presents case studies and a comparative analysis of existing consent-

management approaches in selected banking applications. The chapter reveals similarities

and differences between strategies and identifies common design patterns. In the end, it

discusses the strengths and shortcomings of the reviewed strategies.

8.  Chapter 8 describes the design and implementation of the consent management prototype

developed within this project. It explains key design decisions, user-experience principles,

and technical implementation choices. This chapter concludes by demonstrating how

regulatory requirements and user needs were translated into a working solution.

9.  Chapter 9 describes the usability testing process and the gathering of user feedback. It

outlines how the testing sessions were organized, how interface components were

evaluated, and how participants interacted with the prototype.

10. Chapter 10 presents the results of the usability studies. It summarizes the main results

from testing, including observed improvements in interaction with the revised prototype

and remaining usability issues.

11. Finally, Chapter 11 compares the results with the research questions and research

objectives. It reflects on the study’s contributions, summarizes development proposals,

and presents the conclusions.

3  Ethical Considerations

The project followed the ethical guidelines of JAMK University of Applied Sciences, the Arene

guidelines on the use of artificial intelligence (AI) in higher education, and the principles of

research ethics. User-centered design, regulatory analysis, and technical development were

addressed with ethical considerations integrated throughout the research process.

3.1  Research Integrity and Authorship

The author documented all research methodology, design, and analysis used in this study.

References to prior knowledge or authoritative materials used in this study follow JAMK

---

<!-- PAGE 12 -->

documentation standards. The study identifies both existing and new information. Each statement

in this study relies on primary legal documentation (e.g., the GDPR, the CCPA) and relevant

supporting materials. The ideas and conclusions were analyzed against expert perspectives and

appropriate academic materials.

10

The author originally developed all the research questions, design choices, technical decisions, and

interpretations of prior knowledge. The key concepts, analytical findings, and overall thesis

structure presented in the study were developed through the author's independent efforts and

knowledge. The references to previous studies and original contributions were clearly identified in

accordance with JAMK documentation guidelines. Legal perspectives were supported by the

source (the GDPR), academic, and professional literature. The author accepts complete

responsibility for the content, analysis, and conclusions provided in this research.

3.2  Transparency and Responsible Use of AI

As noted earlier, the research was implemented in several phases, with the author maintaining

control over content quality and executive decisions throughout the process. All written material

was produced as part of an independent thesis project. It demonstrates individual reasoning,

analysis, and interpretation of the subject.

Initially, AI-assisted tools (Copilot and ChatGPT) were used to support topic planning and refine

the research scope. These tools helped narrow down the study area, plan potential research

stages, and learn and adapt to academic tone.

AI-assisted language tools were used as a learning aid to become familiar with appropriate

academic vocabulary, style, structure, and argumentation. Example expressions and structural

suggestions were reviewed to identify common patterns in academic texts. AI editing assistants

(Grammarly and QuillBot) supported writing by addressing grammar, punctuation, sentence

structure, and vocabulary to improve consistency in academic writing. These tools neither shaped

nor influenced the study’s key findings.

After completing a few first drafts, AI was used in the revision process. Their purpose was to

support writing coherence and consistency of ideas. The author reviewed each paragraph

---

<!-- PAGE 13 -->

individually and used AI tools to suggest alternative phrasing for sentences that appeared

redundant, repetitive, or grammatically incorrect. This process was repeated in the following

revisions. The final text reflects the author’s ideas and conclusions at every stage, including what

content to keep, how to present the regulatory analysis, the author's own findings, and how to

structure the conclusions.

11

Every AI-suggested rewrite was critically reviewed and refined. Suggested changes that might have

affected meaning, introduced ambiguity, or conflicted with technical or legal accuracy were

excluded. Additionally, the author critically assessed and refined the suggestions to preserve their

personal understanding and intentions. All research questions, design decisions, implementation

logic, analyses, results, and conclusions presented in this thesis were developed by the author.

AI-assisted tools were used as supportive aids during the implementation phase to explain

common programming patterns, support debugging, and suggest refactoring. The general project

architecture, stack choices, data models, and application logic were designed and implemented by

the author. AI tools did not influence the author’s independent decisions on the project's design

and architecture.

3.3  Data Protection and Privacy

Nevertheless, this research did not involve actual private banking or personal information. The

information obtained in this research is based solely on usability studies and on prototype

interactive sessions. The responses obtained were anonymous and recorded without including

personal or financial information. Although this study focuses on people's reactions to consent

screens, it does not involve behavioral analysis. The information is recorded in notes, where it is

safely stored and used only for research.

3.4  Usability Testing and User Feedback

User feedback and usability testing were critical to the interface design. The participants were

informed of the research goals, their voluntary participation, and their right to withdraw at any

stage. Feedback sessions focused on interaction with prototypes rather than on personal issues or

financial information, therefore mitigating ethical concerns. Anonymity ensured that people were

---

<!-- PAGE 14 -->

not identifiable in the results. Feedback supported the design improvements but did not specify

them, as individual experiences vary. The research examined the ethics of maintaining compliance

with laws and users’ sense of control. Ethical design demonstrates that being compliant and using

a system can go hand in hand. Consent is not viewed as a regulatory or technological tool, but

rather as a way of making decisions with freedom.

12

3.5  Balancing Legal Compliance and User Agency

Legal obligations and control in consent management were the primary interest of the study. The

GDPR and similar laws have very specific guidelines when it comes to consent. However, following

these guidelines is not practical from a usability perspective. A design can be highly compliant with

these guidelines but may end up confusing users and leaving them with doubts about their own

decisions. As a result, consent management is a process that, over time, improves users’

understanding of data-sharing mechanisms, the importance of flexibility, and the need for user

control.

4  Methodology

4.1  Research Design

Mixed-methods analysis will be used to examine how users interpret and manage consent in

online banking. A connection to existing literature will be established through a literature review.

Three research methods will be utilized in this study: a short survey, a series of interviews, and

usability studies.

The survey provides critical quantitative data on users' opinions and preferences regarding

consent. The interviews provide information about confusing or complicated issues for users. The

usability tests provide real-world information about interaction barriers when completing a task.

Taken together, these provide a more complete perspective on reasoning, behavior, and

expectations among users, consistent with this study’s focus on improving experience, control,

and compliance.

---

<!-- PAGE 15 -->

During the planning phase, other methods were considered but not applied in this research, such

as a focus group study, extended analysis, or A/B testing. However, the methods utilized in this

research include a small survey, in-depth interviews, and usability studies, with two rounds of

prototype testing. Other methods will be considered in future research studies.

13

4.2  Data Collection Methods

Surveys were used to collect quantitative data on opinions about consent management in general.

An exploratory survey includes a Likert scale question, multiple-choice questions, and short

comments to make some early conclusions before performing usability tests. The small number of

responses obtained reveals that these results are suggestive and not representative. The survey

results can be found in appendices 4-5.

The main technique used in this usability study is usability testing, which tested how well

participants were able to navigate through the consent management interface. The parameters

measured in this usability study include task time, hesitations, error rate, and the proportion of

explanatory queries.

Following usability testing, semi-structured interviews were conducted to collect opinions on the

rationale for observed behavior, confusing interface language encountered during the studies, and

personal understandings of specific consent items. Open-ended questions helped to gather

responses that would not otherwise be possible from task performance data. Through a

combination of surveys, usability studies, and interviews, a better understanding of user needs

and pain points necessary for the redesign was achieved.

4.3  Data Analysis Approach

Analysis began with the organization of task-completion observations and questionnaire

responses. Descriptive information on completion time and reported difficulties was used to

summarize the survey results. Patterns in hesitation, missed steps, and misinterpretations were

compared among participants. Qualitative data from interviews and think-aloud sessions were

analyzed by theme. User comments were split into three areas: confusion about terminology,

---

<!-- PAGE 16 -->

difficulty locating information, and uncertainty about consequences. These themes were

compared with task observations to confirm or deny biased impressions of the author.

14

Such an analysis technique allowed both individual views and overall trends to be considered,

relating usage to explanations and identifying where a design hindered understanding. The results

were used to inform support improvements, which will be explained in detail in the following

chapters.

4.4  Reliability of the Study

Several aspects affect reliability. The sample size was small and therefore not sufficient to

represent all banking customers. The tests were conducted in a controlled environment rather

than in a real banking context. The prototype simplified several back-end support tasks, which can

influence how people understand the choices. Patterns were recognizable despite some of these

flaws. A combination of methods helped achieve reliable results, as different perspectives were

used to present distinct findings.

4.5  Reflection on the Research Process

The research was conducted in iterative cycles. Early tests revealed that the original structure was

overly complex, so the prototype was simplified and the focus shifted to task simplicity. Time and

scope limits required prioritizing essential features, such as presenting detailed consent items

under clear categories. These adjustments kept the study feasible while still answering the

research questions. Although the process was not linear, the iterative strategy improved the final

design and helped achieve more grounded conclusions.

5  User Engagement and Consent Management

5.1  Understanding User Behavior in Banking Applications

To design effective consent management solutions, it is important to understand how users

interact with banking apps. Users prioritize simple navigation when performing everyday tasks

such as checking balances, making payments, or viewing daily transactions. With improved

---

<!-- PAGE 17 -->

navigation, users can complete their tasks with less effort and increase their satisfaction with the

service.

15

Security is the initial focus of expectations in digital banking. It is well established that customers

want to be assured that their financial and personal information will be protected. While

technologies such as encryption and two-factor authentication are important, they must be

accompanied by clear communication. Users want to know how their information will be

collected, processed, and shared, and all this information must be presented in a simple way.

When this occurs, they will be convinced that a reputable financial organization is handling their

information responsibly and securely.

Consent management relies on this integrity. Requesting consent for an application must be

conducted in a way that protects user autonomy. A user must always have access to view, analyze,

and modify consent decisions. Therefore, with such an option being available, a user is in control

of their personal information.

Interfaces that respect user preferences are more likely to support long-term customer

relationships. When users can manage their sensitive information without confusion, they are

more likely to remain loyal to their chosen service. Updating interfaces based on observed

behavior and user feedback reinforces this pattern of trust. A clear and accessible consent

management experience provides users with confidence and complies with secure data

management practices.

5.2  Importance of User Engagement in Consent Management

User engagement is necessary to manage consent effectively in banking apps. Legal requirements

may not enable users to understand what they consent to or to be assured of the validity of their

consent decisions. User engagement supports autonomy by helping users understand consent

requests and adjust them according to their preferences.

When this sense of inclusion is established among users, they will feel valued and empowered.

They will unlikely perceive consent as an obligation but rather as a part of taking control of their

online presence. Users will have an opportunity to reflect before acting, as they will not consent to

---

<!-- PAGE 18 -->

a request until they have understood its meaning. In this way, consent is a dynamic process that

gradually evolves into an ongoing relationship of assurance and respect, rather than just a one-

time event.

16

Therefore, the design of consent mechanisms must go beyond simple checkbox interactions.

Consent solutions must be designed to ensure that end users understand them. Inclusion in this

context refers to ensuring that the end user feels their voice and opinion are heard. An accessible

experience will enable users to trust and commit to a loyal relationship with an organization that

adheres to these principles.

In a digital environment where privacy issues are becoming increasingly important, the

consideration of the user in consent decisions is both justified and necessary. Consent should not

be an administrative task but a dynamic and understandable process in the user experience. A

pragmatic, user-centric approach will help identify the balance between the legislation and the

value provided to users in financial institutions.

5.3  Challenges in Consent Interface Design

The design of consent interfaces in digital banking is a challenge. Designers face a challenge in

providing information in a manner that is not overwhelming to the end-user, especially when

dealing with consent content that is complex and not common knowledge. Long blocks of text lead

to confusion or disengagement, and many users skim these screens without understanding what

they are agreeing to (Kyi et al., 2024; Nouwens et al., 2020).  For this reason, consent fatigue sets

in, making consent less relevant in this context. Research analysis demonstrates that consent

interfaces influence one’s individual decisions, using interface designs to enforce decisions rather

than guiding them with the information they need to understand (EDPB, 2022). Given that digital

banking systems directly affect financial behavior in daily tasks, clear and consistent consent

management flows, and information provision need to be heavily prioritized.

Consent is not a one-shot experience. A person is likely to change their mind about using their

data depending on their life's circumstances. However, most banking systems have consent

models that do not permit straightforward preference settings. Consent interface systems that do

---

<!-- PAGE 19 -->

not allow revocation or modification of consent preferences can limit one’s options and reduce

their understanding of data sharing.

17

Additionally, interfaces must accommodate different levels of technical capacities among users.

Complex terminology or unclear layouts can hinder users who are unfamiliar with technical

language or navigation patterns. Accessibility, therefore, implies inclusive designs with specific

language, usability, and graphic guidelines. Other systems that assume advanced digital literacy

may create barriers for users who are already uncertain about managing their finances online.

Financial institutions face internal issues between compliance, operational tasks, and business

goals. Such dilemmas may lead to design solutions that coerce customers, for instance, by using

preselected options or suggestive language. Even subtle cues can affect user behavior in ways that

compromise their voluntary consent. Such practices can erode trust and raise doubts about the

procedure's validity. A good consent interface will balance the need to comply with regulatory

standards and a focus on users’ needs. A lack of both can make consent appear to be a matter of

procedure rather than an informed choice.

Refined, user-centered design will support users’ decision-making and encourage long-term trust.

However, continuous evaluation is necessary, as user expectations and regulations change all the

time. Although this work is ongoing, it offers clear benefits for both users and banks by providing a

simplified and purposeful consent-management experience.

6  User-Centric Design Principles

With the increasing pace of change in digital financial systems, creating a trustworthy experience

is non-negotiable. With respect to banking apps, which people use to store personal information

and take actions with consequences for their lives, a user-centered approach is critical. User

confusion or frustration with a system will compromise its reliability. User-centered design can

make a system function better, safer, and more appealing to work with.

In this chapter, the principles of User-centered design will be discussed in relation to consent in

the design of mobile banking applications. This chapter also describes how these principles form

---

<!-- PAGE 20 -->

the design process, elevate empathy, accessibility, and adaptability. User evaluation is essential to

every development cycle, and these principles guide practical decisions throughout the process.

When applied consistently, they support legal compliance, user happiness, and customer loyalty.

They also encourage designers to view consent as a shared responsibility that strengthens users’

autonomy and trust within the banking environment.

18

6.1  Principles of User-Centric Design

User-centered design is a philosophy with a central guiding principle: technology must serve

people. In the financial context, for instance, customers possess sensitive and complex financial

data, which leads them to expect a higher level of service from online banking systems. The impact

of user-centered design is not merely formal; it stands for supportive and fair interactions. This is

an important consideration in consent flows, where a sense of understanding and control is

important. By mirroring reality in their design, such interfaces become more intuitive and less

intimidating while encouraging awareness among all user groups.

Empathy is a founding principle of user-centered design. As a user, you want your goals, concerns,

and pain points understood. Empathy enables designers to anticipate difficult situations, such as

navigating unfamiliar consent screens, and to work toward reducing pressure in these situations.

Empathy does not remove complexity; instead, it creates a context in which a user feels

understood, heard, and comforted.

Accessibility is another critical consideration. Bank customers have diverse backgrounds. They

have different levels of literacy, tech capabilities, and skills. They may be uncertain when

presented with new vocabulary or when required to provide long-term consent. Poorly structured

interfaces aggravate exclusion, further marginalizing already vulnerable people. Those who focus

on accessibility demonstrate a commitment to fair treatment of users, not just to a standard or

regulation.

A clearer consent process relies upon empathy and simplicity. A clearer consent process enables

individuals to understand exactly what they are consenting to and how their information will be

used. Many systems hide this information through vague language or dense text that few people

---

<!-- PAGE 21 -->

read. Clear, direct explanations build confidence and reduce confusion. Users tend to respond

positively when they perceive the system as honest.

19

Flexibility is equally essential. User preferences continuously fluctuate, and consent systems

should allow them to grant, accept, or revoke permissions. Some banking applications have not

moved beyond enabling consent decisions to be made only once. They are difficult to return to;

hence, they appear rigid and non-transparent. Efficient systems enable users to review and update

preferences when circumstances change.

With these principles of empathy, accessibility, integrity, and flexibility, a more sophisticated

approach to consent can be achieved in digital banking. With this knowledge in mind, consent

management in digital financial systems will transform a simple procedural requirement into a

representation of customers’ legal rights and expectations. Organizations that respect these

values help users feel recognized, informed, and confident in their actions, therefore contributing

to the ethical and social dimensions of online banking.

6.2  Usability and Accessibility Considerations

Design thinking provides a foundation for creating ethical and user-centric consent experiences.

The conception encourages designers to put themselves in the end user's shoes and to focus on

more than just technical requirements and/or legally worded consent. Design thinking is an

iterative process that involves continuous communication with end-users. This mindset can

benefit the overall digital consent management process and help maintain the balance among fair

treatment, ethical considerations, and legal requirements.

Empathy is the core principle of design thinking. It is not an abstract ideal but a practical approach

to understanding user needs before determining interface structure or policy. Designers can

observe and listen to their users and tap into their discontent, confusion, or hesitations. Consent

screens can sometimes raise doubts or apprehensions among users, especially when they involve

sharing personal information.

Another step is the problem definition. Often, consent dilemmas are couched in terms that focus

too narrowly on consent or on simple agreement, rather than on providing a well-informed choice.

---

<!-- PAGE 22 -->

In online banking, for instance, it is not a matter of simply getting an ‘opt-in consent’ but rather

ensuring a meaningful acceptance or denial. A sounder approach avoids solutions that introduce

hidden obstacles.

20

Next comes the ideation phase. Designers develop solution concepts, prototype designs, and

evaluate multiple approaches for representing consent information. The objective is not to

immediately develop a perfect solution but to study various designs and patterns. Prototype

testing can help designers identify which designs appeal to users and which introduce unnecessary

complexity.

Prototyping allows ideas to be worked into a tangible form. Even a minimal prototype or

wireframe can show how people will engage with consent formats. Prototyping can help to

improve text, page designs, and navigation before they are put into production. Where

prototyping is especially helpful is in assessing whether consent language is accurate and relevant,

as well as understanding how well an interface supports or compromises end-user control.

Iteration is where design thinking begins. Consent interfaces require reassessment over time,

considering evolving expectations, technological developments, and legal frameworks. Feedback

from usability studies and user research informs this cycle. Through iterative, observation-focused

processes, organizations can transform consent design into an ethics-driven practice that aligns

with user autonomy.

6.3  Usability and Accessibility Considerations

A key principle of informed consent is usability. A dysfunctional navigation system prevents people

from making educated decisions based on their data. A system with confusing and unreliable

interfaces erodes autonomy and increases frustration, especially with the involvement of financial

information. Financial operations often carry emotional weight, so unclear interactions can quickly

lead to hesitation or withdrawal.

Usability refers to how easily a user can navigate an interface to perform necessary actions, such

as accepting, rejecting, and granting permissions. Text density, technical slang, and unintuitive

menu paths reduce comprehension. Minor elements of an interface, such as button placement,

---

<!-- PAGE 23 -->

text, icons, and whitespace, influence where users focus their attention when encountering

consent notification popups. Inconsistencies in these elements can lead to misunderstandings of

the information presented or to the missing important information. Clear text, intuitive flows, and

well-structured content lower cognitive load. These principles also align with regulatory guidance,

which expects consent interfaces to be clear, accessible, and easy to understand (EDPB, 2020).

21

Accessibility can work in alliance with usability. Users possess varying skill levels, experiences, and

limitations. Therefore, a designer must incorporate all these aspects into the interface.

Accessibility in design relates to making text readable, providing good contrast, facilitating screen

readers, enabling keyboard navigation, and providing alternative text. A designer with a vision for

accessibility is not someone who strictly complies with rules and regulations but someone who

dives into issues of equality and justice to help people retain control of their information.

A good thing to keep in mind is context. Often, people access mobile banking apps in stressful and

complicated situations. Here, accessibility functionality can work wonders. Practices such as

providing reassuring feedback, using focus indicators, and designing effective error handling can

help minimize errors. The support for different screen sizes and assistive technologies can be very

helpful in this regard.

User-centered design promotes a culture of fairness and truth. When people are informed of their

choices and can make decisions confidently, they will behave in ways that correspond with their

real intentions. An accessible interface is less presumptuous and less likely to include designs that

mislead users into making unwanted decisions. User-centered design helps build a culture of trust

and provides a solid foundation for a responsible consent model that remains transparent and

empathetic with users in an evolving system.

7  Case Studies and Comparative Analysis

After establishing consent management theory in detail, this chapter will review the studied

concepts in action within existing banking systems. It will examine selected banking interfaces and

the choices they make when designing consent flows. The presented cases are not the subject of

critique or judgment; instead, they illustrate how design decisions affect consent management in

financial systems.

---

<!-- PAGE 24 -->

Every situation reveals how consent is organized within these institutions, how it is communicated

transparently, and how users can control their sensitive information. Some banks view consent

through the lens of a long-term relationship, offering customers the opportunity to update their

consent preferences at any time. Other banks practice a minimalist approach to consent, treating

it as a matter of law.

22

The chapter further considers the challenges banks face, including regulatory deadlines, existing

systems, and the cutthroat nature of competitive markets in which they operate. Such pressures

are frequently prioritized over mere design considerations when making interface decisions. Even

for banks with good intentions, opportunities for customer empowerment might be overlooked

due to technical or organizational realities. The case studies include success stories and life

lessons, followed by recommendations in the next chapter.

7.1  Analysis of Existing Banking Application Interfaces

In this section, consent in the interfaces of three banks, namely Barclays, Revolut, and Bank of

America, will be reviewed. The GDPR and other international data protection laws set a minimum

standard for consent but leave the details of its presentation to each organization. Therefore,

banks respond to these standards in different ways, which affects consent management

processes.

Barclays attempted to bring a new method of consent management into a format aligned with

existing systems. During the onboarding phase, a notice appears in a short, layered structure,

rather than in a traditional page-long format. Further along in this interface, consent preferences

become accessible in a ‘Manage app permissions’ option, where users can verify or update their

preferences. While not a radical redesign, this approach begins to recognize the importance of

readability in a system where a flashing novelty is infeasible.

Revolut takes a mobile-first approach and integrates consent into both sign-up and account

settings. The different types of data are presented clearly. Users are not expected to consent to

everything at once; they can return to any settings in "Privacy Preferences." While this system is

simpler, it still provides options for user control. Figure 6.1 illustrates how access permissions are

distributed within this interface.

---

<!-- PAGE 25 -->

23

Figure 6.1. Revolut privacy settings show category-based consent controls for marketing,

payments, and analytics

Source: Publicly available application interface screenshot, accessed October 2025.

Bank of America offers a more fragmented experience shaped by U.S. regulations and the bank’s

large technical environment. A user can control permissions for data processing, sharing with third

parties, and marketing targeting, but these settings may change by device and application. Such

inconsistencies can confuse users who expect a stable interaction across platforms. Although the

bank complies with the law, the interface does not always prioritize transparency and

understanding.

Taken together, these examples show that legally sufficient consent does not necessarily make the

experience positive. Language and reversible consent substantially affect consent decisions. A

system that focuses on consent for a function can hinder participation. In contrast, a consent

interface that raises awareness can empower people to make decisions about their own data with

higher confidence.

---

<!-- PAGE 26 -->

24

7.2  Case Studies of Successful Consent Management Implementations

In this section, two banks will be considered: ING Spain and Nordea, which take different

approaches to processing consent. In contrast to ING Spain, Nordea will describe consent in

situations where third-party information is accessed. While ING Spain focuses on consent through

improved design and workflows across ING Bank systems, Nordea will describe consent in

situations where third-party access to information occurs. These cases show how practical design

decisions can support understanding and reduce user confusion. In this chapter, interface design

refers to how consent information is organized, displayed, and accessed within an app or website,

and how it helps users identify their options faster.

ING Spain selected Didomi’s Consent Management Platform to consolidate consent across their

online and mobile channels. Figure 6.2 shows how ING Spain’s consent page is delivered via the

Didomi Consent Management Platform. Consent permissions are organized by purpose in a single

interface.

---

<!-- PAGE 27 -->

Figure 6.2. ING Spain consent settings implemented through the Didomi Consent Management

Source: Consent platform vendors, accessed October 2025.

25

Prior to this, customers frequently encountered consent prompts with inconsistent terminology.

This inconsistency leads to confusion and redundant actions. With this new interface design

approach, consent messages are presented in a standard format across all channels. Such

standardization eliminates redundancy and improves pattern recognition. Reports from Didomi

indicate higher engagement after the change, suggesting that users better understood the

information when it appeared consistently (Montes, 2024). The implementation is technically

simple but improves usability by reducing cognitive load and maintaining a predictable flow across

devices.

Nordea’s example illustrates authorization flow for third-party data access in an open banking

context, where external services request permission to access a user’s bank data. Open banking

allows third-party services, for instance, budgeting or payment apps, to access bank data with the

user’s permission. These use cases require explicit consent due to the sensitive nature of the

financial data. When a third-party request is made, Nordea redirects the user to its own interface

to confirm or deny access. Figure 6.3 illustrates Nordea’s open-banking consent flow, where third-

party access is authorized within the bank’s native interface.

---

<!-- PAGE 28 -->

26

Figure 6.3. Nordea’s open banking identification flow, showing third-party access approval within

the bank’s secure authentication interface

Source: Nordea Open Banking documentation (Nordea Group, n.d.), accessed December 2025

The identification flow occurs within their own applications at banks, not via a service. It implies

that users do not have to assess the credibility of unfamiliar applications in real time. This flow

provides control during high-risk data-sharing actions. As a result, consent is easier to understand

at the exact moment it is given.

Through these examples, it is evident how consent design improves user understanding and trust.

ING improves UX simplicity by standardizing the consent management platform interaction across

all channels. Nordea focuses on control: all third-party requests for access to user data are

authorized in a single interaction screen, ensuring a predictable and secure process. These cases

show that effective consent management does not depend on complex features. Instead, it relies

on a simple interface layout that support conscious decisions of users

---

<!-- PAGE 29 -->

27

7.3  Comparative Analysis of Different Consent Management Approaches

Every case study mentioned above, including Revolut, Barclays, Bank of America, ING Spain, and

Nordea, takes a different stance when handling consent. As a matter of fact, this is in line with

their business models, architecture, and environments. Although each organization is guided by

regulations such as GDPR and CCPA, they have different interpretations.

Some banks prioritize usability and user control, while others focus on formal obligations and risk

mitigation. As such, this affects how consent management is handled, where consent is displayed

on-screen, and how accessible the update functionality becomes over time. As a result, consent

can appear either as a clear interaction that supports user understanding or as a background

requirement enclosed in complex settings.

Revolut exemplifies a mobile-first, consent-by-design approach, being highly user-centric

throughout the process. A simple, straightforward approach is presented for each category of

personal information, with a prominent call-to-action button. Users can return to and manage

their consents in "Privacy Preferences" at any time.

This approach minimizes cognitive load by consolidating all permissions in one place and allowing

modifications to be viewed immediately. Figure 6.4 below shows how privacy settings can be

presented in a single view, allowing users to review and adjust their preferences rather than

navigating through a series of screens. As a result, consent is treated as an ongoing interaction

rather than a one-time requirement.

---

<!-- PAGE 30 -->

28

Figure 6.4. Revolut’s “Privacy Preferences” provide centralized access to consent settings for

advertising, data sharing, and analytics.

Source: User-captured interface screenshot from publicly accessible sources, accessed October

2025.

This structure shows Revolut’s focus on making things simple and easy to communicate with. This

approach works well for most people but may feel limited for those who want more detailed

explanations or legal references. Revolut prioritizes accessibility over complexity, which improves

the system’s intuitiveness but leaves some information abstract.

While this might be uncommon in personal accounts, Barclays employs the most traditional

approach informed by existing systems. The bank offers a layered privacy structure, but other

activities, such as account settings, remain hidden behind numerous permission prompts.

Although options are available, they are usually obscured by submenus or presented in overly

technical language. Regulatory guidance warns that patterns like this may undermine informed

consent (EDPB, 2022). As a result, the flow feels transactional rather than supportive. Barclays

---

<!-- PAGE 31 -->

complies with its legal obligations, but the design reflects the challenges of updating legacy

infrastructure and the tendency of large banking organizations to prioritize risk management over

user engagement. This approach is illustrated in Figure 6.5.

29

Figure 6.5 Barclays push notification settings illustrate a traditional consent interface with dense

explanatory text and limited interaction options.

Source: Barclays Help Center, accessed October 2025.

Bank of America is another example of a system formed under regulatory requirements in a

decentralized technical environment. The application provides consent options for both data

collection and sharing, but this is inconsistent across devices. A customer may be presented with

different consent requests based on the device they are using, which can compromise consistent

behavior across devices. The bank offers a range of options that comply with requirements but do

not lead customers to a substantive level of understanding. These issues were identified in

regulatory guidance on consent clarity and interface framing (EDPB, 2022). At this stage, consent is

reduced to a compliance requirement rather than an essential part of transparent consent

---

<!-- PAGE 32 -->

management. This compliance-oriented framing is illustrated in Figure 6.6, where consent is

presented as a single acceptance step combining multiple legal agreements.

30

Figure 6.6. Bank of America consent screen showing a bundled acceptance of multiple legal

disclosures during onboarding.

Source: Bank of America, Mobile Banking Instructions, accessed October 2025.

ING in Spain uses a consent management platform from Didomi that integrates consent across all

mobile, web, and desktop channels. The same messages and choices are presented to customers

on all channels. Moreover, ING can conduct interface tests and measure consumer engagement

with these interfaces. The strategy is straightforward. However, it is largely delegated to an

external platform, which may be less effective in this context.

The Nordea example does not illustrate an ongoing consent workflow but rather a well-secured

authorization with explicit approval to share information. This demonstrates how consent for data

sharing can be presented when relevant. As a result, approval remains within the bank’s

---

<!-- PAGE 33 -->

ecosystem, which clearly indicates who is requesting access and what information they are

accessing. Although this model relies on a rigid format with limited personalization, it provides

stability when handling sensitive operations. In this way, Nordea Bank prioritizes security and

stability, whereas Revolut’s system is more adaptable.

31

Taken together, these examples suggest that no one approach works in every case when designing

a consent management system. Effective design depends on how well the approach fits a bank’s

system architecture, regulatory pressures, and user expectations.  Revolut and ING prioritize

access and consistency. Nordea focuses on safety and usability. Examples given by Barclays and

Bank of America illustrate the difficulty of scaling consent in existing, or perhaps more complicated

systems, for more current consent principles. In each of these examples, good communication,

solid structure, and reversible decisions can go a long way in making a good impression.

An efficient consent management design goes beyond adding toggles or checkboxes. It requires

integrating clear data management solutions throughout the user journey to make predictability

and alignment with user-centered values the key priority.

8

Implementation of Consent Management Tool

8.1  User Experience Design of the Consent Management Tool

The project kicked off with a focus on User Experience pain points. The key question was how

people interact with consent in a banking environment and why these moments are often

perceived as confusing or intrusive. Consent is more than a signature; it is an ongoing relationship

with a bank. The goal of this project was to make each step understandable, easy to follow, and

reversible. The goal was to reduce pressure and ensure people felt their choice was honored.

The first stage involved creating a map of typical user flows. For banking apps, critical consent

moments occur during onboarding, the standard transaction cycle, and updates to terms and

conditions. While onboarding remains a critical moment, most applications are guilty of displaying

a series of dense screens full of information, which most users skim and ignore. To address this

issue in the prototype, a series of smaller steps for obtaining consent has been implemented. In

this case, each screen displays a single primary decision with a rationale. While this provides a

---

<!-- PAGE 34 -->

moment for reflection, it does not render the process endless. Initial sketch testing indicated a

preference for reading when information is presented in smaller chunks. Figure 7.1 summarizes

the main consent flow implemented in the prototype, from the initial snapshot view to category-

level decisions and confirmation.

32

Figure 7.1. Overview of the consent management flow implemented in the prototype.

Source: Created on Whimsical

Prototyping played a dominant role in influencing design decisions. Low fidelity prototyping

enabled testing of different designs, ranging from a simple list to a more extensive presentation.

User responses suggested a preference for short title descriptions with expandable title links

rather than a series of text descriptions. Icons and dividing lines were added to assist in quickly

---

<!-- PAGE 35 -->

categorizing information, such as analytics, personalization, and marketing, which will allow a user

to promptly realize which type of decision they were on the verge of making before delving into

detail. The prototypes are shown in Appendices 1-3 (Figures A1.1-A3.2).

33

Accessibility considerations were incorporated from the beginning. The prototype was tested for

color contrast and font size, and modifications were made accordingly. Interactive elements, such

as buttons and switches, were consistent in size and position, ensuring that users did not have to

learn a new interface at each step. The interface permitted a return to previous views, ensuring

that a user did not become disoriented. Such considerations were important for those who were

not very tech-savvy but needed control over their information.

The detailed consent view is a secondary consideration in consent evaluation and modification.

The page lists major consent categories, provides a simple explanation of their significance, and

shows their status at a given time. As soon as a user modifies a consent setting, the system

provides an immediate response, enabling the user to see the effect of the operation on the

consent setting. Such a system reiterates the idea of dynamic consent and the continuous

recording of this consent over time. The detailed consent view is depicted in Appendix 2 (Figure

A2.1).

Overall, the UX work provided a solid framework for the technical implementation. The interface is

more than a cosmetic overlay; it reflects the system’s state. A MEAN Stack prototype was

developed to achieve this goal. This prototype ensured that each UI interaction had a

corresponding change in the system.

8.2  Designing an AI-Driven Consent Explanation Tool

A common feature in banking apps is a lengthy, static consent notice that makes interaction

difficult. Users will go through these notifications, not because they do not see the relevance of

such information to a privacy matter, but because they find it cumbersome. For this reason, the

project considers an AI-supported explanation tool as a possible future addition to the consent

interface. The tool is not fully implemented in the current prototype and is presented as a design

idea rather than a finished feature. Therefore, a future addition to this consent interface will be an

AI-enabled explanation feature.

---

<!-- PAGE 36 -->

34

In this model, each consent notification will include a "Summarize" button that appears clearly on

screen. When clicked, a small message will appear summarizing the implications of this consent.

Such messages will be linked to a consent type and written in plain language. For instance, if a user

declines consent to personalization, this may result in basic account functionality and less

personalized recommendations. The detailed AI consent summary page is shown in Figure A3.1 in

Appendix 3.

The explanation facility can also assist with a basic understanding of usage. A common source of

confusion is how long information is retained and when it may be accessed after consent is

granted. Brief responses to these questions help clarify these doubts, whilst additional detail may

be left to the individual to read. A future development could enable this facility to operate in

tandem with consent, exactly as with all other components of this system.

Ethical matters inform this idea. The information provided will not influence a user's choice, nor

will it obscure trade-offs. Benefits and drawbacks must be clearly articulated. Anonymized usage

interaction data can indicate which consented-to topics confuse users without identifying specific

users. The tool will help users understand their choices.

8.3  Full-Stack Development Approach

The consent management prototype will be built using the MEAN stack: MongoDB, Express.js,

Angular, and Node.js. The selection of MEAN is based on its support for a modular system

architecture, ensuring tight integration between front-end and back-end operations. The authors

of this research paper hope to establish core functionality that can be tested and proven. Future

research work can include AI support.

MongoDB is used as the leading storage solution. Its flexibility enables updating consent

categories and consent histories in a time-stamped manner without requiring frequent migrations.

A consent record includes fields such as a user ID, consent category, status, and a history of prior

status updates, as consent status can change over time. This reflects the idea that consent is

dynamic rather than fixed.

---

<!-- PAGE 37 -->

35

A Node.js/Express.js backend provides a RESTful API for generating, reading, updating, and

revoking consent records. Each function validates inputs, verifies authenticated access when

necessary, and creates a record rather than updating an existing one. The strategy ensures that an

auditable trail is generated to assess consent dynamics over time. Although the current project

does not involve a real-world banking system, this setup is intended to serve as a traceable system

that meets regulatory requirements.

The Angular frontend implements consent categories, so they are presented across a set of related

but distinct views. Reusable components handle categories across the list view, detailed view, and

confirmation message. Such a structure promotes consistency in interface designs and reduces the

need for a total restructure when a new category is added. The interface design is based on

guidelines provided in Chapter 5 and usability results.

In this way, the full-stack solution links user actions directly to stored data. While this prototype

runs in a simplified setting, it illustrates how interface events and logic can be coordinated to

enable transparent consent management. Future work in this area may include adding

functionality to this stack, such as logging, integration points, or an explanation tool, as described

above. The focus of implementation is on demonstrating the consent architecture, traceability,

and control, rather than on scaling for production or integration with a banking system.

8.4  Back-End Functionality for Consent Management

The backend is responsible for storing, validating, and exposing user consent decisions in a reliable

way. Its role is to translate simple interface actions into structured, auditable records. To achieve

this, the system must capture each decision in a retrievable format for both user review and

technical checks.

Node.js and Express.js provide the groundwork for routing and application functionality. The API

offers endpoints for granting, updating, and revoking consent. The controllers handle the core

functionality, ensuring that request processing is decoupled from database access. Such a

structure is typical in web application development and, in this case, supports compliance by

enabling each endpoint to be tested and documented.

---

<!-- PAGE 38 -->

Validation occurs on every request. Middleware checks that the consent category is known that

the input format is valid, and that required identifiers are present. Each change is stamped with a

timestamp and written as a new record rather than overwriting the previous one. This creates a

simple but effective audit trail. Even if the interface changes later, the underlying history still

shows how decisions were made and updated.

36

The backend model supports partial consent states. For example, a user may allow personalization

within the bank’s systems but block data sharing with external partners. Consent records are

mapped into clear flags that other modules could interpret. Although this project does not

implement complex downstream systems, the structure is ready for future expansions if the tool is

integrated into a larger environment. Security and traceability are built into the design. Access to

detailed logs is restricted, and log data can be protected with hashing or similar measures to

reduce the risk of tampering. Users should be able to request a readable summary of their own

consent history, while institutions can use the same data for audits. The current prototype

implements only the basic elements of this model. Still, the design is prepared for more advanced

features such as expiry reminders or scheduled reviews, where users could be prompted to

confirm whether their previous decisions still reflect their preferences.

8.5  Integration with Existing Banking Systems

This project does not integrate the prototype into a live banking system. However, the design

assumes how such integration could work in practice. Real banking environments consist of many

connected services, including authentication, customer data, transaction processing, and

compliance tools. A consent management service should fit within this landscape without

disrupting critical operations.

One of the primary considerations in integration is identity management. Consent must be linked

to a persistent user identity rather than to a device or a browser session. In a production

implementation, for instance, the consent service would integrate with a bank's central identity

provider and access user IDs via a secure token service. The user would therefore be able to follow

preferences across channels such as mobile, web, and branch.

---

<!-- PAGE 39 -->

Data flow is another area that would be especially important. Other systems would need to verify

consent before using personal data for analysis, personalization, or external sharing. In a future

integration, the consent service would expose a simple API to retrieve the relevant flags for a

given user. Systems that lack a mechanism to call the API in real time would receive periodic

exports to update their local rules.

37

Internal visibility can also be controlled. Customer service or compliance officers may need access

to verify whether consent was given, when it was disclosed, and for what purpose. A dashboard

with role-defined access rights can help achieve this without exposing other information. All

access would be logged to support accountability.

Integration would also require a consistent language. If different systems describe the same

consent option in other terms, users will become confused, and trust may erode. Aligning wording

and options across channels is therefore as important as technical integration. While the current

prototype remains independent, the design decisions anticipate these constraints and outline a

path toward a system that can be connected to real banking infrastructure in a controlled and

transparent way.

9  Usability Testing and User Feedback

This chapter will discuss the evaluation of the prototype and how the consent model design was

informed by user feedback. The goal of this stage is to determine whether the consent model is

understandable to users and whether they can easily complete critical tasks without confusion.

The following sections will address the plan for conducting this evaluation, how to develop a

consent model, and the key elements required for understanding.

9.1  Usability Testing Plan

The usability testing primarily involved observing how well participants understood and navigated

the consent management interface. The objective was to identify areas of uncertainty and assess

how well they could make an informed decision. In the first usability test, participants were asked

to complete a series of tasks, including viewing consent categories, updating preferences, and

searching for additional information. They were encouraged to think aloud so that their thought

---

<!-- PAGE 40 -->

process could be monitored. Observation during these tests allowed analysts to pinpoint where

they may have paused or skipped information and to request clarification. A follow-up, smaller

usability test was conducted after refining the designs.

38

9.2  Category-Based Consent Overview (First Layer)

The first layer presents consent categories at a higher level. Its purpose is to help users understand

the consent model structure before viewing individual consents. The consent overview screen

shows all data categories in a simple tile layout. Each category has an icon and a short title that

indicates the type of information it contains. This first layer is intended to provide information to

users of the consent structure. When hovering over a category, users can see how the data is

utilized and whether the category is active or inactive. A green badge indicates that all items in a

category are accepted, while a yellow badge indicates that only some consents are accepted. This

high-level view replaces long text blocks commonly found in banking interfaces and provides users

with a clearer understanding of how to navigate the categories. Testing suggested that most users

identified consent areas more quickly with this layout.

9.3  Detailed Consent View (Second Layer)

The second layer provides a more detailed view of consent choices. It allows users to review

individual permissions within each category and adjust them as needed. When users access a

category, the interface expands to display the individual consent items beneath it. Each item has a

short label and a checkbox indicating whether the permission is enabled or disabled. This second

layer provides users with a clearer view of the category's contents. If a category contains both

enabled and disabled items, this partial state is indicated by a yellow badge in the first-layer

overview. Tooltips appear next to each item, explaining what each consent type means and why it

might be important. These tooltips open on a hover and provide brief explanations without forcing

users to read long paragraphs. This layer illustrates gradual disclosure: users first check the state

of a category, then review specific items as needed. Most participants reported that this structure

was clearer than the earlier design, although some technical terms still confused them.

---

<!-- PAGE 41 -->

39

9.4  “Smart Summary” AI feature

The consent management tool prototype demonstrates an AI-generated summary of a user’s

selections in plain language. This AI-powered feature consolidates active and inactive categories

into a single, concise message, allowing users to review all their selections without navigating each

category again. The summary highlights the active data types and informs the user which will not

be used if specific categories are inactive. Additionally, it tells them that they can change these

settings at any time through the consent management view. Participants found this summary

helpful to confirm their decisions before saving changes. Some wording may still need

improvement to keep the explanations accurate and easy to read, especially for users who prefer

shorter guidance.

10 Results

This chapter presents the main findings from two rounds of usability testing, focusing on users’

understanding of consent model concepts, points of confusion among participants, and the effects

of design modifications. Additionally, this chapter will identify improvements achieved in the

second round of usability testing and areas that require further improvement.

10.1 User Feedback Analysis (First round of User Studies)

The first testing phase identified several issues with users’ understanding of the navigation. The

main issue was the first consent-management screen. Users were overwhelmed by the lengthy

block of text at the start of the flow. Some participants were adamant that they "never read

consent descriptions in real life and did not do so during testing," which suggests a negative

impact on the user experience. Several participants did not use the explanatory tooltips because

there were no clear visual cues indicating where to hover or tap. Some were unsure how to

navigate the category-based interface because they did not understand where consent items fit

within these categories. A minority of respondents were uncertain about the effects of disabling

specific options for their personal banking.

---

<!-- PAGE 42 -->

40

10.2 Iterative Improvements based on User Input

A few parts of the prototype were updated in response to this prototype. The long consent

description was broken into smaller segments to make the information easier to process. This

reduced cognitive load and helped participants focus on one decision at a time. Shorter headers

and simpler category labels were added to make the purpose of each screen more specific. Icons

were added to help participants identify consent types more quickly. Tooltip placement was

adjusted so additional explanations appeared directly beside the relevant area. Some phrasing was

simplified to make definitions clearer while preserving meaning. These adjustments were intended

to reduce friction during the management task and to support users who prefer scanning to

reading long text.

10.3 Observed Improvements and Remaining Gaps (Second round of User Studies)

The second testing phase involved a smaller participant group but showed notable improvements.

Task completion time decreased, and navigation between screens occurred with minimal pauses.

Testers found it easier to follow a shorter sequence of steps and no longer felt lost in the process.

Testers quickly noticed icons in each category, which helped them better understand the intent

behind each permission level. More test participants opened tooltips without prompting, thanks

to improved positioning. However, some matters were left unresolved. One participant remained

unsure about the nature of the payment-related option and whether disabling it would affect

other banking activities. A third participant recommended improving summary information on the

final "consent overview" page. The results have demonstrated that not all consent terminology

and the final stage of consent have yet been optimized. These conclusions support earlier findings

that interface structure significantly affects consent behavior (Nouwens et al., 2020).

10.4 Final Improvements Suggestion

The final section summarizes the remaining issues and proposes areas for further refinement. The

two rounds of testing indicated that the new flow improved clarity; however, several areas still

require attention. Some users continued to struggle with labels in the Payments and Activity

categories. These may require simpler terms or short examples that illustrate how the data is

used. The final “consent overview” also needs more precise descriptions so users can understand

each category’s state without opening it. Further testing with a broader user base would help

---

<!-- PAGE 43 -->

confirm whether the changes reduce confusion across different levels of digital experience. Future

work should investigate how long-term use affects trust and willingness to revise consent choices.

These steps would further support informed and confident decision-making.

41

11 Discussion and Conclusion

11.1 Linking Results to Research Questions

The study followed the guidelines presented in Chapter 2 for research questions concerning

consent management, user experience, and legal protocols in digital banking. The first research

question examined how consent is currently used in banking systems and whether this usage

supports an understanding of consent in banking. The research question was answered through

the first usability test. The findings showed that consent management in banking systems often

employed complex legal language, confusing formats, and terms that users did not clearly

understand. This leads to hesitation and doubt during critical decision-making.

The second research question examined how end users perceive and use consent functionality.

The results obtained from both testing phases indicated the benefit of a more transparent

structure and progressive access to information. Having a primary overview organized by

categories, in addition to a detailed lower-level view, helped ensure that end users understood

what they were agreeing to and where they could make modifications. Improving design through

more explicit labeling and tooltips increased end-user confidence in managing their consent

decisions.

The third research question focused on how regulatory requirements can be incorporated into

interface design without undermining control. The results demonstrate that legal compliance does

not require complicated or restrictive interfaces. When consent is presented as a reviewable

process, users feel more in control while the system remains aligned with regulatory expectations.

Together, these findings show that user-centered design can support legal compliance, improve

usability, and strengthen trust when consent management is integrated into everyday banking.

---

<!-- PAGE 44 -->

42

11.2 Interpretation of Findings

The results indicate a clearer understanding of consent management among users when

information was presented in concise steps, with headings used to guide navigation. This aligns

with prior conclusions on cognitive load and recognition-driven navigation. Furthermore, it

confirms that congested texts, whether simplified or not, impair interaction with consent

management systems. Although assistance from a category-based design facilitated understanding

of the system’s architectural model, some concepts require more precise definitions. The progress

observed in the second iteration confirms that a minimalist approach to system structure can

significantly improve understanding and confidence in use. These observations support the views

presented in earlier chapters, including intuitive design, progressive disclosure, and control in

design.

11.3 Sustainability Considerations

A well-organized consent flow supports social and digital sustainability by helping users

understand how their data is handled. Clear and intuitive design reduces information gaps and

supports users with different levels of digital competence. A consent workflow with an organized

management system supports social and digital sustainability by providing users with clear

information about data processing. A workflow with an organized consent management system

will be easy to access and understand, helping less tech-savvy users and promoting social

sustainability. Furthermore, this consent workflow, supported by an organized consent

management system, will be updated in the future, contributing to digital sustainability by

addressing all regulatory requirements.

Apart from ethics and social aspects, sustainability also involves a technical angle in this case. As

noted, a consent architecture with a modular design, based on reusable elements and well-

structured data models, can be easily maintained and expanded over time in alignment with

regulations and evolving business needs. Technical sustainability provides a foundation for a

responsible, continuous approach to developing digital banking systems in such instances.

---

<!-- PAGE 45 -->

43

11.4 Development Proposals

Future improvements should focus on using explicit technical terms, especially in the “Payments”

and “Activity” categories, as was mentioned in previous chapters. The Consent Overview screen

would benefit from clearer description tooltips to help users be more confident with their choices.

Comprehensive user testing across different age groups and digital skill levels would help assess

whether the design is effective for a broader user group. It may also be helpful to evaluate how

users interact with the consent model over time and whether the “Smart Summary” feature

improves long-term understanding. These steps would help strengthen informed decision-making

in digital banking.

11.5 Conclusion

This study examined how consent management in digital banking can be made more

understandable and controllable from a user’s perspective. A consent management prototype was

designed and implemented using a two-level structure: a category-based consent overview and a

detailed consent view for reviewing and updating individual choices. The prototype was evaluated

through a small survey, two rounds of usability testing, and semi-structured interviews.

The findings show that traditional consent screens, which rely on long legal text and limited

interaction, do not support informed decision-making. Participants tended to ignore or skim this

information and felt unsure about the consequences of their choices. In contrast, the layered

consent interface, shorter explanations, and visible status of consent states helped users orient

themselves and make more deliberate decisions. At the same time, some concepts and categories

still require more precise wording and concrete examples.

The work contributes three primary outcomes. First, it demonstrates a practical consent interface

design that supports reversible decisions, visible status, and gradual disclosure. Second, it provides

empirical evidence that user-centered design principles, such as empathy, accessibility, and

flexibility, can be applied to consent flows without compromising regulatory requirements. Third,

it offers design recommendations for future work, including the potential use of an AI-supported

explanation tool and integration into existing banking infrastructures.

---

<!-- PAGE 46 -->

Overall, the study suggests that consent in digital banking need not be a purely formal

requirement. With careful design, it can become a clearer, more approachable part of the user

experience, supporting both legal compliance and long-term trust.

44

---

<!-- PAGE 47 -->

45

References

California Consumer Privacy Act of 2018, Cal. Civ. Coda § 1798.100 et sei. (2018). 
https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CI
V&title=1.81.5

European Data Protection Board (EDPB). (2020). Guidelines 05/2020 on consent under Regulation 
(EU) 2016/679. 
https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_202005_consent_en.
pdf

European Data Protection Board (EDPB). (2022). Guidelines 3/2022 on dark patterns in social 
media platform interfaces. https://www.edpb.europa.eu/system/files/2022-03/edpb_03-
2022_guidelines_on_dark_patterns_in_social_media_platform_interfaces_en.pdf

Financial Conduct Authority. (2018). Report on a study of how consumers currently consent to 
sharing their financial data with a third party https://www.fca.org.uk/panels/consumer-
panel/publication/fscp_report_on_how_consumers_currently_consent_to_share_their_data.pdf

Følstad, A. and Hornbæk, K. (2017). Comparing usability problems and redesign suggestions 
elicited with think-aloud and constructive interaction. Human-centric Computing and Information 
Sciences. https://hcis-journal.springeropen.com/articles/10.1186/s13673-017-0100-
y?utm_source=chatgpt.com

Gartner. (2024). Market guide for consent and preference management. Gartner, Inc. 
https://www.gartner.com/en/documents/5643691

General Data Protection Regulation (GDPR). (2016). Regulation (EU) 2016/679 of the European 
Parliament and of the Council. https://eur-lex.europa.eu/eli/reg/2016/679/oj

Kyi, L., Haidl, A., Santos, C., Roesner, F., & Biega, A. (2024). In Proceedings of the CHI Conference 
on Human Factors in Computing Systems. https://doi.org/10.1145/3613904.3642260

McKinsey & Company. (2020). The consumer data opportunity and the privacy imperative 
https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/the-consumer-data-
opportunity-and-the-privacy-imperative

Montes, Karen. (2024). Unified digital consent: the strategy behind the success of ING Spain. 
https://www.didomi.io/blog/ing-spain-case-study

Nordea Group. (n.d.). Open banking authentication and consent flows. 
https://documentation.nordeaopenbanking.com

Nouwens, M., Liccardi, I., Veale, M., Karger, D., & Kagal, L. (2020). Dark patterns after the GDPR: 
Scraping consent pop-ups and demonstrating their influence 
https://doi.org/10.1145/3313831.3376321

---

<!-- PAGE 48 -->

46

Ponemon Institute. (2012). The Human Factor in Data Protection. 
https://www.ponemon.org/news-updates/blog/security/the-human-factor-in-data-
protection.html

World Economic Forum. (2018). Personal data: The emergence of a new asset class. 
https://www.weforum.org/publications/the-appropriate-use-of-customer-data-in-financial-
services/

Yusuff, M. (2023). Ensuring Compliance with GDPR, CCPA, and Other Data Protection Regulations: 
Challenges and Best Practices. Federal University of Technology. 
https://www.researchgate.net/publication/387224965

---

<!-- PAGE 49 -->

Appendices

Appendix 1. Category-Based Consent Overview (Figma)

The figures illustrate how consent categories are grouped and displayed.

47

Figure A1.1. Category-based consent overview presenting high-level consent categories / Figma, 
2025

Figure A1.2. High-level consent categories management view / Figma, 2025

---

<!-- PAGE 50 -->

Appendix 2. Granular Consent Settings Within a Category

The figures illustrate how detailed consent settings and partially accepted consent categories are 
grouped and displayed.

48

Figure A2.1. Detailed consent settings within the Security category / Figma, 2025

Figure A2.2. Category-based consent overview presenting partially accepted Security category / 
Figma, 2025

---

<!-- PAGE 51 -->

Appendix 3. Consent Summary and Confirmation View

The figures illustrate how the AI-powered consent summary and category-based consent 
confirmation message are grouped and displayed.

49

Figure A3.1. AI-powered consent summary / Figma, 2025

Figure A3.2. Category-based consent confirmation view presenting fully accepted categories / 
Figma, 2025

---

<!-- PAGE 52 -->

Appendix 4. User Questionnaire (Exploratory, n=6)

The figures present the exploratory questionnaire items and corresponding answers collected 
prior to usability testing. The questionnaire was used for exploratory input and to guide usability 
sessions. Due to the small sample size, the results are descriptive and not generalized.

50

---

<!-- PAGE 53 -->

51

---

<!-- PAGE 54 -->

52

---

<!-- PAGE 55 -->

53

---

<!-- PAGE 56 -->

54

---

<!-- PAGE 57 -->

Appendix 5. Semi-Structured Interview Topics

The interviews conducted for this study followed a semi-structured format.

55

The discussions were guided by key topics related to the consent management prototype and

participants’ experiences. This approach allowed exploration of relevant pain points raised during

the interviews while ensuring that all sessions covered the same topics.

1.  What are your first impressions of the consent interface?

2.  How clear do you think categories and labels are?

3.  How much control do you feel like having over your consent choices?

4.  Do you understand the consequences of accepting or declining the consent option?

5.  How confident do you feel when making consent decisions?

6.  Please compare this tool with consent experiences in existing digital banking applications.

7.  Any confusion, hesitation, or frustration during interaction? Please, share.

8.  Suggestions for improving clarity, structure, or usability? Please, share.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Optimizing Banking Application
Interfaces

A User-Centric Perspective on Consent Management in
Digital Banking Environments

Olga Pakarinen

Master’s thesis
December 2025
Master’s Degree Programme in Information Technology, Full Stack
Software Development

Description

Olga Pakarinen

Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management

Jyväskylä University of Applied Sciences, December 2025, 55 pages.

Degree Programme in Information Technology, Full Stack Software Development. Master’s Thesis

Permission for open access publication: Yes

Language of publication: English

Abstract

This study examined the implementation of a consent management tool for digital banking users that is
more transparent, accessible, and controllable than existing solutions. This goal was achieved by designing
and testing a consent management tool and by examining the effects of different consent flows on users’
understanding and trust in decision-making. The study used a mixed-methods approach, including an initial
quick exploratory survey, two rounds of usability testing, and semi-structured interviews.

The prototype is structured into two levels. A category-based overview will allow users to view all the
categories of their data usage at a higher level. Users can also view and adjust individual permissions via a
detailed consent view.

During the usability studies, participants interacted with the prototype, provided feedback on the wording
and formatting of the text, and assessed their confidence in making consent-related decisions. The research
results showed that lengthy, complex consent language impairs users' understanding. Conversely, concise,
clear steps and explicit labels, along with the visibility of the consent state, improve users' perception of
control and confidence when consenting.

Research findings can inform practical recommendations for designing consent interfaces.
Recommendations include gradual disclosure of content, consistent structures, and the implications of
reversible consent decisions. Additionally, the study guides further development, including an AI-supported
summarization tool. The summary feature will explain why users need consent for specific options and how
their choices affect the security of their data. Ultimately, the main goal of this project is to establish and
promote best practices for creating a Consent Management Solution that supports users' needs above
those of regulatory compliance.

Keywords/tags (subjects)

Consent management, Digital Banking, User-Centered Design, Data Privacy, GDPR, Usability Testing

Miscellaneous (Confidential information)

None

1

Contents

1

2

Introduction ................................................................................................................. 3

Background and Context of the Study ........................................................................... 4

2.1	 Research Motivation ........................................................................................................ 5

2.2	 Research Objectives ......................................................................................................... 6

2.3	 Research problem and research questions ...................................................................... 6

2.4	 Scope and Limitations ...................................................................................................... 7

2.5	 Thesis Structure ............................................................................................................... 8

3

Ethical Considerations .................................................................................................. 9

3.1	 Research Integrity and Authorship .................................................................................. 9

3.2	 Transparency and Responsible Use of AI ....................................................................... 10

3.3	 Data Protection and Privacy .......................................................................................... 11

3.4	 Usability Testing and User Feedback ............................................................................. 11

3.5	 Balancing Legal Compliance and User Agency ............................................................... 12

4	 Methodology ............................................................................................................... 12

4.1	 Research Design ............................................................................................................. 12

4.2	 Data Collection Methods ............................................................................................... 13

4.3	 Data Analysis Approach ................................................................................................. 13

4.4	 Reliability of the Study ................................................................................................... 14

4.5	 Reflection on the Research Process ............................................................................... 14

5	 User Engagement and Consent Management ............................................................... 14

5.1	 Understanding User Behavior in Banking Applications ................................................. 14

5.2

Importance of User Engagement in Consent Management .......................................... 15

5.3	 Challenges in Consent Interface Design ......................................................................... 16

6	 User-Centric Design Principles ..................................................................................... 17

6.1	 Principles of User-Centric Design ................................................................................... 18

6.2	 Usability and Accessibility Considerations ..................................................................... 19

6.3	 Usability and Accessibility Considerations ..................................................................... 20

7

Case Studies and Comparative Analysis ....................................................................... 21

7.1	 Analysis of Existing Banking Application Interfaces ....................................................... 22

7.2	 Case Studies of Successful Consent Management Implementations ............................ 24

7.3	 Comparative Analysis of Different Consent Management Approaches ........................ 27

8

Implementation of Consent Management Tool ............................................................ 31

8.1	 User Experience Design of the Consent Management Tool .......................................... 31

2

8.2	 Designing an AI-Driven Consent Explanation Tool ......................................................... 33

8.3	 Full-Stack Development Approach ................................................................................ 34

8.4	 Back-End Functionality for Consent Management ........................................................ 35

8.5

Integration with Existing Banking Systems .................................................................... 36

9	 Usability Testing and User Feedback ............................................................................ 37

9.1	 Usability Testing Plan ..................................................................................................... 37

9.2	 Category-Based Consent Overview (First Layer) ............................................................ 38

9.3	 Detailed Consent View (Second Layer) .......................................................................... 38

9.4	 “Smart Summary” AI feature ......................................................................................... 39

10	 Results ......................................................................................................................... 39

10.1	 User Feedback Analysis (First round of User Studies) ................................................... 39

10.2	 Iterative Improvements based on User Input ................................................................ 40

10.3	 Observed Improvements and Remaining Gaps (Second round of User Studies) ........... 40

10.4	 Final Improvements Suggestion ..................................................................................... 40

11	 Discussion and Conclusion ........................................................................................... 41

11.1	 Linking Results to Research Questions .......................................................................... 41

11.2	 Interpretation of Findings .............................................................................................. 42

11.3	 Sustainability Considerations ......................................................................................... 42

11.4	 Development Proposals ................................................................................................. 43

11.5	 Conclusion ..................................................................................................................... 43

References .......................................................................................................................... 45

Appendices ......................................................................................................................... 47

Appendix 1. Category-Based Consent Overview (Figma) ....................................................... 47

Appendix 2. Granular Consent Settings Within a Category .................................................... 48

Appendix 3. Consent Summary and Confirmation View ......................................................... 49

Appendix 4. User Questionnaire (Exploratory, n=6) ............................................................... 50

Appendix 5. Semi-Structured Interview Topics ...................................................................... 55

3

1

Introduction

Digital banking has grown over the last decade. Mobile banking applications and online systems

now handle tasks that previously required a visit to a bank branch. As a result, customers expect

these services to be fast, simple, and continuously available. Since banking services have moved

online, the volume of personal data processed has increased, along with concerns for personal

information privacy.

Consent management defines how users accept or decline the processing of personal information

and how that consent is subsequently managed. Often, this relates to decisions about which

personal information can be collected, how it will be processed, and when it can be shared.

Regulations such as the GDPR and the CCPA set minimum requirements for the collection and

management of consent. According to Yusuff (2023), consent management in information systems

adds a level of trust and accountability in digital systems. In banking environments, consent

management affects how individuals' private data is handled. It shows that consent is more of a

practical mechanism than a legal concept.

In banking applications, consent is often presented in ways that are difficult for users to

understand. To present consent information and support users’ decision-making, designing an

efficient interface structure was selected as a key objective of this project. User behavior in

consent flows, information needs, and common points of misunderstanding are analyzed using

qualitative and quantitative methods. Based on these findings, a user-centered prototype is

developed. The design integrates consent into everyday interactions rather than presenting it as

an isolated legal item.

The research explores how interface design can align user expectations with legal requirements.

Banking systems must meet legal requirements, but they also need to function in ways that feel

reasonable to their customers. Still, clear communication and consistent data handling remain the

foundation for trust. This project blends regulatory analysis, user-centered design principles, and

observational usability testing to identify improvements in consent management for digital

banking interfaces.

4

2  Background and Context of the Study

The future of online banking depends on how user consent is defined and managed within data

privacy policies. Banks store large volumes of sensitive information about their clients. They need

to handle this information with caution while complying with confidentiality requirements. Several

laws regulate the processing of personal data, which increases the importance of consent.

Regulations such as the GDPR and the CCPA require organizations to manage personal data

transparently before processing it (GDPR, 2016).

Collecting and managing consents creates the foundation of data privacy governance in banking.

Legal regulations raise expectations for information security, particularly when personal data is

collected via explicit customer consent. As stated by Husain, financial institutions are obligated to

be transparent and accountable in handling all personal information in their operations (GDPR,

2016).

The General Data Protection Regulation and California Consumer Privacy Act both require express

consent before processing personal information (General Data Protection Regulation, 2016;

California Consumer Privacy Act, Cal. Civ. Code § 1798.100 et seq.). According to the European

Data Protection Board, users should be able to grant and revoke their consents (European Data

Protection Board, 2020). European data protection law states that “consent of the data subject”

refers to a voluntary, informed, and obvious indication of a person’s wishes (GDPR, Art. 4(11)).

This definition guides how banking interfaces must request and record user decisions.

Consent is closely related to risk management in banking systems. Given the frequent occurrence

of data breaches and cyberattacks, banks need to be especially careful with sensitive information.

Banks can develop secure systems and minimize the risk of unauthorized access by understanding

how users interact with consent systems. Additionally, banks aim to increase customer satisfaction

through personalized services. These services depend on users’ willingness to grant consent.

According to Gartner (2024), effective consent management supports risk control and responsible

data use.

Banks use data to create individual services, but only when users feel comfortable granting

permission. As indicated by the World Economic Forum, consent will always be heavily dependent

on customer expectations regarding personalization (WEF, 2018). When used wisely, consent

supports customer-centered services. When handled poorly, it compromises customer trust and

loyalty.

5

A bank’s reputation is shaped by how responsibly it handles consent and personal data. Neglecting

to obtain consent or failing to protect data may compromise customers’ confidence. McKinsey &

Company believes that strong data protection practices and consent handling are critical in

achieving sustained success in organizations (McKinsey, 2020). Digital banking systems must

balance legal requirements, user expectations, and technical limitations.

The materials used in this study reflect this balance. GDPR guidelines form the basis for the

consent analysis. Industry literature gives an insight into the banking industry, but sometimes

these texts are published with a commercial focus and must be interpreted with caution. Research

on consent management in digital banking remains limited, but the available sources support the

analysis conducted in this study.

2.1  Research Motivation

The new era of online environment has changed the entire meaning and perception of data

privacy. GDPR and the CCPA remind banks that consent should be obtained before processing

personal data. These requirements have pushed banks to revise their systems and ensure that

consent is properly collected and recorded. Banks can improve their management of regulatory

requirements and reduce legal and financial risks by examining how consent operates in real-

world banking interactions (Financial Conduct Authority, 2018).

Working with financial information adds an extra level of complexity due to its sensitive nature.

According to the Ponemon Institute (2012), banks must prioritize effective risk management

policies. This includes precautions against data leaks and the maintenance of incident response

plans in the event of security breaches. Addressing these risks requires an understanding of how

customers approach consent. Improving consent practices helps protect customers and supports

trust in financial institutions.

Cyber incidents remain a long-term issue. The increase in data theft and fraud highlights the need

for clear permission settings and reliable safety measures (Ponemon Institute, 2012). When

consent tools are predictable and easy to understand, users can manage their preferences with

confidence. Predictability promotes loyal relationships, and banks can meet expectations

regarding privacy and security (Financial Conduct Authority, 2018).

6

2.2  Research Objectives

Customers frequently manage personal information in digital banking applications. Therefore,

consent management has become a standard part of the user experience. Although consent

management flows are widely used across banking systems, their design and structure vary quite

extensively. The research will explore how these consent systems function and how customers

respond when they encounter them.

Legal requirements, particularly the General Data Protection Regulation (GDPR), affect the design

and implementation of consent mechanisms in banking applications. The study aims to improve

banking interfaces to make consent easier to understand and manage. User testing sessions and

participant feedback from individuals who interacted with the prototype will assist in this goal.

One additional goal is to investigate consent with double considerations: first, how well the user

understands it, and second, how well consent is documented and applied in the system. The

integration of these perspectives will help in understanding both where the design is already

effective and where it can be improved (Følstad & Hornbæk, 2017).

2.3  Research problem and research questions

User consent is a key area of study in data protection and customer experience in digital banking.

With growing online banking experience, there is a clear need for a consent management system

that is simple and easy to understand. While consent functionality is present in most online

banking systems, a significant gap exists between standard technical implementation and legal

requirements for consent, especially under the GDPR and the CCPA.

7

The most common problem with digital banks is inadequate regulation and poorly optimized

consent management systems. A consent management system with an unclear or intrusive

consent flow can easily affect customer satisfaction and compromise their trust. A modern digital

bank with limited knowledge of how to properly implement consent management systems must

therefore learn from existing practices, customer expectations, and real constraints of digital

banking.

This research addresses several questions. First, it reviews existing consent solutions in online

banking to determine how well they respond to industry standards and regulatory requirements.

Then, it investigates how users behave during consent management and how they understand

consent-related information. The study looks at users’ needs, challenges, and decision-making

through usability testing, questionnaires, and interviews. A further question is whether these

practices meet the expectations set by regulatory organizations such as the GDPR and the CCPA.

Additionally, this project aims to make recommendations on consent management in banking

apps more actionable. The design process will be supported by end-user testing and validation.

These inputs helped refine the prototype and assess whether the proposed model improved

understanding, supported user choice, and remained compliant with legal standards.

2.4  Scope and Limitations

Consent management in digital banking is the primary focus of this study. Likewise, regulatory

requirements, user experience, consent management design and architecture are three essential

components addressed through the user-centric perspective. The research investigates how users

understand consent, how they manage it, and how design choices influence these behaviors.

The research does not cover financial risks, back-end banking operations, or other organizational

policies beyond consent management. A combination of usability testing, interviews, and a

research questionnaire is used to identify existing commonalities in the requirements and

expectations of banking customers. The objective of this research is to find out how individuals

perceive consent management and banks’ expectations, and how effective design can support

these decisions in digital banking.

8

Some flaws have been noted. A limited research time resulted in a smaller user group, therefore

limiting the opportunity to generalize the findings. Conducting this research in a controlled

environment and not in a real-life banking system is another shortcoming. Several technical issues

have influenced the prototype design, which can be addressed as a simplified model of a banking

system. Despite these limitations, the findings provide a practical foundation for improving

consent design and guiding future research.

2.5  Thesis Structure

The findings of this research are presented in an eleven-chapter structure from background and

motivation through design, evaluation, and conclusions.

1.  Chapter 1 introduces the research topic and explains its relevance to consent management

in modern digital banking. The background is outlined, and consent is considered an

essential part of user interactions in a banking environment.

2.  Chapter 2 presents the research context. It reviews the regulatory framework, key

concepts, and definitions of data protection and consent. The chapter also reviews the

relevant sources on digital banking, consent management, and usability. In addition, it

presents the research motivation, objectives, research questions, scope, and limitations,

explaining what the study focuses on and what it does not.

3.  Chapter 3 presents ethical considerations related to the research. It explains how research

integrity, data protection, and responsible use of AI were addressed throughout the study.

The chapter also analyzes the balance between legal compliance and user agency, and how

ethical responsibilities were managed during the research and design phases.

4.  Chapter 4 describes the research methodology used in the study. It explains how the

research was planned, how data were collected and analyzed, and why these methods

were selected. The chapter also supports the credibility of the findings by addressing issues

of reliability.

5.  Chapter 5 focuses on user engagement in digital banking applications, with precise

attention to consent-related interactions. It examines how users encounter consent

management in everyday contexts, how they respond to it, and the challenges they face in

these interactions. The chapter compares observed user behavior to issues in consent

interface design.

9

6.  Chapter 6 introduces user-centered design principles and discusses usability and

accessibility in consent management. It explains how these principles support clear

communication, reduce users’ cognitive load, and help them make informed decisions in

banking digital environments.

7.  Chapter 7 presents case studies and a comparative analysis of existing consent-

management approaches in selected banking applications. The chapter reveals similarities

and differences between strategies and identifies common design patterns. In the end, it

discusses the strengths and shortcomings of the reviewed strategies.

8.  Chapter 8 describes the design and implementation of the consent management prototype

developed within this project. It explains key design decisions, user-experience principles,

and technical implementation choices. This chapter concludes by demonstrating how

regulatory requirements and user needs were translated into a working solution.

9.  Chapter 9 describes the usability testing process and the gathering of user feedback. It

outlines how the testing sessions were organized, how interface components were

evaluated, and how participants interacted with the prototype.

10. Chapter 10 presents the results of the usability studies. It summarizes the main results

from testing, including observed improvements in interaction with the revised prototype

and remaining usability issues.

11. Finally, Chapter 11 compares the results with the research questions and research

objectives. It reflects on the study’s contributions, summarizes development proposals,

and presents the conclusions.

3  Ethical Considerations

The project followed the ethical guidelines of JAMK University of Applied Sciences, the Arene

guidelines on the use of artificial intelligence (AI) in higher education, and the principles of

research ethics. User-centered design, regulatory analysis, and technical development were

addressed with ethical considerations integrated throughout the research process.

3.1  Research Integrity and Authorship

The author documented all research methodology, design, and analysis used in this study.

References to prior knowledge or authoritative materials used in this study follow JAMK

documentation standards. The study identifies both existing and new information. Each statement

in this study relies on primary legal documentation (e.g., the GDPR, the CCPA) and relevant

supporting materials. The ideas and conclusions were analyzed against expert perspectives and

appropriate academic materials.

10

The author originally developed all the research questions, design choices, technical decisions, and

interpretations of prior knowledge. The key concepts, analytical findings, and overall thesis

structure presented in the study were developed through the author's independent efforts and

knowledge. The references to previous studies and original contributions were clearly identified in

accordance with JAMK documentation guidelines. Legal perspectives were supported by the

source (the GDPR), academic, and professional literature. The author accepts complete

responsibility for the content, analysis, and conclusions provided in this research.

3.2  Transparency and Responsible Use of AI

As noted earlier, the research was implemented in several phases, with the author maintaining

control over content quality and executive decisions throughout the process. All written material

was produced as part of an independent thesis project. It demonstrates individual reasoning,

analysis, and interpretation of the subject.

Initially, AI-assisted tools (Copilot and ChatGPT) were used to support topic planning and refine

the research scope. These tools helped narrow down the study area, plan potential research

stages, and learn and adapt to academic tone.

AI-assisted language tools were used as a learning aid to become familiar with appropriate

academic vocabulary, style, structure, and argumentation. Example expressions and structural

suggestions were reviewed to identify common patterns in academic texts. AI editing assistants

(Grammarly and QuillBot) supported writing by addressing grammar, punctuation, sentence

structure, and vocabulary to improve consistency in academic writing. These tools neither shaped

nor influenced the study’s key findings.

After completing a few first drafts, AI was used in the revision process. Their purpose was to

support writing coherence and consistency of ideas. The author reviewed each paragraph

individually and used AI tools to suggest alternative phrasing for sentences that appeared

redundant, repetitive, or grammatically incorrect. This process was repeated in the following

revisions. The final text reflects the author’s ideas and conclusions at every stage, including what

content to keep, how to present the regulatory analysis, the author's own findings, and how to

structure the conclusions.

11

Every AI-suggested rewrite was critically reviewed and refined. Suggested changes that might have

affected meaning, introduced ambiguity, or conflicted with technical or legal accuracy were

excluded. Additionally, the author critically assessed and refined the suggestions to preserve their

personal understanding and intentions. All research questions, design decisions, implementation

logic, analyses, results, and conclusions presented in this thesis were developed by the author.

AI-assisted tools were used as supportive aids during the implementation phase to explain

common programming patterns, support debugging, and suggest refactoring. The general project

architecture, stack choices, data models, and application logic were designed and implemented by

the author. AI tools did not influence the author’s independent decisions on the project's design

and architecture.

3.3  Data Protection and Privacy

Nevertheless, this research did not involve actual private banking or personal information. The

information obtained in this research is based solely on usability studies and on prototype

interactive sessions. The responses obtained were anonymous and recorded without including

personal or financial information. Although this study focuses on people's reactions to consent

screens, it does not involve behavioral analysis. The information is recorded in notes, where it is

safely stored and used only for research.

3.4  Usability Testing and User Feedback

User feedback and usability testing were critical to the interface design. The participants were

informed of the research goals, their voluntary participation, and their right to withdraw at any

stage. Feedback sessions focused on interaction with prototypes rather than on personal issues or

financial information, therefore mitigating ethical concerns. Anonymity ensured that people were

not identifiable in the results. Feedback supported the design improvements but did not specify

them, as individual experiences vary. The research examined the ethics of maintaining compliance

with laws and users’ sense of control. Ethical design demonstrates that being compliant and using

a system can go hand in hand. Consent is not viewed as a regulatory or technological tool, but

rather as a way of making decisions with freedom.

12

3.5  Balancing Legal Compliance and User Agency

Legal obligations and control in consent management were the primary interest of the study. The

GDPR and similar laws have very specific guidelines when it comes to consent. However, following

these guidelines is not practical from a usability perspective. A design can be highly compliant with

these guidelines but may end up confusing users and leaving them with doubts about their own

decisions. As a result, consent management is a process that, over time, improves users’

understanding of data-sharing mechanisms, the importance of flexibility, and the need for user

control.

4  Methodology

4.1  Research Design

Mixed-methods analysis will be used to examine how users interpret and manage consent in

online banking. A connection to existing literature will be established through a literature review.

Three research methods will be utilized in this study: a short survey, a series of interviews, and

usability studies.

The survey provides critical quantitative data on users' opinions and preferences regarding

consent. The interviews provide information about confusing or complicated issues for users. The

usability tests provide real-world information about interaction barriers when completing a task.

Taken together, these provide a more complete perspective on reasoning, behavior, and

expectations among users, consistent with this study’s focus on improving experience, control,

and compliance.

During the planning phase, other methods were considered but not applied in this research, such

as a focus group study, extended analysis, or A/B testing. However, the methods utilized in this

research include a small survey, in-depth interviews, and usability studies, with two rounds of

prototype testing. Other methods will be considered in future research studies.

13

4.2  Data Collection Methods

Surveys were used to collect quantitative data on opinions about consent management in general.

An exploratory survey includes a Likert scale question, multiple-choice questions, and short

comments to make some early conclusions before performing usability tests. The small number of

responses obtained reveals that these results are suggestive and not representative. The survey

results can be found in appendices 4-5.

The main technique used in this usability study is usability testing, which tested how well

participants were able to navigate through the consent management interface. The parameters

measured in this usability study include task time, hesitations, error rate, and the proportion of

explanatory queries.

Following usability testing, semi-structured interviews were conducted to collect opinions on the

rationale for observed behavior, confusing interface language encountered during the studies, and

personal understandings of specific consent items. Open-ended questions helped to gather

responses that would not otherwise be possible from task performance data. Through a

combination of surveys, usability studies, and interviews, a better understanding of user needs

and pain points necessary for the redesign was achieved.

4.3  Data Analysis Approach

Analysis began with the organization of task-completion observations and questionnaire

responses. Descriptive information on completion time and reported difficulties was used to

summarize the survey results. Patterns in hesitation, missed steps, and misinterpretations were

compared among participants. Qualitative data from interviews and think-aloud sessions were

analyzed by theme. User comments were split into three areas: confusion about terminology,

difficulty locating information, and uncertainty about consequences. These themes were

compared with task observations to confirm or deny biased impressions of the author.

14

Such an analysis technique allowed both individual views and overall trends to be considered,

relating usage to explanations and identifying where a design hindered understanding. The results

were used to inform support improvements, which will be explained in detail in the following

chapters.

4.4  Reliability of the Study

Several aspects affect reliability. The sample size was small and therefore not sufficient to

represent all banking customers. The tests were conducted in a controlled environment rather

than in a real banking context. The prototype simplified several back-end support tasks, which can

influence how people understand the choices. Patterns were recognizable despite some of these

flaws. A combination of methods helped achieve reliable results, as different perspectives were

used to present distinct findings.

4.5  Reflection on the Research Process

The research was conducted in iterative cycles. Early tests revealed that the original structure was

overly complex, so the prototype was simplified and the focus shifted to task simplicity. Time and

scope limits required prioritizing essential features, such as presenting detailed consent items

under clear categories. These adjustments kept the study feasible while still answering the

research questions. Although the process was not linear, the iterative strategy improved the final

design and helped achieve more grounded conclusions.

5  User Engagement and Consent Management

5.1  Understanding User Behavior in Banking Applications

To design effective consent management solutions, it is important to understand how users

interact with banking apps. Users prioritize simple navigation when performing everyday tasks

such as checking balances, making payments, or viewing daily transactions. With improved

navigation, users can complete their tasks with less effort and increase their satisfaction with the

service.

15

Security is the initial focus of expectations in digital banking. It is well established that customers

want to be assured that their financial and personal information will be protected. While

technologies such as encryption and two-factor authentication are important, they must be

accompanied by clear communication. Users want to know how their information will be

collected, processed, and shared, and all this information must be presented in a simple way.

When this occurs, they will be convinced that a reputable financial organization is handling their

information responsibly and securely.

Consent management relies on this integrity. Requesting consent for an application must be

conducted in a way that protects user autonomy. A user must always have access to view, analyze,

and modify consent decisions. Therefore, with such an option being available, a user is in control

of their personal information.

Interfaces that respect user preferences are more likely to support long-term customer

relationships. When users can manage their sensitive information without confusion, they are

more likely to remain loyal to their chosen service. Updating interfaces based on observed

behavior and user feedback reinforces this pattern of trust. A clear and accessible consent

management experience provides users with confidence and complies with secure data

management practices.

5.2  Importance of User Engagement in Consent Management

User engagement is necessary to manage consent effectively in banking apps. Legal requirements

may not enable users to understand what they consent to or to be assured of the validity of their

consent decisions. User engagement supports autonomy by helping users understand consent

requests and adjust them according to their preferences.

When this sense of inclusion is established among users, they will feel valued and empowered.

They will unlikely perceive consent as an obligation but rather as a part of taking control of their

online presence. Users will have an opportunity to reflect before acting, as they will not consent to

a request until they have understood its meaning. In this way, consent is a dynamic process that

gradually evolves into an ongoing relationship of assurance and respect, rather than just a one-

time event.

16

Therefore, the design of consent mechanisms must go beyond simple checkbox interactions.

Consent solutions must be designed to ensure that end users understand them. Inclusion in this

context refers to ensuring that the end user feels their voice and opinion are heard. An accessible

experience will enable users to trust and commit to a loyal relationship with an organization that

adheres to these principles.

In a digital environment where privacy issues are becoming increasingly important, the

consideration of the user in consent decisions is both justified and necessary. Consent should not

be an administrative task but a dynamic and understandable process in the user experience. A

pragmatic, user-centric approach will help identify the balance between the legislation and the

value provided to users in financial institutions.

5.3  Challenges in Consent Interface Design

The design of consent interfaces in digital banking is a challenge. Designers face a challenge in

providing information in a manner that is not overwhelming to the end-user, especially when

dealing with consent content that is complex and not common knowledge. Long blocks of text lead

to confusion or disengagement, and many users skim these screens without understanding what

they are agreeing to (Kyi et al., 2024; Nouwens et al., 2020).  For this reason, consent fatigue sets

in, making consent less relevant in this context. Research analysis demonstrates that consent

interfaces influence one’s individual decisions, using interface designs to enforce decisions rather

than guiding them with the information they need to understand (EDPB, 2022). Given that digital

banking systems directly affect financial behavior in daily tasks, clear and consistent consent

management flows, and information provision need to be heavily prioritized.

Consent is not a one-shot experience. A person is likely to change their mind about using their

data depending on their life's circumstances. However, most banking systems have consent

models that do not permit straightforward preference settings. Consent interface systems that do

not allow revocation or modification of consent preferences can limit one’s options and reduce

their understanding of data sharing.

17

Additionally, interfaces must accommodate different levels of technical capacities among users.

Complex terminology or unclear layouts can hinder users who are unfamiliar with technical

language or navigation patterns. Accessibility, therefore, implies inclusive designs with specific

language, usability, and graphic guidelines. Other systems that assume advanced digital literacy

may create barriers for users who are already uncertain about managing their finances online.

Financial institutions face internal issues between compliance, operational tasks, and business

goals. Such dilemmas may lead to design solutions that coerce customers, for instance, by using

preselected options or suggestive language. Even subtle cues can affect user behavior in ways that

compromise their voluntary consent. Such practices can erode trust and raise doubts about the

procedure's validity. A good consent interface will balance the need to comply with regulatory

standards and a focus on users’ needs. A lack of both can make consent appear to be a matter of

procedure rather than an informed choice.

Refined, user-centered design will support users’ decision-making and encourage long-term trust.

However, continuous evaluation is necessary, as user expectations and regulations change all the

time. Although this work is ongoing, it offers clear benefits for both users and banks by providing a

simplified and purposeful consent-management experience.

6  User-Centric Design Principles

With the increasing pace of change in digital financial systems, creating a trustworthy experience

is non-negotiable. With respect to banking apps, which people use to store personal information

and take actions with consequences for their lives, a user-centered approach is critical. User

confusion or frustration with a system will compromise its reliability. User-centered design can

make a system function better, safer, and more appealing to work with.

In this chapter, the principles of User-centered design will be discussed in relation to consent in

the design of mobile banking applications. This chapter also describes how these principles form

the design process, elevate empathy, accessibility, and adaptability. User evaluation is essential to

every development cycle, and these principles guide practical decisions throughout the process.

When applied consistently, they support legal compliance, user happiness, and customer loyalty.

They also encourage designers to view consent as a shared responsibility that strengthens users’

autonomy and trust within the banking environment.

18

6.1  Principles of User-Centric Design

User-centered design is a philosophy with a central guiding principle: technology must serve

people. In the financial context, for instance, customers possess sensitive and complex financial

data, which leads them to expect a higher level of service from online banking systems. The impact

of user-centered design is not merely formal; it stands for supportive and fair interactions. This is

an important consideration in consent flows, where a sense of understanding and control is

important. By mirroring reality in their design, such interfaces become more intuitive and less

intimidating while encouraging awareness among all user groups.

Empathy is a founding principle of user-centered design. As a user, you want your goals, concerns,

and pain points understood. Empathy enables designers to anticipate difficult situations, such as

navigating unfamiliar consent screens, and to work toward reducing pressure in these situations.

Empathy does not remove complexity; instead, it creates a context in which a user feels

understood, heard, and comforted.

Accessibility is another critical consideration. Bank customers have diverse backgrounds. They

have different levels of literacy, tech capabilities, and skills. They may be uncertain when

presented with new vocabulary or when required to provide long-term consent. Poorly structured

interfaces aggravate exclusion, further marginalizing already vulnerable people. Those who focus

on accessibility demonstrate a commitment to fair treatment of users, not just to a standard or

regulation.

A clearer consent process relies upon empathy and simplicity. A clearer consent process enables

individuals to understand exactly what they are consenting to and how their information will be

used. Many systems hide this information through vague language or dense text that few people

read. Clear, direct explanations build confidence and reduce confusion. Users tend to respond

positively when they perceive the system as honest.

19

Flexibility is equally essential. User preferences continuously fluctuate, and consent systems

should allow them to grant, accept, or revoke permissions. Some banking applications have not

moved beyond enabling consent decisions to be made only once. They are difficult to return to;

hence, they appear rigid and non-transparent. Efficient systems enable users to review and update

preferences when circumstances change.

With these principles of empathy, accessibility, integrity, and flexibility, a more sophisticated

approach to consent can be achieved in digital banking. With this knowledge in mind, consent

management in digital financial systems will transform a simple procedural requirement into a

representation of customers’ legal rights and expectations. Organizations that respect these

values help users feel recognized, informed, and confident in their actions, therefore contributing

to the ethical and social dimensions of online banking.

6.2  Usability and Accessibility Considerations

Design thinking provides a foundation for creating ethical and user-centric consent experiences.

The conception encourages designers to put themselves in the end user's shoes and to focus on

more than just technical requirements and/or legally worded consent. Design thinking is an

iterative process that involves continuous communication with end-users. This mindset can

benefit the overall digital consent management process and help maintain the balance among fair

treatment, ethical considerations, and legal requirements.

Empathy is the core principle of design thinking. It is not an abstract ideal but a practical approach

to understanding user needs before determining interface structure or policy. Designers can

observe and listen to their users and tap into their discontent, confusion, or hesitations. Consent

screens can sometimes raise doubts or apprehensions among users, especially when they involve

sharing personal information.

Another step is the problem definition. Often, consent dilemmas are couched in terms that focus

too narrowly on consent or on simple agreement, rather than on providing a well-informed choice.

In online banking, for instance, it is not a matter of simply getting an ‘opt-in consent’ but rather

ensuring a meaningful acceptance or denial. A sounder approach avoids solutions that introduce

hidden obstacles.

20

Next comes the ideation phase. Designers develop solution concepts, prototype designs, and

evaluate multiple approaches for representing consent information. The objective is not to

immediately develop a perfect solution but to study various designs and patterns. Prototype

testing can help designers identify which designs appeal to users and which introduce unnecessary

complexity.

Prototyping allows ideas to be worked into a tangible form. Even a minimal prototype or

wireframe can show how people will engage with consent formats. Prototyping can help to

improve text, page designs, and navigation before they are put into production. Where

prototyping is especially helpful is in assessing whether consent language is accurate and relevant,

as well as understanding how well an interface supports or compromises end-user control.

Iteration is where design thinking begins. Consent interfaces require reassessment over time,

considering evolving expectations, technological developments, and legal frameworks. Feedback

from usability studies and user research informs this cycle. Through iterative, observation-focused

processes, organizations can transform consent design into an ethics-driven practice that aligns

with user autonomy.

6.3  Usability and Accessibility Considerations

A key principle of informed consent is usability. A dysfunctional navigation system prevents people

from making educated decisions based on their data. A system with confusing and unreliable

interfaces erodes autonomy and increases frustration, especially with the involvement of financial

information. Financial operations often carry emotional weight, so unclear interactions can quickly

lead to hesitation or withdrawal.

Usability refers to how easily a user can navigate an interface to perform necessary actions, such

as accepting, rejecting, and granting permissions. Text density, technical slang, and unintuitive

menu paths reduce comprehension. Minor elements of an interface, such as button placement,

text, icons, and whitespace, influence where users focus their attention when encountering

consent notification popups. Inconsistencies in these elements can lead to misunderstandings of

the information presented or to the missing important information. Clear text, intuitive flows, and

well-structured content lower cognitive load. These principles also align with regulatory guidance,

which expects consent interfaces to be clear, accessible, and easy to understand (EDPB, 2020).

21

Accessibility can work in alliance with usability. Users possess varying skill levels, experiences, and

limitations. Therefore, a designer must incorporate all these aspects into the interface.

Accessibility in design relates to making text readable, providing good contrast, facilitating screen

readers, enabling keyboard navigation, and providing alternative text. A designer with a vision for

accessibility is not someone who strictly complies with rules and regulations but someone who

dives into issues of equality and justice to help people retain control of their information.

A good thing to keep in mind is context. Often, people access mobile banking apps in stressful and

complicated situations. Here, accessibility functionality can work wonders. Practices such as

providing reassuring feedback, using focus indicators, and designing effective error handling can

help minimize errors. The support for different screen sizes and assistive technologies can be very

helpful in this regard.

User-centered design promotes a culture of fairness and truth. When people are informed of their

choices and can make decisions confidently, they will behave in ways that correspond with their

real intentions. An accessible interface is less presumptuous and less likely to include designs that

mislead users into making unwanted decisions. User-centered design helps build a culture of trust

and provides a solid foundation for a responsible consent model that remains transparent and

empathetic with users in an evolving system.

7  Case Studies and Comparative Analysis

After establishing consent management theory in detail, this chapter will review the studied

concepts in action within existing banking systems. It will examine selected banking interfaces and

the choices they make when designing consent flows. The presented cases are not the subject of

critique or judgment; instead, they illustrate how design decisions affect consent management in

financial systems.

Every situation reveals how consent is organized within these institutions, how it is communicated

transparently, and how users can control their sensitive information. Some banks view consent

through the lens of a long-term relationship, offering customers the opportunity to update their

consent preferences at any time. Other banks practice a minimalist approach to consent, treating

it as a matter of law.

22

The chapter further considers the challenges banks face, including regulatory deadlines, existing

systems, and the cutthroat nature of competitive markets in which they operate. Such pressures

are frequently prioritized over mere design considerations when making interface decisions. Even

for banks with good intentions, opportunities for customer empowerment might be overlooked

due to technical or organizational realities. The case studies include success stories and life

lessons, followed by recommendations in the next chapter.

7.1  Analysis of Existing Banking Application Interfaces

In this section, consent in the interfaces of three banks, namely Barclays, Revolut, and Bank of

America, will be reviewed. The GDPR and other international data protection laws set a minimum

standard for consent but leave the details of its presentation to each organization. Therefore,

banks respond to these standards in different ways, which affects consent management

processes.

Barclays attempted to bring a new method of consent management into a format aligned with

existing systems. During the onboarding phase, a notice appears in a short, layered structure,

rather than in a traditional page-long format. Further along in this interface, consent preferences

become accessible in a ‘Manage app permissions’ option, where users can verify or update their

preferences. While not a radical redesign, this approach begins to recognize the importance of

readability in a system where a flashing novelty is infeasible.

Revolut takes a mobile-first approach and integrates consent into both sign-up and account

settings. The different types of data are presented clearly. Users are not expected to consent to

everything at once; they can return to any settings in "Privacy Preferences." While this system is

simpler, it still provides options for user control. Figure 6.1 illustrates how access permissions are

distributed within this interface.

23

Figure 6.1. Revolut privacy settings show category-based consent controls for marketing,

payments, and analytics

Source: Publicly available application interface screenshot, accessed October 2025.

Bank of America offers a more fragmented experience shaped by U.S. regulations and the bank’s

large technical environment. A user can control permissions for data processing, sharing with third

parties, and marketing targeting, but these settings may change by device and application. Such

inconsistencies can confuse users who expect a stable interaction across platforms. Although the

bank complies with the law, the interface does not always prioritize transparency and

understanding.

Taken together, these examples show that legally sufficient consent does not necessarily make the

experience positive. Language and reversible consent substantially affect consent decisions. A

system that focuses on consent for a function can hinder participation. In contrast, a consent

interface that raises awareness can empower people to make decisions about their own data with

higher confidence.

24

7.2  Case Studies of Successful Consent Management Implementations

In this section, two banks will be considered: ING Spain and Nordea, which take different

approaches to processing consent. In contrast to ING Spain, Nordea will describe consent in

situations where third-party information is accessed. While ING Spain focuses on consent through

improved design and workflows across ING Bank systems, Nordea will describe consent in

situations where third-party access to information occurs. These cases show how practical design

decisions can support understanding and reduce user confusion. In this chapter, interface design

refers to how consent information is organized, displayed, and accessed within an app or website,

and how it helps users identify their options faster.

ING Spain selected Didomi’s Consent Management Platform to consolidate consent across their

online and mobile channels. Figure 6.2 shows how ING Spain’s consent page is delivered via the

Didomi Consent Management Platform. Consent permissions are organized by purpose in a single

interface.

Figure 6.2. ING Spain consent settings implemented through the Didomi Consent Management

Source: Consent platform vendors, accessed October 2025.

25

Prior to this, customers frequently encountered consent prompts with inconsistent terminology.

This inconsistency leads to confusion and redundant actions. With this new interface design

approach, consent messages are presented in a standard format across all channels. Such

standardization eliminates redundancy and improves pattern recognition. Reports from Didomi

indicate higher engagement after the change, suggesting that users better understood the

information when it appeared consistently (Montes, 2024). The implementation is technically

simple but improves usability by reducing cognitive load and maintaining a predictable flow across

devices.

Nordea’s example illustrates authorization flow for third-party data access in an open banking

context, where external services request permission to access a user’s bank data. Open banking

allows third-party services, for instance, budgeting or payment apps, to access bank data with the

user’s permission. These use cases require explicit consent due to the sensitive nature of the

financial data. When a third-party request is made, Nordea redirects the user to its own interface

to confirm or deny access. Figure 6.3 illustrates Nordea’s open-banking consent flow, where third-

party access is authorized within the bank’s native interface.

26

Figure 6.3. Nordea’s open banking identification flow, showing third-party access approval within

the bank’s secure authentication interface

Source: Nordea Open Banking documentation (Nordea Group, n.d.), accessed December 2025

The identification flow occurs within their own applications at banks, not via a service. It implies

that users do not have to assess the credibility of unfamiliar applications in real time. This flow

provides control during high-risk data-sharing actions. As a result, consent is easier to understand

at the exact moment it is given.

Through these examples, it is evident how consent design improves user understanding and trust.

ING improves UX simplicity by standardizing the consent management platform interaction across

all channels. Nordea focuses on control: all third-party requests for access to user data are

authorized in a single interaction screen, ensuring a predictable and secure process. These cases

show that effective consent management does not depend on complex features. Instead, it relies

on a simple interface layout that support conscious decisions of users

27

7.3  Comparative Analysis of Different Consent Management Approaches

Every case study mentioned above, including Revolut, Barclays, Bank of America, ING Spain, and

Nordea, takes a different stance when handling consent. As a matter of fact, this is in line with

their business models, architecture, and environments. Although each organization is guided by

regulations such as GDPR and CCPA, they have different interpretations.

Some banks prioritize usability and user control, while others focus on formal obligations and risk

mitigation. As such, this affects how consent management is handled, where consent is displayed

on-screen, and how accessible the update functionality becomes over time. As a result, consent

can appear either as a clear interaction that supports user understanding or as a background

requirement enclosed in complex settings.

Revolut exemplifies a mobile-first, consent-by-design approach, being highly user-centric

throughout the process. A simple, straightforward approach is presented for each category of

personal information, with a prominent call-to-action button. Users can return to and manage

their consents in "Privacy Preferences" at any time.

This approach minimizes cognitive load by consolidating all permissions in one place and allowing

modifications to be viewed immediately. Figure 6.4 below shows how privacy settings can be

presented in a single view, allowing users to review and adjust their preferences rather than

navigating through a series of screens. As a result, consent is treated as an ongoing interaction

rather than a one-time requirement.

28

Figure 6.4. Revolut’s “Privacy Preferences” provide centralized access to consent settings for

advertising, data sharing, and analytics.

Source: User-captured interface screenshot from publicly accessible sources, accessed October

2025.

This structure shows Revolut’s focus on making things simple and easy to communicate with. This

approach works well for most people but may feel limited for those who want more detailed

explanations or legal references. Revolut prioritizes accessibility over complexity, which improves

the system’s intuitiveness but leaves some information abstract.

While this might be uncommon in personal accounts, Barclays employs the most traditional

approach informed by existing systems. The bank offers a layered privacy structure, but other

activities, such as account settings, remain hidden behind numerous permission prompts.

Although options are available, they are usually obscured by submenus or presented in overly

technical language. Regulatory guidance warns that patterns like this may undermine informed

consent (EDPB, 2022). As a result, the flow feels transactional rather than supportive. Barclays

complies with its legal obligations, but the design reflects the challenges of updating legacy

infrastructure and the tendency of large banking organizations to prioritize risk management over

user engagement. This approach is illustrated in Figure 6.5.

29

Figure 6.5 Barclays push notification settings illustrate a traditional consent interface with dense

explanatory text and limited interaction options.

Source: Barclays Help Center, accessed October 2025.

Bank of America is another example of a system formed under regulatory requirements in a

decentralized technical environment. The application provides consent options for both data

collection and sharing, but this is inconsistent across devices. A customer may be presented with

different consent requests based on the device they are using, which can compromise consistent

behavior across devices. The bank offers a range of options that comply with requirements but do

not lead customers to a substantive level of understanding. These issues were identified in

regulatory guidance on consent clarity and interface framing (EDPB, 2022). At this stage, consent is

reduced to a compliance requirement rather than an essential part of transparent consent

management. This compliance-oriented framing is illustrated in Figure 6.6, where consent is

presented as a single acceptance step combining multiple legal agreements.

30

Figure 6.6. Bank of America consent screen showing a bundled acceptance of multiple legal

disclosures during onboarding.

Source: Bank of America, Mobile Banking Instructions, accessed October 2025.

ING in Spain uses a consent management platform from Didomi that integrates consent across all

mobile, web, and desktop channels. The same messages and choices are presented to customers

on all channels. Moreover, ING can conduct interface tests and measure consumer engagement

with these interfaces. The strategy is straightforward. However, it is largely delegated to an

external platform, which may be less effective in this context.

The Nordea example does not illustrate an ongoing consent workflow but rather a well-secured

authorization with explicit approval to share information. This demonstrates how consent for data

sharing can be presented when relevant. As a result, approval remains within the bank’s

ecosystem, which clearly indicates who is requesting access and what information they are

accessing. Although this model relies on a rigid format with limited personalization, it provides

stability when handling sensitive operations. In this way, Nordea Bank prioritizes security and

stability, whereas Revolut’s system is more adaptable.

31

Taken together, these examples suggest that no one approach works in every case when designing

a consent management system. Effective design depends on how well the approach fits a bank’s

system architecture, regulatory pressures, and user expectations.  Revolut and ING prioritize

access and consistency. Nordea focuses on safety and usability. Examples given by Barclays and

Bank of America illustrate the difficulty of scaling consent in existing, or perhaps more complicated

systems, for more current consent principles. In each of these examples, good communication,

solid structure, and reversible decisions can go a long way in making a good impression.

An efficient consent management design goes beyond adding toggles or checkboxes. It requires

integrating clear data management solutions throughout the user journey to make predictability

and alignment with user-centered values the key priority.

8

Implementation of Consent Management Tool

8.1  User Experience Design of the Consent Management Tool

The project kicked off with a focus on User Experience pain points. The key question was how

people interact with consent in a banking environment and why these moments are often

perceived as confusing or intrusive. Consent is more than a signature; it is an ongoing relationship

with a bank. The goal of this project was to make each step understandable, easy to follow, and

reversible. The goal was to reduce pressure and ensure people felt their choice was honored.

The first stage involved creating a map of typical user flows. For banking apps, critical consent

moments occur during onboarding, the standard transaction cycle, and updates to terms and

conditions. While onboarding remains a critical moment, most applications are guilty of displaying

a series of dense screens full of information, which most users skim and ignore. To address this

issue in the prototype, a series of smaller steps for obtaining consent has been implemented. In

this case, each screen displays a single primary decision with a rationale. While this provides a

moment for reflection, it does not render the process endless. Initial sketch testing indicated a

preference for reading when information is presented in smaller chunks. Figure 7.1 summarizes

the main consent flow implemented in the prototype, from the initial snapshot view to category-

level decisions and confirmation.

32

Figure 7.1. Overview of the consent management flow implemented in the prototype.

Source: Created on Whimsical

Prototyping played a dominant role in influencing design decisions. Low fidelity prototyping

enabled testing of different designs, ranging from a simple list to a more extensive presentation.

User responses suggested a preference for short title descriptions with expandable title links

rather than a series of text descriptions. Icons and dividing lines were added to assist in quickly

categorizing information, such as analytics, personalization, and marketing, which will allow a user

to promptly realize which type of decision they were on the verge of making before delving into

detail. The prototypes are shown in Appendices 1-3 (Figures A1.1-A3.2).

33

Accessibility considerations were incorporated from the beginning. The prototype was tested for

color contrast and font size, and modifications were made accordingly. Interactive elements, such

as buttons and switches, were consistent in size and position, ensuring that users did not have to

learn a new interface at each step. The interface permitted a return to previous views, ensuring

that a user did not become disoriented. Such considerations were important for those who were

not very tech-savvy but needed control over their information.

The detailed consent view is a secondary consideration in consent evaluation and modification.

The page lists major consent categories, provides a simple explanation of their significance, and

shows their status at a given time. As soon as a user modifies a consent setting, the system

provides an immediate response, enabling the user to see the effect of the operation on the

consent setting. Such a system reiterates the idea of dynamic consent and the continuous

recording of this consent over time. The detailed consent view is depicted in Appendix 2 (Figure

A2.1).

Overall, the UX work provided a solid framework for the technical implementation. The interface is

more than a cosmetic overlay; it reflects the system’s state. A MEAN Stack prototype was

developed to achieve this goal. This prototype ensured that each UI interaction had a

corresponding change in the system.

8.2  Designing an AI-Driven Consent Explanation Tool

A common feature in banking apps is a lengthy, static consent notice that makes interaction

difficult. Users will go through these notifications, not because they do not see the relevance of

such information to a privacy matter, but because they find it cumbersome. For this reason, the

project considers an AI-supported explanation tool as a possible future addition to the consent

interface. The tool is not fully implemented in the current prototype and is presented as a design

idea rather than a finished feature. Therefore, a future addition to this consent interface will be an

AI-enabled explanation feature.

34

In this model, each consent notification will include a "Summarize" button that appears clearly on

screen. When clicked, a small message will appear summarizing the implications of this consent.

Such messages will be linked to a consent type and written in plain language. For instance, if a user

declines consent to personalization, this may result in basic account functionality and less

personalized recommendations. The detailed AI consent summary page is shown in Figure A3.1 in

Appendix 3.

The explanation facility can also assist with a basic understanding of usage. A common source of

confusion is how long information is retained and when it may be accessed after consent is

granted. Brief responses to these questions help clarify these doubts, whilst additional detail may

be left to the individual to read. A future development could enable this facility to operate in

tandem with consent, exactly as with all other components of this system.

Ethical matters inform this idea. The information provided will not influence a user's choice, nor

will it obscure trade-offs. Benefits and drawbacks must be clearly articulated. Anonymized usage

interaction data can indicate which consented-to topics confuse users without identifying specific

users. The tool will help users understand their choices.

8.3  Full-Stack Development Approach

The consent management prototype will be built using the MEAN stack: MongoDB, Express.js,

Angular, and Node.js. The selection of MEAN is based on its support for a modular system

architecture, ensuring tight integration between front-end and back-end operations. The authors

of this research paper hope to establish core functionality that can be tested and proven. Future

research work can include AI support.

MongoDB is used as the leading storage solution. Its flexibility enables updating consent

categories and consent histories in a time-stamped manner without requiring frequent migrations.

A consent record includes fields such as a user ID, consent category, status, and a history of prior

status updates, as consent status can change over time. This reflects the idea that consent is

dynamic rather than fixed.

35

A Node.js/Express.js backend provides a RESTful API for generating, reading, updating, and

revoking consent records. Each function validates inputs, verifies authenticated access when

necessary, and creates a record rather than updating an existing one. The strategy ensures that an

auditable trail is generated to assess consent dynamics over time. Although the current project

does not involve a real-world banking system, this setup is intended to serve as a traceable system

that meets regulatory requirements.

The Angular frontend implements consent categories, so they are presented across a set of related

but distinct views. Reusable components handle categories across the list view, detailed view, and

confirmation message. Such a structure promotes consistency in interface designs and reduces the

need for a total restructure when a new category is added. The interface design is based on

guidelines provided in Chapter 5 and usability results.

In this way, the full-stack solution links user actions directly to stored data. While this prototype

runs in a simplified setting, it illustrates how interface events and logic can be coordinated to

enable transparent consent management. Future work in this area may include adding

functionality to this stack, such as logging, integration points, or an explanation tool, as described

above. The focus of implementation is on demonstrating the consent architecture, traceability,

and control, rather than on scaling for production or integration with a banking system.

8.4  Back-End Functionality for Consent Management

The backend is responsible for storing, validating, and exposing user consent decisions in a reliable

way. Its role is to translate simple interface actions into structured, auditable records. To achieve

this, the system must capture each decision in a retrievable format for both user review and

technical checks.

Node.js and Express.js provide the groundwork for routing and application functionality. The API

offers endpoints for granting, updating, and revoking consent. The controllers handle the core

functionality, ensuring that request processing is decoupled from database access. Such a

structure is typical in web application development and, in this case, supports compliance by

enabling each endpoint to be tested and documented.

Validation occurs on every request. Middleware checks that the consent category is known that

the input format is valid, and that required identifiers are present. Each change is stamped with a

timestamp and written as a new record rather than overwriting the previous one. This creates a

simple but effective audit trail. Even if the interface changes later, the underlying history still

shows how decisions were made and updated.

36

The backend model supports partial consent states. For example, a user may allow personalization

within the bank’s systems but block data sharing with external partners. Consent records are

mapped into clear flags that other modules could interpret. Although this project does not

implement complex downstream systems, the structure is ready for future expansions if the tool is

integrated into a larger environment. Security and traceability are built into the design. Access to

detailed logs is restricted, and log data can be protected with hashing or similar measures to

reduce the risk of tampering. Users should be able to request a readable summary of their own

consent history, while institutions can use the same data for audits. The current prototype

implements only the basic elements of this model. Still, the design is prepared for more advanced

features such as expiry reminders or scheduled reviews, where users could be prompted to

confirm whether their previous decisions still reflect their preferences.

8.5  Integration with Existing Banking Systems

This project does not integrate the prototype into a live banking system. However, the design

assumes how such integration could work in practice. Real banking environments consist of many

connected services, including authentication, customer data, transaction processing, and

compliance tools. A consent management service should fit within this landscape without

disrupting critical operations.

One of the primary considerations in integration is identity management. Consent must be linked

to a persistent user identity rather than to a device or a browser session. In a production

implementation, for instance, the consent service would integrate with a bank's central identity

provider and access user IDs via a secure token service. The user would therefore be able to follow

preferences across channels such as mobile, web, and branch.

Data flow is another area that would be especially important. Other systems would need to verify

consent before using personal data for analysis, personalization, or external sharing. In a future

integration, the consent service would expose a simple API to retrieve the relevant flags for a

given user. Systems that lack a mechanism to call the API in real time would receive periodic

exports to update their local rules.

37

Internal visibility can also be controlled. Customer service or compliance officers may need access

to verify whether consent was given, when it was disclosed, and for what purpose. A dashboard

with role-defined access rights can help achieve this without exposing other information. All

access would be logged to support accountability.

Integration would also require a consistent language. If different systems describe the same

consent option in other terms, users will become confused, and trust may erode. Aligning wording

and options across channels is therefore as important as technical integration. While the current

prototype remains independent, the design decisions anticipate these constraints and outline a

path toward a system that can be connected to real banking infrastructure in a controlled and

transparent way.

9  Usability Testing and User Feedback

This chapter will discuss the evaluation of the prototype and how the consent model design was

informed by user feedback. The goal of this stage is to determine whether the consent model is

understandable to users and whether they can easily complete critical tasks without confusion.

The following sections will address the plan for conducting this evaluation, how to develop a

consent model, and the key elements required for understanding.

9.1  Usability Testing Plan

The usability testing primarily involved observing how well participants understood and navigated

the consent management interface. The objective was to identify areas of uncertainty and assess

how well they could make an informed decision. In the first usability test, participants were asked

to complete a series of tasks, including viewing consent categories, updating preferences, and

searching for additional information. They were encouraged to think aloud so that their thought

process could be monitored. Observation during these tests allowed analysts to pinpoint where

they may have paused or skipped information and to request clarification. A follow-up, smaller

usability test was conducted after refining the designs.

38

9.2  Category-Based Consent Overview (First Layer)

The first layer presents consent categories at a higher level. Its purpose is to help users understand

the consent model structure before viewing individual consents. The consent overview screen

shows all data categories in a simple tile layout. Each category has an icon and a short title that

indicates the type of information it contains. This first layer is intended to provide information to

users of the consent structure. When hovering over a category, users can see how the data is

utilized and whether the category is active or inactive. A green badge indicates that all items in a

category are accepted, while a yellow badge indicates that only some consents are accepted. This

high-level view replaces long text blocks commonly found in banking interfaces and provides users

with a clearer understanding of how to navigate the categories. Testing suggested that most users

identified consent areas more quickly with this layout.

9.3  Detailed Consent View (Second Layer)

The second layer provides a more detailed view of consent choices. It allows users to review

individual permissions within each category and adjust them as needed. When users access a

category, the interface expands to display the individual consent items beneath it. Each item has a

short label and a checkbox indicating whether the permission is enabled or disabled. This second

layer provides users with a clearer view of the category's contents. If a category contains both

enabled and disabled items, this partial state is indicated by a yellow badge in the first-layer

overview. Tooltips appear next to each item, explaining what each consent type means and why it

might be important. These tooltips open on a hover and provide brief explanations without forcing

users to read long paragraphs. This layer illustrates gradual disclosure: users first check the state

of a category, then review specific items as needed. Most participants reported that this structure

was clearer than the earlier design, although some technical terms still confused them.

39

9.4  “Smart Summary” AI feature

The consent management tool prototype demonstrates an AI-generated summary of a user’s

selections in plain language. This AI-powered feature consolidates active and inactive categories

into a single, concise message, allowing users to review all their selections without navigating each

category again. The summary highlights the active data types and informs the user which will not

be used if specific categories are inactive. Additionally, it tells them that they can change these

settings at any time through the consent management view. Participants found this summary

helpful to confirm their decisions before saving changes. Some wording may still need

improvement to keep the explanations accurate and easy to read, especially for users who prefer

shorter guidance.

10 Results

This chapter presents the main findings from two rounds of usability testing, focusing on users’

understanding of consent model concepts, points of confusion among participants, and the effects

of design modifications. Additionally, this chapter will identify improvements achieved in the

second round of usability testing and areas that require further improvement.

10.1 User Feedback Analysis (First round of User Studies)

The first testing phase identified several issues with users’ understanding of the navigation. The

main issue was the first consent-management screen. Users were overwhelmed by the lengthy

block of text at the start of the flow. Some participants were adamant that they "never read

consent descriptions in real life and did not do so during testing," which suggests a negative

impact on the user experience. Several participants did not use the explanatory tooltips because

there were no clear visual cues indicating where to hover or tap. Some were unsure how to

navigate the category-based interface because they did not understand where consent items fit

within these categories. A minority of respondents were uncertain about the effects of disabling

specific options for their personal banking.

40

10.2 Iterative Improvements based on User Input

A few parts of the prototype were updated in response to this prototype. The long consent

description was broken into smaller segments to make the information easier to process. This

reduced cognitive load and helped participants focus on one decision at a time. Shorter headers

and simpler category labels were added to make the purpose of each screen more specific. Icons

were added to help participants identify consent types more quickly. Tooltip placement was

adjusted so additional explanations appeared directly beside the relevant area. Some phrasing was

simplified to make definitions clearer while preserving meaning. These adjustments were intended

to reduce friction during the management task and to support users who prefer scanning to

reading long text.

10.3 Observed Improvements and Remaining Gaps (Second round of User Studies)

The second testing phase involved a smaller participant group but showed notable improvements.

Task completion time decreased, and navigation between screens occurred with minimal pauses.

Testers found it easier to follow a shorter sequence of steps and no longer felt lost in the process.

Testers quickly noticed icons in each category, which helped them better understand the intent

behind each permission level. More test participants opened tooltips without prompting, thanks

to improved positioning. However, some matters were left unresolved. One participant remained

unsure about the nature of the payment-related option and whether disabling it would affect

other banking activities. A third participant recommended improving summary information on the

final "consent overview" page. The results have demonstrated that not all consent terminology

and the final stage of consent have yet been optimized. These conclusions support earlier findings

that interface structure significantly affects consent behavior (Nouwens et al., 2020).

10.4 Final Improvements Suggestion

The final section summarizes the remaining issues and proposes areas for further refinement. The

two rounds of testing indicated that the new flow improved clarity; however, several areas still

require attention. Some users continued to struggle with labels in the Payments and Activity

categories. These may require simpler terms or short examples that illustrate how the data is

used. The final “consent overview” also needs more precise descriptions so users can understand

each category’s state without opening it. Further testing with a broader user base would help

confirm whether the changes reduce confusion across different levels of digital experience. Future

work should investigate how long-term use affects trust and willingness to revise consent choices.

These steps would further support informed and confident decision-making.

41

11 Discussion and Conclusion

11.1 Linking Results to Research Questions

The study followed the guidelines presented in Chapter 2 for research questions concerning

consent management, user experience, and legal protocols in digital banking. The first research

question examined how consent is currently used in banking systems and whether this usage

supports an understanding of consent in banking. The research question was answered through

the first usability test. The findings showed that consent management in banking systems often

employed complex legal language, confusing formats, and terms that users did not clearly

understand. This leads to hesitation and doubt during critical decision-making.

The second research question examined how end users perceive and use consent functionality.

The results obtained from both testing phases indicated the benefit of a more transparent

structure and progressive access to information. Having a primary overview organized by

categories, in addition to a detailed lower-level view, helped ensure that end users understood

what they were agreeing to and where they could make modifications. Improving design through

more explicit labeling and tooltips increased end-user confidence in managing their consent

decisions.

The third research question focused on how regulatory requirements can be incorporated into

interface design without undermining control. The results demonstrate that legal compliance does

not require complicated or restrictive interfaces. When consent is presented as a reviewable

process, users feel more in control while the system remains aligned with regulatory expectations.

Together, these findings show that user-centered design can support legal compliance, improve

usability, and strengthen trust when consent management is integrated into everyday banking.

42

11.2 Interpretation of Findings

The results indicate a clearer understanding of consent management among users when

information was presented in concise steps, with headings used to guide navigation. This aligns

with prior conclusions on cognitive load and recognition-driven navigation. Furthermore, it

confirms that congested texts, whether simplified or not, impair interaction with consent

management systems. Although assistance from a category-based design facilitated understanding

of the system’s architectural model, some concepts require more precise definitions. The progress

observed in the second iteration confirms that a minimalist approach to system structure can

significantly improve understanding and confidence in use. These observations support the views

presented in earlier chapters, including intuitive design, progressive disclosure, and control in

design.

11.3 Sustainability Considerations

A well-organized consent flow supports social and digital sustainability by helping users

understand how their data is handled. Clear and intuitive design reduces information gaps and

supports users with different levels of digital competence. A consent workflow with an organized

management system supports social and digital sustainability by providing users with clear

information about data processing. A workflow with an organized consent management system

will be easy to access and understand, helping less tech-savvy users and promoting social

sustainability. Furthermore, this consent workflow, supported by an organized consent

management system, will be updated in the future, contributing to digital sustainability by

addressing all regulatory requirements.

Apart from ethics and social aspects, sustainability also involves a technical angle in this case. As

noted, a consent architecture with a modular design, based on reusable elements and well-

structured data models, can be easily maintained and expanded over time in alignment with

regulations and evolving business needs. Technical sustainability provides a foundation for a

responsible, continuous approach to developing digital banking systems in such instances.

43

11.4 Development Proposals

Future improvements should focus on using explicit technical terms, especially in the “Payments”

and “Activity” categories, as was mentioned in previous chapters. The Consent Overview screen

would benefit from clearer description tooltips to help users be more confident with their choices.

Comprehensive user testing across different age groups and digital skill levels would help assess

whether the design is effective for a broader user group. It may also be helpful to evaluate how

users interact with the consent model over time and whether the “Smart Summary” feature

improves long-term understanding. These steps would help strengthen informed decision-making

in digital banking.

11.5 Conclusion

This study examined how consent management in digital banking can be made more

understandable and controllable from a user’s perspective. A consent management prototype was

designed and implemented using a two-level structure: a category-based consent overview and a

detailed consent view for reviewing and updating individual choices. The prototype was evaluated

through a small survey, two rounds of usability testing, and semi-structured interviews.

The findings show that traditional consent screens, which rely on long legal text and limited

interaction, do not support informed decision-making. Participants tended to ignore or skim this

information and felt unsure about the consequences of their choices. In contrast, the layered

consent interface, shorter explanations, and visible status of consent states helped users orient

themselves and make more deliberate decisions. At the same time, some concepts and categories

still require more precise wording and concrete examples.

The work contributes three primary outcomes. First, it demonstrates a practical consent interface

design that supports reversible decisions, visible status, and gradual disclosure. Second, it provides

empirical evidence that user-centered design principles, such as empathy, accessibility, and

flexibility, can be applied to consent flows without compromising regulatory requirements. Third,

it offers design recommendations for future work, including the potential use of an AI-supported

explanation tool and integration into existing banking infrastructures.

Overall, the study suggests that consent in digital banking need not be a purely formal

requirement. With careful design, it can become a clearer, more approachable part of the user

experience, supporting both legal compliance and long-term trust.

44

45

References

California Consumer Privacy Act of 2018, Cal. Civ. Coda § 1798.100 et sei. (2018).
https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CI
V&title=1.81.5

European Data Protection Board (EDPB). (2020). Guidelines 05/2020 on consent under Regulation
(EU) 2016/679.
https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_202005_consent_en.
pdf

European Data Protection Board (EDPB). (2022). Guidelines 3/2022 on dark patterns in social
media platform interfaces. https://www.edpb.europa.eu/system/files/2022-03/edpb_03-
2022_guidelines_on_dark_patterns_in_social_media_platform_interfaces_en.pdf

Financial Conduct Authority. (2018). Report on a study of how consumers currently consent to
sharing their financial data with a third party https://www.fca.org.uk/panels/consumer-
panel/publication/fscp_report_on_how_consumers_currently_consent_to_share_their_data.pdf

Følstad, A. and Hornbæk, K. (2017). Comparing usability problems and redesign suggestions
elicited with think-aloud and constructive interaction. Human-centric Computing and Information
Sciences. https://hcis-journal.springeropen.com/articles/10.1186/s13673-017-0100-
y?utm_source=chatgpt.com

Gartner. (2024). Market guide for consent and preference management. Gartner, Inc.
https://www.gartner.com/en/documents/5643691

General Data Protection Regulation (GDPR). (2016). Regulation (EU) 2016/679 of the European
Parliament and of the Council. https://eur-lex.europa.eu/eli/reg/2016/679/oj

Kyi, L., Haidl, A., Santos, C., Roesner, F., & Biega, A. (2024). In Proceedings of the CHI Conference
on Human Factors in Computing Systems. https://doi.org/10.1145/3613904.3642260

McKinsey & Company. (2020). The consumer data opportunity and the privacy imperative
https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/the-consumer-data-
opportunity-and-the-privacy-imperative

Montes, Karen. (2024). Unified digital consent: the strategy behind the success of ING Spain.
https://www.didomi.io/blog/ing-spain-case-study

Nordea Group. (n.d.). Open banking authentication and consent flows.
https://documentation.nordeaopenbanking.com

Nouwens, M., Liccardi, I., Veale, M., Karger, D., & Kagal, L. (2020). Dark patterns after the GDPR:
Scraping consent pop-ups and demonstrating their influence
https://doi.org/10.1145/3313831.3376321

46

Ponemon Institute. (2012). The Human Factor in Data Protection.
https://www.ponemon.org/news-updates/blog/security/the-human-factor-in-data-
protection.html

World Economic Forum. (2018). Personal data: The emergence of a new asset class.
https://www.weforum.org/publications/the-appropriate-use-of-customer-data-in-financial-
services/

Yusuff, M. (2023). Ensuring Compliance with GDPR, CCPA, and Other Data Protection Regulations:
Challenges and Best Practices. Federal University of Technology.
https://www.researchgate.net/publication/387224965

Appendices

Appendix 1. Category-Based Consent Overview (Figma)

The figures illustrate how consent categories are grouped and displayed.

47

Figure A1.1. Category-based consent overview presenting high-level consent categories / Figma,
2025

Figure A1.2. High-level consent categories management view / Figma, 2025

Appendix 2. Granular Consent Settings Within a Category

The figures illustrate how detailed consent settings and partially accepted consent categories are
grouped and displayed.

48

Figure A2.1. Detailed consent settings within the Security category / Figma, 2025

Figure A2.2. Category-based consent overview presenting partially accepted Security category /
Figma, 2025

Appendix 3. Consent Summary and Confirmation View

The figures illustrate how the AI-powered consent summary and category-based consent
confirmation message are grouped and displayed.

49

Figure A3.1. AI-powered consent summary / Figma, 2025

Figure A3.2. Category-based consent confirmation view presenting fully accepted categories /
Figma, 2025

Appendix 4. User Questionnaire (Exploratory, n=6)

The figures present the exploratory questionnaire items and corresponding answers collected
prior to usability testing. The questionnaire was used for exploratory input and to guide usability
sessions. Due to the small sample size, the results are descriptive and not generalized.

50

51

52

53

54

Appendix 5. Semi-Structured Interview Topics

The interviews conducted for this study followed a semi-structured format.

55

The discussions were guided by key topics related to the consent management prototype and

participants’ experiences. This approach allowed exploration of relevant pain points raised during

the interviews while ensuring that all sessions covered the same topics.

1.  What are your first impressions of the consent interface?

2.  How clear do you think categories and labels are?

3.  How much control do you feel like having over your consent choices?

4.  Do you understand the consequences of accepting or declining the consent option?

5.  How confident do you feel when making consent decisions?

6.  Please compare this tool with consent experiences in existing digital banking applications.

7.  Any confusion, hesitation, or frustration during interaction? Please, share.

8.  Suggestions for improving clarity, structure, or usability? Please, share.

