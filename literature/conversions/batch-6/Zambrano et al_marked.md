---
conversion_metadata:
  converted_at: "2026-07-21T10:03:52Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Zambrano et al.pdf"
  source_pdf_sha256: "cfda874ab67e53750be59cb4de3eb782c11d3920cfdc722061d7a737334654da"
  page_count: 12
  markdown_char_count: 144732
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

World Development Sustainability 3 (2023) 100081

Contents lists available at ScienceDirect

World Development Sustainability

journal homepage: www.elsevier.com/locate/wds

Rotating savings and credit associations: A scoping review

Andres Felipe Zambrano a , ∗ , Luis Felipe Giraldo b , Monica Tatiana Perdomo c , 
Iván Darío Hernández d , Jesús María Godoy e 
a 
Graduate School of Education, University of Pennsylvania, Philadelphia, 19104, United States 
b 
Department of Biomedical Engineering and Department of Electrical and Electronic Engineering, Universidad de los Andes, Bogota, 111711, Colombia 
c 
Department of Psychology, Universidad de Ibague, Ibague, 730002, Colombia 
d 
Department of Economics, Universidad de Ibague, Ibague, 730002, Colombia 
e 
International Bussiness Administration, Universidad de Ibague, Ibague, 730002, Colombia

a r t i c l e

i n f o

a b s t r a c t

Keywords: 
ROSCA 
Informal ﬁnance 
Resilience 
Social capital 
Inclusive economy 
Microﬁnance

A Rotating Savings and Credit Association (ROSCA) is an informal cooperation strategy that has emerged in sev- 
eral parts of the world as a tool to increase the resilience and social development of individuals in underprivileged 
communities. This strategy has been widely studied for decades to recognize ROSCAs’ beneﬁts, risks, and opera- 
tion rules in several regions and countries. In this study, we conducted a scoping review using the PRISMA-ScR 
protocol to determine the most important recent ﬁndings about ROSCAs. First, we analyzed the location of the 
community being studied, methodological approaches, and most common keywords of the 96 articles included 
in the review. Second, we discussed the most signiﬁcant conclusions of each article on topics such as the origin, 
participants, beneﬁts, risks, operation, penalties, and structure of ROSCAs. Based on this review, we discuss how 
ROSCAs have provided beneﬁts to their members that are not exclusively ﬁnancial, how these schemes have 
evolved from traditional ones to strategies with improved structure, rules, and technological tools, and some key 
research opportunities to be addressed.

1. Introduction

Informal ﬁnancial cooperation strategies have emerged in several 
parts of the world to increase the resilience of low-income communi- 
ties by promoting cooperation between their members [84,89] . One of 
the most representative examples of this type of strategy is the Rotating 
Savings and Credit Associations (ROSCAs) [23,24,38,68,69] . ROSCAs 
are an agreement between some individuals to cooperatively save a pot 
of capital by paying a fee each week or month [16] . ROSCAs vary signif- 
icantly in terms of the number of members, frequency of contribution, 
amount of the contribution, and the process for allocating the pot [13] . 
ROSCAs can be classiﬁed into three primary types depending on the 
strategy used to allocate the pot: random, ﬁxed, and bidding. In random 
ROSCAs, the order of receiving the pot is randomly determined at the be- 
ginning of each cycle (the period required for all members to receive the 
pot once) [11] . In ﬁxed ROSCAs, the order remains ﬁxed across cycles 
[13] . Finally, in bidding ROSCAs, the ﬁrst turns are assigned to members 
who pay or contribute more to the pot for receiving these initial turns 
[54] . Regardless of the strategy to deﬁne their turns, all types of ROSCAs 
allow individuals to access some ﬁnancial services and even social and

cultural beneﬁts that formal institutions do not provide, typically to low- 
income communities without a positive credit score [69,89] .

ROSCAs have represented an alternative to formal ﬁnancial insti- 
tutions. They have inspired banks and credit unions for individuals in 
poverty situations that require help for credit alleviation or for mak- 
ing aﬀordable a new productive activity to increase their well-being. 
One of the most successful examples that ROSCAs have inspired is the 
Grameen Bank [45] . The Grameen Bank was founded in 1976 as a re- 
search project with the primary goal of providing ﬁnancial assistance 
to rural communities in Bangladesh [45] . This project showed a posi- 
tive impact on the socioeconomic life of their participants. Therefore, 
motivated by the positive contributions of the Grameen bank in several 
aspects that transcend ﬁnancial life, several researchers and communi- 
ties have adopted ROSCAs idea to replicate similar projects worldwide 
to mitigate poverty, mainly in places where formal banking is not an 
option [110] .

Each ROSCA implementation results from the context of the place 
where it is replicated. Due to the emergence of ROSCAs in several parts 
of the world, ROSCAs from each country usually have diﬀerent struc- 
tures, rules, and beneﬁts. For example, ROSCAs from Kenya [78] , Japan 
[76] , and the United States [55] have signiﬁcant diﬀerences in terms of

∗

Corresponding author. 
E-mail addresses: azamb13@upenn.edu (A.F. Zambrano), lf.giraldo404@uniandes.edu.co (L.F. Giraldo), tatiana.perdomo@unibague.edu.co (M.T. Perdomo),

ivan.hernandez@unibague.edu.co (I.D. Hernández), jesus.godoy@unibague.edu.co (J.M. Godoy) .

https://doi.org/10.1016/j.wds.2023.100081 
Received 28 September 2022; Received in revised form 25 April 2023; Accepted 31 May 2023 
2772-655X/© 2023 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ )

---

<!-- PAGE 2 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

the number of participants, the pot allocation strategy, the periodicity 
of the fee payment, and the non-monetary beneﬁts due to their culture, 
tradition, needs and particular legislation of each country. Although 
research before 2000 has focused on many of the aspects of ROSCAs 
mentioned above [3,16,23,69,110] , many researchers have recently ex- 
plored case studies to identify the particular characteristics, beneﬁts, 
and challenges of ROSCAs all over the world. Moreover, the new tech- 
nological developments have allowed researchers to analyze ROSCAs 
from a theoretical perspective by employing mathematical models and 
simulations. These diﬀerences in the methodological approaches and lo- 
cations for ROSCAs have increased the number of publications studying 
them in recent years. However, as far as we know, no literature review 
has conducted a systematic analysis of the most important ﬁndings of 
these studies. For this reason, we conducted a scoping review to compile 
the analysis and conclusions of research on this topic during the last 22 
years.

We used the Preferred Reporting Items for Systematic Reviews and 
Meta-analysis Protocol extension for Scoping Reviews (PRISMA-ScR) 
[98] to conduct a systematic map of ROSCAs research since 2000. Based 
on this map, we identiﬁed which continents and countries have been 
widely investigated in previous ROSCAs research and where there are 
opportunities to conduct such studies. After that, we analyzed the most 
common keywords of the studies, the co-occurrence of these keywords, 
and the most common methodological approaches to recognize which 
topics and how they have been analyzed. Then, we provide the most 
important ﬁndings of the articles included in the review, discussing top- 
ics such as origin, participants, beneﬁts, risks, operation, penalties, and 
structure of ROSCAs. Moreover, we show some technological applica- 
tions that have emerged in the last years to analyze and support the 
functioning of ROSCAs. We ended this review with some conclusions 
and future directions in this research area.

2. Materials and methods

Our protocol was drafted using PRISMA-ScR [98] . We searched arti- 
cles available on the Scopus and Web of Science bibliographic databases 
to identify potentially relevant documents. The papers included in this 
review must analyze, study, or model Rotation Savings and Credit Asso- 
ciations (ROSCAs). We only considered peer-reviewed journal or confer- 
ence papers published between January 2000 to July 2022 and written 
in English. The ﬁnal search strategy, deﬁned by team discussion, can be 
found in Appendix A . To consider diﬀerent aspects of ROSCAs, we in- 
cluded studies that used qualitative, quantitative, and mixed methods to

analyze ROSCAs in real communities and studies that use mathematical, 
econometric, and computational tools to model these types of associa- 
tions. We excluded papers that did not ﬁt into the conceptual framework 
of the review or were not focused on ROSCAs. Finally, we also excluded 
book chapters, book or conference introductions, and opinion articles 
without clear and supported contributions.

To increase consistency among the authors of this review, we all 
screened the titles of the 227 publications that resulted from our search 
strategy. During this process, we excluded 104 papers whose title refers 
to a diﬀerent area of knowledge or discipline. Then, all of us revised the 
abstract of each of the remaining 123 articles and decided to exclude 15 
papers. We did not ﬁnd retrieval from one of the remaining 108 papers. 
Finally, we evaluated the full text of the retrieved 107 articles and de- 
cided to include 96 based on the previously described criteria. The ﬂow 
diagram of this search is shown in Fig. A.1 . We extracted their keywords, 
published year, continent, and country of origin of the analyzed ROSCA, 
methodological approaches, and most important conclusions for each se- 
lected paper. We analyzed all keywords to group similar keywords into 
just one. For example, the words Save, Saving , and Savings were grouped 
in the concept Saving . Similarly, the words Women empowerment and Fe- 
male empowerment were grouped in the same concept. We decided this 
to provide a more accurate analysis of the co-occurrence of keywords 
and the content of the selected articles. We resolved disagreements on 
all of these steps by consensus and discussion with other reviewers if 
needed.

3. Publication trends since 2000

In this section, we ﬁrst analyze the location of ROSCAs investigated 
in the studies included in this review. For each year since 2000, we 
show the number of papers that studied ROSCAs from each continent. 
Then, we present the methodological approaches used in these studies, 
including the evolution in the number of articles that have used these 
approaches since 2000. Finally, we show the most common concepts 
included in the keywords of the studies and the co-occurrences of these 
concepts among the articles.

3.1. Continent and country of origin

For each article included in this review, we determined the country 
and continent where its data was collected. Figs. 1 and 2 show the num- 
ber of papers per continent and country, respectively. Some studies do 
not use real-world data and employed theoretical approaches based on

Fig. 1. Continent of data collection. Number of studies investigating ROSCAs 
from each continent.

2

---

<!-- PAGE 3 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Fig. 2. Country of data collection. Number of studies investigating 
ROSCAs from each countries.

Fig. 3. Published year and continent of studied ROSCAs. Number 
of papers published between January 2000 and July 2022 consid- 
ering the continent of the analyzed ROSCA.

previous ﬁndings. These studies are classiﬁed in the category None in 
the ﬁgures. Fig. 2 also includes a category called Others to refer to those 
countries studied only in one article.

Asia and Africa are the continents where most studies have collected 
their data. As mentioned in the Discussion section, one of the most 
important motivations to participate in ROSCAs is the limited access 
to ﬁnancial support from formal institutions such as banks. Therefore, 
ROSCAs are common in countries where the poverty index is high [106] . 
Research that uses data from developed countries also focuses on under- 
privileged communities such as migrants, mainly the studies from North 
America [47,48,74] and Europe [17,26] . We only found one study that 
used data from the Caribbean [97] and two that used data from Mex- 
ico [71,80] since 2000. Moreover, we did not ﬁnd any articles that 
used data from South America and Oceania. However, ROSCAs from 
Bolivia have been also studied in some works [2,3,30] , and Colombian 
researchers have also studied ROSCAs from a theoretical and computa- 
tional approach [113,114] .

Fig. 3 shows the number of publications for each year since 2000. 
The number of articles that use data from each continent for every year

was included. Between 2016 and 2019 seems to be an increasing trend 
in the published papers. However, this tendency stopped for the last 
three years, probably due to the eﬀects of pandemics that reduced the 
possibility of interacting with ROSCAs members and acquiring data from 
real scenarios. This hypothesis is also analyzed in the Methodological 
approaches section.

3.2. Methodological approaches

Since  2000,  the  studies  have  used  diﬀerent  methodological  ap- 
proaches depending on the particular objectives of the authors. Fig. 4 
shows the number of published articles that have used each of these 
approaches to analyze ROSCAs. Interviews and surveys are the most 
common approaches for acquiring data from particular case studies 
[42,53,65] . Using this data, authors tend to provide an analysis using de- 
scriptive statistics methods, including central tendency and dispersion 
measurements, and applying statistical hypothesis testing [25,40,62] . 
Other approaches for analyzing case studies are theoretical and histori- 
cal reviews. These works use methods employed in systematic or scoping

3

---

<!-- PAGE 4 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Fig. 4. Methodological approaches. Number of papers that uses each method- 
ological approaches employed for studying ROSCAs.

reviews to explore particular research questions about the evolution of 
ROSCAs in speciﬁc regions or countries. In those cases, the authors do 
not acquire their data and use data or ﬁndings from previous studies to 
provide a similar analysis to those with their own data.

Mathematical models have also been used to analyze ROSCAs. These 
mathematical models are developed using data from real ROSCAs to 
provide helpful conclusions about these schemes and their participants. 
These studies use surveys or previously acquired data to create Probit, 
Logit, or other regression models and test hypothesis based on the pa- 
rameters of the models [1,7,14,18,32,87] . Theoretical models from eco- 
nomics, such as utility functions [8,28,81,89] and econometric models 
[70] have also been used to provide a similar analysis. From this per- 
spective, studies tend to use the rationale formulated by previous ﬁnd- 
ings for their models. Moreover, some of these studies compared their 
models with data from real scenarios [89] .

Technological advances have enabled the use of other approaches 
that require the use of computing resources. Some hypotheses and sce- 
narios require months or years of data acquisition to be tested and ana- 
lyzed. Computational models and multi-agent simulations have emerged 
as an alternative for this type of analysis [51,61,92,107,108] . These 
models employ theoretical concepts of control systems and game theory 
to propose possible interventions for real ROSCAs [37,73,111] . Also, 
web applications have been developed to support the operation and 
maintenance of real ROSCAs. Finally, social experiments have been con- 
ducted to analyze the behavior of human beings. These experiments of- 
fer useful ﬁndings on trust, reputation, altruism, and other concepts of 
social theory in ROSCAs [35,60] .

Fig. 5 shows the evolution of the use of these approaches since 2000. 
Interviews, surveys, and models based on data from real scenarios have 
been the most common approaches until 2020. However, during the 
last three years, the number of studies that use these approaches has de- 
creased. Pandemic restrictions would explain this decrease. During these 
years, access to communities has been limited. Therefore, other theo-

retical approaches, such as reviews, and economic and computational 
models, have prevailed. Moreover, the number of studies that employ 
computational tools has also been increasing in the last few years.

3.3. Keywords analysis

Keywords occurrence can give an idea of what topics are being an- 
alyzed more in articles about ROSCAs since 2000. However, counting 
the occurrence of keywords without analyzing the concept behind them 
can bias the analysis. For example, although immigrants and migrants are 
diﬀerent words, both refer to the same concept. Similarly, when com- 
paring keywords such as Informal savings and Mutual-saved money , three 
concepts are recognized. The concept Informal and Mutual are particular 
for each keyword, but they also have a common concept which is Sav- 
ings . Therefore, we change the focus from keywords to concepts. To do 
this, we considered the root or the concept behind each word in each 
keyword and then split all keywords and counted the occurrence and 
co-occurrence of each concept among all papers. We also considered 
the country and continent of ROSCAs being studied as a concept be- 
cause many articles included them as keywords. This process was made 
manually without employing any additional software to avoid mistakes 
in interpreting each keyword’s roots or in splitting the keywords with 
more than one word. To increase consistency, we all screened the key- 
words of the selected publications and evaluated the concepts described 
by each keyword. These are the concepts employed for the occurrence 
and co-occurrence analysis.

Fig. 6 shows the number of occurrences of all the concepts that ap- 
pear in the keywords of at least ﬁve studies. As was expected, ROSCA 
is the most repeated concept in keywords. However, only 65 of the 96 
articles included it as a keyword. Other common concepts that appear 
signiﬁcantly in keywords of articles are related to ﬁnance and econ- 
omy. Concepts such as Finance, Micro, Small, Enterprise, Credit, Savings, 
Banking, Management , and Market show that authors are researching the

4

---

<!-- PAGE 5 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Fig. 5. Published year. Number of papers published between January 
2000 and July 2022 considering the methodological approach of each 
study.

Fig. 6. Number of occurrences of most common 
keywords. A threshold of at least 5 occurrences was 
applied.

