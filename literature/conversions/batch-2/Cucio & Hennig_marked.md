---
conversion_metadata:
  converted_at: "2026-07-22T13:02:45Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Cucio & Hennig.pdf"
  source_pdf_sha256: "f612cb93ff643d534cdd336cd8987ed2d26a5e7f13c0814ffe3a58c2337ee23c"
  page_count: 34
  markdown_char_count: 174141
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Artificial Intelligence and 
the Philippine Labor 
Market: Mapping 
Occupational Exposure 
and Complementarity

Micholo Cucio and Tristan Hennig

WP/25/43

IMF Working Papers describe research in 
progress by the author(s) and are published to 
elicit comments and to encourage debate. 
The views expressed in IMF Working Papers are 
those of the author(s) and do not necessarily 
represent the views of the IMF, its Executive Board, 
or IMF management.

2025 
FEB

---

<!-- PAGE 2 -->

© 2025 International Monetary Fund

WP/25/43

IMF Working Paper 
APD

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity 
Prepared by Micholo Cucio and Tristan Hennig*

Authorized for distribution by Maria Gonzalez 
February 2025

IMF Working Papers describe research in progress by the author(s) and are published to elicit 
comments and to encourage debate. The views expressed in IMF Working Papers are those of the 
author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper combines labor force survey microdata with measures of occupational AI exposure 
and complementarity to examine the potential impact of recent advancements in AI on the Philippine labor 
market. We find that around one third of workers are highly exposed to AI with around sixty percent of those 
also rated highly complementary, indicating potential productivity gains. College-educated, young, urban, 
female, and well-paid workers in the services sector are most exposed. Business process outsourcing (BPO) is 
identified as the sector with the highest proportion of jobs at risk of displacement. Addressing regulatory gaps, 
infrastructure needs, and workforce reskilling is crucial to maximize benefits and mitigate negative impacts.

RECOMMENDED CITATION: M. Cucio and T. Hennig “Artificial Intelligence and the Philippine Labor Market: 
Mapping Occupational Exposure and Complementarity” IMF Working Paper No. 25/43, February 2025

JEL Classification Numbers:

J21, J23, J24, J31, M54, O15, O53

Keywords:

Artificial Intelligence (AI), Labor Market, Philippines, Business 
Process Outsourcing (BPO), AI Exposure and Complementarity

Author’s E-Mail Address:

CucioMI@bsp.gov.ph and Thennig2@imf.org

* This paper has benefitted tremendously from comments by Elif Arbatli Saxegaard, Elmer Li, Maria Cynthia Sison, the Bangko
Sentral ng Pilipinas (BSP), the Philippine National Economic and Development Authority, as well as seminar audiences at the BSP
and IMF. We would also like to thank the Philippine Statistics Authority for providing the Labor Force Survey microdata, the IMF
Resident Representative Office in Manila under the helm of Ragnar Gudmundsson for facilitating the data transmittal and the
conversation with the authorities, and Carlo Pizzinelli for providing the AI complementarity scores.

---

<!-- PAGE 3 -->

WORKING PAPERS

Artificial Intelligence and the 
Philippine Labor Market: Mapping 
Occupational Exposure and 
Complementarity

Prepared by Micholo Cucio and Tristan Hennig1

---

<!-- PAGE 4 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Contents

Executive Summary ............................................................................................................................................ 3

I. Introduction ...................................................................................................................................................... 4

II. Context ............................................................................................................................................................. 7

A. The Philippine Labor Market ..................................................................................................................... 7

B. The BPO Industry ...................................................................................................................................... 8

III. Existing Literature ...................................................................................................................................... 11

IV. Data and Methodology ............................................................................................................................... 13

V. Analysis and Labor Market Implications .................................................................................................. 14

VI. AI Preparedness ......................................................................................................................................... 18

VII. Regulatory Framework ............................................................................................................................. 20

VIII. Policies to Foster AI Adoption and Harness its Benefits ..................................................................... 22

References ......................................................................................................................................................... 25

Appendix  ........................................................................................................................................................... 28

BOXES

1. The History of Artificial Intelligence ......................................................................................................... 6 
2. Types of BPO Services ........................................................................................................................... 9

FIGURES

1. The Philippine Labor Force: Key Summary Statistics ............................................................................. 7 
2. Unemployment and Labor Force Participation ........................................................................................ 8 
3. Evolution of Pay in Real Terms ............................................................................................................... 8 
4. BPO Export Revenues .......................................................................................................................... 10 
5. BPO Employment .................................................................................................................................. 10 
6. Exposure and Complementarity Across Occupations ........................................................................... 13 
7. AI Exposure by Occupation ................................................................................................................... 28 
8. Exposure and Complementary by Gender, Age, Education, Wage, Location, and Sector ................... 28 
9. AI Preparedness Across Asia ................................................................................................................ 19 
10. National AI Strategy Pillars, Dimensions, Imperatives .......................................................................... 20 
11. AI Exposure by Occupation, Gender, and Education ............................................................................ 28 
12. Exposure and Complementary by Activity within Services .................................................................... 28 
13. Exposure and Complementarity by Class of Worker ............................................................................. 28

TABLES 
International Market Share of the Philippines’ BPO Industry ................................................................. 10 
1.
2. AI Exposure and Complementarity in the Philippines ............................................................................ 14 
3. AI Exposure and Complementarity in the Philippines and Asia ............................................................. 30

INTERNATIONAL MONETARY FUND

2

---

<!-- PAGE 5 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Executive Summary

This paper examines the potential impact of recent advancements in artificial intelligence (AI) on the labor 
market in the Philippines. The Philippines faces unique challenges and opportunities due to its large BPO 
sector—a significant contributor to the national economy. We build on the occupational classification framework 
proposed by the Cazzaniga et al. (2024), which is in turn based on the work of Felten et al. (2021) and 
Pizzinelli et al. (2023). Felten et al. develop an AI exposure index capturing the overlap between AI capabilities 
and occupational tasks, while Pizzinelli et al. introduce an AI complementarity score assessing how AI might 
enhance or replace human roles, considering required skill levels and societal context. By combining these 
measures, occupations are categorized into high exposure/high complementarity, high exposure/low 
complementarity, and low exposure groups. The primary innovation of this paper is linking these classifications 
to the specific circumstances of the Philippines by merging the AI exposure and complementarity scores with 
microdata from the Philippine Statistics Authority's October 2022 Labor Force Survey, comprising over 180,000 
observations, 80,000 of which are tagged as “employed”. This approach provides a granular analysis of 
occupations potentially affected by AI and correlates AI exposure with demographic indicators.

We find that around one third of occupations in the Philippines are highly exposed to AI, meaning that many of 
the tasks could be performed by AI technologies. 61% of these highly exposed jobs are also rated as highly 
complementary, suggesting that AI is likely to augment rather than replace these roles, potentially increasing 
productivity. The remainder (14% of the total workforce) hold jobs with low complementarity, making them 
susceptible to displacement by AI. College-educated, young, urban, female, and well-paid workers in the 
service sector are most exposed to AI. These groups however also tend to occupy roles with high 
complementarity, indicating they may be better positioned to leverage AI advancements as the nature of work 
evolves. While BPO workers are classified as highly exposed with low complementarity, they represent only 
about 3% of the total workforce. Nonetheless, the BPO sector's significant contribution to the economy—
accounting for 7.4% of GDP in 2023, similar in magnitude to remittances—means that changes within this 
industry are macro-critical and may have spillover effects on the broader economy.

The Philippine government has recognized the transformative potential of AI and is actively working to harness 
its benefits for national development, despite the absence of a comprehensive legal framework. The National 
AI Strategy Roadmap, first introduced in 2021 and updated in 2024, outlines a strategic vision for integrating AI 
across various sectors to boost competitiveness, foster research and development collaboration, and prepare 
the workforce for future jobs while ensuring responsible AI governance. Complementing this initiative, the 
Trabaho Para sa Bayan Act aims to align education with industry needs and generate job opportunities amid 
technological change. Additionally, several bills are under consideration to establish regulatory and 
developmental bodies for AI, reflecting a proactive stance toward AI development and regulation.

Despite these efforts, challenges persist, including regulatory gaps, inadequate infrastructure, workforce 
reskilling needs, and limited AI adoption due to cost concerns. Addressing these issues is crucial for the 
Philippines to fully leverage AI's economic and societal benefits. The analysis in this paper can inform 
strategies to mitigate negative consequences, such as job displacement, and maximize positive outcomes, 
such as increased productivity and the creation of new job categories. Investments in education and training 
programs focused on AI and digital skills are essential to prepare the workforce for the future. Furthermore, 
developing a regulatory framework that ensures the ethical use of AI and addresses issues related to labor 
market transitions is imperative, drawing on lessons from global best practices.

INTERNATIONAL MONETARY FUND

3

---

<!-- PAGE 6 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

I. Introduction

Recent advances in the development and public availability of artificial intelligence (AI) are likely to significantly 
transform economies across the globe. One of the most notable advancements is the development of 
generative AI models, such as OpenAI's GPT-4 and Google's Gemini. These models have revolutionized 
natural language processing, enabling machines to understand and generate human-like text with 
unprecedented accuracy. Their output has wide-ranging applications, including in content creation, coding, and 
problem-solving, which could allow businesses to automate tasks, enhance customer service, and optimize 
decision-making processes. As a result, industries ranging from healthcare to finance are beginning to integrate 
AI-driven tools into their operations, promising efficiency gains and innovation opportunities. Recent advances 
build on a long history of research and development which is outlined in greater detail in box 1.

This paper studies the potential impact of these rapid technological advancements on the labor market in the 
Philippines. As AI systems become more capable and readily available, they are likely to replace or significantly 
alter many job roles, particularly those involving routine and repetitive tasks. The Philippines, with its large 
business process outsourcing (BPO) sector, faces unique challenges and opportunities. The BPO industry, a 
significant contributor to the country's economy, might experience shifts as AI-driven chatbots and virtual 
assistants handle more customer service tasks. However, AI could also create new opportunities, fostering 
growth in tech-driven industries and necessitating a workforce with advanced digital skills.

We follow the occupational classification proposed by Cazzaniga et al. (2024) which is in turn based on work by 
Felten et al. (2021) and Pizzinelli et al (2023). This strand of the literature considers occupations to be a list of 
tasks. Felten et al. (2021) develop an AI “exposure” index that captures the overlap between the capabilities of 
recent gen-AI tools and the tasks required for each occupation. Pizzinelli et al. (2023) develop an AI 
complementarity score which considers the required skill level for each occupation as well as its societal 
context to evaluate how shielded each job is from AI-driven replacement. Combining these two measures, each 
occupation can therefore be categorized as either “high exposure/high complementarity”; “high exposure/low 
complementarity”; and “low exposure” where the median exposure or complementarity score respectively 
serves as the cutoff value between the high and low categories.

The main innovation of this paper is to connect the findings from the academic literature on occupational AI 
exposure and complementarity to the specific circumstances of the Philippines. We merge the above-
mentioned classification of occupations with labor force survey microdata provided by the Philippine Statistics 
Authority (PSA). We use the October 2022 vintage of the Philippine labor force survey which contains 183,602 
observations of 52 variables. By using microdata rather than aggregated data from the International Labor 
Organization (ILO), we obtain a more granular picture of the distribution of occupations potentially affected by 
AI and are also able to correlate AI exposure with other demographic indicators.

We find that around one third of occupations in the Philippines are highly exposed to artificial intelligence. This 
means that their jobs entail tasks which can now be performed by AI. 61% of those highly exposed jobs are 
however also rated as highly complementary, meaning that artificial intelligence is likely to support rather than 
replace the worker, potentially increasing their productivity. The remaining low complementarity jobs, which 
represent 14% of the total workforce, are at risk of being replaced by AI.

Looking at other socioeconomic indicators recorded in the labor force survey, we find that college educated, 
young, urban, female, and well-paid workers in the service sector are most exposed. However, these

INTERNATIONAL MONETARY FUND

4

---

<!-- PAGE 7 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

characteristics also correlate with complementarity, suggesting that these workers may also be better placed to 
take advantage of AI as the nature of work evolves.

While BPO workers are classified as highly exposed with low complementarity in our analysis, BPO sector 
employees only make up about 3 percent of the total workforce. They therefore have less influence on the 
aggregate numbers than one might have otherwise expected. Having said that, the nature of work in the BPO 
sector will undoubtedly undergo substantial shifts in the wake of AI adoption and there may be spillovers to 
other parts of the economy which would not be captured by the analysis in this paper. Given the size of BPO 
sector revenues (7.4 percent of GDP in 2023, and similar in magnitude to remittances), changes in the BPO 
sector will therefore still be macro critical.

The Philippine government has recognized the transformative potential of AI and is actively working to harness 
its benefits for national development, although there is no comprehensive legal framework for the time being. 
The National AI Strategy Roadmap, first introduced in 2021 and updated in 2024, outlines a strategic vision for 
integrating AI across various sectors to boost competitiveness, foster R&D collaboration, and prepare the 
workforce for future jobs while ensuring responsible AI governance. Complementing this initiative, the Trabaho 
Para sa Bayan Act (Republic Act No. 11962) aims to align education with industry needs and generate 
employment opportunities in the face of technological change. Concurrently, several bills are under 
consideration to establish regulatory and developmental bodies for AI, reflecting a proactive stance towards AI 
development and regulation. However, challenges persist, including regulatory gaps, inadequate infrastructure, 
workforce reskilling needs, and limited AI adoption due to cost concerns.

Addressing these issues will be crucial for the Philippines to fully leverage AI's economic and societal benefits. 
The analysis in this paper can help inform strategies to mitigate negative consequences, such as job 
displacement, and maximize positive outcomes, such as increased productivity and the creation of new job 
categories. Investments in education and training programs focused on AI and digital skills will be essential to 
prepare the workforce for the future. Furthermore, regulatory frameworks need to be developed to ensure the 
ethical use of AI and to address issues related to labor market transitions. These should draw on lessons from 
global best practices in regulating and ensuring ethical AI use. By proactively studying AI's impact, the 
Philippines can better navigate the technological transformation and ensure inclusive economic growth.

INTERNATIONAL MONETARY FUND

5

---

<!-- PAGE 8 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Box 1. The History of Artificial Intelligence

The origins of Artificial Intelligence (AI) can be traced back to 1943 when Warren McCullock and Walter Pittz 
published their work in the Bulletin of Mathematical Biophysics. They introduced the concept of networks 
composed of artificial neurons and how these networks could perform basic logical problems. Their work 
established the foundation for computer-based neural networks and deep learning. In 1950, Alan Turing 
wrote “Computing Machinery and Intelligence” which defined the complexities of defining intelligence. 
Turing’s proposal noted that a computer that was capable of conversing without being distinguished from 
human interaction could loosely be regarded as having cognitive abilities, this became a test known as the 
Turing test.

Pioneering developments in AI such as the Manchester Mark I were characterized by machines and limited 
capabilities and focused on fundamental applications. At the Dartmouth Summer Research Project in 1956, 
the Logic Theory Machine, funded by the Research and Development Corporation (RAND) was introduced. 
The program was designed to mimic human’s problem-solving skills, and it was considered by many to be 
the first AI program. The following years saw significant advancements in AI, such as the development of 
the Symbolic Automatic Integrator (SAINT) by James Slagle in 1961, which can solve calculus problems at 
a freshman level, and the creation of ELIZA, as an early natural language processing computer, by Joseph 
Weizenbaum in 1965.

Despite the slowdown of interest in AI during the 1970s, SHRDLU, a program which could utilize virtual 
robotic arms to manipulate virtual blocks, respond to commands in plain English and explain the necessity 
of its actions was developed in 1971. Paul Werbos, an American social scientist conceptualized a method of 
training artificial neural networks through backpropagation of errors. In 1975, Ted Shortliffe introduced 
MYCIN, a medical diagnostic system that influenced future expert systems despite its limited use due to its 
slow response speed. During the Gulf War, the Defense Advanced Research Projects Agency’s (DARPA) 
Dynamic Analysis and Replanning Tool (DART) showcased AI’s practical applications revolutionizing the 
logistics planning and allocation of resources in the battlefield.

The introduction of domestic AI products like Furby and AIBO opened AI for domestic consumption. 
Advancements in technology in 2005 enabled companies to monitor web and media activity, facilitating 
personalized product recommendation based on individual interests of customers. In 2017, Large Language 
Models (LLMs) were introduced which are trained on enormous amounts of data to provide the foundational 
capabilities needed to drive multiple use cases and applications. In 2018, the first Generative Pre-Trained 
Transformer (GPT) algorithm was introduced which used deep learning to generate a variety of output such 
as computer codes, poetry, and writing an essay. In 2022, Open AI debuted ChatGPT, an AI chatbot which 
is capable of various functions such as chat support, content creation, and translation among others. The 
introduction spurred the interest of the public and within two months, it reached 100 million users. In 
comparison, the internet and mobile phone took twenty years to reach 80 percent of countries. It has also 
galvanized other technology companies to innovate and introduce their own GPT versions such as Google’s 
Gemini, Microsoft’s Bing AI, and Meta’s Llama and has led to a dramatic increase of AI patents from 2015-
2022, highlighting the swift progress made in AI development.

