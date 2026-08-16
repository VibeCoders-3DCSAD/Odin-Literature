---
conversion_metadata:
  converted_at: "2026-07-21T08:45:47Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Sipila.pdf"
  source_pdf_sha256: "d6104639e59e9d9b5eca8b6a939549730ed84dab8bdfc6b288301a908f4fb3aa"
  page_count: 60
  markdown_char_count: 261659
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Master’s Programme in Computer, Communication and Information Sciences

Proof of concept of centralized personal
finance application

Milla Sipilä

Master’s Thesis
2025

---

<!-- PAGE 2 -->

Author Milla Sipilä

Title Proof of concept of centralized personal finance application

Degree programme Computer, Communication and Information Sciences

Major Algorithms, Logic, and Computation

Supervisor and advisor Arto Hellas

Date 29.6.2025

Number of pages 60

Language English

Abstract
This thesis presents the design and development of a centralized personal finance
management application using the Design Science Research Methodology (DSRM).
The work is based in prior research on financial behavior, planning, and management
tools, explaining how motivation, structured planning, and digital solutions influence
financial well-being. The goal was to address real-world challenges faced by an
individual stakeholder, whose existing financial tracking system relied on fragmented
tools and manual processes. A proof-of-concept (PoC) application was developed
using Flutter, .NET, and MongoDB, including functionalities such as asset tracking,
categorized cash flow visualization, real-time data updates, and financial report
generation. The solution was iteratively designed based on stakeholder’s feedback and
evaluated through task-based testing, structured questionnaires, and comparison to the
baseline system. Results show significant improvements in automation, accuracy, and
usability. While some features, such as authentication and full banking integration,
were out of scope for this PoC, the system provides a strong foundation for further
development and wider applicability in the domain of personal finance management.

Keywords Personal finance, Financial planning, Design Science Research, Proof of
Concept, Personal finance application, Financial tracking, User-centered
design

---

<!-- PAGE 3 -->

Tekijä Milla Sipilä

Työn nimi Keskitetyn henkilökohtaisen rahoitussovelluksen konseptitodistus

Koulutusohjelma Tietotekniikka

Pääaine Algoritmit, Logiikka, ja Laskenta

Työn valvoja ja ohjaaja Arto Hellas

Päivämäärä 29.6.2025

Sivumäärä 60

Kieli englanti

Tiivistelmä
Tämä diplomityö käsittelee keskitetyn henkilökohtaisen taloudenhallintasovelluk-
sen suunnittelua ja kehittämistä hyödyntäen Design Science Research Methodology
(DSRM) -tutkimusmenetelmää. Työn teoreettinen tausta pohjautuu aiempaan kirjalli-
suuteen taloudellisesta käyttäytymisestä, suunnittelusta ja taloudenhallintatyökaluista,
joissa korostuvat motivaatio, suunnitelmallisuus ja digitaaliset ratkaisut taloudellisen
hyvinvoinnin tukena. Työn tavoitteena oli parantaa yksityisen toimijan olemassa olevaa
järjestelmää, joka koostui hajanaisista työkaluista ja manuaalisista prosesseista. Kon-
septitodistus kehitettiin hyödyntäen teknologioita kuten Flutter, .NET ja MongoDB.
Sovellus sisältää toimintoja kuten varallisuuden seuranta, kategorisoitu kassavirta-
analyysi, reaaliaikainen datan päivitys sekä talousraporttien generointi. Ratkaisu
suunniteltiin iteratiivisesti toimijan palautteen perusteella ja arvioitiin tehtäväpoh-
jaisella testauksella, strukturoidulla kyselyllä ja vertailulla aiempaan järjestelmään.
Tulokset osoittavat merkittäviä parannuksia automaatiossa, luotettavuudessa ja käytet-
tävyydessä. Vaikka kaikkia toimintoja, kuten tunnistautumista tai pankki-integraatioita,
ei toteutettu konseptitodistuksessa, sovellus luo vahvan pohjan jatkokehitykselle ja
laajemmalle käytettävyydelle henkilökohtaisen taloudenhallinnan alueella.

Avainsanat Henkilökohtainen talous, Taloussuunnittelu, Kehittämistutkimus,
Konseptitodistus, Henkilökohtaisen talouden sovellus, Talouden
seuranta, Käyttäjälähtöinen suunnittelu

---

<!-- PAGE 4 -->

Contents

Abstract

Abstract (in Finnish)

Contents

Symbols and abbreviations

1

Introduction
1.1 Context and motivation . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Objectives and scope . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Use of artificial intelligence tools . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Thesis structure .

.

.

2 Literature review

2.1 Financial literacy and behaviors
. . . . . . . . . . . . . . . . . . .
2.2 Personal financial planning . . . . . . . . . . . . . . . . . . . . . .
2.3 Personal finance management tools . . . . . . . . . . . . . . . . . .
2.4 Design science research . . . . . . . . . . . . . . . . . . . . . . . .

3 Research methodology
.
3.1 DSRM actions .

.

.

. . . . . . . . . . . . . . . . . . . . . . . . .
3.1.1
Problem identification and motivation . . . . . . . . . . . .
3.1.2 Define the objectives for the solution . . . . . . . . . . . . .
3.1.3 Design and development
. . . . . . . . . . . . . . . . . . .
3.1.4 Demonstration . . . . . . . . . . . . . . . . . . . . . . . .
3.1.5 Evaluation .
. . . . . . . . . . . . . . . . . . . . . . . . .
3.1.6 Communication . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Motivation for DSRM . . . . . . . . . . . . . . . . . . . . . . . . .

4 Problem identification and motivation

4.1 Stakeholder insights from questionnaire . . . . . . . . . . . . . . .
4.1.1 Current financial management approach . . . . . . . . . . .
4.1.2
Frequency of use . . . . . . . . . . . . . . . . . . . . . . .
4.1.3 Challenges with the current system . . . . . . . . . . . . .
4.1.4 Desired features for an improved solution . . . . . . . . . .
Stakeholder reflections . . . . . . . . . . . . . . . . . . . .
4.1.5
. . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . .

4.2 Problem description .
4.3 Motivation .

. .

. .

5 Defining objectives for the solution

5.1 Requirements . .
. . . . . . . . . . . . . . . . . . . . . . . . .
5.2 Prioritized objectives . . . . . . . . . . . . . . . . . . . . . . . . .

.

.

4

2

3

4

6

7
7
8
8
9

10
10
11
13
15

18
18
18
19
19
20
21
22
23

24
24
24
24
24
25
25
25
26

28
28
30

---

<!-- PAGE 5 -->

6 Design and development

6.1 Architectural decisions . . . . . . . . . . . . . . . . . . . . . . . .
6.2 System architecture .
. . . . . . . . . . . . . . . . . . . . . . . . .
Implementation details . . . . . . . . . . . . . . . . . . . . . . . .
6.3
6.3.1 Data model and domain objects
. . . . . . . . . . . . . . .
6.3.2 User interface structure and design approach . . . . . . . .
6.3.3 Development tools and process . . . . . . . . . . . . . . . .

7 Demonstration

7.1 Addressing complexity and human error . . . . . . . . . . . . . . .
7.2 Solving scalability limitations
. . . . . . . . . . . . . . . . . . . .
7.3 Automating financial data retrieval . . . . . . . . . . . . . . . . . .
7.4 Centralized tracking across categories . . . . . . . . . . . . . . . .
Integrated and efficient reporting . . . . . . . . . . . . . . . . . . .
7.5

8 Evaluation

8.1 Task-based user testing . . . . . . . . . . . . . . . . . . . . . . . .
8.2 Stakeholder insights from questionnaire . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . .
Feature satisfaction . . . . . . . . . . . . . . . . . . . . . .
Problem-solving impact
. . . . . . . . . . . . . . . . . . .
Suggestions and future improvements . . . . . . . . . . . .
8.3 Comparison to baseline . . . . . . . . . . . . . . . . . . . . . . . .
8.4 Evaluation against design objectives . . . . . . . . . . . . . . . . .

8.2.1 General impressions
8.2.2
8.2.3
8.2.4

9 Discussion

9.1 Summary of results and impact . . . . . . . . . . . . . . . . . . . .
9.2 Limitations of the solution . . . . . . . . . . . . . . . . . . . . . .
9.3 Reflection on DSRM . . . . . . . . . . . . . . . . . . . . . . . . .
9.4 Opportunities for future development . . . . . . . . . . . . . . . . .

10 Conclusions

References

32
32
34
35
35
36
37

38
38
40
41
43
45

48
48
49
49
49
50
50
50
51

54
54
55
56
57

58

59

5

---

<!-- PAGE 6 -->

Symbols and abbreviations

Application Programming Interface
Database
Design Science
Design Science Research

Abbreviations
API
DB
DS
DSR
DSRM Design Science Research Methodology
FR
PFM
PoC
QA
STD
UI
UX

Functional Requirement
Personal Finance Management
Proof-of-concept
Quality Attribute
Self-Determination Theory
User Interface
User Experience

6

---

<!-- PAGE 7 -->

1 Introduction

1.1 Context and motivation

Peter Drucker said, "If you can’t measure it, you can’t manage it" highlighting the
importance of data in decision-making. Hamming’s quote, "You get what you measure"
represents how we guide ourselves with measuring the steps we take toward achieving
our goals. W. Edwards Deming presented the saying "In God we trust, all others
bring data" which is a reminder that we should base our decisions off data and not
assumptive beliefs.

This holds true for Personal Finance Management (PFM) which requires financial
literacy, motivation and structured planning to make informed financial decisions.
Studies suggest that people with higher rates of financial literacy are more likely to
participate in types of behaviors related to saving, investing, and avoiding unnecessary
financial mistakes (Lusardi and Mitchell 2014; Rajesh and Giridhar 2024).
In
addition, global surveys suggest that lower rates of financial literacy remain in many
demographics, particularly young adults, women, and among lower income or education
levels (Atkinson and Messy 2012; Lusardi and Mitchell 2014).

Financial knowledge alone is not enough to create behavioral change. Di Domenico
et al. (2022) explains that autonomous motivation, driven by internal values and
interest, is more strongly associated with sustainable financial habits and well-being
than controlled motivation which relates to external pressure or guilt. Furthermore,
Kaye et al. (2014) has shown that financial management behaviors are driven by
emotional, social and experiential motivations, not just rational knowledge. Shafiee
et al. (2024) suggests that well-designed, personalized financial tools can increase
financial literacy and support decision-making, while still fulfilling an educational
and advisory role.

While digital PFM tools aim to help users track expenses, manage budgets, and
visualize financial data, their adoption remains limited. Stefanov et al. (2024) found
that only few available tools were able to meet all consumer needs for easier financial
management, especially in underrepresented regions. In addition, many tools only
offer one service to the users, such as budgeting, and do not provide educational content
which would help raise trust to financial services (Torno et al. 2021). Research has
shown that adding personalization, gamified feedback, and simplified interactions can
improve user engagement and financial self-efficacy (Bitrián et al. 2021; Cederberg
2013), yet these elements are still uncommon in mainstream applications.

This thesis responds to these limitations by designing a centralized personal finance
application that consolidates financial data, supports user learning and motivation,
and offers tools for financial planning and analysis.

---

<!-- PAGE 8 -->

1.2 Objectives and scope

The goal of this study is to design and build a proof-of-concept of centralized
personal finance application that helps individuals make informed, data-driven financial
decisions. Following the Design Science Research Methodology (DSRM), the study
aims to identify user needs, create a customized solution, and evaluate its practical
relevance and functionality. The application was developed for a private stakeholder
with real-life requirements.

In particular, the application aims to achieve:

• Consolidation of financial data across asset classes including cash, shares and

real estate from multiple sources on a single platform

• Track a user’s net worth development over time through visualized data

• Provide clear visual overviews of transactions and cash flow through tables and

charts

• Improve transparency and accessibility by structuring personal financial data in

a scalable, easy-to-navigate system

• Provide breakdowns of the assets by categories and subcategories including

market value, equity, country attribution and more

This work contributes to the development of practical PFM tools by focusing on data
integration, visual clarity, and actionable insights. It also demonstrates the application
of DSRM to guide artifact development and iteration based on stakeholder’s feedback
and evaluation.

1.3 Use of artificial intelligence tools

Artificial intelligence tools, including ChatGPT, were used to support the structuring
and writing of this thesis. AI assistance was first used to help outline the overall
structure of the thesis and deciding what content should be included in each chapter and
section. Once the structure was in place, AI was used to help draft some paragraphs
based on predefined ideas, bullet points, and notes.

In the Literature review (Chapter 2), the process involved first highlighting and
collecting relevant information from selected academic sources. The material was
manually organized into clearly defined subsections. AI tools were then used to help
compose coherent and logically structured paragraphs, ensuring that the collected
sources were presented under the appropriate themes and headings.

Additionally, AI was used throughout the thesis to check that statements were
supported by the cited literature and to refine clarity, grammar, and academic tone. All
AI-assisted content was reviewed, edited, and finalized to ensure accuracy, integrity,

8

---

<!-- PAGE 9 -->

and appropriateness for academic work.

1.4 Thesis structure

This thesis consists of ten chapters. Chapter 1 introduces the research context,
motivation, and objectives. Chapter 2 reviews relevant literature on financial literacy,
personal finance planning, management tools, and DSRM. Chapter 3 presents the
research methodology. Chapters 4 to 8 follow the DSRM process: identifying the
problem, defining solution objectives, designing and developing the proof-of-concept,
demonstrating its use, and evaluating its effectiveness. Chapter 9 discusses the broader
impact of the results and future development opportunities. Chapter 10 concludes the
thesis by summarizing key findings and reflecting on the research outcomes.

9

---

<!-- PAGE 10 -->

2 Literature review

This chapter provides the theoretical background for the research by investigating the
three topics relevant to the development of a centralized personal finance application.
First, it looks into financial literacy and behavior, focusing how knowledge, motivation,
and habits shape financial outcomes. Second, it looks into personal financial planning
as a structured process aimed at achieving financial goals through budgeting, saving,
and investing. Third, it looks into current state of personal finance management tools,
highlighting current capabilities, user needs, and design opportunities. Finally, the
chapter explains Design Science Research Methodology (DSRM), tracing its origins,
artifact types, and structured research process, which forms the methodological base
of this thesis.

2.1 Financial literacy and behaviors

Financial literacy is essential for managing money, making informed decisions, and
achieving long-term financial well-being. Rajesh and Giridhar (2024) argue that
low levels of financial literacy can lead to significant consequences related to the
accumulation of overall wealth, such as unsustainable levels of debt, poor credit, and
possibly even bankruptcy. Many people struggle with financial management, such
as, overspending, making poor investment decisions, borrowing too much money
unnecessarily, and failing to plan for retirement. They note that increased financial
literacy allows individuals to have better saving and spending routines, control their debt
better, and achieve improved financial strength. Likewise, Lusardi and Mitchell (2014)
confirm that low levels of financial literacy are present in all populations, particularly
the elderly and youth. They say that all populations show major gaps in certain areas,
such as, issues understanding interest rates, inflation, or risk diversification. They
state that historically, people relied on government-managed pensions and paid little
attention to financial planning which does not apply today anymore. The authors point
out the connection between financial illiteracy and riskier behaviors such as late bill
payments or excessive interest credit usage. In contrast, financially literate individuals
report more planning for retirement and long-term wealth accumulation.

From the behavior side, Atkinson and Messy (2012) note that financial literacy
incorporates attitudes and habits that can lead to financial well-being. Their inter-
national survey concluded that people with better financial knowledge also display
better behaviors including budgeting, saving and timely bill payment. Individuals
exposed toward longer-term planning are also likely to adopt healthier behaviors in
their financial practices. The research demonstrated notable demographic findings:
women scored lower than men on both the knowledge and behavior component, and
middle-aged individuals generally outperformed the younger and older age groups.
Financial literacy and education were highly correlated, but low-income individuals
sometimes showed resistance to outside guidance.

Complementing these findings, Kaye et al. (2014) illustrates that personal finance

10

---

<!-- PAGE 11 -->

behavior is not simply a logical process. Rather, the emotional, culture, and relational
contexts of how people manage money influences financial behaviors. Instead of
a complete, structured picture of their finances, individuals tend to piece together
financial insights through more informal practices, such as only glancing the balance
in their account or skimming last week’s transactions. This suggests a disconnect
between how financial literacy is typically supported and how people actually prefer to
engage with their finances. The findings show the importance of designing financial
tools that reflect real-life behaviors and habits, and also recognizing that financial
decision-making is deeply shaped by individual context and lived experience (Kaye
et al. 2014).

Motivation is another aspect to note. Di Domenico et al.

(2022) apply Self-
Determination Theory framework to reflect on how autonomous, controlled, and
amotivated motivation relates to financial knowledge and outcomes. Research demon-
strated that individuals who are autonomous, i.e. people who engaged in financial tasks
willingly, showed better financial knowledge, self-efficacy, and well-being. While,
amotivated individuals, i.e. people lacking interest or feel they cannot manage their
finances, were more likely to overspend and reported having lower levels of financial
confidence. While both autonomous and controlled motivation were show to correlate
with saving and investing, only autonomous motivation had a clear association with
positive financial outcomes further mitigating the importance of internal motivation
and supportive financial behaviors.

Finally, Lasmiatun (2024) examined how financial education shaped Generation
Z’s financial awareness and habits. The study found that the understanding and ability
of young adults to manage money, strategically plan, and invest was higher for those
who participated in the financial education. Although, the understanding of financial
competency primarily came from informal learning on social media and things like
blogs, instead of formal sources. Lasmiatun (2024) said that participants valued digital
content that is presented in an interactive and visual format (infographic, videos,
interactive simulations) as they found the smaller chunks of information and visuals
easier to engage with and understand. This suggests that improving financial education
for Generation Z may require integrating more accessible, digital formats that align
with their learning habits and media consumption (Lasmiatun 2024).

2.2 Personal financial planning

Personal financial planning is a lifelong process designed to maximize the use of
income and assets, meet financial goals, and reduce uncertainty. Siegel and Yacht
(2009) describe this as analogous to planning in other areas: knowing where you are,
knowing where you want to go, and figuring out how to get there. They go on to note
that there are many interrelated variables and the uncertainty of life can complicate the
planning process. Since personal circumstances and the economy change over time,
financial planning has to be sufficiently flexible to deal with change while pursuing
life-long goals. Financial planning involves continually reassessing goals, considering

11

---

<!-- PAGE 12 -->

alternatives and deciding if changes need to be made (Siegel and Yacht 2009).

In building on this idea, Gitman et al.

(2011) note that financial planning is
increasingly important given the context of a world in which we cannot expect
employer or government support to guarantee long-term security. They describe
financial planning as a systematic effort to organize a financial plan for personal
goals/values. Their financial planning model has six basic steps: (1) identify and define
financial goals (2) develop financial strategies (3) implement financial strategies (4)
create and maintain budgets (5) evaluate results using financial statements (6) revise
financial plans due to changes in personal circumstances, or unexpected challenges.
While success is not guaranteed, consistent and flexible financial planning can improve
the likelihood of success in achieving financial security and adapting to the unexpected
(Gitman et al. 2011). Huang (2016) states that financial planning is an important
skill integrated into daily life, regardless of how much financial considerations affect
people in their daily decisions, such as costs being affected by interest rates, increases
in annual tuition and others. This is especially important for young people, and college
graduates, experiencing independence in an expensive world with low income for
the first time. Huang (2016) acknowledged that while some people follow structured
paths, and others adopt a more reactive method, financial planning is necessary for
eventual success. Similar to Gitman et al. (2011), she also divided the process to
six steps: (1) Identifying Smart Financial Goals, (2) Know Your Current Financial
Situations, (3) Spending Wisely with a Budget, (4) Managing the Credit, (5) Saving
for the Future and (6) Investing the Money.

In the Malaysian context, Lai and Tan (2009) investigated how individuals engage
with different areas of financial planning. The results indicated that while budgeting
and investment planning is relatively well pursued, financial planning across other
areas like insurance, retirement, and estate planning are often disregarded. Specifically,
10% of respondents remarked that they planned across all areas of personal finance.
Despite this, there are generally positive attitudes toward budgeting and money, with
the conscious recognition of the importance of investment for long term financial
security. However, there were less positive attitudes towards retirement, as results
indicated greater consideration on health and lifestyle changes. In addition, Lai and
Tan (2009) examined job status in financial planning. Findings indicated that employed
and self-employed individuals engaged in financial planning more than those without
stable income, highlighting that job status has an impact on planning behaviors.

Shah and Bhatt (2014) studied income allocation and investment behavior among
residents of the city of Ahmedabad, in the district of Gujarat. Findings indicated that
individuals typically allocate 45% of income to consumption, saving 25%, and 15%
to investments and emergency funds, with saving priorities of their children’s needs,
housing, and to save taxes. In addition, respondents expressed that their preferred
investments are fixed deposits with banks, insurance plans, and public provident funds.
Regarding investment behaviors, male respondents certainly favored investing in stock
markets, while female respondents tended to prefer gold, bullion, and PPF investment

12

---

<!-- PAGE 13 -->

products respectively. The above trends may reflect a cautious and security based
financial planning behavior focused on meeting long term needs and awareness of
investment risk (Shah and Bhatt 2014).

2.3 Personal finance management tools

Personal finance management (PFM) applications have changed from being paper-
and-pencil or spreadsheet-based systems, to being advanced web or mobile tools. As
Gafrikova et al. (2015) demonstrate, although using traditional paper-and-pencil, or
spreadsheet, methods offers maximized freedom, the downside is greater technical skill
and time commitment. Gafrikova et al. (2015) traced back that dedicated PFM software
started appearing in the 1980’s, and has since progressed into today’s specialized
web and mobile tools, many of which are now integrated into banking systems. A
key milestone was the launch of Mint.com in 2007, which set a global benchmark for
online PFM tools. Despite this, adoption has remained low. Citing a 2012 Aite Group
survey they estimate 58% of U.S. consumers have never used and do not plan to use
PFM applications, and only 13% of them wanted financial consulting and planning
from their financial institutions. In Poland, PFM tools embedded within banks are
relatively common but often limited to intra-bank account management, although with
higher security standards.

Stefanov et al. (2024) presented a user-centered design approach for developing a
mobile PFM app focusing on the Bulgarian context, where no PFM solutions currently
exist. In interviews and survey responses conducted by Stefanov et al. (2024), they
identified practices on how the users wanted to manage their finances: budgeting,
monitored expenses, investment planning, and strategy planning. They say that many
existing tools fall short due to overly complex interfaces or lack of accessibility. Based
on their analysis, they identified some desired functionalities: portable calculator,
currency converter, chart extraction, and barcode scanning, all bundled onto a single
platform to enhance user experience and effective personal finance management.
The significance of design and usability is also verified by Cederberg (2013), who
researched the PFM features young users preferred when embedded in banking apps.
She conducted user interviews and prototype testing with their target market while
they used the PFM functionalities. Features that the respondents liked included
general income and spending diagrams, category-based pie charts, budget tracking
with monthly limits, alerts for nearing those limits, and visual planning of fixed
expenses. Users identified a desire for easy-to-use applications and preferred minimal
manual input with automated categorization features. Users also noted aesthetics were
important as they wanted a pleasing and recognizable user interface, as they believed
these types of tools would help them more effectively manage their finances due to
new insight, control, and goal setting.

Looking at broader range of tools, Torno et al. (2021) did a taxonomy and cluster
analysis on 170 PFM apps, finding ten separate archetypes. The clusters ranged
from apps focused on financial news and asset monitoring, to advanced and manual

13

---

<!-- PAGE 14 -->

budgeting tools, to full-featured mobile banking platforms. Most apps required internet
access and user accounts and generally, offline functionality was limited to apps that
have a basic calculator and manual budgeting possibilities. Very few apps provide an
advisory or educational element in their service. Within the clusters, examples such
as "Investing with Advice" offer predictive analysis and products while others (e.g.,
"Transaction Authorisation") are narrower in scope. Despite the wide functionality
spectrum, Torno et al. (2021) highlight a lack of educational content across most
apps, suggesting a missed opportunity for financial service providers to improve user
engagement and trust through better financial literacy tools.

Herrala et al. (2023) explore how PFM systems can both empower and constrain
young users, using empathy-based storytelling (MEBS) as a qualitative research
method with 191 university students. Participants had significant positive experiences:
improved budgeting ability, improved savings and investing practices, and better access
to lending and digital transactions, all factors that contribute to personal agency and
long-term planning. There were also significant negative experiences: spontaneous
spending, difficulty grasping the value of digital money, and over-indebtedness due
to ease of credit. Other concerns included stress regarding privacy, surveillance,
cybersecurity, overload on information, and over-reliance on technology and digital
competence. The study concludes that while PFM tools can promote financial well-
being, they may also reinforce behavioral control and cognitive overload when not
appropriately designed or supported.

Gamification might offer a partial way around these problems. Bitrián et al.
(2021) investigate how gamified features promote user motivation by combining
self-determination theory (SDT) with the technology acceptance model (TAM). They
evaluated 208 Mint app users and conclude that budgeting, alerts, credit score and
tracking opportunities are features that promote competence and autonomy. These
feature sets encouraged users’ motivation to use the app and resulted in strong perceived
usefulness and ease-of-use. Bitrián et al. (2021) suggest independent goal setting,
visual display of progress and budgets, real time notifications/alerts, and rewards are
elements that app designers can introduce to improve user autonomy and competence.
The recommended aspects for both the app designer and user suggest the potential for
long-term engagement and a sense of empowerment for the user.

In continuing with a generational perspective, Handayani et al. (2024) described
fintech adoption from a millennial perspective since they grew up with technology as
a normal way to interact with the world. They examined millennials attitudes toward
technology-based financial services and distributed an online survey to 120 users of
personal finance apps. The authors felt that personal finance apps helped provide
visibility by enabling users to see their income, expenses, and balances in real-time
that supported their ability to track their spending behaviour, set their goals, and plan
their finances. They presented key features that were seen as motivating factors such
as automatic expence tracking, bill reminders, and personalized advice. Concerns
about data security and privacy on online platforms did still exist. Fintech applications

14

---

<!-- PAGE 15 -->

have become central to millennials’ financial behavior, and their growing usage is
pushing traditional financial institutions to adapt and integrate similar technologies to
stay competitive (Handayani et al. 2024).

Finally, French et al. (2021) evaluate four PFM apps developed collaboratively with
credit unions and tested via a randomized controlled trial with 500 members of Derry
Credit Union in Northern Ireland where 260 were in the treatment group and 240 in
the control group. The treatment group showed small, significant increases in financial
literacy, ability to budget, confidence to budget, and ability to plan for unexpected
bills. The treatment group did not show significant increases to digital literacy or
behavioural change (i.e., saving money regularly).
In terms of use, expectable,
descriptive analysis showed that 45% of users used the apps regularly (5 or more
times), 32% used the app infrequently, and 23% did not use the app. For the non-user
reasons included forgetfulness, relevance, and restrictiveness. Still, most users rated
the apps positively, indicating strong potential if future designs can address barriers to
usage and engagement.

In summary, the effectiveness of PFM tools lies not only in their technical capabilities
but also in their ability to support user behavior, motivation, and emotional well-being.
Integrated and user-friendly tools that address privacy concerns, offer personalized
insights, and engage users in meaningful way are most likely to foster long-term
financial stability and inclusion.

2.4 Design science research

De Sordi (2021) describes Design Science Research Methodology (DSRM) as an
approach emerged in the early 2000s to provide a more structured, scientific basis for
the development of information systems. Essentially, DSRM aims to solve real-world
problems through designing artifacts in a systematic way. Vaishnavi and Kuechler
(2015) notes that design is more than simply describing and they define design as
purposeful creation of new artifacts, where an artifact can take many forms and types.
They say that a design is a routine in a situation when you have enough knowledge to
create without the need to develop or extend knowledge, versus a design being labeled
innovative when it manifests any form of new knowledge. They continue that the
subject of Design Science (DS) is focused on the concepts and processes followed to
produce artifacts which comprise constructs, models, methods, and instantiations. This
then comprises the practical forms of knowledge needed to solve particular functional
needs. Conversely, Design Science Research (DSR) focuses on the scientific study of
the design process including analysis, reflection, abstraction, and evaluation. Vaishnavi
and Kuechler (2015) explain that DSR contributes to knowledge by investigating and
documenting how artifacts have evolved through DSRI and how artifacts achieve their
intended use function within contexts.

De Sordi (2021) also describes the difference between natural science, which
develops knowledge to examine either physical or abstract phenomena that already

15

---

<!-- PAGE 16 -->

exist, and artificial science, which develops knowledge based in context to develop
the creation of human artifacts that aim to solve problems for human populations.
According to De Sordi (2021), one defining characteristic of artificial science is a focus
on attempting to understand the context of the artifact, in terms of the environment
in which will be used or the individual human characteristics and needs that may
impact the use of the artifact. As referenced by De Sordi (2021, p. 9), “Design
involves designing something that is a solution to a need, which are called artifacts.”
Artifacts developed using DSRM can take many forms. Vaishnavi and Kuechler
(2015) define constructs, as the concepts and terms to describe problems and solutions,
which may actually evolve in the research. Models are organized representation
of the relationships among constructs, which may be useful not perfectly accurate.
Methods are the procedures, algorithms, or techniques used to accomplish desired
ends. Instantiations are artifact constructs, models, or methods used in practice, which
may occur prior to theory being formed (Vaishnavi and Kuechler 2015).