usage and performance of ROSCAs as alternatives to formal banking to 
provide some type of economic beneﬁt to their members, such as cred- 
its to start or invest in a micro-small enterprise, or a mechanism to save 
for uncertain negative events in the future [32,47,51,86,89,103–105] . 
The continents and countries also appear commonly in keywords. For 
this reason, Asia, Africa, Kenya, India, Japan, and other continents and 
countries that have been widely studied according to Figs. 1 and 2 also 
appear in Fig. 6 . Finally, some concepts that are not directly related to 
ﬁnance, such as Social, Informal, Women, Behavior , and Rural , are also 
common in the studies.

To consider the relation between these concepts, we plotted a net- 
work shown in Fig. 7 that considers the occurrence and co-occurrence 
of the concepts. Each node of the graph represents the number of occur-

rences of the concept in the keywords among all papers. Each arc repre- 
sents the number of co-occurrences of two concepts in the same article 
among all studies. We deﬁned a minimum threshold of ﬁve occurrences 
and ﬁve co-occurrences to be included in the graph. The strongest con- 
nections in the plot occur between ROSCAs, ﬁnancial concepts, and the 
two continents with the highest amount of studies. This graph shows 
a relation between ROSCAs and micro, small, and medium enterprises 
because of the importance of ROSCAs to ﬁnance entrepreneurs. Lastly, 
there is also an interesting relation between the concepts of Social, Cap- 
ital, Women , and Immigrants . These relations show that several articles 
focus on the social groups who participate in ROSCAs, their motiva- 
tions, behavior in the association, and the non-ﬁnancial beneﬁt that 
these individuals would obtain as social, health, or cultural capital

5

---

<!-- PAGE 6 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Fig. 7. Keywords Occurrences and Co-occurrences. A threshold of at least 5 occurrences and co-occurrences was applied.

[48,53,63,65,74] . In the discussion section, we deeply analyze the com- 
mon ﬁndings of the studies included in this review.

4. Findings and contributions of publications since 2000

We identiﬁed 96 papers addressing studies on ROSCAs between 2000 
and 2022 to include in this scoping review. These articles study char- 
acteristics such as the origin of ROSCAs, their participants, beneﬁts, 
motivations, and behavior of their members, and mechanisms of op- 
eration and control that have been used by real ROSCAs. Moreover, 
other articles have also found and proposed alternatives to improve the 
economic performance and wellness of the ROSCAs and their members 
through mathematical and computational models and technological ap- 
plications. In this section, we discussed these ﬁndings. To organize the 
most relevant ﬁndings of these articles, we grouped them into ﬁve cat- 
egories. These categories are not exclusive. Therefore, those articles 
whose contributions go beyond one speciﬁc category are discussed in 
more than one section.

4.1. Origin, participants and beneﬁts of ROSCAs

As it is shown in Figs. 1 and 2 , ROSCAs have emerged in several 
parts of the world. Associations in one continent are not necessarily the 
consequence of another ROSCA from a diﬀerent place, and the causes of 
their consolidation can vary from one case to another. The most recog- 
nized motivation for creating a ROSCA is the limited access to ﬁnancial 
services for several people from diﬀerent types of social groups [1,91] . 
Although this issue can be common for low-income communities be- 
cause of a low credit score, migrants and women also have social and 
cultural barriers to accessing ﬁnancial services from formal institutions 
such as banks [46,99] or even borrowing money from their neighbors 
[50] . Therefore, ROSCAs have emerged as a mechanism that can give 
these communities access to credits, looking for ﬁnancing for education 
and health services [31,78,109] , vehicles, housing, lands, livestock, and 
other means of production [15,28,48,93] , or non-capital goods and so- 
cial and cultural events [65] .

ROSCAs are also used as mechanisms to save money periodically 
[38] . Women have stated that having the discipline to save money and 
avoid spending it on non-capital goods would be diﬃcult [17] . Self- 
control is not only a problem for women. Men have shown lower dis- 
cipline saving than women [99] . In several cases, women are mainly 
motivated to participate in ROSCAs to attenuate the self-control prob-

lems of their husbands [9] . Several studies have shown that individuals 
from diﬀerent social groups and demographics recognize their discipline 
problems to save money [25,41,86] . Therefore, many individuals par- 
ticipate in ROSCAs looking for a mechanism to force themselves to save 
and reduce expenses because of the social pressure and the embarrass- 
ment that can imply a non-payment or a defection [34,36,49,94] . They 
visualize ROSCAs as an opportunity to eﬀectively save money, increas- 
ing their resilience for future uncertain negative events and allowing 
them to have the capital to invest in the future [6,8,25,41,73] .

This desire to increase and improve their investing opportunities is 
also an important motivation for consolidating informal associations. Al- 
though ROSCAs are common in underprivileged and underrepresented 
communities, many entrepreneurs from micro, small, and medium en- 
terprises also use ROSCAs as alternatives to formal ﬁnancing institutions 
[5,22,27,32,52] . Some members of ROSCAs also can obtain credits from 
banks but prefer informal associations because of the lower or null inter- 
est rates [22,34,43,88,90,93,103–105] and the ﬂexibility of the usage of 
the credits [44] , instead of having excessive restrictions and debts with 
banks that they consider diﬃcult to pay because of the high interests 
[26] . Although individuals of high income prefer formal institutions to 
save and invest their money [21] , the participation of medium-income 
individuals in ROSCAs is higher than individuals with low income [56] . 
In some cases, participants of ROSCAs have also recognized that they 
consider banks corrupted and non-transparent institutions [55] . There- 
fore, no matter the interest rates, they trust informal associations more 
and prefer this ﬁnancing option.

Based on this preference of some entrepreneurs for ROSCAs, several 
works have modeled the possible impact of ROSCAs on entrepreneurs 
showing positive economic results [82,83] . Higher economic growth 
and lower poverty rates of members of ROSCAs have been observed in 
real scenarios around the world [7,27,39] . This positive economic im- 
pact on participants of informal associations, including those who can 
access formal institutions, shows the viability and the importance of the 
coexistence of diﬀerent types of ﬁnancial institutions to oﬀer the ser- 
vices that people from diﬀerent demographics require.

Lastly, ﬁnancial services are not the unique motivation for ROSCAs 
members. In some cases, the creation of social capital is more important 
than the economic beneﬁt that members would receive [15,76,95,109] . 
Some of them believe that informal associations are an opportunity to 
meet new people who can be helpful for career development or future 
business or to increase their social status [1,91] . In other cases, mainly 
for women, migrants, and other underrepresented groups, ROSCAs are

6

---

<!-- PAGE 7 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

an empowerment tool that helps them meet people with similar ideas, 
habits, and cultures, consolidating links and friendships that transcend 
the professional and economic ﬁeld [17,53,64,89] . Women and mi- 
grants have recognized that ROSCAs help them to feel welcomed and 
respected by others who are similar to them [74] and, in the case of im- 
migrants, who preserve the same ancestral traditions [97] . This social 
capital has also shown a beneﬁcial impact on the physical and psycho- 
logical health of ROSCAs members. For example, Mujin participation in 
Japan is correlated to a reduction in the decrease of the functional ca- 
pacity of elderly people [62,63,87] . These studies have shown that the 
positive impact of ROSCAs on health occurs for those participants who 
are not only interested in the economic beneﬁt. Therefore, social capital 
and its positive implications are also substantial beneﬁts of ROSCAs that 
the formal banking system cannot oﬀer.

4.2. Operation and control

Although all ROSCAs share similar characteristics, such as the peri- 
odical fee and the allocation of a percentage of the pot to each member, 
each ROSCA has its peculiarities that directly impact the performance 
of the association. Some characteristics such as the order of the pot al- 
location, structure, number of participants, roles, connectivity and in- 
teractions between members, amount of the fee, and control strategies 
are fundamental for the success of the scheme [72,85] .

Usually, ROSCAs have a horizontal structure where all members can 
participate in most decisions. However, the leader and other members 
with relevant roles tend to be more inﬂuential on the most important 
decisions of the association. Therefore, the ethics of these members are 
crucial for the correct functioning of the association [42] . One of these 
decisions is the order of the pot allocation, which would be decisive for 
the particular actions of each member of the scheme. The traditional 
method to assign this order is by a random selection at the beginning 
of the process [73] . During the ﬁrst meeting, individuals usually know 
when they will receive the pot. In several cases, the leader, the mem- 
bers with important roles, and their closest friends or guests received 
the ﬁrst turns because of their inﬂuence, while the random selection is 
applied only for the remaining turns [14] . In other cases, the ﬁrst turns 
are assigned to those members who decide to pay more for these turns 
[54] . This type of association, called Auction or Bidding ROSCA, helps 
those members who need the money for an investment, such as start- 
ing a micro-small enterprise, or for any particular reason to be the ﬁrst 
to receive the pot. In this way, members who would beneﬁt more from 
receiving the pot earlier are prioritized if they can pay for it. However, 
some individuals would need the pot early to pay debts and cannot pay 
for receiving it before others. To help them, in some cases, members of 
the ROSCA agree to assign the order based on the needs of each partic- 
ipant, giving priority to those with higher needs [17] .

ROSCAs participants do not necessarily prefer the ﬁrst turns [13] . 
Individuals with higher incomes and women tend to be more patient 
and accept later turns [18] . Some ROSCAs agree to wait until the end 
of the process to divide the total pot among all contributing members 
without assigning an order for the pot allocation [96] . Although this 
would not be optimal considering the value of money over time, some 
members prefer it to avoid the temptation of spending the pot if they 
receive it early or just the negative perception of owing money to the 
others [6] . In summary, the order of the pot allocation is always based 
on the particular interests and sense of justice of the members who desire 
to maximize their income, diversify the risks and help those with more 
needs [67] .

Another important decision in ROSCAs is the admission of new mem- 
bers. This decision is mainly inﬂuenced by the social circle of the per- 
son who desires to participate [93] . In several cases, ROSCAs only admit 
new members if they have been suggested by older members, looking for 
higher trustworthiness of the scheme [12] . With this admission method- 
ology, recommenders will pay for the credit defaults of their guests. 
Another common selection criterion is the income of the candidates.

If they cannot demonstrate regular incomes or a minimum level of in- 
come, ROSCAs exclude them because of the risk of defaults in the fees 
[21,75,93] . This rule justiﬁes that, in some cases, individuals of middle 
income participate more in these schemes than individuals from low- 
income communities. This evidence reframes the initial motivation for 
using ROSCAs only as an alternative for low-income communities who 
cannot access formal ﬁnancial institutions because, in several cases, they 
cannot access informal schemes either.

ROSCAs participants tend to trust other members, mainly in small as- 
sociations. However, in schemes with more members, participants pre- 
fer to use signed contracts, registering of contributions, identiﬁcation 
cards, and other strategies that do not depend on the social relations of 
the members [112] . To punish the defaults, ROSCAs use heavy economic 
penalties, disqualiﬁcation to receive the pot, social sanctions, and exclu- 
sion of social and cultural events [10,60,61,112] . The economic penal- 
ties, added to the small interest rates, sometimes provide a surplus in 
the pot after all the turns. This surplus is employed for the common ben- 
eﬁt of the community. On some occasions, this money is divided among 
all the members. In other cases, the members who actively participate 
by asking for credits and paying higher fees also demand to receive a 
higher percentage of the pot surplus [67] . Finally, from a theoretical and 
mathematical perspective, it has been argued that in the absence of an 
external (social) sanctioning mechanism, ROSCAs are never sustainable, 
even if the defecting member is excluded from all future ROSCAs. [10] . 
However, other theoretical models have shown that some associations 
can be immune to defection without social sanctions if the number of re- 
sources lost because of the default is small enough to avoid a reduction 
in the motivation of their members [81] . This result shows the impor- 
tance of trust and motivation. In real scenarios, many participants trust 
their ROSCAs because of the requirements to become a member and the 
strategies to minimize defections [112] . However, informal associations 
have some risks and disadvantages that would diminish motivation and 
cause a negative impact on their members.

4.3. Risks and disadvantages

Although ROSCAs are resilient to the loss of money, the loss of mo- 
tivation of the members would be the immediate cause of ROSCAs’ fail- 
ures. This loss of motivation can result from the default of any of the 
members or discontent with the rules, roles, or transparency of the asso- 
ciation [4,60,95,99,115] . For this reason, the ethics and behavior of the 
members, mainly the leader, is vital for the scheme’s success. However, 
there are also other risk factors in ROSCAs, even in scenarios where 
all individuals desire to cooperate. In some cases, mainly in bidding 
ROSCAs, individuals would be tempted to pay an excessive fee or ac- 
cept high-interest rates to obtain an early turn [14,54] . This situation 
would be aggravated due to the impatience of some members who are 
reluctant to wait several months [19] . If fees or rates are excessive, some 
participants will fall into diﬃculty paying debts, forcing them to default 
and reducing the motivation of the other members.

The reduced ﬁnancial knowledge of several members and the low in- 
tervention of the government due to the informal nature of the associa- 
tions would worsen this negative situation [20] . These reduced ﬁnancial 
skills can also motivate the transition to Ponzi schemes because of the 
desire of the members to obtain immediate and higher rewards [116] . 
These schemes are unsustainable because, at some point, new members 
will not receive back the money they contributed. After all, this money 
is employed to pay the proﬁt of older participants, and later contribu- 
tions would not be enough. Therefore, this transition and the lack of 
ﬁnancial skills exacerbate the risk for ROSCAs members.

In some cases, participants will be trustworthy and have a minimum 
ﬁnancial education to avoid unsustainable decisions. However, some in- 
trinsic characteristics of ROSCAs can also be a disadvantage compared 
to formal institutions. Many ROSCAs are conformed by members that do 
not have regular incomes [50] . Therefore, even if individuals want to 
contribute to the association, they would not be able to pay their fees for

7

---

<!-- PAGE 8 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

some months. Moreover, the maximum pot is the sum of the particular 
contributions of each member. This amount of money is considerably 
less than the amount of money that a bank would have. For this reason, 
if some individual needs a credit higher than the total pot, the beneﬁt 
received from the ROSCA would not be enough [75] . Finally, if the as- 
sociations do not charge an interest fee or invest the pot to get an extra 
return, the members would be losing money over time because of the 
inﬂation of countries and the evolution of the value of money [88] .

Lastly, exogenous factors such as natural disasters, thefts, health is- 
sues, and even the death of a member, and economic issues of the region 
or country of associations would also be a risk to their success [4,70] . 
However, when a loss of money happens due to an exogenous cause, 
ROSCAs tend to evolve and be more resilient compared to those scenar- 
ios where the cause of the loss was a defection of a member [34,70] . 
As we mentioned before, the motivation to cooperate is the most rel- 
evant factor for the scheme’s success. When the cause of the loss is a 
defection, the decrease in motivation is higher, and the probability of 
failure of the ROSCAs increases [56] . For this reason, it is crucial to 
maintain the members motivated and committed to the success of all 
the participants.

4.4. Improvement of economic performance and wellness

Many studies have modeled ROSCAs to identify alternatives to im- 
prove their economic performance and the wellness of all their members 
[16] . These works have included concepts such as altruism, reciprocity, 
and reputation to ﬁnd helpful insights to improve real ROSCAs. One of 
the most relevant ﬁndings of these works is the importance of reciprocity 
and altruism for the correct operation of traditional ROSCAs [60] . When 
individuals are more willing to contribute to others and are also mo- 
tivated by the contributions of others, ROSCAs tend to be successful 
and provide economic development to their members [59,61,92,107] . 
Several social experiments have also demonstrated that members of 
ROSCAs usually have high levels of reciprocity and altruism [35,60] . 
Therefore, a strategy to potentially improve the performance of ROSCAs 
is to maintain and enforce these behaviors between members. For ex- 
ample, ROSCAs have been employed to ﬁnance the electriﬁcation of 
vulnerable communities that historically had no access to electricity ser- 
vices [29] . This type of project promotes reciprocity by beneﬁting the 
community over individual interests.