INTERNATIONAL MONETARY FUND

6

---

<!-- PAGE 9 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

II. Context

A.  The Philippine Labor Market

Figure 1 presents several basic summary statistics that help set the context for our analysis of the Philippine 
labor market and its exposure to artificial intelligence. The bulk of the workforce works in the services sector, 
with the rest broadly evenly split between agriculture and industry. There is a sizeable gap in the labor force 
participation between men and women with 75% of working age men either working or looking for work while 
the same is only true for 53% of women. Most working Filipinos’ highest educational degree is the (junior) high 
school diploma though just over a quarter do hold a college degree. The most common employment is a 
salaried position (i.e., in a private company, the government, or for a private household), followed by self-
employment, and being an unpaid family worker. While the analysis in this paper focuses on the current state 
of the labor market, it is important to acknowledge long-running trends in some of the variables depicted in 
Figure 1 – for example, the share of employment in agriculture has seen steady declines while the share in 
industry and particularly services has increased over time.

Figure 1. The Philippine Labor Force: Key Summary Statistics

Source (for all graphs): Philippine Statistics Authority (data, April 2024 vintage), Own calculations

INTERNATIONAL MONETARY FUND

7

---

<!-- PAGE 10 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

During COVID-19, unemployment spiked, and the labor force participation rate dropped (Figure 2). However, 
this shock gradually dissipated as the pandemic faded and the economy reopened. As of April 2024, the 
unemployment rate was 4.0%, below pre-pandemic levels, and the labor force participation rate has also 
recovered to pre-pandemic levels though its measurement has arguably become somewhat noisier in recent 
years. There is also significant underemployment, with 10-15% of employed workers looking for additional work 
or wanting longer hours of work.

Figure 2. Unemployment and Labor Force Participation

Figure 3 shows the evolution of wages over the past 
15 years. The minimum wage for the national capital 
region (NCR) kept pace with inflation until COVID-19 but 
fell behind during the post-pandemic surge in inflation. 
Average daily basic pay, meanwhile, rose faster than 
inflation, bestowing workers with a roughly 30% real 
wage increase since 2009. The fact that the minimum 
wage did not make any gains in real terms over this time 
frame suggests that most of the real wage increases 
were concentrated in jobs with higher pay. These are 
likely the jobs that require specific skills or education to 
perform.

B.  The BPO Industry

Figure 3. Evolution of Pay in Real Terms

Wages and Inflation in the Philippines
(Index, 2009=100)

Average Daily Basic Pay

NCR Minimum Wage

Real Average Daily Basic Pay

Real NCR Minimum Wage

240

220

200

180

160

140

120

100

80

2009

2011

2013

2015

2017

2019

2021

2023

S

CEIC

The Philippine economy is supported by its large service sector driven economy. In 2023, the services sector, 
as a share of total of Gross Domestic Product (GDP) accounted for 62.3 percent. In terms of employment, the 
April 2024 labor force survey from the Philippine Statistics Authority (PSA) noted that the services sector 
accounted for a large share of employment at 61.4 percent. A key driver of growth in the services sector has 
been the country's large Business Process Outsourcing (BPO) industry, which started in 1992. Offshore 
outsourcing has allowed multi-national corporations in developed economies to conduct commercial operations 
in a more cost-effective manner by tapping into a pool of highly skilled individuals in developing economies. 
This has resulted in 20-40 percent reduction in costs even factoring in additional costs such as business setup 
and infrastructure access (Marasigan, 2015).

INTERNATIONAL MONETARY FUND

8

---

<!-- PAGE 11 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

The Philippines holds a significant portion of the global outsourcing market, estimated at 15 percent.1 This is 
supported by the presence of 788 BPO companies, as reported by the Philippine Economic Zone Authority.2 In 
2023, the BPO sector generated US$35.5 billion in revenues, an increase of 9 percent over the previous year, 
or 8.1 percent of the country's total GDP. It also employs 1.7 million Filipinos, equivalent to 3.4 percent of the 
total labor force as of 2023 (Figures 4 and 5). Despite its small share in the country's labor market, the 
industry's presence in various cities throughout the archipelago generates positive spillovers to other sectors of 
the economy, such as the property and services sector. Additionally, BPO revenues are substantial and nearly 
as large as overseas remittances. The industry's ongoing expansion is fueled by robust government support, 
low labor costs, abundant pool of service-oriented, English speaking and young workforce, and a conducive 
business environment. The BPO sector in the country is composed of several business segments, in which the 
majority of the revenues are generated by contact centers and back-office support services (Box 2).

The IT & Business Process Association of the Philippines (IBPAP) highlights that North America remains the 
dominant market for the BPO industry with a 70 percent share. This is attributed to the region's extensive 
English-speaking population, cost-effective labor, and close cultural ties with the United States. Europe and the 
Asia-Pacific Region each hold 15 percent of the market share. Europe leverages the industry for its distinctive 
talent specialization and cost efficiency. Conversely, the Asia-Pacific Region leverages on the relative lack of 
onshore BPO centers for client markets, geographical proximity, and time zone overlap.

Box 2. Types of BPO Services

Contact Center - Consist of in-bound and outbound voice operation services for the purpose of sales, 
customer service, technical support, and others.

Back Office - Service related to finance and accounting and human resource administration.

Data Transcription - Provision of transcription services for interpreting oral dictation of health professionals, 
dictations during legal proceedings, and other data encoding services.

Animation - Process of giving the illusion of movement to cinematographic drawings, models or inanimate 
objects through 2D, 3D, etc.

Software Development - Analysis and design, prototyping, programming, and testing, customization, 
reengineering, and conversion, installation and maintenance, education and training of systems software, 
middleware and application software.

Engineering Development - Includes engineering design for civil works, building and building components, 
ship building, and electronics.

Digital Content - Creation of products that are available in digital form, such as music, information, and

images that are available for download or distribution on electronic media.

Source: Department of Trade and Industry (DTI), Locsin (2006), The Computer Language Company Inc. (2006)

1 https://www.magellan-solutions.com/blog/whats-the-number-analysis-of-the-latest-statistics-of-the-bpo-industry/ 
2 https://www.magellan-solutions.com/studies/call-center-benchmarking-report/

INTERNATIONAL MONETARY FUND

9

---

<!-- PAGE 12 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Figure 4: BPO Export Revenues 
In US$ Billion

Figure 5: BPO Employment 
In ‘000s

Table 1: International Market Share of the Philippines’ BPO Industry

In Percent

Industry

Percent Share

Banking, Financial Services, and Insurance (BFSI)

Technology, media, and telecom (TMT) 
Retail  
Healthcare  
Manufacturing 
Energy 
Others

Source: IBPAP, data as of 2023

25%

14-18% 
14-18% 
11-15% 
6% 
6% 
25%

Pre-pandemic, the BPO industry, one of Manila's economic jewels largely perceived the risk of AI as limited. 
The industry found solace in the fact that AI was not yet capable of demonstrating what customers needed: 
empathy, problem-solving skills, or engaging in English conversations. However, this perspective underwent a 
significant shift.  The BPO Industry Employees Network, a call-center union noted that improvements in AI 
software have led to improved services at the expense of people's jobs. The union added that AI has turned 
into an adversary and is powerless to halt its progress. Outsourcing advisory firms have warned that the 
industry could face substantial job losses due to AI in the next five years (Avasant, 2024). On the other hand, 
AI is also expected to create new jobs such as data curation and algorithm training (Bloomberg, 2024).

Meanwhile, IBPAP noted that AI is both an opportunity and a challenge to the sector. It recognized the 
challenges that employees need to face such as improving skills in data handling, sharpening emotional 
intelligence and creativity through training courses and partnering with educational institutions. On the other 
hand, it acknowledged the potential benefits that can lead to the adoption of AI such as boosting productivity 
and improving customer experience, reduction of costs, and revenue growth.

INTERNATIONAL MONETARY FUND

10

---

<!-- PAGE 13 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Before, the threat of automation was contained to low-skilled, blue-collar jobs. However, generative AI's 
capabilities now pose a threat to white-collar jobs, especially for IT-BPM workers as customer services agents, 
tech support, and non-university educated employees. The Department of Labor and Employment (DOLE) has 
acknowledged that Filipinos are already losing jobs due to AI. In contrast, a survey conducted by Microsoft and 
LinkedIn showed that Filipino professionals are actively incorporating AI to their workflows. It indicated that 86 
percent of Filipino professional workers that have been surveyed already use AI in some form, higher than the 
global average of 75 percent. Meanwhile, 55 percent of Filipinos who were surveyed are worried that their 
organizations lack plans and visions for implementing AI. Ng, et al. (2023) noted that generative AI can unlock 
US$79.3 billion in productive capacity, or equivalent to one-fifth of the country's 2022 GDP by 2030 especially 
in the country's manufacturing and Wholesale and Retail Trade sectors, largely due to its large share in the 
local workforce. In addition, GenAI is foreseen to complement the workforce, rather than replacing people 
entirely. The study noted that only one percent of the workforce would see GenAI utilized more than 20 percent 
of the work while 56% of workers in the Philippines will potentially use generative AI for between 5-20% of their 
regular work activities. Indeed, BPO companies have started to introduce AI assistant or copilots working 
alongside humans.

III.  Existing Literature

The academic literature has approached the study of AI through the lens of task-based models such as 
Acemoglu and Restrepo (2019) which were originally developed to study the impact of automation and 
robotics. This literature has identified three main channels through which automation may impact 
macroeconomic outcomes such as GDP, unemployment, and the income shares of capital and labor. 
Automation or AI may cause unemployment by replacing labor with machines (displacement), it may increase 
the productivity of existing capital or labor (productivity), and it may even generate new tasks and new jobs for 
producing and maintaining these machines (reinstatement)3.

There is no consensus in the academic literature on the magnitude or relative importance of these channels. 
Frank et al. (2019) classifies researchers as either doomsayers or optimists but there are also prominent 
academics arguing that little change will come about. In terms of the most recent debate on the productivity 
impact of generative artificial intelligence, the two ends of the spectrum have been shaped by Acemoglu (2024) 
and Korinek (2024). Acemoglu (2024) argues that AI will bring only marginal TFP improvements of no more 
than 0.71% over ten years while Korinek (2024) predicts that the inevitable advent of artificial general 
intelligence will make all human work obsolete and drive the income share of labor to zero.

Empirical and experimental work has focused on more near-term and immediately quantifiable metrics. One 
strand looks at the overlap between occupational tasks and the capabilities of AI (Felten et al. 2021; Pizzinelli 
et al. 2023; Eloundou et al., 2023, Webb 2020). Gmyrek et al. (2023) even employ AI itself (GPT-4) to estimate 
task-level exposure scores. Brynjolfsson et al. (2023) find that generative AI increases the productivity of 
novice contact center workers the most while experienced workers benefit little. Others have studied labor 
market outcomes - Hui, Reshef, Zhou (2023) find that writing-related occupations and freelancers saw a 2.0 
percent decline in the number of monthly jobs and a 5.2 percent decrease in monthly wages following the 
public availability of generative AI.

3 See Berg et al. (2024) for a more detailed discussion of these channels.

INTERNATIONAL MONETARY FUND

11

---

<!-- PAGE 14 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

In the context of emerging markets, Das and Hilgenstock (2018) studied 160 countries from 1969 to 2015 and 
noted that EM economies are less susceptible to routinization and thus automation as production in these 
economies is less capital intensive, with manual and mainly low-skilled occupations which are not easily 
automated. In addition, the authors noted that the large degree of informality in the economy, lack of supporting 
infrastructure such as but not limited to fast and stable internet connection, mobile coverage, computers, 
electricity, and adequacy of education and skills insulates EMs from the influence of GenAI in their labor 
markets. Even within emerging markets, this effect can generate differences. Carbonero et al. (2021) compare 
the effects of AI on the labor markets of Vietnam and Lao PDR. Vietnam has a higher risk of job displacement 
from AI due to labor composition differences and past industrialization. In contrast, Lao PDR has a larger share 
of agricultural workers. Both countries have high potential for AI adoption and task reorganization within 
occupations, but many job activities remain unsuitable for AI, mitigating labor displacement. In a service-centric 
economy like India, Copestake et al. (2023) find that jobs that harness AI can offer a substantial wage 
premium. However, these only benefit a niche group of workers, particularly those with AI skills, and are 
concentrated only in specific industries, places, and corporations. Displacement is primarily present in older 
'incumbent' enterprises that do not adopt AI.

In the Philippines, Gaspar and Harris (2020) discovered that non-production workers have better job prospects 
due to their roles being less automatable and their higher skills. However, the authors noted that this may lead 
to increased trends of seasonal work, which may increase workers' exposure to economic shocks. In the short 
run, employment gains may not continue with advanced technologies such as AI, while its long-term effects 
remain uncertain. Additionally, the researchers indicated that AI adoption in the Philippines can create jobs, 
provided that proper training exists to offset its adverse effects. In fact, firms in the country that adopt 
automation are more likely to hire additional employees rather than lay them off.

The BPO industry, which predominantly focuses on routine-centric tasks and low-skilled roles such as 
answering phone calls and dealing with inquiries, may be adversely affected by AI. An (ILO, 2017) study noted 
that modern algorithms and programs have already undermined the availability of jobs in the sector, which 
often requires basic literacy and English language skills. It estimates that 89 percent of the BPO workforce is at 
high risk of automation as consumers and clients demand better services and explore cost-saving measures. 
Two main technologies have been mentioned that influenced the radical shift in the BPO industry: cloud 
technology and robotic process automation. The former uses a network of online servers to manage, store, and 
analyze data on cloud platforms, while the latter utilizes software with algorithms to execute highly structured 
and routine operations. In fact, a recent report by the ASEAN Macroeconomic Research Office (AMRO) 
mentioned that the large BPO industry in the economy can face a greater risk of worker displacement, primarily 
those engaged in routine work, as AI gradually reshapes ICT operations. AMRO stated that the country should 
upgrade its BPO services to more knowledge-based services (AMRO, 2024).

Conversely, reports by the World Bank (2024a, 2024b) reported the significant adoption of generative AI tools 
in the Philippines, driven by its young, tech-savvy population and digital infrastructure. The study also revealed 
that GenAI is primarily used for productivity-related tasks. This has contributed positively to the economy, 
especially in sectors that require high-skilled tasks. However, challenges such as digital infrastructure and skills 
development need to be addressed to fully harness AI's benefits. Broadly, there is a proactive stance in the 
country in integrating AI technologies.

INTERNATIONAL MONETARY FUND

12

---

<!-- PAGE 15 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

IV.  Data and Methodology

This section provides additional details on the exposure and complementarity metrics as well as the Philippine 
labor force survey data. Felten et al. (2021) introduce the AI Occupational Exposure (AIOE) measure to 
evaluate the overlap between AI capabilities and the required tasks for different occupations. To construct the 
AIOE, the authors first identify ten common AI applications4, such as reading comprehension, image 
recognition and speech recognition, sourced from the Electronic Frontier Foundation's AI Progress 
Measurement project. Then, the authors obtain occupational "abilities" using data from the Occupational 
Information Network (O*NET), a database sponsored by the U.S. Department of Labor containing lists of 
required tasks to perform each occupation together with tasks' relative importance. Lastly, the authors connect 
the occupational abilities to AI capabilities via relevance ratings obtained from a crowd-sourced dataset.5 The 
ability-level AI exposure scores are calculated by summing the relevance ratings of all AI applications for each 
ability within an occupation. These scores are then aggregated to the occupation level, weighted by the 
prevalence and importance of each ability within an occupation. This results in an occupation-level AIOE score 
for 774 different occupations. The score is standardized such that the median of the score is zero and the 
standard deviation is one. Figure 6 shows the distribution of AIOE scores across aggregated occupations.

Figure 6. Exposure and Complementarity Across Occupations

Pizzinelli et al. (2023) build on the AIOE by introducing a complementarity index to account for the extent to 
which AI complements or substitutes human labor. The complementarity index is high for occupations where AI 
is more likely to complement human abilities rather than substitute them. It is calculated by considering both the 
importance of AI applications and the context in which they are used, reflecting societal and technical 
constraints that may limit AI's substitutive potential in certain jobs.6 It therefore highlights occupations that, 
despite high AI exposure, may not experience significant displacement due to the complementary nature of AI

4 The ten applications are abstract strategy games, real-time video games, image recognition, visual question answering, image 
generation, reading comprehension, language modeling, translation, speech recognition, instrumental track recognition. 
5 The relevance ratings come from a dataset provided by Amazon which aggregates a large number of survey responses on the

relevance of certain AI applications for different tasks.

6 The six components of the score are communication, responsibility, physical conditions, criticality, routine, and skills. The O*NET 
database records a relevance score of these components for each occupation. The complementarity score is the weighted 
average of these sub-scores. See Pizzinelli et al (2023) for details.

INTERNATIONAL MONETARY FUND

13

---

<!-- PAGE 16 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

in those roles. For example, professionals and managers tend to have high exposure but also high 
complementarity scores, indicating that AI is more likely to augment rather than replace their work. On the other 
hand, clerical workers, who generally face higher substitution risks, show high exposure but lower 
complementarity scores, making them more vulnerable to AI-driven disruption. The two dimensions provide 
sufficient nuance to obtain a clearer understanding of the potential impacts of AI on the labor market by 
considering both exposure and the likelihood of AI acting as a complement. For the remainder of the paper, 
"high"/"low" exposure/complementarity for a given occupation mean that the occupation has an above median 
exposure/complementarity score.