Among the various process models proposed for conducting design science research,
the most widely adopted is from Peffers et al. (2007), presented in Figure 1. Their
model was developed to address the lack of structure in early DSR efforts and has since
become a foundational framework in information systems research. It has a structured
six-step process: (1) problem identification and motivation, (2) define objectives for a
solution, (3) design and development of the artifact, (4) demonstration of the artifact
in use, (5) evaluation of the artifact’s performance, and (6) communication of research
results. This structured process will form the methodological basis of this thesis, and
is further explained in Chapter 3.

Figure 1: Design Science Process Model (Peffers et al., 2007, p. 54)

In addition to structure and guidelines, DSR also requires an understanding of what
a valid contribution means. According to Hevner et al. (2004), design science in
information systems requires the replication of artifacts that are not only novel and
effective, but also, that have been evaluated objectively in the context of use. The
authors provide a balance to the effective usability versus research methodological

16

---

<!-- PAGE 17 -->

rigor by claiming utility as the artifact’s valued contribution. In another words, the
artifact’s reasonable way to address a usable problem. The balance between topical
relevance and rigor of method is one of the strengths of design science research,
and makes DSRM particularly relevant in applied contexts, such as personal finance
technology.

In conclusion, DSRM provide a method to theoretically shape a practical solution to
complex problems using iterative artifact development. DSRM encourages including
feedback from users, as well as contextual constraints, and formal evaluation. These
elements contribute to appropriateness of applying DSRM to develop a more engaging
central personal finance application, presented in this thesis.

17

---

<!-- PAGE 18 -->

3 Research methodology

This chapter describes the research methodology used in this thesis, which follows the
Design Science Research Methodology (DSRM). The chapter explains how each of
the six DSRM phases has been utilized within the scope of this study, from problem
identification to communicating results. In addition, the last section provides the
justification for why DSRM was selected as the methodology for this thesis.

3.1 DSRM actions

This thesis follows the DSRM proposed by Peffers et al. (2007), which consists of
six structured steps for developing and evaluating innovative artifacts. Each step is
described in detail below.

3.1.1 Problem identification and motivation

The first step of DSRM, Problem Identification and Motivation, focuses on defining a
research-worthy problem that holds both academic significance and practical relevance
(Peffers et al. 2007). As De Sordi (2021) explains, this requires direct engagement with
the field to ensure that the identified challenge reflects real user needs and contextual
constraints.

Usability, lack of features, and low demand have all been identified as the most
significant limitations facing personal financial management (PFM). Torno et al.
(2021) discover that the majority of mobile PFM apps focus on narrow tasks, such as
keeping a budget or facilitating payments, and rarely include educational content or
consider incorporating holistic financial planning. Herrala et al. (2023) illustrate that
while PFM tools can empower users and place them in control of their financial lives,
they also run the risk of generating user stress, impulsive behaviors, and create a sense
of surveillance.

To validate the problem in this study, a structured questionnaire was conducted with
the stakeholder (Table 1), using open-ended questions to investigate challenges and
feature gaps. The analysis of the final problem definition is presented in Chapter 4.

Problem identification questionnaire
Q1: How do you currently manage personal finances?
Q2: How often do you use the current solution?
Q3: What different purposes do you use it for?
Q4: What is the most challenging aspect of using the current solution?
Q5: Are there any missing features or functionalities you wish existed?
Q6: How often do you encounter errors, delays, or inconsistencies?
Q7: How would you rate the user experience (UX) and ease of use?

Table 1: Questions used in the problem identification questionnaire

18

---

<!-- PAGE 19 -->

3.1.2 Define the objectives for the solution

The second step of DSRM, Define Objectives for the Solution, involves setting goals
that respond directly to the identified problem, while ensuring they are feasible and
relevant (Peffers et al. 2007). Objectives can be both quantitative, such as measurable
improvements, and qualitative, such as addressing user frustrations or unmet needs. As
De Sordi (2021) notes, this stage includes assessing the current state of the problem,
reviewing existing tools, and identifying how the proposed artifact can offer a suitable
solution.

To formalize the solution scope, the system requirements were divided into functional
and non-functional categories. Functional requirements define what the system should
do, such as authentication, data processing, and reporting, while non-functional
requirements specify how the system should perform, including its reliability, security,
and responsiveness (Ironhack 2024). This structure helps ensure the artifact meets
both usability expectations and technical standards.

To focus development on the most critical features, a prioritization of the require-
ments was conducted with the stakeholder. The MoSCoW method (Brush 2023), a
common approach in Agile development, was adapted to suit the project context. The
customized scale, shown in Table 2, includes four levels: Must have, Should have,
Nice to have, and Optional.

Prioritization
Must have
Should have
Nice to have
Optional

Description
Mandatory in the final product
Essential but not absolutely vital
Useful additions, but not necessary
Could be added later

Table 2: Custom prioritization scale for the context case

This customized ranking allowed the stakeholder to distinguish core features from
those better suited for future iterations. Requirements were labeled as functional
requirements (FR) or quality attributes (QA), and numbered by priority, with lower
numbers indicating higher importance. The requirements are presented in detail in
Chapter 5.

3.1.3 Design and development

The third step of DSRM, Design and Development, involves specifying the system
architecture and core functionality, followed by the implementation of the artifact
(Peffers et al. 2007). According to De Sordi (2021), this phase is iterative and includes
ongoing development and evaluation to ensure that the artifact effectively addresses the
defined problem. Continuous refinement based on stakeholder feedback is encouraged
to enhance both functionality and relevance.

19

---

<!-- PAGE 20 -->

Architectural decisions were made based on the prioritized requirements. Enstrom
(2018) defines Architectural Decisions (ADs) as significant, documented choices that
influence the system’s structure, including software technologies, data integration,
and maintainability strategies. These decisions are distinct from routine design details
and serve to align the system with long-term goals and constraints (Enstrom 2018).
The key ADs for this project are presented in Chapter 6.

After defining the architecture, the artifact was developed in iterative cycles.
Feedback from the stakeholder was used to refine features, user workflows, and
interface elements. This is motivated from the findings from literature as both Stefanov
et al. (2024) and Cederberg (2013) noted the importance of usability, simplified and
inviting interface, and centralized functionality.

3.1.4 Demonstration

The fourth step of DSRM, Demonstration, involves showing that the developed artifact
can solve at least one instance of the identified problem (Peffers et al. 2007). This
may involve experimentation, simulations, case studies, or other forms of proof.
As described by De Sordi (2021), this phase aims to validate whether the artifact’s
structure, procedures, and outputs address the problem in a meaningful way, even
if full performance optimization has not yet been achieved. De Sordi (2021) also
notes that demonstration is sometimes incorrectly reported as evaluation in academic
studies, especially when the artifact is still in development.

In this thesis, demonstration was used to show how the artifact addresses key issues
identified during stakeholder analysis. These included fragmented tools, repetitive
manual updates, and limited trust in the accuracy of financial data. These same
challenges were also noted in the literature. Gafrikova et al. (2015) mentions that
spreadsheet-based solutions require time and technical skills. Cederberg (2013) found
that users might stop using the tool if it requires too much manual input, encouraging
automation. Additionally, Herrala et al. (2023) found that financial tools perceived as
unreliable or difficult to use may increase user stress and undermine their sense of
control.

The demonstration presents the following capabilities of the system:

• Addressing complexity and reducing human error

• Solving scalability limitations

• Automating financial data retrieval

• Providing centralized tracking across financial categories

• Delivering integrated and efficient reporting

20

---

<!-- PAGE 21 -->

3.1.5 Evaluation

The fifth step of DSRM, Evaluation, assesses how well the artifact solves the identified
problem by comparing its intended objectives with the actual outcomes (Peffers et al.
2007). This step involves analyzing the artifact’s performance, usability, and functional
alignment with user needs. Evaluation is important for determining whether the artifact
works as intended in reality. De Sordi (2021) explain that there are artificial evaluations
occurring under isolated or theoretical conditions, and naturalistic evaluations that
occur within real environments, with real users, and real problems. Naturalistic
evaluations are aligned with the fundamental principles of design science, particularly
in applied domains.

In this study, the artifact was evaluated using four different methods. First, task-based
user testing was conducted to assess usability and alignment with expected workflows.
The stakeholder performed typical usage scenarios independently on their own device
while being observed. This allowed for direct feedback on task completion, design
effectiveness, and interface clarity. The scenarios are listed in Table 3.

User testing tasks
T1: Add a new transaction for every asset category and review updated
net worth
T2: View and interpret asset distribution using pie charts and asset tables
T3: Add an expense and income and review the updated cash flow
visualization
T4: Generate a financial report for the past three months

Table 3: Task-based user testing

Following the test session, the stakeholder completed a structured evaluation
questionnaire in similar format as in problem identification. The questions were
grouped into four categories: general impressions, feature satisfaction, problem-
solving, and suggestions for improvement (Table 4).

21

---

<!-- PAGE 22 -->

Evaluation questionnaire
General impressions
How intuitive did you find the application interface?
Was it easy to find and use the key features you needed?
Feature satisfaction
How satisfied are you with the asset tracking functionality?
How satisfied are you with the cash flow tracking functionality?
Do you feel the visualizations (charts, tables) are helpful and informative?
How useful is the PDF report generation compared to your previous
manual process?
Problem solving
To what extent has this solution reduced manual work compared to your
old system?
Do you feel this solution helps you avoid errors or inconsistencies?
Has your confidence in your financial data improved?
Suggestions and improvements
Is there anything missing you would expect in a full solution?
What would you improve in future versions?

Table 4: Questions used in the evaluation questionnaire

In addition to collecting qualitative feedback, the evaluation included a comparison
with the stakeholder’s baseline system. This helped identify gains in automation,
usability, and reporting quality. Finally, an analytical review was performed by
checking how well the implemented solution satisfied the original design objectives
from earlier DSRM stages. The evaluation results are presented in Chapter 7.

3.1.6 Communication

The sixth and final step of DSRM, Communication, focuses on sharing the research
outcomes with both academic and professional audiences. According to Peffers et al.
(2007, p. 92), “Communicate the problem and its importance, the artifact, its utility
and novelty, the rigor of its design, and its effectiveness to researchers and other
relevant audiences, such as practicing professionals, when appropriate.” De Sordi
(2021) highlights that effective communication in DSR must be tailored to its audience.
He says that for practitioners, the emphasis is on the artifact’s purpose and practical
utility. For researchers, the focus is on presenting the design process, structure, and
evaluation outcomes to ensure methodological rigor and reproducibility (De Sordi
2021).

This thesis represents the communication phase of the DSRM process. It documents
all stages of the research, beginning with problem identification and continuing
through design, development, demonstration, and evaluation. The aim is to present
the motivation for the work, the rigor of its execution, and its contribution to both

22

---

<!-- PAGE 23 -->

research and practice. By clearly articulating the methodology and results, this thesis
contributes to ongoing discussions about the design of personal finance tools and the
practical application of DSRM to real-world challenges.

3.2 Motivation for DSRM

DSRM is well suited for this thesis due to its structured and iterative process for
developing and evaluating artifacts that address real-world problems. This study aims
to create a proof-of-concept (PoC) of personal finance management application that
fulfills a stakeholder’s specific needs by using automation and data integration to
provide better financial insight. DSRM provides an organized and systematic approach
as an avenue to develop, validate and refine such an artifact ensuring its effectiveness
and relevance in practice. This was also pointed by Torno et al. (2021) who stated that
design science research is a promising practice to develop innovative IT artifacts.

The methodology is specifically intended for research where the goal is to construct
and evaluate artifacts that extend existing solutions or introduce new functionality
(Peffers et al. 2007). As Hevner et al. (2004) explains, design science research is
most effective when artifacts are developed in response to clearly defined business
needs and evaluated within real-world contexts. This aligns with the aims of this
thesis, which addresses limitations in current financial tracking tools such as manual
spreadsheets that lack scalability, automation, and integration. Through DSRM, these
limitations can be systematically addressed using an iterative development process.
The six-phase structure provides a transparent development roadmap, making it easier
to track progress and validate design decisions.

DSRM differs from purely theoretical approaches by including demonstration and
practical evaluation. Because this project involves a real stakeholder with specific
financial tracking needs, the methodology supports continuous engagement to ensure
that the resulting solution meets actual user expectations. As noted by De Sordi (2021),
practitioner involvement strengthens both academic rigor and real-world applicability.
The evaluation phase allows the artifact to be assessed against predefined objectives
and revised if necessary. Since the goal of the thesis is to develop a PoC rather
than a production system, DSRM also allows for design flexibility and exploration of
feasibility without requiring full deployment. In particular, the Demonstration phase
enables targeted testing of core functionality in a controlled setting, helping confirm
the solution’s effectiveness before further development (Peffers et al. 2007; Hevner
et al. 2004).

23

---

<!-- PAGE 24 -->

4 Problem identification and motivation

This chapter presents the problem description that the proof-of-concept application
aims to address. It begins with insights gathered from a structured questionnaire
conducted with the stakeholder, followed by a detailed description of the current
financial management approach and its associated challenges. Finally, the chapter
explains the motivation for developing a new solution, based on the limitations and
problems identified in the existing system.

4.1 Stakeholder insights from questionnaire

To gain a deeper understanding of the problem, a structured questionnaire was
conducted with the stakeholder, as introduced in Chapter 3.1.1. Several challenges
were found from the financial management approach based on the responses.

4.1.1 Current financial management approach

The stakeholder uses multiple financial tools to track income, expenses, and invest-
ments. Their process includes:

• Tools used: A combination of Spendee (for expense tracking), multiple bank
accounts across two countries, Google Sheets (for share price and exchange rate
tracking), and several Excel spreadsheets for real estate and mortgage tracking.

• Manual data entry: Financial data is periodically fetched from various sources

and consolidated into a “master” Excel file, in use since 2014.

• Financial reporting: Quarterly and yearly reports are generated manually by

analyzing data and producing graphs.

4.1.2 Frequency of use

The stakeholder engages with the financial system at varying intervals:

• Daily: Tracking expenses in Spendee.

• Weekly: Updating and maintaining Excel files.

• Quarterly: Conducting a full financial review and generating reports.

4.1.3 Challenges with the current system

The stakeholder identified the following major issues:

• Complexity and human error: The system has become difficult to maintain and

prone to mistakes.

24

---

<!-- PAGE 25 -->

• Scalability limitations: Excel structures struggle to handle growing financial

data needs.

• Lack of automation: No integration with online sources and updates must be

done manually.

• Reporting inefficiencies: The quarterly report process is time-consuming and

fragmented.

4.1.4 Desired features for an improved solution

The stakeholder expressed the need for:

• More automation: A system that tracks key metrics with minimal manual effort.

• Better data integration: Automatic synchronization with sources like stock

prices, exchange rates, and banks.

• A centralized platform: A single system combining all financial aspects.

• Enhanced accuracy: Reduced human error and more reliable data.

4.1.5 Stakeholder reflections

The stakeholder summarized their concerns as follows: "The whole process is getting
overly complex, resulting in a higher probability of human error impacting data
quality. Any changes made to the document might break something due to complex
dependencies across different data tabs."

Although they find Excel somewhat enjoyable and familiar, they acknowledge the
system is not user-friendly for others and is increasingly difficult to manage. As
they put it: "For me, it is somewhat of a relaxing experience, but it is starting to
feel overwhelming because of the inaccuracies and gaps that hinder me from getting
accurate data."

4.2 Problem description

The stakeholder has tracked income, expenses, and investments for over a decade using
a combination of spreadsheets, financial applications, and manual data collection. Over
time, this system evolved to support detailed financial analysis, including quarterly
and yearly reporting. However, as financial data has grown in volume and complexity,
maintaining the system has become increasingly difficult.

The current setup involves multiple tools: Spendee for expense tracking, bank
accounts across two countries, and Excel spreadsheets for managing real estate
investments, mortgages, and stock portfolios. These fragmented sources require

25

---

<!-- PAGE 26 -->

manual consolidation into a “master” Excel file. Data must be periodically fetched,
entered, and processed by hand, resulting in a time-consuming workflow that is
increasingly prone to error due to complex interdependencies across formulas and
sheets.

The main challenges of the existing system include:

• Scalability limitations – Excel struggles to accommodate the increasing volume

and complexity of financial data.

• High risk of error – Manual updates to stock prices, exchange rates, and

balances introduce inconsistencies and inaccuracies.

• Lack of automation – No integration with online financial data sources requires

frequent copy-paste operations and manual data entry.

• Inefficient reporting – Quarterly reporting involves multiple manual steps:
collecting data, updating formulas, generating charts, and compiling summaries.

The stakeholder is very sophisticated in their financial management, but as their
system complexity and fragmentation grow, inefficiencies and the risk of error has
increased. As many of the authors note, working with disparate tools or manual
processes creates usability issues, deters engagement, and leads to errors in financial
decision-making (Gafrikova et al. 2015; Torno et al. 2021; Stefanov et al. 2024).
Research also shows that even knowledgeable users cannot maintain their desired
financial behaviours (or make decisions) when the available tools do not simplify
their decision-making or provide timely feedback related to their current financial
goals (Atkinson and Messy 2012; Kaye et al. 2014; Cederberg 2013). This behaviour
supports the concepts of integrated ease of use, automation, real-time data, and
supporting feedback loops toward the establishment of habits, all of which were also
requested by user participants in the most recent fintech and PFM adoption studies
(Bitrián et al. 2021; Handayani et al. 2024)

4.3 Motivation

The stakeholder’s difficulties represent a wider demand for personal finance tools that
combine automation, accuracy, and usability. Their current system allows them to
track all aspects of their finances in great detail, though, it is becoming more and more
difficult to sustain, as well as requiring scaling. The stakeholder has not considered
commercial tools, because the stakeholder believe their needs to be really specific,
they would be unable to find an off-the-shelf product that fulfilled their needs. It is
noted by Stefanov et al. (2024), that the absence of localized tools (e.g. applications
in Bulgarian) could also lead to unmet expectations for users in certain regions. Torno
et al. (2021) also note that most personal finance applications tend to focus on a single
function (budgeting versus payments) than being a solution for everything, and as
such, users often need to resort to some other method, for example use of spreadsheets.

26

---

<!-- PAGE 27 -->

Besides missing features, many existing tools do not offer a complete solution and
force users to manage their finances across several separate apps. While automation
was recognized as a major priority, the stakeholder also indicated that accuracy
and completeness are critical aspects of their financial data. They said that without
these, they may not justify the expense of moving to another system in the future.
This viewpoint is aligned with Cederberg (2013), who found that users would often
abandon tools that required excessive manual effort even if they provided some level
of automation or tracking.

An improved solution should address the following key needs:

• Automated financial data retrieval to eliminate repetitive manual updates.

• Centralized tracking of financial data across multiple accounts and investment

platforms.

• Integrated analytics and reporting to generate insights with minimal user inter-

vention.

• Enhanced accuracy and reliability to reduce the risk of calculation errors.

The motivation for this research is based on creating a scalable personal finance
system that can improve data reliability, reduce manual effort, and allow individuals to
make informed decisions. These priorities match the recommendations in the literature
for creating tools that not only automate and do financial tasks, but can motivate users,
give feedback, and support the financial goals of the user (Bitrián et al. 2021; Shafiee
et al. 2024). While some studies also mention potential stress or overreliance on
digital systems, they note the importance of user-centered and emotionally supportive
design (Herrala et al. 2023).

27

---

<!-- PAGE 28 -->

5 Defining objectives for the solution

This chapter defines the objectives of the proposed solution based on the problem
analysis and stakeholder needs presented in Chapter 4. It presents both functional
and non-functional requirements that guide the development of the proof-of-concept
application. These requirements are then prioritized to ensure that the most critical
features are addressed.

5.1 Requirements

The following requirements are intended to resolve the major problems and motivations
explained in Chapter 4. These requirements reflect user needs and incorporate some of
best practices in software development and PFM design. The requirements are related
to practices mentioned in the literature where fragmented and manual systems have
been shown to be inefficient and create cognitive burden and low usability (Gafrikova
et al. 2015; Herrala et al. 2023). In contrast, research also highlights that effective
personal finance tools build long-term engagement by providing automated features,
availability, ease of use, and tools to create engagement and maintain motivation
(Bitrián et al. 2021; Cederberg 2013).

The requirements are divided into two main categories: functional and non-
functional. Tables 5 and 6 present a summary of each, including descriptions, user
stories, and acceptance criteria that define when the requirement is considered fulfilled.

The functional requirements focus on features that support an understanding
of financial visibility, decision making, and operational efficiency. For example,
dashboards, tags, and reporting features. These features were requested by the
stakeholder, and research also suggests that clear goal-oriented feedback increases
engagement and personal oversight (Shafiee et al. 2024).

Functional require-
ment
Present real-time cap-
ital information

User interface (Desk-
top and mobile)

Data visualization of
capital and statistics

User story

Acceptance

"As a user, I want to see the
real-time value of all my as-
sets."

"As a user, I want to be able to
add/update/view my financial
data from mobile and desk-
top."
"As a user, I want to see how
my assets are growing in a way
that supports me in making
financial decisions."

The system fetches up-to-date
stock prices and displays the
real-time value of all tracked
assets.
The application provides a re-
sponsive user interface that
works on both desktop and
mobile devices.
The application displays inter-
active visualizations, such as
charts and tables, represent-
ing asset growth and financial
trends.

28

---

<!-- PAGE 29 -->

Functional require-
ment
Manual financial data
input

Automatic data fetch-
ing

Tagging

Financial report gen-
eration

Customizable dash-
boards

Choose currency

User story

Acceptance

"As a user, I want to be able
to add/modify/delete income,
expenses, and different assets
through the application or im-
port them from a file."
"As a user, I want my income,
transactions, and
expenses,
different assets to be fetched
automatically from the bank
and brokers that I use."
"As a user, I want to be able to
divide my assets into different
categories and subcategories."
"As a user, I want to receive
on-demand financial reports
(weekly/monthly) summariz-
ing my income, expenses, and
asset growth."
"As a user, I want to customize
the widgets on my dashboard
to suit my financial goals"

"As a user, I want to be able to
choose the currency I want to
use for data visualization and
analytics."

Users can manually input and
manage financial records and
import data via supported file
formats.

The system integrates with ex-
ternal APIs or services to au-
tomatically retrieve user finan-
cial data.

Users can assign, edit, and
view custom categories and
subcategories for each asset.
Users can generate and view
downloadable reports summa-
rizing key financial metrics
over a selected time range.

Users can add, remove, and
rearrange dashboard elements
such as charts, summaries, and
alerts.
Users can select a preferred
display currency, and the sys-
tem automatically converts
values using current exchange
rates.

Table 5: Functional requirements

The non-functional requirements address factors such as trust, reliability, and
responsiveness which are important factors for user adoption and continued engagement.
Herrala et al. (2023) noted that technical issues, user errors and concerns about data
security resulted in increased stress and lower rates of user engagement. Handayani et
al. (2024) identified privacy and information security as major concerns for millennial
users.

29

---

<!-- PAGE 30 -->

Category

Data protection
and security

Non-Functional
requirement
Prevent unau-
thorized parties
from accessing
data.

Reliability

The statistics
provided by the
system should be
correct.

Performance

Good response
time

User story

Acceptance

“As a user, I want
my personal data
to be safe and not
get into the wrong
hands.”
“As an application
owner, I want to
protect customer
and business data
from unauthorized
access.”
“As a user, I need to
trust the calculation
and analytics given
by the system.”

“As a user, I want
the system to pro-
cess my actions,
such as updating
assets and fetching
reports, quickly.”

All user data is iso-
lated and accessible
only to the authenti-
cated user. External
access is restricted
via secure authenti-
cation and authoriza-
tion mechanisms.

The system produces
correct financial
analytics with an
accuracy rate of at
least 99.99% when
validated against
sample data.
95% of user requests
are processed within
1 second under nor-
mal operating condi-
tions.

Table 6: Non-Functional requirements

5.2 Prioritized objectives

After the requirements for the proof-of-concept application were defined, they were
prioritized together with the stakeholder, as described in Section 3.1.2. The prioritized
list is presented in Table 7, including a short description, associated goal, and priority
level for each requirement.

Label
FR-01

FR-02

Description
User interface (Desktop
and mobile)

Data visualization of
capital and statistics

Goal
Ensure the application has a
responsive and intuitive inter-
face usable across devices.
Provide interactive and clear
visualizations to help users
analyze financial perfor-
mance.

Priority
Must have

Must have

30

---

<!-- PAGE 31 -->

Label
FR-03

Description
Tagging

QA-01

FR-04

FR-05

QA-02

The statistics provided
by the system must be
correct

Present real-time capital
information

Financial report genera-
tion

Prevent unauthorized
parties from accessing
data

FR-06

Automatic data fetching

FR-07

Choose currency

FR-08

FR-09

Customizable dash-
boards

Manual financial data
input

QA-03

Good response time

Goal
Allow users to organize fi-
nancial data using custom
categories and tags.
Ensure that all system-
generated statistics and
analytics are accurate and
reliable.
Display up-to-date values of
all user assets using real-time
data sources.
Generate reports that sum-
marize financial metrics for
selected periods.
Secure all user data and pre-
vent unauthorized access
through authentication and
encryption.
Integrate with financial APIs
to import transaction and
asset data automatically.
Allow users to choose their
preferred display currency
and apply real-time conver-
sion.
Let users tailor their dash-
boards with widgets for per-
sonalized financial tracking.
Support manual entry for
transactions and assets when
automation is unavailable.
Ensure fast and responsive
interaction for common user
actions.

Priority
Must have

Must have

Should have

Should have

Should have

Nice to have

Nice to have

Nice to have

Optional

Optional

Table 7: Prioritized requirements

31

---

<!-- PAGE 32 -->

6 Design and development

The chapter provides the technical basis for the proof-of-concept application. The
chapter presents the major design decisions, system architecture, and implementa-
tion details that were used to meet the functional and non-functional requirements
described in the previous chapter. The focus was on designing a modular, scalable
and maintainable system that met stakeholder requirements while facilitating rapid
development under the scope of a PoC.

6.1 Architectural decisions

Based on the prioritized functional requirements (FR) and quality attributes (QA)
presented in Chapter 5, key architectural decisions were made to support the most
critical goals for the system. The focus was placed on addressing the “Must have” and
“Should have” requirements. Since this is a proof-of-concept (PoC) application, the
architecture is intentionally simplified to focus feasibility, core functionality, and rapid
development while minimizing unnecessary complexity. The architectural decisions
are presented in Table 8, along with their justifications and corresponding requirement
links.

The technical design reflects both stakeholder needs and recommendations from the
literature on PFM tools. Previous studies indicated the importance of centralization
and modularity for facilitating sustained usage and continued engagement (Gafrikova
et al. 2015; Torno et al. 2021). Similarly, usability and reliability were important
factors. Cederberg (2013) noted the need for an intuitive user interface and automated
categorization to minimize user effort, while Herrala et al. (2023) recognized that
technical complexity and user error may lead to stress and lower user trust. The
decision to create a cross platform UI, and modular back end is meant to promote
flexibility and scalability. Additionally, features like visual analytics and automation
were chosen based on findings that they enhance user motivation and promote clearer
financial understanding (Shafiee et al. 2024; Cederberg 2013).

Short
description
User
interface

Decision

Justification

Requirement

- Use Flutter for a
cross-platform UI
(mobile and desktop).
- Implement a basic
responsive UI.

- Flutter allows quick UI
iteration with a single
code base.
- Responsive UI ensures
usability across devices.

FR-01

32

---

<!-- PAGE 33 -->

Requirement
Link
FR-01,
QA-02

FR-03,
FR-06,
QA-01

FR-02

FR-04,
FR-06

FR-07

FR-08

FR-09

Decision

Justification

Short
description
Backend
services

Database

Data visual-
ization

Automatic
data fetching