Maintaining members highly motivated is vital to deal with the de- 
fection issue. One possible solution is to improve the selection process 
of new members. Although the use of a minimum threshold of income 
has become a method to select the participants of ROSCAs, this would 
deny access to people who really need that ﬁnancial service and would 
not necessarily defect the association in the future. Therefore, through 
computational modeling analysis, it has been proposed to use reputa- 
tion to select new participants [61,113] . This selection method has been 
used by ROSCAs when requiring old members to recommend new ones 
[12,102] . On the other hand, other authors proposed to increase the 
economic and social penalties [33,61] . With this strategy, individuals 
will be more reluctant to defect to avoid these penalties and lose their 
reputation with others [34,49] . Finally, to reduce the economic impact 
of defection, it has also been proposed to increase the interest rates, 
mainly for ROSCAs with a high number of members [4] , and to use a 
cash reserve ratio that will support the losses caused by defaults [114] . 
Defections and defaults are inevitable, even in cases where all the 
individuals desire to cooperate. If individuals have to decide between 
using their capital to acquire some vital goods or continue contributing 
to the association, survival would be the decision for everyone. For this 
reason, some variations in the order of turns to reduce this situation 
would increase the resilience of the association. One possible strategy is 
giving ﬁrst turns to individuals who have higher needs. In these cases, 
if those individuals invest that beneﬁt appropriately, they would have 
more options to continue contributing in the future instead of losing 
the capacity to pay the fee of the ROSCA [17] . Another option is giving

priority to individuals with higher incomes and capital because they 
would have a higher capacity to continue contributing to others, and 
the risk of default after receiving the pot will be reduced [4,54] .

The structure can also be modiﬁed to increase the resilience of as- 
sociations and individuals. If each member participates simultaneously 
in more than one association, it would have a higher probability of re- 
ceiving a pot earlier and a lower probability of losing all the money due 
to a ROSCA’s failure. This strategy, inspired by the diversiﬁcation of 
investments to reduce the risk, is studied in [114] , showing promising 
results. Moreover, several ROSCAs members in real scenarios have been 
participating in more than one association showing economic growth 
[1,105] . Another proposal of the work in [114] is to reduce the number 
of members on each ROSCA. Small ROSCAs can force their members 
to save while reducing the probability of defection by decreasing the 
number of members. Following these proposals, participants diversify 
their contribution while reducing the number of people they depend 
on, signiﬁcantly decreasing the risk. Furthermore, although the pot will 
be lower, the waiting time until receiving it will also be lower due to the 
small number of members. This idea has also shown promising results 
in real scenarios [8] .

Lastly, a ﬁnal proposal to increase the performance of ROSCAs is the 
transition from informality to formality [31,55] . This transition would 
provide this type of association with rules such as a cash reserve ratio re- 
quirement, a maximum fee, a maximum or a minimum number of mem- 
bers, or interest rates, added to government support to reduce the risks 
of defaults and defections. However, before transitioning to formality, it 
must be analyzed if the new formal ROSCAs would have the same issues 
as banks, discouraging the participation of several social groups that the 
current informal ROSCAs contribute. Therefore, another alternative is to 
provide both options to participants and allow them to decide between 
formality, informality, or both. This option has also shown promising 
results [22] . In summary, some proposals such as diversiﬁcation, the 
coexistence of formal and informal ﬁnancial services, and the formal- 
ization or regulation of current ROSCAs should be analyzed to improve 
the beneﬁts and reduce the risks of their participants [58,77,82] .

4.5. Technological applications

Technological development has allowed new methodological ap- 
proaches to analyze and support ROSCAs. Since observing and evaluat- 
ing the performance of improvement strategies in real ROSCAs takes sig- 
niﬁcant time and eﬀort, computer tools have been proposed in research 
work to model human dynamics [4,92] . These computational models 
have been used to predict the results of applying realistic variations to 
ROSCAs [113,114] . Based on dynamic systems and multi-agent systems 
theory, the works in [61,113,114] have demonstrated the importance of 
motivating reputation and altruism and the need for decentralized struc- 
tures, diversiﬁcation of investments in ROSCAs, and a cash reserve ratio 
to increase resilience in scenarios with low trust and trustworthiness. 
Furthermore, the authors of [51] have also used agent-based models 
to explore the resilience of informal associations to disasters, showing 
the importance of carefully tailoring to local contexts. Finally, compu- 
tational models have also been used to analyze the particular actions 
of each participant of informal associations to increase their individual 
resilience [107,108] . These works have used feedback control theory to 
show that the best actions for individuals are the investment in health 
and education capital, which can represent a high return on investment 
in the future, and being altruistic with their neighbors to increase the 
probability that one of them would help them in the future if they need 
it.

Technological tools have also been used to provide ROSCAs partic- 
ipants with better control tools and allow them to participate in these 
schemes even if all the members are not geographically in the same place 
[37] . These tools help participants organize their ﬁnance, have an in- 
dividual and collective register of contributions and expenses, schedule 
reminders for future fees, and identify defaults [73,111] . In summary,

8

---

<!-- PAGE 9 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

these technological tools help ROSCAs, mainly those with a higher num- 
ber of members, to increase the security and transparency in the trans- 
actions, pot allocation, and economic decisions of members [112] .

4.6. New research directions

Although research about ROSCAs has been mainly focused on spe- 
ciﬁc communities around the world employing several methodological 
approaches, the interest of researchers is still highly concentrated in 
Asia and Africa. Before 2000, [110] and [3] had shown the presence of 
ROSCAs in North and South America, respectively. However, the num- 
ber of publications that used data from America during this century has 
been lower than ten. Therefore, there is a need to continue investigat- 
ing the particularities of ROSCAs in America, mainly in South America, 
to understand how the context of a country would impact the bene- 
ﬁts, management, and limitations of these cooperative schemes. This 
research would have a signiﬁcant impact in countries such as Colom- 
bia, Venezuela, and Argentina, where several cooperative eﬀorts have 
emerged in diﬀerent social groups [66,79] , including Japanese migrant 
communities that have employed these cooperative strategies in Ar- 
gentina after World War II [57,100,101] .

Another research direction for future years is to investigate inter- 
ventions in ROSCAs looking for an improvement in the socioeconomic 
conditions of the communities that would be beneﬁted from them. As 
shown in this review, most studies have conducted a descriptive anal- 
ysis using surveys and interviews or proposed interventions based on 
mathematical and computational models. However, few studies have 
intervened in the associations to test the real impact of the proposed al- 
ternatives to improve ROSCAs. These interventions should be designed 
in agreement with the administrators and members of associations to 
understand the possible implications of these interventions that are not 
necessarily considered in mathematical models and simulations, and to 
avoid a negative impact on the community. It is critical to establish close 
communication with these organizations to implement aﬀordable inter- 
ventions that would oﬀer the desired impact on these communities and 
report the complete design and implementation experience to replicate 
this type of intervention in several parts of the world.

One of the interventions explored is using technological devices as 
control and advisory tools for administrators and members of ROSCAs. 
Further developments in control theory and artiﬁcial intelligence can 
potentially be used to recognize those patterns that would maximize 
members’ proﬁt and design ideal advisors for ROSCAs, considering pri- 
vacy and ethical issues.

5. Conclusion

This article presented a scoping review of Rotating Savings and 
Credit Associations (ROSCAs) research over the last 22 years. Asia and 
Africa were the continents with the highest amount of ROSCAs studied 
since 2000. There have been diﬀerent methodological approaches to

studying these informal associations. These approaches mainly include 
case studies that collected data through surveys and interviews and used 
descriptive statistics or developed regression models based on these data 
to analyze them. Some of the most important ﬁndings are the ability of 
ROSCAs to help their members increase their ﬁnancial wellness by forc- 
ing individuals to save money and enabling them to have better invest- 
ments. Furthermore, ROSCAs also enforce the social relations of their 
members, improving their social capital, and, in some particular groups 
such as migrants, women, and the elderly, maintain ancestral traditions, 
improve physical and psychological health, and empower them. More- 
over, some strategies, such as increasing the number of ROSCAs where 
each individual participates, reducing the fee and the number of partic- 
ipants of each ROSCA, and promoting altruism and reciprocity, would 
potentially minimize the eﬀect of defection and default.

With the recent development of technological and computational 
tools, new methodological approaches have become available. Multi- 
agent systems, feedback control theory, and machine learning models 
have been employed to analyze ROSCAs. Furthermore, these models also 
oﬀer the opportunity to test several promising strategies before applying 
them in real scenarios to recognize if they can be aﬀordable and help- 
ful for communities. Finally, web and mobile applications also become 
available to improve the transparency and security of ROSCAs, help- 
ing their members register transactions and providing investment and 
contributions advice. We consider that future research directions should 
be the observation of these associations in continents where they have 
not been widely studied and the application of these mathematical and 
technological tools to improve ROSCAs’ performance and wellness of 
their members. For these interventions, researchers should remember 
the limitations that mathematical models and technological tools have, 
the ancestral and social importance of ROSCAs to several communities, 
and the need for close communication with the communities.

Declaration of Competing Interest

The authors certify that they have NO aﬃliations with or involve- 
ment in any organization or entity with any ﬁnancial interest (such 
as honoraria; educational grants; participation in speakers’ bureaus; 
membership, employment, consultancies, stock ownership, or other eq- 
uity interest; and expert testimony or patent-licensing arrangements), 
or non-ﬁnancial interest (such as personal or professional relationships, 
aﬃliations, knowledge or beliefs) in the subject matter or materials dis- 
cussed in this manuscript.

Acknowledgments

This work was partially supported by Google through the Google 
Research Award for Latin America, and by the Universidad de los Andes 
and Universidad de Ibagué through Convocatoria Conjunta Unibagué- 
Uniandes.

9

---

<!-- PAGE 10 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Appendix A. Final Search Strategy

S1 File

Fig. A1. Identiﬁcation and screening processes followed to determine the included studies in this review.

Final search strategy. Search strategy employed to identify articles

that would be included in this review.

References

[1] J.K. Acquah, R. Dahal, Rosca s as lenders of last resort after ﬁnancial crises: lessons

from Indonesia, J Int Dev 30 (7) (2018) 1223–1239 .

[2] D.W. Adams, M.L. Canavesi, Rotating savings and credit associations in Bolivia 1, 
in: Informal Finance in Low-income Countries, Routledge, 2019, pp. 313–323 . 
[3] D.W. Adams, M.L.C. de Sahonero, Rotating savings and credit associations in bo- 
livia/les institutions informelles de crédit en bolivie (roscas), Savings and develop- 
ment (1989) 219–236 .

[4] D. Ahn, W. Kang, K.-K. Kim, H. Shin, Analysis and design of microﬁnance services:

a case of rosca, The Engineering Economist 62 (3) (2017) 197–230 .

[5] J.E. Akoten, Y. Sawada, K. Otsuka, The determinants of credit access and its impacts 
on micro and small enterprises: the case of garment producers in kenya, Econ Dev 
Cult Change 54 (4) (2006) 927–944 .

[6] M. Aliber, Rotating savings and credit associations and the pursuit of self-discipline: 
a case study in south Africa, African review of money ﬁnance and banking (2001) 
51–73 .

[7] M. Altuntas, A. Erlbeck, F. Huber, The eﬀect of rosca participation on microin- 
surance purchase, Zeitschrift für die gesamte Versicherungswissenschaft 108 (2) 
(2019) 141–163 .

[8] S. Ambec, N. Treich, Roscas as ﬁnancial agreements to cope with self-control prob-

lems, J Dev Econ 82 (1) (2007) 120–137 .

[9] S. Anderson, J.-M. Baland, The economics of roscas and intrahousehold resource

allocation, Q J Econ 117 (3) (2002) 963–995 .

[10] S.  Anderson,  J.-M.  Baland,  K.O.  Moene,  Enforcement  in  informal  saving 
groups, J Dev Econ 90 (1) (2009) 14–23, doi: 10.1016/j.jdeveco.2008.09.003 . 
https://www.sciencedirect.com/science/article/pii/S0304387808000862

[11] S. Ardener, The comparative study of rotating credit associations, The Journal of 
the Royal Anthropological Institute of Great Britain and Ireland 94 (2) (1964) 
201–229 .

[12] D. Aredo, Rotating savings and credit associations: characterization with particular 
reference to the ethiopian iqqub, Savings and Development (2004) 179–200 . 
[13] J.-M.  Baland,  C.  Guirkinger,  R.  Hartwig,  Now  or  later?  the  al- 
location  of  the  pot  and  the  insurance  motive  in  ﬁxed  roscas,  J 
Dev 
doi: 10.1016/j.jdeveco.2019.04.001 . 
https://www.sciencedirect.com/science/article/pii/S0304387818316389 
[14] J. Bauchet, V. Larsen, Rosca composition and repayment: evidence from taiwanese

(2019)

1–11,

Econ

140

bidding roscas, J Dev Stud 54 (9) (2018) 1483–1495 .

[15] C. Benda, Community rotating savings and credit associations as an agent of 
well-being: a case study from northern rwanda, Community Dev J 48 (2) (2013) 
232–247 .

[16] T. Besley, S. Coate, G. Loury, The economics of rotating savings and credit associ-

ations, Am Econ Rev (1993) 792–810 .

[17] B. Bilecen, ’alt ı n günü’: migrant women’s social protection networks, Comparative

Migration Studies 7 (1) (2019) 1–17 .

[18] J. Bonan, P. LeMay-Boucher, K. McNabb, C.C. Tomavo, Time preferences and com- 
mitment devices: evidence from roscas and funeral groups in benin, Oxford Devel- 
opment Studies 47 (3) (2019) 356–372 .

[19] J.  Bonan,  P.  LeMay-Boucher,  D.  Scott,  Can  hypothetical  measures  of  time 
preference  predict  actual  and  incentivised  behaviour?  evidence  from  sene- 
gal,  World  Dev  159  (2022)  106029,  doi: 10.1016/j.worlddev.2022.106029 . 
https://www.sciencedirect.com/science/article/pii/S0305750X22002194

10

---

<!-- PAGE 11 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

[20] M.J. Bophela, N. Khumalo, The role of stokvels in south Africa: a case of economic 
transformation of a municipality, Problems and Perspectives in Management 17 (4) 
(2019) 26 .

[21] S.B. Carpenter, R.T. Jensen, Household participation in formal and informal sav- 
ings mechanisms: evidence from pakistan, Review of Development Economics 6 
(3) (2002) 314–328 .

[22] N.S. Chiteji, Promises kept: enforcement and the role of rotating savings and credit

associations in an economy, J Int Dev 14 (4) (2002) 393–411 .

[23] J.S. Coleman, Foundations of Social Theory, Harvard University Press, 1994 . 
[24] D. Collins, J. Morduch, S. Rutherford, O. Ruthven, Portfolios of the Poor: How the

rate liberalization-a case study of wenzhou, The Chinese Economy 52 (2) (2019) 
155–170 .

[55] M. Kear, Peer lending and the subsumption of the informal, J Cult Econ 9 (3) (2016)

261–276 .

[56] A.M. Kedir, G. Ibrahim, Roscas in urban ethiopia: are the characteristics of the in- 
stitutions more important than those of members? Journal of development studies 
47 (7) (2011) 998–1016 .

[57] Minorities and diversity, K. Kimura (Ed.), Trans Paciﬁc Press, 2011 . 
[58] S. Klonner, Rotating savings and credit associations when participants are risk

averse, Int Econ Rev (Philadelphia) 44 (3) (2003) 979–1005 .

World’s Poor Live on $2 a Day, Princeton University Press, 2010 .

[59] S. Klonner, Private information and altruism in bidding roscas, The Economic Jour-

[25] O. Dagnelie, P. Lemay-Boucher, Rosca participation in benin: a commitment issue,

nal 118 (528) (2008) 775–800 .

Oxf Bull Econ Stat 74 (2) (2012) 235–252 .

[26] K. Datta, C. Aznar, The space-times of migration and debt: re-positioning migrants’ 
debt and credit practices and institutions in, and through, london, Geoforum 98 
(2019) 300–308 .

[27] R. Dekle, K. Hamada, On the development of rotating credit associations in japan,

Econ Dev Cult Change 49 (1) (2000) 77–90 .

[28] Y. Dinç, R. Jahangir, R. Nagayev, F. Çak ı r, Economics of savings-based ﬁnance: an 
interest-free model of rotating savings and credit association in turkey, Journal of 
Islamic Accounting and Business Research (2021) .

[29] B. Diouf, Tontine: self-help ﬁnancing for solar home systems, Renew Energy 90

(2016) 166–174 .

[30] S.B. Donoso, Y. Altunba ş , A. Kara, The rationale behind informal ﬁnance: evidence

from roscas in bolivia, The journal of developing areas (2011) 191–208 .

[31] N. Dube, K. Edwell, Strengthening informal social security to provide meaning- 
ful social protection: the case of stokvels in soweto, J Soc Dev Afr 33 (1) (2018) 
157–181 .