We merge the exposure and complementarity scores with labor force survey microdata from the Philippine 
Statistics Authority, specifically the October 2022 vintage which contains 183,602 observations for 52 variables. 
Critically, the LFS microdata contain information on occupations at the 4-digit ISCO-08 level (there are 436 
occupations in total), allowing a very granular look at the distribution of occupations in the Philippines7.

Several important caveats apply to our analysis. The most important one is that the analysis in this paper is 
static. The data we use presents a snapshot of the current labor market in the Philippines and the scores 
linking jobs to AI is based on the current state of AI's capabilities which are rapidly evolving. Over the medium 
to long term, workers will retrain and adapt, and new jobs may emerge. This process is likely to vary across 
countries, sectors, firms, and even at the occupational level. Over time, resources will be reallocated across 
sectors which could in turn generate feedback effects which would not be captured in this analysis. The results 
in this paper are therefore likely to be more relevant for the short to medium term. Second, the AI exposure and 
complementarity scores are designed to capture the capabilities of generative AI. The results in this paper 
therefore do not speak to the impact of potential advances in automation or robotics which may materialize in 
the future as AI is deployed and will likely impact different occupations than those affected by generative AI.

Another important assumption underlying this work is that the tasks in each job and their relative importance do 
not vary across countries. The work by Felten et al. (2021) and Pizzinelli (2023) relies on the O*NET database 
which contains data on occupations in the U.S. The literature on studying the impact of AI on both developed 
and developing countries (see also Dalla Zuanna (2024), IMF (2025)) has so far operated under the premise 
that tasks performed within each occupation are similar around the world. However, recent studies, e.g. 
Caunedo et al. (2023), suggest that some occupations in developing countries tend to be more intensive in 
routine and therefore automatable tasks. In similar fashion, the societal context of each occupation and as a 
result the extent to which it is shielded from being replaced by AI could vary across countries. Taken together, 
this would potentially imply a higher exposure and/or lower complementarity for some occupations. The 
estimates presented in this paper can therefore be interpreted as being on the conservative side. Future work 
tweaking exposure and complementarity scores to the country level would be a helpful contribution to the 
literature, data permitting.

V.  Analysis and Labor Market Implications

Table 2 shows example occupations for the three exposure/complementarity categories along with their shares 
in the Philippine workforce. 36% of workers are highly exposed to artificial intelligence and over a third (39%) of

7 To translate the AIOE scores from the Standard Occupational Classification (SOC) system to the ISCO-08 classification, the SOC-

ISCO-08 crosswalk published by the US Bureau of Labor Statistics is used.

INTERNATIONAL MONETARY FUND

14

---

<!-- PAGE 17 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

those highly exposed have low complementarity. Comparing the results for the Philippines with peer countries 
in the region is possible with some caveats; the appendix contains the details.

Table 2. AI Exposure and Complementarity in the Philippines

Exposure  Complementarity  Example Occupation Titles

Share (PHL)

High

High

General and Operations Managers, First-Line Supervisors, Teachers and 
Teaching Assistants, Lawyers, Civil Engineers, Counselors

High

Low

Customer Service Representatives, Telemarketers, Accountants, Auditors, 
Secretaries, Administrative Clerks

Low

n/a

Farmworkers, Construction Laborers, Janitors, Maids and Cleaners, Waiters, 
Textile workers, Food Preparation Workers

22%

14%

64%

Figure 7 presents the distribution of exposure and complementarity across major occupational groups. It shows 
that occupations with low exposure are mostly agriculture workers, the trades, elementary occupations, and 
some services. Moving to highly exposed professions, Managers, Professionals, and some service workers are 
most likely to benefit from AI indicated by their high complementarity score. Those occupations most likely to 
be displaced by AI are clerical support workers, some professionals, and some service workers.

Figure 7. AI Exposure by Occupation

The microdata from the PSA also allows us to look at how exposure and complementarity correlate with other 
socio-economic and demographic variables. Figure 8 shows the gender, age, education, income, regional, and 
sectoral dimensions. We note a substantial difference along the gender dimension with female workers much 
more exposed to AI than male workers. This is due to more women being employed as clerical support, 
service, and sales workers whereas men have a higher share in trades, agriculture, machine operations, and

INTERNATIONAL MONETARY FUND

15

---

<!-- PAGE 18 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

elementary occupations which are less likely to be impacted by AI at this stage (see Figure 11 in the appendix). 
A similar argument applies to the education variable. College-educated workers are more often employed as 
managers, professionals, or technicians. Here, we also note that jobs with high complementarity potential tend 
to be held by college-educated workers. As the world of work changes, this means that they are more likely to 
have the requisite skills to harness the productivity benefits from AI. Along the age dimension, overall exposure 
does not vary much. However, Figure 8 shows that older workers tend to hold more complementary jobs as 
they are more represented in managerial roles. It will be critical for young workers to have the skills that allow 
them to employ AI to increase their productivity for the Philippines to capitalize on the impending demographic 
dividend8. There may also be age-based differentials in skill sets when it comes to the use of digital 
technologies which need to be accounted for (see policy section).

Figure 8. Exposure and Complementary by Gender, Age, Education, Wage, Location, and Sector

8 See selected issues paper on Potential Growth and Demographic Dividend of IMF Country Report No. 24/352

INTERNATIONAL MONETARY FUND

16

---

<!-- PAGE 19 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Sources: Philippine Statistics Authority; and IMF staff calculations.

The results in Figure 8 also show that AI could have profound implications for wage9 inequality. College-
educated workers in well-paid occupations which lend themselves to integration with AI could see their 
productivity, and thus likely also their wages, improve dramatically. At the same time, many college-educated 
workers are also in occupations which could be eliminated by AI, potentially shifting income dynamics in favor 
of blue-collar workers. It is in this respect that recent technological advances differ from those seen in the past 
which have typically replaced low-skilled and low-income laborers. It is worth noting, however, that there is 
considerable disagreement in the literature on the longer-term direction and magnitude of AI's impact on 
wages. Some (e.g. Korinek (2024)) argue that the advent of artificial general intelligence will eventually cause 
competitive market wages to plummet whereas others (e.g. Acemoglu (2018)) argue that higher productivity 
and the creation of new labor-intensive jobs are forces that could support the labor share of income over the 
long run. The purpose of this paper is not to take a stance on the debate but instead to flesh out the 
characteristics and distribution of potentially impacted workers in the Philippine labor force.

In terms of sectors of the economy, Figure 8 reveals that AI is a phenomenon which will mostly affect the 
services sector. This is of course not a particularly surprising result - however, it is important to note that there 
is high heterogeneity within the services sector (see Figure 12 in the appendix). The subsector with the highest 
proportion of occupations classified as high exposure/low complementarity is the BPO sector.10 73 percent of 
workers employed in this sector are "Contact Center Information Clerks”11 which score highly on AI exposure 
but low on complementarity. Meanwhile, the subsector with the highest proportion of occupations classified as 
high exposure/high complementarity is the education sector. 12 The bulk of occupations in this sector are

9 The labor force survey captures individual’s basic pay per day in their primary occupation. The cutoffs for the quintiles of this 
distribution are 300/400/500/700. In other words, 20 percent of workers earn less than 300 PHP/day, the next 20 percent earn 
between 300 and 400 PHP/day, and so on. 
10 ISIC Rev. 4 Code 82, “Office administrative, office support and other business support activities, including activities of call

centers”.

11 ISCO-08 code 4222 
12 ISIC Rev. 4 Code 85, “Education”

INTERNATIONAL MONETARY FUND

17

---

<!-- PAGE 20 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

"Secondary Education Teachers" and "Primary School Teachers”13 which score highly both on exposure and 
complementarity to AI. Overall, this illustrates the high heterogeneity even within the services sector.

When comparing exposure and complementarity across different types of employment (see Figure 13 in the 
appendix), government workers stand out as the most exposed, with a substantial portion of that rated as low 
complementarity. This is driven by the high number of general, accounting, and bookkeeping clerks working for 
the government. The high share of high complementarity jobs in this category is driven by teachers. While self-
employed workers exhibit an average proportion of low complementarity jobs, the impact of job displacement 
could be higher given potentially unstable work arrangements and limited social protection for this type of 
worker.

VI.  AI Preparedness

While the exposure and complementarity of occupations to AI may be one of the most important factors, there 
are several other aspects which will have a profound impact on the adoption of AI in the Philippines.

The AI preparedness index (AIPI) developed by Cazzaniga et al. (2024) is based on four key dimensions which 
are likely relevant for smooth AI adoption: digital infrastructure, human capital and policies, innovation and 
integration, and regulation and ethics. For each dimension, the authors collect a rich set of indicators compiled 
by different institutions, including, but not limited to, sustained human capital investment, inclusive STEM 
expertise, labor and capital mobility within and across countries, R&D ecosystem, and the adaptability of legal 
frameworks to digital business models. All indicators are normalized to a 0-1 scale and then averaged. The 
AIPI is the simple average of the four dimensions.

13 ISCO-08 codes 2330 and 2341

INTERNATIONAL MONETARY FUND

18

---

<!-- PAGE 21 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Figure 9. AI Preparedness Across Asia

Comparing the scores for the Philippines against other Asian economies shown in Figure 9, the Philippines 
emerges as broadly in line with the scores of its emerging market peers (red dashed boxes). Looking at the 
underlying components, the Philippines scores well on human capital (light blue bars) but less so on digital 
infrastructure (dark blue bars) when compared to both its ASEAN peers but also emerging markets more 
broadly. The quality and reach of digital infrastructure may have implications on how much (or how little) the 
country can benefit from AI, even in occupations with high exposure/high complementarity with AI.

Several caveats apply to the AIPI. First, the AIPI does not capture all dimensions that could affect the adoption 
of AI. For instance, the importance of the BPO sector in the Philippines is not considered. Second, there is high 
uncertainty about what the institutional requirements for an economy-wide integration of AI will ultimately be. As 
a result, the AIPI should be seen as an indicative exercise to highlight potential areas for improvement along 
the four dimensions. For the Philippines, the AIPI points to room for further enhancements along all dimensions 
and particularly in digital infrastructure. This would likely also help greatly with harnessing the opportunities 
presented by the Philippine's human capital considering the country's impending demographic dividend. 
Further work identifying specific preparedness gaps in the Philippines, going beyond the labor-market focused 
analysis in this paper, would be beneficial.

INTERNATIONAL MONETARY FUND

19

---

<!-- PAGE 22 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

VII. Regulatory Framework

Understanding the implications of AI and establishing a clear regulatory framework is vital to harness its full 
potential and economic benefits. Currently, there is no legislative framework to guide investments, foster 
research and development, and prepare the workforce for AI development and application in the Philippines.  
However, the country has recognized the need for such a framework and has taken initial steps towards this 
goal. In 2021, the Philippine government formulated the National AI Strategy Roadmap, which was 
subsequently updated in July 2024. The main goal of the National AI Strategy Roadmap 2.0 is to guide the 
government and the private sector in the use of AI and related technologies and how they can be utilized for 
national development.

The latest roadmap has the following main objectives: 1) Increased local industries' regional and global 
competitiveness; 2) Promote collaboration between the government, private sector, and the academia in 
research and development; 3) Identify key investment areas in research and development; 4) Prepare the 
workforce for future jobs; 5) Attract major industries to create jobs; 6) Ensure responsible rollout and 
governance of AI technologies.

Figure 10: National AI Strategy Pillars, Dimensions, Imperatives

Source: DTI, National AI Strategy Roadmap (2021)

Note: DTI is still finalizing the National AI Strategy Roadmap 2.0. Chart above was sourced from the 2021 AI Roadmap.

In addition to the National AI Strategy Roadmap, the government has passed Republic Act (RA) No. 11962, 
also known as the Trabaho Para sa Bayan Act. Recognizing the changing employment landscape due to 
emerging technologies, the law aims to establish a ten-year National Employment Master Plan (TPB) with four 
strategic priorities: stimulating national and local economic growth to address labor market challenges; 
improving the employability and competitiveness of Filipino workers by aligning education and training 
programs with industry requirements; reducing regulatory burdens on micro, small, and medium enterprises, 
including increasing access to capital, security, and protection; and encouraging upskilling and reskilling 
workers by leveraging opportunities provided by AI tools. It is anticipated that the TPB will generate three 
million jobs by 2028.

INTERNATIONAL MONETARY FUND

20

---

<!-- PAGE 23 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Furthermore, as part of the government’s overall strategy on AI, there are pending legislations in Congress 
which aims to promote the development, deployment, and regulation of AI14. These propose to establish 
various official bodies (Philippine Council of Artificial Intelligence, AI Development Authority, National Center for 
Artificial Intelligence Research), and regulatory frameworks for the use of AI in the workplace and ethical AI 
development. It is important to note that these AI specific legislations are still in their infancy, will evolve along 
the legislative process, and may be overlapping in scope.

References to AI can also be found in other, broader, government strategies. The Philippine Development 
Plan, which serves as the government’s overall guide in development planning, expresses the commitment of 
the government to adopting AI, including the following strategies: Anticipate skills needs in priority sectors 
(Chapter 4, Outcome 2),increase access of MSMEs to capital, digital technologies, and startups (Chapter 7, 
Outcome 2), support globally competitive industries and an agile workforce (Chapter 8, Outcome 4), enhance 
monitoring and understanding of emerging technologies, markets, and business models (Chapter 10, Cross-
Cutting Strategies), and promote RegTech development (Chapter 11, Cross-Cutting Strategies).

Identification of gaps in current policies and challenges in implementation.

History has shown that technological development is guided by the decisions made by regulators. The rapid 
advancement of AI has led to policy gaps and hurdles that limits its adoption, limiting the Philippines’ ability to 
fully harness the potential benefits of AI.

Gaps in Regulation and Governance: Understanding AI’s implications is crucial in managing risks and 
opportunities. The National AI Strategy Roadmap and its updated version are promising steps, but lack of 
legislation limits its effectiveness. A forthcoming harmonized legislation from the proposed bills will manage AI 
risks like algorithmic transparency, cybersecurity, privacy, errors, biases, and labor protection.15 Regulation will 
also promote best practices and cooperation between the government and private sector. However, with the 
rapid advancement of AI, regulations surrounding the country’s data privacy and intellectual property laws must 
evolve to keep pace.  For example, the United Kingdom and European Union have guidelines for ethical AI 
use, and the UN adopted a resolution for safe AI in March 2024.16

Gaps in Physical and Digital Infrastructure: AI requires robust physical and digital infrastructure. For 
instance, an AI chatbot handling 195 million queries needs data centers consuming power equivalent to 23,000 
U.S. households. It is forecasted that data centers’ electricity consumption is expected to increase, straining 
electricity grids for countries like the US and Ireland. Similarly, expanding the adoption of AI in the Philippines 
will have important implications for power demand and infrastructure needs17, which come on top of the 
existing gaps in access to and quality of power supply—about two million households still lack electricity, and 
power interruptions remain common (PIDS, 2023). A fast and reliable internet connection is also crucial for AI, 
yet the Philippines has slow speeds and high costs. In the 2023 Worldwide Broadband Speed League, the 
Philippines ranked 86th out of 220 countries with an average download speed of 43.36mbps, lower than the

14 As of January 2025, these include house bills 7396, 9448, 7913, 7983 
15  https://lti.institute/2022/09/how-regulation-can-catch-up-with-ai/ 
16 https://news.un.org/en/story/2024/03/1147831 
17 https://www.bworldonline.com/economy/2024/02/25/577716/energy-dept-seeking-to-gauge-major-data-centers-re-

needs/#:~:text=The%20Philippines%20is%20positioning%20itself,approximately%20300%20MW%20by%202025.

INTERNATIONAL MONETARY FUND

21

---

<!-- PAGE 24 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Asian average of 45.72mbps.18 Meanwhile, the World Data Lab estimates that nearly 19 million Filipinos or 
16.6 percent of the population cannot afford a minimum package of internet.19 The quality and reach of digital 
infrastructure will matter not just on the household side, but also on the firm side, particularly for MSMEs, which 
may face challenges in terms of capacity, cost, access.

Upskilling and Reskilling: The Future of Jobs report states that 23 percent of the workforce will change within 
five years, with 60 percent needing training by 2027 which are centered on creative and analytical thinking, AI, 
and big data (WEF, 2023)20. Despite high internet penetration, 90 percent of Filipinos lack basic ICT skills. The 
Philippines also lags in international education assessments in mathematics, reading, science, and creative 
thinking. Workers also lack soft skills like adaptability, problem-solving, and collaboration (PIDS, 2023). Despite 
the high demand for trainings, obstacles to skills enhancement include inadequate internet access, lack of time, 
high training costs, and limited opportunities (Economist, 2023). 21 However, the government has multiple 
training initiatives that are underway, that are backed by the industry to boost reskilling. In addition, the 
government is also updating the education curriculum and reskilling educators to meet to industry needs.22 
IBPAP noted that the Philippine tech industry is expected to generate 1.1 million new jobs by 2028, 
necessitating a steady supply of skilled workers.