- Use ASP.NET Core
Web API for backend
logic (C#).
- Implement RESTful
API for data flow.
- Use MongoDB.Driver
for data access.
- Separate frontend and
backend into modular
components.

- Use MongoDB for
storing financial data,
tags, and transactions.
- Define collections for
structured data storage.
- Use chart libraries and
built in tables in Flutter
for financial data
visualization.
- Use Google Sheet API
to fetch share prices.
- Implement scheduled
jobs to fetch and store
data.

Multi-
currency
support

Customizable
dashboards

Manual
financial
data input

- Store all financial data
in a base currency (e.g.,
USD/EUR).
- Fetch exchange rates
from HexaRate API.
- Store dashboard layouts
in MongoDB as JSON
documents.
- Use Flutter’s
Drag-and-Drop Widgets.
- Use different forms to
input different
transactions manually.
- Make tables editable.
- Support CSV imports.

33

- ASP.NET Core is
performant, scalable, and
aligns with developer
expertise.
- Using MongoDB.Driver
ensures compatibility and
flexibility with
MongoDB data models.
- Modular architecture
supports maintainability
and future scaling.
- Flexible schema allows
adapting to evolving
financial data.

- Charts and tables help
users analyze financial
trends effectively.

- Google Sheet
integration ensures
real-time financial
updates with no costs.
- Scheduled jobs
automate data retrieval.
- Storing data in a base
currency avoids
unnecessary conversions.
- Dynamic conversion
provides user flexibility.
- JSON storage enables
flexible UI customization.
- Drag-and-Drop UI
enhances usability.

- Enables easy data input
when integrations might
not be available.
- CSV import reduces
manual workload for bulk
data entry.

---

<!-- PAGE 34 -->

Short
description
Performance
optimiza-
tion

Decision

Justification

- Reduces response times
and improves scalability.

- Optimize API and DB
queries with indexing and
caching.
- Use providers in UI and
only call API when
something is updated.

Requirement
Link
QA-03

Table 8: Architectural decisions and their linkage to requirements

6.2 System architecture

The high-level system architecture is shown in Figure 2. The system consists of three
core components aligned with the architectural decisions discussed in the previous
section: the user interface, the backend API, and the data storage layer. Additionally
the two integrations are presented in the picture: stock prices and exchange rates.

The user interface is developed using Flutter and Dart to support cross-platform
deployment across mobile and web platforms. It handles user interactions, such as
adding or editing transactions, and visualizes financial data through interactive charts
and tables. While WinUI was initially considered for the front end, it was eventually
let go due to its limited visualization capabilities and its restriction to the Windows
desktop environment.

Figure 2: High-level system architecture diagram

The backend API is implemented in C# using the .NET framework. It contains
the core business logic of the application, including transaction handling (shares,

34

---

<!-- PAGE 35 -->

cash, and real estate), statistical computations, and communication with external data
sources. The API is also responsible for all interactions with the database, including
data storage, updates, and retrieval. While this design does not scale far in production
environment where there is more traffic, the code is structured in a way that would
allow separation to microservices later on.

MongoDB is used as the NoSQL database due to its flexibility in managing diverse
financial data. It stores all the data models, including transactions, asset details (shares,
real estate, and cash), cash flow (income and expenses), and daily net worth snapshots.

To enrich the application with current market data, two external integrations are
included. For stock prices, the system uses a Google Sheets integration powered by
Google Finance. Real-time prices are retrieved via the Google Sheets API based on
ticker symbols, with data refreshed each time the application is opened or modified.
Although this solution requires some manual setup by users, it was selected due to the
high cost and limited availability of commercial stock APIs.

Currency exchange rates are fetched from the HexaRate API. To improve efficiency,
exchange rates are retrieved once per day and cached in the database for reuse, ensuring
up-to-date conversion data with minimal external requests.

6.3 Implementation details

6.3.1 Data model and domain objects

The application’s data model is designed to reflect the financial domain and support
core functionalities such as asset tracking, income and expense monitoring, and net
worth calculation. A NoSQL, document-based approach is used, with each domain
object stored in a separate MongoDB collection. The main collections and their roles
are described below:

• ShareTransaction, CashTransaction, RealEstateTransaction: These collec-
tions store raw transaction data entered by users. Each record includes metadata
such as transaction date, amount, and relevant domain-specific fields such as
purchase price or loan amount for real estate. These transactions form the base
for calculating asset values.

• Share, Cash, RealEstate: These collections represent the user’s current asset
state. They are computed dynamically from transaction history. For example,
the Share collection aggregates holdings per ticker symbol, calculating total
quantity and current market value.

• CashFlowTransaction: This collection tracks income and expense activity.
Each entry includes the transaction type (income or expense), category, amount,
currency, and optional notes. This enables budget tracking, category breakdowns,
and monthly expense summaries.

35

---

<!-- PAGE 36 -->

• NetWorthSnapShot: This collection stores daily snapshots of the user’s total
net worth. Whenever assets are modified, for example, through a new or updated
transaction, the system either creates or updates the snapshot for that date. These
records support historical net worth tracking and trend visualization.

• ExchangeRate: This collection stores daily currency exchange rates retrieved
from the HexaRate API. Rates are fetched once per day and cached to reduce
external requests. All financial data are normalized to a base currency (e.g.,
EUR or USD) using these stored rates.

This modular data model supports a flexible and extensible architecture, enabling
new features to be added with minimal disruption to existing components. The backend
API follows a structured design pattern in which each domain feature is managed
through a dedicated Controller–Logic pair, promoting a clear separation between
request handling and business logic. This pattern also enables possible later separation
to their own microservices to increase scalability.

6.3.2 User interface structure and design approach

The user interface is implemented in Flutter using a modular, screen-based architecture.
Each primary functionality, such as the dashboard, asset management, transaction
input, and cash flow tracking, is encapsulated in a dedicated screen. These screens
are composed of reusable UI components, including editable tables, input forms,
pie charts, and bar graphs. All components are located in the widgets/ folder and
access application data through state management provided by the provider package.
The interface updates reactively in response to changes in the underlying data layer,
ensuring synchronization between the data model and the rendered views.

Financial visualizations are built using the fl_chart library, supporting different
diagrams such as line, bar, and pie charts. These provide users with immediate visual
feedback on financial distributions and trends. As noted by Bitrián et al. (2021), visual
progress indicators and dashboards can improve user motivation and purposefulness.
To support responsive layouts, Flutter’s layout tools, such as Expanded, Flexible,
and LayoutBuilder, are used alongside maximum width constraints to optimize the
interface for large screens. While the current design primarily targets desktop and
web resolutions, the use of Flutter enables future mobile support with minimal code
changes.

The UI design focuses clarity and ease of data entry. Structured forms are provided
for each transaction type, and editable tables enable efficient bulk modifications.
Usability and data integrity are further improved through features such as real-time
form validation, dropdown menus, and multi-select checkboxes. This emphasis on
visual feedback and structured input aligns with design recommendations for PFM
tools, which stress that reducing manual effort and simplifying interactions encourages
continued engagement and reduces user stress. Cederberg (2013) highlights that young

36

---

<!-- PAGE 37 -->

users value tools that have inviting interface, automated categorization, and minimized
input complexity, while Herrala et al. (2023) caution that systems perceived as difficult
or unreliable can increase cognitive load and undermine trust.

6.3.3 Development tools and process

A range of modern tools were utilized during the PoC development. Backend services
were developed using Microsoft Visual Studio Community 2022, while the Flutter-
based frontend was implemented in Visual Studio Code. MongoDB Compass was used
to inspect and manage database documents during development. Version control was
handled using Git, enabling structured branching, change tracking, and safe iteration.

Generative AI tools were used to support the development process by assisting with
code scaffolding, debugging suggestions, and exploration of architectural patterns.
These tools were particularly helpful in accelerating UI layout design in Flutter,
formulating MongoDB queries, and structuring backend logic in .NET. However, their
role was strictly supportive: all code was manually reviewed, adapted, and integrated
to meet the project’s specific requirements.

An iterative development approach was followed, including regular feedback from
the stakeholder. The functionality was implemented in modular units. For example,
share management and its related transactions were treated as a single feature set.
Each feature typically followed a consistent workflow: beginning with UI design,
followed by data contract definition, backend logic and API endpoint creation, database
integration, and finally frontend-backend connection. After each feature reached a
working state, time was allocated for refactoring and fine-tuning before proceeding to
the next set of features. This incremental approach supported rapid prototyping while
allowing flexibility to respond to evolving requirements throughout the development
phase. Iterative development with stakeholder feedback is also recommended in DSR
literature. Hevner et al. (2004) stated that iteration and implementation are central
pieces to this research as it increases the quality of the end product and helps address
problems along the way.

37

---

<!-- PAGE 38 -->

7 Demonstration

This chapter describes a practical demonstration of the proof-of-concept application.
The goal is to demonstrate how the implemented system solves the main problems
in the stakeholder’s financial management process. The demonstration will follow a
structure of the most important issues and how the proposed solution addresses these.

7.1 Addressing complexity and human error

A major challenge with the stakeholder’s current system is its complexity and vul-
nerability to human error, caused by the use of multiple spreadsheets and manual
calculations across various financial sources. The PoC application mitigates these
issues by consolidating all financial data into a single, structured backend supported
by well-defined logic and calculations.

Each financial domain (shares, cash, and real estate) is handled by a dedicated logic
class in the backend, following a consistent Controller–Logic design pattern. This
separation ensures that each logic class is responsible for domain-specific operations
such as asset aggregation, transaction handling, and profit calculation. For example,
the ShareLogic class compiles a user’s holdings based on transaction history and
computes key metrics, including:

• Total invested amount

• Current market value (based on the latest prices)

• Profit or loss in absolute terms

• Profit or loss as a percentage

These calculations are performed automatically on the server side, using the user’s
base currency and up-to-date exchange rates and share prices. The results are returned
to the frontend as part of the asset model, eliminating the need for spreadsheet-based
formulas or manual input. Similar logic applies to cash and real estate assets, with
real estate computations taking into account the purchase price and loan amount.

By encapsulating business logic in code, the system delivers consistent and reliable
results, significantly reducing the risk of errors caused by user input, broken formulas,
or accidental modifications. Centralized logic also simplifies future updates as any
change to calculation rules, such as profit formulas or exchange rate handling, can be
applied system-wide from a single source.

The frontend presents these results visually and interactively. On the Dashboard
page, shares are displayed in a doughnut chart (Figure 3), while the Assets and
Transactions page shows detailed asset data in editable tables (Figure 4).

38

---

<!-- PAGE 39 -->

Figure 3: User’s shares presented in an interactive doughnut chart

Figure 4: User’s assets presented in editable tables with summary statistics

39

---

<!-- PAGE 40 -->

Automating complex calculations and reducing manual workflows increases ease
of use. This is consistent with research that suggests users are more likely to engage
with systems with low effort and clear feedback. Cederberg (2013) found that young
users preferred financial tools that required less manual input, included automated
categorization, and improved visual clarity which further empowered them to manage
their finances better and encouraged continued use. Likewise, Herrala et al. (2023)
identified that by making financial tasks easier to complete, user stress was reduced,
and sense of control increased.

7.2 Solving scalability limitations

The stakeholder’s previous system, based on Excel spreadsheets, had scalability
limitations as the financial data volume increased. Over time, the growing number
of transactions, investment types, and calculated fields made the system fragile
and difficult to scale. Complex dependencies between formulas and worksheets
created a risk where even minor changes could disrupt the entire setup. The PoC
application addresses these challenges through a service-oriented architecture and a
document-based database model.

Financial data is stored in MongoDB collections, which are convenient for evolving
data structures. This enables the system to handle increasing volumes of transactions
and assets without requiring strict schemas or manual reconfiguration. The backend
is implemented as a stateless ASP.NET Core Web API, which supports horizontal
scalability. While this PoC is not intended for production deployment, the underlying
architecture allows for future containerization and cloud-based scaling.

The PoC has removed the traditional limitations of Excel, such as worksheet size,
formula depth, and fragile cross-sheet dependencies giving a basis for scalability over
time, data reliability, and consistent performance, as the financial data grows. In
addition to greater data volumes, the application supports more complex data models
that are more structured, more object-oriented than traditional spreadsheets. This
could include things like real estate records that could have fields for loan amount,
terms of mortgage payments, and all of the payment history, or share transactions
that could track dividends, market pricing, and country attribution. It is difficult to
model the level of detail in Excel and to maintain its reliability. This limitation is also
observed in studies of PFM tools, where traditional systems relying on manual entry
and static formats often struggle to support growing data needs and complex financial
contexts (Gafrikova et al. 2015).

One example of improved scalability is the automated net worth tracking feature.
Previously, the stakeholder manually gathered asset values from various sources and
combined them to update a dataset for visualization. In contrast, the PoC system
calculates net worth automatically whenever any asset is modified and can also generate
historical values retrospectively (see Figure 5).

40

---

<!-- PAGE 41 -->

Figure 5: User’s net worth over time

7.3 Automating financial data retrieval

One of the key goals identified during the problem definition phase was to reduce
the manual effort required to update financial data, especially stock prices, exchange
rates, and account balances. While full automation remains a challenge due to limited
access to bank and broker APIs, the current solution introduces partial automation
that meaningfully reduces the user’s workload.

Stock prices are automatically retrieved through a Google Sheets integration, where
the sheet is powered by the GOOGLEFINANCE function (See Figure 6). The application
connects to this sheet through the Google Sheets API and fetches up-to-date prices
for all tickers listed by the user. Although users must still maintain this ticker list and
enter share transactions manually, the solution removes the need to repeatedly copy
data between Excel files.

41

---

<!-- PAGE 42 -->

Figure 6: Google Sheet with the user’s stock tickers powered by the GOOGLEFINANCE
function

Exchange rates are retrieved daily using the HexaRate API and stored in the database
for reuse. This ensures that all financial data regardless of original currency is converted
consistently without requiring the user to look up or input rates manually.

While income and expense data are still entered manually through the application’s
user interface, the system centralizes this information for easier tracking. In the
stakeholder’s previous workflow, expense and income data were entered into Spendee,
exported, and then incorporated into a financial report and master Excel file. In contrast,
the new system decreases redundancy and improves consistency by maintaining all
data in a centralized platform. This removes the need to update rates and prices across
multiple tabs and formulas.

Future iterations may include integration with Open Banking APIs or broker-

42

---

<!-- PAGE 43 -->

specific services, if reliable and cost-effective options become available. The current
solution offers a practical balance between automation, data accuracy, and user control.
Achieving even partial automation has helped reduce friction for users and create a
level of consistency. This aligns with findings by Cederberg (2013), who noted that
users were more likely to adopt PFM tools when features such as transaction tracking
and visual summaries were automated, reducing manual input and cognitive effort.
However, as pointed by Kaye et al. (2014), some users may become frustrated with
too much automation, such as inflexible or inaccurate expense categorization, which
can hinder trust or usability. This supports the rationale for retaining user control
alongside automation, ensuring the system remains both efficient and adaptable to
individual preferences.

7.4 Centralized tracking across categories

The application provides structured and centralized tracking of financial data across
asset and cash flow categories. Assets, including shares, cash, and real estate, are stored
in dedicated collections and grouped using relevant identifiers to support organized
analysis.

Shares are enriched with metadata such as category (e.g., dividend, growth),
subcategory (e.g., REIT, BDC), and country of origin. These additional fields enable
detailed breakdowns and are visualized through multi-layered pie charts, as shown in
Figure 7.

Figure 7: Share distribution visualized by category, country, and subcategory

Cash assets are grouped by account name (e.g., savings or investment account),
while real estate holdings are categorized by property name. This helps users track
the value and performance of each asset individually, without mixing different types
of finances together (See Figure 8).

43

---

<!-- PAGE 44 -->

Figure 8: Other asset distribution visualized by category, country, and subcategory

Additionally, the application tracks income and expenses under the cash flow
module. Transactions are tagged with labels such as food, salary, or shopping, enabling
categorized insights. As shown in Figure 9, cash flow data is presented through
categorized pie charts, a chronological transaction timeline, and a bar chart comparing
monthly income and expenses.

44

---

<!-- PAGE 45 -->

Figure 9: Cash flow tracking: categorized income and expenses with monthly
comparison

The system provides the user with insights that were previously fragmented through-
out different tools and spreadsheets by standardizing categorization for both assets
and transactions and consolidating all of the data within a single interface. This helps
centralizing the user’s financial management, and ultimately helps their decision-
making process. More organized and categorized financial data can aid more informed
insights and decision-making. This supports findings from Gafrikova et al. (2015),
who described how PFM tools provide users with categorized expense tracking,
grouped spending by type (e.g., rent, food, transportation), and aggregated financial
information from various sources, which improves visibility into personal financial
flows. Handayani et al. (2024) similarly noted that automatic expense trackers, cate-
gorization features, and integration across financial sources allow users to recognize
their spending patterns and make better financial decisions.

7.5 Integrated and efficient reporting

One of the most labor-intensive tasks in the stakeholder’s previous workflow was
the creation of quarterly financial reports. This process involved manually copying
charts, aggregating figures from various spreadsheets, and compiling them into a Word
document. The PoC application replaces this with a fully integrated reporting feature
that generates a comprehensive summary for a selected time period.

The report consolidates data from multiple parts of the system into a single PDF

45

---

<!-- PAGE 46 -->

file and includes the following elements:

• Monthly income, expenses, and surplus visualized in a grouped bar chart

• Savings percentage per month

• Expenses vs. income displayed as a line chart

• A detailed list of categorized cash flow transactions

• Net worth development over time and breakdown by asset category

• Share distribution by type, country, and subcategory

All data is automatically retrieved from the backend and visualized through charts
and tables based on the selected time frame. The compiled report is exported as
a downloadable PDF document, allowing users to archive or review their financial
summaries without manual intervention.

This feature saves time and effort when generating reports on a recurring basis
by replacing a multi-step manual process with one integrated functionality. As
Cederberg (2013) says, automating repetitive financial tasks along with providing
visual summaries for clarity can reduce the burden on users and ease adoption.
Likewise, Shafiee et al. (2024) point out that reporting provides coherent and visual
outputs to help establish understanding and inform decisions. It also satisfies the idea
for an overview of finances by Kaye et al. (2014), consolidating a number of tools and
processes into a singular reporting process.

46

---

<!-- PAGE 47 -->

Figure 10: User-generated financial report for a selected time period

By automating the generation of structured and visually rich reports, the system
supports more efficient and consistent financial review cycles while preserving the
stakeholder’s preference for detailed documentation and analysis.

47

---

<!-- PAGE 48 -->

8 Evaluation

This chapter presents the results of the evaluation phase. The goal of this phase is to
assess how effectively the implemented artifact addresses the original problem and
fulfills the defined solution objectives. Four evaluation methods were used: task-based
user testing, a stakeholder feedback questionnaire, comparison to the baseline system,
and analytical assessment against the design objectives.

8.1 Task-based user testing

Task-based user testing was conducted to observe the stakeholder interacting with the
system in a realistic usage scenario. The purpose was to evaluate the usability, core
functionality, and overall user experience. The stakeholder performed a predefined set
of tasks on their own machine while being observed. Each task was assessed based on
successful completion, workflow intuitiveness, and any usability issues or feedback
that arose. The tasks were originally defined in Chapter 3.1.5.

All tasks were completed successfully. The stakeholder navigated the system
confidently and required no external guidance to locate or use any of the key features.
Task durations ranged from two to five minutes, depending on data entry requirements.
For example:

• Task 1: The stakeholder imported share transactions using a CSV file and

manually added two cash and two real estate transactions.

• Task 2: The user explored pie charts on the dashboard by category and reviewed
data tables on the "Assets and Transactions" page, including testing the sorting
and editing functionalities.

• Task 3: Multiple income and expense transactions were added across a four-
month period, followed by a review of the updated cash flow visualizations.

• Task 4: The stakeholder generated a financial report for the period 1.1.2025–30.4.2025

and examined the contents of the generated PDF file.

Feedback during testing primarily concerned user interface clarity and usability

improvements. Notable suggestions included:

• Enhancing tooltips in pie charts to show additional details (e.g., EUR value)

• Improving label clarity in the real estate table

• Adjusting the transaction ordering in the cash flow list for better intuitiveness

Despite these observations, all tasks were completed without errors or external
assistance which indicates that the system provides a generally intuitive and user-

48

---

<!-- PAGE 49 -->

friendly experience. These findings are consistent with literature showing that
structured, intuitive interfaces and visual feedback mechanisms play a big role in
improving user engagement and confidence in personal finance tools. This is supported
by Cederberg (2013), who found that simplified interfaces with visual summaries
reduce user effort and promote adoption. Similarly, Shafiee et al. (2024) note that
user-friendly and personalized interfaces improve users’ understanding and confidence
in financial decision-making.

8.2 Stakeholder insights from questionnaire

Following the task-based testing session, a structured questionnaire was administered
to gather deeper feedback from the stakeholder. The questions were organized into
four areas: general impressions, feature satisfaction, problem-solving impact, and
suggestions for future development. This section summarizes the stakeholder’s
responses in each area.

8.2.1 General impressions

The stakeholder found the interface intuitive and user-friendly. Although some
functionalities were not immediately visible, they were easily discovered through brief
exploration. Overall, the structure and navigation of the application were considered
effective and aligned with typical user expectations.

8.2.2 Feature satisfaction

The share tracking functionality was praised for its scalability and ease of use compared
to the stakeholder’s previous Excel system. The automation of data aggregation and
value computation was seen as a major improvement.

The stakeholder found the cash flow feature useful and realistic but suggested
clarifying its purpose whether it is meant for detailed budgeting like in apps such as
Spendee, or for more general expense tracking. This would help determine whether
the feature should be simplified or offer more customization.

Visualizations were described as clear and informative. The stakeholder highlighted
the pie charts and trend graphs as particularly valuable for gaining quick insights.
Minor refinements were suggested, particularly for the long-term capital development
graph to improve clarity.

It
The PDF report generation feature was considered a strong improvement.
streamlined a previously manual and time-consuming reporting process, offering clear
value through automation and integration.

49

---

<!-- PAGE 50 -->

8.2.3 Problem-solving impact

The stakeholder reported a reduction in manual work, especially with processes that
went back and forth between excel and google sheets. The ability to see all the financial
information in one interface was seen as a major improvement. This supports findings
by Kaye et al. (2014) that users preferred simplified snapshots rather than a complete
representation. In a similar manner, Cederberg (2013) noted that PFM systems offering
centralized and easy-to-access financial data increase user motivation and ongoing
engagement.

System stability and data reliability were also noteworthy. In contrast to the previous
Excel workflow that was susceptible to broken formulas and inconsistencies, the PoC
was praised as secure and dependable. Automatic integration of transactions and
chronological organization contributed to a higher level of trust in the data. This
finding supports the consideration of epistemic stability in personal finance tools,
articulated by Herrala et al. (2023). They argued that users must be able to trust the
logic and output of the application in order to experience the sense of empowerment
and feeling of control over their finances. When tools are perceived as unpredictable
or "black box", users’ trust in the data and the system as a whole can decrease.

8.2.4 Suggestions and future improvements

Suggestions focused primarily on improving user experience and refining existing
features. These included:

• Enhancing tooltip and graph clarity

• Adding the ability to modify transactions directly from the transaction list

• Clarifying the intended use of the cash flow functionality

Overall, the stakeholder expressed strong confidence in the application’s potential.
They indicated that with further refinement and iteration, the system could evolve into
a fully deployable product that meets broader personal finance management needs.

8.3 Comparison to baseline

In order to assess the practical advantages of the implemented solution, a simple
comparison was made between the stakeholder’s existing financial tracking method
to the PoC application. The original method consisted of numerous approaches and
tools, such as Excel spreadsheets, Google Sheets, and the Spendee application, where
consolidating all of the information was laborious and manual.

Table 9 summarizes key differences between the baseline setup and the PoC system.

50

---

<!-- PAGE 51 -->

Old system (Baseline)
Multiple tools: Excel,
Spendee, Google Sheets
Manual copy-paste from
Google Finance
Manually checked and entered Automatically fetched daily

New system (PoC)
Centralized, web-based
application
Automated via Google Sheets
API integration

Aspect
Tool
fragmentation
Share price
updates
Exchange rate
updates
Income/expense
tracking
Data visualization Static, manually created Excel

Recorded in Spendee,
analyzed in Excel

Financial
reporting
Stability and
accuracy
Time spent
updating

charts
Manual report assembly in
Word with Excel charts
High risk of formula errors
and broken references
Significant manual effort and
tool switching

from HexaRate API
Entered and visualized within
the application
Interactive, real-time
visualizations and tables
Automated PDF reports with
integrated data and visuals
Backend-calculated values
with robust logic
Streamlined updates via
integrated data flow

Table 9: Comparison of the baseline system and the PoC application

As seen in Table 9, the PoC solution meets the most important issues found from
the previous system, by offering centralized data, an automated updates, and built-in
analytic capabilities. In short, it minimizes user manual workload and error rates while
increasing data transparency. The stakeholder was in agreement that the usability,
automation, and trust in the accuracy of the data had improved. Torno et al. (2021)
found that most personal finance solutions tend to focus on very few features or
services, so this PoC focuses bridging these gaps.

8.4 Evaluation against design objectives

This section assesses how effectively the implemented PoC meets the functional and
quality objectives defined in Chapter 5. Each requirement is reviewed based on the
actual system implementation, stakeholder feedback, and outcomes observed during
the evaluation phase.

FR-01: User interface (Desktop and mobile)

The system was implemented using Flutter, supporting deployment across desktop,
web, and mobile platforms. The stakeholder confirmed the interface was intuitive and
easy to use during desktop testing. However, the current implementation is primarily
optimized for desktop and web, with mobile-specific layout adjustments still pending.
Status: Partially achieved

FR-02: Data visualization of capital and statistics

Interactive charts and graphs were implemented to visualize net worth trends, asset

51

---

<!-- PAGE 52 -->

categories, and cash flow summaries. The stakeholder highlighted these features as
clear and significantly more effective than their previous manual visualizations. Status:
Achieved

FR-03: Tagging

The data model supports asset classification by categories, subcategories, and country
of origin. Tagging is applied consistently across shares, cash accounts, real estate, and
cash flow transactions. Status: Achieved

QA-01: Correctness of statistics

Key calculations, including net worth, profit/loss, and savings rate, are performed by
centralized backend logic, reducing risk of user error. The stakeholder confirmed the
accuracy and reliability of the results. Status: Achieved

FR-04: Present real-time capital information

Real-time market data and exchange rates are fetched automatically, ensuring up-to-
date capital values. This functionality was identified by the stakeholder as a major
improvement over the manual update process. Status: Achieved

FR-05: Financial report generation

The system provides downloadable PDF reports summarizing key financial metrics
over a selected time frame. This replaced the stakeholder’s manual reporting process
and was viewed as a major efficiency improvement. Status: Achieved

QA-02: Data access control

Although the data model is designed to support user-level data segregation, no
authentication or authorization mechanisms were implemented. This limitation was
acknowledged and deferred due to time constraints and PoC scope. Status: Not
achieved

FR-06: Automatic data fetching

The system integrates with external sources to retrieve exchange rates and share
prices. However, full automation of bank or broker transactions was not implemented.
Despite this, the current solution meaningfully reduces manual effort. Status: Partially
achieved

FR-07: Choose currency

All financial data is normalized to a base currency, with exchange rates fetched daily.
This ensures consistency across calculations and supports user-defined currency views.
Status: Achieved

FR-08: Customizable dashboards

Customizable dashboards were not implemented. All visualizations are static and
predefined. This feature was deprioritized due to limited time and PoC focus. Status:
Not achieved

52

---

<!-- PAGE 53 -->

FR-09: Manual financial data input

Structured forms and CSV import features were implemented for all major transaction
types, enabling effective manual data entry and corrections. Status: Achieved

QA-03: Good response time

Performance during testing was consistently fast. Efficient data fetching, use of
caching, and state management contributed to a responsive user experience. However
no performance testing was conducted and some refinements would be needed for
production version. Status: Achieved

In summary, all core "Must have" requirements were successfully implemented or
partially fulfilled, ensuring that the fundamental goals of the PoC were met. Most
"Should have" features were included, while lower-priority items such as authentication
and dashboard customization were deferred for future development iterations.

53

---

<!-- PAGE 54 -->

9 Discussion

This chapter looks back on the project and reflects on what was achieved. It starts by
reviewing how well the final solution addressed the original problem and what kind
of feedback the stakeholder gave. It also considers how useful the Design Science
Research Methodology (DSRM) was throughout the process. In addition, the chapter
highlights some of the challenges faced during development and points out possible
ways the solution could be improved or expanded in the future. Altogether, it gives a
clear picture of what the project accomplished and where it could go next.

9.1 Summary of results and impact

The findings from this research project show that the PoC application accomplishes the
identified goals defined earlier in the thesis. The core functionalities were implemented
and tested with the actual end user in a realistic environment. User feedback confirmed
that the application solved the primary stakeholder concerns: it reduced manual effort
and mitigated human errors. This finding corresponds with Herrala et al. (2023)’s
observation that complex in an error-prone tools can reduce financial confidence and
raise unnecessary anxiety, especially for younger users. By reducing complexity and
centralizing financial data, the PoC system improves both usability and reliability.

Unlike many existing PFM tools which focus on limited functionality, such as
budgeting or tracking spending patterns (e.g., Mint, YNAB, Spendee), the PoC was
designed to provide a more global and integrated approach across all aspects of PFM.
The PoC provided a functionality for tracking investments, monitoring net worth,
analyzing cash flow, and producing financial reports, in a more centralized way.
The PoC’s design directly addressed the fragmented focus of PFM as recognized by
Torno et al. (2021). The study noted that most PFM apps focus on single service
and rarely combine planning, tracking, and education in one app. While Kaye et
al. (2014) noted that some tools provide discomfort due to perceived complexity,
reliability, and fragmented view of PFM thus risking long-term engagement. The
existing stakeholder system also lacked automation which was noted in the literature.
According to Cederberg (2013), automating tasks and reducing manual user input
were big motivators for adopting mobile financial tools, as they simplified workflows
and reduced friction. The PoC application improves on this by providing automated
retrieval of exchange rates, stock price updates, and aggregation of asset data in
real-time.

One of the major strengths was the PoC being adaptable under the European
context. Many of the popular PFM tools, such as Mint, Quicken, etc. are largely
based on U.S. users, customarily linked to regionally-identified financial APIs. This
also complements the findings of Stefanov et al. (2024), who stated that users from
underrepresented markets, for example from Eastern Europe, face localization issues
relating to global PFM tools. The stakeholder was also able to benefit from features
that include multi-currency and share price updates for both Finnish and Swedish

54

---

<!-- PAGE 55 -->

stocks, which is commonly not available in mainstream financial applications.

Another identified core improvement was the transition on reporting from quarterly
to real-time financial reporting. Previously, the stakeholder was only engaging in
quarterly reviews due to time consuming process. The stakeholder can now analyze
real-time dashboards in one quick view and initiate reports into pdf. This functionality
supports the findings of Cederberg (2013), which implied that financial tools with
less manual inputs and offered simplified workflows made it likely that users further
engage with personal finance technologies. Similarly, Shafiee et al. (2024) noted
that real-time, personalized outputs enhance users’ understanding and support more
responsive financial decision-making.

Finally, by delivering real-time insights and visual feedback through pie charts, bar
graphs, and trend visualizations, the application promotes awareness and decision
confidence. Bitrián et al. (2021) found that visual and gamified elements can increase
users’ perceived competence and engagement. Similarly, Shafiee et al. (2024) showed
that personalized and real-time financial guidance helps users better understand
complex financial factors and make more informed decisions.

9.2 Limitations of the solution

While the PoC successfully addressed core requirements, several limitations remain.
Most unimplemented features were categorized as “nice to have” or optional and were
intentionally excluded due to the limited scope and timeframe of the project. However,
one critical weakness is the absence of user authentication and authorization. Security
is a fundamental concern in financial technology, especially where sensitive personal
data is involved. Kaye et al. (2014) explains that users are often reluctant to adopt
digital finance tools due to fears around data access and privacy. Similarly, Handayani
et al. (2024) identify security and data protection as central factors influencing user
trust in fintech solutions. Herrala et al. (2023) further argue that when users feel a lack
of control over their financial information, it can contribute to stress and disengagement,
highlighting the importance of transparent and secure system design. These findings
underscore the importance of implementing basic access control mechanisms in future
iterations to strengthen system credibility and promote long-term use.

From a development perspective, the most significant limitation is the incomplete
automation of financial data retrieval. Although the stakeholder expressed satisfaction
with the current level of automation, the system lacks the scalability needed to support
broader user base. Ideally, users would be able to connect their bank and brokerage
accounts directly to the application, allowing automatic synchronization of transactions
and balances. However, this level of integration remains difficult to implement due
to different factors. Several stock price API’s were investigated such as Finnhub,
stockdata.org, eoddata, and Alpha vintage, but were eventually discarded due to limited
support for European stocks or were too expensive. Investment brokers also do not
have API’s or they are limited, for example Nordnet offers API only in Sweden.

55

---

<!-- PAGE 56 -->

Additionally, from open-banking perspective, some options were investigated such as
Yapily, Polygon, and GoCardless. These were not suitable for the context case as they
were either targeted for enterprises or required a lot of development work. Another
issue with the open-banking integrations is the automated categorization which was
pointed out also by Kaye et al. (2014).

As a practical workaround, the PoC application integrates with Google Sheets using
the GOOGLEFINANCE function to retrieve stock prices. This solution, while manual to set
up, aligned with the stakeholder’s workflow and allowed real-time pricing without
additional financial costs. Still, the absence of seamless, API-based integration for
broader asset classes and account types remains a major limitation. These findings
support what Cederberg (2013) observed: manual data entry and scattered tools make
it difficult for people to continue using personal finance systems in the long run.

Another thing to note is the stakeholders good financial literacy and therefore higher
expectations from the system. As they have tracked their finances more than a decade,
they have accumulated a lot of knowledge and experience in this domain. However,
some usability improvements and educational content would be beneficial to add
in the current application for more novice users. This need is also reflected in the
literature. Torno et al. (2021) point out that few personal finance applications offer
built-in financial education, despite its potential to increase trust and engagement.
Similarly, Lasmiatun (2024) found that younger users often turn to digital platforms
for financial guidance and prefer interactive and visual formats for learning. Kaye et al.
(2014) also noted that many users do not engage with existing all-in-one financial
systems, suggesting an opportunity to design more accessible and user-tailored financial
experiences.

9.3 Reflection on DSRM

Design Science Research Methodology (DSRM) provided an effective structure
for development of this project. The structured iterative process created a logical
progression starting with a problem definition step and ending with an artifact evaluation
step which was extremely useful in a solo development environment. DSRM consists
of set of steps as described by Peffers et al. (2007) that enable researchers to develop
solutions to real-world problems by the design and evaluation of artifacts.

Each phase of the DSRM directly informed the next. In Design and Development
phase, the architectural decisions were derived from the functional and non-functional
requirements. The requirements on the other hand were formatted based on the
stakeholder needs found in the Problem identification phase. Evaluation phase benefited
from the established objectives but also provided substance to their evaluation. This
corresponds with the guidance of Hevner et al. (2004) that utility, quality, and efficacy
are necessary criteria of evaluating design artifacts in information systems research
context.

56

---

<!-- PAGE 57 -->

Having a real stakeholder involved made a big difference in the project. Their
ongoing feedback gave practical insights that would have been hard to discover through
theory alone. By taking part in the demonstration and evaluation, they ensured the
solution met real needs and worked in practice. As De Sordi (2021) points out,
involving practitioners in Design Science Research makes the results more relevant
and strengthens the credibility of the research.

Overall, Design Science Research Methodology gave a clear but flexible way to
work through the project. It made it easier to build a useful and practical solution
while still following a solid research process. This made it a good choice for a project
like this that combines real-world needs with academic work.

9.4 Opportunities for future development

The evaluation phase revealed several key opportunities to enhance the PoC application
and move toward a production-ready solution. The most critical area for future
development is the integration of automated data fetching from banks and brokers.
Implementing such features would significantly reduce manual input, enhance user
convenience, and improve the system’s scalability for a wider audience. This addresses
a limitation also observed by Torno et al. (2021) and Stefanov et al. (2024), who found
that most PFM tools lack comprehensive integration across financial institutions, with
Stefanov et al. (2024) further noting that many solutions offer only limited localized
services, reducing their effectiveness in certain markets.

Usability improvements also emerged as a priority. The stakeholder identified a
range of refinements that would improve the user experience, including the ability
to edit transactions directly, more informative tooltips, and clearer differentiation
between detailed budgeting and high-level cash flow tracking. This aligns with findings
by Cederberg (2013), who described that users value intuitive, visually appealing
interfaces that reduce manual effort and support financial self-awareness. Similarly,
Bitrián et al. (2021) found that clear feedback mechanisms and well-designed user
experiences foster perceived competence and autonomy which are two key drivers of
sustained use in personal finance applications.

The addition of user authentication and authorization is essential for ensuring data
privacy and security, especially if the system is to be deployed beyond the original
stakeholder. On the technical side, the introduction of unit and integration testing,
along with comprehensive documentation, would support long-term maintainability
and facilitate collaboration in larger development teams. Also, splitting the architecture
into several microservices would increase scalability and increase performance for a
production environment where more traffic is to be expected.

57

---

<!-- PAGE 58 -->

10 Conclusions

This thesis covered the design and development of a centralized personal finance
management application that addressed the problems faced by an individual stakeholder.
The main issues involved the complexity, fragmentation, and manual workload
that were found in the stakeholder’s existing financial tracking setup. The system
relied on a combination of Excel spreadsheets, third-party apps, and manual data
consolidation. The objective was to create a customized solution that improves
automation, visualization, and reporting while supporting personalized financial
analysis.

The project followed the Design Science Research Methodology (DSRM), which
provided a structured and iterative framework with six steps: problem identification,
objective definition, design and development, demonstration, evaluation, and com-
munication. This methodology supported both the technical execution and academic
rigor of the research process. Each phase produced outcomes that could be used on the
next stages, eventually resulting in a functioning proof-of-concept (PoC) application.

The final artifact includes asset tracking such as shares, cash, and real-estates,
categorized cash flow monitoring, and financial PDF report generation. In addition to
constant feedback during the development phase, these features were validated through
task-based user testing and structured stakeholder feedback. Compared to the baseline
system, the PoC significantly reduced manual effort, improved data reliability, and
offered a centralized view of the user’s financial status. These outcomes align with
findings in the literature, which stressed that simplification, visual feedback, and trust
are important for effective personal finance tools.

However, the PoC did not implement several planned features, including user
authentication, customizable dashboards, or full data automation through banking and
broker integrations. These limitations stemmed from external API constraints and
the limited scope of a solo development project and would be main focus area if this
application would be deployed to broader use.

One of the challenges faced during this thesis was finding good literature that really
looked at how people manage their finances in everyday life. A lot of the existing
research focuses on financial literacy, behavior, or planning theory, but there was not
much detail about what tools people actually use. It was hard to find statistics or studies
about which apps people rely on, what works for them, and what problems they run
into. That is one of the main reasons this thesis came to life. Most apps on the market
are built just for budgeting or tracking expenses. With simple Google search “personal
finance apps,” almost all of them fall into that category. But managing your finances
is more than just budgeting. People also want to track investments, assets, and see
their full financial picture in one place. More research is needed that looks into how
people actually manage their finances and how tools could be built to support that.

58

---

<!-- PAGE 59 -->

References

Atkinson, Adele and Flore-Anne Messy (2012). Measuring Financial Literacy:
Results of the OECD / INFE Pilot Study. Tech. rep. 15. OECD Publishing. d o i:
10 . 1787 / 5k9csfs90fr4 - en. u r l: https : / / www . oecd . org / content / dam / oecd /
en/publications/reports/2012/03/measuring- financial- literacy_g17a210b/
5k9csfs90fr4-en.pdf.

Bitrián, Paula et al. (2021). “Making finance fun: the gamification of personal financial
management apps”. In: International Journal of Bank Marketing 39.7, pp. 1310–
1332. d o i: 10.1108/IJBM-02-2021-0074. u r l: https://doi.org/10.1108/IJBM-
02-2021-0074.

Brush, Kate (2023). MoSCoW method. TechTarget definitions. u r l: https://www.

techtarget.com/searchsoftwarequality/definition/MoSCoW-method.

Cederberg, Jessica (2013). “Changing Financial Behaviors Using Mobile PFM Tools
(Dissertation)”. In: Södertörn University, Sweden. u r l: https://urn.kb.se/
resolve?urn=urn:nbn:se:sh:diva-19735.

De Sordi, José Osvaldo (2021). Design Science Research Methodology: Theory
Development from Artifacts. 1st. Palgrave Macmillan Cham. d o i: https :
//doi.org/10.1007/978-3-030-82156-2.

Di Domenico, Stefano I. et al. (2022). “Motivations for personal financial management:
A Self-Determination Theory perspective”. In: Frontiers in Psychology Volume 13
- 2022. i s s n: 1664-1078. d o i: 10.3389/fpsyg.2022.977818. u r l: https://www.
frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.977818.
Enstrom, D. W. (2018). Guideline: Architectural Decision. https://www.unified-
am.com/UAM/UAM/guidances/guidelines/uam_architectural_decision_BAE7AFA2.
html. Unified Architecture Method (UAM).

French, Declan et al. (2021). “Personal finance apps and low-income households”. In:

Strategic Change 30, pp. 367–375. do i: 10.1002/jsc.2430.

Gafrikova, V. et al. (2015). “Online personal finance management applications”. In: In-
formation Systems in Management 4.1, pp. 39–52. url: https://bibliotekanauki.
pl/articles/94727.

Gitman, L.J. et al. (2011). Personal financial planning. 12th. South-Western Cengage

Learning. is bn: 978-1-4390-4447-6.

Handayani, Tika et al. (2024). “Fintech Analysis of Personal Finance App Usage
among Millennials”. In: Journal of Economic Education and Entrepreneurship
Studies 5, pp. 150–162. doi: 10.62794/je3s.v5i2.2299.

Herrala, Juha-Matti et al. (2023). “How Personal Finance Management Systems
Emancipate and Oppress Young People”. In: Proceedings of the 56th Hawaii
International Conference on System Sciences, pp. 5542–5550. d o i: 10.24251/
HICSS.2023.675.

Hevner, Alan R. et al. (2004). “Design Science in Information Systems Research”.
In: MIS Quarterly 28.1, pp. 75–105. do i: https://doi.org/10.2307/25148625.
Huang, Lisha (2016). “Personal Financial Planning for College Graduates”. In:
Technology and Investment 7, pp. 123–134. d o i: 10.4236/ti.2016.73014. u r l:
https://doi.org/10.4236/ti.2016.73014.

59

---

<!-- PAGE 60 -->

Ironhack (2024). Functional vs Non-Functional Requirements: Understanding the
Core Differences and Examples. Ironhack blogs. u r l: https://www.ironhack.
com / gb / blog / functional - vs - non - functional - requirements - understanding -
the-core-differences-and.

Kaye, Joseph Jofish et al. (2014). “Money talks: tracking personal finances”. In:
Proceedings of the SIGCHI Conference on Human Factors in Computing Systems.
Association for Computing Machinery, pp. 521–530. isbn: 9781450324731. doi:
10.1145/2556288.2556975. u rl: https://doi.org/10.1145/2556288.2556975.
Lai, Ming-Ming and Wei-Khong Tan (2009). “An Empirical Analysis of Personal
Financial Planning in an Emerging Economy”. In: European Journal of Economics,
Finance and Administrative Sciences. i ssn: 1450-2275.

Lasmiatun, KMT (2024). “The Role of Financial Education in Improving Personal
Financial Planning: A Qualitative Study on Generation Z”. In: Nomico 1, pp. 149–
158. doi: 10.62872/8n585q36.

Lusardi, Annamaria and Olivia S. Mitchell (2014). “The Economic Importance of
Financial Literacy: Theory and Evidence”. In: Journal of Economic Literature
52.1, pp. 5–44. doi: https://doi.org/10.1257/jel.52.1.5.

Peffers, Ken et al. (2007). “A design science research methodology for information
systems research”. In: Journal of Management Information Systems 24, pp. 45–77.
doi: 10.2753/MIS0742-1222240302.

Rajesh, R.J. and K.V. Giridhar (2024). “Financial literacy and personal financial
management: Smart moves towards personal finance”. In: Shanlax International
Journal of Arts, Science and Humanities 12.S1, pp. 62–67. d o i: https://doi.
org/10.34293/sijash.v12iS1- Oct.8285. u r l: https://shanlaxjournals.in/
journals/index.php/sijash/article/view/8285.

Shafiee, Sara et al. (2024). “Improving Financial Literacy and Supporting Financial
Decisions: Developing a Personalized Configurator”. In: Journal of the Knowledge
Economy 15, pp. 14256–14285. d o i: https://doi.org/10.1007/s13132- 023-
01651-9.

Shah, Sweety and Amola Bhatt (2014). “Understanding Practices of Personal Financial
Planning (PFP)”. In: International conference on “Role of Financial Industry in
Accelerating Economic Growth” organised by Gujarat Technological University
(GTU) - Centre for Financial Services, Ahmedabad.

Siegel, R. and C. Yacht (2009). Personal Finance. Saylor Foundation. i s b n:
9780982361863. u rl: https://open.umn.edu/opentextbooks/textbooks/31.
Stefanov, Tihomir et al. (2024). “Personal Finance Management Application”. In:

TEM Journal 13, pp. 2066–2075. do i: 10.18421/TEM133-34.

Torno, Albert et al. (2021). “More than Mobile Banking – A Taxonomy-based
Analysis of Mobile Personal Finance Applications”. In: PACIS 2021 Proceedings.
179. u rl: https://aisel.aisnet.org/pacis2021/179.

Vaishnavi, V.K. and W. Kuechler (2015). Design Science Research Methods and
Patterns: Innovating Information and Communication Technology. 2nd. CRC
Press. doi: https://doi.org/10.1201/b18448.

60

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Master’s Programme in Computer, Communication and Information Sciences
| Proof   | of concept  | of centralized | personal |
| ------- | ----------- | -------------- | -------- |
| finance | application |                |          |
Milla Sipilä
Master’s Thesis
2025

MillaSipilä
Author
Proofofconceptofcentralizedpersonalfinanceapplication
Title
Computer,CommunicationandInformationSciences
Degree programme
Algorithms,Logic,andComputation
Major
ArtoHellas
Supervisor and advisor
29.6.2025 60 English
Date Number of pages Language
Abstract
This thesis presents the design and development of a centralized personal finance
management application using the Design Science Research Methodology (DSRM).
Theworkisbasedinpriorresearchonfinancialbehavior,planning,andmanagement
tools, explaining how motivation, structured planning, and digital solutions influence
financial well-being. The goal was to address real-world challenges faced by an
individualstakeholder,whoseexistingfinancialtrackingsystemreliedonfragmented
tools and manual processes. A proof-of-concept (PoC) application was developed
usingFlutter,.NET,andMongoDB,includingfunctionalitiessuchasassettracking,
categorized cash flow visualization, real-time data updates, and financial report
generation. Thesolutionwasiterativelydesignedbasedonstakeholder’sfeedbackand
evaluatedthroughtask-basedtesting,structuredquestionnaires,andcomparisontothe
baseline system. Results show significant improvements in automation, accuracy, and
usability. Whilesomefeatures,suchasauthenticationandfullbankingintegration,
were out of scope for this PoC, the system provides a strong foundation for further
developmentandwiderapplicabilityinthedomainofpersonalfinancemanagement.
Personalfinance,Financialplanning,DesignScienceResearch,Proofof
Keywords
Concept,Personalfinanceapplication,Financialtracking,User-centered
design

MillaSipilä
Tekijä
Keskitetynhenkilökohtaisenrahoitussovelluksenkonseptitodistus
Työn nimi
Tietotekniikka
Koulutusohjelma
Algoritmit,Logiikka,jaLaskenta
Pääaine
ArtoHellas
Työn valvoja ja ohjaaja
29.6.2025 60 englanti
Päivämäärä Sivumäärä Kieli
Tiivistelmä
Tämä diplomityö käsittelee keskitetyn henkilökohtaisen taloudenhallintasovelluk-
sensuunnitteluajakehittämistähyödyntäenDesignScienceResearchMethodology
(DSRM)-tutkimusmenetelmää.Työnteoreettinentaustapohjautuuaiempaankirjalli-
suuteentaloudellisestakäyttäytymisestä,suunnittelustajataloudenhallintatyökaluista,
joissa korostuvat motivaatio, suunnitelmallisuus ja digitaaliset ratkaisut taloudellisen
hyvinvoinnintukena.Työntavoitteenaoliparantaayksityisentoimijanolemassaolevaa
järjestelmää,joka koostuihajanaisista työkaluista ja manuaalisistaprosesseista. Kon-
septitodistuskehitettiinhyödyntäenteknologioitakutenFlutter,.NETjaMongoDB.
Sovellus sisältää toimintoja kuten varallisuuden seuranta, kategorisoitu kassavirta-
analyysi, reaaliaikainen datan päivitys sekä talousraporttien generointi. Ratkaisu
suunniteltiin iteratiivisesti toimijan palautteen perusteella ja arvioitiin tehtäväpoh-
jaisella testauksella,strukturoidulla kyselyllä ja vertailulla aiempaan järjestelmään.
Tuloksetosoittavatmerkittäviäparannuksiaautomaatiossa,luotettavuudessajakäytet-
tävyydessä.Vaikkakaikkiatoimintoja,kutentunnistautumistataipankki-integraatioita,
ei toteutettu konseptitodistuksessa, sovellus luo vahvan pohjan jatkokehitykselle ja
laajemmallekäytettävyydellehenkilökohtaisentaloudenhallinnanalueella.
Henkilökohtainentalous,Taloussuunnittelu,Kehittämistutkimus,
Avainsanat
Konseptitodistus,Henkilökohtaisentaloudensovellus,Talouden
seuranta,Käyttäjälähtöinensuunnittelu

Contents
Abstract 2
Abstract(inFinnish) 3
Contents 4
Symbolsandabbreviations 6
1 Introduction 7
1.1 Contextandmotivation . . . . . . . . . . . . . . . . . . . . . . . . 7
1.2 Objectivesandscope . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.3 Useofartificialintelligencetools . . . . . . . . . . . . . . . . . . . 8
1.4 Thesisstructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2 Literaturereview 10
2.1 Financialliteracyandbehaviors . . . . . . . . . . . . . . . . . . . 10
2.2 Personalfinancialplanning . . . . . . . . . . . . . . . . . . . . . . 11
2.3 Personalfinancemanagementtools . . . . . . . . . . . . . . . . . . 13
2.4 Designscienceresearch . . . . . . . . . . . . . . . . . . . . . . . . 15
3 Researchmethodology 18
3.1 DSRMactions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.1.1 Problemidentificationandmotivation . . . . . . . . . . . . 18
3.1.2 Definetheobjectivesforthesolution . . . . . . . . . . . . . 19
3.1.3 Designanddevelopment . . . . . . . . . . . . . . . . . . . 19
3.1.4 Demonstration . . . . . . . . . . . . . . . . . . . . . . . . 20
3.1.5 Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.1.6 Communication . . . . . . . . . . . . . . . . . . . . . . . . 22
3.2 MotivationforDSRM . . . . . . . . . . . . . . . . . . . . . . . . . 23
4 Problemidentificationandmotivation 24
4.1 Stakeholderinsightsfromquestionnaire . . . . . . . . . . . . . . . 24
4.1.1 Currentfinancialmanagementapproach . . . . . . . . . . . 24
4.1.2 Frequencyofuse . . . . . . . . . . . . . . . . . . . . . . . 24
4.1.3 Challengeswiththecurrentsystem . . . . . . . . . . . . . 24
4.1.4 Desiredfeaturesforanimprovedsolution . . . . . . . . . . 25
4.1.5 Stakeholderreflections . . . . . . . . . . . . . . . . . . . . 25
4.2 Problemdescription . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.3 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5 Definingobjectivesforthesolution 28
5.1 Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
5.2 Prioritizedobjectives . . . . . . . . . . . . . . . . . . . . . . . . . 30
4

6 Designanddevelopment 32
6.1 Architecturaldecisions . . . . . . . . . . . . . . . . . . . . . . . . 32
6.2 Systemarchitecture . . . . . . . . . . . . . . . . . . . . . . . . . . 34
6.3 Implementationdetails . . . . . . . . . . . . . . . . . . . . . . . . 35
6.3.1 Datamodelanddomainobjects . . . . . . . . . . . . . . . 35
6.3.2 Userinterfacestructureanddesignapproach . . . . . . . . 36
6.3.3 Developmenttoolsandprocess . . . . . . . . . . . . . . . . 37
7 Demonstration 38
7.1 Addressingcomplexityandhumanerror . . . . . . . . . . . . . . . 38
7.2 Solvingscalabilitylimitations . . . . . . . . . . . . . . . . . . . . 40
7.3 Automatingfinancialdataretrieval . . . . . . . . . . . . . . . . . . 41
7.4 Centralizedtrackingacrosscategories . . . . . . . . . . . . . . . . 43
7.5 Integratedandefficientreporting . . . . . . . . . . . . . . . . . . . 45
8 Evaluation 48
8.1 Task-basedusertesting . . . . . . . . . . . . . . . . . . . . . . . . 48
8.2 Stakeholderinsightsfromquestionnaire . . . . . . . . . . . . . . . 49
8.2.1 Generalimpressions . . . . . . . . . . . . . . . . . . . . . 49
8.2.2 Featuresatisfaction . . . . . . . . . . . . . . . . . . . . . . 49
8.2.3 Problem-solvingimpact . . . . . . . . . . . . . . . . . . . 50
8.2.4 Suggestionsandfutureimprovements . . . . . . . . . . . . 50
8.3 Comparisontobaseline . . . . . . . . . . . . . . . . . . . . . . . . 50
8.4 Evaluationagainstdesignobjectives . . . . . . . . . . . . . . . . . 51
9 Discussion 54
9.1 Summaryofresultsandimpact . . . . . . . . . . . . . . . . . . . . 54
9.2 Limitationsofthesolution . . . . . . . . . . . . . . . . . . . . . . 55
9.3 ReflectiononDSRM . . . . . . . . . . . . . . . . . . . . . . . . . 56
9.4 Opportunitiesforfuturedevelopment . . . . . . . . . . . . . . . . . 57
10 Conclusions 58
References 59
5

Symbols and abbreviations
Abbreviations
API ApplicationProgrammingInterface
DB Database
DS DesignScience
DSR DesignScienceResearch
DSRM DesignScienceResearchMethodology
FR FunctionalRequirement
PFM PersonalFinanceManagement
PoC Proof-of-concept
QA QualityAttribute
STD Self-DeterminationTheory
UI UserInterface
UX UserExperience
6

1 Introduction
1.1 Context and motivation
Peter Drucker said, "If you can’t measure it, you can’t manage it" highlighting the
importanceofdataindecision-making. Hamming’squote,"Yougetwhatyoumeasure"
representshowweguideourselveswithmeasuringthestepswetaketowardachieving
our goals. W. Edwards Deming presented the saying "In God we trust, all others
bring data" which is a reminder that we should base our decisions off data and not
assumptivebeliefs.
This holdstrue forPersonal Finance Management(PFM) whichrequires financial
literacy, motivation and structured planning to make informed financial decisions.
Studiessuggestthatpeoplewithhigherratesoffinancialliteracyaremorelikelyto
participateintypesofbehaviorsrelatedtosaving,investing,andavoidingunnecessary
financial mistakes (Lusardi and Mitchell 2014; Rajesh and Giridhar 2024). In
addition, globalsurveys suggestthat lowerratesof financialliteracy remainin many
demographics,particularlyyoungadults,women,andamonglowerincomeoreducation
levels(AtkinsonandMessy2012;LusardiandMitchell2014).
Financialknowledgealoneisnotenoughtocreatebehavioralchange. DiDomenico
et al. (2022) explains that autonomous motivation, driven by internal values and
interest,ismorestronglyassociatedwithsustainablefinancialhabitsandwell-being
thancontrolledmotivationwhichrelatestoexternalpressureorguilt. Furthermore,
Kaye et al. (2014) has shown that financial management behaviors are driven by
emotional,socialandexperientialmotivations,notjustrationalknowledge. Shafiee
et al. (2024) suggests that well-designed, personalized financial tools can increase
financial literacy and support decision-making, while still fulfilling an educational
andadvisoryrole.
While digital PFM tools aim to help users track expenses, manage budgets, and
visualizefinancialdata,theiradoptionremainslimited. Stefanovetal. (2024)found
thatonlyfew availabletools were ableto meetallconsumerneeds foreasierfinancial
management, especially in underrepresented regions. In addition, many tools only
offeroneservicetotheusers,suchasbudgeting,anddonotprovideeducationalcontent
whichwouldhelpraisetrusttofinancialservices(Tornoetal. 2021). Researchhas
shownthataddingpersonalization,gamifiedfeedback,andsimplifiedinteractionscan
improveuserengagementandfinancialself-efficacy(Bitriánetal. 2021; Cederberg
2013),yettheseelementsarestilluncommoninmainstreamapplications.
Thisthesisrespondstotheselimitationsbydesigningacentralizedpersonalfinance
application that consolidates financial data, supports user learning and motivation,
andofferstoolsforfinancialplanningandanalysis.

1.2 Objectives and scope
The goal of this study is to design and build a proof-of-concept of centralized
personalfinanceapplicationthathelpsindividualsmakeinformed,data-drivenfinancial
decisions. FollowingtheDesignScienceResearchMethodology(DSRM),thestudy
aims to identify user needs, create a customized solution, and evaluate its practical
relevanceandfunctionality. Theapplicationwasdevelopedforaprivatestakeholder
withreal-liferequirements.
Inparticular,theapplicationaimstoachieve:
• Consolidationoffinancialdataacrossassetclassesincludingcash,sharesand
realestatefrommultiplesourcesonasingleplatform
• Trackauser’snetworthdevelopmentovertimethroughvisualizeddata
• Provideclearvisualoverviewsoftransactionsandcashflowthroughtablesand
charts
• Improvetransparencyandaccessibilitybystructuringpersonalfinancialdatain
ascalable,easy-to-navigatesystem
• Provide breakdowns of the assets by categories and subcategories including
marketvalue,equity,countryattributionandmore
ThisworkcontributestothedevelopmentofpracticalPFMtoolsbyfocusingondata
integration,visualclarity,andactionableinsights. Italsodemonstratestheapplication
ofDSRM toguide artifactdevelopment anditerationbased onstakeholder’sfeedback
andevaluation.
1.3 Use of artificial intelligence tools
Artificialintelligencetools,includingChatGPT,wereusedtosupportthestructuring
and writing of this thesis. AI assistance was first used to help outline the overall
structureofthethesisanddecidingwhatcontentshouldbeincludedineachchapterand
section. Oncethestructurewasinplace,AIwasusedtohelpdraftsomeparagraphs
basedonpredefinedideas,bulletpoints,andnotes.
In the Literature review (Chapter 2), the process involved first highlighting and
collecting relevant information from selected academic sources. The material was
manuallyorganizedintoclearlydefinedsubsections. AItoolswerethenusedtohelp
compose coherent and logically structured paragraphs, ensuring that the collected
sourceswerepresentedundertheappropriatethemesandheadings.
Additionally, AI was used throughout the thesis to check that statements were
supportedbythecitedliteratureandtorefineclarity,grammar,andacademictone. All
AI-assistedcontentwasreviewed, edited,andfinalizedtoensureaccuracy, integrity,
8

andappropriatenessforacademicwork.
1.4 Thesis structure
This thesis consists of ten chapters. Chapter 1 introduces the research context,
motivation, andobjectives. Chapter2 reviews relevant literatureon financialliteracy,
personal finance planning, management tools, and DSRM. Chapter 3 presents the
research methodology. Chapters 4 to 8 follow the DSRM process: identifying the
problem,definingsolutionobjectives,designinganddevelopingtheproof-of-concept,
demonstratingitsuse,andevaluatingitseffectiveness. Chapter9discussesthebroader
impactoftheresultsandfuturedevelopmentopportunities. Chapter10concludesthe
thesisbysummarizingkeyfindingsandreflectingontheresearchoutcomes.
9

2 Literature review
Thischapterprovidesthetheoreticalbackgroundfortheresearchbyinvestigatingthe
threetopicsrelevanttothedevelopmentofacentralizedpersonalfinanceapplication.
First,itlooksintofinancialliteracyandbehavior,focusinghowknowledge,motivation,
and habits shape financial outcomes. Second, itlooks into personal financial planning
asastructuredprocessaimedatachievingfinancialgoalsthroughbudgeting,saving,
andinvesting. Third, itlooksintocurrentstateofpersonalfinancemanagementtools,
highlighting current capabilities, user needs, and design opportunities. Finally, the
chapterexplainsDesignScienceResearchMethodology(DSRM),tracingitsorigins,
artifacttypes,andstructuredresearchprocess,whichformsthemethodologicalbase
ofthisthesis.
2.1 Financial literacy and behaviors
Financialliteracyisessentialformanagingmoney,makinginformeddecisions,and
achieving long-term financial well-being. Rajesh and Giridhar (2024) argue that
low levels of financial literacy can lead to significant consequences related to the
accumulationofoverallwealth,suchasunsustainablelevelsofdebt,poorcredit,and
possibly even bankruptcy. Many people struggle with financial management, such
as, overspending, making poor investment decisions, borrowing too much money
unnecessarily, and failing to plan for retirement. They note that increased financial
literacyallowsindividualstohavebettersavingandspendingroutines,controltheirdebt
better,andachieveimprovedfinancialstrength. Likewise,LusardiandMitchell(2014)
confirm thatlow levelsof financialliteracyare presentinall populations,particularly
theelderlyandyouth. Theysaythatallpopulationsshowmajorgapsin certainareas,
such as, issues understanding interest rates, inflation, or risk diversification. They
statethathistorically,peoplereliedongovernment-managedpensionsandpaidlittle
attentiontofinancialplanningwhichdoesnotapplytodayanymore. Theauthorspoint
outtheconnectionbetweenfinancialilliteracyandriskierbehaviorssuchaslatebill
paymentsorexcessiveinterestcreditusage. Incontrast,financiallyliterateindividuals
reportmoreplanningforretirementandlong-termwealthaccumulation.
From the behavior side, Atkinson and Messy (2012) note that financial literacy
incorporates attitudes and habits that can lead to financial well-being. Their inter-
national survey concluded that people with better financial knowledge also display
better behaviors including budgeting, saving and timely bill payment. Individuals
exposedtowardlonger-termplanningarealsolikelyto adopthealthierbehaviorsin
theirfinancialpractices. Theresearchdemonstratednotabledemographicfindings:
womenscoredlowerthanmenonboththeknowledgeandbehaviorcomponent,and
middle-agedindividualsgenerallyoutperformedtheyoungerandolderagegroups.
Financialliteracyandeducationwerehighlycorrelated,butlow-incomeindividuals
sometimesshowedresistancetooutsideguidance.
Complementingthesefindings,Kayeetal. (2014)illustratesthatpersonalfinance
10

behavior isnot simply alogicalprocess. Rather, theemotional, culture, andrelational
contexts of how people manage money influences financial behaviors. Instead of
a complete, structured picture of their finances, individuals tend to piece together
financialinsightsthroughmoreinformalpractices,suchasonlyglancingthebalance
in their account or skimming last week’s transactions. This suggests a disconnect
betweenhowfinancialliteracyistypicallysupportedandhowpeopleactuallypreferto
engage with theirfinances. The findings show the importance of designingfinancial
tools that reflect real-life behaviors and habits, and also recognizing that financial
decision-making is deeply shaped by individual context and lived experience (Kaye
etal. 2014).
Motivation is another aspect to note. Di Domenico et al. (2022) apply Self-
Determination Theory framework to reflect on how autonomous, controlled, and
amotivatedmotivationrelatestofinancialknowledgeandoutcomes. Researchdemon-
stratedthatindividualswhoareautonomous,i.e. peoplewhoengagedinfinancialtasks
willingly, showed better financial knowledge, self-efficacy, and well-being. While,
amotivatedindividuals,i.e. peoplelackinginterestorfeeltheycannotmanagetheir
finances,weremorelikelytooverspendandreportedhavinglowerlevelsoffinancial
confidence. Whilebothautonomousandcontrolledmotivationwereshowtocorrelate
withsavingandinvesting,onlyautonomousmotivationhadaclearassociationwith
positivefinancialoutcomesfurthermitigatingtheimportanceofinternalmotivation
andsupportivefinancialbehaviors.
Finally, Lasmiatun (2024) examined how financial education shaped Generation
Z’sfinancialawarenessandhabits. Thestudyfoundthattheunderstandingandability
ofyoungadultstomanagemoney,strategicallyplan,andinvestwashigherforthose
who participatedin thefinancialeducation. Although, theunderstanding offinancial
competencyprimarilycamefrominformallearningonsocialmediaandthingslike
blogs,insteadofformalsources. Lasmiatun(2024)saidthatparticipantsvalueddigital
content that is presented in an interactive and visual format (infographic, videos,
interactive simulations)as they foundthe smallerchunks ofinformation andvisuals
easiertoengagewithandunderstand. Thissuggeststhatimprovingfinancialeducation
forGenerationZmayrequireintegratingmoreaccessible,digitalformatsthatalign
withtheirlearninghabitsandmediaconsumption(Lasmiatun2024).
2.2 Personal financial planning
Personal financial planning is a lifelong process designed to maximize the use of
income and assets, meet financial goals, and reduce uncertainty. Siegel and Yacht
(2009)describethisasanalogoustoplanninginotherareas: knowingwhereyouare,
knowingwhereyouwanttogo,andfiguringouthowtogetthere. Theygoontonote
thattherearemanyinterrelatedvariablesandtheuncertaintyoflifecancomplicatethe
planningprocess. Sincepersonalcircumstancesandtheeconomychangeovertime,
financialplanning has tobe sufficiently flexibleto dealwith change while pursuing
life-longgoals. Financialplanninginvolvescontinuallyreassessinggoals,considering
11

alternativesanddecidingifchangesneedtobemade(SiegelandYacht2009).
In building on this idea, Gitman et al. (2011) note that financial planning is
increasingly important given the context of a world in which we cannot expect
employer or government support to guarantee long-term security. They describe
financial planning as a systematic effort to organize a financial plan for personal
goals/values. Theirfinancialplanningmodelhassixbasicsteps: (1)identifyanddefine
financialgoals (2) develop financialstrategies(3) implementfinancial strategies (4)
createandmaintainbudgets(5)evaluateresultsusingfinancialstatements(6)revise
financialplansduetochangesinpersonalcircumstances,orunexpectedchallenges.
Whilesuccessisnotguaranteed,consistentandflexiblefinancialplanningcanimprove
thelikelihoodofsuccessinachievingfinancialsecurityandadaptingtotheunexpected
(Gitman et al. 2011). Huang (2016) states that financial planning is an important
skillintegratedinto dailylife, regardless ofhow muchfinancial considerationsaffect
peopleintheirdailydecisions, suchascostsbeingaffectedbyinterestrates,increases
inannualtuitionandothers. Thisisespeciallyimportantforyoungpeople,andcollege
graduates, experiencing independence in an expensive world with low income for
thefirsttime. Huang(2016)acknowledgedthatwhilesomepeoplefollowstructured
paths, and others adopt a more reactive method, financial planning is necessary for
eventual success. Similar to Gitman et al. (2011), she also divided the process to
six steps: (1) Identifying Smart Financial Goals, (2) Know Your Current Financial
Situations,(3)SpendingWiselywithaBudget,(4)ManagingtheCredit,(5)Saving
fortheFutureand(6)InvestingtheMoney.
IntheMalaysiancontext,LaiandTan(2009)investigatedhowindividualsengage
withdifferentareasoffinancialplanning. Theresultsindicatedthatwhilebudgeting
and investment planning is relatively well pursued, financial planning across other
areaslikeinsurance,retirement,andestateplanningareoftendisregarded. Specifically,
10%ofrespondentsremarkedthattheyplannedacrossallareasofpersonalfinance.
Despitethis,therearegenerallypositiveattitudestowardbudgetingandmoney,with
the conscious recognition of the importance of investment for long term financial
security. However, there were less positive attitudes towards retirement, as results
indicatedgreaterconsiderationonhealthandlifestylechanges. Inaddition,Laiand
Tan(2009)examinedjobstatusinfinancialplanning. Findingsindicatedthatemployed
andself-employedindividualsengagedinfinancialplanningmorethanthosewithout
stableincome,highlightingthatjobstatushasanimpactonplanningbehaviors.
ShahandBhatt(2014)studiedincomeallocation andinvestmentbehavioramong
residentsofthecityofAhmedabad,inthedistrictofGujarat. Findingsindicatedthat
individualstypicallyallocate45%ofincometoconsumption,saving25%,and15%
toinvestmentsandemergencyfunds,withsavingprioritiesoftheirchildren’sneeds,
housing, and to save taxes. In addition, respondents expressed that their preferred
investmentsarefixeddepositswithbanks,insuranceplans,andpublicprovidentfunds.
Regardinginvestmentbehaviors,malerespondentscertainlyfavoredinvestinginstock
markets,while female respondentstendedtoprefergold, bullion,andPPF investment
12

products respectively. The above trends may reflect a cautious and security based
financial planning behavior focused on meeting long term needs and awareness of
investmentrisk(ShahandBhatt2014).
2.3 Personal finance management tools
Personal finance management (PFM) applications have changed from being paper-
and-pencilorspreadsheet-basedsystems,tobeingadvancedwebormobiletools. As
Gafrikovaetal. (2015)demonstrate,althoughusingtraditionalpaper-and-pencil,or
spreadsheet,methodsoffersmaximizedfreedom,thedownsideisgreatertechnicalskill
andtimecommitment. Gafrikovaetal. (2015)tracedbackthatdedicatedPFMsoftware
started appearing in the 1980’s, and has since progressed into today’s specialized
web and mobile tools, many of which are now integrated into banking systems. A
keymilestonewasthelaunchofMint.comin2007,whichsetaglobalbenchmarkfor
onlinePFMtools. Despitethis,adoptionhasremainedlow. Citinga2012AiteGroup
surveytheyestimate58%ofU.S. consumershaveneverusedanddonotplantouse
PFMapplications, andonly13%of themwantedfinancialconsulting andplanning
from their financial institutions. In Poland, PFM tools embedded within banks are
relativelycommonbutoftenlimitedtointra-bankaccountmanagement,althoughwith
highersecuritystandards.
Stefanov etal. (2024)presented auser-centered designapproach fordevelopinga
mobilePFMappfocusingontheBulgariancontext,wherenoPFMsolutionscurrently
exist. In interviews and survey responses conducted by Stefanov et al. (2024), they
identified practices on how the users wanted to manage their finances: budgeting,
monitoredexpenses,investment planning,andstrategyplanning. Theysay thatmany
existingtoolsfallshortduetooverlycomplexinterfacesorlackofaccessibility. Based
on their analysis, they identified some desired functionalities: portable calculator,
currencyconverter, chartextraction,andbarcodescanning, allbundledontoa single
platform to enhance user experience and effective personal finance management.
The significance of design and usability is also verified by Cederberg (2013), who
researchedthePFMfeaturesyounguserspreferredwhenembeddedinbankingapps.
She conducted user interviews and prototype testing with their target market while
they used the PFM functionalities. Features that the respondents liked included
general income and spending diagrams, category-based pie charts, budget tracking
with monthly limits, alerts for nearing those limits, and visual planning of fixed
expenses. Users identified a desireforeasy-to-use applicationsand preferredminimal
manualinputwithautomatedcategorizationfeatures. Usersalsonotedaestheticswere
importantastheywantedapleasingandrecognizableuserinterface,astheybelieved
these types of tools would help them more effectively manage their finances due to
newinsight,control,andgoalsetting.
Looking atbroader range of tools, Torno et al. (2021) did a taxonomy and cluster
analysis on 170 PFM apps, finding ten separate archetypes. The clusters ranged
fromappsfocusedonfinancialnewsandassetmonitoring,toadvancedandmanual
13

budgetingtools,tofull-featuredmobilebankingplatforms. Mostappsrequiredinternet
accessand useraccountsandgenerally, offlinefunctionality waslimitedtoapps that
haveabasiccalculatorandmanualbudgetingpossibilities. Veryfewappsprovidean
advisoryoreducationalelement intheirservice. Withinthe clusters,examples such
as"InvestingwithAdvice"offerpredictiveanalysisandproductswhileothers(e.g.,
"TransactionAuthorisation")arenarrowerinscope. Despitethewidefunctionality
spectrum, Torno et al. (2021) highlight a lack of educational content across most
apps,suggestingamissedopportunityforfinancialserviceproviderstoimproveuser
engagementandtrustthroughbetterfinancialliteracytools.
Herralaetal. (2023)explorehowPFMsystemscanbothempowerandconstrain
young users, using empathy-based storytelling (MEBS) as a qualitative research
methodwith191universitystudents. Participantshadsignificantpositiveexperiences:
improvedbudgetingability,improvedsavingsandinvestingpractices,andbetteraccess
tolendinganddigitaltransactions,allfactorsthatcontributetopersonalagencyand
long-termplanning. Therewerealsosignificantnegativeexperiences: spontaneous
spending,difficultygraspingthevalueofdigitalmoney,andover-indebtednessdue
to ease of credit. Other concerns included stress regarding privacy, surveillance,
cybersecurity,overloadoninformation,andover-relianceontechnologyanddigital
competence. ThestudyconcludesthatwhilePFMtoolscanpromotefinancialwell-
being, they may also reinforce behavioral control and cognitive overload when not
appropriatelydesignedorsupported.
Gamification might offer a partial way around these problems. Bitrián et al.
(2021) investigate how gamified features promote user motivation by combining
self-determinationtheory(SDT)withthetechnologyacceptancemodel(TAM). They
evaluated 208 Mint app users and conclude that budgeting, alerts, credit score and
tracking opportunities are features that promote competence and autonomy. These
featuresetsencouragedusers’motivationtousetheappandresultedinstrongperceived
usefulness and ease-of-use. Bitrián et al. (2021) suggest independent goal setting,
visualdisplayofprogressandbudgets,realtimenotifications/alerts,andrewardsare
elementsthatappdesignerscanintroducetoimproveuserautonomyandcompetence.
Therecommendedaspectsforboththeappdesignerandusersuggestthepotentialfor
long-termengagementandasenseofempowermentfortheuser.
Incontinuingwithagenerationalperspective,Handayaniet al. (2024)described
fintechadoptionfrom amillennial perspective sincetheygrewupwith technology as
anormalwaytointeractwiththeworld. Theyexaminedmillennialsattitudestoward
technology-basedfinancialservicesanddistributedanonlinesurveyto120usersof
personal finance apps. The authors felt that personal finance apps helped provide
visibilitybyenablinguserstoseetheirincome,expenses,andbalancesinreal-time
thatsupportedtheirabilitytotracktheirspendingbehaviour,settheirgoals,andplan
theirfinances. Theypresentedkeyfeaturesthatwereseenasmotivatingfactorssuch
as automatic expence tracking, bill reminders, and personalized advice. Concerns
aboutdatasecurityandprivacyononlineplatformsdidstillexist. Fintechapplications
14

have become central to millennials’ financial behavior, and their growing usage is
pushingtraditionalfinancialinstitutionstoadaptandintegratesimilartechnologiesto
staycompetitive(Handayanietal. 2024).
Finally,Frenchetal. (2021)evaluatefourPFMappsdevelopedcollaborativelywith
creditunionsand testedvia arandomizedcontrolledtrialwith500membersofDerry
CreditUnioninNorthernIrelandwhere260wereinthetreatmentgroupand240in
thecontrolgroup. Thetreatmentgroupshowedsmall,significantincreasesinfinancial
literacy, ability to budget, confidence to budget, and ability to plan for unexpected
bills. The treatment group did not show significant increases to digital literacy or
behavioural change (i.e., saving money regularly). In terms of use, expectable,
descriptive analysis showed that 45% of users used the apps regularly (5 or more
times),32%usedtheappinfrequently,and23%didnotusetheapp. Forthenon-user
reasonsincludedforgetfulness,relevance,andrestrictiveness. Still,mostusersrated
theappspositively,indicatingstrongpotentialiffuturedesignscanaddressbarriersto
usageandengagement.
Insummary,theeffectivenessofPFMtoolsliesnotonlyintheirtechnicalcapabilities
butalsointheirabilitytosupportuserbehavior,motivation,andemotionalwell-being.
Integratedanduser-friendlytoolsthataddressprivacyconcerns,offerpersonalized
insights, and engage users in meaningful way are most likely to foster long-term
financialstabilityandinclusion.
2.4 Design science research
De Sordi (2021) describes Design Science Research Methodology (DSRM) as an
approachemergedintheearly2000sto provide amorestructured, scientificbasisfor
the development ofinformation systems. Essentially, DSRM aims to solve real-world
problems through designing artifacts in a systematic way. Vaishnavi and Kuechler
(2015) notes that design is more than simply describing and they define design as
purposeful creationofnew artifacts,where anartifactcan takemanyformsandtypes.
Theysaythata designisa routinein asituationwhen you haveenough knowledgeto
createwithouttheneedtodeveloporextendknowledge,versusadesignbeinglabeled
innovative when it manifests any form of new knowledge. They continue that the
subjectofDesignScience(DS)isfocusedontheconceptsandprocessesfollowedto
produceartifactswhichcompriseconstructs,models,methods,andinstantiations. This
thencomprisesthepracticalformsofknowledgeneededtosolveparticularfunctional
needs. Conversely,DesignScienceResearch(DSR)focusesonthescientificstudyof
thedesignprocessincludinganalysis,reflection,abstraction,andevaluation. Vaishnavi
andKuechler(2015)explainthatDSRcontributestoknowledgebyinvestigatingand
documentinghowartifactshaveevolvedthroughDSRIandhowartifactsachievetheir
intendedusefunctionwithincontexts.
De Sordi (2021) also describes the difference between natural science, which
develops knowledge to examine either physical or abstract phenomena that already
15

exist, and artificial science, which develops knowledge based in context to develop
the creation of human artifacts that aim to solve problems for human populations.
AccordingtoDeSordi(2021),onedefiningcharacteristicofartificialscienceisafocus
on attempting to understand the context ofthe artifact, in terms ofthe environment
in which will be used or the individual human characteristics and needs that may
impact the use of the artifact. As referenced by De Sordi (2021, p. 9), “Design
involvesdesigningsomethingthatisasolutiontoaneed,whicharecalledartifacts.”
Artifacts developed using DSRM can take many forms. Vaishnavi and Kuechler
(2015)defineconstructs,astheconceptsandtermstodescribeproblemsandsolutions,
which may actually evolve in the research. Models are organized representation
of the relationships among constructs, which may be useful not perfectly accurate.
Methods are the procedures, algorithms, or techniques used to accomplish desired
ends. Instantiationsareartifactconstructs,models,ormethodsusedinpractice,which
mayoccurpriortotheorybeingformed(VaishnaviandKuechler2015).
Amongthevariousprocessmodelsproposedforconductingdesignscienceresearch,
the most widely adopted is from Peffers et al. (2007), presented in Figure 1. Their
modelwasdevelopedtoaddressthelackofstructureinearlyDSReffortsandhassince
becomeafoundationalframeworkin informationsystemsresearch. Ithasastructured
six-stepprocess: (1)problemidentificationandmotivation,(2)defineobjectivesfora
solution,(3)designanddevelopmentoftheartifact,(4)demonstrationoftheartifact
inuse,(5)evaluationoftheartifact’sperformance,and(6)communicationofresearch
results. This structuredprocesswill form themethodological basisofthis thesis,and
isfurtherexplainedinChapter3.
DesignScienceProcessModel(Peffersetal.,2007,p. 54)
Figure 1:
Inadditiontostructureandguidelines,DSRalsorequiresanunderstandingofwhat
a valid contribution means. According to Hevner et al. (2004), design science in
information systems requires the replication of artifacts that are not only novel and
effective, but also, that have been evaluated objectively in the context of use. The
authors provide a balance to the effective usability versus research methodological
16

rigor by claiming utility as the artifact’s valued contribution. In another words, the
artifact’sreasonablewaytoaddressausableproblem. Thebalancebetweentopical
relevance and rigor of method is one of the strengths of design science research,
andmakesDSRMparticularlyrelevantinappliedcontexts,suchaspersonalfinance
technology.
Inconclusion,DSRMprovideamethodtotheoreticallyshapeapracticalsolutionto
complexproblemsusingiterativeartifactdevelopment. DSRMencouragesincluding
feedbackfromusers,aswellascontextualconstraints,andformalevaluation. These
elementscontributetoappropriatenessofapplyingDSRMtodevelopamoreengaging
centralpersonalfinanceapplication,presentedinthisthesis.
17

| 3 Research | methodology |     |
| ---------- | ----------- | --- |
Thischapterdescribestheresearchmethodologyusedinthisthesis,whichfollowsthe
DesignScience ResearchMethodology(DSRM). Thechapterexplainshoweachof
thesixDSRMphaseshasbeenutilizedwithinthescopeofthisstudy,fromproblem
identification to communicating results. In addition, the last section provides the
justificationforwhyDSRMwasselectedasthemethodologyforthisthesis.
| 3.1 DSRM | actions |     |
| -------- | ------- | --- |
This thesis follows the DSRM proposed by Peffers et al. (2007), which consists of
six structured steps for developing and evaluating innovative artifacts. Each step is
describedindetailbelow.
| 3.1.1 Problem | identification | and motivation |
| ------------- | -------------- | -------------- |
ThefirststepofDSRM,ProblemIdentificationandMotivation,focusesondefininga
research-worthyproblemthatholdsbothacademicsignificanceandpracticalrelevance
(Peffersetal. 2007). AsDeSordi(2021)explains,thisrequiresdirectengagementwith
thefieldtoensurethattheidentifiedchallengereflectsrealuserneedsandcontextual
constraints.
Usability, lack of features, and low demand have all been identified as the most
significant limitations facing personal financial management (PFM). Torno et al.
(2021)discoverthatthemajorityofmobilePFMappsfocusonnarrowtasks,suchas
keepingabudgetorfacilitatingpayments,andrarelyincludeeducationalcontentor
considerincorporatingholisticfinancial planning. Herralaet al. (2023)illustrate that
whilePFM toolscanempowerusersandplacethem incontroloftheirfinanciallives,
theyalsoruntheriskofgeneratinguserstress,impulsivebehaviors,andcreateasense
ofsurveillance.
Tovalidatetheprobleminthisstudy,astructuredquestionnairewasconductedwith
the stakeholder (Table1), using open-endedquestionsto investigate challengesand
featuregaps. TheanalysisofthefinalproblemdefinitionispresentedinChapter4.
Problemidentificationquestionnaire
| Q1: Howdoyoucurrentlymanagepersonalfinances?                 |     |     |
| ------------------------------------------------------------ | --- | --- |
| Q2: Howoftendoyouusethecurrentsolution?                      |     |     |
| Q3: Whatdifferentpurposesdoyouuseitfor?                      |     |     |
| Q4: Whatisthemostchallengingaspectofusingthecurrentsolution? |     |     |
Q5: Arethereanymissingfeaturesorfunctionalitiesyouwishexisted?
| Q6: Howoftendoyouencountererrors,delays,orinconsistencies? |     |     |
| ---------------------------------------------------------- | --- | --- |
| Q7: Howwouldyouratetheuserexperience(UX)andeaseofuse?      |     |     |
Questionsusedintheproblemidentificationquestionnaire
| Table | 1:  |     |
| ----- | --- | --- |
18

3.1.2 Define the objectives for the solution
ThesecondstepofDSRM,DefineObjectivesfortheSolution,involvessettinggoals
that respond directly to the identifiedproblem, whileensuring theyare feasible and
relevant (Peffers etal. 2007). Objectives canbe bothquantitative, suchas measurable
improvements,andqualitative,suchasaddressinguserfrustrationsorunmetneeds. As
De Sordi(2021) notes, this stageincludes assessing the currentstate ofthe problem,
reviewingexistingtools,andidentifyinghowtheproposedartifactcanofferasuitable
solution.
Toformalizethesolutionscope,thesystemrequirementsweredividedintofunctional
andnon-functionalcategories. Functionalrequirementsdefinewhatthesystemshould
do, such as authentication, data processing, and reporting, while non-functional
requirementsspecifyhowthesystemshouldperform,includingitsreliability,security,
and responsiveness (Ironhack 2024). This structure helps ensure the artifact meets
bothusabilityexpectationsandtechnicalstandards.
Tofocusdevelopmentonthemostcriticalfeatures,aprioritizationoftherequire-
ments was conducted with the stakeholder. The MoSCoW method (Brush 2023), a
common approachin Agile development, was adapted to suitthe project context. The
customized scale, shown in Table 2, includes four levels: Must have, Should have,
Nicetohave,andOptional.
Prioritization Description
Musthave Mandatoryinthefinalproduct
Shouldhave Essentialbutnotabsolutelyvital
Nicetohave Usefuladditions,butnotnecessary
Optional Couldbeaddedlater
Customprioritizationscaleforthecontextcase
Table 2:
This customizedranking allowedthe stakeholderto distinguishcore featuresfrom
those better suited for future iterations. Requirements were labeled as functional
requirements(FR)orqualityattributes(QA),andnumberedbypriority,withlower
numbers indicating higher importance. The requirements are presented in detail in
Chapter5.
3.1.3 Design and development
The third step of DSRM, Design and Development, involves specifying the system
architecture and core functionality, followed by the implementation of the artifact
(Peffersetal. 2007). AccordingtoDeSordi(2021),thisphaseisiterativeandincludes
ongoingdevelopmentandevaluationtoensurethattheartifacteffectivelyaddressesthe
definedproblem. Continuousrefinementbasedonstakeholderfeedbackisencouraged
toenhancebothfunctionalityandrelevance.
19

Architecturaldecisionsweremadebased ontheprioritized requirements. Enstrom
(2018)definesArchitecturalDecisions(ADs) assignificant,documentedchoicesthat
influence the system’s structure, including software technologies, data integration,
andmaintainabilitystrategies. Thesedecisionsaredistinctfromroutinedesigndetails
andserve toalignthe system withlong-termgoalsand constraints(Enstrom 2018).
ThekeyADsforthisprojectarepresentedinChapter6.
After defining the architecture, the artifact was developed in iterative cycles.
Feedback from the stakeholder was used to refine features, user workflows, and
interfaceelements. ThisismotivatedfromthefindingsfromliteratureasbothStefanov
etal. (2024)andCederberg(2013)notedtheimportanceofusability,simplifiedand
invitinginterface,andcentralizedfunctionality.
3.1.4 Demonstration
ThefourthstepofDSRM,Demonstration,involvesshowingthatthedevelopedartifact
can solve at least one instance of the identified problem (Peffers et al. 2007). This
may involve experimentation, simulations, case studies, or other forms of proof.
As described by De Sordi (2021), this phase aims to validate whether the artifact’s
structure, procedures, and outputs address the problem in a meaningful way, even
if full performance optimization has not yet been achieved. De Sordi (2021) also
notesthatdemonstrationissometimesincorrectlyreportedasevaluationinacademic
studies,especiallywhentheartifactisstillindevelopment.
Inthisthesis,demonstrationwasusedtoshowhowtheartifactaddresseskeyissues
identified during stakeholder analysis. These included fragmented tools, repetitive
manual updates, and limited trust in the accuracy of financial data. These same
challenges were also noted in the literature. Gafrikova et al. (2015) mentions that
spreadsheet-basedsolutionsrequiretimeandtechnicalskills. Cederberg(2013)found
that usersmight stopusing the tool ifit requirestoo much manualinput, encouraging
automation. Additionally,Herralaetal. (2023)foundthatfinancialtoolsperceivedas
unreliable or difficult to use may increase user stress and undermine their sense of
control.
Thedemonstrationpresentsthefollowingcapabilitiesofthesystem:
• Addressingcomplexityandreducinghumanerror
• Solvingscalabilitylimitations
• Automatingfinancialdataretrieval
• Providingcentralizedtrackingacrossfinancialcategories
• Deliveringintegratedandefficientreporting
20

3.1.5 Evaluation
ThefifthstepofDSRM,Evaluation,assesseshowwelltheartifactsolvestheidentified
problem bycomparing itsintended objectives withthe actual outcomes (Peffers etal.
2007). Thisstepinvolvesanalyzingtheartifact’sperformance,usability,andfunctional
alignmentwithuserneeds. Evaluationisimportantfordeterminingwhethertheartifact
worksasintendedinreality. DeSordi(2021)explainthatthereareartificialevaluations
occurring under isolated or theoretical conditions, and naturalistic evaluations that
occur within real environments, with real users, and real problems. Naturalistic
evaluationsarealignedwiththefundamentalprinciplesofdesignscience,particularly
inapplieddomains.
Inthisstudy,theartifactwasevaluatedusingfourdifferentmethods. First,task-based
usertestingwasconductedtoassessusabilityandalignmentwithexpectedworkflows.
Thestakeholderperformedtypicalusagescenariosindependentlyontheirowndevice
while being observed. This allowed for direct feedback on task completion, design
effectiveness,andinterfaceclarity. ThescenariosarelistedinTable3.
Usertestingtasks
T1: Addanewtransactionforeveryassetcategoryandreviewupdated
networth
T2: Viewandinterpretassetdistributionusingpiechartsandassettables
T3: Add an expense and income and review the updated cash flow
visualization
T4: Generateafinancialreportforthepastthreemonths
Task-basedusertesting
Table 3:
Following the test session, the stakeholder completed a structured evaluation
questionnaire in similar format as in problem identification. The questions were
grouped into four categories: general impressions, feature satisfaction, problem-
solving,andsuggestionsforimprovement(Table4).
21

Evaluationquestionnaire
Generalimpressions
Howintuitivedidyoufindtheapplicationinterface?
Wasiteasytofindandusethekeyfeaturesyouneeded?
Featuresatisfaction
Howsatisfiedareyouwiththeassettrackingfunctionality?
Howsatisfiedareyouwiththecashflowtrackingfunctionality?
Doyoufeelthevisualizations(charts,tables)arehelpfulandinformative?
How useful is the PDF report generation compared to your previous
manualprocess?
Problemsolving
Towhatextenthasthissolutionreducedmanualworkcomparedtoyour
oldsystem?
Doyoufeelthissolutionhelpsyouavoiderrorsorinconsistencies?
Hasyourconfidenceinyourfinancialdataimproved?
Suggestionsandimprovements
Isthereanythingmissingyouwouldexpectinafullsolution?
Whatwouldyouimproveinfutureversions?
Questionsusedintheevaluationquestionnaire
Table 4:
Inadditiontocollectingqualitativefeedback,theevaluationincludedacomparison
with the stakeholder’s baseline system. This helped identify gains in automation,
usability, and reporting quality. Finally, an analytical review was performed by
checking how wellthe implementedsolution satisfiedthe original designobjectives
fromearlierDSRMstages. TheevaluationresultsarepresentedinChapter7.
3.1.6 Communication
ThesixthandfinalstepofDSRM,Communication,focusesonsharingtheresearch
outcomeswithbothacademicandprofessionalaudiences. AccordingtoPeffersetal.
(2007, p.92), “Communicate theproblemand itsimportance, the artifact, itsutility
and novelty, the rigor of its design, and its effectiveness to researchers and other
relevant audiences, such as practicing professionals, when appropriate.” De Sordi
(2021)highlightsthateffectivecommunicationinDSRmustbetailoredtoitsaudience.
Hesaysthatforpractitioners,theemphasisisontheartifact’spurposeandpractical
utility. Forresearchers,thefocusisonpresentingthedesignprocess,structure,and
evaluation outcomes to ensure methodological rigor and reproducibility (De Sordi
2021).
ThisthesisrepresentsthecommunicationphaseoftheDSRMprocess. Itdocuments
all stages of the research, beginning with problem identification and continuing
throughdesign,development,demonstration, andevaluation. Theaimis topresent
the motivation for the work, the rigor of its execution, and its contribution to both
22

researchandpractice. By clearlyarticulatingthemethodology andresults,this thesis
contributestoongoingdiscussionsaboutthedesignofpersonalfinancetoolsandthe
practicalapplicationofDSRMtoreal-worldchallenges.
3.2 Motivation for DSRM
DSRM is well suited for this thesis due to its structured and iterative process for
developingandevaluatingartifactsthataddressreal-worldproblems. Thisstudyaims
tocreate aproof-of-concept(PoC)of personalfinancemanagementapplication that
fulfills a stakeholder’s specific needs by using automation and data integration to
providebetterfinancialinsight. DSRMprovidesanorganizedandsystematicapproach
asan avenueto develop, validate andrefinesuchan artifactensuringits effectiveness
andrelevanceinpractice. ThiswasalsopointedbyTornoetal. (2021)whostatedthat
designscienceresearchisapromisingpracticetodevelopinnovativeITartifacts.
Themethodologyisspecificallyintendedforresearchwherethegoalistoconstruct
and evaluate artifacts that extend existing solutions or introduce new functionality
(Peffers et al. 2007). As Hevner et al. (2004) explains, design science research is
most effective when artifacts are developed in response to clearly defined business
needs and evaluated within real-world contexts. This aligns with the aims of this
thesis,whichaddresseslimitationsincurrentfinancialtrackingtoolssuchasmanual
spreadsheetsthatlackscalability,automation,andintegration. ThroughDSRM,these
limitationscan besystematically addressedusingan iterative development process.
Thesix-phasestructureprovidesatransparentdevelopmentroadmap,makingiteasier
totrackprogressandvalidatedesigndecisions.
DSRMdiffersfrompurelytheoreticalapproachesbyincludingdemonstrationand
practical evaluation. Because this project involves a real stakeholder with specific
financialtrackingneeds,themethodologysupportscontinuousengagementtoensure
thattheresultingsolutionmeetsactualuserexpectations. AsnotedbyDeSordi(2021),
practitioner involvement strengthens both academic rigor and real-world applicability.
Theevaluationphaseallowstheartifacttobeassessedagainstpredefinedobjectives
and revised if necessary. Since the goal of the thesis is to develop a PoC rather
than a production system, DSRM also allows for design flexibility and exploration of
feasibility without requiring full deployment. In particular, the Demonstration phase
enablestargetedtestingofcorefunctionalityinacontrolledsetting,helpingconfirm
thesolution’seffectivenessbeforefurtherdevelopment(Peffersetal. 2007;Hevner
etal. 2004).
23

| 4 Problem |     | identification |     | and motivation |
| --------- | --- | -------------- | --- | -------------- |
This chapterpresents the problemdescription thatthe proof-of-conceptapplication
aims to address. It begins with insights gathered from a structured questionnaire
conducted with the stakeholder, followed by a detailed description of the current
financial management approach and its associated challenges. Finally, the chapter
explainsthemotivationfordevelopinga new solution,based onthelimitations and
problemsidentifiedintheexistingsystem.
| 4.1 Stakeholder |     | insights | from | questionnaire |
| --------------- | --- | -------- | ---- | ------------- |
To gain a deeper understanding of the problem, a structured questionnaire was
conducted with the stakeholder, as introduced in Chapter 3.1.1. Several challenges
werefoundfromthefinancialmanagementapproachbasedontheresponses.
| 4.1.1 Current | financial | management |     | approach |
| ------------- | --------- | ---------- | --- | -------- |
Thestakeholderusesmultiplefinancialtoolstotrackincome,expenses,andinvest-
ments. Theirprocessincludes:
• Tools used: A combination of Spendee (for expense tracking), multiple bank
accountsacrosstwocountries,GoogleSheets(forsharepriceandexchangerate
tracking),andseveralExcelspreadsheetsforrealestateandmortgagetracking.
• Manualdataentry: Financialdataisperiodicallyfetchedfromvarioussources
andconsolidatedintoa“master”Excelfile,inusesince2014.
• Financial reporting: Quarterly and yearly reports are generated manually by
analyzingdataandproducinggraphs.
| 4.1.2 Frequency |     | of use |     |     |
| --------------- | --- | ------ | --- | --- |
Thestakeholderengageswiththefinancialsystematvaryingintervals:
| • Daily:  | TrackingexpensesinSpendee.        |     |     |     |
| --------- | --------------------------------- | --- | --- | --- |
| • Weekly: | UpdatingandmaintainingExcelfiles. |     |     |     |
• Quarterly: Conductingafullfinancialreviewandgeneratingreports.
| 4.1.3 Challenges |     | with the current |     | system |
| ---------------- | --- | ---------------- | --- | ------ |
Thestakeholderidentifiedthefollowingmajorissues:
• Complexityandhumanerror: Thesystemhasbecomedifficulttomaintainand
pronetomistakes.
24

• Scalability limitations: Excel structures struggle to handle growing financial
dataneeds.
• Lack of automation: No integration with online sources and updates must be
donemanually.
• Reportinginefficiencies: Thequarterlyreportprocessistime-consumingand
fragmented.
4.1.4 Desired features for an improved solution
Thestakeholderexpressedtheneedfor:
• Moreautomation: Asystemthattrackskeymetricswithminimalmanualeffort.
• Better data integration: Automatic synchronization with sources like stock
prices,exchangerates,andbanks.
• Acentralizedplatform: Asinglesystemcombiningallfinancialaspects.
• Enhancedaccuracy: Reducedhumanerrorandmorereliabledata.
4.1.5 Stakeholder reflections
Thestakeholdersummarizedtheirconcernsasfollows: "Thewholeprocessisgetting
overly complex, resulting in a higher probability of human error impacting data
quality. Any changes made to the document might break something due to complex
dependenciesacrossdifferentdatatabs."
AlthoughtheyfindExcelsomewhatenjoyableandfamiliar,theyacknowledgethe
system is not user-friendly for others and is increasingly difficult to manage. As
they put it: "For me, it is somewhat of a relaxing experience, but it is starting to
feeloverwhelmingbecauseoftheinaccuraciesandgapsthathindermefromgetting
accuratedata."
4.2 Problem description
Thestakeholderhastrackedincome,expenses,andinvestmentsforoveradecadeusing
acombinationofspreadsheets,financialapplications,andmanualdatacollection. Over
time, this system evolved to support detailed financial analysis, including quarterly
and yearly reporting. However, asfinancial data hasgrown involumeand complexity,
maintainingthesystemhasbecomeincreasinglydifficult.
The current setup involves multiple tools: Spendee for expense tracking, bank
accounts across two countries, and Excel spreadsheets for managing real estate
investments, mortgages, and stock portfolios. These fragmented sources require
25

manualconsolidationintoa“master”Excelfile. Datamustbeperiodicallyfetched,
entered, and processed by hand, resulting in a time-consuming workflow that is
increasingly prone to error due to complex interdependencies across formulas and
sheets.
Themainchallengesoftheexistingsysteminclude:
• Scalabilitylimitations–Excelstrugglestoaccommodatetheincreasingvolume
andcomplexityoffinancialdata.
• High risk of error – Manual updates to stock prices, exchange rates, and
balancesintroduceinconsistenciesandinaccuracies.
• Lackofautomation–Nointegrationwithonlinefinancialdatasourcesrequires
frequentcopy-pasteoperationsandmanualdataentry.
• Inefficient reporting – Quarterly reporting involves multiple manual steps:
collectingdata,updatingformulas,generatingcharts,andcompilingsummaries.
The stakeholder is very sophisticated in their financial management, but as their
system complexity and fragmentation grow, inefficiencies and the risk of error has
increased. As many of the authors note, working with disparate tools or manual
processescreatesusability issues,detersengagement,and leadstoerrorsinfinancial
decision-making (Gafrikova et al. 2015; Torno et al. 2021; Stefanov et al. 2024).
Research also shows that even knowledgeable users cannot maintain their desired
financial behaviours (or make decisions) when the available tools do not simplify
their decision-making or provide timely feedback related to their current financial
goals(AtkinsonandMessy2012;Kayeetal. 2014;Cederberg2013). Thisbehaviour
supports the concepts of integrated ease of use, automation, real-time data, and
supportingfeedbackloopstowardtheestablishmentofhabits,allofwhichwerealso
requested by user participants in the most recent fintech and PFM adoption studies
(Bitriánetal. 2021;Handayanietal. 2024)
4.3 Motivation
Thestakeholder’sdifficultiesrepresentawiderdemandforpersonalfinancetoolsthat
combine automation, accuracy, and usability. Their current system allows them to
trackallaspectsoftheirfinancesingreatdetail,though,itisbecomingmoreandmore
difficultto sustain, as well asrequiring scaling. Thestakeholderhas notconsidered
commercial tools, because the stakeholder believe their needs to be really specific,
they would be unable to find an off-the-shelf product that fulfilled their needs. It is
notedbyStefanovetal. (2024),thattheabsenceoflocalizedtools(e.g. applications
inBulgarian)couldalsoleadtounmetexpectationsforusersincertainregions. Torno
etal. (2021)alsonotethatmostpersonalfinanceapplicationstendtofocusonasingle
function (budgeting versus payments) than being a solution for everything, and as
such,usersoftenneedtoresorttosomeothermethod,forexampleuseofspreadsheets.
26

Besidesmissingfeatures,manyexistingtoolsdonotofferacompletesolutionand
forceuserstomanagetheirfinancesacrossseveralseparateapps. Whileautomation
was recognized as a major priority, the stakeholder also indicated that accuracy
and completeness are critical aspects of their financial data. They said that without
these, they may not justify the expense of moving to another system in the future.
This viewpoint is aligned with Cederberg (2013), who found thatusers would often
abandontoolsthatrequiredexcessivemanualefforteveniftheyprovidedsomelevel
ofautomationortracking.
Animprovedsolutionshouldaddressthefollowingkeyneeds:
• Automatedfinancialdataretrievaltoeliminaterepetitivemanualupdates.
• Centralizedtrackingoffinancialdataacrossmultipleaccountsandinvestment
platforms.
• Integrated analytics and reporting to generate insights with minimal user inter-
vention.
• Enhancedaccuracyandreliabilitytoreducetheriskofcalculationerrors.
The motivation for this research is based on creating a scalable personal finance
systemthatcanimprovedatareliability,reducemanualeffort,andallowindividualsto
makeinformeddecisions. Theseprioritiesmatchtherecommendationsintheliterature
forcreatingtoolsthatnotonlyautomateanddofinancialtasks,butcanmotivateusers,
givefeedback,andsupportthefinancialgoalsoftheuser(Bitriánetal. 2021;Shafiee
et al. 2024). While some studies also mention potential stress or overreliance on
digitalsystems,theynotetheimportanceofuser-centeredandemotionallysupportive
design(Herralaetal. 2023).
27

| 5 Defining | objectives |     | for the | solution |     |     |
| ---------- | ---------- | --- | ------- | -------- | --- | --- |
This chapter defines the objectives of the proposed solution based on the problem
analysis and stakeholder needs presented in Chapter 4. It presents both functional
andnon-functionalrequirementsthatguidethedevelopmentoftheproof-of-concept
application. Theserequirementsarethenprioritizedtoensurethatthemostcritical
featuresareaddressed.
5.1 Requirements
Thefollowingrequirementsareintendedtoresolvethemajorproblemsandmotivations
explainedinChapter4. Theserequirementsreflectuserneedsandincorporatesomeof
bestpracticesinsoftwaredevelopmentandPFMdesign. Therequirementsarerelated
topracticesmentionedintheliteraturewherefragmentedandmanualsystemshave
beenshowntobeinefficientandcreatecognitiveburdenandlowusability(Gafrikova
et al. 2015; Herrala et al. 2023). In contrast, research also highlights that effective
personalfinancetoolsbuildlong-termengagementbyprovidingautomatedfeatures,
availability, ease of use, and tools to create engagement and maintain motivation
| (Bitriánetal. | 2021;Cederberg2013). |     |     |     |     |     |
| ------------- | -------------------- | --- | --- | --- | --- | --- |
The requirements are divided into two main categories: functional and non-
functional. Tables 5 and 6 present a summary of each, including descriptions, user
stories,andacceptancecriteriathatdefinewhentherequirementisconsideredfulfilled.
The functional requirements focus on features that support an understanding
of financial visibility, decision making, and operational efficiency. For example,
dashboards, tags, and reporting features. These features were requested by the
stakeholder, and research also suggests that clear goal-oriented feedback increases
| engagementandpersonaloversight(Shafieeetal. |          |           |     | 2024).     |     |     |
| ------------------------------------------- | -------- | --------- | --- | ---------- | --- | --- |
| Functional                                  | require- | Userstory |     | Acceptance |     |     |
ment
Presentreal-timecap- "As a user, I want to see the Thesystemfetchesup-to-date
italinformation real-time value of all my as- stock prices and displays the
|     |     | sets." |     | real-time | value of all | tracked |
| --- | --- | ------ | --- | --------- | ------------ | ------- |
assets.
User interface(Desk- "Asauser,Iwanttobeableto Theapplicationprovidesare-
topandmobile) add/update/viewmy financial sponsive user interface that
|     |     | data from | mobile and | desk- works    | on both desktop | and |
| --- | --- | --------- | ---------- | -------------- | --------------- | --- |
|     |     | top."     |            | mobiledevices. |                 |     |
Datavisualizationof "Asauser,Iwanttoseehow Theapplicationdisplaysinter-
capitalandstatistics myassetsaregrowinginaway active visualizations, such as
|     |     | that supports        | me in | making charts              | and tables, represent- |     |
| --- | --- | -------------------- | ----- | -------------------------- | ---------------------- | --- |
|     |     | financialdecisions." |       | ingassetgrowthandfinancial |                        |     |
trends.
28

| Functional | require- | Userstory |     | Acceptance |     |     |
| ---------- | -------- | --------- | --- | ---------- | --- | --- |
ment
Manualfinancialdata "As a user, I want to be able Userscanmanuallyinputand
| input |     | toadd/modify/deleteincome, |     | managefinancialrecordsand |     |     |
| ----- | --- | -------------------------- | --- | ------------------------- | --- | --- |
expenses,anddifferentassets importdataviasupportedfile
|     |     | throughthe | application | orim- formats. |     |     |
| --- | --- | ---------- | ----------- | -------------- | --- | --- |
portthemfromafile."
Automaticdatafetch- "Asauser,Iwantmyincome, Thesystemintegrateswithex-
| ing |     | expenses,     | transactions, | and ternalAPIs                        | orservicesto | au- |
| --- | --- | ------------- | ------------- | ------------------------------------- | ------------ | --- |
|     |     | different     | assets to be  | fetched tomaticallyretrieveuserfinan- |              |     |
|     |     | automatically | from          | the bank cialdata.                    |              |     |
andbrokersthatIuse."
| Tagging |     | "Asauser,Iwanttobeableto    |     | Users can   | assign, edit, | and |
| ------- | --- | --------------------------- | --- | ----------- | ------------- | --- |
|         |     | dividemyassetsintodifferent |     | view custom | categories    | and |
categoriesandsubcategories." subcategoriesforeachasset.
Financialreportgen- "As a user, I want to receive Users can generate and view
eration on-demand financial reports downloadablereportssumma-
|     |     | (weekly/monthly) | summariz-         | rizing key                  | financial | metrics |
| --- | --- | ---------------- | ----------------- | --------------------------- | --------- | ------- |
|     |     | ing my           | income, expenses, | and overaselectedtimerange. |           |         |
assetgrowth."
Customizable dash- "Asauser,Iwanttocustomize Users can add, remove, and
| boards |     | thewidgetsonmydashboard |     | rearrange | dashboard elements |     |
| ------ | --- | ----------------------- | --- | --------- | ------------------ | --- |
tosuitmyfinancialgoals" suchascharts,summaries,and
alerts.
Choosecurrency "Asauser,Iwanttobeableto Users can select a preferred
choosethecurrencyIwantto displaycurrency,andthesys-
|     |     | usefordatavisualizationand |     | tem automatically | converts         |     |
| --- | --- | -------------------------- | --- | ----------------- | ---------------- | --- |
|     |     | analytics."                |     | values using      | current exchange |     |
rates.
Functionalrequirements
Table 5:
The non-functional requirements address factors such as trust, reliability, and
responsivenesswhichareimportantfactorsforuseradoptionandcontinuedengagement.
Herralaetal. (2023)notedthattechnicalissues,usererrorsandconcernsaboutdata
security resulted in increased stress and lowerrates of userengagement. Handayani et
al. (2024)identifiedprivacyandinformationsecurityasmajorconcernsformillennial
users.
29

| Category | Non-Functional | Userstory |     | Acceptance |     |
| -------- | -------------- | --------- | --- | ---------- | --- |
requirement
Dataprotection Preventunau- “Asauser, Iwant Alluserdataisiso-
andsecurity thorizedparties mypersonaldata latedandaccessible
|     | from accessing | tobesafeandnot  |             | onlytotheauthenti-  |          |
| --- | -------------- | --------------- | ----------- | ------------------- | -------- |
|     | data.          | getintothewrong |             | cateduser.          | External |
|     |                | hands.”         |             | accessisrestricted  |          |
|     |                | “Asan           | application | viasecureauthenti-  |          |
|     |                | owner,          | Iwantto     | cationandauthoriza- |          |
|     |                | protectcustomer |             | tionmechanisms.     |          |
andbusinessdata
from unauthorized
access.”
Reliability Thestatistics “Asauser, Ineedto Thesystem produces
|     | providedbythe  | trustthecalculation |     | correctfinancial |     |
| --- | -------------- | ------------------- | --- | ---------------- | --- |
|     | systemshouldbe | andanalyticsgiven   |     | analyticswithan  |     |
|     | correct.       | bythesystem.”       |     | accuracyrateofat |     |
least99.99%when
validatedagainst
sampledata.
| Performance | Goodresponse | “Asauser,         | Iwant  | 95%ofuserrequests  |     |
| ----------- | ------------ | ----------------- | ------ | ------------------ | --- |
|             | time         | thesystem         | topro- | areprocessedwithin |     |
|             |              | cessmyactions,    |        | 1secondundernor-   |     |
|             |              | suchasupdating    |        | maloperatingcondi- |     |
|             |              | assetsandfetching |        | tions.             |     |
reports,quickly.”
Non-Functionalrequirements
Table 6:
5.2 Prioritized objectives
Aftertherequirementsfortheproof-of-conceptapplicationweredefined,theywere
prioritizedtogetherwiththestakeholder,asdescribedinSection3.1.2. Theprioritized
listis presentedin Table 7, includinga short description, associatedgoal, andpriority
levelforeachrequirement.
| Label | Description | Goal |     |     | Priority |
| ----- | ----------- | ---- | --- | --- | -------- |
FR-01 Userinterface(Desktop Ensuretheapplication hasa Musthave
|     | andmobile) | responsiveandintuitiveinter- |     |     |     |
| --- | ---------- | ---------------------------- | --- | --- | --- |
faceusableacrossdevices.
FR-02 Datavisualization of Provideinteractiveandclear Musthave
|     | capitalandstatistics | visualizationstohelpusers |     |     |     |
| --- | -------------------- | ------------------------- | --- | --- | --- |
analyzefinancialperfor-
mance.
30

| Label | Description |     | Goal                    | Priority |
| ----- | ----------- | --- | ----------------------- | -------- |
| FR-03 | Tagging     |     | Allowuserstoorganizefi- | Musthave |
nancialdatausingcustom
categoriesandtags.
| QA-01 | Thestatisticsprovided |        | Ensurethatallsystem-    | Musthave |
| ----- | --------------------- | ------ | ----------------------- | -------- |
|       | bythesystem           | mustbe | generatedstatisticsand  |          |
|       | correct               |        | analyticsareaccurateand |          |
reliable.
FR-04 Presentreal-timecapital Displayup-to-datevaluesof Shouldhave
|     | information |     | alluserassetsusingreal-time |     |
| --- | ----------- | --- | --------------------------- | --- |
datasources.
FR-05 Financialreportgenera- Generatereportsthatsum- Shouldhave
|     | tion |     | marizefinancialmetricsfor |     |
| --- | ---- | --- | ------------------------- | --- |
selectedperiods.
QA-02 Preventunauthorized Securealluserdataandpre- Shouldhave
|     | partiesfrom | accessing | ventunauthorizedaccess |     |
| --- | ----------- | --------- | ---------------------- | --- |
|     | data        |           | throughauthentication  | and |
encryption.
FR-06 Automaticdatafetching IntegratewithfinancialAPIs Nicetohave
|     |     |     | toimporttransaction | and |
| --- | --- | --- | ------------------- | --- |
assetdataautomatically.
| FR-07 | Choosecurrency |     | Allowuserstochoosetheir | Nicetohave |
| ----- | -------------- | --- | ----------------------- | ---------- |
preferreddisplaycurrency
andapplyreal-timeconver-
sion.
| FR-08 | Customizabledash- |     | Letuserstailortheirdash- | Nicetohave |
| ----- | ----------------- | --- | ------------------------ | ---------- |
|       | boards            |     | boardswithwidgetsforper- |            |
sonalizedfinancialtracking.
| FR-09 | Manualfinancialdata |     | Supportmanualentryfor     | Optional |
| ----- | ------------------- | --- | ------------------------- | -------- |
|       | input               |     | transactionsandassetswhen |          |
automationisunavailable.
| QA-03 | Goodresponsetime |     | Ensurefastandresponsive | Optional |
| ----- | ---------------- | --- | ----------------------- | -------- |
interactionforcommonuser
actions.
|     |     | Table 7: Prioritizedrequirements |     |     |
| --- | --- | -------------------------------- | --- | --- |
31

| 6 Design | and development |     |     |
| -------- | --------------- | --- | --- |
The chapter provides the technical basis for the proof-of-concept application. The
chapter presents the major design decisions, system architecture, and implementa-
tion details that were used to meet the functional and non-functional requirements
described in the previous chapter. The focus was on designing a modular, scalable
and maintainable system that met stakeholder requirements while facilitating rapid
developmentunderthescopeofaPoC.
6.1 Architectural decisions
Based on the prioritized functional requirements (FR) and quality attributes (QA)
presented in Chapter 5, key architectural decisions were made to support the most
criticalgoalsforthesystem. Thefocuswasplacedonaddressingthe“Musthave”and
“Shouldhave”requirements. Sincethisisaproof-of-concept(PoC)application,the
architectureisintentionallysimplifiedtofocusfeasibility,corefunctionality,andrapid
developmentwhileminimizingunnecessarycomplexity. Thearchitecturaldecisions
arepresentedinTable8,alongwiththeirjustificationsandcorrespondingrequirement
links.
Thetechnicaldesignreflectsbothstakeholderneedsandrecommendationsfromthe
literature onPFM tools. Previous studiesindicated the importance of centralization
andmodularityforfacilitatingsustainedusageandcontinuedengagement(Gafrikova
et al. 2015; Torno et al. 2021). Similarly, usability and reliability were important
factors. Cederberg(2013)notedtheneedforanintuitiveuserinterfaceandautomated
categorization to minimize user effort, while Herrala et al. (2023) recognized that
technical complexity and user error may lead to stress and lower user trust. The
decision to create a cross platform UI, and modular back end is meant to promote
flexibilityandscalability. Additionally,featureslikevisualanalyticsandautomation
werechosenbasedonfindingsthattheyenhanceusermotivationandpromoteclearer
| financialunderstanding(Shafieeetal. | 2024;Cederberg2013). |               |             |
| ----------------------------------- | -------------------- | ------------- | ----------- |
| Short                               | Decision             | Justification | Requirement |
description
| User      | -UseFlutterfora     | -FlutterallowsquickUI   | FR-01 |
| --------- | ------------------- | ----------------------- | ----- |
| interface | cross-platformUI    | iterationwithasingle    |       |
|           | (mobileanddesktop). | codebase.               |       |
|           | -Implementabasic    | -ResponsiveUIensures    |       |
|           | responsiveUI.       | usabilityacrossdevices. |       |
32

| Short       | Decision             | Justification           | Requirement |
| ----------- | -------------------- | ----------------------- | ----------- |
| description |                      |                         | Link        |
| Backend     | -UseASP.NETCore      | -ASP.NETCoreis          | FR-01,      |
| services    | WebAPIforbackend     | performant,scalable,and | QA-02       |
|             | logic(C#).           | alignswithdeveloper     |             |
|             | -ImplementRESTful    | expertise.              |             |
|             | APIfordataflow.      | -UsingMongoDB.Driver    |             |
|             | -UseMongoDB.Driver   | ensurescompatibilityand |             |
|             | fordataaccess.       | flexibilitywith         |             |
|             | -Separatefrontendand | MongoDBdatamodels.      |             |
|             | backendintomodular   | -Modulararchitecture    |             |
|             | components.          | supportsmaintainability |             |
andfuturescaling.
| Database | -UseMongoDBfor        | -Flexibleschemaallows | FR-03, |
| -------- | --------------------- | --------------------- | ------ |
|          | storingfinancialdata, | adaptingtoevolving    | FR-06, |
|          | tags,andtransactions. | financialdata.        | QA-01  |
-Definecollectionsfor
structureddatastorage.
| Datavisual- | -Usechartlibrariesand  | -Chartsandtableshelp  | FR-02 |
| ----------- | ---------------------- | --------------------- | ----- |
| ization     | builtintablesinFlutter | usersanalyzefinancial |       |
|             | forfinancialdata       | trendseffectively.    |       |
visualization.
| Automatic    | -UseGoogleSheetAPI  | -GoogleSheet        | FR-04, |
| ------------ | ------------------- | ------------------- | ------ |
| datafetching | tofetchshareprices. | integrationensures  | FR-06  |
|              | -Implementscheduled | real-timefinancial  |        |
|              | jobstofetchandstore | updateswithnocosts. |        |
|              | data.               | -Scheduledjobs      |        |
automatedataretrieval.
| Multi-   | -Storeallfinancialdata | -Storingdatainabase      | FR-07 |
| -------- | ---------------------- | ------------------------ | ----- |
| currency | inabasecurrency(e.g.,  | currencyavoids           |       |
| support  | USD/EUR).              | unnecessaryconversions.  |       |
|          | -Fetchexchangerates    | -Dynamicconversion       |       |
|          | fromHexaRateAPI.       | providesuserflexibility. |       |
Customizable -Storedashboardlayouts -JSONstorageenables FR-08
| dashboards | inMongoDBasJSON | flexibleUIcustomization. |     |
| ---------- | --------------- | ------------------------ | --- |
|            | documents.      | -Drag-and-DropUI         |     |
|            | -UseFlutter’s   | enhancesusability.       |     |
Drag-and-DropWidgets.
| Manual    | -Usedifferentformsto  | -Enableseasydatainput | FR-09 |
| --------- | --------------------- | --------------------- | ----- |
| financial | inputdifferent        | whenintegrationsmight |       |
| datainput | transactionsmanually. | notbeavailable.       |       |
|           | -Maketableseditable.  | -CSVimportreduces     |       |
|           | -SupportCSVimports.   | manualworkloadforbulk |       |
dataentry.
33

| Short       | Decision               | Justification           | Requirement |
| ----------- | ---------------------- | ----------------------- | ----------- |
| description |                        |                         | Link        |
| Performance | -OptimizeAPIandDB      | -Reducesresponsetimes   | QA-03       |
| optimiza-   | querieswithindexingand | andimprovesscalability. |             |
| tion        | caching.               |                         |             |
-UseprovidersinUIand
onlycallAPIwhen
somethingisupdated.
Architecturaldecisionsandtheirlinkagetorequirements
| Table      | 8:           |     |     |
| ---------- | ------------ | --- | --- |
| 6.2 System | architecture |     |     |
Thehigh-levelsystemarchitectureisshowninFigure2. Thesystemconsistsofthree
core components aligned with the architectural decisions discussed in the previous
section: theuserinterface,thebackendAPI,andthedatastoragelayer. Additionally
thetwointegrationsarepresentedinthepicture: stockpricesandexchangerates.
The user interface is developed using Flutter and Dart to support cross-platform
deployment across mobile and web platforms. It handles user interactions, such as
addingoreditingtransactions,andvisualizesfinancialdatathroughinteractivecharts
andtables. WhileWinUIwasinitiallyconsideredforthefrontend,itwaseventually
letgoduetoitslimitedvisualizationcapabilitiesanditsrestrictiontotheWindows
desktopenvironment.
Figure 2: High-levelsystemarchitecturediagram
The backend API is implemented in C# using the .NET framework. It contains
the core business logic of the application, including transaction handling (shares,
34

cash,andrealestate),statisticalcomputations,andcommunicationwithexternaldata
sources. TheAPIisalsoresponsibleforallinteractionswiththedatabase,including
datastorage,updates, andretrieval. Whilethisdesign doesnotscalefarinproduction
environment where there is more traffic, the code is structured in a way that would
allowseparationtomicroserviceslateron.
MongoDBisusedastheNoSQLdatabaseduetoitsflexibilityinmanagingdiverse
financialdata. Itstoresallthedatamodels,includingtransactions,assetdetails(shares,
realestate,andcash),cashflow(incomeandexpenses),anddailynetworthsnapshots.
To enrich the application with current market data, two external integrations are
included. Forstockprices,thesystemusesaGoogleSheetsintegrationpoweredby
GoogleFinance. Real-time prices areretrieved viatheGoogle SheetsAPIbased on
tickersymbols,withdatarefreshedeachtimetheapplicationisopenedormodified.
Althoughthissolutionrequiressomemanualsetupbyusers,itwasselectedduetothe
highcostandlimitedavailabilityofcommercialstockAPIs.
CurrencyexchangeratesarefetchedfromtheHexaRateAPI. Toimproveefficiency,
exchangeratesareretrievedonceperdayandcachedinthedatabaseforreuse,ensuring
up-to-dateconversiondatawithminimalexternalrequests.
6.3 Implementation details
6.3.1 Data model and domain objects
Theapplication’sdatamodelisdesignedtoreflectthefinancialdomainandsupport
corefunctionalitiessuchasassettracking,incomeandexpensemonitoring,andnet
worthcalculation. ANoSQL,document-basedapproachisused,witheachdomain
objectstoredinaseparateMongoDBcollection. Themaincollectionsandtheirroles
aredescribedbelow:
• ShareTransaction, CashTransaction, RealEstateTransaction: These collec-
tionsstorerawtransactiondataenteredbyusers. Eachrecordincludesmetadata
such as transaction date, amount, and relevant domain-specific fields such as
purchasepriceorloanamountforrealestate. Thesetransactionsformthebase
forcalculatingassetvalues.
• Share,Cash, RealEstate:Thesecollections representtheuser’s current asset
state. Theyarecomputeddynamicallyfromtransactionhistory. Forexample,
the collection aggregates holdings per ticker symbol, calculating total
Share
quantityandcurrentmarketvalue.
• CashFlowTransaction: This collection tracks income and expense activity.
Eachentryincludesthetransactiontype(incomeorexpense),category,amount,
currency,andoptionalnotes. Thisenablesbudgettracking,categorybreakdowns,
andmonthlyexpensesummaries.
35

• NetWorthSnapShot:Thiscollectionstoresdailysnapshotsoftheuser’stotal
networth. Wheneverassetsaremodified,forexample,throughaneworupdated
transaction,thesystemeithercreatesorupdatesthesnapshotforthatdate. These
recordssupporthistoricalnetworthtrackingandtrendvisualization.
• ExchangeRate: Thiscollectionstoresdailycurrencyexchangeratesretrieved
fromtheHexaRateAPI. Ratesarefetchedonceperdayandcachedtoreduce
external requests. All financial data are normalized to a base currency (e.g.,
EURorUSD)usingthesestoredrates.
Thismodulardatamodelsupportsaflexibleandextensiblearchitecture,enabling
newfeaturestobeaddedwithminimaldisruptiontoexistingcomponents. Thebackend
API follows a structured design pattern in which each domain feature is managed
through a dedicated – pair, promoting a clear separation between
Controller Logic
requesthandlingandbusinesslogic. Thispatternalsoenablespossiblelaterseparation
totheirownmicroservicestoincreasescalability.
6.3.2 User interface structure and design approach
TheuserinterfaceisimplementedinFlutterusingamodular,screen-basedarchitecture.
Each primary functionality, such as the dashboard, asset management, transaction
input, and cash flow tracking, is encapsulated in a dedicated screen. These screens
are composed of reusable UI components, including editable tables, input forms,
pie charts, and bar graphs. All components are located in the folder and
widgets/
accessapplicationdatathroughstatemanagementprovidedbythe package.
provider
Theinterfaceupdatesreactivelyinresponsetochangesintheunderlyingdatalayer,
ensuringsynchronizationbetweenthedatamodelandtherenderedviews.
Financial visualizations are built using the fl_chart library, supporting different
diagramssuchasline,bar,andpiecharts. Theseprovideuserswithimmediatevisual
feedbackonfinancialdistributionsandtrends. AsnotedbyBitriánetal. (2021),visual
progress indicators and dashboards can improve user motivation and purposefulness.
To support responsive layouts, Flutter’s layout tools, such as , ,
Expanded Flexible
and , are used alongside maximum width constraints to optimize the
LayoutBuilder
interface for large screens. While the current design primarily targets desktop and
webresolutions,theuseofFlutterenablesfuturemobilesupportwithminimalcode
changes.
TheUI designfocuses clarityandease ofdataentry. Structuredformsareprovided
for each transaction type, and editable tables enable efficient bulk modifications.
Usabilityand dataintegrityarefurtherimproved throughfeatures suchas real-time
form validation, dropdown menus, and multi-select checkboxes. This emphasis on
visual feedback and structured input aligns with design recommendations for PFM
tools,whichstressthatreducingmanualeffortandsimplifyinginteractionsencourages
continuedengagementandreducesuserstress. Cederberg(2013)highlightsthatyoung
36

usersvaluetoolsthathaveinvitinginterface,automatedcategorization,andminimized
inputcomplexity,whileHerralaetal. (2023)cautionthatsystemsperceivedasdifficult
orunreliablecanincreasecognitiveloadandunderminetrust.
6.3.3 Development tools and process
ArangeofmoderntoolswereutilizedduringthePoCdevelopment. Backendservices
weredevelopedusingMicrosoftVisualStudioCommunity2022,whiletheFlutter-
basedfrontendwasimplementedinVisualStudioCode. MongoDBCompasswasused
to inspect and manage database documents during development. Version control was
handledusingGit,enablingstructuredbranching,changetracking,andsafeiteration.
GenerativeAItoolswereusedtosupportthedevelopmentprocessbyassistingwith
code scaffolding, debugging suggestions, and exploration of architectural patterns.
These tools were particularly helpful in accelerating UI layout design in Flutter,
formulatingMongoDBqueries,andstructuringbackendlogicin.NET. However,their
rolewasstrictlysupportive: allcodewasmanuallyreviewed,adapted,andintegrated
tomeettheproject’sspecificrequirements.
An iterative development approach was followed, including regular feedback from
thestakeholder. Thefunctionalitywasimplementedinmodularunits. Forexample,
share management and its related transactions were treated as a single feature set.
Each feature typically followed a consistent workflow: beginning with UI design,
followedbydatacontractdefinition,backendlogicandAPIendpointcreation,database
integration, and finally frontend-backend connection. After each feature reached a
workingstate,timewasallocatedforrefactoringandfine-tuningbeforeproceedingto
thenextsetoffeatures. Thisincrementalapproachsupportedrapidprototypingwhile
allowing flexibilityto respondto evolving requirementsthroughout thedevelopment
phase. Iterative developmentwith stakeholderfeedback is also recommendedin DSR
literature. Hevner et al. (2004) stated that iteration and implementation are central
piecestothisresearchasitincreasesthequalityoftheendproductandhelpsaddress
problemsalongtheway.
37

7 Demonstration
This chapterdescribes apractical demonstration ofthe proof-of-conceptapplication.
The goal is to demonstrate how the implemented system solves the main problems
inthestakeholder’sfinancialmanagementprocess. Thedemonstrationwillfollowa
structureofthemostimportantissuesandhowtheproposedsolutionaddressesthese.
7.1 Addressing complexity and human error
A major challenge with the stakeholder’s current system is its complexity and vul-
nerability to human error, caused by the use of multiple spreadsheets and manual
calculations across various financial sources. The PoC application mitigates these
issuesbyconsolidatingallfinancialdataintoasingle,structuredbackendsupported
bywell-definedlogicandcalculations.
Eachfinancialdomain(shares,cash,andrealestate)ishandledbyadedicatedlogic
class in the backend, following a consistent – design pattern. This
Controller Logic
separationensuresthateachlogicclassisresponsiblefordomain-specificoperations
suchasassetaggregation,transactionhandling,andprofitcalculation. Forexample,
the class compiles a user’s holdings based on transaction history and
ShareLogic
computeskeymetrics,including:
• Totalinvestedamount
• Currentmarketvalue(basedonthelatestprices)
• Profitorlossinabsoluteterms
• Profitorlossasapercentage
Thesecalculationsareperformedautomaticallyontheserverside,usingtheuser’s
basecurrencyandup-to-dateexchangeratesandshareprices. Theresultsarereturned
tothefrontendaspartoftheassetmodel,eliminatingtheneedforspreadsheet-based
formulas or manual input. Similar logic applies to cash and real estate assets, with
realestatecomputationstakingintoaccountthepurchasepriceandloanamount.
By encapsulatingbusiness logic in code, the system delivers consistentand reliable
results,significantlyreducingtheriskoferrorscausedbyuserinput,brokenformulas,
or accidental modifications. Centralized logic also simplifies future updates as any
changetocalculationrules,suchasprofitformulasorexchangeratehandling,canbe
appliedsystem-widefromasinglesource.
The frontend presents these results visually and interactively. On the
Dashboard
page, shares are displayed in a doughnut chart (Figure 3), while the
Assets and
pageshowsdetailedassetdataineditabletables(Figure4).
Transactions
38

User’ssharespresentedinaninteractivedoughnutchart
Figure 3:
User’sassetspresentedineditabletableswithsummarystatistics
Figure 4:
39

Automatingcomplexcalculationsandreducingmanualworkflowsincreasesease
ofuse. This isconsistentwithresearchthatsuggests usersaremorelikelytoengage
withsystemswithloweffortandclearfeedback. Cederberg(2013)foundthatyoung
users preferred financial tools that required less manual input, included automated
categorization,andimprovedvisualclaritywhichfurtherempoweredthemtomanage
theirfinancesbetterandencouragedcontinueduse. Likewise,Herralaetal. (2023)
identified that by makingfinancial tasks easier to complete, user stress was reduced,
andsenseofcontrolincreased.
7.2 Solving scalability limitations
The stakeholder’s previous system, based on Excel spreadsheets, had scalability
limitations as the financial data volume increased. Over time, the growing number
of transactions, investment types, and calculated fields made the system fragile
and difficult to scale. Complex dependencies between formulas and worksheets
created a risk where even minor changes could disrupt the entire setup. The PoC
applicationaddressesthesechallengesthroughaservice-orientedarchitectureanda
document-baseddatabasemodel.
FinancialdataisstoredinMongoDBcollections,whichareconvenientforevolving
data structures. This enables thesystem to handleincreasing volumes oftransactions
andassetswithoutrequiringstrictschemasormanualreconfiguration. Thebackend
is implemented as a stateless ASP.NET Core Web API, which supports horizontal
scalability. WhilethisPoCis notintendedforproductiondeployment,the underlying
architectureallowsforfuturecontainerizationandcloud-basedscaling.
ThePoC hasremovedthe traditionallimitationsofExcel,suchasworksheetsize,
formuladepth,and fragilecross-sheetdependenciesgivinga basisforscalabilityover
time, data reliability, and consistent performance, as the financial data grows. In
additiontogreaterdatavolumes,theapplicationsupportsmorecomplexdatamodels
that are more structured, more object-oriented than traditional spreadsheets. This
could include things like real estate records that could have fields for loan amount,
terms of mortgage payments, and all of the payment history, or share transactions
that could track dividends, market pricing, and country attribution. It is difficult to
modelthelevelofdetailinExcelandtomaintainitsreliability. Thislimitationisalso
observedinstudiesofPFMtools,wheretraditionalsystemsrelyingonmanualentry
andstaticformatsoftenstruggletosupportgrowingdataneedsandcomplexfinancial
contexts(Gafrikovaetal. 2015).
Oneexampleofimprovedscalabilityistheautomatednetworthtrackingfeature.
Previously, thestakeholder manuallygathered assetvalues fromvarious sourcesand
combined them to update a dataset for visualization. In contrast, the PoC system
calculatesnetworthautomaticallywheneveranyassetismodifiedandcanalsogenerate
historicalvaluesretrospectively(seeFigure5).
40

User’snetworthovertime
Figure 5:
7.3 Automating financial data retrieval
One of the key goals identified during the problem definition phase was to reduce
the manualeffortrequired toupdate financialdata, especiallystock prices, exchange
rates,andaccountbalances. Whilefullautomationremainsachallengeduetolimited
access to bank and broker APIs, the current solution introduces partial automation
thatmeaningfullyreducestheuser’sworkload.
StockpricesareautomaticallyretrievedthroughaGoogleSheetsintegration,where
thesheetispoweredbythe function(SeeFigure6). Theapplication
GOOGLEFINANCE
connects to this sheet through the Google Sheets API and fetches up-to-date prices
foralltickerslistedbytheuser. Althoughusersmuststillmaintainthistickerlistand
entersharetransactionsmanually,thesolutionremovestheneedtorepeatedlycopy
databetweenExcelfiles.
41

GoogleSheetwiththeuser’sstocktickerspoweredbythe
Figure 6: GOOGLEFINANCE
function
ExchangeratesareretrieveddailyusingtheHexaRateAPIandstoredinthedatabase
forreuse. Thisensuresthatallfinancialdataregardlessoforiginalcurrencyisconverted
consistentlywithoutrequiringtheusertolookuporinputratesmanually.
Whileincomeandexpensedataarestillenteredmanuallythroughtheapplication’s
user interface, the system centralizes this information for easier tracking. In the
stakeholder’spreviousworkflow,expenseandincomedatawereenteredintoSpendee,
exported,andthenincorporatedintoafinancialreportandmasterExcelfile. Incontrast,
thenewsystemdecreasesredundancyandimprovesconsistencybymaintainingall
datainacentralizedplatform. Thisremovestheneedtoupdateratesandpricesacross
multipletabsandformulas.
Future iterations may include integration with Open Banking APIs or broker-
42

specificservices,if reliableandcost-effectiveoptionsbecomeavailable. Thecurrent
solutionoffersapracticalbalancebetweenautomation,dataaccuracy,andusercontrol.
Achievingevenpartialautomationhashelpedreducefrictionforusersandcreatea
levelofconsistency. ThisalignswithfindingsbyCederberg(2013),whonotedthat
usersweremorelikelytoadoptPFMtoolswhenfeaturessuchastransactiontracking
andvisualsummarieswereautomated,reducingmanualinputandcognitiveeffort.
However,aspointedbyKayeetal. (2014),someusersmaybecomefrustratedwith
toomuchautomation,suchasinflexibleorinaccurateexpensecategorization,which
can hinder trust or usability. This supports the rationale for retaining user control
alongside automation, ensuring the system remains both efficient and adaptable to
individualpreferences.
7.4 Centralized tracking across categories
Theapplication providesstructuredand centralizedtrackingoffinancial dataacross
assetandcashflowcategories. Assets,includingshares,cash,andrealestate,arestored
indedicatedcollectionsandgroupedusingrelevantidentifierstosupportorganized
analysis.
Shares are enriched with metadata such as category (e.g., dividend, growth),
subcategory(e.g.,REIT,BDC),andcountryoforigin. Theseadditionalfieldsenable
detailedbreakdownsandarevisualizedthroughmulti-layeredpiecharts,asshownin
Figure7.
Sharedistributionvisualizedbycategory,country,andsubcategory
Figure 7:
Cash assets are grouped by account name (e.g., savings or investment account),
whilerealestateholdingsarecategorizedbypropertyname. Thishelpsuserstrack
thevalueandperformanceofeachassetindividually,withoutmixingdifferenttypes
offinancestogether(SeeFigure8).
43

Otherassetdistributionvisualizedbycategory,country,andsubcategory
Figure 8:
Additionally, the application tracks income and expenses under the cash flow
module. Transactionsaretaggedwithlabelssuchasfood,salary,orshopping,enabling
categorized insights. As shown in Figure 9, cash flow data is presented through
categorizedpiecharts,achronologicaltransactiontimeline,andabarchartcomparing
monthlyincomeandexpenses.
44

Cash flow tracking: categorized income and expenses with monthly
Figure 9:
comparison
Thesystemprovidestheuserwithinsightsthatwerepreviouslyfragmentedthrough-
out different tools and spreadsheets by standardizing categorization for both assets
andtransactionsandconsolidatingallofthedatawithinasingleinterface. Thishelps
centralizing the user’s financial management, and ultimately helps their decision-
makingprocess. Moreorganizedandcategorizedfinancialdatacanaidmoreinformed
insightsanddecision-making. ThissupportsfindingsfromGafrikovaetal. (2015),
who described how PFM tools provide users with categorized expense tracking,
groupedspendingbytype(e.g.,rent,food,transportation),andaggregatedfinancial
informationfromvarioussources,whichimprovesvisibilityintopersonalfinancial
flows. Handayani etal. (2024)similarly notedthatautomatic expensetrackers, cate-
gorizationfeatures,andintegrationacrossfinancialsourcesallowuserstorecognize
theirspendingpatternsandmakebetterfinancialdecisions.
7.5 Integrated and efficient reporting
One of the most labor-intensive tasks in the stakeholder’s previous workflow was
the creation of quarterly financial reports. This process involved manually copying
charts,aggregatingfiguresfromvariousspreadsheets,andcompilingthemintoaWord
document. ThePoCapplicationreplacesthiswithafullyintegratedreportingfeature
thatgeneratesacomprehensivesummaryforaselectedtimeperiod.
ThereportconsolidatesdatafrommultiplepartsofthesystemintoasinglePDF
45

fileandincludesthefollowingelements:
• Monthlyincome,expenses,andsurplusvisualizedinagroupedbarchart
• Savingspercentagepermonth
• Expensesvs. incomedisplayedasalinechart
• Adetailedlistofcategorizedcashflowtransactions
• Networthdevelopmentovertimeandbreakdownbyassetcategory
• Sharedistributionbytype,country,andsubcategory
Alldataisautomaticallyretrievedfromthebackendandvisualizedthroughcharts
and tables based on the selected time frame. The compiled report is exported as
a downloadable PDF document, allowing users to archive or review their financial
summarieswithoutmanualintervention.
This feature saves time and effort when generating reports on a recurring basis
by replacing a multi-step manual process with one integrated functionality. As
Cederberg (2013) says, automating repetitive financial tasks along with providing
visual summaries for clarity can reduce the burden on users and ease adoption.
Likewise,Shafieeetal. (2024)pointoutthatreportingprovidescoherentandvisual
outputsto helpestablishunderstanding andinformdecisions. It alsosatisfies theidea
foranoverviewoffinancesbyKayeetal. (2014),consolidatinganumberoftoolsand
processesintoasingularreportingprocess.
46

User-generatedfinancialreportforaselectedtimeperiod
Figure 10:
By automating the generation of structured and visually rich reports, the system
supports more efficient and consistent financial review cycles while preserving the
stakeholder’spreferencefordetaileddocumentationandanalysis.
47

8 Evaluation
Thischapterpresentstheresultsoftheevaluationphase. Thegoalofthisphaseisto
assess how effectively the implemented artifact addresses the original problem and
fulfillsthedefinedsolutionobjectives. Fourevaluationmethodswereused: task-based
usertesting, astakeholderfeedbackquestionnaire,comparisontothebaselinesystem,
andanalyticalassessmentagainstthedesignobjectives.
8.1 Task-based user testing
Task-basedusertestingwasconducted toobservethestakeholderinteractingwiththe
systemina realisticusagescenario. Thepurpose was toevaluatetheusability, core
functionality,andoveralluserexperience. Thestakeholderperformedapredefinedset
oftasksontheirownmachinewhilebeingobserved. Eachtaskwasassessedbasedon
successfulcompletion, workflow intuitiveness, and any usabilityissues orfeedback
thatarose. ThetaskswereoriginallydefinedinChapter3.1.5.
All tasks were completed successfully. The stakeholder navigated the system
confidentlyandrequirednoexternalguidancetolocateoruseanyofthekeyfeatures.
Taskdurationsrangedfromtwotofiveminutes,dependingondataentryrequirements.
Forexample:
• Task 1: The stakeholder imported share transactions using a CSV file and
manuallyaddedtwocashandtworealestatetransactions.
• Task2:Theuserexploredpiechartsonthedashboardbycategoryandreviewed
datatableson the"AssetsandTransactions"page,includingtestingthesorting
andeditingfunctionalities.
• Task 3: Multiple income and expense transactions were added across a four-
monthperiod,followedbyareviewoftheupdatedcashflowvisualizations.
• Task4:Thestakeholdergeneratedafinancialreportfortheperiod1.1.2025–30.4.2025
andexaminedthecontentsofthegeneratedPDFfile.
Feedback during testing primarily concerned user interface clarity and usability
improvements. Notablesuggestionsincluded:
• Enhancingtooltipsinpiechartstoshowadditionaldetails(e.g.,EURvalue)
• Improvinglabelclarityintherealestatetable
• Adjustingthetransactionorderinginthecashflowlistforbetterintuitiveness
Despite these observations, all tasks were completed without errors or external
assistance which indicates that the system provides a generally intuitive and user-
48

friendly experience. These findings are consistent with literature showing that
structured, intuitive interfaces and visual feedback mechanisms play a big role in
improvinguserengagementandconfidenceinpersonalfinancetools. Thisissupported
by Cederberg (2013), who found that simplified interfaces with visual summaries
reduce user effort and promote adoption. Similarly, Shafiee et al. (2024) note that
user-friendlyandpersonalizedinterfacesimproveusers’understandingandconfidence
infinancialdecision-making.
8.2 Stakeholder insights from questionnaire
Followingthetask-basedtestingsession,astructuredquestionnairewasadministered
to gather deeper feedback from the stakeholder. The questions were organized into
four areas: general impressions, feature satisfaction, problem-solving impact, and
suggestions for future development. This section summarizes the stakeholder’s
responsesineacharea.
8.2.1 General impressions
The stakeholder found the interface intuitive and user-friendly. Although some
functionalitieswerenotimmediatelyvisible,theywereeasilydiscoveredthroughbrief
exploration. Overall,the structureandnavigation ofthe application wereconsidered
effectiveandalignedwithtypicaluserexpectations.
8.2.2 Feature satisfaction
Thesharetrackingfunctionalitywaspraisedforitsscalabilityandeaseofusecompared
tothestakeholder’spreviousExcelsystem. Theautomationofdataaggregationand
valuecomputationwasseenasamajorimprovement.
The stakeholder found the cash flow feature useful and realistic but suggested
clarifyingitspurposewhetheritismeantfordetailedbudgetinglikeinappssuchas
Spendee,orformoregeneralexpensetracking. Thiswouldhelpdeterminewhether
thefeatureshouldbesimplifiedoroffermorecustomization.
Visualizationsweredescribedasclearandinformative. Thestakeholderhighlighted
the pie charts and trend graphs as particularly valuable for gaining quick insights.
Minorrefinementsweresuggested,particularlyforthelong-termcapitaldevelopment
graphtoimproveclarity.
The PDF report generation feature was considered a strong improvement. It
streamlinedapreviouslymanualandtime-consumingreportingprocess,offeringclear
valuethroughautomationandintegration.
49

8.2.3 Problem-solving impact
The stakeholder reported a reduction in manual work, especially with processes that
wentbackandforthbetweenexcelandgooglesheets. Theabilitytoseeallthefinancial
informationinoneinterfacewasseenasamajorimprovement. Thissupportsfindings
byKayeetal. (2014)thatuserspreferredsimplifiedsnapshotsratherthanacomplete
representation. Inasimilarmanner,Cederberg(2013)notedthatPFMsystemsoffering
centralized and easy-to-access financial data increase user motivation and ongoing
engagement.
Systemstabilityanddatareliabilitywerealsonoteworthy. Incontrasttotheprevious
Excelworkflowthatwassusceptibletobrokenformulasandinconsistencies,thePoC
was praised as secure and dependable. Automatic integration of transactions and
chronological organization contributed to a higher level of trust in the data. This
finding supports the consideration of epistemic stability in personal finance tools,
articulatedbyHerralaetal. (2023). Theyarguedthatusersmustbeabletotrustthe
logic andoutputof the applicationin orderto experience thesense ofempowerment
andfeelingofcontrolovertheirfinances. Whentoolsareperceivedasunpredictable
or"blackbox",users’trustinthedataandthesystemasawholecandecrease.
8.2.4 Suggestions and future improvements
Suggestions focused primarily on improving user experience and refining existing
features. Theseincluded:
• Enhancingtooltipandgraphclarity
• Addingtheabilitytomodifytransactionsdirectlyfromthetransactionlist
• Clarifyingtheintendeduseofthecashflowfunctionality
Overall,thestakeholderexpressedstrongconfidenceintheapplication’spotential.
Theyindicatedthatwithfurtherrefinementanditeration,thesystemcouldevolveinto
afullydeployableproductthatmeetsbroaderpersonalfinancemanagementneeds.
8.3 Comparison to baseline
In order to assess the practical advantages of the implemented solution, a simple
comparisonwasmadebetweenthestakeholder’sexistingfinancialtrackingmethod
tothe PoCapplication. Theoriginalmethodconsisted ofnumerousapproaches and
tools,suchasExcelspreadsheets,GoogleSheets, andtheSpendeeapplication,where
consolidatingalloftheinformationwaslaboriousandmanual.
Table9summarizeskeydifferencesbetweenthebaselinesetupandthePoCsystem.
50

| Aspect        | Oldsystem(Baseline)  |        | Newsystem(PoC)           |
| ------------- | -------------------- | ------ | ------------------------ |
| Tool          | Multipletools:       | Excel, | Centralized,web-based    |
| fragmentation | Spendee,GoogleSheets |        | application              |
| Shareprice    | Manualcopy-pastefrom |        | AutomatedviaGoogleSheets |
| updates       | GoogleFinance        |        | APIintegration           |
Exchangerate Manuallycheckedandentered Automaticallyfetcheddaily
| updates        |                    |     | fromHexaRateAPI            |
| -------------- | ------------------ | --- | -------------------------- |
| Income/expense | RecordedinSpendee, |     | Enteredandvisualizedwithin |
| tracking       | analyzedinExcel    |     | theapplication             |
Datavisualization Static,manuallycreatedExcel Interactive,real-time
|           | charts                 |     | visualizationsandtables  |
| --------- | ---------------------- | --- | ------------------------ |
| Financial | Manualreportassemblyin |     | AutomatedPDFreportswith  |
| reporting | WordwithExcelcharts    |     | integrateddataandvisuals |
Stabilityand Highriskofformulaerrors Backend-calculatedvalues
| accuracy                                                   | andbrokenreferences        |     | withrobustlogic       |
| ---------------------------------------------------------- | -------------------------- | --- | --------------------- |
| Timespent                                                  | Significantmanualeffortand |     | Streamlinedupdatesvia |
| updating                                                   | toolswitching              |     | integrateddataflow    |
| Table 9: ComparisonofthebaselinesystemandthePoCapplication |                            |     |                       |
Asseen inTable9, thePoC solutionmeetsthe mostimportantissuesfoundfrom
theprevious system,by offeringcentralizeddata, anautomated updates,andbuilt-in
analyticcapabilities. Inshort,itminimizesusermanualworkloadanderrorrateswhile
increasing data transparency. The stakeholder was in agreement that the usability,
automation,andtrustintheaccuracyofthedatahadimproved. Tornoetal. (2021)
found that most personal finance solutions tend to focus on very few features or
services,sothisPoCfocusesbridgingthesegaps.
| 8.4 Evaluation | against | design objectives |     |
| -------------- | ------- | ----------------- | --- |
ThissectionassesseshoweffectivelytheimplementedPoCmeetsthefunctionaland
quality objectives defined in Chapter 5. Each requirement is reviewed basedon the
actual system implementation, stakeholderfeedback, andoutcomes observed during
theevaluationphase.
FR-01: Userinterface(Desktopandmobile)
ThesystemwasimplementedusingFlutter,supportingdeploymentacrossdesktop,
web,andmobileplatforms. Thestakeholderconfirmedtheinterfacewasintuitiveand
easytouseduringdesktoptesting. However,thecurrentimplementationisprimarily
optimized fordesktop and web, withmobile-specific layoutadjustments stillpending.
Status: Partiallyachieved
FR-02: Datavisualizationofcapitalandstatistics
Interactivechartsandgraphswereimplementedtovisualizenetworthtrends,asset
51

categories,andcashflowsummaries. Thestakeholderhighlightedthesefeaturesas
clearandsignificantlymoreeffectivethantheirpreviousmanualvisualizations. Status:
Achieved
FR-03: Tagging
Thedatamodelsupportsassetclassificationbycategories,subcategories,andcountry
oforigin. Taggingisappliedconsistentlyacrossshares,cashaccounts,realestate,and
cashflowtransactions. Status: Achieved
QA-01: Correctnessofstatistics
Keycalculations,includingnetworth,profit/loss,andsavingsrate,areperformedby
centralizedbackendlogic,reducingriskofusererror. Thestakeholderconfirmedthe
accuracyandreliabilityoftheresults. Status: Achieved
FR-04: Presentreal-timecapitalinformation
Real-timemarketdataandexchangeratesarefetchedautomatically,ensuringup-to-
date capital values. This functionality was identified by the stakeholder as a major
improvementoverthemanualupdateprocess. Status: Achieved
FR-05: Financialreportgeneration
ThesystemprovidesdownloadablePDFreportssummarizingkeyfinancialmetrics
overaselectedtimeframe. Thisreplacedthestakeholder’smanualreportingprocess
andwasviewedasamajorefficiencyimprovement. Status: Achieved
QA-02: Dataaccesscontrol
Although the data model is designed to support user-level data segregation, no
authenticationorauthorizationmechanismswereimplemented. Thislimitationwas
acknowledged and deferred due to time constraints and PoC scope. Status: Not
achieved
FR-06: Automaticdatafetching
The system integrates with external sources to retrieve exchange rates and share
prices. However,fullautomationofbankorbrokertransactionswasnotimplemented.
Despitethis,thecurrentsolutionmeaningfullyreducesmanualeffort. Status: Partially
achieved
FR-07: Choosecurrency
All financialdata is normalized to a base currency, with exchange rates fetcheddaily.
Thisensuresconsistencyacrosscalculationsandsupportsuser-definedcurrencyviews.
Status: Achieved
FR-08: Customizabledashboards
Customizable dashboards were not implemented. All visualizations are static and
predefined. Thisfeature wasdeprioritizeddue to limitedtime and PoCfocus. Status:
Notachieved
52

FR-09: Manualfinancialdatainput
StructuredformsandCSVimportfeatureswereimplementedforallmajortransaction
types,enablingeffectivemanualdataentryandcorrections. Status: Achieved
QA-03: Goodresponsetime
Performance during testing was consistently fast. Efficient data fetching, use of
caching, and statemanagement contributed toa responsive userexperience. However
no performance testing was conducted and some refinements would be needed for
productionversion. Status: Achieved
Insummary,allcore"Musthave"requirementsweresuccessfullyimplementedor
partially fulfilled, ensuring that the fundamental goals of the PoC were met. Most
"Shouldhave"featureswereincluded,whilelower-priorityitemssuchasauthentication
anddashboardcustomizationweredeferredforfuturedevelopmentiterations.
53

9 Discussion
Thischapterlooksbackon theprojectandreflectsonwhat was achieved. Itstartsby
reviewinghowwellthefinalsolutionaddressedtheoriginalproblemandwhatkind
of feedback the stakeholder gave. It also considers how useful the Design Science
ResearchMethodology(DSRM)wasthroughoutthe process. Inaddition, thechapter
highlightssome ofthechallenges facedduringdevelopmentandpoints outpossible
waysthe solutioncould beimprovedorexpanded inthe future. Altogether, itgivesa
clearpictureofwhattheprojectaccomplishedandwhereitcouldgonext.
9.1 Summary of results and impact
ThefindingsfromthisresearchprojectshowthatthePoCapplicationaccomplishesthe
identifiedgoalsdefinedearlierinthethesis. Thecorefunctionalitieswereimplemented
andtestedwiththeactualenduserinarealisticenvironment. Userfeedbackconfirmed
that theapplication solved theprimary stakeholder concerns: it reducedmanual effort
and mitigated human errors. This finding corresponds with Herrala et al. (2023)’s
observationthatcomplexinanerror-pronetoolscanreducefinancialconfidenceand
raiseunnecessaryanxiety,especiallyforyoungerusers. Byreducingcomplexityand
centralizingfinancialdata,thePoCsystemimprovesbothusabilityandreliability.
Unlike many existing PFM tools which focus on limited functionality, such as
budgetingortrackingspendingpatterns(e.g.,Mint,YNAB,Spendee),thePoCwas
designedtoprovideamoreglobalandintegratedapproachacrossallaspectsofPFM.
The PoC provided a functionality for tracking investments, monitoring net worth,
analyzing cash flow, and producing financial reports, in a more centralized way.
ThePoC’sdesigndirectlyaddressedthefragmentedfocusofPFMasrecognizedby
Torno et al. (2021). The study noted that most PFM apps focus on single service
and rarely combine planning, tracking, and education in one app. While Kaye et
al. (2014) noted that some tools provide discomfort due to perceived complexity,
reliability, and fragmented view of PFM thus risking long-term engagement. The
existingstakeholdersystemalsolackedautomationwhichwasnotedintheliterature.
According to Cederberg (2013), automating tasks and reducing manual user input
werebigmotivatorsforadoptingmobilefinancialtools,astheysimplifiedworkflows
andreduced friction. ThePoC applicationimproveson thisbyproviding automated
retrieval of exchange rates, stock price updates, and aggregation of asset data in
real-time.
One of the major strengths was the PoC being adaptable under the European
context. Many of the popular PFM tools, such as Mint, Quicken, etc. are largely
basedonU.S. users,customarilylinkedtoregionally-identifiedfinancialAPIs. This
alsocomplementsthefindingsofStefanovetal. (2024),whostatedthatusersfrom
underrepresentedmarkets,forexamplefromEasternEurope,facelocalizationissues
relatingtoglobalPFMtools. Thestakeholderwasalsoabletobenefitfromfeatures
that include multi-currency and share price updates for both Finnish and Swedish
54

stocks,whichiscommonlynotavailableinmainstreamfinancialapplications.
Anotheridentifiedcoreimprovementwasthetransitiononreportingfromquarterly
to real-time financial reporting. Previously, the stakeholder was only engaging in
quarterly reviews dueto time consuming process. The stakeholder cannowanalyze
real-timedashboardsinonequickviewandinitiatereportsintopdf. Thisfunctionality
supports the findings of Cederberg (2013), which implied that financial tools with
lessmanualinputsandofferedsimplifiedworkflowsmadeitlikelythatusersfurther
engage with personal finance technologies. Similarly, Shafiee et al. (2024) noted
that real-time, personalized outputs enhance users’ understanding and support more
responsivefinancialdecision-making.
Finally,bydeliveringreal-timeinsightsandvisualfeedbackthroughpiecharts,bar
graphs, and trend visualizations, the application promotes awareness and decision
confidence. Bitrián etal. (2021)foundthatvisualandgamifiedelementscanincrease
users’ perceivedcompetenceandengagement. Similarly, Shafieeetal. (2024)showed
that personalized and real-time financial guidance helps users better understand
complexfinancialfactorsandmakemoreinformeddecisions.
9.2 Limitations of the solution
WhilethePoCsuccessfullyaddressedcorerequirements,severallimitationsremain.
Mostunimplementedfeatureswerecategorizedas“nicetohave”oroptionalandwere
intentionallyexcludedduetothelimitedscopeandtimeframeoftheproject. However,
onecriticalweaknessistheabsenceofuserauthenticationandauthorization. Security
isafundamentalconcerninfinancialtechnology,especiallywheresensitivepersonal
data is involved. Kaye et al. (2014) explains that users are often reluctant to adopt
digitalfinancetoolsduetofearsarounddataaccessandprivacy. Similarly,Handayani
et al. (2024)identify securityand dataprotection as centralfactors influencing user
trustinfintechsolutions. Herralaetal. (2023)furtherarguethatwhenusersfeelalack
ofcontrolovertheirfinancialinformation,itcancontributetostressanddisengagement,
highlightingtheimportanceoftransparentandsecuresystemdesign. Thesefindings
underscoretheimportanceofimplementingbasicaccesscontrolmechanismsinfuture
iterationstostrengthensystemcredibilityandpromotelong-termuse.
Fromadevelopmentperspective,themostsignificantlimitationistheincomplete
automationoffinancialdataretrieval. Althoughthestakeholderexpressedsatisfaction
withthecurrentlevelofautomation,thesystemlacksthescalabilityneededtosupport
broaderuserbase. Ideally, userswould beabletoconnect theirbankandbrokerage
accountsdirectlytotheapplication,allowingautomaticsynchronizationoftransactions
and balances. However, this level of integration remains difficult to implement due
to different factors. Several stock price API’s were investigated such as Finnhub,
stockdata.org,eoddata,andAlphavintage,butwereeventuallydiscardedduetolimited
support for European stocks or were too expensive. Investment brokers also do not
have API’s or they are limited, for example Nordnet offers API only in Sweden.
55

Additionally,fromopen-bankingperspective,someoptionswereinvestigatedsuchas
Yapily, Polygon, andGoCardless. Thesewere notsuitable forthe contextcase asthey
wereeithertargetedforenterprisesorrequiredalotofdevelopmentwork. Another
issuewiththeopen-bankingintegrationsistheautomatedcategorizationwhichwas
pointedoutalsobyKayeetal. (2014).
Asapracticalworkaround,thePoCapplicationintegrateswithGoogleSheetsusing
the functiontoretrievestockprices. Thissolution,whilemanualtoset
GOOGLEFINANCE
up, aligned with the stakeholder’s workflow and allowed real-time pricing without
additional financial costs. Still, the absence of seamless, API-based integration for
broader asset classes and account types remains a major limitation. These findings
supportwhatCederberg(2013)observed: manualdataentryandscatteredtoolsmake
itdifficultforpeopletocontinueusingpersonalfinancesystemsinthelongrun.
Anotherthingtonoteisthestakeholdersgoodfinancialliteracyandthereforehigher
expectationsfromthesystem. Astheyhavetrackedtheirfinancesmorethanadecade,
theyhaveaccumulatedalotofknowledgeandexperienceinthisdomain. However,
some usability improvements and educational content would be beneficial to add
in the current application for more novice users. This need is also reflected in the
literature. Torno et al. (2021) point out that few personal finance applications offer
built-in financial education, despite its potential to increase trust and engagement.
Similarly,Lasmiatun(2024)foundthatyoungerusersoftenturntodigitalplatforms
forfinancialguidanceandpreferinteractiveandvisualformatsforlearning. Kayeetal.
(2014) also noted that many users do not engage with existing all-in-one financial
systems,suggestinganopportunitytodesignmoreaccessibleanduser-tailoredfinancial
experiences.
9.3 Reflection on DSRM
Design Science Research Methodology (DSRM) provided an effective structure
for development of this project. The structured iterative process created a logical
progressionstartingwithaproblemdefinitionstepandendingwithanartifactevaluation
stepwhich was extremely usefulin a solodevelopmentenvironment. DSRM consists
ofsetofstepsas describedbyPeffersetal. (2007)thatenableresearcherstodevelop
solutionstoreal-worldproblemsbythedesignandevaluationofartifacts.
EachphaseoftheDSRM directlyinformedthenext. In DesignandDevelopment
phase,thearchitecturaldecisionswerederivedfromthefunctionalandnon-functional
requirements. The requirements on the other hand were formatted based on the
stakeholderneedsfoundintheProblemidentificationphase. Evaluationphasebenefited
fromtheestablishedobjectivesbutalsoprovidedsubstancetotheirevaluation. This
correspondswiththeguidanceofHevneretal. (2004)thatutility,quality,andefficacy
arenecessarycriteriaofevaluatingdesignartifactsininformationsystemsresearch
context.
56

Having a real stakeholder involved made a big difference in the project. Their
ongoingfeedbackgavepracticalinsightsthatwouldhavebeenhardtodiscoverthrough
theory alone. By taking part in the demonstration and evaluation, they ensured the
solution met real needs and worked in practice. As De Sordi (2021) points out,
involvingpractitionersinDesignScienceResearchmakestheresultsmorerelevant
andstrengthensthecredibilityoftheresearch.
Overall, Design Science Research Methodology gave a clear but flexible way to
work through the project. It made it easier to build a useful and practical solution
whilestillfollowinga solidresearchprocess. Thismade itagoodchoice foraproject
likethisthatcombinesreal-worldneedswithacademicwork.
9.4 Opportunities for future development
TheevaluationphaserevealedseveralkeyopportunitiestoenhancethePoCapplication
and move toward a production-ready solution. The most critical area for future
development is the integration of automated data fetching from banks and brokers.
Implementing such features wouldsignificantlyreduce manual input, enhance user
convenience,andimprovethesystem’sscalabilityforawideraudience. Thisaddresses
alimitationalsoobservedbyTornoetal. (2021)andStefanovetal. (2024),whofound
thatmostPFMtoolslackcomprehensiveintegrationacrossfinancialinstitutions,with
Stefanovetal. (2024)furthernotingthatmanysolutionsofferonlylimitedlocalized
services,reducingtheireffectivenessincertainmarkets.
Usability improvements also emerged as a priority. The stakeholder identified a
range of refinements that would improve the user experience, including the ability
to edit transactions directly, more informative tooltips, and clearer differentiation
betweendetailedbudgetingandhigh-levelcashflowtracking. Thisalignswithfindings
by Cederberg (2013), who described that users value intuitive, visually appealing
interfacesthatreducemanualeffortandsupportfinancialself-awareness. Similarly,
Bitrián et al. (2021) found that clear feedback mechanisms and well-designed user
experiencesfosterperceivedcompetenceandautonomywhicharetwokeydriversof
sustaineduseinpersonalfinanceapplications.
Theadditionofuserauthenticationandauthorizationisessentialforensuringdata
privacy and security, especially if the system is to be deployed beyond the original
stakeholder. On the technical side, the introduction of unit and integration testing,
alongwith comprehensivedocumentation, wouldsupportlong-termmaintainability
andfacilitatecollaborationinlargerdevelopmentteams. Also,splittingthearchitecture
into severalmicroservices wouldincrease scalabilityandincrease performancefora
productionenvironmentwheremoretrafficistobeexpected.
57

10 Conclusions
This thesis covered the design and development of a centralized personal finance
managementapplicationthataddressedtheproblemsfacedbyanindividualstakeholder.
The main issues involved the complexity, fragmentation, and manual workload
that were found in the stakeholder’s existing financial tracking setup. The system
relied on a combination of Excel spreadsheets, third-party apps, and manual data
consolidation. The objective was to create a customized solution that improves
automation, visualization, and reporting while supporting personalized financial
analysis.
The projectfollowedthe DesignScience ResearchMethodology (DSRM),which
providedastructuredanditerativeframeworkwithsixsteps: problemidentification,
objective definition, design and development, demonstration, evaluation, and com-
munication. This methodologysupportedboththe technicalexecutionandacademic
rigoroftheresearchprocess. Eachphaseproducedoutcomesthatcouldbeusedonthe
nextstages,eventuallyresultinginafunctioningproof-of-concept(PoC)application.
The final artifact includes asset tracking such as shares, cash, and real-estates,
categorizedcashflowmonitoring,andfinancialPDFreportgeneration. Inadditionto
constantfeedbackduringthedevelopmentphase,thesefeatureswerevalidatedthrough
task-basedusertestingandstructuredstakeholderfeedback. Comparedtothebaseline
system, the PoC significantly reduced manual effort, improved data reliability, and
offered a centralized view of the user’s financial status. These outcomes align with
findingsintheliterature,whichstressedthatsimplification,visualfeedback,andtrust
areimportantforeffectivepersonalfinancetools.
However, the PoC did not implement several planned features, including user
authentication,customizabledashboards,orfulldataautomationthroughbankingand
broker integrations. These limitations stemmed from external API constraints and
thelimitedscopeofasolodevelopmentprojectandwouldbemainfocusareaifthis
applicationwouldbedeployedtobroaderuse.
Oneofthechallengesfacedduringthisthesiswasfindinggoodliteraturethatreally
looked at how people manage their finances in everyday life. A lot of the existing
researchfocusesonfinancialliteracy,behavior,orplanningtheory,buttherewasnot
muchdetailaboutwhattoolspeopleactuallyuse. Itwashardtofindstatisticsorstudies
aboutwhichappspeoplerelyon,whatworksforthem,andwhatproblemstheyrun
into. Thatisoneofthemainreasonsthisthesiscametolife. Mostappsonthemarket
arebuiltjustforbudgetingortrackingexpenses. WithsimpleGooglesearch“personal
financeapps,”almostallofthemfallintothatcategory. Butmanagingyourfinances
is more than just budgeting. People also want to track investments, assets, and see
theirfullfinancial pictureinone place. Moreresearchis neededthatlooks intohow
peopleactuallymanagetheirfinancesandhowtoolscouldbebuilttosupportthat.
58

References
| Atkinson, | Adele      | and | Flore-Anne |                 | Messy | (2012). |           |                     |           |           |      |
| --------- | ---------- | --- | ---------- | --------------- | ----- | ------- | --------- | ------------------- | --------- | --------- | ---- |
|           |            |     |            |                 |       |         | Measuring |                     | Financial | Literacy: |      |
|           |            |     |            | INFEPilotStudy. |       | Tech.   | rep.      | 15. OECDPublishing. |           |           | doi: |
| Results   | oftheOECD/ |     |            |                 |       |         |           |                     |           |           |      |
|           |            |     |            | .               | url:  |         |           |                     |           |           |      |
10.1787/5k9csfs90fr4-en https://www.oecd.org/content/dam/oecd/
en/publications/reports/2012/03/measuring-financial-literacy_g17a210b/
.
5k9csfs90fr4-en.pdf
Bitrián,Paulaetal. (2021). “Makingfinancefun: thegamificationofpersonalfinancial
managementapps”. In: InternationalJournalofBankMarketing39.7,pp.1310–
| 1332. | doi: |                           |     |     |     | . url: |                               |     |     |     |     |
| ----- | ---- | ------------------------- | --- | --- | --- | ------ | ----------------------------- | --- | --- | --- | --- |
|       |      | 10.1108/IJBM-02-2021-0074 |     |     |     |        | https://doi.org/10.1108/IJBM- |     |     |     |     |
.
02-2021-0074
| Brush, | Kate (2023). |     |        |     | method. TechTarget |     | definitions. |     | url:         |     |     |
| ------ | ------------ | --- | ------ | --- | ------------------ | --- | ------------ | --- | ------------ | --- | --- |
|        |              |     | MoSCoW |     |                    |     |              |     | https://www. |     |     |
.
techtarget.com/searchsoftwarequality/definition/MoSCoW-method
Cederberg,Jessica(2013). “ChangingFinancialBehaviorsUsingMobilePFMTools
| (Dissertation)”. |     |     | In: Södertörn |     | University, | Sweden. |     | url: |     |     |     |
| ---------------- | --- | --- | ------------- | --- | ----------- | ------- | --- | ---- | --- | --- | --- |
https://urn.kb.se/
.
resolve?urn=urn:nbn:se:sh:diva-19735
De Sordi, José Osvaldo (2021). Design Science Research Methodology: Theory
Development from Artifacts. 1st. Palgrave Macmillan Cham. doi:
https:
.
//doi.org/10.1007/978-3-030-82156-2
DiDomenico,StefanoI. etal. (2022). “Motivationsforpersonalfinancialmanagement:
ASelf-DeterminationTheoryperspective”. In: FrontiersinPsychologyVolume13
| -2022. | issn: | 1664-1078. |     | doi: |                           |     |     |     | . url:       |     |     |
| ------ | ----- | ---------- | --- | ---- | ------------------------- | --- | --- | --- | ------------ | --- | --- |
|        |       |            |     |      | 10.3389/fpsyg.2022.977818 |     |     |     | https://www. |     |     |
.
frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.977818
| Enstrom, | D.  | W. (2018). |            |     |               |     | Decision. |     |                      |     |     |
| -------- | --- | ---------- | ---------- | --- | ------------- | --- | --------- | --- | -------------------- | --- | --- |
|          |     |            | Guideline: |     | Architectural |     |           |     | https://www.unified- |     |     |
am.com/UAM/UAM/guidances/guidelines/uam_architectural_decision_BAE7AFA2.
|     | . UnifiedArchitectureMethod(UAM). |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
html
French,Declanetal. (2021). “Personalfinanceappsandlow-incomehouseholds”. In:
| StrategicChange30,pp.367–375. |     |     |     |     | doi: |     |     |     | .   |     |     |
| ----------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
10.1002/jsc.2430
Gafrikova,V. etal. (2015). “Onlinepersonalfinancemanagementapplications”. In:
In-
| formationSystemsinManagement4.1,pp.39–52. |     |     |     |     |     |     | url: |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
https://bibliotekanauki.
.
pl/articles/94727
Gitman,L.J. etal. (2011). Personalfinancialplanning. 12th. South-WesternCengage
| Learning. |     | isbn: | 978-1-4390-4447-6. |     |     |     |     |     |     |     |     |
| --------- | --- | ----- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Handayani, Tika et al. (2024). “Fintech Analysis of Personal Finance App Usage
among Millennials”. In: Journal of Economic Education and Entrepreneurship
| Studies5,pp.150–162. |     |     |     | doi: |     |     |     | .   |     |     |     |
| -------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
10.62794/je3s.v5i2.2299
Herrala, Juha-Matti et al. (2023). “How Personal Finance Management Systems
Emancipate and Oppress Young People”. In: Proceedings of the 56th Hawaii
International Conference on System Sciences, pp. 5542–5550. doi:
10.24251/
.
HICSS.2023.675
Hevner,AlanR. etal. (2004). “DesignScienceinInformationSystemsResearch”.
| In: MISQuarterly28.1,pp.75–105. |     |     |     |     | doi: |     |     |     |     |     | .   |
| ------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.2307/25148625
Huang, Lisha (2016). “Personal Financial Planning for College Graduates”. In:
| Technology |     | and | Investment | 7,  | pp. 123–134. |     | doi: |     |     |     | . url: |
| ---------- | --- | --- | ---------- | --- | ------------ | --- | ---- | --- | --- | --- | ------ |
10.4236/ti.2016.73014
.
https://doi.org/10.4236/ti.2016.73014
59

Ironhack (2024). Functional vs Non-Functional Requirements: Understanding the
| Core Differences |     | and | Examples. | Ironhack | blogs. | url: |     |     |
| ---------------- | --- | --- | --------- | -------- | ------ | ---- | --- | --- |
https://www.ironhack.
com/gb/blog/functional-vs-non-functional-requirements-understanding-
.
the-core-differences-and
Kaye, Joseph Jofish et al. (2014). “Money talks: tracking personal finances”. In:
ProceedingsoftheSIGCHIConferenceonHumanFactorsinComputingSystems.
AssociationforComputingMachinery,pp.521–530. isbn: 9781450324731. doi:
|     |     |     | . url: |     |     |     |     | .   |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- |
10.1145/2556288.2556975 https://doi.org/10.1145/2556288.2556975
Lai, Ming-Ming and Wei-Khong Tan (2009). “An Empirical Analysis of Personal
FinancialPlanninginanEmergingEconomy”. In: EuropeanJournalofEconomics,
| FinanceandAdministrativeSciences. |     |     |     | issn: | 1450-2275. |     |     |     |
| --------------------------------- | --- | --- | --- | ----- | ---------- | --- | --- | --- |
Lasmiatun, KMT (2024). “The Role of Financial Education in Improving Personal
FinancialPlanning: AQualitativeStudyonGeneration Z”. In: Nomico1, pp.149–
| 158. doi: |     |     |     | .   |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- |
10.62872/8n585q36
Lusardi, Annamaria and Olivia S. Mitchell (2014). “The Economic Importance of
| Financial     | Literacy: | Theory | and | Evidence”. |     | In:     |             |            |
| ------------- | --------- | ------ | --- | ---------- | --- | ------- | ----------- | ---------- |
|               |           |        |     |            |     | Journal | of Economic | Literature |
| 52.1,pp.5–44. |           | doi:   |     |            |     |         | .           |            |
https://doi.org/10.1257/jel.52.1.5
Peffers,Kenetal. (2007). “Adesignscienceresearchmethodologyforinformation
systems research”. In: Journal ofManagementInformation Systems 24, pp. 45–77.
| doi: |     |     |     | .   |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
10.2753/MIS0742-1222240302
Rajesh, R.J. and K.V. Giridhar (2024). “Financial literacy and personal financial
management: Smart movestowardspersonalfinance”. In: ShanlaxInternational
| Journal | of Arts, | Science | and | Humanities | 12.S1, | pp. 62–67. | doi: |     |
| ------- | -------- | ------- | --- | ---------- | ------ | ---------- | ---- | --- |
https://doi.
. url:
org/10.34293/sijash.v12iS1-Oct.8285 https://shanlaxjournals.in/
.
journals/index.php/sijash/article/view/8285
Shafiee,Saraetal. (2024). “ImprovingFinancialLiteracyandSupportingFinancial
| Decisions: | DevelopingaPersonalizedConfigurator”. |     |     |     |     | In: |     |     |
| ---------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
JournaloftheKnowledge
| Economy | 15, | pp. 14256–14285. |     | doi: |     |     |     |     |
| ------- | --- | ---------------- | --- | ---- | --- | --- | --- | --- |
https://doi.org/10.1007/s13132-023-
.
01651-9
Shah,SweetyandAmolaBhatt(2014). “UnderstandingPracticesofPersonalFinancial
Planning (PFP)”. In: Internationalconferenceon “Roleof FinancialIndustryin
AcceleratingEconomicGrowth”organisedbyGujaratTechnologicalUniversity
(GTU)-CentreforFinancialServices,Ahmedabad.
Siegel, R. and C. Yacht (2009). Finance. Saylor Foundation. isbn:
Personal
| 9780982361863. |     | url: |     |     |     |     |     | .   |
| -------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
https://open.umn.edu/opentextbooks/textbooks/31
Stefanov, Tihomir et al. (2024). “Personal Finance Management Application”. In:
| TEMJournal |     | 13,pp.2066–2075. |     | doi: |     |     | .   |     |
| ---------- | --- | ---------------- | --- | ---- | --- | --- | --- | --- |
10.18421/TEM133-34
Torno, Albert et al. (2021). “More than Mobile Banking – A Taxonomy-based
AnalysisofMobilePersonalFinance Applications”. In: PACIS 2021Proceedings.
| 179. url: |     |     |     |     |     | .   |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://aisel.aisnet.org/pacis2021/179
Vaishnavi, V.K. and W. Kuechler (2015). Design Science Research Methods and
|           |            |     |             |     |               |     | Technology. | 2nd. CRC |
| --------- | ---------- | --- | ----------- | --- | ------------- | --- | ----------- | -------- |
| Patterns: | Innovating |     | Information | and | Communication |     |             |          |
| Press.    | doi:       |     |             |     |               | .   |             |          |
https://doi.org/10.1201/b18448
60