[32] B.-C. Egbide, et al., Rotating and savings credit association (RoSCAs): averitable 
tool for enhancing the performance of micro and small enterprises in nigeria, Asian 
Economic and Financial Review 10 (2) (2020) 189–199 .

[33] M. El-Gamal, M. El-Komi, D. Karlan, A. Osman, Bank-insured RoSCA for microﬁ- 
nance: experimental evidence in poor Egyptian villages, Journal of Economic Be- 
havior & Organization 103 (2014) S56–S73 .

[34] Ş . Ero ğlu, Informal ﬁnance and the urban poor: an investigation of rotating savings

[60] S. Koike, M. Nakamaru, T. Otaka, H. Shimao, K.-I. Shimomura, T. Yamato, Reci- 
procity and exclusion in informal ﬁnancial institutions: an experimental study of 
rotating savings and credit associations, PLoS ONE 13 (8) (2018) e0202878 . 
[61] S. Koike, M. Nakamaru, M. Tsujimoto, Evolution of cooperation in rotating indi-

visible goods game, J. Theor. Biol. 264 (1) (2010) 143–153 .

[62] N. Kondo, J. Minai, H. Imai, Z. Yamagata, Engagement in a cohesive group and 
higher-level functional capacity in older adults in japan: a case of the mujin, Social 
Science & Medicine 64 (11) (2007) 2311–2323 .

[63] N. Kondo, K. Suzuki, J. Minai, Z. Yamagata, Positive and negative eﬀects of ﬁ- 
nance-based social capital on incident functional disability and mortality: an 8-year 
prospective study of elderly japanese, Journal of epidemiology 22 (6) (2012) 
543–550 .

[64] M. Kshetrimayum, Rotating savings and credit associations: an important space for

social work practice, Indian J Soc Work 77 (3) (2016) 311–322 .

[65] J. Lappeman, J. Litkie, S. Bramdaw, A. Quibell, Exploring retail orientated rotat- 
ing savings and credit associations: festive season ’stokvels’ in South Africa, The 
International Review of Retail, Distribution and Consumer Research 30 (3) (2020) 
331–358 .

[66] M. Larrabure, M. Vieta, D. Schugurensky, The ’new cooperativism’in Latin Amer- 
ica: worker-recuperated enterprises and socialist production units, Studies in the 
Education of Adults 43 (2) (2011) 181–196 .

[67] M. Le Polain, O. Sterck, M. Nyssens, Interest rates in savings groups: thrift or threat?

World Dev 101 (2018) 162–172 .

and credit associations in turkey, J Soc Policy 39 (3) (2010) 461–481 .

[68] R. Leonardi, R.Y. Nanetti, R.D. Putnam, Making democracy work: Civic traditions

[35] A. Etang, D. Fielding, S. Knowles, Trust and rosca membership in rural cameroon,

in modern Italy, Princeton University Press Princeton, NJ, USA, 2001 .

J Int Dev 23 (4) (2011) 461–475 .

[36] D.M. Fessler, Windfall and socially distributed willpower: the psychocultural dy- 
namics of rotating savings and credit associations in a bengkulu village, Ethos 30 
(1–2) (2002) 25–48 .

[37] P. Francois, M. Squires, Linking mobile money networks to ”e-RoSCA ”: an experi-

mental study, Sci Adv 7 (1) (2021) eabc5831 .

[38] C. Geertz, The rotating credit association: a ”middle rung ” in development, Econ

Dev Cult Change 10 (3) (1962) 241–263 .

[39] S. Ghazali, Kut (informal rotating credit) in the livelihood strategies of urban house-

holds in penang, malaysia, Area 35 (2) (2003) 183–194 .

[40] J. Goedecke, I. Guérin, B. d’Espallier, G. Venkatasubramanian, Why do ﬁnancial 
inclusion policies fail in mobilizing savings from the poor? lessons from rural south 
india, Development Policy Review 36 (2018) O201–O219 .

[41] M.K. Gugerty, You can’t save alone: commitment in rotating savings and credit

associations in kenya, Econ Dev Cult Change 55 (2) (2007) 251–282 .

[42] S. Han, Q. Zhang, L. Liu, The risk management mechanism of China’s bidding ro- 
tating savings and credit association: a case study of chengnan village in wenzhou, 
Emerging Markets Finance and Trade 56 (13) (2020) 3095–3105 .

[43] K. Hansen, J.J. Kim, S. Suﬃan, K. Mehta, Leveraging informal lending mechanisms 
to facilitate technology transfer and microenterprise in developing countries, Tech- 
nol Soc 41 (2015) 65–75 .

[44] H.A.A.B. Hoque, M.B. Khalily, ROSCAs and ASCRAs in Bangladesh: implications 
for ﬁnancial market development, Savings and Development (2002) 395–418 . 
[45] M.  Hossain,  Credit  for  Alleviation  of  Rural  Poverty:  The  Grameen  Bank  in

Bangladesh, volume 65, Intl Food Policy Res Inst, 1988 .

[46] C.S. Hossein, Fringe banking in canada: a study of rotating savings and credit as- 
sociations (roscas) in toronto’s inner suburbs, Canadian Journal of Nonproﬁt and 
Social Economy Research 8 (1) (2017) 29 .

[47] H. Ibrahim, Do institutions matter? the persistence of ROSCAs among immigrants 
in developed economies, Journal of Enterprising Communities: People and Places 
in the Global Economy (2019) .

[48] H. Ibrahim, Structured savings and asset ownership: the role of rotating savings 
and credit associations among african immigrants in the united states, J. Soc. & 
Soc. Welfare 47 (2020) 29 .

[49] D. Imami, K. Rama, A. Polese, Informality and access to ﬁnance during socialism 
and transition–the case of the rotating savings and credit schemes, Journal of Evo- 
lutionary Economics 30 (5) (2020) 1367–1383 .

[50] S. Johnson, Gender norms in ﬁnancial markets: evidence from kenya, World Dev

32 (8) (2004) 1355–1374 .

[51] M.Y. Joshi, J. Flacke, N. Schwarz, Do microﬁnance institutes help slum-dwellers 
in coping with frequent disasters? an agent-based modelling study, Int. J. Disaster 
Risk Reduct. 49 (2020) 101627 .

[52] K. Kan, Informal capital sources and household investment: evidence from taiwan,

J Dev Econ 62 (1) (2000) 209–232 .

[53] S. Kaur, S. Srivastav, A. Tyagi, Impact of using rosca on women empowerment 
(with reference to delhi NCR), in: 2021 9th International Conference on Reliability, 
Infocom Technologies and Optimization (Trends and Future Directions)(ICRITO), 
IEEE, 2021, pp. 1–5 .

[54] R. Ke, M. Ye, The practice of rotating saving and credit associations and interest

[69] A.R.  Levenson,  T.  Besley,  The  anatomy  of  an  informal  ﬁnancial  mar- 
ket:  ROSCA  participation  in  Taiwan,  J  Dev  Econ  51  (1)  (1996)  45–68, 
doi: 10.1016/S0304-3878(96)00425-7 . Interamerican Seminar on Macroeconomics 
[70] B. Linkow, L. Rentschler, Fraying of the ties that bind: community-level ﬁnancial 
institutions and hiv/aids with evidence from kwazulu-natal, south africa, J Afr Econ 
(2016) 1–21 .

[71] L. Martin, S. Goldman, O. Jiménez, The tanda: a practice at the intersection of 
mathematics, culture, and ﬁnancial goals, Mind, Culture, and Activity 16 (4) (2009) 
338–352 .

[72] K. McNabb, P. LeMay-Boucher, J. Bonan, Enforcement problems in roscas: evi- 
dence from benin, The European Journal of Development Research 31 (5) (2019) 
1389–1415 .

[73] H. Mehmood, T. Ahmad, L. Razaq, S. Mare, M.Z. Usmani, R. Anderson, A.A. Raza, 
Towards digitization of collaborative savings among low-income groups, Proceed- 
ings of the ACM on Human-Computer Interaction 3 (CSCW) (2019) 1–30 . 
[74] G. Mianda, Francophone sub-Saharan African immigrants organizing tontines in 
toronto: a basis for solidarity and integration, Can Ethn Stud 52 (3) (2020) 7–26 . 
[75] M.S. Mohieldin, P.W. Wright, Formal and informal credit markets in Egypt, Econ

Dev Cult Change 48 (3) (2000) 657–670 .

[76] M. Onda, Rotating savings and credit associations as traditional mutual help net- 
works in east asia, International Journal of Asian Studies 18 (2) (2021) 271–287 . 
[77] I. Onoyere, An investigation of activities of microﬁnance banks as a veritable tool 
for reducing poverty and unemployment in developing economies. the evidence 
from nigeria, Mediterr J Soc Sci 5 (6) (2014) 99 .

[78] T. Oraro, K. Wyss, How does membership in local savings groups inﬂuence the de- 
terminants of national health insurance demand? a cross-sectional study in kisumu, 
kenya, Int J Equity Health 17 (1) (2018) 1–9 .

[79] L.P. Pardo-Martínez, M.V. Huertas de Mora, La historia del cooperativismo en 
colombia: hitos y periodos, Cooperativismo & Desarrollo 22 (104) (2014) . 
[80] K. Raccanello, J. Anand, P.A. Martínez, Social capital as an incentive for partici- 
pation and formation of women-dominant Rosca, Economic Development, Integra- 
tion, and Morality in Asia and the Americas, Emerald Group Publishing Limited, 
2009 .

[81] F. Reito, Roscas without sanctions, Rev Soc Econ 78 (4) (2020) 561–579 . 
[82] F. Reito, S. Spagano, A comparison between formal and informal mutual-credit

arrangements, Dev Econ 52 (2) (2014) 179–201 .

[83] C. Rogers, Financing rural enterprise: the use of rotating credit by a village com-

munity in nepal, Savings and Development (2006) 109–130 .

[84] E.J. Ryu, A. Suzuki, Roscas as insurance: comparing formal and informal methods 
of saving among the unskilled workers in the ethiopian cut-ﬂower industry, Dev 
Econ 59 (3) (2021) 243–274 .

[85] S.K. Sadr, The optimum size of rotating Qard Hasan savings and credit associations,

ISRA International Journal of Islamic Finance (2017) .

[86] E.B. Satkunasingam, B. Shanmugam, Underground banking in Malaysia: a case

study of ROSCAs, Journal of Money Laundering Control (2006) .

[87] K. Sato, N. Kondo, K. Kondo, Rotating savings and credit association, its members’ 
diversity, and higher-level functional capacity: a 3-year prospective study from the 
japan gerontological evaluation study, Geriatrics & gerontology international 19 
(12) (2019) 1268–1274 .

11

---

<!-- PAGE 12 -->

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

[88] U. Scholten, Rotating savings and credit associations in developed countries: the

german–austrian bausparkassen, J Comp Econ 28 (2) (2000) 340–363 .

[89] A.K. Sedai, R. Vasudevan, A. Alves Pena, Friends and beneﬁts? endogenous ro- 
tating savings and credit associations as alternative for women’s empowerment 
in india, World Dev 145 (2021) 105515, doi: 10.1016/j.worlddev.2021.105515 . 
https://www.sciencedirect.com/science/article/pii/S0305750X21001273 
[90] A.O. Shem, H.J. Rösner, Savings institutions that count for small and micro enter- 
prises: the case of urban Kenya, African Review of Money Finance and Banking 
(2003) 23–46 .

[91] A. Shoaib, M.A. Siddiqui, Why do people participate in rosca saving schemes? ﬁnd-

ings from a qualitative empirical study, Decision 47 (2) (2020) 177–189 .

[92] Z. Sijia, M. Horita, Reciprocity and rule preferences of a rotating savings and 
credit association (ROSCA) in China: evolutionary simulation in imitation games, 
in: International Conference on Group Decision and Negotiation, Springer, 2019, 
pp. 43–56 .

[93] P. Smets, Roscas as a source of housing ﬁnance for the urban poor: an analysis of 
self-help practices from Hyderabad, India, Community Dev J 35 (1) (2000) 16–30 . 
[94] P. Smets, Indian community-based housing ﬁnance systems: potentials and pitfalls 
for urban development and housing improvement, International Journal of Urban 
Sciences 23 (4) (2019) 586–600 .

[95] J.P. Stodder, P. Schroth, Barriers to transparency: growth, and the growth of cor- 
ruption, in: IEMC’03 Proceedings. Managing Technologically Driven Organizations: 
The Human Side of Innovation and Change, IEEE, 2003, pp. 556–560 .

[96] D. Stoesz, I. Gutau, R. Rodreiguez, SUSU: captalizing development from the bottom

up, J. Soc. & Soc. Welfare 43 (2016) 121 .

[97] B.W. Stoﬄe, T. Purcell, R.W. Stoﬄe, K. Van Vlack, K. Arnett, J. Minnis, Credit, 
identity, and resilience in the Bahamas and Barbados, Ethnology 48 (1) (2009) 
71–84 .

[98] A.C. Tricco, E. Lillie, W. Zarin, K.K. O’Brien, H. Colquhoun, D. Levac, D. Moher, 
M.D. Peters, T. Horsley, L. Weeks, et al., PRISMA extension for scoping reviews 
(PRISMA-ScR): checklist and explanation, Ann. Intern. Med. 169 (7) (2018) 467–
473, doi: 10.7326/M18-0850 . PMID: 30178033

[99] K.S. Tsai, Banquet banking: gender and rotating savings and credit associations in

south China, China Q 161 (2000) 142–170 .

[100] M. Tsujimoto, The economic adaptation of migrants and the cooperative behavior 
by generalized exchange: the rotating credit association of Japanese migrants in 
buenos aires, Japanese Journal of Social Psychology 16 (2000) 50–63 .

[101] M. Tsujimoto, Rotating credit associations of the japanese in argentina: economic 
adaptation by generalized exchange, Japanese Journal of Qualitative Research in 
Psychology 5 (2006) 165–179 .

[102] M. Tsujimoto, M. Kuniyoshi, I. Yokuda, The genesis of resource exchange: a study 
of rotating savings and credit associations in the Okinawa islands, The Japanese 
Journal of Social Psychology (2007) .

[103] M.S. Ullah, N. Naiimi, R. Mohd Yusof, Are small and medium enterprises (SMEs) 
in lahore failing at the rate suggested in prior studies? an analysis of the degree 
of ﬁnancial stress on small and medium enterprises and its impact on their life 
expectancy, International Business Management 10 (18) (2016) 4258–4267 . 
[104] M.S. Ullah, N. Naiimi, R. Mohd Yusof, The impact of entrepreneurs’ levels of edu- 
cation, age and years in business on their decision to obtain ﬁnance for small and 
medium enterprises (SMEs) from rotating savings and credit associations (ROSCAs) 
in lahore, The Social Sciences 11 (13) (2016) 3252–3256 .

[105] M.S. Ullah, N. Naiimi, R. Mohd Yusof, What size of opportunity will open to banks 
that penetrate the small and medium enterprise (SME) ﬁnance market at lahore? 
the next great challenge for enterprising banks, The Social Sciences 11 (13) (2016) 
3245–3251 .

[106] UNDP (United Nations Development Programme), 2021 Global multidimensional 
poverty index (MPI), UNDP (United Nations Development Programme) (2021) . 
http://hdr.undp.org/en/2021-MPI

[107] H.G. Villasanti, L.F. Giraldo, K.M. Passino, Feedback control engineering for coop- 
erative community development: tools for ﬁnancial management advice for low-in- 
come individuals, IEEE Control Syst. Mag. 38 (3) (2018) 87–101 .

[108] H.G. Villasanti, K.M. Passino, Feedback controllers as ﬁnancial advisors for low-in-

come individuals, IEEE Trans. Control Syst. Technol. 25 (6) (2016) 2194–2201 .

[109] R. Vokes, D. Mills, ’Time for school’? School fees, savings clubs and social reci- 
procity in uganda, Journal of Eastern African Studies 9 (2) (2015) 326–342 . 
[110] A.N.M. Wahid, The grameen bank and poverty alleviation in bangladesh: theory, 
evidence and limitations theory, evidence and limitations, Am J Econ Sociol 53 (1) 
(1994) 1–15 .

[111] A. Wambua, P.K. Wamuyu, Role of mobile applications in mitigating challenges 
faced by informal saving groups, in: 2020 IST-Africa Conference (IST-Africa), IEEE, 
2020, pp. 1–11 .