Use Cases and the Cost of Adoption: The Philippine AI Roadmap has noted that one of the gaps in adopting 
AI is that some companies in the Philippines do not yet fully comprehend its capabilities and limitations to utilize 
and enhance their productivity and efficiency. Moreover, hesitancy remains in adopting AI and emerging 
technologies due to high costs and lack of clear and tangible returns. Firms in the country noted that key 
roadblocks in modernizing their technology is the high fixed capital costs followed by high licensing costs 
associated with technology adoption (ILO, 2017). In addition, a survey made by Cisco, noted that firms in the 
Philippines have expressed that only 17 percent are ready to deploy and use AI in their business processes, 44 
percent are said to be moderately ready, 35 percent indicated they have minimal readiness while 4 percent 
answered they are not prepared to use AI. The clear understanding of AI may also entice the private and public 
sector to support research and development. Currently, the Philippines is spending less than 0.2 percent of 
GDP, equivalent to US$0.8bn, lower than the global benchmark of 1 percent of GDP or US$3.75bn. This 
places the Philippines second last compared to other Southeast Asian countries (DTI, 2021).

VIII. Policies to Foster AI Adoption and Harness
its Benefits

The analysis in this paper shows that a substantial proportion of the Philippine labor force will be impacted by 
AI. 14 percent of jobs are classified to be at risk of displacement by AI and another 22 percent are likely to see 
the nature of their work change significantly as AI is rolled out. The BPO sector is the most exposed sector of 
the economy and therefore deserves particular attention. While BPO sector employees only make up about 3 
percent of the total workforce, the size of its revenues (7.4 percent of GDP, similar in magnitude to all

18 https://www.pids.gov.ph/details/news/in-the-news/think-tank-says-ph-connectivity-still-lags-behind-in-

asia#:~:text=Despite%20this%20improvement%2C%20however%2C%20the,Asian%20average%20of%2045.72%20Mbps.

19 https://www.bworldonline.com/infographics/2022/04/18/442463/philippines-most-internet-poor-in-southeast-asia/ 
20 https://www.weforum.org/publications/the-future-of-jobs-report-2023/digest/ 
21 https://impact.economist.com/perspectives/talent-education/bridging-skills-gap-fuelling-careers-and-economy-philippines#_ftn21 
22 https://www.philstar.com/headlines/2024/06/26/2365677/ai-education-pressing-issues-employers-ecop

INTERNATIONAL MONETARY FUND

22

---

<!-- PAGE 25 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

remittances) generates large potential spillovers from changes in the BPO sector to other parts of the economy. 
This section lays out several key areas that policymakers can focus on to harness the opportunities and 
mitigate the risks presented by the rollout of AI.

The first key area for policymakers is investment in digital infrastructure. The quality and reach of the digital 
infrastructure in the Philippines are uneven, with significant disparities between urban and rural areas. 
Improving internet connectivity, expanding electricity grids, and ensuring reliable access to power will be 
critical. The government should also support the development of a robust digital economy and entrepreneurial 
ecosystem, which can foster innovation and create an environment conducive to AI deployment. Providing 
fiscal incentives for private sector investment in AI, such as research and development grants, can stimulate 
technological advancements and facilitate the integration of AI across various sectors.

Second, enhancing human capital through education and training programs is essential. The Philippines has a 
relatively young and dynamic workforce with English language skills, but there are gaps in digital literacy and 
advanced technical skills23. The education system needs to be updated to include AI and related subjects, and 
there should be a focus on upskilling the current workforce. Studies have shown that introducing basic 
concepts in early education can build foundational understanding and critical thinking in young students24. On 
the tertiary level, studies argue that AI education should focus on specialized knowledge and applications 
which can prepare students for advance roles in their chosen fields. Meanwhile, technical vocation and training 
(TVET) play a crucial role in AI adoption by developing sector-specific skills, adapting curricula to meet industry 
needs, and providing lifelong learning opportunities to ensure continued employability and inclusivity to a 
broader segment of society. Beyond formal education, policymakers will need to promote lifelong learning and 
upskilling initiatives to prepare the workforce for AI-related changes. This includes offering specialized training 
programs to help workers adapt to new technologies. Additionally, fostering collaboration between academia, 
industry, and government can help bridge the skills gap, ensure that training programs are up-to-date vis-à-vis 
the latest developments in this fast-changing field, and equip the workforce with the necessary skills to thrive in 
an AI-driven economy.

Third, strengthening social protection systems to support workers during transitions, such as unemployment 
insurance, will also be crucial in mitigating the potential negative impacts of AI on the labor market. The 
Philippine Social Security System already explicitly allows claiming unemployment benefits in the case of 
redundancy due to the “installation of labor-saving devices”25. Against this backdrop, instituting reskilling and 
upskilling programs could help workers transition to different jobs without having to rely on unemployment 
insurance. This needs to be combined with developing strategies for businesses to responsibly integrate AI 
while supporting and training workers. The potentially increased use of unemployment insurance and the cost 
of reskilling programs may also involve fiscal cost which would need to be budgeted for. Over the medium term, 
the taxation of capital income may need to be recalibrated if the income share of labor does indeed decline due 
to the adoption of AI (see Cazzaniga et al. (2024)) for a more in-depth discussion.

Overall, a comprehensive strategy that includes infrastructure development, human capital enhancement, and 
supportive fiscal policies will be essential for the Philippines to fully capitalize on the opportunities presented by 
AI. This paper has fleshed out the geography of the labor market which will help policymakers tailor and target

23 Chapter 5 of OECD (2023) discusses skill needs in the age of AI in detail. 
24 See Yim and Su (2024) 
25 Source: https://www.sss.gov.ph/unemployment-benefit/

INTERNATIONAL MONETARY FUND

23

---

<!-- PAGE 26 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

their measures to those parts of the economy that benefit from them most. This approach will help the country 
navigate the challenges of AI integration and position itself as a competitive player in the global digital 
economy. The Philippines is not the only country facing the enormous challenge of effectively making use of AI. 
International partnerships, peer learning, and support from organizations like the IMF will help along the way.

INTERNATIONAL MONETARY FUND

24

---

<!-- PAGE 27 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

References

Acemoglu, D. and Restrepo, P., 2020. Robots and jobs: Evidence from US labor markets. Journal of political

economy, 128(6), pp.2188-2244.

Acemoglu, D., 2024. The Simple Macroeconomics of AI (No. w32487). National Bureau of Economic Research.

Asian Development Bank Institute. (2020). ADBI Working Paper 1081. Retrieved from

https://www.adb.org/sites/default/files/publication/566281/adbi-wp1081.pdf

ASEAN+3 Macroeconomic Research Office. (2024). AREO 2024 Special Feature. Retrieved from https://amro-

asia.org/wp-content/uploads/2024/04/AREO-2024-C2-Special-Feature.pdf

Berg, A., Papageorgiou, C. and Vaziri, M. (2023). Technology’s Bifurcated Bite. Finance & Development

Magazine, IMF. Retrieved from: https://www.imf.org/en/Publications/fandd/issues/2023/12/Technology-
bifurcated-bite-Berg-Papageorgiou-Vaziri

Bernardo, A. B. I., Albert, J. R. G., Vizmanos, J. F. V., & Muñoz, M. S. (2023). Toward measuring soft skills for

youth development: A scoping study. Discussion Papers (No. 2023-28). Philippine Institute for 
Development Studies. https://doi.org/10.62986/dp2023.28

Brynjolfsson, E., Li, D. and Raymond, L.R., 2023. Generative AI at work (No. w31161). National Bureau of

Economic Research.

Carbonero, F., Davies, J., Ernst, E., Fossen, F.M., Samaan, D. and Sorgner, A., 2023. The impact of artificial 
intelligence on labor markets in developing countries: a new method with an illustration for Lao PDR and 
urban Viet Nam. Journal of Evolutionary Economics, 33(3), pp.707-736.

Caunedo, J., Keller, E. and Shin, Y., 2023. Technology and the task content of jobs across the development

spectrum. The World Bank Economic Review, 37(3), pp.479-493.

Cazzaniga, M., Jaumotte, M.F., Li, L., Melina, M.G., Panton, A.J., Pizzinelli, C., Rockall, E.J. and Tavares, 
M.M.M., 2024. Gen-ai: Artificial intelligence and the future of work. International Monetary Fund.

Copestake, A., Marczinek, M., Pople, A., & Stapleton, K. (2023, March). AI and services-led growth: Evidence

from Indian job adverts. [Working Paper]. Centre for Economic Policy Research (CEPR). Retrieved from 
https://steg.cepr.org/sites/default/files/2023-
03/WP060%20CopestakeMarczinekPopleStapleton%20AIAndServicesLedGrowth_0.pdf

Centre for Economic Policy Research. (2023). Fear of Technology-Driven Unemployment and Its Empirical 
Base. Retrieved from https://cepr.org/voxeu/columns/fear-technology-driven-unemployment-and-its-
empirical-base

Cornell University. (2023). Artificial Intelligence and Its Short-Term Effects on Employment. Retrieved from

https://arxiv.org/pdf/2303.10130

Dalla Zuanna, A., Dottori, D., Gentili, E. and Lattanzio, S., 2024. An assessment of occupational exposure to

artificial intelligence in Italy (No. 878). Bank of Italy, Questioni di Economia e Finanza (Occasional Papers).

Das, M. and Hilgenstock, B., 2022. The exposure to routinization: Labor market implications for developed and

developing economies. Structural change and economic dynamics, 60, pp.99-113.

Department of Trade and Industry Philippines. (2021). National AI Strategy Roadmap.

INTERNATIONAL MONETARY FUND

25

---

<!-- PAGE 28 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Economist Impact. (2023). Bridging Skills Gap: Fuelling Careers and Economy in the Philippines. Retrieved

from https://impact.economist.com/perspectives/talent-education/bridging-skills-gap-fuelling-careers-and-
economy-philippines#_ftn21

Eloundou, T., Manning, S., Mishkin, P. and Rock, D., 2023. Gpts are gpts: An early look at the labor market

impact potential of large language models. arXiv preprint arXiv:2303.10130.

Emerald Insight. (2023). Economics of ChatGPT: A Labor Market View on the Occupational Impact of Artificial

Intelligence. Retrieved from https://www.emerald.com/insight/content/doi/10.1108/JEBDE-10-2023-
0021/full/pdf?title=economics-of-chatgpt-a-labor-market-view-on-the-occupational-impact-of-artificial-
intelligence

Ewrin, R. (2017). History of artificial intelligence. In Artificial intelligence: The quest for the ultimate thinking

machine (pp. 45-54). Arcturus Publishing Ltd.

Felten, E., Raj, M. and Seamans, R., 2021. Occupational, industry, and geographic exposure to artificial

intelligence: A novel dataset and its potential uses. Strategic Management Journal, 42(12), pp.2195-2217.

Frank, M.R., Autor, D., Bessen, J.E., Brynjolfsson, E., Cebrian, M., Deming, D.J., Feldman, M., Groh, M., Lobo,

J., Moro, E. and Wang, D., 2019. Toward understanding the impact of artificial intelligence on labor. 
Proceedings of the National Academy of Sciences, 116(14), pp.6531-6539.

Gaspar, R. and Harris, N., 2020. The fate of job creation in the Philippines amid the automation revolution: A

firm-level analysis (No. 1081). ADBI Working Paper Series.

Gmyrek, P., J. Berg, and D. Bescond. 2023. Generative AI and Jobs: A Global Analysis of Potential Effects on 
Job Quantity and Quality. ILO Working Paper 96. International Labour Organization, Geneva, Switzerland.

Hebrew University of Jerusalem. (2023). Automation and Employment. Retrieved from

https://en.economics.huji.ac.il/sites/default/files/economics-en/files/automation_4.pdf

Hui, X., Reshef, O. and Zhou, L., 2023. The short-term effects of generative artificial intelligence on

employment: Evidence from an online labor market. Available at SSRN 4527336.

Institute of Labor Economics. (2023). IZA Discussion Paper 14944. Retrieved from

https://docs.iza.org/dp14944.pdf

International Labour Organization. (2017). ILO Report. Retrieved from

https://www.ilo.org/media/421871/download

International Monetary Fund. (2018). IMF Working Paper 135. Retrieved from

https://www.elibrary.imf.org/view/journals/001/2018/135/article-A001-en.xml

International Monetary Fund. (2025). Transforming the Future: The impact of artificial intelligence in Korea.

Selected Issues Papers.

Korinek, A. and Juelfs, M., 2022. Preparing for the (non-existent?) future of work (No. w30172). National

Bureau of Economic Research.

Liu, Y., & Wang, H. (2024). Who on earth is using generative AI? Policy Research Working Paper No. 10870.

Washington, DC: World Bank. Retrieved from: 
https://openknowledge.worldbank.org/entities/publication/5a876bd0-f85a-479b-ae32-cf0b7f33792f

MIT Initiative on the Digital Economy. (2016). AER Article. Retrieved from 
https://ide.mit.edu/sites/default/files/publications/aer.20160696.pdf

INTERNATIONAL MONETARY FUND

26

---

<!-- PAGE 29 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

National Bureau of Economic Research. (2023). NBER Working Paper 30074. Retrieved from

https://www.nber.org/system/files/working_papers/w30074/w30074.pdf

National Center for Biotechnology Information. (2019). PNAS Article. Retrieved from 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6452673/pdf/pnas.201900949.pdf

Ng, M., Khoo, M., Haridas, G., & Toh, J. T. (2023, May). Generative AI in the Philippines: Challenges and

Opportunities. Access Partnership. Retrieved from   https://accesspartnership.com/wp-
content/uploads/2023/05/Micr_GenAI_-Philippines_FINAL_230529.pdf

Organisation for Economic Co-operation and Development (OECD). 2023. “OECD Employment Outlook 2023:

Artificial Intelligence and the Labour Market.” Paris, France.

Philippine Institute for Development Studies. (2023). Electricity Supply Interruptions in the Philippines:

Characteristics, Trends, Causes. Retrieved from https://www.pids.gov.ph/publication/discussion-
papers/electricity-supply-interruptions-in-the-philippines-characteristics-trends-causes

Philippine Journal of Labor and Industrial Relations, Volume 33. (2015). Retrieved from

https://journals.upd.edu.ph/index.php/pjlir/article/view/7256/6319

Pizzinelli, C., Panton, A.J., Tavares, M.M.M., Cazzaniga, M. and Li, L., 2023. Labor market exposure to AI:

Cross-country differences and distributional implications. International Monetary Fund.

Standard Chartered – ChatGPT Impact on Labor Markets. (2023). Retrieved from

https://research.sc.com/research/api/application/protected/rp/api/data/render/241545

The Philippine IT-BPM Industry Roadmap 2028. (2022). Retrieved from https://www.ibpap.org/knowledge-hub

Webb, M. 2020. “The Impact of Artificial Intelligence on the Labor Market.” Stanford University Working Paper,

Stanford, CA.

World Bank. 2024a. “Who on Earth Is Using Generative AI?” World Bank Publication. Retrieved from

https://openknowledge.worldbank.org/entities/publication/5a876bd0-f85a-479b-ae32-cf0b7f33792f

World Bank. 2024b. World Bank East Asia and the Pacific Economic Update, October 2024: Jobs and

Technology. Washington, DC: World Bank

World Economic Forum. (2023). The Future of Jobs Report 2023. Retrieved from

https://www.weforum.org/publications/the-future-of-jobs-report-2023/digest/

Yim, I.H.Y., Su, J. Artificial intelligence (AI) learning tools in K-12 education: A scoping review. J. Comput. 
Educ. (2024).

INTERNATIONAL MONETARY FUND

27

---

<!-- PAGE 30 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Appendix

Figure 11. AI Exposure by Occupation, Gender, and Education

INTERNATIONAL MONETARY FUND

28

---

<!-- PAGE 31 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Figure 12. Exposure and Complementary by Activity within Services

INTERNATIONAL MONETARY FUND

29

---

<!-- PAGE 32 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Figure 13. Exposure and Complementary by Type of Worker

Cross-country comparison

Comparing the results for the Philippines with peer countries in the region is possible though a few caveats 
apply. To compute exposure and complementarity shares for other Asian economies, we use data on 
employment by occupation from the International Labor Organization (ILO)26. This dataset contains aggregated 
data submitted by country authorities. Occupations are captured at the 2-digit level (43 different occupations) 
and therefore less granular and less accurate than the data for Philippines used in this paper which captured 
occupations at the 4-digit level (436 different occupations). Table 2 shows that the Philippine labor force 
exhibits a total exposure that is higher than other Asian EMDEs but not as high as Asia’s advanced economies.

Comparing the shares computed using ILO vs PSA data for the Philippines in table 2 shows that having access 
to granular data matters mostly for the complementarity angle. In other words, the additional granularity helps 
in breaking down the ISCO-08 major groups which are highly heterogeneous in terms of AI exposure such as 
services and sales workers (Figures 7, 12). As a result, results for the Philippines and its peers in the region 
along this dimension are difficult to compare.

26 The reader may also refer to box I in the chapter 2 of the Fall 2024 IMF Regional Economic Outlook for Asia and the Pacific.

INTERNATIONAL MONETARY FUND

30

---

<!-- PAGE 33 -->

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and 
Complementarity

Table 2. AI Exposure and Complementarity in Philippines and Asia

Exposure  Complementarity

Example Occupation Titles

Share 
(PHL)

Share (other 
Asian EMDEs)

Share 
(Asian AEs)

High

High

General and Operations Managers, First-Line 
Supervisors, Teachers and Teaching 
Assistants, Lawyers, Civil Engineers, 
Counselors

ILO: 10% 
PSA: 22%

9%

24%

High

Low

Low

n/a

Customer Service Representatives, 
Telemarketers, Accountants, Auditors, 
Secretaries, Administrative Clerks

Farmworkers, Construction Laborers, 
Janitors, Maids and Cleaners, Waiters, 
Textile workers, Food Preparation Workers

ILO: 27% 
PSA: 14%

ILO: 63% 
PSA: 64%

18%

26%

73%

50%

Sample includes AE = AUS, SGP, JPN; EMDE = BGD, BRN, BTN, IDN, IND, KHM, KIR, LAO, LKA, MDV, MNG, PHL, PNG, THA, 
TLS, TUV, VNM, WSM.

INTERNATIONAL MONETARY FUND

31

---

<!-- PAGE 34 -->

The Impact of Artificial Intelligence on the Labor Market in the Philippines

Working Paper No. WP/2025/043

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Artificial Intelligence and
the Philippine Labor
Market: Mapping
Occupational Exposure
and Complementarity

Micholo Cucio and Tristan Hennig

WP/25/43

IMF Working Papers describe research in
progress by the author(s) and are published to
elicit comments and to encourage debate.
The views expressed in IMF Working Papers are
those of the author(s) and do not necessarily
represent the views of the IMF, its Executive Board,
or IMF management.

2025
FEB

© 2025 International Monetary Fund

WP/25/43

IMF Working Paper
APD

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity
Prepared by Micholo Cucio and Tristan Hennig*

Authorized for distribution by Maria Gonzalez
February 2025

IMF Working Papers describe research in progress by the author(s) and are published to elicit
comments and to encourage debate. The views expressed in IMF Working Papers are those of the
author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper combines labor force survey microdata with measures of occupational AI exposure
and complementarity to examine the potential impact of recent advancements in AI on the Philippine labor
market. We find that around one third of workers are highly exposed to AI with around sixty percent of those
also rated highly complementary, indicating potential productivity gains. College-educated, young, urban,
female, and well-paid workers in the services sector are most exposed. Business process outsourcing (BPO) is
identified as the sector with the highest proportion of jobs at risk of displacement. Addressing regulatory gaps,
infrastructure needs, and workforce reskilling is crucial to maximize benefits and mitigate negative impacts.

RECOMMENDED CITATION: M. Cucio and T. Hennig “Artificial Intelligence and the Philippine Labor Market:
Mapping Occupational Exposure and Complementarity” IMF Working Paper No. 25/43, February 2025

JEL Classification Numbers:

J21, J23, J24, J31, M54, O15, O53

Keywords:

Artificial Intelligence (AI), Labor Market, Philippines, Business
Process Outsourcing (BPO), AI Exposure and Complementarity

Author’s E-Mail Address:

CucioMI@bsp.gov.ph and Thennig2@imf.org

* This paper has benefitted tremendously from comments by Elif Arbatli Saxegaard, Elmer Li, Maria Cynthia Sison, the Bangko
Sentral ng Pilipinas (BSP), the Philippine National Economic and Development Authority, as well as seminar audiences at the BSP
and IMF. We would also like to thank the Philippine Statistics Authority for providing the Labor Force Survey microdata, the IMF
Resident Representative Office in Manila under the helm of Ragnar Gudmundsson for facilitating the data transmittal and the
conversation with the authorities, and Carlo Pizzinelli for providing the AI complementarity scores.

WORKING PAPERS

Artificial Intelligence and the
Philippine Labor Market: Mapping
Occupational Exposure and
Complementarity

Prepared by Micholo Cucio and Tristan Hennig1

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Contents

Executive Summary ............................................................................................................................................ 3

I. Introduction ...................................................................................................................................................... 4

II. Context ............................................................................................................................................................. 7

A. The Philippine Labor Market ..................................................................................................................... 7

B. The BPO Industry ...................................................................................................................................... 8

III. Existing Literature ...................................................................................................................................... 11

IV. Data and Methodology ............................................................................................................................... 13

V. Analysis and Labor Market Implications .................................................................................................. 14

VI. AI Preparedness ......................................................................................................................................... 18

VII. Regulatory Framework ............................................................................................................................. 20

VIII. Policies to Foster AI Adoption and Harness its Benefits ..................................................................... 22

References ......................................................................................................................................................... 25

Appendix  ........................................................................................................................................................... 28

BOXES

1. The History of Artificial Intelligence ......................................................................................................... 6
2. Types of BPO Services ........................................................................................................................... 9

FIGURES

1. The Philippine Labor Force: Key Summary Statistics ............................................................................. 7
2. Unemployment and Labor Force Participation ........................................................................................ 8
3. Evolution of Pay in Real Terms ............................................................................................................... 8
4. BPO Export Revenues .......................................................................................................................... 10
5. BPO Employment .................................................................................................................................. 10
6. Exposure and Complementarity Across Occupations ........................................................................... 13
7. AI Exposure by Occupation ................................................................................................................... 28
8. Exposure and Complementary by Gender, Age, Education, Wage, Location, and Sector ................... 28
9. AI Preparedness Across Asia ................................................................................................................ 19
10. National AI Strategy Pillars, Dimensions, Imperatives .......................................................................... 20
11. AI Exposure by Occupation, Gender, and Education ............................................................................ 28
12. Exposure and Complementary by Activity within Services .................................................................... 28
13. Exposure and Complementarity by Class of Worker ............................................................................. 28

TABLES
International Market Share of the Philippines’ BPO Industry ................................................................. 10
1.
2. AI Exposure and Complementarity in the Philippines ............................................................................ 14
3. AI Exposure and Complementarity in the Philippines and Asia ............................................................. 30

INTERNATIONAL MONETARY FUND

2

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Executive Summary

This paper examines the potential impact of recent advancements in artificial intelligence (AI) on the labor
market in the Philippines. The Philippines faces unique challenges and opportunities due to its large BPO
sector—a significant contributor to the national economy. We build on the occupational classification framework
proposed by the Cazzaniga et al. (2024), which is in turn based on the work of Felten et al. (2021) and
Pizzinelli et al. (2023). Felten et al. develop an AI exposure index capturing the overlap between AI capabilities
and occupational tasks, while Pizzinelli et al. introduce an AI complementarity score assessing how AI might
enhance or replace human roles, considering required skill levels and societal context. By combining these
measures, occupations are categorized into high exposure/high complementarity, high exposure/low
complementarity, and low exposure groups. The primary innovation of this paper is linking these classifications
to the specific circumstances of the Philippines by merging the AI exposure and complementarity scores with
microdata from the Philippine Statistics Authority's October 2022 Labor Force Survey, comprising over 180,000
observations, 80,000 of which are tagged as “employed”. This approach provides a granular analysis of
occupations potentially affected by AI and correlates AI exposure with demographic indicators.

We find that around one third of occupations in the Philippines are highly exposed to AI, meaning that many of
the tasks could be performed by AI technologies. 61% of these highly exposed jobs are also rated as highly
complementary, suggesting that AI is likely to augment rather than replace these roles, potentially increasing
productivity. The remainder (14% of the total workforce) hold jobs with low complementarity, making them
susceptible to displacement by AI. College-educated, young, urban, female, and well-paid workers in the
service sector are most exposed to AI. These groups however also tend to occupy roles with high
complementarity, indicating they may be better positioned to leverage AI advancements as the nature of work
evolves. While BPO workers are classified as highly exposed with low complementarity, they represent only
about 3% of the total workforce. Nonetheless, the BPO sector's significant contribution to the economy—
accounting for 7.4% of GDP in 2023, similar in magnitude to remittances—means that changes within this
industry are macro-critical and may have spillover effects on the broader economy.

The Philippine government has recognized the transformative potential of AI and is actively working to harness
its benefits for national development, despite the absence of a comprehensive legal framework. The National
AI Strategy Roadmap, first introduced in 2021 and updated in 2024, outlines a strategic vision for integrating AI
across various sectors to boost competitiveness, foster research and development collaboration, and prepare
the workforce for future jobs while ensuring responsible AI governance. Complementing this initiative, the
Trabaho Para sa Bayan Act aims to align education with industry needs and generate job opportunities amid
technological change. Additionally, several bills are under consideration to establish regulatory and
developmental bodies for AI, reflecting a proactive stance toward AI development and regulation.

Despite these efforts, challenges persist, including regulatory gaps, inadequate infrastructure, workforce
reskilling needs, and limited AI adoption due to cost concerns. Addressing these issues is crucial for the
Philippines to fully leverage AI's economic and societal benefits. The analysis in this paper can inform
strategies to mitigate negative consequences, such as job displacement, and maximize positive outcomes,
such as increased productivity and the creation of new job categories. Investments in education and training
programs focused on AI and digital skills are essential to prepare the workforce for the future. Furthermore,
developing a regulatory framework that ensures the ethical use of AI and addresses issues related to labor
market transitions is imperative, drawing on lessons from global best practices.

INTERNATIONAL MONETARY FUND

3

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

I. Introduction

Recent advances in the development and public availability of artificial intelligence (AI) are likely to significantly
transform economies across the globe. One of the most notable advancements is the development of
generative AI models, such as OpenAI's GPT-4 and Google's Gemini. These models have revolutionized
natural language processing, enabling machines to understand and generate human-like text with
unprecedented accuracy. Their output has wide-ranging applications, including in content creation, coding, and
problem-solving, which could allow businesses to automate tasks, enhance customer service, and optimize
decision-making processes. As a result, industries ranging from healthcare to finance are beginning to integrate
AI-driven tools into their operations, promising efficiency gains and innovation opportunities. Recent advances
build on a long history of research and development which is outlined in greater detail in box 1.

This paper studies the potential impact of these rapid technological advancements on the labor market in the
Philippines. As AI systems become more capable and readily available, they are likely to replace or significantly
alter many job roles, particularly those involving routine and repetitive tasks. The Philippines, with its large
business process outsourcing (BPO) sector, faces unique challenges and opportunities. The BPO industry, a
significant contributor to the country's economy, might experience shifts as AI-driven chatbots and virtual
assistants handle more customer service tasks. However, AI could also create new opportunities, fostering
growth in tech-driven industries and necessitating a workforce with advanced digital skills.

We follow the occupational classification proposed by Cazzaniga et al. (2024) which is in turn based on work by
Felten et al. (2021) and Pizzinelli et al (2023). This strand of the literature considers occupations to be a list of
tasks. Felten et al. (2021) develop an AI “exposure” index that captures the overlap between the capabilities of
recent gen-AI tools and the tasks required for each occupation. Pizzinelli et al. (2023) develop an AI
complementarity score which considers the required skill level for each occupation as well as its societal
context to evaluate how shielded each job is from AI-driven replacement. Combining these two measures, each
occupation can therefore be categorized as either “high exposure/high complementarity”; “high exposure/low
complementarity”; and “low exposure” where the median exposure or complementarity score respectively
serves as the cutoff value between the high and low categories.

The main innovation of this paper is to connect the findings from the academic literature on occupational AI
exposure and complementarity to the specific circumstances of the Philippines. We merge the above-
mentioned classification of occupations with labor force survey microdata provided by the Philippine Statistics
Authority (PSA). We use the October 2022 vintage of the Philippine labor force survey which contains 183,602
observations of 52 variables. By using microdata rather than aggregated data from the International Labor
Organization (ILO), we obtain a more granular picture of the distribution of occupations potentially affected by
AI and are also able to correlate AI exposure with other demographic indicators.

We find that around one third of occupations in the Philippines are highly exposed to artificial intelligence. This
means that their jobs entail tasks which can now be performed by AI. 61% of those highly exposed jobs are
however also rated as highly complementary, meaning that artificial intelligence is likely to support rather than
replace the worker, potentially increasing their productivity. The remaining low complementarity jobs, which
represent 14% of the total workforce, are at risk of being replaced by AI.

Looking at other socioeconomic indicators recorded in the labor force survey, we find that college educated,
young, urban, female, and well-paid workers in the service sector are most exposed. However, these

INTERNATIONAL MONETARY FUND

4

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

characteristics also correlate with complementarity, suggesting that these workers may also be better placed to
take advantage of AI as the nature of work evolves.

While BPO workers are classified as highly exposed with low complementarity in our analysis, BPO sector
employees only make up about 3 percent of the total workforce. They therefore have less influence on the
aggregate numbers than one might have otherwise expected. Having said that, the nature of work in the BPO
sector will undoubtedly undergo substantial shifts in the wake of AI adoption and there may be spillovers to
other parts of the economy which would not be captured by the analysis in this paper. Given the size of BPO
sector revenues (7.4 percent of GDP in 2023, and similar in magnitude to remittances), changes in the BPO
sector will therefore still be macro critical.

The Philippine government has recognized the transformative potential of AI and is actively working to harness
its benefits for national development, although there is no comprehensive legal framework for the time being.
The National AI Strategy Roadmap, first introduced in 2021 and updated in 2024, outlines a strategic vision for
integrating AI across various sectors to boost competitiveness, foster R&D collaboration, and prepare the
workforce for future jobs while ensuring responsible AI governance. Complementing this initiative, the Trabaho
Para sa Bayan Act (Republic Act No. 11962) aims to align education with industry needs and generate
employment opportunities in the face of technological change. Concurrently, several bills are under
consideration to establish regulatory and developmental bodies for AI, reflecting a proactive stance towards AI
development and regulation. However, challenges persist, including regulatory gaps, inadequate infrastructure,
workforce reskilling needs, and limited AI adoption due to cost concerns.

Addressing these issues will be crucial for the Philippines to fully leverage AI's economic and societal benefits.
The analysis in this paper can help inform strategies to mitigate negative consequences, such as job
displacement, and maximize positive outcomes, such as increased productivity and the creation of new job
categories. Investments in education and training programs focused on AI and digital skills will be essential to
prepare the workforce for the future. Furthermore, regulatory frameworks need to be developed to ensure the
ethical use of AI and to address issues related to labor market transitions. These should draw on lessons from
global best practices in regulating and ensuring ethical AI use. By proactively studying AI's impact, the
Philippines can better navigate the technological transformation and ensure inclusive economic growth.

INTERNATIONAL MONETARY FUND

5

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Box 1. The History of Artificial Intelligence

The origins of Artificial Intelligence (AI) can be traced back to 1943 when Warren McCullock and Walter Pittz
published their work in the Bulletin of Mathematical Biophysics. They introduced the concept of networks
composed of artificial neurons and how these networks could perform basic logical problems. Their work
established the foundation for computer-based neural networks and deep learning. In 1950, Alan Turing
wrote “Computing Machinery and Intelligence” which defined the complexities of defining intelligence.
Turing’s proposal noted that a computer that was capable of conversing without being distinguished from
human interaction could loosely be regarded as having cognitive abilities, this became a test known as the
Turing test.

Pioneering developments in AI such as the Manchester Mark I were characterized by machines and limited
capabilities and focused on fundamental applications. At the Dartmouth Summer Research Project in 1956,
the Logic Theory Machine, funded by the Research and Development Corporation (RAND) was introduced.
The program was designed to mimic human’s problem-solving skills, and it was considered by many to be
the first AI program. The following years saw significant advancements in AI, such as the development of
the Symbolic Automatic Integrator (SAINT) by James Slagle in 1961, which can solve calculus problems at
a freshman level, and the creation of ELIZA, as an early natural language processing computer, by Joseph
Weizenbaum in 1965.

Despite the slowdown of interest in AI during the 1970s, SHRDLU, a program which could utilize virtual
robotic arms to manipulate virtual blocks, respond to commands in plain English and explain the necessity
of its actions was developed in 1971. Paul Werbos, an American social scientist conceptualized a method of
training artificial neural networks through backpropagation of errors. In 1975, Ted Shortliffe introduced
MYCIN, a medical diagnostic system that influenced future expert systems despite its limited use due to its
slow response speed. During the Gulf War, the Defense Advanced Research Projects Agency’s (DARPA)
Dynamic Analysis and Replanning Tool (DART) showcased AI’s practical applications revolutionizing the
logistics planning and allocation of resources in the battlefield.

The introduction of domestic AI products like Furby and AIBO opened AI for domestic consumption.
Advancements in technology in 2005 enabled companies to monitor web and media activity, facilitating
personalized product recommendation based on individual interests of customers. In 2017, Large Language
Models (LLMs) were introduced which are trained on enormous amounts of data to provide the foundational
capabilities needed to drive multiple use cases and applications. In 2018, the first Generative Pre-Trained
Transformer (GPT) algorithm was introduced which used deep learning to generate a variety of output such
as computer codes, poetry, and writing an essay. In 2022, Open AI debuted ChatGPT, an AI chatbot which
is capable of various functions such as chat support, content creation, and translation among others. The
introduction spurred the interest of the public and within two months, it reached 100 million users. In
comparison, the internet and mobile phone took twenty years to reach 80 percent of countries. It has also
galvanized other technology companies to innovate and introduce their own GPT versions such as Google’s
Gemini, Microsoft’s Bing AI, and Meta’s Llama and has led to a dramatic increase of AI patents from 2015-
2022, highlighting the swift progress made in AI development.