[112] G.A. Yimer, W. Decock, M.G. Ghebregergs, G.H. Abera, G.S. Halibo, The inter- 
play between oﬃcial and unoﬃcial laws in rotating savings and credit associations 
(Eqqub) in Tigray, Ethiopia, The Journal of Legal Pluralism and Unoﬃcial Law 50 
(1) (2018) 94–113 .

[113] A.F. Zambrano, G. Díaz-García, S. Ramírez, L.F. Giraldo, H. Gonzalez-Villasanti, 
M.T. Perdomo, I.D. Hernández, J.M. Godoy, Donation networks in underprivileged 
communities, IEEE Trans. Comput. Social Syst. 8 (1) (2020) 76–85 .

[114] A.F. Zambrano, L.F. Giraldo, M.T. Perdomo, I.D. Hernández, J.M. Godoy, Variations 
of rotating savings and credit associations for community development, IEEE Trans. 
Comput. Social Syst. (2022) 1–9 .

[115] D. Zeitlyn, The talk goes outside: argument, privacy and power in mambila society

towards a sociology of embedded praxis, Africa 73 (4) (2003) 606–622 .

[116] D.A. Zelenova, V.V. Kruchinsky, An economy of miracle: rotating credit and savings 
associations in townships of Johannesburg, Etnograﬁcheskoe obozrenie 2019 (2) 
(2019) 78–97 .

12

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

World Development Sustainability 3 (2023) 100081

Contents lists available at ScienceDirect

World Development Sustainability

journal homepage: www.elsevier.com/locate/wds

Rotating savings and credit associations: A scoping review

Andres Felipe Zambrano a , ∗ , Luis Felipe Giraldo b , Monica Tatiana Perdomo c ,
Iván Darío Hernández d , Jesús María Godoy e
a
Graduate School of Education, University of Pennsylvania, Philadelphia, 19104, United States
b
Department of Biomedical Engineering and Department of Electrical and Electronic Engineering, Universidad de los Andes, Bogota, 111711, Colombia
c
Department of Psychology, Universidad de Ibague, Ibague, 730002, Colombia
d
Department of Economics, Universidad de Ibague, Ibague, 730002, Colombia
e
International Bussiness Administration, Universidad de Ibague, Ibague, 730002, Colombia

a r t i c l e

i n f o

a b s t r a c t

Keywords:
ROSCA
Informal ﬁnance
Resilience
Social capital
Inclusive economy
Microﬁnance

A Rotating Savings and Credit Association (ROSCA) is an informal cooperation strategy that has emerged in sev-
eral parts of the world as a tool to increase the resilience and social development of individuals in underprivileged
communities. This strategy has been widely studied for decades to recognize ROSCAs’ beneﬁts, risks, and opera-
tion rules in several regions and countries. In this study, we conducted a scoping review using the PRISMA-ScR
protocol to determine the most important recent ﬁndings about ROSCAs. First, we analyzed the location of the
community being studied, methodological approaches, and most common keywords of the 96 articles included
in the review. Second, we discussed the most signiﬁcant conclusions of each article on topics such as the origin,
participants, beneﬁts, risks, operation, penalties, and structure of ROSCAs. Based on this review, we discuss how
ROSCAs have provided beneﬁts to their members that are not exclusively ﬁnancial, how these schemes have
evolved from traditional ones to strategies with improved structure, rules, and technological tools, and some key
research opportunities to be addressed.

1. Introduction

Informal ﬁnancial cooperation strategies have emerged in several
parts of the world to increase the resilience of low-income communi-
ties by promoting cooperation between their members [84,89] . One of
the most representative examples of this type of strategy is the Rotating
Savings and Credit Associations (ROSCAs) [23,24,38,68,69] . ROSCAs
are an agreement between some individuals to cooperatively save a pot
of capital by paying a fee each week or month [16] . ROSCAs vary signif-
icantly in terms of the number of members, frequency of contribution,
amount of the contribution, and the process for allocating the pot [13] .
ROSCAs can be classiﬁed into three primary types depending on the
strategy used to allocate the pot: random, ﬁxed, and bidding. In random
ROSCAs, the order of receiving the pot is randomly determined at the be-
ginning of each cycle (the period required for all members to receive the
pot once) [11] . In ﬁxed ROSCAs, the order remains ﬁxed across cycles
[13] . Finally, in bidding ROSCAs, the ﬁrst turns are assigned to members
who pay or contribute more to the pot for receiving these initial turns
[54] . Regardless of the strategy to deﬁne their turns, all types of ROSCAs
allow individuals to access some ﬁnancial services and even social and

cultural beneﬁts that formal institutions do not provide, typically to low-
income communities without a positive credit score [69,89] .

ROSCAs have represented an alternative to formal ﬁnancial insti-
tutions. They have inspired banks and credit unions for individuals in
poverty situations that require help for credit alleviation or for mak-
ing aﬀordable a new productive activity to increase their well-being.
One of the most successful examples that ROSCAs have inspired is the
Grameen Bank [45] . The Grameen Bank was founded in 1976 as a re-
search project with the primary goal of providing ﬁnancial assistance
to rural communities in Bangladesh [45] . This project showed a posi-
tive impact on the socioeconomic life of their participants. Therefore,
motivated by the positive contributions of the Grameen bank in several
aspects that transcend ﬁnancial life, several researchers and communi-
ties have adopted ROSCAs idea to replicate similar projects worldwide
to mitigate poverty, mainly in places where formal banking is not an
option [110] .

Each ROSCA implementation results from the context of the place
where it is replicated. Due to the emergence of ROSCAs in several parts
of the world, ROSCAs from each country usually have diﬀerent struc-
tures, rules, and beneﬁts. For example, ROSCAs from Kenya [78] , Japan
[76] , and the United States [55] have signiﬁcant diﬀerences in terms of

∗

Corresponding author.
E-mail addresses: azamb13@upenn.edu (A.F. Zambrano), lf.giraldo404@uniandes.edu.co (L.F. Giraldo), tatiana.perdomo@unibague.edu.co (M.T. Perdomo),

ivan.hernandez@unibague.edu.co (I.D. Hernández), jesus.godoy@unibague.edu.co (J.M. Godoy) .

https://doi.org/10.1016/j.wds.2023.100081
Received 28 September 2022; Received in revised form 25 April 2023; Accepted 31 May 2023
2772-655X/© 2023 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ )

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

the number of participants, the pot allocation strategy, the periodicity
of the fee payment, and the non-monetary beneﬁts due to their culture,
tradition, needs and particular legislation of each country. Although
research before 2000 has focused on many of the aspects of ROSCAs
mentioned above [3,16,23,69,110] , many researchers have recently ex-
plored case studies to identify the particular characteristics, beneﬁts,
and challenges of ROSCAs all over the world. Moreover, the new tech-
nological developments have allowed researchers to analyze ROSCAs
from a theoretical perspective by employing mathematical models and
simulations. These diﬀerences in the methodological approaches and lo-
cations for ROSCAs have increased the number of publications studying
them in recent years. However, as far as we know, no literature review
has conducted a systematic analysis of the most important ﬁndings of
these studies. For this reason, we conducted a scoping review to compile
the analysis and conclusions of research on this topic during the last 22
years.

We used the Preferred Reporting Items for Systematic Reviews and
Meta-analysis Protocol extension for Scoping Reviews (PRISMA-ScR)
[98] to conduct a systematic map of ROSCAs research since 2000. Based
on this map, we identiﬁed which continents and countries have been
widely investigated in previous ROSCAs research and where there are
opportunities to conduct such studies. After that, we analyzed the most
common keywords of the studies, the co-occurrence of these keywords,
and the most common methodological approaches to recognize which
topics and how they have been analyzed. Then, we provide the most
important ﬁndings of the articles included in the review, discussing top-
ics such as origin, participants, beneﬁts, risks, operation, penalties, and
structure of ROSCAs. Moreover, we show some technological applica-
tions that have emerged in the last years to analyze and support the
functioning of ROSCAs. We ended this review with some conclusions
and future directions in this research area.

2. Materials and methods

Our protocol was drafted using PRISMA-ScR [98] . We searched arti-
cles available on the Scopus and Web of Science bibliographic databases
to identify potentially relevant documents. The papers included in this
review must analyze, study, or model Rotation Savings and Credit Asso-
ciations (ROSCAs). We only considered peer-reviewed journal or confer-
ence papers published between January 2000 to July 2022 and written
in English. The ﬁnal search strategy, deﬁned by team discussion, can be
found in Appendix A . To consider diﬀerent aspects of ROSCAs, we in-
cluded studies that used qualitative, quantitative, and mixed methods to

analyze ROSCAs in real communities and studies that use mathematical,
econometric, and computational tools to model these types of associa-
tions. We excluded papers that did not ﬁt into the conceptual framework
of the review or were not focused on ROSCAs. Finally, we also excluded
book chapters, book or conference introductions, and opinion articles
without clear and supported contributions.

To increase consistency among the authors of this review, we all
screened the titles of the 227 publications that resulted from our search
strategy. During this process, we excluded 104 papers whose title refers
to a diﬀerent area of knowledge or discipline. Then, all of us revised the
abstract of each of the remaining 123 articles and decided to exclude 15
papers. We did not ﬁnd retrieval from one of the remaining 108 papers.
Finally, we evaluated the full text of the retrieved 107 articles and de-
cided to include 96 based on the previously described criteria. The ﬂow
diagram of this search is shown in Fig. A.1 . We extracted their keywords,
published year, continent, and country of origin of the analyzed ROSCA,
methodological approaches, and most important conclusions for each se-
lected paper. We analyzed all keywords to group similar keywords into
just one. For example, the words Save, Saving , and Savings were grouped
in the concept Saving . Similarly, the words Women empowerment and Fe-
male empowerment were grouped in the same concept. We decided this
to provide a more accurate analysis of the co-occurrence of keywords
and the content of the selected articles. We resolved disagreements on
all of these steps by consensus and discussion with other reviewers if
needed.

3. Publication trends since 2000

In this section, we ﬁrst analyze the location of ROSCAs investigated
in the studies included in this review. For each year since 2000, we
show the number of papers that studied ROSCAs from each continent.
Then, we present the methodological approaches used in these studies,
including the evolution in the number of articles that have used these
approaches since 2000. Finally, we show the most common concepts
included in the keywords of the studies and the co-occurrences of these
concepts among the articles.

3.1. Continent and country of origin

For each article included in this review, we determined the country
and continent where its data was collected. Figs. 1 and 2 show the num-
ber of papers per continent and country, respectively. Some studies do
not use real-world data and employed theoretical approaches based on

Fig. 1. Continent of data collection. Number of studies investigating ROSCAs
from each continent.

2

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Fig. 2. Country of data collection. Number of studies investigating
ROSCAs from each countries.

Fig. 3. Published year and continent of studied ROSCAs. Number
of papers published between January 2000 and July 2022 consid-
ering the continent of the analyzed ROSCA.

previous ﬁndings. These studies are classiﬁed in the category None in
the ﬁgures. Fig. 2 also includes a category called Others to refer to those
countries studied only in one article.

Asia and Africa are the continents where most studies have collected
their data. As mentioned in the Discussion section, one of the most
important motivations to participate in ROSCAs is the limited access
to ﬁnancial support from formal institutions such as banks. Therefore,
ROSCAs are common in countries where the poverty index is high [106] .
Research that uses data from developed countries also focuses on under-
privileged communities such as migrants, mainly the studies from North
America [47,48,74] and Europe [17,26] . We only found one study that
used data from the Caribbean [97] and two that used data from Mex-
ico [71,80] since 2000. Moreover, we did not ﬁnd any articles that
used data from South America and Oceania. However, ROSCAs from
Bolivia have been also studied in some works [2,3,30] , and Colombian
researchers have also studied ROSCAs from a theoretical and computa-
tional approach [113,114] .

Fig. 3 shows the number of publications for each year since 2000.
The number of articles that use data from each continent for every year

was included. Between 2016 and 2019 seems to be an increasing trend
in the published papers. However, this tendency stopped for the last
three years, probably due to the eﬀects of pandemics that reduced the
possibility of interacting with ROSCAs members and acquiring data from
real scenarios. This hypothesis is also analyzed in the Methodological
approaches section.

3.2. Methodological approaches

Since  2000,  the  studies  have  used  diﬀerent  methodological  ap-
proaches depending on the particular objectives of the authors. Fig. 4
shows the number of published articles that have used each of these
approaches to analyze ROSCAs. Interviews and surveys are the most
common approaches for acquiring data from particular case studies
[42,53,65] . Using this data, authors tend to provide an analysis using de-
scriptive statistics methods, including central tendency and dispersion
measurements, and applying statistical hypothesis testing [25,40,62] .
Other approaches for analyzing case studies are theoretical and histori-
cal reviews. These works use methods employed in systematic or scoping

3

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Fig. 4. Methodological approaches. Number of papers that uses each method-
ological approaches employed for studying ROSCAs.

reviews to explore particular research questions about the evolution of
ROSCAs in speciﬁc regions or countries. In those cases, the authors do
not acquire their data and use data or ﬁndings from previous studies to
provide a similar analysis to those with their own data.

Mathematical models have also been used to analyze ROSCAs. These
mathematical models are developed using data from real ROSCAs to
provide helpful conclusions about these schemes and their participants.
These studies use surveys or previously acquired data to create Probit,
Logit, or other regression models and test hypothesis based on the pa-
rameters of the models [1,7,14,18,32,87] . Theoretical models from eco-
nomics, such as utility functions [8,28,81,89] and econometric models
[70] have also been used to provide a similar analysis. From this per-
spective, studies tend to use the rationale formulated by previous ﬁnd-
ings for their models. Moreover, some of these studies compared their
models with data from real scenarios [89] .

Technological advances have enabled the use of other approaches
that require the use of computing resources. Some hypotheses and sce-
narios require months or years of data acquisition to be tested and ana-
lyzed. Computational models and multi-agent simulations have emerged
as an alternative for this type of analysis [51,61,92,107,108] . These
models employ theoretical concepts of control systems and game theory
to propose possible interventions for real ROSCAs [37,73,111] . Also,
web applications have been developed to support the operation and
maintenance of real ROSCAs. Finally, social experiments have been con-
ducted to analyze the behavior of human beings. These experiments of-
fer useful ﬁndings on trust, reputation, altruism, and other concepts of
social theory in ROSCAs [35,60] .

Fig. 5 shows the evolution of the use of these approaches since 2000.
Interviews, surveys, and models based on data from real scenarios have
been the most common approaches until 2020. However, during the
last three years, the number of studies that use these approaches has de-
creased. Pandemic restrictions would explain this decrease. During these
years, access to communities has been limited. Therefore, other theo-

retical approaches, such as reviews, and economic and computational
models, have prevailed. Moreover, the number of studies that employ
computational tools has also been increasing in the last few years.

3.3. Keywords analysis

Keywords occurrence can give an idea of what topics are being an-
alyzed more in articles about ROSCAs since 2000. However, counting
the occurrence of keywords without analyzing the concept behind them
can bias the analysis. For example, although immigrants and migrants are
diﬀerent words, both refer to the same concept. Similarly, when com-
paring keywords such as Informal savings and Mutual-saved money , three
concepts are recognized. The concept Informal and Mutual are particular
for each keyword, but they also have a common concept which is Sav-
ings . Therefore, we change the focus from keywords to concepts. To do
this, we considered the root or the concept behind each word in each
keyword and then split all keywords and counted the occurrence and
co-occurrence of each concept among all papers. We also considered
the country and continent of ROSCAs being studied as a concept be-
cause many articles included them as keywords. This process was made
manually without employing any additional software to avoid mistakes
in interpreting each keyword’s roots or in splitting the keywords with
more than one word. To increase consistency, we all screened the key-
words of the selected publications and evaluated the concepts described
by each keyword. These are the concepts employed for the occurrence
and co-occurrence analysis.

Fig. 6 shows the number of occurrences of all the concepts that ap-
pear in the keywords of at least ﬁve studies. As was expected, ROSCA
is the most repeated concept in keywords. However, only 65 of the 96
articles included it as a keyword. Other common concepts that appear
signiﬁcantly in keywords of articles are related to ﬁnance and econ-
omy. Concepts such as Finance, Micro, Small, Enterprise, Credit, Savings,
Banking, Management , and Market show that authors are researching the

4

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Fig. 5. Published year. Number of papers published between January
2000 and July 2022 considering the methodological approach of each
study.