INTERNATIONAL MONETARY FUND

6

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

II. Context

A.  The Philippine Labor Market

Figure 1 presents several basic summary statistics that help set the context for our analysis of the Philippine
labor market and its exposure to artificial intelligence. The bulk of the workforce works in the services sector,
with the rest broadly evenly split between agriculture and industry. There is a sizeable gap in the labor force
participation between men and women with 75% of working age men either working or looking for work while
the same is only true for 53% of women. Most working Filipinos’ highest educational degree is the (junior) high
school diploma though just over a quarter do hold a college degree. The most common employment is a
salaried position (i.e., in a private company, the government, or for a private household), followed by self-
employment, and being an unpaid family worker. While the analysis in this paper focuses on the current state
of the labor market, it is important to acknowledge long-running trends in some of the variables depicted in
Figure 1 – for example, the share of employment in agriculture has seen steady declines while the share in
industry and particularly services has increased over time.

Figure 1. The Philippine Labor Force: Key Summary Statistics

Source (for all graphs): Philippine Statistics Authority (data, April 2024 vintage), Own calculations

INTERNATIONAL MONETARY FUND

7

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

During COVID-19, unemployment spiked, and the labor force participation rate dropped (Figure 2). However,
this shock gradually dissipated as the pandemic faded and the economy reopened. As of April 2024, the
unemployment rate was 4.0%, below pre-pandemic levels, and the labor force participation rate has also
recovered to pre-pandemic levels though its measurement has arguably become somewhat noisier in recent
years. There is also significant underemployment, with 10-15% of employed workers looking for additional work
or wanting longer hours of work.

Figure 2. Unemployment and Labor Force Participation

Figure 3 shows the evolution of wages over the past
15 years. The minimum wage for the national capital
region (NCR) kept pace with inflation until COVID-19 but
fell behind during the post-pandemic surge in inflation.
Average daily basic pay, meanwhile, rose faster than
inflation, bestowing workers with a roughly 30% real
wage increase since 2009. The fact that the minimum
wage did not make any gains in real terms over this time
frame suggests that most of the real wage increases
were concentrated in jobs with higher pay. These are
likely the jobs that require specific skills or education to
perform.

B.  The BPO Industry

Figure 3. Evolution of Pay in Real Terms

Wages and Inflation in the Philippines
(Index, 2009=100)

Average Daily Basic Pay

NCR Minimum Wage

Real Average Daily Basic Pay

Real NCR Minimum Wage

240

220

200

180

160

140

120

100

80

2009

2011

2013

2015

2017

2019

2021

2023

S

 CEIC

The Philippine economy is supported by its large service sector driven economy. In 2023, the services sector,
as a share of total of Gross Domestic Product (GDP) accounted for 62.3 percent. In terms of employment, the
April 2024 labor force survey from the Philippine Statistics Authority (PSA) noted that the services sector
accounted for a large share of employment at 61.4 percent. A key driver of growth in the services sector has
been the country's large Business Process Outsourcing (BPO) industry, which started in 1992. Offshore
outsourcing has allowed multi-national corporations in developed economies to conduct commercial operations
in a more cost-effective manner by tapping into a pool of highly skilled individuals in developing economies.
This has resulted in 20-40 percent reduction in costs even factoring in additional costs such as business setup
and infrastructure access (Marasigan, 2015).

INTERNATIONAL MONETARY FUND

8

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

The Philippines holds a significant portion of the global outsourcing market, estimated at 15 percent.1 This is
supported by the presence of 788 BPO companies, as reported by the Philippine Economic Zone Authority.2 In
2023, the BPO sector generated US$35.5 billion in revenues, an increase of 9 percent over the previous year,
or 8.1 percent of the country's total GDP. It also employs 1.7 million Filipinos, equivalent to 3.4 percent of the
total labor force as of 2023 (Figures 4 and 5). Despite its small share in the country's labor market, the
industry's presence in various cities throughout the archipelago generates positive spillovers to other sectors of
the economy, such as the property and services sector. Additionally, BPO revenues are substantial and nearly
as large as overseas remittances. The industry's ongoing expansion is fueled by robust government support,
low labor costs, abundant pool of service-oriented, English speaking and young workforce, and a conducive
business environment. The BPO sector in the country is composed of several business segments, in which the
majority of the revenues are generated by contact centers and back-office support services (Box 2).

The IT & Business Process Association of the Philippines (IBPAP) highlights that North America remains the
dominant market for the BPO industry with a 70 percent share. This is attributed to the region's extensive
English-speaking population, cost-effective labor, and close cultural ties with the United States. Europe and the
Asia-Pacific Region each hold 15 percent of the market share. Europe leverages the industry for its distinctive
talent specialization and cost efficiency. Conversely, the Asia-Pacific Region leverages on the relative lack of
onshore BPO centers for client markets, geographical proximity, and time zone overlap.

Box 2. Types of BPO Services

Contact Center - Consist of in-bound and outbound voice operation services for the purpose of sales,
customer service, technical support, and others.

Back Office - Service related to finance and accounting and human resource administration.

Data Transcription - Provision of transcription services for interpreting oral dictation of health professionals,
dictations during legal proceedings, and other data encoding services.

Animation - Process of giving the illusion of movement to cinematographic drawings, models or inanimate
objects through 2D, 3D, etc.

Software Development - Analysis and design, prototyping, programming, and testing, customization,
reengineering, and conversion, installation and maintenance, education and training of systems software,
middleware and application software.

Engineering Development - Includes engineering design for civil works, building and building components,
ship building, and electronics.

Digital Content - Creation of products that are available in digital form, such as music, information, and

images that are available for download or distribution on electronic media.

Source: Department of Trade and Industry (DTI), Locsin (2006), The Computer Language Company Inc. (2006)

1 https://www.magellan-solutions.com/blog/whats-the-number-analysis-of-the-latest-statistics-of-the-bpo-industry/
2 https://www.magellan-solutions.com/studies/call-center-benchmarking-report/

INTERNATIONAL MONETARY FUND

9

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Figure 4: BPO Export Revenues
In US$ Billion

Figure 5: BPO Employment
In ‘000s

Table 1: International Market Share of the Philippines’ BPO Industry

In Percent

Industry

Percent Share

Banking, Financial Services, and Insurance (BFSI)

Technology, media, and telecom (TMT)
Retail
Healthcare
Manufacturing
Energy
Others

Source: IBPAP, data as of 2023

25%

14-18%
14-18%
11-15%
6%
6%
25%

Pre-pandemic, the BPO industry, one of Manila's economic jewels largely perceived the risk of AI as limited.
The industry found solace in the fact that AI was not yet capable of demonstrating what customers needed:
empathy, problem-solving skills, or engaging in English conversations. However, this perspective underwent a
significant shift.  The BPO Industry Employees Network, a call-center union noted that improvements in AI
software have led to improved services at the expense of people's jobs. The union added that AI has turned
into an adversary and is powerless to halt its progress. Outsourcing advisory firms have warned that the
industry could face substantial job losses due to AI in the next five years (Avasant, 2024). On the other hand,
AI is also expected to create new jobs such as data curation and algorithm training (Bloomberg, 2024).

Meanwhile, IBPAP noted that AI is both an opportunity and a challenge to the sector. It recognized the
challenges that employees need to face such as improving skills in data handling, sharpening emotional
intelligence and creativity through training courses and partnering with educational institutions. On the other
hand, it acknowledged the potential benefits that can lead to the adoption of AI such as boosting productivity
and improving customer experience, reduction of costs, and revenue growth.

INTERNATIONAL MONETARY FUND

10

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Before, the threat of automation was contained to low-skilled, blue-collar jobs. However, generative AI's
capabilities now pose a threat to white-collar jobs, especially for IT-BPM workers as customer services agents,
tech support, and non-university educated employees. The Department of Labor and Employment (DOLE) has
acknowledged that Filipinos are already losing jobs due to AI. In contrast, a survey conducted by Microsoft and
LinkedIn showed that Filipino professionals are actively incorporating AI to their workflows. It indicated that 86
percent of Filipino professional workers that have been surveyed already use AI in some form, higher than the
global average of 75 percent. Meanwhile, 55 percent of Filipinos who were surveyed are worried that their
organizations lack plans and visions for implementing AI. Ng, et al. (2023) noted that generative AI can unlock
US$79.3 billion in productive capacity, or equivalent to one-fifth of the country's 2022 GDP by 2030 especially
in the country's manufacturing and Wholesale and Retail Trade sectors, largely due to its large share in the
local workforce. In addition, GenAI is foreseen to complement the workforce, rather than replacing people
entirely. The study noted that only one percent of the workforce would see GenAI utilized more than 20 percent
of the work while 56% of workers in the Philippines will potentially use generative AI for between 5-20% of their
regular work activities. Indeed, BPO companies have started to introduce AI assistant or copilots working
alongside humans.

III.  Existing Literature

The academic literature has approached the study of AI through the lens of task-based models such as
Acemoglu and Restrepo (2019) which were originally developed to study the impact of automation and
robotics. This literature has identified three main channels through which automation may impact
macroeconomic outcomes such as GDP, unemployment, and the income shares of capital and labor.
Automation or AI may cause unemployment by replacing labor with machines (displacement), it may increase
the productivity of existing capital or labor (productivity), and it may even generate new tasks and new jobs for
producing and maintaining these machines (reinstatement)3.

There is no consensus in the academic literature on the magnitude or relative importance of these channels.
Frank et al. (2019) classifies researchers as either doomsayers or optimists but there are also prominent
academics arguing that little change will come about. In terms of the most recent debate on the productivity
impact of generative artificial intelligence, the two ends of the spectrum have been shaped by Acemoglu (2024)
and Korinek (2024). Acemoglu (2024) argues that AI will bring only marginal TFP improvements of no more
than 0.71% over ten years while Korinek (2024) predicts that the inevitable advent of artificial general
intelligence will make all human work obsolete and drive the income share of labor to zero.

Empirical and experimental work has focused on more near-term and immediately quantifiable metrics. One
strand looks at the overlap between occupational tasks and the capabilities of AI (Felten et al. 2021; Pizzinelli
et al. 2023; Eloundou et al., 2023, Webb 2020). Gmyrek et al. (2023) even employ AI itself (GPT-4) to estimate
task-level exposure scores. Brynjolfsson et al. (2023) find that generative AI increases the productivity of
novice contact center workers the most while experienced workers benefit little. Others have studied labor
market outcomes - Hui, Reshef, Zhou (2023) find that writing-related occupations and freelancers saw a 2.0
percent decline in the number of monthly jobs and a 5.2 percent decrease in monthly wages following the
public availability of generative AI.

3 See Berg et al. (2024) for a more detailed discussion of these channels.

INTERNATIONAL MONETARY FUND

11

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

In the context of emerging markets, Das and Hilgenstock (2018) studied 160 countries from 1969 to 2015 and
noted that EM economies are less susceptible to routinization and thus automation as production in these
economies is less capital intensive, with manual and mainly low-skilled occupations which are not easily
automated. In addition, the authors noted that the large degree of informality in the economy, lack of supporting
infrastructure such as but not limited to fast and stable internet connection, mobile coverage, computers,
electricity, and adequacy of education and skills insulates EMs from the influence of GenAI in their labor
markets. Even within emerging markets, this effect can generate differences. Carbonero et al. (2021) compare
the effects of AI on the labor markets of Vietnam and Lao PDR. Vietnam has a higher risk of job displacement
from AI due to labor composition differences and past industrialization. In contrast, Lao PDR has a larger share
of agricultural workers. Both countries have high potential for AI adoption and task reorganization within
occupations, but many job activities remain unsuitable for AI, mitigating labor displacement. In a service-centric
economy like India, Copestake et al. (2023) find that jobs that harness AI can offer a substantial wage
premium. However, these only benefit a niche group of workers, particularly those with AI skills, and are
concentrated only in specific industries, places, and corporations. Displacement is primarily present in older
'incumbent' enterprises that do not adopt AI.

In the Philippines, Gaspar and Harris (2020) discovered that non-production workers have better job prospects
due to their roles being less automatable and their higher skills. However, the authors noted that this may lead
to increased trends of seasonal work, which may increase workers' exposure to economic shocks. In the short
run, employment gains may not continue with advanced technologies such as AI, while its long-term effects
remain uncertain. Additionally, the researchers indicated that AI adoption in the Philippines can create jobs,
provided that proper training exists to offset its adverse effects. In fact, firms in the country that adopt
automation are more likely to hire additional employees rather than lay them off.

The BPO industry, which predominantly focuses on routine-centric tasks and low-skilled roles such as
answering phone calls and dealing with inquiries, may be adversely affected by AI. An (ILO, 2017) study noted
that modern algorithms and programs have already undermined the availability of jobs in the sector, which
often requires basic literacy and English language skills. It estimates that 89 percent of the BPO workforce is at
high risk of automation as consumers and clients demand better services and explore cost-saving measures.
Two main technologies have been mentioned that influenced the radical shift in the BPO industry: cloud
technology and robotic process automation. The former uses a network of online servers to manage, store, and
analyze data on cloud platforms, while the latter utilizes software with algorithms to execute highly structured
and routine operations. In fact, a recent report by the ASEAN Macroeconomic Research Office (AMRO)
mentioned that the large BPO industry in the economy can face a greater risk of worker displacement, primarily
those engaged in routine work, as AI gradually reshapes ICT operations. AMRO stated that the country should
upgrade its BPO services to more knowledge-based services (AMRO, 2024).

Conversely, reports by the World Bank (2024a, 2024b) reported the significant adoption of generative AI tools
in the Philippines, driven by its young, tech-savvy population and digital infrastructure. The study also revealed
that GenAI is primarily used for productivity-related tasks. This has contributed positively to the economy,
especially in sectors that require high-skilled tasks. However, challenges such as digital infrastructure and skills
development need to be addressed to fully harness AI's benefits. Broadly, there is a proactive stance in the
country in integrating AI technologies.

INTERNATIONAL MONETARY FUND

12

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

IV.  Data and Methodology

This section provides additional details on the exposure and complementarity metrics as well as the Philippine
labor force survey data. Felten et al. (2021) introduce the AI Occupational Exposure (AIOE) measure to
evaluate the overlap between AI capabilities and the required tasks for different occupations. To construct the
AIOE, the authors first identify ten common AI applications4, such as reading comprehension, image
recognition and speech recognition, sourced from the Electronic Frontier Foundation's AI Progress
Measurement project. Then, the authors obtain occupational "abilities" using data from the Occupational
Information Network (O*NET), a database sponsored by the U.S. Department of Labor containing lists of
required tasks to perform each occupation together with tasks' relative importance. Lastly, the authors connect
the occupational abilities to AI capabilities via relevance ratings obtained from a crowd-sourced dataset.5 The
ability-level AI exposure scores are calculated by summing the relevance ratings of all AI applications for each
ability within an occupation. These scores are then aggregated to the occupation level, weighted by the
prevalence and importance of each ability within an occupation. This results in an occupation-level AIOE score
for 774 different occupations. The score is standardized such that the median of the score is zero and the
standard deviation is one. Figure 6 shows the distribution of AIOE scores across aggregated occupations.

Figure 6. Exposure and Complementarity Across Occupations

Pizzinelli et al. (2023) build on the AIOE by introducing a complementarity index to account for the extent to
which AI complements or substitutes human labor. The complementarity index is high for occupations where AI
is more likely to complement human abilities rather than substitute them. It is calculated by considering both the
importance of AI applications and the context in which they are used, reflecting societal and technical
constraints that may limit AI's substitutive potential in certain jobs.6 It therefore highlights occupations that,
despite high AI exposure, may not experience significant displacement due to the complementary nature of AI

4 The ten applications are abstract strategy games, real-time video games, image recognition, visual question answering, image
generation, reading comprehension, language modeling, translation, speech recognition, instrumental track recognition.
5 The relevance ratings come from a dataset provided by Amazon which aggregates a large number of survey responses on the

relevance of certain AI applications for different tasks.

6 The six components of the score are communication, responsibility, physical conditions, criticality, routine, and skills. The O*NET
database records a relevance score of these components for each occupation. The complementarity score is the weighted
average of these sub-scores. See Pizzinelli et al (2023) for details.

INTERNATIONAL MONETARY FUND

13

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

in those roles. For example, professionals and managers tend to have high exposure but also high
complementarity scores, indicating that AI is more likely to augment rather than replace their work. On the other
hand, clerical workers, who generally face higher substitution risks, show high exposure but lower
complementarity scores, making them more vulnerable to AI-driven disruption. The two dimensions provide
sufficient nuance to obtain a clearer understanding of the potential impacts of AI on the labor market by
considering both exposure and the likelihood of AI acting as a complement. For the remainder of the paper,
"high"/"low" exposure/complementarity for a given occupation mean that the occupation has an above median
exposure/complementarity score.