Fig. 6. Number of occurrences of most common
keywords. A threshold of at least 5 occurrences was
applied.

usage and performance of ROSCAs as alternatives to formal banking to
provide some type of economic beneﬁt to their members, such as cred-
its to start or invest in a micro-small enterprise, or a mechanism to save
for uncertain negative events in the future [32,47,51,86,89,103–105] .
The continents and countries also appear commonly in keywords. For
this reason, Asia, Africa, Kenya, India, Japan, and other continents and
countries that have been widely studied according to Figs. 1 and 2 also
appear in Fig. 6 . Finally, some concepts that are not directly related to
ﬁnance, such as Social, Informal, Women, Behavior , and Rural , are also
common in the studies.

To consider the relation between these concepts, we plotted a net-
work shown in Fig. 7 that considers the occurrence and co-occurrence
of the concepts. Each node of the graph represents the number of occur-

rences of the concept in the keywords among all papers. Each arc repre-
sents the number of co-occurrences of two concepts in the same article
among all studies. We deﬁned a minimum threshold of ﬁve occurrences
and ﬁve co-occurrences to be included in the graph. The strongest con-
nections in the plot occur between ROSCAs, ﬁnancial concepts, and the
two continents with the highest amount of studies. This graph shows
a relation between ROSCAs and micro, small, and medium enterprises
because of the importance of ROSCAs to ﬁnance entrepreneurs. Lastly,
there is also an interesting relation between the concepts of Social, Cap-
ital, Women , and Immigrants . These relations show that several articles
focus on the social groups who participate in ROSCAs, their motiva-
tions, behavior in the association, and the non-ﬁnancial beneﬁt that
these individuals would obtain as social, health, or cultural capital

5

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Fig. 7. Keywords Occurrences and Co-occurrences. A threshold of at least 5 occurrences and co-occurrences was applied.

[48,53,63,65,74] . In the discussion section, we deeply analyze the com-
mon ﬁndings of the studies included in this review.

4. Findings and contributions of publications since 2000

We identiﬁed 96 papers addressing studies on ROSCAs between 2000
and 2022 to include in this scoping review. These articles study char-
acteristics such as the origin of ROSCAs, their participants, beneﬁts,
motivations, and behavior of their members, and mechanisms of op-
eration and control that have been used by real ROSCAs. Moreover,
other articles have also found and proposed alternatives to improve the
economic performance and wellness of the ROSCAs and their members
through mathematical and computational models and technological ap-
plications. In this section, we discussed these ﬁndings. To organize the
most relevant ﬁndings of these articles, we grouped them into ﬁve cat-
egories. These categories are not exclusive. Therefore, those articles
whose contributions go beyond one speciﬁc category are discussed in
more than one section.

4.1. Origin, participants and beneﬁts of ROSCAs

As it is shown in Figs. 1 and 2 , ROSCAs have emerged in several
parts of the world. Associations in one continent are not necessarily the
consequence of another ROSCA from a diﬀerent place, and the causes of
their consolidation can vary from one case to another. The most recog-
nized motivation for creating a ROSCA is the limited access to ﬁnancial
services for several people from diﬀerent types of social groups [1,91] .
Although this issue can be common for low-income communities be-
cause of a low credit score, migrants and women also have social and
cultural barriers to accessing ﬁnancial services from formal institutions
such as banks [46,99] or even borrowing money from their neighbors
[50] . Therefore, ROSCAs have emerged as a mechanism that can give
these communities access to credits, looking for ﬁnancing for education
and health services [31,78,109] , vehicles, housing, lands, livestock, and
other means of production [15,28,48,93] , or non-capital goods and so-
cial and cultural events [65] .

ROSCAs are also used as mechanisms to save money periodically
[38] . Women have stated that having the discipline to save money and
avoid spending it on non-capital goods would be diﬃcult [17] . Self-
control is not only a problem for women. Men have shown lower dis-
cipline saving than women [99] . In several cases, women are mainly
motivated to participate in ROSCAs to attenuate the self-control prob-

lems of their husbands [9] . Several studies have shown that individuals
from diﬀerent social groups and demographics recognize their discipline
problems to save money [25,41,86] . Therefore, many individuals par-
ticipate in ROSCAs looking for a mechanism to force themselves to save
and reduce expenses because of the social pressure and the embarrass-
ment that can imply a non-payment or a defection [34,36,49,94] . They
visualize ROSCAs as an opportunity to eﬀectively save money, increas-
ing their resilience for future uncertain negative events and allowing
them to have the capital to invest in the future [6,8,25,41,73] .

This desire to increase and improve their investing opportunities is
also an important motivation for consolidating informal associations. Al-
though ROSCAs are common in underprivileged and underrepresented
communities, many entrepreneurs from micro, small, and medium en-
terprises also use ROSCAs as alternatives to formal ﬁnancing institutions
[5,22,27,32,52] . Some members of ROSCAs also can obtain credits from
banks but prefer informal associations because of the lower or null inter-
est rates [22,34,43,88,90,93,103–105] and the ﬂexibility of the usage of
the credits [44] , instead of having excessive restrictions and debts with
banks that they consider diﬃcult to pay because of the high interests
[26] . Although individuals of high income prefer formal institutions to
save and invest their money [21] , the participation of medium-income
individuals in ROSCAs is higher than individuals with low income [56] .
In some cases, participants of ROSCAs have also recognized that they
consider banks corrupted and non-transparent institutions [55] . There-
fore, no matter the interest rates, they trust informal associations more
and prefer this ﬁnancing option.

Based on this preference of some entrepreneurs for ROSCAs, several
works have modeled the possible impact of ROSCAs on entrepreneurs
showing positive economic results [82,83] . Higher economic growth
and lower poverty rates of members of ROSCAs have been observed in
real scenarios around the world [7,27,39] . This positive economic im-
pact on participants of informal associations, including those who can
access formal institutions, shows the viability and the importance of the
coexistence of diﬀerent types of ﬁnancial institutions to oﬀer the ser-
vices that people from diﬀerent demographics require.

Lastly, ﬁnancial services are not the unique motivation for ROSCAs
members. In some cases, the creation of social capital is more important
than the economic beneﬁt that members would receive [15,76,95,109] .
Some of them believe that informal associations are an opportunity to
meet new people who can be helpful for career development or future
business or to increase their social status [1,91] . In other cases, mainly
for women, migrants, and other underrepresented groups, ROSCAs are

6

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

an empowerment tool that helps them meet people with similar ideas,
habits, and cultures, consolidating links and friendships that transcend
the professional and economic ﬁeld [17,53,64,89] . Women and mi-
grants have recognized that ROSCAs help them to feel welcomed and
respected by others who are similar to them [74] and, in the case of im-
migrants, who preserve the same ancestral traditions [97] . This social
capital has also shown a beneﬁcial impact on the physical and psycho-
logical health of ROSCAs members. For example, Mujin participation in
Japan is correlated to a reduction in the decrease of the functional ca-
pacity of elderly people [62,63,87] . These studies have shown that the
positive impact of ROSCAs on health occurs for those participants who
are not only interested in the economic beneﬁt. Therefore, social capital
and its positive implications are also substantial beneﬁts of ROSCAs that
the formal banking system cannot oﬀer.

4.2. Operation and control

Although all ROSCAs share similar characteristics, such as the peri-
odical fee and the allocation of a percentage of the pot to each member,
each ROSCA has its peculiarities that directly impact the performance
of the association. Some characteristics such as the order of the pot al-
location, structure, number of participants, roles, connectivity and in-
teractions between members, amount of the fee, and control strategies
are fundamental for the success of the scheme [72,85] .

Usually, ROSCAs have a horizontal structure where all members can
participate in most decisions. However, the leader and other members
with relevant roles tend to be more inﬂuential on the most important
decisions of the association. Therefore, the ethics of these members are
crucial for the correct functioning of the association [42] . One of these
decisions is the order of the pot allocation, which would be decisive for
the particular actions of each member of the scheme. The traditional
method to assign this order is by a random selection at the beginning
of the process [73] . During the ﬁrst meeting, individuals usually know
when they will receive the pot. In several cases, the leader, the mem-
bers with important roles, and their closest friends or guests received
the ﬁrst turns because of their inﬂuence, while the random selection is
applied only for the remaining turns [14] . In other cases, the ﬁrst turns
are assigned to those members who decide to pay more for these turns
[54] . This type of association, called Auction or Bidding ROSCA, helps
those members who need the money for an investment, such as start-
ing a micro-small enterprise, or for any particular reason to be the ﬁrst
to receive the pot. In this way, members who would beneﬁt more from
receiving the pot earlier are prioritized if they can pay for it. However,
some individuals would need the pot early to pay debts and cannot pay
for receiving it before others. To help them, in some cases, members of
the ROSCA agree to assign the order based on the needs of each partic-
ipant, giving priority to those with higher needs [17] .

ROSCAs participants do not necessarily prefer the ﬁrst turns [13] .
Individuals with higher incomes and women tend to be more patient
and accept later turns [18] . Some ROSCAs agree to wait until the end
of the process to divide the total pot among all contributing members
without assigning an order for the pot allocation [96] . Although this
would not be optimal considering the value of money over time, some
members prefer it to avoid the temptation of spending the pot if they
receive it early or just the negative perception of owing money to the
others [6] . In summary, the order of the pot allocation is always based
on the particular interests and sense of justice of the members who desire
to maximize their income, diversify the risks and help those with more
needs [67] .

Another important decision in ROSCAs is the admission of new mem-
bers. This decision is mainly inﬂuenced by the social circle of the per-
son who desires to participate [93] . In several cases, ROSCAs only admit
new members if they have been suggested by older members, looking for
higher trustworthiness of the scheme [12] . With this admission method-
ology, recommenders will pay for the credit defaults of their guests.
Another common selection criterion is the income of the candidates.

If they cannot demonstrate regular incomes or a minimum level of in-
come, ROSCAs exclude them because of the risk of defaults in the fees
[21,75,93] . This rule justiﬁes that, in some cases, individuals of middle
income participate more in these schemes than individuals from low-
income communities. This evidence reframes the initial motivation for
using ROSCAs only as an alternative for low-income communities who
cannot access formal ﬁnancial institutions because, in several cases, they
cannot access informal schemes either.

ROSCAs participants tend to trust other members, mainly in small as-
sociations. However, in schemes with more members, participants pre-
fer to use signed contracts, registering of contributions, identiﬁcation
cards, and other strategies that do not depend on the social relations of
the members [112] . To punish the defaults, ROSCAs use heavy economic
penalties, disqualiﬁcation to receive the pot, social sanctions, and exclu-
sion of social and cultural events [10,60,61,112] . The economic penal-
ties, added to the small interest rates, sometimes provide a surplus in
the pot after all the turns. This surplus is employed for the common ben-
eﬁt of the community. On some occasions, this money is divided among
all the members. In other cases, the members who actively participate
by asking for credits and paying higher fees also demand to receive a
higher percentage of the pot surplus [67] . Finally, from a theoretical and
mathematical perspective, it has been argued that in the absence of an
external (social) sanctioning mechanism, ROSCAs are never sustainable,
even if the defecting member is excluded from all future ROSCAs. [10] .
However, other theoretical models have shown that some associations
can be immune to defection without social sanctions if the number of re-
sources lost because of the default is small enough to avoid a reduction
in the motivation of their members [81] . This result shows the impor-
tance of trust and motivation. In real scenarios, many participants trust
their ROSCAs because of the requirements to become a member and the
strategies to minimize defections [112] . However, informal associations
have some risks and disadvantages that would diminish motivation and
cause a negative impact on their members.

4.3. Risks and disadvantages

Although ROSCAs are resilient to the loss of money, the loss of mo-
tivation of the members would be the immediate cause of ROSCAs’ fail-
ures. This loss of motivation can result from the default of any of the
members or discontent with the rules, roles, or transparency of the asso-
ciation [4,60,95,99,115] . For this reason, the ethics and behavior of the
members, mainly the leader, is vital for the scheme’s success. However,
there are also other risk factors in ROSCAs, even in scenarios where
all individuals desire to cooperate. In some cases, mainly in bidding
ROSCAs, individuals would be tempted to pay an excessive fee or ac-
cept high-interest rates to obtain an early turn [14,54] . This situation
would be aggravated due to the impatience of some members who are
reluctant to wait several months [19] . If fees or rates are excessive, some
participants will fall into diﬃculty paying debts, forcing them to default
and reducing the motivation of the other members.

The reduced ﬁnancial knowledge of several members and the low in-
tervention of the government due to the informal nature of the associa-
tions would worsen this negative situation [20] . These reduced ﬁnancial
skills can also motivate the transition to Ponzi schemes because of the
desire of the members to obtain immediate and higher rewards [116] .
These schemes are unsustainable because, at some point, new members
will not receive back the money they contributed. After all, this money
is employed to pay the proﬁt of older participants, and later contribu-
tions would not be enough. Therefore, this transition and the lack of
ﬁnancial skills exacerbate the risk for ROSCAs members.

In some cases, participants will be trustworthy and have a minimum
ﬁnancial education to avoid unsustainable decisions. However, some in-
trinsic characteristics of ROSCAs can also be a disadvantage compared
to formal institutions. Many ROSCAs are conformed by members that do
not have regular incomes [50] . Therefore, even if individuals want to
contribute to the association, they would not be able to pay their fees for

7

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

some months. Moreover, the maximum pot is the sum of the particular
contributions of each member. This amount of money is considerably
less than the amount of money that a bank would have. For this reason,
if some individual needs a credit higher than the total pot, the beneﬁt
received from the ROSCA would not be enough [75] . Finally, if the as-
sociations do not charge an interest fee or invest the pot to get an extra
return, the members would be losing money over time because of the
inﬂation of countries and the evolution of the value of money [88] .

Lastly, exogenous factors such as natural disasters, thefts, health is-
sues, and even the death of a member, and economic issues of the region
or country of associations would also be a risk to their success [4,70] .
However, when a loss of money happens due to an exogenous cause,
ROSCAs tend to evolve and be more resilient compared to those scenar-
ios where the cause of the loss was a defection of a member [34,70] .
As we mentioned before, the motivation to cooperate is the most rel-
evant factor for the scheme’s success. When the cause of the loss is a
defection, the decrease in motivation is higher, and the probability of
failure of the ROSCAs increases [56] . For this reason, it is crucial to
maintain the members motivated and committed to the success of all
the participants.

4.4. Improvement of economic performance and wellness

Many studies have modeled ROSCAs to identify alternatives to im-
prove their economic performance and the wellness of all their members
[16] . These works have included concepts such as altruism, reciprocity,
and reputation to ﬁnd helpful insights to improve real ROSCAs. One of
the most relevant ﬁndings of these works is the importance of reciprocity
and altruism for the correct operation of traditional ROSCAs [60] . When
individuals are more willing to contribute to others and are also mo-
tivated by the contributions of others, ROSCAs tend to be successful
and provide economic development to their members [59,61,92,107] .
Several social experiments have also demonstrated that members of
ROSCAs usually have high levels of reciprocity and altruism [35,60] .
Therefore, a strategy to potentially improve the performance of ROSCAs
is to maintain and enforce these behaviors between members. For ex-
ample, ROSCAs have been employed to ﬁnance the electriﬁcation of
vulnerable communities that historically had no access to electricity ser-
vices [29] . This type of project promotes reciprocity by beneﬁting the
community over individual interests.

Maintaining members highly motivated is vital to deal with the de-
fection issue. One possible solution is to improve the selection process
of new members. Although the use of a minimum threshold of income
has become a method to select the participants of ROSCAs, this would
deny access to people who really need that ﬁnancial service and would
not necessarily defect the association in the future. Therefore, through
computational modeling analysis, it has been proposed to use reputa-
tion to select new participants [61,113] . This selection method has been
used by ROSCAs when requiring old members to recommend new ones
[12,102] . On the other hand, other authors proposed to increase the
economic and social penalties [33,61] . With this strategy, individuals
will be more reluctant to defect to avoid these penalties and lose their
reputation with others [34,49] . Finally, to reduce the economic impact
of defection, it has also been proposed to increase the interest rates,
mainly for ROSCAs with a high number of members [4] , and to use a
cash reserve ratio that will support the losses caused by defaults [114] .
Defections and defaults are inevitable, even in cases where all the
individuals desire to cooperate. If individuals have to decide between
using their capital to acquire some vital goods or continue contributing
to the association, survival would be the decision for everyone. For this
reason, some variations in the order of turns to reduce this situation
would increase the resilience of the association. One possible strategy is
giving ﬁrst turns to individuals who have higher needs. In these cases,
if those individuals invest that beneﬁt appropriately, they would have
more options to continue contributing in the future instead of losing
the capacity to pay the fee of the ROSCA [17] . Another option is giving