We merge the exposure and complementarity scores with labor force survey microdata from the Philippine
Statistics Authority, specifically the October 2022 vintage which contains 183,602 observations for 52 variables.
Critically, the LFS microdata contain information on occupations at the 4-digit ISCO-08 level (there are 436
occupations in total), allowing a very granular look at the distribution of occupations in the Philippines7.

Several important caveats apply to our analysis. The most important one is that the analysis in this paper is
static. The data we use presents a snapshot of the current labor market in the Philippines and the scores
linking jobs to AI is based on the current state of AI's capabilities which are rapidly evolving. Over the medium
to long term, workers will retrain and adapt, and new jobs may emerge. This process is likely to vary across
countries, sectors, firms, and even at the occupational level. Over time, resources will be reallocated across
sectors which could in turn generate feedback effects which would not be captured in this analysis. The results
in this paper are therefore likely to be more relevant for the short to medium term. Second, the AI exposure and
complementarity scores are designed to capture the capabilities of generative AI. The results in this paper
therefore do not speak to the impact of potential advances in automation or robotics which may materialize in
the future as AI is deployed and will likely impact different occupations than those affected by generative AI.

Another important assumption underlying this work is that the tasks in each job and their relative importance do
not vary across countries. The work by Felten et al. (2021) and Pizzinelli (2023) relies on the O*NET database
which contains data on occupations in the U.S. The literature on studying the impact of AI on both developed
and developing countries (see also Dalla Zuanna (2024), IMF (2025)) has so far operated under the premise
that tasks performed within each occupation are similar around the world. However, recent studies, e.g.
Caunedo et al. (2023), suggest that some occupations in developing countries tend to be more intensive in
routine and therefore automatable tasks. In similar fashion, the societal context of each occupation and as a
result the extent to which it is shielded from being replaced by AI could vary across countries. Taken together,
this would potentially imply a higher exposure and/or lower complementarity for some occupations. The
estimates presented in this paper can therefore be interpreted as being on the conservative side. Future work
tweaking exposure and complementarity scores to the country level would be a helpful contribution to the
literature, data permitting.

V.  Analysis and Labor Market Implications

Table 2 shows example occupations for the three exposure/complementarity categories along with their shares
in the Philippine workforce. 36% of workers are highly exposed to artificial intelligence and over a third (39%) of

7 To translate the AIOE scores from the Standard Occupational Classification (SOC) system to the ISCO-08 classification, the SOC-

ISCO-08 crosswalk published by the US Bureau of Labor Statistics is used.

INTERNATIONAL MONETARY FUND

14

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

those highly exposed have low complementarity. Comparing the results for the Philippines with peer countries
in the region is possible with some caveats; the appendix contains the details.

Table 2. AI Exposure and Complementarity in the Philippines

Exposure  Complementarity  Example Occupation Titles

Share (PHL)

High

High

General and Operations Managers, First-Line Supervisors, Teachers and
Teaching Assistants, Lawyers, Civil Engineers, Counselors

High

Low

Customer Service Representatives, Telemarketers, Accountants, Auditors,
Secretaries, Administrative Clerks

Low

n/a

Farmworkers, Construction Laborers, Janitors, Maids and Cleaners, Waiters,
Textile workers, Food Preparation Workers

22%

14%

64%

Figure 7 presents the distribution of exposure and complementarity across major occupational groups. It shows
that occupations with low exposure are mostly agriculture workers, the trades, elementary occupations, and
some services. Moving to highly exposed professions, Managers, Professionals, and some service workers are
most likely to benefit from AI indicated by their high complementarity score. Those occupations most likely to
be displaced by AI are clerical support workers, some professionals, and some service workers.

Figure 7. AI Exposure by Occupation

The microdata from the PSA also allows us to look at how exposure and complementarity correlate with other
socio-economic and demographic variables. Figure 8 shows the gender, age, education, income, regional, and
sectoral dimensions. We note a substantial difference along the gender dimension with female workers much
more exposed to AI than male workers. This is due to more women being employed as clerical support,
service, and sales workers whereas men have a higher share in trades, agriculture, machine operations, and

INTERNATIONAL MONETARY FUND

15

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

elementary occupations which are less likely to be impacted by AI at this stage (see Figure 11 in the appendix).
A similar argument applies to the education variable. College-educated workers are more often employed as
managers, professionals, or technicians. Here, we also note that jobs with high complementarity potential tend
to be held by college-educated workers. As the world of work changes, this means that they are more likely to
have the requisite skills to harness the productivity benefits from AI. Along the age dimension, overall exposure
does not vary much. However, Figure 8 shows that older workers tend to hold more complementary jobs as
they are more represented in managerial roles. It will be critical for young workers to have the skills that allow
them to employ AI to increase their productivity for the Philippines to capitalize on the impending demographic
dividend8. There may also be age-based differentials in skill sets when it comes to the use of digital
technologies which need to be accounted for (see policy section).

Figure 8. Exposure and Complementary by Gender, Age, Education, Wage, Location, and Sector

8 See selected issues paper on Potential Growth and Demographic Dividend of IMF Country Report No. 24/352

INTERNATIONAL MONETARY FUND

16

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Sources: Philippine Statistics Authority; and IMF staff calculations.

The results in Figure 8 also show that AI could have profound implications for wage9 inequality. College-
educated workers in well-paid occupations which lend themselves to integration with AI could see their
productivity, and thus likely also their wages, improve dramatically. At the same time, many college-educated
workers are also in occupations which could be eliminated by AI, potentially shifting income dynamics in favor
of blue-collar workers. It is in this respect that recent technological advances differ from those seen in the past
which have typically replaced low-skilled and low-income laborers. It is worth noting, however, that there is
considerable disagreement in the literature on the longer-term direction and magnitude of AI's impact on
wages. Some (e.g. Korinek (2024)) argue that the advent of artificial general intelligence will eventually cause
competitive market wages to plummet whereas others (e.g. Acemoglu (2018)) argue that higher productivity
and the creation of new labor-intensive jobs are forces that could support the labor share of income over the
long run. The purpose of this paper is not to take a stance on the debate but instead to flesh out the
characteristics and distribution of potentially impacted workers in the Philippine labor force.

In terms of sectors of the economy, Figure 8 reveals that AI is a phenomenon which will mostly affect the
services sector. This is of course not a particularly surprising result - however, it is important to note that there
is high heterogeneity within the services sector (see Figure 12 in the appendix). The subsector with the highest
proportion of occupations classified as high exposure/low complementarity is the BPO sector.10 73 percent of
workers employed in this sector are "Contact Center Information Clerks”11 which score highly on AI exposure
but low on complementarity. Meanwhile, the subsector with the highest proportion of occupations classified as
high exposure/high complementarity is the education sector. 12 The bulk of occupations in this sector are

9 The labor force survey captures individual’s basic pay per day in their primary occupation. The cutoffs for the quintiles of this
distribution are 300/400/500/700. In other words, 20 percent of workers earn less than 300 PHP/day, the next 20 percent earn
between 300 and 400 PHP/day, and so on.
10 ISIC Rev. 4 Code 82, “Office administrative, office support and other business support activities, including activities of call

centers”.

11 ISCO-08 code 4222
12 ISIC Rev. 4 Code 85, “Education”

INTERNATIONAL MONETARY FUND

17

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

"Secondary Education Teachers" and "Primary School Teachers”13 which score highly both on exposure and
complementarity to AI. Overall, this illustrates the high heterogeneity even within the services sector.

When comparing exposure and complementarity across different types of employment (see Figure 13 in the
appendix), government workers stand out as the most exposed, with a substantial portion of that rated as low
complementarity. This is driven by the high number of general, accounting, and bookkeeping clerks working for
the government. The high share of high complementarity jobs in this category is driven by teachers. While self-
employed workers exhibit an average proportion of low complementarity jobs, the impact of job displacement
could be higher given potentially unstable work arrangements and limited social protection for this type of
worker.

VI.  AI Preparedness

While the exposure and complementarity of occupations to AI may be one of the most important factors, there
are several other aspects which will have a profound impact on the adoption of AI in the Philippines.

The AI preparedness index (AIPI) developed by Cazzaniga et al. (2024) is based on four key dimensions which
are likely relevant for smooth AI adoption: digital infrastructure, human capital and policies, innovation and
integration, and regulation and ethics. For each dimension, the authors collect a rich set of indicators compiled
by different institutions, including, but not limited to, sustained human capital investment, inclusive STEM
expertise, labor and capital mobility within and across countries, R&D ecosystem, and the adaptability of legal
frameworks to digital business models. All indicators are normalized to a 0-1 scale and then averaged. The
AIPI is the simple average of the four dimensions.

13 ISCO-08 codes 2330 and 2341

INTERNATIONAL MONETARY FUND

18

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Figure 9. AI Preparedness Across Asia

Comparing the scores for the Philippines against other Asian economies shown in Figure 9, the Philippines
emerges as broadly in line with the scores of its emerging market peers (red dashed boxes). Looking at the
underlying components, the Philippines scores well on human capital (light blue bars) but less so on digital
infrastructure (dark blue bars) when compared to both its ASEAN peers but also emerging markets more
broadly. The quality and reach of digital infrastructure may have implications on how much (or how little) the
country can benefit from AI, even in occupations with high exposure/high complementarity with AI.

Several caveats apply to the AIPI. First, the AIPI does not capture all dimensions that could affect the adoption
of AI. For instance, the importance of the BPO sector in the Philippines is not considered. Second, there is high
uncertainty about what the institutional requirements for an economy-wide integration of AI will ultimately be. As
a result, the AIPI should be seen as an indicative exercise to highlight potential areas for improvement along
the four dimensions. For the Philippines, the AIPI points to room for further enhancements along all dimensions
and particularly in digital infrastructure. This would likely also help greatly with harnessing the opportunities
presented by the Philippine's human capital considering the country's impending demographic dividend.
Further work identifying specific preparedness gaps in the Philippines, going beyond the labor-market focused
analysis in this paper, would be beneficial.

INTERNATIONAL MONETARY FUND

19

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

VII. Regulatory Framework

Understanding the implications of AI and establishing a clear regulatory framework is vital to harness its full
potential and economic benefits. Currently, there is no legislative framework to guide investments, foster
research and development, and prepare the workforce for AI development and application in the Philippines.
However, the country has recognized the need for such a framework and has taken initial steps towards this
goal. In 2021, the Philippine government formulated the National AI Strategy Roadmap, which was
subsequently updated in July 2024. The main goal of the National AI Strategy Roadmap 2.0 is to guide the
government and the private sector in the use of AI and related technologies and how they can be utilized for
national development.

The latest roadmap has the following main objectives: 1) Increased local industries' regional and global
competitiveness; 2) Promote collaboration between the government, private sector, and the academia in
research and development; 3) Identify key investment areas in research and development; 4) Prepare the
workforce for future jobs; 5) Attract major industries to create jobs; 6) Ensure responsible rollout and
governance of AI technologies.

Figure 10: National AI Strategy Pillars, Dimensions, Imperatives

Source: DTI, National AI Strategy Roadmap (2021)

Note: DTI is still finalizing the National AI Strategy Roadmap 2.0. Chart above was sourced from the 2021 AI Roadmap.

In addition to the National AI Strategy Roadmap, the government has passed Republic Act (RA) No. 11962,
also known as the Trabaho Para sa Bayan Act. Recognizing the changing employment landscape due to
emerging technologies, the law aims to establish a ten-year National Employment Master Plan (TPB) with four
strategic priorities: stimulating national and local economic growth to address labor market challenges;
improving the employability and competitiveness of Filipino workers by aligning education and training
programs with industry requirements; reducing regulatory burdens on micro, small, and medium enterprises,
including increasing access to capital, security, and protection; and encouraging upskilling and reskilling
workers by leveraging opportunities provided by AI tools. It is anticipated that the TPB will generate three
million jobs by 2028.

INTERNATIONAL MONETARY FUND

20

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Furthermore, as part of the government’s overall strategy on AI, there are pending legislations in Congress
which aims to promote the development, deployment, and regulation of AI14. These propose to establish
various official bodies (Philippine Council of Artificial Intelligence, AI Development Authority, National Center for
Artificial Intelligence Research), and regulatory frameworks for the use of AI in the workplace and ethical AI
development. It is important to note that these AI specific legislations are still in their infancy, will evolve along
the legislative process, and may be overlapping in scope.

References to AI can also be found in other, broader, government strategies. The Philippine Development
Plan, which serves as the government’s overall guide in development planning, expresses the commitment of
the government to adopting AI, including the following strategies: Anticipate skills needs in priority sectors
(Chapter 4, Outcome 2),increase access of MSMEs to capital, digital technologies, and startups (Chapter 7,
Outcome 2), support globally competitive industries and an agile workforce (Chapter 8, Outcome 4), enhance
monitoring and understanding of emerging technologies, markets, and business models (Chapter 10, Cross-
Cutting Strategies), and promote RegTech development (Chapter 11, Cross-Cutting Strategies).

Identification of gaps in current policies and challenges in implementation.

History has shown that technological development is guided by the decisions made by regulators. The rapid
advancement of AI has led to policy gaps and hurdles that limits its adoption, limiting the Philippines’ ability to
fully harness the potential benefits of AI.

Gaps in Regulation and Governance: Understanding AI’s implications is crucial in managing risks and
opportunities. The National AI Strategy Roadmap and its updated version are promising steps, but lack of
legislation limits its effectiveness. A forthcoming harmonized legislation from the proposed bills will manage AI
risks like algorithmic transparency, cybersecurity, privacy, errors, biases, and labor protection.15 Regulation will
also promote best practices and cooperation between the government and private sector. However, with the
rapid advancement of AI, regulations surrounding the country’s data privacy and intellectual property laws must
evolve to keep pace.  For example, the United Kingdom and European Union have guidelines for ethical AI
use, and the UN adopted a resolution for safe AI in March 2024.16

Gaps in Physical and Digital Infrastructure: AI requires robust physical and digital infrastructure. For
instance, an AI chatbot handling 195 million queries needs data centers consuming power equivalent to 23,000
U.S. households. It is forecasted that data centers’ electricity consumption is expected to increase, straining
electricity grids for countries like the US and Ireland. Similarly, expanding the adoption of AI in the Philippines
will have important implications for power demand and infrastructure needs17, which come on top of the
existing gaps in access to and quality of power supply—about two million households still lack electricity, and
power interruptions remain common (PIDS, 2023). A fast and reliable internet connection is also crucial for AI,
yet the Philippines has slow speeds and high costs. In the 2023 Worldwide Broadband Speed League, the
Philippines ranked 86th out of 220 countries with an average download speed of 43.36mbps, lower than the

14 As of January 2025, these include house bills 7396, 9448, 7913, 7983
15  https://lti.institute/2022/09/how-regulation-can-catch-up-with-ai/
16 https://news.un.org/en/story/2024/03/1147831
17 https://www.bworldonline.com/economy/2024/02/25/577716/energy-dept-seeking-to-gauge-major-data-centers-re-

needs/#:~:text=The%20Philippines%20is%20positioning%20itself,approximately%20300%20MW%20by%202025.

INTERNATIONAL MONETARY FUND

21

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Asian average of 45.72mbps.18 Meanwhile, the World Data Lab estimates that nearly 19 million Filipinos or
16.6 percent of the population cannot afford a minimum package of internet.19 The quality and reach of digital
infrastructure will matter not just on the household side, but also on the firm side, particularly for MSMEs, which
may face challenges in terms of capacity, cost, access.

Upskilling and Reskilling: The Future of Jobs report states that 23 percent of the workforce will change within
five years, with 60 percent needing training by 2027 which are centered on creative and analytical thinking, AI,
and big data (WEF, 2023)20. Despite high internet penetration, 90 percent of Filipinos lack basic ICT skills. The
Philippines also lags in international education assessments in mathematics, reading, science, and creative
thinking. Workers also lack soft skills like adaptability, problem-solving, and collaboration (PIDS, 2023). Despite
the high demand for trainings, obstacles to skills enhancement include inadequate internet access, lack of time,
high training costs, and limited opportunities (Economist, 2023). 21 However, the government has multiple
training initiatives that are underway, that are backed by the industry to boost reskilling. In addition, the
government is also updating the education curriculum and reskilling educators to meet to industry needs.22
IBPAP noted that the Philippine tech industry is expected to generate 1.1 million new jobs by 2028,
necessitating a steady supply of skilled workers.

Use Cases and the Cost of Adoption: The Philippine AI Roadmap has noted that one of the gaps in adopting
AI is that some companies in the Philippines do not yet fully comprehend its capabilities and limitations to utilize
and enhance their productivity and efficiency. Moreover, hesitancy remains in adopting AI and emerging
technologies due to high costs and lack of clear and tangible returns. Firms in the country noted that key
roadblocks in modernizing their technology is the high fixed capital costs followed by high licensing costs
associated with technology adoption (ILO, 2017). In addition, a survey made by Cisco, noted that firms in the
Philippines have expressed that only 17 percent are ready to deploy and use AI in their business processes, 44
percent are said to be moderately ready, 35 percent indicated they have minimal readiness while 4 percent
answered they are not prepared to use AI. The clear understanding of AI may also entice the private and public
sector to support research and development. Currently, the Philippines is spending less than 0.2 percent of
GDP, equivalent to US$0.8bn, lower than the global benchmark of 1 percent of GDP or US$3.75bn. This
places the Philippines second last compared to other Southeast Asian countries (DTI, 2021).