priority to individuals with higher incomes and capital because they
would have a higher capacity to continue contributing to others, and
the risk of default after receiving the pot will be reduced [4,54] .

The structure can also be modiﬁed to increase the resilience of as-
sociations and individuals. If each member participates simultaneously
in more than one association, it would have a higher probability of re-
ceiving a pot earlier and a lower probability of losing all the money due
to a ROSCA’s failure. This strategy, inspired by the diversiﬁcation of
investments to reduce the risk, is studied in [114] , showing promising
results. Moreover, several ROSCAs members in real scenarios have been
participating in more than one association showing economic growth
[1,105] . Another proposal of the work in [114] is to reduce the number
of members on each ROSCA. Small ROSCAs can force their members
to save while reducing the probability of defection by decreasing the
number of members. Following these proposals, participants diversify
their contribution while reducing the number of people they depend
on, signiﬁcantly decreasing the risk. Furthermore, although the pot will
be lower, the waiting time until receiving it will also be lower due to the
small number of members. This idea has also shown promising results
in real scenarios [8] .

Lastly, a ﬁnal proposal to increase the performance of ROSCAs is the
transition from informality to formality [31,55] . This transition would
provide this type of association with rules such as a cash reserve ratio re-
quirement, a maximum fee, a maximum or a minimum number of mem-
bers, or interest rates, added to government support to reduce the risks
of defaults and defections. However, before transitioning to formality, it
must be analyzed if the new formal ROSCAs would have the same issues
as banks, discouraging the participation of several social groups that the
current informal ROSCAs contribute. Therefore, another alternative is to
provide both options to participants and allow them to decide between
formality, informality, or both. This option has also shown promising
results [22] . In summary, some proposals such as diversiﬁcation, the
coexistence of formal and informal ﬁnancial services, and the formal-
ization or regulation of current ROSCAs should be analyzed to improve
the beneﬁts and reduce the risks of their participants [58,77,82] .

4.5. Technological applications

Technological development has allowed new methodological ap-
proaches to analyze and support ROSCAs. Since observing and evaluat-
ing the performance of improvement strategies in real ROSCAs takes sig-
niﬁcant time and eﬀort, computer tools have been proposed in research
work to model human dynamics [4,92] . These computational models
have been used to predict the results of applying realistic variations to
ROSCAs [113,114] . Based on dynamic systems and multi-agent systems
theory, the works in [61,113,114] have demonstrated the importance of
motivating reputation and altruism and the need for decentralized struc-
tures, diversiﬁcation of investments in ROSCAs, and a cash reserve ratio
to increase resilience in scenarios with low trust and trustworthiness.
Furthermore, the authors of [51] have also used agent-based models
to explore the resilience of informal associations to disasters, showing
the importance of carefully tailoring to local contexts. Finally, compu-
tational models have also been used to analyze the particular actions
of each participant of informal associations to increase their individual
resilience [107,108] . These works have used feedback control theory to
show that the best actions for individuals are the investment in health
and education capital, which can represent a high return on investment
in the future, and being altruistic with their neighbors to increase the
probability that one of them would help them in the future if they need
it.

Technological tools have also been used to provide ROSCAs partic-
ipants with better control tools and allow them to participate in these
schemes even if all the members are not geographically in the same place
[37] . These tools help participants organize their ﬁnance, have an in-
dividual and collective register of contributions and expenses, schedule
reminders for future fees, and identify defaults [73,111] . In summary,

8

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

these technological tools help ROSCAs, mainly those with a higher num-
ber of members, to increase the security and transparency in the trans-
actions, pot allocation, and economic decisions of members [112] .

4.6. New research directions

Although research about ROSCAs has been mainly focused on spe-
ciﬁc communities around the world employing several methodological
approaches, the interest of researchers is still highly concentrated in
Asia and Africa. Before 2000, [110] and [3] had shown the presence of
ROSCAs in North and South America, respectively. However, the num-
ber of publications that used data from America during this century has
been lower than ten. Therefore, there is a need to continue investigat-
ing the particularities of ROSCAs in America, mainly in South America,
to understand how the context of a country would impact the bene-
ﬁts, management, and limitations of these cooperative schemes. This
research would have a signiﬁcant impact in countries such as Colom-
bia, Venezuela, and Argentina, where several cooperative eﬀorts have
emerged in diﬀerent social groups [66,79] , including Japanese migrant
communities that have employed these cooperative strategies in Ar-
gentina after World War II [57,100,101] .

Another research direction for future years is to investigate inter-
ventions in ROSCAs looking for an improvement in the socioeconomic
conditions of the communities that would be beneﬁted from them. As
shown in this review, most studies have conducted a descriptive anal-
ysis using surveys and interviews or proposed interventions based on
mathematical and computational models. However, few studies have
intervened in the associations to test the real impact of the proposed al-
ternatives to improve ROSCAs. These interventions should be designed
in agreement with the administrators and members of associations to
understand the possible implications of these interventions that are not
necessarily considered in mathematical models and simulations, and to
avoid a negative impact on the community. It is critical to establish close
communication with these organizations to implement aﬀordable inter-
ventions that would oﬀer the desired impact on these communities and
report the complete design and implementation experience to replicate
this type of intervention in several parts of the world.

One of the interventions explored is using technological devices as
control and advisory tools for administrators and members of ROSCAs.
Further developments in control theory and artiﬁcial intelligence can
potentially be used to recognize those patterns that would maximize
members’ proﬁt and design ideal advisors for ROSCAs, considering pri-
vacy and ethical issues.

5. Conclusion

This article presented a scoping review of Rotating Savings and
Credit Associations (ROSCAs) research over the last 22 years. Asia and
Africa were the continents with the highest amount of ROSCAs studied
since 2000. There have been diﬀerent methodological approaches to

studying these informal associations. These approaches mainly include
case studies that collected data through surveys and interviews and used
descriptive statistics or developed regression models based on these data
to analyze them. Some of the most important ﬁndings are the ability of
ROSCAs to help their members increase their ﬁnancial wellness by forc-
ing individuals to save money and enabling them to have better invest-
ments. Furthermore, ROSCAs also enforce the social relations of their
members, improving their social capital, and, in some particular groups
such as migrants, women, and the elderly, maintain ancestral traditions,
improve physical and psychological health, and empower them. More-
over, some strategies, such as increasing the number of ROSCAs where
each individual participates, reducing the fee and the number of partic-
ipants of each ROSCA, and promoting altruism and reciprocity, would
potentially minimize the eﬀect of defection and default.

With the recent development of technological and computational
tools, new methodological approaches have become available. Multi-
agent systems, feedback control theory, and machine learning models
have been employed to analyze ROSCAs. Furthermore, these models also
oﬀer the opportunity to test several promising strategies before applying
them in real scenarios to recognize if they can be aﬀordable and help-
ful for communities. Finally, web and mobile applications also become
available to improve the transparency and security of ROSCAs, help-
ing their members register transactions and providing investment and
contributions advice. We consider that future research directions should
be the observation of these associations in continents where they have
not been widely studied and the application of these mathematical and
technological tools to improve ROSCAs’ performance and wellness of
their members. For these interventions, researchers should remember
the limitations that mathematical models and technological tools have,
the ancestral and social importance of ROSCAs to several communities,
and the need for close communication with the communities.

Declaration of Competing Interest

The authors certify that they have NO aﬃliations with or involve-
ment in any organization or entity with any ﬁnancial interest (such
as honoraria; educational grants; participation in speakers’ bureaus;
membership, employment, consultancies, stock ownership, or other eq-
uity interest; and expert testimony or patent-licensing arrangements),
or non-ﬁnancial interest (such as personal or professional relationships,
aﬃliations, knowledge or beliefs) in the subject matter or materials dis-
cussed in this manuscript.

Acknowledgments

This work was partially supported by Google through the Google
Research Award for Latin America, and by the Universidad de los Andes
and Universidad de Ibagué through Convocatoria Conjunta Unibagué-
Uniandes.

9

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

Appendix A. Final Search Strategy

S1 File

Fig. A1. Identiﬁcation and screening processes followed to determine the included studies in this review.

Final search strategy. Search strategy employed to identify articles

that would be included in this review.

References

[1] J.K. Acquah, R. Dahal, Rosca s as lenders of last resort after ﬁnancial crises: lessons

from Indonesia, J Int Dev 30 (7) (2018) 1223–1239 .

[2] D.W. Adams, M.L. Canavesi, Rotating savings and credit associations in Bolivia 1,
in: Informal Finance in Low-income Countries, Routledge, 2019, pp. 313–323 .
[3] D.W. Adams, M.L.C. de Sahonero, Rotating savings and credit associations in bo-
livia/les institutions informelles de crédit en bolivie (roscas), Savings and develop-
ment (1989) 219–236 .

[4] D. Ahn, W. Kang, K.-K. Kim, H. Shin, Analysis and design of microﬁnance services:

a case of rosca, The Engineering Economist 62 (3) (2017) 197–230 .

[5] J.E. Akoten, Y. Sawada, K. Otsuka, The determinants of credit access and its impacts
on micro and small enterprises: the case of garment producers in kenya, Econ Dev
Cult Change 54 (4) (2006) 927–944 .

[6] M. Aliber, Rotating savings and credit associations and the pursuit of self-discipline:
a case study in south Africa, African review of money ﬁnance and banking (2001)
51–73 .

[7] M. Altuntas, A. Erlbeck, F. Huber, The eﬀect of rosca participation on microin-
surance purchase, Zeitschrift für die gesamte Versicherungswissenschaft 108 (2)
(2019) 141–163 .

[8] S. Ambec, N. Treich, Roscas as ﬁnancial agreements to cope with self-control prob-

lems, J Dev Econ 82 (1) (2007) 120–137 .

[9] S. Anderson, J.-M. Baland, The economics of roscas and intrahousehold resource

allocation, Q J Econ 117 (3) (2002) 963–995 .

[10] S.  Anderson,  J.-M.  Baland,  K.O.  Moene,  Enforcement  in  informal  saving
groups, J Dev Econ 90 (1) (2009) 14–23, doi: 10.1016/j.jdeveco.2008.09.003 .
https://www.sciencedirect.com/science/article/pii/S0304387808000862

[11] S. Ardener, The comparative study of rotating credit associations, The Journal of
the Royal Anthropological Institute of Great Britain and Ireland 94 (2) (1964)
201–229 .

[12] D. Aredo, Rotating savings and credit associations: characterization with particular
reference to the ethiopian iqqub, Savings and Development (2004) 179–200 .
[13] J.-M.  Baland,  C.  Guirkinger,  R.  Hartwig,  Now  or  later?  the  al-
location  of  the  pot  and  the  insurance  motive  in  ﬁxed  roscas,  J
Dev
doi: 10.1016/j.jdeveco.2019.04.001 .
https://www.sciencedirect.com/science/article/pii/S0304387818316389
[14] J. Bauchet, V. Larsen, Rosca composition and repayment: evidence from taiwanese

(2019)

1–11,

Econ

140

bidding roscas, J Dev Stud 54 (9) (2018) 1483–1495 .

[15] C. Benda, Community rotating savings and credit associations as an agent of
well-being: a case study from northern rwanda, Community Dev J 48 (2) (2013)
232–247 .

[16] T. Besley, S. Coate, G. Loury, The economics of rotating savings and credit associ-

ations, Am Econ Rev (1993) 792–810 .

[17] B. Bilecen, ’alt ı n günü’: migrant women’s social protection networks, Comparative

Migration Studies 7 (1) (2019) 1–17 .

[18] J. Bonan, P. LeMay-Boucher, K. McNabb, C.C. Tomavo, Time preferences and com-
mitment devices: evidence from roscas and funeral groups in benin, Oxford Devel-
opment Studies 47 (3) (2019) 356–372 .

[19] J.  Bonan,  P.  LeMay-Boucher,  D.  Scott,  Can  hypothetical  measures  of  time
preference  predict  actual  and  incentivised  behaviour?  evidence  from  sene-
gal,  World  Dev  159  (2022)  106029,  doi: 10.1016/j.worlddev.2022.106029 .
https://www.sciencedirect.com/science/article/pii/S0305750X22002194

10

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

[20] M.J. Bophela, N. Khumalo, The role of stokvels in south Africa: a case of economic
transformation of a municipality, Problems and Perspectives in Management 17 (4)
(2019) 26 .

[21] S.B. Carpenter, R.T. Jensen, Household participation in formal and informal sav-
ings mechanisms: evidence from pakistan, Review of Development Economics 6
(3) (2002) 314–328 .

[22] N.S. Chiteji, Promises kept: enforcement and the role of rotating savings and credit

associations in an economy, J Int Dev 14 (4) (2002) 393–411 .

[23] J.S. Coleman, Foundations of Social Theory, Harvard University Press, 1994 .
[24] D. Collins, J. Morduch, S. Rutherford, O. Ruthven, Portfolios of the Poor: How the

rate liberalization-a case study of wenzhou, The Chinese Economy 52 (2) (2019)
155–170 .

[55] M. Kear, Peer lending and the subsumption of the informal, J Cult Econ 9 (3) (2016)

261–276 .

[56] A.M. Kedir, G. Ibrahim, Roscas in urban ethiopia: are the characteristics of the in-
stitutions more important than those of members? Journal of development studies
47 (7) (2011) 998–1016 .

[57] Minorities and diversity, K. Kimura (Ed.), Trans Paciﬁc Press, 2011 .
[58] S. Klonner, Rotating savings and credit associations when participants are risk

averse, Int Econ Rev (Philadelphia) 44 (3) (2003) 979–1005 .

World’s Poor Live on $2 a Day, Princeton University Press, 2010 .

[59] S. Klonner, Private information and altruism in bidding roscas, The Economic Jour-

[25] O. Dagnelie, P. Lemay-Boucher, Rosca participation in benin: a commitment issue,

nal 118 (528) (2008) 775–800 .

Oxf Bull Econ Stat 74 (2) (2012) 235–252 .

[26] K. Datta, C. Aznar, The space-times of migration and debt: re-positioning migrants’
debt and credit practices and institutions in, and through, london, Geoforum 98
(2019) 300–308 .

[27] R. Dekle, K. Hamada, On the development of rotating credit associations in japan,

Econ Dev Cult Change 49 (1) (2000) 77–90 .

[28] Y. Dinç, R. Jahangir, R. Nagayev, F. Çak ı r, Economics of savings-based ﬁnance: an
interest-free model of rotating savings and credit association in turkey, Journal of
Islamic Accounting and Business Research (2021) .

[29] B. Diouf, Tontine: self-help ﬁnancing for solar home systems, Renew Energy 90

(2016) 166–174 .

[30] S.B. Donoso, Y. Altunba ş , A. Kara, The rationale behind informal ﬁnance: evidence

from roscas in bolivia, The journal of developing areas (2011) 191–208 .

[31] N. Dube, K. Edwell, Strengthening informal social security to provide meaning-
ful social protection: the case of stokvels in soweto, J Soc Dev Afr 33 (1) (2018)
157–181 .

[32] B.-C. Egbide, et al., Rotating and savings credit association (RoSCAs): averitable
tool for enhancing the performance of micro and small enterprises in nigeria, Asian
Economic and Financial Review 10 (2) (2020) 189–199 .

[33] M. El-Gamal, M. El-Komi, D. Karlan, A. Osman, Bank-insured RoSCA for microﬁ-
nance: experimental evidence in poor Egyptian villages, Journal of Economic Be-
havior & Organization 103 (2014) S56–S73 .

[34] Ş . Ero ğlu, Informal ﬁnance and the urban poor: an investigation of rotating savings

[60] S. Koike, M. Nakamaru, T. Otaka, H. Shimao, K.-I. Shimomura, T. Yamato, Reci-
procity and exclusion in informal ﬁnancial institutions: an experimental study of
rotating savings and credit associations, PLoS ONE 13 (8) (2018) e0202878 .
[61] S. Koike, M. Nakamaru, M. Tsujimoto, Evolution of cooperation in rotating indi-

visible goods game, J. Theor. Biol. 264 (1) (2010) 143–153 .