VIII. Policies to Foster AI Adoption and Harness
its Benefits

The analysis in this paper shows that a substantial proportion of the Philippine labor force will be impacted by
AI. 14 percent of jobs are classified to be at risk of displacement by AI and another 22 percent are likely to see
the nature of their work change significantly as AI is rolled out. The BPO sector is the most exposed sector of
the economy and therefore deserves particular attention. While BPO sector employees only make up about 3
percent of the total workforce, the size of its revenues (7.4 percent of GDP, similar in magnitude to all

18 https://www.pids.gov.ph/details/news/in-the-news/think-tank-says-ph-connectivity-still-lags-behind-in-

asia#:~:text=Despite%20this%20improvement%2C%20however%2C%20the,Asian%20average%20of%2045.72%20Mbps.

19 https://www.bworldonline.com/infographics/2022/04/18/442463/philippines-most-internet-poor-in-southeast-asia/
20 https://www.weforum.org/publications/the-future-of-jobs-report-2023/digest/
21 https://impact.economist.com/perspectives/talent-education/bridging-skills-gap-fuelling-careers-and-economy-philippines#_ftn21
22 https://www.philstar.com/headlines/2024/06/26/2365677/ai-education-pressing-issues-employers-ecop

INTERNATIONAL MONETARY FUND

22

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

remittances) generates large potential spillovers from changes in the BPO sector to other parts of the economy.
This section lays out several key areas that policymakers can focus on to harness the opportunities and
mitigate the risks presented by the rollout of AI.

The first key area for policymakers is investment in digital infrastructure. The quality and reach of the digital
infrastructure in the Philippines are uneven, with significant disparities between urban and rural areas.
Improving internet connectivity, expanding electricity grids, and ensuring reliable access to power will be
critical. The government should also support the development of a robust digital economy and entrepreneurial
ecosystem, which can foster innovation and create an environment conducive to AI deployment. Providing
fiscal incentives for private sector investment in AI, such as research and development grants, can stimulate
technological advancements and facilitate the integration of AI across various sectors.

Second, enhancing human capital through education and training programs is essential. The Philippines has a
relatively young and dynamic workforce with English language skills, but there are gaps in digital literacy and
advanced technical skills23. The education system needs to be updated to include AI and related subjects, and
there should be a focus on upskilling the current workforce. Studies have shown that introducing basic
concepts in early education can build foundational understanding and critical thinking in young students24. On
the tertiary level, studies argue that AI education should focus on specialized knowledge and applications
which can prepare students for advance roles in their chosen fields. Meanwhile, technical vocation and training
(TVET) play a crucial role in AI adoption by developing sector-specific skills, adapting curricula to meet industry
needs, and providing lifelong learning opportunities to ensure continued employability and inclusivity to a
broader segment of society. Beyond formal education, policymakers will need to promote lifelong learning and
upskilling initiatives to prepare the workforce for AI-related changes. This includes offering specialized training
programs to help workers adapt to new technologies. Additionally, fostering collaboration between academia,
industry, and government can help bridge the skills gap, ensure that training programs are up-to-date vis-à-vis
the latest developments in this fast-changing field, and equip the workforce with the necessary skills to thrive in
an AI-driven economy.

Third, strengthening social protection systems to support workers during transitions, such as unemployment
insurance, will also be crucial in mitigating the potential negative impacts of AI on the labor market. The
Philippine Social Security System already explicitly allows claiming unemployment benefits in the case of
redundancy due to the “installation of labor-saving devices”25. Against this backdrop, instituting reskilling and
upskilling programs could help workers transition to different jobs without having to rely on unemployment
insurance. This needs to be combined with developing strategies for businesses to responsibly integrate AI
while supporting and training workers. The potentially increased use of unemployment insurance and the cost
of reskilling programs may also involve fiscal cost which would need to be budgeted for. Over the medium term,
the taxation of capital income may need to be recalibrated if the income share of labor does indeed decline due
to the adoption of AI (see Cazzaniga et al. (2024)) for a more in-depth discussion.

Overall, a comprehensive strategy that includes infrastructure development, human capital enhancement, and
supportive fiscal policies will be essential for the Philippines to fully capitalize on the opportunities presented by
AI. This paper has fleshed out the geography of the labor market which will help policymakers tailor and target

23 Chapter 5 of OECD (2023) discusses skill needs in the age of AI in detail.
24 See Yim and Su (2024)
25 Source: https://www.sss.gov.ph/unemployment-benefit/

INTERNATIONAL MONETARY FUND

23

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

their measures to those parts of the economy that benefit from them most. This approach will help the country
navigate the challenges of AI integration and position itself as a competitive player in the global digital
economy. The Philippines is not the only country facing the enormous challenge of effectively making use of AI.
International partnerships, peer learning, and support from organizations like the IMF will help along the way.

INTERNATIONAL MONETARY FUND

24

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

References

Acemoglu, D. and Restrepo, P., 2020. Robots and jobs: Evidence from US labor markets. Journal of political

economy, 128(6), pp.2188-2244.

Acemoglu, D., 2024. The Simple Macroeconomics of AI (No. w32487). National Bureau of Economic Research.

Asian Development Bank Institute. (2020). ADBI Working Paper 1081. Retrieved from

https://www.adb.org/sites/default/files/publication/566281/adbi-wp1081.pdf

ASEAN+3 Macroeconomic Research Office. (2024). AREO 2024 Special Feature. Retrieved from https://amro-

asia.org/wp-content/uploads/2024/04/AREO-2024-C2-Special-Feature.pdf

Berg, A., Papageorgiou, C. and Vaziri, M. (2023). Technology’s Bifurcated Bite. Finance & Development

Magazine, IMF. Retrieved from: https://www.imf.org/en/Publications/fandd/issues/2023/12/Technology-
bifurcated-bite-Berg-Papageorgiou-Vaziri

Bernardo, A. B. I., Albert, J. R. G., Vizmanos, J. F. V., & Muñoz, M. S. (2023). Toward measuring soft skills for

youth development: A scoping study. Discussion Papers (No. 2023-28). Philippine Institute for
Development Studies. https://doi.org/10.62986/dp2023.28

Brynjolfsson, E., Li, D. and Raymond, L.R., 2023. Generative AI at work (No. w31161). National Bureau of

Economic Research.

Carbonero, F., Davies, J., Ernst, E., Fossen, F.M., Samaan, D. and Sorgner, A., 2023. The impact of artificial
intelligence on labor markets in developing countries: a new method with an illustration for Lao PDR and
urban Viet Nam. Journal of Evolutionary Economics, 33(3), pp.707-736.

Caunedo, J., Keller, E. and Shin, Y., 2023. Technology and the task content of jobs across the development

spectrum. The World Bank Economic Review, 37(3), pp.479-493.

Cazzaniga, M., Jaumotte, M.F., Li, L., Melina, M.G., Panton, A.J., Pizzinelli, C., Rockall, E.J. and Tavares,
M.M.M., 2024. Gen-ai: Artificial intelligence and the future of work. International Monetary Fund.

Copestake, A., Marczinek, M., Pople, A., & Stapleton, K. (2023, March). AI and services-led growth: Evidence

from Indian job adverts. [Working Paper]. Centre for Economic Policy Research (CEPR). Retrieved from
https://steg.cepr.org/sites/default/files/2023-
03/WP060%20CopestakeMarczinekPopleStapleton%20AIAndServicesLedGrowth_0.pdf

Centre for Economic Policy Research. (2023). Fear of Technology-Driven Unemployment and Its Empirical
Base. Retrieved from https://cepr.org/voxeu/columns/fear-technology-driven-unemployment-and-its-
empirical-base

Cornell University. (2023). Artificial Intelligence and Its Short-Term Effects on Employment. Retrieved from

https://arxiv.org/pdf/2303.10130

Dalla Zuanna, A., Dottori, D., Gentili, E. and Lattanzio, S., 2024. An assessment of occupational exposure to

artificial intelligence in Italy (No. 878). Bank of Italy, Questioni di Economia e Finanza (Occasional Papers).

Das, M. and Hilgenstock, B., 2022. The exposure to routinization: Labor market implications for developed and

developing economies. Structural change and economic dynamics, 60, pp.99-113.

Department of Trade and Industry Philippines. (2021). National AI Strategy Roadmap.

INTERNATIONAL MONETARY FUND

25

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Economist Impact. (2023). Bridging Skills Gap: Fuelling Careers and Economy in the Philippines. Retrieved

from https://impact.economist.com/perspectives/talent-education/bridging-skills-gap-fuelling-careers-and-
economy-philippines#_ftn21

Eloundou, T., Manning, S., Mishkin, P. and Rock, D., 2023. Gpts are gpts: An early look at the labor market

impact potential of large language models. arXiv preprint arXiv:2303.10130.

Emerald Insight. (2023). Economics of ChatGPT: A Labor Market View on the Occupational Impact of Artificial

Intelligence. Retrieved from https://www.emerald.com/insight/content/doi/10.1108/JEBDE-10-2023-
0021/full/pdf?title=economics-of-chatgpt-a-labor-market-view-on-the-occupational-impact-of-artificial-
intelligence

Ewrin, R. (2017). History of artificial intelligence. In Artificial intelligence: The quest for the ultimate thinking

machine (pp. 45-54). Arcturus Publishing Ltd.

Felten, E., Raj, M. and Seamans, R., 2021. Occupational, industry, and geographic exposure to artificial

intelligence: A novel dataset and its potential uses. Strategic Management Journal, 42(12), pp.2195-2217.

Frank, M.R., Autor, D., Bessen, J.E., Brynjolfsson, E., Cebrian, M., Deming, D.J., Feldman, M., Groh, M., Lobo,

J., Moro, E. and Wang, D., 2019. Toward understanding the impact of artificial intelligence on labor.
Proceedings of the National Academy of Sciences, 116(14), pp.6531-6539.

Gaspar, R. and Harris, N., 2020. The fate of job creation in the Philippines amid the automation revolution: A

firm-level analysis (No. 1081). ADBI Working Paper Series.

Gmyrek, P., J. Berg, and D. Bescond. 2023. Generative AI and Jobs: A Global Analysis of Potential Effects on
Job Quantity and Quality. ILO Working Paper 96. International Labour Organization, Geneva, Switzerland.

Hebrew University of Jerusalem. (2023). Automation and Employment. Retrieved from

https://en.economics.huji.ac.il/sites/default/files/economics-en/files/automation_4.pdf

Hui, X., Reshef, O. and Zhou, L., 2023. The short-term effects of generative artificial intelligence on

employment: Evidence from an online labor market. Available at SSRN 4527336.

Institute of Labor Economics. (2023). IZA Discussion Paper 14944. Retrieved from

https://docs.iza.org/dp14944.pdf

International Labour Organization. (2017). ILO Report. Retrieved from

https://www.ilo.org/media/421871/download

International Monetary Fund. (2018). IMF Working Paper 135. Retrieved from

https://www.elibrary.imf.org/view/journals/001/2018/135/article-A001-en.xml

International Monetary Fund. (2025). Transforming the Future: The impact of artificial intelligence in Korea.

Selected Issues Papers.

Korinek, A. and Juelfs, M., 2022. Preparing for the (non-existent?) future of work (No. w30172). National

Bureau of Economic Research.

Liu, Y., & Wang, H. (2024). Who on earth is using generative AI? Policy Research Working Paper No. 10870.

Washington, DC: World Bank. Retrieved from:
https://openknowledge.worldbank.org/entities/publication/5a876bd0-f85a-479b-ae32-cf0b7f33792f

MIT Initiative on the Digital Economy. (2016). AER Article. Retrieved from
https://ide.mit.edu/sites/default/files/publications/aer.20160696.pdf

INTERNATIONAL MONETARY FUND

26

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

National Bureau of Economic Research. (2023). NBER Working Paper 30074. Retrieved from

https://www.nber.org/system/files/working_papers/w30074/w30074.pdf

National Center for Biotechnology Information. (2019). PNAS Article. Retrieved from
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6452673/pdf/pnas.201900949.pdf

Ng, M., Khoo, M., Haridas, G., & Toh, J. T. (2023, May). Generative AI in the Philippines: Challenges and

Opportunities. Access Partnership. Retrieved from   https://accesspartnership.com/wp-
content/uploads/2023/05/Micr_GenAI_-Philippines_FINAL_230529.pdf

Organisation for Economic Co-operation and Development (OECD). 2023. “OECD Employment Outlook 2023:

Artificial Intelligence and the Labour Market.” Paris, France.

Philippine Institute for Development Studies. (2023). Electricity Supply Interruptions in the Philippines:

Characteristics, Trends, Causes. Retrieved from https://www.pids.gov.ph/publication/discussion-
papers/electricity-supply-interruptions-in-the-philippines-characteristics-trends-causes

Philippine Journal of Labor and Industrial Relations, Volume 33. (2015). Retrieved from

https://journals.upd.edu.ph/index.php/pjlir/article/view/7256/6319

Pizzinelli, C., Panton, A.J., Tavares, M.M.M., Cazzaniga, M. and Li, L., 2023. Labor market exposure to AI:

Cross-country differences and distributional implications. International Monetary Fund.

Standard Chartered – ChatGPT Impact on Labor Markets. (2023). Retrieved from

https://research.sc.com/research/api/application/protected/rp/api/data/render/241545

The Philippine IT-BPM Industry Roadmap 2028. (2022). Retrieved from https://www.ibpap.org/knowledge-hub

Webb, M. 2020. “The Impact of Artificial Intelligence on the Labor Market.” Stanford University Working Paper,

Stanford, CA.

World Bank. 2024a. “Who on Earth Is Using Generative AI?” World Bank Publication. Retrieved from

https://openknowledge.worldbank.org/entities/publication/5a876bd0-f85a-479b-ae32-cf0b7f33792f

World Bank. 2024b. World Bank East Asia and the Pacific Economic Update, October 2024: Jobs and

Technology. Washington, DC: World Bank

World Economic Forum. (2023). The Future of Jobs Report 2023. Retrieved from

https://www.weforum.org/publications/the-future-of-jobs-report-2023/digest/

Yim, I.H.Y., Su, J. Artificial intelligence (AI) learning tools in K-12 education: A scoping review. J. Comput.
Educ. (2024).

INTERNATIONAL MONETARY FUND

27

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Appendix

Figure 11. AI Exposure by Occupation, Gender, and Education

INTERNATIONAL MONETARY FUND

28

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Figure 12. Exposure and Complementary by Activity within Services

INTERNATIONAL MONETARY FUND

29

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Figure 13. Exposure and Complementary by Type of Worker

Cross-country comparison

Comparing the results for the Philippines with peer countries in the region is possible though a few caveats
apply. To compute exposure and complementarity shares for other Asian economies, we use data on
employment by occupation from the International Labor Organization (ILO)26. This dataset contains aggregated
data submitted by country authorities. Occupations are captured at the 2-digit level (43 different occupations)
and therefore less granular and less accurate than the data for Philippines used in this paper which captured
occupations at the 4-digit level (436 different occupations). Table 2 shows that the Philippine labor force
exhibits a total exposure that is higher than other Asian EMDEs but not as high as Asia’s advanced economies.

Comparing the shares computed using ILO vs PSA data for the Philippines in table 2 shows that having access
to granular data matters mostly for the complementarity angle. In other words, the additional granularity helps
in breaking down the ISCO-08 major groups which are highly heterogeneous in terms of AI exposure such as
services and sales workers (Figures 7, 12). As a result, results for the Philippines and its peers in the region
along this dimension are difficult to compare.

26 The reader may also refer to box I in the chapter 2 of the Fall 2024 IMF Regional Economic Outlook for Asia and the Pacific.

INTERNATIONAL MONETARY FUND

30

IMF WORKING PAPERS

Artificial Intelligence and the Philippine Labor Market: Mapping Occupational Exposure and
Complementarity

Table 2. AI Exposure and Complementarity in Philippines and Asia

Exposure  Complementarity

Example Occupation Titles

Share
(PHL)

Share (other
Asian EMDEs)

Share
(Asian AEs)

High

High

General and Operations Managers, First-Line
Supervisors, Teachers and Teaching
Assistants, Lawyers, Civil Engineers,
Counselors

ILO: 10%
PSA: 22%

9%

24%

High

Low

Low

n/a

Customer Service Representatives,
Telemarketers, Accountants, Auditors,
Secretaries, Administrative Clerks

Farmworkers, Construction Laborers,
Janitors, Maids and Cleaners, Waiters,
Textile workers, Food Preparation Workers

ILO: 27%
PSA: 14%

ILO: 63%
PSA: 64%

18%

26%

73%

50%

Sample includes AE = AUS, SGP, JPN; EMDE = BGD, BRN, BTN, IDN, IND, KHM, KIR, LAO, LKA, MDV, MNG, PHL, PNG, THA,
TLS, TUV, VNM, WSM.

INTERNATIONAL MONETARY FUND

31

The Impact of Artificial Intelligence on the Labor Market in the Philippines

Working Paper No. WP/2025/043