[62] N. Kondo, J. Minai, H. Imai, Z. Yamagata, Engagement in a cohesive group and
higher-level functional capacity in older adults in japan: a case of the mujin, Social
Science & Medicine 64 (11) (2007) 2311–2323 .

[63] N. Kondo, K. Suzuki, J. Minai, Z. Yamagata, Positive and negative eﬀects of ﬁ-
nance-based social capital on incident functional disability and mortality: an 8-year
prospective study of elderly japanese, Journal of epidemiology 22 (6) (2012)
543–550 .

[64] M. Kshetrimayum, Rotating savings and credit associations: an important space for

social work practice, Indian J Soc Work 77 (3) (2016) 311–322 .

[65] J. Lappeman, J. Litkie, S. Bramdaw, A. Quibell, Exploring retail orientated rotat-
ing savings and credit associations: festive season ’stokvels’ in South Africa, The
International Review of Retail, Distribution and Consumer Research 30 (3) (2020)
331–358 .

[66] M. Larrabure, M. Vieta, D. Schugurensky, The ’new cooperativism’in Latin Amer-
ica: worker-recuperated enterprises and socialist production units, Studies in the
Education of Adults 43 (2) (2011) 181–196 .

[67] M. Le Polain, O. Sterck, M. Nyssens, Interest rates in savings groups: thrift or threat?

World Dev 101 (2018) 162–172 .

and credit associations in turkey, J Soc Policy 39 (3) (2010) 461–481 .

[68] R. Leonardi, R.Y. Nanetti, R.D. Putnam, Making democracy work: Civic traditions

[35] A. Etang, D. Fielding, S. Knowles, Trust and rosca membership in rural cameroon,

in modern Italy, Princeton University Press Princeton, NJ, USA, 2001 .

J Int Dev 23 (4) (2011) 461–475 .

[36] D.M. Fessler, Windfall and socially distributed willpower: the psychocultural dy-
namics of rotating savings and credit associations in a bengkulu village, Ethos 30
(1–2) (2002) 25–48 .

[37] P. Francois, M. Squires, Linking mobile money networks to ”e-RoSCA ”: an experi-

mental study, Sci Adv 7 (1) (2021) eabc5831 .

[38] C. Geertz, The rotating credit association: a ”middle rung ” in development, Econ

Dev Cult Change 10 (3) (1962) 241–263 .

[39] S. Ghazali, Kut (informal rotating credit) in the livelihood strategies of urban house-

holds in penang, malaysia, Area 35 (2) (2003) 183–194 .

[40] J. Goedecke, I. Guérin, B. d’Espallier, G. Venkatasubramanian, Why do ﬁnancial
inclusion policies fail in mobilizing savings from the poor? lessons from rural south
india, Development Policy Review 36 (2018) O201–O219 .

[41] M.K. Gugerty, You can’t save alone: commitment in rotating savings and credit

associations in kenya, Econ Dev Cult Change 55 (2) (2007) 251–282 .

[42] S. Han, Q. Zhang, L. Liu, The risk management mechanism of China’s bidding ro-
tating savings and credit association: a case study of chengnan village in wenzhou,
Emerging Markets Finance and Trade 56 (13) (2020) 3095–3105 .

[43] K. Hansen, J.J. Kim, S. Suﬃan, K. Mehta, Leveraging informal lending mechanisms
to facilitate technology transfer and microenterprise in developing countries, Tech-
nol Soc 41 (2015) 65–75 .

[44] H.A.A.B. Hoque, M.B. Khalily, ROSCAs and ASCRAs in Bangladesh: implications
for ﬁnancial market development, Savings and Development (2002) 395–418 .
[45] M.  Hossain,  Credit  for  Alleviation  of  Rural  Poverty:  The  Grameen  Bank  in

Bangladesh, volume 65, Intl Food Policy Res Inst, 1988 .

[46] C.S. Hossein, Fringe banking in canada: a study of rotating savings and credit as-
sociations (roscas) in toronto’s inner suburbs, Canadian Journal of Nonproﬁt and
Social Economy Research 8 (1) (2017) 29 .

[47] H. Ibrahim, Do institutions matter? the persistence of ROSCAs among immigrants
in developed economies, Journal of Enterprising Communities: People and Places
in the Global Economy (2019) .

[48] H. Ibrahim, Structured savings and asset ownership: the role of rotating savings
and credit associations among african immigrants in the united states, J. Soc. &
Soc. Welfare 47 (2020) 29 .

[49] D. Imami, K. Rama, A. Polese, Informality and access to ﬁnance during socialism
and transition–the case of the rotating savings and credit schemes, Journal of Evo-
lutionary Economics 30 (5) (2020) 1367–1383 .

[50] S. Johnson, Gender norms in ﬁnancial markets: evidence from kenya, World Dev

32 (8) (2004) 1355–1374 .

[51] M.Y. Joshi, J. Flacke, N. Schwarz, Do microﬁnance institutes help slum-dwellers
in coping with frequent disasters? an agent-based modelling study, Int. J. Disaster
Risk Reduct. 49 (2020) 101627 .

[52] K. Kan, Informal capital sources and household investment: evidence from taiwan,

J Dev Econ 62 (1) (2000) 209–232 .

[53] S. Kaur, S. Srivastav, A. Tyagi, Impact of using rosca on women empowerment
(with reference to delhi NCR), in: 2021 9th International Conference on Reliability,
Infocom Technologies and Optimization (Trends and Future Directions)(ICRITO),
IEEE, 2021, pp. 1–5 .

[54] R. Ke, M. Ye, The practice of rotating saving and credit associations and interest

[69] A.R.  Levenson,  T.  Besley,  The  anatomy  of  an  informal  ﬁnancial  mar-
ket:  ROSCA  participation  in  Taiwan,  J  Dev  Econ  51  (1)  (1996)  45–68,
doi: 10.1016/S0304-3878(96)00425-7 . Interamerican Seminar on Macroeconomics
[70] B. Linkow, L. Rentschler, Fraying of the ties that bind: community-level ﬁnancial
institutions and hiv/aids with evidence from kwazulu-natal, south africa, J Afr Econ
(2016) 1–21 .

[71] L. Martin, S. Goldman, O. Jiménez, The tanda: a practice at the intersection of
mathematics, culture, and ﬁnancial goals, Mind, Culture, and Activity 16 (4) (2009)
338–352 .

[72] K. McNabb, P. LeMay-Boucher, J. Bonan, Enforcement problems in roscas: evi-
dence from benin, The European Journal of Development Research 31 (5) (2019)
1389–1415 .

[73] H. Mehmood, T. Ahmad, L. Razaq, S. Mare, M.Z. Usmani, R. Anderson, A.A. Raza,
Towards digitization of collaborative savings among low-income groups, Proceed-
ings of the ACM on Human-Computer Interaction 3 (CSCW) (2019) 1–30 .
[74] G. Mianda, Francophone sub-Saharan African immigrants organizing tontines in
toronto: a basis for solidarity and integration, Can Ethn Stud 52 (3) (2020) 7–26 .
[75] M.S. Mohieldin, P.W. Wright, Formal and informal credit markets in Egypt, Econ

Dev Cult Change 48 (3) (2000) 657–670 .

[76] M. Onda, Rotating savings and credit associations as traditional mutual help net-
works in east asia, International Journal of Asian Studies 18 (2) (2021) 271–287 .
[77] I. Onoyere, An investigation of activities of microﬁnance banks as a veritable tool
for reducing poverty and unemployment in developing economies. the evidence
from nigeria, Mediterr J Soc Sci 5 (6) (2014) 99 .

[78] T. Oraro, K. Wyss, How does membership in local savings groups inﬂuence the de-
terminants of national health insurance demand? a cross-sectional study in kisumu,
kenya, Int J Equity Health 17 (1) (2018) 1–9 .

[79] L.P. Pardo-Martínez, M.V. Huertas de Mora, La historia del cooperativismo en
colombia: hitos y periodos, Cooperativismo & Desarrollo 22 (104) (2014) .
[80] K. Raccanello, J. Anand, P.A. Martínez, Social capital as an incentive for partici-
pation and formation of women-dominant Rosca, Economic Development, Integra-
tion, and Morality in Asia and the Americas, Emerald Group Publishing Limited,
2009 .

[81] F. Reito, Roscas without sanctions, Rev Soc Econ 78 (4) (2020) 561–579 .
[82] F. Reito, S. Spagano, A comparison between formal and informal mutual-credit

arrangements, Dev Econ 52 (2) (2014) 179–201 .

[83] C. Rogers, Financing rural enterprise: the use of rotating credit by a village com-

munity in nepal, Savings and Development (2006) 109–130 .

[84] E.J. Ryu, A. Suzuki, Roscas as insurance: comparing formal and informal methods
of saving among the unskilled workers in the ethiopian cut-ﬂower industry, Dev
Econ 59 (3) (2021) 243–274 .

[85] S.K. Sadr, The optimum size of rotating Qard Hasan savings and credit associations,

ISRA International Journal of Islamic Finance (2017) .

[86] E.B. Satkunasingam, B. Shanmugam, Underground banking in Malaysia: a case

study of ROSCAs, Journal of Money Laundering Control (2006) .

[87] K. Sato, N. Kondo, K. Kondo, Rotating savings and credit association, its members’
diversity, and higher-level functional capacity: a 3-year prospective study from the
japan gerontological evaluation study, Geriatrics & gerontology international 19
(12) (2019) 1268–1274 .

11

A.F. Zambrano, L.F. Giraldo, M.T. Perdomo et al.

World Development Sustainability 3 (2023) 100081

[88] U. Scholten, Rotating savings and credit associations in developed countries: the

german–austrian bausparkassen, J Comp Econ 28 (2) (2000) 340–363 .

[89] A.K. Sedai, R. Vasudevan, A. Alves Pena, Friends and beneﬁts? endogenous ro-
tating savings and credit associations as alternative for women’s empowerment
in india, World Dev 145 (2021) 105515, doi: 10.1016/j.worlddev.2021.105515 .
https://www.sciencedirect.com/science/article/pii/S0305750X21001273
[90] A.O. Shem, H.J. Rösner, Savings institutions that count for small and micro enter-
prises: the case of urban Kenya, African Review of Money Finance and Banking
(2003) 23–46 .

[91] A. Shoaib, M.A. Siddiqui, Why do people participate in rosca saving schemes? ﬁnd-

ings from a qualitative empirical study, Decision 47 (2) (2020) 177–189 .

[92] Z. Sijia, M. Horita, Reciprocity and rule preferences of a rotating savings and
credit association (ROSCA) in China: evolutionary simulation in imitation games,
in: International Conference on Group Decision and Negotiation, Springer, 2019,
pp. 43–56 .

[93] P. Smets, Roscas as a source of housing ﬁnance for the urban poor: an analysis of
self-help practices from Hyderabad, India, Community Dev J 35 (1) (2000) 16–30 .
[94] P. Smets, Indian community-based housing ﬁnance systems: potentials and pitfalls
for urban development and housing improvement, International Journal of Urban
Sciences 23 (4) (2019) 586–600 .

[95] J.P. Stodder, P. Schroth, Barriers to transparency: growth, and the growth of cor-
ruption, in: IEMC’03 Proceedings. Managing Technologically Driven Organizations:
The Human Side of Innovation and Change, IEEE, 2003, pp. 556–560 .

[96] D. Stoesz, I. Gutau, R. Rodreiguez, SUSU: captalizing development from the bottom

up, J. Soc. & Soc. Welfare 43 (2016) 121 .

[97] B.W. Stoﬄe, T. Purcell, R.W. Stoﬄe, K. Van Vlack, K. Arnett, J. Minnis, Credit,
identity, and resilience in the Bahamas and Barbados, Ethnology 48 (1) (2009)
71–84 .

[98] A.C. Tricco, E. Lillie, W. Zarin, K.K. O’Brien, H. Colquhoun, D. Levac, D. Moher,
M.D. Peters, T. Horsley, L. Weeks, et al., PRISMA extension for scoping reviews
(PRISMA-ScR): checklist and explanation, Ann. Intern. Med. 169 (7) (2018) 467–
473, doi: 10.7326/M18-0850 . PMID: 30178033

[99] K.S. Tsai, Banquet banking: gender and rotating savings and credit associations in

south China, China Q 161 (2000) 142–170 .

[100] M. Tsujimoto, The economic adaptation of migrants and the cooperative behavior
by generalized exchange: the rotating credit association of Japanese migrants in
buenos aires, Japanese Journal of Social Psychology 16 (2000) 50–63 .

[101] M. Tsujimoto, Rotating credit associations of the japanese in argentina: economic
adaptation by generalized exchange, Japanese Journal of Qualitative Research in
Psychology 5 (2006) 165–179 .

[102] M. Tsujimoto, M. Kuniyoshi, I. Yokuda, The genesis of resource exchange: a study
of rotating savings and credit associations in the Okinawa islands, The Japanese
Journal of Social Psychology (2007) .

[103] M.S. Ullah, N. Naiimi, R. Mohd Yusof, Are small and medium enterprises (SMEs)
in lahore failing at the rate suggested in prior studies? an analysis of the degree
of ﬁnancial stress on small and medium enterprises and its impact on their life
expectancy, International Business Management 10 (18) (2016) 4258–4267 .
[104] M.S. Ullah, N. Naiimi, R. Mohd Yusof, The impact of entrepreneurs’ levels of edu-
cation, age and years in business on their decision to obtain ﬁnance for small and
medium enterprises (SMEs) from rotating savings and credit associations (ROSCAs)
in lahore, The Social Sciences 11 (13) (2016) 3252–3256 .

[105] M.S. Ullah, N. Naiimi, R. Mohd Yusof, What size of opportunity will open to banks
that penetrate the small and medium enterprise (SME) ﬁnance market at lahore?
the next great challenge for enterprising banks, The Social Sciences 11 (13) (2016)
3245–3251 .

[106] UNDP (United Nations Development Programme), 2021 Global multidimensional
poverty index (MPI), UNDP (United Nations Development Programme) (2021) .
http://hdr.undp.org/en/2021-MPI

[107] H.G. Villasanti, L.F. Giraldo, K.M. Passino, Feedback control engineering for coop-
erative community development: tools for ﬁnancial management advice for low-in-
come individuals, IEEE Control Syst. Mag. 38 (3) (2018) 87–101 .

[108] H.G. Villasanti, K.M. Passino, Feedback controllers as ﬁnancial advisors for low-in-

come individuals, IEEE Trans. Control Syst. Technol. 25 (6) (2016) 2194–2201 .

[109] R. Vokes, D. Mills, ’Time for school’? School fees, savings clubs and social reci-
procity in uganda, Journal of Eastern African Studies 9 (2) (2015) 326–342 .
[110] A.N.M. Wahid, The grameen bank and poverty alleviation in bangladesh: theory,
evidence and limitations theory, evidence and limitations, Am J Econ Sociol 53 (1)
(1994) 1–15 .

[111] A. Wambua, P.K. Wamuyu, Role of mobile applications in mitigating challenges
faced by informal saving groups, in: 2020 IST-Africa Conference (IST-Africa), IEEE,
2020, pp. 1–11 .

[112] G.A. Yimer, W. Decock, M.G. Ghebregergs, G.H. Abera, G.S. Halibo, The inter-
play between oﬃcial and unoﬃcial laws in rotating savings and credit associations
(Eqqub) in Tigray, Ethiopia, The Journal of Legal Pluralism and Unoﬃcial Law 50
(1) (2018) 94–113 .

[113] A.F. Zambrano, G. Díaz-García, S. Ramírez, L.F. Giraldo, H. Gonzalez-Villasanti,
M.T. Perdomo, I.D. Hernández, J.M. Godoy, Donation networks in underprivileged
communities, IEEE Trans. Comput. Social Syst. 8 (1) (2020) 76–85 .

[114] A.F. Zambrano, L.F. Giraldo, M.T. Perdomo, I.D. Hernández, J.M. Godoy, Variations
of rotating savings and credit associations for community development, IEEE Trans.
Comput. Social Syst. (2022) 1–9 .

[115] D. Zeitlyn, The talk goes outside: argument, privacy and power in mambila society

towards a sociology of embedded praxis, Africa 73 (4) (2003) 606–622 .

[116] D.A. Zelenova, V.V. Kruchinsky, An economy of miracle: rotating credit and savings
associations in townships of Johannesburg, Etnograﬁcheskoe obozrenie 2019 (2)
(2019) 78–97 .

12

